#!/usr/bin/env python3
"""Steadfold motion kit: author a Reel as beat-timed scenes with transitions, render it frame by frame with
Playwright (2x, Lanczos down), add sub-frame motion blur on fast moves, post effects (glitch, pixelate),
cut to the music's tempo and mux with a soft instrument bed. See README.md.

    from kit import Reel, el, words, svg
    r = Reel("hb-reel-...", "hourback", bpm=108, css=CSS)
    r.scene(2, html, tin="whipL")          # length in beats; first scene is the hook (frame 0)
    r.loop()                                # ends on the hook layout again
    r.build(out_mp4, music_mp3)
"""
import glob
import io
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
from multiprocessing import Process
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
W, H, FPS = 1080, 1920, 30
CHROME = (glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome") or glob.glob("/opt/pw-browsers/chromium*/chrome-linux/chrome"))[0]

BRANDS = {
    "littlefold": dict(name="Littlefold", mark="littlefold.png", bg="#FFF4E0", ink="#2C2A3A", acc="#D9497A", acc2="#FF8A70",
                       pink="#FFD6E3", peach="#FFD3AE", butter="#FFE27E", deep="#7A2149"),
    "fullyfunded": dict(name="Fully Funded", mark="fullyfunded.png", bg="#F5F7FF", ink="#0E1440", acc="#FF6A3D", acc2="#FFB08F",
                        main="#2B3FE0", deep="#16206B", cream="#F7F1E5"),
    "lockedhour": dict(name="Locked Hour", mark="lockedhour.png", bg="#FFE27A", ink="#141414", acc="#FF5CA8", acc2="#E8336F",
                       hl="#FFD43B", cream="#FFF4E0"),
    "hourback": dict(name="Hourback", mark="hourback.png", bg="#FFF8EF", ink="#2A2238", acc="#FFC94D", acc2="#FF8A3D",
                     main="#5E54C9", plum="#3A2240", peach="#FFE6D3"),
}

FONTS = f"""
@font-face{{font-family:'Instrument Serif';src:url('{(REPO / "assets/inbox/InstrumentSerif-Regular.ttf").as_uri()}')}}
@font-face{{font-family:'Instrument Serif';font-style:italic;src:url('{(REPO / "assets/inbox/InstrumentSerif-Italic.ttf").as_uri()}')}}
@font-face{{font-family:'Caveat Brush';src:url('{(REPO / "assets/fonts/CaveatBrush-Regular.ttf").as_uri()}')}}
@font-face{{font-family:'Caveat';src:url('{(REPO / "assets/fonts/Caveat-Variable.ttf").as_uri()}')}}
@font-face{{font-family:'Fraunces';src:url('{(REPO / "assets/fonts/Fraunces-Variable.ttf").as_uri()}')}}
"""

BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:var(--stage)}
#stage{position:absolute;inset:0;overflow:hidden}
.scene{position:absolute;inset:0;overflow:hidden;display:none}
.cam{position:absolute;inset:0;transform-origin:50% 45%}
.par{position:absolute;inset:-6%;background-size:cover;background-position:center}
.el{position:absolute}
.c{left:0;width:1080px;text-align:center}
.el[style*="width:1080px;text-align:center"]{padding-left:70px;padding-right:70px}
.w{display:inline-block}
.chip{position:absolute;display:flex;align-items:center;gap:12px;border-radius:999px;padding:6px 22px 6px 6px;font:700 28px/1 Inter}
.chip img{width:46px;height:46px;border-radius:50%;background:#fff}
.sk{position:absolute;left:-2%;top:52%;height:.12em;width:0;border-radius:.06em}
.strike{position:relative;display:inline-block}
.emo{font-family:'Noto Color Emoji';line-height:1}
svg{overflow:visible}
"""


def asset(name):
    return (HERE / "assets" / name).as_uri()


def el(html, x=0, y=0, w=None, a="up", t=0.0, d=0.4, cls="", style="", r=0, loop=None, amp=None, **data):
    """One positioned element. x='c' centres it across the frame. a = entrance animation (see motion.js)."""
    pos = "left:0;width:1080px;text-align:center;" if x == "c" else f"left:{x}px;" + (f"width:{w}px;" if w else "")
    attrs = f'data-a="{a}" data-t="{t:.3f}" data-d="{d}"'
    if r:
        attrs += f' data-r="{r}"'
    if loop:
        attrs += f' data-loop="{loop}"'
    if amp is not None:
        attrs += f' data-amp="{amp}"'
    for k, v in data.items():
        attrs += f' data-{k}="{v}"'
    return f'<div class="el {cls}" style="{pos}top:{y}px;{style}" {attrs}>{html}</div>'


def words(text, x="c", y=0, w=None, t=0.0, gap=0.11, d=0.32, cls="", style="", em_cls="em", r=0):
    """Kinetic caption: each word pops in on its own. *word* gets the accent class; '/' forces a line break."""
    out, on = [], False
    for tok in text.split(" "):
        if tok == "/":
            out.append("<br>")
            continue
        start = tok.startswith("*")
        core = tok.replace("*", "")
        if start:
            on = True
        out.append(f'<span class="w {em_cls}">{core}</span>' if on else f'<span class="w">{core}</span>')
        if tok.rstrip(".,?!:;").endswith("*") or tok.endswith("*"):
            on = False
    return el(" ".join(out), x, y, w, a="words", t=t, d=d, cls=cls, style=style, r=r, gap=gap)


def emoji(ch, x, y, size=160, a="pop", t=0.0, d=0.4, r=0, loop=None, amp=None):
    return el(f'<span class="emo" style="font-size:{size}px">{ch}</span>', x, y, a=a, t=t, d=d, r=r, loop=loop, amp=amp)


def img(name, x, y, w, a="pop", t=0.0, d=0.45, r=0, loop="float", shadow=True, amp=None):
    sh = "filter:drop-shadow(0 26px 30px rgba(0,0,0,.22)) drop-shadow(0 6px 8px rgba(0,0,0,.12));" if shadow else ""
    return el(f'<img src="{asset(name)}" style="width:{w}px;display:block;{sh}">', x, y, a=a, t=t, d=d, r=r, loop=loop, amp=amp)


def chip(brand, x=84, y=300, bg="#fff", ink=None, a="fade", t=0.0):
    b = BRANDS[brand]
    return el(f'<div class="chip" style="position:static;display:inline-flex;background:{bg};color:{ink or b["ink"]}"><img src="{asset(b["mark"])}">{b["name"]}</div>',
              x, y, a=a, t=t, d=0.3)


def ring(cx, cy, r, color, width=26, t=0.0, d=0.6, rot=-90):
    """A circle that draws itself (timer rings, circled answers)."""
    return (f'<svg class="el" style="left:0;top:0;width:1080px;height:1920px" viewBox="0 0 1080 1920">'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" '
            f'transform="rotate({rot} {cx} {cy})" data-a="draw" data-t="{t}" data-d="{d}"/></svg>')


def scribble_circle(cx, cy, rx, ry, color, width=12, t=0.0, d=0.45):
    """Hand-drawn loop around something (marker annotation)."""
    pts = []
    for k in range(0, 112):
        a = -2.2 + k / 100 * 2 * math.pi
        wob = 1 + 0.035 * math.sin(k * 0.7)
        pts.append(f"{cx + rx * wob * math.cos(a):.1f},{cy + ry * wob * math.sin(a) + k * 0.25:.1f}")
    return (f'<svg class="el" style="left:0;top:0;width:1080px;height:1920px" viewBox="0 0 1080 1920">'
            f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" '
            f'stroke-linejoin="round" data-a="draw" data-t="{t}" data-d="{d}"/></svg>')


def arrow(x1, y1, x2, y2, color, width=10, t=0.0, d=0.35, bend=60):
    mx, my = (x1 + x2) / 2 + bend, (y1 + y2) / 2 - bend
    ang = math.atan2(y2 - my, x2 - mx)
    hx1, hy1 = x2 - 40 * math.cos(ang - 0.5), y2 - 40 * math.sin(ang - 0.5)
    hx2, hy2 = x2 - 40 * math.cos(ang + 0.5), y2 - 40 * math.sin(ang + 0.5)
    return (f'<svg class="el" style="left:0;top:0;width:1080px;height:1920px" viewBox="0 0 1080 1920"><g fill="none" stroke="{color}" '
            f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{x1},{y1} Q{mx},{my} {x2},{y2}" data-a="draw" data-t="{t}" data-d="{d}"/>'
            f'<path d="M{hx1:.1f},{hy1:.1f} L{x2},{y2} L{hx2:.1f},{hy2:.1f}" data-a="draw" data-t="{t + d * 0.8:.3f}" data-d="0.15"/></g></svg>')


class Reel:
    def __init__(self, rid, brand, bpm, css="", stage=None, beat_offset=0.0):
        self.rid, self.brand, self.bpm = rid, brand, bpm
        self.beat = 60.0 / bpm
        self.css = css
        self.stage = stage or BRANDS[brand]["bg"]
        self.scenes = []        # dict(start, dur, html, tin, cam, bg)
        self.t = beat_offset
        self.shakes, self.blur_spans = [], []

    def scene(self, beats, html, tin="cut", td=None, cam="push", bg=None, focus=None, color=None, color2=None, color3=None,
              shake=None, cls=""):
        dur = beats * self.beat
        tr = None
        if self.scenes:
            tr = dict(type=tin, d=td if td is not None else min(0.36, self.beat * 0.6), focus=focus, color=color, color2=color2, color3=color3)
            if tin == "cut":
                tr["d"] = 1 / FPS
        self.scenes.append(dict(start=round(self.t, 4), dur=dur, html=html, tin=tr, cam=cam, bg=bg or self.stage, cls=cls))
        if shake:
            self.shakes.append([len(self.scenes) - 1, shake[0], shake[1], shake[2]])
        self.t += dur
        return self

    def loop(self, beats=1.5, tin="zoom", **kw):
        """Close on the hook scene again so the last frame flows into frame 0."""
        s0 = self.scenes[0]
        return self.scene(beats, s0["html"], tin=tin, cam=s0["cam"], bg=s0["bg"], cls=s0["cls"], **kw)

    def stretch(self, target=12.6):
        """Add half beats to the wordiest scenes (never the hook) until the Reel is at least `target` s."""
        import re as _re
        wc = lambda h: len(_re.findall(r'class="w', h)) + len(_re.sub(r"<[^>]+>", " ", h).split()) // 3  # noqa: E731
        k = 0
        order = sorted(range(1, len(self.scenes)), key=lambda i: -wc(self.scenes[i]["html"]))
        while self.duration < target and order:
            self.scenes[order[k % len(order)]]["dur"] += 0.5 * self.beat
            k += 1
            t = self.scenes[0]["start"]
            for sc in self.scenes:
                sc["start"] = round(t, 4)
                t += sc["dur"]
            self.t = t
        return self

    @property
    def duration(self):
        return self.t

    def cuts(self):
        return [s["start"] for s in self.scenes[1:]]

    def html(self):
        shakes = [[self.scenes[i]["start"] + t0, d, a] for i, t0, d, a in self.shakes]
        tl = dict(scenes=[dict(start=s["start"], dur=s["dur"], tin=s["tin"], cam=s["cam"]) for s in self.scenes],
                  shakes=shakes, blurSpans=self.blur_spans)
        body = "".join(f'<div class="scene {s["cls"]}" style="background:{s["bg"]}"><div class="cam">{s["html"]}</div></div>'
                       for s in self.scenes)
        js = (HERE / "motion.js").read_text()
        return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}{BASE_CSS}:root{{--stage:{self.stage}}}{self.css}</style>"
                f"</head><body><div id='stage'>{body}<div id='ov'></div></div><script>{js}</script>"
                f"<script>motionInit({json.dumps(tl)});</script></body></html>")


# =============================================================================================== rendering
def _post(im, post, fi):
    if not post:
        return im
    if post.get("pixel"):
        s = max(2, int(post["pixel"]))
        small = im.resize((max(1, W // s), max(1, H // s)), Image.BILINEAR)
        return small.resize((W, H), Image.NEAREST)
    if post.get("glitch"):
        a = float(post["glitch"])
        arr = np.asarray(im).copy()
        rng = np.random.default_rng(1000 + int(post.get("seed", fi)))
        y = 0
        while y < H:
            hgt = int(rng.integers(30, 220))
            if rng.random() < 0.55:
                arr[y:y + hgt] = np.roll(arr[y:y + hgt], int(rng.integers(-1, 2) * a * rng.integers(40, 180)), axis=1)
            y += hgt
        sh = int(22 * a)
        out = arr.copy()
        out[..., 0] = np.roll(arr[..., 0], sh, axis=1)
        out[..., 2] = np.roll(arr[..., 2], -sh, axis=1)
        return Image.fromarray(out)
    return im


def _worker(html_path, frames, outdir, dsf):
    from playwright.sync_api import sync_playwright
    url = Path(html_path).as_uri()
    with sync_playwright() as p:
        state = {}

        def fresh():
            if state.get("b"):
                try:
                    state["b"].close()
                except Exception:
                    pass
            b = p.chromium.launch(executable_path=CHROME, args=["--disable-gpu", "--font-render-hinting=none"])
            pages = []
            for scale in (dsf, 1):  # full-quality page + a 1x page for blur sub-frames
                pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=scale)
                pg.goto(url)
                pg.wait_for_timeout(300)
                pg.evaluate("document.fonts.ready")
                pages.append(pg)
            state.update(b=b, hi=pages[0], lo=pages[1], n=0)

        def shot(t, page):
            r = page.evaluate(f"seek({t:.5f})")
            raw = Image.open(io.BytesIO(page.screenshot(type="jpeg", quality=96))).convert("RGB")
            if raw.size != (W, H):
                raw = raw.resize((W, H), Image.LANCZOS)
            state["n"] += 1
            return raw, r

        def frame(fi):
            t = fi / FPS
            r = state["hi"].evaluate(f"seek({t:.5f})")
            n = int(r.get("blur", 1))
            if n > 1:  # sub-frame motion blur: average 2n samples (8-12) across a 0.8-frame shutter (blurred, so 1x is enough)
                n = 2 * n
                acc = np.zeros((H, W, 3), np.float32)
                for k in range(n):
                    off = (-0.4 + 0.8 * k / (n - 1)) / FPS
                    sub, _ = shot(max(0.0, t + off), state["lo"])
                    acc += np.asarray(sub, np.float32)
                im = Image.fromarray(np.clip(acc / n + 0.5, 0, 255).astype(np.uint8))
            else:
                im, r = shot(t, state["hi"])
            return _post(im, r.get("post"), fi)

        fresh()
        for fi in frames:
            if state["n"] > 120:  # Chromium grows with every screenshot; recycle before it runs out of memory
                fresh()
            for attempt in range(3):
                try:
                    im = frame(fi)
                    break
                except Exception as e:  # renderer crashed: restart and redo this frame
                    print(f"frame {fi}: {str(e)[:80]} -> restart", flush=True)
                    fresh()
            im.save(f"{outdir}/{fi:05d}.png", compress_level=1)
        state["b"].close()


def render_frames(reel, workdir, dsf=2, workers=1, only=None):
    workdir = Path(workdir)
    workdir.mkdir(parents=True, exist_ok=True)
    html_path = workdir / f"{reel.rid}.html"
    html_path.write_text(reel.html())
    n = int(round(reel.duration * FPS))
    frames = only if only is not None else list(range(n))
    fdir = workdir / "frames"
    if only is None and fdir.exists():
        shutil.rmtree(fdir)
    fdir.mkdir(exist_ok=True)
    chunks = [frames[i::workers] for i in range(workers)]
    ps = [Process(target=_worker, args=(str(html_path), c, str(fdir), dsf)) for c in chunks if c]
    [p.start() for p in ps]
    [p.join() for p in ps]
    return fdir, n


def encode(fdir, n, music, out, bpm=None, fade=1.4, crf=19):
    dur = n / FPS
    tmp = Path(out).with_suffix(".silent.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", f"{fdir}/%05d.png", "-frames:v", str(n),
                    "-c:v", "libx264", "-preset", "slow", "-crf", str(crf), "-maxrate", "9M", "-bufsize", "18M",
                    "-pix_fmt", "yuv420p", "-profile:v", "high", "-g", "30", str(tmp)], check=True)
    af = (f"atrim=0:{dur:.3f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.04,afade=t=out:st={dur - fade:.3f}:d={fade},"
          f"lowpass=f=9500,alimiter=limit=0.89")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(tmp), "-stream_loop", "-1", "-i", str(music), "-filter_complex",
                    f"[1:a]{af}[a]", "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-ar", "44100",
                    "-shortest", "-movflags", "+faststart", str(out)], check=True)
    tmp.unlink()
    master_audio(out)


def probe(path):
    j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration,size:stream=codec_name,width,height,r_frame_rate",
                                   "-of", "json", str(path)], capture_output=True, text=True).stdout)
    v = [s for s in j["streams"] if s.get("width")][0]
    a = [s for s in j["streams"] if not s.get("width")]
    return dict(w=v["width"], h=v["height"], vcodec=v["codec_name"], fps=v["r_frame_rate"], acodec=a[0]["codec_name"] if a else None,
                dur=float(j["format"]["duration"]), mb=int(j["format"]["size"]) / 1e6)


def loudness(path):
    r = subprocess.run(["ffmpeg", "-nostats", "-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    tail = r[r.rfind("Summary"):]
    get = lambda key: float(tail.split(key)[1].split()[0]) if key in tail else None  # noqa: E731
    return dict(I=get("I:"), peak=get("Peak:"))


def sheet(fdir, times, out, cols=8, scale=0.2):
    """QA contact sheet from rendered frames at the given times (s)."""
    from PIL import ImageDraw
    ims = []
    for t in times:
        f = Path(fdir) / f"{int(round(t * FPS)):05d}.png"
        if f.exists():
            im = Image.open(f).convert("RGB").resize((int(W * scale), int(H * scale)), Image.LANCZOS)
            ImageDraw.Draw(im).text((6, 6), f"{t:.2f}s", fill=(255, 0, 0))
            ims.append(im)
    if not ims:
        return
    rows = math.ceil(len(ims) / cols)
    sh = Image.new("RGB", (cols * ims[0].width, rows * ims[0].height), "black")
    for k, im in enumerate(ims):
        sh.paste(im, ((k % cols) * im.width, (k // cols) * im.height))
    sh.save(out, quality=88)


def qa_times(reel):
    ts = [0.0] + [float(s) for s in range(1, int(reel.duration) + 1)]
    for c in reel.cuts():
        ts += [c - 0.1, c, c + 0.1]
    return sorted(set(round(min(max(0, x), reel.duration - 1 / FPS), 3) for x in ts))


def overflow_check(reel, margin=30):
    """Flag any text that leaves the frame (x < margin or x > 1080 - margin) at the middle and end of each scene."""
    from playwright.sync_api import sync_playwright
    import tempfile as _tf
    js = """(m) => { const out = [];
      document.querySelectorAll('.scene').forEach((sc, i) => { if (sc.style.display !== 'block') return;
        const tw = document.createTreeWalker(sc, NodeFilter.SHOW_TEXT); let n;
        while ((n = tw.nextNode())) { if (!n.textContent.trim()) continue;
          const rg = document.createRange(); rg.selectNodeContents(n);
          for (const r of rg.getClientRects()) { if (r.width < 2) continue;
            let op = 1, el = n.parentElement; while (el && el !== sc) { op *= +getComputedStyle(el).opacity; el = el.parentElement; }
            if (op < 0.1) continue;
            if (r.left < m || r.right > 1080 - m) out.push([i, n.textContent.trim().slice(0, 40), Math.round(r.left), Math.round(r.right)]); } } });
      return out; }"""
    with _tf.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(reel.html())
    bad = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto(Path(f.name).as_uri())
        pg.wait_for_timeout(300)
        for s in reel.scenes:
            for t in (s["start"] + s["dur"] * 0.6, s["start"] + s["dur"] - 0.2):
                pg.evaluate(f"seek({t:.4f})")
                bad += [(round(t, 2), *x) for x in pg.evaluate(js, margin)]
        b.close()
    os.unlink(f.name)
    return bad


def master_audio(mp4, target=-14.0, limit_db=-1.6):
    """Bring the Reel's audio to the house loudness (tools/music_check.py: -14 LUFS +/- 1, true peak <= -1 dBTP), video untouched."""
    mp4 = Path(mp4)
    for _ in range(3):
        lu = loudness(mp4)
        if lu["I"] is not None and abs(lu["I"] - target) <= 0.4 and (lu["peak"] or 0) <= -1.2:
            return lu
        gain = target - (lu["I"] or target)
        tmp = mp4.with_suffix(".m.mp4")
        lim = 10 ** (limit_db / 20)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(mp4), "-map", "0:v", "-map", "0:a", "-c:v", "copy",
                        "-af", f"volume={gain + 0.15:.2f}dB,alimiter=limit={lim:.3f}:attack=3:release=60:level=disabled",
                        "-c:a", "aac", "-b:a", "160k", "-ar", "44100", "-movflags", "+faststart", str(tmp)], check=True)
        tmp.replace(mp4)
    return loudness(mp4)

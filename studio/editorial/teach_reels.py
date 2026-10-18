#!/usr/bin/env python3
"""§13 teaching Reels (Oct 17 pm): hook (frame 0 = cover) -> the move -> "because..." -> payoff ON the track's drop
-> "Do this:" -> save-line -> loop to the hook. 18-30 s (Deep dive 25-40 s). Same editorial look as §12 (boldkit/edkit),
same motion kit (studio/motion/kit.py: 2x frames, motion blur, transitions on every cut).

The payoff can sit anywhere: the music starts at an offset into the (loop-safe) v4 track so its measured drop lands exactly
on the payoff cut. Every cut stays on the track's quarter-beat grid.

    python3 studio/editorial/teach_reels.py <ids> [--plan] [--out DIR]
"""
import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "studio" / "motion"))
sys.path.insert(0, str(REPO / "studio" / "pivot"))
sys.path.insert(0, str(HERE))
import reels as RP  # noqa: E402
from boldkit import ED, FIELDS, beat_stamp, field_css, mark_txt  # noqa: E402
from kit import FPS, Reel, el, loudness, master_audio, probe, qa_times, read_need, render_frames, sheet  # noqa: E402
from PIL import Image  # noqa: E402

LIB = json.loads((REPO / "tools" / "music-library.json").read_text())["tracks"]


def track_len(f):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(REPO / f)],
                         capture_output=True, text=True).stdout
    return float(out.strip())


def rewrap(text, width=17):
    """Re-break a line into lines of <= width characters (pills split per line), so the action reads big on the card."""
    toks, on = [], False
    for w in text.replace(" / ", " ").split():
        if w.startswith("*"):
            on = True
        toks.append((w.replace("*", ""), on))
        if on and w.endswith("*"):
            on = False
    lines, cur = [], []
    for t in toks:
        if cur and len(" ".join(x for x, _ in cur + [t])) > width:
            lines.append(cur)
            cur = []
        cur.append(t)
    if cur:
        lines.append(cur)
    out = []
    for ln in lines:
        parts, run = [], []
        for w, p in ln:
            if p:
                run.append(w)
            else:
                if run:
                    parts.append("*" + " ".join(run) + "*")
                    run = []
                parts.append(w)
        if run:
            parts.append("*" + " ".join(run) + "*")
        out.append(" ".join(parts))
    return " / ".join(out)


def do_html(brand, sc):
    """'Do this:' beat: big handwritten label, the ONE action in serif with pills on a white ink-bordered card."""
    f = FIELDS[brand][sc["f"]]
    ink = f["ink"]
    lab = (f'<div data-a="pop" data-t="0" data-d="0.3" style="font-family:\'Caveat Brush\';font-size:150px;line-height:1;color:{ED.ACCENT[brand]};'
           f'transform:rotate(-4deg)">Do this:</div>')
    card = (f'<div data-a="fly" data-t="0.15" data-d="0.4" data-r="-1.5" style="background:#fff;border:5px solid {ink};border-radius:48px;'
            f'box-shadow:0 18px 0 {ink};padding:50px 46px;width:940px">'
            + RP.wtxt(rewrap(sc["text"], sc.get("chars", 16)), sc.get("size", 100), t=0.25, gap=0.07) + '</div>')
    return RP.col(lab + card, gap=36)


def save_html(brand, sc):
    f = FIELDS[brand][sc["f"]]
    inner = (f'<div data-a="pop" data-t="0" data-d="0.35" style="font-family:\'Caveat Brush\';font-size:{sc.get("size", 112)}px;line-height:1.02;'
             f'color:{ED.ACCENT[brand]};transform:rotate(-3deg);max-width:930px;text-align:center">{sc["text"].replace(" / ", "<br>")}</div>')
    if sc.get("next"):
        inner += (f'<div data-a="pop" data-t="0.35" data-d="0.3" class="T" style="font-size:78px;color:{f["ink"]};background:{f["p2"]};'
                  f'border:4px solid {f["ink"]};border-radius:999px;padding:16px 48px 24px;box-shadow:0 10px 0 {f["ink"]}">{mark_txt(sc["next"])}</div>')
    inner += RP.sticker_obj("ok" if brand != "hourback" else "point", 330, 0.2, "float")
    return RP.col(inner, gap=40)


def because_html(brand, sc):
    """'because…' beat: small handwritten 'because' kicker over the serif line."""
    k = (f'<div data-a="pop" data-t="0" data-d="0.25" style="font-family:\'Caveat Brush\';font-size:96px;line-height:1;'
         f'color:{ED.ACCENT[brand]};transform:rotate(-3deg)">{sc.get("kicker", "because…")}</div>')
    return RP.col(k + RP.wtxt(rewrap(sc["text"], sc.get("chars", 14)), sc.get("size", RP.SAY_PX[brand] - 30), t=0.2,
                              cw=RP.CW.get(brand, 0.5)), gap=34)


def scene_html(brand, sc):
    k = sc["k"]
    if k == "do":
        return RP.wrap(sc["f"], do_html(brand, sc) + beat_stamp(brand))
    if k == "save":
        return RP.wrap(sc["f"], save_html(brand, sc) + beat_stamp(brand))
    if k == "because":
        return RP.wrap(sc["f"], because_html(brand, sc) + beat_stamp(brand))
    return RP.scene_html(brand, sc)


def plan(spec):
    tr = LIB[spec["track"]]
    beat, drop = 60.0 / tr["bpm"], tr["drop_s"]
    q = 0.25
    htmls = [scene_html(spec["brand"], sc) for sc in spec["scenes"]]
    need = [max(sc.get("min", 1.5), math.ceil((read_need(h)[0] + 0.15 - 1e-3) / beat / q) * q) for sc, h in zip(spec["scenes"], htmls)]
    need[0] = max(need[0], math.ceil(2.4 / beat / q) * q)  # the hook holds long enough to read it AS the cover
    loop_beats = max(1.5, math.ceil((read_need(htmls[0])[0] - 1e-3) / beat / q) * q)
    lo, hi = (25.0, 40.0) if spec.get("fmt") == "deep" else (18.0, 30.0)
    total = (sum(need) + loop_beats) * beat
    k = 1
    while total < lo + 0.3:  # breathe: add half beats to the text beats after the hook
        need[k] += 0.5
        k = 1 + k % (len(need) - 1)
        total = (sum(need) + loop_beats) * beat
    if total > hi:
        raise SystemExit(f"{spec['id']}: {total:.2f}s is over {hi:.0f} s; cut words")
    di = next(i for i, sc in enumerate(spec["scenes"]) if sc.get("drop"))
    payoff_t = sum(need[:di]) * beat
    L = track_len(tr["file"])
    offset = (drop - payoff_t) % L  # music starts here so its drop lands on the payoff cut
    return htmls, need, loop_beats, beat, payoff_t, offset, total


def make(spec):
    brand = spec["brand"]
    tr = LIB[spec["track"]]
    htmls, need, loop_beats, beat, payoff_t, offset, total = plan(spec)
    r = Reel(spec["id"], brand, bpm=tr["bpm"], css=field_css(brand) + "\n.em.T{display:inline-block}",
             stage=FIELDS[brand][spec["scenes"][0]["f"]]["bg"])
    trans = RP.TRANS[brand]
    cams = ["push", "left", "rise", "push", "tilt", "right", "push"]
    for i, (sc, h, b) in enumerate(zip(spec["scenes"], htmls, need)):
        kw = dict(cam=cams[i % len(cams)], bg=FIELDS[brand][sc["f"]]["bg"])
        if i == 0:
            kw["shake"] = (0.12, 0.22, 16)
        else:
            t = sc.get("tin") or trans[(i - 1) % len(trans)]
            kw["tin"] = t
            if t in ("zoom", "iris", "blob"):
                kw["focus"] = (540, 820)
            if t in ("iris", "stripes", "blob"):
                cols = [v["bg"] for v in FIELDS[brand].values()]
                kw.update(color=cols[1 % len(cols)], color2=cols[2 % len(cols)], color3=cols[0])
            if sc.get("drop"):
                kw["shake"] = (0.0, 0.28, 24)
        r.scene(b, h, **kw)
    r.loop(loop_beats, tin="whipU" if brand != "hourback" else "pixel")
    r.music_offset = offset
    r.payoff_t = payoff_t
    return r


def encode(fdir, n, music, out, offset, fade=1.4):
    dur = n / FPS
    tmp = Path(out).with_suffix(".silent.mp4")
    # 18-40 s must stay under autopost's 19.5 MB: cap the video bitrate at 3.6 Mbps
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", f"{fdir}/%05d.png", "-frames:v", str(n),
                    "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-maxrate", "3600k", "-bufsize", "7200k",
                    "-pix_fmt", "yuv420p", "-profile:v", "high", "-g", "30", str(tmp)], check=True)
    af = (f"atrim=start={offset:.3f}:duration={dur:.3f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.04,"
          f"afade=t=out:st={dur - fade:.3f}:d={fade},lowpass=f=9500,alimiter=limit=0.89")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(tmp), "-stream_loop", "-1", "-i", str(music), "-filter_complex",
                    f"[1:a]{af}[a]", "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-ar", "44100",
                    "-shortest", "-movflags", "+faststart", str(out)], check=True)
    tmp.unlink()
    master_audio(out)


def report(spec):
    r = make(spec)
    tr = LIB[spec["track"]]
    print(f"{spec['id']}  track={spec['track']} bpm={tr['bpm']} drop={tr['drop_s']}  payoff@{r.payoff_t:.2f}s  music from {r.music_offset:.2f}s"
          f"  total={r.duration:.2f}s")
    for i, s in enumerate(r.scenes):
        need, nw = read_need(s["html"])
        print(f"  {i}: {s['start']:5.2f}s +{s['dur']:4.2f}  words={nw:2d} need={need:4.2f} {'OK' if s['dur'] + 1e-3 >= need else 'FAST'}")
    return r


def lint(spec):
    errs = []
    if sum(1 for s in spec["scenes"] if s["k"] == "do") != 1:
        errs.append("needs ONE do beat")
    if not any(s["k"] == "because" for s in spec["scenes"]):
        errs.append("needs a because beat")
    for i, s in enumerate(spec["scenes"]):
        t = " ".join(str(s.get(x, "")) for x in ("text", "label", "suf", "next")) + " " + " ".join(s.get("items", []) or [])
        n = len([w for w in re.sub(r"[*/]", " ", t).split() if re.search(r"[0-9A-Za-z$%]", w)])
        if n > 25:
            errs.append(f"beat {i}: {n} words")
        if re.search(r"example|e\.g\.|hypothetical", t, re.I):
            errs.append(f"beat {i}: banned word")
        if spec["brand"] == "fullyfunded" and re.search(r"\b6%", t):
            errs.append(f"beat {i}: 6%")
    if errs:
        raise SystemExit(f"{spec['id']}: " + "; ".join(errs))


def build(spec, out_root, workers=2):
    lint(spec)
    r = report(spec)
    assert not [s for s in r.scenes if s["dur"] + 1e-3 < read_need(s["html"])[0]], "a text beat is too fast to read"
    work = Path(out_root) / spec["id"]
    fdir, n = render_frames(r, work, dsf=2, workers=workers)
    mp4 = work / f"{spec['id']}.mp4"
    encode(fdir, n, REPO / LIB[spec["track"]]["file"], mp4, r.music_offset)
    sheet(fdir, qa_times(r), work / f"{spec['id']}-qa.jpg", cols=10, scale=0.16)
    cov = Image.open(fdir / f"{int(0.75 * FPS):05d}.png").convert("RGB")
    dst = REPO / "media" / "reels"
    cov.save(dst / f"{spec['id']}-cover.jpg", quality=92, subsampling=0)
    shutil.copy(mp4, dst / f"{spec['id']}.mp4")
    pr, lu = probe(mp4), loudness(mp4)
    print(json.dumps(dict(id=spec["id"], probe=pr, lufs=lu)), flush=True)
    shutil.rmtree(fdir, ignore_errors=True)  # frames deleted after every encode
    return pr


def spec_for(rid):
    from specs_teach import REELS
    spec = dict(REELS[rid], id=rid)
    split = lambda t: re.sub(r"\*(.+?)\*", lambda m: " / ".join(f"*{p}*" for p in m.group(1).split(" / ")), t)  # noqa: E731
    sc = []
    for s in spec["scenes"]:  # a pill never spans a line break in the kinetic type: one pill per line
        s = dict(s)
        if s.get("text"):
            s["text"] = split(s["text"])
        sc.append(s)
    spec["scenes"] = [dict(sc[0], save=spec.get("save"))] + sc[1:]
    return spec


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--out", default="/tmp/teach-reels")
    ap.add_argument("--workers", type=int, default=2)
    a = ap.parse_args()
    for rid in a.ids:
        spec = spec_for(rid)
        if a.plan:
            lint(spec)
            report(spec)
        else:
            build(spec, a.out, a.workers)

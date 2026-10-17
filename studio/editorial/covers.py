#!/usr/bin/env python3
"""Editorial feed tiles + Story tiles in the approved look. Chromium 2x render, Lanczos to size, JPEG q92, no subsampling.

    python3 studio/editorial/covers.py feed [ids]      -> media/<id>/01.jpg ...  (cover + up to 2 inner slides)
    python3 studio/editorial/covers.py story [ids]     -> media/stories/<id>.jpg
"""
import glob
import io
import random
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import edkit as K  # noqa: E402
from PIL import Image, ImageEnhance, ImageOps  # noqa: E402

CHROME = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")[0]
MOSAIC_DIR = HERE / "mosaic"


# ------------------------------------------------------------------------------------------------ mosaic background
def mosaic(brand, W, H, tile=54, seed=7):
    """'I have nothing to post' background: a dense wall of tiny real-photo tiles (licensed stock already in the repo)."""
    MOSAIC_DIR.mkdir(exist_ok=True)
    out = MOSAIC_DIR / f"{brand}-{W}x{H}.jpg"
    if out.exists():
        return out
    pool = []
    for p in sorted(glob.glob(str(REPO / "assets/inbox/g-*.png"))) + sorted(glob.glob(str(REPO / "studio/motion/assets/*.jpg"))):
        try:
            pool.append(Image.open(p).convert("RGB"))
        except Exception:
            pass
    tmp = Path(tempfile.mkdtemp())
    for v in sorted(glob.glob(str(REPO / "assets/inbox/*.mp4")))[:60]:
        f = tmp / (Path(v).stem + ".jpg")
        subprocess.run(["ffmpeg", "-v", "quiet", "-ss", "1.5", "-i", v, "-frames:v", "1", "-vf", "scale=320:-1", str(f)], check=False)
        if f.exists():
            pool.append(Image.open(f).convert("RGB"))
    rnd = random.Random(seed)
    tiles = []
    for im in pool:
        for _ in range(6):
            s = rnd.randint(min(im.size) // 4, min(im.size) // 2)
            x, y = rnd.randint(0, im.width - s), rnd.randint(0, im.height - s)
            tiles.append(im.crop((x, y, x + s, y + s)).resize((tile, tile), Image.LANCZOS))
    can = Image.new("RGB", (W, H))
    for y in range(0, H, tile):
        for x in range(0, W, tile):
            can.paste(rnd.choice(tiles), (x, y))
    can = ImageEnhance.Color(can).enhance(0.75)
    can.save(out, quality=90)
    return out


# ------------------------------------------------------------------------------------------------ layouts
def head(brand, f, text, top, height, size, left=70, right=70, align="center", wmax=940, extra=""):
    return (f'<div style="position:absolute;left:{left}px;right:{right}px;top:{top}px;height:{height}px;display:flex;'
            f'flex-direction:column;justify-content:center;z-index:2">'
            + K.dual(text, f, "S fit", f'font-size:{size}px;color:{f["ink"]};text-align:{align};white-space:nowrap;{extra}').replace('class="S fit"', f'class="S fit" data-w="{wmax}" data-h="{height}"', 1)
            + '</div>')


def kicker(brand, f, text, top=96):
    return (f'<div style="position:absolute;left:0;right:0;top:{top}px;text-align:center;z-index:3"><span style="display:inline-block;'
            f'font:600 30px/1 Fraunces;letter-spacing:.12em;text-transform:uppercase;color:{f["ink"]};border:2.5px solid {f["ink"]};'
            f'border-radius:99px;padding:14px 26px 12px">{text}</span></div>')


OBJ_AT = {  # (x, y, w, rot, flip) on a 1080x1350 tile
    ("point", "tr"): (590, 70, 460, -52, True), ("point", "bl"): (-70, 880, 460, -18, False), ("point", "tl"): (-80, 90, 440, 22, False),
    ("ok", "bl"): (-40, 820, 400, 10, False), ("ok", "br"): (770, 930, 330, -8, True),
    ("piggy", "br"): (600, 900, 470, -6, False), ("piggy", "bl"): (-30, 920, 440, 6, True),
    ("clock", "br"): (720, 870, 330, 10, False), ("hourglass", "bl"): (40, 860, 250, -10, False),
    ("cup", "bl"): (40, 880, 300, -8, False), ("shoe", "br"): (650, 940, 380, -8, False),
    ("megaphone", "bl"): (-30, 880, 420, -8, False), ("phone", "br"): (770, 820, 250, 12, False),
    ("phone", "tr"): (790, 80, 220, 14, False), ("chat", "tr"): (720, 90, 300, 8, False), ("chat", "bl"): (60, 930, 320, -6, False),
}


def place(name, at, H=1350, dy=0):
    x, y, w, r, fl = OBJ_AT[(name, at)]
    if H != 1350:
        y = int(y * H / 1350) + dy
    return K.obj(name, x, y, w, r, fl)


def stamp_for(brand, at, W, H, size=200):
    """Stamp goes in a corner the object doesn't use."""
    spot = {"tr": (60, 60), "tl": (W - size - 60, 60), "bl": (W - size - 60, H - size - 60), "br": (60, H - size - 60)}[at]
    return K.stamp(brand, spot[0], spot[1], size, rot=-12)


def lay_pills(brand, c, W=1080, H=1350):
    f = K.FIELDS[brand][c["f"]]
    at = c.get("at", "tr")
    top = 290 if at in ("tr", "tl") else 170
    if c.get("kicker"):
        top = max(top, 200)
    body = head(brand, f, c["text"], top, 700, 230)
    sy = top + 730
    if at in ("bl", "br"):
        sx, sw = (380, 640) if at == "bl" else (60, 620)
        body += K.save_line(c["save"], sx, sy, sw, 66, -4, brand)
    else:
        body += K.save_line(c["save"], 130, sy, 820, 70, -3, brand)
    st = stamp_for(brand, at, W, H)
    if at in ("tr", "tl") and c.get("kicker"):
        st = K.stamp(brand, W - 260, H - 260, 200, -12)
    return body + place(c["obj"], at) + st + (kicker(brand, f, c["kicker"]) if c.get("kicker") else "")


def lay_sticky(brand, c, W=1080, H=1350):
    f = K.FIELDS[brand][c["f"]]
    top = 150 if c.get("kicker") else 90
    body = head(brand, f, c["text"], top + 60, 330, 150, left=70, right=70)
    note = "#FFF3A8" if brand != "lockedhour" else "#FFFDF4"
    items = "".join(f'<div style="display:flex;gap:18px;align-items:baseline;border-bottom:2px solid rgba(40,40,80,.13);padding:6px 0 4px">'
                    f'<span style="font:700 46px/1 Caveat;color:{K.ACCENT[brand]}">✓</span><span>{it}</span></div>' for it in c["items"])
    body += (f'<div style="position:absolute;left:230px;top:{top + 440}px;width:640px;padding:70px 56px 50px;background:{note};'
             f'transform:rotate(-3deg);box-shadow:0 26px 40px rgba(30,30,60,.18),0 3px 6px rgba(30,30,60,.08);z-index:2;'
             f'font:600 54px/1.15 Caveat;color:{f["ink"]}">'
             f'<div style="position:absolute;left:50%;top:-24px;width:200px;height:52px;margin-left:-100px;background:rgba(255,255,255,.55);'
             f'transform:rotate(2deg);box-shadow:0 1px 2px rgba(0,0,0,.08)"></div>{items}</div>')
    at = c.get("at", "bl")
    body += K.save_line(c["save"], 330 if at == "bl" else 70, H - 140, 700, 52, -2, brand)
    if c["obj"] == "point" and at == "bl":
        o = K.obj("point", -70, top + 690, 420, -6, False)
    else:
        o = place(c["obj"], at)
    st = K.stamp(brand, W - 250, 50, 190, 12) if not c.get("kicker") else K.stamp(brand, W - 230, top + 300, 170, 12)
    return body + o + st + (kicker(brand, f, c["kicker"], 70) if c.get("kicker") else "")


def lay_mosaic(brand, c, W=1080, H=1350):
    f = K.FIELDS[brand][c["f"]]
    bg = mosaic(brand, W, H)
    lines = c["text"].split(" / ")
    cols = [f["p2"] if brand != "fullyfunded" else "#FFF1C9", "#F9C4CC", "#C6CDF8", "#FFD9BF"]
    txt = "<br>".join(f'<span style="color:{cols[i % len(cols)]}">{ln}</span>' for i, ln in enumerate(lines))
    return (f'<img src="{K.uri(bg)}" style="position:absolute;inset:0;width:{W}px;height:{H}px">'
            f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse 75% 50% at 50% 46%,rgba(18,16,40,.62),rgba(18,16,40,.30))"></div>'
            f'<div style="position:absolute;left:60px;right:60px;top:250px;height:640px;display:flex;flex-direction:column;justify-content:center;z-index:2">'
            f'<div class="S fit" data-w="960" data-h="640" style="font-size:210px;text-shadow:0 6px 30px rgba(0,0,0,.35)">{txt}</div></div>'
            f'<div class="hand" style="position:absolute;left:330px;width:690px;top:960px;font-size:66px;color:#FFF1C9;transform:rotate(-4deg);z-index:4;'
            f'text-shadow:0 3px 14px rgba(0,0,0,.4)">{c["save"]}</div>'
            + place(c["obj"], c.get("at", "bl")) + K.stamp(brand, W - 250, 60, 190, 12))


def lay_line(brand, c, W=1080, H=1350):
    f = K.FIELDS[brand][c["f"]]
    body = head(brand, f, c["text"], 110, 420, 170)
    ink = f["ink"]
    path = "M 20 900 C 100 900, 130 770, 200 770 S 420 1010, 690 770 S 930 700, 1070 840"
    body += (f'<svg style="position:absolute;left:0;top:0;width:{W}px;height:{H}px;z-index:1" viewBox="0 0 {W} {H}">'
             f'<path d="{path}" fill="none" stroke="{ink}" stroke-width="7" stroke-linecap="round" stroke-dasharray="2 16"/></svg>')
    pts = [(200, 760), (690, 760)]
    for (x, y), (a, b, v), col in zip(pts, c["dots"], [f["p1"], f["p2"]]):
        body += (f'<div style="position:absolute;left:{x - 150}px;top:{y - 120}px;width:300px;text-align:center;z-index:3">'
                 f'<div style="font:600 52px/1 Caveat;color:{ink}">{a}<br><span style="font-size:42px;opacity:.75">{b}</span></div>'
                 f'<div style="margin:16px auto 0;width:44px;height:44px;border-radius:50%;background:{K.ACCENT[brand]};border:5px solid #fff"></div>'
                 f'<div class="S" style="font-size:120px;color:{ink};margin-top:18px;white-space:nowrap"><span class="pill" style="background:{col}">{v.split(" ")[0]}</span></div>'
                 f'<div style="font:600 46px/1 Caveat;color:{ink};margin-top:6px">{" ".join(v.split(" ")[1:])}</div></div>')
    body += K.save_line(c["save"], 230, H - 200, 520, 62, -3, brand)
    return body + place(c["obj"], c.get("at", "br")) + K.stamp(brand, 50, H - 230, 170, -14)


LAYOUTS = {"pills": lay_pills, "sticky": lay_sticky, "mosaic": lay_mosaic, "line": lay_line}


def inner(brand, s, i, n, W=1080, H=1350):
    """Slides 2-3: same field + texture + serif + pills, one hero number, a handwritten note, small stamp."""
    f = K.FIELDS[brand][s["f"]]
    parts = K.dual(s["text"], f, "S fit", f'font-size:150px;color:{f["ink"]}').replace('class="S fit"', 'class="S fit" data-w="920" data-h="520"', 1)
    if s.get("num"):
        parts += (f'<div class="S fit" data-w="920" style="font-size:330px;color:{f["ink"]};margin-top:30px">'
                  f'<span class="pill" style="background:{f["p1"]}">{s["num"]}</span></div>')
    if s.get("sub"):
        parts += f'<div class="hand" style="font-size:68px;margin-top:46px;transform:rotate(-2deg)">{s["sub"]}</div>'
    return (f'<div style="position:absolute;left:70px;right:70px;top:120px;height:1060px;display:flex;flex-direction:column;'
            f'justify-content:center;align-items:center;z-index:2">{parts}</div>'
            f'<div style="position:absolute;right:60px;top:60px;font:600 30px/1 Fraunces;color:{f["ink"]};opacity:.55">{i + 1}/{n}</div>'
            + K.stamp(brand, 60, H - 220, 160, -12))


def page(brand, field, body, W, H, dark=False):
    f = K.FIELDS[brand][field]
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{K.css(brand, W, H)}</style></head><body>'
            f'<div class="page">{K.field_bg(f)}{body}</div></body></html>')


# ------------------------------------------------------------------------------------------------ stories
def story(brand, s, W=1080, H=1920):
    f = K.FIELDS[brand][s["f"]]
    ink = f["ink"]
    k = s["k"]
    label = {"question": "morning question", "newpost": "just posted", "tip": "quick tip", "evening": "tonight's check-in"}[k]
    body = (f'<div class="hand" style="position:absolute;left:0;right:0;top:270px;font-size:64px;transform:rotate(-3deg)">{label}</div>')
    if k in ("newpost", "evening"):
        body += head(brand, f, s["text"], 360, 330, 140)
        tall = k == "evening"
        w = 560 if tall else 640
        body += (f'<div style="position:absolute;left:50%;top:{740 if tall else 760}px;width:{w}px;margin-left:-{w // 2}px;transform:rotate(-4deg);'
                 f'background:#fff;padding:14px;box-shadow:0 30px 60px rgba(30,30,60,.22);z-index:2">'
                 f'<img src="{K.uri(REPO / "media" / s["img"])}" style="display:block;width:100%;{"height:" + str(int((w - 28) * 1.25)) + "px;object-fit:cover;object-position:50% 30%" if tall else ""}"></div>')
        body += K.obj("point", -60, 1180 if not tall else 1250, 400, -12, False, z=4)
        if s.get("a"):
            body += answers(brand, f, s["a"], s["b"], 1470)
        else:
            body += K.save_line("tap our profile to see it", 330, 1470, 680, 62, -3, brand)
        body += K.stamp(brand, W - 250, 1300 if tall else 1250, 190, 12)
    else:
        body += head(brand, f, s["text"], 420, 640, 190)
        if s.get("sub"):
            body += K.save_line(s["sub"], 120, 1100, 840, 70, -3, brand)
        if k == "question":
            body += answers(brand, f, s["a"], s["b"], 1180)
        o = s.get("obj", "point")
        pos = {"point": (-60, 1330, 470, -14, False), "ok": (60, 1270, 360, 8, False), "piggy": (80, 1300, 420, -6, False)}[o]
        body += K.obj(o, *pos)
        body += K.stamp(brand, W - 270, 1330, 200, 12)
    return body


def answers(brand, f, a, b, top):
    pill = (lambda t, col: f'<div class="S" style="font-size:78px;color:{f["ink"]};background:{col};border:3px solid {f["ink"]};'
            f'border-radius:999px;padding:20px 52px 26px;box-shadow:0 8px 0 {f["ink"]}">{t}</div>')
    return (f'<div style="position:absolute;left:0;right:0;top:{top}px;display:flex;justify-content:center;gap:34px;z-index:3">'
            f'{pill(a, f["p1"])}{pill(b, f["p2"])}</div>')


# ------------------------------------------------------------------------------------------------ render
class R:
    def __init__(self):
        from playwright.sync_api import sync_playwright
        self.p = sync_playwright().start()
        self.b = self.p.chromium.launch(executable_path=CHROME, args=["--disable-gpu", "--font-render-hinting=none",
                                                                      "--allow-file-access-from-files"])
        self.tmp = Path(tempfile.mkdtemp())

    def shot(self, html, W, H, out):
        pg = self.b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        f = self.tmp / "p.html"
        f.write_text(html)
        pg.goto(f.as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(120)
        pg.evaluate(K.FIT_JS, 940)
        im = Image.open(io.BytesIO(pg.screenshot(type="png"))).convert("RGB").resize((W, H), Image.LANCZOS)
        pg.close()
        im.save(out, quality=92, subsampling=0)
        return out

    def close(self):
        self.b.close()
        self.p.stop()


def build_feed(ids, r=None):
    from specs import POSTS
    own = r is None
    r = r or R()
    done = {}
    for pid in ids:
        spec = POSTS[pid]
        b, c = spec["brand"], spec["cover"]
        d = REPO / "media" / pid
        d.mkdir(exist_ok=True)
        for old in d.glob("*.jpg"):
            old.unlink()
        slides = spec.get("slides", [])
        n = 1 + len(slides)
        assert n <= 3, pid
        body = LAYOUTS[c["lay"]](b, c)
        if n > 1:
            body += (f'<div class="hand" style="position:absolute;right:56px;top:{1350 - 110 if c["lay"] != "line" else 60}px;'
                     f'font-size:52px;z-index:5;{"color:#FFF1C9" if c["lay"] == "mosaic" else ""}">swipe →</div>'
                     if c["lay"] in ("sticky", "mosaic", "line") else "")
        files = [r.shot(page(b, c["f"], body, 1080, 1350), 1080, 1350, d / "01.jpg")]
        for i, s in enumerate(slides, 1):
            files.append(r.shot(page(b, s["f"], inner(b, s, i, n), 1080, 1350), 1080, 1350, d / f"{i + 1:02d}.jpg"))
        done[pid] = [f"{pid}/{Path(x).name}" for x in files]
        print(pid, done[pid], flush=True)
    if own:
        r.close()
    return done


def build_story(ids, r=None):
    from specs import STORIES
    own = r is None
    r = r or R()
    for sid in ids:
        s = STORIES[sid]
        out = REPO / "media" / "stories" / f"{sid}.jpg"
        r.shot(page(s["brand"], s["f"], story(s["brand"], s), 1080, 1920), 1080, 1920, out)
        print(sid, out.name, flush=True)
    if own:
        r.close()


if __name__ == "__main__":
    mode, ids = sys.argv[1], sys.argv[2:]
    if mode == "feed":
        from specs import POSTS
        build_feed(ids or list(POSTS))
    else:
        from specs import STORIES
        build_story(ids or list(STORIES))


OBJ_WORDS = {"point": "a black-and-white halftone pointing hand", "ok": "a halftone OK-sign hand", "piggy": "a halftone piggy bank",
             "clock": "a halftone alarm clock", "hourglass": "a halftone hourglass", "cup": "a halftone coffee cup",
             "phone": "a black-and-white phone with chat bubbles", "chat": "black-and-white chat bubbles", "shoe": "a halftone baby shoe",
             "megaphone": "a halftone megaphone"}
LAY_WORDS = {"pills": "", "sticky": " above a yellow sticky note", "mosaic": " over a wall of tiny photos", "line": " above a dotted line"}


def clean(t):
    import re
    return re.sub(r"\s+", " ", t.replace("*", "").replace(" / ", " ")).strip()


def alt_text(pid):
    from specs import POSTS
    sp = POSTS[pid]
    b, c = sp["brand"], sp["cover"]
    n = 1 + len(sp.get("slides", []))
    kind = f"{n}-slide carousel" if n > 1 else "single image"
    s1 = f"'{clean(c['text'])}' in a large serif with highlighted words{LAY_WORDS[c['lay']]}"
    if c["lay"] == "sticky":
        s1 += " listing: " + ", ".join(c["items"])
    if c["lay"] == "line":
        s1 += ": " + "; ".join(f"{a}, {w}: {v}" for a, w, v in c["dots"])
    s1 += f", {OBJ_WORDS[c['obj']]}, and the handwritten note '{c['save']}'."
    out = f"{K.NAME[b]} {kind}. " + ("Slide 1: " if n > 1 else "") + s1
    for i, s in enumerate(sp.get("slides", []), 2):
        out += f" Slide {i}: {clean(s['text'])}" + (f" {s['num']}" if s.get("num") else "") + (f" ({s['sub']})" if s.get("sub") else "") + "."
    return out


def apply_schedule(ids):
    """images + alt_text in schedule/posts.json for the rebuilt posts (nothing else is touched)."""
    import json
    p = REPO / "schedule" / "posts.json"
    d = json.loads(p.read_text())
    for post in d["posts"]:
        if post["id"] in ids:
            post["images"] = sorted(f"{post['id']}/{f.name}" for f in (REPO / "media" / post["id"]).glob("*.jpg"))
            post["alt_text"] = alt_text(post["id"])
    p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")

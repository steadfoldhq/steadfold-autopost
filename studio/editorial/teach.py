#!/usr/bin/env python3
"""Brand system §13 (Oct 17, 7:07-7:37 pm): teaching posts + Story chains in the SAME approved editorial look (§12).

    python3 studio/editorial/teach.py feed  [ids]     -> media/<id>/01.jpg ... (cover + up to 9 inner slides)
    python3 studio/editorial/teach.py story [ids]     -> media/stories/<frame-id>.jpg  (every frame of each chain)
    python3 studio/editorial/teach.py sheet <kind> <ids...> --out FILE   -> one owner sheet (contact strip)

Feed: the cover uses covers.LAYOUTS (pills / sticky / mosaic / line). Inner slide kinds (k):
  say    serif line + pills, optional num (hero number), sub (handwritten), label (handwritten kicker), src
  why    "why it works" kicker, the mechanism in serif, an analogy (handwritten), optional bars (mini visual), src
  rows   a white table card (covers.inner_list)          steps  numbered 3-step card (covers.inner_list)
  catch  "the catch" kicker + serif line + sub           do     "Do this:" on its own slide: the ONE action in a card
Story chain frames (1080x1920), one chain per page per day (§13.4):
  photo    the hook: quote in handwriting on a real photo, one highlighted word, page labels, arrow (owner references)
  bubbles  text bubbles that build the story / the WHY, on the page's soft field (serif kicker, object, stamp)
  payoff   the number / the exact words, editorial serif + pills, "screenshot this"
  handoff  "Full breakdown in today's post 👆" with the post's cover, or "Part 2 tomorrow"
"""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import covers as C  # noqa: E402
import edkit as K  # noqa: E402

W, H = 1080, 1350
SW, SH = 1080, 1920
BUBBLE_OUT = {"fullyfunded": "#2B3FE0", "hourback": "#5E54C9", "lockedhour": "#E8336F", "littlefold": "#D9497A"}
HL = {"fullyfunded": "#FFD3BF", "hourback": "#FFE08A", "lockedhour": "#FFD43B", "littlefold": "#FFE59A"}  # photo-frame highlighter
FMT_LABEL = {"keep": "keep this", "suggestion": "try this", "tip": "tip", "learning": "learn this", "deep": "deep dive"}


def words(t):
    return len([w for w in re.sub(r"[*/“”\"]", " ", t or "").split() if re.search(r"[0-9A-Za-z$%]", w)])


# ------------------------------------------------------------------------------------------------ feed inner slides
def counter(f, i, n):
    return f'<div style="position:absolute;right:60px;top:52px;font:600 30px/1 Fraunces;color:{f["ink"]};opacity:.55;z-index:6">{i + 1}/{n}</div>'


def label_html(brand, text, top=110):
    return (f'<div class="hand" style="position:absolute;left:0;right:0;top:{top}px;font-size:76px;transform:rotate(-3deg);z-index:4">'
            f'{text}<svg style="display:block;margin:2px auto 0" width="300" height="22" viewBox="0 0 300 22"><path d="M6 14 C 80 4, 200 4, 294 12" '
            f'fill="none" stroke="{K.ACCENT[brand]}" stroke-width="6" stroke-linecap="round"/></svg></div>')


def bars_html(brand, f, bars, top=820):
    """Mini visual: up to 5 bars growing left to right, value pill on top, handwritten label under."""
    mx = max(v for _, v, _ in bars)
    bw, gap = 150, 40
    total = len(bars) * bw + (len(bars) - 1) * gap
    x0 = (W - total) // 2
    hmax = 300
    out = ""
    for i, (lab, v, shown) in enumerate(bars):
        h = max(18, int(hmax * v / mx))
        x = x0 + i * (bw + gap)
        col = f["p1"] if i < len(bars) - 1 else K.ACCENT[brand]
        out += (f'<div style="position:absolute;left:{x}px;top:{top + hmax - h}px;width:{bw}px;height:{h}px;background:{col};'
                f'border:3px solid {f["ink"]};border-radius:18px 18px 6px 6px;z-index:2"></div>'
                f'<div class="S" style="position:absolute;left:{x - 40}px;width:{bw + 80}px;top:{top + hmax - h - 70}px;font-size:52px;'
                f'color:{f["ink"]};z-index:3;white-space:nowrap">{shown}</div>'
                f'<div style="position:absolute;left:{x - 30}px;width:{bw + 60}px;top:{top + hmax + 14}px;text-align:center;'
                f'font:600 44px/1 Caveat;color:{f["ink"]};z-index:3">{lab}</div>')
    return out


def say_slide(brand, s, i, n, kicker_default=None):
    f = K.FIELDS[brand][s["f"]]
    lab = s.get("label", kicker_default)
    has_bars = bool(s.get("bars"))
    top = 230 if lab else 120
    hgt = (520 if has_bars else 1000) if not s.get("num") else 980
    parts = K.dual(s["text"], f, "S fit", f'font-size:{s.get("size", 150)}px;color:{f["ink"]}').replace(
        'class="S fit"', f'class="S fit" data-w="920" data-h="{460 if (has_bars or s.get("num")) else 560}"', 1)
    if s.get("num"):
        parts += (f'<div class="S fit" data-w="920" style="font-size:300px;color:{f["ink"]};margin-top:30px">'
                  f'<span class="pill" style="background:{f["p1"]}">{s["num"]}</span></div>')
    if s.get("sub") and not has_bars:
        parts += f'<div class="hand" style="font-size:66px;margin-top:44px;transform:rotate(-2deg);max-width:900px">{s["sub"]}</div>'
    body = (f'<div style="position:absolute;left:70px;right:70px;top:{top}px;height:{hgt}px;display:flex;flex-direction:column;'
            f'justify-content:center;align-items:center;z-index:2">{parts}</div>')
    if lab:
        body += label_html(brand, lab)
    if has_bars:
        body += bars_html(brand, f, s["bars"])
        if s.get("sub"):
            body += K.save_line(s["sub"], 140, 1195, 800, 54, -2, brand)
    st = K.stamp(brand, 60, H - 220, 160, -12)
    o = ""
    if s.get("obj"):
        o = K.obj(s["obj"], W - 330, H - 400, 300, 8, True) if s["obj"] != "point" else K.obj("point", W - 420, H - 360, 380, 18, True)
    return body + counter(f, i, n) + st + o + C.src_line(f, s.get("src"))


def do_slide(brand, s, i, n):
    """'Do this:' on its own slide: ONE action, specific (what, where, how much, when), in an ink-bordered card."""
    f = K.FIELDS[brand][s["f"]]
    ink = f["ink"]
    body = (f'<div style="position:absolute;left:0;right:0;top:120px;text-align:center;z-index:4">'
            f'<span class="hand" style="display:inline-block;font-size:150px;transform:rotate(-4deg)">Do this:</span></div>')
    card = K.dual(s["text"].replace(" / ", " "), f, "S fit", f'font-size:{s.get("size", 104)}px;color:{ink};line-height:1.02;text-wrap:balance;width:800px').replace(
        'class="S fit"', 'class="S fit" data-w="820" data-h="580"', 1)
    body += (f'<div style="position:absolute;left:90px;right:90px;top:360px;height:660px;background:#FFFFFF;border:4px solid {ink};'
             f'border-radius:44px;box-shadow:0 16px 0 {ink};display:flex;align-items:center;justify-content:center;padding:40px 50px;z-index:2">'
             f'{card}</div>')
    if s.get("save"):
        body += K.save_line(s["save"], 230, 1110, 620, 62, -3, brand)
    body += K.obj("point", -90, 980, 380, -20, False, z=4)
    return body + counter(f, i, n) + K.stamp(brand, W - 230, H - 230, 170, -12) + C.src_line(f, s.get("src"))


def inner(brand, s, i, n):
    k = s.get("k", "say")
    if k in ("rows", "steps"):
        s2 = dict(s)
        return C.inner_list(brand, s2, i, n, W, H)
    if k == "do":
        return do_slide(brand, s, i, n)
    if k == "why":
        return say_slide(brand, s, i, n, "why it works")
    if k == "catch":
        return say_slide(brand, s, i, n, "the catch")
    return say_slide(brand, s, i, n)


def check_post(pid, spec):
    """§13 lint: 25 words max per slide, ONE do slide, no 'example', 6% never on FF."""
    errs = []
    sl = spec.get("slides", [])
    if sum(1 for s in sl if s.get("k") == "do") != 1:
        errs.append("needs exactly one 'Do this:' slide")
    for j, s in enumerate([spec["cover"]] + sl):
        txt = " ".join(str(s.get(x, "")) for x in ("text", "sub", "save", "label", "kicker"))
        txt += " " + " ".join(s.get("items", []) or []) + " " + " ".join(" ".join(r) for r in s.get("rows", []) or [])
        if words(txt) > 25:
            errs.append(f"slide {j + 1}: {words(txt)} words")
        if re.search(r"example|e\.g\.|for illustration|hypothetical", txt, re.I):
            errs.append(f"slide {j + 1}: banned word")
        if spec["brand"] == "fullyfunded" and re.search(r"\b6%", txt):
            errs.append(f"slide {j + 1}: 6% rate")
    if errs:
        raise SystemExit(f"{pid}: " + "; ".join(errs))


def build_feed(ids, r=None):
    from specs_teach import POSTS
    own = r is None
    r = r or C.R()
    done = {}
    for pid in ids:
        spec = POSTS[pid]
        check_post(pid, spec)
        b, c = spec["brand"], spec["cover"]
        d = REPO / "media" / pid
        d.mkdir(exist_ok=True)
        for old in d.glob("*.jpg"):
            old.unlink()
        slides = spec.get("slides", [])
        n = 1 + len(slides)
        assert n <= 10, pid
        body = C.LAYOUTS[c["lay"]](b, c)
        if n > 1:
            col = "#FFF1C9" if c["lay"] == "mosaic" else K.ACCENT[b]
            y = {"sticky": H - 66, "mosaic": H - 110, "line": 60, "pills": H - 86}[c["lay"]]
            x = "right:56px" if c["lay"] != "pills" else ("left:430px" if c.get("at") in ("bl", "br") else "left:300px")
            if c["lay"] == "pills" and c.get("src"):
                y, x = 52, "left:60px"
            body += (f'<div class="hand" style="position:absolute;{x};top:{y}px;font-size:52px;z-index:5;color:{col}">'
                     f'{n} slides · swipe →</div>')
        files = [r.shot(C.page(b, c["f"], body, W, H), W, H, d / "01.jpg")]
        for i, s in enumerate(slides, 1):
            files.append(r.shot(C.page(b, s["f"], inner(b, s, i, n), W, H), W, H, d / f"{i + 1:02d}.jpg"))
        done[pid] = [f"{pid}/{Path(x).name}" for x in files]
        print(pid, len(files), "slides", flush=True)
    if own:
        r.close()
    return done


# ------------------------------------------------------------------------------------------------ story chain frames
def arrow_svg(col, x=820, y=1620, w=170):
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:40px;z-index:6" viewBox="0 0 170 40">'
            f'<path d="M4 22 C 50 18, 110 18, 160 20 M140 6 L162 20 L140 34" fill="none" stroke="{col}" stroke-width="4.5" '
            f'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def hl_quote(text, hl):
    """'*word*' -> marker highlight behind the word (rough-edged, like a highlighter swipe); ' / ' -> break."""
    t = re.sub(r"\*(.+?)\*", lambda m: f'<span style="background:linear-gradient(100deg,transparent 0 2%,{hl} 3% 96%,transparent 98%);'
               f'border-radius:.55em .3em .6em .35em;padding:0 .14em;-webkit-box-decoration-break:clone;box-decoration-break:clone">{m.group(1)}</span>', text)
    return t.replace(" / ", "<br>")


def photo_frame(brand, fr, chain):
    ink = "#1E1B1B" if fr.get("ink", "dark") == "dark" else "#FFFFFF"
    shadow = ("0 0 24px rgba(0,0,0,.55),0 2px 8px rgba(0,0,0,.45)" if ink == "#FFFFFF"
              else "0 0 26px rgba(255,255,255,.8),0 0 8px rgba(255,255,255,.65)")
    y = fr.get("y", 700)
    src = HERE / "photos" / f"{chain['photo']}.jpg"
    lab_col = "#FFFFFF"
    body = (f'<img src="{K.uri(src)}" style="position:absolute;inset:0;width:{SW}px;height:{SH}px;object-fit:cover">'
            f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.28) 0,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 74%,rgba(0,0,0,.30) 100%)"></div>'
            f'<div style="position:absolute;left:84px;top:300px;font:italic 400 40px/1 \'Instrument Serif\';color:{lab_col};z-index:5;text-shadow:0 1px 8px rgba(0,0,0,.35)">{chain["series"]}</div>'
            f'<div style="position:absolute;right:84px;top:300px;font:italic 400 40px/1 \'Instrument Serif\';color:{lab_col};z-index:5;text-shadow:0 1px 8px rgba(0,0,0,.35)">{K.NAME[brand].lower()}</div>'
            f'<div style="position:absolute;left:70px;right:70px;top:{y - 260}px;height:620px;display:flex;flex-direction:column;'
            f'justify-content:center;align-items:center;gap:26px;z-index:4">'
            f'<div class="fit" data-w="940" data-h="430" style="text-align:center;font:700 172px/1.0 Caveat;color:{ink};text-shadow:{shadow}">'
            f'{hl_quote(fr["text"], HL[brand])}</div>'
            + (f'<div style="text-align:center;font:600 70px/1.08 Caveat;color:{ink};text-shadow:{shadow}">{hl_quote(fr["sub"], HL[brand])}</div>'
               if fr.get("sub") else "") + '</div>')
    body += (f'<div style="position:absolute;left:84px;top:1610px;font:400 40px/1 \'Instrument Serif\';color:{lab_col};z-index:5;'
             f'text-shadow:0 1px 8px rgba(0,0,0,.35)">{K.HANDLE[brand]}</div>')
    body += arrow_svg("#FFFFFF")
    body += K.stamp(brand, 84, 1400, 150, -12)
    return body


def bubble(text, side, brand, size=62):
    if side == "in":
        st = "background:#FFFFFF;color:#1B1B1F;border-bottom-left-radius:10px;align-self:flex-start"
    elif side == "ai":
        st = f"background:{K.FIELDS[brand][next(iter(K.FIELDS[brand]))]['p2']};color:#1B1B1F;border:3px solid #1B1B1F;border-bottom-left-radius:10px;align-self:flex-start"
    else:
        st = f"background:{BUBBLE_OUT[brand]};color:#FFFFFF;border-bottom-right-radius:10px;align-self:flex-end"
    t = re.sub(r"\*(.+?)\*", r"<b>\1</b>", text)
    return (f'<div style="max-width:860px;padding:30px 42px 32px;border-radius:50px;font:500 {size}px/1.18 Inter;{st};'
            f'box-shadow:0 10px 24px rgba(30,30,60,.14)">{t}</div>')


def bubbles_frame(brand, fr, chain):
    f = K.FIELDS[brand][fr["f"]]
    body = f'<div class="hand" style="position:absolute;left:0;right:0;top:300px;font-size:70px;transform:rotate(-3deg);z-index:4">{fr["label"]}</div>'
    if fr.get("title"):
        body += C.head(brand, f, fr["title"], 400, 250, 120)
    top = 690 if fr.get("title") else 420
    body += (f'<div style="position:absolute;left:70px;right:70px;top:{top}px;height:{1380 - top}px;display:flex;flex-direction:column;'
             f'justify-content:center;gap:30px;z-index:3">'
             + "".join(bubble(t, side, brand) for side, t in fr["bubbles"]) + '</div>')
    body += K.obj(fr.get("obj", "point"), -60, 1440, 360, -14, False, z=4) if fr.get("obj", "point") == "point" else K.obj(fr["obj"], 70, 1400, 260, -8, False, z=4)
    body += K.save_line(fr.get("tap", "tap →"), 560, 1640, 440, 64, -3, brand)
    body += K.stamp(brand, W - 230, 1400, 150, 12)
    return body


def payoff_frame(brand, fr, chain):
    f = K.FIELDS[brand][fr["f"]]
    body = f'<div class="hand" style="position:absolute;left:0;right:0;top:300px;font-size:70px;transform:rotate(-3deg);z-index:4">{fr["label"]}</div>'
    body += C.head(brand, f, fr["text"], 420, 640, 190)
    if fr.get("sub"):
        body += K.save_line(fr["sub"], 100, 1100, 880, 66, -3, brand)
    body += K.obj(fr.get("obj", "ok"), 60, 1260, 340, 8, False, z=4) if fr.get("obj", "ok") != "point" else K.obj("point", -60, 1330, 430, -14, False)
    body += K.save_line(fr.get("tap", "screenshot this · next story →"), 400, 1600, 620, 56, -3, brand)
    body += K.stamp(brand, W - 260, 1330, 190, 12)
    return body


def handoff_frame(brand, fr, chain):
    f = K.FIELDS[brand][fr["f"]]
    ink = f["ink"]
    body = f'<div class="hand" style="position:absolute;left:0;right:0;top:290px;font-size:66px;transform:rotate(-3deg);z-index:4">{fr.get("label", chain["series"])}</div>'
    body += C.head(brand, f, fr["text"], 370, 260, 130)
    if fr.get("img"):
        w = 520
        body += (f'<div style="position:absolute;left:50%;top:660px;width:{w}px;margin-left:-{w // 2}px;transform:rotate(-3deg);'
                 f'background:#fff;padding:14px;box-shadow:0 30px 60px rgba(30,30,60,.22);z-index:2">'
                 f'<img src="{K.uri(REPO / "media" / fr["img"])}" style="display:block;width:100%;height:{int((w - 28) * 1.25)}px;object-fit:cover"></div>')
    body += (f'<div class="hand" style="position:absolute;left:60px;right:60px;top:1330px;font-size:78px;transform:rotate(-2deg);z-index:5">'
             f'{fr.get("cta", "Full breakdown in today&#39;s post 👆")}</div>')
    if fr.get("next"):
        body += (f'<div style="position:absolute;left:0;right:0;top:1470px;text-align:center;z-index:5"><span class="S" style="display:inline-block;'
                 f'font-size:58px;color:{ink};background:{f["p2"]};border:3px solid {ink};border-radius:999px;padding:14px 40px 20px;'
                 f'box-shadow:0 8px 0 {ink}">{fr["next"]}</span></div>')
    body += K.obj("point", -70, 1150, 360, -30, False, z=4)
    body += K.stamp(brand, W - 240, 1180, 170, 12)
    return body


FRAMES = {"photo": photo_frame, "bubbles": bubbles_frame, "payoff": payoff_frame, "handoff": handoff_frame}


def chain_frames(cid):
    from specs_teach import CHAINS
    ch = CHAINS[cid]
    return [(f"{cid}-{i + 1}", fr) for i, fr in enumerate(ch["frames"])]


def build_story(cids, r=None):
    from specs_teach import CHAINS
    own = r is None
    r = r or C.R()
    out = []
    for cid in cids:
        ch = CHAINS[cid]
        b = ch["brand"]
        for fid, fr in chain_frames(cid):
            txt = " ".join(str(fr.get(x, "")) for x in ("text", "sub", "label", "title", "cta", "next")) + " " + " ".join(t for _, t in fr.get("bubbles", []))
            assert words(txt) <= 32, (fid, words(txt))
            assert not re.search(r"example|e\.g\.|hypothetical", txt, re.I), fid
            field = fr.get("f", next(iter(K.FIELDS[b])))
            html = C.page(b, field, FRAMES[fr["k"]](b, fr, ch), SW, SH)
            dst = REPO / "media" / "stories" / f"{fid}.jpg"
            r.shot(html, SW, SH, dst)
            out.append(dst)
            print(fid, flush=True)
    if own:
        r.close()
    return out


# ------------------------------------------------------------------------------------------------ owner sheets
def sheet(paths, out, title, cols=None, tw=360):
    from PIL import Image, ImageDraw, ImageFont
    ims = [Image.open(p).convert("RGB") for p in paths]
    cols = cols or min(len(ims), 5)
    ths = []
    for im in ims:
        th = im.resize((tw, int(tw * im.height / im.width)), Image.LANCZOS)
        ths.append(th)
    rows = (len(ths) + cols - 1) // cols
    rh = max(t.height for t in ths)
    pad = 24
    can = Image.new("RGB", (cols * (tw + pad) + pad, rows * (rh + pad) + pad + 90), "#F4F1EA")
    d = ImageDraw.Draw(can)
    try:
        fnt = ImageFont.truetype(str(REPO / "assets/fonts/Fraunces-Variable.ttf"), 44)
    except Exception:
        fnt = None
    d.text((pad, 24), title, fill="#141A55", font=fnt)
    for i, t in enumerate(ths):
        can.paste(t, (pad + (i % cols) * (tw + pad), 90 + pad + (i // cols) * (rh + pad)))
    can.save(out, quality=90)
    return out


if __name__ == "__main__":
    mode, ids = sys.argv[1], sys.argv[2:]
    if mode == "feed":
        from specs_teach import POSTS
        build_feed(ids or list(POSTS))
    elif mode == "story":
        from specs_teach import CHAINS
        build_story(ids or list(CHAINS))

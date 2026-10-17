#!/usr/bin/env python3
"""Pivot (Oct 17): the bold one-idea look for all four pages.

One idea per post, a giant 3-6 word hook, one strong colour field per frame, at most 3 slides.
Shared by stills.py (feed tiles) and reels.py (Reels cut with studio/motion/kit.py).
See docs/brand-system-v4.md, "Pivot (Oct 17)".
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
MARKS = REPO / "studio" / "motion" / "assets"

# EDITORIAL (Oct 17, restored approved look): the fields, type and accents now come from studio/editorial/edkit.py.
# Soft single-colour field + paper grain, the page's display serif in deep ink, accent words on highlighter pills.
# Same field keys as before (cob/lite/coral/deep, indi/yel/plum/orng, ...) so every spec maps over unchanged.
sys.path.insert(0, str(REPO / "studio" / "editorial"))
import edkit as ED  # noqa: E402

FIELDS = {b: {k: dict(bg=v["bg"], ink=v["ink"], p1=v["p1"], p2=v["p2"],
                      em=f"background:{v['p1']};color:{v['ink']};border-radius:.42em;padding:0 .12em .02em;-webkit-box-decoration-break:clone;box-decoration-break:clone",
                      dot="rgba(0,0,0,0)")
              for k, v in fs.items()} for b, fs in ED.FIELDS.items()}
FONT = ED.SERIF
NAME = {"fullyfunded": "Fully Funded", "hourback": "Hourback", "lockedhour": "Locked Hour", "littlefold": "Littlefold"}
HANDLE = {"fullyfunded": "@fullyfundedhq", "hourback": "@hourbackhq", "lockedhour": "@lockedhourhq", "littlefold": "@littlefoldhq"}
MARK = {"fullyfunded": "fullyfunded.png", "hourback": "hourback.png", "lockedhour": "lockedhour.png", "littlefold": "littlefold.png"}


def data_uri(path):
    """Pages rendered with set_content() are about:blank and can't load file:// images, so inline them."""
    import base64
    path = Path(path)
    mime = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".svg": "image/svg+xml"}[path.suffix.lower()]
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def field_css(brand):
    """.fx-<name> sets the ink; .em / .em2 are the two pill colours; .dotbg is the soft field + paper grain."""
    out = [ED.FONTS]
    for k, f in FIELDS[brand].items():
        out.append(f".fx-{k}{{color:{f['ink']}}} .fx-{k} .em{{{f['em']}}} .fx-{k} .em2{{background:{f['p2']}}}"
                   f" .fx-{k}.dotbg{{background:url('{ED.uri(ED.GRAIN)}') 0 0/420px 420px,{f['bg']};background-blend-mode:multiply}}")
    out.append(f".T{{{FONT[brand]}}}")
    out.append(".T .em,.T .em2{display:inline-block;white-space:nowrap}")
    return "\n".join(out)


def mark_txt(text):
    """'*word word*' -> one pill per run (alternating the field's two pill colours); '/' -> line break."""
    k = [0]

    def rep(m):
        k[0] += 1
        return f'<span class="em{"" if k[0] % 2 else " em2"}">{m.group(1)}</span>'
    text = re.sub(r"\*(.+?)\*", rep, text)
    return text.replace(" / ", "<br>")


def n_words(text):
    return len([w for w in re.sub(r"[*/]", " ", text).split() if re.search(r"[0-9A-Za-z$%]", w)])


# ------------------------------------------------------------------ editorial Reel pieces (frame 0 = the cover)
SAVES = {  # handwritten save-line on each Reel's hook / cover
    "ff-reel-1017am-match": "save this before your next benefits check",
    "ff-reel-1017-raise-half": "save this for your next raise",
    "ff-reel-1018am-lower-rate": "save this before you pay your card",
    "ff-reel-1018-the-door": "save this if you have a little one",
    "ff-reel-1019am-gift-per-person": "save this before you start gift shopping",
    "ff-reel-1019-late-start": "save this if you feel late to saving",
    "ff-reel-1020am-three-numbers": "save this before you move in together",
    "ff-reel-1020-windfall-pause": "save this for your next bonus",
    "hb-reel-1017am-swap": "save this for the next recipe",
    "hb-reel-1017-offline": "save this for 6 pm tonight",
    "hb-reel-1018am-freeze-frame": "send this to the family chat",
    "hb-reel-1018-school-email": "save this for the next newsletter",
    "hb-reel-1019am-just-the-asks": "save this for your inbox",
    "hb-reel-1019-one-sorry": "save this before you hit send",
    "lf-reel-1019-sick-day-plan": "save this before cold season",
    "lf-reel-1017-one-job": "save this for the first week home",
    "lh-reel-1017-one-tab": "save this for your next focus hour",
    "lf-reel-1018am-3am-windows": "save this for the 3 am feed",
    "lh-reel-1018am-pick-3": "save this for Sunday night",
    "lf-reel-1018-breathe": "it's ok to put baby down safely",
    "lh-reel-1018-mute-the-world": "save this for tomorrow morning",
    "lf-reel-1019am-hunger-cues": "save this for the first feeds",
}
HOOK_OBJ = {"fullyfunded": ["point", "ok", "piggy"], "hourback": ["point", "phone", "chat"]}


def obj_for(brand, emo, i=0):
    o = ED.EMOJI_OBJ.get(emo or "", None)
    return o or HOOK_OBJ.get(brand, ["point"])[i % len(HOOK_OBJ.get(brand, ["point"]))]


def sticker_obj(name, w=380, t=0.12, loop="float", r=0):
    """A halftone cut-out in the column flow, popping in like the old emoji sticker did."""
    if name in ("phone", "chat"):
        inner = ED.phone(0, 0, int(w * 0.55), r) if name == "phone" else ED.chat(0, 0, w, r)
        inner = inner.replace("position:absolute", "position:relative", 1)
        hgt = int(w * 0.55 * 1.95) if name == "phone" else int(w * 0.76)
        return (f'<span data-a="pop" data-t="{t}" data-d="0.4" data-loop="{loop}" style="display:inline-block;position:relative;'
                f'width:{w if name == "chat" else int(w * .55)}px;height:{hgt}px">{inner}</span>')
    return (f'<span data-a="pop" data-t="{t}" data-d="0.4" data-loop="{loop}" style="display:inline-block">'
            f'<img src="{ED.uri(ED.ASSETS / ED.OBJ[name])}" '
            f'style="display:block;width:{w}px;transform:rotate({r}deg);filter:drop-shadow(0 18px 22px rgba(20,20,40,.16))"></span>')


def hook_scene(brand, field, text, emo=None, save=None, size=None, wtxt=None):
    """Static editorial hook = the Reel cover: serif + pills, the page's object interacting with the type,
    handwritten save-line, brand stamp. Inside the 4:5 grid crop (y 285-1635) and clear of the Reel UI."""
    f = FIELDS[brand][field]
    o = obj_for(brand, emo)
    size = min(size or 230, 230)
    if " / " not in text and len(text.split()) >= 2:  # one long line reads small: break before the pill (or mid-way)
        w = text.split()
        k = next((i for i, x in enumerate(w) if x.startswith("*")), 0) or len(w) // 2
        text = " ".join(w[:k]) + " / " + " ".join(w[k:])
    txt = wtxt(text, size, anim=False) if wtxt else f'<div class="T" style="font-size:{size}px">{mark_txt(text)}</div>'
    # lines break only at ' / '; the kit's autofit (class cc) shrinks the block to the safe width, so the size lives on the .el
    txt = txt.replace(f"font-size:{size}px", "font-size:1em;white-space:nowrap;display:inline-block", 1)
    body = (f'<div class="el cc" data-a="none" style="left:0;width:1080px;top:600px;height:600px;font-size:{size}px;display:flex;'
            f'flex-direction:column;justify-content:center;align-items:center;text-align:center">{txt}</div>')
    if save:
        body += (f'<div class="el emo" data-a="none" style="left:110px;width:860px;top:1240px;text-align:center;font-family:\'Caveat Brush\';'
                 f'font-size:76px;line-height:1.02;color:{ED.ACCENT[brand]};transform:rotate(-3deg)">{save}</div>')
    pos = {"point": (560, 330, 470, -52, True), "ok": (-20, 1360, 360, 10, False), "piggy": (620, 1370, 400, -6, False),
           "phone": (800, 290, 220, 14, False), "chat": (700, 300, 320, 8, False), "clock": (740, 1370, 290, 10, False),
           "hourglass": (70, 1360, 230, -10, False), "cup": (70, 1370, 260, -8, False), "megaphone": (-30, 1370, 380, -8, False),
           "shoe": (640, 1380, 340, -8, False)}[o]
    # the kit animates .el transforms, so objects/stamps sit INSIDE a still .el wrapper (keeps flip + rotation)
    body += f'<div class="el emo" data-a="none" style="left:0;top:0;width:1080px;height:1920px">{ED.obj(o, *pos)}</div>'
    corner = (90, 1400) if o in ("point", "phone", "chat") else ((810, 330) if pos[0] < 500 else (90, 330))
    body += f'<div class="el emo" data-a="none" style="left:0;top:0;width:1080px;height:1920px">{ED.stamp(brand, corner[0], corner[1], 200, -12)}</div>'

    return body


def beat_stamp(brand, y=1460):
    """Small brand stamp on every text beat."""
    return f'<div class="el emo" data-a="none" style="left:0;top:0;width:1080px;height:1920px">{ED.stamp(brand, 810, y, 150, -12)}</div>'

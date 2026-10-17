#!/usr/bin/env python3
"""Editorial look (restored Oct 17): the APPROVED Steadfold style, yoursocialteam-league.

Huge display serif in deep ink, tight leading, 4-6 words; rounded highlighter PILLS behind key words in two soft
brand colours; a halftone cut-out object or hand interacting with the type; a handwritten save-line in the accent
colour (Caveat Brush); the round brand stamp in a corner; a soft single-colour field with paper texture.
Never a bare flat card. See docs/brand-system-v4.md section 12.

Used by studio/editorial/covers.py (feed + Story tiles) and, through studio/pivot/boldkit.py, by the Reel builders.
Pages are written to a temp .html file and opened with goto(), so file:// fonts and images load.
"""
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
ASSETS = REPO / "studio" / "motion" / "assets"
GRAIN = REPO / "studio" / "styles" / "assets" / "paper-grain.png"


def uri(p):
    return Path(p).as_uri()


FONTS = f"""
@font-face{{font-family:'Fraunces';src:url('{uri(REPO / "assets/fonts/Fraunces-Variable.ttf")}')}}
@font-face{{font-family:'DM Serif Display';src:url('{uri(REPO / "assets/fonts/DMSerifDisplay-Regular.ttf")}')}}
@font-face{{font-family:'Instrument Serif';src:url('{uri(REPO / "assets/inbox/InstrumentSerif-Regular.ttf")}')}}
@font-face{{font-family:'Instrument Serif';font-style:italic;src:url('{uri(REPO / "assets/inbox/InstrumentSerif-Italic.ttf")}')}}
@font-face{{font-family:'Caveat Brush';src:url('{uri(REPO / "assets/fonts/CaveatBrush-Regular.ttf")}')}}
@font-face{{font-family:'Caveat';src:url('{uri(REPO / "assets/fonts/Caveat-Variable.ttf")}')}}
"""

# Soft single-colour fields. Same keys as the pivot fields so every existing spec maps over.
# p1/p2 = the two highlighter pill colours on that field.
FF_INK, HB_INK, LH_INK, LF_INK = "#141A55", "#2A1D47", "#1B1717", "#3A1F3D"
FIELDS = {
    "fullyfunded": {
        "cob":   dict(bg="#CBD4F7", ink=FF_INK, p1="#FFC6B2", p2="#FBF2DF"),
        "lite":  dict(bg="#F7F1E6", ink=FF_INK, p1="#C9D3F7", p2="#FFC6B2"),
        "coral": dict(bg="#F9D0C3", ink=FF_INK, p1="#CBD4F7", p2="#FBF2DF"),
        "deep":  dict(bg="#DDE3FA", ink=FF_INK, p1="#FFC6B2", p2="#FFEFB8"),
    },
    "hourback": {
        "indi":  dict(bg="#C9CAF5", ink=HB_INK, p1="#FFD4BD", p2="#FFF0C2"),
        "yel":   dict(bg="#FFDDC9", ink=HB_INK, p1="#C9CAF5", p2="#FFF0C2"),
        "plum":  dict(bg="#FFF5EA", ink=HB_INK, p1="#C9CAF5", p2="#FFD4BD"),
        "orng":  dict(bg="#FFE9C2", ink=HB_INK, p1="#C9CAF5", p2="#FFD4BD"),
    },
    "lockedhour": {
        "dots":  dict(bg="#FFF0A6", ink=LH_INK, p1="#FFBAD6", p2="#FFFDF4"),
        "cream": dict(bg="#FFF6E5", ink=LH_INK, p1="#FFBAD6", p2="#FFE27A"),
        "pink":  dict(bg="#FFD5E5", ink=LH_INK, p1="#FFE27A", p2="#FFFDF4"),
    },
    "littlefold": {
        "cream":  dict(bg="#FFF1E3", ink=LF_INK, p1="#FFBFD3", p2="#FFE59A"),
        "pink":   dict(bg="#FFD8E5", ink=LF_INK, p1="#FFE59A", p2="#FFF8EE"),
        "butter": dict(bg="#FFEBAE", ink=LF_INK, p1="#FFBFD3", p2="#FFF8EE"),
        "berry":  dict(bg="#FFDCC4", ink=LF_INK, p1="#FFBFD3", p2="#FFF8EE"),
    },
}
ACCENT = {"fullyfunded": "#E04E28", "hourback": "#D4532A", "lockedhour": "#E0306C", "littlefold": "#D9497A"}
STAMP_BG = {"fullyfunded": "#FBF2DF", "hourback": "#FFF0C2", "lockedhour": "#FFFDF4", "littlefold": "#FFF8EE"}
# Display serif per page: FF Fraunces, HB DM Serif Display, LH Instrument Serif, LF Fraunces (softer).
SERIF = {
    "fullyfunded": "font-family:Fraunces;font-variation-settings:'opsz' 60,'wght' 700,'SOFT' 0,'WONK' 0;letter-spacing:-.04em;line-height:.92",
    "hourback": "font-family:'DM Serif Display';font-weight:400;letter-spacing:-.035em;line-height:.92",
    "lockedhour": "font-family:'Instrument Serif';font-weight:400;letter-spacing:-.025em;line-height:.9",
    "littlefold": "font-family:Fraunces;font-variation-settings:'opsz' 72,'wght' 620,'SOFT' 100,'WONK' 0;letter-spacing:-.035em;line-height:.94",
}
NAME = {"fullyfunded": "Fully Funded", "hourback": "Hourback", "lockedhour": "Locked Hour", "littlefold": "Littlefold"}
TAG = {"fullyfunded": "MONEY, MADE CLEAR", "hourback": "YOUR EVENINGS BACK", "lockedhour": "ONE HOUR AT A TIME",
       "littlefold": "SMALL DAYS, GENTLY"}
HANDLE = {"fullyfunded": "@fullyfundedhq", "hourback": "@hourbackhq", "lockedhour": "@lockedhourhq", "littlefold": "@littlefoldhq"}
MARK = {"fullyfunded": "fullyfunded.png", "hourback": "hourback.png", "lockedhour": "lockedhour.png", "littlefold": "littlefold.png"}

# halftone cut-outs in studio/motion/assets (w/h ratio for placement)
OBJ = {
    "point": "ht-point.png", "ok": "ht-ok.png", "piggy": "ht-piggy.png", "clock": "ht-clock.png", "hourglass": "ht-hourglass.png",
    "cup": "ht-cup.png", "shoe": "ht-shoe.png", "megaphone": "ht-megaphone.png",
}
# emoji in the old specs -> the page's signature object
EMOJI_OBJ = {
    "🏦": "piggy", "🙈": "ok", "🔍": "point", "📝": "point", "⏳": "hourglass", "🧥": "ok", "🫠": "ok", "🏠": "piggy", "🕐": "clock",
    "🎉": "ok", "📞": "phone", "🍼": "piggy", "🎁": "point", "💰": "piggy", "📄": "point", "🏆": "ok", "📬": "phone",
    "✂️": "point", "🗓️": "phone", "💬": "chat", "🛒": "phone", "🥱": "cup", "🍝": "phone", "🧾": "phone", "🥚": "point",
    "🧠": "cup", "📩": "phone", "📧": "phone", "🙇": "chat", "⏰": "clock", "⏱️": "clock", "🐇": "hourglass", "🔒": "clock",
    "📣": "megaphone", "📚": "hourglass", "🌙": "shoe", "🫶": "ok", "🧺": "shoe", "🌡️": "point", "🤧": "shoe", "🗝️": "point",
}


def css(brand, W, H):
    return f"""{FONTS}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
.page{{position:absolute;inset:0;overflow:hidden}}
.grain{{position:absolute;inset:0;background:url('{uri(GRAIN)}') 0 0/420px 420px;mix-blend-mode:multiply;opacity:.55;pointer-events:none}}
.glow{{position:absolute;inset:0;background:radial-gradient(ellipse 70% 55% at 50% 42%,rgba(255,255,255,.28),rgba(255,255,255,0) 70%);pointer-events:none}}
.S{{{SERIF[brand]};text-align:center}}
.S .pill,.pill{{border-radius:.42em;padding:0 .12em .02em;margin:0 -.04em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.hand{{font-family:'Caveat Brush';color:{ACCENT[brand]};line-height:1.02;text-align:center}}
.obj{{filter:drop-shadow(0 18px 22px rgba(20,20,40,.16)) drop-shadow(0 4px 6px rgba(20,20,40,.10))}}
.stamp{{position:absolute}}
"""


def dual(text, f, cls="S fit", style=""):
    """Pills on a layer UNDER the words (tight leading never lets a pill cover the line above)."""
    t = pills(text, f)
    under = re.sub(r'class="pill" style="background:([^"]+)"', r'class="pill" style="background:\1;color:transparent"', t)
    over = re.sub(r'class="pill" style="background:[^"]+"', 'class="pill" style="background:transparent"', t)
    return (f'<div class="{cls}" style="position:relative;{style}"><div style="position:absolute;inset:0;color:transparent">{under}</div>'
            f'<div style="position:relative">{over}</div></div>')


def pills(text, f, rot=0):
    """'*a b*' -> one pill per run, alternating the field's two pill colours; ' / ' -> line break."""
    k = [0]

    def rep(m):
        col = f["p1"] if k[0] % 2 == 0 else f["p2"]
        k[0] += 1
        return f'<span class="pill" style="background:{col}">{m.group(1)}</span>'
    out = re.sub(r"\*(.+?)\*", rep, text)
    return out.replace(" / ", "<br>")


def stamp(brand, x, y, size=190, rot=-12):
    """Round brand stamp: cream disc, ink ring, circular caps text, the page mark in the middle."""
    ink = FIELDS[brand][next(iter(FIELDS[brand]))]["ink"]
    txt = f"{NAME[brand].upper()} · {TAG[brand]} · "
    r = 70
    return f"""<svg class="stamp" style="position:absolute;left:{x}px;top:{y}px;width:{size}px;height:{size}px;transform:rotate({rot}deg)" viewBox="0 0 200 200">
<defs><path id="sp" d="M100,100 m-{r},0 a{r},{r} 0 1,1 {2 * r},0 a{r},{r} 0 1,1 -{2 * r},0"/></defs>
<circle cx="100" cy="100" r="96" fill="{STAMP_BG[brand]}" stroke="{ink}" stroke-width="4"/>
<text font-family="Fraunces" font-weight="700" font-size="17.5" letter-spacing="2.2" fill="{ink}"><textPath href="#sp" textLength="{2 * math.pi * r - 6:.0f}">{txt}</textPath></text>
<circle cx="100" cy="100" r="44" fill="none" stroke="{ink}" stroke-width="2"/>
<image href="{uri(ASSETS / MARK[brand])}" x="66" y="66" width="68" height="68"/>
</svg>"""


def obj(name, x, y, w, rot=0, flip=False, z=3):
    if name == "phone":
        return phone(x, y, w, rot, z)
    if name == "chat":
        return chat(x, y, w, rot, z)
    t = f"rotate({rot}deg)" + (" scaleX(-1)" if flip else "")
    return f'<img class="obj" src="{uri(ASSETS / OBJ[name])}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:{t};z-index:{z}">'


def phone(x, y, w, rot=0, z=3):
    """Black-and-white phone with chat bubbles (Hourback signature), drawn so it halftones with the rest."""
    h = int(w * 1.95)
    return f"""<div class="obj" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);z-index:{z};
border-radius:{w * .16:.0f}px;background:#1b1b1f;padding:{w * .05:.0f}px;box-shadow:inset 0 0 0 3px #4a4a52">
<div style="width:100%;height:100%;border-radius:{w * .12:.0f}px;background:repeating-radial-gradient(circle at 50% 50%,#f4f4f4 0 1.2px,#e9e9ea 1.3px 4px);position:relative;overflow:hidden">
<div style="position:absolute;left:50%;top:{w * .04:.0f}px;transform:translateX(-50%);width:{w * .3:.0f}px;height:{w * .07:.0f}px;border-radius:99px;background:#1b1b1f"></div>
<div style="position:absolute;left:8%;top:22%;width:62%;height:{w * .16:.0f}px;border-radius:{w * .06:.0f}px {w * .06:.0f}px {w * .06:.0f}px 4px;background:#fff;box-shadow:0 2px 0 #ccc"></div>
<div style="position:absolute;right:8%;top:38%;width:58%;height:{w * .16:.0f}px;border-radius:{w * .06:.0f}px {w * .06:.0f}px 4px {w * .06:.0f}px;background:#2a2a30"></div>
<div style="position:absolute;left:8%;top:54%;width:70%;height:{w * .22:.0f}px;border-radius:{w * .06:.0f}px {w * .06:.0f}px {w * .06:.0f}px 4px;background:#fff;box-shadow:0 2px 0 #ccc"></div>
<div style="position:absolute;right:8%;top:76%;width:40%;height:{w * .14:.0f}px;border-radius:{w * .06:.0f}px {w * .06:.0f}px 4px {w * .06:.0f}px;background:#2a2a30"></div>
</div></div>"""


def chat(x, y, w, rot=0, z=3, lines=("…", "", "")):
    """Three stacked chat bubbles, white + ink (Hourback)."""
    b = []
    for i, (wd, side, dark) in enumerate([(0.82, "l", False), (0.62, "r", True), (0.74, "l", False)]):
        col, edge = ("#2a2a30", "#2a2a30") if dark else ("#ffffff", "#2a2a30")
        r = w * 0.09
        pos = "left:0" if side == "l" else "right:0"
        tail = f"border-bottom-left-radius:6px" if side == "l" else "border-bottom-right-radius:6px"
        dots = "".join(f'<i style="display:inline-block;width:{w * .04:.0f}px;height:{w * .04:.0f}px;border-radius:50%;margin:0 {w * .015:.0f}px;background:{"#fff" if dark else "#2a2a30"}"></i>' for _ in range(3)) if i == 1 else ""
        b.append(f'<div style="position:absolute;{pos};top:{i * w * 0.27:.0f}px;width:{w * wd:.0f}px;height:{w * 0.2:.0f}px;background:{col};'
                 f'border:3px solid {edge};border-radius:{r:.0f}px;{tail};display:flex;align-items:center;justify-content:center">{dots}</div>')
    return (f'<div class="obj" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.76:.0f}px;transform:rotate({rot}deg);z-index:{z}">'
            + "".join(b) + "</div>")


def save_line(text, x, y, w, size=64, rot=-3, brand="fullyfunded"):
    return (f'<div class="hand" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;transform:rotate({rot}deg);'
            f'z-index:4">{text}</div>')


def field_bg(f):
    return f'<div style="position:absolute;inset:0;background:{f["bg"]}"></div><div class="glow"></div><div class="grain"></div>'


FIT_JS = """(maxw) => { document.querySelectorAll('.fit').forEach(h => { const mw = +(h.dataset.w || maxw);
  for (let k = 0; k < 14; k++) { const r = document.createRange(); r.selectNodeContents(h); let lo = 1e9, hi = -1e9;
    for (const q of r.getClientRects()) { if (q.width < 1) continue; lo = Math.min(lo, q.left); hi = Math.max(hi, q.right); }
    const mh = +(h.dataset.h || 1e9);
    if (hi - lo <= mw && h.getBoundingClientRect().height <= mh) break;
    h.style.fontSize = (parseFloat(getComputedStyle(h).fontSize) * 0.95) + 'px'; } }); }"""

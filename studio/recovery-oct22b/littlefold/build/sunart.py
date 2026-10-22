#!/usr/bin/env python3
"""Littlefold "Washing-line morning" art kit (recovery Oct 22b).

Founder note (Oct 22 evening): the burgundy Night Light revision improved the message but missed the emotion.
This kit keeps the facts, the type family (Fraunces display, Lora italic, Caveat Brush, Poppins chips) and the
round stamp, and swaps the dark lamp circle for a sunlit illustrated world:
  - a pastel sky (dawn blush -> morning butter), a sleepy sun character that wakes up on the "Do this" beat,
  - sage hills with a little cottage, cream clouds,
  - the Littlefold washing line: tiny pastel clothes, pegged one per beat (the page's progress motif:
    little things, folded and hung with care).
All parts are original SVG drawn here. No children or people are drawn.
"""
import math
import os
import sys
import tempfile
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio" / "editorial"))
import edkit as K  # noqa: E402
from PIL import Image  # noqa: E402

B = "littlefold"
INK = "#3A1F3D"
KICK = "#B23A62"          # deeper berry for Caveat kickers: 4.9:1 on the blush sky
PLUM = "#6B3B5A"          # soft outline colour for illustrations
CREAM = "#FFF8EE"
PINK, BLUE, BUTTER, SAGE, PEACH = "#FFB9CF", "#BFD9F2", "#FFE08A", "#BFD8B0", "#FFC8A8"
F = dict(p1="#FFE08A", p2="#CFE3F6")   # pills: butter, then soft blue
SCR = Path(os.environ.get("LF_SCR", "/tmp/claude-0/-home-claude/60837be5-8cde-507a-87a7-2bafa6fa6f6c/scratchpad/lfsun"))
SCR.mkdir(parents=True, exist_ok=True)

EXTRA_CSS = """
.lora{font-family:Lora;font-style:italic;font-weight:600}
.pop{font-family:Poppins;font-weight:500}
.chipf{display:inline-block;font-family:Poppins;font-weight:500;color:#3A1F3D;background:#FFF8EE;border:2px solid #6B3B5A;border-radius:99px;padding:8px 24px;white-space:nowrap;box-shadow:0 4px 0 rgba(107,59,90,.12)}
.kick{position:absolute;left:0;right:0;text-align:center;font-family:Poppins;font-weight:600;letter-spacing:.28em}
.card{position:absolute;background:rgba(255,250,243,.94);border:2.5px solid #6B3B5A;border-radius:34px;box-shadow:0 10px 0 rgba(107,59,90,.10)}
"""

# ---------------------------------------------------------------- sky / light
SKIES = {
    "dawn": ["#C5D8F2 0%", "#D9DCF2 24%", "#F6E0EC 44%", "#FFE2E3 58%", "#FFDCC6 70%", "#FFD9A8 80%", "#FFE5B0 100%"],
    "morning": ["#BCDDF6 0%", "#D6ECF8 26%", "#FFF4EA 50%", "#FFF0D6 66%", "#FFE9B4 80%", "#FFE6A2 100%"],
    "afternoon": ["#C3DDF4 0%", "#E3E3F2 26%", "#FBE6EC 46%", "#FFE6D2 62%", "#FFD8B4 80%", "#FFE3B0 100%"],
}


def sky(W, H, kind, haze_y=0.44, horizon=0.77):
    stops = ",".join(SKIES[kind])
    return (f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,{stops})"></div>'
            f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse {W*0.62:.0f}px {H*0.16:.0f}px at 50% {horizon*100:.0f}%,rgba(255,246,214,.85),rgba(255,246,214,0) 100%)"></div>'
            f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse {W*0.55:.0f}px {H*0.2:.0f}px at 50% {haze_y*100:.0f}%,rgba(255,251,246,.55),rgba(255,251,246,0) 100%)"></div>'
            f'<div class="grain" style="opacity:.32"></div>')


def sun_svg(size=520, awake=False):
    """Sun character. Sleepy: closed downward eyes. Awake: happy upturned eyes, open smile, rosy cheeks."""
    eyes = ('<path d="M-46 -4 q16 16 32 0 M14 -4 q16 16 32 0" stroke="#B8653A" stroke-width="7" fill="none" stroke-linecap="round"/>'
            if not awake else
            '<path d="M-46 2 q16 -20 32 0 M14 2 q16 -20 32 0" stroke="#B8653A" stroke-width="7" fill="none" stroke-linecap="round"/>')
    mouth = ('<path d="M-14 30 q14 10 28 0" stroke="#B8653A" stroke-width="6" fill="none" stroke-linecap="round"/>' if not awake else
             '<path d="M-20 24 q20 26 40 0 z" fill="#E77F72" stroke="#B8653A" stroke-width="5" stroke-linejoin="round"/>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="-260 -260 520 520">
<defs><radialGradient id="gl"><stop offset="0" stop-color="#FFF2B8" stop-opacity=".95"/><stop offset=".45" stop-color="#FFE7A0" stop-opacity=".55"/><stop offset="1" stop-color="#FFE7A0" stop-opacity="0"/></radialGradient>
<radialGradient id="dk" cx=".4" cy=".35"><stop offset="0" stop-color="#FFE9A6"/><stop offset=".7" stop-color="#FFD36B"/><stop offset="1" stop-color="#FFC25A"/></radialGradient></defs>
<circle r="258" fill="url(#gl)"/>
<circle r="122" fill="url(#dk)" stroke="#F2A94B" stroke-width="4"/>
{eyes}{mouth}
<circle cx="-62" cy="26" r="17" fill="#FF9EA8" opacity=".55"/><circle cx="62" cy="26" r="17" fill="#FF9EA8" opacity=".55"/>
</svg>"""


def rays_svg(size=1500, n=14):
    w = []
    for i in range(n):
        a0 = (i / n) * 2 * math.pi
        a1 = a0 + math.pi / n * 0.55
        r = size / 2
        w.append(f'<path d="M0 0 L{r*math.cos(a0):.1f} {r*math.sin(a0):.1f} A{r} {r} 0 0 1 {r*math.cos(a1):.1f} {r*math.sin(a1):.1f} Z" fill="url(#rr)"/>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="{-size/2} {-size/2} {size} {size}">
<defs><radialGradient id="rr" cx="0" cy="0" r="{size/2}" gradientUnits="userSpaceOnUse"><stop offset=".12" stop-color="#FFF0B0" stop-opacity=".75"/><stop offset=".6" stop-color="#FFE9A8" stop-opacity=".25"/><stop offset="1" stop-color="#FFE9A8" stop-opacity="0"/></radialGradient></defs>
{''.join(w)}</svg>"""


def cloud_svg(w=420, tint="#FFFAF3"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{w*0.42:.0f}" viewBox="0 0 420 176">
<g fill="#E2E9F6"><ellipse cx="210" cy="150" rx="190" ry="22"/></g>
<g fill="{tint}"><circle cx="120" cy="104" r="56"/><circle cx="200" cy="78" r="72"/><circle cx="290" cy="100" r="58"/><circle cx="350" cy="126" r="38"/><circle cx="66" cy="132" r="36"/>
<rect x="60" y="110" width="310" height="50" rx="25"/></g></svg>"""


def hills_svg(W=1080, H=1920, top=1460, cottage=True, flowers=True):
    s = top - 1460  # vertical offset
    def p(d):
        import re
        return re.sub(r"(-?\d+(?:\.\d+)?) (-?\d+(?:\.\d+)?)", lambda m: f"{m.group(1)} {float(m.group(2))+s:.0f}", d)
    fl = ""
    if flowers:
        import random
        rnd = random.Random(7)
        for i in range(26):
            x = rnd.uniform(30, W - 30)
            y = rnd.uniform(1615, 1900) + s
            c = rnd.choice(["#FFB9CF", "#FFF4D6", "#FFE08A", "#FFC8A8"])
            r = rnd.uniform(6, 10)
            fl += (f'<g transform="translate({x:.0f} {y:.0f})"><path d="M0 0 v18" stroke="#8DB07F" stroke-width="3"/>'
                   + "".join(f'<circle cx="{r*0.9*math.cos(k*1.2566):.1f}" cy="{r*0.9*math.sin(k*1.2566):.1f}" r="{r*0.62:.1f}" fill="{c}"/>' for k in range(5))
                   + f'<circle r="{r*0.45:.1f}" fill="#F2A94B"/></g>')
    ck = ""
    if cottage:
        x, y = 800, 1352 + s
        ck = f"""<g transform="translate({x} {y})">
<rect x="58" y="-36" width="16" height="34" fill="{PEACH}" stroke="{PLUM}" stroke-width="3"/>
<rect x="0" y="40" width="120" height="86" rx="6" fill="#FFF6EA" stroke="{PLUM}" stroke-width="4"/>
<path d="M-14 46 L60 -14 L134 46 Z" fill="#F6A98A" stroke="{PLUM}" stroke-width="4" stroke-linejoin="round"/>
<rect x="18" y="62" width="32" height="30" rx="5" fill="#FFE59A" stroke="{PLUM}" stroke-width="3"/>
<path d="M34 62 v30 M18 77 h32" stroke="{PLUM}" stroke-width="2"/>
<path d="M72 126 v-44 a14 14 0 0 1 28 0 v44" fill="{SAGE}" stroke="{PLUM}" stroke-width="3"/>
<g transform="translate(225 46) scale(.8)"><rect x="-6" y="40" width="12" height="60" fill="#C99A7A"/><circle cx="0" cy="22" r="40" fill="#B5D1A7" stroke="{PLUM}" stroke-width="3"/><circle cx="-24" cy="44" r="26" fill="#B5D1A7" stroke="{PLUM}" stroke-width="3"/><circle cx="24" cy="44" r="26" fill="#B5D1A7" stroke="{PLUM}" stroke-width="3"/></g>
</g>"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<path d="{p('M0 1500 C 250 1418 420 1444 600 1478 S 950 1426 1080 1456 L1080 1920 L0 1920 Z')}" fill="#D7E8CB"/>
{ck}
<path d="{p('M0 1608 C 200 1548 380 1566 540 1594 S 900 1534 1080 1572 V1920 H0 Z')}" fill="#BCD7AE"/>
<path d="{p('M0 1736 C 300 1668 700 1716 1080 1660 V1920 H0 Z')}" fill="#A8CA9A"/>
{fl}</svg>"""


# ---------------------------------------------------------------- the washing line
def peg(x, y):
    return f'<rect x="{x-8}" y="{y-16}" width="16" height="34" rx="5" fill="#E9BE92" stroke="{PLUM}" stroke-width="3"/>'


def garment_svg(kind, w=170):
    """Pastel baby clothes, hung from (85, 14) in a 170x220 box."""
    o = f'stroke="{PLUM}" stroke-width="4" stroke-linejoin="round"'
    if kind == "onesie":
        body = (f'<path d="M52 18 L30 28 L8 60 L30 76 L44 62 L44 150 Q44 170 64 172 L72 192 L98 192 L106 172 Q126 170 126 150 L126 62 L140 76 L162 60 L140 28 L118 18 Q85 44 52 18 Z" fill="{PINK}" {o}/>'
                f'<path d="M85 100 c-8 -14 -28 -6 -20 8 l20 18 l20 -18 c8 -14 -12 -22 -20 -8 z" fill="#FFF0F4" stroke="{PLUM}" stroke-width="3"/>'
                f'<circle cx="78" cy="184" r="3" fill="{PLUM}"/><circle cx="92" cy="184" r="3" fill="{PLUM}"/>'
                + peg(56, 20) + peg(114, 20))
    elif kind == "sock":
        body = (f'<path d="M62 16 L108 16 L108 112 Q108 124 120 132 L148 150 Q166 166 150 182 Q136 196 114 184 L68 156 Q54 146 58 128 Z" fill="{BLUE}" {o}/>'
                f'<path d="M62 34 h46 M62 48 h46" stroke="{PLUM}" stroke-width="3"/>'
                f'<path d="M126 140 Q142 150 150 166" stroke="#FFF8EE" stroke-width="6" fill="none" stroke-linecap="round" opacity=".8"/>'
                + peg(85, 18))
    elif kind == "bib":
        body = (f'<path d="M40 22 Q30 40 32 70 A54 60 0 1 0 138 70 Q140 40 130 22 Q118 70 85 70 Q52 70 40 22 Z" fill="{BUTTER}" {o}/>'
                + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="#FFF8EE"/>' for x, y in [(62, 110), (85, 132), (108, 110), (72, 150), (98, 152), (85, 92)])
                + peg(42, 20) + peg(128, 20))
    elif kind == "hat":
        body = (f'<circle cx="85" cy="30" r="20" fill="#FFF8EE" {o}/>'
                f'<path d="M30 140 Q26 52 85 48 Q144 52 140 140 Z" fill="{SAGE}" {o}/>'
                f'<rect x="22" y="128" width="126" height="34" rx="14" fill="#A9CB9C" {o}/>'
                + "".join(f'<path d="M{x} 132 v26" stroke="{PLUM}" stroke-width="2" opacity=".6"/>' for x in range(36, 140, 14))
                + peg(85, 16))
    elif kind == "dress":
        body = (f'<path d="M58 20 L112 20 L120 64 L152 168 Q118 186 85 180 Q52 186 18 168 L50 64 Z" fill="{PEACH}" {o}/>'
                f'<path d="M58 20 Q85 46 112 20" fill="#FFF8EE" {o}/>'
                f'<path d="M30 160 Q46 172 62 164 Q78 176 94 166 Q110 176 126 164 Q138 172 146 160" stroke="#FFF8EE" stroke-width="5" fill="none" stroke-linecap="round"/>'
                + "".join(f'<circle cx="85" cy="{y}" r="5" fill="#FFF8EE" stroke="{PLUM}" stroke-width="2"/>' for y in (62, 86, 110))
                + peg(62, 22) + peg(108, 22))
    elif kind == "star":  # little knitted star toy
        pts = " ".join(f"{85+ (62 if i%2==0 else 28)*math.cos(-math.pi/2+i*math.pi/5):.1f},{110+(62 if i%2==0 else 28)*math.sin(-math.pi/2+i*math.pi/5):.1f}" for i in range(10))
        body = (f'<path d="M85 16 V52" stroke="{PLUM}" stroke-width="3"/><polygon points="{pts}" fill="{BUTTER}" {o}/>'
                + peg(85, 18))
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{w*220/170:.0f}" viewBox="0 0 170 220">{body}</svg>'


def line_y(x, y0=300, sag=50, W=1080):
    t = (x + 20) / (W + 40)
    return y0 + 4 * sag * t * (1 - t)


def line_svg(W=1080, H=1920, y0=300, sag=50):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<path d="M-20 {y0} Q{W/2} {y0+2*sag} {W+20} {y0}" stroke="{PLUM}" stroke-width="5" fill="none" stroke-linecap="round"/></svg>')


# ---------------------------------------------------------------- rendering
_pw = None


def _browser():
    global _pw
    if _pw is None:
        from playwright.sync_api import sync_playwright
        p = sync_playwright().start()
        _pw = (p, p.chromium.launch())
    return _pw[1]


def page(W, H, body, transparent=False):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{K.css(B, W, H)}{EXTRA_CSS}"
            f"html,body{{background:{'transparent' if transparent else '#FFF1E3'}}}</style></head>"
            f"<body><div class='page'>{body}</div></body></html>")


def render(html, out, W, H, transparent=False, fit=900):
    br = _browser()
    pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, dir=SCR) as f:
        f.write(html)
        tmp = f.name
    pg.goto(Path(tmp).as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(200)
    pg.evaluate(K.FIT_JS, fit)
    png = tmp + ".png"
    pg.screenshot(path=png, omit_background=transparent)
    pg.close()
    im = Image.open(png).resize((W, H), Image.LANCZOS)
    os.remove(tmp)
    os.remove(png)
    if transparent:
        im = im.convert("RGBA")
        if str(out).endswith(".png"):
            im.save(out)
        return im
    im = im.convert("RGB")
    im.save(out, quality=92, subsampling=0)
    return im


def svg_img(svg, w, h, name):
    """Render a standalone SVG sprite to an RGBA PIL image at 2x then Lanczos down."""
    body = f'<div style="position:absolute;left:0;top:0;width:{w}px;height:{h}px">{svg}</div>'
    return render(page(w, h, body, transparent=True), SCR / f"{name}.png", w, h, transparent=True)


def abs_svg(svg, x, y, w=None, rot=0):
    st = f"position:absolute;left:{x}px;top:{y}px;" + (f"width:{w}px;" if w else "") + (f"transform:rotate({rot}deg);" if rot else "")
    return f'<div style="{st}">{svg}</div>'

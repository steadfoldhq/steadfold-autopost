#!/usr/bin/env python3
"""Littlefold recovery (Oct 22): "Night Light" (v0.5 floor) reconciled with brand-system-v4.

v0.5 gives the motif: the answer sits inside a warm circle of lamp light; day tiles are cream with an award rosette.
v4 keeps: Sherbet palette (cream / pink / butter / peach, berry accent, LF ink #3A1F3D, Ep. deep berry #7A2149),
Fraunces soft serif + pills under key words, Caveat Brush save-line, the round brand stamp, paper grain.
Night tiles use the v4 Ep. deep berry -> LF ink as the dark (never black), with the lamp glow in the centre.

Renders HTML with Playwright Chromium at 2x and downsamples with Lanczos (v4 section 7).
"""
import sys, tempfile, os
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio" / "editorial"))
import edkit as K  # noqa: E402
from PIL import Image  # noqa: E402

B = "littlefold"
INK = "#3A1F3D"
BERRY = "#D9497A"
DEEP = "#7A2149"
CREAM = "#FFF8EE"
P1, P2 = "#FFBFD3", "#FFE59A"
F = dict(p1=P1, p2=P2)
FD = dict(p1=P1, p2="#FFF8EE")

EXTRA_CSS = f"""
.lora{{font-family:Lora;font-style:italic;font-weight:600}}
.pop{{font-family:Poppins;font-weight:500}}
.chip{{position:absolute;font-family:Poppins;font-weight:500;border:2px solid currentColor;border-radius:99px;padding:6px 22px;white-space:nowrap}}
.kick{{position:absolute;left:0;right:0;text-align:center;font-family:Poppins;font-weight:600;letter-spacing:.28em}}
"""


def night_bg(W, H, cx=.5, cy=.42, r=.46, day=False):
    """Lamp glow. Night: deep berry -> ink edges. Day: cream field with a butter/peach morning glow."""
    R = r * W
    if not day:
        g = (f"radial-gradient(circle {R:.0f}px at {cx*100}% {cy*100}%, #FFF4E2 0%, #FFE9C9 34%, #FFD3AE 58%, "
             f"rgba(255,191,160,.55) 74%, rgba(122,33,73,0) 100%),"
             f"radial-gradient(circle {R*2.4:.0f}px at {cx*100}% {cy*100}%, #8A2B55 0%, {DEEP} 40%, #4E1A3C 75%, {INK} 100%)")
    else:
        g = (f"radial-gradient(circle {R:.0f}px at {cx*100}% {cy*100}%, #FFF6D8 0%, #FFEDB0 40%, rgba(255,229,154,.65) 66%, rgba(255,241,227,0) 100%),"
             f"radial-gradient(circle {W*.42:.0f}px at 4% 96%, #FFD3E0 0%, rgba(255,211,224,0) 100%),"
             f"radial-gradient(circle {W*.36:.0f}px at 98% 6%, #FFDCC4 0%, rgba(255,220,196,0) 100%),"
             f"#FFF1E3")
    return f'<div style="position:absolute;inset:0;background:{g}"></div><div class="grain" style="opacity:{.35 if not day else .5}"></div>'


def lamp(x, y, s=1.0, col=DEEP, shade="#FFD3AE"):
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{150*s:.0f}px;height:{190*s:.0f}px" viewBox="0 0 150 190">'
            f'<path d="M40 20 L110 20 L132 82 L18 82 Z" fill="{shade}" stroke="{col}" stroke-width="5" stroke-linejoin="round"/>'
            f'<rect x="70" y="82" width="10" height="78" fill="{col}"/><rect x="30" y="158" width="90" height="14" rx="7" fill="{col}"/>'
            f'</svg>')


def drop(x, y, w, label="400", sub="IU"):
    h = w * 1.3
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h:.0f}px" viewBox="0 0 200 260">'
            f'<path d="M100 8 C 100 8 22 118 22 170 A 78 78 0 0 0 178 170 C 178 118 100 8 100 8 Z" fill="#FFB48A" stroke="{DEEP}" stroke-width="7"/>'
            f'<path d="M46 150 A 56 56 0 0 0 60 196" fill="none" stroke="#FFF1DC" stroke-width="9" stroke-linecap="round" opacity=".8"/>'
            f'<text x="100" y="186" text-anchor="middle" font-family="Fraunces" font-weight="700" font-size="58" fill="{DEEP}">{label}</text>'
            f'<text x="100" y="226" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="24" letter-spacing="3" fill="{DEEP}">{sub}</text>'
            f'</svg>')


def rosette(x, y, w, title="Showered.", col="#FFBFD3", ribbon2="#F6C9C4", icon=""):
    pts = []
    import math
    for i in range(48):
        a = i / 48 * 2 * math.pi
        rr = 150 if i % 2 == 0 else 134
        pts.append(f"{200+rr*math.cos(a):.1f},{180+rr*math.sin(a):.1f}")
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w*1.45:.0f}px" viewBox="0 0 400 580">'
            f'<path d="M150 270 L95 540 L150 500 L185 560 L215 300 Z" fill="{DEEP}"/>'
            f'<path d="M250 270 L305 540 L250 500 L215 560 L185 300 Z" fill="{ribbon2}" stroke="{DEEP}" stroke-width="3"/>'
            f'<polygon points="{" ".join(pts)}" fill="{col}" stroke="{DEEP}" stroke-width="4"/>'
            f'<circle cx="200" cy="180" r="112" fill="{CREAM}" stroke="{DEEP}" stroke-width="5"/>'
            f'<circle cx="200" cy="180" r="98" fill="none" stroke="{DEEP}" stroke-width="2" stroke-dasharray="6 7"/>'
            f'<text x="200" y="120" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="19" letter-spacing="4" fill="{DEEP}">SMALL WIN</text>'
            f'{icon}'
            f'<text x="200" y="244" text-anchor="middle" font-family="Lora" font-style="italic" font-weight="600" font-size="31" fill="{INK}">{title}</text>'
            f'</svg>')


SHOWER_ICON = (f'<g transform="translate(200 172)" stroke="{DEEP}" stroke-width="7" stroke-linecap="round" fill="none">'
               f'<path d="M-46 -22 L46 -22"/><path d="M0 -22 L0 -42 L30 -42"/>'
               + "".join(f'<path d="M{dx} {dy} l-3 12"/>' for dx, dy in [(-34, -2), (-12, -2), (12, -2), (34, -2), (-23, 22), (0, 22), (23, 22)])
               + '</g>')


def page(W, H, body, transparent=False):
    bg = "" if transparent else ""
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{K.css(B, W, H)}{EXTRA_CSS}"
            f"html,body{{background:{'transparent' if transparent else '#FFF1E3'}}}</style></head>"
            f"<body><div class='page'>{body}</div></body></html>")


_pw = None


def _browser():
    global _pw
    if _pw is None:
        from playwright.sync_api import sync_playwright
        p = sync_playwright().start()
        _pw = (p, p.chromium.launch())
    return _pw[1]


def render(html, out, W, H, transparent=False, jpeg=True):
    br = _browser()
    pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
        tmp = f.name
    pg.goto(Path(tmp).as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(250)
    pg.evaluate(K.FIT_JS, 900)
    png = tmp + ".png"
    pg.screenshot(path=png, omit_background=transparent)
    pg.close()
    im = Image.open(png)
    im = im.resize((W, H), Image.LANCZOS)
    if transparent:
        im.save(out)
    else:
        im = im.convert("RGB")
        if jpeg:
            im.save(out, quality=92, subsampling=0)
        else:
            im.save(out)
    os.remove(tmp)
    os.remove(png)
    return out

"""Locked Hour recovery kit (Oct 22): v4 editorial look (Instrument Serif + pills + halftone object + Caveat line + stamp,
butter/cream/pink fields with the zine dot grid) carrying the v0.5 'Two-Ink Hour' signature: the 60:00 ring with a
keyhole notch, a pink riso plate offset on the one big word, mono source notes. No black full fields, no pointing hand,
no piggy bank."""
import sys, os, subprocess, tempfile
from pathlib import Path
sys.path.insert(0, "/home/claude/steadfold-autopost/studio/editorial")
import edkit  # noqa: E402
from PIL import Image  # noqa: E402

B = "lockedhour"
F = edkit.FIELDS[B]
INK = "#1B1717"
PINK = "#FF5CA8"
DPINK = "#E0306C"
YEL = "#FFD43B"
BUTTER = "#FFE27A"
CREAM = "#FFF4E0"
ACC = edkit.ACCENT[B]
A = edkit.ASSETS

def obj(name):
    return edkit.uri(A / edkit.OBJ[name])

def css(W, H, field="dots"):
    f = F[field]
    return edkit.css(B, W, H) + f"""
@font-face{{font-family:'DejaVu Sans Mono';src:local('DejaVu Sans Mono')}}
body{{background:{f['bg']}}}
.field{{position:absolute;inset:0;background-color:{f['bg']};
 background-image:radial-gradient(rgba(20,20,20,.12) 1.2px,transparent 1.5px);background-size:30px 30px;background-position:15px 15px}}
.mono{{font-family:'DejaVu Sans Mono',monospace;color:{INK};letter-spacing:.01em}}
.label{{display:inline-block;background:{INK};color:{CREAM};font-family:'Inter Display',Inter,sans-serif;font-weight:800;
 letter-spacing:.12em;text-transform:uppercase;border-radius:8px}}
.riso{{text-shadow:.045em .035em 0 {PINK}}}
.card{{position:absolute;background:#FFFDF6;border:5px solid {INK};border-radius:26px;box-shadow:12px 12px 0 {INK}}}
.ink{{color:{INK}}}
.hand2{{font-family:'Caveat Brush';color:{ACC}}}
.dothis{{font-family:'Caveat Brush';color:{ACC}}}
"""

def pills(text, field="dots"):
    return edkit.pills(text, F[field])

def dual(text, field="dots", style=""):
    return edkit.dual(text, F[field], cls="S", style=style)

def stamp(x, y, size=170, rot=-12):
    return edkit.stamp(B, x, y, size, rot)

def ring(size, frac, centre="", sub="", stroke=None, col=PINK, track="rgba(27,23,23,.13)", notch=True, ticks=True,
         marks=(), font=None):
    """The 60:00 ring with a keyhole notch at 12 o'clock. frac 0..1 filled clockwise from 12."""
    s = size; r = s * 0.40; cx = cy = s / 2; sw = stroke or s * 0.085
    C = 2 * 3.14159265 * r
    tk = ""
    if ticks:
        import math
        for i in range(60):
            a = math.radians(i * 6 - 90); L = s * (0.035 if i % 5 else 0.06)
            r1 = r + sw * 0.75; r2 = r1 + L
            tk += (f'<line x1="{cx+r1*math.cos(a):.1f}" y1="{cy+r1*math.sin(a):.1f}" x2="{cx+r2*math.cos(a):.1f}" '
                   f'y2="{cy+r2*math.sin(a):.1f}" stroke="{INK}" stroke-width="{s*(0.006 if i%5 else 0.011):.1f}" stroke-linecap="round"/>')
    mk = ""
    import math
    for m in marks:  # (fraction, colour)
        a = math.radians(m[0] * 360 - 90)
        mk += (f'<circle cx="{cx+r*math.cos(a):.1f}" cy="{cy+r*math.sin(a):.1f}" r="{sw*0.78:.1f}" fill="{m[1]}" '
               f'stroke="{INK}" stroke-width="{s*0.012:.1f}"/>')
    kh = ""
    if notch:
        kw = sw * 1.1
        kh = (f'<g transform="translate({cx},{cy-r})"><circle r="{kw*0.62:.1f}" fill="{INK}"/>'
              f'<path d="M{-kw*0.32:.1f},0 L{kw*0.32:.1f},0 L{kw*0.5:.1f},{kw*1.25:.1f} L{-kw*0.5:.1f},{kw*1.25:.1f} Z" fill="{INK}"/>'
              f'<circle r="{kw*0.22:.1f}" cy="{-kw*0.05:.1f}" fill="{CREAM}"/></g>')
    fnt = font or s * 0.2
    return f"""<svg width="{s}" height="{s}" viewBox="0 0 {s} {s}" style="overflow:visible">
<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFDF6" stroke="none"/>
<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{track}" stroke-width="{sw}"/>
<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="butt"
 stroke-dasharray="{C*frac:.2f} {C:.2f}" transform="rotate(-90 {cx} {cy})"/>
{tk}{mk}{kh}
<text x="{cx}" y="{cy + fnt*0.33:.1f}" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="{fnt:.1f}" fill="{INK}">{centre}</text>
<text x="{cx}" y="{cy + fnt*0.33 + s*0.10:.1f}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="{s*0.055:.1f}" fill="{INK}" opacity=".75">{sub}</text>
</svg>"""

def page(body, W, H, field="dots", extra=""):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css(W,H,field)}{extra}</style></head><body>" \
           f"<div class='page'><div class='field'></div>{body}<div class='grain'></div></div></body></html>"

def shoot(html_pages, outs, W, H, q=92):
    """Render static pages at 2x and Lanczos down to WxH JPEG."""
    from playwright.sync_api import sync_playwright
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        for html, out in zip(html_pages, outs):
            tf = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, dir="/tmp/claude-0/-home-claude/60837be5-8cde-507a-87a7-2bafa6fa6f6c/scratchpad/lh")
            tf.write(html); tf.close()
            pg.goto("file://" + tf.name); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(250)
            png = tf.name + ".png"; pg.screenshot(path=png)
            Image.open(png).convert("RGB").resize((W, H), Image.LANCZOS).save(out, quality=q, subsampling=0)
            os.unlink(png); os.unlink(tf.name)
        b.close()

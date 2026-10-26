#!/usr/bin/env python3
"""Oct 26 (Social studio, Littlefold maker): 3 am Club No. 3, 2 slides, same layout as No. 1 / No. 2
(oct24_feed.py + oct25_littlefold_feed.py: pills cover on the berry field, halftone shoe, 'new night tip every Mon · Wed · Fri';
inner slide on cream with a drawn object and a source line). Topic = the one No. 2's caption promised:
'when your baby will only sleep on you'. Imports those helpers; edits nothing.

    python3 studio/editorial/oct26_littlefold_feed.py
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import oct24_feed as F  # noqa: E402

LF = F.LF
PID = "lf-3amclub-03"
OUT = F.REPO / "media" / "studio-oct26" / "littlefold" / PID
INKC = "#3A1F3D"

# Gate fixes (Oct 26): the grey toddler sneaker -> a warm drawn sleepy moon (newborn, night); slide 2 says WHO is sleepy;
# the crib shows a baby in a sleep sack on a flat, empty mattress (no loose-blanket read), drawn large to fill the slide.


def svg_moon(x, y, w=330):
    """Sleepy crescent moon with a nightcap, closed smiling eye, rosy cheek, two small stars and a soft glow (Littlefold, drawn)."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;z-index:3;overflow:visible" viewBox="0 0 300 300">'
            '<circle cx="150" cy="160" r="140" fill="#FFF2B8" opacity=".55"/>'
            f'<path d="M190 40 A120 120 0 1 0 250 230 A96 96 0 1 1 190 40 Z" fill="#FFE27E" stroke="{INKC}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M96 150 q14 12 28 0" stroke="{INKC}" stroke-width="6" fill="none" stroke-linecap="round"/>'
            '<circle cx="98" cy="182" r="13" fill="#FF9EA8" opacity=".75"/>'
            f'<path d="M110 206 q12 8 24 -2" stroke="{INKC}" stroke-width="5" fill="none" stroke-linecap="round"/>'
            f'<path d="M150 62 Q110 10 60 30 Q90 40 104 76 Z" fill="#FFBFD3" stroke="{INKC}" stroke-width="5" stroke-linejoin="round"/>'
            f'<circle cx="58" cy="30" r="13" fill="#FFF8EE" stroke="{INKC}" stroke-width="5"/>'
            f'<path d="M248 70 l7 16 l17 2 l-13 11 l4 17 l-15 -9 l-15 9 l4 -17 l-13 -11 l17 -2z" fill="#FFF8EE" stroke="{INKC}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M262 160 l5 11 l12 1 l-9 8 l3 12 l-11 -6 l-11 6 l3 -12 l-9 -8 l12 -1z" fill="#FFF8EE" stroke="{INKC}" stroke-width="3.5" stroke-linejoin="round"/>'
            '<text x="196" y="300" font-family="Caveat Brush" font-size="44" fill="#D9497A">z z</text></svg>')


def svg_crib_sack(x, y, w=600):
    """Crib with a baby on their back in a sleep sack on a flat, firm, empty mattress (no blanket, pillow or toys)."""
    bars = "".join(f'<rect x="{46 + k * 34}" y="40" width="10" height="176" rx="5" fill="{INKC}"/>' for k in range(15))
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.62:.0f}px;z-index:3;overflow:visible" viewBox="0 0 600 372">'
            f'<rect x="20" y="10" width="18" height="350" rx="9" fill="{INKC}"/><rect x="562" y="10" width="18" height="350" rx="9" fill="{INKC}"/>'
            f'<rect x="20" y="30" width="560" height="16" rx="8" fill="{INKC}"/>'
            + bars.replace('height="176"', 'height="172"') +
            f'<rect x="38" y="214" width="524" height="34" rx="10" fill="#FFF8EE" stroke="{INKC}" stroke-width="5"/>'
            # baby: head left, sleep sack (zip line + shoulder straps), arms out, on the back
            f'<path d="M190 214 Q186 160 236 152 L410 156 Q446 162 446 214 Z" fill="#FFBFD3" stroke="{INKC}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M240 186 H432" stroke="{INKC}" stroke-width="3.5" stroke-dasharray="7 7"/>'
            f'<path d="M226 158 Q214 132 186 130" stroke="{INKC}" stroke-width="20" stroke-linecap="round" fill="none"/>'
            f'<path d="M226 158 Q214 132 186 130" stroke="#FFDCC4" stroke-width="12" stroke-linecap="round" fill="none"/>'
            f'<circle cx="150" cy="176" r="44" fill="#FFDCC4" stroke="{INKC}" stroke-width="5"/>'
            f'<path d="M130 170 q8 7 16 0 M154 168 q8 7 16 0" stroke="{INKC}" stroke-width="4.5" fill="none" stroke-linecap="round"/>'
            f'<path d="M144 192 q8 5 16 0" stroke="#9A4E2A" stroke-width="4" fill="none" stroke-linecap="round"/>'
            '<circle cx="128" cy="186" r="8" fill="#FF9EA8" opacity=".7"/>'
            f'<path d="M126 136 q12 -14 26 -2" stroke="#A0674A" stroke-width="4.5" fill="none" stroke-linecap="round"/>'
            f'<rect x="20" y="246" width="560" height="16" rx="8" fill="{INKC}"/>'
            '<text x="470" y="30" font-family="Caveat Brush" font-size="52" fill="#D9497A">z z</text></svg>')


def cover():
    import re
    c = dict(lay="pills", f="berry", kicker="3 am club · no. 3", text="It's 3 am. / They'll only / *sleep on me.*", obj="shoe",
             at="br", save=F.SAVE_LF)
    body = F.lift_save(F.C.LAYOUTS["pills"](LF, c))
    body = re.sub(r'<img class="obj"[^>]*ht-shoe[^>]*>', "", body)
    assert "ht-shoe" not in body
    return F.C.page(LF, "berry", body + svg_moon(690, 940, 340), F.W, F.H)


S2 = dict(f="cream", text="Feeling sleepy yourself? / Move baby to / *their own crib.*", sub="on their back, in a flat, clear space",
          src="The Lullaby Trust · NHS")


def slide2():
    body = F.C.inner(LF, S2, 1, 2).replace("top:120px;height:1060px", "top:70px;height:700px", 1)
    return F.C.page(LF, "cream", body + svg_crib_sack(240, 800, 600), F.W, F.H)


PAGES = [cover, slide2]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = F.C.R()
    try:
        for i, fn in enumerate(PAGES, 1):
            r.shot(fn(), F.W, F.H, OUT / f"{i:02d}.jpg")
            print(OUT / f"{i:02d}.jpg", flush=True)
    finally:
        r.close()


if __name__ == "__main__":
    main()

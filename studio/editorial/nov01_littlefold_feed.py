#!/usr/bin/env python3
"""Nov 1 (Social studio, Littlefold maker): 3 am Club No. 5 (Wed Nov 4, 17:00), 3 slides, same layout as No. 4
(oct28_littlefold_feed.py: pills cover on the peach field with the save line, a drawn object bottom right; inner slides on
cream with a drawn object and a source line). Imports oct24_feed and oct28_littlefold_feed; edits nothing.

Topic: 'It's 3 am. Baby's been sick.' Keep feeding (small feeds, more often); fewer wet diapers = get help now.
Facts (checked Nov 1 2026): NHS 'Diarrhoea and vomiting' (nhs.uk/symptoms/diarrhoea-and-vomiting/, last reviewed 21 Dec 2023):
  "carry on breast or bottle feeding your baby – if they're being sick, try giving small feeds more often than usual";
  "give babies on formula or solid foods small sips of water between feeds"; "do not make baby formula weaker";
  "vomiting usually stops in 1 or 2 days"; call 111 if "you're worried about a baby under 12 months", "your child stops
  breast or bottle feeding while they're ill", "a child under 5 years has signs of dehydration, such as fewer wet nappies";
  999/A&E if "yellow-green or green vomit (children)".

    python3 studio/editorial/nov01_littlefold_feed.py
"""
import re
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import oct24_feed as F  # noqa: E402
import oct28_littlefold_feed as P  # noqa: E402  (svg_phone; nothing renders on import)

LF = F.LF
PID = "lf-3amclub-05"
OUT = F.REPO / "media" / "studio-nov01" / "littlefold" / PID
INKC = P.INKC


def bottle(x, y, s=1.0):
    """A drawn baby bottle, origin = top of the teat, ~110 x 270 at s=1."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M30 40 Q50 -6 70 40 Z" fill="#FFE27E" stroke="{INKC}" stroke-width="5" stroke-linejoin="round"/>'
            f'<rect x="12" y="38" width="76" height="30" rx="8" fill="#FFBFD3" stroke="{INKC}" stroke-width="5"/>'
            f'<rect x="4" y="66" width="92" height="210" rx="28" fill="#E3EEF8" stroke="{INKC}" stroke-width="5"/>'
            '<rect x="9" y="170" width="82" height="102" rx="24" fill="#FFFDF6"/>'
            f'<rect x="4" y="66" width="92" height="210" rx="28" fill="none" stroke="{INKC}" stroke-width="5"/>'
            + "".join(f'<path d="M4 {110 + 32 * i} h22" stroke="{INKC}" stroke-width="4"/>' for i in range(4))
            + f'<path d="M50 200 c-7 -12 -24 -5 -17 7 l17 15 l17 -15 c7 -12 -10 -19 -17 -7z" fill="#FFBFD3" stroke="{INKC}" stroke-width="3.5"/></g>')


def svg_cover_obj(x, y, w=340):
    """Cover: a bottle beside a soft muslin cloth with a heart, under a little moon (night, gentle)."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;z-index:3;overflow:visible" viewBox="0 0 300 300">'
            '<circle cx="150" cy="150" r="140" fill="#FFF2B8" opacity=".55"/>'
            f'<path d="M232 34 A34 34 0 1 0 262 84 A26 26 0 1 1 232 34Z" fill="#FFE27E" stroke="{INKC}" stroke-width="4"/>'
            f'<path d="M40 190 Q60 150 120 160 Q170 150 196 186 L186 262 Q120 280 52 262 Z" fill="#CFE3F6" stroke="{INKC}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M60 196 Q120 186 180 200" stroke="{INKC}" stroke-width="3" fill="none" opacity=".5"/>'
            f'<path d="M118 222 c-7 -12 -24 -5 -17 7 l17 15 l17 -15 c7 -12 -10 -19 -17 -7z" fill="#FFBFD3" stroke="{INKC}" stroke-width="3.5"/>'
            + bottle(178, 40, 0.82) + '</svg>')


def svg_feed_clock(x, y, w=560):
    """Slide 2: a bottle, then a clock with three small feed marks close together (small feeds, more often)."""
    marks = "".join(f'<circle cx="{390 + 92 * __import__("math").cos(-1.57 + 0.9 * i)}" cy="{150 + 92 * __import__("math").sin(-1.57 + 0.9 * i)}" r="16" fill="#FFBFD3" stroke="{INKC}" stroke-width="4"/>' for i in range(4))
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.6:.0f}px;z-index:3;overflow:visible" viewBox="0 0 560 336">'
            '<ellipse cx="280" cy="318" rx="270" ry="18" fill="#F6D9C3" opacity=".7"/>'
            + bottle(60, 30, 1.0) +
            f'<circle cx="390" cy="150" r="120" fill="#FFF8EE" stroke="{INKC}" stroke-width="6"/>'
            + marks +
            f'<path d="M390 150 V80 M390 150 L440 176" stroke="{INKC}" stroke-width="8" stroke-linecap="round"/><circle cx="390" cy="150" r="9" fill="{INKC}"/>'
            '<text x="390" y="330" font-family="Caveat Brush" font-size="44" fill="#D9497A" text-anchor="middle">little and often ✓</text>'
            '</svg>')


def svg_diaper(x, y, w=300):
    """Slide 3: a dry diaper with a counting tally under it (fewer wet diapers)."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;z-index:3;overflow:visible" viewBox="0 0 300 300">'
            '<circle cx="150" cy="150" r="140" fill="#FFF2B8" opacity=".55"/>'
            f'<path d="M50 80 H250 Q258 140 214 176 Q190 198 182 236 H118 Q110 198 86 176 Q42 140 50 80Z" fill="#FFF8EE" stroke="{INKC}" stroke-width="6" stroke-linejoin="round"/>'
            f'<rect x="50" y="72" width="200" height="30" rx="10" fill="#CFE3F6" stroke="{INKC}" stroke-width="5"/>'
            f'<path d="M150 150 c-8 -14 -28 -6 -20 8 l20 18 l20 -18 c8 -14 -12 -22 -20 -8z" fill="#FFBFD3" stroke="{INKC}" stroke-width="3.5"/>'
            f'<path d="M86 270 v-30 M106 270 v-30 M126 270 v-30" stroke="{INKC}" stroke-width="6" stroke-linecap="round"/>'
            '<text x="190" y="272" font-family="Caveat Brush" font-size="40" fill="#D9497A">fewer?</text>'
            '</svg>')


def cover():
    c = dict(lay="pills", f="berry", kicker="3 am club · no. 5", text="It's 3 am. / Baby keeps / *throwing up.*", obj="shoe",
             at="br", save=F.SAVE_LF)
    body = F.lift_save(F.C.LAYOUTS["pills"](LF, c))
    body = re.sub(r'<img class="obj"[^>]*ht-shoe[^>]*>', "", body)
    assert "ht-shoe" not in body
    return F.C.page(LF, "berry", body + svg_cover_obj(690, 940, 340), F.W, F.H)


S2 = dict(f="cream", text="Keep feeding: / *small feeds, / more often.*", sub="formula: mix it the usual way.<br>don't water it down.",
          src="NHS · Diarrhoea and vomiting")
S3 = dict(f="cream", text="Fewer wet diapers / than usual? / *Call your doctor / or nurse line now.*", sub="that can mean dehydration.<br>green vomit? go to emergency.",
          src="NHS · Diarrhoea and vomiting")


def slide2():
    body = F.C.inner(LF, S2, 1, 3).replace("top:120px;height:1060px", "top:70px;height:700px", 1)
    return F.C.page(LF, "cream", body + svg_feed_clock(260, 790, 560), F.W, F.H)


def slide3():
    body = F.C.inner(LF, S3, 2, 3).replace("top:120px;height:1060px", "top:70px;height:700px", 1).replace("font-size:150px;", "font-size:150px;white-space:nowrap;", 1)
    return F.C.page(LF, "cream", body + svg_diaper(180, 760, 360) + P.svg_phone(580, 760, 340), F.W, F.H)


PAGES = [cover, slide2, slide3]


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

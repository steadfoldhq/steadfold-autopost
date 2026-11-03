#!/usr/bin/env python3
"""Nov 3 (Social studio, Littlefold maker): 3 am Club No. 6 (Fri Nov 6, 17:00), 2 slides, same layout as No. 5
(nov01_littlefold_feed.py: pills cover on the peach field with the save line and a drawn object bottom right; inner slide
on cream with a drawn object and a source line). Imports oct24_feed and nov01_littlefold_feed; edits nothing.

Topic (gate pick, Nov 3): '3 am bottle? Use the kettle within 30 minutes.' Boiled water, cooled no more than 30 minutes, so it's still at least 70°C.
Facts (checked Nov 3 2026): NHS 'How to make up baby formula'
  (nhs.uk/baby/breastfeeding-and-bottle-feeding/bottle-feeding/making-up-baby-formula/, last reviewed 31 Aug 2023):
  "Leave the water to cool for no more than 30 minutes, so that it remains at a temperature of at least 70C.";
  "Water at 70C or more will kill any harmful bacteria."; sealed powder "can sometimes contain bacteria";
  cool "by holding the bottle (with the lid on) under cold running water"; test "on the inside of your wrist";
  "make up feeds 1 at a time"; leftovers after a feed: "throw it away"; never warm formula in a microwave.

    python3 studio/editorial/nov03_littlefold_feed.py
"""
import re
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import oct24_feed as F  # noqa: E402
import nov01_littlefold_feed as P5  # noqa: E402  (bottle(); nothing renders on import)

LF = F.LF
PID = "lf-3amclub-06"
OUT = F.REPO / "media" / "studio-nov03" / "littlefold" / PID
INKC = P5.INKC


def kettle(x, y, s=1.0, tag=True):
    """A drawn kettle (origin top-left of a ~260 x 240 box) with steam and a berry '70°C+' tag."""
    t = (f'<g transform="translate(150 6) rotate(-6)"><rect x="0" y="0" width="150" height="62" rx="22" fill="#D9497A" stroke="{INKC}" stroke-width="4"/>'
         '<text x="75" y="44" font-family="Poppins" font-weight="700" font-size="36" text-anchor="middle" fill="#FFF8EE">70°C+</text></g>') if tag else ""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            + "".join(f'<path d="M{70 + 30 * i} 60 q-14 -22 0 -44 q14 -22 0 -44" stroke="#FFFFFF" stroke-width="9" fill="none" stroke-linecap="round" opacity=".9"/>' for i in range(2))
            + f'<path d="M30 230 L50 100 Q130 70 210 100 L230 230 Z" fill="#CFE3F6" stroke="{INKC}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M210 120 Q262 130 258 190 Q256 222 228 214" stroke="{INKC}" stroke-width="22" fill="none" stroke-linecap="round"/>'
            f'<path d="M210 120 Q262 130 258 190 Q256 222 228 214" stroke="#FFBFD3" stroke-width="12" fill="none" stroke-linecap="round"/>'
            f'<path d="M50 120 Q10 110 0 80" stroke="{INKC}" stroke-width="22" fill="none" stroke-linecap="round"/><path d="M50 120 Q10 110 0 80" stroke="#CFE3F6" stroke-width="12" fill="none" stroke-linecap="round"/>'
            f'<rect x="96" y="76" width="68" height="20" rx="10" fill="#FFE27E" stroke="{INKC}" stroke-width="4"/>'
            f'<path d="M130 176 c-8 -14 -28 -6 -20 8 l20 18 l20 -18 c8 -14 -12 -22 -20 -8z" fill="#FFBFD3" stroke="{INKC}" stroke-width="3.5"/>'
            + t + '</g>')


def svg_cover_obj(x, y, w=340):
    """Cover: kettle beside a bottle, a berry '70°C+' tag top left, a little moon top right (same slot as No. 5's object)."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;z-index:3;overflow:visible" viewBox="0 0 300 300">'
            '<circle cx="150" cy="150" r="140" fill="#FFF2B8" opacity=".55"/>'
            f'<path d="M262 6 A30 30 0 1 0 290 50 A23 23 0 1 1 262 6Z" fill="#FFE27E" stroke="{INKC}" stroke-width="4"/>'
            + kettle(-20, 74, 0.86, tag=False) + P5.bottle(206, 70, 0.74)
            + f'<g transform="translate(-6 0) rotate(-6)"><rect x="0" y="0" width="150" height="62" rx="22" fill="#D9497A" stroke="{INKC}" stroke-width="4"/>'
            '<text x="75" y="44" font-family="Poppins" font-weight="700" font-size="36" text-anchor="middle" fill="#FFF8EE">70°C+</text></g>'
            '</svg>')


def svg_kettle_clock(x, y, w=600):
    """Slide 2: kettle (no tag) + a clock with a 30-minute wedge + '70°C or hotter ✓'."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.6:.0f}px;z-index:3;overflow:visible" viewBox="0 0 600 360">'
            '<ellipse cx="300" cy="330" rx="290" ry="18" fill="#F6D9C3" opacity=".7"/>'
            + kettle(10, 70, 1.0, tag=False) +
            f'<circle cx="440" cy="170" r="120" fill="#FFF8EE" stroke="{INKC}" stroke-width="6"/>'
            '<path d="M440 170 L440 62 A108 108 0 0 1 440 278 Z" fill="#FFBFD3" opacity=".8"/>'
            f'<path d="M440 170 V78 M440 170 V262" stroke="{INKC}" stroke-width="8" stroke-linecap="round"/><circle cx="440" cy="170" r="9" fill="{INKC}"/>'
            '<text x="540" y="70" font-family="Caveat Brush" font-size="44" fill="#D9497A">30 min</text>'
            '<text x="300" y="356" font-family="Caveat Brush" font-size="46" fill="#D9497A" text-anchor="middle">still 70°C or hotter ✓</text>'
            '</svg>')


def cover():
    c = dict(lay="pills", f="berry", kicker="3 am club · no. 6", text="3 am bottle? / Use water boiled / *in the last 30 minutes.*", obj="shoe",
             at="br", save=F.SAVE_LF)
    body = F.lift_save(F.C.LAYOUTS["pills"](LF, c))
    body = re.sub(r'<img class="obj"[^>]*ht-shoe[^>]*>', "", body)
    assert "ht-shoe" not in body
    return F.C.page(LF, "berry", body + svg_cover_obj(690, 940, 340), F.W, F.H)


S2 = dict(f="cream", text="Boiled water: / *still 70°C or hotter.*",
          sub="hot enough to kill germs in the powder.<br>then cool the bottle under a cold tap.", src="NHS · How to make up baby formula")


def slide2():
    body = F.C.inner(LF, S2, 1, 2).replace("top:120px;height:1060px", "top:70px;height:700px", 1)
    return F.C.page(LF, "cream", body + svg_kettle_clock(240, 800, 600), F.W, F.H)


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

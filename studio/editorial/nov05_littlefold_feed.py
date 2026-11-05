#!/usr/bin/env python3
"""Nov 5 (Social studio, Littlefold maker): 3 am Club No. 8 (Wed Nov 11, 17:00), 2 slides, SAME layout as No. 7
(nov04_littlefold_feed.py: pills cover on the peach field with the save line and a drawn object bottom right; inner slide
on cream with a drawn object and a source line). Imports oct24_feed, nov01_littlefold_feed and nov04_littlefold_feed
(sleeper); edits nothing.

Topic (gate Nov 5: picker's hook): '3 am feed? Newborns need 8-12 a day.' Breastfed newborns feed about 8 to 12 times in 24 hours in the first weeks, so a
3 am feed is part of a normal day. Facts (checked Nov 5 2026):
  CDC 'How Much and How Often to Breastfeed' (cdc.gov/infant-toddler-nutrition/breastfeeding/how-much-and-how-often.html,
    last updated April 16 2026): "Your baby will breastfeed about 8 to 12 times in 24 hours."; "At first, babies need to eat
    every 2 to 4 hours to help them get enough nutrition and to grow."; "You may need to wake your baby to feed.";
    "Continue to follow your baby's cues and breastfeed when you notice signs of hunger."
  CPS caringforkids 'Breastfeeding' (last updated August 2020): "In the first few weeks, babies need to be breastfed 8 to 12
    times over a 24-hour period."; "Let your baby set the pace."; "In the first few days of life, it is not uncommon for babies
    to need to be woken up for a feed."; "If this behavior persists into the second week of life, talk to your doctor."

    python3 studio/editorial/nov05_littlefold_feed.py
"""
import math
import re
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import oct24_feed as F  # noqa: E402
import nov01_littlefold_feed as P5  # noqa: E402  (nothing renders on import)
import nov04_littlefold_feed as P7  # noqa: E402  (nothing renders on import)

LF = F.LF
PID = "lf-3amclub-08"
OUT = F.REPO / "media" / "studio-nov05" / "littlefold" / PID
INKC = P5.INKC
# 10 feeds around a 24-hour day (made up for this post: one spread inside the 8-12 range), as clock hours
FEEDS = [0.5, 3, 5.5, 8, 10.5, 13, 15.5, 18, 20.5, 22.5]


def drop(x, y, s=1.0, fill="#FFB9CF"):
    return (f'<path transform="translate({x:.1f} {y:.1f}) scale({s})" d="M0 -22 Q16 -2 14 8 A14 14 0 1 1 -14 8 Q-16 -2 0 -22Z" '
            f'fill="{fill}" stroke="{INKC}" stroke-width="4" stroke-linejoin="round"/>')


def dayring(x, y, s=1.0, label=True):
    """A 24-hour day ring (midnight at the top): sun side and moon side, 10 milk drops for 10 feeds, the 3 am drop in berry
    with a little moon beside it."""
    R = 120
    out = (f'<g transform="translate({x} {y}) scale({s})">'
           f'<circle r="{R + 26}" fill="#FFF8EE" stroke="{INKC}" stroke-width="6"/>'
           # night half (6 pm -> 6 am, the left/top arc is clock 18..24..6): soft blue wedge; day half butter
           f'<path d="M{-(R + 20)} 0 A{R + 20} {R + 20} 0 0 1 {R + 20} 0 Z" fill="#DCE9F7"/>'
           f'<path d="M{-(R + 20)} 0 A{R + 20} {R + 20} 0 0 0 {R + 20} 0 Z" fill="#FFF2B8"/>'
           f'<circle r="{R + 26}" fill="none" stroke="{INKC}" stroke-width="6"/>')
    for k in range(24):
        a = k / 24 * 2 * math.pi
        r0 = R + 8 if k % 6 else R - 2
        out += f'<path d="M{r0 * math.sin(a):.1f} {-r0 * math.cos(a):.1f} L{(R + 20) * math.sin(a):.1f} {-(R + 20) * math.cos(a):.1f}" stroke="{INKC}" stroke-width="{4 if k % 6 else 6}" stroke-linecap="round"/>'
    for hr in FEEDS:
        a = hr / 24 * 2 * math.pi
        out += drop(0.72 * R * math.sin(a), -0.72 * R * math.cos(a), 0.9, "#D9497A" if hr == 3 else "#FFB9CF")
    a3 = 3 / 24 * 2 * math.pi
    mx, my = (R + 62) * math.sin(a3), -(R + 62) * math.cos(a3)
    out += f'<path transform="translate({mx:.1f} {my:.1f})" d="M-6 -26 A26 26 0 1 0 22 14 A20 20 0 1 1 -6 -26Z" fill="#FFE27E" stroke="{INKC}" stroke-width="4"/>'
    if label:
        out += ('<text y="-6" font-family="Poppins" font-weight="700" font-size="34" text-anchor="middle" fill="#3A1F3D">24</text>'
                '<text y="26" font-family="Poppins" font-weight="600" font-size="22" text-anchor="middle" fill="#3A1F3D">hours</text>')
    return out + '</g>'


def svg_cover_obj(x, y, w=340):
    """Cover: the day ring with 10 drops (3 am drop in berry + moon) and the sleeper below (No. 7 slot)."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;z-index:3;overflow:visible" viewBox="0 0 300 300">'
            '<circle cx="150" cy="150" r="140" fill="#FFF2B8" opacity=".55"/>'
            + dayring(168, 122, 0.66) + P7.sleeper(110, 268, 0.62)
            + '</svg>')


def svg_slide2(x, y, w=600):
    """Slide 2: the sleeper + the day ring, '8 to 12 drops a day ✓'."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.6:.0f}px;z-index:3;overflow:visible" viewBox="0 0 600 360">'
            '<ellipse cx="300" cy="330" rx="290" ry="18" fill="#F6D9C3" opacity=".7"/>'
            + P7.sleeper(160, 290, 1.05) + dayring(440, 160, 0.95) +
            '<text x="300" y="370" font-family="Caveat Brush" font-size="46" fill="#D9497A" text-anchor="middle">night feeds count too ✓</text>'
            '</svg>')


def cover():
    c = dict(lay="pills", f="berry", kicker="3 am club · no. 8", text="3 am feed? / *Newborns need / 8–12 a day.*", obj="shoe",
             at="br", save=F.SAVE_LF)
    body = F.lift_save(F.C.LAYOUTS["pills"](LF, c))
    body = re.sub(r'<img class="obj"[^>]*ht-shoe[^>]*>', "", body)
    assert "ht-shoe" not in body
    return F.C.page(LF, "berry", body + svg_cover_obj(690, 940, 340), F.W, F.H)


S2 = dict(f="cream", text="8 to 12 feeds / *in 24 hours.*",
          sub="that's breastfed newborns,<br>in the first few weeks.<br>follow their hunger cues.<br>baby still needs waking for feeds<br>in week 2? talk to your doctor.",
          src="CDC · Canadian Paediatric Society")


def slide2():
    body = F.C.inner(LF, S2, 1, 2).replace("top:120px;height:1060px", "top:70px;height:700px", 1)
    assert body.count("font-size:150px") == 1 and body.count("font-size:68px;margin-top:46px") == 1
    body = body.replace("font-size:150px", "font-size:132px").replace("font-size:68px;margin-top:46px", "font-size:62px;margin-top:30px")
    body = body.replace("top:70px;height:700px", "top:100px;height:700px", 1)
    return F.C.page(LF, "cream", body + svg_slide2(240, 840, 600), F.W, F.H)


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

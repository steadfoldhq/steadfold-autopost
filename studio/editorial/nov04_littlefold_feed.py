#!/usr/bin/env python3
"""Nov 4 (Social studio, Littlefold maker): 3 am Club No. 7 (Mon Nov 9, 17:00), 2 slides, SAME layout as No. 6
(nov03_littlefold_feed.py: pills cover on the peach field with the save line and a drawn object bottom right; inner slide
on cream with a drawn object and a source line). Imports oct24_feed and nov01_littlefold_feed; edits nothing.

Topic (gate Nov 4: picker's hook): 'Newborn breathing pauses: under 10 seconds is normal.' Newborn pauses under 10 seconds (periodic breathing) are normal if the baby
is comfortable. Facts (checked Nov 4 2026): AAP HealthyChildren.org symptom checker 'Newborn Reflexes and Behavior'
(Barton Schmitt MD, FAAP): "Transient Breathing Pauses of Less Than 10 Seconds. Also Called Periodic Breathing.";
"Often, the pause is followed by some faster breathing to 'catch-up.'"; "These breathing pauses are normal if the baby
is comfortable during them."; "Usually resolves by 1 month of age."; Call 911 Now: "Bluish (or gray) lips, tongue or
face now"; Call Doctor or Seek Care Now: "Breathing stopped for more than 10 seconds and now it's normal".

    python3 studio/editorial/nov04_littlefold_feed.py
"""
import re
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import oct24_feed as F  # noqa: E402
import nov01_littlefold_feed as P5  # noqa: E402  (nothing renders on import)

LF = F.LF
PID = "lf-3amclub-07"
OUT = F.REPO / "media" / "studio-nov04" / "littlefold" / PID
INKC = P5.INKC


def stopwatch(x, y, s=1.0, wedge=1.0):
    """A drawn stopwatch (centre x,y, r 110) with a sage wedge for the first 10 of 60 seconds."""
    import math
    a = 2 * math.pi * (10 / 60) * wedge
    ex, ey = 110 * math.sin(a), -110 * math.cos(a)
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-22" y="-150" width="44" height="34" rx="10" fill="#FFE27E" stroke="{INKC}" stroke-width="5"/>'
            f'<circle cx="0" cy="0" r="124" fill="#FFF8EE" stroke="{INKC}" stroke-width="6"/>'
            f'<path d="M0 0 L0 -110 A110 110 0 0 1 {ex:.1f} {ey:.1f} Z" fill="#BFD8B0" stroke="{INKC}" stroke-width="3"/>'
            + "".join(f'<path d="M{100 * math.sin(k * math.pi / 6):.1f} {-100 * math.cos(k * math.pi / 6):.1f} L{116 * math.sin(k * math.pi / 6):.1f} {-116 * math.cos(k * math.pi / 6):.1f}" stroke="{INKC}" stroke-width="5" stroke-linecap="round"/>' for k in range(12))
            + f'<path d="M0 0 L{ex * 0.9:.1f} {ey * 0.9:.1f}" stroke="{INKC}" stroke-width="8" stroke-linecap="round"/><circle cx="0" cy="0" r="10" fill="{INKC}"/>'
            '</g>')


def sleeper(x, y, s=1.0):
    """A drawn newborn asleep on its back in a pink sleep sack (side view), small 'z's."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-150" y="0" width="300" height="30" rx="12" fill="#FFF8EE" stroke="{INKC}" stroke-width="4"/>'
            f'<path d="M-70 -2 Q-78 -58 -20 -62 L80 -58 Q118 -52 114 -2 Z" fill="#FFB9CF" stroke="{INKC}" stroke-width="5" stroke-linejoin="round"/>'
            f'<circle cx="-112" cy="-38" r="40" fill="#FFDCC4" stroke="{INKC}" stroke-width="5"/>'
            f'<path d="M-126 -44 q7 6 14 0" stroke="#5A2E22" stroke-width="4.5" fill="none" stroke-linecap="round"/>'
            '<circle cx="-96" cy="-28" r="7" fill="#FF9EA8" opacity=".6"/>'
            '<text x="-70" y="-90" font-family="Caveat Brush" font-size="34" fill="#B23A62">z</text>'
            '<text x="-44" y="-118" font-family="Caveat Brush" font-size="44" fill="#B23A62">z</text>'
            '</g>')


def svg_cover_obj(x, y, w=340):
    """Cover: sleeping newborn + stopwatch with the 10-second wedge, a berry 'under 10 sec' tag, a little moon (No. 6 slot)."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;z-index:3;overflow:visible" viewBox="0 0 300 300">'
            '<circle cx="150" cy="150" r="140" fill="#FFF2B8" opacity=".55"/>'
            f'<path d="M262 6 A30 30 0 1 0 290 50 A23 23 0 1 1 262 6Z" fill="#FFE27E" stroke="{INKC}" stroke-width="4"/>'
            + stopwatch(200, 150, 0.62) + sleeper(110, 262, 0.72)
            + '</svg>')  # gate round 2: the 'if comfortable' tag was cryptic out of context; dropped


def svg_slide2(x, y, w=600):
    """Slide 2: sleeping newborn + stopwatch wedge + 'under 10 seconds ✓'."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.6:.0f}px;z-index:3;overflow:visible" viewBox="0 0 600 360">'
            '<ellipse cx="300" cy="330" rx="290" ry="18" fill="#F6D9C3" opacity=".7"/>'
            + sleeper(170, 290, 1.05) + stopwatch(450, 170, 1.0) +
            '<text x="300" y="356" font-family="Caveat Brush" font-size="46" fill="#D9497A" text-anchor="middle">under 10 seconds ✓</text>'
            '</svg>')


def cover():
    c = dict(lay="pills", f="berry", kicker="3 am club · no. 7", text="Newborn breathing / pauses under / *10 seconds are normal.*", obj="shoe",
             at="br", save=F.SAVE_LF)
    body = F.lift_save(F.C.LAYOUTS["pills"](LF, c))
    body = re.sub(r'<img class="obj"[^>]*ht-shoe[^>]*>', "", body)
    assert "ht-shoe" not in body
    return F.C.page(LF, "berry", body + svg_cover_obj(690, 940, 340), F.W, F.H)


S2 = dict(f="cream", text="Pauses under / 10 seconds / *are normal.*",
          sub="your baby should look comfortable.<br>longer than 10 seconds?<br>call your doctor now.<br>not breathing, or blue or grey lips?<br>call 911.",
          src="AAP · HealthyChildren.org · NHS 111 Wales")


def slide2():
    body = F.C.inner(LF, S2, 1, 2).replace("top:120px;height:1060px", "top:70px;height:700px", 1)
    # gate round 2: the 5-line safety block pushed the headline into the '2/2' mark; headline 150 -> 124 px, notes 68 -> 62 px
    assert body.count("font-size:150px") == 1 and body.count("font-size:68px;margin-top:46px") == 1
    body = body.replace("font-size:150px", "font-size:124px").replace("font-size:68px;margin-top:46px", "font-size:62px;margin-top:30px")
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

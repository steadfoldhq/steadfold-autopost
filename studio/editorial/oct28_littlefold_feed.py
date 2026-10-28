#!/usr/bin/env python3
"""Oct 28 (Social studio, Littlefold maker): 3 am Club No. 4 (Mon Nov 2, 17:00), 3 slides, same layout as No. 3
(oct26_littlefold_feed.py: pills cover on the peach field, 'new night tip every Mon · Wed · Fri', a drawn object bottom right
in place of the halftone shoe; inner slides on cream with a drawn object and a source line). Imports oct24_feed; edits nothing.

Topic: 'It's 3 am. Baby feels hot.' Under 3 months with 38°C (100.4°F) or more: call the doctor right away.
Facts (checked Oct 28 2026): NHS 'High temperature (fever) in children' (nhs.uk/symptoms/fever-in-children/, reviewed 3 Jan 2024);
AAP HealthyChildren.org 'Fever and Your Baby' (updated 9/23/2025).

    python3 studio/editorial/oct28_littlefold_feed.py
"""
import re
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import oct24_feed as F  # noqa: E402

LF = F.LF
PID = "lf-3amclub-04"
OUT = F.REPO / "media" / "studio-oct28" / "littlefold" / PID
INKC = "#3A1F3D"


def svg_thermo(x, y, w=330, reading="38.0°C", glow=True):
    """Friendly digital thermometer (Littlefold, drawn): rounded body, display with a reading, a little heart button,
    two small stars and a soft glow. No face."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;z-index:3;overflow:visible" viewBox="0 0 300 300">'
            + ('<circle cx="150" cy="150" r="140" fill="#FFF2B8" opacity=".55"/>' if glow else '')
            + '<g transform="rotate(-32 150 150)">'
            f'<rect x="40" y="112" width="200" height="76" rx="38" fill="#FFF8EE" stroke="{INKC}" stroke-width="6"/>'
            f'<path d="M236 136 L286 144 Q296 150 286 156 L236 164 Z" fill="#CFE3F6" stroke="{INKC}" stroke-width="6" stroke-linejoin="round"/>'
            f'<rect x="62" y="126" width="118" height="48" rx="12" fill="#FFE27E" stroke="{INKC}" stroke-width="5"/>'
            f'<text x="121" y="161" font-family="Poppins" font-weight="700" font-size="27" text-anchor="middle" fill="{INKC}">{reading}</text>'
            f'<path d="M206 146 c-5 -9 -18 -4 -13 5 l13 11 l13 -11 c5 -9 -8 -14 -13 -5z" fill="#FFBFD3" stroke="{INKC}" stroke-width="3.5"/>'
            '</g>'
            f'<path d="M58 60 l7 16 l17 2 l-13 11 l4 17 l-15 -9 l-15 9 l4 -17 l-13 -11 l17 -2z" fill="#FFF8EE" stroke="{INKC}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M250 236 l5 11 l12 1 l-9 8 l3 12 l-11 -6 l-11 6 l3 -12 l-9 -8 l12 -1z" fill="#FFF8EE" stroke="{INKC}" stroke-width="3.5" stroke-linejoin="round"/>'
            '</svg>')


def svg_phone(x, y, w=300):
    """A ringing phone with a heart on the screen (calling the doctor), drawn, warm."""
    rings = "".join(f'<path d="M{60 - 16 * i} {100 - 10 * i} q-{18 + 6 * i} 50 0 {100 + 20 * i}" stroke="#D9497A" stroke-width="6" fill="none" stroke-linecap="round"/>'
                    f'<path d="M{240 + 16 * i} {100 - 10 * i} q{18 + 6 * i} 50 0 {100 + 20 * i}" stroke="#D9497A" stroke-width="6" fill="none" stroke-linecap="round"/>' for i in (1, 2))
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;z-index:3;overflow:visible" viewBox="0 0 300 300">'
            '<circle cx="150" cy="150" r="140" fill="#FFF2B8" opacity=".55"/>' + rings +
            f'<rect x="90" y="40" width="120" height="220" rx="24" fill="{INKC}"/><rect x="102" y="58" width="96" height="176" rx="14" fill="#FFF8EE"/>'
            f'<circle cx="150" cy="130" r="30" fill="#BFD8B0" stroke="{INKC}" stroke-width="4"/>'
            f'<path d="M138 118 q-4 14 8 24 q12 10 22 4" stroke="{INKC}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<path d="M150 196 c-6 -11 -22 -5 -16 6 l16 14 l16 -14 c6 -11 -10 -17 -16 -6z" fill="#FFBFD3" stroke="{INKC}" stroke-width="3.5"/></svg>')


def svg_feed(x, y, w=520):
    """Slide 3: a bottle and a cosy sleep sack on a hanger (keep feeding, keep them dressed), drawn."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.62:.0f}px;z-index:3;overflow:visible" viewBox="0 0 520 322">'
            '<ellipse cx="260" cy="300" rx="250" ry="18" fill="#F6D9C3" opacity=".7"/>'
            # bottle
            f'<path d="M110 40 Q130 -6 150 40 Z" fill="#FFE27E" stroke="{INKC}" stroke-width="5" stroke-linejoin="round"/>'
            f'<rect x="92" y="38" width="76" height="30" rx="8" fill="#FFBFD3" stroke="{INKC}" stroke-width="5"/>'
            f'<rect x="84" y="66" width="92" height="224" rx="28" fill="#E3EEF8" stroke="{INKC}" stroke-width="5"/>'
            '<rect x="89" y="150" width="82" height="136" rx="24" fill="#FFFDF6"/>'
            f'<rect x="84" y="66" width="92" height="224" rx="28" fill="none" stroke="{INKC}" stroke-width="5"/>'
            + "".join(f'<path d="M84 {120 + 34 * i} h22" stroke="{INKC}" stroke-width="4"/>' for i in range(4)) +
            # baby, dressed in a footed onesie, sitting up, smiling (face drawn), with a 'keep it on' tick
            f'<ellipse cx="390" cy="292" rx="110" ry="16" fill="#F6D9C3"/>'
            f'<path d="M318 286 Q300 230 318 170 Q340 130 390 128 Q440 130 462 170 Q480 230 462 286 Z" fill="#FFBFD3" stroke="{INKC}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M326 290 Q318 262 346 256 Q380 262 372 292 Z M408 292 Q400 262 434 256 Q462 262 454 290 Z" fill="#FFBFD3" stroke="{INKC}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M322 180 Q290 214 304 250" stroke="{INKC}" stroke-width="30" fill="none" stroke-linecap="round"/><path d="M322 180 Q290 214 304 250" stroke="#FFBFD3" stroke-width="21" fill="none" stroke-linecap="round"/>'
            f'<path d="M458 180 Q490 214 476 250" stroke="{INKC}" stroke-width="30" fill="none" stroke-linecap="round"/><path d="M458 180 Q490 214 476 250" stroke="#FFBFD3" stroke-width="21" fill="none" stroke-linecap="round"/>'
            f'<circle cx="304" cy="256" r="13" fill="#FFDCC4" stroke="{INKC}" stroke-width="4"/><circle cx="476" cy="256" r="13" fill="#FFDCC4" stroke="{INKC}" stroke-width="4"/>'
            f'<path d="M390 196 c-8 -14 -28 -6 -20 8 l20 18 l20 -18 c8 -14 -12 -22 -20 -8z" fill="#FFF8EE" stroke="{INKC}" stroke-width="3.5"/>'
            f'<circle cx="390" cy="86" r="56" fill="#FFDCC4" stroke="{INKC}" stroke-width="5"/>'
            f'<path d="M366 82 q8 8 16 0 M398 82 q8 8 16 0" stroke="{INKC}" stroke-width="4.5" fill="none" stroke-linecap="round"/>'
            f'<path d="M378 104 q12 10 24 0" stroke="#9A4E2A" stroke-width="4.5" fill="none" stroke-linecap="round"/>'
            '<circle cx="356" cy="102" r="9" fill="#FF9EA8" opacity=".7"/><circle cx="424" cy="102" r="9" fill="#FF9EA8" opacity=".7"/>'
            f'<path d="M376 34 q14 -16 28 -2" stroke="#A0674A" stroke-width="4.5" fill="none" stroke-linecap="round"/>'
            '<text x="452" y="26" font-family="Caveat Brush" font-size="50" fill="#D9497A" transform="rotate(-6 452 26)">keep it on ✓</text>'
            '</svg>')


def cover():
    c = dict(lay="pills", f="berry", kicker="3 am club · no. 4", text="It's 3 am. / Baby feels / *hot.*", obj="shoe",
             at="br", save=F.SAVE_LF)
    body = F.lift_save(F.C.LAYOUTS["pills"](LF, c))
    body = re.sub(r'<img class="obj"[^>]*ht-shoe[^>]*>', "", body)
    assert "ht-shoe" not in body
    return F.C.page(LF, "berry", body + svg_thermo(690, 940, 340), F.W, F.H)


S2 = dict(f="cream", text="Under 3 months / and 38°C or more? / *Call the doctor now.*", sub="38°C is 100.4°F · even if they seem fine",
          src="NHS · AAP HealthyChildren.org")
S3 = dict(f="cream", text="While you call: / *keep feeding.*", sub="don't undress or sponge them down",
          src="NHS · High temperature in children")


def slide2():
    body = F.C.inner(LF, S2, 1, 3).replace("top:120px;height:1060px", "top:70px;height:700px", 1).replace("font-size:150px;", "font-size:150px;white-space:nowrap;", 1)
    return F.C.page(LF, "cream", body + svg_thermo(150, 740, 400, glow=False) + svg_phone(600, 740, 360), F.W, F.H)


def slide3():
    body = F.C.inner(LF, S3, 2, 3).replace("top:120px;height:1060px", "top:70px;height:640px", 1)
    return F.C.page(LF, "cream", body + svg_feed(280, 780, 560), F.W, F.H)


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

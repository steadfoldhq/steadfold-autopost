#!/usr/bin/env python3
"""Nov 4 studio build: Rich Habits, Decoded No. 7 (ff-richhabits-07), Mon Nov 9 17:00 (promised in No. 6's caption).
Same series layout as No. 6 (pills cover on the coral field + series badge + handwritten series line + round stamp + a drawn card
bottom-right; slide 2 from covers.inner() on the lite field + a drawn card), imported from nov01_fullyfunded_feed.py (not edited).
Habit No. 7: starting a free trial -> set a phone reminder 2 days before it ends, then keep it or cancel.
Competition Bureau Canada 'Subscription traps' (modified 2022-01-19): some free trials turn into monthly charges; read the terms,
check your card statements for frequent or unknown charges.

    python3 studio/editorial/nov04_fullyfunded_feed.py
Writes media/studio-nov04/fullyfunded/ff-richhabits-07/0N.jpg.
"""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import nov01_fullyfunded_feed as F  # noqa: E402  (No. 5/6: series layout via oct28/oct25)
import edkit as K  # noqa: E402
# CD gate (Nov 4): the lavender pill (p1 #C9D3F7 / #CBD4F7) reads as Hourback periwinkle. In-process only (kit not edited):
# white pill on the coral field, soft coral #FFB08F on the lite field.
K.FIELDS["fullyfunded"]["coral"] = dict(K.FIELDS["fullyfunded"]["coral"], p1="#FFFFFF")
K.FIELDS["fullyfunded"]["lite"] = dict(K.FIELDS["fullyfunded"]["lite"], p1="#FFB08F")

Q, P, C = F.Q, F.P, F.C
FF, W, H, COB, CORAL, INK = P.FF, P.W, P.H, P.COB, P.CORAL, F.INK
GREEN = "#1F8A5B"
OUT = REPO / "media/studio-nov04/fullyfunded/ff-richhabits-07"

TRIAL, REMIND = 30, 28
assert TRIAL - REMIND == 2

COVER = dict(lay="pills", f="coral", kicker="rich habits, decoded · no. 7", text="Free 30-day trial? / *Set a day-28 / reminder.*",
             obj="ok", at="br", save=P.SAVE)
S2 = dict(f="lite", text="Still using it? / Keep it. / *If not, cancel.*", sub="check your bill for the charge")


def trial(x0=540, y0=845, w=470, h=440):
    """Drawn sign-up card: FREE TRIAL header, '30 DAYS FREE', 'THEN BILLED MONTHLY' in small mono, and a REMIND ME DAY 28 stamp."""
    return "".join([
        f'<svg style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="0 0 {w} {h}">',
        f'<rect x="14" y="34" width="{w - 12}" height="{h - 30}" rx="22" fill="{INK}"/>',
        f'<rect x="6" y="20" width="{w - 12}" height="{h - 30}" rx="22" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>',
        f'<rect x="6" y="20" width="{w - 12}" height="64" rx="22" fill="{COB}" stroke="{INK}" stroke-width="5"/>',
        f'<rect x="9" y="58" width="{w - 18}" height="26" fill="{COB}"/>',
        f'<text x="{w / 2}" y="64" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="#FFFFFF">START FREE TRIAL</text>',
        f'<text x="{w / 2}" y="200" text-anchor="middle" font-family="Inter Display, Inter" font-weight="800" font-size="96" fill="{CORAL}">30 DAYS</text>',
        f'<text x="{w / 2}" y="250" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="{INK}">FREE, THEN BILLED MONTHLY</text>',
        f'<line x1="40" y1="290" x2="{w - 40}" y2="290" stroke="{INK}" stroke-opacity=".2" stroke-width="3" stroke-dasharray="10 8"/>',
        f'<rect x="40" y="320" width="{w - 80}" height="74" rx="37" fill="{INK}"/>',
        f'<text x="{w / 2}" y="368" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="28" fill="#FFFFFF">ADD CARD</text>',
        f'<g transform="rotate(-8 {w / 2} 360)"><rect x="{w / 2 - 150}" y="305" width="300" height="114" rx="16" fill="#FFFFFF" '
        f'stroke="{CORAL}" stroke-width="8"/>'
        f'<text x="{w / 2}" y="340" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="24" fill="{CORAL}">'
        f'REMIND ME ON</text>'
        f'<text x="{w / 2}" y="398" text-anchor="middle" font-family="Inter Display, Inter" font-weight="800" font-size="60" fill="{CORAL}">'
        f'DAY 28</text></g>',
        "</svg>"])


def reminder(x, y, w=560):
    """Drawn phone reminder for slide 2: DAY 28 · TRIAL ENDS IN 2 DAYS / 'Still using it?' with KEEP IT and CANCEL."""
    h = 300
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="0 0 {w} {h}">'
            f'<rect x="12" y="14" width="{w - 8}" height="{h - 10}" rx="34" fill="{INK}"/>'
            f'<rect x="4" y="4" width="{w - 8}" height="{h - 10}" rx="34" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
            f'<circle cx="60" cy="66" r="26" fill="{COB}"/><path d="M60,50 v18 l12,8" stroke="#FFFFFF" stroke-width="6" fill="none" stroke-linecap="round"/>'
            f'<text x="104" y="76" font-family="DejaVu Sans Mono" font-weight="700" font-size="25" fill="{INK}">DAY 28 · ENDS IN 2 DAYS</text>'
            f'<text x="40" y="160" font-family="Inter Display, Inter" font-weight="800" font-size="58" fill="{INK}">Still using it?</text>'
            f'<rect x="40" y="198" width="220" height="62" rx="31" fill="{COB}"/>'
            f'<text x="150" y="240" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="#FFFFFF">YES · KEEP</text>'
            f'<rect x="282" y="198" width="230" height="62" rx="31" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/>'
            f'<text x="397" y="240" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="{INK}">NO · CANCEL</text>'
            '</svg>')


def cover():
    body = C.lay_pills(FF, COVER)
    body = P.lift_save(re.sub(r'<img class="obj"[^>]*>', "", body, count=1))   # drawn trial card replaces the halftone object
    body = body.replace("width:620px;font-size:66px", "width:470px;font-size:62px", 1)
    return C.page(FF, "coral", body + trial(), W, H)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = C.R()
    try:
        files = [r.shot(cover(), W, H, OUT / "01.jpg"),
                 r.shot(C.page(FF, S2["f"], C.inner(FF, S2, 1, 2) + reminder(260, 1000, 560), W, H), W, H, OUT / "02.jpg")]
    finally:
        r.close()
    print(files)


if __name__ == "__main__":
    main()

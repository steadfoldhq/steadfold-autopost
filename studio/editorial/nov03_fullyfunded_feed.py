#!/usr/bin/env python3
"""Nov 3 studio build: Rich Habits, Decoded No. 6 (ff-richhabits-06), Fri Nov 6 17:00 (promised in No. 5's caption).
Same series layout as No. 5 (pills cover on the coral field + series badge + handwritten series line + round stamp + a small drawn
object bottom-right; slide 2 from covers.inner()), imported from nov01_fullyfunded_feed.py / oct28 / oct25 (not edited).
Desk order (Nov 3): 2 slides, minimal hours, the number visible on the cover, cover hook <= 8 words naming a moment in the viewer's
own words. Habit No. 6: a checkout countdown ("Sale ends in 10 minutes") -> wait 24 hours, then decide. Competition Bureau Canada
(Nov 25 2024): fake urgency, "The timer runs out or resets but the offer is still available."

    python3 studio/editorial/nov03_fullyfunded_feed.py
Writes media/studio-nov03/fullyfunded/ff-richhabits-06/0N.jpg.
"""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import nov01_fullyfunded_feed as F  # noqa: E402  (No. 5: series layout via oct28/oct25)

Q, P, C = F.Q, F.P, F.C
FF, W, H, COB, CORAL, INK = P.FF, P.W, P.H, P.COB, P.CORAL, F.INK
OUT = REPO / "media/studio-nov03/fullyfunded/ff-richhabits-06"

COVER = dict(lay="pills", f="coral", kicker="rich habits, decoded · no. 6", text="Only 2 left? / *Sleep on it / 24 hours.*",
             obj="ok", at="br", save=P.SAVE)
S2 = dict(f="lite", text="Still want it / tomorrow? / *Then buy it.*", sub="‘only 2 left’ is sometimes a sales trick")


def checkout(x0=540, y0=845, w=470, h=440):
    """Drawn checkout card: CHECKOUT header, 'HURRY! ONLY 2 LEFT' in coral, a cart line, and a WAIT 24 H stamp across it."""
    o = [f'<svg style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="0 0 {w} {h}">',
         f'<rect x="14" y="34" width="{w - 12}" height="{h - 30}" rx="22" fill="{INK}"/>',
         f'<rect x="6" y="20" width="{w - 12}" height="{h - 30}" rx="22" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>',
         f'<rect x="6" y="20" width="{w - 12}" height="64" rx="22" fill="{COB}" stroke="{INK}" stroke-width="5"/>',
         f'<rect x="9" y="58" width="{w - 18}" height="26" fill="{COB}"/>',
         f'<text x="{w / 2}" y="64" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="#FFFFFF">CHECKOUT</text>',
         f'<text x="{w / 2}" y="140" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="{INK}">HURRY! ONLY</text>',
         f'<text x="{w / 2}" y="240" text-anchor="middle" font-family="Inter Display, Inter" font-weight="800" font-size="104" fill="{CORAL}">2 LEFT</text>',
         f'<line x1="40" y1="290" x2="{w - 40}" y2="290" stroke="{INK}" stroke-opacity=".2" stroke-width="3" stroke-dasharray="10 8"/>',
         f'<rect x="40" y="320" width="{w - 80}" height="74" rx="37" fill="{INK}"/>',
         f'<text x="{w / 2}" y="368" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="28" fill="#FFFFFF">BUY NOW</text>',
         # the habit: a coral rubber stamp across the card
         f'<g transform="rotate(-8 {w / 2} 360)"><rect x="{w / 2 - 160}" y="305" width="320" height="110" rx="16" fill="#FFFFFF" '
         f'stroke="{CORAL}" stroke-width="8"/>'
         f'<text x="{w / 2}" y="383" text-anchor="middle" font-family="Inter Display, Inter" font-weight="800" font-size="62" fill="{CORAL}">'
         f'WAIT 24 H</text></g>',
         "</svg>"]
    return "".join(o)


def reminder(x, y, w=520):
    """Drawn phone reminder card for slide 2: TOMORROW, 9:00 PM / 'Still want it?' with YES · BUY and NO · SKIP."""
    h = 300
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="0 0 {w} {h}">'
            f'<rect x="12" y="14" width="{w - 8}" height="{h - 10}" rx="34" fill="{INK}"/>'
            f'<rect x="4" y="4" width="{w - 8}" height="{h - 10}" rx="34" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
            f'<circle cx="60" cy="66" r="26" fill="{COB}"/><path d="M60,50 v18 l12,8" stroke="#FFFFFF" stroke-width="6" fill="none" stroke-linecap="round"/>'
            f'<text x="104" y="76" font-family="DejaVu Sans Mono" font-weight="700" font-size="28" fill="{INK}">REMINDER · TOMORROW</text>'
            f'<text x="40" y="160" font-family="Inter Display, Inter" font-weight="800" font-size="58" fill="{INK}">Still want it?</text>'
            f'<rect x="40" y="198" width="200" height="62" rx="31" fill="{COB}"/>'
            f'<text x="140" y="240" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="#FFFFFF">YES · BUY</text>'
            f'<rect x="262" y="198" width="210" height="62" rx="31" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/>'
            f'<text x="367" y="240" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="{INK}">NO · SKIP</text>'
            '</svg>')


def cover():
    body = C.lay_pills(FF, COVER)
    body = P.lift_save(re.sub(r'<img class="obj"[^>]*>', "", body, count=1))   # drawn checkout card replaces the halftone object
    body = body.replace("width:620px;font-size:66px", "width:470px;font-size:62px", 1)
    return C.page(FF, "coral", body + checkout(), W, H)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = C.R()
    try:
        files = [r.shot(cover(), W, H, OUT / "01.jpg"),
                 r.shot(C.page(FF, S2["f"], C.inner(FF, S2, 1, 2) + reminder(280, 1000, 520), W, H), W, H, OUT / "02.jpg")]
    finally:
        r.close()
    print(files)


if __name__ == "__main__":
    main()

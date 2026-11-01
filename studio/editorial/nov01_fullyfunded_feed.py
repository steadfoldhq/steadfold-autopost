#!/usr/bin/env python3
"""Nov 1 studio build: Rich Habits, Decoded No. 5 (ff-richhabits-05), Wed Nov 4 17:00 (promised in No. 4's caption).
Same series layout as No. 1-4 (pills cover on the coral field + series badge + handwritten series line + round stamp + a small drawn
object; slides 2-3 from covers.inner()), imported from oct25_fullyfunded_feed.py / oct28_fullyfunded_feed.py (not edited).
Habit No. 5: a 20-minute money date once a month (alone or with your partner), with a 3-question agenda. No numbers, no returns.

    python3 studio/editorial/nov01_fullyfunded_feed.py
Writes media/studio-nov01/fullyfunded/ff-richhabits-05/0N.jpg.
"""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import oct28_fullyfunded_feed as Q  # noqa: E402  (No. 4: imports the series layout + pill fix; no_hand)
import edkit as K  # noqa: E402
K.FIELDS["fullyfunded"].setdefault("cobt", dict(K.FIELDS["fullyfunded"]["cob"], bg="#A9B4F4"))   # in-process cobalt tint for slide 3 (kit not edited)

P, C = Q.P, Q.C
FF, W, H, COB, CORAL, INK = P.FF, P.W, P.H, P.COB, P.CORAL, Q.INK
OUT = REPO / "media/studio-nov01/fullyfunded/ff-richhabits-05"

COVER = dict(lay="pills", f="coral", kicker="rich habits, decoded · no. 5", text="Money talk only / *in a fight?*", obj="ok", at="br",
             save=P.SAVE)
S2 = dict(f="lite", text="Book a monthly / *money date.*", sub="20 minutes · alone or together")
S3 = dict(f="cobt", text="The 20-minute / *agenda*",
          items=["What came in this month?", "What went out?", "What’s the next big bill?"],
          sub="then pick one thing to change next month")


def date_card(x0=540, y0=900, w=470, h=380):
    """Drawn calendar card: EVERY MONTH, the first Sunday circled, MONEY DATE · 20 MIN."""
    days = "MTWTFSS"
    cw = (w - 40) / 7
    o = [f'<svg style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="0 0 {w} {h}">',
         f'<rect x="6" y="40" width="{w - 12}" height="{h - 60}" rx="22" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>',
         f'<rect x="6" y="40" width="{w - 12}" height="66" rx="22" fill="{COB}" stroke="{INK}" stroke-width="5"/>',
         f'<rect x="9" y="80" width="{w - 18}" height="26" fill="{COB}"/>',
         f'<text x="{w / 2}" y="84" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="#FFFFFF">EVERY MONTH</text>']
    for d in range(7):
        cx = 20 + d * cw + cw / 2
        o.append(f'<text x="{cx:.0f}" y="180" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="30" fill="{INK}">{d + 1}</text>')
    c7 = 20 + 6 * cw + cw / 2
    o.append(f'<ellipse cx="{c7:.0f}" cy="170" rx="30" ry="28" fill="none" stroke="{CORAL}" stroke-width="6"/>')
    o.append(f'<path d="M{c7:.0f},204 L{c7 - 40:.0f},252" stroke="{CORAL}" stroke-width="6" stroke-linecap="round"/>')
    o.append(f'<text x="{w - 30}" y="292" text-anchor="end" font-family="DejaVu Sans Mono" font-weight="700" font-size="28" fill="{CORAL}">MONEY DATE · 20 MIN</text>')
    o.append(f'<text x="{w - 30}" y="336" text-anchor="end" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="{INK}">SAME DAY EVERY MONTH</text>')
    o.append("</svg>")
    return "".join(o)


def timer(x, y, w=300):
    """Drawn kitchen timer set to 20:00 (slide 2 object)."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;z-index:3;overflow:visible" viewBox="0 0 300 300">'
            f'<rect x="132" y="8" width="36" height="34" rx="8" fill="{INK}"/>'
            f'<circle cx="160" cy="170" r="128" fill="{INK}"/>'
            f'<circle cx="150" cy="160" r="128" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>'
            f'<path d="M150,160 L150,32 A128,128 0 0 1 260.9,224 Z" fill="#FFD9CB"/>'
            f'<circle cx="150" cy="160" r="128" fill="none" stroke="{INK}" stroke-width="7"/>'
            f'<text x="150" y="182" text-anchor="middle" font-family="Inter Display, Inter" font-weight="800" font-size="70" fill="{INK}">20:00</text>'
            '</svg>')


def two_mugs(x, y, w=280):
    """Drawn: two mugs side by side (slide 3 object, replaces the retired pointing hand)."""
    def mug(mx, col):
        return (f'<rect x="{mx + 8}" y="58" width="100" height="120" rx="16" fill="{INK}"/>'
                f'<rect x="{mx}" y="50" width="100" height="120" rx="16" fill="{col}" stroke="{INK}" stroke-width="6"/>'
                f'<path d="M{mx + 100},80 c34,0 34,56 0,56" fill="none" stroke="{INK}" stroke-width="8"/>'
                f'<path d="M{mx + 30},38 c-10,-14 10,-20 0,-34 M{mx + 62},38 c-10,-14 10,-20 0,-34" fill="none" stroke="{INK}" stroke-width="5" '
                f'stroke-linecap="round" opacity=".5"/>')
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.7:.0f}px;z-index:3;overflow:visible" viewBox="0 0 280 196">'
            + mug(10, "#FFFFFF") + mug(150, CORAL) + "</svg>")


def cover():
    body = C.lay_pills(FF, COVER)
    body = P.lift_save(re.sub(r'<img class="obj"[^>]*>', "", body, count=1))   # drawn calendar card replaces the halftone object
    body = body.replace("width:620px;font-size:66px", "width:470px;font-size:62px", 1)
    return C.page(FF, "coral", body + date_card(), W, H)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = C.R()
    try:
        s3 = Q.no_hand(C.inner(FF, S3, 2, 3))
        s3 = s3.replace("left:300px;top:1010px;width:700px;font-size:76px", "left:250px;top:1030px;width:580px;font-size:66px", 1)   # clear the stamp
        files = [r.shot(cover(), W, H, OUT / "01.jpg"),
                 r.shot(C.page(FF, S2["f"], C.inner(FF, S2, 1, 3) + timer(390, 980, 300), W, H), W, H, OUT / "02.jpg"),
                 r.shot(C.page(FF, S3["f"], s3 + two_mugs(40, 1080, 280), W, H), W, H, OUT / "03.jpg")]
    finally:
        r.close()
    print(files)


if __name__ == "__main__":
    main()

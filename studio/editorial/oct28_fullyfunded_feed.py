#!/usr/bin/env python3
"""Oct 28 studio build: Rich Habits, Decoded No. 4 (ff-richhabits-04), Mon Nov 2 17:00.
Same series layout as No. 1-3 (pills cover on the coral field + series badge + handwritten series line + round stamp + a small
drawn object in place of the halftone cut-out; slides 2-3 from covers.inner()), imported from oct25_fullyfunded_feed.py (not edited).
Habit No. 4: live one month ahead (keep one month of bills in the bank, so this month's bills are paid with last month's pay).

    python3 studio/editorial/oct28_fullyfunded_feed.py
Writes media/studio-oct28/fullyfunded/ff-richhabits-04/0N.jpg. Amounts are made up for this post and labelled so on slide 3.
"""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import oct25_fullyfunded_feed as P  # noqa: E402  (series layout, pill fix, lift_save)

C = P.C
FF, W, H, COB, CORAL = P.FF, P.W, P.H, P.COB, P.CORAL
INK = "#141A55"
OUT = REPO / "media/studio-oct28/fullyfunded/ff-richhabits-04"

# ---------------------------------------------------------------- MATHS (made up for this post; stated on slide 3 and in the caption)
BILLS = 2000          # one month of bills
SAVE = 200            # set aside each month
MONTHS = BILLS // SAVE
assert MONTHS == 10 and SAVE * MONTHS == BILLS

COVER = dict(lay="pills", f="coral", kicker="rich habits, decoded · no. 4", text="Rent due / *before payday?*", obj="ok", at="br",
             save=P.SAVE)
S2 = dict(f="lite", text="Keep one month / of bills / *in the bank.*",
          sub="pay this month with last month’s pay")
S3 = dict(f="cob", text="One month ahead, / *in numbers*", cap="made up for this post · use your own bills",
          rows=[(f"Bills a month", f"${BILLS:,}"), ("Set aside each month", f"${SAVE}"), ("Months to get there", f"{MONTHS}")],
          sub="next month’s $2,000 of bills: already saved")


def gap_strip(x0=540, y0=900, w=470, h=380):
    """Drawn month strip: RENT DUE on the 1st lands BEFORE PAYDAY on the 5th (the gap the habit closes)."""
    days = 7
    cw = (w - 40) / days
    out = [f'<svg style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="0 0 {w} {h}">',
           f'<rect x="6" y="40" width="{w - 12}" height="{h - 60}" rx="22" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>',
           f'<rect x="6" y="40" width="{w - 12}" height="66" rx="22" fill="{COB}" stroke="{INK}" stroke-width="5"/>',
           f'<rect x="9" y="80" width="{w - 18}" height="26" fill="{COB}"/>',
           f'<text x="{w / 2}" y="84" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="#FFFFFF">THIS MONTH</text>']
    for d in range(days):
        cx = 20 + d * cw
        hot = d == 0
        pay = d == 4
        fill = "#FFE3D6" if hot else ("#DDE3FF" if pay else "#FFFFFF")
        out.append(f'<rect x="{cx + 4:.0f}" y="130" width="{cw - 8:.0f}" height="78" rx="10" fill="{fill}" stroke="{INK}" stroke-width="3"/>')
        out.append(f'<text x="{cx + cw / 2:.0f}" y="182" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="30" '
                   f'fill="{INK}">{d + 1}</text>')
    c1 = 20 + cw / 2
    c5 = 20 + 4 * cw + cw / 2
    out.append(f'<path d="M{c1:.0f},222 L{c1:.0f},262" stroke="{CORAL}" stroke-width="6" stroke-linecap="round"/>')
    out.append(f'<text x="{c1 - 18:.0f}" y="300" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="{CORAL}">RENT DUE</text>')
    out.append(f'<path d="M{c5:.0f},222 L{c5:.0f},262" stroke="{COB}" stroke-width="6" stroke-linecap="round"/>')
    out.append(f'<text x="{c5 + 30:.0f}" y="300" text-anchor="end" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="{COB}">PAYDAY</text>')
    out.append("</svg>")
    return "".join(out)


def two_months(x, y, w=520):
    """Drawn: LAST MONTH'S PAY envelope sliding into THIS MONTH'S BILLS (slide 2 object)."""
    h = w * 0.5
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h:.0f}px;z-index:3;overflow:visible" viewBox="0 0 520 260">'
            '<rect x="10" y="40" width="230" height="160" rx="16" fill="#FFFFFF" stroke="#141A55" stroke-width="6"/>'
            '<path d="M10 52 L125 130 L240 52" fill="none" stroke="#141A55" stroke-width="6" stroke-linejoin="round"/>'
            f'<text x="125" y="232" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="22" fill="{COB}">LAST MONTH’S PAY</text>'
            f'<path d="M262 120 L330 120" stroke="{CORAL}" stroke-width="10" stroke-linecap="round"/>'
            f'<path d="M314 98 L340 120 L314 142" fill="none" stroke="{CORAL}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
            '<rect x="362" y="30" width="150" height="180" rx="14" fill="#FFFFFF" stroke="#141A55" stroke-width="6"/>'
            + "".join(f'<path d="M384 {y0} l14 14 l26 -28" fill="none" stroke="{CORAL}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
                      f'<rect x="438" y="{y0 - 4}" width="54" height="12" rx="6" fill="rgba(20,26,85,.25)"/>' for y0 in (76, 126, 176))
            + f'<text x="437" y="242" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="22" fill="{CORAL}">THIS MONTH’S BILLS</text>'
            '</svg>')


def account_card(x, y, w=250):
    """Drawn savings card, filled: big $2,000 and a tick (slide 3 object, replaces the retired halftone hand). The words are in the
    handwritten line beside it ("next month's $2,000 of bills: already saved")."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.8:.0f}px;z-index:3;overflow:visible" viewBox="0 0 250 200">'
            '<rect x="14" y="16" width="230" height="180" rx="22" fill="#141A55"/>'
            '<rect x="4" y="4" width="230" height="180" rx="22" fill="#FFFFFF" stroke="#141A55" stroke-width="6"/>'
            f'<circle cx="119" cy="58" r="34" fill="{CORAL}"/>'
            '<path d="M101 58 l12 13 l24 -26" fill="none" stroke="#FFFFFF" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<text x="119" y="160" text-anchor="middle" font-family="Inter Display, Inter" font-weight="800" font-size="60" fill="#141A55">${BILLS:,}</text>'
            '</svg>')


def no_hand(html):
    out, n = re.subn(r'<img class="obj"[^>]*>', "", html)
    assert n == 1, n
    return out


def cover():
    body = C.lay_pills(FF, COVER)
    body = P.lift_save(re.sub(r'<img class="obj"[^>]*>', "", body, count=1))   # drawn month strip replaces the halftone object
    body = body.replace("width:620px;font-size:66px", "width:470px;font-size:62px", 1)
    return C.page(FF, "coral", body + gap_strip(), W, H)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = C.R()
    try:
        files = [r.shot(cover(), W, H, OUT / "01.jpg"),
                 r.shot(C.page(FF, S2["f"], C.inner(FF, S2, 1, 3) + two_months(280, 1000, 520), W, H), W, H, OUT / "02.jpg"),
                 r.shot(C.page(FF, S3["f"], no_hand(C.inner(FF, S3, 2, 3)).replace("left:300px;top:1020px;width:700px;font-size:76px", "left:320px;top:1000px;width:470px;font-size:70px") + account_card(50, 1030, 250), W, H), W, H, OUT / "03.jpg")]
    finally:
        r.close()
    print(files)


if __name__ == "__main__":
    main()

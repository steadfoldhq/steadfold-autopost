#!/usr/bin/env python3
"""Oct 25 studio build: Rich Habits, Decoded No. 2 (ff-richhabits-02), Wed Oct 28 17:00.
Same series layout as No. 1 (studio/recovery-oct22/fullyfunded/build/richhabits.py, imported, not edited): pills cover with the
series badge, handwritten series line, round stamp and a small drawn-to-scale chart in place of the halftone object; slides 2-3 from
covers.inner(). Habit: split every yearly bill by 12 and save it monthly (a "sinking fund"), on a normal paycheque.

    python3 studio/editorial/oct25_fullyfunded_feed.py
Writes media/studio-oct25/fullyfunded/ff-richhabits-02/0N.jpg. Prices are made up for this post and labelled so on slide 3.
"""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
sys.path.insert(0, str(REPO / "studio/recovery-oct22/fullyfunded/build"))
import glob as _glob  # noqa: E402
_g0 = _glob.glob  # this box ships chromium as chrome-linux64/; covers.py looks for chrome-linux/ (shared file left untouched)
_glob.glob = lambda p, *a, **k: _g0(p, *a, **k) or _g0(p.replace("chrome-linux/", "chrome-linux64/"), *a, **k)
import covers as C  # noqa: E402
import richhabits as RH  # noqa: E402,F401  (No. 1's module: same series layout; its C.place hook is harmless here)
_glob.glob = _g0
import edkit as K  # noqa: E402

OUT = REPO / "media/studio-oct25/fullyfunded/ff-richhabits-02"
FF = "fullyfunded"
W, H = 1080, 1350
COB, CORAL = "#2B3FE0", "#E04E28"
SAVE = "new one<br>every Mon · Wed · Fri"            # series line, as on No. 1 (gate, Oct 24)

# Same pill fix the Oct 24 gate applied to the series (pills start lower, stay UNDER the words)
_css0 = K.css
K.css = lambda brand, W_, H_: _css0(brand, W_, H_) + ".S .pill,.pill{border-top:.2em solid transparent;background-clip:padding-box!important}\n"

# ---------------------------------------------------------------- MATHS (made up for this post; stated on slide 3 and in the caption)
INS, GIFTS = 1200, 600
M_INS, M_GIFTS = INS // 12, GIFTS // 12
M_TOT = M_INS + M_GIFTS
assert (M_INS, M_GIFTS, M_TOT) == (100, 50, 150)
PER_PAY_26 = INS / 26                                   # paid every 2 weeks: 26 paydays
assert round(PER_PAY_26, 2) == 46.15


def fund_chart(x0=560, y0=880, w=460, h=420):
    """Drawn to scale: $100 a month piles up Jan..Dec and meets the $1,200 bill line in December."""
    base, top = y0 + h - 76, y0 + 100
    out = [f'<svg style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="{x0} {y0} {w} {h}">',
           f'<rect x="{x0 + 6}" y="{y0 + 6}" width="{w - 12}" height="{h - 12}" fill="rgba(255,255,255,.55)" stroke="{COB}" stroke-width="3"/>']
    for gx in range(x0 + 6, x0 + w - 6, 30):
        out.append(f'<line x1="{gx}" y1="{y0 + 6}" x2="{gx}" y2="{y0 + h - 6}" stroke="rgba(43,63,224,.10)" stroke-width="1"/>')
    for gy in range(y0 + 6, y0 + h - 6, 30):
        out.append(f'<line x1="{x0 + 6}" y1="{gy}" x2="{x0 + w - 6}" y2="{gy}" stroke="rgba(43,63,224,.10)" stroke-width="1"/>')
    bw, gap, sx = 26, 7, x0 + 34
    for m in range(12):
        x = sx + m * (bw + gap)
        bh = (base - top) * (m + 1) / 12
        out.append(f'<rect x="{x}" y="{base - bh:.0f}" width="{bw}" height="{bh:.0f}" fill="{COB if m == 11 else "#C9D3F7"}" '
                   f'stroke="{COB}" stroke-width="3"/>')
    xe = sx + 12 * (bw + gap) - gap
    out.append(f'<line x1="{sx - 10}" y1="{top}" x2="{xe + 8}" y2="{top}" stroke="{CORAL}" stroke-width="4" stroke-dasharray="10 7"/>')
    out.append(f'<text x="{xe + 6}" y="{top - 14}" text-anchor="end" font-family="DejaVu Sans Mono" font-weight="700" font-size="24" '
               f'fill="{CORAL}">BILL DUE: $1,200</text>')
    out.append(f'<line x1="{sx - 10}" y1="{base}" x2="{xe + 8}" y2="{base}" stroke="{COB}" stroke-width="5"/>')
    for m, lab in ((0, "JAN"), (11, "DEC")):
        out.append(f'<text x="{sx + m * (bw + gap) + bw / 2}" y="{base + 40}" text-anchor="middle" font-family="DejaVu Sans Mono" '
                   f'font-weight="700" font-size="24" fill="{COB}">{lab}</text>')
    out.append(f'<text x="{sx + 200}" y="{base + 40}" text-anchor="middle" font-family="DejaVu Sans Mono" font-size="22" fill="{COB}">+$100 A MONTH</text>')
    out.append(f'<text x="{x0 + 26}" y="{y0 + 46}" font-family="DejaVu Sans Mono" font-size="22" fill="{COB}" letter-spacing="2">SAVED FOR THE BILL</text>')
    out.append("</svg>")
    return "".join(out)


def calendar(x, y, w=300):
    """Drawn calendar page: 12 months, each ticked (Fully Funded cobalt/coral line)."""
    cells = []
    for k in range(12):
        cx, cy = 34 + (k % 4) * 60, 110 + (k // 4) * 56
        cells.append(f'<rect x="{cx}" y="{cy}" width="48" height="44" rx="8" fill="#FFFFFF" stroke="#141A55" stroke-width="3"/>'
                     f'<path d="M{cx + 12} {cy + 23} l9 9 l16 -18" stroke="{CORAL}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.97:.0f}px;z-index:3;overflow:visible" viewBox="0 0 300 290">'
            '<rect x="14" y="30" width="272" height="250" rx="24" fill="#FBF2DF" stroke="#141A55" stroke-width="6"/>'
            f'<rect x="14" y="30" width="272" height="62" rx="24" fill="{COB}" stroke="#141A55" stroke-width="6"/>'
            '<rect x="70" y="12" width="14" height="40" rx="7" fill="#141A55"/><rect x="216" y="12" width="14" height="40" rx="7" fill="#141A55"/>'
            + "".join(cells) + "</svg>")


COVER = dict(lay="pills", f="coral", kicker="rich habits, decoded · no. 2", text="Insurance due. / *Surprised* / *again?*", obj="ok", at="br",
             save=SAVE)
S2 = dict(f="lite", text="Divide each / yearly bill / *by 12.*",
          sub="save that much every month")
S3 = dict(f="cob", text="Your yearly bills, / *monthly*", cap="made up for this post · use your own bills",
          rows=[(f"Insurance ${INS:,}/yr", f"${M_INS}"), (f"Gifts ${GIFTS}/yr", f"${M_GIFTS}"), ("Save each month", f"${M_TOT}")],
          sub="no more surprise bills")


def lift_save(body, dy=-50):
    """Two-line series save-line: lift it so its 2nd line clears the corner stamp (as on No. 1)."""
    return re.sub(r'(<div class="hand" style="position:absolute;left:\d+px;top:)(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + dy), body, count=1)


def cover():
    body = C.lay_pills(FF, COVER)
    body = lift_save(re.sub(r'<img class="obj"[^>]*>', "", body, count=1))       # drawn chart replaces the halftone object
    body = body.replace("width:620px;font-size:66px", "width:470px;font-size:62px", 1)
    return C.page(FF, "coral", body + fund_chart(), W, H)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = C.R()
    try:
        files = [r.shot(cover(), W, H, OUT / "01.jpg"),
                 r.shot(C.page(FF, S2["f"], C.inner(FF, S2, 1, 3) + calendar(390, 960, 300), W, H), W, H, OUT / "02.jpg"),
                 r.shot(C.page(FF, S3["f"], C.inner(FF, S3, 2, 3), W, H), W, H, OUT / "03.jpg")]
    finally:
        r.close()
    print(files)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Oct 26 studio build: Rich Habits, Decoded No. 3 (ff-richhabits-03), Fri Oct 30 17:00.
The parked "yearly bills / 12" episode (built Oct 25 as an insurance No. 2 by oct25_fullyfunded_feed.py, then parked when the
lunch No. 2 stayed queued). Same series layout, imported (nothing in it edited). Changes for No. 3:
  - cover badge "rich habits, decoded · no. 3"
  - slide 3: the retired halftone OK-hand cut-out (covers.inner always adds one) is removed; a drawn "BILLS" jar takes its place
  - slide 3 header "a year → a month" labels both columns; rows kept short so every pill sits inside the card (gate r2)

    python3 studio/editorial/oct26_fullyfunded_feed.py
Writes media/studio-oct26/fullyfunded/ff-richhabits-03/0N.jpg.
"""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import oct25_fullyfunded_feed as P  # noqa: E402  (series layout, pill fix, chart, calendar)

C = P.C
FF, W, H, COB, CORAL = P.FF, P.W, P.H, P.COB, P.CORAL
OUT = REPO / "media/studio-oct26/fullyfunded/ff-richhabits-03"

P.COVER = dict(P.COVER, kicker="rich habits, decoded · no. 3")
S3 = dict(f="cob", text="Your yearly bills, / *monthly*", cap="made up for this post · a year → a month",
          rows=[(f"Insurance ${P.INS:,}", f"${P.M_INS}"), (f"Gifts ${P.GIFTS}", f"${P.M_GIFTS}"),
                ("Save each month", f"${P.M_TOT}")],
          sub="no more surprise bills")


def jar(x, y, w=230):
    """Drawn glass jar labelled BILLS, a third full of coins (FF signature object: jar)."""
    h = w * 1.15
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h:.0f}px;z-index:3;overflow:visible" viewBox="0 0 200 230">'
            '<rect x="40" y="8" width="120" height="26" rx="8" fill="#141A55"/>'
            '<path d="M48 34 Q22 50 22 90 L22 196 Q22 222 50 222 L150 222 Q178 222 178 196 L178 90 Q178 50 152 34 Z" '
            'fill="rgba(255,255,255,.65)" stroke="#141A55" stroke-width="6"/>'
            '<path d="M25 160 L175 160 L175 196 Q175 219 150 219 L50 219 Q25 219 25 196 Z" fill="#F6D44C" opacity=".9"/>'
            + "".join(f'<ellipse cx="{cx}" cy="{cy}" rx="22" ry="8" fill="#F6D44C" stroke="#141A55" stroke-width="3"/>'
                      for cx, cy in ((70, 160), (112, 152), (148, 162), (92, 142)))
            + '<rect x="46" y="88" width="108" height="44" rx="10" fill="#FFFFFF" stroke="#141A55" stroke-width="4"/>'
            f'<text x="100" y="119" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="24" fill="{CORAL}">BILLS</text>'
            '</svg>')


def no_hand(html):
    out, n = re.subn(r'<img class="obj"[^>]*>', "", html)
    assert n == 1, n
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = C.R()
    try:
        files = [r.shot(P.cover(), W, H, OUT / "01.jpg"),
                 r.shot(C.page(FF, P.S2["f"], C.inner(FF, P.S2, 1, 3) + P.calendar(390, 960, 300), W, H), W, H, OUT / "02.jpg"),
                 r.shot(C.page(FF, S3["f"], no_hand(C.inner(FF, S3, 2, 3)) + jar(70, 1010), W, H), W, H, OUT / "03.jpg")]
    finally:
        r.close()
    print(files)


if __name__ == "__main__":
    main()

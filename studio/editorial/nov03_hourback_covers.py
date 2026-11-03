#!/usr/bin/env python3
"""Dedicated Reel covers for the Nov 3 Hourback build (never a raw frame). 1080x1920, 2x then Lanczos down.
Reuses oct28_hourback_covers.page()/shot() and nov01_hourback_covers.sticky_list() by import (paths re-pointed); edits
nothing shared.

thanks  -> sticky-note list (style 13, QUIET). Grid: after Fri 5:45 pm Day 13 (series Look B, loud).
dinners -> follow the line (LOUD): the hook huge, then Claude's real 'used more than once' lines drawn as coloured lines
           from 3 ingredients to the weekday pills (Chicken: Mon, Tue, Thu / Bell peppers: Mon, Wed, Fri / Black beans:
           Wed, Fri, word for word from hb-nov03-run-dinners.txt). Grid: after Fri 7 pm thanks (sticky list, quiet).
All text inside x 90-990, y 300-1400; hooks >= 120 px.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True
import oct28_hourback_covers as C  # noqa: E402
import nov01_hourback_covers as C1  # noqa: E402
import edkit as K  # noqa: E402

C.OUT = Path("/home/claude/steadfold-autopost/media/studio-nov03/hourback")
C.SCR = Path("/tmp/claude-0/nov03-hourback")
HB, INK, ACC = C.HB, C.INK, C.ACC

ENVS = ('<svg style="position:absolute;left:560px;top:760px" width="300" height="230" viewBox="0 0 300 230">'
        + "".join(f'<g transform="translate({20 + i * 6} {150 - i * 26}) rotate({(-1) ** i * 3} 130 40)"><rect width="250" height="80" rx="8" fill="#FFFFFF" stroke="#2A1D47" stroke-width="5"/>'
                  f'<path d="M0 0 L125 44 L250 0" fill="none" stroke="#2A1D47" stroke-width="5"/></g>' for i in range(5))
        + '<g transform="translate(200 20) rotate(10)"><rect width="96" height="56" rx="10" fill="#FFC94D" stroke="#2A1D47" stroke-width="4"/>'
          '<text x="48" y="40" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="30" fill="#2A1D47">×20</text></g></svg>')


def thanks_cover():
    b = C1.sticky_list("20 thank-you<br>notes.<br>Due today.",
                       ["paste who gave what", "AI drafts all 20", "read, fix, sign"],
                       "real Claude notes inside", items_top=520, tsize=128, extra=ENVS)
    b += K.stamp(HB, 800, 1440, size=150, rot=-10)
    return C.page("#C9CAF5", b)


DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
LINES = [("Chicken", ["Mon", "Tue", "Thu"], "#FF8A3D"), ("Bell peppers", ["Mon", "Wed", "Fri"], "#E8453C"),
         ("Black beans", ["Wed", "Fri"], "#5E54C9")]


def follow_svg():
    """3 ingredient chips (left) -> lines -> 5 weekday pills (right). Pills x 760, rows y 0..; chips x 0."""
    w, h = 900, 560
    s = f'<svg style="position:absolute;left:90px;top:820px" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
    py = {d: 40 + i * 110 for i, d in enumerate(DAYS)}
    cy = [100, 280, 460]
    for k, (nm, ds, col) in enumerate(LINES):
        for d in ds:
            s += (f'<path d="M390 {cy[k]} C 560 {cy[k]}, 560 {py[d]}, 720 {py[d]}" fill="none" stroke="{col}" stroke-width="12" '
                  f'stroke-linecap="round" opacity=".95"/>')
    for k, (nm, ds, col) in enumerate(LINES):
        s += (f'<rect x="0" y="{cy[k] - 46}" width="390" height="92" rx="46" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
              f'<circle cx="46" cy="{cy[k]}" r="22" fill="{col}" stroke="{INK}" stroke-width="4"/>'
              f'<text x="84" y="{cy[k] + 15}" font-family="Poppins" font-weight="700" font-size="38" fill="{INK}">{nm}</text>')
    for d in DAYS:
        s += (f'<rect x="720" y="{py[d] - 40}" width="170" height="80" rx="40" fill="#FFC94D" stroke="{INK}" stroke-width="5"/>'
              f'<text x="805" y="{py[d] + 15}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="40" fill="{INK}">{d}</text>')
    return s + "</svg>"


def dinners_cover():
    f = dict(p1="#FFC94D", p2="#FFD4BD")
    b = K.dual("Store closes at 9. / *5 dinners?*", f, cls="S fit",
               style=f"position:absolute;left:90px;width:900px;top:320px;white-space:nowrap;font-size:150px;line-height:1.1;color:{INK}")
    b += f'<div class="hand" style="position:absolute;left:90px;right:90px;top:680px;font-size:68px;transform:rotate(-2deg)">AI plans them to share ingredients</div>'
    b += follow_svg()
    b += f'<div style="position:absolute;left:90px;top:1395px;font:600 30px Inter;color:{INK};opacity:.75">Claude\'s real lines · plan made up for this post</div>'
    b += K.stamp(HB, 820, 1480, size=150, rot=-10)
    return C.page("#FFF5EA", b)


def build(key):
    C.OUT.mkdir(parents=True, exist_ok=True)
    if key == "thanks":
        return C.shot(thanks_cover(), C.OUT / "hb-reel-1106-thank-you-20-cover.jpg")
    if key == "dinners":
        return C.shot(dinners_cover(), C.OUT / "hb-reel-1107-5-dinners-cover.jpg")


if __name__ == "__main__":
    for k in sys.argv[1:]:
        print(build(k))

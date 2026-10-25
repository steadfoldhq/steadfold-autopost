#!/usr/bin/env python3
"""Oct 25 gate fixes for two QUEUED Fully Funded series posts, rendered as NEW files (queued media untouched).

  ff-richhabits-02 (queued "$15 lunch", built by oct24_feed.py) -> media/studio-oct25/fullyfunded/ff-richhabits-02-r2/01-03.jpg
     (a) cover chart: second bar label "PACK 3, BUY 2" (it is the mixed week's cost, not the cost of 3 packed days)
     (b) slide 3: the retired halftone OK-hand cut-out is removed; a drawn lunchbox takes its place
  ff-richhabits-01 (queued Mon 5 pm, recovery-oct22 richhabits.py) -> media/studio-oct25/fullyfunded/ff-richhabits-01-r2/01-03.jpg
     slide 1 copied unchanged; slide 2 save-line "do this: move savings out the day your pay lands";
     slide 3 "Save more with every raise." + "In one study, workers who did went from saving 3.5% of their pay to 13.6%."

Uses oct24_feed.py's code path by import (its pill fix, lift_save, ed_inner, FF02 specs); nothing in it is edited.
    python3 studio/editorial/oct25_fullyfunded_fixes.py [rh02] [rh01]
"""
import re
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import oct24_feed as O  # noqa: E402  (registers its POSTS; main() not called)

C, K = O.C, O.K
FF, W, H = O.FF, O.W, O.H
OUT = REPO / "media/studio-oct25/fullyfunded"
COB, CORAL = O.COB, O.CORAL
ALL5, MIX = O.ALL5, O.MIX


def lunch_chart(x0=560, y0=900, w=460, h=400):
    """oct24_feed.lunch_chart with the second bar labelled for what it is: pack 3 days AND buy 2 (the whole week)."""
    base, top = y0 + h - 80, y0 + 96
    out = [f'<svg style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="{x0} {y0} {w} {h}">',
           f'<rect x="{x0 + 6}" y="{y0 + 6}" width="{w - 12}" height="{h - 12}" fill="rgba(255,255,255,.55)" stroke="{COB}" stroke-width="3"/>']
    for gx in range(x0 + 6, x0 + w - 6, 30):
        out.append(f'<line x1="{gx}" y1="{y0 + 6}" x2="{gx}" y2="{y0 + h - 6}" stroke="rgba(43,63,224,.10)" stroke-width="1"/>')
    for gy in range(y0 + 6, y0 + h - 6, 30):
        out.append(f'<line x1="{x0 + 6}" y1="{gy}" x2="{x0 + w - 6}" y2="{gy}" stroke="rgba(43,63,224,.10)" stroke-width="1"/>')
    bars = [("BUY 5 DAYS", ALL5, COB), ("PACK 3, BUY 2", MIX, "#C9D3F7")]
    bw = 130
    for i, (lab, v, fill) in enumerate(bars):
        x = x0 + 70 + i * 190
        bh = (base - top) * v / ALL5
        out.append(f'<rect x="{x}" y="{base - bh:.0f}" width="{bw}" height="{bh:.0f}" fill="{fill}" stroke="{COB}" stroke-width="4"/>')
        out.append(f'<text x="{x + bw / 2}" y="{base - bh - 14:.0f}" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" '
                   f'font-size="28" fill="{CORAL if i else COB}">${v:,}</text>')
        out.append(f'<text x="{x + bw / 2}" y="{base + 42}" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" '
                   f'font-size="21" fill="{COB}">{lab}</text>')
    out.append(f'<line x1="{x0 + 40}" y1="{base}" x2="{x0 + w - 40}" y2="{base}" stroke="{COB}" stroke-width="5"/>')
    out.append(f'<text x="{x0 + 26}" y="{y0 + 46}" font-family="DejaVu Sans Mono" font-size="22" fill="{COB}" letter-spacing="2">LUNCH MONEY, 1 YEAR</text>')
    out.append("</svg>")
    return "".join(out)


O.lunch_chart = lunch_chart          # O.ff_cover() looks the chart up in its module globals


def no_hand(html):
    """Drop the halftone OK-hand cut-out that covers.inner_list() always adds (hand props are retired)."""
    out, n = re.subn(r'<img class="obj"[^>]*>', "", html)
    assert n == 1, n
    return out


def rh02(r):
    d = OUT / "ff-richhabits-02-r2"
    d.mkdir(parents=True, exist_ok=True)
    s3 = C.page(FF, O.FF02_S[1]["f"], no_hand(C.inner(FF, O.FF02_S[1], 2, 3)) + O.svg_lunchbox(60, 1050, 260), W, H)
    pages = [O.ff_cover(), O.ed_inner(FF, O.FF02_S[0], 1, 3, O.svg_lunchbox(390, 930, 300))(), s3]
    for i, html in enumerate(pages, 1):
        r.shot(html, W, H, d / f"{i:02d}.jpg")
    print("ff-richhabits-02-r2", sorted(p.name for p in d.glob("*.jpg")))


RH01_S2 = dict(f="lite", text="Pay *yourself* / first.", sub="do this: on payday, auto-move savings into a separate account")
RH01_S3 = dict(f="cob", text="Save more / *with every raise.*",
               sub="In one study, workers who saved more at each raise went from saving 3.5% of their pay to 13.6% in about 3 years.", src="Thaler &amp; Benartzi, 2004")


def rh01(r):
    d = OUT / "ff-richhabits-01-r3"   # gate round 3 wording (r2 kept)
    d.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(REPO / "media/recovery-oct22/fullyfunded/ff-richhabits-01/01.jpg", d / "01.jpg")
    r.shot(C.page(FF, RH01_S2["f"], C.inner(FF, RH01_S2, 1, 3), W, H), W, H, d / "02.jpg")
    r.shot(C.page(FF, RH01_S3["f"], C.inner(FF, RH01_S3, 2, 3), W, H), W, H, d / "03.jpg")
    print("ff-richhabits-01-r3", sorted(p.name for p in d.glob("*.jpg")))


if __name__ == "__main__":
    which = sys.argv[1:] or ["rh02", "rh01"]
    r = C.R()
    try:
        if "rh02" in which:
            rh02(r)
        if "rh01" in which:
            rh01(r)
    finally:
        r.close()

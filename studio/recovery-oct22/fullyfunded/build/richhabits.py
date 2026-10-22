#!/usr/bin/env python3
"""Rich Habits, Decoded No. 1 (ff-richhabits-01), recovery cut: same series layout (pills + badge kicker + save-line + stamp),
but the overused halftone piggy is replaced by a drawn-to-scale "pay week" chart (the paycheque draining Fri -> Wed), and
slide 3's number is qualified as one study's saving rate. Writes media/recovery-oct22/fullyfunded/ff-richhabits-01/0N.jpg."""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import covers as C  # noqa: E402
import edkit as K  # noqa: E402

OUT = REPO / "media/recovery-oct22/fullyfunded/ff-richhabits-01"
COB, INK, CORAL = "#2B3FE0", "#141A55", "#E04E28"


def week_chart(x0=560, y0=860, w=460, h=430):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    left = [1.0, 0.62, 0.41, 0.27, 0.12, 0.0]   # share of the paycheque still there (illustrative shape, no figure claimed)
    bw, gap = 50, 16
    base = y0 + h - 70
    top = y0 + 70
    out = [f'<svg style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" '
           f'viewBox="{x0} {y0} {w} {h}">',
           f'<rect x="{x0 + 6}" y="{y0 + 6}" width="{w - 12}" height="{h - 12}" fill="rgba(255,255,255,.55)" stroke="{COB}" stroke-width="3"/>']
    for gx in range(x0 + 6, x0 + w - 6, 30):
        out.append(f'<line x1="{gx}" y1="{y0 + 6}" x2="{gx}" y2="{y0 + h - 6}" stroke="rgba(43,63,224,.10)" stroke-width="1"/>')
    for gy in range(y0 + 6, y0 + h - 6, 30):
        out.append(f'<line x1="{x0 + 6}" y1="{gy}" x2="{x0 + w - 6}" y2="{gy}" stroke="rgba(43,63,224,.10)" stroke-width="1"/>')
    sx = x0 + 34
    for i, (d, v) in enumerate(zip(days, left)):
        x = sx + i * (bw + gap)
        bh = (base - top) * v
        if v > 0:
            out.append(f'<rect x="{x}" y="{base - bh:.0f}" width="{bw}" height="{bh:.0f}" fill="{"#C9D3F7" if i else COB}" stroke="{COB}" stroke-width="4"/>')
        else:
            out.append(f'<rect x="{x}" y="{base - 14}" width="{bw}" height="14" fill="none" stroke="{CORAL}" stroke-width="4" stroke-dasharray="8 6"/>')
        out.append(f'<text x="{x + bw / 2}" y="{base + 44}" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" '
                   f'font-size="24" fill="{CORAL if d == "WED" else COB}">{d}</text>')
    out.append(f'<line x1="{sx - 12}" y1="{base}" x2="{sx + 6 * (bw + gap) - 6}" y2="{base}" stroke="{COB}" stroke-width="5"/>')
    out.append(f'<text x="{x0 + 26}" y="{y0 + 46}" font-family="DejaVu Sans Mono" font-size="22" fill="{COB}" letter-spacing="2">PAYCHEQUE LEFT</text>')
    out.append("</svg>")
    return "".join(out)


_place = C.place


def place(name, at, H=1350, dy=0):
    if name == "week":
        return week_chart()
    return _place(name, at, H, dy)


C.place = place

COVER = dict(lay="pills", f="coral", kicker="rich habits, decoded · no. 1", text="Paid Friday. / *Broke by* / *Wednesday?*", obj="week", at="br",
             save="mon · wed · fri")
SLIDES = [dict(f="lite", text="Pay *yourself* / first.", sub="move it the day it lands"),
          dict(f="cob", text="Saving rate / *3.5% → 13.6%*", sub="in one study, as it rose with every raise",
               src="Thaler &amp; Benartzi, 2004")]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = C.R()
    b = "fullyfunded"
    n = 1 + len(SLIDES)
    files = [r.shot(C.page(b, COVER["f"], C.LAYOUTS["pills"](b, COVER), 1080, 1350), 1080, 1350, OUT / "01.jpg")]
    for i, s in enumerate(SLIDES, 1):
        files.append(r.shot(C.page(b, s["f"], C.inner(b, s, i, n), 1080, 1350), 1080, 1350, OUT / f"{i + 1:02d}.jpg"))
    r.close()
    print(files)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Oct 25 (Social studio, Littlefold maker): 3 am Club No. 2, 2 slides, same layout as No. 1 (lf-3amclub-01 was rendered by
oct24_feed.py through covers.py: pills cover, berry field, halftone shoe, 'new night tip every Mon · Wed · Fri' line; inner
slide on cream with a drawn object and a source line). Imports those helpers; edits nothing. Renders to
media/studio-oct25/littlefold/lf-3amclub-02/0N.jpg (the older 3-slide render in media/lf-3amclub-02/ is left untouched).

    python3 studio/editorial/oct25_littlefold_feed.py
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import oct24_feed as F  # noqa: E402

LF = F.LF
PID = "lf-3amclub-02"
OUT = F.REPO / "media" / "studio-oct25" / "littlefold" / PID
COVER = dict(lay="pills", f="berry", kicker="3 am club · no. 2", text="3 am, and / baby's wide / *awake?*", obj="shoe", at="br",
             save=F.SAVE_LF)
S2 = dict(f="cream", text="Big light *off.* / Quiet voice. / *No play.*", sub="fed and changed? back in their crib, on their back",
          src="NHS")
PAGES = [F.ed_cover(LF, COVER), F.ed_inner(LF, S2, 1, 2, F.svg_lamp(790, 990, 220))]


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

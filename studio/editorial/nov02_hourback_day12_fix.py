#!/usr/bin/env python3
"""Gate fix (Nov 2 2026) for the queued hb-day12-potluck (Wed Nov 4, 17:45): re-render SLIDE 3 ONLY.

    python3 studio/editorial/nov02_hourback_day12_fix.py

Slide 3 said "Fits all 3 diets. It wrote:" as a fact. On an allergy topic that is risky: some people with nut allergies
avoid coconut, and curry paste or stock can hide gluten. New heading: "AI's 3 ideas / for all 3 diets:" and the save line
now says "check every label for nuts, gluten and dairy" (the "cooking times… in the caption" line is dropped for space).
The 3 dish names stay word for word from studio/editorial/hb-nov01-run-potluck.txt.
Overwrites media/studio-nov01/hourback/hb-day12-potluck/03.jpg (the path schedule/posts.json uses); the Nov 1 version is
kept at media/studio-nov02/hourback/rollback/hb-day12-potluck-03-nov01.jpg. Imports nov01_hourback_feed; edits nothing older.
"""
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import nov01_hourback_feed as F  # noqa: E402

C, K, HB, W, H = F.C, F.K, F.HB, F.W, F.H
SLIDE = dict(f="yel", text="AI's 3 ideas / *for all 3 diets:*",
             items=["Black bean & corn salad", "Coconut chickpea curry over rice", "Roasted potatoes and veggies"])
SAVE3 = "real reply, shortened<br>check every label for<br>nuts, gluten and dairy"


def main():
    dst = C.REPO / "media" / F.D12 / "03.jpg"
    bak = C.REPO / "media/studio-nov02/hourback/rollback/hb-day12-potluck-03-nov01.jpg"
    if not bak.exists():
        bak.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(dst, bak)
    r = C.R()
    try:
        out = r.shot(C.page(HB, "yel", C.inner(HB, SLIDE, 2, 3) + K.save_line(SAVE3, 60, 1080, 760, 54, -3, HB), W, H), W, H, dst)
    finally:
        r.close()
    print(out, bak)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Gate fix (Nov 1 2026) for the queued hb-day11-gift-for-dad (Mon Nov 2, 17:45): stranger verdict CONFUSING.
- Slide 2 header: "type this, with your own details:" (was "type this about your person:").
- Slide 3: bullets, no numbers (the 4, 1, 5 numbering read as an error); header "3 of its 5 ideas (all 5 in the caption)";
  "Claude's own numbers" dropped.
Writes a NEW folder media/studio-nov01/hourback/hb-day11-gift-for-dad/ (slide 1 copied unchanged from the Oct 28 build;
the Oct 28 media is not overwritten). Reuses oct28_hourback_feed by import; edits nothing shared.

    python3 studio/editorial/nov01_hourback_day11_fix.py
"""
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oct28_hourback_feed as D11  # noqa: E402

C, K, HB, W, H = D11.C, D11.K, D11.HB, D11.W, D11.H
SRC = C.REPO / "media/studio-oct28/hourback/hb-day11-gift-for-dad"
OUT = C.REPO / "media/studio-nov01/hourback/hb-day11-gift-for-dad"
SLIDE3 = dict(f="yel", text="3 of its 5 ideas / *(all 5 in the caption)*",
              items=["Heirloom seed collection (~$25)", "Premium whole-bean coffee sampler (~$30)",
                     "Personalized garden kneeler or stool (~$40)"])


def slide2():
    f = K.FIELDS[HB]["indi"]
    ink = f["ink"]
    body = C.head(HB, f, "In ChatGPT, Claude or Gemini,", 110, 90, 64)
    body += C.head(HB, f, "type this, / *with your own details:*", 200, 330, 150)
    body += (f'<div style="position:absolute;left:80px;right:80px;top:560px;background:#FFFFFF;border:4px solid {ink};border-radius:36px;'
             f'box-shadow:0 16px 0 {ink};padding:30px 44px 36px;z-index:3;color:{ink}">'
             f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px">'
             f'<span style="font:700 28px Inter;letter-spacing:.12em;text-transform:uppercase;opacity:.7">Copy this prompt</span>'
             f'<span style="font:700 26px Inter;background:{ink};color:#FFF5EA;border-radius:99px;padding:8px 22px">⧉ copy</span></div>'
             f'<div style="font:500 44px/1.5 Inter">{D11.PROMPT}</div></div>')
    body += K.save_line("change the yellow words to yours", 50, 1120, 720, 54, -3, HB)
    body += f'<div style="position:absolute;right:60px;top:40px;font:600 30px/1 Fraunces;color:{ink};opacity:.55;z-index:5">2/3</div>'
    body += K.stamp(HB, W - 200, H - 185, 145, -12)
    return C.page(HB, "indi", body, W, H)


def bullets(html):
    """Number circles 1, 2, 3 -> bullet dots (no numbering at all)."""
    for k in (1, 2, 3):
        a = f'line-height:88px">{k}</span>'
        assert html.count(a) == 1, k
        html = html.replace(a, 'line-height:88px">•</span>')
    return html


def build(r):
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC / "01.jpg", OUT / "01.jpg")
    return [OUT / "01.jpg",
            r.shot(slide2(), W, H, OUT / "02.jpg"),
            r.shot(C.page(HB, "yel", bullets(C.inner(HB, SLIDE3, 2, 3)) + K.save_line("real reply, shortened", 70, 1090, 760, 50, -3, HB), W, H),
                   W, H, OUT / "03.jpg")]


if __name__ == "__main__":
    r = C.R()
    try:
        print(build(r))
    finally:
        r.close()

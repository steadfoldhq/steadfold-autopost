#!/usr/bin/env python3
"""Dedicated Reel covers for the Nov 2 Hourback build (never a raw frame). 1080x1920, 2x then Lanczos down.
Reuses oct28_hourback_covers.page()/shot() by import (paths re-pointed); edits nothing shared.

interview -> 'Instead of… Ask…' reframe (style 7, QUIET). Grid: after Wed 5:45 pm Day 12 (series Look B, LOUD).
             The question on the 'Ask…' card is Claude's real question 4, word for word.
packing   -> one giant word (style 4 look, LOUD; a drawn suitcase stands in for the photo). Grid: after the interview
             reframe (quiet); before Fri's series tile (Look B, loud; two louds touch because the series cover is fixed loud).
All text inside x 90-990, y 300-1400; hooks >= 120 px.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True
import oct28_hourback_covers as C  # noqa: E402
import edkit as K  # noqa: E402

C.OUT = Path("/home/claude/steadfold-autopost/media/studio-nov02/hourback")
C.SCR = Path("/tmp/claude-0/nov02-hourback")
HB, INK, ACC = C.HB, C.INK, C.ACC


def interview_cover():
    f = dict(p1="#FFD4BD", p2="#C9CAF5")
    b = K.dual("Interview at 9 am. / *Haven't prepared.*", f, cls="S fit",
               style=f"position:absolute;left:90px;width:900px;top:330px;white-space:nowrap;font-size:132px;color:{INK}")
    b += (f'<div style="position:absolute;left:90px;right:90px;top:680px;background:#FFE6D3;border:4px solid {INK};border-radius:36px;padding:30px 46px 36px;transform:rotate(-1.5deg)">'
          f'<div style="font-family:\'Caveat Brush\';font-size:70px;color:{ACC};line-height:1">Instead of…</div>'
          f'<div style="font-family:\'Instrument Serif\';font-size:120px;line-height:1;color:{INK};margin-top:10px;text-decoration:line-through;text-decoration-thickness:7px;text-decoration-color:{ACC};opacity:.8">winging it</div></div>')
    b += (f'<div style="position:absolute;left:90px;right:90px;top:965px;background:#FFFFFF;border:4px solid {INK};border-radius:36px;padding:30px 46px 34px;box-shadow:0 14px 0 {INK};transform:rotate(1deg)">'
          f'<div style="font-family:\'Caveat Brush\';font-size:66px;color:{ACC};line-height:1">Paste the posting. Practise:</div>'
          f'<div style="font-family:\'Instrument Serif\';font-size:74px;line-height:1.05;color:{INK};margin-top:14px">“Your cash drawer is $20 short at close. What do you do?”</div>'
          f'<div style="font-family:\'Caveat Brush\';font-size:44px;color:#5E54C9;margin-top:14px;text-align:right">Claude\'s real question, word for word</div></div>')
    b += K.stamp(HB, 800, 1470, size=140, rot=-10)
    return C.page("#FFF5EA", b)


SUITCASE = ('<svg style="position:absolute;left:150px;top:1010px" width="560" height="400" viewBox="0 0 560 400">'
            '<path d="M200 70 V30 Q200 10 220 10 H340 Q360 10 360 30 V70" fill="none" stroke="#2A1D47" stroke-width="14"/>'
            '<rect x="40" y="70" width="480" height="290" rx="36" fill="#5E54C9" stroke="#2A1D47" stroke-width="8"/>'
            '<path d="M160 70 V360 M400 70 V360" stroke="#2A1D47" stroke-width="6"/>'
            '<rect x="70" y="350" width="40" height="30" rx="10" fill="#2A1D47"/><rect x="450" y="350" width="40" height="30" rx="10" fill="#2A1D47"/>'
            '<g transform="translate(430 120) rotate(14)"><path d="M0 0 C-6 24 6 40 0 56" stroke="#2A1D47" stroke-width="5" fill="none"/>'
            '<rect x="-70" y="56" width="150" height="88" rx="12" fill="#FFC94D" stroke="#2A1D47" stroke-width="5"/>'
            '<text x="5" y="114" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="34" fill="#2A1D47">6 am</text></g></svg>')


def packing_cover():
    """One giant word (style 4 look, LOUD): 'Packed?' huge, the hook above, a drawn carry-on, Caveat line, stamp."""
    f = dict(p1="#FFC94D", p2="#FFD4BD")
    b = K.dual("Flight at 6 am.", f, cls="S fit",
               style=f"position:absolute;left:90px;width:900px;top:330px;white-space:nowrap;font-size:130px;color:{INK}")
    b += K.dual("*Packed?*", f, cls="S fit",
                style=f"position:absolute;left:90px;width:900px;top:520px;white-space:nowrap;font-size:300px;line-height:1.05;color:{INK}")
    b += f'<div class="hand" style="position:absolute;left:90px;right:90px;top:880px;font-size:72px;transform:rotate(-2deg)">ask AI for a list sorted by room</div>'
    b += SUITCASE
    b += K.stamp(HB, 790, 1230, size=150, rot=-10)
    return C.page("#C9CAF5", b)


def build(key):
    C.OUT.mkdir(parents=True, exist_ok=True)
    if key == "interview":
        return C.shot(interview_cover(), C.OUT / "hb-reel-1104-interview-9am-cover.jpg")
    if key == "packing":
        return C.shot(packing_cover(), C.OUT / "hb-reel-1105-flight-6am-cover.jpg")


if __name__ == "__main__":
    for k in sys.argv[1:]:
        print(build(k))

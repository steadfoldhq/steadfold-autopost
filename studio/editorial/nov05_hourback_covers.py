#!/usr/bin/env python3
"""Dedicated Reel cover for the Nov 5 Hourback build (never a raw frame). 1080x1920, 2x then Lanczos down.
Reuses oct28_hourback_covers.page()/shot() by import (paths re-pointed); edits nothing shared.

sitter -> kinetic big text (style 5, LOUD): giant serif 'Babysitter at 6. / Messy brain dump?' (CD Nov 5: 2 lines, pill on line 2 with open leading), yellow pill,
          a drawn 5:48 clock magnet over a small fridge note whose 3 rows are Claude's REAL lines (word for word),
          Caveat line, stamp. Not the taped lined-note, not big-number, not Look B (CD Nov 4 + previous 2 grid covers:
          Mon Day 14 Look B, Mon 7 pm retire big number). Grid: after Mon 7 pm retire (quiet), before Wed Day 15 (Look B).
All text inside x 90-990, y 300-1400; hook >= 120 px.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True
import oct28_hourback_covers as C  # noqa: E402
import edkit as K  # noqa: E402

C.OUT = Path("/home/claude/steadfold-autopost/media/studio-nov05/hourback")
C.SCR = Path("/tmp/claude-0/nov05-hourback")
HB, INK, ACC = C.HB, C.INK, C.ACC
ROWS = [("7:00", "No screens from now on."), ("7:30", "Leo to bed with his stuffed rabbit."), ("8:00", "Maya to bed.")]


def sitter_cover():
    import nov05_hourback as R   # the real rows, parsed from the transcript
    real = dict(R.SD["raw"]["rows"])
    for k, v in ROWS:
        assert real[k] == v, (k, v)
    f = dict(p1="#FFC94D", p2="#FFD4BD")
    b = K.dual("Babysitter at 6. / *Messy brain dump?*", f, cls="S fit",
               style=f"position:absolute;left:90px;width:900px;top:330px;white-space:nowrap;font-size:150px;line-height:1.34;color:{INK}")
    rows = "".join(
        f'<div style="display:flex;align-items:center;gap:22px;margin-top:14px">'
        f'<span style="font:700 34px Poppins;color:{INK};background:#C9CAF5;border:3px solid {INK};border-radius:99px;padding:4px 20px">{k}</span>'
        f'<span style="font:700 50px Caveat;color:#3B34A0">{v}</span></div>' for k, v in ROWS)
    b += (f'<div style="position:absolute;left:110px;right:110px;top:800px;background:#FFFDF6;border:4px solid {INK};border-radius:14px;'
          f'padding:30px 40px 34px;box-shadow:0 14px 0 rgba(42,29,71,.18);transform:rotate(-1.2deg)">'
          f'<div style="font:400 40px \'Caveat Brush\';color:{ACC}">Claude\'s real note, shortened:</div>{rows}</div>')
    b += ('<svg style="position:absolute;left:640px;top:715px;transform:rotate(5deg)" width="300" height="130" viewBox="0 0 300 130">'
          f'<rect x="10" y="14" width="280" height="110" rx="22" fill="rgba(42,29,71,.18)"/><rect x="4" y="4" width="280" height="110" rx="22" fill="{INK}"/>'
          '<rect x="20" y="20" width="248" height="78" rx="12" fill="#3B2E5E"/>'
          '<text x="144" y="86" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="74" fill="#FFC94D">5:48</text></svg>')
    b += ('<svg style="position:absolute;left:150px;top:765px" width="60" height="60" viewBox="0 0 60 60"><circle cx="30" cy="30" r="24" fill="#FFC94D" stroke="#2A1D47" stroke-width="4"/></svg>')
    b += K.save_line("paste the mess, AI sorts it by time", 120, 1215, 840, 64, -3, HB)
    b += K.stamp(HB, 820, 1470, size=140, rot=-10)
    return C.page("#C9CAF5", b)


def build(key):
    C.OUT.mkdir(parents=True, exist_ok=True)
    if key == "sitter":
        return C.shot(sitter_cover(), C.OUT / "hb-reel-1110-sitter-at-6-cover.jpg")


if __name__ == "__main__":
    print(build(sys.argv[1]))

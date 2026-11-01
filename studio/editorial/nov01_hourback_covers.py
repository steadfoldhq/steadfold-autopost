#!/usr/bin/env python3
"""Dedicated Reel covers for the Nov 1 Hourback build (never a raw frame). 1080x1920, 2x then Lanczos down.
Reuses oct28_hourback_covers.page()/shot() by import (paths re-pointed); edits nothing shared.

toast -> sticky-note list (style 13, QUIET): lined note, red margin, tape, Caveat Brush title, Caveat items with ticks.
         Grid: after Sat 7 pm costume (kinetic big text, loud), before Mon 5:45 pm Day 11 (series Look B, loud).
cue   -> swipe-to-reveal style card (style 11, QUIET): after Day 11 (loud).
tidy  -> one-word photo-free giant word (style 4 look, LOUD): before Day 12 (Look B, loud).
All text inside x 90-990, y 300-1400.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True
import oct28_hourback_covers as C  # noqa: E402
import edkit as K  # noqa: E402

C.OUT = Path("/home/claude/steadfold-autopost/media/studio-nov01/hourback")
C.SCR = Path("/tmp/claude-0/nov01-hourback")
HB, INK, ACC = C.HB, C.INK, C.ACC


def sticky_list(title, items, foot, bg="#C9CAF5", note_top=330, tsize=120, items_top=442, extra=""):
    """Sticky-note list: lined card, red margin line, tape strip, Caveat Brush title, Caveat items with ticks."""
    lines = "".join(f'<div style="height:96px;border-bottom:3px solid #C7D2F2"></div>' for _ in range(11))
    its = "".join(
        f'<div style="display:flex;align-items:center;gap:26px;height:96px;font-family:Caveat;font-weight:700;font-size:70px;color:{INK}">'
        f'<span style="display:inline-flex;width:66px;height:66px;border-radius:50%;background:#FFC94D;border:4px solid {INK};'
        f'align-items:center;justify-content:center;font:800 40px Inter;color:{INK}">✓</span>{t}</div>' for t in items)
    return (f'<div style="position:absolute;left:90px;right:90px;top:{note_top}px;height:1060px;transform:rotate(-1.5deg)">'
            f'<div style="position:absolute;inset:0;transform:translate(14px,18px);background:rgba(42,29,71,.18);border-radius:10px"></div>'
            f'<div style="position:absolute;inset:0;background:#FFFDF6;border:4px solid {INK};border-radius:10px;overflow:hidden">'
            f'<div style="position:absolute;left:0;right:0;top:250px">{lines}</div>'
            f'<div style="position:absolute;left:108px;top:0;bottom:0;width:4px;background:#E86A6A"></div>'
            f'<div style="position:absolute;left:140px;right:40px;top:60px;font-family:\'Caveat Brush\';font-size:{tsize}px;line-height:1.0;color:{INK}">{title}</div>'
            f'<div style="position:absolute;left:140px;right:30px;top:{items_top}px">{its}</div>'
            f'{extra}'
            f'<div style="position:absolute;left:140px;right:40px;bottom:46px;font-family:\'Caveat Brush\';font-size:50px;color:{ACC};transform:rotate(-2deg)">{foot}</div></div>'
            f'<div style="position:absolute;left:340px;top:-34px;width:220px;height:68px;background:rgba(255,201,77,.75);border:2px solid rgba(42,29,71,.25);transform:rotate(-4deg)"></div></div>')


FLUTES = ('<svg style="position:absolute;left:560px;top:700px" width="285" height="240" viewBox="0 0 380 320">'
          '<g transform="translate(115 290) rotate(14)"><ellipse cx="0" cy="0" rx="46" ry="11" fill="#fff" stroke="#2A1D47" stroke-width="5"/>'
          '<path d="M0 -4 V-90" stroke="#2A1D47" stroke-width="6"/><path d="M-30 -230 Q-34 -110 0 -92 Q34 -110 30 -230Z" fill="#FFC94D" stroke="#2A1D47" stroke-width="5"/></g>'
          '<g transform="translate(295 290) rotate(-14)"><ellipse cx="0" cy="0" rx="46" ry="11" fill="#fff" stroke="#2A1D47" stroke-width="5"/>'
          '<path d="M0 -4 V-90" stroke="#2A1D47" stroke-width="6"/><path d="M-30 -230 Q-34 -110 0 -92 Q34 -110 30 -230Z" fill="#FFC94D" stroke="#2A1D47" stroke-width="5"/></g>'
          '<path d="M200 20 v-18 M178 30 l-14 -12 M222 30 l14 -12" stroke="#FF8A3D" stroke-width="7" stroke-linecap="round"/></svg>')


def toast_cover():
    b = sticky_list("Best friend's<br>wedding.<br>No toast yet.",
                    ["give AI 3 real stories", "ask for a 1-minute toast", "pause where it says"],
                    "real Claude reply inside · Part 1 of 2", items_top=442, extra=FLUTES)
    b += K.stamp(HB, 800, 1440, size=150, rot=-10)
    return C.page("#C9CAF5", b)


def cue_cover():
    """Compare (original simple template family, style 8, QUIET): one page to memorize vs a 5-line cue card."""
    f = dict(p1="#FFD4BD", p2="#C9CAF5")
    b = K.dual("Toast tonight? / *Can't memorize it?*", f, cls="S fit",
               style=f"position:absolute;left:90px;width:900px;top:330px;white-space:nowrap;font-size:120px;color:{INK}")
    scrib = "".join(f'<div style="height:12px;border-radius:6px;background:#C7C3E0;margin:0 0 20px;width:{70 + (i * 37) % 30}%"></div>' for i in range(14))
    b += (f'<div style="position:absolute;left:90px;top:690px;width:400px;height:620px;background:#FFFFFF;border:4px solid {INK};border-radius:14px;'
          f'transform:rotate(-3deg);padding:30px 30px;box-sizing:border-box">'
          f'<div style="font-family:\'Caveat Brush\';font-size:54px;color:{ACC};margin-bottom:16px">1 page to learn</div>{scrib}</div>')
    cues = ["1. Intro", "2. Fire alarm", "3. She shows up", "4. Scrabble", "5. Raise glasses"]
    rows = "".join(f'<div style="font-family:Caveat;font-weight:700;font-size:56px;line-height:76px;border-bottom:3px solid #C7D2F2;color:#3B34A0">{c}</div>' for c in cues)
    b += (f'<div style="position:absolute;left:530px;top:740px;width:460px;height:560px;background:#FFFFFF;border:4px solid {INK};border-radius:14px;'
          f'transform:rotate(2deg);padding:26px 30px;box-sizing:border-box;box-shadow:0 14px 0 {INK}">'
          f'<div style="font-family:\'Caveat Brush\';font-size:54px;color:#5E54C9;border-bottom:3px solid #E86A6A;padding-bottom:6px">5 cues to glance at</div>{rows}</div>')
    b += (f'<div style="position:absolute;left:470px;top:960px;font:800 90px Inter;color:{ACC}">→</div>')
    b += f'<div class="hand" style="position:absolute;left:90px;right:90px;top:1330px;font-size:58px;transform:rotate(-2deg)">Claude\'s real cue card, shortened · Part 2</div>'
    b += K.stamp(HB, 60, 1440, size=140, rot=-10)
    return C.page("#FFF5EA", b)


def tidy_cover():
    """Kinetic big text (style 5, LOUD): stacked giant serif, one pill, a drawn kitchen timer, Caveat line, stamp."""
    f = dict(p1="#FFC94D", p2="#FFD4BD")
    b = K.dual("Guests in / *30 minutes?*", f, cls="S fit",
               style=f"position:absolute;left:90px;width:900px;top:330px;white-space:nowrap;font-size:190px;line-height:1.08;color:{INK}")
    b += (f'<div style="position:absolute;left:240px;top:820px;width:600px;height:300px;background:#FFF8EF;border:7px solid {INK};border-radius:60px;'
          f'box-shadow:0 18px 0 {INK};transform:rotate(-3deg);display:flex;align-items:center;justify-content:center;font:700 200px Poppins;color:{INK}">30:00</div>')
    b += (f'<svg style="position:absolute;left:180px;top:770px" width="720" height="90" viewBox="0 0 720 90">'
          f'<path d="M40 70 L10 40 M680 70 L710 40 M120 40 L100 6 M600 40 L620 6" stroke="{ACC}" stroke-width="10" stroke-linecap="round"/></svg>')
    b += f'<div class="hand" style="position:absolute;left:90px;right:90px;top:1190px;font-size:70px;transform:rotate(-2deg)">ask AI what to clean first</div>'
    b += ('<svg style="position:absolute;left:150px;top:1290px" width="300" height="230" viewBox="-150 -130 300 230">'
          '<path d="M-60 -40 L-20 -98 L10 -60 Z" fill="#FF8A3D" stroke="#2A1D47" stroke-width="6" stroke-linejoin="round"/>'
          '<path d="M0 -50 Q30 -120 70 -70 L50 -40Z" fill="#FFFFFF" stroke="#2A1D47" stroke-width="6" stroke-linejoin="round"/>'
          '<path d="M-110 -50 H110 L88 80 H-88Z" fill="#E7B877" stroke="#2A1D47" stroke-width="7" stroke-linejoin="round"/>'
          '<path d="M-102 -6 H102 M-96 36 H96 M-50 -50 L-44 80 M0 -50 V80 M50 -50 L44 80" stroke="#B9874A" stroke-width="5"/>'
          '<path d="M-110 -50 H110" stroke="#2A1D47" stroke-width="7"/></svg>')
    b += K.stamp(HB, 800, 1300, size=140, rot=-10)
    return C.page("#C9CAF5", b)


def build(key):
    C.OUT.mkdir(parents=True, exist_ok=True)
    if key == "toast":
        return C.shot(toast_cover(), C.OUT / "hb-reel-1101-wedding-toast-cover.jpg")
    if key == "cue":
        return C.shot(cue_cover(), C.OUT / "hb-reel-1102-toast-cue-card-cover.jpg")
    if key == "tidy":
        return C.shot(tidy_cover(), C.OUT / "hb-reel-1103-guests-30-min-cover.jpg")


if __name__ == "__main__":
    for k in sys.argv[1:]:
        print(build(k))

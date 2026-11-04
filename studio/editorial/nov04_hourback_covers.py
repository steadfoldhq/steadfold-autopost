#!/usr/bin/env python3
"""Dedicated Reel covers for the Nov 4 Hourback build (never a raw frame). 1080x1920, 2x then Lanczos down.
Reuses oct28_hourback_covers.page()/shot() by import (paths re-pointed); edits nothing shared.

nonna  -> 'Instead of… Write…' reframe (style 7, QUIET). Grid: after Sat 7 pm dinners (follow the line, loud), before
          Mon 5:45 pm Day 14 (series Look B, loud). 'Write…' = Claude's real first line, word for word.
retire -> original simple template 'big number' (style 8, QUIET): a giant '2:00' with the hook and Claude's real closing
          toast line. Grid: after Mon 5:45 pm Day 14 (Look B, loud).
All text inside x 90-990, y 300-1400; hooks >= 120 px.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True
import oct28_hourback_covers as C  # noqa: E402
import edkit as K  # noqa: E402

C.OUT = Path("/home/claude/steadfold-autopost/media/studio-nov04/hourback")
C.SCR = Path("/tmp/claude-0/nov04-hourback")
HB, INK, ACC = C.HB, C.INK, C.ACC


def nonna_cover():
    f = dict(p1="#FFD4BD", p2="#C9CAF5")
    b = K.dual("Nonna turns 90. / *In Italian?*", f, cls="S fit",
               style=f"position:absolute;left:90px;width:900px;top:320px;white-space:nowrap;font-size:140px;color:{INK}")
    b += (f'<div style="position:absolute;left:90px;right:90px;top:690px;background:#FFE6D3;border:4px solid {INK};border-radius:36px;padding:30px 46px 36px;transform:rotate(-1.5deg)">'
          f'<div style="font-family:\'Caveat Brush\';font-size:70px;color:{ACC};line-height:1">Instead of…</div>'
          f'<div style="font-family:\'Instrument Serif\';font-size:104px;line-height:1;color:{INK};margin-top:10px;text-decoration:line-through;text-decoration-thickness:7px;text-decoration-color:{ACC};opacity:.8">Happy birthday!</div></div>')
    b += (f'<div style="position:absolute;left:90px;right:90px;top:975px;background:#FFFFFF;border:4px solid {INK};border-radius:36px;padding:30px 46px 34px;box-shadow:0 14px 0 {INK};transform:rotate(1deg)">'
          f'<div style="font-family:\'Caveat Brush\';font-size:66px;color:{ACC};line-height:1">Write, in her language:</div>'
          f'<div style="font-family:\'Instrument Serif\';font-size:80px;line-height:1.05;color:{INK};margin-top:14px">“Tanti auguri per i tuoi 90 anni, cara Nonna!”</div>'
          f'<div style="font-family:\'Caveat Brush\';font-size:44px;color:#5E54C9;margin-top:14px;text-align:right">Claude\'s real line, word for word</div></div>')
    b += K.stamp(HB, 800, 1470, size=140, rot=-10)
    return C.page("#FFF5EA", b)


def retire_cover():
    f = dict(p1="#FFC94D", p2="#FFD4BD")
    b = K.dual("31 years. / *You get 2 minutes.*", f, cls="S fit",
               style=f"position:absolute;left:90px;width:900px;top:320px;white-space:nowrap;font-size:132px;color:{INK}")
    b += (f'<div style="position:absolute;left:90px;right:90px;top:640px;text-align:center;font:700 400px/1 Poppins;color:#5E54C9;'
          f'letter-spacing:-.02em;text-shadow:0 14px 0 rgba(42,29,71,.16)">2:00</div>')
    b += (f'<div style="position:absolute;left:90px;right:90px;top:1080px;background:#FFFFFF;border:4px solid {INK};border-radius:32px;padding:26px 40px 28px;box-shadow:0 12px 0 {INK};transform:rotate(-1deg)">'
          f'<div style="font-family:\'Caveat Brush\';font-size:56px;color:{ACC};line-height:1">Claude\'s real last line, word for word:</div>'
          f'<div style="font-family:\'Instrument Serif\';font-size:64px;line-height:1.08;color:{INK};margin-top:12px">“To Linda, who knew all our names and made every one of us feel known.”</div></div>')
    b += K.stamp(HB, 820, 1460, size=140, rot=-10)
    return C.page("#C9CAF5", b)


def build(key):
    C.OUT.mkdir(parents=True, exist_ok=True)
    if key == "nonna":
        return C.shot(nonna_cover(), C.OUT / "hb-reel-1108-nonna-90-cover.jpg")
    if key == "retire":
        return C.shot(retire_cover(), C.OUT / "hb-reel-1109-retirement-speech-cover.jpg")


if __name__ == "__main__":
    for k in sys.argv[1:]:
        print(build(k))

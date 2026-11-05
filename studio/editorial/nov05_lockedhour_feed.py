"""Locked Hour Nov 5 build, part 2: One Word No. 9 "Skip." (Wed Nov 11 17:00), 2 slides, SAME layout as lh-oneword-08
(studio/editorial/nov04_lockedhour_feed.py, itself the nov03/nov01/oct28/oct26 layout). Run: python3 studio/editorial/nov05_lockedhour.py oneword
Research: Gardiner, C., Weakley, J., Burke, L. M., Roach, G. D., Sargent, C., Maniar, N., Huynh, M., Miller, D. J., Townshend, A. &
Halson, S. L. (2025). The effect of alcohol on subsequent sleep in healthy adults: A systematic review and meta-analysis.
Sleep Medicine Reviews, 80, 102030. doi:10.1016/j.smrv.2024.102030."""
import os
import sys
from pathlib import Path

os.environ.setdefault("LH_SCR", "/tmp/claude-0/nov05-lockedhour")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from oct26_lockedhour import *  # noqa: F401,F403,E402
import oct25_lockedhour as o25  # noqa: E402
import oct26_lockedhour_feed as f26  # noqa: E402

frame = f26.frame
FW, FH = 1080, 1350
OUT = Path("/home/claude/steadfold-autopost/media/studio-nov05/lockedhour")
YEL = "#FFD43B"


def glass():
    """The one object (same slot and size as No. 8's alarm clock): a drawn wine glass, pink wine, a small crescent moon tag
    on the stem ('before bed'), ink outline + hard offset shadow; no extra props."""
    bowl = "M96 40 H296 Q300 210 196 250 Q92 210 96 40Z"
    wine = "M104 130 H288 Q280 222 196 246 Q112 222 104 130Z"
    g = (f"<g transform='translate(12 12)'><path d='{bowl}' fill='{INK}'/><rect x='186' y='248' width='20' height='120' fill='{INK}'/>"
         f"<ellipse cx='196' cy='376' rx='92' ry='22' fill='{INK}'/></g>"
         f"<path d='{bowl}' fill='#FFFDF6' stroke='{INK}' stroke-width='8' stroke-linejoin='round'/>"
         f"<path d='{wine}' fill='{PINK}' stroke='{INK}' stroke-width='6' stroke-linejoin='round'/>"
         f"<path d='M126 70 Q122 120 136 160' stroke='#FFFFFF' stroke-width='12' fill='none' stroke-linecap='round' opacity='.9'/>"
         f"<rect x='186' y='248' width='20' height='120' fill='#FFFDF6' stroke='{INK}' stroke-width='7'/>"
         f"<ellipse cx='196' cy='376' rx='92' ry='22' fill='#FFFDF6' stroke='{INK}' stroke-width='8'/>"
         f"<g transform='translate(250 300) rotate(-12)'><rect x='-6' y='-34' width='96' height='68' rx='12' fill='{YEL}' stroke='{INK}' stroke-width='6'/>"
         f"<path d='M56 -18 A20 20 0 1 0 56 18 A14 14 0 1 1 56 -18Z' fill='{INK}'/><path d='M-6 0 H-40' stroke='{INK}' stroke-width='5'/></g>")
    return (f"<svg style='position:absolute;left:620px;top:850px;overflow:visible;transform:rotate(4deg) scale(.72);transform-origin:0 0' width='400' height='400' viewBox='0 0 400 400'>"
            f"{g}</svg>")


def oneword():
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:30px;padding:12px 20px'>One Word · No. 9</span></div>
<div style='position:absolute;left:70px;right:70px;top:190px'>{dual("2 drinks before bed? / *Less dream sleep.*", style="font-size:112px;text-align:left")}</div>
<div style='position:absolute;left:50px;top:680px;width:470px;height:110px;background:{PINK};opacity:.85;border-radius:56px'></div>
<div class='S riso' style='position:absolute;left:40px;right:40px;top:540px;font-size:300px;text-align:left'>Skip.</div>
{glass()}
<div class='hand' style='position:absolute;left:90px;top:960px;font-size:60px;text-align:left'>no nightcap<br>tonight</div>
<div class='mono' style='position:absolute;left:90px;top:1200px;font-size:40px;opacity:.85'>one word that guards your focus</div>
<style>.pill{{padding-bottom:.16em!important}}</style>
""", "No. 9", "ONE WORD")
    s2 = frame(f"""
<div style='position:absolute;left:0;right:0;top:100px'>{dual("A nightcap costs you / *dream sleep.*", style="font-size:100px;line-height:1.28")}</div>
<div class='S' style='position:absolute;left:90px;right:90px;top:395px;font-size:47px;line-height:1.1'>A review of 27 lab studies: about 2 drinks before bed already cut REM, the sleep stage where most dreams happen. More drinks cut more. Falling asleep faster took about 5 drinks, and by then dream sleep was cut even more.</div>
<div class='card' style='left:110px;right:110px;top:690px;padding:36px 40px'>
 <div class='dothis' style='font-size:76px;text-align:left'>Do this:</div>
 <div class='S' style='font-size:58px;text-align:left;line-height:1.14'>Skip it. <span class='pill' style='background:{F['pink']['p1']}'>Wind down without a drink.</span></div></div>
<div class='hand' style='position:absolute;left:90px;right:90px;top:1010px;font-size:42px;line-height:1.15'>healthy adults in a lab · 1 drink here = 10 g of alcohol,<br>a bit less than a can of beer</div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1150px;font-size:26px;opacity:.85;line-height:1.4'>Gardiner et al. 2025, Sleep Medicine Reviews<br>27 studies; REM sleep cut at about 2 drinks</div>
""", "No. 9", "ONE WORD")
    d = OUT / "lh-oneword-09"; d.mkdir(parents=True, exist_ok=True)
    o25.shoot([page(s, FW, FH, f) for s, f in ((s1, "pink"), (s2, "cream"))], [d / f"0{i+1}.jpg" for i in range(2)], FW, FH)

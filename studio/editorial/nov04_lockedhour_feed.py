"""Locked Hour Nov 4 build, part 2: One Word No. 8 "Same." (Mon Nov 9 17:00), 2 slides, SAME layout as lh-oneword-07
(studio/editorial/nov03_lockedhour_feed.py, itself the nov01/oct28/oct26 layout). Run: python3 studio/editorial/nov04_lockedhour.py oneword
Research: Windred, D. P., Burns, A. C., Lane, J. M., Saxena, R., Rutter, M. K., Cain, S. W. & Phillips, A. J. K. (2024).
Sleep regularity is a stronger predictor of mortality risk than sleep duration: A prospective cohort study. Sleep, 47(1),
zsad253. doi:10.1093/sleep/zsad253."""
import math
import os
import sys
from pathlib import Path

os.environ.setdefault("LH_SCR", "/tmp/claude-0/nov04-lockedhour")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from oct26_lockedhour import *  # noqa: F401,F403,E402
import oct25_lockedhour as o25  # noqa: E402
import oct26_lockedhour_feed as f26  # noqa: E402

frame = f26.frame
FW, FH = 1080, 1350
OUT = Path("/home/claude/steadfold-autopost/media/studio-nov04/lockedhour")
YEL = "#FFD43B"


def alarm():
    """The one object: the LH signature alarm clock (same drawing as No. 7), hands at 7:00, the top bar reads '7 DAYS',
    no extra props (same layout as No. 7)."""
    g = (f"<circle cx='196' cy='226' r='150' fill='{INK}'/>"
         f"<path d='M86 120 l-46 -44 M306 120 l46 -44' stroke='{INK}' stroke-width='14' stroke-linecap='round'/>"
         f"<path d='M40 112 A70 70 0 0 1 120 46 Z' fill='{PINK}' stroke='{INK}' stroke-width='7' stroke-linejoin='round'/>"
         f"<path d='M352 112 A70 70 0 0 0 272 46 Z' fill='{PINK}' stroke='{INK}' stroke-width='7' stroke-linejoin='round'/>"
         f"<rect x='116' y='30' width='160' height='40' rx='14' fill='{PINK}' stroke='{INK}' stroke-width='7'/>"
         f"<circle cx='186' cy='216' r='150' fill='{YEL}' stroke='{INK}' stroke-width='8'/>"
         f"<circle cx='186' cy='216' r='112' fill='#FFFDF6' stroke='{INK}' stroke-width='6'/>")
    for k in range(12):
        a = k * math.pi / 6
        r1, r2 = (92, 106) if k % 3 else (84, 106)
        g += (f"<path d='M{186 + r1 * math.sin(a):.1f} {216 - r1 * math.cos(a):.1f} L{186 + r2 * math.sin(a):.1f} {216 - r2 * math.cos(a):.1f}' "
              f"stroke='{INK}' stroke-width='{7 if k % 3 == 0 else 4}' stroke-linecap='round'/>")
    g += (f"<path d='M186 216 L186 140' stroke='{INK}' stroke-width='9' stroke-linecap='round'/>"           # minute hand at 12
          f"<path d='M186 216 L186 168' stroke='{INK}' stroke-width='11' stroke-linecap='round' transform='rotate(210 186 216)'/>"  # hour hand at 7
          f"<circle cx='186' cy='216' r='10' fill='{INK}'/>"
          f"<path d='M100 352 l-24 36 M272 352 l24 36' stroke='{INK}' stroke-width='12' stroke-linecap='round'/>")
    lab = f"<text x='196' y='22' font-family='Inter' font-weight='900' font-size='26' fill='{INK}' text-anchor='middle'>7 DAYS</text>"
    days = ""
    for i, d in enumerate("MTWTFSS"):
        x = 6 + i * 56
        days += (f"<rect x='{x}' y='420' width='46' height='58' rx='10' fill='{'#FFFDF6' if i < 5 else YEL}' stroke='{INK}' stroke-width='5'/>"
                 f"<text x='{x + 23}' y='462' font-family='Inter' font-weight='900' font-size='30' fill='{INK}' text-anchor='middle'>{d}</text>"
                 f"<path d='M{x + 8} 500 l10 10 l20 -22' stroke='{PINK}' stroke-width='7' fill='none' stroke-linecap='round' stroke-linejoin='round'/>")
    return (f"<svg style='position:absolute;left:620px;top:860px;overflow:visible;transform:rotate(4deg) scale(.72);transform-origin:0 0' width='400' height='400' viewBox='0 0 400 400'>"
            f"{g}{lab}</svg>")


def oneword():
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:30px;padding:12px 20px'>One Word · No. 8</span></div>
<div style='position:absolute;left:70px;right:70px;top:190px'>{dual("Slept in Sunday? / *Same alarm, all 7 days.*", style="font-size:112px;text-align:left")}</div>
<div style='position:absolute;left:50px;top:680px;width:600px;height:110px;background:{PINK};opacity:.85;border-radius:56px'></div>
<div class='S riso' style='position:absolute;left:40px;right:40px;top:540px;font-size:300px;text-align:left'>Same.</div>
{alarm()}
<div class='hand' style='position:absolute;left:90px;top:960px;font-size:60px;text-align:left'>one wake-up time,<br>weekends too</div>
<div class='mono' style='position:absolute;left:90px;top:1200px;font-size:40px;opacity:.85'>one word that guards your focus</div>
<style>.pill{{padding-bottom:.16em!important}}</style>
""", "No. 8", "ONE WORD")
    s2 = frame(f"""
<div style='position:absolute;left:0;right:0;top:100px'>{dual("Steady sleep times / *mattered more than hours.*", style="font-size:100px")}</div>
<div class='S' style='position:absolute;left:90px;right:90px;top:400px;font-size:50px;line-height:1.1'>60,977 adults wore wrist trackers for about a week. Followed for about 6 years, how regular their sleep times were predicted their risk of dying early better than hours slept.</div>
<div class='card' style='left:110px;right:110px;top:650px;padding:36px 40px'>
 <div class='dothis' style='font-size:76px;text-align:left'>Do this:</div>
 <div class='S' style='font-size:58px;text-align:left;line-height:1.14'>Pick one wake-up time. <span class='pill' style='background:{F['pink']['p1']}'>Keep it all 7 days.</span></div></div>
<div class='hand' style='position:absolute;left:90px;right:90px;top:990px;font-size:46px'>a link, not proof · average age 63</div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1090px;font-size:26px;opacity:.85;line-height:1.4'>Windred et al. 2024, Sleep (UK Biobank)<br>60,977 adults; regularity beat sleep length</div>
""", "No. 8", "ONE WORD")
    d = OUT / "lh-oneword-08"; d.mkdir(parents=True, exist_ok=True)
    o25.shoot([page(s, FW, FH, f) for s, f in ((s1, "pink"), (s2, "cream"))], [d / f"0{i+1}.jpg" for i in range(2)], FW, FH)

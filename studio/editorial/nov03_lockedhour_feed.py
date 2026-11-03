"""Locked Hour Nov 3 build, part 2: One Word No. 7 "Snooze." (Fri Nov 6 17:00), 2 slides, same cover layout as
lh-oneword-06 (studio/editorial/nov01_lockedhour_feed.py, itself the oct28/oct26 layout). Desk order Nov 3: feed reach
is 0-1, so 2 slides and minimal hours. Run: python3 studio/editorial/nov03_lockedhour.py oneword
Research: Sundelin, T., Landry, S. & Axelsson, J. (2023). Is snoozing losing? Why intermittent morning alarms are used
and how they affect sleep, cognition, cortisol, and mood. Journal of Sleep Research. doi:10.1111/jsr.14054."""
import os
import sys
from pathlib import Path

os.environ.setdefault("LH_SCR", "/tmp/claude-0/nov03-lockedhour")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from oct26_lockedhour import *  # noqa: F401,F403,E402
import oct25_lockedhour as o25  # noqa: E402
import oct26_lockedhour_feed as f26  # noqa: E402

frame = f26.frame
FW, FH = 1080, 1350
OUT = Path("/home/claude/steadfold-autopost/media/studio-nov03/lockedhour")
YEL = "#FFD43B"


def alarm():
    """The one object: the LH signature alarm clock, drawn (ink lines, butter body, pink bells, hard offset shadow),
    hands at 6:30, a big pink SNOOZE bar on top being pressed, three drawn z's."""
    g = (f"<circle cx='196' cy='226' r='150' fill='{INK}'/>"
         f"<path d='M86 120 l-46 -44 M306 120 l46 -44' stroke='{INK}' stroke-width='14' stroke-linecap='round'/>"
         f"<path d='M40 112 A70 70 0 0 1 120 46 Z' fill='{PINK}' stroke='{INK}' stroke-width='7' stroke-linejoin='round'/>"
         f"<path d='M352 112 A70 70 0 0 0 272 46 Z' fill='{PINK}' stroke='{INK}' stroke-width='7' stroke-linejoin='round'/>"
         f"<rect x='126' y='30' width='140' height='40' rx='14' fill='{PINK}' stroke='{INK}' stroke-width='7'/>"
         f"<circle cx='186' cy='216' r='150' fill='{YEL}' stroke='{INK}' stroke-width='8'/>"
         f"<circle cx='186' cy='216' r='112' fill='#FFFDF6' stroke='{INK}' stroke-width='6'/>")
    for k in range(12):
        import math
        a = k * math.pi / 6
        r1, r2 = (92, 106) if k % 3 else (84, 106)
        g += (f"<path d='M{186 + r1 * math.sin(a):.1f} {216 - r1 * math.cos(a):.1f} L{186 + r2 * math.sin(a):.1f} {216 - r2 * math.cos(a):.1f}' "
              f"stroke='{INK}' stroke-width='{7 if k % 3 == 0 else 4}' stroke-linecap='round'/>")
    g += (f"<path d='M186 216 L186 140' stroke='{INK}' stroke-width='9' stroke-linecap='round' transform='rotate(180 186 216)'/>"
          f"<path d='M186 216 L186 168' stroke='{INK}' stroke-width='11' stroke-linecap='round' transform='rotate(195 186 216)'/>"
          f"<circle cx='186' cy='216' r='10' fill='{INK}'/>"
          f"<path d='M100 352 l-24 36 M272 352 l24 36' stroke='{INK}' stroke-width='12' stroke-linecap='round'/>")
    zz = "".join(f"<text x='{x}' y='{y}' font-family='Inter Display' font-weight='900' font-size='{fs}' fill='{INK}' transform='rotate(-10 {x} {y})'>z</text>"
                 for x, y, fs in ((360, 70, 70), (410, 10, 56), (450, -40, 44)))
    lab = (f"<text x='196' y='22' font-family='Inter' font-weight='900' font-size='26' fill='{INK}' text-anchor='middle'>SNOOZE</text>")
    return (f"<svg style='position:absolute;left:620px;top:885px;overflow:visible;transform:rotate(5deg) scale(.72);transform-origin:0 0' width='400' height='400' viewBox='0 0 400 400'>"
            f"{g}{lab}{zz}</svg>")


def oneword():
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:30px;padding:12px 20px'>One Word · No. 7</span></div>
<div style='position:absolute;left:70px;right:70px;top:190px'>{dual("Hit snooze again? / *30 minutes is okay.*", style="font-size:118px;text-align:left")}</div>
<div style='position:absolute;left:60px;top:760px;width:960px;height:120px;background:{PINK};opacity:.85;border-radius:60px'></div>
<div class='S riso' style='position:absolute;left:40px;right:40px;top:540px;font-size:300px;text-align:left'>Snooze.</div>
{alarm()}
<div class='hand' style='position:absolute;left:90px;top:960px;font-size:60px;text-align:left'>up to 30 minutes,<br>then really get up</div>
<div class='mono' style='position:absolute;left:90px;top:1200px;font-size:40px;opacity:.85'>one word that guards your focus</div>
<style>.pill{{padding-bottom:.16em!important}}</style>
""", "No. 7", "ONE WORD")
    s2 = frame(f"""
<div style='position:absolute;left:0;right:0;top:100px'>{dual("Snoozing cost only / *about 6 minutes of sleep.*", style="font-size:100px")}</div>
<div class='S' style='position:absolute;left:90px;right:90px;top:400px;font-size:50px;line-height:1.1'>31 regular snoozers slept in a sleep lab. After 30 minutes of snoozing, they did as well or a bit better on tests right after waking than when the first alarm got them up.</div>
<div class='card' style='left:110px;right:110px;top:650px;padding:36px 40px'>
 <div class='dothis' style='font-size:76px;text-align:left'>Do this:</div>
 <div class='S' style='font-size:58px;text-align:left;line-height:1.14'>Snoozing anyway? <span class='pill' style='background:{F['pink']['p1']}'>Stop at 30 minutes, then get up.</span></div></div>
<div class='hand' style='position:absolute;left:90px;right:90px;top:990px;font-size:46px'>tested on regular snoozers · one small lab study</div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1090px;font-size:26px;opacity:.85;line-height:1.4'>Sundelin, Landry &amp; Axelsson 2023, J Sleep Research<br>31 regular snoozers; about 6 minutes of sleep lost</div>
""", "No. 7", "ONE WORD")
    d = OUT / "lh-oneword-07"; d.mkdir(parents=True, exist_ok=True)
    o25.shoot([page(s, FW, FH, f) for s, f in ((s1, "pink"), (s2, "cream"))], [d / f"0{i+1}.jpg" for i in range(2)], FW, FH)

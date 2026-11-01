"""Locked Hour Nov 1 build, part 2: One Word No. 6 "Doodle." (Wed Nov 4 17:00), same layout as lh-oneword-05
(studio/editorial/oct28_lockedhour_feed.py, itself the oct26 layout). Run: python3 studio/editorial/nov01_lockedhour.py oneword
Research: Andrade, J. (2010). What does doodling do? Applied Cognitive Psychology, 24(1), 100-106. doi:10.1002/acp.1561."""
import os
import sys
from pathlib import Path

os.environ.setdefault("LH_SCR", "/tmp/claude-0/nov01-lockedhour")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from oct26_lockedhour import *  # noqa: F401,F403,E402
import oct25_lockedhour as o25  # noqa: E402
import oct26_lockedhour_feed as f26  # noqa: E402

frame = f26.frame
FW, FH = 1080, 1350
OUT = Path("/home/claude/steadfold-autopost/media/studio-nov01/lockedhour")
YEL = "#FFD43B"


def doodles():
    """The one object: a page corner of drawn doodles like the study's task (shaded squares and circles), ink lines,
    pink/yellow fills, hatch shading, hard offset shadow, plus a pencil."""
    hatch = "".join(f"<path d='M{x} 0 L{x-40} 40' stroke='{INK}' stroke-width='4'/>" for x in range(0, 120, 12))
    g = (f"<defs><clipPath id='sq'><rect x='0' y='0' width='80' height='80'/></clipPath><clipPath id='ci'><circle cx='40' cy='40' r='40'/></clipPath></defs>")
    g += (f"<rect x='14' y='14' width='360' height='400' rx='14' fill='{INK}'/>"
          f"<rect x='0' y='0' width='360' height='400' rx='14' fill='#FFFDF6' stroke='{INK}' stroke-width='6'/>")
    shapes = [("sq", 40, 40, YEL, 1), ("ci", 140, 40, PINK, 1), ("sq", 240, 40, "#FFFDF6", 1),
              ("ci", 40, 150, "#FFFDF6", 1), ("sq", 140, 150, PINK, 1), ("ci", 240, 150, YEL, 0.6),
              ("sq", 40, 260, PINK, 0.4), ("ci", 140, 260, "#FFFDF6", 0)]
    for kind, x, y, col, shade in shapes:
        body = (f"<rect x='0' y='0' width='80' height='80' fill='{col}'/>" if kind == "sq" else f"<circle cx='40' cy='40' r='40' fill='{col}'/>")
        lines = "".join(f"<path d='M{a} -10 L{a-90} 90' stroke='{INK}' stroke-width='4'/>" for a in range(10, int(10 + 170 * shade), 13)) if shade else ""
        edge = (f"<rect x='0' y='0' width='80' height='80' fill='none' stroke='{INK}' stroke-width='5'/>" if kind == "sq"
                else f"<circle cx='40' cy='40' r='40' fill='none' stroke='{INK}' stroke-width='5'/>")
        g += f"<g transform='translate({x} {y})'>{body}<g clip-path='url(#{kind})'>{lines}</g>{edge}</g>"
    pencil = (f"<g transform='translate(300 330) rotate(35)'><rect x='-14' y='-190' width='28' height='170' rx='6' fill='{YEL}' stroke='{INK}' stroke-width='5'/>"
              f"<rect x='-14' y='-206' width='28' height='22' rx='6' fill='{PINK}' stroke='{INK}' stroke-width='5'/>"
              f"<path d='M-14 -20 L0 18 L14 -20Z' fill='#FFE7C2' stroke='{INK}' stroke-width='5' stroke-linejoin='round'/><path d='M-4 6 L0 18 L4 6Z' fill='{INK}'/></g>")
    return (f"<svg style='position:absolute;left:600px;top:830px;overflow:visible;transform:rotate(4deg) scale(.85);transform-origin:0 0' width='380' height='420' viewBox='0 0 380 420'>"
            f"{g}{pencil}</svg>")


def bars():
    """Average details recalled in the surprise test: 5.8 (just listened) vs 7.5 (shaded shapes). Bars to scale (max 8)."""
    def row(lab, v, col):
        w = int(600 * v / 8)
        return (f"<div style='margin-bottom:46px'><div class='S' style='font-size:50px;text-align:left;margin-bottom:12px'>{lab}</div>"
                f"<div style='position:relative;width:640px;height:96px;border:6px solid {INK};border-radius:24px;background:#FFFDF6;box-shadow:10px 10px 0 {INK}'>"
                f"<div style='position:absolute;left:8px;top:8px;bottom:8px;width:{w}px;border-radius:16px;background:{col}'></div>"
                f"<div style='position:absolute;right:-180px;top:0;font:900 80px/96px Inter Display,Inter;color:{INK}'>{v}</div></div></div>")
    return row("Just listened", 5.8, "#E6DCCB") + row("Filled in shapes while listening", 7.5, PINK)


def oneword():
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:30px;padding:12px 20px'>One Word · No. 6</span></div>
<div style='position:absolute;left:70px;right:70px;top:190px'>{dual("Boring call? / *Grab a pen.*", style="font-size:124px;text-align:left")}</div>
<div style='position:absolute;left:60px;top:760px;width:960px;height:120px;background:{PINK};opacity:.85;border-radius:60px'></div>
<div class='S riso' style='position:absolute;left:40px;right:40px;top:540px;font-size:300px;text-align:left'>Doodle.</div>
{doodles()}
<div class='hand' style='position:absolute;left:90px;top:960px;font-size:60px;text-align:left'>fill in simple shapes<br>while you listen</div>
<div class='mono' style='position:absolute;left:90px;top:1200px;font-size:40px;opacity:.85'>one word that guards your focus</div>
<style>.pill{{padding-bottom:.16em!important}}</style>
""", "No. 6", "ONE WORD")
    s2 = frame(f"""
<div style='position:absolute;left:0;right:0;top:110px'>{dual("Doodlers remembered / *29% more.*", style="font-size:104px")}</div>
<div style='position:absolute;left:120px;top:440px'>{bars()}</div>
<div class='hand' style='position:absolute;left:0;right:0;top:1060px;font-size:52px'>details remembered, on average,<br>from a dull phone message</div>
""", "No. 6", "ONE WORD")
    s3 = frame(f"""
<div style='position:absolute;left:0;right:0;top:120px'>{dual("*Ears on, pen moving.*", style="font-size:130px")}</div>
<div class='S' style='position:absolute;left:90px;right:90px;top:320px;font-size:54px;line-height:1.06'>40 people heard a dull 2.5-minute phone message. The half who filled in shapes while listening caught more and remembered more in a surprise test.</div>
<div class='card' style='left:110px;right:110px;top:650px;padding:36px 40px'>
 <div class='dothis' style='font-size:76px;text-align:left'>Do this:</div>
 <div class='S' style='font-size:58px;text-align:left;line-height:1.14'>Long call or lecture? Keep a pen and paper. <span class='pill' style='background:{F['pink']['p1']}'>Fill in simple shapes while you listen.</span></div></div>
<div class='hand' style='position:absolute;left:90px;right:90px;top:1040px;font-size:46px'>simple shapes, not art · one small study</div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1130px;font-size:26px;opacity:.85;line-height:1.4'>Andrade 2010, Applied Cognitive Psychology 24(1)<br>40 people; recalled 7.5 vs 5.8 details on average</div>
""", "No. 6", "ONE WORD")
    d = OUT / "lh-oneword-06"; d.mkdir(parents=True, exist_ok=True)
    o25.shoot([page(s, FW, FH, f) for s, f in ((s1, "pink"), (s2, "cream"), (s3, "dots"))], [d / f"0{i+1}.jpg" for i in range(3)], FW, FH)

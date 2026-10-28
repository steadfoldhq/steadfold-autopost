"""Locked Hour Oct 28 build, part 2: One Word No. 5 "Walk." (Mon Nov 2 17:00), same layout as lh-oneword-04
(studio/editorial/oct26_lockedhour_feed.py oneword()). Run: python3 studio/editorial/oct28_lockedhour.py oneword
Research: Oppezzo & Schwartz 2014, JEP: Learning, Memory, and Cognition 40(4):1142-1152 (doi 10.1037/a0036577)."""
import os
import sys
from pathlib import Path

os.environ.setdefault("LH_SCR", "/tmp/claude-0/oct28-lockedhour")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from oct26_lockedhour import *  # noqa: F401,F403,E402
import oct25_lockedhour as o25  # noqa: E402
import oct26_lockedhour_feed as f26  # noqa: E402

frame = f26.frame
FW, FH = 1080, 1350
OUT = Path("/home/claude/steadfold-autopost/media/studio-oct28/lockedhour")


def dots100(n_on=81):
    """10x10 dot grid, the first n_on filled pink: 81 of 100 people had more ideas walking (Experiment 1)."""
    s = ""
    for i in range(100):
        r, c = divmod(i, 10)
        on = i < n_on
        s += (f"<div style='position:absolute;left:{c*62}px;top:{r*44}px;width:34px;height:34px;border-radius:50%;"
              f"border:4px solid {INK};background:{PINK if on else '#FFFDF6'};opacity:{1 if on else .6}'></div>")
    return f"<div style='position:relative;width:600px;height:440px'>{s}</div>"


def steps():
    """Drawn zine footprints walking up and to the right (ink line, pink fill, hard offset shadow): the one object."""
    sole = "M0 -48 C26 -48 34 -18 30 10 C26 34 14 46 0 46 C-16 46 -26 30 -28 6 C-30 -22 -22 -48 0 -48 Z"
    heel = "M-2 58 C16 58 24 70 22 86 C20 102 8 108 -4 106 C-18 104 -24 92 -22 78 C-20 66 -12 58 -2 58 Z"
    toes = "".join(f"<circle cx='{cx}' cy='{cy}' r='{r}'/>" for cx, cy, r in [(-20, -66, 11), (0, -74, 10), (18, -70, 8.5), (31, -60, 7), (38, -46, 6)])
    g = ""
    for k, (x, y, r) in enumerate([(40, 330, -14), (150, 250, 8), (215, 120, -14), (325, 40, 8)]):
        foot = f"<path d='{sole}' /><path d='{heel}' />{toes}"
        g += (f"<g transform='translate({x+9} {y+9}) rotate({r})' fill='{INK}'>{foot}</g>"
              f"<g transform='translate({x} {y}) rotate({r})' fill='{PINK if k % 2 else '#FFD43B'}' stroke='{INK}' stroke-width='6'>{foot}</g>")
    return f"<svg style='position:absolute;left:640px;top:770px;overflow:visible' width='380' height='460' viewBox='0 0 380 460'>{g}</svg>"


def oneword():
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:30px;padding:12px 20px'>One Word · No. 5</span></div>
<div style='position:absolute;left:70px;right:70px;top:190px'>{dual("Blank page? / *Stand up.*", style="font-size:124px;text-align:left")}</div>
<div style='position:absolute;left:60px;top:760px;width:960px;height:120px;background:{PINK};opacity:.85;border-radius:60px'></div>
<div class='S riso' style='position:absolute;left:40px;right:40px;top:540px;font-size:340px;text-align:left'>Walk.</div>
{steps()}
<div class='hand' style='position:absolute;left:90px;top:960px;font-size:60px;text-align:left'>even indoors,<br>even facing a wall</div>
<div class='mono' style='position:absolute;left:90px;top:1150px;font-size:24px;opacity:.8'>one word that guards your focus</div>
""", "No. 5", "ONE WORD")
    s2 = frame(f"""
<div style='position:absolute;left:0;right:0;top:110px'>{dual("*81% of people* / had more ideas walking.", style="font-size:100px")}</div>
<div style='position:absolute;left:250px;top:430px'>{dots100(81)}</div>
<div class='S' style='position:absolute;left:90px;right:90px;top:920px;font-size:56px;line-height:1.08'>Same idea task, done sitting, then <span class='pill' style='background:{F['cream']['p1']}'>walking on a treadmill facing a blank wall.</span></div>
<div class='hand' style='position:absolute;left:0;right:0;top:1110px;font-size:50px'>in one experiment: pink = more ideas walking</div>
""", "No. 5", "ONE WORD")
    s3 = frame(f"""
<div style='position:absolute;left:0;right:0;top:120px'>{dual("*More new ideas.*", style="font-size:150px")}</div>
<div class='S' style='position:absolute;left:90px;right:90px;top:330px;font-size:58px;line-height:1.05'>In 4 experiments, people thought up more new ideas walking than sitting. It still helped a bit after they sat back down.</div>
<div class='card' style='left:110px;right:110px;top:640px;padding:36px 40px'>
 <div class='dothis' style='font-size:76px;text-align:left'>Do this:</div>
 <div class='S' style='font-size:58px;text-align:left;line-height:1.02'>Stuck for ideas? Get up and walk, even around the room. <span class='pill' style='background:{F['pink']['p1']}'>Say every idea into a voice memo.</span></div></div>
<div class='hand' style='position:absolute;left:90px;right:90px;top:1040px;font-size:46px'>for brainstorming, not for one-right-answer problems</div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1130px;font-size:22px;opacity:.85;line-height:1.45'>Oppezzo &amp; Schwartz 2014, Journal of Experimental Psychology:<br>Learning, Memory, and Cognition (4 experiments, 176 people)</div>
""", "No. 5", "ONE WORD")
    d = OUT / "lh-oneword-05"; d.mkdir(parents=True, exist_ok=True)
    o25.shoot([page(s, FW, FH, f) for s, f in ((s1, "pink"), (s2, "cream"), (s3, "dots"))], [d / f"0{i+1}.jpg" for i in range(3)], FW, FH)

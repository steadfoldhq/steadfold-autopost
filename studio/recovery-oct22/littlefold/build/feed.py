#!/usr/bin/env python3
"""Littlefold recovery feed tiles + Story hand-offs (Oct 22). Output: media/recovery-oct22/littlefold/."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lfnl import *  # noqa

OUT = REPO / "media" / "recovery-oct22" / "littlefold"
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1080, 1350


def chip(text, x, y, col=CREAM, size=26):
    return f'<div class="chip" style="left:{x}px;top:{y}px;color:{col};font-size:{size}px">{text}</div>'


def kick(text, y, col=CREAM, size=26):
    return f'<div class="kick" style="top:{y}px;color:{col};font-size:{size}px">{text}</div>'


def num(t, col=CREAM):
    return f'<div class="pop" style="position:absolute;right:70px;top:70px;font-size:24px;color:{col};opacity:.8">{t}</div>'


def handle(col=CREAM, y=1268):
    return f'<div class="pop" style="position:absolute;left:70px;top:{y}px;font-size:24px;color:{col};opacity:.85">@littlefoldhq</div>'


def paw(x, y, s=1, rot=0, col="#FFBFD3"):
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{70*s:.0f}px;height:{70*s:.0f}px;transform:rotate({rot}deg)" viewBox="0 0 70 70">'
            f'<ellipse cx="35" cy="46" rx="16" ry="13" fill="{col}"/>'
            + "".join(f'<ellipse cx="{cx}" cy="{cy}" rx="7" ry="9" fill="{col}"/>' for cx, cy in [(14, 26), (27, 16), (43, 16), (56, 26)])
            + '</svg>')


# ---------- 1. Crying has a peak: 3-slide carousel (replaces lf-1025-follow-crying) ----------
def crying_s1():
    body = (night_bg(W, H, cy=.40, r=.47) + kick("NIGHT LIGHT · THE NEWBORN WEEKS", 92) + num("1/3")
            + K.dual("The crying / has a *peak.*", F, cls="S fit", style=f"position:absolute;left:110px;width:860px;top:330px;font-size:132px;color:{INK}")
            + f'<div class="lora" style="position:absolute;left:150px;width:780px;top:640px;font-size:42px;line-height:1.22;text-align:center;color:{INK}">'
              'Often somewhere around 3 to 12 weeks. Usually over by 3 to 4 months.</div>'
            + lamp(770, 770, .9)
            + f'<div class="hand" style="position:absolute;left:110px;width:860px;top:1060px;font-size:58px;transform:rotate(-2deg);color:#FFBFD3">send this to someone in week 3</div>'
            + chip("CPS · Colic and crying", 70, 1185) + handle() + K.stamp(B, 868, 1150, size=150, rot=-10))
    return render(page(W, H, body), OUT / "crying-peak-01.jpg", W, H)


def crying_s2():
    items = [("Check first:", "hungry, wet diaper, too hot or cold, fever."),
             ("Hold them.", "You can't spoil a baby by picking them up."),
             ("Calm it down:", "dim the lights, shush, sway, or walk them close to you.")]
    rows = "".join(
        f'<div style="display:flex;gap:26px;align-items:flex-start;margin:0 0 34px">'
        f'<div style="flex:none;width:62px;height:62px;border-radius:50%;background:{DEEP};color:{CREAM};font-family:Fraunces;font-weight:700;font-size:34px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
        f'<div style="font-family:Poppins;font-size:36px;line-height:1.3;color:{INK}"><b style="font-family:Lora;font-style:italic;font-size:42px">{a}</b> {b}</div></div>'
        for i, (a, b) in enumerate(items))
    body = (night_bg(W, H, cy=.24, r=.40) + kick("WHAT HELPS, IN ORDER", 92, col=DEEP) + num("2/3")
            + K.dual("Check first. / Then *hold close.*", F, cls="S fit", style=f"position:absolute;left:150px;width:780px;top:205px;font-size:104px;color:{INK}")
            + f'<div style="position:absolute;left:80px;right:80px;top:600px;background:{CREAM};border-radius:34px;padding:52px 50px 22px;box-shadow:0 26px 40px rgba(0,0,0,.25)">{rows}</div>'
            + chip("CPS · Colic and crying", 70, 1185) + handle() + K.stamp(B, 868, 1150, size=150, rot=-10))
    return render(page(W, H, body), OUT / "crying-peak-02.jpg", W, H)


def crying_s3():
    body = (night_bg(W, H, cy=.30, r=.52, day=True) + kick("DO THIS", 92, col=DEEP) + num("3/3", INK)
            + K.dual("Next cry: / *check first,* / then hold close.", F, cls="S fit", style=f"position:absolute;left:110px;width:860px;top:190px;font-size:116px;color:{INK}")
            + f'<div style="position:absolute;left:90px;right:90px;top:690px;border:3px solid {DEEP};border-radius:30px;padding:34px 40px;background:rgba(255,248,238,.92)">'
              f'<div style="font-family:Poppins;font-size:34px;line-height:1.35;color:{INK}"><b>Too much?</b> Put baby in their crib, step out and take a moment. It\'s OK to ask for help.</div>'
              f'<div style="height:2px;background:{P1};margin:24px 0"></div>'
              f'<div style="font-family:Poppins;font-size:34px;line-height:1.35;color:{INK}"><b>Under 3 months with a fever?</b> Get care right away.</div></div>'
            + K.save_line("save this for 3 am", 110, 1090, 860, size=60, rot=-2, brand=B)
            + chip("CPS · Colic and crying", 70, 1185, col=DEEP) + handle(INK) + K.stamp(B, 868, 1150, size=150, rot=-10))
    return render(page(W, H, body), OUT / "crying-peak-03.jpg", W, H)


# ---------- 2. Vitamin D 400 IU single (replaces lf-1025-hold-million-words) ----------
def vitd():
    body = (night_bg(W, H, cy=.36, r=.46, day=True) + kick("ONE NUMBER · VITAMIN D", 92, col=DEEP)
            + drop(410, 175, 260)
            + K.dual("Breastfed babies: / *400 IU* a day.", F, cls="S fit", style=f"position:absolute;left:110px;width:860px;top:540px;font-size:118px;color:{INK}")
            + f'<div class="lora" style="position:absolute;left:150px;width:780px;top:820px;font-size:40px;line-height:1.25;text-align:center;color:{INK}">'
              'Vitamin D drops, every day from birth, until they get enough from food.</div>'
            + f'<div class="pop" style="position:absolute;left:150px;width:780px;top:960px;font-size:28px;line-height:1.4;text-align:center;color:{INK};opacity:.85">'
              'Formula already has it added. Northern community or other risk factors? Ask about a higher dose.</div>'
            + K.save_line("set a daily reminder ♡", 110, 1080, 860, size=58, rot=-2, brand=B)
            + chip("CPS · Vitamin D", 70, 1185, col=DEEP) + handle(INK) + K.stamp(B, 868, 1150, size=150, rot=-10))
    return render(page(W, H, body), OUT / "vitamin-d-400.jpg", W, H)


# ---------- 3. Small Wins No.2: Showered (replaces lf-1024-roadmap-bedtime) ----------
def small_win():
    body = (night_bg(W, H, cy=.50, r=.44, day=True)
            + f'<div style="position:absolute;left:0;right:0;top:86px;text-align:center"><span style="display:inline-block;background:#FF8A70;color:{CREAM};'
              f'font-family:Poppins;font-weight:600;font-size:30px;letter-spacing:.2em;padding:12px 34px;border-radius:99px">SMALL WINS · No.2</span></div>'
            + K.dual("You *showered* / today.", F, cls="S fit", style=f"position:absolute;left:110px;width:860px;top:190px;font-size:138px;color:{INK}")
            + rosette(320, 470, 440, title="Showered.", icon=SHOWER_ICON)
            + paw(170, 560, 1.3, -20, "#F49AB8") + paw(830, 700, 1.1, 18, "#F49AB8") + paw(210, 860, .9, 12, "#F7C35A")
            + f'<div class="lora" style="position:absolute;left:150px;width:780px;top:1105px;font-size:38px;line-height:1.25;text-align:center;color:{INK}">'
              'Before noon, even. Nobody claps for this part, so we will.</div>'
            + K.save_line("it counts ♡", 90, 1200, 300, size=58, rot=-4, brand=B)
            + handle(INK) + K.stamp(B, 868, 1150, size=150, rot=-10))
    return render(page(W, H, body), OUT / "small-wins-02-showered.jpg", W, H)


# ---------- Story hand-offs (1080x1920, text inside y 250-1650) ----------
SW, SH = 1080, 1920


def story_card(img, x, y, w, rot):
    return (f'<img src="{Path(img).as_uri()}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg);'
            f'border-radius:18px;box-shadow:0 30px 50px rgba(0,0,0,.28),0 0 0 8px {CREAM}">')


def story_resp():
    body = (night_bg(SW, SH, cy=.30, r=.48, day=True)
            + K.save_line("baby money", 0, 280, SW, size=56, rot=0, brand=B)
            + K.dual("Never opened / an *RESP?*", F, cls="S fit", style=f"position:absolute;left:110px;width:860px;top:370px;font-size:130px;color:{INK}")
            + story_card(REPO / "media/lf-1023-resp-catch-up/01.jpg", 270, 700, 540, -4)
            + K.save_line("full breakdown in today's post ↑", 90, 1440, 900, size=64, rot=-2, brand=B)
            + K.stamp(B, 860, 1520, size=150, rot=-10))
    return render(page(SW, SH, body), OUT / "story-lf-ch-1023-4.jpg", SW, SH)


def story_crying():
    body = (night_bg(SW, SH, cy=.30, r=.50)
            + f'<div class="hand" style="position:absolute;left:0;right:0;top:280px;font-size:56px;color:#7A2149">calmer newborn days</div>'
            + K.dual("It has / a *peak.*", F, cls="S fit", style=f"position:absolute;left:160px;width:760px;top:400px;font-size:140px;color:{INK}")
            + story_card(OUT / "crying-peak-01.jpg", 270, 760, 540, 3)
            + f'<div class="hand" style="position:absolute;left:60px;right:60px;top:1480px;font-size:64px;color:#FFBFD3;transform:rotate(-2deg)">full breakdown in today\'s post ↑</div>'
            + K.stamp(B, 860, 1560, size=140, rot=-10))
    return render(page(SW, SH, body), OUT / "story-lf-ch-1025-4.jpg", SW, SH)


if __name__ == "__main__":
    which = sys.argv[1:] or ["all"]
    for fn in [crying_s1, crying_s2, crying_s3, vitd, small_win, story_resp, story_crying]:
        if "all" in which or fn.__name__ in which:
            print(fn())

#!/usr/bin/env python3
"""Oct 18 morning Reels re-cut with the motion kit for READABLE PACING (standard, Oct 16 9:48 am):
the old kinetic versions held 20-45 words for 3.5-4 s. Same message and numbers, fewer words per beat,
and every beat held for at least 0.4 s per word + 0.6 s (enforced in reels_1016am.build).

    python3 studio/motion/reels_1018am.py ff-reel-1018am-lower-rate --out DIR
"""
import argparse
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reels_1016am as AM  # noqa: E402
from kit import BRANDS, Reel, el, emoji, img, scribble_circle, words  # noqa: E402

R = AM.R
FF, LH = BRANDS["fullyfunded"], BRANDS["lockedhour"]
PILL = lambda txt, bg="#2B3FE0", fg="#fff": (f'<span style="font:800 42px/1 Inter;letter-spacing:.12em;color:{fg};background:{bg};'  # noqa: E731
                                             f'padding:16px 26px;border-radius:999px">{txt}</span>')

# Example math (same as the caption): 5,000 kept on a card for a year, monthly compounding, no payments or new spending.
def interest(rate, bal=5000.0):
    return bal * ((1 + rate / 12) ** 12 - 1)


I20, I16 = interest(0.20), interest(0.16)
SAVED = I20 - I16          # ~236
N = lambda x: f"{x:,.0f}"  # noqa: E731


# =============================================================================================== FF 08:15 ask for a lower rate
def ff_lower_rate():
    r = Reel("ff-reel-1018am-lower-rate", "fullyfunded", bpm=95, css=AM.FF_CSS, stage="#2B3FE0")
    coral, soft = FF["acc"], FF["acc2"]
    r.scene(2, "".join([
        '<div class="par cob"></div>', AM.ff_chip(),
        el('One call.<br><span class="emw">One question.</span>', "c", 430, a="none", cls="Hw", style="font-size:150px"),
        emoji("📞", 420, 960, 230, t=0.25, d=0.35, loop="buzz", amp=1.2),
    ]), cam="push", shake=(0.25, 0.2, 14))
    r.scene(1.5, "".join(['<div class="par lite"></div>',
                          words("Your card charges / *20% a year?*", "c", 560, t=0.0, gap=0.1, cls="H", style="font-size:130px")]),
            tin="whipL", cam="push")
    bar = lambda lab, to, val, col, t0: (
        f'<div style="font:700 54px/1.1 Inter;color:#0E1440;margin-bottom:16px">{lab}</div>'
        f'<div class="bar" style="background:rgba(43,63,224,.12)"><div class="f" data-a="bar" data-t="{t0}" data-d="0.8" data-to="{to}" '
        f'style="background:{col}"></div></div><div class="H" style="font-size:120px;margin-top:16px"><span data-a="count" data-t="{t0}" '
        f'data-d="0.8" data-to="{round(val)}" data-comma="1">0</span></div>')
    r.scene(3, "".join(['<div class="par lite"></div>',
                        el(PILL("EXAMPLE · 5,000 FOR A YEAR", "#FF6A3D"), "c", 330, a="stamp", t=0.0, d=0.25, r=-2),
                        el(bar("Interest at 20%", 100, I20, coral, 0.2), 90, 470, 900, a="up", t=0.0),
                        el(bar("Interest at 16%", round(100 * I16 / I20, 1), I16, "#2B3FE0", 0.5), 90, 900, 900, a="up", t=0.3)]),
            tin="slam", cam="rise")
    r.scene(2, "".join(['<div class="par deep"></div>',
                        words("That's about", "c", 420, t=0.0, cls="Hw", style="font-size:110px"),
                        el(f'<span data-a="count" data-t="0.15" data-d="0.7" data-to="{round(SAVED)}" data-comma="1">0</span>', "c", 600,
                           a="none", cls="Hw", style="font-size:300px;color:#FFB08F;letter-spacing:-.06em"),
                        words("less a year.", "c", 960, t=0.6, cls="Hw", style="font-size:110px")]),
            tin="zoom", focus=(540, 800), cam="push", shake=(0.85, 0.2, 16))
    r.scene(2.5, "".join(['<div class="par lite"></div>',
                          el(PILL("SAY THIS"), "c", 360, a="pop", t=0.0),
                          el('<div class="card" style="font:700 66px/1.25 Inter;padding:56px 60px">“I’ve paid on time.<br>Can you lower my rate?”</div>',
                             90, 520, 900, a="fly", t=0.1, d=0.45, r=-2),
                          scribble_circle(540, 700, 470, 190, coral, 10, t=0.7, d=0.45)]),
            tin="iris", focus=(540, 800), color=soft, cam="push")
    r.scene(1.5, "".join(['<div class="par cob"></div>',
                          words("Some say *yes.* / Some say no.", "c", 560, t=0.0, gap=0.1, cls="Hw", em_cls="emw", style="font-size:140px")]),
            tin="whipR", cam="tilt")
    r.scene(2.5, "".join(['<div class="par deep"></div>', el(PILL("THE CATCH", "#FF6A3D"), "c", 380, a="stamp", t=0.0, d=0.25, r=-4),
                          words("Paying it *down* / beats any rate cut.", "c", 540, t=0.15, gap=0.07, cls="Hw", em_cls="emw",
                                style="font-size:110px"),
                          words("Intro rates can jump back.", "c", 960, t=0.6, gap=0.05, cls="Hw", style="font-size:72px;opacity:.9")]),
            tin="stripes", color=coral, color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, "".join(['<div class="par lite"></div>',
                        words("Save this for your / next *free 5 minutes.*", "c", 480, t=0.0, gap=0.08, cls="H", style="font-size:110px"),
                        img("ht-piggy.png", 350, 880, 380, t=0.3, r=6),
                        el('<div class="finek">Example math. Not advice.</div>', "c", 1380, a="fade", t=0.3)]),
            tin="push", cam="push")
    r.loop(1.5, tin="whipU")
    return r


R["ff-reel-1018am-lower-rate"] = dict(make=ff_lower_rate, music="ff-curious-el-01.mp3")


# =============================================================================================== LH 08:30 pick 3, block them
LH_WEEK_CSS = AM.LH_CSS + """
.cal{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;width:900px}
.day{height:520px;border:6px solid #141414;border-radius:22px;background:#fff;box-shadow:10px 10px 0 #141414;position:relative;overflow:hidden}
.day b{display:block;font:900 44px/1 'Inter Display';padding:18px 0;text-align:center;border-bottom:4px solid #141414}
.blk{position:absolute;left:8px;right:8px;height:150px;border:4px solid #141414;border-radius:14px;font:800 34px/1.05 Inter;color:#141414;
  padding:14px 10px;box-shadow:4px 4px 0 #141414}
.pick{display:flex;gap:24px;align-items:center;font:800 70px/1.15 Inter;color:#141414;margin:22px 0}
.pick .ck{width:70px;height:70px;border-radius:16px;background:#FF5CA8;border:5px solid #141414;color:#fff;font:900 50px/60px Inter;text-align:center}
"""


def cal(blocks=False, t0=0.3):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    put = {0: ("Report", "#FF5CA8", 120), 2: ("Gym", "#FFD43B", 200), 4: ("Course", "#FF5CA8", 280)}
    out = ""
    for i, d in enumerate(days):
        b = ""
        if blocks and i in put:
            lab, col, top = put[i]
            k = sorted(put).index(i)
            b = (f'<div class="blk" data-a="drop" data-t="{t0 + 0.4 * k:.2f}" data-d="0.45" style="top:{top}px;background:{col}">{lab}</div>')
        out += f'<div class="day"><b>&nbsp;</b>{b}</div>'  # no day names: fewer words to read
    return f'<div class="cal">{out}</div>'


def lh_pick_3():
    r = Reel("lh-reel-1018am-pick-3", "lockedhour", bpm=100, css=LH_WEEK_CSS, stage="#FFE27A")
    r.scene(2, "".join([
        '<div class="par dots"></div>', AM.lh_chip(),
        el('Pick 3.<br><span class="em">Block them.</span>', "c", 420, a="none", cls="H", style="font-size:180px"),
        el(cal(True, t0=-1), 90, 900, a="none"),
    ]), cam="push")
    r.scene(2, "".join(['<div class="par dotsc"></div>',
                        words("Your week fills up / *on its own.*", "c", 420, t=0.0, gap=0.08, cls="H", style="font-size:120px"),
                        el(cal(False), 90, 860, a="up", t=0.3)]),
            tin="whipL", cam="push", shake=(0.4, 0.2, 10))
    picks = ["Finish the report", "Gym, twice", "One course lesson"]
    r.scene(3, "".join(['<div class="par dots"></div>', el('<span class="num">1</span>', 90, 360, a="pop", t=0.0),
                        words("Pick 3 that make / the week *good.*", "c", 560, t=0.05, gap=0.07, cls="H", em_cls="emy", style="font-size:110px"),
                        *[el(f'<div class="pick"><span class="ck">✓</span>{p}</div>', 110, 900 + k * 140, 860, a="left", t=0.5 + 0.35 * k, d=0.3)
                          for k, p in enumerate(picks)]]),
            tin="slam", cam="rise")
    r.scene(2.5, "".join(['<div class="par dotsc"></div>', el('<span class="num">2</span>', 90, 360, a="pop", t=0.0),
                          words("Give each one / a *locked hour.*", "c", 520, t=0.05, gap=0.08, cls="H", em_cls="emy", style="font-size:120px"),
                          el(cal(True, t0=0.5), 90, 900, a="none")]),
            tin="whipU", cam="push")
    r.scene(2, "".join(['<div class="par dotsp"></div>', el('<span class="num">3</span>', 90, 360, a="pop", t=0.0),
                        words("Treat it like / *a meeting.*", "c", 560, t=0.05, gap=0.1, cls="H", em_cls="emy", style="font-size:150px")]),
            tin="zoom", focus=(540, 700), cam="push")
    r.scene(2, "".join(['<div class="par dots"></div>',
                        words("Move it? *Fine.* / Delete it? *No.*", "c", 560, t=0.0, gap=0.12, cls="H", em_cls="emy", style="font-size:130px"),
                        img("ht-hourglass.png", 420, 1020, 240, t=0.4, r=8)]),
            tin="glitch", td=0.2, cam="tilt", shake=(0.6, 0.2, 12))
    r.scene(2, "".join(['<div class="par dotsp"></div>',
                        words("Save this / for *Sunday.*", "c", 520, t=0.0, gap=0.12, cls="H", em_cls="emy", style="font-size:160px"),
                        el('<span class="lab">@lockedhourhq</span>', "c", 980, a="pop", t=0.5)]),
            tin="stripes", color="#FFD43B", color2="#FFFFFF", color3="#141414", cam="push")
    r.loop(1.5, tin="whipU")
    return r


R["lh-reel-1018am-pick-3"] = dict(make=lh_pick_3, music="lh-focus-el-01.mp3")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--out", default="/tmp/motion-out")
    ap.add_argument("--qa-only", action="store_true")
    a = ap.parse_args()
    for i in a.ids or ["ff-reel-1018am-lower-rate", "lh-reel-1018am-pick-3"]:
        AM.build(i, a.out, a.qa_only)

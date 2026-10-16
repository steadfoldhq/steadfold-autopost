#!/usr/bin/env python3
"""Oct 17 Reels (08:00-08:45 and 19:00), re-edited with the motion kit. Same rules as reels_1016am.py.

    python3 studio/motion/reels_1017.py <id> --out DIR
"""
import argparse
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reels_1016am as AM  # noqa: E402
import reels_1016pm as PM  # noqa: E402
from kit import BRANDS, Reel, arrow, el, emoji, img, ring, scribble_circle, words  # noqa: E402

R = AM.R
photo = PM.photo
LF, FF, LH, HB = (BRANDS[b] for b in ("littlefold", "fullyfunded", "lockedhour", "hourback"))
PILL = lambda txt, bg="#2B3FE0", fg="#fff": (f'<span style="font:800 42px/1 Inter;letter-spacing:.12em;color:{fg};background:{bg};'  # noqa: E731
                                             f'padding:16px 26px;border-radius:999px">{txt}</span>')


# =============================================================================================== LF 08:00 read
def lf_read():
    r = Reel("lf-reel-1017am-read", "littlefold", bpm=92, css=PM.LFS_CSS + """
.book{width:420px;height:300px;border-radius:18px 30px 30px 18px;background:#FF8A70;box-shadow:inset 26px 0 0 #D9497A,0 26px 50px rgba(122,33,73,.25);
  display:flex;align-items:center;justify-content:center;font:700 64px/1 Lora;color:#fff}
""", stage="#2C2A3A")
    r.scene(2, "".join([
        photo("lf-father-bw.jpg", 0.4),
        el("Too little<br>for <i class='em'>books?</i>", "c", 440, a="none", cls="S", style="font-size:190px"),
        emoji("📚", 420, 1020, 220, t=0.3, d=0.4, loop="wobble"),
    ]), cam="push")
    r.scene(1.5, "".join(['<div class="par blobs"></div>', words("Read to them / *anyway.*", "c", 560, t=0.0, gap=0.14, cls="H", style="font-size:170px")]),
            tin="zoom", focus=(540, 700), cam="push")
    r.scene(1.5, "".join(['<div class="par pinkbg"></div>',
                          words("They won't follow / the *story* yet.", "c", 560, t=0.0, gap=0.1, cls="H", style="font-size:120px"),
                          emoji("🤷", 420, 1000, 220, t=0.35, d=0.3, loop="wobble")]), tin="whipL", cam="tilt")
    r.scene(1, "".join(['<div class="par blobs2"></div>', el("That's OK.", "c", 680, a="stamp", t=0.0, d=0.25, cls="H", style="font-size:200px")]),
            tin="cut", cam="push", shake=(0.0, 0.2, 14))
    r.scene(2, "".join([photo("lf-father-bw.jpg", 0.5, "40% center"),
                        words("Your *voice* and / the pictures / are the start.", "c", 480, t=0.0, gap=0.09, cls="S", style="font-size:150px")]),
            tin="flash", color=LF["peach"], color2=LF["butter"], cam="pull")
    r.scene(1.5, "".join(['<div class="par blobs"></div>', el('<span class="num">1</span>', "c", 380, a="pop", t=0.0),
                          words("Pick one / *board book.*", "c", 560, t=0.05, cls="H", style="font-size:150px"),
                          el('<div class="book">Moo!</div>', 330, 1000, a="fly", t=0.25, d=0.45, r=-6)]), tin="slam", cam="rise")
    r.scene(1.5, "".join(['<div class="par blobs2"></div>', el('<span class="num">2</span>', "c", 380, a="pop", t=0.0),
                          words("Same time / each day.", "c", 560, t=0.05, cls="H", style="font-size:150px"),
                          el('<span class="note" style="font-size:90px">like bedtime ☾</span>', "c", 980, a="pop", t=0.45, r=-4)]),
            tin="whipL", cam="push")
    r.scene(2, "".join(['<div class="par pinkbg"></div>', el('<span class="num">3</span>', "c", 360, a="pop", t=0.0),
                        words("Point. / Name it. / *Pause.*", "c", 540, t=0.1, gap=0.3, d=0.3, cls="H", style="font-size:170px"),
                        emoji("👉", 140, 1200, 170, t=0.2, d=0.3, r=-8), emoji("🐮", 700, 1200, 190, t=0.5, d=0.3, loop="wobble")]),
            tin="blob", focus=(540, 900), color=LF["butter"], cam="push")
    r.scene(1.5, "".join(['<div class="par blobs"></div>', words("Let them / *look.*", "c", 600, t=0.0, gap=0.14, cls="H", style="font-size:190px"),
                          emoji("👀", 420, 1060, 220, t=0.3, d=0.3, loop="float")]), tin="push", cam="pull")
    r.scene(2, "".join([
        '<div class="par" style="background:radial-gradient(circle, rgba(255,255,255,.08) 2px, transparent 2.6px) 0 0/34px 34px,#7A2149"></div>',
        el('<div class="small" style="font-size:40px">The American Academy of Pediatrics</div>', "c", 420, a="up", t=0.0),
        words("recommends reading / aloud together / *from infancy.*", "c", 540, t=0.15, gap=0.08, cls="S", em_cls="em", style="font-size:130px"),
        el('<div class="small" style="font-size:30px;opacity:.75">Source: AAP policy statement on literacy promotion (2014), HealthyChildren.org</div>',
           "c", 1200, a="fade", t=0.4, style="padding:0 90px"),
    ]), tin="iris", focus=(540, 800), color=LF["pink"], cam="push")
    r.scene(2, "".join(['<div class="par blobs2"></div>',
                        words("Save this for / *bedtime.*", "c", 560, t=0.0, gap=0.12, cls="H", style="font-size:160px"),
                        emoji("🌙", 420, 980, 200, t=0.35, d=0.35, loop="float"),
                        el('<div class="src">General information, not medical advice. Photo made with AI.</div>', "c", 1380, a="fade", t=0.3)]),
            tin="stripes", color=LF["pink"], color2=LF["butter"], color3=LF["peach"], cam="push")
    r.loop(1.5, tin="flash", color=LF["peach"], color2=LF["butter"])
    return r


# =============================================================================================== FF 08:15 match
def ff_match():
    r = Reel("ff-reel-1017am-match", "fullyfunded", bpm=95, css=AM.FF_CSS, stage="#2B3FE0")
    coral, soft = FF["acc"], FF["acc2"]
    r.scene(2, "".join([
        '<div class="par cob"></div>', AM.ff_chip(),
        el('You joined<br>the plan.<br>Never checked<br>the <span class="emw">match?</span>', "c", 400, a="none", cls="Hw", style="font-size:130px"),
        emoji("🫣", 420, 1080, 220, t=0.3, d=0.35, loop="wobble"),
    ]), cam="push")
    r.scene(1.5, "".join(['<div class="par lite"></div>',
                          words("Many employers / *add money* / when you do.", "c", 520, t=0.0, gap=0.1, cls="H", style="font-size:120px"),
                          emoji("🤝", 420, 1000, 220, t=0.4, d=0.3, loop="float")]), tin="whipL", cam="push")
    r.scene(2, "".join(['<div class="par deep"></div>', el(PILL("EXAMPLE MATH", "#FF6A3D"), "c", 380, a="stamp", t=0.0, d=0.25, r=-3),
                        words("Pay: 50,000 a year.", "c", 520, t=0.1, cls="Hw", style="font-size:96px"),
                        words("They add *half* of what / you put in, up to / 6% of pay.", "c", 700, t=0.4, gap=0.06, cls="Hw", em_cls="emw",
                              style="font-size:84px")]), tin="glitch", td=0.2, cam="tilt")
    bar = lambda lab, to, val, col, t0: (
        f'<div style="font:700 50px/1.1 Inter;color:#0E1440;margin-bottom:16px">{lab}</div>'
        f'<div class="bar" style="background:rgba(43,63,224,.12)"><div class="f" data-a="bar" data-t="{t0}" data-d="0.5" data-to="{to}" '
        f'style="background:{col}"></div></div><div class="H" style="font-size:110px;margin-top:16px">+<span data-a="count" data-t="{t0}" '
        f'data-d="0.5" data-to="{val}" data-comma="1">0</span> <span style="font-size:56px">from them</span></div>')
    r.scene(3.5, "".join(['<div class="par lite"></div>',
                          el(bar("You put in 3%", 50, 750, soft, 0.1), 90, 420, 900, a="up", t=0.0),
                          el(bar("You put in 6%", 100, 1500, "#2B3FE0", 0.45), 90, 860, 900, a="up", t=0.3)]), tin="slam", cam="rise")
    r.scene(1.5, "".join(['<div class="par cob"></div>',
                          el('+<span data-a="count" data-t="0.05" data-d="0.6" data-to="750">0</span>', "c", 480, a="none", cls="Hw",
                             style="font-size:300px;color:#FFB08F;letter-spacing:-.06em"),
                          words("a year more / *from them.*", "c", 860, t=0.3, cls="Hw", em_cls="emw", style="font-size:120px")]),
            tin="zoom", focus=(540, 700), cam="push", shake=(0.6, 0.2, 18))
    r.scene(1.5, "".join(['<div class="par lite"></div>', el('<span class="num">1</span>', "c", 400, a="pop", t=0.0),
                          words("Open your / *benefits portal.*", "c", 580, t=0.05, cls="H", style="font-size:120px")]), tin="whipL", cam="push")
    r.scene(1.5, "".join(['<div class="par lite"></div>', el('<span class="num">2</span>', "c", 400, a="pop", t=0.0),
                          words("Search for", "c", 580, t=0.05, cls="H", style="font-size:120px"),
                          el('<div class="field">🔍 <span data-a="type" data-t="0.3" data-d="0.35">match</span><span class="caret"></span></div>',
                             130, 780, a="up", t=0.1)]), tin="push", cam="push")
    r.scene(1.5, "".join(['<div class="par lite"></div>', el('<span class="num">3</span>', "c", 400, a="pop", t=0.0),
                          words("Compare what you / put in with *the most* / they'll match.", "c", 580, t=0.05, gap=0.06, cls="H",
                                style="font-size:100px")]), tin="iris", focus=(540, 700), color=soft, cam="push")
    r.scene(2.5, "".join(['<div class="par deep"></div>', el(PILL("THE CATCH", "#FF6A3D"), "c", 380, a="stamp", t=0.0, d=0.25, r=-4),
                          words("The match may need / you to stay a while / *(vesting).*", "c", 520, t=0.15, gap=0.06, cls="Hw", em_cls="emw",
                                style="font-size:88px"),
                          words("It's usually locked / until retirement age.", "c", 900, t=0.7, gap=0.05, cls="Hw", style="font-size:70px;opacity:.9"),
                          words("Only put in what / you can keep up.", "c", 1130, t=1.1, gap=0.05, cls="Hw", em_cls="emw", style="font-size:70px")]),
            tin="stripes", color=coral, color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, "".join(['<div class="par cob"></div>',
                        words("401(k) · group RRSP · / *workplace pension*", "c", 480, t=0.0, gap=0.08, cls="Hw", em_cls="emw", style="font-size:90px"),
                        words("Rules differ where you live. / Check your plan's documents.", "c", 760, t=0.4, gap=0.05, cls="Hw",
                              style="font-size:62px;opacity:.9"),
                        el('<div class="fine">Example math. General education only, not financial advice.</div>', "c", 1300, a="fade", t=0.3)]),
            tin="push", cam="push")
    r.scene(1.5, "".join(['<div class="par lite"></div>', words("Check it / *today.*", "c", 560, t=0.0, cls="H", style="font-size:190px"),
                          img("ht-piggy.png", 360, 980, 360, t=0.3, r=-6)]), tin="flash", color=soft, color2="#FFFFFF", cam="push")
    r.loop(1.5, tin="whipU")
    return r


# =============================================================================================== LH 08:30 next step
def lh_next_step():
    r = Reel("lh-reel-1017am-next-step", "lockedhour", bpm=100, css=AM.LH_CSS + """
.todo{width:880px;padding:40px 46px}
.todo .row{display:flex;align-items:center;gap:22px;font:800 64px/1.2 Inter;color:#141414;padding:16px 0;border-top:3px solid #EEE}
.todo .bx{width:54px;height:54px;border:5px solid #141414;border-radius:10px;flex:none}
.strike{position:relative}.sk{background:#FF5CA8;height:.16em;top:48%}
.new{font-family:'Caveat Brush';font-size:96px;color:#E8336F;line-height:1}
""", stage="#FFE27A")
    r.scene(2, "".join([
        '<div class="par dots"></div>', AM.lh_chip(),
        el('<div class="box todo"><div style="font:900 56px/1 \'Inter Display\';margin-bottom:16px">To do</div>'
           '<div class="row"><span class="bx"></span>Do taxes</div><div class="row"><span class="bx"></span>Plan the trip</div>'
           '<div class="row"><span class="bx"></span>Fix my CV</div></div>', 100, 420, a="none", r=-2),
        el('<span class="badge" style="font-size:60px">3 weeks</span>', 640, 520, a="stamp", t=0.3, d=0.25, r=10, loop="pulse"),
        el('Why won\'t it<br><span class="em">start?</span>', "c", 1050, a="none", cls="H", style="font-size:150px"),
    ]), cam="push", shake=(0.3, 0.2, 16))
    r.scene(1.5, "".join(['<div class="par dotsp"></div>',
                          words("“Do taxes” / isn't a task.", "c", 520, t=0.0, gap=0.1, cls="H", style="font-size:150px")]),
            tin="glitch", td=0.2, cam="push")
    r.scene(1.5, "".join(['<div class="par dots"></div>', words("It's a / *project.*", "c", 560, t=0.0, gap=0.14, cls="H", style="font-size:220px")]),
            tin="cut", cam="push", shake=(0.0, 0.25, 22))
    r.scene(2, "".join(['<div class="par dotsc"></div>',
                        words("Ask: what would I / *physically* do first?", "c", 480, t=0.0, gap=0.08, cls="H", style="font-size:110px"),
                        emoji("🤔", 420, 960, 230, t=0.4, d=0.3, loop="wobble")]), tin="stripes", color="#FF5CA8", color2="#FFFFFF",
            color3="#141414", cam="tilt")
    rw = lambda old, new, t0: (f'<div class="paper" style="padding:46px 50px"><div class="H" style="font-size:96px"><span class="strike">{old}'
                               f'<span class="sk" data-a="strike" data-t="{t0}" data-d="0.3"></span></span></div>'
                               f'<div class="new" data-a="wipe" data-t="{t0 + 0.3}" data-d="0.5" style="margin-top:24px">→ {new}</div></div>')
    r.scene(2.5, "".join(['<div class="par dots"></div>', el(rw("Do taxes", "Find last year's form", 0.25), 90, 560, 900, a="fly", t=0.0, d=0.45, r=-2),
                          emoji("✍️", 780, 1020, 170, t=0.7, d=0.3, loop="wobble")]), tin="slam", cam="rise")
    r.scene(2, "".join(['<div class="par dotsc"></div>', el(rw("Plan the trip", "Text Sam 2 dates", 0.2), 90, 560, 900, a="right", t=0.0, d=0.35, r=2)]),
            tin="whipL", cam="push")
    r.scene(2, "".join(['<div class="par dots"></div>', el(rw("Fix my CV", "Update one job title", 0.2), 90, 560, 900, a="right", t=0.0, d=0.35, r=-2)]),
            tin="whipL", cam="push")
    r.scene(1.5, "".join(['<div class="par dotsp"></div>',
                          words("Write *that* down. / Start there.", "c", 560, t=0.0, gap=0.1, cls="H", em_cls="emy", style="font-size:140px")]),
            tin="zoom", focus=(540, 700), cam="push")
    r.scene(2, "".join(['<div class="par dots"></div>',
                        words("Rewrite / one task / *now.*", "c", 420, t=0.0, gap=0.1, cls="H", style="font-size:150px"),
                        el('<div class="B">Save this, and follow<br>@lockedhourhq.</div>', "c", 960, a="up", t=0.4),
                        img("ht-hourglass.png", 420, 1120, 230, t=0.45, r=8)]), tin="iris", focus=(540, 800), color="#FFFFFF", cam="push")
    r.loop(1.5, tin="whipU")
    return r


# =============================================================================================== HB 08:45 swap
def hb_swap():
    r = Reel("hb-reel-1017am-swap", "hourback", bpm=108, css=AM.HB_CSS + """
.rc{background:#fff;border-radius:40px;padding:44px 50px;box-shadow:0 30px 60px rgba(0,0,0,.25);font:600 56px/1.5 Inter;color:#2A2238}
.rc .t{font:700 70px/1 Poppins;margin-bottom:14px}
.strike{position:relative}.sk{background:#FF8A3D;height:.14em;top:48%}
.res{background:#FFC94D;border-radius:36px;padding:36px 42px;font:600 52px/1.35 Inter;color:#2A2238;box-shadow:0 20px 40px rgba(0,0,0,.2)}
""", stage="#3A2240")
    org = HB["acc2"]
    r.scene(2, "".join([
        '<div class="par peach"></div>', AM.hb_chip(),
        el('Halfway in.<br><span class="em">No eggs.</span>', "c", 420, a="none", cls="H", style="font-size:170px"),
        emoji("🥞", 180, 920, 260, t=-0.5, loop="float"),
        emoji("🥚", 620, 940, 200, t=0.2, d=0.3, loop="buzz"),
        el('<span style="font:800 200px/1 Inter;color:#E8336F">✕</span>', 620, 900, a="stamp", t=0.45, d=0.22),
    ]), cam="push", shake=(0.45, 0.2, 18))
    r.scene(2, "".join(['<div class="par cream"></div>',
                        el('<div class="rc"><div class="t">Pancakes</div>1 cup flour<br>1 cup milk<br><span class="strike">1 egg<span class="sk" '
                           'data-a="strike" data-t="0.4" data-d="0.3"></span></span><br>2 tsp baking powder</div>', 120, 480, 840, a="fly", t=0.0, d=0.4, r=-3),
                        emoji("😩", 420, 1240, 200, t=0.6, d=0.3, loop="wobble")]), tin="whipL", cam="tilt")
    r.scene(1.5, "".join(['<div class="par indi"></div>',
                          words("Don't run / to the *shop.*", "c", 560, t=0.0, gap=0.12, cls="Hw", em_cls="emo2", style="font-size:170px")]),
            tin="glitch", td=0.18, cam="push")
    prompt = ('<div class="pc"><span class="k">PROMPT · IN THE CAPTION</span><br>I’m making <span class="chipy">[recipe]</span> and I’m out of '
              '<span class="chipy">[ingredient]</span>. Give me 2 swaps most kitchens have. Say how much to use and how each changes the result.</div>')
    r.scene(2.5, "".join(['<div class="par cream"></div>', words("Ask any AI chat / for a *swap.*", "c", 380, t=0.0, gap=0.1, cls="H", style="font-size:110px"),
                          el(prompt, 80, 720, 920, a="fly", t=0.1, d=0.45, r=-2)]), tin="whipU", cam="rise")
    r.scene(3, "".join(['<div class="par plum"></div>', el('<span class="tag">WHAT YOU GET · EXAMPLE MADE UP</span>', "c", 400, a="pop", t=0.0),
                        el('<div class="res">🍌 <b>Mashed banana:</b> ¼ cup per egg. Sweeter, a bit denser.</div>', 80, 520, 920, a="left", t=0.1, d=0.3),
                        el('<div class="res">🥣 <b>Plain yogurt:</b> ¼ cup per egg. Soft, a little tangy.</div>', 80, 900, 920, a="left", t=0.6, d=0.3),
                        emoji("😋", 420, 1300, 200, t=1.0, d=0.3, loop="float")]), tin="pixel", td=0.4, cam="pull")
    r.scene(1.5, "".join(['<div class="par indi"></div>',
                          words("Pick the one / that *fits.*", "c", 560, t=0.0, gap=0.12, cls="Hw", em_cls="emo2", style="font-size:170px")]),
            tin="push", cam="push")
    r.scene(2, "".join(['<div class="par cream"></div>',
                        words("Allergies? / Say so in / the *prompt.*", "c", 460, t=0.0, gap=0.1, cls="H", style="font-size:140px"),
                        el('<div class="fine">And double-check anything important before you cook.</div>', "c", 1000, a="up", t=0.45)]),
            tin="iris", focus=(540, 800), color=HB["acc"], cam="push")
    r.scene(1.5, "".join(['<div class="par peach"></div>', words("Paste. Ask. / *Keep cooking.*", "c", 560, t=0.0, gap=0.12, cls="H", style="font-size:150px"),
                          emoji("🥞", 420, 1180, 230, t=0.35, d=0.3, loop="float")]), tin="stripes", color=HB["acc"], color2="#5E54C9", color3=org,
            cam="push")
    r.loop(1.5, tin="flash", color=HB["acc"], color2=org)
    return r


# =============================================================================================== FF 19:00 raise half
def ff_raise_half():
    r = Reel("ff-reel-1017-raise-half", "fullyfunded", bpm=95, css=AM.FF_CSS, stage="#16206B")
    coral, soft = FF["acc"], FF["acc2"]
    r.scene(2, "".join([photo("ff-street.jpg", 0.35), AM.ff_chip(),
                        el('Got a<br><span class="emw">raise?</span>', "c", 460, a="none", cls="Hw", style="font-size:220px"),
                        emoji("🎉", 420, 1000, 220, t=0.3, d=0.35, loop="wobble")]), cam="push", shake=(0.3, 0.2, 14))
    r.scene(1.5, "".join(['<div class="par cob"></div>', words("Save *half.*", "c", 520, t=0.0, gap=0.14, cls="Hw", em_cls="emw", style="font-size:220px"),
                          words("Enjoy half.", "c", 820, t=0.4, cls="Hw", style="font-size:150px")]), tin="zoom", focus=(540, 700), cam="push")
    r.scene(2, "".join(['<div class="par lite"></div>', el(PILL("EXAMPLE MATH"), "c", 380, a="pop", t=0.0),
                        words("A raise of / *200 a month.*", "c", 520, t=0.05, cls="H", style="font-size:130px"),
                        el('<div style="display:flex;gap:40px;justify-content:center"><div class="card" style="font:800 140px/1 \'Inter Display\';'
                           'color:#2B3FE0;padding:50px 60px">100<br><span style="font:700 48px Inter;color:#4A5180">saved</span></div><div class="card" style="font:800 140px/1 '
                           '\'Inter Display\';color:#FF6A3D;padding:50px 60px">100<br><span style="font:700 48px Inter;color:#4A5180">enjoyed</span></div></div>', "c", 860,
                           a="up", t=0.45)]), tin="whipL", cam="push")
    r.scene(2.5, "".join(['<div class="par deep"></div>',
                          words("Save 100 a month / for 20 years:", "c", 420, t=0.0, gap=0.08, cls="Hw", style="font-size:96px"),
                          el('<span data-a="count" data-t="0.2" data-d="1.0" data-to="46204" data-comma="1">0</span>', "c", 690, a="none", cls="Hw",
                             style="font-size:250px;color:#FFB08F;letter-spacing:-.06em"),
                          words("from 24,000 paid in.", "c", 1000, t=0.7, cls="Hw", style="font-size:80px")]), tin="slam", cam="push",
            shake=(1.2, 0.2, 14))
    r.scene(1.5, "".join(['<div class="par cob"></div>',
                          words("Set the transfer / the day it *lands.*", "c", 520, t=0.0, gap=0.1, cls="Hw", em_cls="emw", style="font-size:120px"),
                          emoji("🔁", 420, 980, 220, t=0.35, d=0.3, loop="spin", amp=2)]), tin="glitch", td=0.2, cam="tilt")
    r.scene(1.5, "".join(['<div class="par lite"></div>',
                          words("Before you get / *used to* the extra.", "c", 560, t=0.0, gap=0.1, cls="H", style="font-size:120px")]),
            tin="push", cam="push")
    r.scene(2.5, "".join(['<div class="par deep"></div>', el(PILL("THE CATCH", "#FF6A3D"), "c", 380, a="stamp", t=0.0, d=0.25, r=-4),
                          words("Only save what / you can *keep up.*", "c", 520, t=0.15, gap=0.08, cls="Hw", em_cls="emw", style="font-size:120px"),
                          words("A smaller amount you never stop / beats a big one you cancel.", "c", 900, t=0.6, gap=0.04, cls="Hw",
                                style="font-size:60px;opacity:.9")]), tin="stripes", color=coral, color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, "".join([photo("ff-street.jpg", 0.5, "30% center"),
                        words("Save this for / your *next raise.*", "c", 520, t=0.0, gap=0.1, cls="Hw", em_cls="emw", style="font-size:130px"),
                        el('<div class="fine" style="color:#E6E9FF">Example at 6% a year, compounded monthly. Not a promise. Real returns vary, before fees, '
                           'tax and inflation. General education only, not financial advice. Photo made with AI.</div>', "c", 1240, a="fade", t=0.3,
                           style="padding:0 90px")]), tin="flash", color=soft, color2="#FFFFFF", cam="push")
    r.loop(1.5, tin="zoom", focus=(540, 700))
    return r


# =============================================================================================== HB 19:00 offline
def hb_offline():
    r = Reel("hb-reel-1017-offline", "hourback", bpm=108, css=AM.HB_CSS + """
.dump{display:flex;flex-wrap:wrap;gap:16px;justify-content:center;width:940px}
.dump span{background:#fff;color:#2A2238;font:600 44px/1 Inter;padding:20px 26px;border-radius:999px;box-shadow:0 10px 20px rgba(0,0,0,.18)}
.plan{background:#FFC94D;border-radius:36px;padding:40px 46px;font:600 50px/1.5 Inter;color:#2A2238}
""", stage="#3A2240")
    yel, org = HB["acc"], HB["acc2"]
    chips = ["dentist?", "reply to Jo", "gym", "report draft", "buy milk", "call mum", "book car service", "laundry", "invoice", "RSVP"]
    r.scene(2, "".join([photo("hb-clouds.jpg", 0.35), AM.hb_chip(),
                        el('Off work.<br>Brain still <span class="emo2">at work?</span>', "c", 440, a="none", cls="Hw", style="font-size:130px"),
                        emoji("🧠", 420, 940, 220, t=0.2, d=0.3, loop="buzz", amp=1.2)]), cam="push")
    r.scene(2.5, "".join(['<div class="par plum"></div>', words("Dump *everything* / into any AI chat.", "c", 380, t=0.0, gap=0.08, cls="Hw",
                                                                em_cls="emo2", style="font-size:100px"),
                          el('<div class="dump" data-a="stack" data-t="0.3" data-gap="0.07" data-d="0.3">' + "".join(f"<span>{c}</span>" for c in chips)
                             + '</div>', 70, 760, a="none")]), tin="whipL", cam="tilt")
    prompt = ('<div class="pc"><span class="k">PROMPT · IN THE CAPTION</span><br>Here’s everything on my mind for tomorrow: <span class="chipy">[brain dump]'
              '</span>. Pick my 3 must-dos and give me a rough schedule. Move the rest to later this week.</div>')
    r.scene(2.5, "".join(['<div class="par cream"></div>', words("Ask for your / *3 must-dos.*", "c", 380, t=0.0, gap=0.1, cls="H", style="font-size:120px"),
                          el(prompt, 80, 740, 920, a="fly", t=0.1, d=0.45, r=-2)]), tin="whipU", cam="rise")
    r.scene(2.5, "".join(['<div class="par indi"></div>', el('<span class="tag">EXAMPLE MADE UP</span>', "c", 400, a="pop", t=0.0),
                          el('<div class="plan"><div data-a="left" data-t="0.15" data-d="0.3"><b>9:00</b> Report draft</div><div data-a="left" '
                             'data-t="0.4" data-d="0.3"><b>12:30</b> Reply to Jo</div><div data-a="left" data-t="0.65" data-d="0.3"><b>17:30</b> Gym</div>'
                             '<div data-a="fade" data-t="1.0" data-d="0.3" style="font-size:40px;opacity:.75;margin-top:14px">Later this week: the rest</div></div>',
                             90, 520, 900, a="none")]), tin="pixel", td=0.4, cam="pull")
    r.scene(1.5, "".join(['<div class="par cream"></div>', words("Check it. / Move what's *wrong.*", "c", 560, t=0.0, gap=0.1, cls="H", style="font-size:140px")]),
            tin="push", cam="push")
    r.scene(2, "".join([photo("hb-clouds.jpg", 0.45, "30% center"), words("Then *log off.*", "c", 600, t=0.0, gap=0.14, cls="Hw", em_cls="emo2",
                                                                         style="font-size:200px"),
                        emoji("💻", 420, 1000, 220, t=0.3, d=0.3), el('<span class="tag">CLOSED</span>', "c", 1260, a="stamp", t=0.55, d=0.22, r=-6)]),
            tin="flash", color=yel, color2=org, cam="push", shake=(0.55, 0.2, 14))
    r.scene(2, "".join(['<div class="par plum"></div>',
                        words("Save this / for *tonight.*", "c", 520, t=0.0, gap=0.12, cls="Hw", em_cls="emo2", style="font-size:170px"),
                        el('<div class="fine" style="color:#CFC6E6">Tip: remove personal details before you paste.<br>Photo made with AI.</div>', "c", 1000,
                           a="up", t=0.4)]), tin="stripes", color=yel, color2="#5E54C9", color3=org, cam="push")
    r.loop(1.5, tin="zoom", focus=(540, 700))
    return r


# =============================================================================================== LF 19:00 one job
def lf_one_job():
    r = Reel("lf-reel-1017-one-job", "littlefold", bpm=92, css=AM.LF_CSS + """
.bub{background:#fff;border-radius:44px;border-bottom-left-radius:12px;padding:36px 44px;font:600 56px/1.3 Inter;color:#2C2A3A;
  box-shadow:0 24px 50px rgba(122,33,73,.18)}
.job{background:#fff;border-radius:40px;padding:40px 46px;box-shadow:0 26px 60px rgba(122,33,73,.18);display:flex;gap:30px;align-items:center}
.job .emo{font-size:150px}
""", stage="#FFF4E0")
    r.scene(2, "".join(['<div class="par blobs"></div>', AM.lf_chip(),
                        el('<div class="bub">Let me know if you<br>need anything! 😊</div>', 110, 420, 860, a="none", loop="float", amp=0.5),
                        el('Hard to answer<br>at <span class="em">3 am.</span>', "c", 820, a="none", cls="H", style="font-size:150px"),
                        emoji("😵‍💫", 420, 1180, 200, t=0.3, d=0.3, loop="wobble")]), cam="push")
    r.scene(1.5, "".join(['<div class="par pinkbg"></div>', words("Give them / *one job.*", "c", 560, t=0.0, gap=0.14, cls="H", style="font-size:190px")]),
            tin="zoom", focus=(540, 700), cam="push", shake=(0.3, 0.2, 14))
    jobs = [("🍲", "Bring dinner", "on Tuesday."), ("🧺", "Fold one load", "of laundry."), ("🚿", "Hold the baby", "while I shower."), ("🐕", "Walk the", "dog.")]
    tins = ["slam", "whipL", "whipL", "whipL"]
    for k, (e, a, b) in enumerate(jobs):
        r.scene(1.5, "".join([f'<div class="par {"blobs" if k % 2 == 0 else "blobs2"}"></div>', el(f'<span class="num">{k + 1}</span>', "c", 380, a="pop", t=0.0),
                              el(f'<div class="job"><span class="emo">{e}</span><div class="H" style="font-size:96px">{a}<br><span class="em">{b}</span></div></div>',
                                 80, 600, 920, a="fly", t=0.05, d=0.45, r=-3 if k % 2 else 3)]), tin=tins[k], cam="rise")
    r.scene(2, "".join(['<div class="par pinkbg"></div>', words("A clear job is / *easy to say yes to.*", "c", 520, t=0.0, gap=0.09, cls="H", style="font-size:120px"),
                        emoji("🙌", 420, 960, 220, t=0.4, d=0.3, loop="float")]), tin="iris", focus=(540, 800), color=LF["butter"], cam="push")
    r.scene(1.5, "".join(['<div class="par blobs2"></div>', words("Then let them do it / *their way.*", "c", 560, t=0.0, gap=0.1, cls="H", style="font-size:130px")]),
            tin="blob", focus=(540, 900), color=LF["pink"], cam="pull")
    r.scene(2, "".join(['<div class="par blobs"></div>',
                        words("Send this to the friend / who keeps asking / how they can *help.*", "c", 480, t=0.0, gap=0.07, cls="H", style="font-size:110px"),
                        emoji("💌", 420, 1020, 220, t=0.45, d=0.35, loop="float")]), tin="stripes", color=LF["pink"], color2=LF["butter"],
            color3=LF["peach"], cam="push")
    r.loop(1.5, tin="flash", color=LF["peach"], color2=LF["butter"])
    return r


# =============================================================================================== LH 19:00 one tab
def lh_one_tab():
    r = Reel("lh-reel-1017-one-tab", "lockedhour", bpm=100, css=AM.LH_CSS + """
.tabs{display:flex;gap:6px;width:960px;overflow:hidden}
.tab{flex:1 0 auto;min-width:46px;height:70px;background:#fff;border:4px solid #141414;border-radius:14px 14px 0 0;font:800 26px/62px Inter;
  text-align:center;color:#141414;padding:0 6px;overflow:hidden}
.win{width:960px;height:520px;background:#fff;border:6px solid #141414;border-radius:0 0 24px 24px;box-shadow:14px 14px 0 #141414}
""", stage="#FFE27A")
    many = "".join(f'<div class="tab" data-a="pop" data-t="{0.02 * k - 0.6:.2f}" data-d="0.2">{"✕" if k % 3 else "•"}</div>' for k in range(22))
    r.scene(2, "".join(['<div class="par dots"></div>', AM.lh_chip(),
                        el('How many tabs<br>are <span class="em">open?</span>', "c", 430, a="none", cls="H", style="font-size:122px"),
                        el(f'<div class="tabs">{many}</div><div class="win"></div>', 60, 820, a="none", loop="buzz", amp=0.3),
                        emoji("😵", 420, 1000, 220, t=0.3, d=0.3, loop="wobble")]), cam="push")
    r.scene(1.5, "".join(['<div class="par dotsp"></div>', words("Close every tab / *but one.*", "c", 560, t=0.0, gap=0.1, cls="H", em_cls="emy",
                                                               style="font-size:150px")]), tin="glitch", td=0.2, cam="push", shake=(0.0, 0.2, 20))
    r.scene(2, "".join(['<div class="par dotsc"></div>',
                        el('<div class="tabs"><div class="tab" style="flex:0 0 520px;height:96px;background:#FFD43B;font:900 48px/86px \'Inter Display\'">The one task</div></div><div class="win"></div>',
                           60, 600, a="stamp", t=0.0, d=0.3),
                        words("Ahh.", "c", 1250, t=0.4, cls="H", style="font-size:170px")]), tin="spin", cam="push")
    steps = [("1", "Keep the one tab / you *need.*"), ("2", "Opened a new one? / *Close it.* Go back."), ("3", "Need something later? / *Jot it* on paper.")]
    for k, (n, t) in enumerate(steps):
        r.scene(1.5, "".join([f'<div class="par {"dots" if k % 2 == 0 else "dotsc"}"></div>', el(f'<span class="num">{n}</span>', "c", 380, a="pop", t=0.0),
                              words(t, "c", 560, t=0.05, gap=0.08, cls="H", style="font-size:120px")]), tin=["slam", "whipL", "whipL"][k], cam="rise")
    r.scene(2.5, "".join([photo_clock(), words("One tab. / One task. / *One hour.*", "c", 420, t=0.0, gap=0.3, d=0.3, cls="H", style="font-size:170px")]),
            tin="zoom", focus=(540, 700), cam="push")
    r.scene(2, "".join(['<div class="par dotsp"></div>',
                        words("Save this. / Try it *tomorrow.*", "c", 520, t=0.0, gap=0.1, cls="H", em_cls="emy", style="font-size:150px"),
                        el('<span class="lab">@lockedhourhq</span>', "c", 980, a="pop", t=0.5)]), tin="stripes", color="#FFD43B", color2="#FFFFFF",
            color3="#141414", cam="push")
    r.loop(1.5, tin="whipU")
    return r


def photo_clock():
    return '<div class="par dots"></div>' + img("ht-clock.png", 290, 1000, 500, t=0.2, r=-6, loop="wobble", amp=0.4)


R.update({
    "lf-reel-1017am-read": dict(make=lf_read, music="lf-cosy-inst-01.mp3"),
    "ff-reel-1017am-match": dict(make=ff_match, music="ff-curious-inst-01.mp3"),
    "lh-reel-1017am-next-step": dict(make=lh_next_step, music="lh-focus-inst-01.mp3"),
    "hb-reel-1017am-swap": dict(make=hb_swap, music="hb-playful-inst-01.mp3"),
    "ff-reel-1017-raise-half": dict(make=ff_raise_half, music="ff-curious-inst-01.mp3"),
    "hb-reel-1017-offline": dict(make=hb_offline, music="hb-playful-inst-01.mp3"),
    "lf-reel-1017-one-job": dict(make=lf_one_job, music="lf-cosy-inst-01.mp3"),
    "lh-reel-1017-one-tab": dict(make=lh_one_tab, music="lh-focus-inst-01.mp3"),
})
ORDER = ["lf-reel-1017am-read", "ff-reel-1017am-match", "lh-reel-1017am-next-step", "hb-reel-1017am-swap",
         "ff-reel-1017-raise-half", "hb-reel-1017-offline", "lf-reel-1017-one-job", "lh-reel-1017-one-tab"]

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--out", default="/tmp/motion-out")
    ap.add_argument("--qa-only", action="store_true")
    a = ap.parse_args()
    for i in a.ids or ORDER:
        AM.build(i, a.out, a.qa_only)

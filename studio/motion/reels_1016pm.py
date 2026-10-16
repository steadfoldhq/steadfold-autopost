#!/usr/bin/env python3
"""Oct 16 evening Reels (19:00), re-edited with the motion kit. Same rules as reels_1016am.py.

    python3 studio/motion/reels_1016pm.py lf-reel-1016-doing-better --out DIR
"""
import argparse
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reels_1016am as AM  # noqa: E402
from kit import BRANDS, Reel, arrow, asset, el, emoji, img, ring, scribble_circle, words  # noqa: E402

R = AM.R  # register into the same table so AM.build() works


def photo(name, dark=0.45, pos="center"):
    return (f'<div class="par" style="background:url({asset(name)}) {pos}/cover"></div>'
            f'<div style="position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,{dark * .6}),rgba(0,0,0,{dark}) 55%,rgba(0,0,0,{dark * 1.3}))"></div>')


# =============================================================================================== Littlefold: silhouette story
LFS_CSS = AM.LF_CSS + """
.S{font-family:'Instrument Serif';color:#FFF4E0;line-height:.98;letter-spacing:-.01em;text-shadow:0 6px 30px rgba(0,0,0,.35)}
.S .em{font-style:italic;color:#FFD6E3}
.small{font:600 40px/1.3 Inter;color:#FFF4E0;opacity:.9}
"""


def lf_doing_better():
    r = Reel("lf-reel-1016-doing-better", "littlefold", bpm=92, css=LFS_CSS, stage="#2C2A3A")
    lf = BRANDS["littlefold"]
    r.scene(2, "".join([
        photo("lf-sil-walk.jpg", 0.35),
        el("You're doing<br><i class='em'>better</i> than<br>you think.", "c", 420, a="none", cls="S", style="font-size:170px"),
        emoji("✨", 760, 380, 110, t=0.3, d=0.4, loop="pulse", amp=2),
    ]), cam="push")
    r.scene(1.5, "".join([photo("lf-sil-lift.jpg", 0.3), words("You *fed* them.", "c", 520, t=0.0, gap=0.14, cls="S", style="font-size:180px")]),
            tin="flash", color=lf["peach"], color2=lf["butter"], cam="push")
    r.scene(1.5, "".join([photo("lf-shoulders.jpg", 0.3), words("You *held* them.", "c", 520, t=0.0, gap=0.14, cls="S", style="font-size:180px")]),
            tin="zoom", focus=(540, 700), cam="pull")
    r.scene(1.5, "".join([photo("lf-sil-walk.jpg", 0.4, "30% center"),
                          words("You came / *back*", "c", 520, t=0.0, gap=0.14, cls="S", style="font-size:190px")]),
            tin="push", cam="left")
    r.scene(1, "".join([photo("lf-sil-lift.jpg", 0.5, "60% center"),
                        el("<i class='em'>again,</i>", "c", 640, a="stamp", t=0.0, d=0.25, cls="S", style="font-size:240px")]),
            tin="cut", cam="push", shake=(0.0, 0.2, 12))
    r.scene(1.5, "".join([photo("lf-shoulders.jpg", 0.5, "40% center"),
                          el("<i class='em'>and again.</i>", "c", 620, a="stamp", t=0.0, d=0.25, cls="S", style="font-size:200px")]),
            tin="cut", cam="push", shake=(0.0, 0.2, 14))
    r.scene(2, "".join([
        '<div class="par" style="background:radial-gradient(circle, rgba(255,255,255,.08) 2px, transparent 2.6px) 0 0/34px 34px,#7A2149"></div>',
        words("Some nights it / doesn't feel like / *enough.*", "c", 560, t=0.0, gap=0.09, cls="S", style="font-size:140px"),
    ]), tin="slit", color=lf["pink"], cam="pull")
    r.scene(1.5, "".join([
        '<div class="par blobs"></div>',
        el("It is.", "c", 620, a="stamp", t=0.0, d=0.3, cls="H", style="font-size:280px"),
        emoji("💗", 420, 1020, 240, t=0.3, d=0.4, loop="pulse", amp=2),
    ]), tin="blob", focus=(540, 800), color=lf["butter"], cam="push")
    r.scene(2, "".join([
        photo("lf-shoulders.jpg", 0.45, "55% center"),
        words("Read this on / the *long nights.*", "c", 560, t=0.0, gap=0.1, cls="S", style="font-size:160px"),
        emoji("🌙", 440, 1000, 200, t=0.4, d=0.35, loop="float"),
    ]), tin="zoom", focus=(540, 700), cam="pull")
    r.scene(2.5, "".join([
        photo("lf-sil-lift.jpg", 0.35),
        words("That's the / *whole job* / today.", "c", 480, t=0.0, gap=0.12, cls="S", style="font-size:180px"),
    ]), tin="flash", color=lf["peach"], color2=lf["pink"], cam="push")
    r.scene(2, "".join([
        '<div class="par blobs2"></div>',
        words("Send this to a / *tired parent.*", "c", 520, t=0.0, gap=0.1, cls="H", style="font-size:130px"),
        emoji("💌", 420, 1060, 220, t=0.45, d=0.4, loop="float"),
        el('<div class="src">Photos made with AI.</div>', "c", 1400, a="fade", t=0.3),
    ]), tin="stripes", color=lf["pink"], color2=lf["butter"], color3=lf["peach"], cam="rise")
    r.loop(1.5, tin="flash", color=lf["peach"], color2=lf["butter"])
    return r


R["lf-reel-1016-doing-better"] = dict(make=lf_doing_better, music="lf-cosy-el-01.mp3")


# =============================================================================================== Fully Funded: the 1% fee
def ff_fee():
    r = Reel("ff-reel-1016-fee", "fullyfunded", bpm=95, css=AM.FF_CSS, stage="#2B3FE0")
    ff = BRANDS["fullyfunded"]
    coral, soft = ff["acc"], ff["acc2"]
    r.scene(2, "".join([
        '<div class="par cob"></div>', AM.ff_chip(),
        el('A <span class="emw">1%</span> fee<br>looks tiny.', "c", 460, a="none", cls="Hw", style="font-size:180px"),
        img("ht-piggy.png", 300, 920, 480, t=-0.5, r=-6, loop="float"),
        el('<div style="background:#FF6A3D;color:#fff;font:800 60px/1 Inter;padding:20px 36px;border-radius:999px">It isn\'t.</div>',
           600, 1300, a="stamp", t=0.4, d=0.25, r=-8, loop="pulse"),
    ]), cam="push", shake=(0.4, 0.25, 22))
    r.scene(1.5, "".join([
        '<div class="par lite"></div>',
        el('<span style="font:800 40px/1 Inter;letter-spacing:.14em;color:#fff;background:#2B3FE0;padding:16px 26px;border-radius:999px">'
           'EXAMPLE</span>', "c", 400, a="pop", t=0.0),
        words("200 a month / for *30 years.*", "c", 560, t=0.05, cls="H", style="font-size:140px"),
        el('<div class="finek" style="font-size:48px">6% a year. Not a promise.</div>', "c", 900, a="up", t=0.5),
    ]), tin="whipL", cam="push")
    bar = lambda lab, to, val, col, t0: (
        f'<div style="font:700 46px/1.1 Inter;color:#0E1440;margin-bottom:16px">{lab}</div>'
        f'<div class="bar" style="background:rgba(43,63,224,.12)"><div class="f" data-a="bar" data-t="{t0}" data-d="0.9" data-to="{to}" '
        f'style="background:{col}"></div></div><div class="H" style="font-size:120px;margin-top:16px"><span data-a="count" data-t="{t0}" '
        f'data-d="0.9" data-to="{val}" data-comma="1">0</span></div>')
    r.scene(3, "".join([
        '<div class="par lite"></div>',
        el(bar("No yearly fee", 100, 200903, "#2B3FE0", 0.1), 90, 420, 900, a="up", t=0.0),
        el(bar("With a 1% yearly fee", 82.9, 166452, coral, 0.3), 90, 860, 900, a="up", t=0.15),
    ]), tin="slam", cam="rise")
    r.scene(2, "".join([
        '<div class="par deep"></div>',
        words("That 1% costs / about", "c", 420, t=0.0, cls="Hw", style="font-size:110px"),
        el('<span data-a="count" data-t="0.15" data-d="0.7" data-to="34000" data-comma="1">0</span>', "c", 690, a="none", cls="Hw",
           style="font-size:270px;color:#FFB08F;letter-spacing:-.06em"),
    ]), tin="zoom", focus=(540, 900), cam="push", shake=(0.85, 0.2, 16))
    r.scene(1.5, "".join([
        '<div class="par cob"></div>',
        words("About a *sixth* / of the pot.", "c", 600, t=0.0, gap=0.12, cls="Hw", em_cls="emw", style="font-size:160px"),
        emoji("🍰", 420, 1050, 220, t=0.35, d=0.3, loop="wobble"),
    ]), tin="spin", cam="push")
    r.scene(1.5, "".join([
        '<div class="par cob"></div>',
        words("Find *yours* / this week.", "c", 560, t=0.0, cls="Hw", em_cls="emw", style="font-size:160px"),
        emoji("🔍", 400, 1000, 260, t=0.3, d=0.35, loop="float"),
    ]), tin="whipR", cam="tilt")
    doc = ('<div class="card" style="font:600 56px/1.6 Inter;padding:50px 56px;text-align:center">'
           '<span style="position:relative;display:inline-block">Annual fee / <b>expense ratio</b></span></div>')
    r.scene(2, "".join([
        '<div class="par lite"></div>',
        words("In each account, / look for:", "c", 400, t=0.0, gap=0.08, cls="H", style="font-size:110px"),
        el(doc, 110, 720, 860, a="fly", t=0.05, d=0.45, r=-2),
        scribble_circle(540, 818, 430, 80, coral, 10, t=0.55, d=0.4),
    ]), tin="iris", focus=(540, 900), color=soft, cam="push")
    r.scene(2.5, "".join([
        '<div class="par deep"></div>',
        el('<span style="font:800 44px/1 Inter;letter-spacing:.14em;color:#fff;background:#FF6A3D;padding:16px 26px;border-radius:999px">'
           'THE CATCH</span>', "c", 400, a="stamp", t=0.0, d=0.25, r=-4),
        words("Cheaper isn't / always *better.*", "c", 560, t=0.15, gap=0.08, cls="Hw", em_cls="emw", style="font-size:120px"),
        words("Compare like / with like.", "c", 960, t=0.5, gap=0.06, cls="Hw", style="font-size:80px;opacity:.9"),
    ]), tin="stripes", color=coral, color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, "".join([
        '<div class="par lite"></div>',
        words("Send this to a friend / with a *retirement* account.", "c", 480, t=0.0, gap=0.06, cls="H",
              style="font-size:100px"),
        img("ht-piggy.png", 350, 900, 380, t=0.3, r=6),
        el('<div class="finek">Education only. Not advice.</div>', "c", 1380, a="fade", t=0.3, style="padding:0 80px"),
    ]), tin="push", cam="push")
    r.loop(1.5, tin="whipU")
    return r


R["ff-reel-1016-fee"] = dict(make=ff_fee, music="ff-curious-el-01.mp3")


# =============================================================================================== Locked Hour: one quiet hour
def lh_quiet():
    r = Reel("lh-reel-1016-quiet", "lockedhour", bpm=100, css=AM.LH_CSS + """
.W{font-family:'Inter Display';font-weight:900;letter-spacing:-.05em;line-height:.95;color:#FFF4E0;text-shadow:0 8px 30px rgba(0,0,0,.4)}
.bubl{background:#fff;border:6px solid #141414;border-radius:36px;box-shadow:12px 12px 0 #141414;padding:34px 40px;font:800 60px/1.2 Inter;color:#141414}
.dnd{display:flex;align-items:center;gap:30px;background:#fff;border:6px solid #141414;border-radius:36px;box-shadow:12px 12px 0 #141414;
  padding:30px 40px;font:900 64px/1 'Inter Display'}
.tog{width:220px;height:120px;border-radius:999px;background:#ddd;border:5px solid #141414;position:relative;overflow:hidden;margin-left:auto}
.tog .on{position:absolute;inset:0;background:#FF5CA8}
.knob{position:absolute;left:8px;top:8px;width:94px;height:94px;border-radius:50%;background:#fff;border:5px solid #141414}
""", stage="#FFE27A")
    lh = BRANDS["lockedhour"]
    pings = "".join(f'<div class="mail"><span class="emo" style="font-size:52px">{a}</span><span>&nbsp;</span></div>' for a in "💬📩🔔💬")
    r.scene(2, "".join([
        '<div class="par dots"></div>', AM.lh_chip(),
        el('Want one<br><span class="em">quiet</span> hour?', "c", 460, a="none", cls="H", style="font-size:180px"),
        el(f'<div class="box inbox" style="width:860px"><div data-a="stack" data-t="-0.35" data-gap="0.16" data-d="0.3">{pings}</div></div>',
           110, 960, a="none", loop="buzz", amp=0.4),
    ]), cam="push", shake=(0.6, 0.2, 12))
    r.scene(1.5, "".join([
        '<div class="par dotsc"></div>',
        words("Ping. / Ping. / *Ping.*", "c", 420, t=0.0, gap=0.2, cls="H", style="font-size:200px"),
        emoji("📱", 700, 1200, 200, t=0.1, d=0.25, loop="buzz", amp=1.5),
    ]), tin="whipU", cam="tilt", shake=(0.2, 0.4, 10))
    r.scene(1.5, "".join([
        '<div class="par dotsp"></div>',
        words("Send *one line* / first.", "c", 600, t=0.0, gap=0.1, cls="H", em_cls="emy", style="font-size:140px"),
    ]), tin="glitch", td=0.2, cam="push")
    r.scene(2.5, "".join([
        '<div class="par dotsc"></div>',
        el('<span class="num">1</span>', 90, 380, a="pop", t=0.0),
        el('<div class="bubl"><span data-a="type" data-t="0.15" data-d="0.9">“Heads down till 11. Call if it’s urgent.”</span></div>', 90, 600, 900,
           a="up", t=0.05),
        el('<span class="lab">SENT ✓</span>', 660, 1000, a="stamp", t=1.15, d=0.22, r=-6),
    ]), tin="whipL", cam="rise", shake=(1.15, 0.2, 14))
    r.scene(2, "".join([
        '<div class="par dots"></div>',
        el('<span class="num">2</span>', 90, 380, a="pop", t=0.0),
        el('<div class="dnd"><span class="emo" style="font-size:90px">🌙</span>Do Not Disturb<div class="tog"><div class="on" data-a="fade" '
           'data-t="0.45" data-d="0.15"></div><div class="knob" data-a="right" data-t="0.4" data-d="0.25" style="left:108px"></div></div></div>',
           90, 640, 900, a="fly", t=0.05, d=0.4, r=-2),
        words("for *60 minutes.*", "c", 1000, t=0.5, cls="H", style="font-size:130px"),
    ]), tin="slam", cam="push")
    r.scene(1.5, "".join([
        '<div class="par dotsc"></div>',
        el('<span class="num">3</span>', "c", 360, a="pop", t=0.0),
        el("Start.", "c", 560, a="stamp", t=0.05, d=0.25, cls="H", style="font-size:330px"),
    ]), tin="zoom", focus=(540, 700), cam="push", shake=(0.05, 0.2, 22))
    r.scene(1.5, "".join([
        '<div class="par dots"></div>',
        words("Your hour. / *Your* work.", "c", 600, t=0.0, gap=0.14, cls="H", style="font-size:170px"),
    ]), tin="spin", cam="push")
    r.scene(3, "".join([
        photo("lh-forest.jpg", 0.35),
        el("Quiet.", "c", 520, a="fade", t=0.0, d=0.5, cls="W", style="font-size:300px"),
        ring(540, 1150, 170, "rgba(255,244,224,.25)", 26, t=-1, d=0.01),
        ring(540, 1150, 170, "#FFE27A", 26, t=0.1, d=1.4),
        el('<span data-a="count" data-t="0.1" data-d="1.4" data-from="3600" data-to="0" data-mmss="1">60:00</span>', "c", 1105, a="none",
           cls="W", style="font-size:90px"),
    ]), tin="flash", color="#FFE27A", color2="#FFFFFF", cam="push")
    r.scene(2, "".join([
        '<div class="par dots"></div>',
        words("The messages / will still be / *there* at 11.", "c", 480, t=0.0, gap=0.08, cls="H", style="font-size:130px"),
        emoji("⭐", 160, 1100, 150, t=0.5, d=0.3, loop="float"),
        el('<div class="B" style="font-size:52px">Favourites can<br>still call you.</div>', 300, 1110, 720,
           a="up", t=0.55, style="text-align:left"),
    ]), tin="iris", focus=(540, 800), color="#FF5CA8", cam="rise")
    r.scene(2, "".join([
        '<div class="par dotsp"></div>',
        words("Send this to / *someone who* / *answers every ping.*", "c", 420, t=0.0, gap=0.07, cls="H", em_cls="emy",
              style="font-size:100px"),
        el('<span class="lab">@lockedhourhq</span>', "c", 1180, a="pop", t=0.6),
    ]), tin="stripes", color="#FFD43B", color2="#FFFFFF", color3="#141414", cam="push")
    r.loop(1.5, tin="whipU")
    return r


R["lh-reel-1016-quiet"] = dict(make=lh_quiet, music="lh-focus-el-01.mp3")


# =============================================================================================== Hourback: just the asks
def hb_email_asks():
    r = Reel("hb-reel-1016-email-asks", "hourback", bpm=108, css=AM.HB_CSS + """
.mail{background:#fff;border-radius:40px;padding:44px 48px;width:900px;box-shadow:0 30px 60px rgba(0,0,0,.25)}
.mail .ln{height:26px;border-radius:13px;background:#E6E1F2;margin:18px 0}
.ask{background:#fff;border-radius:30px;padding:30px 36px;font:600 46px/1.3 Inter;color:#2A2238;margin-bottom:22px;box-shadow:0 14px 30px rgba(0,0,0,.15)}
.ask b{color:#5E54C9}.ask q{display:block;font:italic 500 36px/1.3 Inter;color:#6B6080;margin-top:10px}
""", stage="#3A2240")
    hb = BRANDS["hourback"]
    yel, org = hb["acc"], hb["acc2"]
    lines = "".join(f'<div class="ln" style="width:{60 + (k * 37) % 40}%"></div>' for k in range(40))
    r.scene(2, "".join([
        '<div class="par plum"></div>', AM.hb_chip(),
        el('Long email.<br><span class="emo2">Again.</span>', "c", 400, a="none", cls="Hw", style="font-size:160px"),
        el(f'<div class="mail" style="height:820px;overflow:hidden"><div data-a="none" data-loop="none" style="font:700 40px/1 Inter;color:#2A2238">'
           f'Re: Re: Fwd: Thursday</div><div class="scroller" data-a="scroll" data-t="0.1" data-d="1.0" data-to="700">{lines}</div></div>', 90, 820, a="up", t=-0.6),
        emoji("😩", 760, 1300, 200, t=0.4, d=0.3, loop="wobble"),
    ]), cam="push")
    r.scenes[-1]["dur"] = 2.5 * r.beat
    r.t = r.scenes[-1]["start"] + r.scenes[-1]["dur"]
    r.scene(2, "".join([
        '<div class="par indi"></div>',
        words("Read it twice. / Still not sure / what they *want.*", "c", 480, t=0.0, gap=0.09, cls="Hw", em_cls="emo2", style="font-size:112px"),
        emoji("🤔", 420, 1100, 220, t=0.45, d=0.3, loop="wobble"),
    ]), tin="glitch", td=0.2, cam="tilt")
    r.scene(1.5, "".join([
        '<div class="par cream"></div>',
        words("You just need / *the asks.*", "c", 600, t=0.0, gap=0.12, cls="H", style="font-size:136px"),
        img("ht-point.png", 520, 1020, 420, a="fly", t=0.3, d=0.35, r=-20, loop="float"),
    ]), tin="zoom", focus=(540, 1000), cam="push")
    prompt = ('<div class="pc"><span class="k">PROMPT IN CAPTION</span><br>What do they need from me, by when?</div>')
    r.scene(2.5, "".join([
        '<div class="par cream"></div>',
        words("Paste it in / and *ask:*", "c", 380, t=0.0, gap=0.1, cls="H", style="font-size:120px"),
        el(prompt, 80, 740, 920, a="fly", t=0.1, d=0.45, r=-2),
    ]), tin="whipU", cam="rise")
    asks = [("Send the deck", "Thu"), ("Confirm the room", "Fri"), ("Pick a date", "anytime")]
    r.scene(3.5, "".join([
        '<div class="par plum"></div>',
        el('<span class="tag">EXAMPLE · MADE UP</span>', "c", 360, a="pop", t=0.0),
        *[el(f'<div class="ask" style="font-size:60px"><b>{a}</b> · {b}</div>', 80, 520 + k * 240, 920, a="left", t=0.15 + k * 0.4, d=0.3)
          for k, (a, b) in enumerate(asks)],
    ]), tin="pixel", td=0.4, cam="pull")
    r.scene(2, "".join([
        '<div class="par indi"></div>',
        words("Check each / *quote* against / the email.", "c", 480, t=0.0, gap=0.1, cls="Hw", em_cls="emo2", style="font-size:130px"),
        emoji("🔎", 420, 1100, 220, t=0.4, d=0.3, loop="float"),
    ]), tin="push", cam="push")
    r.scene(1.5, "".join([
        '<div class="par cream"></div>',
        words("Then reply / to *the asks.*", "c", 560, t=0.0, gap=0.1, cls="H", style="font-size:160px"),
        el('<span class="send">Reply ➤</span>', "c", 1050, a="pop", t=0.4, loop="pulse"),
    ]), tin="iris", focus=(540, 900), color=yel, cam="push", shake=(0.4, 0.2, 10))
    r.scene(2.5, "".join([
        '<div class="par plum"></div>',
        words("Save for the / next *long email.*", "c", 460, t=0.0, gap=0.1, cls="Hw", em_cls="emo2", style="font-size:140px"),
        el('<div class="fine" style="color:#CFC6E6">Remove private details first.<br>Hand image made with AI.</div>', "c", 1100, a="up", t=0.4),
    ]), tin="stripes", color=yel, color2="#5E54C9", color3=org, cam="push")
    r.loop(2.5, tin="flash", color=yel, color2=org)
    return r


R["hb-reel-1016-email-asks"] = dict(make=hb_email_asks, music="hb-playful-el-01.mp3")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--out", default="/tmp/motion-out")
    ap.add_argument("--qa-only", action="store_true")
    a = ap.parse_args()
    for i in a.ids or ["lf-reel-1016-doing-better", "ff-reel-1016-fee", "lh-reel-1016-quiet", "hb-reel-1016-email-asks"]:
        AM.build(i, a.out, a.qa_only)

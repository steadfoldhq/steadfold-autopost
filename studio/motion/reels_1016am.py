#!/usr/bin/env python3
"""Oct 16 morning Reels, re-edited with the motion kit (no slideshows): a new beat every 0.6-1.2 s on the music's
tempo, a transition on every cut, kinetic word-by-word type, hook in frame 0, ends on the hook so it loops.

    python3 studio/motion/reels_1016am.py lf-reel-1016am-tummy-time [--qa-only] [--out DIR]
"""
import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from kit import (BRANDS, asset as asset_uri, Reel, arrow, chip, el, emoji, encode, img, loudness, probe, qa_times, render_frames,  # noqa: E402
                 ring, scribble_circle, sheet, words)

REPO = HERE.parent.parent
MUSIC = REPO / "media" / "music" / "library"
R = {}


# =============================================================================================== Littlefold
LF = BRANDS["littlefold"]
LF_CSS = """
.H{font-family:Lora;font-weight:600;color:#2C2A3A;letter-spacing:-.02em;line-height:1.04}
.em{font-style:italic;color:#D9497A}
.B{font:600 52px/1.25 Inter;color:#2C2A3A}
.note{font-family:'Caveat Brush';color:#D9497A}
.blobs{background:
  radial-gradient(420px 420px at 6% 8%, #FFD6E3 0 60%, transparent 61%),
  radial-gradient(360px 360px at 100% 22%, #FFE27E 0 58%, transparent 59%),
  radial-gradient(520px 520px at 96% 100%, #FFD3AE 0 60%, transparent 61%),
  radial-gradient(300px 300px at 0% 92%, #FFC9D6 0 58%, transparent 59%),
  radial-gradient(circle, rgba(44,42,58,.07) 2px, transparent 2.6px) 0 0/34px 34px, #FFF4E0}
.blobs2{background:
  radial-gradient(520px 520px at 100% 0%, #FFD6E3 0 60%, transparent 61%),
  radial-gradient(420px 420px at 0% 60%, #FFD3AE 0 58%, transparent 59%),
  radial-gradient(360px 360px at 90% 100%, #FFE27E 0 58%, transparent 59%),
  radial-gradient(circle, rgba(44,42,58,.07) 2px, transparent 2.6px) 0 0/34px 34px, #FFF8E4}
.pinkbg{background:radial-gradient(circle, rgba(122,33,73,.10) 2px, transparent 2.6px) 0 0/34px 34px, #FFD6E3}
.card{background:#fff;border-radius:56px;padding:56px 60px;box-shadow:0 30px 70px rgba(122,33,73,.16)}
.num{display:inline-flex;align-items:center;justify-content:center;width:120px;height:120px;border-radius:50%;background:#D9497A;
  color:#fff;font:700 70px/1 Lora}
.sticky{background:repeating-linear-gradient(#FFFDF6 0 74px,#E9DCCB 74px 76px);border-radius:10px;padding:150px 60px 60px 120px;
  box-shadow:0 30px 60px rgba(44,42,58,.18);position:relative}
.sticky:before{content:"";position:absolute;left:92px;top:0;bottom:0;width:4px;background:#F08A8A}
.tape{position:absolute;left:50%;top:-34px;width:260px;height:70px;margin-left:-130px;background:rgba(255,214,227,.85);transform:rotate(-3deg)}
.it{font:700 80px/76px Caveat;color:#2C2A3A;display:flex;gap:18px;align-items:center}
.tk{color:#D9497A;font:700 64px/1 Inter}
.dot{width:96px;height:96px;border-radius:50%;background:#fff;border:6px solid #F3B7C9}
.fill{background:#D9497A;border-color:#D9497A}
.dot{position:relative}.dfill{position:absolute;inset:-6px;border-radius:50%;background:#D9497A}
.em2{font-style:italic;color:#FFD6E3}
.src{font:600 30px/1.3 Inter;color:#7A6F80}
"""


def lf_bg(k=1):
    return f'<div class="par {"blobs" if k == 1 else "blobs2"}"></div>'


def lf_chip():
    return chip("littlefold", "c", 250, bg="#FFFFFF", a="none")


def lf_tummy():
    r = Reel("lf-reel-1016am-tummy-time", "littlefold", bpm=92, css=LF_CSS, stage="#FFF4E0")
    berry, coral = LF["acc"], LF["acc2"]
    hook = "".join([
        lf_bg(1), lf_chip(),
        el('Baby <span class="em">hates</span><br>tummy time?', "c", 520, a="none", cls="H", style="font-size:150px"),
        emoji("😫", 380, 900, 300, t=-0.5, d=0.45, loop="wobble", amp=1.6),
        el('<div style="background:#D9497A;color:#fff;font:800 64px/1 Inter;padding:22px 40px;border-radius:999px;letter-spacing:.04em">TRY THIS</div>',
           600, 1240, a="stamp", t=0.45, d=0.3, r=-8, loop="pulse"),
    ])
    r.scene(2, hook, cam="push", shake=(0.45, 0.3, 26))
    r.scene(1, "".join([
        lf_bg(2),
        words("On the *floor:*", "c", 470, t=0.0, cls="H", style="font-size:140px"),
        emoji("😭", 330, 820, 420, t=0.1, d=0.3, loop="buzz", amp=1.4),
    ]), tin="whipL", cam="tilt")
    r.scene(1, "".join([
        '<div class="par pinkbg"></div>',
        words("Every. / Single. / *Time.*", "c", 380, t=0.0, gap=0.16, cls="H", style="font-size:170px"),
        emoji("😭", 120, 1230, 220, t=0.3, d=0.25, loop="buzz", r=-12),
        emoji("😭", 700, 1300, 260, t=0.45, d=0.25, loop="buzz", r=10),
    ]), tin="glitch", td=0.2, cam="push", shake=(0.0, 0.25, 30))
    r.scene(2, "".join([
        lf_bg(1),
        words("So try it / on *your chest.*", "c", 470, t=0.0, gap=0.12, cls="H", style="font-size:140px"),
        emoji("💗", 400, 900, 300, t=0.55, d=0.4, loop="pulse", amp=2),
        el('<span class="note" style="font-size:70px">face to face ♡</span>', "c", 1280, a="pop", t=0.9, r=-4),
    ]), tin="zoom", cam="push")
    r.scene(1.5, "".join([
        lf_bg(2),
        el('<div class="card"><span class="num">1</span><div class="H" style="font-size:104px;margin-top:40px">Lie back,<br>'
           '<span class="em">propped up.</span></div></div>', 90, 520, 900, a="fly", t=0.0, d=0.5, r=-3),
        el('<div class="B" style="font-size:52px">Wide awake.</div>', "c", 1260, a="up", t=0.45),
    ]), tin="slam", cam="rise")
    r.scene(1.5, "".join([
        lf_bg(1),
        el('<div class="card"><span class="num">2</span><div class="H" style="font-size:104px;margin-top:40px">Baby tummy-down<br>'
           '<span class="em">on you.</span></div></div>', 90, 520, 900, a="fly", t=0.0, d=0.5, r=3),
    ]), tin="whipL", cam="rise")
    r.scene(2, "".join([
        '<div class="par pinkbg"></div>',
        el('<span class="num">3</span>', "c", 360, a="pop", t=0.0),
        words("Talk. / Sing. / Just *look.*", "c", 560, t=0.1, gap=0.33, d=0.3, cls="H", style="font-size:170px"),
    ]), tin="blob", focus=(540, 900), color=LF["butter"], cam="push")
    r.scene(1.5, "".join([
        lf_bg(2),
        ring(540, 820, 300, "#F3B7C9", 40, t=-1, d=0.01),
        ring(540, 820, 300, berry, 40, t=0.0, d=0.9),
        el('1–2<br><span style="font-size:70px">min</span>', "c", 690, a="pop", t=0.05, cls="H", style="font-size:170px;line-height:.9"),
        words("is plenty *to start.*", "c", 1200, t=0.35, cls="H", style="font-size:96px"),
    ]), tin="iris", focus=(540, 820), color=LF["pink"], cam="pull")
    items = [("From birth", 0.25), ("Only while baby's awake", 0.75), ("And you're wide awake", 1.25)]
    lis = "".join(el(f'<div class="it"><span class="tk">✓</span>{x}</div>', 0, 0, a="left", t=tt, d=0.3,
                     style="position:relative;margin-bottom:14px") for x, tt in items)
    r.scene(2.5, "".join([
        lf_bg(1),
        el(f'<div class="sticky"><div class="tape"></div><div class="note" style="position:absolute;left:120px;top:44px;font-size:84px">'
           f'Tummy time, gently:</div>{lis}</div>', 80, 470, 920, a="drop", t=0.0, d=0.55, r=-2),
    ]), tin="whipU", cam="tilt")
    r.scene(1.5, "".join([
        '<div class="par pinkbg"></div>',
        el('<span data-a="count" data-t="0" data-d="0.75" data-to="30">0</span>', "c", 360, a="none", cls="H",
           style="font-size:520px;color:#D9497A;line-height:1"),
        words("minutes a day", "c", 960, t=0.3, cls="H", style="font-size:110px"),
        el('<div class="src">What the WHO suggests for babies<br>not yet moving around.</div>', "c", 1150, a="up", t=0.6),
    ]), tin="zoom", focus=(540, 700), cam="push")
    dots = "".join(f'<div class="dot"><div class="dfill" data-a="pop" data-t="{0.35 + k * 0.045:.3f}" data-d="0.25"></div></div>'
                   for k in range(30))
    r.scene(2.5, "".join([
        lf_bg(2),
        words("Spread *through* the day.", "c", 400, t=0.0, cls="H", style="font-size:110px"),
        el(f'<div id="dots" style="display:grid;grid-template-columns:repeat(6,96px);gap:26px;justify-content:center">{dots}</div>',
           "c", 680, a="up", t=0.1),
        el('<span class="note" style="font-size:84px">it adds up, a minute at a time</span>', "c", 1430, a="pop", t=0.9, r=-3),
    ]), tin="push", cam="rise")
    r.scene(2, "".join([
        '<div class="par" style="background:radial-gradient(circle, rgba(255,255,255,.12) 2px, transparent 2.6px) 0 0/34px 34px,#7A2149"></div>',
        emoji("🌙", 400, 360, 280, t=0.05, d=0.45, loop="float"),
        words("Feeling sleepy?", "c", 760, t=0.15, cls="H", style="font-size:120px;color:#FCE5EB"),
        words("Baby goes on / their *back* in the cot.", "c", 1000, t=0.5, gap=0.09, cls="H", style="font-size:84px;color:#fff",
              em_cls="em2"),
    ]), tin="flash", color=LF["peach"], color2=LF["pink"], cam="pull")
    r.scene(2, "".join([
        lf_bg(1),
        words("Send this to a / *new parent.*", "c", 560, t=0.0, cls="H", style="font-size:130px"),
        emoji("💌", 420, 980, 240, t=0.4, d=0.4, loop="float"),
        el('<div class="src">Sources: WHO (2019) · NHS tummy time advice<br>General info, not medical advice.</div>', "c", 1400, a="fade", t=0.2),
    ]), tin="stripes", color=LF["pink"], color2=LF["butter"], color3=LF["peach"], cam="push")
    r.loop(1.5, tin="zoom", focus=(540, 700))
    return r


R["lf-reel-1016am-tummy-time"] = dict(make=lf_tummy, music="lf-cosy-inst-01.mp3")


# =============================================================================================== Fully Funded
FF = BRANDS["fullyfunded"]
FF_CSS = """
.H{font-family:'Inter Display';font-weight:800;letter-spacing:-.045em;line-height:.98;color:#0E1440}
.Hw{font-family:'Inter Display';font-weight:800;letter-spacing:-.045em;line-height:.98;color:#fff}
.em{color:#FF6A3D}
.emw{color:#FFB08F}
.serif{font-family:'Instrument Serif';font-weight:400;letter-spacing:-.02em;line-height:.9}
.B{font:600 52px/1.25 Inter;color:#0E1440}
.cob{background:radial-gradient(circle, rgba(255,255,255,.10) 2px, transparent 2.6px) 0 0/36px 36px,#2B3FE0}
.lite{background:radial-gradient(circle, rgba(43,63,224,.08) 2px, transparent 2.6px) 0 0/36px 36px,#F5F7FF}
.deep{background:radial-gradient(circle, rgba(255,255,255,.08) 2px, transparent 2.6px) 0 0/36px 36px,#16206B}
.card{background:#fff;border-radius:44px;padding:54px 56px;box-shadow:0 30px 70px rgba(14,20,64,.22)}
.num{display:inline-flex;align-items:center;justify-content:center;width:110px;height:110px;border-radius:50%;background:#2B3FE0;color:#fff;
  font:800 64px/1 'Inter Display'}
.bill{background:#fff;border-radius:30px;padding:34px 40px;box-shadow:0 30px 60px rgba(0,0,0,.3);font:700 44px/1.2 Inter;color:#0E1440;width:520px}
.bill .due{display:inline-block;background:#FF6A3D;color:#fff;font:800 30px/1 Inter;letter-spacing:.1em;padding:12px 18px;border-radius:12px;margin-top:18px}
.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:14px}
.cal div{height:150px;border-radius:24px;background:#fff;border:4px solid #DDE2FF;font:800 40px/1 'Inter Display';color:#0E1440;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px}
.cal small{font:700 22px/1 Inter;color:#6870A8;letter-spacing:.06em}
.ccard{width:640px;height:400px;border-radius:40px;background:linear-gradient(135deg,#16206B,#2B3FE0);box-shadow:0 40px 80px rgba(0,0,0,.35);
  position:relative;color:#fff;font:700 40px/1 Inter}
.ccard .chipc{position:absolute;left:60px;top:110px;width:110px;height:80px;border-radius:16px;background:#F6D44C}
.ccard .nm{position:absolute;left:60px;bottom:60px;letter-spacing:.2em;opacity:.85}
.field{background:#fff;border:6px solid #2B3FE0;border-radius:28px;padding:34px 40px;font:700 84px/1 Inter;color:#0E1440;width:820px}
.caret{display:inline-block;width:8px;height:84px;background:#FF6A3D;vertical-align:-10px;margin-left:6px}
.tog{width:300px;height:160px;border-radius:999px;background:#C9CEF2;position:relative;overflow:hidden}
.tog .on{position:absolute;inset:0;background:#FF6A3D}
.knob{position:absolute;left:12px;top:12px;width:136px;height:136px;border-radius:50%;background:#fff;box-shadow:0 8px 20px rgba(0,0,0,.25)}
.bar{height:110px;border-radius:30px;background:rgba(255,255,255,.15);overflow:hidden;position:relative}
.bar .f{position:absolute;left:0;top:0;bottom:0;border-radius:30px}
.lab{font:700 46px/1.1 Inter;color:#fff;margin:0 0 18px}
.fine{font:600 32px/1.3 Inter;color:#C9CEF2}
.finek{font:600 32px/1.3 Inter;color:#4A5180}
"""


def ff_chip(dark=True):
    return chip("fullyfunded", "c", 250, bg="#FFFFFF" if dark else "#E6E9FF", a="none")


def ff_buffer():
    r = Reel("ff-reel-1016am-buffer", "fullyfunded", bpm=95, css=FF_CSS, stage="#2B3FE0")
    coral, soft = FF["acc"], FF["acc2"]
    hook = "".join([
        '<div class="par cob"></div>', ff_chip(),
        el('The car repair<br>is <span class="emw">today.</span>', "c", 470, a="none", cls="Hw", style="font-size:150px"),
        el('<div class="bill">🔧 Car repair<br><span style="font-weight:600;color:#4A5180">Brakes + labour</span><br>'
           '<span class="due">DUE TODAY</span></div>', 280, 900, a="fly", t=-0.6, d=0.5, r=-6, loop="float"),
        emoji("😬", 700, 1280, 200, t=0.35, d=0.35, loop="wobble"),
    ])
    r.scene(2, hook, cam="push", shake=(0.35, 0.25, 20))
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    cells = "".join(f'<div><small>{d}</small>{k + 13}</div>' for k, d in enumerate(days))
    r.scene(1.5, "".join([
        '<div class="par lite"></div>',
        words("Payday *isn't.*", "c", 440, t=0.0, cls="H", style="font-size:170px"),
        el(f'<div class="cal">{cells}</div>', 60, 820, 960, a="up", t=0.05),
        scribble_circle(128, 895, 80, 92, coral, 10, t=0.2, d=0.3),
        el('<span style="font:800 40px/1 Inter;color:#FF6A3D">today</span>', 70, 1010, a="pop", t=0.3),
        scribble_circle(679, 895, 80, 92, "#2B3FE0", 10, t=0.5, d=0.3),
        el('<span style="font:800 40px/1 Inter;color:#2B3FE0">payday</span>', 612, 1010, a="pop", t=0.6),
        arrow(200, 1090, 640, 1090, "#0E1440", 8, t=0.45, d=0.4, bend=-40),
    ]), tin="whipL", cam="left")
    r.scene(1.5, "".join([
        '<div class="par deep"></div>',
        words("So it lands / on a *card.*", "c", 420, t=0.0, cls="Hw", em_cls="emw", style="font-size:150px"),
        el('<div class="ccard"><div class="chipc"></div><div class="nm">•••• 4242</div></div>', 220, 900, a="fly", t=0.05, d=0.5, r=-8),
        el('<div style="background:#FF6A3D;color:#fff;font:800 56px/1 Inter;padding:20px 34px;border-radius:999px">+ interest</div>',
           600, 1320, a="stamp", t=0.55, d=0.25, r=8, loop="pulse"),
    ]), tin="glitch", td=0.2, cam="tilt", shake=(0.55, 0.25, 22))
    r.scene(2, "".join([
        f'<div class="par" style="background:url({asset_uri("ff-family-bw.jpg")}) center/cover;filter:grayscale(1) brightness(.62)"></div>',
        el('Buffer.', "c", 560, a="stamp", t=0.0, d=0.3, cls="serif", style="font-size:330px;color:#fff"),
        words("A small pot for / *surprise bills.*", "c", 940, t=0.3, gap=0.08, cls="Hw", em_cls="emw", style="font-size:84px"),
    ]), tin="zoom", focus=(540, 1000), cam="push")
    r.scene(1.5, "".join([
        '<div class="par lite"></div>',
        el('<div class="card"><span class="num">1</span><div class="H" style="font-size:100px;margin-top:34px">Open a separate<br>'
           '<span class="em">savings account.</span></div></div>', 80, 560, 920, a="fly", t=0.0, d=0.5, r=-3),
    ]), tin="slam", cam="rise")
    r.scene(1.5, "".join([
        '<div class="par lite"></div>',
        el('<span class="num">2</span>', "c", 470, a="pop", t=0.0),
        words("Name it", "c", 640, t=0.05, cls="H", style="font-size:130px"),
        el('<div class="field"><span data-a="type" data-t="0.3" data-d="0.45">Buffer</span><span class="caret" data-a="none" '
           'data-loop="pulse"></span></div>', 130, 860, a="up", t=0.1),
        emoji("✏️", 820, 1080, 150, t=0.7, d=0.3, r=-10),
    ]), tin="whipL", cam="push")
    r.scene(1.5, "".join([
        '<div class="par lite"></div>',
        el('<span class="num">3</span>', "c", 400, a="pop", t=0.0),
        words("Auto-move / *25 a week.*", "c", 570, t=0.05, cls="H", style="font-size:130px"),
        el('<div class="tog"><div class="on" data-a="fade" data-t="0.45" data-d="0.15"></div>'
           '<div class="knob" data-a="right" data-t="0.4" data-d="0.25" style="left:152px"></div></div>', 390, 1000, a="up", t=0.15),
    ]), tin="push", cam="push")
    r.scene(1.5, "".join([
        '<div class="par cob"></div>',
        words("Only for / *surprises.*", "c", 520, t=0.0, cls="Hw", em_cls="emw", style="font-size:150px"),
        emoji("🚗", 110, 960, 170, t=0.25, d=0.3, r=-10, loop="float"),
        emoji("🦷", 420, 1060, 150, t=0.4, d=0.3, r=8, loop="float"),
        emoji("📱", 700, 960, 160, t=0.55, d=0.3, r=-6, loop="float"),
        emoji("🐶", 300, 1300, 160, t=0.7, d=0.3, r=6, loop="float"),
        emoji("🔧", 620, 1290, 160, t=0.85, d=0.3, r=-8, loop="float"),
    ]), tin="iris", focus=(540, 960), color=soft, cam="pull")
    r.scene(2, "".join([
        '<div class="par lite"></div>',
        el('<span style="font:800 44px/1 Inter;letter-spacing:.14em;color:#fff;background:#2B3FE0;padding:16px 26px;border-radius:999px">'
           'EXAMPLE MATH</span>', "c", 380, a="pop", t=0.0),
        words("25 a week =", "c", 520, t=0.05, cls="H", style="font-size:120px"),
        el('<span data-a="count" data-t="0.3" data-d="0.8" data-to="1300" data-comma="1">0</span>', "c", 700, a="none", cls="H",
           style="font-size:330px;color:#2B3FE0;letter-spacing:-.06em"),
        words("in a year", "c", 1060, t=0.55, cls="H", style="font-size:110px"),
        el('<div class="finek">Before any interest.</div>', "c", 1220, a="fade", t=0.8),
    ]), tin="zoom", focus=(540, 900), cam="push")
    r.scene(1, "".join([
        '<div class="par cob"></div>',
        words("Any currency. / *Same math.*", "c", 700, t=0.0, gap=0.1, cls="Hw", em_cls="emw", style="font-size:130px"),
    ]), tin="cut", cam="push", shake=(0.0, 0.2, 24))
    r.scene(2, "".join([
        '<div class="par deep"></div>',
        el('<span style="font:800 44px/1 Inter;letter-spacing:.14em;color:#fff;background:#FF6A3D;padding:16px 26px;border-radius:999px">'
           'THE CATCH</span>', "c", 400, a="stamp", t=0.0, d=0.25, r=-4),
        words("Cash grows slowly. / Prices *rise.*", "c", 560, t=0.15, gap=0.08, cls="Hw", em_cls="emw", style="font-size:104px"),
        words("It's for surprises, / not for investing.", "c", 1000, t=0.6, gap=0.06, cls="Hw", style="font-size:72px;opacity:.9"),
        emoji("📈", 760, 1250, 160, t=0.4, d=0.3, r=8, loop="float"),
    ]), tin="stripes", color=coral, color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, "".join([
        '<div class="par cob"></div>',
        el('<div class="fine" style="font-size:40px;color:#fff">A common rule of thumb:</div>', 90, 420, 900, a="up", t=0.0),
        el('<div class="lab">Start with</div><div class="bar"><div class="f" data-a="bar" data-t="0.15" data-d="0.4" data-to="18" '
           'style="background:#FFB08F"></div></div><div class="Hw" style="font-size:96px;margin-top:20px">1 month <span class="emw">of spending</span></div>',
           90, 540, 900, a="up", t=0.05),
        el('<div class="lab">Then build to</div><div class="bar"><div class="f" data-a="bar" data-t="0.7" data-d="0.5" data-to="100" '
           'style="background:#FF6A3D"></div></div><div class="Hw" style="font-size:96px;margin-top:20px">3 to 6 months</div>',
           90, 1000, 900, a="up", t=0.55),
    ]), tin="push", cam="rise")
    r.scene(1.5, "".join([
        '<div class="par lite"></div>',
        words("Save this / for *payday.*", "c", 600, t=0.0, cls="H", style="font-size:160px"),
        img("ht-piggy.png", 330, 1000, 420, t=0.25, r=-6),
        el('<div class="finek">Example math. General education only, not financial advice.</div>', "c", 1540, a="fade", t=0.3),
    ]), tin="flash", color=soft, color2="#FFFFFF", cam="push")
    r.loop(1.5, tin="whipU")
    return r


R["ff-reel-1016am-buffer"] = dict(make=ff_buffer, music="ff-curious-inst-01.mp3")


# =============================================================================================== Locked Hour
LH = BRANDS["lockedhour"]
LH_CSS = """
.H{font-family:'Inter Display';font-weight:900;letter-spacing:-.05em;line-height:.95;color:#141414}
.em{background:linear-gradient(#FF5CA8,#FF5CA8) 0 88%/100% 38% no-repeat;padding:0 .06em}
.emy{background:linear-gradient(#FFD43B,#FFD43B) 0 88%/100% 38% no-repeat;padding:0 .06em}
.dots{background:radial-gradient(circle, rgba(20,20,20,.12) 2.4px, transparent 3px) 0 0/30px 30px,#FFE27A}
.dotsc{background:radial-gradient(circle, rgba(20,20,20,.12) 2.4px, transparent 3px) 0 0/30px 30px,#FFF4E0}
.dotsp{background:radial-gradient(circle, rgba(20,20,20,.14) 2.4px, transparent 3px) 0 0/30px 30px,#FF5CA8}
.box{background:#fff;border:6px solid #141414;border-radius:28px;box-shadow:14px 14px 0 #141414}
.inbox{width:900px;padding:30px 34px}
.inbox .top{display:flex;justify-content:space-between;font:900 48px/1 'Inter Display';margin-bottom:18px}
.badge{background:#FF5CA8;color:#141414;border:5px solid #141414;border-radius:999px;padding:6px 20px;font:900 44px/1 'Inter Display'}
.mail{display:flex;gap:16px;align-items:center;font:700 40px/1.2 Inter;color:#141414;padding:18px 6px;border-top:3px solid #EEE}
.mail:before{content:"";width:18px;height:18px;border-radius:50%;background:#FF5CA8;flex:none}
.mail span{color:#888;font-weight:500}
.num{display:inline-flex;align-items:center;justify-content:center;width:120px;height:120px;border-radius:50%;background:#FFD43B;
  border:6px solid #141414;font:900 70px/1 'Inter Display';color:#141414;box-shadow:6px 6px 0 #141414}
.paper{background:#FFFDF6;border:6px solid #141414;border-radius:18px;box-shadow:14px 14px 0 #141414;padding:60px 56px}
.hand{font-family:'Caveat Brush';font-size:120px;color:#141414;line-height:1}
.timer{font:900 300px/1 'Inter Display';letter-spacing:-.04em;color:#141414}
.lab{display:inline-block;background:#141414;color:#FFE27A;font:900 40px/1 'Inter Display';letter-spacing:.08em;padding:16px 26px;border-radius:12px}
.B{font:800 54px/1.2 Inter;color:#141414}
"""


def lh_chip():
    return chip("lockedhour", "c", 250, bg="#141414", ink="#FFE27A", a="none")


def lh_email():
    r = Reel("lh-reel-1016am-before-email", "lockedhour", bpm=100, css=LH_CSS, stage="#FFE27A")
    pink = LH["acc"]
    mails = [("Re: quick question", "Can you look at…"), ("Team update", "A few things for…"), ("Invoice 2231", "Your invoice is…"),
             ("Fwd: Fwd: plan", "See below…"), ("Lunch?", "Are you free…")]
    inbox = lambda t0, gap: ('<div class="box inbox"><div class="top">Inbox <span class="badge"><span data-a="tick" data-t="%s" data-d="1.0" '
                             'data-from="3" data-to="27">27</span> new</span></div><div data-a="stack" data-t="%s" data-gap="%s" data-d="0.3">%s</div></div>'
                             % (t0, t0, gap, "".join(f'<div class="mail">{a}<span>{b}</span></div>' for a, b in mails)))
    hook = "".join([
        '<div class="par dots"></div>', lh_chip(),
        el('Open email<br><span class="em">first?</span>', "c", 470, a="none", cls="H", style="font-size:190px"),
        emoji("📧", 380, 960, 300, t=-0.5, loop="wobble"),
        el('<span class="badge" style="font-size:90px;padding:10px 34px">27</span>', 600, 930, a="stamp", t=0.3, d=0.25, r=10, loop="pulse"),
        img("ht-hourglass.png", 120, 1240, 220, t=0.55, r=-10),
    ])
    r.scene(2, hook, cam="push", shake=(0.3, 0.25, 22))
    r.scene(2, "".join([
        '<div class="par dotsc"></div>',
        el(inbox(0.0, 0.14), 90, 420, a="none"),
        words("Ping. Ping. *Ping.*", "c", 1300, t=0.1, gap=0.18, cls="H", style="font-size:130px"),
    ]), tin="whipU", cam="tilt", shake=(0.75, 0.2, 14))
    r.scene(1.5, "".join([
        '<div class="par dotsp"></div>',
        words("Now it picks / your *morning.*", "c", 600, t=0.0, gap=0.1, cls="H", em_cls="emy", style="font-size:136px"),
    ]), tin="glitch", td=0.2, cam="push", shake=(0.0, 0.25, 26))
    r.scene(1.5, "".join([
        '<div class="par dots"></div>',
        el('<span class="lab">INSTEAD</span>', "c", 420, a="stamp", t=0.0, d=0.25, r=-4),
        el('<span class="em">ONE</span>', "c", 560, a="stamp", t=0.1, d=0.3, cls="H", style="font-size:400px"),
        words("thing first.", "c", 1000, t=0.35, cls="H", style="font-size:150px"),
    ]), tin="stripes", color=pink, color2="#FFFFFF", color3="#141414", cam="push")
    r.scene(2, "".join([
        '<div class="par dotsc"></div>',
        el('<span class="num">1</span>', 90, 380, a="pop", t=0.0),
        words("Write it / on paper.", 250, 380, 800, t=0.05, cls="H", style="font-size:110px;text-align:left"),
        el('<div class="paper"><div class="hand" data-a="wipe" data-t="0.35" data-d="0.6">finish the deck</div></div>', 110, 760, 860,
           a="fly", t=0.05, d=0.45, r=-3),
        emoji("✍️", 760, 1080, 180, t=0.75, d=0.3, loop="wobble"),
    ]), tin="slam", cam="rise")
    r.scene(1.5, "".join([
        '<div class="par dots"></div>',
        el('<span class="num">2</span>', 90, 380, a="pop", t=0.0),
        words("Set a / *25-minute* timer.", 250, 380, 800, t=0.05, cls="H", style="font-size:110px;text-align:left"),
        img("ht-clock.png", 300, 850, 480, t=0.25, r=-6, loop="wobble", amp=0.5),
    ]), tin="whipL", cam="push")
    r.scene(2.5, "".join([
        '<div class="par dotsc"></div>',
        ring(540, 900, 380, "#EEE2A8", 44, t=-1, d=0.01),
        ring(540, 900, 380, pink, 44, t=0.05, d=1.3),
        el('<span data-a="count" data-t="0.05" data-d="1.3" data-from="1500" data-to="0" data-mmss="1">25:00</span>', "c", 760, a="none",
           cls="timer"),
        words("Only the *one thing.*", "c", 1360, t=0.2, cls="H", style="font-size:96px"),
    ]), tin="zoom", focus=(540, 900), cam="push")
    r.scene(1.5, "".join([
        '<div class="par dots"></div>',
        el('<span class="num">3</span>', "c", 400, a="pop", t=0.0),
        words("Then open / *email.*", "c", 580, t=0.05, cls="H", style="font-size:170px"),
        emoji("📬", 400, 1060, 280, t=0.35, d=0.35, loop="float"),
    ]), tin="iris", focus=(540, 900), color="#FFFFFF", cam="pull")
    r.scene(1.5, "".join([
        '<div class="par dotsc"></div>',
        words("It'll still / be *there.*", "c", 420, t=0.0, cls="H", style="font-size:160px"),
        el(inbox(-2, 0.01), 90, 860, a="up", t=0.1),
    ]), tin="push", cam="rise")
    r.scene(1.5, "".join([
        '<div class="par dotsp"></div>',
        words("Your first 25 / minutes go / to *you.*", "c", 560, t=0.0, gap=0.08, cls="H", em_cls="emy", style="font-size:150px"),
    ]), tin="flash", color="#FFD43B", color2="#FFFFFF", cam="push")
    r.scene(2, "".join([
        '<div class="par dots"></div>',
        words("Try it / *tomorrow.*", "c", 520, t=0.0, cls="H", style="font-size:180px"),
        el('<div class="B">Save this. Send it to the friend<br>who lives in their inbox.</div>', "c", 1000, a="up", t=0.4),
        img("ht-hourglass.png", 420, 1200, 240, t=0.5, r=8),
    ]), tin="whipR", cam="push")
    r.loop(1.5, tin="zoom", focus=(540, 650))
    return r


R["lh-reel-1016am-before-email"] = dict(make=lh_email, music="lh-focus-inst-01.mp3")


# =============================================================================================== Hourback
HB = BRANDS["hourback"]
HB_CSS = """
.H{font-family:Poppins;font-weight:700;letter-spacing:-.035em;line-height:1.02;color:#2A2238}
.Hw{font-family:Poppins;font-weight:700;letter-spacing:-.035em;line-height:1.02;color:#fff}
.em{background:linear-gradient(#FFC94D,#FFC94D) 0 90%/100% 40% no-repeat;padding:0 .05em}
.emo2{color:#FFC94D}
.plum{background:radial-gradient(circle, rgba(255,255,255,.07) 2px, transparent 2.6px) 0 0/34px 34px,#3A2240}
.indi{background:radial-gradient(circle, rgba(255,255,255,.09) 2px, transparent 2.6px) 0 0/34px 34px,#5E54C9}
.cream{background:radial-gradient(circle, rgba(42,34,56,.07) 2px, transparent 2.6px) 0 0/34px 34px,#FFF8EF}
.peach{background:radial-gradient(circle, rgba(42,34,56,.07) 2px, transparent 2.6px) 0 0/34px 34px,#FFE6D3}
.bub{border-radius:44px;padding:36px 44px;font:600 54px/1.28 Inter;max-width:880px;box-shadow:0 24px 50px rgba(0,0,0,.18)}
.them{background:#fff;color:#2A2238;border-bottom-left-radius:12px}
.me{background:#5E54C9;color:#fff;border-bottom-right-radius:12px}
.ai{background:#FFC94D;color:#2A2238;border-bottom-left-radius:12px}
.who{font:700 30px/1 Inter;opacity:.6;margin-bottom:14px;letter-spacing:.02em}
.send{display:inline-flex;align-items:center;gap:18px;background:#FF8A3D;color:#fff;font:700 80px/1 Poppins;padding:34px 64px;border-radius:999px;
  box-shadow:0 20px 40px rgba(255,138,61,.45)}
.pc{background:#5E54C9;border-radius:40px;padding:44px 48px;color:#fff;font:600 50px/1.35 Inter;box-shadow:0 30px 60px rgba(58,34,64,.3)}
.pc .k{display:inline-block;background:#fff;color:#5E54C9;font:800 28px/1 Inter;letter-spacing:.12em;padding:12px 18px;border-radius:999px;margin-bottom:22px}
.chipy{background:#FFC94D;color:#2A2238;border-radius:12px;padding:0 12px;font-weight:700}
.tag{display:inline-block;background:#2A2238;color:#FFC94D;font:800 28px/1 Inter;letter-spacing:.12em;padding:12px 18px;border-radius:999px}
.caret{display:inline-block;width:6px;height:58px;background:#FFC94D;vertical-align:-8px;margin-left:4px}
.fine{font:600 32px/1.3 Inter;color:#6B6080}
"""


def hb_chip(dark=True):
    return chip("hourback", "c", 250, bg="#FFF8EF" if dark else "#5E54C9", ink="#2A2238" if dark else "#FFFFFF", a="none")


def hb_calm():
    r = Reel("hb-reel-1016am-calm-reply", "hourback", bpm=108, css=HB_CSS, stage="#3A2240")
    yel, org = HB["acc"], HB["acc2"]
    them = ('<div class="bub them"><div class="who">Them · 8:47 am</div>Per my last email, this was due yesterday.</div>')
    hook = "".join([
        '<div class="par plum"></div>', hb_chip(),
        el('When this lands<br>before <span class="emo2">coffee:</span>', "c", 400, a="none", cls="Hw", style="font-size:120px"),
        el(them, 90, 800, 900, a="none", loop="float", amp=0.5),
        img("ht-cup.png", 700, 1180, 260, t=0.25, r=10),
        emoji("😤", 160, 1220, 220, t=0.45, d=0.3, loop="wobble"),
    ])
    r.scene(2, hook, cam="push", shake=(0.45, 0.2, 16))
    r.scene(1.5, "".join([
        '<div class="par cream"></div>',
        words("“Per my / *last email*”", "c", 560, t=0.0, gap=0.12, cls="H", style="font-size:170px"),
        scribble_circle(560, 860, 430, 120, org, 12, t=0.3, d=0.35),
        emoji("🙄", 400, 1120, 280, t=0.45, d=0.3, loop="wobble"),
    ]), tin="zoom", focus=(540, 900), cam="push")
    r.scene(2.5, "".join([
        '<div class="par plum"></div>',
        words("You, typing:", "c", 420, t=0.0, cls="Hw", style="font-size:120px"),
        el('<div class="bub me"><div class="who" style="color:#FFC94D;opacity:1">Your first draft</div>'
           '<span data-a="type" data-t="0.2" data-d="0.95">Actually, if you’d READ my email you’d know I never got it!!</span>'
           '<span class="caret"></span></div>', 90, 700, 900, a="up", t=0.05, loop="buzz", amp=0.5),
        emoji("😤", 420, 1280, 230, t=0.9, d=0.25, loop="buzz", amp=1.5),
    ]), tin="whipL", cam="tilt", shake=(1.0, 0.3, 14))
    r.scene(1, "".join([
        '<div class="par plum"></div>',
        el('<span class="send">Send ➤</span>', "c", 820, a="pop", t=0.0, loop="pulse", amp=1.5),
        img("ht-point.png", 560, 1050, 460, a="fly", t=0.05, d=0.35, r=-30, loop=None, shadow=True),
    ]), tin="cut", cam="push")
    r.scene(1, "".join([
        '<div class="par indi"></div>',
        el('WAIT.', "c", 640, a="stamp", t=0.0, d=0.22, cls="Hw", style="font-size:300px;color:#FFC94D"),
        emoji("✋", 400, 1060, 280, t=0.08, d=0.25, loop="shake"),
    ]), tin="glitch", td=0.18, cam="push", shake=(0.0, 0.3, 34))
    r.scene(1.5, "".join([
        '<div class="par cream"></div>',
        words("Don't send / *draft one.*", "c", 560, t=0.0, gap=0.12, cls="H", style="font-size:170px"),
        emoji("🙅", 420, 1060, 230, t=0.35, d=0.3, loop="wobble"),
    ]), tin="whipL", cam="push")
    prompt = ('<div class="pc"><span class="k">THE PROMPT · IN THE CAPTION</span><br>Here’s a message I got: <span class="chipy">[paste it]</span>. '
              'Here’s my draft: <span class="chipy">[paste it]</span>. Rewrite my reply so it’s calm and clear, keeps my point, under 80 words.</div>')
    r.scene(2, "".join([
        '<div class="par cream"></div>',
        words("Paste both into / *any AI chat.*", "c", 380, t=0.0, gap=0.08, cls="H", style="font-size:110px"),
        el(prompt, 80, 740, 920, a="fly", t=0.1, d=0.45, r=-2),
    ]), tin="whipU", cam="rise")
    r.scene(1.5, "".join([
        '<div class="par plum"></div>',
        el('<div class="bub me" style="font-size:58px"><div class="who" style="color:#FFC94D;opacity:1">Draft one</div>'
           'Actually, if you’d READ my email you’d know I never got it!!</div>', 90, 760, 900, a="none", loop="buzz", amp=0.6),
        words("Ask for the / *calm version.*", "c", 380, t=0.0, gap=0.1, cls="Hw", em_cls="emo2", style="font-size:110px"),
    ]), tin="push", cam="push")
    r.scene(3, "".join([
        '<div class="par plum"></div>',
        el('<span class="tag">CALM VERSION · EXAMPLE MADE UP</span>', "c", 470, a="pop", t=0.05),
        el('<div class="bub ai" style="font-size:58px"><div class="who">AI</div>Thanks for flagging. I didn’t receive it on Tuesday. '
           'Could you resend it? I’ll reply by 3 pm.</div>', 90, 600, 900, a="none", loop="float", amp=0.4),
        emoji("😌", 420, 1220, 240, t=0.45, d=0.35, loop="float"),
        el('<span class="tag" style="background:#5E54C9;color:#fff">SAME POINT. NO HEAT.</span>', "c", 1520, a="stamp", t=1.0, d=0.22, r=-3),
    ]), tin="pixel", td=0.4, cam="pull")
    r.scene(1.5, "".join([
        '<div class="par cream"></div>',
        words("Read it once. / Make it *sound like you.*", "c", 560, t=0.0, gap=0.08, cls="H", style="font-size:104px"),
        emoji("✏️", 420, 1060, 200, t=0.4, d=0.3, r=-10, loop="wobble"),
    ]), tin="whipL", cam="push")
    r.scene(1.5, "".join([
        '<div class="par indi"></div>',
        el('<div class="bub ai" style="font-size:44px;max-width:700px"><div class="who">You</div>Thanks for flagging. I didn’t receive it…</div>',
           260, 560, 760, a="right", t=0.0, d=0.3),
        el('<span style="font:700 40px/1 Inter;color:#FFC94D">Sent ✓✓</span>', 760, 860, a="pop", t=0.35),
        words("Same point. / *Zero regret.*", "c", 1080, t=0.3, gap=0.1, cls="Hw", em_cls="emo2", style="font-size:120px"),
    ]), tin="iris", focus=(540, 700), color=yel, cam="rise")
    r.scene(2, "".join([
        '<div class="par cream"></div>',
        words("Draft angry. / Send *calm.*", "c", 520, t=0.0, gap=0.12, cls="H", style="font-size:160px"),
        img("ht-cup.png", 410, 1000, 260, t=0.4, r=-8),
    ]), tin="stripes", color=yel, color2="#5E54C9", color3=org, cam="push")
    r.scene(2, "".join([
        '<div class="par indi"></div>',
        words("The prompt's / in the *caption.*", "c", 520, t=0.0, gap=0.1, cls="Hw", em_cls="emo2", style="font-size:140px"),
        arrow(540, 900, 540, 1250, "#FFC94D", 14, t=0.35, d=0.35, bend=40),
        el('<div class="fine" style="color:#E4DDF5">Save it for your next tricky reply.<br>Remove names before you paste.</div>', "c", 1320, a="up", t=0.5),
    ]), tin="whipU", cam="rise")
    r.loop(1.5, tin="flash", color=yel, color2=org)
    return r


R["hb-reel-1016am-calm-reply"] = dict(make=hb_calm, music="hb-playful-inst-01.mp3")


# =============================================================================================== build
def build(rid, outdir, qa_only=False, dsf=2):
    spec = R[rid]
    r = spec["make"]()
    work = Path(outdir) / rid
    if not qa_only:
        fdir, n = render_frames(r, work, dsf=dsf)
        out = work / f"{rid}.mp4"
        encode(fdir, n, MUSIC / spec["music"], out)
        pr = probe(out)
        lu = loudness(out)
        print(json.dumps(dict(id=rid, probe=pr, lufs=lu, cuts=[round(c, 2) for c in r.cuts()],
                              gaps=[round(b - a, 2) for a, b in zip([0] + r.cuts(), r.cuts() + [r.duration])])))
    fdir = work / "frames"
    sheet(fdir, qa_times(r), work / f"{rid}-qa.jpg", cols=10, scale=0.16)
    return r


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--out", default="/tmp/motion-out")
    ap.add_argument("--qa-only", action="store_true")
    ap.add_argument("--dsf", type=float, default=2)
    a = ap.parse_args()
    for i in a.ids or list(R):
        build(i, a.out, a.qa_only, a.dsf)

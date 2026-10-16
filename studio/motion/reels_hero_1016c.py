#!/usr/bin/env python3
"""Oct 16 hero samples, round 3 (Steadfold Creative Playbook): two signature formats, sold as outcomes.

    python3 studio/motion/reels_hero_1016c.py <id> --out DIR

ff-hero-1016-same-alarm   Fully Funded, "Same Alarm, Different Life"   signature format: THE MOVING LINE
                          (a split frame, today on top and the life it buys below; the coral divider carries the maths,
                          climbs as the age chip ticks 25 -> 65, and the future takes over the screen)
lf-hero-1016-ten-minutes  Littlefold, "Ten Minutes"                     signature format: THE NIGHT LIGHT
                          (berry-dark frame, a warm circle of lamp light carries each line and widens with every
                          helpful step until morning fills the screen)

Rules kept: clean floating text (very soft shadow, no plates), ElevenLabs v3 voice (one take, re-spaced phrase by phrase),
music ducked under the voice, master -14 LUFS, 1080x1920, under 19 MB, MP4s written outside the repo.

Footage (Pexels, free for commercial use, no attribution: https://www.pexels.com/license/):
  6963821  Close-Up View of Woman Turning off Alarm Clock https://www.pexels.com/video/close-up-view-of-woman-turning-off-alarm-clock-6963821/
  37293574 Serene Morning Coffee in the Sun             https://www.pexels.com/video/serene-morning-coffee-in-the-sun-37293574/
  855749   Time Lapse Video Of People At Subway Station https://www.pexels.com/video/time-lapse-video-of-people-at-subway-station-855749/
  37533808 Lone Walker on Beach at Sunrise              https://www.pexels.com/video/lone-walker-on-beach-at-sunrise-37533808/
  8730843  Person Walking With His Dog In the Beach     https://www.pexels.com/video/person-walking-with-his-dog-in-the-beach-8730843/
  5991819  Close-Up View of a Woman (hand to face)      https://www.pexels.com/video/close-up-view-of-a-woman-meditating-5991819/
  8486629  Tired Woman Entering the House and Sitting   https://www.pexels.com/video/tired-woman-entering-the-house-and-sitting-on-a-chair-8486629/
  5823594  A Bedroom Interior                           https://www.pexels.com/video/a-bedroom-interior-5823594/
  2108274  Person Opening And Closing The Door          https://www.pexels.com/video/person-opening-and-closing-the-door-2108274/
  5835697  A Woman Opening a Window                     https://www.pexels.com/video/a-woman-opening-a-window-5835697/
Money maths: ff_math() ($200 a month for 480 months, age 25 to 65, at 8% a year, monthly compounding).
Parenting fact: NHS, Soothing a crying baby, https://www.nhs.uk/baby/caring-for-a-newborn/soothing-a-crying-baby/
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reels_hero_1016 as H  # noqa: E402
from kit import FPS, asset, el, probe, qa_times, reading_report, render_frames, sheet, words  # noqa: E402

REPO = HERE.parent.parent
LIB = REPO / "media" / "music" / "library"
VOICE = REPO / "media" / "voice" / "hero3"
H.CACHE = Path(os.environ.get("HERO_CACHE", "/tmp/hero-footage"))
ft = H.ft
R = {}

H.CLIPS.update({
    # Fully Funded: today (cool) on top, the life it buys (warm) below
    "alarm": ("px-6963821.mp4", "scale=-2:1240:flags=lanczos,crop=1080:960:(iw-1080)*0.40:(ih-960)*0.95",
              "eq=contrast=1.06:saturation=0.78:brightness=-0.05,colorbalance=rs=-.04:bs=.06:rm=-.02:bm=.04"),
    "subway": ("px-855749.mp4", "scale=-2:960:flags=lanczos,crop=1080:960:(iw-1080)*0.30:0",
               "eq=contrast=1.1:saturation=0.75:brightness=-0.04,colorbalance=rs=-.05:bs=.07"),
    "cup": ("px-37293574.mp4", "scale=1080:1920:flags=lanczos",
            "eq=contrast=1.06:saturation=1.05:brightness=-0.07,colorbalance=rs=.05:gs=.01:bs=-.04:rh=.03"),
    "walker": ("px-37533808.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920",
               "eq=contrast=1.07:saturation=1.08:brightness=-0.05,colorbalance=rs=.05:bs=-.02:rh=.03:bh=-.02"),
    "dog": ("px-8730843.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920:(iw-1080)*0.70:0",
            "eq=contrast=1.04:saturation=1.08,colorbalance=rs=.05:bs=-.03:rh=.02"),
    # Littlefold: night, graded warm (peach lights, berry shadows)
    "face": ("px-5991819.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920:(iw-1080)*0.46:0",
             "eq=contrast=1.05:saturation=0.88:brightness=-0.10:gamma=0.92,colorbalance=rs=.08:gs=-.01:bs=.0:rm=.06:bm=-.02"),
    "sit": ("px-8486629.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920:(iw-1080)*0.56:0",
            "eq=contrast=1.05:saturation=0.9:brightness=-0.06:gamma=0.95,colorbalance=rs=.07:gs=-.01:bs=.01:rm=.05:bm=-.02"),
    "enter": ("px-8486629.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920:(iw-1080)*0.24:0",
              "eq=contrast=1.05:saturation=0.9:brightness=-0.04,colorbalance=rs=.07:gs=-.01:bs=.01:rm=.05:bm=-.02"),
    "bedroom": ("px-5823594.mp4", "scale=1080:1920:flags=lanczos",
                "eq=contrast=1.08:saturation=0.75:brightness=-0.20:gamma=0.85,colorbalance=rs=.06:bs=.02:rm=.04"),
    "sunroom": ("px-5823594.mp4", "scale=1080:1920:flags=lanczos",
                "eq=contrast=1.0:saturation=0.9:brightness=-0.06,colorbalance=rs=.04:bs=.01:rh=.02"),
    "door": ("px-2108274.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920:(iw-1080)*0.05:0",
             "eq=contrast=1.04:saturation=0.92:brightness=-0.05,colorbalance=rs=.07:bs=-.01:rm=.04:bm=-.02"),
    "window": ("px-5835697.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920:(iw-1080)*0.38:0",
               "eq=contrast=1.03:saturation=0.95:brightness=-0.03,colorbalance=rs=.06:bs=-.02:rm=.04"),
})

# extra time-driven moves on top of the hero seek wrapper:
#   data-split="t0,d,from,to"  sets --sy (px) on the element: the Moving Line's divider position
#   data-light="t0,d,r0,r1"    sets --r (px): the Night Light circle radius
SPLIT_WRAP = """
<script>(function(){
const S = window.__STARTS, scs=[...document.querySelectorAll('.scene')], _s = window.seek;
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)), io=p=>(p<.5?4*p*p*p:1-Math.pow(-2*p+2,3)/2);
window.seek = function(t){
  return Promise.resolve(_s(t)).then(r=>{
    scs.forEach((sc,i)=>{
      if (sc.style.display!=='block') return;
      const u = Math.max(0, t - S[i]);
      sc.querySelectorAll('[data-split]').forEach(e=>{ const [t0,d,a,b]=e.dataset.split.split(',').map(Number);
        e.style.setProperty('--sy', (a+(b-a)*io(cl((u-t0)/d))).toFixed(1)+'px'); });
      sc.querySelectorAll('[data-light]').forEach(e=>{ const [t0,d,a,b]=e.dataset.light.split(',').map(Number);
        e.style.setProperty('--r', (a+(b-a)*io(cl((u-t0)/d))).toFixed(1)+'px'); });
    });
    return r;
  });
};})();</script>
"""


class CReel(H.HReel):
    def html(self):
        return super().html().replace("</body>", SPLIT_WRAP + "</body>")


# ---------------------------------------------------------------------------------------------- voice + sound helpers
SOFT = "text-shadow:0 4px 28px rgba(0,0,0,.30),0 1px 3px rgba(0,0,0,.18)"
BASE = H.EXTRA_CSS + f"""
.HD{{font-family:'Inter Display';font-weight:800;color:#fff;letter-spacing:-.035em;line-height:.98;{SOFT}}}
.SR{{font-family:'Instrument Serif';color:#fff;line-height:1;{SOFT}}}
"""


def word_times(name):
    d = json.load(open(VOICE / f"{name}.json"))
    a = d.get("normalized_alignment") or d["alignment"]
    out, cur, ws, we = [], [], None, None
    for c, st, en in zip(a["characters"], a["character_start_times_seconds"], a["character_end_times_seconds"]):
        if not c.strip():
            if cur:
                out.append(("".join(cur), ws, we))
                cur = []
            continue
        if not cur:
            ws = st
        cur.append(c)
        we = en
    if cur:
        out.append(("".join(cur), ws, we))
    return out


def place_vo(name, plan, out, tempo=1.0):
    """plan: [(first_word, last_word, t[, end_override_s])]. Cuts each phrase from the one take and places it at t.
    end_override trims trailing silence inside a drawn-out word (measured from the take's energy)."""
    ws = word_times(name)
    ins, fc, spans = [], [], []
    for k, ph in enumerate(plan):
        a, b, t = ph[:3]
        s0 = max(0.0, ws[a][1] - 0.07)
        e = ws[b][2] + 0.16
        if b + 1 < len(ws):
            e = min(e, ws[b + 1][1] - 0.03)
        if len(ph) > 3:
            e = ph[3]
        ins += ["-i", str(VOICE / f"{name}.mp3")]
        ms = int(t * 1000)
        fc.append(f"[{k}:a]atrim={s0:.3f}:{e:.3f},asetpts=PTS-STARTPTS,atempo={tempo},afade=t=in:d=0.02,"
                  f"afade=t=out:st={max(0.0, (e - s0) / tempo - 0.08):.3f}:d=0.08,adelay={ms}|{ms}[v{k}]")
        spans.append((round(t, 2), round(t + (e - s0) / tempo, 2), " ".join(w[0] for w in ws[a:b + 1])))
    fc.append("".join(f"[v{k}]" for k in range(len(plan))) + f"amix=inputs={len(plan)}:normalize=0[a]")
    subprocess.run(["ffmpeg", "-y", "-v", "error", *ins, "-filter_complex", ";".join(fc), "-map", "[a]", "-ar", "44100",
                    "-ac", "2", str(out)], check=True)
    return spans


def duck_expr(spans, low=0.42):
    return f"if(gt({'+'.join(f'between(t,{a - 0.1:.2f},{b + 0.15:.2f})' for a, b, _ in spans)},0),{low},1)"


def trimmed(sfx, dur, out):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(LIB / f"{sfx}.mp3"), "-af",
                    f"atrim=0:{dur},afade=t=out:st={max(0, dur - 0.6)}:d=0.6", str(out)], check=True)
    return out


# ============================================================================================== FULLY FUNDED
def ff_math():
    b = 0.0
    for _ in range(480):
        b = b * (1 + 0.08 / 12) + 200
    return round(b), 200 * 480


FF_CSS = BASE + f"""
.SR i{{color:#fff}}
.cor{{color:#fff;font-family:'Instrument Serif';font-style:italic;font-weight:400;letter-spacing:-.01em;font-size:1.12em}}
.nw{{white-space:nowrap}}
.split{{position:absolute;inset:0;--sy:960px}}
.topP{{position:absolute;left:0;top:calc(var(--sy) - 960px);width:1080px;height:960px;overflow:hidden}}
.topP .ft{{height:960px}}
.botP{{position:absolute;inset:0;clip-path:inset(var(--sy) 0 0 0)}}
.line{{position:absolute;left:0;width:1080px;top:calc(var(--sy) - 4px);height:8px;background:#FF6A3D;
  box-shadow:0 0 26px rgba(255,106,61,.55)}}
.ride{{position:absolute;top:calc(var(--sy) - 46px);height:92px}}
.pill{{display:inline-block;background:#FF6A3D;color:#fff;font:800 70px/92px 'Inter Display';letter-spacing:-.02em;
  padding:0 42px;border-radius:46px;box-shadow:0 14px 34px rgba(14,20,64,.28);white-space:nowrap}}
.age{{display:inline-block;background:#F7F1E5;color:#0E1440;font:800 38px/92px Inter;letter-spacing:.08em;padding:0 30px;
  border-radius:46px;box-shadow:0 14px 34px rgba(14,20,64,.28);white-space:nowrap}}
  .age b{{font:800 62px/92px 'Inter Display';letter-spacing:-.02em;color:#2B3FE0;margin-left:10px}}
.tl{{font:800 46px/1 Inter;letter-spacing:.14em;color:#fff;{SOFT}}}
.big{{font:800 230px/1 'Inter Display';color:#fff;letter-spacing:-.05em;{SOFT};white-space:nowrap}}
.pre{{font:800 64px/1 'Inter Display';color:#fff;letter-spacing:-.02em;{SOFT}}}
.cool{{position:absolute;inset:0;background:linear-gradient(rgba(16,32,107,.18),rgba(16,32,107,.05))}}
"""


def ff_split(top, top_off, bot, bot_off, split="0,0.01,960,960", extra_top="", extra_bot="", ride=""):
    return (f'<div class="split" data-split="{split}">'
            f'<div class="botP">{ft(bot, bot_off)}{extra_bot}</div>'
            f'<div class="topP">{ft(top, top_off)}<div class="cool"></div>{extra_top}</div>'
            f'<div class="line"></div>{ride}</div>')


def ff_hook():
    return ff_split("alarm", 0.6, "cup", 0.0,
                    extra_top=el('<div class="HD nw" style="font-size:150px">Same alarm.</div>', "c", 380, a="none"),
                    extra_bot=el('<div class="SR nw" style="font-size:190px"><i>Different life.</i></div>', "c", 1240, a="none"),
                    ride=f'<div class="ride" style="left:404px" data-a="pop" data-t="0.12" data-d="0.35">'
                         f'<span class="age">AGE<b>25</b></span></div>')


def ff_same_alarm():
    total, paid = ff_math()
    r = CReel("ff-hero-1016-same-alarm", "fullyfunded", bpm=60, css=FF_CSS, stage="#0E1440")
    # 1 hook (0-2.6): split frame, alarm on top / slow coffee below; both lines readable at 0.0 s
    r.scene(3.0, ff_hook(), cam="push")
    # 2 (2.6-5.4): commute on top; "$200 a month" lands ON the line, then "from 25"
    ride = ('<div class="ride" style="left:0;width:1080px;text-align:center" data-a="stamp" data-t="0.25" data-d="0.32" data-r="-2">'
            '<span class="pill">$200 a month</span></div>')
    r.scene(3.1, ff_split("subway", 0.0, "cup", 3.0,
                          extra_bot=words("from age *25.*", "c", 1250, t=1.4, gap=0.12, cls="HD", em_cls="cor",
                                          style="font-size:120px"),
                          ride=ride),
            tin="slit", color="#FF6A3D", color2="#F7F1E5", cam="rise")
    # 3 (5.4-8.4): THE MOVING LINE. Divider climbs 960 -> 300, age ticks 25 -> 65, the beach takes the frame
    age = ('<div class="ride" style="left:330px" data-a="none">'
           '<span class="age">AGE<b data-a="tick" data-t="0.35" data-d="2.5" data-from="25" data-to="65">25</b></span></div>')
    r.scene(3.4, ff_split("subway", 3.1, "walker", 0.0, split="0.3,2.6,960,420",
                          extra_bot=words("Every year, / *the line moves.*", "c", 1330, t=0.25, gap=0.12, cls="HD",
                                          em_cls="cor", style="font-size:110px"),
                          ride=age),
            tin="cut", cam="pull", shake=(0.02, 0.22, 10))
    # 4 (8.4-11.4): full frame sunrise; the number rolls from what you paid in to what time made
    big = (f'<div class="tl">8% A YEAR, BY 65</div><div class="pre" style="margin-top:34px">about</div>'
           f'<div class="big">$<span data-a="count" data-t="0.7" data-d="1.8" data-from="{paid // 1000}" '
           f'data-to="{round(total / 1000, -1):.0f}">{paid // 1000}</span>K</div>')
    r.scene(4.2, "".join([ft("walker", 3.4), el(big, "c", 560, a="up", t=0.05, d=0.4)]),
            tin="zoom", focus=(540, 360), cam="push")
    # 5 (11.4-13.2): you put in $96K
    r.scene(2.2, "".join([ft("cup", 5.5), words(f"You put in / *${paid // 1000}K.*", "c", 360, t=0.1, gap=0.12, cls="HD",
                                                  em_cls="cor", style="font-size:140px")]),
            tin="flash", td=0.45, color="#FFB08F", color2="#FFF4E0", cam="pull")
    # 6 (13.2-16.2): time bought the mornings
    r.scene(3.0, "".join([ft("dog", 1.0), words("Time bought / *the mornings.*", "c", 360, t=0.15, gap=0.14, cls="HD",
                                                 em_cls="cor", style="font-size:128px"),
                          el(f'<img src="{asset(H.FF["mark"])}" style="width:120px;height:120px;border-radius:50%;background:#fff;'
                             'box-shadow:0 8px 30px rgba(0,0,0,.25)">', "c", 1290, a="pop", t=1.5)]),
            tin="iris", color="#FF6A3D", color2="#F7F1E5", focus=(540, 1500), cam="push")
    r.loop(0.6, tin="whipL")
    plan = [(0, 1, 0.1), (2, 3, 2.08), (4, 7, 3.15), (8, 9, 4.4), (10, 14, 6.25), (15, 17, 8.05), (18, 23, 9.6),
            (24, 27, 13.85), (28, 31, 16.05)]
    return r, dict(voice=("ff-same-alarm-t2", plan, 1.06), music=LIB / "v3" / "ff-c-confident-build-el.mp3",
                   sfx=[("sfx-phone-buzz", 1.4, 0.0, -14), ("sfx-whoosh-soft", 0.85, 2.9, -13), ("sfx-city-rush", 3.1, 3.0, -16),
                        ("sfx-tick-ding", 1.04, 6.05, -14), ("sfx-whoosh-fast", 0.8, 9.4, -16), ("sfx-waves", 6.0, 9.5, -10),
                        ("sfx-cash", 0.9, 11.6, -16), ("sfx-waves", 5.5, 15.8, -12)])


R["ff-hero-1016-same-alarm"] = ff_same_alarm


# ============================================================================================== LITTLEFOLD
LF_CSS = BASE + """
.nl{position:absolute;inset:0;--r:420px;pointer-events:none;
  background:radial-gradient(circle at var(--cx,540px) var(--cy,980px), rgba(42,15,37,0) 0, rgba(42,15,37,0) var(--r),
  rgba(42,15,37,.80) calc(var(--r) + 380px))}
.glow{position:absolute;inset:0;pointer-events:none;mix-blend-mode:screen;
  background:radial-gradient(circle at var(--cx,540px) var(--cy,980px), rgba(255,190,140,.22) 0, rgba(255,190,140,0) calc(var(--r) + 120px))}
.nhs{display:inline-block;font:800 52px/1 Inter;letter-spacing:.24em;color:#FFD3AE;""" + SOFT + """}
.H2{font-family:Lora;font-weight:600;color:#FFF4E0;letter-spacing:-.02em;line-height:1.06;
  text-shadow:0 4px 28px rgba(42,15,37,.42),0 1px 3px rgba(42,15,37,.22)}
.H2 .em{font-style:italic;color:#FFD6E3}
.H2.inkm{color:#2C2A3A;text-shadow:0 2px 24px rgba(255,248,236,.85),0 1px 2px rgba(255,248,236,.6)}
.H2.inkm .em{color:#B8325E}
.ring10{font:600 150px/1 Lora;color:#FFF4E0;font-variant-numeric:tabular-nums;""" + SOFT + """}
.morning{position:absolute;inset:0;background:radial-gradient(130% 90% at 50% 100%,rgba(255,211,174,.55),rgba(255,244,224,.2) 60%,rgba(255,244,224,0))}
"""


def night(r0, r1=None, t0=0.0, d=1.0, cx=540, cy=980):
    r1 = r0 if r1 is None else r1
    st = f"--cx:{cx}px;--cy:{cy}px"
    return (f'<div class="nl" style="{st}" data-light="{t0},{d},{r0},{r1}"></div>'
            f'<div class="glow" style="{st}" data-light="{t0},{d},{r0},{r1}"></div>')


def lf_hook():
    return "".join([ft("face", 0.5), night(380, 440, 0.0, 2.6, cy=1150),
                    el('<div class="H2" style="font-size:150px">Hour two</div>'
                       '<div class="H2" style="font-size:150px;margin-top:6px"><span class="em">of crying.</span></div>', "c", 330,
                       a="none")])


def lf_ten_minutes():
    r = CReel("lf-hero-1016-ten-minutes", "littlefold", bpm=60, css=LF_CSS, stage="#2A0F25")
    mark = (f'<img src="{asset(H.LF["mark"])}" style="width:116px;height:116px;border-radius:50%;background:#fff;'
            'box-shadow:0 10px 30px rgba(122,33,73,.25)">')
    # 1 hook (0-2.6): a tired parent, hand to face, inside the circle of lamp light
    r.scene(2.6, lf_hook(), cam="push")
    # 2 (2.6-4.4): running on empty
    r.scene(1.8, "".join([ft("sit", 28.0), night(340, 420, 0.0, 1.6, cy=1150),
                          words("Running / on *empty.*", "c", 360, t=0.05, gap=0.12, cls="H2", style="font-size:150px")]),
            tin="blob", color="#7A2149", focus=(540, 1250), cam="pull")
    # 3 (4.4-6.8): what the NHS says
    r.scene(2.4, "".join([ft("window", 0.0), night(380, 460, 0.0, 2.2, cy=900),
                          el('<span class="nhs">NHS</span>', "c", 330, a="up", t=0.05),
                          words("If it's / *too much:*", "c", 440, t=0.3, gap=0.12, cls="H2", style="font-size:150px")]),
            tin="push", cam="rise")
    # 4 (6.8-9.4): baby safe in the cot
    r.scene(2.6, "".join([ft("bedroom", 0.5), night(440, 520, 0.0, 2.4, cy=1150),
                          words("Baby safe / *in the cot.*", "c", 360, t=0.15, gap=0.12, cls="H2", style="font-size:140px")]),
            tin="blob", color="#FFD3AE", focus=(540, 1150), cam="push")
    # 5 (9.4-11.2): close the door
    r.scene(1.8, "".join([ft("door", 4.2), night(520, 580, 0.0, 1.6, cy=1000),
                          words("Close / *the door.*", "c", 360, t=0.05, gap=0.1, cls="H2", style="font-size:150px")]),
            tin="cut", cam="push", shake=(0.05, 0.18, 6))
    # 6 (11.2-14.2): another room, ten minutes, breathe; the timer starts
    timer = '<div class="ring10" data-a="tick" data-t="1.0" data-d="2.0" data-from="600" data-to="598" data-mmss="1">10:00</div>'
    r.scene(3.0, "".join([ft("window", 8.0), night(600, 760, 0.0, 2.8, cy=1000),
                          words("Another room.", "c", 330, t=0.05, gap=0.1, cls="H2", style="font-size:110px"),
                          words("*Ten minutes.*", "c", 500, t=0.95, gap=0.12, cls="H2", style="font-size:150px"),
                          el(timer, "c", 1240, a="pop", t=0.95, d=0.35),
                          words("Breathe.", "c", 690, t=1.9, gap=0.1, cls="H2", style="font-size:120px")]),
            tin="slam", cam="rise")
    # 7 (14.2-16.0): then go back
    r.scene(1.8, "".join([ft("enter", 0.3), night(760, 900, 0.0, 1.6, cy=1100),
                          words("Then / *go back.*", "c", 360, t=0.05, gap=0.12, cls="H2", style="font-size:150px")]),
            tin="flash", td=0.45, color="#FFD3AE", color2="#FFF4E0", cam="push")
    # 8 (16.0-19.2): morning floods the frame
    r.scene(3.2, "".join([ft("sunroom", 9.0), night(900, 1700, 0.0, 1.6, cy=1000), '<div class="morning"></div>',
                          words("Stepping out / isn't *giving up.*", "c", 330, t=0.1, gap=0.1, cls="H2 inkm", style="font-size:124px"),
                          el(mark, "c", 1300, a="pop", t=1.6)]),
            tin="iris", color="#FFD6E3", color2="#FFF4E0", focus=(540, 1000), cam="pull")
    r.loop(0.6, tin="blob", color="#7A2149", focus=(540, 1000))
    plan = [(0, 3, 0.1, 2.2), (4, 8, 2.05), (9, 13, 3.4), (14, 19, 5.15), (20, 25, 7.0), (26, 28, 9.5), (29, 32, 10.65),
            (33, 34, 12.15), (35, 35, 13.1), (36, 38, 14.4), (39, 43, 16.1, 18.55), (44, 49, 17.5)]
    return r, dict(voice=("lf-ten-minutes-t2", plan, 1.06), music=LIB / "v3" / "lf-b-tender-el.mp3",
                   sfx=[("amb-room-tone", 19.0, 0.0, -20), ("sfx-whoosh-soft", 0.85, 2.5, -18), ("sfx-door-open", 1.2, 9.4, -14),
                        ("sfx-rain-window", 4.0, 11.2, -22), ("sfx-tick-ding", 1.04, 12.1, -16)])


R["lf-hero-1016-ten-minutes"] = lf_ten_minutes


# ============================================================================================== build
def build(rid, outdir, qa_only=False, dsf=2):
    r, snd = R[rid]()
    work = Path(outdir) / rid
    work.mkdir(parents=True, exist_ok=True)
    for x in reading_report(r):
        if not x["ok"]:
            print("READ", x)
    name, plan, tempo = snd["voice"]
    vo = work / f"{rid}-vo.wav"
    spans = place_vo(name, plan, vo, tempo)
    print(json.dumps(dict(spans=spans, cuts=[round(c, 2) for c in r.cuts()], dur=round(r.duration, 2))))
    if not qa_only:
        fdir, n = render_frames(r, work, dsf=dsf)
        silent = work / f"{rid}.silent.mp4"
        H.encode_silent(fdir, n, silent)
        cues = [(vo, 0.0, 2.0, 12000)]
        for k, (s, d, t, g) in enumerate(snd["sfx"]):
            cues.append((trimmed(s, d, work / f"sfx{k}.wav"), t, g, 8000))
        out = work / f"{rid}.mp4"
        lu = H.mix(silent, out, snd["music"], cues, n / FPS, music_gain=-6, duck=duck_expr(spans), fade=1.0)
        silent.unlink()
        print(json.dumps(dict(id=rid, probe=probe(out), lufs=lu, size_mb=round(out.stat().st_size / 1e6, 2))))
    fdir = work / "frames"
    sheet(fdir, qa_times(r), work / f"{rid}-qa.jpg", cols=10, scale=0.16)
    return r


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--out", required=True)
    ap.add_argument("--qa-only", action="store_true")
    ap.add_argument("--dsf", type=float, default=2)
    a = ap.parse_args()
    for i in a.ids or list(R):
        build(i, a.out, a.qa_only, a.dsf)

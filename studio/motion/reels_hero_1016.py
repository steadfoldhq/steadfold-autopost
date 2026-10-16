#!/usr/bin/env python3
"""Oct 16 HERO Reels (creative director pass): real footage + code-built cinema + sound design, cut with the motion kit.

    python3 studio/motion/reels_hero_1016.py <id> [--out DIR] [--qa-only]

What this adds to the kit:
- `ft(...)`: real stock footage as a layer. The clip is pre-extracted to graded JPEG frames (ffmpeg, cached in --cache),
  and a seek() wrapper swaps the frame for the scene's local time, so rendering stays deterministic (motion blur works).
- `data-door`, `data-spill`, `data-drift`, `data-blink`: small time-driven moves (door swing, light spill, dust, clock colon).
- `mix()`: music bed (trimmed/extended) + timed SFX and voice, low-passed, ducked, then mastered to -14 LUFS.

Footage (all Pexels, free for commercial use, no attribution: https://www.pexels.com/license/):
  28968243 Peaceful Ocean Waves at Sunset   https://www.pexels.com/video/peaceful-ocean-waves-at-sunset-28968243/
  37700770 City Night Traffic from Above    https://www.pexels.com/video/city-night-traffic-timelapse-from-above-37700770/
  34689939 Tranquil Morning Mist over Lake  https://www.pexels.com/video/tranquil-morning-mist-over-serene-lake-34689939/
  35180821 Raindrops on Window, City Bokeh  https://www.pexels.com/video/raindrops-on-window-with-city-lights-bokeh-35180821/
Money figures: computed in ff_math() below (100 a month for 216 months, then held 564 months, monthly compounding).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from kit import (BRANDS, FPS, Reel, asset, el, emoji, img, loudness, master_audio, probe, qa_times, render_frames,  # noqa: E402
                 ring, sheet, words)

REPO = HERE.parent.parent
INBOX = REPO / "assets" / "inbox"
LIB = REPO / "media" / "music" / "library"
VOICE = REPO / "media" / "voice" / "hero"
CACHE = Path("/tmp/hero-footage")
R = {}

# ---------------------------------------------------------------------------------------------- footage
CLIPS = {
    # name: (source, crop/scale filter, grade)
    "ocean": ("px-28968243.mp4", "scale=1080:1920",
              "eq=contrast=1.07:saturation=1.12:brightness=0.01,colorbalance=rs=.05:gs=.015:bs=-.05:rm=.03:bm=-.02"),
    "traffic": ("px-37700770.mp4", "scale=1296:2304:flags=lanczos",
                "eq=contrast=1.12:saturation=1.15:brightness=-0.02"),
    "lake": ("px-34689939.mp4", "scale=1080:1920",
             "eq=contrast=1.04:saturation=0.95:brightness=0.03:gamma=1.04,colorbalance=rs=.04:bs=-.03:rh=.03:bh=-.02"),
    "rain": ("px-35180821.mp4", "scale=1296:2304:flags=lanczos",
             "eq=contrast=1.05:saturation=1.05:brightness=-0.03,colorbalance=rs=.08:gs=-.01:bs=-.04:rm=.06:bm=-.03"),
}


def prep(name):
    """Extract a clip to graded 30 fps JPEG frames (cached). Returns (file-uri dir, frame count)."""
    src, geo, grade = CLIPS[name]
    out = CACHE / name
    if not (out / "00001.jpg").exists():
        out.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(INBOX / src), "-vf", f"fps=30,{geo},{grade}",
                        "-q:v", "3", str(out / "%05d.jpg")], check=True)
    return out.as_uri(), len(list(out.glob("*.jpg")))


def ft(name, off=0.0, sp=1.0, style="", cls=""):
    d, n = prep(name)
    return (f'<img class="ft {cls}" src="{d}/{max(1, int(off * 30) + 1):05d}.jpg" data-dir="{d}" data-n="{n}" '
            f'data-off="{off}" data-sp="{sp}" style="{style}">')


EXTRA_CSS = """
.ft{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.scrimT{position:absolute;left:0;right:0;top:0;height:1250px;background:linear-gradient(rgba(8,12,40,.8),rgba(8,12,40,.55) 55%,rgba(8,12,40,0))}
.scrimA{position:absolute;inset:0;background:rgba(8,10,30,.38)}
.grain{position:absolute;inset:0;background:radial-gradient(120% 90% at 50% 45%,rgba(0,0,0,0) 55%,rgba(0,0,0,.45));pointer-events:none}
"""

SEEK_WRAP = """
<script>(function(){
const S = window.__STARTS, scs=[...document.querySelectorAll('.scene')], _s = window.seek;
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)), io=p=>(p<.5?4*p*p*p:1-Math.pow(-2*p+2,3)/2);
window.seek = function(t){
  const r = _s(t), ps = [];
  scs.forEach((sc,i)=>{
    if (sc.style.display!=='block') return;
    const u = Math.max(0, t - S[i]);
    sc.querySelectorAll('img.ft').forEach(im=>{
      const n=+im.dataset.n; let f=Math.floor((u*(+im.dataset.sp)+(+im.dataset.off))*30);
      f=Math.max(0,Math.min(n-1,f));
      const src=im.dataset.dir+'/'+String(f+1).padStart(5,'0')+'.jpg';
      if (im.getAttribute('src')!==src){ im.src=src; ps.push(im.decode().catch(()=>{})); }
    });
    sc.querySelectorAll('[data-door]').forEach(e=>{ const [t0,d]=e.dataset.door.split(',').map(Number);
      e.style.transform=`rotateY(${-104*io(cl((u-t0)/d))}deg)`; });
    sc.querySelectorAll('[data-spill]').forEach(e=>{ const [t0,d]=e.dataset.spill.split(',').map(Number);
      e.style.opacity=(+(e.dataset.base||0))+(1-(+(e.dataset.base||0)))*io(cl((u-t0)/d)); });
    sc.querySelectorAll('[data-drift]').forEach(e=>{ const [vx,vy,ph]=e.dataset.drift.split(',').map(Number);
      e.style.transform=`translate(${vx*t+Math.sin(t*1.3+ph)*14}px,${vy*t+Math.cos(t*1.1+ph)*10}px)`;
      e.style.opacity=.35+.35*Math.sin(t*2+ph); });
    sc.querySelectorAll('[data-out]').forEach(e=>{ const [t0,d]=e.dataset.out.split(',').map(Number);
      e.style.opacity=1-io(cl((u-t0)/d)); });
    sc.querySelectorAll('[data-blink]').forEach(e=>{ e.style.opacity=(Math.floor(t*1.6)%2)?.25:1; });
  });
  return Promise.all(ps).then(()=>r);
};})();</script>
"""


class HReel(Reel):
    def html(self):
        h = super().html()
        starts = json.dumps([s["start"] for s in self.scenes])
        return h.replace("</body>", f"<script>window.__STARTS={starts};</script>{SEEK_WRAP}</body>")


# ---------------------------------------------------------------------------------------------- sound
def mix(video, out, music, cues, dur, music_from=0.0, music_gain=0.0, duck=None, extend=None, fade=1.3, eq=None):
    """music: library mp3; cues: [(path, t, gain_db, lowpass_hz)]; duck: ffmpeg volume expression on the bed;
    extend: (cut_at, xfade, restart_from) to lengthen the bed with a crossfade back into itself."""
    inputs = ["-i", str(video), "-i", str(music)]
    fc = []
    if extend:
        cut, xf, rs = extend
        inputs += ["-i", str(music)]
        fc.append(f"[1:a]atrim={music_from}:{cut},asetpts=PTS-STARTPTS[m1];[2:a]atrim={rs},asetpts=PTS-STARTPTS[m2];"
                  f"[m1][m2]acrossfade=d={xf}:c1=tri:c2=tri[mb]")
    else:
        fc.append(f"[1:a]atrim={music_from},asetpts=PTS-STARTPTS[mb]")
    vol = f"volume={music_gain}dB" + (f",{eq}" if eq else "")
    if duck:
        vol += f",volume='{duck}':eval=frame"
    fc.append(f"[mb]{vol},apad,atrim=0:{dur:.3f}[bed]")
    labels = ["[bed]"]
    for k, (p, t, g, lp) in enumerate(cues):
        idx = len(inputs) // 2
        inputs += ["-i", str(p)]
        ms = int(t * 1000)
        fc.append(f"[{idx}:a]aformat=channel_layouts=stereo,aresample=44100,lowpass=f={lp},volume={g}dB,adelay={ms}|{ms},apad,"
                  f"atrim=0:{dur:.3f}[c{k}]")
        labels.append(f"[c{k}]")
    fc.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:duration=first,"
              f"afade=t=in:st=0:d=0.03,afade=t=out:st={dur - fade:.3f}:d={fade},lowpass=f=9500,alimiter=limit=0.89[a]")
    subprocess.run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", ";".join(fc), "-map", "0:v", "-map", "[a]",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-ar", "44100", "-movflags", "+faststart", str(out)], check=True)
    return master_audio(out)


def encode_silent(fdir, n, out, crf=20):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", f"{fdir}/%05d.png", "-frames:v", str(n),
                    "-c:v", "libx264", "-preset", "slow", "-crf", str(crf), "-maxrate", "9M", "-bufsize", "18M",
                    "-pix_fmt", "yuv420p", "-profile:v", "high", "-g", "30", str(out)], check=True)


SFX = lambda n: LIB / f"{n}.mp3"  # noqa: E731


# ============================================================================================== FULLY FUNDED: The Door
def ff_math():
    def run(rate, amt=100, m_in=216, m_hold=564):
        r, b = rate / 12, 0.0
        for _ in range(m_in):
            b = b * (1 + r) + amt
        at18 = b
        for _ in range(m_hold):
            b *= 1 + r
        return round(at18), round(b)
    m = {k: run(k / 100) for k in (6, 8, 10)}
    paid = 100 * 216
    today = round(m[8][1] / 1.025 ** 65)  # 8% result in today's money if inflation averages 2.5% a year for 65 years
    return m, paid, today


FF = BRANDS["fullyfunded"]
FF_CSS = EXTRA_CSS + """
.HD{font-family:'Inter Display';font-weight:800;color:#fff;letter-spacing:-.035em;line-height:.98}
.SR{font-family:'Instrument Serif';color:#fff;line-height:1}
.SR i,.cor{color:#FFB08F}
.B{font:600 46px/1.3 Inter;color:#0E1440}
.pill{display:inline-block;font:800 34px/1 Inter;letter-spacing:.12em;color:#fff;background:#FF6A3D;padding:16px 26px;border-radius:999px}
.room{position:absolute;inset:0;background:radial-gradient(70% 45% at 50% 62%,#24308A 0%,#121A55 45%,#070B2A 100%)}
.wall{position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.025) 0 2px,transparent 2px 120px)}
.floor{position:absolute;left:0;right:0;top:1520px;bottom:0;background:linear-gradient(#0B1240,#05081E)}
.dw{position:absolute;left:300px;top:700px;width:480px;height:820px;perspective:1600px}
.dwin{position:absolute;inset:0;overflow:hidden;border-radius:6px;box-shadow:0 0 90px 20px rgba(255,176,143,.35)}
.leaf{position:absolute;inset:0;transform-origin:0 50%;background:linear-gradient(90deg,#1E2A7A,#2B3FE0 60%,#2536B8);
  border-radius:6px;box-shadow:inset 0 0 0 10px #16206B, inset 0 0 0 14px rgba(255,255,255,.08)}
.leaf:before{content:"";position:absolute;left:52px;right:52px;top:60px;height:300px;border:6px solid rgba(255,255,255,.12);border-radius:8px}
.leaf:after{content:"";position:absolute;left:52px;right:52px;top:420px;height:340px;border:6px solid rgba(255,255,255,.12);border-radius:8px}
.knob{position:absolute;right:46px;top:430px;width:34px;height:34px;border-radius:50%;background:radial-gradient(#FFD9C6,#FF6A3D)}
.frame{position:absolute;left:-26px;top:-26px;right:-26px;bottom:-4px;border:26px solid #0E1440;border-bottom:none;border-radius:10px}
.edge{position:absolute;left:300px;top:700px;width:480px;height:820px;box-shadow:0 0 60px 14px rgba(255,190,150,.7),inset 0 0 0 4px #FFD9C6;border-radius:6px}
.crack{position:absolute;left:774px;top:704px;width:10px;height:812px;background:linear-gradient(#FFE3CF,#FFB08F);box-shadow:0 0 40px 10px rgba(255,176,143,.8)}
.under{position:absolute;left:300px;top:1508px;width:480px;height:14px;background:#FFE3CF;box-shadow:0 0 50px 16px rgba(255,176,143,.9)}
.hand{font-family:'Caveat Brush';color:#FFB08F}
.spill{position:absolute;left:0;right:0;top:1520px;height:400px;clip-path:polygon(28% 0,72% 0,100% 100%,0 100%);
  background:linear-gradient(rgba(255,196,150,.75),rgba(255,140,90,0))}
.mote{position:absolute;width:8px;height:8px;border-radius:50%;background:#FFE3CF;box-shadow:0 0 12px #FFB08F}
.card{background:#F7F1E5;border-radius:44px;padding:50px 56px;box-shadow:0 40px 90px rgba(5,8,30,.45)}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:20px;border-bottom:3px solid rgba(14,20,64,.10);padding:22px 0}
.row:last-child{border-bottom:none}
.k{font:600 52px/1.2 Inter;color:#0E1440}.v{font:800 64px/1 'Inter Display';color:#2B3FE0;white-space:nowrap}
.v.big{color:#FF6A3D}
.lab{font:800 34px/1 Inter;letter-spacing:.12em;color:#FF6A3D;margin-bottom:14px}
.fine{font:600 36px/1.35 Inter;color:#5A6190}
.deep{position:absolute;inset:0;background:radial-gradient(90% 60% at 50% 40%,#2B3FE0,#16206B 70%)}
"""


def ff_door_scene(open_at=None):
    motes = "".join(f'<div class="mote" style="left:{330 + (k * 97) % 420}px;top:{760 + (k * 173) % 700}px" '
                    f'data-drift="{(k % 3 - 1) * 4},{-6 - k % 4},{k}"></div>' for k in range(14))
    door_attr = f'data-door="{open_at},0.85"' if open_at is not None else 'data-door="99,1"'
    spill_attr = f'data-spill="{open_at},0.85" data-base="0.4"' if open_at is not None else 'data-spill="99,1" data-base="0.4"'
    return "".join([
        '<div class="room"></div><div class="wall"></div><div class="floor"></div>',
        f'<div class="spill" {spill_attr}></div>',
        '<div class="edge"></div><div class="crack"></div><div class="under"></div>',
        f'<div class="dw"><div class="dwin">{ft("ocean", 0.0)}</div><div class="leaf" {door_attr}><div class="knob"></div></div>'
        '<div class="frame"></div></div>',
        motes,
        '<div class="grain"></div>',
        el('100 a month.', "c", 300, a="none", cls="HD", style="font-size:150px"),
        el('<i>From birth to 18.</i>', "c", 460, a="none", cls="SR", style="font-size:112px"),
        el('<span class="hand">…then never touch it.</span>', "c", 585, a="none", style="font-size:76px;transform:rotate(-2deg)"),
    ])


def ff_door():
    (m6, m8, m10), paid, today = (lambda m: ((m[0][6], m[0][8], m[0][10]), m[1], m[2]))(ff_math())
    r = HReel("ff-reel-1018-the-door", "fullyfunded", bpm=80, css=FF_CSS, stage="#070B2A")
    f = lambda v: f"{v:,}" if v < 30000 else f"{round(v, -3):,}"  # noqa: E731  (about-figures, nearest 1,000)
    # 1 hook: a closed door with light behind it; it swings open on the bar
    r.scene(3, ff_door_scene(open_at=1.05), cam="push")
    # 2 through the door: the sea, and the number
    r.scene(2, "".join([ft("ocean", 2.25), '<div class="scrimT"></div>',
                        el('<span class="pill">EXAMPLE · 8% A YEAR</span>', "c", 300, a="stamp", t=0.0, d=0.25, r=-3),
                        el(f'≈<span data-a="count" data-t="0.1" data-d="1.0" data-from="{paid}" data-to="{round(m8[1], -3)}" data-comma="1">{f(paid)}</span>',
                           "c", 420, a="none", cls="HD", style="font-size:150px"),
                        words("*by 65.* Hands off / since 18.", "c", 620, t=0.35, gap=0.08, cls="SR", style="font-size:96px")]),
            tin="flash", td=0.5, color="#FFB08F", color2="#FFE3CF", cam="pull")
    # 3 what went in
    r.scene(2, "".join([ft("ocean", 4.0), '<div class="scrimT"></div>',
                        words(f"You put in / *{f(paid)}.*", "c", 330, t=0.0, gap=0.1, cls="HD", em_cls="cor", style="font-size:130px"),
                        words("Time did / *the rest.*", "c", 680, t=0.5, gap=0.1, cls="SR", style="font-size:110px")]),
            tin="whipL", cam="right")
    # 4 the plain math
    rows = [("Birth to 18", "100 a month"), ("At 18", f"≈ {f(m8[0])}"), ("18 to 65", "no more deposits"), ("At 65", f"≈ {f(m8[1])}")]
    card = ('<div class="card"><div class="lab">THE PLAIN MATH · 8% A YEAR</div>' +
            "".join(f'<div class="row" data-a="up" data-t="{0.15 + k * 0.28:.2f}" data-d="0.35"><span class="k">{a}</span>'
                    f'<span class="v{" big" if k == 3 else ""}">{b}</span></div>' for k, (a, b) in enumerate(rows)) + '</div>')
    r.scene(2.5, "".join([ft("ocean", 5.8, style="filter:blur(6px) brightness(.8)"), el(card, 80, 420, 920, a="up", t=0.0, d=0.35)]),
            tin="slam", cam="rise")
    # 5 same plan, different years
    rows = [("6% a year", f"≈ {f(m6[1])}"), ("8% a year", f"≈ {f(m8[1])}"), ("10% a year", f"≈ {f(m10[1])}")]
    card = ('<div class="card"><div class="lab">SAME PLAN, DIFFERENT YEARS</div>' +
            "".join(f'<div class="row" data-a="left" data-t="{0.1 + k * 0.25:.2f}" data-d="0.35"><span class="k">{a}</span>'
                    f'<span class="v">{b}</span></div>' for k, (a, b) in enumerate(rows)) +
            '<div class="fine" style="margin-top:22px" data-a="fade" data-t="0.9" data-d="0.4">US stocks\' long-run average: roughly 10% a year, '
            'before inflation. Not a promise.</div></div>')
    r.scene(2.5, "".join([ft("ocean", 1.0, style="filter:blur(6px) brightness(.8)"), el(card, 80, 420, 920, a="up", t=0.0, d=0.35)]),
            tin="iris", focus=(540, 700), color="#FF6A3D", cam="push")
    # 6 the catch (a breath away from the sea)
    r.scene(3, "".join(['<div class="deep"></div>',
                        el('<span class="pill">THE CATCH</span>', "c", 300, a="stamp", t=0.0, d=0.25, r=-4),
                        words("Returns swing. / Some years *fall.*", "c", 430, t=0.1, gap=0.07, cls="HD", em_cls="cor", style="font-size:100px"),
                        words("Fees take *a slice.*", "c", 690, t=0.6, gap=0.07, cls="HD", em_cls="cor", style="font-size:84px"),
                        words(f"And {f(m8[1])} then buys / what ≈ *{f(today)}* buys today.", "c", 850, t=1.1, gap=0.05, cls="SR",
                              style="font-size:76px"),
                        el('<div class="fine" style="color:#C9CEF5">If inflation averages 2.5% a year. Example math.</div>', "c", 1090,
                           a="fade", t=1.5)]),
            tin="stripes", color="#FF6A3D", color2="#F7F1E5", color3="#2B3FE0", cam="tilt")
    # 7 the swell: the sea, the line
    r.scene(4, "".join([ft("ocean", 8.2), '<div class="scrimT" style="opacity:.8"></div>',
                        words("The door / is *time.*", "c", 340, t=0.1, gap=0.14, cls="SR", style="font-size:170px"),
                        words("Open it early.", "c", 720, t=1.3, gap=0.12, cls="HD", style="font-size:104px"),
                        el(f'<img src="{asset(FF["mark"])}" style="width:110px;height:110px;border-radius:50%;background:#fff">', "c", 1200,
                           a="pop", t=1.9)]),
            tin="flash", td=0.5, color="#FFB08F", color2="#FFFFFF", cam="pull")
    # loop: back to the closed door
    r.scene(1.5, ff_door_scene(open_at=None), tin="zoom", focus=(540, 1100), cam="push")
    sound = dict(music=LIB / "ff-hero-horizon-el.mp3", music_from=0.72,
                 cues=[(SFX("sfx-door-open"), 1.2, -2, 6000), (SFX("sfx-waves"), 1.6, -4, 3800),
                       (SFX("sfx-whoosh-soft"), 3.6, -12, 6000), (SFX("sfx-whoosh-soft"), 7.0, -12, 6000),
                       (SFX("sfx-waves"), 10.6, -8, 3800)])
    return r, sound


R["ff-reel-1018-the-door"] = ff_door


# ============================================================================================== LOCKED HOUR: Mute the World
LH = BRANDS["lockedhour"]
LH_CSS = EXTRA_CSS + """
.HD{font-family:'Inter Display';font-weight:900;color:#fff;letter-spacing:-.04em;line-height:.98}
.ink{color:#141414}
.em{background:linear-gradient(#FF5CA8,#FF5CA8) 0 88%/100% 34% no-repeat;padding:0 .08em}
.emy{background:#FFE27A;color:#141414;padding:0 .14em;border-radius:10px;box-shadow:7px 7px 0 #141414;margin:0 .04em}
.nt{display:flex;align-items:center;gap:18px;background:rgba(255,255,255,.94);border-radius:30px;padding:22px 28px;
  font:700 40px/1.1 Inter;color:#141414;box-shadow:0 18px 40px rgba(0,0,0,.35);margin-bottom:18px;width:760px}
.nt b{font-weight:800}.nt .ic{font-family:'Noto Color Emoji';font-size:46px}
.note{font-family:'Caveat Brush';color:#FFE27A}
.butter{position:absolute;inset:0;background:radial-gradient(circle,rgba(20,20,20,.10) 2.4px,transparent 3px) 0 0/40px 40px,#FFE27A}
.zine{border:8px solid #141414;border-radius:36px;background:#FFF4E0;box-shadow:16px 16px 0 #141414;padding:46px 50px}
.timer{font:900 210px/1 'Inter Display';color:#fff;letter-spacing:-.04em;text-shadow:0 10px 40px rgba(0,0,0,.35)}
"""


def lh_hook_html():
    nts = [("📩", "<b>Quick question?</b> got a sec"), ("📅", "<b>Meeting moved</b> to 2:30"), ("💬", "<b>you there??</b>"),
           ("🛒", "<b>Sale ends tonight</b>"), ("🔔", "<b>Reminder:</b> the thing")]
    stack = "".join(f'<div class="nt"><span class="ic">{i}</span><span>{t}</span></div>' for i, t in nts)
    return "".join([ft("traffic", 0.0, sp=2.0), '<div class="scrimA"></div><div class="grain"></div>',
                    el('Busy all day.', "c", 300, a="none", cls="HD", style="font-size:150px"),
                    el('<span class="em">Nothing finished.</span>', "c", 470, a="none", cls="HD", style="font-size:124px"),
                    el(stack, 160, 760, 760, a="stack", t=0.08, d=0.3, gap=0.22, loop="buzz", amp=0.6)])


def lh_mute():
    r = HReel("lh-reel-1018-mute-the-world", "lockedhour", bpm=100, css=LH_CSS, stage="#141414")
    r.scene(3, lh_hook_html(), cam="push")
    tabs = "".join(f'<div style="flex:1;background:{c};border:5px solid #141414;border-bottom:none;border-radius:18px 18px 0 0;'
                   f'height:70px;margin-right:-6px"></div>' for c in ["#FFF4E0", "#FFE27A", "#FF5CA8", "#FFF4E0", "#FFD43B", "#FFF4E0",
                                                                       "#FF5CA8", "#FFF4E0", "#FFE27A", "#FFF4E0", "#FFD43B", "#FFF4E0"])
    r.scene(2, "".join([ft("traffic", 4.0, sp=2.6), '<div class="scrimA"></div>',
                        el(f'<div style="display:flex;width:900px">{tabs}</div>', 90, 330, 900, a="drop", t=0.0, d=0.5, loop="shake"),
                        words("Tabs. Pings. / *“Got a sec?”*", "c", 520, t=0.1, gap=0.09, cls="HD", style="font-size:130px"),
                        emoji("📱", 420, 900, 240, a="pop", t=0.4, loop="buzz", amp=2.5)]),
            tin="glitch", td=0.24, cam="tilt", shake=(0.0, 0.5, 26))
    # silence: the lake
    r.scene(3, "".join([ft("lake", 0.0), '<div class="grain" style="opacity:.6"></div>',
                        words("Lock", "c", 380, t=0.25, cls="HD", style="font-size:200px"),
                        words("*one hour.*", "c", 590, t=0.6, cls="HD", em_cls="emy", style="font-size:170px")]),
            tin="slit", td=0.5, color="#FFE27A", cam="pull")
    r.scene(3, "".join([ft("lake", 1.8), '<div class="scrimA" style="opacity:.6"></div>',
                        ring(540, 760, 300, "rgba(255,255,255,.25)", width=22, t=0.0, d=0.01),
                        ring(540, 760, 300, "#FFE27A", width=22, t=0.05, d=1.4),
                        el('<span data-a="tick" data-t="0.2" data-d="1.6" data-from="3600" data-to="3598" data-mmss="1">60:00</span>', "c", 655,
                           a="none", cls="timer"),
                        el(f'<img src="{asset(LH["mark"])}" style="width:120px;height:120px;border-radius:50%;background:#fff">', "c", 1120,
                           a="pop", t=0.5),
                        words("One hour. One thing.", "c", 320, t=0.3, gap=0.08, cls="HD", style="font-size:92px")]),
            tin="push", cam="push")
    for txt, tin, off in [("Phone: / *another room.*", "whipU", 3.4), ("One task. / *Not three.*", "whipL", 4.6),
                          ("Door closed. / *Pings off.*", "iris", 5.8)]:
        r.scene(2, "".join([ft("lake", off), '<div class="scrimA" style="opacity:.55"></div>',
                            words(txt, "c", 420, t=0.0, gap=0.1, cls="HD", em_cls="emy", style="font-size:136px")]),
                tin=tin, focus=(540, 600), color="#FF5CA8", cam="push" if tin != "whipL" else "left")
    r.scene(3, "".join([ft("lake", 7.0), '<div class="scrimA" style="opacity:.55"></div>',
                        words("Mind wanders? / Bring it back.", "c", 380, t=0.0, gap=0.08, cls="HD", style="font-size:110px"),
                        el('<span class="note" style="font-size:118px">that\'s the work.</span>', "c", 700, a="wipe", t=0.9, d=0.5, r=-3)]),
            tin="stripes", color="#FFE27A", color2="#FF5CA8", color3="#FFF4E0", cam="rise")
    r.scene(3, "".join([ft("lake", 8.6), '<div class="grain" style="opacity:.5"></div>',
                        words("The world / can wait / *an hour.*", "c", 360, t=0.0, gap=0.13, cls="HD", em_cls="emy", style="font-size:150px")]),
            tin="flash", td=0.45, color="#FFE27A", color2="#FFF4E0", cam="pull")
    r.scene(2, "".join(['<div class="butter"></div>',
                        el(f'<div class="zine" style="text-align:center"><img src="{asset(LH["mark"])}" style="width:150px;height:150px;'
                           f'border-radius:50%;background:#fff;border:6px solid #141414"><div class="HD ink" style="font-size:96px;margin-top:26px">'
                           f'Locked Hour</div><div style="font:700 50px/1.3 Inter;color:#141414;margin-top:20px">Save this for your<br>next hour.</div>'
                           '</div>', 140, 520, 800, a="pop", t=0.0, d=0.45)]),
            tin="slam", cam="push")
    r.loop(1.5, tin="glitch", td=0.24)
    sound = dict(music=LIB / "lh-hero-quiet-power-el.mp3", music_from=0.0,
                 duck="if(lt(t,3.0),0.55,1)",
                 cues=[(SFX("sfx-city-rush"), 0.0, -3, 6500), (SFX("sfx-whoosh-fast"), 1.75, -9, 6000),
                       (SFX("sfx-tick-ding"), 5.6, -10, 6000), (SFX("sfx-whoosh-soft"), 7.75, -12, 6000),
                       (SFX("sfx-whoosh-soft"), 8.95, -12, 6000), (SFX("sfx-city-rush"), 15.0, -9, 6500)])
    return r, sound


R["lh-reel-1018-mute-the-world"] = lh_mute


# ============================================================================================== HOURBACK: Freeze Frame
HB = BRANDS["hourback"]
HB_CSS = EXTRA_CSS + """
.HP{font-family:Poppins;font-weight:700;color:#2A2238;letter-spacing:-.02em;line-height:1.02}
.wht{color:#fff}
.em{background:linear-gradient(#FFC94D,#FFC94D) 0 90%/100% 36% no-repeat;padding:0 .08em}
.set{position:absolute;inset:0;background:linear-gradient(#FFE6D3 0 62%,#E9B99A 62% 100%)}
.wp{position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(94,84,201,.06) 0 40px,transparent 40px 120px);height:62%}
.win{position:absolute;left:70px;top:420px;width:300px;height:420px;border:16px solid #fff;border-radius:12px;
  background:linear-gradient(#9FB8FF,#FFD8B0)}
.lamp{position:absolute;right:40px;top:600px;width:600px;height:600px;border-radius:50%;
  background:radial-gradient(rgba(255,201,77,.55),rgba(255,201,77,0) 65%)}
.sofa{position:absolute;left:-40px;right:-40px;top:1480px;height:360px;background:#5E54C9;border-radius:80px 80px 0 0}
.sofa:before{content:"";position:absolute;left:80px;right:80px;top:-120px;height:200px;background:#4C43B0;border-radius:60px}
.phone{position:absolute;left:190px;top:640px;width:700px;height:1120px;background:#2A2238;border-radius:80px;padding:26px;
  box-shadow:0 50px 90px rgba(42,34,56,.4)}
.scr{width:100%;height:100%;background:#FFF8EF;border-radius:58px;overflow:hidden;position:relative}
.hdr{display:flex;align-items:center;gap:16px;padding:40px 36px 24px;border-bottom:3px solid #F0E2D2;font:700 44px/1 Poppins;color:#2A2238}
.badge{margin-left:auto;background:#FF8A3D;color:#fff;font:800 34px/1 Inter;border-radius:999px;padding:10px 20px}
.msgs{padding:20px 26px}
.m{background:#fff;border-radius:30px;padding:18px 26px;font:600 40px/1.2 Inter;color:#2A2238;margin:0 0 14px;
  box-shadow:0 4px 0 rgba(42,34,56,.06);width:fit-content;max-width:560px}
.m.me{margin-left:auto;background:#5E54C9;color:#fff}
.m small{display:block;font:700 24px/1 Inter;color:#9A8FB0;margin-bottom:6px}
.frz{filter:sepia(.95) saturate(.75) contrast(1.18) brightness(.9)}
.frzv{position:absolute;inset:0;box-shadow:inset 0 0 220px 60px rgba(40,22,10,.55);pointer-events:none}
.cap{display:inline-block;background:#FFC94D;color:#2A2238;font:800 74px/1.05 Poppins;padding:18px 34px;border-radius:14px;
  box-shadow:10px 10px 0 #2A2238;transform:rotate(-2deg)}
.sub{display:inline-block;background:rgba(42,34,56,.9);color:#fff;font:600 50px/1.25 Inter;padding:16px 28px;border-radius:14px}
.plum{position:absolute;inset:0;background:radial-gradient(circle,rgba(255,255,255,.07) 2.4px,transparent 3px) 0 0/40px 40px,#3A2240}
.cream{position:absolute;inset:0;background:radial-gradient(circle,rgba(42,34,56,.07) 2.4px,transparent 3px) 0 0/40px 40px,#FFF8EF}
.pc{background:#5E54C9;border-radius:40px;padding:46px 50px;color:#fff;font:600 54px/1.3 Inter;box-shadow:0 30px 60px rgba(42,34,56,.3)}
.chipk{display:inline-block;background:#FFC94D;color:#2A2238;font:800 30px/1 Inter;letter-spacing:.1em;padding:12px 20px;border-radius:999px}
.res{background:#fff;border-radius:40px;padding:40px 44px;box-shadow:0 30px 70px rgba(42,34,56,.18)}
.ri{display:flex;gap:22px;align-items:flex-start;font:600 48px/1.25 Inter;color:#2A2238;padding:20px 0;border-bottom:3px solid #F3E7DA}
.ri:last-child{border-bottom:none}.ri .e{font-family:'Noto Color Emoji';font-size:56px}
.small{font:600 32px/1.3 Inter;color:#8C7F9E}
"""

CHAT = [("Mum", "ok so Saturday 🎉"), ("Uncle Raj", "👍"), ("Sis", "who's doing dessert??"), ("Mum", "🎤 Voice message · 2:41"),
        ("Dad", "did anyone ask Grandpa"), ("Sis", "WAIT what time"), ("Uncle Raj", "📷 Photo"), ("Mum", "6!! at mine")]


def hb_set():
    return '<div class="set"></div><div class="wp"></div><div class="win"></div><div class="lamp"></div><div class="sofa"></div>'


def hb_phone(start=0, n=8, a="stack", t=0.1, gap=0.16):
    msgs = "".join(f'<div class="m"><small>{who}</small>{txt}</div>' for who, txt in CHAT[start:start + n])
    return (f'<div class="phone"><div class="scr"><div class="hdr"><span class="emo">🏡</span>Family<span class="badge">147</span></div>'
            f'<div class="msgs el" style="position:static" data-a="{a}" data-t="{t}" data-d="0.28" data-gap="{gap}">{msgs}</div></div></div>')


def hb_freeze():
    r = HReel("hb-reel-1018am-freeze-frame", "hourback", bpm=120, css=HB_CSS, stage="#FFE6D3")
    hook = "".join([hb_set(), el(hb_phone(0, 8, t=-0.45, gap=0.2), 0, 0, a="none", loop="buzz", amp=0.35),
                    el('147 unread', "c", 290, a="none", cls="HP", style="font-size:140px"),
                    el('<span class="em">in the family chat.</span>', "c", 445, a="none", cls="HP", style="font-size:96px")])
    r.scene(3, hook, cam="push")
    r.scene(2, "".join([hb_set(), el(hb_phone(2, 6, t=0.0, gap=0.11), 0, -120, a="none", loop="buzz", amp=1.4),
                        emoji("😵‍💫", 690, 300, 200, a="pop", t=0.2, loop="wobble")]),
            tin="whipR", cam="tilt", shake=(0.1, 0.8, 14))
    # freeze frame: the music stops, record scratch, narrator
    frozen = "".join([hb_set(), el(hb_phone(2, 6, a="none"), 0, -120, a="none"), '<div class="grain"></div>'])
    r.scene(7, "".join([f'<div class="frz" style="position:absolute;inset:0">{frozen}</div><div class="frzv"></div>',
                        el('<span class="cap">Yep. That\'s me.</span>', "c", 330, a="stamp", t=0.15, d=0.25, r=-3),
                        el('<span class="sub">You\'re probably wondering<br>how I got here.</span>', "c", 1240, a="up", t=1.3, d=0.3)]),
            tin="cut", cam="push", shake=(0.0, 0.25, 30))
    r.scene(3, "".join(['<div class="plum"></div>',
                        el('<span class="chipk">THE FIX</span>', "c", 330, a="stamp", t=0.0, d=0.25, r=-3),
                        words("Copy the chat. / *Take out names* / and numbers.", "c", 450, t=0.1, gap=0.08, cls="HP wht",
                              style="font-size:110px")]),
            tin="pixel", td=0.4, cam="push")
    r.scene(4, "".join(['<div class="cream"></div>',
                        el('<span class="chipk">ASK ANY AI</span>', "c", 330, a="pop", t=0.0),
                        el('<div class="pc"><span data-a="type" data-t="0.2" data-d="1.1">What do I need to do, and by when? One line each.</span></div>',
                           120, 460, 840, a="up", t=0.0),
                        img("ht-point.png", 150, 900, 470, a="fly", t=0.35, r=-32, loop="float")]),
            tin="whipL", cam="push")
    res = ('<div class="res"><div class="small" style="margin-bottom:10px">WHAT YOU GET · EXAMPLE</div>' +
           "".join(f'<div class="ri" data-a="left" data-t="{0.15 + k * 0.4:.2f}" data-d="0.35"><span class="e">{e}</span><span>{t}</span></div>'
                   for k, (e, t) in enumerate([("🍰", "<b>Bring dessert.</b> Sat, 6 pm, Mum's."),
                                               ("🎁", "<b>Chip in for Grandpa's gift.</b> By Thu."),
                                               ("💬", "Everything else: chatter.")])) +
           '<div class="small" style="margin-top:12px">Example made up for this post.</div></div>')
    r.scene(4, "".join(['<div class="cream"></div>', el(res, 90, 400, 900, a="up", t=0.0)]), tin="slam", cam="rise")
    r.scene(3, "".join([hb_set(), '<div class="scrimA" style="background:rgba(58,34,64,.55)"></div>',
                        words("147 messages.", "c", 420, t=0.0, gap=0.1, cls="HP wht", style="font-size:130px"),
                        el('<span class="cap" style="font-size:150px">2 jobs.</span>', "c", 640, a="stamp", t=0.45, d=0.3, r=-4),
                        emoji("🎉", 680, 960, 200, a="pop", t=0.7, loop="wobble"),
                        el(f'<img src="{asset(HB["mark"])}" style="width:110px;height:110px;border-radius:50%;background:#fff">', "c", 1200,
                           a="pop", t=0.9)]),
            tin="zoom", focus=(540, 700), cam="push", shake=(0.45, 0.2, 18))
    r.loop(1.5, tin="spin")
    s3 = r.scenes[2]["start"]
    s4 = r.scenes[3]["start"]
    duck = f"if(lt(t,{s3 - 0.02:.2f}),1,if(lt(t,{s4 - 0.15:.2f}),0.0,1))"
    sound = dict(music=LIB / "hb-hero-sitcom-el.mp3", music_from=2.5, duck=duck,
                 eq="equalizer=f=2600:t=o:w=1.6:g=-8,equalizer=f=4200:t=o:w=1:g=-4",
                 cues=[(SFX("sfx-phone-buzz"), 0.05, -9, 6000), (SFX("sfx-phone-buzz"), s3 - 1.0, -7, 6000),
                       (SFX("sfx-record-scratch"), s3 - 0.04, -3, 7000),
                       (VOICE / "hb-hero-narrator.mp3", s3 + 0.25, 8, 9000),
                       (SFX("sfx-whoosh-fast"), r.scenes[4]["start"] - 0.1, -10, 6000),
                       (SFX("sfx-tick-ding"), r.scenes[6]["start"] + 0.45, -6, 7000)])
    return r, sound


R["hb-reel-1018am-freeze-frame"] = hb_freeze


# ============================================================================================== LITTLEFOLD: 3 am, Lit Windows
LF = BRANDS["littlefold"]
LF_CSS = EXTRA_CSS + """
.H{font-family:Lora;font-weight:600;color:#FFF4E0;letter-spacing:-.02em;line-height:1.06}
.em{font-style:italic;color:#FFD6E3}
.ink{color:#2C2A3A}.emb{font-style:italic;color:#D9497A}
.clock{font:600 280px/1 Lora;color:#FFF4E0;letter-spacing:-.03em;text-shadow:0 10px 50px rgba(255,163,92,.45)}
.night{position:absolute;inset:0;background:linear-gradient(#2A0F25 0%,#5A1A3E 52%,#7A2149 78%,#A8456A 100%)}
.moon{position:absolute;left:720px;top:330px;width:170px;height:170px;border-radius:50%;background:#FFF8E4;
  box-shadow:0 0 80px 30px rgba(255,214,227,.35)}
.bld{position:absolute;bottom:0;background:#2A0F25;display:grid;gap:22px;padding:40px 30px}
.wn{width:100%;height:52px;border-radius:6px;background:#3E1734}
.wn.on{background:#FFD3AE;box-shadow:0 0 30px rgba(255,163,92,.8)}
.lampglow{position:absolute;left:-200px;right:-200px;top:900px;height:1300px;
  background:radial-gradient(50% 45% at 50% 50%,rgba(255,211,174,.55),rgba(255,138,112,.18) 55%,rgba(0,0,0,0) 75%)}
.card{background:#FFF4E0;border-radius:56px;padding:56px 60px;box-shadow:0 30px 70px rgba(42,15,37,.45)}
.lab{font:700 30px/1 Inter;letter-spacing:.14em;color:#D9497A}
.blob{position:absolute;inset:0;background:
  radial-gradient(420px 420px at 6% 8%, #FFD6E3 0 60%, transparent 61%),
  radial-gradient(360px 360px at 100% 22%, #FFE27E 0 58%, transparent 59%),
  radial-gradient(520px 520px at 96% 100%, #FFD3AE 0 60%, transparent 61%), #FFF4E0}
.src{font:600 30px/1.3 Inter;color:#7A6F80}
"""


def skyline(lit_from=0.0, density=0.45, seed=3, dark_at=None, static=False, moon=True):
    import random
    rnd = random.Random(seed)
    out = ['<div class="night"></div>' + ('<div class="moon"></div>' if moon else '')]
    xs = [(-20, 260, 900), (220, 300, 1180), (500, 240, 800), (720, 380, 1050)]
    k = 0
    for x, w, h in xs:
        cols = 3 if w < 300 else 4
        cells = []
        rows = (h - 80) // 74
        for _ in range(rows * cols):
            on = rnd.random() < density
            if on:
                if dark_at is not None:
                    cells.append(f'<div class="wn on" data-out="{dark_at + rnd.random() * 0.9:.2f},0.2"></div>')
                elif static:
                    cells.append('<div class="wn on"></div>')
                else:
                    cells.append(f'<div class="wn on" data-a="fade" data-t="{lit_from + rnd.random() * 1.2:.2f}" data-d="0.25"></div>')
                k += 1
            else:
                cells.append('<div class="wn"></div>')
        out.append(f'<div class="bld" style="left:{x}px;width:{w}px;height:{h}px;grid-template-columns:repeat({cols},1fr);'
                   f'align-content:start">{"".join(cells)}</div>')
    return "".join(out)


def lf_hook():
    return "".join([ft("rain", 0.0), '<div class="scrimA" style="background:rgba(42,15,37,.42)"></div><div class="grain"></div>',
                    el('3<span data-blink="1">:</span>07<span style="font-size:110px"> am</span>', "c", 330, a="none", cls="clock"),
                    el('Up again.<br><span class="em">Just you and the quiet.</span>', "c", 690, a="none", cls="H", style="font-size:92px")])


def lf_3am():
    r = HReel("lf-reel-1018am-3am-windows", "littlefold", bpm=60, css=LF_CSS, stage="#2A0F25")
    r.scene(1.5, lf_hook(), cam="push")
    r.scene(1.75, "".join([skyline(0.15, 0.22, 3), words("Look at the / *lit windows.*", "c", 560, t=0.0, gap=0.1, cls="H",
                                                          style="font-size:112px")]),
            tin="blob", color="#FFD6E3", focus=(540, 800), cam="rise")
    r.scene(1.75, "".join([skyline(0.0, 0.4, 3), words("Some of them? / *Another parent,* / up too.", "c", 560, t=0.0, gap=0.09, cls="H",
                                                         style="font-size:104px")]),
            tin="push", cam="push")
    r.scene(1.5, "".join([f'<div style="position:absolute;inset:0;filter:blur(7px) brightness(.8)">{skyline(static=True, density=0.5, seed=3)}</div>',
                          '<div class="lampglow"></div>',
                          words("You're not / the only one / *awake.*", "c", 520, t=0.0, gap=0.12, cls="H", style="font-size:126px")]),
            tin="flash", color="#FFD3AE", color2="#FFF4E0", cam="pull")
    r.scene(1.75, "".join(['<div class="blob"></div>',
                           el('<div class="card"><div class="lab">ONE THING THAT HELPS · NHS</div><div style="font:600 92px/1.08 Lora;'
                              'color:#2C2A3A;margin-top:24px">Make night<br>feel like <i style="color:#D9497A">night.</i></div></div>',
                              110, 520, 860, a="up", t=0.0, d=0.4)]),
            tin="slam", cam="push")
    for k, (emo, txt, tin) in enumerate([("💡", "Lights / *down low.*", "whipL"), ("🤫", "Voice soft. / *Not much talk.*", "whipL"),
                                         ("🛏️", "Fed and changed? / *Back down.*", "whipU")]):
        sky = (skyline(dark_at=0.25, density=0.5, seed=5, moon=False) if k == 0
               else skyline(static=True, density=[0, 0.12, 0.05][k], seed=5, moon=False))
        r.scene(1.25, "".join([sky, '<div class="lampglow" style="opacity:.55"></div>',
                               emoji(emo, 440, 230, 190, a="pop", t=0.0, loop="float"),
                               words(txt, "c", 450, t=0.08, gap=0.1, cls="H", style="font-size:116px")]),
                tin=tin, cam="push")
    r.scene(1.75, "".join([ft("rain", 2.0), '<div class="scrimA" style="background:rgba(42,15,37,.5)"></div>',
                           words("Bit by bit, they learn / night is for *sleep.*", "c", 480, t=0.0, gap=0.08, cls="H", style="font-size:100px")]),
            tin="iris", color="#FFD6E3", focus=(540, 700), cam="pull")
    r.scene(1.75, "".join(['<div class="night"></div><div class="lampglow"></div>',
                           words("Send this to / someone up / *at 3 am.*", "c", 460, t=0.0, gap=0.1, cls="H", style="font-size:118px"),
                           emoji("💛", 450, 920, 180, a="pop", t=0.6, loop="pulse"),
                           el(f'<img src="{asset(LF["mark"])}" style="width:110px;height:110px;border-radius:50%;background:#fff">', "c", 1200,
                              a="pop", t=0.8)]),
            tin="blob", color="#FFD3AE", focus=(540, 1000), cam="push")
    r.loop(1.5, tin="flash", color="#FFD3AE", color2="#FFF4E0")
    rain = SFX("sfx-rain-window")
    sound = dict(music=LIB / "lf-hero-3am-el.mp3", music_from=0.0, extend=(12.0, 1.5, 0.0),
                 cues=[(rain, 0.0, 22, 5000), (rain, 7.6, 22, 5000), (SFX("sfx-whoosh-soft"), 1.4, -14, 5000)])
    return r, sound


R["lf-reel-1018am-3am-windows"] = lf_3am


# ============================================================================================== build
def build(rid, outdir, qa_only=False, dsf=2):
    r, snd = R[rid]()
    r.stretch(12.6)
    work = Path(outdir) / rid
    if not qa_only:
        fdir, n = render_frames(r, work, dsf=dsf)
        silent = work / f"{rid}.silent.mp4"
        encode_silent(fdir, n, silent)
        out = work / f"{rid}.mp4"
        lu = mix(silent, out, snd["music"], snd["cues"], n / FPS, music_from=snd.get("music_from", 0.0), duck=snd.get("duck"),
                 extend=snd.get("extend"), eq=snd.get("eq"))
        silent.unlink()
        print(json.dumps(dict(id=rid, probe=probe(out), lufs=lu, cuts=[round(c, 2) for c in r.cuts()])))
    fdir = work / "frames"
    ts = sorted(set([round(k * 0.5, 2) for k in range(int(r.duration * 2) + 1) if k * 0.5 < r.duration]))
    sheet(fdir, ts, work / f"{rid}-half.jpg", cols=8, scale=0.18)
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

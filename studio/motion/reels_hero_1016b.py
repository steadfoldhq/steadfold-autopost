#!/usr/bin/env python3
"""Oct 16 hero samples, round 2 (creative playbook): sell the OUTCOME, barely show the product.

    python3 studio/motion/reels_hero_1016b.py <id> --out DIR

ff-hero-1016-tuesdays  Fully Funded, "Buy Back Your Tuesdays" (signature format: The Freedom Receipt)
lf-hero-1016-warm-tea  Littlefold, "Warm Tea" (signature format: The Small Win Rosette)

Built on reels_hero_1016.py (footage layers, sound mix). Differences: clean floating text (very soft shadow, no scrims,
bands or plates), an ElevenLabs v3 voice re-spaced phrase by phrase from its word timings, and music ducked under the voice.

Footage (Pexels, free for commercial use, no attribution: https://www.pexels.com/license/):
  34118766 Urban Traffic Jam in New York City   https://www.pexels.com/video/urban-traffic-jam-in-new-york-city-34118766/
  20736942 A coffee cup with steam              https://www.pexels.com/video/a-coffee-cup-with-steam-coming-out-of-it-20736942/
  14458145 A Woman Walking on the Beach at Sunrise https://www.pexels.com/video/a-woman-walking-on-the-beach-at-sunrise-14458145/
  20549082 A person's feet in the water         https://www.pexels.com/video/a-person-s-feet-are-in-the-water-at-the-beach-20549082/
  4710717  Person using a microwave              https://www.pexels.com/video/video-of-person-using-microwave-4710717/
  11350957 Hot tea in cup                        https://www.pexels.com/video/hot-tea-in-cup-11350957/
  35434114 Sunlight through sheer curtains       https://www.pexels.com/video/sunlight-streaming-through-sheer-curtains-35434114/
  7592151  Woman waking up in the morning        https://www.pexels.com/video/woman-waking-up-in-the-morning-7592151/
  5935128  Person drinking green tea             https://www.pexels.com/video/person-drinking-green-tea-5935128/
Money maths: computed in ff_math() ($300 a month for 480 months at 8% a year, monthly compounding).
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
VOICE = REPO / "media" / "voice" / "hero2"
H.CACHE = Path(os.environ.get("HERO_CACHE", "/tmp/hero-footage"))
ft = H.ft
R = {}

H.CLIPS.update({
    "jam": ("px-34118766.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920", "eq=contrast=1.12:saturation=0.82:brightness=-0.09:gamma=0.92"),
    "coffee": ("px-20736942.mp4", "scale=1080:1920", "eq=contrast=1.04:saturation=1.08,colorbalance=rs=.03:bs=-.03"),
    "beach": ("px-14458145.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920:(iw-1080)*0.62:0",
              "eq=contrast=1.05:saturation=1.1:brightness=-0.03,colorbalance=rs=.04:bs=-.02:rh=.03"),
    "feet": ("px-20549082.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920", "eq=contrast=1.04:saturation=1.05,colorbalance=rs=.03:bs=.02"),
    "micro": ("px-4710717.mp4", "scale=1080:-2:flags=lanczos", "eq=contrast=1.03:saturation=0.9,colorbalance=rs=.03:bs=-.02"),
    "microbg": ("px-4710717.mp4", "scale=-2:1920,crop=1080:1920,boxblur=28:2", "eq=saturation=0.8:brightness=0.03,colorbalance=rs=.06:bs=-.02"),
    "candle": ("px-11350957.mp4", "scale=1080:1920", "eq=contrast=1.03:saturation=1.0:brightness=-0.02"),
    "curtain": ("px-35434114.mp4", "scale=1080:1920", "eq=contrast=1.02:saturation=1.0,colorbalance=rs=.05:bs=-.03"),
    "wake": ("px-7592151.mp4", "scale=-2:1920:flags=lanczos,crop=1080:1920", "eq=contrast=1.02:saturation=1.0,colorbalance=rs=.05:gs=.01:bs=-.02"),
    "matcha": ("px-5935128.mp4", "scale=1080:1920", "eq=contrast=1.03:saturation=1.02,colorbalance=rs=.05:bs=-.03"),
})

# clean floating text: very soft shadow only (Oct 16 1:25 pm rule)
SOFT = "text-shadow:0 4px 28px rgba(0,0,0,.30),0 1px 3px rgba(0,0,0,.18)"
BASE = H.EXTRA_CSS + f"""
.HD{{font-family:'Inter Display';font-weight:800;color:#fff;letter-spacing:-.035em;line-height:.98;{SOFT}}}
.SR{{font-family:'Instrument Serif';color:#fff;line-height:1;{SOFT}}}
"""


# ---------------------------------------------------------------------------------------------- voice
def word_times(name):
    d = json.load(open(VOICE / f"{name}.json"))
    a = d.get("normalized_alignment") or d["alignment"]
    out, cur, ws, we = [], [], None, None
    for c, s, e in zip(a["characters"], a["character_start_times_seconds"], a["character_end_times_seconds"]):
        if not c.strip():
            if cur:
                out.append(("".join(cur), ws, we))
                cur = []
            continue
        if not cur:
            ws = s
        cur.append(c)
        we = e
    if cur:
        out.append(("".join(cur), ws, we))
    return out


def place_vo(name, plan, out, tempo=1.0):
    """plan: [(first_word, last_word, t)] word indexes inclusive. Cuts each phrase from the take and places it at t.
    Returns [(t0, t1)] speech spans (for ducking and for checking text sync)."""
    ws = word_times(name)
    ins, fc, spans = [], [], []
    for k, (a, b, t) in enumerate(plan):
        s = max(0.0, ws[a][1] - 0.07)
        e = ws[b][2] + 0.16
        if b + 1 < len(ws):
            e = min(e, ws[b + 1][1] - 0.03)
        ins += ["-i", str(VOICE / f"{name}.mp3")]
        ms = int(t * 1000)
        fc.append(f"[{k}:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS,atempo={tempo},afade=t=in:d=0.02,"
                  f"afade=t=out:st={max(0.0, (e - s) / tempo - 0.05):.3f}:d=0.05,adelay={ms}|{ms}[v{k}]")
        spans.append((round(t, 2), round(t + (e - s) / tempo, 2), " ".join(w[0] for w in ws[a:b + 1])))
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
        b = b * (1 + 0.08 / 12) + 300
    return round(b), 300 * 480


FF_CSS = BASE + """
.SR i,.cor{color:#FFB08F}
.ink{color:#0E1440;text-shadow:0 2px 20px rgba(255,244,230,.55)}
.ink .cor,.ink i{color:#E2501F}
.nw{white-space:nowrap}
.sk{background:#FF6A3D}
.rc{position:relative;width:780px;background:#F7F1E5;padding:46px 54px 70px;box-shadow:0 34px 70px rgba(5,8,30,.35);
  clip-path:polygon(0 0,100% 0,100% calc(100% - 22px),95% 100%,90% calc(100% - 22px),85% 100%,80% calc(100% - 22px),75% 100%,
  70% calc(100% - 22px),65% 100%,60% calc(100% - 22px),55% 100%,50% calc(100% - 22px),45% 100%,40% calc(100% - 22px),35% 100%,
  30% calc(100% - 22px),25% 100%,20% calc(100% - 22px),15% 100%,10% calc(100% - 22px),5% 100%,0 calc(100% - 22px))}
.rh{font:800 30px/1 Inter;letter-spacing:.22em;color:#2B3FE0;text-align:center}
.rs{font:600 26px/1 Inter;letter-spacing:.16em;color:#6B7096;text-align:center;margin-top:14px}
.dash{border-top:4px dashed rgba(14,20,64,.22);margin:26px 0}
.rr{display:flex;justify-content:space-between;align-items:baseline;font:600 44px/1.25 Inter;color:#0E1440;padding:8px 0}
.rr b{font:800 50px/1 'Inter Display';color:#0E1440;font-variant-numeric:tabular-nums}
.tot{font:800 30px/1 Inter;letter-spacing:.16em;color:#FF6A3D;margin-top:4px}
.big{white-space:nowrap;font:800 84px/1 'Inter Display';color:#FF6A3D;letter-spacing:-.03em;font-variant-numeric:tabular-nums;margin-top:10px}
.paid{font:700 30px/1.3 Inter;color:#6B7096;margin-top:16px}
.bars{height:54px;margin-top:22px;background:repeating-linear-gradient(90deg,#0E1440 0 4px,transparent 4px 9px,#0E1440 9px 11px,transparent 11px 17px)}
"""


def ff_hook():
    return "".join([ft("jam", 0.0), '<div class="grain" style="opacity:.55"></div>',
                    el('<div class="HD nw" style="font-size:128px">What\'s money</div>'
                       '<div class="SR nw" style="font-size:150px;margin-top:18px"><i style="color:#fff">actually for?</i></div>',
                       "c", 330, a="none")])


def ff_tuesdays():
    total, paid = ff_math()
    r = H.HReel("ff-hero-1016-tuesdays", "fullyfunded", bpm=60, css=FF_CSS, stage="#0E1440")
    # 1 hook (0-2.9): traffic, the question
    r.scene(2.9, ff_hook(), cam="push")
    # 2 (2.9-4.3): not the car
    r.scene(1.8, "".join([ft("jam", 3.2), '<div class="grain" style="opacity:.55"></div>',
                          el('<span class="strike">Not the car.<span class="sk" data-a="strike" data-t="0.55" data-d="0.3"></span></span>',
                             "c", 420, a="pop", t=0.0, d=0.3, cls="HD", style="font-size:150px")]),
            tin="whipL", cam="left", shake=(0.55, 0.25, 10))
    # 3 (4.3-5.4): This.
    r.scene(1.1, "".join([ft("coffee", 0.4), words("This.", "c", 330, t=0.05, cls="HD ink", style="font-size:220px")]),
            tin="flash", td=0.45, color="#FFB08F", color2="#FFF4E0", cam="push")
    # 4: a Tuesday that's yours
    r.scene(3.0, "".join([ft("coffee", 1.5), words("A Tuesday morning / that's *all yours.*", "c", 330, t=0.1, gap=0.12, cls="HD ink",
                                                     em_cls="cor", style="font-size:104px")]),
            tin="zoom", focus=(560, 1250), cam="pull")
    # 5 (8.2-10.5): no alarm, no traffic
    r.scene(2.3, "".join([ft("beach", 3.0), words("No alarm.", "c", 330, t=0.1, gap=0.1, cls="HD ink", style="font-size:140px"),
                          words("No traffic.", "c", 500, t=0.85, gap=0.1, cls="HD ink", style="font-size:140px")]),
            tin="slit", color="#FF6A3D", color2="#F7F1E5", cam="rise")
    # 6 (10.5-16.1): THE FREEDOM RECEIPT prints up over the water
    rows = [("$300", "a month", 0.3), ("from age", "25", 0.85), ("at", "8% a year", 1.85)]
    rr = "".join(f'<div class="rr" data-a="up" data-t="{t:.2f}" data-d="0.3"><span>{a}</span><b>{b}</b></div>' for a, b, t in rows)
    receipt = ('<div class="rc"><div class="rh">FREEDOM RECEIPT</div><div class="rs">TUESDAY · 10:12 AM · THE SEA</div>'
               f'<div class="dash"></div>{rr}<div class="dash" data-a="fade" data-t="2.75" data-d="0.2"></div>'
               '<div data-a="up" data-t="2.85" data-d="0.3"><div class="tot">BY 65</div>'
               f'<div class="big">over $<span data-a="count" data-t="2.9" data-d="1.0" data-from="{paid}" data-to="{1_000_000}" '
               f'data-comma="1">{paid:,}</span></div>'
               f'<div class="paid">You paid in ${paid:,}. Time did the rest.</div></div><div class="bars" data-a="fade" data-t="3.9" data-d="0.3"></div></div>')
    r.scene(5.2, "".join([ft("feet", 2.0), el(receipt, 150, 470, 780, a="up", t=0.0, d=0.55, r=-1.5)]),
            tin="slam", cam="push")
    # 7 (16.1-19.3): buy back your Tuesdays
    r.scene(3.3, "".join([ft("beach", 9.0),
                          words("Start small.", "c", 330, t=0.1, gap=0.12, cls="HD ink", style="font-size:120px"),
                          words("Buy back / your *Tuesdays.*", "c", 490, t=0.9, gap=0.14, cls="HD ink", em_cls="cor", style="font-size:128px"),
                          el(f'<img src="{asset(H.FF["mark"])}" style="width:116px;height:116px;border-radius:50%;background:#fff;'
                             'box-shadow:0 8px 30px rgba(0,0,0,.25)">', "c", 1210, a="pop", t=1.9)]),
            tin="flash", td=0.5, color="#FFB08F", color2="#FFFFFF", cam="pull")
    r.loop(0.45, tin="zoom", focus=(540, 900))
    plan = [(0, 3, 0.25), (4, 6, 3.0), (7, 7, 4.85), (8, 13, 5.95), (14, 17, 8.95), (18, 33, 11.3), (34, 39, 16.65)]
    return r, dict(voice=("ff-tuesdays-v3", plan, 1.06), music=LIB / "v3" / "ff-c-confident-build-el.mp3",
                   sfx=[("sfx-city-rush", 4.7, 0.0, -12), ("sfx-whoosh-soft", 0.85, 2.85, -12), ("sfx-whoosh-soft", 0.85, 5.75, -14),
                        ("sfx-waves", 6.0, 8.8, -9), ("sfx-paper", 0.73, 11.1, -6), ("sfx-tick-ding", 1.04, 15.0, -10),
                        ("sfx-waves", 6.0, 15.6, -11)])


R["ff-hero-1016-tuesdays"] = ff_tuesdays


# ============================================================================================== LITTLEFOLD
LF_CSS = BASE + """
.H{font-family:Lora;font-weight:600;color:#FFF4E0;letter-spacing:-.02em;line-height:1.06;text-shadow:0 4px 28px rgba(42,15,37,.38),0 1px 3px rgba(42,15,37,.2)}
.em{font-style:italic;color:#FFD6E3}
.ink{color:#2C2A3A;text-shadow:0 2px 20px rgba(255,248,236,.6)}.emb{font-style:italic;color:#C2335F}
.vid{border-radius:44px;overflow:hidden;box-shadow:0 40px 80px rgba(42,15,37,.45);position:relative;width:960px;height:540px}
.vid .ft{position:absolute;inset:0}
.blob{position:absolute;inset:0;background:
  radial-gradient(420px 420px at 6% 8%, #FFD6E3 0 60%, transparent 61%),
  radial-gradient(360px 360px at 100% 22%, #FFE27E 0 58%, transparent 59%),
  radial-gradient(520px 520px at 96% 100%, #FFD3AE 0 60%, transparent 61%), #FFF4E0}
.dots{position:absolute;inset:0;background:radial-gradient(circle,rgba(217,73,122,.10) 2.2px,transparent 2.8px) 0 0/34px 34px}
.note{font-family:'Caveat Brush';color:#D9497A}
.lab{font:700 30px/1 Inter;letter-spacing:.16em;color:#D9497A}
"""


def rosette(label="Warm tea"):
    """Sherbet award rosette (SVG scallops + ribbon tails), built in code."""
    import math
    sc = "".join(f'<circle cx="{200 + 150 * math.cos(k * math.pi / 12):.1f}" cy="{200 + 150 * math.sin(k * math.pi / 12):.1f}" r="34" fill="#D9497A"/>'
                 for k in range(24))
    return (f'<svg width="400" height="560" viewBox="0 0 400 560" style="filter:drop-shadow(0 22px 26px rgba(42,15,37,.35))">'
            '<path d="M120 300 L70 540 L125 505 L160 560 L200 330 Z" fill="#E8743B"/>'
            '<path d="M280 300 L330 540 L275 505 L240 560 L200 330 Z" fill="#FF8A70"/>'
            f'{sc}<circle cx="200" cy="200" r="150" fill="#D9497A"/><circle cx="200" cy="200" r="124" fill="#FFD6E3"/>'
            '<circle cx="200" cy="200" r="108" fill="#FFF4E0" stroke="#D9497A" stroke-width="4" stroke-dasharray="6 9"/>'
            '<text x="200" y="168" text-anchor="middle" font-family="Inter" font-weight="800" font-size="26" letter-spacing="5" fill="#D9497A">SMALL WIN</text>'
            f'<text x="200" y="232" text-anchor="middle" font-family="Lora" font-style="italic" font-weight="600" font-size="52" fill="#2C2A3A">{label}</text>'
            '<text x="200" y="276" text-anchor="middle" font-family="Inter" font-weight="700" font-size="22" letter-spacing="4" fill="#E8743B">★ ★ ★</text></svg>')


def lf_hook():
    return "".join([ft("microbg", 0.0), el(f'<div class="vid">{ft("micro", 0.0)}</div>', 60, 820, 960, a="none", r=-2),
                    el('<div class="H ink" style="font-size:150px">Tea #1.</div><div class="H ink" style="font-size:120px;margin-top:14px">'
                       '<span class="emb">Reheated twice.</span></div>', "c", 300, a="none")])


def lf_warm_tea():
    r = H.HReel("lf-hero-1016-warm-tea", "littlefold", bpm=60, css=LF_CSS, stage="#2A0F25")
    # 1 hook (0-3.5): the microwave, again
    r.scene(3.5, lf_hook(), cam="push")
    # 2 (3.5-5.6): nobody claps
    r.scene(2.6, "".join([ft("candle", 2.0), words("Nobody claps / *for this part.*", "c", 360, t=0.1, gap=0.12, cls="H",
                                                     style="font-size:118px")]),
            tin="push", cam="pull")
    # 3 (5.6-6.9): then one morning
    r.scene(1.7, "".join([ft("curtain", 0.5), words("Then one / *morning,*", "c", 1230, t=0.05, gap=0.12, cls="H",
                                                      style="font-size:130px")]),
            tin="blob", color="#FFD3AE", focus=(540, 900), cam="rise")
    # 4 (6.9-8.3): the light comes in
    r.scene(2.1, "".join([ft("wake", 1.0), words("the light / *comes in.*", "c", 1430, t=0.05, gap=0.12, cls="H ink", em_cls="emb",
                                                   style="font-size:130px")]),
            tin="flash", color="#FFE27E", color2="#FFF4E0", cam="push")
    # 5 (8.3-9.9): and you drink it warm
    r.scene(2.4, "".join([ft("matcha", 0.2), words("and you drink it / *warm.*", "c", 330, t=0.05, gap=0.1, cls="H ink", em_cls="emb",
                                                     style="font-size:118px")]),
            tin="whipU", cam="push")
    # 6 (9.9-11.6): freeze, the rosette stamps on: SMALL WIN
    r.scene(1.8, "".join([ft("matcha", 2.6, sp=0.0, style="filter:saturate(.85) brightness(1.03)"),
                          el(rosette(), 340, 360, 400, a="stamp", t=0.05, d=0.35, r=-8),
                          words("That *counts.*", "c", 1060, t=0.45, gap=0.12, cls="H ink", em_cls="emb", style="font-size:120px")]),
            tin="cut", cam="push", shake=(0.12, 0.2, 9))
    # 7 (11.6-14.2): Sherbet end card
    r.scene(3.4, "".join(['<div class="blob"></div><div class="dots"></div>',
                          words("Small wins / *count.*", "c", 420, t=0.05, gap=0.12, cls="H ink", em_cls="emb", style="font-size:150px"),
                          el('<span class="note">Send this to a tired parent ♡</span>', "c", 820, a="up", t=0.7, style="font-size:74px"),
                          el(f'<img src="{asset(H.LF["mark"])}" style="width:116px;height:116px;border-radius:50%;background:#fff;'
                             'box-shadow:0 10px 30px rgba(122,33,73,.25)">', "c", 1180, a="pop", t=1.1)]),
            tin="blob", color="#FFD6E3", focus=(540, 1000), cam="push")
    r.loop(0.8, tin="zoom", focus=(540, 1000))
    plan = [(0, 4, 0.2), (5, 9, 3.65), (10, 12, 6.2), (13, 16, 7.85), (17, 21, 10.0), (22, 23, 12.6), (24, 26, 14.3)]
    return r, dict(voice=("lf-warm-tea-v3", plan, 1.0), music=LIB / "v3" / "lf-c-sunny-morning-el.mp3",
                   sfx=[("sfx-whoosh-soft", 0.85, 3.4, -16), ("sfx-whoosh-soft", 0.85, 9.8, -16), ("sfx-tick-ding", 1.04, 12.35, -12),
                        ("sfx-paper", 0.73, 14.1, -10)])


R["lf-hero-1016-warm-tea"] = lf_warm_tea


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

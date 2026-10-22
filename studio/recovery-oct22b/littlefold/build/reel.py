#!/usr/bin/env python3
"""Littlefold sunlit Reels (recovery Oct 22b). 1080x1920, 30 fps, H.264 + AAC, <=15 s.

Motion grammar ("washing-line morning"):
  frame 0  the rule is already on screen, first garment already pegged, sleepy sun low behind the hills;
  0.3 s    source chip pops (something moves immediately);
  each beat  previous words lift away (0.15 s), the new words unfold top-to-bottom (0.35 s), a new little garment
             drops onto the line with a damped swing, with a soft pop SFX on the music grid; the sun rises a step;
  last beat  "Do this": the sky warms to full morning and the sun opens its eyes (the recurring payoff);
  end        garments lift off and the hook fades back in, so the loop lands on frame 0.
"""
import math
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops

sys.path.insert(0, str(Path(__file__).parent))
from sunart import *  # noqa
import stills as ST  # noqa

W, H, FPS = 1080, 1920, 30
OUT = ST.OUT
LIB = REPO / "media" / "music" / "library"


def ease(t):
    t = min(max(t, 0), 1)
    return 1 - (1 - t) ** 3


def full(body, name):
    return render(page(W, H, body, transparent=True), SCR / f"{name}.png", W, H, transparent=True)


def crop(im):
    bb = im.getbbox() or (0, 0, 1, 1)
    return im.crop(bb), bb[:2]


def text_layers(b):
    main = (f'<div class="hand" style="position:absolute;left:90px;width:900px;top:{b.get("ky", 560)}px;font-size:72px;color:{KICK}">{b["kick"]}</div>'
            + K.dual(b["head"], F, cls="S fit", style=f"position:absolute;left:100px;width:880px;top:{b.get('hy', 650)}px;white-space:nowrap;font-size:{b.get('fs', 158)}px;color:{INK}")
            + (f'<div class="lora" style="position:absolute;left:80px;width:920px;top:{b.get("sy", 1150)}px;font-size:{b.get("ss", 56)}px;line-height:1.2;text-align:center;color:{INK}">{b["sub"]}</div>' if b.get("sub") else ""))
    chip = ST.chip(b["chip"], 1300)
    return crop(full(main, "t")), crop(full(chip, "c"))


def build(spec, tag):
    beats = spec["beats"]
    kinds = spec["sky"]
    skyA = render(page(W, H, sky(W, H, kinds[0], horizon=0.77)), SCR / "skyA.jpg", W, H).convert("RGBA")
    skyB = render(page(W, H, sky(W, H, kinds[1], horizon=0.77)), SCR / "skyB.jpg", W, H).convert("RGBA")
    rays = svg_img(rays_svg(1500), 1500, 1500, "rays")
    sun0 = svg_img(sun_svg(520, False), 520, 520, "sun0")
    sun1 = svg_img(sun_svg(520, True), 520, 520, "sun1")
    hills = full(f'<div style="position:absolute;left:0;top:0">{hills_svg(W, H, top=1460)}</div>', "hills")
    c1 = svg_img(cloud_svg(360), 360, 152, "cl1")
    c2 = svg_img(cloud_svg(300), 300, 126, "cl2")
    line = full(f'<div style="position:absolute;left:0;top:0">{line_svg(W, H, 300, 50)}</div>', "line")
    gw = 150
    gar = [svg_img(garment_svg(k, gw), gw, int(gw * 220 / 170), f"g{i}") for i, k in enumerate(spec["garments"])]
    stamp = crop(full(K.stamp(B, 66, 1380, size=150, rot=-10), "stamp"))
    TL = [text_layers(b) for b in beats]

    durs = [b["dur"] for b in beats]
    starts = np.cumsum([0] + durs[:-1])
    body_end = sum(durs)
    LOOP = spec["loop"]
    total = body_end + LOOP
    n = int(round(total * FPS))
    fdir = SCR / f"{tag}-frames"
    shutil.rmtree(fdir, ignore_errors=True)
    fdir.mkdir(parents=True)
    sun_ys = spec["sun_y"]
    last = len(beats) - 1
    pops = []

    def paste(fr, im, xy, alpha=1.0):
        if alpha <= 0.003:
            return
        if alpha < 0.999:
            a = im.getchannel("A").point(lambda v: int(v * alpha))
            im = im.copy()
            im.putalpha(a)
        x, y = int(round(xy[0])), int(round(xy[1]))
        # clip to frame
        if x >= W or y >= H or x + im.width <= 0 or y + im.height <= 0:
            return
        cx0, cy0 = max(0, -x), max(0, -y)
        cx1, cy1 = min(im.width, W - x), min(im.height, H - y)
        fr.alpha_composite(im.crop((cx0, cy0, cx1, cy1)), (x + cx0, y + cy0))

    for f in range(n):
        t = f / FPS
        loop_k = None
        if t >= body_end:
            loop_k = (t - body_end) / LOOP
            i = last
        else:
            i = int(np.searchsorted(starts, t, side="right") - 1)
        lt = t - starts[i]
        # sky + sun progress
        prog = (i + min(lt / durs[i], 1)) / len(beats)
        d = spec["sky_mix"](i, lt, prog)
        if loop_k is not None:
            d = d * (1 - ease(loop_k))
        fr = Image.blend(skyA, skyB, d) if d > 0.002 else skyA.copy()
        sy = np.interp(prog, np.linspace(0, 1, len(sun_ys)), sun_ys)
        if i == last:
            sy -= 12 * ease((lt - 0.1) / 0.6)
        if loop_k is not None:
            sy = sy * (1 - ease(loop_k)) + sun_ys[0] * ease(loop_k)
        sx = W / 2
        ang = (t * 7) % 360
        r = rays.rotate(ang, resample=Image.BILINEAR)
        paste(fr, r, (sx - 750, sy - 750), alpha=0.45 + 0.4 * d)
        breath = 1 + 0.015 * math.sin(2 * math.pi * t / 2.4)
        awake = 0.0
        if i == last and loop_k is None:
            awake = ease((lt - 0.35) / 0.25)
        if loop_k is not None:
            awake = 1 - ease(loop_k * 2)
        for im, al in ((sun0, 1 - awake), (sun1, awake)):
            if al > 0.003:
                s = breath * (1 + (0.06 * math.sin(min(max((lt - 0.35) / 0.4, 0), 1) * math.pi) if i == last else 0))
                im2 = im.resize((int(520 * s), int(520 * s)), Image.BILINEAR) if abs(s - 1) > 1e-3 else im
                paste(fr, im2, (sx - im2.width / 2, sy - im2.height / 2), alpha=al)
        paste(fr, hills, (0, 0))
        paste(fr, c1, (-80 + 14 * t, 150), alpha=.95)
        paste(fr, c2, (W - 320 - 10 * t, 228), alpha=.9)
        paste(fr, line, (0, 0))
        # garments
        for g in range(len(beats)):
            if g > i:
                continue
            gx = ST.XS[g]
            gy = line_y(gx, 300, 50, W)
            gl = t - starts[g]
            drop = 0 if g == 0 else 70 * (1 - ease(gl / 0.32))
            gal = 1 if g == 0 else min(1, gl / 0.12)
            rot = spec["sway"] * math.sin(2 * math.pi * t / 2.6 + g * 1.3)
            if g > 0:
                rot += 16 * math.exp(-4.5 * gl) * math.cos(11 * gl)
            if loop_k is not None and g > 0:
                gal *= 1 - ease(loop_k / 0.7)
                drop -= 60 * ease(loop_k / 0.7)
            im = gar[g]
            px, py = gw / 2, 14 * gw / 170  # peg point
            # rotate about the peg: pad so the peg is the centre
            pad = Image.new("RGBA", (gw * 2, im.height * 2), (0, 0, 0, 0))
            pad.paste(im, (int(gw - px), int(im.height - py)))
            pr = pad.rotate(-rot, resample=Image.BICUBIC, center=(gw, im.height))
            paste(fr, pr, (gx - gw, gy - im.height - drop), alpha=gal)
        # text
        (tim, txy), (cim, cxy) = TL[i]
        if loop_k is None:
            if i > 0 and lt < 0.15:
                (pim, pxy), _ = TL[i - 1]
                paste(fr, pim, (pxy[0], pxy[1] - 40 * ease(lt / .15)), alpha=1 - ease(lt / 0.13))
            if i == 0:
                paste(fr, tim, txy)
            else:
                p = (lt - 0.12) / 0.38
                if p > 0:
                    if p < 1:
                        ramp = np.clip((ease(p) * (tim.height + 120) - np.arange(tim.height)) / 120, 0, 1)
                        m = Image.fromarray((np.repeat(ramp[:, None], tim.width, 1) * 255).astype(np.uint8), "L")
                        t2 = tim.copy()
                        t2.putalpha(ImageChops.multiply(tim.getchannel("A"), m))
                        paste(fr, t2, (txy[0], txy[1] + 26 * (1 - ease(p))))
                    else:
                        paste(fr, tim, txy)
            cp = (lt - (0.3 if i == 0 else 0.42)) / 0.2
            if cp > 0:
                paste(fr, cim, (cxy[0], cxy[1] + 12 * (1 - ease(cp))), alpha=min(1, cp))
        else:
            paste(fr, tim, txy, alpha=1 - ease(loop_k / 0.5))
            paste(fr, cim, cxy, alpha=1 - ease(loop_k / 0.5))
            (him, hxy), _ = TL[0]
            paste(fr, him, hxy, alpha=ease((loop_k - 0.3) / 0.7))
        paste(fr, stamp[0], stamp[1])
        fr.convert("RGB").save(fdir / f"{f:04d}.png", compress_level=1)
    pops = [starts[g] + 0.1 for g in range(1, len(beats))]
    return fdir, total, pops


def encode(fdir, total, music, pops, out_mp4):
    a = SCR / "a.wav"
    pop = LIB / "sfx-x-sticker-pop.mp3"
    inputs = ["-i", str(music)]
    filt = [f"[0:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.05,afade=t=out:st={total-0.9:.3f}:d=0.9[m]"]
    mix = ["[m]"]
    for k, p in enumerate(pops):
        inputs += ["-i", str(pop)]
        filt.append(f"[{k+1}:a]volume=0.22,adelay={int(p*1000)}|{int(p*1000)}[p{k}]")
        mix.append(f"[p{k}]")
    filt.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[o]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[o]", "-ar", "48000", "-ac", "2", str(a)], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(fdir / "%04d.png"), "-i", str(a),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "slow", "-crf", "18", "-profile:v", "high",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out_mp4)], check=True)
    shutil.rmtree(fdir)


B_SUN = 60 / 120.2      # lf-c-sunny-morning-el beat
B_TEN = 60 / 84.7       # lf-b-tender-el beat
SPECS = {
    "spoil": dict(
        out="lf-reel-1025am-cant-spoil-sun", music=LIB / "v3/lf-c-sunny-morning-el.mp3",
        sky=("dawn", "morning"), sun_y=[1470, 1450, 1430, 1410, 1390], sway=2.5, loop=0.4,
        sky_mix=lambda i, lt, prog: 0.55 * prog if i < 4 else 0.45 + 0.55 * ease((lt - 0.1) / 0.8),
        garments=["onesie", "sock", "bib", "hat", "dress"],
        beats=[
            dict(dur=5 * B_SUN, kick="heard “you'll spoil her”?", head="You can't / *spoil* a / newborn.", sub="Pick them up.", chip="CPS · Colic and crying"),
            dict(dur=6 * B_SUN, kick="because", head="Answer their / cries, and / they cry *less.*", fs=150, chip="AAP · Responding to your baby's cries"),
            dict(dur=5 * B_SUN, kick="first, check", head="Hungry? / Diaper? / *Too hot or cold?*", fs=146, chip="CPS · Colic and crying"),
            dict(dur=5 * B_SUN, kick="then", head="Hold close. / *Sway.* Shush. / Walk.", fs=150, chip="CPS · Colic and crying"),
            dict(dur=7 * B_SUN, kick="Do this:", head="Next cry: / *pick them up* / first.", sub="send this to someone in the newborn weeks", ss=42, chip="CPS · AAP"),
        ]),
    "stepaway": dict(
        out="lf-reel-1025-step-away-sun", music=LIB / "v3/lf-b-tender-el.mp3",
        sky=("afternoon", "morning"), sun_y=[1450, 1430, 1415, 1400, 1385], sway=4.0, loop=0.35,
        sky_mix=lambda i, lt, prog: 0.0 if i < 4 else 0.6 * ease((lt - 0.1) / 0.8),
        garments=["hat", "onesie", "sock", "dress", "bib"],
        beats=[
            dict(dur=4 * B_TEN, kick="still crying? at your limit?", head="It's OK to / *step away.*", fs=172, chip="CPS · Colic and crying"),
            dict(dur=3 * B_TEN, kick="first", head="Crib first. / *On their back.*", fs=160, chip="CPS · Colic and crying"),
            dict(dur=4 * B_TEN, kick="then", head="Step out. / Breathe. / *Take a moment.*", fs=146, chip="CPS · Colic and crying"),
            dict(dur=4 * B_TEN, kick="and always", head="Never shake / a baby. / *Never.*", fs=150, chip="CPS · Colic and crying"),
            dict(dur=5 * B_TEN, kick="Do this:", head="Tonight, pick / *who you'll text.*", sub="“Can you come?” It's OK to ask for help.", ss=44, fs=140, sy=1060, chip="CPS · Colic and crying"),
        ]),
}

if __name__ == "__main__":
    for key in (sys.argv[1:] or SPECS):
        s = SPECS[key]
        fdir, total, pops = build(s, key)
        out = OUT / f"{s['out']}.mp4"
        encode(fdir, total, s["music"], pops, out)
        print(out, round(total, 2))

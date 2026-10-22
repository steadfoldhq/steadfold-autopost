#!/usr/bin/env python3
"""Littlefold Night Light Reels (recovery Oct 22). 1080x1920, 30 fps, H.264 + AAC, <=15 s.

Grammar (v0.5 floor + v4 motion rules): frame 0 = the lamp circle already lit with the answer in it (rule + reassurance
open); something moves by 0.3 s (source chip pops); each beat widens the glow; every cut uses a different transition
(iris, push-up, zoom punch, whip, morning-light flood); the last beat is morning light; the end loops back to frame 0.
"""
import sys, subprocess, shutil, math
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))
from lfnl import *  # noqa
from PIL import Image

W, H, FPS = 1080, 1920, 30
OUT = REPO / "media" / "recovery-oct22" / "littlefold"
TMP = Path("/tmp/claude-0/-home-claude/60837be5-8cde-507a-87a7-2bafa6fa6f6c/scratchpad/reel")
CX, CY = 540, 790


def hexrgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)


YY, XX = np.mgrid[0:H, 0:W].astype(np.float32)
D = np.sqrt((XX - CX) ** 2 + (YY - CY) ** 2)
_g = np.asarray(Image.open(K.GRAIN).convert("RGBA").resize((420, 420))).astype(np.float32) / 255.0
GR = 1 - _g[..., 3] * (1 - _g[..., :3].mean(-1))  # effective multiply factor of the grain overlay
GR = np.tile(GR, (H // 420 + 1, W // 420 + 1))[:H, :W]


def grad(t, stops):
    out = np.zeros(t.shape + (3,), np.float32)
    xs = [s for s, _ in stops]
    for c in range(3):
        out[..., c] = np.interp(t, xs, [col[c] for _, col in stops])
    return out


NIGHT_OUT = [(0, hexrgb("#8A2B55")), (.4, hexrgb(DEEP)), (.75, hexrgb("#4E1A3C")), (1, hexrgb(INK))]
NIGHT_IN = [(0, hexrgb("#FFF4E2")), (.34, hexrgb("#FFE9C9")), (.58, hexrgb("#FFD3AE")), (.74, hexrgb("#FFBFA0"))]
DAY_IN = [(0, hexrgb("#FFF6D8")), (.4, hexrgb("#FFEDB0")), (.66, hexrgb("#FFE59A")), (1, hexrgb("#FFF1E3"))]


Dh = D[::2, ::2]


def bg(R, day=0.0):
    t = Dh / R
    outer = grad(np.clip(Dh / (2.4 * R), 0, 1), NIGHT_OUT)
    inner = grad(np.clip(t, 0, .74), NIGHT_IN)
    a = np.interp(t, [0, .74, 1.0], [1, .55, 0])[..., None]
    night = inner * a + outer * (1 - a)
    if day > 0:
        dd = grad(np.clip(Dh / (R * 1.15), 0, 1), DAY_IN)
        night = night * (1 - day) + dd * day
    up = np.asarray(Image.fromarray(np.clip(night, 0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)).astype(np.float32)
    g = 1 - (1 - GR[..., None]) * (.35 + .15 * day)
    return up * g


class Lay:
    """Pre-converted RGBA layer: float rgb and alpha, cropped to its bounding box for speed."""
    def __init__(self, im):
        bb = im.getbbox() or (0, 0, 1, 1)
        self.im = im
        self.bb = bb
        a = np.asarray(im.crop(bb)).astype(np.float32)
        self.rgb = a[..., :3]
        self.a = a[..., 3:4] / 255.0


def over(base, layer, x=0, y=0, alpha=1.0, scale=1.0, mask=None):
    if alpha <= 0.002:
        return base
    if abs(scale - 1) > 1e-3:
        im = layer.im
        w, h = int(W * scale), int(H * scale)
        L2 = im.resize((w, h), Image.BILINEAR)
        c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        c.paste(L2, ((W - w) // 2, (H - h) // 2))
        layer = Lay(c)
    x0, y0, x1, y1 = layer.bb
    x0 += int(x); x1 += int(x); y0 += int(y); y1 += int(y)
    cx0, cy0, cx1, cy1 = max(x0, 0), max(y0, 0), min(x1, W), min(y1, H)
    if cx0 >= cx1 or cy0 >= cy1:
        return base
    rgb = layer.rgb[cy0 - y0:cy1 - y0, cx0 - x0:cx1 - x0]
    a = layer.a[cy0 - y0:cy1 - y0, cx0 - x0:cx1 - x0] * alpha
    if mask is not None:
        a = a * mask[cy0:cy1, cx0:cx1, None]
    reg = base[cy0:cy1, cx0:cx1]
    base[cy0:cy1, cx0:cx1] = reg * (1 - a) + rgb * a
    return base


def ease(t):
    t = min(max(t, 0), 1)
    return 1 - (1 - t) ** 3


def beat_html(b, day=False):
    kcol = BERRY if day else DEEP
    chipcol = DEEP if day else CREAM
    main = (f'<div class="hand" style="position:absolute;left:90px;width:900px;top:{b.get("ky", 470)}px;font-size:64px;color:{kcol}">{b["kick"]}</div>'
            + K.dual(b["head"], F if not day else F, cls="S fit",
                     style=f"position:absolute;left:110px;width:860px;top:{b.get('hy', 580)}px;font-size:{b.get('fs', 150)}px;color:{INK}")
            + (f'<div class="lora" style="position:absolute;left:140px;width:800px;top:{b.get("sy", 1040)}px;font-size:54px;line-height:1.2;text-align:center;color:{INK}">{b["sub"]}</div>' if b.get("sub") else ""))
    chip = (f'<div style="position:absolute;left:0;right:0;top:1350px;text-align:center"><span class="chip" style="position:relative;display:inline-block;'
            f'color:{chipcol};font-size:30px">{b["chip"]}</span></div>')
    return page(W, H, main, transparent=True), page(W, H, chip, transparent=True)


def layers(spec, tag):
    TMP.mkdir(parents=True, exist_ok=True)
    out = []
    for i, b in enumerate(spec["beats"]):
        day = b.get("day", False)
        m, c = beat_html(b, day)
        pm = render(m, TMP / f"{tag}-b{i}.png", W, H, transparent=True)
        pc = render(c, TMP / f"{tag}-c{i}.png", W, H, transparent=True)
        out.append((Lay(Image.open(pm).convert("RGBA")), Lay(Image.open(pc).convert("RGBA"))))
    deco = render(page(W, H, lamp(800, 1080, 1.0), transparent=True), TMP / f"{tag}-lamp.png", W, H, transparent=True)
    st = render(page(W, H, K.stamp(B, 92, 1170, size=160, rot=-10), transparent=True), TMP / f"{tag}-stamp.png", W, H, transparent=True)
    return out, Lay(Image.open(deco).convert("RGBA")), Lay(Image.open(st).convert("RGBA"))


def build(spec, tag):
    beats = spec["beats"]
    L, lampL, stampL = layers(spec, tag)
    durs = [b["dur"] for b in beats]
    starts = np.cumsum([0] + durs[:-1])
    LOOP = 0.4
    total = sum(durs) + LOOP
    n = int(round(total * FPS))
    fdir = TMP / f"{tag}-frames"
    shutil.rmtree(fdir, ignore_errors=True)
    fdir.mkdir(parents=True)
    R0 = 470
    trans = ["none", "iris", "push", "zoom", "whip", "flood"]
    for f in range(n):
        t = f / FPS
        if t >= sum(durs):  # loop back to the hook frame
            k = (t - sum(durs)) / LOOP
            i = len(beats) - 1
            lt = t - starts[i]
        else:
            k = None
            i = int(np.searchsorted(starts, t, side="right") - 1)
            lt = t - starts[i]
        b = beats[i]
        R = R0 + 26 * i + 18 * math.sin(2 * math.pi * t / 3.2) + 10 * lt  # breathing, widening each beat
        dayv = 0.0
        if b.get("day"):
            dayv = ease(lt / 0.55)
        if k is not None:
            dayv = 1 - ease(k)
            R = R * (1 - k) + (R0 + 18 * math.sin(0)) * k
        frame = bg(R, dayv)
        frame = over(frame, lampL, alpha=1 - dayv)
        # previous beat quick exit (first 0.12 s of a beat)
        if i > 0 and lt < 0.12 and k is None:
            frame = over(frame, L[i - 1][0], y=-30 * lt / .12, alpha=1 - ease(lt / .1))
        tr = trans[min(i, len(trans) - 1)] if not b.get("day") else "flood"
        p = ease((lt - 0.08) / 0.32)
        x = y = 0
        sc = 1.0
        al = 1.0
        mask = None
        if i == 0 or tr == "none":
            pass
        elif tr == "iris":
            rr = p * 1400
            mask = np.clip((rr - D) / 40, 0, 1) if p < 1 else None
        elif tr == "push":
            y = 160 * (1 - p)
            al = p
        elif tr == "zoom":
            sc = 1.14 - 0.14 * p
            al = min(1, p * 1.6)
        elif tr == "whip":
            x = 420 * (1 - p)
            al = min(1, p * 1.4)
        elif tr == "flood":
            y = 60 * (1 - p)
            al = ease((lt - 0.15) / 0.4)
        drift = -8 * lt / b["dur"] if i > 0 else 0
        main_alpha = al
        if k is not None:
            main_alpha = 1 - ease(k / 0.6)
        frame = over(frame, L[i][0], x=x, y=y + drift, alpha=main_alpha, scale=sc, mask=mask)
        # chip pop (0.2-0.5 s into each beat; present at frame 0 only after the pop)
        cp = (lt - 0.2) / 0.3
        if cp > 0:
            s = 1 + 0.12 * math.sin(min(cp, 1) * math.pi) if cp < 1 else 1
            frame = over(frame, L[i][1], alpha=min(1, cp * 2) * (1 if k is None else 1 - ease(k / .6)), scale=1.0)
            if s != 1:
                pass
        if k is not None:  # hook fades back in
            frame = over(frame, L[0][0], alpha=ease(k))
        frame = over(frame, stampL)
        Image.fromarray(frame.astype(np.uint8)).save(fdir / f"{f:04d}.png", compress_level=1)
    return fdir, total


def encode(fdir, total, music, out_mp4):
    a = TMP / "a.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(music), "-t", f"{total:.3f}",
                    "-af", f"afade=t=in:d=0.05,afade=t=out:st={total-1.0:.3f}:d=1.0,loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", str(a)], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(fdir / "%04d.png"), "-i", str(a),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "slow", "-crf", "17", "-profile:v", "high",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out_mp4)], check=True)
    shutil.rmtree(fdir)


def cover(spec, out_jpg):
    c = spec["cover"]
    day = c.get("day", False)
    bgh = night_bg(W, H, cy=.41, r=(.62 if day else .50), day=day)
    body = (bgh + (lamp(800, 1080, 1.0) if not day else K.obj("shoe", 700, 1110, 250, rot=-8))
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:430px;font-size:72px;color:{BERRY if day else DEEP}">{c["kick"]}</div>'
            + K.dual(c["head"], F, cls="S fit", style=f"position:absolute;left:100px;width:880px;top:560px;font-size:{c.get('fs', 160)}px;color:{INK}")
            + (f'<div class="lora" style="position:absolute;left:140px;width:800px;top:{c.get("sy", 1080)}px;font-size:56px;text-align:center;color:{INK}">{c["sub"]}</div>' if c.get("sub") else "")
            + K.stamp(B, 92, 1170, size=160, rot=-10))
    return render(page(W, H, body), out_jpg, W, H)


SPECS = {
    "spoil": dict(
        music=REPO / "media/music/library/v3/lf-c-sunny-morning-el.mp3",
        cover=dict(day=True, kick="heard “you'll spoil her”?", head="You can't / *spoil* a / newborn.", sub="Pick them up."),
        beats=[
            dict(dur=2.6, kick="heard “you'll spoil her”?", head="You can't / *spoil* a / newborn.", sub="Pick them up.", chip="CPS · Colic and crying"),
            dict(dur=3.0, kick="because", head="Answer their cries, / and they / cry *less.*", fs=140, chip="AAP · Responding to your baby's cries"),
            dict(dur=2.6, kick="first, check", head="Hungry? / Diaper? / *Too hot or cold?*", fs=140, chip="CPS · Colic and crying"),
            dict(dur=2.6, kick="then", head="Hold close. / *Sway.* Shush. / Walk.", chip="CPS · Colic and crying"),
            dict(dur=3.4, day=True, kick="Do this:", head="Next cry: / *pick them up* / first.", sub="send this to someone in the newborn weeks", chip="CPS · AAP"),
        ]),
    "stepaway": dict(
        music=REPO / "media/music/library/v3/lf-a-cosy-el.mp3",
        cover=dict(day=False, kick="still crying? at your limit?", head="It's OK to / *step away.*"),
        beats=[
            dict(dur=2.8, kick="still crying? at your limit?", head="It's OK to / *step away.*", chip="CPS · Colic and crying"),
            dict(dur=2.6, kick="first", head="Crib first. / *On their back.*", chip="CPS · Colic and crying"),
            dict(dur=3.0, kick="then", head="Step out. / Breathe. / *Take a moment.*", fs=140, chip="CPS · Colic and crying"),
            dict(dur=2.6, kick="and always", head="Never shake / a baby. / *Never.*", chip="CPS · Colic and crying"),
            dict(dur=3.4, day=True, kick="Do this:", head="Tonight, pick / *who you'll text.*", sub="“Can you come?” It's OK to ask for help.", fs=140, sy=1000, chip="CPS · Colic and crying"),
        ]),
}

if __name__ == "__main__":
    names = {"spoil": "lf-reel-1025am-cant-spoil", "stepaway": "lf-reel-1025-step-away-nl"}
    for key in ([a for a in sys.argv[1:] if not a.startswith("--")] or SPECS):
        spec = SPECS[key]
        base = names[key]
        print(cover(spec, OUT / f"{base}-cover.jpg"))
        if "--cover-only" in sys.argv:
            continue
        fdir, total = build(spec, key)
        encode(fdir, total, spec["music"], OUT / f"{base}.mp4")
        print(OUT / f"{base}.mp4", total)

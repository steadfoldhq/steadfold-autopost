#!/usr/bin/env python3
"""60 s music sampler: the 12 Oct 16 impact tracks, 5 s each, cut 2 s before -> 3 s after each MEASURED drop
(tools/music-library.json), with the track name, page, tempo, live spectrum bars and a flash on the drop.

    python3 studio/styles/sampler.py OUT.mp4
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

REPO = Path(__file__).resolve().parents[2]
LIB = json.load(open(REPO / "tools/music-library.json"))
SR, FPS, W, H, SEG, PRE = 44100, 30, 1080, 1920, 5.0, 2.0
FB = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
FD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
PAGES = {"ff": ("Fully Funded", "#2B3FE0", "#F5F7FF", "#FF6A3D"), "lh": ("Locked Hour", "#FFE27A", "#141414", "#FF5CA8"),
         "hb": ("Hourback", "#5E54C9", "#FFF8EF", "#FFC94D"), "lf": ("Littlefold", "#FFD6E3", "#2C2A3A", "#D9497A")}
ORDER = ["lh-x-lock-in", "lh-x-phone-down", "lh-x-tick-boom", "ff-x-money-moves", "ff-x-level-up", "ff-x-big-reveal",
         "hb-x-smart-bounce", "hb-x-ta-da-funk", "hb-x-future-easy", "lf-x-sunny-bounce", "lf-x-giggle-pop", "lf-x-tiny-parade"]


def title(name):
    return " ".join(w.capitalize() for w in name.split("-")[2:]).replace("Ta Da", "Ta-Da")


def decode(p):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, "<f4").reshape(-1, 2).copy()


def hexrgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def main(out):
    out = Path(out)
    work = out.parent / "_sampler"
    (work / "f").mkdir(parents=True, exist_ok=True)
    segs = []
    for name in ORDER:
        m = LIB["tracks"][name]
        x = decode(REPO / m["file"])
        a = int(max(0, m["drop_s"] - PRE) * SR)
        s = x[a:a + int(SEG * SR)]
        if len(s) < SEG * SR:
            s = np.r_[s, np.zeros((int(SEG * SR) - len(s), 2), np.float32)]
        fi, fo = int(0.02 * SR), int(0.12 * SR)
        s[:fi] *= np.linspace(0, 1, fi)[:, None]
        s[-fo:] *= np.linspace(1, 0, fo)[:, None]
        segs.append(s)
    audio = np.concatenate(segs)
    wav = work / "a.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", str(wav)],
                   input=audio.astype("<f4").tobytes(), check=True)
    mono = audio.mean(1)
    big, mid, small = ImageFont.truetype(FB, 132), ImageFont.truetype(FD, 46), ImageFont.truetype(FD, 36)
    huge = ImageFont.truetype(FB, 230)
    nfr = int(len(ORDER) * SEG * FPS)
    NB = 28
    prev = np.zeros(NB)
    for fi in range(nfr):
        t = fi / FPS
        k = min(len(ORDER) - 1, int(t // SEG))
        lt = t - k * SEG
        name = ORDER[k]
        m = LIB["tracks"][name]
        page, bg, ink, acc = PAGES[name[:2]]
        im = Image.new("RGB", (W, H), hexrgb(bg))
        d = ImageDraw.Draw(im)
        # spectrum of the last 2048 samples
        c = int(t * SR)
        win = mono[max(0, c - 2048):c]
        if len(win) < 2048:
            win = np.r_[np.zeros(2048 - len(win)), win]
        sp = np.abs(np.fft.rfft(win * np.hanning(2048)))
        edges = np.geomspace(2, 700, NB + 1).astype(int)
        bands = np.array([sp[edges[i]:max(edges[i] + 1, edges[i + 1])].mean() for i in range(NB)])
        bands = np.clip(np.log1p(bands * 4) / 3.2, 0, 1)
        prev = np.maximum(bands, prev * 0.82)
        beat = 60 / m["bpm"]
        since_drop = lt - PRE
        flash = max(0.0, 1 - since_drop / 0.35) if since_drop >= 0 else 0.0
        pulse = np.exp(-((since_drop % beat) if since_drop >= 0 else ((lt - PRE) % beat)) / 0.12)
        # drop flash: accent colour washes the frame for a moment
        if flash > 0:
            ov = Image.new("RGB", (W, H), hexrgb(acc))
            im = Image.blend(im, ov, 0.55 * flash)
            d = ImageDraw.Draw(im)
        cx, base = W // 2, 1480
        bw = 26
        for i in range(NB):
            h = 40 + prev[i] * 400 * (1 + 0.2 * flash)
            x0 = cx - NB * (bw + 8) // 2 + i * (bw + 8)
            d.rounded_rectangle([x0, base - h, x0 + bw, base], radius=13, fill=hexrgb(acc if i % 3 == 0 else ink))
        d.text((80, 150), "STEADFOLD SOUND  ·  NEW HITS", font=small, fill=hexrgb(ink))
        d.text((W - 80, 150), f"{k + 1:02d} / 12", font=small, fill=hexrgb(ink), anchor="ra")
        d.rounded_rectangle([80, 260, 80 + d.textlength(page, font=mid) + 60, 340], radius=40, fill=hexrgb(acc))
        d.text((110, 274), page, font=mid, fill=(255, 255, 255) if name[:2] != "lh" else hexrgb("#141414"))
        tt = title(name)
        s = 1 + 0.03 * pulse
        f2 = ImageFont.truetype(FB, int(132 * s))
        d.multiline_text((80, 420), tt.replace(" ", "\n", 1) if len(tt) > 12 else tt, font=f2, fill=hexrgb(ink), spacing=4)
        d.text((80, 760), f"{m['bpm']:.0f} BPM  ·  drop at {m['drop_s']:.1f} s{'  (built)' if m.get('drop_built') else ''}", font=mid, fill=hexrgb(ink))
        d.text((80, 830), name + ".mp3", font=small, fill=hexrgb(ink))
        if since_drop >= 0 and since_drop < 0.9:
            u = min(1, since_drop / 0.12)
            fnt = ImageFont.truetype(FB, int(230 * (1.6 - 0.6 * u)))
            d.text((cx, 1620), "DROP", font=fnt, fill=hexrgb(acc if flash < 0.5 else ink), anchor="mm")
        else:
            d.text((cx, 1620), "▶  drop in " + (f"{-since_drop:.1f}s" if since_drop < 0 else "✓"), font=mid, fill=hexrgb(ink), anchor="mm")
        # progress bar for this card
        d.rounded_rectangle([80, 1780, 80 + (W - 160) * lt / SEG, 1796], radius=8, fill=hexrgb(acc))
        im.save(work / "f" / f"{fi:05d}.jpg", quality=92)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", str(work / "f" / "%05d.jpg"), "-i", str(wav),
                    "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "44100", "-shortest", "-movflags", "+faststart", str(out)], check=True)
    subprocess.run(["rm", "-rf", str(work)])
    print(out)


if __name__ == "__main__":
    main(sys.argv[1])

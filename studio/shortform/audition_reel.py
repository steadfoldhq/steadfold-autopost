"""House-voice audition reel (Oct 16 2026): the 3 cast voices saying the same 2 lines, ~30 s, music bed under it.
Each voice clip is ONE continuous slice of its Eleven v3 audition take (no edits inside a line).
Usage: python3 studio/shortform/audition_reel.py OUT.mp4"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2 import (FPS, H, LIB, REPO, SR, W, T, _BG, _decode, _decode_st, _loop, _lufs_arr, dots_bg, hexc, master,  # noqa: E402
                pop, words_from_alignment)

AUD = os.path.join(REPO, "media/voice/audition/")
FIRST, LAST = "Who", "how?!"            # line 1: "Who has more at sixty-five? Wait, you're gonna LOVE this one!"  line 2: "It's seven forty-three... how?!"
CAST = json.load(open(os.path.join(REPO, "tools/voices.json")))["voices"]
LOOK = {"Kayla": ("2B3FE0", "FFD63B", "FULLY FUNDED"), "Laura": ("FFE27A", "B0105A", "LOCKED HOUR"), "Liam": ("3A2240", "FFC94D", "HOURBACK")}


def clip(name):
    a = _decode(AUD + f"aud-{name.lower()}.mp3", SR)
    ws = words_from_alignment(json.load(open(AUD + f"aud-{name.lower()}.json")))
    i0 = next(i for i, w in enumerate(ws) if w[0] == FIRST)
    i1 = next(i for i, w in enumerate(ws) if w[0] == LAST)
    s, e = ws[i0][1] - 0.12, ws[i1][2] + 0.35
    seg = a[int(s * SR):int(e * SR)].copy()
    f = int(0.02 * SR)
    seg[:f] *= np.linspace(0, 1, f)
    seg[-f:] *= np.linspace(1, 0, f)
    return seg, [[w[0], w[1] - s, w[2] - s] for w in ws[i0:i1 + 1]]


def main(out):
    gap, intro = 0.6, 0.6
    parts, t = [], intro
    for v in CAST:
        seg, words = clip(v["name"])
        parts.append((v, seg, words, t))
        t += len(seg) / SR + gap
    total = t + 0.4
    n = int(total * SR)
    voice = np.zeros(n, np.float32)
    for v, seg, words, t0 in parts:
        i = int(t0 * SR)
        voice[i:i + len(seg)] += seg
    voice *= 10 ** ((-16 - _lufs_arr(voice)) / 20)
    bed = _loop(_decode_st(LIB + "v3/lh-a-focus-pulse-el.mp3"), n)
    bed *= 10 ** ((-16 - 17 - _lufs_arr(bed)) / 20)
    room = _loop(_decode_st(LIB + "amb-room-tone.mp3"), n, xf=2.0)
    room *= 10 ** ((-16 - 24 - _lufs_arr(room)) / 20)
    y = bed + room + voice[:, None]
    y[-int(0.4 * SR):] *= np.linspace(1, 0, int(0.4 * SR))[:, None]
    tmp = out + ".mix.wav"
    import wave
    with wave.open(tmp, "w") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
    import subprocess
    silent = out + ".video.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", silent],
                         stdin=subprocess.PIPE)
    for fi in range(int(total * FPS)):
        tt = fi / FPS
        cur = parts[0]
        for pt in parts:
            if tt >= pt[3] - gap / 2:
                cur = pt
        v, seg, words, t0 = cur
        bg, acc, page = LOOK[v["name"]]
        img = dots_bg(hexc(bg), (255, 255, 255, 20) if v["name"] != "Laura" else (20, 20, 20, 24), tt)
        ink = hexc("141414") if v["name"] == "Laura" else hexc("FFFFFF")
        q = min(1.0, pop(tt, t0 - gap / 2, 0.35))
        T(img, "HOUSE VOICE AUDITION", W / 2, 200, 54, ink, f="xbold", key="title")
        T(img, v["name"].upper(), W / 2, 520, 240, hexc(acc), key=v["name"], scale=0.8 + 0.2 * q)
        T(img, page, W / 2, 720, 70, ink, key=page)
        T(img, "Eleven v3 · one take", W / 2, 810, 46, ink, f="semi", key="v3")
        line = [w for w in words if w[1] <= tt - t0 + 0.05]
        if line:
            first2 = next((i for i, w in enumerate(words) if w[0] == "It's"), len(words))
            shown = words[first2:] if len(line) > first2 else words[:first2]
            txt = " ".join(w[0] for w in shown).upper()
            T(img, txt, W / 2, 1250, 84, ink, maxw=900, key=txt)
        p.stdin.write(img.convert("RGB").tobytes())
    p.stdin.close()
    p.wait()
    master(silent, tmp, out, total)
    os.remove(silent)
    os.remove(tmp)
    print(json.dumps({"out": out, "seconds": round(total, 1), "order": [v["name"] for v, *_ in parts]}))


if __name__ == "__main__":
    main(sys.argv[1])

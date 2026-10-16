"""Master ElevenLabs (or any) music files into loop-ready, voice-friendly beds.

Usage: python3 tools/music_master.py OUTDIR FILE.mp3 [FILE.mp3 ...]

Beds (names not starting with "st-"):
1. Loop point search: the generated file ends with its own outro, so we cut
   earlier. Among cut points 1.5-6 s before the end of the active audio we pick
   the one whose next 2 s of rhythm (onset envelope) best matches the first 2 s.
   The 60 ms after the cut is blended into the head (equal-power), so the file
   loops with no click and the groove keeps its place.
2. Same gentle master as tools/music_post.py: HP 40 Hz, -3.5 dB @ 2.8 kHz
   (voice room), -2 dB @ 5.5 kHz, low-pass 9.5 kHz, 2:1 glue,
   two-pass loudnorm -14 LUFS / -1.5 dBTP.
Stingers: trailing silence trimmed, 0.3 s fade, EQ, gain to -15 LUFS + limiter.
Also writes OUTDIR/preview/<name> with a 1.2 s fade-out for listening.
"""
import json
import os
import subprocess
import sys

import numpy as np

SR = 44100
EQ = ("highpass=f=40,equalizer=f=2800:t=q:w=1.0:g=-3.5,equalizer=f=5500:t=q:w=1.0:g=-2,"
      "lowpass=f=9500,lowpass=f=9500,acompressor=threshold=-20dB:ratio=2:attack=20:release=250:makeup=1")


def decode(p):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, "<f4").reshape(-1, 2).copy()


def env(x, hop=512):
    m = x.mean(1)
    fr = np.lib.stride_tricks.sliding_window_view(m, 2048)[::hop]
    mag = np.log1p(np.abs(np.fft.rfft(fr * np.hanning(2048), axis=1)))
    return np.r_[0, np.maximum(0, np.diff(mag, axis=0)).sum(1)]


def active_end(x, floor_db=-40):
    m = np.abs(x).max(1)
    w = int(0.05 * SR)
    r = np.sqrt(np.convolve(m ** 2, np.ones(w) / w, "same"))
    thr = r.max() * 10 ** (floor_db / 20)
    idx = np.where(r > thr)[0]
    return idx[-1] if len(idx) else len(x)


def loop_cut(x):
    hop = 512
    e = env(x, hop)
    K = int(2.0 * SR / hop)
    head = e[:K] - e[:K].mean()
    end = active_end(x, -24)          # before the outro fade
    lo, hi = int((end - 6 * SR) / hop), int((end - 1.5 * SR) / hop)
    best, bi = -9, hi
    for i in range(max(K, lo), max(K + 1, hi)):
        seg = e[i:i + K]
        if len(seg) < K:
            break
        seg = seg - seg.mean()
        c = float(seg @ head / (np.linalg.norm(seg) * np.linalg.norm(head) + 1e-9))
        if c > best:
            best, bi = c, i
    L = bi * hop
    f = int(0.06 * SR)
    out = x[:L].copy()
    t = np.linspace(0, np.pi / 2, f)[:, None]
    out[:f] = x[:f] * np.sin(t) + x[L:L + f] * np.cos(t)
    return out, best


def write(p, a):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", p],
                   input=a.astype("<f4").tobytes(), check=True)


def master(src, dst, target, fade_out=0.0, dur=None):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", src, "-af",
                        f"{EQ},loudnorm=I={target}:TP=-1.5:LRA=9:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = json.loads(p.stderr[p.stderr.rindex("{"):p.stderr.rindex("}") + 1])
    ln = (f"loudnorm=I={target}:TP=-1.5:LRA=9:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    af = f"{EQ},{ln}"
    if fade_out and dur:
        af += f",afade=t=out:st={dur - fade_out:.3f}:d={fade_out}"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-af", af, "-ar", str(SR),
                    "-c:a", "libmp3lame", "-b:a", "192k", dst], check=True)


def gain_to(src, dst, target):
    """Short stingers: loudnorm is unreliable under ~3 s, so EQ, measure, then plain gain + limiter."""
    eq = f"/tmp/_eq_{os.path.basename(dst)}.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-af", EQ, eq], check=True)
    err = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", eq, "-af", "ebur128", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    i = float(err[err.rfind("Summary:"):].split("I:")[1].split("LUFS")[0])
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", eq, "-af", f"volume={target - i:.2f}dB,alimiter=limit=0.84:level=false",
                    "-ar", str(SR), "-c:a", "libmp3lame", "-b:a", "192k", dst], check=True)
    os.remove(eq)


def main(out, files):
    os.makedirs(f"{out}/preview", exist_ok=True)
    report = []
    for f in files:
        name = os.path.basename(f)
        x = decode(f)
        tmp = f"/tmp/_master_{name}.wav"
        if name.startswith("st-"):
            end = min(len(x), active_end(x, -50) + int(0.1 * SR))
            y = x[:end].copy()
            fl = int(0.3 * SR)
            y[-fl:] *= np.linspace(1, 0, fl)[:, None]
            write(tmp, y)
            gain_to(tmp, f"{out}/{name}", -15)
            gain_to(tmp, f"{out}/preview/{name}", -15)
            score = None
        else:
            y, score = loop_cut(x)
            write(tmp, y)
            master(tmp, f"{out}/{name}", -14)
            # listening preview: the whole generated track with its own ending, mastered the same way
            full = x[:min(len(x), active_end(x, -50) + int(0.2 * SR))]
            write(tmp, full)
            master(tmp, f"{out}/preview/{name}", -14, fade_out=0.6, dur=len(full) / SR)
        os.remove(tmp)
        report.append({"file": name, "seconds": round(len(y) / SR, 2), "loop_match": None if score is None else round(score, 2)})
        print(name, report[-1])
    json.dump(report, open(f"{out}/master-report.json", "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])

"""Signal-analysis QA for music beds (we can't listen, so we measure).

Usage: python3 tools/music_check.py FILE_OR_DIR [...] [--kind bed|stinger|mix] [--json out.json]

--kind mix is for a finished, voiced video (short-form pilots): loudness -14, true peak, clipping and harsh
highs only. The bed-only rules (voice gap, hook, loop seam) don't apply once a voice sits on the bed.

Per file:
- loudness  integrated LUFS (target -14 +/- 1; stingers -15) and true peak (<= -1.0 dBTP)
- clipping  samples at |x| >= 0.999 (must be 0)
- harsh     share of energy above 8 kHz (< 0.5 %) and 4-8 kHz (< 4 %): no screech
- voice gap energy 1.5-4 kHz vs 200-1500 Hz (dB; below -8 dB leaves room for a voice)
- hook      RMS of the first second vs the whole file (>= -6 dB: no empty intro)
- seam      beds: spectral jolt at the loop join vs the track's own strong beats (<= 1.0) -> no click
- tempo     onset-autocorrelation BPM; key: Krumhansl chroma estimate
"""
import json
import os
import re
import subprocess
import sys

import numpy as np

SR = 22050
MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
NAMES = "C C# D D# E F F# G G# A A# B".split()


def decode(path, sr=SR, ch=1):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", str(ch), "-ar", str(sr), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, "<f4")


def ebur(path):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    summ = err[err.rfind("Summary:"):]
    i = float(re.search(r"I:\s+(-?[\d.]+) LUFS", summ).group(1))
    tp = float(re.search(r"Peak:\s+(-?[\d.inf]+) dBFS", summ).group(1))
    return i, tp


def band_share(x, sr, lo, hi):
    spec = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    f = np.fft.rfftfreq(len(x), 1 / sr)
    tot = spec[f > 20].sum() + 1e-12
    return spec[(f >= lo) & (f < hi)].sum() / tot


def tempo(x, sr):
    hop = 256
    frames = np.lib.stride_tricks.sliding_window_view(x, 1024)[::hop]
    mag = np.abs(np.fft.rfft(frames * np.hanning(1024), axis=1))
    flux = np.maximum(0, np.diff(np.log1p(mag), axis=0)).sum(1)
    flux -= flux.mean()
    ac = np.correlate(flux, flux, "full")[len(flux) - 1:]
    fps = sr / hop
    lags = np.arange(len(ac))
    ok = (lags >= fps * 60 / 150) & (lags <= fps * 60 / 70)
    if not ok.any():  # clip shorter than one slow beat (short SFX): no tempo
        return 0.0
    lag = lags[ok][np.argmax(ac[ok])]
    return 60 * fps / lag


def key_est(x, sr):
    n = 8192
    if len(x) < n:  # very short SFX
        x = np.pad(x, (0, n - len(x)))
    frames = np.lib.stride_tricks.sliding_window_view(x, n)[::n // 2]
    mag = np.abs(np.fft.rfft(frames * np.hanning(n), axis=1)).mean(0)
    f = np.fft.rfftfreq(n, 1 / sr)
    sel = (f > 60) & (f < 2000)
    pc = np.round(12 * np.log2(f[sel] / 440)).astype(int) % 12
    chroma = np.bincount((pc + 9) % 12, weights=mag[sel], minlength=12)
    best = max(((np.corrcoef(np.roll(prof, r), chroma)[0, 1], f"{NAMES[r]} {name}")
                for prof, name in ((MAJ, "major"), (MIN, "minor")) for r in range(12)))
    return best[1]


def check(path, kind="bed"):
    x = decode(path)
    xs = decode(path, 44100, 2)
    i, tp = ebur(path)
    dur = len(x) / SR
    rms = lambda a: float(20 * np.log10(np.sqrt(np.mean(a ** 2)) + 1e-9))
    r = {
        "file": os.path.basename(path), "seconds": round(dur, 2), "lufs": i, "true_peak": tp,
        "clipped": int((np.abs(xs) >= 0.999).sum()),
        "hf_8k_pct": round(100 * band_share(x, SR, 8000, 11025), 3),
        "hf_4_8k_pct": round(100 * band_share(x, SR, 4000, 8000), 2),
        "voice_gap_db": round(10 * np.log10(band_share(x, SR, 1500, 4000) / band_share(x, SR, 200, 1500)), 1),
        "hook_db": round(rms(x[:SR]) - rms(x), 1),
        "bpm_est": round(float(tempo(x, SR)), 1), "key_est": key_est(x, SR),
    }
    if kind == "bed":
        # Loop join click test: a click is a sample-level jump, so look at the first difference
        # (a crude high-pass) of end->start. Energy in the 6 ms around the join vs the 99th
        # percentile of 6 ms windows across the track. <= 1.0 = no worse than the music itself.
        y = np.r_[xs.reshape(-1, 2).mean(1)[-4410:], xs.reshape(-1, 2).mean(1)[:4410]]
        d = np.diff(xs.reshape(-1, 2).mean(1)) ** 2
        w = 265
        win = np.convolve(d, np.ones(w), "valid")[::w]
        dj = np.convolve(np.diff(y) ** 2, np.ones(w), "valid")
        r["seam_ratio"] = round(float(dj[4410 - w:4410 + 1].max() / (np.percentile(win, 99) + 1e-12)), 2)
    target = -15 if kind == "stinger" else -14
    fails = []
    if abs(i - target) > 1.0: fails.append("loudness")
    if tp > -1.0: fails.append("true-peak")
    if r["clipped"]: fails.append("clipping")
    if r["hf_8k_pct"] > 0.5 or r["hf_4_8k_pct"] > 4: fails.append("harsh-highs")
    if kind == "bed" and r["voice_gap_db"] > -8: fails.append("voice-gap")  # stingers sit in pauses
    if kind == "bed" and r["hook_db"] < -6: fails.append("slow-start")
    if kind == "bed" and r["seam_ratio"] > 1.0: fails.append("loop-click")
    r["pass"] = not fails
    r["fails"] = fails
    return r


def main(args):
    out = None
    force = None
    if "--kind" in args:
        force = args[args.index("--kind") + 1]
        args = args[:args.index("--kind")] + args[args.index("--kind") + 2:]
    if "--json" in args:
        out = args[args.index("--json") + 1]
        args = args[:args.index("--json")]
    files = []
    for a in args:
        files += sorted(os.path.join(a, f) for f in os.listdir(a) if f.endswith(".mp3")) if os.path.isdir(a) else [a]
    res = []
    for f in files:
        kind = force or ("stinger" if os.path.basename(f).startswith("st-") else "bed")
        r = check(f, kind)
        res.append(r)
        print(f"{'PASS' if r['pass'] else 'FAIL'} {r['file']:34s} {r['seconds']:5.1f}s {r['lufs']:6.1f} LUFS tp {r['true_peak']:5.1f} "
              f"clip {r['clipped']} >8k {r['hf_8k_pct']:.2f}% 4-8k {r['hf_4_8k_pct']:.1f}% gap {r['voice_gap_db']} "
              f"hook {r['hook_db']} seam {r.get('seam_ratio', '-')} ~{r['bpm_est']}bpm {r['key_est']} {' '.join(r['fails'])}")
    if out:
        json.dump(res, open(out, "w"), indent=1)
    return 0 if all(r["pass"] for r in res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

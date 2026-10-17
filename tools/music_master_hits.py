"""Master "impact" tracks (hook -> build -> drop) and transition SFX, and log where each drop really lands.

Usage: python3 tools/music_master_hits.py SPEC.json OUTDIR [--library tools/music-library.json] [--engineer name,name]

Unlike tools/music_master.py (loop beds), these keep the whole arrangement so the drop stays at its time.
Tracks: HP 40 Hz, an adaptive voice dip (a wide cut around 2.5 kHz deepened until music_check's voice gap
is <= -8 dB, max -9 dB), -2 dB @ 5.5 kHz, low-pass 9.5 kHz, 2:1 glue, two-pass loudnorm -14 LUFS / -1.5 dBTP,
0.5 s fade at the very end.  SFX: same tone shaping, trimmed, gain to -15 LUFS with a limiter.

Measured per track and written to the library JSON: bpm (onset autocorrelation), drop_s (the biggest
low-end energy jump between 3.5 and 10 s, snapped to the nearest strong onset), beat grid anchored on the drop.
"""
import json
import os
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import music_check as mc  # noqa: E402

SR = 44100


def eq(dip, soft=0):
    hi = "highshelf=f=6000:g=-5,lowpass=f=8000,lowpass=f=8000" if soft else "lowpass=f=9500,lowpass=f=9500"
    return (f"highpass=f=40,equalizer=f=2500:t=q:w=0.8:g={dip:.1f},equalizer=f=5500:t=q:w=1.0:g=-2,"
            f"{hi},acompressor=threshold=-20dB:ratio=2:attack=20:release=250:makeup=1")


def lead_trim(src):
    """Seconds of near-silence before the music starts (the hook must be in the first 0.5 s)."""
    x = mc.decode(src, 22050, 1)
    r = np.sqrt(np.convolve(x ** 2, np.ones(220) / 220, "same"))
    idx = np.where(r > r.max() * 10 ** (-30 / 20))[0]
    return max(0.0, idx[0] / 22050 - 0.01) if len(idx) else 0.0


def downbeat_near(src, t0, bpm):
    """Strongest onset within half a beat of t0 (so a built drop lands on the groove)."""
    x = mc.decode(src, 22050, 1)
    hop = 256
    fr = np.lib.stride_tricks.sliding_window_view(x, 1024)[::hop]
    mag = np.log1p(np.abs(np.fft.rfft(fr * np.hanning(1024), axis=1)))
    f = np.fft.rfftfreq(1024, 1 / 22050)
    flux = np.r_[0, np.maximum(0, np.diff(mag[:, f < 200], axis=0)).sum(1)]
    fps = 22050 / hop
    half = 30 / bpm
    a, b = int((t0 - half) * fps), int((t0 + half) * fps)
    return (a + int(np.argmax(flux[a:b]))) / fps


def engineer_drop(src, dst, at, bpm, sfxdir):
    """Build a drop on a flat arrangement: one beat filtered + ducked, a riser into it, a bass-drop hit on it."""
    d = downbeat_near(src, at, bpm)
    a = d - 60 / bpm
    riser, boom = f"{sfxdir}/sfx-x-riser.mp3", f"{sfxdir}/sfx-x-bass-drop.mp3"
    rl = len(mc.decode(riser, 22050, 1)) / 22050
    fc = (f"[0:a]lowpass=f=450:enable='between(t,{a:.3f},{d:.3f})',volume=0.45:enable='between(t,{a:.3f},{d:.3f})'[m];"
          f"[1:a]adelay={int((d - rl) * 1000)}|{int((d - rl) * 1000)},volume=0.5[r];"
          f"[2:a]adelay={int(d * 1000)}|{int(d * 1000)},volume=0.9[b];"
          "[m][r][b]amix=inputs=3:normalize=0:duration=first")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-i", riser, "-i", boom, "-filter_complex", fc,
                    "-ar", str(SR), "-c:a", "pcm_s16le", dst], check=True)
    return d


def master_track(src, dst, dip, dur, soft=0):
    chain = eq(dip, soft)
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", src, "-af",
                        f"{chain},loudnorm=I=-14:TP=-1.5:LRA=9:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = json.loads(p.stderr[p.stderr.rindex("{"):p.stderr.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=9:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    af = f"{chain},{ln},afade=t=out:st={dur - 0.5:.3f}:d=0.5,alimiter=limit=0.84:level=false"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-af", af, "-ar", str(SR),
                    "-c:a", "libmp3lame", "-b:a", "192k", dst], check=True)


def sfx(src, dst, soft=0):
    x = mc.decode(src, SR, 1)
    r = np.sqrt(np.convolve(x ** 2, np.ones(441) / 441, "same"))
    idx = np.where(r > r.max() * 10 ** (-50 / 20))[0]
    end = (idx[-1] + int(0.08 * SR)) / SR if len(idx) else len(x) / SR
    tmp = dst + ".wav"
    tone = ("highshelf=f=3500:g=-8,lowpass=f=6500,lowpass=f=6500" if soft else
            "equalizer=f=5500:t=q:w=1.0:g=-3,lowpass=f=8500,lowpass=f=8500")
    # ebur128 needs >= 0.4 s to measure: pad very short hits with silence
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-af",
                    f"atrim=0:{end:.3f},afade=t=out:st={max(0, end - 0.08):.3f}:d=0.08,highpass=f=35,{tone},"
                    f"apad=whole_dur={max(end, 0.6):.3f}", tmp], check=True)
    i, _ = mc.ebur(tmp)
    for _ in range(3):
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", tmp, "-af",
                        f"volume={-15 - i:.2f}dB,alimiter=limit=0.84:attack=1:release=30:level=false",
                        "-ar", str(SR), "-c:a", "libmp3lame", "-b:a", "192k", dst], check=True)
        got, _ = mc.ebur(dst)
        if abs(got + 15) <= 0.6:
            break
        i += got + 15  # the limiter ate some level: push the gain by the miss
    os.remove(tmp)


def analyse(path, plan_drop=6.0):
    x = mc.decode(path, 22050, 1)
    sr = 22050
    bpm = float(mc.tempo(x, sr))
    hop = 512
    fr = np.lib.stride_tricks.sliding_window_view(x, 2048)[::hop]
    spec = np.abs(np.fft.rfft(fr * np.hanning(2048), axis=1)) ** 2
    f = np.fft.rfftfreq(2048, 1 / sr)
    low = 10 * np.log10(spec[:, (f > 35) & (f < 250)].sum(1) + 1e-9)
    full = 10 * np.log10(spec.sum(1) + 1e-9)
    flux = np.r_[0, np.maximum(0, np.diff(np.log1p(np.sqrt(spec)), axis=0)).sum(1)]
    fps = sr / hop
    w = int(0.8 * fps)
    best, bt = -99, plan_drop
    for i in range(int(3.5 * fps), int(10 * fps)):
        jump = (low[i:i + w].mean() - low[i - w:i].mean()) + 0.5 * (full[i:i + w].mean() - full[i - w:i].mean())
        if jump > best:
            best, bt = jump, i / fps
    # snap to the strongest onset within +/- 0.15 s
    a, b = int((bt - 0.15) * fps), int((bt + 0.15) * fps)
    k = a + int(np.argmax(flux[a:b]))
    drop = k / fps
    return dict(bpm=round(bpm, 1), drop_s=round(drop, 3), drop_jump_db=round(float(best), 1))


def main(spec_path, out, lib_path="tools/music-library.json", engineer=(), at=8.0):
    os.makedirs(out, exist_ok=True)
    os.makedirs(f"{out}/sfx", exist_ok=True)
    spec = json.load(open(spec_path))
    spec = [i for i in spec if i.get("type") == "sfx"] + [i for i in spec if i.get("type") != "sfx"]
    lib = json.load(open(lib_path)) if os.path.exists(lib_path) else {"_note": "", "tracks": {}, "sfx": {}}
    lib["_note"] = ("Impact tracks (hook in the first 0.5 s, build, drop) and transition SFX. drop_s is MEASURED in the mastered "
                    "file; beats = drop_s + k * 60/bpm. Masters: media/music/library/v4/. Made by tools/music_master_hits.py.")
    for item in spec:
        name = item["name"]
        src = f"media/music/library/{name}.mp3"
        if item.get("type") == "sfx":
            dst = f"{out}/sfx/{name}.mp3"
            sfx(src, dst)
            r = mc.check(dst, "stinger")
            if "harsh-highs" in r["fails"]:
                sfx(src, dst, soft=1)
                r = mc.check(dst, "stinger")
            lib["sfx"][name] = dict(file=dst, seconds=r["seconds"], lufs=r["lufs"], pass_=r["pass"], fails=r["fails"])
            print(name, r["pass"], r["fails"], r["seconds"])
            continue
        dst = f"{out}/{name}.mp3"
        lead = lead_trim(src)
        work = f"{out}/_{name}.wav"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{lead:.3f}", "-i", src, "-ar", str(SR), work], check=True)
        built = None
        if name in engineer:
            built = engineer_drop(work, work + ".b.wav", at, item.get("bpm", 110), f"{out}/sfx")
            os.replace(work + ".b.wav", work)
        dur = len(mc.decode(work, 22050, 1)) / 22050
        dip, soft, r = -3.5, 0, None
        while True:
            master_track(work, dst, dip, dur, soft)
            r = mc.check(dst, "bed")
            if "harsh-highs" in r["fails"] and not soft:
                soft = 1
                continue
            if r["voice_gap_db"] <= -8 or dip <= -12:
                break
            dip -= 1.5
        os.remove(work)
        a = analyse(dst, built or item.get("drop_s", 6.0))
        if built:  # we placed the hit ourselves: trust the placement (snapped to the onset analyse finds)
            a["drop_s"] = round(built, 3)
        lib["tracks"][name] = dict(file=dst, page=name[:2], seconds=r["seconds"], bpm=a["bpm"], planned_bpm=item.get("bpm"),
                                   drop_s=a["drop_s"], planned_drop_s=item.get("drop_s"), drop_jump_db=a["drop_jump_db"],
                                   lufs=r["lufs"], true_peak=r["true_peak"], voice_gap_db=r["voice_gap_db"], hook_db=r["hook_db"],
                                   voice_dip_db=dip, soft_highs=bool(soft), lead_trim_s=round(lead, 3),
                                   drop_built=bool(built), pass_=r["pass"], fails=r["fails"])
        print(name, a, dip, r["pass"], r["fails"])
    json.dump(lib, open(lib_path, "w"), indent=1)


if __name__ == "__main__":
    args = sys.argv[1:]
    lib = "tools/music-library.json"
    eng = []
    for flag in ("--library", "--engineer"):
        if flag in args:
            v = args[args.index(flag) + 1]
            args = args[:args.index(flag)] + args[args.index(flag) + 2:]
            if flag == "--library":
                lib = v
            else:
                eng = v.split(",")
    main(args[0], args[1], lib, engineer=eng)

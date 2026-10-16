"""Master rendered beds/stingers into the Steadfold music library.

Usage: python3 tools/music_post.py RAWDIR OUTDIR
RAWDIR holds <code>.wav (FluidSynth renders, 44.1 kHz stereo, rendered with
extra tail) and meta.json from tools/music_v2.py.

For each bed:
1. Loop edit: keep exactly loop_seconds; the tail after the loop point
   (reverb and ringing notes) is folded back onto the start, so the file
   loops with no gap or click.
2. Gentle master: high-pass 40 Hz, -3.5 dB around 2.8 kHz (room for a voice),
   -2 dB at 5.5 kHz, steep low-pass at 9 kHz (no harsh highs), light 2:1 glue.
3. Two-pass loudness normalisation to -14 LUFS, true peak <= -1.5 dBTP.
Stingers keep their natural tail (0.4 s fade) and are normalised to -15 LUFS.

Output: OUTDIR/<code>-<slug>.mp3 (192 kbps) + OUTDIR/library.json
"""
import json
import os
import subprocess
import sys
import wave

import numpy as np

SR = 44100
EQ = ("highpass=f=40,equalizer=f=2800:t=q:w=1.0:g=-3.5,equalizer=f=5500:t=q:w=1.0:g=-2,"
      "lowpass=f=9000,lowpass=f=9000,acompressor=threshold=-20dB:ratio=2:attack=20:release=250:makeup=1")


def read_wav(path):
    with wave.open(path) as w:
        n, ch, sw = w.getnframes(), w.getnchannels(), w.getsampwidth()
        raw = w.readframes(n)
    if sw == 2:
        a = np.frombuffer(raw, "<i2").astype(np.float32) / 32768
    elif sw == 4:
        a = np.frombuffer(raw, "<i4").astype(np.float32) / 2**31
    else:
        raise SystemExit(f"unsupported sample width {sw}")
    return a.reshape(-1, ch)


def write_wav(path, a):
    a = np.clip(a, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(a.shape[1])
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((a * 32767).astype("<i2").tobytes())


def loop_edit(a, seconds):
    L = int(round(seconds * SR))
    if len(a) < L:
        a = np.vstack([a, np.zeros((L - len(a), a.shape[1]), np.float32)])
    body = a[:L].copy()
    tail = a[L:L + 4 * SR]
    body[:len(tail)] += tail
    return body


def loudnorm(src, dst, target, extra=""):
    chain = EQ + (("," + extra) if extra else "")
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", src, "-af",
                        f"{chain},loudnorm=I={target}:TP=-1.5:LRA=9:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    js = p.stderr[p.stderr.rindex("{"):p.stderr.rindex("}") + 1]
    m = json.loads(js)
    ln = (f"loudnorm=I={target}:TP=-1.5:LRA=9:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af", f"{chain},{ln}",
                    "-ar", str(SR), "-c:a", "libmp3lame", "-b:a", "192k", dst], check=True)


def main(raw, out):
    os.makedirs(out, exist_ok=True)
    meta = json.load(open(f"{raw}/meta.json"))
    lib = []
    for m in meta:
        code = m["code"].lower()
        a = read_wav(f"{raw}/{code}.wav")
        tmp = f"{raw}/{code}.edit.wav"
        name = f"{code}-{m['slug']}.mp3"
        if m["kind"] == "bed":
            write_wav(tmp, loop_edit(a, m["loop_seconds"]))
            loudnorm(tmp, f"{out}/{name}", -14)
        else:
            L = int((m["loop_seconds"] + 1.2) * SR)
            b = a[:L].copy()
            fade = np.linspace(1, 0, int(0.4 * SR))[:, None]
            b[-len(fade):] *= fade
            write_wav(tmp, b)
            loudnorm(tmp, f"{out}/{name}", -15)
        lib.append(m | {"file": name})
        print("mastered", name)
    json.dump(lib, open(f"{out}/library.json", "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

"""Write pleasant real-instrument MIDI beds (rendered by FluidSynth in CI).

Usage: python3 tools/instrument_beds.py OUTDIR
Writes OUTDIR/<name>.mid and OUTDIR/<name>.secs for each track.
Moods follow the brand music brief: curious, warm, never harsh.
"""
import os
import sys

import mido

TPB = 480


def note_events(track, ch, notes):
    """notes: list of (start_beat, dur_beats, pitch, vel). Adds sorted events."""
    ev = []
    for s, d, p, v in notes:
        ev.append((int(s * TPB), 1, mido.Message("note_on", channel=ch, note=p, velocity=v)))
        ev.append((int((s + d) * TPB), 0, mido.Message("note_off", channel=ch, note=p, velocity=0)))
    ev.sort(key=lambda e: (e[0], e[1]))
    t = 0
    for at, _, m in ev:
        m.time = at - t
        t = at
        track.append(m)


def song(path, bpm, parts, seconds):
    mid = mido.MidiFile(ticks_per_beat=TPB)
    meta = mido.MidiTrack()
    meta.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(bpm)))
    mid.tracks.append(meta)
    for ch, program, vol, rev, notes in parts:
        tr = mido.MidiTrack()
        if ch != 9:
            tr.append(mido.Message("program_change", channel=ch, program=program))
        tr.append(mido.Message("control_change", channel=ch, control=7, value=vol))
        tr.append(mido.Message("control_change", channel=ch, control=91, value=rev))
        note_events(tr, ch, notes)
        mid.tracks.append(tr)
    mid.save(path + ".mid")
    open(path + ".secs", "w").write(str(seconds))


# I - V - vi - IV in C major (and friends), as (root, chord tones)
PROG_C = [(48, [60, 64, 67]), (43, [59, 62, 67]), (45, [57, 60, 64]), (41, [57, 60, 65])]
PROG_F = [(41, [57, 60, 65]), (48, [55, 60, 64]), (50, [57, 62, 65]), (46, [58, 62, 65])]
PROG_G = [(43, [59, 62, 67]), (40, [59, 64, 67]), (48, [60, 64, 67]), (50, [57, 62, 66])]


def bars_for(seconds, bpm):
    return int(seconds * bpm / 60 / 4) + 1


def arps(prog, bars, octave=0, vel=58, pattern=(0, 1, 2, 1, 0, 1, 2, 1), step=0.5):
    out = []
    for b in range(bars):
        _, tones = prog[b % len(prog)]
        for i, k in enumerate(pattern):
            out.append((b * 4 + i * step, step * 1.6, tones[k] + octave, vel - (i % 2) * 8))
    return out


def bassline(prog, bars, vel=70, rhythm=((0, 1.5), (1.5, 0.5), (2, 2))):
    out = []
    for b in range(bars):
        root, _ = prog[b % len(prog)]
        for s, d in rhythm:
            out.append((b * 4 + s, d * 0.95, root - 12 if root > 40 else root, vel))
    return out


def chords(prog, bars, vel=52, octave=0, hits=((0, 3.9),)):
    out = []
    for b in range(bars):
        _, tones = prog[b % len(prog)]
        for s, d in hits:
            for p in tones:
                out.append((b * 4 + s, d, p + octave, vel))
    return out


def melody(prog, bars, motif, vel=64, octave=12):
    """motif: list of (beat, dur, chord_index) repeated each bar, last bar lifts."""
    out = []
    for b in range(bars):
        _, tones = prog[b % len(prog)]
        for s, d, k in motif:
            out.append((b * 4 + s, d, tones[k % 3] + octave + (12 if k >= 3 else 0), vel))
    return out


def drums(bars, kick=36, snare=None, hat=42, vel=(70, 55, 30), claps=False, start_bar=0):
    out = []
    for b in range(start_bar, bars):
        o = b * 4
        out += [(o, 0.3, kick, vel[0]), (o + 2.5, 0.3, kick, vel[0] - 10)]
        if snare:
            out += [(o + 1, 0.3, snare, vel[1]), (o + 3, 0.3, snare, vel[1])]
        if claps:
            out += [(o + 1, 0.3, 39, vel[1] - 10), (o + 3, 0.3, 39, vel[1] - 10)]
        out += [(o + i * 0.5, 0.2, hat, vel[2] + (6 if i % 2 == 0 else 0)) for i in range(8)]
    return out


def main(outdir):
    os.makedirs(outdir, exist_ok=True)

    # Littlefold: cosy nylon guitar + felt piano + glockenspiel, 92 bpm
    s, bpm = 18, 92
    n = bars_for(s, bpm)
    song(f"{outdir}/lf-cosy-inst-01", bpm, [
        (0, 24, 92, 50, arps(PROG_F, n, vel=60)),
        (1, 0, 78, 60, melody(PROG_F, n, [(0, 1.5, 2), (1.5, 0.5, 1), (2, 2, 0)], vel=54)),
        (2, 9, 46, 70, melody(PROG_F, n, [(0, 0.5, 2), (3, 0.5, 1)], vel=40, octave=24)),
        (3, 32, 80, 30, bassline(PROG_F, n, vel=62, rhythm=((0, 2), (2, 2)))),
    ], s)

    # Fully Funded: curious lo-fi, Rhodes + bass + soft drums, 95 bpm
    s, bpm = 18, 95
    n = bars_for(s, bpm)
    song(f"{outdir}/ff-curious-inst-01", bpm, [
        (0, 4, 88, 55, chords(PROG_C, n, vel=50, hits=((0, 1.4), (1.5, 0.4), (2.5, 1.4)))),
        (1, 33, 92, 20, bassline(PROG_C, n, vel=72)),
        (2, 11, 60, 60, melody(PROG_C, n, [(0.5, 0.5, 0), (1, 0.5, 1), (1.5, 1, 2), (3, 0.5, 1)], vel=46)),
        (9, 0, 70, 25, drums(n, snare=37, vel=(72, 50, 28))),
    ], s)

    # Locked Hour: focused, muted guitar 8ths + pad that rises, 100 bpm
    s, bpm = 16, 100
    n = bars_for(s, bpm)
    pad = [(b * 4, 3.95, p + (12 if b >= n // 2 else 0), 34 + min(b, 8) * 3)
           for b in range(n) for p in PROG_G[b % 4][1]]
    song(f"{outdir}/lh-focus-inst-01", bpm, [
        (0, 28, 84, 30, arps(PROG_G, n, vel=62, pattern=(0, 0, 1, 0, 2, 0, 1, 0))),
        (1, 89, 70, 80, pad),
        (2, 38, 90, 20, bassline(PROG_G, n, vel=70, rhythm=((0, 0.5), (0.5, 0.5), (1, 1), (2, 0.5), (2.5, 0.5), (3, 1)))),
        (9, 0, 70, 20, drums(n, snare=None, claps=True, vel=(74, 56, 26), start_bar=1)),
    ], s)

    # Hourback: playful marimba + ukulele-ish nylon + claps, 108 bpm
    s, bpm = 16, 108
    n = bars_for(s, bpm)
    song(f"{outdir}/hb-playful-inst-01", bpm, [
        (0, 12, 90, 45, melody(PROG_C, n, [(0, 0.5, 0), (0.5, 0.5, 1), (1, 0.5, 2), (2, 0.5, 3), (2.5, 1, 2)], vel=58, octave=12)),
        (1, 24, 80, 40, chords(PROG_C, n, vel=48, hits=((0, 0.4), (1, 0.4), (1.5, 0.4), (2.5, 0.4), (3, 0.4)))),
        (2, 33, 88, 20, bassline(PROG_C, n, vel=70, rhythm=((0, 1), (1.5, 0.5), (2, 1), (3, 1)))),
        (9, 0, 66, 25, drums(n, snare=None, claps=True, vel=(66, 58, 24))),
    ], s)


if __name__ == "__main__":
    main(sys.argv[1])

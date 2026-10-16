"""Steadfold music library v2: curious, warm, never harsh.

Writes MIDI for 14 candidate beds (3-4 per page) and 3 reveal stingers.
Rendered with real-instrument samples (FluidSynth + FluidR3_GM, MIT licence)
by .github/workflows/music-library.yml, then mastered by tools/music_post.py.

Replaces music2.py "warm" (retired Oct 16: Dharma found it unpleasant).

Brief (Dharma, Oct 15 11:39 pm): build curiosity and pull people to keep
watching. A gentle forward pulse, a rising motif, a light "what's next" feel.
Suspense only for reveals (the stingers), never by default.

Every bed:
- starts with its hook on beat 1 (no empty intro),
- is a whole number of bars, ending on a chord that leads back to bar 1,
  so the mastered file loops cleanly,
- climbs in bar 7 and hangs on an open note in bar 8 ("what's next"),
- uses soft velocities, no crash/open hats, and is low-passed in mastering.

Usage: python3 tools/music_v2.py OUTDIR   -> OUTDIR/<code>.mid + OUTDIR/meta.json
Pure Python, no dependencies.
"""
import json
import os
import random
import struct
import sys

TPB = 480
MAJOR = [0, 2, 4, 5, 7, 9, 11]


# ---------------------------------------------------------------- MIDI writer
def vlq(n):
    out = [n & 0x7F]
    n >>= 7
    while n:
        out.append((n & 0x7F) | 0x80)
        n >>= 7
    return bytes(reversed(out))


def track_bytes(events):
    """events: list of (tick, order, bytes). Returns an MTrk chunk."""
    events.sort(key=lambda e: (e[0], e[1]))
    data, t = b"", 0
    for tick, _, msg in events:
        data += vlq(max(0, tick - t)) + msg
        t = max(t, tick)
    data += vlq(0) + b"\xFF\x2F\x00"
    return b"MTrk" + struct.pack(">I", len(data)) + data


def write_midi(path, bpm, parts):
    """parts: list of dicts {ch, program, vol, rev, cho, pan, notes:[(beat,dur,pitch,vel)], expr:[(beat,val)]}"""
    tempo = int(60_000_000 / bpm)
    last = max((int((b + d) * TPB) for p in parts for b, d, _, _ in p["notes"]), default=0)
    pad_ticks = int(4.0 * bpm / 60 * TPB)  # 4 s of silence so the render keeps the reverb tail
    meta = [(0, 0, b"\xFF\x51\x03" + tempo.to_bytes(3, "big")), (last + pad_ticks, 9, b"\xFF\x06\x03end")]
    chunks = [track_bytes(meta)]
    for p in parts:
        ch = p["ch"]
        ev = []
        if ch != 9:
            ev.append((0, 0, bytes([0xC0 | ch, p["program"]])))
        for cc, val in ((7, p.get("vol", 90)), (10, p.get("pan", 64)), (91, p.get("rev", 50)),
                        (93, p.get("cho", 0)), (11, p.get("expr0", 127))):
            ev.append((0, 0, bytes([0xB0 | ch, cc, max(0, min(127, int(val)))])))
        for beat, val in p.get("expr", []):
            ev.append((int(beat * TPB), 1, bytes([0xB0 | ch, 11, max(0, min(127, int(val)))])))
        for beat, dur, pitch, vel in p["notes"]:
            on = int(beat * TPB)
            off = int((beat + dur) * TPB)
            pitch = max(0, min(127, int(pitch)))
            ev.append((on, 3, bytes([0x90 | ch, pitch, max(1, min(127, int(vel)))])))
            ev.append((max(on + 1, off), 2, bytes([0x80 | ch, pitch, 0])))
        chunks.append(track_bytes(ev))
    head = b"MThd" + struct.pack(">IHHH", 6, 1, len(chunks), TPB)
    with open(path, "wb") as f:
        f.write(head + b"".join(chunks))


# ---------------------------------------------------------------- theory
class Key:
    def __init__(self, root):  # root: MIDI note of the tonic around C4 (60)
        self.root = root

    def deg(self, d, octave=0):
        """Scale degree d (0 = tonic, may be negative / >6) -> MIDI pitch."""
        o, i = divmod(d, 7)
        return self.root + 12 * (o + octave) + MAJOR[i]

    def chord(self, degree, kind="triad"):
        """Scale-degree chord tones (as degrees)."""
        tones = [degree, degree + 2, degree + 4]
        if kind == "7":
            tones.append(degree + 6)
        elif kind == "add9":
            tones.append(degree + 8)
        elif kind == "sus4":
            tones = [degree, degree + 3, degree + 4]
        elif kind == "sus2":
            tones = [degree, degree + 1, degree + 4]
        return tones


def voice(key, tones, center=64, spread=3):
    """Place chord tones close to `center` (smooth voice leading)."""
    out = []
    for d in tones[:spread + 1]:
        p = key.deg(d)
        while p < center - 6:
            p += 12
        while p > center + 6:
            p -= 12
        out.append(p)
    return sorted(set(out))


def nearest_chord_tone(key, d, tones):
    pcs = {t % 7 for t in tones}
    for delta in (0, -1, 1, -2, 2, 3, -3):
        if (d + delta) % 7 in pcs:
            return d + delta
    return d


# ---------------------------------------------------------------- parts
def rng_for(code):
    return random.Random(sum(map(ord, code)) * 7919)


def humanize(notes, r, t=0.012, v=5):
    return [(max(0, b + r.uniform(-t, t)) if b > 0 else 0, d, p, vel + r.randint(-v, v)) for b, d, p, vel in notes]


def melody(key, prog, hook, r, bars, octave=1, vel=64, climb=True, hang=4, answer=None):
    """hook: [(beat, dur, degree)] for bar 1. Transposed to each bar's chord.
    Bar 7 climbs (scale run up to the hang note), bar 8 hangs on an open degree."""
    out = []
    for b in range(bars):
        cdeg, kind = prog[b % len(prog)]
        tones = key.chord(cdeg, kind)
        o = b * 4
        if climb and b == bars - 2:
            start = nearest_chord_tone(key, hook[0][2] + cdeg, tones)
            run = [start + i for i in range(7)]
            for i, d in enumerate(run):
                out.append((o + i * 0.5, 0.45, key.deg(d, octave), vel - 6 + i * 2))
            continue
        if b == bars - 1:
            # the "what's next" hang: an unresolved open note over V, leads back to bar 1
            out.append((o, 2.6, key.deg(hang, octave), vel - 2))
            out.append((o + 3, 0.5, key.deg(hang - 1, octave), vel - 14))
            out.append((o + 3.5, 0.5, key.deg(hook[0][2] + 1, octave), vel - 12))
            continue
        cell = answer if (answer and b % 4 == 3) else hook
        shift = 0 if b % 4 in (0, 2) else (cdeg - prog[0][0])
        for i, (s, d, deg) in enumerate(cell):
            dd = deg + shift
            if i == 0 or d >= 1 or s in (0, 2):
                dd = nearest_chord_tone(key, dd, tones)
            out.append((o + s, d * 0.92, key.deg(dd, octave), vel - (0 if s in (0, 2) else 8)))
    return humanize(out, r)


def chords(key, prog, bars, r, rhythm=((0, 3.9),), vel=50, center=62, spread=3, start_bar=0):
    out = []
    for b in range(start_bar, bars):
        cdeg, kind = prog[b % len(prog)]
        ps = voice(key, key.chord(cdeg, kind), center, spread)
        for s, d in rhythm:
            for j, p in enumerate(ps):
                out.append((b * 4 + s + j * 0.008, d, p, vel - j * 2))
    return humanize(out, r, t=0.006, v=3)


def arp(key, prog, bars, r, pattern=(0, 1, 2, 3, 2, 1, 0, 1), step=0.5, vel=56, center=64, start_bar=0, ring=1.6):
    out = []
    for b in range(start_bar, bars):
        cdeg, kind = prog[b % len(prog)]
        ps = voice(key, key.chord(cdeg, kind) + [cdeg + 7], center, 4)
        for i, k in enumerate(pattern):
            if i * step >= 4:
                break
            out.append((b * 4 + i * step, step * ring, ps[k % len(ps)], vel - (i % 2) * 7))
    return humanize(out, r)


def bass(key, prog, bars, r, rhythm=((0, 1.5), (1.5, 0.5), (2, 1.9)), vel=70, start_bar=0, walk=False):
    out = []
    for b in range(start_bar, bars):
        cdeg, _ = prog[b % len(prog)]
        root = key.deg(cdeg, -2)
        if root < 36:
            root += 12
        for k, (s, d) in enumerate(rhythm):
            p = root
            if walk and k == len(rhythm) - 1:
                nxt = key.deg(prog[(b + 1) % len(prog)][0], -2)
                p = root + (2 if nxt > root else -1)
            out.append((b * 4 + s, d * 0.92, p, vel - (k % 2) * 6))
    return humanize(out, r, v=4)


def pad(key, prog, bars, r, vel=40, center=60, start_bar=0, rise=True):
    out = []
    for b in range(start_bar, bars):
        cdeg, kind = prog[b % len(prog)]
        for p in voice(key, key.chord(cdeg, kind), center, 3):
            v = vel + (min(b, 7) * 3 if rise else 0)
            out.append((b * 4, 3.98, p, v))
    return out


def beat(bars, r, style="lofi", vel=60, start_bar=0, swing=0.0, build_from=None):
    """Soft kits only: kick, side-stick/clap, closed or pedal hat, shaker. No crashes, no open hats."""
    out = []
    for b in range(start_bar, bars):
        o = b * 4
        lift = 6 if (build_from is not None and b >= build_from) else 0
        if style == "lofi":
            out += [(o, .3, 36, vel), (o + 2.5, .3, 36, vel - 14), (o + 1, .3, 37, vel - 8), (o + 3, .3, 37, vel - 6)]
            hats = [(i * 0.5 + (swing if i % 2 else 0)) for i in range(8)]
            out += [(o + h, .15, 42, 26 + (6 if i % 2 == 0 else 0) + lift) for i, h in enumerate(hats)]
        elif style == "pulse":  # focus: four-on-the-floor softly, claps on 2 and 4
            out += [(o + i, .3, 36, vel - (0 if i % 2 == 0 else 8)) for i in range(4)]
            out += [(o + 1, .3, 39, vel - 22 + lift), (o + 3, .3, 39, vel - 20 + lift)]
            out += [(o + i * 0.5 + 0.25, .1, 44, 24 + lift) for i in range(8)]
        elif style == "bounce":  # playful
            out += [(o, .3, 36, vel), (o + 1.5, .3, 36, vel - 16), (o + 2, .3, 36, vel - 6)]
            out += [(o + 1, .3, 39, vel - 16), (o + 3, .3, 39, vel - 14)]
            out += [(o + i * 0.5, .1, 82, 30 + lift) for i in range(8)]
        elif style == "brush":  # cosy
            out += [(o, .3, 36, vel - 10), (o + 2, .3, 36, vel - 18)]
            out += [(o + i * 0.5 + (swing if i % 2 else 0), .1, 70, 24 + (5 if i % 2 == 0 else 0)) for i in range(8)]
        elif style == "snap":
            out += [(o, .3, 36, vel - 6), (o + 2.5, .3, 36, vel - 16)]
            out += [(o + 1, .3, 39, vel - 24), (o + 3, .3, 39, vel - 22)]
            out += [(o + 1, .1, 75, 30), (o + 3, .1, 75, 28)]
    return humanize(out, r, t=0.008, v=4)


def P(ch, program, notes, vol=90, rev=50, cho=0, pan=64, expr=None):
    return {"ch": ch, "program": program, "notes": notes, "vol": vol, "rev": rev, "cho": cho, "pan": pan,
            "expr": expr or []}


# GM programs used (FluidR3_GM): 0 piano, 4 EP1, 8 celesta, 9 glock, 10 music box, 11 vibes, 12 marimba,
# 24 nylon gtr, 28 muted gtr, 32 acoustic bass, 33 finger bass, 38 synth bass 1, 45 pizzicato,
# 46 harp, 48 strings, 49 slow strings, 71 clarinet, 73 flute, 89 warm pad
I, II, III, IV, V, VI = 0, 1, 2, 3, 4, 5


def bars_for(bpm, lo=15.5, hi=26):
    for n in (8, 10, 12, 16):
        if lo <= n * 4 * 60 / bpm <= hi:
            return n
    return 8


TRACKS = []


def track(code, page, slug, bpm, key_root, key_name, mood, desc):
    def deco(fn):
        TRACKS.append(dict(code=code, page=page, slug=slug, bpm=bpm, key_root=key_root, key=key_name,
                           mood=mood, desc=desc, fn=fn))
        return fn
    return deco


# ----------------------------------------------------------------- Fully Funded
LOFI = [(I, "7"), (VI - 0, "7"), (II, "7"), (V, "7")]          # Imaj7 vi7 ii7 V7
POP = [(I, "triad"), (V, "triad"), (VI - 0, "triad"), (IV, "triad")]
POP_V = [(I, "add9"), (V, "triad"), (VI - 0, "7"), (IV, "add9"), (I, "add9"), (V, "triad"), (IV, "add9"), (V, "sus4")]


@track("FF-A", "fullyfunded", "curious-lofi", 90, 65, "F major", "curious",
       "Warm Rhodes, vibraphone hook that climbs, lazy soft beat. Thinking-out-loud money talk.")
def ff_a(k, n, r):
    prog = LOFI
    hook = [(0, 0.5, 4), (0.5, 0.5, 5), (1, 1, 7), (2.5, 0.5, 6), (3, 1, 4)]
    return [
        P(0, 4, chords(k, prog, n, r, rhythm=((0, 1.4), (1.75, 0.6), (2.5, 1.4)), vel=50, center=60, spread=3), vol=92, rev=55, cho=30),
        P(1, 11, melody(k, prog, hook, r, n, octave=1, vel=60, hang=8), vol=82, rev=70, pan=74),
        P(2, 33, bass(k, prog, n, r, vel=74, start_bar=1), vol=96, rev=10),
        P(9, 0, beat(n, r, "lofi", vel=58, start_bar=1, swing=0.08), vol=78, rev=20),
    ]


@track("FF-B", "fullyfunded", "bright-pop", 100, 62, "D major", "optimistic",
       "Felt piano and plucked strings over light claps. Optimistic, 'you can do this' energy.")
def ff_b(k, n, r):
    prog = POP_V
    hook = [(0, 0.5, 2), (0.5, 0.5, 4), (1, 0.5, 7), (1.5, 1.5, 6), (3.5, 0.5, 4)]
    return [
        P(0, 0, chords(k, prog, n, r, rhythm=((0, 0.9), (1, 0.4), (1.5, 0.9), (2.5, 0.4), (3, 0.9)), vel=46, center=62), vol=88, rev=50),
        P(1, 45, arp(k, prog, n, r, pattern=(0, 2, 1, 3, 0, 2, 1, 3), vel=58, center=72, start_bar=2, ring=0.6), vol=74, rev=45, pan=44),
        P(3, 0, melody(k, prog, hook, r, n, octave=1, vel=66, hang=8), vol=86, rev=55, pan=80),
        P(2, 33, bass(k, prog, n, r, rhythm=((0, 0.75), (0.75, 0.75), (2, 0.75), (2.75, 0.75), (3.5, 0.4)), vel=70, start_bar=1), vol=94, rev=10),
        P(9, 0, beat(n, r, "bounce", vel=60, start_bar=2), vol=74, rev=20),
    ]


@track("FF-C", "fullyfunded", "confident-build", 96, 67, "G major", "confident",
       "Muted guitar pulse, bass and kick that build bar by bar, warm pad rising underneath.")
def ff_c(k, n, r):
    prog = [(VI, "7"), (IV, "add9"), (I, "add9"), (V, "triad")]
    hook = [(0, 0.5, 5), (0.5, 0.5, 4), (1, 0.5, 2), (1.5, 1, 4), (3, 0.5, 5), (3.5, 0.5, 7)]
    return [
        P(0, 28, arp(k, prog, n, r, pattern=(0, 0, 1, 0, 2, 0, 1, 0), vel=60, center=60, ring=0.5), vol=86, rev=35, pan=50),
        P(1, 89, pad(k, prog, n, r, vel=34, center=60, start_bar=2), vol=76, rev=80),
        P(3, 4, melody(k, prog, hook, r, n, octave=1, vel=62, hang=8), vol=84, rev=60, pan=78, cho=20),
        P(2, 33, bass(k, prog, n, r, rhythm=((0, .5), (.5, .5), (1, 1), (2, .5), (2.5, .5), (3, 1)), vel=70, start_bar=2), vol=94, rev=10),
        P(9, 0, beat(n, r, "pulse", vel=60, start_bar=1, build_from=4), vol=72, rev=20),
    ]


@track("FF-D", "fullyfunded", "question-marimba", 92, 60, "C major", "curious",
       "Marimba and Rhodes ask a little musical question each bar. Good under 'here's the catch' posts.")
def ff_d(k, n, r):
    prog = [(I, "add9"), (III, "7"), (IV, "add9"), (V, "sus4")]
    hook = [(0, 0.5, 0), (0.5, 0.5, 2), (1, 0.5, 4), (1.5, 0.5, 5), (2, 1.5, 4)]
    answer = [(0, 0.5, 5), (0.5, 0.5, 4), (1, 0.5, 2), (1.5, 2, 1)]
    return [
        P(0, 12, melody(k, prog, hook, r, n, octave=1, vel=70, hang=8, answer=answer), vol=86, rev=50, pan=70),
        P(1, 4, chords(k, prog, n, r, rhythm=((0, 1.8), (2, 1.8)), vel=44, center=58), vol=86, rev=55, cho=30),
        P(2, 32, bass(k, prog, n, r, rhythm=((0, 1.4), (1.5, .5), (2, 1.9)), vel=72, start_bar=1), vol=94, rev=10),
        P(9, 0, beat(n, r, "snap", vel=58, start_bar=2), vol=72, rev=25),
    ]


# ----------------------------------------------------------------- Locked Hour
@track("LH-A", "lockedhour", "focus-pulse", 104, 69, "A minor feel (C major)", "focused",
       "Steady muted-guitar eighths and soft four-on-the-floor; a pad lifts in the second half.")
def lh_a(k, n, r):
    prog = [(VI, "triad"), (IV, "add9"), (I, "triad"), (V, "sus4")]
    k = Key(60)
    hook = [(0, 1, 5), (1, 0.5, 4), (1.5, 0.5, 5), (2, 1.5, 7), (3.5, 0.5, 6)]
    return [
        P(0, 28, arp(k, prog, n, r, pattern=(0,) * 8, vel=58, center=57, ring=0.45), vol=86, rev=30, pan=46),
        P(4, 28, arp(k, prog, n, r, pattern=(1, 2, 1, 2, 1, 2, 1, 2), vel=46, center=64, ring=0.45, start_bar=2), vol=74, rev=40, pan=82),
        P(1, 89, pad(k, prog, n, r, vel=30, center=62, start_bar=n // 2), vol=78, rev=80),
        P(3, 4, melody(k, prog, hook, r, n, octave=1, vel=58, hang=7), vol=78, rev=60, pan=64),
        P(2, 38, bass(k, prog, n, r, rhythm=tuple((i * .5, .45) for i in range(8)), vel=62, start_bar=1), vol=80, rev=5),
        P(9, 0, beat(n, r, "pulse", vel=62, start_bar=1, build_from=n // 2), vol=72, rev=15),
    ]


@track("LH-B", "lockedhour", "ticking-marimba", 110, 64, "E minor feel (G major)", "focused",
       "Clock-like marimba ostinato with a warm bass; feels like the timer just started.")
def lh_b(k, n, r):
    k = Key(67)
    prog = [(VI, "triad"), (II, "7"), (IV, "add9"), (V, "triad")]
    hook = [(0, 0.5, 5), (0.5, 0.5, 7), (1, 1, 9), (2, 0.5, 8), (2.5, 0.5, 7), (3, 1, 5)]
    return [
        P(0, 12, arp(k, prog, n, r, pattern=(0, 2, 1, 2, 0, 2, 1, 2), step=0.5, vel=60, center=60, ring=0.7), vol=88, rev=40, pan=52),
        P(1, 73, melody(k, prog, hook, r, n, octave=0, vel=56, hang=6), vol=74, rev=65, pan=76),
        P(2, 33, bass(k, prog, n, r, rhythm=((0, 1), (1.5, .5), (2, 1), (3, .5), (3.5, .5)), vel=72, start_bar=1), vol=94, rev=10),
        P(3, 48, pad(k, prog, n, r, vel=28, center=60, start_bar=4), vol=72, rev=70),
        P(9, 0, beat(n, r, "snap", vel=60, start_bar=2), vol=70, rev=20),
    ]


@track("LH-C", "lockedhour", "morning-drive", 100, 62, "D major", "focused, lifting",
       "Piano ostinato with strings swelling in; a 'you've got this hour' lift.")
def lh_c(k, n, r):
    prog = [(I, "add9"), (V, "triad"), (II, "7"), (IV, "add9")]
    hook = [(0, 0.5, 4), (0.5, 0.5, 2), (1, 0.5, 4), (1.5, 0.5, 5), (2, 2, 4)]
    strings = pad(k, prog, n, r, vel=26, center=62, start_bar=2)
    return [
        P(0, 0, arp(k, prog, n, r, pattern=(0, 1, 2, 1, 3, 1, 2, 1), vel=52, center=62, ring=0.9), vol=88, rev=50, pan=54),
        P(1, 48, strings, vol=80, rev=75, pan=70, expr=[(8 + i, 70 + i * 3) for i in range(0, 4 * (n - 2), 4)]),
        P(3, 46, melody(k, prog, hook, r, n, octave=1, vel=62, hang=8), vol=82, rev=60, pan=80),
        P(2, 32, bass(k, prog, n, r, rhythm=((0, 1.9), (2, 1), (3, .9)), vel=70, start_bar=1), vol=92, rev=10),
        P(9, 0, beat(n, r, "brush", vel=62, start_bar=2), vol=72, rev=20),
    ]


@track("LH-D", "lockedhour", "lock-in-build", 108, 59, "B minor feel (D major)", "focused, building",
       "Harp arpeggios and a rising Rhodes line; light hats join in the second half. Slight build.")
def lh_d(k, n, r):
    k = Key(62)
    prog = [(VI, "7"), (IV, "add9"), (V, "triad"), (III, "7")]
    hook = [(0, 0.5, 5), (0.5, 0.5, 6), (1, 0.5, 7), (1.5, 1.5, 9), (3.5, 0.5, 7)]
    return [
        P(0, 46, arp(k, prog, n, r, pattern=(0, 1, 2, 3, 4, 3, 2, 1), step=0.5, vel=58, center=62, ring=1.2), vol=86, rev=55, pan=48),
        P(1, 4, melody(k, prog, hook, r, n, octave=1, vel=58, hang=8), vol=80, rev=60, pan=78, cho=20),
        P(2, 38, bass(k, prog, n, r, rhythm=((0, .75), (.75, .75), (1.5, .5), (2, .75), (2.75, .75), (3.5, .5)), vel=60, start_bar=2), vol=78, rev=5),
        P(3, 89, pad(k, prog, n, r, vel=28, center=60, start_bar=1), vol=74, rev=80),
        P(9, 0, beat(n, r, "pulse", vel=58, start_bar=n // 2, build_from=n - 2), vol=70, rev=15),
    ]


# ----------------------------------------------------------------- Hourback
@track("HB-A", "hourback", "ta-da-pizzicato", 116, 60, "C major", "playful",
       "Bouncy pizzicato and marimba with claps; a little 'ta-da' lift at the turn.")
def hb_a(k, n, r):
    prog = [(I, "triad"), (IV, "triad"), (V, "triad"), (I, "triad"), (VI, "triad"), (II, "7"), (IV, "triad"), (V, "sus4")]
    hook = [(0, 0.5, 4), (0.5, 0.5, 4), (1, 0.5, 5), (1.5, 0.5, 7), (2.5, 1, 4), (3.5, 0.5, 2)]
    tada = [(4 * (n - 1) + 2 + i * 0.25, 1.6 - i * .25, k.deg(d, 2), 60 + i * 4) for i, d in enumerate((0, 2, 4, 7))]
    return [
        P(0, 45, arp(k, prog, n, r, pattern=(0, 2, 1, 2, 0, 2, 1, 2), vel=60, center=64, ring=0.5), vol=84, rev=40, pan=48),
        P(1, 12, melody(k, prog, hook, r, n, octave=1, vel=68, hang=8), vol=86, rev=45, pan=78),
        P(2, 32, bass(k, prog, n, r, rhythm=((0, .5), (1, .5), (1.5, .5), (2, .5), (3, .5)), vel=72, start_bar=1), vol=94, rev=10),
        P(3, 9, tada, vol=58, rev=70, pan=64),
        P(9, 0, beat(n, r, "bounce", vel=62, start_bar=1), vol=74, rev=20),
    ]


@track("HB-B", "hourback", "sunny-strum", 112, 67, "G major", "playful, light",
       "Nylon-guitar strum, clarinet tune and woodblock; a clever little life-hack feel.")
def hb_b(k, n, r):
    prog = [(I, "triad"), (V, "triad"), (IV, "triad"), (V, "triad")]
    hook = [(0, 0.5, 2), (0.5, 0.5, 4), (1, 1, 5), (2, 0.5, 4), (2.5, 0.5, 2), (3, 1, 0)]
    answer = [(0, 0.5, 4), (0.5, 0.5, 5), (1, 0.5, 7), (1.5, 2.5, 6)]
    strum = chords(k, prog, n, r, rhythm=((0, .45), (1, .45), (1.5, .45), (2.5, .45), (3, .45)), vel=48, center=60)
    return [
        P(0, 24, strum, vol=86, rev=40, pan=44),
        P(1, 71, melody(k, prog, hook, r, n, octave=0, vel=60, hang=8, answer=answer), vol=80, rev=55, pan=80),
        P(2, 32, bass(k, prog, n, r, rhythm=((0, 1), (1.5, .5), (2, 1), (3, 1)), vel=70, start_bar=1, walk=True), vol=92, rev=10),
        P(9, 0, beat(n, r, "snap", vel=58, start_bar=1), vol=74, rev=25),
    ]


@track("HB-C", "hourback", "clever-celesta", 120, 65, "F major", "playful, curious",
       "Celesta and finger-snap groove with a walking bass; sly, smart, 'watch this'.")
def hb_c(k, n, r):
    prog = [(I, "7"), (VI, "7"), (II, "7"), (V, "7")]
    hook = [(0, 0.5, 7), (0.5, 0.5, 6), (1, 0.5, 4), (1.5, 0.5, 5), (2, 0.5, 6), (2.5, 1.5, 4)]
    return [
        P(0, 8, melody(k, prog, hook, r, n, octave=1, vel=64, hang=8), vol=84, rev=55, pan=74),
        P(1, 4, chords(k, prog, n, r, rhythm=((0.5, .4), (1.5, .4), (2.5, .4), (3.5, .4)), vel=44, center=60), vol=84, rev=45, pan=52, cho=25),
        P(2, 32, bass(k, prog, n, r, rhythm=tuple((i, .9) for i in range(4)), vel=70, start_bar=0, walk=True), vol=92, rev=10),
        P(9, 0, beat(n, r, "snap", vel=60, start_bar=1), vol=74, rev=25),
    ]


# ----------------------------------------------------------------- Littlefold
@track("LF-A", "littlefold", "cosy-fingerpick", 88, 65, "F major", "tender, cosy",
       "Fingerpicked nylon guitar, felt piano tune and a glockenspiel sparkle. Warm, never sleepy.")
def lf_a(k, n, r):
    prog = [(I, "add9"), (V, "triad"), (VI, "7"), (IV, "add9")]
    hook = [(0, 0.5, 4), (0.5, 0.5, 5), (1, 1.5, 7), (3, 0.5, 5), (3.5, 0.5, 4)]
    sparkle = [(b * 4 + 3.5, 0.5, k.deg(d, 2), 38) for b in range(1, n, 2) for d in (4,)]
    return [
        P(0, 24, arp(k, prog, n, r, pattern=(0, 2, 1, 3, 0, 2, 1, 3), vel=56, center=60, ring=1.8), vol=88, rev=55, pan=50),
        P(1, 0, melody(k, prog, hook, r, n, octave=1, vel=52, hang=8), vol=82, rev=65, pan=74),
        P(3, 9, sparkle, vol=50, rev=80, pan=64),
        P(2, 32, bass(k, prog, n, r, rhythm=((0, 1.9), (2, 1.9)), vel=62, start_bar=1), vol=88, rev=15),
        P(9, 0, beat(n, r, "brush", vel=54, start_bar=2, swing=0.05), vol=64, rev=30),
    ]


@track("LF-B", "littlefold", "tender-musicbox", 84, 60, "C major", "tender",
       "Music-box tune over soft piano and a gentle string pad. Sweet and calm, still moving forward.")
def lf_b(k, n, r):
    prog = [(I, "add9"), (III, "7"), (IV, "add9"), (V, "sus4")]
    hook = [(0, 1, 4), (1, 0.5, 2), (1.5, 0.5, 4), (2, 1, 7), (3, 1, 5)]
    return [
        P(0, 10, melody(k, prog, hook, r, n, octave=1, vel=56, hang=8), vol=70, rev=70, pan=70),
        P(1, 0, arp(k, prog, n, r, pattern=(0, 1, 2, 1, 3, 1, 2, 1), vel=46, center=58, ring=1.6), vol=88, rev=55, pan=52),
        P(2, 49, pad(k, prog, n, r, vel=30, center=60, start_bar=2), vol=74, rev=80),
        P(3, 32, bass(k, prog, n, r, rhythm=((0, 3.8),), vel=56, start_bar=2), vol=84, rev=20),
    ]


@track("LF-C", "littlefold", "sunny-morning", 92, 67, "G major", "cosy, happy",
       "Nylon strum, celesta and soft shaker; a 'good morning, little one' smile.")
def lf_c(k, n, r):
    prog = [(I, "triad"), (IV, "add9"), (I, "triad"), (V, "triad"), (VI, "7"), (IV, "add9"), (II, "7"), (V, "sus4")]
    hook = [(0, 0.5, 2), (0.5, 0.5, 4), (1, 1, 7), (2, 0.5, 6), (2.5, 0.5, 4), (3, 1, 5)]
    return [
        P(0, 24, chords(k, prog, n, r, rhythm=((0, .9), (1, .4), (1.5, .9), (2.5, .4), (3, .9)), vel=46, center=60), vol=86, rev=45, pan=46),
        P(1, 8, melody(k, prog, hook, r, n, octave=1, vel=58, hang=8), vol=78, rev=60, pan=78),
        P(2, 32, bass(k, prog, n, r, rhythm=((0, 1.4), (1.5, .5), (2, 1.9)), vel=62, start_bar=1), vol=86, rev=15),
        P(9, 0, beat(n, r, "brush", vel=52, start_bar=1), vol=62, rev=30),
    ]


# ----------------------------------------------------------------- Stingers
STINGERS = []


def stinger(code, slug, bpm, key_root, desc):
    def deco(fn):
        STINGERS.append(dict(code=code, page="all", slug=slug, bpm=bpm, key_root=key_root, key="",
                             mood="reveal", desc=desc, fn=fn))
        return fn
    return deco


@stinger("ST-1", "soft-rise", 96, 60, "Harp run up into a warm chord with a sparkle. Use right before the answer appears.")
def st_1(k, r):
    run = [(i * 0.25, 0.9, k.deg(d), 46 + i * 2) for i, d in enumerate(range(0, 15))]
    land = 15 * 0.25
    ch = [(land, 3.5, p, 58) for p in voice(k, k.chord(I, "add9"), 64)]
    sw = pad(k, [(IV, "add9")], 1, r, vel=24, center=60) + [(4, 3.4, p, 40) for p in voice(k, k.chord(I, "add9"), 60)]
    spark = [(land + i * 0.25, 1.2, k.deg(d, 2), 42) for i, d in enumerate((0, 4, 7))]
    return [P(0, 46, run + ch, vol=88, rev=70), P(1, 49, sw, vol=76, rev=85, expr=[(0, 50), (2, 85), (3.5, 110)]),
            P(2, 9, spark, vol=54, rev=85)], 7.5


@stinger("ST-2", "ta-da", 110, 60, "Two pick-up notes and a bright, friendly chord hit. The 'here it is' moment.")
def st_2(k, r):
    pick = [(0, 0.4, k.deg(4), 62), (0.5, 0.4, k.deg(5), 66)]
    hitp = [(1, 2.5, p, 70) for p in voice(k, k.chord(I, "add9"), 64)] + [(1, 2.5, k.deg(0, -1), 70)]
    gl = [(1 + i * 0.12, 1.5, k.deg(d, 2), 48) for i, d in enumerate((0, 2, 4, 7))]
    pizz = [(1, 0.5, p, 66) for p in voice(k, k.chord(I), 60)]
    return [P(0, 0, pick + hitp, vol=88, rev=60), P(1, 9, gl, vol=56, rev=80), P(2, 45, pizz, vol=80, rev=50),
            P(9, 0, [(1, .3, 36, 64)], vol=70)], 4.5


@stinger("ST-3", "wait-for-it", 92, 60, "A held 'hmm?' chord with a soft tick-tock, then it resolves. For 'wait for it' beats.")
def st_3(k, r):
    sus = [(0, 3.9, p, 50) for p in voice(k, k.chord(V, "sus4"), 62)]
    res = [(4, 3.5, p, 56) for p in voice(k, k.chord(I, "add9"), 64)]
    tick = [(i * 1.0, .1, 76 if i % 2 == 0 else 77, 38) for i in range(4)]
    spark = [(4 + i * 0.2, 1.2, k.deg(d, 2), 42) for i, d in enumerate((2, 4, 7))]
    return [P(0, 4, sus + res, vol=88, rev=60, cho=30), P(1, 49, [(b, d, p - 12, v - 16) for b, d, p, v in sus + res], vol=72, rev=80),
            P(2, 9, spark, vol=52, rev=80), P(9, 0, tick, vol=66, rev=30)], 8.0


def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    meta = []
    for t in TRACKS:
        k = Key(t["key_root"])
        n = bars_for(t["bpm"])
        parts = t["fn"](k, n, rng_for(t["code"]))
        name = t["code"].lower()
        write_midi(f"{outdir}/{name}.mid", t["bpm"], parts)
        loop = n * 4 * 60 / t["bpm"]
        meta.append({k_: v for k_, v in t.items() if k_ != "fn"} | {"bars": n, "loop_seconds": round(loop, 4), "kind": "bed"})
    for s in STINGERS:
        k = Key(s["key_root"])
        parts, beats = s["fn"](k, rng_for(s["code"]))
        name = s["code"].lower()
        write_midi(f"{outdir}/{name}.mid", s["bpm"], parts)
        meta.append({k_: v for k_, v in s.items() if k_ != "fn"} | {"bars": 0, "loop_seconds": round(beats * 60 / s["bpm"], 4), "kind": "stinger"})
    json.dump(meta, open(f"{outdir}/meta.json", "w"), indent=1)
    for m in meta:
        print(m["code"], m["slug"], m["bpm"], "bpm", m["loop_seconds"], "s")


if __name__ == "__main__":
    main(sys.argv[1])

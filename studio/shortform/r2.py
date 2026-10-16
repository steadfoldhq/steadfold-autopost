"""Short-form round 2 (Oct 16 2026): entertainment-first, interactive pilots that obey READABLE PACING.

What changed from round 1 (owner feedback: "viewers can't read everything in time"):
- Captions are whole short phrases (<= 6 words), shown at once, with the spoken word lit. The voice is paused
  after a phrase whenever needed, so every caption holds >= 0.4 s per word + 0.6 s.
- Every piece of text drawn goes through T(), which logs it per frame. After rendering, check_reading() measures how
  long each text stayed on screen and fails the build if any is shorter than the rule.
- Sound design from media/music/library (sfx-*, st-*), mixed under the ElevenLabs voice. No music bed in the file
  (a licensed sound is added in-app).
- The page is shown only as a 1-second, wordless end card (the logo mark).
"""
import json
import math
import os
import subprocess
import sys
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from engine import FPS, H, W, back, ease, font, hexc, rrect, text_size, words_from_alignment  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))
V = os.path.join(REPO, "media/voice/shortform/")
LIB = os.path.join(REPO, "media/music/library/")
MARKS = os.path.join(REPO, "studio/motion/assets/")
OUT = os.environ.get("SHORTFORM_OUT", "/tmp/shortform-r2")
PER_WORD, BASE = 0.4, 0.6
EMOJI_FONT = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"


def need(n):
    return PER_WORD * n + BASE


def nwords(s):
    return sum(1 for w in str(s).split() if any(c.isalnum() for c in w))


# ------------------------------------------------------------------------------------------- voice + phrases
def _decode(path, sr=44100):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "s16le", "-ac", "1", "-ar", str(sr), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768


def _ends_phrase(tok):
    core = tok.rstrip("'’\"”")
    return core.endswith((".", "?", "!", ":"))


MAXW = 6  # most words in one caption


def _alnum(tok):
    return any(c.isalnum() for c in tok)


def _split_long(words, p):
    """Split a phrase longer than MAXW words: at a comma if one leaves >= 2 words each side, else at the longest pause."""
    if sum(_alnum(words[j][0]) for j in p) <= MAXW:
        return [p]
    cands = [i for i in range(1, len(p) - 1) if words[p[i - 1]][0].endswith(",")]
    if not cands:
        cands = list(range(3, len(p) - 2)) or list(range(2, len(p) - 1))
        weak = {"to", "a", "an", "the", "of", "at", "in", "on", "and", "or", "your", "my", "any"}
        cands = [i for i in cands if words[p[i - 1]][0].lower() not in weak] or cands
    mid = len(p) / 2
    best = max(cands, key=lambda i: (words[p[i]][1] - words[p[i - 1]][2]) - 0.02 * abs(i - mid) - (0 if words[p[i - 1]][0].endswith(",") else 0.2))
    return _split_long(words, p[:best]) + _split_long(words, p[best:])


def phrases_of(words):
    out, cur = [], []
    for i, w in enumerate(words):
        cur.append(i)
        if _ends_phrase(w[0]):
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    res = []
    for p in out:
        res += _split_long(words, p)
    return res


def _splice(a, ws, skip, sr=44100):
    """Drop whole phrases (by index) from the voice: cut their audio, shift the word times."""
    ph = phrases_of(ws)
    txt = lambda p: " ".join(ws[j][0] for j in p)  # noqa: E731
    keep = [p for k, p in enumerate(ph) if k not in skip and txt(p) not in skip]
    assert all(isinstance(x, int) or any(txt(p) == x for p in ph) for x in skip), "skip text not found"
    out, nws, t = [], [], 0.0
    for p in keep:
        s0 = max(0.0, ws[p[0]][1] - 0.04)
        nxt = ws[p[-1] + 1][1] if p[-1] + 1 < len(ws) else len(a) / sr
        e0 = min(nxt - 0.04, ws[p[-1]][2] + 0.25) if p[-1] + 1 < len(ws) else len(a) / sr
        seg = a[int(s0 * sr):int(e0 * sr)]
        for j in p:
            nws.append([ws[j][0], t + ws[j][1] - s0, t + ws[j][2] - s0])
        out.append(seg)
        t += len(seg) / sr
    return np.concatenate(out), nws


def build_voice(name, out_wav, hold=None, maxgap=0.30, lead=0.15, min_gap=0.12, skip=()):
    """Voice with natural gaps trimmed, then a pause after any phrase that would leave the screen too soon.
    hold: {phrase_index: seconds} extra silence after that phrase (pauses for 'pause and guess', reveals).
    Returns (words, phrases, total_voice_seconds). Word times are on the final timeline."""
    hold = hold or {}
    sr = 44100
    a = _decode(V + name + ".mp3", sr)
    ws = words_from_alignment(json.load(open(V + name + ".json")))
    if skip:
        a, ws = _splice(a, ws, set(skip), sr)
    ph = phrases_of(ws)
    for key in [x for x in hold if isinstance(x, str)]:  # hold by phrase text
        ks = [k for k, p in enumerate(ph) if " ".join(ws[j][0] for j in p) == key]
        assert ks, f"hold text not found: {key}"
        hold[ks[0]] = hold.pop(key)
    last_of = {p[-1]: k for k, p in enumerate(ph)}
    first_of = {p[0]: k for k, p in enumerate(ph)}
    segs, words, t, pos = [np.zeros(int(lead * sr), np.float32)], [], lead, 0.0
    t_phrase_start = {}
    for i, (tok, s, e) in enumerate(ws):
        nxt = ws[i + 1][1] if i + 1 < len(ws) else len(a) / sr
        gap = nxt - e
        keep_to = (e + min(gap, maxgap)) if i + 1 < len(ws) else min(len(a) / sr, e + 0.3)
        seg = a[int(pos * sr):int(keep_to * sr)]
        ws_t = t + (s - pos)
        if i in first_of:
            t_phrase_start[first_of[i]] = ws_t
        words.append([tok, ws_t, t + (e - pos)])
        segs.append(seg)
        t += len(seg) / sr
        pos = max(keep_to, nxt - 0.05) if i + 1 < len(ws) else len(a) / sr
        if i in last_of:
            k = last_of[i]
            n = sum(1 for j in ph[k] if any(c.isalnum() for c in ws[j][0]))
            # time until the next phrase's first word if we add nothing more
            nxt_start = t + (nxt - pos if i + 1 < len(ws) else 0.0)
            short = need(n) + 0.05 - (nxt_start - t_phrase_start[k]) if i + 1 < len(ws) else 0.0
            extra = max(short, hold.get(k, 0.0), min_gap if i + 1 < len(ws) else 0.0)
            if extra > 0:
                segs.append(np.zeros(int(extra * sr), np.float32))
                t += extra
    segs.append(np.zeros(int(0.15 * sr), np.float32))
    y = np.concatenate(segs)
    with wave.open(out_wav, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
    return words, ph, len(y) / sr


class Script:
    """Phrase timeline: S.p(k) = start of phrase k; S.end(k) = when its caption leaves."""

    def __init__(self, name, hold=None, tail=0.0, endcard=1.0, skip=(), out_name=None):
        os.makedirs(OUT, exist_ok=True)
        self.name = out_name or name
        self.wav = f"{OUT}/{self.name}.voice.wav"
        self.words, self.ph, vt = build_voice(name, self.wav, hold, skip=skip)
        last = self.words[-1][2]
        last_need = self.p(len(self.ph) - 1) + need(self.nw(len(self.ph) - 1)) + 0.05
        self.end_voice = max(vt, last + 0.35, last_need) + tail
        self.endcard = endcard
        self.total = self.end_voice + endcard

    def nw(self, k):
        return sum(1 for j in self.ph[k] if any(c.isalnum() for c in self.words[j][0]))

    def p(self, k):
        return self.words[self.ph[k][0]][1] - 0.05

    def end(self, k):
        return self.p(k + 1) if k + 1 < len(self.ph) else self.end_voice

    def at(self, t):
        k = None
        for i in range(len(self.ph)):
            if self.p(i) <= t:
                k = i
        return k

    def text(self, k):
        return " ".join(self.words[j][0] for j in self.ph[k])

    def find(self, needle, after=0.0):
        nd = needle.lower().strip(".,?!:'\"")
        for w in self.words:
            if w[1] >= after and w[0].lower().strip(".,?!:'\"’“”") == nd:
                return w[1]
        raise KeyError(needle)

    def phrase(self, needle, after=-1):
        for k in range(after + 1, len(self.ph)):
            if needle.lower() in self.text(k).lower():
                return k
        raise KeyError(needle)


# ------------------------------------------------------------------------------------------- text logging
LOG = {}          # key -> set(frame indices)
LOGW = {}         # key -> words
_FRAME = [0]


def T(img, s, x, y, size=80, fill=(255, 255, 255, 255), f="black", anchor="mm", alpha=1.0, stroke=0, sfill=(0, 0, 0, 255),
      key=None, words=None, maxw=None, lh=1.12, scale=1.0):
    """Draw text (wrapped to maxw) and log it for the reading check. Returns bottom y."""
    if alpha <= 0.02 or not str(s).strip():
        return y
    fo = font(f, max(8, int(size * scale)))
    d = ImageDraw.Draw(img)
    lines = [str(s)]
    if not maxw and anchor[0] == "m":  # keep single lines inside the frame (60 px margins)
        wd = text_size(d, str(s), fo)[0]
        if wd > 960:
            fo = font(f, max(8, int(fo.size * 960 / wd)))
    if maxw:
        lines, line = [], ""
        for wd in str(s).split():
            tt = (line + " " + wd).strip()
            if text_size(d, tt, fo)[0] <= maxw:
                line = tt
            else:
                if line:
                    lines.append(line)
                line = wd
        if line:
            lines.append(line)
    hh = fo.size * lh
    y0 = y - (len(lines) - 1) * hh / 2 if anchor[1] == "m" else y
    for i, ln in enumerate(lines):  # draw into a small tile, then composite (much faster than a full-frame layer)
        bb = d.textbbox((x, y0 + i * hh), ln, font=fo, anchor=anchor, stroke_width=stroke)
        x0, yy0 = int(bb[0]) - 4, int(bb[1]) - 4
        tile = Image.new("RGBA", (int(bb[2]) - x0 + 8, int(bb[3]) - yy0 + 8), (0, 0, 0, 0))
        ImageDraw.Draw(tile).text((x - x0, y0 + i * hh - yy0), ln, font=fo, fill=fill[:3] + (int(255 * alpha),), anchor=anchor,
                                  stroke_width=stroke, stroke_fill=sfill[:3] + (int(255 * alpha),))
        _comp(img, tile, x0, yy0)
    k = key or str(s)
    LOG.setdefault(k, set()).add(_FRAME[0])
    LOGW[k] = words if words is not None else nwords(s)
    return y0 + len(lines) * hh


def _comp(img, tile, x, y):
    """alpha_composite that tolerates tiles hanging off the frame."""
    W0, H0 = img.size
    cx0, cy0 = max(0, -x), max(0, -y)
    cx1, cy1 = min(tile.width, W0 - x), min(tile.height, H0 - y)
    if cx1 <= cx0 or cy1 <= cy0:
        return
    if (cx0, cy0, cx1, cy1) != (0, 0, tile.width, tile.height):
        tile = tile.crop((cx0, cy0, cx1, cy1))
    img.alpha_composite(tile, (x + cx0, y + cy0))


def box(img, b, r, fill, shadow=None, outline=None, width=0):
    """Rounded rectangle drawn in a tile (fast). shadow=(dx, dy, rgba)."""
    x0, y0, x1, y1 = [int(v) for v in b]
    pad = 40
    ex = (shadow[0] if shadow else 0, shadow[1] if shadow else 0)
    tile = Image.new("RGBA", (x1 - x0 + 2 * pad + abs(ex[0]), y1 - y0 + 2 * pad + abs(ex[1])), (0, 0, 0, 0))
    d = ImageDraw.Draw(tile)
    if shadow:
        d.rounded_rectangle((pad + ex[0], pad + ex[1], pad + ex[0] + x1 - x0, pad + ex[1] + y1 - y0), r, fill=shadow[2])
    d.rounded_rectangle((pad, pad, pad + x1 - x0, pad + y1 - y0), r, fill=fill, outline=outline, width=width)
    _comp(img, tile, x0 - pad, y0 - pad)


_emo = {}


def emoji(img, ch, cx, cy, size=160, alpha=1.0, rot=0):
    if ch not in _emo:
        f = ImageFont.truetype(EMOJI_FONT, 109)
        im = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((80, 80), ch, font=f, embedded_color=True, anchor="mm")
        _emo[ch] = im.crop(im.getbbox() or (0, 0, 160, 160))
    e = _emo[ch]
    s = size / max(e.size)
    e = e.resize((max(1, int(e.width * s)), max(1, int(e.height * s))), Image.LANCZOS)
    if rot:
        e = e.rotate(rot, Image.BICUBIC, expand=True)
    if alpha < 1:
        e = e.copy()
        e.putalpha(e.split()[3].point(lambda v: int(v * alpha)))
    _comp(img, e, int(cx - e.width / 2), int(cy - e.height / 2))


_marks = {}


def mark(img, name, cx, cy, size, alpha=1.0):
    if name not in _marks:
        _marks[name] = Image.open(MARKS + name).convert("RGBA")
    m = _marks[name].resize((int(size), int(size)), Image.LANCZOS)
    if alpha < 1:
        m.putalpha(m.split()[3].point(lambda v: int(v * alpha)))
    _comp(img, m, int(cx - size / 2), int(cy - size / 2))


def pop(t, t0, d=0.28):
    return back((t - t0) / d) if t >= t0 else 0.0


def fade(t, t0, d=0.2):
    return ease((t - t0) / d) if t >= t0 else 0.0


def layer():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def put(img, L, s=1.0, cx=W / 2, cy=H / 2, alpha=1.0, dx=0, dy=0):
    """Composite a full-frame layer scaled about (cx, cy) and moved by (dx, dy). Works on the layer's bounding box only."""
    if s <= 0.02 or alpha <= 0.02:
        return
    bb = L.getbbox()
    if not bb:
        return
    tile = L.crop(bb)
    x, y = bb[0], bb[1]
    if abs(s - 1) > 0.004:
        tile = tile.resize((max(1, int(tile.width * s)), max(1, int(tile.height * s))), Image.BILINEAR)
        x, y = cx + (x - cx) * s, cy + (y - cy) * s
    if alpha < 1:
        tile.putalpha(tile.split()[3].point(lambda v: int(v * alpha)))
    _comp(img, tile, int(x + dx), int(y + dy))


def dots_bg(base, dot, t, spacing=54, r=3, vx=6, vy=10):
    img = Image.new("RGBA", (W, H), base)
    d = ImageDraw.Draw(img)
    ox, oy = (vx * t) % spacing, (vy * t) % spacing
    y = -spacing + oy
    while y < H + spacing:
        x = -spacing + ox
        while x < W + spacing:
            d.ellipse((x - r, y - r, x + r, y + r), fill=dot)
            x += spacing
        y += spacing
    return img


def shake(t, t0, dur=0.25, amp=18):
    if t0 <= t < t0 + dur:
        k = 1 - (t - t0) / dur
        return amp * k * math.sin(t * 90), amp * k * math.cos(t * 77)
    return 0, 0


# ------------------------------------------------------------------------------------------- captions
def captions(img, S, t, y=1290, size=104, fill=(255, 255, 255, 255), lit=(255, 214, 59, 255), stroke=(14, 20, 64, 255),
             upper=True, maxw=940, box=None):
    """The current phrase, whole, with the spoken word lit. Big, centred, clear of the app buttons (y 1180-1420)."""
    k = S.at(t)
    if k is None or t >= S.end_voice:
        return
    toks = [S.words[j] for j in S.ph[k]]
    clean = lambda s: s.replace("’", "'")  # noqa: E731
    disp = [clean(w[0]).upper() if upper else clean(w[0]) for w in toks]
    fo = font("black", size)
    d = ImageDraw.Draw(img)
    sp = size * 0.26
    # wrap into lines
    lines, cur, cw = [], [], 0
    for i, s in enumerate(disp):
        wdt = text_size(d, s, fo)[0]
        if cur and cw + sp + wdt > maxw:
            lines.append(cur)
            cur, cw = [], 0
        cur.append(i)
        cw += (sp if cw else 0) + wdt
    if cur:
        lines.append(cur)
    L = layer()
    ld = ImageDraw.Draw(L)
    lh = size * 1.12
    y0 = y - (len(lines) - 1) * lh / 2
    if box:
        rrect(L, (60, y0 - lh / 2 - 26, W - 60, y0 + (len(lines) - 1) * lh + lh / 2 + 18), 34, box)
    for li, ln in enumerate(lines):
        ws = [text_size(d, disp[i], fo)[0] for i in ln]
        x = W / 2 - (sum(ws) + sp * (len(ln) - 1)) / 2
        for i, wdt in zip(ln, ws):
            on = toks[i][1] - 0.04 <= t < toks[i][2] + 0.12
            ld.text((x, y0 + li * lh), disp[i], font=fo, fill=lit if on else fill, anchor="lm",
                    stroke_width=max(6, int(size * 0.085)), stroke_fill=stroke)
            x += wdt + sp
    p = pop(t, S.p(k), 0.2)
    put(img, L, 0.9 + 0.1 * p, W / 2, y)
    key = f"cap{k}"
    LOG.setdefault(key, set()).add(_FRAME[0])
    LOGW[key] = S.nw(k)


def endcard(img, S, t, bg, mark_name):
    """1-second wordless end card: the page's mark pops in."""
    u = t - S.end_voice
    img.paste(Image.new("RGBA", (W, H), bg), (0, 0))
    p = pop(u, 0.0, 0.35)
    mark(img, mark_name, W / 2, H * 0.42, 420 * (0.6 + 0.4 * p), alpha=min(1, u / 0.15))


# ------------------------------------------------------------------------------------------- audio
def sfx_track(cues, total, out_wav, sr=44100):
    """cues: [(name, t, gain_db)]  name = file in media/music/library without .mp3"""
    a = np.zeros(int((total + 2) * sr), np.float32)
    cache = {}
    for name, t0, g in cues:
        if name not in cache:
            cache[name] = _decode(LIB + name + ".mp3", sr)
        s = cache[name] * (10 ** (g / 20))
        i = int(max(0, t0) * sr)
        n = min(len(s), len(a) - i)
        if n > 0:
            a[i:i + n] += s[:n]
    a = a[:int(total * sr)]
    with wave.open(out_wav, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())


def render(S, draw, cues, outdir=OUT):
    LOG.clear()
    LOGW.clear()
    os.makedirs(outdir, exist_ok=True)
    silent = f"{outdir}/{S.name}.video.mp4"
    n = int(round(S.total * FPS))
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", silent],
                         stdin=subprocess.PIPE)
    for i in range(n):
        _FRAME[0] = i
        im = draw(i / FPS)
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close()
    p.wait()
    fx = f"{outdir}/{S.name}.fx.wav"
    sfx_track(cues, S.total, fx)
    out = f"{outdir}/{S.name}.mp4"
    filt = ("[1:a]apad,loudnorm=I=-16:TP=-2:LRA=9[v];[2:a]apad[f];[v][f]amix=inputs=2:duration=first:normalize=0,"
            "alimiter=limit=0.89,loudnorm=I=-15:TP=-1.5:LRA=9[a]")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", silent, "-i", S.wav, "-i", fx, "-filter_complex", filt, "-map", "0:v",
                    "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-t", f"{S.total:.3f}",
                    "-movflags", "+faststart", out], check=True)
    os.remove(silent)
    return out


def check_reading(fps=FPS):
    """Every logged text: each continuous on-screen run must last >= 0.4 s/word + 0.6 s. Returns (rows, failures)."""
    rows, bad = [], []
    for k, frames in LOG.items():
        fr = sorted(frames)
        runs, st, pv = [], fr[0], fr[0]
        for f in fr[1:]:
            if f != pv + 1:
                runs.append((st, pv))
                st = f
            pv = f
        runs.append((st, pv))
        n = LOGW.get(k, 0)
        for a, b in runs:
            dur = (b - a + 1) / fps
            ok = n == 0 or dur + 1e-6 >= need(n)
            rows.append(dict(text=k, words=n, on=round(a / fps, 2), secs=round(dur, 2), need=round(need(n), 2), ok=ok))
            if not ok:
                bad.append(rows[-1])
    return rows, bad


def sheet(path, times, outpng, cols=6, scale=0.22):
    """Contact sheet from the finished MP4."""
    ims = []
    for t in times:
        r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", path, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                           capture_output=True)
        if r.stdout:
            import io
            im = Image.open(io.BytesIO(r.stdout)).convert("RGB").resize((int(W * scale), int(H * scale)))
            ImageDraw.Draw(im).text((6, 6), f"{t:.1f}s", fill=(255, 0, 0))
            ims.append(im)
    rows = math.ceil(len(ims) / cols)
    sh = Image.new("RGB", (cols * ims[0].width, rows * ims[0].height), "black")
    for k, im in enumerate(ims):
        sh.paste(im, ((k % cols) * im.width, (k // cols) * im.height))
    sh.save(outpng, quality=85)


def finish(S, draw, cues, report_extra=None):
    out = render(S, draw, cues)
    rows, bad = check_reading()
    rep = dict(id=S.name, total=round(S.total, 2), phrases=len(S.ph), texts=len(rows), too_fast=bad, out=out)
    json.dump(dict(rep, rows=rows), open(f"{OUT}/{S.name}.reading.json", "w"), indent=1)
    sheet(out, [0.0, 0.5] + [S.p(k) + 0.3 for k in range(0, len(S.ph), max(1, len(S.ph) // 16))] + [S.total - 0.5],
          f"{OUT}/{S.name}-sheet.jpg")
    print(json.dumps(dict(rep, rows=None)))
    if bad:
        sys.exit(f"READING RULE FAILED: {bad}")
    return out

"""Short-form round 2 (Oct 16 2026): entertainment-first, interactive pilots that obey READABLE PACING.

Round 2b (Oct 16 pm, owner feedback on sound and polish):
- VOICE: one continuous Eleven v3 take per pilot (house voices in tools/voices.json, audio tags + ellipses). The take is
  never cut or spliced. Only where a beat needs a hold ('pause and guess') or a caption needs more screen time is a
  pause lengthened, at its quietest point inside a natural gap.
- NO DEAD AIR: a music bed (media/music/library) and room tone run continuously under everything; the bed ducks under
  the voice and rises in pauses. check_audio() fails the build on any > 250 ms drop below -50 dBFS.
- LOUDNESS: two-pass loudnorm to -14 LUFS, true peak <= -1.5 dBTP; verified with tools/music_check.py.
- CLEAN TEXT: words float with a very soft shadow only (no outline, box, band or halo). Every text's contrast against
  what is actually behind it is measured per frame (>= 3:1) and the build fails below that.
- READABLE PACING: captions are whole short phrases with the spoken word lit; each caption rolls up to the line above
  while the next is spoken, so it holds >= 0.4 s/word + 0.6 s without slowing the voice. check_reading() enforces it.
- LOCKED HOUR LOOK: colour scenes (scene_bg) that hard-cut under bold transitions (transition(): whip blur + colour
  slab or iris) landing exactly on the spoken line.
- The page is shown only as a 1-second, wordless end card (the logo mark), with the music still playing.
"""
import json
import math
import os
import subprocess
import sys
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

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


def _quiet_point(a, s0, s1, sr=44100):
    """Quietest 10 ms inside [s0, s1] (seconds) of the take: where a pause can be lengthened inaudibly."""
    i0, i1 = int(s0 * sr), int(s1 * sr)
    if i1 - i0 < int(0.03 * sr):
        return (s0 + s1) / 2
    win = int(0.01 * sr)
    x = a[i0:i1] ** 2
    c = np.convolve(x, np.ones(win) / win, "valid")
    return (i0 + int(np.argmin(c)) + win // 2) / sr


def caption_groups(ws, ph, hold, lead=0.0):
    """Fold very short phrases ('One.', 'Fine.', 'Okay.') forward into the next phrase when the pair stays <= 5 words, so
    captions don't flicker. A phrase with a hold after it always ends its caption."""
    nw = lambda p: sum(1 for j in p if _alnum(ws[j][0]))  # noqa: E731
    groups = [[k] for k in range(len(ph))]
    g = 0
    while g < len(groups) - 1:
        cur, nxt = groups[g], groups[g + 1]
        wc, wn = sum(nw(ph[k]) for k in cur), sum(nw(ph[k]) for k in nxt)
        if wc <= 2 and wc + wn <= 5 and cur[-1] not in hold:
            groups[g] = cur + nxt
            del groups[g + 1]
            continue
        g += 1
    return groups


ROLL = 2   # captions roll: each caption stays up (as the line above) while the next one is spoken


def build_voice(name, out_wav, hold=None, lead=0.25, tail=0.3, min_gap=0.0):
    """ONE continuous take, never cut. Captions are grouped from whole phrases; where a caption still needs more
    screen time (or a beat needs a hold, e.g. 'pause and guess'), the take's own pause after that caption is
    lengthened at its quietest point. Room tone and music run under everything, so a pause is never dead air.
    hold: {phrase index or exact phrase text: minimum seconds of pause after it}.
    Returns (words, phrases, groups, total_voice_seconds, inserts). Word times are on the final timeline."""
    sr = 44100
    a = _decode(V + name + ".mp3", sr)
    ws = words_from_alignment(json.load(open(V + name + ".json")))
    ph = phrases_of(ws)
    hold = dict(hold or {})
    for key in [x for x in hold if isinstance(x, str)]:
        ks = [k for k, p in enumerate(ph) if " ".join(ws[j][0] for j in p) == key]
        assert ks, f"hold text not found: {key!r} in {[' '.join(ws[j][0] for j in p) for p in ph]}"
        hold[ks[0]] = hold.pop(key)
    groups = caption_groups(ws, ph, hold)
    # plan the pause lengthening on the source clock. A caption is on screen from its start until ROLL captions later
    # (it rolls up to the line above), so it only needs need(words) across that window.
    starts = [ws[ph[grp[0]][0]][1] for grp in groups]
    ends = [ws[ph[grp[-1]][-1]][2] for grp in groups]
    ins = [0.0] * len(groups)          # extra seconds after caption i (before caption i+1)
    for i in range(len(groups) - 1):
        ins[i] = max(0.0, hold.get(groups[i][-1], 0.0) - (starts[i + 1] - ends[i]), min_gap - (starts[i + 1] - ends[i]))
    for g in range(len(groups)):
        j = g + ROLL
        if j >= len(groups):
            break
        n = sum(1 for k in groups[g] for jj in ph[k] if _alnum(ws[jj][0]))
        have = starts[j] - starts[g] + sum(ins[g:j])
        if have < need(n) + 0.06:
            # lengthen the larger natural pause inside the window (sentence ends breathe best)
            i = max(range(g, j), key=lambda i: starts[i + 1] - ends[i])
            ins[i] += need(n) + 0.06 - have
    inserts = [(_quiet_point(a, ends[i] + 0.02, starts[i + 1] - 0.02, sr), ins[i])
               for i in range(len(groups) - 1) if ins[i] > 0.005]
    added = 0.0
    # last caption must also stay long enough
    segs, pos = [np.zeros(int(lead * sr), np.float32)], 0.0
    shift = []            # (source_time, cumulative shift after it)
    cum = lead
    for st, ex in inserts:
        seg = a[int(pos * sr):int(st * sr)].copy()
        f = min(len(seg), int(0.008 * sr))
        if f:
            seg[-f:] *= np.linspace(1, 0, f)
        segs.append(seg)
        segs.append(np.zeros(int(ex * sr), np.float32))
        pos = st
        cum += ex
        shift.append((st, cum))
        added += ex
    seg = a[int(pos * sr):].copy()
    if inserts:
        f = min(len(seg), int(0.008 * sr))
        seg[:f] *= np.linspace(0, 1, f)
    segs.append(seg)
    segs.append(np.zeros(int(tail * sr), np.float32))

    def remap(x):
        s = lead
        for st, c in shift:
            if x >= st:
                s = c
        return x + s

    words = [[tok, remap(s), remap(e)] for tok, s, e in ws]
    y = np.concatenate(segs)
    with wave.open(out_wav, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
    return words, ph, groups, len(y) / sr, [(round(remap(s), 2), round(e, 2)) for s, e in inserts]


class Script:
    """Phrase timeline: S.p(k) = start of phrase k (visual anchors). Captions run by group: S.groups."""

    def __init__(self, name, hold=None, tail=0.0, endcard=1.0, out_name=None, min_gap=0.0):
        os.makedirs(OUT, exist_ok=True)
        self.name = out_name or name
        self.voice_name = name
        self.wav = f"{OUT}/{self.name}.voice.wav"
        self.words, self.ph, self.groups, vt, self.inserts = build_voice(name, self.wav, hold, min_gap=min_gap)
        last = self.words[-1][2]
        g = self.groups[-1]
        last_need = max(self.gp(i) + need(self.gw(i)) + 0.05 for i in range(max(0, len(self.groups) - ROLL), len(self.groups)))
        self.end_voice = max(vt, last + 0.35, last_need) + tail
        self.endcard = endcard
        self.total = self.end_voice + endcard

    def nw(self, k):
        return sum(1 for j in self.ph[k] if any(c.isalnum() for c in self.words[j][0]))

    def gw(self, g):
        return sum(self.nw(k) for k in self.groups[g])

    def p(self, k):
        return self.words[self.ph[k][0]][1] - 0.05

    def gp(self, g):
        return self.p(self.groups[g][0])

    def end(self, k):
        return self.p(k + 1) if k + 1 < len(self.ph) else self.end_voice

    def at(self, t):
        k = None
        for i in range(len(self.ph)):
            if self.p(i) <= t:
                k = i
        return k

    def gat(self, t):
        g = None
        for i in range(len(self.groups)):
            if self.gp(i) <= t:
                g = i
        return g

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
        raise KeyError(f"{needle!r} not in {[self.text(i) for i in range(len(self.ph))]}")


# ------------------------------------------------------------------------------------------- text logging
LOG = {}          # key -> set(frame indices)
LOGW = {}         # key -> words
CONTRAST = {}     # key -> worst contrast ratio seen (text colour vs what is behind it)
CONTRAST_AT = {}  # key -> frame of that worst case
_FRAME = [0]
_BG = [None]      # this frame's background (set by dots_bg / scene_bg): what a layer will land on
MIN_CONTRAST = 3.0   # WCAG large-text minimum; all our type is >= 32 px bold


def _lum(rgb):
    c = np.asarray(rgb, np.float32)[..., :3] / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def _ratio(l1, l2):
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def _behind(img, bb):
    """Pixels the text will sit on: the target image, with the frame background under any see-through part."""
    x0, y0, x1, y1 = [int(v) for v in bb]
    x0, y0, x1, y1 = max(0, x0), max(0, y0), min(img.width, x1), min(img.height, y1)
    if x1 - x0 < 2 or y1 - y0 < 2:
        return None
    reg = img.crop((x0, y0, x1, y1))
    if _BG[0] is not None and img is not _BG[0] and np.asarray(reg)[..., 3].mean() < 250:
        base = _BG[0].crop((x0, y0, x1, y1)).copy()
        base.alpha_composite(reg)
        reg = base
    return np.asarray(reg.convert("RGB"))[::3, ::3]


def check_contrast(img, bb, fill, key):
    px = _behind(img, bb)
    if px is None:
        return
    lb = _lum(px).reshape(-1)
    lt = float(_lum(np.array(fill[:3])))
    # the text must read against the typical pixel behind it, and against 90 % of them
    worst = min(_ratio(lt, float(v)) for v in (np.median(lb), np.percentile(lb, 10), np.percentile(lb, 90)))
    if worst < CONTRAST.get(key, 99.0):
        CONTRAST[key] = worst
        CONTRAST_AT[key] = _FRAME[0]


def soft_shadow_tile(mask, size, dark=True):
    """A very soft drop shadow from a text mask: no outline, no box, no halo ring."""
    r = max(3, int(size * 0.07))
    a = 0.42 if dark else 0.18
    sh = mask.filter(ImageFilter.GaussianBlur(r)).point(lambda v: int(v * a))
    tile = Image.new("RGBA", mask.size, (0, 0, 0, 0))
    tile.putalpha(sh)
    return tile


def T(img, s, x, y, size=80, fill=(255, 255, 255, 255), f="black", anchor="mm", alpha=1.0, stroke=0, sfill=(0, 0, 0, 255),
      key=None, words=None, maxw=None, lh=1.12, scale=1.0, shadow=True):
    """Draw floating text (wrapped to maxw) with a very soft shadow, log it for the reading and contrast checks.
    stroke/sfill are accepted for old call sites but ignored: no outlines (CLEAN TEXT rule)."""
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
    k = key or str(s)
    light_text = float(_lum(np.array(fill[:3]))) > 0.4
    off = max(2, int(fo.size * 0.05))
    for i, ln in enumerate(lines):
        bb = d.textbbox((x, y0 + i * hh), ln, font=fo, anchor=anchor)
        pad = max(10, int(fo.size * 0.25))
        x0, yy0 = int(bb[0]) - pad, int(bb[1]) - pad
        sz = (int(bb[2]) - x0 + pad, int(bb[3]) - yy0 + pad + off)
        if alpha > 0.6 and (words is None or words > 0):
            check_contrast(img, bb, fill, k)
        mask = Image.new("L", sz, 0)
        ImageDraw.Draw(mask).text((x - x0, y0 + i * hh - yy0), ln, font=fo, fill=int(255 * alpha), anchor=anchor)
        if shadow:
            _comp(img, soft_shadow_tile(mask, fo.size, dark=light_text), x0, yy0 + off)
        tile = Image.new("RGBA", sz, fill[:3] + (0,))
        tile.putalpha(mask)
        _comp(img, tile, x0, yy0)
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
    _BG[0] = img.copy()
    return img


def scene_bg(t, scenes):
    """scenes: [(t_start, base_rgba, dot_rgba)]. The background colour hard-cuts on each scene start
    (the cut itself is hidden under a transition(), Locked Hour style)."""
    cur = scenes[0]
    for sc in scenes:
        if t >= sc[0]:
            cur = sc
    return dots_bg(cur[1], cur[2], t)


def shake(t, t0, dur=0.25, amp=18):
    if t0 <= t < t0 + dur:
        k = 1 - (t - t0) / dur
        return amp * k * math.sin(t * 90), amp * k * math.cos(t * 77)
    return 0, 0


# ------------------------------------------------------------------------------------------- transitions
TD = 0.34   # transition length (s), centred on the cut


def _whip(img, px):
    """Horizontal motion blur of px pixels (whip pan)."""
    if px < 4:
        return img
    a = np.asarray(img.convert("RGB")).astype(np.float32)
    n = 7
    acc = np.zeros_like(a)
    for i in range(n):
        acc += np.roll(a, int(px * (i / (n - 1) - 0.5)), axis=1)
    return Image.fromarray((acc / n).astype(np.uint8)).convert("RGBA")


def transition(img, t, cuts):
    """cuts: [(t_cut, colour, kind)] kind in wipeL wipeR wipeU wipeD iris. A bold colour slab sweeps across with a
    whip blur, fully covering the frame at t_cut, where the scene (and background colour) swaps underneath.
    Returns the new image. Frames mostly covered are not counted as 'text on screen' by the reading check."""
    for tc, col, kind in cuts:
        u = (t - (tc - TD / 2)) / TD
        if not 0.0 <= u <= 1.0:
            continue
        sp = math.sin(math.pi * u)                      # 0 -> 1 (at the cut) -> 0
        img = _whip(img, 140 * sp if kind in ("wipeL", "wipeR") else 0)
        if kind in ("wipeU", "wipeD") and sp > 0.1:     # vertical whip
            a = np.asarray(img.convert("RGB")).astype(np.float32)
            acc = sum(np.roll(a, int(120 * sp * (i / 6 - 0.5)), axis=0) for i in range(7)) / 7
            img = Image.fromarray(acc.astype(np.uint8)).convert("RGBA")
        L = layer()
        d = ImageDraw.Draw(L)
        e = u * u * (3 - 2 * u)
        if kind == "iris":
            r = 1250 * math.sin(math.pi * e)
            d.ellipse((W / 2 - r, H / 2 - r, W / 2 + r, H / 2 + r), fill=col)
        else:
            span = 2 * W + 600 if kind in ("wipeL", "wipeR") else 2 * H + 600
            lead = -300 + e * span                    # slab leading edge
            tail = lead - (W + 400 if kind in ("wipeL", "wipeR") else H + 400)
            sk = 260
            if kind == "wipeR":
                poly = [(lead, 0), (lead - sk, H), (tail - sk, H), (tail, 0)]
            elif kind == "wipeL":
                poly = [(W - lead, 0), (W - lead + sk, H), (W - tail + sk, H), (W - tail, 0)]
            elif kind == "wipeD":
                poly = [(0, lead), (W, lead - sk), (W, tail - sk), (0, tail)]
            else:
                poly = [(0, H - lead), (W, H - lead + sk), (W, H - tail + sk), (0, H - tail)]
            d.polygon(poly, fill=col)
        cover = np.asarray(L)[::16, ::16, 3].mean() / 255
        img.alpha_composite(L)
        if cover > 0.5:
            for k, fr in LOG.items():
                fr.discard(_FRAME[0])
    return img


# ------------------------------------------------------------------------------------------- captions
INK0 = (20, 20, 24, 255)


def captions(img, S, t, y=1290, size=104, fill=None, lit=None, stroke=None, upper=True, maxw=940, box=None,
             lit_light=(255, 214, 59, 255), lit_dark=(205, 22, 96, 255), ink=INK0):
    """The current caption group (whole short phrases, <= 6 words), with the spoken word lit. Words float with a soft
    shadow: no outline, box or band. Colours follow what is behind them: white on dark scenes, ink on light ones.
    fill/lit force colours; stroke and box are ignored (CLEAN TEXT rule)."""
    g = S.gat(t)
    if g is None or t >= S.end_voice:
        return img
    clean = lambda s: s.replace("’", "'")  # noqa: E731
    d = ImageDraw.Draw(img)

    def layout(gi, sz):
        toks = [S.words[j] for k in S.groups[gi] for j in S.ph[k]]
        disp = [clean(w[0]).upper() if upper else clean(w[0]) for w in toks]
        fo = font("black", sz)
        sp = sz * 0.26
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
        return toks, disp, fo, sp, lines

    toks, disp, fo, sp, lines = layout(g, size)
    if len(lines) > 1:
        size = int(size * 0.92)
        toks, disp, fo, sp, lines = layout(g, size)
    lh = size * 1.12
    zone = y - 150            # caption zone: y-150 .. ~y+135, kept clear of the picture above and the app UI below
    prev = None
    top = zone + 40
    if g >= 1 and ROLL > 1:   # the previous caption rolls up and stays readable, smaller, on one line above
        psz = int(size * 0.6)
        while True:
            ptoks, pdisp, pfo, psp, plines = layout(g - 1, psz)
            if len(plines) == 1 or psz <= 44:
                break
            psz -= 4
        plh = psz * 1.12
        prev = (ptoks, pdisp, pfo, psp, plines, plh, zone + plh / 2)
        top = zone + len(plines) * plh + 14
    y0 = top + lh / 2
    region = (60, int(zone), W - 60, int(y0 + (len(lines) - 1) * lh + lh / 2))
    px = _behind(img, region)
    light_bg = px is not None and float(np.median(_lum(px))) > 0.35
    f_col = fill or (ink if light_bg else (255, 255, 255, 255))
    l_col = lit or (lit_dark if light_bg else lit_light)
    if px is not None:        # what is behind can change (a transition slab passing): keep both colours readable
        lb = _lum(px).reshape(-1)
        stats = [float(np.median(lb)), float(np.percentile(lb, 10)), float(np.percentile(lb, 90))]

        def worst(c):
            lt = float(_lum(np.array(c[:3])))
            return min(_ratio(lt, v) for v in stats)

        pool = [ink, (255, 255, 255, 255), lit_light, lit_dark]
        if worst(f_col) < MIN_CONTRAST:
            f_col = max(pool[:2], key=worst)
        if worst(l_col) < MIN_CONTRAST or l_col == f_col:
            cands = [c for c in [l_col] + pool[2:] + pool[:2] if c != f_col and worst(c) >= MIN_CONTRAST]
            l_col = cands[0] if cands else max([c for c in pool if c != f_col], key=worst)
    M = Image.new("L", (W, H), 0)          # text mask for the soft shadow
    L = layer()
    ld, md = ImageDraw.Draw(L), ImageDraw.Draw(M)

    def draw_lines(tk, ds, f_, sp_, lns, lh_, ytop, live):
        for li, ln in enumerate(lns):
            ws = [text_size(d, ds[i], f_)[0] for i in ln]
            x = W / 2 - (sum(ws) + sp_ * (len(ln) - 1)) / 2
            for i, wdt in zip(ln, ws):
                on = live and tk[i][1] - 0.04 <= t < tk[i][2] + 0.12
                yy = ytop + li * lh_ - (6 if on else 0)
                ld.text((x, yy), ds[i], font=f_, fill=l_col if on else f_col, anchor="lm")
                md.text((x, yy), ds[i], font=f_, fill=255, anchor="lm")
                x += wdt + sp_

    if prev:
        ptoks, pdisp, pfo, psp, plines, plh, pyl = prev
        draw_lines(ptoks, pdisp, pfo, psp, plines, plh, pyl, False)
        pk = f"cap{g - 1}"
        LOG.setdefault(pk, set()).add(_FRAME[0])
    draw_lines(toks, disp, fo, sp, lines, lh, y0, True)
    bb = M.getbbox()
    key = f"cap{g}"
    if bb:
        check_contrast(img, bb, f_col, key)
        check_contrast(img, bb, l_col, key)
        pad = int(size * 0.4)
        cb = (max(0, bb[0] - pad), max(0, bb[1] - pad), min(W, bb[2] + pad), min(H, bb[3] + pad))
        off = max(2, int(size * 0.05))
        tile = Image.new("RGBA", (cb[2] - cb[0], cb[3] - cb[1]), (0, 0, 0, 0))
        sh = soft_shadow_tile(M.crop((cb[0], cb[1] - off, cb[2], cb[3] - off)), size, dark=not light_bg)
        tile.alpha_composite(sh)
        tile.alpha_composite(L.crop(cb))
        L = layer()
        L.paste(tile, cb[:2])
    p = pop(t, S.gp(g), 0.2)
    put(img, L, 0.94 + 0.06 * p, W / 2, y)
    LOG.setdefault(key, set()).add(_FRAME[0])
    LOGW[key] = S.gw(g)
    return img


def endcard(img, S, t, bg, mark_name):
    """1-second wordless end card: the page's mark pops in (music keeps playing under it)."""
    u = t - S.end_voice
    img.paste(Image.new("RGBA", (W, H), bg), (0, 0))
    p = pop(u, 0.0, 0.35)
    mark(img, mark_name, W / 2, H * 0.42, 420 * (0.6 + 0.4 * p), alpha=min(1, u / 0.15))


# ------------------------------------------------------------------------------------------- audio
SR = 44100


def _decode_st(path, sr=SR):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", "2", "-ar", str(sr), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, "<f4").reshape(-1, 2).copy()


def _lufs_arr(x, sr=SR):
    """Integrated loudness (LUFS) of a float array via ffmpeg's ebur128."""
    x = x if x.ndim == 2 else np.stack([x, x], 1)
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-f", "f32le", "-ac", "2", "-ar", str(sr), "-i", "-",
                        "-af", "ebur128", "-f", "null", "-"], input=x.astype("<f4").tobytes(), capture_output=True)
    err = p.stderr.decode()
    summ = err[err.rfind("Summary:"):]
    import re
    return float(re.search(r"I:\s+(-?[\d.]+) LUFS", summ).group(1))


def _loop(x, n, xf=1.2, sr=SR):
    """Loop a stereo bed to n samples with equal-power crossfades (no seam, no gap)."""
    f = int(xf * sr)
    if len(x) >= n:
        return x[:n].copy()
    out = x.copy()
    ramp = np.sin(np.linspace(0, math.pi / 2, f))[:, None]
    while len(out) < n:
        head = out[:-f]
        join = out[-f:] * ramp[::-1] + x[:f] * ramp
        out = np.concatenate([head, join, x[f:]])
    return out[:n]


def _env(v, sr=SR, win=0.02, att=0.06, rel=0.45):
    """Voice activity envelope 0..1 (smoothed), for ducking the bed."""
    hop = int(win * sr)
    n = len(v) // hop + 1
    pad = np.zeros(n * hop, np.float32)
    pad[:len(v)] = v
    rms = np.sqrt((pad.reshape(n, hop) ** 2).mean(1))
    act = (20 * np.log10(rms + 1e-9) > -38).astype(np.float32)
    out = np.zeros(n, np.float32)
    a, r = math.exp(-win / att), math.exp(-win / rel)
    s = 0.0
    for i, x in enumerate(act):
        c = a if x > s else r
        s = c * s + (1 - c) * x
        out[i] = s
    return np.interp(np.arange(len(v)) / hop, np.arange(n), out).astype(np.float32)


BED_GAP_DB, BED_UNDER_DB, AMB_DB = -11.0, -19.0, -24.0   # relative to the voice level


def mix(S, cues, bed, amb, out_wav):
    """Voice (one take) + a continuous music bed ducked under the voice + continuous room tone + SFX.
    Every source is levelled to -16 LUFS first, then placed relative to the voice. Returns the stems for QA."""
    n = int(S.total * SR)
    v = _decode(S.wav, SR)
    v = np.pad(v, (0, max(0, n - len(v))))[:n]
    v *= 10 ** ((-16 - _lufs_arr(v[:int(S.end_voice * SR)])) / 20)
    b = _loop(_decode_st(LIB + bed), n)
    b *= 10 ** ((-16 - _lufs_arr(b)) / 20)
    e = _env(v)
    gdb = BED_GAP_DB + (BED_UNDER_DB - BED_GAP_DB) * e
    b *= (10 ** (gdb / 20))[:, None]
    am = _loop(_decode_st(LIB + amb), n, xf=2.0)
    am *= 10 ** ((-16 + AMB_DB - _lufs_arr(am)) / 20)
    fx = np.zeros(n + 4 * SR, np.float32)
    cache = {}
    for name, t0, gdb_ in cues:
        if name not in cache:
            cache[name] = _decode(LIB + name + ".mp3", SR)
        s = cache[name] * (10 ** (gdb_ / 20))
        i = int(max(0, t0) * SR)
        m = min(len(s), len(fx) - i)
        if m > 0:
            fx[i:i + m] += s[:m]
    fx = fx[:n]
    y = b + am + (v + fx)[:, None]
    fi, fo = int(0.03 * SR), int(0.45 * SR)
    y[:fi] *= np.linspace(0, 1, fi)[:, None]
    y[-fo:] *= np.linspace(1, 0, fo)[:, None]
    with wave.open(out_wav, "w") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
    return v, (b + am)


def master(silent, mix_wav, out, total, target=-14.0, tp=-1.5):
    """Two-pass loudnorm to -14 LUFS, true peak <= -1.5 dBTP, muxed with the picture."""
    import re
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", mix_wav, "-af",
                        f"loudnorm=I={target}:TP={tp}:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True)
    m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", p.stderr, re.S).group(0))
    filt = (f"loudnorm=I={target}:TP={tp}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
            f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", silent, "-i", mix_wav, "-map", "0:v", "-map", "1:a", "-af", filt,
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-t", f"{total:.3f}",
                    "-movflags", "+faststart", out], check=True)


def render(S, draw, cues, outdir=OUT, bed=None, amb="amb-room-tone.mp3"):
    LOG.clear()
    LOGW.clear()
    CONTRAST.clear()
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
    mw = f"{outdir}/{S.name}.mix.wav"
    voice, bedstem = mix(S, cues, bed, amb, mw)
    out = f"{outdir}/{S.name}.mp4"
    master(silent, mw, out, S.total)
    os.remove(silent)
    return out, voice, bedstem


# ------------------------------------------------------------------------------------------- QA
def _rms_db(x, win):
    m = len(x) // win
    x = x[:m * win].reshape(m, win, -1) if x.ndim == 2 else x[:m * win].reshape(m, win)
    return 20 * np.log10(np.sqrt((x ** 2).reshape(m, -1).mean(1)) + 1e-9)


def _runs(mask):
    runs, st = [], None
    for i, v in enumerate(list(mask) + [False]):
        if v and st is None:
            st = i
        elif not v and st is not None:
            runs.append((st, i))
            st = None
    return runs


def check_audio(mp4, voice, bedstem, total):
    """No dead air: (1) the finished mix never drops below -50 dBFS for > 250 ms; (2) every pause in the voice
    longer than 250 ms has the bed audible under it (>= -50 dBFS). (3) Loudness via tools/music_check.py."""
    win = int(0.05 * SR)
    mixd = _decode(mp4, SR)
    end = int((total - 0.5) * SR)                   # the last 0.5 s is the music's fade-out
    mdb = _rms_db(mixd[:end], win)
    dead = [(round(a * 0.05, 2), round((b - a) * 0.05, 2)) for a, b in _runs(mdb < -50) if (b - a) * 0.05 > 0.25]
    vdb = _rms_db(voice[:end], win)
    bdb = _rms_db(bedstem[:end], win)
    pauses = [(a, b) for a, b in _runs(vdb < -45) if (b - a) * 0.05 > 0.25]
    under = [float(bdb[a:b].min()) for a, b in pauses]
    sys.path.insert(0, os.path.join(REPO, "tools"))
    import music_check
    lc = music_check.check(mp4, "bed")
    fails = [f for f in lc["fails"] if f in ("loudness", "true-peak", "clipping")]
    return dict(dead_air=dead, voice_pauses_over_250ms=len(pauses),
                bed_under_pauses_min_db=round(min(under), 1) if under else None,
                longest_voice_pause_s=round(max([(b - a) * 0.05 for a, b in pauses] or [0]), 2),
                lufs=lc["lufs"], true_peak=lc["true_peak"], clipped=lc["clipped"], hf_4_8k_pct=lc["hf_4_8k_pct"],
                hf_8k_pct=lc["hf_8k_pct"], loud_fails=fails,
                ok=not dead and not fails and (not under or min(under) > -50))


def check_reading(fps=FPS):
    """Every logged text: each continuous on-screen run must last >= 0.4 s/word + 0.6 s. Returns (rows, failures)."""
    rows, bad = [], []
    for k, frames in LOG.items():
        if not frames:
            continue
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


def check_contrast_report():
    low = {k: (round(v, 2), round(CONTRAST_AT.get(k, 0) / FPS, 2)) for k, v in CONTRAST.items() if v < MIN_CONTRAST}
    return dict(texts=len(CONTRAST), min=round(min(CONTRAST.values()), 2) if CONTRAST else None, low=low)


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


def finish(S, draw, cues, bed, amb="amb-room-tone.mp3", report_extra=None):
    out, voice, bedstem = render(S, draw, cues, bed=bed, amb=amb)
    rows, bad = check_reading()
    con = check_contrast_report()
    aud = check_audio(out, voice, bedstem, S.total)
    rep = dict(id=S.name, total=round(S.total, 2), captions=len(S.groups), pauses_lengthened=S.inserts, texts=len(rows),
               too_fast=bad, contrast=con, audio=aud, out=out)
    json.dump(dict(rep, rows=rows), open(f"{OUT}/{S.name}.qa.json", "w"), indent=1)
    sheet(out, [0.0, 0.5] + [S.gp(g) + 0.35 for g in range(0, len(S.groups), max(1, len(S.groups) // 22))] + [S.total - 0.5],
          f"{OUT}/{S.name}-sheet.jpg")
    print(json.dumps(rep))
    fails = []
    if bad:
        fails.append(f"READING: {bad}")
    if con["low"]:
        fails.append(f"CONTRAST: {con['low']}")
    if not aud["ok"]:
        fails.append(f"AUDIO: {aud}")
    if fails:
        sys.exit("QA FAILED: " + " | ".join(fails))
    return out

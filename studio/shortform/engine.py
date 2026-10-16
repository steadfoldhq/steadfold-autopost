"""Short-form studio engine: 9:16 voiced pilots with TikTok-style word-by-word captions."""
import json, math, os, subprocess, wave, struct
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
FD = "/usr/share/fonts/opentype/inter/"
AF = "/home/claude/steadfold-autopost/assets/fonts/"
_fc = {}
def font(name, size):
    k = (name, int(size))
    if k not in _fc:
        path = {"black": FD + "Inter-Black.otf", "xbold": FD + "Inter-ExtraBold.otf", "bold": FD + "Inter-Bold.otf",
                "semi": FD + "Inter-SemiBold.otf", "reg": FD + "Inter-Regular.otf",
                "dblack": FD + "InterDisplay-Black.otf", "brush": AF + "CaveatBrush-Regular.ttf",
                "poppins": "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf",
                "serif": "/home/claude/steadfold-autopost/assets/inbox/InstrumentSerif-Regular.ttf"}[name]
        if not os.path.exists(path):
            path = FD + "Inter-ExtraBold.otf"
        _fc[k] = ImageFont.truetype(path, int(size))
    return _fc[k]

def hexc(h, a=255):
    h = h.lstrip("#"); return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)

def ease(t): t = max(0, min(1, t)); return 1 - (1 - t) ** 3
def back(t):
    t = max(0, min(1, t)); c = 1.70158; return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2

# ---------- words from ElevenLabs alignment ----------
def words_from_alignment(j, offset=0.0):
    al = j.get("alignment") or j.get("normalized_alignment")
    ch, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    out, cur, s0, e0 = [], "", None, None
    for c, s, e in zip(ch, st, en):
        if c.isspace():
            if cur: out.append([cur, s0 + offset, e0 + offset]); cur = ""
            continue
        if not cur: s0 = s
        cur += c; e0 = e
    if cur: out.append([cur, s0 + offset, e0 + offset])
    return out

def audio_dur(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                       capture_output=True, text=True)
    return float(r.stdout.strip())

def build_voice(parts, out_wav, pauses=None, maxgap=0.42, lead=0.2, tail=0.9, between=0.3):
    """parts: list of (mp3, json). Long silences between words are trimmed to maxgap.
    pauses: {global_word_index: seconds} of silence inserted AFTER that word.
    Returns words with times on the final timeline and the total duration."""
    pauses = pauses or {}; sr = 44100
    out = [np.zeros(int(lead * sr), np.float32)]; t = lead; words = []; k = 0
    for pi, (mp3, js) in enumerate(parts):
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", mp3, "-f", "s16le", "-ac", "1", "-ar", str(sr), "-"],
                             capture_output=True, check=True).stdout
        a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
        ws = words_from_alignment(json.load(open(js)))
        pos = 0.0  # source position consumed
        for wi, w in enumerate(ws):
            s, e = w[1], w[2]
            nxt = ws[wi + 1][1] if wi + 1 < len(ws) else len(a) / sr
            # copy from pos to end of word (+ a natural gap up to maxgap)
            gap = nxt - e
            keep_to = e + min(gap, maxgap) if wi + 1 < len(ws) else min(len(a) / sr, e + 0.25)
            seg = a[int(pos * sr):int(keep_to * sr)]
            words.append([w[0], t + (s - pos), t + (e - pos)])
            out.append(seg); t += len(seg) / sr
            pos = max(keep_to, nxt - 0.06) if wi + 1 < len(ws) else len(a) / sr
            if gap > maxgap and wi + 1 < len(ws):
                # bring in a short fade-in pre-roll of the next word
                pre = a[int((nxt - 0.06) * sr):int(nxt * sr)]
                pos = nxt - 0.06
            g = pauses.get(k + wi)
            if g: out.append(np.zeros(int(g * sr), np.float32)); t += g
        k += len(ws)
        if pi < len(parts) - 1:
            out.append(np.zeros(int(between * sr), np.float32)); t += between
    out.append(np.zeros(int(tail * sr), np.float32))
    a = np.concatenate(out)
    with wave.open(out_wav, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())
    return words, len(a) / sr

def ping_track(times, total, out_wav, vol=0.10, kind="ping"):
    sr = 44100; a = np.zeros(int(total * sr) + sr, dtype=np.float32)
    for t0 in times:
        n = int(0.35 * sr); tt = np.arange(n) / sr
        if kind == "ping":
            s = (np.sin(2 * np.pi * 1318.5 * tt) * 0.6 + np.sin(2 * np.pi * 1975.5 * tt) * 0.25) * np.exp(-tt * 14)
        elif kind == "pop":
            s = np.sin(2 * np.pi * (520 - 300 * tt) * tt) * np.exp(-tt * 30)
        else:  # soft tick
            s = np.sin(2 * np.pi * 880 * tt) * np.exp(-tt * 40)
        s[: int(0.004 * sr)] *= np.linspace(0, 1, int(0.004 * sr))
        i = int(t0 * sr); a[i:i + n] += s[: len(a) - i] * vol
    with wave.open(out_wav, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())

# ---------- drawing helpers ----------
def text_size(d, s, f):
    b = d.textbbox((0, 0), s, font=f); return b[2] - b[0], b[3] - b[1], b[1]

def wrap(d, s, f, maxw):
    out, line = [], ""
    for w in s.split():
        t = (line + " " + w).strip()
        if text_size(d, t, f)[0] <= maxw: line = t
        else:
            if line: out.append(line)
            line = w
    if line: out.append(line)
    return out

def draw_center(img, s, y, f, fill, maxw=900, stroke=0, sfill=None, lh=1.12, alpha=255, x=W // 2):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    lines = wrap(d, s, f, maxw); hh = f.size * lh
    for i, ln in enumerate(lines):
        tw = text_size(d, ln, f)[0]
        d.text((x - tw / 2, y + i * hh), ln, font=f, fill=fill[:3] + (alpha,), stroke_width=stroke,
               stroke_fill=(sfill or (0, 0, 0, 255))[:3] + (alpha,))
    img.alpha_composite(layer)
    return y + len(lines) * hh

def rrect(img, box, r, fill, outline=None, width=0, shadow=None):
    if shadow:
        sx, sy, sc = shadow
        sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle(
            (box[0] + sx, box[1] + sy, box[2] + sx, box[3] + sy), r, fill=sc)
        img.alpha_composite(sh)
    l = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(l).rounded_rectangle(box, r, fill=fill, outline=outline, width=width)
    img.alpha_composite(l)

def paste_scaled(img, layer, s, cx, cy, alpha=1.0):
    """layer: RGBA full-frame image centred at (cx,cy) in its own coords; scale s about that point."""
    if s <= 0.01 or alpha <= 0.01: return
    if abs(s - 1) > 0.005:
        nw, nh = int(W * s), int(H * s)
        L = layer.resize((nw, nh), Image.BICUBIC)
        off = (int(cx - cx * s), int(cy - cy * s))
        tmp = Image.new("RGBA", img.size, (0, 0, 0, 0)); tmp.paste(L, off); layer = tmp
    if alpha < 1:
        a = layer.split()[3].point(lambda v: int(v * alpha)); layer.putalpha(a)
    img.alpha_composite(layer)

# ---------- captions ----------
def caption_groups(words, maxw=3, maxchars=16):
    groups, cur = [], []
    for i, w in enumerate(words):
        cur.append(i)
        txt = " ".join(words[j][0] for j in cur)
        end_punct = w[0][-1] in ".?!,:" 
        nxt_gap = (words[i + 1][1] - w[2]) if i + 1 < len(words) else 9
        if len(cur) >= maxw or len(txt) >= maxchars or end_punct or nxt_gap > 0.45:
            groups.append(cur); cur = []
    if cur: groups.append(cur)
    return groups

def draw_captions(img, t, words, groups, y=1180, accent=(255, 214, 59, 255), size=96, fill=(255, 255, 255, 255),
                  stroke=(14, 20, 64, 255), clean=lambda s: s):
    gi = None
    for k, g in enumerate(groups):
        st = words[g[0]][1] - 0.05; en = words[g[-1]][2] + 0.25
        if k + 1 < len(groups): en = min(en, words[groups[k + 1][0]][1] - 0.05)
        if st <= t < en: gi = k; break
    if gi is None: return
    g = groups[gi]
    f = font("black", size)
    d = ImageDraw.Draw(img)
    toks = [clean(words[j][0]) for j in g]
    toks = [x.upper() for x in toks]
    sp = size * 0.28
    widths = [text_size(d, x, f)[0] for x in toks]
    total = sum(widths) + sp * (len(toks) - 1)
    if total > 960:  # shrink to fit
        f = font("black", size * 960 / total); widths = [text_size(d, x, f)[0] for x in toks]
        sp = f.size * 0.28; total = sum(widths) + sp * (len(toks) - 1)
    pop = back((t - (words[g[0]][1] - 0.05)) / 0.18)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    x = W / 2 - total / 2
    for j, tok, wdt in zip(g, toks, widths):
        active = words[j][1] - 0.03 <= t
        col = accent if (active and t < words[j][2] + 0.15) else fill
        
        ld.text((x, y), tok, font=f, fill=col, stroke_width=max(6, int(f.size * 0.09)), stroke_fill=stroke)
        x += wdt + sp
    paste_scaled(img, layer, 0.85 + 0.15 * pop, W / 2, y + f.size / 2)

def find_word(words, needle, nth=0, after=0.0):
    c = 0
    for w in words:
        if w[1] < after: continue
        if needle.lower().strip(".,?!:") == w[0].lower().strip(".,?!:\u201c\u201d\"'"):
            if c == nth: return w[1]
            c += 1
    raise KeyError(needle)

# ---------- render ----------
def render(name, total, draw_frame, voice_wav, fx_wav, outdir, cover_t=0.0):
    os.makedirs(outdir, exist_ok=True)
    silent = f"{outdir}/{name}.video.mp4"
    n = int(total * FPS)
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                          "-pix_fmt", "yuv420p", silent], stdin=subprocess.PIPE)
    for i in range(n):
        im = draw_frame(i / FPS)
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait()
    out = f"{outdir}/{name}.mp4"
    inputs = ["-i", silent, "-i", voice_wav]; filt = "[1:a]apad,loudnorm=I=-15:TP=-1.5:LRA=7[v]"
    if fx_wav:
        inputs += ["-i", fx_wav]; filt += ";[v][2:a]amix=inputs=2:duration=first:normalize=0[a]"; amap = "[a]"
    else: amap = "[v]"
    subprocess.run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", filt, "-map", "0:v", "-map", amap,
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-t", f"{total:.3f}", "-movflags", "+faststart", out], check=True)
    os.remove(silent)
    return out

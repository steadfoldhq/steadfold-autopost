#!/usr/bin/env python3
"""Style menu (Oct 16 2026): shared engine for the 8 visual-language prototypes of one Locked Hour script.

Every style is an HTML page with an async `window.seek(t)` (rendered frame by frame by studio/motion/kit.py's
renderer, which awaits the promise), cut on the beat grid of its music track:

    B1 "You opened your phone to check one thing."          hook, fully on screen in frame 0
    B2 "40 minutes later…"
    B3 "Try this: phone in another room. One task. One hour."   starts ON the music's drop
    B4 "Your future self says thanks."

Block lengths are the reading minimum (0.4 s/word + 0.6 s) rounded UP to half beats, so every cut is on the grid and
B3 lands on the drop measured in tools/music-library.json. The one Laura voice take (media/voice/stylemenu) is split
at its pauses and each phrase is placed 0.12 s after its block starts. Music runs under everything (ducked under the
voice), SFX from media/music/library/v4/sfx land on the cuts.

    from common import Style
    st = Style(1, "storybook", track="lh-x-phone-down")
    st.build(css, body_html, js)          # -> OUT/Style-1-storybook.mp4 + QA sheet; frames deleted after encode
"""
import json
import math
import os
import shutil
import subprocess
import sys
from pathlib import Path

os.environ.setdefault("KIT_FRAME_EXT", "jpg")  # disk is tight
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "studio/motion"))
sys.path.insert(0, str(REPO / "tools"))
import kit  # noqa: E402
import numpy as np  # noqa: E402

OUT = Path(os.environ.get("STYLE_OUT", "/tmp/style-menu"))
CACHE = Path(os.environ.get("STYLE_CACHE", str(OUT / "_cache")))
LIB = json.load(open(REPO / "tools/music-library.json"))
VOICE = REPO / "media/voice/stylemenu/lh-stylemenu-t2.mp3"
VJSON = json.load(open(REPO / "media/voice/stylemenu/lh-stylemenu-t2.json"))
SFX = REPO / "media/music/library/v4/sfx"
SR = 44100
W, H, FPS = 1080, 1920, 30
INK, BUTTER, PINK, CREAM, PINK2 = "#141414", "#FFE27A", "#FF5CA8", "#FFF4E0", "#E8336F"

LINES = ["You opened your phone to check one thing.", "40 minutes later…",
         "Try this: phone in another room. One task. One hour.", "Your future self says thanks."]
NEED = [0.4 * len(s.split()) + 0.6 for s in LINES]   # 3.8, 1.8, 4.6, 2.6 s


def _vt(key, end=False):
    a = VJSON["alignment"]
    txt = "".join(a["characters"])
    i = txt.index(key)
    return a["character_end_times_seconds"][i + len(key) - 1] if end else a["character_start_times_seconds"][i]


# phrase starts in the take, and where the take is split (in the silences between phrases)
VP = dict(l1=_vt("You opened"), l2=_vt("Forty"), try_=_vt("Try this"), phone=_vt("phone in"), task=_vt("One task"),
          hour=_vt("One hour"), l4=_vt("Your future"))
VSPLIT = [0.0, (_vt("one thing.", True) + VP["l2"]) / 2, (_vt("later...", True) + VP["try_"]) / 2,
          (_vt("hour.", True) + VP["l4"]) / 2, None]


def timeline(track, lead=0.12):
    """Blocks, B3 item times, beat grid and voice placement for one track."""
    m = LIB["tracks"][track]
    bpm, drop = m["bpm"], m["drop_s"]
    beat = 60 / bpm
    hb = beat / 2
    # B3 also needs room for its last item ("One hour.", 2 words) to be read after it appears
    need = list(NEED)
    need[2] = max(NEED[2], (VP["hour"] - VP["try_"]) - 0.15 + 0.4 * 2 + 0.6 - 0.35)
    lens = [math.ceil(n / hb - 1e-6) * hb for n in need]
    starts = [0.0]
    for L in lens[:-1]:
        starts.append(starts[-1] + L)
    dur = starts[-1] + lens[-1]
    t_drop = starts[2]
    offset = drop - t_drop                     # where the video starts inside the track
    if offset < 0:
        raise ValueError(f"{track}: drop at {drop}s is too early for B3 at {t_drop:.2f}s")
    b3 = starts[2]
    sh = b3 + lead - VP["try_"]               # shift that puts "Try this" 0.12 s after the drop
    items = dict(try_=b3, phone=VP["phone"] + sh - 0.15, task=VP["task"] + sh - 0.15,
                 hour=min(VP["hour"] + sh - 0.15, starts[3] - (0.4 * 2 + 0.6)))
    beats = [t_drop + k * beat for k in range(-int(t_drop / beat) - 1, int((dur - t_drop) / beat) + 2)]
    beats = [round(b, 4) for b in beats if -1e-6 <= b <= dur]
    voice = []  # (take_from, take_to, place_at)
    anchors = [VP["l1"], VP["l2"], VP["try_"], VP["l4"]]
    for k in range(4):
        a0, a1 = VSPLIT[k], VSPLIT[k + 1]
        place = starts[k] + lead - (anchors[k] - a0) if k else 0.0
        voice.append((a0, a1, max(0.0, place)))
    return dict(track=track, bpm=bpm, beat=beat, drop=t_drop, offset=offset, dur=round(dur, 4),
                blocks=[dict(start=round(s, 4), end=round(s + L, 4), text=LINES[i]) for i, (s, L) in enumerate(zip(starts, lens))],
                items={k: round(v, 4) for k, v in items.items()}, beats=beats, voice=voice,
                drop_built=m.get("drop_built", False))


# ------------------------------------------------------------------------------------------- footage
def clip_frames(src, ss, dur, w=W, h=H, key=None, vf_extra="", fps=FPS, q=3):
    """Cover-crop a clip segment to w x h and dump it as JPG frames (cached). Returns (dir, n) for the page."""
    key = key or f"{Path(src).stem}_{ss}_{dur}_{w}x{h}{'_' + str(abs(hash(vf_extra)) % 10**6) if vf_extra else ''}"
    d = CACHE / key
    if not (d.exists() and any(d.iterdir())):
        d.mkdir(parents=True, exist_ok=True)
        vf = (f"scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h},fps={fps}"
              + (f",{vf_extra}" if vf_extra else ""))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-i", str(src), "-t", str(dur), "-vf", vf,
                        "-q:v", str(q), f"{d}/%04d.jpg"], check=True)
    n = len(list(d.glob("*.jpg")))
    return d, n


def inbox(name):
    return REPO / "assets/inbox" / name


def fluent(name):
    return (HERE / "assets/fluent3d" / f"{name}_3d.png").as_uri()


# ------------------------------------------------------------------------------------------- page
JS_LIB = r"""
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const lerp=(a,b,u)=>a+(b-a)*u;
const prog=(t,t0,d)=>clamp((t-t0)/d);
const E={
  out2:u=>1-(1-u)*(1-u), out3:u=>1-Math.pow(1-u,3), out5:u=>1-Math.pow(1-u,5), in3:u=>u*u*u,
  inOut:u=>u<.5?4*u*u*u:1-Math.pow(-2*u+2,3)/2, expo:u=>u>=1?1:1-Math.pow(2,-10*u),
  inExpo:u=>u<=0?0:Math.pow(2,10*u-10),
  back:(u,s=1.9)=>1+(s+1)*Math.pow(u-1,3)+s*Math.pow(u-1,2),
};
// damped spring 0 -> 1 (overshoots); f = Hz, z = damping ratio
function spring(t,t0,f=2.6,z=0.38){ if(t<=t0) return 0; const x=t-t0, w=2*Math.PI*f, wd=w*Math.sqrt(1-z*z);
  return 1-Math.exp(-z*w*x)*(Math.cos(wd*x)+z*w/wd*Math.sin(wd*x)); }
// a bounce landing: 0 at t0 (in the air) -> 1 landed, with decaying bounces; returns {y, squash}
function bounce(t,t0,fall=0.32,n=3){ if(t<=t0) return {y:0,sq:0,landed:false};
  const x=t-t0; if(x<fall){ const u=x/fall; return {y:u*u,sq:0,landed:false}; }
  let r=x-fall, h=0.18, d=fall*0.75;
  for(let i=0;i<n;i++){ if(r<d){ const u=r/d; const yy=1-h*4*u*(1-u); const sq=i===0&&u<0.18?(1-u/0.18):0; return {y:yy,sq:sq*(1-i*0.3),landed:true}; } r-=d; h*=0.35; d*=0.6; }
  return {y:1,sq:0,landed:true}; }
const $=id=>document.getElementById(id);
const $$=(sel,root=document)=>Array.from(root.querySelectorAll(sel));
function tf(el,{x=0,y=0,s=1,sx=null,sy=null,r=0,o=null,z=null}={}){ if(!el) return;
  el.style.transform=`translate(${x}px,${y}px) rotate(${r}deg) scale(${sx??s},${sy??s})`;
  if(o!==null) el.style.opacity=o; if(z!==null) el.style.zIndex=z; }
function vis(el,on){ if(el) el.style.visibility=on?'visible':'hidden'; }
// footage: <img data-clip="dir" data-n="N"> ; local time -> frame
const _pending=[];
function foot(img,lt,rate=1){ if(!img) return; const n=+img.dataset.n; let k=Math.floor(clamp(lt*rate*30,0,n-1))+1;
  const src=img.dataset.clip+'/'+String(k).padStart(4,'0')+'.jpg'; if(img._k!==k){ img._k=k; img.src=src; _pending.push(img.decode().catch(()=>{})); } }
async function flush(){ const p=_pending.splice(0); await Promise.all(p); }
// kinetic words: el contains span.w ; modes: pop | drop | up | stamp | slide
function kwords(el,t,t0,{gap=0.07,mode='pop',d=0.42,f=2.4,z=0.42}={}){ if(!el) return; $$('.w',el).forEach((w,i)=>{
  const s0=t0+i*gap; const u=spring(t,s0,f,z), p=prog(t,s0,0.12);
  if(t<s0){ w.style.opacity=0; return; } w.style.opacity=p;
  if(mode==='pop') w.style.transform=`translateY(${(1-u)*40}px) scale(${0.35+0.65*u})`;
  else if(mode==='drop') w.style.transform=`translateY(${(1-u)*-220}px) rotate(${(1-u)*-8}deg)`;
  else if(mode==='up') w.style.transform=`translateY(${(1-u)*90}px)`;
  else if(mode==='stamp') w.style.transform=`scale(${1+(1-u)*1.6}) rotate(${(1-u)*-6}deg)`;
  else if(mode==='slide') w.style.transform=`translateX(${(1-u)*-160}px) skewX(${(1-u)*-12}deg)`;
}); }
function shake(t,t0,d=0.35,amp=18){ if(t<t0||t>t0+d) return {x:0,y:0}; const k=1-(t-t0)/d;
  return {x:Math.sin((t-t0)*95)*amp*k, y:Math.cos((t-t0)*71)*amp*k*0.7}; }
// time since the latest beat (for pulses)
function sinceBeat(t){ let last=-9; for(const b of TL.beats){ if(b<=t) last=b; else break; } return t-last; }
function blockAt(t){ let k=0; TL.blocks.forEach((b,i)=>{ if(t>=b.start) k=i; }); return k; }
"""

EXTRA_FONTS = "".join(
    f"@font-face{{font-family:'{fam}';src:url('{(REPO / 'assets/fonts' / f).as_uri()}')}}"
    for fam, f in [("DM Serif Display", "DMSerifDisplay-Regular.ttf"), ("Gochi Hand", "GochiHand-Regular.ttf"),
                   ("Kalam", "Kalam-Bold.ttf"), ("Playfair Display", "PlayfairDisplay-Variable.ttf")])

BASE = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:var(--bg,#FFE27A)}
#stage{position:absolute;inset:0;overflow:hidden}
.abs{position:absolute}
.w{display:inline-block;will-change:transform}
.txt{position:absolute;left:0;width:1080px;padding:0 80px;text-align:center;font:900 92px/1.02 Inter;letter-spacing:-0.035em;color:#141414;
     text-shadow:0 6px 22px rgba(0,0,0,.16),0 2px 4px rgba(0,0,0,.10)}
.lt{color:#FFF8EA;text-shadow:0 4px 18px rgba(0,0,0,.42),0 2px 4px rgba(0,0,0,.30)}
.hl{background:linear-gradient(transparent 62%,rgba(255,92,168,.85) 62%,rgba(255,92,168,.85) 92%,transparent 92%);padding:0 .06em}
img{display:block}
"""


def words(text, cls="", em=()):
    """span.w per word; words in `em` get the .em class (the style decides what it looks like)."""
    out = []
    for w in text.split(" "):
        if w == "/":
            out.append("<br>")
            continue
        core = w.strip(".,:!?…").lower()
        out.append(f'<span class="w{" em" if core in em else ""}">{w}</span>')
    return f'<span class="{cls}">' + " ".join(out) + "</span>"


class Page:
    def __init__(self, rid, html, dur):
        self.rid, self._html, self.duration = rid, html, dur

    def html(self):
        return self._html


class Style:
    def __init__(self, n, name, track):
        self.n, self.name, self.track = n, name, track
        self.tl = timeline(track)
        self.rid = f"Style-{n}-{name}"
        self.dir = OUT / self.rid
        self.dir.mkdir(parents=True, exist_ok=True)
        self.sfx = []  # (time, file, gain_db)

    # ---------------------------------------------------------------- page
    def page(self, css, body, js, bg=BUTTER):
        return (f"<!doctype html><html><head><meta charset='utf-8'><style>{kit.FONTS}{EXTRA_FONTS}{BASE}"
                f":root{{--bg:{bg}}}{css}</style></head><body><div id='stage'>{body}</div>"
                f"<script>const TL={json.dumps(self.tl)};{JS_LIB}</script><script>{js}</script></body></html>")

    # ---------------------------------------------------------------- audio
    def add_sfx(self, t, name, gain_db=0.0):
        self.sfx.append((t, name, gain_db))

    def default_sfx(self, cut="sfx-x-swoosh-in", b4="sfx-x-whoosh-hit"):
        tl = self.tl
        b = tl["blocks"]
        if not tl["drop_built"]:
            self.add_sfx(tl["drop"] - 1.83, "sfx-x-riser", -9)
        self.add_sfx(tl["drop"], "sfx-x-bass-drop", -4 if not tl["drop_built"] else -9)
        self.add_sfx(tl["drop"] - 0.12, "sfx-x-whoosh-hit", -6)
        self.add_sfx(b[1]["start"] - 0.1, cut, -6)
        self.add_sfx(b[3]["start"] - 0.1, b4, -8)

    def mix(self, out_wav):
        tl = self.tl
        n = int(round(tl["dur"] * SR))
        dec = lambda p: kit_decode(p)  # noqa: E731
        music = dec(LIB["tracks"][self.track]["file"] if os.path.isabs(LIB["tracks"][self.track]["file"])
                    else REPO / LIB["tracks"][self.track]["file"])
        o = int(tl["offset"] * SR)
        m = music[o:o + n]
        if len(m) < n:
            m = np.r_[m, np.zeros((n - len(m), 2), np.float32)]
        v = np.zeros((n, 2), np.float32)
        take = dec(VOICE)
        for a0, a1, at in tl["voice"]:
            seg = take[int(a0 * SR): int(a1 * SR) if a1 else len(take)]
            k = int(at * SR)
            seg = seg[: max(0, n - k)]
            v[k:k + len(seg)] += seg
        # voice to about -16 LUFS-ish level relative to music; duck the music under it (smooth envelope)
        env = np.sqrt(np.convolve((v ** 2).mean(1), np.ones(int(0.05 * SR)) / int(0.05 * SR), "same"))
        on = np.clip(env / (np.percentile(env[env > 1e-4], 60) + 1e-9), 0, 1) if (env > 1e-4).any() else env * 0
        on = np.convolve(on, np.ones(int(0.12 * SR)) / int(0.12 * SR), "same")
        duck = 1 - 0.5 * on                      # about -6 dB under the voice
        mus_rms = np.sqrt((m ** 2).mean()) + 1e-9
        voice_rms = np.sqrt((v[np.abs(v).max(1) > 1e-3] ** 2).mean()) + 1e-9
        vg = (mus_rms * 1.9) / voice_rms         # voice sits ~5.6 dB over the bed
        mix = m * duck[:, None] + v * vg
        for t, name, g in self.sfx:
            s = dec(SFX / f"{name}.mp3") * (10 ** (g / 20)) * mus_rms / 0.12
            k = int(max(0, t) * SR)
            s = s[: max(0, n - k)]
            mix[k:k + len(s)] += s
        f = int(0.45 * SR)
        mix[-f:] *= np.linspace(1, 0.15, f)[:, None]  # gentle tail, never silence
        mix /= max(1.0, np.abs(mix).max() / 0.95)
        # tame the top (voice sibilance + bright SFX): music_check --kind mix wants < 0.5 % above 8 kHz
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-af",
                        "highshelf=f=6500:g=-5,lowpass=f=8800,lowpass=f=8800", str(out_wav)],
                       input=mix.astype("<f4").tobytes(), check=True)

    # ---------------------------------------------------------------- build
    def build(self, css, body, js, bg=BUTTER, workers=2, dsf=2, keep_frames=False, only=None):
        html = self.page(css, body, js, bg)
        page = Page(self.rid, html, self.tl["dur"])
        (self.dir / f"{self.rid}.html").write_text(html)
        fdir, n = kit.render_frames(page, self.dir, dsf=dsf, workers=workers, only=only)
        if only is not None:
            return fdir
        silent = self.dir / f"{self.rid}.silent.mp4"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", f"{fdir}/%05d.{kit.FRAME_EXT}",
                        "-frames:v", str(n), "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-maxrate", "10M",
                        "-bufsize", "20M", "-pix_fmt", "yuv420p", "-profile:v", "high", "-g", "30", str(silent)], check=True)
        wav = self.dir / f"{self.rid}.wav"
        self.mix(wav)
        out = OUT / f"{self.rid}.mp4"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(silent), "-i", str(wav), "-map", "0:v", "-map", "1:a",
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-shortest", "-movflags", "+faststart",
                        str(out)], check=True)
        silent.unlink()
        wav.unlink()
        kit.master_audio(out)
        self.qa(fdir, out)
        if not keep_frames:
            shutil.rmtree(fdir)
        return out

    def remix(self):
        """Rebuild only the sound of an already rendered prototype (same picture)."""
        out = OUT / f"{self.rid}.mp4"
        wav = self.dir / f"{self.rid}.wav"
        self.mix(wav)
        tmp = self.dir / "remix.mp4"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(out), "-i", str(wav), "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                        "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-shortest", "-movflags", "+faststart", str(tmp)], check=True)
        tmp.replace(out)
        wav.unlink()
        kit.master_audio(out)
        r = subprocess.run([sys.executable, str(REPO / "tools/music_check.py"), str(out), "--kind", "mix"], capture_output=True, text=True)
        (self.dir / "mix-check.txt").write_text(r.stdout)
        print(r.stdout.strip())
        return out

    def qa(self, fdir, out):
        tl = self.tl
        ts = [0.0, 0.3] + [b["start"] + d for b in tl["blocks"][1:] for d in (-0.1, 0.0, 0.1, 0.35)]
        ts += [b["start"] + (b["end"] - b["start"]) * 0.6 for b in tl["blocks"]] + list(tl["items"].values())
        ts += [tl["dur"] - 0.05]
        ts = sorted(set(round(min(max(0, x), tl["dur"] - 1 / FPS), 3) for x in ts))
        kit.sheet(fdir, ts, self.dir / f"{self.rid}-qa.jpg", cols=8, scale=0.2)
        # hero frames for the 2x4 contact sheet
        for k, b in enumerate(tl["blocks"]):
            t = b["start"] + (b["end"] - b["start"]) * (0.7 if k != 2 else 0.85)
            src = Path(fdir) / f"{int(round(t * FPS)):05d}.{kit.FRAME_EXT}"
            if src.exists():
                shutil.copy(src, self.dir / f"hero-{k + 1}.jpg")
        r = subprocess.run([sys.executable, str(REPO / "tools/music_check.py"), str(out), "--kind", "mix"],
                           capture_output=True, text=True)
        (self.dir / "mix-check.txt").write_text(r.stdout)
        print(r.stdout.strip())
        print(json.dumps(kit.probe(out)))


def kit_decode(p):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, "<f4").reshape(-1, 2).copy()


if __name__ == "__main__":
    for tr in [t for t in LIB["tracks"] if LIB["tracks"][t]["drop_s"] > 6]:
        tl = timeline(tr)
        print(tr, tl["dur"], [(b["start"], b["end"]) for b in tl["blocks"]], tl["items"], round(tl["offset"], 2),
              [round(x[2], 2) for x in tl["voice"]])


# ------------------------------------------------------------------------------------------- tracking
def track(frame_dir, x, y, win=70, key=None):
    """Follow one point through a frame folder (Lucas-Kanade on good features around it, median motion).
    Returns [[x, y], ...] per frame in the frames' pixel space; cached as track-<x>-<y>.json in the folder."""
    import cv2
    cache = Path(frame_dir) / f"track-{x}-{y}.json"
    if cache.exists():
        return json.load(open(cache))
    files = sorted(Path(frame_dir).glob("*.jpg"))
    prev = cv2.cvtColor(cv2.imread(str(files[0])), cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(prev)
    mask[max(0, y - win):y + win, max(0, x - win):x + win] = 255
    pts = cv2.goodFeaturesToTrack(prev, 40, 0.01, 6, mask=mask)
    out, cx, cy = [[x, y]], float(x), float(y)
    for f in files[1:]:
        cur = cv2.cvtColor(cv2.imread(str(f)), cv2.COLOR_BGR2GRAY)
        if pts is None or len(pts) < 4:
            mask[:] = 0
            mask[int(max(0, cy - win)):int(cy + win), int(max(0, cx - win)):int(cx + win)] = 255
            pts = cv2.goodFeaturesToTrack(prev, 40, 0.01, 6, mask=mask)
        if pts is not None and len(pts):
            nxt, st, _ = cv2.calcOpticalFlowPyrLK(prev, cur, pts, None, winSize=(31, 31), maxLevel=3)
            good = st.reshape(-1) == 1
            if good.sum() >= 3:
                d = np.median((nxt[good] - pts[good]).reshape(-1, 2), axis=0)
                cx, cy = cx + float(d[0]), cy + float(d[1])
                pts = nxt[good].reshape(-1, 1, 2)
        out.append([round(cx, 1), round(cy, 1)])
        prev = cur
    # light smoothing (3-frame) so doodles don't jitter
    a = np.array(out)
    k = np.ones(5) / 5
    sm = np.c_[np.convolve(np.pad(a[:, 0], 2, mode="edge"), k, "valid"), np.convolve(np.pad(a[:, 1], 2, mode="edge"), k, "valid")]
    res = [[round(float(p), 1), round(float(q), 1)] for p, q in sm]
    json.dump(res, open(cache, "w"))
    return res

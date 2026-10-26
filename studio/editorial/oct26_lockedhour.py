"""Locked Hour, Oct 26 studio build.

  python3 studio/editorial/oct26_lockedhour.py [head|wish|feed|oneword|stories|covers] [--keep]

Pieces (Toronto):
  lh-reel-1027am-head-start  Tue 27 08:30 (trial auto)  style: compare cards (original-template family), Inter Display hooks
  lh-1027-new-place          Tue 27 12:00               style: swipe to reveal (3 slides)
  lh-reel-1029-picture-win   Thu 29 19:00               style: calm text Reel (code-made sky paper, slow drift, static text)
  lh-oneword-04              Fri 30 17:00               One Word series layout (No. 3 'Space' candidate, relabelled No. 4)
  lh-st-1027/1028/1029-<n>   Stories, 2 frames a day, 12:30 / 12:31

Reuses the Oct 25 builder (studio/editorial/oct25_lockedhour.py) and the LH recovery kit it imports (60:00 ring, zine dot
grid, pills, Caveat lines, transitions, render + library-track scoring). No new music: existing LH v4 tracks only.
"""
import os, sys, json, shutil, subprocess
from pathlib import Path

SCR = Path(os.environ.get("LH_SCR", "/tmp/claude-0/-home-claude-steadfold-autopost/ff2300fc-7071-5e6e-ab73-de16719b794b/scratchpad/lh"))
SCR.mkdir(parents=True, exist_ok=True)
os.environ["LH_SCR"] = str(SCR)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import oct25_lockedhour as o25  # noqa: E402
from oct25_lockedhour import *  # noqa: E402,F401,F403
import edkit  # noqa: E402

REPO = Path("/home/claude/steadfold-autopost")
OUT = REPO / "media/studio-oct26/lockedhour"
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "stories").mkdir(exist_ok=True)

HCSS = (".H{font-family:'Inter Display',Inter,sans-serif;font-weight:900;color:#1B1717;letter-spacing:-.025em;line-height:1.04;text-align:center}"
        ".H .pill{border-radius:.3em;padding:0 .1em .03em}")


def Hd(text, field, size, align="center", extra=""):
    """Inter Display 900 hook (the LH v4 hook font) with highlighter pills under the words."""
    return edkit.dual(text, F[field], cls="H", style=f"font-size:{size}px;text-align:{align};{extra}")


# inject the hook class into every page the kit builds
_css0 = o25.css


def css2(W_, H_, field="dots"):
    return _css0(W_, H_, field) + HCSS


o25.css = css2
o25.reelkit.css = css2
o25.lhkit.css = css2
css = css2


# ------------------------------------------------------------------ objects
def stampcard(w, need, free=0, stamp_t=None, title="FREE WASH CARD", sub=None, done=0, ink_col=PINK):
    """Zine loyalty card: `need` circles, the first `free` pre-stamped (pop in at stamp_t[i] if given)."""
    cols = 5
    gap = w * 0.035
    cell = (w - w * 0.12 - gap * (cols - 1)) / cols
    rows = (need + cols - 1) // cols
    h = w * 0.22 + rows * (cell + gap) + w * 0.06
    dots = ""
    for i in range(need):
        r, c = divmod(i, cols)
        x = w * 0.06 + c * (cell + gap); y = w * 0.20 + r * (cell + gap)
        filled = i < free or i < done
        inner = ""
        if filled:
            tin = f"data-in='{stamp_t[i]}' data-k='pop'" if stamp_t and i < len(stamp_t) else ""
            inner = (f"<div {tin} style='position:absolute;inset:-4px;border-radius:50%;background:{ink_col};border:5px solid {INK};"
                     f"transform:rotate(-12deg);display:flex;align-items:center;justify-content:center;"
                     f"font:900 {cell*0.5:.0f}px/1 Inter Display,Inter;color:{INK}'>✓</div>")
        dots += (f"<div style='position:absolute;left:{x:.0f}px;top:{y:.0f}px;width:{cell:.0f}px;height:{cell:.0f}px;border-radius:50%;"
                 f"border:5px dashed rgba(27,23,23,.45);background:#FFFDF6'>{inner}</div>")
    sub_html = (f"<div class='mono' style='position:absolute;right:{w*0.06:.0f}px;top:{w*0.07:.0f}px;font-size:{w*0.045:.0f}px;"
                f"font-weight:700'>{sub}</div>") if sub else ""
    return (f"<div style='position:relative;width:{w}px;height:{h:.0f}px;background:#FFFDF6;border:6px solid {INK};border-radius:{w*0.05:.0f}px;"
            f"box-shadow:12px 12px 0 {INK}'>"
            f"<div style='position:absolute;left:{w*0.06:.0f}px;top:{w*0.06:.0f}px;font:900 {w*0.06:.0f}px/1 Inter Display,Inter;"
            f"letter-spacing:.08em;color:{INK}'>{title}</div>{sub_html}{dots}</div>")


def bar(w, frac_to, t0, label, col, h=86, fs=40):
    """Horizontal result bar that grows to frac_to (0..1 of w) with a rolling % label."""
    pct = round(frac_to * 100)
    return (f"<div style='position:relative;width:{w}px;height:{h}px;border:5px solid {INK};border-radius:16px;background:#FFFDF6'>"
            f"<div data-grow='{t0},0.7,0,{w*frac_to:.0f}' style='position:absolute;left:0;top:0;bottom:0;width:0;background:{col};"
            f"border-radius:10px 0 0 10px'></div>"
            f"<div style='position:absolute;z-index:2;left:22px;top:0;line-height:{h-10}px;font:800 {fs}px Inter Display,Inter;color:{INK}'>{label} "
            f"<span data-roll='{t0},0.7,0,{pct}' data-suf='%'>0%</span></div></div>")


def todo(w, items, t0=0.3, step=0.45):
    """Lined note card list; (text, ticked) items; ticks pop in order."""
    rows = ""
    k = 0
    for txt, ticked in items:
        box = (f"<div style='position:relative;width:62px;height:62px;border:5px solid {INK};border-radius:12px;background:#FFFDF6;flex:none'>"
               + (f"<div data-in='{t0 + k*step}' data-k='pop' style='position:absolute;inset:-14px -18px -6px -6px;"
                  f"font:900 80px/1 Inter Display,Inter;color:{DPINK}'>✓</div>" if ticked else "") + "</div>")
        if ticked:
            k += 1
        rows += (f"<div style='display:flex;align-items:center;gap:30px;height:110px;border-bottom:3px solid rgba(70,120,200,.35)'>{box}"
                 f"<div class='hand' style='font-size:66px;color:{INK};text-align:left;{'' if not ticked else ''}'>{txt}</div></div>")
    return (f"<div style='position:relative;width:{w}px;background:#FFFDF6;border:5px solid {INK};border-radius:14px;box-shadow:12px 12px 0 {INK};"
            f"padding:40px 50px 30px 120px;transform:rotate(-1.5deg)'>"
            f"<div style='position:absolute;left:84px;top:0;bottom:0;width:4px;background:#E8605A;opacity:.7'></div>"
            f"<div style='position:absolute;left:50%;top:-30px;width:220px;height:56px;margin-left:-110px;background:rgba(255,212,59,.75);"
            f"transform:rotate(-3deg);border:2px solid rgba(27,23,23,.2)'></div>{rows}</div>")


# ------------------------------------------------------------------ REEL A: HEAD START (Tue 27 08:30, trial)
HEAD_HOOK = "A head start / makes you / *finish.*"


def head():
    hook = lambda t=0: at(90, 290, Hd(HEAD_HOOK, "cream", 146), t, w=900)
    card0 = lambda st=None: at(150, 810, stampcard(780, 10, 2, st, sub="10 STAMPS"), 0, w=780)
    sc = [
        scene(0, 2.6, "cream", hook() + card0([0.25, 0.6]) +
              at(90, 1345, hand("2 stamps, free", 76), 0.9, "pop", w=900)),
        scene(2.6, 6.2, "pink",
              at(90, 280, Hd("Both cards: / *8 washes to go.*", "pink", 108), 0, w=900) +
              at(70, 560, stampcard(450, 8, 0, title="CARD A", sub="8 STAMPS"), 0.0, "left", w=450) +
              at(560, 560, stampcard(450, 10, 2, title="CARD B", sub="10 STAMPS"), 0.15, "left", w=450) +
              at(70, 880, f"<div class='S' style='font-size:58px;line-height:1.02'>Card A:<br>8 stamps,<br>none free</div>", 0.0, w=450) +
              at(560, 880, f"<div class='S' style='font-size:58px;line-height:1.02'>Card B:<br>10 stamps,<br><span class='pill' style='background:{F['pink']['p1']}'>2 already free</span></div>", 0.15, w=450) +
              at(70, 1085, bar(940, 0.19, 0.4, "Card A finished:", YEL, 104, 48), 0.3, "up", w=940) +
              at(70, 1210, bar(940, 0.34, 0.6, "Card B finished:", PINK, 104, 48), 0.4, "up", w=940) +
              at(90, 1340, hand("almost twice as many finished", 80), 1.2, "pop", w=900) +
              at(90, 1460, mono("Nunes &amp; Drèze 2006 · 300 loyalty cards"), 0.5, w=900),
              "slam"),
        scene(6.2, 9.8, "dots",
              at(90, 290, "<div class='dothis' style='font-size:130px;text-align:center'>Do this:</div>", 0, w=900) +
              at(90, 470, Hd("Start your list with / *2 done things.*", "dots", 96), 0, w=900) +
              at(150, 760, todo(780, [("made coffee", True), ("replied to Sam", True), ("write the report", False)], 0.6, 0.45), 0.25, "drop", w=780) +
              at(90, 1230, hand("the rest of the list feels shorter", 66), 1.7, "up", w=900), "push"),
        scene(9.8, 12.6, "cream", hook() + card0() +
              at(90, 1355, hand(o25.FOLLOW_HAND.replace(" / ", "<br>"), 58), 0.3, "up", w=900) +
              stampx(850, 1170, 0.5, 150), "plate"),
    ]
    cov = (at(90, 290, Hd(HEAD_HOOK, "cream", 146), 0, w=900) +
           at(100, 820, stampcard(420, 8, 0, title="CARD A", sub="8 STAMPS"), 0, w=420) +
           at(560, 820, stampcard(420, 10, 2, title="CARD B", sub="10 STAMPS"), 0, w=420) +
           at(90, 1180, hand("both 8 to go. card B came with 2 free.", 62), 0, w=900) +
           stampx(830, 1430, 0, 150))
    return sc, 12.6, cov, "cream", "lh-x-lock-in", 6.2


# ------------------------------------------------------------------ REEL B: PICTURE THE WIN (Thu 29 19:00), calm text
SKY = ("<div class='sky' style='position:absolute;inset:-120px;background:"
       "radial-gradient(ellipse 60% 40% at 30% 30%,rgba(255,255,255,.75),rgba(255,255,255,0) 70%),"
       "radial-gradient(ellipse 50% 35% at 75% 65%,rgba(255,186,214,.55),rgba(255,186,214,0) 70%),"
       "linear-gradient(180deg,#FFF6E5 0%,#FFEFC2 55%,#FFE0EC 100%)' data-drift='1'></div>")

JS_DRIFT = r"""
function seek3(t){ document.querySelectorAll('[data-drift]').forEach(el=>{ el.style.transform=`translate(${Math.sin(t*0.35)*40}px,${-t*6}px) scale(1.06)`; });
 document.querySelectorAll('.sc').forEach(s=>{ if(s.style.display!=='block') return; const lt=t-(+s.dataset.a);
  s.querySelectorAll('[data-batt]').forEach(el=>{ const [t0,d,f0,f1]=el.dataset.batt.split(',').map(Number);
    const q=Math.max(0,Math.min(1,(lt-t0)/d)); const e=q<.5?2*q*q:1-Math.pow(-2*q+2,2)/2; const f=f0+(f1-f0)*e;
    el.style.width=(f*100)+'%'; el.style.background=f<0.35?'#E0306C':(f<0.6?'#FFD43B':'#7BD389'); });
 }); }
"""


def battery(w, batt, static=None):
    if static is not None:
        col = '#E0306C' if static < 0.35 else ('#FFD43B' if static < 0.6 else '#7BD389')
        return battery(w, batt).replace("width:90%;border-radius", f"width:{static*100:.0f}%;border-radius").replace("background:#7BD389'></div></div>", f"background:{col}'></div></div>")
    return (f"<div style='position:relative;width:{w}px;height:{w*0.42:.0f}px'>"
            f"<div style='position:absolute;left:0;top:0;width:{w*0.92:.0f}px;height:100%;border:8px solid {INK};border-radius:{w*0.07:.0f}px;"
            f"background:#FFFDF6;padding:{w*0.03:.0f}px'><div data-batt='{batt}' style='height:100%;width:90%;border-radius:{w*0.04:.0f}px;"
            f"background:#7BD389'></div></div>"
            f"<div style='position:absolute;right:0;top:30%;width:{w*0.06:.0f}px;height:40%;background:{INK};border-radius:0 10px 10px 0'></div></div>")


def cloud(w, inner):
    return (f"<div style='position:relative;width:{w}px;height:{w*0.62:.0f}px'>"
            f"<div style='position:absolute;inset:0;background:#FFFDF6;border:6px solid {INK};border-radius:{w*0.31:.0f}px;box-shadow:10px 10px 0 {INK}'></div>"
            f"<div style='position:absolute;left:{w*0.12:.0f}px;bottom:-{w*0.12:.0f}px;width:{w*0.12:.0f}px;height:{w*0.12:.0f}px;border-radius:50%;"
            f"background:#FFFDF6;border:5px solid {INK}'></div>"
            f"<div style='position:absolute;left:{w*0.04:.0f}px;bottom:-{w*0.24:.0f}px;width:{w*0.07:.0f}px;height:{w*0.07:.0f}px;border-radius:50%;"
            f"background:#FFFDF6;border:4px solid {INK}'></div>"
            f"<div style='position:absolute;inset:0;display:flex;align-items:center;justify-content:center'>{inner}</div></div>")


def calm_scene(a, b, body, tr="cut"):
    return (f"<div class='sc' data-a='{a}' data-b='{b}' data-tr='{tr}' style='position:absolute;inset:0;display:none;background:#FFF6E5'>"
            f"{SKY}<div class='cam' style='position:absolute;inset:0;transform-origin:50% 45%'>{body}</div><div class='grain'></div></div>")


TROPHY = ("<svg width='{w}' height='{w}' viewBox='0 0 200 200' style='overflow:visible'>"
          "<path d='M62 34 H138 V78 C138 104 120 120 100 120 C80 120 62 104 62 78 Z' fill='#FF5CA8' stroke='#1B1717' stroke-width='8' stroke-linejoin='round'/>"
          "<path d='M62 46 C30 46 30 92 66 92 M138 46 C170 46 170 92 134 92' fill='none' stroke='#1B1717' stroke-width='8' stroke-linecap='round'/>"
          "<path d='M100 120 V146' stroke='#1B1717' stroke-width='10'/>"
          "<rect x='70' y='146' width='60' height='22' rx='6' fill='#FFE27A' stroke='#1B1717' stroke-width='8'/>"
          "<path d='M82 52 C80 66 82 80 90 92' fill='none' stroke='#FFFDF6' stroke-width='7' stroke-linecap='round' opacity='.85'/></svg>")


def trophy(w):
    return TROPHY.replace("{w}", str(w))


WISH_HOOK = "Daydreaming / the goal? / You may *do less.*"


def wcard():
    return (f"<div class='card' style='position:relative;padding:34px 40px'>"
                   f"<div class='S' style='font-size:64px;text-align:left;line-height:1.15'>"
                   f"<b style='font-family:Inter Display;font-weight:900;font-size:46px;letter-spacing:.1em'>WISH</b>&nbsp; finish the report<br>"
                   f"<b style='font-family:Inter Display;font-weight:900;font-size:46px;letter-spacing:.1em'>IN THE WAY</b>&nbsp; I keep checking email<br>"
                   f"<b style='font-family:Inter Display;font-weight:900;font-size:46px;letter-spacing:.1em'>PLAN</b>&nbsp; <span class='pill' style='background:{F['cream']['p1']}'>if I open email,</span><br>"
                   f"<span class='pill' style='background:{F['cream']['p2']}'>I close it and keep going</span></div></div>")


def wish():
    hookS = lambda: at(90, 300, D(WISH_HOOK, "cream", 128), 0, w=900)
    sc = [
        calm_scene(0, 2.9, hookS() +
                   at(150, 760, cloud(470, trophy(240)), 0, w=470) +
                   at(640, 1010, battery(280, "0.2,2.4,0.95,0.3"), 0, w=280) +
                   at(600, 1170, hand("energy", 60), 0, w=360)),
        calm_scene(2.9, 6.6,
                   at(90, 300, D("People who pictured / an ideal week / *said they did less.*", "cream", 112), 0, w=900) +
                   at(140, 830, chip("less energy right away", "#FFFDF6", 56, -2), 0.5, "drop") +
                   at(300, 970, chip("less done a week later", F['cream']['p1'], 56, 2), 1.0, "drop") +
                   at(90, 1180, mono("Kappes &amp; Oettingen 2011 · 4 small experiments"), 0.4, w=900),
                   "iris"),
        calm_scene(6.6, 10.4,
                   at(90, 300, D("Then picture / *what's in the way.*", "cream", 128), 0, w=900) +
                   at(110, 690, wcard(), 0.2, "pop", w=860) +
                   at(90, 1240, hand("wish, obstacle, plan:<br>it helped people in 21 studies", 60), 1.4, "up", w=900), "push"),
        calm_scene(10.4, 13.2,
                   at(90, 300, "<div class='dothis' style='font-size:120px;text-align:center'>Do this:</div>", 0, w=900) +
                   at(90, 470, D("Write the wish, / *the obstacle,* / then your plan.", "cream", 110), 0, w=900) +
                   at(110, 860, wcard(), 0, w=860) +
                   at(90, 1300, hand(o25.FOLLOW_HAND.replace(" / ", "<br>"), 56), 0.5, "up", w=900) +
                   stampx(860, 1100, 0.4, 150), "plate"),
    ]
    cov = (hookS() + at(110, 760, cloud(540, trophy(270)), 0, w=540) +
           at(660, 1060, battery(300, "0,0.01,0.3,0.3", static=0.25), 0, w=300) + at(620, 1230, hand("your energy", 60), 0, w=360) +
           at(90, 1250, hand("daydream", 60), 0, w=420) + stampx(860, 1430, 0, 150))
    return sc, 13.2, cov, "cream", "lh-x-tick-boom", 9.5


# ------------------------------------------------------------------ render (kit render + drift + SFX-free score)
def build_html(scenes):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css2(W, H)}</style></head><body>"
            f"<div class='page'>{''.join(scenes)}</div><script>{o25.reelkit.JS}{o25.JS2}{JS_DRIFT}</script></body></html>")


def render(rid, scenes, dur, track, beat_t, out_mp4, keep=False):
    from playwright.sync_api import sync_playwright
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    fd = SCR / f"frames-{rid}"; shutil.rmtree(fd, ignore_errors=True); fd.mkdir(parents=True)
    hp = SCR / f"{rid}.html"; hp.write_text(build_html(scenes))
    n = int(round(dur * FPS))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg.goto("file://" + str(hp)); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
        for k in range(n):
            t = k / FPS + 1e-4
            pg.evaluate(f"seek({t});seek2({t});seek3({t})")
            pg.screenshot(path=str(fd / f"{k:05d}.jpg"), type="jpeg", quality=93)
        b.close()
    tr = o25.LIB[track]
    off = tr["drop_s"] - beat_t
    pre = ["-ss", f"{off:.3f}"] if off > 0 else []
    delay = f"adelay={int(-off*1000)}|{int(-off*1000)}," if off < 0 else ""
    aud = SCR / f"{rid}-a.m4a"
    subprocess.run(["ffmpeg", "-nostdin", "-y", "-v", "error", *pre, "-i", str(REPO / tr["file"]), "-vn", "-af",
                    f"{delay}apad,atrim=0:{dur},afade=t=in:d=0.05,afade=t=out:st={dur-0.9:.2f}:d=0.9,loudnorm=I=-14:TP=-1.5:LRA=11,alimiter=limit=0.75:level=false",
                    "-ar", "44100", "-ac", "2", "-c:a", "aac", "-b:a", "160k", str(aud)], check=True)
    subprocess.run(["ffmpeg", "-nostdin", "-y", "-v", "error", "-framerate", str(FPS), "-i", str(fd / "%05d.jpg"), "-i", str(aud),
                    "-vf", f"scale={W}:{H}:flags=lanczos,format=yuv420p", "-c:v", "libx264", "-profile:v", "high",
                    "-preset", "slow", "-crf", "20", "-r", str(FPS), "-threads", "1", "-c:a", "copy", "-shortest",
                    "-movflags", "+faststart", str(out_mp4)], check=True)
    if not keep:
        shutil.rmtree(fd); aud.unlink(); hp.unlink()


def cover(body, field, out_jpg, calm=False):
    bg = SKY.replace("data-drift='1'", "") if calm else f"<div class='field' style='background-color:{F[field]['bg']}'></div>"
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{css2(W, H)}</style></head><body><div class='page' "
            f"style='background:{F[field]['bg']}'>{bg}{body}<div class='grain'></div></div></body></html>")
    o25.shoot([html], [out_jpg], W, H)


SPECS = {"head": ("lh-reel-1027am-head-start", head, False), "wish": ("lh-reel-1029-picture-win", wish, True)}

if __name__ == "__main__":
    args = sys.argv[1:]
    keep = "--keep" in args
    which = [a for a in args if not a.startswith("--")] or ["head", "wish", "feed", "oneword", "stories"]
    covers_only = "covers" in which
    for k in which:
        if k == "feed":
            import oct26_lockedhour_feed as fd_; fd_.feed(); print("done feed"); continue
        if k == "oneword":
            import oct26_lockedhour_feed as fd_; fd_.oneword(); print("done oneword"); continue
        if k == "stories":
            import oct26_lockedhour_feed as fd_; fd_.stories(); print("done stories"); continue
        if k not in SPECS:
            continue
        rid, fn, calm = SPECS[k]
        sc, dur, cov, field, track, beat = fn()
        cover(cov, field, OUT / f"{rid}-cover.jpg", calm)
        if not covers_only:
            render(rid, sc, dur, track, beat, OUT / f"{rid}.mp4", keep)
        print("done", rid)

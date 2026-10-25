"""Locked Hour, Oct 25 studio build: 3 Reels (Mon-Wed 7 pm) + One Word No. 3 (Wed 5 pm).

Built on the LH recovery kit (studio/recovery-oct22/lockedhour/build/reelkit.py + lhkit.py; imported, not edited):
60:00 ring with keyhole, zine dot grid, pills, Caveat lines, slam/iris/wipe/push/plate transitions.
Frame-0 rule (Oct 25 orders): ONE hook line (<=6 words) + ONE object, nothing else (no stamp, no handwritten line).

  python3 studio/editorial/oct25_lockedhour.py [grey|print|aloud|oneword|covers] [--keep]
Music: existing LH v4 tracks from tools/music-library.json (no new music), -14 LUFS, drop aligned to the "Do this" beat.
"""
import os, sys, json, shutil, subprocess
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
KIT = REPO / "studio/recovery-oct22/lockedhour/build"
sys.path.insert(0, str(KIT))
import reelkit  # noqa: E402
from reelkit import *  # noqa: E402,F401
import lhkit  # noqa: E402

SCR = Path(os.environ.get("LH_SCR", "/tmp/claude-0/-home-claude-steadfold-autopost/83b8b3af-3981-538b-bfe3-7c8459a8a782/scratchpad/lh"))
SCR.mkdir(parents=True, exist_ok=True)
reelkit.SCR = SCR
M = REPO / "media"
OUT = M / "studio-oct25/lockedhour"
OUT.mkdir(parents=True, exist_ok=True)
LIB = json.loads((REPO / "tools/music-library.json").read_text())["tracks"]


# ------------------------------------------------------------------ shoot (kit version has a hard-coded temp dir)
def shoot(html_pages, outs, W_, H_, q=92):
    import tempfile
    from playwright.sync_api import sync_playwright
    from PIL import Image
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W_, "height": H_}, device_scale_factor=2)
        for html, out in zip(html_pages, outs):
            tf = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, dir=str(SCR))
            tf.write(html); tf.close()
            pg.goto("file://" + tf.name); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            png = tf.name + ".png"; pg.screenshot(path=png)
            Image.open(png).convert("RGB").resize((W_, H_), Image.LANCZOS).save(out, quality=q, subsampling=0)
            os.unlink(png); os.unlink(tf.name)
        b.close()


lhkit.shoot = shoot
reelkit.shoot = shoot

# ------------------------------------------------------------------ extra motion (meaningful: colour drains, text scrolls, toggles flip)
JS2 = r"""
function seek2(t){
 document.querySelectorAll('.ovl').forEach(el=>{
  const p=el.dataset.ovl.split(','); const ty=p[0], tc=+p[1], d=0.2; const q=(t-(tc-d))/(2*d);
  if(q<0||q>1){el.style.display='none';return;} el.style.display='block';
  const E=x=>1-Math.pow(1-x,3);
  if(ty==='bar'){ const dir=+(p[2]||1); const x=-1800+q*(1080+1800); el.style.transform=dir>0?`translateX(${x}px) skewX(-12deg)`:`translateX(${1080-1700-x-1800+1080}px) skewX(12deg)`; }
  if(ty==='dot'){ const k=q<0.5?E(q*2):1-E((q-0.5)*2); el.style.transform=`translate(-50%,-50%) scale(${Math.max(0.001,k)})`; }
 });
 document.querySelectorAll('.sc').forEach(s=>{
  if(s.style.display!=='block') return; const lt=t-(+s.dataset.a);
  const E=x=>1-Math.pow(1-x,3), C=x=>Math.max(0,Math.min(1,x));
  s.querySelectorAll('[data-gray]').forEach(el=>{const [t0,d]=el.dataset.gray.split(',').map(Number);
    el.style.filter=`grayscale(${E(C((lt-t0)/d))})`;});
  s.querySelectorAll('[data-scroll]').forEach(el=>{const [t0,d,px]=el.dataset.scroll.split(',').map(Number);
    el.style.transform=`translateY(${-px*C((lt-t0)/d)}px)`;});
  s.querySelectorAll('[data-dim]').forEach(el=>{const [t0,d,o]=el.dataset.dim.split(',').map(Number);
    el.style.opacity=1-(1-o)*E(C((lt-t0)/d));});
  s.querySelectorAll('[data-flip]').forEach(el=>{const [t0,px]=el.dataset.flip.split(',').map(Number); const q=E(C((lt-t0)/0.25));
    el.querySelector('.knob').style.transform=`translateX(${px*q}px)`; el.style.background=q>0.5?'#E0306C':'#d8d2c4';});
  s.querySelectorAll('[data-wig]').forEach(el=>{const [t0]=el.dataset.wig.split(',').map(Number); const k=lt>t0?Math.sin((lt-t0)*22)*6*Math.exp(-(lt-t0)*1.2):0;
    el.style.transform=(el.dataset.b2||'')+` rotate(${k}deg)`;});
 });
}
"""


def build_html(scenes):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css(W, H)}</style></head><body>"
            f"<div class='page'>{''.join(scenes)}</div><script>{reelkit.JS}{JS2}</script></body></html>")


def render(rid, scenes, dur, track, beat_t, out_mp4, keep=False):
    """Kit render + seek2 + a library track with its measured drop placed on the 'Do this' beat."""
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
            pg.evaluate(f"seek({t});seek2({t})")
            pg.screenshot(path=str(fd / f"{k:05d}.jpg"), type="jpeg", quality=93)
        b.close()
    tr = LIB[track]
    src = REPO / tr["file"]
    off = tr["drop_s"] - beat_t
    pre = ["-ss", f"{off:.3f}"] if off > 0 else []
    delay = f"adelay={int(-off*1000)}|{int(-off*1000)}," if off < 0 else ""
    aud = SCR / f"{rid}-a.m4a"
    subprocess.run(["ffmpeg", "-nostdin", "-y", "-v", "error", *pre, "-i", str(src), "-vn", "-af",
                    f"{delay}apad,atrim=0:{dur},afade=t=in:d=0.05,afade=t=out:st={dur-0.9:.2f}:d=0.9,loudnorm=I=-14:TP=-1.5:LRA=11,alimiter=limit=0.75:level=false",
                    "-ar", "44100", "-ac", "2", "-c:a", "aac", "-b:a", "160k", str(aud)], check=True)
    subprocess.run(["ffmpeg", "-nostdin", "-y", "-v", "error", "-framerate", str(FPS), "-i", str(fd / "%05d.jpg"), "-i", str(aud),
                    "-vf", f"scale={W}:{H}:flags=lanczos,format=yuv420p", "-c:v", "libx264", "-profile:v", "high",
                    "-preset", "slow", "-crf", "20", "-r", str(FPS), "-threads", "1", "-c:a", "copy", "-shortest",
                    "-movflags", "+faststart", str(out_mp4)], check=True)
    if not keep:
        shutil.rmtree(fd); aud.unlink(); hp.unlink()


def cover(body, field, out_jpg):
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{css(W, H)}</style></head><body><div class='page' "
            f"style='background:{F[field]['bg']}'><div class='field' style='background-color:{F[field]['bg']}'></div>{body}"
            f"<div class='grain'></div></div></body></html>")
    shoot([html], [out_jpg], W, H)


# ------------------------------------------------------------------ helpers (same API as reels.py)
def D(text, field, size, align="center", extra=""):
    return dual(text, field, style=f"font-size:{size}px;text-align:{align};{extra}")


def at(x, y, inner, t=0, k="up", w=None, base=""):
    ww = f"width:{w}px;" if w else ""
    return (f"<div data-in='{t}' data-k='{k}' data-base='{base}' style='position:absolute;left:{x}px;top:{y}px;{ww}"
            f"transform:{base}'>{inner}</div>")


def hand(txt, size=64, color=None, align="center"):
    c = f"color:{color};" if color else ""
    return f"<div class='hand' style='font-size:{size}px;text-align:{align};{c}'>{txt}</div>"


def mono(txt, size=26, align="center"):
    return f"<div class='mono' style='font-size:{size}px;line-height:1.4;opacity:.85;text-align:{align}'>{txt}</div>"


def chip(txt, bg, size=46, rot=0):
    return (f"<div style='display:inline-block;background:{bg};border:4px solid {INK};border-radius:18px;padding:10px 22px;"
            f"box-shadow:7px 7px 0 {INK};font:800 {size}px/1.1 Inter Display,Inter,sans-serif;color:{INK};transform:rotate({rot}deg)'>{txt}</div>")


def stampx(x=820, y=1440, t=0.15, size=160):
    return at(x, y, stamp(0, 0, size, -12).replace("position:absolute;left:0px;top:0px;", "position:relative;"), t, "pop")


def dothis(lines, field, size=96, y=520, t=0.15):
    return (at(90, 300, "<div class='dothis' style='font-size:130px;text-align:center'>Do this:</div>", 0, w=900) +
            at(110, y, f"<div class='card' style='position:relative;padding:50px 44px'>{D(lines, field, size)}</div>", t, "pop", w=860))


APPCOLS = ["#FF5CA8", "#FFD43B", "#4DA3FF", "#3CC47C", "#FF8A3D", "#9B6BFF", "#FF4D4D", "#21C7C7",
           "#FFD43B", "#FF5CA8", "#3CC47C", "#4DA3FF", "#9B6BFF", "#FF8A3D", "#21C7C7", "#FF4D4D"]


def appphone(w, gray=None, badge=True):
    """Zine phone (cream body, ink border, hard shadow) with a grid of bright app tiles. gray='t0,d' drains the colour."""
    h = int(w * 1.9); pad = w * 0.09; tile = (w - 2 * pad - 3 * w * 0.06) / 4
    tiles = ""
    for i, c in enumerate(APPCOLS):
        r, cl_ = divmod(i, 4)
        x = pad + cl_ * (tile + w * 0.06); y = w * 0.30 + r * (tile + w * 0.09)
        dot = (f"<div style='position:absolute;right:-{tile*0.18:.0f}px;top:-{tile*0.18:.0f}px;width:{tile*0.42:.0f}px;height:{tile*0.42:.0f}px;"
               f"border-radius:50%;background:#FF2D2D;border:3px solid {INK}'></div>") if badge and i in (0, 5, 10) else ""
        tiles += (f"<div style='position:absolute;left:{x:.0f}px;top:{y:.0f}px;width:{tile:.0f}px;height:{tile:.0f}px;border-radius:{tile*0.26:.0f}px;"
                  f"background:{c};border:3px solid {INK}'>{dot}</div>")
    g = f"data-gray='{gray}'" if gray else ""
    flt = "" if gray else ""
    return (f"<div style='position:relative;width:{w}px;height:{h}px;background:#FFFDF6;border:7px solid {INK};border-radius:{w*0.15:.0f}px;"
            f"box-shadow:16px 16px 0 {INK}'>"
            f"<div style='position:absolute;left:50%;top:{w*0.05:.0f}px;transform:translateX(-50%);width:{w*0.28:.0f}px;height:{w*0.06:.0f}px;border-radius:99px;background:{INK}'></div>"
            f"<div class='mono' style='position:absolute;left:0;right:0;top:{w*0.12:.0f}px;text-align:center;font-size:{w*0.11:.0f}px;font-weight:700'>9:41</div>"
            f"<div {g} style='position:absolute;inset:0;{flt}'>{tiles}</div>"
            f"<div style='position:absolute;left:50%;bottom:{w*0.05:.0f}px;transform:translateX(-50%);width:{w*0.34:.0f}px;height:{w*0.03:.0f}px;border-radius:99px;background:{INK};opacity:.6'></div>"
            f"</div>")


def textphone(w, scroll=None):
    """Zine phone with lines of small text (reading on a screen). scroll='t0,d,px' scrolls the page up."""
    h = int(w * 1.9)
    lines = "".join(f"<div style='height:{w*0.035:.0f}px;margin:{w*0.045:.0f}px 0;border-radius:6px;background:{INK};opacity:.55;"
                    f"width:{[92,86,95,70,90,84,93,60,88,94,79,91,85,67,92,87,95,72,90,83][i%20]}%'></div>" for i in range(40))
    sc = f"data-scroll='{scroll}'" if scroll else ""
    return (f"<div style='position:relative;width:{w}px;height:{h}px;background:#FFFDF6;border:7px solid {INK};border-radius:{w*0.15:.0f}px;"
            f"box-shadow:16px 16px 0 {INK};overflow:hidden'>"
            f"<div style='position:absolute;left:50%;top:{w*0.05:.0f}px;transform:translateX(-50%);width:{w*0.28:.0f}px;height:{w*0.06:.0f}px;border-radius:99px;background:{INK};z-index:2'></div>"
            f"<div style='position:absolute;left:{w*0.1:.0f}px;right:{w*0.1:.0f}px;top:{w*0.2:.0f}px;bottom:{w*0.1:.0f}px;overflow:hidden'>"
            f"<div {sc}>{lines}</div></div></div>")


def sheet(w, hl_t=None, hl_rows=(2,), rows=11, spoken=False):
    """Printed page: white sheet, ink border, grey text lines; pink highlighter grows across hl_rows."""
    h = int(w * 1.32); out = ""
    for i in range(rows):
        wd = [92, 85, 95, 74, 90, 82, 94, 66, 88, 93, 78][i % 11]
        hl = ""
        if hl_t is not None and i in hl_rows:
            k = list(hl_rows).index(i)
            hl = (f"<div style='position:absolute;left:-8px;top:-10px;height:{w*0.075:.0f}px;width:0;background:{PINK};opacity:.75;border-radius:8px' "
                  f"data-grow='{hl_t + k*0.35},0.45,0,{w*0.8*wd/100+16:.0f}'></div>")
        mark = (f"<div class='hand' style='position:absolute;left:{w*0.8*wd/100+30:.0f}px;top:-30px;font-size:{w*0.12:.0f}px;line-height:1'>“”</div>"
                if spoken and i in hl_rows else "")
        out += (f"<div style='position:relative;height:{w*0.035:.0f}px;margin:{w*0.052:.0f}px 0;width:{w*0.8*wd/100:.0f}px'>{hl}"
                f"<div style='position:relative;height:100%;border-radius:6px;background:{INK};opacity:.6'></div>{mark}</div>")
    return (f"<div style='position:relative;width:{w}px;height:{h}px;background:#FFFFFF;border:6px solid {INK};border-radius:10px;"
            f"box-shadow:14px 14px 0 {INK};padding:{w*0.08:.0f}px {w*0.1:.0f}px'>{out}</div>")


def toggle(t0, label):
    return (f"<div style='display:flex;align-items:center;gap:26px'>"
            f"<div class='S' style='font-size:64px;text-align:left'>{label}</div>"
            f"<div data-flip='{t0},64' style='width:150px;height:86px;border-radius:99px;border:5px solid {INK};background:#d8d2c4;position:relative'>"
            f"<div class='knob' style='position:absolute;left:6px;top:6px;width:64px;height:64px;border-radius:50%;background:#FFFDF6;border:4px solid {INK}'></div></div></div>")


FOLLOW_HAND = "follow for one small focus fix a day, / each one backed by research"


def follow(y=1250, size=58, t=0.5):
    return at(90, y, hand(FOLLOW_HAND.replace(" / ", "<br>"), size), t, "up", w=900)


# ------------------------------------------------------------------ REEL 1: GREY PHONE (Mon 26)
def grey():
    hookD = lambda: at(90, 300, D("Turn your phone / *grey* tonight.", "pink", 168).replace("#FFE27A", "#CFC9C2"), 0, w=900)
    def phone_at(gray, t=0, k="up"):
        return at(320, 700, appphone(440, gray), t, k, w=440)
    sc = [
        scene(0, 2.3, "pink", hookD() + phone_at("0.25,1.6")),
        scene(2.3, 5.4, "cream",
              at(90, 300, D("A grey phone / is a *boring* phone.", "cream", 150), 0, w=900) +
              at(90, 700, anim_ring(420, 0.0, 1/3, 0.35, 1.2, centre="−20", sub="minutes a day", col=PINK, font=110), 0.2, "pop") +
              at(540, 760, hand("people spent about <br>20 minutes less <br>a day on it", 70, align="left"), 0.9, "pop", w=440) +
              at(90, 1230, mono("Dekker &amp; Baumgartner 2024 · 84 young adults · <br>phone use logged by an app, 1 week each way"), 0.4, w=900),
              "slam"),
        scene(5.4, 8.1, "dots",
              at(90, 300, D("You'll still pick it up. / You'll *put it down* / *sooner.*", "dots", 124), 0, w=900) +
              at(120, 760, chip("picked up: as often as before", "#FFFDF6", 50, -2), 0.3, "drop") +
              at(250, 900, chip("time on it: less", F['dots']['p1'], 58, 2), 0.7, "drop") +
              at(350, 1060, f"<div style='transform:scale(.62);transform-origin:50% 0'>{appphone(380, '0,0.01', badge=False)}</div>", 0.0, "up", w=380),
              "iris"),
        scene(8.1, 11.0, "pink",
              dothis("Turn on *Grayscale* / tonight.", "pink", 118, y=500) +
              at(140, 900, toggle(0.9, "Grayscale"), 0.5, "pop", w=800) +
              at(90, 1060, mono("iPhone: Settings › Accessibility ›<br>Display &amp; Text Size › Color Filters › Grayscale", 28), 0.6, w=900) +
              at(90, 1170, hand("Android: search “grayscale” in Settings", 58), 0.8, "up", w=900), "push"),
        scene(11.0, 13.6, "pink", hookD() + at(390, 680, f"<div style='transform:scale(.8);transform-origin:50% 0'>{appphone(380, '0,0.01')}</div>", 0, w=380) +
              follow(1290, 56, 0.3) + stampx(860, 1080, 0.5, 140), "plate"),
    ]
    cov = (at(90, 300, D("Turn your phone / *grey* tonight.", "pink", 168).replace("#FFE27A", "#CFC9C2"), 0, w=900) +
           at(220, 720, appphone(380, None), 0, w=380) +
           at(620, 860, f"<div style='filter:grayscale(1)'>{appphone(250, None, badge=False)}</div>", 0, w=250) +
           at(560, 790, hand("→", 110), 0, w=80) + stampx(820, 1440, 0, 150))
    return sc, 13.6, cov, "pink", "lh-x-phone-down", 8.1


# ------------------------------------------------------------------ REEL 2: PRINT IT (Tue 27, SEND TEST)
def printit():
    hook = at(90, 300, D("For whoever studies / on their *phone.*", "cream", 128), 0, w=900)
    sc = [
        scene(0, 2.3, "cream", hook + at(375, 690, textphone(330, "0.2,2.1,240"), 0, w=330) +
              at(90, 1360, hand("paper wins. here's when.", 74), 0, w=900)),
        scene(2.3, 5.4, "pink",
              at(90, 300, D("You understand / more *on paper.*", "pink", 140), 0, w=900) +
              at(300, 640, f"<div style='transform:rotate(-3deg)'>{sheet(470, hl_t=0.6, hl_rows=(2, 3))}</div>", 0.05, "drop", w=470) +
              at(90, 1310, mono("Delgado, Vargas, Ackerman &amp; Salmerón 2018 · <br>54 studies · 171,055 readers"), 0.4, w=900), "plate"),
        scene(5.4, 8.3, "dots",
              at(90, 300, D("Paper wins most / when you're *in a rush.*", "dots", 120), 0, w=900) +
              at(90, 700, anim_ring(380, 1.0, 0.2, 0.2, 2.2, centre="", sub="", col=PINK), 0.0, "pop") +
              at(90, 1085, f"<div style='width:380px'>{hand('time running out', 54)}</div>", 0.3, "pop", w=380) +
              at(510, 740, chip("textbooks ✓", "#FFFDF6", 50, -3), 0.5, "drop") +
              at(530, 880, chip("work docs ✓", F['dots']['p1'], 50, 2), 0.75, "drop") +
              at(90, 1230, hand("stories? no real difference.", 70), 1.3, "up", w=900), "cut"),
        scene(8.3, 11.0, "cream",
              dothis("Print the pages / you *must understand.*", "cream", 96, y=500, t=0) +
              at(90, 1000, hand("then read them with a pen in hand.", 64), 0.8, "up", w=900), "cut"),
        scene(11.0, 13.6, "pink",
              at(90, 300, D("*Send this* to whoever / studies on their phone.", "pink", 112), 0, w=900) +
              at(420, 650, f"<div style='transform:scale(.68);transform-origin:50% 0'>{textphone(360, '0,1,0')}</div>", 0.1, "pop", w=360) +
              follow(1180, 56, 0.6) + stampx(860, 1420, 0.5, 140), "cut"),
        # transitions as full covers: never two scenes' text on screen together
        f"<div class='ovl' data-ovl='bar,5.4,1' style='position:absolute;left:0;top:-120px;width:1800px;height:2160px;background:{PINK};"
        f"border-left:12px solid {INK};border-right:12px solid {INK};z-index:999;display:none'></div>",
        f"<div class='ovl' data-ovl='dot,8.3' style='position:absolute;left:540px;top:960px;width:2300px;height:2300px;border-radius:50%;"
        f"background:{BUTTER};border:14px solid {INK};z-index:999;display:none'></div>",
        f"<div class='ovl' data-ovl='bar,11.0,1' style='position:absolute;left:0;top:-120px;width:1800px;height:2160px;background:{CREAM};"
        f"border-left:12px solid {INK};border-right:12px solid {INK};z-index:999;display:none'></div>",
    ]
    cov = (hook + at(160, 700, textphone(330), 0, w=330) +
           at(540, 760, f"<div style='transform:rotate(4deg)'>{sheet(400, hl_t=-5, hl_rows=(2,))}</div>", 0, w=400) +
           at(90, 1390, hand("paper wins. here's when.", 70), 0, w=700) + stampx(830, 1420, 0, 150))
    return sc, 13.6, cov, "cream", "lh-x-tick-boom", 8.3


# ------------------------------------------------------------------ REEL 3: SAY IT OUT LOUD (Wed 28)
def megaphone(w, wig=None):
    wg = f"data-wig='{wig}' data-b2='rotate(-10deg)'" if wig else ""
    return f"<img class='obj' {wg} src='{obj('megaphone')}' style='width:{w}px;transform:rotate(-10deg)'>"


def aloud():
    hookD = at(90, 300, D("Need it to stick? / *Say it.*", "dots", 180), 0, w=900)
    waves = "".join(at(760 + i * 34, 860 - i * 50, f"<div style='width:{60+i*30}px;height:{140+i*90}px;border:9px solid {DPINK};"
                                                   f"border-left:none;border-top-color:transparent;border-bottom-color:transparent;border-radius:0 50% 50% 0'></div>",
                       0.25 + i * 0.18, "pop") for i in range(3))
    sc = [
        scene(0, 2.3, "dots", hookD + at(260, 760, megaphone(480, "0.15"), 0, w=480) + waves),
        scene(2.3, 5.4, "cream",
              at(90, 300, D("Words you *say out loud* / stick better than / words you *read silently.*", "cream", 112), 0, w=900) +
              at(130, 800, chip("said out loud", PINK, 62, -3), 0.3, "drop") +
              at(130, 940, f"<div data-dim='0.8,0.9,0.28'>{chip('read silently', '#FFFDF6', 62, 2)}</div>", 0.45, "drop") +
              at(640, 790, hand("remembered ✓", 66), 0.7, "pop", w=360) +
              at(640, 950, hand("faded", 66, color="#9a8f86"), 1.2, "pop", w=360) +
              at(90, 1260, mono("MacLeod, Gopie, Hourihan, Neary &amp; Ozubko 2010 · <br>8 experiments · the “production effect”"), 0.4, w=900),
              "slam"),
        scene(5.4, 8.3, "pink",
              at(90, 300, D("But only / *the key lines.*", "pink", 150), 0, w=900) +
              at(300, 640, sheet(480, hl_t=0.3, hl_rows=(3, 7), spoken=True), 0.05, "drop", w=480) +
              at(90, 1310, hand("say everything, and nothing stands out.", 62), 1.2, "up", w=900), "iris"),
        scene(8.3, 11.0, "dots",
              dothis("Read only the key lines / *out loud.*", "dots", 100, y=500) +
              at(90, 1000, hand("the rest: read as usual.", 66), 0.8, "up", w=900), "push"),
        scene(11.0, 13.6, "dots", hookD + at(330, 700, megaphone(380), 0, w=380) + follow(1230, 56, 0.3) + stampx(860, 1430, 0.5, 140), "plate"),
    ]
    cov = hookD.replace("data-in='0'", "data-in='0'") + at(240, 760, megaphone(480), 0, w=480) + \
        "".join(at(740 + i * 34, 860 - i * 50, f"<div style='width:{60+i*30}px;height:{140+i*90}px;border:9px solid {DPINK};"
                                              f"border-left:none;border-top-color:transparent;border-bottom-color:transparent;border-radius:0 50% 50% 0'></div>", 0)
                for i in range(3)) + stampx(820, 1440, 0, 150)
    return sc, 13.6, cov, "dots", "lh-x-lock-in", 8.3


# ------------------------------------------------------------------ ONE WORD No. 3: SPACE (same layout as No. 2, feed.py)
def oneword():
    sys.path.insert(0, str(KIT))
    import feed  # noqa  (reuse frame(); feed.OUT is untouched: we only call the layout helpers)
    frame = feed.frame
    FW, FH = 1080, 1350
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:30px;padding:12px 20px'>One Word · No. 3</span></div>
<div style='position:absolute;left:70px;right:70px;top:190px'>{dual("Cramming the night / *before* again?", style="font-size:124px;text-align:left")}</div>
<div style='position:absolute;left:60px;top:760px;width:960px;height:120px;background:{PINK};opacity:.85;border-radius:60px'></div>
<div class='S riso' style='position:absolute;left:40px;right:40px;top:540px;font-size:340px;text-align:left'>Space.</div>
<img class='obj' src='{obj("hourglass")}' style='position:absolute;left:770px;top:850px;width:200px;transform:rotate(8deg)'>
<div class='hand' style='position:absolute;left:90px;top:960px;font-size:60px;text-align:left'>same study time,<br>spread over days</div>
<div class='mono' style='position:absolute;left:90px;top:1150px;font-size:24px;opacity:.8'>one word that guards your focus</div>
""", "No. 3", "ONE WORD")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    on = {0: "20 min", 2: "20 min", 4: "20 min"}
    cells = ""
    for i, d in enumerate(days):
        x = 95 + i * 128
        lit = i in on
        cells += (f"<div style='position:absolute;left:{x}px;top:470px;width:112px;height:250px;border:5px solid {INK};border-radius:16px;"
                  f"background:{PINK if lit else '#FFFDF6'};box-shadow:{'8px 8px 0 ' + INK if lit else 'none'};opacity:{1 if lit else .75}'>"
                  f"<div style='font:800 34px/1 Inter Display,Inter;color:{INK};text-align:center;margin-top:22px'>{d}</div>"
                  + (f"<div class='mono' style='font-size:25px;font-weight:700;text-align:center;margin-top:70px;line-height:1.1'>20<br>min</div>" if lit else "")
                  + "</div>")
    s2 = frame(f"""
<div style='position:absolute;left:0;right:0;top:110px'>{dual("*3 short sessions.* / Not one long one.", style="font-size:124px")}</div>
{cells}
<div class='S' style='position:absolute;left:0;right:0;top:790px;font-size:70px'>Same hour. <span class='pill' style='background:{F['cream']['p1']}'>Spread out.</span></div>
<div class='hand' style='position:absolute;left:0;right:0;top:900px;font-size:50px'>20 + 20 + 20 minutes = the same hour.</div>
""", "No. 3", "ONE WORD")
    s3 = frame(f"""
<div style='position:absolute;left:0;right:0;top:130px'>{dual("*Remember more.*", style="font-size:160px")}</div>
<div class='S' style='position:absolute;left:90px;right:90px;top:350px;font-size:62px;line-height:1.05'>Across 317 experiments, spreading the same study time over days beat cramming it into one go.</div>
<div class='card' style='left:110px;right:110px;top:680px;padding:36px 40px'>
 <div class='dothis' style='font-size:76px;text-align:left'>Do this:</div>
 <div class='S' style='font-size:62px;text-align:left;line-height:1.02'>Split your next study hour into 3 short sessions. <span class='pill' style='background:{F['pink']['p1']}'>Put them in your calendar.</span></div></div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1110px;font-size:22px;opacity:.85;line-height:1.45'>Cepeda, Pashler, Vul, Wixted &amp; Rohrer 2006, Psychological Bulletin<br>review of 317 experiments (184 articles)</div>
""", "No. 3", "ONE WORD")
    d = OUT / "lh-oneword-03-space"; d.mkdir(exist_ok=True)
    shoot([page(s, FW, FH, f) for s, f in ((s1, "pink"), (s2, "cream"), (s3, "dots"))], [d / f"0{i+1}.jpg" for i in range(3)], FW, FH)


SPECS = {"grey": ("lh-reel-1028-grey-phone-r2", grey), "print": ("lh-reel-1026-print-it-r2", printit),
         "aloud": ("lh-reel-1028-say-it-aloud", aloud)}

if __name__ == "__main__":
    args = sys.argv[1:]
    keep = "--keep" in args
    which = [a for a in args if not a.startswith("--")] or ["grey", "print", "aloud", "oneword"]
    covers_only = "covers" in which
    for k in which:
        if k == "oneword":
            oneword(); print("done oneword"); continue
        if k not in SPECS:
            continue
        rid, fn = SPECS[k]
        sc, dur, cov, field, track, beat = fn()
        cover(cov, field, OUT / f"{rid}-cover.jpg")
        if not covers_only:
            render(rid, sc, dur, track, beat, OUT / f"{rid}.mp4", keep)
        print("done", rid)


def remux_audio(rid, key):
    """Re-score an already-rendered Reel (video stream copied) with the current audio chain."""
    sc, dur, cov, field, track, beat = SPECS[key][1]()
    tr = LIB[track]; off = tr["drop_s"] - beat
    pre = ["-ss", f"{off:.3f}"] if off > 0 else []
    delay = f"adelay={int(-off*1000)}|{int(-off*1000)}," if off < 0 else ""
    mp4 = OUT / f"{rid}.mp4"; tmp = SCR / f"{rid}-remux.mp4"
    subprocess.run(["ffmpeg", "-nostdin", "-y", "-v", "error", "-i", str(mp4), *pre, "-i", str(REPO / tr["file"]), "-map", "0:v", "-map", "1:a",
                    "-af", f"{delay}apad,atrim=0:{dur},afade=t=in:d=0.05,afade=t=out:st={dur-0.9:.2f}:d=0.9,"
                           "loudnorm=I=-14:TP=-1.5:LRA=11,alimiter=limit=0.75:level=false",
                    "-ar", "44100", "-ac", "2", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-t", f"{dur}",
                    "-movflags", "+faststart", str(tmp)], check=True)
    shutil.move(str(tmp), str(mp4))

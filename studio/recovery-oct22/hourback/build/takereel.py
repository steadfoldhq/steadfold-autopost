#!/usr/bin/env python3
"""Hourback "Take Two" Reel renderer (recovery Oct 22).

Brand v4 §12 editorial look (DM Serif Display ink #2A1D47, pills under words, halftone B/W phone object,
Caveat Brush note, round stamp, soft paper fields) + v0.5 "Take Two" grammar (payoff on frame 0, anticlockwise
rewind coin -> greyed TAKE 1 -> clapper -> TAKE 2 typed live -> answer card on the drop -> Do this -> loop).

HTML/CSS scene graph, a JS seek(t) per frame, Playwright screenshots at 30 fps, ffmpeg H.264 + AAC.
Usage: python3 takereel.py <name>   (names in REELS at the bottom of reels.py)
"""
import json, subprocess, sys, shutil, tempfile, math
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio" / "editorial"))
import edkit  # noqa: E402

W, H, FPS = 1080, 1920, 30
INK = "#2A1D47"
ACC = edkit.ACCENT["hourback"]
F = edkit.FIELDS["hourback"]
GREY_BG, GREY_INK = "#DCD8E6", "#5F5975"
SUN = "#FFC94D"

JS = r"""
const C=(x)=>Math.max(0,Math.min(1,x));
const E=(x)=>1-Math.pow(1-C(x),3);
const B=(x)=>{x=C(x);const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
function seek(t){
 document.querySelectorAll('[data-in]').forEach(el=>{
  const a=+el.dataset.in,b=+(el.dataset.out||999)+(el.dataset.hard?0:0.5),fx=el.dataset.fx||'none',d=+(el.dataset.d||0.32);
  if(t<a||t>=b){el.style.visibility='hidden';return}
  el.style.visibility='visible';
  const p=(t-a)/d; let o=1,tr='',f='none',clip='none';
  switch(fx){
   case 'pop': tr=`scale(${0.55+0.45*B(p)})`; o=C(p*3); break;
   case 'up': tr=`translateY(${(1-E(p))*140}px)`; o=C(p*2.5); break;
   case 'drop': tr=`translateY(${-(1-B(p))*260}px) rotate(${(1-E(p))*-4}deg)`; o=C(p*4); break;
   case 'whipL': tr=`translateX(${(1-E(p))*1200}px) skewX(${(1-E(p))*-12}deg)`; f=`blur(${(1-C(p))*22}px)`; break;
   case 'whipR': tr=`translateX(${-(1-E(p))*1200}px) skewX(${(1-E(p))*12}deg)`; f=`blur(${(1-C(p))*22}px)`; break;
   case 'slam': tr=`scale(${1+(1-E(p))*0.7}) rotate(${(1-E(p))*-7}deg)`; o=C(p*5); break;
   case 'zoom': tr=`scale(${1.4-0.4*E(p)})`; f=`blur(${(1-C(p))*12}px)`; o=C(p*3); break;
   case 'iris': clip=`circle(${E(p)*120}% at 50% 46%)`; break;
   case 'wipe': clip=`inset(0 0 0 ${(1-E(p))*100}%)`; break;
   case 'wipeD': clip=`inset(0 0 ${(1-E(p))*100}% 0)`; break;
   case 'spinin': tr=`rotate(${(1-E(p))*200}deg) scale(${0.3+0.7*B(p)})`; o=C(p*3); break;
  }
  const dr=+(el.dataset.drift||0); if(dr) tr+=` scale(${1+(t-a)*dr})`;
  const fl=+(el.dataset.float||0); if(fl) tr+=` translateY(${Math.sin((t-a)*2.2)*fl}px) rotate(${Math.sin((t-a)*1.7)*fl*0.08}deg)`;
  const sp=+(el.dataset.spin||0); if(sp) tr+=` rotate(${(t-a)*sp}deg)`;
  const pu=+(el.dataset.pulse||0); if(pu) tr+=` scale(${1+Math.sin((t-a)*6.5)*pu})`;
  el.style.opacity=o; el.style.transform=(el.dataset.base||'')+' '+tr; el.style.filter=f; el.style.clipPath=clip;
 });
 document.querySelectorAll('[data-type]').forEach(el=>{
  const a=+el.dataset.t0,b=+el.dataset.t1,s=el.dataset.type; const n=Math.round(s.length*C((t-a)/(b-a)));
  el.querySelector('.tx').textContent=s.slice(0,n);
  el.querySelector('.caret').style.opacity=(t<b+0.6 && Math.floor(t*3)%2==0)?1:0;
 });
 document.querySelectorAll('[data-roll]').forEach(el=>{
  const a=+el.dataset.t0,b=+el.dataset.t1,v0=+el.dataset.v0,v1=+el.dataset.v1;
  const v=Math.round(v0+(v1-v0)*E((t-a)/(b-a))); el.textContent=eval('`'+el.dataset.roll+'`');
 });
 document.querySelectorAll('.spk').forEach(e=>{e.style.transform=`rotate(${Math.sin(t*2.4)*14}deg) scale(${1+Math.sin(t*6.5)*0.08})`});
 // camera shake on impacts
 let sx=0,sy=0; (window.SHAKES||[]).forEach(s=>{const k=t-s; if(k>=0&&k<0.28){const a=(1-k/0.28)*14; sx+=Math.sin(k*90)*a; sy+=Math.cos(k*77)*a*0.6}});
 document.getElementById('cam').style.transform=`translate(${sx}px,${sy}px)`;
 // VHS rewind overlay
 document.querySelectorAll('.vhs').forEach(el=>{el.style.backgroundPosition=`0 ${(t*900)%40}px`;});
}
"""


def T(x, a, b=999, fx="none", d=0.32, extra="", base="", **kw):
    """Wrap html x in a timed absolutely positioned layer."""
    attrs = " ".join(f'data-{k}="{v}"' for k, v in kw.items())
    return f'<div data-in="{a}" data-out="{b}" data-fx="{fx}" data-d="{d}" data-base="{base}" {attrs} style="position:absolute;{extra}">{x}</div>'


def serif(text, size, f=F["plum"], ink=INK, width=900, align="center"):
    return edkit.dual(text, f, cls="S", style=f"font-size:{size}px;color:{ink};width:{width}px;text-align:{align}")


def hand(text, size=70, color=ACC, rot=-3, width=900):
    return f'<div class="hand" style="font-size:{size}px;color:{color};transform:rotate({rot}deg);width:{width}px">{text}</div>'


def tab(label, dim=False):
    ink = GREY_INK if dim else INK
    stripe = f"repeating-linear-gradient(-45deg,{ink} 0 18px,{'#EDEAF2' if dim else SUN} 18px 36px)"
    return (f'<div style="display:flex;align-items:center;gap:0;border:4px solid {ink};border-radius:14px;overflow:hidden;'
            f'box-shadow:6px 6px 0 {ink};background:#FFFDF8">'
            f'<div style="width:96px;height:62px;background:{stripe}"></div>'
            f'<div style="font:700 38px Poppins;letter-spacing:.06em;color:{ink};padding:6px 22px 2px">{label}</div></div>')


def coin(size=300, dim=False):
    """Yellow rewind coin, arrow runs ANTICLOCKWISE (Oct 11 logo rule)."""
    r, cx, cy = 27, 50, 50
    th_s, th_e = math.radians(-50), math.radians(20)
    sx, sy = cx + r * math.cos(th_s), cy + r * math.sin(th_s)
    ex, ey = cx + r * math.cos(th_e), cy + r * math.sin(th_e)
    tx, ty = math.sin(th_e), -math.cos(th_e)          # tangent for decreasing angle (anticlockwise on screen)
    nx, ny = math.cos(th_e), math.sin(th_e)
    tip = (ex + tx * 11, ey + ty * 11)
    b1 = (ex + nx * 9 - tx * 1, ey + ny * 9 - ty * 1)
    b2 = (ex - nx * 9 - tx * 1, ey - ny * 9 - ty * 1)
    ink = GREY_INK if dim else INK
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100"><circle cx="50" cy="50" r="46" fill="{SUN}" stroke="{ink}" stroke-width="4"/>'
            f'<path d="M{sx:.2f},{sy:.2f} A{r},{r} 0 1 0 {ex:.2f},{ey:.2f}" fill="none" stroke="{ink}" stroke-width="7" stroke-linecap="round"/>'
            f'<polygon points="{tip[0]:.2f},{tip[1]:.2f} {b1[0]:.2f},{b1[1]:.2f} {b2[0]:.2f},{b2[1]:.2f}" fill="{ink}"/></svg>')


def sparkle(size=120, fill=SUN):
    return (f'<svg class="spk" width="{size}" height="{size}" viewBox="0 0 100 100" style="vertical-align:-0.1em;display:inline-block">'
            f'<path d="M50 4 C55 34 66 45 96 50 C66 55 55 66 50 96 C45 66 34 55 4 50 C34 45 45 34 50 4Z" fill="{fill}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/></svg>')


def card(inner, w=900, pad=40, bg="#FFFDF8", ink=INK):
    return (f'<div style="width:{w}px;background:{bg};border:5px solid {ink};border-radius:30px;box-shadow:12px 12px 0 {ink};'
            f'padding:{pad}px;font-family:Inter;color:{ink}">{inner}</div>')


def chip(text, bg):
    return f'<span style="display:inline-block;background:{bg};border:3px solid {INK};border-radius:99px;padding:6px 22px;margin:0 10px 10px 0;font:700 32px Inter">{text}</span>'


def typed(text, a, b, size=42, label="one sentence:"):
    inner = (f'<div style="font:600 28px Inter;letter-spacing:.04em;color:#8E89A3;text-transform:uppercase;margin-bottom:14px">{label}</div>'
             f'<div style="font:500 {size}px/1.3 Inter;min-height:{int(size*1.3*3)}px"><span class="tx"></span><span class="caret" style="display:inline-block;width:4px;height:{size}px;background:{INK};vertical-align:-6px;margin-left:3px"></span></div>'
             f'<div style="display:flex;justify-content:flex-end;margin-top:8px"><div style="width:74px;height:74px;border-radius:50%;background:{ACC};color:#fff;font:800 44px Inter;display:flex;align-items:center;justify-content:center">↑</div></div>')
    return f'<div data-type="{text}" data-t0="{a}" data-t1="{b}">{card(inner, pad=36)}</div>'


def scene(bg, a, b, fx, inner, d=0.4, grey=False, drift=0.006):
    gr = "filter:saturate(.25);" if grey else ""
    return (f'<div data-in="{a}" data-out="{b}" data-fx="{fx}" data-d="{d}" style="position:absolute;inset:0;background:{bg};{gr}">'
            f'<div data-in="{a}" data-out="{b}" data-drift="{drift}" style="position:absolute;inset:0;transform-origin:50% 45%">{inner}</div>'
            f'<div class="grain"></div></div>')


def page(scenes, shakes):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{edkit.css('hourback', W, H)}
.vhs{{position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.18) 0 3px,rgba(0,0,0,0) 3px 20px,rgba(42,29,71,.10) 20px 23px,rgba(0,0,0,0) 23px 40px);mix-blend-mode:overlay}}
</style></head><body><div id="cam" style="position:absolute;inset:0;overflow:hidden">{''.join(scenes)}</div>
<script>window.SHAKES={json.dumps(shakes)};{JS}</script></body></html>"""


def rewind(a, b, label="TAKE 1"):
    inner = (T(coin(320), a, b, "spinin", 0.25, f"left:{540-160}px;top:{820-160}px", spin=-900) +
             T(tab(label, dim=True), a + 0.22, b, "slam", 0.18, "left:90px;top:300px") +
             T(hand("rewind", 84, GREY_INK, -4), a + 0.1, b, "pop", 0.2, "left:90px;top:1080px") +
             '<div class="vhs"></div>')
    return scene(GREY_BG, a, b, "zoom", inner, d=0.2, drift=0.02)


def clapper(a, b):
    stripe = f"repeating-linear-gradient(-45deg,{INK} 0 44px,{SUN} 44px 88px)"
    top = (f'<div style="width:760px;height:120px;background:{stripe};border:6px solid {INK};border-radius:16px;'
           f'transform-origin:20px 110px"></div>')
    body = (f'<div style="width:760px;height:330px;background:#FFFDF8;border:6px solid {INK};border-radius:20px;box-shadow:14px 14px 0 {INK};'
            f'display:flex;align-items:center;justify-content:center;font:700 120px Poppins;letter-spacing:.04em;color:{INK}">TAKE 2</div>')
    inner = (T(top, a, b, "none", extra=f"left:160px;top:{620}px", base="rotate(-24deg)") +
             T(top, a + 0.12, b, "none", extra=f"left:160px;top:{620}px") +
             T(body, a, b, "slam", 0.14, f"left:160px;top:760px"))
    # the opened bar hides once the closed bar appears
    inner = inner.replace(f'data-in="{a}" data-out="{b}" data-fx="none" data-d="0.32" data-base="rotate(-24deg)"',
                          f'data-hard="1" data-in="{a}" data-out="{a+0.12}" data-fx="none" data-d="0.32" data-base="rotate(-24deg)"')
    return scene(F["yel"]["bg"], a, b, "whipL", inner, d=0.12, drift=0.03)


def render(name, html, dur, audio, out_dir, cover_t=0.9):
    tmp = Path(tempfile.mkdtemp(prefix=f"hb-{name}-", dir="/tmp/claude-0/-home-claude/60837be5-8cde-507a-87a7-2bafa6fa6f6c/scratchpad"))
    (tmp / "p.html").write_text(html)
    from playwright.sync_api import sync_playwright
    n = int(round(dur * FPS))
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto((tmp / "p.html").as_uri()); pg.wait_for_timeout(600)
        for i in range(n):
            pg.evaluate(f"seek({i / FPS:.4f})")
            pg.screenshot(path=str(tmp / f"f{i:04d}.jpg"), type="jpeg", quality=93)
        # 2x cover, Lanczos down
        pg2 = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg2.goto((tmp / "p.html").as_uri()); pg2.wait_for_timeout(600)
        pg2.evaluate(f"seek({cover_t})"); pg2.screenshot(path=str(tmp / "cover2x.png"))
        br.close()
    from PIL import Image
    Image.open(tmp / "cover2x.png").convert("RGB").resize((W, H), Image.LANCZOS).save(out_dir / f"{name}-cover.jpg", quality=92)
    mp4 = out_dir / f"{name}.mp4"
    fade = max(0, dur - 1.2)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(tmp / "f%04d.jpg"), "-i", str(audio),
                    "-filter_complex", f"[1:a]atrim=0:{dur},asetpts=N/SR/TB,afade=t=in:d=0.03,afade=t=out:st={fade}:d=1.2[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "19",
                    "-preset", "slow", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart",
                    "-t", str(dur), str(mp4)], check=True)
    shutil.rmtree(tmp)
    return mp4

"""Tiny deterministic Reel renderer for the LH recovery: HTML scenes, JS seek(t), Playwright 2x screenshots,
ffmpeg Lanczos to 1080x1920, original track reused (trimmed, faded, -14 LUFS)."""
import os, sys, json, subprocess, shutil, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lhkit import *  # noqa

W, H = 1080, 1920
FPS = 30
SCR = Path("/tmp/claude-0/-home-claude/60837be5-8cde-507a-87a7-2bafa6fa6f6c/scratchpad/lh")

JS = r"""
const ease=x=>1-Math.pow(1-x,3);
const back=x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
const cl=(x)=>Math.max(0,Math.min(1,x));
function seek(t){
 const scs=[...document.querySelectorAll('.sc')];
 scs.forEach((s,i)=>{
  const a=+s.dataset.a,b=+s.dataset.b,tr=s.dataset.tr;
  const nxt=scs[i+1]; const nb = nxt? +nxt.dataset.a : 1e9;
  const vis = t>=a && t<b+0.0001 || (nxt && t>=nb && t<nb+0.28 && false);
  s.style.display = (t>=a && t<b)?'block':'none';
  if(!(t>=a && t<b)) return;
  const lt=t-a, p=cl(lt/0.28), e=ease(p);
  s.style.zIndex=10+i; s.style.clipPath='none'; s.style.transform='none'; s.style.filter='none';
  if(i>0 && lt<0.28){
   // keep previous visible beneath during the transition
   const pv=scs[i-1]; pv.style.display='block'; pv.style.zIndex=9+i;
   if(tr==='wipe') s.style.clipPath=`inset(0 ${100-100*e}% 0 0)`;
   if(tr==='iris') s.style.clipPath=`circle(${e*120}% at 50% 45%)`;
   if(tr==='diag') s.style.clipPath=`polygon(0 0, ${e*220}% 0, ${e*220-100}% 100%, 0 100%)`;
   if(tr==='push'){ s.style.transform=`translateY(${(1-e)*100}%)`; pv.style.transform=`translateY(${-e*30}%)`; }
   if(tr==='slam'){ const k=1+(1-back(p))*0.0+ (1-e)*0.22; s.style.transform=`scale(${k})`; s.style.opacity=Math.min(1,p*3);}
   if(tr==='plate'){ if(lt<0.1){ s.style.filter='none'; s.style.transform=`translate(${lt<0.05?10:-8}px,${lt<0.05?7:-5}px)`; } }
  } else { s.style.opacity=1; }
  // shake after slam
  if(tr==='slam' && lt>=0.28 && lt<0.45){ const k=Math.sin(lt*90)*6*(1-(lt-0.28)/0.17); s.style.transform=`translate(${k}px,${-k*0.6}px)`; }
  // camera push
  const cam=s.querySelector('.cam'); if(cam){ const pr=cl(lt/Math.max(0.1,b-a)); cam.style.transform=`scale(${1+0.035*pr})`; }
  s.querySelectorAll('[data-in]').forEach(el=>{
   const ti=+el.dataset.in, q=cl((lt-ti)/0.24); const kind=el.dataset.k||'up';
   if(ti<=0 && lt>=0){ el.style.opacity=1; el.style.transform=el.dataset.base||''; }
   if(ti>0){
    el.style.opacity=q>0?Math.min(1,q*2):0;
    const bb=back(q);
    if(kind==='up') el.style.transform=`${el.dataset.base||''} translateY(${(1-bb)*60}px)`;
    if(kind==='pop') el.style.transform=`${el.dataset.base||''} scale(${0.4+0.6*bb})`;
    if(kind==='left') el.style.transform=`${el.dataset.base||''} translateX(${(1-bb)*-140}px)`;
    if(kind==='drop') el.style.transform=`${el.dataset.base||''} translateY(${(1-bb)*-220}px) rotate(${(1-bb)*-14}deg)`;
   }
  });
  s.querySelectorAll('[data-ring]').forEach(el=>{
   const [t0,d,f0,f1,C]=el.dataset.ring.split(',').map(Number); const q=ease(cl((lt-t0)/d));
   el.setAttribute('stroke-dasharray',`${C*(f0+(f1-f0)*q)} ${C}`);
  });
  s.querySelectorAll('[data-roll]').forEach(el=>{
   const [t0,d,v0,v1]=el.dataset.roll.split(',').map(Number); const q=ease(cl((lt-t0)/d));
   el.textContent=Math.round(v0+(v1-v0)*q)+(el.dataset.suf||'');
  });
  s.querySelectorAll('[data-grow]').forEach(el=>{
   const [t0,d,w0,w1]=el.dataset.grow.split(',').map(Number); const q=ease(cl((lt-t0)/d));
   el.style.width=(w0+(w1-w0)*q)+'px';
  });
  s.querySelectorAll('[data-jit]').forEach(el=>{
   const [t0]=el.dataset.jit.split(',').map(Number); if(lt>t0){ const k=Math.sin((lt-t0)*40)*5; el.style.transform=(el.dataset.base||'')+` translate(${k}px,0)`; }
  });
 });
}
"""

def anim_ring(size, frac0, frac1, t0, d, **kw):
    """ring() with an animated fill: returns svg where the fill circle carries data-ring."""
    svg = ring(size, frac0, **kw)
    r = size * 0.40; C = 2 * 3.14159265 * r
    # the 3rd <circle> is the fill
    i = svg.find('stroke-dasharray="')
    return svg[:i] + f'data-ring="{t0},{d},{frac0},{frac1},{C:.2f}" ' + svg[i:]

def scene(a, b, field, body, tr="cut"):
    return (f"<div class='sc' data-a='{a}' data-b='{b}' data-tr='{tr}' style='position:absolute;inset:0;display:none;"
            f"background:{F[field]['bg']}'><div class='field' style='background-color:{F[field]['bg']}'></div>"
            f"<div class='cam' style='position:absolute;inset:0;transform-origin:50% 45%'>{body}</div><div class='grain'></div></div>")

def build_html(scenes):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css(W,H)}</style></head><body>"
            f"<div class='page'>{''.join(scenes)}</div><script>{JS}</script></body></html>")

def render(rid, scenes, dur, audio_src, out_mp4, keep_frames=False):
    from playwright.sync_api import sync_playwright
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    fd = SCR / f"frames-{rid}"; shutil.rmtree(fd, ignore_errors=True); fd.mkdir(parents=True)
    hp = SCR / f"{rid}.html"; hp.write_text(build_html(scenes))
    n = int(round(dur * FPS))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg.goto("file://" + str(hp)); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        for k in range(n):
            pg.evaluate(f"seek({k / FPS + 1e-4})")
            pg.screenshot(path=str(fd / f"{k:05d}.jpg"), type="jpeg", quality=93)
        b.close()
    aud = SCR / f"{rid}-a.m4a"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(audio_src), "-vn", "-t", f"{dur}", "-af",
                    f"afade=t=in:d=0.05,afade=t=out:st={dur-0.9:.2f}:d=0.9,loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-ar", "44100", "-c:a", "aac", "-b:a", "160k", str(aud)], check=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", str(fd / "%05d.jpg"), "-i", str(aud),
                    "-vf", f"scale={W}:{H}:flags=lanczos,format=yuv420p", "-c:v", "libx264", "-profile:v", "high",
                    "-preset", "slow", "-crf", "20", "-r", str(FPS), "-c:a", "copy", "-shortest", "-movflags", "+faststart",
                    str(out_mp4)], check=True)
    if not keep_frames:
        shutil.rmtree(fd); aud.unlink()

def cover(scene_body, field, out_jpg):
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{css(W,H)}</style></head><body><div class='page' "
            f"style='background:{F[field]['bg']}'><div class='field' style='background-color:{F[field]['bg']}'></div>{scene_body}"
            f"<div class='grain'></div></div></body></html>")
    shoot([html], [out_jpg], W, H)

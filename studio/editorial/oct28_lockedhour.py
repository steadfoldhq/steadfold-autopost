#!/usr/bin/env python3
"""Locked Hour, Oct 28 studio build (Social studio, Wed Oct 28 2026).

Two Reels in the LH zine version of the drawn "claim + ONE action drawn being done by second 2" format (the shape of
"A head start makes you finish", 5.03 s / 40% on 46), built on the Oct 27 LH kit (studio/editorial/oct27_lockedhour.py:
its JS draw(t), face(), cloud(), laptop(), label(), check(), burst() are imported, not edited) plus new scenes here.

  resume  lh-reel-1029am-ready-to-resume  Thu Oct 29 08:30 ET, no trial.
          Frame 0: "Your half-done task follows you." + a drawn face whose thought cloud still holds the half-done report
          while someone asks "Got a minute?". By 1.9 s a sticky note is written ("next: fix slide 4") and the cloud
          shrinks into it. Research: Leroy & Glomb 2018, Organization Science 29(3):380-397.
  list    lh-reel-1031-bedtime-list        Sat Oct 31 19:00 ET, no trial.
          Frame 0: "A to-do list helps you sleep." + a drawn person awake in bed, tomorrow's tasks swirling in a thought
          cloud. By 2.0 s the tasks fly onto a notepad, the lamp clicks off, the eyes close.
          Research: Scullin et al. 2018, J Exp Psychol: General 147(1):139-146.
  oneword lh-oneword-05                    Mon Nov 2 17:00 ET, One Word No. 5 "Walk." (layout of lh-oneword-04).
          Research: Oppezzo & Schwartz 2014, JEP: Learning, Memory, and Cognition 40(4):1142-1152.

  python3 studio/editorial/oct28_lockedhour.py resume|list|oneword [--cover-only] [--still=0,1.5,3]
Music: existing LH v4 library tracks only (tools/music-library.json), -14 LUFS. No new music.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
SCR = Path(os.environ.setdefault("LH_SCR", "/tmp/claude-0/oct28-lockedhour"))
SCR.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(REPO / "studio/editorial"))
import edkit  # noqa: E402
import oct27_lockedhour as k27  # noqa: E402

OUT = REPO / "media/studio-oct28/lockedhour"
OUT.mkdir(parents=True, exist_ok=True)
W, H, FPS, INK = 1080, 1920, 30, k27.INK
CSS, LIB, F = k27.CSS, k27.LIB, k27.F

JS_EXTRA = r"""
// ================= shared extras (Oct 28) =================
function penD(x,y){return `<g transform="translate(${x} ${y}) rotate(28)"><rect x="-11" y="-170" width="22" height="140" rx="7" fill="${HP}" stroke="${INK}" stroke-width="5"/>`+
 `<rect x="-11" y="-182" width="22" height="22" rx="6" fill="${CR}" stroke="${INK}" stroke-width="5"/><path d="M-11 -30 L0 0 L11 -30Z" fill="${CR2}" stroke="${INK}" stroke-width="5" stroke-linejoin="round"/></g>`;}
// sticky note: lines revealed char by char (chars), optional pen at the writing point, optional strike on line `strike` (k 0..1)
function noteD(x,y,rot,s,lines,chars,op){op=op||{};const w=op.w||400,h=op.h||250,fs=op.fs||50,lh=op.lh||66,cw=op.cw||0.31;
 let n=chars,body='',px=null,py=null;
 lines.forEach((ln,i)=>{const k=Math.max(0,Math.min(ln.length,n));const show=ln.slice(0,k);n-=ln.length;const by=-h/2+86+i*lh;
  body+=`<text x="${-w/2+30}" y="${by}" font-family="Caveat Brush" font-size="${fs}" fill="${INK}">${show}</text>`;
  if(k>0&&k<ln.length&&px===null){px=-w/2+30+k*fs*cw;py=by;}
  if(op.strike===i&&op.sk>0) body+=`<path d="M${-w/2+24} ${by-fs*0.3} l${(ln.length*fs*cw+12)*op.sk} 0" stroke="${DP}" stroke-width="8" stroke-linecap="round"/>`;});
 let pen=(op.pen&&px!==null)?penD(px,py):'';
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">`+sh(`<rect x="${-w/2}" y="${-h/2}" width="${w}" height="${h}" rx="6" fill="${op.col||HY}" ${o}/>`,9)+
  `<rect x="-70" y="${-h/2-24}" width="140" height="44" fill="${HPL}" opacity=".9" stroke="${INK}" stroke-width="3" transform="rotate(-4)"/>`+body+pen+`</g>`;}
function cloudG(cx,cy,s,inner){return `<g transform="translate(${cx} ${cy}) scale(${s}) translate(${-cx} ${-cy})">${cloud(cx,cy,1)}${inner||''}</g>`;}
function chipD(x,y,txt,fs,op){const w=txt.length*fs*0.56+44;return `<g transform="translate(${x} ${y})" opacity="${op==null?1:op}"><rect x="${-w/2}" y="${-fs*0.95}" width="${w}" height="${fs*1.6}" rx="${fs*0.8}" fill="${CR}" stroke="${INK}" stroke-width="5"/>`+
 `<text x="0" y="${fs*0.32}" font-family="Inter" font-weight="800" font-size="${fs}" fill="${INK}" text-anchor="middle">${txt}</text></g>`;}

// ================= SCENE A: ready-to-resume note (rev 2, CD gate Oct 28) =================
const NOTE_A=['stopped: slide 4','next: fix the chart'], NOTE_O={w:470,h:250,fs:52,lh:72};
function recol(svg,hair,shirt){return svg.split('#FFD43B').join(hair).split('#FFBAD6').join(shirt);}
function coworker(x,y,s,look,smile,t){return recol(face(x,y,s,0,look,smile,t),'#FF5CA8','#FFE27A');}
function reportCloud(cx,cy,lab){return `<g transform="translate(${cx-20} ${cy+85}) scale(.55)">${laptop(0,0,.5)}</g>`+(lab?label(cx+10,cy-95,'the report, half done',-3,48):'');}
function noteBlank(x,y,rot,s){return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">`+sh(`<rect x="-235" y="-125" width="470" height="250" rx="6" fill="${HY}" ${o}/>`,9)+
 `<rect x="-70" y="-149" width="140" height="44" fill="${HPL}" opacity=".9" stroke="${INK}" stroke-width="3" transform="rotate(-4)"/>`+
 `<rect x="-190" y="-50" width="300" height="26" rx="13" fill="${INK}" opacity=".55"/><rect x="-190" y="20" width="360" height="26" rx="13" fill="${INK}" opacity=".55"/></g>`;}
SC.resume=function(t){
 let s='';
 const ph=t<2.2?0:t<5.4?1:t<8.8?2:t<11.8?3:4;
 if(ph==0||ph==1||ph==4){
  const look=ph==0?-EIO(seg(t,0.3,0.6))*0+EIO(seg(t,0.3,0.6)):1, smile=t>1.95?1:0.15;
  // the half-done task, still in the head (cloud), shrinks into the note once it's written
  if(ph==0){const g=EIO(seg(t,1.85,2.15)), bob=8*Math.sin(t*4);
   const cx=640+(560-640)*g, cy=800+bob+(1400-800)*g;
   if(g<1) s+=`<g opacity="${1-g*.6}">`+cloudG(cx,cy,0.85*(1-0.8*g),reportCloud(640,800,true))+`</g>`;
   if(t<0.95) s+=label(185,1000,'still on it…',-6,52);}
  // the interruption: a coworker walks up and asks
  const cin=1;
  s+=coworker(860+220*(1-cin),1190,0.72,-1,ph==0?0.4:1,t);
  const bk=ph==0?pop(seg(t,0.3,0.6)):(ph==1?1-seg(t,2.9,3.1):0);
  if(bk>0) s+=bubbleD(640,1050,'Got a minute?',1,bk,true);
  if(ph==1&&t>3.0){const k=pop(seg(t,3.0,3.3)); s+=bubbleD(430,1000,'Sure, go ahead.',1-seg(t,5.1,5.35),k,false);}
  s+=face(250,1170,0.8,0,look,smile,t);
  // the note: flies up at 0.9, written 1.0-1.85, then stays parked between them
  if(t>=0.9){const fin=EIO(seg(t,0.9,1.15)); const ny=1750+(1400-1750)*fin;
   const ch=ph==0?Math.floor(35*seg(t,1.0,1.85)):99;
   s+=noteD(560,ny,-3,0.86,NOTE_A,ch,Object.assign({pen:ph==0},NOTE_O));}
  if(ph==0) s+=burst(560,1400,seg(t,2.0,2.4),HY);
  if((ph==1&&t>3.3)||ph==4) s+=`<g opacity="${ph==4?1:seg(t,3.3,3.6)}">`+label(560,1255,'parked for later',-3,52)+`</g>`;
  return s;}
 if(ph==2){ // compare: no note vs note (labels >= 50 px)
  const a=pop(seg(t,5.5,5.85)), b=pop(seg(t,5.75,6.1));
  s+=`<g transform="translate(270 1190) scale(${0.8*a})">`+face(0,0,1,0,0,0.1,t)+`</g>`;
  if(a>0) s+=cloudG(430,930,0.45*a,reportCloud(430,930,false));
  s+=`<g transform="translate(800 1190) scale(${0.8*b})">`+face(0,0,1,0,-1,1,t)+`</g>`;
  if(b>0) s+=noteBlank(660,950,-5,0.4*b);
  if(t>6.0) s+=`<g opacity="${seg(t,6.0,6.3)}">`+label(270,1530,'no note',-3,60)+`</g>`;
  if(t>6.3) s+=check(950,1050,seg(t,6.3,6.7),44)+`<g opacity="${seg(t,6.3,6.6)}">`+label(800,1530,'wrote a note',-3,60)+`</g>`;
  return s;}
 // ph 3: do this, close-up: the same note is written, then stuck on the laptop
 s+=`<g transform="translate(540 1560) scale(1.4)">${laptop(0,0,.55)}</g>`;
 const ch=Math.floor(35*seg(t,9.0,10.4)); const q=EIO(seg(t,10.6,10.9));
 const ny=960+(1395-960)*q, ns=1.25-0.43*q;
 s+=noteD(540,ny,-3+3*q,ns,NOTE_A,ch,Object.assign({pen:q==0},NOTE_O));
 s+=burst(540,1395,seg(t,10.9,11.4),HY);
 if(t>11.0) s+=check(860,1240,seg(t,11.0,11.4),44);
 return s;};

// ================= SCENE B: bedtime to-do list =================
const TASKS=['email Sam','9 am call','buy milk'];
function bedD(){let s='';
 s+=sh(`<rect x="232" y="1170" width="46" height="400" rx="18" fill="${HY}" ${o}/>`,10);
 s+=sh(`<rect x="262" y="1420" width="790" height="86" rx="22" fill="${CR}" ${o}/>`,10);
 s+=`<path d="M300 1506 V1590 M1010 1506 V1590" stroke="${INK}" stroke-width="12" stroke-linecap="round"/>`;
 s+=`<ellipse cx="385" cy="1395" rx="115" ry="44" fill="#FFFFFF" ${o}/>`;return s;}
function blanketD(){return sh(`<path d="M478 1318 Q560 1276 660 1298 Q820 1330 1040 1318 Q1062 1380 1052 1428 H466 Q446 1370 478 1318Z" fill="${HPL}" ${o}/>`,10)+
 `<path d="M560 1330 Q600 1380 590 1426 M760 1328 Q800 1380 790 1426 M950 1322 Q990 1380 980 1426" stroke="${HP}" stroke-width="10" fill="none" stroke-linecap="round" opacity=".8"/>`;}
function tableD(on){let s=sh(`<rect x="40" y="1380" width="170" height="26" rx="8" fill="${HY}" ${o}/>`,8)+`<path d="M70 1406 V1580 M180 1406 V1580" stroke="${INK}" stroke-width="10" stroke-linecap="round"/>`;
 if(on>0) s+=`<path d="M70 1236 L0 1380 H260 L190 1236Z" fill="#FFF4B0" opacity="${0.75*on}"/>`;
 s+=`<path d="M125 1380 V1250" stroke="${INK}" stroke-width="9"/><rect x="95" y="1366" width="60" height="16" rx="6" fill="${INK}"/>`;
 s+=sh(`<path d="M80 1176 H170 L200 1246 H50Z" fill="${on>0.5?HY:'#E6DCCB'}" ${o}/>`,8);
 return s;}
function zzz(t,t0){let s='';for(let i=0;i<3;i++){const k=((t-t0)*0.6+i/3)%1; if(t<t0+i*0.4) continue;
  s+=`<text x="${470+60*k+i*8}" y="${1210-170*k}" font-family="Inter Display" font-weight="900" font-size="${44+26*k}" fill="${DP}" opacity="${Math.sin(Math.PI*k)}">z</text>`;}return s;}
function padD(x,y,s,lines,chars,op){op=op||{};const w=op.w||360,h=op.h||330,fs=op.fs||50,lh=op.lh||68,cw=0.31;
 let n=chars,body='',px=null,py=null;
 for(let i=0;i<(op.rows||4);i++) body+=`<path d="M${-w/2+20} ${-h/2+96+i*lh} H${w/2-20}" stroke="#8FB0E0" stroke-width="3" opacity=".7"/>`;
 lines.forEach((ln,i)=>{const k=Math.max(0,Math.min(ln.length,n));n-=ln.length;const by=-h/2+86+i*lh;
  body+=`<text x="${-w/2+34}" y="${by}" font-family="Caveat Brush" font-size="${fs}" fill="${INK}">${ln.slice(0,k)}</text>`;
  if(k>0&&k<ln.length&&px===null){px=-w/2+34+k*fs*cw;py=by;}
  if(op.strike===i&&op.sk>0) body+=`<path d="M${-w/2+28} ${by-fs*0.3} l${(ln.length*fs*cw+14)*op.sk} 0" stroke="${DP}" stroke-width="8" stroke-linecap="round"/>`;
  if(op.ticks&&op.ticks[i]>0) body+=check(w/2-46,by-fs*0.3,op.ticks[i],24);});
 let rings='';for(let i=0;i<6;i++) rings+=`<circle cx="${-w/2+40+i*(w-80)/5}" cy="${-h/2}" r="12" fill="${CR}" stroke="${INK}" stroke-width="5"/>`;
 return `<g transform="translate(${x} ${y}) scale(${s})">`+sh(`<rect x="${-w/2}" y="${-h/2}" width="${w}" height="${h}" rx="10" fill="#FFFFFF" ${o}/>`,10)+
  `<path d="M${-w/2+20} ${-h/2+20} V${h/2-14}" stroke="#E8605A" stroke-width="3" opacity=".6"/>`+body+rings+(op.pen&&px!==null?penD(px,py):'')+`</g>`;}
function moonD(x,y,k){if(k<=0)return '';return `<g transform="translate(${x} ${y}) scale(${k})">`+sh(`<path d="M30 -70 A75 75 0 1 0 30 70 A58 58 0 1 1 30 -70Z" fill="${HY}" ${o}/>`,9)+
 `<circle cx="110" cy="-50" r="7" fill="${INK}"/><circle cx="140" cy="20" r="5" fill="${INK}"/></g>`;}
SC.list=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==4){ // end card (distinct from Thursday's): the finished list by moonlight
  const L=['work stuff','email Sam the budget','call the dentist at 9','buy milk on the way home'];
  s+=moonD(170,880,pop(seg(t,12.05,12.4)));
  s+=padD(540,1170,1.0,L,99,{w:600,h:420,fs:50,lh:76,rows:4,strike:0,sk:1,ticks:[0,1,1,1]});
  s+=label(540,1470,'goodnight.',-3,64)+`<g transform="translate(420 -60)">${zzz(t,12.0)}</g>`;
  return s;}
 if(ph==0||ph==1){
  const lampOn=ph==0?1-seg(t,2.0,2.1):0;
  const lid=ph==0?EIO(seg(t,2.05,2.35)):1;
  s+=bedD()+tableD(lampOn);
  // head lying on the pillow, eyes on the ceiling until the list is written
  s+=`<g transform="translate(395 1340) rotate(-90) scale(.62)">`+recol(face(0,0,1,lid,ph==0&&t<1.0?Math.sin(t*5):0,lid>0.9?1:0,t),'#FF5CA8','#FFE27A')+`</g>`;
  s+=blanketD();
  // tomorrow's tasks swirling in the cloud, then flying onto the notepad
  if(ph==0){const ck=1-EIO(seg(t,1.95,2.2));
   if(ck>0) s+=cloudG(760,990,ck,'');
   TASKS.forEach((tx,i)=>{const t0=0.95+0.3*i, f=EIO(seg(t,t0,t0+0.3));
    if(f>=1) return; const sl=[[680,930],[835,1005],[690,1080]][i]; const x0=sl[0]+14*Math.sin(t*3+i*2), y0=sl[1]+10*Math.cos(t*3.4+i);
    const x=x0+(225-x0)*f, y=y0+(915+i*68-y0)*f; s+=chipD(x,y,tx,42,1-0.7*f);});
   if(t<0.95) s+=label(720,760,"can't stop thinking about tomorrow",-3,52);}
  // the notepad: on the table, lifts up to be written on, goes back
  const up=ph==0?EIO(seg(t,0.7,0.95)):(ph==1?1-EIO(seg(t,2.4,2.8)):0);
  const px=125+(225-125)*up, py=1372+(960-1372)*up, ps=0.32+0.68*up;
  const ch=ph==0?Math.floor(26*seg(t,1.2,1.95)):99;
  s+=padD(px,py,ps,TASKS,ch,{pen:ph==0&&t>1.2&&t<1.95,rows:3,h:300});
  if(ph>=1||t>2.2) s+=zzz(t,2.25);
  if(ph==1&&t>3.0) s+=`<g opacity="${seg(t,3.0,3.3)}">`+label(760,1000,'on paper, not in your head',-3,52)+`</g>`;
  if(ph==0) s+=burst(225,960,seg(t,1.95,2.35),HY);
  return s;}
 if(ph==2){ // bars: minutes to fall asleep (BPS Research Digest: about 15 vs about 25), labels >= 52 px
  const g1=EIO(seg(t,5.9,6.6)), g2=EIO(seg(t,6.2,7.1));
  s+=label(540,1020,'minutes to fall asleep',-2,64);
  const row=(y,txt,frac,g,col,num)=>`<text x="100" y="${y-22}" font-family="Inter" font-weight="800" font-size="54" fill="${INK}">${txt}</text>`+
   sh(`<rect x="100" y="${y}" width="880" height="120" rx="26" fill="${CR}" ${o}/>`,9)+`<rect x="110" y="${y+10}" width="${860*frac*g}" height="100" rx="18" fill="${col}"/>`+
   `<text x="${Math.max(150,110+860*frac*g-24)}" y="${y+80}" font-family="Inter Display" font-weight="900" font-size="58" fill="${INK}" text-anchor="end" opacity="${seg(g,.6,1)}">${num}</text>`;
  s+=row(1140,"Wrote a to-do list",0.6,g1,HP,'about 15');
  s+=row(1380,"Listed what they'd done",1.0,g2,'#E6DCCB','about 25');
  if(t>7.3) s+=check(700,1200,seg(t,7.3,7.7),46);
  return s;}
 // ph 3: do this: vague line struck, specific lines written
 const L=['work stuff','email Sam the budget','call the dentist at 9','buy milk on the way home'];
 const t1=seg(t,9.05,9.35), sk=EIO(seg(t,9.5,9.75));
 const ch=Math.floor(10*t1)+(t>9.8?Math.floor(65*seg(t,9.8,11.2)):0);
 s+=padD(540,1240,1.32,L,ch,{pen:t<11.2,w:600,h:420,fs:50,lh:76,rows:4,strike:0,sk:sk,ticks:[0,seg(t,10.3,10.6),seg(t,10.85,11.15),seg(t,11.35,11.65)]});
 if(t>9.6&&t<12) s+=label(300,925,'too vague',-6,52);
 return s;};
"""


def H_(text, size, field="dots"):
    return edkit.dual(text, F[field], cls="H fit", style=f"font-size:{size}px")


def page(spec, cover_html=None):
    T = ""
    for k, b in enumerate(spec["beats"]):
        T += (f'<div id="b{k}" style="position:absolute;left:90px;width:900px;top:{b.get("top", 300)}px;opacity:0;transform-origin:50% 0">'
              + (f'<div class="kick" style="font-size:{b.get("ks", 70)}px;margin-bottom:14px">{b["kick"]}</div>' if b.get("kick") else "")
              + H_(b["head"], b.get("fs", 124), b.get("field", "dots"))
              + (f'<div class="sub" style="font-size:{b.get("ss", 46)}px;margin-top:24px">{b["sub"]}</div>' if b.get("sub") else "")
              + (f'<div style="text-align:center;margin-top:20px"><span style="display:inline-block;padding:8px 22px;border-radius:99px;background:#FFFDF4;border:4px solid {INK};box-shadow:5px 5px 0 {INK};font:700 30px Inter;color:{INK};max-width:900px">{b["src"]}</span></div>' if b.get("src") else "")
              + "</div>")
    follow = (f'<div id="follow" style="position:absolute;left:0;right:0;top:{spec.get("follow_y", 1470)}px;text-align:center;opacity:0">'
              f'<span class="chip">Follow for one small<br>focus trick a day.</span></div>')
    sx, sy = spec.get("stamp_xy", (850, 1560))
    stamp = f'<div id="stampw" style="position:absolute;left:0;top:0;opacity:0">{edkit.stamp("lockedhour", sx, sy, size=150, rot=-10)}</div>'
    bg2 = spec.get("bg2col", "#FFF6E5")
    css = CSS.replace("opacity:0;background-color:#FFF6E5", f"opacity:0;background-color:{bg2}")
    body = ('<div id="bg"></div><div id="bg2"></div>'
            f'<svg id="art" style="position:absolute;left:0;top:0" width="{W}" height="{H}" viewBox="0 0 {W} {H}"></svg>'
            + T + follow + stamp + (cover_html or "") + f"<script>{k27.JS}{JS_EXTRA}</script>")
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"


def render(spec, tag, still=None, cover_page=None, cover_out=None):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    durs = spec["durs"]
    starts = [round(sum(durs[:k]), 4) for k in range(len(durs))]
    js = dict(durs=durs, starts=starts, scene=spec["scene"], cover=False, cover_t=0, bg2=[b.get("bg2", False) for b in spec["beats"]])
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--renderer-process-limit=1"])
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2 if cover_out else 1)
        tf = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, dir=str(SCR))
        tf.write(cover_page if cover_page else page(spec)); tf.close()
        pg.goto(Path(tf.name).as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        pg.evaluate(edkit.FIT_JS, 900)
        if cover_page:
            png = SCR / f"{tag}-cover.png"; pg.screenshot(path=str(png))
            Image.open(png).resize((W, H), Image.LANCZOS).convert("RGB").save(cover_out, quality=92, subsampling=0)
            br.close(); os.unlink(tf.name); png.unlink(); return cover_out
        pg.evaluate(f"SPEC={json.dumps(js)}")
        if still:
            ims = []
            for ts in still:
                pg.evaluate(f"draw({ts})"); pth = SCR / f"{tag}-still.png"; pg.screenshot(path=str(pth))
                ims.append(Image.open(pth).convert("RGB").resize((432, 768)))
            sh = Image.new("RGB", (437 * len(ims), 768), "white")
            for k, im in enumerate(ims):
                sh.paste(im, (437 * k, 0))
            sh.save(SCR / f"{tag}-stills.jpg", quality=85); br.close(); os.unlink(tf.name); return None
        fdir = SCR / f"{tag}-frames"; shutil.rmtree(fdir, ignore_errors=True); fdir.mkdir(parents=True)
        total = sum(durs); n = int(round(total * FPS))
        for fr in range(n):
            pg.evaluate(f"draw({fr / FPS})")
            pg.screenshot(path=str(fdir / f"{fr:04d}.jpg"), type="jpeg", quality=93)
        br.close()
    os.unlink(tf.name)
    return fdir, total, starts


def encode(fdir, total, music, hits, out_mp4):
    a = SCR / f"{out_mp4.stem}.wav"
    inputs = ["-i", str(REPO / music)]
    filt = [f"[0:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.04,afade=t=out:st={total-0.7:.3f}:d=0.7[m]"]
    mix = ["[m]"]
    for k, (pt, name, vol) in enumerate(hits):
        inputs += ["-i", str(REPO / LIB["sfx"][name]["file"])]
        filt.append(f"[{k+1}:a]volume={vol},adelay={int(pt*1000)}|{int(pt*1000)}[p{k}]")
        mix.append(f"[p{k}]")
    filt.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[o]")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[o]",
                    "-ar", "48000", "-ac", "2", str(a)], check=True)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(fdir / "%04d.jpg"), "-i", str(a),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "19", "-profile:v", "high", "-threads", "1",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out_mp4)], check=True)
    shutil.rmtree(fdir); a.unlink()


# ------------------------------------------------------------------ covers (dedicated, style-menu layouts)
def cover_lookb():
    """Style 1 Look B big-headline cover in the LH zine look (loud): Inter Display 900 hook with highlighter pills,
    Caveat Brush save-line + arrow, the Reel's drawn scene (the half-done task in a thought cloud, the coworker, the note), stamp."""
    hook = f"<div style='position:absolute;left:90px;width:900px;top:300px'>" + H_("Switching tasks? / *Your mind stays behind.*", 132, "dots") + "</div>"
    save = ("<div style=\"position:absolute;left:90px;width:900px;top:545px;text-align:center;font-family:'Caveat Brush';font-size:62px;"
            "color:#E8336F;transform:rotate(-3deg)\">write one line before you switch ↓</div>")
    art = ("<svg id='cv' style='position:absolute;left:0;top:0' width='1080' height='1920' viewBox='0 0 1080 1920'></svg>"
           "<script>T=0;document.getElementById('cv').innerHTML='<g transform=\"translate(0 -40)\">'+cloudG(650,880,0.72,reportCloud(650,880,true))"
           "+coworker(860,1190,0.72,-1,0.6,0)+face(250,1170,0.8,0,1,0.6,0)"
           "+noteD(560,1390,-3,0.86,NOTE_A,99,NOTE_O)+'</g>'</script>")
    stamp = edkit.stamp("lockedhour", 60, 760, size=140, rot=-12)
    return hook + save + art + stamp


def cover_sticky():
    """Style 13 sticky-note list (quiet): lined note card, red margin, tape, Caveat Brush title, ticked Caveat items,
    on the LH pink dot grid, plus the Reel's drawn lamp."""
    paper = "#FFFDF4"
    card = (f"<div style='position:absolute;left:110px;top:330px;width:860px;height:790px;background:{paper};transform:rotate(-2deg);"
            f"border:6px solid {INK};border-radius:10px;box-shadow:14px 14px 0 {INK};"
            f"background-image:linear-gradient({paper} 330px,transparent 330px),repeating-linear-gradient({paper} 0 118px,rgba(80,110,180,.30) 118px 121px)'>"
            f"<div style='position:absolute;left:96px;top:0;bottom:0;width:4px;background:rgba(220,80,80,.55)'></div>"
            f"<div style='position:absolute;left:130px;right:40px;top:50px;font-family:\"Caveat Brush\";font-size:112px;line-height:.98;color:#E8336F;white-space:nowrap'>"
            f"A to-do list<br>helps you sleep.</div>"
            f"<ul style='position:absolute;left:130px;right:30px;top:330px;list-style:none;font-family:Caveat;font-weight:700;font-size:84px;line-height:120px;color:{INK}'>"
            f"<li><span style='color:#E8336F'>✓</span> write tomorrow's list</li><li><span style='color:#E8336F'>✓</span> be specific</li>"
            f"<li><span style='color:#E8336F'>✓</span> then lights out</li></ul></div>"
            f"<div style='position:absolute;left:420px;top:300px;width:240px;height:66px;background:rgba(255,212,59,.8);transform:rotate(3deg);border:2px solid rgba(27,23,23,.25)'></div>")
    art = ("<svg id='cv' style='position:absolute;left:0;top:0' width='1080' height='1920' viewBox='0 0 1080 1920'></svg>"
           "<script>T=0;document.getElementById('cv').innerHTML='<g transform=\"translate(790 -40)\">'+tableD(0)+'</g>'"
           "</script>")
    stamp = edkit.stamp("lockedhour", 110, 1170, size=165, rot=-12)
    return card + art + stamp


def cover_page(kind):
    bg = "#FFD5E5" if kind == "sticky" else "#FFF0A6"
    inner = {"lookb": cover_lookb, "sticky": cover_sticky}[kind]()
    css = CSS.replace("background-color:#FFF0A6", f"background-color:{bg}", 1)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body><div id='bg'></div>"
            f"<script>{k27.JS}{JS_EXTRA}</script>{inner}</body></html>")


# ------------------------------------------------------------------ specs
SPECS = {
    "resume": dict(
        id="lh-reel-1029am-ready-to-resume", scene="resume", music="media/music/library/v4/lh-x-tick-boom.mp3",
        durs=[2.2, 3.2, 3.4, 3.0, 2.2], cover="lookb", follow_y=600, stamp_xy=(60, 800),
        hits=[(0.3, "sfx-x-sticker-pop", 0.25), (1.0, "sfx-x-swoosh-in", 0.3), (2.0, "sfx-x-sticker-pop", 0.35),
              (5.4, "sfx-x-whoosh-hit", 0.25), (10.9, "sfx-x-paper-slap", 0.35)],
        beats=[
            dict(head="Switching tasks? / *Your mind stays behind.*", fs=128, top=300),
            dict(kick="so before you switch,", head="Write where you stopped / *and what's next.*", fs=104),
            dict(kick="people who wrote a note before switching", ks=60, head="*remembered more*", fs=140,
                 sub="and made better choices on the next task.", ss=44, src="Leroy &amp; Glomb 2018 · Organization Science", bg2=True),
            dict(kick="Do this:", head="Before you switch, / *write your next step.*", fs=112),
            dict(head="Switching tasks? / *Your mind stays behind.*", fs=128, top=300),
        ]),
    "list": dict(
        id="lh-reel-1031-bedtime-list", scene="list", music="media/music/library/v4/lh-x-phone-down.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.2], cover="sticky", follow_y=600, stamp_xy=(870, 800), bg2col="#FFE3EE",
        hits=[(0.95, "sfx-x-swoosh-in", 0.3), (2.05, "sfx-x-sticker-pop", 0.35), (5.6, "sfx-x-whoosh-hit", 0.25),
              (9.5, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(head="A to-do list / helps you *sleep.*", fs=150, top=300),
            dict(kick="lying awake planning tomorrow?", head="Put tomorrow on paper. / *Sleep comes sooner.*", fs=104, bg2=True),
            dict(kick="the research", head="People who wrote a / to-do list fell asleep / *about 10 minutes faster*", fs=94,
                 sub="vs. people who listed what they'd done.", ss=46,
                 src="Scullin et al. 2018 · J Exp Psych"),
            dict(kick="Do this, before bed:", head="Write tomorrow's list. / *Be specific.*", fs=112,
                 sub="5 minutes, every task you need to do.", ss=46),
            dict(head="A to-do list / helps you *sleep.*", fs=150, top=300, bg2=True),
        ]),
}

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    still = next((a[8:] for a in sys.argv if a.startswith("--still=")), None)
    for key in args or list(SPECS):
        if key == "oneword":
            import oct28_lockedhour_feed as fd_; fd_.oneword(); print("done oneword"); continue
        s = SPECS[key]
        cov = OUT / f"{s['id']}-cover.jpg"
        render(s, key, cover_page=cover_page(s["cover"]), cover_out=cov)
        print("cover", cov)
        if "--cover-only" in sys.argv:
            continue
        if still:
            render(s, key, still=[float(x) for x in still.split(",")]); print("stills", SCR / f"{key}-stills.jpg"); continue
        fdir, total, starts = render(s, key)
        out = OUT / f"{s['id']}.mp4"
        encode(fdir, total, s["music"], s["hits"], out)
        print(out, round(total, 2), starts)

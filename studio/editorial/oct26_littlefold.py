#!/usr/bin/env python3
"""Oct 26 (Social studio, Littlefold maker): Thu Oct 29 19:00 Reel 'Back to sleep. Tummy to play.'

STYLE: kinetic big text (style-menu #5) + the Littlefold ARCH CARD and a soft-countdown giant numeral beat (style #2, LF
'lf-count'), on a sunny Warm Sherbet paper field with drifting blobs. Deliberately NOT the 'sunshine washing-line' world
(no washing line, no hills, no sky): LF already has ~6 washing-line Reels in a row (grid rule: never the same style twice).

Reuses the reel_story engine (studio/recovery-oct22c/littlefold/reel_story.py: helpers, frames(), encode(); imported, not
edited) and replaces only draw() and html(). Frames: Playwright Chromium, 1080x1920, 30 fps -> H.264 + AAC.
Music: existing track lf-x-tiny-parade (tools/music-library.json, 103.4 bpm, drop 9.195 s): 'Do this' lands on the drop.
Facts (checked Oct 26 2026): AAP HealthyChildren.org 'Back to Sleep, Tummy to Play' (updated 9/8/2026);
CPS Caring for Kids 'Preventing flat heads in babies who sleep on their backs'.

    python3 studio/editorial/oct26_littlefold.py [--still=0.1,1.5,...] [--cover-only]
"""
import os
import sys
from pathlib import Path
sys.dont_write_bytecode = True
os.environ.setdefault("LF_SCR", "/tmp/claude-0/lf26")
sys.path.insert(0, "/home/claude/steadfold-autopost/studio/recovery-oct22c/littlefold")
import reel_story as RS  # noqa: E402

K, F, INK, KICK, B = RS.K, RS.F, RS.INK, RS.KICK, RS.B
W, H = RS.W, RS.H
OUT = RS.REPO / "media" / "studio-oct26" / "littlefold"
MUSIC = RS.LIB / "v4" / "lf-x-tiny-parade.mp3"
BP = 60 / 103.4
DROP = 9.195
FOLLOW = "Follow for one calm thing a night, from bump to toddler."
CHIP_AAP = "AAP · HealthyChildren.org"
CHIP_CPS = "CPS · Caring for Kids"

RS.JS += r"""
// ===================== Oct 26: kinetic text + arch card (no washing line) =====================
const BSK2='#FFDCC4', BERRY='#D9497A', LILAC='#D9D3F2';
const AX=190, AY=860, AW=700, AH=520;           // arch card box
function archPath(x,y,w,h){const r=w/2;return `M${x} ${y+h} L${x} ${y+r} A${r} ${r} 0 0 1 ${x+w} ${y+r} L${x+w} ${y+h} Z`;}
function blobsBG(t){ // soft drifting corner blobs (background layer moves least)
 const b=[[60,330,260,'#FFD6E3'],[1010,520,230,'#FFE27E'],[-10,1240,250,'#CFE3F6'],[1060,1450,270,'#FFD3AE'],[560,170,170,'#D7E8CB']];
 let s='';b.forEach(([x,y,r,c],i)=>{const dx=14*Math.sin(t*0.5+i*1.7), dy=10*Math.cos(t*0.4+i);
  s+=`<circle cx="${x+dx}" cy="${y+dy}" r="${r}" fill="${c}" opacity=".75"/>`;});
 // faint paw prints (LF signature), drifting up very slowly
 const paws=[[150,980],[930,1080],[880,300],[120,620]];
 paws.forEach(([x,y],i)=>{const yy=y-6*t; s+=`<g transform="translate(${x} ${yy}) rotate(${-15+i*12}) scale(.9)" opacity=".22" fill="${BERRY}"><ellipse cx="0" cy="12" rx="22" ry="18"/><circle cx="-22" cy="-14" r="8"/><circle cx="-7" cy="-24" r="8"/><circle cx="9" cy="-24" r="8"/><circle cx="23" cy="-14" r="8"/></g>`;});
 return s;}
function rosette(x,y,col,txt,k,t){ if(k<=0) return ''; const s=0.3+0.7*E(k)+0.06*Math.sin(Math.PI*cl(k*1.4,0,1));
 let sc='';for(let i=0;i<16;i++){const a=i*Math.PI/8;sc+=`<circle cx="${62*Math.cos(a)}" cy="${62*Math.sin(a)}" r="16" fill="${col}" ${o} stroke-width="3.5"/>`;}
 return `<g transform="translate(${x} ${y}) scale(${1.3*s}) rotate(${4*Math.sin(t*2+x)})">
  <path d="M-30 40 L-52 130 L-30 116 L-14 138 L4 50Z" fill="${BERRY}" ${o} stroke-width="3.5"/><path d="M30 40 L52 130 L30 116 L14 138 L-4 50Z" fill="${CORAL}" ${o} stroke-width="3.5"/>
  ${sc}<circle r="60" fill="${CREAM}" ${o} stroke-width="3.5"/><circle r="50" fill="none" stroke="${col}" stroke-width="4" stroke-dasharray="4 7"/>
  ${(()=>{const L=txt.split(' ');return L.length>1?`<text y="-6" font-family="Caveat Brush" font-size="40" text-anchor="middle" fill="${INK}">${L[0]}</text><text y="30" font-family="Caveat Brush" font-size="40" text-anchor="middle" fill="${INK}">${L.slice(1).join(' ')}</text>`:`<text y="14" font-family="Caveat Brush" font-size="44" text-anchor="middle" fill="${INK}">${txt}</text>`;})()}</g>`;}
function matSVG(w){ // playmat, side-on (a soft sage rug with dots)
 let d='';for(let i=0;i<9;i++)d+=`<circle cx="${-w/2+40+i*(w-80)/8}" cy="16" r="5" fill="${CREAM}" opacity=".9"/>`;
 return `<rect x="${-w/2}" y="0" width="${w}" height="34" rx="17" fill="${SAGE}" ${o} stroke-width="4"/>${d}`;}
function babyTummy(lift,push,t,awake){ // side view, facing right, origin = floor under the chest
 const ch=-8-34*push;                       // chest height
 let s=`<path d="M-200 -6 Q-236 -30 -214 -60 Q-180 -78 -150 -52 L-140 -10 Z" fill="${PEACH}" ${o}/>`; // bottom + legs
 s+=`<path d="M-176 -8 Q-230 -4 -246 -26 Q-250 -42 -232 -44 Q-206 -36 -170 -30Z" fill="${PEACH}" ${o}/><circle cx="-248" cy="-32" r="15" fill="${BSK2}" ${o} stroke-width="4"/>`;
 s+=`<path d="M-200 -8 Q-190 ${-86-20*push} -70 ${ch-74} Q20 ${ch-84} 40 ${ch-30} L46 ${-6} Z" fill="${PEACH}" ${o}/>`;           // body
 s+=`<path d="M-120 ${ch-60} Q-60 ${ch-74} 10 ${ch-60}" stroke="${PL}" stroke-width="3" fill="none" opacity=".4"/>`;
 // forearm: elbow on the floor, hand forward; push straightens it
 const ex=10, ey=-8, hx=150, hy=-6-6*push;
 s+=`<path d="M${ex-10} ${ch-40} L${ex} ${ey}" stroke="${PL}" stroke-width="34" stroke-linecap="round"/><path d="M${ex-10} ${ch-40} L${ex} ${ey}" stroke="${PEACH}" stroke-width="25" stroke-linecap="round"/>`;
 s+=`<path d="M${ex} ${ey} L${hx-20} ${hy}" stroke="${PL}" stroke-width="30" stroke-linecap="round"/><path d="M${ex} ${ey} L${hx-20} ${hy}" stroke="${BSK2}" stroke-width="21" stroke-linecap="round"/><circle cx="${hx}" cy="${hy-4}" r="15" fill="${BSK2}" ${o} stroke-width="4"/>`;
 // head rotates up about the neck
 const nx=40, ny=ch-40, rot=-2-22*lift;
 s+=`<g transform="translate(${nx} ${ny}) rotate(${rot})">
  <circle cx="58" cy="-6" r="62" fill="${BSK2}" ${o}/>
  <path d="M22 -66 q18 -18 34 -2 q10 14 -6 20 q-14 4 -14 -10" stroke="#A0674A" stroke-width="4.5" fill="none" stroke-linecap="round"/>
  <path d="M30 -22 q-14 2 -12 18 q2 12 14 10" fill="${BSK2}" stroke="${PL}" stroke-width="4" stroke-linecap="round"/>
  ${awake?`<circle cx="92" cy="-12" r="7" fill="#5A2E22"/><circle cx="94" cy="-15" r="2.5" fill="#fff"/>`:`<path d="M84 -12 q9 7 18 0" stroke="#5A2E22" stroke-width="5" fill="none" stroke-linecap="round"/>`}
  <path d="M88 20 q14 14 28 0" stroke="#9A4E2A" stroke-width="5.5" fill="none" stroke-linecap="round"/>
  <circle cx="70" cy="16" r="11" fill="#FF9EA8" opacity=".6"/></g>`;
 return s;}
function babyAsleep(t){ // side view, on the back in a sleep sack on a flat mattress, origin = mattress top centre
 let s=`<rect x="-230" y="0" width="460" height="40" rx="14" fill="${CREAM}" ${o} stroke-width="4"/>`;
 s+=`<path d="M-120 -4 Q-130 -78 -40 -82 L120 -78 Q176 -70 170 -4 Z" fill="${PINK}" ${o}/><path d="M-60 -76 Q-50 -40 -66 -6 M40 -80 Q50 -44 36 -6" stroke="${PL}" stroke-width="3" fill="none" opacity=".4"/>`;
 s+=`<circle cx="-180" cy="-52" r="54" fill="${BSK2}" ${o}/><path d="M-218 -88 q14 -16 28 -2" stroke="#A0674A" stroke-width="4.5" fill="none" stroke-linecap="round"/>`;
 s+=`<path d="M-196 -60 q9 7 18 0" stroke="#5A2E22" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M-176 -26 q8 5 16 0" stroke="#9A4E2A" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="-160" cy="-44" r="9" fill="#FF9EA8" opacity=".6"/>`;
 for(let i=0;i<3;i++){const k=(t*0.6+i/3)%1;s+=`<text x="${-130+30*k+i*26}" y="${-120-70*k}" font-family="Caveat Brush" font-size="${36+14*k}" fill="${KICK2}" opacity="${Math.sin(Math.PI*k)}">z</text>`;}
 return s;}
const KICK2='#B23A62';
function adultReclined(lift,t){ // gate fix: adult PROPPED UP (about 35 degrees) on a big floor cushion, eyes OPEN, no blanket; baby tummy-down on the chest
 const d=[-0.819,-0.574], n=[0.574,-0.819];
 let s=`<path d="M-420 0 Q-450 -170 -390 -290 Q-340 -340 -280 -300 Q-200 -160 -100 0 Z" fill="${PINK}" ${o}/>`;           // floor cushion
 s+=`<path d="M-380 -260 Q-330 -160 -320 -30" stroke="${PL}" stroke-width="3" fill="none" opacity=".4"/>`;
 s+=`<path d="M-40 -34 L250 -34" stroke="${PL}" stroke-width="74" stroke-linecap="round"/><path d="M-40 -34 L250 -34" stroke="${BLUE}" stroke-width="64" stroke-linecap="round"/>`; // legs
 s+=`<ellipse cx="292" cy="-46" rx="30" ry="40" fill="${CREAM}" ${o} stroke-width="4"/>`;
 s+=`<g transform="translate(-60 -40) rotate(-145)"><rect x="-30" y="-72" width="290" height="144" rx="66" fill="${SAGE}" ${o}/></g>`; // torso
 const sh=[-60+d[0]*235,-40+d[1]*235];
 // arm (drawn BEFORE the baby, so the baby sits on top): along the chest, hand on baby's back/bottom
 const cp=[-60+d[0]*125+n[0]*68, -40+d[1]*125+n[1]*68];
 const hand=[cp[0]+n[0]*40-d[0]*110, cp[1]+n[1]*40-d[1]*110];
 s+=`<path d="M${sh[0]+20} ${sh[1]+40} Q${sh[0]+120} ${sh[1]+130} ${hand[0]} ${hand[1]}" stroke="${PL}" stroke-width="40" fill="none" stroke-linecap="round"/><path d="M${sh[0]+20} ${sh[1]+40} Q${sh[0]+120} ${sh[1]+130} ${hand[0]} ${hand[1]}" stroke="${SAGE}" stroke-width="31" fill="none" stroke-linecap="round"/>`;
 s+=`<rect x="${sh[0]-24}" y="${sh[1]-58}" width="48" height="60" rx="14" fill="${SK}" ${o} transform="rotate(-55 ${sh[0]} ${sh[1]})"/>`;  // neck
 const hx=sh[0]-36, hy=sh[1]-58;
 s+=`<circle cx="${hx}" cy="${hy}" r="64" fill="${SK}" ${o}/>`;
 s+=`<path d="M${hx-62} ${hy+10} Q${hx-80} ${hy-80} ${hx-6} ${hy-66} Q${hx+50} ${hy-60} ${hx+60} ${hy-24} Q${hx+20} ${hy-44} ${hx-20} ${hy-36} Q${hx-46} ${hy-20} ${hx-62} ${hy+10}Z" fill="#8A5A44" ${o}/>`;
 s+=`<circle cx="${hx+32}" cy="${hy-2}" r="9" fill="#5A2E22"/><circle cx="${hx+35}" cy="${hy-5}" r="3" fill="#fff"/>`;              // OPEN eye
 s+=`<path d="M${hx+22} ${hy+32} q14 12 30 -2" stroke="#9A4E2A" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="${hx+12}" cy="${hy+18}" r="11" fill="#FF9EA8" opacity=".6"/>`;
 s+=`<g transform="translate(${cp[0]} ${cp[1]}) rotate(35) scale(-.74 .74)">`+babyTummy(lift,0.3,t,true)+`</g>`;
 s+=`<circle cx="${hand[0]}" cy="${hand[1]}" r="20" fill="${SK}" ${o} stroke-width="4"/>`;
 return s;}
function timerRing(cx,cy,r,k){const C=2*Math.PI*r;return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${CREAM}" stroke-width="22"/><circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${CORAL}" stroke-width="22" stroke-linecap="round" stroke-dasharray="${C}" stroke-dashoffset="${C*(1-k)}" transform="rotate(-90 ${cx} ${cy})"/>`;}
function archCard(inner,skyTop,skyBot,ky){ // the arch card: soft sky inside, the scene clipped to the arch
 return `<defs><linearGradient id="ag" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${skyTop}"/><stop offset="1" stop-color="${skyBot}"/></linearGradient>
  <clipPath id="ac"><path d="${archPath(AX,AY,AW,AH)}"/></clipPath></defs>
  <path d="${archPath(AX+10,AY+14,AW,AH)}" fill="rgba(107,59,90,.12)"/>
  <path d="${archPath(AX,AY,AW,AH)}" fill="url(#ag)"/>
  <g clip-path="url(#ac)">${inner}</g>
  <path d="${archPath(AX,AY,AW,AH)}" fill="none" stroke="${PL}" stroke-width="5"/>
  <path d="${archPath(AX+18,AY+18,AW-36,AH-36)}" fill="none" stroke="${CREAM}" stroke-width="4" stroke-dasharray="2 14" stroke-linecap="round" opacity=".9"/>`;}
function mix(a,b,k){const pa=[1,3,5].map(i=>parseInt(a.substr(i,2),16)),pb=[1,3,5].map(i=>parseInt(b.substr(i,2),16));return '#'+pa.map((v,i)=>Math.round(v+(pb[i]-v)*k).toString(16).padStart(2,'0')).join('');}
const SCN=[];
SCN[0]=(lt,t)=>{ // asleep on the back (lilac) -> awake on the tummy (butter): a sun-wipe across the arch
 const w=EIO(seg(lt,1.05,1.75)); const cx=AX+AW/2, fy=AY+AH-70;
 let inner=`<rect x="${AX}" y="${AY+AH-70}" width="${AW}" height="70" fill="#FFE9C9"/>`;
 const sleep=`<g transform="translate(${cx} ${fy-30})">${babyAsleep(t)}</g>`+label(cx,AY+150,'asleep: on their back',-3,50);
 const lift=E(seg(lt,1.55,2.3))*(0.85+0.15*Math.sin(t*3));
 const awake=`<g transform="translate(${cx} ${fy})">${matSVG(560)}</g><g transform="translate(${cx+20} ${fy})">${babyTummy(lift,0.15,t,true)}</g>`
   +`<g transform="translate(${cx+230} ${fy-40}) rotate(${10*Math.sin(t*4)})"><circle r="30" fill="${BUT}" ${o} stroke-width="4"/><path d="M0 -4 c-5 -9 -18 -4 -13 5 l13 11 l13 -11 c5 -9 -8 -14 -13 -5z" fill="${PINK}" stroke="${PL}" stroke-width="2.5"/><path d="M0 30 V56" stroke="${PL}" stroke-width="8" stroke-linecap="round"/></g>`
   +label(cx,AY+150,'awake: tummy time',-3,50);
 inner+=`<g opacity="${1-w}">${sleep}</g><g opacity="${w}">${awake}</g>`;
 inner+=`<rect x="${AX-200+1100*w}" y="${AY}" width="160" height="${AH}" fill="#FFF6D8" opacity="${0.6*Math.sin(Math.PI*w)}" transform="skewX(-10)"/>`;
 return archCard(inner, mix('#D9D3F2','#FFF0C8',w), mix('#F6E0EC','#FFE2B8',w));};
SCN[1]=(lt,t)=>{ // countdown: small tummy-time vignette under the numeral text
 const cx=540, fy=1360; const lift=0.55+0.45*Math.sin(t*2.4)**2;
 let s=`<g transform="translate(${cx} ${fy})">${matSVG(620)}</g><g transform="translate(${cx+30} ${fy})">${babyTummy(lift,0.2,t,true)}</g>`;
 s+=`<g transform="translate(${cx+330} ${fy-110})">`+`<circle r="58" fill="${CREAM}" ${o} stroke-width="4"/>`+timerRing(0,0,40,seg(lt,0.2,2.8))+`</g>`;
 s+=label(cx-250,fy-120,'awake + watched',-4,50);
 return s;};
SCN[2]=(lt,t)=>{ // push-up + rosettes
 const cx=AX+AW/2, fy=AY+AH-70; const push=EIO(seg(lt,0.15,0.9)), lift=0.6+0.4*E(seg(lt,0.15,0.9));
 let inner=`<rect x="${AX}" y="${fy}" width="${AW}" height="70" fill="#FFE9C9"/><g transform="translate(${cx} ${fy})">${matSVG(560)}</g><g transform="translate(${cx+40} ${fy})">${babyTummy(lift,push,t,true)}</g>`;
 for(let i=0;i<3;i++) inner+=sparkle(cx-200+i*130,AY+170+((i*37)%40),0.6+0.3*Math.sin(t*5+i),seg(lt,0.8+i*0.2,1.1+i*0.2));
 let s=archCard(inner,'#FFF0C8','#FFE2B8');
 s+=rosette(175,965,PINK,'head up',seg(lt,0.9,1.4),t)+rosette(905,965,BUT,'strong arms',seg(lt,1.4,1.9),t)+rosette(905,1225,BLUE,'round head',seg(lt,1.9,2.4),t);
 return s;};
SCN[3]=(lt,t)=>{ // do this: parent lies back, baby on the chest lifts their head to look at them; hearts
 const cx=AX+AW/2+20, fy=AY+AH-90; const lift=0.5+0.5*E(seg(lt,0.2,1.0))*(0.8+0.2*Math.sin(t*2.5));
 let inner=`<rect x="${AX}" y="${fy+20}" width="${AW}" height="90" fill="#FFE9C9"/><g transform="translate(${cx+20} ${fy+50}) scale(.95)">${adultReclined(lift,t)}</g>`;
 inner+=hearts(t,cx+130,fy-210);
 return archCard(inner,'#FFF0C8','#FFE2B8');};
let SC_COVER=false;
function draw(t){
 T=t; const S=SPEC, starts=S.starts, n=S.durs.length; let i=0; for(let k=0;k<n;k++) if(t>=starts[k]) i=k;
 let lt=t-starts[i]; if(S.cover){i=S.coverBeat; lt=S.coverLt;}
 let svg=blobsBG(t);
 // light-leak flash at each cut
 if(!S.cover&&i>0&&lt<0.35){svg+=`<rect x="0" y="0" width="1080" height="1920" fill="#FFF6D8" opacity="${0.55*(1-lt/0.35)}"/>`;}
 // camera: gentle push-in per beat; slam shake on beat 3
 let cam=1+0.03*seg(lt,0,S.durs[i]); let sh=0; if(!S.cover&&i==3&&lt<0.4){sh=14*Math.sin(lt*60)*(1-lt/0.4);}
 svg+=`<g transform="translate(${540+sh} 1100) scale(${cam}) translate(-540 -1100)">`+SCN[i](lt,t)+`</g>`;
 document.getElementById('art').innerHTML=svg;
 const ENTER=['none','zoom','whip','slam'];
 for(let k=0;k<n;k++){const el=document.getElementById('b'+k); if(!el) continue; let op=0, tr='';
  if(S.cover){op=0;} else if(k==i){ const e=ENTER[i];
    if(e=='none'){op=1;}
    else if(e=='zoom'){const p=E(seg(lt,0,0.28)); op=p; tr=`scale(${1.35-0.35*p})`;}
    else if(e=='whip'){const p=E(seg(lt,0,0.26)); op=Math.min(1,p*2); tr=`translateX(${900*(1-p)}px) skewX(${-12*(1-p)}deg)`;}
    else if(e=='slam'){const p=seg(lt,0,0.22); op=Math.min(1,p*3); const y=-260*(1-p*p); tr=`translateY(${y}px) scale(${1+0.08*(1-p)})`;} }
  else if(!S.cover && k==i-1 && lt<0.12){const p=seg(lt,0,0.12); op=1-p; const e=ENTER[i];
    tr= e=='whip'?`translateX(${-700*p}px)`: e=='slam'?`translateY(${120*p}px)`:`scale(${1-0.2*p})`;}
  el.style.opacity=op; el.style.transform=tr; el.style.transformOrigin='540px 600px';}
 for(let k=0;k<n;k++){const c=document.getElementById('c'+k); if(c) c.style.opacity=(!S.cover&&k==i)?(i==0?(t<0.3?0:Math.min(1,(t-0.3)/0.2)):1):0;}
 const f=document.getElementById('follow'); if(f){const p=(S.cover||i!=n-1)?0:E(seg(lt,1.0,1.4)); f.style.opacity=p; f.style.transform=`translateY(${30*(1-p)}px)`;}
 const num=document.getElementById('num'); if(num&&!S.cover&&i==1){const p=seg(lt,0.05,0.45); num.style.transform=`scale(${0.6+0.4*E(p)+0.06*Math.sin(Math.PI*cl(p*1.3,0,1))}) rotate(${-4+4*E(p)}deg)`;}
}
"""


def html(spec, cover=None):
    T = ""
    for k, b in enumerate(spec["beats"]):
        inner = f'<div class="hand" style="position:absolute;left:90px;width:900px;top:{b.get("ky", 330)}px;font-size:66px;color:{KICK}">{b["kick"]}</div>'
        if b.get("num"):
            inner += (f'<div id="num" style="position:absolute;left:0;right:0;top:380px;text-align:center;transform-origin:540px 260px">'
                      f'<span class="S" style="display:inline-block;font-size:560px;line-height:.9;color:{INK};position:relative">'
                      f'<span style="position:absolute;left:50%;top:52%;width:430px;height:430px;margin:-215px 0 0 -215px;border-radius:50%;background:#FFBFD3;z-index:-1"></span>{b["num"]}</span></div>')
            inner += K.dual(b["head"], F, cls="S fit", style=f"position:absolute;left:90px;width:900px;top:{b.get('hy', 900)}px;white-space:nowrap;font-size:{b.get('fs', 110)}px;color:{INK}")
        else:
            inner += K.dual(b["head"], F, cls="S fit", style=f"position:absolute;left:90px;width:900px;top:{b.get('hy', 410)}px;white-space:nowrap;font-size:{b.get('fs', 140)}px;color:{INK}")
        if b.get("sub"):
            inner += (f'<div class="lora" style="position:absolute;left:70px;width:940px;top:{b.get("sy", 770)}px;font-size:{b.get("ss", 46)}px;'
                      f'line-height:1.2;text-align:center;color:{INK}">{b["sub"]}</div>')
        T += f'<div id="b{k}" style="position:absolute;left:0;top:0;width:{W}px;height:1400px;opacity:0;z-index:4">{inner}</div>'
        T += f'<div id="c{k}" style="position:absolute;left:0;right:0;top:1440px;text-align:center;opacity:0;z-index:4"><span class="chipf" style="font-size:28px">{b["chip"]}</span></div>'
    cv = ""
    if cover:
        cv = (f'<div class="hand" style="position:absolute;left:90px;width:900px;top:330px;font-size:76px;color:{KICK};z-index:4">{cover["kick"]}</div>'
              + K.dual(cover["head"], F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:420px;white-space:nowrap;font-size:{cover.get('fs', 160)}px;color:{INK};z-index:4"))
    follow = (f'<div id="follow" style="position:absolute;left:0;right:0;top:735px;text-align:center;opacity:0;z-index:5">'
              f'<span style="display:inline-block;max-width:820px;padding:16px 36px;border-radius:40px;background:{INK};color:#FFF8EE;font:600 34px/1.25 Poppins">{spec["follow"]}</span></div>')
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4 0%,#FFF4E0 55%,#FFEBD2 100%)"></div>'
            f'<svg id="art" style="position:absolute;left:0;top:0;z-index:2" width="{W}" height="{H}" viewBox="0 0 {W} {H}"></svg>'
            '<div class="grain" style="opacity:.3;z-index:3"></div>'
            + T + cv + follow + K.stamp(B, 46, 1500, size=120, rot=-10).replace('class="stamp" style="', 'class="stamp" style="z-index:5;')
            + f"<script>{RS.JS}</script>")
    return RS.page(W, H, body)


RS.html = html

SPEC = dict(
    out="lf-reel-1029-tummy-to-play", music=MUSIC, follow=FOLLOW, scene="coat", garments=["none"] * 5,
    durs=[5 * BP, 5 * BP, DROP - 10 * BP, 14.4 - DROP], extra_pops=[], cover_beat=0, cover_lt=2.6,
    cover=dict(kick="asleep or awake?", head="Back to sleep. / *Tummy to play.*", fs=150),
    beats=[
        dict(kick="asleep or awake?", head="Back to sleep. / *Tummy to play.*", fs=140, chip=CHIP_AAP),
        dict(kick="start the day you get home", num="3", head="minutes, / *2 to 3 times a day.*", fs=104, hy=920, chip=CHIP_AAP),
        dict(kick="why it matters", head="Strong muscles. / *Fewer flat spots.*", fs=132, chip=CHIP_CPS),
        dict(kick="Do this:", head="Recline. / *Baby on your chest.*", sub="Only while you're awake and watching.", fs=120, sy=652, ss=44, chip=CHIP_AAP),
    ])

if __name__ == "__main__":
    for a in sys.argv:
        if a.startswith("--still="):
            RS.STILLS = [float(x) for x in a[8:].split(",")]
        if a.startswith("--sw="):
            RS.SW = int(a[5:])
    s = SPEC
    OUT.mkdir(parents=True, exist_ok=True)
    RS.frames(s, "tummy", cover=s["cover"], cover_out=OUT / f"{s['out']}-cover.jpg")
    print("cover", OUT / f"{s['out']}-cover.jpg", flush=True)
    if "--cover-only" not in sys.argv:
        r = RS.frames(s, "tummy")
        if r is None:
            print("stills", RS.SCR / "tummy-stills.jpg")
        else:
            fdir, total, starts = r
            pops = [(st + 0.1, 0.22) for k, st in enumerate(starts) if k > 0]
            out = OUT / f"{s['out']}.mp4"
            RS.encode(fdir, total, s["music"], pops, out)
            print(out, round(total, 2), flush=True)

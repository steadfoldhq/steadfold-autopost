#!/usr/bin/env python3
"""Locked Hour, Nov 2 studio build (Social studio, Mon Nov 2 2026). Extends studio/editorial/nov01_lockedhour.py
(imported, not edited: its page(), draw() gate fix and JS helpers are reused; this file appends its own scenes to
n1.JS_NOV at runtime).

Hook model: the Nov 1 winner "Shower 90 minutes before bed." = a number you can do tonight + one action + one drawn object.

  getup    lh-reel-1104-get-up-20     Wed Nov 4 19:00 ET. "Can't sleep", Part 1. Object: the bed (+ reading chair).
           Schutte-Rodin et al. 2008, J Clin Sleep Med 4(5):487-504 (stimulus control, ~20 minutes, Standard);
           Edinger et al. 2021, J Clin Sleep Med 17(2):263-298 (AASM review).
  workout  lh-reel-1105-workout-1h    Thu Nov 5 19:00 ET. Part 2 (promised by A). Object: a dumbbell.
           Stutz, Eiholzer & Spengler 2019, Sports Medicine 49(2):269-287 (doi 10.1007/s40279-018-1015-0).
  sigh     lh-reel-1105am-slow-sighs  Thu Nov 5 08:00 ET, trial "auto", standalone. Object: a breath gauge + 5-minute sand timer.
           Balban et al. 2023, Cell Reports Medicine 4(1):100895 (doi 10.1016/j.xcrm.2022.100895).

  python3 studio/editorial/nov02_lockedhour.py getup|workout|sigh [--cover-only] [--still=0,1.5,3]
Music: existing LH v4 library tracks only (tools/music-library.json), loudnorm -14 LUFS. No new music. 1 render worker.
"""
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
os.environ["LH_SCR"] = "/tmp/claude-0/nov02-lockedhour"
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import edkit  # noqa: E402
import oct27_lockedhour as k27  # noqa: E402
import oct28_lockedhour as k28  # noqa: E402  (SCR fixed to the nov02 scratch dir here)
import nov01_lockedhour as n1  # noqa: E402

OUT = REPO / "media/studio-nov02/lockedhour"
OUT.mkdir(parents=True, exist_ok=True)
k28.OUT = OUT
FOLLOW_NEW = "Follow for one small<br>sleep or focus trick a day."


def page(spec, cover_html=None):
    """n1.page() with the gate-approved follow line (Nov 2 gate: sleep/stress Reels)."""
    h = n1.page(spec, cover_html)
    assert "Follow for one small<br>focus trick a day." in h
    return h.replace("Follow for one small<br>focus trick a day.", FOLLOW_NEW)


k28.page = page
SCR = k28.SCR
CSS = k27.CSS

JS_NOV2 = r"""
// ================= Nov 2 extras =================
const BROWN='#7A4A2E', SKY='#8FC8EE', NIGHT2='#4A3F78';
const lerp=(a,b,k)=>a+(b-a)*k;
function person(x,y,s,rot,lid,look,smile,t){return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">`+recol(face(0,0,1,lid,look,smile,t),BROWN,'#FFBAD6')+`</g>`;}
// ---------- SCENE A: the bed + the reading chair ----------
function lampSmall(x,y,on){let s='';
 if(on>0) s+=`<circle cx="${x}" cy="${y-60}" r="${150+30*on}" fill="#FFE9A8" opacity="${0.55*on}"/><circle cx="${x}" cy="${y-60}" r="80" fill="#FFF3C4" opacity="${0.6*on}"/>`;
 s+=`<path d="M${x} ${y} V${y-70}" stroke="${INK}" stroke-width="9"/>`+sh(`<ellipse cx="${x}" cy="${y}" rx="34" ry="10" fill="${CR}" ${o}/>`,5);
 s+=sh(`<path d="M${x-48} ${y-66} L${x-30} ${y-130} H${x+30} L${x+48} ${y-66}Z" fill="${on>0.5?HY:'#E6DCCB'}" ${o}/>`,7);
 return s;}
function alarmClock(x,y,s,flip){ // flip 0 = face out, 1 = turned to the wall
 const sx=Math.cos(Math.PI*flip); const back=flip>0.5;
 let g=`<path d="M-40 -56 l-18 -20 M40 -56 l18 -20" stroke="${INK}" stroke-width="9" stroke-linecap="round"/>`+sh(`<circle r="62" fill="${back?'#E6DCCB':HY}" ${o}/>`,7);
 if(!back) g+=`<circle r="46" fill="${CR}" stroke="${INK}" stroke-width="5"/><path d="M0 0 V-32" stroke="${INK}" stroke-width="7" stroke-linecap="round"/><path d="M0 0 L22 10" stroke="${DP}" stroke-width="7" stroke-linecap="round"/><circle r="6" fill="${INK}"/>`;
 else g+=`<circle r="20" fill="${CR2}" stroke="${INK}" stroke-width="5"/>`;
 g+=`<path d="M-40 56 l-10 18 M40 56 l10 18" stroke="${INK}" stroke-width="8" stroke-linecap="round"/>`;
 return `<g transform="translate(${x} ${y}) scale(${s*Math.max(0.06,Math.abs(sx))} ${s})">${g}</g>`;}
function chairBack(x,y){return sh(`<rect x="${x-130}" y="${y-200}" width="260" height="300" rx="70" fill="${HY}" ${o}/>`,10);}
function chairFront(x,y){let s=sh(`<rect x="${x-120}" y="${y+70}" width="240" height="90" rx="30" fill="${HY}" ${o}/>`,8);
 s+=sh(`<rect x="${x-165}" y="${y-30}" width="60" height="200" rx="28" fill="${HY}" ${o}/><rect x="${x+105}" y="${y-30}" width="60" height="200" rx="28" fill="${HY}" ${o}/>`,8);
 s+=`<path d="M${x-110} ${y+160} V${y+210} M${x+110} ${y+160} V${y+210}" stroke="${INK}" stroke-width="12" stroke-linecap="round"/>`;
 return s;}
function bookOpen(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})">`+sh(`<path d="M0 0 L-90 -14 V-80 L0 -66Z" fill="#FFFFFF" ${o}/><path d="M0 0 L90 -14 V-80 L0 -66Z" fill="#FFFFFF" ${o}/>`,6)+
 [0,1,2].map(i=>`<path d="M-74 ${-58+i*16} L-18 ${-50+i*16}" stroke="${INK}" stroke-width="4" opacity=".35"/><path d="M18 ${-50+i*16} L74 ${-58+i*16}" stroke="${INK}" stroke-width="4" opacity=".35"/>`).join('')+`</g>`;}
function bedroom(t,o2){ // o2: {p:0 bed..1 chair, lid, look, smile, lamp, clockFlip, blanket(1 on..0 off), book}
 let s='';
 s+=sh(`<rect x="110" y="820" width="860" height="880" rx="26" fill="${CR2}" ${o}/>`,12);
 s+=`<rect x="190" y="880" width="250" height="200" rx="10" fill="${NIGHT2}" ${o}/><path d="M315 880 V1080 M190 980 H440" stroke="${INK}" stroke-width="7"/>`+`<g transform="translate(380 940) scale(.32)">`+moonD(0,0,1)+`</g>`;
 s+=`<path d="M116 1640 H964" stroke="${INK}" stroke-width="6" opacity=".35"/>`;
 // lamp glow first (behind furniture)
 // bed (side view)
 s+=sh(`<rect x="140" y="1250" width="44" height="390" rx="18" fill="${HP}" ${o}/>`,10);
 s+=sh(`<rect x="150" y="1460" width="400" height="74" rx="22" fill="${CR}" ${o}/>`,10);
 s+=`<path d="M190 1534 V1630 M520 1534 V1630" stroke="${INK}" stroke-width="12" stroke-linecap="round"/>`;
 s+=`<ellipse cx="250" cy="1440" rx="72" ry="30" fill="#FFFFFF" ${o}/>`;
 // nightstand + lamp + clock
 s+=sh(`<rect x="565" y="1500" width="120" height="24" rx="8" fill="${HY}" ${o}/>`,7)+`<path d="M585 1524 V1630 M665 1524 V1630" stroke="${INK}" stroke-width="10" stroke-linecap="round"/>`;
 s+=lampSmall(595,1500,o2.lamp);
 s+=alarmClock(655,1458,0.5,o2.clockFlip||0);
 // chair
 const cx=830, cy=1420;
 s+=chairBack(cx,cy);
 // person: lerp bed -> chair along an arc
 const p=o2.p, px=lerp(255,cx,p), py=lerp(1400,cy-40,p)-150*Math.sin(Math.PI*p), rot=lerp(-90,0,EIO(p)), sc=lerp(0.42,0.55,p);
 const inChair=p>0.5;
 if(!inChair){ s+=person(px,py,sc,rot,o2.lid,o2.look,o2.smile,t); }
 // blanket: on = covering the body; off = folded at the foot
 const bk=o2.blanket;
 if(bk>0.5) s+=sh(`<path d="M300 1398 Q380 1370 470 1384 Q540 1392 552 1400 Q560 1440 552 1470 H296 Q286 1430 300 1398Z" fill="${HY}" ${o}/>`,8)+`<path d="M360 1392 Q380 1430 372 1468 M450 1388 Q470 1430 462 1468" stroke="${HP}" stroke-width="9" fill="none" stroke-linecap="round" opacity=".8"/>`;
 else s+=sh(`<path d="M440 1430 Q500 1412 556 1424 Q566 1450 556 1474 H436 Q430 1450 440 1430Z" fill="${HY}" ${o}/>`,6)+`<path d="M470 1428 Q484 1450 478 1472" stroke="${HP}" stroke-width="8" fill="none" stroke-linecap="round" opacity=".8"/>`;
 if(inChair){ s+=person(px,py,sc,rot,o2.lid,o2.look,o2.smile,t); if(o2.book>0) s+=`<g opacity="${o2.book}">`+bookOpen(cx,cy+92,0.9)+`</g>`; }
 s+=chairFront(cx,cy);
 return s;}
// pill label that stays inside the frame
function pl(x,y,txt,size,col,rot){return pillLab(x,y,txt,size||54,col,rot);}
function chairIcon(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})">`+chairBack(0,0)+chairFront(0,0)+`</g>`;}
function arcArrow(x1,x2,y,h,k,col,up){ if(k<=0) return ''; const dir=up?-1:1, mx=(x1+x2)/2, cy=y+dir*h;
 const d=`M${x1} ${y} Q${mx} ${cy} ${x2} ${y}`;
 const L=Math.abs(x2-x1)*1.4+h; const ang=Math.atan2(y-cy,x2-mx);
 let s=`<path d="${d}" stroke="${col}" stroke-width="14" fill="none" stroke-linecap="round" stroke-dasharray="${L}" stroke-dashoffset="${L*(1-E(k))}"/>`;
 if(k>0.85){const a=ang, hx=x2, hy=y; s+=`<path d="M${hx-40*Math.cos(a-0.5)} ${hy-40*Math.sin(a-0.5)} L${hx} ${hy} L${hx-40*Math.cos(a+0.5)} ${hy-40*Math.sin(a+0.5)}" stroke="${col}" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;}
 return s;}
SC.getup=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==0){
  const p=EIO(seg(t,1.05,1.6));
  s+=bedroom(t,{p:p,lid:p>0.6?0:0,look:t<1.0?Math.sin(t*6):0,smile:p>0.6?0.6:-0.2,lamp:E(seg(t,1.0,1.15)),clockFlip:0,blanket:t<1.05?1:0,book:seg(t,1.7,2.0)});
  if(t<1.0) s+=pl(560,1180,'still awake…',58);
  if(t>1.55) s+=`<g opacity="${Q(t,1.55)}">`+pl(560,1180,'get up',62)+`</g>`;
  s+=burst(830,1300,seg(t,1.6,2.1),HY);
  return s;}
 if(ph==1){ // in the chair, dim lamp, gets sleepy, back to bed
  const back=EIO(seg(t,4.5,5.0));
  const lid=t<4.5?0.25+0.6*seg(t,3.2,4.3):(back>0.9?1:0.85);
  s+=bedroom(t,{p:1-back,lid:lid,look:0,smile:0.5,lamp:1-E(seg(t,4.95,5.1)),clockFlip:0,blanket:back>0.95?1:0,book:1-seg(t,4.4,4.6)});
  if(t>2.6&&t<4.4) s+=`<g opacity="${Q(t,2.6)}">`+pl(560,1180,'dim lamp, dull book',54)+`</g>`;
  if(t>4.4) s+=`<g opacity="${Q(t,4.4)}">`+pl(560,1180,'sleepy? back to bed',54)+`</g>`;
  if(t>5.05) s+=`<g transform="translate(-200 120)">`+zz(470,1210,t,5.05)+`</g>`;
  return s;}
 if(ph==2){ // the loop: bed -> (not asleep in ~20 min) -> chair -> (sleepy) -> bed
  const a=pop(seg(t,5.6,5.85)), b=pop(seg(t,5.8,6.05));
  if(a>0) s+=`<g transform="translate(290 1360) scale(${a*1.25})">`+bedIcon(0,0,1)+`</g>`;
  if(b>0) s+=`<g transform="translate(790 1380) scale(${b*0.55})">`+chairIcon(0,0,1)+`</g>`;
  s+=arcArrow(330,760,1200,190,seg(t,6.1,6.6),DP,true);
  if(t>6.4) s+=`<g opacity="${Q(t,6.4)}">`+pl(545,1000,'not asleep in about 20 minutes',50)+`</g>`;
  s+=arcArrow(760,330,1560,150,seg(t,6.9,7.4),INK,false);
  if(t>7.2) s+=`<g opacity="${Q(t,7.2)}">`+pl(545,1680,'sleepy again',54,INK)+`</g>`;
  if(t>7.6) s+=zz(330,1240,t,7.6);
  return s;}
 if(ph==3){ // do this: clock turned to the wall, then up to the chair
  const flip=EIO(seg(t,9.3,9.7)), p=EIO(seg(t,10.3,10.8));
  s+=bedroom(t,{p:p,lid:0,look:0,smile:p>0.5?0.6:0,lamp:E(seg(t,10.2,10.35)),clockFlip:flip,blanket:t<10.3?1:0,book:seg(t,10.8,11.0)});
  if(t>9.6&&t<10.4) s+=`<g opacity="${Q(t,9.6)}">`+pl(560,1180,'hide the clock, guess the 20 minutes',46)+`</g>`;
  if(t>10.9) s+=check(830,1180,seg(t,10.9,11.3),44);
  return s;}
 s+=`<g transform="translate(540 1400) scale(.62) translate(-540 -1270)">`+bedroom(t,{p:1,lid:0.4,look:0,smile:0.6,lamp:1,clockFlip:1,blanket:0,book:1})+`</g>`;
 return s;};

// ---------- SCENE B: the dumbbell ----------
function dumbbell(x,y,s,rot){return `<g transform="translate(${x} ${y}) rotate(${rot||0}) scale(${s})">`+
 sh(`<rect x="-150" y="-14" width="300" height="28" rx="12" fill="#E6DCCB" ${o}/>`,6)+
 sh(`<rect x="-150" y="-62" width="44" height="124" rx="14" fill="${HP}" ${o}/><rect x="-104" y="-48" width="30" height="96" rx="12" fill="${HP}" ${o}/>`,7)+
 sh(`<rect x="106" y="-62" width="44" height="124" rx="14" fill="${HP}" ${o}/><rect x="74" y="-48" width="30" height="96" rx="12" fill="${HP}" ${o}/>`,7)+`</g>`;}
function lifter(x,y,s,lift,lid,smile,t,sweat){ // front-facing person pressing a dumbbell overhead; lift 0 (at chest) .. 1 (overhead), -1 = no dumbbell
 let g='';
 const hy=lift<0?150:lerp(-245,-340,lift);
 if(lift>=0){
  g+=`<path d="M-108 210 Q-170 ${hy+120} -150 ${hy}" stroke="${INK}" stroke-width="56" fill="none" stroke-linecap="round"/><path d="M-108 210 Q-170 ${hy+120} -150 ${hy}" stroke="#FFE3C8" stroke-width="40" fill="none" stroke-linecap="round"/>`;
  g+=`<path d="M108 210 Q170 ${hy+120} 150 ${hy}" stroke="${INK}" stroke-width="56" fill="none" stroke-linecap="round"/><path d="M108 210 Q170 ${hy+120} 150 ${hy}" stroke="#FFE3C8" stroke-width="40" fill="none" stroke-linecap="round"/>`;
 }
 g+=recol(face(0,0,1,lid,0,smile,t),BROWN,'#8FC8EE');
 if(lift>=0) g+=dumbbell(0,hy,1.12,0);
 if(sweat>0) [[-150,-60],[160,-20],[130,-120]].forEach(([dx,dy],i)=>{const k=((t*1.6+i*0.33)%1); g+=`<path d="M${dx} ${dy+40*k} q-14 24 0 32 q14 -8 0 -32z" fill="#BFE3F2" stroke="${INK}" stroke-width="4" opacity="${sweat*(1-k)}"/>`;});
 return `<g transform="translate(${x} ${y}) scale(${s})">${g}</g>`;}
function heartD(x,y,k,beat){const j=Math.max(0,Math.sin(T*14))*beat; // pulse line + zap marks (not a heart)
 return `<g transform="translate(${x} ${y}) scale(${k})">`+`<path d="M-90 0 H-40 L-22 ${-40-20*j} L-2 ${40+10*j} L16 -20 L30 0 H90" stroke="${DP}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`+
  `<path d="M-70 -70 l-16 -22 M0 -86 v-26 M70 -70 l16 -22" stroke="${INK}" stroke-width="8" stroke-linecap="round" opacity="${0.5+0.5*j}"/></g>`;}
function gym(t,lift,lid,smile,sweat){let s='';
 s+=sh(`<rect x="110" y="820" width="860" height="880" rx="26" fill="${CR2}" ${o}/>`,12);
 s+=`<rect x="680" y="880" width="230" height="190" rx="10" fill="${NIGHT2}" ${o}/><path d="M795 880 V1070 M680 975 H910" stroke="${INK}" stroke-width="7"/>`+`<g transform="translate(860 930) scale(.28)">`+moonD(0,0,1)+`</g>`;
 s+=sh(`<path d="M170 1600 L230 1560 H850 L910 1600Z" fill="${HPL}" ${o}/>`,8);
 s+=lifter(540,1400,0.82,lift,lid,smile,t,sweat);
 return s;}
function bedScene(t,lid,smile,awake){let s='';
 s+=sh(`<rect x="110" y="820" width="860" height="880" rx="26" fill="${CR2}" ${o}/>`,12);
 s+=`<rect x="680" y="880" width="230" height="190" rx="10" fill="${NIGHT2}" ${o}/><path d="M795 880 V1070 M680 975 H910" stroke="${INK}" stroke-width="7"/>`+`<g transform="translate(860 930) scale(.28)">`+moonD(0,0,1)+`</g>`;
 s+=sh(`<rect x="160" y="1300" width="44" height="340" rx="18" fill="${HP}" ${o}/>`,10)+sh(`<rect x="170" y="1470" width="740" height="74" rx="22" fill="${CR}" ${o}/>`,10);
 s+=`<path d="M210 1544 V1630 M880 1544 V1630" stroke="${INK}" stroke-width="12" stroke-linecap="round"/><ellipse cx="290" cy="1450" rx="80" ry="32" fill="#FFFFFF" ${o}/>`;
 s+=`<g transform="translate(300 1408) rotate(-90) scale(.46)">`+recol(face(0,0,1,lid,awake?Math.sin(t*7):0,smile,t),BROWN,'#8FC8EE')+`</g>`;
 s+=sh(`<path d="M360 1404 Q520 1372 700 1390 Q860 1400 910 1408 Q920 1440 910 1480 H356 Q344 1440 360 1404Z" fill="${HY}" ${o}/>`,8);
 if(awake) s+=heartD(840,1290,1,1);
 return s;}
function tlRow(t){ // evening timeline 7 pm .. 11 pm (bed): any workout fine up to 10; 10-11: only easy ones
 let s='';
 const x0=150, x1=930, X=h=>x0+(x1-x0)*(h-19)/4;
 const g=EIO(seg(t,5.7,6.3)), z=EIO(seg(t,6.4,7.0));
 s+=sh(`<rect x="${x0}" y="1290" width="${(X(22)-x0)*g}" height="90" rx="20" fill="${HY}" ${o}/>`,8);
 if(z>0) s+=sh(`<rect x="${X(22)+8}" y="1290" width="${(x1-X(22)-8)*z}" height="90" rx="20" fill="${HPL}" ${o}/>`,8);
 ['7 pm','8','9','10','11'].forEach((h,i)=>{const xx=X(19+i); if(g>0.2*i) s+=`<text x="${xx}" y="1450" font-family="Inter" font-weight="800" font-size="46" fill="${INK}" text-anchor="middle">${h}</text><path d="M${xx} 1385 v20" stroke="${INK}" stroke-width="6"/>`;});
 if(t>6.0) s+=`<g opacity="${Q(t,6.0)}">`+dumbbell(X(20.5),1210,0.5,0)+pl(X(20.5),1130,'hard workout: fine',50)+`</g>`;
 if(t>6.9) s+=`<g opacity="${Q(t,6.9)}">`+pl(760,1560,'only easy stuff',54,INK)+`</g>`;
 if(t>6.6) s+=`<g transform="translate(870 1205) scale(.55)">`+bedIcon(0,0,1)+`</g>`;
 if(t>7.3) s+=`<path d="M${X(22)} 1270 V1400" stroke="${DP}" stroke-width="10" stroke-dasharray="18 12" opacity="${Q(t,7.3)}"/>`+`<text x="${X(22.5)+4}" y="1354" font-family="Inter Display" font-weight="900" font-size="50" fill="${INK}" text-anchor="middle" opacity="${Q(t,7.3)}">1 hour</text>`;
 return s;}
SC.workout=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==0){ // pressing fast, sweat; 10 pm tag; dumbbell goes down, smile
  const down=EIO(seg(t,1.35,1.75));
  const lift=t<1.35?0.5+0.5*Math.sin(t*9):lerp(0.5+0.5*Math.sin(1.35*9),0,down);
  s+=gym(t,down>0?-1:lift,0,down>0.5?0.8:0.1,1-down);
  if(down>0) s+=dumbbell(lerp(540,330,down),lerp(1400-0.82*245,1570,down),lerp(0.92,0.62,down),-8*down);
  if(t<1.2) s+=pl(390,1000,'hard workout',58);
  s+=clockChip(385,1000,'done by 10 pm',seg(t,1.4,1.7),HY);
  s+=burst(330,1570,seg(t,1.75,2.2),HY);
  return s;}
 if(ph==1){ // hard workout right before bed: wide awake, heart going; done earlier: asleep
  if(t<4.1){ s+=bedScene(t,0,-0.4,true); s+=`<g opacity="${Q(t,2.55)}">`+pl(520,1130,'hard workout at 10:45, bed at 11',48)+`</g>`; if(t>3.0) s+=pl(600,1260,'wide awake',56,INK); }
  else { s+=bedScene(t,1,0.6,false); s+=`<g opacity="${Q(t,4.1)}">`+pl(520,1130,'workout done by 10',56)+`</g>`; s+=zz(640,1400,t,4.2); s+=check(820,1250,seg(t,4.4,4.8),40); }
  return s;}
 if(ph==2){ s+=label(540,1020,'your evening',-2,64); s+=tlRow(t); return s;}
 if(ph==3){ // do this: press, dumbbell down, 10 pm tag, tick
  const down=EIO(seg(t,10.0,10.4));
  const lift=t<10.0?0.5+0.5*Math.sin(t*9):lerp(0.5+0.5*Math.sin(10.0*9),0,down);
  s+=gym(t,down>0?-1:lift,0,down>0.5?0.8:0.2,1-down);
  if(down>0) s+=dumbbell(lerp(540,330,down),lerp(1400-0.82*245,1570,down),lerp(0.92,0.62,down),-8*down);
  s+=clockChip(400,1000,'10 pm',seg(t,9.2,9.45),HY);
  if(t>10.6) s+=check(800,1050,seg(t,10.6,11.0),44);
  return s;}
 s+=`<g transform="translate(540 1400) scale(.62) translate(-540 -1270)">`+gym(t,-1,0,0.8,0)+dumbbell(330,1570,0.62,-8)+`</g>`;
 return s;};

// ---------- SCENE C: slow sighs (breath gauge + 5-minute sand timer) ----------
// one cycle (3.2 s): in 0-0.9 (to 70%), sip 0.9-1.25 (to 100%), long out 1.25-3.2 (to 0)
function breath(tc){tc=((tc%3.2)+3.2)%3.2; if(tc<0.9) return [0.7*EIO(tc/0.9),0]; if(tc<1.25) return [0.7+0.3*EIO((tc-0.9)/0.35),1]; return [1-EIO((tc-1.25)/1.95),2];}
function gauge(x,y,lvl,ph){let s=sh(`<rect x="${x-60}" y="${y-300}" width="120" height="400" rx="60" fill="${CR}" ${o}/>`,9);
 const h=380*lvl; s+=`<rect x="${x-46}" y="${y+86-h}" width="92" height="${h}" rx="46" fill="${ph==2?SKY:HP}"/>`;
 s+=`<path d="M${x+60} ${y-266+0.3*380} h-26" stroke="${INK}" stroke-width="6" stroke-linecap="round"/>`;
 return s;}
function sighFace(x,y,s,lvl,ph,t){ // shoulders rise with the breath, eyes soften on the out-breath
 const lift=-26*lvl, lid=ph==2?0.55+0.4*(1-lvl):0.15;
 let g=`<g transform="translate(0 ${lift})">`+recol(face(0,0,1,lid,0,ph==2?0.5:0.1,t),'#2F2A3A','#FFE27A')+`</g>`;
 if(ph<2){ // air in through the nose: two small arrows
  const k=ph==0?0.5+0.5*Math.sin(T*9):1; g+=`<path d="M-200 ${30+lift} h70 m-22 -20 l22 20 l-22 20" stroke="${SKY}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="${0.5+0.5*k}"/>`;
 } else { // long breath out through the mouth
  for(let i=0;i<3;i++){const k=((t*0.7+i/3)%1); g+=`<path d="M${40+170*k} ${90+lift+(i-1)*26} q35 -20 70 0 q35 20 70 0" stroke="${SKY}" stroke-width="12" fill="none" stroke-linecap="round" opacity="${(1-k)*0.95}"/>`;}
 }
 return `<g transform="translate(${x} ${y}) scale(${s})">${g}</g>`;}
function hourglass(x,y,s,k,flip){ // k 0..1 sand fallen
 let g=`<g transform="rotate(${180*flip})">`+sh(`<rect x="-110" y="-180" width="220" height="26" rx="10" fill="${HP}" ${o}/><rect x="-110" y="154" width="220" height="26" rx="10" fill="${HP}" ${o}/>`,6);
 g+=`<path d="M-86 -154 H86 Q86 -60 12 -6 V6 Q86 60 86 154 H-86 Q-86 60 -12 6 V-6 Q-86 -60 -86 -154Z" fill="#FFFFFF" ${o}/>`;
 const top=1-k; if(top>0.02) g+=`<path d="M${-70*top} ${-20-110*top} H${70*top} L0 -14Z" fill="${HY}" stroke="${INK}" stroke-width="3"/>`;
 if(k>0.02) g+=`<path d="M-72 146 Q0 ${146-120*k} 72 146Z" fill="${HY}" stroke="${INK}" stroke-width="3"/>`;
 if(k>0&&k<1) g+=`<path d="M0 -6 V140" stroke="${HY}" stroke-width="5" stroke-dasharray="10 8" stroke-dashoffset="${-T*60}"/>`;
 g+=`</g>`;
 return `<g transform="translate(${x} ${y}) scale(${s})">${g}</g>`;}
function calmRoom(t,tc,show){let s='';
 s+=sh(`<rect x="110" y="820" width="860" height="880" rx="26" fill="${CR2}" ${o}/>`,12);
 // morning window
 s+=`<rect x="170" y="880" width="250" height="200" rx="10" fill="#CFE8FA" ${o}/><path d="M295 880 V1080 M170 980 H420" stroke="${INK}" stroke-width="7"/><circle cx="360" cy="935" r="32" fill="${HY}" ${o}/>`;
 const [lvl,ph]=breath(tc);
 s+=sighFace(440,1360,1.12,lvl,ph,t);
 s+=gauge(830,1440,lvl,ph);
 if(show){
  const lab=ph==0?'breathe in':(ph==1?'one more sip':'long, slow out');
  s+=pl(650,1075,lab,60,ph==2?INK:DP,-2);
 }
 return s;}
SC.sigh=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==0){ s+=calmRoom(t,t+0.2,true); return s;}
 if(ph==1){ s+=calmRoom(t,t-2.4+0.2,true); return s;}
 if(ph==2){ // research: two groups over a month, both feel better, sighs more
  s+=label(540,1000,'how much better people felt',-2,60);
  const g1=EIO(seg(t,5.65,6.3)), g2=EIO(seg(t,5.85,6.6));
  const col=(x,h,g,c,txt,ic)=>sh(`<rect x="${x-110}" y="${1560-h*g}" width="220" height="${h*g}" rx="24" fill="${c}" ${o}/>`,9)+`<text x="${x}" y="1640" font-family="Inter" font-weight="800" font-size="50" fill="${INK}" text-anchor="middle">${txt}</text>`;
  s+=`<path d="M150 1560 H930" stroke="${INK}" stroke-width="8" stroke-linecap="round"/>`;
  s+=col(330,220,g1,'#E6DCCB','meditation');
  s+=col(750,380,g2,HP,'slow sighs');
  if(t>6.7) s+=check(750,1110,seg(t,6.7,7.1),44)+`<g opacity="${Q(t,6.8)}">`+pl(330,1240,'both helped',54,INK)+`</g>`;
  return s;}
 if(ph==3){ // do this: 5-minute sand timer flips, the breath keeps going
  s+=sh(`<rect x="110" y="820" width="860" height="880" rx="26" fill="${CR2}" ${o}/>`,12);
  const fl=EIO(seg(t,9.1,9.5)), k=seg(t,9.5,11.6);
  s+=hourglass(330,1270,1.0,k,1-fl);
  s+=`<g opacity="${Q(t,9.4)}">`+pl(330,1560,'5 minutes',62)+`</g>`;
  const [lvl,bp]=breath(t-9.0);
  s+=gauge(760,1360,lvl,bp);
  s+=pl(760,1560,bp==0?'in':(bp==1?'in':'out, slowly'),56,bp==2?INK:DP,-2);
  if(t>11.2) s+=check(560,1000,seg(t,11.2,11.6),44);
  return s;}
 s+=`<g transform="translate(540 1400) scale(.62) translate(-540 -1270)">`+calmRoom(t,t,false)+`</g>`;
 return s;};
"""
n1.JS_NOV = n1.JS_NOV + JS_NOV2


def svg_cover(js_expr):
    return n1.svg_cover(js_expr)


def H_(text, size, field="dots"):
    return k28.H_(text, size, field)


# ------------------------------------------------------------------ covers (dedicated, style-menu layouts)
def cover_reframe_getup():
    """Style 7 Ep.01 reframe 'Instead of... / Say...' (quiet), the oct27 reframe layout: Inter Display hook with pill,
    two tilted cards (struck 'Instead of' line, Instrument Serif quotes, Caveat Brush labels), small drawn bed->chair loop, stamp.
    On the LH pink dot grid."""
    hook = "<div style='position:absolute;left:90px;width:900px;top:300px'>" + H_("Lying awake? / *Get out of bed.*", 128, "pink") + "</div>"
    c = lambda bg, rot: (f"padding:34px 46px;border-radius:36px;background:{bg};border:6px solid {k27.INK};box-shadow:12px 12px 0 {k27.INK};transform:rotate({rot}deg)")
    lab = "font-family:'Caveat Brush';font-size:72px;color:#E8336F;line-height:1"
    q = f"font-family:'Instrument Serif';font-size:92px;line-height:1.02;color:{k27.INK};margin-top:10px"
    cards = (f"<div style='position:absolute;left:110px;right:110px;top:640px;display:flex;flex-direction:column;gap:40px'>"
             f"<div style='{c('#FFFDF4', -1.5)}'><div style=\"{lab}\">Instead of…</div>"
             f"<div style=\"{q};text-decoration:line-through;text-decoration-thickness:7px;text-decoration-color:#E8336F\">“I'll lie here till I sleep.”</div></div>"
             f"<div style='{c('#FFE27A', 1.2)}'><div style=\"{lab}\">Say…</div>"
             f"<div style=\"{q}\">“After 20 minutes,<br>I get up.”</div></div></div>")
    art = svg_cover("'<g transform=\"translate(560 1440) scale(.5)\">'+bedIcon(0,0,1)+'</g>'"
                    "+'<g transform=\"translate(840 1460) scale(.3)\">'+chairIcon(0,0,1)+'</g>'"
                    "+arcArrow(610,800,1390,70,1,DP,true)")
    stamp = edkit.stamp("lockedhour", 90, 1330, size=160, rot=-12)
    return hook + cards + art + stamp


def cover_line_workout():
    """Style 9 follow-the-line (quiet): Inter Display hook with pill, a hand-drawn dashed path winding from the
    dumbbell through '10 pm: done' and '1 hour' to the bed at 11, Caveat stops, stamp. On the LH cream dot grid."""
    hook = "<div style='position:absolute;left:90px;width:900px;top:300px'>" + H_("Hard workout? / *Done 1 hour before bed.*", 112, "cream") + "</div>"
    art = svg_cover(
        "`<path d=\"M230 760 C560 760 820 820 820 960 S260 1060 260 1180 S700 1300 800 1300\" stroke=\"${INK}\" stroke-width=\"10\" fill=\"none\" stroke-dasharray=\"26 20\" stroke-linecap=\"round\"/>`"
        "+dumbbell(230,760,0.62,-10)"
        "+`<circle cx=\"820\" cy=\"960\" r=\"26\" fill=\"${HY}\" ${o}/>`+pillLab(640,975,'10 pm: workout done',54)"
        "+`<circle cx=\"260\" cy=\"1180\" r=\"26\" fill=\"${HP}\" ${o}/>`+pillLab(440,1195,'1 hour: wind down',54,INK)"
        "+'<g transform=\"translate(830 1290) scale(.8)\">'+bedIcon(0,0,1)+'</g>'+label(830,1400,'11 pm: bed',-3,60)")
    stamp = edkit.stamp("lockedhour", 80, 1290, size=150, rot=-12)
    return hook + art + stamp


def cover_kinetic_sigh():
    """Style 5 kinetic big text, cover frame (loud): giant '5' on a pink highlighter stripe, 'minutes of slow sighs' pill line,
    Caveat line, the drawn breath gauge + face, stamp. On butter dot grid. Round 2: whole stack inside the 3:4 grid crop (y 240-1680)."""
    top = "<div style='position:absolute;left:90px;width:900px;top:275px'>" + H_("Stressed already?", 84, "dots") + "</div>"
    big = ("<div style='position:absolute;left:0;right:0;top:380px;text-align:center'>"
           "<div style='position:absolute;left:320px;right:320px;top:205px;height:100px;background:#FF5CA8;opacity:.85;border-radius:50px;transform:rotate(-2deg)'></div>"
           "<div class='H' style='position:relative;font-size:340px;line-height:.9;letter-spacing:-.05em'>5</div></div>")
    line = "<div style='position:absolute;left:90px;width:900px;top:720px'>" + H_("*minutes of slow sighs.*", 100, "dots") + "</div>"
    note = ("<div style=\"position:absolute;left:90px;width:900px;top:860px;text-align:center;font-family:'Caveat Brush';font-size:66px;"
            "color:#E8336F;transform:rotate(-3deg)\">deep breath in, a sip more, long out ↓</div>")
    art = svg_cover("'<g transform=\"translate(540 1370) scale(.6) translate(-540 -1270)\">'+calmRoom(0,1.3,false)+'</g>'")
    stamp = edkit.stamp("lockedhour", 70, 1180, size=150, rot=-12)
    return top + big + line + note + art + stamp


def cover_page(kind):
    bg = {"reframe": "#FFD5E5", "line": "#FFF6E5", "kinetic": "#FFF0A6"}[kind]
    inner = {"reframe": cover_reframe_getup, "line": cover_line_workout, "kinetic": cover_kinetic_sigh}[kind]()
    css = CSS.replace("background-color:#FFF0A6", f"background-color:{bg}", 1)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body><div id='bg'></div>"
            f"<script>{k27.JS}{k28.JS_EXTRA}{n1.JS_NOV}</script>{inner}</body></html>")


# ------------------------------------------------------------------ specs
SPECS = {
    "getup": dict(
        id="lh-reel-1104-get-up-20", scene="getup", music="media/music/library/v4/lh-x-phone-down.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.6], cover="reframe", follow_y=640, stamp_xy=(70, 1390), part2_line="Part 2 tomorrow, 7 pm.",
        hits=[(1.05, "sfx-x-swoosh-in", 0.3), (1.6, "sfx-x-sticker-pop", 0.35), (4.5, "sfx-x-swoosh-in", 0.25),
              (5.6, "sfx-x-whoosh-hit", 0.25), (9.3, "sfx-x-paper-slap", 0.25), (10.3, "sfx-x-swoosh-in", 0.3), (12.0, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(kick="Lying awake?", ks=76, head="After 20 minutes, / *get out of bed.*", fs=128, top=290),
            dict(kick="try this", head="Teach your brain: / *bed is for sleeping.*", fs=116,
                 sub="Lying awake teaches it the opposite.<br>Sit somewhere calm until you feel sleepy.", ss=44, bg2=True),
            dict(kick="the research", head="Sleep doctors use this / *to treat insomnia.*", fs=104,
                 sub="Their guideline: not asleep in about<br>20 minutes? Get up. Back when sleepy.", ss=46,
                 src="Schutte-Rodin et al. 2008 · J Clin Sleep Med"),
            dict(kick="Do this tonight:", head="Hide the clock. / *Up after 20 minutes.*", fs=118,
                 sub="Dim lamp, a dull book, another seat.<br>Back to bed only when you're sleepy.", ss=46, bg2=True),
            dict(kick="Lying awake?", ks=76, head="After 20 minutes, / *get out of bed.*", fs=128, top=290),
        ]),
    "workout": dict(
        id="lh-reel-1105-workout-1h", scene="workout", music="media/music/library/v4/lh-x-lock-in.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.6], cover="line", follow_y=640, stamp_xy=(70, 1390),
        hits=[(1.4, "sfx-x-sticker-pop", 0.3), (1.75, "sfx-x-paper-slap", 0.3), (4.1, "sfx-x-swoosh-in", 0.3),
              (5.6, "sfx-x-whoosh-hit", 0.25), (9.2, "sfx-x-sticker-pop", 0.3), (10.4, "sfx-x-paper-slap", 0.3), (12.0, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(kick="Working out tonight?", ks=76, head="Bed at 11? / *Hard workout done by 10.*", fs=118, top=290),
            dict(kick="sleep, part 2", head="Evening workouts are fine. / *Just not hard ones late.*", fs=100,
                 sub="A hard session that ends right before bed<br>can make it harder to fall asleep.", ss=44, bg2=True),
            dict(kick="the research", head="23 studies: evening exercise / *didn't hurt sleep.*", fs=98,
                 sub="The possible exception: hard workouts<br>that end within 1 hour of bed.", ss=46,
                 src="Stutz et al. 2019 · Sports Medicine"),
            dict(kick="Do this tonight:", head="Finish hard workouts / *1 hour before bed.*", fs=112,
                 sub="A walk or easy stretch later is fine.", ss=48, bg2=True),
            dict(kick="Working out tonight?", ks=76, head="Bed at 11? / *Hard workout done by 10.*", fs=118, top=290),
        ]),
    "sigh": dict(
        id="lh-reel-1105am-slow-sighs", scene="sigh", music="media/music/library/v4/lh-x-tick-boom.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.6], cover="kinetic", follow_y=720, stamp_xy=(70, 1390),
        hits=[(5.6, "sfx-x-whoosh-hit", 0.2), (9.1, "sfx-x-swoosh-in", 0.3), (11.2, "sfx-x-sticker-pop", 0.3), (12.0, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(kick="Stressed already?", ks=76, head="Sigh slowly / *for 5 minutes.*", fs=136, top=290),
            dict(kick="try this", head="One deep breath in, / a short sip more, / *then a long breath out.*", fs=96,
                 sub="In through your nose.<br>Out slowly through your mouth.", ss=44, bg2=True),
            dict(kick="the research", head="5 minutes a day for a month / lifted mood *more than meditation.*", fs=90,
                 sub="108 people. Both groups felt better;<br>the sighing group gained more.", ss=44,
                 src="Balban et al. 2023 · Cell Reports Medicine"),
            dict(kick="Do this now:", head="Set a 5-minute timer. / *In, in, long out.*", fs=110,
                 sub="Keep going until it rings.", ss=48, bg2=True),
            dict(kick="Stressed already?", ks=76, head="Sigh slowly / *for 5 minutes.*", fs=136, top=290),
        ]),
}

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    still = next((a[8:] for a in sys.argv if a.startswith("--still=")), None)
    for key in args or list(SPECS):
        s = SPECS[key]
        cov = OUT / f"{s['id']}-cover.jpg"
        if not still:
            k28.render(s, key, cover_page=cover_page(s["cover"]), cover_out=cov)
            print("cover", cov)
        if "--cover-only" in sys.argv:
            continue
        if still:
            k28.render(s, key, still=[float(x) for x in still.split(",")]); print("stills", SCR / f"{key}-stills.jpg"); continue
        fdir, total, starts = k28.render(s, key)
        out = OUT / f"{s['id']}.mp4"
        k28.encode(fdir, total, s["music"], s["hits"], out)
        print(out, round(total, 2), starts)

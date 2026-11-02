#!/usr/bin/env python3
"""Nov 2 (Social studio, Littlefold maker): three Reels in the rice-grain / grapes shape (sunny sky + ONE drawn object doing
the rule + a number you can picture), extending nov01_littlefold.py (imported, not edited: html(), draw(), board(), knife(),
highChair() ...) which itself extends oct27_littlefold.py and recovery-oct22c/littlefold/reel_story.py.

A  lf-reel-1104-coin-battery     (Wed Nov 4 19:00)  PART 1: "A nickel-sized battery can burn in 2 hours."
   A remote's battery lid pops, a coin battery rolls out beside a nickel ('same size as a nickel'); a clock sweeps 2 hours.
   Where they hide: remote, key fob, musical card, flameless candle. Used ones: tape both sides, recycle. Do this: tape
   strip across the remote's battery lid. Last beat: 'Part 2 tomorrow, 7 pm.' + follow. COVER: sticky-note list (#13, quiet).
B  lf-reel-1105-battery-honey    (Thu Nov 5 19:00)  PART 2: "Battery swallowed? ER now. 2 teaspoons of honey."
   Honey jar + teaspoon counted 1, 2; a clock with 6 spoon dots (every 10 minutes, up to 6 times); a speech bubble with a
   coin battery to a drawn hospital sign ('It might be a coin battery.'); Do this: a phone saves the poison centre contact.
   COVER: Ep.01 reframe 'instead of... / try...' (#7, quiet).
C  lf-reel-1105am-medicine-mL    (Thu Nov 5 08:00, trial auto)  "Kids' medicine? 0.5 mL is not 5 mL."
   Two oral syringes fill to 0.5 and 5; three kitchen spoons of different sizes get a 'no' ring; the syringe that came with
   the bottle gets a check; Do this: the syringe draws medicine up to its mL line. COVER: kinetic big text (#5, loud).

Facts (checked Nov 2 2026): see the manifest's first_comment for each Reel (AAP HealthyChildren.org, Health Canada).

    python3 studio/editorial/nov02_littlefold.py battery|honey|medicine [--still=0.0,1.5,...] [--cover-only] [--no-cover]
"""
import os
import sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import nov01_littlefold as N1  # noqa: E402
S27, RS = N1.S27, N1.RS
SCRD = Path("/tmp/claude-0/nov02-littlefold")
SCRD.mkdir(parents=True, exist_ok=True)
RS.SCR = SCRD
K, F, INK, KICK, B = RS.K, RS.F, RS.INK, RS.KICK, RS.B
W, H = RS.W, RS.H
OUT = RS.REPO / "media" / "studio-nov02" / "littlefold"
LIB = RS.LIB
FOLLOW = N1.FOLLOW
BB, DROP_BB = N1.BB, N1.DROP_BB   # lf-x-sunny-bounce
BG, DROP_BG = N1.BG, N1.DROP_BG   # lf-x-giggle-pop
BP, DROP_BP = N1.BP, N1.DROP_BP   # lf-x-tiny-parade

JS = r"""
// ===================== Nov 2: coin batteries, honey, medicine in mL =====================
const SIL='#DDE4EC', SIL2='#B9C4D0', HON='#F6B73C', HON2='#FFD978', AMB='#E59A4C', MED='#F49AB0';
function coinBat(x,y,s,rot){return `<g transform="translate(${x} ${y}) rotate(${rot||0}) scale(${s||1})"><circle r="44" fill="${SIL}" ${o}/>
 <circle r="32" fill="none" stroke="${SIL2}" stroke-width="5"/><path d="M-8 -12 h16 M0 -20 v16" stroke="${PL}" stroke-width="5" stroke-linecap="round"/>
 <path d="M-26 -22 q10 -12 26 -14" stroke="#FFFFFF" stroke-width="6" fill="none" stroke-linecap="round"/></g>`;}
function nickel(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s||1})"><circle r="46" fill="#C9CFD8" ${o}/><circle r="37" fill="none" stroke="#AEB7C3" stroke-width="4" stroke-dasharray="3 6"/>
 <text x="0" y="13" font-family="Poppins" font-weight="700" font-size="34" text-anchor="middle" fill="#6E7A88">5¢</text></g>`;}
function remote(x,y,lid,s,tape){ // TV remote lying flat, seen from above; lid 0 closed .. 1 off; tape 0..1 strip across the lid
 const lx=120, ly=40*E(lid), lr=0;
 let b='';for(let r=0;r<3;r++)for(let c=0;c<2;c++) b+=`<circle cx="${-120+c*44}" cy="${-22+r*22}" r="8" fill="${[PINK,BUT,BLUE][r]}" stroke="${PL}" stroke-width="3"/>`;
 return `<g transform="translate(${x} ${y}) scale(${s||1})"><rect x="-190" y="-52" width="380" height="104" rx="40" fill="#8E93C8" ${o}/>
 <circle cx="-150" cy="0" r="13" fill="${CORAL}" stroke="${PL}" stroke-width="3"/>${b}<rect x="-40" y="-24" width="70" height="48" rx="14" fill="#A9AEDA" stroke="${PL}" stroke-width="3"/>
 <rect x="68" y="-40" width="104" height="80" rx="18" fill="#6E73A8" stroke="${PL}" stroke-width="3"/>
 ${lid<1?'':''}<g transform="translate(${lx} ${ly}) rotate(${lr})" opacity="${1-seg(lid,0.3,1)}"><rect x="-52" y="-40" width="104" height="80" rx="18" fill="#A9AEDA" ${o} stroke-width="4"/><path d="M-20 -10 h40 M-20 6 h40" stroke="${PL}" stroke-width="3" opacity=".5"/></g>
 ${tape>0?`<g opacity="${seg(tape,0,0.15)}"><rect x="${80}" y="-58" width="${190*E(tape)}" height="116" rx="6" fill="#FFE9A6" fill-opacity=".85" stroke="#E9C46A" stroke-width="3" transform="rotate(-8 120 0)"/></g>`:''}</g>`;}
function clockF(x,y,r,k,lab){ // clock face; k sweeps 0..1 of 2 hours (60 degrees)
 let s=`<circle cx="${x}" cy="${y}" r="${r}" fill="${CREAM}" ${o}/>`;
 for(let i=0;i<12;i++){const a=i*Math.PI/6; s+=`<path d="M${x+r*0.8*Math.sin(a)} ${y-r*0.8*Math.cos(a)} L${x+r*0.92*Math.sin(a)} ${y-r*0.92*Math.cos(a)}" stroke="${PL}" stroke-width="${i%3?3:6}" stroke-linecap="round"/>`;}
 const a1=Math.PI/3*k, R=r*0.72;
 if(k>0) s+=`<path d="M${x} ${y} L${x} ${y-R} A${R} ${R} 0 0 1 ${x+R*Math.sin(a1)} ${y-R*Math.cos(a1)} Z" fill="${CORAL}" opacity=".55"/>`;
 s+=`<path d="M${x} ${y} L${x+R*0.95*Math.sin(a1)} ${y-R*0.95*Math.cos(a1)}" stroke="${PL}" stroke-width="7" stroke-linecap="round"/><circle cx="${x}" cy="${y}" r="9" fill="${PL}"/>`;
 return s;}
function sparkleAt(x,y,k){if(k<=0)return '';return sparkle(x,y,0.6+0.5*Math.sin(Math.PI*k),Math.sin(Math.PI*cl(k,0,1)));}
function fob(x,y){return `<g transform="translate(${x} ${y})"><circle cx="0" cy="-86" r="26" fill="none" stroke="${SIL2}" stroke-width="9"/><rect x="-46" y="-64" width="92" height="140" rx="40" fill="#F49AB0" ${o}/>
 <circle cx="0" cy="-20" r="14" fill="${CREAM}" stroke="${PL}" stroke-width="3"/><circle cx="0" cy="22" r="14" fill="${CREAM}" stroke="${PL}" stroke-width="3"/></g>`;}
function smallRemote(x,y){let b='';for(let r=0;r<4;r++) b+=`<circle cx="-14" cy="${-40+r*28}" r="8" fill="${[PINK,BUT,BLUE,SAGE][r]}" stroke="${PL}" stroke-width="3"/><circle cx="14" cy="${-40+r*28}" r="8" fill="${[BUT,BLUE,SAGE,PINK][r]}" stroke="${PL}" stroke-width="3"/>`;
 return `<g transform="translate(${x} ${y})"><rect x="-42" y="-100" width="84" height="200" rx="34" fill="#8E93C8" ${o}/><circle cx="0" cy="-70" r="12" fill="${CORAL}" stroke="${PL}" stroke-width="3"/>${b}</g>`;}
function card(x,y,t){return `<g transform="translate(${x} ${y}) rotate(-6)"><path d="M-70 -90 L70 -90 L70 90 L-70 90Z" fill="#FFE3EC" ${o}/><path d="M0 -90 V90" stroke="${PL}" stroke-width="3" opacity=".45"/>
 <path d="M-30 -20 c-8 -14 -30 -6 -22 10 l22 20 l22 -20 c8 -16 -14 -24 -22 -10z" fill="#D9497A"/>
 <g transform="translate(36 ${-30+6*Math.sin(t*5)})"><path d="M-8 20 V-16 L14 -22 V12" stroke="${PL}" stroke-width="5" fill="none"/><circle cx="-14" cy="20" r="8" fill="${PL}"/><circle cx="8" cy="14" r="8" fill="${PL}"/></g></g>`;}
function candle(x,y,t){const f=1+0.06*Math.sin(t*9);return `<g transform="translate(${x} ${y})"><rect x="-44" y="-50" width="88" height="140" rx="16" fill="${CREAM}" ${o}/>
 <path d="M0 -60 Q${-20*f} -90 0 ${-130*f} Q${20*f} -90 0 -60Z" fill="${BUT}" ${o} stroke-width="4"/><circle cx="0" cy="-84" r="34" fill="${BUT}" opacity=".25"/></g>`;}
function tapeStrip(x,y,len,rot,k){if(k<=0)return '';return `<rect x="${x-len/2}" y="${y-26}" width="${len*E(k)}" height="52" rx="5" fill="#FFE9A6" fill-opacity=".9" stroke="#E9C46A" stroke-width="3" transform="rotate(${rot} ${x} ${y})"/>`;}
function recycleBox(x,y){return `<g transform="translate(${x} ${y})"><path d="M-110 -70 L110 -70 L94 100 L-94 100Z" fill="#BFD8B0" ${o}/><rect x="-124" y="-90" width="248" height="34" rx="12" fill="#A8CA9A" ${o} stroke-width="4"/>
 <g transform="translate(0 20)" fill="none" stroke="${PL}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"><path d="M-30 18 L-44 -6 L-24 -36"/><path d="M-24 -36 l-2 14 m2 -14 l12 6"/><path d="M8 -38 L36 -38 L44 -6"/><path d="M44 -6 l-12 -4 m12 4 l4 -12"/><path d="M34 22 L-6 22"/><path d="M-6 22 l10 -10 m-10 10 l10 10"/></g></g>`;}
// ---------- honey / ER / phone
function honeyJar(x,y,k){return `<g transform="translate(${x} ${y})"><path d="M-80 -60 Q-96 -40 -92 30 Q-90 100 0 104 Q90 100 92 30 Q96 -40 80 -60Z" fill="${HON}" ${o}/>
 <path d="M-62 -30 Q-70 20 -56 60" stroke="${HON2}" stroke-width="12" fill="none" stroke-linecap="round" opacity=".8"/>
 <rect x="-92" y="-96" width="184" height="44" rx="14" fill="${CREAM}" ${o}/><path d="M-92 -74 h184" stroke="#E9C9A0" stroke-width="4"/>
 <ellipse cx="0" cy="34" rx="44" ry="30" fill="${CREAM}" stroke="${PL}" stroke-width="3"/><path d="M0 50 c-8 -14 -26 -6 -18 8 l18 14 l18 -14 c8 -14 -10 -22 -18 -8z" transform="translate(0 -28) scale(.8)" fill="#D9497A"/></g>`;}
function teaspoon(x,y,rot,full){return `<g transform="translate(${x} ${y}) rotate(${rot})"><rect x="0" y="-9" width="190" height="18" rx="9" fill="${SIL}" ${o} stroke-width="4"/>
 <ellipse cx="-40" cy="0" rx="50" ry="34" fill="${SIL}" ${o} stroke-width="4"/>${full>0?`<ellipse cx="-40" cy="2" rx="${38*full}" ry="${24*full}" fill="${HON}"/>`:''}</g>`;}
function drip(x,y,k){if(k<=0||k>=1)return '';return `<path d="M${x} ${y} Q${x+6} ${y+60*k} ${x} ${y+90*k}" stroke="${HON}" stroke-width="10" fill="none" stroke-linecap="round"/><circle cx="${x}" cy="${y+96*k}" r="9" fill="${HON}"/>`;}
function numBub(x,y,n,k){if(k<=0)return '';const s=E(k);return `<g transform="translate(${x} ${y}) scale(${s})"><circle r="34" fill="#D9497A"/><text y="12" font-family="Poppins" font-weight="700" font-size="36" text-anchor="middle" fill="#FFF8EE">${n}</text></g>`;}
function spoonDots(x,y,n,k){let s='';for(let i=0;i<6;i++){const on=i<n?1:0;const kk=seg(k,i/6,(i+1)/6);
 s+=`<g transform="translate(${x+i*92} ${y})"><circle r="32" fill="${kk>0?HON2:CREAM}" ${o} stroke-width="4"/>${kk>0?`<circle r="${20*E(kk)}" fill="${HON}"/>`:''}</g>`;}return s;}
function hospital(x,y){return `<g transform="translate(${x} ${y})"><rect x="-120" y="-120" width="240" height="240" rx="40" fill="#FFFFFF" ${o}/>
 <path d="M-26 -78 h52 v52 h52 v52 h-52 v52 h-52 v-52 h-52 v-52 h52Z" fill="${CORAL}" ${o} stroke-width="4"/></g>`;}
function speech(x,y,k){if(k<=0)return '';const s=E(k);return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-130 -90 Q-130 -120 -100 -120 L100 -120 Q130 -120 130 -90 L130 40 Q130 70 100 70 L20 70 L-20 120 L-30 70 L-100 70 Q-130 70 -130 40Z" fill="${CREAM}" ${o}/>`+coinBat(-40,-24,1)+`<text x="56" y="0" font-family="Caveat Brush" font-size="84" fill="#B23A62" text-anchor="middle">?</text></g>`;}
function phoneS(x,y,k,t){ // phone with a new contact being saved: avatar + lines, a star fills, a check
 const st=seg(k,0.2,0.6);
 return `<g transform="translate(${x} ${y}) rotate(-4)"><rect x="-130" y="-230" width="260" height="460" rx="40" fill="${INK}"/><rect x="-112" y="-206" width="224" height="412" rx="24" fill="#FFF8EE"/>
 <circle cx="0" cy="-110" r="54" fill="#FFE3EC" ${o} stroke-width="4"/><path d="M-12 -150 h24 v28 h28 v24 h-28 v28 h-24 v-28 h-28 v-24 h28Z" fill="${CORAL}"/>
 <rect x="-80" y="-30" width="160" height="22" rx="11" fill="#E9DFF0"/><rect x="-60" y="10" width="120" height="18" rx="9" fill="#EFE8F3"/>
 <path transform="translate(0 100) scale(${0.9+0.25*Math.sin(Math.PI*st)})" d="M0 -40 l12 24 l26 4 l-19 18 l5 26 l-24 -13 l-24 13 l5 -26 l-19 -18 l26 -4z" fill="${st>0?BUT:'#FFFFFF'}" ${o} stroke-width="4"/></g>`;}
// ---------- medicine
function syringeH(x,y,len,fill,s){ // oral syringe lying flat, tip LEFT; fill 0..1 of the barrel; 10 ticks
 let tk='';for(let i=0;i<=10;i++) tk+=`<path d="M${-len/2+20+i*(len-40)/10} -30 v${i%5?14:24}" stroke="${PL}" stroke-width="${i%5?3:5}"/>`;
 const fw=(len-40)*fill;
 return `<g transform="translate(${x} ${y}) scale(${s||1})"><path d="M${-len/2-50} -10 L${-len/2} -14 L${-len/2} 14 L${-len/2-50} 10Z" fill="#FFFFFF" ${o} stroke-width="4"/>
 ${fill>0?`<rect x="${-len/2+20}" y="-26" width="${fw}" height="52" fill="${MED}"/>`:''}
 <rect x="${-len/2}" y="-34" width="${len}" height="68" rx="12" fill="#FFFFFF" fill-opacity=".35" ${o}/>${tk}
 <rect x="${-len/2+20+fw}" y="-30" width="16" height="60" rx="4" fill="#9AA6B8" stroke="${PL}" stroke-width="3"/>
 <rect x="${-len/2+36+fw}" y="-7" width="${len-36-fw+40}" height="14" fill="#E6EBF2" stroke="${PL}" stroke-width="3"/>
 <rect x="${len/2+40}" y="-40" width="22" height="80" rx="8" fill="#E6EBF2" ${o} stroke-width="4"/>
 <rect x="${len/2-6}" y="-50" width="14" height="100" rx="6" fill="#FFFFFF" ${o} stroke-width="4"/></g>`;}
function spoonK(x,y,s,rot){return `<g transform="translate(${x} ${y}) rotate(${rot||0}) scale(${s})"><rect x="0" y="-9" width="190" height="18" rx="9" fill="${SIL}" ${o} stroke-width="4"/><ellipse cx="-40" cy="0" rx="50" ry="34" fill="${SIL}" ${o} stroke-width="4"/><ellipse cx="-50" cy="-8" rx="18" ry="9" fill="#FFFFFF" opacity=".7"/></g>`;}
function bottle(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s||1})"><rect x="-70" y="-100" width="140" height="200" rx="30" fill="${AMB}" ${o}/><rect x="-46" y="-150" width="92" height="56" rx="14" fill="${CREAM}" ${o}/>
 <rect x="-56" y="-46" width="112" height="96" rx="12" fill="${CREAM}" stroke="${PL}" stroke-width="3"/><path d="M0 14 c-8 -14 -26 -6 -18 8 l18 14 l18 -14 c8 -14 -10 -22 -18 -8z" transform="translate(0 -20)" fill="#D9497A"/>
 <path d="M-50 -80 Q-56 0 -50 80" stroke="#F4BE86" stroke-width="10" fill="none" stroke-linecap="round" opacity=".8"/></g>`;}
SCN.battery=[
 (lt,t)=>{ // frame 0: a coin battery beside a nickel, same size; then a clock sweeps 2 hours
  const ck=seg(lt,0.35,1.6);
  let s=board(540,1250,700)+coinBat(380,1180,1.4,-10)+nickel(535,1180,1.38);
  s+=label(460,1065,'same size as a nickel',-4,46);
  s+=`<g opacity="${seg(lt,0.2,0.4)}">`+clockF(745,1160,86,EIO(ck))+`</g>`;
  if(lt>1.4) s+=label(745,1045,'2 hours',-5,56);
  return s;},
 (lt,t)=>{ // where they hide: remote, key fob, musical card, flameless candle
  let s=board(540,1270,700);
  const X=[295,455,620,780], D=[smallRemote,fob,card,candle];
  X.forEach((x,i)=>{const k=i==0?1:seg(lt,0.05+0.18*i,0.35+0.18*i); if(k<=0) return;
   s+=`<g transform="translate(${x} ${1190}) scale(${0.6+0.4*E(k)}) translate(${-x} -1190)" opacity="${seg(k,0,0.3)}">`+D[i](x,1190,t)+`</g>`;
   const bk=seg(lt,0.2+0.2*i,0.6+0.2*i); if(bk>0) s+=coinBat(x+34,1070-30*E(bk),0.72,0)+sparkleAt(x+70,1030,seg(lt,0.3+0.2*i,1.0+0.2*i));});
  return s;},
 (lt,t)=>{ // used ones: tape both sides, then into the recycling box
  const mv=EIO(seg(lt,1.25,1.85));
  let s=board(540,1270,700)+recycleBox(715,1170);
  const bx=380+335*mv, by=1170-160*Math.sin(Math.PI*mv)+40*mv;
  s+=`<g transform="translate(${bx} ${by}) scale(${1.5-0.9*mv}) translate(${-bx} ${-by})">`+coinBat(bx,by,1,0)+tapeStrip(bx,by,120,-20,seg(lt,0.15,0.45))+tapeStrip(bx,by,120,25,seg(lt,0.5,0.8))+`</g>`;
  if(lt>0.5&&lt<1.3) s+=label(380,1040,'tape both sides',-4,52);
  if(lt>1.85) s+=check(800,1050,seg(lt,1.85,2.3));
  return s;},
 (lt,t)=>{ // Do this: a tape strip goes over the remote's battery lid; check; hearts
  let s=board(540,1250,700)+remote(505,1180,0,1.2,seg(lt,0.3,1.0));
  if(lt>1.0) s+=check(770,1115,seg(lt,1.0,1.5));
  if(lt>1.6) s+=hearts(t,360,1100);
  return s;},
];
SCN.honey=[
 (lt,t)=>{ // honey jar, a teaspoon dips in and lifts out full, twice: 1, 2
  let s=board(540,1270,700)+honeyJar(360,1160);
  const d1=seg(lt,0.1,0.7), d2=seg(lt,0.8,1.4), k=lt<0.75?d1:d2;
  const lift=Math.sin(Math.PI*k);
  const sx=430+110*lift, sy=1075-35*lift;
  s+=teaspoon(sx,sy,-12,lift>0.15?1:0)+drip(sx-36,sy+30,seg(k,0.5,0.95));
  s+=numBub(640,1150,1,seg(lt,0.55,0.8))+numBub(730,1150,2,seg(lt,1.25,1.5));
  if(lt>1.5) s+=label(690,1228,'2 teaspoons',-3,52);
  return s;},
 (lt,t)=>{ // clock: every 10 minutes, 6 spoon dots fill
  let s=`<circle cx="540" cy="1110" r="104" fill="${CREAM}" ${o}/>`;
  for(let i=0;i<12;i++){const a=i*Math.PI/6; s+=`<path d="M${540+84*Math.sin(a)} ${1110-84*Math.cos(a)} L${540+96*Math.sin(a)} ${1110-96*Math.cos(a)}" stroke="${PL}" stroke-width="${i%3?3:6}" stroke-linecap="round"/>`;}
  const k=seg(lt,0.2,2.3), m=k*6;
  const a=2*Math.PI*(m%1)*0+Math.PI/3*m; // minute hand: 10 minutes = 60 degrees per dose
  s+=`<path d="M540 1110 A76 76 0 ${a>Math.PI?1:0} 1 ${540+76*Math.sin(Math.min(a,6.27))} ${1110-76*Math.cos(Math.min(a,6.27))}" fill="none"/>`;
  s+=`<path d="M540 1110 L${540+82*Math.sin(a)} ${1110-82*Math.cos(a)}" stroke="${PL}" stroke-width="8" stroke-linecap="round"/><circle cx="540" cy="1110" r="10" fill="${PL}"/>`;
  s+=spoonDots(310,1270,6,k);
  return s;},
 (lt,t)=>{ // at the ER: a speech bubble with a coin battery, a hospital sign
  let s=hospital(760,1150)+speech(400,1110,seg(lt,0.2,0.6));
  return s;},
 (lt,t)=>{ // Do this: phone saves the poison centre contact
  let s=`<g transform="translate(540 1215) scale(.58) translate(-540 -1150)">`+phoneS(540,1150,seg(lt,0.2,1.2),t)+`</g>`;
  if(lt>1.2) s+=check(370,1200,seg(lt,1.2,1.7));
  if(lt>1.8) s+=hearts(t,760,1220);
  return s;},
];
SCN.medicine=[
 (lt,t)=>{ // two syringes fill: 0.5 mL vs 5 mL
  const k=EIO(seg(lt,0.15,1.2));
  let s=syringeH(600,1090,400,0.1*k,0.8)+syringeH(600,1250,400,1.0*k,0.8);
  if(lt>0.9) s+=label(300,1105,'0.5 mL',-4,54)+label(300,1265,'5 mL',-4,54);
  return s;},
 (lt,t)=>{ // three kitchen spoons of different sizes: no
  let s=board(540,1260,700);
  [[370,0.62],[545,0.82],[725,1.0]].forEach(([x,sc],i)=>{const k=i==0?1:seg(lt,0.1+0.2*i,0.35+0.2*i); if(k>0) s+=`<g opacity="${seg(k,0,0.4)}">`+spoonK(x,1235-190*sc,sc,90)+`</g>`;});
  if(lt>0.9) s+=noRing(545,1135,185,seg(lt,0.9,1.6));
  return s;},
 (lt,t)=>{ // the syringe that came with it: check
  let s=board(540,1270,700)+bottle(380,1150,1.0);
  const k=E(seg(lt,0.1,0.6));
  s+=`<g opacity="${k}">`+syringeH(700+60*(1-k),1210,300,0,0.75)+`</g>`;
  if(lt>0.8) s+=check(700,1120,seg(lt,0.8,1.3))+label(620,1045,'came in the box',-4,48);
  return s;},
 (lt,t)=>{ // Do this: syringe in the bottle draws up to the line
  let s=board(540,1290,700)+bottle(460,1180,1.0);
  const f=EIO(seg(lt,0.3,1.6));
  s+=`<g transform="translate(700 1135) rotate(-90) translate(-700 -1135)">`+syringeH(700,1135,260,0.6*f,0.8)+`</g>`;
  if(lt>1.6) s+=check(820,1060,seg(lt,1.6,2.1));
  if(lt>2.2) s+=hearts(t,270,1100);
  return s;},
];
['battery','honey','medicine'].forEach(k=>{SCN[k]=SCN[k].map(f=>(lt,t)=>`<g transform="translate(540 1120) scale(1.0) translate(-540 -1180)">`+f(lt,t)+`</g>`);});
"""


SPEC_BATTERY = dict(
    out="lf-reel-1104-coin-battery", music=LIB / "v4/lf-x-sunny-bounce.mp3", scene="battery", follow=FOLLOW, follow_y=820,
    part2="Part 2 tomorrow, 7 pm.", part2_y=700, follow_at=0.6, garments=["none"] * 4,
    durs=[6 * BB, 5 * BB, DROP_BB - 11 * BB, 3.2],
    beats=[
        dict(kick="a swallowed coin battery", head="Can burn a throat / *in 2 hours.*", sub="<span style=\"display:inline-block;padding:10px 32px 12px;border-radius:40px;background:#D9497A;color:#FFF8EE;font:600 48px/1.2 Poppins;font-style:normal\">Swallowed, or think so? ER now.</span>", fs=130, sy=720, ss=50, chip="AAP HealthyChildren.org · Health Canada"),
        dict(kick="where they hide", head="Remotes, key fobs, / *toys, musical cards.*", sub="Also flameless candles and scales.", fs=120, sy=730, ss=50, chip="AAP HealthyChildren.org · Health Canada"),
        dict(kick="used ones too", head="Tape both sides, / *then recycle them.*", sub="Keep new and used ones out of reach.", fs=124, sy=730, ss=50, chip="Health Canada · AAP"),
        dict(kick="Do this:", head="Tonight: tape the / *remote's battery lid.*", fs=120, chip="AAP HealthyChildren.org · Health Canada"),
    ])

SPEC_HONEY = dict(
    out="lf-reel-1105-battery-honey", music=LIB / "v4/lf-x-tiny-parade.mp3", scene="honey", follow=FOLLOW, follow_y=860,
    tag="PART 2 · COIN BATTERIES", follow_at=0.6, garments=["none"] * 4,
    durs=[6 * BP, 5 * BP, DROP_BP - 11 * BP, 4.2],
    beats=[
        dict(kick="battery swallowed?", head="ER now. On the way: / *2 teaspoons of honey.*", sub="<span style=\"display:inline-block;padding:6px 28px 10px;background:#FFE08A;border-radius:14px;box-shadow:0 6px 0 rgba(107,59,90,.18);font-family:'Caveat Brush';font-style:normal;font-weight:400;font-size:60px;line-height:1.1;color:#B23A62\">only if over 1 and can swallow liquids</span>", fs=116, sy=715, ss=50, chip="AAP HealthyChildren.org"),
        dict(kick="over age 1 only", head="Every 10 minutes, / *up to 6 times.*", sub="Never wait to find honey. Just go.", fs=128, sy=730, ss=50, chip="AAP HealthyChildren.org"),
        dict(kick="at the ER, say", head="“It might be a / *coin battery.*”", sub="Damage can start in 2 hours.", fs=128, sy=730, ss=50, chip="AAP HealthyChildren.org"),
        dict(kick="Do this:", head="Save the poison / *centre number tonight.*", sub="<span style=\"display:inline-block;padding:14px 30px;border-radius:26px;background:#FFF8EE;border:3px solid #6B3B5A;font:600 46px/1.35 Poppins;font-style:normal;color:#3A1F3D\">Canada: 1-844-764-7669<br>US: 1-800-222-1222</span>", sy=680, fs=120, chip="Health Canada · AAP HealthyChildren.org"),
    ])

SPEC_MEDICINE = dict(
    out="lf-reel-1105am-medicine-mL", music=LIB / "v4/lf-x-giggle-pop.mp3", scene="medicine", follow=FOLLOW, follow_y=700,
    follow_at=0.6, garments=["none"] * 4,
    durs=[8 * BG, 6 * BG, 6 * BG, 3.2],
    beats=[
        dict(kick="kids' medicine?", head="0.5 mL is / *not 5 mL.*", sub="A mix-up is 10 times too much.", fs=150, sy=730, ss=50, chip="AAP HealthyChildren.org"),
        dict(kick="", head="Kitchen spoons come / *in lots of sizes.*", sub="So never measure medicine with one.", fs=118, sy=730, ss=50, chip="AAP HealthyChildren.org · NHS"),
        dict(kick="use this", head="The syringe that / *came with it.*", sub="No syringe? Ask your pharmacist for one.", fs=130, sy=730, ss=50, chip="AAP HealthyChildren.org · NHS"),
        dict(kick="Do this:", head="Measure in mL, / *with its own syringe.*", fs=124, chip="AAP HealthyChildren.org"),
    ])

SPECS = {"battery": SPEC_BATTERY, "honey": SPEC_HONEY, "medicine": SPEC_MEDICINE}

# =====================================================================================================================
# Covers (dedicated, 2x)
# =====================================================================================================================
BLOBS = S27.BLOBS


def _cover(body_html, art_js):
    return RS.page(W, H, body_html + f"<script>{RS.JS}\nT=0;{art_js}</script>")


def cover_battery_html():
    """Sticky-note list (style #13, quiet): lined note card, red margin, tape strip, Caveat Brush title, Caveat items + ticks."""
    items = ["remotes", "key fobs", "musical cards", "flameless candles", "toys and scales"]
    lis = "".join(f'<div style="height:96px;line-height:96px"><span style="color:#D9497A;margin-right:18px">✓</span>{x}</div>' for x in items)
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFE9C9,#FFD9B8)"></div>'
            + BLOBS.format(a="#FFD6E3", b="#FFE27E", c="#CFE3F6") + '<div class="grain" style="opacity:.3"></div>'
            + '<div style="position:absolute;left:90px;top:240px"><span style="display:inline-block;padding:8px 24px;border-radius:99px;background:#D9497A;color:#FFF8EE;font:600 30px Poppins;letter-spacing:.06em">PART 1 · COIN BATTERIES</span></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:315px;font-size:70px;color:{KICK}">a swallowed coin battery</div>'
            + K.dual("Can burn a throat / *in 2 hours.*", F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:400px;white-space:nowrap;font-size:132px;color:{INK}")
            + '<div style="position:absolute;left:110px;top:720px;width:860px;height:660px;background:#FFFDF6;transform:rotate(-2deg);border-radius:6px;'
              'box-shadow:0 24px 40px rgba(107,59,90,.18);background-image:linear-gradient(#FFFDF6 150px,transparent 150px),repeating-linear-gradient(#FFFDF6 0 94px,rgba(80,110,180,.28) 94px 96px)">'
              '<div style="position:absolute;left:96px;top:0;bottom:0;width:3px;background:rgba(220,80,80,.45)"></div>'
              '<div style="position:absolute;left:130px;top:44px;font-family:\'Caveat Brush\';font-size:92px;color:#D9497A;line-height:1">where they hide:</div>'
              f'<div style="position:absolute;left:130px;top:150px;font-family:Caveat;font-weight:700;font-size:72px;color:#3A1F3D">{lis}</div></div>'
            + '<div style="position:absolute;left:420px;top:690px;width:240px;height:64px;background:rgba(255,255,255,.6);transform:rotate(3deg);box-shadow:0 2px 6px rgba(0,0,0,.08)"></div>'
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:3" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    art = "document.getElementById('art').innerHTML=coinBat(770,1060,1.25,-12)+nickel(870,1180,1.2)+sparkle(700,980,0.9,1);"
    return _cover(body, art)


def cover_honey_html():
    """Ep.01 reframe 'instead of... / try...' (style #7, quiet): two stacked cards on a butter field."""
    card = ('<div style="position:absolute;left:90px;width:900px;top:{y}px;height:{h}px;border-radius:36px;background:{bg};'
            'box-shadow:0 14px 0 rgba(107,59,90,.12);border:5px solid #6B3B5A"></div>'
            '<div class="hand" style="position:absolute;left:140px;top:{ly}px;font-size:66px;color:#B23A62;text-align:left">{lab}</div>'
            '<div class="lora" style="position:absolute;left:140px;top:{ty}px;width:560px;font-size:76px;font-weight:700;color:#3A1F3D;line-height:1.05">{txt}</div>')
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF1BF,#FFE08A)"></div>'
            + BLOBS.format(a="#FFD3AE", b="#FFF8E4", c="#FFC9D6") + '<div class="grain" style="opacity:.3"></div>'
            + '<div style="position:absolute;left:90px;top:240px"><span style="display:inline-block;padding:8px 24px;border-radius:99px;background:#D9497A;color:#FFF8EE;font:600 30px Poppins;letter-spacing:.06em">PART 2 · COIN BATTERIES</span></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:320px;font-size:70px;color:{KICK}">battery swallowed?</div>'
            + K.dual("ER now. On the way: / *2 teaspoons of honey.*", F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:405px;white-space:nowrap;font-size:120px;color:{INK}")
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:630px;font-size:54px;color:{KICK}">only if over 1 and can swallow liquids</div>'
            + card.format(y=740, h=290, bg="#FFFDF7", ly=760, lab="instead of…", ty=850, txt="waiting to see")
            + card.format(y=1070, h=330, bg="#FCE5EB", ly=1095, lab="try…", ty=1185, txt="ER now, honey<br>on the way")
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:3" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    art = ("document.getElementById('art').innerHTML=clockF(840,880,90,1)+noRing(840,880,110,1)"
           "+`<g transform='translate(850 1250) scale(.85) translate(-850 -1250)'>`+honeyJar(850,1250)+`</g>`;")
    return _cover(body, art)


def cover_medicine_html():
    """Kinetic big text (style #5, loud): giant '0.5' vs '5' on a blush field, the two syringes under them."""
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFE3EC,#FFD0DC)"></div>'
            + BLOBS.format(a="#FFE27E", b="#FFF8E4", c="#FFD3AE") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:300px;font-size:76px;color:{KICK}">kids\' medicine?</div>'
            + '<div class="lora" style="position:absolute;left:0;width:1080px;top:400px;text-align:center;font-weight:700;font-size:250px;line-height:1;color:#D9497A;text-shadow:8px 8px 0 #FFFFFF">0.5 mL</div>'
            + f'<div class="lora" style="position:absolute;left:0;width:1080px;top:660px;text-align:center;font-weight:700;font-size:120px;line-height:1;color:{INK}">is not</div>'
            + '<div class="lora" style="position:absolute;left:0;width:1080px;top:790px;text-align:center;font-weight:700;font-size:250px;line-height:1;color:#D9497A;text-shadow:8px 8px 0 #FFFFFF">5 mL</div>'
            + f'<div class="hand" style="position:absolute;left:60px;width:960px;top:1310px;text-align:center;font-size:64px;color:{KICK};z-index:4">use the syringe that came with it ♡</div>'
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:3" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    art = "document.getElementById('art').innerHTML=syringeH(560,1120,500,0.1,0.95)+syringeH(560,1240,500,1,0.95);"
    return _cover(body, art)


COVERS = {"battery": cover_battery_html, "honey": cover_honey_html, "medicine": cover_medicine_html}


def use(key):
    RS.JS = S27.BASE_JS + S27.JS_TEETH + N1.JS + JS
    RS.html = N1.html
    return SPECS[key], COVERS[key]


if __name__ == "__main__":
    for a in sys.argv:
        if a.startswith("--still="):
            RS.STILLS = [float(x) for x in a[8:].split(",")]
        if a.startswith("--sw="):
            RS.SW = int(a[5:])
    for key in [a for a in sys.argv[1:] if not a.startswith("--")]:
        s, ch = use(key)
        OUT.mkdir(parents=True, exist_ok=True)
        if "--no-cover" not in sys.argv:
            S27.render_cover(ch(), OUT / f"{s['out']}-cover.jpg")
        if "--cover-only" in sys.argv:
            continue
        r = RS.frames(s, key)
        if r is None:
            print("stills", RS.SCR / f"{key}-stills.jpg")
            continue
        fdir, total, starts = r
        pops = [(st + 0.1, 0.22) for k, st in enumerate(starts) if k > 0]
        out = OUT / f"{s['out']}.mp4"
        N1.encode(fdir, total, s["music"], pops, out)
        print(out, round(total, 2), flush=True)

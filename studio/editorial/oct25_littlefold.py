#!/usr/bin/env python3
"""Oct 25 (Social studio, Littlefold maker): three Reels in the proven 'sunshine washing-line' story system
(studio/recovery-oct22c/littlefold/reel_story.py, imported, not edited; Oct 24 props imported from oct24_lf_a.py).
Each Reel has its own drawn vignettes that SHOW the check being done:

  SC.neck  - (send test) blankets keep dropping onto a baby's shoulders (seen from behind, no face); two adult fingers
             touch the back of the neck; sweat drops appear, the top blanket lifts off and flies up to be pegged on the
             washing line; a cool little hand and foot get frost sparkles and a 'normal' check; Do this: one light layer,
             fingers on the neck, hearts.
  SC.kiss  - side view of a parent wearing a baby in a sling: the parent tips their head forward and kisses the baby's
             head (heart pops); a low, saggy sling leaves a dashed gap, the strap pulls snug and the baby rides up;
             fabric over the baby's head slides away and a sightline draws from the parent's eye; Do this: tip, kiss.
  SC.chin  - (part 2) close-up of the baby's sleeping profile in the sling: an adult finger slides into the gap under the
             chin; the chin curls onto the chest, breath swirls stall, a 'no' ring, the head lifts and the swirls flow;
             a slumped baby in a loose sling is pulled snug and upright; Do this: finger under the chin, hearts.

No 'Little Rules' pill (unapproved). Facts: NHS (SIDS page, T.I.C.K.S.), The Lullaby Trust, NHS Fife (checked Oct 25 2026).

    python3 studio/editorial/oct25_littlefold.py neck|kiss|chin [--still=0.1,1.5,...] [--cover-only]
"""
import os
import sys
from pathlib import Path
sys.dont_write_bytecode = True
os.environ.setdefault("LF_SCR", "/tmp/claude-0/lf25")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oct24_lf_a as A  # noqa: E402  (adds palm, babyBack, babyHand, moon, zzz ... to RS.JS; patches the cover kicker size)
RS = A.RS

OUT = RS.REPO / "media" / "studio-oct25" / "littlefold"
FOLLOW = "Follow for one calm thing a night ☀"
V4 = RS.LIB / "v4"
BB = 60 / 112.3   # lf-x-sunny-bounce
BP = 60 / 103.4   # lf-x-tiny-parade
BG = 60 / 120.2   # lf-x-giggle-pop

RS.JS += r"""
// ===================== Oct 25 props =====================
function twoFingers(x,y,rot,s){ // adult index + middle finger from the right, tips at the origin
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
 <path d="M120 -64 Q240 -76 300 -40 L300 70 Q220 92 120 64 Z" fill="${SK}" ${o}/>
 <rect x="0" y="-38" width="170" height="34" rx="17" fill="${SK}" ${o}/>
 <rect x="10" y="4" width="166" height="34" rx="17" fill="${SK}" ${o}/>
 <path d="M14 -30 q-8 9 0 18 M24 12 q-8 9 0 18" stroke="${SKD}" stroke-width="3" fill="none"/>
 <path d="M150 50 Q200 80 250 40" stroke="${SKD}" stroke-width="4" fill="none"/></g>`;}
function shawl(y,col,op,len,wd){ len=len||132; wd=wd||128; // a soft blanket draped over the shoulders (baby seen from behind)
 let d=`M-104 ${y+8} Q0 ${y-34} 104 ${y+8} L${wd} ${y+len}`;
 for(let i=6;i>=0;i--){const xx=-wd+2*wd*i/6;d+=` Q${xx+wd/6} ${y+len+18} ${xx} ${y+len}`;} d+=' Z';
 return `<g opacity="${op}"><path d="${d}" fill="${col}" ${o}/><path d="M-60 ${y+20} Q-50 ${y+70} -66 ${y+124} M60 ${y+20} Q50 ${y+70} 66 ${y+124}" stroke="${PL}" stroke-width="3" fill="none" opacity=".45"/></g>`;}
function drops(t,x,y,op){let s='';for(let i=0;i<3;i++){const k=(t*0.8+i/3)%1;const dx=x+(i-1)*34, dy=y+30*k;
 s+=`<path d="M${dx} ${dy-14} q-11 16 0 22 q11 -6 0 -22z" fill="${BLUE}" stroke="${PL}" stroke-width="3" opacity="${op*(1-0.6*k)}"/>`;}return s;}
function pulse(x,y,k){if(k<=0)return '';let s='';for(let i=0;i<2;i++){const q=(k*1.4+i*0.5)%1;s+=`<circle cx="${x}" cy="${y}" r="${18+50*q}" fill="none" stroke="#B23A62" stroke-width="4" opacity="${0.7*(1-q)}"/>`;}return s;}
function frost(x,y,s,op){return `<g transform="translate(${x} ${y}) scale(${s})" opacity="${op}">${[0,60,120].map(r=>`<path d="M-22 0 H22" transform="rotate(${r})" stroke="#7FB3E0" stroke-width="6" stroke-linecap="round"/>`).join('')}<circle r="5" fill="#7FB3E0"/></g>`;}
function foot(x,y,rot,s){ // little bare foot, sole towards us, onesie leg
 let toes='';[[-34,-112,15],[-12,-122,13],[8,-122,12],[26,-116,11],[42,-104,10]].forEach(([tx,ty,r])=>{toes+=`<circle cx="${tx}" cy="${ty}" r="${r}" fill="${BSK}" ${o} stroke-width="4"/>`;});
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
 <path d="M-56 60 L-60 240 L60 240 L56 60Z" fill="${PINK}" ${o}/><path d="M-58 90 Q0 80 58 90 M-58 106 Q0 96 58 106" stroke="${PL}" stroke-width="3" fill="none" opacity=".5"/>
 ${toes}<path d="M-50 -90 Q-66 -20 -46 50 Q0 80 46 50 Q62 -20 52 -90 Q0 -118 -50 -90Z" fill="${BSK}" ${o}/>
 <path d="M-20 10 Q0 24 20 10" stroke="#E8A98A" stroke-width="4" fill="none" stroke-linecap="round"/></g>`;}
function bundleBack(t,layers,lift,tx){ // baby from behind, onesie, blankets stacked over the shoulders
 const cols=[BUT,BLUE,PEACH]; let s='';
 s+=babyBack(0,0,0,1.0);
 for(let i=0;i<layers.length;i++){const k=layers[i]; if(k<=0) continue;
  const off=i==layers.length-1?lift:0; const y=-48-i*6-240*(1-E(k))-off*320;
  s+=`<g transform="translate(${off*260} 0) rotate(${off*-18})">`+shawl(y,cols[i%3],Math.min(1,k*3)*(1-off),150-34*i,140-8*i)+`</g>`;}
 return s;}
SC.neck=[
 (lt,D,t)=>{ // blankets pile on; two fingers come in and touch the back of the neck
   const L=[1, seg(lt,0,0.35)+1, seg(lt,0.25,0.75)].map(v=>Math.min(v,1));
   const fin=E(seg(lt,0.7,1.3));
   let s=bundleBack(t,L,0,0);
   if(fin>0) s+=twoFingers(22+600*(1-fin),-50,8,0.8); s+=pulse(22,-50,seg(lt,1.3,3.2));  // r2: hand fully off-frame until it slides in (clean frame 0)
   if(lt>0.5) s+=label(-175,-185,lt<1.2?'another blanket?':'feel here',-6,46);
   if(lt>1.25) s+=`<path d="M-150 -165 Q-60 -160 0 -78" stroke="#B23A62" stroke-width="5" fill="none" stroke-dasharray="6 12" stroke-linecap="round"/>`;
   return stage(s,40,1.4,150);},
 (lt,D,t)=>{ // hot and sweaty: drops, then the top blanket lifts away (pegged on the line); check
   const lift=EIO(seg(lt,1.0,1.7));
   let s=bundleBack(t,[1,1,1],lift,0);
   s+=drops(t,-10,-30,1-seg(lt,1.6,2.0))+twoFingers(22,-50,8,0.8);
   s+=label(-175,-185,lt<1.0?'sweaty? too hot':'one layer off',-6,46);
   if(lt>2.0) s+=check(-190,40,seg(lt,2.0,2.5));
   return stage(s,40,1.4,150);},
 (lt,D,t)=>{ // cool hand + cool foot: frost sparkles, 'normal' check
   const a=E(seg(lt,0,0.4)), b=E(seg(lt,0.35,0.8));
   let s=`<g opacity="${a}">`+babyHand(-150,40,-8,0.95,[0,0,0,0],300)+`</g><g opacity="${b}">`+foot(170,60,8,0.95)+`</g>`;
   for(let i=0;i<3;i++){s+=frost(-260+i*90,-150+((i*37)%40),0.8+0.2*Math.sin(t*4+i),seg(lt,0.6+i*0.15,1.0+i*0.15));s+=frost(90+i*80,-130+((i*29)%40),0.8+0.2*Math.sin(t*4+i+1),seg(lt,0.8+i*0.15,1.2+i*0.15));}
   s+=label(-150,330,'cool hands',-4,46)+label(170,330,'cool feet',-4,46);
   if(lt>1.3) s+=check(10,90,seg(lt,1.3,1.8))+label(10,10,'normal',-4,50);
   return stage(s,40,1.1,20);},
 (lt,D,t)=>{ // do this: two layers, fingers resting on the neck, hearts
   let s=bundleBack(t,[1,1],0,0)+twoFingers(22,-50,8,0.8)+pulse(22,-50,lt*0.5)+hearts(t,-200,40);
   return stage(s,40,1.4,150);},
];
SC.neck.special=(beat,lt)=>(y0,sag)=>{ // beat 1: the top blanket flies up and is pegged on the line; stays there after
  if(beat<1) return ''; const f=beat>1?1:EIO(seg(lt,1.0,1.9)); if(f<=0) return '';
  const tx=930, ty=lineY(930,y0,sag)+4, sx=760, sy=1080; const X=sx+(tx-sx)*f+170*Math.sin(Math.PI*f), Y=sy+(ty-sy)*E(f);
  const fold=`<path d="M-60 0 H60 L70 120 Q35 136 0 124 Q-35 136 -70 120Z" fill="${PEACH}" ${o}/><path d="M-30 6 V118 M30 6 V118" stroke="${PL}" stroke-width="3" opacity=".4"/>`;
  return `<g transform="translate(${X} ${Y}) rotate(${-20*(1-f)+4*Math.sin(T*2)}) scale(.9)">${fold}${f>0.98?peg(-40)+peg(40):''}</g>`;};

// ---------- sling, side view (parent faces right; baby on the chest, facing in, no baby face)
function parentSide(tilt,eyeLine){ // torso + arm; head rotates forward about the neck (tilt 0..1)
 const P=[-95,-95];
 let s=`<path d="M-230 470 L-230 40 Q-226 -40 -150 -60 L-60 -66 Q0 -50 10 30 L30 470Z" fill="${BLUE}" ${o}/>`;
 s+=`<rect x="-120" y="-118" width="54" height="70" fill="${SK}" ${o}/>`;
 s+=`<g transform="rotate(${42*tilt} ${P[0]} ${P[1]})">
  <ellipse cx="-80" cy="-160" rx="74" ry="80" fill="${SK}" ${o}/>
  <path d="M-12 -170 Q8 -150 -6 -132" fill="${SK}" ${o}/>
  <path d="M-150 -170 Q-150 -250 -70 -244 Q-6 -236 -4 -190 Q-30 -214 -70 -210 Q-110 -206 -126 -150 Z" fill="#8A5A44" ${o}/>
  <path d="M-46 -176 q10 9 20 0" stroke="#5A2E22" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M-26 -116 q12 6 20 -4" stroke="#9A4E2A" stroke-width="5" fill="none" stroke-linecap="round"/>
  <circle cx="-44" cy="-140" r="11" fill="#FF9EA8" opacity=".6"/>
  ${eyeLine?`<path d="M-30 -168 L120 60" stroke="#B23A62" stroke-width="5" stroke-dasharray="6 12" stroke-linecap="round" opacity="${eyeLine}"/>`:''}</g>`;
 return s;}
function mouthAt(tilt){const a=42*tilt*Math.PI/180, x=-12+95, y=-122+95; return [-95+x*Math.cos(a)-y*Math.sin(a), -95+x*Math.sin(a)+y*Math.cos(a)];}
function babyIn(y,rot,cover){ // baby head (from behind/side, hair + ear) in a sage wrap on the chest; y = head centre
 let s=`<g transform="translate(70 ${y}) rotate(${rot})">
  <path d="M-80 30 Q-96 150 -60 230 Q10 262 80 220 Q104 120 82 26 Q0 0 -80 30Z" fill="${PINK}" ${o}/>
  <ellipse cx="-10" cy="-2" rx="58" ry="60" fill="${BSK}" ${o}/>
  <ellipse cx="22" cy="6" rx="12" ry="16" fill="${BSK}" ${o} stroke-width="4"/>
  <path d="M-18 -48 q14 -14 26 -2 q8 12 -6 18 q-12 4 -12 -8" stroke="#A0674A" stroke-width="4.5" fill="none" stroke-linecap="round"/></g>`;
 return s;}
function wrap(y,slack,over){ // sling fabric around the baby body + strap over the parent's shoulder
 const top=y+42+(over||0)*-150, bot=y+250+60*slack;
 return `<path d="M-120 -40 Q-30 -70 30 ${top-10}" stroke="${PL}" stroke-width="44" fill="none" stroke-linecap="round"/><path d="M-120 -40 Q-30 -70 30 ${top-10}" stroke="#A8CA9A" stroke-width="36" fill="none" stroke-linecap="round"/>
 <path d="M-8 ${top} Q70 ${top-18-20*slack} 160 ${top+10} Q${190+40*slack} ${(top+bot)/2} 150 ${bot} Q60 ${bot+30} -8 ${bot-6}Z" fill="${SAGE}" ${o}/>
 <path d="M20 ${top+40} Q90 ${top+30} 150 ${top+50} M20 ${top+100} Q90 ${top+90} 158 ${top+110}" stroke="${PL}" stroke-width="3.5" fill="none" opacity=".45"/>`;}
SC.kiss=[
 (lt,D,t)=>{ // tip head forward, kiss the baby's head, heart pops
   const tilt=EIO(seg(lt,0.35,1.1))*(1-0.6*EIO(seg(lt,2.2,2.8)));
   let s=parentSide(tilt,0)+babyIn(-40+3*Math.sin(t*2),0,0)+wrap(-40,0,0);
   const [mx,my]=mouthAt(tilt);
   if(lt>1.05){const k=seg(lt,1.05,2.2);s+=heartP(mx+20,my-30-90*k,1.6,Math.sin(Math.PI*k));}
   s+=label(250,-200,lt<1.05?'tip your head…':'kiss ✓',-6,58);
   return stage(s,0,1.22,150);},
 (lt,D,t)=>{ // too low: dashed gap; strap pulls snug; baby rides up; check
   const up=EIO(seg(lt,0.9,1.7)), tilt=0.95;
   const by=110-150*up, sl=1-up;
   let s=parentSide(tilt,0)+babyIn(by,6*sl,0)+wrap(by,sl,0);
   const [mx,my]=mouthAt(tilt);
   if(up<0.7) s+=`<path d="M${mx} ${my} L${mx+70} ${by-40}" stroke="#B23A62" stroke-width="6" stroke-dasharray="4 12" stroke-linecap="round" opacity="${1-up/0.7}"/>`+label(260,-120,'too low',-5,58);
   else s+=label(260,-200,'snug and high',-5,54);
   if(lt>0.9&&lt<1.8) s+=`<path d="M-150 -70 l-40 -50 M-150 -70 l-60 -18" stroke="#B23A62" stroke-width="6" stroke-linecap="round" opacity="${Math.sin(Math.PI*seg(lt,0.9,1.8))}"/>`;
   if(lt>1.8) s+=check(250,-60,seg(lt,1.8,2.3));
   return stage(s,0,1.22,150);},
 (lt,D,t)=>{ // fabric over the head slides away; sightline from the eye; check
   const off=EIO(seg(lt,0.3,1.0));
   let s=parentSide(0.35,seg(lt,1.0,1.4))+babyIn(-40,0,0)+wrap(-40,0,1-off);
   s+=label(250,-200,off<1?'fabric off their face':'see them at a glance',-5,50);
   if(lt>1.5) s+=check(250,-70,seg(lt,1.5,2.0));
   return stage(s,0,1.22,150);},
 (lt,D,t)=>{ // do this: tip + kiss loop, hearts
   const tilt=0.5+0.5*Math.sin(Math.min(lt*2.2,Math.PI/2));
   let s=parentSide(tilt,0)+babyIn(-40+3*Math.sin(t*2),0,0)+wrap(-40,0,0)+hearts(t,300,40);
   return stage(s,0,1.22,150);},
];
SC.kiss.special=(beat,lt)=>(y0,sag)=>'';

// ---------- chin close-up (baby profile facing left, sleeping, in the sling)
function profile(rot,breath,t){ // head rotates about the neck (rot>0 curls the chin down)
 let s=chinWrap()+`<path d="M-150 120 Q-170 260 -120 420 L230 420 Q260 260 210 120 Q40 70 -150 120Z" fill="${SAGE}" ${o}/>
  <path d="M-110 200 Q40 170 200 210 M-120 290 Q40 260 220 300" stroke="${PL}" stroke-width="3.5" fill="none" opacity=".45"/>`;
 s+=`<g transform="rotate(${rot} 40 90)">
  <circle cx="40" cy="-30" r="118" fill="${BSK}" ${o}/>
  <path d="M-78 -40 Q-102 -26 -86 -4 Q-80 4 -74 6" fill="${BSK}" ${o}/>
  <path d="M-62 56 Q-50 92 -6 96" fill="none" ${o}/>
  <path d="M-40 -46 q16 12 34 0" stroke="#5A2E22" stroke-width="6" fill="none" stroke-linecap="round"/>
  <circle cx="-26" cy="0" r="17" fill="#FF9EA8" opacity=".6"/>
  <path d="M-58 36 q8 6 16 0" stroke="#9A4E2A" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M66 -30 q22 -6 24 16 q2 22 -20 24" fill="${BSK}" ${o} stroke-width="4"/><path d="M72 -16 q10 0 8 10" stroke="#E8A98A" stroke-width="3.5" fill="none"/>
  <path d="M-98 -14 q-16 14 -2 26" fill="${BSK}" ${o} stroke-width="4"/>
  <path d="M10 -142 q20 -22 40 -4 q12 18 -8 26 q-18 6 -18 -12" stroke="#A0674A" stroke-width="5" fill="none" stroke-linecap="round"/></g>`;
 if(breath>0){for(let i=0;i<3;i++){const k=(t*0.7+i/3)%1;const bx=-120-120*k, by=10-20*Math.sin(k*6+i);
   s+=`<path d="M${bx+30} ${by} q-14 -16 -28 0 q-14 16 -28 0" stroke="#7FB3E0" stroke-width="5" fill="none" stroke-linecap="round" opacity="${breath*Math.sin(Math.PI*k)}"/>`;}}
 return s;}
function finger(x,y,rot,s){return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
 <path d="M150 -50 Q260 -70 330 -30 L340 90 Q250 120 160 70 Q120 40 150 -50Z" fill="${SK}" ${o}/>
 <path d="M168 20 Q200 40 236 30 M172 52 Q206 72 244 62" stroke="${SKD}" stroke-width="4" fill="none"/>
 <rect x="0" y="-20" width="190" height="40" rx="20" fill="${SK}" ${o}/>
 <path d="M8 -12 q-8 12 0 24" stroke="${SKD}" stroke-width="3" fill="none"/><path d="M60 -20 v6 M60 14 v6" stroke="${SKD}" stroke-width="3"/></g>`;}
function chinWrap(){return `<path d="M-150 130 Q-300 60 -420 -120" stroke="${PL}" stroke-width="58" fill="none" stroke-linecap="round"/><path d="M-150 130 Q-300 60 -420 -120" stroke="#A8CA9A" stroke-width="48" fill="none" stroke-linecap="round"/>`;}
SC.chin=[
 (lt,D,t)=>{ // finger slides into the gap under the chin, check
   const a=E(seg(lt,0.4,1.2));
   let s=profile(8,1,t)+`<g transform="scale(-1 1)">`+finger(40+320*(1-a),104,-30,0.8)+`</g>`;
   s+=label(-170,-190,lt<1.2?'room under the chin?':'one finger fits ✓',-5,54);
   if(lt>1.3) s+=check(-200,250,seg(lt,1.3,1.8));
   return stage(s,40,1.0,60);},
 (lt,D,t)=>{ // chin curls down, breath stalls, no ring; head lifts, breath flows
   const curl=EIO(seg(lt,0.1,0.7))*(1-EIO(seg(lt,1.9,2.6)));
   let s=profile(8-36*curl,1-curl,t);
   if(lt>0.6&&lt<2.2) s+=`<g opacity="${1-seg(lt,1.9,2.2)}">`+noRing(-60,110,80,seg(lt,0.6,1.3))+`</g>`;
   s+=label(-170,-190,curl>0.5?'chin on chest':'chin up, breathing easy',-5,52);
   return stage(s,40,1.0,60);},
 (lt,D,t)=>{ // slumped in a loose sling -> pulled snug and upright (side view)
   const up=EIO(seg(lt,0.6,1.5)); const by=110-150*up;
   let s=parentSide(0,0)+babyIn(by,18*(1-up),0)+wrap(by,1-up,0);
   s+=label(260,-200,up<0.5?'slumped low':'snug, upright',-5,54);
   if(lt>1.6) s+=check(250,-60,seg(lt,1.6,2.1));
   return stage(s,0,1.22,150);},
 (lt,D,t)=>{ // do this: finger under the chin, breath flowing, hearts
   let s=profile(8,1,t)+`<g transform="scale(-1 1)">`+finger(40,104,-30,0.8)+`</g>`+hearts(t,260,80);
   return stage(s,40,1.0,60);},
];
SC.chin.special=(beat,lt)=>(y0,sag)=>'';
"""

CHIP_NECK = "NHS · The Lullaby Trust"
CHIP_SLING = "NHS · T.I.C.K.S. sling safety"

RS.SPECS["neck"] = dict(
    out="lf-reel-1026-neck-check", outdir=OUT, music=V4 / "lf-x-sunny-bounce.mp3", scene="neck", follow=FOLLOW,
    sky=("dawn", "morning"), garments=["hat", "sock", "onesie", "dress", "none"],
    durs=[6 * BB, 6 * BB, 6 * BB, 9 * BB], extra_pops=[], cover_beat=0, cover_lt=2.2,
    cover=dict(kick="for whoever keeps adding blankets", head="Feel the back / of their *neck.*", fs=170, pill="", py=1000),
    beats=[
        dict(kick="for whoever keeps adding blankets", head="Feel the back / of their *neck.*", fs=150, chip=CHIP_NECK),
        dict(kick="hot or sweaty?", head="Take a / *layer off.*", fs=160, chip=CHIP_NECK),
        dict(kick="and don't worry", head="Cool hands and / feet are *normal.*", fs=140, chip=CHIP_NECK),
        dict(kick="Do this:", head="Check the *neck,* / not the hands.", sub="send this to whoever keeps adding blankets", fs=140, sy=860, ss=42, chip=CHIP_NECK),
    ])

RS.SPECS["kiss"] = dict(
    out="lf-reel-1027-sling-kiss", outdir=OUT, music=V4 / "lf-x-tiny-parade.mp3", scene="kiss", follow=FOLLOW,
    sky=("dawn", "morning"), garments=["onesie", "bib", "sock", "hat", "dress"],
    durs=[6 * BP, 6 * BP, 5 * BP, 8 * BP], extra_pops=[], cover_beat=0, cover_lt=1.6,
    cover=dict(kick="baby in a sling?", head="Can you *kiss* / their head?", fs=170, pill="", py=1000),
    beats=[
        dict(kick="baby in a sling?", head="Can you *kiss* / their head?", fs=160, chip=CHIP_SLING),
        dict(kick="if you can't", head="Snug it up. / *Lift them higher.*", fs=140, chip=CHIP_SLING),
        dict(kick="and", head="Always see / *their face.*", fs=160, chip=CHIP_SLING),
        dict(kick="Do this:", head="Tip your head. / *Kiss their head.*", sub="Part 2 tomorrow, 7 pm: the chin check.", fs=140, sy=860, ss=46, chip=CHIP_SLING),
    ])

RS.SPECS["chin"] = dict(
    out="lf-reel-1028-sling-chin", outdir=OUT, music=V4 / "lf-x-giggle-pop.mp3", scene="chin", follow=FOLLOW,
    sky=("dawn", "morning"), garments=["dress", "hat", "onesie", "sock", "bib"],
    durs=[7 * BG, 7 * BG, 7 * BG, 8 * BG], extra_pops=[], cover_beat=0, cover_lt=2.2,
    cover=dict(kick="baby in a sling? part 2", head="One *finger* / under the chin.", fs=165, pill="", py=1000),
    beats=[
        dict(kick="baby in a sling? part 2", head="One *finger* / under the chin.", fs=150, chip=CHIP_SLING),
        dict(kick="because", head="Chin on chest can / *restrict breathing.*", fs=126, chip=CHIP_SLING),
        dict(kick="and", head="Snug and upright, / *back supported.*", fs=130, chip=CHIP_SLING),
        dict(kick="Do this:", head="Slide one finger / *under their chin.*", sub="Part 1 was the kiss check.", fs=130, sy=860, ss=42, chip=CHIP_SLING),
    ])

# ---------------------------------------------------------------- r2 (gate fixes, Oct 25): neck check only
# 1 'baby's neck' in the headline + last beat; 2 clean frame 0 (hand off-frame); 3 hard text cuts between beats (HARD);
# 4 the sun dips behind the hill on 'hot or sweaty?' and rises again after (SUNDIP); 5 follow chip = the page FOLLOW line, no glyph.
RS.JS = RS.JS.replace("if(i==0){op=1;} else {const p=E(seg(lt,0.05,0.3)); op=p; y=40*(1-p);}",
                      "if(i==0||(typeof HARD!=='undefined'&&HARD)){op=1;} else {const p=E(seg(lt,0.05,0.3)); op=p; y=40*(1-p);}", 1)
RS.JS = RS.JS.replace("else if(k==i-1 && lt<0.12)", "else if(k==i-1 && lt<0.12 && !(typeof HARD!=='undefined'&&HARD))", 1)
RS.JS = RS.JS.replace("svg+=sun(870, 1430-60*prog-(S.cover?60:0), beam, t);",
                      "const _dip=(S.cover||typeof SUNDIP==='undefined')?0:(i==SUNDIP?340*EIO(seg(lt,0,0.3)):(i==SUNDIP+1?340*(1-EIO(seg(lt,0,0.6))):0));"
                      "svg+=sun(870, 1430-60*prog-(S.cover?60:0)+_dip, beam, t);", 1)
assert "SUNDIP" in RS.JS and RS.JS.count("HARD") >= 2
_html2 = RS.html


def _html_r2(spec, cover=None):
    h = _html2(spec, cover)
    if spec.get("r2"):
        h = h.replace("font:600 32px Poppins\">", "font:600 24px Poppins\">", 1) + "<script>var HARD=true, SUNDIP=1;</script>"
    return h


RS.html = _html_r2
FOLLOW_FULL = "Follow for one calm thing a night, from bump to toddler."
RS.SPECS["neck2"] = dict(RS.SPECS["neck"], out="lf-reel-1026-neck-check-r2", follow=FOLLOW_FULL, r2=True,
    cover=dict(kick="for whoever keeps adding blankets", head="Feel the back / of *baby's neck.*", fs=170, pill="", py=1000),
    beats=[
        dict(kick="for whoever keeps adding blankets", head="Feel the back / of *baby's neck.*", fs=150, chip=CHIP_NECK),
        dict(kick="hot or sweaty?", head="Take a / *layer off.*", fs=160, chip=CHIP_NECK),
        dict(kick="and don't worry", head="Cool hands and / feet are *normal.*", fs=140, chip=CHIP_NECK),
        dict(kick="Do this:", head="Check *baby's neck,* / not the hands.", sub="send this to whoever keeps adding blankets", fs=140, sy=860, ss=42, chip=CHIP_NECK),
    ])

if __name__ == "__main__":
    for a in sys.argv:
        if a.startswith("--still="):
            RS.STILLS = [float(x) for x in a[8:].split(",")]
        if a.startswith("--sw="):
            RS.SW = int(a[5:])
    for key in [a for a in sys.argv[1:] if not a.startswith("--")]:
        s = RS.SPECS[key]
        OUT.mkdir(parents=True, exist_ok=True)
        RS.frames(s, key, cover=s["cover"], cover_out=OUT / f"{s['out']}-cover.jpg")
        print("cover", OUT / f"{s['out']}-cover.jpg", flush=True)
        if "--cover-only" in sys.argv:
            continue
        r = RS.frames(s, key)
        if r is None:
            print("stills", RS.SCR / f"{key}-stills.jpg")
            continue
        fdir, total, starts = r
        pops = [(st + 0.1, 0.22) for k, st in enumerate(starts) if k > 0 and k not in s.get("no_pop", [])] + s["extra_pops"]
        out = OUT / f"{s['out']}.mp4"
        RS.encode(fdir, total, s["music"], pops, out)
        print(out, round(total, 2), flush=True)

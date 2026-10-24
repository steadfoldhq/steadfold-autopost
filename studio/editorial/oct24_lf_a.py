#!/usr/bin/env python3
"""Oct 24 (Social studio, LF maker A): two Littlefold Reels in the proven 'sunshine washing-line' story system
(studio/recovery-oct22c/littlefold/reel_story.py, imported, not edited). New drawn vignettes in the same line style:

  SC.burp  - bottle feed with 'gulp' air bubbles, the bottle pauses and a flat adult palm pats the back ('burp!');
             a bottle drains to the 2-3 oz mark and lifts away; a bundle moves across a nursing pillow from side 1 to
             side 2 with a burp at the top; three burping positions (over the shoulder / sitting on the lap /
             tummy-down across the lap) with a patting palm; Do this: shoulder pats, hearts, a burp cloth pegged on the line.
  SC.nails - a little baby hand (no face) with sharp nail tips; a soft emery board files each tip round; the hand
             sleeps on a blanket under a moon while an adult hand files; a tooth gets a 'no' ring (don't bite);
             Do this: sleeping hand, smooth nails, check and hearts.

No 'Little Rules' pill (unapproved series). Facts: AAP HealthyChildren.org + NHS 111 Wales (checked Oct 24 2026).

    python3 studio/editorial/oct24_lf_a.py burp|nails [--still=0.2,1.5,...] [--cover-only]
"""
import os
import sys
from pathlib import Path
sys.dont_write_bytecode = True
os.environ.setdefault("LF_SCR", "/tmp/claude-0/lf-a")
sys.path.insert(0, "/home/claude/steadfold-autopost/studio/recovery-oct22c/littlefold")
import reel_story as RS  # noqa: E402

OUT = RS.REPO / "media" / "studio-oct24" / "littlefold"
FOLLOW = "Follow for one calm thing a night ☀"
LIB = RS.LIB
BS = 60 / 120.2   # lf-c-sunny-morning-el
BT = 60 / 84.7    # lf-b-tender-el

RS.JS += r"""
// ===================== Oct 24 props =====================
const BSK='#FFDCC4';
function palm(x,y,rot,s){ // flat open adult hand, fingers together pointing -x
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
 ${[[-40,-118],[-18,-130],[4,-126],[26,-112]].map(([y,x])=>`<rect x="${x}" y="${y}" width="${-x+10}" height="22" rx="11" fill="${SK}" ${o} stroke-width="4"/>`).join('')}
 <path d="M-40 -46 Q40 -56 160 -46 L160 42 Q100 58 -40 50 Q-56 2 -40 -46Z" fill="${SK}" ${o}/>
 <path d="M30 -46 Q0 -90 -38 -88 Q-56 -82 -44 -66 Q-12 -60 14 -30" fill="${SK}" ${o}/></g>`;}
function patLines(x,y,k){let s='';for(let i=0;i<3;i++){const a=-0.6+i*0.6;s+=`<path d="M${x+40*Math.cos(a)} ${y+40*Math.sin(a)} L${x+66*Math.cos(a)} ${y+66*Math.sin(a)}" stroke="#B23A62" stroke-width="6" stroke-linecap="round" opacity="${k}"/>`;}return s;}
function bubbles(t,x,y,op){let s='';for(let i=0;i<5;i++){const k=(t*0.9+i*0.2)%1;const bx=x+(i-2)*24+10*Math.sin(t*4+i),by=y-150*k;
 s+=`<circle cx="${bx}" cy="${by}" r="${7+9*k}" fill="#FFFFFF" fill-opacity=".75" stroke="${PL}" stroke-width="3" opacity="${op*Math.sin(Math.PI*k)}"/>`;}return s;}
function popBurst(x,y,k){if(k<=0||k>=1)return '';let s='';const r=30+50*k;for(let i=0;i<8;i++){const a=i*Math.PI/4;
 s+=`<path d="M${x+r*Math.cos(a)} ${y+r*Math.sin(a)} L${x+(r+22)*Math.cos(a)} ${y+(r+22)*Math.sin(a)}" stroke="${BUT}" stroke-width="7" stroke-linecap="round" opacity="${1-k}"/>`;}return s;}
function bottle(x,y,rot,s,lv,ticks){ // origin = body centre, teat up
 const h=180, f=h*cl(lv,0,1);
 let tk='';if(ticks){for(let i=1;i<=4;i++){const yy=h/2-i*h/4.6;tk+=`<path d="M-46 ${yy} h20" stroke="${PL}" stroke-width="3.5"/>`;}}
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
 <path d="M-22 ${-h/2-34} Q0 ${-h/2-90} 22 ${-h/2-34} Z" fill="${BUT}" ${o}/>
 <rect x="-40" y="${-h/2-38}" width="80" height="32" rx="8" fill="${PINK}" ${o}/>
 <rect x="-46" y="${-h/2-8}" width="92" height="${h+8}" rx="26" fill="#E3EEF8" ${o}/>
 <rect x="-41" y="${h/2-f-3}" width="82" height="${f}" rx="${Math.min(22,f/2)}" fill="#FFFDF6"/>
 <rect x="-46" y="${-h/2-8}" width="92" height="${h+8}" rx="26" fill="none" ${o}/>${tk}</g>`;}
function adultShoulder(){ // parent (simple cartoon, eyes closed, smiling) holding baby up at the left shoulder
 return `<path d="M-180 440 L-180 150 Q-176 52 -80 34 L20 26 L120 26 Q240 40 250 150 L250 440Z" fill="${SAGE}" ${o}/>
 <path d="M-86 40 Q-130 120 -132 320 M156 40 Q210 120 208 320" stroke="${PL}" stroke-width="3.5" fill="none" opacity=".4"/>
 <rect x="34" y="-30" width="56" height="70" fill="${SK}" ${o}/><path d="M10 28 Q62 64 114 28" stroke="${PL}" stroke-width="4" fill="${SAGE}"/>
 <ellipse cx="64" cy="-96" rx="66" ry="72" fill="${SK}" ${o}/>
 <path d="M-4 -110 Q-2 -176 66 -174 Q138 -170 132 -96 Q120 -136 84 -140 Q30 -146 -4 -110Z" fill="#8A5A44" ${o}/>
 <circle cx="104" cy="-170" r="24" fill="#8A5A44" ${o}/>
 <path d="M44 -92 q11 10 22 0 M88 -92 q11 10 22 0" stroke="#5A2E22" stroke-width="5" fill="none" stroke-linecap="round"/>
 <path d="M64 -62 q14 12 28 0" stroke="#9A4E2A" stroke-width="5" fill="none" stroke-linecap="round"/>
 <circle cx="40" cy="-70" r="11" fill="#FF9EA8" opacity=".6"/><circle cx="114" cy="-70" r="11" fill="#FF9EA8" opacity=".6"/>`;}
function forearm(x,y,rot,s){ // adult forearm + cupped hand, pointing -x (supports the baby's bottom)
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})"><path d="M220 -30 L-40 -26 Q-90 -26 -100 0 Q-96 30 -40 30 L220 34Z" fill="${SK}" ${o}/>
 <path d="M-96 -6 Q-120 -30 -104 -44 Q-88 -40 -76 -22" fill="${SK}" ${o}/><path d="M-60 -10 Q-40 -4 -30 -12" stroke="${SKD}" stroke-width="4" fill="none"/></g>`;}
function babyBack(x,y,rot,s){ // baby seen from behind: round head with hair swirl + ears (no face), footed onesie, little arms
 const leg=(dx)=>`<path d="M${dx-20} 96 L${dx-22} 150 Q${dx-22} 172 ${dx} 172 Q${dx+22} 172 ${dx+20} 150 L${dx+20} 96Z" fill="${PINK}" ${o}/>`;
 const arm=(sg)=>`<path d="M${66*sg} -30 Q${104*sg} 0 ${100*sg} 52" stroke="${PL}" stroke-width="36" fill="none" stroke-linecap="round"/><path d="M${66*sg} -30 Q${104*sg} 0 ${100*sg} 52" stroke="${PINK}" stroke-width="27" fill="none" stroke-linecap="round"/><circle cx="${100*sg}" cy="66" r="15" fill="${BSK}" ${o} stroke-width="4"/>`;
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">${leg(-34)}${leg(34)}${arm(-1)}${arm(1)}
 <path d="M-72 -36 Q-92 40 -66 108 Q0 130 66 108 Q92 40 72 -36 Q40 -60 0 -60 Q-40 -60 -72 -36Z" fill="${PINK}" ${o}/>
 <path d="M0 -50 Q6 30 0 116" stroke="${PL}" stroke-width="3" fill="none" opacity=".35"/><circle cx="0" cy="-20" r="5" fill="${CREAM}" ${o} stroke-width="2.5"/><circle cx="0" cy="10" r="5" fill="${CREAM}" ${o} stroke-width="2.5"/>
 <ellipse cx="-58" cy="-104" rx="14" ry="19" fill="${BSK}" ${o} stroke-width="4"/><ellipse cx="58" cy="-104" rx="14" ry="19" fill="${BSK}" ${o} stroke-width="4"/>
 <circle cx="0" cy="-110" r="60" fill="${BSK}" ${o}/>
 <path d="M-6 -150 q14 -14 26 -2 q8 12 -6 18 q-12 4 -12 -8" stroke="#A0674A" stroke-width="4.5" fill="none" stroke-linecap="round"/>
 <path d="M-34 -150 q6 -12 16 -14 M26 -158 q10 2 16 12" stroke="#A0674A" stroke-width="4" fill="none" stroke-linecap="round"/></g>`;}
function thigh(){ // seated adult lap, side view
 return `<rect x="-300" y="230" width="480" height="104" rx="52" fill="${BLUE}" ${o}/><rect x="96" y="250" width="96" height="130" rx="40" fill="${BLUE}" ${o}/><path d="M-220 262 Q-60 250 60 262" stroke="${PL}" stroke-width="3.5" fill="none" opacity=".45"/>`;}
function pillow(){const d="M-230 120 Q-230 380 0 380 Q230 380 230 120";return `<path d="${d}" stroke="${PL}" stroke-width="130" fill="none" stroke-linecap="round"/><path d="${d}" stroke="${PEACH}" stroke-width="120" fill="none" stroke-linecap="round"/><path d="${d}" stroke="#FFE4CF" stroke-width="40" fill="none" stroke-linecap="round" opacity=".7"/>`;}
function table(x,y){return `<g transform="translate(${x} ${y})"><rect x="-90" y="0" width="180" height="22" rx="8" fill="${PEACH}" ${o}/><path d="M-70 22 V130 M70 22 V130" stroke="${PL}" stroke-width="6" stroke-linecap="round"/></g>`;}
function fuss(t,x,y,op){let s='';for(let i=0;i<2;i++){const sx=x+i*150, j=4*Math.sin(t*20+i);s+=`<path d="M${sx} ${y+j} l14 -14 l10 14 l14 -14" stroke="#B23A62" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="${op}"/>`;}return s;}
function burpPose(p,lp,t,wig){ // 0 over the shoulder, 1 tummy-down across the lap; patting palm on the back
 const pat=16*Math.abs(Math.sin(lp*9)), pk=0.5+0.5*Math.sin(lp*9); let s='';
 if(p==0){ s+=adultShoulder()+babyBack(-60,66,3+(wig||0),0.9)+forearm(-40,226,-4,0.8)+palm(70+pat,90,-6,0.68)+patLines(4,90,pk); }
 if(p==1){ s+=thigh()+babyBack(-30,170,-84,0.85)+palm(-250,182,180,0.58)+palm(120+pat,80,-28,0.66)+patLines(-10,120,pk); }
 return s;}
SC.burp=[
 (lt,D,t)=>{ // on the shoulder, squirming + gulped-air bubbles from frame 0; the bottle is set down (pause); pats; burp!
   const wig=6*Math.sin(t*15)*(1-seg(lt,1.8,2.1)), drop=E(seg(lt,0,0.45));
   let s=burpPose(0,lt>0.55?lt-0.55:0,t,wig);
   if(lt<0.55) s=adultShoulder()+babyBack(-60,66,3+wig,0.9)+forearm(-40,226,-4,0.8);
   s+=table(-290,280)+bottle(-290,180-260*(1-drop)+8*Math.sin(Math.PI*seg(lt,0.45,0.65)),-30*(1-drop),0.55,0.5,false);
   s+=bubbles(t,-60,-110,1-seg(lt,1.9,2.2))+fuss(t,-210,-60,1-seg(lt,1.7,2.0))+popBurst(-60,-170,seg(lt,1.85,2.35));
   if(lt<0.55) s+=label(220,-210,'gulp, gulp…',-6,58); else if(lt<1.85) s+=label(220,-210,'pause. pat.',-6,58); else s+=label(220,-210,'burp!',-8,70);
   return stage(s,10,1.05,140);},
 (lt,D,t)=>{ // bottle drains to 2-3 oz (gently tipping as baby drinks), lifts away
   const lv=1-0.62*EIO(seg(lt,0.1,1.5)), lift=EIO(seg(lt,1.55,2.0)); const oz=Math.min(3,1+Math.floor(3*seg(lt,0.1,1.5)));
   let s=bottle(-60,150-60*lift,-40*(1-lift)*seg(lt,0,0.3)+5*Math.sin(t*5)*(1-lift)+24*lift,1.35,lv,true);
   s+=bubbles(t,-60,40,1-seg(lt,1.5,1.7));
   if(lt<1.55) s+=label(200,60,`${oz} oz in…`,-5,60);
   else {s+=label(200,60,'pause. burp.',-5,60);}
   if(lt>2.0) s+=check(200,260,seg(lt,2.0,2.5));
   return stage(s,0,1.2,40);},
 (lt,D,t)=>{ // nursing pillow: side 1 -> up for a burp -> side 2
   const k=0.5*EIO(seg(lt,0.2,0.9))+0.5*EIO(seg(lt,1.9,2.6));
   const x=-230+460*k, y=150-230*Math.sin(Math.PI*k), rot=-60+120*k;
   let s=pillow()+label(-100,240,'side 1',-3,46)+label(100,240,'side 2',-3,46);
   s+=`<path d="M-230 60 Q0 -260 230 60" stroke="#B23A62" stroke-width="5" fill="none" stroke-dasharray="6 14" stroke-linecap="round" opacity=".7"/>`;
   s+=babyBack(x,y,rot,0.7)+cradle(x,y+70,0,0.8);
   if(lt>0.9&&lt<1.95){const lp=lt-0.9;s+=palm(x+90+16*Math.abs(Math.sin(lp*9)),y+10,-4,0.6)+patLines(x+30,y+10,0.5+0.5*Math.sin(lp*9))+popBurst(x,y-150,seg(lt,1.4,1.85));s+=label(x+250,y-80,'burp ✓',-6,58);}
   return stage(s,-50,1.0,20);},
 (lt,D,t)=>{ // two positions, 1.5 s each, slide transition
   const p=lt<1.5?0:1, lp=lt-p*1.5, sl=1-E(seg(lp,0,0.25));
   const L=['over your shoulder','tummy-down across your lap'];
   let s=`<g transform="translate(${p>0?160*sl:0} 0)" opacity="${p>0?1-sl*0.8:1}">`+burpPose(p,lp,t,0)+`</g>`;
   s+=label(-20,-250,L[p],-3,50);
   return stage(s,10,1.05,140);},
 (lt,D,t)=>{ // do this: shoulder pats, hearts, paused bottle on a table
   let s=burpPose(0,lt*0.6,t,0)+hearts(t,-60,-40)+table(-290,280)+bottle(-290,180,0,0.55,0.5,false);
   return stage(s,10,1.05,140);},
];
SC.burp.special=(beat,lt)=>(y0,sag)=>{ // Do this: a burp cloth flies up and is pegged on the line
  if(beat<4) return ''; const f=EIO(seg(lt,0.1,0.9)); const tx=930, ty=lineY(930,y0,sag);
  const sx=480, sy=1100; const X=sx+(tx-sx)*f, Y=sy+(ty-sy)*f-160*Math.sin(Math.PI*f);
  return `<g transform="translate(${X} ${Y}) rotate(${-20*(1-f)+4*Math.sin(T*2)}) scale(.88)">${G.bib()}</g>`;};
// ---------- nails
function babyHand(x,y,rot,s,nl,SL){ SL=SL||360; // little open hand, fingers up, nl = [4] nail overhang 0..1 (index..pinky)
 const F=[[-54,-6,64],[-18,-26,80],[18,-22,78],[52,-2,60]];
 let f='';F.forEach(([cx,dy,L],j)=>{const top=-60+dy-L, n=nl[j];
   f+=`<rect x="${cx-17}" y="${top}" width="34" height="${L+70}" rx="17" fill="${BSK}" ${o}/>`;
   if(n>0.03) f+=`<path d="M${cx-12} ${top+10} L${cx-5} ${top-14*n} L${cx} ${top-4-4*n} L${cx+5} ${top-14*n} L${cx+12} ${top+10}Z" fill="#FFFFFF" stroke="${PL}" stroke-width="3" stroke-linejoin="round"/>`;
   f+=`<path d="M${cx-11} ${top+20} Q${cx-11} ${top+5} ${cx} ${top+4} Q${cx+11} ${top+5} ${cx+11} ${top+20} Q${cx} ${top+25} ${cx-11} ${top+20}Z" fill="#FFF4EE" stroke="${PL}" stroke-width="2.5"/>`;});
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">${f}
 <path d="M-86 -50 Q-100 -20 -96 30 Q-86 104 0 110 Q86 104 92 30 Q96 -20 80 -50 Q0 -70 -86 -50Z" fill="${BSK}" ${o}/>
 <path d="M-88 40 Q-130 26 -134 -10 Q-132 -32 -112 -28 Q-100 -4 -80 6" fill="${BSK}" ${o}/>
 <path d="M-40 40 Q0 56 40 40" stroke="#E8A98A" stroke-width="4" fill="none" stroke-linecap="round"/>
 <path d="M-50 74 Q0 84 50 74" stroke="#E8A98A" stroke-width="4" fill="none" stroke-linecap="round"/>
 <path d="M-80 92 Q-90 ${92+SL*0.5} -96 ${92+SL} L96 ${92+SL} Q90 ${92+SL*0.5} 80 92 Q0 76 -80 92Z" fill="${PINK}" ${o}/>
 <path d="M-82 112 Q0 98 82 112 M-84 128 Q0 114 84 128" stroke="${PL}" stroke-width="3" fill="none" opacity=".5"/>
 <path d="M-40 ${92+SL*0.55} q12 -12 24 0 q12 -12 24 0" stroke="#FFF0F4" stroke-width="5" fill="none" stroke-linecap="round"/></g>`;}
function emery(x,y,rot,s){let g='';for(let i=0;i<14;i++)g+=`<circle cx="${-96+i*14.5}" cy="${(i%2?-5:5)}" r="2.6" fill="${PL}" opacity=".35"/>`;
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})"><rect x="-120" y="-17" width="240" height="34" rx="17" fill="${PINK}" ${o}/>${g}</g>`;}
function dust(t,x,y,op){let s='';for(let i=0;i<6;i++){const k=(t*1.6+i/6)%1;s+=`<circle cx="${x+(i-3)*9+6*Math.sin(i*2+t*5)}" cy="${y+60*k}" r="3.5" fill="#FFFFFF" stroke="${PL}" stroke-width="1.5" opacity="${op*(1-k)}"/>`;}return s;}
function moon(x,y){return `<path transform="translate(${x} ${y})" d="M20 -50 A52 52 0 1 0 50 34 A42 42 0 1 1 20 -50Z" fill="${BUT}" ${o}/>`;}
function zzz(t,x,y){let s='';for(let i=0;i<3;i++){const k=(t*0.5+i/3)%1;s+=`<text x="${x+30*k+i*6}" y="${y-80*k}" font-family="Caveat Brush" font-size="${36+20*k}" fill="#B23A62" opacity="${Math.sin(Math.PI*k)}">z</text>`;}return s;}
function tooth(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-60 -50 Q-70 -80 -36 -84 Q-16 -86 0 -74 Q16 -86 36 -84 Q70 -80 60 -50 Q56 0 40 60 Q30 80 18 60 L6 20 Q0 10 -6 20 L-18 60 Q-30 80 -40 60 Q-56 0 -60 -50Z" fill="#FFFFFF" ${o}/></g>`;}
const FX=[-54,-18,18,52], FT=[-130,-166,-160,-122]; // fingertip x / y (hand-local)
function sleeper(lt,t,nl,extra){ // SAFE SLEEP: baby on their back in a crib, seen from above, on a flat firm mattress with
 // a plain fitted sheet and nothing soft around; swaddle with hat (no face), one arm out, hand resting while it's filed
 const br=1+0.02*Math.sin(t*2.2); let sl='';
 for(let i=0;i<12;i++){const x=-262+i*47.6;sl+=`<path d="M${x} -46 V-26 M${x} 326 V346" stroke="${PL}" stroke-width="5" stroke-linecap="round"/>`;}
 for(let i=0;i<8;i++){const y=-6+i*46;sl+=`<path d="M-292 ${y} H-272 M292 ${y} H272" stroke="${PL}" stroke-width="5" stroke-linecap="round"/>`;}
 let s=`<rect x="-300" y="-56" width="600" height="412" rx="26" fill="${PEACH}" ${o}/>${sl}
 <rect x="-262" y="-18" width="524" height="336" rx="14" fill="#FFFDF6" ${o}/><rect x="-262" y="-18" width="524" height="336" rx="14" fill="none" stroke="#BFD9F2" stroke-width="10" opacity=".6"/>`;
 s+=babyHand(-130,190,-90,0.55,nl,250);
 s+=`<g transform="translate(70 150) scale(${br}) translate(-70 -150)"><g transform="translate(70 170)">
 <ellipse cx="-46" cy="-112" rx="12" ry="16" fill="${BSK}" ${o} stroke-width="4"/><ellipse cx="46" cy="-112" rx="12" ry="16" fill="${BSK}" ${o} stroke-width="4"/>
 <circle cx="0" cy="-112" r="50" fill="${BSK}" ${o}/>
 <path d="M-6 -146 q12 -12 22 -2 q7 10 -5 15 q-10 3 -10 -7" stroke="#A0674A" stroke-width="4.5" fill="none" stroke-linecap="round"/>
 <path d="M-70 -40 Q-90 60 -40 120 Q0 140 40 120 Q90 60 70 -40 Q40 -76 0 -76 Q-40 -76 -70 -40Z" fill="${PINK}" ${o}/>
 <path d="M-60 -20 Q0 20 60 -30 M-50 40 Q0 70 55 30" stroke="${PL}" stroke-width="3.5" fill="none" opacity=".55"/></g></g>`;
 s+=label(-150,40,'on their back',-3,40);
 return s;}
SC.nails=[
 (lt,D,t)=>{ // sharp nails twinkle; the board slides in at once and files the first tip round
   const f0=EIO(seg(lt,0.6,1.8)), f1=EIO(seg(lt,1.8,2.7)); const nl=[1-f0,1-f1,1,1], hs=1.0, hy=40, rot=10+3*Math.sin(t*3);
   let s=babyHand(0,hy,rot,hs,nl);
   const tip=j=>{const a=rot*Math.PI/180, X=FX[j]*hs, Y=FT[j]*hs; return [X*Math.cos(a)-Y*Math.sin(a), hy+X*Math.sin(a)+Y*Math.cos(a)];};
   for(let j=0;j<4;j++) if(nl[j]>0.5){const [X,Y]=tip(j); s+=sparkle(X+14,Y-24,0.4+0.15*Math.sin(t*6+j),0.95);}
   const a=E(seg(lt,0.15,0.6)), jj=lt<1.8?0:1, [X,Y]=tip(jj);
   s+=emery(X+(1-a)*300+22*Math.sin(lt*16),Y-8,rot-12,0.6)+dust(t,X,Y,a);
   s+=label(250,-10,lt<0.9?'tiny, sharp nails':'file them smooth',-5,40);
   return stage(s,0,1.5,100);},
 (lt,D,t)=>{ // emery board files each tip in turn
   const nl=[0,0,1,1].map((v,j)=>j<2?0:1-EIO(seg(lt,0.1+(j-2)*1.0,0.95+(j-2)*1.0)));
   const j=lt<1.05?2:3, hs=1.0, hy=40, rot=10+2*Math.sin(t*2.5);
   let s=babyHand(0,hy,rot,hs,nl);
   const ar=rot*Math.PI/180, X=FX[j]*hs*Math.cos(ar)-FT[j]*hs*Math.sin(ar), Y=hy+FX[j]*hs*Math.sin(ar)+FT[j]*hs*Math.cos(ar);
   if(lt<2.1){s+=emery(X+22*Math.sin(lt*16),Y-8,rot-10,0.6)+dust(t,X,Y,1);}
   else {s+=emery(230,110+10*Math.sin(t*4),-30,0.6)+check(200,-110,seg(lt,2.1,2.5));}
   s+=label(250,-10,'soft emery board',-5,40);
   return stage(s,0,1.5,100);},
 (lt,D,t)=>{ // asleep: arm out of the swaddle, hand on the blanket, gentle filing, moon + zzz
   let s=sleeper(lt,t,[0,0.6*(1-seg(lt,0.4,2.2)),0,0]);
   s+=emery(-238,138+10*Math.sin(lt*10),84,0.42)+moon(250,-140)+zzz(t,130,-70);
   return stage(s,-10,1.05,110);},
 (lt,D,t)=>{ // tooth wobbles + no ring -> emery board files the air, check
   let s=`<g transform="rotate(${4*Math.sin(t*7)} -110 80)">`+tooth(-110,80,1.1)+`</g>`+noRing(-110,80,120,seg(lt,0.15,0.9));
   const a=E(seg(lt,0.9,1.3)); if(a>0){s+=emery(165+16*Math.sin(t*10)*seg(lt,1.3,1.5),80+50*(1-a),-30,0.75*a)+check(185,210,seg(lt,1.3,1.8));}
   s+=label(-110,250,'not your teeth',-4,42); if(lt>1.0) s+=label(170,-50,'a file ✓',-5,42);
   return stage(s,0,1.4,40);},
 (lt,D,t)=>{ // do this: sleeping, smooth nails, check, hearts
   let s=sleeper(lt,t,[0,0,0,0])+emery(-238,138+12*Math.sin(t*6),84,0.42)+moon(250,-140)+zzz(t,130,-70)+hearts(t,-120,-80)+check(-150,260,seg(lt,0.3,0.8));
   return stage(s,-10,1.05,110);},
];
SC.nails.special=(beat,lt)=>(y0,sag)=>'';
"""

_html = RS.html
RS.html = lambda spec, cover=None: _html(spec, cover).replace("top:450px;font-size:76px", "top:458px;font-size:60px")  # long cover kickers stay on one line

RS.SPECS["burp"] = dict(
    out="lf-reel-1026am-burp-halfway", outdir=OUT, music=LIB / "v3/lf-c-sunny-morning-el.mp3", scene="burp", follow=FOLLOW,
    sky=("dawn", "morning"), garments=["onesie", "sock", "hat", "dress", "none"],
    durs=[5 * BS, 6 * BS, 6 * BS, 6 * BS, 6 * BS], extra_pops=[], cover_beat=0, cover_lt=2.05,
    cover=dict(kick="gulping, then fussing, every feed?", head="Pause to burp / *mid-feed.*", fs=170, pill="", py=1000),
    beats=[
        dict(kick="gulping, then fussing, every feed?", head="Pause to burp / *mid-feed.*", sub="Not just at the end.", fs=150, sy=860, ss=50, chip="AAP · Burping, hiccups & spit-up"),
        dict(kick="with a bottle", head="Burp every / *2 to 3 ounces.*", sub="That's about 60–90 ml.", fs=140, sy=860, ss=48, chip="AAP · Burping, hiccups & spit-up"),
        dict(kick="breastfeeding?", head="Burp when you / *switch sides.*", fs=140, chip="AAP · Burping, hiccups & spit-up"),
        dict(kick="two ways to burp", head="Over your shoulder / or tummy-down / *across your lap.*", fs=128, chip="AAP · Burping, hiccups & spit-up"),
        dict(kick="Do this:", head="Next feed: pause, / *burp,* then finish.", sub="send this to whoever does the night feeds", fs=130, sy=860, ss=42, chip="AAP · HealthyChildren.org"),
    ])

RS.SPECS["nails"] = dict(
    out="lf-reel-1026-baby-nails", outdir=OUT, music=LIB / "lf-b-tender-el.mp3", scene="nails", follow=FOLLOW,
    sky=("afternoon", "morning"), garments=["sock", "onesie", "bib", "hat", "dress"],
    durs=[4 * BT, 4 * BT, 4 * BT, 4 * BT, 5 * BT], extra_pops=[], cover_beat=0, cover_lt=1.2,
    cover=dict(kick="scratches on their face again?", head="Keep tiny nails / *short and smooth.*", fs=150, pill="", py=1000),
    beats=[
        dict(kick="scratches on their face again?", head="Keep tiny nails / *short and smooth.*", sub="So they can't scratch themselves.", fs=140, sy=860, ss=48, chip="AAP · NHS"),
        dict(kick="the gentle way", head="File with a soft / *emery board.*", sub="Or use baby nail clippers.", fs=140, sy=860, ss=48, chip="NHS · AAP"),
        dict(kick="the easy time", head="While they're / *asleep.*", sub="Or after a bath, if they lie still.", fs=150, sy=860, ss=48, chip="AAP · Nail care"),
        dict(kick="and", head="Don't bite / *them short.*", sub="Biting can pass an infection to their finger.", fs=150, sy=860, ss=44, chip="AAP · Nail care"),
        dict(kick="Do this:", head="Tonight: file their / nails *while they sleep.*", sub="send this to someone with a brand-new baby", fs=126, sy=860, ss=42, chip="AAP · NHS"),
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

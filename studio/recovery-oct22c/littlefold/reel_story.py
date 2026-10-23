#!/usr/bin/env python3
"""Littlefold finished Reels v2 (QA fixes, Oct 22 night): a real animated story per beat, not a static scene.

Per frame the page redraws (JS draw(t)):
  - light changes: dawn -> morning sky crossfade, rotating rays, a warm light sweep at each cut;
  - the washing line moves in the wind (sag + gusts), a new garment pegs on each beat;
  - a story stage (hand-drawn vignette in the brand line style) acts out each beat:
      coat-off: the puffy coat lifts out of the car seat, straps swing in and click; the padding squashes and leaves a gap;
                fingers pinch the slack strap, the strap pulls tight, a check draws on; a blanket falls over the straps;
                Do this: the coat flies up and is pegged on the line, hearts float up.
      teething: frost sparkles on a cool cloth while a fingertip rubs in gentle circles; drops wet the cloth, it twists,
                it goes into a little freezer and frost blooms; a bead necklace gets a drawn 'no' ring and a bead rolls off;
                a numbing-gel tube gets a 'no' ring and slides into a drawer; Do this: the cool cloth is pegged on the line.
  - text: the next beat's words slide in while the old ones slide out (always words on screen, no blank beats);
  - the joyful sun (eyes open, smiling) beams wider on Do this; an on-screen follow prompt lands; no fade-out at the end.
Covers are their own scenes. Frames: Playwright Chromium (vector SVG), 1080x1920, 30 fps -> ffmpeg H.264 + AAC.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

KIT = Path("/home/claude/steadfold-autopost/studio/recovery-oct22b/littlefold/build")
sys.path.insert(0, str(KIT))
from sunart import *  # noqa
import stills as ST  # noqa

OUTD = Path("/home/claude/steadfold/creative/v061/littlefold/finished")
LIB = REPO / "media" / "music" / "library"
W, H, FPS = 1080, 1920, 30
BB = 60 / 112.3   # lf-x-sunny-bounce
BC = 60 / 92.3    # lf-cosy-el-01
BS = 60 / 120.2   # lf-c-sunny-morning-el
BT = 60 / 84.7    # lf-b-tender-el

JS = r"""
const W=1080,H=1920, PL='#6B3B5A', INK='#3A1F3D', SK='#F2C4A0', SKD='#D99B78';
const PINK='#FFB9CF', BLUE='#BFD9F2', BUT='#FFE08A', SAGE='#BFD8B0', PEACH='#FFC8A8', CREAM='#FFF8EE', CORAL='#F27C6B';
const cl=(x,a,b)=>Math.min(Math.max(x,a),b), E=t=>1-Math.pow(1-cl(t,0,1),3), EIO=t=>{t=cl(t,0,1);return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;};
const seg=(t,a,b)=>cl((t-a)/(b-a),0,1);
const o=`stroke="${PL}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"`;
function lineY(x,y0,sag){const u=(x+20)/(W+40);return y0+4*sag*u*(1-u);}
// ---------- garments (hung from peg point 0,0)
function peg(x){return `<rect x="${x-8}" y="-14" width="16" height="32" rx="5" fill="#E9BE92" stroke="${PL}" stroke-width="3"/>`;}
const G={
 onesie:()=>`<path d="M-33 4 L-55 14 L-77 46 L-55 62 L-41 48 L-41 136 Q-41 156 -21 158 L-13 176 L13 176 L21 158 Q41 156 41 136 L41 48 L55 62 L77 46 L55 14 L33 4 Q0 30 -33 4Z" fill="${PINK}" ${o}/><path d="M0 86 c-8 -14 -28 -6 -20 8 l20 18 l20 -18 c8 -14 -12 -22 -20 -8z" fill="#FFF0F4" stroke="${PL}" stroke-width="3"/>`+peg(-29)+peg(29),
 sock:()=>`<path d="M-23 2 L23 2 L23 98 Q23 110 35 118 L63 136 Q81 152 65 168 Q51 182 29 170 L-17 142 Q-31 132 -27 114Z" fill="${BLUE}" ${o}/><path d="M-23 20h46M-23 34h46" stroke="${PL}" stroke-width="3"/>`+peg(0),
 bib:()=>`<path d="M-45 8 Q-55 26 -53 56 A54 60 0 1 0 53 56 Q55 26 45 8 Q33 56 0 56 Q-33 56 -45 8Z" fill="${BUT}" ${o}/>`+[[-23,96],[0,118],[23,96],[-13,136],[13,138]].map(p=>`<circle cx="${p[0]}" cy="${p[1]}" r="5" fill="${CREAM}"/>`).join('')+peg(-43)+peg(43),
 hat:()=>`<circle cx="0" cy="16" r="20" fill="${CREAM}" ${o}/><path d="M-55 126 Q-59 38 0 34 Q59 38 55 126Z" fill="${SAGE}" ${o}/><rect x="-63" y="114" width="126" height="34" rx="14" fill="#A8CA9A" ${o}/>`+peg(0),
 dress:()=>`<path d="M-27 6 L27 6 L35 50 L67 154 Q33 172 0 166 Q-33 172 -67 154 L-35 50Z" fill="${PEACH}" ${o}/><path d="M-27 6 Q0 32 27 6" fill="${CREAM}" ${o}/>`+peg(-23)+peg(23),
 coat:()=>coatSVG(0.62)+peg(-40)+peg(40),
 none:()=>'',
 cloth:()=>`<g transform="translate(0 8)">${clothSVG(0,1,0.6)}</g>`+peg(-30)+peg(30),
};
// ---------- drawn props
function coatSVG(s){ // puffy coat, front view, origin top centre
 let q='';for(let i=1;i<5;i++)q+=`<path d="M-70 ${i*44} Q0 ${i*44+12} 70 ${i*44}" stroke="${PL}" stroke-width="3" fill="none" opacity=".55"/>`;
 return `<g transform="scale(${s})"><path d="M-48 0 Q0 22 48 0 L96 18 Q132 60 136 150 Q130 196 104 200 L96 112 L84 230 Q0 252 -84 230 L-96 112 L-104 200 Q-130 196 -136 150 Q-132 60 -96 18Z" fill="${PINK}" ${o}/>
 <path d="M-34 6 Q0 34 34 6 L30 -10 Q0 8 -30 -10Z" fill="#FFD6E3" ${o}/>${q}<path d="M0 26 V236" stroke="${PL}" stroke-width="3"/>
 <circle cx="12" cy="70" r="5" fill="${PL}"/><circle cx="12" cy="130" r="5" fill="${PL}"/><circle cx="12" cy="190" r="5" fill="${PL}"/></g>`;}
function seatSVG(){ // car seat shell (front), origin = seat centre top
 return `<path d="M-150 -10 Q-196 20 -186 90 Q-176 120 -150 120Z M150 -10 Q196 20 186 90 Q176 120 150 120Z" fill="#F6A98A" ${o}/><path d="M-150 -10 Q-170 150 -130 290 Q-60 340 0 340 Q60 340 130 290 Q170 150 150 -10 Q130 -60 0 -64 Q-130 -60 -150 -10Z" fill="${PEACH}" ${o}/>
 <path d="M-112 0 Q-124 140 -96 256 Q-48 292 0 292 Q48 292 96 256 Q124 140 112 0 Q96 -30 0 -32 Q-96 -30 -112 0Z" fill="#FFF1E3" ${o}/>
 <path d="M-170 300 Q0 360 170 300 L184 334 Q0 400 -184 334Z" fill="#F6A98A" ${o}/>`;}
function straps(k,click){ // k: 0 open .. 1 buckled
 const ax=-62, bx=62, ay=30;
 const L=`<g transform="rotate(${55*(1-k)} ${ax} ${ay})"><path d="M${ax-16} ${ay} L${ax+16} ${ay} L${-6} 210 L${-30} 206Z" fill="#9CC490" ${o}/></g>`;
 const R=`<g transform="rotate(${-55*(1-k)} ${bx} ${ay})"><path d="M${bx+16} ${ay} L${bx-16} ${ay} L${6} 210 L${30} 206Z" fill="#9CC490" ${o}/></g>`;
 const clip=k>.98?`<rect x="-36" y="112" width="72" height="26" rx="8" fill="${BUT}" ${o}/>`:'';
 const buckle=`<rect x="-26" y="196" width="52" height="44" rx="10" fill="${k>.98?BUT:CREAM}" ${o}/><path d="M0 240 V292" stroke="#9CC490" stroke-width="22"/><path d="M-11 240 V292 M11 240 V292" stroke="${PL}" stroke-width="4"/>`;
 let burst='';if(click>0&&click<1){const r=40+50*click;for(let i=0;i<8;i++){const a=i*Math.PI/4;burst+=`<path d="M${r*Math.cos(a)} ${218+r*Math.sin(a)} L${(r+22)*Math.cos(a)} ${218+(r+22)*Math.sin(a)}" stroke="${BUT}" stroke-width="7" stroke-linecap="round" opacity="${1-click}"/>`;}}
 return L+R+buckle+clip+burst;}
function hand(x,y,rot,s,pinch){ // drawn adult hand from the right: palm + thumb + index (pinch 0 open..1 closed)
 const g=26*(1-pinch);
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
 <path d="M60 -40 Q140 -60 220 -30 L240 60 Q150 90 70 60 Z" fill="${SK}" ${o}/>
 <path d="M70 -34 Q20 ${-40-g} -30 ${-30-g} Q-46 ${-24-g} -34 ${-12-g} Q10 ${-6-g} 70 -6" fill="${SK}" ${o}/>
 <path d="M70 34 Q20 ${40+g} -26 ${30+g} Q-42 ${22+g} -30 ${10+g} Q14 ${6+g} 70 8" fill="${SK}" ${o}/>
 <path d="M150 -10 Q170 0 150 14" stroke="${SKD}" stroke-width="4" fill="none"/></g>`;}
function blanket(x,y,w,h,wave){ // soft draped blanket: curved top, flared sides, wavy hem, fold lines
 let d=`M${x+10} ${y+24} Q${x+w/2} ${y-14} ${x+w-10} ${y+24} L${x+w+18} ${y+h}`;const n=8;
 for(let i=n;i>=0;i--){const xx=x-18+(w+36)*i/n;d+=` Q${xx+(w+36)/n/2} ${y+h+16+wave*6*Math.sin(i+wave*5)} ${xx} ${y+h}`;}d+=' Z';
 let folds='';for(let i=0;i<3;i++){const fx=x+w*(0.25+0.25*i);folds+=`<path d="M${fx-10} ${y+30} Q${fx+6} ${y+h*0.5} ${fx-4} ${y+h-6}" stroke="${PL}" stroke-width="3" fill="none" opacity=".45"/>`;}
 let hearts='';for(let i=0;i<2;i++){const hx=x+w*(0.33+0.34*i),hy=y+h*0.5;hearts+=`<path d="M${hx} ${hy} c-6 -11 -22 -5 -16 6 l16 14 l16 -14 c6 -11 -10 -17 -16 -6z" fill="${PINK}" stroke="${PL}" stroke-width="3"/>`;}
 return `<path d="${d}" fill="${BUT}" ${o}/>${folds}${hearts}`;}
function clothSVG(twist,wet,frost){ // folded terry washcloth; twist 0..1 morphs into a rope
 const w=170-70*twist, h=120+20*twist;
 let dots='';for(let i=0;i<5;i++)for(let j=0;j<4;j++)dots+=`<circle cx="${-w/2+18+i*(w-36)/4}" cy="${16+j*(h-32)/3}" r="3.2" fill="${CREAM}" opacity=".8"/>`;
 let tw='';if(twist>0){for(let i=0;i<6;i++){const yy=10+i*(h-20)/5;tw+=`<path d="M${-w/2} ${yy} Q0 ${yy+18*twist} ${w/2} ${yy+30*twist}" stroke="${PL}" stroke-width="3.5" fill="none" opacity="${twist}"/>`;}}
 const col=wet>0?`rgb(${191-40*wet},${217-30*wet},${242-20*wet})`:BLUE;
 let fr='';if(frost>0){for(let i=0;i<5;i++){const a=i*1.3,fx=-w/2+20+((i*53)%Math.max(w-40,10)),fy=12+((i*37)%(h-20)),s=10+12*frost;fr+=`<g transform="translate(${fx} ${fy})" opacity="${frost}">${[0,60,120].map(r=>`<path d="M${-s} 0 H${s}" transform="rotate(${r+frost*30})" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>`).join('')}</g>`;}}
 return `<rect x="${-w/2}" y="0" width="${w}" height="${h}" rx="${18+20*twist}" fill="${col}" ${o}/><path d="M${-w/2} 24 H${w/2}" stroke="${PL}" stroke-width="3" opacity=".6"/>${dots}${tw}${fr}`;}
function noRing(cx,cy,r,k){ // drawn coral 'no' ring
 const C=2*Math.PI*r;return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${CORAL}" stroke-width="16" stroke-linecap="round" stroke-dasharray="${C}" stroke-dashoffset="${C*(1-seg(k,0,.6))}" transform="rotate(-90 ${cx} ${cy})"/>
 <path d="M${cx-r*0.7} ${cy-r*0.7} L${cx-r*0.7+1.4*r*seg(k,.55,1)} ${cy-r*0.7+1.4*r*seg(k,.55,1)}" stroke="${CORAL}" stroke-width="16" stroke-linecap="round"/>`;}
function check(cx,cy,k){return `<circle cx="${cx}" cy="${cy}" r="44" fill="${SAGE}" ${o} opacity="${seg(k,0,.3)}"/><path d="M${cx-20} ${cy} l14 15 l28 -30" stroke="${PL}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="80" stroke-dashoffset="${80*(1-seg(k,.2,1))}"/>`;}
function label(x,y,txt,rot,size){return `<text x="${x}" y="${y}" font-family="Caveat Brush" font-size="${size||48}" fill="#B23A62" transform="rotate(${rot||-4} ${x} ${y})" text-anchor="middle">${txt}</text>`;}
function hearts(t,x,y){let s='';for(let i=0;i<4;i++){const k=(t*0.6+i*0.25)%1;const hx=x+(i-1.5)*60+14*Math.sin(t*3+i),hy=y-160*k;s+=`<path d="M${hx} ${hy} c-6 -11 -22 -5 -16 6 l16 14 l16 -14 c6 -11 -10 -17 -16 -6z" fill="${PINK}" stroke="${PL}" stroke-width="3" opacity="${Math.sin(Math.PI*k)}"/>`;}return s;}
function sparkle(x,y,s,op){return `<g transform="translate(${x} ${y}) scale(${s})" opacity="${op}"><path d="M0 -26 Q4 -4 26 0 Q4 4 0 26 Q-4 4 -26 0 Q-4 -4 0 -26Z" fill="#FFFFFF" stroke="${PL}" stroke-width="2.5"/></g>`;}
// ---------- the joyful sun
function sun(x,y,beam,t){
 const r=118*(1+0.02*Math.sin(t*2.6))*(1+0.08*beam);
 const eyes=beam>0.5?`<path d="M-48 -6 q16 -22 32 0 M16 -6 q16 -22 32 0" stroke="#9A4E2A" stroke-width="8" fill="none" stroke-linecap="round"/>`:
  `<ellipse cx="-34" cy="-10" rx="11" ry="15" fill="#5A2E22"/><ellipse cx="34" cy="-10" rx="11" ry="15" fill="#5A2E22"/><circle cx="-30" cy="-16" r="4.5" fill="#fff"/><circle cx="38" cy="-16" r="4.5" fill="#fff"/>`;
 const m=18+14*beam;
 return `<g transform="translate(${x} ${y})"><circle r="${r*2.1}" fill="url(#glow)" opacity="${0.75+0.25*beam}"/>
 <g transform="rotate(${t*9})" opacity="${0.55+0.35*beam}">${[...Array(12)].map((_,i)=>`<path d="M0 ${-r-22} L10 ${-r-62-20*beam} L-10 ${-r-62-20*beam}Z" fill="#FFD36B" stroke="#F2A94B" stroke-width="3" transform="rotate(${i*30})"/>`).join('')}</g>
 <circle r="${r}" fill="url(#disc)" stroke="#F2A94B" stroke-width="5"/>${eyes}
 <path d="M${-m-8} 22 Q0 ${30+m*1.6} ${m+8} 22 Z" fill="#E77F72" stroke="#9A4E2A" stroke-width="6" stroke-linejoin="round"/>
 <circle cx="-66" cy="22" r="18" fill="#FF9EA8" opacity=".6"/><circle cx="66" cy="22" r="18" fill="#FF9EA8" opacity=".6"/></g>`;}
// ---------- ground (drawn, no clip-art props)
function ground(t){
 let tufts='';for(let i=0;i<22;i++){const x=20+i*49+((i*37)%23),y=1640+((i*53)%120),sw=6*Math.sin(t*2.2+i*0.7);tufts+=`<path d="M${x} ${y} q${-6+sw} -30 ${-10+sw*2} -52 M${x} ${y} q${4+sw} -34 ${8+sw*2} -60 M${x} ${y} q${10+sw} -22 ${22+sw*2} -38" stroke="#8DB07F" stroke-width="5" fill="none" stroke-linecap="round"/>`;}
 let hatch='';for(let i=0;i<30;i++){const x=(i*71)%1080,y=1560+((i*97)%300);hatch+=`<path d="M${x} ${y} l26 -8" stroke="#9EC293" stroke-width="4" stroke-linecap="round" opacity=".7"/>`;}
 return `<path d="M0 1520 C 240 1470 460 1500 640 1520 S 960 1480 1080 1500 V1920 H0Z" fill="#D7E8CB" ${o} stroke-width="4"/>
 <path d="M0 1640 C 300 1590 720 1630 1080 1580 V1920 H0Z" fill="#BCD7AE"/>${hatch}${tufts}`;}
// ---------- washing line in the wind
function washline(t,n,kinds,starts,special){
 const y0=250, sag=46+9*Math.sin(t*1.7)+5*Math.sin(t*4.1);
 let s=`<path d="M-20 ${y0} Q540 ${y0+2*sag} 1100 ${y0}" stroke="${PL}" stroke-width="5" fill="none" stroke-linecap="round"/>`;
 const XS=[150,345,540,735,930];
 for(let i=0;i<5;i++){ if(i>=n) continue; const gl=t-starts[i]; const x=XS[i], y=lineY(x,y0,sag);
  let rot=7*Math.sin(t*1.9+i*1.1)+4*Math.sin(t*4.3+i);
  let drop=0; if(i>0){drop=70*(1-E(gl/0.32)); rot+=16*Math.exp(-4.5*gl)*Math.cos(11*gl);}
  s+=`<g transform="translate(${x} ${y-drop}) rotate(${rot}) scale(.88)">${G[kinds[i]]()}</g>`;}
 if(special){s+=special(y0,sag);} return s;}
function stage(svg,dx,sc,dy){return `<g transform="translate(${440+(dx||0)} ${1075+(dy||0)}) scale(${sc||1.12})">${svg}</g>`;}
// ===================== scenes =====================
const SC={};
SC.coat=[
 (lt,D,t)=>{ // coat lifts out, straps swing in, click
   const up=EIO(seg(lt,0.25,1.15)), k=EIO(seg(lt,1.0,1.7)), click=seg(lt,1.7,2.1);
   let s=seatSVG()+straps(k,click);
   s+=`<g transform="translate(${-260*up} ${10-330*up}) rotate(${-24*up})" opacity="${1-seg(lt,1.0,1.3)}">${coatSVG(1.0)}</g>`;
   if(lt<0.9) s+=label(270,80,'coat off ↑',-6,58);
   if(lt>1.8) s+=label(250,150,'click!',-8,60);
   return stage(s);},
 (lt,D,t)=>{ // padding squashes, gap appears (cross-section)
   const p=Math.max(EIO(seg(lt,0.3,0.7))*(1-seg(lt,1.2,1.5)), EIO(seg(lt,1.6,2.0)));
   const hgt=210*(1-0.68*p);
   let s=`<rect x="-230" y="0" width="70" height="300" rx="20" fill="${PEACH}" ${o}/>`+label(-195,340,'seat',0,40);
   s+=`<rect x="-160" y="${150-hgt/2}" width="${300*(1-0.68*p)}" height="${hgt}" rx="${50*(1-0.5*p)}" fill="${PINK}" ${o}/>`;
   for(let i=1;i<4;i++)s+=`<path d="M${-160+i*75*(1-0.68*p)} ${150-hgt/2+12} V${150+hgt/2-12}" stroke="${PL}" stroke-width="3" opacity=".5"/>`;
   s+=`<rect x="170" y="0" width="44" height="300" rx="12" fill="#9CC490" ${o}/>`+label(192,340,'strap',0,40);
   if(p>0.6){const gx=-160+300*(1-0.68*p);s+=`<path d="M${gx+14} 150 H160" stroke="#B23A62" stroke-width="6" stroke-dasharray="4 12" stroke-linecap="round"/>`+label((gx+170)/2,120,'gap',-4,58);}
   else s+=label(-10,330,'puffy coat',-4,48);
   return stage(s,40,1.25);},
 (lt,D,t)=>{ // pinch test: slack loop, fingers pinch it, strap pulled tight, check
   const reach=E(seg(lt,0,0.45)), pinch=E(seg(lt,0.45,0.8))*(1-seg(lt,1.25,1.45)), taut=EIO(seg(lt,1.3,1.9));
   const L=70*(1-taut);
   let s=`<rect x="-150" y="-40" width="300" height="420" rx="40" fill="${PEACH}" ${o}/><rect x="-110" y="-10" width="220" height="360" rx="30" fill="#FFF1E3" ${o}/>`;
   s+=`<path d="M-44 -30 V120 Q${-44+L*1.6} ${120} ${-44+L*1.6} ${160} Q${-44+L*1.6} 200 -44 200 V330" stroke="#9CC490" stroke-width="58" fill="none" stroke-linejoin="round"/>`;
   s+=`<path d="M-44 -30 V120 Q${-44+L*1.6} ${120} ${-44+L*1.6} ${160} Q${-44+L*1.6} 200 -44 200 V330" stroke="${PL}" stroke-width="4" fill="none" stroke-dasharray="3 16" stroke-linecap="round"/>`;
   s+=`<rect x="-74" y="${330+50*taut}" width="60" height="64" rx="12" fill="${BUT}" ${o}/><path d="M-44 320 V${330+50*taut}" stroke="#9CC490" stroke-width="22"/>`;
   const hx=-44+L*1.6+10+260*(1-reach)+(lt>1.25?260*seg(lt,1.25,1.6):0);
   s+=hand(hx,160,0,0.9,pinch);
   if(lt>0.5&&lt<1.35) s+=label(-60,-70,'slack? you can pinch it',-4,50);
   if(lt>1.35) s+=label(-60,-70,'pull it snug',-4,54);
   if(lt>1.75) s+=check(140,330,seg(lt,1.75,2.2));
   return stage(s,40,1.0);},
 (lt,D,t)=>{ // blanket falls over the buckled straps
   const f=EIO(seg(lt,0.2,1.0)); let s=seatSVG()+straps(1,0);
   const bh=30+150*f; s+=`<g opacity="${seg(lt,0.1,0.3)}">${blanket(-150,175-80*(1-f),300,bh,(1-f)*1.4+0.15*Math.sin(t*3))}</g>`;
   if(lt<1.1) s+=label(250,-40,'thin layers under',-6,48); else s+=label(250,-40,'blanket on top ✓',-6,48);
   return stage(s);},
 (lt,D,t)=>{ // do this: buckled + blanket, hearts float up
   let s=seatSVG()+straps(1,0)+blanket(-150,175,300,150,0.15*Math.sin(t*3))+hearts(t,0,90);
   return stage(s);},
];
SC.coat.special=(beat,lt)=>(y0,sag)=>{ // on Do this, the coat flies up and is pegged on the line
  if(beat<4) return ''; const f=EIO(seg(lt,0.1,0.9)); const tx=930, ty=lineY(930,y0,sag)+8;
  const sx=440, sy=1000; const X=sx+(tx-sx)*f, Y=sy+(ty-sy)*f-160*Math.sin(Math.PI*f);
  return `<g transform="translate(${X} ${Y}) rotate(${-20*(1-f)+4*Math.sin(T*2)})">${coatSVG(0.55)}${f>0.98?peg(-26)+peg(26):''}</g>`;};
SC.teeth=[
 (lt,D,t)=>{ // cool cloth with frost + fingertip gentle circles
   let s=`<g transform="translate(-170 40) rotate(-6)">${clothSVG(0,0,0.6+0.4*Math.sin(t*3)**2)}</g>`;
   s+=sparkle(-60,20,0.9+0.3*Math.sin(t*5),0.9)+sparkle(-250,170,0.7+0.3*Math.sin(t*4+1),0.9);
   const a=t*4.2; s+=`<g transform="translate(${160+22*Math.cos(a)} ${120+14*Math.sin(a)})">${hand(-60,0,0,0.8,1)}</g>`;
   s+=`<path d="M110 196 a56 26 0 1 0 112 0" stroke="#B23A62" stroke-width="5" fill="none" stroke-dasharray="6 10" stroke-linecap="round"/>`;
   s+=label(-170,240,'cool cloth',-4,48)+label(190,290,'gentle rub',-4,48);
   return stage(s,0,1.3,-30);},
 (lt,D,t)=>{ // wet -> twist -> chill (freezer, frost)
   const tw=EIO(seg(lt,0.8,1.5)), fr=seg(lt,2.0,2.5);
   const door=EIO(seg(lt,1.45,1.7))*(1-EIO(seg(lt,2.0,2.3)));
   let body='',doorS='',after='';
   if(lt>1.35){ body=`<g transform="translate(-330 -40)"><rect x="0" y="0" width="250" height="260" rx="24" fill="${CREAM}" ${o}/><rect x="16" y="16" width="218" height="228" rx="16" fill="#E3EEF8" stroke="${PL}" stroke-width="3"/></g>`;
     doorS=`<g transform="translate(-314 -24) scale(${1-0.92*door} 1)"><rect x="0" y="0" width="218" height="228" rx="16" fill="${BLUE}" ${o}/><rect x="188" y="84" width="12" height="60" rx="6" fill="${CREAM}" ${o}/><g transform="translate(100 114)">${[0,60,120].map(r=>`<path d="M-36 0 H36" transform="rotate(${r})" stroke="${CREAM}" stroke-width="9" stroke-linecap="round"/>`).join("")}</g></g>`;
     if(lt>2.1){for(let i=0;i<4;i++)after+=sparkle(-300+i*62,-70+((i*41)%60),0.6+0.4*Math.sin(t*5+i),seg(lt,2.1,2.4));}
     after+=label(150,0,'chill it',-5,54)+label(160,250,'not frozen solid',-4,44);}
   const mv=EIO(seg(lt,1.55,1.95));
   const cloth=`<g transform="translate(${-40-170*mv} ${60-10*mv}) scale(${1-0.25*mv})">${clothSVG(tw,seg(lt,0.2,0.9),0)}</g>`;
   let s=body+cloth+doorS+after;
   if(lt<0.95){for(let i=0;i<3;i++){const k=(lt*1.8+i*0.33)%1;s+=`<path d="M${-60+i*40} ${-120+150*k} q-12 18 0 26 q12 -8 0 -26z" fill="${BLUE}" stroke="${PL}" stroke-width="3" opacity="${1-k*0.6}"/>`;}s+=label(150,0,'wet it',-5,54);}
   else if(lt<1.35) s+=label(150,0,'twist it',-5,54);
   return stage(s,90,1.3,-30);},
 (lt,D,t)=>{ // necklace + drawn no-ring, a bead rolls away
   let s='';const cols=[PINK,BUT,BLUE,SAGE,PEACH];
   for(let i=0;i<11;i++){const a=Math.PI*(0.15+0.7*i/10),x=-10+170*Math.cos(a),y=40+150*Math.sin(a)+4*Math.sin(t*3+i);
     if(i==8&&lt>1.2){const k=E(seg(lt,1.2,2.2));s+=`<circle cx="${x+260*k}" cy="${y+90*k}" r="22" fill="${cols[i%5]}" ${o} transform="rotate(${360*k} ${x+260*k} ${y+90*k})"/>`;continue;}
     s+=`<circle cx="${x}" cy="${y}" r="22" fill="${cols[i%5]}" ${o}/>`;}
   s+=`<path d="M-180 40 Q-10 -60 160 40" stroke="${PL}" stroke-width="4" fill="none"/>`;
   s+=noRing(-10,130,165,seg(lt,0.35,1.2));
   return stage(s,0,1.3,-30);},
 (lt,D,t)=>{ // gel tube + no-ring, slides into a drawer
   const away=EIO(seg(lt,1.4,2.1));
   let s=`<g transform="translate(${-40} ${-90*away}) scale(${1-0.25*away})" opacity="${1-seg(lt,1.9,2.2)}"><rect x="-140" y="60" width="240" height="90" rx="20" fill="${CREAM}" ${o}/><path d="M100 70 L150 85 L150 125 L100 140Z" fill="${PEACH}" ${o}/><rect x="150" y="88" width="40" height="34" rx="6" fill="${CORAL}" ${o}/>
     <text x="-20" y="118" font-family="Poppins" font-weight="600" font-size="34" text-anchor="middle" fill="${INK}">gel</text></g>`;
   s+=`<g opacity="${1-seg(lt,1.4,1.7)}">${noRing(0,105,170,seg(lt,0.3,1.1))}</g>`;
   if(lt>1.3){s+=`<rect x="-200" y="180" width="400" height="140" rx="20" fill="${PEACH}" ${o}/><rect x="-60" y="236" width="120" height="22" rx="11" fill="${CREAM}" ${o}/>`; s+=label(0,360,'put it away',-3,48);}
   return stage(s,0,1.3,-30);},
 (lt,D,t)=>{ // do this: cloth on a plate with frost, sun beams
   let s=`<ellipse cx="0" cy="250" rx="230" ry="50" fill="${CREAM}" ${o}/><g transform="translate(-50 120) rotate(-8)">${clothSVG(0.15,0.3,0.7+0.3*Math.sin(t*3)**2)}</g>`;
   for(let i=0;i<3;i++)s+=sparkle(-170+i*170,90+((i*31)%50),0.7+0.3*Math.sin(t*4+i),0.95);
   return stage(s,0,1.3,-30);},
];
SC.teeth.special=(beat,lt)=>(y0,sag)=>'';
// ---------- newborn-care props (no faces: a swaddled bundle with a little hat, held by adult hands)
function bundle(x,y,rot,s){return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
 <path d="M-70 -40 Q-90 60 -40 120 Q0 140 40 120 Q90 60 70 -40 Q40 -80 0 -80 Q-40 -80 -70 -40Z" fill="${PINK}" ${o}/>
 <path d="M-60 -20 Q0 20 60 -30 M-50 40 Q0 70 55 30" stroke="${PL}" stroke-width="3.5" fill="none" opacity=".55"/>
 <path d="M-44 -66 Q0 -120 44 -66 Q20 -54 0 -54 Q-20 -54 -44 -66Z" fill="${SAGE}" ${o}/><circle cx="0" cy="-104" r="12" fill="${CREAM}" ${o}/></g>`;}
function cradle(x,y,rot,s){ // two hands from below
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})"><path d="M-150 60 Q-120 10 -40 20 Q0 26 10 50 Q-30 70 -150 90Z" fill="${SK}" ${o}/>
 <path d="M150 60 Q120 10 40 20 Q0 26 -10 50 Q30 70 150 90Z" fill="${SK}" ${o}/></g>`;}
function bassinet(x,y){return `<g transform="translate(${x} ${y})"><path d="M-170 0 H170 Q160 110 0 120 Q-160 110 -170 0Z" fill="${BLUE}" ${o}/><path d="M-170 0 H170" stroke="${PL}" stroke-width="6"/>
 <path d="M-120 120 L-140 190 M120 120 L140 190" stroke="${PL}" stroke-width="6" stroke-linecap="round"/></g>`;}
function crib(x,y){let b='';for(let i=0;i<9;i++)b+=`<path d="M${-180+i*45} -40 V120" stroke="${PL}" stroke-width="6" stroke-linecap="round"/>`;
 return `<g transform="translate(${x} ${y})"><rect x="-200" y="110" width="400" height="34" rx="10" fill="${PEACH}" ${o}/><rect x="-200" y="-60" width="400" height="26" rx="10" fill="${PEACH}" ${o}/>${b}
 <path d="M-210 -80 V200 M210 -80 V200" stroke="${PL}" stroke-width="10" stroke-linecap="round"/></g>`;}
function heartP(x,y,s,op){return `<path transform="translate(${x} ${y}) scale(${s})" d="M0 0 c-8 -14 -28 -6 -20 8 l20 18 l20 -18 c8 -14 -12 -22 -20 -8z" fill="${PINK}" stroke="${PL}" stroke-width="3" opacity="${op}"/>`;}
SC.spoil=[
 (lt,D,t)=>{ // bundle lifted from the bassinet into waiting hands, hearts pop
   const up=EIO(seg(lt,0.2,1.2)); let s=bassinet(0,170);
   s+=bundle(0,140-120*up,-80+80*up,1.0)+(up>0.2?cradle(0,190-120*up,0,1.0):'');
   if(lt>1.2){for(let i=0;i<3;i++){const k=seg(lt,1.2+i*0.2,2.2+i*0.2);s+=heartP(-90+i*90,-120-80*k,1.2,Math.sin(Math.PI*k));}}
   s+=label(240,200,lt<1.2?'pick them up':'held ♡',-6,54);
   return stage(s,0,1.05,45);},
 (lt,D,t)=>{ // cry 'volume' bars shrink while held
   const sway=6*Math.sin(t*2.4); let s=`<g transform="rotate(${sway})">`+bundle(-60,40,0,1.0)+cradle(-60,90,0,1.0)+`</g>`;
   const lvl=1-0.75*EIO(seg(lt,0.4,2.4)); for(let i=0;i<5;i++){const h=(30+i*28)*lvl*(0.85+0.15*Math.sin(t*9+i));s+=`<rect x="${130+i*36}" y="${150-h}" width="24" height="${h}" rx="10" fill="${i<3?BUT:PEACH}" ${o} stroke-width="3"/>`;}
   s+=label(220,210,lt<1.4?'answered…':'…cries less',-4,50);
   return stage(s,0,1.05,45);},
 (lt,D,t)=>{ // checklist: bottle, diaper, thermometer pop in with ticks
   let s=''; const items=[[-210,'bottle'],[0,'diaper'],[210,'temp']];
   items.forEach(([x,k],j)=>{const a=E(seg(lt,0.15+j*0.5,0.45+j*0.5)); if(a<=0) return; let g='';
     if(k=='bottle') g=`<rect x="-34" y="-40" width="68" height="120" rx="24" fill="${CREAM}" ${o}/><path d="M-20 -40 Q0 -90 20 -40Z" fill="${PEACH}" ${o}/><path d="M-34 10 H34" stroke="${PL}" stroke-width="3"/>`;
     if(k=='diaper') g=`<path d="M-70 -30 H70 Q60 60 0 70 Q-60 60 -70 -30Z" fill="${CREAM}" ${o}/><rect x="-74" y="-40" width="40" height="22" rx="8" fill="${BLUE}" ${o}/><rect x="34" y="-40" width="40" height="22" rx="8" fill="${BLUE}" ${o}/>`;
     if(k=='temp') g=`<rect x="-16" y="-70" width="32" height="130" rx="16" fill="${CREAM}" ${o}/><circle cx="0" cy="70" r="26" fill="${CORAL}" ${o}/><rect x="-6" y="${-40+40*(1-a)}" width="12" height="${90}" rx="6" fill="${CORAL}"/>`;
     s+=`<g transform="translate(${x} 60) scale(${0.6+0.4*a})" opacity="${a}">${g}</g>`;
     s+=check(x+60,160,seg(lt,0.35+j*0.5,0.75+j*0.5)); });
   return stage(s,0,1.05,45);},
 (lt,D,t)=>{ // hold close, sway, shush, walk
   const sway=12*Math.sin(t*3.2); let s=`<g transform="translate(${-40+30*Math.sin(t*1.6)} 0) rotate(${sway})">`+bundle(0,40,0,1.0)+cradle(0,90,0,1.0)+`</g>`;
   for(let i=0;i<3;i++){const k=(lt*0.8+i*0.33)%1; s+=`<text x="${120+60*k}" y="${-20-70*k+i*10}" font-family="Caveat Brush" font-size="${40+16*k}" fill="#B23A62" opacity="${Math.sin(Math.PI*k)}">shh</text>`;}
   for(let i=0;i<5;i++){const k=seg(lt,0.2+i*0.3,0.5+i*0.3); s+=`<ellipse cx="${-220+i*90}" cy="${230+(i%2?16:0)}" rx="16" ry="24" fill="${PL}" opacity="${0.5*k}"/>`;}
   return stage(s,0,1.05,45);},
 (lt,D,t)=>{ // do this: picked up first, hearts float
   const sway=5*Math.sin(t*2); let s=`<g transform="rotate(${sway})">`+bundle(0,40,0,1.05)+cradle(0,95,0,1.05)+`</g>`+hearts(t,0,-40);
   return stage(s,0,1.05,45);},
];
SC.spoil.special=(beat,lt)=>(y0,sag)=>'';
SC.step=[
 (lt,D,t)=>{ // a door opens onto warm light, footsteps step out
   const op=EIO(seg(lt,0.3,1.4)); let s=`<rect x="-150" y="-80" width="240" height="380" rx="14" fill="#FFF6D8" ${o}/>
   <g transform="translate(-150 -80) scale(${1-0.7*op} 1)"><rect x="0" y="0" width="240" height="380" rx="14" fill="${PEACH}" ${o}/><circle cx="200" cy="200" r="12" fill="${BUT}" ${o}/></g>`;
   s+=`<path d="M-150 300 L-230 330 H170 L90 300Z" fill="#FFE9A8" opacity="${0.8*op}"/>`;
   for(let i=0;i<4;i++){const k=seg(lt,1.0+i*0.3,1.3+i*0.3); s+=`<ellipse cx="${-20+i*70}" cy="${330+(i%2?14:0)}" rx="14" ry="22" fill="${PL}" opacity="${0.5*k}"/>`;}
   s+=label(250,-40,'a short break is OK',-5,48);
   return stage(s,20,1.05,-20);},
 (lt,D,t)=>{ // crib first, on their back: hands lower the bundle in, flat
   const dn=EIO(seg(lt,0.1,1.1)); let s=crib(0,60);
   s+=bundle(0,-120+170*dn,-90*dn,0.85)+(dn<0.95?cradle(0,-70+170*dn,-90*dn*0.2,0.9):'');
   if(lt>1.2) s+=label(0,-110,'on their back ✓',-3,52);
   return stage(s,0,1.05,0);},
 (lt,D,t)=>{ // breathe: a calm butter circle grows and shrinks, leaves drift
   const ph=(lt%2.8)/2.8, br=0.5-0.5*Math.cos(2*Math.PI*ph);
   let s=`<circle cx="0" cy="110" r="${120+60*br}" fill="${BUT}" opacity=".55" ${o} stroke-width="4"/><circle cx="0" cy="110" r="${95+30*br}" fill="#FFF6D8" ${o} stroke-width="4"/>`;
   s+=`<text x="0" y="122" font-family="Caveat Brush" font-size="46" fill="#B23A62" text-anchor="middle">${ph<0.5?'breathe in':'and out'}</text>`;
   for(let i=0;i<3;i++){const k=(t*0.18+i*0.33)%1; s+=`<path transform="translate(${-260+520*k} ${-40+60*Math.sin(k*6+i)}) rotate(${k*200})" d="M0 0 q20 -20 40 0 q-20 20 -40 0z" fill="${SAGE}" ${o} stroke-width="3"/>`;}
   return stage(s,0,1.05,0);},
 (lt,D,t)=>{ // never shake: calm, still crib, slow steady heart (no playful motion)
   let s=crib(0,60)+bundle(0,50,-90,0.85); const p=1+0.06*Math.sin(t*2.2);
   s+=heartP(0,-110,2.2*p,1);
   return stage(s,0,1.05,0);},
 (lt,D,t)=>{ // do this: a phone types 'Can you come?', reply heart
   const msg='Can you come?', n=Math.floor(msg.length*seg(lt,0.2,1.2));
   let s=`<rect x="-160" y="-80" width="320" height="400" rx="36" fill="${INK}" ${o}/><rect x="-144" y="-60" width="288" height="360" rx="26" fill="${CREAM}"/>`;
   s+=`<rect x="-128" y="40" width="${Math.max(30,13*n+34)}" height="60" rx="22" fill="${BLUE}" ${o} stroke-width="3"/><text x="-110" y="80" font-family="Poppins" font-weight="600" font-size="22" fill="${INK}">${msg.slice(0,n)}</text>`;
   if(lt>1.4){const k=E(seg(lt,1.4,1.8)); s+=`<g opacity="${k}"><rect x="-10" y="140" width="96" height="56" rx="22" fill="${PINK}" ${o} stroke-width="3"/>${heartP(38,160,1.0,1)}</g>`;}
   s+=label(290,0,'your person',-5,50);
   return stage(s,30,1.0,-10);},
];
SC.step.special=(beat,lt)=>(y0,sag)=>'';
// ===================== frame =====================
let SPEC=null;
let T=0;
function draw(t){
 T=t; const S=SPEC, starts=S.starts, n=S.durs.length; let i=0; for(let k=0;k<n;k++) if(t>=starts[k]) i=k; const lt=t-starts[i], D=S.durs[i];
 const prog=(i+Math.min(lt/D,1))/n;
 document.getElementById('skyB').style.opacity=S.cover?1:Math.min(1,0.15+0.85*prog+(i==n-1?0.3*E(lt/0.8):0));
 const beam=S.cover?1:(i==n-1?E(seg(lt,0.2,0.7)):0);
 let svg=`<defs><radialGradient id="glow"><stop offset="0" stop-color="#FFF2B8" stop-opacity=".95"/><stop offset=".5" stop-color="#FFE7A0" stop-opacity=".45"/><stop offset="1" stop-color="#FFE7A0" stop-opacity="0"/></radialGradient>
  <radialGradient id="disc" cx=".4" cy=".35"><stop offset="0" stop-color="#FFE9A6"/><stop offset=".7" stop-color="#FFD36B"/><stop offset="1" stop-color="#FFC25A"/></radialGradient></defs>`;
 // light sweep at each cut
 const sw=seg(lt,0,0.6); if(!S.cover&&i>0&&sw<1) svg+=`<rect x="${-600+1900*E(sw)}" y="0" width="360" height="1920" fill="#FFF6D8" opacity="${0.35*Math.sin(Math.PI*sw)}" transform="skewX(-12)"/>`;
 svg+=sun(870, 1430-60*prog-(S.cover?60:0), beam, t);
 svg+=ground(t);
 const sp=SC[S.scene].special(S.cover?S.coverBeat:i, S.cover?2:lt);
 svg+=washline(t, S.cover?5:i+1, S.garments, S.cover?[-9,-9,-9,-9,-9]:starts, sp);
 if(S.cover) svg+=SC[S.scene][S.coverBeat](S.coverLt, S.durs[S.coverBeat], t);
 else svg+=SC[S.scene][i](lt, D, t);
 document.getElementById('art').innerHTML=svg;
 // text: slide in while old slides out (never blank)
 for(let k=0;k<n;k++){const el=document.getElementById('b'+k); if(S.cover){el.style.opacity=0;continue;}
  let op=0, y=0;
  if(k==i){ if(i==0){op=1;} else {const p=E(seg(lt,0.05,0.3)); op=p; y=40*(1-p);} }
  else if(k==i-1 && lt<0.12){const p=seg(lt,0,0.12); op=1-p; y=-40*E(p);}
  el.style.opacity=op; el.style.transform=`translateY(${y}px)`;}
 for(let k=0;k<n;k++){const c=document.getElementById('c'+k); if(S.cover){c.style.opacity=0;continue;} c.style.opacity=(k==i)?(i==0?(t<0.3?0:Math.min(1,(t-0.3)/0.2)):1):0;}
 const f=document.getElementById('follow'); f.style.opacity=S.cover?0:(i==n-1?E(seg(lt,0.9,1.3)):0); f.style.transform=`translateY(${S.cover?0:30*(1-E(seg(lt,0.9,1.3)))}px)`;
}
"""


def html(spec, cover=None):
    beats = spec["beats"]
    T = ""
    for k, b in enumerate(beats):
        T += (f'<div id="b{k}" style="position:absolute;left:0;top:0;width:{W}px;height:1060px;opacity:0">'
              f'<div class="hand" style="position:absolute;left:90px;width:900px;top:455px;font-size:68px;color:{KICK}">{b["kick"]}</div>'
              + K.dual(b["head"], F, cls="S fit", style=f"position:absolute;left:90px;width:900px;top:530px;white-space:nowrap;font-size:{b.get('fs', 140)}px;color:{INK}")
              + (f'<div class="lora" style="position:absolute;left:70px;width:940px;top:{b.get("sy", 940)}px;font-size:{b.get("ss", 46)}px;line-height:1.2;text-align:center;color:{INK}">{b["sub"]}</div>' if b.get("sub") else "")
              + "</div>")
        T += f'<div id="c{k}" style="position:absolute;left:0;right:0;top:1585px;text-align:center;opacity:0"><span class="chipf" style="font-size:28px">{b["chip"]}</span></div>'
    cv = ""
    if cover:
        cv = (f'<div class="hand" style="position:absolute;left:90px;width:900px;top:450px;font-size:76px;color:{KICK}">{cover["kick"]}</div>'
              + K.dual(cover["head"], F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:540px;white-space:nowrap;font-size:{cover.get('fs', 170)}px;color:{INK}")
              + (f'<div style="position:absolute;left:0;right:0;top:{cover.get("py", 1000)}px;text-align:center"><span style="display:inline-block;padding:10px 28px;border-radius:99px;background:#FF8A70;color:#FFF8EE;font:600 30px Poppins;letter-spacing:.16em">{cover["pill"]}</span></div>' if cover.get("pill") else ""))
    follow = (f'<div id="follow" style="position:absolute;left:0;right:0;top:1500px;text-align:center;opacity:0">'
              f'<span style="display:inline-block;padding:12px 30px;border-radius:99px;background:{INK};color:#FFF8EE;font:600 32px Poppins">{spec.get('follow', 'Follow for the next Little Rule ☀')}</span></div>')
    body = (f'<div id="skyA" style="position:absolute;inset:0">{sky(W, H, spec["sky"][0], horizon=0.78)}</div>'
            f'<div id="skyB" style="position:absolute;inset:0;opacity:0">{sky(W, H, spec["sky"][1], horizon=0.78)}</div>'
            f'<svg id="art" style="position:absolute;left:0;top:0" width="{W}" height="{H}" viewBox="0 0 {W} {H}"></svg>'
            + T + cv + follow + K.stamp(B, 46, 1470, size=120, rot=-10)
            + f"<script>{JS}</script>")
    return page(W, H, body)


def frames(spec, tag, cover=None, cover_out=None):
    from playwright.sync_api import sync_playwright
    durs = spec["durs"]
    starts = [sum(durs[:k]) for k in range(len(durs))]
    js_spec = dict(durs=durs, starts=starts, scene=spec["scene"], garments=spec["garments"], cover=bool(cover),
                   coverBeat=spec.get("cover_beat", 4), coverLt=spec.get("cover_lt", 2.0))
    fdir = SCR / f"{tag}-frames"
    shutil.rmtree(fdir, ignore_errors=True)
    fdir.mkdir(parents=True)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2 if cover else 1)
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, dir=SCR) as f:
            f.write(html(spec, cover))
            tmp = f.name
        pg.goto(Path(tmp).as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        pg.evaluate(K.FIT_JS, 900)
        pg.evaluate(f"SPEC={json.dumps(js_spec)}")
        if cover:
            pg.evaluate("draw(3.0)")
            png = SCR / f"{tag}-cover.png"
            pg.screenshot(path=str(png))
            Image.open(png).resize((W, H), Image.LANCZOS).convert("RGB").save(cover_out, quality=92, subsampling=0)
            br.close()
            return cover_out
        total = sum(durs)
        n = int(round(total * FPS))
        if STILLS:
            ims = []
            for ts in STILLS:
                pg.evaluate(f"draw({ts})")
                pth = SCR / f"{tag}-still.png"
                pg.screenshot(path=str(pth))
                ims.append(Image.open(pth).convert("RGB").resize((SW, int(SW*16/9))))
            sh = Image.new("RGB", ((SW+5) * len(ims), int(SW*16/9)), "white")
            for k, im in enumerate(ims):
                sh.paste(im, ((SW+5) * k, 0))
            sh.save(SCR / f"{tag}-stills.jpg", quality=85)
            br.close()
            return None
        for fr in range(n):
            pg.evaluate(f"draw({fr / FPS})")
            pg.screenshot(path=str(fdir / f"{fr:04d}.jpg"), type="jpeg", quality=95)
        br.close()
    return fdir, total, starts


def encode(fdir, total, music, pops, out_mp4):
    a = SCR / f"{out_mp4.stem}.wav"
    pop = LIB / "sfx-x-sticker-pop.mp3"
    inputs = ["-i", str(music)]
    filt = [f"[0:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.05,afade=t=out:st={total-0.6:.3f}:d=0.6[m]"]
    mix = ["[m]"]
    for k, (pt, vol) in enumerate(pops):
        inputs += ["-i", str(pop)]
        filt.append(f"[{k+1}:a]volume={vol},adelay={int(pt*1000)}|{int(pt*1000)}[p{k}]")
        mix.append(f"[p{k}]")
    filt.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[o]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[o]", "-ar", "48000", "-ac", "2", str(a)], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(fdir / "%04d.jpg"), "-i", str(a),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "slow", "-crf", "18", "-profile:v", "high",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out_mp4)], check=True)
    shutil.rmtree(fdir)


SPECS = {
    "spoil": dict(
        out="lf-reel-1025am-cant-spoil-anim", outdir=REPO / "media/recovery-oct22c/littlefold", music=LIB / "v3/lf-c-sunny-morning-el.mp3", scene="spoil", follow="Follow for one calm thing a night ☀",
        sky=("dawn", "morning"), garments=["onesie", "sock", "bib", "hat", "dress"],
        durs=[5 * BS, 6 * BS, 5 * BS, 5 * BS, 7 * BS], extra_pops=[], cover_beat=4, cover_lt=2.0,
        cover=dict(kick="heard “you'll spoil her”?", head="You can't / *spoil* a / newborn.", fs=160, pill="", py=1000),
        beats=[
            dict(kick="heard “you'll spoil her”?", head="You can't / *spoil* a / newborn.", sub="Pick them up.", fs=136, sy=960, ss=50, chip="CPS · Colic and crying"),
            dict(kick="because", head="Answer their / cries, and / they cry *less.*", fs=136, chip="AAP · Responding to your baby's cries"),
            dict(kick="first, check", head="Hungry? / Diaper? / *Too hot or cold?*", fs=136, chip="CPS · Colic and crying"),
            dict(kick="then", head="Hold close. / *Sway.* Shush. / Walk.", fs=136, chip="CPS · Colic and crying"),
            dict(kick="Do this:", head="Next cry: / *pick them up* / first.", sub="send this to someone in the newborn weeks", fs=136, sy=960, ss=42, chip="CPS · AAP"),
        ]),
    "stepaway": dict(
        out="lf-reel-1025-step-away-anim", outdir=REPO / "media/recovery-oct22c/littlefold", music=LIB / "v3/lf-b-tender-el.mp3", scene="step", follow="Follow for one calm thing a night ☀",
        sky=("afternoon", "morning"), garments=["hat", "onesie", "sock", "dress", "bib"],
        durs=[4 * BT, 3 * BT, 4 * BT, 4 * BT, 5 * BT], extra_pops=[], no_pop=[3], cover_beat=4, cover_lt=2.2,
        cover=dict(kick="still crying? at your limit?", head="It's OK to / *step away.*", fs=170, pill="", py=1000),
        beats=[
            dict(kick="still crying? at your limit?", head="It's OK to / *step away.*", fs=150, chip="CPS · Colic and crying"),
            dict(kick="first", head="Crib first. / *On their back.*", fs=140, chip="CPS · Colic and crying"),
            dict(kick="then", head="Step out. / Breathe. / *Take a moment.*", fs=136, chip="CPS · Colic and crying"),
            dict(kick="and always", head="Never shake / a baby. / *Never.*", fs=140, chip="CPS · Colic and crying"),
            dict(kick="Do this:", head="Tonight, pick / *who you'll text.*", sub="“Can you come?” It's OK to ask for help.", fs=136, sy=900, ss=44, chip="CPS · Colic and crying"),
        ]),
    "carseat": dict(
        out="lf-reel-coat-off-buckle", music=LIB / "v4/lf-x-sunny-bounce.mp3", scene="coat",
        sky=("dawn", "morning"), garments=["hat", "dress", "sock", "onesie", "none"],
        durs=[5 * BB, 5 * BB, 5 * BB, 5 * BB, 7 * BB],
        extra_pops=[(5 * BB * 0 + 1.75, 0.3)],  # buckle click
        cover_beat=3, cover_lt=2.0,
        cover=dict(kick="first cold morning?", head="Coat *off.* / Then buckle.", fs=170, pill="LITTLE RULES · No.1", py=930),
        beats=[
            dict(kick="first cold morning?", head="Coat *off.* / Then buckle.", sub="Warm goes on top of the straps.", fs=150, chip="AAP · CPS"),
            dict(kick="because", head="Puffy padding / *squashes flat* / in a crash.", sub="That leaves room to slip out of the straps.", fs=126, sy=960, ss=42, chip="AAP · Winter car seat safety"),
            dict(kick="the pinch test", head="Pinch the strap. / *Can you?* / Tighten it.", fs=130, chip="AAP · Winter car seat safety"),
            dict(kick="to stay warm", head="Thin layers. / *Blanket over* / the straps.", fs=136, chip="AAP · Winter car seat safety"),
            dict(kick="Do this:", head="Coat off. / Buckle. / *Blanket on.*", sub="save this for the first cold morning", fs=136, sy=960, ss=42, chip="AAP · CPS"),
        ]),
    "teething": dict(
        out="lf-reel-teething-cold-cloth", music=LIB / "lf-cosy-el-01.mp3", scene="teeth",
        sky=("afternoon", "morning"), garments=["bib", "onesie", "hat", "sock", "dress"],
        durs=[4 * BC, 4 * BC, 4 * BC, 4 * BC, 6 * BC],
        extra_pops=[],
        cover_beat=4, cover_lt=2.0,
        cover=dict(kick="sore gums tonight?", head="Cold cloth. / *Gentle rub.*", fs=170, pill="LITTLE RULES · No.2", py=930),
        beats=[
            dict(kick="sore gums tonight?", head="Cold cloth. / *Gentle rub.*", sub="Two simple fixes for sore gums.", fs=150, chip="AAP · Teething pain"),
            dict(kick="the cloth", head="Wet it. / Twist it. / *Chill it.*", fs=130, chip="AAP · Teething pain"),
            dict(kick="skip", head="Teething / necklaces. / *Choking risk.*", sub="Amber, wood, marble or silicone.", fs=128, sy=960, ss=42, chip="AAP · Teething pain"),
            dict(kick="skip", head="Numbing gels / with *benzocaine.*", sub="They can be dangerous for children.", fs=128, ss=44, chip="AAP · Teething pain"),
            dict(kick="Do this:", head="Chill a cloth / *tonight.*", sub="A high fever isn't a teething sign.<br>Call your baby's doctor.", fs=150, ss=42, chip="AAP · Teething pain"),
        ]),
}

STILLS = None
SW = 270
if __name__ == "__main__":
    for a in sys.argv:
        if a.startswith("--still="):
            STILLS = [float(x) for x in a[8:].split(",")]
        if a.startswith("--sw="):
            SW = int(a[5:])
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    for key in (args or SPECS):
        s = SPECS[key]
        od = s.get("outdir", OUTD); od.mkdir(parents=True, exist_ok=True)
        frames(s, key, cover=s["cover"], cover_out=od / f"{s['out']}-cover.jpg")
        print("cover", key)
        if "--cover-only" in sys.argv:
            continue
        r = frames(s, key)
        if r is None:
            print("stills", SCR / f"{key}-stills.jpg")
            continue
        fdir, total, starts = r
        pops = [(st + 0.1, 0.22) for k, st in enumerate(starts) if k > 0 and k not in s.get("no_pop", [])] + s["extra_pops"]
        out = od / f"{s['out']}.mp4"
        encode(fdir, total, s["music"], pops, out)
        print(out, round(total, 2))

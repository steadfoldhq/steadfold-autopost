#!/usr/bin/env python3
"""Oct 24 (Social studio, lf-b): two Littlefold Reels in the proven 'sunshine washing-line' story system
(studio/recovery-oct22c/littlefold/reel_story.py, imported as RS; reel_story.py itself is not edited).

  bath     lf-reel-1027am-bath-elbow   Tue Oct 27 08:00 ET  (NHS 'Bathing your baby' + AAP 'Bathing Your Baby')
  swaddle  lf-reel-1027-swaddle-hips   Tue Oct 27 19:00 ET  (AAP 'Swaddling: Is it Safe for Your Baby?')

New drawn vignettes (plum outlines, sherbet fills, adult arms/hands only, the faceless swaddled bundle):
  SC.bath:    elbow dips into a cross-section baby bath, ripples, steam settles, check; cold tap then hot tap, a hand
              mixes the hot patch away; phone buzzes, hands lift the bundle out in a towel and carry it along;
              Do this: elbow in again, bubbles + hearts, a hooded towel is pegged on the line.
  SC.swaddle: top view on a thin blanket: legs bend up and out (frog), wrap folds over the chest, the bottom folds up
              loosely, 'room here' arrows at the hips; two fingers slide under the wrap at the chest; the bundle rocks
              (trying to roll) and the swaddle comes off; Do this: loose-hip wrap with hearts, blanket on the line.
No 'Little Rules' pill (series unapproved). Short follow pill on screen; full follow line in the caption.

    python3 studio/editorial/oct24_lf_b.py bath|swaddle [--still=0.2,1.5,...] [--cover-only]
"""
import os
import sys
sys.dont_write_bytecode = True
os.environ.setdefault("LF_SCR", "/tmp/claude-0/lf-b")
sys.path.insert(0, "/home/claude/steadfold-autopost/studio/recovery-oct22c/littlefold")
import reel_story as RS  # noqa: E402

OUT = RS.REPO / "media" / "studio-oct24" / "littlefold"
FOLLOW = "Follow for one calm thing a night ☀"
BG = 60 / 120.2   # v4/lf-x-giggle-pop
BT = RS.BT        # v3/lf-b-tender-el

JS_ADD = r"""
// ===================== oct24 lf-b: bath + swaddle =====================
function limb(d,w,col){return `<path d="${d}" stroke="${PL}" stroke-width="${w+10}" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}" stroke="${col}" stroke-width="${w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;}
const lerp=(a,b,k)=>a+(b-a)*k;
function mixCol(a,b,k){const p=s=>[1,3,5].map(i=>parseInt(s.slice(i,i+2),16));const A=p(a),B=p(b);return `rgb(${A.map((v,i)=>Math.round(lerp(v,B[i],k))).join(',')})`;}
G.towel=()=>`<path d="M-58 6 H58 L62 150 Q0 162 -62 150 Z" fill="${CREAM}" ${o}/><path d="M-58 6 H58 L0 66 Z" fill="${PEACH}" ${o}/><circle cx="-26" cy="20" r="9" fill="${PEACH}" ${o} stroke-width="3"/><circle cx="26" cy="20" r="9" fill="${PEACH}" ${o} stroke-width="3"/><path d="M-62 128 Q0 140 62 128" stroke="${PL}" stroke-width="3" fill="none" opacity=".5"/>`+peg(-44)+peg(44);
G.swaddle=()=>`<path d="M-60 6 H60 L66 150 Q0 164 -66 150 Z" fill="${BUT}" ${o}/><path d="M-60 40 H60 M-62 112 H62" stroke="${PL}" stroke-width="3" opacity=".45"/>`+heartP(-20,74,0.9,1)+heartP(28,96,0.7,1)+peg(-44)+peg(44);
// ---------- bath props (cross-section tub, adult arm)
const TIN="M-222 -10 Q-232 186 -118 212 H118 Q232 186 222 -10 Z";
function tubBack(){return `<rect x="-200" y="236" width="40" height="26" rx="10" fill="#F6A98A" ${o}/><rect x="160" y="236" width="40" height="26" rx="10" fill="#F6A98A" ${o}/>
 <path d="M-250 -10 Q-262 210 -130 242 H130 Q262 210 250 -10 Z" fill="${PINK}" ${o}/><path d="${TIN}" fill="#FFF6EC" ${o} stroke-width="4"/>`;}
function water(level,col,t,extra){const wy=205-200*level, a=7*Math.sin(t*3.1);
 return `<clipPath id="tc"><path d="${TIN}"/></clipPath><g clip-path="url(#tc)"><path d="M-260 ${wy} Q-195 ${wy-a} -130 ${wy} T0 ${wy} T130 ${wy} T260 ${wy} V270 H-260Z" fill="${col}" opacity=".82"/>${extra||''}
 <path d="M-260 ${wy} Q-195 ${wy-a} -130 ${wy} T0 ${wy} T130 ${wy} T260 ${wy}" stroke="#FFFFFF" stroke-width="5" fill="none" opacity=".8"/></g>`;}
function tubLip(){return `<rect x="-266" y="-24" width="532" height="26" rx="13" fill="${CREAM}" ${o}/>`;}
function arm(ex,ey){const sx=ex+260,sy=ey-170,hx=ex-90,hy=ey-200;
 return limb(`M${sx} ${sy} L${ex} ${ey} L${hx} ${hy}`,64,SK)+`<path d="M${ex+4} ${ey-40} q12 12 26 4" stroke="${SKD}" stroke-width="4" fill="none" stroke-linecap="round"/>`
  +limb(`M${sx+60} ${sy-40} L${ex+150} ${ey-98}`,84,BLUE)+`<path d="M${ex+125} ${ey-137} L${ex+175} ${ey-59}" stroke="${PL}" stroke-width="4"/>`
  +`<ellipse cx="${hx-4}" cy="${hy-22}" rx="40" ry="44" fill="${SK}" ${o}/><path d="M${hx-26} ${hy-44} q16 -6 32 0 M${hx-28} ${hy-26} q16 -6 32 0" stroke="${SKD}" stroke-width="3.5" fill="none" stroke-linecap="round"/>`;}
function steam(x,y,k,t){let s='';for(let i=0;i<3;i++){const ph=(t*0.5+i*0.33)%1, yy=y-90*ph;
 s+=`<path d="M${x+i*70} ${yy} q-18 -26 0 -52 q18 -26 0 -52" stroke="#FFFFFF" stroke-width="9" fill="none" stroke-linecap="round" opacity="${k*Math.sin(Math.PI*ph)}"/>`;}return s;}
function ripples(x,y,k){let s='';for(let i=0;i<3;i++){const p=cl(k*1.4-i*0.25,0,1);if(p<=0||p>=1)continue;s+=`<ellipse cx="${x}" cy="${y}" rx="${30+150*p}" ry="${8+26*p}" fill="none" stroke="#FFFFFF" stroke-width="5" opacity="${1-p}"/>`;}return s;}
function tap(x,y,col,flow,wy,t){let s=`<path d="M${x+130} ${y-40} H${x+10} Q${x-22} ${y-40} ${x-22} ${y-8} V${y+6}" stroke="${PL}" stroke-width="40" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M${x+130} ${y-40} H${x+10} Q${x-22} ${y-40} ${x-22} ${y-8} V${y+6}" stroke="${CREAM}" stroke-width="28" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cx="${x+86}" cy="${y-62}" r="20" fill="${col}" ${o}/>`;
 if(flow>0){s+=`<path d="M${x-22} ${y+16} V${wy}" stroke="${col}" stroke-width="${14*flow}" stroke-linecap="round" opacity=".9"/>`;
  for(let i=0;i<4;i++){const k=(t*2.2+i*0.25)%1;s+=`<circle cx="${x-22+((i%2)?8:-8)}" cy="${y+20+(wy-y-20)*k}" r="${7*flow}" fill="#FFFFFF" opacity="${0.8*flow}"/>`;}}
 return s;}
function phone(x,y,buzz,t){const j=buzz?5*Math.sin(t*60):0;let s=`<g transform="translate(${x+j} ${y}) rotate(${-8+j})"><rect x="-38" y="-66" width="76" height="132" rx="16" fill="${INK}" ${o}/><rect x="-28" y="-54" width="56" height="100" rx="8" fill="${BLUE}"/><circle cx="0" cy="54" r="5" fill="${CREAM}"/></g>`;
 if(buzz){for(let i=0;i<2;i++)s+=`<path d="M${x-60-i*16} ${y-30} q-12 30 0 60 M${x+60+i*16} ${y-30} q12 30 0 60" stroke="#B23A62" stroke-width="5" fill="none" stroke-linecap="round" opacity="${0.5+0.5*Math.sin(t*20)}"/>`;}
 return s;}
function bubbles(t,x,y){let s='';for(let i=0;i<6;i++){const k=(t*0.5+i/6)%1;s+=`<circle cx="${x+(i-2.5)*60+12*Math.sin(t*3+i)}" cy="${y-170*k}" r="${10+6*(i%3)}" fill="#FFFFFF" fill-opacity=".55" stroke="${PL}" stroke-width="3" opacity="${Math.sin(Math.PI*k)}"/>`;}return s;}
const WARM='#D9E2F4';
SC.bath=[
 (lt,D,t)=>{ // elbow dips in, ripples, steam settles, check
   const dip=EIO(seg(lt,0.12,0.9)), ex=lerp(60,40,dip), ey=lerp(40,110,dip);
   let s=tubBack()+steam(-120,40,1-0.55*seg(lt,0.9,1.6),t)+arm(ex,ey)+water(0.75,WARM,t,ripples(ex,55,seg(lt,0.85,2.2)))+tubLip();
   s+=label(-95,175,lt<1.0?'elbow in ↓':'warm, not hot',-4,52);
   if(lt>1.5) s+=check(-200,60,seg(lt,1.5,2.0));
   return stage(s,0,1.0,90);},
 (lt,D,t)=>{ // cold tap first, then hot, then a hand mixes the hot patch away
   const cold=seg(lt,0.1,1.35), hot=seg(lt,1.35,2.15), mix=EIO(seg(lt,2.1,3.3));
   const level=0.08+0.47*E(cold)+0.2*E(hot), wy=205-200*level;
   const fc=lt>0.1&&lt<1.4?1:0, fh=lt>1.4&&lt<2.15?1:0;
   const blob=hot>0?`<ellipse cx="${60+20*Math.sin(t*2)}" cy="${wy+48}" rx="${(40+60*E(hot))*(1-mix)}" ry="${(20+22*E(hot))*(1-mix)}" fill="#FFC870" opacity="${0.55*(1-mix)}"/>`+[0,1,2].map(i=>`<path d="M${10+i*40+14*Math.sin(t*4+i)} ${wy+30+i*12} q15 -8 30 0 q15 8 30 0" stroke="#FFF3C4" stroke-width="5" fill="none" stroke-linecap="round" opacity="${(0.5+0.5*Math.sin(t*7+i*2))*(1-mix)}"/>`).join(''):'';
   let sw='';if(mix>0&&mix<1){for(let i=0;i<3;i++){const a=t*5+i*2.1;sw+=`<path d="M${40+70*Math.cos(a)} ${wy+50+20*Math.sin(a)} A70 22 0 0 1 ${40+70*Math.cos(a+1.4)} ${wy+50+20*Math.sin(a+1.4)}" stroke="#FFFFFF" stroke-width="6" fill="none" stroke-linecap="round"/>`;}}
   let s=tubBack()+(hot>0?steam(0,wy-6,E(hot)*(1-mix),t):'')+water(level,mixCol('#BFD9F2',WARM,mix),t,blob+sw)+tubLip();
   s+=tap(-130,-50,'#7FB3E6',fc,wy,t)+tap(50,-50,CORAL,fh,wy,t);
   if(lt>2.0&&lt<3.45){const a=t*5; s+=`<g opacity="${seg(lt,2.0,2.2)*(1-seg(lt,3.25,3.45))}">${hand(60+50*Math.cos(a),wy+6+12*Math.sin(a),-18,0.75,0.2)}</g>`;}
   s+=label(-90,175,lt<1.35?'cold first':(lt<2.1?'then hot':'mix it well'),-4,54);
   if(lt>2.9) s+=check(150,150,seg(lt,2.9,3.4));
   return stage(s,0,1.0,90);},
 (lt,D,t)=>{ // baby just lifted out in a hooded towel; the phone buzzes; baby is carried along to it
   const up=EIO(seg(lt,0.0,0.6)), go=EIO(seg(lt,1.5,2.7)), bx=lerp(0,-170,go), by=lerp(10,-30,up)+60*go;
   let s=tubBack()+water(0.75,WARM,t)+tubLip()+phone(-330,150,lt<2.6,t);
   let b=`<g transform="translate(${bx} ${by}) rotate(${4*Math.sin(t*2.4)})">`+bundle(0,0,0,0.85)
     +`<path transform="scale(.85)" d="M-84 -30 Q-100 70 -44 128 Q0 146 44 128 Q100 70 84 -30 Q0 0 -84 -30Z" fill="${CREAM}" ${o}/><path transform="scale(.85)" d="M-74 40 Q0 70 74 40" stroke="${PL}" stroke-width="3" fill="none" opacity=".5"/>`
     +`<path transform="scale(.85)" d="M-48 -64 Q0 -128 48 -64 Q24 -50 0 -50 Q-24 -50 -48 -64Z" fill="${PEACH}" ${o}/><circle cx="-26" cy="-84" r="11" fill="${PEACH}" ${o} stroke-width="3"/><circle cx="26" cy="-84" r="11" fill="${PEACH}" ${o} stroke-width="3"/>`
     +hand(62,40,0,0.55,0.55)+`<g transform="scale(-1 1)">${hand(62,40,0,0.55,0.55)}</g>`+`</g>`;
   let drips='';if(lt<1.4){for(let i=0;i<3;i++){const k=(lt*2+i*0.33)%1;drips+=`<path d="M${bx-40+i*40} ${by+110+50*k} q-9 14 0 20 q9 -6 0 -20z" fill="${BLUE}" stroke="${PL}" stroke-width="2.5" opacity="${1-k}"/>`;}}
   s+=b+drips+label(-330,40,'buzz…',-6,46);
   s+=label(250,-45,lt>2.4?'baby comes too ♡':'not even a second',-5,50);
   return stage(s,0,1.0,90);},
 (lt,D,t)=>{ // do this: elbow in again, check, bubbles + hearts
   const dip=EIO(seg(lt,0.1,0.75)), ex=lerp(60,40,dip), ey=lerp(40,110,dip)+8*Math.sin(t*3)*seg(lt,0.8,1.2);
   const rp=lt<0.7?0:((lt-0.7)%1.5)/1.5, dx=-150+60*Math.sin(t*1.3), dy=50+5*Math.sin(t*3.4);
   const duck=`<g transform="translate(${dx} ${dy}) rotate(${6*Math.sin(t*3.4)})" opacity="${seg(lt,0.3,0.6)}"><path d="M-40 0 Q-44 -26 -14 -24 Q-22 -60 6 -62 Q30 -62 30 -38 L50 -34 L32 -24 Q44 -4 34 6 Q0 18 -40 0Z" fill="${BUT}" ${o} stroke-width="4"/><circle cx="12" cy="-44" r="4.5" fill="${INK}"/><path d="M-16 -8 q14 6 26 -2" stroke="${PL}" stroke-width="3" fill="none"/></g>`;
   let s=tubBack()+arm(ex,ey)+water(0.75,WARM,t,ripples(ex,55,rp))+duck+tubLip()+bubbles(t,-40,40);
   if(lt>0.85) s+=check(-200,60,seg(lt,0.85,1.3));
   s+=hearts(t,-60,30);
   return stage(s,0,1.0,90);},
];
SC.bath.special=(beat,lt)=>(y0,sag)=>{ if(beat<3) return ''; const f=EIO(seg(lt,0.6,1.5)); const tx=930, ty=lineY(930,y0,sag)+8;
  const sx=440, sy=1180; const X=sx+(tx-sx)*f, Y=sy+(ty-sy)*f-160*Math.sin(Math.PI*f);
  return `<g transform="translate(${X} ${Y}) rotate(${-20*(1-f)+(4+6*f)*Math.sin(T*2.6)}) scale(.88)">${G.towel()}</g>`;};
// ---------- swaddle props (top view, faceless bundle on a thin blanket)
function mattress(){return `<rect x="-360" y="-130" width="660" height="520" rx="60" fill="#DCEBF7" ${o}/>`;}
function diamond(op,dx){return `<g opacity="${op}" transform="translate(${dx||0} 0)"><path d="M0 -112 L280 120 L0 365 L-280 120Z" fill="${BUT}" ${o}/><path d="M-70 -54 L0 -112 L70 -54 Q0 -30 -70 -54Z" fill="#FFF1B8" ${o} stroke-width="4"/>
 ${[[-150,130],[150,130],[0,300]].map(p=>heartP(p[0],p[1],0.9,0.7)).join('')}</g>`;}
function legs(k,dashed){let s='';[-1,1].forEach(sd=>{const kx=sd*lerp(42,122,k),ky=lerp(242,214,k),fx=sd*lerp(40,58,k),fy=lerp(306,292,k);const d=`M${sd*36} 170 L${kx} ${ky} L${fx} ${fy}`;
  s+=dashed?`<path d="${d}" stroke="${PL}" stroke-width="5" fill="none" stroke-dasharray="7 11" stroke-linecap="round" stroke-linejoin="round"/>`:limb(d,36,PINK)+`<circle cx="${fx}" cy="${fy+8}" r="20" fill="${CREAM}" ${o}/>`;});return s;}
function body(armsOut){return `<path d="M-72 20 Q-84 120 -56 178 H56 Q84 120 72 20 Q0 2 -72 20Z" fill="${PINK}" ${o}/>`+(armsOut?limb('M-68 40 Q-120 70 -150 30',30,PINK)+limb('M68 40 Q120 70 150 30',30,PINK):limb('M-70 40 Q-98 92 -72 146',28,PINK)+limb('M70 40 Q98 92 72 146',28,PINK));}
function hat(){return `<circle cx="0" cy="-34" r="54" fill="${SAGE}" ${o}/><rect x="-58" y="-6" width="116" height="26" rx="12" fill="#A8CA9A" ${o}/><circle cx="0" cy="-92" r="15" fill="${CREAM}" ${o}/>`;}
function pouch(k){if(k<=0)return '';return `<g transform="translate(0 ${150*(1-k)})" opacity="${cl(k*2,0,1)}"><path d="M-150 160 Q-190 300 -40 350 Q0 358 40 350 Q190 300 150 160 Q0 186 -150 160Z" fill="${BUT}" fill-opacity=".5" ${o}/>
 <path d="M-110 200 Q-120 280 -60 320 M110 200 Q120 280 60 320" stroke="${PL}" stroke-width="3" fill="none" opacity=".45"/></g>`;}
function flapL(k){if(k<=0)return '';return `<g transform="translate(${-260*(1-k)} 0)" opacity="${cl(k*3,0,1)}"><path d="M-116 12 Q0 0 116 60 L156 142 L102 188 Q0 196 -106 180Z" fill="${BUT}" ${o}/><path d="M-96 52 Q20 50 132 120 M-90 120 Q20 110 104 160" stroke="${PL}" stroke-width="3" fill="none" opacity=".4"/></g>`;}
function flapR(k){if(k<=0)return '';return `<g transform="translate(${260*(1-k)} 0)" opacity="${cl(k*3,0,1)}"><path d="M116 22 Q0 8 -116 64 L-156 150 L-102 190 Q0 198 106 182Z" fill="#FFD66E" ${o}/><path d="M96 62 Q-20 58 -132 128 M90 128 Q-20 118 -104 166" stroke="${PL}" stroke-width="3" fill="none" opacity=".4"/></g>`;}
function room(k,t){if(k<=0)return '';const w=8*Math.sin(t*4);let s='';[-1,1].forEach(sd=>{const x0=sd*165,x1=sd*(225+w);s+=`<path d="M${x0} 236 H${x1} M${x1-sd*20} 220 L${x1} 236 L${x1-sd*20} 252" stroke="#B23A62" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="${k}"/>`;});return s;}
function wrapped(bend,t,roomK){return diamond(1)+legs(bend,false)+body(false)+pouch(1)+legs(bend,true)+flapL(1)+flapR(1)+hat()+room(roomK,t);}
SC.swaddle=[
 (lt,D,t)=>{ // legs bend up and out, wrap folds over the chest, bottom folds up loosely, 'room here'
   const bend=EIO(seg(lt,0.05,0.75)), kl=EIO(seg(lt,0.8,1.3)), kr=EIO(seg(lt,1.25,1.75)), kp=EIO(seg(lt,1.7,2.3));
   let s=mattress()+diamond(1)+legs(bend,false)+body(false)+pouch(kp)+(kp>0.3?legs(bend,true):'')+flapL(kl)+flapR(kr)+hat()+room(seg(lt,2.2,2.5),t);
   if(lt<0.85) s+=label(-235,335,'up and out',-5,44);
   else if(lt>2.25) s+=label(-235,335,'room here',-5,46);
   if(lt>2.6) s+=check(235,300,seg(lt,2.6,3.1));
   return stage(s,0,0.9,65);},
 (lt,D,t)=>{ // two fingers slide under the wrap at the chest
   const inn=EIO(seg(lt,0.2,1.3)), out=EIO(seg(lt,2.7,3.4)), fx=lerp(380,30,inn)+350*out;
   let s=mattress()+wrapped(1,t,0);
   s+=`<g transform="translate(${fx} 44)">${limb('M330 6 L560 36',84,SK)+limb('M500 28 L780 64',104,BLUE)}<path d="M498 -26 L486 84" stroke="${PL}" stroke-width="4"/>${limb('M150 -16 H0',26,SK)+limb('M150 16 H14',26,SK)}<path d="M120 -56 Q250 -70 330 -40 L340 70 Q240 90 120 60 Z" fill="${SK}" ${o}/>${limb('M150 -50 Q110 -70 84 -64',24,SK)}<path d="M140 -20 q-10 16 0 32 M150 12 q-10 16 0 32" stroke="${SKD}" stroke-width="4" fill="none" stroke-linecap="round"/></g>`;
   s+=`<path d="M-104 30 Q0 12 104 30" stroke="${PL}" stroke-width="30" fill="none" stroke-linecap="round"/><path d="M-104 30 Q0 12 104 30" stroke="#FFD66E" stroke-width="20" fill="none" stroke-linecap="round"/>`+hat();
   if(lt>1.0) s+=label(-235,335,'fingers fit',-5,44);
   if(lt>1.5) s+=check(235,300,seg(lt,1.5,2.0));
   return stage(s,0,0.9,65);},
 (lt,D,t)=>{ // the bundle rocks (trying to roll); the swaddle comes off, arms free
   const rk=seg(lt,0.1,0.4)*(1-seg(lt,1.2,1.5)), ang=13*rk*Math.sin(t*6.5), off=EIO(seg(lt,1.25,2.0));
   let g=diamond(1-off,-300*off)+legs(1,false)+body(off>0.6)+pouch(1-off)+(off<0.3?legs(1,true):'')+flapL(1-off)+flapR(1-off)+hat();
   let s=mattress()+`<g transform="rotate(${ang} 0 150)">${g}</g>`;
   if(rk>0.05){for(let i=0;i<2;i++)s+=`<path d="M${-210-i*26} 60 q-22 90 0 180 M${210+i*26} 60 q22 90 0 180" stroke="#B23A62" stroke-width="6" fill="none" stroke-linecap="round" opacity="${rk*(0.5+0.5*Math.sin(t*12+i))}"/>`;}
   s+=label(-232,335,lt<1.3?'trying to roll?':'swaddle off',-5,36);
   return stage(s,0,0.9,65);},
 (lt,D,t)=>{ // do this: loose-hip wrap, legs move, hearts
   const bend=0.88+0.12*Math.sin(t*3);
   let s=mattress()+wrapped(bend,t,1)+label(-235,335,'room here ♡',-5,44)+hearts(t,0,-40);
   return stage(s,0,0.9,65);},
];
SC.swaddle.special=(beat,lt)=>(y0,sag)=>'';
"""
assert 'if(i==0){op=1;} else {const p=E(seg(lt,0.05,0.3)); op=p; y=40*(1-p);} }\n  else if(k==i-1 && lt<0.12){const p=seg(lt,0,0.12); op=1-p; y=-40*E(p);}' in RS.JS
RS.JS = RS.JS.replace('if(i==0){op=1;} else {const p=E(seg(lt,0.05,0.3)); op=p; y=40*(1-p);} }\n  else if(k==i-1 && lt<0.12){const p=seg(lt,0,0.12); op=1-p; y=-40*E(p);}', 'if(i==0){op=1;} else {const p=E(seg(lt,0.09,0.32)); op=p; y=110*(1-p);} }\n  else if(k==i-1 && lt<0.1){const p=seg(lt,0,0.1); op=1-E(p); y=-120*E(p);}', 1) + JS_ADD

RS.SPECS["bath"] = dict(
    out="lf-reel-1027am-bath-elbow", outdir=OUT, music=RS.LIB / "v4/lf-x-giggle-pop.mp3", scene="bath", follow=FOLLOW,
    sky=("dawn", "morning"), garments=["sock", "hat", "onesie", "bib", "none"],
    durs=[6 * BG, 7 * BG, 8 * BG, 8 * BG], extra_pops=[], cover_beat=3, cover_lt=2.0,
    cover=dict(kick="Bath water too hot?", head="Elbow in. / *Then baby in.*", fs=170, pill="", py=1000),
    beats=[
        dict(kick="Bath water too hot?", head="Dip your *elbow* / in first.", sub="It should feel warm, not hot.", fs=150, sy=870, chip="NHS · AAP"),
        dict(kick="filling it?", head="Cold water *first.* / Then hot. / *Mix it well.*", sub="So there are no hot patches.", fs=136, sy=960, chip="NHS · Bathing your baby"),
        dict(kick="and always", head="Never leave them / alone in the bath. / *Not for a second.*", sub="Phone or doorbell? Take baby with you.", fs=126, sy=960, ss=44, chip="NHS · AAP"),
        dict(kick="Do this:", head="Elbow in. / *Then baby in.*", sub="send this to whoever does bath time", fs=150, sy=870, ss=44, chip="NHS · AAP"),
    ])

RS.SPECS["swaddle"] = dict(
    out="lf-reel-1027-swaddle-hips", outdir=OUT, music=RS.LIB / "v3/lf-b-tender-el.mp3", scene="swaddle", follow=FOLLOW,
    sky=("afternoon", "morning"), garments=["hat", "sock", "onesie", "swaddle", "dress"],
    durs=[5 * BT, 5 * BT, 4 * BT, 6 * BT], extra_pops=[], cover_beat=3, cover_lt=2.0,
    cover=dict(kick="swaddling?", head="Leave room / for the *hips.*", fs=170, pill="", py=1000),
    beats=[
        dict(kick='<span style="font-size:58px">Swaddling? Leave room for the hips.</span>', head="Legs bend / *up and out.*",
             sub="Tight, straight legs can harm their hips.", fs=150, ss=44, chip="AAP · Swaddling"),
        dict(kick="check the chest", head="Slide 2 or 3 fingers / between the wrap / *and their chest.*", sub="If they fit, it's not too tight.",
             fs=120, sy=960, ss=44, chip="AAP · Swaddling"),
        dict(kick="when to stop", head="Trying to roll? / *Stop swaddling.*", sub="Some start trying at 2 months.", fs=140, ss=44, chip="AAP · Swaddling"),
        dict(kick="Do this:", head="Tonight, leave / *room at the hips.*", sub="send this to whoever does the night feeds", fs=140, ss=42, chip="AAP · Swaddling"),
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

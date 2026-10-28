#!/usr/bin/env python3
"""Oct 28 (Social studio, Littlefold maker): two Reels in the illustrated "physical rule, shown being done" format
(sunshine washing-line world; studio/recovery-oct22c/littlefold/reel_story.py imported, not edited; Oct 24 props via
oct24_lf_a.py and the Oct 27 top-view baby + changing mat via oct27_littlefold.JS_STUMP, both imported, not edited).

1. lf-reel-1029am-hot-drink (Thu Oct 29 08:00, trial auto) -- SEND-BEAT TEST
   SC.mug: frame 0 a steaming mug in an adult hand beside a baby in a bassinet; a dotted line draws to a high shelf, the
   mug travels along it and lands ('out of reach'), then two hands lift the baby (by ~2.5 s); a little arm reaches for a
   bright mug at the table edge and the mug flies up to the shelf; a clock sweeps 15 minutes while the mug keeps
   steaming; Do this: mug on the shelf, baby held and swaying, hearts, a tea towel pegged on the line.
   Last beat carries the on-screen send line "Send this to the grandparent who always has a cup of tea."
   COVER: follow the line (style-menu #9, quiet).
2. lf-reel-1031am-hand-on-baby (Sat Oct 31 08:00, trial auto)
   SC.change: frame 0 a wriggling baby on a changing mat, the wipes out of reach; a flat palm lands on the tummy and
   stays while the other hand fetches the wipes (by ~1.6 s); diaper, wipes and clean clothes pop in with ticks; a doorbell
   rings and the baby is lifted off the mat and carried along; Do this: palm on tummy, check, hearts, a diaper pegged.
   COVER: Littlefold soft countdown giant numeral (style-menu #2, 'lf-count', loud).

Facts (checked Oct 28 2026):
  NHS 'Baby and toddler safety' (nhs.uk/conditions/baby/first-aid-and-safety/safety/baby-and-toddler-safety/,
    last reviewed 19 Feb 2026): "If you're having a hot drink, put it down well out of reach before you hold your baby.";
    "Babies and toddlers will grab at brightly coloured objects, such as mugs."; "A hot drink can still scald 15 minutes
    after it was made."; "A baby's skin burns more easily than an adult's."; "Change your baby's nappy on a changing mat
    on the floor."; "Do not leave your baby unattended on a bed, sofa or changing table, even for a second, as they could
    roll off."
  Health Canada 'Change tables' (canada.ca/en/health-canada/services/infant-care/change-tables.html): "keeping one hand
    on your baby at all times when using the change table, even with the safety straps in use"; "preparing everything
    you need before you place your baby on the change table"; "taking your baby with you if you leave the area for any reason".

    python3 studio/editorial/oct28_littlefold.py mug|change [--still=0.0,1.5,...] [--cover-only]
"""
import os
import sys
import tempfile
from pathlib import Path
sys.dont_write_bytecode = True
os.environ["LF_SCR"] = "/tmp/claude-0/oct28-littlefold"
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oct24_lf_a as A  # noqa: E402  (adds palm, babyBack, bottle, table, thigh, forearm ... to RS.JS)
import oct27_littlefold as S27  # noqa: E402  (JS_STUMP: babyTop, mat, G.diaper, popBurstS; nothing runs on import)
RS = A.RS

K, F, INK, KICK, B = RS.K, RS.F, RS.INK, RS.KICK, RS.B
W, H = RS.W, RS.H
OUT = RS.REPO / "media" / "studio-oct28" / "littlefold"
LIB = RS.LIB
FOLLOW = "Follow for one calm thing a night, from bump to toddler."
SEND = "Send this to the grandparent who always has a cup of tea."
BG = 60 / 120.2    # lf-x-giggle-pop (v4), drop 3.971 s
BP = 60 / 103.4    # lf-x-tiny-parade (v4), drop 9.195 s
DROP_BP = 9.195

# Oct 27 helpers without its duplicate `const BSK` (oct24 already declares it) and without its SC.stump scenes.
JS27 = S27.JS_STUMP.replace("const BSK='#FFDCC4';", "")
JS27 = JS27[:JS27.index("SC.stump=[")]

JS = r"""
// ===================== Oct 28: hot drink + changing table =====================
const STEAM='#C98BA6';
function steam(x,y,t,op,s){s=s||1;let w='';for(let i=0;i<3;i++){const k=(t*0.8+i/3)%1, xx=x+(i-1)*30*s, yy=y-20*s-70*s*k;
  w+=`<path d="M${xx} ${yy} q${-14*s} ${-18*s} 0 ${-36*s} q${14*s} ${-18*s} 0 ${-36*s}" stroke="${STEAM}" stroke-width="${8*s}" fill="none" stroke-linecap="round" opacity="${op*Math.sin(Math.PI*k)}"/>`;}return w;}
function mug(x,y,s,t,st){ // origin = centre of the mug's base; handle on the right
 return `<g transform="translate(${x} ${y}) scale(${s})">`+steam(0,-120,t,st===undefined?1:st,1)+
 `<path d="M54 -96 Q104 -96 104 -60 Q104 -24 54 -26" stroke="${PL}" stroke-width="30" fill="none" stroke-linecap="round"/><path d="M54 -96 Q104 -96 104 -60 Q104 -24 54 -26" stroke="${CORAL}" stroke-width="20" fill="none" stroke-linecap="round"/>
 <path d="M-62 -120 L62 -120 L56 -14 Q54 0 38 0 L-38 0 Q-54 0 -56 -14 Z" fill="${CORAL}" ${o}/>
 <ellipse cx="0" cy="-120" rx="62" ry="13" fill="#8A5A44" ${o} stroke-width="4"/>
 <path d="M0 -50 c-8 -14 -28 -6 -20 8 l20 18 l20 -18 c8 -14 -12 -22 -20 -8z" fill="#FFF0F4" stroke="${PL}" stroke-width="3"/></g>`;}
function shelf(x,y){return `<g transform="translate(${x} ${y})"><rect x="-130" y="0" width="260" height="24" rx="8" fill="${PEACH}" ${o}/>
 <path d="M-90 24 L-90 70 L-50 24 Z M90 24 L90 70 L50 24 Z" fill="#E9BE92" ${o} stroke-width="4"/></g>`;}
function dashArc(x1,y1,x2,y2,lift,k,col){ if(k<=0) return ''; const mx=(x1+x2)/2, my=Math.min(y1,y2)-lift;
 return `<path d="M${x1} ${y1} Q${mx} ${my} ${x2} ${y2}" stroke="${col||'#B23A62'}" stroke-width="7" fill="none" stroke-dasharray="4 16" stroke-linecap="round" pathLength="100" style="stroke-dasharray:${100*k} 100"/>`;}
function dashArc2(x1,y1,x2,y2,lift,k,col){ if(k<=0) return ''; const mx=(x1+x2)/2, my=Math.min(y1,y2)-lift; // dotted, drawn on via a mask
 return `<defs><mask id="dm${Math.round(x1)}"><path d="M${x1} ${y1} Q${mx} ${my} ${x2} ${y2}" stroke="#fff" stroke-width="14" fill="none" pathLength="100" stroke-dasharray="${100*k} 200"/></mask></defs>
 <path mask="url(#dm${Math.round(x1)})" d="M${x1} ${y1} Q${mx} ${my} ${x2} ${y2}" stroke="${col||'#B23A62'}" stroke-width="7" fill="none" stroke-dasharray="4 16" stroke-linecap="round"/>`;}
function qpt(x1,y1,x2,y2,lift,f){const mx=(x1+x2)/2, my=Math.min(y1,y2)-lift; const u=1-f;
 return [u*u*x1+2*u*f*mx+f*f*x2, u*u*y1+2*u*f*my+f*f*y2];}
function babyArm(x,y,len,ang,grab){ // little sleeve + hand reaching from (x,y)
 const ex=x+len*Math.cos(ang), ey=y+len*Math.sin(ang); const g=grab;
 let fing='';for(let i=0;i<4;i++){const a=ang-0.6+i*0.4, r=26+6*g; fing+=`<path d="M${ex} ${ey} L${ex+r*Math.cos(a)} ${ey+r*Math.sin(a)}" stroke="${PL}" stroke-width="18" stroke-linecap="round"/><path d="M${ex} ${ey} L${ex+r*Math.cos(a)} ${ey+r*Math.sin(a)}" stroke="${BSK}" stroke-width="11" stroke-linecap="round"/>`;}
 return `<path d="M${x} ${y} L${ex} ${ey}" stroke="${PL}" stroke-width="44" stroke-linecap="round"/><path d="M${x} ${y} L${ex} ${ey}" stroke="${PINK}" stroke-width="35" stroke-linecap="round"/>`+fing+`<circle cx="${ex}" cy="${ey}" r="22" fill="${BSK}" ${o} stroke-width="4"/>`;}
function clock(x,y,r,min){const a=-Math.PI/2+2*Math.PI*min/60; let tk='';
 for(let i=0;i<12;i++){const b=i*Math.PI/6;tk+=`<path d="M${x+(r-16)*Math.cos(b)} ${y+(r-16)*Math.sin(b)} L${x+(r-6)*Math.cos(b)} ${y+(r-6)*Math.sin(b)}" stroke="${PL}" stroke-width="${i%3?3:6}" stroke-linecap="round"/>`;}
 const wedge=min>0?`<path d="M${x} ${y} L${x} ${y-r+20} A${r-20} ${r-20} 0 ${min>30?1:0} 1 ${x+(r-20)*Math.cos(a)} ${y+(r-20)*Math.sin(a)} Z" fill="${BUT}" opacity=".85"/>`:'';
 return `<circle cx="${x}" cy="${y}" r="${r}" fill="${CREAM}" ${o}/>${wedge}${tk}<path d="M${x} ${y} L${x} ${y-r*0.45}" stroke="${PL}" stroke-width="9" stroke-linecap="round"/>
 <path d="M${x} ${y} L${x+(r-30)*Math.cos(a)} ${y+(r-30)*Math.sin(a)}" stroke="${CORAL}" stroke-width="7" stroke-linecap="round"/><circle cx="${x}" cy="${y}" r="9" fill="${PL}"/>`;}
function towel(){return `<rect x="-52" y="4" width="104" height="150" rx="10" fill="${CREAM}" ${o}/><path d="M-52 40 H52 M-52 54 H52 M-52 112 H52 M-52 126 H52" stroke="${CORAL}" stroke-width="6"/>`+peg(-34)+peg(34);}
G.towel=towel;
function bell(x,y,t,k){ if(k<=0) return ''; const r=8*Math.sin(t*26)*k;
 let w='';for(let i=1;i<3;i++){w+=`<path d="M${-70-16*i} ${-40-8*i} q${-14} 40 0 ${80+16*i}" stroke="#B23A62" stroke-width="6" fill="none" stroke-linecap="round" opacity="${k*(0.5+0.5*Math.sin(t*14))}"/><path d="M${70+16*i} ${-40-8*i} q14 40 0 ${80+16*i}" stroke="#B23A62" stroke-width="6" fill="none" stroke-linecap="round" opacity="${k*(0.5+0.5*Math.sin(t*14))}"/>`;}
 return `<g transform="translate(${x} ${y}) scale(${0.5+0.5*E(k)})">${w}<g transform="rotate(${r} 0 -70)"><path d="M-56 30 Q-56 -60 0 -64 Q56 -60 56 30 L70 46 L-70 46 Z" fill="${BUT}" ${o}/><circle cx="0" cy="58" r="14" fill="${CORAL}" ${o} stroke-width="4"/><circle cx="0" cy="-70" r="10" fill="${BUT}" ${o} stroke-width="4"/></g></g>`;}
function wipes(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s||1})"><rect x="-90" y="-50" width="180" height="100" rx="26" fill="${BLUE}" ${o}/><rect x="-40" y="-40" width="80" height="34" rx="14" fill="${CREAM}" ${o} stroke-width="4"/><path d="M-20 -24 q20 -26 40 0" fill="#FFFFFF" stroke="${PL}" stroke-width="3.5"/><text x="0" y="34" font-family="Poppins" font-weight="600" font-size="24" text-anchor="middle" fill="${INK}">wipes</text></g>`;}
function wiggle(t,x,y,op){let s='';for(let i=0;i<2;i++){const j=5*Math.sin(t*24+i*2);s+=`<path d="M${x+j} ${y-60+i*120} q-16 -10 -32 0 q-16 10 -32 0" stroke="${CORAL}" stroke-width="6" fill="none" stroke-linecap="round" opacity="${op}"/>`;}return s;}
// ---------- Reel 1: hot drink
function bundleF(x,y,rot,s){ // swaddled baby WITH a face: sleepy eyes, smile, rosy cheeks, knit hat; origin = swaddle centre, head up
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
 <path d="M-66 -20 Q-86 70 -40 124 Q0 142 40 124 Q86 70 66 -20 Q40 -50 0 -50 Q-40 -50 -66 -20Z" fill="${PINK}" ${o}/>
 <path d="M-56 10 Q0 50 58 0 M-46 64 Q0 92 52 56" stroke="${PL}" stroke-width="3.5" fill="none" opacity=".55"/>
 <circle cx="0" cy="-62" r="52" fill="${BSK}" ${o}/>
 <path d="M-50 -76 Q-46 -128 0 -128 Q46 -128 50 -76 Q24 -90 0 -90 Q-24 -90 -50 -76Z" fill="${SAGE}" ${o}/><circle cx="0" cy="-134" r="12" fill="${CREAM}" ${o} stroke-width="4"/>
 <path d="M-26 -58 q9 8 18 0 M8 -58 q9 8 18 0" stroke="#5A2E22" stroke-width="5" fill="none" stroke-linecap="round"/>
 <path d="M-9 -34 q9 8 18 0" stroke="#9A4E2A" stroke-width="5" fill="none" stroke-linecap="round"/>
 <circle cx="-32" cy="-40" r="9" fill="#FF9EA8" opacity=".7"/><circle cx="32" cy="-40" r="9" fill="#FF9EA8" opacity=".7"/></g>`;}
function adultHold(t,k){ // parent (drawn, smiling) holding the swaddled baby across the chest; k>0: second hand comes to the baby
 const sw=3*Math.sin(t*2.2);
 return `<g transform="translate(-170 -10) scale(.8) rotate(${sw} 40 300)">`+adultShoulder()+bundleF(0,180,-58,1.0)+forearm(-30,250,-6,0.85)+
  (k>0?palm(130+120*(1-k),170,-20,0.6):'')+`</g>`;}
const MX0=70, MY0=150, SX=300, SY=-40;     // mug start (in the parent's other hand, right next to baby) and shelf top
SC.mug=[
 (lt,D,t)=>{ // parent holding baby AND a steaming mug -> dotted line to the shelf, mug goes up; second hand to baby, hearts
   const go=EIO(seg(lt,0.55,1.45)), [mx,my]=qpt(MX0,MY0,SX,SY,90,go), away=E(seg(lt,1.55,2.0)), k=E(seg(lt,1.9,2.4));
   let s=shelf(SX,SY)+adultHold(t,k);
   s+=dashArc2(MX0+10,MY0-150,SX,SY-150,90,seg(lt,0.15,0.6));
   s+=mug(mx,my,0.95,t,1);
   s+=hand(mx+78+520*away,my-62,0,0.62,1);
   if(lt>1.45) s+=popBurst(SX,SY-60,seg(lt,1.45,1.9));
   if(lt<0.55) s+=label(330,225,'baby + hot tea…',-4,60);
   else if(lt<2.0) s+=label(300,170,'up, out of reach',-4,60);
   else s+=label(300,170,'now hold baby ♡',-4,60);
   if(lt>2.4){for(let i=0;i<3;i++){const k2=seg(lt,2.4+i*0.15,3.4+i*0.15);s+=heartP(-140+i*70,-120-80*k2,1.2,Math.sin(Math.PI*k2));}}
   return stage(s,0,0.9,40);},
 (lt,D,t)=>{ // little arm reaches for a mug at the table edge; the mug flies up to the shelf
   const reach=EIO(seg(lt,0.0,0.7)), grab=0.5+0.5*Math.sin(t*12), fly=EIO(seg(lt,1.0,1.7)), back=E(seg(lt,1.6,2.1));
   let s=shelf(SX,SY+50)+table(110,232)+babyBack(-170,190,4,0.82);
   s+=babyArm(-116,165,40+120*reach*(1-0.6*back),-0.12,grab);
   const [mx,my]=qpt(100,232,SX,SY+50,120,fly); s+=mug(mx,my,0.85,t,1);
   if(lt<1.0) s+=label(-150,-110,'grab!',-8,70); else if(lt>1.7) s+=label(-60,-110,'out of reach ✓',-4,58);
   if(lt>1.7) s+=popBurst(SX,SY-10,seg(lt,1.7,2.1));
   return stage(s,-10,1.0,20);},
 (lt,D,t)=>{ // a clock sweeps 15 minutes while the mug keeps steaming
   const m=15*EIO(seg(lt,0.15,2.0));
   let s=mug(-150,240,1.35,t,1)+clock(200,80,140,m);
   s+=`<text x="200" y="${-90}" font-family="Poppins" font-weight="600" font-size="46" text-anchor="middle" fill="${INK}">${Math.round(m)} min</text>`;
   if(lt>2.0) s+=label(-150,-90,'still hot!',-6,64);
   return stage(s,0,0.95,40);},
 (lt,D,t)=>{ // Do this: mug up on the shelf, parent holds baby with both hands, hearts
   let s=shelf(SX,SY)+mug(SX,SY,0.95,t,1)+adultHold(t,1)+hearts(t,-60,-120);
   return stage(s,0,0.78,120);},
];
SC.mug.special=(beat,lt)=>(y0,sag)=>{ // Do this: a striped tea towel flies up and is pegged on the line
  if(beat<3) return ''; const f=EIO(seg(lt,0.1,0.9)); const tx=930, ty=lineY(930,y0,sag);
  const sx=480, sy=1150; const X=sx+(tx-sx)*f, Y=sy+(ty-sy)*f-160*Math.sin(Math.PI*f);
  return `<g transform="translate(${X} ${Y}) rotate(${-20*(1-f)+4*Math.sin(T*2)}) scale(.88)">${towel()}</g>`;};
// ---------- Reel 2: changing table
function babyW(t,k){ // the top-view baby on the mat; k = wriggle amount
 return `<g transform="rotate(${3*k*Math.sin(t*9)} -80 0) translate(${8*k*Math.sin(t*7)} 0)">${babyTop(1,t,0)}</g>`;}
const PX=-30, PY=-10;   // where the palm rests on the tummy (stage coords before scale)
SC.change=[
 (lt,D,t)=>{ // wriggling baby, wipes out of reach -> a palm lands on the tummy and stays; the other hand fetches the wipes
   const land=E(seg(lt,0.15,0.6)), wr=1-seg(lt,0.5,0.8);
   const fetch=EIO(seg(lt,0.75,1.25)), ret=EIO(seg(lt,1.25,1.8));
   const wx=560-280*ret, wy=-150+40*ret;
   let s=mat()+babyW(t,wr)+wiggle(t,-470,0,wr);
   s+=palm(PX+420*(1-land),PY-30,0,0.85);
   s+=wipes(wx,wy,1.0);
   const hx=wx+60+420*(1-fetch)+(lt>1.8?900*E(seg(lt,1.8,2.3)):0); s+=hand(hx,wy+10,0,0.7,fetch>0.95?1:0);
   if(lt<0.6) s+=label(-120,-290,'wriggle, wriggle…',-4,76);
   else if(lt<1.8) s+=label(-120,-290,'one hand stays on',-4,76);
   else s+=label(-120,-290,'one hand stays on ✓',-4,76);
   if(lt>2.0) s+=check(PX-30,-230,seg(lt,2.0,2.5));
   return stage(s,40,0.7,100);},
 (lt,D,t)=>{ // everything ready first: diaper, wipes, clean clothes pop in with ticks
   let s=mat()+babyW(t,0)+palm(PX,PY-30,0,0.85);
   const it=[[400,-230,'diaper'],[400,-60,'wipes'],[400,110,'onesie']];
   it.forEach(([x,y,k],j)=>{const a=E(seg(lt,0.1+j*0.35,0.45+j*0.35)); if(a<=0) return; let g='';
     if(k=='diaper') g=`<g transform="translate(0 -60) scale(.9)">${G.diaper()}</g>`.replace(/<rect x="-?\d+" y="-14"[^>]*\/>/g,'');
     if(k=='wipes') g=wipes(0,0,0.8);
     if(k=='onesie') g=`<g transform="translate(0 -90) scale(.85)">${G.onesie()}</g>`.replace(/<rect x="-?\d+" y="-14"[^>]*\/>/g,'');
     s+=`<g transform="translate(${x} ${y}) scale(${0.5+0.5*a})" opacity="${a}">${g}</g>`+check(x+120,y-30,seg(lt,0.3+j*0.35,0.7+j*0.35));});
   if(lt>1.4) s+=label(-120,-290,'all within reach ✓',-4,76);
   return stage(s,40,0.7,100);},
 (lt,D,t)=>{ // doorbell rings -> baby is lifted off the mat and carried along
   const ring=seg(lt,0.0,0.25)*(1-seg(lt,1.3,1.6)), up=EIO(seg(lt,0.35,1.0)), go=EIO(seg(lt,1.1,2.3));
   const sh=Math.max(up,0);
   let s=mat()+`<ellipse cx="-90" cy="0" rx="300" ry="120" fill="${PL}" opacity="${0.16*sh*(1-go)}"/>`;
   const sc=1+0.14*up, X=-80+60*up+540*go, Y=-50*up+50*go;
   s+=`<g transform="translate(${X} ${Y}) scale(${sc*(1-0.35*go)}) rotate(${-12*go}) translate(80 0)">`+babyW(t,0)
     +palm(-60,150,90,0.7*Math.min(1,up*3+0.01)).replace('<g ','<g opacity="'+Math.min(1,up*3)+'" ')
     +palm(-60,-150,-90,0.7).replace('<g ','<g opacity="'+Math.min(1,up*3)+'" ')+`</g>`;
   for(let i=0;i<3;i++){const k=seg(lt,0.6+i*0.1,1.1+i*0.1); if(k>0&&k<1) s+=`<path d="M${-260+i*120} ${150-60*k} v-50" stroke="#B23A62" stroke-width="7" stroke-linecap="round" opacity="${1-k}"/>`;}
   s+=bell(440,-190,t,ring);
   if(lt<0.6) s+=label(-120,-290,'ding dong!',-6,76);
   else s+=label(-120,-290,'baby comes too ✓',-4,76);
   return stage(s,40,0.7,100);},
 (lt,D,t)=>{ // Do this: palm on the tummy, check, hearts
   let s=mat()+babyW(t,0)+palm(PX,PY-30,0,0.85)+check(PX-30,-230,seg(lt,0.2,0.7))+hearts(t,-120,-140);
   return stage(s,40,0.7,100);},
];
SC.change.special=(beat,lt)=>(y0,sag)=>{ // Do this: a tiny diaper flies up and is pegged on the line
  if(beat<3) return ''; const f=EIO(seg(lt,0.1,0.9)); const tx=930, ty=lineY(930,y0,sag);
  const sx=480, sy=1150; const X=sx+(tx-sx)*f, Y=sy+(ty-sy)*f-160*Math.sin(Math.PI*f);
  return `<g transform="translate(${X} ${Y}) rotate(${-20*(1-f)+4*Math.sin(T*2)}) scale(.88)">${G.diaper()}</g>`;};
// ---------- the send line (Reel 1 only): lands on the last beat, stays to the end
const _draw0=draw;
draw=function(t){ _draw0(t); const el=document.getElementById('send'); if(!el) return; const S=SPEC, n=S.durs.length;
  const lt=t-S.starts[n-1]; const p=(S.cover||lt<0)?0:E(seg(lt,0.45,0.85)); el.style.opacity=p; el.style.transform=`translateY(${24*(1-p)}px) rotate(-2deg)`;};
"""

BASE_HTML = RS.html


def html(spec, cover=None):
    h = BASE_HTML(spec, cover)
    h = (h.replace("top:455px;font-size:68px", "top:455px;font-size:62px")
          .replace("top:1585px;text-align:center;opacity:0", "top:1330px;text-align:center;opacity:0;z-index:6")
          .replace("top:1500px;text-align:center;opacity:0", f"top:{spec.get('follow_y', 1395)}px;text-align:center;opacity:0;z-index:7")
          .replace("padding:12px 30px;border-radius:99px;background:#3A1F3D;color:#FFF8EE;font:600 32px Poppins",
                   "max-width:760px;padding:16px 36px;border-radius:40px;background:#3A1F3D;color:#FFF8EE;font:600 36px/1.25 Poppins"))
    h = h.replace("left:46px;top:1470px;width:120px", "left:46px;top:1430px;width:120px")
    if spec.get("send"):
        send = (f'<div id="send" style="position:absolute;left:80px;width:920px;top:{spec.get("send_y", 850)}px;text-align:center;opacity:0;z-index:6">'
                f'<span style="display:inline-block;padding:10px 30px 14px;background:#FFE08A;border-radius:14px;box-shadow:0 6px 0 rgba(107,59,90,.18);'
                f'font-family:\'Caveat Brush\';font-size:70px;line-height:1.05;color:#B23A62">{spec["send"]}</span></div>')
        h = h.replace('<svg id="art"', send + '<svg id="art"', 1)
    return h


SPEC_MUG = dict(
    out="lf-reel-1029am-hot-drink", outdir=OUT, music=LIB / "v4/lf-x-giggle-pop.mp3", scene="mug", follow=FOLLOW, send=SEND,
    sky=("dawn", "morning"), garments=["onesie", "sock", "hat", "none"],
    durs=[8 * BG, 6 * BG, 6 * BG, 9 * BG], extra_pops=[], cover_beat=0, cover_lt=2.0,
    beats=[
        dict(kick="holding baby with a hot drink?", head="Put the mug / *down first.*", sub="Out of reach, before you hold baby.", fs=150, sy=860, ss=48, chip="NHS · Baby and toddler safety"),
        dict(kick="because", head="Babies / *grab mugs.*", sub="And their skin burns more easily than ours.", fs=150, sy=860, ss=46, chip="NHS · Baby and toddler safety"),
        dict(kick="and", head="Still hot after / *15 minutes.*", sub="A hot drink can still scald.", fs=150, sy=860, ss=48, chip="NHS · Baby and toddler safety"),
        dict(kick="Do this:", head="Mug down. / *Then pick baby up.*", fs=130, chip="NHS · Baby and toddler safety"),
    ])

SPEC_CHANGE = dict(
    out="lf-reel-1031am-hand-on-baby", outdir=OUT, music=LIB / "v4/lf-x-tiny-parade.mp3", scene="change", follow=FOLLOW,
    sky=("dawn", "morning"), garments=["sock", "onesie", "hat", "none"],
    durs=[6 * BP, 5 * BP, DROP_BP - 11 * BP, 14.4 - DROP_BP], extra_pops=[], cover_beat=0, cover_lt=2.0,
    beats=[
        dict(kick="reaching for the wipes mid-change?", head="Keep one hand / *on baby.*", sub="They can roll off in a second.", fs=150, sy=860, ss=48, chip="NHS · Health Canada"),
        dict(kick="before you start", head="Grab everything / *first.*", sub="Diaper, wipes, clean clothes.", fs=150, sy=860, ss=48, chip="Health Canada · Change tables"),
        dict(kick="doorbell mid-change?", head="Take baby / *with you.*", sub="Never leave them on the table.", fs=150, sy=860, ss=48, chip="Health Canada · NHS"),
        dict(kick="Do this:", head="One hand on baby, / *every change.*", sub="Or change them on a mat on the floor.", fs=130, sy=860, ss=46, chip="NHS · Health Canada"),
    ])

# =====================================================================================================================
# Covers (dedicated, 2x)
# =====================================================================================================================
BLOBS = S27.BLOBS


def cover_mug_html():
    """Follow the line (style #9, quiet): mug -> dotted berry line -> high shelf ('1'); hands -> coral line -> baby ('2')."""
    art = r"""
    let s='';
    s+=`<g transform="translate(240 1250)">${mug(0,0,1.25,0.6,1)}</g>`;
    s+=`<g transform="translate(820 980)">${shelf(0,0)}${mug(0,0,0.9,1.4,0.45)}</g>`;
    s+=`<path d="M300 1060 C 360 870 560 820 740 860" stroke="#D9497A" stroke-width="10" fill="none" stroke-dasharray="2 22" stroke-linecap="round"/>`;
    s+=`<path d="M722 846 l24 14 l-22 18" stroke="#D9497A" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;
    s+=`<circle cx="430" cy="900" r="34" fill="#D9497A"/><text x="430" y="914" font-family="Poppins" font-weight="700" font-size="38" text-anchor="middle" fill="#FFF8EE">1</text>`;
    s+=label(600,1118,'mug up, out of reach',-5,54);
    s+=`<g transform="translate(760 1310)">${bundleF(0,-30,0,0.85)}${cradle(0,40,0,0.85)}</g>`;
    s+=`<path d="M880 1030 C 960 1080 950 1150 870 1200" stroke="#F27C6B" stroke-width="10" fill="none" stroke-dasharray="2 22" stroke-linecap="round"/>`;
    s+=`<circle cx="950" cy="1110" r="34" fill="#F27C6B"/><text x="950" y="1124" font-family="Poppins" font-weight="700" font-size="38" text-anchor="middle" fill="#FFF8EE">2</text>`;
    s+=label(400,1395,'then pick baby up ♡',-4,56);
    document.getElementById('art').innerHTML=s;"""
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4,#FFEFD8)"></div>'
            + BLOBS.format(a="#FFD6E3", b="#FFE27E", c="#CFE3F6") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:318px;font-size:68px;color:{KICK}">holding baby with a hot drink?</div>'
            + K.dual("Mug down. / *Then baby.*", F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:405px;white-space:nowrap;font-size:170px;color:{INK}")
            + '<svg id="art" style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10)
            + f"<script>{RS.JS}\n{art}</script>")
    return RS.page(W, H, body)


def cover_change_html():
    """Littlefold soft countdown (style #2 'lf-count', loud): a giant numeral 1 + 'hand on baby', a drawn palm on the tummy."""
    art = r"""
    document.getElementById('art').innerHTML=`<g transform="translate(560 1190) scale(.6)">${mat()}${babyTop(1,0,0)}${palm(70,-40,0,0.85)}</g>`+check(820,1020,1)+label(720,1400,'every single change',-4,58);"""
    num = ('<div style="position:absolute;left:40px;top:380px;width:480px;height:720px;display:flex;align-items:center;justify-content:center;z-index:2">'
           '<div style="position:absolute;width:440px;height:440px;border-radius:50%;background:#FFE27E;opacity:.85;top:150px;left:20px"></div>'
           '<div class="lora" style="position:relative;font-weight:700;font-size:720px;line-height:1;color:#D9497A;'
           'text-shadow:10px 10px 0 #FFC9D6">1</div></div>')
    words = (f'<div class="lora" style="position:absolute;left:470px;top:470px;width:560px;font-weight:700;font-size:150px;line-height:1.0;color:{INK};z-index:3">'
             'hand<br>on<br><span style="font-style:italic;color:#D9497A">baby.</span></div>')
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4,#FFF1DC)"></div>'
            + BLOBS.format(a="#CFE3F6", b="#FFD6E3", c="#FFE27E") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:318px;font-size:72px;color:{KICK};z-index:3">changing a diaper?</div>'
            + num + words
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:2" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10)
            + f"<script>{RS.JS}\n{art}</script>")
    return RS.page(W, H, body)


def use(key):
    RS.JS = BASE_JS + JS27 + JS
    RS.html = html
    return {"mug": (SPEC_MUG, cover_mug_html), "change": (SPEC_CHANGE, cover_change_html)}[key]


BASE_JS = RS.JS

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
        RS.encode(fdir, total, s["music"], pops, out)
        print(out, round(total, 2), flush=True)

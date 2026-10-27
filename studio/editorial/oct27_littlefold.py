#!/usr/bin/env python3
"""Oct 27 (Social studio, Littlefold maker): two Reels + dedicated covers.

1. lf-reel-1028am-cord-stump (Wed Oct 28 08:00, trial auto)
   FORMAT: the winning illustrated "physical rule, shown being done" in the sunshine washing-line world
   (studio/recovery-oct22c/littlefold/reel_story.py imported, not edited; approach copied from oct24_lf_a.py).
   New drawn vignette SC.stump: a baby on a changing mat seen from above (head left, sleeping face, knit hat);
   the diaper waist is up over the cord stump with little rub marks; an adult hand folds the diaper top DOWN below
   the stump by ~1.4 s; a lens close-up shows air drying the stump and an 'alcohol' bottle getting a 'no' ring;
   the stump shrinks over 'week 1, 2, 3' and drops off by itself; three warm call-your-doctor signs pop in by a
   phone; Do this: folded diaper, check, hearts, and a tiny diaper is pegged on the washing line.
   COVER: sticky-note list (style #13, quiet), NOT a washing-line frame (neighbours: Tue 7 pm swaddle washing-line,
   Wed 5 pm 3 am Club No. 2 Look B pills).

2. lf-reel-1030-rice-grain (Fri Oct 30 19:00, no trial)
   STYLE: calm text Reel (style #15) cut with the motion rules: sunny sky + drifting clouds and blobs, static serif
   text per beat, a soft butter iris wipe on each cut, ONE drawn object doing the meaning (a toothbrush; the tube
   squeezes a rice-grain smear, it grows to a pea, a rinse cup gets a 'no' ring, a little tooth gets brushed at
   bedtime). No washing line, no hills, no arch card. Toddler age band.
   COVER: awards / rosettes (style #10, quiet) (neighbours: Thu 7 pm tummy arch card, Fri 5 pm 3 am Club No. 3 Look B).

Facts (checked Oct 27 2026):
  AAP HealthyChildren.org 'Umbilical Cord Care in Newborns' (updated 7/6/2025): keep the stump clean and dry;
    no need for alcohol; keep the diaper folded below the cord so urine doesn't soak it; should fall off by 3 weeks;
    call for foul-smelling yellowish discharge, red skin around the base, crying when touched; active bleeding: call immediately.
  Sheffield Children's NHS FT 'Umbilical cord care': keep it clean and dry, keep it out of the nappy area, try not to touch it.
  AAP HealthyChildren.org 'Toothbrushing Tips for Young Children' (updated 5/14/2025): from the first tooth; under 3 a smear
    the size of a grain of rice; 3 to 6 pea-sized; twice a day; spit, don't rinse.
  NHS Best Start in Life 'Baby and toddler tooth care': smear (size of a grain of rice) up to 3; pea-sized 3 to 6; at least
    1,000 ppm fluoride; brush last thing at night and one other time; spit out, don't rinse (washes the fluoride away).

    python3 studio/editorial/oct27_littlefold.py stump|teeth [--still=0.2,1.5,...] [--cover-only]
"""
import json
import os
import sys
import tempfile
from pathlib import Path
sys.dont_write_bytecode = True
os.environ.setdefault("LF_SCR", "/tmp/claude-0/oct27-littlefold")
sys.path.insert(0, "/home/claude/steadfold-autopost/studio/recovery-oct22c/littlefold")
import reel_story as RS  # noqa: E402

K, F, INK, KICK, B = RS.K, RS.F, RS.INK, RS.KICK, RS.B
W, H = RS.W, RS.H
OUT = RS.REPO / "media" / "studio-oct27" / "littlefold"
LIB = RS.LIB
FOLLOW = "Follow for one calm thing a night, from bump to toddler."
BS = 60 / 120.2   # lf-c-sunny-morning-el (the burp Reel's track)
BB = 60 / 112.3   # lf-x-sunny-bounce (v4), drop 8.266 s
DROP_BB = 8.266
BASE_JS = RS.JS
BASE_HTML = RS.html

# =====================================================================================================================
# Reel 1: cord stump (washing-line world)
# =====================================================================================================================
JS_STUMP = r"""
// ===================== Oct 27: cord stump =====================
const BSK='#FFDCC4';
G.diaper=()=>`<path d="M-50 4 L50 4 Q58 70 0 96 Q-58 70 -50 4Z" fill="${CREAM}" ${o}/><rect x="-56" y="0" width="26" height="18" rx="6" fill="${BLUE}" ${o} stroke-width="3"/><rect x="30" y="0" width="26" height="18" rx="6" fill="${BLUE}" ${o} stroke-width="3"/>`+peg(-30)+peg(30);
function stumpSVG(x,y,k){ // shrinking, darkening stump; k=1 fresh .. 0 gone (navel)
 let s=`<path d="M${x-12} ${y+4} q12 12 24 0" stroke="${SKD}" stroke-width="4" fill="none" stroke-linecap="round"/>`;
 if(k<=0.02) return s;
 const sc=0.45+0.55*k, col=k>0.5?'#D2AE78':'#A9875A';
 return s+`<g transform="translate(${x} ${y}) scale(${sc})"><path d="M-14 -4 Q-24 -30 -4 -38 Q20 -42 22 -18 Q24 4 8 10 Q-10 14 -14 -4Z" fill="${col}" ${o} stroke-width="4"/><path d="M-4 -26 q9 -3 13 6" stroke="#7E5E36" stroke-width="3" fill="none" stroke-linecap="round"/></g>`;}
function diaperFlap(k){ // the waist flap folds about x=30: covers [-40,30] -> folded onto [30,100]
 const fx=30, xe=fx-70*Math.cos(Math.PI*cl(k,0,1)), inner=k>0.5, b=xe<fx?-8:8;
 return `<path d="M${fx} -120 L${xe} -114 Q${xe+b} 0 ${xe} 114 L${fx} 120 Z" fill="${inner?'#E3EEF8':CREAM}" ${o}/>`+
  (inner?`<path d="M${xe-6} -100 Q${xe-2} 0 ${xe-6} 100" stroke="#FFFFFF" stroke-width="8" fill="none" stroke-linecap="round" opacity=".9"/>`:
         `<path d="M${xe+10} -100 Q${xe+16} 0 ${xe+10} 100" stroke="${BLUE}" stroke-width="9" fill="none" stroke-linecap="round" opacity=".85"/>`);}
function babyTop(fold,t,stk){ // baby on their back seen from above, head LEFT, sleeping face + knit hat; origin = belly
 const br=1+0.012*Math.sin(t*2.4); let s='';
 const arm=sg=>`<path d="M-200 ${92*sg} Q-252 ${168*sg} -312 ${150*sg}" stroke="${PL}" stroke-width="44" fill="none" stroke-linecap="round"/><path d="M-200 ${92*sg} Q-252 ${168*sg} -312 ${150*sg}" stroke="${BSK}" stroke-width="35" fill="none" stroke-linecap="round"/><circle cx="-322" cy="${148*sg}" r="22" fill="${BSK}" ${o} stroke-width="4"/>`;
 const leg=sg=>`<path d="M168 ${72*sg} Q262 ${150*sg} 226 ${212*sg}" stroke="${PL}" stroke-width="58" fill="none" stroke-linecap="round"/><path d="M168 ${72*sg} Q262 ${150*sg} 226 ${212*sg}" stroke="${BSK}" stroke-width="49" fill="none" stroke-linecap="round"/><ellipse cx="204" cy="${232*sg}" rx="36" ry="25" fill="${BLUE}" ${o} stroke-width="4"/>`;
 s+=arm(-1)+arm(1)+leg(-1)+leg(1);
 s+=`<g transform="scale(${br} 1)"><rect x="-236" y="-116" width="400" height="232" rx="100" fill="${BSK}" ${o}/></g>`;
 s+=`<path d="M-252 -114 L-124 -114 Q-108 0 -124 114 L-252 114 Q-264 0 -252 -114Z" fill="${PINK}" ${o}/><path d="M-132 -106 Q-117 0 -132 106" stroke="#FFF0F4" stroke-width="10" fill="none" stroke-linecap="round"/>`;
 s+=stumpSVG(-20,0,stk===undefined?1:stk);
 s+=`<path d="M30 -120 L168 -110 Q252 -70 252 0 Q252 70 168 110 L30 120 Z" fill="${CREAM}" ${o}/>`;
 s+=`<rect x="40" y="-136" width="56" height="34" rx="10" fill="${BLUE}" ${o} stroke-width="4"/><rect x="40" y="102" width="56" height="34" rx="10" fill="${BLUE}" ${o} stroke-width="4"/>`;
 s+=diaperFlap(fold);
 // head (face toward the viewer, top of the head LEFT)
 s+=`<ellipse cx="-318" cy="-84" rx="16" ry="20" fill="${BSK}" ${o} stroke-width="4"/><ellipse cx="-318" cy="84" rx="16" ry="20" fill="${BSK}" ${o} stroke-width="4"/>`;
 s+=`<circle cx="-322" cy="0" r="86" fill="${BSK}" ${o}/>`;
 s+=`<path d="M-318 -84 Q-436 -92 -432 0 Q-436 92 -318 84 Q-356 0 -318 -84Z" fill="${SAGE}" ${o}/><path d="M-336 -76 Q-372 0 -336 76" stroke="#A8CA9A" stroke-width="12" fill="none" stroke-linecap="round"/><circle cx="-444" cy="0" r="20" fill="${CREAM}" ${o} stroke-width="4"/>`;
 s+=`<path d="M-302 -40 q-10 12 0 24 M-302 16 q-10 12 0 24" stroke="#5A2E22" stroke-width="5" fill="none" stroke-linecap="round"/>`;
 s+=`<path d="M-268 -10 q10 10 0 20" stroke="#9A4E2A" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="-282" cy="-46" r="10" fill="#FF9EA8" opacity=".6"/><circle cx="-282" cy="46" r="10" fill="#FF9EA8" opacity=".6"/>`;
 return s;}
function mat(){let st='';for(let i=0;i<6;i++)st+=`<path d="M${-420+i*140} -244 V244" stroke="#FFE4CF" stroke-width="30" opacity=".7"/>`;
 return `<rect x="-470" y="-260" width="760" height="520" rx="60" fill="${PEACH}" ${o}/>${st}<rect x="-470" y="-260" width="760" height="520" rx="60" fill="none" ${o}/>`;}
function rubs(t,op){let s='';for(let i=0;i<3;i++){const y=-50+i*50, j=5*Math.sin(t*22+i*2);s+=`<path d="M${-52+j} ${y-12} l-14 12 l14 12" stroke="${CORAL}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="${op}"/>`;}return s;}
function lens(inner,r){ // round magnifier close-up, with handle
 return `<defs><clipPath id="lz"><circle cx="0" cy="0" r="${r}"/></clipPath></defs><path d="M${r*0.72} ${r*0.72} L${r*1.18} ${r*1.18}" stroke="${PL}" stroke-width="40" stroke-linecap="round"/><path d="M${r*0.72} ${r*0.72} L${r*1.18} ${r*1.18}" stroke="${BUT}" stroke-width="28" stroke-linecap="round"/>
 <circle r="${r+8}" fill="${CREAM}" ${o}/><g clip-path="url(#lz)"><rect x="${-r}" y="${-r}" width="${2*r}" height="${2*r}" fill="${PEACH}"/>${inner}</g><circle r="${r}" fill="none" stroke="${PL}" stroke-width="7"/><circle r="${r+8}" fill="none" ${o}/>`;}
function breeze(t,op){let s='';for(let i=0;i<3;i++){const k=(t*0.55+i/3)%1, y=-120+i*110;s+=`<path d="M${-260+420*k} ${y} q40 -26 80 0 q30 20 56 -6" stroke="#FFFFFF" stroke-width="9" fill="none" stroke-linecap="round" opacity="${op*Math.sin(Math.PI*k)}"/>`;}return s;}
function alcohol(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-40" y="-70" width="80" height="140" rx="16" fill="#E3EEF8" ${o}/><rect x="-22" y="-100" width="44" height="32" rx="6" fill="${PEACH}" ${o}/><rect x="-36" y="-20" width="72" height="44" rx="6" fill="${CREAM}" stroke="${PL}" stroke-width="3"/><text x="0" y="9" font-family="Poppins" font-weight="600" font-size="15" text-anchor="middle" fill="${INK}">alcohol</text></g>`;}
function phone(x,y,t,k){const ring=0.5+0.5*Math.sin(t*14);return `<g transform="translate(${x} ${y}) rotate(${6*Math.sin(t*14)*k})"><rect x="-70" y="-120" width="140" height="240" rx="26" fill="${PL}"/><rect x="-58" y="-104" width="116" height="200" rx="16" fill="${CREAM}"/>
 <circle cx="0" cy="-10" r="34" fill="${SAGE}" ${o} stroke-width="4"/><path d="M-14 -22 q-4 14 8 24 q12 10 22 4" stroke="${PL}" stroke-width="7" fill="none" stroke-linecap="round"/>
 ${[1,2].map(i=>`<path d="M${-90-18*i} ${-40-10*i} q-${16+6*i} 40 0 ${80+20*i}" stroke="#B23A62" stroke-width="6" fill="none" stroke-linecap="round" opacity="${k*ring}"/><path d="M${90+18*i} ${-40-10*i} q${16+6*i} 40 0 ${80+20*i}" stroke="#B23A62" stroke-width="6" fill="none" stroke-linecap="round" opacity="${k*ring}"/>`).join('')}</g>`;}
function sign(x,y,k,kind){if(k<=0)return '';const s=0.4+0.6*E(k);let g='';
 if(kind==0) g=`<circle r="40" fill="${BSK}" ${o} stroke-width="4"/><circle r="26" fill="none" stroke="#F28B8B" stroke-width="10" opacity=".85"/>`+stumpSVG(0,4,0.8);
 if(kind==1) g=`<circle r="40" fill="${CREAM}" ${o} stroke-width="4"/><path d="M0 -24 q-20 26 -12 36 q12 12 24 0 q8 -10 -12 -36z" fill="#F4D35E" stroke="${PL}" stroke-width="3.5"/>`;
 if(kind==2) g=`<circle r="40" fill="${CREAM}" ${o} stroke-width="4"/>${[-14,0,14].map(d=>`<path d="M${d} 22 q-10 -12 0 -22 q10 -12 0 -24" stroke="#9CC490" stroke-width="5" fill="none" stroke-linecap="round"/>`).join('')}`;
 return `<g transform="translate(${x} ${y}) scale(${1.25*s})" opacity="${seg(k,0,0.3)}">${g}</g>`;}
const SST=(s)=>stage(s,40,0.92,120);
SC.stump=[
 (lt,D,t)=>{ // diaper over the stump with rub marks -> a hand folds the waist DOWN below the stump
   const fold=EIO(seg(lt,0.5,1.35)), reach=E(seg(lt,0.05,0.5)), away=E(seg(lt,1.45,1.9));
   let s=mat()+babyTop(fold,t,1)+rubs(t,1-seg(lt,0.4,0.6));
   const xe=30-70*Math.cos(Math.PI*fold);
   s+=hand(xe+4+330*(1-reach)+330*away,-70,0,0.78,reach>0.95&&away<0.05?1:0);
   if(lt<0.55) s+=label(-60,300,'rub, rub…',-4,60); else if(lt<1.4) s+=label(-60,300,'fold it down',-4,60);
   else {s+=label(-60,300,'below the stump ✓',-4,60);}
   if(lt>1.45) s+=popBurstS(-20,-10,seg(lt,1.45,1.9));
   return SST(s);},
 (lt,D,t)=>{ // lens close-up: air dries it; an alcohol bottle gets a 'no' ring
   const a=E(seg(lt,0,0.35)); let inner=`<g transform="scale(2.4) translate(20 0)">${babyTop(1,t,1)}</g>`+breeze(t,1);
   inner+=sparkle(-60,-150,0.8+0.3*Math.sin(t*5),0.9)+sparkle(110,130,0.7+0.3*Math.sin(t*4+1),0.9);
   let s=`<g transform="translate(-90 0) scale(${0.7+0.3*a})">${lens(inner,230)}</g>`;
   s+=label(-90,300,'let the air dry it',-4,56);
   const b=E(seg(lt,1.0,1.4)); if(b>0){s+=alcohol(240+200*(1-b),20,1.35)+noRing(240,20,120,seg(lt,1.3,2.1)); if(lt>1.7) s+=label(250,-150,'not needed',-5,52);}
   return SST(s);},
 (lt,D,t)=>{ // the stump shrinks over 3 weeks, then drops off by itself
   const k=1-EIO(seg(lt,0.15,1.9)); const off=seg(lt,1.9,2.4);
   let inner=`<g transform="scale(2.4) translate(20 0)">${babyTop(1,t,off>0?0:Math.max(k,0.08))}</g>`;
   if(off>0){ inner+=`<g transform="translate(${-48+90*E(off)} ${-10+300*off*off}) rotate(${200*off})">${stumpSVG(0,0,0.25).replace(/^<path[^>]*\/>/,'')}</g>`; inner+=sparkle(-48,-80,0.9,seg(lt,2.1,2.4))+heartP(-40,-170,1.4,seg(lt,2.2,2.6));}
   let s=`<g transform="translate(-90 0)">${lens(inner,230)}</g>`;
   const wk=Math.min(3,1+Math.floor(3*seg(lt,0.15,1.95)));
   for(let i=0;i<3;i++){const on=wk>i; s+=`<circle cx="${190+i*80}" cy="-150" r="30" fill="${on?BUT:CREAM}" ${o} stroke-width="4"/><text x="${190+i*80}" y="-139" font-family="Poppins" font-weight="600" font-size="30" text-anchor="middle" fill="${INK}">${i+1}</text>`;}
   s+=label(270,-215,'weeks',-3,46);
   if(lt>2.0) s+=label(-90,300,'all by itself ✓',-4,56);
   return SST(s);},
 (lt,D,t)=>{ // three signs pop in, the phone rings
   let s=sign(-300,-150,seg(lt,0.0,0.3),0)+sign(-300,10,seg(lt,0.12,0.42),1)+sign(-300,170,seg(lt,0.24,0.54),2);
   s+=(lt>0.08?label(-130,-136,'red skin',-3,54):'')+(lt>0.12?label(-112,26,'yellow ooze',-3,54):'')+(lt>0.24?label(-126,186,'bad smell',-3,54):'');
   s+=phone(200,10,t,seg(lt,0.6,0.9));
   if(lt>0.7) s+=label(200,-175,'call your doctor',-4,54);
   return SST(s);},
 (lt,D,t)=>{ // do this: diaper folded below the stump, check, hearts
   let s=mat()+babyTop(1,t,1)+check(-20,-190,seg(lt,0.2,0.7))+hearts(t,-100,-120);
   return SST(s);},
];
function popBurstS(x,y,k){if(k<=0||k>=1)return '';let s='';const r=40+50*k;for(let i=0;i<8;i++){const a=i*Math.PI/4;
 s+=`<path d="M${x+r*Math.cos(a)} ${y+r*Math.sin(a)} L${x+(r+22)*Math.cos(a)} ${y+(r+22)*Math.sin(a)}" stroke="${BUT}" stroke-width="7" stroke-linecap="round" opacity="${1-k}"/>`;}return s;}
SC.stump.special=(beat,lt)=>(y0,sag)=>{ // Do this: a tiny diaper flies up and is pegged on the line
  if(beat<4) return ''; const f=EIO(seg(lt,0.1,0.9)); const tx=930, ty=lineY(930,y0,sag);
  const sx=480, sy=1150; const X=sx+(tx-sx)*f, Y=sy+(ty-sy)*f-160*Math.sin(Math.PI*f);
  return `<g transform="translate(${X} ${Y}) rotate(${-20*(1-f)+4*Math.sin(T*2)}) scale(.88)">${G.diaper()}</g>`;};
"""

SPEC_STUMP = dict(
    out="lf-reel-1028am-cord-stump", outdir=OUT, music=LIB / "v3/lf-c-sunny-morning-el.mp3", scene="stump", follow=FOLLOW,
    sky=("dawn", "morning"), garments=["onesie", "sock", "hat", "dress", "none"],
    durs=[5 * BS, 6 * BS, 6 * BS, 6 * BS, 6 * BS], extra_pops=[], cover_beat=0, cover_lt=2.0,
    beats=[
        dict(kick="diaper rubbing the cord stump?", head="Fold the diaper / *below the stump.*", sub="So pee can't soak it.", fs=140, sy=860, ss=50, chip="AAP · Umbilical cord care"),
        dict(kick="until it falls off", head="Keep it / *clean and dry.*", sub="No alcohol needed.", fs=150, sy=860, ss=50, chip="AAP · NHS"),
        dict(kick="leave it be", head="It falls off / *on its own.*", sub="Usually by 3 weeks old.", fs=150, sy=860, ss=50, chip="AAP · Umbilical cord care"),
        dict(kick="call your doctor if you see", head="Red skin, yellow / *ooze, a bad smell.*", sub="Active bleeding? Call right away.", fs=130, sy=860, ss=46, chip="AAP · Umbilical cord care"),
        dict(kick="Do this:", head="Next diaper: fold it / *below the stump.*", sub="send this to someone with a brand-new baby", fs=126, sy=860, ss=42, chip="AAP · NHS"),
    ])

# =====================================================================================================================
# Reel 2: rice-grain toothpaste (calm text, sky + clouds, no washing line)
# =====================================================================================================================
JS_TEETH = r"""
// ===================== Oct 27: rice-grain toothpaste (calm text) =====================
function cloudS(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-120 30 Q-130 -20 -80 -24 Q-70 -70 -20 -64 Q10 -100 56 -70 Q110 -76 112 -28 Q150 -20 140 30 Z" fill="#FFFAF3" opacity=".92"/></g>`;}
function skyBG(t){let s='';
 const b=[[40,560,230,'#FFD6E3'],[1050,760,210,'#FFE27E'],[1060,1700,260,'#FFD3AE'],[20,1600,240,'#D7E8CB']];
 b.forEach(([x,y,r,c],i)=>{s+=`<circle cx="${x+16*Math.sin(t*0.45+i*1.7)}" cy="${y+10*Math.cos(t*0.4+i)}" r="${r}" fill="${c}" opacity=".7"/>`;});
 s+=cloudS(180+12*t,250,1.0)+cloudS(860-9*t,170,0.8);
 let tl='';for(let i=0;i<7;i++)tl+=`<path d="M${i*180} 1340 V1920" stroke="#FFDDB8" stroke-width="4"/>`;
 s+=`<rect x="-10" y="1320" width="1100" height="620" fill="#FFE9C9" stroke="${PL}" stroke-width="5"/><rect x="-10" y="1320" width="1100" height="26" fill="#FFF4E0" stroke="${PL}" stroke-width="5"/>${tl}`;
 return s;}
function brush(x,y,rot,s){ // toothbrush, bristles UP, head LEFT; origin = centre of the bristle top
 let br='';for(let i=0;i<7;i++){const bx=-120+i*40;br+=`<rect x="${bx-13}" y="0" width="26" height="62" rx="9" fill="${i%2?'#FFFFFF':'#CFE3F6'}" stroke="${PL}" stroke-width="3.5"/>`;}
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">${br}
 <rect x="-150" y="58" width="330" height="56" rx="26" fill="${CREAM}" ${o}/>
 <path d="M170 74 Q300 70 640 66 Q690 66 690 92 Q690 118 640 118 Q300 114 170 108Z" fill="${PINK}" ${o}/>
 <ellipse cx="560" cy="92" rx="70" ry="12" fill="#FFF0F4" opacity=".8"/></g>`;}
function paste(x,y,k,w){ // white paste blob sitting on the bristles; w=0 rice-grain smear, w=1 pea
 if(k<=0) return ''; const rx=(46+14*w)*k, ry=(14+40*w)*k;
 return `<g transform="translate(${x} ${y-ry+4})"><ellipse rx="${rx}" ry="${ry}" fill="#FFFFFF" ${o} stroke-width="4"/><path d="M${-rx*0.6} ${-ry*0.1} Q0 ${-ry*0.7} ${rx*0.6} ${-ry*0.1}" stroke="#BFD9F2" stroke-width="${5+5*w}" fill="none" stroke-linecap="round"/></g>`;}
function tube(x,y,sq){ // toothpaste tube, nozzle DOWN at (x,y); sq squeeze 0..1
 const wv=1-0.18*sq;
 return `<g transform="translate(${x} ${y}) rotate(-24)"><rect x="-12" y="-36" width="24" height="36" rx="5" fill="#FFFFFF" ${o} stroke-width="4"/><rect x="-26" y="-74" width="52" height="40" rx="8" fill="${CORAL}" ${o} stroke-width="4"/>
 <path d="M-50 -74 Q${-70*wv} -170 -64 -300 L64 -300 Q${70*wv} -170 50 -74Z" fill="#E3EEF8" ${o}/><path d="M-74 -300 H74 L68 -322 H-68Z" fill="${PEACH}" ${o} stroke-width="4"/>
 <path d="M-36 -230 q36 -18 72 0" stroke="${BUT}" stroke-width="16" fill="none" stroke-linecap="round"/></g>`;}
function rice(x,y,s,op){return `<g transform="translate(${x} ${y}) scale(${s}) rotate(-14)" opacity="${op}"><ellipse rx="44" ry="15" fill="#FFFDF4" ${o} stroke-width="4"/><path d="M-26 -3 Q0 -9 26 -3" stroke="#E9DFC6" stroke-width="4" fill="none" stroke-linecap="round"/></g>`;}
function pea(x,y,s,op){return `<g transform="translate(${x} ${y}) scale(${s})" opacity="${op}"><circle r="50" fill="#A8D08D" ${o}/><circle cx="-16" cy="-16" r="12" fill="#D7EBC6"/></g>`;}
function cup(x,y,t){return `<g transform="translate(${x} ${y})"><path d="M-70 -90 L70 -90 L56 90 Q0 104 -56 90Z" fill="#CFE3F6" ${o}/><path d="M-62 -40 L62 -40 L56 86 Q0 98 -56 86Z" fill="#9CC4EC" opacity=".7"/><path d="M-62 -40 Q0 ${-30+6*Math.sin(t*4)} 62 -40" stroke="#FFFFFF" stroke-width="5" fill="none"/></g>`;}
function toothF(x,y,s,t,sm){return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-60 -50 Q-70 -80 -36 -84 Q-16 -86 0 -74 Q16 -86 36 -84 Q70 -80 60 -50 Q56 0 40 60 Q30 80 18 60 L6 20 Q0 10 -6 20 L-18 60 Q-30 80 -40 60 Q-56 0 -60 -50Z" fill="#FFFFFF" ${o}/>
 <path d="M-26 -40 q8 -8 16 0 M10 -40 q8 -8 16 0" stroke="#5A2E22" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M-14 -16 q14 ${10+6*sm} 28 0" stroke="#9A4E2A" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="-38" cy="-24" r="8" fill="#FF9EA8" opacity=".6"/><circle cx="38" cy="-24" r="8" fill="#FF9EA8" opacity=".6"/></g>`;}
function bubblesT(t,x,y,op){let s='';for(let i=0;i<6;i++){const k=(t*0.8+i/6)%1;s+=`<circle cx="${x+(i-3)*30+10*Math.sin(t*3+i)}" cy="${y-120*k}" r="${8+10*k}" fill="#FFFFFF" fill-opacity=".8" stroke="${PL}" stroke-width="3" opacity="${op*Math.sin(Math.PI*k)}"/>`;}return s;}
function moonS(x,y){return `<path transform="translate(${x} ${y})" d="M20 -50 A52 52 0 1 0 50 34 A42 42 0 1 1 20 -50Z" fill="${BUT}" ${o}/>`;}
const BX=300, BY=1170;   // where the paste sits on the bristles (screen)
const SCT=[];
SCT[0]=(lt,t)=>{ // tube squeezes a rice-grain smear; a rice grain drops in beside for scale
 const sq=Math.sin(Math.PI*seg(lt,0.2,0.9)), k=E(seg(lt,0.35,0.95)), rk=E(seg(lt,1.1,1.5));
 let s=brush(BX,BY,0,1.0)+paste(BX,BY,k,0)+tube(BX-20-520*E(seg(lt,1.0,1.5)),BY-60-80*E(seg(lt,1.0,1.5)),sq);
 s+=rice(BX+440,BY-300+120*rk,1.3,rk);
 if(lt>1.4){s+=`<path d="M${BX+370} ${BY-170} Q${BX+200} ${BY-220} ${BX-20} ${BY-60}" stroke="#B23A62" stroke-width="5" fill="none" stroke-dasharray="6 12" stroke-linecap="round"/>`+label(BX+450,BY-260,'a rice grain',-5,60);}
 return s;};
SCT[1]=(lt,t)=>{ // the smear grows to a pea-sized dot; a pea rolls in
 const w=EIO(seg(lt,0.2,1.0)), pk=E(seg(lt,0.6,1.2));
 let s=brush(BX,BY,0,1.0)+paste(BX,BY,1,w);
 s+=`<g transform="translate(${BX+440+300*(1-pk)} ${BY-170}) rotate(${-300*(1-pk)})">${pea(0,0,1.25,1)}</g>`;
 if(lt>1.2) s+=label(BX+440,BY-280,'a pea',-5,60);
 return s;};
SCT[2]=(lt,t)=>{ // spit: brush tilts; the rinse cup gets a 'no' ring
 let s=brush(BX-40,BY,-6,1.0)+paste(BX-80,BY-4,1-seg(lt,0,0.4),0.4)+bubblesT(t,BX-70,BY-40,1-seg(lt,0.8,1.2));
 s+=cup(BX+330,BY-110,t)+noRing(BX+330,BY-110,140,seg(lt,0.35,1.1));
 if(lt>1.0) s+=label(BX+330,BY-290,'leave the fluoride on',-4,54);
 return s;};
SCT[3]=(lt,t)=>{ // bedtime brush: a little tooth gets brushed, sparkles, moon, hearts
 const bx=BX-60+50*Math.sin(t*9)*(1-seg(lt,1.6,2.0));
 let s=moonS(900,1000)+toothF(BX+330,BY-70,1.3,t,seg(lt,1.4,2.0));
 s+=`<g transform="translate(${bx-BX} 0)">`+brush(BX+10,BY+60,-8,0.8)+paste(BX-12,BY+48,1,0)+`</g>`;
 if(lt<1.7) s+=bubblesT(t,BX+330,BY-90,1); else {for(let i=0;i<3;i++) s+=sparkle(BX+250+i*80,BY-200+((i*37)%50),0.7+0.3*Math.sin(t*5+i),0.95); s+=hearts(t,BX+330,BY-180);}
 return s;};
function draw(t){
 T=t; const S=SPEC, starts=S.starts, n=S.durs.length; let i=0; for(let k=0;k<n;k++) if(t>=starts[k]) i=k;
 let lt=t-starts[i]; if(S.cover){i=S.coverBeat; lt=S.coverLt;}
 let svg=skyBG(t);
 const cam=1+0.035*seg(lt,0,S.durs[i]);
 svg+=`<g transform="translate(540 1180) scale(${cam}) translate(-540 -1180)">`+SCT[i](lt,t)+`</g>`;
 // soft butter iris wipe at each cut (expands from the object, then clears)
 if(!S.cover&&i>0&&lt<0.45){const p=seg(lt,0,0.45);svg+=`<circle cx="${BX}" cy="${BY-60}" r="${80+1500*E(p)}" fill="#FFF6D8" opacity="${0.8*(1-p)}"/>`;}
 document.getElementById('art').innerHTML=svg;
 for(let k=0;k<n;k++){const el=document.getElementById('b'+k); if(!el) continue; let op=0, y=0;
  if(S.cover) op=0; else if(k==i){ op=1; if(i>0){const p=E(seg(lt,0.0,0.22)); y=24*(1-p);} }
  el.style.opacity=op; el.style.transform=`translateY(${y}px)`;}
 for(let k=0;k<n;k++){const c=document.getElementById('c'+k); if(c) c.style.opacity=(!S.cover&&k==i)?(i==0?(t<0.3?0:Math.min(1,(t-0.3)/0.2)):1):0;}
 const f=document.getElementById('follow'); if(f){const p=(S.cover||i!=n-1)?0:E(seg(lt,1.0,1.4)); f.style.opacity=p; f.style.transform=`translateY(${30*(1-p)}px)`;}
}
"""


def html_teeth(spec, cover=None):
    T = ""
    for k, b in enumerate(spec["beats"]):
        inner = f'<div class="hand" style="position:absolute;left:90px;width:900px;top:{b.get("ky", 330)}px;font-size:66px;color:{KICK}">{b["kick"]}</div>'
        inner += K.dual(b["head"], F, cls="S fit", style=f"position:absolute;left:90px;width:900px;top:{b.get('hy', 415)}px;white-space:nowrap;font-size:{b.get('fs', 130)}px;color:{INK}")
        if b.get("sub"):
            inner += (f'<div class="lora" style="position:absolute;left:70px;width:940px;top:{b.get("sy", 800)}px;font-size:{b.get("ss", 46)}px;'
                      f'line-height:1.2;text-align:center;color:{INK}">{b["sub"]}</div>')
        T += f'<div id="b{k}" style="position:absolute;left:0;top:0;width:{W}px;height:1000px;opacity:0;z-index:4">{inner}</div>'
        T += f'<div id="c{k}" style="position:absolute;left:0;right:0;top:1450px;text-align:center;opacity:0;z-index:4"><span class="chipf" style="font-size:28px">{b["chip"]}</span></div>'
    follow = (f'<div id="follow" style="position:absolute;left:0;right:0;top:{spec.get("follow_y", 890)}px;text-align:center;opacity:0;z-index:5">'
              f'<span style="display:inline-block;max-width:820px;padding:16px 36px;border-radius:40px;background:{INK};color:#FFF8EE;font:600 34px/1.25 Poppins">{spec["follow"]}</span></div>')
    body = (f'<div style="position:absolute;inset:0">{RS.sky(W, H, "afternoon", horizon=0.8)}</div>'
            f'<svg id="art" style="position:absolute;left:0;top:0;z-index:2" width="{W}" height="{H}" viewBox="0 0 {W} {H}"></svg>'
            + T + follow + K.stamp(B, 46, 1530, size=120, rot=-10).replace('class="stamp" style="', 'class="stamp" style="z-index:5;')
            + f"<script>{RS.JS}</script>")
    return RS.page(W, H, body)


SPEC_TEETH = dict(
    out="lf-reel-1030-rice-grain", outdir=OUT, music=LIB / "v4/lf-x-sunny-bounce.mp3", follow=FOLLOW, follow_y=800,
    scene="coat", garments=["none"] * 5,
    durs=[6 * BB, 5 * BB, DROP_BB - 11 * BB, 14.3 - DROP_BB], extra_pops=[],
    beats=[
        dict(kick="toothpaste for under-3s", head="A smear the size / *of a rice grain.*", sub="Fluoride toothpaste, from the first tooth.", fs=124, sy=730, ss=46, chip="NHS · AAP"),
        dict(kick="from age 3 to 6", head="Then a / *pea-sized dot.*", fs=140, chip="NHS · AAP"),
        dict(kick="after brushing", head="Spit it out. / *Don't rinse.*", sub="Rinsing washes the fluoride away.", fs=140, sy=730, ss=46, chip="NHS · Best Start in Life"),
        dict(kick="Do this:", head="Tonight: a rice-grain / *smear, then brush.*", sub="Twice a day. Last thing before bed.", fs=118, sy=700, ss=44, chip="NHS · AAP"),
    ])

# =====================================================================================================================
# Covers (dedicated, 2x)
# =====================================================================================================================
BLOBS = ('<div style="position:absolute;left:-140px;top:120px;width:420px;height:420px;border-radius:50%;background:{a};opacity:.8"></div>'
         '<div style="position:absolute;right:-160px;top:820px;width:440px;height:440px;border-radius:50%;background:{b};opacity:.75"></div>'
         '<div style="position:absolute;left:-120px;bottom:-120px;width:460px;height:460px;border-radius:50%;background:{c};opacity:.75"></div>')


def svg_wrap(inner, x, y, w, h, vb):
    return f'<svg style="position:absolute;left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="{vb}">{inner}</svg>'


def cover_stump_html():
    note = (
        '<div style="position:absolute;left:100px;top:440px;width:880px;height:940px;background:#FFFDF7;transform:rotate(-2deg);border-radius:8px;'
        'box-shadow:0 24px 40px rgba(107,59,90,.18);background-image:linear-gradient(#FFFDF7 300px,transparent 300px),'
        'repeating-linear-gradient(#FFFDF7 0 98px,rgba(80,110,180,.26) 98px 100px)">'
        '<div style="position:absolute;left:92px;top:0;bottom:0;width:2px;background:rgba(220,80,80,.45)"></div>'
        f'<div style="position:absolute;left:116px;right:6px;top:64px;font-family:\'Caveat Brush\';font-size:112px;white-space:nowrap;line-height:1.0;color:{INK}">'
        'Fold the diaper<br><span style="color:#D9497A">below the stump.</span></div>'
        '<ul style="position:absolute;left:120px;right:30px;top:300px;list-style:none;white-space:nowrap;font-family:Caveat;font-weight:700;font-size:57px;line-height:100px;color:#3A1F3D">'
        '<li><span style="color:#D9497A;margin-right:16px">✓</span>keep it clean and dry</li>'
        '<li><span style="color:#D9497A;margin-right:16px">✓</span>it falls off by 3 weeks</li>'
        '<li><span style="color:#D9497A;margin-right:16px">✓</span>red, oozing, smelly? call the doctor</li></ul></div>'
        '<div style="position:absolute;left:420px;top:410px;width:240px;height:66px;background:rgba(255,255,255,.6);transform:rotate(3deg);box-shadow:0 2px 6px rgba(0,0,0,.08)"></div>')
    art = svg_wrap("<g id='mini'></g>", 400, 1050, 560, 330, "0 0 560 330")
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4,#FFEFD8)"></div>'
            + BLOBS.format(a="#FFD6E3", b="#FFE27E", c="#FFD3AE") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:318px;font-size:70px;color:{KICK}">diaper rubbing the cord stump?</div>'
            + note + art + K.stamp(B, 46, 1470, size=120, rot=-10)
            + f"<script>{BASE_JS}{JS_STUMP}\n"
            + "document.getElementById('mini').innerHTML=`<g transform='translate(320 165) scale(.58)'>${babyTop(1,0,1)}</g>`+check(470,50,1);</script>")
    return RS.page(W, H, body)


def cover_teeth_html():
    ros = ""
    for (x, col, l1, l2) in [(300, "#FFB9CF", "under 3", "rice grain"), (780, "#FFE08A", "3 to 6", "a pea")]:
        sc = "".join(f'<circle cx="{62 * __import__("math").cos(i * 0.3927):.1f}" cy="{62 * __import__("math").sin(i * 0.3927):.1f}" r="16" fill="{col}" stroke="#6B3B5A" stroke-width="3.5"/>' for i in range(16))
        ros += (f'<g transform="translate({x} 1150) scale(1.75)"><path d="M-30 40 L-52 130 L-30 116 L-14 138 L4 50Z" fill="#D9497A" stroke="#6B3B5A" stroke-width="3.5" stroke-linejoin="round"/>'
                f'<path d="M30 40 L52 130 L30 116 L14 138 L-4 50Z" fill="#F27C6B" stroke="#6B3B5A" stroke-width="3.5" stroke-linejoin="round"/>{sc}'
                f'<circle r="60" fill="#FFF8EE" stroke="#6B3B5A" stroke-width="3.5"/><circle r="50" fill="none" stroke="{col}" stroke-width="4" stroke-dasharray="4 7"/>'
                f'<text y="-8" font-family="Caveat Brush" font-size="30" text-anchor="middle" fill="#3A1F3D">{l1}</text>'
                f'<text y="24" font-family="Caveat Brush" font-size="26" text-anchor="middle" fill="#B23A62">{l2}</text></g>')
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4,#FFF1DC)"></div>'
            + BLOBS.format(a="#CFE3F6", b="#FFD6E3", c="#FFE27E") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:318px;font-size:72px;color:{KICK}">toothpaste for under-3s</div>'
            + K.dual("Just a smear, / *a rice grain.*", F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:405px;white-space:nowrap;font-size:150px;color:{INK}")
            + '<svg id="art" style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10)
            + f"<script>{BASE_JS}{JS_TEETH}\n"
            + "document.getElementById('art').innerHTML=brush(400,890,0,0.75)+paste(400,890,1,0)+label(720,800,'just this much',-5,54)+`<path d='M600 815 Q500 800 440 850' stroke='#B23A62' stroke-width='5' fill='none' stroke-dasharray='6 12' stroke-linecap='round'/>`"
            + f"+`{ros}`;</script>")
    return RS.page(W, H, body)


def render_cover(html, out):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, dir=RS.SCR) as f:
            f.write(html)
            tmp = f.name
        pg.goto(Path(tmp).as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        pg.evaluate(K.FIT_JS, 920)
        png = RS.SCR / (out.stem + ".png")
        pg.screenshot(path=str(png))
        br.close()
    Image.open(png).resize((W, H), Image.LANCZOS).convert("RGB").save(out, quality=92, subsampling=0)
    print("cover", out, flush=True)


def use(key):
    if key == "stump":
        RS.JS = BASE_JS + JS_STUMP
        RS.html = lambda spec, cover=None: BASE_HTML(spec, cover).replace("top:455px;font-size:68px", "top:455px;font-size:62px").replace("top:1500px;text-align:center;opacity:0", "top:1440px;text-align:center;opacity:0;z-index:6").replace("padding:12px 30px;border-radius:99px;background:#3A1F3D;color:#FFF8EE;font:600 32px Poppins", "max-width:700px;padding:14px 34px;border-radius:40px;background:#3A1F3D;color:#FFF8EE;font:600 34px/1.25 Poppins")
        return SPEC_STUMP, cover_stump_html
    RS.JS = BASE_JS + JS_TEETH
    RS.html = html_teeth
    return SPEC_TEETH, cover_teeth_html


if __name__ == "__main__":
    for a in sys.argv:
        if a.startswith("--still="):
            RS.STILLS = [float(x) for x in a[8:].split(",")]
        if a.startswith("--sw="):
            RS.SW = int(a[5:])
    for key in [a for a in sys.argv[1:] if not a.startswith("--")]:
        s, ch = use(key)
        OUT.mkdir(parents=True, exist_ok=True)
        render_cover(ch(), OUT / f"{s['out']}-cover.jpg")
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

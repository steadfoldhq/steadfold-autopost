#!/usr/bin/env python3
"""Nov 1 (Social studio, Littlefold maker): three Reels in the rice-grain shape (calm sky + ONE drawn object doing the
rule + a size or amount you can picture), extending oct27_littlefold.py (JS_TEETH: skyBG, cup, sparkle, label ...) and
studio/recovery-oct22c/littlefold/reel_story.py through it. Both imported, not edited.

A  lf-reel-1101-grapes-in-4     (Sun Nov 1 19:00)  PART 1: "Toddler eating grapes? Cut each grape into 4."
   Chopping board: a knife cuts one grape lengthways, then again -> 4 pieces, numbered 1-4 (by ~1.7 s); cherry tomato,
   cherry and blueberry split into quarters; an apple chunk gets a 'no' ring, slices fan out; Do this: a toddler in a
   high chair (second LF baby pose) eats quartered grapes. Last beat: "Part 2 tomorrow, 7 pm." tape + follow pill.
   COVER: Ep.01 reframe 'Instead of... / Try...' (style-menu #7, quiet).
B  lf-reel-1102-sausage-strips  (Mon Nov 2 19:00)  PART 2: "Sausage for a toddler? Strips, not round slices."
   Round slices drop off the knife and get a 'no' ring; the other half splits lengthways into strips (check) by ~2.4 s;
   step 1 in half / step 2 lengthways; whole nuts and popcorn get 'no' rings, chopped nuts a check; Do this: toddler
   with strips on the tray. COVER: original simple template 'compare' (style-menu #8, quiet).
C  lf-reel-1103-5cm-water       (Tue Nov 3 19:00)  "Babies can drown in just 5 cm of water."
   Sunny tiled bathroom: water rises in an empty tub to a drawn 5 cm mark on a ruler (by ~1.3 s); a parent's hand stays on
   the baby in the bath while a phone rings ('it can wait'); a bath seat is labelled 'not a safety device', the hand stays;
   Do this: the plug is pulled, the water swirls away, a check. COVER: kinetic big text '5 cm' (style-menu #5, loud).

Facts (checked Nov 1 2026):
  NHS Best Start in Life 'Preparing food safely for babies' (nhs.uk/best-start-in-life/baby/weaning/safe-weaning/preparing-food-safely/,
    modified 12 Jun 2026): "Cut small round fruits like grapes, cherries, berries, strawberries and cherry tomatoes into quarters
    (4 small pieces)."; "Cut fruit like melon and apples into slices instead of small chunks."; "Cut sausages and hot dogs into
    short strips."; "Cut them in half and then lengthways, or as thinly as possible."; "Do not give whole nuts or popcorn to
    children under 5 years old."; "Chop or flake whole nuts, peanuts and seeds."; "avoid round shapes and firm foods".
  AAP HealthyChildren.org 'Choking Prevention' (last updated 2/27/2026): round, firm foods such as hot dogs or grapes "can be
    served if completely chopped into tiny pieces"; keep high-risk foods away "until 4 years of age or older"; "Most children
    who die from choking are under age 5."
  NHS 'Baby and toddler safety' (last reviewed 19 Feb 2026): "Babies can drown in as little as 5cm (2 inches) of water.";
    "it's often silent"; "Stay with your baby or toddler the whole time they're in the bath."; "Never leave them for a moment,
    even if there's an older brother or sister in the bath with them."; "If you use a bath seat, remember that it's not a
    safety device."; "Empty the bath as soon as you've taken your child out."

    python3 studio/editorial/nov01_littlefold.py grapes|sausage|water [--still=0.0,1.5,...] [--cover-only] [--no-cover]
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path
sys.dont_write_bytecode = True
os.environ["LF_SCR"] = "/tmp/claude-0/nov01-littlefold"
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oct27_littlefold as S27  # noqa: E402  (imports reel_story as RS; nothing renders on import)
RS = S27.RS

K, F, INK, KICK, B = RS.K, RS.F, RS.INK, RS.KICK, RS.B
W, H, FPS = RS.W, RS.H, RS.FPS
OUT = RS.REPO / "media" / "studio-nov01" / "littlefold"
LIB = RS.LIB
FOLLOW = "Follow for one calm thing a night, from bump to toddler."
BB, DROP_BB = 60 / 112.3, 8.266   # lf-x-sunny-bounce (the rice-grain track)
BG, DROP_BG = 60 / 120.2, 3.971   # lf-x-giggle-pop
BP, DROP_BP = 60 / 103.4, 9.195   # lf-x-tiny-parade

JS = r"""
// ===================== Nov 1: grapes, sausages, 5 cm of water =====================
const BSK2='#FFDCC4', GRN='#B9D98C', GRN2='#E4F2CF', RED='#F2707A', SAUS='#E99A74', SAUS2='#F7C3A6';
function board(x,y,w){w=w||760;return `<g transform="translate(${x} ${y})"><rect x="${-w/2}" y="-30" width="${w}" height="64" rx="26" fill="#F3CFA0" ${o}/>
 <path d="M${-w/2+40} -6 H${w/2-90} M${-w/2+80} 10 H${w/2-140}" stroke="#E2B47E" stroke-width="5" stroke-linecap="round"/><circle cx="${w/2-46}" cy="0" r="12" fill="#FFE9C9" ${o} stroke-width="4"/></g>`;}
function knife(x,y,rot,s){return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s||1})">
 <path d="M0 0 L250 -6 Q262 6 250 26 L10 30 Q-6 16 0 0Z" fill="#EEF3F8" ${o}/><path d="M24 8 L220 4" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
 <rect x="-170" y="-6" width="176" height="44" rx="18" fill="${CORAL}" ${o}/><circle cx="-120" cy="16" r="6" fill="${CREAM}"/><circle cx="-60" cy="16" r="6" fill="${CREAM}"/></g>`;}
function lens(cx,cy,len,th,rot,col,col2){ // a long grape quarter seen from above
 return `<g transform="translate(${cx} ${cy}) rotate(${rot})"><path d="M${-len/2} 0 Q0 ${-th} ${len/2} 0 Q0 ${th} ${-len/2} 0Z" fill="${col2}" ${o} stroke-width="4"/>
 <path d="M${-len/2+10} 0 Q0 ${-th*0.6} ${len/2-10} 0" stroke="${col}" stroke-width="${th*0.55}" fill="none" stroke-linecap="round" opacity=".9"/></g>`;}
function grape(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s||1})"><ellipse rx="70" ry="54" fill="${GRN}" ${o}/>
 <ellipse cx="-24" cy="-20" rx="18" ry="10" fill="#FFFFFF" opacity=".55"/><path d="M66 -6 q16 -6 22 -20" stroke="#8A6A4A" stroke-width="7" fill="none" stroke-linecap="round"/></g>`;}
function grapeCut(x,y,k1,k2,num){ // k1: first lengthways cut (2 halves), k2: second cut (4 long pieces)
 if(k1<=0) return grape(x,y,1);
 let s='';
 if(k2<=0){ const g=10+22*E(k1); s+=lens(x,y-g,140,34,0,GRN,GRN2)+lens(x,y+g,140,34,0,GRN,GRN2); return s; }
 const g=20+16*E(k2);
 [-3,-1,1,3].forEach((m,i)=>{const yy=y+m*g/2*1.2; s+=lens(x,yy,140,22,0,GRN,GRN2);
   if(num>0){const nk=seg(num,i*0.2,i*0.2+0.3); if(nk>0) s+=`<g opacity="${nk}"><circle cx="${x+104}" cy="${yy}" r="${20*nk}" fill="#D9497A"/><text x="${x+104}" y="${yy+9}" font-family="Poppins" font-weight="700" font-size="${26*nk}" text-anchor="middle" fill="#FFF8EE">${i+1}</text></g>`;}});
 return s;}
function quarters(x,y,r,k,col,col2,top){ // a round fruit seen from above, splitting into 4 wedges
 const g=22*E(k); let s='';
 for(let i=0;i<4;i++){const a0=i*Math.PI/2, am=a0+Math.PI/4, dx=g*Math.cos(am), dy=g*Math.sin(am);
   s+=`<path d="M${x+dx} ${y+dy} L${x+dx+r*Math.cos(a0)} ${y+dy+r*Math.sin(a0)} A${r} ${r} 0 0 1 ${x+dx+r*Math.cos(a0+Math.PI/2)} ${y+dy+r*Math.sin(a0+Math.PI/2)} Z" fill="${k>0?col2:col}" ${o} stroke-width="4"/>`;
   if(k>0) s+=`<path d="M${x+dx+r*0.9*Math.cos(a0+0.15)} ${y+dy+r*0.9*Math.sin(a0+0.15)} A${r*0.9} ${r*0.9} 0 0 1 ${x+dx+r*0.9*Math.cos(a0+Math.PI/2-0.15)} ${y+dy+r*0.9*Math.sin(a0+Math.PI/2-0.15)}" stroke="${col}" stroke-width="10" fill="none" stroke-linecap="round"/>`;}
 if(k<=0) s=`<circle cx="${x}" cy="${y}" r="${r}" fill="${col}" ${o}/><ellipse cx="${x-r*0.35}" cy="${y-r*0.4}" rx="${r*0.25}" ry="${r*0.14}" fill="#FFFFFF" opacity=".55"/>`+(top||'');
 return s;}
function leafStar(x,y){return `<path d="M${x} ${y-60} l10 14 l16 -6 l-6 16 l14 10 l-17 4 l-2 17 l-13 -11 l-13 11 l-2 -17 l-17 -4 l14 -10 l-6 -16 l16 6z" fill="#8DB07F" stroke="${PL}" stroke-width="3"/>`;}
function appleChunk(x,y){return `<g transform="translate(${x} ${y})"><path d="M-50 -30 L20 -50 L60 -20 L60 40 L-10 60 L-50 30Z" fill="#FFF3D6" ${o}/><path d="M20 -50 L60 -20 L60 40 L20 10Z" fill="#FFE7B0" ${o} stroke-width="4"/><path d="M-50 -30 L20 -50 L20 10 L-50 30" fill="none" stroke="${RED}" stroke-width="8"/></g>`;}
function appleSlices(x,y,k){let s='';for(let i=0;i<4;i++){const a=(-30+20*i)*E(k);
 s+=`<g transform="translate(${x} ${y}) rotate(${a} 0 70)"><path d="M-16 -70 Q30 -60 30 0 Q30 60 -16 70 Q6 0 -16 -70Z" fill="#FFF3D6" ${o} stroke-width="4"/><path d="M-16 -70 Q30 -60 30 0 Q30 60 -16 70" fill="none" stroke="${RED}" stroke-width="8"/></g>`;}return s;}
function highChair(x,y,t,eat,tray){ // toddler (front view, smiling, face drawn) in a high chair; eat 0..1 hand to mouth
 const hy=y-170, bob=3*Math.sin(t*3);
 const hx=x+60-40*eat, hY=y-30-100*eat;
 return `<g>
 
 <rect x="${x-130}" y="${y-250}" width="260" height="300" rx="50" fill="${BLUE}" ${o}/>
 <path d="M${x-80} ${y-80} Q${x} ${y-110} ${x+80} ${y-80} L${x+90} ${y+30} L${x-90} ${y+30}Z" fill="${PINK}" ${o}/>
 <path d="M${x-60} ${y-86} Q${x} ${y-40} ${x+60} ${y-86} Q${x+40} ${y-20} ${x} ${y-14} Q${x-40} ${y-20} ${x-60} ${y-86}Z" fill="${BUT}" ${o} stroke-width="4"/>
 <g transform="translate(0 ${bob})"><circle cx="${x}" cy="${hy}" r="78" fill="${BSK2}" ${o}/>
 <path d="M${x-40} ${hy-66} q20 -36 46 -16 q10 -24 30 -6" stroke="#A0674A" stroke-width="7" fill="none" stroke-linecap="round"/>
 <circle cx="${x-28}" cy="${hy-6}" r="8" fill="#5A2E22"/><circle cx="${x+28}" cy="${hy-6}" r="8" fill="#5A2E22"/><circle cx="${x-25}" cy="${hy-9}" r="3" fill="#fff"/><circle cx="${x+31}" cy="${hy-9}" r="3" fill="#fff"/>
 <path d="M${x-18} ${hy+24} q18 ${eat>0.6?6:16} 36 0" stroke="#9A4E2A" stroke-width="6" fill="${eat>0.6?'none':'#E77F72'}" stroke-linecap="round"/>
 <circle cx="${x-50}" cy="${hy+16}" r="12" fill="#FF9EA8" opacity=".65"/><circle cx="${x+50}" cy="${hy+16}" r="12" fill="#FF9EA8" opacity=".65"/></g>
 <path d="M${x-70} ${y-60} Q${x-110} ${y-20} ${x-90} ${y+20}" stroke="${PL}" stroke-width="34" fill="none" stroke-linecap="round"/><path d="M${x-70} ${y-60} Q${x-110} ${y-20} ${x-90} ${y+20}" stroke="${PINK}" stroke-width="25" fill="none" stroke-linecap="round"/>
 <path d="M${x+70} ${y-60} Q${(x+70+hx)/2+30} ${(y-60+hY)/2+10} ${hx} ${hY}" stroke="${PL}" stroke-width="34" fill="none" stroke-linecap="round"/><path d="M${x+70} ${y-60} Q${(x+70+hx)/2+30} ${(y-60+hY)/2+10} ${hx} ${hY}" stroke="${PINK}" stroke-width="25" fill="none" stroke-linecap="round"/>
 <circle cx="${hx}" cy="${hY}" r="19" fill="${BSK2}" ${o} stroke-width="4"/>
 <rect x="${x-210}" y="${y+20}" width="420" height="44" rx="20" fill="${CREAM}" ${o}/>${tray||''}</g>`;}
function sausage(x,y,len,rot){return `<g transform="translate(${x} ${y}) rotate(${rot||0})"><rect x="${-len/2}" y="-30" width="${len}" height="60" rx="30" fill="${SAUS}" ${o}/><path d="M${-len/2+30} -12 H${len/2-30}" stroke="${SAUS2}" stroke-width="8" stroke-linecap="round"/></g>`;}
function coin(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s||1})"><circle r="32" fill="${SAUS2}" ${o} stroke-width="4"/><circle r="22" fill="none" stroke="${SAUS}" stroke-width="6"/></g>`;}
function strip(x,y,len,rot){return `<g transform="translate(${x} ${y}) rotate(${rot||0})"><rect x="${-len/2}" y="-11" width="${len}" height="22" rx="10" fill="${SAUS2}" ${o} stroke-width="4"/><path d="M${-len/2+8} -11 H${len/2-8}" stroke="${SAUS}" stroke-width="6"/></g>`;}
function nut(x,y,r){return `<g transform="translate(${x} ${y}) rotate(${r||0})"><path d="M-46 0 Q-50 -34 -16 -30 Q0 -20 16 -30 Q50 -34 46 0 Q50 34 16 30 Q0 20 -16 30 Q-50 34 -46 0Z" fill="#E8C08C" ${o} stroke-width="4"/><path d="M-26 -10 l6 6 M20 8 l6 6 M-6 12 l6 6" stroke="#B88A5A" stroke-width="4" stroke-linecap="round"/></g>`;}
function popcorn(x,y){return `<g transform="translate(${x} ${y})"><path d="M-30 10 Q-50 -10 -28 -28 Q-20 -54 6 -42 Q30 -56 40 -28 Q60 -8 36 14 Q30 36 4 30 Q-24 40 -30 10Z" fill="#FFF8E0" ${o} stroke-width="4"/><path d="M-6 6 q10 -10 22 -2" stroke="${BUT}" stroke-width="7" fill="none" stroke-linecap="round"/></g>`;}
function flakes(x,y){let s='';const P=[[-40,0],[-14,-14],[12,2],[38,-10],[-26,18],[4,20],[30,16],[-4,-26]];P.forEach(([a,b],i)=>{s+=`<path transform="translate(${x+a} ${y+b}) rotate(${i*41})" d="M-12 -5 L10 -8 L13 5 L-8 8Z" fill="#E8C08C" stroke="${PL}" stroke-width="3" stroke-linejoin="round"/>`;});return s;}
function step(x,y,n,txt,k){if(k<=0) return ''; return `<g opacity="${k}"><circle cx="${x}" cy="${y}" r="30" fill="#D9497A"/><text x="${x}" y="${y+11}" font-family="Poppins" font-weight="700" font-size="32" text-anchor="middle" fill="#FFF8EE">${n}</text>`+label(x+40+txt.length*12,y+14,txt,-3,54)+`</g>`;}
// ---------- bathroom
function bathBG(t){let s=`<rect width="1080" height="1920" fill="#FFF6E6"/>`;
 for(let r=0;r<9;r++)for(let c=0;c<7;c++){const x=c*160+(r%2?80:0)-40, y=180+r*130; s+=`<rect x="${x}" y="${y}" width="150" height="120" rx="14" fill="${(r+c)%3==0?'#FFE3D2':'#FFEFD9'}" stroke="#F6D9C3" stroke-width="4"/>`;}
 const b=[[40,560,200,'#FFD6E3'],[1050,760,190,'#FFE27E'],[1060,1700,240,'#FFD3AE']];
 b.forEach(([x,y,r,c],i)=>{s+=`<circle cx="${x+14*Math.sin(t*0.45+i*1.7)}" cy="${y+10*Math.cos(t*0.4+i)}" r="${r}" fill="${c}" opacity=".55"/>`;});
 s+=`<rect x="-10" y="1520" width="1100" height="440" fill="#CFE3F6" stroke="${PL}" stroke-width="5"/>`;
 for(let i=0;i<8;i++) s+=`<path d="M${i*150} 1520 V1920" stroke="#BCD5EE" stroke-width="4"/>`;
 return s;}
const TX=540, TRIM=1010, TBOT=1330, WL=TBOT-24;   // tub centre, rim, inner floor
function tub(t,lvl,inner){ // side view; lvl = water height in px (70 px = 5 cm on the drawn ruler)
 const top=WL-lvl;
 return `<path d="M${TX-360} ${TBOT+10} L${TX-330} ${TBOT+70} M${TX+360} ${TBOT+10} L${TX+330} ${TBOT+70}" stroke="${PL}" stroke-width="16" stroke-linecap="round"/>
 ${inner||''}
 ${lvl>0?`<path d="M${TX-372} ${top} Q${TX-200} ${top+6*Math.sin(t*3)} ${TX} ${top} T${TX+372} ${top} L${TX+372} ${WL+6} L${TX-372} ${WL+6}Z" fill="#7FB3E8" opacity=".88"/>`:''}
 <path d="M${TX-400} ${TRIM} H${TX+400} L${TX+380} ${TBOT-20} Q${TX+370} ${TBOT+20} ${TX+320} ${TBOT+20} H${TX-320} Q${TX-370} ${TBOT+20} ${TX-380} ${TBOT-20} Z" fill="${CREAM}" ${o} opacity=".35"/>
 <path d="M${TX-400} ${TRIM} H${TX+400} L${TX+380} ${TBOT-20} Q${TX+370} ${TBOT+20} ${TX+320} ${TBOT+20} H${TX-320} Q${TX-370} ${TBOT+20} ${TX-380} ${TBOT-20} Z" fill="none" ${o}/>
 <rect x="${TX-420}" y="${TRIM-26}" width="840" height="34" rx="16" fill="#FFFFFF" ${o}/>`;}
function ruler(x,k){ // a drawn ruler standing on the tub floor, 0..10 cm (14 px per cm)
 let s=`<rect x="${x-24}" y="${WL-150}" width="48" height="156" rx="6" fill="${BUT}" ${o} stroke-width="4"/>`;
 for(let i=0;i<=10;i++) s+=`<path d="M${x-24} ${WL-14*i} h${i%5?16:30}" stroke="${PL}" stroke-width="${i%5?3:5}"/>`;
 return `<g opacity="${k}">${s}</g>`;}
function duck(x,y,t){const b=4*Math.sin(t*3.2);return `<g transform="translate(${x} ${y+b}) rotate(${3*Math.sin(t*2)})"><path d="M-60 0 Q-64 -44 -14 -40 Q-20 -84 18 -86 Q52 -84 50 -52 Q70 -54 78 -44 Q64 -32 44 -34 Q70 -20 60 4 Q40 30 -20 28 Q-56 26 -60 0Z" fill="#FFD84D" ${o}/><circle cx="24" cy="-62" r="6" fill="#5A2E22"/><path d="M-30 -6 q20 14 40 0" stroke="#F2A94B" stroke-width="6" fill="none" stroke-linecap="round"/></g>`;}
function bathBaby(x,y,t,seat){ // baby sitting in water, smiling, face drawn; seat: a ring bath seat around the tummy
 const sw=2*Math.sin(t*2.4);
 return `<g transform="rotate(${sw} ${x} ${y})"><path d="M${x-70} ${y+60} Q${x-80} ${y-40} ${x} ${y-50} Q${x+80} ${y-40} ${x+70} ${y+60}Z" fill="${BSK2}" ${o}/>
 <path d="M${x-62} ${y-20} Q${x-118} ${y+10} ${x-104} ${y+50}" stroke="${PL}" stroke-width="34" fill="none" stroke-linecap="round"/><path d="M${x-62} ${y-20} Q${x-118} ${y+10} ${x-104} ${y+50}" stroke="${BSK2}" stroke-width="25" fill="none" stroke-linecap="round"/>
 <path d="M${x+62} ${y-20} Q${x+118} ${y+10} ${x+104} ${y+50}" stroke="${PL}" stroke-width="34" fill="none" stroke-linecap="round"/><path d="M${x+62} ${y-20} Q${x+118} ${y+10} ${x+104} ${y+50}" stroke="${BSK2}" stroke-width="25" fill="none" stroke-linecap="round"/>
 ${seat?`<ellipse cx="${x}" cy="${y+20}" rx="120" ry="34" fill="${SAGE}" ${o}/><ellipse cx="${x}" cy="${y+14}" rx="78" ry="18" fill="#A8CA9A"/><path d="M${x-90} ${y+46} L${x-100} ${y+150} M${x+90} ${y+46} L${x+100} ${y+150}" stroke="${SAGE}" stroke-width="18" stroke-linecap="round"/><path d="M${x-90} ${y+46} L${x-100} ${y+150} M${x+90} ${y+46} L${x+100} ${y+150}" stroke="${PL}" stroke-width="4" stroke-linecap="round" opacity=".6"/>`:''}
 <circle cx="${x}" cy="${y-120}" r="76" fill="${BSK2}" ${o}/><path d="M${x-14} ${y-196} q14 -24 30 -4" stroke="#A0674A" stroke-width="7" fill="none" stroke-linecap="round"/>
 <circle cx="${x-26}" cy="${y-128}" r="8" fill="#5A2E22"/><circle cx="${x+26}" cy="${y-128}" r="8" fill="#5A2E22"/><circle cx="${x-23}" cy="${y-131}" r="3" fill="#fff"/><circle cx="${x+29}" cy="${y-131}" r="3" fill="#fff"/>
 <path d="M${x-18} ${y-98} q18 16 36 0" stroke="#9A4E2A" stroke-width="6" fill="#E77F72" stroke-linecap="round"/>
 <circle cx="${x-50}" cy="${y-104}" r="12" fill="#FF9EA8" opacity=".65"/><circle cx="${x+50}" cy="${y-104}" r="12" fill="#FF9EA8" opacity=".65"/></g>`;}
function adultArm(x,y,k){ // an adult forearm from the right edge, the palm resting at (x,y)
 const ox=x+520*(1-k);
 return `<g transform="translate(${ox} ${y})"><path d="M30 -10 L700 -60 L700 70 L30 40Z" fill="${PEACH}" ${o}/><path d="M-50 -30 Q-70 0 -50 34 L40 44 L40 -26Z" fill="${SK}" ${o}/>
 <path d="M-50 -24 Q-90 -24 -92 -6 M-52 2 Q-96 4 -96 20 M-50 26 Q-88 30 -86 44" stroke="${PL}" stroke-width="4" fill="none" stroke-linecap="round"/></g>`;}
function phoneR(x,y,t,k){ if(k<=0) return ''; const r=6*Math.sin(t*30);
 return `<g transform="translate(${x} ${y}) rotate(${r})" opacity="${k}"><rect x="-44" y="-80" width="88" height="160" rx="18" fill="${INK}"/><rect x="-34" y="-64" width="68" height="124" rx="10" fill="#FFF8EE"/><circle cx="0" cy="-8" r="18" fill="${SAGE}"/>
 <path d="M-62 -40 q-16 40 0 80 M62 -40 q16 40 0 80" stroke="#D9497A" stroke-width="6" fill="none" stroke-linecap="round"/></g>`;}
function plug(x,k){const up=60*E(k);return `<path d="M${x} ${WL-up} Q${x+40} ${WL-140-up} ${x+90} ${TRIM}" stroke="#B8C4D0" stroke-width="6" fill="none" stroke-dasharray="2 10" stroke-linecap="round"/><rect x="${x-22}" y="${WL-14-up}" width="44" height="18" rx="6" fill="#B8C4D0" ${o} stroke-width="4"/>`;}
function swirl(x,t,k){ if(k<=0) return ''; let s='';for(let i=0;i<3;i++){const r=20+16*i, a=t*6+i;s+=`<path d="M${x+r*Math.cos(a)} ${WL-6+r*0.3*Math.sin(a)} A${r} ${r*0.3} 0 1 1 ${x+r*Math.cos(a+2.5)} ${WL-6+r*0.3*Math.sin(a+2.5)}" stroke="#FFFFFF" stroke-width="5" fill="none" stroke-linecap="round" opacity="${k}"/>`;}return s;}
function towelH(x,y){return `<g transform="translate(${x} ${y})"><rect x="-80" y="0" width="160" height="230" rx="16" fill="${PINK}" ${o}/><path d="M-80 40 H80 M-80 56 H80" stroke="#FFF0F4" stroke-width="8"/><rect x="-100" y="-14" width="200" height="22" rx="10" fill="#E9BE92" ${o} stroke-width="4"/></g>`;}
// ---------- scene sets
const SCN={};
SCN.grapes=[
 (lt,t)=>{ // knife cuts one grape lengthways, then again: 4 numbered pieces
  const k1=seg(lt,0.55,0.8), k2=seg(lt,1.05,1.3), kx=seg(lt,0.3,0.85), kx2=seg(lt,0.85,1.35), away=E(seg(lt,1.35,1.7));
  let s=board(540,1250,660)+grapeCut(500,1150,k1,k2,seg(lt,1.4,2.4));
  const ky=1150, kxx=lt<0.85?440+230*EIO(kx):440+230*EIO(kx2);
  s+=`<g opacity="${1-away}">`+knife(kxx-60,ky-6-180*away,0,0.8)+`</g>`;
  if(lt>1.6) s+=label(560,1040,'4 small pieces',-4,56);
  return s;},
 (lt,t)=>{ // cherry tomato, cherry, blueberry: each splits into quarters
  let s=board(540,1250,640);
  const F=[[330,RED,'#FFC1C1','cherry tomato',leafStar(330,1170)],[540,'#F06A7E','#FFD0D6','strawberry',leafStar(540,1170)],[750,'#6F86D6','#CFD8F6','blueberry','']];
  F.forEach(([x,c,c2,n,top],i)=>{const k=seg(lt,0.25+0.4*i,0.55+0.4*i); s+=quarters(x,1180,58,k,c,c2,top); if(k>0) s+=label(x,1070,n,-4,40);});
  return s;},
 (lt,t)=>{ // apple: a chunk gets a 'no' ring; slices fan out with a check
  let s=board(540,1250,640)+appleChunk(340,1170)+noRing(340,1170,100,seg(lt,0.2,0.9));
  s+=appleSlices(720,1150,seg(lt,0.6,1.3));
  if(lt>0.8) s+=label(340,1030,'chunks',-4,54);
  if(lt>1.3) {s+=label(720,1030,'slices',-4,54)+check(800,1080,seg(lt,1.3,1.8));}
  return s;},
 (lt,t)=>{ // Do this: toddler in a high chair eats quartered grapes, hearts
  const eat=0.5-0.5*Math.cos(Math.PI*2*seg(lt,0.6,2.2)) ;
  let tray='';for(let i=0;i<4;i++) tray+=lens(450+i*62,1262,60,16,-12+i*9,GRN,GRN2);
  let s=highChair(540,1250,t,eat,tray);
  if(lt>2.3) s+=hearts(t,860,1180);
  return `<g transform="translate(540 1284) scale(.7) translate(-540 -1270)">`+s+`</g>`;},
];
SCN.sausage=[
 (lt,t)=>{ // round slices -> 'no'; the other half -> long strips -> check
  const c=seg(lt,0.15,0.9), nc=Math.floor(c*3.99);
  let s=board(540,1250,660);
  for(let i=0;i<Math.min(nc,3);i++) s+=coin(280+i*70,1190+6*i,1);
  if(lt<1.3){ s+=sausage(430+40*c,1180,300-120*c,0); s+=knife(450+120*c,1040+10*Math.sin(lt*18)*(lt<0.9?1:0),80,0.85); }
  else { const k=seg(lt,1.3,1.9); for(let i=0;i<4;i++) s+=strip(700,1140+(24+10*E(k))*i-(k>0?0:0),170,0); }
  if(lt>0.95) s+=noRing(350,1195,110,seg(lt,0.95,1.5));
  if(lt>1.2) s+=label(350,1050,"round slices",-4,52);
  if(lt>1.9) s+=label(700,1050,'strips',-4,56)+check(820,1090,seg(lt,1.9,2.4));
  return s;},
 (lt,t)=>{ // step 1: in half, step 2: lengthways
  const h=seg(lt,0.2,0.7), l=seg(lt,1.0,1.6), g=50*E(h);
  let s=board(540,1250,660);
  if(l<=0){ s+=sausage(440-g,1180,200,0)+sausage(640+g,1180,200,0); }
  else { for(const xx of [440-g,640+g]) for(let i=0;i<2;i++) s+=strip(xx,1166+28*i+(i?1:-1)*12*E(l),196,0); }
  s+=step(260,990,1,'in half',seg(lt,0.4,0.7))+step(260,1062,2,'down its length',seg(lt,1.2,1.5));
  return s;},
 (lt,t)=>{ // whole nuts and popcorn: 'no' rings; chopped flakes: check
  let s=board(540,1250,660)+`<g transform="translate(390 1180) scale(1.0) translate(-330 -1180)">`+nut(250,1170,-20)+nut(320,1200,30)+popcorn(410,1170)+`</g>`;
  s+=noRing(390,1180,130,seg(lt,0.2,0.9));
  s+=`<g opacity="${seg(lt,0.9,1.3)}">`+`<g transform="translate(760 1190) scale(1.4) translate(-780 -1190)">`+flakes(780,1190)+`</g>`+`</g>`;
  if(lt>1.3) s+=label(760,1050,'chopped ✓',-4,56);
  return s;},
 (lt,t)=>{ // Do this: toddler with strips on the tray
  const eat=0.5-0.5*Math.cos(Math.PI*2*seg(lt,0.6,2.2));
  let tray='';for(let i=0;i<4;i++) tray+=strip(450+i*62,1262,64,-14+i*10);
  let s=highChair(540,1250,t,eat,tray);
  if(lt>2.3) s+=hearts(t,860,1180);
  return `<g transform="translate(540 1284) scale(.7) translate(-540 -1270)">`+s+`</g>`;},
];
SCN.water=[
 (lt,t)=>{ // empty tub: water rises to the 5 cm mark on a ruler
  const lv=70*EIO(seg(lt,0.2,1.1));
  let s=tub(t,lv,ruler(TX-250,1))+duck(TX+240,WL-lv-10,t);
  if(lt>1.1){ s+=`<path d="M${TX-210} ${WL-70} H${TX+330}" stroke="#D9497A" stroke-width="6" stroke-dasharray="4 14" stroke-linecap="round"/>`+label(TX+20,WL-100,'5 cm (2 in)',-4,70);}
  return s;},
 (lt,t)=>{ // baby in the bath; the parent's hand stays; the phone rings: it can wait
  let s=tub(t,70,bathBaby(TX-40,WL-40,t,false))+adultArm(TX+62,WL-62,E(seg(lt,0.0,0.4)));
  s+=phoneR(925,940,t,seg(lt,0.5,0.8)*(1-seg(lt,1.9,2.2)));
  if(lt>0.9&&lt<2.0) s+=label(640,905,'the phone can wait',-5,56);
  if(lt>2.0) s+=label(760,950,'right there ✓',-5,56);
  return s;},
 (lt,t)=>{ // bath seat: not a safety device; the hand stays
  let s=tub(t,70,bathBaby(TX-40,WL-90,t,true))+adultArm(TX+62,WL-112,1);
  if(lt>0.5) s+=label(TX-280,TRIM-50,'bath seat',-4,54);
  if(lt>1.2) s+=label(760,950,'hand stays ✓',-5,56);
  return s;},
 (lt,t)=>{ // Do this: plug out, water swirls away, check, towel
  const lv=70*(1-EIO(seg(lt,0.5,2.2)));
  let s=towelH(170,1030)+tub(t,lv,plug(TX+200,seg(lt,0.1,0.5)))+duck(TX-80,WL-lv-10,t)+swirl(TX+200,t,seg(lt,0.5,0.8)*(1-seg(lt,2.0,2.3)));
  if(lt>2.2) s+=check(TX+130,WL-170,seg(lt,2.2,2.7))+label(TX-40,WL-150,'empty',-4,64);
  return s;},
];
function draw(t){
 T=t; const S=SPEC, starts=S.starts, n=S.durs.length; let i=0; for(let k=0;k<n;k++) if(t>=starts[k]) i=k;
 let lt=t-starts[i]; if(S.cover){i=S.coverBeat; lt=S.coverLt;}
 let svg=(S.scene=='water')?bathBG(t):skyBG(t).replace(/1320/g,'1440').replace(/1340/g,'1460');
 const pop=(!S.cover&&i>0)?0.94+0.06*E(seg(lt,0,0.3)):1;
 const cam=pop*(S.scene=='water'?1.15:1.55)*(1+0.03*seg(lt,0,S.durs[i])), CY=(S.scene=='water'?1277:1279);
 svg+=`<g transform="translate(540 ${CY}) scale(${cam}) translate(-540 -1180)">`+SCN[S.scene][i](lt,t)+`</g>`;
 document.getElementById('art').innerHTML=svg;
 for(let k=0;k<n;k++){const el=document.getElementById('b'+k); if(!el) continue; let op=0, y=0;
  if(!S.cover&&k==i){ op=1; if(i>0){const p=E(seg(lt,0.0,0.22)); y=24*(1-p);} }
  el.style.opacity=op; el.style.transform=`translateY(${y}px)`;}
 for(let k=0;k<n;k++){const c=document.getElementById('c'+k); if(c) c.style.opacity=(!S.cover&&k==i)?(i==0?(t<0.3?0:Math.min(1,(t-0.3)/0.2)):1):0;}
 const last=(!S.cover&&i==n-1);
 const f=document.getElementById('follow'); if(f){const p=last?E(seg(lt,FOLLOW_AT,FOLLOW_AT+0.4)):0; f.style.opacity=p; f.style.transform=`translateY(${30*(1-p)}px)`;}
 const q=document.getElementById('part2'); if(q){const p=last?E(seg(lt,0.5,0.9)):0; q.style.opacity=p; q.style.transform=`translateY(${24*(1-p)}px) rotate(-2deg)`;}
}
"""


def html(spec, cover=None):
    T = ""
    for k, b in enumerate(spec["beats"]):
        inner = f'<div class="hand" style="position:absolute;left:90px;width:900px;top:{b.get("ky", 330)}px;font-size:66px;color:{KICK}">{b["kick"]}</div>'
        inner += K.dual(b["head"], F, cls="S fit", style=f"position:absolute;left:90px;width:900px;top:{b.get('hy', 415)}px;white-space:nowrap;font-size:{b.get('fs', 130)}px;color:{INK}")
        if b.get("sub"):
            inner += (f'<div class="lora" style="position:absolute;left:70px;width:940px;top:{b.get("sy", 730)}px;font-size:{b.get("ss", 46)}px;'
                      f'line-height:1.2;text-align:center;color:{INK}">{b["sub"]}</div>')
        T += f'<div id="b{k}" style="position:absolute;left:0;top:0;width:{W}px;height:1000px;opacity:0;z-index:4">{inner}</div>'
        T += f'<div id="c{k}" style="position:absolute;left:0;right:0;top:1522px;text-align:center;opacity:0;z-index:4"><span class="chipf" style="font-size:28px">{b["chip"]}</span></div>'
    follow = (f'<div id="follow" style="position:absolute;left:0;right:0;top:{spec.get("follow_y", 800)}px;text-align:center;opacity:0;z-index:5">'
              f'<span style="display:inline-block;max-width:900px;padding:16px 36px;border-radius:40px;background:{INK};color:#FFF8EE;font:600 46px/1.25 Poppins">{spec["follow"]}</span></div>')
    part2 = ""
    if spec.get("part2"):
        part2 = (f'<div id="part2" style="position:absolute;left:60px;width:960px;top:{spec.get("part2_y", 700)}px;text-align:center;opacity:0;z-index:6">'
                 f'<span style="display:inline-block;padding:8px 34px 12px;background:#FFE08A;border-radius:14px;box-shadow:0 6px 0 rgba(107,59,90,.18);'
                 f'font-family:\'Caveat Brush\';font-size:68px;line-height:1.05;color:#B23A62">{spec["part2"]}</span></div>')
    tag = ""
    if spec.get("tag"):
        tag = (f'<div style="position:absolute;left:90px;top:{spec.get("tag_y", 250)}px;z-index:6"><span style="display:inline-block;padding:8px 24px;border-radius:99px;'
               f'background:#D9497A;color:#FFF8EE;font:600 30px Poppins;letter-spacing:.06em">{spec["tag"]}</span></div>')
    bg = (f'<div style="position:absolute;inset:0">{RS.sky(W, H, "afternoon", horizon=0.8)}</div>' if spec["scene"] != "water" else "")
    body = (bg + f'<svg id="art" style="position:absolute;left:0;top:0;z-index:2" width="{W}" height="{H}" viewBox="0 0 {W} {H}"></svg>'
            + T + tag + part2 + follow + K.stamp(B, 924, 196, size=110, rot=-10).replace('class="stamp" style="', 'class="stamp" style="z-index:5;')
            + f"<script>const FOLLOW_AT={spec.get('follow_at', 1.0)};\n{RS.JS}</script>")
    return RS.page(W, H, body)


SPEC_GRAPES = dict(
    out="lf-reel-1101-grapes-in-4", music=LIB / "v4/lf-x-sunny-bounce.mp3", scene="grapes", follow=FOLLOW, follow_y=820,
    part2="Part 2 tomorrow, 7 pm.", part2_y=700, follow_at=1.2, garments=["none"] * 4,
    durs=[6 * BB, 5 * BB, DROP_BB - 11 * BB, 14.3 - DROP_BB],
    beats=[
        dict(kick="toddler eating grapes?", head="Cut each grape / *into 4.*", sub="Round foods are the easiest to choke on.", fs=136, sy=730, ss=50, chip="NHS · AAP HealthyChildren.org"),
        dict(kick="same for", head="Cherry tomatoes / *and berries.*", sub="Quarters: 4 small pieces each.", fs=130, sy=730, ss=50, chip="NHS · Preparing food safely"),
        dict(kick="and", head="Apple and melon: / *slices, not chunks.*", fs=118, chip="NHS · Preparing food safely"),
        dict(kick="Do this:", head="Tonight: cut the / *grapes into 4.*", fs=130, chip="NHS · AAP HealthyChildren.org"),
    ])

SPEC_SAUSAGE = dict(
    out="lf-reel-1102-sausage-strips", music=LIB / "v4/lf-x-giggle-pop.mp3", scene="sausage", follow=FOLLOW, follow_y=720,
    tag="PART 2 · CUTTING FOOD", follow_at=0.0, garments=["none"] * 4,
    durs=[8 * BG, 6 * BG, 6 * BG, 14.3 - 20 * BG],
    beats=[
        dict(kick="sausage for a toddler?", head="Strips, not / *round slices.*", sub="Round shapes are the riskiest.", fs=140, sy=730, ss=50, chip="NHS · Preparing food safely"),
        dict(kick="how to cut it", head="Cut it in half, then cut / *each half down its length.*", sub="Then short strips, as thin as you can.", fs=110, sy=730, ss=50, chip="NHS · Preparing food safely"),
        dict(kick="and one more", head="Kids under 5: / *no whole nuts, / no popcorn.*", sub="Chop nuts up small instead.", fs=136, sy=850, ss=50, chip="NHS · Preparing food safely"),
        dict(kick="Do this:", head="Next sausage: / *cut it lengthways.*", fs=124, chip="NHS · AAP HealthyChildren.org"),
    ])

SPEC_WATER = dict(
    out="lf-reel-1103-5cm-water", music=LIB / "v4/lf-x-tiny-parade.mp3", scene="water", follow=FOLLOW, follow_y=720,
    follow_at=1.0, garments=["none"] * 4,
    durs=[6 * BP, 5 * BP, DROP_BP - 11 * BP, 14.4 - DROP_BP],
    beats=[
        dict(kick="Bath time? Stay the whole time.", head="Babies can drown / *in 5 cm of water.*", sub="That's 2 inches. And it's often silent.", fs=118, sy=730, ss=50, chip="NHS · Baby and toddler safety"),
        dict(kick="so at bath time", head="Stay with them / *the whole time.*", sub="Never leave them, even for a moment.", fs=130, sy=730, ss=50, chip="NHS · Baby and toddler safety"),
        dict(kick="the catch", head="A bath seat isn't / *a safety device.*", sub="You still stay right there.", fs=124, sy=730, ss=50, chip="NHS · Baby and toddler safety"),
        dict(kick="Do this:", head="Bath done? / *Empty it right away.*", fs=124, chip="NHS · Baby and toddler safety"),
    ])

SPECS = {"grapes": SPEC_GRAPES, "sausage": SPEC_SAUSAGE, "water": SPEC_WATER}

# =====================================================================================================================
# Covers (dedicated, 2x)
# =====================================================================================================================
BLOBS = S27.BLOBS
CJS = None


def _cover(body_html, art_js):
    return RS.page(W, H, body_html + f"<script>{RS.JS}\nT=0;{art_js}</script>")


def cover_grapes_html():
    """Ep.01 reframe 'Instead of... / Try...' (style #7, quiet): two stacked cards, a whole grape vs the grape in 4."""
    card = ('<div style="position:absolute;left:90px;width:900px;top:{y}px;height:{h}px;border-radius:36px;background:{bg};'
            'box-shadow:0 14px 0 rgba(107,59,90,.12);border:5px solid #6B3B5A"></div>'
            '<div class="hand" style="position:absolute;left:140px;top:{ly}px;font-size:66px;color:#B23A62">{lab}</div>'
            '<div class="lora" style="position:absolute;left:140px;top:{ty}px;font-size:84px;font-weight:700;color:#3A1F3D;line-height:1.05">{txt}</div>')
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4,#FFEFD8)"></div>'
            + BLOBS.format(a="#FFD6E3", b="#FFE27E", c="#D7E8CB") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:300px;font-size:70px;color:{KICK}">toddler eating grapes?</div>'
            + K.dual("Cut each grape / *into 4.*", F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:385px;white-space:nowrap;font-size:140px;color:{INK}")
            + card.format(y=720, h=300, bg="#FFFDF7", ly=745, lab="instead of…", ty=835, txt="a whole grape")
            + card.format(y=1070, h=330, bg="#FCE5EB", ly=1095, lab="try…", ty=1185, txt="4 small pieces")
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:3" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    art = ("document.getElementById('art').innerHTML=grape(820,880,1.15)+noRing(820,880,100,1)"
           "+grapeCut(790,1240,1,1,0);")
    return _cover(body, art)


def cover_sausage_html():
    """Original simple template 'compare' (style #8, quiet): two cream panels, round slices (no) vs short strips (check)."""
    panel = ('<div style="position:absolute;left:{x}px;top:760px;width:440px;height:600px;border-radius:30px;background:{bg};border:5px solid #6B3B5A"></div>'
             '<div style="position:absolute;left:{x}px;width:440px;top:1260px;text-align:center;font:700 52px Poppins;color:#3A1F3D">{txt}</div>')
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFB59E,#FF9C82)"></div>'
            + BLOBS.format(a="#FFD3AE", b="#FFE27E", c="#FFC9D6") + '<div class="grain" style="opacity:.3"></div>'
            + '<div style="position:absolute;left:90px;top:240px"><span style="display:inline-block;padding:8px 24px;border-radius:99px;background:#D9497A;color:#FFF8EE;font:600 30px Poppins;letter-spacing:.06em">PART 2 · CUTTING FOOD</span></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:320px;font-size:70px;color:#7A2149">sausage for a toddler?</div>'
            + K.dual("Strips, not / *round slices.*", F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:405px;white-space:nowrap;font-size:150px;color:{INK}")
            + panel.format(x=80, bg="#FFFDF7", txt="round slices") + panel.format(x=560, bg="#FCE5EB", txt="short strips")
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:3" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    art = ("let s='';for(let i=0;i<3;i++)for(let j=0;j<2;j++) s+=coin(220+i*80,960+j*110,1.2);"
           "s+=noRing(300,1015,165,1);for(let i=0;i<4;i++) s+=strip(780,940+i*56,260,0);s+=check(930,860,1);"
           "document.getElementById('art').innerHTML=s;")
    return _cover(body, art)


def cover_water_html():
    """Kinetic big text (style #5, loud): a giant '5 cm' with the water line drawn through it, a duck and a ruler."""
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4,#FFE9D6)"></div>'
            + BLOBS.format(a="#CFE3F6", b="#FFD6E3", c="#FFE27E") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:300px;font-size:76px;color:{KICK}">bath time</div>'
            + '<div class="lora" style="position:absolute;left:0;width:1080px;top:420px;text-align:center;font-weight:700;font-size:420px;line-height:1;color:#D9497A;text-shadow:10px 10px 0 #FFC9D6;z-index:2">5 cm</div>'
            + '<div style="position:absolute;left:0;width:1080px;top:690px;height:180px;background:linear-gradient(180deg,rgba(156,196,236,.78),rgba(156,196,236,.9));z-index:3"></div>'
            + f'<div class="lora" style="position:absolute;left:60px;width:960px;top:930px;text-align:center;font-weight:700;font-size:78px;line-height:1.1;color:{INK};z-index:4">Babies can drown<br>in this much water.</div>'
            + f'<div class="hand" style="position:absolute;left:60px;width:960px;top:1150px;text-align:center;font-size:64px;color:{KICK};z-index:4">stay with them the whole bath ♡</div>'
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:3" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    art = "document.getElementById('art').innerHTML=duck(880,700,0.6)+`<path d='M0 690 Q270 676 540 690 T1080 690' stroke='#FFFFFF' stroke-width='8' fill='none'/>`;"
    return _cover(body, art)


COVERS = {"grapes": cover_grapes_html, "sausage": cover_sausage_html, "water": cover_water_html}


def encode(fdir, total, music, pops, out_mp4):
    """reel_story.encode with -nostdin (studio rule)."""
    a = RS.SCR / f"{out_mp4.stem}.wav"
    pop = LIB / "sfx-x-sticker-pop.mp3"
    inputs = ["-i", str(music)]
    filt = [f"[0:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.05,afade=t=out:st={total-0.6:.3f}:d=0.6[m]"]
    mix = ["[m]"]
    for k, (pt, vol) in enumerate(pops):
        inputs += ["-i", str(pop)]
        filt.append(f"[{k+1}:a]volume={vol},adelay={int(pt*1000)}|{int(pt*1000)}[p{k}]")
        mix.append(f"[p{k}]")
    filt.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[o]")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[o]", "-ar", "48000", "-ac", "2", str(a)], check=True)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-threads", "1", "-framerate", str(FPS), "-i", str(fdir / "%04d.jpg"), "-i", str(a),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "slow", "-crf", "18", "-profile:v", "high",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out_mp4)], check=True)
    shutil.rmtree(fdir)


def use(key):
    RS.JS = S27.BASE_JS + S27.JS_TEETH + JS
    RS.html = html
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
        encode(fdir, total, s["music"], pops, out)
        print(out, round(total, 2), flush=True)

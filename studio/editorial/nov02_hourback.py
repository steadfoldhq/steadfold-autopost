#!/usr/bin/env python3
"""Hourback Reels built Mon Nov 2 2026 by the Hourback maker (Social studio).

    python3 studio/editorial/nov02_hourback.py interview|packing             # mp4 + dedicated cover -> media/studio-nov02/hourback/
    python3 studio/editorial/nov02_hourback.py interview --still 0,2.5,5      # stills sheet in the scratch dir (review)
    python3 studio/editorial/nov02_hourback.py interview --cover-only

interview = hb-reel-1104-interview-9am (Wed Nov 4, 7 pm). Drawn evening bedroom: an ironed shirt on a hanger, a desk
            calendar 'TOMORROW 9 am interview' (= the deadline you can feel) and an empty interviewer's clipboard. A made-up
            job posting flies onto the clipboard and Claude's REAL 5 questions land one at a time (word for word; Q2
            shortened, marked …). Beat 2 = its 'Really checking' line for the cash-drawer question, word for word.
            Real run: studio/editorial/hb-nov02-run-interview.txt. Cover: reframe 'Instead of… Ask…' (style 7, QUIET).
packing   = hb-reel-1105-flight-6am (Thu Nov 5, 7 pm). Drawn night floor: an empty open carry-on with a '6 am flight' tag.
            Claude's REAL packing list, room by room (4 room tabs; items word for word; drawn items drop in the case).
            Beat 2 = its 'wear the hiking shoes on the plane' line, word for word. Real run: hb-nov02-run-packing.txt.
            Cover: one giant word (style 4 look, LOUD, drawn object instead of a photo).

Extends studio/editorial/nov01_hourback.py (and through it oct28_hourback.py) by import: its JS engine, html(), render(),
stills(). New scenes are appended to the JS; module paths/specs are pointed at Nov 2. No shared kit or older script edited.
Both Reels are standalone (no Part 2 promise).
"""
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
sys.dont_write_bytecode = True
import nov01_hourback as N1  # noqa: E402  (sets up B = oct28_hourback with the Nov 1 JS + html override)

B = N1.B
B.OUT = REPO / "media/studio-nov02/hourback"
B.SCR = Path("/tmp/claude-0/nov02-hourback")
LIB = B.LIB

JS_NOV02 = r"""
// =============================================== shared Nov 2 helpers
function wrapQ(lines,x,y,size,lh,col,fam){return lines.map((l,i)=>`<text x="${x}" y="${y+i*lh}" font-family="${fam||'DM Serif Display'}" font-size="${size}" fill="${col||INK}">${esc(l)}</text>`).join('');}

// =============================================== scene: interview tomorrow at 9 am (Nov 4)
function hangerShirt(x,y,t){ // (x,y) = hook on the wall
 const sw=3*Math.sin(t*1.6);
 return `<g transform="translate(${x} ${y}) rotate(${sw})"><circle cx="0" cy="0" r="9" fill="${OL}"/>
  <path d="M0 0 q0 -22 16 -22 q16 0 16 16 q0 12 -14 18 L0 30" stroke="${OL}" stroke-width="6" fill="none" stroke-linecap="round"/>
  <path d="M0 30 L-150 92 H150Z" fill="none" stroke="${OL}" stroke-width="8" stroke-linejoin="round"/>
  <path d="M-62 60 L-150 96 L-176 196 L-128 206 L-118 150 L-118 300 H118 L118 150 L128 206 L176 196 L150 96 L62 60 Q0 86 -62 60Z" fill="#FFFFFF" ${o}/>
  <path d="M-62 60 L-22 120 L0 84 L22 120 L62 60" fill="#FFFFFF" ${o}/>
  <path d="M0 84 L-18 104 L0 122 L18 104Z M-6 120 L-22 250 L0 278 L22 250 L6 120Z" fill="${INDI}" ${o} stroke-width="4"/>
  ${[150,190,230,270].map(yy=>`<circle cx="34" cy="${yy}" r="5" fill="${PERI}" stroke="${OL}" stroke-width="2"/>`).join('')}</g>`;}
function deskCal(x,y,rot,glow){ // tear-off desk calendar: TOMORROW / 9 am / interview
 return `<g transform="translate(${x} ${y}) rotate(${rot})">
  ${glow>0?`<circle cx="120" cy="120" r="${170+30*glow}" fill="url(#glow)" opacity="${0.9*glow}"/>`:''}
  <rect x="8" y="12" width="240" height="236" rx="18" fill="rgba(42,29,71,.16)"/>
  <rect x="0" y="0" width="240" height="236" rx="18" fill="#FFFFFF" ${o}/>
  <path d="M0 18 Q0 0 18 0 H222 Q240 0 240 18 V66 H0Z" fill="${ACC}" ${o}/>
  <text x="120" y="48" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="32" fill="#FFFFFF" letter-spacing="2">TOMORROW</text>
  <text x="120" y="150" text-anchor="middle" font-family="DM Serif Display" font-size="92" fill="${INK}">9 am</text>
  <text x="120" y="208" text-anchor="middle" font-family="Caveat Brush" font-size="46" fill="${INDI}">interview</text>
  <rect x="58" y="-14" width="14" height="30" rx="7" fill="${OL}"/><rect x="168" y="-14" width="14" height="30" rx="7" fill="${OL}"/></g>`;}
const IQ=[["“Tell me about a time you dealt","with an upset customer.”"],
          ["“How would you handle a team","member who shows up late…”"],
          ["“Can you reliably open at 6 am","and work weekends?”"],
          ["“Your cash drawer is $20 short","at close. What do you do?”"],
          ["“How would you train a brand-new","hire on their first shift?”"]];
const QT=[0.95,1.9,2.85,3.8,4.75];           // when each question lands (s after beat 1 starts)
const CB_X=70, CB_Y=1125, CBW=940, CBH=400;
function clipboard(t,st,beat,lt){
 let s=`<rect x="12" y="16" width="${CBW}" height="${CBH}" rx="26" fill="rgba(42,29,71,.16)"/><rect x="0" y="0" width="${CBW}" height="${CBH}" rx="26" fill="#D9A867" ${o}/>`;
 s+=`<rect x="26" y="34" width="${CBW-52}" height="${CBH-56}" rx="8" fill="#FFFFFF" stroke="${OL}" stroke-width="4"/>`;
 s+=`<rect x="${CBW/2-120}" y="-26" width="240" height="66" rx="16" fill="#B9B4D8" ${o}/><rect x="${CBW/2-60}" y="-10" width="120" height="22" rx="11" fill="${OL}"/>`;
 // which question is showing
 let k=-1; if(beat==1){ for(let i=0;i<5;i++) if(lt>=QT[i]) k=i; } else if(beat>=2) k=3;
 if(k<0){ // empty: header + dashed space
   s+=`<text x="58" y="112" font-family="Caveat Brush" font-size="56" fill="${INDI}">Their questions:</text>`;
   const e=beat==0?1:1-seg(lt,0.6,0.9);
   s+=`<rect x="58" y="140" width="${CBW-116}" height="${CBH-200}" rx="16" fill="none" stroke="${INDI}" stroke-width="4" stroke-dasharray="14 14" opacity="${e*(0.55+0.35*Math.sin(t*5))}"/>`;
   s+=`<text x="${CBW/2}" y="${CBH/2+90}" text-anchor="middle" font-family="DM Serif Display" font-size="110" fill="${INDI}" opacity="${e*0.5}">?</text>`;
   return s; }
 const a=beat==1?st[1]+QT[k]:st[2], p=E(seg(t,a,a+0.12));
 s+=`<text x="58" y="104" font-family="Poppins" font-weight="700" font-size="42" fill="${INDI}">Question ${k+1} of 5</text>`;
 for(let i=0;i<5;i++) s+=`<circle cx="${620+i*56}" cy="90" r="17" fill="${i<=k?SUN:'#FFFFFF'}" stroke="${OL}" stroke-width="3"/>`;
 if(beat>=2){ const hk=E(seg(t,st[2]+0.25,st[2]+0.6)); s+=`<rect x="48" y="${168}" width="${(CBW-96)*hk}" height="160" rx="14" fill="${SUN}" opacity=".45"/>`; }
 s+=`<g opacity="${p}" transform="translate(${36*(1-p)} 0)">`+wrapQ(IQ[k],58,232,52,76)+`</g>`;
 if(beat==3) s+=check(CBW-90,96,seg(lt,0.2,0.8));
 return s;}
function postingNote(k,fly){ // the made-up job posting; fly 0..1 -> onto the clipboard
 const x0=60, y0=712, tx=x0+(CB_X+CBW/2-260-x0)*E(fly), ty=y0+(CB_Y+120-y0)*E(fly), sc=1-0.7*E(fly);
 const inner=label(26,58,'job posting we made up:',-2,44,ACC,'start')
  +`<text x="26" y="128" font-family="DM Serif Display" font-size="50" fill="${INK}">Shift Supervisor, bakery café</text>`
  +textLines(26,188,["open at 6 am · lead a team of 4","count the cash drawer · train new staff"],44,50,OL,'Caveat',700);
 return `<g opacity="${k*(1-seg(fly,.8,1))}" transform="translate(${tx} ${ty}) scale(${sc})">`+sticky(0,0,820,262,-2,'#FFE7A0',inner,40*(1-k))+`</g>`;}
function interviewScene(beat,lt,t,S){
 const st=S.starts; let s='';
 const glow=beat==3?E(seg(lt,0.05,0.6)):0;
 s+=tableTop(1050);
 // wall: shirt on a hook (left), calendar on the desk (right)
 s+=hangerShirt(250,700,t);
 s+=deskCal(770,770,4,glow);
 if(beat==1){ const k=E(seg(lt,0.0,0.12)), fl=seg(lt,0.55,0.95); s+=postingNote(k,fl); }
 if(beat==2){ const k=E(seg(t,st[2]+0.0,st[2]+0.1));
   const inner=label(24,56,"why they ask it, word for word:",-2,44,ACC,'start')+textLines(24,124,["Really checking: honesty and process.","Recount, document, report, and","don't cover it up or guess."],50,56,OL,'Caveat',700);
   s+=`<g opacity="${k}">`+sticky(40,712,760,270,-2,'#FFE7A0',inner,(1-k)*120)+`</g>`; }
 s+=`<g transform="translate(${CB_X} ${CB_Y}) rotate(-1)">`+clipboard(t,st,beat,lt)+`</g>`;
 if(beat==3) s+=confetti(880,860,seg(lt,0.05,1.2),t);
 return s;}
SCENES.interview=interviewScene;

// =============================================== scene: flight at 6 am, not packed (Nov 5)
const ROOMS=["Bedroom","Bathroom","Kitchen","Front door"];
const RL=[["Suit, dress shirt, tie or pocket square, belt","Rain jacket (wear it on the plane)"],
          ["Toothbrush, toothpaste, deodorant","Liquids in a clear bag, 100 ml max each"],
          ["Reusable water bottle (empty for security)","Snacks for the hike and the flight"],
          ["ID or passport, wallet, keys","Boarding pass","Compact umbrella"]];
const RT=[1.35,2.55,3.75,4.95];             // when each room lands (s after beat 1 starts)
function nightWindow(x,y,t){let st='';[[60,60],[170,40],[250,120],[110,150]].forEach((p,i)=>{st+=sparkle(p[0],p[1],0.3+0.12*Math.sin(t*3+i),0.9);});
 return `<g transform="translate(${x} ${y})"><rect x="0" y="0" width="330" height="250" rx="18" fill="#3A2240" ${o}/>
  <circle cx="250" cy="70" r="40" fill="#FFF3C4" stroke="${OL}" stroke-width="4"/><circle cx="268" cy="60" r="34" fill="#3A2240"/>${st}
  <path d="M165 0 V250 M0 125 H330" stroke="${OL}" stroke-width="7"/><rect x="-14" y="242" width="358" height="24" rx="8" fill="${CREAM}" ${o}/></g>`;}
function alarm(x,y,t,ring){const sh=ring*4*Math.sin(t*40);
 return `<g transform="translate(${x+sh} ${y})"><path d="M-62 -58 l-22 -22 M62 -58 l22 -22" stroke="${OL}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="-52" cy="-70" r="24" fill="${SUN}" ${o}/><circle cx="52" cy="-70" r="24" fill="${SUN}" ${o}/>
  <circle r="80" fill="${CREAM}" ${o} stroke-width="7"/><text x="0" y="16" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="44" fill="${INK}">4:30</text>
  <text x="0" y="52" text-anchor="middle" font-family="Caveat Brush" font-size="30" fill="${ACC}">alarm</text>
  <path d="M-50 70 l-16 24 M50 70 l16 24" stroke="${OL}" stroke-width="9" stroke-linecap="round"/></g>`;}
function boardingPass(x,y,t){return `<g transform="translate(${x} ${y+3*Math.sin(t*2)}) rotate(-4)"><rect x="8" y="12" width="420" height="210" rx="18" fill="rgba(42,29,71,.16)"/>
  <rect x="0" y="0" width="420" height="210" rx="18" fill="#FFFFFF" ${o}/><path d="M0 18 Q0 0 18 0 H402 Q420 0 420 18 V62 H0Z" fill="${INDI}" ${o}/>
  <text x="24" y="44" font-family="Poppins" font-weight="700" font-size="28" fill="#FFFFFF" letter-spacing="2">BOARDING PASS</text>
  <path d="M310 0 V210" stroke="${OL}" stroke-width="3" stroke-dasharray="8 8"/>
  <text x="24" y="118" font-family="Poppins" font-weight="700" font-size="40" fill="${INK}">to Vancouver</text>
  <text x="24" y="182" font-family="Poppins" font-weight="700" font-size="52" fill="${ACC}">6:00 am</text>
  <text x="365" y="150" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="30" fill="${INDI}" transform="rotate(-90 365 140)">YVR</text></g>`;}
const SC_X=110, SC_Y=1200, SCW=720, SCH=250;
function suitcase(lid,t){ // open carry-on, lid 0 = open (standing up behind), 1 = closed
 const lh=150*(1-lid);   // lid height when open
 let s=`<g transform="translate(${SC_X} ${SC_Y})">`;
 if(lid<1) s+=`<path d="M10 0 L${SCW-10} 0 L${SCW-40} ${-lh} L40 ${-lh}Z" fill="#7B73D6" ${o}/><path d="M40 ${-lh*0.55} H${SCW-40}" stroke="#5E54C9" stroke-width="6"/>`;
 s+=`<rect x="0" y="0" width="${SCW}" height="${SCH}" rx="26" fill="${INDI}" ${o}/><rect x="26" y="20" width="${SCW-52}" height="${SCH-46}" rx="14" fill="#3B34A0" stroke="${OL}" stroke-width="4"/>`;
 s+=`<path d="M${SCW/2-70} ${SCH} v18 h140 v-18" stroke="${OL}" stroke-width="8" fill="none"/>`;
 s+=`<circle cx="60" cy="${SCH+6}" r="16" fill="${OL}"/><circle cx="${SCW-60}" cy="${SCH+6}" r="16" fill="${OL}"/>`;
 return s+`</g>`;}
function luggageTag(x,y,t){const sw=5*Math.sin(t*2.2);
 return `<g transform="translate(${x} ${y}) rotate(${-8+sw})"><path d="M0 0 C-10 30 10 50 0 70" stroke="${OL}" stroke-width="5" fill="none"/>
  <g transform="translate(-100 70)"><rect x="6" y="8" width="200" height="120" rx="16" fill="rgba(42,29,71,.16)"/><rect x="0" y="0" width="200" height="120" rx="16" fill="${SUN}" ${o}/>
  <circle cx="100" cy="18" r="8" fill="#FFF8EF" stroke="${OL}" stroke-width="3"/>
  <text x="100" y="66" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="36" fill="${INK}">FLIGHT</text>
  <text x="100" y="106" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="36" fill="${ACC}">6:00 am</text></g></g>`;}
// drawn items that drop into the case
const PK={
 jacket:()=>`<path d="M-50 -84 H50 L120 -54 L134 60 L98 64 L88 0 L84 90 H6 V-60 H-6 V90 H-84 L-88 0 L-98 64 L-134 60 L-120 -54Z" fill="#33304A" ${o}/><path d="M-50 -84 L-6 -30 M50 -84 L6 -30" stroke="#9E98D8" stroke-width="5"/>`,
 rain:()=>`<path d="M-44 -76 L44 -76 L110 -48 L94 40 L66 30 L66 84 H-66 L-66 30 L-94 40 L-110 -48Z" fill="${ORNG}" ${o}/><path d="M-44 -76 Q0 -40 44 -76 M0 -60 V84" stroke="${OL}" stroke-width="4" fill="none"/>`,
 brush:()=>`<rect x="-100" y="-12" width="200" height="24" rx="12" fill="${PERI}" ${o}/><rect x="56" y="-34" width="44" height="24" rx="4" fill="#FFFFFF" ${o} stroke-width="4"/>`,
 bag:()=>`<rect x="-80" y="-60" width="160" height="120" rx="12" fill="rgba(255,255,255,.75)" ${o}/><path d="M-80 -36 H80" stroke="#6E8FC9" stroke-width="6"/><rect x="-50" y="-10" width="36" height="56" rx="8" fill="${PEACH}" stroke="${OL}" stroke-width="3"/><rect x="6" y="0" width="30" height="46" rx="8" fill="${SUN}" stroke="${OL}" stroke-width="3"/>`,
 bottle:()=>`<rect x="-34" y="-90" width="68" height="180" rx="26" fill="#6E8FC9" ${o}/><rect x="-22" y="-112" width="44" height="30" rx="8" fill="${OL}"/>`,
 snack:()=>`<path d="M-70 -50 L70 -50 L60 50 L-60 50Z" fill="${SUN}" ${o}/><path d="M-70 -50 l14 -14 l14 14 l14 -14 l14 14 l14 -14 l14 14 l14 -14 l14 14 l14 -14 l14 14" stroke="${OL}" stroke-width="4" fill="none"/>`,
 passport:()=>`<rect x="-60" y="-80" width="120" height="160" rx="10" fill="#B23A62" ${o}/><circle cx="0" cy="-10" r="30" fill="none" stroke="${SUN}" stroke-width="5"/>`,
 umbrella:()=>`<path d="M-30 -110 L30 -110 L22 90 Q0 110 -22 90Z" fill="${INDI}" ${o}/><path d="M0 90 V130 q0 20 -20 20" stroke="${OL}" stroke-width="8" fill="none" stroke-linecap="round"/>`,
};
const PKP=[[['jacket',300,-6],['rain',560,8]],[['brush',360,-20],['bag',620,10]],[['bottle',330,70],['snack',600,-12]],[['passport',300,-14],['umbrella',560,62]]];
function pkItem(n,x,y,r,s){return `<g transform="translate(${x} ${y}) rotate(${r}) scale(${s})">${PK[n]()}</g>`;}
function boots(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})">${[0,1].map(i=>`<g transform="translate(${i*120} ${i*6})"><path d="M-40 -110 H20 V-10 Q60 -10 70 20 V40 H-46 Z" fill="#8A5A3B" ${o}/><path d="M-46 30 H70" stroke="${OL}" stroke-width="10"/><path d="M-30 -80 h40 M-30 -56 h40 M-30 -32 h40" stroke="${SUN}" stroke-width="5"/></g>`).join('')}</g>`;}
function roomTabs(k,ink){let s=''; const W0=210, G=20, x0=(1080-(4*W0+3*G))/2;
 ROOMS.forEach((r,i)=>{const x=x0+i*(W0+G), on=i==k, done=i<k;
  s+=`<rect x="${x}" y="0" width="${W0}" height="66" rx="33" fill="${on?SUN:done?'#FFFFFF':'rgba(255,255,255,.55)'}" ${o} stroke-width="4"/>`;
  s+=`<text x="${x+W0/2}" y="44" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="30" fill="${INK}" opacity="${on||done?1:0.55}">${r}</text>`;
  if(i<3) s+=`<path d="M${x+W0+2} 33 h${G-4}" stroke="${OL}" stroke-width="4" stroke-dasharray="4 4"/>`;});
 return s;}
function roomCard(k,p){ // list card for room k (Claude's lines, word for word)
 const L=RL[k]; let s=`<rect x="10" y="14" width="940" height="290" rx="22" fill="rgba(42,29,71,.14)"/><rect x="0" y="0" width="940" height="290" rx="22" fill="#FFFFFF" ${o}/>`;
 s+=`<g opacity="${p}" transform="translate(${30*(1-p)} 0)"><text x="40" y="70" font-family="DM Serif Display" font-size="56" fill="${INDI}">${ROOMS[k]}</text>`;
 L.forEach((l,i)=>{s+=`<text x="40" y="${148+i*62}" font-family="Caveat" font-weight="700" font-size="52" fill="${PEN}">– ${esc(l)}</text>`;});
 return s+`</g>`;}
function packingScene(beat,lt,t,S){
 const st=S.starts; let s='';
 // floor
 s+=`<rect x="-40" y="1120" width="1160" height="840" fill="#F2C79B" ${o}/><path d="M-40 1140 H1120" stroke="#E0AC7C" stroke-width="10"/>`;
 const lid=beat==3?E(seg(lt,0.1,0.5)):0;
 const cardOut=beat>=2?E(seg(t,st[2],st[2]+0.25)):0;
 if(beat==0||(beat>=2)) { s+=nightWindow(660,700,t); }
 if(beat==0||beat==3){ const bk=beat==3?E(seg(lt,0,0.3)):1; s+=`<g opacity="${bk}">`+boardingPass(60,770,t)+`</g>`; }
 s+=suitcase(lid,t);
 // items inside the case (all rooms up to now)
 const lt1=t-st[1]; let ins='';
 for(let k=0;k<4;k++){ if(beat<1) break; const a=RT[k]+0.2; PKP[k].forEach((it,j)=>{const e=E(seg(lt1,a+j*0.15,a+0.45+j*0.15)); if(e<=0) return;
   const [n,x,r]=it; const ii=k*2+j, tx=SC_X+100+ii*66, ty=SC_Y+118+(ii%2?18:-14); const y=880+(ty-880)*e-120*Math.sin(Math.PI*e);
   ins+=pkItem(n,tx,y,r*(1-e)+r*0.2,0.62+0.2*(1-e)); }); }
 s+=ins;
 if(lid>0) s+=`<g transform="translate(${SC_X} ${SC_Y})" opacity="${lid}"><rect x="0" y="0" width="${SCW}" height="${SCH}" rx="26" fill="#7B73D6" ${o}/><path d="M30 40 H${SCW-30}" stroke="${OL}" stroke-width="5" stroke-dasharray="10 6"/><rect x="${SCW-90}" y="28" width="34" height="26" rx="6" fill="${SUN}" stroke="${OL}" stroke-width="3"/><path d="M40 120 H${SCW-40} M40 170 H${SCW-40}" stroke="#5E54C9" stroke-width="6"/></g>`;
 // boots: in the case in beat 1 (from the bedroom), hop out to the floor on beat 2
 if(beat>=1){ const bo=beat>=2?E(seg(t,st[2]+0.3,st[2]+0.9)):0; const bin=E(seg(lt1,RT[0]+0.6,RT[0]+1.0));
   const bx=SC_X+610+(900-SC_X-610)*bo, by=SC_Y+150+(SC_Y+210-SC_Y-150)*bo-140*Math.sin(Math.PI*bo);
   if(bin>0) s+=boots(bx-120*(1-bin)*0, by-(1-bin)*300, 0.62);
   if(bo>0.8){ s+=label(960,SC_Y+40,'wear on',-4,54,INK,'middle')+label(960,SC_Y+96,'the plane',-4,54,INK,'middle'); } }
 // room tabs + list card (beat 1)
 if(beat==1||(beat==2&&cardOut<1)){ const k0=E(seg(lt1,RT[0]-0.15,RT[0])); let k=0; for(let i=0;i<4;i++) if(lt1>=RT[i]) k=i;
   const p=E(seg(t,st[1]+RT[k],st[1]+RT[k]+0.12));
   s+=`<g opacity="${k0*(1-cardOut)}" transform="translate(0 ${700-40*(1-k0)})">`+roomTabs(lt1>=RT[0]?k:-1)+`</g>`;
   if(lt1>=RT[0]) s+=`<g opacity="${1-cardOut}" transform="translate(70 790)">`+roomCard(k,p)+`</g>`; }
 if(beat==2){ const k=E(seg(t,st[2]+0.1,st[2]+0.2));
   const inner=label(24,56,"its line, word for word:",-2,44,ACC,'start')+textLines(24,122,["Hiking shoes (wear them on the plane,","since they're the bulkiest pair)"],52,58,OL,'Caveat',700);
   s+=`<g opacity="${k}">`+sticky(60,712,800,210,-2,'#FFE7A0',inner,(1-k)*120)+`</g>`; }
 if(beat==3) s+=`<g transform="translate(${SC_X} ${SC_Y})">`+check(SCW-70,-20,seg(lt,0.4,1.0))+`</g>`;
 return s;}
function tripNote(lt){ // the made-up trip from the real prompt, beat 1 start; flies into the case
 const k=E(seg(lt,0,0.12)), fl=seg(lt,1.0,1.35); if(fl>=1) return '';
 const tx=60+(SC_X+200-60)*E(fl), ty=712+(SC_Y+40-712)*E(fl), sc=1-0.75*E(fl);
 const inner=label(26,58,'trip we made up for this post:',-2,46,ACC,'start')+textLines(26,128,["3 nights in Vancouver, carry-on only","a wedding (I'm wearing a suit), one day hike","and it'll probably rain"],50,58,OL,'Caveat',700);
 return `<g opacity="${k*(1-seg(fl,.8,1))}" transform="translate(${tx} ${ty}) scale(${sc})">`+sticky(0,0,880,260,-2,'#FFE7A0',inner,40*(1-k))+`</g>`;}
SCENES.packing=(beat,lt,t,S)=>packingScene(beat,lt,t,S)+(beat==1?tripNote(lt):'');
"""

B.JS = B.JS + JS_NOV02

SPECS = {
    "interview": dict(
        id="hb-reel-1104-interview-9am", scene="interview", music=LIB / "hb-x-smart-bounce.mp3",
        wall="linear-gradient(180deg,#C2BDF0 0%,#CFCDF5 30%,#E6DFF4 50%,#FFF8EF 54.6%,#FFF8EF 100%)",
        durs=[2.2, 5.7, 3.2, 3.3], follow_at=0.6, follow_y=1016, chip_y=1550,
        beats=[
            dict(kick="", head="Interview at 9 am. / *Haven't prepared.*", fs=124),
            dict(kick="paste the job posting into AI", head="It lists the 5 questions / *they'll likely ask.*", fs=100,
                 sub="Claude's real questions, word for word:"),
            dict(kick="it tells you why they ask", head="Practise the answer / *they're looking for.*", fs=104),
            dict(kick="Do this:", head="Paste the posting. / *Ask for 5 questions.*", fs=104,
                 sub="In ChatGPT, Claude or Gemini."),
        ],
        chip="Real Claude reply · job posting made up for this post",
    ),
    "packing": dict(
        id="hb-reel-1105-flight-6am", scene="packing", music=LIB / "hb-x-ta-da-funk.mp3",
        wall="linear-gradient(180deg,#B9B4EE 0%,#C9CAF5 35%,#E3DDF6 58%,#E3DDF6 100%)",
        durs=[2.2, 6.2, 3.0, 3.0], follow_at=0.5, follow_y=1036, chip_y=1545,
        beats=[
            dict(kick="", head="Flight at 6 am. / *Not packed.*", fs=136),
            dict(kick="tell AI the trip", head="It sorts your list room by room, / *so you walk through once.*", fs=92,
                 sub="Claude's real list, shortened:"),
            dict(kick="it plans for carry-on", head="Wear the bulky shoes / *on the plane.*", fs=110),
            dict(kick="Do this:", head="Ask for a packing list / *sorted by room.*", fs=104,
                 sub="In ChatGPT, Claude or Gemini."),
        ],
        chip="Real Claude reply · trip made up for this post",
    ),
}
B.SPECS = SPECS


if __name__ == "__main__":
    key = sys.argv[1]
    if "--still" in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index("--still") + 1].split(",")]
        print(B.stills(key, ts))
    elif "--full" in sys.argv:
        print(B.full(key, float(sys.argv[sys.argv.index("--full") + 1]), B.SCR / f"{key}-full.png"))
    elif "--cover-only" in sys.argv:
        import nov02_hourback_covers as CV
        print(CV.build(key))
    else:
        print(B.render(key))
        import nov02_hourback_covers as CV
        print(CV.build(key))

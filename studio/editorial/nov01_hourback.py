#!/usr/bin/env python3
"""Hourback Reels built Sun Nov 1 2026 by the Hourback maker (Social studio).

    python3 studio/editorial/nov01_hourback.py toast|cue|tidy            # mp4 + dedicated cover -> media/studio-nov01/hourback/
    python3 studio/editorial/nov01_hourback.py toast --still 0,2.5,5      # stills sheet in the scratch dir (review)
    python3 studio/editorial/nov01_hourback.py toast --cover-only

toast = hb-reel-1101-wedding-toast (Sun Nov 1, 7 pm). Drawn wedding-reception scene (string lights, mic stand, a blank
        index card, 'Toasts at 8 pm' tent card = the deadline you can feel). Three made-up memories fly into the card and
        a drawn hand writes Claude's REAL toast lines in (word for word, shortened, marked …). Beat 2 = Claude's own
        delivery tip, word for word, and the hand draws the pause mark. Real run: studio/editorial/hb-nov01-run-toast.txt.
        Ends 'Part 2 tomorrow, 7 pm.' + follow line (desk Part 2 test). Cover: sticky-note list (style 13, QUIET).
cue   = hb-reel-1102-toast-cue-card (Mon Nov 2, 7 pm), Part 2. Real run: hb-nov01-run-cue.txt (the toast pasted verbatim).
tidy  = hb-reel-1103-guests-30-min (Tue Nov 3, 7 pm). Real run: hb-nov01-run-tidy.txt.

Extends studio/editorial/oct28_hourback.py by import (its JS engine, html(), render(), stills()); new scenes are appended
to its JS and its module paths/specs are pointed at Nov 1. No shared kit is edited.
"""
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
sys.dont_write_bytecode = True
import oct28_hourback as B  # noqa: E402

B.OUT = REPO / "media/studio-nov01/hourback"
B.SCR = Path("/tmp/claude-0/nov01-hourback")
LIB = B.LIB

JS_NEW = r"""
// =============================================== shared Nov 1 helpers
function garland(t,beam){ // string lights across the top; brighter on beam
 let s=''; const yAt=x=>110+80*(1-Math.pow((x-540)/600,2));
 let d='M-20 '+yAt(-20); for(let x=0;x<=1100;x+=20) d+=' L'+x+' '+yAt(x).toFixed(1);
 s+=`<path d="${d}" stroke="${OL}" stroke-width="4" fill="none"/>`;
 const C=[SUN,ORNG,'#FFF3C4',PEACH];
 for(let i=0;i<13;i++){const x=20+i*86, y=yAt(x)+8, tw=0.55+0.45*Math.sin(t*4+i*1.7);
   s+=`<circle cx="${x}" cy="${y+26}" r="${30+14*beam}" fill="url(#glow)" opacity="${(0.35+0.5*beam)*tw}"/>`;
   s+=`<rect x="${x-7}" y="${y-4}" width="14" height="12" rx="3" fill="${INK}"/><ellipse cx="${x}" cy="${y+22}" rx="13" ry="18" fill="${C[i%4]}" stroke="${OL}" stroke-width="3"/>`;}
 return s;}
function flute(x,y,rot,fill,t){ // champagne flute; (x,y) = foot centre
 let b=''; for(let i=0;i<4;i++){const k=(t*0.7+i*0.25)%1; b+=`<circle cx="${-8+i*5}" cy="${-150+90*(1-k)}" r="3.5" fill="#FFFFFF" opacity="${Math.sin(Math.PI*k)}"/>`;}
 return `<g transform="translate(${x} ${y}) rotate(${rot})"><ellipse cx="0" cy="0" rx="46" ry="11" fill="#FFFFFF" ${o} stroke-width="4"/>
  <path d="M0 -4 V-90" stroke="${OL}" stroke-width="6"/>
  <path d="M-30 -230 Q-34 -110 0 -92 Q34 -110 30 -230Z" fill="rgba(255,255,255,.55)" ${o} stroke-width="4"/>
  <path d="M-27 ${-230+70*(1-fill)} Q-30 -112 0 -96 Q30 -112 27 ${-230+70*(1-fill)}Z" fill="${SUN}" opacity=".9"/>${b}
  <path d="M-16 -210 Q-20 -150 -10 -118" stroke="#FFFFFF" stroke-width="6" fill="none" stroke-linecap="round" opacity=".8"/></g>`;}
function micStand(x,y){return `<g transform="translate(${x} ${y})"><path d="M0 0 V-230" stroke="${OL}" stroke-width="10" stroke-linecap="round"/>
  <path d="M0 -230 L-40 -270" stroke="${OL}" stroke-width="8" stroke-linecap="round"/>
  <g transform="translate(-48 -282) rotate(-40)"><rect x="-20" y="-50" width="40" height="70" rx="20" fill="#3B3456" ${o} stroke-width="4"/>
  <path d="M-20 -30 H20 M-20 -14 H20" stroke="#9E98D8" stroke-width="3"/></g></g>`;}
function tent(x,y,lines,rot){return `<g transform="translate(${x} ${y}) rotate(${rot})"><path d="M8 118 L18 0 H210 L222 118Z" fill="rgba(42,29,71,.14)"/>
  <path d="M0 110 L12 0 H200 L212 110Z" fill="#FFFFFF" ${o} stroke-width="4"/>
  ${lines.map((l,i)=>`<text x="106" y="${48+i*44}" text-anchor="middle" font-family="Caveat Brush" font-size="${i?44:40}" fill="${i?ACC:INDI}">${l}</text>`).join('')}</g>`;}
// generic hand-writing into a rotated group; returns [svg, tipLocal]
const WMEAS={};
function writeLines(key,lines,x,y,size,lh,p,col){
 if(!WMEAS[key]){WMEAS[key]=lines.map((l,i)=>{const e=document.getElementById(key+i);return e?e.getComputedTextLength():l.length*size*0.42;});}
 const ww=WMEAS[key]; const tot=lines.reduce((a,l)=>a+l.length,0); let n=p*tot, s='', tip=[x,y-10];
 lines.forEach((l,i)=>{const L=l.length, f=cl(n/L,0,1); n-=L; if(f<=0) return; const w=ww[i]*f;
   s+=`<clipPath id="c${key}${i}"><rect x="${x-10}" y="${y+i*lh-size}" width="${w+12}" height="${lh+24}"/></clipPath>`;
   s+=`<text clip-path="url(#c${key}${i})" x="${x}" y="${y+i*lh}" font-family="Caveat" font-weight="600" font-size="${size}" fill="${col||PEN}">${esc(l)}</text>`;
   if(f<1||i==lines.length-1) tip=[x+w, y+i*lh-8+4*Math.sin(n*3)]; });
 return [s,tip];}
function measurers(key,lines,size){return lines.map((l,i)=>`<text id="${key}${i}" x="-3000" y="-3000" font-family="Caveat" font-weight="600" font-size="${size}">${esc(l)}</text>`).join('');}
function rotPt(gx,gy,r,x,y){const a=r*Math.PI/180;return [gx+x*Math.cos(a)-y*Math.sin(a), gy+x*Math.sin(a)+y*Math.cos(a)];}
function tableTop(y){return `<rect x="-40" y="${y}" width="1160" height="${1960-y}" fill="#FFF8EF" ${o}/><path d="M-40 ${y+18} H1120" stroke="${PEACH}" stroke-width="10"/>`;}

// =============================================== scene: wedding toast (Nov 1)  [gate rev: big serif lines, no hand over text]
const TC_X=50, TC_Y=1105, TC_R=-1.2, TCW=980, TCH=390;
const TL=["…Maya had set off the fire alarm.","Making toast."];
const TLX=44, TLY=200, TLS=72, TLH=96;
function indexCard(t,empty){
 let s=`<rect x="10" y="14" width="${TCW}" height="${TCH}" rx="12" fill="rgba(42,29,71,.14)"/><rect x="0" y="0" width="${TCW}" height="${TCH}" rx="12" fill="#FFFFFF" ${o}/>`;
 s+=`<path d="M0 96 H${TCW}" stroke="#E86A6A" stroke-width="3"/>`;
 for(let i=0;i<2;i++) s+=`<path d="M0 ${TLY+18+i*TLH} H${TCW}" stroke="#B9C6F0" stroke-width="2.5"/>`;
 s+=`<text x="40" y="72" font-family="Caveat Brush" font-size="60" fill="${INDI}">My toast:</text>`;
 if(empty>0){ s+=`<rect x="36" y="116" width="${TCW-72}" height="${TCH-150}" rx="16" fill="none" stroke="${INDI}" stroke-width="4" stroke-dasharray="14 14" opacity="${empty*(0.55+0.35*Math.sin(t*5))}"/>`;
   s+=`<text x="${TCW/2}" y="${TCH/2+90}" text-anchor="middle" font-family="DM Serif Display" font-size="120" fill="${INDI}" opacity="${empty*0.5}">?</text>`;}
 return s;}
function serifLines(lines,x,y,size,lh,p){ // ink appears word by word (no hand over the text)
 const tot=lines.reduce((a,l)=>a+l.split(' ').length,0); let n=p*tot, s='';
 lines.forEach((l,i)=>{const ws=l.split(' '); const k=Math.max(0,Math.min(ws.length,Math.floor(n+0.0001))); const fr=n-k; n-=ws.length; if(k<=0&&fr<=0) return;
   const shown=ws.slice(0,k).join(' '), next=k<ws.length?ws[k]:'';
   s+=`<text x="${x}" y="${y+i*lh}" font-family="Instrument Serif" font-size="${size}" fill="${INK}">${esc(shown)}${next&&fr>0?`<tspan opacity="${cl(fr*1.6,0,1)}"> ${esc(next)}</tspan>`:''}</text>`;});
 return s;}
function factNote(x,y,rot,lines,k,fly){ // made-up story note; fly 0..1 -> into the card
 const tx=x+(TC_X+TCW/2-x-150)*E(fly), ty=y+(TC_Y+200-y)*E(fly), sc=1-0.75*E(fly);
 const inner=textLines(18,66,lines,46,50,OL,'Caveat',700);
 return `<g opacity="${k*(1-seg(fly,.75,1))}" transform="translate(${tx} ${ty}) scale(${sc})">`+sticky(0,0,300,178,rot,'#FFE7A0',inner,40*(1-k))+`</g>`;}
function toastScene(beat,lt,t,S){
 const st=S.starts; let s='';
 const beam=beat==3?E(seg(lt,0.05,0.6)):0;
 s+=garland(t,beam);
 s+=micStand(1010,1060);
 s+=tableTop(1040);
 if(beat==1){ const k=E(seg(lt,0.0,0.1)), fl=seg(lt,1.1,1.6);
   if(fl<1){ s+=`<g opacity="${k*(1-fl)}">`+label(60,755,'stories we made up for this post:',-2,50,ACC,'start')+'</g>'; }
   s+=factNote(30,790,-4,["she set off the","fire alarm","making toast"],k,fl);
   s+=factNote(380,797,3,["she drove 6 hours","to help me move"],E(seg(lt,0.03,0.13)),seg(lt,1.15,1.65));
   s+=factNote(728,790,-2,["her fiancé Theo","beats her at","Scrabble"],E(seg(lt,0.06,0.16)),seg(lt,1.2,1.7)); }
 if(beat==2){ const k=E(seg(t,st[2]+0.0,st[2]+0.1)); const inner=label(24,60,"its tip, word for word:",-2,48,ACC,'start')+textLines(24,128,["Pause after “Making toast.”","The laugh lands there."],56,62,OL,'Caveat',700);
   s+=`<g opacity="${k}">`+sticky(90,745,700,240,-2,'#FFE7A0',inner,(1-k)*120)+`</g>`; }
 s+=`<g transform="translate(${TC_X} ${TC_Y}) rotate(${TC_R})">`;
 s+=indexCard(t, beat==0?1:Math.max(0,1-seg(t,st[1]+1.6,st[1]+1.75)));
 s+=`<text id="mtm" x="-3000" y="-3000" font-family="Instrument Serif" font-size="${TLS}">Making toast.</text>`;
 s+=serifLines(TL,TLX,TLY,TLS,TLH,seg(t,st[1]+1.75,st[1]+2.35));
 if(beat>=2){ const pk=seg(t,st[2]+0.35,st[2]+0.9); const px=WMEAS.mt?WMEAS.mt:400, py=TLY+TLH-56;
   s+=`<text id="mtm" x="-3000" y="-3000" font-family="Instrument Serif" font-size="${TLS}">Making toast.</text>`;
   s+=`<path d="M${px+32} ${py} v${58*cl(pk*2,0,1)} M${px+54} ${py} v${58*cl(pk*2-1,0,1)}" stroke="${ACC}" stroke-width="9" stroke-linecap="round"/>`;
   s+=`<circle cx="${px+43}" cy="${py+29}" r="42" fill="none" stroke="${ACC}" stroke-width="5" stroke-dasharray="270" stroke-dashoffset="${270*(1-seg(t,st[2]+0.8,st[2]+1.3))}"/>`; }
 if(beat==3){ s+=check(TCW-80,52,seg(lt,0.2,0.8)); }
 s+=`</g>`;
 s+=tent(800,992,["Toasts","at 8 pm"],3);
 return s;}
function measureToast(){ if(WMEAS.mt) return; const e=document.getElementById('mtm'); if(e) WMEAS.mt=TLX+e.getComputedTextLength(); }
SCENES.toast=toastScene;
function draw(t){
 const S=SPEC, starts=S.starts, n=S.durs.length; let i=0; for(let k=0;k<n;k++) if(t>=starts[k]) i=k; const lt=t-starts[i];
 let svg=`<defs><radialGradient id="glow"><stop offset="0" stop-color="#FFF2B8" stop-opacity=".95"/><stop offset=".5" stop-color="#FFE7A0" stop-opacity=".45"/><stop offset="1" stop-color="#FFE7A0" stop-opacity="0"/></radialGradient>
  <linearGradient id="cone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE7A0" stop-opacity=".9"/><stop offset="1" stop-color="#FFE7A0" stop-opacity="0"/></linearGradient></defs>`;
 svg+=SCENES[S.scene](i,lt,t,S);
 document.getElementById('art').innerHTML=svg;
 if(S.scene=='toast') measureToast();
 for(let k=0;k<n;k++){const el=document.getElementById('b'+k); let op=0,y=0;
  if(k==i){ if(i==0){op=1;} else {const p=E(seg(lt,0.0,0.08)); op=p; y=20*(1-p);} }
  el.style.opacity=op; el.style.transform=`translateY(${y}px)`;}
 const f=document.getElementById('follow'); const fk=i==n-1?E(seg(lt,S.followAt,S.followAt+0.3)):0; f.style.opacity=fk; f.style.transform=`translateY(${30*(1-fk)}px) scale(${0.92+0.08*fk})`;
}

// =============================================== scene: toast cue card (Nov 2, Part 2)  [gate rev: big 5-cue card, no hand]
const CC_X=60, CC_Y=1045, CC_R=-1.2, CCW=960, CCH=470;
const CL=["1. Intro: best friend since college","2. Fire alarm, 2 a.m. → “Making toast.”","3. She shows up: six-hour drive","4. Theo beat her at Scrabble","5. Raise glasses"];
const CLX=44, CLY=160, CLS=58, CLH=66;
function wallClock(x,y,t){const m=(52+t/14.4*3)/60*2*Math.PI, h=(7+(52+t/14.4*3)/60)/12*2*Math.PI;
 let ticks=''; for(let i=0;i<12;i++){const a=i/12*2*Math.PI; ticks+=`<path d="M${62*Math.sin(a)} ${-62*Math.cos(a)} L${72*Math.sin(a)} ${-72*Math.cos(a)}" stroke="${OL}" stroke-width="${i%3?3:6}"/>`;}
 return `<g transform="translate(${x} ${y})"><circle r="92" fill="rgba(42,29,71,.14)" cx="6" cy="9"/><circle r="92" fill="#FFF8EF" ${o} stroke-width="7"/>${ticks}
  <path d="M0 0 L${40*Math.sin(h)} ${-40*Math.cos(h)}" stroke="${OL}" stroke-width="9" stroke-linecap="round"/>
  <path d="M0 0 L${66*Math.sin(m)} ${-66*Math.cos(m)}" stroke="${ACC}" stroke-width="6" stroke-linecap="round"/><circle r="8" fill="${OL}"/>
  <text x="0" y="140" text-anchor="middle" font-family="Caveat Brush" font-size="48" fill="${ACC}">toasts at 8</text></g>`;}
function wholeToast(){ // the long one-page toast (too much to memorize)
 let s=`<rect x="70" y="-30" width="800" height="${CCH+40}" rx="8" fill="#F4F1FB" ${o} transform="rotate(3 470 270)"/>`;
 s+=`<rect x="60" y="-40" width="800" height="${CCH+40}" rx="8" fill="#FFFFFF" ${o}/>`;
 s+=`<text x="100" y="34" font-family="Caveat Brush" font-size="58" fill="${INDI}">My toast (all of it):</text>`;
 for(let i=0;i<11;i++){const w=560+((i*137)%180); s+=`<path d="M100 ${86+i*36} H${100+w}" stroke="#B9B4D8" stroke-width="10" stroke-linecap="round" stroke-dasharray="${40+(i*13)%30} 12"/>`;}
 return s;}
function cueCard(t,st,beat){
 let s=`<rect x="10" y="14" width="${CCW}" height="${CCH}" rx="12" fill="rgba(42,29,71,.14)"/><rect x="0" y="0" width="${CCW}" height="${CCH}" rx="12" fill="#FFFFFF" ${o}/>`;
 s+=`<path d="M0 100 H${CCW}" stroke="#E86A6A" stroke-width="3"/>`;
 for(let i=0;i<5;i++) s+=`<path d="M0 ${CLY+18+i*CLH} H${CCW}" stroke="#B9C6F0" stroke-width="2.5"/>`;
 s+=`<text x="44" y="74" font-family="Caveat Brush" font-size="62" fill="${INDI}">Cue card</text>`;
 if(beat>=2){ const hk=seg(t,st[2]+0.3,st[2]+0.7); s+=`<rect x="${CLX-10}" y="${CLY+CLH-50}" width="${860*hk}" height="64" rx="12" fill="${SUN}" opacity=".6"/>`; }
 CL.forEach((l,i)=>{const a=st[1]+0.75+i*0.55, k=E(seg(t,a,a+0.25));
  if(k>0) s+=`<text x="${CLX+30*(1-k)}" y="${CLY+i*CLH}" opacity="${k}" font-family="Caveat" font-weight="700" font-size="${CLS}" fill="${PEN}">${esc(l)}</text>`;});
 if(beat==3) s+=check(CCW-80,54,seg(t,st[3]+0.2,st[3]+0.8));
 return s;}
function cueScene(beat,lt,t,S){
 const st=S.starts; let s='';
 const beam=beat==3?E(seg(lt,0.05,0.6)):0;
 s+=garland(t,beam);
 s+=tableTop(1040);
 { const out=beat>=2?E(seg(t,st[2],st[2]+0.3)):0; if(out<1) s+=`<g opacity="${1-out}" transform="translate(${300*out} 0)">`+wallClock(905,800,t)+`</g>`; }
 if(beat==2){ const k=E(seg(t,st[2]+0.0,st[2]+0.1)); const inner=label(24,60,"its tip, in short:",-2,50,ACC,'start')+textLines(24,130,["Lost your place? Skip to","the end: raise your glasses."],56,62,OL,'Caveat',700);
   s+=`<g opacity="${k}">`+sticky(60,712,760,240,-2,'#FFE7A0',inner,(1-k)*120)+`</g>`; }
 const sw=E(seg(t,st[1]+0.1,st[1]+0.6));   // page slides out left, card slides in from right
 if(sw<1) s+=`<g transform="translate(${CC_X-1100*sw} ${CC_Y}) rotate(${CC_R-6*sw})">`+wholeToast()+`</g>`;
 if(sw>0) s+=`<g transform="translate(${CC_X+1100*(1-sw)} ${CC_Y}) rotate(${CC_R})">`+cueCard(t,st,beat)+`</g>`;
 return s;}
SCENES.cue=cueScene;

// =============================================== scene: guests in 30 minutes (Nov 3)
const PL=["0–5 min: Entry (first impression)","5–10 min: Living area","10–14 min: Table","14–21 min: Kitchen","21–28 min: Bathroom","28–30 min: Final touch"];
const PC_X=80, PC_Y=1195, PCW=920, PCH=400;
function door(x,y,open,t){return `<g transform="translate(${x} ${y})"><rect x="-14" y="-14" width="228" height="314" fill="${CREAM}" ${o}/>
 <rect x="0" y="0" width="200" height="300" fill="#3B34A0"/><g transform="skewY(${-8*open}) scale(${1-0.35*open} 1)"><rect x="0" y="0" width="200" height="300" fill="${INDI}" ${o}/>
 <rect x="26" y="26" width="148" height="110" rx="8" fill="none" stroke="${OL}" stroke-width="4"/><rect x="26" y="160" width="148" height="110" rx="8" fill="none" stroke="${OL}" stroke-width="4"/>
 <circle cx="170" cy="150" r="11" fill="${SUN}" stroke="${OL}" stroke-width="4"/></g></g>`;}
function timer(x,y,t){const rem=Math.max(0,30*(1-seg(t,2.2,10.9))); const mm=Math.floor(rem), ss=Math.floor((rem-mm)*60); const done=rem<=0;
 const txt=done?'0:00':`${mm}:${String(ss).padStart(2,'0')}`;
 return `<g transform="translate(${x} ${y})"><rect x="6" y="9" width="190" height="110" rx="22" fill="rgba(42,29,71,.15)"/><rect x="0" y="0" width="190" height="110" rx="22" fill="${done?SUN:'#FFF8EF'}" ${o}/>
 <text x="95" y="80" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="62" fill="${done?ACC:OL}">${txt}</text>
 </g>`;}
function couch(){return `<path d="M320 900 Q320 850 370 850 H770 Q820 850 820 900 V960 H320Z" fill="${PERI}" ${o}/>
 <rect x="290" y="940" width="560" height="90" rx="30" fill="#B7B6EE" ${o}/><rect x="270" y="910" width="70" height="130" rx="30" fill="${PERI}" ${o}/><rect x="800" y="910" width="70" height="130" rx="30" fill="${PERI}" ${o}/>
 <path d="M320 1040 v26 M820 1040 v26" stroke="${OL}" stroke-width="10" stroke-linecap="round"/>`;}
function laundry(k,t){ // pile on the couch -> flies into the basket (k 0..1)
 const C=[ORNG,'#FFFFFF',SUN,'#6E8FC9','#E0413B',PEACH]; let s='';
 for(let i=0;i<6;i++){const sx=400+i*62, sy=930-(i%2)*30, tx=960, ty=1150; const e=E(seg(k,i*0.08,0.5+i*0.08));
  const x=sx+(tx-sx)*e, y=sy+(ty-sy)*e-160*Math.sin(Math.PI*e);
  s+=`<g transform="translate(${x} ${y}) rotate(${i*35+e*200}) scale(${1-0.4*e})" opacity="${1-seg(e,.9,1)}"><path d="M-38 -22 L-14 -30 Q0 -20 14 -30 L38 -22 L44 2 L28 4 L28 30 H-28 L-28 4 L-44 2Z" fill="${C[i]}" ${o} stroke-width="4"/></g>`;}
 return s;}
function basket(x,y,s2){return `<g transform="translate(${x} ${y}) scale(${s2})"><path d="M-80 -40 H80 L64 50 H-64Z" fill="#E7B877" ${o}/>
 <path d="M-74 -10 H74 M-68 20 H68 M-40 -40 L-34 50 M0 -40 V50 M40 -40 L34 50" stroke="#B9874A" stroke-width="4"/><path d="M-80 -40 H80" ${o} fill="none"/></g>`;}
function shoes(k){ // messy by the door -> neat row along the wall
 const P=[[70,1060,-18,1080,'#2E2A3A'],[150,1088,14,1080,'#2E2A3A'],[230,1060,170,1080,ORNG],[110,1110,190,1080,ORNG]]; let s='';
 const N=[[70,1035],[130,1035],[190,1035],[250,1035]];
 P.forEach((p,i)=>{const e=E(seg(k,i*0.1,0.6+i*0.1)); const x=p[0]+(N[i][0]-p[0])*e, y=p[1]+(N[i][1]-p[1])*e, r=p[2]*(1-e);
  s+=`<g transform="translate(${x} ${y}) rotate(${r})"><path d="M-30 6 Q-30 -16 -8 -16 Q4 -6 22 -4 Q32 0 32 10 H-30Z" fill="${p[4]}" ${o} stroke-width="4"/></g>`;});
 // bag: on the floor -> hung on a hook
 const e=E(seg(k,0.3,0.9)); const bx=200+(30-200)*e*0, by=1100+(-0)*e;
 const gx=230+40*e, gy=1095-(1095-800)*e;
 s+=`<g transform="translate(${gx} ${gy}) rotate(${20*(1-e)})"><path d="M-22 -30 Q0 -64 22 -30" stroke="${OL}" stroke-width="6" fill="none"/><rect x="-40" y="-30" width="80" height="70" rx="14" fill="${SUN}" ${o} stroke-width="4"/></g>`;
 return s;}
function coffeeTable(){return `<rect x="350" y="1120" width="420" height="34" rx="10" fill="#F2C79B" ${o}/><path d="M380 1154 v80 M740 1154 v80" stroke="${OL}" stroke-width="12" stroke-linecap="round"/>`;}
function mail(k){let s=''; const M=[[390,1100,-25],[440,1090,18],[490,1104,-8],[530,1092,30],[420,1080,-15]];
 M.forEach((m,i)=>{const e=E(seg(k,i*0.08,0.5+i*0.08)); const x=m[0]+(430-m[0])*e, y=m[1]+(1100-6*i-m[1])*e, r=m[2]*(1-e);
  s+=`<g transform="translate(${x} ${y}) rotate(${r})"><rect x="-38" y="-20" width="76" height="40" rx="4" fill="#FFFFFF" ${o} stroke-width="3"/><path d="M-38 -20 L0 6 L38 -20" stroke="${OL}" stroke-width="3" fill="none"/></g>`;});
 return s;}
const STEPT=[0.3,1.3,2.3,3.3,4.0,4.7];
const PQ=["“Shoes go in a neat row or into a closet.”","“Laundry goes into a basket or bin…”","“Sweep all the mail into one pile or bag…”","“Load the dishwasher, or soak the dishes…”","“Wipe the sink, faucet and mirror.”","“Open a window or light a candle…”"];   // when each plan step lands (s after beat 1 starts)
function planCard(t,st,beat){ // ONE big step at a time (gate rev), not a list
 if(beat==0||beat==3) return '';
 const lt=t-st[1]; let k=0; for(let i=0;i<6;i++) if(lt>=STEPT[i]) k=i; if(lt<STEPT[0]) return '';
 const a=st[1]+STEPT[k], p=E(seg(t,a,a+0.1)); const ik=E(seg(t,st[1]+STEPT[0],st[1]+STEPT[0]+0.2));
 let s=`<g opacity="${ik}" transform="translate(60 1200) rotate(-1)"><rect x="10" y="14" width="960" height="270" rx="22" fill="rgba(42,29,71,.14)"/><rect x="0" y="0" width="960" height="270" rx="22" fill="#FFFFFF" ${o}/>`;
 s+=`<text x="40" y="62" font-family="Poppins" font-weight="700" font-size="44" fill="${INDI}">Step ${k+1} of 6</text>`;
 for(let i=0;i<6;i++) s+=`<circle cx="${640+i*48}" cy="48" r="15" fill="${i<=k?SUN:'#FFFFFF'}" stroke="${OL}" stroke-width="3"/>`;
 s+=`<g opacity="${p}" transform="translate(${30*(1-p)} 0)"><text x="40" y="148" font-family="DM Serif Display" font-size="58" fill="${INK}">${esc(PL[k])}</text>`;
 s+=`<text x="40" y="228" font-family="Caveat" font-weight="700" font-size="54" fill="${PEN}">${esc(PQ[k])}</text></g>`;
 return s+`</g>`;}
function tidyScene(beat,lt,t,S){
 const st=S.starts; let s='';
 const ring=beat==3?E(seg(lt,0.0,0.4)):0;
 s+='<g transform="translate(0 -60)">';
 s+=door(50,740,ring*0.6,t);
 s+=couch();
 s+=coffeeTable();
 s+=timer(570,1010,t);
 const a=st[1]+0.35;
 s+=shoes(seg(t,st[1]+0.35,st[1]+1.25));
 s+=mail(seg(t,st[1]+2.35,st[1]+3.2));
 const bk=beat>=1?E(seg(t,a+0.4,a+0.8)):0;
 if(bk>0) s+=basket(960,1170,bk);
 s+=laundry(seg(t,st[1]+1.35,st[1]+2.3),t);
 s+='</g>';
 if(beat==2){ const k=E(seg(t,st[2]+0.0,st[2]+0.1)); const inner=label(24,58,"its tip, word for word:",-2,46,ACC,'start')+textLines(24,122,["Carry one empty basket or bag","as you go."],52,58,OL,'Caveat',700);
   s+=`<g opacity="${k}">`+sticky(300,700,640,210,-2,'#FFE7A0',inner,(1-k)*120)+`</g>`;
   const bb=E(seg(lt,0.5,1.2)); s+=`<g transform="translate(${-30*Math.sin(t*6)*bb} ${-40*Math.abs(Math.sin(t*5))*bb})"></g>`; }
 s+=planCard(t,st,beat);
 return s;}
SCENES.tidy=tidyScene;
"""

B.JS = B.JS + JS_NEW

SPECS = {
    "toast": dict(
        id="hb-reel-1101-wedding-toast", scene="toast", music=LIB / "hb-x-future-easy.mp3",
        wall="linear-gradient(180deg,#B9B4EE 0%,#C9CAF5 30%,#E3DDF6 50%,#FFEEDC 54%,#FFEEDC 100%)",
        durs=[2.2, 5.2, 3.2, 3.8], follow_at=0.6, follow_y=820, chip_y=1515,
        beats=[
            dict(kick="", head="Best friend's wedding. / *No toast yet.*", fs=118),
            dict(kick="Give AI 3 true stories about your friend.", head="It writes you / *a 1-minute toast.*", fs=118),
            dict(kick="it even coaches you", head="It tells you / *where to pause.*", fs=124),
            dict(kick="Do this:", head="Give AI 3 stories. / *Ask for a 1-minute toast.*", fs=96,
                 sub="In ChatGPT, Claude or Gemini.", send="Part 2 tomorrow, 7 pm: the cue card."),
        ],
        chip="Claude's real lines, shortened · names and stories made up for this post",
    ),
    "cue": dict(
        id="hb-reel-1102-toast-cue-card", scene="cue", music=LIB / "hb-x-smart-bounce.mp3",
        wall="linear-gradient(180deg,#C2BDF0 0%,#CFCDF5 30%,#E6DFF4 50%,#FFE6D3 54%,#FFE6D3 100%)",
        durs=[2.2, 5.4, 3.2, 3.6], follow_at=0.6, follow_y=800, chip_y=1540,
        beats=[
            dict(kick="", head="Toast tonight? / *Can't memorize it?*", fs=120),
            dict(kick="paste your toast into AI", head="Ask for a / *5-line cue card.*", fs=124,
                 sub="Claude's real cue card, shortened:"),
            dict(kick="glance, don't read", head="One look / *per part.*", fs=128),
            dict(kick="Do this:", head="Paste your toast. / *Ask for 5 cues.*", fs=104,
                 sub="In ChatGPT, Claude or Gemini.", send="send this to whoever's giving a toast"),
        ],
        chip="Real Claude reply · toast and names made up for this post",
    ),
    "tidy": dict(
        id="hb-reel-1103-guests-30-min", scene="tidy", music=LIB / "hb-x-ta-da-funk.mp3",
        wall="linear-gradient(180deg,#C9CAF5 0%,#D9D7F7 30%,#E8E2F6 51.3%,#FFEEDC 51.4%,#FFEEDC 100%)",
        durs=[2.2, 5.2, 3.4, 3.6], follow_at=0.6, follow_y=1250, chip_y=1495,
        beats=[
            dict(kick="", head="Guests in / *30 minutes?*", fs=140),
            dict(kick="ask AI for a 30-minute plan", head="Start with what / *guests see first.*", fs=112,
                 sub="Claude's real plan, shortened:"),
            dict(kick="the one-basket trick", head="Don't put things away yet. / *Toss them in one basket.*", fs=88),
            dict(kick="Do this:", head="List the mess. / *Ask AI for a 30-minute plan.*", fs=88,
                 sub="In ChatGPT, Claude or Gemini."),
        ],
        chip="Real Claude reply · apartment made up for this post",
    ),
}
B.SPECS = SPECS

_html0 = B.html


def _html(spec, cover=False):
    """oct28 html() with the beat sub-line and the hand line 24 px lower (clears the pill's descender)."""
    import re
    h = _html0(spec, cover)
    for b in spec["beats"]:
        t0 = 385 + int(b["fs"] * 1.9)
        h = h.replace(f"top:{t0}px;font:600 40px", f"top:{t0 + 24}px;font:600 40px")
        if b.get("send"):
            t1 = t0 + 50 * b.get("sublines", 1) + 24
            h = re.sub(rf"(width:960px;top:){t1}(px;font-size:54px)", rf"\g<1>{t1 + 24}\2", h)
    return h


B.html = _html


if __name__ == "__main__":
    key = sys.argv[1]
    if "--still" in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index("--still") + 1].split(",")]
        print(B.stills(key, ts))
    elif "--full" in sys.argv:
        print(B.full(key, float(sys.argv[sys.argv.index("--full") + 1]), B.SCR / f"{key}-full.png"))
    elif "--cover-only" in sys.argv:
        import nov01_hourback_covers as CV
        print(CV.build(key))
    else:
        print(B.render(key))
        import nov01_hourback_covers as CV
        print(CV.build(key))

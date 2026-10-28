#!/usr/bin/env python3
"""Hourback Reels built Wed Oct 28 2026 by the Hourback maker (Social studio).

    python3 studio/editorial/oct28_hourback.py card|costume            # mp4 + dedicated cover -> media/studio-oct28/hourback/
    python3 studio/editorial/oct28_hourback.py card --still 0,1.2,3    # stills sheet in the scratch dir (review)
    python3 studio/editorial/oct28_hourback.py card --cover-only

card    = hb-reel-1029am-coworker-card (Thu Oct 29, 8:45 am, NO trial). The Performance desk TEST (Oct 28 order 3): the
          Littlefold DRAWN illustrated style in the Hourback palette, not a phone screen and not chat bubbles on a flat card.
          One illustrated desk scene (periwinkle wall, wooden desk, yellow lamp = HB's 'sun', a birthday card already signed by
          others). A drawn hand writes Claude's REAL reply into the card from ~2.4 s. Real run, quoted exactly:
          studio/editorial/hb-oct28-run-card.txt. Names made up for this post.
          Cover = 'Instead of… Say…' reframe (style 7, QUIET).
costume = hb-reel-1031-closet-costume (Sat Oct 31, 7 pm, no trial). Same drawn engine, evening bedroom scene: the clothes
          on the bed become Claude's real costume ideas (ghost with sunglasses, cartoon burglar). Real run, quoted exactly:
          studio/editorial/hb-oct28-run-costume.txt. Closet list made up for this post.
          Cover = Kinetic big text (style 5, LOUD).

Self-contained engine (pattern of studio/recovery-oct22c/littlefold/reel_story.py: per-frame SVG redraw, beats slide in
while old ones slide out, the 'sun' beams on Do this, follow line lands and holds). Imports edkit for fonts/stamp only;
no shared kit is edited. Frames: Playwright Chromium, 1 worker, 1080x1920 @30 -> ffmpeg H.264 + AAC; frames deleted.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
sys.dont_write_bytecode = True
import edkit as K  # noqa: E402
from PIL import Image  # noqa: E402

HB = "hourback"
W, H, FPS = 1080, 1920, 30
OUT = REPO / "media/studio-oct28/hourback"
SCR = Path("/tmp/claude-0/oct28-hourback")
LIB = REPO / "media/music/library/v4"
INK = "#2A1D47"
ACC = "#D4532A"
FOLLOW = "Follow to learn one real AI trick a day."
PILLS = dict(p1="#FFD4BD", p2="#C9CAF5")

JS = r"""
const W=1080,H=1920, OL='#2A1D47', INK='#2A1D47', INDI='#5E54C9', PERI='#C9CAF5', SUN='#FFC94D', ORNG='#FF8A3D', CREAM='#FFF8EF',
 PEACH='#FFD4BD', SK='#F4C9A8', SKD='#DDA27E', WOOD='#F2C79B', WOODD='#E0AC7C', ACC='#D4532A', PEN='#3B34A0';
const cl=(x,a,b)=>Math.min(Math.max(x,a),b), E=t=>1-Math.pow(1-cl(t,0,1),3), EIO=t=>{t=cl(t,0,1);return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;};
const seg=(t,a,b)=>cl((t-a)/(b-a),0,1);
const o=`stroke="${OL}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"`;
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function label(x,y,txt,rot,size,col,anchor){return `<text x="${x}" y="${y}" font-family="Caveat Brush" font-size="${size||46}" fill="${col||ACC}" transform="rotate(${rot||-4} ${x} ${y})" text-anchor="${anchor||'middle'}">${txt}</text>`;}
function sparkle(x,y,s,op){return `<g transform="translate(${x} ${y}) scale(${s})" opacity="${op}"><path d="M0 -26 Q4 -4 26 0 Q4 4 0 26 Q-4 4 -26 0 Q-4 -4 0 -26Z" fill="#FFFFFF" stroke="${OL}" stroke-width="2.5"/></g>`;}
function check(cx,cy,k){return `<circle cx="${cx}" cy="${cy}" r="40" fill="${SUN}" ${o} opacity="${seg(k,0,.3)}"/><path d="M${cx-18} ${cy} l13 14 l26 -28" stroke="${OL}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="80" stroke-dashoffset="${80*(1-seg(k,.2,1))}"/>`;}
// ---------- drawn hand holding a pen; (x,y) = pen tip
function penHand(x,y,s){return `<g transform="translate(${x} ${y}) rotate(38) scale(${s||1})">
 <path d="M0 0 L34 -11 L34 11 Z" fill="${SUN}" ${o} stroke-width="4"/>
 <rect x="32" y="-13" width="300" height="26" rx="11" fill="${INDI}" ${o} stroke-width="4"/>
 <rect x="250" y="-13" width="18" height="26" fill="${SUN}" stroke="${OL}" stroke-width="3"/>
 <path d="M150 -16 Q190 -70 270 -60 Q360 -48 380 20 Q392 92 320 118 Q236 140 170 92 Q120 60 128 30 Q138 6 168 14 L200 24" fill="${SK}" ${o}/>
 <path d="M96 10 Q86 34 112 44 Q160 54 196 40" fill="${SK}" ${o}/>
 <path d="M210 70 Q250 84 290 70 M230 100 Q262 110 296 98" stroke="${SKD}" stroke-width="4" fill="none" stroke-linecap="round"/></g>`;}
// ---------- the desk lamp (HB's 'sun'): warm light that beams on Do this
function lamp(x,y,beam,t){
 const g=0.55+0.45*beam+0.04*Math.sin(t*3);
 return `<g transform="translate(${x} ${y})"><path d="M30 -52 L120 -150 L150 196" stroke="${OL}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="120" cy="-150" r="13" fill="${SUN}" stroke="${OL}" stroke-width="4"/><ellipse cx="150" cy="206" rx="70" ry="20" fill="${INDI}" ${o}/>
 <path d="M-40 40 L-260 ${330+40*beam} L200 ${330+40*beam} L40 40Z" fill="url(#cone)" opacity="${0.35+0.4*beam}"/>
 <circle cx="0" cy="40" r="${120+40*beam}" fill="url(#glow)" opacity="${g}"/>
 <path d="M-80 40 Q-74 -50 0 -62 Q74 -50 80 40Z" fill="${SUN}" ${o}/>
 <path d="M-80 40 Q0 58 80 40" stroke="${OL}" stroke-width="5" fill="none"/>
 <ellipse cx="0" cy="44" rx="34" ry="14" fill="#FFF3C4" stroke="${OL}" stroke-width="4"/>
 <path d="M-30 -30 Q-24 -46 -8 -50" stroke="#FFF3C4" stroke-width="7" fill="none" stroke-linecap="round"/></g>`;}
function mug(x,y,t){let st='';for(let i=0;i<3;i++){const k=(t*0.5+i*0.33)%1;st+=`<path d="M${x-20+i*20} ${y-20-60*k} q-10 -16 0 -32 q10 -16 0 -32" stroke="${OL}" stroke-width="4" fill="none" stroke-linecap="round" opacity="${0.5*Math.sin(Math.PI*k)}"/>`;}
 return st+`<path d="M${x+42} ${y+20} q40 4 34 34 q-6 26 -36 22" stroke="${OL}" stroke-width="6" fill="none"/><path d="M${x-48} ${y} H${x+48} L${x+42} ${y+92} Q${x} ${y+104} ${x-42} ${y+92}Z" fill="${PERI}" ${o}/><path d="M${x-48} ${y} Q${x} ${y+14} ${x+48} ${y}" stroke="${OL}" stroke-width="4" fill="none"/>`;}
function sticky(x,y,w,h,rot,col,inner,drop){return `<g transform="translate(${x} ${y-drop}) rotate(${rot})"><rect x="6" y="10" width="${w}" height="${h}" fill="rgba(42,29,71,.13)"/><rect x="0" y="0" width="${w}" height="${h}" fill="${col}" ${o} stroke-width="4"/>
 <rect x="${w/2-60}" y="-16" width="120" height="34" fill="rgba(255,255,255,.6)" stroke="rgba(42,29,71,.25)" stroke-width="2" transform="rotate(-3 ${w/2} 0)"/>${inner}</g>`;}
function textLines(x,y,lines,size,lh,col,fam,weight,id){return lines.map((l,i)=>`<text ${id?`id="${id}${i}"`:''} x="${x}" y="${y+i*lh}" font-family="${fam||'Caveat'}" font-weight="${weight||600}" font-size="${size}" fill="${col||OL}">${esc(l)}</text>`).join('');}
// ---------- confetti burst (Do this)
function confetti(cx,cy,k,t){let s='';const C=[SUN,ORNG,INDI,PERI,PEACH];for(let i=0;i<16;i++){const a=i*0.39+0.2,r=60+300*E(k),x=cx+r*Math.cos(a)*1.2,y=cy-r*Math.sin(a)*0.9+260*k*k;
 s+=`<rect x="${x}" y="${y}" width="18" height="10" rx="3" fill="${C[i%5]}" stroke="${OL}" stroke-width="2" transform="rotate(${i*40+t*200} ${x} ${y})" opacity="${1-seg(k,.7,1)}"/>`;}return s;}

// =============================================== scene A: the office birthday card
const CARD_X=90, CARD_Y=990, CARD_R=-1.5, CW=900, CH=500;   // one flat office card, fully in frame
const WL=["Happy birthday, Dana!","Hope your year ahead is","a good one, and that it","balances out in your","favour."];
const WX=70, WY=175, WS=54, WLH=60;           // written lines inside the card group
let WW=null;                                   // measured line widths
function cardBase(t,empty){
 let s=`<g transform="translate(${CARD_X} ${CARD_Y}) rotate(${CARD_R})">`;
 s+=`<rect x="10" y="14" width="${CW}" height="${CH}" rx="16" fill="rgba(42,29,71,.14)"/><rect x="0" y="0" width="${CW}" height="${CH}" rx="16" fill="#FFFFFF" ${o}/>`;
 s+=`<text x="40" y="92" font-family="DM Serif Display" font-size="68" fill="${INDI}">Happy <tspan fill="${ORNG}">Birthday</tspan></text>`;
 [[470,40],[505,95],[560,55],[600,100]].forEach((p,i)=>{s+=`<circle cx="${p[0]}" cy="${p[1]}" r="${8+i%3*3}" fill="${[SUN,PERI,PEACH][i%3]}" stroke="${OL}" stroke-width="2.5"/>`;});
 s+=`<text x="${CW-40}" y="82" text-anchor="end" font-family="Caveat Brush" font-size="46" fill="${ORNG}" transform="rotate(3 ${CW-40} 82)">HBD!! – Kim</text>`;
 s+=`<text x="${CW-40}" y="250" text-anchor="end" font-family="Caveat Brush" font-size="44" fill="#2F8F6A" transform="rotate(-5 ${CW-40} 250)">Have the</text><text x="${CW-40}" y="296" text-anchor="end" font-family="Caveat Brush" font-size="44" fill="#2F8F6A" transform="rotate(-5 ${CW-40} 296)">best day! – Mo</text>`;
 s+=`<text x="${CW-40}" y="${CH-36}" text-anchor="end" font-family="Caveat Brush" font-size="44" fill="#B23A62" transform="rotate(-2 ${CW-40} ${CH-36})">Happy birthday! – J.</text>`;
 if(empty>0){ s+=`<rect x="44" y="125" width="580" height="320" rx="18" fill="none" stroke="${INDI}" stroke-width="4" stroke-dasharray="14 14" opacity="${empty*(0.55+0.35*Math.sin(t*5))}"/>`;
   s+=`<text x="334" y="320" text-anchor="middle" font-family="DM Serif Display" font-size="110" fill="${INDI}" opacity="${empty*0.5}">?</text>`;}
 return s;}
function measure(){ if(WW) return; WW=WL.map((l,i)=>{const e=document.getElementById('wm'+i);return e?e.getComputedTextLength():l.length*22;}); }
function writing(p){
 measure(); const tot=WL.reduce((a,l)=>a+l.length,0); let n=p*tot, s='', tip=[WX,WY-10];
 WL.forEach((l,i)=>{const L=l.length, f=cl(n/L,0,1); n-=L; if(f<=0) return; const w=WW[i]*f;
   s+=`<clipPath id="wc${i}"><rect x="${WX-10}" y="${WY+i*WLH-60}" width="${w+10}" height="${WLH+20}"/></clipPath>`;
   s+=`<text clip-path="url(#wc${i})" x="${WX}" y="${WY+i*WLH}" font-family="Caveat" font-weight="600" font-size="${WS}" fill="${PEN}">${esc(l)}</text>`;
   if(f<1||i==WL.length-1) tip=[WX+w, WY+i*WLH-8+4*Math.sin(n*3)]; });
 return [s,tip];}
function cardScene(beat,lt,t,S){
 const st=S.starts; let s='';
 s+=mug(790,862,t);
 s+=lamp(975,880,beat==3?E(seg(lt,0.1,0.7)):0,t);
 // wall note 1 (beats 0-1): what we asked, summed up (>=44 px)
 const pin=E(seg(t,0.55,0.9)); const away=beat>=2?E(seg(lt,0,0.3)):0;
 if(pin>0&&away<1){ const inner=label(26,62,'we asked Claude for',-2,46,ACC,'start')+textLines(26,128,["3 short, warm lines","for Dana in accounting.","Nothing cheesy."],46,52,OL,'Caveat',700);
   s+=`<g opacity="${pin*(1-away)}">`+sticky(80-560*away,700,520,262,-3,'#FFE7A0',inner,60*(1-pin))+`</g>`; }
 // wall note 2 (beat 2): Claude's 3rd line, word for word (>=44 px)
 if(beat==2){ const k=E(seg(t,st[2]+0.05,st[2]+0.4)); const inner=label(24,58,"its line 3, word for word:",-2,44,ACC,'start')+textLines(24,116,["Happy birthday, Dana! I hope today","brings you some well-earned","time off from the spreadsheets."],44,50,OL,'Caveat',700);
   s+=`<g opacity="${k}">`+sticky(80,690,690,262,-2,'#FFE7A0',inner,(1-k)*120)+`</g>`; }
 s+=cardBase(t, beat==0?1:Math.max(0,1-seg(t,st[1],st[1]+0.3)));
 s+=WL.map((l,i)=>`<text id="wm${i}" x="-3000" y="-3000" font-family="Caveat" font-weight="600" font-size="${WS}">${esc(l)}</text>`).join('');
 const wp=seg(t,st[1]+0.15,st[1]+3.3);
 const [ws,tip]=writing(wp); s+=ws;
 if(beat>=2){ s+=`<text x="${WX+250}" y="${WY+4*WLH}" font-family="Caveat Brush" font-size="44" fill="${ACC}" transform="rotate(-4 ${WX+250} ${WY+4*WLH})" opacity="${seg(t,st[2],st[2]+0.3)}">← line 1</text>`; }
 if(beat>=3){ s+=check(760,380,seg(lt,0.2,0.8)); }
 s+=`</g>`;
 const g=(x,y)=>{const a=CARD_R*Math.PI/180;return [CARD_X+x*Math.cos(a)-y*Math.sin(a), CARD_Y+x*Math.sin(a)+y*Math.cos(a)];};
 let hx,hy; if(t<st[1]+0.15){const p=g(WX+260,WY+90);hx=p[0]+20*Math.sin(t*2.4);hy=p[1]+40+14*Math.cos(t*3.1);}
 else{const p=g(tip[0],tip[1]);hx=p[0];hy=p[1];}
 const leave=E(seg(t,st[1]+3.45,st[1]+4.1)); hx+=600*leave; hy+=500*leave;
 if(leave<1) s+=penHand(hx,hy,1.0);
 return s;}

// =============================================== scene B: the closet costume (evening bedroom)
function pumpkin(x,y,beam,t){const g=0.5+0.5*beam+0.08*Math.sin(t*6);
 return `<g transform="translate(${x} ${y})"><circle r="${120+40*beam}" fill="url(#glow)" opacity="${g}"/>
 <ellipse cx="-34" cy="0" rx="50" ry="62" fill="${ORNG}" ${o}/><ellipse cx="34" cy="0" rx="50" ry="62" fill="${ORNG}" ${o}/><ellipse cx="0" cy="0" rx="50" ry="66" fill="#FF9C55" ${o}/>
 <path d="M-6 -64 Q-2 -92 18 -98" stroke="#5E8C4A" stroke-width="10" fill="none" stroke-linecap="round"/>
 <path d="M-46 -14 l18 -20 l14 20Z M14 -14 l18 -20 l14 20Z" fill="${SUN}" stroke="${OL}" stroke-width="3"/>
 <path d="M-50 20 Q0 ${54+10*beam} 50 20 L36 28 L26 18 L14 30 L0 20 L-14 30 L-26 18 L-36 28Z" fill="${SUN}" stroke="${OL}" stroke-width="3"/></g>`;}
function windowNight(t){let st='';[[160,120],[300,70],[420,160],[230,200]].forEach((p,i)=>{st+=sparkle(p[0],p[1],0.35+0.15*Math.sin(t*3+i),0.9);});
 return `<g transform="translate(590 860)"><rect x="0" y="0" width="460" height="300" rx="18" fill="#3A2240" ${o}/>
 <circle cx="360" cy="90" r="46" fill="#FFF3C4" stroke="${OL}" stroke-width="4"/><circle cx="380" cy="80" r="40" fill="#3A2240"/>${st}
 <path d="M230 0 V300 M0 150 H460" stroke="${OL}" stroke-width="8"/><rect x="-16" y="292" width="492" height="26" rx="8" fill="${CREAM}" ${o}/></g>`;}
function bed(){return `<path d="M-40 1180 H1120 V1720 H-40Z" fill="${PERI}" ${o}/><path d="M-40 1180 Q540 1150 1120 1180 V1250 Q540 1220 -40 1250Z" fill="#B7B6EE" ${o} stroke-width="4"/>
 ${[0,1,2,3,4,5,6].map(i=>`<path d="M${-20+i*170} 1300 q40 20 80 0" stroke="${INDI}" stroke-width="4" fill="none" opacity=".35"/>`).join('')}`;}
// items (origin = centre)
const IT={
 sheet:(k)=>`<path d="M-120 -70 H120 V70 H-120Z" fill="#FFFFFF" ${o}/><path d="M-120 -20 H120 M-120 25 H120" stroke="${PERI}" stroke-width="4"/>`,
 turtle:()=>`<path d="M-40 -80 H40 L50 -66 L110 -50 L130 40 L96 46 L84 -10 L80 90 H-80 L-84 -10 L-96 46 L-130 40 L-110 -50 L-50 -66Z" fill="#2E2A3A" ${o}/><rect x="-36" y="-98" width="72" height="26" rx="8" fill="#2E2A3A" ${o}/>`,
 jeans:()=>`<path d="M-70 -90 H70 L84 100 H24 L4 -20 L-16 100 H-84Z" fill="#33304A" ${o}/><path d="M-70 -66 H70" stroke="#6C67A0" stroke-width="4"/>`,
 tee:()=>`<path d="M-44 -76 Q0 -56 44 -76 L110 -48 L94 0 L66 -10 L66 84 H-66 L-66 -10 L-94 0 L-110 -48Z" fill="#FFFFFF" ${o}/>${[-40,-12,16,44,72].map(y=>`<path d="M-66 ${y} H66" stroke="${INDI}" stroke-width="12"/>`).join('')}<path d="M-44 -76 Q0 -56 44 -76" fill="none" ${o}/>`,
 beanie:()=>`<path d="M-70 30 Q-74 -60 0 -66 Q74 -60 70 30Z" fill="${INK}" ${o}/><rect x="-80" y="18" width="160" height="40" rx="12" fill="#3B3456" ${o}/><circle cx="0" cy="-74" r="16" fill="#3B3456" ${o}/>`,
 bandana:()=>`<path d="M-80 -40 H80 L0 60Z" fill="#E0413B" ${o}/>${[[-40,-20],[10,-24],[0,20],[40,-14]].map(p=>`<circle cx="${p[0]}" cy="${p[1]}" r="6" fill="#FFFFFF"/>`).join('')}`,
 shades:()=>`<path d="M-90 -12 H90" stroke="${OL}" stroke-width="7" stroke-linecap="round"/><path d="M-84 -14 H-12 Q-14 30 -48 30 Q-82 30 -84 -14Z M12 -14 H84 Q82 30 48 30 Q14 30 12 -14Z" fill="#1D1830" ${o}/><path d="M-70 -4 l20 -2 M26 -4 l20 -2" stroke="#9E98D8" stroke-width="5" stroke-linecap="round"/>`,
 jacket:()=>`<path d="M-50 -84 H50 L120 -54 L134 60 L98 64 L88 0 L84 90 H6 V-60 H-6 V90 H-84 L-88 0 L-98 64 L-134 60 L-120 -54Z" fill="#6E8FC9" ${o}/><path d="M-50 -84 L-6 -30 M50 -84 L6 -30" stroke="${OL}" stroke-width="4"/>`,
 board:()=>`<rect x="-80" y="-60" width="160" height="120" rx="6" fill="#D9A867" ${o}/><path d="M-60 -30 H40 M-60 0 H60 M-60 30 H20" stroke="#B9874A" stroke-width="4"/><rect x="40" y="40" width="70" height="16" rx="6" fill="${INK}" transform="rotate(-30 75 48)"/>`,
};
const ITPOS={sheet:[200,1330,-4],turtle:[470,1310,5],jeans:[720,1330,-6],tee:[930,1350,6],beanie:[150,1520,-8],bandana:[380,1530,10],shades:[600,1520,-4],jacket:[830,1540,4],board:[980,1560,-10]};
function drawItem(name,x,y,rot,s,op){return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s||0.8})" opacity="${op==null?1:op}">${IT[name]()}</g>`;}
function ghost(x,y,k,t,sh){ // sheet draped into a ghost, k 0..1 drape progress, sh = sunglasses on (0..1)
 const bob=6*Math.sin(t*3); const w=150+30*(1-k), hh=60+250*k;
 let hem=''; const n=6; for(let i=n;i>=0;i--){const xx=-w+2*w*i/n; hem+=` Q${xx+w/n} ${hh+24*Math.sin(i+t*3)} ${xx} ${hh}`;}
 let s=`<g transform="translate(${x} ${y+bob})"><path d="M${-w} ${hh} Q${-w} ${-140*k} 0 ${-170*k-20} Q${w} ${-140*k} ${w} ${hh}${hem.replace(/^ Q/,' L'+(w)+' '+hh+' Q')}Z" fill="#FFFFFF" ${o}/>`;
 if(k>0.6){const e=seg(k,.6,1); s+=`<ellipse cx="-44" cy="-40" rx="${18*e}" ry="${26*e}" fill="${INK}"/><ellipse cx="44" cy="-40" rx="${18*e}" ry="${26*e}" fill="${INK}"/>`;}
 if(sh>0){s+=`<g transform="translate(0 ${-44-260*(1-E(sh))}) rotate(${-20*(1-E(sh))}) scale(1.05)">${IT.shades()}</g>`;}
 s+=`</g>`; return s;}
function burglar(x,y,k,t){ // flat-lay figure assembled from tee, jeans, beanie, bandana, shades, cardboard sack
 const P=(name,dx,dy,rot,sc,a)=>{const e=E(seg(k,a,a+0.35)); const [sx,sy]=ITPOS[name]; const X=sx+(x+dx-sx)*e, Y=sy+(y+dy-sy)*e; return drawItem(name,X,Y,rot*(1-e),sc,1);};
 let s='';
 s+=P('jeans',0,170,-6,1.0,0.25)+P('tee',0,10,6,1.0,0.1)+P('beanie',0,-210,-8,0.9,0.4);
 if(k>0.45){const e=E(seg(k,.45,.7)); s+=`<circle cx="${x}" cy="${y-130}" r="${62*e}" fill="${SK}" ${o}/>`;}
 s+=P('beanie',0,-200,-8,0.9,0.5);
 s+=P('shades',0,-140,-4,0.62,0.6)+P('bandana',0,-96,10,0.62,0.7);
 const e=E(seg(k,.75,1)); s+=`<g transform="translate(${x+230} ${y+20}) scale(${0.3+0.7*e})" opacity="${e}"><path d="M-80 -70 Q-90 60 -60 90 H60 Q90 60 80 -70 Q60 -90 40 -70 Q0 -96 -40 -70 Q-60 -90 -80 -70Z" fill="#D9A867" ${o}/><text x="0" y="40" text-anchor="middle" font-family="DM Serif Display" font-size="110" fill="${INK}">$</text></g>`;
 return s;}
function costumeScene(beat,lt,t,S){
 const st=S.starts; let s=windowNight(t)+pumpkin(985,1092,beat==3?E(seg(lt,0.1,0.7)):0,t)+bed();
 // prompt sticky (shortened, labelled) on the wall
 const pin=E(seg(t,0.5,0.85)), away=beat>=1?E(seg(t,st[1]+1.6,st[1]+2.0)):0;
 if(pin>0&&away<1){const inner=label(24,60,'we asked Claude for',-2,46,ACC,'start')+textLines(24,124,["3 costume ideas, made only","from what's in my closet,","for a party in an hour."],46,52,OL,'Caveat',700);
   s+=`<g opacity="${pin*(1-away)}">`+sticky(40-560*away,760,540,262,-3,'#FFE7A0',inner,60*(1-pin))+`</g>`;}
 // the clothes on the bed (they leave as they are used)
 const gk=seg(t,st[1]+0.1,st[1]+1.4), bk=seg(t,st[2]+0.05,st[2]+1.8);
 const usedB=['tee','jeans','beanie','bandana','shades','board','turtle'];
 for(const n in ITPOS){ if(n=='sheet'&&t>st[1]+0.1) continue; if(beat>=2&&usedB.includes(n)) continue; if(beat==1&&n=='shades'&&t>st[1]+1.2) continue;
   const [x,y,r]=ITPOS[n]; s+=drawItem(n,x,y,r+2*Math.sin(t*2+x),0.8,beat>=2?0.5:1);}
 if(beat==1||(beat==2&&lt<0.4)){ const out=beat==2?E(seg(lt,0,0.4)):0; s+=`<g transform="translate(${-700*out} 0)">`+ghost(540,1320,EIO(gk),t,seg(t,st[1]+1.3,st[1]+1.8))+`</g>`;}
 if(beat>=2){ s+=burglar(beat==3?500-170*E(seg(lt,0,0.4)):500,1380,beat==3?1:bk,t); }
 if(beat==3){ s+=ghost(790+400*(1-E(seg(lt,0,0.45))),1330,1,t,1); }
 // quote cards: Claude's words, exactly
 if(beat==1){const k=E(seg(t,st[1]+1.8,st[1]+2.2)); s+=`<g opacity="${k}" transform="translate(0 ${30*(1-k)})">`+quote(540,700,["Idea 1 of 3: Classic Ghost","“Add the sunglasses over the eye holes","if you want a ‘cool ghost.’”"])+`</g>`;}
 if(beat==2){const k=E(seg(t,st[2]+1.5,st[2]+1.9)); s+=`<g opacity="${k}" transform="translate(0 ${30*(1-k)})">`+quote(540,700,["Idea 3 of 3: Cartoon Burglar / Robber","“Striped T-shirt, black jeans and the beanie.","Red bandana over your lower face, plus sunglasses.”"])+`</g>`;}
 return s;}
function quote(cx,y,lines){const w=960; let s=`<g transform="translate(${cx-w/2} ${y})"><rect x="6" y="10" width="${w}" height="${44+lines.length*50}" rx="22" fill="rgba(42,29,71,.18)"/><rect x="0" y="0" width="${w}" height="${36+lines.length*50}" rx="22" fill="#FFFFFF" ${o} stroke-width="4"/>`;
 s+=`<text x="${w/2}" y="56" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="40" fill="${INDI}">${esc(lines[0])}</text>`;
 lines.slice(1).forEach((l,i)=>{s+=`<text x="${w/2}" y="${110+i*48}" text-anchor="middle" font-family="Inter" font-weight="600" font-size="34" fill="${OL}">${esc(l)}</text>`;});
 return s+`</g>`;}

const SCENES={card:cardScene, costume:costumeScene};
// =============================================== frame
let SPEC=null;
function draw(t){
 const S=SPEC, starts=S.starts, n=S.durs.length; let i=0; for(let k=0;k<n;k++) if(t>=starts[k]) i=k; const lt=t-starts[i];
 let svg=`<defs><radialGradient id="glow"><stop offset="0" stop-color="#FFF2B8" stop-opacity=".95"/><stop offset=".5" stop-color="#FFE7A0" stop-opacity=".45"/><stop offset="1" stop-color="#FFE7A0" stop-opacity="0"/></radialGradient>
  <linearGradient id="cone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE7A0" stop-opacity=".9"/><stop offset="1" stop-color="#FFE7A0" stop-opacity="0"/></linearGradient></defs>`;
 const sw=seg(lt,0,0.6); if(i>0&&sw<1) svg+=`<rect x="${-600+1900*E(sw)}" y="0" width="360" height="1920" fill="#FFF6D8" opacity="${0.3*Math.sin(Math.PI*sw)}" transform="skewX(-12)"/>`;
 svg+=SCENES[S.scene](i,lt,t,S);
 document.getElementById('art').innerHTML=svg;
 for(let k=0;k<n;k++){const el=document.getElementById('b'+k); let op=0,y=0;
  if(k==i){ if(i==0){op=1;} else {const p=E(seg(lt,0.05,0.3)); op=p; y=40*(1-p);} }
  else if(k==i-1 && lt<0.12){const p=seg(lt,0,0.12); op=1-p; y=-40*E(p);}
  el.style.opacity=op; el.style.transform=`translateY(${y}px)`;}
 const f=document.getElementById('follow'); const fk=i==n-1?E(seg(lt,S.followAt,S.followAt+0.35)):0; f.style.opacity=fk; f.style.transform=`translateY(${30*(1-fk)}px) scale(${0.92+0.08*fk})`;
}
"""

# ------------------------------------------------------------------ specs
SPECS = {
    "card": dict(
        id="hb-reel-1029am-coworker-card", scene="card", music=LIB / "hb-x-smart-bounce.mp3",
        wall="linear-gradient(180deg,#C9CAF5 0%,#D9D7F7 26%,#EEE4F4 40%,#FFEEDC 48%,#FFEEDC 49.9%,#F2C79B 50%,#F2C79B 100%)",
        desk_y=1100,
        durs=[2.4, 5.1, 3.3, 3.6], follow_at=0.75, follow_y=735, chip_y=1515,
        beats=[
            dict(kick="", head="Office card coming? / *AI writes your line.*", fs=124),
            dict(kick="ask for 3 short, warm lines", head="Write the best one / *in by hand.*", fs=124, sub="Below: Claude's real line 1, word for word."),
            dict(kick="2 of its 3 lines", head="Pick the one / *that sounds like you.*", fs=118),
            dict(kick="Do this:", head="Ask AI for 3 lines. / *Pick one.*", fs=104,
                 sub="In ChatGPT, Claude or Gemini.",
                 send="send this to whoever's signing next"),
        ],
        chip="Real Claude reply · card and names made up for this post",
    ),
    "costume": dict(
        id="hb-reel-1031-closet-costume", scene="costume", music=LIB / "hb-x-ta-da-funk.mp3",
        wall="linear-gradient(180deg,#B9B4EE 0%,#C9CAF5 35%,#E3DDF6 55%,#E3DDF6 100%)",
        durs=[2.4, 4.8, 3.6, 3.6], follow_at=0.75, follow_y=735, chip_y=1192,
        beats=[
            dict(kick="", head="Party in an hour. / *No costume?*", fs=128),
            dict(kick="list what you own", head="AI turns your closet / *into 3 costumes.*", fs=112, sub="Claude's real reply, word for word:"),
            dict(kick="its idea 3 of 3", head="Same closet. / *Different costume.*", fs=118, sub="Claude's real reply, word for word:"),
            dict(kick="Do this:", head="List your clothes. / *Ask for 3 costumes.*", fs=104,
                 sub="In ChatGPT, Claude or Gemini.",
                 send="send this to whoever still has no costume"),
        ],
        chip="Real Claude reply · closet made up for this post",
    ),
}


def html(spec, cover=False):
    f = dict(p1=PILLS["p1"], p2=PILLS["p2"])
    T = ""
    for k, b in enumerate(spec["beats"]):
        T += (f'<div id="b{k}" style="position:absolute;left:0;top:0;width:{W}px;height:1000px;opacity:0">'
              f'<div class="hand" style="position:absolute;left:70px;width:940px;top:300px;font-size:62px">{b["kick"]}</div>'
              + K.dual(b["head"], f, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:385px;white-space:nowrap;font-size:{b['fs']}px;color:{INK}")
              + (f'<div style="position:absolute;left:80px;width:920px;top:{385 + int(b["fs"] * 1.9)}px;font:600 40px/1.25 Inter;text-align:center;color:{INK}">{b["sub"]}</div>' if b.get("sub") else "")
              + (f'<div class="hand" style="position:absolute;left:60px;width:960px;top:{385 + int(b["fs"] * 1.9) + 50 * b.get("sublines", 1) + 24}px;font-size:54px;transform:rotate(-2deg)">{b["send"]}</div>' if b.get("send") else "")
              + "</div>")
    follow = (f'<div id="follow" style="position:absolute;left:0;right:0;top:{spec.get("follow_y", 935)}px;text-align:center;opacity:0">'
              f'<span style="display:inline-block;padding:16px 34px;border-radius:99px;background:{INK};color:#FFF8EF;font:700 40px Poppins;box-shadow:0 8px 0 rgba(42,29,71,.18)">{FOLLOW}</span></div>')
    chip = (f'<div style="position:absolute;left:0;right:0;top:{spec.get("chip_y", 1515)}px;text-align:center"><span style="display:inline-block;font:500 26px Poppins;color:{INK};'
            f'background:#FFF8EF;border:2px solid {INK};border-radius:99px;padding:8px 22px">{spec["chip"]}</span></div>')
    body = (f'<div style="position:absolute;inset:0;background:{spec["wall"]}"></div><div class="grain" style="opacity:.28"></div>'
            f'<svg id="art" style="position:absolute;left:0;top:0" width="{W}" height="{H}" viewBox="0 0 {W} {H}"></svg>'
            + T + follow + chip + K.stamp(HB, 36, 200, size=104, rot=-10) + f"<script>{JS}</script>")
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{K.css(HB, W, H)}"
            f"html,body{{background:#FFF8EF}}</style></head><body><div class='page'>{body}</div></body></html>")


def _page(pw, spec, scale=1):
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=scale)
    SCR.mkdir(parents=True, exist_ok=True)
    tmp = SCR / f"{spec['scene']}.html"
    tmp.write_text(html(spec))
    pg.goto(tmp.as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(400)
    pg.evaluate(K.FIT_JS, 920)
    durs = spec["durs"]
    starts = [round(sum(durs[:k]), 3) for k in range(len(durs))]
    pg.evaluate(f"SPEC={json.dumps(dict(durs=durs, starts=starts, scene=spec['scene'], followAt=spec['follow_at']))}")
    return br, pg, starts


def stills(key, ts, sw=270):
    from playwright.sync_api import sync_playwright
    spec = SPECS[key]
    with sync_playwright() as pw:
        br, pg, _ = _page(pw, spec)
        ims = []
        for t in ts:
            pg.evaluate(f"draw({t})")
            p = SCR / f"{key}-still.png"
            pg.screenshot(path=str(p))
            ims.append(Image.open(p).convert("RGB").resize((sw, int(sw * 16 / 9))))
        br.close()
    sh = Image.new("RGB", ((sw + 6) * len(ims), int(sw * 16 / 9)), "white")
    for k, im in enumerate(ims):
        sh.paste(im, ((sw + 6) * k, 0))
    out = SCR / f"{key}-stills.jpg"
    sh.save(out, quality=88)
    return out


def full(key, t, out):
    from playwright.sync_api import sync_playwright
    spec = SPECS[key]
    with sync_playwright() as pw:
        br, pg, _ = _page(pw, spec)
        pg.evaluate(f"draw({t})")
        pg.screenshot(path=str(out))
        br.close()
    return out


def render(key):
    from playwright.sync_api import sync_playwright
    spec = SPECS[key]
    total = sum(spec["durs"])
    n = int(round(total * FPS))
    fdir = SCR / f"{key}-frames"
    shutil.rmtree(fdir, ignore_errors=True)
    fdir.mkdir(parents=True)
    with sync_playwright() as pw:
        br, pg, starts = _page(pw, spec)
        for fr in range(n):
            pg.evaluate(f"draw({fr / FPS})")
            pg.screenshot(path=str(fdir / f"{fr:04d}.jpg"), type="jpeg", quality=94)
        br.close()
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{spec['id']}.mp4"
    wav = SCR / f"{key}.wav"
    pop = LIB / "sfx/sfx-x-sticker-pop.mp3"
    slap = LIB / "sfx/sfx-x-paper-slap.mp3"
    hits = [(0.6, slap, 0.35)] + [(s + 0.08, pop, 0.25) for s in starts[1:]] + spec.get("sfx", [])
    if key == "card":
        hits.append((starts[2] + 0.05, slap, 0.35))
    inputs = ["-i", str(spec["music"])]
    filt = [f"[0:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.05,afade=t=out:st={total - 0.6:.3f}:d=0.6[m]"]
    mix = ["[m]"]
    for k, (pt, f, vol) in enumerate(hits):
        inputs += ["-i", str(f)]
        filt.append(f"[{k + 1}:a]volume={vol},adelay={int(pt * 1000)}|{int(pt * 1000)}[p{k}]")
        mix.append(f"[p{k}]")
    filt.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[o]")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[o]",
                    "-ar", "48000", "-ac", "2", str(wav)], check=True)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(fdir / "%04d.jpg"), "-i", str(wav),
                    "-c:v", "libx264", "-threads", "1", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "19", "-profile:v", "high",
                    "-r", str(FPS), "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out)], check=True)
    shutil.rmtree(fdir)
    wav.unlink()
    return out, total


if __name__ == "__main__":
    key = sys.argv[1]
    st = [a for a in sys.argv if a.startswith("--still")]
    if st:
        ts = [float(x) for x in sys.argv[sys.argv.index("--still") + 1].split(",")]
        print(stills(key, ts))
    elif "--full" in sys.argv:
        print(full(key, float(sys.argv[sys.argv.index("--full") + 1]), SCR / f"{key}-full.png"))
    elif "--cover-only" in sys.argv:
        import oct28_hourback_covers as CV
        print(CV.build(key))
    else:
        print(render(key))
        import oct28_hourback_covers as CV
        print(CV.build(key))

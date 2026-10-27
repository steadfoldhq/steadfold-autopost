#!/usr/bin/env python3
"""Locked Hour, Oct 27 studio build: two Reels in an LH-zine version of Littlefold's winning
"felt question -> the action DRAWN BEING DONE" format (studio/editorial/oct24_lf_a.py +
studio/recovery-oct22c/littlefold/reel_story.py: one JS draw(t) per frame, one illustrated scene that keeps acting
while the words change). Own kit here; the shared LF kit is not imported or edited.

LH zine look: butter/cream/pink fields with the 30 px dot grid, thick ink lines (7 px), hard offset ink shadows,
highlighter pops (yellow #FFD43B, pink #FF5CA8 / #FFBAD6), Inter Display 900 hooks with pills, Caveat Brush notes.
Never black-heavy: ink is line work only.

  eyes    lh-reel-1028am-close-your-eyes  Wed Oct 28 08:30 ET, NO trial (desk order 3). Desk order 4 TEST.
          Frame 0: "Can't recall what you saw?" + a drawn face with open eyes, pings and a ticking clock around it.
          By 1.7 s the eyelids are drawn shut, the distractions drop away and a thought cloud fills with what was seen.
          Research: Perfect et al. 2008, Law and Human Behavior (5 experiments; eyes-closed recall better in 4).
  tempt   lh-reel-1030-fewer-temptations  Fri Oct 30 19:00 ET, no trial.
          Frame 0: the rule as a fact, "Fewer temptations beat more willpower." + a drawn desk with a cookie jar and a
          game controller; by 2.2 s both are lifted into a box marked "other room". Body includes an Ep.01-style
          "Instead of... / Say..." reframe beat. Research: Milyavskaya & Inzlicht 2017, SPPS 8(6):603-611.

  python3 studio/editorial/oct27_lockedhour.py eyes|tempt [--cover-only] [--still=0,1.7,3] [--keep]
Music: existing LH v4 library tracks only (tools/music-library.json), -14 LUFS. No new music.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import edkit  # noqa: E402

os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
SCR = Path(os.environ.get("LH_SCR", "/tmp/claude-0/oct27-lockedhour"))
SCR.mkdir(parents=True, exist_ok=True)
OUT = REPO / "media/studio-oct27/lockedhour"
OUT.mkdir(parents=True, exist_ok=True)
LIB = json.loads((REPO / "tools/music-library.json").read_text())
W, H, FPS = 1080, 1920, 30
INK = "#1B1717"
FOLLOW = "Follow for one small focus trick a day."
F = edkit.FIELDS["lockedhour"]

CSS = edkit.FONTS + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#FFF0A6}}
#bg{{position:absolute;inset:0;background-color:#FFF0A6;
 background-image:radial-gradient(circle,rgba(20,20,20,.12) 2.4px,transparent 2.6px);background-size:30px 30px}}
#bg2{{position:absolute;inset:0;opacity:0;background-color:#FFF6E5;
 background-image:radial-gradient(circle,rgba(20,20,20,.12) 2.4px,transparent 2.6px);background-size:30px 30px}}
.H{{white-space:nowrap;font-family:'Inter Display',Inter,sans-serif;font-weight:900;color:{INK};letter-spacing:-.03em;line-height:1.02;text-align:center}}
.H .pill{{border-radius:.28em;padding:0 .1em .03em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.kick{{font-family:'Caveat Brush';color:#E8336F;text-align:center;line-height:1}}
.sub{{font-family:Inter;font-weight:700;color:{INK};text-align:center;line-height:1.22}}
.sh *{{fill:{INK}!important;stroke:{INK}!important}}
.chip{{display:inline-block;max-width:880px;line-height:1.15;padding:18px 40px;border-radius:99px;background:#FFFDF4;border:6px solid {INK};box-shadow:8px 8px 0 {INK};
 font:800 56px Inter;color:{INK};letter-spacing:-.01em}}
"""

JS = r"""
const W=1080,H=1920, INK='#1B1717', BUT='#FFE27A', HY='#FFD43B', HP='#FF5CA8', HPL='#FFBAD6', CR='#FFFDF4', CR2='#FFF4E0', DP='#E8336F', GREY='#C9C2B8';
const cl=(x,a,b)=>Math.min(Math.max(x,a),b), E=t=>1-Math.pow(1-cl(t,0,1),3), EIO=t=>{t=cl(t,0,1);return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;};
const seg=(t,a,b)=>cl((t-a)/(b-a),0,1), BK=t=>{t=cl(t,0,1);const c=1.7;return 1+(c+1)*Math.pow(t-1,3)+c*Math.pow(t-1,2);};
const o=`stroke="${INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"`;
const sh=(svg,d)=>`<g class="sh" transform="translate(${d||12} ${d||12})">${svg}</g>${svg}`;
function label(x,y,txt,rot,size,col){return `<text x="${x}" y="${y}" font-family="Caveat Brush" font-size="${size||56}" fill="${col||DP}" transform="rotate(${rot||-4} ${x} ${y})" text-anchor="middle">${txt}</text>`;}
function check(cx,cy,k,r){r=r||38;return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${HY}" ${o} opacity="${seg(k,0,.3)}"/><path d="M${cx-r*.45} ${cy} l${r*.32} ${r*.34} l${r*.62} ${-r*.7}" stroke="${INK}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="90" stroke-dashoffset="${90*(1-seg(k,.2,1))}"/>`;}
function burst(x,y,k,col){if(k<=0||k>=1)return '';let s='';const r=30+60*k;for(let i=0;i<8;i++){const a=i*Math.PI/4+.3;s+=`<path d="M${x+r*Math.cos(a)} ${y+r*Math.sin(a)} L${x+(r+26)*Math.cos(a)} ${y+(r+26)*Math.sin(a)}" stroke="${col||HP}" stroke-width="9" stroke-linecap="round" opacity="${1-k}"/>`;}return s;}
function pop(k){return k<=0?0:BK(k);}
function xmark(cx,cy,r,k){const a=seg(k,0,.5),b=seg(k,.5,1);return `<path d="M${cx-r} ${cy-r} L${cx-r+2*r*a} ${cy-r+2*r*a}" stroke="${DP}" stroke-width="12" stroke-linecap="round"/><path d="M${cx+r} ${cy-r} L${cx+r-2*r*b} ${cy-r+2*r*b}" stroke="${DP}" stroke-width="12" stroke-linecap="round"/>`;}

// ================= SCENE 1: eyes (close your eyes to remember) =================
function eye(x,y,lid,look){ // lid 0 open .. 1 shut
 const ry=34*(1-lid);
 if(lid>0.92) return `<path d="M${x-36} ${y} Q${x} ${y+26} ${x+36} ${y}" stroke="${INK}" stroke-width="8" fill="none" stroke-linecap="round"/>`+
   [[-26,10],[0,16],[26,10]].map(([dx,dy])=>`<path d="M${x+dx} ${y+dy} l${dx*.25} 14" stroke="${INK}" stroke-width="6" stroke-linecap="round"/>`).join('');
 const px=x+14*look, py=y+2;
 return `<ellipse cx="${x}" cy="${y}" rx="38" ry="${Math.max(ry,3)}" fill="#FFFFFF" ${o}/>`+(ry>12?`<circle cx="${px}" cy="${py}" r="${Math.min(17,ry*.6)}" fill="${INK}"/><circle cx="${px+6}" cy="${py-6}" r="5" fill="#fff"/>`:'')+
   `<path d="M${x-40} ${y-ry-2} Q${x} ${y-ry-12-6*lid} ${x+40} ${y-ry-2}" stroke="${INK}" stroke-width="7" fill="none" stroke-linecap="round"/>`;}
function face(x,y,s,lid,look,smile,t){
 let f=sh(`<path d="M-120 250 Q-120 150 0 150 Q120 150 120 250 L120 300 L-120 300Z" fill="${HPL}" ${o}/>`,14); // shoulders/top
 f+=`<rect x="-34" y="96" width="68" height="70" fill="${CR2}" ${o}/>`;
 const head=`<ellipse cx="0" cy="0" rx="138" ry="150" fill="${CR2}" ${o}/>`;
 f+=sh(head,16);
 f+=`<path d="M-140 -10 Q-160 -170 0 -168 Q150 -170 142 -20 Q120 -90 60 -110 Q0 -60 -70 -100 Q-120 -80 -140 -10Z" fill="${HY}" ${o}/>`; // highlighter hair
 f+=`<path d="M-60 -128 q20 -16 40 0 M30 -132 q18 -14 36 2" stroke="${INK}" stroke-width="5" fill="none" stroke-linecap="round" opacity=".5"/>`;
 f+=eye(-54,10,lid,look)+eye(54,10,lid,look);
 f+=`<circle cx="-92" cy="62" r="20" fill="${HPL}" opacity=".9"/><circle cx="92" cy="62" r="20" fill="${HPL}" opacity=".9"/>`;
 f+=`<path d="M-8 34 Q-14 60 2 62" stroke="${INK}" stroke-width="6" fill="none" stroke-linecap="round"/>`;
 const m=smile; f+=`<path d="M-36 ${88-4*m} Q0 ${92+26*m} 36 ${88-4*m}" stroke="${INK}" stroke-width="7" fill="${m>.5?'#fff':'none'}" stroke-linecap="round"/>`;
 return `<g transform="translate(${x} ${y}) scale(${s})">${f}</g>`;}
function phoneD(x,y,rot,buzz,op){const j=buzz?6*Math.sin(T*60):0;
 let s=`<g transform="translate(${x+j} ${y}) rotate(${rot})" opacity="${op}">`+sh(`<rect x="-52" y="-92" width="104" height="184" rx="20" fill="${CR}" ${o}/>`,9)+
 `<rect x="-36" y="-70" width="72" height="34" rx="10" fill="${HPL}" stroke="${INK}" stroke-width="4"/><rect x="-36" y="-26" width="58" height="12" rx="6" fill="${GREY}"/><rect x="-36" y="-6" width="44" height="12" rx="6" fill="${GREY}"/>`;
 if(buzz) s+=`<path d="M-74 -40 q-12 20 0 40 M-90 -50 q-18 30 0 60 M74 -40 q12 20 0 40 M90 -50 q18 30 0 60" stroke="${INK}" stroke-width="6" fill="none" stroke-linecap="round"/>`;
 return s+`</g>`;}
function clockD(x,y,op){const a=T*6;let s=`<g transform="translate(${x} ${y})" opacity="${op}">`+sh(`<circle r="70" fill="${CR}" ${o}/>`,9)+
 `<path d="M-50 -70 l-20 -22 M50 -70 l20 -22" stroke="${INK}" stroke-width="10" stroke-linecap="round"/><path d="M0 0 L0 -44" stroke="${INK}" stroke-width="8" stroke-linecap="round" transform="rotate(${a*30})"/><path d="M0 0 L30 0" stroke="${DP}" stroke-width="8" stroke-linecap="round" transform="rotate(${a*6})"/><circle r="8" fill="${INK}"/>`;
 return s+`</g>`;}
function bubbleD(x,y,txt,op,sc,flip){const w=Math.max(140,txt.length*12.5+40);return `<g transform="translate(${x} ${y}) scale(${(sc||1)*(flip?-1:1)} ${sc||1})" opacity="${op}">`+sh(`<path d="M${-w+20} -56 H${w-20} Q${w} -56 ${w} -36 V30 Q${w} 50 ${w-20} 50 H${-w+80} L${-w+44} 86 L${-w+54} 50 H${-w+20} Q${-w} 50 ${-w} 30 V-36 Q${-w} -56 ${-w+20} -56Z" fill="${CR}" ${o}/>`,9)+
 `<text x="0" y="12" transform="scale(${flip?-1:1} 1)" font-family="Inter" font-weight="800" font-size="40" fill="${INK}" text-anchor="middle">${txt}</text></g>`;}
function cloud(x,y,k){if(k<=0)return '';const s=E(k);
 const c=`<path d="M-230 70 Q-290 70 -280 10 Q-290 -60 -210 -70 Q-200 -150 -100 -140 Q-50 -200 30 -160 Q110 -210 170 -130 Q260 -140 260 -60 Q320 -20 280 50 Q290 120 200 120 H-190 Q-260 130 -230 70Z" fill="${CR}" ${o}/>`;
 return `<g transform="translate(${x} ${y}) scale(${s})">`+sh(c,16)+`</g>`+
  `<circle cx="${x-250*s}" cy="${y+170*s}" r="${22*s}" fill="${CR}" ${o}/><circle cx="${x-300*s}" cy="${y+225*s}" r="${13*s}" fill="${CR}" ${o}/>`;}
function car(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-90 10 L-70 -30 Q-60 -48 -30 -48 H30 Q56 -48 70 -26 L92 10 Q104 12 104 26 V40 H-104 V26 Q-104 12 -90 10Z" fill="${HP}" ${o}/><path d="M-52 -34 H-6 V4 H-74Z M8 -34 H36 Q50 -34 60 -16 L70 4 H8Z" fill="${CR}" stroke="${INK}" stroke-width="5"/><circle cx="-56" cy="42" r="22" fill="${CR}" ${o}/><circle cx="56" cy="42" r="22" fill="${CR}" ${o}/></g>`;}
function door(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-56" y="-90" width="112" height="180" rx="8" fill="${HY}" ${o}/><rect x="-34" y="-66" width="68" height="50" rx="4" fill="${CR}" stroke="${INK}" stroke-width="5"/><circle cx="34" cy="20" r="8" fill="${INK}"/><text x="0" y="-28" font-family="Inter" font-weight="900" font-size="34" fill="${INK}" text-anchor="middle">12</text></g>`;}
function sign(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-80" y="-44" width="160" height="88" rx="14" fill="${HPL}" ${o}/><text x="0" y="16" font-family="Inter Display" font-weight="900" font-size="50" fill="${INK}" text-anchor="middle">3:15</text></g>`;}
function qmark(x,y,op){return `<text x="${x}" y="${y}" font-family="Inter Display" font-weight="900" font-size="70" fill="${GREY}" text-anchor="middle" opacity="${op}">?</text>`;}
const SC={};
SC.eyes=function(t){
 // lid: open, shut 1.15-1.7; open 5.7-6.1 (why beat: clutter returns), shut 7.0-7.4; open 8.85-9.2 (asked), shut 9.9-10.3
 let lid=EIO(seg(t,1.15,1.7));
 if(t>3.7) lid=1-EIO(seg(t,3.7,4.0)); if(t>4.8) lid=EIO(seg(t,4.8,5.2));
 if(t>8.85) lid=1-EIO(seg(t,8.85,9.15)); if(t>9.9) lid=EIO(seg(t,9.9,10.3));
 const open=1-lid;
 const look=open>0.5?Math.sin(t*5.5)*(t<1.2?1:0.8):0;
 const smile=lid>0.9?Math.min(1,0.4+0.6*seg(t,11.4,11.9)+(t>2.6&&t<3.7?0.4:0)+(t>5.3?0.3:0)):0;
 // distractions: strong when eyes open, drop away when shut
 const dk=1-lid; // phone + clock in place from frame 0, gone (no ghosts) when the eyes are shut
 let s='';
 const head=face(330,1300,1.0,lid,look,smile,t);
 // cloud + memories, visible when the eyes are shut
 const qv=(t>8.75&&t<10.2)?EIO(seg(t,8.75,9.0))*(1-EIO(seg(t,9.95,10.2))):0; // question shown, memory fogged
 const cl1=seg(t,1.75,2.3)*(1-qv);
 s+=cloud(745,1110,cl1);
 const blur=(t>3.7&&t<5.3)?(1-seg(t,4.8,5.3))*seg(t,3.7,4.0):0; // items fog over while the eyes are open again
 const items=[[car,600,1070,2.3,'the car'],[door,770,1050,2.6,'the door'],[sign,920,1080,2.9,'the time']];
 items.forEach(([fn,x,y,t0,lb])=>{const k=pop(seg(t,t0,t0+0.35));if(k<=0||qv>0.5)return;
   s+=`<g opacity="${(1-0.75*blur)*(1-qv)}">${fn(x,y,0.9*k)}${label(x,1190,lb,-3,40*Math.min(k,1))}</g>`;
   if(blur>0.3) s+=qmark(x,y+20,blur);
   if(t>t0+0.3&&blur<0.3) s+=check(x+62,y-52,seg(t,t0+0.3,t0+0.7),24);});
 if(t>2.3&&t<3.7) s+=label(760,1330,'what you saw',-3,58);
 // distractions around the head
 const jig=(i)=>4*Math.sin(t*7+i);
 const base=0;
 s+=phoneD(115+jig(1)-60*lid,960,-12,open>0.5,base+(1-base)*dk);
 s+=clockD(905+60*lid,1330+jig(2),base+(1-base)*dk);
 s+=bubbleD(650+90*lid,1450+jig(3),'ding!',dk,0.9,false);
 if(t<1.15) s+=label(240,900,'ping!',-8,60)+label(915,1465,'tick, tock',-4,52);
 if(t>3.85&&t<4.85) s+=label(760,1585,'too much to look at',-3,56);
 if(t>5.15&&t<5.6) s+=label(760,1585,'eyes shut: it clears',-3,56);
 // asked: a speech bubble from someone off-screen (do this beat)
 if(qv>0){s+=bubbleD(740,1060,'So what happened?',qv,1.0*pop(seg(t,8.75,9.05)),true);}
 if(t>10.4&&t<11.5){const k=pop(seg(t,10.4,10.7)); s+=bubbleD(340,960,'A pink car, at 3:15.',1-seg(t,11.3,11.5),k,false);}
 s+=head;
 if(t>1.55&&t<2.2) s+=burst(330,1310,seg(t,1.55,2.2),HY);
 return s;};

// ================= SCENE 2: temptations off the desk =================
function desk(){return sh(`<path d="M60 1300 H1020 V1336 H60Z" fill="${HPL}" ${o}/>`,10)+`<path d="M120 1336 V1500 M960 1336 V1500" stroke="${INK}" stroke-width="10" stroke-linecap="round"/>`;}
function laptop(x,y,prog){let s=sh(`<path d="M-170 0 L-150 -230 H150 L170 0Z" fill="${CR}" ${o}/>`,10)+`<rect x="-136" y="-212" width="272" height="190" rx="6" fill="${BUT}" stroke="${INK}" stroke-width="5"/>`+
 `<rect x="-200" y="0" width="400" height="22" rx="8" fill="${CR}" ${o}/>`;
 s+=`<rect x="-110" y="-186" width="160" height="14" rx="7" fill="${INK}" opacity=".7"/><rect x="-110" y="-160" width="120" height="14" rx="7" fill="${INK}" opacity=".35"/>`;
 s+=`<rect x="-110" y="-110" width="220" height="34" rx="12" fill="${CR}" stroke="${INK}" stroke-width="5"/><rect x="-106" y="-106" width="${212*prog}" height="26" rx="10" fill="${HP}"/>`;
 return `<g transform="translate(${x} ${y})">${s}</g>`;}
function jar(x,y,rot,s){return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">`+sh(`<path d="M-70 -120 H70 Q90 -120 90 -96 V-10 Q90 0 80 0 H-80 Q-90 0 -90 -10 V-96 Q-90 -120 -70 -120Z" fill="#FFFFFF" fill-opacity=".9" ${o}/>`,9)+
 `<rect x="-78" y="-150" width="156" height="34" rx="10" fill="${HP}" ${o}/>`+
 [[-40,-40],[20,-36],[-10,-82],[44,-84]].map(([a,b])=>`<circle cx="${a}" cy="${b}" r="26" fill="#E9B872" stroke="${INK}" stroke-width="5"/><circle cx="${a-8}" cy="${b-6}" r="4" fill="${INK}"/><circle cx="${a+8}" cy="${b+6}" r="4" fill="${INK}"/>`).join('')+`</g>`;}
function pad(x,y,rot,s){return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">`+sh(`<path d="M-110 -30 Q-110 -60 -70 -60 H70 Q110 -60 110 -30 L130 40 Q136 70 106 72 Q80 74 60 40 H-60 Q-80 74 -106 72 Q-136 70 -130 40Z" fill="${HY}" ${o}/>`,9)+
 `<path d="M-74 -26 V6 M-90 -10 H-58" stroke="${INK}" stroke-width="9" stroke-linecap="round"/><circle cx="64" cy="-24" r="11" fill="${HP}" stroke="${INK}" stroke-width="4"/><circle cx="84" cy="-4" r="11" fill="${CR}" stroke="${INK}" stroke-width="4"/></g>`;}
function box(x,y,s,open){return `<g transform="translate(${x} ${y}) scale(${s})">`+sh(`<path d="M-130 -100 H130 V100 H-130Z" fill="#E9C48E" ${o}/>`,10)+
 `<path d="M-130 -100 L${-130-60*open} ${-150*open-100*(1-open)} M130 -100 L${130+60*open} ${-150*open-100*(1-open)}" stroke="${INK}" stroke-width="7"/>`+
 `<rect x="-122" y="-34" width="244" height="84" rx="10" fill="${CR}" stroke="${INK}" stroke-width="5" transform="rotate(-3)"/><text x="0" y="24" font-family="Caveat Brush" font-size="62" fill="${DP}" text-anchor="middle" transform="rotate(-3)">other room</text></g>`;}
function handD(x,y,rot,s){ // arm from the right, open hand hovering, fingers pointing down-left
 const fing=[[-70,-30,-150],[-62,-4,-160],[-50,22,-165],[-34,44,-170]].map(([fx,fy,a])=>`<rect x="${fx-58}" y="${fy-13}" width="70" height="26" rx="13" fill="${CR2}" ${o} stroke-width="6" transform="rotate(${a+180} ${fx} ${fy})"/>`).join('');
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">`+
 `<path d="M40 -46 H420 V46 H40Z" fill="${HPL}" ${o}/><path d="M40 -46 V46" stroke="${INK}" stroke-width="7"/>`+fing+
 `<path d="M44 -40 Q-40 -56 -70 -20 Q-80 20 -40 46 Q10 60 44 40Z" fill="${CR2}" ${o}/><path d="M-10 -44 Q-30 -90 -66 -86 Q-80 -80 -70 -66 Q-46 -60 -36 -36" fill="${CR2}" ${o} stroke-width="6"/></g>`;}
function meter(x,y,v,lab){return `<g transform="translate(${x} ${y})"><rect x="0" y="0" width="300" height="46" rx="16" fill="${CR}" ${o}/><rect x="6" y="6" width="${288*v}" height="34" rx="12" fill="${v<.35?HP:HY}"/>`+
 `<text x="150" y="-16" font-family="Caveat Brush" font-size="46" fill="${DP}" text-anchor="middle">${lab}</text></g>`;}
function doorway(x,y,open){return `<g transform="translate(${x} ${y})"><rect x="-10" y="-330" width="200" height="330" fill="${CR2}" ${o}/><g transform="translate(-10 -330) scale(${1-0.8*open} 1)"><rect x="0" y="0" width="200" height="330" fill="${HY}" ${o}/><circle cx="170" cy="170" r="10" fill="${INK}"/></g></g>`;}
SC.tempt=function(t){const dn=120*EIO(seg(t,3.0,3.4))*(1-EIO(seg(t,6.6,7.0)));return `<g transform="translate(540 ${1330+dn}) scale(1.35) translate(-540 -1300)">${SC.tempt0(t)}</g>`;};
SC.tempt0=function(t){
 let s=desk();
 // progress on the laptop grows in the why beat
 const prog=0.15+0.7*EIO(seg(t,6.9,8.6));
 s+=laptop(400,1300,prog);
 // phase A (0-3.0): hand hovers over the jar, 'resist...' then jar+pad fly into the box -> box slides off
 // phase B (3.0-6.6): reframe: Instead of (jar back, hand resisting, willpower meter drains) / Say (jar gone, meter full)
 // phase D (9.8-12.8): the box is carried out through a door
 const fly=EIO(seg(t,1.0,1.75)), boxIn=E(seg(t,0.55,0.95)), boxOut=EIO(seg(t,2.2,2.8));
 let jx=760,jy=1300,px=820,py=1236, jr=0, pr=-8, js=1, ps=0.8, show=true;
 // box target
 let bx=780+380*boxOut+380*(1-boxIn), by=1170;
 if(t<3.0){
   const tx=bx, ty=by-40; jx=760+(tx-760)*fly; jy=1300+(ty-1300)*fly-200*Math.sin(Math.PI*fly); jr=-30*fly; js=1-0.45*fly;
   px=290+(tx-290)*fly; py=1236+(ty-1236)*fly-260*Math.sin(Math.PI*fly); pr=-8+40*fly; ps=0.8-0.4*fly;
   const into=seg(t,1.6,1.78);
   s+=box(bx,by,0.85,1-seg(t,1.8,2.0));
   if(into<1) s+=`<g opacity="${1-into}">${jar(jx,jy,jr,js)}${pad(px,py,pr,ps)}</g>`;
   s+=burst(bx,by-120,seg(t,1.75,2.3),HY);
   if(t<1.0){ const hv=10*Math.sin(t*9); s+=handD(880+hv,1110,-12,0.75); s+=label(640,1000,'resist… resist…',-5,54);
     for(let i=0;i<2;i++){const k=(t*1.6+i*.5)%1;s+=`<path d="M${820+i*40} ${1040+60*k} q-10 16 0 24 q10 -8 0 -24z" fill="#BFE3F2" stroke="${INK}" stroke-width="4" opacity="${1-k}"/>`;} }
   if(t>2.1) s+=(t>2.6?check(720,1220,seg(t,2.6,3.0))+label(700,1110,'desk: clear',-4,60):'');
   return s; }
 if(t<6.6){ // reframe beat
   const say=t>4.8; const sw=EIO(seg(t,4.8,5.3));
   if(!say||sw<1){ s+=`<g opacity="${1-sw}">${jar(760,1300,0,1)}${handD(880+10*Math.sin(t*9),1110,-12,0.75)}${meter(600,1030,1-0.8*seg(t,3.2,4.7),'willpower')}</g>`; }
   if(say){ s+=`<g opacity="${sw}">${meter(600,1030,1,'willpower')}${check(720,1230,seg(t,5.3,5.8))}</g>`; s+=label(775,1140,'nothing to resist',-4,40); }
   return s; }
 if(t<9.8){ // why: goals tick on the laptop
   for(let i=0;i<3;i++){const k=seg(t,7.2+i*0.5,7.6+i*0.5); s+=check(640+i*95,1200,k,32);} s+=label(720,1110,'more done',-4,58);
   return s; }
 // do this: the box (with the jar + controller peeking out) is carried out of the door
 const d=doorway(700,1300, EIO(seg(t,9.9,10.3))*(1-EIO(seg(t,11.6,12.0))));
 const carry=EIO(seg(t,10.3,11.5));
 s+=d;
 if(t<11.7){ const cx=560+260*carry, cy=1200-10*Math.abs(Math.sin(t*8)); s+=`<g opacity="${1-seg(t,11.3,11.6)}">${jar(cx-40,cy-70,-10,0.55)}${pad(cx+50,cy-80,14,0.5)}${box(cx,cy,0.75,0)}</g>`; }
 if(t>11.9) s+=check(630,1230,seg(t,11.9,12.3))+label(640,935,'out of the room',-4,60);
 return s;};

let SPEC=null, T=0;
function draw(t){
 T=t; const S=SPEC, starts=S.starts, n=S.durs.length; let i=0; for(let k=0;k<n;k++) if(t>=starts[k]) i=k; const lt=t-starts[i];
 let svg=SC[S.scene](S.cover?S.cover_t:t);
 // wipe accent on every cut: a highlighter stripe sweeps across (meaningful: marks the new line)
 const sw=seg(lt,0,0.45); if(!S.cover&&i>0&&sw<1) svg=`<rect x="${-700+2100*E(sw)}" y="0" width="420" height="1920" fill="${i%2?HPL:HY}" opacity="${0.55*Math.sin(Math.PI*sw)}" transform="skewX(-14)"/>`+svg;
 document.getElementById('art').innerHTML=svg;
 document.getElementById('bg2').style.opacity=S.cover?0:(S.bg2[i]?1:0);
 for(let k=0;k<n;k++){const el=document.getElementById('b'+k); if(S.cover){el.style.opacity=0;continue;}
  let op=0,y=0,sc=1;
  if(k==i){ if(i==0){op=1;} else {const p=E(seg(lt,0.04,0.28)); op=p; y=50*(1-p); sc=0.96+0.04*BK(seg(lt,0.04,0.32));} }
  else if(k==i-1&&lt<0.1){const p=seg(lt,0,0.1); op=1-p; y=-50*E(p);}
  el.style.opacity=op; el.style.transform=`translateY(${y}px) scale(${sc})`;}
 const sk=document.getElementById('strike'); if(sk){const tt=S.cover?9:t; sk.style.width=(100*EIO(seg(tt,S.starts[1]+0.5,S.starts[1]+1.1)))+'%'; const sy=document.getElementById('say'); sy.style.opacity=E(seg(tt,S.starts[1]+1.6,S.starts[1]+1.9)); sy.style.transform=`rotate(1.2deg) translateY(${40*(1-E(seg(tt,S.starts[1]+1.6,S.starts[1]+1.9)))}px)`;}
 const f=document.getElementById('follow'); const fk=S.cover?0:(i==n-1?E(seg(lt,0.2,0.5)):0);
 f.style.opacity=fk; f.style.transform=`translateY(${40*(1-fk)}px)`;
 const st=document.getElementById('stampw'); st.style.opacity=S.cover?0:(i==n-1?fk:0);
}
"""


def reframe_cards():
    c = lambda bg, rot: (f"padding:30px 44px 36px;border-radius:34px;background:{bg};border:6px solid {INK};box-shadow:12px 12px 0 {INK};transform:rotate({rot}deg)")
    lab = "font-family:'Caveat Brush';font-size:70px;color:#E8336F;line-height:1"
    q = f"font-family:'Instrument Serif';font-size:104px;line-height:1;color:{INK};margin-top:8px;position:relative;display:inline-block"
    return (f"<div style='position:absolute;left:100px;right:100px;top:290px;display:flex;flex-direction:column;gap:40px'>"
            f"<div style='{c('#FFFDF4', -1.5)}'><div style=\"{lab}\">Instead of…</div><div style=\"{q}\">“I'll just resist it.”"
            f"<div id='strike' style='position:absolute;left:0;top:52%;height:8px;width:0;background:#E8336F;border-radius:4px'></div></div></div>"
            f"<div id='say' style='{c('#FFE27A', 1.2)};opacity:0'><div style=\"{lab}\">Say…</div><div style=\"{q}\">“It's not in this room.”</div></div></div>")


def H_(text, size, field="dots"):
    return edkit.dual(text, F[field], cls="H fit", style=f"font-size:{size}px")


def page(spec, cover_html=None):
    T = ""
    for k, b in enumerate(spec["beats"]):
        if b.get("html"):
            T += f'<div id="b{k}" style="position:absolute;left:0;top:0;width:{W}px;opacity:0">{reframe_cards()}</div>'
            continue
        T += (f'<div id="b{k}" style="position:absolute;left:90px;width:900px;top:{b.get("top", 300)}px;opacity:0;transform-origin:50% 0">'
              + (f'<div class="kick" style="font-size:{b.get("ks", 76)}px;margin-bottom:14px">{b["kick"]}</div>' if b.get("kick") else "")
              + H_(b["head"], b.get("fs", 124), b.get("field", "dots"))
              + (f'<div class="sub" style="font-size:{b.get("ss", 46)}px;margin-top:26px">{b["sub"]}</div>' if b.get("sub") else "")
              + (f'<div style="text-align:center;margin-top:22px"><span style="display:inline-block;padding:8px 22px;border-radius:99px;background:#FFFDF4;border:4px solid {INK};box-shadow:5px 5px 0 {INK};font:700 28px Inter;color:{INK};max-width:900px">{b["src"]}</span></div>' if b.get("src") else "")
              + "</div>")
    follow = (f'<div id="follow" style="position:absolute;left:0;right:0;top:{spec.get("follow_y", 1470)}px;text-align:center;opacity:0">'
              f'<span class="chip">Follow for one small<br>focus trick a day.</span></div>')
    stamp = f'<div id="stampw" style="position:absolute;left:0;top:0;opacity:0">{edkit.stamp("lockedhour", 850, 1560, size=150, rot=-10)}</div>'
    body = ('<div id="bg"></div><div id="bg2"></div>'
            f'<svg id="art" style="position:absolute;left:0;top:0" width="{W}" height="{H}" viewBox="0 0 {W} {H}"></svg>'
            + T + follow + stamp + (cover_html or "") + f"<script>{JS}</script>")
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"


def render(spec, tag, still=None, cover_html=None, cover_t=None, cover_out=None, cover_page=None):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    durs = spec["durs"]
    starts = [round(sum(durs[:k]), 4) for k in range(len(durs))]
    js = dict(durs=durs, starts=starts, scene=spec["scene"], cover=bool(cover_page or cover_html), cover_t=cover_t or 0,
              bg2=[b.get("bg2", False) for b in spec["beats"]])
    with sync_playwright() as p:
        br = p.chromium.launch()
        cov = bool(cover_out)
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2 if cov else 1)
        tf = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, dir=str(SCR))
        tf.write(cover_page if cover_page else page(spec, cover_html)); tf.close()
        pg.goto(Path(tf.name).as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        pg.evaluate(edkit.FIT_JS, 900)
        if cover_page:
            png = SCR / f"{tag}-cover.png"; pg.screenshot(path=str(png))
            Image.open(png).resize((W, H), Image.LANCZOS).convert("RGB").save(cover_out, quality=92, subsampling=0)
            br.close(); return cover_out
        pg.evaluate(f"SPEC={json.dumps(js)}")
        if still:
            ims = []
            for ts in still:
                pg.evaluate(f"draw({ts})"); pth = SCR / f"{tag}-still.png"; pg.screenshot(path=str(pth))
                ims.append(Image.open(pth).convert("RGB").resize((360, 640)))
            sh = Image.new("RGB", (365 * len(ims), 640), "white")
            for k, im in enumerate(ims):
                sh.paste(im, (365 * k, 0))
            sh.save(SCR / f"{tag}-stills.jpg", quality=85); br.close(); return None
        fdir = SCR / f"{tag}-frames"; shutil.rmtree(fdir, ignore_errors=True); fdir.mkdir(parents=True)
        total = sum(durs); n = int(round(total * FPS))
        for fr in range(n):
            pg.evaluate(f"draw({fr / FPS})")
            pg.screenshot(path=str(fdir / f"{fr:04d}.jpg"), type="jpeg", quality=93)
        br.close()
    os.unlink(tf.name)
    return fdir, total, starts


def encode(fdir, total, music, hits, out_mp4):
    a = SCR / f"{out_mp4.stem}.wav"
    inputs = ["-i", str(REPO / music)]
    filt = [f"[0:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.04,afade=t=out:st={total-0.7:.3f}:d=0.7[m]"]
    mix = ["[m]"]
    for k, (pt, name, vol) in enumerate(hits):
        inputs += ["-i", str(REPO / LIB["sfx"][name]["file"])]
        filt.append(f"[{k+1}:a]volume={vol},adelay={int(pt*1000)}|{int(pt*1000)}[p{k}]")
        mix.append(f"[p{k}]")
    filt.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[o]")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[o]",
                    "-ar", "48000", "-ac", "2", str(a)], check=True)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(fdir / "%04d.jpg"), "-i", str(a),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "19", "-profile:v", "high",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out_mp4)], check=True)
    shutil.rmtree(fdir); a.unlink()


# ------------------------------------------------------------------ covers (dedicated, style-menu layouts)
def cover_sticky():
    """Style 13 sticky-note list (quiet): lined note card, red margin, tape, Caveat Brush title, ticked Caveat items,
    on the LH butter dot grid, plus the drawn shut-eyes face (the Reel's one object)."""
    paper = "#FFFDF4"
    card = (f"<div style='position:absolute;left:110px;top:330px;width:860px;height:1010px;background:{paper};transform:rotate(-2deg);"
            f"border:6px solid {INK};border-radius:10px;box-shadow:14px 14px 0 {INK};"
            f"background-image:linear-gradient({paper} 330px,transparent 330px),repeating-linear-gradient({paper} 0 118px,rgba(80,110,180,.30) 118px 121px)'>"
            f"<div style='position:absolute;left:96px;top:0;bottom:0;width:4px;background:rgba(220,80,80,.55)'></div>"
            f"<div style='position:absolute;left:130px;right:40px;top:50px;font-family:\"Caveat Brush\";font-size:128px;line-height:.98;color:#E8336F'>"
            f"Can't recall<br>what you saw?</div>"
            f"<ul style='position:absolute;left:130px;right:30px;top:352px;list-style:none;font-family:Caveat;font-weight:700;font-size:92px;line-height:120px;color:{INK}'>"
            f"<li><span style='color:#E8336F'>✓</span> close your eyes</li><li><span style='color:#E8336F'>✓</span> then answer</li></ul></div>"
            f"<div style='position:absolute;left:420px;top:300px;width:240px;height:66px;background:rgba(255,212,59,.8);transform:rotate(3deg);border:2px solid rgba(27,23,23,.25)'></div>")
    art = ("<svg style='position:absolute;left:0;top:0' width='1080' height='1920' viewBox='0 0 1080 1920'>"
           "<g transform='translate(-60 -40)'><script>document.currentScript.parentNode.innerHTML=face(760,1240,1.05,1,0,1,0)</script></g></svg>")
    stamp = edkit.stamp("lockedhour", 80, 1180, size=170, rot=-12)
    return card + art + stamp


def cover_reframe():
    """Style 7 Ep.01 reframe 'Instead of... / Say...' (quiet): two cards, struck line in the first, Instrument Serif quotes,
    Caveat Brush labels, on the LH pink field with the dot grid; hook line on top in Inter Display 900."""
    hook = (f"<div style='position:absolute;left:90px;width:900px;top:300px'>" + H_("Fewer temptations / beat more *willpower.*", 120, "pink") + "</div>")
    c = lambda bg, rot: (f"padding:40px 48px;border-radius:36px;background:{bg};border:6px solid {INK};box-shadow:12px 12px 0 {INK};transform:rotate({rot}deg)")
    cards = (f"<div style='position:absolute;left:110px;right:110px;top:640px;display:flex;flex-direction:column;gap:44px'>"
             f"<div style='{c('#FFFDF4', -1.5)}'><div style=\"font-family:'Caveat Brush';font-size:78px;color:#E8336F;line-height:1\">Instead of…</div>"
             f"<div style=\"font-family:'Instrument Serif';font-size:104px;line-height:1;color:{INK};margin-top:10px;text-decoration:line-through;text-decoration-thickness:7px;text-decoration-color:#E8336F\">“I'll just resist it.”</div></div>"
             f"<div style='{c('#FFE27A', 1.2)}'><div style=\"font-family:'Caveat Brush';font-size:78px;color:#E8336F;line-height:1\">Say…</div>"
             f"<div style=\"font-family:'Instrument Serif';font-size:104px;line-height:1;color:{INK};margin-top:10px\">“It's not in this room.”</div></div></div>")
    stamp = edkit.stamp("lockedhour", 90, 1420, size=160, rot=-12)
    return hook + cards + stamp


def cover_hook():
    """Style 1 Look B big-headline cover in the LH zine look (loud): Inter Display 900 hook with highlighter pills,
    Caveat Brush save-line, the drawn eyes-shut face (ink border + hard offset shadow) with its thought cloud, stamp."""
    hook = f"<div style='position:absolute;left:90px;width:900px;top:300px'>" + H_("Close your eyes / to remember / *more.*", 156, "dots") + "</div>"
    save = ("<div style=\"position:absolute;left:90px;width:900px;top:800px;text-align:center;font-family:'Caveat Brush';font-size:64px;"
            "color:#E8336F;transform:rotate(-3deg)\">try it next time someone asks ↓</div>")
    art = ("<svg id='cv' style='position:absolute;left:0;top:0' width='1080' height='1920' viewBox='0 0 1080 1920'></svg>"
           "<script>T=0;document.getElementById('cv').innerHTML=cloud(745,1110,1)+car(600,1070,0.9)+door(770,1050,0.9)+sign(920,1080,0.9)"
           "+label(600,1190,'the car',-3,40)+label(770,1190,'the door',-3,40)+label(920,1190,'the time',-3,40)"
           "+check(662,1018,1,24)+check(832,998,1,24)+check(982,1028,1,24)+face(330,1300,1.0,1,0,1,0)</script>")
    stamp = edkit.stamp("lockedhour", 820, 1400, size=160, rot=-12)
    return hook + save + art + stamp


def cover_page(kind):
    bg = "#FFD5E5" if kind == "reframe" else "#FFF0A6"
    inner = {"sticky": cover_sticky, "reframe": cover_reframe, "hook": cover_hook}[kind]()
    css = CSS.replace("background-color:#FFF0A6", f"background-color:{bg}", 1)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body><div id='bg'></div>"
            f"<script>{JS}</script>{inner}</body></html>")


# ------------------------------------------------------------------ specs
B100 = 60 / 99.4   # lh-x-tick-boom
B126 = 60 / 126.0  # lh-x-lock-in
SPECS = {
    "eyes": dict(
        id="lh-reel-1028am-close-your-eyes", scene="eyes", music="media/music/library/v4/lh-x-lock-in.mp3",
        durs=[1.8, 3.8, 3.1, 2.8, 2.9], cover="hook", follow_y=740,
        hits=[(1.6, "sfx-x-whoosh-hit", 0.35), (5.6, "sfx-x-paper-slap", 0.3), (8.7, "sfx-x-paper-slap", 0.3), (11.5, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(head="Close your eyes / to remember / *more.*", fs=150, top=300),
            dict(kick="mind goes blank when someone asks?", ks=62, head="Less to look at, / *more room* / to remember.", fs=116, bg2=True),
            dict(kick="the research", head="People with eyes shut / recalled *more correct* / *details.*", fs=108,
                 sub="In 4 of 5 experiments, with no extra mistakes.", ss=41, src="Perfect et al. 2008 · Law and Human Behavior"),
            dict(kick="Do this, when someone asks:", head="Close your eyes, / *then answer.*", fs=124),
            dict(head="Close your eyes / to remember / *more.*", fs=124, top=300),
        ]),
    "tempt": dict(
        id="lh-reel-1030-fewer-temptations", scene="tempt", music="media/music/library/v4/lh-x-phone-down.mp3",
        durs=[3.0, 3.6, 3.2, 3.0, 2.0], cover="reframe",
        hits=[(1.0, "sfx-x-whoosh-hit", 0.35), (3.0, "sfx-x-paper-slap", 0.3), (6.6, "sfx-x-paper-slap", 0.3), (9.8, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(head="Fewer temptations / beat more / *willpower.*", fs=128, top=300),
            dict(html=True, head="Instead of… “I'll just resist it.” Say… “It's not in this room.”", bg2=True),
            dict(kick="the research", head="Students who met fewer / temptations made more / *progress on goals.*", fs=96,
                 sub="How hard they resisted didn't predict it.", ss=46,
                 src="Milyavskaya &amp; Inzlicht 2017 · Social Psychological and Personality Science"),
            dict(kick="Do this:", head="Move one temptation / *out of the room.*", fs=110),
            dict(head="Fewer temptations / beat more / *willpower.*", fs=128, top=300),
        ]),
}

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    still = next((a[8:] for a in sys.argv if a.startswith("--still=")), None)
    for key in args or SPECS:
        s = SPECS[key]
        cov = OUT / f"{s['id']}-cover.jpg"
        render(s, key, cover_out=cov, cover_page=cover_page(s["cover"]))
        print("cover", cov)
        if "--cover-only" in sys.argv:
            continue
        if still:
            render(s, key, still=[float(x) for x in still.split(",")]); print("stills", SCR / f"{key}-stills.jpg"); continue
        fdir, total, starts = render(s, key)
        out = OUT / f"{s['id']}.mp4"
        encode(fdir, total, s["music"], s["hits"], out)
        print(out, round(total, 2), starts)

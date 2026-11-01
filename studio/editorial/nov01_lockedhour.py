#!/usr/bin/env python3
"""Locked Hour, Nov 1 studio build (Social studio, Sun Nov 1 2026, 9:30 am Toronto).

Three "do this tonight" Reels, each ONE drawn object acting the action out in the LH zine scene look, built on the
Oct 27/28 LH kits (studio/editorial/oct27_lockedhour.py JS + oct28_lockedhour.py JS_EXTRA, render(), encode():
imported, not edited; k28.page is swapped at runtime for this file's page(), which adds the Part 2 line).

  shower  lh-reel-1101-warm-shower   Sun Nov 1 19:00 ET. "Fall asleep sooner", Part 1. Object: the shower.
          Haghayegh et al. 2019, Sleep Medicine Reviews 46:124-135 (doi 10.1016/j.smrv.2019.04.008).
  lamp    lh-reel-1102-one-lamp      Mon Nov 2 19:00 ET. Part 2 (promised by A). Object: a small lamp.
          Gooley et al. 2011, J Clin Endocrinol Metab 96(3):E463-E472 (doi 10.1210/jc.2010-2098).
  timer   lh-reel-1103-break-timer   Tue Nov 3 19:00 ET. Object: a kitchen timer (LH signature object).
          Biwer et al. 2023, British Journal of Educational Psychology 93(S2):353-367.
  oneword lh-oneword-06              Wed Nov 4 17:00 ET, One Word No. 6 "Doodle." (nov01_lockedhour_feed.py).
          Andrade 2010, Applied Cognitive Psychology 24(1):100-106 (doi 10.1002/acp.1561).

  python3 studio/editorial/nov01_lockedhour.py shower|lamp|timer|oneword [--cover-only] [--still=0,1.5,3]
Music: existing LH v4 library tracks only (tools/music-library.json), -14 LUFS. No new music. 1 render worker.
"""
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
os.environ["LH_SCR"] = "/tmp/claude-0/nov01-lockedhour"
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import edkit  # noqa: E402
import oct27_lockedhour as k27  # noqa: E402
import oct28_lockedhour as k28  # noqa: E402

OUT = REPO / "media/studio-nov01/lockedhour"
OUT.mkdir(parents=True, exist_ok=True)
k28.OUT = OUT
SCR = k28.SCR
W, H, INK = 1080, 1920, k27.INK
CSS, F = k27.CSS, k27.F

JS_NOV = r"""
// ================= Nov 1 extras =================
const SKIN='#FFE3C8', WAT='#8FC8EE', WATL='#CFE8FA';
function tilesD(x0,y0,w,h){let s=`<rect x="${x0}" y="${y0}" width="${w}" height="${h}" rx="26" fill="${CR}" ${o}/>`;
 for(let x=x0+100;x<x0+w;x+=100) s+=`<path d="M${x} ${y0+6} V${y0+h-6}" stroke="${INK}" stroke-width="3" opacity=".18"/>`;
 for(let y=y0+100;y<y0+h;y+=100) s+=`<path d="M${x0+6} ${y} H${x0+w-6}" stroke="${INK}" stroke-width="3" opacity=".18"/>`;
 return sh(`<rect x="${x0}" y="${y0}" width="${w}" height="${h}" rx="26" fill="${CR}" ${o}/>`,12)+s;}
function curtainD(x,y,h){let s='';const w=150;
 s+=sh(`<path d="M${x} ${y} H${x+w} Q${x+w-20} ${y+h*0.5} ${x+w+10} ${y+h} H${x-10} Q${x+20} ${y+h*0.5} ${x} ${y}Z" fill="${HPL}" ${o}/>`,10);
 for(let i=1;i<4;i++) s+=`<path d="M${x+i*w/4} ${y+14} Q${x+i*w/4-14} ${y+h*0.5} ${x+i*w/4+6} ${y+h-10}" stroke="${HP}" stroke-width="7" fill="none" stroke-linecap="round" opacity=".8"/>`;
 for(let i=0;i<5;i++) s+=`<circle cx="${x+12+i*(w-24)/4}" cy="${y-6}" r="11" fill="${HY}" stroke="${INK}" stroke-width="5"/>`;
 return `<path d="M${x-30} ${y-6} H${x+760}" stroke="${INK}" stroke-width="9" stroke-linecap="round"/>`+s;}
// the shower: pipe from the wall, head angled down-left, streams (on 0..1 grows them), knob angle k 0..1
function showerD(hx,hy,on,t,knob){let s='';
 s+=`<path d="M${hx+260} ${hy-150} H${hx+70} Q${hx+40} ${hy-150} ${hx+40} ${hy-120} V${hy-60}" stroke="${INK}" stroke-width="30" fill="none" stroke-linecap="round"/>`+
    `<path d="M${hx+260} ${hy-150} H${hx+70} Q${hx+40} ${hy-150} ${hx+40} ${hy-120} V${hy-60}" stroke="#E6DCCB" stroke-width="16" fill="none" stroke-linecap="round"/>`;
 // streams
 if(on>0){const L=(1630-hy-34)*on;
  for(let i=0;i<9;i++){const x0=hx-78+i*20, x1=x0-60+i*22; const off=-((t*900+i*37)%120);
   s+=`<path d="M${x0} ${hy+34} L${x0+(x1-x0)*on} ${hy+34+L}" stroke="${WAT}" stroke-width="9" stroke-linecap="round" stroke-dasharray="60 60" stroke-dashoffset="${off}" opacity=".95"/>`;}}
 s+=`<g transform="translate(${hx} ${hy}) rotate(18)">`+sh(`<path d="M-22 -70 H22 V-26 L100 24 Q104 44 84 44 H-84 Q-104 44 -100 24 L-22 -26Z" fill="${HY}" ${o}/>`,9);
 for(let i=0;i<7;i++) s+=`<circle cx="${-66+i*22}" cy="34" r="5" fill="${INK}"/>`;
 s+=`</g>`;
 if(knob!=null){const kx=hx+250, ky=hy+300, a=-50+100*knob;
  s+=sh(`<circle cx="${kx}" cy="${ky}" r="62" fill="${CR2}" ${o}/>`,9)+
   `<path d="M${kx-92} ${ky-30} A100 100 0 0 1 ${kx-40} ${ky-90}" stroke="${WAT}" stroke-width="12" fill="none" stroke-linecap="round"/>`+
   `<path d="M${kx+40} ${ky-90} A100 100 0 0 1 ${kx+92} ${ky-30}" stroke="${HP}" stroke-width="12" fill="none" stroke-linecap="round"/>`+
   `<g transform="rotate(${a} ${kx} ${ky})"><rect x="${kx-14}" y="${ky-96}" width="28" height="100" rx="14" fill="${HP}" ${o}/></g><circle cx="${kx}" cy="${ky}" r="14" fill="${INK}"/>`;}
 return s;}
function steamD(x,y,t,k,n){if(k<=0)return '';let s='';n=n||4;
 for(let i=0;i<n;i++){const ph=((t*0.45+i/n)%1); const yy=y-260*ph, xx=x+(i-(n-1)/2)*95+18*Math.sin(t*2.4+i);
  s+=`<path d="M${xx} ${yy} q-26 -34 0 -68 q26 -34 0 -68" stroke="#FFFFFF" stroke-width="16" fill="none" stroke-linecap="round" opacity="${k*0.95*Math.sin(Math.PI*ph)}"/>`+
     `<path d="M${xx} ${yy} q-26 -34 0 -68 q26 -34 0 -68" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round" opacity="${k*0.35*Math.sin(Math.PI*ph)}"/>`;}
 return s;}
function bather(x,y,s,lid,smile,t,towel){let f=recol(face(0,0,1,lid,0,smile,t),'#7A4A2E',SKIN);
 if(towel>0) f+=`<g opacity="${towel}">`+sh(`<path d="M-150 -40 Q-170 -210 0 -215 Q170 -210 150 -40 Q80 -110 0 -105 Q-80 -110 -150 -40Z" fill="${HPL}" ${o}/>`,8)+
   `<path d="M-90 -150 Q0 -190 90 -150 M-120 -95 Q0 -150 120 -95" stroke="${HP}" stroke-width="8" fill="none" stroke-linecap="round"/></g>`;
 return `<g transform="translate(${x} ${y}) scale(${s})">${f}</g>`;}
function thermoD(x,y,lvl,op){let s=`<g transform="translate(${x} ${y})" opacity="${op}">`+sh(`<rect x="-34" y="-260" width="68" height="300" rx="34" fill="${CR}" ${o}/><circle cx="0" cy="70" r="58" fill="${CR}" ${o}/>`,9);
 const top=40-270*lvl; s+=`<rect x="-18" y="${top}" width="36" height="${70-top}" rx="16" fill="${HP}"/><circle cx="0" cy="70" r="42" fill="${HP}"/>`;
 for(let i=0;i<5;i++) s+=`<path d="M34 ${-210+i*50} h-22" stroke="${INK}" stroke-width="5" stroke-linecap="round"/>`;
 return s+`</g>`;}
function arrowDown(x,y,k){if(k<=0)return '';const L=170*E(k);return `<path d="M${x} ${y} V${y+L}" stroke="${DP}" stroke-width="16" stroke-linecap="round"/>`+
 `<path d="M${x-36} ${y+L-36} L${x} ${y+L} L${x+36} ${y+L-36}" stroke="${DP}" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="${seg(k,.6,1)}"/>`;}
function clockChip(x,y,txt,k,col){if(k<=0)return '';const w=Math.max(300,txt.length*38+60);return `<g transform="translate(${x} ${y}) scale(${pop(k)})">`+sh(`<rect x="${-w/2}" y="-62" width="${w}" height="124" rx="24" fill="${col||HPL}" ${o}/>`,9)+
 `<text x="0" y="24" font-family="Inter Display" font-weight="900" font-size="70" fill="${INK}" text-anchor="middle">${txt}</text></g>`;}
function bedIcon(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})">`+sh(`<rect x="-120" y="-20" width="240" height="60" rx="16" fill="${CR}" ${o}/><rect x="-130" y="-110" width="34" height="170" rx="12" fill="${HY}" ${o}/>`,8)+
 `<ellipse cx="-50" cy="-36" rx="44" ry="22" fill="#FFFFFF" ${o}/><path d="M-10 -40 Q60 -64 118 -36 V-20 H-10Z" fill="${HPL}" ${o}/></g>`;}
function showerIcon(x,y,s,t){return `<g transform="translate(${x} ${y}) scale(${s}) translate(${-x} ${-y})">${showerD(x,y,0.22,t,null)}</g>`;}
function zz(x,y,t,t0){let s='';for(let i=0;i<3;i++){const k=((t-t0)*0.6+i/3)%1; if(t<t0+i*0.4) continue;
  s+=`<text x="${x+60*k+i*8}" y="${y-170*k}" font-family="Inter Display" font-weight="900" font-size="${48+26*k}" fill="${DP}" opacity="${Math.sin(Math.PI*k)}">z</text>`;}return s;}

// Caveat label on a cream pill (legible over drawings)
function pillLab(x,y,txt,size,col,rot){size=size||56;const w=txt.length*size*0.43+56,h=size*1.35;
 return `<g transform="rotate(${rot==null?-3:rot} ${x} ${y})">`+sh(`<rect x="${x-w/2}" y="${y-h*0.72}" width="${w}" height="${h}" rx="${h/2}" fill="${CR}" stroke="${INK}" stroke-width="5"/>`,6)+
  `<text x="${x}" y="${y}" font-family="Caveat Brush" font-size="${size}" fill="${col||DP}" text-anchor="middle">${txt}</text></g>`;}
// gate fix (Nov 1 CD): quicker cuts, no half-faded text frames; same structure as the Oct 27 kit draw()
function draw(t){
 T=t; const S=SPEC, starts=S.starts, n=S.durs.length; let i=0; for(let k=0;k<n;k++) if(t>=starts[k]) i=k; const lt=t-starts[i];
 let svg=SC[S.scene](S.cover?S.cover_t:t);
 const sw=seg(lt,0,0.3); if(!S.cover&&i>0&&sw<1) svg=`<rect x="${-700+2100*E(sw)}" y="0" width="420" height="1920" fill="${i%2?HPL:HY}" opacity="${0.4*Math.sin(Math.PI*sw)}" transform="skewX(-14)"/>`+svg;
 document.getElementById('art').innerHTML=svg;
 document.getElementById('bg2').style.opacity=S.cover?0:(S.bg2[i]?1:0);
 for(let k=0;k<n;k++){const el=document.getElementById('b'+k); if(S.cover){el.style.opacity=0;continue;}
  let op=0,y=0,sc=1;
  if(k==i){ if(i==0){op=1;} else {const p=E(seg(lt,0.0,0.1)); op=p; y=30*(1-p); sc=0.97+0.03*BK(seg(lt,0.0,0.25));} }
  el.style.opacity=op; el.style.transform=`translateY(${y}px) scale(${sc})`;}
 const f=document.getElementById('follow'); const fk=S.cover?0:(i==n-1?E(seg(lt,0.1,0.25)):0);
 f.style.opacity=fk; f.style.transform=`translateY(${30*(1-fk)}px)`;
 const st=document.getElementById('stampw'); st.style.opacity=S.cover?0:(i==n-1?fk:0);
}
const Q=(t,a)=>seg(t,a,a+0.1); // quick label fade-in

// ================= SCENE A: warm shower, 90 minutes before bed =================
function bathroom(t,on,knob,lid,smile,towel,steam){let s='';
 s+=tilesD(110,820,860,880);
 s+=curtainD(140,850,700);
 s+=showerD(640,1000,on,t,knob);
 s+=bather(560,1420,0.82,lid,smile,t,towel);
 s+=steamD(560,1180,t,steam,4);
 // tub rim in front
 s+=sh(`<rect x="90" y="1640" width="900" height="70" rx="30" fill="${CR}" ${o}/>`,10);
 return s;}
SC.shower=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==0){
  const knob=EIO(seg(t,0.35,0.8)), on=E(seg(t,0.75,1.35)), lid=EIO(seg(t,1.4,1.8))*0.95+(t<0.8?0.35:0)*(1-seg(t,0.8,1.4)), sm=0.15+0.85*seg(t,1.5,1.9);
  s+=bathroom(t,on,knob,lid,sm,0,seg(t,1.0,1.6));
  if(t<0.85) s+=pillLab(345,1130,'long day…',58);
  if(t>1.35) s+=`<g opacity="${Q(t,1.35)}">`+pillLab(345,1130,'warm, not hot',58)+`</g>`;
  s+=burst(740,1300,seg(t,1.9,2.35),HY);
  return s;}
 if(ph==1){ // after: towel on, body cools, sleepy
  const lvl=0.78-0.38*EIO(seg(t,3.0,4.4));
  s+=tilesD(110,820,860,880);
  s+=curtainD(140,850,700);
  s+=showerD(640,1000,1-E(seg(t,2.4,2.8)),t,null);
  s+=bather(470,1420,0.82,EIO(seg(t,4.4,4.8)),0.8,t,E(seg(t,2.5,2.9)));
  s+=thermoD(830,1360,lvl,seg(t,2.7,3.0));
  s+=arrowDown(950,1100,seg(t,3.1,3.7));
  if(t>3.4) s+=`<g opacity="${Q(t,3.4)}">`+pillLab(360,1130,'then you cool down',54)+`</g>`;
  if(t>4.6) s+=zz(620,1260,t,4.6);
  s+=sh(`<rect x="90" y="1640" width="900" height="70" rx="30" fill="${CR}" ${o}/>`,10);
  return s;}
 if(ph==2){ // research: timeline shower -> bed, 1 to 2 hours
  const ln=EIO(seg(t,5.6,6.1)), a=pop(seg(t,5.6,5.85)), b=pop(seg(t,5.95,6.25)), br=E(seg(t,6.3,6.7));
  s+=`<path d="M150 1420 H${150+780*ln}" stroke="${INK}" stroke-width="10" stroke-linecap="round"/>`;
  if(a>0) s+=`<g transform="translate(250 1420) scale(${a}) translate(-250 -1420)">`+showerIcon(290,1230,0.8,t)+`</g>`+`<circle cx="250" cy="1420" r="18" fill="${HP}" ${o}/>`;
  if(b>0) s+=`<g transform="translate(830 1320) scale(${b*1.05})">`+bedIcon(0,0,1)+`</g><circle cx="840" cy="1420" r="18" fill="${HY}" ${o}/>`;
  if(t>5.8) s+=`<g opacity="${Q(t,5.8)}">`+label(250,1520,'warm shower',-3,58)+`</g>`;
  if(t>6.2) s+=`<g opacity="${Q(t,6.2)}">`+label(840,1520,'bed',-3,58)+`</g>`;
  if(br>0) s+=`<path d="M290 1180 Q290 1130 340 1130 H${340+(400*br)} Q${740+40*br} 1130 ${740+40*br} 1180" stroke="${DP}" stroke-width="9" fill="none" stroke-linecap="round" opacity="${br}"/>`+
    `<g opacity="${Q(t,6.5)}">`+label(545,1075,'1 to 2 hours',-3,68)+`</g>`;
  if(t>7.0) s+=zz(800,1220,t,7.0);
  return s;}
 if(ph==3){ // do this: clock chip 9:30 pm, the shower turns on again, "10 minutes is enough"
  const knob=EIO(seg(t,9.5,9.9)), on=E(seg(t,9.8,10.3));
  s+=bathroom(t,on,knob,EIO(seg(t,10.4,10.8)),0.3+0.7*seg(t,10.5,10.9),0,seg(t,10.0,10.6));
  s+=clockChip(340,1000,'9:30 pm',seg(t,9.1,9.35),HY);
  if(t>11.0) s+=check(860,1480,seg(t,11.0,11.4),44);
  return s;}
 // end: the scene again, smaller, below the hook + Part 2 + follow lines
 s+=`<g transform="translate(540 1370) scale(.62) translate(-540 -1270)">`+bathroom(t,1,1,1,1,0,1)+`</g>`;
 return s;};
// ================= SCENE B: one lamp after dinner (Part 2) =================
const NIGHT='#4A3F78';
function roomB(t,ceil,lamp,lid,smile,moonK){let s='';
 s+=sh(`<rect x="110" y="820" width="860" height="880" rx="26" fill="${CR2}" ${o}/>`,12);
 // window, night outside
 s+=`<rect x="640" y="900" width="260" height="230" rx="10" fill="${NIGHT}" ${o}/>`;
 if(moonK>0) s+=`<g transform="translate(770 ${1060-60*moonK}) scale(${0.45*moonK})">`+moonD(0,0,1)+`</g>`;
 s+=`<path d="M770 900 V1130 M640 1015 H900" stroke="${INK}" stroke-width="7"/>`;
 // ceiling light + glow cone
 if(ceil>0) s+=`<path d="M330 1010 L150 1690 H830 L560 1010Z" fill="#FFF7C2" opacity="${0.75*ceil}"/>`;
 s+=`<path d="M445 826 V950" stroke="${INK}" stroke-width="6"/>`+sh(`<path d="M380 1010 L405 950 H485 L510 1010Z" fill="${ceil>0.5?'#FFF3A0':'#E6DCCB'}" ${o}/>`,7);
 if(ceil>0.5) for(let i=0;i<5;i++){const a=(Math.PI*(0.15+0.7*i/4));s+=`<path d="M${445+70*Math.cos(a)} ${1020+60*Math.sin(a)} l${30*Math.cos(a)} ${30*Math.sin(a)}" stroke="${HY}" stroke-width="8" stroke-linecap="round" opacity="${ceil}"/>`;}
 // dim overlay when the big light is off
 s+=`<rect x="116" y="826" width="848" height="868" rx="22" fill="#B98A6A" opacity="${0.2*(1-ceil)}"/>`;
 // lamp glow
 if(lamp>0) s+=`<clipPath id="rcB"><rect x="116" y="826" width="848" height="868" rx="22"/></clipPath><g clip-path="url(#rcB)"><circle cx="860" cy="1330" r="${170+40*lamp}" fill="#FFE9A8" opacity="${0.6*lamp}"/><circle cx="860" cy="1330" r="110" fill="#FFF3C4" opacity="${0.6*lamp}"/></g>`;
 // sofa + person
 s+=sh(`<rect x="150" y="1330" width="560" height="120" rx="40" fill="${HPL}" ${o}/>`,10);
 s+=recol(face(430,1300,0.7,lid,0,smile,t),'#3B2A20','#FFE27A');
 s+=sh(`<rect x="130" y="1440" width="600" height="150" rx="40" fill="${HP}" ${o}/>`,10)+`<path d="M200 1590 V1650 M660 1590 V1650" stroke="${INK}" stroke-width="12" stroke-linecap="round"/>`;
 // side table + THE lamp
 s+=sh(`<rect x="770" y="1490" width="180" height="24" rx="8" fill="${HY}" ${o}/>`,8)+`<path d="M800 1514 V1650 M920 1514 V1650" stroke="${INK}" stroke-width="10" stroke-linecap="round"/>`;
 s+=`<path d="M860 1490 V1380" stroke="${INK}" stroke-width="10"/>`+sh(`<ellipse cx="860" cy="1484" rx="52" ry="14" fill="${CR}" ${o}/>`,6);
 s+=sh(`<path d="M790 1385 L815 1290 H905 L930 1385Z" fill="${lamp>0.5?'#FFD43B':'#E6DCCB'}" ${o}/>`,8);
 return s;}
SC.lamp=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==0){
  const lamp=E(seg(t,0.95,1.15)), ceil=1-EIO(seg(t,1.25,1.45));
  s+=roomB(t,ceil,lamp,0.45*(1-seg(t,1.4,1.8))+0.35*seg(t,1.4,1.8),0.2+0.6*seg(t,1.5,1.9),0);
  if(t<0.95) s+=label(540,780,'every light on at 9 pm',-3,60);
  if(t>1.2) s+=`<g opacity="${Q(t,1.2)}">`+pillLab(800,1215,'one lamp',60)+`</g>`;
  s+=burst(860,1330,seg(t,1.0,1.5),HY);
  return s;}
 if(ph==1){ // the moon rises = body says night; ceiling flicks on -> moon drops; off again -> moon back
  const on=(t>3.7&&t<4.6)?1:0;
  const mk=t<3.7?E(seg(t,2.6,3.2)):(t<4.6?1-E(seg(t,3.75,4.05)):E(seg(t,4.7,5.1)));
  s+=roomB(t,on,1,on?0.1:0.35,on?0.1:0.8,mk);
  if(t>2.9&&t<3.7) s+=pillLab(540,790,'dim light: body knows it\'s night',48);
  if(t>3.75&&t<4.6) s+=pillLab(540,790,'bright light: body thinks it\'s day',48,INK);
  if(t>4.8) s+=pillLab(540,790,'dim light: body knows it\'s night',48);
  return s;}
 if(ph==2){ // research: the body's night, dim vs room light (about 90 min shorter)
  const g1=EIO(seg(t,5.9,6.6)), g2=EIO(seg(t,6.2,7.0)), cut=seg(t,7.1,7.3);
  s+=label(540,1020,"how long the \u201cit's night\u201d signal lasted",-2,58);
  const row=(y,txt,frac,g,col)=>`<text x="100" y="${y-22}" font-family="Inter" font-weight="800" font-size="54" fill="${INK}">${txt}</text>`+
   sh(`<rect x="100" y="${y}" width="880" height="110" rx="26" fill="${CR}" ${o}/>`,9)+`<rect x="110" y="${y+10}" width="${860*frac*g}" height="90" rx="18" fill="${col}"/>`;
  s+=row(1130,'In dim light',1.0,g1,NIGHT);
  s+=row(1340,'In room light',0.82,g2,'#9D93C9');
  if(g1>0.95) s+=`<g transform="translate(140 1185) scale(.32)">`+moonD(0,0,1)+`</g>`;
  if(cut>0) s+=`<rect x="${110+860*0.82}" y="1350" width="${860*0.18}" height="90" rx="18" fill="none" stroke="${DP}" stroke-width="7" stroke-dasharray="16 12" opacity="${cut}"/>`+
   `<g opacity="${cut}" transform="translate(540 1530) rotate(-2)">`+sh(`<rect x="-415" y="-62" width="830" height="104" rx="52" fill="${HP}" ${o}/>`,8)+`<text x="0" y="12" font-family="Inter Display" font-weight="900" font-size="62" fill="${INK}" text-anchor="middle">about 90 minutes less</text></g>`;
  return s;}
 if(ph==3){
  const lamp=E(seg(t,9.35,9.55)), ceil=1-EIO(seg(t,9.65,9.85));
  s+=roomB(t,ceil,lamp,0.45-0.1*seg(t,9.8,10.2),0.2+0.6*seg(t,9.9,10.3),E(seg(t,10.2,10.7)));
  s+=burst(860,1330,seg(t,9.8,10.3),HY);
  s+=clockChip(400,940,'after dinner',seg(t,9.05,9.3),HY);
  if(t>11.0) s+=check(640,1170,seg(t,11.0,11.4),40);
  return s;}
 s+=`<g transform="translate(540 1400) scale(.62) translate(-540 -1270)">`+roomB(t,0,1,0.35,0.8,1)+`</g>`;
 return s;};
// ================= SCENE C: break timer (24 on, 6 off) =================
function timerD(x,y,s,mins,shake,col,num){col=col||HP;const j=shake?5*Math.sin(T*70):0, r=Math.sin(T*55)*shake*6;
 let g=sh(`<rect x="-26" y="-150" width="52" height="40" rx="10" fill="${INK}"/><circle r="122" fill="${HY}" ${o}/>`,10);
 g+=`<circle r="94" fill="${CR}" stroke="${INK}" stroke-width="5"/>`;
 const a=Math.max(0,Math.min(60,mins))/60*2*Math.PI;
 if(mins>0.05){const x1=94*Math.sin(a), y1=-94*Math.cos(a), lg=a>Math.PI?1:0;
  g+= mins>=59.9?`<circle r="94" fill="${col}"/>`:`<path d="M0 0 L0 -94 A94 94 0 ${lg} 1 ${x1} ${y1}Z" fill="${col}"/>`;}
 for(let i=0;i<12;i++){const b=i*Math.PI/6; g+=`<path d="M${86*Math.sin(b)} ${-86*Math.cos(b)} L${(i%3?74:66)*Math.sin(b)} ${-(i%3?74:66)*Math.cos(b)}" stroke="${INK}" stroke-width="${i%3?4:6}" stroke-linecap="round"/>`;}
 g+=`<circle r="40" fill="${CR}" stroke="${INK}" stroke-width="5"/><text x="0" y="16" font-family="Inter Display" font-weight="900" font-size="46" fill="${INK}" text-anchor="middle">${num!=null?num:Math.round(mins)}</text>`;
 if(shake) g+=`<path d="M-150 -90 q-20 30 0 60 M-176 -104 q-30 44 0 88 M150 -90 q20 30 0 60 M176 -104 q30 44 0 88" stroke="${INK}" stroke-width="7" fill="none" stroke-linecap="round"/>`;
 return `<g transform="translate(${x+j} ${y}) rotate(${r}) scale(${s})">${g}</g>`;}
function bookD(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})">`+sh(`<path d="M0 0 L-150 -20 V-110 L0 -90Z" fill="#FFFFFF" ${o}/><path d="M0 0 L150 -20 V-110 L0 -90Z" fill="#FFFFFF" ${o}/>`,8)+
 [0,1,2].map(i=>`<path d="M-120 ${-80+i*20+4} L-30 ${-70+i*20}" stroke="${INK}" stroke-width="5" opacity=".35"/><path d="M30 ${-70+i*20} L120 ${-80+i*20+4}" stroke="${INK}" stroke-width="5" opacity=".35"/>`).join('')+`</g>`;}
function deskScene(t,mins,shake,col,lid,smile,num){let s='';
 s+=sh(`<rect x="110" y="820" width="860" height="880" rx="26" fill="${CR2}" ${o}/>`,12);
 // night window
 s+=`<rect x="160" y="880" width="230" height="200" rx="10" fill="#4A3F78" ${o}/><path d="M275 880 V1080 M160 980 H390" stroke="${INK}" stroke-width="7"/>`+`<g transform="translate(330 950) scale(.3)">`+moonD(0,0,1)+`</g>`;
 s+=recol(face(380,1270,0.78,lid,0,smile,t),'#FF5CA8','#FFE27A');
 s+=sh(`<path d="M120 1440 H960 V1478 H120Z" fill="${HPL}" ${o}/>`,10)+`<path d="M180 1478 V1660 M900 1478 V1660" stroke="${INK}" stroke-width="12" stroke-linecap="round"/>`;
 s+=bookD(380,1450,1.0);
 s+=timerD(760,1300,0.95,mins,shake,col,num);
 return s;}
SC.timer=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==0){
  const m=24*EIO(seg(t,0.45,1.35));
  s+=deskScene(t,m,false,HP,0.55*(1-seg(t,1.4,1.6)),0.1+0.8*seg(t,1.5,1.9));
  if(t<0.9) s+=label(540,780,'one more hour… no break',-3,60);
  if(t>1.35) s+=`<g opacity="${Q(t,1.35)}">`+pillLab(760,1110,'24 minutes',60)+`</g>`;
  s+=burst(760,1300,seg(t,1.4,1.9),HY);
  return s;}
 if(ph==1){
  const down=24*(1-seg(t,2.6,3.4)), ring=t>3.4&&t<3.95, brk=6*EIO(seg(t,4.1,4.5));
  const m=t<3.95?down:brk;
  s+=deskScene(t,m,ring,t<3.95?HP:'#8FC8EE',t>3.95?1:0,t>3.95?1:0.5,t<3.95?null:Math.round(brk));
  if(ring) s+=pillLab(760,1110,'ring!',66);
  if(t>4.15) s+=pillLab(720,1110,'6-minute break',60);
  if(t>4.15) s+=label(540,780,'stand up, stretch, water',-3,60);
  return s;}
 if(ph==2){ // research: two students, no numbers (the paper's abstract gives directions only)
  const a=pop(seg(t,5.8,6.15)), b=pop(seg(t,6.1,6.45));
  // droopy: heavy lids, flat mouth, head slumped, sweat drop, grey shirt; bright: wide eyes, big smile, sparkles
  s+=`<g transform="translate(290 1250) rotate(-12) scale(${0.8*a})">`+recol(face(0,0,1,0.72,0,-0.6,t),'#C9C2B8','#D9D2C8')+`</g>`;
  if(a>0.9) s+=`<path d="M395 1110 q-16 26 0 36 q16 -10 0 -36z" fill="#BFE3F2" stroke="${INK}" stroke-width="5"/>`;
  s+=`<g transform="translate(800 1240) scale(${0.8*b})">`+recol(face(0,0,1,0,0,1,t),'#FF5CA8','#FFE27A')+`</g>`;
  if(b>0.9) [[670,1110],[940,1110],[930,1380]].forEach(([x,y],i)=>{const k=0.6+0.4*Math.sin(t*6+i*2);s+=`<path d="M${x} ${y-26*k} L${x+8*k} ${y-8*k} L${x+26*k} ${y} L${x+8*k} ${y+8*k} L${x} ${y+26*k} L${x-8*k} ${y+8*k} L${x-26*k} ${y} L${x-8*k} ${y-8*k}Z" fill="${HY}" stroke="${INK}" stroke-width="4"/>`;});
  if(t>6.3){const k=Q(t,6.3); s+=`<g opacity="${k}">`+label(290,945,'breaks when they',-3,56)+label(290,1000,'felt like it',-3,56)+`</g>`;}
  if(t>6.6){const k=Q(t,6.6); s+=`<g opacity="${k}">`+label(800,945,'timed',-3,56)+label(800,1000,'breaks',-3,56)+`</g>`;}
  if(t>6.9) s+=pillLab(290,1550,'more tired',60,INK);
  if(t>7.3) s+=check(960,1530,seg(t,7.3,7.6),40)+`<g opacity="${Q(t,7.3)}">`+pillLab(790,1550,'fresher',64)+`</g>`;
  return s;}
 if(ph==3){ // do this: close-up timer, 24 on, then 6 off
  const on=24*EIO(seg(t,9.3,10.0)), off=6*EIO(seg(t,10.7,11.1));
  const m=t<10.6?on:off;
  s+=timerD(540,1180,1.8,m,t>10.3&&t<10.6,t<10.6?HP:'#8FC8EE',Math.round(m));
  if(t>9.9) s+=label(300,1530,'24 on',-4,90,t<10.6?DP:INK);
  if(t>10.9) s+=label(780,1530,'6 off',-4,90);
  if(t>11.3) s+=check(800,960,seg(t,11.3,11.6),50);
  return s;}
 s+=`<g transform="translate(540 1400) scale(.62) translate(-540 -1270)">`+deskScene(t,24,false,HP,0,1)+`</g>`;
 return s;};
"""


def page(spec, cover_html=None):
    """oct28 page() plus an optional Part 2 line inside the follow block (shown on the last beat with the follow line)."""
    T = ""
    for k, b in enumerate(spec["beats"]):
        T += (f'<div id="b{k}" style="position:absolute;left:90px;width:900px;top:{b.get("top", 300)}px;opacity:0;transform-origin:50% 0">'
              + (f'<div class="kick" style="font-size:{b.get("ks", 70)}px;margin-bottom:14px">{b["kick"]}</div>' if b.get("kick") else "")
              + k28.H_(b["head"], b.get("fs", 124), b.get("field", "dots"))
              + (f'<div class="sub" style="font-size:{b.get("ss", 46)}px;margin-top:24px">{b["sub"]}</div>' if b.get("sub") else "")
              + (f'<div style="text-align:center;margin-top:20px"><span style="display:inline-block;padding:8px 22px;border-radius:99px;background:#FFFDF4;border:4px solid {INK};box-shadow:5px 5px 0 {INK};font:700 30px Inter;color:{INK};max-width:900px">{b["src"]}</span></div>' if b.get("src") else "")
              + "</div>")
    p2 = ""
    if spec.get("part2_line"):
        p2 = (f'<div style="margin-bottom:26px"><span style="display:inline-block;padding:10px 34px;border-radius:20px;background:#FF5CA8;border:6px solid {INK};'
              f'box-shadow:8px 8px 0 {INK};font:900 60px \'Inter Display\';color:{INK};letter-spacing:-.02em;transform:rotate(-2deg)">{spec["part2_line"]}</span></div>')
    follow = (f'<div id="follow" style="position:absolute;left:0;right:0;top:{spec.get("follow_y", 1470)}px;text-align:center;opacity:0">'
              f'{p2}<span class="chip">Follow for one small<br>focus trick a day.</span></div>')
    sx, sy = spec.get("stamp_xy", (850, 1560))
    stamp = f'<div id="stampw" style="position:absolute;left:0;top:0;opacity:0">{edkit.stamp("lockedhour", sx, sy, size=150, rot=-10)}</div>'
    bg2 = spec.get("bg2col", "#FFF6E5")
    css = CSS.replace("opacity:0;background-color:#FFF6E5", f"opacity:0;background-color:{bg2}")
    body = ('<div id="bg"></div><div id="bg2"></div>'
            f'<svg id="art" style="position:absolute;left:0;top:0" width="{W}" height="{H}" viewBox="0 0 {W} {H}"></svg>'
            + T + follow + stamp + (cover_html or "") + f"<script>{k27.JS}{k28.JS_EXTRA}{JS_NOV}</script>")
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"


k28.page = page  # k28.render() looks page() up at call time


def svg_cover(js_expr):
    return ("<svg id='cv' style='position:absolute;left:0;top:0' width='1080' height='1920' viewBox='0 0 1080 1920'></svg>"
            f"<script>T=0;document.getElementById('cv').innerHTML={js_expr}</script>")


# ------------------------------------------------------------------ covers (dedicated, style-menu layouts)
def cover_kinetic_shower():
    """Style 5 kinetic big text, cover frame (loud): a giant '90' in Inter Display 900 with a pink highlighter stripe,
    'minutes before bed' in a pill, the drawn shower + steam, Caveat line, stamp. On butter dot grid."""
    big = (f"<div style='position:absolute;left:0;right:0;top:250px;text-align:center'>"
           f"<div style='position:absolute;left:120px;right:120px;top:250px;height:120px;background:#FF5CA8;opacity:.85;border-radius:60px;transform:rotate(-2deg)'></div>"
           f"<div class='H' style='position:relative;font-size:420px;line-height:.9;letter-spacing:-.05em'>90</div></div>")
    line = ("<div style='position:absolute;left:90px;width:900px;top:690px'>" + k28.H_("*minutes before bed:* / take a warm shower.", 96, "dots") + "</div>")
    top = ("<div style='position:absolute;left:90px;width:900px;top:150px'>" + k28.H_("Can't fall asleep?", 84, "dots") + "</div>")
    note = ("<div style=\"position:absolute;left:90px;width:900px;top:930px;text-align:center;font-family:'Caveat Brush';font-size:64px;"
            "color:#E8336F;transform:rotate(-3deg)\">you'll fall asleep sooner ↓</div>")
    art = svg_cover("'<g transform=\"translate(540 1400) scale(.62) translate(-540 -1270)\">'+bathroom(0.4,1,1,1,1,0,1)+'</g>'")
    stamp = edkit.stamp("lockedhour", 70, 1180, size=150, rot=-12)
    return top + big + line + note + art + stamp


def cover_compare_lamp():
    """Style 8 original templates, compare (quiet): Inter Display hook with pill, two side-by-side panels of the Reel's
    drawn room ('every light on' with an X, 'one lamp' with a tick), Caveat labels, stamp. On the LH cream dot grid."""
    hook = ("<div style='position:absolute;left:90px;width:900px;top:300px'>" + k28.H_("Your ceiling light / says *it's daytime.*", 128, "cream") + "</div>")
    note = ("<div style=\"position:absolute;left:90px;width:900px;top:600px;text-align:center;font-family:'Caveat Brush';font-size:62px;"
            "color:#E8336F;transform:rotate(-3deg)\">after dinner, switch to one lamp ↓</div>")
    art = svg_cover("'<g transform=\"translate(30 760) scale(.5) translate(-110 -820)\">'+roomB(0,1,0,0.45,0.2,0)+'</g>'"
                    "+'<g transform=\"translate(560 760) scale(.5) translate(-110 -820)\">'+roomB(0,0,1,0.35,0.8,1)+'</g>'"
                    "+xmark(245,1260,40,1)+check(775,1260,1,44)"
                    "+label(245,1385,'every light on',-3,58,INK)+label(775,1385,'one small lamp',-3,58)")
    stamp = edkit.stamp("lockedhour", 820, 1420, size=150, rot=-12)
    return hook + note + art + stamp


def cover_lookb_timer():
    """Style 1 Look B big-headline (loud) in the LH zine look: Inter Display 900 hook with pink pill, Caveat Brush save-line
    + arrow, the Reel's drawn kitchen timer (one object, set to 24), round stamp. On butter dot grid."""
    hook = "<div style='position:absolute;left:90px;width:900px;top:300px'>" + k28.H_("Studying tonight? / *24 minutes on, 6 off.*", 124, "pink") + "</div>"
    save = ("<div style=\"position:absolute;left:90px;width:900px;top:600px;text-align:center;font-family:'Caveat Brush';font-size:66px;"
            "color:#E8336F;transform:rotate(-3deg)\">a timer for your study breaks ↓</div>")
    art = svg_cover("timerD(540,1180,2.3,24,false,HP,24)")
    stamp = edkit.stamp("lockedhour", 840, 1420, size=150, rot=-12)
    return hook + save + art + stamp


def cover_page(kind):
    bg = {"kinetic": "#FFF0A6", "compare": "#FFF6E5", "lookb": "#FFD5E5"}.get(kind, "#FFF0A6")
    inner = {"kinetic": cover_kinetic_shower, "compare": cover_compare_lamp, "lookb": cover_lookb_timer}[kind]()
    css = CSS.replace("background-color:#FFF0A6", f"background-color:{bg}", 1)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body><div id='bg'></div>"
            f"<script>{k27.JS}{k28.JS_EXTRA}{JS_NOV}</script>{inner}</body></html>")


# ------------------------------------------------------------------ specs
SPECS = {
    "shower": dict(
        id="lh-reel-1101-warm-shower", scene="shower", music="media/music/library/v4/lh-x-phone-down.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.6], cover="kinetic", follow_y=640, stamp_xy=(70, 1390), part2_line="Part 2 tomorrow, 7 pm.",
        hits=[(0.35, "sfx-x-sticker-pop", 0.25), (0.8, "sfx-x-swoosh-in", 0.3), (1.9, "sfx-x-sticker-pop", 0.35),
              (5.6, "sfx-x-whoosh-hit", 0.25), (9.5, "sfx-x-swoosh-in", 0.3), (12.0, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(kick="Can't fall asleep?", ks=76, head="Shower 90 minutes / *before bed.*", fs=132, top=290),
            dict(kick="try this", head="It helps you / *fall asleep sooner.*", fs=112,
                 sub="Afterwards your body cools down,<br>and that cool-down tells your body<br>it's time to sleep.", ss=44, bg2=True),
            dict(kick="the research", head="A warm shower 1 to 2 hours / before bed helped people / *fall asleep faster.*", fs=92,
                 sub="A review of 17 studies. Even 10 minutes<br>in the water helped.", ss=46,
                 src="Haghayegh et al. 2019 · Sleep Medicine Reviews"),
            dict(kick="Do this tonight:", head="Bed at 11? / Shower warm *at 9:30.*", fs=118,
                 sub="10 minutes in the water is enough.", ss=48, bg2=True),
            dict(kick="Can't fall asleep?", ks=76, head="Shower 90 minutes / *before bed.*", fs=132, top=290),
        ]),
    "lamp": dict(
        id="lh-reel-1102-one-lamp", scene="lamp", music="media/music/library/v4/lh-x-lock-in.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.6], cover="compare", follow_y=640, stamp_xy=(70, 1390),
        hits=[(1.0, "sfx-x-sticker-pop", 0.3), (1.35, "sfx-x-swoosh-in", 0.3), (3.75, "sfx-x-sticker-pop", 0.3),
              (5.6, "sfx-x-whoosh-hit", 0.25), (9.4, "sfx-x-sticker-pop", 0.3), (12.0, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(head="Your ceiling light / says *it's daytime.*", fs=128, top=300),
            dict(kick="fall asleep sooner, part 2", head="Bright room light tells / your body *it's still day.*", fs=104,
                 sub="Dim light lets melatonin, your body's<br>\u201cit's night\u201d signal, rise on time.", ss=44, bg2=True),
            dict(kick="the research", head="In room light, the body's / \u201cit's night\u201d signal lasted / *about 90 minutes less.*", fs=96,
                 sub="Compared with dim light, before bed.", ss=46,
                 src="Gooley et al. 2011 · J Clin Endocrinol Metab"),
            dict(kick="Do this tonight:", head="Big light off. / *One small lamp on.*", fs=118,
                 sub="From after dinner until bed.", ss=50, bg2=True),
            dict(head="Your ceiling light / says *it's daytime.*", fs=128, top=300),
        ]),
    "timer": dict(
        id="lh-reel-1103-break-timer", scene="timer", music="media/music/library/v4/lh-x-tick-boom.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.6], cover="lookb", follow_y=640, stamp_xy=(70, 1390),
        hits=[(0.45, "sfx-x-tick-tock", 0.3), (1.4, "sfx-x-sticker-pop", 0.35), (3.4, "sfx-x-tick-tock", 0.35),
              (5.6, "sfx-x-whoosh-hit", 0.25), (9.3, "sfx-x-tick-tock", 0.3), (11.3, "sfx-x-sticker-pop", 0.3), (12.0, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(head="Studying tonight? / *24 minutes on, 6 off.*", fs=124, top=300),
            dict(kick="try this", head="Planned breaks keep you / *fresher than winging it.*", fs=100,
                 sub="Work until it rings. Then really stop.", ss=48, bg2=True),
            dict(kick="the research", head="Students on timed breaks / felt *less tired, more focused*", fs=94,
                 sub="and got the same work done<br>in less time.", ss=46,
                 src="Biwer et al. 2023 · Brit J Educ Psychol"),
            dict(kick="Do this tonight:", head="Timer: 24 minutes on, / *6 off.*", fs=118,
                 sub="That's the timing from the study.<br>Then the next round.", ss=46, bg2=True),
            dict(head="Studying tonight? / *24 minutes on, 6 off.*", fs=124, top=300),
        ]),
}

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    still = next((a[8:] for a in sys.argv if a.startswith("--still=")), None)
    for key in args or list(SPECS):
        if key == "oneword":
            import nov01_lockedhour_feed as fd_; fd_.oneword(); print("done oneword"); continue
        s = SPECS[key]
        cov = OUT / f"{s['id']}-cover.jpg"
        if not still:
            k28.render(s, key, cover_page=cover_page(s["cover"]), cover_out=cov)
            print("cover", cov)
        if "--cover-only" in sys.argv:
            continue
        if still:
            k28.render(s, key, still=[float(x) for x in still.split(",")]); print("stills", SCR / f"{key}-stills.jpg"); continue
        fdir, total, starts = k28.render(s, key)
        out = OUT / f"{s['id']}.mp4"
        k28.encode(fdir, total, s["music"], s["hits"], out)
        print(out, round(total, 2), starts)

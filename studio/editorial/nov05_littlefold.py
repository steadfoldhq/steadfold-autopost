#!/usr/bin/env python3
"""Nov 5 (Social studio, Littlefold maker). Extends nov04_littlefold.py (imported, not edited) for its kit
(reel_story RS.frames / page / fonts, oct27 helpers label/check/noRing/hearts/sparkle, nov01 encode with -nostdin).

A  lf-reel-1110-stair-gates-2   (Tue Nov 10 19:00, no trial, standalone)
   "Stairs need 2 gates: top and bottom."
   NEW SCENE COMPOSITION (CD Nov 4: the last 3 LF Reels shared the sky + text-on-top + small object on a floor line):
   an indoor side-cutaway staircase that fills the TOP 50% of the frame edge to edge (sunlit butter wall, arched
   window, light beam, pink stair runner), a moving CAMERA that travels the stairs (wide -> top gate close-up ->
   banister close-up -> wide), and the words in a cream band at the BOTTOM under a wavy edge. No sky, no washing line.
   Frame 0: the staircase + 2 half-open gates + the hook (1 text block); gates swing shut and get "1" / "2" badges by 1.2 s;
   a ball rolls into the bottom gate and bounces back; "Keep them up until at least age 2." from 1.9 s.
   COVER: follow-the-line (style-menu #9, quiet): a dashed berry path climbs from the floor through stop 1 (bottom gate)
   to stop 2 (top gate, screwed in).

Facts (checked Nov 5 2026):
  NHS 'Baby and toddler safety' (nhs.uk/baby/first-aid-and-safety/safety/baby-and-toddler-safety/, last reviewed 19 Feb 2026):
    "Carry on using safety gates at the top and bottom of stairs until your infant is at least 2 years old.";
    "If the gaps between banisters or balcony railings are more than 6.5cm (2.5 inches) wide, cover them with boards or
    safety netting."; "Hold on to the handrail when carrying your baby up and down stairs, in case you trip."
  CPS caringforkids 'Keep your young child safe around the house' (May 2023): "Fix them securely to studs in the wall at
    the top of stairs."; "Pressure mounted gates are not safe at the top of stairways."; "Install gates with vertical bars
    made of metal or wood."

    python3 studio/editorial/nov05_littlefold.py stairs [--still=0.0,1.5,...] [--cover-only] [--no-cover]
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import nov04_littlefold as N4  # noqa: E402  (nothing renders on import)
N1, S27, RS = N4.N1, N4.S27, N4.RS
SCRD = Path("/tmp/claude-0/nov05-littlefold")
SCRD.mkdir(parents=True, exist_ok=True)
RS.SCR = SCRD
K, F, INK, KICK, B = RS.K, RS.F, RS.INK, RS.KICK, RS.B
W, H = RS.W, RS.H
OUT = RS.REPO / "media" / "studio-nov05" / "littlefold"
LIB = RS.LIB
FOLLOW = N1.FOLLOW
BB = N1.BB  # lf-x-sunny-bounce, 112.3 bpm

JS5 = r"""
// ===================== Nov 5: stair gates (indoor cutaway + travelling camera) =====================
const BER5='#D9497A', WALL1='#FFF4D6', WALL2='#FFE6CF', WOOD='#F3CFA0', WOOD2='#E2B47E', RUN='#FFB9CF', STEP='#FFD3AE', RAIL='#FFFDF7';
const SX0=230, SY0=880, SR=95, SU=80, SN=7;          // stairs: foot (230,880), 7 steps of 95 x 80; top landing y=320
const LAND=SY0-SN*SU, SXT=SX0+SN*SR;                  // 320, 895
const railY=x=>SY0-SU-170-(x-SX0)*SU/SR;               // handrail line, parallel to the pitch
function gate(hx,y0,w,h,sw,dir,opt){ // a gate with vertical bars; hinge at hx, swings (sw 0..1 shut) toward dir (+1 right / -1 left)
 opt=opt||{}; const s=0.22+0.78*sw, x0=dir>0?hx:hx-w;
 let g=`<rect x="${x0}" y="${y0}" width="${w}" height="${h}" rx="10" fill="#FFE3EC" fill-opacity=".75" ${o} stroke-width="7"/>`;
 g+=`<rect x="${x0}" y="${y0}" width="${w}" height="20" rx="9" fill="${BUT}" ${o} stroke-width="5"/><rect x="${x0}" y="${y0+h-20}" width="${w}" height="20" rx="9" fill="${BUT}" ${o} stroke-width="5"/>`;
 for(let i=1;i<6;i++){const bx=x0+w*i/6; g+=`<path d="M${bx} ${y0+14} V${y0+h-14}" stroke="${PL}" stroke-width="6" stroke-linecap="round"/>`;}
 const lx=dir>0?x0+w-14:x0+14; g+=`<rect x="${lx-12}" y="${y0+h*0.38}" width="24" height="34" rx="7" fill="${BUT}" ${o} stroke-width="4"/>`;
 const rot=opt.rot||0;
 return `<g transform="translate(${hx} ${y0+h}) rotate(${rot}) scale(${s} 1) translate(${-hx} ${-(y0+h)})">${g}</g>`;}
function badge(x,y,n,k){if(k<=0)return '';const a=E(k);return `<g transform="translate(${x} ${y}) scale(${0.4+0.6*a})" opacity="${Math.min(1,a*2)}"><circle r="38" fill="${BER5}" ${o} stroke-width="4"/><text y="17" font-family="Poppins" font-weight="700" font-size="50" text-anchor="middle" fill="#FFF8EE">${n}</text></g>`;}
function screw(x,y,k){ // a screw going in: head turns, sparkle when seated
 if(k<=0) return ''; const a=E(k), r=a*360*2;
 return `<g transform="translate(${x} ${y})" opacity="${Math.min(1,k*4)}"><circle r="13" fill="#EEF3F8" ${o} stroke-width="4"/><path d="M-8 0 H8" stroke="${PL}" stroke-width="4" stroke-linecap="round" transform="rotate(${r})"/></g>`;}
function world(st){ // st: {g1,g2 gate shut 0..1, ball x, pads 0/1, brackets 0..1, screws 0..1, wiggle deg, net 0..1, t}
 const t=st.t||0;
 let s=`<rect x="-400" y="-300" width="1900" height="1300" fill="url(#wallg)"/>`;
 // arched window + sun + beam (beam drifts)
 s+=`<path d="M100 560 V360 Q100 250 215 250 Q330 250 330 360 V560 Z" fill="#BFE0F7" ${o} stroke-width="7"/>`;
 s+=`<circle cx="262" cy="335" r="40" fill="#FFE27E"/><path d="M110 520 q40 -46 90 -16 q30 -40 70 -6 q40 -10 50 30 V552 H110Z" fill="#A8D59A" opacity=".9"/>`;
 s+=`<path d="M215 252 V560 M100 410 H330" stroke="#FFFDF7" stroke-width="12"/><path d="M90 566 H340" stroke="${PL}" stroke-width="8" stroke-linecap="round"/>`;
 const bd=10*Math.sin(t*0.9);
 s+=`<path d="M330 300 L${1000+bd} ${700+bd} L${820+bd} 900 L330 560Z" fill="#FFF6B8" opacity=".33"/>`;
 // little frame on the wall + skirting
 s+=`<rect x="640" y="120" width="120" height="96" rx="10" fill="#FFD6E3" ${o} stroke-width="5" transform="rotate(-3 700 168)"/><path d="M670 190 l22 -30 l18 20 l12 -12 l20 22" stroke="${PL}" stroke-width="4" fill="none"/>`;
 // floor
 s+=`<rect x="-400" y="${SY0}" width="${SX0+400}" height="400" fill="${WOOD}"/><path d="M-400 ${SY0} H${SX0}" stroke="${PL}" stroke-width="6"/>`;
 s+=`<path d="M-200 ${SY0+40} H120 M-60 ${SY0+70} H180" stroke="${WOOD2}" stroke-width="5" stroke-linecap="round"/>`;
 // stairs mass + runner
 let p=`M${SX0} 1300 V${SY0}`; for(let k=0;k<SN;k++) p+=` V${SY0-(k+1)*SU} H${SX0+(k+1)*SR}`; p+=` H1500 V1300 Z`;
 s+=`<path d="${p}" fill="${STEP}" ${o} stroke-width="6"/>`;
 for(let k=0;k<SN;k++){const x=SX0+k*SR, y=SY0-(k+1)*SU; s+=`<rect x="${x}" y="${y}" width="${SR+2}" height="16" fill="${RUN}"/><path d="M${x} ${y} V${y+SU}" stroke="${PL}" stroke-width="4" opacity=".35"/><rect x="${x}" y="${y+16}" width="10" height="${SU-16}" fill="${RUN}" opacity=".85"/>`;}
 s+=`<path d="M${SX0} ${SY0} L${SXT} ${LAND}" stroke="${PL}" stroke-width="0"/>`;
 // spindles (2 per step) + handrail + newels
 for(let k=0;k<SN;k++){[26,70].forEach(dx=>{const x=SX0+k*SR+dx, y=SY0-(k+1)*SU; s+=`<rect x="${x-7}" y="${railY(x)}" width="14" height="${y-railY(x)}" rx="5" fill="${RAIL}" ${o} stroke-width="4"/>`;});}
 if(st.net>0){const n=E(st.net), xa=SX0+2*SR, xb=xa+(3*SR)*n; // safety netting rolls along the banister over steps 3-5
   let m=`<path d="M${xa} ${railY(xa)} L${xb} ${railY(xb)} L${xb} ${SY0-SU*(1+(xb-SX0)/SR)} L${xa} ${SY0-SU*(1+(xa-SX0)/SR)} Z" fill="#FFC9D6" fill-opacity=".55" ${o} stroke-width="4"/>`;
   for(let x=xa+16;x<xb;x+=22) m+=`<path d="M${x} ${railY(x)} L${x} ${SY0-SU*(1+(x-SX0)/SR)}" stroke="${BER5}" stroke-width="2" opacity=".6"/>`;
   for(let d=40;d<230;d+=30) m+=`<path d="M${xa} ${railY(xa)+d} L${xb} ${railY(xb)+d}" stroke="${BER5}" stroke-width="2" opacity=".6"/>`;
   s+=`<g>${m}</g>`;}
 s+=`<path d="M${SX0-30} ${railY(SX0-30)} L${SXT+20} ${railY(SXT+20)}" stroke="${PL}" stroke-width="30" stroke-linecap="round"/><path d="M${SX0-30} ${railY(SX0-30)} L${SXT+20} ${railY(SXT+20)}" stroke="#F6A98A" stroke-width="18" stroke-linecap="round"/>`;
 s+=`<rect x="${SX0-34}" y="${railY(SX0)-30}" width="40" height="${SY0-railY(SX0)+30}" rx="8" fill="#F6A98A" ${o}/><circle cx="${SX0-14}" cy="${railY(SX0)-38}" r="20" fill="#F6A98A" ${o}/>`;
 s+=`<rect x="${SXT+4}" y="${railY(SXT)-30}" width="40" height="${LAND-railY(SXT)+30}" rx="8" fill="#F6A98A" ${o}/><circle cx="${SXT+24}" cy="${railY(SXT)-38}" r="20" fill="#F6A98A" ${o}/>`;
 // wall posts the gates latch onto
 s+=`<rect x="40" y="660" width="40" height="${SY0-690}" rx="8" fill="#FFFDF7" ${o} stroke-width="5"/>`;
 s+=`<rect x="1080" y="110" width="44" height="${LAND-130}" rx="8" fill="#FFFDF7" ${o} stroke-width="5"/>`;
 // bottom gate: hinge on the bottom newel, swings shut toward the wall post on the left
 s+=gate(SX0-34,690,SX0-34-80,190,st.g1,-1);
 // top gate: hinge on the top newel, latch side on the wall post (pads or screwed brackets)
 const tg0=SXT+44, tgw=1080-tg0;
 s+=gate(tg0,LAND-170,tgw,170,st.g2,1,{rot:st.wiggle||0});
 if(st.pads) s+=`<g transform="rotate(${st.wiggle||0} ${tg0} ${LAND})"><rect x="1066" y="${LAND-130}" width="18" height="30" rx="6" fill="${CORAL}" ${o} stroke-width="3"/><rect x="1066" y="${LAND-50}" width="18" height="30" rx="6" fill="${CORAL}" ${o} stroke-width="3"/></g>`;
 if(st.brackets>0){const a=Math.min(1,st.brackets*2); s+=`<g opacity="${a}"><rect x="1062" y="${LAND-136}" width="54" height="40" rx="8" fill="${BUT}" ${o} stroke-width="4"/><rect x="1062" y="${LAND-56}" width="54" height="40" rx="8" fill="${BUT}" ${o} stroke-width="4"/></g>`;
   s+=screw(1098,LAND-116,seg(st.screws,0,0.5))+screw(1098,LAND-36,seg(st.screws,0.5,1));}
 // the ball
 if(st.ball!=null) s+=`<g transform="translate(${st.ball} ${SY0-30}) rotate(${st.ball*2})"><circle r="30" fill="${BUT}" ${o}/><path d="M-30 0 Q0 -18 30 0 M0 -30 Q-14 0 0 30" stroke="${CORAL}" stroke-width="6" fill="none"/></g>`;
 return s;}
const CAMS=[[590,470,0.92],[985,235,2.0],[575,470,2.15],[590,470,0.92]];
function camAt(i,lt){ // whip from the previous beat's camera in the first .45 s; slow push inside the beat
 const c=CAMS[i], p=i>0?CAMS[i-1]:c, k=i>0?EIO(seg(lt,0,0.45)):1, push=1+0.035*seg(lt,0,SPEC.durs[i]);
 return [p[0]+(c[0]-p[0])*k, p[1]+(c[1]-p[1])*k, (p[2]+(c[2]-p[2])*k)*push];}
function tagL(x,y,txt){const w=40+txt.length*27;return `<g transform="rotate(-3 ${x} ${y})"><rect x="${x-w/2}" y="${y-58}" width="${w}" height="84" rx="24" fill="#FFF8EE" ${o} stroke-width="4"/><text x="${x}" y="${y+2}" font-family="Caveat Brush" font-size="60" text-anchor="middle" fill="#B23A62">${txt}</text></g>`;}
function scr(cam,x,y){return [540+cam[2]*(x-cam[0]), 480+cam[2]*(y-cam[1])];}
function band(){return `<path d="M0 948 Q270 918 540 948 T1080 948 V1920 H0Z" fill="#FFF8E4"/><path d="M0 948 Q270 918 540 948 T1080 948" stroke="${PL}" stroke-width="5" fill="none"/>`
  +`<circle cx="-40" cy="1820" r="230" fill="#FFD6E3" opacity=".75"/><circle cx="1120" cy="1180" r="200" fill="#FFE27E" opacity=".6"/>`;}
function stairsState(i,lt,t){
 const st={t:t,g1:1,g2:1,pads:0,brackets:1,screws:1,net:0,ball:null};
 if(i==0){st.g1=0.45+0.55*EIO(seg(lt,0.1,0.5)); st.g2=0.45+0.55*EIO(seg(lt,0.6,1.0)); st.brackets=1; st.screws=1;
   const r=seg(lt,1.35,2.05), b=seg(lt,2.05,2.7); st.ball=lt<1.35?-120:(lt<2.05?-120+(95+120)*EIO(r):95-35*E(b));}
 if(i==1){st.pads=lt<1.35?1:0; st.brackets=seg(lt,1.35,1.6); st.screws=seg(lt,1.55,2.35);
   st.wiggle=(lt>0.5&&lt<1.35)?-5*Math.sin((lt-0.5)*18)*(1-seg(lt,0.5,1.35)):0;}
 if(i==2){st.net=seg(lt,1.25,2.05);}
 if(i==3){st.net=1; st.ball=60;}
 return st;}
function draw(t){
 T=t; const S=SPEC, starts=S.starts, n=S.durs.length; let i=0; for(let k=0;k<n;k++) if(t>=starts[k]) i=k;
 let lt=t-starts[i]; if(S.cover){i=S.coverBeat; lt=S.coverLt;}
 const cam=camAt(i,lt), st=stairsState(i,lt,t);
 let svg=`<defs><linearGradient id="wallg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${WALL1}"/><stop offset="1" stop-color="${WALL2}"/></linearGradient></defs>`;
 svg+=`<g transform="translate(540 480) scale(${cam[2]}) translate(${-cam[0]} ${-cam[1]})">`+world(st)+`</g>`;
 // screen-space marks (stay crisp whatever the zoom)
 if(i==0){const a=scr(cam,SX0-74,640), b=scr(cam,1012,LAND-215);
   svg+=badge(a[0],a[1],'1',seg(lt,0.45,0.75))+badge(b[0],b[1],'2',seg(lt,0.95,1.25));
   if(lt>2.05&&lt<2.6){const q=scr(cam,64,SY0-40); svg+=sparkle(q[0],q[1],0.9*Math.sin(Math.PI*seg(lt,2.05,2.6)),1);}}
 if(i==1){if(lt>0.55&&lt<1.4) svg+=tagL(540,800,'pressure gate? not up here')+noRing(700,470,150,seg(lt,0.8,1.2));
   if(lt>1.7) svg+=tagL(540,800,'screwed into the wall ✓');
   if(lt>2.35) svg+=check(905,300,seg(lt,2.35,2.8));
   [[1.95,1098,LAND-116],[2.35,1098,LAND-36]].forEach(q=>{if(lt>q[0]&&lt<q[0]+0.4){const p=scr(cam,q[1],q[2]); svg+=sparkle(p[0]+40,p[1]-30,0.9*Math.sin(Math.PI*seg(lt,q[0],q[0]+0.4)),1);}});}
 if(i==2){const xa=SX0+2*SR+26, xb=xa+44, y=railY(xb)+150, a=scr(cam,xa+7,y), b=scr(cam,xb-7,y), k=seg(lt,0.35,0.75);
   if(lt<1.3&&k>0) svg+=`<g opacity="${E(k)*(1-seg(lt,1.1,1.3))}"><path d="M${a[0]} ${a[1]-26} v52 M${b[0]} ${b[1]-26} v52 M${a[0]} ${a[1]} H${b[0]}" stroke="${BER5}" stroke-width="11" stroke-linecap="round"/>`
      +`<g transform="translate(${(a[0]+b[0])/2} ${a[1]-80})"><rect x="-170" y="-42" width="340" height="84" rx="26" fill="${BER5}" ${o} stroke-width="4"/><text y="18" font-family="Poppins" font-weight="700" font-size="48" text-anchor="middle" fill="#FFF8EE">over 6.5 cm?</text></g></g>`;
   if(lt>2.05) svg+=check(880,250,seg(lt,2.05,2.5))+tagL(560,800,'safety netting on ✓');}
 if(i==3){const a=scr(cam,SX0-74,640), b=scr(cam,1012,LAND-215); svg+=badge(a[0],a[1],'1',1)+badge(b[0],b[1],'2',1);
   const ga=scr(cam,SX0-74,790), gb=scr(cam,1010,LAND-80); svg+=check(ga[0],ga[1],seg(lt,0.25,0.7))+check(gb[0],gb[1],seg(lt,0.55,1.0)); if(lt>1.0) svg+=hearts(t,700,560);}
 svg+=band();
 document.getElementById('art').innerHTML=svg;
 for(let k=0;k<n;k++){const el=document.getElementById('b'+k); if(!el) continue; let op=0, y=0;
  if(!S.cover&&k==i){op=1; if(i>0){const p=E(seg(lt,0.05,0.35)); y=40*(1-p); op=p;}}
  el.style.opacity=op; el.style.transform=`translateY(${y}px)`;
  const sb=document.getElementById('s'+k); if(sb){const sa=(k==0)?seg(lt,1.85,2.2):1; sb.style.opacity=(!S.cover&&k==i)?E(sa):0;}}
 for(let k=0;k<n;k++){const c=document.getElementById('c'+k); if(c) c.style.opacity=(!S.cover&&k==i)?1:0;}
 const last=(!S.cover&&i==n-1);
 const f=document.getElementById('follow'); if(f){const p=last?E(seg(lt,FOLLOW_AT,FOLLOW_AT+0.4)):0; f.style.opacity=p; f.style.transform=`translateY(${30*(1-p)}px)`;}
}
"""


def html(spec, cover=None):
    T = ""
    for k, b in enumerate(spec["beats"]):
        inner = ""
        if b.get("kick"):
            inner += f'<div class="hand" style="position:absolute;left:90px;width:900px;top:{b.get("ky", 968)}px;font-size:64px;color:{KICK}">{b["kick"]}</div>'
        inner += K.dual(b["head"], F, cls="S fit", style=f"position:absolute;left:90px;width:900px;top:{b.get('hy', 1040)}px;white-space:nowrap;font-size:{b.get('fs', 118)}px;color:{INK}")
        T += f'<div id="b{k}" style="position:absolute;left:0;top:0;width:{W}px;height:1400px;opacity:0;z-index:4">{inner}</div>'
        if b.get("sub"):
            T += (f'<div id="s{k}" class="lora" style="position:absolute;left:70px;width:940px;top:{b.get("sy", 1290)}px;font-size:{b.get("ss", 48)}px;'
                  f'line-height:1.2;text-align:center;color:{INK};opacity:0;z-index:4">{b["sub"]}</div>')
        T += f'<div id="c{k}" style="position:absolute;left:0;right:0;top:1452px;text-align:center;opacity:0;z-index:4"><span class="chipf" style="font-size:30px">{b["chip"]}</span></div>'
    follow = (f'<div id="follow" style="position:absolute;left:0;right:0;top:{spec.get("follow_y", 1272)}px;text-align:center;opacity:0;z-index:5">'
              f'<span style="display:inline-block;max-width:940px;padding:12px 34px;border-radius:36px;background:{INK};color:#FFF8EE;font:600 42px/1.22 Poppins">{spec["follow"]}</span></div>')
    body = (f'<svg id="art" style="position:absolute;left:0;top:0;z-index:2" width="{W}" height="{H}" viewBox="0 0 {W} {H}"></svg>'
            + T + follow + K.stamp(B, 34, 40, size=104, rot=-10).replace('class="stamp" style="', 'class="stamp" style="z-index:5;')
            + f"<script>const FOLLOW_AT={spec.get('follow_at', 0.6)};\n{RS.JS}</script>")
    return RS.page(W, H, body)


CPS = "Canadian Paediatric Society"
SPEC_STAIRS = dict(
    out="lf-reel-1110-stair-gates-2", music=LIB / "v4/lf-x-sunny-bounce.mp3", scene="stairs", follow=FOLLOW, follow_at=0.6, follow_y=1300,
    garments=["none"] * 4,
    clicks=[0.5, 1.0, 2.05],
    durs=[7 * BB, 6 * BB, 6 * BB, 4.0],
    beats=[
        dict(head="Stairs need 2 gates: / *top and bottom.*", hy=1000, fs=120, sub="Keep them up until at least age 2.", sy=1290, chip="NHS · " + CPS),
        dict(kick="at the top", head="Screw the top gate / *into the wall.*", fs=118, sub="Pressure-mounted gates aren't safe there.", chip=CPS),
        dict(kick="and", head="Banister gaps over 6.5 cm? / *Cover them.*", fs=104, sub="That's 2.5 inches. Use boards or netting.", chip="NHS · Baby and toddler safety"),
        dict(kick="Do this:", head="Fit gates at the / *top and bottom.*", fs=120, chip="NHS · " + CPS),
    ])
SPECS = {"stairs": SPEC_STAIRS}


def cover_stairs_html():
    """Follow the line (style-menu #9, quiet): the hook on cream, then the staircase card; a dashed berry line climbs from the
    floor to stop 1 (bottom gate) and on up the stairs to stop 2 (top gate, screwed in)."""
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4,#FCE5EB)"></div>'
            + S27.BLOBS.format(a="#FFE27E", b="#CFE3F6", c="#FFD3AE") + '<div class="grain" style="opacity:.3"></div>'
            + K.dual("Stairs need 2 gates: / *top and bottom.*", F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:300px;white-space:nowrap;font-size:128px;color:{INK}")
            + '<div style="position:absolute;left:90px;top:610px;width:900px;height:640px;border-radius:40px;overflow:hidden;border:6px solid #6B3B5A;box-shadow:0 16px 0 rgba(107,59,90,.12)">'
              '<svg id="art" width="900" height="640" viewBox="0 0 900 640" style="position:absolute;left:0;top:0"></svg></div>'
            + '<svg id="line" style="position:absolute;left:0;top:0;z-index:3;overflow:visible" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:1284px;font-size:64px;color:{KICK};z-index:4">keep them up until at least age 2 ♡</div>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    # card shows world x 20..1140, y 40..940 (scale .80)
    art = ("const S0=0.80, X0=20, Y0=60;"
           "document.getElementById('art').innerHTML=`<defs><linearGradient id='wallg' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='${WALL1}'/><stop offset='1' stop-color='${WALL2}'/></linearGradient></defs>"
           "<g transform='scale(${S0}) translate(${-X0} ${-Y0})'>`+world({t:0,g1:1,g2:1,brackets:1,screws:1,net:0,ball:null})+`</g>`;"
           "const P=(x,y)=>[90+S0*(x-X0), 610+S0*(y-Y0)];"
           "const a=P(40,SY0-24), b=P(SX0-74,760), m=P(SX0+3*SR,railY(SX0+3*SR)-60), c=P(1012,LAND-182);"
           "let s=`<path d='M${a[0]} ${a[1]} Q${a[0]+30} ${a[1]-90} ${b[0]} ${b[1]+40} L${m[0]} ${m[1]} L${c[0]-20} ${c[1]+40}' stroke='${BER5}' stroke-width='9' stroke-dasharray='4 22' stroke-linecap='round' fill='none'/>`;"
           "s+=`<circle cx='${a[0]}' cy='${a[1]}' r='14' fill='${BER5}'/>`+badge(b[0],b[1]-20,'1',1)+badge(c[0],c[1],'2',1);"
           ""
           "document.getElementById('line').innerHTML=s;")
    return RS.page(W, H, body + f"<script>{RS.JS}\nT=0;{art}</script>")


COVERS = {"stairs": cover_stairs_html}


def use(key):
    RS.JS = S27.BASE_JS + S27.JS_TEETH + JS5
    RS.html = html
    return SPECS[key]

# =====================================================================================================================
# FIX (studio gate Nov 5): lf-reel-1109-room-16-20c, re-rendered IN PLACE (media/studio-nov04/littlefold/, cover unchanged).
# Stranger gate: "Put a thermometer where they sleep" reads as a thermometer in the crib; "Take off a blanket" (and the
# peach blanket lifting off the baby) normalises loose bedding. Beat 2 now shows a sweaty baby in the sleep bag and a
# little blue cardigan (a clothing layer) floating off, no blanket anywhere; beat 4 says "room thermometer in their room".
# Facts re-checked Nov 5 2026: NHS SIDS page "remove 1 or more layers of clothing or bedding if your baby skin is hot or
# sweating", "do not use ... loose blankets"; Lullaby Trust 'Keeping a clear cot' (reviewed 1 Feb 2025): "lightweight
# bedding, firmly tucked in no higher than their shoulders, or a baby sleeping bag"; Lullaby Trust room temperature page:
# "use a room thermometer in the rooms where your baby sleeps".
#     python3 studio/editorial/nov05_littlefold.py room [--still=...]
# =====================================================================================================================
OUT_NOV04 = RS.REPO / "media" / "studio-nov04" / "littlefold"
_ROOM_B2_OLD = "cot(560,1270,t,{blanket:1-off,sweat:1-seg(lt,1.2,1.7)})+`</g>`;"
_ROOM_B2_NEW = ("cot(560,1270,t,{sweat:1-seg(lt,1.2,1.7)})"
                "+`<g transform=\"translate(${545+200*off} ${1215-130*off}) rotate(${-25*off}) scale(${0.62-0.1*off})\" opacity=\"${1-seg(lt,0.95,1.25)}\">`"
                "+G.onesie().replace(/fill=\"#FFB9CF\"/,'fill=\"#9CC4EC\"').replace(/<rect[^>]*>/g,'')+`</g>`+`</g>`;")
LT = N4.LT
SPEC_ROOM_FIX = dict(N4.SPEC_ROOM, beats=[
    dict(N4.SPEC_ROOM["beats"][0]),
    dict(kick="check them", head="Too warm? / *Take a layer off.*", sub="Hot or sweaty? Take off some clothes.", fs=130, sy=730, ss=50, chip=LT + " · NHS"),
    dict(N4.SPEC_ROOM["beats"][2]),
    dict(kick="Do this:", head="Put a room thermometer / *in their room.*", fs=112, chip=LT + " · NHS"),
])
SPECS["room"] = SPEC_ROOM_FIX


def use_room():
    s = N4.use("room")
    assert RS.JS.count(_ROOM_B2_OLD) == 1
    RS.JS = RS.JS.replace(_ROOM_B2_OLD, _ROOM_B2_NEW)
    assert RS.JS.count("label(300,1000,'hot or sweaty?',-4,58)") == 1
    # CD round 3: frame 0 thermometer reads inside the band (18) from the first frame instead of dropping from 26;
    # end-card '18°C' tag moves next to the 18 reading (was over the 30 mark)
    for o_, n_ in [("const v=26-8*EIO(seg(lt,0.15,1.3));", "const v=19.6-1.6*EIO(seg(lt,0.1,0.9));"),   # settles 19.6 -> 18, always inside the band
                   ("if(lt>0.8) s+=tag(400,1015,'18°C',BER4,seg(lt,0.8,1.1));", "if(lt>0.8) s+=tag(445,1236,'18°C',BER4,seg(lt,0.8,1.1));")]:
        assert RS.JS.count(o_) == 1, o_
        RS.JS = RS.JS.replace(o_, n_)
    return SPEC_ROOM_FIX



if __name__ == "__main__":
    for a in sys.argv:
        if a.startswith("--still="):
            RS.STILLS = [float(x) for x in a[8:].split(",")]
        if a.startswith("--sw="):
            RS.SW = int(a[5:])
    for key in [a for a in sys.argv[1:] if not a.startswith("--")]:
        if key == "room":   # in-place fix of the Nov 4 render; cover unchanged
            s = use_room()
            r = RS.frames(s, key)
            if r is None:
                print("stills", RS.SCR / f"{key}-stills.jpg")
                continue
            fdir, total, starts = r
            pops = [(st + 0.1, 0.22) for k, st in enumerate(starts) if k > 0]
            out = OUT_NOV04 / f"{s['out']}.mp4"
            N1.encode(fdir, total, s["music"], pops, out)
            print(out, round(total, 2), flush=True)
            continue
        s = use(key)
        OUT.mkdir(parents=True, exist_ok=True)
        if "--no-cover" not in sys.argv:
            S27.render_cover(COVERS[key](), OUT / f"{s['out']}-cover.jpg")
        if "--cover-only" in sys.argv:
            continue
        r = RS.frames(s, key)
        if r is None:
            print("stills", RS.SCR / f"{key}-stills.jpg")
            continue
        fdir, total, starts = r
        pops = [(st + 0.1, 0.22) for k, st in enumerate(starts) if k > 0]
        pops += [(c, 0.14) for c in s.get("clicks", [])]
        pops += [(starts[1] + 1.95, 0.12), (starts[1] + 2.35, 0.12), (starts[3] + 0.4, 0.12), (starts[3] + 0.75, 0.12)]
        out = OUT / f"{s['out']}.mp4"
        N1.encode(fdir, total, s["music"], pops, out)
        print(out, round(total, 2), flush=True)

#!/usr/bin/env python3
"""Nov 4 (Social studio, Littlefold maker), extending nov03_littlefold.py (imported, not edited)
-> nov02_littlefold.py -> nov01_littlefold.py -> oct27_littlefold.py -> recovery-oct22c/littlefold/reel_story.py.

D  lf-reel-1106-highchair-5-straps  (Fri Nov 6 19:00, SEND TEST, REPLACES the Nov 3 render in place)
   Desk order Nov 4: one on-screen send line in the last ~2 s, shown together with the follow line.
   Identical to nov03 'chair' except a butter-tape Caveat Brush line "Send this to whoever feeds them lunch."
   lands 2.0 s into the 4.0 s end beat (on screen the last 2.0 s; the follow pill is up from 0.6 s).
   Output overwrites media/studio-nov03/littlefold/lf-reel-1106-highchair-5-straps.mp4 (cover not re-rendered).

    python3 studio/editorial/nov04_littlefold.py chair [--still=0.0,1.5,...]
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import nov03_littlefold as N3  # noqa: E402
N2, N1, S27, RS = N3.N2, N3.N1, N3.S27, N3.RS
SCRD = Path("/tmp/claude-0/nov04-littlefold")
SCRD.mkdir(parents=True, exist_ok=True)
RS.SCR = SCRD
K, F, INK, KICK, B = RS.K, RS.F, RS.INK, RS.KICK, RS.B
W, H = RS.W, RS.H
OUT = RS.REPO / "media" / "studio-nov04" / "littlefold"
OUT_NOV03 = RS.REPO / "media" / "studio-nov03" / "littlefold"
LIB = RS.LIB
FOLLOW = N1.FOLLOW

# ---------------------------------------------------------------- send line (reuses nov01's 'part2' tape slot, own timing)
_P2_OLD = "const p=last?E(seg(lt,0.5,0.9)):0; q.style.opacity=p;"
_P2_NEW = "const p=last?E(seg(lt,(typeof SEND_AT=='undefined'?0.5:SEND_AT),(typeof SEND_AT=='undefined'?0.5:SEND_AT)+0.4)):0; q.style.opacity=p;"


def html(spec, cover=None):
    h = N1.html(spec, cover)
    if spec.get("send_at") is not None:
        assert h.count("<script>const FOLLOW_AT=") == 1
        h = h.replace("<script>const FOLLOW_AT=", f"<script>const SEND_AT={spec['send_at']};const FOLLOW_AT=")
        if spec.get("send_fs"):
            assert h.count("font-size:68px;line-height:1.05;color:#B23A62") == 1
            h = h.replace("font-size:68px;line-height:1.05;color:#B23A62", f"font-size:{spec['send_fs']}px;line-height:1.05;color:#B23A62")
    if spec.get("chip_top"):
        _c = 'top:1522px;text-align:center;opacity:0;z-index:4"><span class="chipf" style="font-size:28px">'
        assert h.count(_c) == len(spec["beats"])
        h = h.replace(_c, f'top:{spec["chip_top"]}px;text-align:center;opacity:0;z-index:4"><span class="chipf" style="font-size:{spec["chip_fs"]}px">')
    return h


SEND_CHAIR = "Send this to whoever<br>feeds them lunch."
# Gate Nov 4: end card held 5.2 s (was 4.0), send line 72 px on 2 lines from 2.0 s (on screen 3.2 s), ~30 px clear above the follow box
SPEC_CHAIR_SEND = dict(N3.SPEC_CHAIR, part2=SEND_CHAIR, part2_y=662, send_at=2.0, send_fs=72, follow_y=878,
                       durs=N3.SPEC_CHAIR["durs"][:3] + [5.2])

# ---------------------------------------------------------------- shared: sleeping baby from oct26 (extracted, not edited)
_o26 = (HERE / "oct26_littlefold.py").read_text()
_bi = _o26.index("function babyAsleep(")
BABY_JS = _o26[_bi:_o26.index("\nfunction", _bi + 10)] + "\n"

JS4 = r"""
// ===================== Nov 4: windows 10 cm, room 16-20 C =====================
const BER4='#D9497A', GLASS='#EEF4FB', OUTS='#BFE0F7', LEAF='#A8D59A';
const FIX=s=>`<g transform="translate(540 1180) scale(${1/1.55}) translate(-540 -1279)"><g transform="translate(540 860) scale(.85) translate(-540 -860)">`+s+`</g></g>`; // cancels nov01 draw()'s 1.55 camera; gate Nov 4: art x.85 so the floor + source chip sit at <=75% height
// a sash window: frame (x0..x1, y0..y1); lower sash raised by g px; stop block at stopY (or none); screen in the gap
function windowW(x0,y0,x1,y1,g,opt){opt=opt||{};
 const ix0=x0+30, ix1=x1-30, iy0=y0+30, iy1=y1-30, mid=(iy0+iy1)/2, sh=iy1-mid;
 let s=`<rect x="${x0}" y="${y0}" width="${x1-x0}" height="${y1-y0}" rx="18" fill="#FFFDF7" ${o}/>`;
 s+=`<rect x="${ix0}" y="${iy0}" width="${ix1-ix0}" height="${iy1-iy0}" fill="${OUTS}"/>`;
 s+=`<circle cx="${ix0+90}" cy="${iy1-40}" r="70" fill="${LEAF}" opacity=".9"/><circle cx="${ix0+170}" cy="${iy1-20}" r="56" fill="${LEAF}"/>`;
 s+=`<path d="M${ix1-150} ${iy0+70} q20 -26 46 -10 q22 -22 44 6 q26 2 22 24 h-112 q-18 -8 0 -20z" fill="#FFFFFF" opacity=".95"/>`;
 // upper sash (fixed)
 s+=`<rect x="${ix0}" y="${iy0}" width="${ix1-ix0}" height="${mid-iy0}" fill="${GLASS}" opacity=".9" ${o}/>`;
 s+=`<path d="M${ix0+30} ${iy0+30} l60 60 M${ix0+30} ${iy0+80} l30 30" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity=".8"/>`;
 // screen in the opened gap
 if(opt.screen&&g>0){let m='';const b=opt.bulge||0;
   for(let xx=ix0+20;xx<ix1;xx+=24) m+=`<path d="M${xx} ${iy1-g} Q${xx+(xx-(ix0+ix1)/2)*0.02*b} ${iy1-g/2+30*b} ${xx} ${iy1}" stroke="#8E9BB0" stroke-width="2.5" fill="none" opacity=".7"/>`;
   for(let yy=iy1-g+20;yy<iy1;yy+=24) m+=`<path d="M${ix0} ${yy} Q${(ix0+ix1)/2} ${yy+46*b*Math.sin(Math.PI*(yy-iy1+g)/g)} ${ix1} ${yy}" stroke="#8E9BB0" stroke-width="2.5" fill="none" opacity=".7"/>`;
   s+=`<rect x="${ix0}" y="${iy1-g}" width="${ix1-ix0}" height="${g}" fill="#C9D3E0" opacity=".25"/>`+m;}
 // stop blocks on both jambs
 if(opt.stopY!=null){const ks=opt.stopK==null?1:opt.stopK, sy=opt.stopY-120*(1-E(ks));
   if(ks>0) s+=`<g opacity="${Math.min(1,ks*3)}"><rect x="${ix0-26}" y="${sy-26}" width="46" height="26" rx="8" fill="${BER4}" ${o} stroke-width="4"/><rect x="${ix1-20}" y="${sy-26}" width="46" height="26" rx="8" fill="${BER4}" ${o} stroke-width="4"/></g>`;}
 // lower sash (moves up by g)
 const ly0=mid-g, ly1=iy1-g;
 s+=`<rect x="${ix0-8}" y="${ly0}" width="${ix1-ix0+16}" height="${sh}" rx="8" fill="${GLASS}" fill-opacity=".92" ${o} stroke-width="7"/>`;
 s+=`<rect x="${ix0-8}" y="${ly0}" width="${ix1-ix0+16}" height="26" rx="8" fill="#FFFDF7" ${o} stroke-width="5"/>`;
 s+=`<rect x="${(ix0+ix1)/2-40}" y="${ly1-22}" width="80" height="16" rx="8" fill="${BUT}" ${o} stroke-width="4"/>`;
 s+=`<path d="M${ix0+40} ${ly0+60} l50 50" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity=".8"/>`;
 // sill
 s+=`<rect x="${x0-30}" y="${y1-14}" width="${x1-x0+60}" height="40" rx="14" fill="#FFF8EE" ${o}/>`;
 return s;}
function gapBracket(x,yb,g,k,txt){if(k<=0||g<4)return '';const a=E(k);
 return `<g opacity="${a}"><path d="M${x} ${yb-g} h30 M${x} ${yb} h30 M${x+15} ${yb-g} V${yb}" stroke="${BER4}" stroke-width="7" stroke-linecap="round"/>`
  +`<g transform="translate(${x+50} ${yb-g/2}) scale(${0.6+0.4*a})"><rect x="0" y="-40" width="${40+txt.length*30}" height="80" rx="24" fill="${BER4}" ${o} stroke-width="4"/><text x="${20+txt.length*15}" y="18" font-family="Poppins" font-weight="700" font-size="50" text-anchor="middle" fill="#FFF8EE">${txt}</text></g></g>`;}
function teddy(x,y,lean){ // a teddy bear (not a child) leaning forward by lean px
 return `<g transform="translate(${x+lean} ${y}) rotate(${lean*0.3})"><circle cx="-38" cy="-150" r="22" fill="#E2A97E" ${o}/><circle cx="38" cy="-150" r="22" fill="#E2A97E" ${o}/>
 <ellipse cx="0" cy="-40" rx="70" ry="80" fill="#E2A97E" ${o}/><circle cx="0" cy="-120" r="56" fill="#E2A97E" ${o}/><ellipse cx="0" cy="-104" rx="24" ry="18" fill="#F6D2B4"/>
 <circle cx="-20" cy="-130" r="6" fill="${PL}"/><circle cx="20" cy="-130" r="6" fill="${PL}"/><circle cx="0" cy="-108" r="6" fill="${PL}"/><ellipse cx="0" cy="-30" rx="36" ry="44" fill="#F6D2B4"/></g>`;}
const WX0=180, WY0=930, WX1=770, WY1=1470, WG=86;  // window frame in final px; WG = 10 cm opening
SCN.window=[
 (lt,t)=>{ // frame 0: the lower sash slides up and clicks against the stops at 10 cm; bracket + '10 cm' tag
  const g=WG*EIO(seg(lt,0.15,0.95)), hit=seg(lt,0.95,1.2);
  let s=windowW(WX0,WY0,WX1,WY1,g,{stopY:(WY0+WY1)/2-WG+1});
  if(hit>0&&hit<1) s+=sparkle(WX0+18,(WY0+WY1)/2-WG-12,0.8*Math.sin(Math.PI*hit),1)+sparkle(WX1-18,(WY0+WY1)/2-WG-12,0.8*Math.sin(Math.PI*hit),1);
  s+=gapBracket(WX1+16,WY1-30,g,seg(lt,1.0,1.35),'10 cm');
  if(lt>1.6) s+=label(475,WY0-26,'it stops here ✓',-3,62);
  return FIX(s);},
 (lt,t)=>{ // the catch: wide open with only a screen; a teddy leans on it, the mesh bulges; 'no' ring
  const lean=40*EIO(seg(lt,0.2,1.0));
  let s=windowW(WX0,WY0,WX1,WY1,220,{screen:true,bulge:lean/40});
  s+=teddy(475,WY1+10,lean);
  if(lt>1.0) s+=noRing(475,WY1-140,150,seg(lt,1.0,1.4));
  if(lt>1.5) s+=label(475,WY0-26,'a screen is not a stop',-3,58);
  return FIX(s);},
 (lt,t)=>{ // and: the crib slides away from the window; 'no' ring first, check when clear
  const mv=EIO(seg(lt,0.6,1.5)), cx=500+300*mv;
  let s=`<g transform="translate(300 1180) scale(.72) translate(-475 -1190)">`+windowW(WX0,WY0,WX1,WY1,0,{})+`</g>`;
  s+=`<g transform="translate(${cx} 1250)">`+crib(0,0)+`</g>`;
  if(lt<0.9) s+=noRing(420,1240,110,seg(lt,0.1,0.5));
  if(lt>0.6&&lt<1.6) s+=`<path d="M${cx-250} 1250 h70 l-20 -18 m20 18 l-20 18" stroke="${PL}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="${1-seg(lt,1.4,1.6)}"/>`;
  if(lt>1.5) s+=check(800,1080,seg(lt,1.5,2.0))+label(560,985,'away from the window',-3,72);
  return FIX(s);},
 (lt,t)=>{ // Do this: the stops drop into the track, the sash rises and stops at 10 cm, check, hearts
  const g=WG*EIO(seg(lt,0.9,1.55));
  let s=windowW(WX0,WY0,WX1,WY1,g,{stopY:(WY0+WY1)/2-WG+1,stopK:seg(lt,0.1,0.6)});
  if(lt>0.4&&lt<1.4) s+=label(475,WY0-26,'window stops',-3,60);
  s+=gapBracket(WX1+16,WY1-30,g,seg(lt,1.55,1.9),'10 cm');
  if(lt>1.9) s+=check(890,1130,seg(lt,1.9,2.4));
  if(lt>2.3) s+=hearts(t,900,1060);
  return FIX(s);},
];
"""

JS5 = r"""
// ---------- room 16-20 C
const TCOL='#F27C6B', BAND='#BFD8B0';
function thermoR(x,y,val,k){ // wall thermometer card; scale 10..30 C over 400 px; sage band 16..20; origin bulb centre
 if(k<=0) return ''; const a=E(k), L=400, yv=v=>y-50-(L-40)*(v-10)/20;
 let s=`<g transform="translate(${x} ${y}) scale(${0.7+0.3*a}) translate(${-x} ${-y})" opacity="${Math.min(1,a*1.5)}">`;
 s+=`<rect x="${x-95}" y="${y-L-60}" width="190" height="${L+130}" rx="34" fill="#FFFDF7" ${o}/>`;
 for(let c=10;c<=30;c+=5){s+=`<path d="M${x+26} ${yv(c)} h20" stroke="${PL}" stroke-width="4" stroke-linecap="round"/><text x="${x+52}" y="${yv(c)+11}" font-family="Poppins" font-weight="600" font-size="30" fill="${PL}">${c}</text>`;}
 s+=`<rect x="${x-14}" y="${y-L-20}" width="28" height="${L}" rx="14" fill="#FFFFFF" ${o} stroke-width="4"/>`;
 s+=`<rect x="${x-46}" y="${yv(20)}" width="92" height="${yv(16)-yv(20)}" rx="12" fill="${BAND}" ${o} stroke-width="4" opacity=".9"/>`;
 s+=`<rect x="${x-7}" y="${yv(val)}" width="14" height="${y-yv(val)}" fill="${TCOL}"/><circle cx="${x}" cy="${y}" r="36" fill="${TCOL}" ${o}/>`;
 return s+`</g>`;}
function hat(x,y,k){ // knit hat sitting on a head centred (x,y) r54
 return `<g transform="translate(${x} ${y}) rotate(${-20*k}) translate(${-x} ${-y})"><path d="M${x-58} ${y-8} Q${x-60} ${y-86} ${x} ${y-88} Q${x+60} ${y-86} ${x+58} ${y-8} Z" fill="#9CC4EC" ${o}/>
 <rect x="${x-64}" y="${y-22}" width="128" height="28" rx="12" fill="#FFE08A" ${o} stroke-width="4"/><circle cx="${x}" cy="${y-96}" r="18" fill="#FFB9CF" ${o} stroke-width="4"/></g>`;}
function cot(x,y,t,o2){o2=o2||{}; const sc=o2.sc||1; // the sleeping baby in a crib; origin = crib centre; o2.blanket 0..1 (1 = on), o2.hat 0..1 (1 = on), o2.sweat
 let s=`<g transform="translate(${x} ${y}) scale(${sc})">`;
 s+=`<g transform="translate(20 70) scale(.8)">`+babyAsleep(t);
 if(o2.sweat){for(let i=0;i<3;i++) s+=`<path d="M${-240+i*34} ${-110+12*i} q-10 18 0 26 q10 -8 0 -26z" fill="#9CC4EC" ${o} stroke-width="3" opacity="${o2.sweat}"/>`;}
 if(o2.blanket!=null){const b=o2.blanket; s+=`<g transform="translate(${120*(1-b)} ${-160*(1-b)}) rotate(${-14*(1-b)})" opacity="${Math.min(1,b*2)}"><path d="M-130 -8 Q-134 -96 -30 -104 L150 -98 Q196 -86 186 -8 Z" fill="${PEACH}" ${o}/><path d="M-120 -40 H180 M-120 -70 H170" stroke="#FFFFFF" stroke-width="7" opacity=".7"/></g>`;}
 if(o2.hat!=null){const h=o2.hat; s+=`<g transform="translate(${-90*(1-h)} ${-200*(1-h)})" opacity="${Math.min(1,h*2)}">`+hat(-180,-52,1-h)+`</g>`;}
 s+=`</g>`+crib(0,0)+`</g>`; return s;}
SCN.room=[
 (lt,t)=>{ // frame 0: thermometer drops from 26 into the sage band and settles at 18; '16-20°C' tag; baby asleep in the crib
  const v=26-8*EIO(seg(lt,0.15,1.3));
  let s=thermoR(250,1430,v,1)+cot(700,1250,t,{sc:1.15});
  if(lt>1.25) s+=tag(250,880,'16–20°C',BER4,seg(lt,1.25,1.6));
  if(lt>1.8) s+=label(700,1010,'just right ✓',-4,64);
  return FIX(s);},
 (lt,t)=>{ // hot or sweaty: sweat drops, then the blanket lifts off and the drops fade; check
  const off=EIO(seg(lt,0.6,1.4));
  let s=`<g transform="translate(540 1165) scale(1.65) translate(-560 -1270)">`+cot(560,1270,t,{blanket:1-off,sweat:1-seg(lt,1.2,1.7)})+`</g>`;
  if(lt>0.2&&lt<1.3) s+=label(300,1000,'hot or sweaty?',-4,58);
  if(lt>1.6) s+=check(860,1010,seg(lt,1.6,2.1))+label(560,1010,'one layer off',-4,58);
  return FIX(s);},
 (lt,t)=>{ // indoors: hat on, then it floats away; no ring on the hat first
  const off=EIO(seg(lt,0.7,1.5));
  let s=`<g transform="translate(540 1165) scale(1.65) translate(-560 -1270)">`+cot(560,1270,t,{hat:1-off})+`</g>`;
  if(lt<0.9) s+=noRing(388,1180,95,seg(lt,0.1,0.5));
  if(lt>1.6) s+=check(860,1010,seg(lt,1.6,2.1))+label(560,1010,'hat off',-4,62);
  return FIX(s);},
 (lt,t)=>{ // Do this: the thermometer pops onto the wall beside the crib and reads 18; check, hearts
  let s=thermoR(250,1430,18,seg(lt,0.1,0.6))+cot(700,1250,t,{sc:1.15});
  if(lt>0.8) s+=tag(400,1015,'18°C',BER4,seg(lt,0.8,1.1));
  if(lt>1.6) s+=check(860,1010,seg(lt,1.6,2.1));
  if(lt>2.2) s+=hearts(t,690,1000);
  return FIX(s);},
];
"""

PILLS = N3.PILLS
BP, DROP_BP = N1.BP, N1.DROP_BP   # lf-x-tiny-parade
BG, DROP_BG = N1.BG, N1.DROP_BG   # lf-x-giggle-pop
CPS = "Canadian Paediatric Society"

SPEC_WINDOW = dict(
    out="lf-reel-1108-windows-10cm", music=LIB / "v4/lf-x-tiny-parade.mp3", scene="window", follow=FOLLOW, follow_y=745, chip_top=1398, chip_fs=32,
    follow_at=0.6, garments=["none"] * 4,
    clicks=[1.0], clicks_last=[1.6],
    durs=[6 * BP, 5 * BP, DROP_BP - 11 * BP, 4.4],
    beats=[
        dict(kick="toddler at home?", head="Windows: open 10 cm, / *no more.*", sub=PILLS.format("That's 4 inches."), fs=124, sy=720, ss=50, chip=CPS),
        dict(kick="the catch", head="A screen won't / *stop a fall.*", sub="It can't hold a toddler's weight.", fs=130, sy=730, ss=50, chip=CPS),
        dict(kick="and", head="Keep the crib / *away from windows.*", sub="Other furniture, too.", fs=124, sy=730, ss=50, chip=CPS),
        dict(kick="Do this:", head="Fit window stops / *at 10 cm.*", fs=130, chip=CPS + " · caringforkids.cps.ca"),
    ])

LT = "Lullaby Trust"
SPEC_ROOM = dict(
    out="lf-reel-1109-room-16-20c", music=LIB / "v4/lf-x-giggle-pop.mp3", scene="room", follow=FOLLOW, follow_y=770, chip_top=1398, chip_fs=32,
    follow_at=0.6, garments=["none"] * 4,
    durs=[8 * BG, 6 * BG, 6 * BG, 4.2],
    beats=[
        dict(kick="heating on?", head="Baby's room: / *16 to 20°C.*", sub=PILLS.format("About 61 to 68°F."), fs=136, sy=720, ss=50, chip=LT + " · NHS"),
        dict(kick="check them", head="Hot or sweaty? / *Take a layer off.*", sub="Take off a blanket or some clothes.", fs=124, sy=730, ss=50, chip=LT + " · NHS"),
        dict(kick="and", head="Indoors, babies / *don't need a hat.*", sub="Take it off when you get home.", fs=124, sy=730, ss=50, chip=LT + " · NHS"),
        dict(kick="Do this:", head="Put a thermometer / *where they sleep.*", fs=124, chip=LT + " · NHS"),
    ])

SPECS = {"chair": SPEC_CHAIR_SEND, "window": SPEC_WINDOW, "room": SPEC_ROOM}
OUTS = {"chair": OUT_NOV03}
NOCOVER = {"chair"}
BLOBS = S27.BLOBS


def _cover(body_html, art_js):
    return RS.page(W, H, body_html + f"<script>{RS.JS}\nT=0;{art_js}</script>")


def cover_window_html():
    """Sticky-note list (style #13, quiet): 'window rules' note card under the hook, the 10 cm window bottom right."""
    items = ["opens 10 cm, no more", "a screen is not a stop", "crib away from windows", "fit stops or guards"]
    lis = "".join(f'<div style="height:96px;line-height:96px"><span style="color:#D9497A;margin-right:18px">✓</span>{x}</div>' for x in items)
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4,#FFE3EC)"></div>'
            + BLOBS.format(a="#CFE3F6", b="#FFE27E", c="#FFD3AE") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:300px;font-size:76px;color:{KICK}">toddler at home?</div>'
            + K.dual("Windows: open 10 cm, / *no more.*", F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:390px;white-space:nowrap;font-size:124px;color:{INK}")
            + '<div style="position:absolute;left:90px;top:730px;width:880px;height:560px;background:#FFFDF6;transform:rotate(-2deg);border-radius:6px;'
              'box-shadow:0 24px 40px rgba(107,59,90,.18);background-image:linear-gradient(#FFFDF6 140px,transparent 140px),repeating-linear-gradient(#FFFDF6 0 94px,rgba(80,110,180,.28) 94px 96px)">'
              '<div style="position:absolute;left:96px;top:0;bottom:0;width:3px;background:rgba(220,80,80,.45)"></div>'
              '<div style="position:absolute;left:130px;top:40px;font-family:\'Caveat Brush\';font-size:88px;color:#D9497A;line-height:1">window rules:</div>'
              f'<div style="position:absolute;left:130px;top:140px;font-family:Caveat;font-weight:700;font-size:68px;color:#3A1F3D">{lis}</div></div>'
            + '<div style="position:absolute;left:400px;top:700px;width:240px;height:64px;background:rgba(255,255,255,.6);transform:rotate(3deg);box-shadow:0 2px 6px rgba(0,0,0,.08)"></div>'
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:3" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    art = ("document.getElementById('art').innerHTML=`<g transform='translate(700 1490) scale(.58) translate(-475 -1190)'>`"
           "+windowW(WX0,WY0,WX1,WY1,WG,{stopY:(WY0+WY1)/2-WG+1})+gapBracket(WX1+16,WY1-30,WG,1,'10 cm')+`</g>`;")
    return _cover(body, art)


def cover_room_html():
    """Original simple template 'compare' (style #8, quiet): two cream panels, 'too warm' (24, hat, blanket) vs 'just right' (18)."""
    panel = ('<div style="position:absolute;left:{x}px;top:760px;width:440px;height:640px;border-radius:30px;background:{bg};border:5px solid #6B3B5A"></div>'
             '<div style="position:absolute;left:{x}px;width:440px;top:1300px;text-align:center;font:700 54px Poppins;color:#3A1F3D">{txt}</div>')
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4,#FFE9D6)"></div>'
            + BLOBS.format(a="#CFE3F6", b="#FFD6E3", c="#FFE27E") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:300px;font-size:76px;color:{KICK}">heating on?</div>'
            + K.dual("Baby's room: / *16 to 20°C.*", F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:390px;white-space:nowrap;font-size:140px;color:{INK}")
            + panel.format(x=80, bg="#FFFDF7", txt="too warm") + panel.format(x=560, bg="#FCE5EB", txt="just right")
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:3" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    art = ("let s=`<g transform='translate(300 1250) scale(.8) translate(-300 -1250)'>`+thermoR(300,1250,25,1)+`</g>`+noRing(420,860,46,1);"
           "s+=`<g transform='translate(780 1250) scale(.8) translate(-780 -1250)'>`+thermoR(780,1250,18,1)+`</g>`+check(900,860,1);"
           "document.getElementById('art').innerHTML=s;")
    return _cover(body, art)


COVERS = {"window": cover_window_html, "room": cover_room_html}


def use(key):
    if key == "chair":
        N3.use("chair")
        # gate Nov 4: 'room to spare' -> a line said out loud; end-card toddler 30 px lower so the taller send + follow stack clears
        for a, b in [("label(440,1200,'room to spare',-4,50)", "label(385,1062,'away from the counter',-4,42)"),
                     ("return `<g transform=\"translate(540 1340) scale(.95) translate(-540 -1290)\">`", "return `<g transform=\"translate(540 1334) scale(.85) translate(-540 -1290)\">`")]:
            assert RS.JS.count(a) == 1, a
            RS.JS = RS.JS.replace(a, b)
    else:
        RS.JS = S27.BASE_JS + S27.JS_TEETH + N1.JS + N2.JS + N3.ROSETTE_JS + N3.JS + BABY_JS + JS4 + JS5
        _g = "skyBG(t).replace(/1320/g,'1440').replace(/1340/g,'1460')"
        assert RS.JS.count(_g) == 1
        RS.JS = RS.JS.replace(_g, "skyBG(t).replace(/1320/g,'1385').replace(/1340/g,'1405')")   # gate Nov 4: floor up with the x.85 art
    assert RS.JS.count(_P2_OLD) == 1
    RS.JS = RS.JS.replace(_P2_OLD, _P2_NEW)
    RS.html = html
    return SPECS[key]


if __name__ == "__main__":
    for a in sys.argv:
        if a.startswith("--still="):
            RS.STILLS = [float(x) for x in a[8:].split(",")]
        if a.startswith("--sw="):
            RS.SW = int(a[5:])
    for key in [a for a in sys.argv[1:] if not a.startswith("--")]:
        s = use(key)
        od = OUTS.get(key, OUT)
        od.mkdir(parents=True, exist_ok=True)
        if key not in NOCOVER and "--no-cover" not in sys.argv:
            S27.render_cover(COVERS[key](), od / f"{s['out']}-cover.jpg")
        if "--cover-only" in sys.argv:
            continue
        r = RS.frames(s, key)
        if r is None:
            print("stills", RS.SCR / f"{key}-stills.jpg")
            continue
        fdir, total, starts = r
        pops = [(st + 0.1, 0.22) for k, st in enumerate(starts) if k > 0]
        pops += [(c, 0.14) for c in s.get("clicks", [])]
        if key == "chair":
            pops += [(starts[-1] + 0.05 + 0.2 * i + 0.22, 0.12) for i in range(5)]
        pops += [(starts[-1] + c, 0.14) for c in s.get("clicks_last", [])]
        out = od / f"{s['out']}.mp4"
        N1.encode(fdir, total, s["music"], pops, out)
        print(out, round(total, 2), flush=True)

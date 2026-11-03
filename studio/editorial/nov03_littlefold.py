#!/usr/bin/env python3
"""Nov 3 (Social studio, Littlefold maker), extending nov02_littlefold.py (imported, not edited) which extends
nov01_littlefold.py -> oct27_littlefold.py -> recovery-oct22c/littlefold/reel_story.py.

D  lf-reel-1105-battery-honey  (Thu Nov 5 19:00, REPLACES the Nov 2 render in place)
   Desk order Nov 3: no sequel label on screen. Identical to nov02 'honey' except the pill reads "COIN BATTERIES"
   (was "PART 2 · COIN BATTERIES") on every frame and on the cover. Output overwrites media/studio-nov02/littlefold/.

    python3 studio/editorial/nov03_littlefold.py honey [--still=0.0,1.5,...] [--cover-only] [--no-cover]
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import nov02_littlefold as N2  # noqa: E402
N1, S27, RS = N2.N1, N2.S27, N2.RS
SCRD = Path("/tmp/claude-0/nov03-littlefold")
SCRD.mkdir(parents=True, exist_ok=True)
RS.SCR = SCRD
K, F, INK, KICK, B = RS.K, RS.F, RS.INK, RS.KICK, RS.B
W, H = RS.W, RS.H
OUT = RS.REPO / "media" / "studio-nov03" / "littlefold"
OUT_NOV02 = RS.REPO / "media" / "studio-nov02" / "littlefold"
LIB = RS.LIB
FOLLOW = N1.FOLLOW

# ---------------------------------------------------------------- D: honey, sequel label removed
SPEC_HONEY = dict(N2.SPEC_HONEY, tag="COIN BATTERIES")


def cover_honey_html():
    h = N2.cover_honey_html()
    assert h.count("PART 2 · COIN BATTERIES") == 1
    return h.replace("PART 2 · COIN BATTERIES", "COIN BATTERIES")


# ---------------------------------------------------------------- A: high chair, all 5 straps (Fri Nov 6 19:00)
_src = (HERE / "nov01_littlefold.py").read_text()
_hc = _src[_src.index("function highChair("):_src.index("function sausage(")]
assert _hc.count('<g transform="translate(0 ${bob})">') == 1
CHAIRKID = (_hc.replace("function highChair(x,y,t,eat,tray)", "function chairKid(x,y,t,eat,tray,mid)")
            .replace('<g transform="translate(0 ${bob})">', "${mid||''}<g transform=\"translate(0 ${bob})\">"))

JS = CHAIRKID + r"""
// ===================== Nov 3: high-chair straps, hot tap water =====================
const BER='#D9497A';
const SA=(x,y)=>[[x-46,y-82],[x+46,y-82],[x-86,y-8],[x+86,y-8],[x,y+22]];       // strap anchors: 2 shoulders, 2 hips, between the legs
const SB=(x,y)=>[x,y-34];                                                          // buckle
const SN=(x,y)=>[[x-132,y-136],[x+132,y-136],[x-176,y-20],[x+176,y-20],[x,y+118]]; // number bubbles, outside the body
function strapSet(x,y,ks,glow,t){
 const A=SA(x,y), B=SB(x,y); let s='';
 A.forEach((a,i)=>{const k=E(ks[i]); if(k<=0) return; const ex=B[0]+(a[0]-B[0])*(1-k)*0, ey=0;
   const px=a[0]+(B[0]-a[0])*k, py=a[1]+(B[1]-a[1])*k;
   if(glow&&i==4) s+=`<path d="M${a[0]} ${a[1]+30} L${px} ${py}" stroke="${BUT}" stroke-width="${46+6*Math.sin(t*8)}" stroke-linecap="round" opacity=".9"/>`;
   const st=i==4?`M${a[0]} ${a[1]+30} L${px} ${py}`:`M${a[0]} ${a[1]} L${px} ${py}`;
   s+=`<path d="${st}" stroke="${PL}" stroke-width="28" stroke-linecap="round"/><path d="${st}" stroke="${BER}" stroke-width="18" stroke-linecap="round"/>`;});
 const all=ks.every(v=>v>=1);
 s+=`<rect x="${B[0]-34}" y="${B[1]-24}" width="68" height="48" rx="14" fill="${all?BUT:CREAM}" ${o} stroke-width="5"/><rect x="${B[0]-14}" y="${B[1]-8}" width="28" height="16" rx="5" fill="${PL}" opacity=".55"/>`;
 return s;}
function strapNums(x,y,ks,big){const N=SN(x,y);let s='';N.forEach((p,i)=>{const k=seg(ks[i],0.85,1);if(k>0) s+=numBub(p[0],p[1],i+1,k*(big&&i==4?1.35:1));});return s;}
function kidStrapped(x,y,t,ks,opt){opt=opt||{};
 const mid=strapSet(x,y,ks,opt.glow,t);
 return chairKid(x,y,t,opt.eat||0,opt.tray||'',mid)+strapNums(x,y,ks,opt.glow);}
function counter(x,y){ // a kitchen counter seen from the front; top edge at y, right edge at x
 return `<rect x="-40" y="${y}" width="${x+40}" height="420" rx="10" fill="#F3CFA0" ${o}/><rect x="-40" y="${y-26}" width="${x+60}" height="40" rx="14" fill="#FFF8EE" ${o}/>
 <rect x="40" y="${y+60}" width="${x-100}" height="150" rx="16" fill="#F7DDB8" ${o} stroke-width="4"/><circle cx="${x-90}" cy="${y+135}" r="10" fill="${PL}"/>`;}
function bowl(x,y,k){if(k<=0)return '';const s=E(k);let p='';for(let i=0;i<5;i++) p+=`<circle cx="${x-30+i*15}" cy="${y-18-6*(i%2)}" r="10" fill="${SAGE}" stroke="${PL}" stroke-width="3"/>`;
 return `<g transform="translate(${x} ${y}) scale(${s}) translate(${-x} ${-y})">${p}<path d="M${x-56} ${y-14} Q${x} ${y+50} ${x+56} ${y-14}Z" fill="${PINK}" ${o} stroke-width="4"/></g>`;}
const KS=(lt,a,step,len)=>[0,1,2,3,4].map(i=>seg(lt,a+step*i,a+step*i+len));
SCN.chair=[
 (lt,t)=>{ // frame 0: toddler in a high chair; straps 1..5 click in one by one (all 5 by ~1.9 s)
  const ks=KS(lt,0.1,0.36,0.3);
  let s=kidStrapped(540,1250,t,ks);
  if(lt>2.0) s+=label(300,1395,'all 5 ✓',-4,64);
  return `<g transform="translate(540 1290) scale(1.05) translate(-540 -1290)">`+s+`</g>`;},
 (lt,t)=>{ // the strap between the legs glows; number 5 grows; check
  let s=kidStrapped(540,1250,t,[1,1,1,1,1],{glow:true});
  if(lt>0.5) s+=label(560,1462,'this one too',-4,60);
  if(lt>1.2) s+=check(330,1380,seg(lt,1.2,1.7));
  return `<g transform="translate(540 1290) scale(1.05) translate(-540 -1290)">`+s+`</g>`;},
 (lt,t)=>{ // chair slides away from the counter: 'no' at the start, check when clear
  const mv=EIO(seg(lt,0.6,1.5)), cx=450+240*mv;
  let s=counter(300,1150)+`<g transform="translate(${cx} 1290) scale(.85) translate(${-cx} -1290)">`+kidStrapped(cx,1250,t,[1,1,1,1,1])+`</g>`;
  if(lt<0.9) s+=noRing(300,1180,80,seg(lt,0.1,0.5));
  if(lt>0.6&&lt<1.6) s+=`<path d="M${cx-260} 1230 h60 l-18 -16 m18 16 l-18 16" stroke="${PL}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="${1-seg(lt,1.4,1.6)}"/>`;
  if(lt>1.5) s+=check(430,1300,seg(lt,1.5,2.0))+label(440,1200,'room to spare',-4,50);
  return s;},
 (lt,t)=>{ // Do this: 1..5 click fast, then the bowl lands on the tray, toddler eats, hearts
  const ks=KS(lt,0.05,0.2,0.22);
  const eat=lt>1.9?0.5-0.5*Math.cos(Math.PI*2*seg(lt,1.9,3.4)):0;
  let s=kidStrapped(540,1250,t,ks,{eat:eat,tray:bowl(600,1262,seg(lt,1.3,1.7))});
  if(lt>2.2) s+=hearts(t,860,1150);
  return `<g transform="translate(540 1340) scale(.95) translate(-540 -1290)">`+s+`</g>`;},
];
// ---------- hot tap water
const HOT='#F27C6B', COLD='#7FB3E8', WARM='#F7B49A';
function faucet(x,y,hot){ // wall tap; spout mouth at (x,y); hot 0..1 tints the handle
 return `<rect x="${x-300}" y="${y-150}" width="80" height="140" rx="18" fill="#E6EBF2" ${o}/>
 <path d="M${x-230} ${y-90} H${x-50} Q${x} ${y-90} ${x} ${y-40} V${y}" stroke="${PL}" stroke-width="64" fill="none" stroke-linecap="round"/>
 <path d="M${x-230} ${y-90} H${x-50} Q${x} ${y-90} ${x} ${y-40} V${y}" stroke="#E6EBF2" stroke-width="50" fill="none" stroke-linecap="round"/>
 <path d="M${x-210} ${y-104} H${x-60}" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity=".8"/>
 <rect x="${x-180}" y="${y-170}" width="96" height="44" rx="16" fill="${HOT}" ${o} stroke-width="4"/>`;}
function stream(x,y,len,col,t,k){if(k<=0)return '';const L=len*E(k);
 return `<path d="M${x-15} ${y} Q${x-18+3*Math.sin(t*20)} ${y+L/2} ${x-13} ${y+L} L${x+13} ${y+L} Q${x+18+3*Math.sin(t*17)} ${y+L/2} ${x+15} ${y}Z" fill="${col}" opacity=".9"/>
 <path d="M${x-4} ${y+10} V${y+L-10}" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity=".6"/>`;}
function steam(x,y,t,k){if(k<=0)return '';let s='';for(let i=0;i<3;i++){const p=(t*0.7+i*0.33)%1;
 s+=`<path d="M${x+(i-1)*60} ${y-140*p} q-18 -30 0 -60 q18 -30 0 -60" stroke="#FFFFFF" stroke-width="10" fill="none" stroke-linecap="round" opacity="${k*0.85*Math.sin(Math.PI*p)}"/>`;}return s;}
function basin(x,y,lvl,col){ // a sink basin seen from the front; lvl 0..1 water
 return `<path d="M${x-260} ${y} H${x+260} Q${x+250} ${y+170} ${x} ${y+180} Q${x-250} ${y+170} ${x-260} ${y}Z" fill="#FFFFFF" ${o}/>
 ${lvl>0?`<path d="M${x-250+30*(1-lvl)} ${y+150-120*lvl} H${x+250-30*(1-lvl)} Q${x+200} ${y+165} ${x} ${y+170} Q${x-200} ${y+165} ${x-250+30*(1-lvl)} ${y+150-120*lvl}Z" fill="${col}" opacity=".75"/>`:''}
 <rect x="${x-290}" y="${y-22}" width="580" height="34" rx="16" fill="#FFFFFF" ${o}/>`;}
function thermo(x,y,val,rot){ // bulb at (x,y), tube up 330 px, scale 0..60 C
 const L=330, top=y-40-(L-40)*val/60; let tk='';
 for(let c=0;c<=60;c+=10) tk+=`<path d="M${x+22} ${y-40-(L-40)*c/60} h${c%30?12:24}" stroke="${PL}" stroke-width="3"/>`;
 return `<g transform="rotate(${rot||0} ${x} ${y})"><rect x="${x-22}" y="${y-L-20}" width="44" height="${L+10}" rx="22" fill="#FFFFFF" ${o}/>${tk}
 <rect x="${x-9}" y="${top}" width="18" height="${y-top}" fill="${HOT}"/><circle cx="${x}" cy="${y}" r="34" fill="${HOT}" ${o}/></g>`;}
function tag(x,y,txt,col,k){if(k<=0)return '';const s=E(k);const w=40+txt.length*30;
 return `<g transform="translate(${x} ${y}) scale(${s}) rotate(-4)"><rect x="${-w/2}" y="-42" width="${w}" height="84" rx="24" fill="${col||BER}" ${o} stroke-width="4"/><text y="20" font-family="Poppins" font-weight="700" font-size="52" text-anchor="middle" fill="#FFF8EE">${txt}</text></g>`;}
function heater(x,y){return `<g transform="translate(${x} ${y})"><rect x="-80" y="-200" width="160" height="330" rx="70" fill="#E6EBF2" ${o}/><rect x="-46" y="-60" width="92" height="52" rx="12" fill="${CREAM}" ${o} stroke-width="4"/>
 <path d="M-20 70 q10 -24 20 0 q10 24 20 0" stroke="${HOT}" stroke-width="7" fill="none" stroke-linecap="round"/></g>`;}
function flowDots(pts,col,t,k){if(k<=0)return '';let s='';const n=pts.length-1;for(let j=0;j<6;j++){const u=((t*0.5+j/6)%1);const f=u*n, i=Math.min(Math.floor(f),n-1), r=f-i;
 const px=pts[i][0]+(pts[i+1][0]-pts[i][0])*r, py=pts[i][1]+(pts[i+1][1]-pts[i][1])*r; s+=`<circle cx="${px}" cy="${py}" r="11" fill="${col}" stroke="${PL}" stroke-width="3" opacity="${k}"/>`;}return s;}
function pipe(pts,col){const d='M'+pts.map(p=>p.join(' ')).join(' L');return `<path d="${d}" stroke="${PL}" stroke-width="40" fill="none" stroke-linejoin="round" stroke-linecap="round"/><path d="${d}" stroke="${col}" stroke-width="28" fill="none" stroke-linejoin="round" stroke-linecap="round"/>`;}
const UNCAM=s=>`<g transform="translate(540 1240) scale(.645) translate(-540 -1240)">`+s+`</g>`; // cancels nov01 draw()'s 1.55 camera
SCN.tap=[
 (lt,t)=>{ // frame 0: time until skin burns: your bar vs a child's bar, a quarter as long, both fill at the same speed
  const sp=EIO(seg(lt,0.05,2.1)), ax=230, L=600;   // child's bar full at ~0.8 s
  let s=`<rect x="150" y="930" width="780" height="420" rx="40" fill="${CREAM}" ${o}/>`;
  s+=`<text x="540" y="1000" font-family="Caveat Brush" font-size="54" text-anchor="middle" fill="#B23A62">time until hot water burns</text>`;
  const bar=(y,len,lab,k)=>`<text x="${ax}" y="${y-22}" font-family="Poppins" font-weight="700" font-size="40" fill="${INK}">${lab}</text><rect x="${ax}" y="${y}" width="${len}" height="64" rx="20" fill="#FFFFFF" ${o} stroke-width="4"/><rect x="${ax+4}" y="${y+4}" width="${Math.max(0,(len-8)*k)}" height="56" rx="16" fill="${HOT}"/>`;
  s+=bar(1090,L,'your skin',sp)+bar(1240,L/4,"a child's skin",Math.min(1,sp*4));
  if(sp*4>=1) s+=label(ax+L/4+150,1290,'4× faster',-4,62)+sparkle(ax+L/4+8,1240,0.9,1);
  return UNCAM(s);},
 (lt,t)=>{ // payoff (from ~2.3 s): hot tap running, steam; a thermometer in the stream rises to 49 and stops; tag 49°C
  const v=49*EIO(seg(lt,0.1,1.3));
  let s=basin(540,1300,0.35,WARM)+stream(540,1040,265,WARM,t,1)+faucet(540,1040,1)+steam(470,1220,t,1);
  s+=thermo(700,1250,v,18);
  if(lt>1.25) s+=tag(830,960,'49°C',BER,seg(lt,1.25,1.6));
  return `<g transform="translate(0 -26) translate(540 1400) scale(.8) translate(-540 -1400)">`+s+`</g>`;},
 (lt,t)=>{ // the fix: heater 60 -> anti-scald valve (cold joins) -> tap 49
  const k=seg(lt,0.15,0.6);
  const P1=[[320,1150],[540,1150]], P2=[[540,1150],[800,1150],[800,1060]], PC=[[540,1430],[540,1180]];
  let s=pipe(P1,'#F9C6B8')+pipe(PC,'#CFE3F6')+pipe(P2,'#FBD8C8')+heater(230,1230);
  s+=`<circle cx="540" cy="1150" r="62" fill="${BUT}" ${o}/><path d="M512 1150 a28 28 0 1 1 28 28" stroke="${PL}" stroke-width="7" fill="none" stroke-linecap="round"/>`;
  s+=flowDots(P1,HOT,t,k)+flowDots(PC,COLD,t,k)+flowDots(P2,WARM,t,seg(lt,0.4,0.8));
  s+=`<g transform="translate(870 1010) scale(.6) translate(-540 -1040)">`+faucet(540,1040,1)+`</g>`;
  s+=tag(230,975,'60°C',HOT,seg(lt,0.5,0.9))+tag(860,1260,'49°C',BER,seg(lt,1.1,1.5))+label(540,1060,'anti-scald valve',-3,52)+label(410,1290,'heater',-3,62)+label(860,1350,'tap',-3,62);
  return UNCAM(s);},
 (lt,t)=>{ // Do this: cold runs first, then hot joins; water level rises; check, hearts
  const c=seg(lt,0.1,0.5), h=seg(lt,0.9,1.3), col=lt<1.0?COLD:'#B9C9F0';
  let s=basin(540,1300,0.15+0.45*seg(lt,0.2,2.2),col)+stream(540,1040,265,col,t,c)+faucet(540,1040,0);
  if(lt>0.4) s+=label(300,1240,'cold first',-5,56);
  if(lt>1.2) s+=label(790,1240,'then hot',-5,56);
  if(lt>1.9) s+=check(800,1120,seg(lt,1.9,2.4));
  if(lt>2.5) s+=hearts(t,300,1150);
  return `<g transform="translate(0 -26) translate(540 1480) scale(.7) translate(-540 -1480)">`+s+`</g>`;},
];
['chair','tap'].forEach(k=>{SCN[k]=SCN[k].map(f=>(lt,t)=>`<g transform="translate(540 1120) scale(1.0) translate(-540 -1180)">`+f(lt,t)+`</g>`);});
"""

BB, DROP_BB = N2.BB, N2.DROP_BB   # lf-x-sunny-bounce
BG, DROP_BG = N2.BG, N2.DROP_BG   # lf-x-giggle-pop
PILLS = ('<span style="display:inline-block;padding:10px 32px 12px;border-radius:40px;background:#D9497A;color:#FFF8EE;'
         'font:600 42px/1.2 Poppins;font-style:normal;white-space:nowrap">{}</span>')

SPEC_CHAIR = dict(
    out="lf-reel-1106-highchair-5-straps", music=LIB / "v4/lf-x-sunny-bounce.mp3", scene="chair", follow=FOLLOW, follow_y=830,
    follow_at=0.6, garments=["none"] * 4, odir="nov03",
    clicks=[0.1 + 0.36 * i + 0.3 for i in range(5)],
    durs=[6 * BB, 5 * BB, DROP_BB - 11 * BB, 4.0],
    beats=[
        dict(kick="high chair?", head="Buckle all 5 straps, / *every time.*", sub=PILLS.format("2 shoulders, 2 hips, 1 between legs"), fs=124, sy=720, ss=50, chip="NHS · AAP HealthyChildren.org"),
        dict(kick="don't skip", head="The strap between / *the legs, too.*", sub="Even for a quick snack.", fs=124, sy=730, ss=50, chip="AAP HealthyChildren.org"),
        dict(kick="and", head="Not right next to / *a table or counter.*", sub="A push with their feet can tip it over.", fs=118, sy=730, ss=50, chip="AAP HealthyChildren.org"),
        dict(kick="Do this:", head="Next meal: buckle / *all 5 first.*", fs=124, chip="NHS · Baby and toddler safety"),
    ])

SPEC_TAP = dict(
    out="lf-reel-1107-tap-49c", music=LIB / "v4/lf-x-giggle-pop.mp3", scene="tap", follow=FOLLOW, follow_y=720,
    follow_at=0.6, garments=["none"] * 4, odir="nov03",
    durs=[2.3, 3.7, 6 * BG, 3.8],
    beats=[
        dict(kick="hot tap water?", head="Kids' skin burns / *4 times faster.*", sub="It burns in a quarter of the time.", fs=124, sy=730, ss=50, chip="Public Health Agency of Canada"),
        dict(kick="so", head="Keep hot tap water / *at 49°C or less.*", sub=PILLS.format("That's 120°F."), fs=124, sy=720, ss=50, chip="Public Health Agency of Canada"),
        dict(kick="the fix", head="An anti-scald valve / *keeps taps at 49°C.*", sub="The heater itself stays at 60°C.", fs=112, sy=730, ss=50, chip="Public Health Agency of Canada"),
        dict(kick="Do this:", head="Bath tonight? / *Cold first, then hot.*", fs=124, chip="Public Health Agency of Canada · NHS"),
    ])

SPECS = {"honey": SPEC_HONEY, "chair": SPEC_CHAIR, "tap": SPEC_TAP}
OUTS = {"honey": OUT_NOV02}
BLOBS = S27.BLOBS


def _cover(body_html, art_js):
    return RS.page(W, H, body_html + f"<script>{RS.JS}\nT=0;{art_js}</script>")


def cover_chair_html():
    """Awards (style #10, quiet): five numbered rosettes ('shoulder, shoulder, hip, hip, legs') over the strapped toddler."""
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF8E4,#FFE3EC)"></div>'
            + BLOBS.format(a="#FFE27E", b="#CFE3F6", c="#FFD3AE") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:290px;font-size:76px;color:{KICK}">high chair?</div>'
            + K.dual("Buckle all 5 straps, / *every time.*", F, cls="S fit", style=f"position:absolute;left:80px;width:920px;top:380px;white-space:nowrap;font-size:128px;color:{INK}")
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:3" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + f'<div class="hand" style="position:absolute;left:60px;width:960px;top:1730px;text-align:center;font-size:62px;color:{KICK};z-index:4">click, click, click, click, click ♡</div>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    art = ("let s=`<g transform='translate(540 1300) scale(1.25) translate(-540 -1290)'>`+kidStrapped(540,1250,0,[1,1,1,1,1])+`</g>`;"
           "const R=[[160,790,PINK,'shoulder'],[920,790,BUT,'shoulder'],[130,1140,BLUE,'hip'],[950,1140,SAGE,'hip'],[880,1470,PEACH,'legs']];"
           "R.forEach((r,i)=>{s+=`<g transform='translate(${r[0]} ${r[1]}) scale(1.18) translate(${-r[0]} ${-r[1]})'>`+rosette(r[0],r[1],r[2],r[3],1,0).replace('font-size=\"44\"',r[3].length>5?'font-size=\"31\"':'font-size=\"44\"')+`</g>`+numBub(r[0]+62,r[1]-70,i+1,1);});"
           "document.getElementById('art').innerHTML=s;")
    return _cover(body, art)


def cover_tap_html():
    """Kinetic big text (style #5, loud): a giant '49°C' on a peach field, the tap + thermometer under it."""
    body = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFE9C9,#FFD3AE)"></div>'
            + BLOBS.format(a="#FFD6E3", b="#FFF8E4", c="#CFE3F6") + '<div class="grain" style="opacity:.3"></div>'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:290px;font-size:76px;color:{KICK}">hot tap water?</div>'
            + f'<div class="lora" style="position:absolute;left:0;width:1080px;top:380px;text-align:center;font-weight:700;font-size:110px;line-height:1;color:{INK}">Keep it at</div>'
            + '<div class="lora" style="position:absolute;left:0;width:1080px;top:490px;text-align:center;font-weight:700;font-size:330px;line-height:1;color:#D9497A;text-shadow:10px 10px 0 #FFFFFF">49°C</div>'
            + f'<div class="lora" style="position:absolute;left:0;width:1080px;top:830px;text-align:center;font-weight:700;font-size:90px;line-height:1;color:{INK}">or less <span style="font-style:italic;color:#D9497A">(120°F)</span></div>'
            + '<svg id="art" style="position:absolute;left:0;top:0;z-index:3" width="1080" height="1920" viewBox="0 0 1080 1920"></svg>'
            + f'<div class="hand" style="position:absolute;left:190px;width:850px;top:1520px;text-align:center;font-size:62px;color:{KICK};z-index:4">a child\'s skin burns 4× faster ♡</div>'
            + K.stamp(B, 46, 1470, size=120, rot=-10))
    art = ("document.getElementById('art').innerHTML=`<g transform='translate(540 1250) scale(.82) translate(-540 -1250)'>`"
           "+basin(540,1300,0.35,WARM)+stream(540,1040,265,WARM,0.4,1)+faucet(540,1040,1)+steam(470,1220,1.2,1)+thermo(700,1250,49,18)+`</g>`;")
    return _cover(body, art)


COVERS = {"honey": cover_honey_html, "chair": cover_chair_html, "tap": cover_tap_html}
ROSETTE_JS = ""
_o26 = (HERE / "oct26_littlefold.py").read_text()
_ri = _o26.index("function rosette(")
ROSETTE_JS = "const BERRY='#D9497A';\n" + _o26[_ri:_o26.index("\n", _o26.index("})()}</g>`;}", _ri)) + 1]


def use(key):
    RS.JS = S27.BASE_JS + S27.JS_TEETH + N1.JS + N2.JS + ROSETTE_JS + JS
    RS.html = N1.html
    return SPECS[key], COVERS[key]


if __name__ == "__main__":
    for a in sys.argv:
        if a.startswith("--still="):
            RS.STILLS = [float(x) for x in a[8:].split(",")]
        if a.startswith("--sw="):
            RS.SW = int(a[5:])
    for key in [a for a in sys.argv[1:] if not a.startswith("--")]:
        s, ch = use(key)
        od = OUTS.get(key, OUT)
        od.mkdir(parents=True, exist_ok=True)
        if "--no-cover" not in sys.argv:
            S27.render_cover(ch(), od / f"{s['out']}-cover.jpg")
        if "--cover-only" in sys.argv:
            continue
        r = RS.frames(s, key)
        if r is None:
            print("stills", RS.SCR / f"{key}-stills.jpg")
            continue
        fdir, total, starts = r
        pops = [(st + 0.1, 0.22) for k, st in enumerate(starts) if k > 0]
        pops += [(c, 0.14) for c in s.get("clicks", [])]                      # strap clicks on frame 0
        pops += [(starts[-1] + 0.05 + 0.2 * i + 0.22, 0.12) for i in range(5)] if s.get("clicks") else []
        out = od / f"{s['out']}.mp4"
        N1.encode(fdir, total, s["music"], pops, out)
        print(out, round(total, 2), flush=True)

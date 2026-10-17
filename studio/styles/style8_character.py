#!/usr/bin/env python3
"""Style 8: an original character acts the moment (lf-x-tiny-parade, 103.4 bpm).

"Lockie" - a chubby butter-yellow padlock with a pink shackle, soft-shaded like the 3D props around him.
B1 glued to the phone; B2 dizzy, shackle drooping open while the clock spins; B3 (drop) he snaps awake, flings the
phone through a door, sits at his notebook and his shackle CLICKS shut (he locks in); B4 he bounces and waves,
hearts everywhere. Squash-and-stretch on every jump and landing, eyes blink, idle bob on the beat.
FALLBACK BUILD: drawn as shaded SVG because Canva generation was out of credits; swap in generated frames later.
"""
import json
import sys

from common import Style, fluent, words

TRACK = "lf-x-tiny-parade"


def lockie():
    return """
<g id="lk">
 <ellipse id="lkSh" cx="0" cy="8" rx="210" ry="34" fill="rgba(120,60,10,.22)" filter="url(#bl8)"/>
 <g id="lkBody">
  <g id="legL"><rect x="-120" y="-58" width="78" height="66" rx="33" fill="url(#gLimb)"/></g>
  <g id="legR"><rect x="42" y="-58" width="78" height="66" rx="33" fill="url(#gLimb)"/></g>
  <g id="shk"><path d="M-112,-300 L-112,-372 A112,112 0 0 1 112,-372 L112,-300" fill="none" stroke="url(#gShk)" stroke-width="66" stroke-linecap="round"/>
   <path d="M-128,-330 L-128,-372 A128,128 0 0 1 -60,-480" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="12" stroke-linecap="round"/></g>
  <rect x="-200" y="-340" width="400" height="320" rx="128" fill="url(#gBody)"/>
  <rect x="-200" y="-340" width="400" height="320" rx="128" fill="url(#gRim)"/>
  <ellipse cx="-92" cy="-290" rx="70" ry="30" fill="rgba(255,255,255,.55)" filter="url(#bl4)" transform="rotate(-18 -92 -290)"/>
  <g id="hole" transform="translate(0,-62) scale(.62)"><circle r="20" fill="#C98A1E"/><path d="M-11,6 L11,6 L7,40 L-7,40 Z" fill="#C98A1E"/></g>
  <g id="armL"><rect x="-22" y="0" width="44" height="118" rx="22" fill="url(#gLimb)"/></g>
  <g id="armR"><rect x="-22" y="0" width="44" height="118" rx="22" fill="url(#gLimb)"/></g>
  <g id="face" transform="translate(0,-205)">
   <ellipse cx="-104" cy="44" rx="34" ry="20" fill="#FF7DB5" opacity=".55" filter="url(#bl4)"/>
   <ellipse cx="104" cy="44" rx="34" ry="20" fill="#FF7DB5" opacity=".55" filter="url(#bl4)"/>
   <g id="eyesN">
    <g id="eyeL" transform="translate(-66,0)"><ellipse rx="40" ry="50" fill="#fff"/><g class="pup"><circle r="27" fill="#1d1620"/><circle cx="-9" cy="-12" r="10" fill="#fff"/><circle cx="9" cy="10" r="4.5" fill="#fff"/></g></g>
    <g id="eyeR" transform="translate(66,0)"><ellipse rx="40" ry="50" fill="#fff"/><g class="pup"><circle r="27" fill="#1d1620"/><circle cx="-9" cy="-12" r="10" fill="#fff"/><circle cx="9" cy="10" r="4.5" fill="#fff"/></g></g>
    <rect id="lidL" x="-108" y="-52" width="84" height="0" rx="10" fill="#FFD95A"/><rect id="lidR" x="24" y="-52" width="84" height="0" rx="10" fill="#FFD95A"/>
   </g>
   <g id="eyesS" opacity="0">
    <g transform="translate(-66,0)"><ellipse rx="40" ry="50" fill="#fff"/><path id="spL" d="M0,0 m-4,0 a4,4 0 1,1 8,0 a9,9 0 1,1 -17,0 a14,14 0 1,1 27,0 a19,19 0 1,1 -37,0 a24,24 0 1,1 47,0" fill="none" stroke="#1d1620" stroke-width="6"/></g>
    <g transform="translate(66,0)"><ellipse rx="40" ry="50" fill="#fff"/><path id="spR" d="M0,0 m-4,0 a4,4 0 1,1 8,0 a9,9 0 1,1 -17,0 a14,14 0 1,1 27,0 a19,19 0 1,1 -37,0 a24,24 0 1,1 47,0" fill="none" stroke="#1d1620" stroke-width="6"/></g>
   </g>
   <g id="eyesH" opacity="0"><path d="M-100,6 Q-66,-34 -32,6" fill="none" stroke="#1d1620" stroke-width="12" stroke-linecap="round"/>
    <path d="M32,6 Q66,-34 100,6" fill="none" stroke="#1d1620" stroke-width="12" stroke-linecap="round"/></g>
   <g id="brows" opacity="0"><path d="M-104,-66 L-40,-52" stroke="#1d1620" stroke-width="11" stroke-linecap="round"/><path d="M104,-66 L40,-52" stroke="#1d1620" stroke-width="11" stroke-linecap="round"/></g>
   <path id="mSmile" d="M-26,58 Q0,82 26,58" fill="none" stroke="#1d1620" stroke-width="10" stroke-linecap="round"/>
   <path id="mFlat" d="M-22,66 Q0,60 22,66" fill="none" stroke="#1d1620" stroke-width="10" stroke-linecap="round" opacity="0"/>
   <g id="mOpen" opacity="0"><path d="M-36,52 Q0,120 36,52 Z" fill="#7A2149"/><path d="M-18,86 Q0,98 18,86" fill="#FF7DB5"/></g>
  </g>
 </g>
</g>"""


def build(only=None):
    st = Style(8, "character", TRACK)
    tl = st.tl
    PK, INK, BT, CR = "#FF5CA8", "#141414", "#FFE27A", "#FFF4E0"
    props = {k: fluent(v) for k, v in dict(phone="mobile_phone", clock="alarm_clock", door="door", book="notebook_with_decorative_cover",
                                            pen="pencil", hg="hourglass_not_done", couch="couch_and_lamp", bell="bell", chat="speech_balloon",
                                            eyes="eyes", vib="vibration_mode", heart="sparkling_heart", star="glowing_star", party="party_popper",
                                            heart2="pink_heart", sp="sparkles", zz="dizzy").items()}
    imgs = "".join(f'<img class="pr" id="p_{k}" src="{v}">' for k, v in props.items())
    extra = "".join(f'<img class="pr" id="h{i}" src="{props["heart2" if i % 2 else "heart"]}">' for i in range(8)) + \
        "".join(f'<img class="pr" id="n{i}" src="{props[["bell", "chat", "vib", "star"][i % 4]]}">' for i in range(6))
    svg = f"""<svg id="ch" viewBox="0 0 1080 1920" style="position:absolute;inset:0;width:1080px;height:1920px;overflow:visible">
 <defs>
  <radialGradient id="gBody" cx="36%" cy="24%" r="85%"><stop offset="0" stop-color="#FFF6C4"/><stop offset=".42" stop-color="#FFE27A"/><stop offset=".85" stop-color="#F7BC3C"/><stop offset="1" stop-color="#E9A52A"/></radialGradient>
  <linearGradient id="gRim" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="rgba(255,140,190,.35)"/><stop offset=".3" stop-color="rgba(255,140,190,0)"/></linearGradient>
  <linearGradient id="gShk" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFA8D2"/><stop offset=".5" stop-color="#FF5CA8"/><stop offset="1" stop-color="#C8236A"/></linearGradient>
  <radialGradient id="gLimb" cx="35%" cy="30%" r="90%"><stop offset="0" stop-color="#FFE9A0"/><stop offset="1" stop-color="#F0AE33"/></radialGradient>
  <filter id="bl8" x="-30%" y="-100%" width="160%" height="300%"><feGaussianBlur stdDeviation="9"/></filter>
  <filter id="bl4" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
 </defs>
 <g id="lkPos">{lockie()}</g>
</svg>"""
    css = f"""
    #room{{position:absolute;inset:0;background:linear-gradient(180deg,#FFF1B8 0,#FFE27A 58%,#FFD0E4 58.2%,#FFB6D6 100%)}}
    #rug{{position:absolute;left:140px;top:1440px;width:800px;height:230px;border-radius:50%;background:radial-gradient(ellipse,#FFE9F3 0,#FFC4DE 70%,rgba(255,196,222,0) 72%)}}
    #win{{position:absolute;left:640px;top:600px;width:300px;height:380px;border-radius:150px 150px 24px 24px;background:linear-gradient(180deg,#BDEBFF,#FFF6D6);box-shadow:inset 0 0 0 16px #FFF4E0}}
    #sunw{{position:absolute;left:740px;top:690px;width:110px;height:110px;border-radius:50%;background:radial-gradient(circle,#FFF2A8,#FFC93D)}}
    .pr{{position:absolute;left:0;top:0;width:200px;height:200px;will-change:transform}}
    #ch{{z-index:3}} .pr{{z-index:5}} #p_couch,#p_clock,#p_door{{z-index:2}} .txt{{z-index:9}}
    .em{{color:{PK}}}
    #night{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,140,200,.35),rgba(140,120,255,.18));opacity:0}}
    """
    body = f"""<div id="room"></div><div id="win"></div><div id="sunw"></div><div id="rug"></div><div id="night"></div>
{imgs.replace('id="p_couch"', 'id="p_couch" style="width:420px;height:420px"')}{svg}{extra}
<div class="txt" id="T1" style="top:150px">{words("You opened your phone / to check one thing.", em=("one",))}</div>
<div class="txt" id="T2" style="top:170px;font-size:132px">{words("40 minutes / later…", em=("40",))}</div>
<div class="txt" id="T3a" style="top:130px;font-size:112px">{words("Try this:")}</div>
<div class="txt" id="T3b" style="top:270px;font-size:78px">{words("Phone in another room.")}</div>
<div class="txt" id="T3c" style="top:370px;font-size:78px">{words("One task.", em=("one",))} &nbsp;{words("One hour.", em=("one",))}</div>
<div class="txt" id="T4" style="top:170px;font-size:104px">{words("Your future self / says thanks.", em=("thanks",))}</div>
"""
    js = """
const B=TL.blocks, I=TL.items, beat=TL.beat, D=TL.drop;
const ga=(id,a)=>$(id).setAttribute('transform',a);
function P(id,x,y,s=1,r=0,o=1){ const e=$('p_'+id)||$(id); if(!e) return; e.style.opacity=o; e.style.transform=`translate(${x-100}px,${y-100}px) rotate(${r}deg) scale(${s})`; }
function face(mode){ $('eyesN').setAttribute('opacity',mode==='n'||mode==='f'?1:0); $('eyesS').setAttribute('opacity',mode==='s'?1:0); $('eyesH').setAttribute('opacity',mode==='h'?1:0);
  $('brows').setAttribute('opacity',mode==='f'?1:0); }
function mouth(m){ $('mSmile').setAttribute('opacity',m==='s'?1:0); $('mFlat').setAttribute('opacity',m==='f'?1:0); $('mOpen').setAttribute('opacity',m==='o'?1:0); }
window.seek = async (t) => {
  const bk=blockAt(t); let blur=1; const pb=Math.exp(-sinceBeat(t)/0.13);
  // ---------------- character pose
  let x=540, y=1560, s=1.35, sx=1, sy=1, rot=0, shk=0, armL=20, armR=-20, look=[0,0];
  sy=1-0.04*pb; sx=1+0.03*pb;                                     // idle bounce on the beat
  if(bk===0){ armL=-38; armR=38; look=[0,20]; rot=Math.sin(t*2)*1.5; }
  if(bk===1){ const u=prog(t,B[1].start,0.4); sy*=1-0.12*u; sx*=1+0.06*u; rot=Math.sin(t*3.2)*5; shk=-18*E.out3(u); armL=-20; armR=30; }
  if(bk===2){ // snap awake: jump with stretch, land with squash
    const j=prog(t,D,0.5); const hgt=Math.sin(Math.PI*j)*260; y-=hgt; if(j<1){ const st_=Math.sin(Math.PI*j); sy*=1+0.18*st_; sx*=1-0.1*st_; }
    const land=t-(D+0.5); if(land>0&&land<0.25){ const q=1-land/0.25; sy*=1-0.2*q; sx*=1+0.14*q; }
    // fling the phone
    const f0=I.phone+0.05; const fu=prog(t,f0,0.25); armR=lerp(150,-160,E.out3(fu)); armL=lerp(-150,40,E.out3(prog(t,D,0.3)));
    // shackle clicks shut at the hour item
    shk = t<I.hour ? -28*(1-prog(t,D,0.3)) : 0; if(t>=I.hour && t<I.hour+0.15) { sy*=1-0.08; }
    if(t>=I.task){ x=lerp(540,420,E.inOut(prog(t,I.task,0.35))); armR=lerp(-160,-60,prog(t,I.task,0.3)); armL=40; look=[18,14]; }
  }
  if(bk===3){ const u=t-B[3].start; const hop=Math.abs(Math.sin(u*Math.PI/beat))*90; y-=hop; const air=hop/90; sy*=1+0.08*air-0.1*(1-air)*pb; sx*=1-0.05*air;
    armL=-150+Math.sin(u*14)*30; armR=150; rot=Math.sin(u*Math.PI/beat)*5; x=540; }
  ga('lkPos',`translate(${x},${y}) rotate(${rot}) scale(${s})`);
  ga('lkBody',`scale(${sx},${sy})`);
  ga('shk',`translate(${shk<0?-112:0},${shk<0?-300:0}) rotate(${shk}) translate(${shk<0?112:0},${shk<0?300:0}) translate(0,${shk<0?-20*(-shk/35):0})`);
  ga('armL',`translate(-196,-180) rotate(${armL})`); ga('armR',`translate(196,-180) rotate(${armR})`);
  $$('.pup').forEach(p=>p.setAttribute('transform',`translate(${look[0]},${look[1]})`));
  // blink every ~2.3 s (not in dizzy)
  const bt=(t%2.3); const bl=bt<0.12?Math.sin(bt/0.12*Math.PI):0; ['lidL','lidR'].forEach(id=>$(id).setAttribute('height',(104*bl).toFixed(1)));
  if(bk===0){ face('n'); mouth('f'); } if(bk===1){ face('s'); mouth('o'); $('spL').setAttribute('transform',`rotate(${t*400})`); $('spR').setAttribute('transform',`rotate(${-t*400})`); }
  if(bk===2){ face(t<I.task?'n':'f'); mouth(t<I.task?'o':'s'); } if(bk===3){ face('h'); mouth('o'); }
  // ---------------- props
  const hand=[x+ (196+40)*s*sx, y-(180-110)*s];      // right hand (approx.)
  // phone: in hands (B1-B2), flung through the door (B3)
  if(bk<=1 || t<I.phone+0.05){ const held=bk===2; P('phone',held?x+250:x+(bk===1?70:0),held?y-430:y-(bk===1?55:72)*s*sy,bk===1?0.85:0.9,bk===1?28:-4); }
  else { const fu=prog(t,I.phone+0.12,0.55); const px=lerp(x+200,900,fu), py=lerp(y-420,1180,fu)-Math.sin(Math.PI*fu)*360; P('phone',px,py,1.05*(1-0.5*fu),fu*720,fu<1?1:0); if(fu>0&&fu<1) blur=3; }
  // door: slides in for the throw, slams, slides away
  const dIn=E.out3(prog(t,I.phone-0.1,0.25)), dOut=E.in3(prog(t,I.phone+0.95,0.25)); const dOn=bk===2&&t>=I.phone-0.1;
  P('door',lerp(1300,900,dIn)+400*dOut,1150,2.1,0,dOn?1:0);
  // couch behind in B1/B2
  $('p_couch').style.opacity=bk<=1?1:0; $('p_couch').style.transform=`translate(80px,1020px) scale(1)`;
  // notifications swarm (B1 builds, B2 piles)
  for(let i=0;i<6;i++){ const t0=1.2+i*beat*0.5; const on=bk<=1&&t>=t0; const u=spring(t,t0,3,0.4);
    const ang=-2.6+i*0.45; const R=330+(bk===1?60:0); $('n'+i).style.opacity=on?1:0;
    $('n'+i).style.transform=`translate(${540+Math.cos(ang)*R*u-100}px,${1180+Math.sin(ang)*R*0.6*u-100+Math.sin(t*3+i)*12}px) scale(${0.55*u+0.0001}) rotate(${Math.sin(t*4+i)*10}deg)`; }
  // clock spins in B2
  const ck=spring(t,B[1].start,3,0.4); P('clock',830,800,bk===1?0.9*ck+0.0001:0.0001,Math.sin(t*40)*8,bk===1?1:0);
  P('zz',540,y-640*s*sy+ (bk===1?100:0),bk===1?0.8:0.0001,t*200,bk===1?1:0);
  $('night').style.opacity=bk===1?0.9*Math.sin(Math.PI*prog(t,B[1].start,B[2].start-B[1].start)):0;
  // B3: book, pencil, hourglass
  const bo=bk===2&&t>=I.task; P('book',720,1440,bo?1.6*spring(t,I.task,3,0.42)+0.0001:0.0001,-8,bo?1:0);
  P('pen',840,1360,bo?1.2*spring(t,I.task+beat/2,3,0.42)+0.0001:0.0001,Math.sin(t*12)*10+20,bo&&t>=I.task+beat/2?1:0);
  const ho=bk===2&&t>=I.hour; P('hg',880,1130,ho?1.4*spring(t,I.hour,3,0.42)+0.0001:0.0001,0,ho?1:0);
  // click sparkle when the shackle locks
  const cl=prog(t,I.hour,0.4); P('sp',540+(x-540)-10,y-640*s,bk===2&&t>=I.hour?(0.6+0.8*cl):0.0001,cl*90,bk===2&&t>=I.hour?1-cl*0.6:0);
  // B4 hearts fountain + party
  for(let i=0;i<8;i++){ const t0=B[3].start+0.2+i*beat/2; const dt=t-t0; const on=bk===3&&dt>0; const a=-1.57+(i-3.5)*0.32;
    $('h'+i).style.opacity=on?Math.max(0,1-dt/2.2):0; $('h'+i).style.transform=`translate(${540+Math.cos(a)*520*E.out3(clamp(dt/1.2))-100}px,${1050+Math.sin(a)*520*E.out3(clamp(dt/1.2))+dt*dt*90-100}px) scale(${0.6+0.2*(i%3)}) rotate(${Math.sin(t*5+i)*16}deg)`; }
  P('party',220,1180,bk===3?0.95*spring(t,B[3].start+0.3,3,0.4)+0.0001:0.0001,-10,bk===3?1:0);
  P('star',870,1100,bk===3?0.9*spring(t,B[3].start+0.3+beat,3,0.4)+0.0001:0.0001,t*30,bk===3?1:0);
  P('heart',820,1450,0.0001,0,0); P('bell',0,0,0.0001,0,0); P('chat',0,0,0.0001,0,0); P('eyes',0,0,0.0001,0,0); P('vib',0,0,0.0001,0,0); P('heart2',0,0,0.0001,0,0);
  // ---------------- text
  vis($('T1'),bk===0); kwords($('T1'),t,-1,{});
  vis($('T2'),bk===1); if(bk===1) kwords($('T2'),t,B[1].start,{mode:'drop',gap:0.08,f:2.8,z:0.42});
  vis($('T3a'),bk===2); if(bk===2) kwords($('T3a'),t,D,{mode:'stamp',gap:0.1,f:3,z:0.42});
  vis($('T3b'),bk===2&&t>=I.phone); if(bk===2) kwords($('T3b'),t,I.phone,{mode:'pop',gap:0.06});
  vis($('T3c'),bk===2&&t>=I.task); if(bk===2){ $$('.w',$('T3c')).forEach((w,i)=>{ const s0=(i<2?I.task:I.hour)+(i%2)*0.07; const u2=spring(t,s0,2.6,0.4);
      w.style.opacity=t<s0?0:prog(t,s0,0.1); w.style.transform=`translateY(${(1-u2)*50}px) scale(${0.5+0.5*u2})`; }); }
  vis($('T4'),bk===3); if(bk===3) kwords($('T4'),t,B[3].start,{mode:'pop',gap:0.07});
  const sk=shake(t,D,0.35,22); $('stage').style.transform=`translate(${sk.x}px,${sk.y}px)`;
  if(t>=D-0.03&&t<D+0.1) blur=3;
  await flush(); return {blur};
};
"""
    st.default_sfx(cut="sfx-x-swoosh-in", b4="sfx-x-whoosh-hit")
    B, I, beat, D = tl["blocks"], tl["items"], tl["beat"], tl["drop"]
    for i in range(6):
        if 1.2 + i * beat * 0.5 < B[2]["start"]:
            st.add_sfx(1.2 + i * beat * 0.5, "sfx-x-sticker-pop", -11)
    st.add_sfx(B[1]["start"] + 0.1, "sfx-x-tick-tock", -11)
    st.add_sfx(I["phone"] + 0.12, "sfx-x-swoosh-in", -5)
    st.add_sfx(I["phone"] + 0.67, "sfx-x-paper-slap", -4)
    st.add_sfx(I["task"], "sfx-x-sticker-pop", -8)
    st.add_sfx(I["hour"], "sfx-x-camera-shutter", -6)        # the lock clicks
    st.add_sfx(B[3]["start"] + 0.3, "sfx-x-sticker-pop", -6)
    if only == "remix":
        return st.remix()
    return st.build(css, body, js, only=only)


if __name__ == "__main__":
    only = ("remix" if sys.argv[1] == "remix" else [int(x) for x in sys.argv[1].split(",")]) if len(sys.argv) > 1 else None
    print(build(only))

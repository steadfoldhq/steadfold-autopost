#!/usr/bin/env python3
"""Style 2: bright real footage with tracked hand-drawn doodles (lh-x-lock-in, 126 bpm).

Doodles are SVG strokes that write themselves on, "boil" like hand-drawn animation (displacement re-seeded 10x a
second) and ride on points tracked through each clip (common.track). Cuts: whip pan -> zoom punch on the drop ->
beat cut -> pink iris. The frame pulses on every beat.
"""
import json
import sys

from common import CACHE, Style, track, words

TRACK = "lh-x-lock-in"
CLIPS = {"b1": (335, 605, 35), "b2": (520, 820, 70), "b3b": (459, 1272, 70), "b3c": (540, 1350, 70), "b4": (580, 1080, 70)}


def build(only=None):
    st = Style(2, "footage-doodles", TRACK)
    tl = st.tl
    tr = {k: track(CACHE / f"s2_{k}", x, y, win=w) for k, (x, y, w) in CLIPS.items()}
    imgs = "".join(
        f'<div class="clip" id="c_{k}"><img id="v_{k}" data-clip="{(CACHE / f"s2_{k}").as_uri()}" '
        f'data-n="{len(tr[k])}"></div>' for k in CLIPS)
    PK, INK, BT, CR = "#FF5CA8", "#141414", "#FFE27A", "#FFF8EA"
    css = f"""
    .clip{{position:absolute;inset:0;overflow:hidden;visibility:hidden}}
    .clip img{{position:absolute;inset:0;width:1080px;height:1920px;transform-origin:50% 50%}}
    #dood{{position:absolute;inset:0;width:1080px;height:1920px;pointer-events:none}}
    .d{{fill:none;stroke-linecap:round;stroke-linejoin:round}}
    .hand{{font-family:'Caveat Brush';fill:{PK}}}
    .t1{{top:170px;font-size:86px}}
    .em{{color:{PK}}}
    .big40{{font:900 340px/0.9 Inter;letter-spacing:-0.06em;color:{PK};text-shadow:0 10px 34px rgba(0,0,0,.30)}}
    .later{{font:900 104px/1 Inter;color:{CR};letter-spacing:-0.04em}}
    #flash{{position:absolute;inset:0;background:radial-gradient(circle at 50% 45%,#fff 0,{BT} 45%,{PK} 100%);opacity:0}}
    #iris{{position:absolute;left:-860px;top:-500px;width:2800px;height:2800px;border-radius:50%;background:{PK};transform:scale(0);opacity:0}}
    .li{{position:absolute;left:200px;font:900 78px/1.05 Inter;letter-spacing:-0.03em;color:{INK};
         text-shadow:0 4px 18px rgba(255,248,234,.55),0 2px 6px rgba(0,0,0,.12);white-space:nowrap}}
    .try{{position:absolute;left:0;width:1080px;text-align:center;top:190px;font:900 128px/1 Inter;letter-spacing:-0.045em;color:{INK};
          text-shadow:0 6px 24px rgba(255,248,234,.6),0 2px 6px rgba(0,0,0,.12)}}
    """
    # ---------------------------------------------------------------- doodle SVG (paths use pathLength=1 for write-on)
    def p(d, col=PK, w=12, cls="", extra=""):
        return f'<path class="d {cls}" d="{d}" stroke="{col}" stroke-width="{w}" pathLength="1" {extra}/>'

    scrib = " ".join(f"{'M' if i == 0 else 'L'}{665 + 400 * __import__('math').cos(a):.0f},{1165 + 640 * __import__('math').sin(a):.0f}"
                     for i, a in enumerate([-2.2 + k * 0.069 + 0.02 * __import__('math').sin(k) for k in range(100)]))
    rays = "".join(p(f"M{__import__('math').cos(a) * 210:.0f},{__import__('math').sin(a) * 210:.0f} "
                     f"L{__import__('math').cos(a) * 330:.0f},{__import__('math').sin(a) * 330:.0f}", BT, 16, "ray")
                   for a in [k * 0.5236 for k in range(12)])
    tick12 = "".join(p(f"M{__import__('math').cos(a) * 250:.0f},{__import__('math').sin(a) * 250:.0f} "
                       f"L{__import__('math').cos(a) * 285:.0f},{__import__('math').sin(a) * 285:.0f}", CR, 9, "tk")
                     for a in [k * 0.5236 for k in range(12)])
    svg = f"""
<svg id="dood" viewBox="0 0 1080 1920">
 <defs><filter id="boil"><feTurbulence id="turb" type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="1"/>
   <feDisplacementMap in="SourceGraphic" scale="7"/></filter>
   <filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity=".22"/></filter></defs>
 <g filter="url(#boil)"><g filter="url(#soft)">
  <g id="g1">
   <g id="g1t">{p(scrib, PK, 13, "draw", 'id="scrib"')}
     <path id="arw1" d="M0,0"/><path id="arw1h" d="M0,0"/>
   </g>
   <g id="dings"></g>
   <text class="hand" id="just" x="250" y="610" font-size="92" transform="rotate(-5 250 610)">just one thing…</text>
  </g>
  <g id="g2">
   <g id="g2t">
     <g id="swirl" transform="translate(0,-330)">{p("M0,0 m-300,0 a300,80 0 1,0 600,0 a300,80 0 1,0 -600,0", CR, 9, "draw", 'id="halo"')}<g id="stars"></g></g>
     {p("M-310,-120 l-60,-40 M-320,-40 l-80,-10 M-300,40 l-70,30", BT, 12, "draw", 'id="stress"')}
     <g id="clk" transform="translate(-290,560)">
       <circle r="92" fill="{CR}" stroke="{INK}" stroke-width="10"/>
       <line id="hm" x1="0" y1="0" x2="0" y2="-62" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
       <line id="hh" x1="0" y1="0" x2="0" y2="-40" stroke="{PK}" stroke-width="12" stroke-linecap="round"/>
     </g>
   </g>
  </g>
  <g id="g3">
   <g id="burst">{''.join(p(f"M{540 + __import__('math').cos(a) * 160:.0f},{900 + __import__('math').sin(a) * 160:.0f} L{540 + __import__('math').cos(a) * 900:.0f},{900 + __import__('math').sin(a) * 900:.0f}", BT if k % 2 else PK, 30, "br") for k, a in enumerate([k * 0.3927 for k in range(16)]))}</g>
   <g id="box1">{p("M0,0 h58 v58 h-58 z", INK, 8, "draw")}{p("M8,30 L26,52 L70,-14", PK, 13, "draw chk")}</g>
   <g id="box2">{p("M0,0 h58 v58 h-58 z", INK, 8, "draw")}{p("M8,30 L26,52 L70,-14", PK, 13, "draw chk")}</g>
   <g id="box3">{p("M0,0 h58 v58 h-58 z", INK, 8, "draw")}{p("M8,30 L26,52 L70,-14", PK, 13, "draw chk")}</g>
   <g id="door" transform="translate(860,1080)">
     {p("M-95,140 L-95,-150 Q-95,-170 -75,-170 L75,-170 Q95,-170 95,-150 L95,140", INK, 11, "draw")}
     <g id="leaf">{p("M-80,135 L-80,-155 L80,-155 L80,135 Z", PK, 10, "draw")}<circle cx="55" cy="0" r="10" fill="{PK}"/></g>
   </g>
   <g id="dphone">{p("M-55,-95 h110 q16,0 16,16 v158 q0,16 -16,16 h-110 q-16,0 -16,-16 v-158 q0,-16 16,-16 z", INK, 10, "draw")}
     {p("M-20,-78 h40", INK, 8, "draw")}<text class="hand" x="-30" y="22" font-size="70">zz</text></g>
   {p("M300,1180 C 450,980 650,980 800,1060", PK, 8, "dash", 'id="flight"')}
   <text class="hand" id="bye" x="610" y="890" font-size="104" transform="rotate(-8 610 890)">bye!</text>
   <g id="ring">{p("M0,0 m-262,0 a262,262 0 1,0 524,0 a262,262 0 1,0 -524,0", PK, 14, "draw", 'id="ringc"')}{tick12}
     <text class="hand" x="150" y="-250" font-size="92" fill="{BT}" style="fill:{BT}">1 hr</text></g>
  </g>
  <g id="g4">
   <g id="sun">{rays}</g>
   <g id="hearts"></g>
   <text class="hand" id="ty" x="360" y="1620" font-size="120" transform="rotate(-5 360 1620)">thank you!!</text>
  </g>
 </g></g>
</svg>"""
    t1 = words("You opened your phone / to check one thing.", em=("one",))
    body = f"""{imgs}{svg}
<div id="flash"></div><div id="iris"></div>
<div class="txt t1" id="T1">{t1}</div>
<div class="txt" id="T2" style="top:150px"><div class="big40" id="n40">40</div><div class="later" id="lat">{words("minutes later…")}</div></div>
<div class="try" id="T3">{words("Try this:")}</div>
<div class="li" id="L1" style="top:440px">{words("Phone in another room.")}</div>
<div class="li" id="L2" style="top:560px">{words("One task.")}</div>
<div class="li" id="L3" style="top:680px">{words("One hour.")}</div>
<div class="txt" id="T4" style="top:200px;font-size:100px">{words("Your future self / says thanks.", em=("thanks",))}</div>
"""
    js = """
const TR=""" + json.dumps(tr) + """;
const B=TL.blocks, I=TL.items, beat=TL.beat;
const PK='#FF5CA8';
function draw(el,t,t0,d){ if(!el) return; const u=E.out3(prog(t,t0,d)); el.style.strokeDasharray='1 1'; el.style.strokeDashoffset=1-u; el.style.opacity=t<t0?0:1; }
function drawAll(root,t,t0,d,stag=0.05){ $$('.draw',root).forEach((e,i)=>draw(e,t,t0+i*stag,d)); }
// notification doodles that pop out of the phone on beats
const dings=$('dings'); const DN=7;
for(let i=0;i<DN;i++){ const g=document.createElementNS('http://www.w3.org/2000/svg','g');
  g.innerHTML=`<rect x="-120" y="-44" width="240" height="88" rx="26" fill="#FFF8EA" stroke="#141414" stroke-width="8"/>
   <circle cx="-78" cy="0" r="20" fill="${['#FF5CA8','#FFE27A','#7BD3FF','#FF5CA8','#9BE58B','#FFE27A','#FF5CA8'][i]}"/>
   <path d="M-44,-10 h120 M-44,14 h80" stroke="#141414" stroke-width="9" stroke-linecap="round"/>`;
  dings.appendChild(g); }
for(let i=0;i<3;i++){ const g=document.createElementNS('http://www.w3.org/2000/svg','path'); g.setAttribute('d','M0,-30 L9,-9 L30,0 L9,9 L0,30 L-9,9 L-30,0 L-9,-9 Z'); g.setAttribute('fill','#FFE27A'); g.setAttribute('stroke','#141414'); g.setAttribute('stroke-width','5'); $('stars').appendChild(g); }
const DPOS=[[-430,-260],[300,-140],[-450,60],[320,180],[-430,380],[300,500],[-60,-420]];
// hearts
const hearts=$('hearts');
for(let i=0;i<6;i++){ const g=document.createElementNS('http://www.w3.org/2000/svg','path');
  g.setAttribute('d','M0,18 C-30,-8 -22,-34 0,-20 C22,-34 30,-8 0,18 Z'); g.setAttribute('fill',i%2?'#FF5CA8':'#FFE27A');
  g.setAttribute('stroke','#141414'); g.setAttribute('stroke-width','5'); hearts.appendChild(g); }

window.seek = async (t) => {
  // boil: re-seed the displacement 10x a second (hand-drawn line life)
  $('turb').setAttribute('seed', 1 + (Math.floor(t*10)%4));
  const bk=blockAt(t); let blur=1;
  const pulse = 1 + 0.018*Math.exp(-sinceBeat(t)/0.09);
  // ---------- clips: which one, local time, transforms
  const C={b1:[B[0].start,B[1].start],b2:[B[1].start,B[2].start],b3c:[B[2].start,I.task-0.02],b3b:[I.task-0.02,B[3].start],b4:[B[3].start,TL.dur]};
  for(const k in C){ const [a,b]=C[k]; const on=t>=a&&t<b; vis($('c_'+k),on); if(on){ foot($('v_'+k),Math.max(0,t-a)); } }
  // camera: slow push + beat pulse
  for(const k in C){ const [a,b]=C[k]; const u=clamp((t-a)/(b-a)); tf($('v_'+k),{s:(1.02+0.06*u)*pulse}); }
  // whip B1 -> B2 (horizontal, 0.24 s)
  const w0=B[1].start-0.12, wu=prog(t,w0,0.24);
  if(t>=w0-0.01 && t<=w0+0.25){ blur=4; const e=E.inOut(wu);
    tf($('c_b1'),{x:-1180*e}); vis($('c_b1'),true); tf($('c_b2'),{x:1180*(1-e)}); vis($('c_b2'),true); }
  else { tf($('c_b1'),{}); tf($('c_b2'),{}); }
  // zoom punch into the drop
  const z0=B[2].start; const zin=prog(t,z0-0.14,0.14), zout=prog(t,z0,0.3);
  if(t>=z0-0.14 && t<z0){ blur=4; tf($('c_b2'),{s:1+1.6*E.in3(zin)}); }
  if(t>=z0 && t<z0+0.3){ tf($('c_b3c'),{s:1.5-0.5*E.out5(zout)}); if(t<z0+0.12) blur=3; }
  $('flash').style.opacity = t>=z0-0.06 && t<z0+0.28 ? (1-prog(t,z0-0.06,0.34))*0.95 : 0;
  // iris into B4
  const i0=B[3].start; const iu=prog(t,i0-0.2,0.42);
  if(t>=i0-0.2 && t<i0+0.22){ $('iris').style.transform=`scale(${E.inOut(iu)})`;
     $('iris').style.opacity= iu<0.5?1:1-(iu-0.5)*2; vis($('c_b4'), iu>0.5); vis($('c_b3b'), iu<=0.5); }
  else $('iris').style.opacity=0;
  // shake on the drop
  const sk=shake(t,z0,0.32,22); $('stage').style.transform=`translate(${sk.x}px,${sk.y}px)`;

  // ---------- text
  const T1=$('T1'); vis(T1,bk===0); if(bk===0){ kwords(T1,t,-1,{}); tf(T1,{x:t>=w0?-1180*E.inOut(wu):0, y:Math.sin(t*2.2)*4}); }
  const T2=$('T2'); vis(T2,bk===1); if(bk===1){ const u=spring(t,B[1].start,2.4,0.36);
     tf($('n40'),{s:0.3+0.7*u, r:(1-u)*-12}); $('n40').style.opacity=prog(t,B[1].start,0.08);
     kwords($('lat'),t,B[1].start+0.12,{mode:'up',gap:0.08}); }
  vis($('T3'),bk===2); if(bk===2) kwords($('T3'),t,B[2].start,{mode:'stamp',gap:0.09,f:2.8,z:0.45});
  [['L1',I.phone],['L2',I.task],['L3',I.hour]].forEach(([id,t0])=>{ const el=$(id); vis(el,bk===2&&t>=t0); if(bk===2) kwords(el,t,t0,{mode:'slide',gap:0.06}); });
  const T4=$('T4'); vis(T4,bk===3); if(bk===3) kwords(T4,t,B[3].start+0.05,{mode:'pop',gap:0.08});

  // ---------- doodles
  const fr=k=>{ const [a]=C[k]; const arr=TR[k]; return arr[Math.min(arr.length-1,Math.max(0,Math.floor((t-a)*30)))]; };
  const sh_=(id,on)=>{$(id).style.display=on?'inline':'none'}; sh_('g1',bk===0||(t<B[1].start+0.1)); sh_('g2',bk===1); sh_('g3',bk===2); sh_('g4',bk===3);
  if(bk===0||t<B[1].start+0.1){ const [x,y]=fr('b1'); const off = t>=w0 ? -1180*E.inOut(wu) : 0; $('just').setAttribute('transform',`rotate(-5 250 610) translate(${off},0)`);
    $('g1t').setAttribute('transform',`translate(${x-335+off},${y-605})`);
    draw($('scrib'),t,0.15,0.6); draw($('arw1'),t,1.05,0.3); draw($('arw1h'),t,1.3,0.12);
    const j=$('just'); j.style.opacity=prog(t,0.9,0.15); j.style.clipPath=`inset(0 ${100-100*E.out3(prog(t,0.9,0.5))}% 0 0)`;
    // dings pop out on beats after 1.6 s
    const firstBeat=TL.beats.find(b=>b>=1.55);
    $$('g',dings).forEach((g,i)=>{ const t0=firstBeat+i*beat*0.5; const u=spring(t,t0,3,0.4);
      const [dx,dy]=DPOS[i]; const px=x-335+665+dx*u+off, py=y-605+1165+dy*u - (t-t0)*24*(t>t0);
      g.setAttribute('transform',`translate(${px},${py}) scale(${0.2+0.8*u}) rotate(${(i%2?6:-6)})`); g.style.opacity=t<t0?0:1; }); }
  if(bk===1){ const [x,y]=fr('b2'); $('g2t').setAttribute('transform',`translate(${x},${y-40})`);
    draw($('halo'),t,B[1].start+0.05,0.45); draw($('stress'),t,B[1].start+0.25,0.3);
    $$('path',$('stars')).forEach((g,i)=>{ const a=(t-B[1].start)*5+i*2.094; const d=Math.sin(a); g.setAttribute('transform',`translate(${Math.cos(a)*300},${d*80}) scale(${0.8+0.35*d})`); });
    const ck=spring(t,B[1].start+0.1,2.6,0.4); $('clk').setAttribute('transform',`translate(-300,520) scale(${ck})`);
    const sp=(t-B[1].start); $('hm').setAttribute('transform',`rotate(${sp*1080})`); $('hh').setAttribute('transform',`rotate(${sp*90})`); }
  if(bk===2){
    // burst on the drop
    $$('.br').forEach((e,i)=>{ const u=prog(t,B[2].start,0.32); e.style.strokeDasharray='1 1'; e.style.strokeDashoffset=-E.out3(u); e.style.opacity=u<1?1:0; });
    [['box1',I.phone,440],['box2',I.task,560],['box3',I.hour,680]].forEach(([id,t0,y])=>{ const g=$(id); vis(g,t>=t0);
       g.setAttribute('transform',`translate(105,${y+12})`);
       const [bx,ck]=$$('.draw',g); draw(bx,t,t0,0.25);
       const tb=TL.beats.find(b=>b>=t0+0.45)||t0+0.5; draw(ck,t,tb,0.18); });
    // phone flies out through the door
    const ph=$('dphone'), t0=I.phone+0.1, fu=E.inOut(prog(t,t0+0.35,0.75));
    vis(ph,t>=t0 && fu<1 && t<I.task); const sx=lerp(300,830,fu), sy=lerp(1180,1060,fu)-Math.sin(fu*Math.PI)*170;
    ph.setAttribute('transform',`translate(${sx},${sy}) rotate(${fu*28}) scale(${(0.2+0.8*spring(t,t0,3,0.45))*(1-0.55*fu)})`);
    drawAll(ph,t,t0,0.25,0.04);
    const fl=$('flight'); vis(fl,t>=t0&&t<I.task); fl.style.strokeDasharray='0.02 0.025'; fl.style.strokeDashoffset=-t*0.2; fl.style.opacity=0.85*prog(t,t0+0.2,0.2);
    const dr=$('door'); vis(dr,t>=t0&&t<I.task); drawAll(dr,t,t0+0.05,0.3,0.06);
    const open=prog(t,t0+0.3,0.2)*(1-prog(t,t0+1.1,0.12)); $('leaf').setAttribute('transform',`scale(${1-0.75*open},1) translate(${-80*open},0)`);
    const by=$('bye'); vis(by,t>=t0+1.15&&t<I.task); by.setAttribute('transform',`rotate(-8 610 890) translate(0,${(1-spring(t,t0+1.15,3,0.4))*60})`);
    if(t>=t0+1.08&&t<t0+1.4){ const s2=shake(t,t0+1.1,0.25,10); $('stage').style.transform=`translate(${s2.x}px,${s2.y}px)`; }
    // timer ring around the cup
    const rg=$('ring'); vis(rg,t>=I.task); if(t>=I.task){ const [x,y]=fr('b3b'); rg.setAttribute('transform',`translate(${x+10},${y-60}) scale(0.9)`);
      draw($('ringc'),t,I.task+0.05,0.5); $$('.tk',rg).forEach((e,i)=>draw(e,t,I.hour+i*0.025,0.12)); }
  }
  if(bk===3){ const [x,y]=fr('b4'); const t0=B[3].start;
    $('sun').setAttribute('transform',`translate(${x+10},${y-20}) rotate(${(t-t0)*25}) scale(${0.6+0.4*spring(t,t0+0.15,2.2,0.4)})`);
    $$('.ray').forEach((e,i)=>draw(e,t,t0+0.12+i*0.03,0.25));
    $$('path',$('hearts')).forEach((h,i)=>{ const s0=t0+0.35+i*beat*0.5; const u=prog(t,s0,1.6);
      const hx=x+[-260,240,-330,300,-160,180][i], hy=y+[-120,-60,140,180,-300,-320][i]-u*260;
      h.setAttribute('transform',`translate(${hx},${hy}) scale(${(t<s0?0:1)*(0.6+0.9*spring(t,s0,3,0.4))}) rotate(${Math.sin(t*4+i)*10})`); h.style.opacity=1-Math.max(0,u-0.75)*4; });
    const ty=$('ty'); ty.style.opacity=prog(t,t0+0.9,0.1); ty.style.clipPath=`inset(0 ${100-100*E.out3(prog(t,t0+0.9,0.55))}% 0 0)`; }
  await flush();
  return {blur};
};
"""
    st.default_sfx(cut="sfx-x-swoosh-in", b4="sfx-x-whoosh-hit")
    st.add_sfx(tl["items"]["phone"] + 1.2, "sfx-x-paper-slap", -6)          # door slams
    for k, b in enumerate([x for x in tl["beats"] if x >= 1.55][:7]):        # dings pop on half beats
        st.add_sfx(1.55 + 0 if False else [x for x in tl["beats"] if x >= 1.55][0] + k * tl["beat"] * 0.5, "sfx-x-sticker-pop", -12)
    for key in ("phone", "task", "hour"):
        st.add_sfx(tl["items"][key], "sfx-x-sticker-pop", -10)
    st.add_sfx(tl["blocks"][1]["start"] + 0.1, "sfx-x-tick-tock", -14)
    if only == 'remix':
        return st.remix()
    return st.build(css, body, js, only=only)


if __name__ == "__main__":
    only = ('remix' if sys.argv[1] == 'remix' else [int(x) for x in sys.argv[1].split(",")]) if len(sys.argv) > 1 else None
    print(build(only))

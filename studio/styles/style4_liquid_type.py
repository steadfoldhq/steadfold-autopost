#!/usr/bin/env python3
"""Style 4: liquid colour blobs behind huge kinetic type (lh-x-tick-boom, 99.4 bpm).

Gooey metaballs (SVG blur + alpha threshold) drift and pulse on every beat behind poster-scale words. Each block
floods in as a liquid wipe of the next colour; on the drop the blobs burst into droplets on an ink stage.
"""
import json
import math
import sys

from common import Style, words

TRACK = "lh-x-tick-boom"


def build(only=None):
    st = Style(4, "liquid-type", TRACK)
    tl = st.tl
    PK, INK, BT, CR = "#FF5CA8", "#141414", "#FFE27A", "#FFF4E0"
    # palettes per block: (stage, blobA, blobB, text)
    PAL = [(CR, PK, BT, INK), (PK, BT, "#FF8CC4", CR), (INK, PK, BT, CR), (BT, PK, CR, INK)]
    NB = 9
    groups = ""
    for k, (bg, a, b, _) in enumerate(PAL):
        circles_a = "".join(f'<circle id="a{k}_{i}" r="10" fill="{a}"/>' for i in range(NB))
        circles_b = "".join(f'<circle id="b{k}_{i}" r="10" fill="{b}"/>' for i in range(NB))
        drops = "".join(f'<circle id="d{k}_{i}" r="0" fill="{a if i % 2 else b}"/>' for i in range(24)) if k == 2 else ""
        groups += (f'<g id="L{k}"><rect width="1080" height="1920" fill="{bg}"/>'
                   f'<g filter="url(#goo)">{circles_a}</g><g filter="url(#goo)">{circles_b}{drops}</g></g>')
    flood = "".join(f'<g id="F{k}" filter="url(#goo)">' + "".join(
        f'<circle id="f{k}_{i}" r="0" fill="{PAL[k][0]}"/>' for i in range(7)) + "</g>" for k in (1, 2, 3))
    svg = f"""<svg id="liq" viewBox="0 0 1080 1920" style="position:absolute;inset:0;width:1080px;height:1920px">
 <defs><filter id="goo" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur in="SourceGraphic" stdDeviation="28" result="b"/>
 <feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 36 -16"/></filter></defs>
 {groups}{flood}</svg>"""
    css = f"""
    .k{{position:absolute;left:0;width:1080px;text-align:center;font-family:Inter;font-weight:900;letter-spacing:-0.055em;line-height:.9;
        text-shadow:0 8px 30px rgba(0,0,0,.14)}}
    .k .w{{transform-origin:50% 80%}}
    .ink{{color:{INK}}} .cr{{color:{CR};text-shadow:0 8px 30px rgba(0,0,0,.25)}} .pk{{color:{PK}}} .bt{{color:{BT}}}
    .ser{{font-family:'Instrument Serif';font-style:italic;font-weight:400;letter-spacing:-0.02em}}
    """
    body = f"""{svg}
<div id="K1">
 <div class="k ink" style="top:230px;font-size:120px">{words("You opened")}</div>
 <div class="k ink" style="top:350px;font-size:150px">{words("your")} <span class="ser" style="font-size:190px">{words("phone")}</span></div>
 <div class="k ink" style="top:560px;font-size:118px">{words("to check")}</div>
 <div class="k pk" id="one1" style="top:650px;font-size:420px">{words("one")}</div>
 <div class="k ink" style="top:1030px;font-size:150px">{words("thing.")}</div>
</div>
<div id="K2">
 <div class="k ink" id="n40" style="top:330px;font-size:620px">{words("40")}</div>
 <div class="k ink" style="top:900px;font-size:150px">{words("minutes")}</div>
 <div class="k cr ser" style="top:1040px;font-size:190px">{words("later…")}</div>
</div>
<div id="K3">
 <div class="k cr" id="try" style="top:170px;font-size:160px">{words("Try this:")}</div>
 <div class="k" id="it1" style="top:420px;font-size:112px"><span class="cr">{words("Phone in")}</span> <span class="bt">{words("another")}</span><br><span class="bt">{words("room.")}</span></div>
 <div class="k" id="it2" style="top:700px;font-size:200px"><span class="pk">{words("One")}</span> <span class="cr">{words("task.")}</span></div>
 <div class="k" id="it3" style="top:900px;font-size:200px"><span class="bt">{words("One")}</span> <span class="cr">{words("hour.")}</span></div>
</div>
<div id="K4">
 <div class="k ink" style="top:300px;font-size:130px">{words("Your future self")}</div>
 <div class="k ink" style="top:450px;font-size:130px">{words("says")}</div>
 <div class="k pk ser" id="thx" style="top:560px;font-size:330px">{words("thanks.")}</div>
</div>
"""
    js = """
const B=TL.blocks, I=TL.items, beat=TL.beat, D=TL.drop; const NB=""" + str(NB) + """;
let _s=5; const rnd=()=>{ _s=(_s*16807)%2147483647; return (_s-1)/2147483646; };
const spot=(i)=> i<6 ? {x:rnd()*1080, y:1420+rnd()*560} : {x:(i%2?-40:1120), y:rnd()*260+(i===8?1100:0)};
const P=[0,1,2,3].map(()=>[...Array(NB)].map((_,i)=>{ const s=spot(i); return {x:s.x,y:s.y,r:(i<6?120+rnd()*150:90+rnd()*70),fx:0.2+rnd()*0.5,fy:0.2+rnd()*0.5,ph:rnd()*6.28,ax:60+rnd()*120,ay:40+rnd()*90}; }));
const Q=[0,1,2,3].map(()=>[...Array(NB)].map((_,i)=>{ const s=spot(i); return {x:s.x,y:s.y+60,r:(i<6?90+rnd()*130:70+rnd()*60),fx:0.2+rnd()*0.5,fy:0.2+rnd()*0.5,ph:rnd()*6.28,ax:60+rnd()*140,ay:40+rnd()*90}; }));
const DR=[...Array(24)].map(()=>({a:rnd()*6.28,v:500+rnd()*1600,r:20+rnd()*60}));
const FL=[...Array(7)].map((_,i)=>({x:540+Math.cos(i*0.9)*260*(i?1:0),y:960+Math.sin(i*0.9)*420*(i?1:0)}));
function setC(id,x,y,r){ const c=$(id); c.setAttribute('cx',x.toFixed(1)); c.setAttribute('cy',y.toFixed(1)); c.setAttribute('r',Math.max(0,r).toFixed(1)); }
window.seek = async (t) => {
  const bk=blockAt(t); let blur=1;
  const pb=Math.exp(-sinceBeat(t)/0.11);
  // layers: show current block layer (+ next during its flood)
  for(let k=0;k<4;k++){ $('L'+k).style.display = (k===bk)?'inline':'none'; }
  for(let k=0;k<4;k++){ if(k!==bk) continue;
    P[k].forEach((p,i)=>setC(`a${k}_${i}`, p.x+Math.sin(t*p.fx*2+p.ph)*p.ax, p.y+Math.cos(t*p.fy*2+p.ph)*p.ay, p.r*(1+0.16*pb)));
    Q[k].forEach((p,i)=>setC(`b${k}_${i}`, p.x+Math.cos(t*p.fx*2+p.ph)*p.ax, p.y+Math.sin(t*p.fy*2+p.ph)*p.ay, p.r*(1+0.12*pb)));
  }
  // drop: droplets burst out of the centre on the ink stage
  if(bk===2){ const dt=t-D; DR.forEach((d,i)=>{ const u=E.out3(clamp(dt/0.9)); setC(`d2_${i}`,540+Math.cos(d.a)*d.v*u,900+Math.sin(d.a)*d.v*u*1.2+dt*dt*300,d.r*(1-0.6*clamp(dt/1.6))*(dt<0?0:1)); });
     P[2].forEach((p,i)=>{ const u=E.out5(clamp((t-D)/0.5)); const c=$(`a2_${i}`); c.setAttribute('r',(p.r*(0.2+0.8*u)*(1+0.16*pb)).toFixed(1)); }); }
  // floods: the next colour pours in over the last 0.42 s before each cut
  [1,2,3].forEach(k=>{ const t0=B[k].start-0.42; const u=prog(t,t0,0.42); const on=t>=t0&&t<B[k].start+0.02; $('F'+k).style.display=on?'inline':'none';
    if(on) FL.forEach((f,i)=>setC(`f${k}_${i}`, f.x, f.y, E.in3(clamp(u*1.15-i*0.03))*1500*(i?0.55:1))); });
  // ---------------- type
  for(let k=0;k<4;k++) vis($('K'+(k+1)),bk===k);
  const breathe=1+0.03*pb;
  if(bk===0){ kwords($('K1'),t,-1,{gap:0}); const o=$('one1'); const s1=spring(t,1.45,2.6,0.3); tf(o,{s:(0.62+0.38*s1)*breathe, r:(1-s1)*-6}); }
  if(bk===1){ $$('.k',$('K2')).forEach((el,i)=>kwords(el,t,B[1].start+i*0.12,{mode:'stamp',gap:0.06,f:2.8,z:0.42})); tf($('n40'),{s:breathe, r:Math.sin(t*3)*2}); }
  if(bk===2){ kwords($('try'),t,D,{mode:'stamp',gap:0.1,f:3,z:0.42});
    kwords($('it1'),t,I.phone,{mode:'pop',gap:0.06}); kwords($('it2'),t,I.task,{mode:'stamp',gap:0.09}); kwords($('it3'),t,I.hour,{mode:'stamp',gap:0.09});
    tf($('try'),{s:1-0.12*prog(t,I.phone,0.3), y:-30*prog(t,I.phone,0.3)}); }
  if(bk===3){ kwords($('K4'),t,B[3].start,{mode:'up',gap:0.07}); const u=spring(t,B[3].start+0.45,2.2,0.32); tf($('thx'),{s:(0.4+0.6*u)*breathe, r:(1-u)*8}); }
  const sk=shake(t,D,0.4,28); $('stage').style.transform=`translate(${sk.x}px,${sk.y}px)`;
  if(t>=D-0.03&&t<D+0.12) blur=3;
  await flush(); return {blur};
};
"""
    st.default_sfx(cut="sfx-x-swoosh-in", b4="sfx-x-swoosh-in")
    st.add_sfx(1.45, "sfx-x-sticker-pop", -6)
    for key in ("task", "hour"):
        st.add_sfx(tl["items"][key], "sfx-x-whoosh-hit", -10)
    st.add_sfx(tl["blocks"][3]["start"] + 0.45, "sfx-x-sticker-pop", -6)
    if only == "remix":
        return st.remix()
    return st.build(css, body, js, bg=CR, only=only)


if __name__ == "__main__":
    only = ("remix" if sys.argv[1] == "remix" else [int(x) for x in sys.argv[1].split(",")]) if len(sys.argv) > 1 else None
    print(build(only))

#!/usr/bin/env python3
"""Style 3: paper cut-out stop-motion (hb-x-ta-da-funk, 105.5 bpm).

Torn construction-paper shapes with grain and layered shadows, animated "on twos" (12 steps a second) with a tiny
per-step jitter like hand-moved paper under a camera. Time passing = the paper sun arcs across the sky; the drop
RIPS the page in half to reveal the fix; the phone hops into a paper door; the sun rises with a face at the end.
"""
import math
import random
import sys
from pathlib import Path

from common import Style, words

TRACK = "hb-x-ta-da-funk"
GRAIN = (Path(__file__).resolve().parent / "assets/paper-grain.png").as_uri()


def torn(pts, rough=6, seed=0, step=18):
    """Polygon -> path with a torn/deckled edge (points resampled every `step` px and jittered)."""
    rnd = random.Random(seed)
    out = []
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        L = math.hypot(x2 - x1, y2 - y1)
        n = max(1, int(L / step))
        nx, ny = -(y2 - y1) / (L or 1), (x2 - x1) / (L or 1)
        for i in range(n):
            u = i / n
            j = rnd.uniform(-rough, rough)
            out.append((x1 + (x2 - x1) * u + nx * j, y1 + (y2 - y1) * u + ny * j))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in out) + " Z"


def rect(x, y, w, h, **k):
    return torn([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], **k)


def circle(cx, cy, r, n=48, **k):
    return torn([(cx + r * math.cos(a), cy + r * math.sin(a)) for a in [i * 2 * math.pi / n for i in range(n)]], step=999, **k)


def rrect(x, y, w, h, r, **k):
    pts = []
    for cx, cy, a0 in [(x + w - r, y + r, -90), (x + w - r, y + h - r, 0), (x + r, y + h - r, 90), (x + r, y + r, 180)]:
        for i in range(7):
            a = math.radians(a0 + i * 15)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return torn(pts, **k)


def paper(d, fill, pid=None, cls="", shadow=True):
    i = f' id="{pid}"' if pid else ""
    return (f'<g{i} class="pp {cls}"{" filter=\"url(#ds)\"" if shadow else ""}><path d="{d}" fill="{fill}"/>'
            f'<path d="{d}" fill="url(#gr)"/></g>')


def build(only=None):
    st = Style(3, "paper-cutout", TRACK)
    tl = st.tl
    PK, INK, BT, CR, PK2 = "#FF5CA8", "#2A2420", "#FFE27A", "#FFF4E0", "#FF8CC4"
    SKY1, SKY2 = "#FFE9A6", "#FFC9E0"
    # ------------------------------------------------------------------ scene art (all in 1080x1920)
    hills = (paper(torn([(-40, 1500), (220, 1380), (480, 1460), (760, 1350), (1120, 1440), (1120, 1960), (-40, 1960)], 8, 3), "#FFD24D", "hill1") +
             paper(torn([(-40, 1620), (300, 1560), (640, 1640), (900, 1570), (1120, 1620), (1120, 1960), (-40, 1960)], 8, 4), "#FFB0D2", "hill2"))
    cloud = lambda cid, x, y, s: paper(torn([(x + s * a, y + s * b) for a, b in  # noqa: E731
                                            [(0, 60), (40, 10), (110, 0), (160, 30), (220, 20), (270, 70), (250, 110), (20, 110)]], 5, hash(cid) % 99, 14), "#FFFFFF", cid)
    sun = paper(circle(0, 0, 120, rough=5, seed=7), "#FFB000", "sunb") + "".join(
        paper(torn([(150 * math.cos(a) - 18 * math.sin(a), 150 * math.sin(a) + 18 * math.cos(a)), (230 * math.cos(a), 230 * math.sin(a)),
                    (150 * math.cos(a) + 18 * math.sin(a), 150 * math.sin(a) - 18 * math.cos(a))], 3, k, 30), "#FFC93D", shadow=False)
        for k, a in enumerate([i * math.pi / 6 for i in range(12)]))
    face = (f'<g id="face" opacity="0"><path d="M-55,-10 q15,-22 30,0 M25,-10 q15,-22 30,0" stroke="{INK}" stroke-width="10" fill="none" stroke-linecap="round"/>'
            f'<path d="M-45,30 q45,45 90,0" stroke="{INK}" stroke-width="10" fill="none" stroke-linecap="round"/>'
            f'<circle cx="-70" cy="30" r="16" fill="{PK}" opacity=".7"/><circle cx="70" cy="30" r="16" fill="{PK}" opacity=".7"/></g>')
    phone = (paper(rrect(-170, -300, 340, 600, 50, rough=4, seed=11), PK, "phb") +
             paper(rrect(-140, -250, 280, 480, 26, rough=3, seed=12), CR, "phs", shadow=False) +
             "".join(paper(rrect(-118, -230 + i * 120, 236, 96, 18, rough=3, seed=20 + i), ["#FFE27A", "#BFE7FF", "#FFD0E4", "#C9F0C0", "#FFE27A", "#FFD0E4"][i % 6],
                           f"post{i}", shadow=False) for i in range(8)))
    clock = (paper(circle(0, 0, 150, rough=4, seed=31), CR, "ckb") + paper(circle(0, 0, 150, rough=0, seed=31), "none", shadow=False) +
             f'<g id="ckm"><path d="M0,0 L0,-115" stroke="{INK}" stroke-width="16" stroke-linecap="round"/></g>'
             f'<g id="ckh"><path d="M0,0 L0,-70" stroke="{PK}" stroke-width="20" stroke-linecap="round"/></g>'
             f'<circle r="16" fill="{INK}"/>')
    door = (paper(rect(-150, -330, 300, 560, rough=4, seed=41), "#B06BFF", "drf") +
            f'<g id="dleaf">{paper(rect(-130, -310, 260, 530, rough=3, seed=42), "#FFB0D2")}<circle cx="90" cy="-30" r="16" fill="{INK}"/></g>')
    book = paper(rect(-200, -140, 400, 280, rough=4, seed=51), "#7BD3FF", "bk") + paper(rect(-180, -120, 360, 240, rough=3, seed=52), CR, shadow=False) + \
        "".join(f'<path d="M-150,{-80 + i * 46} L150,{-80 + i * 46}" stroke="#B9D9F0" stroke-width="7"/>' for i in range(5))
    pencil = paper(torn([(-20, -200), (20, -200), (20, 140), (0, 200), (-20, 140)], 2, 61, 20), "#FFB000", "pc")
    hourglass = paper(torn([(-110, -170), (110, -170), (15, 0), (110, 170), (-110, 170), (-15, 0)], 3, 71, 20), "#BFE7FF", "hg") + \
        '<path id="sandT" fill="#FFB000"/><path id="sandB" fill="#FFB000"/>'
    hearts = "".join(paper(torn([(0, 40), (-55, -10), (-45, -45), (0, -25), (45, -45), (55, -10)], 3, 80 + i, 14),
                           [PK, BT, PK2, CR][i % 4], f"ht{i}") for i in range(12))
    tearL = paper(torn([(-20, -20), (560, -20), (520, 300), (580, 640), (500, 980), (590, 1300), (520, 1640), (570, 1960), (-20, 1960)], 10, 91, 16), SKY2, "tearL")
    tearR = paper(torn([(560, -20), (1100, -20), (1100, 1960), (570, 1960), (520, 1640), (590, 1300), (500, 980), (580, 640), (520, 300)], 10, 91, 16), SKY2, "tearR")
    svg = f"""<svg viewBox="0 0 1080 1920" style="position:absolute;inset:0;width:1080px;height:1920px">
 <defs><pattern id="gr" patternUnits="userSpaceOnUse" width="512" height="512"><image href="{GRAIN}" width="512" height="512"/></pattern>
  <filter id="ds" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="9" stdDeviation="7" flood-color="#5a3010" flood-opacity=".28"/></filter></defs>
 <g id="world">
  <rect width="1080" height="1920" fill="{SKY1}"/><rect id="dusk" width="1080" height="1920" fill="{SKY2}" opacity="0"/>
  <rect width="1080" height="1920" fill="url(#gr)"/>
  <g id="sun">{sun}{face}</g>
  <g id="c1">{cloud("cl1", 0, 0, 1.1)}</g><g id="c2">{cloud("cl2", 0, 0, 0.8)}</g>
  {hills}
  <g id="clock">{clock}</g>
  <g id="door">{door}</g>
  <g id="phone">{phone}</g>
  <g id="book">{book}</g><g id="pencil">{pencil}</g><g id="hglass">{hourglass}</g>
  <g id="hearts">{hearts}</g>
 </g>
 <g id="tear"><g id="tL">{tearL}</g><g id="tR">{tearR}</g></g>
</svg>"""
    css = """.em{color:#FF5CA8} .pp{transform-box:fill-box}"""
    body = f"""{svg}
<div class="txt" id="T1" style="top:150px">{words("You opened your phone / to check one thing.", em=("one",))}</div>
<div class="txt" id="T2" style="top:170px;font-size:132px">{words("40 minutes / later…", em=("40",))}</div>
<div class="txt" id="T3a" style="top:130px;font-size:112px">{words("Try this:")}</div>
<div class="txt" id="T3b" style="top:270px;font-size:78px">{words("Phone in another room.")}</div>
<div class="txt" id="T3c" style="top:370px;font-size:78px">{words("One task.", em=("one",))} &nbsp;{words("One hour.", em=("one",))}</div>
<div class="txt" id="T4" style="top:170px;font-size:104px">{words("Your future self / says thanks.", em=("thanks",))}</div>
"""
    js = """
const B=TL.blocks, I=TL.items, beat=TL.beat, D=TL.drop;
const FPSA=12; const step=t=>Math.floor(t*FPSA)/FPSA;
function jit(id,k,amp=2.2){ let s=(k*9301+id.length*49297)%233280; const r1=s/233280; s=(s*9301+49297)%233280; const r2=s/233280; s=(s*9301+49297)%233280;
  return {x:(r1-0.5)*2*amp, y:(r2-0.5)*2*amp, r:(s/233280-0.5)*1.2}; }
function put(id,x,y,s=1,r=0,on=true,tq=0){ const e=$(id); if(!e) return; e.style.display=on?'inline':'none'; if(!on) return;
  const j=jit(id,Math.floor(tq*FPSA)); e.setAttribute('transform',`translate(${(x+j.x).toFixed(1)},${(y+j.y).toFixed(1)}) rotate(${(r+j.r).toFixed(2)}) scale(${s.toFixed(3)})`); }
window.seek = async (t) => {
  const tq=step(t); const bk=blockAt(t); let blur=1;
  const pb=Math.exp(-sinceBeat(tq)/0.12);
  // sky + sun path: morning (B1) -> sun arcs over (B2, time passing) -> new day (B4)
  let sa; if(bk<=1){ const u=bk===0?0.08*tq/B[1].start:0.08+0.84*E.inOut(prog(tq,B[1].start,B[2].start-B[1].start)); sa=u; } else sa=0.12;
  const sx=lerp(140,940,sa), sy=560-Math.sin(sa*Math.PI)*260;
  let sunS=1+0.05*pb;
  if(bk===3){ const u=spring(tq,B[3].start,2,0.45); put('sun',540,lerp(1500,820,u),1.5*(0.8+0.2*u)+0.05*pb,Math.sin(tq*3)*6,true,tq); $('face').setAttribute('opacity',1); }
  else { put('sun',sx,sy,sunS*0.8,tq*30,bk!==2,tq); $('face').setAttribute('opacity',0); }
  $('dusk').setAttribute('opacity', bk===1? 0.85*Math.sin(Math.PI*prog(tq,B[1].start,B[2].start-B[1].start)) : 0);
  put('c1', 80+((tq*60)%1300)-200, bk===3?1180:720, 1, 0, true, tq); put('c2', 1000-((tq*45)%1300), bk===3?1300:900, 1, 0, true, tq);
  // B1: phone with posts scrolling (in steps); bounces on the beat
  const phOn = t<I.phone+1.0;
  let phx=540, phy=1180, phr=-4, phs=1+0.04*pb;
  if(bk===1){ phr=8*Math.sin(tq*6); phs=0.9; phy=1220; }
  if(bk>=2){ // phone hops to the door in 3 hops, then vanishes behind it
    const hu=prog(tq,I.phone+0.05,0.8); const hop=Math.abs(Math.sin(hu*Math.PI*3))*160;
    phx=lerp(380,830,hu); phy=1250-hop; phs=0.62*(1-0.5*prog(tq,I.phone+0.7,0.2)); phr=hu*20; }
  put('phone',phx,phy,phs,phr,phOn && !(bk===2 && tq<D+0.08),tq);
  for(let i=0;i<8;i++){ const y=((i*120 - tq*240) % 960 + 960) % 960 - 240; const e=$('post'+i); e.style.display=(y>-232&&y<134)?'inline':'none'; e.setAttribute('transform',`translate(0,${(y-(-230+i*120)).toFixed(0)})`); }
  // B2: clock pops in, hands jump
  const ck=bk===1; const cu=spring(tq,B[1].start,3,0.4); put('clock',800,1040,ck?0.7*cu+0.001:0.001,0,ck,tq);
  $('ckm').setAttribute('transform',`rotate(${Math.floor(tq*12)*30})`); $('ckh').setAttribute('transform',`rotate(${Math.floor(tq*12)*2.5})`);
  // B3: the rip, then door, book, pencil, hourglass
  const ru=E.inOut(prog(t,D-0.02,0.42)); const rip = t>=D-0.02 && ru<1;
  $('tear').style.display=rip?'inline':'none'; if(rip){ $('tL').setAttribute('transform',`translate(${-700*ru},${120*ru}) rotate(${-8*ru})`); $('tR').setAttribute('transform',`translate(${700*ru},${-80*ru}) rotate(${7*ru})`); if(ru>0.1&&ru<0.9) blur=3; }
  const dOn=bk===2; put('door',860,1240,dOn?0.75*spring(tq,I.phone,3,0.42)+0.001:0.001,0,dOn,tq);
  const closed=prog(tq,I.phone+0.7,0.17)*(1-0) ; $('dleaf').setAttribute('transform',`scale(${dOn? (tq<I.phone+0.2?1: 1-0.8*Math.sin(Math.PI*Math.min(1,(tq-I.phone-0.2)/0.7))) :1},1)`);
  const bOn=bk===2&&tq>=I.task; put('book',360,1260,bOn?spring(tq,I.task,3,0.42)*0.95+0.001:0.001,-6,bOn,tq);
  put('pencil',600,1250,bOn?spring(tq,I.task+beat/2,3,0.42)*0.8+0.001:0.001,30,bOn&&tq>=I.task+beat/2,tq);
  const hOn=bk===2&&tq>=I.hour; put('hglass',820,1150,hOn?spring(tq,I.hour,3,0.42)*0.9+0.001:0.001,0,hOn,tq);
  if(hOn){ const su=prog(tq,I.hour,B[3].start-I.hour); $('sandT').setAttribute('d',`M${-80*(1-su)},${-150+150*su} L${80*(1-su)},${-150+150*su} L0,-5 Z`); $('sandB').setAttribute('d',`M${-90*su},150 L${90*su},150 L0,${150-120*su} Z`); }
  // B4 hearts rain (stop-motion)
  for(let i=0;i<12;i++){ const t0=B[3].start+0.3+i*beat/3; const on=bk===3&&tq>=t0; const fy=(tq-t0)*520; put('ht'+i,90+((i*373)%900),620+fy,1.1+0.3*(i%3),Math.sin(tq*5+i)*25,on,tq); }
  // hills breathe a little on the beat
  put('hill1',0,-10*pb,1,0,true,tq); put('hill2',0,-6*pb,1,0,true,tq);
  // text (also on twos, with jitter)
  const jt=jit('txt',Math.floor(tq*FPSA),1.5);
  ['T1','T2','T3a','T3b','T3c','T4'].forEach(id=>{ $(id).style.translate=`${jt.x}px ${jt.y}px`; });
  vis($('T1'),bk===0); kwords($('T1'),tq,-1,{});
  vis($('T2'),bk===1); if(bk===1) kwords($('T2'),tq,B[1].start,{mode:'drop',gap:0.08,f:2.8,z:0.42});
  vis($('T3a'),bk===2); if(bk===2) kwords($('T3a'),tq,D,{mode:'stamp',gap:0.1,f:3,z:0.42});
  vis($('T3b'),bk===2&&t>=I.phone); if(bk===2) kwords($('T3b'),tq,I.phone,{mode:'pop',gap:0.06});
  vis($('T3c'),bk===2&&t>=I.task); if(bk===2){ $$('.w',$('T3c')).forEach((w,i)=>{ const s0=(i<2?I.task:I.hour)+(i%2)*0.07; const u2=spring(tq,s0,2.6,0.4);
      w.style.opacity=tq<s0?0:1; w.style.transform=`translateY(${(1-u2)*50}px) scale(${0.5+0.5*u2})`; }); }
  vis($('T4'),bk===3); if(bk===3) kwords($('T4'),tq,B[3].start,{mode:'pop',gap:0.07});
  const sk=shake(tq,D,0.35,20); $('stage').style.transform=`translate(${sk.x}px,${sk.y}px)`;
  await flush(); return {blur};
};
"""
    st.default_sfx(cut="sfx-x-paper-slap", b4="sfx-x-swoosh-in")
    B, I, beat, D = tl["blocks"], tl["items"], tl["beat"], tl["drop"]
    st.add_sfx(D - 0.02, "sfx-x-paper-slap", -2)          # the rip
    st.add_sfx(B[1]["start"] + 0.05, "sfx-x-tick-tock", -11)
    for k in range(3):
        st.add_sfx(I["phone"] + 0.05 + k * 0.8 / 3, "sfx-x-sticker-pop", -10)
    st.add_sfx(I["phone"] + 0.75, "sfx-x-paper-slap", -6)
    st.add_sfx(I["task"], "sfx-x-paper-slap", -8)
    st.add_sfx(I["task"] + beat / 2, "sfx-x-paper-slap", -10)
    st.add_sfx(I["hour"], "sfx-x-paper-slap", -8)
    if only == "remix":
        return st.remix()
    return st.build(css, body, js, bg="#FFE9A6", only=only)


if __name__ == "__main__":
    only = ("remix" if sys.argv[1] == "remix" else [int(x) for x in sys.argv[1].split(",")]) if len(sys.argv) > 1 else None
    print(build(only))

#!/usr/bin/env python3
"""Style 1: storybook pages with painted plates in parallax (lh-x-phone-down, 110 bpm).

FALLBACK BUILD: Canva image generation was out of credits (Oct 16), so the plates are bright Pexels frames turned
into gouache-style paintings (tools/paint.py: edge-preserving paint, soft colour flattening, ink on strong edges,
warm grade) with the subject cut out (GrabCut) so it floats over an inpainted background = real parallax.
Swap in generated plates (same file names: <block>-bg.png / -fg.png) when credits return.

Each block is a page: serif type with a pink drop cap, a deckle-edged plate, a page number. Cuts are 3D page turns.
"""
import sys
from pathlib import Path

from common import CACHE, Style, words

TRACK = "lh-x-phone-down"
P = CACHE / "s1"
GRAIN = (Path(__file__).resolve().parent / "assets/paper-grain.png").as_uri()
# plate key -> vertical offset into the 1080x1920 painting so the subject sits in the 960x1140 window
PLATES = {"b1": 600, "b2": 260, "b3": 640, "b3m": 620, "b4": 520}


def deckle(w, h, seed=1, j=7, step=22):
    import random
    r = random.Random(seed)
    pts = []
    for x in range(0, w + 1, step):
        pts.append((x, r.uniform(0, j)))
    for y in range(0, h + 1, step):
        pts.append((w - r.uniform(0, j), y))
    for x in range(w, -1, -step):
        pts.append((x, h - r.uniform(0, j)))
    for y in range(h, -1, -step):
        pts.append((r.uniform(0, j), y))
    return "polygon(" + ",".join(f"{x:.0f}px {y:.0f}px" for x, y in pts) + ")"


def build(only=None):
    st = Style(1, "storybook", TRACK)
    tl = st.tl
    PK, INK, BT, CR = "#FF5CA8", "#2A1F22", "#FFE27A", "#FFF4E0"

    def plate(pid, key, seed):
        oy = PLATES[key]
        return (f'<div class="plate" id="{pid}" style="clip-path:{deckle(960, 1140, seed)}">'
                f'<img class="pbg" id="{pid}_bg" src="{(P / f"{key}-bg.png").as_uri()}" style="top:{-oy}px">'
                f'<img class="pfg" id="{pid}_fg" src="{(P / f"{key}-fg.png").as_uri()}" style="top:{-oy}px">'
                f'<div class="glow"></div></div>')

    def page(k, text_html, plates, num):
        return (f'<div class="page" id="pg{k}"><div class="back"></div><div class="grain"></div><div class="tx">{text_html}</div>{plates}'
                f'<div class="num">— {num} —</div><div class="curl"></div></div>')

    dc = lambda letter: f'<span class="dc">{letter}</span>'  # noqa: E731
    pages = (
        page(0, f'<div class="ln" id="T1">{dc("Y")}{words("ou opened your phone / to check one thing.", em=("one",))}</div>', plate("pl0", "b1", 1), 1) +
        page(1, f'<div class="ln big" id="T2"><span class="n40">{words("40")}</span> {words("minutes / later…")}</div>', plate("pl1", "b2", 2), 2) +
        page(2, f'<div class="ln" id="T3a">{dc("T")}{words("ry this:")}</div><div class="ln sm" id="T3b">{words("Phone in another room.")}</div>'
                f'<div class="ln sm" id="T3c">{words("One task.", em=("one",))} {words("One hour.", em=("one",))}</div>',
             plate("pl2", "b3", 3) + plate("pl2b", "b3m", 4), 3) +
        page(3, f'<div class="ln" id="T4">{dc("Y")}{words("our future self / says thanks.", em=("thanks",))}</div>', plate("pl3", "b4", 5), 4)
    )
    dust = "".join(f'<div class="mote" id="m{i}"></div>' for i in range(26))
    css = f"""
    #book{{position:absolute;inset:0;perspective:2600px;perspective-origin:0% 50%}}
    .page{{position:absolute;inset:0;background:linear-gradient(90deg,#F3E2C4 0,{CR} 6%,{CR} 94%,#F6E7CC 100%);transform-origin:0 50%;
           backface-visibility:hidden;box-shadow:inset 18px 0 30px rgba(120,80,30,.12)}}
    .back{{position:absolute;inset:0;transform:rotateY(180deg) translateZ(1px);backface-visibility:hidden;
           background:linear-gradient(270deg,#EAD7B5 0,#FFF4E0 12%,#F8EAD0 100%)}}
    .page{{transform-style:preserve-3d}} .page > :not(.back){{backface-visibility:hidden}}
    .grain{{position:absolute;inset:0;background:url('{GRAIN}') 0 0/512px 512px;opacity:.9;will-change:transform}}
    .tx{{position:absolute;left:70px;right:70px;top:120px;height:430px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}}
    .ln{{font:400 88px/1.06 'DM Serif Display';color:{INK};letter-spacing:-0.01em;text-shadow:0 3px 10px rgba(120,80,30,.12)}}
    .ln.sm{{font-size:70px;margin-top:10px}} .ln.big{{font-size:110px}}
    .n40{{font:400 200px/0.9 'DM Serif Display';color:{PK}}}
    .dc{{font:400 170px/0.8 'DM Serif Display';color:{PK};float:none;display:inline-block;vertical-align:-0.18em;margin-right:-6px}}
    .em{{font-family:'Instrument Serif';font-style:italic;color:{PK};font-size:1.12em}}
    .plate{{position:absolute;left:60px;top:590px;width:960px;height:1140px;overflow:hidden;background:#eee}}
    .plate img{{position:absolute;left:-60px;width:1080px;height:1920px;will-change:transform;filter:brightness(1.12) saturate(1.35) contrast(1.06)}}
    .glow{{position:absolute;inset:0;background:radial-gradient(ellipse at 70% 10%,rgba(255,236,160,.35),transparent 55%),
           radial-gradient(ellipse at 50% 120%,rgba(255,92,168,.12),transparent 60%);mix-blend-mode:screen}}
    .num{{position:absolute;left:0;right:0;top:1770px;text-align:center;font:400 40px/1 'DM Serif Display';color:#9a7f63}}
    .curl{{position:absolute;right:0;bottom:0;width:120px;height:120px;background:linear-gradient(135deg,transparent 50%,#EAD7B5 50%,#FFF8EA 75%);
           box-shadow:-6px -6px 14px rgba(120,80,30,.12)}}
    .turnsh{{position:absolute;inset:0;pointer-events:none;background:linear-gradient(90deg,rgba(60,30,10,.0),rgba(60,30,10,.35));opacity:0}}
    .mote{{position:absolute;width:12px;height:12px;border-radius:50%;background:radial-gradient(circle,#FFF6C9,rgba(255,226,122,0) 70%)}}
    """
    body = f'<div id="book">{pages}</div><div id="motes">{dust}</div>'
    js = """
const B=TL.blocks, I=TL.items, beat=TL.beat, D=TL.drop;
let _s=21; const rnd=()=>{ _s=(_s*16807)%2147483647; return (_s-1)/2147483646; };
const MT=[...Array(26)].map(()=>({x:80+rnd()*920,y:620+rnd()*1080,v:10+rnd()*30,ph:rnd()*6.28,s:0.6+rnd()*1.6}));
const TURN=0.5;
function parallax(pid,lt,dur,dir=1){ const u=clamp(lt/dur); const pb=Math.exp(-sinceBeat(TT)/0.12);
  tf($(pid+'_bg'),{x:-14*u*dir, y:8*u, s:1.12-0.05*u});
  tf($(pid+'_fg'),{x:26*u*dir, y:-14*u, s:(1.0+0.07*u)*(1+0.012*pb)}); }
let TT=0;
window.seek = async (t) => {
  TT=t; const bk=blockAt(t); let blur=1;
  // pages: page k turns away over the last TURN s before block k+1
  for(let k=0;k<4;k++){ const pg=$('pg'+k); pg.style.zIndex=10-k;
    let ang=0; if(k<3){ const t0=B[k+1].start-TURN*0.8; const u=prog(t,t0,TURN); ang=-180*E.inOut(u); if(u>0.1&&u<0.9) blur=3; }
    pg.style.transform=`rotateY(${ang}deg)`;
    const turning=j=>j<3 && t>=B[j+1].start-TURN*0.8 && t<B[j+1].start+TURN*0.2+0.02;
    const show = k===bk || (k===bk+1 && turning(bk)) || (k===bk-1 && turning(k));
    pg.style.display = show?'block':'none';
  }
  // plates
  parallax('pl0',t,B[1].start); parallax('pl1',t-B[1].start,B[2].start-B[1].start,-1);
  parallax('pl2',t-D,I.task-D); parallax('pl2b',t-I.task,B[3].start-I.task,-1); parallax('pl3',t-B[3].start,TL.dur-B[3].start);
  const sw=prog(t,I.task-0.15,0.3); $('pl2b').style.opacity=sw; $('pl2b').style.clipPath=sw<1?`circle(${sw*80}% at 50% 60%)`:'';
  // drop: a tiny camera bump on the new page
  const sk=shake(t,D,0.3,14); $('book').style.transform=`translate(${sk.x}px,${sk.y}px)`;
  // text
  if(bk===0) kwords($('T1'),t,-1,{});
  kwords($('T2'),t,B[1].start-0.1,{mode:'up',gap:0.08});
  kwords($('T3a'),t,D,{mode:'up',gap:0.08}); kwords($('T3b'),t,I.phone,{mode:'up',gap:0.06});
  $$('.w',$('T3c')).forEach((w,i)=>{ const s0=(i<2?I.task:I.hour)+(i%2)*0.07; const u=spring(t,s0,2.6,0.45);
      w.style.opacity=t<s0?0:prog(t,s0,0.12); w.style.transform=`translateY(${(1-u)*40}px)`; });
  $('T3c').style.visibility=t>=I.task-0.5?'visible':'hidden';
  kwords($('T4'),t,B[3].start-0.1,{mode:'up',gap:0.08});
  // drop caps bloom in
  // dust motes drift in light
  MT.forEach((m,i)=>{ const e=$('m'+i); const y=m.y-((t*m.v)%300); e.style.transform=`translate(${m.x+Math.sin(t+m.ph)*20}px,${y}px) scale(${m.s})`;
    e.style.opacity=0.35+0.35*Math.sin(t*2+m.ph); });
  await flush(); return {blur};
};
"""
    st.default_sfx(cut="sfx-x-swoosh-in", b4="sfx-x-swoosh-in")
    for k in (1, 2, 3):
        st.add_sfx(tl["blocks"][k]["start"] - 0.4, "sfx-x-paper-slap", -12)
    st.add_sfx(tl["items"]["task"] - 0.15, "sfx-x-swoosh-in", -10)
    if only == "remix":
        return st.remix()
    return st.build(css, body, js, bg="#3a2a20", only=only)


if __name__ == "__main__":
    only = ("remix" if sys.argv[1] == "remix" else [int(x) for x in sys.argv[1].split(",")]) if len(sys.argv) > 1 else None
    print(build(only))

#!/usr/bin/env python3
"""Style 7: scrapbook collage - polaroids of real footage, washi tape, die-cut stickers, handwriting
(lf-x-sunny-bounce, 112.3 bpm).

One big paper page (2400 x 4000) holds four spreads; the camera travels a path across it, gliding and tilting
to the next spread on each cut. Stickers slap on with a peel-and-press on the beat, tape lands with a paper slap.
"""
import sys

from common import CACHE, Style, fluent, words

TRACK = "lf-x-sunny-bounce"


def build(only=None):
    st = Style(7, "scrapbook", TRACK)
    tl = st.tl
    PK, INK, BT, CR = "#FF5CA8", "#141414", "#FFE27A", "#FFF4E0"
    n = lambda k: len(list((CACHE / f"s2_{k}").glob("*.jpg")))  # noqa: E731

    def polaroid(pid, clip, x, y, w, h, rot, cap):
        return (f'<div class="pol" id="{pid}" style="left:{x}px;top:{y}px;width:{w + 44}px;--r:{rot}deg">'
                f'<div class="ph" style="width:{w}px;height:{h}px"><img id="v_{pid}" data-clip="{(CACHE / f"s2_{clip}").as_uri()}" data-n="{n(clip)}"></div>'
                f'<div class="cap">{cap}</div></div>')

    def tape(tid, x, y, w, rot, col=PK):
        return f'<div class="tape" id="{tid}" style="left:{x}px;top:{y}px;width:{w}px;--r:{rot}deg;--c:{col}"></div>'

    def stk(sid, icon, x, y, size, rot):
        return f'<img class="stk" id="{sid}" src="{fluent(icon)}" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;--r:{rot}deg">'

    page = (
        # spread 1 around (540, 1000)
        polaroid("p1", "b1", 250, 700, 560, 760, -4, "just checking…") + tape("t1", 420, 670, 240, -8) +
        stk("s1a", "bell", 120, 680, 190, -14) + stk("s1b", "speech_balloon", 760, 760, 200, 10) +
        stk("s1c", "eyes", 700, 1330, 180, -8) + stk("s1d", "sparkles", 90, 1300, 150, 0) + stk("s1e", "vibration_mode", 820, 1100, 170, 14) +
        # spread 2 around (1700, 1500)
        polaroid("p2", "b2", 1430, 1180, 560, 760, 5, "uh oh.") + tape("t2", 1580, 1150, 260, 6, BT) +
        stk("s2a", "alarm_clock", 1270, 1160, 230, -12) + stk("s2b", "melting_face", 1910, 1700, 200, 12) + stk("s2c", "hourglass_done", 1300, 1820, 170, -6) +
        # spread 3 around (900, 2600)
        polaroid("p3", "b3c", 560, 2370, 520, 700, -3, "my one task") + tape("t3", 690, 2340, 240, -4, "#7BD3FF") +
        stk("s3a", "no_mobile_phones", 1080, 2330, 230, 10) + stk("s3b", "notebook_with_decorative_cover", 1100, 2640, 200, -8) +
        stk("s3c", "hourglass_not_done", 1110, 2900, 190, 8) + stk("s3d", "door", 420, 2330, 190, -10) +
        # spread 4 around (1800, 3300)
        polaroid("p4", "b4", 1480, 3020, 600, 800, 3, "future me ♥") + tape("t4", 1650, 2990, 280, -5) + tape("t4b", 2000, 3700, 200, 40, BT) +
        stk("s4a", "sun", 1330, 2980, 240, -10) + stk("s4b", "smiling_face_with_hearts", 2010, 3150, 220, 12) +
        stk("s4c", "sparkling_heart", 1380, 3640, 180, -8) + stk("s4d", "trophy", 2050, 3500, 170, 8) + stk("s4e", "rainbow", 1880, 2920, 200, 0)
    )
    doodles = f"""<svg class="doo" viewBox="0 0 2400 4000" style="position:absolute;left:0;top:0;width:2400px;height:4000px">
      <path id="dz1" d="M300,1560 C 500,1640 700,1620 860,1540" stroke="{PK}" stroke-width="10" fill="none" stroke-linecap="round" pathLength="1"/>
      <path id="dz2" d="M1000,1550 C 1200,1520 1300,1450 1380,1360" stroke="{INK}" stroke-width="7" stroke-dasharray="14 16" fill="none" stroke-linecap="round"/>
      <path id="dz3" d="M1450,2050 C 1300,2200 1150,2250 1020,2300" stroke="{INK}" stroke-width="7" stroke-dasharray="14 16" fill="none" stroke-linecap="round"/>
      <path id="dz4" d="M1130,3150 C 1300,3200 1400,3150 1460,3080" stroke="{INK}" stroke-width="7" stroke-dasharray="14 16" fill="none" stroke-linecap="round"/>
    </svg>"""
    GRAIN = (__import__("pathlib").Path(__file__).resolve().parent / "assets/paper-grain.png").as_uri()
    css = f"""
    #cam{{position:absolute;left:0;top:0;width:2400px;height:4000px;transform-origin:0 0}}
    #paper{{position:absolute;inset:-500px;background:
        radial-gradient(circle,rgba(20,20,20,.10) 2px,transparent 2.5px) 0 0/44px 44px,
        linear-gradient(135deg,#FFF6E4,#FFEFD2 50%,#FFF3DE)}}
    #grain{{position:absolute;inset:-500px;background:url('{GRAIN}') 0 0/512px 512px;will-change:transform}}
    .pol{{position:absolute;background:#fff;padding:22px 22px 0;box-shadow:0 26px 40px rgba(90,50,10,.22),0 6px 10px rgba(90,50,10,.12);
         transform:rotate(var(--r));transform-origin:50% 50%}}
    .ph{{overflow:hidden;background:#ddd}} .ph img{{width:100%;height:100%;object-fit:cover}}
    .cap{{font:400 64px/1 'Caveat Brush';color:{INK};padding:20px 6px 26px}}
    .tape{{position:absolute;height:74px;background:repeating-linear-gradient(45deg,var(--c) 0 16px,rgba(255,255,255,.55) 16px 30px);opacity:.82;
         transform:rotate(var(--r));clip-path:polygon(0 8%,4% 0,8% 10%,12% 0,100% 0,96% 12%,100% 25%,96% 40%,100% 55%,96% 70%,100% 85%,96% 100%,0 100%,4% 85%,0 70%,4% 55%,0 40%,4% 25%);
         box-shadow:0 4px 8px rgba(0,0,0,.08)}}
    .stk{{position:absolute;transform:rotate(var(--r));
         filter:drop-shadow(5px 0 0 #fff) drop-shadow(-5px 0 0 #fff) drop-shadow(0 5px 0 #fff) drop-shadow(0 -5px 0 #fff) drop-shadow(0 12px 12px rgba(80,40,10,.25))}}
    .hw{{position:absolute;font:400 92px/1 'Caveat Brush';color:{PK};white-space:nowrap}}
    .em{{color:{PK}}}
    """
    body = f"""
<div id="cam"><div id="paper"></div>
 <div id="grain"></div>
 {doodles}{page}
 <div class="hw" id="h1" style="left:560px;top:1560px;transform:rotate(-6deg)">just 1 thing!</div>
 <div class="hw" id="h3" style="left:1120px;top:3120px;transform:rotate(-4deg);color:{INK}">60 min ✓</div>
</div>
<div class="txt" id="T1" style="top:150px">{words("You opened your phone / to check one thing.", em=("one",))}</div>
<div class="txt" id="T2" style="top:170px;font-size:132px">{words("40 minutes / later…", em=("40",))}</div>
<div class="txt" id="T3a" style="top:130px;font-size:112px">{words("Try this:")}</div>
<div class="txt" id="T3b" style="top:270px;font-size:78px">{words("Phone in another room.")}</div>
<div class="txt" id="T3c" style="top:370px;font-size:78px">{words("One task.", em=("one",))} &nbsp;{words("One hour.", em=("one",))}</div>
<div class="txt" id="T4" style="top:170px;font-size:104px">{words("Your future self / says thanks.", em=("thanks",))}</div>
"""
    js = """
const B=TL.blocks, I=TL.items, beat=TL.beat, D=TL.drop;
// camera spots (page coords that sit at screen (540, 1080)) and a tilt per spread
const SP=[[540,1130,-2],[1700,1580,2],[860,2640,-1.5],[1790,3380,1.5]];
const PB={p1:[0,'b1'],p2:[1,'b2'],p3:[2,'b3c'],p4:[3,'b4']};
const bb=t0=>TL.beats.find(b=>b>=t0-1e-6)||t0;
// sticker / tape appear times
const AT={t1:0, s1a:-1, s1b:-1, s1c:bb(1.4), s1d:bb(1.4)+beat, s1e:bb(1.4)+2*beat, h1:bb(1.4)+3*beat,
  t2:B[1].start+0.15, s2a:B[1].start+0.25, s2b:bb(B[1].start+0.6), s2c:bb(B[1].start+0.6)+beat/2,
  t3:D+0.1, s3d:I.phone, s3a:I.phone+beat/2, s3b:I.task, s3c:I.hour, h3:I.hour+beat,
  t4:B[3].start+0.15, s4a:B[3].start+0.3, s4e:bb(B[3].start+0.5), s4b:bb(B[3].start+0.5)+beat/2, s4c:bb(B[3].start+0.5)+beat, s4d:bb(B[3].start+0.5)+1.5*beat, t4b:bb(B[3].start+0.5)+2*beat};
window.seek = async (t) => {
  const bk=blockAt(t); let blur=1;
  // camera: hold on a spread with a slow drift, glide to the next one across each cut (0.5 s, expo)
  let cx,cy,cr; const tr=0.5;
  const k=bk; const nx=Math.min(3,k+1); const tNext=k<3?B[k+1].start:99;
  const u=E.inOut(prog(t,tNext-tr*0.6,tr));
  cx=lerp(SP[k][0],SP[nx][0],u); cy=lerp(SP[k][1],SP[nx][1],u); cr=lerp(SP[k][2],SP[nx][2],u);
  const drift=(t-B[k].start); cx+=Math.sin(drift*0.9)*18; cy+=drift*10;
  let sc=1+0.02*Math.exp(-sinceBeat(t)/0.12) - 0.18*Math.sin(Math.PI*u);
  if(u>0.08&&u<0.92) blur=3;
  const sk=shake(t,D,0.35,24);
  $('cam').style.transform=`translate(540px,1080px) rotate(${cr}deg) scale(${sc}) translate(${-cx+sk.x}px,${-cy+sk.y}px)`;
  // polaroids: footage plays, polaroid drops in when its spread arrives
  for(const pid in PB){ const [b,clip]=PB[pid]; const t0=B[b].start-(b?0.3:1); foot($('v_'+pid),Math.max(0,t-B[b].start)*0.9);
    const p=$(pid); const s=spring(t,t0,2.4,0.45); p.style.transform=`rotate(var(--r)) scale(${b?0.6+0.4*s:1})`; p.style.opacity=b?(t<t0?0:1):1; }
  // stickers + tape: slap on with a peel overshoot
  for(const id in AT){ const e=$(id); const t0=AT[id]; if(t0<0){ e.style.opacity=1; continue; }
    if(t<t0){ e.style.opacity=0; continue; } const s=spring(t,t0,3.4,0.42); e.style.opacity=1;
    const tape=id[0]==='t'; e.style.transform=`rotate(var(--r)) scale(${tape?1:0.3+0.7*s}) ${tape?`scaleX(${0.2+0.8*E.out3(prog(t,t0,0.18))})`:''} rotate(${(1-s)*-18}deg)`;
    if(id[0]==='h'){ e.style.clipPath=`inset(0 ${100-100*E.out3(prog(t,t0,0.45))}% 0 0)`; e.style.transform=e.id==='h1'?'rotate(-6deg)':'rotate(-4deg)'; } }
  // idle wiggle on the beat for stickers that are on
  const pb=Math.exp(-sinceBeat(t)/0.1);
  $$('.stk').forEach(e=>{ if(+e.style.opacity>0) e.style.transform+=` scale(${1+0.05*pb})`; });
  $('dz1').style.strokeDasharray='1 1'; $('dz1').style.strokeDashoffset=1-E.out3(prog(t,1.0,0.5));
  // spread-1 notes would sit behind later headlines: clear them once the camera leaves
  if(t>B[1].start+0.1){ $('h1').style.opacity=0; $('dz1').style.opacity=0; } else { $('dz1').style.opacity=1; }
  // text
  vis($('T1'),bk===0); kwords($('T1'),t,-1,{}); tf($('T1'),{y:bk===0&&t>tNext-0.3?-60*u:0, o:bk===0?1-u:0});
  vis($('T2'),bk===1); if(bk===1) kwords($('T2'),t,B[1].start,{mode:'drop',gap:0.08,f:2.8,z:0.42});
  vis($('T3a'),bk===2); if(bk===2) kwords($('T3a'),t,D,{mode:'stamp',gap:0.1,f:3,z:0.42});
  vis($('T3b'),bk===2&&t>=I.phone); if(bk===2) kwords($('T3b'),t,I.phone,{mode:'pop',gap:0.06});
  vis($('T3c'),bk===2&&t>=I.task); if(bk===2){ $$('.w',$('T3c')).forEach((w,i)=>{ const s0=(i<2?I.task:I.hour)+(i%2)*0.07; const u2=spring(t,s0,2.6,0.4);
      w.style.opacity=t<s0?0:prog(t,s0,0.1); w.style.transform=`translateY(${(1-u2)*50}px) scale(${0.5+0.5*u2})`; }); }
  vis($('T4'),bk===3); if(bk===3) kwords($('T4'),t,B[3].start,{mode:'pop',gap:0.07});
  if(t>=D-0.03&&t<D+0.1) blur=3;
  await flush(); return {blur};
};
"""
    st.default_sfx(cut="sfx-x-swoosh-in", b4="sfx-x-swoosh-in")
    beats = tl["beats"]
    bb = lambda t0: min([b for b in beats if b >= t0 - 1e-6] or [t0])  # noqa: E731
    B, I, beat, D = tl["blocks"], tl["items"], tl["beat"], tl["drop"]
    pops = [bb(1.4), bb(1.4) + beat, bb(1.4) + 2 * beat, B[1]["start"] + 0.25, bb(B[1]["start"] + 0.6), bb(B[1]["start"] + 0.6) + beat / 2,
            I["phone"], I["phone"] + beat / 2, I["task"], I["hour"], B[3]["start"] + 0.3] + [bb(B[3]["start"] + 0.5) + k * beat / 2 for k in range(4)]
    for k, t0 in enumerate(pops):
        st.add_sfx(t0, "sfx-x-sticker-pop", -8 if k % 2 else -10)
    for t0 in (B[1]["start"] + 0.15, D + 0.1, B[3]["start"] + 0.15):
        st.add_sfx(t0, "sfx-x-paper-slap", -8)
    st.add_sfx(1.0, "sfx-x-camera-shutter", -10)
    if only == "remix":
        return st.remix()
    return st.build(css, body, js, bg="#FFF3DE", only=only)


if __name__ == "__main__":
    only = ("remix" if sys.argv[1] == "remix" else [int(x) for x in sys.argv[1].split(",")]) if len(sys.argv) > 1 else None
    print(build(only))

#!/usr/bin/env python3
"""Style 6: a 3D-ish desk where objects drop in on the beat, bounce, squash and cast shadows (ff-x-big-reveal, 95.7 bpm).

A desk plane in perspective under a soft pink wall. Every object (3D renders, studio/styles/assets/fluent3d) falls
on a beat with a real bounce curve, squash on impact and a contact shadow that tightens as it lands. On the drop a
swipe clears the desk; the fix is built object by object. The camera drifts along a path and punches on impacts.
"""
import sys

from common import Style, fluent, words

TRACK = "ff-x-big-reveal"


def build(only=None):
    st = Style(6, "desk-drop", TRACK)
    tl = st.tl
    B, I, beat, D = tl["blocks"], tl["items"], tl["beat"], tl["drop"]
    beats = tl["beats"]
    bb = lambda t0: min([b for b in beats if b >= t0 - 1e-6] or [t0])  # noqa: E731  next beat at/after t0
    # (id, icon, u (-1..1 across), v (0 far..1 near), size, t_in, t_out, out_mode)
    objs = [
        ("phone", "mobile_phone", 0.0, 0.62, 1.25, -1.0, I["phone"] + 0.1, "lift"),
        ("bell", "bell", -0.72, 0.30, 0.8, bb(0.6), D, "sweep"),
        ("chat", "speech_balloon", 0.72, 0.22, 0.85, bb(0.6) + beat, D, "sweep"),
        ("eyes", "eyes", -0.75, 0.85, 0.8, bb(0.6) + 2 * beat, D, "sweep"),
        ("vib", "vibration_mode", 0.72, 0.80, 0.8, bb(0.6) + 3 * beat, D, "sweep"),
        ("star", "star-struck", -0.35, 0.02, 0.7, bb(0.6) + 4 * beat, D, "sweep"),
        ("clock", "alarm_clock", 0.36, 0.08, 1.15, B[1]["start"], D, "sweep"),
        ("melt", "melting_face", -0.5, 0.55, 0.9, bb(B[1]["start"] + beat * 0.9), D, "sweep"),
        ("door", "door", 0.78, 0.05, 1.25, I["phone"] - 0.05, B[3]["start"], "sweep"),
        ("book", "notebook_with_decorative_cover", -0.25, 0.55, 1.15, I["task"], B[3]["start"], "stay"),
        ("pen", "pencil", 0.3, 0.68, 0.85, bb(I["task"] + 0.3), B[3]["start"], "stay"),
        ("timer", "hourglass_not_done", 0.48, 0.30, 1.0, I["hour"], B[3]["start"], "stay"),
        ("tea", "hot_beverage", -0.68, 0.25, 0.8, bb(I["hour"] + 0.35), 99, "stay"),
        ("plant", "potted_plant", -0.82, 0.02, 0.95, bb(I["hour"] + 0.35) + beat, 99, "stay"),
        ("hero", "smiling_face_with_hearts", 0.0, 0.58, 1.45, B[3]["start"] + 0.05, 99, "stay"),
        ("trophy", "trophy", 0.62, 0.36, 0.95, bb(B[3]["start"] + 0.5), 99, "stay"),
        ("check", "check_mark_button", -0.15, 0.10, 0.75, bb(B[3]["start"] + 0.5) + beat, 99, "stay"),
        ("heart", "sparkling_heart", 0.7, 0.88, 0.8, bb(B[3]["start"] + 0.5) + beat * 1.5, 99, "stay"),
    ]
    PK, INK, BT, CR = "#FF5CA8", "#141414", "#FFE27A", "#FFF4E0"
    html_objs = "".join(f'<div class="sh" id="s_{o[0]}"></div>' for o in objs) + "".join(
        f'<img class="ob" id="o_{o[0]}" src="{fluent(o[1])}">' for o in objs)
    css = f"""
    #world{{position:absolute;inset:0;transform-origin:50% 60%}}
    #wall{{position:absolute;left:-300px;top:-300px;width:1680px;height:1260px;
       background:radial-gradient(ellipse at 50% 70%,#FFE3EF 0,#FFC2DC 45%,#FF9CCB 100%)}}
    #win{{position:absolute;left:90px;top:560px;width:250px;height:330px;border-radius:180px 180px 26px 26px;
       background:linear-gradient(180deg,#FFF6C9,#FFE27A);box-shadow:inset 0 0 0 16px #FFF4E0,0 20px 40px rgba(200,60,120,.18)}}
    #desk{{position:absolute;left:-400px;top:960px;width:1880px;height:1400px;
       background:repeating-linear-gradient(92deg,rgba(190,120,20,.05) 0 9px,rgba(255,255,255,.04) 9px 23px),
                  linear-gradient(180deg,#FFD95A 0%,#FFE27A 35%,#FFEDA8 100%);
       box-shadow:0 -10px 0 #F2C744, 0 -26px 40px rgba(160,90,0,.12)}}
    #glow{{position:absolute;left:0;top:820px;width:1080px;height:1100px;background:radial-gradient(ellipse at 60% 15%,rgba(255,255,255,.55),transparent 55%)}}
    .ob{{position:absolute;left:0;top:0;width:260px;height:260px;transform-origin:50% 100%;will-change:transform}}
    .sh{{position:absolute;left:0;top:0;width:240px;height:60px;border-radius:50%;background:radial-gradient(ellipse,rgba(120,60,0,.42),rgba(120,60,0,0) 70%)}}
    .em{{color:{PK}}}
    #dust{{position:absolute;inset:0;pointer-events:none}}
    .pf{{position:absolute;width:26px;height:26px;border-radius:50%;background:#FFF4E0;opacity:0}}
    """
    puffs = "".join(f'<div class="pf" id="pf{i}"></div>' for i in range(60))
    body = f"""
<div id="world"><div id="wall"></div><div id="win"></div><div id="desk"></div><div id="glow"></div>
 {html_objs}<div id="dust">{puffs}</div></div>
<div class="txt" id="T1" style="top:160px">{words("You opened your phone / to check one thing.", em=("one",))}</div>
<div class="txt" id="T2" style="top:190px;font-size:136px">{words("40 minutes / later…", em=("40",))}</div>
<div class="txt" id="T3a" style="top:130px;font-size:110px">{words("Try this:")}</div>
<div class="txt" id="T3b" style="top:270px;font-size:80px">{words("Phone in another room.")}</div>
<div class="txt" id="T3c" style="top:380px;font-size:80px">{words("One task.", em=("one",))} &nbsp;{words("One hour.", em=("one",))}</div>
<div class="txt" id="T4" style="top:180px;font-size:104px">{words("Your future self / says thanks.", em=("thanks",))}</div>
"""
    import json
    js = """
const OB=""" + json.dumps(objs) + """;
const B=TL.blocks, I=TL.items, beat=TL.beat, D=TL.drop;
let _s=11; const rnd=()=>{ _s=(_s*16807)%2147483647; return (_s-1)/2147483646; };
const SW=OB.map(()=>({vx:900+rnd()*1600, vy:-900-rnd()*900, sp:(rnd()-0.3)*900}));
const PF=[...Array(60)].map(()=>({a:rnd()*Math.PI*2, v:120+rnd()*260, s:0.4+rnd()*0.9}));
function proj(u,v){ return {x:540+u*(300+250*v), y:1060+v*640, k:(0.62+0.55*v)*1.6}; }
window.seek = async (t) => {
  const bk=blockAt(t); let blur=1; let impact=0;
  // camera path: gentle drift + a move per block
  const camX=[0,-40,30,0][bk]*E.inOut(prog(t,B[bk].start,0.5)) + Math.sin(t*0.7)*14;
  const camS=[1.0,1.06,1.0,1.04][bk];
  let shx=0, shy=0;
  // ---------------- objects
  let landings=[];
  OB.forEach(([id,ic,u,v,sz,tin,tout,mode],i)=>{ const o=$('o_'+id), s=$('s_'+id); const p=proj(u,v);
    const W=260*sz*p.k;
    if(t<tin && tin>0){ vis(o,false); vis(s,false); return; }
    let y=p.y, x=p.x, r=0, sx=1, sy=1, op=1, h=0;
    const b=bounce(t,Math.max(tin,-5),0.34,3); if(tin>0){ h=(1-b.y)*1500; sy=1-0.22*b.sq; sx=1+0.2*b.sq; if(b.landed&&t-tin<0.5) landings.push([tin+0.34,p,i]); }
    if(t>=tout){ const dt=t-tout;
      if(mode==='sweep'){ const w=SW[i]; x+=w.vx*dt*(1+i%3*0.2); h+= -(w.vy*dt) - 0.5*-2600*dt*dt*-1; h=Math.max(-200, -w.vy*dt - 1300*dt*dt); r=w.sp*dt; if(dt<0.25) blur=3; }
      if(mode==='lift'){ const u2=E.inExpo(prog(t,tout,0.55)); h=u2*1700; x=lerp(p.x, proj(0.78,0.05).x, E.inOut(prog(t,tout,0.55))); sx=sy=1-0.4*u2; r=u2*-14; if(u2>0.05&&u2<0.98) blur=3; }
    }
    // idle life: wobble on the beat
    const pb=Math.exp(-sinceBeat(t)/0.12); if(t>tin+0.6 && t<tout){ sy*=1+0.04*pb; sx*=1-0.02*pb; }
    if(id==='clock' && t>=tin && t<tout){ r=Math.sin(t*50)*4*(t<D?1:0); }
    if(id==='hero' && t>=tin+0.5){ r=Math.sin((t-tin)*3)*4; }
    vis(o,true); vis(s,mode!=='sweep'||t<tout+0.1);
    o.style.width=o.style.height=W+'px';
    o.style.transform=`translate(${x-W/2}px,${y-W - h}px) rotate(${r}deg) scale(${sx},${sy})`; o.style.zIndex=Math.round(100+v*100);
    const hs=clamp(1-h/1500); const SWd=W*0.9*(0.5+0.5*hs);
    s.style.width=SWd+'px'; s.style.height=SWd*0.24+'px'; s.style.opacity=(t>=tout&&mode!=='stay')?Math.max(0,1-(t-tout)*5)*hs:0.25+0.75*hs*hs;
    s.style.transform=`translate(${p.x-SWd/2}px,${p.y-SWd*0.12}px)`; s.style.filter=`blur(${(1-hs)*14+2}px)`; s.style.zIndex=99;
  });
  // impacts: dust puffs + small camera kick
  $$('.pf').forEach(e=>e.style.opacity=0);
  landings.forEach(([tl_,p,i],j)=>{ const dt=t-tl_; if(dt<0||dt>0.45) return; if(dt<0.12){ shy+= (1-dt/0.12)*10*OB[i][4]; }
    for(let k=0;k<6;k++){ const e=$('pf'+((i*6+k)%60)), f=PF[(i*6+k)%60]; const u=E.out3(dt/0.45);
      e.style.opacity=(1-dt/0.45)*0.8; e.style.transform=`translate(${p.x+Math.cos(f.a)*f.v*u*p.k-13}px,${p.y-8+Math.sin(f.a)*f.v*u*0.25*p.k}px) scale(${f.s*(1+u)})`; } });
  const sk=shake(t,D,0.4,30); shx+=sk.x; shy+=sk.y;
  $('world').style.transform=`translate(${camX+shx}px,${shy}px) scale(${camS})`;
  if(t>=D-0.02&&t<D+0.1) blur=3;
  // ---------------- text
  vis($('T1'),bk===0); kwords($('T1'),t,-1,{});
  vis($('T2'),bk===1); if(bk===1) kwords($('T2'),t,B[1].start,{mode:'drop',gap:0.08,f:2.6,z:0.4});
  vis($('T3a'),bk===2); if(bk===2) kwords($('T3a'),t,D,{mode:'drop',gap:0.1,f:2.8,z:0.4});
  vis($('T3b'),bk===2&&t>=I.phone); if(bk===2) kwords($('T3b'),t,I.phone,{mode:'drop',gap:0.06});
  vis($('T3c'),bk===2&&t>=I.task); if(bk===2){ $$('.w',$('T3c')).forEach((w,i)=>{ const s0=(i<2?I.task:I.hour)+(i%2)*0.07; const u=spring(t,s0,2.6,0.4);
      w.style.opacity=t<s0?0:prog(t,s0,0.1); w.style.transform=`translateY(${(1-u)*-200}px)`; }); }
  vis($('T4'),bk===3); if(bk===3) kwords($('T4'),t,B[3].start,{mode:'drop',gap:0.07});
  await flush(); return {blur};
};
"""
    st.default_sfx(cut="sfx-x-whoosh-hit", b4="sfx-x-whoosh-hit")
    for o in objs:
        if o[5] > 0:
            land = o[5] + 0.34
            st.add_sfx(land, "sfx-x-paper-slap", -7 if o[4] > 1.0 else -10)
    st.add_sfx(D + 0.02, "sfx-x-swoosh-in", -4)
    st.add_sfx(tl["items"]["phone"] + 0.1, "sfx-x-swoosh-in", -6)
    st.add_sfx(tl["blocks"][1]["start"] + 0.4, "sfx-x-tick-tock", -12)
    if only == "remix":
        return st.remix()
    return st.build(css, body, js, bg="#FFC2DC", only=only)


if __name__ == "__main__":
    only = ("remix" if sys.argv[1] == "remix" else [int(x) for x in sys.argv[1].split(",")]) if len(sys.argv) > 1 else None
    print(build(only))

#!/usr/bin/env python3
"""Style 5: phone-UI simulation, notifications pile up and EXPLODE on the drop (hb-x-smart-bounce, 114.8 bpm).

B1 lock screen -> notifications drop in on half beats; B2 screen-time counter races to 40:00 while the stack
overflows the phone; B3 (drop) every card blasts out with physics, the phone zips off into another room, a
focus widget builds "one task / one hour" with a live 60:00 ring; B4 a message from "Future you" lands.
"""
import sys

from common import Style, fluent, words

TRACK = "hb-x-smart-bounce"

APPS = [  # (3D icon, app, line) generic, nothing branded
    ("speech_balloon", "Messages", "Sam: did you see this?? 😂"),
    ("bell", "Reminders", "3 things are waiting"),
    ("sparkles", "For You", "12 new videos for you"),
    ("party_popper", "Group chat", "47 new messages"),
    ("wrapped_gift", "Shop", "Sale ends tonight!"),
    ("eyes", "Social", "Alex viewed your story"),
    ("star", "Games", "Your lives are full ❤️"),
    ("balloon", "Events", "Party at 8? 🎉"),
    ("rocket", "News", "You won't believe this…"),
    ("glowing_star", "Photos", "On this day, 3 years ago"),
    ("speech_balloon", "Messages", "Jordan: lol same"),
    ("bell", "Mail", "14 unread"),
]


def build(only=None):
    st = Style(5, "phone-ui", TRACK)
    tl = st.tl
    PK, INK, BT, CR = "#FF5CA8", "#141414", "#FFE27A", "#FFF4E0"
    cards = "".join(
        f'<div class="nt" id="n{i}"><img src="{fluent(ic)}"><div><b>{app}</b><span>{line}</span></div><i>now</i></div>'
        for i, (ic, app, line) in enumerate(APPS))
    confetti = "".join(f'<img class="cf" id="cf{i}" src="{fluent(n)}">' for i, n in enumerate(
        ["party_popper", "sparkles", "pink_heart", "glowing_star", "sparkling_heart", "star", "confetti_ball", "smiling_face_with_hearts"]))
    css = f"""
    #bg{{position:absolute;inset:-200px;background:radial-gradient(circle at 20% 15%,#FFF1B0 0,transparent 42%),
        radial-gradient(circle at 85% 70%,rgba(255,92,168,.30) 0,transparent 45%),{BT}}}
    .blob{{position:absolute;border-radius:50%;filter:blur(40px);opacity:.55}}
    #phone{{position:absolute;left:210px;top:560px;width:660px;height:1330px;border-radius:96px;background:{INK};
        box-shadow:0 60px 90px rgba(20,20,20,.28),0 18px 30px rgba(20,20,20,.18),inset 0 0 0 4px #3a3a3a;transform-origin:50% 40%}}
    #scr{{position:absolute;left:22px;top:22px;right:22px;bottom:22px;border-radius:76px;overflow:hidden;
        background:linear-gradient(160deg,#FFB3D6 0%,#FFD9A8 45%,#FFE27A 100%)}}
    #island{{position:absolute;left:50%;top:22px;width:180px;height:50px;margin-left:-90px;border-radius:30px;background:{INK};z-index:5}}
    #clock{{position:absolute;top:120px;width:100%;text-align:center;font:800 170px/1 Inter;color:#fff;letter-spacing:-0.04em;
        text-shadow:0 6px 20px rgba(160,40,90,.25)}}
    #date{{position:absolute;top:96px;width:100%;text-align:center;font:600 34px/1 Inter;color:#fff;opacity:.95}}
    .nt{{position:absolute;left:34px;width:548px;height:118px;border-radius:34px;background:rgba(255,255,255,.88);
        display:flex;align-items:center;gap:18px;padding:0 22px;box-shadow:0 10px 24px rgba(120,40,80,.16);font-family:Inter}}
    .nt img{{width:76px;height:76px;border-radius:20px;background:#fff;padding:6px}}
    .nt div{{flex:1;display:flex;flex-direction:column;gap:6px;min-width:0}}
    .nt b{{font:800 28px/1 Inter;color:{INK}}} .nt span{{font:500 27px/1.1 Inter;color:#3a3a3a;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
    .nt i{{font:500 22px/1 Inter;color:#777;font-style:normal;align-self:flex-start;margin-top:26px}}
    #badge{{position:absolute;left:610px;top:520px;min-width:120px;height:120px;border-radius:60px;background:{PK};color:#fff;
        font:900 58px/120px Inter;text-align:center;padding:0 24px;box-shadow:0 14px 30px rgba(232,51,111,.35);z-index:20}}
    #st{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
        background:rgba(20,20,20,.0)}}
    #stc{{font:900 168px/1 Inter;color:{INK};letter-spacing:-0.05em;font-variant-numeric:tabular-nums}}
    #stl{{font:800 38px/1 Inter;color:{INK};opacity:.75;margin-bottom:18px}}
    #ring{{position:absolute;left:50%;top:50%;width:520px;height:520px;margin:-260px 0 0 -260px}}
    #focus{{position:absolute;left:150px;top:800px;width:780px;height:760px;border-radius:70px;background:{CR};
        box-shadow:0 50px 80px rgba(20,20,20,.20),0 14px 26px rgba(20,20,20,.12);overflow:hidden}}
    #fh{{position:absolute;left:60px;top:54px;font:800 40px/1 Inter;color:{INK};display:flex;align-items:center;gap:16px}}
    #tog{{position:absolute;right:60px;top:44px;width:120px;height:66px;border-radius:33px;background:#ccc}}
    #knob{{position:absolute;left:6px;top:6px;width:54px;height:54px;border-radius:27px;background:#fff;box-shadow:0 3px 8px rgba(0,0,0,.2)}}
    .row{{position:absolute;left:60px;right:60px;height:120px;border-radius:30px;background:#fff;display:flex;align-items:center;gap:26px;
        padding:0 30px;font:900 60px/1 Inter;color:{INK};letter-spacing:-0.03em;box-shadow:0 8px 18px rgba(20,20,20,.08)}}
    .cb{{width:60px;height:60px;border-radius:18px;border:6px solid {INK};position:relative;flex:none}}
    .cb svg{{position:absolute;left:-6px;top:-14px;width:80px;height:80px;overflow:visible}}
    #timer{{position:absolute;left:50%;bottom:120px;width:330px;height:330px;margin-left:-165px}}
    #tnum{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:900 84px/1 Inter;color:{INK};font-variant-numeric:tabular-nums}}
    #door{{position:absolute;left:1080px;top:880px;width:300px;height:560px;border-radius:24px 24px 0 0;background:#FFB3D6;
        box-shadow:inset 0 0 0 14px {INK};}}
    #door:after{{content:'';position:absolute;left:36px;top:280px;width:30px;height:30px;border-radius:50%;background:{INK}}}
    #msg{{position:absolute;left:90px;top:780px;width:900px;border-radius:56px;background:#fff;padding:44px 50px 50px;
        box-shadow:0 50px 90px rgba(20,20,20,.22),0 12px 24px rgba(20,20,20,.12);font-family:Inter}}
    #msg .from{{display:flex;align-items:center;gap:22px;font:800 40px/1 Inter;color:{INK}}}
    #msg .from img{{width:96px;height:96px}}
    #msg .body{{margin-top:30px;font:900 120px/1 Inter;color:{PK};letter-spacing:-0.04em}}
    .cf{{position:absolute;width:150px;height:150px}}
    .em{{color:{PK}}}
    .hlw{{background:linear-gradient(transparent 60%,rgba(255,92,168,.75) 60%,rgba(255,92,168,.75) 90%,transparent 90%)}}
    """
    body = f"""
<div id="bg"></div>
<div class="blob" style="left:-120px;top:1200px;width:520px;height:520px;background:#FF8CC4" id="bl1"></div>
<div class="blob" style="left:700px;top:260px;width:460px;height:460px;background:#FFF6C9" id="bl2"></div>
<div id="door"></div>
<div id="phone"><div id="scr"><div id="date">Thursday, 16 October</div><div id="clock">9:41</div>
  <div id="stack">{cards}</div>
  <div id="st"><div id="stl">Screen time today</div><div id="stc">0:00</div>
   <svg id="ring" viewBox="0 0 520 520"><circle cx="260" cy="260" r="236" fill="none" stroke="rgba(20,20,20,.12)" stroke-width="26"/>
    <circle id="rp" cx="260" cy="260" r="236" fill="none" stroke="{PK}" stroke-width="26" stroke-linecap="round" transform="rotate(-90 260 260)" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1"/></svg></div>
 </div><div id="island"></div></div>
<div id="badge">+1</div>
<div id="focus"><div id="fh"><img src="{fluent('locked')}" style="width:62px;height:62px">Focus</div><div id="tog"><div id="knob"></div></div>
  <div class="row" id="r1" style="top:170px"><div class="cb"><svg viewBox="0 0 80 80"><path id="k1" d="M12,40 L32,62 L76,8" fill="none" stroke="{PK}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1"/></svg></div>One task</div>
  <div id="timer"><svg viewBox="0 0 330 330" style="width:330px;height:330px"><circle cx="165" cy="165" r="140" fill="none" stroke="rgba(20,20,20,.1)" stroke-width="24"/>
   <circle id="tp" cx="165" cy="165" r="140" fill="none" stroke="{PK}" stroke-width="24" stroke-linecap="round" transform="rotate(-90 165 165)" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="0"/></svg>
   <div id="tnum">60:00</div></div></div>
<div id="msg"><div class="from"><img src="{fluent('smiling_face_with_hearts')}"><div>Future you<div style="font:500 30px/1.4 Inter;color:#777">now</div></div></div>
  <div class="body" id="mb">{words("thanks.")} <span class="w">💛</span></div></div>
{confetti}
<div class="txt" id="T1" style="top:150px">{words("You opened your phone / to check one thing.", em=("one",))}</div>
<div class="txt" id="T2" style="top:170px;font-size:130px">{words("40 minutes / later…", em=("40",))}</div>
<div class="txt" id="T3a" style="top:150px;font-size:118px">{words("Try this:")}</div>
<div class="txt" id="T3b" style="top:300px;font-size:84px">{words("Phone in another room.")}</div>
<div class="txt" id="T3c" style="top:420px;font-size:84px">{words("One task.", em=("one",))} &nbsp;{words("One hour.", em=("one",))}</div>
<div class="txt" id="T4" style="top:200px;font-size:104px">{words("Your future self / says thanks.", em=("thanks",))}</div>
"""
    js = """
const B=TL.blocks, I=TL.items, beat=TL.beat, D=TL.drop;
// deterministic random
let _s=7; const rnd=()=>{ _s=(_s*16807)%2147483647; return (_s-1)/2147483646; };
const N=12; const V=[...Array(N)].map(()=>({vx:(rnd()-0.5)*5200, vy:-1400-rnd()*2600, sp:(rnd()-0.5)*1500}));
const CF=[...Array(8)].map(()=>({vx:(rnd()-0.5)*2200, vy:-2200-rnd()*1400, sp:(rnd()-0.5)*900, x:440+rnd()*200}));
const firstNt = 0.75;                     // first notification lands
const ntT=[...Array(N)].map((_,i)=>{ const half=beat/2; return firstNt + i*half*(i<6?1:0.5) + (i>=6?3*half:0); });
window.seek = async (t) => {
  const bk=blockAt(t); let blur=1;
  const pulse=Math.exp(-sinceBeat(t)/0.1);
  $('bg').style.transform=`translate(${Math.sin(t*0.8)*40}px,${Math.cos(t*0.6)*40}px) scale(${1+0.01*pulse})`;
  tf($('bl1'),{x:Math.sin(t*1.3)*80,y:Math.cos(t*1.1)*60,s:1+0.08*pulse}); tf($('bl2'),{x:Math.cos(t*1.2)*70,y:Math.sin(t)*70,s:1+0.08*pulse});
  // ---------------- phone
  const ph=$('phone'); let pS=1, pX=0, pY=0, pR=0;
  pY=Math.sin(t*2)*6; pR=Math.sin(t*1.3)*1.2;
  if(bk===1){ const u=E.out3(prog(t,B[1].start,0.35)); pS=1-0.08*u; pR+= -4*u; }
  // at the drop: phone jolts, then zips right into the door at the phone item
  const z0=I.phone+0.05, zu=E.inExpo(prog(t,z0+0.2,0.42));
  if(t>=D){ const k=spring(t,D,3,0.35); pS=0.94+0.06*k; }
  if(t>=z0){ pX=1200*zu; pR+=zu*25; pS*=1-0.35*zu; if(zu>0.05&&zu<0.98) blur=3; }
  tf(ph,{x:pX,y:pY+ (bk===3?2000:0),s:pS,r:pR}); vis(ph,t<z0+0.62);
  // door slides in, takes the phone, slides out
  const dIn=E.out3(prog(t,z0,0.25)), dOut=E.in3(prog(t,z0+0.7,0.25));
  tf($('door'),{x:-400*dIn+400*dOut}); vis($('door'),t>=z0&&t<z0+1.0);
  // ---------------- lock screen clock + notifications
  const nOver = (t>=D);
  for(let i=0;i<N;i++){ const n=$('n'+i); const t0=ntT[i]; if(t<t0){ n.style.opacity=0; continue; }
    const u=spring(t,t0,3.2,0.5); const order=ntT.filter(x=>x<=t).length-1-i; // newest on top
    let x=0, y=330+order*134 - (1-u)*160, s=0.85+0.15*u, r=0, o=prog(t,t0,0.08);
    if(bk===1){ y+= (t-B[1].start)*60; o*=1-0.8*prog(t,B[1].start,0.2); s*=1-0.1*prog(t,B[1].start,0.2); }
    if(nOver){ const dt=t-D; const v=V[i]; x+=v.vx*dt; y+=v.vy*dt+0.5*5200*dt*dt; r=v.sp*dt; s*=1+dt*0.8; o=dt<0.7?1:Math.max(0,1-(dt-0.7)*4); }
    n.style.transform=`translate(${x}px,${y}px) rotate(${r}deg) scale(${s})`; n.style.opacity=o; n.style.zIndex=50+i; }
  // explosion cards must leave the phone's screen clip: move them out of #scr at the drop
  const stack=$('stack'); if(nOver && stack.parentNode.id==='scr'){ /* handled by reparent below */ }
  $('clock').style.opacity = t<ntT[3]?1:Math.max(0,1-(t-ntT[3])*3);
  $('date').style.opacity = $('clock').style.opacity;
  // badge
  const cnt=ntT.filter(x=>x<=t).length; const bd=$('badge'); vis(bd, cnt>0 && t<D);
  const lastT=ntT.filter(x=>x<=t).pop()||0; const bu=spring(t,lastT,4,0.35);
  bd.textContent='+'+(bk===1? Math.floor(cnt*1+ (t-B[1].start)*60):cnt*3); tf(bd,{s:0.7+0.3*bu, r:(1-bu)*-20});
  // screen time (B2)
  const st_=$('st'); st_.style.opacity=bk===1?prog(t,B[1].start,0.12):0;
  if(bk===1){ const u=E.inOut(prog(t,B[1].start+0.05,B[2].start-B[1].start-0.35)); const m=Math.floor(u*40), sec=Math.floor((u*40-m)*60);
    $('stc').textContent=`${m}:${String(sec).padStart(2,'0')}`; $('rp').style.strokeDashoffset=1-u*0.67; }
  // ---------------- focus widget
  const fo=$('focus'); const f0=I.phone+0.75; vis(fo,t>=f0&&bk===2);
  if(t>=f0){ const u=spring(t,f0,2.4,0.45); tf(fo,{y:(1-u)*900,r:(1-u)*8}); }
  const tg=prog(t,I.task+0.1,0.18); $('tog').style.background=tg>0.5?'#FF5CA8':'#cfcfcf'; tf($('knob'),{x:54*E.out3(tg)});
  $('k1').style.strokeDashoffset=1-E.out3(prog(t,(TL.beats.find(b=>b>=I.task+0.35)||I.task+0.4),0.2));
  const hu=prog(t,I.hour,TL.blocks[3].start-I.hour); const secs=Math.max(0,3600-Math.floor(hu*48));
  $('tnum').textContent=`${Math.floor(secs/60)}:${String(secs%60).padStart(2,'0')}`; $('tp').style.strokeDashoffset=t>=I.hour?hu*0.02:0;
  tf($('timer'),{s:t<I.hour?0.0001:0.6+0.4*spring(t,I.hour,3,0.4)});
  // ---------------- B4: message from future you + confetti
  const ms=$('msg'); vis(ms,bk===3); if(bk===3){ const u=spring(t,B[3].start+0.1,2.6,0.42); tf(ms,{y:(1-u)*-700,s:0.8+0.2*u,r:(1-u)*-6});
    kwords($('mb'),t,B[3].start+0.45,{mode:'pop',gap:0.12}); }
  for(let i=0;i<8;i++){ const c=$('cf'+i); const t0=B[3].start+0.55; const dt=t-t0; vis(c,dt>0);
    if(dt>0){ const v=CF[i]; c.style.transform=`translate(${v.x+v.vx*dt*0.5}px,${1500+v.vy*dt+0.5*2600*dt*dt}px) rotate(${v.sp*dt}deg) scale(${0.6+0.4*spring(t,t0,3,0.4)})`; } }
  // ---------------- text
  vis($('T1'),bk===0); kwords($('T1'),t,-1,{});
  vis($('T2'),bk===1); if(bk===1) kwords($('T2'),t,B[1].start,{mode:'stamp',gap:0.08,f:3,z:0.45});
  vis($('T3a'),bk===2); if(bk===2) kwords($('T3a'),t,D,{mode:'stamp',gap:0.1,f:3,z:0.45});
  vis($('T3b'),bk===2&&t>=I.phone); if(bk===2) kwords($('T3b'),t,I.phone,{mode:'up',gap:0.06});
  vis($('T3c'),bk===2&&t>=I.task); if(bk===2){ const ws=$$('.w',$('T3c')); ws.forEach((w,i)=>{ const s0=(i<2?I.task:I.hour)+(i%2)*0.07; const u=spring(t,s0,2.6,0.42);
      w.style.opacity=t<s0?0:prog(t,s0,0.1); w.style.transform=`translateY(${(1-u)*60}px) scale(${0.5+0.5*u})`; }); }
  vis($('T4'),bk===3); if(bk===3) kwords($('T4'),t,B[3].start,{mode:'pop',gap:0.07});
  // camera shake on the drop
  const sk=shake(t,D,0.35,26); $('stage').style.transform=`translate(${sk.x}px,${sk.y}px)`;
  if(t>=D-0.03&&t<D+0.12) blur=3;
  await flush(); return {blur};
};
// cards need to fly past the phone's rounded screen: keep them in #stage coordinates by lifting the stack out
(function(){ const stack=$('stack'), scr=$('scr'); const holder=document.createElement('div'); holder.style.cssText='position:absolute;left:232px;top:582px;width:616px;height:1286px;border-radius:76px;overflow:hidden;z-index:6';
  $('phone').after(holder); holder.appendChild(stack); window._holder=holder;
  const st=$('st'); const sh=document.createElement('div'); sh.style.cssText='position:absolute;left:232px;top:582px;width:616px;height:1286px;z-index:7;pointer-events:none';
  holder.after(sh); sh.appendChild(st); window._sth=sh; })();
const _seek=window.seek; window.seek=async(t)=>{ const r=await _seek(t); const h=window._holder; const ph=$('phone');
  h.style.transform=ph.style.transform; h.style.transformOrigin='50% 40%'; h.style.visibility=ph.style.visibility;
  const s2=window._sth; s2.style.transform=ph.style.transform; s2.style.transformOrigin='50% 40%';
  h.style.overflow = t>=TL.drop ? 'visible' : 'hidden'; if(t>=TL.drop){ h.style.transform='none'; } return r; };
"""
    st.default_sfx(cut="sfx-x-swoosh-in", b4="sfx-x-whoosh-hit")
    half = tl["beat"] / 2
    nt = [0.75 + i * half * (1 if i < 6 else 0.5) + (3 * half if i >= 6 else 0) for i in range(12)]
    for i, t0 in enumerate(nt):
        if t0 < tl["drop"]:
            st.add_sfx(t0, "sfx-x-sticker-pop", -11 if i % 2 else -9)
    st.add_sfx(tl["blocks"][1]["start"] + 0.05, "sfx-x-tick-tock", -12)
    st.add_sfx(tl["items"]["phone"] + 0.25, "sfx-x-swoosh-in", -6)
    st.add_sfx(tl["items"]["phone"] + 0.68, "sfx-x-paper-slap", -6)
    st.add_sfx(tl["items"]["task"] + 0.1, "sfx-x-sticker-pop", -8)
    st.add_sfx(tl["items"]["hour"], "sfx-x-sticker-pop", -8)
    st.add_sfx(tl["blocks"][3]["start"] + 0.55, "sfx-x-sticker-pop", -6)
    if only == "remix":
        return st.remix()
    return st.build(css, body, js, only=only)


if __name__ == "__main__":
    only = ("remix" if sys.argv[1] == "remix" else [int(x) for x in sys.argv[1].split(",")]) if len(sys.argv) > 1 else None
    print(build(only))

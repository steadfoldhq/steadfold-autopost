#!/usr/bin/env python3
"""Hourback Reels built Wed Nov 4 2026 by the Hourback maker (Social studio).

    python3 studio/editorial/nov04_hourback.py thanks|nonna|retire           # mp4 (+ dedicated cover for nonna/retire)
    python3 studio/editorial/nov04_hourback.py thanks --still 0,2.5,5         # stills sheet in the scratch dir (review)
    python3 studio/editorial/nov04_hourback.py thanks --full 13.5             # one full-size frame (review)
    python3 studio/editorial/nov04_hourback.py nonna --cover-only

thanks = D2 re-edit of hb-reel-1106-thank-you-20 (Fri Nov 6, 7 pm) = the SEND TEST (Performance desk Nov 4, order 1)
         + output in frame 0 (order 4). Frame 0 now shows Claude's real note 1 (Aunt Rosa) word for word in the note card
         under the hook (was an empty 'Dear…' card). Beat 1 is shorter (notes 2-20 riffle sooner); in the last 2.3 s the
         note card flips to ONE send line ('Send this to whoever just had a baby shower.') together with the follow pill.
         Overwrites media/studio-nov03/hourback/hb-reel-1106-thank-you-20.mp4 (cover unchanged). Real run unchanged:
         studio/editorial/hb-nov03-run-thanks.txt.
nonna  = hb-reel-1108-nonna-90 (Sun Nov 8, 7 pm). See JS_NOV04 below. Real run: hb-nov04-run-nonna.txt.
retire = hb-reel-1109-retirement-speech (Mon Nov 9, 7 pm). Real run: hb-nov04-run-retire.txt.

Extends studio/editorial/nov03_hourback.py (-> nov02 -> nov01 -> oct28 engine) by import. No shared kit or older
script is edited; the Nov 3 JS is patched in memory only.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
sys.dont_write_bytecode = True
import nov03_hourback as N3  # noqa: E402

B = N3.B
B.SCR = Path("/tmp/claude-0/nov04-hourback")
LIB = B.LIB
OUT4 = REPO / "media/studio-nov04/hourback"
OUT3 = REPO / "media/studio-nov03/hourback"


def run_reply(slug, day="nov04"):
    t = (REPO / f"studio/editorial/hb-{day}-run-{slug}.txt").read_text()
    return t.split("===== REPLY (verbatim) =====\n", 1)[1]


# ------------------------------------------------------------------ D2 data: note 1 in full (word for word)
ROSA = N3.N[1][1]
assert ROSA.startswith("Your handmade quilt is already folded") and ROSA.endswith("something you made.")
assert ROSA in run_reply("thanks", "nov03").replace("\n", " ")
SEND_THANKS = "Send this to whoever just had a baby shower."

JS_D2 = r"""
// =============================================== Nov 4 D2: note 1 in frame 0, send-line flip at the end
const D4T=__D4T__;
const ASK_HOLD=2.0, T0=2.3;            // CD gate Nov 4: the made-up prompt sticky holds >=2 s at >=36 px, then flies in
const RS4=T0+1.2, RE4=RS4+1.4;
function giftList4(lt){ // the made-up gift list from the real prompt: held 2 s above the card, then flies into it
 const k=E(seg(lt,0,0.15)), fl=seg(lt,ASK_HOLD,T0); if(fl>=1) return '';
 const tx=60+(TN_X+200-60)*E(fl), ty=690+(TN_Y+60-690)*E(fl), sc=1-0.72*E(fl);
 const inner=label(26,60,'gift list we made up for this post:',-2,50,ACC,'start')+textLines(26,132,["1. Aunt Rosa: a handmade quilt","2. Priya: a baby carrier","3. Grandpa Joe: a rocking chair he fixed up","… 20 in all"],52,60,OL,'Caveat',700);
 return `<g opacity="${k*(1-seg(fl,.8,1))}" transform="translate(${tx} ${ty}) scale(${sc})">`+sticky(0,0,900,352,-2,'#FFE7A0',inner,40*(1-k))+`</g>`;}
function afterDraw(i,lt){ const e=document.getElementById('sub1'); if(!e) return;
 e.style.opacity = i==1 ? E(seg(lt,T0,T0+0.25)) : 1; }
function noteCard4(beat,lt,t,st){
 let s=`<rect x="12" y="16" width="${TNW}" height="${TNH}" rx="22" fill="rgba(42,29,71,.16)"/><rect x="0" y="0" width="${TNW}" height="${TNH}" rx="22" fill="#FFFFFF" ${o}/>`;
 // the send flip (last beat): the card turns over and carries the one send line
 if(beat==3 && lt>=D4T.sendAt-0.12){
   const k=seg(lt,D4T.sendAt-0.12,D4T.sendAt+0.12);
   if(k<0.5){ return `<g transform="translate(0 ${TNH/2}) scale(1 ${1-2*k}) translate(0 ${-TNH/2})">`+noteBody(3,9,t)+`</g>`; }
   const e=E((k-0.5)*2); let c=`<g transform="translate(0 ${TNH/2}) scale(1 ${e}) translate(0 ${-TNH/2})">`;
   c+=`<rect x="12" y="16" width="${TNW}" height="${TNH}" rx="22" fill="rgba(42,29,71,.16)"/><rect x="0" y="0" width="${TNW}" height="${TNH}" rx="22" fill="#FFE7A0" ${o}/>`;
   c+=`<g transform="translate(${TNW-150} 70) rotate(8)"><rect x="-70" y="-40" width="140" height="80" rx="8" fill="#FFFFFF" stroke="${OL}" stroke-width="4"/><path d="M-70 -40 L0 8 L70 -40" fill="none" stroke="${OL}" stroke-width="4"/></g>`;
   c+=`<text x="${TNW/2}" y="${TNH/2+4}" text-anchor="middle" font-family="Caveat Brush" font-size="84" fill="${INDI}">Send this to whoever</text>`;
   c+=`<text x="${TNW/2}" y="${TNH/2+100}" text-anchor="middle" font-family="Caveat Brush" font-size="84" fill="${ACC}">just had a baby shower.</text>`;
   return c+`</g>`; }
 return s+noteBody(beat,lt,t);}
function noteBody(beat,lt,t){
 let s=`<rect x="0" y="0" width="${TNW}" height="${TNH}" rx="22" fill="#FFFFFF" ${o}/>`;
 s+=`<path d="M0 22 Q0 0 22 0 H${TNW-22} Q${TNW} 0 ${TNW} 22 V92 H0Z" fill="${PEACH}" ${o} stroke-width="4"/>`;
 if(beat==0 || (beat==1 && lt<T0)){ // note 1, word for word, already on the card at 0.00 s
   s+=`<text x="40" y="64" font-family="Poppins" font-weight="700" font-size="40" fill="${INK}">Note 1 of 20, word for word</text>`;
   s+=`<text x="40" y="156" font-family="DM Serif Display" font-size="52" fill="${INDI}">${esc(D3.show[0][1])}</text>`;
   s+=textLines(40,214,D4T.rosa,44,52,PEN,'Caveat',700);
   return s; }
 let num=0, name='', lines=[], big=false, hl=0, fresh=0;
 if(beat==1){
   num=2; name=D3.show[1][1]; lines=D3.show[1][2]; fresh=lt-T0;
   if(lt>=RS4){ const k=Math.min(17,Math.floor((lt-RS4)/(RE4-RS4)*18)); const r=D3.riff[k]; num=r[0]; name=r[1]; lines=r[2]; fresh=1; }
 } else { num=3; name="Grandpa Joe"; big=true; fresh=beat==2?lt:1; hl=beat==2?E(seg(lt,0.5,1.0)):1; }
 const p=E(seg(fresh,0,0.14));
 s+=`<text x="40" y="64" font-family="Poppins" font-weight="700" font-size="40" fill="${INK}">${big?'Note 3, word for word':'Note '+num+' of 20'}</text>`;
 const bw=big?1:Math.min(1,num/20); s+=`<rect x="560" y="36" width="340" height="30" rx="15" fill="#FFFFFF" stroke="${OL}" stroke-width="3"/><rect x="563" y="39" width="${334*bw}" height="24" rx="12" fill="${SUN}"/>`;
 s+=`<g opacity="${p}" transform="translate(${30*(1-p)} 0)"><text x="40" y="162" font-family="DM Serif Display" font-size="56" fill="${INDI}">${esc(name)}</text>`;
 if(!big){ s+=textLines(40,236,lines,50,62,PEN,'Caveat',700); }
 else { const A=D3.joeA, Bl=D3.joeB, y0=228, lh=58;
   const yb=y0+A.length*lh; s+=`<rect x="28" y="${yb-46}" width="${(TNW-56)*hl}" height="${Bl.length*lh+14}" rx="12" fill="${SUN}" opacity=".5"/>`;
   s+=textLines(40,y0,A,46,lh,PEN,'Caveat',700)+textLines(40,yb,Bl,46,lh,PEN,'Caveat',700); }
 s+=`</g>`;
 if(beat==3) s+=check(TNW-70,160,seg(lt,0.2,0.8));
 return s;}
function flyEnv4(lt){ if(lt<RS4-0.1||lt>RE4+0.4) return ''; let s='';
 for(let i=0;i<18;i++){ const a=RS4+i*(RE4-RS4)/18, k=seg(lt,a,a+0.35); if(k<=0||k>=1) continue;
   const x=TN_X+400+(770-TN_X-400)*E(k), y=TN_Y+60+(900-TN_Y-60)*E(k)-160*Math.sin(Math.PI*k);
   s+=`<g transform="translate(${x} ${y}) rotate(${-20+30*k})"><rect x="-90" y="-26" width="180" height="52" rx="6" fill="#FFFFFF" stroke="${OL}" stroke-width="3"/><path d="M-90 -26 L0 8 L90 -26" fill="none" stroke="${OL}" stroke-width="3"/></g>`; }
 return s;}
function thanksScene4(beat,lt,t,S){
 let s=''; s+=tableTop(1050);
 let done=0; if(beat==1){ if(lt>=T0) done=1; if(lt>=RS4) done=2+Math.min(18,Math.floor((lt-RS4)/(RE4-RS4)*18)); if(lt>=RE4) done=20; } else if(beat>=2) done=20;
 done=Math.min(done,20);
 s+=cardStack(90,840,20-done);
 s+=outTray(730,790,done,t);
 if(beat==1){ s+=giftList4(lt); s+=flyEnv4(lt); }
 s+=`<g transform="translate(${TN_X} ${TN_Y}) rotate(-0.8)">`+noteCard4(beat,lt,t,S.starts)+`</g>`;
 if(beat==3) s+=confetti(870,880,seg(lt,0.05,1.2),t);
 return s;}
SCENES.thanks4=thanksScene4;
"""

SPECS = {
    "thanks": dict(
        id="hb-reel-1106-thank-you-20", scene="thanks4", out=OUT3, music=LIB / "hb-x-future-easy.mp3",
        wall="linear-gradient(180deg,#C2BDF0 0%,#CFCDF5 30%,#E6DFF4 50%,#FFF8EF 54.6%,#FFF8EF 100%)",
        durs=[2.0, 5.5, 3.2, 3.9], follow_at=1.6, follow_y=724, chip_y=228, send_at=1.6,
        beats=[
            dict(kick="", head="Baby shower's over. / *20 notes left.*", fs=124),
            dict(kick="try this", head="Paste who gave what. / *AI drafts all 20.*", fs=112,
                 sub="Claude's real notes, shortened:"),
            dict(kick="every note is different", head="It names each gift / *and how you'll use it.*", fs=104),
            dict(kick="Do this:", head="Paste names and gifts. / *Ask for notes.*", fs=104,
                 sub="In ChatGPT, Claude or Gemini.<br>Edit before you send."),
        ],
        chip="Real Claude reply · names and gifts made up for this post",
    ),
}

D4T = dict(rosa=N3.wrap(ROSA, 54), sendAt=SPECS["thanks"]["send_at"])
B.JS = B.JS + JS_D2.replace("__D4T__", json.dumps(D4T, ensure_ascii=False))

# A and B scenes are appended below (JS_NOV04) once their runs are in.
try:
    import nov04_hourback_ab as AB  # noqa: E402
    B.JS = B.JS + AB.js(run_reply)
    SPECS.update(AB.specs(LIB, OUT4))
except ImportError:
    AB = None

B.SPECS = SPECS

# CD gate Nov 4: hook so the beat-1 subtitle hides while the prompt sticky shows; last draw() calls afterDraw()
_k = B.JS.rfind("f.style.opacity=fk;")
B.JS = B.JS[:_k] + "if(typeof afterDraw=='function') afterDraw(i,lt); " + B.JS[_k:]
_html1 = B.html


def _html4(spec, cover=False):
    """Nov 3 html() + (1) id="sub1" on the beat-1 subtitle (hidden while the prompt sticky shows) and (2) the
    'Real Claude reply' chip moved to the top band (y 228, right of the stamp; was ~82% height under the caption overlay)."""
    h = _html1(spec, cover)
    sub = spec["beats"][1].get("sub")
    if sub:
        h = re.sub(r'<div (style="position:absolute;left:80px;width:920px;top:\d+px;font:600 40px/1.25 Inter;text-align:center;color:#2A1D47">'
                   + re.escape(sub) + ")", r'<div id="sub1" \1', h, count=1)
    h = h.replace(f'left:0;right:0;top:{spec["chip_y"]}px;text-align:center', f'left:160px;right:30px;top:{spec["chip_y"]}px;text-align:center')
    return h


B.html = _html4
_render0 = B.render


def render(key):
    spec = SPECS[key]
    B.OUT = spec["out"]
    if key == "thanks":   # a paper slap on the send flip
        spec["sfx"] = [(sum(spec["durs"][:3]) + spec["send_at"], LIB / "sfx/sfx-x-paper-slap.mp3", 0.35)]
    return _render0(key)


if __name__ == "__main__":
    key = sys.argv[1]
    if "--still" in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index("--still") + 1].split(",")]
        print(B.stills(key, ts))
    elif "--full" in sys.argv:
        print(B.full(key, float(sys.argv[sys.argv.index("--full") + 1]), B.SCR / f"{key}-full.png"))
    elif "--cover-only" in sys.argv:
        import nov04_hourback_covers as CV
        print(CV.build(key))
    else:
        print(render(key))
        if key != "thanks":
            import nov04_hourback_covers as CV
            print(CV.build(key))

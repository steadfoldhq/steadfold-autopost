#!/usr/bin/env python3
"""Hourback Reels built Tue Nov 3 2026 by the Hourback maker (Social studio).

    python3 studio/editorial/nov03_hourback.py thanks|dinners              # mp4 + dedicated cover -> media/studio-nov03/hourback/
    python3 studio/editorial/nov03_hourback.py thanks --still 0,2.5,5       # stills sheet in the scratch dir (review)
    python3 studio/editorial/nov03_hourback.py thanks --cover-only

thanks  = hb-reel-1106-thank-you-20 (Fri Nov 6, 7 pm). Drawn desk: a stack of 20 blank cards ('20 to write'), an OUT tray
          ('mail today') and an empty note card with a 0-of-20 counter (= the number + deadline on frame 0). A made-up gift
          list flies into the card; Claude's REAL notes land one at a time (notes 1-2 shortened, marked …), then the counter
          runs to 20 of 20 as sealed envelopes fly to the tray (each riffle card shows the note's real first words). Beat 2 =
          note 3 (Grandpa Joe) word for word, its 'how we'll use it' sentence highlighted.
          Real run: studio/editorial/hb-nov03-run-thanks.txt.
dinners = hb-reel-1107-5-dinners (Sat Nov 7, 7 pm). Drawn kitchen wall: clock at 8:10 + 'store closes at 9' note, an empty
          grocery bag, a week card Mon-Fri. Claude's REAL 5 dinners land row by row (word for word, descriptions cut); beat 2
          walks its 'used more than once' lines (Chicken / Bell peppers / Black beans, word for word) and lights the rows.
          Real run: studio/editorial/hb-nov03-run-dinners.txt.

Extends studio/editorial/nov02_hourback.py (-> nov01 -> oct28 engine) by import: JS engine, html(), render(), stills().
New scenes are appended to the JS; module paths/specs are pointed at Nov 3. No shared kit or older script is edited.
Both Reels are standalone (no Part 2, no callback).
"""
import json
import re
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
sys.dont_write_bytecode = True
import nov02_hourback as N2  # noqa: E402

B = N2.B
B.OUT = REPO / "media/studio-nov03/hourback"
B.SCR = Path("/tmp/claude-0/nov03-hourback")
LIB = B.LIB


def run_reply(slug):
    t = (REPO / f"studio/editorial/hb-nov03-run-{slug}.txt").read_text()
    return t.split("===== REPLY (verbatim) =====\n", 1)[1]


def notes():
    """{n: (name, text)} parsed from the real thank-you run."""
    out = {}
    for m in re.finditer(r"\*\*(\d+)\. ([^*]+)\*\*\n(.+)", run_reply("thanks")):
        out[int(m.group(1))] = (m.group(2).strip(), m.group(3).strip())
    assert len(out) == 20, len(out)
    return out


def wrap(s, n):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    if len(lines) > 1 and lines[-1] in ("…", ". …"):
        last = lines.pop()
        lines[-1] += " " + last
    return [ln.replace("*", "") for ln in lines]   # markdown italics marker in the reply, not a character


def first_words(s, k):
    return " ".join(s.split()[:k]).rstrip(",.!") + "…"


N = notes()
SHOW = []   # (num, name, lines, full?)
# note 1 and 2: first sentence(s), shortened, marked …
r1 = N[1][1].split(". ")[0] + ". …"
p2 = N[2][1].split(" so we both")[0] + "…"
SHOW.append((1, N[1][0], wrap(r1, 50)))
SHOW.append((2, N[2][0], wrap(p2, 50)))
RIFF = [(k, N[k][0], wrap(re.split(r'(?<=[.!?]) ', N[k][1])[0] + ' …', 50)) for k in range(3, 21)]
JOE = N[3][1]
assert JOE.startswith("I can't believe how beautiful the rocking chair")
JOE_A, JOE_B = JOE.split(" It's going")
JOE_B = "It's going" + JOE_B
for s in (r1[:-2], p2[:-1], JOE):
    assert s.replace("…", "").strip(" .") in run_reply("thanks").replace("\n", " "), s

DAYS = []
for m in re.finditer(r"\d\. \*\*(Mon|Tue|Wed|Thu|Fri): ([^*]+)\*\*", run_reply("dinners")):
    DAYS.append((m.group(1), m.group(2).strip()))
assert len(DAYS) == 5, DAYS
REUSE = []
for nm in ("Chicken", "Bell peppers", "Black beans"):
    m = re.search(rf"- \*\*{nm}:\*\* ([^\n]+)", run_reply("dinners"))
    REUSE.append((nm, m.group(1).strip()))

DATA = dict(show=SHOW, riff=RIFF, joeA=wrap(JOE_A, 52), joeB=wrap(JOE_B, 52), days=DAYS, reuse=REUSE)

JS_NOV03 = r"""
// =============================================== Nov 3 data (parsed from the real runs at build time)
const D3=__DATA__;
// =============================================== scene: 20 thank-you notes, due today (Nov 6)
function cardStack(x,y,left){ // blank cards still to write; height follows the count
 const n=Math.max(1,Math.round(2+10*left/20)); let s='';
 for(let i=0;i<n;i++){const yy=-i*12, r=(i%3-1)*1.6; s+=`<g transform="translate(0 ${yy}) rotate(${r} 160 100)"><rect x="0" y="0" width="320" height="200" rx="10" fill="${i==n-1?'#FFFFFF':'#FFF3E6'}" ${o} stroke-width="4"/></g>`;}
 const ty=-n*12+14;
 s+=`<g transform="translate(0 ${ty})"><text x="160" y="88" text-anchor="middle" font-family="Caveat Brush" font-size="58" fill="${INDI}">Thank you</text>
   <path d="M60 130 H260 M60 160 H220" stroke="#D9D3F3" stroke-width="5" stroke-linecap="round"/></g>`;
 return `<g transform="translate(${x} ${y})"><ellipse cx="160" cy="212" rx="170" ry="14" fill="rgba(42,29,71,.14)"/>${s}
  <g transform="translate(338 ${ty+70}) rotate(6)"><rect x="5" y="7" width="190" height="78" rx="12" fill="rgba(42,29,71,.15)"/><rect width="190" height="78" rx="12" fill="${SUN}" ${o} stroke-width="4"/>
  <text x="95" y="54" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="36" fill="${INK}">${left} to write</text></g></g>`;}
function outTray(x,y,done,t){ // wire OUT tray, envelopes pile up
 let s=`<g transform="translate(${x} ${y})">`;
 s+=`<path d="M-10 150 H290 L270 200 H10Z" fill="#B9B4D8" ${o}/>`;
 const n=Math.min(done,20); for(let i=0;i<n;i++){const yy=140-i*5, r=((i*37)%7-3)*1.2; s+=`<g transform="translate(${30+(i%2)*8} ${yy}) rotate(${r} 110 0)"><rect x="0" y="-40" width="220" height="60" rx="6" fill="#FFFFFF" stroke="${OL}" stroke-width="3"/><path d="M0 -40 L110 -2 L220 -40" fill="none" stroke="${OL}" stroke-width="3"/></g>`;}
 s+=`<path d="M-10 150 V60 M290 150 V60" stroke="${OL}" stroke-width="6" stroke-linecap="round"/><path d="M-10 70 H290" stroke="${OL}" stroke-width="4" stroke-dasharray="10 8"/>`;
 s+=`<rect x="70" y="160" width="140" height="34" rx="8" fill="${CREAM}" stroke="${OL}" stroke-width="3"/><text x="140" y="186" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="24" fill="${INK}">OUT</text>`;
 s+=label(140,250,'mail today',-3,50,ACC,'middle');
 return s+`</g>`;}
const TN_X=70, TN_Y=1110, TNW=940, TNH=440;
function noteCard(beat,lt,t,st){ // the note card where Claude's notes land
 let s=`<rect x="12" y="16" width="${TNW}" height="${TNH}" rx="22" fill="rgba(42,29,71,.16)"/><rect x="0" y="0" width="${TNW}" height="${TNH}" rx="22" fill="#FFFFFF" ${o}/>`;
 s+=`<path d="M0 22 Q0 0 22 0 H${TNW-22} Q${TNW} 0 ${TNW} 22 V92 H0Z" fill="${PEACH}" ${o} stroke-width="4"/>`;
 // which note: k = index into a virtual sequence
 const RS=3.85, RE=5.25; // riffle window in beat 1 (s)
 let num=0, name='', lines=[], big=false, hl=0, fresh=0;
 if(beat==1){
   if(lt>=1.25){ num=1; name=D3.show[0][1]; lines=D3.show[0][2]; fresh=lt-1.25; }
   if(lt>=2.55){ num=2; name=D3.show[1][1]; lines=D3.show[1][2]; fresh=lt-2.55; }
   if(lt>=RS){ const k=Math.min(17,Math.floor((lt-RS)/(RE-RS)*18)); const r=D3.riff[k]; num=r[0]; name=r[1]; lines=r[2]; fresh=1; }
 } else if(beat>=2){ num=3; name="Grandpa Joe"; big=true; fresh=beat==2?lt:1; hl=beat==2?E(seg(lt,0.5,1.0)):1; }
 if(num==0){
   s+=`<text x="40" y="64" font-family="Poppins" font-weight="700" font-size="40" fill="${INK}">Note 0 of 20</text>`;
   const e=beat==0?1:1-seg(lt,0.9,1.2);
   s+=`<rect x="40" y="124" width="${TNW-80}" height="${TNH-164}" rx="16" fill="none" stroke="${INDI}" stroke-width="4" stroke-dasharray="14 14" opacity="${e*(0.55+0.35*Math.sin(t*5))}"/>`;
   s+=`<text x="${TNW/2}" y="${TNH/2+86}" text-anchor="middle" font-family="Caveat Brush" font-size="90" fill="${INDI}" opacity="${e*0.5}">Dear…</text>`;
   return s; }
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
function giftList(lt){ // the made-up gift list from the real prompt; flies into the card
 const k=E(seg(lt,0,0.12)), fl=seg(lt,0.9,1.25); if(fl>=1) return '';
 const tx=60+(TN_X+200-60)*E(fl), ty=712+(TN_Y+60-712)*E(fl), sc=1-0.72*E(fl);
 const inner=label(26,56,'gift list we made up for this post:',-2,44,ACC,'start')+textLines(26,122,["1. Aunt Rosa: a handmade quilt","2. Priya: a baby carrier","3. Grandpa Joe: a rocking chair he fixed up  … 20 in all"],46,54,OL,'Caveat',700);
 return `<g opacity="${k*(1-seg(fl,.8,1))}" transform="translate(${tx} ${ty}) scale(${sc})">`+sticky(0,0,900,282,-2,'#FFE7A0',inner,40*(1-k))+`</g>`;}
function flyEnv(lt){ // during the riffle, sealed envelopes fly from the card to the tray
 const RS=3.85, RE=5.25; if(lt<RS-0.1||lt>RE+0.4) return ''; let s='';
 for(let i=0;i<18;i++){ const a=RS+i*(RE-RS)/18, k=seg(lt,a,a+0.35); if(k<=0||k>=1) continue;
   const x=TN_X+400+(770-TN_X-400)*E(k), y=TN_Y+60+(900-TN_Y-60)*E(k)-160*Math.sin(Math.PI*k);
   s+=`<g transform="translate(${x} ${y}) rotate(${-20+30*k})"><rect x="-90" y="-26" width="180" height="52" rx="6" fill="#FFFFFF" stroke="${OL}" stroke-width="3"/><path d="M-90 -26 L0 8 L90 -26" fill="none" stroke="${OL}" stroke-width="3"/></g>`; }
 return s;}
function thanksScene(beat,lt,t,S){
 const st=S.starts; let s='';
 s+=tableTop(1050);
 // how many done (left/right counters)
 let done=0; if(beat==1){ if(lt>=2.55) done=1; if(lt>=3.85) done=2+Math.min(18,Math.floor((lt-3.85)/1.4*18)+0); if(lt>=5.25) done=20; } else if(beat>=2) done=20;
 done=Math.min(done,20);
 const showStack=!(beat==1&&lt<1.25)&&!(beat==2&&lt<0.1);
 s+=cardStack(90,840,20-done);
 s+=outTray(730,790,done,t);
 if(beat==1){ s+=giftList(lt); s+=flyEnv(lt); }
 s+=`<g transform="translate(${TN_X} ${TN_Y}) rotate(-0.8)">`+noteCard(beat,lt,t,st)+`</g>`;
 if(beat==3) s+=confetti(870,880,seg(lt,0.05,1.2),t);
 return s;}
SCENES.thanks=thanksScene;

// =============================================== scene: store closes at 9, plan 5 dinners (Nov 7)
function clock9(x,y,t){ const mm=10+t*0.4, m=mm/60*2*Math.PI, h=(8+mm/60)/12*2*Math.PI;
 let ticks=''; for(let i=0;i<12;i++){const a=i/12*2*Math.PI; ticks+=`<path d="M${62*Math.sin(a)} ${-62*Math.cos(a)} L${72*Math.sin(a)} ${-72*Math.cos(a)}" stroke="${OL}" stroke-width="${i%3?3:6}"/>`;}
 return `<g transform="translate(${x} ${y})"><circle r="92" fill="rgba(42,29,71,.14)" cx="6" cy="9"/><circle r="92" fill="#FFF8EF" ${o} stroke-width="7"/>${ticks}
  <path d="M0 0 L${40*Math.sin(h)} ${-40*Math.cos(h)}" stroke="${OL}" stroke-width="9" stroke-linecap="round"/>
  <path d="M0 0 L${66*Math.sin(m)} ${-66*Math.cos(m)}" stroke="${ACC}" stroke-width="6" stroke-linecap="round"/><circle r="8" fill="${OL}"/></g>`;}
function storeNote(x,y,glow){return `<g transform="translate(${x} ${y}) rotate(5)">${glow>0?`<circle cx="130" cy="70" r="${150+30*glow}" fill="url(#glow)" opacity="${0.8*glow}"/>`:''}
 <rect x="6" y="9" width="270" height="150" fill="rgba(42,29,71,.13)"/><rect width="270" height="150" fill="#FFE7A0" ${o} stroke-width="4"/>
 <text x="135" y="62" text-anchor="middle" font-family="Caveat Brush" font-size="48" fill="${INK}">store closes</text>
 <text x="135" y="124" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="52" fill="${ACC}">at 9 pm</text></g>`;}
const BAG={
 chicken:()=>`<rect x="-60" y="-34" width="120" height="68" rx="10" fill="#FFFFFF" ${o} stroke-width="4"/><ellipse cx="0" cy="0" rx="40" ry="20" fill="#F6B3A0" stroke="${OL}" stroke-width="3"/>`,
 pepper:()=>`<path d="M-34 -20 Q-44 40 0 46 Q44 40 34 -20 Q0 -36 -34 -20Z" fill="#E8453C" ${o} stroke-width="4"/><path d="M0 -30 q4 -18 16 -20" stroke="#2F7D4F" stroke-width="7" fill="none" stroke-linecap="round"/>`,
 beans:()=>`<rect x="-34" y="-44" width="68" height="88" rx="8" fill="${INDI}" ${o} stroke-width="4"/><rect x="-34" y="-14" width="68" height="30" fill="${SUN}" stroke="${OL}" stroke-width="3"/>`,
 rice:()=>`<path d="M-44 -56 H44 L52 56 H-52Z" fill="#FFF8EF" ${o} stroke-width="4"/><text x="0" y="12" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="24" fill="${INK}">RICE</text>`,
 tort:()=>`<ellipse cx="0" cy="0" rx="56" ry="18" fill="#F2D08F" ${o} stroke-width="4"/><ellipse cx="0" cy="-10" rx="56" ry="18" fill="#F5DCA3" ${o} stroke-width="4"/>`,
};
function groceryBag(x,y,fill,t){ // fill 0..5 items
 const IT=[['rice',-60,-60,-6],['chicken',40,-40,8],['pepper',-20,-90,-12],['beans',70,-80,10],['tort',0,-120,-4]];
 let s=`<g transform="translate(${x} ${y})"><ellipse cx="0" cy="150" rx="170" ry="14" fill="rgba(42,29,71,.14)"/>`;
 IT.forEach((it,i)=>{const k=E(seg(fill,i,i+0.6)); if(k<=0) return; s+=`<g transform="translate(${it[1]} ${it[2]-200*(1-k)}) rotate(${it[3]})" opacity="${k}">${BAG[it[0]]()}</g>`;});
 s+=`<path d="M-140 -10 L-120 150 H120 L140 -10Z" fill="#D9A867" ${o}/><path d="M-140 -10 H140" stroke="${OL}" stroke-width="5"/>
  <path d="M-110 20 L-100 120 M110 20 L100 120" stroke="#B98A4F" stroke-width="5" stroke-linecap="round"/>
  <text x="0" y="96" text-anchor="middle" font-family="Caveat Brush" font-size="46" fill="${INK}">groceries</text></g>`;
 return s;}
const WK_X=70, WK_Y=1100, WKW=940, WKH=470, ROWT=[1.25,1.95,2.65,3.35,4.05];
function weekCard(beat,lt,t,st){
 let s=`<rect x="12" y="16" width="${WKW}" height="${WKH}" rx="24" fill="rgba(42,29,71,.16)"/><rect x="0" y="0" width="${WKW}" height="${WKH}" rx="24" fill="#FFFFFF" ${o}/>`;
 let n=0; if(beat==1){ for(let i=0;i<5;i++) if(lt>=ROWT[i]) n=i+1; } else if(beat>=2) n=5;
 // header
 let rk=-1; if(beat==2){ rk=Math.min(2,Math.floor(Math.max(0,lt-0.15)/1.05)); }
 const used=rk>=0?D3.reuse[rk][1].split(',').map(x=>x.trim().slice(0,3)):[];
 if(rk<0) s+=`<text x="40" y="70" font-family="Poppins" font-weight="700" font-size="42" fill="${INK}">Dinners ${n} of 5</text>`;
 else { const p=E(seg(lt,0.15+rk*1.05,0.3+rk*1.05)); s+=`<g opacity="${p}"><rect x="24" y="18" width="${WKW-48}" height="72" rx="16" fill="${SUN}" opacity=".55"/>
   <text x="40" y="70" font-family="Poppins" font-weight="700" font-size="42" fill="${INK}">${esc(D3.reuse[rk][0])}: ${esc(D3.reuse[rk][1])}</text></g>`; }
 if(n==0){ s+=`<rect x="40" y="110" width="${WKW-80}" height="${WKH-150}" rx="16" fill="none" stroke="${INDI}" stroke-width="4" stroke-dasharray="14 14" opacity="${0.55+0.35*Math.sin(t*5)}"/>
   <text x="${WKW/2}" y="${WKH/2+70}" text-anchor="middle" font-family="DM Serif Display" font-size="100" fill="${INDI}" opacity=".5">?</text>`; return s; }
 for(let i=0;i<n;i++){ const d=D3.days[i], y=110+i*70, a=beat==1?st[1]+ROWT[i]:-9, p=E(seg(t,a,a+0.14));
   const on=used.includes(d[0]);
   if(on) s+=`<rect x="24" y="${y}" width="${WKW-48}" height="62" rx="14" fill="${PERI}" opacity=".9"/>`;
   s+=`<g opacity="${rk>=0&&!on?0.4:p}" transform="translate(${30*(1-p)} 0)"><rect x="40" y="${y+8}" width="104" height="48" rx="24" fill="${on?SUN:CREAM}" stroke="${OL}" stroke-width="3"/>
    <text x="92" y="${y+42}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="28" fill="${INK}">${d[0]}</text>
    <text x="168" y="${y+46}" font-family="DM Serif Display" font-size="44" fill="${INK}">${esc(d[1])}</text></g>`; }
 if(beat==3) s+=check(WKW-70,56,seg(lt,0.2,0.8));
 return s;}
function dinnerNote(lt){ // the made-up ask from the real prompt; flies into the card
 const k=E(seg(lt,0,0.12)), fl=seg(lt,0.85,1.2); if(fl>=1) return '';
 const tx=60+(WK_X+200-60)*E(fl), ty=736+(WK_Y+60-736)*E(fl), sc=1-0.72*E(fl);
 const inner=label(26,56,'what we told it (made up for this post):',-2,44,ACC,'start')+textLines(26,122,["5 weeknight dinners for 2 adults","each under 30 minutes, about $80 in total","share ingredients so nothing goes to waste"],44,56,OL,'Caveat',700);
 return `<g opacity="${k*(1-seg(fl,.8,1))}" transform="translate(${tx} ${ty}) scale(${sc})">`+sticky(0,0,900,280,-2,'#FFE7A0',inner,40*(1-k))+`</g>`;}
function dinnersScene(beat,lt,t,S){
 const st=S.starts; let s='';
 s+=tableTop(1050);
 const glow=beat==3?E(seg(lt,0.05,0.6)):0;
 s+=clock9(180,880,t)+storeNote(360,770,glow);
 s+=`<g transform="translate(${WK_X} ${WK_Y}) rotate(-0.8)">`+weekCard(beat,lt,t,st)+`</g>`;
 if(beat==3) s+=confetti(780,880,seg(lt,0.05,1.2),t);
 return s;}
SCENES.dinners=dinnersScene;
"""

B.JS = B.JS + JS_NOV03.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))

SPECS = {
    "thanks": dict(
        id="hb-reel-1106-thank-you-20", scene="thanks", music=LIB / "hb-x-future-easy.mp3",
        wall="linear-gradient(180deg,#C2BDF0 0%,#CFCDF5 30%,#E6DFF4 50%,#FFF8EF 54.6%,#FFF8EF 100%)",
        durs=[2.0, 6.0, 3.4, 3.2], follow_at=0.5, follow_y=724, chip_y=1572,
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
    "dinners": dict(
        id="hb-reel-1107-5-dinners", scene="dinners", music=LIB / "hb-x-ta-da-funk.mp3",
        wall="linear-gradient(180deg,#B9B4EE 0%,#C9CAF5 35%,#E6DFF4 50%,#FFF8EF 54.6%,#FFF8EF 100%)",
        durs=[2.0, 6.0, 3.4, 3.2], follow_at=0.5, follow_y=686, chip_y=1600,
        beats=[
            dict(kick="", head="Store closes at 9. / *5 dinners?*", fs=128),
            dict(kick="try this", head="AI plans 5 dinners / *and one shopping list.*", fs=104,
                 sub="Claude's real plan, shortened:"),
            dict(kick="it reuses ingredients", head="So less food / *goes to waste.*", fs=118,
                 sub="Its lines, word for word:"),
            dict(kick="Do this:", head="Ask for 5 dinners / *that share ingredients.*", fs=104,
                 sub="In ChatGPT, Claude or Gemini."),
        ],
        chip="Real Claude reply · plan made up for this post",
    ),
}
B.SPECS = SPECS

# the bag is drawn separately so it never sits under the week card (simple, readable)
B.JS = B.JS.replace("SCENES.dinners=dinnersScene;", r"""
const _dS=dinnersScene;
SCENES.dinners=(beat,lt,t,S)=>{ let fill=0; if(beat==1) fill=Math.max(0,(lt-1.4)/0.75); else if(beat>=2) fill=5;
  return _dS(beat,lt,t,S)+groceryBag(830,900,Math.min(5,fill),t)+(beat==1?dinnerNote(lt):''); };""")


if __name__ == "__main__":
    key = sys.argv[1]
    if "--still" in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index("--still") + 1].split(",")]
        print(B.stills(key, ts))
    elif "--full" in sys.argv:
        print(B.full(key, float(sys.argv[sys.argv.index("--full") + 1]), B.SCR / f"{key}-full.png"))
    elif "--cover-only" in sys.argv:
        import nov03_hourback_covers as CV
        print(CV.build(key))
    else:
        print(B.render(key))
        import nov03_hourback_covers as CV
        print(CV.build(key))

#!/usr/bin/env python3
"""Locked Hour, Nov 4 studio build (Social studio, Wed Nov 4 2026). Extends studio/editorial/nov03_lockedhour.py
(imported, not edited: its specs, scenes, covers and the nov02/nov01/oct28/oct27 kits are reused; this file appends its
own scenes to n1.JS_NOV at runtime and wraps k28.page to add the optional on-screen send line).

  send     lh-reel-1106-mix-3-kinds    (job D, SEND TEST) the Nov 3 Reel with ONE send line shown with the follow line
           on the last beat; everything else identical; overwrites media/studio-nov03/lockedhour/ (cover unchanged).
  (A/B/C are added below as they are built.)

  python3 studio/editorial/nov04_lockedhour.py send|... [--cover-only] [--still=0,1.5,3]
Music: existing LH v4 library tracks only (tools/music-library.json), loudnorm -14 LUFS. No new music. 1 render worker.
"""
import copy
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import edkit  # noqa: E402
import nov03_lockedhour as n3  # noqa: E402  (sets up n2/k27/k28/n1 and appends JS_NOV3)
k27, k28, n1, n2 = n3.k27, n3.k28, n3.n1, n3.n2

SCR = Path("/tmp/claude-0/nov04-lockedhour")
SCR.mkdir(parents=True, exist_ok=True)
k28.SCR = SCR
OUT = REPO / "media/studio-nov04/lockedhour"
OUT.mkdir(parents=True, exist_ok=True)
OUT_NOV3 = REPO / "media/studio-nov03/lockedhour"
CSS = k27.CSS
INK = "#141414"

_page_prev = k28.page  # nov02 page (gate-approved follow line)


def page(spec, cover_html=None):
    """Previous page() plus an optional send line inside the follow block, so it shows on the last beat together with
    the follow line (same fade-in, same ~2.3 s on screen). Only specs with send_line get it (clean send test)."""
    h = _page_prev(spec, cover_html)
    if spec.get("send_line"):
        anchor = "sleep or focus trick a day.</span>"
        assert h.count(anchor) == 1
        line = (f'<div style="margin-top:34px"><span style="display:inline-block;padding:10px 30px;border-radius:18px;'
                f'background:#FF5CA8;border:6px solid {INK};box-shadow:8px 8px 0 {INK};font:900 {spec.get("send_fs", 50)}px '
                f'\'Inter Display\';color:{INK};letter-spacing:-.01em;line-height:1.12;transform:rotate(-1.5deg);max-width:880px">'
                f'{spec["send_line"]}</span></div>')
        h = h.replace(anchor, anchor + line)
    return h


k28.page = page

JS_NOV4 = r"""
// ================= Nov 4 extras =================
// ---------- SCENE A: last coffee 9 hours before bed (a mug + a wall clock) ----------
const COF='#8A5A3B';
function mugD(x,y,s,t,steam,tea){ // pink mug (coffee) or cream cup with a tea tag (decaf/herbal)
 let g=sh(`<path d="M58 -30 q58 0 58 52 q0 52 -58 52" fill="none" stroke="${INK}" stroke-width="16" stroke-linecap="round"/>`,0);
 g+=sh(`<path d="M-80 -70 H70 V60 Q70 110 20 110 H-30 Q-80 110 -80 60Z" fill="${tea?CR:HP}" ${o}/>`,8);
 g+=`<ellipse cx="-5" cy="-70" rx="75" ry="16" fill="${tea?'#E9C46A':COF}" ${o}/>`;
 if(tea) g+=`<path d="M30 -70 V10" stroke="${INK}" stroke-width="4"/><rect x="12" y="10" width="40" height="44" rx="6" fill="${HY}" stroke="${INK}" stroke-width="5"/>`;
 if(steam>0){ for(let i=0;i<3;i++){const ph=(t*0.9+i/3)%1, xx=-40+i*36;
  g+=`<path d="M${xx} ${-100-60*ph} q-18 -24 0 -48 q18 -24 0 -48" fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round" opacity="${steam*Math.sin(Math.PI*ph)*0.8}"/>`;}}
 return `<g transform="translate(${x} ${y}) scale(${s})">${g}</g>`;}
function hA(h){return ((h%12)/12)*2*Math.PI;}
function pie(cx,cy,r,h0,h1,col){ if(h1<=h0+0.001) return ''; const a0=hA(h0), a1=a0+(h1-h0)/12*2*Math.PI;
 const x0=cx+r*Math.sin(a0), y0=cy-r*Math.cos(a0), x1=cx+r*Math.sin(a1), y1=cy-r*Math.cos(a1);
 return `<path d="M${cx} ${cy} L${x0} ${y0} A${r} ${r} 0 ${(h1-h0)>6?1:0} 1 ${x1} ${y1}Z" fill="${col}" opacity=".9"/>`;}
function wallClock(cx,cy,r,hand,h0,col,h1){ // h0..hand shaded; hour hand at 'hand' (hours, 14 = 2 pm)
 let s=sh(`<circle cx="${cx}" cy="${cy}" r="${r}" fill="${HY}" ${o}/>`,10);
 s+=`<circle cx="${cx}" cy="${cy}" r="${r-34}" fill="${CR}" stroke="${INK}" stroke-width="6"/>`;
 if(h0!=null) s+=pie(cx,cy,r-40,h0,h1==null?hand:h1,col||HPL);
 for(let k=0;k<12;k++){const a=k*Math.PI/6, r1=k%3?r-62:r-76, r2=r-44;
  s+=`<path d="M${cx+r1*Math.sin(a)} ${cy-r1*Math.cos(a)} L${cx+r2*Math.sin(a)} ${cy-r2*Math.cos(a)}" stroke="${INK}" stroke-width="${k%3?5:9}" stroke-linecap="round"/>`;}
 const ah=hA(hand), am=(hand%1)*2*Math.PI;
 s+=`<path d="M${cx} ${cy} L${cx+(r-120)*Math.sin(ah)} ${cy-(r-120)*Math.cos(ah)}" stroke="${INK}" stroke-width="16" stroke-linecap="round"/>`;
 s+=`<path d="M${cx} ${cy} L${cx+(r-70)*Math.sin(am)} ${cy-(r-70)*Math.cos(am)}" stroke="${INK}" stroke-width="9" stroke-linecap="round"/>`;
 s+=`<circle cx="${cx}" cy="${cy}" r="14" fill="${INK}"/>`;
 return s;}
const CX=540, CY=1250, CRAD=270;
function atClock(h,rr){const a=hA(h);return [CX+rr*Math.sin(a), CY-rr*Math.cos(a)];}
function coffeeClock(t,hand,h0,mugK,bedK,tea,h1){ let s=panel();
 s+=wallClock(CX,CY,CRAD,hand,h0,null,h1);
 const m=atClock(14,355), b=atClock(23,350);
 if(mugK>0) s+=mugD(m[0]+20,m[1]+10,0.62*pop(mugK),t,1,tea);
 if(bedK>0) s+=`<g transform="translate(${b[0]-10} ${b[1]+20}) scale(${0.52*pop(bedK)})">`+bedIcon(0,0,1)+`</g>`;
 return s;}
function sleepBars(t,t0){ let s='';
 const g1=EIO(seg(t,t0,t0+0.5)), g2=EIO(seg(t,t0+0.2,t0+0.7)), x0=170, Wd=740, cut=Wd*45/420;
 const row=(y,w,g,col,txt)=>`<text x="${x0}" y="${y-30}" font-family="Inter" font-weight="800" font-size="46" fill="${INK}">${txt}</text>`+
   sh(`<rect x="${x0}" y="${y}" width="${Math.max(1,w*g)}" height="110" rx="24" fill="${col}" ${o}/>`,9);
 s+=row(1130,Wd,g1,HY,'no caffeine');
 s+=row(1390,Wd-cut,g2,HP,'caffeine');
 if(g2>0.95){ const k=Q(t,t0+0.75);
  s+=`<rect x="${x0+Wd-cut+12}" y="1390" width="${cut-12}" height="110" rx="20" fill="none" stroke="${INK}" stroke-width="6" stroke-dasharray="16 12" opacity="${k}"/>`;
  s+=`<g opacity="${k}">`+pl(x0+Wd-cut/2,1600,'45 min less',56)+`</g>`;}
 s+=`<g transform="translate(${x0+270} 1352) scale(.36)">`+mugD(0,0,1,t,1,false)+`</g>`;
 return s;}
SC.coffee=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==0){ // the hand sweeps 2 pm -> 11 pm, the 9-hour wedge fills; mug at 2, bed at 11
  const k=EIO(seg(t,0.5,1.7)), hand=14+9*k;
  s+=coffeeClock(t,hand,14,1,seg(t,1.6,1.9),false);
  s+=`<g opacity="${t<0.5?1:1-Q(t,1.5)}">`+(t<1.6?pl(540,1640,'last coffee: 2 pm',54,INK):'')+`</g>`;
  if(t>1.7) s+=`<g opacity="${Q(t,1.7)}">`+pl(540,1640,'9 hours later: bed',54)+`</g>`;
  if(t>1.0){ const c=atClock(18.5,150); s+=`<text x="${c[0]}" y="${c[1]+20}" font-family="Inter Display" font-weight="900" font-size="74" fill="${INK}" text-anchor="middle" opacity="${Q(t,1.0)}">9 h</text>`; }
  return s;}
 if(ph==1){ // asleep… but the coffee is still working
  s+=bedScene(t,1,0,false);
  s+=sh(`<rect x="140" y="1050" width="330" height="22" rx="8" fill="${HPL}" ${o}/>`,6)+mugD(300,980,0.6,t,seg(t,3.0,3.4),false);
  s+=zz(560,1380,t,2.5);
  if(t<3.9) s+=`<g opacity="${Q(t,2.5)}">`+pl(680,1260,'asleep…',56,INK)+`</g>`;
  if(t>3.9) s+=`<g opacity="${Q(t,3.9)}">`+pl(680,1260,'but sleeping less',54)+`</g>`;
  if(t>4.3) s+=`<g opacity="${Q(t,4.3)}">`+pl(350,1140,'coffee: still working',46)+`</g>`;
  return s;}
 if(ph==2){ s+=sleepBars(t,5.65); return s;}
 if(ph==3){ // do this: count back 9 hours from bedtime; after 2 pm, decaf or herbal tea
  const k=EIO(seg(t,9.2,10.3)), hand=23-9*k;
  s+=coffeeClock(t,hand,hand,seg(t,10.2,10.5),1,false,23);
  if(t<10.4) s+=`<g opacity="${Q(t,9.1)}">`+pl(540,1660,'count back 9 hours',54,INK)+`</g>`;
  if(t>10.6){ s+=`<g opacity="${Q(t,10.6)}">`+pl(540,1660,'after 2 pm: decaf or herbal tea',50)+`</g>`;
   s+=mugD(225,1500,0.55*pop(seg(t,10.6,10.9)),t,1,true);}
  if(t>11.2) s+=check(800,1450,seg(t,11.2,11.6),44);
  return s;}
 s+=`<g transform="translate(540 1400) scale(.62) translate(-540 -1270)">`+coffeeClock(t,23,14,1,1,false)+`</g>`;
 return s;};

// ---------- SCENE B: flashcards, right 3 times (a card with tally marks) ----------
function fcard(x,y,rot,s,face,ticks,sx,dim){ sx=(sx==null?1:sx);
 let g=sh(`<rect x="-200" y="-130" width="400" height="260" rx="20" fill="${dim?'#E6DCCB':CR}" ${o}/>`,9);
 g+=`<path d="M-200 -70 H200" stroke="${HP}" stroke-width="5"/>`;
 if(face=='q') g+=`<text x="0" y="50" font-family="Inter Display" font-weight="900" font-size="120" fill="${INK}" text-anchor="middle">?</text>`;
 if(face=='a') g+=`<path d="M-150 0 H30 M-150 60 H-20" stroke="${INK}" stroke-width="12" stroke-linecap="round" opacity=".6"/>`;
 for(let i=0;i<(ticks||0);i++) g+=`<path d="M${88+i*36} -36 v110" stroke="${DP}" stroke-width="16" stroke-linecap="round"/>`;
 return `<g transform="translate(${x} ${y}) rotate(${rot||0}) scale(${s*sx} ${s})">${g}</g>`;}
function pileD(x,y,n,s,dim){let g='';for(let i=0;i<n;i++) g+=fcard(x+i*5,y-i*10,-3+i*1.5,s,'',0,1,dim);return g;}
function flipX(t,t0){const f=seg(t,t0,t0+0.3);return (f>0&&f<1)?Math.max(0.05,Math.abs(Math.cos(Math.PI*f))):1;}
SC.cards=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==0){ // one card: right once (tick), twice, three times -> into the done pile
  s+=panel();
  const n=t<0.6?1:t<1.1?2:3, go=EIO(seg(t,1.6,2.05));
  s+=pileD(300,1520,4,0.55,false)+label(300,1640,'to learn',-3,52,INK);
  s+=pileD(780,1520,go>0.99?1:0,0.55,false)+label(780,1640,'set aside',-3,56);
  s+=fcard(lerp(540,780,go),lerp(1120,1520,go),lerp(0,-3,go),lerp(1.15,0.55,go),'a',n);
  if(t<1.6) s+=pl(540,900,['','right once: keep it','right twice: keep it','right 3 times: set aside'][n],54,n==3?DP:INK);
  if(t>1.1) s+=check(850,1300,seg(t,1.1,1.4),44);
  if(t>2.0) s+=burst(780,1500,seg(t,2.0,2.35),HY);
  return s;}
 if(ph==1){ // right once and dropped -> forgotten (fades to grey, question mark)
  s+=panel();
  const go=EIO(seg(t,3.3,3.75)), fade=seg(t,3.9,4.4);
  s+=pileD(780,1520,1,0.55,false)+label(780,1640,'dropped',-3,52,INK);
  s+=fcard(lerp(400,780,go),lerp(1180,1500,go),0,lerp(1,0.55,go),fade>0.5?'q':'a',1,1,fade>0.5);
  if(t<3.8) s+=`<g opacity="${Q(t,2.5)}">`+pl(420,960,'right once… drop it?',52,INK)+`</g>`;
  if(t>4.0) s+=`<g opacity="${Q(t,4.0)}">`+pl(540,960,'later: forgotten',54)+`</g>`;
  if(t>4.6) s+=xmark(600,1500,44,seg(t,4.6,4.95));
  return s;}
 if(ph==2){ // research: 3 right tonight, then 3 later reviews
  s+=label(540,1000,'one card, over the weeks',-2,58);
  const days=['tonight','review 1','review 2','review 3'];
  for(let i=0;i<4;i++){ const k=pop(seg(t,5.7+i*0.35,6.0+i*0.35)); if(k<=0) continue;
   const x=210+i*220;
   s+=`<g transform="translate(${x} 1250) scale(${k})">`+fcard(0,0,-3+i*2,0.48,'a',i==0?3:1)+`</g>`;
   s+=`<text x="${x}" y="1410" font-family="Inter" font-weight="800" font-size="44" fill="${INK}" text-anchor="middle">${days[i]}</text>`;
   }
  if(t>7.0) s+=`<g opacity="${Q(t,7.0)}">`+label(540,1530,'each mark = one right answer',-2,52)+`</g>`;
  if(t>7.4) s+=`<g opacity="${Q(t,7.4)}">`+pl(540,1650,'tested 1 to 4 months later',52)+`</g>`;
  return s;}
 if(ph==3){ // do this: tally on the corner; wrong goes to the back of the pile
  s+=panel();
  const n=t<9.4?1:t<10.6?2:3, wr=seg(t,9.9,10.4), go=EIO(seg(t,11.0,11.4));
  s+=pileD(300,1520,3,0.55,false)+label(300,1640,'the pile',-3,52,INK);
  s+=pileD(780,1520,go>0.99?1:0,0.55,false)+label(780,1640,'set aside',-3,56);
  const wrongNow=wr>0&&wr<1;
  const cx=wrongNow?lerp(540,300,Math.sin(Math.PI*wr)):lerp(540,780,go), cy=wrongNow?lerp(1120,1400,Math.sin(Math.PI*wr)):lerp(1120,1520,go);
  s+=fcard(cx,cy,0,lerp(1.15,0.55,go),'a',n);
  if(wrongNow) s+=xmark(cx+160,cy-140,36,1);
  if(t<9.9) s+=pl(540,900,'tally marks on the corner',52,INK);
  else if(t<10.6) s+=pl(540,900,'wrong? back of the pile',52);
  else if(t<11.5) s+=pl(540,900,'3 tallies: set it aside',54);
  else s+=pl(540,900,'review again in a few days',52);
  if(t>11.4) s+=check(900,1300,seg(t,11.4,11.8),42);
  return s;}
 s+=`<g transform="translate(540 1400) scale(.62) translate(-540 -1270)">`+panel()+pileD(300,1520,3,0.55,false)+fcard(540,1120,0,1.15,'a',3)+pileD(780,1520,2,0.55,false)+`</g>`;
 return s;};
"""
n1.JS_NOV = n1.JS_NOV + JS_NOV4

# ------------------------------------------------------------------ job D: send test on the Fri Nov 6 Reel
SEND = copy.deepcopy(n3.SPECS["mix"])
SEND["send_line"] = "Send this to a friend with<br>a maths test this week."
SEND["follow_y"] = 700

def svg_cover(js_expr):
    return n1.svg_cover(js_expr)


def H_(text, size, field="dots"):
    return k28.H_(text, size, field)


# ------------------------------------------------------------------ covers (dedicated, style-menu layouts)
def cover_kinetic_coffee():
    """Style 5 kinetic big text (loud), the warm-shower cover layout: 'Bed at 11?' + 'Last coffee by' + a giant '2 pm' with a
    pink highlighter stripe, Caveat '9 hours before bed', the Reel's own drawn clock (2 pm -> 11 pm wedge) with mug and bed, stamp."""
    top = "<div style='position:absolute;left:90px;width:900px;top:140px'>" + H_("Bed at 11? / *Last coffee by*", 104, "dots") + "</div>"
    big = (f"<div style='position:absolute;left:0;right:0;top:380px;text-align:center'>"
           f"<div style='position:absolute;left:150px;right:150px;top:200px;height:110px;background:#FF5CA8;opacity:.85;border-radius:60px;transform:rotate(-2deg)'></div>"
           f"<div class='H' style='position:relative;font-size:330px;line-height:.9;letter-spacing:-.05em'>2 pm</div></div>")
    note = ("<div style=\"position:absolute;left:90px;width:900px;top:790px;text-align:center;font-family:'Caveat Brush';font-size:68px;"
            "color:#E8336F;transform:rotate(-3deg)\">that's 9 hours before bed ↓</div>")
    art = svg_cover("'<g transform=\"translate(540 1420) scale(.6) translate(-540 -1270)\">'+coffeeClock(0.4,23,14,1,1,false)+'</g>'")
    stamp = edkit.stamp("lockedhour", 70, 1210, size=150, rot=-12)
    return top + big + note + art + stamp


def cover_sticky_cards():
    """Style 13 sticky-note list (quiet), the Oct 28 layout: lined note card, red margin, tape, Caveat Brush title,
    ticked Caveat steps, on the LH pink dot grid, plus the Reel's drawn flashcard with 3 tally marks."""
    paper = "#FFFDF4"
    card = (f"<div style='position:absolute;left:110px;top:300px;width:860px;height:740px;background:{paper};transform:rotate(-2deg);"
            f"border:6px solid {INK};border-radius:10px;box-shadow:14px 14px 0 {INK};"
            f"background-image:linear-gradient({paper} 330px,transparent 330px),repeating-linear-gradient({paper} 0 118px,rgba(80,110,180,.30) 118px 121px)'>"
            f"<div style='position:absolute;left:96px;top:0;bottom:0;width:4px;background:rgba(220,80,80,.55)'></div>"
            f"<div style='position:absolute;left:130px;right:30px;top:50px;font-family:\"Caveat Brush\";font-size:104px;line-height:.98;color:#E8336F;white-space:nowrap'>"
            f"Got it right once?<br>Don't drop it yet.</div>"
            f"<ul style='position:absolute;left:130px;right:20px;top:330px;list-style:none;font-family:Caveat;font-weight:700;font-size:64px;line-height:120px;color:{INK};white-space:nowrap'>"
            f"<li><span style='color:#E8336F'>✓</span> right? tally on the corner</li><li><span style='color:#E8336F'>✓</span> 3 tallies: set it aside</li>"
            f"<li><span style='color:#E8336F'>✓</span> review it in a few days</li></ul></div>"
            f"<div style='position:absolute;left:420px;top:270px;width:240px;height:66px;background:rgba(255,212,59,.8);transform:rotate(3deg);border:2px solid rgba(27,23,23,.25)'></div>")
    art = svg_cover("fcard(560,1360,-5,1.05,'a',3)")
    stamp = edkit.stamp("lockedhour", 820, 1560, size=150, rot=-12)
    return card + art + stamp


def cover_page(kind):
    bg = {"kinetic": "#FFF0A6", "sticky": "#FFD5E5"}[kind]
    inner = {"kinetic": cover_kinetic_coffee, "sticky": cover_sticky_cards}[kind]()
    css = CSS.replace("background-color:#FFF0A6", f"background-color:{bg}", 1)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body><div id='bg'></div>"
            f"<script>{k27.JS}{k28.JS_EXTRA}{n1.JS_NOV}</script>{inner}</body></html>")


SPECS = {
    "coffee": dict(
        id="lh-reel-1108-coffee-9h", scene="coffee", music="media/music/library/v4/lh-x-phone-down.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.6], cover="kinetic", follow_y=720, stamp_xy=(70, 1390),
        hits=[(0.5, "sfx-x-swoosh-in", 0.2), (1.6, "sfx-x-sticker-pop", 0.3), (3.0, "sfx-x-swoosh-in", 0.15), (3.9, "sfx-x-sticker-pop", 0.25),
              (5.6, "sfx-x-whoosh-hit", 0.25), (6.4, "sfx-x-sticker-pop", 0.25), (9.2, "sfx-x-swoosh-in", 0.2), (10.6, "sfx-x-sticker-pop", 0.3),
              (11.2, "sfx-x-paper-slap", 0.22), (12.0, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(head="Bed at 11? / *Last coffee* / *by 2 pm.*", fs=136, top=270),
            dict(kick="the catch", head="It's still in you / *at bedtime.*", fs=112,
                 sub="You can fall asleep fine and still<br>sleep less, without noticing.", ss=44, bg2=True),
            dict(kick="the research", head="24 studies: caffeine cut sleep / by *45 minutes* on average.", fs=92,
                 sub="For a regular coffee, the cutoff<br>was about 9 hours before bed.", ss=44,
                 src="Gardiner et al. 2023 · Sleep Medicine Reviews"),
            dict(kick="Do this tomorrow:", head="Pick your bedtime. / *Count back 9 hours.*", fs=112,
                 sub="Bed at 11? Last coffee by 2 pm.<br>After that, decaf or herbal tea.", ss=44, bg2=True),
            dict(head="Bed at 11? / *Last coffee* / *by 2 pm.*", fs=124, top=270),
        ]),
    "cards": dict(
        id="lh-reel-1109-flashcards-3x", scene="cards", music="media/music/library/v4/lh-x-lock-in.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.6], cover="sticky", follow_y=640, stamp_xy=(70, 1390),
        hits=[(0.6, "sfx-x-sticker-pop", 0.25), (1.0, "sfx-x-sticker-pop", 0.25), (1.4, "sfx-x-sticker-pop", 0.3), (1.6, "sfx-x-swoosh-in", 0.2),
              (3.3, "sfx-x-swoosh-in", 0.2), (4.6, "sfx-x-paper-slap", 0.22), (5.6, "sfx-x-whoosh-hit", 0.25), (9.9, "sfx-x-swoosh-in", 0.2),
              (11.0, "sfx-x-paper-slap", 0.25), (11.4, "sfx-x-sticker-pop", 0.3), (12.0, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(head="Got it right once? / *Don't drop it yet.*", fs=124, top=300),
            dict(kick="the catch", head="Right once / *isn't learned yet.*", fs=118,
                 sub="Drop a card after one right answer<br>and you're more likely to forget it.", ss=44, bg2=True),
            dict(kick="the research", head="What worked: 3 right tonight, / then *3 reviews on later days.*", fs=92,
                 sub="The later reviews mattered most<br>on tests 1 to 4 months later.", ss=44,
                 src="Rawson & Dunlosky 2011 · J Exp Psychology: General"),
            dict(kick="Do this tonight:", head="Right 3 times? / *Set it aside.*", fs=118,
                 sub="Tally mark on the corner each time.<br>Then review the pile again in a few days.", ss=44, bg2=True),
            dict(head="Got it right once? / *Don't drop it yet.*", fs=124, top=300),
        ]),
}


def build(key, s, out_dir, cover_page=None):
    still = next((a[8:] for a in sys.argv if a.startswith("--still=")), None)
    if still:
        k28.render(s, key, still=[float(x) for x in still.split(",")]); print("stills", SCR / f"{key}-stills.jpg"); return
    if cover_page is not None:
        cov = out_dir / f"{s['id']}-cover.jpg"
        k28.render(s, key, cover_page=cover_page, cover_out=cov); print("cover", cov)
    if "--cover-only" in sys.argv:
        return
    fdir, total, starts = k28.render(s, key)
    out = out_dir / f"{s['id']}.mp4"
    k28.encode(fdir, total, s["music"], s["hits"], out)
    print(out, round(total, 2), starts)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    for key in args:
        if key == "send":  # cover unchanged (no follow/send line on it)
            build("send", SEND, OUT_NOV3)
        elif key == "oneword":
            import nov04_lockedhour_feed as fd_; fd_.oneword(); print("done oneword")
        else:
            build(key, SPECS[key], OUT, cover_page(SPECS[key]["cover"]))

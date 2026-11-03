#!/usr/bin/env python3
"""Locked Hour, Nov 3 studio build (Social studio, Tue Nov 3 2026). Extends studio/editorial/nov02_lockedhour.py
(imported, not edited: its page() with the gate-approved follow line, the nov01/oct28/oct27 kits and JS helpers are
reused; this file appends its own scenes to n1.JS_NOV at runtime). Every Reel is standalone: no sequel framing on screen.

  mix      lh-reel-1106-mix-3-kinds    Fri Nov 6 19:00 ET. Object: practice-problem cards, shuffled.
           Rohrer & Taylor 2007, Instructional Science 35:481-498 (doi 10.1007/s11251-007-9015-8);
           Brunmair & Richter 2019, Psychological Bulletin 145(11):1029-1052 (doi 10.1037/bul0000209).
  music    lh-reel-1107-calm-music-45  Sat Nov 7 19:00 ET. Object: a small speaker on the bedroom shelf.
           Harmat, Takacs & Bodizs 2008, J Adv Nursing 62(3):327-335; Jespersen et al. 2022, Cochrane CD010459.pub3.
  workout  lh-reel-1105-workout-1h     (desk order, job D) re-render of the Nov 2 Reel with the beat-2 kicker
           "sleep, part 2" -> "the catch"; everything else identical; overwrites media/studio-nov02/lockedhour/.
  oneword  lh-oneword-07               Fri Nov 6 17:00 ET, One Word No. 7 "Snooze." (nov03_lockedhour_feed.py).

  python3 studio/editorial/nov03_lockedhour.py mix|music|workout|oneword [--cover-only] [--still=0,1.5,3]
Music: existing LH v4 library tracks only (tools/music-library.json), loudnorm -14 LUFS. No new music. 1 render worker.
"""
import copy
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import edkit  # noqa: E402
import nov02_lockedhour as n2  # noqa: E402  (sets up k27/k28/n1 and appends JS_NOV2)
k27, k28, n1 = n2.k27, n2.k28, n2.n1

SCR = Path("/tmp/claude-0/nov03-lockedhour")
SCR.mkdir(parents=True, exist_ok=True)
k28.SCR = SCR  # render()/encode() read the module global at call time
OUT = REPO / "media/studio-nov03/lockedhour"
OUT.mkdir(parents=True, exist_ok=True)
OUT_NOV2 = REPO / "media/studio-nov02/lockedhour"
CSS = k27.CSS

JS_NOV3 = r"""
// ================= Nov 3 extras =================
// ---------- SCENE A: practice-problem cards (3 kinds) ----------
const KC=[HP,HY,SKY], KN=['A','B','C'];
function kIcon(kind,col){ if(kind==0) return `<path d="M0 -40 L44 34 H-44Z" fill="${col}" ${o}/>`;
 if(kind==1) return `<circle r="40" fill="${col}" ${o}/>`; return `<rect x="-38" y="-38" width="76" height="76" rx="6" fill="${col}" ${o}/>`;}
function pcard(x,y,kind,rot,s,sx){sx=(sx==null?1:sx);
 let g=sh(`<rect x="-80" y="-104" width="160" height="208" rx="16" fill="${CR}" ${o}/>`,8);
 g+=`<rect x="-80" y="-104" width="160" height="44" rx="16" fill="${KC[kind]}" stroke="${INK}" stroke-width="7"/>`;
 g+=`<g transform="translate(0 6) scale(.8)">`+kIcon(kind,KC[kind])+`</g>`;
 g+=`<path d="M-50 70 H10 M24 70 H50" stroke="${INK}" stroke-width="7" stroke-linecap="round" opacity=".55"/>`;
 return `<g transform="translate(${x} ${y}) rotate(${rot||0}) scale(${s*sx} ${s})">${g}</g>`;}
const GX=[300,540,780], GY=[1060,1300,1540];
const MIXED=[0,1,2,1,2,0,2,0,1];
function slotXY(i){return [GX[i%3],GY[Math.floor(i/3)]];}
function mixSlot(kind,j){let c=0;for(let i=0;i<9;i++){if(MIXED[i]==kind){if(c==j)return i;c++;}}return 0;}
function cardGrid(k,t0,s){ // k: 0 blocked (rows AAA/BBB/CCC) .. 1 mixed; cards travel on arcs, staggered
 let out='';const lay=[];
 for(let kind=0;kind<3;kind++) for(let j=0;j<3;j++){
  const a=slotXY(kind*3+j), b=slotXY(mixSlot(kind,j)); const d=(kind*3+j)*0.035;
  const p=EIO(cl((k-d)/(1-0.28),0,1)); const lift=-90*Math.sin(Math.PI*p);
  lay.push([p>0&&p<1?1:0, lerp(a[0],b[0],p), lerp(a[1],b[1],p)+lift, kind, 6*Math.sin(Math.PI*p)*(j%2?1:-1)]);}
 lay.sort((u,v)=>u[0]-v[0]);
 lay.forEach(c=>{out+=pcard(c[1],c[2],c[3],c[4],s||1);});
 return out;}
function panel(){return sh(`<rect x="110" y="820" width="860" height="880" rx="26" fill="${CR2}" ${o}/>`,12);}
function deskStudent(t,look,lid,smile){ // student at a desk looking at one card
 let s=panel();
 s+=sh(`<path d="M120 1580 H960 V1620 H120Z" fill="${HPL}" ${o}/>`,8);
 s+=`<g transform="translate(770 1330) scale(.72)">`+recol(face(0,0,1,lid,look,smile,t),'#7A4A2E','#8FC8EE')+`</g>`;
 return s;}
SC.mix=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==0){
  const k=seg(t,0.85,1.6);
  s+=panel();
  s+=cardGrid(k,0,1);
  if(t<0.85) s+=pl(540,900,'one kind at a time…',54,INK);
  if(t>1.6) s+=`<g opacity="${Q(t,1.6)}">`+pl(540,900,'mixed together',54)+`</g>`;
  s+=burst(780,1060,seg(t,1.6,2.1),HY);
  return s;}
 if(ph==1){ // which kind is this one? -> pick the method -> tick
  const f1=seg(t,3.1,3.4), f2=seg(t,3.9,4.2);
  const kind=t<3.25?0:(t<4.05?1:2);
  const sx=Math.max(0.05,Math.abs(Math.cos(Math.PI*(f1<1&&f1>0?f1:(f2<1&&f2>0?f2:0)))));
  s+=deskStudent(t,-0.6,0,t>4.5?0.7:0.0);
  s+=pcard(340,1320,kind,-4,1.55,sx);
  if(t<4.4) s+=`<g opacity="${Q(t,2.5)}">`+pl(540,930,'which kind is this one?',54,INK)+`</g>`;
  if(t>4.4) s+=`<g opacity="${Q(t,4.4)}">`+pl(540,930,'pick the method, then solve',54)+`</g>`;
  if(t>4.6) s+=check(560,1120,seg(t,4.6,5.0),44);
  return s;}
 if(ph==2){ // research bars: test a week later
  s+=label(540,1000,'the test, a week later',-2,62);
  const g1=EIO(seg(t,5.65,6.2)), g2=EIO(seg(t,5.85,6.6)), Hm=560;
  const bar=(x,v,g,c)=>sh(`<rect x="${x-120}" y="${1540-Hm*v*g}" width="240" height="${Hm*v*g}" rx="22" fill="${c}" ${o}/>`,9)+
   (g>0.9?`<text x="${x}" y="${1540-Hm*v-28}" font-family="Inter Display" font-weight="900" font-size="78" fill="${INK}" text-anchor="middle">${Math.round(v*100)}%</text>`:'');
  s+=`<path d="M150 1540 H930" stroke="${INK}" stroke-width="8" stroke-linecap="round"/>`;
  s+=bar(320,0.20,g1,'#E6DCCB')+bar(760,0.63,g2,HP);
  s+=`<text x="320" y="1610" font-family="Inter" font-weight="800" font-size="46" fill="${INK}" text-anchor="middle">one kind</text><text x="320" y="1662" font-family="Inter" font-weight="800" font-size="46" fill="${INK}" text-anchor="middle">at a time</text>`;
  s+=`<text x="760" y="1610" font-family="Inter" font-weight="800" font-size="46" fill="${INK}" text-anchor="middle">mixed</text>`;
  if(t>6.8) s+=`<g opacity="${Q(t,6.8)}">`+pl(320,1180,'felt easier',52,INK)+`</g>`;
  if(t>7.3) s+=check(920,1180,seg(t,7.3,7.7),40);
  return s;}
 if(ph==3){ // do this: deal from 3 chapter piles into one mixed set
  s+=panel();
  const PX=[280,540,800]; let dealt=0; for(let i=0;i<6;i++) if(t>=9.35+i*0.25) dealt++;
  for(let c=0;c<3;c++){ let gone=0; for(let i=0;i<dealt;i++) if(i%3==c) gone++;
   for(let j=0;j<3-gone;j++) s+=pcard(PX[c]+j*6,1060-j*8,c,-2+2*j,0.78);
   s+=`<text x="${PX[c]}" y="1220" font-family="Caveat Brush" font-size="54" fill="${INK}" text-anchor="middle">chapter ${4+c}</text>`;}
  // dealt cards fan out in a single pile
  for(let i=0;i<6;i++){ const st=9.35+i*0.25; if(t<st) break; const p=EIO(seg(t,st,st+0.25)), kind=i%3;
   const tx=330+i*76, ty=1470+(i%2?14:-6); s+=pcard(lerp(PX[kind],tx,p),lerp(1060,ty,p)-60*Math.sin(Math.PI*p),kind,lerp(0,-8+i*3,p),0.82);}
  if(t>10.95) s+=`<g opacity="${Q(t,10.95)}">`+pl(540,1660,'one mixed set',54)+`</g>`;
  if(t>11.2) s+=check(900,1300,seg(t,11.2,11.6),42);
  return s;}
 s+=`<g transform="translate(540 1400) scale(.62) translate(-540 -1270)">`+panel()+cardGrid(1,0,1)+`</g>`;
 return s;};

// ---------- SCENE B: calm music at bedtime (a small speaker on the shelf) ----------
function speakerD(x,y,s,on){const p=on?1+0.05*Math.max(0,Math.sin(T*9)):1;
 let g=sh(`<rect x="-90" y="-70" width="180" height="140" rx="26" fill="${HY}" ${o}/>`,8);
 g+=`<circle cx="-36" cy="0" r="${34*p}" fill="${CR}" stroke="${INK}" stroke-width="6"/><circle cx="-36" cy="0" r="12" fill="${INK}"/>`;
 g+=`<circle cx="44" cy="-26" r="12" fill="${on?HP:'#E6DCCB'}" stroke="${INK}" stroke-width="5"/><path d="M30 18 H62 M30 36 H62" stroke="${INK}" stroke-width="6" stroke-linecap="round"/>`;
 return `<g transform="translate(${x} ${y}) scale(${s})">${g}</g>`;}
function noteG(x,y,s,rot,col,op){return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})" opacity="${op}"><ellipse cx="0" cy="0" rx="20" ry="15" fill="${col}" stroke="${INK}" stroke-width="5" transform="rotate(-20)"/><path d="M17 -4 V-70 Q40 -60 46 -40" stroke="${INK}" stroke-width="7" fill="none" stroke-linecap="round"/></g>`;}
function notesFlow(x0,y0,x1,y1,t,k){if(k<=0) return '';let s='';
 for(let i=0;i<4;i++){const q=((t*0.32+i/4)%1); const x=lerp(x0,x1,q), y=lerp(y0,y1,q)-50*Math.sin(q*Math.PI*2+i);
  s+=noteG(x,y,1.25,-10+20*Math.sin(t*2+i),i%2?HP:CR,k*Math.min(1,4*q)*Math.min(1,4*(1-q)));}
 return s;}
function shelfSpeaker(on){return sh(`<rect x="140" y="1050" width="330" height="22" rx="8" fill="${HPL}" ${o}/>`,6)+speakerD(300,975,1.05,on);}
function musicRoom(t,lid,smile,awake,on,k){let s=n2_bed(t,lid,smile,awake);
 s+=shelfSpeaker(on); s+=notesFlow(420,960,640,1200,t,k); return s;}
function n2_bed(t,lid,smile,awake){return bedScene(t,lid,smile,awake);}
function calGrid(t,t0,t1){let s='';const n=21; const f=Math.floor(n*seg(t,t0,t1)+0.0001);
 for(let i=0;i<n;i++){const c=i%7, r=Math.floor(i/7), x=178+c*104, y=1060+r*104;
  s+=sh(`<rect x="${x}" y="${y}" width="90" height="90" rx="14" fill="${i<f?HY:CR}" stroke="${INK}" stroke-width="6"/>`,5);
  if(i<f) s+=noteG(x+40,y+62,0.55,-8,HP,1);}
 return s;}
function phoneTimer(x,y,sel,dim){let s=sh(`<rect x="${x-170}" y="${y-300}" width="340" height="600" rx="44" fill="${CR}" ${o}/>`,10);
 s+=`<rect x="${x-140}" y="${y-260}" width="280" height="520" rx="20" fill="${dim>0.5?'#4A3F78':'#FFFDF4'}" stroke="${INK}" stroke-width="5"/>`;
 if(dim<0.5){ s+=`<text x="${x}" y="${y-200}" font-family="Inter" font-weight="900" font-size="38" fill="${INK}" text-anchor="middle">Sleep timer</text>`;
  ['15 min','30 min','45 min','1 hour'].forEach((lb,i)=>{const yy=y-110+i*92, on=(i==2&&sel>0);
   s+=`<rect x="${x-118}" y="${yy-46}" width="236" height="72" rx="16" fill="${on?HP:'#F3EBDD'}" stroke="${INK}" stroke-width="${on?6:3}"/>`+
    `<text x="${x}" y="${yy+4}" font-family="Inter" font-weight="800" font-size="40" fill="${INK}" text-anchor="middle">${lb}</text>`;});
 } else s+=`<g transform="translate(${x} ${y-40}) scale(.5)">`+moonD(0,0,1)+`</g>`;
 return s;}
SC.music=function(t){
 let s='';
 const ph=t<2.4?0:t<5.6?1:t<9.0?2:t<12.0?3:4;
 if(ph==0){
  const on=t>0.8, k=seg(t,0.85,1.2), lid=EIO(seg(t,1.05,1.6));
  s+=musicRoom(t,lid,t>1.4?0.6:-0.3,t<0.8,on,k);
  s+=burst(300,975,seg(t,0.8,1.25),HP);
  if(t<0.8) s+=pl(640,1210,'still awake…',56,INK);
  if(t>1.25) s+=`<g opacity="${Q(t,1.25)}">`+pl(640,1210,'calm music, low volume',50)+`</g>`;
  if(t>1.7) s+=zz(560,1380,t,1.7);
  return s;}
 if(ph==1){ // every night: a 3-week calendar fills with music notes
  s+=panel();
  s+=label(540,1000,'every night, not just once',-2,58);
  s+=calGrid(t,2.6,4.8);
  s+=`<g transform="translate(470 1520) scale(.8)">`+bedIcon(0,0,1)+`</g>`;
  if(t>4.0) s+=zz(560,1460,t,4.0);
  if(t>4.9) s+=check(780,1500,seg(t,4.9,5.3),42);
  return s;}
 if(ph==2){ // research: nothing / audiobook / calm music -> sleep got better?
  s+=label(540,1000,'did sleep get better?',-2,62);
  const a=pop(seg(t,5.65,5.9)), b=pop(seg(t,5.85,6.1)), c=pop(seg(t,6.05,6.3));
  if(a>0) s+=`<g transform="translate(250 1260) scale(${a*0.85})">`+bedIcon(0,0,1)+`</g>`;
  if(b>0) s+=`<g transform="translate(540 1300) scale(${b})">`+bookOpen(0,0,1.15)+`</g>`;
  if(c>0) s+=speakerD(830,1240,0.9*c,true);
  const lab=(x,txt,k)=>k>0?`<text x="${x}" y="1420" font-family="Inter" font-weight="800" font-size="46" fill="${INK}" text-anchor="middle" opacity="${k}">${txt}</text>`:'';
  s+=lab(250,'nothing',Q(t,5.9))+lab(540,'audiobook',Q(t,6.1))+lab(830,'calm music',Q(t,6.3));
  if(t>6.6) s+=xmark(250,1540,40,seg(t,6.6,6.9));
  if(t>6.9) s+=xmark(540,1540,40,seg(t,6.9,7.2));
  if(t>7.2) s+=check(830,1540,seg(t,7.2,7.6),46);
  return s;}
 if(ph==3){ // do this: sleep timer 45 min, music plays, screen dims, sleep
  s+=panel();
  const sel=seg(t,9.5,9.6), dim=seg(t,10.7,10.8);
  s+=phoneTimer(360,1270,sel,dim);
  if(t>9.5) s+=`<g opacity="${Q(t,9.5)}">`+notesFlow(620,1180,900,900,t,1)+`</g>`;
  s+=speakerD(780,1450,0.85,t>9.6);
  if(t>9.6) s+=burst(560,1340,seg(t,9.6,10.0),HY);
  if(t>11.0) s+=check(905,1600,seg(t,11.0,11.4),44);
  return s;}
 s+=`<g transform="translate(540 1400) scale(.62) translate(-540 -1270)">`+musicRoom(t,1,0.6,false,true,1)+`</g>`;
 return s;};
"""
n1.JS_NOV = n1.JS_NOV + JS_NOV3


def svg_cover(js_expr):
    return n1.svg_cover(js_expr)


def H_(text, size, field="dots"):
    return k28.H_(text, size, field)


# ------------------------------------------------------------------ covers (dedicated, style-menu layouts)
def cover_compare_mix():
    """Style 8 original templates, compare (quiet): Inter Display hook with pill, two side-by-side panels of the Reel's
    drawn card grid ('one kind at a time' with an X, 'mixed' with a tick), Caveat labels + line, stamp. LH cream dot grid."""
    hook = "<div style='position:absolute;left:90px;width:900px;top:300px'>" + H_("Maths test coming up? / *Mix 3 kinds of problems.*", 112, "cream") + "</div>"
    note = ("<div style=\"position:absolute;left:90px;width:900px;top:560px;text-align:center;font-family:'Caveat Brush';font-size:62px;"
            "color:#E8336F;transform:rotate(-3deg)\">1 of each kind, then repeat ↓</div>")
    art = svg_cover("'<g transform=\"translate(30 790) scale(.5) translate(-110 -820)\">'+panel()+cardGrid(0,0,1)+'</g>'"
                    "+'<g transform=\"translate(560 790) scale(.5) translate(-110 -820)\">'+panel()+cardGrid(1,0,1)+'</g>'"
                    "+xmark(245,1290,40,1)+check(775,1290,1,44)"
                    "+label(245,1420,'one kind at a time',-3,56,INK)+label(775,1420,'mixed',-3,62)")
    stamp = edkit.stamp("lockedhour", 820, 1440, size=150, rot=-12)
    return hook + note + art + stamp


def cover_lookb_music():
    """Style 1 Look B big-headline (loud) in the LH zine look, gate rev 2 (Nov 3 CD): Inter Display 900 hook >=120 px
    in 3 lines with pink pills, Caveat Brush save-line + arrow, the Reel's own bedroom scene (bed + shelf speaker + notes)
    large and centred as the one object, round stamp tucked on the scene's top-right corner. On the LH pink dot grid."""
    hook = "<div style='position:absolute;left:90px;width:900px;top:280px'>" + H_("Can't switch off? / *45 minutes* / *of calm music.*", 136, "pink") + "</div>"
    save = ("<div style=\"position:absolute;left:90px;width:900px;top:735px;text-align:center;font-family:'Caveat Brush';font-size:68px;"
            "color:#E8336F;transform:rotate(-3deg)\">set a sleep timer tonight ↓</div>")
    art = svg_cover("'<g transform=\"translate(540 1248) scale(.9) translate(-540 -1260)\">'+musicRoom(0.9,1,0.6,false,true,1)+'</g>'")
    stamp = edkit.stamp("lockedhour", 830, 1470, size=160, rot=-12)
    return hook + save + art + stamp


def cover_page(kind):
    bg = {"compare": "#FFF6E5", "lookb": "#FFD5E5"}[kind]
    inner = {"compare": cover_compare_mix, "lookb": cover_lookb_music}[kind]()
    css = CSS.replace("background-color:#FFF0A6", f"background-color:{bg}", 1)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body><div id='bg'></div>"
            f"<script>{k27.JS}{k28.JS_EXTRA}{n1.JS_NOV}</script>{inner}</body></html>")


# ------------------------------------------------------------------ specs
WORKOUT = copy.deepcopy(n2.SPECS["workout"])
assert WORKOUT["beats"][1]["kick"] == "sleep, part 2"
WORKOUT["beats"][1]["kick"] = "the catch"  # desk order Nov 3: no sequel framing on screen

SPECS = {
    "mix": dict(
        id="lh-reel-1106-mix-3-kinds", scene="mix", music="media/music/library/v4/lh-x-tick-boom.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.6], cover="compare", follow_y=700, stamp_xy=(70, 1390),
        hits=[(0.85, "sfx-x-swoosh-in", 0.3), (1.6, "sfx-x-sticker-pop", 0.35), (3.1, "sfx-x-swoosh-in", 0.2), (4.6, "sfx-x-sticker-pop", 0.3),
              (5.6, "sfx-x-whoosh-hit", 0.25), (9.35, "sfx-x-paper-slap", 0.22), (10.1, "sfx-x-paper-slap", 0.22), (11.2, "sfx-x-sticker-pop", 0.3),
              (12.0, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(kick="Maths test coming up?", ks=76, head="Mix 3 kinds / *of problems.*", fs=136, top=290),
            dict(kick="try this", head="It feels harder. / *You remember more.*", fs=112,
                 sub="Mixed up, you have to pick the method<br>each time, just like on the real test.", ss=44, bg2=True),
            dict(kick="the research", head="A week later, mixed practice / scored *63% vs 20%.*", fs=96,
                 sub="against doing one kind at a time,<br>even though it felt harder while practising.", ss=44,
                 src="Rohrer & Taylor 2007 · Instructional Science"),
            dict(kick="Do this tonight:", head="1 of each kind, / *then repeat.*", fs=124,
                 sub="Take problems from your last 3 chapters<br>and shuffle them into one set.", ss=44, bg2=True),
            dict(kick="Maths test coming up?", ks=76, head="Mix 3 kinds / *of problems.*", fs=136, top=290),
        ]),
    "music": dict(
        id="lh-reel-1107-calm-music-45", scene="music", music="media/music/library/v4/lh-x-phone-down.mp3",
        durs=[2.4, 3.2, 3.4, 3.0, 2.6], cover="lookb", follow_y=730, stamp_xy=(70, 1390),
        hits=[(0.8, "sfx-x-sticker-pop", 0.3), (2.6, "sfx-x-swoosh-in", 0.2), (4.9, "sfx-x-sticker-pop", 0.3),
              (5.6, "sfx-x-whoosh-hit", 0.25), (7.2, "sfx-x-sticker-pop", 0.3), (9.5, "sfx-x-sticker-pop", 0.3), (11.0, "sfx-x-paper-slap", 0.25),
              (12.0, "sfx-x-paper-slap", 0.3)],
        beats=[
            dict(head="Can't switch off? / *45 minutes* / *of calm music.*", fs=124, top=270),
            dict(kick="try this", head="Calm music can help / *you sleep better.*", fs=112,
                 sub="Play it every night for a few weeks,<br>not just once. Quiet and slow.", ss=44, bg2=True),
            dict(kick="the research", head="94 students, 3 weeks: / music helped. *An audiobook didn't.*", fs=92,
                 sub="45 minutes of calm classical music<br>at bedtime, every night.", ss=44,
                 src="Harmat et al. 2008 · J Adv Nursing"),
            dict(kick="Do this tonight:", head="Calm playlist on. / *Sleep timer: 45 minutes.*", fs=110,
                 sub="Spotify: tap ••• on the song,<br>then Sleep timer, then 45 minutes.", ss=44, bg2=True),
            dict(head="Can't switch off? / *45 minutes* / *of calm music.*", fs=124, top=270),
        ]),
}

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    still = next((a[8:] for a in sys.argv if a.startswith("--still=")), None)
    for key in args or list(SPECS):
        if key == "oneword":
            import nov03_lockedhour_feed as fd_; fd_.oneword(); print("done oneword"); continue
        if key == "workout":  # job D: same spec, new kicker; keep the existing dedicated cover (it has no kicker)
            s, out_dir = WORKOUT, OUT_NOV2
        else:
            s, out_dir = SPECS[key], OUT
        if still:
            k28.render(s, key, still=[float(x) for x in still.split(",")]); print("stills", SCR / f"{key}-stills.jpg"); continue
        if key != "workout":
            cov = out_dir / f"{s['id']}-cover.jpg"
            k28.render(s, key, cover_page=cover_page(s["cover"]), cover_out=cov)
            print("cover", cov)
        if "--cover-only" in sys.argv:
            continue
        fdir, total, starts = k28.render(s, key)
        out = out_dir / f"{s['id']}.mp4"
        k28.encode(fdir, total, s["music"], s["hits"], out)
        print(out, round(total, 2), starts)

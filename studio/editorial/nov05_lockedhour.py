#!/usr/bin/env python3
"""Locked Hour, Nov 5 studio build (Social studio, Thu Nov 5 2026). Extends studio/editorial/nov04_lockedhour.py
(imported, not edited: its page()/render()/encode() chain from the nov03/nov02/nov01/oct28/oct27 kits is reused; this file
appends its own scene to n1.JS_NOV at runtime).

  book     lh-reel-1110-questions-first   Tue Nov 10 19:00 ET. Object: an open textbook at its end-of-chapter questions page.
           NEW scene composition (CD Nov 4, template sameness): no framed square panel; the book is drawn full-bleed and
           bleeds off both sides, seen from above, with page-turn transitions and a pencil; the end beat closes the book.
           St. Hilaire, Chan & Ahn 2024, Psychonomic Bulletin & Review 31:411-441 (doi 10.3758/s13423-023-02353-8);
           Pan & Carpenter 2023, Educational Psychology Review (doi 10.1007/s10648-023-09814-5);
           Richland, Kornell & Kao 2009, J Exp Psychol: Applied 15(3):243-257 (doi 10.1037/a0016496).
  oneword  lh-oneword-09                  Wed Nov 11 17:00 ET, One Word No. 9 "Skip." (nov05_lockedhour_feed.py).

  python3 studio/editorial/nov05_lockedhour.py book|oneword [--cover-only] [--still=0,1.5,3]
Music: existing LH v4 library track only (tools/music-library.json), loudnorm -14 LUFS. No new music. 1 render worker.
"""
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import edkit  # noqa: E402
import nov04_lockedhour as n4  # noqa: E402  (sets up n3/n2/k27/k28/n1, page() wrapper, JS_NOV4)
k27, k28, n1 = n4.k27, n4.k28, n4.n1

SCR = Path("/tmp/claude-0/nov05-lockedhour")
SCR.mkdir(parents=True, exist_ok=True)
k28.SCR = SCR
OUT = REPO / "media/studio-nov05/lockedhour"
OUT.mkdir(parents=True, exist_ok=True)
CSS = k27.CSS
INK = "#141414"

JS_NOV5 = r"""
// ================= Nov 5 extras =================
// ---------- SCENE: questions first (an open textbook, full-bleed, seen from above) ----------
const LINEC='#CFC6B6';
function textRows(x0,x1,y0,n,gap,seed){let s='';for(let i=0;i<n;i++){const w=(x1-x0)*(0.72+0.28*Math.abs(Math.sin(seed+i*1.7)));
 s+=`<rect x="${x0}" y="${y0+i*gap}" width="${i%6==5?w*0.5:w}" height="13" rx="6.5" fill="${LINEC}"/>`;}return s;}
function pageL(content){return `<path d="M0 -350 Q-250 -385 -505 -352 V352 Q-250 322 0 350Z" fill="${CR}" ${o}/>`+content;}
function pageR(content){return `<path d="M0 -350 Q250 -385 505 -352 V352 Q250 322 0 350Z" fill="${CR}" ${o}/>`+content;}
function scrib(x,y,len,k,col){ // a handwritten guess as a pencil scribble, drawn left to right
 if(k<=0) return ''; let d=`M${x} ${y}`; const n=Math.round(len/26);
 for(let i=0;i<n;i++){const yy=(i%2?-1:1)*(8+5*Math.sin(i*2.3)); d+=` q13 ${yy*-2} 26 0`;}
 return `<path d="${d}" fill="none" stroke="${col||'#5A5250'}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="${len*1.6}" stroke-dashoffset="${len*1.6*(1-k)}"/>`;}
const QY=i=>-205+i*112, GLEN=[230,180,260,200,240];
function qPage(g,ticks){ // right page: 'Questions', 5 numbered rows; g[i] = guess written 0..1; ticks[i] = checked 0..1
 let c=`<text x="60" y="-262" font-family="Inter Display" font-weight="900" font-size="54" fill="${INK}">Questions</text>`;
 c+=`<rect x="56" y="-252" width="262" height="16" rx="8" fill="${HP}" opacity=".55"/>`;
 for(let i=0;i<5;i++){const y=QY(i);
  c+=`<circle cx="92" cy="${y}" r="30" fill="${HY}" stroke="${INK}" stroke-width="5"/><text x="92" y="${y+14}" font-family="Inter" font-weight="900" font-size="38" fill="${INK}" text-anchor="middle">${i+1}</text>`;
  c+=`<rect x="140" y="${y-24}" width="${300-30*(i%2)}" height="12" rx="6" fill="${LINEC}"/><rect x="140" y="${y-4}" width="${190+20*(i%3)}" height="12" rx="6" fill="${LINEC}"/>`;
  c+=scrib(146,y+40,GLEN[i],g[i]);
  if(ticks&&ticks[i]>0) c+=`<g transform="translate(450 ${y+20}) scale(${pop(ticks[i])})"><path d="M-22 0 l14 16 l30 -34" stroke="${DP}" stroke-width="11" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>`;}
 return c;}
function chapterPage(side,seed){return side<0?textRows(-460,-50,-300,16,40,seed):textRows(50,460,-300,16,40,seed);}
function flipPage(k,frontR,backL){ // one page turning from right to left around the spine, k 0..1
 if(k<=0||k>=1) return ''; const c=Math.cos(Math.PI*k), lift=Math.sin(Math.PI*k);
 const shade=`<path d="M0 -350 Q250 -385 505 -352 V352 Q250 322 0 350Z" fill="${INK}" opacity="${0.10*lift}"/>`;
 return `<g transform="scale(${c} 1) translate(0 ${-14*lift})">`+pageR(c>0?frontR:'')+(c<0?`<g transform="scale(-1 1)">${backL||''}</g>`:'')+shade+`</g>`;}
function bookD(cx,cy,s,rot,L,R,flip){ // L/R page contents; flip = [k, frontR, backL]
 let g=sh(`<rect x="-530" y="-380" width="1060" height="760" rx="26" fill="${HP}" ${o}/>`,14);
 g+=`<path d="M-505 352 V364 Q-250 334 0 362 Q250 334 505 364 V352" fill="${CR2}" ${o}/>`;
 g+=pageL(L)+pageR(R);
 g+=`<rect x="-34" y="-356" width="68" height="708" fill="${INK}" opacity=".07"/><path d="M0 -350 V350" stroke="${INK}" stroke-width="5"/>`;
 if(flip) g+=flipPage(flip[0],flip[1],flip[2]);
 return `<g transform="translate(${cx} ${cy}) rotate(${rot}) scale(${s})">${g}</g>`;}
function pencilD(x,y,rot,s){ // tip at (x,y)
 const g=sh(`<path d="M0 0 L-22 -62 H22Z" fill="#F3D9B1" ${o}/><rect x="-22" y="-330" width="44" height="268" fill="${HY}" ${o}/>`+
  `<rect x="-24" y="-366" width="48" height="38" fill="${GREY}" ${o}/><rect x="-24" y="-420" width="48" height="56" rx="14" fill="${HPL}" ${o}/>`,9)+
  `<path d="M0 0 L-7 -20 H7Z" fill="${INK}"/><path d="M-7 -320 V-70 M7 -320 V-70" stroke="${INK}" stroke-width="3" opacity=".35"/>`;
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">${g}</g>`;}
function noteD(x,y,rot,s,xk,tk){ // sticky note with a guess scribble; xk = wrong X, tk = ticked after reading
 let g=sh(`<rect x="-150" y="-120" width="300" height="240" rx="10" fill="${HY}" ${o}/>`,9)+`<rect x="-60" y="-138" width="120" height="36" fill="rgba(255,255,255,.65)" stroke="rgba(20,20,20,.25)" stroke-width="2"/>`;
 g+=scrib(-110,-30,200,1)+scrib(-110,40,140,1);
 if(xk>0) g+=xmark(80,-50,34,xk);
 if(tk>0) g+=`<g transform="translate(90 70) scale(${pop(tk)})">`+`<circle r="40" fill="${HP}" ${o}/><path d="M-18 0 l12 14 l26 -30" stroke="${INK}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>`;
 return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">${g}</g>`;}
const BX=430;
const G5=(t,t0,d)=>[0,1,2,3,4].map(i=>seg(t,t0+i*d,t0+(i+0.85)*d));
SC.book=function(t){
 let s='';
 const S0=SPEC.starts, b1=S0[1], b2=S0[2], b3=S0[3];
 if(t<b1){ // HOOK: the questions page, guesses going in one by one (rows 1-2 already written at frame 0)
  const g=[1,1,seg(t,0.15,0.6),seg(t,0.65,1.1),seg(t,1.15,1.6)], row=t<0.6?2:t<1.1?3:4, k=seg(t,[0.15,0.65,1.15][row-2],[0.6,1.1,1.6][row-2]);
  const cam=1.18+0.03*EIO(seg(t,0,b1));
  s+=bookD(BX,1380,cam,-3,textRows(-460,-50,-300,16,40,1.3),qPage(g,null));
  const px=BX+cam*(146+GLEN[row]*Math.min(1,k)+10), py=1380+cam*(QY(row)+40)-12+6*Math.sin(t*40);
  s+=pencilD(t<1.7?px:lerp(px,880,EIO(seg(t,1.7,2.2))),t<1.7?py:lerp(py,1080,EIO(seg(t,1.7,2.2))),32,1);
  return s;}
 if(t<b2){ // PAYOFF: flip back to the chapter; one line gets highlighted; the wrong guess gets the real answer
  const f1=seg(t,b1+0.05,b1+0.45), f2=seg(t,b1+0.3,b1+0.7);
  const hk=EIO(seg(t,b1+0.9,b1+1.5)), yy=1420;
  let R=chapterPage(1,4.1);
  R+=`<rect x="44" y="${-300+40*6-10}" width="${430*hk}" height="34" rx="10" fill="${HY}" opacity=".8"/>`;
  s+=bookD(540,yy,1.18,-2,(t<b1+0.45?textRows(-460,-50,-300,16,40,1.3):chapterPage(-1,2.2)),R,
     f1<1?[f1,qPage([1,1,1,1,1],null),chapterPage(-1,2.2)]:(f2<1?[f2,chapterPage(1,3.3),chapterPage(-1,2.2)]:null));
  s+=noteD(290,1250,-6,0.9*pop(seg(t,b1+0.6,b1+0.95)),seg(t,b1+1.0,b1+1.35),seg(t,b1+2.0,b1+2.3));
  if(t>b1+1.0&&t<b1+2.0) s+=`<g opacity="${Q(t,b1+1.0)}">`+pl(340,860,'my guess: wrong',66,INK)+`</g>`;
  if(t>b1+2.0) s+=`<g opacity="${Q(t,b1+2.0)}">`+pl(480,860,'then I read it: it sticks',62)+`</g>`;
  if(t>b1+1.6){ const ak=E(seg(t,b1+1.6,b1+2.0)); // arrow from the highlighted line to the note
   s+=`<path d="M${820} ${1330} Q${640} ${1160} ${lerp(820,450,ak)} ${lerp(1330,1230,ak)}" fill="none" stroke="${DP}" stroke-width="10" stroke-linecap="round" stroke-dasharray="${600}" stroke-dashoffset="${600*(1-ak)}"/>`;}
  s+=burst(420,1300,seg(t,b1+2.0,b1+2.4),HP);
  return s;}
 if(t<b3){ // DO THIS: turn to the end, guess all 5, then read and tick each one
  const f1=seg(t,b2+0.05,b2+0.4), f2=seg(t,b2+0.25,b2+0.6);
  const g=G5(t,b2+0.8,0.34), tk=G5(t,b2+2.7,0.22);
  s+=bookD(BX,1400,1.18,-3,textRows(-460,-50,-300,16,40,1.3),qPage(g,tk));
  if(t<b2+0.7){ // the turning pages (backwards: from left to right) covering the right page
   const k=Math.max(f1,f2); s=bookD(BX,1400,1.18,-3,textRows(-460,-50,-300,16,40,1.3),(t<b2+0.25?chapterPage(1,4.1):qPage([0,0,0,0,0],null)),[1-k,qPage([0,0,0,0,0],null),chapterPage(-1,2.2)]);}
  let row=0; for(let i=0;i<5;i++) if(g[i]>0) row=i;
  if(t>b2+0.7&&t<b2+2.6){ const px=BX+1.18*(146+GLEN[row]*Math.min(1,g[row])+10), py=1400+1.18*(QY(row)+40)-12+6*Math.sin(t*40); s+=pencilD(px,py,32,1);}
  if(t>b2+0.8&&t<b2+2.6) s+=`<g opacity="${Q(t,b2+0.8)}">`+pl(560,850,'guess all 5, right or wrong',52,INK)+`</g>`;
  if(t>b2+2.6) s+=`<g opacity="${Q(t,b2+2.6)}">`+pl(560,850,'tick each answer you find',56)+`</g>`;
   return s;}
 // END: the book, all 5 guessed and ticked, settles small under the follow line
 const k=EIO(seg(t,b3,b3+0.45));
 s+=bookD(lerp(BX,540,k),lerp(1400,1420,k),lerp(1.18,0.74,k),-3,textRows(-460,-50,-300,16,40,1.3),qPage([1,1,1,1,1],[1,1,1,1,1]));
 return s;};
"""
n1.JS_NOV = n1.JS_NOV + JS_NOV5


def H_(text, size, field="dots"):
    return k28.H_(text, size, field)


def cover_lookb_book():
    """Style 1 Look B big-headline cover (loud) on the LH CREAM dot grid: Inter Display 900 hook with pink highlighter pills,
    Caveat Brush save-line + arrow, the Reel's own drawn book (questions page, 5 guesses, pencil), round stamp.
    Not kinetic (Nov 8) and not the taped lined note (Nov 9); Look B last used Nov 7 on pink."""
    kick = ("<div style=\"position:absolute;left:90px;width:900px;top:320px;text-align:center;font-family:'Caveat Brush';font-size:84px;"
            "color:#E8336F;line-height:1\">Reading tonight?</div>")
    hook = "<div style='position:absolute;left:90px;width:900px;top:360px'>" + H_("Guess 5 answers. / *Then read.*", 156, "dots") + "</div>"
    save = ("<div style=\"position:absolute;left:90px;width:900px;top:700px;text-align:center;font-family:'Caveat Brush';font-size:66px;"
            "color:#E8336F;transform:rotate(-3deg)\">even wrong guesses help ↓</div>")
    art = n1.svg_cover("bookD(470,1200,0.86,-3,textRows(-460,-50,-300,16,40,1.3),qPage([1,1,1,1,0.55],null))+pencilD(470+0.86*(146+240*0.55+10),1200+0.86*(QY(4)+40)-12,32,0.88)")
    stamp = edkit.stamp("lockedhour", 840, 1530, size=140, rot=-12)
    return hook + save + art + stamp


def cover_page():
    css = CSS.replace("background-color:#FFF0A6", "background-color:#FFF6E5", 1)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body><div id='bg'></div>"
            f"<script>{k27.JS}{k28.JS_EXTRA}{n1.JS_NOV}</script>{cover_lookb_book()}</body></html>")


SPECS = {
    "book": dict(
        id="lh-reel-1110-questions-first", scene="book", music="media/music/library/v4/lh-x-tick-boom.mp3",
        durs=[2.5, 3.7, 4.3, 3.0], follow_y=700, stamp_xy=(830, 960),
        hits=[(0.15, "sfx-x-swoosh-in", 0.12), (1.7, "sfx-x-sticker-pop", 0.25), (2.55, "sfx-x-paper-slap", 0.3), (2.85, "sfx-x-paper-slap", 0.22),
              (3.55, "sfx-x-sticker-pop", 0.25), (3.55 + 0.45, "sfx-x-swoosh-in", 0.15), (4.5, "sfx-x-sticker-pop", 0.3),
              (6.25, "sfx-x-paper-slap", 0.3), (6.5, "sfx-x-paper-slap", 0.22), (8.9, "sfx-x-sticker-pop", 0.2), (9.34, "sfx-x-sticker-pop", 0.2),
              (10.0, "sfx-x-paper-slap", 0.22), (10.5, "sfx-x-whoosh-hit", 0.22)],
        beats=[
            dict(head="Guess 5 answers. / *Then read.*", fs=150, top=320),
            dict(kick="try this", head="Even wrong guesses / *help it stick.*", fs=112,
                 sub="Guess first, then read. You remember<br>those answers better.", ss=44,
                 src="St. Hilaire et al. 2024 · Psychonomic Bulletin & Review", top=230),
            dict(kick="Do this tonight:", head="Turn to the end. / *Guess 5 answers.*", fs=112,
                 sub="Use the end-of-chapter questions.<br>Then read, and check each one.", ss=44, top=230),
            dict(head="Guess 5 answers. / *Then read.*", fs=124, top=300),
        ]),
}


def build(key, s, out_dir):
    still = next((a[8:] for a in sys.argv if a.startswith("--still=")), None)
    if still:
        k28.render(s, key, still=[float(x) for x in still.split(",")]); print("stills", SCR / f"{key}-stills.jpg"); return
    cov = out_dir / f"{s['id']}-cover.jpg"
    k28.render(s, key, cover_page=cover_page(), cover_out=cov); print("cover", cov)
    if "--cover-only" in sys.argv:
        return
    fdir, total, starts = k28.render(s, key)
    out = out_dir / f"{s['id']}.mp4"
    k28.encode(fdir, total, s["music"], s["hits"], out)
    print(out, round(total, 2), starts)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    for key in args:
        if key == "oneword":
            import nov05_lockedhour_feed as fd_; fd_.oneword(); print("done oneword")
        else:
            build(key, SPECS[key], OUT)

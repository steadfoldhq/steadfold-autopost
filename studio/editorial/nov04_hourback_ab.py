#!/usr/bin/env python3
"""Scenes + specs for the Nov 4 Hourback Reels A and B (imported by nov04_hourback.py; run that file, not this one).

nonna  = hb-reel-1108-nonna-90 (Sun Nov 8, 7 pm). Drawn kitchen table: a cake with '9' '0' candles, a floured board of
         gnocchi with a fork ('Sundays'), and Nonna's open card. FRAME 0 already shows Claude's real Italian card (all 3
         sentences + sign-off, word for word) under the hook. Beat 1: the made-up ask flies in, then each sentence gets its
         English meaning (word for word from the reply). Beat 2: its own note on 'tu' / 'Ti voglio bene', word for word.
         Real run: studio/editorial/hb-nov04-run-nonna.txt.
retire = hb-reel-1109-retirement-speech (Mon Nov 9, 7 pm). Drawn send-off table: a mic on a stand, a stopwatch counting
         down from 2:00, a jar of lemon candies, and the speech page. FRAME 0 shows the real opening of Claude's speech
         ('Speech for Linda', word for word). Beat 1: the made-up facts fly in, then the page runs through 3 real
         passages (the joke highlighted). Beat 2: the candy-jar passage word for word (jar glows). Beat 3: its closing
         toast line. Real run: studio/editorial/hb-nov04-run-retire.txt.
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
import nov03_hourback as N3  # noqa: E402

wrap = N3.wrap


CFG = [(72, 34, 56, 31), (52, 46, 38, 45), (60, 40, 50, 34)]   # (Italian px, wrap, English px, wrap) per line card


def _nonna(reply):
    it = re.findall(r"^\*\*(.+?)\*\*$", reply, re.M)
    en = [m for m in re.findall(r"^\*([^*].*?)\*$", reply, re.M)]
    assert it[:3] and len(en) == 4, (it, en)
    note = reply.strip().split("\n\n")[-1].strip()
    assert note.startswith('This uses the informal "tu" form'), note
    sign = f"{it[3]} {it[4]}"
    return dict(it=[wrap(s, 52) for s in it[:3]], it1=[wrap(s, c[1]) for s, c in zip(it[:3], CFG)], en=[wrap(s, c[3]) for s, c in zip(en[:3], CFG)], cfg=CFG,
                sign=sign, note=wrap(note, 44), raw_it=it, raw_en=en, raw_note=note)


def _retire(reply):
    body = reply.split("\n---\n")[0]
    paras = [p.strip() for p in body.split("\n\n") if p.strip()]
    assert paras[0] == "**Speech for Linda**", paras[0]
    P = paras[1:]
    open_ = " ".join(P[0:3])                       # Good afternoon … whose face it was.
    reg = P[3]                                      # Linda knew every regular by name …
    joke = P[4]                                     # She also knew exactly whose books were overdue …
    story = P[5]
    jar = P[6]
    toast = P[-1]
    assert reg.startswith("Linda knew every regular") and joke.endswith("Mostly.") and jar.startswith("And then there's the jar")
    assert toast.startswith("To Linda,"), toast
    jar_q = jar.split(" It was a small thing.")[0]  # shortened on screen, marked …
    story_q = story.split(" Some of those kids")[0]
    reg_q = reg.split(" Your favorite authors.")[0]
    open3 = P[2].split(" And she always knew")[0] + " …"   # CD gate: the odd-out-loud line is cut on screen (marked …)
    return dict(open=[wrap(s, 40) for s in (P[0], P[1], open3)], reg=wrap(reg_q + " …", 48), joke=wrap(joke, 48),
                story=wrap(story_q + " …", 48), jar=wrap(jar_q.replace("And then there's the jar. ", "") + " …", 46),
                jarlead="And then there's the jar.", toast=wrap(toast, 40),
                raw=dict(open=P[0:3], reg_q=reg_q, joke=joke, story_q=story_q, jar_q=jar_q, toast=toast))


JS = r"""
// =============================================== Nov 4 A/B shared
const QX=70, QY=1090, QW=940, QH=500;
function card4(head,inner,col){ return `<rect x="12" y="16" width="${QW}" height="${QH}" rx="22" fill="rgba(42,29,71,.16)"/><rect x="0" y="0" width="${QW}" height="${QH}" rx="22" fill="${col||'#FFFFFF'}" ${o}/>
 <path d="M0 22 Q0 0 22 0 H${QW-22} Q${QW} 0 ${QW} 22 V92 H0Z" fill="${PEACH}" ${o} stroke-width="4"/>
 <text x="40" y="64" font-family="Poppins" font-weight="700" font-size="40" fill="${INK}">${esc(head)}</text>${inner}`;}
function askNote(lt,title,lines,ty){ // the made-up ask flies from the wall into the card
 const k=E(seg(lt,0,0.15)), fl=seg(lt,ASK_HOLD,T0); if(fl>=1) return '';   // CD gate: held 2 s at 52 px
 const tx=60+(QX+200-60)*E(fl), y=ty+(QY+60-ty)*E(fl), sc=1-0.72*E(fl);
 const inner=label(26,60,title,-2,50,ACC,'start')+textLines(26,132,lines,52,62,OL,'Caveat',700);
 return `<g opacity="${k*(1-seg(fl,.8,1))}" transform="translate(${tx} ${y}) scale(${sc})">`+sticky(0,0,900,104+lines.length*62,-2,'#FFE7A0',inner,40*(1-k))+`</g>`;}
function hlLines(x,y,lines,size,lh,col,fam,hk){ // lines with a yellow marker that sweeps in (hk 0..1)
 let s=''; if(hk>0) s+=`<rect x="${x-12}" y="${y-size*0.95}" width="${(QW-56)*hk}" height="${lines.length*lh+10}" rx="12" fill="${SUN}" opacity=".5"/>`;
 return s+textLines(x,y,lines,size,lh,col,fam,700);}

// =============================================== scene: Nonna turns 90 tomorrow, card in Italian (Nov 8)
const NNX=__NONNA__;
function cake90(x,y,beam,t){
 let s=`<g transform="translate(${x} ${y})"><ellipse cx="0" cy="150" rx="200" ry="18" fill="rgba(42,29,71,.14)"/>`;
 s+=`<ellipse cx="0" cy="140" rx="190" ry="20" fill="#FFFFFF" ${o}/>`;
 s+=`<path d="M-160 40 H160 V130 Q0 150 -160 130Z" fill="${PEACH}" ${o}/><path d="M-160 40 Q-130 70 -100 40 Q-70 70 -40 40 Q-10 70 20 40 Q50 70 80 40 Q110 70 140 40 L160 40" fill="#FFFFFF" ${o} stroke-width="4"/>`;
 s+=`<path d="M-110 -40 H110 V40 H-110Z" fill="${PERI}" ${o}/><path d="M-110 -40 Q-80 -14 -50 -40 Q-20 -14 10 -40 Q40 -14 70 -40 Q90 -20 110 -40" fill="#FFFFFF" ${o} stroke-width="4"/>`;
 ['9','0'].forEach((d,i)=>{ const cx=-44+i*88, fl=1+0.12*Math.sin(t*11+i*2)+0.5*beam;
  s+=`<text x="${cx}" y="-50" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="120" fill="${SUN}" stroke="${OL}" stroke-width="5" paint-order="stroke">${d}</text>`;
  s+=`<circle cx="${cx}" cy="-176" r="${40+30*beam}" fill="url(#glow)" opacity="${0.7+0.3*beam}"/>`;
  s+=`<path d="M${cx} ${-150-34*fl} Q${cx+14} -164 ${cx} -146 Q${cx-14} -164 ${cx} ${-150-34*fl}Z" fill="${ORNG}" stroke="${OL}" stroke-width="3"/>`;
  s+=`<path d="M${cx} -146 V-140" stroke="${OL}" stroke-width="4"/>`; });
 return s+`</g>`;}
function gnocchiBoard(x,y,t){
 let s=`<g transform="translate(${x} ${y}) rotate(-6)"><ellipse cx="0" cy="60" rx="190" ry="16" fill="rgba(42,29,71,.14)"/>`;
 s+=`<rect x="-180" y="-70" width="360" height="130" rx="26" fill="${WOOD}" ${o}/><rect x="170" y="-26" width="70" height="40" rx="14" fill="${WOOD}" ${o}/>`;
 s+=`<path d="M-150 -40 q20 10 40 0 M60 30 q30 -10 60 4" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity=".7"/>`;
 [[-110,-20],[-50,10],[10,-24],[70,4],[-90,30],[120,-30]].forEach((p,i)=>{ s+=`<g transform="translate(${p[0]} ${p[1]}) rotate(${i*23})"><ellipse rx="26" ry="18" fill="#FFF3C4" stroke="${OL}" stroke-width="4"/><path d="M-12 -6 q12 6 24 0 M-12 4 q12 6 24 0" stroke="${WOODD}" stroke-width="3" fill="none"/></g>`; });
 s+=`<g transform="translate(40 -96) rotate(18)"><rect x="-8" y="0" width="16" height="150" rx="7" fill="#D9D3F3" stroke="${OL}" stroke-width="4"/><path d="M-22 -60 V0 H22 V-60 M-7 -60 V0 M7 -60 V0" stroke="${OL}" stroke-width="5" fill="none" stroke-linecap="round"/></g>`;
 s+=label(-120,-100,'Sundays',-6,58,ACC,'middle');
 return s+`</g>`;}
const NTX=[2.3,3.4,4.5];   // beat 1: when each sentence gets its English
function nonnaCard(beat,lt,t){
 const full=(hk)=>{ let y=158, s=''; NNX.it.forEach((ls,i)=>{ s+=hlLines(40,y,ls,44,52,PEN,'Caveat',hk&&hk[i]?hk[i]:0); y+=ls.length*52+16; });
   return s+`<text x="${QW-40}" y="${y+14}" text-anchor="end" font-family="Caveat" font-weight="700" font-size="46" fill="${INDI}">${esc(NNX.sign)}</text>`; };
 if(beat==0||(beat==1&&lt<NTX[0])) return card4("Claude's card for Nonna, in Italian", full());
 if(beat==1){ let k=0; for(let i=0;i<3;i++) if(lt>=NTX[i]) k=i; const p=E(seg(lt,NTX[k],NTX[k]+0.18));
   const c=NNX.cfg[k], il=c[0]*1.12, el=c[2]*1.25, y0=104+c[0];   // CD gate: Italian + English in ink, sized to fill the card
   let s=`<g opacity="${p}" transform="translate(${26*(1-p)} 0)">`+textLines(40,y0,NNX.it1[k],c[0],il,INK,'Caveat',700);
   const yd=y0+(NNX.it1[k].length-1)*il+c[0]*0.55;
   s+=`<rect x="28" y="${yd}" width="${QW-56}" height="4" rx="2" fill="${PERI}"/>`;
   s+=textLines(40,yd+c[2]*1.2,NNX.en[k],c[2],el,INK,'Inter',600)+`</g>`;
   return card4(`Line ${k+1} of 3, with its English`, s); }
 if(beat==2){ const p=E(seg(lt,0.1,0.35)); let s=`<g opacity="${p}">`+textLines(40,178,NNX.note,40,58,INK,'Inter',500)+`</g>`;
   return card4("Its note, word for word", s,'#FFFDF6'); }
 return card4("Claude's card for Nonna, in Italian", full([1,1,1].map(()=>E(seg(lt,0.1,0.6)))) + check(QW-70,46+0,seg(lt,0.2,0.8)));}
function nonnaScene(beat,lt,t,S){
 let s=tableTop(1050);
 const beam=beat==3?E(seg(lt,0.05,0.6)):0;
 s+=`<g transform="translate(270 985) scale(.74)">`+cake90(0,0,beam,t)+`</g>`+gnocchiBoard(790,990,t);
 s+=`<g transform="translate(${QX} ${QY}) rotate(-0.8)">`+nonnaCard(beat,lt,t)+`</g>`;
 if(beat==1) s+=askNote(lt,'what we told it (made up for this post):',["Grandma turns 90 tomorrow","she reads Italian best, my Italian is basic","she taught me to make gnocchi on Sundays"],660);
 if(beat==3) s+=confetti(540,860,seg(lt,0.05,1.2),t);
 return s;}
SCENES.nonna=nonnaScene;

// =============================================== scene: 31 years, a 2-minute retirement speech (Nov 9)
const RTX=__RETIRE__;
function micStand(x,y,t){ return `<g transform="translate(${x} ${y})"><ellipse cx="0" cy="180" rx="90" ry="14" fill="rgba(42,29,71,.14)"/>
 <path d="M0 10 V176 M-60 180 H60" stroke="${OL}" stroke-width="10" stroke-linecap="round"/>
 <rect x="-34" y="-110" width="68" height="120" rx="34" fill="${INDI}" ${o}/><path d="M-34 -70 H34 M-34 -40 H34" stroke="${PERI}" stroke-width="4"/>
 <path d="M-52 -20 Q-52 40 0 40 Q52 40 52 -20" stroke="${OL}" stroke-width="7" fill="none"/>
 ${[0,1,2].map(i=>{const k=(t*0.8+i/3)%1; return `<path d="M${60+40*k} ${-80-10*k} q14 30 0 60" stroke="${ORNG}" stroke-width="5" fill="none" stroke-linecap="round" opacity="${0.8*Math.sin(Math.PI*k)}"/>`;}).join('')}</g>`;}
function stopwatch(x,y,t,beam){ const left=Math.max(0,120-t), mm=Math.floor(left/60), ss=Math.floor(left%60);
 const a=(t%60)/60*2*Math.PI;
 return `<g transform="translate(${x} ${y})"><circle r="${120+30*beam}" fill="url(#glow)" opacity="${0.6*beam}"/><circle cx="6" cy="10" r="100" fill="rgba(42,29,71,.14)"/>
 <rect x="-18" y="-130" width="36" height="30" rx="8" fill="${SUN}" ${o} stroke-width="4"/><circle r="100" fill="#FFFFFF" ${o} stroke-width="7"/>
 <circle r="84" fill="none" stroke="${PERI}" stroke-width="10"/><path d="M0 -84 A84 84 0 ${a>Math.PI?1:0} 1 ${84*Math.sin(a)} ${-84*Math.cos(a)}" fill="none" stroke="${ORNG}" stroke-width="10" stroke-linecap="round"/>
 <text x="0" y="22" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="62" fill="${INK}">${mm}:${String(ss).padStart(2,'0')}</text></g>`;}
function candyJar(x,y,glow,t){ let s=`<g transform="translate(${x} ${y})">${glow>0?`<circle cx="0" cy="20" r="${150+20*glow}" fill="url(#glow)" opacity="${glow}"/>`:''}<ellipse cx="0" cy="120" rx="110" ry="14" fill="rgba(42,29,71,.14)"/>`;
 s+=`<path d="M-80 -40 Q-100 0 -96 70 Q-90 116 0 118 Q90 116 96 70 Q100 0 80 -40Z" fill="rgba(201,202,245,.55)" ${o}/>`;
 [[-50,80],[0,90],[50,78],[-26,50],[30,48],[-60,30],[60,26],[0,18]].forEach((p,i)=>{ s+=`<g transform="translate(${p[0]} ${p[1]}) rotate(${i*40})"><ellipse rx="24" ry="17" fill="${SUN}" stroke="${OL}" stroke-width="3"/><path d="M-30 -6 L-22 0 L-30 6 M30 -6 L22 0 L30 6" fill="${SUN}" stroke="${OL}" stroke-width="3"/></g>`; });
 s+=`<rect x="-86" y="-66" width="172" height="34" rx="10" fill="${INDI}" ${o} stroke-width="4"/>`;
 s+=label(10,-96,'rough-day candies',-4,44,ACC,'middle');
 return s+`</g>`;}
const RTTX=[2.3,3.35,4.4];   // beat 1 passage times
function retireCard(beat,lt,t){
 const lined=()=>`<path d="M28 ${QH-30} H${QW-28}" stroke="#E4E1F6" stroke-width="3"/>`;
 if(beat==0||(beat==1&&lt<RTTX[0])){ let y=158, s=lined(); RTX.open.forEach(ls=>{ s+=textLines(40,y+10,ls,54,64,PEN,'Caveat',700); y+=ls.length*64+8; });
   return card4("Speech for Linda, shortened", s); }
 if(beat==1){ let k=0; for(let i=0;i<3;i++) if(lt>=RTTX[i]) k=i; const p=E(seg(lt,RTTX[k],RTTX[k]+0.16));
   const L=[RTX.reg,RTX.joke,RTX.story][k], hk=k==1?E(seg(lt,RTTX[1]+0.3,RTTX[1]+0.7)):0;
   let s=lined()+`<g opacity="${p}" transform="translate(0 ${30*(1-p)})">`+hlLines(40,170,L,50,60,PEN,'Caveat',hk);
   if(k==1) s+=label(QW-60,170+L.length*60+30,'← the joke',-4,46,ACC,'end');
   s+=`</g>`;
   return card4("Speech for Linda, shortened", s); }
 if(beat==2){ const hk=E(seg(lt,0.5,1.0)); let s=lined()+textLines(40,166,[RTX.jarlead],46,58,PEN,'Caveat',700)+hlLines(40,224,RTX.jar,46,56,PEN,'Caveat',hk);
   return card4("Its jar story, word for word", s); }
 let s=lined()+label(40,166,'its last line:',-2,46,ACC,'start')+textLines(40,236,RTX.toast,58,68,INDI,'Caveat',700)+check(QW-70,46,seg(lt,0.2,0.8));
 return card4("Speech for Linda, word for word", s);}
function retireScene(beat,lt,t,S){
 let s=tableTop(1050);
 const glow=beat==2?E(seg(lt,0.1,0.5)):0, beam=beat==3?E(seg(lt,0.05,0.6)):0;
 s+=micStand(190,915,t)+stopwatch(540,950,t,beam)+candyJar(860,950,glow,t);
 s+=`<g transform="translate(${QX} ${QY}) rotate(-0.8)">`+retireCard(beat,lt,t)+`</g>`;
 if(beat==1) s+=askNote(lt,'what we told it (made up for this post):',["Linda: 31 years at the library front desk","knew every regular's name","20 years of Saturday story time","lemon candies for anyone's rough day"],640);
 if(beat==3) s+=confetti(540,860,seg(lt,0.05,1.2),t);
 return s;}
SCENES.retire=retireScene;
"""


def js(run_reply):
    n = _nonna(run_reply("nonna"))
    r = _retire(run_reply("retire"))
    return (JS.replace("__NONNA__", json.dumps({k: v for k, v in n.items() if not k.startswith("raw")}, ensure_ascii=False))
              .replace("__RETIRE__", json.dumps({k: v for k, v in r.items() if k != "raw"}, ensure_ascii=False)))


def specs(LIB, OUT):
    return {
        "nonna": dict(
            id="hb-reel-1108-nonna-90", scene="nonna", out=OUT, music=LIB / "hb-x-smart-bounce.mp3",
            wall="linear-gradient(180deg,#C9CAF5 0%,#D3CFF6 30%,#EBE1F2 50%,#FFF8EF 54.6%,#FFF8EF 100%)",
            durs=[2.0, 5.6, 3.0, 3.9], follow_at=1.2, follow_y=724, chip_y=228,
            beats=[
                dict(kick="", head="Nonna turns 90 / *tomorrow. In Italian?*", fs=124),
                dict(kick="try this", head="Ask AI to write it / *in her language.*", fs=112,
                     sub="With the English under each line:"),
                dict(kick="it explains its choices", head="It picks the words / *you'd use with family.*", fs=104),
                dict(kick="Do this:", head="Ask for her language, / *English underneath.*", fs=104,
                     sub="In ChatGPT, Claude or Gemini.<br>Then ask someone who speaks it."),
            ],
            chip="Real Claude reply · Nonna and Marco made up for this post",
        ),
        "retire": dict(
            id="hb-reel-1109-retirement-speech", scene="retire", out=OUT, music=LIB / "hb-x-ta-da-funk.mp3",
            wall="linear-gradient(180deg,#B9B4EE 0%,#C9CAF5 35%,#E6DFF4 50%,#FFF8EF 54.6%,#FFF8EF 100%)",
            durs=[2.0, 5.4, 3.0, 4.0], follow_at=1.4, follow_y=724, chip_y=228,
            beats=[
                dict(kick="", head="31 years. / *You get 2 minutes.*", fs=128),
                dict(kick="try this", head="Tell AI 3 true stories. / *It writes the speech.*", fs=104,
                     sub="Claude's real speech, shortened:"),
                dict(kick="it turns facts into moments", head="A jar of candies / *becomes the best line.*", fs=108),
                dict(kick="Do this:", head="Tell AI 3 stories. / *Ask for 2 minutes.*", fs=110,
                     sub="In ChatGPT, Claude or Gemini.<br>Read it out loud once."),
            ],
            chip="Real Claude reply · Linda and the library made up for this post",
        ),
    }

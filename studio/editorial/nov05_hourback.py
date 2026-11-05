#!/usr/bin/env python3
"""Hourback Reel built Thu Nov 5 2026 by the Hourback maker (Social studio).

    python3 studio/editorial/nov05_hourback.py sitter                    # mp4 + dedicated cover -> media/studio-nov05/hourback/
    python3 studio/editorial/nov05_hourback.py sitter --still 0,2.5,5     # stills sheet in the scratch dir (review)
    python3 studio/editorial/nov05_hourback.py sitter --full 0            # one full-size frame (review)
    python3 studio/editorial/nov05_hourback.py sitter --cover-only

sitter = hb-reel-1110-sitter-at-6 (Tue Nov 10, 7 pm). NEW composition (CD Nov 4: no table-line + card-at-the-bottom
         template): a fridge front fills the lower frame; a digital clock magnet on the freezer reads 5:48.
         CD gate fixes (Nov 5): FRAME 0 = hook + the big messy brain-dump note (made up, 62 px, out of order) + the clock.
         Beat 1 (2.0 s): the dump flies off and Claude's REAL sorted note slams onto the door (shortened: its 10:30 row is
         left off), rows light in order. Beat 2: its own note about the missing dinner time, word for word, BELOW the rows;
         head 'It flags what you forgot. / Still add allergies.' Beat 3: phone blanks light, tick, clock 5:51.
         Real run: studio/editorial/hb-nov05-run-sitter.txt.

Extends studio/editorial/nov04_hourback.py (-> nov03 -> nov02 -> nov01 -> oct28 engine) by import; edits nothing shared.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
sys.dont_write_bytecode = True
import nov04_hourback as N4  # noqa: E402

B = N4.B
B.SCR = Path("/tmp/claude-0/nov05-hourback")
LIB = B.LIB
OUT5 = REPO / "media/studio-nov05/hourback"
wrap = N4.N3.wrap


def run_reply(slug):
    t = (REPO / f"studio/editorial/hb-nov05-run-{slug}.txt").read_text()
    return t.split("===== REPLY (verbatim) =====\n", 1)[1]


def sitter_data():
    r = run_reply("sitter")
    title = re.search(r"^\*\*(Babysitter Notes[^*]+)\*\*$", r, re.M).group(1)
    rows = re.findall(r"^- \*\*(.+?):\*\* (.+)$", r, re.M)
    call = re.search(r"^\*\*(Please CALL[^*]+)\*\*$", r, re.M).group(1)
    blanks = re.search(r"^(Mom: _+ Dad: _+)$", r, re.M).group(1)
    note = r.strip().split("\n\n")[-1].strip()
    assert title == "Babysitter Notes – Maya (7) & Leo (3)", title
    assert [k for k, _ in rows] == ["Dinner", "7:00", "7:30", "7:40", "8:00", "10:30"], rows
    assert note.startswith("You didn't give a dinner time"), note
    blanks_short = "Mom: ________   Dad: ________"     # same words, shorter rules so it fits the sheet
    # CD gate Nov 5 round 3: keep a 10:30 line, cropped word for word to its first sentence (marked …), which drops the
    # contradictory "We're at a restaurant 10 minutes away." while keeping "back by 10:30"
    R1030 = rows[5][1].split(". ")[0] + ". …"
    assert R1030 == "We're home. …", R1030
    return dict(title=title, rows=[[k, wrap(v, 36 if len(v) <= 36 else 33)] for k, v in rows[:5]] + [["10:30", [R1030]]], call=call, blanks=blanks_short,
                note=wrap(note, 46), raw=dict(rows=rows, call=call, blanks=blanks, note=note, title=title))


SD = sitter_data()

JS_NOV05 = r"""
// =============================================== Nov 5: babysitter at 6, the fridge note (Nov 10)
(()=>{   // own scope: no clash with older scenes' globals
const SDX=__SITTER__;
const FX=96, FY=740, FW=888, FH=820;                 // fridge body
const SX=150, SY=858, SW=780, SH=612;        // the note on the door
function fridge(t){
 let s=`<ellipse cx="540" cy="${FY+FH+22}" rx="500" ry="22" fill="rgba(42,29,71,.14)"/>`;
 s+=`<rect x="${FX+70}" y="${FY+FH-10}" width="70" height="34" rx="8" fill="${INK}"/><rect x="${FX+FW-140}" y="${FY+FH-10}" width="70" height="34" rx="8" fill="${INK}"/>`;
 s+=`<rect x="${FX+14}" y="${FY+18}" width="${FW}" height="${FH}" rx="56" fill="rgba(42,29,71,.14)"/>`;
 s+=`<rect x="${FX}" y="${FY}" width="${FW}" height="${FH}" rx="56" fill="#FFFFFF" ${o}/>`;
 s+=`<path d="M${FX} ${FY+102} H${FX+FW}" stroke="${OL}" stroke-width="5"/>`;                       // freezer seam
 s+=`<rect x="${FX+44}" y="${FY+30}" width="200" height="22" rx="11" fill="${PERI}" ${o} stroke-width="4"/>`; // freezer handle
 s+=`<rect x="${FX+28}" y="${FY+134}" width="22" height="360" rx="11" fill="${PERI}" ${o} stroke-width="4"/>`; // door handle
 s+=`<path d="M${FX+40} ${FY+90} q120 -10 260 0" stroke="#E9E6F8" stroke-width="10" stroke-linecap="round" fill="none"/>`;
 return s;}
function clockMag(x,y,t,beat,lt){ // digital clock magnet: the deadline, ticking
 const late=beat==3&&lt>0.3; const txt=late?'5:51':'5:48'; const col=Math.floor(t*2)%2==0?1:0.25;
 const pop=late?1+0.12*Math.sin(Math.PI*seg(lt,0.3,0.6)):1+0.03*Math.sin(t*4);
 const [h,m]=txt.split(':');
 return `<g transform="translate(${x} ${y}) scale(${pop}) rotate(4)"><rect x="-128" y="-48" width="256" height="104" rx="20" fill="rgba(42,29,71,.16)" transform="translate(6 8)"/>
 <rect x="-128" y="-48" width="256" height="104" rx="20" fill="${INK}" ${o}/><rect x="-112" y="-34" width="224" height="76" rx="12" fill="#3B2E5E"/>
 <text x="-14" y="26" text-anchor="end" font-family="Poppins" font-weight="700" font-size="70" fill="${SUN}">${h}</text>
 <text x="0" y="20" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="70" fill="${SUN}" opacity="${col}">:</text>
 <text x="14" y="26" text-anchor="start" font-family="Poppins" font-weight="700" font-size="70" fill="${SUN}">${m}</text></g>`;}
function magnet(x,y,col){ return `<circle cx="${x+3}" cy="${y+5}" r="26" fill="rgba(42,29,71,.18)"/><circle cx="${x}" cy="${y}" r="26" fill="${col}" ${o} stroke-width="4"/><circle cx="${x-8}" cy="${y-8}" r="7" fill="#FFFFFF" opacity=".7"/>`;}
function sunMag(x,y,t){ // a crayon-sun magnet (decor), slow spin
 let s=`<g transform="translate(${x} ${y}) rotate(${t*20})">`; for(let i=0;i<8;i++){ s+=`<path d="M0 -40 V-58" stroke="${ORNG}" stroke-width="7" stroke-linecap="round" transform="rotate(${i*45})"/>`; }
 return s+`<circle r="32" fill="${SUN}" ${o} stroke-width="4"/><path d="M-12 -4 v2 M12 -4 v2 M-12 10 q12 10 24 0" stroke="${OL}" stroke-width="4" fill="none" stroke-linecap="round"/></g>`;}
const ROWT=[0.9,1.3,1.7,2.1,2.5,2.9];    // beat 1: rows light in order (lt)
function sitterSheet(beat,lt,t){
 let s=`<rect x="10" y="14" width="${SW}" height="${SH}" rx="10" fill="rgba(42,29,71,.14)"/><rect x="0" y="0" width="${SW}" height="${SH}" rx="10" fill="#FFFDF6" ${o} stroke-width="4"/>`;
 s+=`<text x="34" y="60" font-family="Caveat" font-weight="700" font-size="46" fill="${INDI}">${esc(SDX.title)}</text>`;
 s+=`<text x="${SW-30}" y="96" text-anchor="end" font-family="Caveat Brush" font-size="32" fill="${ACC}">Claude's real note, shortened · kids made up for this post</text>`;
 s+=`<path d="M28 112 H${SW-28}" stroke="#E4E1F6" stroke-width="3"/>`;
 let y=160; const L=44;
 SDX.rows.forEach((r,i)=>{
   let hk=0;
   if(beat==1){ if(lt>=ROWT[i]) hk=E(seg(lt,ROWT[i],ROWT[i]+0.25)); if(i<5 && lt>=ROWT[i+1]) hk=0.35; if(i==5&&lt>ROWT[5]+0.6) hk=0.35; }
   if(beat==2 && i==0) hk=E(seg(lt,0.3,0.6));
   const hh=r[1].length*L;
   if(hk>0) s+=`<rect x="20" y="${y-40}" width="${(SW-40)*Math.min(1,hk*1.2)}" height="${hh+8}" rx="10" fill="${SUN}" opacity="${0.55*Math.min(1,hk)}"/>`;
   const pw=r[0].length>4?150:132;
   s+=`<rect x="30" y="${y-35}" width="${pw}" height="44" rx="22" fill="${i==0?PEACH:PERI}" stroke="${OL}" stroke-width="3"/>`;
   s+=`<text x="${30+pw/2}" y="${y-2}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="28" fill="${INK}">${esc(r[0])}</text>`;
   s+=textLines(204,y,r[1],42,L,PEN,'Caveat',700);
   y+=hh+6; });
 y+=8;
 if(beat==2) return s;   // its note covers this area in beat 2: no half-hidden line under it
 const bk=beat==3?E(seg(lt,0.25,0.6)):0;
 s+=`<text x="34" y="${y+8}" font-family="Caveat" font-weight="700" font-size="44" fill="${ACC}">${esc(SDX.call)}</text>`;
 if(bk>0) s+=`<rect x="20" y="${y+30}" width="${(SW-40)*bk}" height="58" rx="10" fill="${SUN}" opacity=".55"/>`;
 s+=`<text x="34" y="${y+74}" font-family="Caveat" font-weight="700" font-size="44" fill="${PEN}">${esc(SDX.blanks)}</text>`;
 if(beat==3) s+=check(SW-80,y+60,seg(lt,0.4,1.0));
 return s;}
const DUMP=["back by 10:30 · call, don't text","Maya: bed 8, reads 20 min first","mac and cheese, heat 2 min","no screens after 7","Leo: bed 7:30, stuffed rabbit"];
const DROT=[-1.5,1.2,-0.6,1.8,-1.0], DX=[0,34,10,46,18];
function dumpNote(beat,lt,t){ // frame 0: the made-up brain dump, big and legible, in no order; beat 1: it flies off as the sorted note lands
 if(beat>1) return ''; let fl=beat==1?E(seg(lt,0,0.35)):0; if(fl>=1) return '';
 const x=120+(-40-120)*fl, y=880+(720-880)*fl, sc=1-0.6*fl, bob=beat==0?4*Math.sin(t*3):0;
 const w=840, h=120+DUMP.length*76;
 let s=`<g opacity="${1-fl}" transform="translate(${x} ${y+bob}) scale(${sc}) rotate(-2.5)"><rect x="8" y="12" width="${w}" height="${h}" fill="rgba(42,29,71,.15)"/><rect x="0" y="0" width="${w}" height="${h}" fill="#FFE7A0" ${o} stroke-width="4"/>`;
 s+=`<text x="34" y="66" font-family="Caveat Brush" font-size="46" fill="${ACC}">my brain dump (made up for this post):</text>`;
 DUMP.forEach((l,i)=>{ const yy=146+i*76; s+=`<text x="${40+DX[i]}" y="${yy}" font-family="Caveat" font-weight="700" font-size="62" fill="${OL}" transform="rotate(${DROT[i]} ${40+DX[i]} ${yy})">${esc(l)}</text>`; });
 return s+magnet(w/2,0,ORNG)+`</g>`;}
function itsNote(lt){ // beat 2: its own note, word for word, pinned BELOW the list rows (CD gate Nov 5)
 const k=E(seg(lt,0.05,0.35)); const h=106+SDX.note.length*44;
 let s=`<g opacity="${k}" transform="translate(110 ${1328+60*(1-k)}) rotate(0.6)"><rect x="10" y="14" width="860" height="${h}" rx="22" fill="rgba(42,29,71,.18)"/><rect x="0" y="0" width="860" height="${h}" rx="22" fill="#FFFFFF" ${o}/>`;
 s+=`<path d="M0 22 Q0 0 22 0 H838 Q860 0 860 22 V54 H0Z" fill="${PEACH}" ${o} stroke-width="4"/>`;
 s+=`<text x="36" y="39" font-family="Poppins" font-weight="700" font-size="28" fill="${INK}">Its note under the list, word for word</text>`;
 s+=textLines(36,94,SDX.note,34,44,INK,'Inter',600);
 return s+`</g>`;}
function sitterScene(beat,lt,t,S){
 const punch=beat>0?1+0.035*(1-E(seg(lt,0,0.35))):1;          // zoom punch-in on every cut
 const shake=(beat==1&&lt>0.35&&lt<0.53)?8*Math.sin(lt*120):0; // the sorted note slams on: frame shake
 let s=`<g transform="translate(540 1200) scale(${punch}) translate(-540 -1200) translate(${shake} 0)">`;
 const hideTop=beat==3?1-E(seg(lt,S.followAt-0.25,S.followAt)):1;   // CD round 3: clock + sun fade out before the follow pill lands on the freezer
 s+=fridge(t)+`<g opacity="${hideTop}">`+clockMag(800,FY+52,t,beat,lt)+sunMag(420,FY+50,t)+`</g>`;
 if(beat>=1){ const a=beat==1?E(seg(lt,0.12,0.4)):1, sc=1+0.08*(1-a);
   s+=`<g opacity="${a}" transform="translate(${SX+SW/2} ${SY+SH/2}) scale(${sc}) translate(${-SW/2} ${-SH/2}) rotate(-0.6)">`+sitterSheet(beat,lt,t)+magnet(70,4,SUN)+magnet(SW-70,4,ORNG)+`</g>`; }
 if(beat==2) s+=itsNote(lt);
 s+=`</g>`;
 s+=dumpNote(beat,lt,t);
 if(beat==3) s+=confetti(540,1060,seg(lt,0.05,1.2),t);   // burst from the note, clear of the Do-this sub line
 return s;}
SCENES.sitter=sitterScene;
})();
"""
B.JS = B.JS + JS_NOV05.replace("__SITTER__", json.dumps({k: v for k, v in SD.items() if k != "raw"}, ensure_ascii=False))

SPECS = dict(B.SPECS)
SPECS["sitter"] = dict(
    id="hb-reel-1110-sitter-at-6", scene="sitter", out=OUT5, music=LIB / "hb-x-future-easy.mp3",
    wall="linear-gradient(180deg,#C2BDF0 0%,#CFCDF5 30%,#E6DFF4 44%,#FFF8EF 60%,#FFF8EF 100%)",
    durs=[2.0, 4.8, 3.4, 4.0], follow_at=1.2, follow_y=760, chip_y=-400,
    beats=[
        dict(kick="", head="Babysitter at 6. / *Messy brain dump?*", fs=116),
        dict(kick="try this", head="Paste the mess. / *AI sorts it by time.*", fs=112),
        dict(kick="it spots the gap", head="It flags what you forgot. / *Still add allergies.*", fs=104),
        dict(kick="Do this:", head="Paste your brain dump. / *Ask: sorted by time.*", fs=100,
             sub="In ChatGPT, Claude or Gemini.<br>Write phone numbers by hand."),
    ],
    chip="",
)
B.SPECS = SPECS
N4.SPECS.update(SPECS)
_html4 = B.html


def _html5(spec, cover=False):
    h = _html4(spec, cover)
    if not spec.get("chip"):   # no chip at all (frame 0: 2 text blocks)
        h = re.sub(r'<div style="position:absolute;left:160px;right:30px;top:-400px;text-align:center"><span[^>]*></span></div>', "", h)
    # CD round 3: beat 2's descenders ('flags', 'you') ran into the line-2 pill: open the leading on that beat only
    h = h.replace("top:385px;white-space:nowrap;font-size:104px;color:#2A1D47", "top:375px;white-space:nowrap;font-size:104px;line-height:1.16;color:#2A1D47")
    return h


B.html = _html5


def render(key):
    return N4.render(key)


if __name__ == "__main__":
    key = sys.argv[1]
    if "--still" in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index("--still") + 1].split(",")]
        print(B.stills(key, ts))
    elif "--full" in sys.argv:
        print(B.full(key, float(sys.argv[sys.argv.index("--full") + 1]), B.SCR / f"{key}-full.png"))
    elif "--cover-only" in sys.argv:
        import nov05_hourback_covers as CV
        print(CV.build(key))
    else:
        print(render(key))
        import nov05_hourback_covers as CV
        print(CV.build(key))

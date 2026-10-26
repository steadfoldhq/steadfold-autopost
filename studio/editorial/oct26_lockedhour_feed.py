"""Locked Hour Oct 26 build, part 2: feed post (swipe to reveal), One Word No. 4 (relabelled 'Space'), Stories.
Run through studio/editorial/oct26_lockedhour.py feed|oneword|stories (it sets up the shared CSS and scratch dir)."""
import sys
from oct26_lockedhour import *  # noqa: F401,F403
import oct26_lockedhour as m
import oct25_lockedhour as o25

KIT = o25.KIT
sys.path.insert(0, str(KIT))
import feed as kitfeed  # noqa: E402

frame = kitfeed.frame
FW, FH = 1080, 1350
OUT = m.OUT


def optcard(letter, text, bg, rot=0, extra=""):
    return (f"<div style='position:relative;width:420px;height:300px;background:{bg};border:6px solid {INK};border-radius:26px;"
            f"box-shadow:12px 12px 0 {INK};transform:rotate({rot}deg)'>"
            f"<div style='position:absolute;left:26px;top:22px;width:70px;height:70px;border-radius:50%;background:{INK};color:{CREAM};"
            f"font:900 44px/70px Inter Display,Inter;text-align:center'>{letter}</div>"
            f"<div class='S' style='position:absolute;left:30px;right:30px;top:110px;font-size:72px;line-height:1.0;text-align:left'>{text}</div>{extra}</div>")


def sticker(txt="?"):
    return (f"<div style='position:absolute;inset:-14px;border-radius:30px;background:{PINK};border:6px solid {INK};"
            f"transform:rotate(4deg);display:flex;align-items:center;justify-content:center;font:900 190px/1 Inter Display,Inter;color:{INK}'>{txt}"
            f"<div style='position:absolute;right:-6px;top:-6px;width:90px;height:90px;background:#FFF0F6;border-left:5px solid {INK};"
            f"border-bottom:5px solid {INK};border-radius:0 26px 0 30px'></div></div>")


def circled():
    return (f"<svg width='560' height='430' viewBox='0 0 520 400' style='position:absolute;left:-80px;top:-70px;overflow:visible'>"
            f"<path d='M60,200 C40,80 200,20 330,40 C470,60 520,170 470,280 C420,380 200,390 110,330 C60,300 50,250 70,190' "
            f"fill='none' stroke='{DPINK}' stroke-width='12' stroke-linecap='round'/></svg>")


def feed():
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:26px;padding:12px 18px'>Swipe to reveal</span></div>
<div style='position:absolute;left:70px;right:70px;top:180px'>{dual("What breaks / a *strong habit?*", style="font-size:136px;text-align:left")}</div>
<div style='position:absolute;left:90px;top:620px'>{optcard("A", "Wanting it<br>more", "#FFFDF6", -2)}</div>
<div style='position:absolute;left:570px;top:640px'>{optcard("B", "", "#FFFDF6", 2, sticker())}</div>
<div class='hand' style='position:absolute;left:90px;right:90px;top:1030px;font-size:66px'>guess first, then swipe →</div>
{stamp(860, 1100, 140, -10)}""", "1/3", "SWIPE TO REVEAL")
    s2 = frame(f"""
<div style='position:absolute;left:70px;right:70px;top:110px'>{dual("*A new place.*", style="font-size:150px")}</div>
<div style='position:absolute;left:90px;top:330px;opacity:.55'>{optcard("A", "Wanting it<br>more", "#FFFDF6", -2)}</div>
<div style='position:absolute;left:570px;top:350px'>{optcard("B", "A change<br>of place", F['cream']['p2'], 2, circled())}</div>
<div class='S' style='position:absolute;left:90px;right:90px;top:740px;font-size:58px;line-height:1.08;text-align:left'>115 students switched universities. Their strong habits (exercise, TV, reading the news) <span class='pill' style='background:{F['cream']['p1']}'>kept going only where the setting stayed the same.</span></div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1120px;font-size:22px;opacity:.85;line-height:1.45'>Wood, Tam &amp; Guerrero Witt 2005,<br>Journal of Personality and Social Psychology</div>
""", "2/3", "SWIPE TO REVEAL")
    s3 = frame(f"""
<div style='position:absolute;left:0;right:0;top:120px'>{dual("Your next *fresh start* / is a new place.", style="font-size:112px")}</div>
<div class='card' style='left:110px;right:110px;top:440px;padding:40px 44px'>
 <div class='dothis' style='font-size:80px;text-align:left'>Do this:</div>
 <div class='S' style='font-size:64px;text-align:left;line-height:1.04'>New job, home or term? Set up the habit you want <span class='pill' style='background:{F['pink']['p1']}'>in the first weeks.</span></div></div>
<div class='hand' style='position:absolute;left:90px;right:90px;top:900px;font-size:54px'>in one study, the boost showed up only<br>in the first 3 months after a move</div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1080px;font-size:22px;opacity:.85;line-height:1.45'>Verplanken &amp; Roy 2016, Journal of Environmental Psychology<br>(521 people; small effect)</div>
""", "3/3", "LOCKED HOUR")
    d = OUT / "lh-1027-new-place"; d.mkdir(exist_ok=True)
    o25.shoot([page(s, FW, FH, f) for s, f in ((s1, "dots"), (s2, "cream"), (s3, "pink"))], [d / f"0{i+1}.jpg" for i in range(3)], FW, FH)


def oneword():
    """One Word No. 4 'Space': the Oct 25 candidate (oct25_lockedhour.oneword) relabelled No. 4, slide 2 headline and the
    Do-this line made clearer (spacing is about days apart, not about short sessions)."""
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:30px;padding:12px 20px'>One Word · No. 4</span></div>
<div style='position:absolute;left:70px;right:70px;top:190px'>{dual("Cramming the night / *before* again?", style="font-size:124px;text-align:left")}</div>
<div style='position:absolute;left:60px;top:760px;width:960px;height:120px;background:{PINK};opacity:.85;border-radius:60px'></div>
<div class='S riso' style='position:absolute;left:40px;right:40px;top:540px;font-size:340px;text-align:left'>Space.</div>
<img class='obj' src='{obj("hourglass")}' style='position:absolute;left:770px;top:850px;width:200px;transform:rotate(8deg)'>
<div class='hand' style='position:absolute;left:90px;top:960px;font-size:60px;text-align:left'>same study time,<br>spread over days</div>
<div class='mono' style='position:absolute;left:90px;top:1150px;font-size:24px;opacity:.8'>one word that guards your focus</div>
""", "No. 4", "ONE WORD")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    on = {0, 2, 4}
    cells = ""
    for i, dname in enumerate(days):
        x = 95 + i * 128
        lit = i in on
        cells += (f"<div style='position:absolute;left:{x}px;top:470px;width:112px;height:250px;border:5px solid {INK};border-radius:16px;"
                  f"background:{PINK if lit else '#FFFDF6'};box-shadow:{'8px 8px 0 ' + INK if lit else 'none'};opacity:{1 if lit else .75}'>"
                  f"<div style='font:800 34px/1 Inter Display,Inter;color:{INK};text-align:center;margin-top:22px'>{dname}</div>"
                  + ("<div class='mono' style='font-size:25px;font-weight:700;text-align:center;margin-top:70px;line-height:1.1'>20<br>min</div>" if lit else "")
                  + "</div>")
    s2 = frame(f"""
<div style='position:absolute;left:0;right:0;top:110px'>{dual("*3 days, 20 minutes each.* / Not 1 hour in 1 night.", style="font-size:104px")}</div>
{cells}
<div class='S' style='position:absolute;left:0;right:0;top:790px;font-size:70px'>Same hour. <span class='pill' style='background:{F['cream']['p1']}'>Spread out.</span></div>
<div class='hand' style='position:absolute;left:0;right:0;top:900px;font-size:50px'>20 + 20 + 20 minutes = the same hour.</div>
""", "No. 4", "ONE WORD")
    s3 = frame(f"""
<div style='position:absolute;left:0;right:0;top:130px'>{dual("*Remember more.*", style="font-size:160px")}</div>
<div class='S' style='position:absolute;left:90px;right:90px;top:350px;font-size:62px;line-height:1.05'>Across 317 experiments, spreading the same study time over days beat cramming it into one go.</div>
<div class='card' style='left:110px;right:110px;top:680px;padding:36px 40px'>
 <div class='dothis' style='font-size:76px;text-align:left'>Do this:</div>
 <div class='S' style='font-size:60px;text-align:left;line-height:1.02'>Split your next study hour into 3 sessions on 3 different days. <span class='pill' style='background:{F['pink']['p1']}'>Put them in your calendar.</span></div></div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1130px;font-size:22px;opacity:.85;line-height:1.45'>Cepeda, Pashler, Vul, Wixted &amp; Rohrer 2006, Psychological Bulletin<br>review of 317 experiments (184 articles)</div>
""", "No. 4", "ONE WORD")
    d = OUT / "lh-oneword-04"; d.mkdir(exist_ok=True)
    o25.shoot([page(s, FW, FH, f) for s, f in ((s1, "pink"), (s2, "cream"), (s3, "dots"))], [d / f"0{i+1}.jpg" for i in range(3)], FW, FH)


# ------------------------------------------------------------------ Stories (1080x1920, text inside y 250..1580)
STORIES = {
    "lh-st-1027-1": ("dots", "Quick question", "Which breaks a habit: / wanting it more, / or a *new place?*", "answer next →", None),
    "lh-st-1027-2": ("cream", "The answer", "*A new place.*", "Students who moved to a new university kept their old habits only where the setting stayed the same.",
                     "the full version is in today's post"),
    "lh-st-1028-1": ("pink", "Quick question", "Turn your phone / grey. Do you / pick it up / *less often?*", "answer next →", None),
    "lh-st-1028-2": ("dots", "The answer", "*No.* Just as often. / But you put it / down sooner.", "About 80 pick-ups a day either way, but about 20 minutes less a day on the phone.",
                     "tonight at 7 pm: the 15-second version"),
    "lh-st-1029-1": ("cream", "Quick question", "Does picturing / the win help / you *get it?*", "answer next →", None),
    "lh-st-1029-2": ("pink", "The answer", "*Not on its own.*", "People who daydreamed an ideal week felt less energy and got less done. Add the obstacle and a plan.",
                     "tonight at 7 pm: the 15-second version"),
}


def stories():
    pages, outs = [], []
    for sid, (field, label, big, note, pointer) in STORIES.items():
        is_q = pointer is None
        size = 128 if is_q else (150 if len(big) < 20 else 118)
        body = (f"<div style='position:absolute;left:90px;top:300px'><span class='label' style='font-size:30px;padding:12px 20px'>{label}</span></div>"
                f"<div style='position:absolute;left:80px;right:80px;top:420px'>{dual(big, field, style=f'font-size:{size}px')}</div>")
        if is_q:
            body += (f"<img class='obj' src='{obj('clock')}' style='position:absolute;left:390px;top:1010px;width:300px;transform:rotate(-6deg)'>"
                     f"<div class='hand' style='position:absolute;left:90px;right:90px;top:1440px;font-size:70px'>{note}</div>")
        else:
            body += (f"<div class='card' style='left:110px;right:110px;top:{720 if len(big) < 20 else 860}px;padding:40px 44px'>"
                     f"<div class='S' style='font-size:66px;line-height:1.1'>{note.replace(' / ', '<br>')}</div></div>"
                     f"<div class='hand' style='position:absolute;left:90px;right:90px;top:1360px;font-size:66px'>{pointer} ↓</div>")
        body += stamp(820, 1390 if is_q else 1180, 150, -10) if not is_q else stamp(800, 270, 150, 10)
        pages.append(page(body + f"<div class='mono' style='position:absolute;left:90px;top:1520px;font-size:24px;opacity:.75'>@lockedhourhq</div>",
                          1080, 1920, field))
        outs.append(OUT / "stories" / f"{sid}.jpg")
    o25.shoot(pages, outs, 1080, 1920)

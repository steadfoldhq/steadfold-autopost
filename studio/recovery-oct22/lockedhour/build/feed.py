"""Feed tiles + Story for the LH recovery (reveal-47, Monday handle, One Word No. 2, story lh-ch-1024-5)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lhkit import *  # noqa

OUT = Path("/home/claude/steadfold-autopost/media/recovery-oct22/lockedhour")
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1080, 1350

def frame(inner, n=None, series=""):
    foot = (f"<div class='mono' style='position:absolute;left:70px;bottom:52px;font-size:22px;opacity:.8'>@lockedhourhq</div>"
            f"<div class='mono' style='position:absolute;right:70px;bottom:52px;font-size:22px;opacity:.8'>{series}{(' · ' + n) if n else ''}</div>")
    border = f"<div style='position:absolute;inset:26px;border:7px solid {INK};border-radius:6px;pointer-events:none'></div>"
    return inner + foot + border

# ---------------- lh-1024-reveal-47-seconds ----------------
def reveal():
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:24px;padding:10px 16px'>Focus science · guess first</span></div>
<div style='position:absolute;left:70px;right:70px;top:170px'>{dual("How long do you / *stay on one / screen?*", style="font-size:150px;text-align:left")}</div>
<div style='position:absolute;left:560px;top:690px'>{ring(430, 0.0, "?:??", "now", notch=True)}</div>
<div style='position:absolute;left:90px;top:760px;width:440px' class='S'><div style='font-size:74px;text-align:left;line-height:1'>2004:<br><span class='pill' style='background:{F['dots']['p1']}'>2½ minutes.</span></div>
<div class='hand' style='font-size:58px;text-align:left;margin-top:34px'>today it's shorter<br>than one song →</div></div>
{stamp(860,100,150,10)}""", "1/3", "FOCUS SCIENCE")
    s2 = frame(f"""
<div style='position:absolute;left:0;right:0;top:110px'>{dual("*47 seconds.*", style="font-size:190px")}</div>
<div class='S' style='position:absolute;left:0;right:0;top:330px;font-size:70px'>on one screen, on average</div>
<div style='position:absolute;left:95px;top:500px;text-align:center'>{ring(400, 150/180, "2:30", "2004", col=BUTTER)}</div>
<div style='position:absolute;left:585px;top:500px;text-align:center'>{ring(400, 47/180, "0:47", "2016–2020", col=PINK)}</div>
<div class='hand' style='position:absolute;left:0;right:0;top:960px;font-size:58px'>it kept dropping, study after study.</div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1080px;font-size:23px;line-height:1.45;opacity:.85'>Rings to scale: full ring = 3 min.<br>Gloria Mark (UC Irvine), Attention Span, 2023;<br>UC Newsroom, 2024. Averages from her studies.</div>
""", "2/3", "FOCUS SCIENCE")
    s3 = frame(f"""
<div class='dothis' style='position:absolute;left:0;right:0;top:150px;text-align:center;font-size:120px'>Do this:</div>
<div class='card' style='left:110px;right:110px;top:330px;padding:56px 50px'>
 {dual("Next task: *full screen.* / One window, / until it's *done.*", style="font-size:104px")}</div>
<div style='position:absolute;left:390px;top:860px'>{ring(300, 1.0, "60:00", "", col=YEL)}</div>
<div class='hand' style='position:absolute;left:0;right:0;top:1180px;font-size:50px'>send this to your 40-tabs friend</div>
{stamp(850,1000,150,-10)}""", "3/3", "FOCUS SCIENCE")
    return [page(s, W, H, f) for s, f in ((s1, "dots"), (s2, "cream"), (s3, "pink"))]

# ---------------- Monday handle (replaces lh-1025-climb-one-percent) ----------------
def week_strip(y):
    days = "MTWTFSS"; x0 = 90; cells = ""
    for i, d in enumerate(days):
        if i == 0:
            cells += (f"<div style='position:absolute;left:{x0}px;top:{y}px;width:200px;height:220px;background:{YEL};border:6px solid {INK};"
                      f"border-radius:18px;box-shadow:9px 9px 0 {INK};font:900 120px/220px Inter Display,Inter;text-align:center;color:{INK}'>M</div>"
                      f"<div style='position:absolute;left:{x0+45}px;top:{y-120}px;width:110px;height:140px;border:22px solid {INK};"
                      f"border-bottom:none;border-radius:60px 60px 0 0'></div>")
        else:
            x = x0 + 230 + (i - 1) * 113
            cells += (f"<div style='position:absolute;left:{x}px;top:{y+30}px;width:96px;height:160px;border:4px solid {INK};"
                      f"border-radius:14px;background:#FFFDF6;font:800 54px/160px Inter Display,Inter;text-align:center;color:{INK};opacity:.75'>{d}</div>")
    return cells

def monday():
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:24px;padding:10px 16px'>Fresh-start days</span></div>
<div style='position:absolute;left:70px;right:70px;top:170px'>{dual("Monday isn't / magic.", style="font-size:170px;text-align:left")}</div>
<div class='S riso' style='position:absolute;left:70px;top:520px;font-size:170px;text-align:left'>It's a handle.</div>
{week_strip(900)}
<div class='hand' style='position:absolute;left:90px;top:1150px;font-size:54px;text-align:left'>grab it tonight, not "someday" →</div>
{stamp(860,96,150,10)}""", "1/3", "FRESH START")
    s2 = frame(f"""
<div class='S' style='position:absolute;left:0;right:0;top:120px;font-size:96px'>At the start of a week,</div>
<div style='position:absolute;left:0;right:0;top:230px'>{dual("gym visits / jumped *33.4%.*", style="font-size:150px")}</div>
<div class='card' style='left:110px;right:110px;top:620px;padding:40px 46px'>
 <div class='mono' style='font-size:30px;line-height:1.5'>start of a week ....... +33.4%<br>start of a month ...... +14.4%<br>start of a semester ... +47.1%</div>
 <div class='S' style='font-size:52px;text-align:left;margin-top:22px;line-height:1.05'>New starts make people <span class='pill' style='background:{F['cream']['p1']}'>try again.</span></div></div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1080px;font-size:22px;line-height:1.45;opacity:.85'>Dai, Milkman &amp; Riis 2014, Management Science. Gym records of<br>~12,000 students at one US university, 2010–11, vs. baseline.<br>Correlational: it shows when people start,<br>not that Mondays cause success.</div>
""", "2/3", "FRESH START")
    s3 = frame(f"""
<div class='dothis' style='position:absolute;left:0;right:0;top:140px;text-align:center;font-size:120px'>Do this:</div>
<div class='card' style='left:100px;right:100px;top:320px;padding:50px 46px'>
 {dual("Tonight, pick *one* thing. / Write *when* you start:", style="font-size:84px")}
 <div class='hand' style='font-size:76px;margin-top:26px;color:{INK}'>"Monday, 8 am, after coffee."</div></div>
<div class='S' style='position:absolute;left:0;right:0;top:900px;font-size:72px'>Use the handle. <span class='pill' style='background:{F['pink']['p1']}'>Don't wait for it.</span></div>
<div class='hand' style='position:absolute;left:0;right:0;top:1040px;font-size:48px;padding-right:140px'>missed Monday? Tuesday has a handle too.</div>
{stamp(850,1110,140,-10)}""", "3/3", "FRESH START")
    return [page(s, W, H, f) for s, f in ((s1, "dots"), (s2, "cream"), (s3, "pink"))]

# ---------------- One Word No. 2: Batch ----------------
def oneword():
    s1 = frame(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:30px;padding:12px 20px'>One Word · No. 2</span></div>
<div style='position:absolute;left:70px;right:70px;top:190px'>{dual("Inbox open / *all day* again?", style="font-size:124px;text-align:left")}</div>
<div style='position:absolute;left:60px;top:760px;width:960px;height:120px;background:{PINK};opacity:.85;border-radius:60px'></div>
<div class='S riso' style='position:absolute;left:40px;right:40px;top:540px;font-size:340px;text-align:left'>Batch.</div>
<img class='obj' src='{obj("clock")}' style='position:absolute;left:740px;top:860px;width:240px;transform:rotate(8deg)'>
<div class='hand' style='position:absolute;left:90px;top:960px;font-size:60px;text-align:left'>3 email checks a day,<br>not all day</div>
<div class='mono' style='position:absolute;left:90px;top:1150px;font-size:24px;opacity:.8'>one word that guards your focus</div>
""", "No. 2", "ONE WORD")
    marks = [((9.5 % 12) / 12, PINK), ((1.0) / 12, PINK), ((4.5) / 12, PINK)]
    s2 = frame(f"""
<div style='position:absolute;left:0;right:0;top:110px'>{dual("*3 checks.* / That's it.", style="font-size:140px")}</div>
<div style='position:absolute;left:290px;top:420px'>{ring(500, 0, "", "", col=PINK, notch=True, marks=marks)}</div>
<div class='mono' style='position:absolute;left:150px;top:560px;font-size:34px;font-weight:700'>9:30</div>
<div class='mono' style='position:absolute;left:800px;top:470px;font-size:34px;font-weight:700'>1:00</div>
<div class='mono' style='position:absolute;left:790px;top:830px;font-size:34px;font-weight:700'>4:30</div>
<div class='S' style='position:absolute;left:0;right:0;top:960px;font-size:70px'>Tab <span class='pill' style='background:{F['cream']['p1']}'>closed</span> in between.</div>
<div class='hand' style='position:absolute;left:0;right:0;top:1070px;font-size:48px'>urgent? people can call or text.</div>
""", "No. 2", "ONE WORD")
    s3 = frame(f"""
<div style='position:absolute;left:0;right:0;top:130px'>{dual("*Less stress.*", style="font-size:170px")}</div>
<div class='S' style='position:absolute;left:90px;right:90px;top:360px;font-size:66px;line-height:1.05'>In a 2-week study, the week people checked email 3 times a day felt calmer than the week they checked whenever.</div>
<div class='card' style='left:110px;right:110px;top:690px;padding:36px 40px'>
 <div class='dothis' style='font-size:76px;text-align:left'>Do this:</div>
 <div class='S' style='font-size:66px;text-align:left;line-height:1.02'>Write your 3 check times on a sticky note. <span class='pill' style='background:{F['pink']['p1']}'>Close the tab.</span></div></div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1130px;font-size:22px;opacity:.85'>Kushlev &amp; Dunn 2015, Computers in Human Behavior · 124 adults</div>
""", "No. 2", "ONE WORD")
    return [page(s, W, H, f) for s, f in ((s1, "pink"), (s2, "cream"), (s3, "dots"))]

def story_1024_5(cover_jpg):
    SW, SH = 1080, 1920
    body = f"""
<div class='hand' style='position:absolute;left:0;right:0;top:250px;font-size:64px'>focus science</div>
<div style='position:absolute;left:0;right:0;top:400px'>{dual("*2½ minutes* then. / Now?", style="font-size:150px")}</div>
<img src='{edkit.uri(cover_jpg)}' style='position:absolute;left:250px;top:720px;width:580px;border:6px solid {INK};border-radius:10px;box-shadow:14px 14px 0 {INK};transform:rotate(-3deg)'>
<div class='hand' style='position:absolute;left:0;right:0;top:1480px;font-size:68px'>the answer is in today's post ↑</div>
{stamp(90,1560,140,-10)}"""
    return page(body, SW, SH, "dots")

if __name__ == "__main__":
    which = sys.argv[1:] or ["reveal", "monday", "oneword", "story"]
    if "reveal" in which:
        d = OUT / "lh-1024-reveal-47-seconds"; d.mkdir(exist_ok=True)
        shoot(reveal(), [d / f"0{i+1}.jpg" for i in range(3)], W, H)
    if "monday" in which:
        d = OUT / "lh-1025-monday-handle"; d.mkdir(exist_ok=True)
        shoot(monday(), [d / f"0{i+1}.jpg" for i in range(3)], W, H)
    if "oneword" in which:
        d = OUT / "lh-oneword-02-batch"; d.mkdir(exist_ok=True)
        shoot(oneword(), [d / f"0{i+1}.jpg" for i in range(3)], W, H)
    if "story" in which:
        d = OUT / "stories"; d.mkdir(exist_ok=True)
        shoot([story_1024_5(OUT / "lh-1024-reveal-47-seconds/01.jpg")], [d / "lh-ch-1024-5.jpg"], 1080, 1920)

#!/usr/bin/env python3
"""Hourback feed posts built Oct 26 2026 (Hourback maker). Reuses covers.py / specs.py / edkit.py by import; edits none of them.

    python3 studio/editorial/oct26_hourback_feed.py mechanic   -> media/studio-oct26/hourback/hb-1027-mechanic-questions/0N.jpg
    python3 studio/editorial/oct26_hourback_feed.py day10      -> media/studio-oct26/hourback/hb-day10-pancakes-for-6/0N.jpg
    python3 studio/editorial/oct26_hourback_feed.py stories    -> media/studio-oct26/hourback/stories/hb-st-10DD-N.jpg

mechanic = Tue Oct 27 12:00, style 'prompt card with yellow [bracket] chips'. Real run: studio/editorial/hb-oct26-run-mechanic-questions.txt.
day10    = 'AI, for real · Day 10' (Fri Oct 30 17:45). Same series layout as Day 8/9 (specs 'series' fmt, pills cover). The reply on
           slide 3 comes from the fresh verbatim run studio/editorial/hb-oct25-run-day9.txt (claude -p, Oct 25); slide 2 is re-lettered
           to the run's real prompt wording.
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import glob  # noqa: E402
_g = glob.glob
glob.glob = lambda p, *a, **k: _g(p, *a, **k) or _g(p.replace("chrome-linux/", "chrome-linux64/"), *a, **k)
import specs  # noqa: E402
import covers as C  # noqa: E402
glob.glob = _g
K = C.K
_obj = K.obj
K.obj = lambda name, *a, **k: "" if name in ("point", "ok") else _obj(name, *a, **k)  # retired props never render

HB = "hourback"
W, H = 1080, 1350
OUT = C.REPO / "media/studio-oct26/hourback"
SUN = "#FFC94D"


def chip(t):
    return (f'<span style="background:{SUN};border:3px solid #2A1D47;border-radius:14px;padding:0 12px 2px;box-decoration-break:clone;'
            f'-webkit-box-decoration-break:clone;font-weight:700">{t}</span>')


def prompt_card(top, size=50):
    ink = "#2A1D47"
    txt = (f"My {chip('car')} makes {chip('a squeal when I brake')}. Give me 5 short questions to ask the {chip('mechanic')} "
           f"so I understand the quote before I say yes.")
    return (f'<div style="position:absolute;left:80px;right:80px;top:{top}px;background:#FFFFFF;border:4px solid {ink};border-radius:36px;'
            f'box-shadow:0 16px 0 {ink};padding:34px 46px 40px;z-index:3;color:{ink}">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:22px">'
            f'<span style="font:700 28px Inter;letter-spacing:.12em;text-transform:uppercase;opacity:.7">Copy this prompt</span>'
            f'<span style="font:700 26px Inter;background:#2A1D47;color:#FFF5EA;border-radius:99px;padding:8px 22px">⧉ copy</span></div>'
            f'<div style="font:500 {size}px/1.5 Inter">{txt}</div></div>')


def mech_cover():
    f = K.FIELDS[HB]["plum"]
    body = C.head(HB, f, "Before you / say yes to / *the mechanic*", 70, 440, 170)
    body += prompt_card(580)
    body += K.save_line("change the yellow words to yours", 70, 1150, 760, 58, -3, HB)
    body += K.stamp(HB, W - 220, H - 200, 165, -12)
    body += '<div class="hand" style="position:absolute;left:90px;top:1250px;font-size:48px;z-index:5">swipe →</div>'
    return C.page(HB, "plum", body, W, H)


Q1 = "“What exactly is causing the squeal?”"
Q4 = "“Can you break the quote into parts and labour, and what grade of parts is that?”"


def mech_reply():
    f = K.FIELDS[HB]["indi"]
    ink = f["ink"]
    body = C.head(HB, f, "It wrote 5. / *Here are 2:*", 90, 330, 170)
    row = lambda n, t, bg: (f'<div style="display:flex;gap:28px;align-items:flex-start;padding:26px 4px">'
                            f'<span class="S" style="flex:none;width:92px;height:92px;border-radius:50%;background:{bg};border:3px solid {ink};'
                            f'font-size:60px;line-height:84px;text-align:center">{n}</span>'
                            f'<span style="font:700 52px/1.18 Fraunces">{t}</span></div>')
    body += (f'<div style="position:absolute;left:80px;right:80px;top:470px;background:#FFFFFF;border:3px solid {ink};border-radius:36px;'
             f'padding:22px 44px 18px;color:{ink};box-shadow:0 14px 0 {ink};z-index:2">'
             f'<div style="font:600 22px Inter;letter-spacing:.06em;white-space:nowrap;text-transform:uppercase;opacity:.7;padding-top:8px">Claude\'s reply, word for word · questions 1 and 4</div>'
             + row(1, Q1, f["p1"]) + f'<div style="border-top:3px solid rgba(20,26,85,.14)"></div>' + row(4, Q4, f["p2"]) + '</div>')
    body += K.save_line("all 5 are in the caption", 120, 1110, 600, 60, -3, HB)
    body += f'<div style="position:absolute;right:60px;top:40px;font:600 30px/1 Fraunces;color:{ink};opacity:.55;z-index:5">2/3</div>'
    body += K.stamp(HB, W - 230, H - 230, 170, -12)
    return C.page(HB, "indi", body, W, H)


def mech_do():
    f = K.FIELDS[HB]["yel"]
    ink = f["ink"]
    body = f'<div class="hand" style="position:absolute;left:0;right:0;top:150px;text-align:center;font-size:110px;z-index:3">Do this:</div>'
    body += C.head(HB, f, "Paste it into / *ChatGPT, Claude* / *or Gemini*", 300, 470, 150)
    body += C.head(HB, f, "before you call the shop.", 790, 120, 80)
    body += (f'<div style="position:absolute;left:150px;right:150px;top:960px;background:#FFF0C2;border:3px solid {ink};border-radius:28px;'
             f'box-shadow:0 10px 0 {ink};padding:24px 34px;font:700 40px/1.3 Inter;color:{ink};text-align:center;z-index:3;transform:rotate(-1deg)">'
             f'No plate number or VIN needed.<br>“My car” is enough.</div>')
    body += f'<div style="position:absolute;right:60px;top:40px;font:600 30px/1 Fraunces;color:{ink};opacity:.55;z-index:5">3/3</div>'
    body += K.stamp(HB, W - 240, H - 230, 170, -12)
    return C.page(HB, "yel", body, W, H)


# ---------------------------------------------------------------- Day 10 (relabel of the parked Day 9 pancakes post)
D10 = "studio-oct26/hourback/hb-day10-pancakes-for-6"
specs.POSTS[D10] = dict(
    brand=HB, fmt="series",
    cover=dict(lay="pills", f="orng", kicker="ai, for real · day 10", text="Recipe for 4. / *Six are* / *coming?*", obj="chat",
               at="bl", save="new one<br>every Mon · Wed · Fri"),
    slides=[dict(f="indi", text="Serves 4. / Rewrite it / *for 6 people.*", sub="type this above any recipe"),
            dict(f="yel", text="Pancakes for 6. / *It wrote:*",
                 items=["2¼ cups flour", "1¾ cups + 2 tbsp milk", "1½ eggs<br>(or 1 egg plus 1 yolk)"],
                 sub="real reply, shortened")])
D10_SAVE = "3 of 7 shown, all 7 in the caption,<br>we checked every one"


def pancakes(x, y, w=380, rot=-6):
    """One drawn object for the Day 10 cover: a pancake stack with butter and syrup (ink outlines, brand colours)."""
    ink = "#2A1D47"
    cakes = "".join(f'<ellipse cx="190" cy="{y0}" rx="165" ry="38" fill="#F4B76A" stroke="{ink}" stroke-width="6"/>'
                    f'<path d="M25 {y0} Q25 {y0 + 30} 70 {y0 + 40} L310 {y0 + 40} Q355 {y0 + 30} 355 {y0}" fill="#E39A4B" stroke="{ink}" stroke-width="6"/>'
                    for y0 in (230, 190, 150, 110))
    svg = (f'<svg width="{w}" height="{w * 0.9:.0f}" viewBox="0 0 380 340">'
           f'<ellipse cx="190" cy="285" rx="185" ry="42" fill="#FFFFFF" stroke="{ink}" stroke-width="6"/>{cakes}'
           f'<path d="M80 108 Q120 140 150 112 Q170 150 200 115 Q240 145 290 110 L300 100 L70 100 Z" fill="#B5652A" stroke="{ink}" stroke-width="5"/>'
           f'<path d="M285 112 Q300 170 292 196" fill="none" stroke="#B5652A" stroke-width="14" stroke-linecap="round"/>'
           f'<rect x="160" y="62" width="70" height="44" rx="10" fill="#FFC94D" stroke="{ink}" stroke-width="6" transform="rotate(-8 195 84)"/></svg>')
    return f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);z-index:3">{svg}</div>'


D10_PROMPT = (f"{chip('This pancake recipe')} serves {chip('4')}. Rewrite the ingredient list for {chip('6')} people. Just the list.")


def d10_slide2():
    f = K.FIELDS[HB]["indi"]
    ink = f["ink"]
    body = C.head(HB, f, "In ChatGPT, Claude or Gemini,", 110, 90, 64)
    body += C.head(HB, f, "type this / *above any recipe:*", 200, 330, 160)
    body += (f'<div style="position:absolute;left:80px;right:80px;top:580px;background:#FFFFFF;border:4px solid {ink};border-radius:36px;'
             f'box-shadow:0 16px 0 {ink};padding:34px 46px 40px;z-index:3;color:{ink}">'
             f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:22px">'
             f'<span style="font:700 28px Inter;letter-spacing:.12em;text-transform:uppercase;opacity:.7">Copy this prompt</span>'
             f'<span style="font:700 26px Inter;background:{ink};color:#FFF5EA;border-radius:99px;padding:8px 22px">⧉ copy</span></div>'
             f'<div style="font:500 54px/1.5 Inter">{D10_PROMPT}</div></div>')
    body += K.save_line("tip: add “round to cups and spoons I own”", 60, 990, 960, 58, -3, HB)
    body += f'<div style="position:absolute;right:60px;top:40px;font:600 30px/1 Fraunces;color:{ink};opacity:.55;z-index:5">2/3</div>'
    body += K.stamp(HB, W - 230, H - 230, 170, -12)
    return C.page(HB, "indi", body, W, H)


def d10_build(r):
    spec = specs.POSTS[D10]
    d = C.REPO / "media" / D10
    d.mkdir(parents=True, exist_ok=True)
    c = spec["cover"]
    _o = K.obj
    C.K.obj = lambda name, *a, **k: pancakes(30, 900) if name == "chat" else _o(name, *a, **k)
    try:
        cov = C.lay_pills(HB, c)
    finally:
        C.K.obj = _o
    out = [r.shot(C.page(HB, c["f"], cov, W, H), W, H, d / "01.jpg"),
           r.shot(d10_slide2(), W, H, d / "02.jpg"),
           r.shot(C.page(HB, "yel", C.inner(HB, spec["slides"][1], 2, 3) + K.save_line(D10_SAVE, 80, 1130, 720, 50, -3, HB), W, H),
                  W, H, d / "03.jpg")]
    return out


# ---------------------------------------------------------------- Stories (Tue-Thu, 2 frames, 12:30 + 12:31)
STORIES = {
    "hb-st-1027-1": ("indi", "Car repair quote? / Ask *before* / *you say yes.*", "AI can write the questions for you.", None),
    "hb-st-1027-2": ("plum", "“What exactly / *is causing* / *the squeal?*”", "1 of the 5 questions Claude wrote for us.",
                     "All 5 + the prompt to copy: today's post on our page"),
    "hb-st-1028-1": ("orng", "Google can name / a song you / *only hum?*", "", None),
    "hb-st-1028-2": ("indi", "Google app → mic → / *Search a song.*", "Then hum, whistle or sing the tune.",
                     "Tonight at 7 pm: a 15-second Reel on our page"),
    "hb-st-1029-1": ("yel", "Bill went up? / AI can tell you / *why.*", "", None),
    "hb-st-1029-2": ("plum", "Paste last month's and / this month's bill into / *ChatGPT, Claude* / *or Gemini.* / Ask: *what changed?*",
                     "Cover your account number and address first.", "Tonight at 7 pm: a 15-second Reel on our page"),
}


def story(sid):
    fld, text, sub, point = STORIES[sid]
    f = K.FIELDS[HB][fld]
    ink = f["ink"]
    q = sid.endswith("-1")
    body = (f'<div class="hand" style="position:absolute;left:0;right:0;top:330px;text-align:center;font-size:64px;transform:rotate(-3deg);z-index:3">'
            f'{"quick question" if q else "the answer"}</div>')
    body += C.head(HB, f, text, 440, 560, 170)
    body += (f'<div style="position:absolute;left:110px;right:110px;top:1040px;text-align:center;font:600 50px/1.3 Inter;color:{ink};z-index:3">{sub}</div>')
    if q:
        body += K.obj("chat", 120, 1230, 280, -6)
        body += '<div class="hand" style="position:absolute;left:0;right:0;top:1470px;text-align:center;font-size:70px;z-index:4">tap for the answer →</div>'
        body += K.stamp(HB, 800, 1240, 150, 12)
    else:
        body += (f'<div style="position:absolute;left:110px;right:110px;top:1250px;background:#FFFFFF;border:3px solid {ink};border-radius:30px;'
                 f'box-shadow:0 10px 0 {ink};padding:26px 30px;font:700 46px/1.25 Inter;color:{ink};text-align:center;z-index:3">{point}</div>')
        body += K.stamp(HB, 480, 1455, 120, 12)
    return C.page(HB, fld, body, 1080, 1920)


if __name__ == "__main__":
    what = sys.argv[1]
    r = C.R()
    try:
        if what == "day10":
            print(d10_build(r))
        if what == "mechanic":
            d = OUT / "hb-1027-mechanic-questions"; d.mkdir(parents=True, exist_ok=True)
            for i, fn in enumerate([mech_cover, mech_reply, mech_do], 1):
                print(r.shot(fn(), W, H, d / f"{i:02d}.jpg"))
        elif what == "stories":
            d = OUT / "stories"; d.mkdir(parents=True, exist_ok=True)
            for sid in STORIES:
                print(r.shot(story(sid), 1080, 1920, d / f"{sid}.jpg"))
    finally:
        r.close()

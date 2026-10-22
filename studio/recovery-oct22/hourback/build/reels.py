#!/usr/bin/env python3
"""The three Hourback recovery Reels (Oct 22). python3 reels.py [fridge|week|sparkle] [--frame t ...]"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from takereel import *  # noqa

OUT = REPO / "media" / "recovery-oct22" / "hourback"
TRACK = REPO / "media/music/library/v4/hb-x-ta-da-funk.mp3"   # HB v4 master, -14.2 LUFS, drop 7.93 s, 105.5 bpm
CREDIT = "Claude, by Anthropic · run Oct 22, 2026"


def stamp(x=90, y=1440, s=170):
    return edkit.stamp("hourback", x, y, s)


def phone(x, y, w, rot, a, b, fl=10):
    return T(edkit.phone(x, y, w, rot), a, b, "none", float=fl)


# ---------------------------------------------------------------- fridge (Sat Oct 24, 7 pm)
def fridge():
    dur = 14.0
    hookf = F["yel"]

    def hook(a, b, first):
        fx = "none" if first else "iris"
        ans = card(
            f'<div style="font:700 28px Inter;letter-spacing:.05em;color:#8E89A3;text-transform:uppercase">TAKE 2 · the answer</div>'
            f'<div style="font:800 54px/1.12 Inter;margin:12px 0 22px">Spinach, bean &amp; egg quesadillas</div>'
            + chip("20 min", SUN) + chip("serves 2", F["indi"]["bg"]) + chip("what you had", F["yel"]["p1"]), w=760, pad=36)
        inner = (T(serif("Open fridge, / no plan?", 132, hookf), a, b, "none", extra="left:90px;top:330px") +
                 T(serif("*You already / have dinner.*", 132, hookf), a, b, "none", extra="left:90px;top:610px") +
                 T(ans, a + (0 if first else 0.25), b, "none" if first else "drop", 0.42, "left:110px;top:930px", base="rotate(-2deg)") +
                 phone(840, 1230, 160, 14, a, b) +
                 T(hand("one sentence. 20 minutes.", 66, width=700), a + (0.1 if first else 0.5), b, "pop", 0.3, "left:60px;top:1340px") +
                 T(stamp(110, 1470, 160), a, b))
        return scene(hookf["bg"], a, b, fx, inner, d=0.45)

    s = [hook(0, 2.4, True), rewind(2.4, 3.0)]
    g = dict(bg=GREY_BG, p1="#C9C4D6", p2="#EDEAF2")
    t1 = (T(tab("TAKE 1", dim=True), 3.0, 5.5, "none", extra="left:90px;top:300px") +
          T('<div data-roll="6:${String(v).padStart(2,\'0\')} pm" data-t0="3.05" data-t1="5.2" data-v0="2" data-v1="19" '
            f'style="font-family:\'DM Serif Display\';font-size:210px;color:{GREY_INK};letter-spacing:-.03em;width:900px;text-align:center"></div>',
            3.0, 5.5, "whipL", 0.3, "left:90px;top:420px") +
          T(serif("Staring.", 120, g, GREY_INK), 3.3, 5.5, "pop", 0.25, "left:90px;top:720px") +
          T(serif("Scrolling.", 120, g, GREY_INK), 3.87, 5.5, "pop", 0.25, "left:90px;top:860px") +
          T(serif("*Ordering takeout.*", 120, g, GREY_INK), 4.44, 5.5, "slam", 0.22, "left:90px;top:1000px") +
          T(hand("same evening, take 1", 62, GREY_INK, 2), 3.5, 5.5, "pop", 0.3, "left:90px;top:1300px"))
    s.append(scene(GREY_BG, 3.0, 5.5, "whipL", t1, d=0.3, grey=True))
    s.append(clapper(5.5, 5.95))
    pr = "In my fridge: 4 eggs, spinach, cheddar, 2 tortillas, half an onion, leftover rice, black beans, salsa. One dinner for 2 in 20 minutes. Just the steps."
    steps = ["1. Soften the onion, add beans + salsa", "2. Wilt the spinach, scramble the eggs", "3. Fill, fold, toast 2–3 min a side"]
    ans = (f'<div style="font:700 26px Inter;letter-spacing:.05em;color:#8E89A3;text-transform:uppercase">{CREDIT}</div>'
           f'<div style="font:800 50px/1.1 Inter;margin:10px 0 6px">Spinach, bean &amp; egg quesadillas</div>'
           f'<div style="font:600 34px Inter;color:#6B6480;margin-bottom:18px">about 20 min · serves 2</div>'
           + "".join(T(f'<div style="font:600 36px/1.25 Inter;padding:10px 0;border-top:3px dashed #D9D3E6;width:820px">{x}</div>',
                       8.45 + i * 0.57, 11.0, "up", 0.25, f"position:relative") for i, x in enumerate(steps))
           + '<div style="font:500 26px Inter;color:#8E89A3;margin-top:10px">real reply, shortened</div>')
    t2 = (T(tab("TAKE 2"), 5.95, 11.0, "none", extra="left:90px;top:300px") +
          T(typed(pr, 6.0, 7.55, 38), 5.95, 11.0, "up", 0.25, "left:90px;top:400px") +
          T(card(ans, w=900, pad=36), 7.93, 11.0, "drop", 0.4, "left:90px;top:840px", base="rotate(-1deg)") +
          T(hand("6:22 pm. dinner's on.", 70), 10.05, 11.0, "pop", 0.3, "left:90px;top:1540px"))
    s.append(scene(F["plum"]["bg"], 5.95, 11.0, "wipeD", t2, d=0.25))
    do = (T('<div class="hand" style="font-size:110px;color:%s">Do this:</div>' % ACC, 11.0, 13.4, "slam", 0.2, "left:90px;top:330px") +
          T(card(serif("List your fridge. / Ask for *one / 20-min dinner.*", 104, F["plum"], width=820), w=900, pad=40),
            11.15, 13.4, "pop", 0.3, "left:90px;top:520px") +
          T(hand("check: it added oil. did you have it?", 58, ACC, -2), 11.85, 13.4, "pop", 0.25, "left:90px;top:1100px") +
          T(stamp(110, 1440, 150), 11.0, 13.4))
    s.append(scene(F["indi"]["bg"], 11.0, 13.4, "wipe", do, d=0.28))
    s.append(hook(12.9, 99, False))
    return dur, page(s, [2.62, 4.44, 5.62, 7.93, 11.0]), 0.95


# ---------------------------------------------------------------- week card (Sun Oct 25, 7 pm)
WEEK = [("Mon", "Bins out by 7 am. Reply C to confirm the dentist."),
        ("Tue", "Milk + dog food. Dentist at 4:15 pm."),
        ("Wed", "Send $6 for pizza lunch. No soccer."),
        ("Thu", "Pizza lunch. Soccer 6 pm, same field."),
        ("Fri", "Picture day retakes, morning."),
        ("Sat", "Your partner's mom's birthday.")]


def weekrows(a=None, step=0.4, end=99, size=34, hi=None):
    out = ""
    for i, (d, x) in enumerate(WEEK):
        bg = f"background:{SUN};" if hi == i else ""
        row = (f'<div style="display:flex;gap:20px;padding:9px 6px;border-top:3px dashed #D9D3E6;width:830px;{bg}border-radius:10px">'
               f'<div style="font:800 {size}px Inter;width:84px;flex:none">{d}</div><div style="font:500 {size}px/1.25 Inter">{x}</div></div>')
        out += row if a is None else T(row, a + i * step, end, "up", 0.22, "position:relative")
    return out


def week():
    dur = 14.5
    hf = F["indi"]

    def hook(a, b, first):
        fx = "none" if first else "iris"
        pv = card(f'<div style="font:800 46px Inter;margin-bottom:10px">Your week</div>' + weekrows(size=30), w=860, pad=32)
        inner = (T(serif("Sunday night?", 136, hf), a, b, "none", extra="left:90px;top:320px") +
                 T(serif("*Your week fits / on one card.*", 120, hf), a, b, "none", extra="left:90px;top:470px") +
                 T(pv, a + (0 if first else 0.25), b, "none" if first else "drop", 0.42, "left:110px;top:780px", base="rotate(-2deg)") +
                 phone(850, 1300, 150, 14, a, b) +
                 T(hand("one sentence did this", 66, width=700), a + (0.1 if first else 0.5), b, "pop", 0.3, "left:60px;top:1430px") +
                 T(stamp(110, 1530, 140), a, b))
        return scene(hf["bg"], a, b, fx, inner, d=0.45)

    s = [hook(0, 2.4, True), rewind(2.4, 3.0)]
    msgs = ["Reminder: your cleaning is Tue Oct 27, 4:15 pm. Reply C", "Pizza lunch Thursday. Send $6 by Wednesday.",
            "Soccer moved from Wed to Thu, 6 pm", "Garbage and green bin: Monday, by 7 am",
            "grab milk + dog food before Tue? also my mom's bday Sat"]
    g = dict(bg=GREY_BG, p1="#C9C4D6", p2="#EDEAF2")
    bub = ""
    for i, m in enumerate(msgs):
        left = 90 if i % 2 == 0 else 250
        bub += T(f'<div style="max-width:740px;background:#F4F2F8;border:4px solid {GREY_INK};border-radius:30px 30px 30px 8px;'
                 f'padding:18px 26px;font:500 36px/1.25 Inter;color:{GREY_INK}">{m}</div>',
                 3.1 + i * 0.4, 5.6, "whipL" if i % 2 else "whipR", 0.22, f"left:{left}px;top:{420 + i * 170}px")
    t1 = (T(tab("TAKE 1", dim=True), 3.0, 5.6, "none", extra="left:90px;top:300px") + bub +
          T('<div style="background:%s;padding:20px 30px;border-radius:24px">' % GREY_BG +
            serif("*5 messages.* / 0 plan.", 120, g, GREY_INK, width=780) + '</div>', 5.05, 5.6, "slam", 0.18,
            "left:100px;top:1300px"))
    s.append(scene(GREY_BG, 3.0, 5.6, "whipL", t1, d=0.3, grey=True))
    s.append(clapper(5.6, 6.0))
    pr = "Turn these into my week, Mon to Sat. One line a day: what to do, by when."
    ans = (f'<div style="font:700 26px Inter;letter-spacing:.05em;color:#8E89A3;text-transform:uppercase">{CREDIT}</div>'
           f'<div style="font:800 50px Inter;margin:8px 0 8px">Your week</div>' + weekrows(8.2, 0.42, 11.3, 35) +
           '<div style="font:500 26px Inter;color:#8E89A3;margin-top:8px">real reply, quoted exactly · made-up messages</div>')
    t2 = (T(tab("TAKE 2"), 6.0, 11.3, "none", extra="left:90px;top:300px") +
          T(typed(pr, 6.05, 7.3, 42, "pasted the 5 messages, then:"), 6.0, 11.3, "up", 0.25, "left:90px;top:400px") +
          T(card(ans, w=900, pad=34), 7.93, 11.3, "drop", 0.4, "left:90px;top:760px", base="rotate(-1deg)") +
          T(hand("sunday, sorted.", 74), 10.75, 11.3, "pop", 0.25, "left:90px;top:1560px"))
    s.append(scene(F["plum"]["bg"], 6.0, 11.3, "wipeD", t2, d=0.25))
    chk = card(f'<div style="font:700 30px Inter;color:#8E89A3;letter-spacing:.05em;text-transform:uppercase;margin-bottom:8px">the check caught one</div>'
               + serif("“before Tue” ≠ *Tue.*", 92, F["plum"], width=800), w=900, pad=34)
    do = (T('<div class="hand" style="font-size:110px;color:%s">Do this:</div>' % ACC, 11.3, 13.9, "slam", 0.2, "left:90px;top:320px") +
          T(card(serif("Paste the week's / messages. Ask for / *one line a day.*", 96, F["plum"], width=820), w=900, pad=36),
            11.42, 13.9, "pop", 0.3, "left:90px;top:490px") +
          T(chk, 12.15, 13.9, "drop", 0.3, "left:90px;top:1010px", base="rotate(1.5deg)") +
          T(stamp(110, 1450, 140), 11.3, 13.9))
    s.append(scene(F["indi"]["bg"], 11.3, 13.9, "wipe", do, d=0.28))
    s.append(hook(13.4, 99, False))
    return dur, page(s, [2.62, 5.05, 5.72, 7.93, 12.15]), 0.95


# ---------------------------------------------------------------- sparkle (Sun Oct 25, 8:45 am) — same facts, recut
def sparkle_reel():
    dur = 13.0
    hf = F["plum"]

    def hook(a, b, first):
        fx = "none" if first else "iris"
        inner = (T(edkit.dual(f'That {sparkle(150)} / button?', hf, cls="S", style=f"font-size:150px;color:{INK};width:900px"),
                   a, b, "none", extra="left:90px;top:360px") +
                 T(serif("*It's AI.*", 200, hf), a, b, "none", extra="left:90px;top:780px") +
                 T(hand("you already use it", 76), a + 0.15, b, "pop", 0.3, "left:90px;top:1030px") +
                 phone(700, 1150, 200, 12, a, b, 12) +
                 T(stamp(110, 1400, 170), a, b))
        return scene(hf["bg"], a, b, fx, inner, d=0.45)

    s = [hook(0, 1.6, True)]
    nf = F["indi"]
    num = (T(serif("About", 90, nf), 1.6, 4.0, "none", extra="left:90px;top:380px") +
           T(serif("*1 billion*", 210, nf), 1.6, 4.0, "zoom", 0.3, "left:90px;top:500px") +
           T(serif("people use *Meta AI* / every month", 92, nf), 2.55, 4.0, "up", 0.25, "left:90px;top:780px") +
           T('<div style="font:600 32px Inter;color:#5F5975;width:900px;text-align:center">Meta, May 2025</div>', 2.9, 4.0, "up", 0.25,
             "left:90px;top:1030px"))
    s.append(scene(nf["bg"], 1.6, 4.0, "zoom", num, d=0.25))
    yf = F["yel"]
    rows = [("WhatsApp", "Meta AI"), ("iPhone", "Writing Tools"), ("Gmail", "Gemini")]
    apps = "".join(T(f'<div style="font:700 44px Inter;color:#5F5975;width:900px;text-align:center;margin-bottom:26px">{a_}</div>'
                     + serif(f"*{b_}*", 116, yf), 4.2 + i * 0.75, 7.4, "whipL" if i % 2 == 0 else "whipR", 0.28,
                     f"left:90px;top:{360 + i * 230}px") for i, (a_, b_) in enumerate(rows))
    apps += T('<div style="font:600 32px Inter;color:#5F5975;width:900px;text-align:center">on newer phones and plans; varies by country</div>',
              6.5, 7.4, "up", 0.25, "left:90px;top:1060px")
    s.append(scene(yf["bg"], 4.0, 7.4, "whipL", apps, d=0.3))
    why = (T(hand("because…", 96), 7.4, 9.4, "pop", 0.25, "left:90px;top:400px") +
           T(serif("AI moved into", 120, hf), 7.55, 9.4, "up", 0.25, "left:90px;top:560px") +
           T(serif("*apps you / already use.*", 130, hf), 7.93, 9.4, "slam", 0.22, "left:90px;top:700px"))
    s.append(scene(hf["bg"], 7.4, 9.4, "iris", why, d=0.3))
    do = (T('<div class="hand" style="font-size:110px;color:%s">Do this:</div>' % ACC, 9.4, 12.4, "slam", 0.2, "left:90px;top:360px") +
          T(card(edkit.dual(f'Tap the {sparkle(96)} once / today, on one / *real task.*', hf, cls="S",
                            style=f"font-size:104px;color:{INK};width:820px"), w=900, pad=40), 9.55, 12.4, "pop", 0.3, "left:90px;top:560px") +
          T(hand("then check what it says", 70), 10.4, 12.4, "pop", 0.25, "left:90px;top:1080px") +
          T(stamp(110, 1440, 150), 9.4, 12.4))
    s.append(scene(nf["bg"], 9.4, 12.4, "wipe", do, d=0.28))
    s.append(hook(11.9, 99, False))
    return dur, page(s, [1.62, 4.2, 7.93, 9.4]), 0.8


REELS = {"fridge": ("hb-reel-1024-fridge-dinner-r", fridge), "week": ("hb-reel-1025-week-card", week),
         "sparkle": ("hb-reel-1025am-talk-dont-type-r", sparkle_reel)}

if __name__ == "__main__":
    key = sys.argv[1]
    name, fn = REELS[key]
    dur, html, ct = fn()
    if "--frame" in sys.argv:   # quick stills for review
        from playwright.sync_api import sync_playwright
        ts = [float(x) for x in sys.argv[sys.argv.index("--frame") + 1:]]
        p = Path("/tmp/claude-0/-home-claude/60837be5-8cde-507a-87a7-2bafa6fa6f6c/scratchpad/prev"); p.mkdir(exist_ok=True)
        (p / f"{key}.html").write_text(html)
        with sync_playwright() as pw:
            br = pw.chromium.launch(); pg = br.new_page(viewport={"width": W, "height": H})
            pg.goto((p / f"{key}.html").as_uri()); pg.wait_for_timeout(700)
            from PIL import Image
            ims = []
            for t in ts:
                pg.evaluate(f"seek({t})"); f = p / f"{key}-{t}.png"; pg.screenshot(path=str(f)); ims.append(Image.open(f).convert("RGB").resize((360, 640)))
            br.close()
        sh = Image.new("RGB", (370 * len(ims), 640), "white")
        for i, im in enumerate(ims): sh.paste(im, (i * 370, 0))
        sh.save(p / f"{key}-sheet.jpg", quality=85); print(p / f"{key}-sheet.jpg")
    else:
        OUT.mkdir(parents=True, exist_ok=True)
        print(render(name, html, dur, TRACK, OUT, ct))

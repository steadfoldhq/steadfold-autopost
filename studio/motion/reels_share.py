#!/usr/bin/env python3
"""Share-test Reels (Oct 16 audit): every queued Reel for Oct 16 19:00 to Oct 19 08:45, rebuilt to pass READABLE PACING.

The old cuts flashed 9-12 text beats in 13 s (every beat failed 0.4 s/word + 0.6 s). These keep the motion kit's look
(transitions on every cut, camera moves, objects in motion) but say less: one idea per beat, 2-7 words, held long enough
to read with the sound off. Frame 0 is the hook and doubles as the cover. The last beat is the hook's background with
no words, so the loop lands back on the hook.

    python3 studio/motion/reels_share.py ff-reel-1016-fee --out /tmp/share-out        # render + cover + QA sheet
    python3 studio/motion/reels_share.py --check                                         # pacing + overflow for all
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reels_1016am as AM  # noqa: E402
from kit import (BRANDS, FPS, Reel, arrow, asset, el, emoji, encode, img, loudness, make_readable, overflow_check,  # noqa: E402
                 probe, qa_times, reading_report, render_frames, ring, scribble_circle, sheet, words)

REPO = HERE.parent.parent
LIB = REPO / "media" / "music" / "library"
R = {}

EXTRA = """
.kick{display:inline-block;font:800 52px/1 Inter;letter-spacing:.12em;padding:20px 34px;border-radius:999px}
.bub{font:600 76px/1.22 Inter !important;max-width:900px !important;padding:44px 52px !important}
.big{font-size:150px}
.mid{font-size:128px}
.sm{font-size:100px}
.lbl{font:700 46px/1.15 Inter}
.ph{position:absolute;inset:-6%;background-size:cover;background-position:center;will-change:transform}
.gl{width:100%;height:30px;border-radius:15px;background:rgba(42,34,56,.12);margin:22px 0}
"""


def par(cls):
    return f'<div class="par {cls}"></div>'


def photo(name, tint="rgba(122,33,73,.38)", pos="center"):
    """Photo background with a brand tint (keeps a photo beat on-palette)."""
    return (f'<div class="par" style="background:url({asset(name)}) {pos}/cover"></div>'
            f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,{tint},rgba(44,42,58,.30) 50%,{tint})"></div>')


def kick(text, bg, ink, y=360, a="pop", t=0.0, r=0):
    return el(f'<span class="kick" style="background:{bg};color:{ink}">{text}</span>', "c", y, a=a, t=t, d=0.3, r=r)


def stamp(text, x, y, bg, ink="#fff", t=0.4, r=-8, size=60):
    return el(f'<div style="background:{bg};color:{ink};font:800 {size}px/1 Inter;padding:20px 38px;border-radius:999px">{text}</div>',
              x, y, a="stamp", t=t, d=0.28, r=r, loop="pulse")


def head(text, y, cls, size=150, t=0.0, gap=0.12, em="em", hook=False):
    """Hook lines are fully on screen at t=0 (a='none'); later lines arrive word by word."""
    if hook:
        html = text.replace("*", "")
        # rebuild emphasis without the kinetic spans
        out, on = [], False
        for tok in text.split(" "):
            if tok == "/":
                out.append("<br>")
                continue
            if tok.startswith("*"):
                on = True
            core = tok.replace("*", "")
            out.append(f'<span class="{em}">{core}</span>' if on else core)
            if tok.endswith("*") or tok.rstrip(".,?!:;").endswith("*"):
                on = False
        html = " ".join(out).replace(" <br> ", "<br>")
        return el(html, "c", y, a="none", cls=cls, style=f"font-size:{size}px")
    return words(text, "c", y, t=t, gap=gap, cls=cls, em_cls=em, style=f"font-size:{size}px")


def reel(rid, brand, music, stage, css):
    bpm = {"littlefold": 92, "fullyfunded": 95, "lockedhour": 100, "hourback": 108}[brand]
    r = Reel(rid, brand, bpm=bpm, css=css + EXTRA, stage=stage)
    r.music = music
    return r


def close(r, html, tin, **kw):
    """Last beat: the hook's background and object, no words, so the loop lands on the hook."""
    r.scene(1.5, html, tin=tin, **kw)
    return r


# =============================================================================================== Fully Funded
FF = BRANDS["fullyfunded"]
FFC = AM.FF_CSS + ".emw{color:#FFB08F}"
COB, LITE, DEEP = par("cob"), par("lite"), par("deep")


def ff_kick(text, dark=False, y=360, t=0.0):
    return kick(text, "#FF6A3D" if dark else "#2B3FE0", "#fff", y=y, t=t)


def ff_bars(a_lab, a_val, a_pct, b_lab, b_val, b_pct, t0=0.15):
    def one(lab, val, pct, col, t):
        return (f'<div class="lbl" style="color:#0E1440;margin-bottom:16px">{lab}</div>'
                f'<div class="bar" style="background:rgba(43,63,224,.12)"><div class="f" data-a="bar" data-t="{t}" data-d="0.9" data-to="{pct}" '
                f'style="background:{col};height:100%;border-radius:30px"></div></div>'
                f'<div class="H" style="font-size:130px;margin-top:14px"><span data-a="count" data-t="{t}" data-d="0.9" data-to="{val}" '
                f'data-comma="1">0</span></div>')
    return (el(one(a_lab, a_val, a_pct, "#2B3FE0", t0), 90, 470, 900, a="up", t=0.0)
            + el(one(b_lab, b_val, b_pct, "#FF6A3D", t0 + 0.25), 90, 930, 900, a="up", t=0.12))


def ff_fee():
    r = reel("ff-reel-1016-fee", "fullyfunded", "ff-c-confident-build-el.mp3", "#2B3FE0", FFC)
    pig = img("ht-piggy.png", 290, 1170, 500, t=-0.5, r=-6, loop="float")
    r.scene(2, COB + head("A 1% fee / looks *tiny.*", 470, "Hw", 190, em="emw", hook=True) + pig
            + emoji("🤏", 690, 1240, 170, t=0.3, d=0.35, loop="wobble"), cam="push", shake=(0.3, 0.2, 16))
    r.scene(2, LITE + head("200 a month. / 30 years. / *6%* a year.", 470, "H", 140, t=0.0)
            + emoji("📅", 420, 1170, 220, t=0.6, d=0.35, loop="float"), tin="whipL", cam="push")
    r.scene(2, LITE + ff_bars("No fee", 200903, 100, "1% fee", 166452, 82.9), tin="slam", cam="rise")
    r.scene(2, DEEP + head("The fee took", 470, "Hw", 120, t=0.0)
            + el('<span data-a="count" data-t="0.2" data-d="0.8" data-to="34451" data-comma="1">0</span>', "c", 660, a="none", cls="Hw",
                 style="font-size:250px;color:#FFB08F;letter-spacing:-.06em"),
            tin="zoom", focus=(540, 900), cam="push", shake=(1.0, 0.2, 14))
    r.scene(2, COB + head("Find yours: / *expense ratio.*", 520, "Hw", 140, em="emw")
            + emoji("🔍", 400, 1170, 260, t=0.4, d=0.35, loop="float"), tin="whipR", cam="tilt")
    r.scene(2, DEEP + kick("THE CATCH", "#FF6A3D", "#fff", y=400, a="stamp", r=-4)
            + head("Cheaper isn't / always *better.*", 560, "Hw", 140, t=0.2, em="emw"), tin="stripes", color="#FF6A3D",
            color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, LITE + head("Send to a / *new investor.*", 520, "H", 150)
            + img("ht-piggy.png", 330, 1170, 420, t=0.3, r=6), tin="push", cam="push")
    return close(r, COB + pig, "zoom", focus=(540, 800))


R["ff-reel-1016-fee"] = ff_fee


# =============================================================================================== Hourback
HB = BRANDS["hourback"]
HBC = AM.HB_CSS
INDI, CREAM, PEACH, PLUM = par("indi"), par("cream"), par("peach"), par("plum")


def bub(text, kind="me", who=None, x=None, y=600, t=0.0, w=860):
    side = 120 if kind == "me" else 90
    who_html = f'<div class="who">{who}</div>' if who else ""
    return el(f'<div class="bub {kind}">{who_html}{text}</div>', x if x is not None else side, y, w, a="pop", t=t, d=0.35)


def mail_card(y=560, t=0.0, lines=9):
    gl = "".join('<div class="gl" style="width:%d%%"></div>' % (60 + (k * 37) % 40) for k in range(lines))
    return el(f'<div style="background:#fff;border-radius:40px;padding:50px 56px;box-shadow:0 30px 70px rgba(0,0,0,.25);width:860px">'
              f'<div class="lbl" style="color:#5E54C9">✉︎ Inbox</div>{gl}</div>', 110, y, a="fly", t=t, d=0.5, r=-3, loop="float")


def hb_email_asks():
    r = reel("hb-reel-1016-email-asks", "hourback", "hb-c-clever-celesta-el.mp3", "#FFF8EF", HBC)
    hand = img("ht-point.png", 120, 1150, 560, t=-0.5, r=-10, loop="float")
    r.scene(2, CREAM + head("Long email. / What do they *want?*", 430, "H", 150, hook=True) + hand
            + emoji("📧", 720, 1170, 190, t=0.25, d=0.35, loop="buzz"), cam="push", shake=(0.25, 0.2, 14))
    r.scene(2, INDI + head("Read it *twice.* / Still lost.", 360, "Hw", 130, em="emo2") + mail_card(860, 0.2),
            tin="whipL", cam="rise")
    r.scene(2, PEACH + kick("ASK AI", "#5E54C9", "#fff", y=380)
            + bub("The asks, and by when?", "me", y=620, t=0.2), tin="slam", cam="push")
    r.scene(2, CREAM + kick("AI REPLY", "#FFC94D", "#2A2238", y=380)
            + bub("Deck → Thu<br>Room → Fri", "ai", y=600, t=0.15, w=700), tin="pixel", cam="rise")
    r.scene(2, INDI + head("Check each *quote.* / Then reply.", 560, "Hw", 140, em="emo2")
            + emoji("✅", 430, 1170, 220, t=0.5, d=0.3, loop="pulse"), tin="glitch", td=0.2, cam="push")
    r.scene(2, CREAM + head("Save for your / next *long email.*", 520, "H", 140)
            + img("ht-point.png", 260, 1170, 520, t=0.3, r=-6), tin="zoom", focus=(540, 800), cam="push")
    return close(r, CREAM + hand, "whipU")


R["hb-reel-1016-email-asks"] = hb_email_asks


# =============================================================================================== Littlefold
LF = BRANDS["littlefold"]
LFC = AM.LF_CSS + """
.S{font-family:Lora;font-weight:600;color:#FFF8E4;line-height:1.02;letter-spacing:-.02em;text-shadow:0 6px 30px rgba(44,42,58,.45)}
.S .em{font-style:italic;color:#FFD6E3}
"""
BLOB, BLOB2, PINK = par("blobs"), par("blobs2"), par("pinkbg")
BERRY = '<div class="par" style="background:radial-gradient(circle, rgba(255,255,255,.08) 2px, transparent 2.6px) 0 0/34px 34px,#7A2149"></div>'


def lf_doing_better():
    r = reel("lf-reel-1016-doing-better", "littlefold", "lf-b-tender-el.mp3", "#FFF4E0", LFC)
    warm = "rgba(255,138,112,.30)"
    r.scene(2, photo("lf-sil-walk.jpg", warm) + head("You're doing / *better* than / you think.", 420, "S", 165, hook=True)
            + emoji("✨", 780, 360, 110, t=0.2, d=0.4, loop="pulse", amp=2), cam="push")
    r.scene(2, photo("lf-sil-lift.jpg", warm) + head("You *fed* them.", 560, "S", 180), tin="flash", color=LF["peach"],
            color2=LF["butter"], cam="push")
    r.scene(2, photo("lf-shoulders.jpg", warm) + head("You *held* them.", 560, "S", 180), tin="zoom", focus=(540, 700), cam="pull")
    r.scene(2, photo("lf-sil-walk.jpg", warm, "30% center") + head("You came *back.*", 560, "S", 180), tin="push", cam="left")
    r.scene(2, BERRY + head("Again and / *again.*", 600, "S", 190), tin="slit", color=LF["pink"], cam="push", shake=(0.5, 0.2, 10))
    r.scene(2, BLOB + head("That's the / *whole job.*", 560, "H", 160) + emoji("💗", 420, 1170, 240, t=0.5, d=0.4, loop="pulse", amp=2),
            tin="blob", focus=(540, 800), color=LF["butter"], cam="push")
    r.scene(2, BLOB2 + head("Send to a / *tired parent.*", 540, "H", 150) + emoji("💌", 420, 1170, 220, t=0.4, d=0.4, loop="float"),
            tin="stripes", color=LF["pink"], color2=LF["butter"], color3=LF["peach"], cam="rise")
    return close(r, photo("lf-sil-walk.jpg", warm), "flash", color=LF["peach"], color2=LF["butter"])


R["lf-reel-1016-doing-better"] = lf_doing_better


# =============================================================================================== Locked Hour
LH = BRANDS["lockedhour"]
LHC = AM.LH_CSS
DOTS, DOTSC, DOTSP = par("dots"), par("dotsc"), par("dotsp")


def lh_quiet():
    r = reel("lh-reel-1016-quiet", "lockedhour", "lh-a-focus-pulse-el.mp3", "#FFE27A", LHC)
    pings = "".join(emoji("🔔", x, y, 130, t=tt, d=0.25, loop="buzz", r=rr) for x, y, tt, rr in
                    [(150, 1050, -0.4, -12), (760, 1000, -0.2, 10), (440, 1260, 0.15, -4)])
    r.scene(2, DOTS + head("One *quiet* hour. / Two moves.", 470, "H", 160, hook=True) + pings, cam="push", shake=(0.15, 0.25, 18))
    r.scene(2, DOTSC + kick("1 · SEND THIS", "#141414", "#FFE27A", y=380)
            + el('<div class="paper"><div class="hand">Heads down<br>till 11.</div></div>', 140, 560, 800, a="fly", t=0.1, d=0.45, r=-2)
            + stamp("SENT", 640, 1080, "#FF5CA8", "#141414", t=0.9), tin="stripes", color=LH["acc"], color2="#FFD43B",
            color3="#FFF4E0", cam="rise")
    r.scene(2, DOTSP + kick("2", "#141414", "#FFE27A", y=380) + head("Do Not / *Disturb.*", 560, "H", 190, em="emy")
            + emoji("🌙", 420, 1170, 240, t=0.4, d=0.35, loop="float"), tin="slam", cam="push")
    r.scene(2, DOTS + kick("3 · START", "#141414", "#FFE27A", y=380)
            + el('<span data-a="tick" data-mmss="1" data-from="3600" data-to="3594" data-t="0.1" data-d="2.0">60:00</span>', "c", 640,
                 a="none", cls="timer") + img("ht-hourglass.png", 400, 1170, 280, t=0.2, r=6, loop="float"),
            tin="whipU", cam="push")
    r.scene(2, DOTSC + head("The pings / will *wait.*", 560, "H", 170), tin="cut", cam="push", shake=(0.0, 0.2, 16))
    r.scene(2, DOTS + head("Send to someone / who answers / *every ping.*", 480, "H", 130)
            + img("ht-clock.png", 380, 1170, 320, t=0.4, r=-6), tin="iris", focus=(540, 900), color=LH["acc"], cam="push")
    return close(r, DOTS + pings, "zoom", focus=(540, 900))


R["lh-reel-1016-quiet"] = lh_quiet


# =============================================================================================== Oct 17 (08:00 and 19:00)
STRIKE = ".strike{position:relative;display:inline-block}.sk{position:absolute;left:-2%;top:50%;height:.14em;width:0;border-radius:.07em;background:#FF5CA8}"


def strike(old, t0=0.3, color=None):
    c = f' style="background:{color}"' if color else ""
    return f'<span class="strike">{old}<span class="sk"{c} data-a="strike" data-t="{t0}" data-d="0.35"></span></span>'


def sticky_lf(title, items, y=520, t0=0.25):
    lis = "".join(el(f'<div class="it"><span class="tk">✓</span>{x}</div>', 0, 0, a="left", t=t0 + k * 0.4, d=0.3,
                     style="position:relative;margin-bottom:14px") for k, x in enumerate(items))
    return el(f'<div class="sticky"><div class="tape"></div><div class="note" style="position:absolute;left:120px;top:44px;font-size:84px">'
              f'{title}</div>{lis}</div>', 80, y, 920, a="drop", t=0.0, d=0.55, r=-2)


def lf_read():
    r = reel("lf-reel-1017am-read", "littlefold", "lf-a-cosy-el.mp3", "#FFF4E0", LFC)
    book = emoji("📖", 360, 1170, 330, t=-0.5, d=0.45, loop="float")
    r.scene(2, BLOB + head("Too little / for *books?*", 470, "H", 170, hook=True) + book
            + stamp("READ ANYWAY", 520, 1300, LF["acc"], t=0.35, size=52), cam="push", shake=(0.35, 0.2, 12))
    r.scene(2, BLOB2 + head("They won't / follow the *story.*", 560, "H", 150), tin="blob", focus=(540, 800), color=LF["pink"], cam="push")
    r.scene(2, PINK + head("Your *voice* / is the start.", 560, "H", 160) + emoji("💗", 420, 1170, 240, t=0.4, d=0.4, loop="pulse", amp=2),
            tin="flash", color=LF["peach"], color2=LF["butter"], cam="pull")
    r.scene(2, BLOB + sticky_lf("Tonight:", ["One board book", "Same time daily", "Point, name, pause"]), tin="iris",
            focus=(540, 800), color=LF["butter"], cam="rise")
    r.scene(2, BLOB2 + kick("AAP", LF["acc"], "#fff", y=400) + head("Read aloud from / *infancy.*", 560, "H", 150),
            tin="push", cam="push")
    r.scene(2, PINK + head("Send to a / *new parent.*", 560, "H", 160) + emoji("💌", 420, 1170, 220, t=0.4, d=0.4, loop="float"),
            tin="stripes", color=LF["pink"], color2=LF["butter"], color3=LF["peach"], cam="rise")
    return close(r, BLOB + book, "blob", focus=(540, 900), color=LF["pink"])


def ff_match():
    r = reel("ff-reel-1017am-match", "fullyfunded", "ff-d-question-marimba-el.mp3", "#2B3FE0", FFC)
    face = emoji("🫣", 380, 1170, 320, t=-0.5, d=0.4, loop="wobble")
    r.scene(2, COB + head("Never checked / your *match?*", 470, "Hw", 160, em="emw", hook=True) + face, cam="push", shake=(0.2, 0.2, 14))
    r.scene(2, LITE + head("Pay 50,000. / They add *half,* / up to 6%.", 470, "H", 130, t=0.0),
            tin="whipL", cam="push")
    r.scene(2, LITE + ff_bars("You put in 3%", 750, 50, "You put in 6%", 1500, 100), tin="slam", cam="rise")
    r.scene(2, COB + head("Search your plan: / *“match”*", 540, "Hw", 140, em="emw") + emoji("🔍", 400, 1170, 260, t=0.4, d=0.35, loop="float"),
            tin="whipR", cam="tilt")
    r.scene(2, DEEP + kick("THE CATCH", "#FF6A3D", "#fff", y=400, a="stamp", r=-4) + head("It may need / *time to vest.*", 560, "Hw", 140, t=0.2,
            em="emw"), tin="stripes", color="#FF6A3D", color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, LITE + head("Send to a / *new hire.*", 540, "H", 170) + img("ht-piggy.png", 330, 1170, 420, t=0.3, r=6), tin="push", cam="push")
    return close(r, COB + face, "zoom", focus=(540, 900))


def lh_next_step():
    r = reel("lh-reel-1017am-next-step", "lockedhour", "lh-b-ticking-marimba-el.mp3", "#FFE27A", LHC + STRIKE)
    note = el('<div class="paper" style="padding:40px 50px"><div class="hand" style="font-size:110px">☐ Do taxes</div></div>', 230, 980, 620,
              a="fly", t=-0.5, d=0.45, r=-4, loop="float")
    r.scene(2, DOTS + head("“Do taxes” / isn't a *task.*", 450, "H", 170, hook=True) + note + stamp("3 WEEKS", 640, 1330, "#FF5CA8", "#141414",
            t=0.35, size=52), cam="push", shake=(0.35, 0.2, 14))
    r.scene(2, DOTSP + head("It's a / *project.*", 600, "H", 200, em="emy"), tin="cut", cam="push", shake=(0.0, 0.2, 20))
    r.scene(2, DOTSC + head("Ask: what would I / *physically* do first?", 520, "H", 120), tin="stripes", color=LH["acc"], color2="#FFD43B",
            color3="#FFF4E0", cam="rise")
    rw = lambda old, new: (f'<div class="paper"><div class="H" style="font-size:96px">{strike(old, 0.3)}</div>'
                           f'<div class="hand" style="margin-top:30px" data-a="type" data-t="0.7" data-d="0.6">{new}</div></div>')
    r.scene(2, DOTS + el(rw("Do taxes", "Find last year's form"), 110, 600, 860, a="fly", t=0.0, d=0.45, r=-2), tin="slam", cam="push")
    r.scene(2, DOTSC + el(rw("Plan the trip", "Text Sam 2 dates"), 110, 600, 860, a="fly", t=0.0, d=0.45, r=2), tin="whipL", cam="push")
    r.scene(2, DOTS + head("Rewrite *one* / task now.", 560, "H", 170) + img("ht-clock.png", 380, 1170, 320, t=0.4, r=-6),
            tin="iris", focus=(540, 900), color=LH["acc"], cam="push")
    return close(r, DOTS + note, "zoom", focus=(540, 900))


def hb_swap():
    r = reel("hb-reel-1017am-swap", "hourback", "hb-a-ta-da-el.mp3", "#FFE6D3", HBC + STRIKE.replace("#FF5CA8", "#FF8A3D"))
    eggs = emoji("🥚", 300, 1170, 300, t=-0.5, d=0.4, loop="wobble") + emoji("❌", 560, 1170, 220, t=0.25, d=0.3, loop="pulse")
    r.scene(2, PEACH + head("Halfway in. / *No eggs.*", 470, "H", 170, hook=True) + eggs, cam="push", shake=(0.25, 0.2, 14))
    r.scene(2, INDI + head("Don't run / to the *shop.*", 560, "Hw", 170, em="emo2") + emoji("🏃", 420, 1170, 240, t=0.3, d=0.3, loop="buzz"),
            tin="whipL", cam="push")
    r.scene(2, CREAM + kick("ASK AI", "#5E54C9", "#fff", y=400) + bub("Out of eggs. 2 swaps?", "me", y=620, t=0.2), tin="slam", cam="rise")
    r.scene(2, PEACH + kick("AI REPLY", "#FFC94D", "#2A2238", y=400) + bub("🍌 Banana · ¼ cup<br>🥣 Yogurt · ¼ cup", "ai", y=600, t=0.15, w=760),
            tin="pixel", cam="push")
    r.scene(2, INDI + head("Allergies? / *Say so.*", 600, "Hw", 180, em="emo2"), tin="glitch", td=0.2, cam="push")
    r.scene(2, CREAM + head("Save for your next / *half-made recipe.*", 520, "H", 120) + emoji("🥞", 400, 1170, 280, t=0.4, d=0.35, loop="float"),
            tin="zoom", focus=(540, 800), cam="push")
    return close(r, PEACH + eggs, "whipU")


def ff_raise_half():
    r = reel("ff-reel-1017-raise-half", "fullyfunded", "ff-b-bright-pop-el.mp3", "#16206B", FFC)
    street = photo("ff-street.jpg", "rgba(22,32,107,.55)")
    r.scene(2, street + head("Got a raise? / Save *half.*", 500, "Hw", 180, em="emw", hook=True)
            + emoji("🎉", 420, 1170, 240, t=-0.4, d=0.35, loop="wobble"), cam="push")
    r.scene(2, LITE + head("Raise: / 200 more / a *month.*", 470, "H", 170, t=0.0), tin="whipL", cam="push")
    split = ('<div style="display:flex;gap:40px;justify-content:center">'
             '<div class="card" style="text-align:center;width:400px"><div class="H" style="font-size:150px">100</div><div class="lbl">saved</div></div>'
             '<div class="card" style="text-align:center;width:400px;background:#FF6A3D"><div class="Hw" style="font-size:150px">100</div>'
             '<div class="lbl" style="color:#fff">enjoyed</div></div></div>')
    r.scene(2, DEEP + head("Save 100 at 6%, 20 years:", 470, "Hw", 90)
            + el('<span data-a="count" data-t="0.2" data-d="0.9" data-to="46204" data-comma="1">0</span>', "c", 660, a="none", cls="Hw",
                 style="font-size:250px;color:#FFB08F;letter-spacing:-.06em")
            + head("from 24,000 in", 980, "Hw", 90, t=0.6), tin="zoom", focus=(540, 900), cam="push", shake=(1.1, 0.2, 12))
    r.scene(2, COB + head("Set it up / the day it *lands.*", 560, "Hw", 140, em="emw") + emoji("📆", 420, 1170, 240, t=0.4, d=0.35, loop="float"),
            tin="whipR", cam="tilt")
    r.scene(2, DEEP + kick("THE CATCH", "#FF6A3D", "#fff", y=400, a="stamp", r=-4) + head("Pick an amount / you'll *keep.*", 560, "Hw", 140,
            t=0.2, em="emw"), tin="stripes", color="#FF6A3D", color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, LITE + head("Save for your / *next raise.*", 540, "H", 160) + img("ht-piggy.png", 330, 1170, 420, t=0.3, r=6), tin="push", cam="push")
    return close(r, street, "zoom", focus=(540, 900))


def hb_offline():
    r = reel("hb-reel-1017-offline", "hourback", "hb-b-sunny-strum-el.mp3", "#3A2240", HBC)
    sky = photo("hb-clouds.jpg", "rgba(58,34,64,.45)")
    r.scene(2, sky + head("Off work. / Brain *still on?*", 480, "Hw", 170, em="emo2", hook=True)
            + emoji("🧠", 400, 1170, 280, t=-0.4, d=0.35, loop="buzz"), cam="push")
    tasks = "".join(bub(x, "them", x=[110, 360, 160, 420][k], y=620 + k * 190, t=0.2 + k * 0.25, w=520) for k, x in
                    enumerate(["Report", "Reply Jo", "Gym", "Dentist?"]))
    r.scene(2, INDI + head("Dump it *all.*", 380, "Hw", 150, em="emo2") + tasks, tin="whipL", cam="rise")
    r.scene(2, PEACH + kick("ASK AI", "#5E54C9", "#fff", y=400) + bub("Pick my 3 must-dos.", "me", y=620, t=0.2), tin="slam", cam="push")
    r.scene(2, CREAM + kick("AI REPLY", "#FFC94D", "#2A2238", y=400) + bub("9:00 Report<br>12:30 Reply Jo<br>17:30 Gym", "ai", y=600, t=0.15, w=760),
            tin="pixel", cam="rise")
    r.scene(2, PLUM + head("Then *log off.*", 560, "Hw", 190, em="emo2") + stamp("CLOSED", 560, 1000, "#FFC94D", "#2A2238", t=0.7),
            tin="glitch", td=0.2, cam="push")
    r.scene(2, CREAM + head("Save for / *tonight.*", 560, "H", 190) + img("ht-cup.png", 400, 1170, 280, t=0.3, r=-6),
            tin="zoom", focus=(540, 800), cam="push")
    return close(r, sky, "whipU")


def lf_one_job():
    r = reel("lf-reel-1017-one-job", "littlefold", "lf-c-sunny-morning-el.mp3", "#FFF4E0", LFC)
    hands = emoji("🤲", 380, 1170, 320, t=-0.5, d=0.4, loop="float")
    r.scene(2, BLOB + head("Someone offers help? / Give *one job.*", 450, "H", 140, hook=True) + hands, cam="push")
    card = lambda n, txt: el(f'<div class="card"><span class="num">{n}</span><div class="H" style="font-size:110px;margin-top:40px">{txt}</div></div>',
                             90, 560, 900, a="fly", t=0.0, d=0.5, r=-3 if n % 2 else 3)
    r.scene(2, BLOB2 + card(1, "Dinner on <span class='em'>Tuesday.</span>"), tin="slam", cam="rise")
    r.scene(2, PINK + card(2, "Fold <span class='em'>one load.</span>"), tin="whipL", cam="rise")
    r.scene(2, BLOB + card(3, "Hold baby while <span class='em'>I shower.</span>"), tin="blob", focus=(540, 900), color=LF["butter"], cam="rise")
    r.scene(2, BLOB2 + head("Then let them / do it *their way.*", 560, "H", 140), tin="flash", color=LF["peach"], color2=LF["butter"], cam="push")
    r.scene(2, PINK + head("Send to the friend / who keeps *asking.*", 540, "H", 130) + emoji("💌", 420, 1170, 220, t=0.4, d=0.4, loop="float"),
            tin="stripes", color=LF["pink"], color2=LF["butter"], color3=LF["peach"], cam="rise")
    return close(r, BLOB + hands, "blob", focus=(540, 900), color=LF["pink"])


def tabs(n, y=1120, t0=-0.4, close_after=None):
    out = []
    for k in range(n):
        x, row = 80 + (k % 6) * 150, k // 6
        style = "width:136px;height:70px;border-radius:16px 16px 0 0;background:#fff;border:5px solid #141414"
        a = "pop"
        out.append(el(f'<div style="{style}"></div>', x, y + row * 90, a=a, t=t0 + k * 0.03, d=0.25, loop="buzz" if k % 3 == 0 else None))
    return "".join(out)


def lh_one_tab():
    r = reel("lh-reel-1017-one-tab", "lockedhour", "lh-c-morning-drive-el.mp3", "#FFE27A", LHC)
    many = tabs(18)
    r.scene(2, DOTS + head("How many tabs / are *open?*", 470, "H", 160, hook=True) + many, cam="push", shake=(0.1, 0.25, 14))
    r.scene(2, DOTSP + head("Close every tab / but *one.*", 500, "H", 150, em="emy") + tabs(1, 1120, 0.5), tin="cut", cam="push",
            shake=(0.0, 0.2, 20))
    r.scene(2, DOTSC + head("New one opened? / *Close it.*", 540, "H", 140) + emoji("🙅", 420, 1170, 240, t=0.4, d=0.3, loop="wobble"),
            tin="stripes", color=LH["acc"], color2="#FFD43B", color3="#FFF4E0", cam="rise")
    r.scene(2, DOTS + head("Need it later? / Jot it *down.*", 470, "H", 140)
            + el('<div class="paper" style="padding:40px 50px"><div class="hand" style="font-size:100px">later: ☐ ☐</div></div>', 240, 960, 600,
                 a="fly", t=0.4, d=0.45, r=-3), tin="slam", cam="push")
    r.scene(2, DOTSC + head("One tab. / One task. / *One hour.*", 460, "H", 150) + img("ht-clock.png", 380, 1170, 320, t=0.6, r=-6),
            tin="whipU", cam="push")
    r.scene(2, DOTS + head("Try it in your / *next hour.*", 560, "H", 150), tin="iris", focus=(540, 900), color=LH["acc"], cam="push")
    return close(r, DOTS + many, "zoom", focus=(540, 900))


for _f in (lf_read, ff_match, lh_next_step, hb_swap, ff_raise_half, hb_offline, lf_one_job, lh_one_tab):
    R[_f().rid] = _f


# =============================================================================================== Oct 18 (08:00 and 19:00) and Oct 19 (08:00)
def windows(y=1080, t0=-0.5, lit=(1, 4, 6, 11, 13, 18)):
    cells = "".join(f'<div style="width:150px;height:110px;border-radius:12px;background:{"#FFE27E" if k in lit else "rgba(255,214,227,.18)"};'
                    f'{"box-shadow:0 0 40px rgba(255,226,126,.7)" if k in lit else ""}"></div>' for k in range(20))
    return el(f'<div style="display:grid;grid-template-columns:repeat(5,150px);gap:26px;justify-content:center">{cells}</div>', "c", y,
              a="up", t=t0, d=0.6)


def lf_3am():
    r = reel("lf-reel-1018am-3am-windows", "littlefold", "lf-hero-3am-el.mp3", "#7A2149", LFC)
    night = BERRY + windows() + emoji("🌙", 800, 300, 140, t=-0.4, d=0.4, loop="float")
    r.scene(2, night + head("3:07 am. / *Up again?*", 470, "S", 180, hook=True), cam="push")
    r.scene(2, BERRY + windows(860, 0.0) + head("See the lit / *windows?*", 420, "S", 150), tin="flash", color=LF["butter"], color2=LF["pink"],
            cam="pull")
    r.scene(2, PINK + head("Some are parents, / up *like you.*", 560, "H", 140) + emoji("💗", 420, 1170, 240, t=0.4, d=0.4, loop="pulse", amp=2),
            tin="blob", focus=(540, 900), color=LF["pink"], cam="push")
    r.scene(2, BLOB + kick("NHS TIP", LF["acc"], "#fff", y=400) + head("Make night / feel like *night.*", 560, "H", 150), tin="iris",
            focus=(540, 800), color=LF["butter"], cam="push")
    r.scene(2, BLOB2 + sticky_lf("At night:", ["Lights low", "Voice soft", "Feed, then down"]), tin="push", cam="rise")
    r.scene(2, PINK + head("Send to someone / up at *3 am.*", 560, "H", 140) + emoji("💌", 420, 1170, 220, t=0.4, d=0.4, loop="float"),
            tin="stripes", color=LF["pink"], color2=LF["butter"], color3=LF["peach"], cam="rise")
    return close(r, night, "flash", color=LF["butter"], color2=LF["pink"])


def ff_lower_rate():
    r = reel("ff-reel-1018am-lower-rate", "fullyfunded", "ff-c-confident-build-el.mp3", "#2B3FE0", FFC)
    phone = emoji("☎️", 380, 1170, 300, t=-0.5, d=0.4, loop="buzz")
    r.scene(2, COB + head("Ask for a / *lower rate.*", 480, "Hw", 180, em="emw", hook=True) + phone, cam="push", shake=(0.1, 0.25, 16))
    r.scene(2, LITE + head("5,000 on a card / at *20%* a year.", 500, "H", 130, t=0.0), tin="whipL", cam="push")
    r.scene(2, LITE + ff_bars("Interest at 20%", 1097, 100, "Interest at 16%", 861, 78.5), tin="slam", cam="rise")
    r.scene(2, COB + el('<div class="card"><div class="H" style="font-size:100px">“Can you lower my rate?”</div></div>',
                        90, 560, 900, a="fly", t=0.0, d=0.5, r=-2), tin="whipR", cam="push")
    r.scene(2, DEEP + kick("THE CATCH", "#FF6A3D", "#fff", y=400, a="stamp", r=-4) + head("Paying it down / helps *more.*", 560, "Hw", 140, t=0.2,
            em="emw"), tin="stripes", color="#FF6A3D", color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, LITE + head("Save for your / next *5 minutes.*", 540, "H", 150) + img("ht-cup.png", 400, 1170, 280, t=0.3, r=6),
            tin="push", cam="push")
    return close(r, COB + phone, "zoom", focus=(540, 900))


def lh_pick_3():
    r = reel("lh-reel-1018am-pick-3", "lockedhour", "lh-a-focus-pulse-el.mp3", "#FFE27A", LHC)
    clock = img("ht-clock.png", 360, 1100, 360, t=-0.5, r=-6, loop="wobble")
    r.scene(2, DOTS + head("Sunday. / *10 minutes.*", 500, "H", 190, hook=True) + clock, cam="push", shake=(0.2, 0.2, 14))
    r.scene(2, DOTSC + head("Pick *3 things* / for the week.", 560, "H", 150), tin="stripes", color=LH["acc"], color2="#FFD43B",
            color3="#FFF4E0", cam="rise")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    blocks = {0: ("#FF5CA8", "Gym"), 2: ("#FFD43B", "Report"), 4: ("#FF5CA8", "Course")}
    cols = "".join(f'<div style="flex:1;border-left:4px solid #141414;min-height:520px;position:relative">'
                   f'<div style="font:800 34px/1 Inter;padding:14px 8px">{d}</div>'
                   + (f'<div data-a="pop" data-t="{0.3 + k * 0.25:.2f}" data-d="0.3" style="position:absolute;left:8px;right:8px;top:120px;height:200px;'
                      f'background:{blocks[k][0]};border:5px solid #141414;border-radius:14px;font:900 40px/1.1 Inter;padding:14px">{blocks[k][1]}</div>'
                      if k in blocks else "") + '</div>' for k, d in enumerate(days))
    r.scene(2, DOTS + head("Block *them.*", 400, "H", 150)
            + el(f'<div class="box" style="display:flex;padding:0;overflow:hidden;width:900px">{cols}</div>', 90, 660, 900, a="up", t=0.1),
            tin="slam", cam="push")
    r.scene(2, DOTSP + head("Treat it like / a *meeting.*", 580, "H", 170, em="emy"), tin="cut", cam="push", shake=(0.0, 0.2, 18))
    r.scene(2, DOTSC + head("Move it: fine. / Delete it: *no.*", 560, "H", 150), tin="whipL", cam="push")
    r.scene(2, DOTS + head("Save for / *Sunday.*", 560, "H", 190) + img("ht-hourglass.png", 420, 1170, 240, t=0.4, r=6), tin="iris",
            focus=(540, 900), color=LH["acc"], cam="push")
    return close(r, DOTS + clock, "zoom", focus=(540, 900))


def hb_freeze():
    r = reel("hb-reel-1018am-freeze-frame", "hourback", "hb-hero-sitcom-el.mp3", "#FFF8EF", HBC)
    pile = "".join(bub(x, "them", x=[100, 380, 140, 420][k], y=1000 + k * 120, t=-0.6 + k * 0.12, w=520) for k, x in
                   enumerate(['<div class="gl" style="width:300px;margin:6px 0"></div>', "👍", '<div class="gl" style="width:380px;margin:6px 0"></div>', "😅"]))
    r.scene(2, CREAM + head("*147* unread / in the family chat.", 430, "H", 140, hook=True) + pile, cam="push", shake=(0.3, 0.2, 12))
    r.scene(2, PLUM + head("Copy it. / Take out *names.*", 560, "Hw", 160, em="emo2") + emoji("✂️", 420, 1170, 220, t=0.4, d=0.3, loop="wobble"),
            tin="glitch", td=0.2, cam="push")
    r.scene(2, PEACH + kick("ASK AI", "#5E54C9", "#fff", y=400) + bub("What do I do, by when?", "me", y=620, t=0.2), tin="slam", cam="rise")
    r.scene(2, CREAM + kick("AI REPLY", "#FFC94D", "#2A2238", y=400) + bub("Dessert · Sat<br>RSVP · Thu", "ai", y=600, t=0.15, w=760),
            tin="pixel", cam="push")
    r.scene(2, INDI + head("Check each line / against the *chat.*", 560, "Hw", 140, em="emo2"), tin="whipL", cam="push")
    r.scene(2, CREAM + head("Send to the one / in *every group chat.*", 520, "H", 130) + img("ht-point.png", 260, 1170, 520, t=0.3, r=-6),
            tin="zoom", focus=(540, 800), cam="push")
    return close(r, CREAM + pile, "whipU")


def hb_school():
    r = reel("hb-reel-1018-school-email", "hourback", "hb-c-clever-celesta-el.mp3", "#5E54C9", HBC)
    env = emoji("📩", 380, 1100, 320, t=-0.5, d=0.4, loop="buzz")
    r.scene(2, INDI + head("School newsletter. / *Again.*", 480, "Hw", 160, em="emo2", hook=True) + env, cam="push", shake=(0.2, 0.2, 14))
    r.scene(2, CREAM + head("Dates buried / in *paragraph 6.*", 360, "H", 130) + mail_card(800, 0.2), tin="whipL", cam="rise")
    r.scene(2, PEACH + kick("ASK AI", "#5E54C9", "#fff", y=400) + bub("List every date, earliest first.", "me", y=620, t=0.2), tin="slam", cam="push")
    r.scene(2, CREAM + kick("AI REPLY", "#FFC94D", "#2A2238", y=400) + bub("Thu · picture day<br>Fri · forms due", "ai", y=600, t=0.15, w=800),
            tin="pixel", cam="rise")
    r.scene(2, INDI + head("Check each line. / Add to *calendar.*", 560, "Hw", 140, em="emo2") + emoji("📅", 420, 1170, 220, t=0.4, d=0.3,
            loop="float"), tin="glitch", td=0.2, cam="push")
    r.scene(2, CREAM + head("Send to the other / *pick-up grown-up.*", 520, "H", 130) + img("ht-point.png", 260, 1170, 520, t=0.3, r=-6),
            tin="zoom", focus=(540, 800), cam="push")
    return close(r, INDI + env, "whipU")


def lf_breathe():
    r = reel("lf-reel-1018-breathe", "littlefold", "lf-b-tender-el.mp3", "#FFD6E3", LFC)
    wind = emoji("🌬️", 380, 1100, 320, t=-0.5, d=0.45, loop="float")
    r.scene(2, PINK + head("Crying won't stop? / *Step away.*", 470, "H", 150, hook=True) + wind, cam="push")
    card = lambda n, txt: el(f'<div class="card"><span class="num">{n}</span><div class="H" style="font-size:120px;margin-top:40px">{txt}</div></div>',
                             90, 560, 900, a="fly", t=0.0, d=0.5, r=-3 if n % 2 else 3)
    r.scene(2, BLOB + card(1, "On their back, <span class='em'>in the crib.</span>"), tin="blob", focus=(540, 900), color=LF["butter"], cam="rise")
    r.scene(2, BLOB2 + card(2, "Step out. <span class='em'>Breathe.</span>"), tin="slam", cam="rise")
    r.scene(2, PINK + card(3, "Go back when <span class='em'>calmer.</span>"), tin="push", cam="rise")
    r.scene(2, BERRY + head("Never shake / a *baby.*", 600, "S", 180), tin="slit", color=LF["pink"], cam="push")
    r.scene(2, BLOB + head("Call someone / to take a *turn.*", 560, "H", 150) + emoji("📞", 420, 1170, 220, t=0.4, d=0.35, loop="buzz"),
            tin="flash", color=LF["peach"], color2=LF["butter"], cam="push")
    r.scene(2, BLOB2 + head("Send to a / *new parent.*", 560, "H", 160) + emoji("💌", 420, 1170, 220, t=0.4, d=0.4, loop="float"),
            tin="stripes", color=LF["pink"], color2=LF["butter"], color3=LF["peach"], cam="rise")
    return close(r, PINK + wind, "blob", focus=(540, 900), color=LF["pink"])


def lh_mute():
    r = reel("lh-reel-1018-mute-the-world", "lockedhour", "lh-hero-quiet-power-el.mp3", "#FFE27A", LHC)
    pings = "".join(emoji(e, x, y, 140, t=tt, d=0.25, loop="buzz", r=rr) for e, x, y, tt, rr in
                    [("🔔", 150, 1080, -0.4, -12), ("📱", 760, 1040, -0.2, 10), ("✉️", 440, 1280, 0.15, -4)])
    r.scene(2, DOTS + head("Busy all day. / *Nothing finished.*", 440, "H", 150, hook=True) + pings, cam="push", shake=(0.15, 0.25, 18))
    r.scene(2, DOTSP + head("Lock *one hour.*", 620, "H", 190, em="emy"), tin="cut", cam="push", shake=(0.0, 0.2, 20))
    r.scene(2, DOTSC + kick("1", "#141414", "#FFE27A", y=400) + head("Phone: / *another room.*", 560, "H", 160) + emoji("📱", 420, 1170, 220, t=0.4,
            d=0.3, loop="float"), tin="stripes", color=LH["acc"], color2="#FFD43B", color3="#FFF4E0", cam="rise")
    r.scene(2, DOTS + kick("2", "#141414", "#FFE27A", y=400) + head("One task. / *Not three.*", 560, "H", 170), tin="slam", cam="push")
    r.scene(2, DOTSC + kick("3", "#141414", "#FFE27A", y=400) + head("Door closed. / *Pings off.*", 560, "H", 170) + emoji("🚪", 420, 1170, 220,
            t=0.4, d=0.3, loop="float"), tin="whipL", cam="push")
    r.scene(2, DOTSP + head("Mind wanders? / *Bring it back.*", 560, "H", 150, em="emy"), tin="iris", focus=(540, 900), color="#FFD43B", cam="push")
    r.scene(2, DOTS + head("The world can / wait an *hour.*", 560, "H", 150) + img("ht-hourglass.png", 420, 1170, 240, t=0.4, r=6),
            tin="zoom", focus=(540, 800), cam="push")
    return close(r, DOTS + pings, "whipU")


def ff_door():
    r = reel("ff-reel-1018-the-door", "fullyfunded", "ff-hero-horizon-el.mp3", "#16206B", FFC)
    door = el('<div style="width:420px;height:640px;border-radius:24px 24px 0 0;background:linear-gradient(#2B3FE0,#16206B);'
              'border:10px solid #3B4FF0;box-shadow:0 0 120px rgba(255,176,143,.55),inset 0 0 60px rgba(0,0,0,.4);position:relative">'
              '<div style="position:absolute;right:40px;top:330px;width:36px;height:36px;border-radius:50%;background:#FF6A3D"></div></div>',
              330, 980, a="up", t=-0.6, d=0.6, loop="float", amp=0.4)
    r.scene(2, DEEP + head("100 a month. / From *birth.*", 450, "Hw", 170, em="emw", hook=True) + door, cam="push")
    r.scene(2, DEEP + head("Stop at *18.* / Never touch it.", 520, "Hw", 150, em="emw", t=0.0),
            tin="slit", color="#FFB08F", cam="push")
    r.scene(2, LITE + head("At 65, at 8% a year:", 460, "H", 100)
            + el('<span data-a="count" data-t="0.3" data-d="1.1" data-to="2036000" data-comma="1">0</span>', "c", 640, a="none", cls="H",
                 style="font-size:210px;color:#FF6A3D;letter-spacing:-.06em"), tin="zoom", focus=(540, 900), cam="push", shake=(1.4, 0.2, 14))
    r.scene(2, DEEP + kick("THE CATCH", "#FF6A3D", "#fff", y=400, a="stamp", r=-4)
            + head("In today's money: / about *409,000.*", 560, "Hw", 140, t=0.2, em="emw"), tin="stripes", color="#FF6A3D",
            color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, LITE + head("Send to / *new parents.*", 560, "H", 170) + img("ht-piggy.png", 330, 1170, 420, t=0.3, r=6), tin="push", cam="push")
    return close(r, DEEP + door, "zoom", focus=(540, 1200))


def lf_hunger():
    r = reel("lf-reel-1019am-hunger-cues", "littlefold", "lf-a-cosy-el.mp3", "#FFD6E3", LFC)
    bottle = emoji("🍼", 400, 1100, 300, t=-0.5, d=0.45, loop="wobble")
    r.scene(2, PINK + head("Crying is a / *late* hunger sign.", 450, "H", 150, hook=True) + bottle, cam="push")
    r.scene(2, BLOB + head("Watch for the / *early cues.*", 560, "H", 160) + emoji("👀", 420, 1170, 220, t=0.4, d=0.3, loop="float"),
            tin="blob", focus=(540, 900), color=LF["butter"], cam="push")
    card = lambda n, txt: el(f'<div class="card"><span class="num">{n}</span><div class="H" style="font-size:130px;margin-top:40px">{txt}</div></div>',
                             90, 600, 900, a="fly", t=0.0, d=0.5, r=-3 if n % 2 else 3)
    r.scene(2, BLOB2 + card(1, "Lip <span class='em'>smacking.</span>"), tin="slam", cam="rise")
    r.scene(2, PINK + card(2, "Rooting, <span class='em'>searching.</span>"), tin="whipL", cam="rise")
    r.scene(2, BLOB + card(3, "Squirming, <span class='em'>more alert.</span>"), tin="push", cam="rise")
    r.scene(2, BLOB2 + head("Missed them? / *Every parent does.*", 560, "H", 140), tin="flash", color=LF["peach"], color2=LF["butter"], cam="push")
    r.scene(2, PINK + kick("SOURCE: AAP", LF["acc"], "#fff", y=400) + head("Send to your / *night-feed partner.*", 560, "H", 130),
            tin="stripes", color=LF["pink"], color2=LF["butter"], color3=LF["peach"], cam="rise")
    return close(r, PINK + bottle, "blob", focus=(540, 900), color=LF["pink"])


def ff_gift():
    r = reel("ff-reel-1019am-gift-per-person", "fullyfunded", "ff-b-bright-pop-el.mp3", "#2B3FE0", FFC)
    gift = emoji("🎁", 380, 1100, 320, t=-0.5, d=0.4, loop="wobble")
    r.scene(2, COB + head("Budget per *person,* / not per total.", 460, "Hw", 150, em="emw", hook=True) + gift, cam="push", shake=(0.2, 0.2, 14))
    names = "".join('<div class="gl" style="background:rgba(14,20,64,.14);width:%d%%"></div>' % w for w in (70, 55, 80, 62, 74, 50))
    r.scene(2, LITE + head("Write every / *name* down.", 420, "H", 150)
            + el(f'<div class="card" style="width:760px">{names}</div>', 160, 860, 760, a="fly", t=0.3, d=0.5, r=-2), tin="whipL", cam="rise")
    r.scene(2, LITE + head("14 people × 25:", 460, "H", 110) + el('<span class="em">350</span>', "c", 640, a="pop", t=0.2, cls="H", style="font-size:220px"),
            tin="slam", cam="push")
    r.scene(2, LITE + head("At 20 each: / *280.*", 560, "H", 190), tin="zoom", focus=(540, 800), cam="push")
    r.scene(2, DEEP + kick("THE CATCH", "#FF6A3D", "#fff", y=400, a="stamp", r=-4) + head("Use money you / *already have.*", 560, "Hw", 140,
            t=0.2, em="emw"), tin="stripes", color="#FF6A3D", color2="#FFFFFF", color3="#2B3FE0", cam="tilt")
    r.scene(2, COB + head("Save before / you *shop.*", 560, "Hw", 180, em="emw") + emoji("🛍️", 420, 1170, 240, t=0.4, d=0.35, loop="float"),
            tin="push", cam="push")
    return close(r, COB + gift, "zoom", focus=(540, 900))


def lh_pick_task():
    r = reel("lh-reel-1019am-pick-task", "lockedhour", "lh-c-morning-drive-el.mp3", "#FFE27A", LHC + STRIKE)
    glass = img("ht-hourglass.png", 400, 1060, 300, t=-0.5, r=6, loop="wobble")
    r.scene(2, DOTS + kick("DAY 1", "#141414", "#FFE27A", y=360, a="none") + head("Task first. / *Timer second.*", 480, "H", 170, hook=True)
            + glass, cam="push", shake=(0.2, 0.2, 14))
    r.scene(2, DOTSC + head("One task, / *one line.*", 420, "H", 160)
            + el('<div class="paper"><div class="hand">Write the report</div></div>', 140, 860, 800, a="fly", t=0.3, d=0.45, r=-2),
            tin="stripes", color=LH["acc"], color2="#FFD43B", color3="#FFF4E0", cam="rise")
    r.scene(2, DOTSP + head("Too big? / *Shrink it.*", 600, "H", 190, em="emy"), tin="cut", cam="push", shake=(0.0, 0.2, 18))
    r.scene(2, DOTS + el(f'<div class="paper"><div class="H" style="font-size:96px">{strike("Write the report", 0.3)}</div>'
                         f'<div class="hand" style="margin-top:30px" data-a="type" data-t="0.7" data-d="0.6">Write the intro</div></div>',
                         110, 600, 860, a="fly", t=0.0, d=0.45, r=-2), tin="slam", cam="push")
    r.scene(2, DOTSC + head("Then *start.*", 420, "H", 170)
            + el('<span data-a="tick" data-mmss="1" data-from="3600" data-to="3596" data-t="0.2" data-d="1.6">60:00</span>', "c", 760, a="none",
                 cls="timer"), tin="whipU", cam="push")
    r.scene(2, DOTS + head("Send to your / *study buddy.*", 560, "H", 160) + img("ht-clock.png", 380, 1170, 320, t=0.4, r=-6),
            tin="iris", focus=(540, 900), color=LH["acc"], cam="push")
    return close(r, DOTS + glass, "zoom", focus=(540, 900))


def hb_just_asks():
    r = reel("hb-reel-1019am-just-the-asks", "hourback", "hb-a-ta-da-el.mp3", "#FFF8EF", HBC)
    card = mail_card(1080, -0.6, lines=6)
    r.scene(2, CREAM + head("8:47 am. / *255 words* / from the building.", 360, "H", 120, hook=True) + card, cam="push")
    r.scene(2, INDI + head("You need / *one thing.*", 600, "Hw", 180, em="emo2") + emoji("🤨", 420, 1170, 240, t=0.4, d=0.3, loop="wobble"),
            tin="whipL", cam="push")
    r.scene(2, PEACH + kick("ASK AI", "#5E54C9", "#fff", y=400) + bub("What are the asks? Quote each.", "me", y=620, t=0.2), tin="slam", cam="rise")
    r.scene(2, CREAM + kick("AI REPLY", "#FFC94D", "#2A2238", y=400) + bub("Car out · Tue 7 am<br>Bike tag · Fri<br>Party · optional", "ai",
            y=600, t=0.15, w=860), tin="pixel", cam="push")
    r.scene(2, INDI + head("All 3 / *checked.*", 600, "Hw", 190, em="emo2") + emoji("✅", 430, 1170, 220, t=0.4, d=0.3, loop="pulse"),
            tin="glitch", td=0.2, cam="push")
    r.scene(2, CREAM + head("Send to your / *neighbour.*", 560, "H", 170) + img("ht-point.png", 260, 1170, 520, t=0.3, r=-6),
            tin="zoom", focus=(540, 800), cam="push")
    return close(r, CREAM + card, "whipU")


for _f in (lf_3am, ff_lower_rate, lh_pick_3, hb_freeze, hb_school, lf_breathe, lh_mute, ff_door, lf_hunger, ff_gift, lh_pick_task, hb_just_asks):
    R[_f().rid] = _f


# =============================================================================================== alt text + caption AI line
PALETTE = {"fullyfunded": "cobalt, white and coral", "lockedhour": "butter yellow, cream and pink", "hourback": "indigo, cream, peach and yellow",
           "littlefold": "soft Sherbet pastels"}
AI_ASSETS = ("lf-sil-", "lf-shoulders", "ff-street", "hb-clouds", "ht-")


def beat_texts(r):
    import re as _re
    out = []
    for sc in r.scenes:
        h = _re.sub(r'<span class="chip.*?</div>', " ", sc["html"])
        h = _re.sub(r"<br\s*/?>", " ", h)
        h = _re.sub(r'<span class="emo"[^>]*>.*?</span>', " ", h)
        h = _re.sub(r'<span data-a="(?:count|tick)"[^>]*data-to="(\d+)"[^>]*>[^<]*</span>',
                    lambda m: f"{int(m.group(1)):,}" if "mmss" not in m.group(0) else "60:00", h)
        h = _re.sub(r'<span data-a="tick"[^>]*>[^<]*</span>', "60:00", h)
        h = _re.sub("[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F]", " ", h)
        t = " ".join(_re.sub(r"<[^>]+>", " ", h).split())
        t = t.replace("Fully Funded", "").replace("Locked Hour", "").replace("Hourback", "").replace("Littlefold", "").strip()
        if t:
            out.append(t)
    return out


def alt_text(rid):
    r = readable(rid)
    beats = beat_texts(r)
    return (f"Video in {PALETTE[r.brand]}, one line at a time, slow enough to read. Text: " + " / ".join(beats).rstrip(".")
            + ". It loops back to the opening line.")


def uses_ai_images(rid):
    html = "".join(sc["html"] for sc in R[rid]().scenes)
    return any(a in html for a in AI_ASSETS)


def fix_caption(rid, cap):
    import re as _re
    pat = _re.compile(r"^(?:(?:[A-Z][A-Za-z ,]*? )?(?:[Ii]mages?|[Pp]hotos?) made with AI\.|The narrator voice is AI-generated\.)[ \t]*$", _re.M)
    line = "Images made with AI." if uses_ai_images(rid) else ""
    found = pat.findall(cap)
    if found:
        cap = pat.sub("\x00", cap)
        cap = cap.replace("\x00", line, 1).replace("\x00", "")
        cap = _re.sub(r"\n{3,}", "\n\n", cap)
    elif line:
        k = cap.rfind("\n\n#")
        cap = cap[:k] + "\n\n" + line + cap[k:] if k > 0 else cap + "\n\n" + line
    return cap


# =============================================================================================== build
def readable(rid):
    r = R[rid]()
    make_readable(r)
    return r


def build(rid, outdir, qa_only=False, dsf=2):
    r = readable(rid)
    rep = reading_report(r)
    assert all(x["ok"] for x in rep), rep  # READABLE PACING (0.4 s/word + 0.6 s)
    work = Path(outdir) / rid
    work.mkdir(parents=True, exist_ok=True)
    info = dict(id=rid, dur=round(r.duration, 2), beats=[(x["dur"], x["words"], x["need"]) for x in rep])
    if not qa_only:
        fdir, n = render_frames(r, work, dsf=dsf)
        out = work / f"{rid}.mp4"
        encode(fdir, n, LIB / r.music, out)
        from PIL import Image
        import kit as _k
        Image.open(fdir / f"00000.{_k.FRAME_EXT}").convert("RGB").save(work / f"{rid}-cover.jpg", quality=92)
        sheet(fdir, qa_times(r), work / f"{rid}-qa.jpg", cols=10, scale=0.16)
        info.update(probe=probe(out), lufs=loudness(out), music=r.music)
        shutil.rmtree(fdir, ignore_errors=True)  # frames are ~1 GB per Reel; the QA sheet and cover are kept
    print(json.dumps(info), flush=True)
    return r


def install(rid, outdir):
    work = Path(outdir) / rid
    for src, dst in [(work / f"{rid}.mp4", REPO / "media" / "reels" / f"{rid}.mp4"),
                     (work / f"{rid}-cover.jpg", REPO / "media" / "reels" / f"{rid}-cover.jpg")]:
        shutil.copyfile(src, dst)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--out", default="/tmp/share-out")
    ap.add_argument("--qa-only", action="store_true")
    ap.add_argument("--check", action="store_true", help="pacing + text overflow only, no render")
    ap.add_argument("--install", action="store_true", help="copy the rendered mp4 + cover into media/reels/")
    a = ap.parse_args()
    for i in a.ids or list(R):
        if a.check:
            r = readable(i)
            print(i, round(r.duration, 1), "s", "pace OK" if all(x["ok"] for x in reading_report(r)) else "PACE FAIL",
                  "overflow:", overflow_check(r) or "none", flush=True)
        elif a.install:
            install(i, a.out)
        else:
            build(i, a.out, a.qa_only)

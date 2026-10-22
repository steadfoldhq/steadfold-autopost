"""Three LH Reels rebuilt for the Oct 24-25 queue: lyrics, planning fallacy, unpack. <=14 s, payoff by ~2 s."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from reelkit import *  # noqa

M = Path("/home/claude/steadfold-autopost/media")
OUT = M / "recovery-oct22/lockedhour/reels"
OUT.mkdir(parents=True, exist_ok=True)

def D(text, field, size, align="center", extra=""):
    return dual(text, field, style=f"font-size:{size}px;text-align:{align};{extra}")

def at(x, y, inner, t=0, k="up", w=None, base=""):
    ww = f"width:{w}px;" if w else ""
    return (f"<div data-in='{t}' data-k='{k}' data-base='{base}' style='position:absolute;left:{x}px;top:{y}px;{ww}"
            f"transform:{base}'>{inner}</div>")

def hand(txt, size=64, color=None):
    c = f"color:{color};" if color else ""
    return f"<div class='hand' style='font-size:{size}px;{c}'>{txt}</div>"

def mono(txt, size=26):
    return f"<div class='mono' style='font-size:{size}px;line-height:1.4;opacity:.85;text-align:center'>{txt}</div>"

def chip(txt, bg, size=46, rot=0):
    return (f"<div style='display:inline-block;background:{bg};border:4px solid {INK};border-radius:18px;padding:10px 22px;"
            f"box-shadow:7px 7px 0 {INK};font:800 {size}px/1.1 Inter Display,Inter,sans-serif;color:{INK};transform:rotate({rot}deg)'>{txt}</div>")

def dothis(lines, field, size=92):
    return (at(90, 330, f"<div class='dothis' style='font-size:130px;text-align:center'>Do this:</div>", 0, w=900) +
            at(110, 560, f"<div class='card' style='position:relative;padding:54px 46px'>{D(lines, field, size)}</div>", 0.15, "pop", w=860))

def stampx(x=820, y=1440, t=0.15):
    return at(x, y, stamp(0, 0, 160, -12).replace("position:absolute;left:0px;top:0px;", "position:relative;"), t, "pop")

# ------------------------------------------------------------------ LYRICS
def lyrics():
    hook_body = lambda line: (
        at(90, 330, D("Studying with / *your playlist* / on?", "pink", 158), 0, w=900) +
        at(90, 880, anim_ring(440, 0.0, 0.0, 0, 1, centre="♪", sub="", col=BUTTER, font=170), 0) +
        at(560, 960, hand(line, 68), 0, w=430) + stampx(820, 1420))
    hook = lambda line: (
        at(90, 330, D("Studying with / *your playlist* / on?", "pink", 158), 0, w=900) +
        at(90, 880, anim_ring(440, 0.0, 0.45, 0.05, 1.6, centre="♪", sub="", col=BUTTER, font=170), 0) +
        at(560, 960, hand(line, 68), 0, w=430) + stampx(820, 1420))
    sc = [
        scene(0, 1.8, "pink", hook("check the words before you press play")),
        scene(1.8, 4.2, "dots",
              at(90, 330, D("Songs *with words* / lowered reading / scores.", "dots", 138), 0, w=900) +
              at(90, 900, hand("even songs they liked.", 92), 0.9, "pop", w=900) +
              at(150, 1100, chip("quiet ✓", "#FFFDF6", 50, -3), 1.25, "drop") +
              at(430, 1100, chip("no words ✓", F['dots']['p1'], 50, 2), 1.45, "drop") +
              at(170, 1230, chip("songs with words ✗", "#FFFDF6", 50, -1), 1.65, "drop") +
              at(90, 1370, mono("Perham &amp; Currie 2014 · 30 students · reading test"), 0.3, w=900), "slam"),
        scene(4.2, 6.6, "cream",
              at(90, 360, D("No words? / *About as good* / *as quiet.*", "cream", 150), 0, w=900) +
              at(340, 960, anim_ring(400, 0.0, 1.0, 0.2, 1.6, centre="60:00", sub="focus hour", col=PINK, font=78), 0.0) +
              stampx(90, 1420, 0.3), "iris"),
        scene(6.6, 9.0, "pink",
              at(90, 330, D("Lyrics and the page / fight for *the same* / *word lane.*", "pink", 128), 0, w=900) +
              at(310, 880, ring(460, 1.0, "", "", col=BUTTER), 0) +
              at(90, 790, chip("la la la…", BUTTER, 54, -6), 0.2, "left") +
              at(640, 790, chip("page 42…", "#FFFDF6", 54, 5), 0.35, "pop") +
              "<div data-jit='0.6' style='position:absolute;left:0;top:0'></div>" +
              at(90, 1360, hand("only one gets through.", 70), 0.9, "up", w=900), "wipe"),
        scene(9.0, 11.4, "dots", dothis("Make one *no-lyrics* / playlist. Play it / every focus hour.", "dots", 92) +
              at(90, 1250, hand("save the songs you love for chores.", 60), 0.8, w=900), "push"),
        scene(11.4, 13.2, "pink", hook_body("follow for one focus fix a day"), "plate"),
    ]
    return sc, 13.2, hook_body("check the words before you press play")

# ------------------------------------------------------------------ PLANNING FALLACY
def ruler(t_guess, t_took, t_worst):
    px = 13.5  # px per day, 60 days = 810
    x0 = 135
    ticks = "".join(f"<div style='position:absolute;left:{x0+d*px-2}px;top:0;width:4px;height:{34 if d%10==0 else 18}px;background:{INK}'></div>"
                    + (f"<div class='mono' style='position:absolute;left:{x0+d*px-30}px;top:44px;width:60px;text-align:center;font-size:26px'>{d}</div>" if d % 10 == 0 else "")
                    for d in range(0, 61, 5))
    return (f"<div style='position:absolute;left:0;top:1180px;width:1080px;height:120px'>{ticks}</div>"
            f"<div style='position:absolute;left:{x0}px;top:1010px;height:70px;width:0;background:{BUTTER};border:5px solid {INK};border-radius:12px' data-grow='{t_guess},0.6,0,{34*px}'></div>"
            f"<div style='position:absolute;left:{x0}px;top:1090px;height:70px;width:0;background:{PINK};border:5px solid {INK};border-radius:12px' data-grow='{t_took},0.9,0,{56*px}'></div>"
            + at(x0 + 49 * px - 6, 960, f"<div style='width:6px;height:220px;background:{DPINK}'></div>", t_worst, "pop")
            + at(x0 + 49 * px - 250, 880, hand("worst-case guess: 49", 54), t_worst, "pop", w=330))

def planning():
    hook = lambda line: (
        at(90, 330, D("Everything / takes longer? / *It's not just you.*", "dots", 150), 0, w=900) +
        at(110, 1010, f"<img class='obj' src='{obj('hourglass')}' style='width:250px;transform:rotate(-8deg)'>", 0.12, "drop") +
        at(420, 1080, hand(line, 62), 0, w=540) + stampx(820, 1420, 0.18))
    sc = [
        scene(0, 1.8, "dots", hook("you're not bad at planning. everyone is.")),
        scene(1.8, 4.8, "cream",
              at(90, 330, D("Students guessed / their thesis: *34 days.*", "cream", 120), 0, w=900) +
              at(90, 640, f"<div class='S' style='font-size:150px'>It took <span class='pill riso' style='background:{F['cream']['p1']}' data-roll='1.1,0.9,34,56' data-suf=''>56</span>.</div>", 1.0, "pop", w=900) +
              ruler(0.2, 1.1, 2.0) +
              at(90, 1380, mono("Buehler, Griffin &amp; Ross 1994 · 37 students"), 0.3, w=900), "slam"),
        scene(4.8, 7.2, "pink",
              at(90, 330, D("We plan for the day / *everything goes right.*", "pink", 128), 0, w=900) +
              at(110, 800, chip("no slow replies", "#FFFDF6", 52, -4), 0.3, "drop") +
              at(470, 930, chip("no sick day", BUTTER, 52, 3), 0.55, "drop") +
              at(150, 1070, chip("no file that won't open", "#FFFDF6", 52, -2), 0.8, "drop") +
              at(90, 1250, hand("real days don't go like that.", 70), 1.2, "up", w=900), "wipe"),
        scene(7.2, 9.6, "dots",
              at(90, 360, D("Ask: how long did / it take *last time?*", "dots", 140), 0, w=900) +
              at(90, 820, hand("not: how long should it take?", 78), 0.6, "pop", w=900) +
              at(340, 960, anim_ring(400, 0.0, 0.75, 0.3, 1.5, centre="?", sub="last time", col=PINK, font=150), 0), "iris"),
        scene(9.6, 12.0, "cream", dothis("Add half again. / *2 hours? Plan 3.*", "cream", 104) +
              at(90, 1150, hand("Part 2 tonight at 7: break it into steps.", 60), 0.8, w=900), "push"),
        scene(12.0, 13.8, "dots", hook("follow for one focus fix a day"), "plate"),
    ]
    return sc, 13.8, hook("you're not bad at planning. everyone is.")

# ------------------------------------------------------------------ UNPACK
def taskcard(t=0):
    return at(150, 1000, f"<div class='card' style='position:relative;padding:30px 40px;transform:rotate(-3deg)'>"
                         f"<div class='mono' style='font-size:28px;opacity:.7'>TO DO · MONDAY</div>"
                         f"<div class='S' style='font-size:84px;text-align:left'>Update the website <span style='font-family:DejaVu Sans Mono;font-size:44px'>(1 h)</span></div></div>",
              t, "pop", w=780)

def unpack():
    hook = lambda line: (
        at(90, 330, D("“It'll take / an hour.” / *It won't.*", "cream", 160), 0, w=900) +
        taskcard(0) + at(90, 1290, hand(line, 62), 0, w=900) + stampx(840, 1430, 0.15))
    steps = [("find the old photos", "15 min"), ("wait for the new ones", "1 day"), ("write the new text", "45 min"),
             ("check, then fix", "30 min + 1 day"), ("upload + test", "20 min")]
    stepchips = "".join(at(110 + (i % 2) * 40, 690 + i * 112,
                           f"<div style='display:flex;gap:14px;align-items:center'>{chip(f'{i+1}. {a}', '#FFFDF6' if i%2 else F['dots']['p1'], 44)}"
                           f"<span class='mono' style='font-size:34px;font-weight:700'>{b}</span></div>", 0.25 + i * 0.22, "left", w=900)
                         for i, (a, b) in enumerate(steps))
    sc = [
        scene(0, 1.8, "cream", hook("save this for Monday")),
        scene(1.8, 4.8, "dots",
              at(90, 330, D("List the steps / *before* you guess.", "dots", 140), 0, w=900) + stepchips +
              at(90, 1290, f"<div class='S' style='font-size:70px'>= <span class='pill' style='background:{F['dots']['p1']}'>2 h of work + 2 days of waiting</span></div>", 1.6, "pop", w=900) +
              at(90, 1400, mono("Made up for this post.", 24), 1.6, w=900), "slam"),
        scene(4.8, 7.2, "pink",
              at(90, 360, D("People who listed / the steps made / *more realistic* / guesses.", "pink", 128), 0, w=900) +
              at(90, 1120, hand("hidden steps are where the time goes.", 66), 0.7, "up", w=900) +
              at(90, 1380, mono("Kruger &amp; Evans 2004 · J. Experimental Social Psychology"), 0.3, w=900), "iris"),
        scene(7.2, 9.6, "cream",
              at(90, 330, D("Always add the / *hidden steps:*", "cream", 140), 0, w=900) +
              at(110, 760, chip("waiting on someone", BUTTER, 56, -3), 0.2, "drop") +
              at(520, 900, chip("setup", "#FFFDF6", 56, 4), 0.4, "drop") +
              at(140, 1040, chip("the back-and-forth", F['cream']['p1'], 56, -2), 0.6, "drop") +
              at(480, 1180, chip("the final check", "#FFFDF6", 56, 3), 0.8, "drop"), "wipe"),
        scene(9.6, 12.0, "dots", dothis("Tonight: list Monday's / biggest task, *step* / *by step.* Then guess.", "dots", 88), "push"),
        scene(12.0, 13.8, "cream", hook("follow for one focus fix a day"), "plate"),
    ]
    return sc, 13.8, hook("save this for Monday")

SPECS = {
    "lh-reel-1024-lyrics": (lyrics, "pink"),
    "lh-reel-1025am-planning-fallacy": (planning, "dots"),
    "lh-reel-1025-unpack": (unpack, "cream"),
}

if __name__ == "__main__":
    ids = sys.argv[1:] or list(SPECS)
    preview = "--preview" in ids
    ids = [i for i in ids if not i.startswith("--")] or list(SPECS)
    for rid in ids:
        fn, field = SPECS[rid]
        sc, dur, cov = fn()
        cover(cov, field, OUT / f"{rid}-r1-cover.jpg")
        render(rid, sc, dur, M / f"reels/{rid}-s15.mp4", OUT / f"{rid}-r1.mp4")
        print("done", rid)

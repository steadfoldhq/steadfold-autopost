#!/usr/bin/env python3
"""Oct 26 studio build, Fully Funded Reels (Wed/Thu 7 pm, no trial flag). Performance desk order 2: "trap rule with a date".
Imports the FF kit (studio/recovery-oct22/fullyfunded/build/ff_reels.py) and the motion kit; nothing in them is rewritten.

  ff-reel-1028-fhsa-room     Wed Oct 28 19:00  CANADA. FHSA room only starts when you open one: open by Dec 31 -> 2026's $8,000.
                                               Style: FOLLOW THE LINE (dot paper, one coral line travelling Today -> Dec 31 -> Jan 1).
  ff-reel-1029-fsa-expires   Thu Oct 29 19:00  US. Health FSA money not spent by the plan's end date can be lost (use-or-lose).
                                               Style: KINETIC BIG TEXT (soft-coral field, giant DEC 31, a calendar page that tears off).

    python3 studio/editorial/oct26_fullyfunded.py <id> [--qa-only] [--cover-only]  < /dev/null
Outputs: media/studio-oct26/fullyfunded/<id>.mp4 + <id>-cover.jpg. Frames go to the scratch dir and are deleted after each encode.
"""
import argparse, json, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
SCR = Path("/tmp/claude-0/ff26")
sys.path.insert(0, str(REPO / "studio/recovery-oct22/fullyfunded/build"))

import glob as _glob  # noqa: E402
_g0 = _glob.glob
_glob.glob = lambda pat, *a, **k: _g0(pat, *a, **k) or _g0(pat.replace("chrome-linux/", "chrome-linux64/"), *a, **k)

import ff_reels as FF  # noqa: E402,F401
from ff_reels import Reel, el, words, stamp, svg, path, txt, COB, INK, CORAL, SOFT, PAPER, CREAM, CSS  # noqa: E402
from kit import (reading_report, overflow_check, render_frames, encode, sheet, qa_times, probe, loudness,  # noqa: E402
                 FONTS, BASE_CSS)

OUT = REPO / "media/studio-oct26/fullyfunded"
DCORAL = "#E04E28"
CSSX = CSS + "svg *{transform-box:fill-box;transform-origin:center}" + f"""
.dots{{background:radial-gradient(rgba(43,63,224,.16) 2px,transparent 2.4px) 0 0/36px 36px,{CREAM}}}
.coralf{{background:radial-gradient(rgba(14,20,64,.07) 1.4px,transparent 1.8px) 0 0/22px 22px,#FFE4D6}}
.tag{{font-family:'DejaVu Sans Mono';font-weight:700;font-size:38px;letter-spacing:.12em;color:#fff;background:{COB};
      border-radius:999px;padding:12px 30px;display:inline-block}}
.K{{font-family:'Inter Display';font-weight:800;letter-spacing:-.045em;line-height:.9;color:{COB}}}
.H .w{{margin-right:.04em}}
"""

# ------------------------------------------------------------------------------------------------ MATHS (on-screen figures)
FHSA_YEAR = 8_000                 # CRA: room in the year you open your first FHSA
FHSA_CARRY_MAX = 8_000            # CRA: carry-forward of unused room, at most $8,000
OPEN_DEC = FHSA_YEAR + min(FHSA_CARRY_MAX, FHSA_YEAR)   # opened in 2026, nothing put in -> 2027 room
OPEN_JAN = FHSA_YEAR                                     # first opened in Jan 2027 -> 2027 room
assert (OPEN_DEC, OPEN_JAN) == (16_000, 8_000)


def timing(r, durs):
    for sc, d in zip(r.scenes, durs):
        sc["dur"] = d
    t = 0.0
    for sc in r.scenes:
        sc["start"] = round(t, 4)
        t += sc["dur"]
    r.t = t
    return r


def do_this(y=300):
    return el('<span class="save" style="font-size:88px">do this:</span>', "c", y, a="pop", t=0.0, r=-3)


# ============================================================================== 1. FHSA room (Wed Oct 28, 7 pm) FOLLOW THE LINE
LY = 1430                         # the line's baseline
LX0, LXD, LX1 = 130, 560, 900     # TODAY ... DEC 31 ... JAN 1


def calendar_card(x, y, top="DEC", big="31", w=190, col=CORAL, t=None):
    a = f' data-a="pop" data-t="{t}" data-d="0.3"' if t is not None else ""
    return (f'<g{a}><rect x="{x - w / 2}" y="{y}" width="{w}" height="{w * 1.02:.0f}" rx="22" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
            f'<rect x="{x - w / 2}" y="{y}" width="{w}" height="{w * 0.32:.0f}" rx="22" fill="{col}" stroke="{INK}" stroke-width="6"/>'
            + txt(x, y + w * 0.24, top, w * 0.2, "#FFFFFF", weight=700)
            + f'<text x="{x}" y="{y + w * 0.88:.0f}" font-size="{w * 0.5:.0f}" fill="{INK}" text-anchor="middle" '
              f'style="font-family:Inter Display" font-weight="800">{big}</text></g>')


def line(t=None, upto=LX1, tick=False):
    """The coral line, stations TODAY / DEC 31 / JAN 1. t=None: already drawn."""
    T = (lambda k: None) if t is None else (lambda k: t + k)  # noqa: E731
    parts = [path(f"M{LX0},{LY} L{upto},{LY}", CORAL, 16, T(0), 0.7)]
    for x, lab in ((LX0, "TODAY"), (LXD, "DEC 31"), (LX1, "JAN 1")):
        if x <= upto:
            parts.append(f'<circle cx="{x}" cy="{LY}" r="22" fill="{CREAM}" stroke="{INK}" stroke-width="7"/>')
            parts.append(txt(x, LY + 86, lab, 44, INK, "middle" if x != LX0 else "start", 700))
    if tick:
        parts.append(path(f"M{LXD - 22},{LY} L{LXD - 6},{LY + 18} L{LXD + 26},{LY - 22}", COB, 9))
    return "".join(parts)


def runner(t0, x0, x1, dur):
    """A cobalt dot that travels along the line (the viewer follows it)."""
    return (f'<g data-a="right" data-t="{t0}" data-d="{dur}"><circle cx="{x1}" cy="{LY}" r="30" fill="{COB}"/></g>'
            if x0 != x1 else f'<circle cx="{x1}" cy="{LY}" r="30" fill="{COB}"/>')


def fhsa():
    r = Reel("ff-reel-1028-fhsa-room", "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    defn = el('<span class="M" style="font-size:34px;line-height:1.5;color:#141A55">FHSA = FIRST HOME SAVINGS ACCOUNT<br>FOR FIRST-TIME BUYERS IN CANADA</span>',
              "c", 712, a="none")
    # frame 0: the rule as a fact + what FHSA means + the date on the line (moved down: CD gate)
    r.scene(4, "".join([
        '<div class="par dots"></div>', stamp(830, 190, 150, t=0.2),
        el('<span class="tag">CANADA · FHSA</span>', "c", 300, a="none"),
        el('No FHSA open?<br><span class="em">No room yet.</span>', "c", 400, a="none", cls="H", style="font-size:136px"),
        defn,
        svg(calendar_card(LXD, 890, w=270) + path(f"M{LXD},{890 + 280} L{LXD},{LY - 26}", INK, 5, dash="10 10") + line()),
        svg(f'<circle cx="{LX0}" cy="{LY}" r="30" fill="{COB}" data-a="pop" data-t="0.15" data-d="0.3"/>'),
    ]), cam="push", shake=(0.2, 0.2, 10))
    # payoff: the dot travels to DEC 31, OPENED marker, the 2026 $8,000 block drops onto the line; "room" defined in words
    block = (f'<g data-a="pop" data-t="1.0" data-d="0.35"><rect x="{LX0}" y="{LY - 250}" width="{LXD - LX0}" height="190" rx="18" '
             f'fill="{COB}"/>' + f'<text x="{(LX0 + LXD) / 2}" y="{LY - 128}" font-size="92" fill="#FFFFFF" text-anchor="middle" '
             f'style="font-family:Inter Display" font-weight="800">$8,000</text></g>')
    r.scene(9, "".join([
        '<div class="par dots"></div>',
        words("Open one by *Dec 31:* / 2026's $8,000 room / is yours.", "c", 330, t=0.0, gap=0.07, cls="H", style="font-size:100px"),
        el('<span class="save" style="font-size:56px">room = how much you\'re allowed to put in</span>', "c", 700, a="pop", t=0.6, r=-2),
        svg(line() + block + txt(LXD + 30, LY - 300, "OPENED", 46, DCORAL, "start", 700, t=0.8)
            + path(f"M{LXD},{LY - 30} L{LXD},{LY - 320}", DCORAL, 7, 0.7, 0.25)),
        svg(runner(0.15, LX0, LXD, 0.55)),
    ]), tin="whipL", td=0.2, cam="right", shake=(1.35, 0.2, 10))
    # stakes: headline static from the first frame (no near-blank in-between frame), bars drawn to scale (840 px = $16,000)
    W = 840
    wd, wj = W, W * OPEN_JAN / OPEN_DEC
    y1, y2 = 1100, 1380
    r.scene(9, "".join([
        '<div class="par dots"></div>',
        el('Open in January?<br>Your 2027 room:<br><span class="em">$8,000,</span> not <span class="em">$16,000.</span>', "c", 330, a="none",
           cls="H", style="font-size:96px"),
        el('<span class="save" style="font-size:62px">unused room carries over (up to 1 year)</span>', "c", 690, a="pop", t=0.2, r=-2),
        svg("".join([
            txt(120, y1 - 26, "OPENED BY DEC 31 · 2027 ROOM", 36, COB, "start", 700, t=0.3),
            f'<path d="M120,{y1 + 60} L{120 + wd:.0f},{y1 + 60}" stroke="{COB}" stroke-width="120" fill="none" data-a="draw" data-t="0.35" data-d="0.6"/>',
            txt(120 + wd - 26, y1 + 84, f"${OPEN_DEC:,}", 66, "#FFFFFF", "end", 700, t=0.9),
            txt(120, y2 - 26, "OPENED IN JANUARY · 2027 ROOM", 36, DCORAL, "start", 700, t=1.1),
            f'<path d="M120,{y2 + 60} L{120 + wj:.0f},{y2 + 60}" stroke="{CORAL}" stroke-width="120" fill="none" data-a="draw" data-t="1.15" data-d="0.4"/>',
            txt(120 + wj - 26, y2 + 84, f"${OPEN_JAN:,}", 66, "#FFFFFF", "end", 700, t=1.5),
            f'<rect x="{120 + wj:.0f}" y="{y2}" width="{wd - wj:.0f}" height="120" fill="none" stroke="{DCORAL}" stroke-width="5" '
            f'stroke-dasharray="16 12" data-a="fade" data-t="1.7" data-d="0.3"/>',
        ])),
    ]), tin="cut", cam="push", shake=(0.0, 0.2, 14))
    # do this: names the place; follow line on the end frame
    r.scene(7, "".join([
        '<div class="par dots"></div>', do_this(290),
        words("Open an FHSA at your / *bank or investing app* / before Dec 31.", "c", 400, t=0.1, gap=0.06, cls="H", style="font-size:92px;white-space:nowrap"),
        svg(calendar_card(LXD - 60, 790, w=250, t=0.4)
            + path(f"M{LXD + 100},{930} L{LXD + 145},{980} L{LXD + 230},{870}", COB, 14, 0.7, 0.3)),
        el('<span class="M" style="font-size:34px;color:#141A55">FOR FIRST-TIME HOME BUYERS IN CANADA</span>', "c", 1095, a="fade", t=0.6),
        el('<span class="save" style="font-size:66px">Follow for one money move a day, in plain words.</span>', "c", 1200, a="pop", t=0.9, r=-2),
        stamp(850, 1400, 130, t=0.6),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.loop(1.0, tin="cut")
    return timing(r, (1.6, 3.9, 4.3, 4.6, 0.5))


# ============================================================================== 2. FSA use-or-lose (Thu Oct 29, 7 pm) KINETIC BIG TEXT
def tear_cal(x, y, w=420, t=None):
    """Big calendar page DEC 31; with t, the page tears off and falls (the year is over)."""
    page = (f'<rect x="{x}" y="{y}" width="{w}" height="{w * 0.95:.0f}" rx="34" fill="#FFFFFF" stroke="{INK}" stroke-width="8"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{w * 0.28:.0f}" rx="34" fill="{COB}" stroke="{INK}" stroke-width="8"/>'
            + f'<text x="{x + w / 2}" y="{y + w * 0.2:.0f}" font-size="{w * 0.15:.0f}" fill="#FFFFFF" text-anchor="middle" '
              f'font-family="DejaVu Sans Mono" font-weight="700" letter-spacing="6">DEC</text>'
            + f'<text x="{x + w / 2}" y="{y + w * 0.8:.0f}" font-size="{w * 0.48:.0f}" fill="{INK}" text-anchor="middle" '
              f'font-family="Inter Display" font-weight="800">31</text>')
    rings = "".join(f'<rect x="{x + w * k - 12}" y="{y - 26}" width="24" height="60" rx="12" fill="{INK}"/>' for k in (0.28, 0.72))
    return page + rings


def fsa():
    r = Reel("ff-reel-1029-fsa-expires", "fullyfunded", bpm=95, css=CSSX, stage="#FFE4D6")
    r.scene(4, "".join([
        '<div class="par coralf"></div>', stamp(840, 190, 140, t=0.2),
        el('<span class="tag">US · HEALTH FSA</span>', "c", 300, a="none"),
        el('Your FSA money<br><span class="em">can expire.</span>', "c", 390, a="none", cls="H", style="font-size:120px;white-space:nowrap"),
        el('<span class="K" style="font-size:290px">DEC 31</span>', "c", 690, a="none"),
        el('<span class="M" style="font-size:30px;color:#141A55">PLANS THAT RUN JAN – DEC</span>', "c", 975, a="fade", t=0.1),
        svg(tear_cal(330, 1150, 420)),
    ]), cam="push", shake=(0.25, 0.2, 10))
    # payoff: kinetic one-at-a-time, the calendar page tears and falls, "$" chips fade out
    r.scene(9, "".join([
        '<div class="par coralf"></div>',
        words("Not spent by / your plan's end date? / *You lose it.*", "c", 330, t=0.0, gap=0.07, cls="H", style="font-size:98px;white-space:nowrap"),
        el('<span class="K" style="font-size:250px;color:#E04E28">$0</span>', "c", 860, a="stamp", t=1.6, d=0.35, r=-6),
        svg(tear_cal(330, 1250, 420) + path("M300,1290 L780,1650", DCORAL, 16, 1.0, 0.3)),
    ]), tin="whipU", td=0.2, cam="push", shake=(1.65, 0.22, 14))
    # the catch: some plans give extra time OR let a little carry over (not both)
    x0, y0 = 110, 1050
    seg = 860 / 5.5          # Oct..Mar 15 drawn to scale, px per month
    months = ["OCT", "NOV", "DEC", "JAN", "FEB", "MAR"]
    cal = "".join(txt(x0 + seg * (i + 0.5), y0 + 160, m, 46, INK, weight=700) for i, m in enumerate(months))
    cal += path(f"M{x0},{y0 + 90} L{x0 + 860},{y0 + 90}", INK, 10)
    cal += "".join(path(f"M{x0 + seg * i:.0f},{y0 + 70} L{x0 + seg * i:.0f},{y0 + 110}", INK, 5) for i in range(6))
    xd = x0 + seg * 3
    cal += path(f"M{xd:.0f},{y0 - 20} L{xd:.0f},{y0 + 120}", DCORAL, 8)
    cal += txt(xd, y0 - 46, "DEC 31", 52, DCORAL, weight=700)
    cal += (f'<rect x="{xd:.0f}" y="{y0 + 20}" width="{seg * 2.5:.0f}" height="140" rx="14" fill="rgba(43,63,224,.25)" '
            f'stroke="{COB}" stroke-width="5" data-a="fade" data-t="0.9" data-d="0.3"/>')
    cal += txt(x0 + 860, y0 + 260, "UP TO 2½ MORE MONTHS", 46, COB, "end", 700, t=1.3)
    r.scene(9, "".join([
        '<div class="par coralf"></div>',
        words("Some plans give / *2½ extra months,* / or let a little / carry over.", "c", 300, t=0.0, gap=0.08, cls="H",
              style="font-size:96px"),
        svg(cal),
    ]), tin="stripes", td=0.2, cam="left", color=COB, color2=SOFT, color3="#FFFFFF")
    r.scene(7, "".join([
        '<div class="par coralf"></div>', do_this(300),
        words("Log in to your FSA or / benefits account today. / *Check your balance* / *and deadline.*", "c", 400, t=0.1, gap=0.06, cls="H", style="font-size:90px;white-space:nowrap"),
        el('<span class="K" style="font-size:170px">DEC 31</span>', "c", 880, a="pop", t=0.6),
        el('<span class="save" style="font-size:66px">Follow for one money move a day, in plain words.</span>', "c", 1110, a="pop", t=0.9, r=-2),
        stamp(840, 1260, 140, t=0.7),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.loop(1.0, tin="cut")
    return timing(r, (1.4, 3.9, 4.6, 4.8, 0.3))


REELS = {
    "ff-reel-1028-fhsa-room": (fhsa, "save this before Dec 31", 1590, REPO / "media/music/library/v4/ff-x-big-reveal.mp3"),
    "ff-reel-1029-fsa-expires": (fsa, "check yours before Dec 31", 1560, REPO / "media/music/library/v4/ff-x-level-up.mp3"),
}


def cover(r, out, save, y):
    """Dedicated cover: the hook scene settled + a handwritten save-line, rendered at 2x (never a raw frame)."""
    from playwright.sync_api import sync_playwright
    from PIL import Image
    import io
    s0 = r.scenes[0]
    html = s0["html"]
    for a in ("stamp", "pop", "draw", "fade", "right", "drop", "down"):
        html = html.replace(f'data-a="{a}"', 'data-a="none"')
    html += el(f'<span class="save" style="font-size:66px">{save}</span>', "c", y, a="none", r=-2)
    page = (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}{BASE_CSS}{r.css}"
            f".el{{position:absolute}}.par{{position:absolute;inset:0}}</style></head><body><div class='scene' style='display:block;background:{s0['bg']}'>"
            f"<div class='cam'>{html}</div></div></body></html>")
    SCR.mkdir(parents=True, exist_ok=True)
    tmp = SCR / f"{Path(out).stem}.html"
    tmp.write_text(page)
    chrome = _glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")[0]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chrome, args=["--disable-gpu", "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=2)
        pg.goto(tmp.as_uri())
        pg.wait_for_timeout(800)
        im = Image.open(io.BytesIO(pg.screenshot(type="png"))).convert("RGB").resize((1080, 1920), Image.LANCZOS)
        im.save(out, quality=92, subsampling=0)
        b.close()
    tmp.unlink()


def build(rid, qa_only=False, cover_only=False):
    fn, save, y, music = REELS[rid]
    r = fn()
    print(json.dumps(reading_report(r)))
    print("duration", round(r.duration, 2), "overflow", overflow_check(r))
    OUT.mkdir(parents=True, exist_ok=True)
    if cover_only or qa_only:
        if cover_only:
            cover(r, OUT / f"{rid}-cover.jpg", save, y)
        if qa_only:
            w = SCR / (rid + "-qa")
            ts = [0.0, 0.4, 1.0, 1.9, 2.6, 3.4, 4.5, 6.0, 7.2, 8.5, 9.7, 10.6, 11.6, 12.6, 13.6, 14.4]
            ts = [t for t in ts if t < r.duration]
            idx = sorted({min(int(t * 30), int(r.duration * 30) - 1) for t in ts})
            fdir, n = render_frames(r, w, dsf=1, only=idx)
            print("qa frames in", fdir)
        return r
    assert r.duration <= 15.0, r.duration
    w = SCR / rid
    fdir, n = render_frames(r, w, dsf=2)
    out = OUT / f"{rid}.mp4"
    encode(fdir, n, music, out, bpm=95)
    sheet(fdir, qa_times(r), SCR / f"{rid}-qa.jpg", cols=8, scale=0.2)
    cover(r, OUT / f"{rid}-cover.jpg", save, y)
    print(json.dumps(dict(id=rid, probe=probe(out), lufs=loudness(out), cuts=[round(c, 2) for c in r.cuts()])))
    shutil.rmtree(w, ignore_errors=True)
    return r


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--qa-only", action="store_true")
    ap.add_argument("--cover-only", action="store_true")
    a = ap.parse_args()
    for i in a.ids:
        build(i, a.qa_only, a.cover_only)

#!/usr/bin/env python3
"""Oct 25 studio build, Fully Funded Reels (Mon-Wed 7 pm). Imports the approved "Drawn to Scale" kit
(studio/recovery-oct22/fullyfunded/build/ff_reels.py) and the motion kit; nothing in them is rewritten.

  ff-reel-1026-cash-at-zero     Mon Oct 26 19:00  cost-of-waiting shape: $10,000 at 0% while prices rise 2% a year (central-bank target)
  ff-reel-1027-car-loan-send    Tue Oct 27 19:00  SEND TEST: "For the friend buying a car" -> 7-year loan costs $2,780 more interest
  ff-reel-1028-save-vs-card     Wed Oct 28 19:00  real-life gap question: savings at 2%, card at 20%

    python3 studio/editorial/oct25_fullyfunded.py <id> [--qa-only] [--cover-only]
Outputs: media/studio-oct25/fullyfunded/<id>.mp4 + <id>-cover.jpg. Frames go to the scratch dir and are deleted after each encode.
Every figure on screen is computed below (MATHS) and labelled; "Not guaranteed. Returns vary." lives in captions only.
"""
import argparse, json, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
SCR = Path("/tmp/claude-0/ff25")
sys.path.insert(0, str(REPO / "studio/recovery-oct22/fullyfunded/build"))

# This machine's Playwright Chromium lives in chrome-linux64/; the kits glob chrome-linux/. Shim glob (kits untouched).
import glob as _glob  # noqa: E402
_g0 = _glob.glob
_glob.glob = lambda pat, *a, **k: _g0(pat, *a, **k) or _g0(pat.replace("chrome-linux/", "chrome-linux64/"), *a, **k)

import ff_reels as FF  # noqa: E402  (puts studio/motion + studio/editorial on sys.path)
from ff_reels import Reel, el, words, stamp, svg, path, txt, dim, COB, INK, CORAL, SOFT, PAPER, CREAM, CSS  # noqa: E402
from kit import (reading_report, overflow_check, render_frames, encode, sheet, qa_times, probe, loudness,  # noqa: E402
                 FONTS, BASE_CSS)

OUT = REPO / "media/studio-oct25/fullyfunded"
MUSIC = REPO / "media/music/library/v4/ff-x-big-reveal.mp3"   # existing FF track (tools/music-library.json), 95.7 bpm
DCORAL = "#E04E28"
SUFFIX = "-r3"   # gate round 3 (Oct 25): new files, earlier renders stay as they are
CSSX = CSS + "svg *{transform-box:fill-box;transform-origin:center}"

# ------------------------------------------------------------------------------------------------ MATHS (all on-screen figures)
CASH, INFL, YEARS = 10_000, 0.02, 10
REAL = [CASH / (1 + INFL) ** k for k in range(YEARS + 1)]          # buying power, in today's dollars, year 0..10
assert round(REAL[-1]) == 8203

LOAN, APR = 30_000, 0.08


def interest(n):
    i = APR / 12
    pmt = LOAN * i / (1 - (1 + i) ** -n)
    return pmt, pmt * n - LOAN


PMT5, INT5 = interest(60)
PMT7, INT7 = interest(84)
EXTRA = INT7 - INT5
assert (round(INT5), round(INT7), round(EXTRA, -1), round(PMT5), round(PMT7)) == (6498, 9277, 2780, 608, 468)

BAL, SAVE_R, CARD_R = 1_000, 0.02, 0.20
EARN, COST = BAL * SAVE_R, BAL * CARD_R
assert (EARN, COST) == (20, 200)


def bgx(cls="sheet"):
    """Paper sheet without the inner frame (CD Oct 24: the frame wasted space)."""
    return f'<div class="par {cls}"></div>'


def do_this(y=300):
    return el('<span class="save" style="font-size:88px">do this:</span>', "c", y, a="pop", t=0.0, r=-3)


def timing(r, durs):
    for sc, d in zip(r.scenes, durs):
        sc["dur"] = d
    t = 0.0
    for sc in r.scenes:
        sc["start"] = round(t, 4)
        t += sc["dur"]
    r.t = t
    return r


# ============================================================================== 1. Cash at 0% (Mon Oct 26, 7 pm)
BX, BW = 110, 860                                   # $10,000 drawn as 860 px
BY, BH = 980, 230
xv = lambda v: BX + BW * v / CASH  # noqa: E731


def cash_bar(label=True):
    return "".join([
        f'<rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="10" fill="{COB}" stroke="{COB}" stroke-width="6"/>',
        txt(BX + 40, BY + 150, "$10,000", 100, "#FFFFFF", "start", 700) if label else "",
    ])


def cash():
    r = Reel("ff-reel-1026-cash-at-zero", "fullyfunded", bpm=95, css=CSSX, stage=PAPER)
    r.scene(4, "".join([
        bgx(), stamp(830, 200, 150, t=0.15),
        el('Your $10,000 earning<br><span class="em">0% interest?</span>', "c", 380, a="none", cls="H", style="font-size:90px;white-space:nowrap"),
        svg(cash_bar()),
    ]), cam="push", shake=(0.25, 0.22, 14))
    # payoff: the same bar loses one slice per year (each slice drawn to scale), leaving $8,203 of buying power
    slices = "".join(
        f'<rect x="{xv(REAL[k]):.1f}" y="{BY}" width="{xv(REAL[k - 1]) - xv(REAL[k]):.1f}" height="{BH}" fill="{CREAM}" '
        f'stroke="{CORAL}" stroke-width="3" data-a="fade" data-t="{0.5 + 0.17 * k:.2f}" data-d="0.12"/>' for k in range(1, YEARS + 1))
    hatch = "".join(
        path(f"M{x:.0f},{BY + BH - 8} L{x + 60:.0f},{BY + 8}", CORAL, 4, 2.3, 0.15)
        for x in range(int(xv(REAL[-1])) + 8, BX + BW - 50, 30))
    r.scene(10, "".join([
        bgx(),
        words("If prices rise 2% a year, / in 10 years it buys / what *$8,203* buys today.", "c", 330, t=0.0, gap=0.05, cls="H",
              style="font-size:92px"),
        # the $10,000 label stays on the bar until the slices are gone, then the bar is relabelled $8,203
        svg(cash_bar(label=True) + slices + hatch
            + f'<rect x="{BX + 20}" y="{BY + 40}" width="520" height="160" fill="{COB}" data-a="fade" data-t="2.35" data-d="0.1"/>'
            + txt(BX + 40, BY + 150, "$8,203", 100, "#FFFFFF", "start", 700, t=2.4)),
    ]), tin="whipL", cam="right", shake=(2.4, 0.2, 10))
    # do this: drawn phone, banking app, the savings-rate line gets circled
    x0, y0, w = 190, 820, 700
    ph = "".join([
        f'<rect x="{x0}" y="{y0}" width="{w}" height="760" rx="64" fill="{PAPER}" stroke="{COB}" stroke-width="9"/>',
        f'<rect x="{x0 + w / 2 - 80}" y="{y0 + 30}" width="160" height="18" rx="9" fill="rgba(43,63,224,.35)"/>',
        f'<rect x="{x0 + 60}" y="{y0 + 100}" width="230" height="24" rx="12" fill="rgba(43,63,224,.35)"/>',
        f'<rect x="{x0 + 60}" y="{y0 + 160}" width="{w - 120}" height="120" rx="20" fill="rgba(43,63,224,.12)"/>',
        f'<rect x="{x0 + 60}" y="{y0 + 310}" width="{w - 120}" height="150" rx="20" fill="#FFFFFF" stroke="{COB}" stroke-width="5"/>',
        txt(x0 + w / 2, y0 + 405, "Savings interest rate", 40, COB, "middle", 700),
        f'<ellipse cx="{x0 + w / 2}" cy="{y0 + 385}" rx="{w / 2 - 10}" ry="110" fill="none" stroke="{CORAL}" stroke-width="10" '
        f'data-a="draw" data-t="1.0" data-d="0.5"/>',
        f'<rect x="{x0 + 60}" y="{y0 + 490}" width="{w - 120}" height="120" rx="20" fill="rgba(43,63,224,.12)"/>',
    ])
    r.scene(8, "".join([
        bgx(), do_this(280),
        words("Under 2% interest? / Move it to / *high-interest savings.*", "c", 390, t=0.1, gap=0.07, cls="H", style="font-size:96px"),
        svg(ph), stamp(860, 150, 130, t=0.6),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    # no loop scene: the gate's longer "do this" line needs the time (Reel stays <= 15.0 s)
    return timing(r, (2.2, 7.2, 5.5))


# ============================================================================== 2. Car loan, SEND TEST (Tue Oct 27, 7 pm)
def car(x=230, y=1000, s=1.0, t=None):
    """Blueprint car, side view, drawn in line (no words)."""
    T = (lambda k: None) if t is None else (lambda k: t + k)  # noqa: E731
    X = lambda v: x + v * s  # noqa: E731
    Y = lambda v: y + v * s  # noqa: E731
    body = (f"M{X(0)},{Y(200)} L{X(0)},{Y(140)} Q{X(0)},{Y(110)} {X(40)},{Y(105)} L{X(150)},{Y(95)} L{X(230)},{Y(20)} "
            f"Q{X(250)},{Y(5)} {X(280)},{Y(5)} L{X(450)},{Y(5)} Q{X(480)},{Y(5)} {X(500)},{Y(25)} L{X(570)},{Y(100)} "
            f"L{X(610)},{Y(110)} Q{X(640)},{Y(120)} {X(640)},{Y(150)} L{X(640)},{Y(200)} Z")
    return "".join([
        f'<path d="{body}" fill="rgba(43,63,224,.10)" stroke="{COB}" stroke-width="9" stroke-linejoin="round"'
        + (f' data-a="draw" data-t="{T(0)}" data-d="0.5"' if t is not None else "") + "/>",
        path(f"M{X(250)},{Y(30)} L{X(345)},{Y(30)} L{X(345)},{Y(95)} L{X(175)},{Y(95)} Z", COB, 6, T(0.2), 0.3),
        path(f"M{X(370)},{Y(30)} L{X(470)},{Y(30)} L{X(530)},{Y(95)} L{X(370)},{Y(95)} Z", COB, 6, T(0.2), 0.3),
        f'<circle cx="{X(145)}" cy="{Y(205)}" r="{58 * s}" fill="{PAPER}" stroke="{INK}" stroke-width="10"/>',
        f'<circle cx="{X(495)}" cy="{Y(205)}" r="{58 * s}" fill="{PAPER}" stroke="{INK}" stroke-width="10"/>',
        f'<circle cx="{X(145)}" cy="{Y(205)}" r="{18 * s}" fill="{COB}"/>',
        f'<circle cx="{X(495)}" cy="{Y(205)}" r="{18 * s}" fill="{COB}"/>',
    ])


def car_loan():
    r = Reel("ff-reel-1027-car-loan-send", "fullyfunded", bpm=95, css=CSSX, stage=PAPER)
    r.scene(4, "".join([
        bgx(), stamp(830, 200, 150, t=0.15),
        el('For the friend<br><span class="em">buying a car</span>', "c", 380, a="none", cls="H", style="font-size:136px"),
        svg(car(236, 980, 0.95)),
    ]), cam="push", shake=(0.3, 0.2, 12))
    # payoff: total interest, drawn to scale (860 px = the 7-year loan's interest)
    x0, wmax = 110, 860
    w5, w7 = wmax * INT5 / INT7, wmax
    y5, y7 = 1010, 1230
    r.scene(10, "".join([
        bgx(),
        words("7 years instead of 5: / smaller monthly payment, / *$2,780 more interest.*", "c", 330, t=0.0, gap=0.05, cls="H", style="font-size:82px"),
        svg("".join([
            txt(540, 900, "TOTAL INTEREST · $30,000 LOAN AT 8%", 38, COB, weight=700, t=0.4),
            txt(x0, y5 - 20, "5 YEARS", 50, COB, "start", 700, t=0.6),
            f'<path d="M{x0},{y5 + 55} L{x0 + w5:.0f},{y5 + 55}" stroke="{COB}" stroke-width="110" fill="none" data-a="draw" data-t="0.65" data-d="0.5"/>',
            txt(x0 + w5 - 24, y5 + 75, f"${INT5:,.0f}", 58, "#FFFFFF", "end", 700, t=1.0),
            txt(x0, y7 - 20, "7 YEARS", 50, DCORAL, "start", 700, t=1.2),
            f'<path d="M{x0},{y7 + 55} L{x0 + w7:.0f},{y7 + 55}" stroke="{CORAL}" stroke-width="110" fill="none" data-a="draw" data-t="1.25" data-d="0.6"/>',
            f'<rect x="{x0 + w5:.0f}" y="{y5 - 10}" width="{w7 - w5:.0f}" height="{y7 + 120 - y5}" fill="rgba(255,106,61,.16)" '
            f'stroke="{DCORAL}" stroke-width="4" stroke-dasharray="14 10" data-a="fade" data-t="2.0" data-d="0.3"/>',
            txt(x0 + w7 - 24, y7 + 75, f"${INT7:,.0f}", 58, "#FFFFFF", "end", 700, t=1.8),
        ])),
    ]), tin="whipL", cam="right", shake=(2.0, 0.2, 10))
    r.scene(8, "".join([
        bgx(), do_this(280),
        words("Ask the lender: / *total interest,* / *in dollars?*", "c", 390, t=0.1, gap=0.07, cls="H", style="font-size:104px"),
        svg(car(236, 1060, 0.95)), stamp(860, 150, 130, t=0.6),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.scene(5, "".join([
        bgx(),
        el('Send this<br><span class="em">before they sign.</span>', "c", 400, a="pop", t=0.0, d=0.3, cls="H", style="font-size:128px"),
        svg('<g data-a="right" data-t="0.0" data-d="0.7">' + car(236, 820, 0.95) + "</g>"
            + path("M150,1120 L930,1120", COB, 6)),
        stamp(780, 1150, 170, t=0.3),
    ]), tin="slamup", cam="push")
    return timing(r, (1.9, 7.6, 3.4, 2.0))


# ============================================================================== 3. Savings at 2%, card at 20% (Wed Oct 28, 7 pm)
def scale_drawing():
    """A balance scale: the 20% card pan sits lower (it weighs more). Coordinates computed, no SVG rotate (kit CSS sets origins)."""
    lx, ly, rx, ry = 220, 912, 860, 1008                  # beam ends: pivot (540, 960), ~8.5 degrees down to the right

    def pan(x, y, lab, col, fill, bw, bh, fs):
        py = y + 170                                       # plate
        return (path(f"M{x},{y} L{x - 100},{py} M{x},{y} L{x + 100},{py}", col, 4)
                + path(f"M{x - 120},{py} L{x + 120},{py}", col, 9)
                + f'<rect x="{x - bw / 2}" y="{py - bh - 5}" width="{bw}" height="{bh}" rx="12" fill="{fill}" stroke="{col}" stroke-width="6"/>'
                + txt(x, py - 5 - bh / 2 + fs * 0.36, lab, fs, "#FFFFFF", weight=700))
    return "".join([
        path("M540,960 L540,1380", INK, 12), path("M420,1380 L660,1380", INK, 12),
        path(f"M{lx},{ly} L{rx},{ry}", COB, 12),
        f'<circle cx="540" cy="960" r="18" fill="{INK}"/>',
        pan(lx, ly, "2%", COB, COB, 92, 70, 40),
        pan(rx, ry, "20%", DCORAL, CORAL, 200, 150, 72),
    ])


def save_vs_card():
    r = Reel("ff-reel-1028-save-vs-card", "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    r.scene(4, "".join([
        bgx("sheetc"), stamp(830, 200, 150, t=0.15),
        el('Savings at 2%.<br><span class="em">Card at 20%?</span>', "c", 380, a="none", cls="H", style="font-size:136px"),
        svg(scale_drawing()),
    ]), cam="push", shake=(0.25, 0.22, 14))
    x0, wmax, y1, y2 = 110, 860, 1000, 1230
    r.scene(10, "".join([
        bgx("sheetc"),
        words("$1,000 saved earns *$20* a year. / $1,000 owed costs *$200.*", "c", 330, t=0.0, gap=0.09, cls="H", style="font-size:96px"),
        svg("".join([
            txt(x0, y1 - 22, "EARNS", 50, COB, "start", 700, t=0.5),
            f'<path d="M{x0},{y1 + 55} L{x0 + wmax * EARN / COST:.0f},{y1 + 55}" stroke="{COB}" stroke-width="110" fill="none" '
            f'data-a="draw" data-t="0.55" data-d="0.25"/>',
            txt(x0 + wmax * EARN / COST + 26, y1 + 74, "$20", 60, COB, "start", 700, t=0.8),
            txt(x0, y2 - 22, "COSTS", 50, DCORAL, "start", 700, t=1.4),
            f'<path d="M{x0},{y2 + 55} L{x0 + wmax:.0f},{y2 + 55}" stroke="{CORAL}" stroke-width="110" fill="none" '
            f'data-a="draw" data-t="1.45" data-d="0.8"/>',
            txt(x0 + wmax - 30, y2 + 74, "$200", 60, "#FFFFFF", "end", 700, t=2.2),
        ])),
    ]), tin="whipL", cam="left", shake=(2.25, 0.2, 10))
    ph = lambda x, lab, col: "".join([  # noqa: E731
        f'<rect x="{x}" y="900" width="340" height="520" rx="46" fill="{PAPER}" stroke="{COB}" stroke-width="8"/>',
        f'<rect x="{x + 120}" y="924" width="100" height="14" rx="7" fill="rgba(43,63,224,.35)"/>',
        txt(x + 170, 1130, lab, 54, col, weight=700),
        f'<rect x="{x + 40}" y="1300" width="260" height="70" rx="35" fill="rgba(43,63,224,.12)"/>',
    ])
    r.scene(8, "".join([
        bgx("sheetc"), do_this(280),
        words("Open both apps. / *Compare the* / *two rates.*", "c", 390, t=0.1, gap=0.08, cls="H", style="font-size:100px"),
        svg(f'<g data-a="left" data-t="0.4" data-d="0.4">{ph(150, "SAVINGS", COB)}</g>'
            f'<g data-a="right" data-t="0.6" data-d="0.4">{ph(590, "CARD", DCORAL)}</g>'),
        stamp(860, 150, 130, t=0.6),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.loop(1.0, tin="zoom")
    return timing(r, (2.6, 6.2, 5.0, 0.7))


REELS = {
    "ff-reel-1026-cash-at-zero": (cash, "check your savings interest rate tonight", 1540),
    "ff-reel-1027-car-loan-send": (car_loan, "send this before they sign", 1330),
    "ff-reel-1028-save-vs-card": (save_vs_card, "check both rates tonight", 1450),
}


def cover(r, out, save, y):
    """Dedicated cover (same method as ff_reels.cover): hook scene settled + handwritten save-line, rendered at 2x."""
    from playwright.sync_api import sync_playwright
    from PIL import Image
    import io
    s0 = r.scenes[0]
    html = (s0["html"].replace('data-a="stamp"', 'data-a="none"').replace('data-a="pop"', 'data-a="none"')
            .replace('data-a="draw"', 'data-a="none"'))
    # cover rule: hook >= 120 px. The Reel keeps the 2-line 104 px hook; the cover sets it at 128 px on 3 lines.
    html = html.replace('Your $10,000 earning<br><span class="em">0% interest?</span>',
                        'Your $10,000<br>earning<br><span class="em">0% interest?</span>').replace(
                        "font-size:90px;white-space:nowrap", "font-size:128px;white-space:nowrap;line-height:1.2").replace("top:380px", "top:385px", 1)
    html += el(f'<span class="save" style="font-size:64px">{save}</span>', "c", y, a="none", r=-2)
    page = (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}{BASE_CSS}{r.css}"
            f".el{{position:absolute}}</style></head><body><div class='scene' style='display:block;background:{s0['bg']}'>"
            f"<div class='cam'>{html}</div></div></body></html>")
    SCR.mkdir(parents=True, exist_ok=True)
    tmp = SCR / f"{Path(out).stem}.html"
    tmp.write_text(page)
    chrome = _glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")[0]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chrome, args=["--disable-gpu", "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=2)
        pg.goto(tmp.as_uri())
        pg.wait_for_timeout(700)
        im = Image.open(io.BytesIO(pg.screenshot(type="png"))).convert("RGB").resize((1080, 1920), Image.LANCZOS)
        im.save(out, quality=92, subsampling=0)
        b.close()
    tmp.unlink()


def build(rid, qa_only=False, cover_only=False):
    fn, save, y = REELS[rid]
    r = fn()
    rep = reading_report(r)
    print(json.dumps(rep))
    print("duration", round(r.duration, 2), "overflow", overflow_check(r))
    OUT.mkdir(parents=True, exist_ok=True)
    if cover_only or qa_only:
        if cover_only:
            cover(r, OUT / f"{rid}{SUFFIX}-cover.jpg", save, y)
        return r
    assert r.duration <= 15.0, r.duration
    w = SCR / rid
    fdir, n = render_frames(r, w, dsf=2)
    out = OUT / f"{rid}{SUFFIX}.mp4"
    encode(fdir, n, MUSIC, out, bpm=95)
    sheet(fdir, qa_times(r), SCR / f"{rid}-qa.jpg", cols=8, scale=0.2)
    cover(r, OUT / f"{rid}{SUFFIX}-cover.jpg", save, y)
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

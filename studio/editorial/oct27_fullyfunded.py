#!/usr/bin/env python3
"""Oct 27 studio build, Fully Funded Reels (no trial flag). Desk order 5: open on a TRAP WITH A DATE / a consequence stated as a fact,
the trap DRAWN HAPPENING by second 2 (the LF burp lesson: draw the thing being done). Imports the FF kit
(studio/recovery-oct22/fullyfunded/build/ff_reels.py) and the motion kit; nothing in them is rewritten.

  ff-reel-1028am-promo-end-date   Wed Oct 28 08:15  US & CANADA. "No interest if paid in full in 12 months": miss the end date and
                                                    interest can be charged back to the day you bought it (CFPB; FCAC).
                                                    Body: drawn offer card + tear-off calendar flipping MONTH 1 -> 12, INTEREST FROM DAY 1 stamp.
                                                    Cover: BIG-NUMBER tile on cobalt (style 8, quiet).
  ff-reel-1030-late-payment       Fri Oct 30 19:00  CANADA & US. A late card payment can stay on your credit report up to 6 years in Canada
                                                    (FCAC, Equifax Canada) and 7 in the US (CFPB): late this month -> until 2032 (CA) / 2033 (US). Reported once 30+ days past due.
                                                    Body: drawn credit report, LATE stamp slams on the October row, year ticks 2026 -> 2032.
                                                    Cover: Look B big-headline editorial (style 1): drawn report + LATE stamp.

    python3 studio/editorial/oct27_fullyfunded.py <id> [--qa-only] [--cover-only]  < /dev/null
Outputs: media/studio-oct27/fullyfunded/<id>.mp4 + <id>-cover.jpg. Frames go to the scratch dir and are deleted after each encode.
"""
import argparse, io, json, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
SCR = Path("/tmp/claude-0/oct27-fullyfunded")
sys.path.insert(0, str(REPO / "studio/recovery-oct22/fullyfunded/build"))

import glob as _glob  # noqa: E402
_g0 = _glob.glob
_glob.glob = lambda pat, *a, **k: _g0(pat, *a, **k) or _g0(pat.replace("chrome-linux/", "chrome-linux64/"), *a, **k)

import ff_reels as FF  # noqa: E402,F401
from ff_reels import Reel, el, words, stamp, svg, path, txt, COB, INK, CORAL, SOFT, PAPER, CREAM, CSS  # noqa: E402
from kit import (reading_report, overflow_check, render_frames, encode, sheet, qa_times, probe, loudness,  # noqa: E402
                 FONTS, BASE_CSS)

OUT = REPO / "media/studio-oct27/fullyfunded"
DCORAL = "#E04E28"
GREEN = "#1F8A5B"
CSSX = CSS + "svg *{transform-box:fill-box;transform-origin:center}" + f"""
.dotsb{{background:radial-gradient(rgba(43,63,224,.13) 2px,transparent 2.4px) 0 0/34px 34px,#F3F5FF}}
.dots{{background:radial-gradient(rgba(43,63,224,.14) 2px,transparent 2.4px) 0 0/36px 36px,{CREAM}}}
.tag{{font-family:'DejaVu Sans Mono';font-weight:700;font-size:36px;letter-spacing:.12em;color:#fff;background:{COB};
      border-radius:999px;padding:12px 30px;display:inline-block}}
.K{{font-family:'Inter Display';font-weight:800;letter-spacing:-.045em;line-height:.9;color:{COB}}}
.H .w{{margin-right:.04em}}
.stampx{{font-family:'Inter Display';font-weight:800;letter-spacing:.01em;color:{DCORAL};border:10px solid {DCORAL};border-radius:22px;
        padding:10px 30px 14px;background:#FFFFFF;display:inline-block;line-height:1}}
"""

# ------------------------------------------------------------------------------------------------ MATHS (on-screen figures)
# Reel 1: the CFPB's own worked numbers (consumerfinance.gov, "How to understand special promotional financing offers").
TV, PER_MONTH, MONTHS, CFPB_INTEREST = 400, 25, 12, 65
PAID = PER_MONTH * MONTHS                  # 300
LEFT = TV - PAID                           # 100
OWE = LEFT + CFPB_INTEREST                 # 165 (CFPB: "you will owe $165")
SPLIT = TV / MONTHS                        # 33.33 -> "about $34 a month" clears it (rounded up)
assert (PAID, LEFT, OWE) == (300, 100, 165) and 33 < SPLIT < 34
# Reel 2: late in Oct 2026 -> Canada up to 6 years (FCAC "up to 6 years"; Equifax Canada "6 years from the date reported"),
# US 7 years (CFPB "most negative information for seven years").
YEAR, CA_YEARS, US_YEARS = 2026, 6, 7
CA_UNTIL, US_UNTIL = YEAR + CA_YEARS, YEAR + US_YEARS
assert (CA_UNTIL, US_UNTIL) == (2032, 2033)


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


FOLLOW = "Follow for one money rule a day, in plain words."


def follow(y, t=0.9, size=70):
    return el(f'<span class="save" style="font-size:{size}px;line-height:1.1">Follow for one money rule a day,<br>in plain words.</span>',
              "c", y, a="pop", t=t, r=-2)


# ============================================================================== 1. 0% promo end date (Wed Oct 28, 8:15 am)
def offer_card(x=150, y=700, w=780, h=250):
    """The store's offer, drawn as a shelf tag: 'NO INTEREST if paid in full in 12 months'."""
    return (f'<rect x="{x + 10}" y="{y + 12}" width="{w}" height="{h}" rx="26" fill="{INK}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="70" rx="26" fill="{COB}" stroke="{INK}" stroke-width="6"/>'
            f'<rect x="{x + 3}" y="{y + 40}" width="{w - 6}" height="30" fill="{COB}"/>'
            + txt(x + w / 2, y + 48, "STORE CARD OFFER", 34, "#FFFFFF", weight=700)
            + f'<text x="{x + w / 2}" y="{y + 160}" font-size="92" fill="{INK}" text-anchor="middle" '
              f'style="font-family:Inter Display" font-weight="800" letter-spacing="-2">NO INTEREST</text>'
            + txt(x + w / 2, y + 220, "IF PAID IN FULL IN 12 MONTHS", 36, INK, weight=700))


def cal_page(k, x=360, y=1010, w=360, t=None, last=False):
    """One tear-off calendar page: MONTH k. With t, it drops onto the stack (pages flipping)."""
    a = f' data-a="down" data-t="{t:.2f}" data-d="0.11"' if t is not None else ""
    head = DCORAL if last else COB
    lab = "LAST MONTH" if last else "MONTH"
    return (f'<g{a}><rect x="{x}" y="{y}" width="{w}" height="{w * 0.86:.0f}" rx="28" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{w * 0.25:.0f}" rx="28" fill="{head}" stroke="{INK}" stroke-width="7"/>'
            f'<rect x="{x + 4}" y="{y + w * 0.15:.0f}" width="{w - 8}" height="{w * 0.1:.0f}" fill="{head}"/>'
            + txt(x + w / 2, y + w * 0.18, lab, w * 0.11, "#FFFFFF", weight=700)
            + f'<text x="{x + w / 2}" y="{y + w * 0.74:.0f}" font-size="{w * 0.44:.0f}" fill="{INK}" text-anchor="middle" '
              f'style="font-family:Inter Display" font-weight="800">{k}</text></g>')


def cal_stack(t0=None, x=360, y=1010, w=360):
    rings = "".join(f'<rect x="{x + w * f - 11}" y="{y - 24}" width="22" height="56" rx="11" fill="{INK}"/>' for f in (0.28, 0.72))
    pages = cal_page(1, x, y, w)
    if t0 is not None:
        pages += "".join(cal_page(k, x, y, w, t=t0 + 0.11 * (k - 2), last=(k == 12)) for k in range(2, 13))
    else:
        pages = cal_page(12, x, y, w, last=True)
    return pages + rings


def promo():
    r = Reel("ff-reel-1028am-promo-end-date", "fullyfunded", bpm=95, css=CSSX, stage="#F3F5FF")
    # frame 0: the trap as a question with its date; by 1.6 s the 12 months have flipped and the consequence stamp lands
    r.scene(4, "".join([
        '<div class="par dotsb"></div>', stamp(860, 170, 130, t=0.2),
        el('<span class="tag">US &amp; CANADA · STORE CARDS</span>', "c", 300, a="none"),
        el('Miss the<br><span class="em">“no interest”</span><br>end date?', "c", 380, a="none", cls="H", style="font-size:112px"),
        svg(offer_card(x=110, y=790, w=860, h=280) + cal_stack(t0=0.12, x=320, y=1150, w=440)),
        el('<span class="stampx" style="font-size:64px">INTEREST FROM DAY 1</span>', "c", 880, a="stamp", t=1.45, d=0.3, r=-7),
    ]), cam="push", shake=(1.5, 0.22, 16))
    # payoff: timeline DAY 1 -> MONTH 12; a coral arrow swings back to day 1 and the whole span turns coral
    X0, X1, Y = 130, 930, 1330
    ticks = "".join(path(f"M{X0 + (X1 - X0) * i / 12:.0f},{Y - 22} L{X0 + (X1 - X0) * i / 12:.0f},{Y + 22}", INK, 6) for i in range(13))
    tl = (path(f"M{X0},{Y} L{X1},{Y}", INK, 10) + ticks
          + txt(X0, Y + 90, "DAY 1", 50, INK, "start", 700) + txt(X1, Y + 90, "MONTH 12", 50, DCORAL, "end", 700)
          + txt(X0, Y - 200, "BOUGHT", 44, COB, "start", 700)
          + f'<rect x="{X0}" y="{Y - 172}" width="210" height="132" rx="12" fill="{INK}"/>'
          + f'<rect x="{X0 + 12}" y="{Y - 160}" width="186" height="100" rx="8" fill="{SOFT}"/>'
          + path(f"M{X0 + 105},{Y - 40} L{X0 + 105},{Y - 12}", INK, 10)
          + path(f"M{X1},{Y - 34} C{X1 - 120},{Y - 420} {X0 + 360},{Y - 420} {X0 + 230},{Y - 120}", DCORAL, 14, 0.55, 0.55)
          + path(f"M{X0 + 206},{Y - 166} L{X0 + 228},{Y - 114} L{X0 + 282},{Y - 136}", DCORAL, 14, 1.05, 0.15)
          + f'<path d="M{X0},{Y} L{X1},{Y}" stroke="{CORAL}" stroke-width="48" stroke-linecap="round" fill="none" opacity=".85" '
            f'data-a="draw" data-t="1.25" data-d="0.6"/>'
          + txt((X0 + X1) / 2, Y + 170, "INTEREST CHARGED FOR ALL 12 MONTHS", 38, DCORAL, weight=700, t=1.7))
    r.scene(6, "".join([
        '<div class="par dotsb"></div>',
        words("Not paid off by then? / Interest can go back / *to the day you bought it.*", "c", 320, t=0.0, gap=0.06, cls="H",
              style="font-size:96px"),
        svg(tl),
    ]), tin="whipL", td=0.2, cam="right")
    # the cost on a cobalt surface, drawn to scale (760 px = $400): the CFPB's own numbers
    W, x0 = 760, 160
    s = W / TV
    yb1, yb2, bh = 960, 1260, 150
    WH = "#FFFFFF"
    bars = "".join([
        txt(x0, yb1 - 34, f"PAID ${PER_MONTH} A MONTH x 12 = ${PAID}", 44, WH, "start", 700, t=0.15),
        f'<rect x="{x0}" y="{yb1}" width="{PAID * s:.0f}" height="{bh}" rx="14" fill="{WH}" data-a="fade" data-t="0.2" data-d="0.3"/>',
        f'<rect x="{x0 + PAID * s + 6:.0f}" y="{yb1}" width="{LEFT * s - 6:.0f}" height="{bh}" rx="14" fill="{SOFT}" stroke="{CORAL}" '
        f'stroke-width="6" stroke-dasharray="16 10" data-a="pop" data-t="0.55" data-d="0.3"/>',
        txt(x0 + PAID * s / 2, yb1 + 95, "PAID", 52, COB, weight=700, t=0.3),
        txt(x0 + PAID * s + LEFT * s / 2 + 3, yb1 + 95, f"${LEFT}", 52, INK, weight=700, t=0.6),
        txt(x0 + PAID * s + LEFT * s / 2 + 3, yb1 + bh + 56, "LEFT", 40, SOFT, weight=700, t=0.6),
        txt(x0, yb2 - 34, "YOU OWE AFTER MONTH 12", 44, SOFT, "start", 700, t=0.9),
        f'<rect x="{x0}" y="{yb2}" width="{LEFT * s:.0f}" height="{bh}" rx="14" fill="{SOFT}" data-a="fade" data-t="0.95" data-d="0.2"/>',
        f'<rect x="{x0 + LEFT * s + 6:.0f}" y="{yb2}" width="{CFPB_INTEREST * s:.0f}" height="{bh}" rx="14" fill="{CORAL}" '
        f'data-a="pop" data-t="1.15" data-d="0.3"/>',
        txt(x0 + LEFT * s / 2, yb2 + 95, f"${LEFT}", 52, INK, weight=700, t=1.0),
        txt(x0 + LEFT * s + 6 + CFPB_INTEREST * s / 2, yb2 + 95, f"+${CFPB_INTEREST}", 48, WH, weight=700, t=1.2),
        txt(x0 + (LEFT + CFPB_INTEREST) * s + 40, yb2 + 62, "INTEREST", 42, WH, "start", 700, t=1.25),
        txt(x0 + (LEFT + CFPB_INTEREST) * s + 40, yb2 + 112, "BACK TO DAY 1", 42, WH, "start", 700, t=1.25),
    ])
    r.scene(6, "".join([
        '<div class="par" style="background:radial-gradient(rgba(255,255,255,.10) 2px,transparent 2.4px) 0 0/34px 34px,#2B3FE0"></div>',
        el('<span class="M" style="font-size:36px;color:#FFFFFF">THE CFPB’S NUMBERS: $400 TV · 25% RATE</span>', "c", 300, a="none"),
        el(f'$100 left at the end?<br>You owe <span class="em" style="color:{INK}">${OWE}.</span>', "c", 380, a="none", cls="H",
           style="font-size:98px;color:#FFFFFF;white-space:nowrap"),
        svg(bars),
    ]), tin="cut", cam="push", bg=COB, shake=(0.0, 0.2, 14))
    # do this: names the action and the math
    r.scene(7, "".join([
        '<div class="par dotsb"></div>', do_this(280),
        words("Divide the price / by the months. / *Pay at least that.*", "c", 400, t=0.1, gap=0.06, cls="H", style="font-size:104px"),
        el(f'<div style="display:inline-block;background:#fff;border:7px solid {INK};border-radius:28px;box-shadow:12px 12px 0 {INK};'
           f'padding:30px 54px"><span class="M" style="font-size:36px;color:#141A55;display:block">MATH</span>'
           f'<span class="K" style="font-size:104px;white-space:nowrap;color:{INK}">$400 ÷ 12 ≈ <span style="color:{COB}">$34</span></span>'
           f'<span class="M" style="font-size:36px;color:#141A55;display:block;margin-top:12px">A MONTH, EVERY MONTH</span></div>',
           "c", 800, a="pop", t=0.5),
        follow(1250, t=0.8, size=76),
        stamp(860, 1420, 120, t=0.6),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.loop(1.0, tin="cut")
    return timing(r, (2.4, 3.7, 3.9, 4.5, 0.4))


# ============================================================================== 2. late payment (Fri Oct 30, 7 pm)
def report_sheet(x=140, y=690, w=800, row_h=96, big=1.0):
    rows = ["JUL", "AUG", "SEP", "OCT"]
    H = 110 + row_h * 4 + 30
    out = [f'<rect x="{x + 12}" y="{y + 14}" width="{w}" height="{H}" rx="24" fill="{INK}"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{H}" rx="24" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="96" rx="24" fill="{COB}" stroke="{INK}" stroke-width="6"/>',
           f'<rect x="{x + 3}" y="{y + 60}" width="{w - 6}" height="36" fill="{COB}"/>',
           txt(x + w / 2, y + 64, "YOUR CREDIT REPORT", 44 * big, "#FFFFFF", weight=700)]
    for i, m in enumerate(rows):
        yy = y + 120 + row_h * i
        out.append(path(f"M{x + 30},{yy + row_h - 6} L{x + w - 30},{yy + row_h - 6}", "rgba(20,26,85,.18)", 3))
        out.append(txt(x + 50, yy + row_h * 0.62, m, 48 * big, INK, "start", 700))
        if i < 3:
            out.append(f'<rect x="{x + 210}" y="{yy + row_h * 0.3:.0f}" width="{w * 0.28:.0f}" height="24" rx="12" fill="rgba(20,26,85,.14)"/>')
            out.append(txt(x + w - 50, yy + row_h * 0.62, "ON TIME ✓", 42 * big, GREEN, "end", 700))
    return "".join(out)


def latepay():
    r = Reel("ff-reel-1030-late-payment", "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    LATE = '<span class="stampx" style="font-size:104px">LATE</span>'
    # frame 0: the moment + the drawn report; by 0.6 s LATE slams on October, by 1.8 s the year has ticked to 2032
    r.scene(4, "".join([
        '<div class="par dots"></div>', stamp(860, 170, 130, t=0.2),
        el('<span class="tag">CANADA · US</span>', "c", 300, a="none"),
        el('Card bill<br><span class="em">30 days late?</span>', "c", 380, a="none", cls="H", style="font-size:124px"),
        svg(report_sheet(y=690)),
        el(LATE, 590, 1088, a="stamp", t=0.45, d=0.3, r=-8),
        el('<span class="M" style="font-size:40px;color:#141A55">CAN STAY ON IT UNTIL</span>', "c", 1262, a="fade", t=0.75),
        el(f'<span class="K" data-a="tick" data-t="0.85" data-d="0.9" data-from="{YEAR}" data-to="{CA_UNTIL}" '
           f'style="font-size:210px;color:{DCORAL}">{CA_UNTIL}</span>', "c", 1310, a="pop", t=0.75, d=0.25),
        el(f'<span class="M" style="font-size:36px;color:#141A55">IN CANADA · {US_UNTIL} IN THE US</span>', "c", 1505, a="fade", t=1.6),
    ]), cam="push", shake=(0.5, 0.2, 14))
    # payoff: drawn to scale, 760 px = 7 years
    W, x0 = 760, 140
    per = W / US_YEARS
    yb1, yb2, bh = 1000, 1300, 130
    yrs = "".join(path(f"M{x0 + per * i:.0f},{yb1 + bh + 14} L{x0 + per * i:.0f},{yb1 + bh + 38}", INK, 5) for i in range(CA_YEARS + 1))
    bars = "".join([
        txt(x0, yb1 - 34, f"CANADA · UP TO {CA_YEARS} YEARS", 46, COB, "start", 700, t=0.4),
        f'<path d="M{x0},{yb1 + bh / 2} L{x0 + per * CA_YEARS:.0f},{yb1 + bh / 2}" stroke="{COB}" stroke-width="{bh}" fill="none" '
        f'data-a="draw" data-t="0.45" data-d="0.6"/>',
        txt(x0 + per * CA_YEARS - 28, yb1 + 86, f"→ {CA_UNTIL}", 62, "#FFFFFF", "end", 700, t=1.0), yrs,
        txt(x0, yb2 - 34, f"US · {US_YEARS} YEARS", 46, DCORAL, "start", 700, t=1.1),
        f'<path d="M{x0},{yb2 + bh / 2} L{x0 + per * US_YEARS:.0f},{yb2 + bh / 2}" stroke="{CORAL}" stroke-width="{bh}" fill="none" '
        f'data-a="draw" data-t="1.15" data-d="0.6"/>',
        txt(x0 + per * US_YEARS - 28, yb2 + 86, f"→ {US_UNTIL}", 62, "#FFFFFF", "end", 700, t=1.7),
    ])
    r.scene(6, "".join([
        '<div class="par dots"></div>',
        words("One late payment / can stay on your / credit report / *for&nbsp;years.*", "c", 310, t=0.0, gap=0.06, cls="H",
              style="font-size:96px;white-space:nowrap"),
        svg(bars),
    ]), tin="whipL", td=0.2, cam="right")
    # the catch: paying it later doesn't erase it (the report row with LATE stays; PAID lands beside it)
    r.scene(5, "".join([
        '<div class="par dots"></div>',
        el('Paying it later<br><span class="em">doesn’t erase it.</span>', "c", 320, a="none", cls="H", style="font-size:116px"),
        svg(report_sheet(y=640, row_h=110)),
        el(LATE, 590, 1100, a="none", r=-8),
        el(f'<span class="stampx" style="font-size:76px;color:{COB};border-color:{COB}">PAID</span>', 330, 1112, a="stamp", t=0.5, d=0.3, r=6),
        el('<span class="save" style="font-size:76px">the LATE mark stays</span>', "c", 1300, a="pop", t=1.0, r=-2),
    ]), tin="cut", cam="push", shake=(0.55, 0.2, 12))
    r.scene(7, "".join([
        '<div class="par dots"></div>', do_this(280),
        words("Turn on autopay / for at least / *the minimum payment.*", "c", 400, t=0.1, gap=0.06, cls="H", style="font-size:94px;white-space:nowrap"),
        el('<span class="M" style="font-size:38px;color:#141A55">IN YOUR CARD’S APP OR ONLINE BANKING</span>', "c", 780, a="fade", t=0.5),
        el(f'<div style="display:inline-flex;align-items:center;gap:36px;background:#fff;border:7px solid {INK};border-radius:999px;'
           f'box-shadow:12px 12px 0 {INK};padding:28px 50px"><span class="K" style="font-size:96px;color:{INK}">AUTOPAY</span>'
           f'<span style="display:inline-block;width:190px;height:100px;border-radius:50px;background:{COB};position:relative">'
           f'<span style="position:absolute;right:10px;top:10px;width:80px;height:80px;border-radius:50%;background:#fff"></span></span></div>',
           "c", 870, a="pop", t=0.55),
        follow(1250, t=0.85, size=76),
        stamp(860, 1420, 120, t=0.6),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.loop(1.0, tin="cut")
    return timing(r, (2.5, 3.8, 3.3, 4.7, 0.4))


# ============================================================================== dedicated covers (style-menu layouts, 2x render)
def cover_bignum():
    """Big-number tile (style 8 'big-number', quiet) on a cobalt field: the labelled CFPB numbers are the hero."""
    return ('<div style="position:absolute;inset:0;background:radial-gradient(rgba(255,255,255,.10) 2px,transparent 2.4px) 0 0/34px 34px,#2B3FE0"></div>'
            '<div class="M" style="position:absolute;left:0;width:1080px;text-align:center;top:310px;font-size:36px;color:#FFFFFF">'
            'STORE CARD “NO INTEREST” DEALS</div>'
            f'<div class="H" style="position:absolute;left:90px;right:90px;top:380px;text-align:center;font-size:124px;color:#FFFFFF">'
            f'Miss the<br><span class="em" style="color:{INK}">end date?</span></div>'
            '<div style="position:absolute;left:0;width:1080px;top:690px;text-align:center">'
            f'<div class="K" style="font-size:120px;color:{SOFT}">$100 left</div>'
            '<div class="K" style="font-size:90px;color:#FFFFFF;margin:14px 0">↓</div>'
            f'<div class="K" style="font-size:120px;color:#FFFFFF">you owe <span style="color:{CORAL}">$165</span></div></div>'
            '<div class="M" style="position:absolute;left:0;width:1080px;text-align:center;top:1110px;font-size:32px;color:#FFFFFF">'
            'THE CFPB’S NUMBERS · $400 TV · 25% RATE</div>'
            f'<div style="position:absolute;left:100px;top:1200px;font-family:\'Caveat Brush\';font-size:80px;color:{SOFT};transform:rotate(-3deg)">'
            'pay price ÷ months</div>'
            + stamp(830, 1210, 150))


def cover_report():
    """Big-headline editorial cover (serif + pill + drawn report object with LATE stamp + handwritten line + stamp)."""
    return ('<div class="par dots" style="position:absolute;inset:0"></div>'
            f'<div class="H" style="position:absolute;left:80px;right:80px;top:300px;text-align:center;font-size:128px">'
            f'<span class="em">30 days late?</span></div>'
            f'<div class="H" style="position:absolute;left:80px;right:80px;top:450px;text-align:center;font-size:104px">'
            f'It can stay<br>6–7 years.</div>'
            + svg(f'<g transform="rotate(-3 540 950)">{report_sheet(x=190, y=720, w=700, row_h=80)}</g>')
            + el('<span class="stampx" style="font-size:96px">LATE</span>', 560, 1080, a="none", r=-10)
            + f'<div class="M" style="position:absolute;left:0;width:1080px;text-align:center;top:1240px;font-size:34px;color:{INK}">'
              'CANADA: UP TO 6 YEARS · US: 7 YEARS</div>'
            + f'<div style="position:absolute;left:100px;top:1295px;font-family:\'Caveat Brush\';font-size:76px;color:{DCORAL};transform:rotate(-3deg)">'
              'set autopay tonight</div>'
            + stamp(860, 1300, 130))


COVERS = {"ff-reel-1028am-promo-end-date": cover_bignum, "ff-reel-1030-late-payment": cover_report}
REELS = {
    "ff-reel-1028am-promo-end-date": (promo, REPO / "media/music/library/v4/ff-x-money-moves.mp3"),
    "ff-reel-1030-late-payment": (latepay, REPO / "media/music/library/v4/ff-x-big-reveal.mp3"),
}


def cover(r, rid, out):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    html = COVERS[rid]()
    page = (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}{BASE_CSS}{r.css}"
            f".el{{position:absolute}}.par{{position:absolute;inset:0}}</style></head><body><div class='scene' style='display:block'>"
            f"{html}</div></body></html>")
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
    fn, music = REELS[rid]
    r = fn()
    print(json.dumps(reading_report(r)))
    print("duration", round(r.duration, 2), "overflow", overflow_check(r))
    OUT.mkdir(parents=True, exist_ok=True)
    if cover_only or qa_only:
        if cover_only:
            cover(r, rid, OUT / f"{rid}-cover.jpg")
        if qa_only:
            w = SCR / (rid + "-qa")
            ts = [0.0, 0.3, 0.7, 1.0, 1.4, 1.8, 2.2, 2.7, 3.2, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 14.6]
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
    cover(r, rid, OUT / f"{rid}-cover.jpg")
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

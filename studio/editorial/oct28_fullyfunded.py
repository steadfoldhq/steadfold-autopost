#!/usr/bin/env python3
"""Oct 28 studio build, Fully Funded Reels (no trial flag). Desk order: open on a TRAP WITH A DATE or LEGAL STAKES, stated in frame 0
in plain words, with ONE drawn object doing the meaning (no pointing hand, no piggy bank, no table). Imports the FF kit
(studio/recovery-oct22/fullyfunded/build/ff_reels.py) and the motion kit; nothing in them is rewritten.

  ff-reel-1029am-refund-deadline  Thu Oct 29 08:15  US. Never filed your 2023 taxes? If tax came out of your pay, you usually have 3 years
                                                    to file and claim the refund; for 2023 that ends April 15, 2027, then the money becomes
                                                    the U.S. Treasury's (IRS IR-2026-37; IRS 'Time you can claim a credit or refund').
                                                    Body: a drawn refund cheque, PAY TO: YOU is struck and re-stamped U.S. TREASURY.
                                                    Cover: style 8 'compare' tile (quiet): two cheque stubs, before / after the date.
  ff-reel-1031-cosign             Sat Oct 31 19:00  CANADA & US. Co-sign a loan and you are legally responsible for all of it if they stop
                                                    paying (FTC Notice to Cosigner; CFPB; FCAC). Body: a drawn loan agreement, you sign,
                                                    the bill for the FULL BALANCE lands addressed to you. On-screen send beat.
                                                    Cover: Ep.01 reframe 'Instead of... Say...' (style 7, quiet).

    python3 studio/editorial/oct28_fullyfunded.py <id> [--qa-only] [--cover-only]  < /dev/null
Outputs: media/studio-oct28/fullyfunded/<id>.mp4 + <id>-cover.jpg. Frames go to the scratch dir and are deleted after each encode.
"""
import argparse, io, json, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
SCR = Path("/tmp/claude-0/oct28-fullyfunded")
sys.path.insert(0, str(REPO / "studio/recovery-oct22/fullyfunded/build"))

import glob as _glob  # noqa: E402
_g0 = _glob.glob
_glob.glob = lambda pat, *a, **k: _g0(pat, *a, **k) or _g0(pat.replace("chrome-linux/", "chrome-linux64/"), *a, **k)

import ff_reels as FF  # noqa: E402,F401
from ff_reels import Reel, el, words, stamp, svg, path, txt, COB, INK, CORAL, SOFT, PAPER, CREAM, CSS  # noqa: E402
from kit import (reading_report, overflow_check, render_frames, encode, sheet, qa_times, probe, loudness,  # noqa: E402
                 FONTS, BASE_CSS)

OUT = REPO / "media/studio-oct28/fullyfunded"
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
.Ins{{font-family:'Instrument Serif';color:{INK};letter-spacing:-.02em;line-height:1}}
.HL{{line-height:1.24}}
.HL .em{{padding:0 .14em;border-radius:.24em}}
"""

# ------------------------------------------------------------------------------------------------ FACTS / MATHS (on-screen figures)
# Reel 1 (IRS): "taxpayers usually have three years to file and claim their tax refunds. If they do not file within three years, the money
# becomes the property of the U.S. Treasury" (IR-2026-37, Mar 20 2026: tax year 2022 -> deadline April 15, 2026).
# "If you filed your return before its due date, the IRS considers it filed on the due date"; withholding counts as paid on the due date.
TAX_YEAR, DUE_YEAR, WINDOW = 2023, 2024, 3
LAST_YEAR = DUE_YEAR + WINDOW
assert LAST_YEAR == 2027                       # 2023 return was due April 15, 2024 -> claim window ends April 15, 2027
IRS_2022_PEOPLE, IRS_2022_MEDIAN = "1.3 million", 686   # IR-2026-37: "over 1.3 million people", "median refund amount is $686 for 2022"


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


def follow(y, t=0.9, size=74):
    return el(f'<span class="save" style="font-size:{size}px;line-height:1.1">Follow for one money rule a day,<br>in plain words.</span>',
              "c", y, a="pop", t=t, r=-2)


# ============================================================================== shared: line-by-line kinetic text (gate r2)
# The kit's words() scales each word up from 0.4, so mid-build words run together ("Onlyco-signwhat"). lines() lifts whole lines
# instead (no scale), and a looser line-height + pill padding keeps a pill from covering the descenders of the line above.
def md(s):
    import re as _re
    return _re.sub(r"\*(.+?)\*", r'<span class="em">\1</span>', s)


def lines(text, y, t=0.0, gap=0.14, size=100, color=None, style=""):
    parts = [p.strip() for p in text.split(" / ")]
    inner = "<br>".join(f'<span style="display:inline-block" data-a="up" data-t="{t + gap * i:.2f}" data-d="0.3">{md(p)}</span>'
                        for i, p in enumerate(parts))
    col = f"color:{color};" if color else ""
    return el(inner, "c", y, a="none", cls="H HL", style=f"font-size:{size}px;white-space:nowrap;{col}{style}")


def still(text, y, size=110, style=""):
    return el(md(text.replace(" / ", "<br>")), "c", y, a="none", cls="H HL", style=f"font-size:{size}px;white-space:nowrap;{style}")


# ============================================================================== 1. 2023 refund deadline (Thu Oct 29, 8:15 am)
def cheque(x=90, y=690, w=900, h=470, payee_t=None):
    """A drawn IRS refund cheque: PAY TO: YOU. With payee_t, YOU is struck through and fades (the stamp lands below it)."""
    out = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#EAF7EF" stroke="{INK}" stroke-width="7"/>',
           "".join(f'<path d="M{x + 24},{y + 150 + k * 26} C{x + w * .3},{y + 115 + k * 26} {x + w * .6},{y + 185 + k * 26} {x + w - 24},{y + 150 + k * 26}" '
                   f'stroke="rgba(31,138,91,.16)" stroke-width="3" fill="none"/>' for k in range(11)),
           txt(x + 40, y + 80, "2023 TAX REFUND", 44, GREEN, "start", 700),
           f'<rect x="{x + w - 410}" y="{y + 30}" width="380" height="70" rx="35" fill="{DCORAL}"/>',
           txt(x + w - 220, y + 77, "BY APR 15, 2027", 32, "#FFFFFF", "middle", 700),
           txt(x + 40, y + 230, "PAY TO:", 46, INK, "start", 700),
           path(f"M{x + 260},{y + 244} L{x + w - 40},{y + 244}", INK, 5)]
    out.append(f'<text x="{x + 290}" y="{y + 230}" font-size="128" fill="{COB}" style="font-family:Inter Display" font-weight="800">YOU</text>')
    if payee_t is not None:
        out.append(f'<rect x="{x + 270}" y="{y + 120}" width="320" height="118" fill="#EAF7EF" fill-opacity=".6" '
                   f'data-a="fade" data-t="{payee_t + 0.15:.2f}" data-d="0.25"/>')
        out.append(path(f"M{x + 270},{y + 192} L{x + 570},{y + 180}", DCORAL, 20, payee_t, 0.18))
    return "".join(out)


def refund():
    r = Reel("ff-reel-1029am-refund-deadline", "fullyfunded", bpm=95, css=CSSX, stage="#F3F5FF")
    X, Y, Wc = 90, 680, 900
    # frame 0: US + the trap + the date on the cheque; YOU struck at 0.7 s, U.S. TREASURY stamped below it at 1.0 s, the plain line at 1.4 s
    r.scene(4, "".join([
        '<div class="par dotsb"></div>', stamp(860, 170, 130, t=0.2),
        el('<span class="tag">US · IRS TAX REFUNDS</span>', "c", 290, a="none"),
        still("Never filed your / *2023 taxes?*", 380, 112),
        svg(cheque(X, Y, Wc, 470, payee_t=0.7)),
        el('<span class="stampx" style="font-size:84px">U.S. TREASURY</span>', "c", Y + 290, a="stamp", t=1.0, d=0.3, r=-5),
        lines("Miss April 15, 2027, and / *the government keeps it.*", 1250, t=1.4, gap=0.12, size=84),
    ]), cam="push", shake=(1.05, 0.22, 16))
    # payoff: drawn to scale, a 3-year window bar; TODAY sits near the end (Oct 29 2026 = 2 y 6.5 mo after Apr 15 2024)
    X0, X1, YB = 110, 970, 860
    per = (X1 - X0) / 3
    today = X0 + per * (2 + 6.5 / 12)
    bar = "".join([
        txt(X0, YB - 40, "APR 15, 2024", 50, INK, "start", 700, t=0.3),
        txt(X1, YB - 40, "APR 15, 2027", 50, DCORAL, "end", 700, t=0.3),
        f'<path d="M{X0},{YB + 90} L{X1},{YB + 90}" stroke="{COB}" stroke-width="170" fill="none" data-a="draw" data-t="0.35" data-d="0.7"/>',
        "".join(txt(X0 + per * (i + 0.5), YB + 108, f"YEAR {i + 1}", 54, "#FFFFFF", "middle", 700, t=0.45 + 0.2 * i) for i in range(3)),
        "".join(path(f"M{X0 + per * i:.0f},{YB + 5} L{X0 + per * i:.0f},{YB + 175}", "#FFFFFF", 6) for i in (1, 2)),
        f'<path d="M{X1 - 6},{YB} L{X1 - 6},{YB + 180}" stroke="{DCORAL}" stroke-width="12" stroke-dasharray="18 12"/>',
        f'<path d="M{today:.0f},{YB + 200} l-34,60 l68,0 z" fill="{DCORAL}" data-a="pop" data-t="1.1" data-d="0.3"/>',
        txt(today - 30, YB + 340, "TODAY", 60, DCORAL, "middle", 700, t=1.2),
    ])
    r.scene(6, "".join([
        '<div class="par dotsb"></div>',
        lines("Owed a refund? / You get *3 years* / to claim it.", 320, t=0.0, gap=0.25, size=100),
        svg(bar),
    ]), tin="whipL", td=0.2, cam="right")
    # do this (US step in words) + follow
    r.scene(7, "".join([
        '<div class="par dotsb"></div>', do_this(280),
        lines("File your 2023 return / *by April 15, 2027.*", 400, t=0.1, gap=0.2, size=98),
        el(f'<div style="display:inline-block;background:#fff;border:7px solid {INK};border-radius:28px;box-shadow:12px 12px 0 {INK};'
           f'padding:30px 52px;text-align:center"><span class="H" style="font-size:66px;line-height:1.15;color:{INK};white-space:nowrap">'
           f'Get your free 2023 wage<br>transcript at <span style="color:{COB}">IRS.gov</span>,<br>then file.</span></div>', "c", 720, a="pop", t=0.6),
        follow(1100, t=0.9, size=78),
        stamp(860, 1390, 120, t=0.6),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.loop(1.0, tin="cut")
    return timing(r, (2.9, 4.2, 5.4, 0.4))


# ============================================================================== 2. co-sign (Sat Oct 31, 7 pm)
def agreement(x=60, y=660, w=960, h=700, sign_t=None):
    """A drawn loan agreement (about 1.5x the r1 size): BORROWER signed; CO-SIGNER (YOU) gets your signature at sign_t."""
    out = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="26" fill="{COB}" stroke="{INK}" stroke-width="7"/>',
           f'<rect x="{x + 4}" y="{y + 66}" width="{w - 8}" height="44" fill="{COB}"/>',
           txt(x + w / 2, y + 74, "LOAN AGREEMENT", 58, "#FFFFFF", weight=700)]
    for k in range(3):
        out.append(f'<rect x="{x + 50}" y="{y + 150 + k * 40}" width="{w - 100 - (k == 2) * 260}" height="16" rx="8" fill="rgba(20,26,85,.14)"/>')
    yb = y + 390
    out += [txt(x + 50, yb, "BORROWER", 50, INK, "start", 700),
            path(f"M{x + 360},{yb + 10} L{x + w - 50},{yb + 10}", INK, 5),
            path(f"M{x + 390},{yb - 8} c36,-60 60,-48 48,0 s48,-48 72,-12 s36,12 72,-24 s48,36 96,0", COB, 7)]
    yc = y + 580
    out += [txt(x + 50, yc, "CO-SIGNER", 50, DCORAL, "start", 700),
            txt(x + 50, yc + 56, "(YOU)", 44, DCORAL, "start", 700),
            path(f"M{x + 360},{yc + 10} L{x + w - 50},{yc + 10}", INK, 5)]
    if sign_t is not None:
        out.append(path(f"M{x + 390},{yc - 6} c24,-72 48,-72 43,-7 s41,-60 65,-17 s29,19 60,-31 s36,12 55,7 s48,-36 84,-5", DCORAL, 8, sign_t, 0.5))
    return "".join(out)


def envelope(x, y, w=900, t=None):
    h = w * 0.6
    a = f' data-a="drop" data-t="{t:.2f}" data-d="0.35"' if t is not None else ""
    return (f'<g{a}><rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h:.0f}" rx="24" fill="{INK}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="24" fill="#FFF6EE" stroke="{INK}" stroke-width="7"/>'
            f'<path d="M{x},{y + 12} L{x + w / 2},{y + h * .5:.0f} L{x + w},{y + 12}" fill="none" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>'
            + txt(x + 60, y + h * 0.74, "TO: YOU", 72, INK, "start", 700)
            + txt(x + 60, y + h * 0.9, "THE CO-SIGNER", 46, DCORAL, "start", 700)
            + "</g>")


def report_card(x, y, w, label, color, t, h=470):
    rows = "".join(f'<rect x="{x + 36}" y="{y + 150 + i * 90}" width="{w - 170}" height="22" rx="11" fill="rgba(20,26,85,.14)"/>'
                   + (txt(x + w - 44, y + 176 + i * 90, "✓", 56, GREEN, "end", 700) if i < 2 else "") for i in range(3))
    cx, cy = x + w - 74, y + 160 + 2 * 90
    return (f'<rect x="{x + 12}" y="{y + 14}" width="{w}" height="{h}" rx="24" fill="{INK}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="24" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="100" rx="24" fill="{color}" stroke="{INK}" stroke-width="7"/>'
            f'<rect x="{x + 4}" y="{y + 60}" width="{w - 8}" height="40" fill="{color}"/>'
            + txt(x + w / 2, y + 68, label, 46, "#FFFFFF", weight=700) + rows
            + f'<g data-a="stamp" data-t="{t:.2f}" data-d="0.3"><circle cx="{cx}" cy="{cy}" r="48" fill="{DCORAL}"/>'
              f'<path d="M{cx - 22},{cy - 22} L{cx + 22},{cy + 22} M{cx + 22},{cy - 22} L{cx - 22},{cy + 22}" '
              f'stroke="#FFFFFF" stroke-width="11" stroke-linecap="round"/></g>')


def cosign():
    r = Reel("ff-reel-1031-cosign", "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    # frame 0: the picked hook + the agreement; you sign at 0.3 s; the stamp lands at 1.15 s
    r.scene(4, "".join([
        '<div class="par dots"></div>', stamp(860, 160, 130, t=0.2),
        el('<span class="tag">CANADA · US</span>', "c", 280, a="none"),
        still("Co-sign, and you can / *owe all of it.*", 370, 106),
        svg(agreement(60, 650, 960, 700, sign_t=0.3)),
        el('<span class="stampx" style="font-size:70px;white-space:nowrap">IF THEY STOP, YOU PAY</span>', "c", 1390, a="stamp", t=1.15, d=0.3, r=-4),
    ]), cam="push", shake=(1.25, 0.22, 16))
    # payoff: the bill lands, addressed to you
    r.scene(6, "".join([
        '<div class="par dots"></div>',
        lines("If they stop paying, / *you can owe all of it.*", 300, t=0.0, gap=0.2, size=100),
        svg(envelope(90, 620, 900, t=0.25)),
        el(f'<div style="display:inline-block;background:#fff;border:8px solid {INK};border-radius:28px;box-shadow:12px 12px 0 {INK};'
           f'padding:26px 50px;text-align:left;white-space:nowrap"><span class="K" style="font-size:86px;color:{INK};display:block">THE FULL BALANCE</span>'
           f'<span class="K" style="font-size:86px;color:{DCORAL};display:block">+ LATE FEES</span></div>', "c", 1230, a="pop", t=0.8, r=-2),
    ]), tin="whipL", td=0.2, cam="right")
    # the catch: both credit reports
    r.scene(5, "".join([
        '<div class="par dots"></div>',
        lines("Their missed payments / can hurt *your credit* too.", 300, t=0.0, gap=0.2, size=94),
        svg(report_card(60, 640, 460, "THEIR REPORT", COB, 0.4) + report_card(560, 640, 460, "YOUR REPORT", DCORAL, 0.8)),
        el('<span class="save" style="font-size:72px;white-space:nowrap">same missed payment, both reports</span>', "c", 1230, a="pop", t=1.05, r=-2),
    ]), tin="cut", cam="push", shake=(0.85, 0.2, 12))
    # do this + the send line (desk send test)
    r.scene(6, "".join([
        '<div class="par dots"></div>', do_this(280),
        lines("Only co-sign what / *you could pay alone.*", 400, t=0.1, gap=0.2, size=104),
        el(f'<div style="display:inline-block;background:#fff;border:8px solid {INK};border-radius:32px;box-shadow:14px 14px 0 {INK};'
           f'padding:40px 44px;text-align:center"><span class="M" style="font-size:48px;color:{INK};display:block">SEND THIS TO WHOEVER</span>'
           f'<span class="K" style="font-size:80px;color:{COB};white-space:nowrap">was asked to co-sign</span></div>', "c", 860, a="pop", t=0.6),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    # follow beat (>=1.2 s on screen)
    r.scene(4, "".join([
        '<div class="par dots"></div>',
        still("Think before / *you co-sign.*", 470, 112),
        follow(900, t=0.1, size=80),
        stamp(860, 1300, 140, t=0.2),
    ]), tin="cut", cam="push")
    r.loop(1.0, tin="cut")
    return timing(r, (2.7, 3.3, 3.0, 3.1, 1.9, 0.4))


# ============================================================================== dedicated covers (style-menu layouts, 2x render)
def cover_refund():
    """Style 8 'compare' tile (quiet): two cheque stubs, before and after the date, on pale-blue dot paper."""
    def stub(y, when, payee, col, struck=False):
        return (f'<div style="position:absolute;left:110px;width:860px;top:{y}px;height:250px;border:7px solid {INK};border-radius:26px;'
                f'background:#EAF7EF;box-shadow:12px 12px 0 {INK}">'
                f'<div class="M" style="position:absolute;left:36px;top:30px;font-size:36px;color:{col};font-weight:700">{when}</div>'
                f'<div class="M" style="position:absolute;left:36px;top:124px;font-size:36px;color:{INK};font-weight:700">PAY TO:</div>'
                f'<div class="K" style="position:absolute;left:230px;top:104px;font-size:84px;white-space:nowrap;color:{col}">{payee}</div></div>')
    return ('<div class="par dotsb" style="position:absolute;inset:0"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:300px;text-align:center"><span class="tag">US · UNFILED 2023 TAXES</span></div>'
            f'<div class="H HL" style="position:absolute;left:60px;right:60px;top:385px;text-align:center;font-size:124px;white-space:nowrap">'
            f'Your refund has<br><span class="em">a last day.</span></div>'
            + stub(740, "UNTIL APRIL 15, 2027", "YOU", COB)
            + stub(1040, "AFTER APRIL 15, 2027", "U.S. TREASURY", DCORAL)
            + f'<div style="position:absolute;left:110px;top:1320px;font-family:\'Caveat Brush\';font-size:74px;color:{DCORAL};transform:rotate(-3deg)">'
              'never filed? you can still file</div>'
            + stamp(880, 1500, 120))


def cover_cosign():
    """Ep.01 reframe 'Instead of... Say...' (style 7, quiet) under the picked hook."""
    card = ('<div style="position:absolute;left:90px;right:90px;top:{y}px;padding:34px 46px 40px;border-radius:36px;background:{bg}">'
            '<div style="font-family:\'Caveat Brush\';font-size:66px;color:{acc};line-height:1">{lab}</div>'
            '<div class="Ins" style="font-size:84px;margin-top:10px;{st}">{q}</div></div>')
    return (f'<div style="position:absolute;inset:0;background:{SOFT}"></div>'
            f'<div style="position:absolute;left:0;width:1080px;top:300px;text-align:center"><span class="tag">CANADA · US · CO-SIGNING</span></div>'
            f'<div class="H HL" style="position:absolute;left:40px;right:40px;top:370px;text-align:center;font-size:120px;white-space:nowrap">'
            f'Co-sign, and you<br>can owe<br><span class="em" style="background:#FFFFFF">all of it.</span></div>'
            + card.format(y=860, bg="#FFE7DC", acc=DCORAL, lab="Instead of…",
                          st=f"text-decoration:line-through;text-decoration-thickness:6px;text-decoration-color:{DCORAL};opacity:.8",
                          q="“I’m just helping them out.”")
            + card.format(y=1115, bg="#FFFFFF", acc=COB, lab="Say…", st="", q="“I could pay all of it.”")
            + stamp(890, 1410, 104))


COVERS = {"ff-reel-1029am-refund-deadline": cover_refund, "ff-reel-1031-cosign": cover_cosign}
REELS = {
    "ff-reel-1029am-refund-deadline": (refund, REPO / "media/music/library/v4/ff-x-level-up.mp3"),
    "ff-reel-1031-cosign": (cosign, REPO / "media/music/library/v4/ff-x-money-moves.mp3"),
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
            ts = [0.0, 0.5, 1.0, 1.4, 1.8, 2.3, 3.0, 3.6, 4.5, 5.5, 6.5, 7.2, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0]
            ts = [t for t in ts if t < r.duration]
            idx = sorted({min(int(t * 30), int(r.duration * 30) - 1) for t in ts})
            fdir, n = render_frames(r, w, dsf=1, only=idx)
            print("qa frames in", fdir)
        return r
    assert r.duration <= 15.0, r.duration
    w = SCR / rid
    fdir, n = render_frames(r, w, dsf=2, workers=1)
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

#!/usr/bin/env python3
"""Nov 3 studio build, Fully Funded Reels (no trial flag, standalone, no Part 2). Desk order (Nov 3): HOLD topic changes; Canadian
partner/family rules, felt moment + a number on frame 0, "Canada" on screen, ONE drawn object doing the meaning, no penalty-fact opens.
Extends studio/editorial/nov02_fullyfunded.py / nov01_fullyfunded.py (imported, not edited) and the FF/motion kits (not edited).

  ff-reel-1106-hbp-couple     Fri Nov 6 19:00  CANADA. Home Buyers' Plan: each first-time buyer can withdraw up to $60,000 from their
                                               own RRSPs (CRA 'Saving for the first home': a couple can each take up to $60,000), repaid
                                               over 15 years or the missed amount is taxed as income. Form T1036, one per withdrawal.
                                               Body: a drawn HOUSE whose two halves fill (YOU $60,000 | PARTNER $60,000); roof counts to
                                               $120,000. Cover: style 10 awards (two rosettes, quiet).
  ff-reel-1107-learning-bond  Sat Nov 7 19:00  CANADA. Canada Learning Bond: $500 the first eligible year + $100 a year to age 15, max $2,000,
                                               no personal contributions needed; kids born 2004+, lower-income families (1-3 kids:
                                               adjusted income <= $58,523 for Jul 2026-Jun 2027). Body: a drawn bond certificate,
                                               YOU ADD $0, a $500 seal drops. Cover: style 13 sticky-note list (quiet).

    python3 studio/editorial/nov03_fullyfunded.py <id> [--qa-only] [--cover-only]  < /dev/null
Outputs: media/studio-nov03/fullyfunded/<id>.mp4 + <id>-cover.jpg. Frames go to the scratch dir and are deleted after each encode.
"""
import argparse, json, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import nov01_fullyfunded as N  # noqa: E402
from nov01_fullyfunded import (Reel, el, stamp, svg, path, txt, COB, INK, SOFT, CREAM, DCORAL, GREEN,  # noqa: E402
                               lines, still, do_this, follow, timing, card, static, scaled)
from kit import reading_report, overflow_check, render_frames, encode, probe, loudness  # noqa: E402

N.SCR = SCR = Path("/tmp/claude-0/nov03-fullyfunded")
OUT = REPO / "media/studio-nov03/fullyfunded"
CSSX = N.CSSX
LIB = REPO / "media/music/library/v4"

# ------------------------------------------------------------------------------------------------ FACTS (checked Nov 3 2026)
# CRA 'How to make withdrawals from your RRSPs under the HBP': "You cannot withdraw more than $60,000 in total under the HBP";
#   form T1036, one per withdrawal. CRA 'How to participate in the HBP' (modified 2026-01-20): limit per person; first-time buyer =
#   no home you or your current spouse/partner owned and lived in, this year or the preceding four calendar years; written agreement to
#   buy or build; resident of Canada; acquire the home before Oct 1 of the year after the withdrawal; 89-day contribution rule.
# CRA 'Saving for the first home' (2026-02-25): the couple Alex and Neena can use the HBP, "which allows each of them to withdraw up to
#   $60,000 from their RRSPs, tax-free."  CRA 'How to repay' (2026-01-20): up to 15 years; first withdrawal 2022-2028 -> repayments start
#   the fifth year after; an unpaid minimum is included as RRSP income (line 12900).
HBP, YEARS = 60_000, 15
assert 2 * HBP == 120_000
# CRA 'Canada Learning Bond' (2026-10-29): $500 initial + $100 for each additional year of eligibility up to age 15, max $2,000; born 2004
#   or later, low-income families; "Personal contributions are not required"; beneficiary under 21 at application. ESDC 'How much money
#   can be added to RESPs' (2026-08-10): Jul 1 2026-Jun 30 2027 CLB income level 1-3 children <= $58,523; 4 < $66,036; 5 < $73,577.
#   ESDC brochure (2025-01-29): child needs a valid SIN; the RESP promoter can help you open the RESP and apply for the CLB.
#   canada.ca 'Canada Learning Bond - Automatic enrolment' (2026-07-02): from April 2028 an RESP opens automatically for eligible kids
#   born 2024 or later; you can still open one now.
assert 500 + 15 * 100 == 2000


# ============================================================================== A. Home Buyers' Plan, $60,000 each (Fri Nov 6, 7 pm)
def house(x=140, y=20, w=800, fill_t=(0.3, 0.7), roof="OUR FIRST HOME", count=None, labels=True, full=False):
    """Drawn HOUSE: cobalt roof, white body split down the middle; the left half fills cobalt (YOU $60,000) and the right half fills
    coral (PARTNER $60,000), each rising like a bar. With count the roof label counts up to the total."""
    rh, bh = 250, 400
    by = y + rh
    half = w / 2
    o = [f'<path d="M{x - 30 + 14},{by + 16} L{x + half + 14},{y + 16} L{x + w + 30 + 14},{by + 16} Z" fill="{INK}"/>',
         f'<rect x="{x + 14}" y="{by + 16}" width="{w}" height="{bh}" rx="10" fill="{INK}"/>',
         f'<rect x="{x}" y="{by}" width="{w}" height="{bh}" rx="10" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>']
    for k, col in enumerate((COB, DCORAL)):
        cx = x + half / 2 + k * half
        y0, y1 = by + bh - 4, by + 4
        if full or fill_t is None:
            o.append(f'<rect x="{x + 4 + k * half}" y="{by + 4}" width="{half - 8}" height="{bh - 8}" fill="{col}"/>')
        else:
            o.append(f'<path d="M{cx},{y0} L{cx},{y1}" stroke="{col}" stroke-width="{half - 8}" fill="none" '
                     f'data-a="draw" data-t="{fill_t[k]:.2f}" data-d="0.45"/>')
    o.append(f'<rect x="{x}" y="{by}" width="{w}" height="{bh}" rx="10" fill="none" stroke="{INK}" stroke-width="7"/>')
    o.append(f'<line x1="{x + half}" y1="{by}" x2="{x + half}" y2="{by + bh}" stroke="{INK}" stroke-width="7"/>')
    o.append(f'<path d="M{x - 30},{by} L{x + half},{y} L{x + w + 30},{by} Z" fill="{COB}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>')
    if count:
        a0, a1 = count
        o.append(txt(x + half, by - 150, "UP TO", 40, "#FFFFFF", weight=700))
        o.append(f'<text x="{x + half}" y="{by - 50}" font-size="96" fill="#FFFFFF" text-anchor="middle" style="font-family:Inter Display" '
                 f'font-weight="800" data-a="count" data-from="{a0}" data-to="{a1}" data-pre="$" data-comma="1" data-t="0.2" data-d="0.8">'
                 f'${a0:,}</text>')
    elif roof:
        o.append(txt(x + half, by - 60, roof, 46, "#FFFFFF", weight=700))
    if labels:
        for k, (who, tt) in enumerate((("YOU", 0.55), ("PARTNER", 0.95))):
            cx = x + half / 2 + k * half
            ft = None if (full or fill_t is None) else fill_t[k] + 0.3
            o.append(txt(cx, by + 130, who, 52, "#FFFFFF", weight=700, t=ft))
            o.append(txt(cx, by + 200, "UP TO", 44, "#FFFFFF", weight=700, t=ft))
            o.append(f'<text x="{cx}" y="{by + 300}" font-size="80" fill="#FFFFFF" text-anchor="middle" style="font-family:Inter Display" '
                     f'font-weight="800"' + (f' data-a="fade" data-t="{ft:.2f}" data-d="0.25"' if ft is not None else "") + '>$60,000</text>')
    return "".join(o)


def t1036(x=90, y=0, w=900, h=520, tick_t=None):
    """Drawn FORM T1036: HOME BUYERS' PLAN request; AMOUNT row and a SIGNED AGREEMENT TO BUY box that gets ticked."""
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="26" fill="{COB}" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x + 4}" y="{y + 66}" width="{w - 8}" height="44" fill="{COB}"/>',
         txt(x + w / 2, y + 74, "FORM T1036", 58, "#FFFFFF", weight=700),
         txt(x + w / 2, y + 175, "HOME BUYERS' PLAN · WITHDRAW FROM RRSP", 34, INK, weight=700)]
    ry = y + 290
    o.append(txt(x + 50, ry, "AMOUNT", 48, INK, "start", 700))
    o.append(f'<line x1="{x + 330}" y1="{ry + 10}" x2="{x + w - 50}" y2="{ry + 10}" stroke="{INK}" stroke-width="4"/>')
    o.append(f'<text x="{x + w - 60}" y="{ry}" font-size="76" fill="{COB}" text-anchor="end" style="font-family:Inter Display" font-weight="800">'
             f'$60,000</text>')
    by = y + 440
    o.append(f'<rect x="{x + 50}" y="{by - 62}" width="84" height="84" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>')
    o.append(txt(x + 165, by, "SIGNED AGREEMENT TO BUY", 44, COB, "start", 700))
    o.append(path(f"M{x + 68},{by - 22} l18,22 l36,-48", GREEN, 13, tick_t, 0.3) if tick_t is not None
             else path(f"M{x + 68},{by - 22} l18,22 l36,-48", GREEN, 13))
    return "".join(o)


def hbp_couple():
    r = Reel("ff-reel-1106-hbp-couple", "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    # frame 0: felt moment + the number (hook, 5 words); the two halves of the house fill 0.3 / 0.7 s; plain payoff at 1.4 s.
    r.scene(4, "".join([
        '<div class="par dots"></div>',
        el('<span class="tag" style="font-size:42px">CANADA · HOME BUYERS’ PLAN</span>', "c", 300, a="none"),
        still("Buying together? / *Up to $60,000 each.*", 390, 108),
        svg(scaled(house(140, 20, 800, fill_t=(0.3, 0.7)), 0.86, 690, vh=700)),
        lines("Each of you can borrow it / *from your own RRSP.*", 1350, t=1.4, gap=0.14, size=80),
    ]), cam="push", shake=(0.8, 0.2, 12))
    r.scene(6, "".join([
        '<div class="par dots"></div>',
        still("Together: up to / *$120,000* for your home.", 330, 100),
        svg(scaled(house(140, 20, 800, full=True, count=(60000, 120000), labels=True), 0.8, 620, vh=700)),
        el('<span class="save" style="font-size:62px;white-space:nowrap">pay back a bit each year, over 15 years</span>',
           "c", 1200, a="pop", t=0.9, r=-2),
        lines("First-time buyers only: / no home of your own in 4 years.", 1310, t=1.3, gap=0.14, size=66),
    ]), tin="cut", cam="right")
    r.scene(7, "".join([
        do_this(320),
        still("Ask your RRSP bank / *for form T1036.*", 420, 100),
        svg(scaled(t1036(90, 10, 900, tick_t=0.45), 0.86, 720, vh=560)),
        card(f'<span class="H" style="font-size:56px;line-height:1.22;color:{INK};white-space:nowrap">One each, once you sign to buy.<br>'
             f'<span style="color:{COB}">Only money already in your RRSP.</span></span>', 1250, t=0.8, pad="32px 40px"),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        still("Send this to / *your partner.*", 340, 116),
        svg(scaled(static(house(140, 20, 800, full=True, count=(120000, 120000), labels=True)), 0.72, 650, vh=700)),
        follow(1210, t=0.15, size=80),
        stamp(840, 1440, 140, t=0.2),
    ]), tin="cut", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.5, 3.6, 3.6, 2.5, 0.4))


# ============================================================================== B. Canada Learning Bond (Sat Nov 7, 7 pm)
def bond(x=90, y=10, w=900, seal_t=0.35, seal="$500", count=None, rows=(("YOU ADD", "$0"),), row_t=None):
    """Drawn CANADA LEARNING BOND certificate: dotted inner border, YOU ADD $0 row, a coral seal carrying the bond drops on (or counts)."""
    import math
    h = 600
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="20" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="#FFFDF6" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x + 26}" y="{y + 26}" width="{w - 52}" height="{h - 52}" rx="12" fill="none" stroke="{COB}" stroke-width="4" '
         f'stroke-dasharray="4 10"/>',
         txt(x + w / 2, y + 115, "CANADA LEARNING BOND", 62, COB, weight=700),
         f'<line x1="{x + 90}" y1="{y + 148}" x2="{x + w - 90}" y2="{y + 148}" stroke="{COB}" stroke-width="4"/>',
         txt(x + w / 2, y + 205, "FOR YOUR CHILD'S RESP", 40, INK, weight=700)]
    one = len(rows) == 1
    for k, (lab, val) in enumerate(rows):
        ry = y + (320 if one else 300) + k * 150
        tt = None if row_t is None else row_t + 0.35 * k
        o.append(txt(x + 70, ry, lab, 54 if one else 36, INK, "start", 700, t=tt))
        an = f' data-a="fade" data-t="{tt:.2f}" data-d="0.25"' if tt is not None else ""
        o.append(f'<text x="{x + 60}" y="{ry + (190 if one else 80)}" font-size="{200 if one else 76}" fill="{COB}" '
                 f'style="font-family:Inter Display" font-weight="800"{an}>{val}</text>')
    cx, cy = x + w - 200, y + 400
    sa = f' data-a="drop" data-t="{seal_t:.2f}" data-d="0.45"' if seal_t is not None else ""
    if count:
        lab = (f'<text x="{cx}" y="{cy + 24}" font-size="70" fill="#FFFFFF" text-anchor="middle" style="font-family:Inter Display" font-weight="800" '
               f'data-a="count" data-from="{count[0]}" data-to="{count[1]}" data-pre="$" data-comma="1" data-t="0.3" data-d="1.0">${count[0]:,}</text>')
    else:
        lab = (f'<text x="{cx}" y="{cy + 30}" font-size="{88 if len(seal) <= 4 else 70}" fill="#FFFFFF" text-anchor="middle" '
               f'style="font-family:Inter Display" font-weight="800">{seal}</text>')
    ribbon = (f'<path d="M{cx - 64},{cy + 90} l-26,110 l42,-26 l22,44 l26,-110 Z" fill="{COB}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
              f'<path d="M{cx + 64},{cy + 90} l26,110 l-42,-26 l-22,44 l-26,-110 Z" fill="{COB}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>')
    pts = []
    for i in range(48):
        rr = 146 if i % 2 == 0 else 130
        a = math.pi * 2 * i / 48
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    o.append(f'<g{sa}>{ribbon}<polygon points="{" ".join(pts)}" transform="translate(8,10)" fill="{INK}"/>'
             f'<polygon points="{" ".join(pts)}" fill="{DCORAL}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
             f'<circle cx="{cx}" cy="{cy}" r="106" fill="none" stroke="#FFFFFF" stroke-opacity=".6" stroke-width="4" stroke-dasharray="8 10"/>'
             f'{lab}</g>')
    return "".join(o)


def checklist(x=90, y=0, w=900, t0=0.4):
    """Drawn 3-step card: CHILD'S SIN / OPEN AN RESP / ASK FOR THE BOND, ticked one after the other."""
    h = 500
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>']
    for k, lab in enumerate(("1  GET YOUR CHILD'S SIN", "2  OPEN AN RESP", "3  ASK FOR THE BOND")):
        by = y + 130 + k * 140
        o.append(f'<rect x="{x + 50}" y="{by - 62}" width="84" height="84" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>')
        o.append(txt(x + 170, by, lab, 50, COB if k == 2 else INK, "start", 700))
        tt = None if t0 is None else t0 + 0.35 * k
        o.append(path(f"M{x + 68},{by - 22} l18,22 l36,-48", GREEN, 13, tt, 0.25) if tt is not None
                 else path(f"M{x + 68},{by - 22} l18,22 l36,-48", GREEN, 13))
    return "".join(o)


def learning_bond():
    r = Reel("ff-reel-1107-learning-bond", "fullyfunded", bpm=95, css=CSSX, stage="#F3F5FF")
    r.scene(4, "".join([
        '<div class="par dotsb"></div>',
        el('<span class="tag" style="font-size:36px;white-space:nowrap">CANADA · LOWER-INCOME FAMILIES</span>', "c", 300, a="none"),
        still("Saving $0? / *Canada still adds $500.*", 390, 108),
        svg(scaled(bond(90, 10, 900, seal_t=0.35), 0.9, 700, vh=680)),
        lines("For your child’s education. / *No savings needed.*", 1350, t=1.4, gap=0.14, size=80),
    ]), cam="push", shake=(0.75, 0.2, 14))
    r.scene(6, "".join([
        '<div class="par dotsb"></div>',
        still("Then *$100 a year,* / up to $2,000.", 330, 104),
        svg(scaled(bond(90, 10, 900, seal_t=None, count=(500, 2000),
                        rows=(("FIRST YEAR", "$500"), ("EACH YEAR TO AGE 15", "+$100"))), 0.84, 620, vh=680)),
        el('<span class="save" style="font-size:64px;white-space:nowrap">for kids born in 2004 or later</span>', "c", 1200, a="pop", t=0.9, r=-2),
        lines("Family income up to $58,523 / with 1 to 3 kids.", 1310, t=1.3, gap=0.14, size=68),
    ]), tin="cut", cam="right")
    r.scene(7, "".join([
        do_this(320),
        still("Open an RESP. / *Ask for the bond.*", 420, 104),
        svg(scaled(checklist(90, 10, 900, t0=0.4), 0.88, 730, vh=540)),
        card(f'<span class="H" style="font-size:62px;line-height:1.2;color:{INK};white-space:nowrap">Bring your SIN and theirs.<br>'
             f'<span style="color:{COB}">Pick a bank that offers it.</span></span>', 1250, t=1.4, pad="34px 48px"),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        still("Send this to / *a new parent.*", 340, 116),
        svg(scaled(static(bond(90, 10, 900, seal_t=None, seal="$500")), 0.76, 660, vh=680)),
        follow(1230, t=0.15, size=80),
        stamp(840, 1450, 140, t=0.2),
    ]), tin="cut", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.5, 3.6, 3.6, 2.5, 0.4))


# ============================================================================== covers
def rosette(cx, cy, col, who, amt, r0=172):
    import math
    pts = []
    for i in range(56):
        rr = r0 if i % 2 == 0 else r0 - 16
        a = math.pi * 2 * i / 56
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    rib = (f'<path d="M{cx - 70},{cy + 100} l-34,150 l52,-30 l26,54 l36,-160 Z" fill="{col}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
           f'<path d="M{cx + 70},{cy + 100} l34,150 l-52,-30 l-26,54 l-36,-160 Z" fill="{col}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>')
    return (rib + f'<polygon points="{" ".join(pts)}" transform="translate(8,10)" fill="{INK}"/>'
            f'<polygon points="{" ".join(pts)}" fill="{col}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r0 - 34}" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
            f'<text x="{cx}" y="{cy - 44}" font-size="36" fill="{INK}" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700">{who}</text>'
            f'<text x="{cx}" y="{cy - 2}" font-size="28" fill="{INK}" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700">UP TO</text>'
            f'<text x="{cx}" y="{cy + 60}" font-size="56" fill="{col}" text-anchor="middle" style="font-family:Inter Display" font-weight="800">{amt}</text>')


def cover_hbp():
    """Style 10 awards (quiet): two rosettes, YOU $60,000 / PARTNER $60,000, serif hook + pill, handwritten total, round stamp."""
    return (f'<div class="par dots" style="position:absolute;inset:0"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:300px;text-align:center"><span class="tag">CANADA · HOME BUYERS’ PLAN</span></div>'
            f'<div class="H HL" style="position:absolute;left:40px;right:40px;top:390px;text-align:center;font-size:96px;white-space:nowrap">'
            f'Buying together?<br><span class="em">Up to $60,000 each.</span></div>'
            f'<svg style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">'
            f'{rosette(320, 880, COB, "YOU", "$60,000")}{rosette(760, 880, DCORAL, "PARTNER", "$60,000")}</svg>'
            f'<div style="position:absolute;left:0;right:0;top:1190px;text-align:center;font-family:\'Caveat Brush\';font-size:72px;color:{DCORAL};'
            f'transform:rotate(-2deg);white-space:nowrap">= up to $120,000 from your RRSPs</div>'
            f'<div style="position:absolute;left:0;right:0;top:1300px;text-align:center;font-family:\'DejaVu Sans Mono\';font-weight:700;'
            f'font-size:33px;letter-spacing:.03em;color:{COB}">FIRST-TIME BUYERS · REPAY OVER 15 YEARS</div>'
            + stamp(870, 1470, 110))


def cover_bond():
    """Style 13 sticky-note list (quiet): lined note card, red margin line, tape strip, on cobalt; serif hook + handwritten lines."""
    return (f'<div style="position:absolute;inset:0;background:{COB}"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:310px;text-align:center"><span class="tag" style="background:#fff;color:#2B3FE0">'
            'CANADA · LOWER-INCOME FAMILIES</span></div>'
            f'<div style="position:absolute;left:110px;width:860px;top:430px;height:930px;transform:rotate(-1.5deg);background:'
            f'repeating-linear-gradient(#FFFDF6 0 86px,#C9D2FF 86px 89px);border-radius:10px;box-shadow:18px 20px 0 rgba(14,20,64,.45)">'
            '<div style="position:absolute;left:88px;top:0;bottom:0;width:4px;background:#E0464C"></div>'
            '<div style="position:absolute;left:330px;top:-34px;width:200px;height:66px;background:rgba(255,176,143,.85);transform:rotate(3deg)"></div>'
            f'<div class="H HL" style="position:absolute;left:120px;right:30px;top:80px;font-size:112px;white-space:nowrap">'
            f'Saving $0?<br>Canada still<br><span class="em">adds $500.</span></div>'
            f'<div style="position:absolute;left:130px;top:520px;font-family:\'Caveat Brush\';font-size:68px;line-height:1.2;color:{DCORAL};'
            f'white-space:nowrap;transform:rotate(-2deg)">the Canada Learning Bond<br>+$100 a year, up to $2,000<br>no savings needed</div></div>'
            + stamp(860, 1440, 120))


COVERS = {"ff-reel-1106-hbp-couple": cover_hbp, "ff-reel-1107-learning-bond": cover_bond}
REELS = {
    "ff-reel-1106-hbp-couple": (hbp_couple, LIB / "ff-x-money-moves.mp3"),
    "ff-reel-1107-learning-bond": (learning_bond, LIB / "ff-x-level-up.mp3"),
}


def cover(r, rid, out):
    N.COVERS[rid] = COVERS[rid]
    N.cover(r, rid, out)


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
            shutil.rmtree(w, ignore_errors=True)
            ts = [0.0, 0.5, 1.0, 1.4, 2.0, 3.0, 3.6, 4.5, 5.5, 6.5, 7.2, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0]
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

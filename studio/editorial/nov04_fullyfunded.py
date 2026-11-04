#!/usr/bin/env python3
"""Nov 4 studio build, Fully Funded Reels (no trial flag, standalone, no Part 2, no on-screen send line: send_test false).
Desk order (Nov 4): FF HOLD. Canadian partner/family rules, felt moment + a number on frame 0, "Canada" on screen, drawn style,
ONE drawn object doing the meaning. Extends studio/editorial/nov03_fullyfunded.py / nov01_fullyfunded.py (imported, not edited).

  ff-reel-1108-medical-one-return  Sun Nov 8 19:00  CANADA. Medical expenses (line 33099): either spouse can claim the family's
                                                    bills (you, partner, kids under 18); only the part above the lesser of 3% of the
                                                    claimer's net income or the fixed amount ($2,834 for 2025) counts, so the lower
                                                    earner usually gets more counted (CRA RC4065 Richard/Pauline story). Object: a
                                                    drawn pharmacy-style RECEIPT ($2,000) that is measured on each return.
  ff-reel-1109-spousal-rrsp-3yr    Mon Nov 9 19:00  CANADA. Spousal RRSP: the contributor deducts, the money is in the partner's
                                                    name; a withdrawal is taxed to the contributor if they paid into any spousal RRSP
                                                    that year or the 2 years before (CRA, modified 2026-06-26). Object: a drawn
                                                    4-year CALENDAR STRIP with a lock that opens in the 4th year.

    python3 studio/editorial/nov04_fullyfunded.py <id> [--qa-only] [--cover-only]  < /dev/null
Outputs: media/studio-nov04/fullyfunded/<id>.mp4 + <id>-cover.jpg. Frames go to the scratch dir and are deleted after each encode.
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

N.SCR = SCR = Path("/tmp/claude-0/nov04-fullyfunded")
OUT = REPO / "media/studio-nov04/fullyfunded"
CSSX = N.CSSX
LIB = REPO / "media/music/library/v4"

# ------------------------------------------------------------------------------------------------ FACTS (checked Nov 4 2026)
# CRA RC4065 'Medical Expenses 2025' (modified 2026-01-20): line 33099 = eligible expenses you or your spouse/common-law partner
#   paid for you, your spouse/partner and your or their children under 18; claim "the total of the eligible expenses minus the lesser
#   of" $2,834 or 3% of net income (line 23600); any 12-month period ending in the tax year. Worked story: $6,300 of family expenses,
#   "Either Richard or Pauline can claim this amount on line 33099"; Pauline (net $55,000) -> $4,650, Richard (net $42,000) -> $5,040,
#   so Richard (the lower income) claims.
# Our maths (made up for this post): $2,000 of bills; $90,000 -> 3% = $2,700 (< $2,834) -> $0 counts; $40,000 -> 3% = $1,200 -> $800.
BILLS = (("DENTIST", 900), ("GLASSES", 650), ("PRESCRIPTIONS", 450))
TOTAL = sum(v for _, v in BILLS)
HI, LO = 90_000, 40_000
assert TOTAL == 2000
assert min(round(HI * .03), 2834) == 2700 and max(0, TOTAL - 2700) == 0
assert min(round(LO * .03), 2834) == 1200 and TOTAL - 1200 == 800
# CRA 'Withdrawing from spousal or common-law partner RRSPs' (modified 2026-06-26): to avoid the contributor including the amount,
#   they must not have contributed to any spousal RRSP in the withdrawal year or the two preceding years; form T2205.
#   CRA 'Contributing to your spouse's or common-law partner's RRSPs' (modified 2026-01-29): the contributor claims the deduction;
#   contributions reduce the contributor's own RRSP deduction limit.
LAST, OK_YEAR = 2026, 2029
assert OK_YEAR - 2 > LAST  # withdrawal year 2029: 2029, 2028, 2027 have no contributions


# ============================================================================== A. Medical bills on one return (Sun Nov 8, 7 pm)
def receipt(x=270, y=0, w=540, row_t=None, total_t=None, who=None, minus=None, counts=None, minus_t=None, counts_t=None):
    """Drawn RECEIPT (FAMILY MEDICAL): DENTIST / GLASSES / PRESCRIPTIONS rows and TOTAL $2,000, zig-zag bottom edge.
    With minus/counts it is measured on one return: 'FIRST $2,700 DOESN'T COUNT' and a COUNTS stamp."""
    rows_h = 96 * len(BILLS)
    h = 250 + rows_h + (300 if minus else 60)
    # zig-zag (torn) bottom edge, right to left
    pts = [f"{x + w - (w / 18) * k:.1f},{y + h + (18 if k % 2 else 0)}" for k in range(19)]
    shape = f"M{x},{y} L{x + w},{y} L" + " L".join(pts) + " Z"
    o = [f'<path d="{shape}" transform="translate(14,16)" fill="{INK}"/>',
         f'<path d="{shape}" fill="#FFFFFF" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>']
    head = who or "FAMILY MEDICAL"
    o.append(txt(x + w / 2, y + 82, head, 44 if who else 46, COB, weight=700))
    o.append(f'<line x1="{x + 36}" y1="{y + 122}" x2="{x + w - 36}" y2="{y + 122}" stroke="{INK}" stroke-width="4" stroke-dasharray="10 8"/>')
    for k, (lab, v) in enumerate(BILLS):
        ry = y + 196 + 96 * k
        tt = None if row_t is None else row_t + 0.2 * k
        o.append(txt(x + 40, ry, lab, 40, INK, "start", 700, t=tt))
        o.append(txt(x + w - 40, ry, f"${v:,}", 44, INK, "end", 700, t=tt))
    ty = y + 196 + rows_h + 20
    o.append(f'<line x1="{x + 36}" y1="{ty - 70}" x2="{x + w - 36}" y2="{ty - 70}" stroke="{INK}" stroke-width="5"/>')
    an = f' data-a="fade" data-t="{total_t:.2f}" data-d="0.25"' if total_t is not None else ""
    o.append(f'<g{an}>' + txt(x + 40, ty, "TOTAL", 48, INK, "start", 700) +
             f'<text x="{x + w - 40}" y="{ty + 6}" font-size="80" fill="{COB}" text-anchor="end" style="font-family:Inter Display" '
             f'font-weight="800">${TOTAL:,}</text></g>')
    if minus:
        my = ty + 96
        ma = f' data-a="fade" data-t="{minus_t:.2f}" data-d="0.25"' if minus_t is not None else ""
        o.append(f'<g{ma}>' + txt(x + 40, my, "MINUS 3% OF INCOME", 34, DCORAL, "start", 700) +
                 txt(x + w - 40, my, f"−${minus:,}", 44, DCORAL, "end", 700) + '</g>')
        sa = f' data-a="stamp" data-t="{counts_t:.2f}" data-d="0.3"' if counts_t is not None else ""
        col = GREEN if counts else DCORAL
        cx, cy = x + w / 2, ty + 200
        o.append(f'<g{sa}><g transform="rotate(-6 {cx} {cy})"><rect x="{cx - 220}" y="{cy - 62}" width="440" height="116" rx="18" '
                 f'fill="#FFFFFF" stroke="{col}" stroke-width="9"/>'
                 f'<text x="{cx}" y="{cy + 24}" font-size="70" fill="{col}" text-anchor="middle" style="font-family:Inter Display" '
                 f'font-weight="800">COUNTS ${counts:,}</text></g></g>')
    return "".join(o)


def measure(x=60, y=0, w=460, who="YOU", inc=HI, t0=None):
    """Tall drawn side receipt for one return (drawn at final size, no scaling): WHO / EARNS $X / BILLS $2,000 / 3% OF INCOME /
    -$2,700, then a stamp kept inside the borders: '$0 / CAN BE CLAIMED' (coral) or '$800 / CAN BE CLAIMED' (green)."""
    minus = min(round(inc * .03), 2834)
    counts = max(0, TOTAL - minus)
    h = 700
    pts = [f"{x + w - (w / 14) * k:.1f},{y + h + (18 if k % 2 else 0)}" for k in range(15)]
    shape = f"M{x},{y} L{x + w},{y} L" + " L".join(pts) + " Z"

    def fa(k):
        return f' data-a="fade" data-t="{t0 + k:.2f}" data-d="0.25"' if t0 is not None else ""
    o = [f'<path d="{shape}" transform="translate(10,12)" fill="{INK}"/>',
         f'<path d="{shape}" fill="#FFFFFF" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>',
         txt(x + w / 2, y + 70, who, 52, COB, weight=700),
         txt(x + w / 2, y + 128, f"EARNS ${inc:,}", 40, INK, weight=700),
         f'<line x1="{x + 28}" y1="{y + 160}" x2="{x + w - 28}" y2="{y + 160}" stroke="{INK}" stroke-width="4" stroke-dasharray="10 8"/>',
         txt(x + 30, y + 232, "BILLS", 36, INK, "start", 700),
         f'<text x="{x + w - 30}" y="{y + 238}" font-size="60" fill="{COB}" text-anchor="end" style="font-family:Inter Display" '
         f'font-weight="800">${TOTAL:,}</text>',
         f'<g{fa(0)}>' + txt(x + 30, y + 312, "3% OF INCOME", 42, DCORAL, "start", 700) +
         f'<text x="{x + w - 30}" y="{y + 398}" font-size="76" fill="{DCORAL}" text-anchor="end" style="font-family:Inter Display" '
         f'font-weight="800">−${minus:,}</text></g>',
         f'<line x1="{x + 28}" y1="{y + 440}" x2="{x + w - 28}" y2="{y + 440}" stroke="{INK}" stroke-width="5"/>']
    col = GREEN if counts else DCORAL
    sa = f' data-a="pop" data-t="{t0 + 0.45:.2f}" data-d="0.3"' if t0 is not None else ""
    bx, bw = x + 30, w - 60
    o.append(f'<g{sa}><rect x="{bx}" y="{y + 470}" width="{bw}" height="190" rx="20" fill="#FFFFFF" stroke="{col}" stroke-width="9"/>'
             f'<text x="{x + w / 2}" y="{y + 572}" font-size="96" fill="{col}" text-anchor="middle" style="font-family:Inter Display" '
             f'font-weight="800">${counts:,}</text>'
             + txt(x + w / 2, y + 632, "CAN BE CLAIMED", 33, col, weight=700) + '</g>')
    return "".join(o)


def return_line(x=90, y=0, w=900, tick_t=None):
    """Drawn tax-return row: LINE 33099 · MEDICAL EXPENSES, $2,000, and a ticked 'ON THE LOWER EARNER'S RETURN' box."""
    h = 420
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="26" fill="{COB}" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x + 4}" y="{y + 66}" width="{w - 8}" height="44" fill="{COB}"/>',
         txt(x + w / 2, y + 74, "YOUR TAX RETURN", 54, "#FFFFFF", weight=700)]
    ry = y + 215
    o.append(txt(x + 50, ry, "LINE 33099", 52, INK, "start", 700))
    o.append(f'<text x="{x + w - 50}" y="{ry + 6}" font-size="80" fill="{COB}" text-anchor="end" style="font-family:Inter Display" '
             f'font-weight="800">${TOTAL:,}</text>')
    by = y + 345
    o.append(f'<rect x="{x + 50}" y="{by - 62}" width="84" height="84" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>')
    o.append(txt(x + 165, by, "ON THE LOWER EARNER'S RETURN", 38, COB, "start", 700))
    o.append(path(f"M{x + 68},{by - 22} l18,22 l36,-48", GREEN, 13, tick_t, 0.3) if tick_t is not None
             else path(f"M{x + 68},{by - 22} l18,22 l36,-48", GREEN, 13))
    return "".join(o)


def medical():
    r = Reel("ff-reel-1108-medical-one-return", "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    # frame 0: felt moment + the number (hook, 5 words); receipt rows tick in 0.15-0.55 s; plain payoff at 1.3 s.
    r.scene(4, "".join([
        '<div class="par dots"></div>',
        el('<span class="tag" style="font-size:42px">CANADA · MEDICAL EXPENSES</span>', "c", 300, a="none"),
        still("Dentist, glasses, pills: / *$2,000 this year?*", 390, 100),
        svg(scaled(receipt(230, 20, 620, row_t=None, total_t=0.3), 0.86, 640, vh=720)),
        lines("Claim them all on / *the lower earner’s return.*", 1215, t=1.3, gap=0.14, size=80),
    ]), cam="push", shake=(0.75, 0.2, 12))
    r.scene(6, "".join([
        '<div class="par dots"></div>',
        still("Only bills above / *3% of income* count.", 330, 100),
        svg(measure(95, 610, 425, "YOU", HI, t0=0.3) + measure(560, 610, 425, "PARTNER", LO, t0=0.95)),
        el('<span class="save" style="font-size:66px;white-space:nowrap">same bills, a bigger claim</span>', "c", 1345, a="pop", t=1.7, r=-2),
    ]), tin="land", cam="right")
    r.scene(7, "".join([
        do_this(320),
        still("Claim them on / *line 33099.*", 420, 104),
        svg(scaled(return_line(90, 10, 900, tick_t=0.45), 0.86, 730, vh=460)),
        card(f'<span class="H" style="font-size:56px;line-height:1.22;color:{INK};white-space:nowrap">Try both returns in your tax app.<br>'
             f'<span style="color:{COB}">Keep the one that counts more.</span></span>', 1180, t=0.8, pad="32px 40px"),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        still("One return. / *The whole family’s bills.*", 340, 104),
        svg(scaled(static(receipt(230, 20, 620, row_t=None, total_t=None)), 0.72, 640, vh=720)),
        follow(1230, t=0.15, size=80),
        stamp(840, 1450, 140, t=0.2),
    ]), tin="land", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.4, 3.8, 3.6, 2.6, 0.4))


# ============================================================================== B. Spousal RRSP, wait 3 years (Mon Nov 9, 7 pm)
def account(x=90, y=0, w=900, row_t=None):
    """Drawn SPOUSAL RRSP account card: IN THE NAME OF / YOUR PARTNER, then TAX BREAK GOES TO / YOU (label line + big value line)."""
    h = 520
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="26" fill="{COB}" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x + 4}" y="{y + 66}" width="{w - 8}" height="44" fill="{COB}"/>',
         txt(x + w / 2, y + 76, "SPOUSAL RRSP", 60, "#FFFFFF", weight=700)]
    for k, (lab, val, col) in enumerate((("IN THE NAME OF", "YOUR PARTNER", DCORAL), ("TAX BREAK GOES TO", "YOU", COB))):
        ry = y + 180 + 190 * k
        tt = None if (row_t is None or k == 0) else row_t
        an = f' data-a="fade" data-t="{tt:.2f}" data-d="0.25"' if tt is not None else ""
        o.append(f'<g{an}>' + txt(x + 50, ry, lab, 40, INK, "start", 700) +
                 f'<text x="{x + 50}" y="{ry + 96}" font-size="92" fill="{col}" style="font-family:Inter Display" '
                 f'font-weight="800">{val}</text></g>')
        if k == 0:
            o.append(f'<line x1="{x + 40}" y1="{ry + 135}" x2="{x + w - 40}" y2="{ry + 135}" stroke="{INK}" stroke-opacity=".2" '
                     f'stroke-width="4" stroke-dasharray="10 8"/>')
    return "".join(o)


def calendar(x=60, y=0, w=960, t0=None, open_t=None):
    """Drawn 4-year CALENDAR STRIP: 2026 (YOUR LAST DEPOSIT) / 2027 / 2028 locked; 2029 unlocks: TAKE IT OUT."""
    import math  # noqa: F401
    o = []
    cw, gap = (w - 3 * 24) / 4, 24
    for k, yr in enumerate((2026, 2027, 2028, 2029)):
        cx = x + k * (cw + gap)
        last = k == 3
        tt = None if t0 is None else t0 + 0.28 * k
        an = f' data-a="pop" data-t="{tt:.2f}" data-d="0.3"' if tt is not None else ""
        fill = "#E9F7EF" if last else "#FFFFFF"
        o.append(f'<g{an}><rect x="{cx + 10}" y="{y + 12}" width="{cw}" height="330" rx="20" fill="{INK}"/>'
                 f'<rect x="{cx}" y="{y}" width="{cw}" height="330" rx="20" fill="{fill}" stroke="{INK}" stroke-width="6"/>'
                 f'<rect x="{cx}" y="{y}" width="{cw}" height="70" rx="20" fill="{GREEN if last else (DCORAL if k == 0 else COB)}" '
                 f'stroke="{INK}" stroke-width="6"/><rect x="{cx + 3}" y="{y + 40}" width="{cw - 6}" height="30" '
                 f'fill="{GREEN if last else (DCORAL if k == 0 else COB)}"/>'
                 f'<text x="{cx + cw / 2}" y="{y + 52}" font-size="40" fill="#FFFFFF" text-anchor="middle" '
                 f'style="font-family:Inter Display" font-weight="800">{yr}</text>')
        mx = cx + cw / 2
        if k == 0:
            o.append(f'<text x="{mx}" y="{y + 175}" font-size="80" fill="{DCORAL}" text-anchor="middle" style="font-family:Inter Display" '
                     f'font-weight="800">+$</text>' + txt(mx, y + 248, "LAST", 42, INK, weight=700) + txt(mx, y + 298, "DEPOSIT", 42, INK, weight=700))
        elif not last:
            # padlock
            o.append(f'<path d="M{mx - 34},{y + 160} v-26 a34,34 0 0 1 68,0 v26" fill="none" stroke="{INK}" stroke-width="10"/>'
                     f'<rect x="{mx - 52}" y="{y + 156}" width="104" height="86" rx="14" fill="{INK}"/>'
                     f'<circle cx="{mx}" cy="{y + 196}" r="11" fill="#FFFFFF"/>' + txt(mx, y + 300, "WAIT", 44, INK, weight=700))
        o.append("</g>")
        if last:
            tk = f"M{mx - 44},{y + 196} l30,34 l60,-80"
            o.append(path(tk, GREEN, 18, open_t, 0.3) if open_t is not None else path(tk, GREEN, 18))
            o.append(txt(mx, y + 300, "TAKE OUT", 35, GREEN, weight=700, t=open_t))
    return "".join(o)


def spousal():
    r = Reel("ff-reel-1109-spousal-rrsp-3yr", "fullyfunded", bpm=95, css=CSSX, stage="#F3F5FF")
    r.scene(4, "".join([
        '<div class="par dotsb"></div>',
        el('<span class="tag" style="font-size:42px">CANADA · SPOUSAL RRSP</span>', "c", 300, a="none"),
        still("Earn twice what / *your partner does?*", 390, 108),
        svg(scaled(account(90, 10, 900, row_t=0.3), 0.88, 690, vh=560)),
        lines("Save in their RRSP. / *You get the tax break.*", 1200, t=1.3, gap=0.14, size=84),
    ]), cam="push", shake=(0.75, 0.2, 12))
    r.scene(6, "".join([
        '<div class="par dotsb"></div>',
        still("Leave it 3 years / *after your last deposit.*", 330, 96),
        svg(scaled(calendar(60, 10, 960, t0=0.2, open_t=1.25), 0.96, 640, vh=360)),
        lines("Take it out sooner? / It’s taxed as your income.", 1080, t=1.5, gap=0.14, size=72),
        el('<span class="save" style="font-size:58px;white-space:nowrap">later, it’s taxed as theirs</span>', "c", 1300, a="pop", t=2.2, r=-2),
    ]), tin="land", cam="right")
    r.scene(7, "".join([
        do_this(320),
        still("Ask your bank for / *a spousal RRSP.*", 420, 104),
        svg(scaled(static(account(90, 10, 900)), 0.8, 690, vh=560)),
        card(f'<span class="H" style="font-size:52px;line-height:1.22;color:{INK};white-space:nowrap">It uses your own RRSP room.<br>'
             f'<span style="color:{COB}">For married or common-law couples.</span></span>', 1180, t=0.8, pad="32px 40px"),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        still("Last deposit? / *Then wait 3 years.*", 340, 112),
        svg(scaled(static(calendar(60, 10, 960)), 0.86, 700, vh=360)),
        follow(1130, t=0.15, size=80),
        stamp(840, 1450, 140, t=0.2),
    ]), tin="land", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.4, 3.8, 3.6, 2.6, 0.4))


# ============================================================================== covers
def cover_medical():
    """Loud big-number cover (style 1 look B: serif hook + soft-coral pill + drawn object + handwritten line + round stamp)."""
    return (f'<div class="par dots" style="position:absolute;inset:0"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:300px;text-align:center"><span class="tag">CANADA · MEDICAL EXPENSES</span></div>'
            f'<div class="H HL" style="position:absolute;left:40px;right:40px;top:390px;text-align:center;font-size:104px;white-space:nowrap">'
            f'Dentist, glasses, pills:<br><span class="em">$2,000 this year?</span></div>'
            f'<svg style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">'
            f'{scaled(receipt(230, 20, 620), 0.62, 720, vh=720)}</svg>'
            f'<div style="position:absolute;left:0;right:0;top:1200px;text-align:center;font-family:\'Caveat Brush\';font-size:64px;color:{DCORAL};'
            f'transform:rotate(-2deg);white-space:nowrap">claim them on the lower earner’s return</div>'
            f'<div style="position:absolute;left:0;right:0;top:1310px;text-align:center;font-family:\'DejaVu Sans Mono\';font-weight:700;'
            f'font-size:34px;letter-spacing:.03em;color:{COB}">LINE 33099 · YOU, PARTNER, KIDS UNDER 18</div>'
            + stamp(860, 1470, 110))


def cover_spousal():
    """Quiet follow-the-line cover (style 9): a coral line runs from the 2026 deposit, past two locked years, to 2029 TAKE OUT."""
    line = (f'<path d="M{150},{1160} C 300,1290 420,1040 560,1170 S 820,1290 930,1160" fill="none" stroke="{DCORAL}" stroke-width="12" '
            f'stroke-linecap="round" stroke-dasharray="2 24"/>')
    return (f'<div class="par dotsb" style="position:absolute;inset:0"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:300px;text-align:center"><span class="tag">CANADA · SPOUSAL RRSP</span></div>'
            f'<div class="H HL" style="position:absolute;left:40px;right:40px;top:390px;text-align:center;font-size:112px;white-space:nowrap">'
            f'Earn twice what<br><span class="em">your partner does?</span></div>'
            f'<svg style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">'
            f'{scaled(calendar(60, 10, 960), 0.86, 830, vh=360)}{line}</svg>'
            f'<div style="position:absolute;left:0;right:0;top:1270px;text-align:center;font-family:\'Caveat Brush\';font-size:58px;color:{DCORAL};'
            f'transform:rotate(-2deg);white-space:nowrap">wait 3 years after your last deposit</div>'
            + stamp(860, 1440, 120))


COVERS = {"ff-reel-1108-medical-one-return": cover_medical, "ff-reel-1109-spousal-rrsp-3yr": cover_spousal}
REELS = {
    "ff-reel-1108-medical-one-return": (medical, LIB / "ff-x-big-reveal.mp3"),
    "ff-reel-1109-spousal-rrsp-3yr": (spousal, LIB / "ff-x-money-moves.mp3"),
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
            ts = [0.0, 0.5, 1.0, 1.5, 2.2, 3.0, 3.6, 4.5, 5.5, 6.5, 7.2, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0]
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

#!/usr/bin/env python3
"""Nov 1 studio build, Fully Funded Reels (no trial flag). Desk order (Nov 1): Canadian rules with a partner, family or deadline at stake,
"Canada" on screen, opening on the felt moment, ONE drawn object doing the meaning (no pointing hand, no piggy bank, no table).
Extends studio/editorial/oct28_fullyfunded.py (imported, not edited) and the FF/motion kits (not edited).

  ff-reel-1101-common-law    Sun Nov 1 19:00  CANADA. Living together 12 continuous months = common-law for the CRA; tell the CRA by the end
                                              of the following month; benefits use family net income (yours + partner's). PART 1.
                                              Body: a drawn marital-status card; 12 month boxes fill, the tick jumps SINGLE -> COMMON-LAW.
                                              Cover: style 13 sticky-note list (quiet).
  ff-reel-1102-both-file     Mon Nov 2 19:00  CANADA. PART 2: to keep getting the Canada child benefit, you AND your spouse or common-law
                                              partner each file every year, by April 30, even with no income (CRA).
                                              Body: a drawn benefit card with two return rows; partner's row stays empty; PAYMENTS CAN STOP.
                                              Cover: style 1 Look B big-headline (loud).
  ff-reel-1103-poa-ontario   Tue Nov 3 19:00  ONTARIO, CANADA. Without an attorney for property, your family, including your spouse, cannot
                                              automatically step in to make financial decisions for you (ontario.ca). Free kit.
                                              Body: a drawn padlocked folder YOUR MONEY; a power-of-attorney key opens it.
                                              Cover: style 9 follow the line (quiet).

    python3 studio/editorial/nov01_fullyfunded.py <id> [--qa-only] [--cover-only]  < /dev/null
Outputs: media/studio-nov01/fullyfunded/<id>.mp4 + <id>-cover.jpg. Frames go to the scratch dir and are deleted after each encode.
"""
import argparse, io, json, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import oct28_fullyfunded as O  # noqa: E402  (helpers: lines, still, do_this, follow, timing, CSSX; kits via its imports)
from oct28_fullyfunded import (Reel, el, stamp, svg, path, txt, COB, INK, CORAL, SOFT, CREAM, DCORAL, GREEN,  # noqa: E402
                               lines, still, do_this, follow, timing, md)
from kit import reading_report, overflow_check, render_frames, encode, sheet, qa_times, probe, loudness, FONTS, BASE_CSS  # noqa: E402

SCR = Path("/tmp/claude-0/nov01-fullyfunded")
OUT = REPO / "media/studio-nov01/fullyfunded"
CSSX = O.CSSX + f"""
.part{{font-family:'Inter Display';font-weight:800;letter-spacing:-.03em;color:{COB}}}
.cobf .H{{color:#FFFFFF}}.cobf .H .em{{color:{INK}}}.cobf .save{{color:{SOFT}}}
.card{{display:inline-block;background:#fff;border:7px solid {INK};border-radius:28px;box-shadow:12px 12px 0 {INK};text-align:center}}
"""
LIB = REPO / "media/music/library/v4"


def card(inner, y, t=0.6, pad="30px 52px"):
    return el(f'<div class="card" style="padding:{pad}">{inner}</div>', "c", y, a="pop", t=t)


def static(svg_inner):
    """Final state of a drawn object, no entrance animation (end cards)."""
    return svg_inner.replace('data-a="', 'data-x="')


def scaled(svg_inner, s, dy, vh=700, vw=1080):
    """Nested svg (the page CSS sets transform-box on every svg child, so a <g transform> scales about its own centre)."""
    return (f'<svg x="{(1080 - vw * s) / 2:.0f}" y="{dy}" width="{vw * s:.0f}" height="{vh * s:.0f}" viewBox="0 0 {vw} {vh}" '
            f'overflow="visible">{svg_inner}</svg>')


def part2_line(y=520):
    return still("*Part 2* tomorrow, / 7 pm.", y, 120)


# ============================================================================== A. common-law at 12 months (Sun Nov 1, 7 pm)
def status_card(x=90, y=680, w=900, flip_t=1.15, fill_t0=0.15):
    """Drawn MARITAL STATUS card: 12 month boxes fill one by one, then the tick jumps from SINGLE to COMMON-LAW."""
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="640" rx="26" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="640" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="26" fill="{COB}" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x + 4}" y="{y + 66}" width="{w - 8}" height="44" fill="{COB}"/>',
         txt(x + w / 2, y + 74, "MARITAL STATUS", 56, "#FFFFFF", weight=700),
         txt(x + 50, y + 186, "MONTHS LIVING TOGETHER", 44, INK, "start", 700)]
    bw, gap = 58, 10
    x0 = x + (w - (12 * bw + 11 * gap)) / 2
    for i in range(12):
        bx = x0 + i * (bw + gap)
        o.append(f'<rect x="{bx:.0f}" y="{y + 210}" width="{bw}" height="{bw}" rx="10" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/>')
        o.append(f'<rect x="{bx + 6:.0f}" y="{y + 216}" width="{bw - 12}" height="{bw - 12}" rx="6" fill="{DCORAL}" '
                 f'data-a="pop" data-t="{fill_t0 + 0.07 * i:.2f}" data-d="0.18"/>')
    o.append(txt(x0 + 12 * bw + 11 * gap, y + 330, "12", 54, DCORAL, "end", 700, t=fill_t0 + 0.8))
    rows = [("SINGLE", y + 420), ("COMMON-LAW", y + 550)]
    for lab, ry in rows:
        o.append(f'<rect x="{x + 60}" y="{ry - 62}" width="84" height="84" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>')
        o.append(txt(x + 180, ry, lab, 62, INK, "start", 700))
    ys, yc = rows[0][1], rows[1][1]
    # SINGLE ticked at frame 0; at flip_t a white patch fades over it and the COMMON-LAW tick draws in coral
    o.append(path(f"M{x + 78},{ys - 22} l18,22 l36,-48", COB, 12))
    o.append(f'<rect x="{x + 66}" y="{ys - 56}" width="72" height="72" fill="#FFFFFF" data-a="fade" data-t="{flip_t:.2f}" data-d="0.15"/>')
    o.append(path(f"M{x + 78},{yc - 22} l18,22 l36,-48", DCORAL, 13, flip_t + 0.1, 0.25))
    return "".join(o)


def income_join(y=760):
    """Drawn: YOUR INCOME + THEIR INCOME drop into one FAMILY NET INCOME box (same card language)."""
    def box(x, w, lab, col, t, h=150, yy=y):
        return (f'<g data-a="drop" data-t="{t:.2f}" data-d="0.3"><rect x="{x + 12}" y="{yy + 14}" width="{w}" height="{h}" rx="22" fill="{INK}"/>'
                f'<rect x="{x}" y="{yy}" width="{w}" height="{h}" rx="22" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>'
                + txt(x + w / 2, yy + h / 2 + 18, lab, 50, col, weight=700) + "</g>")
    return (box(70, 420, "YOUR INCOME", COB, 0.3) + box(590, 420, "THEIR INCOME", DCORAL, 0.45)
            + txt(540, y + 100, "+", 90, INK, weight=700, t=0.55)
            + path(f"M280,{y + 175} C280,{y + 260} 540,{y + 230} 540,{y + 300}", INK, 8, 0.75, 0.3)
            + path(f"M800,{y + 175} C800,{y + 260} 540,{y + 230} 540,{y + 300}", INK, 8, 0.75, 0.3)
            + f'<g data-a="pop" data-t="1.0" data-d="0.3"><rect x="132" y="{y + 324}" width="840" height="170" rx="26" fill="{INK}"/>'
              f'<rect x="120" y="{y + 310}" width="840" height="170" rx="26" fill="{COB}" stroke="{INK}" stroke-width="7"/>'
            + txt(540, y + 415, "FAMILY NET INCOME", 60, "#FFFFFF", weight=700) + "</g>")


def common_law():
    r = Reel("ff-reel-1101-common-law", "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    # frame 0: the stakes hook (6 words); boxes fill 0.15-1.0 s, tick jumps at 1.15 s, plain line at 1.5 s. No stamp up top (UI zone).
    r.scene(4, "".join([
        '<div class="par dots"></div>',
        el('<span class="tag">CANADA · LIVING TOGETHER</span>', "c", 250, a="none"),
        still("Living with your partner / 12 months? / *You're common-law.*", 330, 90),
        svg(scaled(status_card(90, 10, 900, flip_t=1.15), 0.86, 690)),
        lines("In Canada, that counts / *even if you never married.*", 1290, t=1.5, gap=0.14, size=82),
    ]), cam="push", shake=(1.25, 0.2, 14))
    r.scene(6, "".join([
        '<div class="par dots"></div>',
        still("Your benefits now count / both your incomes, / *so they may drop.*", 260, 92),
        svg(income_join(700)),
        el('<span class="save" style="font-size:72px;white-space:nowrap">like the Canada child benefit</span>', "c", 1280, a="pop", t=1.2, r=-2),
    ]), tin="cut", cam="right")
    r.scene(7, "".join([
        do_this(400),
        still("Update your marital status / *in CRA My Account.*", 520, 96),
        card(f'<span class="H" style="font-size:68px;line-height:1.2;color:{INK};white-space:nowrap">Deadline: end of the month<br>'
             f'<span style="color:{DCORAL}">after you hit 12 months.</span></span>', 860, t=0.35, pad="40px 56px"),
        stamp(820, 1230, 160, t=0.6),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        part2_line(250),
        svg(scaled(static(status_card(90, 10, 900)), 0.72, 560)),
        follow(1100, t=0.15, size=80),
        stamp(840, 1320, 140, t=0.2),
    ]), tin="cut", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.4, 3.4, 3.6, 2.4, 0.4))

def ccb_card(x=90, y=660, w=900, x_t=0.8, h=560):
    """Drawn CANADA CHILD BENEFIT card: YOUR TAX RETURN gets a tick; YOUR PARTNER'S stays empty and gets a coral X."""
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="26" fill="{COB}" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x + 4}" y="{y + 66}" width="{w - 8}" height="44" fill="{COB}"/>',
         txt(x + w / 2, y + 74, "CANADA CHILD BENEFIT", 54, "#FFFFFF", weight=700)]
    rows = [("YOUR TAX RETURN", y + 250), ("YOUR PARTNER'S", y + 430)]
    for lab, ry in rows:
        o.append(f'<rect x="{x + 60}" y="{ry - 62}" width="84" height="84" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>')
        o.append(txt(x + 180, ry, lab, 60, INK, "start", 700))
    o.append(path(f"M{x + 78},{rows[0][1] - 22} l18,22 l36,-48", GREEN, 13, 0.25, 0.25))
    yb = rows[1][1]
    o.append(path(f"M{x + 80},{yb - 44} l44,44 M{x + 124},{yb - 44} l-44,44", DCORAL, 13, x_t, 0.2))
    return "".join(o)


def calendar_page(x=300, y=700, w=480, t=0.3):
    h = int(w * 1.05)
    return (f'<g data-a="drop" data-t="{t:.2f}" data-d="0.35"><rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="28" fill="{INK}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="28" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="140" rx="28" fill="{DCORAL}" stroke="{INK}" stroke-width="7"/>'
            f'<rect x="{x + 4}" y="{y + 90}" width="{w - 8}" height="50" fill="{DCORAL}"/>'
            + txt(x + w / 2, y + 100, "APRIL", 70, "#FFFFFF", weight=700)
            + f'<text x="{x + w / 2}" y="{y + 400}" font-size="270" fill="{INK}" text-anchor="middle" '
              f'style="font-family:Inter Display" font-weight="800">30</text>'
            + txt(x + w / 2, y + h - 34, "EVERY YEAR", 46, COB, weight=700) + "</g>")


def both_file():
    r = Reel("ff-reel-1102-both-file", "fullyfunded", bpm=95, css=CSSX, stage="#F3F5FF")
    r.scene(4, "".join([
        '<div class="par dotsb"></div>',
        el('<span class="tag">CANADA · PART 2</span>', "c", 250, a="none"),
        still("Partner didn't file / *a tax return?*", 340, 110),
        svg(ccb_card(90, 620, 900, x_t=0.75)),
        el('<span class="stampx" style="font-size:76px;white-space:nowrap">PAYMENTS CAN STOP</span>', "c", 1215, a="stamp", t=1.05, d=0.3, r=-4),
        lines("To keep your benefits, you each / *file your own return every year.*", 1380, t=1.5, gap=0.14, size=72),
    ]), cam="push", shake=(1.1, 0.22, 16))
    r.scene(6, "".join([
        '<div class="par dotsb"></div>',
        still("Even with *no income.* / File by *April 30.*", 300, 100),
        svg(calendar_page(300, 600, 480, t=0.2)),
        el('<span class="save" style="font-size:62px;white-space:nowrap">late? payments can stop for a while</span>', "c", 1200, a="pop", t=1.0, r=-2),
    ]), tin="cut", cam="right")
    r.scene(7, "".join([
        do_this(400),
        still("Both of you: file / *by April 30, 2027.*", 520, 104),
        card(f'<span class="H" style="font-size:70px;line-height:1.2;color:{INK};white-space:nowrap">Earned $0 this year?<br>'
             f'<span style="color:{COB}">Still file a return.</span></span>', 860, t=0.35, pad="40px 56px"),
        stamp(820, 1230, 160, t=0.6),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        still("Two returns, / *every year.*", 240, 116),
        svg(static(calendar_page(300, 540, 480))),
        follow(1110, t=0.15, size=80),
    ]), tin="cut", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.5, 3.2, 3.4, 2.3, 0.4))

def folder(x=140, y=680, w=800, open_t=None, t_lock=None):
    """Drawn folder YOUR MONEY (BANK · BILLS · HOME) held shut by a padlock; with open_t the shackle lifts open."""
    h = 560
    o = [f'<path d="M{x + 14},{y + 76} l0,{h - 60} l{w},0 l0,{-(h - 60)} z" fill="{INK}"/>',
         f'<path d="M{x},{y + 40} l0,-40 l280,0 l40,40 z" fill="{SOFT}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>',
         f'<rect x="{x}" y="{y + 40}" width="{w}" height="{h - 40}" rx="22" fill="#FFE7DC" stroke="{INK}" stroke-width="7"/>',
         txt(x + 50, y + 150, "YOUR MONEY", 66, INK, "start", 700),
         txt(x + 50, y + 226, "BANK · BILLS · HOME", 44, COB, "start", 700)]
    lx, ly = x + w * 0.85, y + 390
    shackle = f'<path d="M{lx - 60},{ly} L{lx - 60},{ly - 70} A60,60 0 0 1 {lx + 60},{ly - 70} L{lx + 60},{ly}" fill="none" stroke="{INK}" stroke-width="22"/>'
    a = f' data-a="pop" data-t="{t_lock:.2f}" data-d="0.3"' if t_lock is not None else ""
    body = (f'<rect x="{lx - 100}" y="{ly - 10}" width="200" height="170" rx="26" fill="{{c}}" stroke="{INK}" stroke-width="7"/>'
            f'<circle cx="{lx}" cy="{ly + 60}" r="20" fill="{INK}"/><rect x="{lx - 8}" y="{ly + 60}" width="16" height="50" fill="{INK}"/>')
    o.append(f'<g{a}>{shackle}{body.format(c=DCORAL)}</g>')
    if open_t is not None:
        # unlock: a folder-coloured patch fades over the closed shackle, the open shackle draws in green, the lock body turns green
        o.append(f'<rect x="{lx - 80}" y="{ly - 145}" width="160" height="136" fill="#FFE7DC" data-a="fade" data-t="{open_t:.2f}" data-d="0.12"/>')
        o.append(path(f"M{lx + 60},{ly - 10} L{lx + 60},{ly - 150} A60,60 0 0 0 {lx - 60},{ly - 150} L{lx - 60},{ly - 110}",
                      GREEN, 22, open_t + 0.08, 0.3))
        o.append(f'<g data-a="fade" data-t="{open_t + 0.1:.2f}" data-d="0.15">{body.format(c=GREEN)}</g>')
        o.append(f'<g data-a="pop" data-t="{open_t + 0.35:.2f}" data-d="0.3"><rect x="{x + 25}" y="{y + 290}" width="400" height="200" rx="18" '
                 f'fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
                 + path(f"M{x + 80},{y + 450} c20,-30 40,-30 40,0 s30,-30 50,-10 s30,10 60,-20", COB, 5)
                 + txt(x + 215, y + 352, "CONTINUING", 44, COB, weight=700) + txt(x + 215, y + 404, "PROPERTY POA", 44, COB, weight=700) + "</g>")
    return "".join(o)


def poa():
    r = Reel("ff-reel-1103-poa-ontario", "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    r.scene(4, "".join([
        '<div class="par dots"></div>',
        el('<span class="tag">ONTARIO, CANADA</span>', "c", 250, a="none"),
        still("Too sick to make / decisions? / *Who pays your bills?*", 330, 100),
        svg(scaled(folder(140, 10, 800, t_lock=0.35), 0.82, 735, vh=600)),
        lines("Without a power of attorney, / your spouse can't automatically / *manage your money.*", 1235, t=1.3, gap=0.16, size=76),
    ]), cam="push", shake=(0.45, 0.2, 14))
    r.scene(6, "".join([
        '<div class="par dots"></div>',
        still("Your family may have to / *go to court* first.", 300, 96),
        svg(folder(140, 620, 800)),
        el('<span class="stampx" style="font-size:60px;white-space:nowrap;line-height:1.1;text-align:center">COURT-APPOINTED<br>GUARDIAN</span>', "c", 1215, a="stamp", t=0.6, d=0.3, r=-3),
    ]), tin="cut", cam="right")
    r.scene(7, "".join([
        do_this(250),
        still("Sign a *continuing* power / of attorney for property.", 360, 86),
        svg(folder(140, 640, 800, open_t=0.5)),
        el('<span class="save" style="font-size:70px;white-space:nowrap;line-height:1.1">Ontario’s free kit · 2 witnesses</span>', "c", 1250, a="pop", t=0.9, r=-2),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        still("Name who manages / *your money.*", 240, 110),
        svg(scaled(static(folder(140, 10, 800, open_t=0.0)), 0.8, 630)),
        follow(1140, t=0.15, size=80),
    ]), tin="cut", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.6, 3.1, 3.5, 2.3, 0.4))

def cover_common_law():
    """Style 13 sticky-note list (quiet): lined note card, red margin line, tape strip, on cobalt; serif headline + one handwritten line."""
    return (f'<div style="position:absolute;inset:0;background:{COB}"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:310px;text-align:center"><span class="tag" style="background:#fff;color:#2B3FE0">CANADA · COUPLES</span></div>'
            f'<div style="position:absolute;left:110px;width:860px;top:430px;height:930px;transform:rotate(-1.5deg);background:'
            f'repeating-linear-gradient(#FFFDF6 0 86px,#C9D2FF 86px 89px);border-radius:10px;box-shadow:18px 20px 0 rgba(14,20,64,.45)">'
            '<div style="position:absolute;left:88px;top:0;bottom:0;width:4px;background:#E0464C"></div>'
            '<div style="position:absolute;left:330px;top:-34px;width:200px;height:66px;background:rgba(255,176,143,.85);transform:rotate(3deg)"></div>'
            f'<div class="H HL" style="position:absolute;left:120px;right:30px;top:80px;font-size:94px;white-space:nowrap">'
            f'Living with<br>your partner<br>12 months?<br><span class="em">You’re<br>common-law.</span></div>'
            f'<div style="position:absolute;left:130px;top:700px;font-family:\'Caveat Brush\';font-size:66px;line-height:1.15;color:{DCORAL};'
            f'white-space:nowrap;transform:rotate(-2deg)">tell the CRA by the end<br>of the following month</div></div>'
            + stamp(860, 1440, 120))


def cover_both_file():
    """Style 1 Look B big-headline (loud): Fraunces ink hook + pill, drawn object, handwritten line + arrow, round stamp, on soft coral."""
    return (f'<div style="position:absolute;inset:0;background:{SOFT}"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:300px;text-align:center"><span class="tag">CANADA · PART 2</span></div>'
            f'<div class="H HL" style="position:absolute;left:40px;right:40px;top:390px;text-align:center;font-size:132px;white-space:nowrap">'
            f'No income?<br><span class="em" style="background:#FFFFFF">Still file.</span></div>'
            f'<svg style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">{ccb_card(150, 760, 780, h=500).replace("data-a", "data-x")}</svg>'
            f'<div style="position:absolute;left:150px;top:1290px;font-family:\'Caveat Brush\';font-size:78px;color:{DCORAL};transform:rotate(-3deg);white-space:nowrap">'
            'both of you, by April 30</div>'
            + stamp(860, 1480, 120))


def cover_poa():
    """Style 9 follow the line (quiet): one coral line down the page through three stops, ending on a blue dot ('unless you name them')."""
    pts = [(200, 790), (250, 950), (200, 1110), (250, 1280)]
    d = f"M{pts[0][0]},{pts[0][1]} " + " ".join(f"S{(a[0] + b[0]) / 2 + (60 if k % 2 else -60):.0f},{(a[1] + b[1]) / 2:.0f} {b[0]},{b[1]}"
                                                 for k, (a, b) in enumerate(zip(pts, pts[1:])))
    labs = [("if illness or an accident", "leaves you unable to decide"), ("no continuing power", "of attorney for property"), ("your spouse may need court",)]
    lab = "".join(f'<text x="{x + 70}" y="{y + 20 - 30 * (len(s) - 1)}" font-size="60" fill="{INK}" style="font-family:Caveat" font-weight="700">'
                  + "".join(f'<tspan x="{x + 70}" dy="{0 if k == 0 else 60}">{t}</tspan>' for k, t in enumerate(s)) + "</text>"
                  for s, (x, y) in zip(labs, pts))
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="24" fill="{DCORAL}" stroke="{INK}" stroke-width="5"/>' for x, y in pts[:3])
    return (f'<div class="par dots" style="position:absolute;inset:0"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:300px;text-align:center"><span class="tag">ONTARIO, CANADA</span></div>'
            f'<div class="H HL" style="position:absolute;left:40px;right:40px;top:380px;text-align:center;font-size:120px;white-space:nowrap">'
            f'Your spouse can’t<br><span class="em">just step in.</span></div>'
            f'<svg style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">'
            f'<path d="{d}" fill="none" stroke="{DCORAL}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>{dots}'
            f'<circle cx="250" cy="1280" r="38" fill="{COB}" stroke="{INK}" stroke-width="6"/>{lab}'
            f'<text x="320" y="1305" font-size="80" fill="{COB}" style="font-family:Caveat Brush">unless you name them</text></svg>'
            + stamp(880, 1460, 110))


COVERS = {"ff-reel-1101-common-law": cover_common_law, "ff-reel-1102-both-file": cover_both_file, "ff-reel-1103-poa-ontario": cover_poa}
REELS = {
    "ff-reel-1101-common-law": (common_law, LIB / "ff-x-big-reveal.mp3"),
    "ff-reel-1102-both-file": (both_file, LIB / "ff-x-level-up.mp3"),
    "ff-reel-1103-poa-ontario": (poa, LIB / "ff-x-money-moves.mp3"),
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
    chrome = O._glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")[0]
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
            shutil.rmtree(w, ignore_errors=True)
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

#!/usr/bin/env python3
"""Nov 2 studio build, Fully Funded Reels (no trial flag, standalone, no Part 2). Desk order (Nov 2): HOLD topic changes; stay on Canadian
partner/estate/family rules, felt moment on frame 0, "Canada" on screen, ONE drawn object doing the meaning, no penalty-fact opens.
Extends studio/editorial/nov01_fullyfunded.py (imported, not edited) and the FF/motion kits (not edited).

  ff-reel-1104-resp-sin       Wed Nov 4 19:00  CANADA. The RESP grant (CESG) adds 20% on the first $2,500 a year ($20 per $100,
                                               up to $500 a year, $7,200 lifetime), and you need the child's SIN (ESDC). Apply for the
                                               SIN when you register the birth (canada.ca). Body: a drawn BABY'S RESP card; a +$20 coin
                                               drops in, the empty SIN boxes get circled. Cover: style 8 original template big-number (quiet).
  ff-reel-1105-pension-split  Thu Nov 5 19:00  CANADA. Couples can allocate up to 50% of eligible pension income to the spouse on form
                                               T1032, signed and attached to both returns; RRIF income only from 65; CPP/OAS don't count
                                               (CRA). Body: a drawn PENSION cheque cut down the middle; half slides to the other parent.
                                               Cover: style 1 Look B big-headline (loud).

    python3 studio/editorial/nov02_fullyfunded.py <id> [--qa-only] [--cover-only]  < /dev/null
Outputs: media/studio-nov02/fullyfunded/<id>.mp4 + <id>-cover.jpg. Frames go to the scratch dir and are deleted after each encode.
"""
import argparse, io, json, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import nov01_fullyfunded as N  # noqa: E402
from nov01_fullyfunded import (Reel, el, stamp, svg, path, txt, COB, INK, SOFT, CREAM, DCORAL, GREEN,  # noqa: E402
                               lines, still, do_this, follow, timing, card, static, scaled)
from kit import reading_report, overflow_check, render_frames, encode, probe, loudness, FONTS, BASE_CSS  # noqa: E402

N.SCR = SCR = Path("/tmp/claude-0/nov02-fullyfunded")
OUT = REPO / "media/studio-nov02/fullyfunded"
CSSX = N.CSSX
LIB = REPO / "media/music/library/v4"

# ------------------------------------------------------------------------------------------------ FACTS (checked Nov 2 2026)
# ESDC 'It pays to plan for a child's education': "You and the child need a Social Insurance Number (SIN) to open an RESP."
#   CESG "provides 20% on the first $2,500 in annual personal contributions to an RESP", up to $500/yr; lifetime max $7,200.
# CRA 'Canada Education Savings Grant (CESG)' (modified 2026-10-29): 20% basic, max $500 a year ($1,000 with unused room),
#   lifetime $7,200, unused room carried forward, grants to the end of the year the child turns 17.
# canada.ca 'Register your child's birth' (2025-11-18): "In all provinces, you can apply for your child's Social Insurance Number
#   (SIN) when you register your child's birth." Territories: apply through Service Canada.
SAVE, RATE = 100, 0.20
assert round(SAVE * RATE) == 20 and round(2500 * RATE) == 500
# CRA 'Pension income splitting' (2026-01-20): "You can allocate up to 50% of your eligible pension income to your spouse or common-law
#   partner"; RRIF/annuity amounts qualify if the transferring spouse is 65+ at year end; OAS and CPP/QPP are not eligible;
#   T1032 "must be completed, signed and attached to both" returns by the filing due date.


def sin_boxes(x, y, filled=False, t=None):
    o = []
    for k in range(3):
        bx = x + k * 118
        o.append(f'<rect x="{bx}" y="{y - 60}" width="100" height="78" rx="12" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>')
        if filled:
            o.append(txt(bx + 50, y - 6, "•••", 44, INK, weight=700, t=t))
    return "".join(o)


# ============================================================================== A. RESP grant needs the child's SIN (Wed Nov 4, 7 pm)
def resp_card(x=90, y=0, w=900, save="$100", add="+$20", coin_t=0.35, ring_t=1.2, filled=False, count=None, save_lab="YOU SAVE"):
    """Drawn BABY'S RESP card: YOU SAVE / CANADA ADDS (a coral coin drops in) / BABY'S SIN (three empty boxes, circled in coral)."""
    h = 600
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="26" fill="{COB}" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x + 4}" y="{y + 66}" width="{w - 8}" height="44" fill="{COB}"/>',
         txt(x + w / 2, y + 74, "BABY'S RESP", 58, "#FFFFFF", weight=700)]
    r1, r2, r3 = y + 225, y + 375, y + 525
    for ry in (r1 + 52, r2 + 52):
        o.append(f'<line x1="{x + 40}" y1="{ry}" x2="{x + w - 40}" y2="{ry}" stroke="{INK}" stroke-opacity=".18" stroke-width="4" stroke-dasharray="14 12"/>')
    o.append(txt(x + 50, r1, save_lab, 54, INK, "start", 700))
    o.append(txt(x + 50, r2, "CANADA ADDS", 54, INK, "start", 700))
    o.append(txt(x + 50, r3, "BABY'S SIN", 54, INK, "start", 700))
    if count:
        (a0, a1), (b0, b1) = count
        o.append(f'<text x="{x + w - 50}" y="{r1 + 6}" font-size="84" fill="{COB}" text-anchor="end" style="font-family:Inter Display" '
                 f'font-weight="800" data-a="count" data-from="{a0}" data-to="{a1}" data-pre="$" data-comma="1" data-t="0.25" data-d="0.9">${a0}</text>')
    else:
        o.append(f'<text x="{x + w - 50}" y="{r1 + 6}" font-size="84" fill="{COB}" text-anchor="end" style="font-family:Inter Display" '
                 f'font-weight="800">{save}</text>')
    # the coin: a coral disc carrying the grant, drops onto the CANADA ADDS row
    cx, cy = x + w - 150, r2 - 20
    ca = f' data-a="drop" data-t="{coin_t:.2f}" data-d="0.45"' if coin_t is not None else ""
    lab = (f'<text x="{cx}" y="{cy + 22}" font-size="{50 if (count or len(add) > 4) else 64}" fill="#FFFFFF" text-anchor="middle" style="font-family:Inter Display" '
           f'font-weight="800"' + (f' data-a="count" data-from="{b0}" data-to="{b1}" data-pre="+$" data-comma="1" data-t="0.25" data-d="0.9">+${b0}'
                                   if count else f'>{add}') + '</text>')
    o.append(f'<g{ca}><circle cx="{cx + 8}" cy="{cy + 10}" r="98" fill="{INK}"/><circle cx="{cx}" cy="{cy}" r="98" fill="{DCORAL}" '
             f'stroke="{INK}" stroke-width="7"/><circle cx="{cx}" cy="{cy}" r="78" fill="none" stroke="#FFFFFF" stroke-opacity=".55" '
             f'stroke-width="4" stroke-dasharray="8 10"/>{lab}</g>')
    bx = x + w - 50 - (3 * 100 + 2 * 18)
    o.append(sin_boxes(bx, r3 + 8, filled=filled))
    if filled:
        o.append(path(f"M{bx - 80},{r3 - 18} l18,22 l36,-48", GREEN, 13))
    elif ring_t is not None:
        o.append(f'<rect x="{bx - 22}" y="{r3 - 74}" width="{3 * 100 + 2 * 18 + 44}" height="106" rx="30" fill="none" stroke="{DCORAL}" '
                 f'stroke-width="9" data-a="draw" data-t="{ring_t:.2f}" data-d="0.35"/>')
    return "".join(o)


def birth_form(x=90, y=0, w=900, h=520, tick_t=None):
    """Drawn BIRTH REGISTRATION form: name and date lines, and the box 'ALSO APPLY FOR BABY'S SIN' that gets ticked."""
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="26" fill="{DCORAL}" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x + 4}" y="{y + 66}" width="{w - 8}" height="44" fill="{DCORAL}"/>',
         txt(x + w / 2, y + 74, "BIRTH REGISTRATION", 56, "#FFFFFF", weight=700)]
    for k, lab in enumerate(("BABY'S NAME", "DATE OF BIRTH")):
        ry = y + 200 + k * 100
        o.append(txt(x + 50, ry, lab, 44, INK, "start", 700))
        o.append(f'<line x1="{x + 470}" y1="{ry + 8}" x2="{x + w - 50}" y2="{ry + 8}" stroke="{INK}" stroke-width="4"/>')
    by = y + 430
    o.append(f'<rect x="{x + 50}" y="{by - 62}" width="84" height="84" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>')
    o.append(txt(x + 165, by, "ALSO APPLY FOR A SIN", 46, COB, "start", 700))
    o.append(path(f"M{x + 68},{by - 22} l18,22 l36,-48", GREEN, 13, tick_t, 0.3) if tick_t is not None
             else path(f"M{x + 68},{by - 22} l18,22 l36,-48", GREEN, 13))
    return "".join(o)


def resp_sin():
    r = Reel("ff-reel-1104-resp-sin", "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    # frame 0: the felt moment (tag NEW BABY + the drawn baby's account) + a number you can picture; coin drops 0.35 s,
    # empty SIN boxes circled 1.2 s, plain payoff line 1.5 s. Gate r2: layout centred, RESP explained once.
    r.scene(4, "".join([
        '<div class="par dots"></div>',
        el('<span class="tag" style="font-size:44px">CANADA · NEW BABY</span>', "c", 270, a="none"),
        still("Save $100. / *Canada adds $20.*", 360, 112),
        el('<span class="save" style="font-size:64px;white-space:nowrap">RESP: a savings plan for school</span>', "c", 650, a="none", r=-2),
        svg(scaled(resp_card(90, 10, 900, coin_t=0.35, ring_t=1.2), 0.78, 750, vh=640)),
        lines("But the grant needs / *your baby's SIN.*", 1290, t=1.5, gap=0.14, size=84),
    ]), cam="push", shake=(0.75, 0.2, 14))
    r.scene(6, "".join([
        '<div class="par dots"></div>',
        still("Up to *$500 a year,* / $7,200 lifetime max.", 300, 96),
        svg(scaled(resp_card(90, 10, 900, save="$2,500", add="+$500", coin_t=0.3, ring_t=None, filled=True, save_lab="SAVE A YEAR"), 0.78, 590, vh=640)),
        el('<span class="save" style="font-size:56px;white-space:nowrap">save $2,500 a year → Canada adds $500</span>',
           "c", 1120, a="pop", t=0.9, r=-2),
        lines("For kids living in Canada, / until the year they turn 17.", 1230, t=1.3, gap=0.14, size=64),
    ]), tin="cut", cam="right")
    r.scene(7, "".join([
        do_this(290),
        still("Get baby's SIN / *with the birth registration.*", 390, 88),
        svg(scaled(birth_form(90, 10, 900, tick_t=0.45), 0.84, 680, vh=560)),
        card(f'<span class="H" style="font-size:66px;line-height:1.2;color:{INK};white-space:nowrap">Then open an RESP.<br>'
             f'<span style="color:{COB}">Bring your SIN too.</span></span>', 1190, t=0.8, pad="34px 52px"),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        still("No SIN, / *no grant.*", 320, 120),
        svg(scaled(static(resp_card(90, 10, 900, coin_t=None, ring_t=None, filled=True, save="$100")), 0.72, 640, vh=640)),
        follow(1170, t=0.15, size=80),
        stamp(840, 1390, 140, t=0.2),
    ]), tin="cut", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.5, 3.6, 3.6, 2.5, 0.4))


# ============================================================================== B. pension splitting (Thu Nov 5, 7 pm)
def cheque(x=90, y=0, w=900, h=420, cut_t=None, split=False, slide_t=None, labels=True):
    """Drawn PENSION cheque. With cut_t a dotted cut draws down the middle; with slide_t the right half slides away to 'the other' parent."""
    half = w / 2
    def body(x0, ww, side):
        o = [f'<rect x="{x0 + 12}" y="{y + 14}" width="{ww}" height="{h}" rx="22" fill="{INK}"/>',
             f'<rect x="{x0}" y="{y}" width="{ww}" height="{h}" rx="22" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
             f'<rect x="{x0}" y="{y}" width="{ww}" height="96" rx="22" fill="{COB}" stroke="{INK}" stroke-width="7"/>',
             f'<rect x="{x0 + 4}" y="{y + 60}" width="{ww - 8}" height="36" fill="{COB}"/>']
        return "".join(o)
    o = []
    if not split:
        o.append(body(x, w, "all"))
        o.append(txt(x + w / 2, y + 66, "PENSION", 56, "#FFFFFF", weight=700))
        o.append(f'<text x="{x + w / 2}" y="{y + 290}" font-size="200" fill="{INK}" text-anchor="middle" style="font-family:Inter Display" '
                 f'font-weight="800">100%</text>')
        o.append(path(f"M{x + 60},{y + h - 50} c30,-36 60,-36 60,0 s40,-36 70,-12 s40,12 80,-24", COB, 6))
        if cut_t is not None:
            o.append(f'<path d="M{x + half},{y - 40} L{x + half},{y + h + 40}" stroke="{DCORAL}" stroke-width="10" stroke-dasharray="26 18" '
                     f'fill="none" data-a="draw" data-t="{cut_t:.2f}" data-d="0.35"/>')
        return "".join(o)
    # split state: two halves, 50% each; the right half arrives from the left (slides over to the other parent)
    gap = 60
    lw = half - gap / 2
    left = (body(x, lw, "l") + txt(x + lw / 2, y + 66, "PENSION", 50, "#FFFFFF", weight=700)
            + f'<text x="{x + lw / 2}" y="{y + 290}" font-size="150" fill="{INK}" text-anchor="middle" style="font-family:Inter Display" font-weight="800">50%</text>')
    rx = x + half + gap / 2
    right = (body(rx, lw, "r") + txt(rx + lw / 2, y + 66, "PENSION", 50, "#FFFFFF", weight=700)
             + f'<text x="{rx + lw / 2}" y="{y + 290}" font-size="150" fill="{DCORAL}" text-anchor="middle" style="font-family:Inter Display" font-weight="800">50%</text>')
    sa = f' data-a="right" data-t="{slide_t:.2f}" data-d="0.45"' if slide_t is not None else ""
    o.append(left)
    o.append(f'<g{sa}>{right}</g>')
    if labels:
        o.append(txt(x + lw / 2, y + h + 100, "ONE SPOUSE", 58, INK, weight=700))
        o.append(txt(rx + lw / 2, y + h + 100, "THE OTHER", 58, DCORAL, weight=700, t=(slide_t + 0.3) if slide_t is not None else None))
    return "".join(o)


def t1032(x=90, y=0, w=900, h=520, sig_t=None):
    """Drawn FORM T1032 with two signature lines; with sig_t both signatures draw in, one after the other."""
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="26" fill="{COB}" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x + 4}" y="{y + 66}" width="{w - 8}" height="44" fill="{COB}"/>',
         txt(x + w / 2, y + 74, "FORM T1032", 58, "#FFFFFF", weight=700),
         txt(x + w / 2, y + 170, "JOINT ELECTION TO SPLIT", 40, INK, weight=700),
         txt(x + w / 2, y + 218, "PENSION INCOME", 40, INK, weight=700)]
    for k, lab in enumerate(("SPOUSE 1", "SPOUSE 2")):
        ry = y + 330 + k * 120
        o.append(txt(x + 50, ry, lab, 44, INK, "start", 700))
        o.append(f'<line x1="{x + 330}" y1="{ry + 8}" x2="{x + w - 50}" y2="{ry + 8}" stroke="{INK}" stroke-width="4"/>')
        sx = x + 360
        d = f"M{sx},{ry - 4} c20,-46 46,-46 40,0 s30,-40 60,-12 s36,14 70,-26 s40,10 80,-6 s30,-20 60,4"
        st = (sig_t + 0.45 * k) if sig_t is not None else None
        o.append(path(d, DCORAL if k else COB, 7, st, 0.4))
    return "".join(o)


def pension_split():
    r = Reel("ff-reel-1105-pension-split", "fullyfunded", bpm=95, css=CSSX, stage="#F3F5FF")
    # frame 0: felt moment + payoff in the hook; whole PENSION cheque; cut draws 0.5 s; plain payoff 1.4 s. Gate r2: couples, centred.
    r.scene(4, "".join([
        '<div class="par dotsb"></div>',
        el('<span class="tag" style="font-size:42px">CANADA · RETIRED COUPLES</span>', "c", 280, a="none"),
        still("One pension? / *Split it. Pay less tax?*", 370, 108),
        svg(scaled(cheque(90, 10, 900, cut_t=0.5), 0.86, 720, vh=560)),
        lines("In Canada, a couple can split it / *on their tax returns.*", 1260, t=1.4, gap=0.14, size=76),
    ]), cam="push", shake=(0.85, 0.2, 12))
    r.scene(6, "".join([
        '<div class="par dotsb"></div>',
        still("Up to *half* can move / to the other spouse.", 300, 98),
        svg(scaled(cheque(90, 10, 900, split=True, slide_t=0.2), 0.82, 600, vh=560)),
        el('<span class="save" style="font-size:66px;white-space:nowrap;line-height:1.15">their total tax can drop</span>',
           "c", 1080, a="pop", t=0.9, r=-2),
        lines("For couples, married or common-law, / *not separated.*", 1200, t=1.3, gap=0.14, size=64),
    ]), tin="cut", cam="right")
    r.scene(7, "".join([
        do_this(290),
        still("Both sign form T1032 / *at tax time.*", 390, 96),
        svg(scaled(t1032(90, 10, 900, sig_t=0.4), 0.84, 660, vh=560)),
        card(f'<span class="H" style="font-size:64px;line-height:1.2;color:{INK};white-space:nowrap">Workplace pension: counts.<br>'
             f'<span style="color:{COB}">CPP and OAS: don’t.</span></span>', 1190, t=1.3, pad="34px 48px"),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        still("Send this to / *your parents.*", 320, 116),
        svg(scaled(static(cheque(90, 10, 900, split=True, labels=False)), 0.72, 640, vh=560)),
        follow(1150, t=0.15, size=80),
        stamp(840, 1390, 140, t=0.2),
    ]), tin="cut", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.5, 3.6, 3.6, 2.5, 0.4))


# ============================================================================== covers
def cover_resp():
    """Style 8 original simple template, big-number (quiet): one giant '+$20' over a small '$100 saved' line, hook + handwritten catch."""
    return (f'<div class="par dots" style="position:absolute;inset:0"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:300px;text-align:center"><span class="tag">CANADA · NEW BABY</span></div>'
            f'<div class="H HL" style="position:absolute;left:40px;right:40px;top:390px;text-align:center;font-size:104px;white-space:nowrap">'
            f'Save $100 for baby.<br><span class="em">Canada adds:</span></div>'
            f'<div style="position:absolute;left:0;right:0;top:690px;text-align:center;font-family:\'Inter Display\';font-weight:800;'
            f'font-size:330px;line-height:1;letter-spacing:-.05em;color:{DCORAL}">+$20</div>'
            f'<div style="position:absolute;left:0;right:0;top:1100px;text-align:center;font-family:\'DejaVu Sans Mono\';font-weight:700;'
            f'font-size:42px;letter-spacing:.03em;color:{COB}">RESP GRANT · UP TO $500 A YEAR</div>'
            f'<div style="position:absolute;left:0;right:0;top:1200px;text-align:center;font-family:\'Caveat Brush\';font-size:84px;color:{DCORAL};'
            f'transform:rotate(-2deg)">only with baby’s SIN</div>'
            + stamp(870, 1470, 110))


def cover_pension():
    """Style 1 Look B big-headline (loud): Fraunces ink hook + white pill, drawn split cheque, handwritten line, round stamp, on soft cobalt."""
    return (f'<div style="position:absolute;inset:0;background:#C9D2FF"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:300px;text-align:center"><span class="tag">CANADA · RETIRED COUPLES</span></div>'
            f'<div class="H HL" style="position:absolute;left:40px;right:40px;top:390px;text-align:center;font-size:124px;white-space:nowrap">'
            f'One pension?<br><span class="em" style="background:#FFFFFF">Split up to half.</span></div>'
            f'<svg style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">'
            f'{scaled(cheque(90, 10, 900, split=True), 0.86, 760, vh=560)}</svg>'
            f'<div style="position:absolute;left:0;right:0;top:1300px;text-align:center;font-family:\'Caveat Brush\';font-size:64px;color:{DCORAL};'
            f'transform:rotate(-2deg);white-space:nowrap">married or common-law · form T1032</div>'
            + stamp(870, 1480, 110))


COVERS = {"ff-reel-1104-resp-sin": cover_resp, "ff-reel-1105-pension-split": cover_pension}
REELS = {
    "ff-reel-1104-resp-sin": (resp_sin, LIB / "ff-x-level-up.mp3"),
    "ff-reel-1105-pension-split": (pension_split, LIB / "ff-x-big-reveal.mp3"),
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

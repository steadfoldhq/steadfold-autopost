#!/usr/bin/env python3
"""Nov 5 studio build, Fully Funded Reel (no trial flag, standalone, no Part 2, no on-screen send line: send_test false).
Desk (Nov 5): ONE picture + ONE number in frame 0, <=2 text blocks; detail lines from second 2; a scene composition different from
FF's last 3 Reels (those: centred tag pill + centred serif + white offset card, then cobalt do-this / follow cards) and a cover style
different from the last 2 FF Reel covers (Look B big-number, follow the line) and not the taped note.
Extends studio/editorial/nov04_fullyfunded.py / nov01_fullyfunded.py (imported, not edited).

  ff-reel-1110-donations-one-return  Tue Nov 10 19:00  CANADA. Charity receipts: you can claim your spouse's or common-law
        partner's donations (CRA line 34900 'Who can claim'); only the first $200 of a claim gets the lowest federal rate (Finance
        Canada: 14% in 2026), the rest 29% (33% only on income in the top bracket). Two $200 claims = $56 off federal tax;
        one $400 claim = $86. Composition: ONE drawn glass JAR of coins on a soft-coral field, left-aligned type, the camera
        glides between beats; coins pour from the partner's jar into yours. Cover: style 7 'Instead of… / Try…' reframe (quiet).

    python3 studio/editorial/nov05_fullyfunded.py <id> [--qa-only] [--cover-only]  < /dev/null
Outputs: media/studio-nov05/fullyfunded/<id>.mp4 + <id>-cover.jpg. Frames go to the scratch dir and are deleted after each encode.
"""
import argparse, json, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import nov01_fullyfunded as N  # noqa: E402
from nov01_fullyfunded import (Reel, el, stamp, svg, path, txt, COB, INK, SOFT, CREAM, DCORAL, md, static)  # noqa: E402
from kit import reading_report, overflow_check, render_frames, encode, probe, loudness  # noqa: E402

N.SCR = SCR = Path("/tmp/claude-0/nov05-fullyfunded")
OUT = REPO / "media/studio-nov05/fullyfunded"
LIB = REPO / "media/music/library/v4"
FIELD = "#FCD9CB"          # soft coral field (FF palette: soft coral family), new for FF Reels
CSSX = N.CSSX + f"""
.corf{{background:radial-gradient(rgba(224,78,40,.13) 2px,transparent 2.4px) 0 0/36px 36px,{FIELD}}}
.corf .H .em,.crm .H .em{{background:#FFFFFF}}
.crm{{background:radial-gradient(rgba(43,63,224,.12) 2px,transparent 2.4px) 0 0/36px 36px,{CREAM}}}
.crm .H .em{{background:{SOFT}}}
.kick{{font-family:'DejaVu Sans Mono';font-weight:700;font-size:38px;letter-spacing:.14em;color:{COB}}}
.HLL{{line-height:1.2;text-align:left}}
.HLL .em{{padding:0 .14em;border-radius:.24em}}
"""

# ------------------------------------------------------------------------------------------------ FACTS (checked Nov 5 2026)
# CRA 'Who can claim - Donations and gifts' (line 34900, modified 2026-07-06): "You or your spouse or common law partner may be able
#   to claim a tax credit"; gift made by you or your spouse/partner; same portion not claimed on another return; official receipt.
# CRA 'How much you can claim' (modified 2026-07-06): up to 75% of net income; carry forward 5 years; federal rates 14.5/29/33 (2025).
# CRA 'How to claim' (modified 2026-07-06): Schedule 9, then line 34900; keep the official receipts.
# Finance Canada 'Report on the Impact of Reducing the Lowest Marginal Personal Income Tax Rate on Non-Refundable Tax Credits'
#   (modified 2026-07-29): "Only the first $200 of an individual's charitable donation claim is subject to the lowest income tax rate";
#   lowest rate 14% in 2026.  TaxTips.ca '2026 donation tax credit rates': federal 14% first $200, 29% over $200 (33% only to the
#   extent taxable income is in the 33% bracket).
# Our maths (made up for this post): each partner gives $200.
LOW, HIGH, CUT = 0.14, 0.29, 200
GIFT = 200
APART = 2 * round(GIFT * LOW)                       # two returns, each claim stays under $200
TOGETHER = round(CUT * LOW + (2 * GIFT - CUT) * HIGH)  # one return, $400 claim
assert (APART, TOGETHER) == (56, 86) and TOGETHER - APART == 30

LAYER = 54          # one coin layer = $50 of gifts
COIN_LO, COIN_HI = SOFT, COB


# ============================================================================== the drawn object: a glass jar of coins
def jar(x, y, w=330, h=560, lo=4, hi=0, lo_t=None, hi_t=None, empty_t=None, line=True, label=None, label_t=None, uid="j", rim_dx=0):
    """Open glass jar (rim + body), coins in layers from the bottom: `lo` soft-coral layers ($50 each) under the dashed $200 line,
    `hi` cobalt layers above it. lo_t/hi_t make the layers drop in one by one; empty_t fades the coins out (poured away)."""
    rim_h = 46
    bx, by, bw, bh = x, y + rim_h + 14, w, h - rim_h - 14
    r = 46
    body = (f"M{bx + 18},{by} L{bx + bw - 18},{by} Q{bx + bw},{by} {bx + bw},{by + 40} L{bx + bw},{by + bh - r} "
            f"Q{bx + bw},{by + bh} {bx + bw - r},{by + bh} L{bx + r},{by + bh} Q{bx},{by + bh} {bx},{by + bh - r} "
            f"L{bx},{by + 40} Q{bx},{by} {bx + 18},{by} Z")
    o = [f'<defs><clipPath id="cl{uid}"><path d="{body}"/></clipPath></defs>',
         f'<path d="{body}" transform="translate(12,14)" fill="{INK}" opacity=".9"/>',
         f'<path d="{body}" fill="#FFFBF8"/>']   # opaque glass (a see-through fill showed the ink shadow as grey)
    coins = []
    floor = by + bh - 10
    for k in range(lo + hi):
        top = floor - LAYER * (k + 1)
        col = COIN_LO if k < lo else COIN_HI
        tt = (None if lo_t is None else lo_t + 0.09 * k) if k < lo else (None if hi_t is None else hi_t + 0.11 * (k - lo))
        an = f' data-a="down" data-t="{tt:.2f}" data-d="0.3"' if tt is not None else ""
        n = 4
        cw = (bw - 20) / n
        row = "".join(f'<ellipse cx="{bx + 10 + cw * (i + .5) + (cw * .25 if k % 2 else 0):.1f}" cy="{top + LAYER / 2:.1f}" '
                      f'rx="{cw * .56:.1f}" ry="{LAYER * .46:.1f}" fill="{col}" stroke="{INK}" stroke-width="4"/>'
                      for i in range(n + (0 if k % 2 else 0)))
        coins.append(f'<g{an}>{row}</g>')
    ea = f' data-a="fade" data-t="{empty_t:.2f}" data-d="0.3"' if empty_t is not None else ""
    o.append(f'<g clip-path="url(#cl{uid})">{"".join(coins)}'
             + (f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="#FFFFFF" opacity=".97"{ea}/>' if empty_t is not None else "")
             + "</g>")
    # glass highlights
    o.append(f'<path d="M{bx + 34},{by + 70} L{bx + 34},{by + bh - 90}" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round" opacity=".9"/>')
    o.append(f'<path d="{body}" fill="none" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>')
    # rim
    o.append(f'<rect x="{bx - 14 + rim_dx}" y="{y}" width="{bw + 28}" height="{rim_h}" rx="16" fill="{COB}" stroke="{INK}" stroke-width="8"/>')
    o.append(f'<path d="M{bx + 4 + rim_dx},{y + rim_h / 2} L{bx + bw - 4 + rim_dx},{y + rim_h / 2}" stroke="#FFFFFF" stroke-width="5" opacity=".5" '
             f'stroke-dasharray="14 12"/>')
    if line:
        ly = floor - LAYER * 4
        o.append(f'<path d="M{bx - 24},{ly} L{bx + bw + 24},{ly}" stroke="{DCORAL}" stroke-width="7" stroke-dasharray="18 12" '
                 f'stroke-linecap="round"/>')
    if label:
        o.append(f'<g{"" if label_t is None else f" data-a=\"pop\" data-t=\"{label_t:.2f}\" data-d=\"0.3\""}>'
                 f'<rect x="{bx + bw / 2 - 150}" y="{by + 80}" width="300" height="74" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
                 + txt(bx + bw / 2, by + 132, label, 36, INK, weight=700) + "</g>")
    return "".join(o)


def jar_floor(y, h=560):
    """y of the $200 line for a jar drawn at y with height h (matches jar())."""
    by, bh = y + 60, h - 60
    return by + bh - 10 - LAYER * 4


def left(text, y, size=104, x=90, t=None, gap=0.14, style=""):
    """Left-aligned serif lines (new composition: no centred block). With t, the lines lift in one by one."""
    parts = [p.strip() for p in text.split(" / ")]
    if t is None:
        inner = "<br>".join(md(p) for p in parts)
    else:
        inner = "<br>".join(f'<span style="display:inline-block" data-a="up" data-t="{t + gap * i:.2f}" data-d="0.3">{md(p)}</span>'
                            for i, p in enumerate(parts))
    return el(inner, x, y, a="none", cls="H HLL", style=f"font-size:{size}px;white-space:nowrap;{style}")


def hand(text, x, y, size=62, t=0.0, r=-2, color=None, center=False):
    col = f"color:{color};" if color else ""
    if center:
        return el(f'<span class="save" style="font-size:{size}px;white-space:nowrap;{col}">{text}</span>', "c", y, a="pop", t=t, r=r)
    return el(f'<span class="save" style="font-size:{size}px;white-space:nowrap;{col}">{text}</span>', x, y, a="pop", t=t, r=r)


def follow_l(y, t=0.15, size=78):
    return el(f'<span class="save" style="font-size:{size}px;line-height:1.1">Follow for one money rule a day,<br>in plain words.</span>',
              "c", y, a="pop", t=t, r=-2)


def big(x, y, s, size, color, anchor="start", t=None, a="pop"):
    an = f' data-a="{a}" data-t="{t:.2f}" data-d="0.3"' if t is not None else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" style="font-family:Inter Display" '
            f'font-weight="800" letter-spacing="-2"{an}>{s}</text>')


def receipt_slip(x, y, t, uid):
    """Small drawn charity receipt (dropping into the jar in the do-this beat)."""
    w, h = 230, 130
    return (f'<g data-a="drop" data-t="{t:.2f}" data-d="0.4"><g transform="rotate({-8 if uid == "a" else 7} {x + w / 2} {y + h / 2})">'
            f'<rect x="{x + 8}" y="{y + 10}" width="{w}" height="{h}" rx="10" fill="{INK}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
            + txt(x + w / 2, y + 46, "RECEIPT", 30, COB, weight=700)
            + big(x + w / 2, y + 108, "$200", 58, INK, "middle") + "</g></g>")


# ============================================================================== A. donations on one return (Tue Nov 10, 7 pm)
def donations():
    r = Reel("ff-reel-1110-donations-one-return", "fullyfunded", bpm=95, css=CSSX, stage=FIELD)
    JY, JH = 760, 510
    ly = jar_floor(JY, JH)
    # frame 0: 2 text blocks (CANADA kicker + 6-word hook) and one picture (two coin jars, both filled to the same line).
    # 1.05 s: an arrow pours the partner's jar into yours; your jar fills past the line (cobalt); 1.9 s the plain payoff.
    r.scene(4, "".join([
        '<div class="par corf"></div>',
        el('<span class="kick" style="font-size:31px">CANADA · SPOUSE OR COMMON-LAW PARTNER</span>', 90, 300, a="none"),
        left("You both gave / *$200 to charity?*", 360, 108),
        svg(jar(150, JY, 330, JH, lo=4, hi=4, hi_t=1.25, uid="a")
            + jar(600, JY, 330, JH, lo=4, empty_t=1.2, uid="b")
            + path(f"M765,{JY - 24} C720,{JY - 100} 400,{JY - 104} 330,{JY - 30}", DCORAL, 13, 1.0, 0.3)
            + path(f"M300,{JY - 70} L330,{JY - 30} L372,{JY - 58}", DCORAL, 13, 1.25, 0.12)),
        left("Put both on one return. / *You can get more back.*", 1330, 78, t=1.9),
    ]), cam="push", shake=(1.3, 0.2, 10), cls="corf")
    # why: one jar, two rates. Numbers in big type beside the zones; the scoreboard lands at 1.6 / 2.0 s.
    J2X, J2Y = 110, 640
    l2 = jar_floor(J2Y, JH)
    r.scene(7, "".join([
        '<div class="par corf"></div>',
        left("Only the first $200 / *gets the low rate.*", 300, 96),
        svg(jar(J2X, J2Y, 330, JH, lo=4, hi=4, uid="c")
            + txt(500, l2 + 110, "FIRST $200 · TAX CREDIT", 31, INK, "start", 700, t=0.25)
            + big(500, l2 + 200, "14% back", 96, DCORAL, t=0.3)
            + txt(500, l2 - 150, "NEXT $200 · TAX CREDIT", 31, INK, "start", 700, t=0.7)
            + big(500, l2 - 60, "29% back", 96, COB, t=0.75)),
        el(f'<div class="card" style="padding:32px 48px;text-align:left"><span class="H" style="font-size:70px;line-height:1.25;'
           f'white-space:nowrap;color:{INK}">Two returns: <s style="text-decoration-color:{DCORAL};text-decoration-thickness:7px">'
           f'${APART} back</s><br><span style="color:{COB}">One return: ${TOGETHER} back</span></span></div>', 90, 1225, a="pop", t=1.5),
        el(f'<span class="kick" style="font-size:30px;color:{INK}">FEDERAL CREDIT · 2026 RATES</span>', 96, 1505, a="fade", t=1.9),
    ]), tin="glide", cam="left", cls="corf")
    # do this: cream field; text left, the jar bottom-right takes both receipts.
    r.scene(6, "".join([
        '<div class="par crm"></div>',
        hand("do this:", 90, 300, 88, t=0.0, r=-3),
        left("Claim both receipts / *on one return.*", 400, 100),
        left("Official donation receipts. / In your tax app: / *Schedule 9, line 34900.*", 680, 52, t=0.35, gap=0.12,
             style="line-height:1.3"),
        svg(jar(620, 905, 320, 470, lo=0, hi=0, line=False, label="ONE RETURN", uid="d")
            + receipt_slip(600, 1150, 0.5, "a") + receipt_slip(630, 1010, 0.7, "b")),
        hand("give by Dec 31 to count for 2026", 90, 1405, 64, t=1.1, r=-2, center=True),
    ]), tin="slamup", cam="rise", bg=CREAM, cls="crm")
    # end: back on the coral field, the full jar, the follow line, the stamp.
    r.scene(4, "".join([
        '<div class="par corf"></div>',
        left("One return. / *Both gifts.*", 300, 112),
        svg(jar(375, 640, 330, JH, lo=4, hi=4, uid="e")),
        follow_l(1250, t=0.15),
        stamp(840, 1440, 140, t=0.2),
    ]), tin="whipL", cam="push", cls="corf")
    r.loop(1.0, tin="cut")
    return N.timing(r, (3.6, 4.4, 3.6, 2.6, 0.4))


# ============================================================================== cover: style 7 reframe 'Instead of… / Try…' (quiet)
def cover_donations():
    """Style 7 reframe (quiet) + the single full jar (CD r2: not text cards only)."""
    def card(label, body, bg, strike=False):
        s = (f'text-decoration:line-through;text-decoration-thickness:6px;text-decoration-color:{DCORAL};opacity:.75;' if strike else "")
        return (f'<div style="padding:28px 44px;border-radius:36px;background:{bg};border:6px solid {INK};box-shadow:12px 12px 0 {INK}">'
                f'<div style="font-family:\'Caveat Brush\';font-size:62px;color:{DCORAL};line-height:1">{label}</div>'
                f'<div style="font-family:\'Instrument Serif\';font-size:76px;line-height:1.02;color:{INK};margin-top:8px;white-space:nowrap;{s}">'
                f'{body}</div></div>')
    return (f'<div class="par corf" style="position:absolute;inset:0"></div>'
            f'<div style="position:absolute;left:90px;top:300px;white-space:nowrap;font-size:30px" class="kick">CANADA · SPOUSE OR COMMON-LAW PARTNER</div>'
            f'<div class="H HLL" style="position:absolute;left:90px;top:340px;font-size:122px;line-height:1.36;white-space:nowrap">'
            f'You both gave<br><span class="em" style="background:#FFFFFF;padding:0 .12em">$200 to charity?</span></div>'
            f'<div style="position:absolute;left:90px;right:90px;top:720px;display:flex;flex-direction:column;gap:34px">'
            + card("Instead of…", f"two returns, ${APART} back", "#FFF4EE", strike=True)
            + card("Try…", f"one return, ${TOGETHER} back", "#FFFFFF")
            + "</div>"
            f'<svg style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">'
            f'{jar(116, 1232, 210, 400, lo=4, hi=2, uid="cv", rim_dx=5)}</svg>'
            f'<div style="position:absolute;left:380px;top:1290px;font-family:\'DejaVu Sans Mono\';font-weight:700;font-size:30px;'
            f'letter-spacing:.06em;line-height:1.5;color:{COB}">FEDERAL TAX CREDIT<br>2026 RATES · SCHEDULE 9</div>'
            + stamp(860, 1420, 110))


COVERS = {"ff-reel-1110-donations-one-return": cover_donations}
REELS = {"ff-reel-1110-donations-one-return": (donations, LIB / "ff-x-level-up.mp3")}


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
            ts = [0.0, 0.5, 1.0, 1.3, 1.6, 2.2, 3.0, 3.8, 4.5, 5.5, 6.5, 7.6, 8.3, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0]
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

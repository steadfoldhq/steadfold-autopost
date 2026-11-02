#!/usr/bin/env python3
"""Nov 2 clarity-gate fixes for two QUEUED Nov 1 Fully Funded items (re-rendered in place, same media paths as schedule/posts.json).
Copies the Nov 1 builder logic (imports nov01_fullyfunded / nov01_fullyfunded_feed; those scripts are not edited).

  ff-reel-1103-poa-ontario  (a) beat 2 "Your family may have to go to court first." + COURT-APPOINTED GUARDIAN overstated it: Ontario's
                            kit says the PGT may become statutory guardian automatically, family/friends may apply to replace it, or
                            a court may appoint a guardian -> "Your family may need a court or the government to approve them first."
                            + a milder APPROVAL NEEDED label. (b) cover: headline kept, sub-lines cut to ONE line. (c) hook beat:
                            "Who handles your bills?". (d) caption adds who can't witness (incl. your own spouse/partner).
  ff-richhabits-05          the 1-7 row read like a week and "20:00" like 8 pm: a small month page (1-30, the 7th circled,
                            "same day every month") and a timer face reading "20 min". Series layout and number unchanged.

    python3 studio/editorial/nov02_fullyfunded_fixes.py poa|rh05 [--qa-only]  < /dev/null
"""
import argparse, json, re, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import nov01_fullyfunded as N  # noqa: E402
from nov01_fullyfunded import (Reel, el, stamp, still, lines, do_this, follow, timing, svg, scaled, static, folder,  # noqa: E402
                               COB, INK, DCORAL, CSSX)
from kit import reading_report, overflow_check, render_frames, encode, probe, loudness  # noqa: E402

N.SCR = SCR = Path("/tmp/claude-0/nov02-fullyfunded")
OUT = REPO / "media/studio-nov01/fullyfunded"          # SAME paths the queue uses
RID = "ff-reel-1103-poa-ontario"


# ============================================================================== 1. power of attorney (Tue Nov 3, 7 pm), fixed
def poa():
    r = Reel(RID, "fullyfunded", bpm=95, css=CSSX, stage=N.CREAM)
    r.scene(4, "".join([
        '<div class="par dots"></div>',
        el('<span class="tag">ONTARIO, CANADA</span>', "c", 250, a="none"),
        still("Too sick to make / decisions? / *Who handles your bills?*", 330, 96),
        svg(scaled(folder(140, 10, 800, t_lock=0.35), 0.82, 735, vh=600)),
        lines("Without a power of attorney, / your spouse can't automatically / *manage your money.*", 1235, t=1.3, gap=0.16, size=76),
    ]), cam="push", shake=(0.45, 0.2, 14))
    r.scene(6, "".join([
        '<div class="par dots"></div>',
        still("Your family may need / *a court or the government* / to approve them first.", 260, 84),
        svg(folder(140, 640, 800)),
        el('<span class="stampx" style="font-size:72px;white-space:nowrap;line-height:1.1;text-align:center;color:#2B3FE0;'
           'border-color:#2B3FE0">APPROVAL NEEDED</span>', "c", 1240, a="stamp", t=0.7, d=0.3, r=-3),
    ]), tin="cut", cam="right")
    r.scene(7, "".join([
        do_this(250),
        still("Sign a *continuing* power / of attorney for property.", 360, 86),
        svg(folder(140, 640, 800, open_t=0.5)),
        el('<span class="save" style="font-size:66px;white-space:nowrap;line-height:1.1;text-align:center;display:inline-block">Ontario’s free kit · 2 witnesses,<br>not your spouse or kids</span>', "c", 1240, a="pop", t=0.9, r=-2),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        still("Name who manages / *your money.*", 240, 110),
        svg(scaled(static(folder(140, 10, 800, open_t=0.0)), 0.8, 630)),
        follow(1140, t=0.15, size=80),
    ]), tin="cut", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.6, 3.7, 3.5, 2.3, 0.4))


def cover_poa():
    """Style 15 calm text (quiet): cream dot paper, static serif headline, the locked YOUR MONEY folder from beat 2, one handwritten line."""
    return (f'<div class="par dots" style="position:absolute;inset:0"></div>'
            '<div style="position:absolute;left:0;width:1080px;top:300px;text-align:center"><span class="tag">ONTARIO, CANADA</span></div>'
            f'<div class="H HL" style="position:absolute;left:40px;right:40px;top:380px;text-align:center;font-size:120px;white-space:nowrap">'
            f'Your spouse can’t<br><span class="em">just step in.</span></div>'
            f'<svg style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">'
            f'{scaled(folder(140, 10, 800).replace("data-a", "data-x"), 0.86, 730, vh=600)}</svg>'
            f'<div style="position:absolute;left:0;right:0;top:1270px;text-align:center;font-family:\'Caveat Brush\';font-size:70px;line-height:1.1;'
            f'color:{DCORAL};white-space:nowrap;transform:rotate(-2deg)">No power of attorney?<br>They may need approval first.</div>'
            + stamp(880, 1500, 110))


def build_poa(qa_only=False):
    r = poa()
    print(json.dumps(reading_report(r)))
    print("duration", round(r.duration, 2), "overflow", overflow_check(r))
    assert r.duration <= 15.0, r.duration
    N.COVERS[RID] = cover_poa
    if qa_only:
        N.cover(r, RID, SCR / f"{RID}-cover-qa.jpg")
        return r
    w = SCR / RID
    fdir, n = render_frames(r, w, dsf=2, workers=1)
    out = OUT / f"{RID}.mp4"
    encode(fdir, n, N.LIB / "ff-x-money-moves.mp3", out, bpm=95)
    N.cover(r, RID, OUT / f"{RID}-cover.jpg")
    print(json.dumps(dict(id=RID, probe=probe(out), lufs=loudness(out), cuts=[round(c, 2) for c in r.cuts()])))
    shutil.rmtree(w, ignore_errors=True)
    return r


# ============================================================================== 2. Rich Habits, Decoded No. 5, fixed
def build_rh05():
    import nov01_fullyfunded_feed as F
    INKF, CORALF, COBF = F.INK, F.CORAL, F.COB

    def month_page(x0=540, y0=880, w=470, h=470):
        """Drawn month page: EVERY MONTH header, days 1-30 in a grid, the 7th circled; MONEY DATE · 20 MIN / SAME DAY EVERY MONTH."""
        cw = (w - 40) / 7
        o = [f'<svg style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="0 0 {w} {h}">',
             f'<rect x="6" y="20" width="{w - 12}" height="{h - 30}" rx="22" fill="#FFFFFF" stroke="{INKF}" stroke-width="5"/>',
             f'<rect x="6" y="20" width="{w - 12}" height="64" rx="22" fill="{COBF}" stroke="{INKF}" stroke-width="5"/>',
             f'<rect x="9" y="58" width="{w - 18}" height="26" fill="{COBF}"/>',
             f'<text x="{w / 2}" y="64" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="#FFFFFF">EVERY MONTH</text>']
        for d in range(30):
            row, col = divmod(d, 7)
            cx, cy = 20 + col * cw + cw / 2, 124 + row * 46
            o.append(f'<text x="{cx:.0f}" y="{cy}" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="24" '
                     f'fill="{CORALF if d == 6 else INKF}">{d + 1}</text>')
        c7 = 20 + 6 * cw + cw / 2
        o.append(f'<ellipse cx="{c7:.0f}" cy="116" rx="27" ry="24" fill="none" stroke="{CORALF}" stroke-width="5"/>')
        o.append(f'<text x="{w - 30}" y="388" text-anchor="end" font-family="DejaVu Sans Mono" font-weight="700" font-size="28" fill="{CORALF}">MONEY DATE · 20 MIN</text>')
        o.append(f'<text x="{w - 30}" y="428" text-anchor="end" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="{INKF}">SAME DAY EVERY MONTH</text>')
        o.append("</svg>")
        return "".join(o)

    def timer(x, y, w=300):
        """Drawn kitchen timer, a third of the dial shaded, the face reading '20 min' (not a clock time)."""
        return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;z-index:3;overflow:visible" viewBox="0 0 300 300">'
                f'<rect x="132" y="8" width="36" height="34" rx="8" fill="{INKF}"/>'
                f'<circle cx="160" cy="170" r="128" fill="{INKF}"/>'
                f'<circle cx="150" cy="160" r="128" fill="#FFFFFF" stroke="{INKF}" stroke-width="7"/>'
                f'<path d="M150,160 L150,32 A128,128 0 0 1 260.9,224 Z" fill="#FFD9CB"/>'
                f'<circle cx="150" cy="160" r="128" fill="none" stroke="{INKF}" stroke-width="7"/>'
                f'<text x="150" y="184" text-anchor="middle" font-family="Inter Display, Inter" font-weight="800" font-size="58" fill="{INKF}">20 min</text>'
                '</svg>')

    F.date_card = month_page
    F.timer = timer
    F.main()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("what", choices=["poa", "rh05"])
    ap.add_argument("--qa-only", action="store_true")
    a = ap.parse_args()
    SCR.mkdir(parents=True, exist_ok=True)
    build_poa(a.qa_only) if a.what == "poa" else build_rh05()

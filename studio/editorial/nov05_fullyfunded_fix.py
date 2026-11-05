#!/usr/bin/env python3
"""Nov 5 fix (stranger gate: CONFUSING) for the queued Reel ff-reel-1108-medical-one-return (Sun Nov 8 19:00).
Re-renders IN PLACE: media/studio-nov04/fullyfunded/ff-reel-1108-medical-one-return.mp4 + -cover.jpg.
Imports the Nov 4 drawn receipt and helpers from studio/editorial/nov04_fullyfunded.py (not edited); the measured receipts, the
tax-return card and the scene copy are rebuilt here:
  - one number per meaning, each labelled: BILLS $2,000 / 3% OF INCOME -$1,200 / $800 COUNTS FOR CREDIT; line 33099 shows $800
    (CRA RC4065: you claim the total minus the lesser of 3% of net income or the fixed amount), with BILLS $2,000 - $1,200 under it;
  - the saving shown as labelled maths: $800 x 14% = $112 off federal tax (2026 lowest rate, CRA / Finance Canada);
  - ONE instruction: "Usually the lower earner's return. Check both in your tax app.";
  - the cap on screen: "or $2,891 (2026), if that's less" (TaxTips.ca 2026 table; CRA RC4065 2025 gives $2,834).

    python3 studio/editorial/nov05_fullyfunded_fix.py [--qa-only] [--cover-only]  < /dev/null
"""
import argparse, json, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import nov04_fullyfunded as M  # noqa: E402
import nov01_fullyfunded as N  # noqa: E402
from nov04_fullyfunded import (Reel, el, stamp, svg, path, txt, COB, INK, DCORAL, GREEN, CREAM,  # noqa: E402
                               lines, still, do_this, follow, timing, card, static, scaled, receipt, BILLS, TOTAL, HI, LO)
from kit import reading_report, overflow_check, render_frames, encode, probe, loudness  # noqa: E402

RID = "ff-reel-1108-medical-one-return"
N.SCR = SCR = Path("/tmp/claude-0/nov05-fullyfunded")
OUT = REPO / "media/studio-nov04/fullyfunded"      # in place (queued paths)
MUSIC = REPO / "media/music/library/v4/ff-x-big-reveal.mp3"
CSSX = M.CSSX

CAP26, CAP25, RATE = 2891, 2834, 0.14
FLOOR_LO = min(round(LO * .03), CAP26)
COUNTS = TOTAL - FLOOR_LO
SAVE = round(COUNTS * RATE)
assert (FLOOR_LO, COUNTS, SAVE) == (1200, 800, 112)
assert min(round(HI * .03), CAP26) == 2700 and max(0, TOTAL - 2700) == 0 and min(round(HI * .03), CAP25) == 2700


def measure(x, y, w, who, inc, t0=None):
    """Tall drawn receipt for one return: WHO / EARNS / BILLS $2,000 / 3% OF INCOME -$X / a box: $N + COUNTS FOR CREDIT."""
    minus = min(round(inc * .03), CAP26)
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
             + txt(x + w / 2, y + 632, "COUNTS FOR CREDIT", 31, col, weight=700) + '</g>')
    return "".join(o)


def return_line(x=90, y=0, w=900, tick_t=None):
    """Drawn tax-return card: LINE 33099 $800, 'BILLS $2,000 − 3% OF INCOME $1,200' under it, ticked LOWER EARNER box."""
    h = 480
    o = [f'<rect x="{x + 14}" y="{y + 16}" width="{w}" height="{h}" rx="26" fill="{INK}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="26" fill="{COB}" stroke="{INK}" stroke-width="7"/>',
         f'<rect x="{x + 4}" y="{y + 66}" width="{w - 8}" height="44" fill="{COB}"/>',
         txt(x + w / 2, y + 74, "PARTNER'S TAX RETURN", 50, "#FFFFFF", weight=700)]
    ry = y + 210
    o.append(txt(x + 50, ry, "LINE 33099", 52, INK, "start", 700))
    o.append(f'<text x="{x + w - 50}" y="{ry + 8}" font-size="88" fill="{GREEN}" text-anchor="end" style="font-family:Inter Display" '
             f'font-weight="800">${COUNTS:,}</text>')
    o.append(txt(x + 50, ry + 62, f"BILLS ${TOTAL:,} − 3% OF INCOME ${FLOOR_LO:,}", 36, INK, "start", 700))
    by = y + 405
    o.append(f'<rect x="{x + 50}" y="{by - 62}" width="84" height="84" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>')
    o.append(txt(x + 165, by, "THE LOWER EARNER'S RETURN", 40, COB, "start", 700))
    tk = f"M{x + 68},{by - 22} l18,22 l36,-48"
    o.append(path(tk, GREEN, 13, tick_t, 0.3) if tick_t is not None else path(tk, GREEN, 13))
    return "".join(o)


def medical():
    r = Reel(RID, "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    r.scene(4, "".join([
        '<div class="par dots"></div>',
        el('<span class="tag" style="font-size:42px">CANADA · MEDICAL EXPENSES</span>', "c", 300, a="none"),
        still("Dentist, glasses, pills: / *$2,000 this year?*", 390, 100),
        svg(scaled(receipt(230, 20, 620, row_t=None, total_t=None), 0.86, 640, vh=720)),
        lines("Usually best on / *the lower earner’s return.*", 1215, t=1.3, gap=0.14, size=80),
    ]), cam="push", shake=(0.75, 0.2, 12))
    r.scene(7, "".join([
        '<div class="par dots"></div>',
        still("Only bills above / *3% of income* count.", 300, 96),
        el(f'<span class="save" style="font-size:58px;white-space:nowrap;color:{INK}">or above ${CAP26:,} (2026), if that’s less</span>',
           "c", 530, a="fade", t=0.2),
        svg(measure(95, 630, 425, "YOU", HI, t0=0.4) + measure(560, 630, 425, "PARTNER", LO, t0=1.0)),
        el(f'<span class="save" style="font-size:60px;white-space:nowrap">${COUNTS} × 14% = ${SAVE} off federal tax</span>',
           "c", 1370, a="pop", t=1.9, r=-2),
    ]), tin="land", cam="right")
    r.scene(6, "".join([
        do_this(300),
        still("Claim them on / *line 33099.*", 400, 104),
        svg(scaled(return_line(90, 10, 900, tick_t=0.45), 0.86, 700, vh=520)),
        card(f'<span class="H" style="font-size:56px;line-height:1.22;color:{INK};white-space:nowrap">Usually the lower earner’s return.<br>'
             f'<span style="color:{COB}">Check both in your tax app.</span></span>', 1190, t=0.8, pad="32px 40px"),
    ]), tin="cut", cam="rise", bg=COB, cls="cobf")
    r.scene(4, "".join([
        still("One return. / *The whole family’s bills.*", 340, 104),
        svg(scaled(static(receipt(230, 20, 620, row_t=None, total_t=None)), 0.72, 640, vh=720)),
        follow(1230, t=0.15, size=80),
        stamp(840, 1450, 140, t=0.2),
    ]), tin="land", cam="push", bg=COB, cls="cobf")
    r.loop(1.0, tin="cut")
    return timing(r, (3.4, 4.6, 3.8, 2.4, 0.4))


def cover_medical():
    """Same loud Look B cover as Nov 4; the handwritten line now matches the one on-screen instruction."""
    html = M.cover_medical()
    old = "claim them on the lower earner’s return"
    assert old in html
    return html.replace(old, "usually on the lower earner’s return")


def build(qa_only=False, cover_only=False):
    r = medical()
    print(json.dumps(reading_report(r)))
    print("duration", round(r.duration, 2), "overflow", overflow_check(r))
    N.COVERS[RID] = cover_medical
    if cover_only or qa_only:
        if cover_only:
            N.cover(r, RID, SCR / f"{RID}-cover-preview.jpg")
        if qa_only:
            w = SCR / (RID + "-qa")
            shutil.rmtree(w, ignore_errors=True)
            ts = [0.0, 0.5, 1.0, 1.5, 2.2, 3.0, 3.6, 4.5, 5.5, 6.5, 7.6, 8.4, 9.5, 10.5, 11.5, 12.4, 13.4, 14.3]
            ts = [t for t in ts if t < r.duration]
            idx = sorted({min(int(t * 30), int(r.duration * 30) - 1) for t in ts})
            render_frames(r, w, dsf=1, only=idx)
            print("qa frames in", w)
        return r
    assert r.duration <= 15.0, r.duration
    w = SCR / RID
    fdir, n = render_frames(r, w, dsf=2, workers=1)
    out = OUT / f"{RID}.mp4"
    encode(fdir, n, MUSIC, out, bpm=95)
    N.cover(r, RID, OUT / f"{RID}-cover.jpg")
    print(json.dumps(dict(id=RID, probe=probe(out), lufs=loudness(out), cuts=[round(c, 2) for c in r.cuts()])))
    shutil.rmtree(w, ignore_errors=True)
    return r


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--qa-only", action="store_true")
    ap.add_argument("--cover-only", action="store_true")
    a = ap.parse_args()
    build(a.qa_only, a.cover_only)

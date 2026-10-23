#!/usr/bin/env python3
"""Fully Funded recovery Reels (Oct 22): "Drawn to Scale" blueprint sheets (v0.5 floor) in the approved FF palette and
editorial type (Fraunces ink hook + soft-coral pill + round stamp), cut with the studio motion kit at FF's 95 bpm.

    python3 build/ff_reels.py <rid> [--qa-only] [--work DIR]
Outputs go to media/recovery-oct22/fullyfunded/<rid>.mp4 and <rid>-cover.jpg (dedicated cover, rendered at 2x).
"""
import argparse, json, math, os, shutil, sys
from pathlib import Path

os.environ.setdefault("KIT_FRAME_EXT", "jpg")
sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/motion"))
sys.path.insert(0, str(REPO / "studio/editorial"))
from kit import (Reel, el, words, encode, probe, loudness, render_frames, sheet, qa_times, make_readable, reading_report,  # noqa
                 overflow_check, FONTS, BASE_CSS)
import edkit as K  # noqa

OUT = REPO / "media/recovery-oct22/fullyfunded"
MUSIC = REPO / "media/music/library/v3/ff-c-confident-build-el.mp3"
COB, INK, CORAL, SOFT, DEEP, PAPER, CREAM = "#2B3FE0", "#141A55", "#FF6A3D", "#FFB08F", "#16206B", "#F5F7FF", "#F7F1E5"

CSS = f"""
.H{{font-family:Fraunces;font-variation-settings:'opsz' 72,'wght' 720,'SOFT' 0,'WONK' 0;color:{INK};letter-spacing:-.035em;line-height:1.07}}
.w.em:has(+ .w.em){{border-top-right-radius:0;border-bottom-right-radius:0;box-shadow:.26em 0 0 {SOFT}}}
.w.em + .w.em{{border-top-left-radius:0;border-bottom-left-radius:0}}
.em{{background:{SOFT};border-radius:.28em;padding:0 .12em .02em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.emc{{color:{CORAL}}}
.M{{font-family:'DejaVu Sans Mono';font-size:30px;letter-spacing:.08em;color:{COB};text-transform:uppercase}}
.Mb{{font-family:'DejaVu Sans Mono';font-weight:700;letter-spacing:.04em;color:{COB}}}
.save{{font-family:'Caveat Brush';color:#E04E28}}
.num{{font-family:'Inter Display';font-weight:800;letter-spacing:-.03em}}
.sheet{{background:
  linear-gradient(rgba(43,63,224,.16) 2px,transparent 2px) 0 0/150px 150px,
  linear-gradient(90deg,rgba(43,63,224,.16) 2px,transparent 2px) 0 0/150px 150px,
  linear-gradient(rgba(43,63,224,.07) 1px,transparent 1px) 0 0/30px 30px,
  linear-gradient(90deg,rgba(43,63,224,.07) 1px,transparent 1px) 0 0/30px 30px, {PAPER}}}
.sheetc{{background:
  linear-gradient(rgba(43,63,224,.14) 2px,transparent 2px) 0 0/150px 150px,
  linear-gradient(90deg,rgba(43,63,224,.14) 2px,transparent 2px) 0 0/150px 150px,
  linear-gradient(rgba(43,63,224,.06) 1px,transparent 1px) 0 0/30px 30px,
  linear-gradient(90deg,rgba(43,63,224,.06) 1px,transparent 1px) 0 0/30px 30px, {CREAM}}}
.frame{{position:absolute;left:60px;top:200px;right:60px;bottom:200px;border:3px solid rgba(43,63,224,.45)}}
svg text{{font-family:'DejaVu Sans Mono'}}
"""


def bg(cls="sheet"):
    return f'<div class="par {cls}"></div><div class="frame"></div>'


def stamp(x=820, y=250, size=170, t=None):
    # wrapped in a "chip" so the stamp's circular brand text isn't counted as reading words
    a = f'data-a="pop" data-t="{t}" data-d="0.4"' if t is not None else 'data-a="none"'
    return (f'<div class="el chip" style="left:{x}px;top:{y}px;padding:0;background:none" {a}>'
            + K.stamp("fullyfunded", 0, 0, size, -12).replace("position:absolute;left:0px;top:0px;", "position:relative;display:block;")
            + "</div>")


def svg(inner, a="none", t=0.0):
    return (f'<svg class="el" style="left:0;top:0;width:1080px;height:1920px" viewBox="0 0 1080 1920" '
            f'data-a="{a}" data-t="{t}" data-d="0.3">{inner}</svg>')


def path(d, color=COB, w=8, t=None, dur=0.5, dash=None, fill="none"):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    an = f' data-a="draw" data-t="{t}" data-d="{dur}"' if t is not None else ""
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{da}{an}/>'


def txt(x, y, s, size=30, color=COB, anchor="middle", weight=400, t=None):
    an = f' data-a="fade" data-t="{t}" data-d="0.25"' if t is not None else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}" '
            f'letter-spacing="2"{an}>{s}</text>')


def dim(x1, x2, y, color=CORAL, t=None, w=4):
    """Dimension line with arrowheads and end ticks."""
    a = 18
    return "".join([
        path(f"M{x1},{y - 26} L{x1},{y + 26}", color, w, t, 0.15),
        path(f"M{x2},{y - 26} L{x2},{y + 26}", color, w, t, 0.15),
        path(f"M{x1},{y} L{x2},{y}", color, w, t, 0.4),
        path(f"M{x1 + a},{y - 12} L{x1},{y} L{x1 + a},{y + 12}", color, w, None if t is None else t + 0.3, 0.1),
        path(f"M{x2 - a},{y - 12} L{x2},{y} L{x2 - a},{y + 12}", color, w, None if t is None else t + 0.3, 0.1),
    ])


# ============================================================================== 1. Wills (Trial Reel, Sun 8:15 am)
def wills_diagram(t0=None):
    """Estate block feeding two rooms; the common-law pipe is valved shut. Drawn on frame 0 (t0=None) or drawn in."""
    d = lambda k: None if t0 is None else t0 + k  # noqa: E731
    return svg("".join([
        path("M360,870 L720,870 L720,1000 L360,1000 Z", COB, 8, d(0), 0.4),
        txt(540, 950, "ESTATE", 44, COB, weight=700),
        path("M540,1000 L540,1060 L300,1060 L300,1130", COB, 8, d(0.15), 0.35),
        path("M540,1060 L780,1060 L780,1130", COB, 8, d(0.15), 0.35),
        path("M170,1130 L430,1130 L430,1330 L170,1330 Z", COB, 8, d(0.3), 0.4),
        path("M650,1130 L910,1130 L910,1330 L650,1330 Z", COB, 8, d(0.3), 0.4, dash="18 14"),
        txt(300, 1184, "MARRIED", 36, COB, weight=700),
        txt(780, 1184, "COMMON-LAW", 34, COB, weight=700),
        # coral valve, shut
        f'<circle cx="780" cy="1088" r="30" fill="{PAPER}" stroke="{CORAL}" stroke-width="7"/>',
        path("M762,1070 L798,1106 M798,1070 L762,1106", CORAL, 7),
    ]))


def wills():
    r = Reel("ff-pan-1025am-wills-s15", "fullyfunded", bpm=95, css=CSS, stage=PAPER)
    r.scene(3, "".join([
        bg(), stamp(830, 228, 150),
        el('Not married?<br><span class="em">No will?</span>', "c", 400, a="none", cls="H", style="font-size:150px"),
        wills_diagram(),
        el('<span class="num" style="font-size:118px;color:#E04E28">$0</span>', 700, 1218, a="stamp", t=0.3, d=0.3, r=-8),
        el('<span style="font:700 46px/1 Inter;color:#141A55">✓</span>', 285, 1230, a="pop", t=0.2),
    ]), cam="push", shake=(0.3, 0.25, 18))
    r.scene(4, "".join([
        bg(),
        words("*In Ontario:*", "c", 520, t=0.0, gap=0.1, cls="H", style="font-size:150px"),
        svg("".join([
            txt(160, 900, "MARRIED SPOUSE", 40, COB, "start", 700),
            path("M160,940 L920,940 L920,1040 L160,1040 Z", COB, 6, 0.2, 0.4, fill="rgba(43,63,224,.14)"),
            dim(160, 920, 1090, COB, 0.45),
            txt(540, 1150, "GETS THE FIRST $350,000", 44, COB, weight=700, t=0.6),
            txt(160, 1250, "COMMON-LAW PARTNER", 40, "#E04E28", "start", 700, t=0.9),
            path("M160,1280 L172,1280 L172,1380 L160,1380 Z", CORAL, 6, 1.0, 0.2),
            txt(205, 1365, "gets $0", 96, "#E04E28", "start", 700, t=1.1),
        ])),
    ]), tin="whipL", cam="right")
    r.scene(3, "".join([
        bg(),
        el('<span class="save" style="font-size:84px">do this:</span>', "c", 400, a="pop", t=0.0, r=-3),
        words("Call a wills lawyer / *this week.*", "c", 520, t=0.1, gap=0.09, cls="H", style="font-size:108px"),
        stamp(455, 1080, 170, t=0.6),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.loop(1.5, tin="zoom")
    return r


# ============================================================================== 2. TFSA withdrawal trap (Sun 7 pm)
X0, X1 = 120, 960          # Jan 1 .. Dec 31 drawn to scale: 65 px per month
MX = lambda m: X0 + (X1 - X0) * (m - 1) / 12  # noqa: E731  month m starts here (1 = Jan)


def ruler(y=1150, t=None, labels=("MAR", "JUN")):
    d = lambda k: None if t is None else t + k  # noqa: E731
    parts = [path(f"M{X0},{y} L{X1},{y}", COB, 8, d(0), 0.4)]
    for m in range(1, 14):
        x = MX(m)
        h = 34 if m in (1, 13) else 18
        parts.append(path(f"M{x:.1f},{y - h} L{x:.1f},{y + h}", COB, 5 if m in (1, 13) else 3, d(0.05 * m), 0.1))
    for lab in labels:
        m = {"MAR": 3, "JUN": 6, "JAN": 13, "DEC": 12}[lab]
        x = MX(m) + (0 if lab == "JAN" else 32)
        parts.append(txt(x, y + 84, lab, 40, COB, weight=700))
    return "".join(parts)


def trap():
    r = Reel("ff-reel-1025-tfsa-trap-s15", "fullyfunded", bpm=95, css=CSS, stage=CREAM)
    y = 1180
    xm, xj = MX(3) + 32, MX(6) + 32
    arrows = "".join([
        path(f"M{xm},{y - 30} L{xm},{y - 190}", CORAL, 8),
        path(f"M{xm - 18},{y - 168} L{xm},{y - 192} L{xm + 18},{y - 168}", CORAL, 8),
        path(f"M{xj},{y - 190} L{xj},{y - 30}", COB, 8, 0.25, 0.3),
        path(f"M{xj - 18},{y - 52} L{xj},{y - 28} L{xj + 18},{y - 52}", COB, 8, 0.5, 0.1),
    ])
    r.scene(3, "".join([
        bg("sheetc"), stamp(830, 228, 150),
        el('Putting TFSA<br>money back?<br><span class="em">Wait.</span>', "c", 400, a="none", cls="H", style="font-size:140px"),
        svg(ruler(y) + arrows),
    ]), cam="push", shake=(0.55, 0.2, 12))
    hatch = "".join(
        f'<rect x="{MX(6) + 1:.1f}" y="{y - 120}" width="{(MX(13) - MX(6)) - 2:.1f}" height="110" fill="rgba(255,106,61,.22)" '
        f'stroke="{CORAL}" stroke-width="4" data-a="fade" data-t="0.25" data-d="0.3"/>' for _ in [0])
    cells = "".join(path(f"M{MX(m):.1f},{y - 120} L{MX(m):.1f},{y - 10}", CORAL, 3, 0.3 + 0.08 * (m - 6), 0.1) for m in range(7, 13))
    r.scene(4, "".join([
        bg("sheetc"),
        words("Took money out? / It only goes back / in tax-free / *next January 1.*", "c", 360, t=0.0, gap=0.09, cls="H", style="font-size:96px"),
        svg(ruler(y, None, ()) + hatch + cells + dim(MX(6), MX(13), y - 170, CORAL, 0.6)),
    ]), tin="whipL", cam="left")
    r.scene(2, "".join([
        bg("sheetc"),
        el('<span class="save" style="font-size:84px">do this:</span>', "c", 400, a="pop", t=0.0, r=-3),
        words("Wait for / *January 1.*", "c", 500, t=0.1, gap=0.09, cls="H", style="font-size:104px"),
        stamp(455, 1080, 170, t=0.5),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.loop(1.5, tin="zoom")
    return r


R = {"ff-pan-1025am-wills-s15": wills, "ff-reel-1025-tfsa-trap-s15": trap}

COVER_SAVE = {"ff-pan-1025am-wills-s15": "send this to your partner", "ff-reel-1025-tfsa-trap-s15": "save this before you withdraw"}


def cover(r, rid, out):
    """Dedicated cover: the hook scene's settled state + the save-line, rendered at 2x (never a raw frame)."""
    from playwright.sync_api import sync_playwright
    from PIL import Image
    import io, glob
    s0 = r.scenes[0]
    html = s0["html"].replace('data-a="stamp"', 'data-a="none"').replace('data-a="pop"', 'data-a="none"')
    if "wills" in rid:
        html = html.replace("left:700px;top:1218px", "left:700px;top:1190px")
    html += el(f'<span class="save" style="font-size:62px">{COVER_SAVE[rid]}</span>', "c", 755 if "wills" in rid else 1290, a="none", r=-2)
    page = (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}{BASE_CSS}{CSS}"
            f".el{{position:absolute}}</style></head><body><div class='scene' style='display:block;background:{s0['bg']}'>"
            f"<div class='cam'>{html}</div></div></body></html>")
    tmp = Path(out).with_suffix(".html")
    tmp.write_text(page)
    chrome = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")[0]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chrome, args=["--disable-gpu", "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=2)
        pg.goto(tmp.as_uri())
        pg.wait_for_timeout(600)
        im = Image.open(io.BytesIO(pg.screenshot(type="png"))).convert("RGB").resize((1080, 1920), Image.LANCZOS)
        im.save(out, quality=92, subsampling=0)
        b.close()
    tmp.unlink()


def build(rid, work, qa_only=False):
    r = make_readable(R[rid]())
    # the loop scene repeats the hook the viewer already read: keep it at 1.5 beats so it flows into frame 0
    r.scenes[-1]["dur"] = 1.5 * r.beat
    r.t = r.scenes[-1]["start"] + r.scenes[-1]["dur"]
    r.stretch(12.6)
    rep = reading_report(r)
    print(json.dumps(rep))
    print("duration", round(r.duration, 2), "overflow", overflow_check(r))
    assert r.duration <= 15.0, r.duration
    w = Path(work) / rid
    if qa_only:
        return r
    fdir, n = render_frames(r, w, dsf=2)
    out = OUT / f"{rid}.mp4"
    encode(fdir, n, MUSIC, out, bpm=95)
    sheet(fdir, qa_times(r), w / f"{rid}-qa.jpg", cols=8, scale=0.2)
    cover(r, rid, OUT / f"{rid}-cover.jpg")
    print(json.dumps(dict(id=rid, probe=probe(out), lufs=loudness(out), cuts=[round(c, 2) for c in r.cuts()])))
    shutil.rmtree(fdir, ignore_errors=True)
    return r


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--work", default="/tmp/claude-0/-home-claude/60837be5-8cde-507a-87a7-2bafa6fa6f6c/scratchpad/ff/work")
    ap.add_argument("--qa-only", action="store_true")
    ap.add_argument("--cover-only", action="store_true")
    a = ap.parse_args()
    for i in a.ids or list(R):
        if a.cover_only:
            cover(make_readable(R[i]()), i, OUT / f"{i}-cover.jpg")
            continue
        build(i, a.work, a.qa_only)

#!/usr/bin/env python3
"""Oct 24 studio build: FF + LH Reels (imports the approved kits; nothing in them is rewritten).

  A  ff-reel-1025-tfsa-trap-r2          FF "Drawn to Scale" blueprint kit (studio/recovery-oct22/fullyfunded/build/ff_reels.py)
  B  ff-reel-1027am-card-full-balance   same kit
  C  lh-reel-1027-write-from-memory     LH zine kit (studio/recovery-oct22/lockedhour/build/reelkit.py + lhkit.py)

    python3 studio/editorial/oct24_fflh.py <id> [--qa-only]
Outputs: media/studio-oct24/fullyfunded/<id>.mp4 + -cover.jpg, media/studio-oct24/lockedhour/<id>.mp4 + -cover.jpg.
Frames go to /tmp/claude-0/fflh/ and are deleted after each encode.

Pacing: every text beat holds 0.4 s/word + 0.6 s (kit.make_readable, half-beat grid) and the whole Reel is <= 15.0 s,
so each Reel carries ~30 on-screen words in three text beats + a 1-beat loop. Detail lives in the caption.
"""
import argparse, json, shutil, subprocess, sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
SCR = Path("/tmp/claude-0/fflh")
sys.path.insert(0, str(REPO / "studio/recovery-oct22/fullyfunded/build"))

# This machine's Playwright Chromium lives in chrome-linux64/; the kits glob chrome-linux/. Shim glob (kits untouched).
import glob as _glob  # noqa: E402
_g0 = _glob.glob
_glob.glob = lambda pat, *a, **k: _g0(pat, *a, **k) or _g0(pat.replace("chrome-linux/", "chrome-linux64/"), *a, **k)

import ff_reels as FF  # noqa: E402  (also puts studio/motion + studio/editorial on sys.path)
from ff_reels import (Reel, el, words, bg, stamp, svg, path, txt, dim, ruler, MX, X0, X1,  # noqa: E402
                      COB, INK, CORAL, SOFT, PAPER, CREAM, CSS)
from kit import (make_readable, reading_report, overflow_check, render_frames, encode, sheet, qa_times,  # noqa: E402
                 probe, loudness)

OUT_FF = REPO / "media/studio-oct24/fullyfunded"
OUT_LH = REPO / "media/studio-oct24/lockedhour"
DCORAL = "#E04E28"
# SVG children scale about their own centre (pop/stamp on circles, rects), not the viewBox origin.
CSSX = CSS + "svg *{transform-box:fill-box;transform-origin:center}"


def bgx(cls="sheet"):
    """Paper sheet without the inner frame (CD: the frame wasted space)."""
    return f'<div class="par {cls}"></div>'


# ============================================================================== A. TFSA trap, r3 (Sun Oct 25 7 pm)
YR = 1250                        # ruler baseline, lower half
XM, XJ = MX(3) + 32, MX(6) + 32  # mid-March, mid-June


def ruler_l(y=YR):
    """Jan..Jan ruler drawn to scale, labelled MAR, JUN and JAN 1 (next year)."""
    parts = [path(f"M{X0},{y} L{X1},{y}", COB, 9)]
    for m in range(1, 14):
        x = MX(m)
        h = 38 if m in (1, 13) else 20
        parts.append(path(f"M{x:.1f},{y - h} L{x:.1f},{y + h}", COB, 6 if m in (1, 13) else 4))
    parts += [txt(XM, y + 92, "MAR", 50, COB, weight=700), txt(XJ, y + 92, "JUN", 50, COB, weight=700),
              txt(X1 + 24, y + 92, "JAN 1", 50, COB, "end", 700)]
    return "".join(parts)


def took_out(y=YR, labels=True):
    return "".join([path(f"M{XM},{y - 34} L{XM},{y - 250}", CORAL, 10),
                    path(f"M{XM - 22},{y - 224} L{XM},{y - 252} L{XM + 22},{y - 224}", CORAL, 10)]
                   + ([txt(XM, y - 342, "TOOK", 50, DCORAL, weight=700), txt(XM, y - 288, "OUT", 50, DCORAL, weight=700)] if labels else []))


def put_back(x=XJ, y=YR, t=None, labels=True, color=COB):
    T = (lambda k: None) if t is None else (lambda k: t + k)  # noqa: E731
    return "".join([path(f"M{x},{y - 250} L{x},{y - 34}", color, 10, T(0), 0.3),
                    path(f"M{x - 22},{y - 60} L{x},{y - 32} L{x + 22},{y - 60}", color, 10, T(0.25), 0.1)]
                   + ([txt(x, y - 342, "PUT", 50, color, weight=700, t=T(0.1)),
                       txt(x, y - 288, "BACK", 50, color, weight=700, t=T(0.1))] if labels else []))


def trap_r3():
    r = Reel("ff-reel-1025-tfsa-trap-r2", "fullyfunded", bpm=95, css=CSSX, stage=CREAM)
    r.scene(2.5, "".join([
        bgx("sheetc"), stamp(830, 200, 150),
        el('Put TFSA<br>money back<br><span class="em">too soon?</span>', "c", 340, a="none", cls="H", style="font-size:136px"),
        svg(ruler_l() + took_out() + put_back(t=0.2)),
    ]), cam="push", shake=(0.5, 0.2, 12))
    # beat 2: the rule. An arc from the March withdrawal to JAN 1: the room comes back there.
    arc = (f'<path d="M{XM},{YR - 40} C{XM + 150},{YR - 330} {X1 - 150},{YR - 330} {X1},{YR - 46}" fill="none" stroke="{COB}" '
           f'stroke-width="9" stroke-dasharray="22 16" stroke-linecap="round" data-a="draw" data-t="0.35" data-d="0.8"/>'
           + path(f"M{X1 - 34},{YR - 80} L{X1},{YR - 44} L{X1 + 18},{YR - 90}", COB, 9, 1.1, 0.12)
           + f'<circle cx="{X1}" cy="{YR}" r="30" fill="{COB}" data-a="pop" data-t="1.2" data-d="0.25"/>')
    r.scene(5.5, "".join([
        bgx("sheetc"),
        words("The room / comes back / *next January 1.*", "c", 360, t=0.0, gap=0.08, cls="H", style="font-size:112px"),
        svg(ruler_l() + took_out(labels=False) + arc),
    ]), tin="whipL", cam="left", shake=(1.25, 0.2, 10))
    # beat 3: the stakes. Put back in June, every month to December fills coral.
    pops = "".join(
        f'<rect x="{MX(m) + 5:.1f}" y="{YR - 150}" width="{MX(m + 1) - MX(m) - 10:.1f}" height="132" rx="8" fill="{CORAL}" '
        f'data-a="fade" data-t="{0.9 + 0.14 * (m - 6):.2f}" data-d="0.12"/>' for m in range(6, 13))
    r.scene(8, "".join([
        bgx("sheetc"),
        words("Put it back sooner? / CRA taxes the extra / *1% a month.*", "c", 330, t=0.0, gap=0.08, cls="H",
              style="font-size:104px"),
        svg(ruler_l() + pops + put_back(t=0.4, labels=False) + dim(MX(6), MX(13), YR - 200, CORAL, 0.9)),
    ]), tin="slamup", cam="push", shake=(1.9, 0.2, 12))
    # do this: the June put-back is struck out; a new put-back lands on JAN 1 with a tick.
    r.scene(7.5, "".join([
        bgx("sheetc"),
        el('<span class="save" style="font-size:88px">do this:</span>', "c", 300, a="pop", t=0.0, r=-3),
        words("Wait until / *January 1* / to put it back.", "c", 410, t=0.1, gap=0.08, cls="H", style="font-size:108px"),
        svg(ruler_l() + took_out(labels=False) + put_back(labels=False, color="rgba(43,63,224,.35)")
            + path(f"M{XJ - 40},{YR - 200} L{XJ + 40},{YR - 90} M{XJ + 40},{YR - 200} L{XJ - 40},{YR - 90}", CORAL, 10, 0.7, 0.25)
            + put_back(x=X1 - 40, t=1.0, labels=False)
            + path(f"M{X1 - 130},{YR - 330} L{X1 - 100},{YR - 296} L{X1 - 44},{YR - 372}", COB, 12, 1.4, 0.25)),
        stamp(60, 1500, 140, t=0.6),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.loop(1.0, tin="zoom")
    # Seconds, set by hand to land under 15.0 s: hook 1.5 s (CD: <= 2 s, it returns in the loop); each text beat gets
    # 0.4 s/word + 0.6 s for its own words (the MAR/JUN/JAN 1 ruler labels stay put from frame 0, read once).
    for sc, d in zip(r.scenes, (1.5, 3.42, 5.02, 4.62, 0.4)):
        sc["dur"] = d
    t = 0.0
    for sc in r.scenes:
        sc["start"] = round(t, 4)
        t += sc["dur"]
    r.t = t
    return r


# ============================================================================== B. Card: pay the full balance (Tue 8:15 am)
def statement(t_int=0.35):
    """A card statement slip in blueprint line: text rows are drawn as bars; the minimum is ticked; interest stamps in."""
    x0, y0, w, h = 110, 860, 860, 600
    bar = lambda x, yy, ww, a=".22": f'<rect x="{x}" y="{yy}" width="{ww}" height="28" rx="14" fill="rgba(43,63,224,{a})"/>'  # noqa
    return "".join([
        f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="20" fill="{PAPER}" stroke="{COB}" stroke-width="8"/>',
        bar(x0 + 50, y0 + 50, 280, ".35"), bar(x0 + w - 240, y0 + 50, 190, ".35"),
        path(f"M{x0 + 30},{y0 + 120} L{x0 + w - 30},{y0 + 120}", COB, 3, dash="10 10"),
        bar(x0 + 50, y0 + 170, 360), bar(x0 + w - 220, y0 + 170, 170),
        txt(x0 + 50, y0 + 310, "MINIMUM", 66, COB, "start", 700),
        path(f"M{x0 + w - 150},{y0 + 280} L{x0 + w - 114},{y0 + 318} L{x0 + w - 52},{y0 + 240}", COB, 12),
        path(f"M{x0 + 30},{y0 + 380} L{x0 + w - 30},{y0 + 380}", COB, 3, dash="10 10"),
        txt(x0 + 50, y0 + 515, "INTEREST", 64, DCORAL, "start", 700, t=t_int),
        txt(x0 + w - 50, y0 + 525, "$48.50", 108, DCORAL, "end", 700, t=t_int),
    ])


def phone(t=0.5):
    """Drawn phone, card app Autopay screen: the selection moves from Minimum to Full balance, then a tick draws."""
    x0, y0, w = 130, 820, 820
    s0, s1 = y0 + 190, y0 + 380
    return "".join([
        f'<rect x="{x0}" y="{y0}" width="{w}" height="900" rx="70" fill="{PAPER}" stroke="{COB}" stroke-width="9"/>',
        f'<rect x="{x0 + w / 2 - 90}" y="{y0 + 34}" width="180" height="20" rx="10" fill="rgba(43,63,224,.35)"/>',
        f'<rect x="{x0 + 70}" y="{y0 + 92}" width="260" height="26" rx="13" fill="rgba(43,63,224,.35)"/>',
        txt(x0 + 170, s0 + 24, "Minimum", 68, COB, "start", 700),
        txt(x0 + 160, s1 + 22, "Full balance", 62, COB, "start", 700),
        f'<circle cx="{x0 + 100}" cy="{s0}" r="38" fill="none" stroke="{COB}" stroke-width="7"/>',
        f'<circle cx="{x0 + 100}" cy="{s1}" r="38" fill="none" stroke="{COB}" stroke-width="7"/>',
        f'<circle cx="{x0 + 100}" cy="{s0}" r="20" fill="{CORAL}"/>',
        f'<circle cx="{x0 + 100}" cy="{s0}" r="25" fill="{PAPER}" data-a="fade" data-t="{t}" data-d="0.1"/>',
        f'<rect x="{x0 + 34}" y="{s1 - 78}" width="{w - 68}" height="156" rx="30" fill="rgba(255,176,143,.5)" '
        f'data-a="fade" data-t="{t + 0.05}" data-d="0.2"/>',
        f'<circle cx="{x0 + 100}" cy="{s1}" r="20" fill="{COB}" data-a="pop" data-t="{t + 0.08}" data-d="0.2"/>',
        path(f"M{x0 + w - 104},{s1 - 4} L{x0 + w - 80},{s1 + 26} L{x0 + w - 44},{s1 - 32}", COB, 11, t + 0.35, 0.25),
        f'<rect x="{x0 + 70}" y="{y0 + 600}" width="{w - 140}" height="120" rx="60" fill="{COB}" data-a="pop" data-t="{t + 0.6}" data-d="0.25"/>',
    ])


def card():
    r = Reel("ff-reel-1027am-card-full-balance", "fullyfunded", bpm=95, css=CSSX + ".H .w{margin-right:.04em}", stage=PAPER)
    r.scene(4, "".join([
        bgx(), stamp(830, 200, 150),
        el('Paid on time.<br><span class="em">Still charged</span><br><span class="em">interest?</span>', "c", 330, a="none", cls="H",
           style="font-size:132px"),
        svg(statement(0.35)),
    ]), cam="push", shake=(0.4, 0.22, 16))
    # beat 2: two bars drawn to scale (860 px = the $3,000 bill): pay the minimum -> $48.50 interest; pay it all -> interest-free.
    bx, bw = 110, 860
    paid = bw * 90 / 3000
    y1, y2 = 900, 1180
    r.scene(10, "".join([
        bgx(),
        words("Pay the minimum? / You pay interest. / Pay it all? / *$0 interest.*", "c", 300, t=0.0, gap=0.1, cls="H",
              style="font-size:96px;word-spacing:.08em"),
        svg("".join([
            path(f"M{bx},{y1} L{bx + bw},{y1} L{bx + bw},{y1 + 150} L{bx},{y1 + 150} Z", COB, 6, 0.3, 0.3),
            f'<rect x="{bx}" y="{y1}" width="{paid:.1f}" height="150" fill="{COB}" data-a="fade" data-t="0.4" data-d="0.15"/>',
            f'<rect x="{bx + paid + 4:.1f}" y="{y1 + 4}" width="{bw - paid - 8:.1f}" height="142" fill="rgba(255,106,61,.6)" '
            f'data-a="fade" data-t="0.55" data-d="0.25"/>',
            txt(bx + bw - 30, y1 + 98, "$48.50 interest", 60, INK, "end", 700, t=0.7),
            f'<path d="M{bx},{y2 + 75} L{bx + bw},{y2 + 75}" stroke="{COB}" stroke-width="150" fill="none" '
            f'data-a="draw" data-t="1.6" data-d="0.5"/>',
            txt(bx + bw - 30, y2 + 98, "interest-free", 60, "#FFFFFF", "end", 700, t=2.0),
        ])),
    ]), tin="whipL", cam="right", shake=(2.05, 0.2, 10))
    r.scene(7.5, "".join([
        bgx(),
        el('<span class="save" style="font-size:88px">do this:</span>', "c", 280, a="pop", t=0.0, r=-3),
        words("Set autopay to / *full balance.*", "c", 390, t=0.1, gap=0.08, cls="H", style="font-size:112px"),
        svg(phone(0.55)),
        stamp(850, 170, 130, t=0.8),
    ]), tin="iris", focus=(540, 700), color=COB, color2=SOFT, cam="rise")
    r.loop(1.0, tin="zoom")
    return r


FF_REELS = {"ff-reel-1025-tfsa-trap-r2": (trap_r3, "save this before you put money back"),
            "ff-reel-1027am-card-full-balance": (card, "send this to whoever just got a card")}


def cover_ff(r, out, save, y):
    """Dedicated cover (same method as ff_reels.cover: hook scene settled + save-line, 2x render), save-line at y."""
    from playwright.sync_api import sync_playwright
    from PIL import Image
    import io
    from kit import FONTS, BASE_CSS
    s0 = r.scenes[0]
    html = s0["html"].replace('data-a="stamp"', 'data-a="none"').replace('data-a="pop"', 'data-a="none"')
    html += el(f'<span class="save" style="font-size:62px">{save}</span>', "c", y, a="none", r=-2)
    page = (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}{BASE_CSS}{r.css}"
            f".el{{position:absolute}}</style></head><body><div class='scene' style='display:block;background:{s0['bg']}'>"
            f"<div class='cam'>{html}</div></div></body></html>")
    tmp = SCR / f"{Path(out).stem}.html"
    tmp.write_text(page)
    chrome = _glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")[0]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chrome, args=["--disable-gpu", "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=2)
        pg.goto(tmp.as_uri())
        pg.wait_for_timeout(600)
        im = Image.open(io.BytesIO(pg.screenshot(type="png"))).convert("RGB").resize((1080, 1920), Image.LANCZOS)
        im.save(out, quality=92, subsampling=0)
        b.close()
    tmp.unlink()


COVER_Y = {"ff-reel-1025-tfsa-trap-r2": 1420, "ff-reel-1027am-card-full-balance": 1530}


def build_ff(rid, qa_only=False, cover_only=False):
    fn, save = FF_REELS[rid]
    r = fn()   # scene lengths are set by hand in beats (hook <= 2.5 s per CD; text beats meet 0.4 s/word + 0.6 s)
    rep = reading_report(r)
    print(json.dumps(rep[:-1]))
    print("duration", round(r.duration, 2), "overflow", overflow_check(r))
    if cover_only:
        cover_ff(r, OUT_FF / f"{rid}-cover.jpg", save, COVER_Y[rid])
        return r
    if qa_only:
        return r
    assert r.duration <= 15.0, r.duration
    w = SCR / rid
    fdir, n = render_frames(r, w, dsf=2)
    OUT_FF.mkdir(parents=True, exist_ok=True)
    out = OUT_FF / f"{rid}.mp4"
    encode(fdir, n, FF.MUSIC, out, bpm=95)
    sheet(fdir, qa_times(r), SCR / f"{rid}-qa.jpg", cols=8, scale=0.2)
    cover_ff(r, OUT_FF / f"{rid}-cover.jpg", save, COVER_Y[rid])
    print(json.dumps(dict(id=rid, probe=probe(out), lufs=loudness(out), cuts=[round(c, 2) for c in r.cuts()])))
    shutil.rmtree(fdir, ignore_errors=True)
    return r


# ============================================================================== C. LH: write it from memory (Tue 7 pm)
def build_lh(rid, qa_only=False, cover_only=False):
    sys.path.insert(0, str(REPO / "studio/recovery-oct22/lockedhour/build"))
    import reelkit as RK
    RK.SCR = SCR / "lh"
    RK.SCR.mkdir(parents=True, exist_ok=True)
    import lhkit
    lhkit_shoot_dir = SCR / "lh"
    from reelkit import scene, render, cover, dual, F, INK, PINK, DPINK, BUTTER, CREAM as LCREAM, stamp as lstamp
    import os, tempfile

    def at(x, y, inner, t=0, k="up", w=None, base=""):
        ww = f"width:{w}px;" if w else ""
        return (f"<div data-in='{t}' data-k='{k}' data-base='{base}' style='position:absolute;left:{x}px;top:{y}px;{ww}"
                f"transform:{base}'>{inner}</div>")

    def D(text, field, size, align="center", extra=""):
        return dual(text, field, style=f"font-size:{size}px;text-align:{align};{extra}")

    def grow(x, y, w, h, col, t, d, border=True, final=False, rad=10, extra=""):
        b = f"border:4px solid {INK};" if border else ""
        return (f"<div style='position:absolute;left:{x}px;top:{y}px;height:{h}px;width:{w if final else 0}px;background:{col};{b}"
                f"border-radius:{rad}px;{extra}' data-grow='{t},{d},0,{w}'></div>")

    def stampx(x, y, t=0.15):
        return at(x, y, lstamp(0, 0, 150, -12).replace("position:absolute;left:0px;top:0px;", "position:relative;"), t, "pop")

    def notebook(t_close=1.05, final=False, closed=False, x=90, y=920):
        """Open notebook (two pages of text lines); a pink highlighter sweeps three lines; then the book snaps shut."""
        pw, ph = 285, 420
        lines = "".join(f"<div style='position:absolute;left:26px;top:{46 + i * 52}px;width:{225 - (i % 3) * 35}px;height:13px;"
                        f"border-radius:7px;background:rgba(27,23,23,.28)'></div>" for i in range(7))
        hl = "".join(grow(x + 18, y + 36 + i * 52, 240 - (i % 3) * 35, 34, "rgba(255,92,168,.6)", 0.05 + 0.25 * i, 0.25,
                          border=False, final=final, rad=6) for i in range(3))
        left = (f"<div style='position:absolute;left:{x}px;top:{y}px;width:{pw}px;height:{ph}px;background:#FFFDF6;"
                f"border:5px solid {INK};border-radius:16px 4px 4px 16px;box-shadow:8px 8px 0 {INK}'>{lines}</div>")
        right = (f"<div style='position:absolute;left:{x + pw - 2}px;top:{y}px;width:{pw}px;height:{ph}px;background:#FFFDF6;"
                 f"border:5px solid {INK};border-radius:4px 16px 16px 4px;box-shadow:8px 8px 0 {INK};overflow:hidden' "
                 + ("" if final else f"data-grow='{t_close},0.22,{pw},0'") + f">{lines}</div>")
        cov = (f"<div style='width:{pw}px;height:{ph}px;background:{PINK};border:5px solid {INK};border-radius:6px 18px 18px 6px;"
               f"box-shadow:8px 8px 0 {INK};position:relative'><div style='position:absolute;left:34px;top:70px;width:170px;height:20px;"
               f"border-radius:10px;background:rgba(27,23,23,.35)'></div><div style='position:absolute;left:34px;top:110px;width:110px;"
               f"height:20px;border-radius:10px;background:rgba(27,23,23,.25)'></div></div>")
        chip4 = at(x - 10, y - 74, f"<div style='display:inline-block;background:{BUTTER};border:4px solid {INK};border-radius:16px;"
                                  f"padding:6px 20px;box-shadow:6px 6px 0 {INK};font:800 60px/1 Inter Display,Inter;color:{INK}'>4×</div>",
                   0, "pop", base="rotate(-6deg)")
        if closed:
            return at(x + 60, y, cov, 0, "pop")
        return left + hl + right + at(x, y, cov, t_close + 0.2, "pop")

    def page(t0=1.45, final=False, x=680, y=920):
        """A blank page (the 'write what you remember' sheet) with a pencil writing lines."""
        rows = "".join(grow(30, 56 + i * 60, 230 - (i % 2) * 60, 14, INK, t0 + 0.25 + 0.3 * i, 0.3, border=False, final=final, rad=7)
                       for i in range(6))
        sheet_ = (f"<div style='position:relative;width:320px;height:420px;background:#FFFDF6;border:5px solid {INK};border-radius:14px;"
                  f"box-shadow:8px 8px 0 {INK};transform:rotate(3deg)'>{rows}</div>")
        pencil = at(x + 220, y + 300, "<div class='emo' style='font-size:120px;line-height:1'>✏️</div>", 0 if final else t0 + 0.2, "pop")
        jit = (f"<div data-jit='{t0 + 0.25}' style='position:absolute;left:0;top:0'>{pencil}</div>")
        return at(x, y, sheet_, 0 if final else t0, "drop") + (pencil if final else jit)

    hook_txt = D("Exam next week? / *Stop rereading.*", "pink", 160)

    def hook(final=False):
        return (at(90, 330, hook_txt, 0, w=900) + notebook(final=final) + page(final=final) + stampx(840, 1430, 0 if final else 0.2))

    def hook_loop():   # the loop beat: book already shut, pencil writing (the action) — flows into frame 0
        return (at(90, 330, hook_txt, 0, w=900) + notebook(closed=True) + page(final=True) + stampx(840, 1430, 0))

    W = 840
    def big(v, t0, x, y):
        return at(x, y, f"<div class='S' style='font-size:160px;line-height:1'><span data-roll='{t0},0.7,0,{v}' data-suf='%'>{v}%</span></div>",
                  t0, "pop")
    ev = (at(90, 330, D("Students who wrote it / from memory / *remembered 61%.*", "dots", 116, extra="line-height:1.18"), 0, w=900)
          + at(110, 790, "<div class='mono' style='font-size:46px;font-weight:700;text-align:left'>1 WEEK LATER</div>", 0.5, "up", w=900)
          + at(110, 850, "<div class='S' style='font-size:88px;line-height:1;text-align:left'>from memory</div>", 0.6, "left", w=900)
          + grow(110, 960, int(W * 0.61), 150, PINK, 0.8, 0.7)
          + big(61, 0.8, 110 + int(W * 0.61) + 40, 955)
          + at(110, 1140, "<div class='S' style='font-size:88px;line-height:1;text-align:left'>read 4×</div>", 1.3, "left", w=900)
          + grow(110, 1245, int(W * 0.40), 150, BUTTER, 1.5, 0.6)
          + big(40, 1.5, 110 + int(W * 0.40) + 40, 1240)
          + "<div style='position:absolute;left:104px;top:950px;width:7px;height:455px;background:rgba(27,23,23,.55)'></div>")

    dot = (at(90, 330, "<div class='dothis' style='font-size:130px;text-align:center'>Do this:</div>", 0, w=900)
           + at(110, 540, f"<div class='card' style='position:relative;padding:44px 40px'>"
                          f"{D('Shut the book. / *Write what you* / *remember.*', 'cream', 104)}</div>", 0.15, "pop", w=860)
           + notebook(closed=True, y=1040)
           + page(t0=0.5, x=680, y=1040)
           + stampx(860, 1510, 0.4))

    # LH 100 bpm: cuts on beats (0.6 s). Reading: hook 6 words -> 3.0 s; evidence 15 -> 6.6 s; do this 9 -> 4.2 s.
    sc = [
        scene(0, 2.4, "pink", hook()),
        scene(2.4, 9.8, "dots", ev, "slam"),
        scene(9.8, 14.0, "cream", dot, "iris"),
        scene(14.0, 14.9, "pink", hook_loop(), "plate"),
    ]
    dur = 14.9
    for s in sc:
        assert "example" not in s.lower()
    if qa_only:
        print("lh scenes ok", dur)
        return
    OUT_LH.mkdir(parents=True, exist_ok=True)
    cov = (hook_loop()
           + at(90, 755, "<div class='hand' style='font-size:70px;text-align:center'>send this to whoever's cramming</div>", 0, w=900))
    cover(cov, "pink", OUT_LH / f"{rid}-cover.jpg")
    if cover_only:
        return
    render(rid, sc, dur, REPO / "media/music/library/lh-focus-inst-01.mp3", OUT_LH / f"{rid}.mp4", keep_frames=True)
    fd = RK.SCR / f"frames-{rid}"
    times = [0, 0.5, 1.0, 1.3, 1.8, 2.3, 2.8, 3.4, 4.2, 5.5, 7.0, 9.5, 10.1, 10.8, 11.8, 13.0, 13.9, 14.6]
    from PIL import Image
    tiles = [Image.open(fd / f"{int(round(t * 30)):05d}.jpg").resize((216, 384)) for t in times]
    sh = Image.new("RGB", (216 * 9, 384 * 2), "white")
    for i, im in enumerate(tiles):
        sh.paste(im, ((i % 9) * 216, (i // 9) * 384))
    sh.save(SCR / f"{rid}-qa.jpg", quality=88)
    shutil.rmtree(fd, ignore_errors=True)
    print(json.dumps(dict(id=rid, probe=probe(OUT_LH / f"{rid}.mp4"), lufs=loudness(OUT_LH / f"{rid}.mp4"))))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--qa-only", action="store_true")
    ap.add_argument("--cover-only", action="store_true")
    a = ap.parse_args()
    for i in a.ids:
        if i in FF_REELS:
            build_ff(i, a.qa_only, a.cover_only)
        else:
            build_lh(i, a.qa_only, a.cover_only)

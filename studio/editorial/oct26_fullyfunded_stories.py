#!/usr/bin/env python3
"""Oct 26 studio build: Fully Funded Story chains, Tue Oct 27 - Thu Oct 29 (12:30 question, 12:31 answer + tonight's Reel).
Editorial look (Fraunces ink + soft-coral pills + Caveat line + round stamp) on FF cream dot paper. Text stays inside y 250-1580.

    python3 studio/editorial/oct26_fullyfunded_stories.py
Writes media/studio-oct26/fullyfunded/stories/ff-st-10DD-N.jpg (1080x1920, 2x render, Lanczos, q92).
"""
import io
import sys
import glob
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/motion"))
sys.path.insert(0, str(REPO / "studio/editorial"))
_g0 = glob.glob  # this box ships chromium as chrome-linux64/; kit.py looks for chrome-linux/ (kit untouched)
glob.glob = lambda pat, *a, **k: _g0(pat, *a, **k) or _g0(pat.replace("chrome-linux/", "chrome-linux64/"), *a, **k)
from kit import FONTS, BASE_CSS  # noqa: E402
import edkit as K  # noqa: E402

OUT = REPO / "media/studio-oct26/fullyfunded/stories"
COB, INK, CORAL, DCORAL, SOFT, CREAM = "#2B3FE0", "#141A55", "#FF6A3D", "#E04E28", "#FFB08F", "#F7F1E5"

CSS = f"""
body{{margin:0}}
.pg{{position:relative;width:1080px;height:1920px;overflow:hidden;
  background:radial-gradient(rgba(43,63,224,.16) 2px,transparent 2.4px) 0 0/36px 36px,{CREAM}}}
.pg.alt{{background:radial-gradient(rgba(14,20,64,.07) 1.4px,transparent 1.8px) 0 0/22px 22px,#FFE4D6}}
.box{{position:absolute;left:90px;right:90px;top:300px;bottom:510px;display:flex;flex-direction:column;align-items:center;
  justify-content:center;text-align:center;gap:44px}}
.tag{{font:700 34px/1 'DejaVu Sans Mono';letter-spacing:.12em;color:#fff;background:{COB};border-radius:999px;padding:14px 30px}}
.H{{font-family:Fraunces;font-variation-settings:'opsz' 72,'wght' 720;color:{INK};letter-spacing:-.035em;line-height:1.08;margin:0}}
.em{{background:{SOFT};border-radius:.28em;padding:0 .12em .02em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.body{{font:500 50px/1.3 Inter;color:{INK};margin:0}}
.body b{{font-weight:800;color:{DCORAL}}}
.save{{font-family:'Caveat Brush';color:{DCORAL};font-size:70px;transform:rotate(-3deg)}}
.small{{font:700 28px/1.3 'DejaVu Sans Mono';letter-spacing:.08em;color:{COB};text-transform:uppercase}}
.next{{white-space:nowrap;font:800 40px/1.2 Inter;color:#fff;background:{INK};border-radius:28px;padding:26px 36px}}
"""

STORIES = {
    # Tue Oct 27: tonight's 7 pm Reel is the car-loan send test (ff-reel-1027-car-loan-send)
    "ff-st-1027-1": dict(tag="QUICK QUIZ · CAR LOANS", h='A 7-year car loan<br>costs <span class="em">less</span><br>than a 5-year one?',
                         save="true or false? tap →"),
    "ff-st-1027-2": dict(alt=True, tag="THE ANSWER", h='False.<br><span class="em">It costs more.</span>',
                         body="Borrow <b>$30,000</b> at 8%. Over 7 years instead of 5, the monthly payment is smaller, but you pay <b>$2,780 more interest</b>.",
                         small="loan made up for this post · the maths is real", next="Tonight at 7 pm: the 15-second version"),
    # Wed Oct 28: tonight's Reel ff-reel-1028-fhsa-room
    "ff-st-1028-1": dict(tag="CANADA · FHSA", h='Your FHSA room<br>builds up <span class="em">before</span><br><span class="em">you open one?</span>',
                         body="<b>FHSA</b> = First Home Savings Account, for first-time home buyers in Canada. <b>Room</b> = how much you're allowed to put in.",
                         save="true or false? tap →"),
    "ff-st-1028-2": dict(alt=True, tag="THE ANSWER", h='False.<br><span class="em">It starts when</span><br><span class="em">you open one.</span>',
                         fs=100, body="Room (how much you're allowed to put in) starts the year you open your First Home Savings Account: <b>$8,000</b>. Open one at your bank or investing app by <b>Dec 31</b>.",
                         small="for first-time home buyers in Canada · source: CRA", next="Tonight at 7 pm: a 15-second Reel<br>on our page"),
    # Thu Oct 29: tonight's Reel ff-reel-1029-fsa-expires
    "ff-st-1029-1": dict(tag="US · HEALTH FSA", h='<span style="white-space:nowrap">Unspent FSA money</span><br>is <span class="em">always yours</span><br>next year?', fs=96,
                         save="true or false? tap →"),
    "ff-st-1029-2": dict(alt=True, tag="THE ANSWER", h='False.<br><span class="em">It can be lost.</span>',
                         body="Money not used by your plan's end date can be forfeited. Some plans give <b>2½ extra months</b> or let a little carry over.",
                         small="check your own plan's rules · source: IRS", next="Tonight at 7 pm: a 15-second Reel<br>on our page"),
}


def page(s):
    parts = [f'<div class="tag">{s["tag"]}</div>', f'<h1 class="H" style="font-size:{s.get("fs", 108 if s.get("alt") else 112)}px">{s["h"]}</h1>']
    if s.get("body"):
        parts.append(f'<p class="body">{s["body"]}</p>')
    if s.get("save"):
        parts.append(f'<div class="save">{s["save"]}</div>')
    if s.get("small"):
        parts.append(f'<div class="small">{s["small"]}</div>')
    if s.get("next"):
        parts.append(f'<div class="next">{s["next"]}</div>')
    stamp = K.stamp("fullyfunded", 840, 1420, 150, -12)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}{BASE_CSS}{CSS}</style></head><body>"
            f"<div class='pg{' alt' if s.get('alt') else ''}'><div class='box'>{''.join(parts)}</div>{stamp}</div></body></html>")


def main():
    from playwright.sync_api import sync_playwright
    from PIL import Image
    OUT.mkdir(parents=True, exist_ok=True)
    chrome = (glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome") + glob.glob("/opt/pw-browsers/chromium-*/chrome-linux64/chrome"))[0]
    tmp = Path("/tmp/claude-0/ff26"); tmp.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chrome, args=["--disable-gpu", "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=2)
        for sid, s in STORIES.items():
            f = tmp / f"{sid}.html"
            f.write_text(page(s))
            pg.goto(f.as_uri())
            pg.wait_for_timeout(700)
            # safe-zone check: every text block inside y 250..1580
            boxes = pg.evaluate("""() => [...document.querySelectorAll('.box > *')].map(e => {const r = e.getBoundingClientRect();
                                   return [e.className, r.top, r.bottom, r.left, r.right]})""")
            for cls, t, bt, l, rt in boxes:
                assert t >= 250 and bt <= 1410 and l >= 60 and rt <= 1020, (sid, cls, t, bt, l, rt)
            im = Image.open(io.BytesIO(pg.screenshot(type="png"))).convert("RGB").resize((1080, 1920), Image.LANCZOS)
            im.save(OUT / f"{sid}.jpg", quality=92, subsampling=0)
            f.unlink()
            print(sid, "ok")
        b.close()


if __name__ == "__main__":
    main()

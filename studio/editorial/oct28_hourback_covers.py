#!/usr/bin/env python3
"""Dedicated Reel covers for the Oct 28 Hourback build (never a raw frame). 1080x1920, rendered at 2x then Lanczos down.

card    -> 'Instead of… Say…' reframe (style 7, QUIET): sits between Wed 7 pm hum (editorial demo, loud) and Thu 7 pm bill
           (editorial demo, loud). The 'Write…' line is Claude's real reply, word for word (opening greeting cut, marked …).
costume -> Kinetic big text (style 5, LOUD): stacked giant serif, one pill, hand-drawn ring, Caveat line, stamp. Sits after
           Fri 7 pm group chat (follow the line, quiet), before Mon Day 11 (series Look B, loud).
All text inside x 90-990, y 300-1400; hooks >= 120 px.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True
import edkit as K  # noqa: E402
from PIL import Image  # noqa: E402

HB = "hourback"
W, H = 1080, 1920
INK = "#2A1D47"
ACC = "#D4532A"
OUT = Path("/home/claude/steadfold-autopost/media/studio-oct28/hourback")
SCR = Path("/tmp/claude-0/oct28-hourback")


def page(bg, body):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{K.css(HB, W, H)}html,body{{background:{bg}}}</style></head>"
            f"<body><div class='page' style='background:{bg}'><div class='grain' style='opacity:.3'></div>{body}</div></body></html>")


def card_cover():
    f = dict(p1="#FFD4BD", p2="#C9CAF5")
    b = K.dual("Office card coming? / *AI writes your line.*", f, cls="S fit",
                style=f"position:absolute;left:90px;width:900px;top:340px;white-space:nowrap;font-size:132px;color:{INK}")
    b += (f'<div style="position:absolute;left:90px;right:90px;top:700px;background:#FFE6D3;border:4px solid {INK};border-radius:36px;padding:34px 46px 40px;transform:rotate(-1.5deg)">'
          f'<div style="font-family:\'Caveat Brush\';font-size:70px;color:{ACC};line-height:1">Instead of…</div>'
          f'<div style="font-family:\'Instrument Serif\';font-size:130px;line-height:1;color:{INK};margin-top:10px;text-decoration:line-through;text-decoration-thickness:7px;text-decoration-color:{ACC};opacity:.8">“HBD!”</div></div>')
    b += (f'<div style="position:absolute;left:90px;right:90px;top:1000px;background:#FFFFFF;border:4px solid {INK};border-radius:36px;padding:34px 46px 36px;box-shadow:0 14px 0 {INK};transform:rotate(1deg)">'
          f'<div style="font-family:\'Caveat Brush\';font-size:70px;color:{ACC};line-height:1">Write…</div>'
          f'<div style="font-family:\'Instrument Serif\';font-size:72px;line-height:1.05;color:{INK};margin-top:12px">“…Hope your year ahead is a good one, and that it balances out in your favour.”</div>'
          f'<div style="font-family:\'Caveat Brush\';font-size:44px;color:#5E54C9;margin-top:14px;text-align:right">Claude\'s real line, word for word</div></div>')
    b += K.stamp(HB, 820, 1470, size=150, rot=-10)
    return page("#FFF5EA", b)


GHOST = ('<svg style="position:absolute;left:390px;top:1150px" width="300" height="300" viewBox="-150 -170 300 300">'
         '<ellipse cx="0" cy="118" rx="120" ry="14" fill="rgba(42,29,71,.18)"/>'
         '<path d="M-120 100 Q-120 -150 0 -160 Q120 -150 120 100 Q100 122 80 100 Q60 122 40 100 Q20 122 0 100 Q-20 122 -40 100 Q-60 122 -80 100 Q-100 122 -120 100Z" '
         'fill="#FFFFFF" stroke="#2A1D47" stroke-width="6" stroke-linejoin="round"/>'
         '<path d="M-90 -48 H90" stroke="#2A1D47" stroke-width="7" stroke-linecap="round"/>'
         '<path d="M-84 -50 H-12 Q-14 -6 -48 -6 Q-82 -6 -84 -50Z M12 -50 H84 Q82 -6 48 -6 Q14 -6 12 -50Z" fill="#1D1830" stroke="#2A1D47" stroke-width="5"/>'
         '<path d="M-70 -40 l20 -2 M26 -40 l20 -2" stroke="#9E98D8" stroke-width="5" stroke-linecap="round"/>'
         '<path d="M-20 40 Q0 56 20 40" stroke="#2A1D47" stroke-width="6" fill="none" stroke-linecap="round"/></svg>')


def costume_cover():
    f = dict(p1="#FFC94D", p2="#FFD4BD")
    b = K.dual("Party in / an hour. / *No costume?*", f, cls="S fit",
                style=f"position:absolute;left:90px;width:900px;top:320px;white-space:nowrap;font-size:210px;line-height:1.1;color:{INK}")
    b += (f'<svg style="position:absolute;left:270px;top:648px" width="560" height="60" viewBox="0 0 600 60">'
          f'<path d="M10 30 Q 80 6 150 30 T 290 30 T 430 30 T 590 26" fill="none" stroke="{ACC}" stroke-width="10" stroke-linecap="round"/></svg>')
    b += (f'<div class="hand" style="position:absolute;left:90px;right:90px;top:1050px;font-size:74px;transform:rotate(-2deg)">ask AI what your closet can be</div>')
    b += GHOST
    b += K.stamp(HB, 790, 1250, size=150, rot=-10)
    return page("#C9CAF5", b)


def shot(html, out):
    from playwright.sync_api import sync_playwright
    SCR.mkdir(parents=True, exist_ok=True)
    tmp = SCR / (out.stem + ".html")
    tmp.write_text(html)
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg.goto(tmp.as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(400)
        pg.evaluate(K.FIT_JS, 900)
        png = SCR / (out.stem + ".png")
        pg.screenshot(path=str(png))
        br.close()
    Image.open(png).resize((W, H), Image.LANCZOS).convert("RGB").save(out, quality=92, subsampling=0)
    return out


def build(key):
    OUT.mkdir(parents=True, exist_ok=True)
    if key == "card":
        return shot(card_cover(), OUT / "hb-reel-1029am-coworker-card-cover.jpg")
    if key == "costume":
        return shot(costume_cover(), OUT / "hb-reel-1031-closet-costume-cover.jpg")


if __name__ == "__main__":
    for k in sys.argv[1:]:
        print(build(k))

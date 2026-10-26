#!/usr/bin/env python3
"""Hourback Reel for Tue Oct 27, 8:45 am (built Oct 26 2026 by the Hourback maker). NO trial flag (Performance desk order 4).

    python3 studio/editorial/oct26_hourback.py returns                 # render mp4 + dedicated cover -> media/studio-oct26/hourback/
    python3 studio/editorial/oct26_hourback.py returns --frame 0 2 ...  # quick stills sheet for review

Desk orders applied: the ACTION is shown in frame 0 (a drawn chat screen: the pasted return policy + the question, being sent),
hook line <= 6 words, payoff ("Last day: Nov 19") on screen by ~2 s, 4 beats: hook -> payoff -> Do this -> follow -> loop.
Real run: studio/editorial/hb-oct26-run-return-policy.txt (fresh Claude session, Oct 26 2026). Policy and dates made up for this post.
Reuses the Oct 25 Hourback kit (oct25_hb.py -> takereel.py, oct24_hb.py) by import; nothing in them is edited.
Cover = kinetic big text (style 5 look on the dedicated cover), not the 'editorial demo' layout of the neighbouring tiles.
"""
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/recovery-oct22/hourback/build"))
sys.path.insert(0, str(REPO / "studio/editorial"))
sys.dont_write_bytecode = True
import oct25_hb as O  # noqa: E402
from oct25_hb import T, serif, hand, card, scene, F, INK, ACC, SUN, W, H, FPS, stamp, small, kicker, button, page3, screen  # noqa: E402

O.OUT = REPO / "media/studio-oct26/hourback"
O.SCRATCH = Path("/tmp/claude-0/-home-claude-steadfold-autopost/ff2300fc-7071-5e6e-ab73-de16719b794b/scratchpad/hbrender")
MUSIC = REPO / "media/music/library/v4"

# quoted exactly from the transcript (first sentence; second sentence's key clause shown as a chip)
REPLY_1 = "Your last day to return the jacket is November 19 (30 days from the Oct 20 delivery), as long as it's unworn with tags attached."
REPLY_2 = "Because it was a sale item, you'll get store credit only"


def bubble(html, me=True, size=28, w=380):
    bg = "#E4E2FB" if me else "#FFFFFF"
    rad = "26px 26px 8px 26px" if me else "26px 26px 26px 8px"
    al = "flex-end" if me else "flex-start"
    return (f'<div style="display:flex;justify-content:{al};margin-bottom:14px"><div style="max-width:{w}px;background:{bg};border:3px solid {INK};'
            f'border-radius:{rad};padding:14px 18px;font:500 {size}px/1.28 Inter;color:{INK}">{html}</div></div>')


POLICY = ('<div style="font:800 23px Inter;letter-spacing:.08em;margin-bottom:6px">RETURNS</div>'
          'Unworn items with tags: <b>30 days from delivery.</b><br>Sale items: store credit only.<br>$7.99 return fee.')
ASK = "Bought it on sale Oct 12. It arrived Oct 20. <b>Last day to return it?</b>"


def chat_phone(a, b, still=False, w=600, h=760):
    """Frame-0 object: a drawn chat app with the pasted policy and the question, the send button pressed at a+0.25."""
    send = (f'<div style="position:absolute;right:22px;bottom:22px;width:74px;height:74px;border-radius:50%;background:{ACC};color:#fff;'
            f'font:800 44px Inter;display:flex;align-items:center;justify-content:center">↑</div>')
    field = (f'<div style="position:absolute;left:22px;right:110px;bottom:26px;height:66px;border:3px solid #B9B4C9;border-radius:99px;'
             f'font:500 24px/60px Inter;color:#9A95AD;padding-left:22px">Message</div>')
    inner = (f'<div style="position:absolute;left:0;right:0;top:56px;text-align:center;font:700 24px Inter;color:#7E7896">New chat</div>'
             f'<div style="position:absolute;left:22px;right:22px;top:110px">'
             + bubble(POLICY, w=470)
             + bubble(ASK, w=440)
             + T(bubble('<span style="font:800 30px/1 Inter;letter-spacing:.2em;color:#7E7896">• • •</span>', me=False, w=200),
                 a + (0 if still else 0.3), b, "none" if still else "pop", 0.25, "position:relative")
             + '</div>' + field
             + T(send, a, b, "none", extra="right:0;bottom:0;width:100%;height:100%", pulse=0 if still else 0.06))
    return screen(inner, w, h)


def hook(a, b, first, still=False):
    hf = F["indi"]
    fx = "none" if first or still else "iris"
    inner = (T(serif("Returning it? / *Paste the policy.*", 140, hf), a, b, "none", extra="left:90px;top:300px") +
             T(chat_phone(a, b, still), a, b, "none", extra="left:240px;top:760px", base="rotate(-2.5deg)", float=0 if still else 5) +
             T(stamp(90, 1330, 120), a, b))
    return scene(hf["bg"], a, b, fx, inner, d=0.45, drift=0 if still else 0.006)


def returns():
    dur = 12.6
    s = [hook(0, 1.5, True)]
    # 1.5-5.0 payoff: the date, then Claude's exact words as proof
    pf = F["plum"]
    rep = REPLY_1.replace("November 19", "<b style=\"background:#FFF0C2\">November 19</b>")
    bub = (f'<div style="width:900px;background:#FFFFFF;border:5px solid {INK};border-radius:40px 40px 40px 10px;box-shadow:10px 10px 0 {INK};'
           f'padding:28px 34px;font:500 44px/1.28 Inter;color:{INK}">{rep}</div>')
    pay = (T(serif("Last day: / *Nov 19.*", 190, pf), 1.5, 5.0, "slam", 0.22, "left:90px;top:300px") +
           T(kicker("Claude's real reply, word for word", 32), 1.5, 5.0, "none", extra="left:90px;top:760px") +
           T(bub, 1.62, 5.0, "up", 0.25, "left:90px;top:820px") +
           T(f'<div style="width:900px;text-align:center">{button("Sale item: store credit only", 50, SUN)}</div>', 3.3, 5.0, "pop", 0.22,
             "left:90px;top:1200px") +
           T(small("Policy and dates made up for this post.", 36, INK, weight=700), 1.5, 5.0, "none", extra="left:90px;top:1335px"))
    s.append(scene(pf["bg"], 1.5, 5.0, "none", pay, d=0.3))
    # 5.0-8.9 Do this
    yf = F["yel"]
    do = (T('<div class="hand" style="font-size:120px;color:%s">Do this:</div>' % ACC, 5.0, 8.9, "slam", 0.2, "left:90px;top:300px;width:900px") +
          T(card(serif("Paste the policy. / Ask: *last day?*", 110, F["plum"], width=820), w=900, pad=40), 5.12, 8.9, "pop", 0.3,
            "left:90px;top:450px", float=3) +
          T(small("Add the day you bought it and the day it arrived.", 40, INK, weight=700), 6.0, 8.9, "up", 0.25, "left:90px;top:860px") +
          T(card(small("Leave out your order number and address.", 42, INK, 820, weight=700), w=900, pad=28, bg="#FFF0C2"),
            6.9, 8.9, "drop", 0.3, "left:90px;top:1010px", base="rotate(1.2deg)") +
          T(small("Works in ChatGPT, Claude or Gemini.", 34, INK, weight=700), 7.3, 8.9, "up", 0.25, "left:90px;top:1300px"))
    s.append(scene(yf["bg"], 5.0, 8.9, "wipe", do, d=0.28))
    # 8.9-11.8 follow
    nf = F["indi"]
    end = (T(serif("Follow to learn / what AI can / *really do.*", 128, nf), 8.9, 11.8, "up", 0.25, "left:90px;top:360px") +
           T(hand("one real test a day", 92, ACC, -3), 9.4, 11.8, "pop", 0.25, "left:90px;top:860px") +
           T(stamp(820, 1220, 130), 8.9, 11.8))
    s.append(scene(nf["bg"], 8.9, 11.8, "wipeD", end, d=0.26))
    s.append(hook(11.8, 99, False))
    return dur, page3(s, [1.5, 5.0, 6.9, 8.9]), page3([cover()], []), MUSIC / "hb-x-future-easy.mp3"


def cover():
    """Dedicated cover, kinetic big text: the stacked rule, a hand-drawn ring on the key word, small stamp."""
    hf = F["indi"]
    ring = (f'<svg width="720" height="300" viewBox="0 0 760 330" style="position:absolute;left:90px;top:10px;overflow:visible">'
            f'<path d="M420 22 C700 14 760 120 720 210 C670 320 120 330 40 220 C-20 130 120 30 460 26" fill="none" stroke="{ACC}" stroke-width="10" stroke-linecap="round"/></svg>')
    inner = (T(serif("Returning it?", 130, hf), 0, 99, "none", extra="left:90px;top:330px") +
             T(serif("Paste the", 190, hf), 0, 99, "none", extra="left:90px;top:500px") +
             T(f'<div style="position:relative;width:900px">{serif("*policy*", 290, hf)}{ring}</div>', 0, 99, "none", extra="left:90px;top:760px") +
             T(serif("first.", 190, hf), 0, 99, "none", extra="left:90px;top:1080px") +
             T(hand("AI finds your last day", 80, ACC, -3), 0, 99, "none", extra="left:90px;top:1290px") +
             T(stamp(830, 1090, 130), 0, 99))
    return scene(hf["bg"], 0, 99, "none", inner, d=0.1, drift=0)


REELS = {"returns": ("hb-reel-1027am-return-by", returns)}

if __name__ == "__main__":
    key = sys.argv[1]
    name, fn = REELS[key]
    dur, html, cov, track = fn()
    if "--frame" in sys.argv:
        from playwright.sync_api import sync_playwright
        from PIL import Image
        ts = [float(x) for x in sys.argv[sys.argv.index("--frame") + 1:]]
        p = O.SCRATCH / "prev"; p.mkdir(parents=True, exist_ok=True)
        (p / f"{key}.html").write_text(html); (p / f"{key}-c.html").write_text(cov)
        with sync_playwright() as pw:
            br = pw.chromium.launch(); pg = br.new_page(viewport={"width": W, "height": H})
            ims = []
            pg.goto((p / f"{key}-c.html").as_uri()); pg.wait_for_timeout(800); pg.evaluate("seek(50)")
            pg.screenshot(path=str(p / f"{key}-cover.png")); ims.append(Image.open(p / f"{key}-cover.png").convert("RGB").resize((360, 640)))
            pg.goto((p / f"{key}.html").as_uri()); pg.wait_for_timeout(800)
            for t in ts:
                f = p / f"{key}-{t}.png"; pg.evaluate(f"seek({t})"); pg.screenshot(path=str(f))
                ims.append(Image.open(f).convert("RGB").resize((360, 640)))
            br.close()
        sh = Image.new("RGB", (370 * len(ims), 640), "white")
        for i, im in enumerate(ims): sh.paste(im, (i * 370, 0))
        sh.save(p / f"{key}-sheet.jpg", quality=85); print(p / f"{key}-sheet.jpg")
    else:
        print(O.render(name, html, dur, track, cov))

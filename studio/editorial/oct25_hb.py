#!/usr/bin/env python3
"""Hourback Reels for Mon Oct 26 + Tue Oct 27, 7 pm (built Oct 25 2026 by the Hourback maker).

    python3 studio/editorial/oct25_hb.py hum|bill                 # render mp4 + dedicated cover -> media/studio-oct25/hourback/
    python3 studio/editorial/oct25_hb.py hum --frame 0 1.5 3 ...  # quick stills sheet for review

Fixes the Oct 22-24 kit's weaknesses (desk order Oct 25): frame 0 = ONE hook line + ONE object (+ the small stamp), no
answer card, no handwritten line, no grey "Take 1" beat; the payoff is SHOWN by ~2 s; 4 beats: hook -> payoff -> Do this -> send/follow -> loop.
Reuses the Take-Two kit (takereel.py) and the Oct 24 helpers (oct24_hb.py) by import; nothing in them is edited.

hum  = a real shipped feature (Google app, Search a song), verified Oct 25 on support.google.com/websearch/answer/7554088
       (Android + iPhone) and blog.google (hum to search, Oct 15 2020). The phone screen is DRAWN; no song title is claimed.
bill = a real run: studio/editorial/hb-oct25-run-bill.txt (Claude, Oct 25 2026). Bills made up for this post.
"""
import json, subprocess, sys, shutil, tempfile
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/recovery-oct22/hourback/build"))
sys.path.insert(0, str(REPO / "studio/editorial"))
sys.dont_write_bytecode = True
from takereel import (T, serif, hand, card, scene, F, INK, ACC, SUN, W, H, FPS, JS, edkit)  # noqa: E402
from reels import stamp  # noqa: E402
from oct24_hb import EXTRA_JS, small, kicker, button  # noqa: E402

OUT = REPO / "media/studio-oct25/hourback"
SCRATCH = Path("/tmp/claude-0/-home-claude-steadfold-autopost/83b8b3af-3981-538b-bfe3-7c8459a8a782/scratchpad/hbrender")
MUSIC = REPO / "media/music/library/v4"
FOLLOW = "Follow to learn what AI can really do, one real test a day."

EQ_JS = r"""
function eq(t){
 document.querySelectorAll('[data-eq]').forEach(el=>{
  const ph=+el.dataset.eq, a=+(el.dataset.t0||0), b=+(el.dataset.t1||999);
  let k = (t>=a && t<=b) ? Math.abs(Math.sin(t*7.3+ph)*0.6+Math.sin(t*3.1+ph*2)*0.4) : 0.12;
  el.style.height=(14+k*150)+'px';
 });
}
const _seek2=seek; seek=function(t){_seek2(t);eq(t)};
"""


def page3(scenes, shakes):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{edkit.css('hourback', W, H)}</style></head>
<body><div id="cam" style="position:absolute;inset:0;overflow:hidden">{''.join(scenes)}</div>
<script>window.SHAKES={json.dumps(shakes)};{JS}{EXTRA_JS}{EQ_JS}</script></body></html>"""


def render(name, html, dur, audio, cover_html):
    SCRATCH.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix=f"{name}-", dir=SCRATCH))
    (tmp / "p.html").write_text(html)
    (tmp / "c.html").write_text(cover_html)
    from playwright.sync_api import sync_playwright
    n = int(round(dur * FPS))
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto((tmp / "p.html").as_uri()); pg.wait_for_timeout(900)
        for i in range(n):
            pg.evaluate(f"seek({i / FPS:.4f})")
            pg.screenshot(path=str(tmp / f"f{i:04d}.jpg"), type="jpeg", quality=93)
        pg2 = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg2.goto((tmp / "c.html").as_uri()); pg2.wait_for_timeout(900)
        pg2.evaluate("seek(50)"); pg2.screenshot(path=str(tmp / "cover2x.png"))
        br.close()
    from PIL import Image
    Image.open(tmp / "cover2x.png").convert("RGB").resize((W, H), Image.LANCZOS).save(OUT / f"{name}-cover.jpg", quality=92)
    mp4 = OUT / f"{name}.mp4"
    fade = max(0, dur - 1.2)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(tmp / "f%04d.jpg"), "-i", str(audio),
                    "-filter_complex", f"[1:a]atrim=0:{dur},asetpts=N/SR/TB,afade=t=in:d=0.03,afade=t=out:st={fade}:d=1.2[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "19",
                    "-preset", "slow", "-threads", "1", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", "-t", str(dur), str(mp4)], check=True)
    shutil.rmtree(tmp)
    return mp4


def screen(inner, w=440, h=600, x=0, y=0):
    """A clean drawn phone (ink frame, cream screen) - the single object of the hum Reel."""
    return (f'<div style="width:{w}px;height:{h}px;background:{INK};border-radius:64px;padding:18px;box-shadow:12px 12px 0 rgba(42,29,71,.25)">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:48px;overflow:hidden;background:#FFFDF8">'
            f'<div style="position:absolute;left:50%;top:14px;transform:translateX(-50%);width:110px;height:26px;border-radius:99px;background:{INK}"></div>'
            f'{inner}</div></div>')


# ================================================================== A. hum to search (Mon Oct 26, 7 pm) — SEND TEST
def mic(size=170, bg=None):
    bg = bg or SUN
    return (f'<div style="width:{size}px;height:{size}px;border-radius:50%;background:{bg};border:6px solid {INK};display:flex;'
            f'align-items:center;justify-content:center"><svg width="{size*.5:.0f}" height="{size*.5:.0f}" viewBox="0 0 100 100">'
            f'<rect x="34" y="8" width="32" height="54" rx="16" fill="{INK}"/><path d="M20 46 Q20 78 50 78 Q80 78 80 46" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
            f'<rect x="46" y="78" width="8" height="14" fill="{INK}"/></svg></div>')


def notes(a, b, still=False):
    o = ""
    for i, (x, y, s) in enumerate([(-10, 170, 120), (530, 0, 110), (545, 330, 96)]):
        note = (f'<svg width="{s}" height="{s}" viewBox="0 0 100 100"><path d="M38 16 L82 6 L82 70" fill="none" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>'
                f'<path d="M38 16 L38 80" stroke="{INK}" stroke-width="9"/><ellipse cx="27" cy="81" rx="16" ry="12" fill="{ACC}" stroke="{INK}" stroke-width="5"/>'
                f'<ellipse cx="71" cy="71" rx="16" ry="12" fill="{SUN}" stroke="{INK}" stroke-width="5"/></svg>')
        o += T(note, a + (0 if still else 0.12 + i * 0.12), b, "none" if still else "pop", 0.25,
               f"left:{x}px;top:{y}px", float=0 if still else 9)
    return o


def hum_phone(a, b, mode, still=False):
    """mode: 'mic' (frame 0: mic + notes), 'hum' (eq bars, then matches list from a+1.1)."""
    w, h = 440, 600
    if mode == "mic":
        inner = (f'<div style="position:absolute;left:0;right:0;top:170px;display:flex;justify-content:center">' + T(mic(190), a, b, "none", extra="position:relative", pulse=0 if still else 0.05) + '</div>'
                 f'<div style="position:absolute;left:0;right:0;top:400px;text-align:center;font:600 34px Inter;color:{INK}">Hum the tune</div>')
        return screen(inner, w, h)
    bars = "".join(f'<div data-eq="{i * 0.9:.1f}" data-t0="{a}" data-t1="{a + 1.15}" style="width:26px;height:40px;background:{INK};border-radius:13px;margin:0 7px"></div>'
                   for i in range(9))
    hum = (T(f'<div style="position:absolute;left:0;top:0;width:404px;height:564px">'
             f'<div style="position:absolute;left:0;right:0;top:110px;text-align:center;font:700 32px Inter;color:#7E7896">Listening…</div>'
             f'<div style="position:absolute;left:0;right:0;top:200px;height:200px;display:flex;align-items:center;justify-content:center">{bars}</div></div>',
             a, a + 1.15, "none", extra="left:0;top:0", hard=1))

    def row(k, hi):
        bg = SUN if hi else "#FFFFFF"
        return (f'<div style="display:flex;align-items:center;gap:18px;background:{bg};border:4px solid {INK};border-radius:22px;padding:14px 16px;margin-bottom:14px">'
                f'<div style="width:72px;height:72px;border-radius:12px;background:linear-gradient(135deg,#C9CAF5,#FFD4BD);border:3px solid {INK};flex:none"></div>'
                f'<div style="flex:1"><div style="height:18px;width:{200 - k * 30}px;background:{INK};border-radius:9px;opacity:.85"></div>'
                f'<div style="height:14px;width:{130 - k * 20}px;background:#B9B4C9;border-radius:7px;margin-top:12px"></div></div>'
                + (f'<div style="font:800 46px Inter;color:{INK}">✓</div>' if hi else "") + '</div>')
    res = (T(f'<div style="font:700 30px Inter;color:#7E7896;margin:96px 0 18px 6px">Possible matches</div>', a + 1.15, b, "none", extra="position:relative")
           + T('<div style="position:relative">' + row(0, False)
               + T(row(0, True), a + 1.75, b, "pop", 0.2, "left:0;top:0;width:100%") + '</div>',
               a + 1.15, b, "none", extra="position:relative")
           + T(row(1, False), a + 1.15, b, "none", extra="position:relative")
           + T(row(2, False), a + 1.15, b, "none", extra="position:relative"))
    inner = hum + f'<div style="position:absolute;left:24px;right:24px;top:0">{res}</div>'
    return screen(inner, w, h)


def hum_hook(a, b, first, still=False):
    hf = F["indi"]
    fx = "none" if first or still else "iris"
    inner = (T(serif("For the friend / humming / *that song*", 150, hf), a, b, "none", extra="left:90px;top:330px") +
             T(f'<div style="position:relative;width:440px;height:600px">{hum_phone(a, b, "mic", still)}'
               f'<div style="position:absolute;left:-90px;top:-40px;width:620px;height:400px">{notes(a, b, still)}</div></div>',
               a, b, "none", extra="left:320px;top:880px", base="rotate(-3deg)", float=0 if still else 6) +
             T(stamp(90, 1330, 120), a, b))
    return scene(hf["bg"], a, b, fx, inner, d=0.45, drift=0 if still else 0.006)


def hum():
    dur = 12.4
    s = [hum_hook(0, 1.4, True)]
    # 1.4-4.5 payoff, shown: hum -> listening -> matches -> the one
    pf = F["plum"]
    pay = (T(serif("Hum it. / *Google names it.*", 112, pf), 1.4, 4.5, "none", extra="left:90px;top:300px") +
           T(hum_phone(1.4, 4.5, "hum"), 1.4, 4.5, "drop", 0.2, "left:320px;top:590px", base="rotate(2deg)") +
           T(hand("no words needed, just the tune", 72, ACC, -3), 3.3, 4.5, "pop", 0.25, "left:90px;top:1225px") +
           T(small("Drawn for this post. Real Google feature.", 40, INK, weight=700), 1.6, 4.5, "none", extra="left:90px;top:1345px"))
    s.append(scene(pf["bg"], 1.4, 4.5, "none", pay, d=0.3))
    # 4.5-8.6 Do this: the exact taps (drop 7.93 lands the tip)
    yf = F["yel"]
    arrow = f'<div style="font:800 56px Inter;color:{INK};width:900px;text-align:center">↓</div>'
    chain = ""
    for i, lab in enumerate(["Open the Google app", "Tap the mic", "Tap “Search a song”", "Hum for 10–15 seconds"]):
        t0 = 4.85 + i * 0.55
        chain += T(f'<div style="width:900px;text-align:center">{button(lab, 58, SUN if i == 3 else "#FFFDF8")}</div>', t0, 8.6, "pop", 0.25,
                   f"left:90px;top:{470 + i * 175}px")
        if i:
            chain += T(arrow, t0 - 0.12, 8.6, "up", 0.2, f"left:90px;top:{470 + i * 175 - 70}px")
    do = (T('<div class="hand" style="font-size:120px;color:%s">Do this:</div>' % ACC, 4.5, 8.6, "slam", 0.2, "left:90px;top:300px;width:900px") +
          chain +
          T(hand("no perfect pitch needed ✓", 76, ACC, -3), 7.93, 8.6, "slam", 0.2, "left:90px;top:1180px") +
          T(small("Free on Android and iPhone", 34, INK, weight=700), 6.6, 8.6, "up", 0.25, "left:90px;top:1310px"))
    s.append(scene(yf["bg"], 4.5, 8.6, "wipe", do, d=0.28))
    # 8.6-11.8 send + follow
    nf = F["indi"]
    end = (T(hand("send this to", 100, ACC, -3), 8.6, 11.8, "pop", 0.22, "left:90px;top:320px") +
           T(serif("the friend / humming / *that song*", 130, nf), 8.75, 11.8, "slam", 0.22, "left:90px;top:450px") +
           T(card(serif("Follow to learn / what AI can *really do.*", 80, F["plum"], width=820), w=900, pad=34),
             9.7, 11.8, "drop", 0.32, "left:90px;top:930px", base="rotate(-1deg)") +
           T(hand("one real test a day", 76, ACC, -3), 10.1, 11.8, "pop", 0.25, "left:90px;top:1200px") +
           T(stamp(860, 1320, 110), 8.6, 11.8))
    s.append(scene(nf["bg"], 8.6, 11.8, "wipeD", end, d=0.26))
    s.append(hum_hook(11.8, 99, False))
    return dur, page3(s, [1.4, 4.5, 7.93, 8.75]), page3([hum_hook(0, 99, True, still=True)], []), MUSIC / "hb-x-ta-da-funk.mp3"


# ================================================================== B. bill went up (Tue Oct 27, 7 pm) — real run
SEPT = [("Plan", "$65.00"), ("Loyalty discount", "−$15.00"), ("Phone payment", "$38.50"), ("911 fee", "$0.75"), ("Tax", "$11.60")]
OCT = [("Plan", "$65.00"), (None, None), ("Phone payment", "$38.50"), ("911 fee", "$0.75"), ("Tax", "$13.55")]
REPLY = "October is $16.95 higher because your $15 loyalty discount went away, and that also raised your tax."


def bill(month, rows, total, w=440, size=30, hi_t=None, a=0, b=99, still=False):
    o = (f'<div style="font:800 {size + 4}px Inter;letter-spacing:.06em;color:{INK};margin-bottom:6px">{month}</div>'
         f'<div style="height:4px;background:{INK};margin-bottom:6px"></div>')
    for lab, val in rows:
        if lab is None:
            cell = (f'<div style="display:flex;justify-content:center;padding:8px 0;border:3px dashed {ACC};border-radius:10px;margin:4px 0;'
                    f'font:700 {size - 2}px Inter;color:{ACC}">(no discount)</div>')
        else:
            cell = (f'<div style="display:flex;justify-content:space-between;padding:9px 0;border-bottom:2px dashed #D9D3E6;font:500 {size}px Inter;color:{INK}">'
                    f'<span>{lab}</span><span style="font-weight:700">{val}</span></div>')
        if lab == "Loyalty discount" and hi_t is not None:
            cell = (f'<div style="position:relative">{cell}'
                    + T(f'<div style="position:absolute;inset:-4px -10px;border:6px solid {ACC};border-radius:16px"></div>', a + hi_t, b,
                        "pop", 0.2, "left:0;top:0;width:100%;height:100%") + '</div>')
        o += cell
    o += (f'<div style="display:flex;justify-content:space-between;padding-top:12px;font:800 {size + 6}px Inter;color:{INK}">'
          f'<span>Total</span><span>{total}</span></div>')
    return (f'<div style="width:{w}px;background:#FFFFFF;border:5px solid {INK};border-radius:20px;box-shadow:10px 10px 0 {INK};'
            f'padding:26px 28px 24px">{o}</div>')


def bill_hook(a, b, first, still=False):
    hf = F["orng"]
    fx = "none" if first or still else "iris"
    paper = (f'<div style="width:560px;background:#FFFFFF;border:6px solid {INK};border-radius:24px;box-shadow:14px 14px 0 {INK};padding:34px 40px">'
             f'<div style="font:800 34px Inter;letter-spacing:.08em;color:#7E7896">PHONE BILL · OCTOBER</div>'
             f'<div style="height:4px;background:{INK};margin:14px 0 22px"></div>'
             f'<div style="display:flex;justify-content:space-between;align-items:baseline;font:800 52px Inter;color:{INK}">'
             f'<span>Total</span><span style="position:relative">$117.80'
             f'<svg width="330" height="170" viewBox="0 0 330 170" style="position:absolute;left:-50px;top:-48px;overflow:visible">'
             f'<path {"" if still else f"data-draw=1 data-t0={a + 0.15} data-t1={a + 0.7}"} d="M170 14 C300 10 330 70 300 120 C260 170 40 165 14 110 C-6 60 60 20 190 16" '
             f'fill="none" stroke="{ACC}" stroke-width="8" stroke-linecap="round"/></svg></span></div></div>')
    inner = (T(serif("Phone bill / *went up.* / Why?", 160, hf), a, b, "none", extra="left:90px;top:320px") +
             T(paper, a, b, "none", extra="left:260px;top:960px", base="rotate(-3deg)", float=0 if still else 5) +
             T(stamp(90, 1330, 120), a, b))
    return scene(hf["bg"], a, b, fx, inner, d=0.45, drift=0 if still else 0.006)


def bill_reel():
    dur = 12.8
    s = [bill_hook(0, 1.3, True)]
    # 1.3-3.2 paste both bills: the gap is SHOWN by ~2 s
    pf = F["plum"]
    two = (T(serif("Paste both bills. / *Ask AI why.*", 116, pf), 1.3, 3.2, "none", extra="left:90px;top:300px") +
           T(bill("SEPTEMBER", SEPT, "$100.85", hi_t=0.65, a=1.3, b=3.2), 1.3, 3.2, "drop", 0.22, "left:70px;top:580px", base="rotate(-1.5deg)") +
           T(bill("OCTOBER", OCT, "$117.80"), 1.42, 3.2, "drop", 0.22, "left:570px;top:600px", base="rotate(1.5deg)") +
           T(hand("the discount vanished", 84, ACC, -3), 2.05, 3.2, "pop", 0.22, "left:90px;top:1160px") +
           T(small("Bills made up for this post.", 40, INK, weight=700), 1.35, 3.2, "none", extra="left:90px;top:1300px"))
    s.append(scene(pf["bg"], 1.3, 3.2, "none", two, d=0.28))
    # 3.2-6.6 the real reply, quoted exactly
    nf = F["indi"]
    bub = (f'<div style="width:900px;background:#FFFFFF;border:5px solid {INK};border-radius:40px 40px 40px 10px;box-shadow:10px 10px 0 {INK};'
           f'padding:30px 36px;font:500 56px/1.25 Inter;color:{INK}">{REPLY.replace("$15 loyalty discount went away", "<b style=background:#FFF0C2>$15 loyalty discount went away</b>")}</div>')
    rep = (T(kicker("Claude's real reply, word for word", 36), 3.2, 6.6, "none", extra="left:90px;top:300px") +
           T(bub, 3.2, 6.6, "none", extra="left:90px;top:380px") +
           T(f'<div style="width:900px;text-align:center">{button("+$15.00 discount ended", 52, SUN)}</div>', 3.6, 6.6, "pop", 0.22, "left:90px;top:840px") +
           T(f'<div style="width:900px;text-align:center">{button("+$1.95 more tax", 52)}</div>', 3.85, 6.6, "pop", 0.22, "left:90px;top:970px") +
           T(small("Claude, by Anthropic · run Oct 25, 2026", 42, INK, weight=700), 3.2, 6.6, "none", extra="left:90px;top:1110px"))
    s.append(scene(nf["bg"], 3.2, 6.6, "none", rep, d=0.25))
    # 6.6-9.8 Do this + privacy (drop 7.81 lands the privacy card)
    yf = F["yel"]
    do = (T('<div class="hand" style="font-size:120px;color:%s">Do this:</div>' % ACC, 6.6, 9.8, "slam", 0.2, "left:90px;top:300px;width:900px") +
          T(card(serif("Paste 2 bills. / Ask: / *what changed?*", 110, F["plum"], width=820), w=900, pad=40),
            6.72, 9.8, "pop", 0.3, "left:90px;top:450px", float=3) +
          T(card(small("First, cover your account number and address.", 44, INK, 820, weight=700), w=900, pad=28, bg="#FFF0C2"),
            7.81, 9.8, "drop", 0.3, "left:90px;top:980px", base="rotate(1.2deg)") +
          T(small("Works in ChatGPT, Claude or Gemini.", 34, INK, weight=700), 7.2, 9.8, "up", 0.25, "left:90px;top:1300px"))
    s.append(scene(yf["bg"], 6.6, 9.8, "wipe", do, d=0.28))
    # 9.8-12.2 follow
    end = (T(serif("Follow to learn / what AI can / *really do.*", 128, nf), 9.8, 12.2, "up", 0.25, "left:90px;top:360px") +
           T(hand("one real test a day", 92, ACC, -3), 10.3, 12.2, "pop", 0.25, "left:90px;top:860px") +
           T(stamp(820, 1220, 130), 9.8, 12.2))
    s.append(scene(nf["bg"], 9.8, 12.2, "wipeD", end, d=0.26))
    s.append(bill_hook(12.2, 99, False))
    return dur, page3(s, [1.3, 3.3, 7.81, 9.8]), page3([bill_hook(0, 99, True, still=True)], []), MUSIC / "hb-x-smart-bounce.mp3"


REELS = {"hum": ("hb-reel-1026-hum-a-song-r2", hum), "bill": ("hb-reel-1027-bill-went-up-r2", bill_reel)}  # r2: gate fixes Oct 25 (r1 files kept)

if __name__ == "__main__":
    key = sys.argv[1]
    name, fn = REELS[key]
    dur, html, cover, track = fn()
    if "--frame" in sys.argv:
        from playwright.sync_api import sync_playwright
        from PIL import Image
        ts = [float(x) for x in sys.argv[sys.argv.index("--frame") + 1:]]
        p = SCRATCH / "prev"; p.mkdir(parents=True, exist_ok=True)
        (p / f"{key}.html").write_text(html); (p / f"{key}-c.html").write_text(cover)
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
        print(render(name, html, dur, track, cover))

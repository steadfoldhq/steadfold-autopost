#!/usr/bin/env python3
"""Hourback Reels for Oct 25-27 (built Oct 24 2026 by the Hourback Reel maker).

    python3 oct24_hb.py week|eraser|homework            # render mp4 + dedicated cover
    python3 oct24_hb.py week --frame 0 1.5 3 ...        # quick stills sheet for review

Imports the Oct 22 Take-Two kit (studio/recovery-oct22/hourback/build/takereel.py + reels.py) instead of rewriting it.
Real runs: week = studio/recovery-oct22/hourback/runs/run-b-week.txt (Claude, Oct 22);
homework = studio/editorial/hb-oct24-run-homework.txt (Claude, Oct 24). Eraser = a vendor feature, drawn (no output claimed).
"""
import json, subprocess, sys, shutil, tempfile, random
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/recovery-oct22/hourback/build"))
from takereel import (T, serif, hand, card, typed, scene, F, INK, ACC, SUN, W, H, FPS, JS, edkit)  # noqa: E402
from reels import WEEK, weekrows, stamp, phone  # noqa: E402

OUT = REPO / "media/studio-oct24/hourback"
SCRATCH = Path("/tmp/claude-0/hourback")
MUSIC = REPO / "media/music/library/v4"
SANS = "Inter"

EXTRA_JS = r"""
function draw(t){
 document.querySelectorAll('[data-draw]').forEach(el=>{
  const a=+el.dataset.t0,b=+el.dataset.t1,L=el.getTotalLength(); const p=Math.max(0,Math.min(1,(t-a)/(b-a)));
  el.style.strokeDasharray=L; el.style.strokeDashoffset=L*(1-p);
  const dot=el.dataset.dot&&document.getElementById(el.dataset.dot);
  if(dot){ if(t<a||t>b+0.25){dot.style.opacity=0}else{const q=el.getPointAtLength(L*p);dot.setAttribute('cx',q.x);dot.setAttribute('cy',q.y);dot.style.opacity=1} }
 });
}
const _seek=seek; seek=function(t){_seek(t);draw(t)};
"""


def page2(scenes, shakes):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{edkit.css('hourback', W, H)}</style></head>
<body><div id="cam" style="position:absolute;inset:0;overflow:hidden">{''.join(scenes)}</div>
<script>window.SHAKES={json.dumps(shakes)};{JS}{EXTRA_JS}</script></body></html>"""


def small(text, size=30, color="#5F5975", w=900, align="center", weight=600):
    return f'<div style="font:{weight} {size}px/1.25 {SANS};color:{color};width:{w}px;text-align:{align}">{text}</div>'


def kicker(text, size=30):
    return (f'<div style="font:700 {size}px {SANS};letter-spacing:.05em;color:#7E7896;text-transform:uppercase;'
            f'width:900px;text-align:center">{text}</div>')


def pillbox(text, size=46, bg=SUN, w=None):
    ww = f"width:{w}px;" if w else ""
    return (f'<div style="{ww}display:inline-block;background:{bg};border:5px solid {INK};border-radius:26px;box-shadow:8px 8px 0 {INK};'
            f'padding:16px 30px;font:700 {size}px/1.2 Poppins;color:{INK};text-align:center">{text}</div>')


def button(text, size=54, bg="#FFFDF8"):
    return (f'<div style="display:inline-block;background:{bg};border:5px solid {INK};border-radius:99px;box-shadow:7px 7px 0 {INK};'
            f'padding:14px 46px 12px;font:700 {size}px Poppins;color:{INK}">{text}</div>')


# ------------------------------------------------------------------ shared render
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
        pg.goto((tmp / "p.html").as_uri()); pg.wait_for_timeout(800)
        for i in range(n):
            pg.evaluate(f"seek({i / FPS:.4f})")
            pg.screenshot(path=str(tmp / f"f{i:04d}.jpg"), type="jpeg", quality=93)
        pg2 = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg2.goto((tmp / "c.html").as_uri()); pg2.wait_for_timeout(800)
        pg2.evaluate("seek(50)"); pg2.screenshot(path=str(tmp / "cover2x.png"))
        br.close()
    from PIL import Image
    Image.open(tmp / "cover2x.png").convert("RGB").resize((W, H), Image.LANCZOS).save(OUT / f"{name}-cover.jpg", quality=92)
    mp4 = OUT / f"{name}.mp4"
    fade = max(0, dur - 1.2)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(tmp / "f%04d.jpg"), "-i", str(audio),
                    "-filter_complex", f"[1:a]atrim=0:{dur},asetpts=N/SR/TB,afade=t=in:d=0.03,afade=t=out:st={fade}:d=1.2[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "19",
                    "-preset", "slow", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart",
                    "-t", str(dur), str(mp4)], check=True)
    shutil.rmtree(tmp)
    return mp4


def cover_page(scene_html):
    """Dedicated cover: the hook composition rebuilt as a still (every layer settled, no motion state)."""
    return page2([scene_html], [])


# ================================================================== A. week card r2 (Sun Oct 25, 7 pm) — CONTROL, no send line
PROMPT_WEEK = "Turn these into my week, Mon to Sat. One line a day: what to do, by when."
BUBBLES = [("Dentist", "Reminder: your cleaning is Tue Oct 27, 4:15 pm. Reply C"),
           ("School", "Pizza lunch Thursday. Send $6 by Wednesday."),
           ("Coach", "Soccer moved from Wed to Thu, 6 pm"),
           ("City", "Garbage and green bin: Monday, by 7 am"),
           ("Partner", "grab milk + dog food before Tue? also my mom's bday Sat")]


def week_hook(a, b, first, still=False):
    hf = F["indi"]
    fx = "none" if (first or still) else "iris"
    k = 0 if still else 1
    pv = card(f'<div style="font:800 44px Inter;margin-bottom:8px">Your week</div>' + weekrows(size=30), w=860, pad=30)
    inner = (T(serif("Sunday night? / *AI plans / your week.*", 112, hf), a, b, "none", extra="left:90px;top:300px") +
             T(pillbox("In an AI chat app:<br>ChatGPT, Claude or Gemini", 44), a + (0 if first else 0.1), b, "none" if first or still else "pop", 0.3,
               "left:90px;top:645px;width:900px;text-align:center", pulse=0 if still else 0.025) +
             T(pv, a + (0 if first or still else 0.25), b, "none" if first or still else "drop", 0.42, "left:110px;top:850px",
               base="rotate(-2deg)") +
             phone(880, 1210, 130, 14, a, b) +
             T(stamp(70, 1290, 110), a, b))
    return scene(hf["bg"], a, b, fx, inner, d=0.45, drift=0 if still else 0.006)


def week():
    dur = 14.5
    s = [week_hook(0, 2.2, True)]
    # 2.2–4.3 paste the texts
    pf = F["plum"]
    bub = ""
    for i, (who, m) in enumerate(BUBBLES):
        left = 90 if i % 2 == 0 else 190
        bub += T(f'<div style="max-width:800px;background:{"#FFFFFF" if i % 2 == 0 else "#E9E8FB"};border:4px solid {INK};'
                 f'border-radius:30px 30px 30px 8px;box-shadow:6px 6px 0 {INK};padding:14px 24px;font:500 33px/1.22 Inter;color:{INK}">'
                 f'<b style="font-weight:800">{who}:</b> {m}</div>',
                 2.4 + i * 0.32, 4.3, "whipL" if i % 2 else "whipR", 0.22, f"left:{left}px;top:{585 + i * 140}px")
    paste = (T(serif("Paste this / *week's texts*", 104, pf), 2.2, 4.3, "up", 0.25, "left:90px;top:300px") +
             T(kicker("into an AI chat app", 34), 2.3, 4.3, "up", 0.25, "left:90px;top:520px") + bub +
             T(small("Messages made up for this post.", 30), 3.2, 4.3, "up", 0.25, "left:90px;top:1300px"))
    s.append(scene(pf["bg"], 2.2, 4.3, "whipL", paste, d=0.3))
    # 4.3–6.4 the one sentence
    yf = F["yel"]
    sent = (T(serif("Then type / *one sentence:*", 112, yf), 4.3, 6.4, "up", 0.25, "left:90px;top:300px") +
            T(typed(PROMPT_WEEK, 4.45, 5.75, 50, "typed into the AI chat:"), 4.35, 6.4, "up", 0.25, "left:90px;top:560px") +
            T(hand("that's the whole prompt.", 72, ACC, -3), 5.85, 6.4, "pop", 0.25, "left:90px;top:1060px"))
    s.append(scene(yf["bg"], 4.3, 6.4, "wipeD", sent, d=0.25))
    # 6.4–9.9 Claude's real reply, then the check on the drop (7.93)
    head = (T(serif("*Claude's* real reply:", 96, pf), 6.4, 9.9, "none", extra="left:90px;top:300px") +
            T(small("Claude is an AI chat app by Anthropic. Quoted exactly.", 30), 6.5, 9.9, "up", 0.25, "left:90px;top:405px"))
    c1 = card(f'<div style="font:800 46px Inter;margin-bottom:6px">Your week</div>' + weekrows(6.55, 0.2, 7.93, 35), w=900, pad=32)
    c2 = card(f'<div style="font:800 46px Inter;margin-bottom:6px">Your week</div>' + weekrows(size=35, hi=1), w=900, pad=32)
    rep = (head + T(c1, 6.45, 7.93, "zoom", 0.3, "left:90px;top:470px", hard=1) +
           T(c2, 7.93, 9.9, "none", extra="left:90px;top:470px") +
           T(hand("sunday, sorted.", 74), 7.25, 7.93, "pop", 0.25, "left:90px;top:1110px", hard=1) +
           T(card(serif("Check it: the text / said ‘before Tue’. / It wrote *‘on Tue’.*", 64, pf, width=840), w=900, pad=28),
             7.93, 9.9, "slam", 0.22, "left:90px;top:1100px", base="rotate(-1deg)"))
    s.append(scene(pf["bg"], 6.4, 9.9, "zoom", rep, d=0.25))
    # 9.9–13.9 Do this
    nf = F["indi"]
    do = (T('<div class="hand" style="font-size:110px;color:%s">Do this:</div>' % ACC, 9.9, 13.9, "slam", 0.2, "left:90px;top:300px") +
          T(card(serif("Paste your / week's texts / *into ChatGPT.*", 104, nf, width=820), w=900, pad=40),
            10.05, 13.9, "pop", 0.3, "left:90px;top:450px") +
          T(card(small("Ask: one line a day.<br>Claude or Gemini work too.", 44, INK, 820, weight=700), w=900, pad=30, bg="#FFF0C2"),
            10.7, 13.9, "drop", 0.3, "left:90px;top:920px", base="rotate(1.2deg)") +
          T(stamp(96, 1220, 130), 9.9, 13.9))
    s.append(scene(nf["bg"], 9.9, 13.9, "wipe", do, d=0.28))
    s.append(week_hook(13.9, 99, False))
    return dur, page2(s, [2.2, 7.93, 9.9]), cover_page(week_hook(0, 99, True, still=True)), MUSIC / "hb-x-ta-da-funk.mp3"


# ================================================================== B. photo eraser (Mon Oct 26, 7 pm)
def beach(stranger=True, w=520, h=640, uid="b"):
    """Drawn beach photo: a dog seen from behind; a stranger in an orange jacket walks through. No faces."""
    st = ""
    if stranger:
        st = (f'<g id="st{uid}"><rect x="372" y="300" width="15" height="70" rx="6" fill="#33384A"/><rect x="392" y="300" width="15" height="70" rx="6" fill="#2B3040"/>'
              f'<path d="M362 220 Q390 205 418 220 L424 310 L356 310 Z" fill="#FF8A3D" stroke="{INK}" stroke-width="3"/>'
              f'<rect x="346" y="228" width="16" height="66" rx="8" fill="#F07A2E" transform="rotate(12 354 228)"/>'
              f'<circle cx="390" cy="196" r="22" fill="#8A5A44"/><path d="M368 192 Q390 168 412 192 Z" fill="#2A2238"/></g>')
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 520 640" style="display:block;border-radius:22px">'
            f'<defs><linearGradient id="sky{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#BFD4FF"/><stop offset="1" stop-color="#FFE6D3"/></linearGradient>'
            f'<linearGradient id="sea{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6E88E6"/><stop offset="1" stop-color="#9DB3F2"/></linearGradient></defs>'
            f'<rect width="520" height="640" fill="url(#sky{uid})"/><circle cx="420" cy="110" r="46" fill="#FFC94D"/>'
            f'<rect y="250" width="520" height="90" fill="url(#sea{uid})"/>'
            f'<path d="M0 320 Q130 300 260 318 T520 312 L520 640 L0 640Z" fill="#F6DDB0"/>'
            f'<path d="M0 340 Q140 326 270 342 T520 334" fill="none" stroke="#FFFFFF" stroke-width="6" opacity=".7"/>'
            f'{st}'
            # dog from behind: body, head, ears, tail
            f'<g><ellipse cx="200" cy="520" rx="92" ry="64" fill="#C98A4B" stroke="{INK}" stroke-width="4"/>'
            f'<circle cx="200" cy="430" r="52" fill="#C98A4B" stroke="{INK}" stroke-width="4"/>'
            f'<path d="M156 410 Q140 360 168 392 Z" fill="#8E5A2E" stroke="{INK}" stroke-width="4"/>'
            f'<path d="M244 410 Q260 360 232 392 Z" fill="#8E5A2E" stroke="{INK}" stroke-width="4"/>'
            f'<path d="M286 520 Q340 470 318 440" fill="none" stroke="#C98A4B" stroke-width="18" stroke-linecap="round"/>'
            f'<path d="M150 470 Q200 488 250 470" fill="none" stroke="#FF8A3D" stroke-width="10" stroke-linecap="round"/></g>'
            f'</svg>')


def phoneframe(inner, w=560, h=700):
    return (f'<div style="width:{w}px;height:{h}px;background:#1B1B1F;border-radius:60px;padding:20px;box-shadow:14px 14px 0 {INK}">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:42px;overflow:hidden;background:#111">{inner}</div></div>')


def erase_scene_parts(a, b, t_circle=(0.15, 0.95), t_erase=(1.05, 1.6), still=False, uid="h"):
    """Phone with the beach photo; finger circles the stranger, then pixel squares of the clean photo cover him."""
    pw, ph = 520, 640
    base = beach(True, pw, ph, uid + "1")
    clean = beach(False, pw, ph, uid + "2")
    # pixel squares over the stranger's box (x 330-440, y 160-380 in photo coords)
    sq = ""
    if not still:
        rnd = random.Random(7)
        cells = [(x, y) for x in range(326, 446, 30) for y in range(156, 386, 30)]
        rnd.shuffle(cells)
        for i, (x, y) in enumerate(cells):
            t0 = t_erase[0] + (t_erase[1] - t_erase[0]) * i / len(cells)
            sq += (f'<div data-in="{a + t0:.3f}" data-out="{b}" data-fx="pop" data-d="0.12" style="position:absolute;left:{x}px;top:{y}px;'
                   f'width:30px;height:30px;overflow:hidden"><div style="position:absolute;left:{-x}px;top:{-y}px">{clean}</div></div>')
        sq += T(clean, a + t_erase[1] + 0.05, b, "none", extra="left:0;top:0")
    ring = (f'<svg width="{pw}" height="{ph}" viewBox="0 0 520 640" style="position:absolute;left:0;top:0">'
            f'<path data-draw="1" data-t0="{a + t_circle[0]}" data-t1="{a + t_circle[1]}" data-dot="dot{uid}" '
            f'd="M392 146 C470 150 470 380 392 392 C312 396 318 150 386 150" fill="none" stroke="{SUN}" stroke-width="12" stroke-linecap="round"/>'
            f'<circle id="dot{uid}" r="22" fill="#FFFFFF" stroke="{INK}" stroke-width="5" style="opacity:0"/></svg>')
    ring_layer = ring if still is False else ""
    photo = f'<div style="position:relative;width:{pw}px;height:{ph}px">{base}{sq}' + (
        T(ring_layer, a, a + t_erase[1] + 0.1, "none", extra="left:0;top:0", hard=1) if not still else
        f'<svg width="{pw}" height="{ph}" viewBox="0 0 520 640" style="position:absolute;left:0;top:0"><path d="M392 146 C470 150 470 380 392 392 C312 396 318 150 386 150" fill="none" stroke="{SUN}" stroke-width="12" stroke-linecap="round"/></svg>'
    ) + '</div>'
    return phoneframe(photo)


def eraser_hook(a, b, first, still=False):
    hf = F["yel"]
    fx = "none" if first or still else "iris"
    inner = (T(serif("Stranger in / *your best photo?*", 124, hf), a, b, "none", extra="left:90px;top:300px") +
             T(erase_scene_parts(a, b, still=still, uid="h" + str(int(a * 10))), a, b, "none", extra="left:260px;top:560px",
               base="rotate(-2deg) scale(.82)") +
             (T(hand("circle them. gone.", 80, ACC, -3), a + 1.65, b, "pop", 0.25, "left:90px;top:1215px") if not still else
              T(hand("circle them. gone.", 80, ACC, -3), a, b, "none", extra="left:90px;top:1215px")) +
             T(small("Drawn for this post.", 36, "#3E3558", weight=700), a, b, "none", extra="left:90px;top:1335px") +
             T(stamp(850, 1180, 120), a, b))
    return scene(hf["bg"], a, b, fx, inner, d=0.45, drift=0 if still else 0.006)


def eraser():
    dur = 14.0
    s = [eraser_hook(0, 2.0, True)]
    # 2.0–3.6 payoff: before / after
    pf = F["plum"]
    ba = (T(serif("Your phone's AI / *erases them.*", 120, pf), 2.0, 3.6, "up", 0.25, "left:90px;top:300px") +
          T(f'<div style="border:5px solid {INK};border-radius:26px;overflow:hidden;box-shadow:8px 8px 0 {INK}">{beach(True, 420, 517, "ba1")}</div>',
            2.1, 3.6, "whipR", 0.28, "left:90px;top:600px", base="rotate(-2deg)") +
          T(f'<div style="border:5px solid {INK};border-radius:26px;overflow:hidden;box-shadow:8px 8px 0 {INK}">{beach(False, 420, 517, "ba2")}</div>',
            2.45, 3.6, "whipL", 0.28, "left:570px;top:600px", base="rotate(2deg)") +
          T(pillbox("before", 40, "#FFFDF8"), 2.3, 3.6, "pop", 0.25, "left:200px;top:1150px") +
          T(pillbox("after", 40), 2.65, 3.6, "pop", 0.25, "left:700px;top:1150px") +
          T(small("Drawn for this post.", 36, "#3E3558", weight=700), 2.0, 3.6, "none", extra="left:90px;top:1250px"))
    s.append(scene(pf["bg"], 2.0, 3.6, "whipL", ba, d=0.3))
    # 3.6–6.0 iPhone path
    nf = F["indi"]
    arrow = f'<div style="font:800 60px Inter;color:{INK};width:900px;text-align:center">↓</div>'

    def path(labels, a0, b0, top=480, step=0.42, gap=165):
        o = ""
        for i, lab in enumerate(labels):
            o += T(f'<div style="width:900px;text-align:center">{button(lab, 66, SUN if i == len(labels) - 1 else "#FFFDF8")}</div>',
                   a0 + i * step, b0, "pop", 0.25, f"left:90px;top:{top + i * gap}px")
            if i:
                o += T(arrow, a0 + i * step - 0.12, b0, "up", 0.2, f"left:90px;top:{top + i * gap - 62}px")
        return o
    ip = (T(serif("On *iPhone:*", 120, nf), 3.6, 6.0, "up", 0.25, "left:90px;top:300px") +
          path(["Photos", "Edit", "Clean Up"], 3.8, 6.0) +
          T(hand("then circle them.", 84, ACC, -3), 5.05, 6.0, "pop", 0.25, "left:90px;top:990px") +
          T(small("iPhone 15 Pro or newer, iOS 18.1 or later", 36, INK), 5.3, 6.0, "up", 0.25, "left:90px;top:1120px") +
          phone(860, 1180, 130, 14, 3.6, 6.0))
    s.append(scene(nf["bg"], 3.6, 6.0, "wipe", ip, d=0.28))
    # 6.0–8.6 any phone: Google Photos (drop 7.81 lands on Erase)
    yf = F["orng"]
    gp = (T(serif("Any phone: / *Google Photos*", 112, yf), 6.0, 8.6, "up", 0.25, "left:90px;top:300px") +
          path(["Edit", "Magic Eraser", "Erase"], 6.35, 8.6, top=590, step=0.65) +
          T(hand("circle them, then Erase.", 74, ACC, 3), 7.81, 8.6, "pop", 0.25, "left:90px;top:1080px") +
          T(small("Free app on Android or iPhone", 36, INK), 6.6, 8.6, "up", 0.25, "left:90px;top:1210px"))
    s.append(scene(yf["bg"], 6.0, 8.6, "zoom", gp, d=0.25))
    # 8.6–11.9 Do this + send + follow (face beat cut Oct 24 gate; motion kept to the loop)
    do = (T('<div class="hand" style="font-size:110px;color:%s">Do this:</div>' % ACC, 8.6, 11.9, "slam", 0.2, "left:90px;top:300px") +
          T(card(serif("Photos, Edit, / Clean Up, *circle them.*", 84, nf, width=820), w=900, pad=36),
            8.75, 11.9, "pop", 0.3, "left:90px;top:450px", float=4) +
          T(small("Android: Google Photos, Edit, Magic Eraser.", 36, INK, weight=700), 9.15, 11.9, "up", 0.25, "left:90px;top:790px") +
          T(hand("send this to whoever takes the group photos", 56, ACC, -2, 900), 9.6, 11.9, "pop", 0.25, "left:90px;top:880px") +
          T(card(small("Follow to learn what AI can really do, one real test a day.", 38, INK, 820, weight=700), w=900, pad=24, bg="#FFF0C2"),
            10.15, 11.9, "drop", 0.3, "left:90px;top:1010px") +
          T(f'<svg width="900" height="360" viewBox="0 0 900 360"><path data-draw="1" data-t0="10.7" data-t1="11.4" '
            f'd="M560 104 C720 90 874 108 868 156 C862 208 540 214 430 188 C368 168 404 106 560 102" fill="none" stroke="{ACC}" stroke-width="7" stroke-linecap="round"/></svg>',
            10.7, 11.9, "none", extra="left:90px;top:450px") +
          T(stamp(870, 1262, 110), 8.6, 11.9))
    s.append(scene(nf["bg"], 8.6, 11.9, "wipe", do, d=0.28))
    s.append(eraser_hook(11.9, 99, False))
    return 12.6, page2(s, [2.0, 7.81, 8.6]), cover_page(eraser_hook(0, 99, True, still=True)), MUSIC / "hb-x-smart-bounce.mp3"


# ================================================================== C. homework hints (Tue Oct 27, 7 pm)
Q = "A pizza is cut into 8 equal slices. Sam eats 3 slices and Priya eats 2. What fraction of the pizza is left?"
HINTS = ["Hint 1: How many slices was the whole pizza cut into? That number goes on the bottom of the fraction.",
         "Hint 2: How many slices got eaten altogether? Add Sam's and Priya's.",
         "Hint 3: Take the eaten slices away from the whole pizza. How many are left? That number goes on top."]


def pizza(size=300, eaten=0, glow_left=False):
    import math
    o = f'<svg width="{size}" height="{size}" viewBox="0 0 200 200"><circle cx="100" cy="100" r="94" fill="#E8A54B" stroke="{INK}" stroke-width="5"/>'
    for i in range(8):
        a0, a1 = math.radians(-90 + i * 45), math.radians(-90 + (i + 1) * 45)
        x0, y0, x1, y1 = 100 + 82 * math.cos(a0), 100 + 82 * math.sin(a0), 100 + 82 * math.cos(a1), 100 + 82 * math.sin(a1)
        gone = i < eaten
        fill = "#E3DFEA" if gone else ("#FFC94D" if glow_left else "#FFD98A")
        o += f'<path d="M100 100 L{x0:.1f} {y0:.1f} A82 82 0 0 1 {x1:.1f} {y1:.1f} Z" fill="{fill}" stroke="{INK}" stroke-width="3"/>'
        if not gone:
            cx, cy = 100 + 52 * math.cos((a0 + a1) / 2), 100 + 52 * math.sin((a0 + a1) / 2)
            o += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="8" fill="#D4532A"/>'
    return o + "</svg>"


def worksheet(a, b):
    return card(f'<div style="font:700 32px Inter;letter-spacing:.05em;color:#7E7896;text-transform:uppercase;margin-bottom:12px">Grade 5 · question 4</div>'
                f'<div style="font:600 54px/1.24 Inter">{Q}</div>', w=900, pad=36)


def homework_hook(a, b, first, still=False):
    hf = F["indi"]
    fx = "none" if first or still else "iris"
    k = 0 if still else 1
    inner = (T(serif("Kid's fractions. / *You forgot how?*", 118, hf), a, b, "none", extra="left:90px;top:300px") +
             T(worksheet(a, b), a, b, "none", extra="left:90px;top:560px", base="rotate(-1.2deg)") +
             T(pizza(340), a, b, "none", extra="left:100px;top:1000px", spin=0 if still else 12) +
             T(hand("help, without / giving the answer".replace(" / ", "<br>"), 76, ACC, -3, 520), a + 0.15 * k, b,
               "none" if still else "pop", 0.25, "left:470px;top:1060px") +
             T(small("Question made up for this post.", 32, "#3E3558", weight=700), a, b, "none", extra="left:90px;top:1365px") +
             T(stamp(880, 1250, 110), a, b))
    return scene(hf["bg"], a, b, fx, inner, d=0.45, drift=0 if still else 0.006)


def homework():
    dur = 14.0
    s = [homework_hook(0, 1.2, True)]
    # 1.2–3.2: the request typed from its start, the pasted question as a block, then the payoff
    pf = F["yel"]
    t1 = "My kid is in Grade 5 and stuck on this homework question:"
    t2 = "Give me 3 short hints I can say out loud, one at a time. Don't give the answer."

    def tline(txt, t0, t1_, size=54, lines=2):
        return T(f'<div data-type="{txt}" data-t0="{t0}" data-t1="{t1_}" style="font:500 {size}px/1.24 Inter;min-height:{int(size * 1.24 * lines)}px">'
                 f'<span class="tx"></span><span class="caret" style="display:inline-block;width:5px;height:{size}px;background:{INK};vertical-align:-8px;margin-left:3px"></span></div>',
                 t0 - 0.02, 3.2, "none", extra="position:relative")
    pinner = (f'<div style="font:700 30px Inter;letter-spacing:.05em;color:#7E7896;text-transform:uppercase;margin-bottom:12px">typed into Claude, an AI chat app</div>'
              + tline(t1, 1.25, 1.75) +
              T(f'<div style="margin:12px 0 16px;background:#EFEDF6;border-left:10px solid {SUN};border-radius:14px;padding:14px 20px;font:500 44px/1.22 Inter;color:#3E3558">'
                f'“A pizza is cut into 8 equal slices. Sam eats 3… What fraction of the pizza is left?”</div>',
                1.75, 3.2, "pop", 0.2, "position:relative") +
              tline(t2, 1.95, 2.65, lines=3))
    req = (T(card(pinner, w=900, pad=34), 1.2, 3.2, "up", 0.22, "left:90px;top:300px") +
           T(serif("AI gives / *hints, not / the answer.*", 112, pf), 2.65, 3.2, "slam", 0.2, "left:90px;top:1010px"))
    s.append(scene(pf["bg"], 1.2, 3.2, "wipeD", req, d=0.25))
    # 3.2–8.22: Claude's real reply, one hint at a time, large; the pizza acts each one out
    nf = F["plum"]
    starts = [3.3, 5.0, 6.3]
    notes = ["8 slices<br>in all", "3 + 2<br>eaten", "how many<br>left?"]
    rep = T(kicker("Claude's real reply · quoted exactly", 34), 3.2, 8.22, "none", extra="left:90px;top:300px")
    for i, h in enumerate(HINTS):
        a0 = starts[i]; b0 = starts[i + 1] if i < 2 else 8.22; last = i == 2
        kw = {} if last else {"hard": 1}
        rep += T(f'<div style="width:900px;background:{"#FFFFFF" if i != 1 else "#E9E8FB"};border:5px solid {INK};border-radius:36px 36px 36px 10px;'
                 f'box-shadow:8px 8px 0 {INK};padding:22px 30px;font:500 58px/1.22 Inter;color:{INK}">{h}</div>',
                 a0, b0, "whipR" if i % 2 == 0 else "whipL", 0.25, "left:90px;top:370px", **kw)
        rep += T(pizza(400, 0 if i == 0 else 5, i == 2), a0, b0, "pop" if i == 0 else "none", 0.25, "left:90px;top:840px", **kw)
        rep += T(hand(notes[i], 92, ACC, -4, 460), a0 + 0.25, b0, "pop", 0.25, "left:520px;top:930px", **kw)
        dots = "".join(f'<span style="display:inline-block;width:34px;height:34px;border-radius:50%;margin:0 12px;border:4px solid {INK};'
                       f'background:{SUN if d_ <= i else "#FFFDF8"}"></span>' for d_ in range(3))
        rep += T(f'<div style="width:900px;text-align:center">{dots}</div>', a0, b0, "none", extra="left:90px;top:1290px", **kw)
    s.append(scene(nf["bg"], 3.2, 8.22, "zoom", rep, d=0.25))
    # 8.22–9.8 the check (on the drop)
    cf = F["yel"]
    chk = (T(serif("Check it: did / *the answer slip in?*", 108, cf), 8.22, 9.8, "slam", 0.22, "left:90px;top:300px") +
           T(hand("ours didn't. ✓", 104, ACC, -4), 8.55, 9.8, "pop", 0.25, "left:90px;top:560px") +
           T(pizza(360, 5, True), 8.4, 9.8, "drop", 0.3, "left:360px;top:720px") +
           T(serif("It's *3/8*. Let / them say it.", 96, cf), 8.9, 9.8, "up", 0.25, "left:90px;top:1120px"))
    s.append(scene(cf["bg"], 8.22, 9.8, "whipL", chk, d=0.25))
    # 9.8–13.3 Do this + send + follow (card shown as the wipe lands: no ghosted first frame)
    df = F["indi"]
    do = (T('<div class="hand" style="font-size:110px;color:%s">Do this:</div>' % ACC, 9.8, 13.3, "none", extra="left:90px;top:300px") +
          T(card(serif("Type the question. / Add: *‘Hints, not / the answer.’*", 96, df, width=820), w=900, pad=38),
            9.8, 13.3, "none", extra="left:90px;top:440px", float=4) +
          T(small("In ChatGPT, Claude or Gemini.", 46, INK, weight=700), 10.3, 13.3, "up", 0.25, "left:90px;top:840px") +
          T(hand("send this to whoever's on homework duty tonight", 62, ACC, -2, 900), 10.8, 13.3, "pop", 0.25, "left:90px;top:930px") +
          T(card(small("Follow to learn what AI can really do, one real test a day.", 44, INK, 830, weight=700), w=900, pad=26, bg="#FFF0C2"),
            11.4, 13.3, "drop", 0.3, "left:90px;top:1110px") +
          T(stamp(880, 1290, 110), 9.8, 13.3))
    s.append(scene(df["bg"], 9.8, 13.3, "wipe", do, d=0.28))
    s.append(homework_hook(13.3, 99, False))
    return dur, page2(s, [1.2, 2.65, 8.22, 9.8]), cover_page(homework_hook(0, 99, True, still=True)), MUSIC / "hb-x-future-easy.mp3"


REELS = {"week": ("hb-reel-1025-week-card-r2", week), "eraser": ("hb-reel-1026-photo-eraser", eraser),
         "homework": ("hb-reel-1027-homework-hints", homework)}

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
            pg.goto((p / f"{key}-c.html").as_uri()); pg.wait_for_timeout(700); pg.evaluate("seek(50)")
            pg.screenshot(path=str(p / f"{key}-cover.png")); ims.append(Image.open(p / f"{key}-cover.png").convert("RGB").resize((360, 640)))
            pg.goto((p / f"{key}.html").as_uri()); pg.wait_for_timeout(700)
            for t in ts:
                f = p / f"{key}-{t}.png"; pg.evaluate(f"seek({t})"); pg.screenshot(path=str(f))
                ims.append(Image.open(f).convert("RGB").resize((360, 640)))
            br.close()
        sh = Image.new("RGB", (370 * len(ims), 640), "white")
        for i, im in enumerate(ims): sh.paste(im, (i * 370, 0))
        sh.save(p / f"{key}-sheet.jpg", quality=85); print(p / f"{key}-sheet.jpg")
    else:
        print(render(name, html, dur, track, cover))

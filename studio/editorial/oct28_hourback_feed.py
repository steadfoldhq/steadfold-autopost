#!/usr/bin/env python3
"""Hourback series 'AI, for real · Day 11' (Mon Nov 2 2026, 17:45), built Oct 28 2026 by the Hourback maker.

    python3 studio/editorial/oct28_hourback_feed.py   -> media/studio-oct28/hourback/hb-day11-gift-for-dad/0N.jpg

Same series layout as Day 10 (studio/editorial/oct26_hourback_feed.py d10_build: Look B pills cover with one drawn object +
indigo prompt-card slide + yellow white-list-card slide). Real run: studio/editorial/hb-oct28-run-gift.txt (claude -p, fresh
session, Oct 28 2026). Slide 2 = the run's prompt word for word (yellow chips = the parts to change). Slide 3 = 3 of the 5
ideas, word for word (bold heading + price as Claude wrote them; the rest of each line is in the caption).
Reuses oct26_hourback_feed / covers / specs by import; edits none of them.
"""
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oct26_hourback_feed as D  # noqa: E402  (imports specs + covers with the same patches as Day 10)

C, K, specs, chip = D.C, D.K, D.specs, D.chip
HB, W, H = D.HB, D.W, D.H
D11 = "studio-oct28/hourback/hb-day11-gift-for-dad"
specs.POSTS[D11] = dict(
    brand=HB, fmt="series",
    cover=dict(lay="pills", f="orng", kicker="ai, for real · day 11", text="Dad says he / *needs nothing?*", obj="chat",
               at="bl", save="new one<br>every Mon · Wed · Fri"),
    slides=[dict(f="yel", text="Gift ideas for Dad. / *It wrote:*",
                 items=["Heirloom seed collection (~$25)", "Premium whole-bean coffee sampler (~$30)",
                        "Personalized garden kneeler or stool (~$40)"])])
SAVE3 = "real reply, shortened · Claude's own numbers<br>3 of 5 shown, all 5 in the caption"


def giftbox(x, y, w=360, rot=-6):
    """One drawn object for the Day 11 cover: a wrapped gift with a yellow bow and a seed-packet tag."""
    ink = "#2A1D47"
    svg = (f'<svg width="{w}" height="{w}" viewBox="0 0 360 360">'
           f'<ellipse cx="180" cy="330" rx="160" ry="18" fill="rgba(42,29,71,.15)"/>'
           f'<rect x="40" y="150" width="280" height="175" rx="14" fill="#5E54C9" stroke="{ink}" stroke-width="6"/>'
           f'<rect x="26" y="112" width="308" height="56" rx="12" fill="#7A71DB" stroke="{ink}" stroke-width="6"/>'
           f'<rect x="156" y="112" width="48" height="213" fill="#FFC94D" stroke="{ink}" stroke-width="6"/>'
           f'<path d="M180 112 C 120 40, 70 80, 110 110 Z M180 112 C 240 40, 290 80, 250 110 Z" fill="#FFC94D" stroke="{ink}" stroke-width="6" stroke-linejoin="round"/>'
           f'<circle cx="180" cy="110" r="16" fill="#FF8A3D" stroke="{ink}" stroke-width="6"/>'
           f'<path d="M250 160 L300 200" stroke="{ink}" stroke-width="4"/>'
           f'<rect x="282" y="196" width="62" height="80" rx="8" fill="#FFF5EA" stroke="{ink}" stroke-width="5" transform="rotate(12 313 236)"/>'
           f'<path d="M300 240 q12 -26 24 0 q-12 10 -24 0" fill="#5E8C4A" stroke="{ink}" stroke-width="3" transform="rotate(12 313 236)"/></svg>')
    return f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);z-index:3">{svg}</div>'


PROMPT = (f"Help me pick a gift for my {chip('dad')}. He's {chip('64')}, loves {chip('gardening and crossword puzzles')}, "
          f"drinks his coffee black, and says he doesn't need anything. My budget is {chip('$40')}. Give me 5 ideas, one line each.")


def slide2():
    f = K.FIELDS[HB]["indi"]
    ink = f["ink"]
    body = C.head(HB, f, "In ChatGPT, Claude or Gemini,", 110, 90, 64)
    body += C.head(HB, f, "type this / *about your person:*", 200, 330, 160)
    body += (f'<div style="position:absolute;left:80px;right:80px;top:560px;background:#FFFFFF;border:4px solid {ink};border-radius:36px;'
             f'box-shadow:0 16px 0 {ink};padding:30px 44px 36px;z-index:3;color:{ink}">'
             f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px">'
             f'<span style="font:700 28px Inter;letter-spacing:.12em;text-transform:uppercase;opacity:.7">Copy this prompt</span>'
             f'<span style="font:700 26px Inter;background:{ink};color:#FFF5EA;border-radius:99px;padding:8px 22px">⧉ copy</span></div>'
             f'<div style="font:500 44px/1.5 Inter">{PROMPT}</div></div>')
    body += K.save_line("change the yellow words to yours", 50, 1120, 720, 54, -3, HB)
    body += f'<div style="position:absolute;right:60px;top:40px;font:600 30px/1 Fraunces;color:{ink};opacity:.55;z-index:5">2/3</div>'
    body += K.stamp(HB, W - 200, H - 185, 145, -12)
    return C.page(HB, "indi", body, W, H)


def claude_numbers(html):
    """Number circles show Claude's own numbering (ideas 4, 1, 5 of its 5), not slide positions."""
    for k, n in ((1, "#4#"), (2, "#1#"), (3, "#5#")):
        a = f'line-height:88px">{k}</span>'
        assert html.count(a) == 1, k
        html = html.replace(a, f'line-height:88px">{n}</span>')
    return html.replace(">#4#<", ">4<").replace(">#1#<", ">1<").replace(">#5#<", ">5<")


def build(r):
    spec = specs.POSTS[D11]
    d = C.REPO / "media" / D11
    d.mkdir(parents=True, exist_ok=True)
    c = spec["cover"]
    _o = K.obj
    C.K.obj = lambda name, *a, **k: giftbox(40, 880) if name == "chat" else _o(name, *a, **k)
    try:
        cov = C.lay_pills(HB, c)
    finally:
        C.K.obj = _o
    return [r.shot(C.page(HB, c["f"], cov, W, H), W, H, d / "01.jpg"),
            r.shot(slide2(), W, H, d / "02.jpg"),
            r.shot(C.page(HB, "yel", claude_numbers(C.inner(HB, spec["slides"][0], 2, 3)) + K.save_line(SAVE3, 70, 1090, 760, 46, -3, HB), W, H),
                   W, H, d / "03.jpg")]


if __name__ == "__main__":
    r = C.R()
    try:
        print(build(r))
    finally:
        r.close()

#!/usr/bin/env python3
"""Hourback series 'AI, for real · Day 12' (Wed Nov 4 2026, 17:45), built Nov 1 2026 by the Hourback maker.

    python3 studio/editorial/nov01_hourback_feed.py   -> media/studio-nov01/hourback/hb-day12-potluck/0N.jpg

Same series layout as Day 11 (oct28_hourback_feed.py: Look B pills cover with one drawn object + indigo prompt-card
slide + yellow white-list-card slide). Real run: studio/editorial/hb-nov01-run-potluck.txt (claude -p, fresh session,
Nov 1 2026). Slide 2 = the run's prompt word for word (yellow chips = the parts to change). Slide 3 = the 3 dish names
word for word, in Claude's own order (the rest of each line is in the caption).
Reuses oct26/oct28 hourback feed modules by import; edits none of them.
"""
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oct28_hourback_feed as D11  # noqa: E402  (pulls in oct26_hourback_feed + its patches)

D = D11.D
C, K, specs, chip = D.C, D.K, D.specs, D.chip
HB, W, H = D.HB, D.W, D.H
D12 = "studio-nov01/hourback/hb-day12-potluck"
specs.POSTS[D12] = dict(
    brand=HB, fmt="series",
    cover=dict(lay="pills", f="orng", kicker="ai, for real · day 12", text="Potluck tomorrow. / *3 diets?*", obj="chat",
               at="bl", save="new one<br>every Mon · Wed · Fri"),
    slides=[dict(f="yel", text="Fits all 3 diets. / *It wrote:*",
                 items=["Black bean & corn salad", "Coconut chickpea curry over rice", "Roasted potatoes and veggies"])])
SAVE3 = "real reply, shortened<br>cooking times, costs and its tip on checking labels are in the caption"


def dish(x, y, w=430, rot=-6):
    """One drawn object for the Day 12 cover: a covered casserole dish with three diet tags."""
    ink = "#2A1D47"
    tags = ""
    for k, (tx, lab, tw) in enumerate(((50, "vegan", 92), (152, "no nuts", 108), (286, "gluten-free", 150))):
        tags += (f'<g transform="rotate({-8 + 8 * k} {tx} 300)"><path d="M{tx} 262 V286" stroke="{ink}" stroke-width="3"/>'
                 f'<rect x="{tx - tw // 2}" y="286" width="{tw}" height="40" rx="8" fill="#FFF5EA" stroke="{ink}" stroke-width="4"/>'
                 f'<text x="{tx}" y="314" text-anchor="middle" font-family="Caveat Brush" font-size="30" fill="{ink}">{lab}</text></g>')
    svg = (f'<svg width="{w}" height="{w}" viewBox="0 0 360 360">'
           f'<ellipse cx="180" cy="270" rx="165" ry="18" fill="rgba(42,29,71,.15)"/>'
           f'<path d="M30 170 H330 L312 258 Q180 282 48 258 Z" fill="#FF8A3D" stroke="{ink}" stroke-width="6" stroke-linejoin="round"/>'
           f'<rect x="8" y="170" width="44" height="22" rx="10" fill="#FF8A3D" stroke="{ink}" stroke-width="6"/>'
           f'<rect x="308" y="170" width="44" height="22" rx="10" fill="#FF8A3D" stroke="{ink}" stroke-width="6"/>'
           f'<path d="M36 172 Q180 40 324 172 Z" fill="#C9CAF5" stroke="{ink}" stroke-width="6" stroke-linejoin="round"/>'
           f'<circle cx="180" cy="92" r="18" fill="#FFC94D" stroke="{ink}" stroke-width="6"/>'
           f'<path d="M110 70 q-10 -20 0 -40 M150 50 q-10 -20 0 -40" stroke="{ink}" stroke-width="5" fill="none" stroke-linecap="round" opacity=".5"/>'
           f'{tags}</svg>')
    return f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);z-index:3">{svg}</div>'


PROMPT = (f"I'm bringing a dish to a {chip('potluck')} tomorrow. One guest is {chip('vegan')}, one {chip(chr(99) + 'an' + chr(39) + 't eat nuts')}, "
          f"and one is {chip('gluten-free')}. I have about {chip('30 minutes')} to cook and {chip('$20')}. "
          f"Give me 3 dishes that work for all of them, one line each.")


def slide2():
    f = K.FIELDS[HB]["indi"]
    ink = f["ink"]
    body = C.head(HB, f, "In ChatGPT, Claude or Gemini,", 110, 90, 64)
    body += C.head(HB, f, "type this / *about your guests:*", 200, 330, 160)
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


def build(r):
    spec = specs.POSTS[D12]
    d = C.REPO / "media" / D12
    d.mkdir(parents=True, exist_ok=True)
    c = spec["cover"]
    _o = K.obj
    C.K.obj = lambda name, *a, **k: dish(20, 860) if name == "chat" else _o(name, *a, **k)
    try:
        cov = C.lay_pills(HB, c)
    finally:
        C.K.obj = _o
    return [r.shot(C.page(HB, c["f"], cov, W, H), W, H, d / "01.jpg"),
            r.shot(slide2(), W, H, d / "02.jpg"),
            r.shot(C.page(HB, "yel", C.inner(HB, spec["slides"][0], 2, 3) + K.save_line(SAVE3, 70, 1090, 760, 46, -3, HB), W, H),
                   W, H, d / "03.jpg")]


if __name__ == "__main__":
    r = C.R()
    try:
        print(build(r))
    finally:
        r.close()

#!/usr/bin/env python3
"""Hourback series 'AI, for real · Day 14' (Mon Nov 9 2026, 17:45), built Nov 4 2026 by the Hourback maker.

    python3 studio/editorial/nov04_hourback_feed.py   -> media/studio-nov04/hourback/hb-day14-missed-30th/0N.jpg

2 slides, the SAME layout as Day 13 (studio/editorial/nov03_hourback_feed.py, copied): slide 1 = Look B pills cover,
'ai, for real · day 14' kicker, one drawn object bottom-left (a phone with a '30' balloon and a 'zzz'), 'new one every
Mon · Wed · Fri'. Slide 2 = the indigo white-card slide carrying Claude's REAL text message, word for word (its
'(55 words)' after-note is left off the card and discussed in the caption: the text is really 48 words).
Real run: studio/editorial/hb-nov04-run-missed.txt (claude -p, fresh isolated session, Nov 4 2026).
Reuses the oct26/oct28/nov01 hourback feed modules by import; edits none of them.
"""
import html as _h
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oct28_hourback_feed as D11  # noqa: E402

D = D11.D
C, K, specs = D.C, D.K, D.specs
HB, W, H = D.HB, D.W, D.H
D14 = "studio-nov04/hourback/hb-day14-missed-30th"
specs.POSTS[D14] = dict(
    brand=HB, fmt="series",
    cover=dict(lay="pills", f="orng", kicker="ai, for real · day 14", text="Slept through their 30th. / *Now what?*",
               obj="chat", at="bl", save="new one<br>every Mon · Wed · Fri"),
    slides=[])


def reply():
    t = (C.REPO / "studio/editorial/hb-nov04-run-missed.txt").read_text()
    return t.split("===== REPLY (verbatim) =====\n", 1)[1].strip()


REPLY = reply()
TEXT = REPLY.split("\n\n")[0].strip()
AFTER = REPLY.split("\n\n")[1].strip()
assert TEXT.startswith("Hey Jordan, I'm really sorry I missed your 30th") and AFTER == "*(55 words)*", (TEXT, AFTER)
assert len(TEXT.split()) == 48
# CD gate Nov 4: show what we told it, so the migraine visibly comes from our prompt, not from the AI
TOLD = "missed Jordan's 30th birthday dinner on Saturday · had a migraine, fell asleep · didn't text until Sunday morning"


def phone(x, y, w=400, rot=-5):
    """One drawn object for the Day 14 cover: a phone with a '30' balloon on screen and a sleepy 'zzz'."""
    ink = "#2A1D47"
    svg = (f'<svg width="{w}" height="{w}" viewBox="0 0 360 360">'
           f'<ellipse cx="170" cy="334" rx="120" ry="14" fill="rgba(42,29,71,.15)"/>'
           f'<rect x="80" y="20" width="180" height="310" rx="30" fill="#2A1D47" stroke="{ink}" stroke-width="6"/>'
           f'<rect x="94" y="44" width="152" height="262" rx="16" fill="#C9CAF5"/>'
           f'<ellipse cx="170" cy="130" rx="52" ry="62" fill="#FF8A3D" stroke="{ink}" stroke-width="5"/>'
           f'<path d="M170 192 l-8 12 h16z" fill="#FF8A3D" stroke="{ink}" stroke-width="4"/>'
           f'<path d="M170 204 C 160 230, 184 250, 170 280" stroke="{ink}" stroke-width="4" fill="none"/>'
           f'<text x="170" y="150" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="56" fill="#FFF8EF">30</text>'
           f'<text x="280" y="90" font-family="Caveat Brush" font-size="58" fill="#5E54C9" transform="rotate(-10 280 90)">z</text>'
           f'<text x="300" y="50" font-family="Caveat Brush" font-size="44" fill="#5E54C9" transform="rotate(-10 300 50)">z</text>'
           f'<text x="318" y="20" font-family="Caveat Brush" font-size="32" fill="#5E54C9" transform="rotate(-10 318 20)">z</text></svg>')
    return f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);z-index:3">{svg}</div>'


def slide2():
    f = K.FIELDS[HB]["indi"]
    ink = f["ink"]
    body = C.head(HB, f, "Tell AI what happened and what you'll do.", 80, 80, 52)
    body += C.head(HB, f, "It wrote / *this text:*", 150, 220, 112)
    body += (f'<div style="position:absolute;left:70px;right:70px;top:400px;background:#FFFFFF;border:4px solid {ink};border-radius:32px;'
             f'box-shadow:0 14px 0 {ink};padding:26px 40px 34px;z-index:3;color:{ink}">'
             f'<div style="font:700 26px Inter;letter-spacing:.1em;text-transform:uppercase;opacity:.65;margin-bottom:6px">Text to</div>'
             f'<div style="font:700 34px/1.25 Inter;margin-bottom:22px;padding-bottom:14px;border-bottom:3px solid #E4E1F6">Jordan</div>'
             f'<div style="background:#5E54C9;color:#FFFFFF;border-radius:30px 30px 8px 30px;padding:26px 32px;font:500 40px/1.36 Inter;margin-left:40px">{_h.escape(TEXT)}</div>'
             f'</div>')
    body += (f'<div style="position:absolute;left:70px;right:70px;top:1068px;background:#FFE7A0;border:3px solid {ink};border-radius:22px;'
             f'padding:16px 30px 18px;z-index:3;color:{ink};transform:rotate(-0.6deg)">'
             f'<div style="font:400 34px/1 \'Caveat Brush\';color:#D4532A;margin-bottom:6px">what we told it (made up for this post):</div>'
             f'<div style="font:500 30px/1.3 Inter">{_h.escape(TOLD)}</div></div>')
    body += K.save_line("Claude's real text, word for word · names and story made up for this post", 40, 1262, 1000, 36, -2, HB)
    body += f'<div style="position:absolute;right:60px;top:40px;font:600 30px/1 Fraunces;color:{ink};opacity:.55;z-index:5">2/2</div>'
    return C.page(HB, "indi", body, W, H)


def build(r):
    spec = specs.POSTS[D14]
    d = C.REPO / "media" / D14
    d.mkdir(parents=True, exist_ok=True)
    c = spec["cover"]
    _o = K.obj
    C.K.obj = lambda name, *a, **k: phone(30, 860) if name == "chat" else _o(name, *a, **k)
    try:
        cov = C.lay_pills(HB, c)
    finally:
        C.K.obj = _o
    return [r.shot(C.page(HB, c["f"], cov, W, H), W, H, d / "01.jpg"),
            r.shot(slide2(), W, H, d / "02.jpg")]


if __name__ == "__main__":
    r = C.R()
    try:
        print(build(r))
    finally:
        r.close()

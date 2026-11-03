#!/usr/bin/env python3
"""Hourback series 'AI, for real · Day 13' (Fri Nov 6 2026, 17:45), built Nov 3 2026 by the Hourback maker.

    python3 studio/editorial/nov03_hourback_feed.py   -> media/studio-nov03/hourback/hb-day13-landlord-email/0N.jpg

2 slides (Performance desk Nov 3: feed reach 0-1, keep the promised episode, minimal hours). Slide 1 = the SAME cover
layout as Day 12 (nov01_hourback_feed.py: Look B pills cover, 'ai, for real · day N' kicker, one drawn object bottom-left,
'new one every Mon · Wed · Fri'), with a drawn thermostat at 16°C. Slide 2 = the indigo prompt-card slide of the series,
but carrying Claude's REAL email (word for word, from the subject line to the sign-off; its after-note is in the caption).
Real run: studio/editorial/hb-nov03-run-landlord2.txt (claude -p, fresh isolated session, Nov 3 2026; gate fix: dates
that fit the Fri Nov 6 post. The first isolated run, hb-nov03-run-landlord.txt, is kept as the record but no longer used).
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
D13 = "studio-nov03/hourback/hb-day13-landlord-email"
specs.POSTS[D13] = dict(
    brand=HB, fmt="series",
    cover=dict(lay="pills", f="orng", kicker="ai, for real · day 13", text="16°C inside. / *Landlord's not fixing it?*",
               obj="chat", at="bl", save="new one<br>every Mon · Wed · Fri"),
    slides=[])


def reply():
    t = (C.REPO / "studio/editorial/hb-nov03-run-landlord2.txt").read_text()
    return t.split("===== REPLY (verbatim) =====\n", 1)[1].split("\n---\n", 1)[0].strip()


EMAIL = reply()
SUBJECT = EMAIL.splitlines()[0].strip("*").replace("Subject: ", "")
BODY = [p.strip() for p in EMAIL.split("\n\n")[1:]]
assert SUBJECT.startswith("Heat Not Working in Unit 4B") and BODY[0] == "Hi Dan,", (SUBJECT, BODY[:1])


def thermostat(x, y, w=400, rot=-5):
    """One drawn object for the Day 13 cover: a wall thermostat reading 16°C with a frost mark."""
    ink = "#2A1D47"
    svg = (f'<svg width="{w}" height="{w}" viewBox="0 0 360 360">'
           f'<ellipse cx="180" cy="318" rx="150" ry="16" fill="rgba(42,29,71,.15)"/>'
           f'<rect x="40" y="60" width="280" height="240" rx="40" fill="#FFF8EF" stroke="{ink}" stroke-width="6"/>'
           f'<rect x="76" y="96" width="208" height="112" rx="18" fill="#C9CAF5" stroke="{ink}" stroke-width="5"/>'
           f'<text x="180" y="180" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="76" fill="{ink}">16°C</text>'
           f'<circle cx="130" cy="252" r="20" fill="#FF8A3D" stroke="{ink}" stroke-width="5"/>'
           f'<circle cx="230" cy="252" r="20" fill="#5E54C9" stroke="{ink}" stroke-width="5"/>'
           f'<path d="M180 232 V272" stroke="{ink}" stroke-width="5" stroke-linecap="round"/>'
           f'<g transform="translate(318 54)" stroke="#5E54C9" stroke-width="7" stroke-linecap="round">'
           f'<path d="M0 -30 V30 M-26 -15 L26 15 M-26 15 L26 -15"/></g></svg>')
    return f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);z-index:3">{svg}</div>'


def slide2():
    f = K.FIELDS[HB]["indi"]
    ink = f["ink"]
    body = C.head(HB, f, "Tell AI what's wrong and what you need.", 80, 80, 52)
    body += C.head(HB, f, "It wrote / *this email:*", 150, 220, 112)
    paras = "".join(f'<div style="margin-top:{0 if k == 0 else 16}px">{_h.escape(p).replace(chr(10), "<br>")}</div>'
                    for k, p in enumerate(BODY))
    body += (f'<div style="position:absolute;left:70px;right:70px;top:390px;background:#FFFFFF;border:4px solid {ink};border-radius:32px;'
             f'box-shadow:0 14px 0 {ink};padding:26px 40px 30px;z-index:3;color:{ink}">'
             f'<div style="font:700 26px Inter;letter-spacing:.1em;text-transform:uppercase;opacity:.65;margin-bottom:6px">Subject</div>'
             f'<div style="font:700 34px/1.25 Inter;margin-bottom:16px;padding-bottom:14px;border-bottom:3px solid #E4E1F6">{_h.escape(SUBJECT)}</div>'
             f'<div style="font:500 30px/1.32 Inter">{paras}</div></div>')
    body += K.save_line("Claude's real email, word for word · names and dates made up for this post", 40, 1262, 1000, 38, -2, HB)
    body += f'<div style="position:absolute;right:60px;top:40px;font:600 30px/1 Fraunces;color:{ink};opacity:.55;z-index:5">2/2</div>'
    return C.page(HB, "indi", body, W, H)


def build(r):
    spec = specs.POSTS[D13]
    d = C.REPO / "media" / D13
    d.mkdir(parents=True, exist_ok=True)
    c = spec["cover"]
    _o = K.obj
    C.K.obj = lambda name, *a, **k: thermostat(30, 860) if name == "chat" else _o(name, *a, **k)
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

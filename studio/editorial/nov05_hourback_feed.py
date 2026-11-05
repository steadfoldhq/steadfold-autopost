#!/usr/bin/env python3
"""Hourback series 'AI, for real · Day 15' (Wed Nov 11 2026, 17:45), built Nov 5 2026 by the Hourback maker.

    python3 studio/editorial/nov05_hourback_feed.py   -> media/studio-nov05/hourback/hb-day15-roommate-chores/0N.jpg

2 slides, the SAME layout as Day 14 (studio/editorial/nov04_hourback_feed.py, copied): slide 1 = Look B pills cover,
'ai, for real · day 15' kicker, one drawn object bottom-left (a sink with a dish pile and 4 mugs), 'new one every
Mon · Wed · Fri'. Slide 2 = the indigo white-card slide carrying Claude's REAL group-chat text, word for word (its
**bold** markdown shown as bold, emoji kept).
Real run: studio/editorial/hb-nov05-run-chores.txt (claude -p, fresh isolated session, Nov 5 2026).
Reuses the oct26/oct28/nov01 hourback feed modules by import; edits none of them.
"""
import html as _h
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oct28_hourback_feed as D11  # noqa: E402

D = D11.D
C, K, specs = D.C, D.K, D.specs
HB, W, H = D.HB, D.W, D.H
D14 = "studio-nov05/hourback/hb-day15-roommate-chores"
specs.POSTS[D14] = dict(
    brand=HB, fmt="series",
    cover=dict(lay="pills", f="orng", kicker="ai, for real · day 15", text="4 roommates. / *Whose turn is it?*",
               obj="chat", at="bl", save="new one<br>every Mon · Wed · Fri"),
    slides=[])


def reply():
    t = (C.REPO / "studio/editorial/hb-nov05-run-chores.txt").read_text()
    return t.split("===== REPLY (verbatim) =====\n", 1)[1].strip()


REPLY = reply()
assert REPLY.startswith("Hey all! 🧽 Quick idea") and REPLY.endswith("Thoughts? 😊"), REPLY
WORDS = len(re.sub(r"\*\*", "", REPLY).split())
TOLD = "Sam, Ana, Theo and me · dishes every night, trash Tue night, counters + bathroom once a week · Theo works weekend nights"


def text_html():
    """The reply, word for word: paragraphs kept, **bold** shown as bold."""
    out = []
    for para in REPLY.split("\n\n"):
        lines = [re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", _h.escape(ln)) for ln in para.split("\n")]
        out.append("".join(f'<span style="display:block;margin-top:6px">{ln}</span>' if i else ln for i, ln in enumerate(lines)))
    return '<div style="height:16px"></div>'.join(out)


def sink(x, y, w=420, rot=-4):
    """One drawn object for the Day 15 cover: a sink with a dish pile and 4 mugs."""
    ink = "#2A1D47"
    mugs = "".join(f'<g transform="translate({60 + i * 62} {150 - (i % 2) * 8})"><path d="M0 0 h44 l-4 52 h-36z" fill="{c}" stroke="{ink}" stroke-width="5" stroke-linejoin="round"/>'
                   f'<path d="M44 12 q22 2 18 20 q-4 14 -20 12" stroke="{ink}" stroke-width="5" fill="none"/></g>'
                   for i, c in enumerate(["#FF8A3D", "#FFC94D", "#5E54C9", "#FFD4BD"]))
    plates = "".join(f'<ellipse cx="{230 + (i % 2) * 8}" cy="{196 - i * 18}" rx="78" ry="16" fill="#FFFFFF" stroke="{ink}" stroke-width="5"/>' for i in range(5))
    svg = (f'<svg width="{w}" height="{w}" viewBox="0 0 380 380">'
           f'<ellipse cx="190" cy="352" rx="170" ry="14" fill="rgba(42,29,71,.15)"/>'
           f'<path d="M330 210 V70 H270 V96" stroke="{ink}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
           f'<path d="M270 110 v14 M262 140 v10 M278 150 v10" stroke="#5E54C9" stroke-width="5" stroke-linecap="round"/>'
           f'{plates}{mugs}'
           f'<path d="M20 210 H360 L330 340 Q190 356 50 340Z" fill="#C9CAF5" stroke="{ink}" stroke-width="6" stroke-linejoin="round"/>'
           f'<path d="M20 210 H360" stroke="{ink}" stroke-width="8" stroke-linecap="round"/>'
           '</svg>')
    return f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);z-index:3">{svg}</div>'


def slide2():
    f = K.FIELDS[HB]["indi"]
    ink = f["ink"]
    body = C.head(HB, f, "Tell AI the chores and who's busy when.", 80, 80, 52)
    body += C.head(HB, f, "It wrote / *this text:*", 150, 220, 112)
    body += (f'<div style="position:absolute;left:70px;right:70px;top:400px;background:#FFFFFF;border:4px solid {ink};border-radius:32px;'
             f'box-shadow:0 14px 0 {ink};padding:26px 40px 34px;z-index:3;color:{ink}">'
             f'<div style="font:700 26px Inter;letter-spacing:.1em;text-transform:uppercase;opacity:.65;margin-bottom:6px">Text to</div>'
             f'<div style="font:700 34px/1.25 Inter;margin-bottom:22px;padding-bottom:14px;border-bottom:3px solid #E4E1F6">House group chat</div>'
             f'<div style="background:#5E54C9;color:#FFFFFF;border-radius:30px 30px 8px 30px;padding:22px 30px;font:500 31px/1.3 Inter,\'Noto Color Emoji\';margin-left:30px">{text_html()}</div>'
             f'</div>')
    body += (f'<div style="position:absolute;left:70px;right:70px;top:1118px;background:#FFE7A0;border:3px solid {ink};border-radius:22px;'
             f'padding:12px 30px 14px;z-index:3;color:{ink};transform:rotate(-0.6deg)">'
             f'<div style="font:400 34px/1 \'Caveat Brush\';color:#D4532A;margin-bottom:6px">what we told it (made up for this post):</div>'
             f'<div style="font:500 28px/1.28 Inter">{_h.escape(TOLD)}</div></div>')
    body += K.save_line("Claude's real text, word for word · roommates made up for this post", 40, 1292, 1000, 36, -2, HB)
    body += f'<div style="position:absolute;right:60px;top:40px;font:600 30px/1 Fraunces;color:{ink};opacity:.55;z-index:5">2/2</div>'
    return C.page(HB, "indi", body, W, H)


def build(r):
    spec = specs.POSTS[D14]
    d = C.REPO / "media" / D14
    d.mkdir(parents=True, exist_ok=True)
    c = spec["cover"]
    _o = K.obj
    C.K.obj = lambda name, *a, **k: sink(20, 840) if name == "chat" else _o(name, *a, **k)
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

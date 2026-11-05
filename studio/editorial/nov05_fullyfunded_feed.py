#!/usr/bin/env python3
"""Nov 5 studio build: Rich Habits, Decoded No. 8 (ff-richhabits-08), Wed Nov 11 17:00 (promised in No. 7's caption).
Copied from nov04_fullyfunded_feed.py (No. 7), same layout and the same in-process pill colours. Same series layout as No. 6 (pills cover on the coral field + series badge + handwritten series line + round stamp + a drawn card
bottom-right; slide 2 from covers.inner() on the lite field + a drawn card), imported from nov01_fullyfunded_feed.py (not edited).
Habit No. 8: before holiday shopping, write every name with a dollar amount that adds up to one total (a cap), and stop at it.
FCAC 'Making a budget' (modified 2025-08-21): a budget matters when planning a major purchase or life event; make saving for those
goals part of your budget. The $300 cap and the names are made up for this post (the habit's own rule of thumb, not a study).

    python3 studio/editorial/nov05_fullyfunded_feed.py
Writes media/studio-nov05/fullyfunded/ff-richhabits-08/0N.jpg.
"""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/editorial"))
import nov01_fullyfunded_feed as F  # noqa: E402  (No. 5/6: series layout via oct28/oct25)
import edkit as K  # noqa: E402
# CD gate (Nov 4): the lavender pill (p1 #C9D3F7 / #CBD4F7) reads as Hourback periwinkle. In-process only (kit not edited):
# white pill on the coral field, soft coral #FFB08F on the lite field.
K.FIELDS["fullyfunded"]["coral"] = dict(K.FIELDS["fullyfunded"]["coral"], p1="#FFFFFF")
K.FIELDS["fullyfunded"]["lite"] = dict(K.FIELDS["fullyfunded"]["lite"], p1="#FFB08F")

Q, P, C = F.Q, F.P, F.C
FF, W, H, COB, CORAL, INK = P.FF, P.W, P.H, P.COB, P.CORAL, F.INK
GREEN = "#1F8A5B"
OUT = REPO / "media/studio-nov05/fullyfunded/ff-richhabits-08"

CAP = 300
LIST = (("MOM", 70), ("DAD", 70), ("SISTER", 60), ("BEST FRIEND", 60), ("OFFICE SWAP", 40))
assert sum(v for _, v in LIST) == CAP
SPENT = 70 + 70 + 60 + 40          # slide 2: 4 of 5 bought
assert SPENT == 240

COVER = dict(lay="pills", f="coral", kicker="rich habits, decoded · no. 8", text="Holiday gifts? / *Set a $300 cap / first.*",
             obj="ok", at="br", save=P.SAVE)
S2 = dict(f="lite", text="Give every name / a dollar amount. / *Stop at $300.*", sub="check the list before you pay")


def gift_list(x0=540, y0=845, w=470, h=440):
    """Drawn gift list card: GIFT LIST header, 5 names with dollar amounts, a TOTAL CAP $300 line."""
    rows = "".join(
        f'<text x="40" y="{132 + 46 * k}" font-family="DejaVu Sans Mono" font-weight="700" font-size="28" fill="{INK}">{n}</text>'
        f'<text x="{w - 40}" y="{132 + 46 * k}" text-anchor="end" font-family="Inter Display, Inter" font-weight="800" font-size="34" '
        f'fill="{COB}">${v}</text>' for k, (n, v) in enumerate(LIST))
    return "".join([
        f'<svg style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="0 0 {w} {h}">',
        f'<rect x="14" y="34" width="{w - 12}" height="{h - 30}" rx="22" fill="{INK}"/>',
        f'<rect x="6" y="20" width="{w - 12}" height="{h - 30}" rx="22" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>',
        f'<rect x="6" y="20" width="{w - 12}" height="64" rx="22" fill="{COB}" stroke="{INK}" stroke-width="5"/>',
        f'<rect x="9" y="58" width="{w - 18}" height="26" fill="{COB}"/>',
        f'<text x="{w / 2}" y="64" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="#FFFFFF">HOLIDAY GIFT LIST</text>',
        rows,
        f'<line x1="40" y1="{132 + 46 * 5 - 22}" x2="{w - 40}" y2="{132 + 46 * 5 - 22}" stroke="{INK}" stroke-width="4"/>',
        f'<g transform="rotate(-4 {w / 2} {h - 50})"><rect x="40" y="{h - 98}" width="{w - 80}" height="88" rx="16" fill="#FFFFFF" '
        f'stroke="{CORAL}" stroke-width="8"/>'
        f'<text x="64" y="{h - 42}" font-family="DejaVu Sans Mono" font-weight="700" font-size="28" fill="{CORAL}">TOTAL CAP</text>'
        f'<text x="{w - 64}" y="{h - 34}" text-anchor="end" font-family="Inter Display, Inter" font-weight="800" font-size="60" fill="{CORAL}">${CAP}</text></g>',
        "</svg>"])


def tally(x, y, w=560):
    """Drawn tally card for slide 2: SPENT $240 OF $300, a progress bar at 80%, '$60 left · 1 gift to go'."""
    h = 300
    bw = w - 80
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="0 0 {w} {h}">'
            f'<rect x="12" y="14" width="{w - 8}" height="{h - 10}" rx="34" fill="{INK}"/>'
            f'<rect x="4" y="4" width="{w - 8}" height="{h - 10}" rx="34" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
            f'<text x="40" y="76" font-family="DejaVu Sans Mono" font-weight="700" font-size="26" fill="{INK}">GIFTS BOUGHT · 4 OF 5</text>'
            f'<text x="40" y="160" font-family="Inter Display, Inter" font-weight="800" font-size="62" fill="{INK}">${SPENT} of ${CAP}</text>'
            f'<rect x="40" y="190" width="{bw}" height="34" rx="17" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/>'
            f'<rect x="44" y="194" width="{(bw - 8) * SPENT / CAP:.0f}" height="26" rx="13" fill="{COB}"/>'
            f'<text x="40" y="264" font-family="DejaVu Sans Mono" font-weight="700" font-size="25" fill="{CORAL}">${CAP - SPENT} LEFT · 1 GIFT TO GO</text>'
            '</svg>')


def cover():
    body = C.lay_pills(FF, COVER)
    body = P.lift_save(re.sub(r'<img class="obj"[^>]*>', "", body, count=1))   # drawn gift list replaces the halftone object
    body = body.replace("width:620px;font-size:66px", "width:470px;font-size:62px", 1)
    return C.page(FF, "coral", body + gift_list(), W, H)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = C.R()
    try:
        files = [r.shot(cover(), W, H, OUT / "01.jpg"),
                 r.shot(C.page(FF, S2["f"], C.inner(FF, S2, 1, 2) + tally(260, 1000, 560), W, H), W, H, OUT / "02.jpg")]
    finally:
        r.close()
    print(files)


if __name__ == "__main__":
    main()

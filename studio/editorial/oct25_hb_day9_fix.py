#!/usr/bin/env python3
"""Fix of queued hb-day9-kind-firm-no (gate, Oct 25): slide 2 named no app ("Ask AI:"), and the Oct 24 reply had no transcript.
New real run: studio/editorial/hb-oct25-run-kind-firm-no.txt (fresh Claude session, Oct 25 2026). Same code path as the
queued build (oct24_feed.py ed_inner + its reply-slide layout); slide 1 copied unchanged. Writes NEW files only:

    python3 studio/editorial/oct25_hb_day9_fix.py  -> media/studio-oct25/hourback/hb-day9-kind-firm-no-r2/01-03.jpg
"""
import shutil
import sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oct24_feed as O  # noqa: E402  (registers its posts; builds nothing on import)

C, K, HB, W, H = O.C, O.K, O.HB, O.W, O.H
REPO = O.REPO
SRC = REPO / "media/hb-day9-kind-firm-no"
OUT = REPO / "media/studio-oct25/hourback/hb-day9-kind-firm-no-r2"

# Claude's second version (no $200, which slides 1-2 never introduce), quoted exactly from the transcript (it also wrote a second version; see the caption)
REPLY = "Hey, I'm going to pass on this one. I hope it works out, and I'm here if you want to talk it through."

S2 = dict(O.HB9_S2, text="Ask Claude: / “Help me say no / to lending $500.” / Add: *kind, firm,* / *no excuses.*")


def reply_slide():
    f = K.FIELDS[HB]["yel"]
    ink = f["ink"]
    body = C.head(HB, f, "It *wrote:*", 120, 220, 190)
    body += (f'<div style="position:absolute;left:90px;right:90px;top:390px;z-index:2">'
             f'<div style="font:600 30px/1.2 Inter;letter-spacing:.08em;text-transform:uppercase;color:{ink};opacity:.75;margin:0 0 18px 8px">'
             f'Claude\'s reply, word for word</div>'
             f'<div style="background:#FFFFFF;border:3px solid {ink};border-radius:44px 44px 44px 10px;box-shadow:0 14px 0 {ink};'
             f'padding:40px 46px;font:500 48px/1.26 Inter;color:{ink}">{REPLY.replace("pass on this one", "<b>pass on this one</b>")}</div></div>')
    body += K.save_line("1 of 2 replies it wrote ·<br>situation made up for this post", 60, 790, 960, 56, -2, HB)
    body += f'<div style="position:absolute;right:60px;top:40px;font:600 30px/1 Fraunces;color:{ink};opacity:.55;z-index:5">3/3</div>'
    body += K.stamp(HB, W - 230, H - 230, 170, -12)
    return C.page(HB, "yel", body, W, H)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    if "--all" in sys.argv:
        shutil.copyfile(SRC / "01.jpg", OUT / "01.jpg")
    r = C.R()
    try:
        if "--all" in sys.argv:
            r.shot(O.ed_inner(HB, S2, 1, 3)(), W, H, OUT / "02.jpg")
        r.shot(reply_slide(), W, H, OUT / "03.jpg")
    finally:
        r.close()
    print(sorted(str(p.relative_to(REPO / "media")) for p in OUT.glob("*.jpg")))

#!/usr/bin/env python3
"""Hourback series feed post 'AI, for real · Day 9' (Wed Oct 28, 5:45 pm), built Oct 25 2026.

Same layout as Day 8 (series_oct26.py hb-day8-ask-me-first): pills cover with the series kicker, an indigo line slide,
a white list card. Reuses specs.py + covers.py by import; edits neither.
Real run: studio/editorial/hb-oct25-run-day9.txt (Claude, Oct 25 2026). Recipe made up for this post.

    python3 studio/editorial/oct25_hb_day9.py   -> media/studio-oct25/hourback/hb-day9-pancakes-for-6/0N.jpg
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import glob  # noqa: E402
_g = glob.glob
# this machine's Playwright Chromium lives in chrome-linux64/ (covers.py looks in chrome-linux/); shim without editing covers.py
glob.glob = lambda p, *a, **k: _g(p, *a, **k) or _g(p.replace("chrome-linux/", "chrome-linux64/"), *a, **k)
import specs  # noqa: E402
import covers as C  # noqa: E402
glob.glob = _g
# retired props (pointing hand, OK hand; brand addendum Oct 22) never render on Hourback series slides
_obj = C.K.obj
C.K.obj = lambda name, *a, **k: "" if name in ("point", "ok") else _obj(name, *a, **k)

PID = "studio-oct25/hourback/hb-day9-pancakes-for-6"
specs.POSTS[PID] = dict(
    brand="hourback", fmt="series",
    cover=dict(lay="pills", f="orng", kicker="ai, for real · day 9", text="Recipe for 4. / *Six are* / *coming?*", obj="chat",
               at="bl", save="mon · wed · fri"),
    slides=[dict(f="indi", text="Rewrite this / recipe for / *6 people.*", sub="type this under any recipe"),
            dict(f="yel", text="Pancakes for 6. / *It wrote:*",
                 items=["2¼ cups flour", "1¾ cups + 2 tbsp milk", "1½ eggs<br>(or 1 egg plus 1 yolk)"],
                 sub="real reply, shortened", save="we checked: all 7 correct")])

if __name__ == "__main__":
    (C.REPO / "media" / PID).parent.mkdir(parents=True, exist_ok=True)
    C.build_feed([PID])
    print(C.alt_text(PID))

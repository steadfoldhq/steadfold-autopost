#!/usr/bin/env python3
"""Oct 23 (Social studio): clarity-gate rewrites of single slides in queued teach.py / formats.py carousels.
A fresh stranger read (on-screen text only) marked these lines CONFUSING. The post is re-rendered into a scratch root with
the edited spec (pointing hand stays retired), and ONLY the edited slides are copied over the queued files; every other
slide stays exactly as queued. Before/after sheet per post in the scratch root.

    python3 studio/editorial/patch_slides_oct23.py [--apply]
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from PIL import Image  # noqa: E402
import edkit as K  # noqa: E402
_obj = K.obj
K.obj = lambda name, *a, **k: "" if name == "point" else _obj(name, *a, **k)
import covers as C  # noqa: E402,F401
import teach as T  # noqa: E402
from specs_teach import POSTS  # noqa: E402  (import specs_teach first)
import formats as F  # noqa: E402
import v5_formats as V  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
SCR = Path("/tmp/claude-0/patchslides")


def teach_edit(pid, n, **kw):  # slide n (1-based, cover = 1) of a specs_teach post
    POSTS[pid]["slides"][n - 2].update(kw)


# hb-1024-share-eta (Oct 24 1 pm): "from Prediction Machines" didn't say it's a book; the electricity slide never said what it means for you
teach_edit("hb-1024-share-eta", 3, sub="from the book Prediction Machines")
teach_edit("hb-1024-share-eta", 7, text="Factories took / *decades* to redesign / around electricity. / Same with AI: the wins / come when *work changes.*")
# ff-1025-tfsa-room (Oct 25 noon): "TFSA room" never explained; "(Jan 1)"; "at 10%" unlabelled
teach_edit("ff-1025-tfsa-room", 2, text="Your *room* adds up", cap="Room = what you can put in · CRA limits")
teach_edit("ff-1025-tfsa-room", 6, text="Fill it: *$7,000* / a year from 30, / at 10% a year:")
st = POSTS["ff-1025-tfsa-room"]["slides"][6]
st["items"] = ["Log in to CRA My Account" if "Log in" in x else ("Find your room on Jan 1" if "Find TFSA" in x else x)
               for x in st["items"]]
# hb-1024-climb-5-levels (Oct 24 5:45 pm): whose levels; what AGI means
cl = V.FORMATS["hb-1024-climb-5-levels"]
for lv in [cl.get("cover", {})] + cl.get("levels", cl.get("steps", cl.get("beats", []))):
    if isinstance(lv, dict) and "note" in lv:
        lv["note"] = (lv["note"].replace("Reported by Bloomberg, 2024. Here's what / each level *really* looks like.",
                                         "OpenAI's 5 levels, as Bloomberg / reported in 2024. Here's each one *for real.*")
                      .replace("Not here. This is the level / people mean by *AGI.*",
                               "Not here yet. Most people / call this top level *AGI.*"))
for k in ("note", "sub"):
    if isinstance(cl.get(k), str):
        cl[k] = cl[k].replace("Reported by Bloomberg, 2024. Here's what / each level *really* looks like.",
                              "OpenAI's 5 levels, as Bloomberg / reported in 2024. Here's each one *for real.*")

cl["beats"][0]["text"] = "Chatbot. Reasoner. / *Agent.* / What comes *next?*"
PLAN = {"hb-1024-share-eta": [3, 7], "ff-1025-tfsa-room": [2, 6, 8], "hb-1024-climb-5-levels": [1, 6]}
if "--only" in sys.argv:
    PLAN = {"hb-1024-climb-5-levels": [6]}

if __name__ == "__main__":
    apply = "--apply" in sys.argv
    (SCR / "media").mkdir(parents=True, exist_ok=True)
    T.REPO = SCR
    F.REPO = SCR
    for pid, slides in PLAN.items():
        if pid in V.FORMATS:
            F.build([pid])
        else:
            T.build_feed([pid])
        tw = 360
        S = Image.new("RGB", (tw * 2, int(tw * 1.25) * len(slides)), "white")
        for k, n in enumerate(slides):
            old, new = REPO / "media" / pid / f"{n:02d}.jpg", SCR / "media" / pid / f"{n:02d}.jpg"
            S.paste(Image.open(old).resize((tw, int(tw * 1.25))), (0, k * int(tw * 1.25)))
            S.paste(Image.open(new).resize((tw, int(tw * 1.25))), (tw, k * int(tw * 1.25)))
            if apply:
                Image.open(new).save(old, quality=92, subsampling=0)
        S.save(SCR / f"{pid}-sheet.jpg", quality=80)
        print(pid, "slides", slides, "applied" if apply else "preview", flush=True)

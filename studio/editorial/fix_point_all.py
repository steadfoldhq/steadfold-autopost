#!/usr/bin/env python3
"""Oct 23 (Social studio): re-render queued teach.py / formats.py carousels without the retired pointing hand
(north-star 'Rejected'), into a scratch root, and report per slide how much changed. With --apply, a slide is replaced only
when it changed (the hand was there) and less than --max of the slide differs (anything bigger means the spec drifted
from what is queued: those are left alone). Before/after sheets go to the scratch root for a human look.

    python3 studio/editorial/fix_point_all.py <post ids...> [--apply] [--max 0.10]
"""
import json
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np  # noqa: E402
from PIL import Image  # noqa: E402
import edkit as K  # noqa: E402
_obj = K.obj
K.obj = lambda name, *a, **k: "" if name == "point" else _obj(name, *a, **k)
import covers as C  # noqa: E402
import teach as T  # noqa: E402
from specs_teach import POSTS  # noqa: E402  (import specs_teach first)
import formats as F  # noqa: E402
import v5_formats as V  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
SCR = Path("/tmp/claude-0/pointfix")
args = sys.argv[1:]
apply = "--apply" in args
mx = float(args[args.index("--max") + 1]) if "--max" in args else 0.10
ids = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] != "--max")]
Q = {p["id"]: p for p in json.loads((REPO / "schedule" / "posts.json").read_text())["posts"]}
(SCR / "media").mkdir(parents=True, exist_ok=True)
T.REPO = SCR
F.REPO = SCR

for pid in ids:
    imgs = Q[pid].get("images") or []
    if not imgs or not all(x.startswith(pid + "/") for x in imgs):
        print(pid, "skip: queued images were rebuilt elsewhere", flush=True)
        continue
    if pid in V.FORMATS:
        F.build([pid])
    elif pid in POSTS:
        T.build_feed([pid])
    else:
        print(pid, "skip: not a teach.py/formats.py post", flush=True)
        continue
    pairs = []
    for x in imgs:
        old, new = REPO / "media" / x, SCR / "media" / x
        if not new.exists():
            print(pid, x, "missing in re-render", flush=True)
            continue
        a = np.asarray(Image.open(old).convert("RGB"), dtype=int)
        b = np.asarray(Image.open(new).convert("RGB"), dtype=int)
        frac = (np.abs(a - b).sum(2) > 60).mean()
        verdict = "same" if frac < 0.004 else ("REPLACE" if frac < mx else "DRIFT-keep")
        print(pid, x, f"{frac:.2%}", verdict, flush=True)
        if verdict == "REPLACE":
            pairs.append((old, new))
            if apply:
                Image.open(new).save(old, quality=92, subsampling=0)
    if pairs:
        tw = 360
        S = Image.new("RGB", (tw * 2, int(tw * 1.25) * len(pairs)), "white")
        for k, (o, n) in enumerate(pairs):
            S.paste(Image.open(o).resize((tw, int(tw * 1.25))), (0, k * int(tw * 1.25)))
            S.paste(Image.open(SCR / "media" / o.relative_to(REPO / "media")).resize((tw, int(tw * 1.25))), (tw, k * int(tw * 1.25)))
        (SCR / "sheets").mkdir(exist_ok=True)
        S.save(SCR / "sheets" / f"{pid}.jpg", quality=80)

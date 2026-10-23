#!/usr/bin/env python3
"""Oct 23 (Social studio): re-render queued Story-chain frames without the retired props (pointing hand; piggy bank as a
default prop), into a scratch root. A frame is replaced only when it changed by less than --max of its pixels (the
prop was there and nothing else drifted); bigger differences mean the frame was rebuilt elsewhere, so it stays.

    python3 studio/editorial/fix_story_props.py <chain ids...> [--apply] [--max 0.12]
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
K.obj = lambda name, *a, **k: "" if name in ("point", "piggy") else _obj(name, *a, **k)
import covers as C  # noqa: E402,F401
import teach as T  # noqa: E402
from specs_teach import CHAINS  # noqa: E402,F401

REPO = Path(__file__).resolve().parents[2]
SCR = Path("/tmp/claude-0/storyfix")
args = sys.argv[1:]
apply = "--apply" in args
mx = float(args[args.index("--max") + 1]) if "--max" in args else 0.12
cids = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] != "--max")]
Q = {p["id"]: p for p in json.loads((REPO / "schedule" / "posts.json").read_text())["posts"]}
(SCR / "media" / "stories").mkdir(parents=True, exist_ok=True)
T.REPO = SCR
T.build_story(cids)
pairs = []
for cid in cids:
    for fid, _ in T.chain_frames(cid):
        q = Q.get(fid)
        if not q:
            continue
        rel = q.get("image") or (q.get("images") or [None])[0]
        if rel != f"stories/{fid}.jpg":
            print(fid, "skip: queued image built elsewhere", rel)
            continue
        old, new = REPO / "media" / rel, SCR / "media" / rel
        a = np.asarray(Image.open(old).convert("RGB"), dtype=int)
        b = np.asarray(Image.open(new).convert("RGB").resize(Image.open(old).size), dtype=int)
        frac = (np.abs(a - b).sum(2) > 60).mean()
        v = "same" if frac < 0.004 else ("REPLACE" if frac < mx else "DRIFT-keep")
        print(fid, f"{frac:.2%}", v, flush=True)
        if v == "REPLACE":
            pairs.append((old, new))
            if apply:
                Image.open(new).convert("RGB").resize(Image.open(old).size).save(old, quality=92, subsampling=0)
if pairs:
    S = Image.new("RGB", (300 * len(pairs), 533 * 2), "white")
    for k, (o, n) in enumerate(pairs):
        S.paste(Image.open(o).convert("RGB").resize((300, 533)), (300 * k, 0))
        S.paste(Image.open(n).convert("RGB").resize((300, 533)), (300 * k, 533))
    S.save(SCR / "sheet.jpg", quality=80)

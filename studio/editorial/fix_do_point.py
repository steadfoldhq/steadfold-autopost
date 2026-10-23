#!/usr/bin/env python3
"""Oct 23 (Social studio): re-render ONLY the 'Do this:' slide of queued carousels without the retired pointing hand
(north-star 'Rejected': repetitive pointing-hand graphics). The slide is rebuilt from its own spec with the same renderer;
the script refuses to replace a file when more than 1% of the slide outside the hand's corner differs (the spec drifted
from what is queued), and skips posts whose queued images were rebuilt by another pipeline.

    python3 studio/editorial/fix_do_point.py <post ids...> [--apply]
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
apply = "--apply" in sys.argv
ids = [a for a in sys.argv[1:] if not a.startswith("--")]
Q = {p["id"]: p for p in json.loads((REPO / "schedule" / "posts.json").read_text())["posts"]}
r = C.R()


def one(pid):
    tmp = Path("/tmp/claude-0/fixdo") / pid
    tmp.mkdir(parents=True, exist_ok=True)
    if pid in V.FORMATS:  # interactive formats (formats.py): the Do slide is always the last image
        spec = V.FORMATS[pid]
        n = len(list((REPO / "media" / pid).glob("*.jpg")))
        dst = REPO / "media" / pid / f"{n:02d}.jpg"
        make = lambda: F.do_slide(r, spec, tmp, n, n)  # noqa: E731
    elif pid in POSTS:
        spec = POSTS[pid]
        b, sl = spec["brand"], spec["slides"]
        n = 1 + len(sl)
        i = next(j for j, s in enumerate(sl, 1) if s.get("k") == "do")
        dst = REPO / "media" / pid / f"{i + 1:02d}.jpg"
        make = lambda: r.shot(C.page(b, sl[i - 1]["f"], T.inner(b, sl[i - 1], i, n), T.W, T.H), T.W, T.H, tmp / dst.name)  # noqa: E731
    else:
        print(pid, "skip: not built by teach.py/formats.py", flush=True)
        return
    if f"{pid}/{dst.name}" not in (Q[pid].get("images") or []):
        print(pid, "skip: queued images were rebuilt elsewhere", flush=True)
        return
    new = make()
    a = np.asarray(Image.open(dst).convert("RGB"), dtype=int)
    bb = np.asarray(Image.open(new).convert("RGB"), dtype=int)
    d = np.abs(a - bb).sum(2) > 60
    corner = d[900:1350, 0:460].mean()
    d[900:1350, 0:460] = False
    frac = d.mean()
    ok = frac < 0.01 and corner > 0.02
    print(pid, dst.name, f"outside corner {frac:.3%}", f"corner {corner:.1%}", "REPLACE" if ok else "keep", flush=True)
    if ok and apply:
        Image.open(new).save(dst, quality=92, subsampling=0)


for pid in ids:
    one(pid)
r.close()

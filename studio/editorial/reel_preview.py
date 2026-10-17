#!/usr/bin/env python3
"""Quick look at a Reel before the 9-minute render: frame 0.75 s (the cover) + the middle of every beat, as one strip.

    python3 studio/editorial/reel_preview.py <reel-id> OUT.jpg
"""
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO / "studio" / "pivot"))
sys.path.insert(0, str(REPO / "studio" / "motion"))
from PIL import Image  # noqa: E402


def reel_for(rid):
    from specs_hits import REELS as H
    from boldkit import SAVES
    if rid in H:
        import hits as M
        spec = dict(H[rid], id=rid)
    else:
        import reels as M
        from specs_reels import REELS as R
        spec = dict(R[rid], id=rid)
    spec["scenes"] = [dict(spec["scenes"][0], save=SAVES.get(rid))] + spec["scenes"][1:]
    return M.make(spec)


def main(rid, out):
    from kit import render_frames
    r = reel_for(rid)
    ts = [0.75] + [s["start"] + s["dur"] * 0.7 for s in r.scenes[1:-1]]
    idx = [int(t * 30) for t in ts]
    work = Path("/tmp/reel-preview") / rid
    fdir, _ = render_frames(r, work, dsf=1, workers=2, only=idx)
    ims = []
    for i in idx:
        f = next(fdir.glob(f"{i:05d}.*"))
        ims.append(Image.open(f).convert("RGB").resize((360, 640)))
    sh = Image.new("RGB", (370 * len(ims), 640), "white")
    for k, im in enumerate(ims):
        sh.paste(im, (k * 370, 0))
    sh.save(out, quality=88)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

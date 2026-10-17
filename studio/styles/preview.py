"""Render a few frames of a style and tile them (QA before a full render). Usage: preview.py MODULE t1,t2,..."""
import importlib, sys, math
from pathlib import Path
from PIL import Image, ImageDraw
mod = importlib.import_module(sys.argv[1])
ts = [float(x) for x in sys.argv[2].split(",")]
fr = [int(round(t * 30)) for t in ts]
fdir = Path(mod.build(fr))
ims = []
for t, f in zip(ts, fr):
    im = Image.open(fdir / f"{f:05d}.jpg").resize((270, 480), Image.LANCZOS)
    ImageDraw.Draw(im).text((6, 6), f"{t:.2f}", fill=(255, 0, 0))
    ims.append(im)
cols = min(8, len(ims)); rows = math.ceil(len(ims) / cols)
sh = Image.new("RGB", (cols * 270, rows * 480), "black")
for k, im in enumerate(ims):
    sh.paste(im, ((k % cols) * 270, (k // cols) * 480))
out = fdir.parent / "preview.jpg"; sh.save(out, quality=88); print(out)

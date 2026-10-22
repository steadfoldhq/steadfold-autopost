#!/usr/bin/env python3
"""Repaint the 'tonight: …' hand-off pill on a queued Hourback Story so it points at the Reel that will actually run."""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
R = "/home/claude/steadfold-autopost"
src, dst, text = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(src).convert("RGB"); a = np.asarray(im).astype(int)
band = a[1440:1600]
ink = (abs(band[..., 0] - 0x2A) < 30) & (abs(band[..., 1] - 0x1D) < 30) & (abs(band[..., 2] - 0x47) < 35)
ys, xs = np.nonzero(ink); y0, y1, x0, x1 = ys.min() + 1440, ys.max() + 1440, xs.min(), xs.max()
pill_fill = tuple(int(v) for v in a[y0 + 12, x0 + 40])   # cream inside the border
# cover the old pill with paper texture taken from the empty band below it
h = y1 - y0 + 16
patch = im.crop((0, y1 + 60, 1080, y1 + 60 + h))
im.paste(patch, (0, y0 - 8))
d = ImageDraw.Draw(im)
f = ImageFont.truetype(f"{R}/assets/fonts/DMSerifDisplay-Regular.ttf", 64)
tw = d.textlength(text, font=f); pw = int(tw + 90); ph = y1 - y0 - 8
px = (1080 - pw) // 2; py = y0
d.rounded_rectangle((px + 7, py + 9, px + pw + 7, py + ph + 9), radius=ph // 2, fill="#2A1D47")
d.rounded_rectangle((px, py, px + pw, py + ph), radius=ph // 2, fill=pill_fill, outline="#2A1D47", width=5)
d.text((540, py + ph / 2 - 4), text, font=f, fill="#2A1D47", anchor="mm")
im.save(dst, quality=93)
print(dst, (x0, y0, x1, y1), pill_fill)

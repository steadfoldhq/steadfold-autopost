#!/usr/bin/env python3
"""Cut an object off a white/flat background, give it a halftone dot screen and a white sticker edge.

    python3 studio/editorial/cutout.py SRC OUT.png [--box x0,y0,x1,y1] [--key auto|white] [--tol 18]
Edges: flood-fill from the border (interior whites stay), 1 px erode + 1.2 px feather (no fringe), 12 px white rim.
"""
import argparse
import math
from PIL import Image, ImageChops, ImageDraw, ImageFilter
import numpy as np


def halftone(gray, cell=7, angle=45, mix=0.55):
    """Cosine dot screen (AM halftone) blended with the tone so it reads as print, not noise."""
    g = np.asarray(gray, dtype=np.float32) / 255.0
    h, w = g.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    a = math.radians(angle)
    u = (xx * math.cos(a) + yy * math.sin(a)) * (2 * math.pi / cell)
    v = (-xx * math.sin(a) + yy * math.cos(a)) * (2 * math.pi / cell)
    screen = (np.cos(u) * np.cos(v) + 1) / 2          # 0..1 dot field
    dots = (g > screen * 0.92 + 0.04).astype(np.float32)
    out = mix * dots + (1 - mix) * g
    # keep deep shadows solid and whites clean
    out = np.where(g < 0.12, g, out)
    out = np.where(g > 0.95, 1.0, out)
    return Image.fromarray(np.clip(out * 255, 0, 255).astype(np.uint8), "L")


def cut(src, box=None, tol=18, rim=12, cell=7, holes="fill", min_hole=4000):
    im = Image.open(src).convert("RGB")
    if box:
        im = im.crop(box)
    w, h = im.size
    # border colour = median of the frame edge
    a = np.asarray(im).astype(np.int16)
    edge = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
    bg = np.median(edge, axis=0)
    dist = np.abs(a - bg).max(axis=2)
    near = Image.fromarray(((dist <= tol) * 255).astype(np.uint8), "L")
    # flood from every border pixel that is background: mark as 128
    m = near.copy()
    for x in range(0, w, 4):
        for y in (0, h - 1):
            if m.getpixel((x, y)) == 255:
                ImageDraw.floodfill(m, (x, y), 128)
    for y in range(0, h, 4):
        for x in (0, w - 1):
            if m.getpixel((x, y)) == 255:
                ImageDraw.floodfill(m, (x, y), 128)
    from scipy import ndimage
    solid = np.asarray(m) != 128
    solid = ndimage.median_filter(solid.astype(np.uint8), 5).astype(bool)
    if holes in ("fill", "cut"):
        filled = ndimage.binary_fill_holes(solid)
        if holes == "cut":  # interior background pockets >= min_hole px stay see-through (the OK-sign ring)
            lab, n = ndimage.label(filled & ~solid)
            for k in range(1, n + 1):
                if (lab == k).sum() < min_hole:
                    solid[lab == k] = True
        else:  # close small gaps to the outside first so blown highlights don't leak
            solid = ndimage.binary_fill_holes(ndimage.binary_closing(solid, iterations=8)) & ndimage.binary_dilation(solid, iterations=2) | filled
    alpha = Image.fromarray(solid.astype(np.uint8) * 255, "L")
    alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    bb = alpha.point(lambda p: 255 if p > 20 else 0).getbbox()
    pad = rim + 8
    bb = (max(0, bb[0] - pad), max(0, bb[1] - pad), min(w, bb[2] + pad), min(h, bb[3] + pad))
    im, alpha = im.crop(bb), alpha.crop(bb)
    tone = halftone(im.convert("L"), cell=cell).convert("RGB")
    obj = Image.merge("RGBA", (*tone.split(), alpha))
    rim_a = alpha.point(lambda p: 255 if p > 90 else 0).filter(ImageFilter.MaxFilter(rim * 2 + 1)).filter(ImageFilter.GaussianBlur(1.4))
    out = Image.new("RGBA", obj.size, (255, 255, 255, 0))
    out.paste(Image.new("RGBA", obj.size, (255, 255, 255, 255)), (0, 0), rim_a)
    out.alpha_composite(obj)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--box")
    ap.add_argument("--tol", type=int, default=18)
    ap.add_argument("--cell", type=int, default=7)
    ap.add_argument("--holes", default="fill", choices=["fill", "cut", "keep"])
    a = ap.parse_args()
    box = tuple(int(v) for v in a.box.split(",")) if a.box else None
    cut(a.src, box, a.tol, cell=a.cell, holes=a.holes).save(a.out)
    print(a.out)

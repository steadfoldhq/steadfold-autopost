"""Shared helpers to rebuild listing-image callouts (v0.6.2 staging).
The original image build scripts are not in the repo, so each fix edits the shipped JPG:
it restores the pixels the old callout covered (from identical neighbouring rows of the same
screen) and draws a new callout that does not overlap the screen."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

INTER_DISPLAY_BOLD = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"

def copy_block(im, src_box, dst_xy):
    im.paste(im.crop(src_box), dst_xy)

def fill_rows_from(im, x0, x1, y0, y1, src_y):
    """Fill x0..x1, y0..y1 by repeating pixel row src_y (for flat or x-only-gradient backgrounds)."""
    row = im.crop((x0, src_y, x1, src_y + 1))
    for y in range(y0, y1):
        im.paste(row, (x0, y))

def rounded_mask(size, r):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], r, fill=255)
    return m

def make_callout(content, border_rgb, border=14, radius=34, pad=18, inner_bg=None):
    """Zoom panel: content framed by a rounded border."""
    w, h = content.size[0] + 2 * (pad + border), content.size[1] + 2 * (pad + border)
    panel = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    frame = Image.new("RGBA", (w, h), border_rgb + (255,))
    panel.paste(frame, (0, 0), rounded_mask((w, h), radius))
    iw, ih = w - 2 * border, h - 2 * border
    inner = Image.new("RGBA", (iw, ih), (inner_bg or content.getpixel((2, 2))[:3]) + (255,))
    inner.paste(content.convert("RGBA"), (pad, pad))
    panel.paste(inner, (border, border), rounded_mask((iw, ih), max(4, radius - border)))
    return panel

def make_label(text, size, fg, bg, padx=26, pady=14, radius=16, font=INTER_DISPLAY_BOLD):
    f = ImageFont.truetype(font, size)
    l, t, r, b = f.getbbox(text)
    w, h = r - l + 2 * padx, b - t + 2 * pady
    lab = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(lab)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius, fill=bg + (255,))
    d.text((padx - l, pady - t), text, font=f, fill=fg)
    return lab

def place(im, layer, xy, angle=0.0, shadow=True):
    """Paste an RGBA layer (rotated by angle degrees) with a soft drop shadow."""
    lay = layer.rotate(angle, resample=Image.BICUBIC, expand=True) if angle else layer
    if shadow:
        a = lay.split()[3]
        sh = Image.new("RGBA", lay.size, (10, 5, 30, 0))
        sh.putalpha(a.point(lambda v: int(v * 0.45)))
        pad = 40
        big = Image.new("RGBA", (lay.size[0] + 2 * pad, lay.size[1] + 2 * pad), (0, 0, 0, 0))
        big.paste(sh, (pad, pad))
        big = big.filter(ImageFilter.GaussianBlur(18))
        base = im.convert("RGBA")
        base.alpha_composite(big, (xy[0] - pad + 6, xy[1] - pad + 16))
        im.paste(base.convert("RGB"))
    base = im.convert("RGBA")
    base.alpha_composite(lay, xy)
    im.paste(base.convert("RGB"))
    return lay.size

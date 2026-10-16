import sys; sys.path.insert(0, '/home/claude/shortform')
from engine import *
V = '/home/claude/steadfold-autopost/media/voice/shortform/'
OUT = '/home/claude/shortform/out'

def bg_dots(base, dot, spacing=48, r=3, drift=(0, 0), t=0):
    img = Image.new("RGBA", (W, H), base)
    d = ImageDraw.Draw(img)
    ox = (drift[0] * t) % spacing; oy = (drift[1] * t) % spacing
    y = -spacing + oy
    while y < H + spacing:
        x = -spacing + ox
        while x < W + spacing:
            d.ellipse((x - r, y - r, x + r, y + r), fill=dot); x += spacing
        y += spacing
    return img

def brand_tag(img, text, col, y=150, size=34, x=None):
    f = font("xbold", size); d = ImageDraw.Draw(img)
    tw = text_size(d, text, f)[0]
    d.text(((W - tw) / 2 if x is None else x, y), text, font=f, fill=col)

def zine_card(img, box, fill, ink=(20, 20, 20, 255), r=28, sh=14, width=6):
    rrect(img, box, r, fill, outline=ink, width=width, shadow=(sh, sh, ink))

def appear(t, t0, dur=0.25):
    return ease((t - t0) / dur)

def layer_draw(fn):
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); fn(L); return L

"""FF-MPB image 1 (thumbnail): subtitle says '50/30/20 · paycheck' while the product, its tab and
the same image say 'Paycheque' (Canadian spelling used across the line). Re-set the one word.
Font/position are fitted by rendering the old word and matching it against the image."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageStat

REPO = Path(__file__).resolve().parents[3]
SRC = REPO / "listings/media/money-planner/bundle-01-ONEGLANCE-SQ.jpg"
OUT = REPO / "commerce/v062/images/money-planner/bundle-01-ONEGLANCE-SQ.jpg"
BG, FG = (24, 31, 109), (255, 255, 255)
FONTS = {(w, z): ImageFont.truetype(f"/usr/share/fonts/opentype/inter/Inter-{w}.otf", z)
         for w in ("SemiBold", "Bold") for z in (39, 40, 41, 42)}
im = Image.open(SRC).convert("RGB")
box = (560, 992, 800, 1070)
ref = im.crop(box)

box = (560, 1010, 800, 1068)
ref = im.crop(box)

def render(word, f, x, y):
    t = Image.new("RGB", (box[2] - box[0], box[3] - box[1]), BG)
    ImageDraw.Draw(t).text((x, y), word, font=f, fill=FG)
    return t

best = min(((ImageStat.Stat(ImageChops.difference(render("paycheck", f, x, y), ref)).mean[0], k, x, y)
            for k, f in FONTS.items() for x in range(12, 26) for y in range(-20, 10)))
print("fit error, font, x, y:", best)
_, k, x, y = best
d = ImageDraw.Draw(im)
d.rectangle([575, 1012, 800, 1066], fill=BG)
d.text((box[0] + x, box[1] + y), "paycheque", font=FONTS[k], fill=FG)
OUT.parent.mkdir(parents=True, exist_ok=True)
im.save(OUT, quality=92)
print(OUT)

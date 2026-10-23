"""HB-SUB-02: the 'the number' callout covered the chart title ('Per year, by categor'), two values
of the 'Your 5 biggest' table and the end of a note line. Rebuild: restore the covered area and put
the zoom of the KPI block in the empty space right of the screen.
Restored values are read or derived from the same screen:
  Video streaming (main) 215.88 (visible above the old label);
  News site 208.00 = 'News and reading' 387.40 - Audiobooks 179.40 (14.95 x 12, Renewals screen 05).
The note line under the table ('Small prices add up: a weekly price is bille...') ran under the old
callout and its ending is not visible anywhere, so the line is removed rather than guessed."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, str(Path(__file__).parent))
from callout import fill_rows_from, make_callout, make_label, place

REPO = Path(__file__).resolve().parents[3]
SRC = REPO / "listings/media/subscription-audit/HB-SUB-02-one-yearly-bill.jpg"
OUT = REPO / "commerce/v062/images/subscription-audit/HB-SUB-02-one-yearly-bill.jpg"
CREAM, WHITE, INK = (255, 248, 238), (255, 255, 255), (42, 34, 57)
im = Image.open(SRC).convert("RGB")
orig = im.copy()
d = ImageDraw.Draw(im)

# 1. table rows 'Video streaming (main)' and 'News site': copy the 'Music family plan' row structure
row = orig.crop((1395, 701, 1629, 753))
im.paste(row, (1395, 752))
im.paste(row, (1395, 803))
vf = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 20)
for top, val in ((752, "215.88"), (803, "208.00")):
    d.rectangle([1455, top + 10, 1624, top + 44], fill=WHITE)
    l, t, r, b = vf.getbbox(val)
    d.text((1539.5 - (r - l) / 2 - l, top + 18 - t), val, font=vf, fill=INK)
# keep each row's original label text (left of x 1395) untouched; restore the row bottom line at 855
for x in range(1395, 1629):
    im.paste(orig.crop((1300, 852, 1301, 860)), (x, 852))

# 2. cream gap, note line removed, chart box rebuilt
d.rectangle([1395, 857, 1628, 966], fill=CREAM)
d.rectangle([1060, 893, 1628, 945], fill=CREAM)
d.rectangle([1395, 968, 1565, 1180], fill=WHITE)
for x in range(1395, 1567):
    im.paste(orig.crop((1300, 964, 1301, 970)), (x, 964))      # top border
for y in range(964, 1182):
    im.paste(orig.crop((1563, 1200, 1575, 1201)), (1563, y))  # right border
d.rectangle([1575, 964, 1628, 1180], fill=CREAM)
# corner: rows 964-969 right of the border are cream
d.rectangle([1568, 960, 1628, 968], fill=CREAM)
# chart title, centred on the chart box (x 1072..1567) like the original
d.rectangle([1150, 990, 1560, 1050], fill=WHITE)
tf = ImageFont.truetype("/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf", 33)
title = "Per year, by category"
l, t, r, b = tf.getbbox(title)
d.text((1319.5 - (r - l) / 2 - l, 1005 - t), title, font=tf, fill=(0, 0, 0))

# 3. background right of the screen
fill_rows_from(im, 1629, 2400, 740, 1200, 1250)

# 4. new zoom of the KPI block, right of the screen
content = orig.crop((140, 540, 672, 672))
content = content.resize((int(content.width * 1.2), int(content.height * 1.2)), Image.LANCZOS)
panel = make_callout(content, (255, 201, 80), border=13, radius=30, pad=12, inner_bg=CREAM)
label = make_label("the number", 44, (255, 255, 255), INK)
pw, ph = place(im, panel, (1668, 650), angle=1.5)
place(im, label, (1690, 572), angle=1.5)
OUT.parent.mkdir(parents=True, exist_ok=True)
im.save(OUT, quality=92)
print(OUT, pw, ph)

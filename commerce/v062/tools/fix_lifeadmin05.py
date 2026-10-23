"""HB-LIFEADMIN-05: 9 date cells render as '###' (column too narrow for 'Mon Nov 16, 2026').
The image is redrawn with the dates those cells hold. Values are back-solved from what the screen
shows, and every one is consistent with it:
  today = Sat Oct 17, 2026 (Laptop: Sep 12 2027 - 330 d; Phone: Nov 21 2026 - 35 d; TV: Jul 9 2027 - 265 d)
  Covered until = Bought on + warranty months; Days left = Covered until - today.
  Fridge 30 d -> Mon Nov 16, 2026 (bought Sat Nov 16, 2024, 24 mo)
  Stroller 165 d -> Wed Mar 31, 2027 (bought Tue Mar 31, 2026, 12 mo)
  Vacuum -30 d -> Thu Sep 17, 2026 (bought Tue Sep 17, 2024, 24 mo)
Text is Liberation Sans 23 px (the screen uses 25 px; at 25 px the longest date is 204 px in a
198 px column, which is why the file shows ###). The PRODUCT still needs its columns widened."""
import datetime as D
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[3]
SRC = REPO / "listings/media/life-admin/HB-LIFEADMIN-05-warranties.jpg"
OUT = REPO / "commerce/v062/images/life-admin/HB-LIFEADMIN-05-warranties.jpg"
TODAY = D.date(2026, 10, 17)

def edate(d, m):
    return D.date(d.year + (d.month - 1 + m) // 12, (d.month - 1 + m) % 12 + 1, d.day)

fmt = lambda d: d.strftime("%a %b %-d, %Y")
rows = [  # (row top, bought, months, days-left shown on the screen)
    (690, D.date(2025, 9, 12), 24, 330), (740, D.date(2024, 11, 16), 24, 30),
    (790, D.date(2025, 11, 21), 12, 35), (840, D.date(2026, 3, 31), 12, 165),
    (890, D.date(2024, 9, 17), 24, -30)]
for top, b, m, dl in rows:  # self-check against the screen's Days left
    assert (edate(b, m) - TODAY).days == dl, (b, m, dl)

im = Image.open(SRC).convert("RGB")
d = ImageDraw.Draw(im)
f = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 23)
INK = (40, 36, 50)

def redraw(x0, x1, top, text):
    box = (x0 + 3, top + 4, x1 - 3, top + 46)
    dark = [(x, y) for x in range(*box[0::2]) for y in range(box[1], box[3]) if sum(im.getpixel((x, y))) < 450]
    if not dark:
        return False
    bg = im.getpixel((x0 + 4, top + 8))
    xs, ys = [p[0] for p in dark], [p[1] for p in dark]
    d.rectangle([min(xs) - 2, min(ys) - 2, max(xs) + 2, max(ys) + 2], fill=bg)
    l, t, r, bb = f.getbbox(text)
    cx = (x0 + x1) / 2
    d.text((cx - (r - l) / 2 - l, min(ys) - t), text, font=f, fill=INK)
    return True

for top, b, m, dl in rows:
    if b in (D.date(2024, 11, 16), D.date(2026, 3, 31), D.date(2024, 9, 17)):
        redraw(431, 629, top, fmt(b))          # Bought on (only the ### cells)
    redraw(1547, 1744, top, fmt(edate(b, m)))  # Covered until (all 5 were ###)
OUT.parent.mkdir(parents=True, exist_ok=True)
im.save(OUT, quality=92)
print(OUT)

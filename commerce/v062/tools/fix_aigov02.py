"""SF-AIGOV-02: the 'the decision' callout clipped its own text (a half-cut 'Not answered yet'
row at its top edge) and covered the Why column of rows 6-10. Rebuild: restore the covered
cells, then draw a new zoom of the Decision block in the empty area to the right."""
import sys
from pathlib import Path
from PIL import Image
sys.path.insert(0, str(Path(__file__).parent))
from callout import fill_rows_from, make_callout, make_label, place

REPO = Path(__file__).resolve().parents[3]
SRC = REPO / "listings/media/ai-governance/SF-AIGOV-02-launch-gate.jpg"
OUT = REPO / "commerce/v062/images/ai-governance/SF-AIGOV-02-launch-gate.jpg"

im = Image.open(SRC).convert("RGB")
orig = im.copy()
# 1. background right of the screen (x >= 1410): rebuild rows 815-1150 from clean row 1300
fill_rows_from(im, 1410, 2400, 815, 1150, 1300)
# 2. screen cells under the old callout. Row lines: 820 866 911 957 1002 1048 1094 1139.
lav = orig.crop((1245, 729, 1413, 775))          # row 3, Why column right part (no text there)
im.paste(lav.crop((0, 0, 168, 46)), (1245, 866))  # row 6
im.paste(lav.crop((15, 0, 168, 46)), (1260, 911))  # row 7 (keep '...concern' text left of 1260)
im.paste(lav.crop((5, 0, 164, 14)), (1250, 911))    # row 7 top strip: corner of the old label
im.paste(lav.crop((30, 0, 168, 46)), (1275, 820))   # row 5 right of '...9 tests run'
im.paste(lav.crop((5, 30, 30, 46)), (1250, 850))    # row 5 below the end of 'run'
im.paste(lav.crop((5, 39, 15, 46)), (1250, 950))    # row 7 under 'concern': frame corner
wht = orig.crop((1044, 1139, 1413, 1185))         # row 12, empty white Why cell (whole column)
for top in (957, 1002, 1048, 1094):
    im.paste(wht, (1044, top))
# 3. new zoom of the Decision block (score cell + decision + reasons), from the same screen
content = orig.crop((834, 1376, 1408, 1512))
content = content.resize((int(content.width * 1.42), int(content.height * 1.42)), Image.LANCZOS)
panel = make_callout(content, (236, 240, 117), border=14, radius=34, pad=16, inner_bg=(246, 243, 254))
label = make_label("the decision", 44, (255, 255, 255), (27, 14, 60))
pw, ph = place(im, panel, (1452, 1240), angle=1.5)
place(im, label, (1475, 1165), angle=1.5)
OUT.parent.mkdir(parents=True, exist_ok=True)
im.save(OUT, quality=92)
print(OUT, pw, ph)

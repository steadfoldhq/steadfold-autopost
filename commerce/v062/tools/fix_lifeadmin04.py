"""HB-LIFEADMIN-04: (a) the subtitle promised more than the file does ("Type an ID number or a
password"): v1.0 flags only 5+ digits and the word "password" (QA Oct 21); (b) the "safety check"
callout zoomed on date/OK rows, not on the row the check actually flags. Rebuild: new subtitle
matching the in-sheet rule and the corrected listing copy; restore the cells the old callout
covered; new zoom on the flagged Health card row, placed in the empty area under the screen."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, str(Path(__file__).parent))
from callout import fill_rows_from, make_callout, make_label, place

REPO = Path(__file__).resolve().parents[3]
SRC = REPO / "listings/media/life-admin/HB-LIFEADMIN-04-where-its-kept.jpg"
OUT = REPO / "commerce/v062/images/life-admin/HB-LIFEADMIN-04-where-its-kept.jpg"
BG = (93, 84, 201)
im = Image.open(SRC).convert("RGB")
orig = im.copy()

# (a) subtitle
d = ImageDraw.Draw(im)
d.rectangle([100, 268, 2300, 400], fill=BG)
f = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Regular.otf", 51)
col = (242, 240, 255)
for i, line in enumerate(["An index of every important paper. Type 5 or more digits or the word",
                          "“password” and it asks you to remove them."]):
    l, t, r, b = f.getbbox(line)
    d.text((111 - l, 277 - t + i * 67), line, font=f, fill=col)

# (b1) background right of the screen, y 540-870: repeat clean row 900
fill_rows_from(im, 1669, 2400, 540, 875, 900)
# (b2) header cell of the Check column: tile a clean dark column, redraw the header word
for x in range(1440, 1669):
    im.paste(orig.crop((1440, 537, 1441, 588)), (x, 537))
hf = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 16)
l, t, r, b = hf.getbbox("Check")
d.text((1463 - l, 556 - t), "Check", font=hf, fill=(255, 255, 255))
# (b3) Check column body rows 1-7 (y 587-864): tile clean columns of the same rows
for x in range(1340, 1669):
    im.paste(orig.crop((1350, 587, 1351, 657)), (x, 587))   # rows 1-2 (peach)
    im.paste(orig.crop((1350, 691, 1351, 864)), (x, 691))   # rows 4-7 (peach)
for x in range(1476, 1669):
    im.paste(orig.crop((1478, 657, 1479, 691)), (x, 657))   # row 3 'Will' (amber flag)

# (b4) new zoom: rows 'Spare house key' .. 'Marriage certificate', columns Where it's kept .. Check
content = orig.crop((530, 864, 1662, 964))
content = content.resize((int(content.width * 1.5), int(content.height * 1.5)), Image.LANCZOS)
panel = make_callout(content, (255, 200, 80), border=14, radius=30, pad=14, inner_bg=(255, 255, 255))
label = make_label("safety check", 46, (255, 255, 255), (42, 34, 57))
pw, ph = place(im, panel, (300, 1150), angle=-1.0)
place(im, label, (330, 1068), angle=-1.0)
OUT.parent.mkdir(parents=True, exist_ok=True)
im.save(OUT, quality=92)
print(OUT, pw, ph)

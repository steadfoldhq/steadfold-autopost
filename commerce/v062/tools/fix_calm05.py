"""DP-CALM-P / DP-CALM-T image 05: the tag on the Steady card reads 'This example'. The founder's
brand rule (brand-system-v4, Oct 17; North Star machine rule) bans the word 'example' anywhere.
Rebuild: a same-shape pill over the old one, reading 'Sample week'. Same pixels in both images."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[3]
PILL, TEXT = (21, 19, 20), (255, 211, 60)
F = ImageFont.truetype("/usr/share/fonts/opentype/inter/InterDisplay-ExtraBold.otf", 40)

def pill(text, w=292, h=64):
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.rounded_rectangle([0, 0, w - 1, h - 1], 24, fill=PILL + (255,))
    l, t, r, b = F.getbbox(text)
    d.text(((w - (r - l)) / 2 - l, (h - (b - t)) / 2 - t), text, font=F, fill=TEXT)
    return lay.rotate(-4.0, resample=Image.BICUBIC, expand=True)

for kind in ("print", "tablet"):
    src = REPO / f"listings/media/calm-planner-2027/{kind}/05-calm-check.jpg"
    out = REPO / f"commerce/v062/images/calm-planner-2027/{kind}/05-calm-check.jpg"
    im = Image.open(src).convert("RGBA")
    lay = pill("Sample week")
    # old pill measured from dark pixels: x 1015..1294, y 1044..1116, tilted ~4 deg clockwise.
    # (v1 of this script centred on y 1097, which included the card border and left old corners visible.)
    cx, cy = 1155, 1080
    im.alpha_composite(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)))
    out.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(out, quality=92)
    print(out)

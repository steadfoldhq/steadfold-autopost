"""Before/after sheets for every corrected listing image (v0.6.2). Left: the image live on Etsy today
(listings/media, untouched). Right: the corrected copy in commerce/v062/images. Labels name the defect."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[3]
OUT = REPO / "commerce/v062/images/before-after"
F = ImageFont.truetype("/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf", 44)
S = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Regular.otf", 32)
FIXES = [
    ("SF-AIGOV-02", "ai-governance/SF-AIGOV-02-launch-gate.jpg", "Callout clipped its own text and covered the Why column"),
    ("HB-SUB-02", "subscription-audit/HB-SUB-02-one-yearly-bill.jpg", "Callout covered the chart title and two table values"),
    ("HB-LIFEADMIN-04", "life-admin/HB-LIFEADMIN-04-where-its-kept.jpg", "Subtitle overclaimed the check; zoom showed date rows, not the flagged row"),
    ("HB-LIFEADMIN-05", "life-admin/HB-LIFEADMIN-05-warranties.jpg", "Nine date cells showed ### (column too narrow)"),
    ("DP-CALM-P-05", "calm-planner-2027/print/05-calm-check.jpg", "Tag used the banned word 'example' (brand rule 12b)"),
    ("DP-CALM-T-05", "calm-planner-2027/tablet/05-calm-check.jpg", "Tag used the banned word 'example' (brand rule 12b)"),
    ("FF-MPB-01", "money-planner/bundle-01-ONEGLANCE-SQ.jpg", "Thumbnail said 'paycheck'; the product line uses 'paycheque'"),
]
OUT.mkdir(parents=True, exist_ok=True)
for name, rel, why in FIXES:
    a = Image.open(REPO / "listings/media" / rel).convert("RGB")
    b = Image.open(REPO / "commerce/v062/images" / rel).convert("RGB")
    assert a.size == b.size, (name, a.size, b.size)
    w = 1400; h = int(a.height * w / a.width)
    a, b = a.resize((w, h), Image.LANCZOS), b.resize((w, h), Image.LANCZOS)
    sheet = Image.new("RGB", (2 * w + 60, h + 200), (245, 245, 250))
    d = ImageDraw.Draw(sheet)
    d.text((20, 18), f"{name}: {why}", font=F, fill=(20, 26, 70))
    d.text((20, 120), "BEFORE (live on Etsy now)", font=S, fill=(179, 38, 30))
    d.text((w + 40, 120), "AFTER (commerce/v062/images)", font=S, fill=(30, 123, 79))
    sheet.paste(a, (20, 180)); sheet.paste(b, (w + 40, 180))
    out = OUT / f"{name}-before-after.jpg"
    sheet.save(out, quality=88)
    print(out.name, b.size)

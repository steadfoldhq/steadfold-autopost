#!/usr/bin/env python3
"""2 x 4 contact sheet of the 8 style prototypes: each cell = hook frame (B1) + fix frame (B3), labelled.

    STYLE_OUT=... python3 studio/styles/contact.py OUT.jpg
"""
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(os.environ.get("STYLE_OUT", "/tmp/style-menu"))
NAMES = ["storybook", "footage-doodles", "paper-cutout", "liquid-type", "phone-ui", "desk-drop", "scrapbook", "character"]
LABELS = ["Storybook parallax", "Footage + doodles", "Paper cut-out", "Liquid type", "Phone UI explosion", "3D desk drop", "Scrapbook", "Character (Lockie)"]
FW, FH, PAD, LAB = 300, 533, 18, 70
FB = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Black.otf", 34)
FS = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", 22)


def main(out):
    cw, ch = 2 * FW + PAD, FH + LAB
    sheet = Image.new("RGB", (4 * cw + 5 * PAD, 2 * ch + 3 * PAD + 70), "#FFE27A")
    d = ImageDraw.Draw(sheet)
    d.text((PAD, 18), "Steadfold style menu · same Locked Hour script, 8 visual languages", font=FB, fill="#141414")
    for i, (n, lab) in enumerate(zip(NAMES, LABELS)):
        r, c = divmod(i, 4)
        x0, y0 = PAD + c * (cw + PAD), 70 + PAD + r * (ch + PAD)
        for k, hero in enumerate(("hero-1.jpg", "hero-3.jpg")):
            p = OUT / f"Style-{i + 1}-{n}" / hero
            if p.exists():
                sheet.paste(Image.open(p).convert("RGB").resize((FW, FH), Image.LANCZOS), (x0 + k * (FW + PAD), y0))
        d.text((x0, y0 + FH + 10), f"{i + 1}  {lab}", font=FB, fill="#141414")
        d.text((x0 + 2 * FW + PAD, y0 + FH + 16), "hook  ·  the fix", font=FS, fill="#141414", anchor="ra")
    sheet.save(out, quality=90)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1])

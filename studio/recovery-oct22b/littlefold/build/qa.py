#!/usr/bin/env python3
"""QA sheet: frames at given times side by side. Usage: qa.py video.mp4 out.jpg t1,t2,..."""
import sys, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
v, out, ts = sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3].split(",")]
w = int(sys.argv[4]) if len(sys.argv) > 4 else 360
ims = []
for t in ts:
    f = tempfile.mktemp(suffix=".png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", v, "-frames:v", "1", f], check=True)
    ims.append(Image.open(f).convert("RGB").resize((w, int(w * 16 / 9)), Image.LANCZOS))
S = Image.new("RGB", (w * len(ims) + 10 * (len(ims) - 1), ims[0].height + 50), "#F4F1EC")
d = ImageDraw.Draw(S); font = ImageFont.load_default(size=28)
for k, (im, t) in enumerate(zip(ims, ts)):
    S.paste(im, (k * (w + 10), 50)); d.text((k * (w + 10) + 8, 10), f"{t:.2f}s", fill="black", font=font)
S.save(out, quality=88)

#!/usr/bin/env python3
"""Side-by-side before/after sheets. Usage: ba.py out.jpg "before1,before2" "after1,after2" (paths under media/, or video@t)."""
import sys, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
M = '/home/claude/steadfold-autopost/media/'
def load(spec):
    if '@' in spec:
        v, t = spec.split('@'); f = tempfile.mktemp(suffix='.png')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', t, '-i', M + v, '-frames:v', '1', f], check=True)
        return Image.open(f).convert('RGB'), f'{v.split("/")[-1]} @ {t}s'
    return Image.open(M + spec).convert('RGB'), spec.split('/')[-1]
def row(specs, h):
    out = []
    for s in specs:
        im, lab = load(s); out.append((im.resize((int(im.width * h / im.height), h), Image.LANCZOS), lab))
    return out
out, b, a = sys.argv[1], sys.argv[2].split(','), sys.argv[3].split(',')
H = 900; f = ImageDraw.Draw(Image.new('RGB', (1, 1))); font = ImageFont.load_default(size=30); big = ImageFont.load_default(size=44)
rb, ra = row(b, H), row(a, H)
wb = sum(i.width for i, _ in rb) + 20 * (len(rb) - 1); wa = sum(i.width for i, _ in ra) + 20 * (len(ra) - 1)
W = wb + wa + 120; S = Image.new('RGB', (W, H + 140), '#F4F1EC'); d = ImageDraw.Draw(S)
d.text((30, 20), 'BEFORE', fill='#8A2B55', font=big); d.text((wb + 90, 20), 'AFTER', fill='#2E7D4F', font=big)
x = 30
for im, lab in rb:
    S.paste(im, (x, 80)); d.text((x, H + 90), lab, fill='black', font=font); x += im.width + 20
x = wb + 90; d.line([(wb + 60, 20), (wb + 60, H + 120)], fill='#999', width=4)
for im, lab in ra:
    S.paste(im, (x, 80)); d.text((x, H + 90), lab, fill='black', font=font); x += im.width + 20
S.save(out, quality=85)
print(out)

import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '/home/claude/content/oct16-21')
import reels_lib as L
O = Path('/home/claude/hb-pilots/out'); F = '/home/claude/content/design/assets/fonts/'
E = json.load(open('entries.json'))
f1 = ImageFont.truetype(F + 'Inter-Bold.ttf', 20); f2 = ImageFont.truetype(F + 'Inter-Medium.ttf', 16); fh = ImageFont.truetype(F + 'Inter-Bold.ttf', 34)
TW, TH = 220, 391
def thumb(p):
    if p.get('story'): im = Image.open(O / p['image'])
    elif p.get('video'): im = Image.open(O / p['cover'])
    else: im = Image.open(O / p['images'][0])
    im = im.convert('RGB'); r = min(TW / im.width, TH / im.height)
    return im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
days = {}
for p in E: days.setdefault(p['publish_at'][:10], []).append(p)
cols = max(len(v) for v in days.values())
rowh = TH + 110
W = 40 + cols * (TW + 16); H = 120 + len(days) * (rowh + 50)
# reel frame strips
reels = [p for p in E if p.get('video')]
SW = 150; SH = 267
H += 80 + len(reels) * (SH + 60)
S = Image.new('RGB', (max(W, 40 + 8 * (SW + 10) + 380), H), '#EFEAF6'); d = ImageDraw.Draw(S)
d.text((40, 30), f'Hourback pilots · Oct 19–21 · {len(E)} items (scheduled by B1; say "pull <id>" to stop one)', fill='#2A2238', font=fh)
y = 110
for day, ps in days.items():
    d.text((40, y), day, fill='#5E54C9', font=f1); y += 34
    for i, p in enumerate(ps):
        x = 40 + i * (TW + 16); t = thumb(p); S.paste(t, (x + (TW - t.width) // 2, y))
        k = 'STORY' if p.get('story') else ('REEL' if p.get('video') else ('CAROUSEL' if len(p['images']) > 1 else 'SINGLE'))
        d.text((x, y + TH + 8), f"{p['publish_at'][11:16]} · {k}", fill='#2A2238', font=f1)
        d.text((x, y + TH + 34), p['id'][3:30], fill='#555', font=f2)
    y += rowh + 16
y += 20; d.text((40, y), 'Reel frames (cover, then every ~3 s)', fill='#2A2238', font=f1); y += 40
for p in reels:
    mp4 = O / p['video']; dur = L.probe(mp4)['dur']
    ims = [Image.open(O / p['cover']).convert('RGB')] + [L.still(mp4, t) for t in [0.0, 3.0, 6.0, 9.0, 12.0, min(15.0, dur - 0.3)]]
    d.text((40, y), f"{p['id']} · {p['publish_at'][5:16]} · {dur:.1f}s", fill='#2A2238', font=f1)
    for i, im in enumerate(ims): S.paste(im.resize((SW, SH), Image.LANCZOS), (40 + i * (SW + 10), y + 28))
    y += SH + 60
S.save(O / 'hourback-pilots-oct19-21-contact-sheet.jpg', quality=88)
print(S.size)

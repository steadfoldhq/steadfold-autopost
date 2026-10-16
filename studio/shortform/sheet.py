import sys, importlib; sys.path.insert(0, '/home/claude/shortform')
from PIL import Image
mod, ts = sys.argv[1], [float(x) for x in sys.argv[2].split(',')]
m = importlib.import_module(mod)
ims = [m.frame(t).convert('RGB').resize((540, 960)) for t in ts]
s = Image.new('RGB', (540 * len(ims), 960)); [s.paste(im, (i * 540, 0)) for i, im in enumerate(ims)]
s.save(f'/home/claude/shortform/out/{mod}_sheet.jpg')

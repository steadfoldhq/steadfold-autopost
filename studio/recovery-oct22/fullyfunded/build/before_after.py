#!/usr/bin/env python3
"""Side-by-side before/after sheets for the FF recovery items -> before-after/<id>.jpg"""
import subprocess, sys, textwrap, tempfile, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
M = Path("/home/claude/steadfold-autopost/media")
OUT = Path("/home/claude/steadfold-autopost/studio/recovery-oct22/fullyfunded/before-after")
F = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
font = lambda s: ImageFont.truetype(F, s)  # noqa: E731


def frames(mp4, ts):
    out = []
    for t in ts:
        f = tempfile.mktemp(suffix=".jpg")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(mp4), "-frames:v", "1", f], check=True)
        out.append(Image.open(f).convert("RGB")); os.unlink(f)
    return out


def dur(mp4):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp4)],
                                capture_output=True, text=True).stdout)


def row(ims, labels, h):
    ims = [i.resize((int(i.width * h / i.height), h), Image.LANCZOS) for i in ims]
    W = sum(i.width for i in ims) + 16 * (len(ims) + 1)
    R = Image.new("RGB", (W, h + 44), "#1d1d24"); d = ImageDraw.Draw(R); x = 16
    for im, lb in zip(ims, labels):
        R.paste(im, (x, 40)); d.text((x, 10), lb, fill="#dddddd", font=font(20)); x += im.width + 16
    return R


def stack(title_a, ra, title_b, rb, out):
    W = max(ra.width, rb.width)
    S = Image.new("RGB", (W, ra.height + rb.height + 120), "#111116"); d = ImageDraw.Draw(S)
    d.text((16, 12), title_a, fill="#ff9a7a", font=font(28)); S.paste(ra, (0, 52))
    y = 52 + ra.height + 8
    d.text((16, y), title_b, fill="#9fb0ff", font=font(28)); S.paste(rb, (0, y + 40))
    S.save(out, quality=88)


def reel(before_mp4, before_cover, after_mp4, after_cover, name, tb, ta):
    L = ["cover", "0.2 s", "1.5 s", "3.5 s", "last s"]
    db, da = dur(before_mp4), dur(after_mp4)
    rb = row([Image.open(before_cover)] + frames(before_mp4, [0.2, 1.5, 3.5, db - 0.8]), L, 560)
    ra = row([Image.open(after_cover)] + frames(after_mp4, [0.2, 1.5, 3.5, da - 0.8]), L, 560)
    stack(f"BEFORE · {tb} ({db:.1f} s)", rb, f"AFTER · {ta} ({da:.1f} s)", ra, OUT / f"{name}.jpg")


def text_card(txt, w=900, h=1100, bg="#F7F1E5"):
    im = Image.new("RGB", (w, h), bg); d = ImageDraw.Draw(im); y = 30
    for para in txt.split("\n"):
        for line in (textwrap.wrap(para, 62) or [""]):
            d.text((30, y), line, fill="#141A55", font=font(22)); y += 30
    return im


if __name__ == "__main__":
    what = sys.argv[1]
    if what == "richhabits":
        b = [Image.open(M / f"ff-richhabits-01/0{i}.jpg") for i in (1, 2, 3)]
        a = [Image.open(M / f"recovery-oct22/fullyfunded/ff-richhabits-01/0{i}.jpg") for i in (1, 2, 3)]
        stack("BEFORE · piggy cut-out (overused), unqualified '3.5% → 13.6%'", row(b, ["1", "2", "3"], 560),
              "AFTER · drawn pay-week chart, 'saving rate · in one study' + source", row(a, ["1", "2", "3"], 560), OUT / "ff-richhabits-01.jpg")
    elif what == "reels":
        R = M / "reels"; N = M / "recovery-oct22/fullyfunded"
        reel(R / "ff-pan-1025am-paycheque-trail-s15.mp4", R / "ff-pan-1025am-paycheque-trail-cover.jpg",
             N / "ff-pan-1025am-wills-s15.mp4", N / "ff-pan-1025am-wills-s15-cover.jpg", "ff-pan-1025am-paycheque-trail",
             "duplicate of Sat noon carousel, piggy", "REPLACED: 'Not married? No will?' Trial Reel, drawn to scale")
        reel(R / "ff-reel-1025-tfsa-withdrawal-trap-s15.mp4", R / "ff-reel-1025-tfsa-withdrawal-trap-s15-cover.jpg",
             N / "ff-reel-1025-tfsa-trap-s15.mp4", N / "ff-reel-1025-tfsa-trap-s15-cover.jpg", "ff-reel-1025-tfsa-withdrawal-trap",
             "3rd pointing-hand template in 5 Reels, hook static to 3 s", "calendar drawn to scale, payoff $50/mo -> $350 by 4 s")

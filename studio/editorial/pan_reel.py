#!/usr/bin/env python3
"""Pan Reel from a panorama carousel: the camera glides left to right across the slides (eased),
pausing on each, then the "Do this" slide drops in. Uses the panorama saved by formats.py.

    python3 studio/editorial/pan_reel.py <carousel-id> <reel-id> <track>
"""
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parent.parent.parent
W, H, FPS = 1080, 1920, 30


def ease(t):
    return 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))


def main(cid, rid, track):
    pano = Image.open(f"/home/claude/rq/pano/{cid}.jpg").convert("RGB")
    n = pano.width // 1080
    slides = sorted((REPO / "media" / cid).glob("*.jpg"))
    do = Image.open(slides[-1]).convert("RGB")
    bg = pano.getpixel((pano.width // 2, 6))
    top = (H - pano.height) // 2
    hold, move = 1.9, 1.1
    plan = []                                   # (time, x offset)
    t = 0.0
    for i in range(n):
        plan.append((t, i * 1080.0))
        t += hold
        if i < n - 1:
            t += move
    pan_end = t
    total = pan_end + 0.4 + 4.0
    tmp = Path(tempfile.mkdtemp())
    nf = int(total * FPS)
    for f in range(nf):
        tt = f / FPS
        frame = Image.new("RGB", (W, H), bg)
        if tt <= pan_end:
            x = plan[-1][1]
            for k, (t0, x0) in enumerate(plan):
                if tt < t0 + hold:
                    x = x0
                    break
                if k + 1 < len(plan) and tt < plan[k + 1][0]:
                    x = x0 + 1080 * ease((tt - t0 - hold) / move)
                    break
            frame.paste(pano.crop((int(x), 0, int(x) + 1080, pano.height)), (0, top))
        else:
            a = min(1.0, (tt - pan_end) / 0.4)
            last = Image.new("RGB", (W, H), bg)
            last.paste(pano.crop((pano.width - 1080, 0, pano.width, pano.height)), (0, top))
            nxt = Image.new("RGB", (W, H), do.getpixel((540, 6)))
            nxt.paste(do, (0, top))
            frame = Image.blend(last, nxt, a)
        frame.save(tmp / f"{f:05d}.jpg", quality=90)
    lib = json.loads((REPO / "tools" / "music-library.json").read_text())["tracks"]
    out = REPO / "media" / "reels" / f"{rid}.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", str(tmp / "%05d.jpg"),
                    "-i", str(REPO / lib[track]["file"]), "-filter_complex",
                    f"[1:a]atrim=0:{total:.2f},afade=t=out:st={total - 1.5:.2f}:d=1.5,alimiter=limit=0.89[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out)], check=True)
    cover = Image.new("RGB", (W, H), bg)
    cover.paste(pano.crop((0, 0, 1080, pano.height)), (0, top))
    cover.save(REPO / "media" / "reels" / f"{rid}-cover.jpg", quality=92)
    subprocess.run(["rm", "-rf", str(tmp)])
    print(rid, f"{total:.1f}s", out.stat().st_size // 1000, "KB")


if __name__ == "__main__":
    main(*sys.argv[1:4])

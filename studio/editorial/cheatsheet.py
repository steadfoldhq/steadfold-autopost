#!/usr/bin/env python3
"""Canada-edition cheat-sheet Reels: one glance, a table worth saving.
Rows pop in one by one on the music, then the full sheet holds so people can screenshot / save it.

    python3 studio/editorial/cheatsheet.py <id> [...]      -> media/reels/<id>.mp4 + -cover.jpg
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import covers as C  # noqa: E402
import edkit as K  # noqa: E402

W, H = 1080, 1920
LIB = json.loads((REPO / "tools" / "music-library.json").read_text())["tracks"]


def body(spec, upto, show_do):
    b, field = spec["brand"], spec["field"]
    f = K.FIELDS[b][field]
    ink = f["ink"]
    out = (f'<div class="hand" style="position:absolute;left:0;right:0;top:215px;font-size:58px;transform:rotate(-2deg)">'
           f'<span style="font-family:\'Noto Color Emoji\'">🇨🇦</span> Canada edition</div>'
           f'<div style="position:absolute;left:60px;right:60px;top:300px;font-size:{spec.get("tsize", 86)}px;line-height:1.02;color:{ink}">'
           f'{K.dual(spec["title"], f)}</div>')
    top = spec.get("table_top", 640)
    rows = spec.get("rows", [])
    cards = spec.get("cards", [])
    if rows:
        hdr = spec.get("head")
        inner = ""
        if hdr:
            inner += (f'<div style="display:flex;justify-content:space-between;padding:0 8px 10px;font-family:\'Caveat Brush\';font-size:42px;'
                      f'color:{K.ACCENT[b]}"><span>{hdr[0]}</span><span>{hdr[1]}</span></div>')
        for i, (lab, val) in enumerate(rows):
            vis = "visible" if i < upto else "hidden"
            col = f["p1"] if i % 2 == 0 else f["p2"]
            inner += (f'<div style="visibility:{vis};display:flex;justify-content:space-between;align-items:center;padding:12px 8px;'
                      f'border-top:{"0" if i == 0 else "2px dashed " + ink + "33"}">'
                      f'<span class="S" style="font-size:48px;text-align:left;color:{ink}">{lab}</span>'
                      f'<span class="S" style="font-size:54px;color:{ink};background:{col};border-radius:.35em;padding:0 .3em .05em">{val}</span></div>')
        out += (f'<div style="position:absolute;left:56px;right:56px;top:{top}px;background:#fff;border:5px solid {ink};border-radius:40px;'
                f'box-shadow:0 14px 0 {ink};padding:30px 36px">{inner}</div>')
    if cards:
        y = top
        for i, cd in enumerate(cards):
            vis = "visible" if i < upto else "hidden"
            col = f["p1"] if i % 2 == 0 else f["p2"]
            lines = "".join(f'<div class="S" style="font-size:40px;text-align:left;color:{ink};line-height:1.15">· {ln}</div>' for ln in cd["lines"])
            out += (f'<div style="visibility:{vis};position:absolute;left:56px;right:56px;top:{y}px;background:#fff;border:5px solid {ink};'
                    f'border-radius:34px;box-shadow:0 10px 0 {ink};padding:22px 32px;display:flex;gap:28px;align-items:center">'
                    f'<div class="S" style="flex:0 0 230px;font-size:58px;background:{col};border-radius:.3em;padding:6px 0 10px">{cd["name"]}</div>'
                    f'<div style="flex:1">{lines}</div></div>')
            y += spec.get("card_h", 250)
    if show_do:
        dy = spec.get("do_top", 1330)
        out += (f'<div style="position:absolute;left:70px;right:70px;top:{dy}px;display:flex;align-items:center;gap:22px">'
                f'<div class="hand" style="font-size:78px;white-space:nowrap;transform:rotate(-4deg)">Do this:</div>'
                f'<div class="S" style="font-size:46px;text-align:left;color:{ink};line-height:1.08">{K.pills(spec["do"], f)}</div></div>'
                f'<div class="hand" style="position:absolute;left:0;right:0;top:{dy + 150}px;font-size:56px;transform:rotate(-2deg)">{spec["save"]}</div>')
    out += f'<div class="S" style="position:absolute;left:80px;right:80px;top:1640px;font-size:24px;opacity:.6">{spec["src"]}</div>'
    out += K.stamp(b, W - 220, 60, 150, 12)
    return out


def build(pid, spec):
    tmp = Path(tempfile.mkdtemp())
    r = C.R()
    n = len(spec.get("rows") or spec.get("cards"))
    states = []
    try:
        for k in range(n + 2):
            upto, show_do = min(k, n), k == n + 1
            p = tmp / f"s{k:02d}.jpg"
            r.shot(C.page(spec["brand"], spec["field"], body(spec, upto, show_do), W, H), W, H, p)
            states.append(p)
    finally:
        r.close()
    durs = [1.6] + [spec.get("beat", 0.6)] * n + [7.0]
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p}'\nduration {d}\n" for p, d in zip(states, durs)) + f"file '{states[-1]}'\n")
    total = sum(durs)
    out = REPO / "media" / "reels" / f"{pid}.mp4"
    track = REPO / LIB[spec["track"]]["file"]
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(track),
                    "-filter_complex", f"[0:v]fps=30,format=yuv420p[v];[1:a]atrim=0:{total:.2f},afade=t=out:st={total - 1.5:.2f}:d=1.5,"
                    f"alimiter=limit=0.89[a]", "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out)], check=True)
    # cover = the full sheet (what people save)
    from PIL import Image
    Image.open(states[-1]).save(REPO / "media" / "reels" / f"{pid}-cover.jpg", quality=92)
    print(pid, f"{total:.1f}s", out.stat().st_size // 1000, "KB", flush=True)
    return out


if __name__ == "__main__":
    import v5_cheats as V
    for pid in sys.argv[1:]:
        build(pid, V.CHEATS[pid])

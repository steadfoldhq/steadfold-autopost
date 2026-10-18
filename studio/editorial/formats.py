#!/usr/bin/env python3
"""Interactive carousel formats (Oct 18, Dharma's references):
  follow  - "Follow the line": pick a problem, follow its coloured line across slides to the fix (one panorama, sliced)
  travel  - "Travelling icon": an object travels a dotted trail (with a loop) through the words across slides
  hold    - "Hold the dots & slide": near-identical frames that animate when the viewer holds and slides (a flipbook)
  reveal  - "Swipe to reveal": the answer starts pixelated and sharpens slide by slide

    python3 studio/editorial/formats.py <id> [...]       (ids from FORMATS below; writes media/<id>/NN.jpg)
Content is registered with specs_teach.post() in v5_formats.py so the scheduler picks it up like any feed post.
"""
import math
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import covers as C  # noqa: E402
import edkit as K  # noqa: E402

W, H = 1080, 1350


def f_(b, field):
    return K.FIELDS[b][field]


def txt(b, field, text, x, y, w, size, align="center", z=4, cls="S"):
    f = f_(b, field)
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;z-index:{z};font-size:{size}px;line-height:1.04;'
            f'color:{f["ink"]};text-align:{align}">{K.dual(text, f, cls=cls)}</div>')


def hand(b, text, x, y, w, size=60, rot=-3, col=None, z=5, align="center"):
    return (f'<div class="hand" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;transform:rotate({rot}deg);'
            f'z-index:{z};text-align:{align};{"color:" + col if col else ""}">{text}</div>')


def counter(i, n, x=W - 120, y=40):
    return f'<div class="S" style="position:absolute;left:{x}px;top:{y}px;font-size:26px;opacity:.45">{i}/{n}</div>'


def do_card(b, field, text, save, x=70, y=380):
    f = f_(b, field)
    ink = f["ink"]
    return (hand(b, "Do this:", 0, y - 200, W, 120, -4)
            + f'<div style="position:absolute;left:{x}px;top:{y}px;width:{W - 2 * x}px;background:#fff;border:5px solid {ink};border-radius:44px;'
            f'box-shadow:0 16px 0 {ink};padding:56px 52px;z-index:4;font-size:76px;line-height:1.08;color:{ink}">{K.dual(text, f)}</div>'
            + hand(b, save, 120, y + 640, W - 240, 56, -3)
            + K.obj("point", -70, y + 470, 330, -10) + K.stamp(b, W - 250, H - 260, 170, 12))


def shot_pano(r, b, field, body, n, out_dir):
    """Render one (n*W) x H canvas and slice it into n slides."""
    tmp = out_dir / "_pano.jpg"
    r.shot(C.page(b, field, body, n * W, H), n * W, H, tmp)
    im = Image.open(tmp)
    files = []
    for i in range(n):
        p = out_dir / f"{i + 1:02d}.jpg"
        im.crop((i * W, 0, (i + 1) * W, H)).save(p, quality=92, subsampling=0)
        files.append(p)
    keep = Path("/home/claude/rq/pano")
    keep.mkdir(parents=True, exist_ok=True)
    im.save(keep / f"{out_dir.name}.jpg", quality=92)
    tmp.unlink()
    return files


# ----------------------------------------------------------------------------------------------- follow the line
def follow(r, spec, out_dir):
    b, field = spec["brand"], spec["field"]
    n = spec["pano"]                       # slides in the panorama (last one holds the answers)
    f = f_(b, field)
    starts = [470 + 220 * k for k in range(len(spec["lines"]))]
    ends = [260 + 320 * k for k in range(len(spec["lines"]))]
    body = ""
    # dot-grid paper feel
    body += (f'<div style="position:absolute;inset:0;background-image:radial-gradient({f["ink"]}22 2.2px,transparent 2.6px);'
             f'background-size:44px 44px;opacity:.6"></div>')
    svg = [f'<svg style="position:absolute;left:0;top:0;z-index:2" width="{n * W}" height="{H}" viewBox="0 0 {n * W} {H}">']
    for k, ln in enumerate(spec["lines"]):
        y0, y1 = starts[k] + 70, ends[k] + 50
        xs = [780 + 50 * k] + [W * j + 200 + 230 * ((k + j) % 3) for j in range(1, n - 1)] + [W * (n - 1) + 40 + 45 * k]
        ys = [y0] + [[430, 680, 930][(k + j) % 3] + 60 * (j % 2) for j in range(1, n - 1)] + [y1]
        pts = [(0, y0)]
        x_prev, y_prev = 0, y0
        for x, y in zip(xs, ys):
            pts += [(x, y_prev), (x, y)]
            y_prev = y
        pts += [(W * (n - 1) + 150, y_prev)]
        d = " ".join(f"{x},{y}" for x, y in pts)
        svg.append(f'<polyline points="{d}" fill="none" stroke="{ln["col"]}" stroke-width="16" stroke-linejoin="round" stroke-linecap="round"/>')
    svg.append("</svg>")
    body += "".join(svg)
    # slide 1: hook + the starting points
    body += txt(b, field, spec["hook"], 60, 120, W - 120, 104)
    for k, ln in enumerate(spec["lines"]):
        y = starts[k]
        body += (f'<div style="position:absolute;left:60px;top:{y}px;width:640px;z-index:4;background:#fff;border:4px solid {f["ink"]};'
                 f'border-left:22px solid {ln["col"]};border-radius:22px;padding:16px 24px;box-shadow:0 8px 0 {f["ink"]}">'
                 f'<div class="S" style="font-size:54px;line-height:1.05;text-align:left;color:{f["ink"]}">{K.pills(ln["start"], f)}</div></div>'
                 f'<div style="position:absolute;left:{560}px;top:{y - 40}px;z-index:6;font-family:\'Noto Color Emoji\';font-size:110px;'
                 f'transform:rotate({-8 + 8 * k}deg);filter:drop-shadow(0 10px 12px rgba(0,0,0,.18))">{ln.get("icon", "")}</div>')
    body += hand(b, "pick one · follow its line →", 140, H - 190, 800, 60)
    # middle slides: little nudges
    for j, note in enumerate(spec["notes"], 1):
        body += hand(b, note, W * j + 140, 150, 800, 72, -4)
    # last slide: the fixes, each at the end of its line
    x0 = W * (n - 1)
    body += hand(b, "you made it!", x0 + 140, 80, 800, 72, -3)
    for k, ln in enumerate(spec["lines"]):
        y = ends[k]
        body += (f'<div style="position:absolute;left:{x0 + 170}px;top:{y - 30}px;width:840px;z-index:4;background:#fff;'
                 f'border:4px solid {f["ink"]};border-top:16px solid {ln["col"]};border-radius:26px;padding:18px 28px 22px;box-shadow:0 8px 0 {f["ink"]}">'
                 f'<div class="S" style="font-size:56px;line-height:1.08;text-align:left;color:{f["ink"]}">{K.pills(ln["fix"], f)}</div></div>')
    body += f'<div class="S" style="position:absolute;left:{x0 + 60}px;top:{H - 92}px;width:960px;font-size:24px;opacity:.6">{spec["src"]}</div>'
    for i in range(n):
        body += counter(i + 1, n + 1, W * i + W - 120)
        if i in (0, n - 1):
            body += K.stamp(b, W * i + (W - 230 if i == 0 else W - 230), 60 if i == n - 1 else H - 330, 150, 12)
    files = shot_pano(r, b, field, body, n, out_dir)
    # closing "Do this" slide
    last = out_dir / f"{n + 1:02d}.jpg"
    r.shot(C.page(b, spec["do_field"], do_card(b, spec["do_field"], spec["do"], spec["save"]) + counter(n + 1, n + 1), W, H), W, H, last)
    return files + [last]


# ----------------------------------------------------------------------------------------------- travelling icon
def travel(r, spec, out_dir):
    b, field = spec["brand"], spec["field"]
    n = len(spec["beats"])
    f = f_(b, field)
    ink = f["ink"]
    # trail: gentle wave across all slides with one loop on slide 3
    pts = []
    loop_c = (W * 2 + 540, 640)
    for x in range(0, n * W + 1, 12):
        y = 860 + 70 * math.sin(x / 520)
        if loop_c[0] - 260 <= x <= loop_c[0] + 260:
            pass
        pts.append((x, y))
    d = "M " + " L ".join(f"{x:.0f},{y:.0f}" for x, y in pts if not (loop_c[0] - 2 < x < loop_c[0] + 2))
    # loop: a circle drawn on the trail on slide 3
    lx, ly = loop_c
    loop = (f'<circle cx="{lx}" cy="{ly + 40}" r="190" fill="none" stroke="{K.ACCENT[b]}" stroke-width="14" stroke-dasharray="2 22" stroke-linecap="round"/>')
    body = (f'<svg style="position:absolute;left:0;top:0;z-index:2" width="{n * W}" height="{H}" viewBox="0 0 {n * W} {H}">'
            f'<path d="{d}" fill="none" stroke="{K.ACCENT[b]}" stroke-width="14" stroke-dasharray="2 22" stroke-linecap="round"/>{loop}</svg>')
    # the traveller: the page object, a little further along on every slide
    obj = spec.get("obj", "phone")
    for i in range(n):
        x = W * i + 120 + 150 * (i % 3)
        y = 860 + 70 * math.sin((x + 120) / 520) - 150
        if i == 2:
            x, y = lx - 85, ly - 90
        body += K.obj(obj, int(x), int(y), 230 if obj != "phone" else 170, -8 + 6 * (i % 2), z=5)
    for i, bt in enumerate(spec["beats"]):
        top = 150 if i != 2 else 120
        body += hand(b, bt.get("label", ""), W * i + 100, top - 10, 880, 58) if bt.get("label") else ""
        body += txt(b, bt.get("f", field), bt["text"], W * i + 80, top + 70, W - 160, bt.get("size", 92))
        if bt.get("sub"):
            body += hand(b, bt["sub"], W * i + 120, 1080, 840, 56)
        body += counter(i + 1, n + 1, W * i + W - 120)
    body += K.stamp(b, W - 230, H - 300, 150, 12)
    body += hand(b, "follow the trail →", 300, H - 110, 700, 54)
    files = shot_pano(r, b, field, body, n, out_dir)
    last = out_dir / f"{n + 1:02d}.jpg"
    r.shot(C.page(b, spec["do_field"], do_card(b, spec["do_field"], spec["do"], spec["save"]) + counter(n + 1, n + 1), W, H), W, H, last)
    return files + [last]


# ----------------------------------------------------------------------------------------------- scenic trail (illustrated)
def trail(r, spec, out_dir):
    """Travelling carousel on an illustrated landscape: sky, sun, clouds, layered hills, a winding dotted path,
    a milestone sign on every slide, and the traveller moving along the path."""
    b, field = spec["brand"], spec["field"]
    n = len(spec["beats"])
    f = f_(b, field)
    ink = f["ink"]
    pal = spec.get("palette", dict(sky1="#FFF4E6", sky2="#FFDCE8", sun="#FFE59A", h1="#FFE3CC", h2="#FFC9D9", h3="#FFB59E", path="#D9497A"))
    Wt = n * W

    def hill(base, amp, per, phase, col, op=1):
        pts = [f"0,{H}"] + [f"{x},{base + amp * math.sin(x / per + phase):.0f}" for x in range(0, Wt + 1, 20)] + [f"{Wt},{H}"]
        return f'<polygon points="{" ".join(pts)}" fill="{col}" opacity="{op}"/>'
    clouds = "".join(f'<g opacity=".9"><ellipse cx="{cx}" cy="{cy}" rx="120" ry="44" fill="#fff"/><ellipse cx="{cx + 70}" cy="{cy - 24}" rx="80" ry="40" fill="#fff"/>'
                     f'<ellipse cx="{cx - 80}" cy="{cy + 6}" rx="70" ry="30" fill="#fff"/></g>'
                     for cx, cy in [(W * i + 260 + 300 * (i % 2), 560 + 50 * ((i + 1) % 2)) for i in range(n)])
    path_y = lambda x: 1040 + 55 * math.sin(x / 430 + 0.6)
    trail_d = "M " + " L ".join(f"{x},{path_y(x):.0f}" for x in range(0, Wt + 1, 12))
    svg = (f'<svg style="position:absolute;left:0;top:0;z-index:1" width="{Wt}" height="{H}" viewBox="0 0 {Wt} {H}">'
           f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{pal["sky1"]}"/>'
           f'<stop offset="1" stop-color="{pal["sky2"]}"/></linearGradient></defs>'
           f'<rect width="{Wt}" height="{H}" fill="url(#sky)"/>'
           f'<circle cx="{W - 150}" cy="660" r="95" fill="{pal["sun"]}"/>{clouds}'
           + hill(800, 40, 520, 0.3, pal["h1"]) + hill(900, 50, 380, 1.7, pal["h2"]) + hill(1010, 36, 300, 0.9, pal["h3"])
           + f'<path d="{trail_d}" fill="none" stroke="{pal["path"]}" stroke-width="13" stroke-dasharray="2 24" stroke-linecap="round"/></svg>')
    body = svg
    # milestone signs + the traveller
    for i, bt in enumerate(spec["beats"]):
        if bt.get("sign"):
            sx = W * i + 760
            sy = path_y(sx)
            body += (f'<div style="position:absolute;left:{sx - 6}px;top:{sy - 230:.0f}px;width:12px;height:230px;background:{ink};border-radius:6px;z-index:3"></div>'
                     f'<div style="position:absolute;left:{sx - 110}px;top:{sy - 330:.0f}px;width:220px;z-index:4;background:#fff;border:5px solid {ink};'
                     f'border-radius:26px;box-shadow:0 8px 0 {ink};padding:10px 0 14px;text-align:center;transform:rotate({-4 + 4 * (i % 3)}deg)">'
                     f'<div style="font-family:\'Noto Color Emoji\';font-size:86px;line-height:1">{bt["sign"]}</div></div>')
        tx = W * i + (140 if i == 0 else 300)
        body += K.obj(spec.get("obj", "shoe"), int(tx), int(path_y(tx + 120) - 210), 250, -6 + 5 * (i % 2), z=5)
        top = 120
        if bt.get("label"):
            body += hand(b, bt["label"], W * i + 100, top, 880, 60)
        body += txt(b, field, bt["text"], W * i + 70, top + 80, W - 140, bt.get("size", 96))
        body += counter(i + 1, n + 1, W * i + W - 120)
    body += f'<div style="position:absolute;inset:0;z-index:6">{K.stamp(b, 50, H - 230, 150, -12)}</div>'
    body += hand(b, spec.get("cta", "follow the path →"), 260, H - 150, 760, 60, -2)
    files = shot_pano(r, b, field, body, n, out_dir)
    last = out_dir / f"{n + 1:02d}.jpg"
    r.shot(C.page(b, spec["do_field"], do_card(b, spec["do_field"], spec["do"], spec["save"]) + counter(n + 1, n + 1), W, H), W, H, last)
    return files + [last]


# ----------------------------------------------------------------------------------------------- hold the dots & slide
def jar_svg(b, level, ink, fill, w=430, h=560):
    lv = max(0.0, min(1.0, level))
    fh = (h - 120) * lv
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<defs><clipPath id="jc"><rect x="40" y="90" width="{w - 80}" height="{h - 120}" rx="60"/></clipPath></defs>'
            f'<rect x="40" y="{90 + (h - 120) - fh:.0f}" width="{w - 80}" height="{fh:.0f}" fill="{fill}" clip-path="url(#jc)"/>'
            + "".join(f'<circle cx="{80 + (k * 53) % (w - 160)}" cy="{h - 60 - (k * 37) % max(1, fh - 20):.0f}" r="20" fill="#fff" opacity=".35" clip-path="url(#jc)"/>'
                      for k in range(int(18 * lv)))
            + f'<rect x="40" y="90" width="{w - 80}" height="{h - 120}" rx="60" fill="none" stroke="{ink}" stroke-width="8"/>'
            f'<rect x="90" y="40" width="{w - 180}" height="60" rx="18" fill="{K.STAMP_BG[b]}" stroke="{ink}" stroke-width="8"/></svg>')


def hold(r, spec, out_dir):
    b, field = spec["brand"], spec["field"]
    f = f_(b, field)
    frames = spec["frames"]                  # list of (label, value, sub)
    n = 1 + len(frames) + 1
    files = []
    cov = (txt(b, field, spec["hook"], 60, 200, W - 120, 112)
           + hand(b, "swipe and watch it grow →", 120, 980, 840, 74, -3)

           + K.obj("piggy", 640, 640, 380, -6) + K.stamp(b, 60, H - 260, 160, -12) + counter(1, n))
    p = out_dir / "01.jpg"
    files.append(r.shot(C.page(b, field, cov, W, H), W, H, p))
    vmax = max(v for _, v, _ in frames)
    for i, (label, v, sub) in enumerate(frames, 2):
        body = (f'<div class="S" style="position:absolute;left:0;right:0;top:120px;font-size:84px;color:{f["ink"]}">{label}</div>'
                f'<div class="S" style="position:absolute;left:0;right:0;top:240px;font-size:150px;color:{f["ink"]}">'
                f'<span class="pill" style="background:{f["p1"]}">${v:,.0f}</span></div>'
                f'<div style="position:absolute;left:{(W - 430) // 2}px;top:480px;z-index:3">{jar_svg(b, v / vmax, f["ink"], K.ACCENT[b])}</div>'
                + hand(b, sub, 120, 1090, 840, 58, -2)
                + hand(b, "keep swiping…" if i < n - 1 else "👀", 300, 1200, 480, 50, -3)
                + counter(i, n))
        files.append(r.shot(C.page(b, field, body, W, H), W, H, out_dir / f"{i:02d}.jpg"))
    files.append(r.shot(C.page(b, spec["do_field"], do_card(b, spec["do_field"], spec["do"], spec["save"]) + counter(n, n), W, H),
                        W, H, out_dir / f"{n:02d}.jpg"))
    return files


# ----------------------------------------------------------------------------------------------- swipe to reveal
def reveal(r, spec, out_dir):
    b, field = spec["brand"], spec["field"]
    f = f_(b, field)
    levels = spec.get("levels", [46, 16])
    n = 1 + len(levels) + 1 + 1            # cover, blurred steps (with hanging lines), the answer, do
    files = []
    cov = (txt(b, field, spec["hook"], 60, 180, W - 120, 100)
           + hand(b, spec["guess"], 120, 820, 840, 66, -3)
           + hand(b, "hold the dots ↓ and slide to reveal →", 100, 1000, 880, 60, -2)
           + K.obj("ok", 740, 560, 280, 8) + K.stamp(b, 60, H - 260, 160, -12) + counter(1, n))
    files.append(r.shot(C.page(b, field, cov, W, H), W, H, out_dir / "01.jpg"))
    ans_body = (hand(b, spec["ans_label"], 120, 240, 840, 70, -3)
                + f'<div class="S" style="position:absolute;left:0;right:0;top:400px;font-size:230px;color:{f["ink"]}">'
                  f'<span class="pill" style="background:{f["p1"]}">{spec["answer"]}</span></div>'
                + txt(b, field, spec["ans_sub"], 100, 760, W - 200, 70)
                + K.obj("piggy" if b != "littlefold" else "shoe", 380, 1010, 300, -6))
    clear = out_dir / "_clear.jpg"
    r.shot(C.page(b, field, ans_body, W, H), W, H, clear)
    im = Image.open(clear)
    hang = spec.get("hang", [])
    for k, px in enumerate(levels, 2):
        small = im.resize((max(1, W // px), max(1, H // px)), Image.BILINEAR)
        bp = out_dir / f"_b{k}.jpg"
        small.resize((W, H), Image.NEAREST).save(bp, quality=92)
        over = (f'<img src="{K.uri(bp)}" style="position:absolute;inset:0;width:{W}px;height:{H}px;z-index:1">'
                f'<div style="position:absolute;left:70px;right:70px;top:880px;z-index:5;background:#fff;border:5px solid {f["ink"]};'
                f'border-radius:40px;box-shadow:0 14px 0 {f["ink"]};padding:34px 40px;font-size:62px;line-height:1.08;color:{f["ink"]}">'
                f'{K.dual(hang[k - 2] if k - 2 < len(hang) else "keep sliding…", f)}</div>' + counter(k, n))
        r.shot(C.page(b, field, over, W, H), W, H, out_dir / f"{k:02d}.jpg")
        bp.unlink()
        files.append(out_dir / f"{k:02d}.jpg")
    k = 2 + len(levels)
    im.save(out_dir / f"{k:02d}.jpg", quality=92, subsampling=0)
    files.append(out_dir / f"{k:02d}.jpg")
    clear.unlink()
    files.append(r.shot(C.page(b, field, do_card(b, field, spec["do"], spec["save"]) + counter(n, n), W, H), W, H, out_dir / f"{n:02d}.jpg"))
    # fix the cover counter total is n; blurred slides carry none on purpose (they are frames)
    return files


BUILD = {"follow": follow, "travel": travel, "trail": trail, "hold": hold, "reveal": reveal}


def build(ids):
    import v5_formats as V
    r = C.R()
    try:
        for pid in ids:
            spec = V.FORMATS[pid]
            d = REPO / "media" / pid
            d.mkdir(exist_ok=True)
            for old in d.glob("*.jpg"):
                old.unlink()
            files = BUILD[spec["kind"]](r, spec, d)
            assert len(files) <= 10, (pid, len(files))
            print(pid, len(files), "slides", flush=True)
    finally:
        r.close()


if __name__ == "__main__":
    build(sys.argv[1:])

#!/usr/bin/env python3
"""Interactive carousel formats (Oct 18, Dharma's references):
  follow  - "Follow the line": pick a problem, follow its coloured line across slides to the fix (one panorama, sliced)
  travel  - "Travelling icon": an object travels a dotted trail (with a loop) through the words across slides
  hold    - "Hold the dots & slide": near-identical frames that animate when the viewer holds and slides (a flipbook)
  reveal  - "Swipe to reveal": the answer starts pixelated and sharpens slide by slide
  climb   - "Staircase": one staircase across every slide; each swipe is one step up to the summit (Oct 19)
  streak  - "Streak calendar": the same month on every slide, filling in as you hold and slide (Oct 19)
  split   - "Swipe to fix": a handle line moves down one row per swipe; above it the AFTER, below the BEFORE (Oct 19)
  roadmap - "Road trip": a top-down map with one winding road, numbered stops and the car moving along (Oct 19)

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


NOTE_SIZE = {"fullyfunded": 48, "littlefold": 50, "hourback": 52, "lockedhour": 56}   # per serif width


def stack(b, field, bt, x, y, w, size=90, z=4):
    """Label (hand) + headline (serif, pills) + optional quieter note, stacked in normal flow so nothing overlaps."""
    f = f_(b, field)
    out = f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;z-index:{z}">'
    if bt.get("label"):
        out += f'<div class="hand" style="font-size:{bt.get("lsize", 60)}px;transform:rotate(-3deg);margin-bottom:24px">{bt["label"]}</div>'
    out += f'<div style="font-size:{bt.get("size", size)}px;line-height:1.04;color:{f["ink"]}">{K.dual(bt["text"], f, cls="S")}</div>'
    if bt.get("note"):
        out += (f'<div class="S" style="margin-top:22px;font-size:{bt.get("nsize", NOTE_SIZE.get(b, 54))}px;line-height:1.12;color:{f["ink"]};opacity:.86">'
                f'{K.pills(bt["note"], f)}</div>')
    return out + '</div>'


def counter(i, n, x=W - 120, y=40):
    return f'<div class="S" style="position:absolute;left:{x}px;top:{y}px;font-size:26px;opacity:.45">{i}/{n}</div>'


def do_card(b, field, text, save, x=70, y=380, size=76, why=None):
    """The closing "Do this" card. Optional `why`: one quiet line (the mechanism) under the card."""
    f = f_(b, field)
    ink = f["ink"]
    return (hand(b, "Do this:", 0, y - 200, W, 120, -4)
            + f'<div style="position:absolute;left:{x}px;top:{y}px;width:{W - 2 * x}px;background:#fff;border:5px solid {ink};border-radius:44px;'
            f'box-shadow:0 16px 0 {ink};padding:56px 52px;z-index:4;font-size:{size}px;line-height:1.08;color:{ink}">{K.dual(text, f)}'
            + (f'<div class="S" style="margin-top:26px;font-size:{int(size * .62)}px;line-height:1.1;opacity:.8;color:{ink}">{K.pills(why, f)}</div>' if why else "")
            + '</div>'
            + hand(b, save, 120, y + 640, W - 240, 56, -3)
            + K.obj("point", -70, y + 470, 330, -10) + K.stamp(b, W - 250, H - 260, 170, 12))


def shot_pano(r, b, field, body, n, out_dir):
    """One continuous (n*W) x H picture, shot slice by slice (the same canvas shifted left by i*W each time,
    so a busy machine never has to screenshot a 10k-pixel page). The joined panorama is kept for pan_reel.py."""
    files = []
    for i in range(n):
        p = out_dir / f"{i + 1:02d}.jpg"
        r.shot(C.page(b, field, f'<div style="position:absolute;left:{-i * W}px;top:0;width:{n * W}px;height:{H}px">{body}</div>', W, H),
               W, H, p)
        files.append(p)
    im = Image.new("RGB", (n * W, H))
    for i, p in enumerate(files):
        im.paste(Image.open(p), (i * W, 0))
    keep = Path("/home/claude/rq/pano")
    keep.mkdir(parents=True, exist_ok=True)
    im.save(keep / f"{out_dir.name}.jpg", quality=92)
    return files


def do_slide(r, spec, out_dir, k, n, field=None):
    b = spec["brand"]
    fld = field or spec["do_field"]
    p = out_dir / f"{k:02d}.jpg"
    r.shot(C.page(b, fld, do_card(b, fld, spec["do"], spec["save"], size=spec.get("do_size", 76), why=spec.get("do_why"))
                  + counter(k, n), W, H), W, H, p)
    return p


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
        lanes = [690, 880, 1070] if spec.get("mids") else [430, 680, 930]   # teaching text needs the top half free
        ys = [y0] + [lanes[(k + j) % 3] + 50 * (j % 2) for j in range(1, n - 1)] + [y1]
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
    mids = spec.get("mids")                # optional: dict(label, text, size) per middle slide (teaching while you follow)
    for j in range(1, n - 1):
        if mids:
            m = mids[j - 1]
            body += hand(b, m.get("label", "keep following…"), W * j + 140, 70, 800, 60, -4)
            body += txt(b, field, m["text"], W * j + 70, 165, W - 140, m.get("size", 70))
        else:
            body += hand(b, spec["notes"][j - 1], W * j + 140, 150, 800, 72, -4)
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
    return files + [do_slide(r, spec, out_dir, n + 1, n + 1)]


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
        body += stack(b, bt.get("f", field), bt, W * i + 80, top - 10, W - 160, 92)
        if bt.get("sub"):
            body += hand(b, bt["sub"], W * i + 120, 1080, 840, 56)
        body += counter(i + 1, n + 1, W * i + W - 120)
    body += K.stamp(b, W - 230, H - 300, 150, 12)
    body += hand(b, "follow the trail →", 300, H - 110, 700, 54)
    files = shot_pano(r, b, field, body, n, out_dir)
    return files + [do_slide(r, spec, out_dir, n + 1, n + 1)]


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
        ob = spec.get("obj", "shoe")
        if ob == "phone":                   # the phone is tall: smaller, and standing on the path
            body += K.obj(ob, int(tx + 30), int(path_y(tx + 120) - 300), 165, -6 + 5 * (i % 2), z=5)
        else:
            body += K.obj(ob, int(tx), int(path_y(tx + 120) - 210), 250, -6 + 5 * (i % 2), z=5)
        body += stack(b, field, bt, W * i + 70, 110, W - 140, 96)
        body += counter(i + 1, n + 1, W * i + W - 120)
    body += f'<div style="position:absolute;inset:0;z-index:6">{K.stamp(b, 50, H - 230, 150, -12)}</div>'
    body += hand(b, spec.get("cta", "follow the path →"), 260, H - 150, 760, 60, -2)
    files = shot_pano(r, b, field, body, n, out_dir)
    return files + [do_slide(r, spec, out_dir, n + 1, n + 1)]


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
           + hand(b, spec.get("cta", "swipe and watch it grow →"), 60 if spec.get("cover_obj", "piggy") != "piggy" else 120,
                  880 if spec.get("cover_obj", "piggy") != "piggy" else 980, 700 if spec.get("cover_obj", "piggy") != "piggy" else 840,
                  64 if spec.get("cover_obj", "piggy") != "piggy" else 74, -3)
           + (K.obj("piggy", 640, 640, 380, -6) if spec.get("cover_obj", "piggy") == "piggy" else
              K.obj(spec["cover_obj"], 760, 560, 250, -6))
           + K.stamp(b, 60, H - 260, 160, -12) + counter(1, n))
    p = out_dir / "01.jpg"
    files.append(r.shot(C.page(b, field, cov, W, H), W, H, p))
    vmax = spec.get("vmax") or max(fr[1] for fr in frames)
    pre, post = spec.get("pre", "$"), spec.get("post", "")
    for i, fr in enumerate(frames, 2):
        label, v, sub = fr[:3]
        note = fr[3] if len(fr) > 3 else None   # optional: one serif line of teaching under the hand-written sub
        body = (f'<div class="S" style="position:absolute;left:0;right:0;top:120px;font-size:84px;color:{f["ink"]}">{label}</div>'
                f'<div class="S" style="position:absolute;left:0;right:0;top:240px;font-size:150px;color:{f["ink"]}">'
                f'<span class="pill" style="background:{f["p1"]}">{spec["show"][i - 2] if spec.get("show") else f"{pre}{v:,.{spec.get('dec', 0)}f}{post}"}</span></div>'
                f'<div style="position:absolute;left:{(W - 430) // 2}px;top:{450 if note else 480}px;z-index:3">{jar_svg(b, v / vmax, f["ink"], K.ACCENT[b])}</div>'
                + hand(b, sub, 100, 1040 if note else 1090, 880, 58, -2)
                + (txt(b, field, note, 80, 1135, W - 160, 50) if note else
                   hand(b, "keep swiping…" if i < n - 1 else "👀", 300, 1200, 480, 50, -3))
                + counter(i, n))
        files.append(r.shot(C.page(b, field, body, W, H), W, H, out_dir / f"{i:02d}.jpg"))
    files.append(do_slide(r, spec, out_dir, n, n))
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
    files.append(do_slide(r, spec, out_dir, n, n, field=field))
    # fix the cover counter total is n; blurred slides carry none on purpose (they are frames)
    return files


# ----------------------------------------------------------------------------------------------- staircase climb (Oct 19, new)
def climb(r, spec, out_dir):
    """One staircase across every slide: each swipe is one step up, with its label painted on the riser,
    and the traveller standing on the step it has reached. Summit flag on the last step."""
    b, field = spec["brand"], spec["field"]
    n = len(spec["beats"])
    f = f_(b, field)
    ink, acc = f["ink"], K.ACCENT[b]
    Wt = n * W
    y_lo, y_hi = spec.get("y_lo", 1235), spec.get("y_hi", 780)
    ys = [y_lo - (y_lo - y_hi) * i / max(1, n - 1) for i in range(n)]
    rise_x = [0] + [W * i + 90 for i in range(1, n)]
    pts = [(0, H)]
    for i in range(n):
        pts += [(rise_x[i], ys[i - 1] if i else ys[0]), (rise_x[i], ys[i])]
    pts += [(Wt, ys[-1]), (Wt, H)]
    poly = " ".join(f"{x:.0f},{y:.0f}" for x, y in pts)
    top = " ".join(f"{x:.0f},{y:.0f}" for x, y in pts[1:-1])
    body = (f'<div style="position:absolute;inset:0;background-image:radial-gradient({ink}22 2.2px,transparent 2.6px);'
            f'background-size:44px 44px;opacity:.55"></div>'
            f'<svg style="position:absolute;left:0;top:0;z-index:2" width="{Wt}" height="{H}" viewBox="0 0 {Wt} {H}">'
            f'<polygon points="{poly}" fill="{f["p1"]}"/>'
            + "".join(f'<rect x="{rise_x[i]}" y="{ys[i]:.0f}" width="{(rise_x[i + 1] if i + 1 < n else Wt) - rise_x[i]}" height="26" fill="#fff" opacity=".55"/>'
                      for i in range(n))
            + f'<polyline points="{top}" fill="none" stroke="{ink}" stroke-width="9" stroke-linejoin="round"/>'
            # footprints: a dotted climb line just above the treads
            + f'<polyline points="{" ".join(f"{x:.0f},{y - 46:.0f}" for x, y in pts[1:-1])}" fill="none" stroke="{acc}" stroke-width="11" '
            f'stroke-dasharray="2 22" stroke-linecap="round" opacity=".9"/></svg>')
    obj = spec.get("obj", "shoe")
    for i, bt in enumerate(spec["beats"]):
        x0 = W * i
        if bt.get("step"):                      # label painted on the riser face
            body += (f'<div class="hand" style="position:absolute;left:{rise_x[i] + 40}px;top:{ys[i] + 44:.0f}px;width:{W - 200}px;'
                     f'font-size:{bt.get("ssize", 70)}px;color:{ink};opacity:.82;text-align:left;z-index:3;transform:rotate(-2deg)">{bt["step"]}</div>')
        ox = x0 + (150 if i == 0 else 560)
        if obj == "phone":
            body += K.obj(obj, int(ox), int(ys[i] - 228), 115, -4 + 6 * (i % 2), z=5)
        elif obj.startswith("emoji:"):
            body += (f'<div style="position:absolute;left:{ox}px;top:{ys[i] - 175:.0f}px;z-index:5;font-family:\'Noto Color Emoji\';font-size:150px;'
                     f'line-height:1;filter:drop-shadow(0 12px 12px rgba(0,0,0,.16))">{obj[6:]}</div>')
        else:                                    # tall cut-outs get narrower so their base sits on the tread
            ow = {"hourglass": 150, "clock": 190, "cup": 190}.get(obj, 210)
            oh = {"hourglass": 250, "clock": 200, "cup": 190}.get(obj, 205)
            body += K.obj(obj, int(ox), int(ys[i] - oh), ow, -6 + 6 * (i % 2), z=5)
        if bt.get("sign"):
            body += (f'<div style="position:absolute;left:{x0 + 820}px;top:{ys[i] - 150:.0f}px;z-index:4;font-family:\'Noto Color Emoji\';font-size:96px;'
                     f'line-height:1;transform:rotate({-6 + 6 * (i % 3)}deg);filter:drop-shadow(0 8px 10px rgba(0,0,0,.14))">{bt["sign"]}</div>')
        body += stack(b, field, bt, x0 + 70, 100, W - 140, 92)
        body += counter(i + 1, n + 1, x0 + W - 120)
    body += f'<div style="position:absolute;inset:0;z-index:6">{K.stamp(b, W - 220, H - 230, 150, 12)}</div>'
    body += hand(b, spec.get("cta", "climb it, one swipe at a time →"), 330, H - 115, 560, 54, -2, z=6)
    files = shot_pano(r, b, field, body, n, out_dir)
    return files + [do_slide(r, spec, out_dir, n + 1, n + 1)]


# ----------------------------------------------------------------------------------------------- streak calendar (Oct 19, new)
def cal_svg(b, f, days, upto, missed=(), marks=None, cols=7, cell=104, gap=12, dows="MTWTFSS"):
    ink, acc = f["ink"], K.ACCENT[b]
    rows = math.ceil(days / cols)
    w, h = cols * cell + (cols - 1) * gap, 40 + rows * (cell + gap)
    out = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">']
    for c, d in enumerate(dows[:cols]):
        out.append(f'<text x="{c * (cell + gap) + cell / 2}" y="26" text-anchor="middle" font-family="Caveat Brush" font-size="32" fill="{ink}" opacity=".6">{d}</text>')
    marks = marks or {}
    for d in range(1, days + 1):
        r_, c = divmod(d - 1, cols)
        x, y = c * (cell + gap), 40 + r_ * (cell + gap)
        cx, cy = x + cell / 2, y + cell / 2
        if d <= upto and d not in missed:
            out.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="24" fill="{acc}"/>')
            if d in marks:
                out.append(f'<text x="{cx}" y="{cy + 20}" text-anchor="middle" font-family="Noto Color Emoji" font-size="56">{marks[d]}</text>')
            else:
                out.append(f'<path d="M{cx - 22},{cy + 2} l15,16 l30,-34" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>')
            if d == upto:
                out.append(f'<rect x="{x - 7}" y="{y - 7}" width="{cell + 14}" height="{cell + 14}" rx="30" fill="none" stroke="{ink}" stroke-width="6"/>')
        elif d <= upto:                          # a missed day: dashed, honest, not the end
            out.append(f'<rect x="{x + 4}" y="{y + 4}" width="{cell - 8}" height="{cell - 8}" rx="22" fill="#fff" fill-opacity=".5" stroke="{ink}" '
                       f'stroke-width="5" stroke-dasharray="10 9"/>'
                       f'<text x="{cx}" y="{cy + 14}" text-anchor="middle" font-family="Caveat Brush" font-size="44" fill="{ink}" opacity=".7">missed</text>'
                       if cell >= 120 else
                       f'<rect x="{x + 4}" y="{y + 4}" width="{cell - 8}" height="{cell - 8}" rx="22" fill="#fff" fill-opacity=".5" stroke="{ink}" '
                       f'stroke-width="5" stroke-dasharray="10 9"/>'
                       f'<text x="{cx}" y="{cy + 16}" text-anchor="middle" font-family="Caveat Brush" font-size="46" fill="{ink}" opacity=".75">✗</text>')
        else:
            out.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="24" fill="#fff" fill-opacity=".62" stroke="{ink}" stroke-opacity=".18" stroke-width="3"/>'
                       f'<text x="{cx}" y="{cy + 12}" text-anchor="middle" font-family="Fraunces" font-size="32" fill="{ink}" opacity=".45">{d}</text>')
    out.append("</svg>")
    return "".join(out), w, h


def streak(r, spec, out_dir):
    """Hold-and-slide streak calendar: the same month on every slide, filling in as you swipe
    (honest misses included), with the lesson for that stretch above it."""
    b, field = spec["brand"], spec["field"]
    f = f_(b, field)
    ink = f["ink"]
    days = spec.get("days", 30)
    frames = spec["frames"]
    n = 1 + len(frames) + 1
    files = []

    def calendar(fr, top):
        svg, w, h = cal_svg(b, f, days, fr.get("upto", 0), fr.get("missed", ()), spec.get("marks"))
        return f'<div style="position:absolute;left:{(W - w) // 2}px;top:{top}px;z-index:3">{svg}</div>'
    cov = (txt(b, field, spec["hook"], 60, 110, W - 120, spec.get("hook_size", 100))
           + calendar(dict(upto=0), 560)
           + hand(b, spec.get("cta", "hold the dots and slide: watch it fill →"), 60, 1190, 800, 56, -3)
           + K.stamp(b, W - 200, H - 210, 150, 12) + counter(1, n))
    files.append(r.shot(C.page(b, field, cov, W, H), W, H, out_dir / "01.jpg"))
    for i, fr in enumerate(frames, 2):
        upto = fr.get("upto", 0)
        done = sum(1 for d in range(1, upto + 1) if d not in fr.get("missed", ()))
        run = 0
        for d in range(upto, 0, -1):
            if d in fr.get("missed", ()):
                break
            run += 1
        pill = fr.get("pill") or (f"🔥 day 1 · first tick" if upto == 1 else f"🔥 {run}-day streak · {done} of {upto} days")
        body = (stack(b, field, dict(label=fr.get("label"), text=fr["text"], size=fr.get("size", 84)), 70, 70, W - 140, 84)
                + f'<div class="S" style="position:absolute;left:0;right:0;top:{fr.get("pill_y", 430)}px;font-size:44px;color:{ink};z-index:4">'
                  f'<span class="pill" style="background:{f["p2"]};padding:.08em .4em">{pill}</span></div>'
                + calendar(fr, 515)
                + (txt(b, field, fr["note"], 70, 1150, W - 140, fr.get("nsize", 50)) if fr.get("note") else "")
                + counter(i, n))
        files.append(r.shot(C.page(b, field, body, W, H), W, H, out_dir / f"{i:02d}.jpg"))
    files.append(do_slide(r, spec, out_dir, n, n))
    return files


# ----------------------------------------------------------------------------------------------- before/after wipe (Oct 19, new)
def split(r, spec, out_dir):
    """Swipe to fix: the same list on every slide, a handle line moving down one row per swipe.
    Above the line: the AFTER version (with its why). Below: the BEFORE version still waiting."""
    b, field = spec["brand"], spec["field"]
    f = f_(b, field)
    ink, acc = f["ink"], K.ACCENT[b]
    rows = spec["rows"]
    R = len(rows)
    n = 1 + R + 1
    top0, avail, gap = spec.get("rows_top", 290), spec.get("rows_h", 960), 16
    rh = (avail - (R - 1) * gap) / R
    fa, fw, fb = spec.get("after_size", 50 if R <= 4 else 44), spec.get("why_size", 34 if R <= 4 else 31), spec.get("before_size", 46 if R <= 4 else 42)
    files = []

    def scene(k, cover=False):
        out = txt(b, field, spec["hook"], 60, 60, W - 120, spec.get("hook_size", 78))
        for j, rw in enumerate(rows):
            y = top0 + j * (rh + gap)
            if j < k:     # fixed
                out += (f'<div style="position:absolute;left:60px;top:{y:.0f}px;width:{W - 120}px;height:{rh:.0f}px;z-index:4;background:#fff;'
                        f'border:4px solid {ink};border-left:20px solid {acc};border-radius:26px;box-shadow:0 8px 0 {ink};padding:14px 26px 0 104px">'
                        f'<div style="position:absolute;left:24px;top:{rh / 2 - 34:.0f}px;width:64px;height:64px;border-radius:50%;background:{acc};'
                        f'display:flex;align-items:center;justify-content:center"><svg width="40" height="40" viewBox="0 0 40 40"><path d="M7,21 l9,9 l17,-20" '
                        f'fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
                        f'<div class="S" style="text-align:left;font-size:{fa}px;line-height:1.04;color:{ink}">{K.pills(rw["after"], f)}</div>'
                        f'<div class="S" style="text-align:left;font-size:{fw}px;line-height:1.1;color:{ink};opacity:.78;margin-top:8px">{K.pills(rw["why"], f)}</div></div>')
            else:         # still the old way
                out += (f'<div style="position:absolute;left:60px;top:{y:.0f}px;width:{W - 120}px;height:{rh:.0f}px;z-index:3;'
                        f'background:{f["p2"]};border:4px dashed {ink}55;border-radius:26px;padding:0 26px 0 104px;display:flex;align-items:center">'
                        f'<div style="position:absolute;left:30px;top:{rh / 2 - 30:.0f}px;font-family:\'Caveat Brush\';font-size:56px;color:{ink};opacity:.5">✗</div>'
                        f'<div class="S" style="text-align:left;font-size:{fb}px;line-height:1.06;color:{ink};opacity:.62">{K.pills(rw["before"], f)}</div></div>')
        # the handle line
        ly = top0 - 34 if k == 0 else top0 + k * (rh + gap) - gap / 2
        lab = spec.get("cta", "swipe: fix one more ↓") if k < R else spec.get("done", "all fixed ✓")
        out += (f'<div style="position:absolute;left:0;width:{W}px;top:{ly - 4:.0f}px;height:8px;background:{acc};z-index:6;'
                f'box-shadow:0 0 0 3px #fff8"></div>'
                f'<div style="position:absolute;left:{W - 150}px;top:{ly - 44:.0f}px;width:88px;height:88px;border-radius:50%;background:#fff;'
                f'border:6px solid {acc};z-index:7;display:flex;align-items:center;justify-content:center;font-family:\'Caveat Brush\';'
                f'font-size:56px;color:{acc}">{"↓" if k < R else "✓"}</div>'
                + (hand(b, lab, 60, top0 + avail + 18, W - 120, 50, -2, z=7) if k in (0, R) else ""))
        return out
    cov = scene(0, cover=True) + K.stamp(b, W - 190, 22, 130, 12) + counter(1, n)
    files.append(r.shot(C.page(b, field, cov, W, H), W, H, out_dir / "01.jpg"))
    for k in range(1, R + 1):
        files.append(r.shot(C.page(b, field, scene(k) + counter(k + 1, n), W, H), W, H, out_dir / f"{k + 1:02d}.jpg"))
    files.append(do_slide(r, spec, out_dir, n, n))
    return files


# ----------------------------------------------------------------------------------------------- road-trip map (Oct 19, new)
def roadmap(r, spec, out_dir):
    """Top-down road-trip map across every slide: one winding road, a numbered pin per stop, the car a little
    further along on each slide, a route strip showing which stop you're at, and the flag at the destination."""
    b, field = spec["brand"], spec["field"]
    n = len(spec["beats"])
    f = f_(b, field)
    ink, acc = f["ink"], K.ACCENT[b]
    Wt = n * W
    road_y = lambda x: 985 + 120 * math.sin(x / 470 + 0.4)
    d = "M " + " L ".join(f"{x},{road_y(x):.0f}" for x in range(-20, Wt + 21, 10))
    blobs = ""
    for i in range(n):                          # parks + lakes: quiet map texture, never under the words
        bx = W * i
        blobs += (f'<ellipse cx="{bx + 180 + 90 * (i % 2)}" cy="{1250 - 20 * (i % 3)}" rx="150" ry="70" fill="{f["p1"]}" opacity=".55"/>'
                  f'<ellipse cx="{bx + 860 - 60 * (i % 2)}" cy="{760 + 20 * (i % 2)}" rx="120" ry="52" fill="{f["p2"]}" opacity=".8"/>')
    svg = (f'<svg style="position:absolute;left:0;top:0;z-index:1" width="{Wt}" height="{H}" viewBox="0 0 {Wt} {H}">'
           f'<defs><pattern id="g" width="90" height="90" patternUnits="userSpaceOnUse"><path d="M90 0 L0 0 0 90" fill="none" stroke="{ink}" '
           f'stroke-opacity=".07" stroke-width="2"/></pattern></defs><rect width="{Wt}" height="{H}" fill="url(#g)"/>{blobs}'
           f'<path d="{d}" fill="none" stroke="{ink}" stroke-width="86" stroke-linecap="round"/>'
           f'<path d="{d}" fill="none" stroke="#fff" stroke-width="70" stroke-linecap="round"/>'
           f'<path d="{d}" fill="none" stroke="{acc}" stroke-width="8" stroke-dasharray="34 26"/></svg>')
    body = svg
    stops = n - 1
    for i, bt in enumerate(spec["beats"]):
        x0 = W * i
        if i > 0:                                # numbered pin
            px = x0 + 760
            py = road_y(px)
            last = i == n - 1 and spec.get("flag", True)
            body += (f'<div style="position:absolute;left:{px - 62}px;top:{py - 205:.0f}px;width:124px;height:124px;z-index:4;'
                     f'background:{acc};border:6px solid {ink};border-radius:50% 50% 50% 0;transform:rotate(-45deg);box-shadow:-6px 8px 0 {ink}33"></div>'
                     f'<div style="position:absolute;left:{px - 46}px;top:{py - 189:.0f}px;width:92px;height:92px;z-index:5;border-radius:50%;'
                     f'background:#fff;display:flex;align-items:center;justify-content:center;font-family:\'Noto Color Emoji\';font-size:54px">'
                     f'{bt.get("sign", "🏁" if last else str(i))}</div>'
                     f'<div style="position:absolute;left:{px - 9}px;top:{py - 16:.0f}px;width:18px;height:18px;border-radius:50%;background:{ink};z-index:4"></div>')
        cx = x0 + (170 if i == 0 else 330)
        ang = math.degrees(math.atan2(road_y(cx + 90) - road_y(cx - 90), 180))
        body += (f'<div style="position:absolute;left:{cx - 85}px;top:{road_y(cx) - 118:.0f}px;z-index:6;font-family:\'Noto Color Emoji\';font-size:150px;'
                 f'line-height:1;transform:scaleX(-1) rotate({-ang:.1f}deg);filter:drop-shadow(0 12px 10px rgba(0,0,0,.2))">{spec.get("car", "🚗")}</div>')
        body += stack(b, field, bt, x0 + 70, 100, W - 140, 92)
        # route strip: which stop you're at
        dots = ""
        sx0, sx1, sy = x0 + 250, x0 + 830, H - 92
        dots += f'<div style="position:absolute;left:{sx0}px;top:{sy - 3}px;width:{sx1 - sx0}px;height:6px;background:{ink};opacity:.25;z-index:5"></div>'
        for k in range(stops + 1):
            dx = sx0 + (sx1 - sx0) * k / stops
            on = k <= i
            dots += (f'<div style="position:absolute;left:{dx - 15:.0f}px;top:{sy - 15}px;width:30px;height:30px;border-radius:50%;z-index:6;'
                     f'background:{acc if on else "#fff"};border:4px solid {ink}"></div>')
        body += dots + counter(i + 1, n + 1, x0 + W - 120)
    body += f'<div style="position:absolute;inset:0;z-index:7">{K.stamp(b, 40, H - 210, 140, -12)}</div>'
    files = shot_pano(r, b, field, body, n, out_dir)
    return files + [do_slide(r, spec, out_dir, n + 1, n + 1)]


BUILD = {"follow": follow, "travel": travel, "trail": trail, "hold": hold, "reveal": reveal,
         "climb": climb, "streak": streak, "split": split, "roadmap": roadmap}


def build(ids):
    """Render each id; on a renderer hiccup (busy machine: screenshot timeouts, a full disk for a moment) restart the
    browser and retry that id, up to 3 tries."""
    import time
    import v5_formats as V
    r = C.R()
    try:
        for pid in ids:
            spec = V.FORMATS[pid]
            d = REPO / "media" / pid
            d.mkdir(exist_ok=True)
            for attempt in range(3):
                for old in d.glob("*.jpg"):
                    old.unlink()
                try:
                    files = BUILD[spec["kind"]](r, spec, d)
                    break
                except Exception as e:  # noqa: BLE001
                    print(pid, "retry", attempt + 1, type(e).__name__, str(e)[:120], flush=True)
                    try:
                        r.close()
                    except Exception:  # noqa: BLE001
                        pass
                    time.sleep(20)
                    r = C.R()
            else:
                raise RuntimeError(f"{pid}: render failed 3 times")
            assert len(files) <= 10, (pid, len(files))
            print(pid, len(files), "slides", flush=True)
    finally:
        r.close()


if __name__ == "__main__":
    build(sys.argv[1:])

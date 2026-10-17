#!/usr/bin/env python3
"""Pivot (Oct 17) Reels: one idea, giant hook in frame 0, one strong colour field per beat, 12-18 s,
cut on the beat grid of a v4 impact track with the payoff landing exactly on the track's measured drop
(tools/music-library.json drop_s). Rendered with studio/motion/kit.py (2x, motion blur, -14 LUFS).

    python3 studio/pivot/reels.py ff-reel-1017am-match [more ids] [--plan] [--out DIR]
    --plan prints the timing table only (no render).
Outputs go straight to media/reels/<id>.mp4 and media/reels/<id>-cover.jpg (the hook frame, 2x Lanczos).
"""
import argparse
import json
import math
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "studio" / "motion"))
sys.path.insert(0, str(HERE))
from kit import Reel, chip, el, emoji, encode, loudness, probe, qa_times, read_need, render_frames, sheet, words  # noqa: E402
from boldkit import FIELDS, field_css, mark_txt  # noqa: E402
from PIL import Image  # noqa: E402

LIB = json.loads((REPO / "tools" / "music-library.json").read_text())["tracks"]
HOOK_PX = {"fullyfunded": 170, "lockedhour": 175, "hourback": 150, "littlefold": 150}
SAY_PX = {"fullyfunded": 150, "lockedhour": 155, "hourback": 132, "littlefold": 136}
TRANS = {
    "fullyfunded": ["whipL", "stripes", "zoom", "slam", "iris", "whipU", "push"],
    "hourback": ["pixel", "whipL", "zoom", "slam", "stripes", "whipU", "iris"],
    "lockedhour": ["whipU", "stripes", "glitch", "zoom", "slam", "whipL", "iris"],
    "littlefold": ["blob", "whipL", "iris", "slam", "zoom", "whipU", "push"],
}
CHIP = {"fullyfunded": ("#FFFFFF", None), "hourback": ("#FFF8EF", "#2A2238"), "lockedhour": ("#141414", "#FFE27A"),
        "littlefold": ("#FFFFFF", None)}


# ------------------------------------------------------------------------------------------- scene html
def wrap(field, inner):
    return f'<div class="fx-{field}" style="position:absolute;inset:0"><div class="par dotbg fx-{field}"></div>{inner}</div>'


def col(inner, top=330, height=1080, gap=44):
    """Everything in one centred column inside the safe zone (y 330-1410), so stickers never collide with the words."""
    return el(inner, "c", top, a="none",
              style=f"height:{height}px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:{gap}px")


def wtxt(text, size, t=0.0, gap=0.11, anim=True, extra=""):
    """Kinetic words (one at a time) or static text. *a b* = accent, ' / ' = line break."""
    out, on = [], False
    for tok in text.split(" "):
        if tok == "/":
            out.append("<br>")
            continue
        if tok.startswith("*"):
            on = True
        core = tok.replace("*", "")
        out.append(f'<span class="w em">{core}</span>' if on else f'<span class="w">{core}</span>')
        if tok.endswith("*") or tok.rstrip(".,?!:;\u201d").endswith("*"):
            on = False
    attrs = f'data-a="words" data-t="{t:.3f}" data-d="0.32" data-gap="{gap}"' if anim else ""
    return f'<div class="T" {attrs} style="font-size:{size}px;{extra}">{" ".join(out)}</div>'


def sticker(ch, size=210, t=0.12, loop="float"):
    return (f'<span class="emo" data-a="pop" data-t="{t}" data-d="0.4" data-loop="{loop}" '
            f'style="display:inline-block;font-size:{size}px;filter:drop-shadow(0 22px 26px rgba(0,0,0,.22))">{ch}</span>')


def hook_html(brand, text, emo=None, size=None):
    size = size or HOOK_PX[brand]
    bg, ink = CHIP[brand]
    inner = wtxt(text, size, anim=False) + (sticker(emo) if emo else "")
    return chip(brand, "c", 230, bg=bg, ink=ink, a="none") + col(inner)


def say_html(brand, text, emo=None, size=None, t=0.0):
    size = size or SAY_PX[brand]
    return col(wtxt(text, size, t=t) + (sticker(emo, 180, 0.3, "wobble") if emo else ""))


def ai_html(brand, text, size=None):
    """The ask, as one big chat bubble with a robot sticker (Hourback)."""
    size = size or 96
    card = (f'<div data-a="fly" data-t="0.08" data-d="0.45" data-r="-2" style="background:#fff;color:#2A2238;border-radius:56px;'
            f'border-bottom-left-radius:14px;padding:56px 60px;text-align:left;box-shadow:0 30px 70px rgba(0,0,0,.28);'
            f'font:700 {size}px/1.12 Poppins;letter-spacing:-.03em">{mark_txt(text)}</div>')
    return col(sticker("🤖", 170, 0.0, "wobble") + card, gap=30)


def num_html(brand, label, value, pre="", suf_line="", size=300):
    inner = wtxt(label, 120, gap=0.1)
    inner += (f'<div class="T"><span class="em" data-a="count" data-t="0.1" data-d="0.75" data-to="{value}" data-comma="1" '
              f'data-pre="{pre}" style="font-size:{size}px;letter-spacing:-.06em;display:inline-block">{pre}0</span></div>')
    if suf_line:
        inner += wtxt(suf_line, 92, t=0.55, gap=0.08)
    return col(inner, gap=30)


def list_html(brand, items, size=118, gap=0.35):
    inner = "".join(f'<div class="T" data-a="pop" data-t="{i * gap:.2f}" data-d="0.35" style="font-size:{size}px">{mark_txt(it)}</div>'
                    for i, it in enumerate(items))
    return col(inner, gap=26)


def scene_html(brand, sc):
    k = sc["k"]
    if k == "hook":
        inner = hook_html(brand, sc["text"], sc.get("emo"), sc.get("size"))
    elif k == "say":
        inner = say_html(brand, sc["text"], sc.get("emo"), sc.get("size"))
    elif k == "ai":
        inner = ai_html(brand, sc["text"], sc.get("size"))
    elif k == "num":
        inner = num_html(brand, sc["label"], sc["value"], sc.get("pre", ""), sc.get("suf", ""), sc.get("size", 300))
    elif k == "list":
        inner = list_html(brand, sc["items"], sc.get("size", 118))
    else:
        raise ValueError(k)
    return wrap(sc["f"], inner)


# ------------------------------------------------------------------------------------------- timing on the drop
def plan(spec):
    """Beat lengths so every scene is readable (0.4 s/word + 0.6 s), cuts sit on the track's 16th-note grid anchored
    at the measured drop, and the scene marked drop=True starts exactly on drop_s."""
    tr = LIB[spec["track"]]
    beat, drop = 60.0 / tr["bpm"], tr["drop_s"]
    q = 0.25
    htmls = [scene_html(spec["brand"], sc) for sc in spec["scenes"]]
    need = [max(sc.get("min", 1.5), math.ceil((read_need(h)[0] - 1e-3) / beat / q) * q) for sc, h in zip(spec["scenes"], htmls)]
    di = next(i for i, sc in enumerate(spec["scenes"]) if sc.get("drop"))
    B = drop / beat
    pre = sum(need[:di])
    if pre > B + 1e-6:
        raise SystemExit(f"{spec['id']}: {pre * beat:.2f}s of reading before the drop at {drop:.2f}s; cut words")
    extra = B - pre
    # spread whole beats over the pre-drop scenes (more air to read), the fraction goes to the hook
    k = 0
    while extra >= 1.0 - 1e-9 and di > 0:
        need[k % di] += 1.0
        extra -= 1.0
        k += 1
    need[0] += extra
    loop_beats = max(1.5, math.ceil((read_need(htmls[0])[0] - 1e-3) / beat / q) * q)
    total = (sum(need) + loop_beats) * beat
    k = di
    while total < 12.6:
        need[k] += 0.5
        k = di + (k - di + 1) % (len(need) - di)
        total = (sum(need) + loop_beats) * beat
    if total > 18.0:
        raise SystemExit(f"{spec['id']}: {total:.2f}s is over 18 s; cut a scene")
    return htmls, need, loop_beats, beat, drop, total


def make(spec):
    brand = spec["brand"]
    tr = LIB[spec["track"]]
    htmls, need, loop_beats, beat, drop, total = plan(spec)
    first_field = spec["scenes"][0]["f"]
    r = Reel(spec["id"], brand, bpm=tr["bpm"], css=field_css(brand) + "\n.em.T{display:inline-block}",
             stage=FIELDS[brand][first_field]["bg"])
    trans = TRANS[brand]
    cams = ["push", "left", "rise", "push", "tilt", "right", "push"]
    for i, (sc, h, b) in enumerate(zip(spec["scenes"], htmls, need)):
        kw = dict(cam=cams[i % len(cams)], bg=FIELDS[brand][sc["f"]]["bg"])
        if i == 0:
            kw["shake"] = (0.12, 0.22, 16)
        else:
            t = sc.get("tin") or trans[(i - 1) % len(trans)]
            kw["tin"] = t
            if t in ("zoom", "iris", "blob"):
                kw["focus"] = (540, 820)
            if t in ("iris", "stripes", "blob"):
                f = FIELDS[brand]
                cols = [v["bg"] for v in f.values()]
                kw.update(color=cols[1 % len(cols)], color2=cols[2 % len(cols)], color3=cols[0])
            if sc.get("drop"):
                kw["shake"] = (0.0, 0.28, 24)
        r.scene(b, h, **kw)
    r.loop(loop_beats, tin="whipU" if brand != "hourback" else "pixel")
    return r


def report(spec):
    r = make(spec)
    tr = LIB[spec["track"]]
    di = next(i for i, sc in enumerate(spec["scenes"]) if sc.get("drop"))
    rows = []
    for i, s in enumerate(r.scenes):
        need, n = read_need(s["html"])
        rows.append(f"  {i}: {s['start']:5.2f}s +{s['dur']:4.2f}  words={n:2d} need={need:4.2f} {'OK' if s['dur'] + 1e-3 >= need else 'FAST'}")
    print(f"{spec['id']}  track={spec['track']} bpm={tr['bpm']} drop={tr['drop_s']}  payoff@{r.scenes[di]['start']:.3f}s  total={r.duration:.2f}s")
    print("\n".join(rows))
    return r


def build(spec, out_root):
    r = report(spec)
    bad = [s for s in r.scenes if s["dur"] + 1e-3 < read_need(s["html"])[0]]
    assert not bad, "a text beat is too fast to read"
    work = Path(out_root) / spec["id"]
    fdir, n = render_frames(r, work, dsf=2)
    mp4 = work / f"{spec['id']}.mp4"
    encode(fdir, n, REPO / LIB[spec["track"]]["file"], mp4)
    sheet(fdir, qa_times(r), work / f"{spec['id']}-qa.jpg", cols=10, scale=0.16)
    # cover = the hook frame after the sticker lands (2x Lanczos frame, chip + hook inside the safe zone)
    cov = Image.open(fdir / f"{int(0.75 * 30):05d}.png").convert("RGB")
    dst = REPO / "media" / "reels"
    cov.save(dst / f"{spec['id']}-cover.jpg", quality=92, subsampling=0)
    shutil.copy(mp4, dst / f"{spec['id']}.mp4")
    pr, lu = probe(mp4), loudness(mp4)
    print(json.dumps(dict(id=spec["id"], probe=pr, lufs=lu)))
    shutil.rmtree(fdir, ignore_errors=True)
    return pr


if __name__ == "__main__":
    from specs_reels import REELS
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--out", default="/tmp/pivot-reels")
    a = ap.parse_args()
    for rid in a.ids or list(REELS):
        spec = dict(REELS[rid], id=rid)
        if a.plan:
            report(spec)
        else:
            build(spec, a.out)

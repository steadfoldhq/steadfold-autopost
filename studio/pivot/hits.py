#!/usr/bin/env python3
"""Aggressive pivot Reels (Oct 17, 1:15 am direction): 10-15 s, a 3-5 word hook readable at frame 0, ONE hero number,
cut with the techniques measured on the owner's reference Reels (studio/pivot/TRANSITIONS.md, T1-T18), payoff exactly
on the v4 track's measured drop (tools/music-library.json drop_s), every other cut on its 16th-note grid.

    python3 studio/pivot/hits.py ff-reel-1017am-match [more ids] [--plan] [--out DIR] [--workers N]
Outputs: media/reels/<id>.mp4, media/reels/<id>-cover.jpg (the hook frame), and a QA sheet of frames around every cut.

Scene kinds (specs_hits.py):
  hook  giant hook (static at frame 0) + sticker pop; burn=True puts it on a card that burns away (T2) before a leak (T1)
  say   one big line; flick=True makes the accent words flicker through looks (T3)
  words one word/chunk at a time in the same spot (T5); ^x^ = bigger emphasis size (T14)
  swap  one giant word that swaps its look on every beat (T4)
  card  a white card (slides up over the last frame with tin="slamup", T8); grow=True pops it from 25% (T13)
  num   the hero number: counts up, punch-in (T7), hand-drawn circle (T9); put drop=True on it
Per scene: tin = transition in (leak, whipL, swipe, slamup, land, glide, cut), cam (push/left/rise/drift...).
Spec: pin=(first_scene, last_scene, text) pins a caption above the transitions (T10). The Reel loops to its hook (T15).
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
from kit import Reel, chip, el, encode, flicker, loudness, oneword, probe, read_need, render_frames, scribble_circle, sheet  # noqa: E402
from boldkit import FIELDS, FONT, field_css, mark_txt  # noqa: E402
from reels import col, sticker, wtxt  # noqa: E402
from PIL import Image  # noqa: E402

LIB = json.loads((REPO / "tools" / "music-library.json").read_text())["tracks"]
HOOK_PX = {"fullyfunded": 178, "lockedhour": 180, "hourback": 156, "littlefold": 156}
SAY_PX = {"fullyfunded": 158, "lockedhour": 160, "hourback": 140, "littlefold": 140}
NUM_INK = {"fullyfunded": "#FFFFFF", "hourback": "#FFFFFF", "lockedhour": "#141414", "littlefold": "#FFF4E0"}
CIRCLE = {"fullyfunded": "#FF6A3D", "hourback": "#FFC94D", "lockedhour": "#FF5CA8", "littlefold": "#FFE27E"}
CHIP = {"fullyfunded": ("#FFFFFF", None), "hourback": ("#FFF8EF", "#2A2238"), "lockedhour": ("#141414", "#FFE27A"),
        "littlefold": ("#FFFFFF", None)}
# T3 flicker looks: the reference cycles ~8 typefaces, one per source frame, and lands on the house style.
LOOKS = {
    "fullyfunded": ["font-family:'Caveat Brush';font-weight:400;letter-spacing:0",
                    "font-family:'Instrument Serif';font-style:italic;font-weight:400;letter-spacing:-.01em",
                    "font-family:Poppins;font-weight:800;letter-spacing:-.04em",
                    "font-family:Fraunces;font-weight:900;letter-spacing:-.03em",
                    "font-family:Lora;font-weight:700;font-style:italic",
                    "font-family:'Caveat';font-weight:700;letter-spacing:0",
                    "font-family:Inter;font-weight:900;text-transform:uppercase;letter-spacing:-.04em",
                    "font-family:'Inter Display';font-weight:800;letter-spacing:-.045em"],
}
# Looks change the face only; colour stays the field's accent (a look in the field's own colour disappears).
LOOKS["hourback"] = LOOKS["fullyfunded"][:-1] + [
    "font-family:Poppins;font-weight:700;letter-spacing:-.035em"]
LOOKS["lockedhour"] = LOOKS["fullyfunded"][:-1] + [
    "font-family:'Inter Display';font-weight:900;letter-spacing:-.05em"]
LOOKS["littlefold"] = LOOKS["fullyfunded"][:-1] + [
    "font-family:Lora;font-weight:600;letter-spacing:-.02em"]


def _flick_text(brand, text, size, t=0.0):
    """Static line where the *accent* run flickers (T3)."""
    out, buf, on = [], [], False
    for tok in text.split(" "):
        if tok == "/":
            (buf if on else out).append("<br>")
            continue
        if tok.startswith("*"):
            on = True
        (buf if on else out).append(tok.replace("*", ""))
        if on and tok.rstrip(".,?!:;”").endswith("*"):
            out.append(flicker(" ".join(buf), LOOKS[brand], base="display:inline-block", t=t + 0.12, cls="em"))
            buf, on = [], False
    if buf:
        out.append(flicker(" ".join(buf), LOOKS[brand], base="display:inline-block", t=t + 0.12, cls="em"))
    return f'<div class="T" style="font-size:{size}px">{" ".join(out)}</div>'


def scene_html(brand, sc, beat):
    k, size = sc["k"], sc.get("size")
    if k == "hook":
        bg, ink = CHIP[brand]
        txt = wtxt(sc["text"], size or HOOK_PX[brand], anim=False)
        if sc.get("burn"):  # T2: the hook sits on a white question-sticker card that burns away before the leak
            f = FIELDS[brand]["lite" if brand == "fullyfunded" else list(FIELDS[brand])[0]]
            txt = (f'<div data-a="burn" data-tend="__BURN_D__" data-d="__BURN_D__" data-to="0.62" style="position:relative;background:#fff;'
                   f'border-radius:56px;padding:58px 54px 64px;box-shadow:0 30px 80px rgba(0,0,0,.30)">'
                   f'<div class="fx-lite" style="color:{f["ink"]}">{wtxt(sc["text"], (size or HOOK_PX[brand]) - 14, anim=False)}</div></div>')
        inner = txt + (sticker(sc["emo"]) if sc.get("emo") else "")
        return chip(brand, "c", 230, bg=bg, ink=ink, a="none") + col(inner)
    if k == "say":
        if sc.get("flick"):
            inner = _flick_text(brand, sc["text"], size or SAY_PX[brand])
        else:
            inner = wtxt(sc["text"], size or SAY_PX[brand])
        return col(inner + (sticker(sc["emo"], 180, 0.3, "wobble") if sc.get("emo") else ""))
    if k == "words":
        return col(oneword(sc["chunks"], t=0.0, gap=sc.get("gap", 0.6), style=f"font-size:{size or SAY_PX[brand]}px"))
    if k == "swap":
        looks = sc.get("looks") or LOOKS[brand][-3:]  # 3 looks, one per beat, lands on the house style
        return col(flicker(mark_txt(sc["text"]), looks, base=f"display:block;font-size:{size or 230}px", step=beat, cls="T"))
    if k == "card":
        inner = (f'<div data-a="{"grow" if sc.get("grow") else "none"}" data-t="0" data-d="0.3" style="background:#fff;color:#0E1440;'
                 f'border-radius:48px;padding:64px 60px;box-shadow:0 30px 80px rgba(0,0,0,.30);width:920px">'
                 f'<div style="font:800 64px/1.1 Inter;letter-spacing:-.02em;opacity:.75">{mark_txt(sc["label"])}</div>'
                 f'<div class="T" style="font-size:{size or 210}px;color:#2B3FE0;margin-top:18px">{mark_txt(sc["value"])}</div></div>')
        return col(inner)
    if k == "num":
        # fixed layout so the punch-in (T7) and circle (T9) land on the number
        lab = wtxt(sc["label"], 118, gap=0.08)
        num = (f'<span data-a="count" data-t="0.06" data-d="0.62" data-to="{sc["value"]}" data-comma="1" data-dec="{sc.get("dec", 0)}" data-from="{sc["value"] if sc["value"] < 10 else 0}" data-pre="{sc.get("pre", "")}" '
               f'data-suf="{sc.get("unit", "")}">{sc.get("pre", "")}0{sc.get("unit", "")}</span>')
        shown = f'{sc.get("pre", "")}{sc["value"]:,.{sc.get("dec", 0)}f}{sc.get("unit", "")}'
        nsize = min(sc.get("size", 260), int(780 / (0.58 * len(shown))))  # 780 px wide, 875 after the 1.12 punch-in: inside x 70-1010
        body = (el(lab, "c", 470, a="none") +
                el(f'<div class="T" style="font-size:{nsize}px;letter-spacing:-.06em;color:{NUM_INK[brand]}">{num}</div>', "c",
                   900 - nsize // 2, a="none") +
                scribble_circle(540, 900, 418, max(150, int(nsize * 0.62)), CIRCLE[brand], width=14, t=0.86, d=0.2) +
                (el(wtxt(sc["suf"], 84, t=0.5, gap=0.07), "c", 1190, a="none") if sc.get("suf") else ""))
        return f'<div data-a="punch" data-t="0.72" data-d="0.17" data-s="{sc.get("punch", 1.12)}" data-ox="540px" data-oy="900px" style="position:absolute;inset:0">{body}</div>'
    raise ValueError(k)


def wrap(field, inner):
    return f'<div class="fx-{field}" style="position:absolute;inset:0"><div class="par dotbg fx-{field}"></div>{inner}</div>'


def plan(spec):
    tr = LIB[spec["track"]]
    beat, drop = 60.0 / tr["bpm"], tr["drop_s"]
    q = 0.25
    htmls = [wrap(sc["f"], scene_html(spec["brand"], sc, beat)) for sc in spec["scenes"]]
    need = [max(sc.get("min", 1.25), math.ceil((read_need(h)[0] - 1e-3) / beat / q) * q) for sc, h in zip(spec["scenes"], htmls)]
    di = next(i for i, sc in enumerate(spec["scenes"]) if sc.get("drop"))
    B = drop / beat
    pre = sum(need[:di])
    if pre > B + 1e-6:
        raise SystemExit(f"{spec['id']}: {pre * beat:.2f}s of reading before the drop at {drop:.2f}s; cut words")
    extra = B - pre
    k = 0
    while extra >= 1.0 - 1e-9 and di > 0:
        need[k % di] += 1.0
        extra -= 1.0
        k += 1
    need[0] += extra
    loop_beats = max(1.5, math.ceil((read_need(htmls[0])[0] - 1e-3) / beat / q) * q)
    total = (sum(need) + loop_beats) * beat
    k = di
    while total < 10.6:
        need[k] += 0.5
        k = di + (k - di + 1) % (len(need) - di)
        total = (sum(need) + loop_beats) * beat
    if total > 15.0:
        raise SystemExit(f"{spec['id']}: {total:.2f}s is over 15 s; cut a scene")
    return htmls, need, loop_beats, beat, drop, total


def make(spec):
    brand = spec["brand"]
    tr = LIB[spec["track"]]
    htmls, need, loop_beats, beat, drop, total = plan(spec)
    r = Reel(spec["id"], brand, bpm=tr["bpm"], css=field_css(brand) + "\n.em.T{display:inline-block}",
             stage=FIELDS[brand][spec["scenes"][0]["f"]]["bg"])
    for i, (sc, h, b) in enumerate(zip(spec["scenes"], htmls, need)):
        dur = b * beat
        if sc["k"] == "hook" and sc.get("burn"):
            bd = min(1.6, max(0.8, dur - 1.6))  # the hook stays clean for at least 1.6 s (cover + read)
            h = h.replace("__BURN_D__", f"{bd:.3f}")
        kw = dict(cam=sc.get("cam", ["push", "left", "rise", "push", "tilt", "right"][i % 6]), bg=FIELDS[brand][sc["f"]]["bg"])
        if i == 0:
            kw["shake"] = (0.12, 0.22, 16)
        else:
            t = sc.get("tin", "whipL")
            kw["tin"] = t
            if t in ("land", "leak"):
                kw["focus"] = (540, 900)
                f = list(FIELDS[brand].values())
                kw.update(color=f[0]["bg"] if brand != "fullyfunded" else "#FFB08F", color2=f[-1]["bg"] if brand != "fullyfunded" else "#FF6A3D")
            if sc.get("drop"):
                kw["shake"] = (0.0, 0.28, 24)
        r.scene(b, h, **kw)
    if spec.get("pin"):
        a, z, text = spec["pin"]
        r.pin(r.scenes[a]["start"], r.scenes[z]["start"] + r.scenes[z]["dur"],
              el(f'<span style="display:inline-block;background:#0E1440;color:#fff;font:800 54px/1 Inter;padding:20px 34px;'
                 f'border-radius:999px;letter-spacing:-.01em">{text}</span>', "c", 1430, a="pop", d=0.25))
    s0 = r.scenes[0]  # T15 seamless loop: end on the clean hook frame (no burn), so the last frame flows into frame 0
    r.scene(loop_beats, s0["html"].replace('data-a="burn"', 'data-a="none"'), tin=spec.get("loop_tin", "leak"), cam=s0["cam"], bg=s0["bg"],
            focus=(540, 900))
    return r


def qa_times(r):
    ts = [0.0, 0.75]
    for c in r.cuts():
        ts += [c - 0.13, c - 0.067, c - 0.033, c, c + 0.033, c + 0.067, c + 0.13, c + 0.2]
    return sorted(set(round(min(max(0, x), r.duration - 1 / 30), 3) for x in ts))


def report(spec):
    r = make(spec)
    tr = LIB[spec["track"]]
    di = next(i for i, sc in enumerate(spec["scenes"]) if sc.get("drop"))
    print(f"{spec['id']}  track={spec['track']} bpm={tr['bpm']} drop={tr['drop_s']}  payoff@{r.scenes[di]['start']:.3f}s  total={r.duration:.2f}s")
    for i, s in enumerate(r.scenes):
        need, n = read_need(s["html"])
        tin = (s["tin"] or {}).get("type", "-")
        print(f"  {i}: {s['start']:5.2f}s +{s['dur']:4.2f} {tin:7s} words={n:2d} need={need:4.2f} {'OK' if s['dur'] + 1e-3 >= need else 'FAST'}")
    return r


def build(spec, out_root, workers=2):
    r = report(spec)
    bad = [s for s in r.scenes if s["dur"] + 1e-3 < read_need(s["html"])[0]]
    assert not bad, "a text beat is too fast to read"
    assert 10.0 <= r.duration <= 15.0, r.duration
    work = Path(out_root) / spec["id"]
    fdir, n = render_frames(r, work, dsf=2, workers=workers)
    mp4 = work / f"{spec['id']}.mp4"
    encode(fdir, n, REPO / LIB[spec["track"]]["file"], mp4)
    sheet(fdir, qa_times(r), work / f"{spec['id']}-qa.jpg", cols=9, scale=0.16)
    cov = Image.open(sorted(fdir.glob("00022.*"))[0]).convert("RGB")
    dst = REPO / "media" / "reels"
    cov.save(dst / f"{spec['id']}-cover.jpg", quality=92, subsampling=0)
    shutil.copy(mp4, dst / f"{spec['id']}.mp4")
    pr, lu = probe(mp4), loudness(mp4)
    print(json.dumps(dict(id=spec["id"], probe=pr, lufs=lu)))
    shutil.rmtree(fdir, ignore_errors=True)
    return pr


if __name__ == "__main__":
    from specs_hits import REELS
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--out", default="/tmp/pivot-hits")
    ap.add_argument("--workers", type=int, default=2)
    a = ap.parse_args()
    for rid in a.ids or list(REELS):
        spec = dict(REELS[rid], id=rid)
        if a.plan:
            report(spec)
        else:
            build(spec, a.out, a.workers)

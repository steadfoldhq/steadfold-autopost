#!/usr/bin/env python3
"""Pivot (Oct 17) feed tiles: one idea, giant hook, one colour field, at most 3 slides.
Rendered with Chromium at 2x and Lanczos-downsampled to 1080x1350 (brand rule 7), JPEG q92, no chroma subsampling.

    python3 studio/pivot/stills.py [ids]        -> media/<id>/01.jpg ... (old extra slides removed)
"""
import glob
import io
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
from boldkit import HANDLE, MARK, MARKS, NAME, field_css, mark_txt  # noqa: E402
from PIL import Image  # noqa: E402

W, H = 1080, 1350
CHROME = (glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))[0]
HOOK_PX = {"fullyfunded": 168, "lockedhour": 172, "hourback": 146, "littlefold": 150}
CHIP = {"fullyfunded": ("#FFFFFF", "#0E1440"), "hourback": ("#FFF8EF", "#2A2238"), "lockedhour": ("#141414", "#FFE27A"),
        "littlefold": ("#FFFFFF", "#2C2A3A")}
KICK = {"fullyfunded": ("#FF6A3D", "#FFFFFF"), "hourback": ("#2A2238", "#FFC94D"), "lockedhour": ("#141414", "#FFE27A"),
        "littlefold": ("#D9497A", "#FFFFFF")}


def slide_html(brand, s, i, n):
    f = s["f"]
    size = s.get("size", HOOK_PX[brand] if i == 0 else int(HOOK_PX[brand] * 0.8))
    cbg, cink = CHIP[brand]
    kbg, kink = KICK[brand]
    parts = []
    if s.get("kicker"):
        parts.append(f'<div class="kick" style="background:{kbg};color:{kink}">{s["kicker"]}</div>')
    parts.append(f'<div class="T hook" style="font-size:{size}px">{mark_txt(s["text"])}</div>')
    if s.get("num"):  # aggressive pivot: ONE hero number, as big as the hook allows
        parts.append(f'<div class="T num em" style="font-size:{s.get("num_px", 230)}px;letter-spacing:-.06em">{s["num"]}</div>')
    if s.get("emo"):
        parts.append(f'<div class="emo" style="font-size:{s.get("emo_px", 190)}px">{s["emo"]}</div>')
    if s.get("sub"):
        parts.append(f'<div class="sub">{mark_txt(s["sub"])}</div>')
    swipe = (f'<div class="swipe" style="background:{cbg};color:{cink}">Swipe →</div>' if (n > 1 and i == 0) else "")
    count = f'<div class="count">{i + 1}/{n}</div>' if n > 1 else ""
    src = s.get("src", "")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
{field_css(brand)}
.page{{position:absolute;inset:0}}
.chip{{position:absolute;left:50%;top:64px;transform:translateX(-50%);display:flex;align-items:center;gap:12px;border-radius:999px;
  padding:6px 24px 6px 6px;font:700 30px/1 Inter;background:{cbg};color:{cink};white-space:nowrap}}
.chip img{{width:48px;height:48px;border-radius:50%;background:#fff}}
.col{{position:absolute;left:70px;right:70px;top:150px;height:1060px;display:flex;flex-direction:column;justify-content:center;
  align-items:center;gap:40px;text-align:center}}
.kick{{font:800 30px/1 Inter;letter-spacing:.12em;text-transform:uppercase;padding:14px 22px;border-radius:999px}}
.emo{{font-family:'Noto Color Emoji';line-height:1;filter:drop-shadow(0 22px 26px rgba(0,0,0,.22))}}
.sub{{font:700 50px/1.22 Inter;max-width:900px;opacity:.92}}
.sub .em{{font-style:normal}}
.count{{position:absolute;right:56px;top:76px;font:800 28px/1 Inter;opacity:.6}}
.swipe{{position:absolute;right:56px;bottom:56px;font:800 30px/1 Inter;padding:16px 26px;border-radius:999px}}
.handle{{position:absolute;left:56px;bottom:66px;font:700 28px/1 Inter;opacity:.7}}
.src{{position:absolute;left:0;right:0;bottom:120px;text-align:center;font:600 26px/1.2 Inter;opacity:.7}}
</style></head><body><div class="page fx-{f} dotbg">
<div class="chip"><img src="{(MARKS / MARK[brand]).as_uri()}">{NAME[brand]}</div>{count}
<div class="col">{''.join(parts)}</div>
{f'<div class="src">{src}</div>' if src else ''}
<div class="handle">{HANDLE[brand]}</div>{swipe}
</div></body></html>"""


def render(posts, ids):
    from playwright.sync_api import sync_playwright
    out = {}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--disable-gpu", "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        for pid in ids:
            spec = posts[pid]
            d = REPO / "media" / pid
            d.mkdir(exist_ok=True)
            for old in d.glob("*.jpg"):
                old.unlink()
            n = len(spec["slides"])
            assert n <= 3, pid
            files = []
            for i, s in enumerate(spec["slides"]):
                pg.set_content(slide_html(spec["brand"], s, i, n))
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(150)
                # shrink any hook line wider than the safe width (x 70-1010)
                pg.evaluate("""() => { document.querySelectorAll('.hook, .num').forEach(h => { for (let k = 0; k < 8; k++) {
                    const r = document.createRange(); r.selectNodeContents(h); let lo = 1e9, hi = -1e9;
                    for (const q of r.getClientRects()) { lo = Math.min(lo, q.left); hi = Math.max(hi, q.right); }
                    if (hi - lo <= 940) break; h.style.fontSize = (parseFloat(getComputedStyle(h).fontSize) * 0.94) + 'px'; } }); }""")
                im = Image.open(io.BytesIO(pg.screenshot(type="png"))).convert("RGB").resize((W, H), Image.LANCZOS)
                fn = d / f"{i + 1:02d}.jpg"
                im.save(fn, quality=92, subsampling=0)
                files.append(f"{pid}/{fn.name}")
            out[pid] = files
            print(pid, files)
        b.close()
    return out


if __name__ == "__main__":
    from specs_stills import POSTS
    render(POSTS, sys.argv[1:] or list(POSTS))

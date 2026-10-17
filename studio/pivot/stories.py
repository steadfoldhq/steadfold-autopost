#!/usr/bin/env python3
"""Aggressive pivot Stories (Oct 17): one giant line, one colour field, at most one card. 1080x1920, 2x render + Lanczos.
Safe zone: nothing important above y 250 or below y 1580 (Instagram's Story UI).

    python3 studio/pivot/stories.py [ids]     -> media/stories/<id>.jpg
Kinds: question (2 answer pills), newpost (the post's new cover on a tilted card), tip, evening (Reel cover + 2 pills).
"""
import glob
import io
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
from boldkit import MARK, MARKS, NAME, data_uri, field_css, mark_txt  # noqa: E402
from PIL import Image  # noqa: E402

W, H = 1080, 1920
CHROME = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")[0]
KICK = {"question": "Morning question", "newpost": "Just posted", "tip": "Quick tip", "evening": "Tonight's check-in"}
HOOK_PX = {"fullyfunded": 150, "hourback": 132, "lockedhour": 155, "littlefold": 136}

FF = "fullyfunded"
STORIES = {
    "ff-st-1017-0750-question": dict(brand=FF, k="question", f="cob", text="Raise lands. / *First move?*", a="Save some", b="Enjoy it all"),
    "ff-st-1017-1230-newpost": dict(brand=FF, k="newpost", f="deep", text="The rich / *borrow.*", img="ff-w03-2-borrow-dont-sell/01.jpg"),
    "ff-st-1017-1535-tip": dict(brand=FF, k="tip", f="coral", text="Ask your lender: / *“Best rate?”*", sub="Once a year. Takes 5 minutes.", emo="📞"),
    "ff-st-1017-2105-evening": dict(brand=FF, k="evening", f="deep", text="Save half / *your next raise?*", img="reels/ff-reel-1017-raise-half-cover.jpg",
                                    a="Yes", b="Not yet"),
    "ff-st-1018-0750-question": dict(brand=FF, k="question", f="cob", text="Got a *will?*", a="Yes", b="Not yet"),
    "ff-st-1018-1230-newpost": dict(brand=FF, k="newpost", f="deep", text="Kids? Name / a *guardian.*", img="ff-w03-3-guardian-will/01.jpg"),
    "ff-st-1018-1535-tip": dict(brand=FF, k="tip", f="coral", text="Tell *1 person* / where your will is.", emo="🗝️"),
    "ff-st-1018-2105-evening": dict(brand=FF, k="evening", f="deep", text="$100 a month / *for a kid?*", img="reels/ff-reel-1018-the-door-cover.jpg",
                                    a="Yes", b="Not yet"),
    "ff-st-1019-0750-question": dict(brand=FF, k="question", f="cob", text="Gift list: / *how many?*", a="Under 10", b="10 or more"),
    "ff-st-1019-1230-newpost": dict(brand=FF, k="newpost", f="deep", text="Price ÷ / *uses.*", img="ff-1019-rich-habits-01/01.jpg"),
    "ff-st-1019-1535-tip": dict(brand=FF, k="tip", f="coral", text="Big buy? / *Price ÷ uses.*", emo="🧥"),
    "ff-st-1019-2105-evening": dict(brand=FF, k="evening", f="deep", text="Transfer set / *for payday?*", img="reels/ff-reel-1019-late-start-cover.jpg",
                                    a="Done", b="Not yet"),
    "ff-st-1020-0750-question": dict(brand=FF, k="question", f="cob", text="Money talk / *at home?*", a="Easy", b="Awkward"),
    "ff-st-1020-1230-newpost": dict(brand=FF, k="newpost", f="deep", text="Same *$10,000.* / 20 years.", img="ff-1020-pick-its-home/01.jpg"),
    "ff-st-1020-1535-tip": dict(brand=FF, k="tip", f="coral", text="Find *1 rate* / on your savings.", emo="🔍"),
    "ff-st-1020-2105-evening": dict(brand=FF, k="evening", f="deep", text="Money coming? / *Park it first.*", img="reels/ff-reel-1020-windfall-pause-cover.jpg",
                                    a="Parked", b="Not yet"),
}


def html(sid, s):
    b = s["brand"]
    parts = [f'<div class="T hook" style="font-size:{s.get("size", HOOK_PX[b])}px">{mark_txt(s["text"])}</div>']
    if s.get("emo"):
        parts.append(f'<div class="emo">{s["emo"]}</div>')
    if s.get("sub"):
        parts.append(f'<div class="sub">{mark_txt(s["sub"])}</div>')
    if s.get("img"):
        tall = s["k"] == "evening"
        parts.append(f'<div class="card {"tall" if tall else ""}"><img src="{data_uri(REPO / "media" / s["img"])}"></div>')
    if s.get("a"):
        parts.append(f'<div class="pills"><div class="pill">{s["a"]}</div><div class="pill alt">{s["b"]}</div></div>')
    if s["k"] == "newpost":
        parts.append('<div class="cta">Tap our profile to see it</div>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0;padding:0}} html,body{{width:{W}px;height:{H}px;overflow:hidden}}
{field_css(b)}
.page{{position:absolute;inset:0}}
.top{{position:absolute;left:80px;right:80px;top:260px;display:flex;justify-content:space-between;align-items:center}}
.chip{{display:flex;align-items:center;gap:12px;border-radius:999px;padding:6px 24px 6px 6px;font:700 32px/1 Inter;background:#fff;color:#0E1440}}
.chip img{{width:50px;height:50px;border-radius:50%}}
.kick{{font:800 30px/1 Inter;letter-spacing:.12em;text-transform:uppercase;padding:16px 24px;border-radius:999px;background:#FF6A3D;color:#fff}}
.col{{position:absolute;left:70px;right:70px;top:380px;bottom:340px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:46px;text-align:center}}
.emo{{font-family:'Noto Color Emoji';font-size:200px;line-height:1;filter:drop-shadow(0 22px 26px rgba(0,0,0,.22))}}
.sub{{font:700 52px/1.2 Inter;opacity:.92}}
.card{{width:470px;transform:rotate(-4deg);background:#fff;padding:14px;border-radius:30px;box-shadow:0 34px 80px rgba(0,0,0,.35)}}
.card.tall{{width:360px}}
.card img{{width:100%;display:block;border-radius:20px}}
.pills{{display:flex;gap:26px}}
.pill{{font:800 54px/1 Inter;padding:30px 46px;border-radius:999px;background:#fff;color:#0E1440}}
.pill.alt{{background:#FF6A3D;color:#fff}}
.cta{{font:800 46px/1 Inter;color:#FFB08F}}
</style></head><body><div class="page fx-{s["f"]} dotbg">
<div class="top"><div class="chip"><img src="{data_uri(MARKS / MARK[b])}">{NAME[b]}</div><div class="kick" style="{"background:#0E1440" if s["f"] == "coral" else ""}">{KICK[s["k"]]}</div></div>
<div class="col">{''.join(parts)}</div></div></body></html>"""


def render(ids):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path=CHROME, args=["--disable-gpu", "--font-render-hinting=none"])
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        for sid in ids:
            pg.set_content(html(sid, STORIES[sid]))
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(200)
            pg.evaluate("""() => { const h = document.querySelector('.hook'); for (let k = 0; k < 8; k++) {
                const r = document.createRange(); r.selectNodeContents(h); let lo = 1e9, hi = -1e9;
                for (const q of r.getClientRects()) { lo = Math.min(lo, q.left); hi = Math.max(hi, q.right); }
                if (hi - lo <= 920) break; h.style.fontSize = (parseFloat(getComputedStyle(h).fontSize) * 0.94) + 'px'; } }""")
            im = Image.open(io.BytesIO(pg.screenshot(type="png"))).convert("RGB").resize((W, H), Image.LANCZOS)
            out = REPO / "media" / "stories" / f"{sid}.jpg"
            im.save(out, quality=92, subsampling=0)
            print(out.relative_to(REPO))
        br.close()


if __name__ == "__main__":
    render(sys.argv[1:] or list(STORIES))

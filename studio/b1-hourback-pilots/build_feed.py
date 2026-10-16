#!/usr/bin/env python3
"""Hourback pilots Oct 19-21 (agent B1): feed tiles + carousel, built on the studio engine (brand-system v4, 2x render)."""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/claude/content/design/samples-v5")
import build_mix as BM            # meme / reframe / paper_list, LOOKB colourways
import build_grid_tiles as GT     # Look B cover
from lib import render_many

OUT = Path("/home/claude/hb-pilots/out")
MK = Path("/home/claude/content/design/assets/marks")
HBV = BM.LOOKB["hb-b"][1]          # approved Hourback Look B colourway (indigo, yellow pills, white ink)
HBV_CREAM = GT.V("#FFF8EF", "#2A2238", ("#FFC94D", "#2A2238"), ("#5E54C9", "#FFFFFF"), "#5E54C9", "#FFC94D", "#2A2238")

def bubble_css():
    return ("<style>.bub{position:absolute;font:600 40px/1.25 Inter;padding:22px 30px;border-radius:34px;max-width:640px;"
            "box-shadow:0 10px 24px rgba(20,10,60,.18)}.bub.me{background:#FFC94D;color:#2A2238;border-bottom-right-radius:10px}"
            ".bub.ai{background:#fff;color:#2A2238;border-bottom-left-radius:10px}.bub small{display:block;font:800 22px/1 Inter;"
            "letter-spacing:.14em;text-transform:uppercase;opacity:.6;margin-bottom:10px}</style>")

# 1) Mon Oct 19 17:45 · Look B (loud) · Group chat vs AI (real run r7)
t1 = GT.cover(GT.HB("group chat vs AI", [("47", 1), "messages.", "Still", "no", ("plan.", 2)],
                    save="", obj=None), HBV, obj=False, save=False,
              extra=bubble_css() +
              '<div class="bub ai" data-noqa style="left:84px;top:1010px;max-width:760px;font-size:44px"><small>Real AI reply</small>'
              '“Saturday at 2pm at Rosa’s, for 4 people, and Noor books.”</div>'
              '<div data-noqa style="position:absolute;right:84px;top:1240px;font:700 24px/1 Inter;color:#fff;opacity:.8">Chat made up</div>')

# 2) Tue Oct 20 17:45 · sticky-note list (quiet) · pilot hb-a5-03
t2 = BM.paper_list("#FFC94D", "#FFFDF8", "#2A2238", "#5E54C9", "hourback.png", "Hourback",
                   "I stopped doing:",
                   ["Reading long emails", "4 sorries per email", "3 tabs at 11 pm", "Scrolling 47 messages"], tilt=-2)
t2 = t2[:-6] + ('<div data-noqa style="position:absolute;right:96px;top:1212px;font-family:CaveatBrush;font-size:58px;'
                'color:#5E54C9;transform:rotate(-2deg)">still checking every quote</div>') + t2[-6:]

# 3) Wed Oct 21 13:00 · AI Said What? carousel, 3 slides (real run r8)
def slide(inner, n):
    return (f'<style>.slide{{width:1080px;height:1350px;background:#FFF8EF;position:relative;overflow:hidden}}'
            f'.k{{position:absolute;left:84px;top:96px;font:800 28px/1 Inter;letter-spacing:.16em;text-transform:uppercase;'
            f'color:#2A2238;background:#FFC94D;padding:14px 20px;border-radius:999px}}'
            f'.n{{position:absolute;right:84px;top:104px;font:700 28px Inter;color:#2A2238;opacity:.6}}'
            f'.h{{position:absolute;left:84px;right:84px;font-family:Poppins;font-weight:700;letter-spacing:-.035em;line-height:1.02;color:#2A2238}}'
            f'.yl{{background:linear-gradient(#FFC94D,#FFC94D) no-repeat 0 88%/100% 46%;padding:0 .06em}}'
            f'.p{{position:absolute;left:84px;right:84px;font:500 42px/1.35 Inter;color:#2A2238}}'
            f'.b{{position:absolute;left:84px;bottom:76px;display:flex;gap:12px;align-items:center;font:700 26px Inter;color:#2A2238}}'
            f'.b img{{width:46px;height:46px;border-radius:50%;background:#fff;padding:2px}}</style>{bubble_css()}'
            f'<div class="slide"><div class="k">AI said what?</div><div class="n">{n}/3</div>{inner}'
            f'<div class="b"><img src="{(MK / "hourback.png").as_uri()}">Hourback</div></div>')

c1_old = slide('<div class="h" style="top:230px;font-size:132px">$96 dinner. <span class="yl">Ana didn’t drink.</span></div>'
           '<div class="p" style="top:760px">We asked AI to split it fairly.</div>'
           '<div class="bub me" style="right:84px;top:880px">Food: all 4. Drinks ($24): only the 3 who drank.</div>'
           '<div class="bub ai" style="left:84px;top:1010px">Typing…</div>'
           '<div class="p" style="top:1130px;font-size:34px;opacity:.75">Swipe for what it said →</div>', 1)
c2 = slide('<div class="h" style="top:200px;font-size:96px">What it said</div>'
           '<div class="bub ai" style="left:84px;top:360px;max-width:912px;font-size:44px"><small>The AI’s math, condensed</small>'
           'Food: $96 − $24 = $72<br>$72 ÷ 4 = <b>$18</b> each<br>Drinks: $24 ÷ 3 = <b>$8</b> each<br><br>'
           'Ana: <b>$18</b><br>Each of the other 3: $18 + $8 = <b>$26</b></div>'
           '<div class="p" style="top:1110px;font-size:34px;opacity:.75">Example made up. Reply from a real AI run, Oct 2026.</div>', 2)
c3 = slide('<div class="h" style="top:210px;font-size:150px">It <span class="yl">passed.</span></div>'
           '<div class="p" style="top:430px">Here’s how we checked:</div>'
           '<div class="p" style="top:530px;font:700 76px/1.2 Poppins">18 + 26 + 26 + 26<br>= 96 ✓</div>'
           '<div class="p" style="top:820px">The fix line for any split:<br><b>“Show the math and check that it adds up.”</b></div>'
           '<div class="p" style="top:1080px;font-size:34px;opacity:.75">Save this for the next group dinner.</div>', 3)

c1 = GT.cover(GT.HB("AI said what?", [("$96", 1), "dinner.", "Ana", "didn’t", ("drink.", 2)], save="", obj=None),
              HBV_CREAM, obj=False, save=False,
              extra=bubble_css() +
              '<div class="bub me" data-noqa style="right:84px;top:1000px;font-size:42px;max-width:760px">Split it fairly. Food: all 4. '
              'Drinks ($24): only the 3 who drank.</div>'
              '<div data-noqa style="position:absolute;right:84px;top:1230px;font:700 28px/1 Inter;color:#2A2238">Swipe for the answer →</div>')

# 4) Wed Oct 21 17:45 · Look B (loud) · subscriptions (real run r9)
t4 = BM.meme("#5E54C9", "#FFFFFF", "#FFC94D", "hourback.png", "Hourback",
             "Me, finally reading my whole card statement:", "🧾👀",
             "AI: 5 subscriptions.<br>$78.47 a month.")
t4 = t4[:-6] + ('<div data-noqa style="position:absolute;right:84px;bottom:90px;font:700 24px/1 Inter;color:#fff;opacity:.8">'
                'Example made up</div>') + t4[-6:]

JOBS = [(t1, OUT / "hb-1019-single-group-chat" / "01"), (t2, OUT / "hb-1020-single-stopped-doing" / "01"),
        (c1, OUT / "hb-1021-ai-said-what-bill" / "01"), (c2, OUT / "hb-1021-ai-said-what-bill" / "02"),
        (c3, OUT / "hb-1021-ai-said-what-bill" / "03"), (t4, OUT / "hb-1021-single-subscriptions" / "01")]
if __name__ == "__main__":
    only = set(sys.argv[1:])
    render_many([j for j in JOBS if not only or j[1].parent.name in only], jpg_q=92)

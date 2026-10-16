#!/usr/bin/env python3
"""Hourback Stories Oct 19-21 (agent B1): 4 a day. Question cards (stickers can't be added by API, so the question is
in the image), behind-the-scenes capture cards and 'new post' shares. 1080x1920, text inside y 250-1650, 2x render."""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/claude/content/design/samples-v5")
from lib import render_many

OUT = Path("/home/claude/hb-pilots/out/stories"); OUT.mkdir(parents=True, exist_ok=True)
FEED = Path("/home/claude/hb-pilots/out")
MK = Path("/home/claude/content/design/assets/marks/hourback.png").as_uri()
BASE = ("<style>.slide{width:1080px;height:1920px;position:relative;overflow:hidden}"
        ".chip{position:absolute;left:96px;top:300px;display:flex;align-items:center;gap:12px;background:#fff;border-radius:999px;"
        "padding:6px 24px 6px 6px;font:700 30px/1 Inter;color:#2A2238}.chip img{width:50px;height:50px;border-radius:50%}"
        ".k{display:inline-block;font:800 30px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:#2A2238;background:#FFC94D;"
        "padding:14px 22px;border-radius:999px}"
        ".h{font-family:Poppins;font-weight:700;letter-spacing:-.035em;line-height:1.04}"
        ".yl{background:linear-gradient(#FFC94D,#FFC94D) no-repeat 0 88%/100% 46%;padding:0 .06em;color:#2A2238}"
        ".p{font:600 50px/1.3 Inter}.box{position:absolute;left:96px;right:96px}"
        ".opt{display:block;background:#fff;color:#2A2238;border-radius:28px;padding:30px 36px;font:700 52px/1.1 Inter;margin:0 0 22px;"
        "box-shadow:0 10px 24px rgba(20,10,60,.16)}.opt b{color:#5E54C9;margin-right:18px}"
        ".card{background:#fff;border-radius:40px;padding:40px 46px;color:#2A2238;font:500 46px/1.38 Inter;box-shadow:0 18px 40px rgba(40,20,100,.2)}"
        ".card .lab{display:inline-block;font:800 26px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:#fff;background:#5E54C9;"
        "padding:10px 16px;border-radius:999px;margin-bottom:20px}.q{color:#5E54C9;font-weight:700}</style>")


def chip():
    return f'<div class="chip"><img src="{MK}">Hourback</div>'


def question(bg, ink, kick, hook, opts, foot):
    o = "".join(f'<span class="opt"><b>{a}</b>{t}</span>' for a, t in opts)
    return (BASE + f'<div class="slide" style="background:{bg}">{chip()}<div class="box" style="top:430px"><span class="k">{kick}</span>'
            f'<div class="h" style="font-size:118px;color:{ink};margin:40px 0 56px">{hook}</div>{o}'
            f'<div class="p" style="color:{ink};opacity:.9;margin-top:24px">{foot}</div></div></div>')


def bts(kick, hook, lab, body, foot):
    return (BASE + f'<div class="slide" style="background:#FFF8EF">{chip()}<div class="box" style="top:430px"><span class="k">{kick}</span>'
            f'<div class="h" style="font-size:104px;color:#2A2238;margin:36px 0 48px">{hook}</div>'
            f'<div class="card"><span class="lab">{lab}</span><div>{body}</div></div>'
            f'<div class="p" style="color:#2A2238;margin-top:44px">{foot}</div></div></div>')


def newpost(tile, line, bg="#5E54C9"):
    src = (FEED / tile).as_uri()
    return (BASE + f'<div class="slide" style="background:{bg}">{chip()}<div class="box" style="top:420px;text-align:center">'
            f'<span class="k">New post</span>'
            f'<img src="{src}" style="display:block;margin:44px auto 0;width:640px;height:800px;border-radius:28px;'
            f'box-shadow:0 30px 60px rgba(20,10,60,.35);transform:rotate(-2deg)">'
            f'<div class="h" style="font-size:76px;color:#fff;margin-top:60px">{line}</div></div></div>')


S = {
    # Mon Oct 19
    "hb-st-1019-1": question("#5E54C9", "#fff", "Morning question", "How many unread emails <span class='yl'>right now?</span>",
                             [("A", "Under 10"), ("B", "10 to 100"), ("C", "Don’t ask")], "Reply with A, B or C."),
    "hb-st-1019-2": bts("Behind the scenes", "We ran it <span class='yl'>for real.</span>", "Our check",
                        "A 255-word email (made up). The AI found 3 asks and quoted each line.<br><span class='q'>All 3 quotes matched.</span>",
                        "That’s the rule here: real runs, real checks."),
    "hb-st-1019-3": newpost("hb-1019-single-group-chat/01.jpg", "Send this to the group chat."),
    "hb-st-1019-4": question("#FFF8EF", "#2A2238", "This or that", "Your group chat <span class='yl'>plans by…</span>",
                             [("A", "47 messages"), ("B", "One person just books it")], "Reply A or B. No judgement."),
    # Tue Oct 20
    "hb-st-1020-1": question("#FFF8EF", "#2A2238", "Be honest", "Sorries in your last email?",
                             [("A", "0"), ("B", "1"), ("C", "4 or more")], "Reply with the number."),
    "hb-st-1020-2": bts("Behind the scenes", "31 words. <span class='yl'>Under 40.</span>", "Our check",
                        "We asked for a calm reply to a neighbour, under 40 words. It wrote 31, owned it and said sorry once.",
                        "Text made up. Reply from a real AI run."),
    "hb-st-1020-3": newpost("hb-1020-single-stopped-doing/01.jpg", "What would be on your list?"),
    "hb-st-1020-4": question("#5E54C9", "#fff", "Your turn", "One thing you’d <span class='yl'>stop doing?</span>",
                             [("✓", "Reading the whole renewal"), ("✓", "Rewriting one text 5 times"), ("✓", "Something else")],
                             "Reply with yours."),
    # Wed Oct 21
    "hb-st-1021-1": question("#5E54C9", "#fff", "Morning question", "Ever had a <span class='yl' style='white-space:nowrap'>too-good</span> brand email?",
                             [("A", "Yes, it was a scam"), ("B", "Yes, it was real"), ("C", "Not yet")], "Reply A, B or C."),
    "hb-st-1021-2": newpost("hb-1021-ai-said-what-bill/01.jpg", "Did it split the bill right?"),
    "hb-st-1021-3": bts("Behind the scenes", "We did the math <span class='yl'>too.</span>", "Our check",
                        "Made-up statement, 16 lines. The AI flagged 5 subscriptions: <span class='q'>12.99 + 2.99 + 9.99 + 45.00 + 7.50 = 78.47.</span> Matches.",
                        "New post at 5:45 pm."),
    "hb-st-1021-4": question("#FFF8EF", "#2A2238", "Tonight’s Reel", "Weather costume: <span class='yl'>who are you?</span>",
                             [("☀", "Sun"), ("☂", "Rain"), ("☁", "Fog"), ("⚡", "Lightning")], "Reply with one."),
}
if __name__ == "__main__":
    render_many([(h, OUT / k) for k, h in S.items()], size=(1080, 1920), jpg_q=92)

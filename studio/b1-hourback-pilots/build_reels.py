#!/usr/bin/env python3
"""Hourback pilot Reels Oct 19-21 (agent B1). Mini-scenes in on-screen text; every 'after' is a real AI run
(runs/CAPTURE-LOG.md). Calm text (slowpan, code-made paper/blobs) for mornings + Oct 19 evening, kinetic (vlab 2x)
for the Oct 20/21 evenings and Oct 20 morning. Music: music2 'warm' via the engine. Covers: reels.cover_html + render_cover QA."""
import shutil, subprocess, sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/claude/content/oct16-21")
sys.path.insert(0, "/home/claude/content/video/src")
import reels as RL                     # noqa: E402  (registers engine, R, cover_html, build)
import reels_lib as L                  # noqa: E402
from reels_lib import Move, mark       # noqa: E402
from vlab import Video, el, count      # noqa: E402
import slowpan_bg as SBG               # noqa: E402
# Hourback has no 'blobs' palette in the engine yet: add one from the v4 Hourback colours (cream base, yellow/periwinkle/peach).
SBG.PAL["hourback"].setdefault("base", "#FFF8EF")
SBG.PAL["hourback"].setdefault("blobs", ["#FFC94D", "#C9C1F2", "#FFB27A", "#E3DDFA", "#FFE2B4"])

OUT = Path("/home/claude/hb-pilots/out/reels"); OUT.mkdir(parents=True, exist_ok=True)
foot = lambda: RL.foot("hourback")
css = RL.hbp + """
.pc .row{margin:14px 0}.pc .q{color:#FFC94D}
.pc .fine{font:600 36px/1.3 Inter;opacity:.85;margin-top:22px}
.mk{background:#FFC94D;color:#2A2238;border-radius:.12em;padding:0 .08em}
.wcard{position:absolute;left:84px;right:84px;background:#fff;border-radius:40px;padding:44px 50px;color:#2A2238;
 box-shadow:0 20px 44px rgba(60,40,140,.18);font:500 50px/1.38 Inter}
.wcard .lab{display:inline-block;font:800 28px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:#fff;background:#5E54C9;
 padding:12px 18px;border-radius:999px;margin-bottom:22px}
.so{background:#FF8A3D;color:#fff;border-radius:.14em;padding:0 .1em}
.s.sm{font-size:42px;opacity:.85}
"""

# ------------------------------------------------------------------ calm text 1 · Mon Oct 19 08:45 · just the asks (r1)
RL.R["hb-reel-1019am-just-the-asks"] = dict(brand="hourback", style="calm text", scenes=lambda: RL.gen_reel(
    "hourback", "paper",
    [f'<div class="c" style="top:400px"><span class="k">255 words · subject: please read!</span></div>'
     f'<div class="c big" style="top:500px">8:47 am. <span class="yl">The building email.</span></div>'
     f'<div class="c s" style="top:900px">What do they actually want from me?</div>{foot()}',
     '<div class="pc" style="top:380px"><span class="lab">The AI’s 3 asks · our summary</span>'
     '<div class="row"><span class="q">Tue, 7 am:</span> car out of the lot</div>'
     '<div class="row"><span class="q">Fri Oct 23:</span> name tag on your bike</div>'
     '<div class="row"><span class="q">Oct 31:</span> reply if you’ll help (optional)</div></div>'
     '<div class="wcard" style="top:1010px;font-size:40px;padding:30px 40px"><span class="lab">The check · quote vs email ✓</span>'
     '<div>“please make sure your car is out of the lot by 7 am Tuesday”</div></div>',
     f'<div class="c big" style="top:470px">Car moved. <span class="yl">Bike tagged.</span></div>'
     f'<div class="c s" style="top:820px">Every quote checked.</div>'
     f'<div class="c s sm" style="top:1020px">Email made up. Prompt in the caption.</div>{foot()}'],
    css, [Move(pan=0.02, push=0.02), Move(pan=-0.02), Move(pan=0.02, push=0.02)], seeds=(141, 142, 143)),
    cover=dict(kind="paper", kicker="255 words · 3 asks", hook="8:47 am. <span class='yl' style='white-space:nowrap'>The building</span> <span class='yl'>email.</span>"))

# ------------------------------------------------------------------ calm text 2 · Mon Oct 19 19:00 · one sorry (r2)
RL.R["hb-reel-1019-one-sorry"] = dict(brand="hourback", style="calm text", scenes=lambda: RL.gen_reel(
    "hourback", "blobs",
    [f'<div class="c" style="top:400px"><span class="k">Things I stopped doing</span></div>'
     f'<div class="c big" style="top:500px">Saying sorry <span class="yl">4 times</span> in one email.</div>{foot()}',
     '<div class="wcard" style="top:380px"><span class="lab">My draft · made up</span><div>'
     '<span class="so">So sorry</span> for the late reply!! I’m <span class="so">really sorry</span>, things have been a bit crazy '
     'this week. <span class="so">Sorry again.</span> I’ll send the photos by Friday if that’s ok? <span class="so">Sorry</span> '
     'for the trouble and thanks for being patient!</div></div>',
     '<div class="pc" style="top:380px"><span class="lab">Real AI rewrite</span><div>Sorry for the late reply, things have been '
     'a bit crazy this week. I’ll send the photos by Friday, if that works. Thanks so much for being patient!</div></div>'
     f'<div class="c big" style="top:1010px;font-size:96px">4 sorries → <span class="yl">1.</span></div>'
     f'<div class="c s sm" style="top:1150px">Same promise. Less grovel.</div>'],
    css, [Move(pan=0.02, push=0.02), Move(pan=-0.02), Move(pan=0.02, push=0.01)], seeds=(151, 152, 153), durs=(4.5, 5.5, 6.0)),
    cover=dict(kind="paper", kicker="Things I stopped doing", hook="Saying sorry <span class='yl' style='white-space:nowrap'>4 times.</span>", sub="In one email"))

# ------------------------------------------------------------------ calm text 3 · Wed Oct 21 08:45 · the brand email (r5)
RL.R["hb-reel-1021am-brand-email"] = dict(brand="hourback", style="calm text", scenes=lambda: RL.gen_reel(
    "hourback", "paper",
    [f'<div class="c" style="top:400px"><span class="k">POV: you post online</span></div>'
     f'<div class="c big" style="top:500px">A brand offers you <span class="yl">$2,000.</span></div>'
     f'<div class="c s" style="top:900px">For one Reel. “Reply within 24 hours.”</div>{foot()}',
     '<div class="pc" style="top:380px"><span class="lab">Real AI reply · trimmed</span><div style="margin-bottom:10px">“No, this looks like a scam.”</div>'
     '<div class="row">1. <span class="q">“enter your Instagram login”</span></div>'
     '<div class="row">2. <span class="q">“pay a $49 refundable onboarding fee”</span></div>'
     '<div class="row">3. <span class="q">“download our creator app”</span></div>'
     '<div class="row">4. <span class="q">“reply within 24 hours”</span></div></div>',
     f'<div class="c big" style="top:450px">Never share your login. <span class="yl">Never pay to get paid.</span></div>'
     f'<div class="c s sm" style="top:1040px">Email and brand made up. Prompt in the caption.</div>{foot()}'],
    css, [Move(pan=0.02, push=0.02), Move(pan=-0.02), Move(pan=0.02, push=0.02)], seeds=(161, 162, 163)),
    cover=dict(kind="paper", kicker="POV: a brand emails you", hook="$2,000 for <span class='yl'>one Reel?</span>", sub="Check it first"))

# ------------------------------------------------------------------ kinetic theme
TH = """
:root{--bg:#FFF8EF;--hl:#FFC94D;--hl-dark:#FFC94D;--prog-bg:transparent;--prog-fg:transparent;--strike:#FF8A3D}
.cam{transform:none!important}
.H{font-family:Poppins;font-weight:700;letter-spacing:-.035em;line-height:1.04;color:#2A2238}
.dark .H{color:#fff}
.B{font:600 54px/1.28 Inter;color:#2A2238}.dark .B{color:#FFF8EF}
.fine{font:600 38px/1.3 Inter;color:#6A6080}.dark .fine{color:#E4DDF5}
.kick{display:inline-block;font:800 30px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:#2A2238;background:#FFC94D;padding:14px 22px;border-radius:999px}
.yl{background:linear-gradient(#FFC94D,#FFC94D) no-repeat 0 88%/100% 46%;padding:0 .06em}
.dark .yl{color:#2A2238;background:#FFC94D;border-radius:.12em}
.pc{background:#5E54C9;border-radius:40px;padding:44px 50px;color:#fff;font:600 52px/1.32 Inter;box-shadow:0 20px 44px rgba(60,40,140,.28)}
.lab{display:inline-block;font:800 26px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:#2A2238;background:#FFC94D;padding:10px 16px;border-radius:999px;margin-bottom:20px}
.res{background:#fff;border-radius:36px;padding:26px 44px;box-shadow:0 16px 36px rgba(60,40,140,.16)}
.r{display:flex;gap:20px;font:600 40px/1.25 Inter;color:#2A2238;padding:14px 0;border-bottom:3px dashed #E4DDF5}
.r:last-child{border:0}.r b{flex:none;width:170px;color:#5E54C9}
.notif{background:rgba(255,255,255,.96);border-radius:38px;padding:30px 36px;box-shadow:0 18px 40px rgba(60,40,140,.2);font:500 44px/1.34 Inter;color:#2A2238}
.notif .hd{display:flex;justify-content:space-between;font:700 30px/1 Inter;color:#6A6080;margin-bottom:14px}
.mail{background:#fff;border-radius:36px;padding:40px 44px;box-shadow:0 16px 36px rgba(60,40,140,.16);font:500 46px/1.4 Inter;color:#2A2238}
.bub{display:inline-block;font:600 46px/1.22 Inter;padding:18px 28px;border-radius:32px;background:#fff;color:#2A2238;box-shadow:0 8px 18px rgba(60,40,140,.14);border-bottom-left-radius:10px}
.bub i{display:block;font:800 22px/1 Inter;font-style:normal;letter-spacing:.12em;text-transform:uppercase;color:#5E54C9;margin-bottom:8px}
.me{background:#FFC94D;border-bottom-left-radius:32px;border-bottom-right-radius:10px}
.ctr{font:800 34px/1 Inter;color:#fff;background:#FF8A3D;padding:12px 22px;border-radius:999px;display:inline-block}
.tab{display:inline-block;font:700 40px/1 Inter;background:#fff;color:#2A2238;border-radius:18px 18px 0 0;padding:22px 28px;margin-right:10px;box-shadow:0 -4px 14px rgba(60,40,140,.1)}
#tag{position:absolute;left:84px;top:300px;display:flex;align-items:center;gap:12px;background:#fff;border-radius:999px;padding:6px 22px 6px 6px;font:700 28px/1 Inter;color:#2A2238}
#tag img{width:46px;height:46px;border-radius:50%}
"""
TAG = f'<div id="tag"><img src="{mark("hourback")}">Hourback</div>'
X, W = 84, 912


def kin_driveway():
    v = Video("hourback", "driveway", TH, TAG)
    v.scene(0, 3.6, "".join([
        el('7:52 am. <span class="yl">The neighbour text.</span>', X, 420, W, a="none", cls="H", style="font-size:128px"),
        el('<div class="notif"><div class="hd"><span>Neighbour</span><span>now</span></div>Hi, not sure if you realise but a car '
           'was blocking our driveway again this morning. Some of us have to get to work…</div>', X, 900, W, a="up", t=0.6, d=0.5),
        el('Your guest’s car. You didn’t know.', X, 1320, W, a="fade", t=1.8, cls="B"),
    ]), tin="cut", bg="#FFF8EF")
    v.scene(3.6, 7.4, "".join([
        el('<span class="lab">My draft 1 · made up</span>', X, 420, a="up", t=0.05),
        el('<div class="mail"><span style="text-decoration:line-through;text-decoration-color:#FF8A3D;text-decoration-thickness:5px">SO sorry!!! It will NEVER happen '
           'again, I feel terrible, I’m so so sorry…</span></div>', X, 500, W, a="up", t=0.2),
        el('Too much.', X, 1000, W, a="up", t=2.1, cls="H", style="font-size:110px"),
    ]), tin="wipe", bg="#FFF8EF")
    v.scene(7.4, 11.8, "".join([
        el('<span class="lab">Real AI reply</span>', X, 420, a="up", t=0.05),
        el('<div class="pc">Hi, thanks for letting me know. That was my guest, and I didn’t realise they’d blocked you. Sorry about '
           'that. They’ve gone now, and I’ll make sure it doesn’t happen again.</div>', X, 500, W, a="up", t=0.2, d=0.5),
        el('31 words. One sorry. Owned it.', X, 1180, W, a="fade", t=1.2, cls="B"),
    ]), tin="wipe", bg="#FFF8EF")
    v.scene(11.8, 15.2, "".join([
        el('Sent. <span class="yl">Still friends.</span>', X, 460, W, a="up", t=0.05, cls="H", style="font-size:140px"),
        el('Text made up. Prompt in the caption.<br>Follow <b style="color:#FFC94D">@hourbackhq</b>', X, 1060, W, a="up", t=0.8, cls="B"),
    ]), tin="wipe", bg="#5E54C9", cls="dark")
    return v


def kin_blender():
    v = Video("hourback", "blender", TH, TAG)
    v.scene(0, 3.6, "".join([
        el('11:02 pm.<br>3 tabs. <span class="yl" style="white-space:nowrap">3 blenders.</span>', X, 420, W, a="none", cls="H", style="font-size:124px"),
        el('<span class="tab">Blender A</span><span class="tab">Blender B</span><span class="tab">Blender C</span>', X, 900, W, a="up", t=0.5),
        el('All say “best seller”.', X, 1060, W, a="up", t=1.5, cls="B"),
    ]), tin="cut", bg="#FFF8EF")
    v.scene(3.6, 7.6, "".join([
        el('<span class="lab">Specs · made up</span>', X, 420, a="up", t=0.05),
        el('<div class="res"><div class="r" data-a="up" data-t="0.25" data-d="0.4"><b>A $89</b>1000 W · glass · 2 yr · 88 dB</div>'
           '<div class="r" data-a="up" data-t="0.55" data-d="0.4"><b>B $129</b>1200 W · plastic · 7 yr · 95 dB</div>'
           '<div class="r" data-a="up" data-t="0.85" data-d="0.4"><b>C $74</b>900 W · small · 1 yr · 85 dB</div></div>', X, 500, W, a="none"),
        el('Smoothies for 2 most mornings. Soup sometimes.', X, 1060, W, a="fade", t=1.4, cls="B"),
    ]), tin="wipe", bg="#FFF8EF")
    v.scene(7.6, 11.8, "".join([
        el('<span class="lab">Real AI reply · trimmed</span>', X, 420, a="up", t=0.05),
        el('<div class="pc">“Get Blender A: it’s the best balance of price, power, and quietness for daily smoothies for two '
           'plus occasional soup.”</div>', X, 500, W, a="up", t=0.2, d=0.5),
        el('Bonus: “glass jar handles hot soup well.”', X, 1060, W, a="fade", t=1.3, cls="B"),
    ]), tin="wipe", bg="#FFF8EF")
    v.scene(11.8, 15.2, "".join([
        el('3 tabs <span class="yl">closed.</span>', X, 460, W, a="up", t=0.05, cls="H", style="font-size:140px"),
        el('Decision made.', X, 800, W, a="up", t=0.4, cls="B"),
        el('Check the specs on the shop page first. Prompt in the caption.', X, 1040, W, a="up", t=0.8, cls="B"),
    ]), tin="wipe", bg="#5E54C9", cls="dark")
    return v


CHAT = [l.split(": ", 1) for l in open("/home/claude/hb-pilots/runs/chat-costume.txt").read().strip().split("\n")]


def chat_block(rows, t0=0.1, st=0.22):
    h = ""
    for k, (who, msg) in enumerate(rows):
        h += (f'<div data-a="up" data-t="{t0 + k * st:.2f}" data-d="0.3" style="margin:0 0 14px"><span class="bub">'
              f'<i>{who}</i>{msg}</span></div>')
    return h


def kin_costume():
    v = Video("hourback", "costume", TH, TAG)
    v.scene(0, 3.0, "".join([
        el('6 friends.<br>1 costume.<br><span class="yl">63 messages.</span>', X, 420, W, a="none", cls="H", style="font-size:128px"),
        el('Group chat, Halloween week.', X, 1060, W, a="fade", t=1.0, cls="B"),
    ]), tin="cut", bg="#FFF8EF")
    idx = [0, 4, 13, 24, 37, 58, 62]
    s = 9.4
    v.scene(3.0, s, "".join([
        count(0, 63, fmt="{:,.0f} messages", t=0.1, d=5.6, cls="ctr", x=X, y=410),
        el(chat_block([CHAT[i] for i in idx], t0=0.15, st=0.8), X, 500, W, a="none"),
    ]), tin="wipe", bg="#EDE8FA")
    v.scene(s, s + 4.2, "".join([
        el('<span class="lab">The AI’s pick, as a table</span>', X, 410, a="up", t=0.05),
        el('Theme: <span class="yl">weather.</span>', X, 480, W, a="up", t=0.2, cls="H", style="font-size:104px"),
        el('<div class="res">' + "".join(
            f'<div class="r" data-a="up" data-t="{0.45 + k * 0.22:.2f}" data-d="0.35"><b>{a}</b>{b}</div>' for k, (a, b) in enumerate([
                ("Priya", "rain · yellow raincoat"), ("Theo", "cloud · white sheet"), ("Mila", "sun · peach dress"),
                ("Kai", "lightning · zigzag shirt"), ("Sam", "fog · grey hoodie"), ("Jonah", "fog machine (or wind)")])) + '</div>',
           X, 640, W, a="none"),
    ]), tin="wipe", bg="#FFF8EF")
    s2 = s + 4.2
    v.scene(s2, s2 + 3.4, "".join([
        el('Decided in<br><span class="yl">1 message.</span>', X, 460, W, a="up", t=0.05, cls="H", style="font-size:140px"),
        el('Jonah: “ok but what if pirates”', X, 820, W, a="up", t=0.5, cls="B"),
        el('Chat made up. Prompt in the caption.', X, 1060, W, a="up", t=0.9, cls="fine"),
    ]), tin="wipe", bg="#5E54C9", cls="dark")
    return v


RL.R["hb-reel-1020am-driveway-text"] = dict(brand="hourback", style="kinetic big text", kinetic=kin_driveway,
    cover=dict(kind="kin", kicker="7:52 am", hook="<span style='display:block;line-height:1.16'>The neighbour <span class='yl'>text.</span></span>", sub="Reply in 31 words"))
RL.R["hb-reel-1020-three-tabs"] = dict(brand="hourback", style="kinetic big text", kinetic=kin_blender,
    cover=dict(kind="kin", kicker="11:02 pm", hook="<span style='display:block;line-height:1.16'>3 tabs.<br><span style='white-space:nowrap'>1 <span class='yl'>blender.</span></span></span>", sub="Pick in one message"))
RL.R["hb-reel-1021-group-costume"] = dict(brand="hourback", style="kinetic big text", kinetic=kin_costume,
    cover=dict(kind="kin", kicker="Group chat vs AI", hook="<span style='display:block;line-height:1.16'>6 friends.<br><span class='yl'>1 costume.</span></span>", sub="63 messages. AI: one line."))

IDS = ["hb-reel-1019am-just-the-asks", "hb-reel-1019-one-sorry", "hb-reel-1020am-driveway-text", "hb-reel-1020-three-tabs",
       "hb-reel-1021am-brand-email", "hb-reel-1021-group-costume"]

if __name__ == "__main__":
    import json
    for rid in (sys.argv[1:] or IDS):
        qa = RL.build(rid)
        mp4 = L.OUT / f"{rid}.mp4"
        shutil.copy(mp4, OUT / mp4.name)
        shutil.copy(L.OUT / f"{rid}-cover.jpg", OUT / f"{rid}-cover.jpg")
        shutil.copy(L.QA / f"{rid}-sheet.png", OUT / f"{rid}-sheet.png")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp4), "-c:v", "copy", "-an", str(OUT / f"{rid}-nomusic.mp4")], check=True)
        (OUT / f"{rid}.qa.json").write_text(json.dumps(qa, indent=1, default=str))

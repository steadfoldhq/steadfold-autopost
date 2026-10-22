#!/usr/bin/env python3
"""Static pieces for the Littlefold sunlit rebuild: Reel covers, the 3-slide crying-peak carousel, the Story hand-off."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from sunart import *  # noqa

OUT = REPO / "media" / "recovery-oct22b" / "littlefold"
OUT.mkdir(parents=True, exist_ok=True)
GARMENTS = ["onesie", "sock", "bib", "hat", "dress"]
XS = [150, 345, 540, 735, 930]


def washing_line(n=5, y0=300, sag=50, W=1080, H=1920, xs=XS, kinds=GARMENTS, scale=1.0, rots=None):
    s = line_svg(W, H, y0, sag)
    g = ""
    gw = int(150 * scale)
    for i in range(n):
        x = xs[i]
        y = line_y(x, y0, sag, W)
        r = (rots or [-4, 3, -2, 4, -3])[i]
        g += (f'<div style="position:absolute;left:{x - gw/2:.0f}px;top:{y - 14*gw/170:.0f}px;width:{gw}px;transform-origin:50% 6%;transform:rotate({r}deg)">'
              f'{garment_svg(kinds[i], gw)}</div>')
    return f'<div style="position:absolute;left:0;top:0">{s}</div>{g}'


def scene(W, H, kind="dawn", sun_y=1440, awake=False, n=5, y0=300, hills_top=1460, cloud_y=(150, 230), rays=True, line=True):
    sx = W / 2
    body = sky(W, H, kind, horizon=(hills_top + 20) / H)
    if rays:
        body += f'<div style="position:absolute;left:{sx-750:.0f}px;top:{sun_y-750}px;opacity:.75">{rays_svg(1500)}</div>'
    body += f'<div style="position:absolute;left:{sx-260:.0f}px;top:{sun_y-260}px">{sun_svg(520, awake)}</div>'
    body += f'<div style="position:absolute;left:0;top:0">{hills_svg(W, H, top=hills_top)}</div>'
    body += f'<div style="position:absolute;left:-60px;top:{cloud_y[0]}px;opacity:.95">{cloud_svg(360)}</div>'
    body += f'<div style="position:absolute;left:{W-330}px;top:{cloud_y[1]}px;opacity:.9">{cloud_svg(300)}</div>'
    if line:
        body += washing_line(n, y0=y0, W=W, H=H)
    return body


def chip(text, top, left=None, size=30):
    if left is None:
        return f'<div style="position:absolute;left:0;right:0;top:{top}px;text-align:center"><span class="chipf" style="font-size:{size}px">{text}</span></div>'
    return f'<div style="position:absolute;left:{left}px;top:{top}px"><span class="chipf" style="font-size:{size}px">{text}</span></div>'


def reel_cover(c, out, kind="morning", awake=True):
    W, H = 1080, 1920
    body = (scene(W, H, kind, sun_y=c.get("sun_y", 1375), awake=awake)
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:560px;font-size:76px;color:{KICK}">{c["kick"]}</div>'
            + K.dual(c["head"], F, cls="S fit", style=f"position:absolute;left:100px;width:880px;top:660px;font-size:{c.get('fs', 168)}px;color:{INK}")
            + (f'<div class="lora" style="position:absolute;left:120px;width:840px;top:{c.get("sy", 1170)}px;font-size:60px;text-align:center;color:{INK}">{c["sub"]}</div>' if c.get("sub") else "")
            + (f'<div style="position:absolute;left:0;right:0;top:1290px;text-align:center"><span style="display:inline-block;padding:10px 28px;border-radius:99px;background:#FF8A70;color:#FFF8EE;font:600 30px Poppins;letter-spacing:.16em">{c["pill"]}</span></div>' if c.get("pill") else "")
            + K.stamp(B, 66, 1380, size=150, rot=-10))
    return render(page(W, H, body), out, W, H)


# ---------------------------------------------------------------- carousel: the crying has a peak
def peak_hill(W=1080, top=760):
    """The 'peak' as a soft pastel hill to walk over: path up, a little flag at the top, sunlit far side with flowers."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="590" viewBox="0 0 1080 590" style="position:absolute;left:0;top:{top}px">
<defs><linearGradient id="hl" x1="0" x2="1"><stop offset="0" stop-color="#FFC9D9"/><stop offset=".55" stop-color="#FFD2C0"/><stop offset="1" stop-color="#FFE7B0"/></linearGradient></defs>
<path d="M-10 590 L-10 470 C 160 450 300 300 430 170 C 480 122 560 118 610 168 C 720 290 860 420 1090 440 L1090 590 Z" fill="url(#hl)" stroke="{PLUM}" stroke-width="5" stroke-linejoin="round"/>
<path d="M-10 520 C 140 505 300 380 420 250 C 470 200 560 196 610 246 C 730 360 880 470 1090 480" stroke="#FFF8EE" stroke-width="10" fill="none" stroke-dasharray="2 24" stroke-linecap="round"/>
<g transform="translate(518 128)"><path d="M0 0 V-92" stroke="{PLUM}" stroke-width="6" stroke-linecap="round"/><path d="M0 -92 L58 -76 L0 -58 Z" fill="{BUTTER}" stroke="{PLUM}" stroke-width="4" stroke-linejoin="round"/></g>
<path d="M-10 590 L-10 540 C 300 520 700 560 1090 520 L1090 590 Z" fill="#BCD7AE"/>
{''.join(f'<g transform="translate({x} {y})"><path d="M0 0 v22" stroke="#8DB07F" stroke-width="3"/>' + ''.join(f'<circle cx="{9*math.cos(k*1.2566):.1f}" cy="{9*math.sin(k*1.2566):.1f}" r="6" fill="{c}"/>' for k in range(5)) + '<circle r="4.5" fill="#F2A94B"/></g>' for x, y, c in [(800, 420, '#FFF4D6'), (870, 440, '#FFB9CF'), (950, 436, '#FFF4D6'), (1020, 446, '#FFE08A'), (900, 500, '#FFC8A8'), (990, 500, '#FFB9CF'), (720, 380, '#FFB9CF')])}
</svg>"""


def peak_slides():
    W, H = 1080, 1350
    common_foot = (f'<div class="pop" style="position:absolute;left:66px;top:1270px;font-size:24px;color:{INK}">@littlefoldhq</div>'
                   + K.stamp(B, 896, 1176, size=130, rot=-10))
    # slide 1: the peak
    s1 = (sky(W, H, "dawn", haze_y=0.22, horizon=0.62)
          + f'<div style="position:absolute;left:730px;top:540px">{sun_svg(400, awake=True)}</div>'.replace('<svg', '<svg style="width:400px;height:400px"')
          + f'<div style="position:absolute;left:-40px;top:60px;opacity:.9">{cloud_svg(260)}</div>'
          + f'<div style="position:absolute;left:830px;top:240px;opacity:.85">{cloud_svg(220)}</div>'
          + f'<div class="kick" style="top:84px;font-size:24px;color:{PLUM}">THE NEWBORN WEEKS</div>'
          + f'<div class="pop" style="position:absolute;right:56px;top:76px;font-size:24px;color:{PLUM}">1/3</div>'
          + K.dual("The crying / has a *peak.*", F, cls="S fit", style=f"position:absolute;left:90px;width:900px;top:150px;font-size:136px;color:{INK}")
          + f'<div class="lora" style="position:absolute;left:110px;width:860px;top:445px;font-size:44px;line-height:1.25;text-align:center;color:{INK}">Often somewhere around 3 to 12 weeks.<br>Usually over by 3 to 4 months.</div>'
          + peak_hill(top=700)
          + f'<div class="hand" style="position:absolute;left:250px;width:330px;top:645px;font-size:44px;color:{KICK};transform:rotate(-4deg)">the peak: often<br>3 to 12 weeks</div>'
          + f'<div class="hand" style="position:absolute;left:660px;width:380px;top:880px;font-size:42px;color:{KICK};transform:rotate(-3deg)">usually over by<br>3 to 4 months</div>'
          + chip("CPS · Colic and crying", 1190, left=60, size=26)
          + common_foot)
    # slide 2: what helps, in order
    rows = [("onesie", "Check first:", "hungry, wet diaper, too hot or cold, fever."),
            ("bib", "Hold them.", "You can't spoil a baby by picking them up."),
            ("hat", "Calm it down:", "dim the lights, shush, sway, or walk them close to you.")]
    rr = ""
    for i, (g, b, t) in enumerate(rows):
        y = 560 + i * 190
        rr += (f'<div style="position:absolute;left:96px;top:{y-6}px;width:120px">{garment_svg(g, 120)}</div>'
               f'<div style="position:absolute;left:150px;top:{y+60}px;width:44px;height:44px;border-radius:50%;background:{INK};color:#FFF8EE;font:600 26px Poppins;display:flex;align-items:center;justify-content:center">{i+1}</div>'
               f'<div style="position:absolute;left:250px;top:{y+8}px;width:740px;font-size:40px;line-height:1.28;color:{INK}"><span class="lora" style="font-size:44px">{b}</span> <span class="pop" style="font-weight:400">{t}</span></div>')
    s2 = (sky(W, H, "morning", haze_y=0.45, horizon=0.95)
          + f'<div style="position:absolute;left:-40px;top:40px;opacity:.9">{cloud_svg(240)}</div>'
          + f'<div style="position:absolute;left:860px;top:70px;opacity:.85">{cloud_svg(200)}</div>'
          + f'<div class="kick" style="top:84px;font-size:24px;color:{PLUM}">WHAT HELPS, IN ORDER</div>'
          + f'<div class="pop" style="position:absolute;right:56px;top:76px;font-size:24px;color:{PLUM}">2/3</div>'
          + K.dual("Check first. / Then *hold close.*", F, cls="S fit", style=f"position:absolute;left:90px;width:900px;top:300px;font-size:120px;color:{INK}")
          + f'<div class="card" style="left:66px;top:530px;width:948px;height:590px"></div>'
          + rr
          + chip("CPS · Colic and crying", 1190, left=60, size=26)
          + common_foot)
    # slide 3: do this (full morning, sun awake)
    s3 = (scene(W, H, "morning", sun_y=1160, awake=True, line=False, hills_top=1180, cloud_y=(40, 90))
          + f'<div class="kick" style="top:84px;font-size:24px;color:{PLUM}">DO THIS</div>'
          + f'<div class="pop" style="position:absolute;right:56px;top:76px;font-size:24px;color:{PLUM}">3/3</div>'
          + K.dual("Next cry: / *check first,* / then *hold close.*", F, cls="S fit", style=f"position:absolute;left:90px;width:900px;top:160px;font-size:124px;color:{INK}")
          + f'<div class="card" style="left:96px;top:600px;width:888px;height:330px;padding:34px 40px">'
            f'<div class="pop" style="font-size:34px;line-height:1.35;color:{INK}"><b style="font-weight:600">Too much?</b> Put baby in their crib, step out and take a moment. It\'s OK to ask for help.</div>'
            f'<div style="height:2px;background:{PLUM};opacity:.3;margin:22px 0"></div>'
            f'<div class="pop" style="font-size:34px;line-height:1.35;color:{INK}"><b style="font-weight:600">Under 3 months with a fever?</b> Get care right away.</div></div>'
          + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:975px;font-size:58px;color:{KICK};transform:rotate(-3deg)">save this for 3 am</div>'
          + chip("CPS · Colic and crying", 1190, left=60, size=26)
          + common_foot)
    outs = []
    for i, s in enumerate([s1, s2, s3], 1):
        p = OUT / f"crying-peak-sun-0{i}.jpg"
        render(page(W, H, s), p, W, H)
        outs.append(p)
    return outs


def story():
    W, H = 1080, 1920
    mini = Image.open(OUT / "crying-peak-sun-01.jpg")
    mp = SCR / "mini.png"
    mini.save(mp)
    body = (scene(W, H, "morning", sun_y=1500, awake=True, n=3, y0=250, hills_top=1520, cloud_y=(120, 180))
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:440px;font-size:66px;color:{KICK}">calmer newborn days</div>'
            + K.dual("It has / a *peak.*", F, cls="S fit", style=f"position:absolute;left:100px;width:880px;top:520px;font-size:170px;color:{INK}")
            + f'<img src="{mp.as_uri()}" style="position:absolute;left:300px;top:880px;width:480px;transform:rotate(-3deg);border-radius:22px;border:5px solid #FFF8EE;box-shadow:0 18px 30px rgba(107,59,90,.25)">'
            + f'<div class="hand" style="position:absolute;left:90px;width:900px;top:1530px;font-size:62px;color:{INK}">full breakdown in today\'s post ↑</div>'
            + K.stamp(B, 60, 1330, size=150, rot=-10))
    p = OUT / "story-lf-ch-1025-4-sun.jpg"
    render(page(W, H, body), p, W, H)
    return p


if __name__ == "__main__":
    what = sys.argv[1:] or ["covers", "feed", "story"]
    if "covers" in what:
        reel_cover(dict(kick="heard “you'll spoil her”?", head="You can't / *spoil* a / newborn.", sub="Pick them up."),
                   OUT / "lf-reel-1025am-cant-spoil-sun-cover.jpg", "morning", True)
        reel_cover(dict(kick="still crying? at your limit?", head="It's OK to / *step away.*", fs=180),
                   OUT / "lf-reel-1025-step-away-sun-cover.jpg", "afternoon", True)
    if "feed" in what:
        print(peak_slides())
    if "story" in what:
        print(story())

#!/usr/bin/env python3
"""Oct 26 (Social studio, Littlefold maker): three 2-frame Story chains (Tue Oct 27, Wed Oct 28, Thu Oct 29, 12:30 + 12:31).
Frame 1 = a rule-as-fact question; frame 2 = the plain answer + 'Tonight at 7 pm: the 15-second version' (each day has an
LF 7 pm Reel on the same topic: swaddle hips / neck check / tummy to play). Page look: Fraunces + pills, Caveat kicker,
stamp, a drawn object (same line style as the Reels), Warm Sherbet fields. All text inside y 250..1580.

    python3 studio/editorial/oct26_littlefold_stories.py
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import oct24_lf_a  # noqa: E402,F401  (adds babyBack, babyHand ... to RS.JS)
import oct26_littlefold as L  # noqa: E402  (RS.JS with the Oct 26 drawing functions)

RS, K, F, INK, KICK, B = L.RS, L.K, L.F, L.INK, L.KICK, L.B
import sunart as SA  # noqa: E402

W, H = 1080, 1920
OUT = L.OUT / "stories"

OBJ = {
    # swaddled baby seen from above-ish: bundle with legs bent up and out (frog position) + check
    "swaddle": "s=`<g transform='translate(540 1180) scale(1.25)'>`"
               "+[-1,1].map(g=>`<path d='M${30*g} 96 Q${120*g} 104 ${112*g} 150 Q${104*g} 186 ${46*g} 168' stroke='${PL}' stroke-width='46' fill='none' stroke-linecap='round'/><path d='M${30*g} 96 Q${120*g} 104 ${112*g} 150 Q${104*g} 186 ${46*g} 168' stroke='${PEACH}' stroke-width='36' fill='none' stroke-linecap='round'/><ellipse cx='${40*g}' cy='166' rx='22' ry='15' fill='#FFDCC4' ${o} stroke-width='4'/>`).join('')"
               "+bundle(0,0,0,1.0)+`</g>`+(F2?check(760,1110,1):'');",
    "neck": "s=`<g transform='translate(540 1270) scale(.95)'>`+babyBack(0,0,0,1.0)+`</g>`"
            "+(F2?`<g transform='translate(560 1160)'><circle r='34' fill='none' stroke='#B23A62' stroke-width='5'/><circle r='58' fill='none' stroke='#B23A62' stroke-width='4' opacity='.5'/></g>`+check(800,1120,1):"
            "`<g transform='translate(330 1150)'>`+babyHand(0,0,-8,0.6,[0,0,0,0],300)+`</g>`);",
    "tummy": "s=`<g transform='translate(540 1330)'>`+matSVG(600)+`</g><g transform='translate(560 1330)'>`+babyTummy(F2?0.9:0.4,0.2,1.2,true)+`</g>`"
             "+(F2?check(830,1130,1):'');",
}

STORIES = [
    ("lf-st-1027-1", "2026-10-27T12:30:00-04:00", "cream", "swaddling tonight?", "Swaddling: legs / *straight or bent?*", "", "Next Story →", "swaddle", False, ""),
    ("lf-st-1027-2", "2026-10-27T12:31:00-04:00", "pink", "hip-healthy swaddling", "Bent up / *and out.*",
     "Leave the blanket loose at the hips, so the legs can move.", "Tonight at 7 pm: the 15-second version", "swaddle", True, "AAP · HealthyChildren.org"),
    ("lf-st-1028-1", "2026-10-28T12:30:00-04:00", "cream", "before you grab a blanket", "Cold little hands. / *Add a layer?*", "", "Next Story →", "neck", False, ""),
    ("lf-st-1028-2", "2026-10-28T12:31:00-04:00", "pink", "the 5-second check", "No. Feel the / *back of the neck.*",
     "Cool hands and feet are normal. Hot or sweaty? Take a layer off.", "Tonight at 7 pm: the 15-second version", "neck", True, "NHS"),
    ("lf-st-1029-1", "2026-10-29T12:30:00-04:00", "cream", "new baby home?", "When can / *tummy time start?*", "", "Next Story →", "tummy", False, ""),
    ("lf-st-1029-2", "2026-10-29T12:31:00-04:00", "pink", "back to sleep, tummy to play", "The day you / *get home.*",
     "A few minutes at a time, only while baby's awake and you're watching.", "Tonight at 7 pm: the 15-second version", "tummy", True, "AAP · HealthyChildren.org"),
]


def html(sid, field, kick, head, sub, cta, obj, f2, src):
    fld = K.FIELDS[B][field]
    pf = dict(p1=fld["p1"], p2=fld["p2"])
    body = K.field_bg(fld)
    body += (f'<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><span style="display:inline-block;padding:10px 28px;'
             f'border:2.5px solid {INK};border-radius:99px;font:600 28px Fraunces;letter-spacing:.14em;color:{INK}">{'THE ANSWER · 2/2' if f2 else 'QUICK QUESTION · 1/2'}</span></div>')
    body += f'<div class="hand" style="position:absolute;left:90px;width:900px;top:430px;font-size:70px;color:{KICK}">{kick}</div>'
    body += K.dual(head, pf, cls="S fit", style=f"position:absolute;left:90px;width:900px;top:520px;white-space:nowrap;font-size:132px;color:{INK}")
    if sub:
        body += (f'<div class="lora" style="position:absolute;left:110px;width:860px;top:830px;font-size:46px;line-height:1.22;text-align:center;'
                 f'color:{INK}">{sub}</div>')
    body += f'<svg id="obj" style="position:absolute;left:0;top:0" width="{W}" height="{H}" viewBox="0 0 {W} {H}"></svg>'
    body += (f'<div style="position:absolute;left:0;right:0;top:1430px;text-align:center"><span style="display:inline-block;padding:14px 32px;'
             f'border-radius:99px;background:{INK};color:#FFF8EE;font:600 34px Poppins">{cta}</span></div>')
    if src:
        body += f'<div style="position:absolute;left:0;right:0;top:1520px;text-align:center;font:500 26px Fraunces;color:{INK};opacity:.75">Source: {src}</div>'
    body += K.stamp(B, 900, 268, size=130, rot=-10)
    js = RS.JS + f"\n;(function(){{const F2={'true' if f2 else 'false'}; let s=''; {OBJ[obj]} document.getElementById('obj').innerHTML=s;}})();"
    return SA.page(W, H, body + f"<script>{js}</script>")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for sid, at, field, kick, head, sub, cta, obj, f2, src in STORIES:
        out = OUT / f"{sid}.jpg"
        SA.render(html(sid, field, kick, head, sub, cta, obj, f2, src), out, W, H)
        print(out, flush=True)


if __name__ == "__main__":
    main()

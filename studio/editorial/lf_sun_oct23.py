#!/usr/bin/env python3
"""Oct 23 (Social studio): two Littlefold Reels in the queued 'sunshine washing-line' look (recovery-oct22c reel_story.py,
the founder's Oct 22 colour direction already used by the Sun Oct 25 items). The two story specs were drafted there
(car-seat coat, teething); here they ship WITHOUT the unapproved 'Little Rules' series pill (founder approval pending),
with a named send target on the last beat and the page's follow line. Facts: AAP HealthyChildren.org (checked Oct 23).

    python3 studio/editorial/lf_sun_oct23.py carseat|teething [--still=0,1,2]
"""
import os
import sys
from pathlib import Path
sys.dont_write_bytecode = True
os.environ.setdefault("LF_SCR", "/tmp/claude-0/lfsun")
sys.path.insert(0, "/home/claude/steadfold-autopost/studio/recovery-oct22c/littlefold")
import reel_story as RS  # noqa: E402

OUT = RS.REPO / "media" / "studio-oct23" / "littlefold"
FOLLOW = "Follow for one calm thing a night ☀"

c = RS.SPECS["carseat"]
c.update(out="lf-reel-1023-coat-off-buckle", outdir=OUT, follow=FOLLOW)
c["cover"] = dict(c["cover"], pill="")
c["beats"][2] = dict(c["beats"][2], head="Pinch the strap / at their chest. / *Extra? Tighten it.*", fs=126)
c["beats"][-1] = dict(c["beats"][-1], sub="send this to whoever does daycare drop-off")

t = RS.SPECS["teething"]
t.update(out="lf-reel-1026am-teething-cold-cloth", outdir=OUT, follow=FOLLOW)
t["cover"] = dict(t["cover"], pill="")
t["beats"][0] = dict(t["beats"][0], sub="Two simple things that help sore gums.")
# CD gate: one "skip" beat, not two (too many ideas for 15 s)
t["beats"][2] = dict(t["beats"][2], head="Skip teething / necklaces and / *numbing gels.*",
                     sub="Choking risk. Benzocaine gels can harm kids.", fs=124)
del t["beats"][3]
t["cover_beat"] = 3
RS.JS = RS.JS.replace("SC.teeth.special=", "SC.teeth.splice(3,1);SC.teeth.special=", 1)  # drop the gel vignette with its beat
t["durs"] = t["durs"][:3] + t["durs"][4:]
t["beats"][-1] = dict(t["beats"][-1], sub="Fever isn't a teething sign.<br>Call your baby's doctor.")

if __name__ == "__main__":
    for a in sys.argv:
        if a.startswith("--still="):
            RS.STILLS = [float(x) for x in a[8:].split(",")]
    for key in [a for a in sys.argv[1:] if not a.startswith("--")]:
        s = RS.SPECS[key]
        OUT.mkdir(parents=True, exist_ok=True)
        RS.frames(s, key, cover=s["cover"], cover_out=OUT / f"{s['out']}-cover.jpg")
        r = RS.frames(s, key)
        if r is None:
            print("stills", RS.SCR / f"{key}-stills.jpg")
            continue
        fdir, total, starts = r
        pops = [(st + 0.1, 0.22) for k, st in enumerate(starts) if k > 0 and k not in s.get("no_pop", [])] + s["extra_pops"]
        out = OUT / f"{s['out']}.mp4"
        RS.encode(fdir, total, s["music"], pops, out)
        print(out, round(total, 2), flush=True)

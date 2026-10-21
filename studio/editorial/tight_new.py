#!/usr/bin/env python3
"""Oct 21: fills tonight's empty Littlefold 7 pm Reel slot with a 3-beat cut of today's own lesson (Special Time, the
11:30 post), same facts and source. Built with the tight format (<= 15 s). Owner direction: minimal on screen, detail in caption.

    python3 studio/editorial/tight_new.py [--plan]
"""
import argparse, sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import teach_reels as T  # noqa: E402

LF = "littlefold"
NEW = {
    "lf-reel-1021-special-time-s15": dict(
        brand=LF, track="lf-x-tiny-parade", fmt="tight", save="send this to a busy parent",
        at="2026-10-21T19:00:00-04:00",
        scenes=[dict(k="hook", f="pink", text="Toddler pulling you / *to come play?*", emo="🧸"),
                dict(k="say", f="butter", text="Phones off. / Sit at *their level.* / *Follow their play.*", drop=True),
                dict(k="do", f="cream", text="Tonight: *10 minutes,* / they choose.")],
        caption=("Toddler pulling you to come play? Give them 10 minutes where they lead and you follow.\n\n"
                 "It's called Special Time, a tip NHS speech and language therapists give parents of toddlers.\n\n"
                 "THE SETUP: 10 minutes, at least 3 to 4 times a week. Phones, TV and music off. Sit at their level, face to face. "
                 "Your child picks the play: blocks, playdough, drawing, cars, dolls.\n\n"
                 "WHAT TO DO: say what you see (\"You're building a tall tower\"). Copy what they do. Praise the exact thing "
                 "(\"Gentle hands with the blocks!\"). More comments, fewer questions.\n\n"
                 "STOP AT 10: thank them, even if they want more. Doing it at the same time each day helps them know it's coming.\n\n"
                 "Do this: tonight, set a 10-minute timer and let them lead.\n\n"
                 "Send this to a parent who feels half there all day.\n\n"
                 "General information only, not medical advice.\n\n"
                 "#toddler #playtime #parenting #toddlermom #newparents"),
        comment=("Source: NHS Lothian, Let's Talk, Special Time (lets-talk.scot.nhs.uk): 10 minutes, at least 3-4 times a week; your "
                 "child chooses the activity (puzzles, building, playdough, drawing, dolls, cars) and leads; TV, devices and background "
                 "noise off; face to face at their level, undivided attention; use comments rather than lots of questions; stop at 10 "
                 "minutes even if they want more and thank your child; a predictable routine helps children know what to expect."),
    ),
}


def spec(rid):
    s = dict(NEW[rid], id=rid)
    s["scenes"] = [dict(s["scenes"][0], save=s.get("save"))] + s["scenes"][1:]
    return s


def check_len(spec, pr):
    want = T.make(spec).duration
    if abs(pr["dur"] - want) > 0.25:
        out = T.REPO / "media" / "reels"
        for x in (out / f"{spec['id']}.mp4", out / f"{spec['id']}-cover.jpg"):
            x.unlink(missing_ok=True)
        raise SystemExit(f"encoded {pr['dur']:.2f}s but planned {want:.2f}s (frames lost; disk?) -> removed")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--out", default="/tmp/tight-reels")
    ap.add_argument("--workers", type=int, default=1)
    a = ap.parse_args()
    for rid in NEW:
        sp = spec(rid)
        T.lint(sp)
        T.report(sp) if a.plan else check_len(sp, T.build(sp, a.out, a.workers))

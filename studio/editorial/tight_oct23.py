#!/usr/bin/env python3
"""Oct 23 (Social studio): five new <= 15 s 3-beat Reels (hook -> the idea in plain words -> "Do this"), the structure the
Performance desk ordered repeated (felt question + one rule with a number: LF toddler play, 5.6 s / 40% on 102).
Hooks picked by a fresh stranger-test subagent (3 options each). Every hook scene carries a named send target (desk test 3).
Facts checked Oct 23: Lullaby Trust (16-20 C, hats off indoors, check the chest / back of neck); Google Lens Translate;
WhatsApp voice message transcripts (Settings > Chats, Nov 2024, on-device); Milne, Orbell & Sheeran 2002 (BJHP 7:163-184);
rule of 72 is arithmetic (1.08^9 = 1.999).

    python3 studio/editorial/tight_oct23.py [ids...] [--plan]
"""
import argparse
import subprocess
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import teach_reels as T  # noqa: E402

LF, HB, FF, LH = "littlefold", "hourback", "fullyfunded", "lockedhour"
NEW = {
    "lf-reel-1024am-room-temp-s15": dict(
        brand=LF, track="lf-x-giggle-pop", save="send this to the night-feed partner",
        scenes=[dict(k="hook", f="pink", text="Baby's room / *feels cold tonight?*", emo="🌙"),
                dict(k="say", f="butter", kicker="the rule", text="Keep the room / *16 to 20°C.* / No hat in bed.", drop=True),
                dict(k="do", f="cream", text="Feel their *neck.* Sweaty? / One layer off.")]),
    "hb-reel-1024am-lens-translate-s15": dict(
        brand=HB, track="hb-x-ta-da-funk", save="send this to your travel buddy",
        scenes=[dict(k="hook", f="indi", text="Menu in / *another language?*", emo="📞"),
                dict(k="say", f="orng", kicker="try this", text="Point your / camera. / *Google Lens* / translates it.", drop=True),
                dict(k="do", f="plum", text="Google app: tap the *camera,* / then *Translate.*")]),
    "ff-reel-1026am-rule-of-72-s15": dict(
        brand=FF, track="ff-x-money-moves", save="send this to your “I'll start later” friend",
        scenes=[dict(k="hook", f="cob", text="How long until / *$10K is $20K?*", emo="⏳"),
                dict(k="say", f="coral", kicker="the rule of 72", text="72 ÷ the / yearly return. / *8%: about 9 years.*", drop=True),
                dict(k="do", f="lite", text="Investing app: / *72 ÷ your return.*")]),
    "lh-reel-1026am-when-where-s15": dict(
        brand=LH, track="lh-x-lock-in", save="send this to your Monday-chaos friend",
        scenes=[dict(k="hook", f="dots", text="Monday plans / *gone by noon?*", emo="⏰"),
                dict(k="say", f="pink", kicker="habit tip", text="Write down / *when* and *where* / you'll start.", drop=True),
                dict(k="do", f="cream", text="Write: *“At 9, at my desk,* / I'll open it.”")]),
    "hb-reel-1026am-voice-transcripts-s15": dict(
        brand=HB, track="hb-x-smart-bounce", save="send this to your voice-note friend",
        scenes=[dict(k="hook", f="yel", text="3-minute voice note, / *mid-meeting?*", emo="📞"),
                dict(k="say", f="indi", kicker="try this", text="WhatsApp can / turn it / *into text.*", drop=True),
                dict(k="do", f="plum", text="Settings, Chats, / Voice message transcripts. / Then *hold the note.*")]),
}


def spec(rid):
    s = dict(NEW[rid], id=rid, fmt="tight")
    s["scenes"] = [dict(s["scenes"][0], save=s.get("save"))] + s["scenes"][1:]
    return s


def check_len(sp, pr):
    want = T.make(sp).duration
    if abs(pr["dur"] - want) > 0.25 or pr["dur"] > 15.0:
        out = T.REPO / "media" / "reels"
        for x in (out / f"{sp['id']}.mp4", out / f"{sp['id']}-cover.jpg"):
            x.unlink(missing_ok=True)
        raise SystemExit(f"encoded {pr['dur']:.2f}s but planned {want:.2f}s -> removed")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--out", default="/tmp/claude-0/tight-oct23")
    a = ap.parse_args()
    for rid in a.ids or list(NEW):
        sp = spec(rid)
        T.lint(sp)
        if a.plan:
            T.report(sp)
        else:
            check_len(sp, T.build(sp, a.out))
            subprocess.run(["rm", "-rf", a.out])

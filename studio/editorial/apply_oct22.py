#!/usr/bin/env python3
"""Oct 22 (Social studio v4): point queued Reels at their <=15 s tight cuts (only when the cut exists and is <=15 s),
align caption line 1 with the new stranger-picked hook, and add ONE page-specific follow reason to every caption close.

    python3 studio/editorial/apply_oct22.py
"""
import json, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
FOLLOW = {
    "littlefold": "Follow for one calm thing a night, from bump to toddler.",
    "lockedhour": "Follow for one small focus fix a day, each one backed by research.",
    "fullyfunded": "Follow for one money move a day, in plain words.",
    "hourback": "Follow to learn what AI can really do, one real test a day.",
}
FIRST = {
    "lh-reel-1022-walk": "Can't crack it at your desk? Stand up. But know which kind of stuck you are.",
    "lf-reel-1023am-screens-bed": "Bedtime turned into a battle again? Turn it into the best 20 minutes of the day.",
    "hb-reel-1023am-photo-search": "Weird light on your dashboard? Point your camera, ask out loud, and AI answers.",
    "ff-reel-1023-cpp-60-or-70": "Your parents taking CPP early? Here's what 60, 65 and 70 pay.",
    "hb-reel-1023-duplicates": "Skimming just the AI summary? Apple's AI wrote a headline. It was false.",
    "lh-reel-1023-caffeine": None,
    "ff-reel-1024am-sick-pay-gap": None,
    "lh-reel-1024am-floss-after": "New habit keeps not sticking? Floss before or after brushing shows why, and the fix works for any habit.",
    "ff-reel-1024-beneficiary": "Never named a TFSA beneficiary? Your TFSA has a blank line. Fill it in.",
    "hb-reel-1024-fridge-dinner": "Your next coworker might be AI. Nvidia's CEO says your IT team will become HR for AI agents.",
    "hb-cheat-1024am-shortcuts": "Nodding along in AI meetings? 6 AI words, decoded 📖",
    "lf-reel-1024-grandma-resp": "New dad, feeling left out? You don't need to feed the baby to bond with them.",
    "lh-reel-1024-lyrics": None,
    "lf-reel-1025am-crying-peak": "Worried you're spoiling your baby? \"Don't pick her up, you'll spoil her.\" You've heard it. It's not true.",
    "lh-reel-1025am-planning-fallacy": None,
    "hb-reel-1025am-talk-dont-type": "That sparkle button? It's AI. You already use it every day.",
    "ff-reel-1025-tfsa-withdrawal-trap": "Putting TFSA money back? Wait. Here's the trap.",
    "lh-reel-1025-unpack": "\"It'll take an hour.\" It won't. Here's the fix that's backed by research.",
    "lf-reel-1025-step-away": None,
    "hb-cheat-1025-voice-words": "That AI button in your apps? Here's where AI already lives 📱 Part 2 of 2.",
    "hb-cheat-1022-travel-admin": None,
}
JOBS = dict(
    caption=("Will AI take your job? Here are the big numbers, by 2030, worldwide.\n\n"
             "THE NUMBERS (World Economic Forum, Future of Jobs Report 2025, a survey of more than 1,000 employers):\n"
             "• 170 million new jobs created\n• 92 million jobs displaced\n• Net: about +78 million jobs\n"
             "• 39% of the key skills in a job are expected to change\n• Fastest-growing skill: AI and big data\n\n"
             "WHAT IT MEANS: the bigger risk isn't a robot taking your job. It's the job changing around you while your skills stay the same.\n\n"
             "THE CATCH: these are employer forecasts, not guarantees, and they vary a lot by industry and country.\n\n"
             "Do this: pick one AI skill your job needs and practise it 15 minutes a day this week.\n\n"
             "Send this to the friend who's job hunting.\n\n"
             "#ai #futureofwork #careers #artificialintelligence #hourback"),
    first_comment=("Source: World Economic Forum, The Future of Jobs Report 2025 (January 2025): 170 million jobs created and 92 million "
                   "displaced by 2030 (net +78 million); employers expect 39% of workers' key skills to change by 2030; AI and big data "
                   "top the list of fastest-growing skills. Forecasts, not guarantees."),
    alt_text=("Cheat-sheet Reel in the Hourback look. Title: Will AI take your job? Table, by 2030 worldwide (WEF): new jobs created "
              "170M · jobs displaced 92M · net change +78M · skills in a job that change 39% · fastest-growing skill AI & data. "
              "Do this: pick one AI skill your job needs, practise it 15 min a day."),
)


def dur(p):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                         capture_output=True, text=True).stdout.strip()
    return float(out) if out else 99.0


def add_follow(cap, acct):
    line = FOLLOW[acct]
    if line in cap:
        return cap
    paras = cap.split("\n\n")
    idx = len(paras)
    for i, para in enumerate(paras):
        if para.startswith("#") or para.startswith("General information only"):
            idx = i
            break
    paras.insert(idx, line)
    return "\n\n".join(paras)


def main():
    f = REPO / "schedule" / "posts.json"
    data = json.loads(f.read_text())
    done = []
    for x in data["posts"]:
        rid = x["id"]
        if rid not in FIRST:
            continue
        cut = REPO / "media" / "reels" / f"{rid}-s15.mp4"
        cov = REPO / "media" / "reels" / f"{rid}-s15-cover.jpg"
        if not (cut.exists() and cov.exists()) or dur(cut) > 15.0:
            print("skip (no valid cut yet):", rid)
            continue
        if x["video"] != f"reels/{rid}-s15.mp4":
            x["video"], x["cover"] = f"reels/{rid}-s15.mp4", f"reels/{rid}-s15-cover.jpg"
        if rid == "hb-cheat-1022-travel-admin":
            x.update(JOBS)
        elif FIRST[rid]:
            lines = x["caption"].split("\n")
            lines[0] = FIRST[rid]
            x["caption"] = "\n".join(lines)
        x["caption"] = add_follow(x["caption"], x["account"])
        done.append(rid)
    f.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("applied:", len(done), done)


if __name__ == "__main__":
    sys.exit(main())

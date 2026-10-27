#!/usr/bin/env python3
"""Social studio Tue Oct 27: queue the gated builds from studio/editorial/oct27/*.json into schedule/posts.json.
Adds 8 Reels (Wed Oct 28 morning, one per page, desk order 1; Fri Oct 30 7 pm, one per page).
Edits only the `caption` text of 9 Wed/Thu Story frames re-lettered after the clarity gate (images re-rendered in place).
Before-state: docs/social-recovery/2026-10-27-before.json.

    python3 studio/editorial/queue_oct27.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "studio/editorial/oct27"
POSTS = REPO / "schedule/posts.json"
BEFORE = REPO / "docs/social-recovery/2026-10-27-before.json"
REEL_KEYS = ("id", "account", "publish_at", "video", "cover", "caption", "first_comment", "alt_text", "trial")
OLD = ("Tonight at 7 pm: the 15-second version", "tonight at 7 pm: the 15-second version")
NEW = ("Tonight at 7 pm: a 15-second Reel on our page", "tonight at 7 pm: a 15-second Reel on our page")
STORY_IDS = ("lf-st-1028-2", "lf-st-1029-2", "ff-st-1028-2", "ff-st-1029-2", "lh-st-1028-2", "lh-st-1029-2",
             "hb-st-1028-1", "hb-st-1028-2", "hb-st-1029-1")
LH_OLD = "Add the obstacle and a plan."
LH_NEW = "So also picture what's in your way, and plan what you'll do when it shows up."


def main():
    data = json.loads(POSTS.read_text())
    posts = data["posts"]
    if not BEFORE.exists():
        BEFORE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    have = {p["id"] for p in posts}
    added, edited = [], []
    for pg in ("littlefold", "lockedhour", "fullyfunded", "hourback"):
        for e in json.loads((SRC / f"{pg}.json").read_text()):
            if e["id"] in have:
                continue
            entry = {k: e[k] for k in REEL_KEYS if e.get(k) not in (None, "", False)}
            if entry.get("trial") and e["account"] != "littlefold":
                entry.pop("trial")  # Performance desk order 3, Oct 27
            posts.append(entry)
            added.append(entry["id"])
    for p in posts:
        if p["id"] not in STORY_IDS:
            continue
        c = p["caption"]
        for o, n in zip(OLD, NEW):
            c = c.replace(o, n)
        c = c.replace(LH_OLD, LH_NEW).replace("People who daydreamed", "People who only daydreamed")
        if p["id"] == "hb-st-1028-1":
            c = "Story hb-st-1028-1: quick question | Google can name a song you only hum? | tap for the answer →"
        if p["id"] == "hb-st-1029-1":
            c = "Story hb-st-1029-1: quick question | Bill went up? AI can tell you why. | tap for the answer →"
        if c != p["caption"]:
            p["caption"] = c
            edited.append(p["id"])
    POSTS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(len(added), "added:", " ".join(added))
    print(len(edited), "story captions edited:", " ".join(edited))


if __name__ == "__main__":
    main()

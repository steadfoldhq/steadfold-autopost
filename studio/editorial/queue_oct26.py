#!/usr/bin/env python3
"""Social studio Mon Oct 26: queue the gated builds from studio/editorial/oct26/*.json into schedule/posts.json.
Adds 6 Reels, 6 feed posts (incl. series No. 3/4 and Day 10 for Fri Oct 30) and 24 Story frames (Tue-Thu, 12:30/12:31).
No queued post is changed. Before-state is saved to docs/social-recovery/2026-10-26-before.json.

    python3 studio/editorial/queue_oct26.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "studio/editorial/oct26"
POSTS = REPO / "schedule/posts.json"
BEFORE = REPO / "docs/social-recovery/2026-10-26-before.json"
FEED_KEYS = ("id", "account", "publish_at", "images", "caption", "first_comment", "alt_text")
REEL_KEYS = ("id", "account", "publish_at", "video", "cover", "caption", "first_comment", "alt_text", "trial")
STORY_KEYS = ("id", "account", "publish_at", "story", "image", "caption")


def main():
    data = json.loads(POSTS.read_text())
    posts = data["posts"]
    if not BEFORE.exists():
        BEFORE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    have = {p["id"] for p in posts}
    added = []
    for pg in ("littlefold", "lockedhour", "fullyfunded", "hourback"):
        for e in json.loads((SRC / f"{pg}.json").read_text()):
            if e["id"] in have:
                continue
            keys = STORY_KEYS if e.get("story") else REEL_KEYS if e.get("video") else FEED_KEYS
            entry = {k: e[k] for k in keys if e.get(k) not in (None, "", False)}
            if entry.get("trial") and e["account"] in ("fullyfunded", "hourback"):
                entry.pop("trial")  # Performance desk order 2/4, Oct 26
            posts.append(entry)
            added.append(entry["id"])
    POSTS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(len(added), "added:", " ".join(added))


if __name__ == "__main__":
    main()

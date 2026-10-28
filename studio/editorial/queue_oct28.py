#!/usr/bin/env python3
"""Social studio Wed Oct 28: queue the gated builds from studio/editorial/oct28/*.json into schedule/posts.json.
Adds 8 Reels (Thu Oct 29 morning + Sat Oct 31, one each per page) and 4 series episodes (Mon Nov 2).
No existing entry is edited. Before-state: docs/social-recovery/2026-10-28-before.json.

    python3 studio/editorial/queue_oct28.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "studio/editorial/oct28"
POSTS = REPO / "schedule/posts.json"
BEFORE = REPO / "docs/social-recovery/2026-10-28-before.json"
KEYS = ("id", "account", "publish_at", "video", "cover", "images", "caption", "first_comment", "alt_text", "trial")


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
            entry = {k: e[k] for k in KEYS if e.get(k) not in (None, "", False, [])}
            if entry.get("trial") and e["account"] != "littlefold":
                entry.pop("trial")  # Performance desk: no trial on FF/LH/HB
            posts.append(entry)
            added.append(entry["id"])
    POSTS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(len(added), "added:", " ".join(added))


if __name__ == "__main__":
    main()

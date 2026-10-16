#!/usr/bin/env python3
"""Re-apply B1 entries to a fresh schedule/posts.json: add only into EMPTY Hourback slots, never replace anything.
Usage: python3 merge.py /home/claude/steadfold-autopost"""
import json, sys
from pathlib import Path
repo = Path(sys.argv[1]); f = repo / "schedule" / "posts.json"
d = json.loads(f.read_text()); posts = d["posts"]
new = json.loads((Path(__file__).parent / "entries.json").read_text())
ids = {p["id"] for p in posts}
kind = lambda p: "story" if p.get("story") else ("reel" if p.get("video") else "feed")  # noqa: E731
taken = {(p["account"], p["publish_at"], kind(p) == "story") for p in posts}
added, skipped = [], []
for e in new:
    if e["id"] in ids:
        skipped.append((e["id"], "id exists")); continue
    if (e["account"], e["publish_at"], kind(e) == "story") in taken:
        skipped.append((e["id"], "slot taken")); continue
    posts.append(e); added.append(e["id"])
posts.sort(key=lambda p: (p["publish_at"], p["account"], p["id"]))
f.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
print(f"added {len(added)}; skipped {skipped}")

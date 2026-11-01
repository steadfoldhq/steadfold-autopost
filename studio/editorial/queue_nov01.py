#!/usr/bin/env python3
"""Social studio Nov 1 2026: add 16 new entries from studio/editorial/nov01/*.json and swap the slides of the
queued hb-day11-gift-for-dad (stranger verdict CONFUSING) per nov01/hourback_day11_fix.json.
Before-state saved to docs/social-recovery/2026-11-01-before.json."""
import json, shutil
from pathlib import Path
R = Path(__file__).resolve().parents[2]
Q = R / "schedule/posts.json"
shutil.copy(Q, R / "docs/social-recovery/2026-11-01-before.json")
P = json.loads(Q.read_text())
KEEP = ("id", "account", "publish_at", "video", "cover", "images", "caption", "first_comment", "alt_text", "trial")
ids = {p["id"] for p in P["posts"]}
added = []
for pg in ("littlefold", "lockedhour", "fullyfunded", "hourback"):
    for e in json.loads((R / f"studio/editorial/nov01/{pg}.json").read_text()):
        assert e["id"] not in ids, e["id"]
        P["posts"].append({k: e[k] for k in KEEP if k in e}); added.append(e["id"])
fix = json.loads((R / "studio/editorial/nov01/hourback_day11_fix.json").read_text())
fix = fix[0] if isinstance(fix, list) else fix
for p in P["posts"]:
    if p["id"] == fix["id"]:
        for k in ("images", "alt_text", "caption"):
            if k in fix: p[k] = fix[k]

Q.write_text(json.dumps(P, indent=2, ensure_ascii=False) + "\n")
print(len(added), "added;", added)

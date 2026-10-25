#!/usr/bin/env python3
"""Social studio Sun Oct 25: queue the gated builds from studio/editorial/oct25/*.json into schedule/posts.json.
Adds 7 Reels (Mon-Thu 7 pm), applies 3 clarity fixes to queued carousels (new media files; originals kept),
fixes one alt text, and drops the trial flag on the Tue FF morning Reel (Performance desk order 1, Oct 25).
Before-state is saved to docs/social-recovery/2026-10-25-before.json.

    python3 studio/editorial/queue_oct25.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "studio/editorial/oct25"
POSTS = REPO / "schedule/posts.json"
BEFORE = REPO / "docs/social-recovery/2026-10-25-before.json"

RENAME = {"lf-reel-1026-neck-check": "lf-reel-1028-neck-check",
          "hb-reel-1026-hum-a-song": "hb-reel-1028-hum-a-song",
          "hb-reel-1027-bill-went-up": "hb-reel-1029-bill-went-up"}
NEW = ["ff-reel-1026-cash-at-zero", "lh-reel-1026-print-it", "ff-reel-1027-car-loan-send",
       "lf-reel-1026-neck-check", "lh-reel-1028-grey-phone", "hb-reel-1026-hum-a-song", "hb-reel-1027-bill-went-up"]
FIX = ["ff-richhabits-01", "ff-richhabits-02", "hb-day9-kind-firm-no"]
HB8_ALT = ("Hourback 3-slide carousel. Slide 1: 'AI, for real · Day 8' badge, 'AI's answer felt generic again?' in a large serif "
           "with highlighted words, black-and-white chat bubbles, and the handwritten note 'new one every Mon · Wed · Fri'. "
           "Slide 2: Before you answer, ask me 3 questions. (add this line to any request). Slide 3: 'Birthday dinner, 6 people, "
           "$150. It asked me:' with the three questions: 1 Out, or at home? 2 Any allergies or diets? 3 Does $150 cover it all? "
           "(real reply, shortened).")


def main():
    data = json.loads(POSTS.read_text())
    posts = data["posts"]
    if not BEFORE.exists():
        BEFORE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    M = {}
    for pg in ("littlefold", "lockedhour", "fullyfunded", "hourback"):
        for e in json.loads((SRC / f"{pg}.json").read_text()):
            M[e["id"]] = e
    byid = {p["id"]: p for p in posts}
    for rid in NEW:
        e, nid = M[rid], RENAME.get(rid, rid)
        if nid in byid:
            continue
        posts.append({"id": nid, "account": e["account"], "publish_at": e["publish_at"], "video": e["video"],
                      "cover": e["cover"], "caption": e["caption"], "first_comment": e["first_comment"],
                      "alt_text": e["alt_text"]})
    for rid in FIX:
        e, p = M[rid], byid[rid]
        p["images"] = e["images"]
        for k in ("caption", "first_comment", "alt_text"):
            if e.get(k):
                p[k] = e[k]
    byid["hb-day8-ask-me-first"]["alt_text"] = HB8_ALT
    byid["ff-reel-1027am-card-full-balance"].pop("trial", None)
    POSTS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write the §13 rebuild into schedule/posts.json (Oct 18 onward). Only touches entries it owns; never state/ or tokens.

    python3 studio/editorial/teach_schedule.py [--since 2026-10-17T20:20]
Feed posts and Story chains go in when their images exist. A Reel's entry switches to the new cut only once its new MP4 is
rendered (mtime after --since); until then the old entry stays, so the queue is never broken.
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import edkit as K  # noqa: E402
import specs_teach as S  # noqa: E402

OFF = "-04:00"


def clean(t):
    return re.sub(r"\s+", " ", (t or "").replace("*", "").replace(" / ", " ")).strip()


def feed_alt(pid):
    sp = S.POSTS[pid]
    c = sp["cover"]
    n = 1 + len(sp["slides"])
    out = f"{K.NAME[sp['brand']]} {n}-slide carousel. Slide 1: '{clean(c['text'])}' in a large serif with highlighted words"
    if c.get("items"):
        out += " above a sticky note listing " + ", ".join(c["items"])
    out += f", a halftone cut-out and the handwritten note '{c['save']}'."
    for i, s in enumerate(sp["slides"], 2):
        bits = [s.get("label"), "Do this:" if s.get("k") == "do" else None, clean(s.get("text"))]
        if s.get("rows"):
            bits.append("; ".join(f"{a}: {b}" for a, b in s["rows"]))
        if s.get("items"):
            bits.append("; ".join(f"{j + 1}. {x}" for j, x in enumerate(s["items"])))
        if s.get("num"):
            bits.append(s["num"])
        if s.get("sub"):
            bits.append(f"({s['sub']})")
        out += f" Slide {i}: " + " ".join(b for b in bits if b) + "."
    return out


def reel_alt(rid):
    sp = S.REELS[rid]
    parts = []
    for sc in sp["scenes"]:
        if sc.get("text"):
            parts.append(("Do this: " if sc["k"] == "do" else ("because " if sc["k"] == "because" else "")) + clean(sc["text"]))
        if sc.get("label"):
            parts.append(clean(sc["label"]) + (f" {sc.get('pre', '')}{sc['value']:,}" if sc.get("value") is not None else ""))
        if sc.get("items"):
            parts.append(", ".join(clean(x) for x in sc["items"]))
    return (f"Edited video in the {K.NAME[sp['brand']]} editorial look: big serif lines on soft paper colours with highlighted words, "
            f"a halftone cut-out and the round stamp, cut on the music. Text: " + " / ".join(parts) + ". It loops back to the opening line.")


def story_caption(cid, i, fr):
    return f"Story chain {cid} frame {i}: " + clean(fr.get("text") or fr.get("label") or "")[:80]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2026-10-17T20:20")
    a = ap.parse_args()
    since = datetime.fromisoformat(a.since).timestamp()
    p = REPO / "schedule" / "posts.json"
    d = json.loads(p.read_text())
    posts = d["posts"]
    old = {x["id"]: x for x in posts}
    accounts = {S.FF: "fullyfunded", S.HB: "hourback", S.LH: "lockedhour", S.LF: "littlefold"}
    new_entries, remove = [], set(S.DROPPED)
    # old Stories from Oct 18 on are replaced by the chains (one chain per page per day)
    for x in posts:
        if x.get("story") and x["publish_at"] >= "2026-10-18" and "-ch-" not in x["id"]:
            remove.add(x["id"])
    for pid, m in S.META.items():
        if m["kind"] == "feed":
            imgs = sorted(f"{pid}/{f.name}" for f in (REPO / "media" / pid).glob("*.jpg"))
            assert len(imgs) == 1 + len(S.POSTS[pid]["slides"]), pid
            e = dict(old.get(pid, {}))
            e.update(id=pid, account=accounts[S.POSTS[pid]["brand"]], publish_at=m["at"] + ":00" + OFF, caption=m["caption"],
                     first_comment=m["comment"], alt_text=feed_alt(pid), images=imgs)
            remove.add(pid)
            new_entries.append(e)
        else:
            mp4 = REPO / "media" / "reels" / f"{pid}.mp4"
            if not mp4.exists() or mp4.stat().st_mtime < since:
                print("reel not rebuilt yet, old entry kept:", pid)
                if pid == "ff-reel-1018-start-28":
                    remove.discard("ff-reel-1018-the-door")
                continue
            e = dict(old.get(pid, {}))
            e.update(id=pid, account=accounts[S.REELS[pid]["brand"]], publish_at=m["at"] + ":00" + OFF, caption=m["caption"],
                     first_comment=m["comment"], alt_text=reel_alt(pid), video=f"reels/{pid}.mp4", cover=f"reels/{pid}-cover.jpg")
            e.pop("images", None)
            remove.add(pid)
            new_entries.append(e)
    for cid, ch in S.CHAINS.items():
        for i, (fr, t) in enumerate(zip(ch["frames"], ch["times"]), 1):
            fid = f"{cid}-{i}"
            assert (REPO / "media" / "stories" / f"{fid}.jpg").exists(), fid
            remove.add(fid)
            new_entries.append(dict(id=fid, account=accounts[ch["brand"]], publish_at=f"{ch['day']}T{t}:00{OFF}", story=True,
                                    image=f"stories/{fid}.jpg", caption=story_caption(cid, i, fr)))
    kept = [x for x in posts if x["id"] not in remove]
    out = kept + new_entries
    out.sort(key=lambda x: (x["publish_at"], x["account"], x["id"]))
    d["posts"] = out
    p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
    gone = sorted(i for i in remove if i not in {e["id"] for e in new_entries})
    print(f"schedule: {len(out)} entries ({len(new_entries)} rebuilt, removed {len(gone)}: {', '.join(gone)})")


if __name__ == "__main__":
    main()

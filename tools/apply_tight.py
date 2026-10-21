#!/usr/bin/env python3
"""Oct 21 queue clean-up (owner: "keep getting better... minimal but valuable, more details").
- Points each long Reel at its tight <=15 s cut (<id>-s15.mp4 + cover) once the file exists. Captions keep every detail.
- 15.3 s pan Reels -> 14.97 s trims.
- Every morning Reel (before noon) gets "trial": "auto".
- Fills empty Reel slots: LF Oct 21 19:00 (Special Time cut), HB Oct 24 08:45 and Oct 25 19:00 (the cheat sheets built for them).
Only touches posts that have not published yet. Originals stay in media/reels.
    python3 tools/apply_tight.py [--dry-run]
"""
import json, sys, subprocess, datetime as dt
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "studio" / "editorial"))
SCHED, STATE, MEDIA = ROOT / "schedule/posts.json", ROOT / "state/published.json", ROOT / "media"


def dur(rel):
    out = subprocess.run(["ffprobe", "-v", "0", "-show_entries", "format=duration", "-of", "csv=p=0", str(MEDIA / rel)],
                         capture_output=True, text=True).stdout.strip()
    return float(out or 0)


def main(dry):
    import tight, tight_new, v5_hb_cheats
    d = json.loads(SCHED.read_text())
    pub = json.loads(STATE.read_text())["posts"]
    now = dt.datetime.now(dt.timezone.utc)
    future = lambda p: p["id"] not in pub and dt.datetime.fromisoformat(p["publish_at"]) > now + dt.timedelta(minutes=20)  # noqa
    log = []
    ids = {p["id"] for p in d["posts"]}
    for p in d["posts"]:
        if not future(p) or p.get("story") or not p.get("video"):
            continue
        rid = p["id"]
        if rid in tight.TIGHT:
            v, c = f"reels/{rid}-s15.mp4", f"reels/{rid}-s15-cover.jpg"
            if (MEDIA / v).exists() and (MEDIA / c).exists() and dur(v) <= 15.05:
                sp = tight.tight_spec(rid)
                txt = " / ".join((s.get("text") or ", ".join(s.get("items") or []) or f"{s.get('label', '')} {s.get('pre', '')}{s.get('value', '')} {s.get('suf', '')}").replace("*", "").replace(" / ", " ")
                                 for s in sp["scenes"])
                if p["video"] != v:
                    p.update(video=v, cover=c,
                             alt_text=p["alt_text"].split(" Text: ")[0] + f" Text: {txt}. It loops back to the opening line.")
                    log.append(f"tight {rid} ({dur(v):.1f}s)")
        elif (MEDIA / p["video"].replace(".mp4", "-s15.mp4")).exists() and "-pan-" in rid and not p["video"].endswith("-s15.mp4"):
            p["video"] = p["video"].replace(".mp4", "-s15.mp4"); log.append(f"trim {rid}")
        t = dt.datetime.fromisoformat(p["publish_at"])
        if t.hour < 12 and p.get("trial") != "auto":
            p["trial"] = "auto"; log.append(f"trial {rid}")
    # fill empty slots
    for rid, n in tight_new.NEW.items():
        v = f"reels/{rid}.mp4"
        if rid not in ids and (MEDIA / v).exists() and future(dict(id=rid, publish_at=n["at"])):
            sp = tight_new.spec(rid)
            txt = " / ".join(s["text"].replace("*", "").replace(" / ", " ") for s in sp["scenes"])
            d["posts"].append(dict(id=rid, account=n["brand"], publish_at=n["at"], caption=n["caption"], first_comment=n["comment"],
                                   alt_text="Edited video in the Littlefold editorial look: big serif lines on soft paper colours with "
                                            f"highlighted words and the round stamp, cut on the music. Text: {txt}. It loops back to the opening line.",
                                   video=v, cover=f"reels/{rid}-cover.jpg"))
            log.append(f"new {rid}")
    for pid in ("hb-cheat-1024am-shortcuts", "hb-cheat-1025-voice-words"):
        m, sp = v5_hb_cheats.META[pid], v5_hb_cheats.CHEATS[pid]
        if pid in ids or not future(dict(id=pid, publish_at=m["at"] + ":00-04:00")):
            continue
        alt = (f"Canada-edition cheat sheet in the Hourback editorial look. Title: {sp['title'].replace('*', '').replace(' / ', ' ')}. "
               + " · ".join(f"{a}: {b}" for a, b in sp["rows"]) + f". Do this: {sp['do'].replace('*', '')}")
        e = dict(id=pid, account="hourback", publish_at=m["at"] + ":00-04:00", caption=m["caption"], first_comment=m["comment"],
                 alt_text=alt, video=f"reels/{pid}.mp4", cover=f"reels/{pid}-cover.jpg")
        if "am-" in pid:
            e["trial"] = "auto"
        d["posts"].append(e); log.append(f"new {pid}")
    d["posts"].sort(key=lambda x: (x["publish_at"], x["account"], x["id"]))
    print("\n".join(log) or "nothing to change")
    if not dry:
        SCHED.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main("--dry-run" in sys.argv)

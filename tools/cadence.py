#!/usr/bin/env python3
"""Dynamic cadence (brand system §13.6): decide tomorrow's post counts per page from the numbers.

    python3 tools/cadence.py                 # table + tomorrow's counts from insights/latest.json
    python3 tools/cadence.py --json          # the counts as JSON (for the daily agents)

Rule (owner, Oct 17 7:15 pm: "some days 2 posts, some days more… keep checking engagement and adjust"):
- Window: the page's posts from the last 7 days that are at least 12 h old (reach has mostly settled by then).
- Score = median reach per post (median views breaks ties), by format (reel / carousel / single) and, for Reels, by slot (am < 11:00 ET, eve >= 17:00 ET).
- Reels: 2 a day (morning + evening) while the page's Reel median >= its carousel median; otherwise 1 (the stronger slot).
  A slot whose median is under half the other slot's (n >= 3 each) moves to the stronger slot's side of the day.
- Feed: 1 teaching post a day, always (the floor). A 2nd feed post only while singles hold >= 0.8x the carousel median.
- Stories: one 4-frame chain a day (hook on a photo -> teaching -> payoff -> hand-off to the post / "Part 2 tomorrow").
  The collector can't read Story metrics yet, so chains hold at 4 frames; 5 on a page's 2-feed-post day (cap 5).
- Ceilings (autopost tests): 2 feed, 2 Reels, 5 Stories per page per Toronto day. Floor: 1 post per page per day.
- Ties and thin data (n < 2 in a format) keep yesterday's count. Re-decided every morning after the Performance desk's "Today's orders" (claude/metrics.md, Learning Lab);
  when the orders disagree with this script, the orders win and the reason goes in the day's report.
"""
import argparse
import json
import statistics
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CEIL = dict(feed=2, reel=2, story=5)
TZ = timezone(timedelta(hours=-4))  # Toronto, EDT until Nov 1


def fmt_of(p):
    return {"REEL": "reel", "CAROUSEL_ALBUM": "carousel", "IMAGE": "single"}.get(p.get("type"), "other")


def med(xs):
    return statistics.median(xs) if xs else None


def decide(latest, now=None):
    now = now or datetime.fromisoformat(latest["collected_at"])
    out = {}
    for acc, a in latest["accounts"].items():
        rows = []
        for p in a.get("posts", []):
            at = datetime.fromisoformat(p["at"].replace("+0000", "+00:00"))
            age = (now - at).total_seconds() / 3600
            reach = (p.get("insights") or {}).get("reach")
            if reach is None or age < 12 or age > 24 * 7:
                continue
            loc = at.astimezone(TZ)
            slot = "am" if loc.hour < 11 else ("eve" if loc.hour >= 17 else "mid")
            rows.append(dict(fmt=fmt_of(p), slot=slot, reach=reach, views=(p.get("insights") or {}).get("views") or 0))
        views = {f: med([r["views"] for r in rows if r["fmt"] == f]) for f in ("reel", "carousel", "single")}
        by = {f: [r["reach"] for r in rows if r["fmt"] == f] for f in ("reel", "carousel", "single")}
        reel_slot = {s: [r["reach"] for r in rows if r["fmt"] == "reel" and r["slot"] == s] for s in ("am", "eve")}
        m = {f: med(v) for f, v in by.items()}
        ms = {s: med(v) for s, v in reel_slot.items()}
        why = []
        reels = 2
        reel_lose = m["reel"] is not None and m["carousel"] is not None and (
            m["reel"] < m["carousel"] or (m["reel"] == m["carousel"] and (views["reel"] or 0) < (views["carousel"] or 0)))
        if reel_lose and len(by["reel"]) >= 2:
            reels = 1
            why.append(f"Reels {m['reel']} < carousels {m['carousel']}: 1 Reel")
        else:
            why.append(f"Reels median {m['reel']} vs carousels {m['carousel']}: 2 Reels")
        slots = ["am", "eve"]
        if all(len(reel_slot[s]) >= 3 for s in slots):
            lo, hi = sorted(slots, key=lambda s: ms[s])
            if ms[lo] < 0.5 * ms[hi]:
                why.append(f"{lo} Reels {ms[lo]} < half of {hi} {ms[hi]}: move the {lo} Reel next to {hi}")
        feed = 1
        if m["single"] is not None and m["carousel"] is not None and len(by["single"]) >= 1 and m["single"] >= 0.8 * m["carousel"]:
            feed = 2
            why.append(f"singles {m['single']} >= 0.8x carousels {m['carousel']}: keep the 2nd feed post")
        else:
            why.append(f"singles {m['single']} < 0.8x carousels {m['carousel']}: 1 feed post (teaching)")
        story = 5 if feed == 2 else 4
        out[acc] = dict(reel=min(reels, CEIL["reel"]), feed=max(1, min(feed, CEIL["feed"])), story=min(story, CEIL["story"]),
                        medians=m, views=views, reel_slots=ms, n={f: len(v) for f, v in by.items()}, why=why)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--latest", default=str(REPO / "insights" / "latest.json"))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    latest = json.loads(Path(a.latest).read_text())
    d = decide(latest)
    if a.json:
        print(json.dumps(d, indent=1))
        return
    print(f"insights read {latest['collected_at']}")
    for acc, v in d.items():
        print(f"{acc:12s} reels {v['reel']}  feed {v['feed']}  stories {v['story']}  = {v['reel'] + v['feed']} posts + {v['story']} Stories"
              f"   medians {v['medians']} n {v['n']} reel slots {v['reel_slots']}")
        for w in v["why"]:
            print("   -", w)


if __name__ == "__main__":
    main()

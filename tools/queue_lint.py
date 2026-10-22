#!/usr/bin/env python3
"""Pre-publication checks for schedule/posts.json (added Oct 22 2026, v0.6 social recovery).

Catches the defects this queue has actually shown, before Autopost picks a post up:
  ERROR  a queued id that is already in state/published.json (Autopost would silently skip it — the
         Oct 21 LH follow-the-line Reel never went out because its id was reused)
  ERROR  duplicate ids, missing media files, Reel files Instagram rejects (not MP4 H.264+AAC, not 9:16,
         19.5 MB or more), publish_at without a UTC offset
  WARN   Reels longer than 15.0 s (studio standard), the same feed/Reel media used by two posts,
         more than one Canada-flag post per page per week (standard B19), "Canada edition" labels,
         the banned word "example", Littlefold health captions without the medical disclaimer,
         daily ceilings per page (2 feed, 2 Reels, 5 Stories), captions that point to a later post
         "tonight" when no later post exists that day on that page.

Usage:  python3 tools/queue_lint.py [--all] [--strict] [--now ISO]
        --all     also check past/published entries (default: only upcoming, unpublished ones)
        --strict  exit 1 on warnings too
Exit code: 0 = no errors (warnings allowed unless --strict), 1 = problems, 2 = bad input.
Reads only; never edits anything.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
TORONTO = ZoneInfo("America/Toronto")
MAX_REEL_BYTES = 19_500_000
MAX_REEL_SECONDS = 15.05
CEILINGS = {"feed": 2, "reel": 2, "story": 5}
# Littlefold's disclaimer rule applies to health content, not to money/forms or "small wins" posts (Oct 22 refinement:
# the first version flagged an RESP post and a showering post).
HEALTH = re.compile(r"\b(sleep|nap|feed(s|ing)?|formula|breast|bottle|fever|temperature|sids|vaccin\w*|rash|colic|"
                    r"cry(ing)?|crie[sd]|reflux|jaundice|teeth|teething|poop|diaper rash|solids|allerg\w*|choking|"
                    r"weight|growth|milestone|postpartum|pregnan\w*|doctor|nurse|medic\w*|health)\b", re.I)
# A "tonight" pointer promises a later post on this page ("Part 2 tonight", "drops tonight at 7"); a viewer call to
# action ("Do this tonight") is not one.
POINTER = re.compile(r"\b(part \d+|no\.? ?\d+|episode|reel|post|video|drops?|posting|coming|out|live|see you)\b"
                     r"[^.\n]{0,30}\btonight\b|\btonight\b[^.\n]{0,12}\b(at \d|\d ?(pm|p\.m\.))", re.I)


def kind(p: dict) -> str:
    if p.get("story"):
        return "story"
    return "reel" if p.get("video") else "feed"


def probe(path: Path) -> dict | None:
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration,size:stream=codec_type,codec_name,width,height",
                              "-of", "json", str(path)], capture_output=True, text=True, timeout=60)
        return json.loads(out.stdout) if out.returncode == 0 else None
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return None


def lint(posts: list[dict], published: dict, now: datetime, check_all: bool = False,
         media_root: Path | None = None, prober=probe) -> tuple[list[str], list[str]]:
    media_root = media_root or ROOT / "media"
    errors: list[str] = []
    warns: list[str] = []
    ids = Counter(p.get("id") for p in posts)
    for i, n in ids.items():
        if n > 1:
            errors.append(f"[{i}] duplicate id ({n} entries)")

    def when(p):
        try:
            t = datetime.fromisoformat(p["publish_at"])
        except (KeyError, ValueError):
            return None
        return t if t.tzinfo else None

    todo = []
    for p in posts:
        t = when(p)
        if t is None:
            errors.append(f"[{p.get('id')}] publish_at missing or without UTC offset: {p.get('publish_at')!r}")
            continue
        rec = published.get(p["id"]) or {}
        pub_at = rec.get("published_at") or rec.get("publish_called_at")
        if pub_at and (check_all or t > now):
            try:
                pt = datetime.fromisoformat(pub_at.replace("Z", "+00:00"))
                if (t - pt).total_seconds() > 24 * 3600:
                    errors.append(f"[{p['id']}] scheduled {p['publish_at']} but this id was already published at "
                                  f"{pub_at}: the entry reuses an old id, so Autopost skipped or will skip it")
            except ValueError:
                pass
        if check_all or (t > now and p["id"] not in published):
            todo.append((p, t))

    media_users: dict[str, list[str]] = defaultdict(list)
    per_day: Counter = Counter()
    canada_week: dict[tuple, list[str]] = defaultdict(list)
    later_today: dict[tuple, list[datetime]] = defaultdict(list)
    for p, t in todo:
        local = t.astimezone(TORONTO)
        later_today[(p["account"], local.date())].append(local)

    for p, t in todo:
        pid, k, local = p["id"], kind(p), t.astimezone(TORONTO)
        per_day[(p["account"], local.date(), k)] += 1
        files = []
        if p.get("video"):
            files.append(("video", p["video"]))
        if p.get("cover"):
            files.append(("cover", p["cover"]))
        for im in p.get("images") or []:
            files.append(("image", im))
        if p.get("image"):
            files.append(("image", p["image"]))
        for role, rel in files:
            f = media_root / rel
            if not f.is_file():
                errors.append(f"[{pid}] missing media file media/{rel}")
                continue
            if k != "story" and role in ("video", "image"):
                media_users[rel].append(pid)
            if role == "video":
                info = prober(f)
                if info is None:
                    errors.append(f"[{pid}] can't read the video media/{rel} (ffprobe failed)")
                    continue
                fmt = info.get("format", {})
                size, dur = int(fmt.get("size") or f.stat().st_size), float(fmt.get("duration") or 0)
                streams = info.get("streams", [])
                codecs = {s.get("codec_name") for s in streams}
                v = next((s for s in streams if s.get("codec_type") == "video"), {})
                if size >= MAX_REEL_BYTES:
                    errors.append(f"[{pid}] Reel is {size/1e6:.1f} MB (Instagram limit used here: 19.5 MB)")
                if not {"h264", "aac"} <= codecs:
                    errors.append(f"[{pid}] Reel codecs {sorted(c for c in codecs if c)} (need H.264 + AAC)")
                w, h = v.get("width"), v.get("height")
                if w and h and abs(w / h - 9 / 16) > 0.01:
                    errors.append(f"[{pid}] Reel is {w}x{h}, not 9:16")
                if dur > MAX_REEL_SECONDS:
                    warns.append(f"[{pid}] Reel is {dur:.1f} s (studio standard: 15 s or less)")
        cap = p.get("caption", "") or ""
        text = " ".join([cap, p.get("alt_text", "") or "", p.get("first_comment", "") or ""])
        if re.search(r"\bexamples?\b", text, re.I):
            warns.append(f"[{pid}] uses the banned word 'example'")
        if re.search(r"canada edition", text, re.I):
            warns.append(f"[{pid}] 'Canada edition' label: check the content really is Canadian")
        if k != "story" and ("🇨🇦" in cap[:400] or re.search(r"canada edition", cap, re.I)):
            year, week, _ = local.isocalendar()
            canada_week[(p["account"], year, week)].append(pid)
        if (p["account"] == "littlefold" and k != "story" and HEALTH.search(re.sub(r"(?i)no health (facts|claims)", "", text))
                and "not medical advice" not in cap.lower()):
            warns.append(f"[{pid}] Littlefold caption without \"General information only, not medical advice.\"")
        if POINTER.search(cap[:600]) and k != "story":
            later = [x for x in later_today[(p["account"], local.date())] if x > local]
            if not later:
                warns.append(f"[{pid}] caption promises something 'tonight' but nothing else is queued later "
                             f"that day on {p['account']}")

    for rel, users in media_users.items():
        if len(set(users)) > 1:
            warns.append(f"same media media/{rel} used by {len(set(users))} posts: {', '.join(sorted(set(users)))}")
    for (acct, year, week), pids in canada_week.items():
        if len(pids) > 1:
            warns.append(f"{acct}: {len(pids)} Canada-flag posts in ISO week {year}-W{week:02d} (B19 max 1): "
                         + ", ".join(pids))
    for (acct, day, k), n in per_day.items():
        if n > CEILINGS[k]:
            warns.append(f"{acct} {day}: {n} {k} posts (ceiling {CEILINGS[k]})")
    return errors, warns


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--now")
    ap.add_argument("--posts", default=str(ROOT / "schedule" / "posts.json"))
    ap.add_argument("--state", default=str(ROOT / "state" / "published.json"))
    a = ap.parse_args(argv)
    try:
        posts = json.loads(Path(a.posts).read_text())["posts"]
        state_path = Path(a.state)
        published = json.loads(state_path.read_text()).get("posts", {}) if state_path.exists() else {}
        now = datetime.fromisoformat(a.now) if a.now else datetime.now(timezone.utc)
        if now.tzinfo is None:
            raise ValueError("--now needs a UTC offset")
    except (OSError, ValueError, KeyError) as exc:
        print(f"queue_lint: {exc}", file=sys.stderr)
        return 2
    errors, warns = lint(posts, published, now, check_all=a.all)
    for e in errors:
        print(f"ERROR {e}")
    for w in warns:
        print(f"WARN  {w}")
    print(f"queue_lint: {len(errors)} error(s), {len(warns)} warning(s)")
    return 1 if errors or (a.strict and warns) else 0


if __name__ == "__main__":
    sys.exit(main())

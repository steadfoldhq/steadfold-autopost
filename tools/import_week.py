#!/usr/bin/env python3
"""
Import a week of Steadfold posts into this repo.

What it does:
  * reads the three Instagram prompt files (9a/9b/9c-instagram-*.txt). They are
    the source of truth for each post's WHEN, FOLDER, CAPTION, ALT TEXT and
    FIRST COMMENT (the caption.txt inside the post folders may be an older draft);
  * takes the slides (01.png, 02.png, ...) from each post folder and converts
    them to high-quality JPEG (quality 92, RGB) under media/<post-id>/NN.jpg,
    because Instagram only accepts JPEG;
  * re-dates the posts so the earliest day lands on --start-date, one post per
    account per day, at each account's usual time of day (Toronto time);
  * writes schedule/posts.json and prints the schedule table.

Scheduling rules, in order:
  1. Each post is shifted by the same number of days (start-date minus the
     earliest original day) and moved to its account's time of day.
  2. Pinned posts (--pin) keep their pinned date no matter what.
  3. Walking through each account's posts in their original order, a post that
     would land on the same day as (or before) the previous one, or on a pinned
     day, moves to the next free day. So each account posts at most once a day.
  4. Deferred posts (--defer) are taken out of the line and placed on the first
     free day after the account's last pinned post.

Built-in rules for the week of Oct 15, 2026 (only used if those posts are in the
import; turn off with --no-default-rules):
  pin   lh-w2-08-lockin-kickoff          Mon Oct 19 (90-Day Lock-In starts that day)
  pin   hb-w02-8-12-automations-kickoff  Mon Oct 19 (12 Automations starts that day)
  pin   lh-w2-05-restart                 Sun Oct 18 (caption says "Use tomorrow" /
                                         "the 90-Day Lock-In begins Monday")
  defer lh-w2-03-todo-bedtime            evergreen; Locked Hour has 5 pre-kickoff
                                         posts but only 4 days (Oct 15-18) before it

Usage:
  python tools/import_week.py --start-date 2026-10-15
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = Path("/tmp/claude-0/-home-claude/8c31f03b-6f3f-5c8d-8bb0-4e6b512aad0e/"
                      "scratchpad/acct/out")
DEFAULT_PROMPTS = Path("/home/claude/tonight")
PROMPT_FILES = {
    "lockedhour": "9a-instagram-lockedhour.txt",
    "fullyfunded": "9b-instagram-fullyfunded.txt",
    "hourback": "9c-instagram-hourback.txt",
}
USERNAMES = {"fullyfunded": "fullyfundedhq", "lockedhour": "lockedhourhq",
             "hourback": "hourbackhq"}
TIME_OF_DAY = {"fullyfunded": time(12, 0), "lockedhour": time(12, 30),
               "hourback": time(13, 0)}
TORONTO = ZoneInfo("America/Toronto")
JPEG_QUALITY = 92
MAX_SLIDES = 10

DEFAULT_PINS = {
    "lh-w2-08-lockin-kickoff": date(2026, 10, 19),
    "hb-w02-8-12-automations-kickoff": date(2026, 10, 19),
    "lh-w2-05-restart": date(2026, 10, 18),
}
DEFAULT_DEFER = ["lh-w2-03-todo-bedtime"]

MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


@dataclass
class Post:
    id: str
    account: str
    folder: str
    original: datetime          # original WHEN (Toronto)
    caption: str
    first_comment: str
    alt_text: str = ""
    when_line: str = ""
    new_date: date | None = None
    notes: list[str] = field(default_factory=list)

    @property
    def publish_at(self) -> datetime:
        return datetime.combine(self.new_date, TIME_OF_DAY[self.account], tzinfo=TORONTO)


# --------------------------------------------------------------------------------------
# Parsing the prompt files
# --------------------------------------------------------------------------------------

BLOCK_SPLIT = re.compile(r"^-{5,} .*? POST \d+ of \d+ -{5,}\s*$", re.MULTILINE)
WHEN_RE = re.compile(
    r"^WHEN:\s*\w{3} (\w{3}) (\d{1,2}), (\d{4}) at (\d{1,2}):(\d{2}) ?(am|pm)", re.MULTILINE)
FOLDER_RE = re.compile(r"^FOLDER:\s*(\S+)", re.MULTILINE)
ACCOUNT_RE = re.compile(r"^INSTAGRAM ACCOUNT:\s*@(\S+)", re.MULTILINE)
CAPTION_RE = re.compile(r"CAPTION \(paste exactly, between the lines\):\n<<<\n(.*?)\n>>>", re.S)
ALT_RE = re.compile(r"^ALT TEXT:\n<<<\n(.*?)\n>>>", re.S | re.MULTILINE)
COMMENT_RE = re.compile(r"FIRST COMMENT \(BY HAND[^)\n]*\):\n<<<\n(.*?)\n>>>", re.S)
FOLDER_NAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})_(\d{4})_([a-z]+)_(.+)$")


def parse_when(block: str) -> datetime:
    m = WHEN_RE.search(block)
    if not m:
        raise ValueError("no parseable WHEN: line")
    mon, day, year, hh, mm, ampm = m.groups()
    hour = int(hh) % 12 + (12 if ampm == "pm" else 0)
    return datetime(int(year), MONTHS[mon.lower()], int(day), hour, int(mm), tzinfo=TORONTO)


def parse_prompt_file(text: str, account: str) -> list[Post]:
    """Return the posts described in one 9x-instagram-*.txt prompt file."""
    pieces = BLOCK_SPLIT.split(text)[1:]  # [0] is the instructions before post 1
    posts: list[Post] = []
    for block in pieces:
        block = block.split("=" * 10, 1)[0]  # drop the trailing "==== END ====" part
        folder_m = FOLDER_RE.search(block)
        cap_m, com_m = CAPTION_RE.search(block), COMMENT_RE.search(block)
        if not (folder_m and cap_m and com_m):
            raise ValueError(f"[{account}] a post block is missing FOLDER, CAPTION or "
                             f"FIRST COMMENT:\n{block[:200]}")
        folder = folder_m.group(1).rstrip("/").split("/")[-1]
        name_m = FOLDER_NAME_RE.match(folder)
        if not name_m:
            raise ValueError(f"[{account}] unexpected folder name {folder!r}")
        brand, post_id = name_m.group(3), name_m.group(4)
        if brand != account:
            raise ValueError(f"[{account}] folder {folder} belongs to {brand}")
        acct_m = ACCOUNT_RE.search(block)
        if acct_m and acct_m.group(1).lower() != USERNAMES[account]:
            raise ValueError(f"[{post_id}] says @{acct_m.group(1)}, expected "
                             f"@{USERNAMES[account]}")
        alt_m = ALT_RE.search(block)
        when_line = WHEN_RE.search(block)
        posts.append(Post(
            id=post_id, account=account, folder=folder, original=parse_when(block),
            caption=cap_m.group(1).strip("\n"), first_comment=com_m.group(1).strip(),
            alt_text=alt_m.group(1).strip() if alt_m else "",
            when_line=block[when_line.start():block.index("\n", when_line.start())]
            .replace("WHEN:", "").strip() if when_line else ""))
    return posts


# --------------------------------------------------------------------------------------
# Scheduling
# --------------------------------------------------------------------------------------

def schedule(posts: list[Post], start: date, pins: dict[str, date],
             defer: list[str]) -> list[str]:
    """Assign new_date to every post (see module docstring). Returns warnings."""
    warnings: list[str] = []
    earliest = min(p.original.date() for p in posts)
    delta = start - earliest
    for acct in TIME_OF_DAY:
        mine = sorted((p for p in posts if p.account == acct), key=lambda p: (p.original, p.id))
        if not mine:
            continue
        acct_pins = {p.id: pins[p.id] for p in mine if p.id in pins}
        taken = set(acct_pins.values())
        if len(taken) != len(acct_pins):
            raise ValueError(f"{acct}: two pinned posts share a day")
        last: date | None = None
        for p in mine:
            if p.id in defer and p.id not in acct_pins:
                continue
            if p.id in acct_pins:
                d = acct_pins[p.id]
                p.notes.append("pinned")
            else:
                d = max(p.original.date() + delta, start)
                if last is not None and d <= last:
                    d = last + timedelta(days=1)
                while d in taken:
                    d += timedelta(days=1)
                taken.add(d)
            p.new_date = d
            last = d if last is None else max(last, d)
        anchor = max(acct_pins.values()) if acct_pins else start - timedelta(days=1)
        for p in mine:
            if p.id in defer and p.id not in acct_pins:
                d = anchor + timedelta(days=1)
                while d in taken:
                    d += timedelta(days=1)
                taken.add(d)
                p.new_date = d
                p.notes.append("deferred")
        # Report posts that were planned before a pinned post but now come after it.
        for p in mine:
            for q in mine:
                if (q.id in acct_pins and p.id not in acct_pins
                        and p.original < q.original and p.new_date > q.new_date):
                    p.notes.append(f"now AFTER {q.id}")
                    warnings.append(f"{p.id} was planned before {q.id} but now goes "
                                    f"out after it (not enough days before the pinned post)")
        for p in mine:
            if p.publish_at.date() < start:
                warnings.append(f"{p.id} lands before the start date")
        days = [p.new_date for p in mine]
        if len(days) != len(set(days)):
            raise AssertionError(f"{acct}: two posts on one day")  # should be impossible
    for p in posts:
        if p.original.hour >= 17:
            p.notes.append(f"was an evening post")
    return warnings


# --------------------------------------------------------------------------------------
# Images
# --------------------------------------------------------------------------------------

def convert_slides(src_folder: Path, dest_folder: Path) -> list[str]:
    """Convert 01.png..NN.png to dest_folder/NN.jpg; return the jpg file names."""
    from PIL import Image  # Pillow is only needed for this local import step

    slides = sorted(p for p in src_folder.iterdir() if re.fullmatch(r"\d{2}\.png", p.name))
    if not slides:
        raise ValueError(f"no numbered slides in {src_folder}")
    if len(slides) > MAX_SLIDES:
        raise ValueError(f"{src_folder.name}: {len(slides)} slides, Instagram allows "
                         f"{MAX_SLIDES}")
    expected = [f"{i:02d}.png" for i in range(1, len(slides) + 1)]
    if [p.name for p in slides] != expected:
        raise ValueError(f"{src_folder.name}: slides are not numbered 01..NN without gaps")
    dest_folder.mkdir(parents=True, exist_ok=True)
    for old in dest_folder.glob("*.jpg"):
        old.unlink()
    names = []
    for png in slides:
        with Image.open(png) as im:
            if im.size != (1080, 1350):
                print(f"  warning: {src_folder.name}/{png.name} is {im.size[0]}x{im.size[1]}, "
                      f"not 1080x1350")
            if im.mode in ("RGBA", "LA", "P"):
                im = im.convert("RGBA")
                bg = Image.new("RGB", im.size, (255, 255, 255))
                bg.paste(im, mask=im.getchannel("A"))
                im = bg
            else:
                im = im.convert("RGB")
            out = dest_folder / (png.stem + ".jpg")
            # Baseline (non-progressive) JPEG, 4:4:4 chroma so slide text stays crisp.
            im.save(out, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=False,
                    subsampling=0)
            names.append(out.name)
    return names


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------

def parse_pin(value: str) -> tuple[str, date]:
    pid, _, d = value.partition("=")
    if not pid or not d:
        raise argparse.ArgumentTypeError("use --pin POST_ID=YYYY-MM-DD")
    return pid.strip(), date.fromisoformat(d.strip()[:10])


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start-date", required=True, type=date.fromisoformat,
                    help="day the earliest posts should go out, e.g. 2026-10-15")
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                    help="folder containing steadfold-<brand>/<post folders>")
    ap.add_argument("--prompts", type=Path, default=DEFAULT_PROMPTS,
                    help="folder containing the 9a/9b/9c-instagram-*.txt prompt files")
    ap.add_argument("--repo", type=Path, default=REPO, help="the autopost repo folder")
    ap.add_argument("--pin", action="append", type=parse_pin, default=[],
                    help="keep POST_ID on this date (repeatable): POST_ID=YYYY-MM-DD")
    ap.add_argument("--defer", action="append", default=[],
                    help="move POST_ID to after the account's pinned posts (repeatable)")
    ap.add_argument("--no-default-rules", action="store_true",
                    help="don't apply the built-in pins/defer for the Oct 2026 week")
    ap.add_argument("--replace", action="store_true",
                    help="replace schedule/posts.json instead of merging into it")
    ap.add_argument("--skip-images", action="store_true", help="don't (re)build media/")
    args = ap.parse_args(argv)

    posts: list[Post] = []
    for acct, fname in PROMPT_FILES.items():
        path = args.prompts / fname
        posts += parse_prompt_file(path.read_text(encoding="utf-8"), acct)
    ids = [p.id for p in posts]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate post ids in the prompt files")

    pins: dict[str, date] = {} if args.no_default_rules else dict(DEFAULT_PINS)
    defer: list[str] = [] if args.no_default_rules else list(DEFAULT_DEFER)
    pins.update(dict(args.pin))
    defer += args.defer
    unknown = [i for i in list(pins) + defer if i not in ids]
    for i in unknown:
        pins.pop(i, None)
    defer = [i for i in defer if i in ids]
    warnings = schedule(posts, args.start_date, pins, defer)

    # Build media and the JSON entries.
    entries = []
    caption_diffs = []
    media_dir = args.repo / "media"
    for p in sorted(posts, key=lambda p: (p.publish_at, p.account)):
        src = args.source / f"steadfold-{p.account}" / p.folder
        if not src.is_dir():
            raise SystemExit(f"post folder not found: {src}")
        old_cap = src / "caption.txt"
        if old_cap.exists() and old_cap.read_text(encoding="utf-8").strip() != p.caption.strip():
            caption_diffs.append(p.id)
        if args.skip_images:
            names = sorted(x.name for x in (media_dir / p.id).glob("*.jpg"))
        else:
            names = convert_slides(src, media_dir / p.id)
        if len(p.caption) > 2200:
            raise SystemExit(f"{p.id}: caption is {len(p.caption)} chars (max 2200)")
        entries.append({
            "id": p.id,
            "account": p.account,
            "publish_at": p.publish_at.isoformat(),
            "caption": p.caption,
            "first_comment": p.first_comment,
            "alt_text": p.alt_text,
            "images": [f"{p.id}/{n}" for n in names],
        })

    posts_file = args.repo / "schedule" / "posts.json"
    existing = []
    if posts_file.exists() and not args.replace:
        raw = json.loads(posts_file.read_text(encoding="utf-8"))
        existing = raw.get("posts", []) if isinstance(raw, dict) else raw
    new_ids = {e["id"] for e in entries}
    merged = [e for e in existing if e["id"] not in new_ids] + entries
    merged.sort(key=lambda e: (e["publish_at"], e["account"]))
    posts_file.parent.mkdir(parents=True, exist_ok=True)
    posts_file.write_text(json.dumps({
        "_about": ("One entry per post. publish_at is Toronto time with its UTC offset. "
                   "images are paths under media/. Built by tools/import_week.py; what has "
                   "already been posted lives in state/published.json, not here."),
        "posts": merged,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Print the table.
    print(f"\nSchedule written to {posts_file} ({len(entries)} imported, "
          f"{len(merged)} total). Times are Toronto (America/Toronto).\n")
    hdr = f"{'#':>2}  {'Date':<10} {'Time':<5} {'Account':<14} {'Post id':<34} {'Sl':>2}  " \
          f"{'Was (prompt WHEN)':<22} Notes"
    print(hdr)
    print("-" * len(hdr))
    by_id = {p.id: p for p in posts}
    for i, e in enumerate(sorted(entries, key=lambda e: e["publish_at"]), 1):
        p = by_id[e["id"]]
        at = p.publish_at
        was = p.original.strftime("%a %b %d %H:%M")
        print(f"{i:>2}  {at.strftime('%a %b %d'):<10} {at.strftime('%H:%M'):<5} "
              f"@{USERNAMES[p.account]:<13} {p.id:<34} {len(e['images']):>2}  {was:<22} "
              f"{', '.join(p.notes)}")
    print()
    for acct in TIME_OF_DAY:
        days = sorted(p.new_date for p in posts if p.account == acct)
        print(f"@{USERNAMES[acct]}: {len(days)} posts, {days[0]:%a %b %d} to "
              f"{days[-1]:%a %b %d}, one per day: {len(days) == len(set(days))}")
    if caption_diffs:
        print(f"\nNote: caption.txt in the post folder differs from the prompt file for "
              f"{len(caption_diffs)} post(s); the prompt file version was used: "
              f"{', '.join(caption_diffs)}")
    for w in warnings:
        print(f"WARNING: {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

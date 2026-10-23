#!/usr/bin/env python3
"""Publish Ledger for steadfold-autopost: post-hoc reconciliation + pre-flight checks. Read-only, stdlib only.

Single-file Python port of the `publish-ledger` rule pack (Steadfold recon core, rules publish-ledger/0.2.0;
TypeScript original: steadfold/src/recon/packs/publish-ledger.ts). Same codes, severities and semantics; the
two implementations are cross-checked on the same inputs (identical (code, key, severity) sets).

Inputs (never written):  schedule/posts.json, state/published.json, insights/latest.json (optional),
                         and a media index (--media-index FILE, one path per line, e.g. from
                         `git ls-tree -r --name-only HEAD media/`; otherwise the files under <repo>/media are listed).

Post-hoc   due_not_published, state_predates_schedule (the Oct 21 class), state_without_platform_media,
           published_not_in_queue, platform_media_not_in_state, duplicate_media_id, duplicate_queue_id,
           late_publish, type_mismatch, account_mismatch, permalink_mismatch, invalid_entry
Pre-flight (upcoming = slot after now and not yet published)
           missing_media (high), duplicate_content_hash, caption_collision_with_published, cap_breach (medium)

Usage:  python3 publish_ledger.py --repo . [--now ISO] [--media-index FILE] [--no-platform] [--ack FILE]
                                  [--late 60] [--grace 60] [--early 15] [--out DIR] [--summary FILE]
--summary defaults to $GITHUB_STEP_SUMMARY when set.
--ack: JSON list of {"code", "key", "reason"} for findings a person has reviewed (e.g. the Oct 21 incident, which
       stays in the history files forever). Acknowledged findings are still reported, but never fail the run;
       acks that no longer match anything are listed as stale.
Exit: 0 = no unacknowledged high findings, 1 = unacknowledged high findings, 2 = bad input.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
from collections import OrderedDict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

RULES_VERSION = "publish-ledger/0.2.0"
VERSION = "0.2.0-py"
TORONTO = ZoneInfo("America/Toronto")
DEFAULT_CEILINGS = {"feed": 2, "reel": 2, "story": 5}
SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2}
CODES = OrderedDict([
    ("due_not_published", "missing"), ("state_predates_schedule", "missing"), ("state_without_platform_media", "missing"),
    ("published_not_in_queue", "extra"), ("platform_media_not_in_state", "extra"),
    ("duplicate_media_id", "duplicate"), ("duplicate_queue_id", "duplicate"), ("late_publish", "late"),
    ("type_mismatch", "mismatch"), ("account_mismatch", "mismatch"), ("permalink_mismatch", "mismatch"),
    ("invalid_entry", "mismatch"), ("missing_media", "missing"), ("duplicate_content_hash", "duplicate"),
    ("caption_collision_with_published", "duplicate"), ("cap_breach", "policy_violation"),
])
EXPECTED_TYPE = {"reel": {"REELS", "REEL", "VIDEO"}, "carousel": {"CAROUSEL_ALBUM"}, "image": {"IMAGE"}}
MIN = 60_000

_TS = re.compile(r"^(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2})(?::(\d{2})(\.\d+)?)?\s*(Z|[+-]\d{2}:?\d{2})?$", re.I)


def parse_ms(v) -> float:
    """ISO 8601 instant → UTC ms. Offset-less times are read as UTC (Autopost writes offsets everywhere). NaN if unreadable."""
    m = _TS.match(str(v or "").strip())
    if not m:
        return math.nan
    y, mo, d, h, mi, s, frac, off = m.groups()
    try:
        dt = datetime(int(y), int(mo), int(d), int(h), int(mi), int(s or 0), tzinfo=timezone.utc)
    except ValueError:
        return math.nan
    ms = dt.timestamp() * 1000 + (round(float(frac) * 1000) if frac else 0)
    if off and off.upper() != "Z":
        sign = -1 if off[0] == "-" else 1
        hh, mm = int(off[1:3]), int(off[-2:])
        ms -= sign * (hh * 60 + mm) * MIN
    return ms


def iso(ms: float) -> str:
    return datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.") + f"{int(ms % 1000):03d}Z"


def toronto_day(ms: float) -> str:
    return datetime.fromtimestamp(ms / 1000, timezone.utc).astimezone(TORONTO).date().isoformat()


def jround(x: float) -> int:
    """JavaScript Math.round (half up), so numbers match the TypeScript pack."""
    return math.floor(x + 0.5)


def normalize_caption(text) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def captions_collide(want: str, have: str) -> bool:
    """Autopost's pre-fix find_existing() rule: equal, or (want longer than 80 chars) the first 300 chars equal."""
    return bool(want) and bool(have) and (have == want or (len(want) > 80 and have[:300] == want[:300]))


def first_line(s) -> str:
    return re.split(r"\r?\n", str(s or ""))[0].strip()


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# ------------------------------------------------------------------ inputs
def parse_inputs(queue_text: str, state_text: str, platform_text: str | None):
    def load(t, name):
        try:
            return json.loads(t.lstrip("﻿"))
        except ValueError as e:
            raise ValueError(f"{name} is not valid JSON ({e}).")
    q, s = load(queue_text, "schedule/posts.json"), load(state_text, "state/published.json")
    p = None if platform_text is None else load(platform_text, "insights/latest.json")
    q_posts = q if isinstance(q, list) else (q.get("posts") if isinstance(q, dict) else None)
    if not isinstance(q_posts, list):
        raise ValueError('schedule/posts.json must be a list of posts or {"posts": [...]}.')
    if not isinstance(s, dict) or not isinstance(s.get("posts"), dict):
        raise ValueError('state/published.json must be {"posts": {<id>: {...}}}.')
    bad, queue = [], []
    for i, x in enumerate(q_posts):
        x = x if isinstance(x, dict) else {}
        pid, at = str(x.get("id") or "").strip(), parse_ms(x.get("publish_at"))
        if not pid or math.isnan(at):
            bad.append((f"queue[{i}]", f"needs an id and a publish_at with an offset (got {json.dumps(x.get('id'))}, {json.dumps(x.get('publish_at'))})"))
            continue
        if x.get("story"):
            kind = "story"
        elif x.get("video"):
            kind = "reel"
        elif isinstance(x.get("images"), list):
            kind = "carousel" if len(x["images"]) > 1 else "image"
        else:
            kind = "image" if x.get("image") else "unknown"
        files = []
        if isinstance(x.get("video"), str):
            files.append(("video", x["video"]))
        if isinstance(x.get("cover"), str):
            files.append(("cover", x["cover"]))
        for im in (x["images"] if isinstance(x.get("images"), list) else []):
            if isinstance(im, str):
                files.append(("image", im))
        if isinstance(x.get("image"), str):
            files.append(("image", x["image"]))
        queue.append({"id": pid, "account": str(x.get("account") or ""), "at": at, "kind": kind,
                      "first_line": first_line(x.get("caption")), "caption": normalize_caption(x.get("caption")), "files": files})
    state = []
    for pid, v in s["posts"].items():
        v = v if isinstance(v, dict) else {}
        state.append({"id": pid, "account": str(v.get("account") or ""), "status": str(v.get("status") or ""),
                      "media_id": str(v.get("media_id") or ""), "at": parse_ms(v.get("published_at")),
                      "permalink": str(v.get("permalink") or ""), "kind": str(v.get("kind") or ""), "recovered": v.get("recovered") is True})
    platform, coverage, collected = [], OrderedDict(), math.nan
    if p is not None:
        collected = parse_ms(p.get("collected_at"))
        if math.isnan(collected):
            raise ValueError("insights/latest.json needs collected_at.")
        for acct, a in (p.get("accounts") or {}).items():
            items = [{"media_id": str(m.get("media_id") or ""), "account": acct, "type": str(m.get("type") or ""), "at": parse_ms(m.get("at")),
                      "permalink": str(m.get("permalink") or ""), "first_line": first_line(m.get("first_line"))} for m in (a.get("posts") or [])]
            platform += items
            ts = [m["at"] for m in items if not math.isnan(m["at"])]
            coverage[acct] = {"from": iso(min(ts)) if ts else None, "to": iso(collected), "mediaInList": len(items),
                              "mediaCount": a.get("media_count") if isinstance(a.get("media_count"), int) else None}
    return queue, state, platform, collected, coverage, bad


# ------------------------------------------------------------------ checks
def run(queue_text: str, state_text: str, platform_text: str | None, now: float, late_min: float = 60, grace_min: float = 60,
        early_min: float = 15, media_index=None, ceilings=None) -> dict:
    if math.isnan(now):
        raise ValueError("--now must be a valid date/time.")
    for k, v in (("late", late_min), ("grace", grace_min), ("early", early_min)):
        if not (isinstance(v, (int, float)) and v >= 0 and not math.isnan(v)):
            raise ValueError(f"--{k} must be a non-negative number.")
    ceilings = ceilings or DEFAULT_CEILINGS
    queue, state, platform, collected, coverage, bad = parse_inputs(queue_text, state_text, platform_text)
    findings = []

    def add(code, key, severity, detail):
        findings.append({"kind": CODES[code], "code": code, "key": key, "severity": severity, "detail": detail})

    for where, why in bad:
        add("invalid_entry", where, "medium", f"Entry {where} {why}; skipped.")
    by_id: dict[str, list] = OrderedDict()
    for q in queue:
        by_id.setdefault(q["id"], []).append(q)
    for pid, items in by_id.items():
        if len(items) > 1:
            add("duplicate_queue_id", pid, "high", f"The queue contains {len(items)} posts with this id; only one can ever be published.")
    by_media = {}
    for m in platform:
        if m["media_id"] and m["media_id"] not in by_media:
            by_media[m["media_id"]] = m
    owners: dict[str, list] = OrderedDict()
    for s in state:
        if s["media_id"]:
            owners.setdefault(s["media_id"], []).append(s)
    for mid, os_ in owners.items():
        if len(os_) > 1:
            add("duplicate_media_id", mid, "high", f"State records {len(os_)} posts as the same platform media: {', '.join(o['id'] for o in os_)}. At most one of them is really on the platform.")

    st_by_id: dict[str, list] = OrderedDict()
    for s in state:
        st_by_id.setdefault(s["id"], []).append(s)
    lateness, check = [], {"stateChecked": 0, "stateStories": 0, "stateOutsideWindow": 0, "stateAfterCollection": 0}
    keys = list(by_id.keys()) + [k for k in st_by_id if k not in by_id]
    for key in keys:
        q = by_id.get(key, [None])[0]
        s = st_by_id.get(key, [None])[0]
        if q is None:
            add("published_not_in_queue", key, "medium", f'State records "{key}" as {s["status"] or "unknown"} (media {s["media_id"] or "none"}), but no queue entry has this id.')
            continue
        due = q["at"] + grace_min * MIN <= now
        if s is None or s["status"] != "published":
            if due:
                st = f'state status is "{s["status"]}"' if s else "no state record"
                add("due_not_published", q["id"], "high", f"Scheduled {iso(q['at'])} for {q['account']}; {st} as of {iso(now)} (grace {grace_min:g} min).")
            continue
        if s["account"] and q["account"] and s["account"] != q["account"]:
            add("account_mismatch", q["id"], "high", f"Queue says account {q['account']}; state says {s['account']}.")
        if math.isnan(s["at"]):
            add("invalid_entry", f"state:{q['id']}", "medium", f'State record for {q["id"]} is "published" without a readable published_at.')
            continue
        delta = s["at"] - q["at"]
        if -delta > early_min * MIN:
            other = [o["id"] for o in owners.get(s["media_id"], []) if o["id"] != q["id"]]
            add("state_predates_schedule", q["id"], "high",
                f"Scheduled {iso(q['at'])}, but state says it was published {iso(s['at'])} — {jround(-delta / 3_600_000 * 10) / 10:g} h before its own slot"
                + (" (recovered: true, i.e. matched to an existing post rather than published by this run)" if s["recovered"] else "")
                + (f"; that media id is also recorded for {', '.join(other)}" if other else "") + ". The scheduled post was most likely never published.")
        else:
            lateness.append(delta / MIN)
            if delta > late_min * MIN:
                add("late_publish", q["id"], "low", f"Published {jround(delta / MIN)} min after its slot ({iso(q['at'])} → {iso(s['at'])}; threshold {late_min:g} min).")
        if platform_text is None:
            continue
        if q["kind"] == "story" or s["kind"] == "story":
            check["stateStories"] += 1
            continue
        cov = coverage.get(s["account"])
        if s["at"] > collected:
            check["stateAfterCollection"] += 1
            continue
        if not cov or not cov["from"] or s["at"] < parse_ms(cov["from"]):
            check["stateOutsideWindow"] += 1
            continue
        check["stateChecked"] += 1
        m = by_media.get(s["media_id"])
        if not m:
            add("state_without_platform_media", q["id"], "medium", f"State says media {s['media_id'] or '(none)'} was published {iso(s['at'])} on {s['account']}, inside the platform list's window, but the platform list has no such media.")
            continue
        if m["account"] != s["account"]:
            add("account_mismatch", q["id"], "high", f"State says {s['account']}; the platform lists media {m['media_id']} under {m['account']}.")
        want = EXPECTED_TYPE.get(q["kind"])
        if want and m["type"] not in want:
            add("type_mismatch", q["id"], "medium", f"Queued as a {q['kind']}, but the media state points to ({m['media_id']}) is a {m['type']} on the platform"
                + (f' ("{m["first_line"][:80]}")' if m["first_line"] else "") + ".")
        if s["permalink"] and m["permalink"] and s["permalink"] != m["permalink"]:
            add("permalink_mismatch", q["id"], "low", f"State permalink {s['permalink']} ≠ platform permalink {m['permalink']}.")

    # ---------------- pre-flight on upcoming posts
    published_ids = {s["id"] for s in state if s["status"] == "published"}
    upcoming = [q for q in queue if q["at"] > now and q["id"] not in published_ids]
    media = None if media_index is None else {re.sub(r"^media/", "", r) for r in media_index}
    if media is not None:
        for q in upcoming:
            for role, rel in q["files"]:
                if rel not in media:
                    add("missing_media", q["id"], "high", f"Upcoming {q['kind']} (slot {iso(q['at'])}) needs media/{rel} ({role}), which is not in the media index. Autopost would reject the post.")
    by_acct: dict[str, list] = OrderedDict()
    for q in upcoming:
        if q["kind"] != "story":
            by_acct.setdefault(q["account"], []).append(q)
    for acct, posts in by_acct.items():
        caps: dict[str, list] = OrderedDict()
        for q in posts:
            if q["caption"]:
                caps.setdefault(sha(q["caption"]), []).append(q)
        for h, same in caps.items():
            if len(same) > 1:
                add("duplicate_content_hash", f"{acct}:caption:{h[:12]}", "medium", f"{len(same)} upcoming posts on {acct} have the same caption (sha256 {h[:12]}…): {', '.join(q['id'] for q in same)}.")
        users: dict[str, list] = OrderedDict()
        for q in posts:
            for role, rel in q["files"]:
                if role != "cover":
                    u = users.setdefault(rel, [])
                    if q["id"] not in u:
                        u.append(q["id"])
        groups: dict[str, list] = OrderedDict()
        for rel, ids in users.items():
            if len(ids) > 1:
                groups.setdefault(",".join(sorted(ids)), []).append(rel)
        for ids, rels in groups.items():
            add("duplicate_content_hash", f"{acct}:media:{ids}", "medium", f"{len(ids.split(','))} upcoming posts on {acct} ({', '.join(ids.split(','))}) use the same media file(s): {', '.join('media/' + r for r in rels)}.")
    published_posts = [q for q in queue if q["id"] in published_ids and q["kind"] != "story" and q["caption"]]
    for q in upcoming:
        if q["kind"] == "story" or not q["caption"]:
            continue
        hits = [p for p in published_posts if p["account"] == q["account"] and p["id"] != q["id"] and captions_collide(q["caption"], p["caption"])]
        if hits:
            add("caption_collision_with_published", q["id"], "medium", f"Upcoming {q['kind']} (slot {iso(q['at'])}) has a caption matching already-published {', '.join(p['id'] for p in hits)} on {q['account']}.")
    cap_kind = lambda q: "story" if q["kind"] == "story" else "reel" if q["kind"] == "reel" else "feed"  # noqa: E731
    up_days = {(q["account"], toronto_day(q["at"])) for q in upcoming}
    per_day: dict[tuple, list] = OrderedDict()
    for q in queue:
        d = (q["account"], toronto_day(q["at"]))
        if d in up_days:
            per_day.setdefault(d + (cap_kind(q),), []).append(q)
    for (acct, day, ck), posts in per_day.items():
        if len(posts) > ceilings[ck]:
            add("cap_breach", f"{acct}:{day}:{ck}", "medium", f"{acct} has {len(posts)} {ck} posts slotted on {day} (Toronto), ceiling {ceilings[ck]}: {', '.join(q['id'] for q in posts)}.")

    # platform media no state entry claims
    if platform_text is not None:
        claimed = {s["media_id"] for s in state}
        first_state = {}
        for s in state:
            if not math.isnan(s["at"]) and (s["account"] not in first_state or s["at"] < first_state[s["account"]]):
                first_state[s["account"]] = s["at"]
        for m in platform:
            if m["media_id"] and m["media_id"] not in claimed:
                before = m["account"] in first_state and m["at"] < first_state[m["account"]]
                add("platform_media_not_in_state", m["media_id"], "low", f"{m['account']} has {m['type']} {m['permalink']} ({iso(m['at']) if not math.isnan(m['at']) else 'time unknown'}) that no state entry claims"
                    + (f"; it predates the earliest state record for this account ({iso(first_state[m['account']])})" if before else "") + ".")

    findings.sort(key=lambda f: (SEVERITY_ORDER[f["severity"]], f["code"], f["key"]))
    srt = sorted(lateness)
    pct = lambda p: jround(srt[min(len(srt) - 1, math.floor(p * len(srt)))]) if srt else None  # noqa: E731
    counts = OrderedDict((c, 0) for c in CODES)
    for f in findings:
        counts[f["code"]] += 1
    inputs = {"schedule/posts.json": queue_text, "state/published.json": state_text}
    if platform_text is not None:
        inputs["insights/latest.json"] = platform_text
    report = OrderedDict([
        ("tool", "steadfold-publish-ledger-py"), ("pack", "publish-ledger"), ("version", VERSION), ("rulesVersion", RULES_VERSION),
        ("now", iso(now)),
        ("notices", ["Read-only reconciliation of the content queue, the publisher's state file and the platform media list. Nothing was posted, edited or deleted."]),
        ("assumptions", [
            f"Pre-flight covers {len(upcoming)} upcoming post(s) (slot after now, not yet published)" + ("" if media is not None else "; no media index given, so missing_media was skipped")
            + f". Ceilings per page per Toronto day: {ceilings['feed']} feed, {ceilings['reel']} Reels, {ceilings['story']} Stories.",
            f"A queue post counts as due {grace_min:g} min after its slot; a publish more than {early_min:g} min before its slot means the state record belongs to something else; late = more than {late_min:g} min after the slot.",
            "The platform list covers only each account's recent media up to collected_at and contains no Stories; state entries outside that window and all Stories are not checked against it."
            if platform_text is not None else "No platform media list given: state ↔ platform checks were skipped."]),
        ("totals", OrderedDict([("queue_posts", len(queue)), ("queue_due", sum(1 for q in queue if q["at"] + grace_min * MIN <= now)),
                                ("state_entries", len(state)), ("state_published", len(published_ids & {s['id'] for s in state})),
                                ("platform_media", len(platform)), ("queue_upcoming", len(upcoming))])),
        ("counts", counts), ("findings", findings),
        ("results", OrderedDict([("checkability", check), ("coverage", coverage), ("recoveredEntries", sorted(s["id"] for s in state if s["recovered"])),
                                 ("latenessMinutes", {"p50": pct(0.5), "p90": pct(0.9), "max": jround(srt[-1]) if srt else None, "over": sum(1 for d in srt if d > late_min)})])),
        ("fingerprints", OrderedDict([("inputs", OrderedDict((k, sha(v)) for k, v in sorted(inputs.items()))), ("report", "")])),
    ])
    report["fingerprints"]["report"] = report_hash(report)
    return report


def load_acks(text: str) -> list[dict]:
    acks = json.loads(text)
    if not isinstance(acks, list) or not all(isinstance(a, dict) and a.get("code") in CODES and isinstance(a.get("key"), str) and str(a.get("reason") or "").strip() for a in acks):
        raise ValueError('--ack must be a JSON list of {"code": <known code>, "key": "...", "reason": "..."} (a reason is required).')
    return acks


def apply_acks(r: dict, acks: list[dict]) -> dict:
    """Marks acknowledged findings (acknowledged: reason) and lists stale acks. Changes no finding's code or severity."""
    by = {(a["code"], a["key"]): a["reason"] for a in acks}
    used = set()
    for f in r["findings"]:
        k = (f["code"], f["key"])
        if k in by:
            f["acknowledged"] = by[k]
            used.add(k)
    r["acks"] = {"applied": len(used), "stale": [{"code": c, "key": k} for (c, k) in by if (c, k) not in used]}
    r["fingerprints"]["report"] = report_hash(r)
    return r


def blocking(r: dict) -> list[dict]:
    return [f for f in r["findings"] if f["severity"] == "high" and not f.get("acknowledged")]


def report_hash(r: dict) -> str:
    """sha256 of the report's canonical JSON (sorted keys, compact) with fingerprints.report blanked. Python-defined; not the TS hash."""
    c = json.loads(json.dumps(r))
    c["fingerprints"]["report"] = ""
    return sha(json.dumps(c, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


def to_markdown(r: dict, title: str = "Publish Ledger") -> str:
    esc = lambda v: str(v).replace("\n", " ").replace("|", "\\|").replace("<", "&lt;")  # noqa: E731
    L = [f"## {title}", "", *[f"> {n}" for n in r["notices"]], ""]
    high = sum(1 for f in r["findings"] if f["severity"] == "high")
    L += [f"**{len(r['findings'])} findings, {high} high, {len(blocking(r))} blocking (high and not acknowledged)** · rules {r['rulesVersion']} · as of {r['now']}", ""]
    L += [f"- {k.replace('_', ' ')}: {v}" for k, v in r["totals"].items()]
    L += ["", "| Finding | Kind | Count |", "|---|---|---|"] + [f"| {c.replace('_', ' ')} | {CODES[c].replace('_', ' ')} | {n} |" for c, n in r["counts"].items()]
    L += ["", "### Findings", ""] + ([f"- **{f['severity'].upper()} · {f['code']}** `{f['key'].replace('`', chr(39))}`: {esc(f['detail'])}"
                                      + (f" _(acknowledged: {esc(f['acknowledged'])})_" if f.get("acknowledged") else "") for f in r["findings"][:300]] or ["None."])
    if len(r["findings"]) > 300:
        L.append(f"- … {len(r['findings']) - 300} more in report.json.")
    if r.get("acks", {}).get("stale"):
        L += ["", "### Stale acknowledgements (match nothing any more; remove them)", ""] + [f"- `{a['code']}` `{a['key']}`" for a in r["acks"]["stale"]]
    L += ["", "### Assumptions", ""] + [f"- {a}" for a in r["assumptions"]]
    L += ["", "### Evidence (SHA-256)", ""] + [f"- `{k}`: `{v}`" for k, v in r["fingerprints"]["inputs"].items()] + [f"- report: `{r['fingerprints']['report']}`"]
    return "\n".join(L) + "\n"


def list_media(repo: Path) -> list[str]:
    root = repo / "media"
    return [p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()] if root.is_dir() else []


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Publish Ledger (read-only).")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--now", help="ISO 8601 with offset; default: the current UTC time")
    ap.add_argument("--media-index")
    ap.add_argument("--no-platform", action="store_true")
    ap.add_argument("--late", type=float, default=60)
    ap.add_argument("--grace", type=float, default=60)
    ap.add_argument("--early", type=float, default=15)
    ap.add_argument("--ack", help="JSON list of reviewed findings that must not fail the run")
    ap.add_argument("--out", help="directory for report.json / report.md (must be outside the repo)")
    ap.add_argument("--summary", default=os.environ.get("GITHUB_STEP_SUMMARY"))
    a = ap.parse_args(argv)
    try:
        repo = Path(a.repo).resolve()
        now = parse_ms(a.now) if a.now else datetime.now(timezone.utc).timestamp() * 1000
        if a.now and math.isnan(now):
            raise ValueError(f'--now "{a.now}" is not an ISO 8601 date/time.')
        read = lambda rel: (repo / rel).read_text(encoding="utf-8")  # noqa: E731
        ins = repo / "insights" / "latest.json"
        platform = None if a.no_platform or not ins.exists() else read("insights/latest.json")
        if a.media_index:
            index = [l.strip() for l in Path(a.media_index).read_text(encoding="utf-8").splitlines() if l.strip()]
        else:
            index = list_media(repo) if (repo / "media").is_dir() else None
        r = run(read("schedule/posts.json"), read("state/published.json"), platform, now, a.late, a.grace, a.early, index)
        if a.ack:
            apply_acks(r, load_acks(Path(a.ack).read_text(encoding="utf-8")))
        if a.out:
            out = Path(a.out).resolve()
            if out == repo or repo in out.parents:
                raise ValueError("--out must be outside the repo (this tool never writes into it).")
            out.mkdir(parents=True, exist_ok=True)
            (out / "report.json").write_text(json.dumps(r, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            (out / "report.md").write_text(to_markdown(r), encoding="utf-8")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"publish_ledger: {exc}", file=sys.stderr)
        return 2
    md = to_markdown(r)
    if a.summary:
        with open(a.summary, "a", encoding="utf-8") as f:
            f.write(md)
    high = blocking(r)
    nonzero = ", ".join(f"{c} {n}" for c, n in r["counts"].items() if n) or "none"
    print(f"Publish ledger: {r['totals']['queue_posts']} queued, {r['totals']['queue_upcoming']} upcoming, {r['totals']['state_published']} published — "
          f"{len(r['findings'])} findings ({len(high)} blocking): {nonzero}")
    for f in high:
        print(f"HIGH {f['code']} {f['key']}: {f['detail']}")
    return 1 if high else 0


if __name__ == "__main__":
    sys.exit(main())

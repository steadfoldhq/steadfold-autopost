#!/usr/bin/env python3
"""
Steadfold Autopost: collect performance data for every account, so the studios can learn.

Runs in GitHub Actions (.github/workflows/insights.yml) a few times a day. For each
account it reads, using that account's own token (never printed):

  - profile: followers_count, follows_count, media_count
  - the latest 40 posts: type, permalink, time, like_count, comments_count
  - per-post insights where the token allows it: views, reach, saved, shares,
    total_interactions (+ Reels watch time)
  - per-post comment text (no usernames: we keep only text, time, likes and whether
    it was our own comment), so studios can read what people ask for.

It writes insights/latest.json (overwritten) and appends one compact line per account
to insights/history.jsonl. Anything the token is not allowed to read is recorded as an
"error" string instead of crashing, so a missing permission shows up in the data.

    python insights.py              # all accounts with a token in the environment
    python insights.py --out DIR    # write somewhere else (tests)
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from autopost import ACCOUNTS, IGClient, IGError, log

MEDIA_FIELDS = "id,media_type,media_product_type,permalink,timestamp,like_count,comments_count,caption"
POST_METRICS = ["views", "reach", "saved", "shares", "total_interactions"]
REEL_EXTRA = ["ig_reels_avg_watch_time", "ig_reels_video_view_total_time"]
MAX_MEDIA = 40
MAX_COMMENTS = 50


def _get(client: IGClient, path: str, params: dict | None = None) -> dict:
    return client._request("GET", path, params=params or {})


def post_insights(client: IGClient, media_id: str, is_reel: bool) -> dict:
    metrics = POST_METRICS + (REEL_EXTRA if is_reel else [])
    out: dict[str, Any] = {}
    try:
        body = _get(client, f"{media_id}/insights", {"metric": ",".join(metrics)})
        for row in body.get("data", []):
            vals = row.get("values") or [{}]
            out[row.get("name")] = row.get("total_value", {}).get("value", vals[0].get("value"))
        return out
    except IGError:
        pass
    # One metric at a time, so one unsupported metric doesn't hide the rest.
    for m in metrics:
        try:
            body = _get(client, f"{media_id}/insights", {"metric": m})
            row = (body.get("data") or [{}])[0]
            vals = row.get("values") or [{}]
            out[m] = row.get("total_value", {}).get("value", vals[0].get("value"))
        except IGError as exc:
            out.setdefault("errors", {})[m] = str(exc)[:160]
    return out


def comments(client: IGClient, media_id: str, own_username: str) -> list[dict] | str:
    try:
        body = _get(client, f"{media_id}/comments",
                    {"fields": "text,timestamp,like_count,username", "limit": MAX_COMMENTS})
    except IGError as exc:
        return f"error: {str(exc)[:160]}"
    rows = []
    for c in body.get("data", []):
        rows.append({"text": c.get("text", ""), "at": c.get("timestamp"),
                     "likes": c.get("like_count", 0),
                     "ours": (c.get("username") or "").lower() == own_username.lower()})
    return rows


def collect_account(key: str, client: IGClient) -> dict:
    me = client.me()
    acct: dict[str, Any] = {"account": key, "username": me["username"]}
    try:
        prof = _get(client, "me", {"fields": "followers_count,follows_count,media_count"})
        acct.update({k: prof.get(k) for k in ("followers_count", "follows_count", "media_count")})
    except IGError as exc:
        acct["profile_error"] = str(exc)[:160]
    posts = []
    try:
        body = _get(client, f"{me['user_id']}/media", {"fields": MEDIA_FIELDS, "limit": MAX_MEDIA})
        media = body.get("data", [])
    except IGError as exc:
        acct["media_error"] = str(exc)[:160]
        media = []
    for m in media:
        is_reel = m.get("media_product_type") == "REELS"
        posts.append({
            "media_id": m.get("id"),
            "type": "REEL" if is_reel else m.get("media_type"),
            "permalink": m.get("permalink"),
            "at": m.get("timestamp"),
            "first_line": (m.get("caption") or "").split("\n", 1)[0][:140],
            "likes": m.get("like_count"),
            "comments_count": m.get("comments_count"),
            "insights": post_insights(client, m["id"], is_reel),
            "comments": comments(client, m["id"], me["username"]) if m.get("comments_count") else [],
        })
    acct["posts"] = posts
    return acct


def summary_line(acct: dict, now: str) -> dict:
    tot = {"views": 0, "reach": 0, "saved": 0, "shares": 0, "likes": 0, "comments": 0}
    for p in acct.get("posts", []):
        ins = p.get("insights", {})
        for k in ("views", "reach", "saved", "shares"):
            if isinstance(ins.get(k), (int, float)):
                tot[k] += ins[k]
        tot["likes"] += p.get("likes") or 0
        tot["comments"] += p.get("comments_count") or 0
    return {"at": now, "account": acct["account"], "followers": acct.get("followers_count"),
            "posts": len(acct.get("posts", [])), **tot}


def main(argv: list[str] | None = None, env: dict | None = None, session: Any = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--out", default="insights")
    args = ap.parse_args(argv)
    env = env if env is not None else dict(os.environ)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    report: dict[str, Any] = {"collected_at": now, "accounts": {}}
    lines = []
    for key, info in ACCOUNTS.items():
        token = (env.get(info["token_env"]) or "").strip()
        if not token:
            report["accounts"][key] = {"error": f"{info['token_env']} not set"}
            continue
        try:
            acct = collect_account(key, IGClient(token, session=session))
        except IGError as exc:
            report["accounts"][key] = {"error": str(exc)[:200]}
            log(f"[{key}] could not collect: {str(exc)[:200]}")
            continue
        report["accounts"][key] = acct
        lines.append(summary_line(acct, now))
        log(f"[{key}] @{acct['username']}: {len(acct['posts'])} posts, followers {acct.get('followers_count')}")
    (out / "latest.json").write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    with (out / "history.jsonl").open("a") as f:
        for line in lines:
            f.write(json.dumps(line) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

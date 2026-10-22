"""Read-only probe: can our tokens reach Instagram's licensed audio library (Audio API)?

For each account it asks GET /ig_audio for trending music and trending original sounds,
plus a few mood searches, and writes titles/artists/ids/durations to insights/audio-probe.json.
It never posts and never prints tokens. Errors are recorded, not raised.

    python tools/audio_probe.py
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from autopost import ACCOUNTS, IGClient, IGError  # noqa: E402

SEARCHES = ["lullaby", "calm piano", "lofi", "acoustic", "focus", "upbeat"]
KEEP = ("id", "title", "artist_name", "display_artist", "duration_in_ms", "is_explicit")


def _slim(body: dict) -> list[dict]:
    out = []
    for item in (body.get("data") or [])[:15]:
        out.append({k: item.get(k) for k in KEEP if k in item} or {"keys": sorted(item)[:12]})
    return out


def probe(client: IGClient) -> dict:
    res: dict = {}
    try:
        me = client._request("GET", "me", params={"fields": "user_id,username,account_type"})
        res["me"] = {k: me.get(k) for k in ("username", "account_type")}
        uid = me.get("user_id") or me.get("id")
    except IGError as e:
        return {"error": str(e)[:300]}
    calls = {"trending_music": {"audio_type": "music"},
             "trending_original": {"audio_type": "original_sound"}}
    for q in SEARCHES:
        calls[f"music:{q}"] = {"audio_type": "music", "search_query": q}
    for name, params in calls.items():
        try:
            body = client._request("GET", "ig_audio", params={**params, "user_id": uid})
            res[name] = _slim(body)
        except IGError as e:
            res[name] = {"error": str(e)[:300]}
            if name == "trending_music":
                break  # the endpoint is not reachable with this token; don't hammer it
    return res


def main() -> int:
    out = {"checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "accounts": {}}
    for key, info in ACCOUNTS.items():
        token = os.environ.get(info["token_env"], "").strip()
        if not token:
            out["accounts"][key] = {"error": "no token in env"}
            continue
        out["accounts"][key] = probe(IGClient(token))
    path = Path("insights/audio-probe.json")
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    for k, v in out["accounts"].items():
        tm = v.get("trending_music")
        print(k, "OK" if isinstance(tm, list) else f"ERR {str(tm or v.get('error'))[:160]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

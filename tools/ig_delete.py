"""Delete published Instagram posts by post id (from state/published.json). Usage: python tools/ig_delete.py <post-id> [...]
Uses the Instagram API with Instagram Login (DELETE /<media-id>). Marks each deleted post in state/published.json."""
import json, os, sys, urllib.request, urllib.error
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "state", "published.json")
VER = os.environ.get("IG_API_VERSION", "").strip() or "v25.0"
st = json.load(open(STATE))
rc = 0
for pid in sys.argv[1:]:
    rec = st["posts"].get(pid)
    if not rec or not rec.get("media_id"):
        print(f"::error::{pid}: no published media id"); rc = 1; continue
    tok = os.environ.get(f"IG_TOKEN_{rec['account'].upper()}", "").strip()
    req = urllib.request.Request(f"https://graph.instagram.com/{VER}/{rec['media_id']}?access_token={tok}", method="DELETE")
    try:
        body = urllib.request.urlopen(req, timeout=60).read().decode()
        print(f"{pid}: deleted ({body})")
        rec["status"] = "deleted"; rec["deleted_media_id"] = rec.pop("media_id")
    except urllib.error.HTTPError as e:
        print(f"::error::{pid}: HTTP {e.code} {e.read().decode()[:300]}"); rc = 1
json.dump(st, open(STATE, "w"), indent=2); open(STATE, "a").write("\n")
sys.exit(rc)

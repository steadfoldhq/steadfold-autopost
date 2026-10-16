"""Voiceover with ElevenLabs text-to-speech (with word timings for captions).

Runs inside GitHub Actions only. The key comes from the ELEVENLABS_API_KEY
secret and is never printed.

Usage: python3 tools/eleventts.py spec.json
spec.json: {"out": "media/voice/shortform", "model": "eleven_multilingual_v2",
            "items": [{"name": "ff-s1", "voice_id": "...", "text": "...",
                       "settings": {"stability": 0.45, "similarity_boost": 0.8, "style": 0.25}}]}
Output per item: <out>/<name>.mp3 and <out>/<name>.json (character timings).
Also writes <out>/_voices.json (premade voice names + ids, no secrets).
"""
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request

BASE = "https://api.elevenlabs.io/v1"


def call(url, key, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET",
                                 headers={"xi-api-key": key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())


def main(path):
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY missing")
    spec = json.load(open(path))
    out = spec.get("out", "media/voice/shortform")
    os.makedirs(out, exist_ok=True)
    log = open(f"{out}/_last-run.txt", "w")
    try:
        v = call(f"{BASE}/voices", key)
        voices = [{"name": x.get("name"), "voice_id": x.get("voice_id"),
                   "category": x.get("category"), "labels": x.get("labels")} for x in v.get("voices", [])]
        json.dump(voices, open(f"{out}/_voices.json", "w"), indent=1)
    except Exception as e:  # voices list is optional
        log.write(f"voices: {type(e).__name__}\n")
    for it in spec["items"]:
        name = it["name"]
        if not re.fullmatch(r"[a-z0-9-]{2,60}", name):
            sys.exit(f"bad name {name!r}")
        body = {"text": it["text"], "model_id": it.get("model", spec.get("model", "eleven_multilingual_v2")),
                "voice_settings": it.get("settings", {"stability": 0.45, "similarity_boost": 0.8, "style": 0.2,
                                                       "use_speaker_boost": True})}
        url = f"{BASE}/text-to-speech/{it['voice_id']}/with-timestamps?output_format=mp3_44100_128"
        try:
            res = call(url, key, body)
        except urllib.error.HTTPError as e:
            msg = f"{name}: HTTP {e.code} {e.read()[:300]!r}"
            print(msg); log.write(msg + "\n"); continue
        open(f"{out}/{name}.mp3", "wb").write(base64.b64decode(res["audio_base64"]))
        json.dump({"text": it["text"], "alignment": res.get("alignment"),
                   "normalized_alignment": res.get("normalized_alignment")}, open(f"{out}/{name}.json", "w"))
        msg = f"{name}: ok"
        print(msg); log.write(msg + "\n")
    log.close()


if __name__ == "__main__":
    main(sys.argv[1])

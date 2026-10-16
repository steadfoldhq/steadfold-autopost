"""Generate instrumental tracks with ElevenLabs Eleven Music.

Runs inside GitHub Actions only. The key comes from the ELEVENLABS_API_KEY
secret and is never printed.

Usage: python3 tools/elevenmusic.py spec.json
spec.json is a list of entries: {"name": "ff-curious-01", "prompt": "...", "seconds": 20}
Output: media/music/library/<name>.mp3
"""
import json
import os
import re
import sys
import urllib.request

API = "https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128"
SFX_API = "https://api.elevenlabs.io/v1/sound-generation?output_format=mp3_44100_128"
OUT = "media/music/library"


def main(path):
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY missing")
    os.makedirs(OUT, exist_ok=True)
    spec = json.load(open(path))
    failed = 0
    log = open(f"{OUT}/_last-run.txt", "w")
    for item in spec:
        name = item["name"]
        if not re.fullmatch(r"[a-z0-9-]{3,60}", name):
            sys.exit(f"bad name {name!r}")
        if item.get("type") == "sfx":
            url, body = SFX_API, json.dumps({
                "text": item["prompt"],
                "duration_seconds": item.get("seconds", 1.0),
                "prompt_influence": 0.5,
            }).encode()
        else:
            url, body = API, json.dumps({
                "prompt": item["prompt"],
                "music_length_ms": int(item.get("seconds", 20) * 1000),
                "force_instrumental": True,
            }).encode()
        req = urllib.request.Request(url, data=body, method="POST", headers={
            "xi-api-key": key, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                data = r.read()
        except urllib.error.HTTPError as e:
            msg = f"{name}: HTTP {e.code} {e.read()[:400]!r}"
            print(msg)
            log.write(msg + "\n")
            failed += 1
            continue
        with open(f"{OUT}/{name}.mp3", "wb") as f:
            f.write(data)
        print(f"{name}: {len(data)} bytes")
        log.write(f"{name}: ok {len(data)} bytes\n")
    log.close()


if __name__ == "__main__":
    main(sys.argv[1])

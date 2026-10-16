"""Voiceover with ElevenLabs text-to-speech (with word timings for captions).

Runs inside GitHub Actions only. The key comes from the ELEVENLABS_API_KEY
secret and is never printed (error bodies are trimmed and the key never appears in them).

Usage: python3 tools/eleventts.py spec.json
spec.json:
  {"out": "media/voice/shortform",
   "model": "eleven_v3",                      # default model for every item ("eleven_multilingual_v2" still works)
   "settings": {"stability": 0.5},            # default voice settings (item "settings" are merged over these)
   "voices": "tools/voices.json",             # optional: lets an item say "voice": "<house name>" instead of voice_id
   "shared_search": [{"gender": "female", "age": "young", "use_cases": "social_media"}],   # optional, read-only
   "add_shared": [{"public_owner_id": "...", "voice_id": "...", "name": "..."}],           # optional: add a Voice Library voice
   "items": [{"name": "ff-s1", "voice": "mia", "text": "[curious] ...", "takes": 1, "seed": 7}]}

One item = ONE continuous take (no stitching). The text may carry Eleven v3 audio tags ([excited], [sighs],
[laughs], [whispers], [curious] ...) and ellipses for natural pauses. Tags are kept out of the caption timings.

Output per item: <out>/<name>.mp3 and <out>/<name>.json (character timings, tags removed).
takes > 1 writes <name>.mp3, <name>-t2.mp3 ... so the renderer can pick the best take.
Also writes <out>/_voices.json (account voices, no secrets) and <out>/_shared.json when shared_search is set.

Eleven v3 notes (docs: elevenlabs.io/docs/best-practices/prompting):
- stability is one of 0.0 Creative / 0.5 Natural / 1.0 Robust; we snap to the nearest. Natural or Creative
  respond best to audio tags. No SSML <break>; use "..." for pauses.
- If the with-timestamps call is refused for a model, we fall back to plain TTS + the forced-alignment API.
"""
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid

BASE = "https://api.elevenlabs.io/v1"
TAG = re.compile(r"\[[^\]]{1,40}\]\s*")
V3_STAB = (0.0, 0.5, 1.0)
MAX_CHARS = 3000   # one request = one take; keep well inside the model limit


def _req(url, key, body=None, method=None, raw=None, ctype="application/json"):
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    req = urllib.request.Request(url, data=data, method=method or ("POST" if data else "GET"),
                                 headers={"xi-api-key": key, "Content-Type": ctype})
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read()


def call(url, key, body=None, method=None):
    return json.loads(_req(url, key, body, method))


def strip_tags(text):
    return re.sub(r"\s{2,}", " ", TAG.sub("", text)).strip()


def settings_for(model, s):
    s = dict(s)
    if model == "eleven_v3":
        if "stability" in s:
            s["stability"] = min(V3_STAB, key=lambda v: abs(v - float(s["stability"])))
        s = {k: v for k, v in s.items() if k in ("stability", "similarity_boost", "use_speaker_boost")}
    return s


def forced_alignment(key, mp3, text):
    """Plain-TTS fallback: character timings from the forced-alignment API, in the with-timestamps shape."""
    b = uuid.uuid4().hex
    body = (f"--{b}\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\n{text}\r\n"
            f"--{b}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"v.mp3\"\r\n"
            f"Content-Type: audio/mpeg\r\n\r\n").encode() + mp3 + f"\r\n--{b}--\r\n".encode()
    res = json.loads(_req(f"{BASE}/forced-alignment", key, raw=body, ctype=f"multipart/form-data; boundary={b}"))
    ch = res.get("characters", [])
    return {"characters": [c["text"] for c in ch],
            "character_start_times_seconds": [c["start"] for c in ch],
            "character_end_times_seconds": [c["end"] for c in ch]}


def clean_alignment(al):
    """Drop [tag] characters (and the space after them) so captions never show a tag."""
    if not al:
        return al
    ch, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    prev_space, skip_space, depth, k2 = True, False, 0, []
    for i, c in enumerate(ch):
        if c == "[":
            depth = 1
            continue
        if depth == 1:
            if c == "]":
                depth = 0
                skip_space = True
            continue
        if skip_space and c.isspace():
            continue
        skip_space = False
        if c.isspace() and prev_space:
            continue
        prev_space = c.isspace()
        k2.append(i)
    return {"characters": [ch[i] for i in k2], "character_start_times_seconds": [st[i] for i in k2],
            "character_end_times_seconds": [en[i] for i in k2]}


def tts(key, voice_id, text, model, settings, seed=None):
    body = {"text": text, "model_id": model, "voice_settings": settings}
    if seed is not None:
        body["seed"] = int(seed)
    q = "?output_format=mp3_44100_128"
    try:
        res = call(f"{BASE}/text-to-speech/{voice_id}/with-timestamps{q}", key, body)
        return base64.b64decode(res["audio_base64"]), res.get("alignment"), res.get("normalized_alignment"), "timestamps"
    except urllib.error.HTTPError as e:
        if e.code not in (400, 404, 422):
            raise
        first = f"with-timestamps HTTP {e.code} {e.read()[:200]!r}"
    mp3 = _req(f"{BASE}/text-to-speech/{voice_id}{q}", key, body)
    try:
        al = forced_alignment(key, mp3, strip_tags(text))
        return mp3, al, None, "forced-alignment (" + first + ")"
    except urllib.error.HTTPError as e:
        return mp3, None, None, f"no timings: {first}; forced-alignment HTTP {e.code}"


def main(path):
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY missing")
    spec = json.load(open(path))
    out = spec.get("out", "media/voice/shortform")
    os.makedirs(out, exist_ok=True)
    log = open(f"{out}/_last-run.txt", "w")

    def say(msg):
        print(msg)
        log.write(msg + "\n")

    house = {}
    if spec.get("voices") and os.path.exists(spec["voices"]):
        house = {v["name"].lower(): v["voice_id"] for v in json.load(open(spec["voices"])).get("voices", [])}

    for q in spec.get("shared_search", []):
        try:
            qs = urllib.parse.urlencode(dict({"page_size": 30, "language": "en", "sort": "usage_character_count_7d"}, **q))
            res = call(f"{BASE}/shared-voices?{qs}", key)
            rows = [{k: v.get(k) for k in ("public_owner_id", "voice_id", "name", "gender", "age", "accent", "descriptive",
                                           "use_case", "category", "description", "usage_character_count_7d",
                                           "cloned_by_count", "preview_url", "verified_languages")}
                    for v in res.get("voices", [])]
            prev = json.load(open(f"{out}/_shared.json")) if os.path.exists(f"{out}/_shared.json") else []
            json.dump(prev + [{"query": q, "voices": rows}], open(f"{out}/_shared.json", "w"), indent=1)
            say(f"shared {q}: {len(rows)}")
        except urllib.error.HTTPError as e:
            say(f"shared {q}: HTTP {e.code} {e.read()[:200]!r}")

    for a in spec.get("add_shared", []):
        try:
            res = call(f"{BASE}/voices/add/{a['public_owner_id']}/{a['voice_id']}", key, {"new_name": a["name"]})
            say(f"added {a['name']}: {res.get('voice_id')}")
            house[a["name"].lower()] = res.get("voice_id")
        except urllib.error.HTTPError as e:
            say(f"add {a['name']}: HTTP {e.code} {e.read()[:200]!r}")

    try:
        v = call(f"{BASE}/voices", key)
        voices = [{"name": x.get("name"), "voice_id": x.get("voice_id"),
                   "category": x.get("category"), "labels": x.get("labels")} for x in v.get("voices", [])]
        json.dump(voices, open(f"{out}/_voices.json", "w"), indent=1)
        for x in voices:
            house.setdefault((x["name"] or "").split(" - ")[0].lower(), x["voice_id"])
    except Exception as e:  # voices list is optional
        say(f"voices: {type(e).__name__}")

    base_settings = spec.get("settings", {"stability": 0.5, "similarity_boost": 0.8, "use_speaker_boost": True})
    for it in spec.get("items", []):
        name = it["name"]
        if not re.fullmatch(r"[a-z0-9-]{2,60}", name):
            sys.exit(f"bad name {name!r}")
        if len(it["text"]) > MAX_CHARS:
            sys.exit(f"{name}: {len(it['text'])} chars is too long for one take")
        vid = it.get("voice_id") or house.get(str(it.get("voice", "")).lower())
        if not vid:
            say(f"{name}: unknown voice {it.get('voice')!r}")
            continue
        model = it.get("model", spec.get("model", "eleven_multilingual_v2"))
        st = settings_for(model, dict(base_settings, **it.get("settings", {})))
        for k in range(int(it.get("takes", 1))):
            nm = name if k == 0 else f"{name}-t{k + 1}"
            seed = it.get("seed")
            seed = None if seed is None else int(seed) + k
            try:
                mp3, al, nal, how = tts(key, vid, it["text"], model, st, seed)
            except urllib.error.HTTPError as e:
                say(f"{nm}: HTTP {e.code} {e.read()[:300]!r}")
                continue
            open(f"{out}/{nm}.mp3", "wb").write(mp3)
            json.dump({"text": it["text"], "spoken": strip_tags(it["text"]), "model": model, "voice_id": vid,
                       "settings": st, "seed": seed, "timings": how,
                       "alignment": clean_alignment(al), "normalized_alignment": clean_alignment(nal)},
                      open(f"{out}/{nm}.json", "w"))
            say(f"{nm}: ok ({model}, {how}, {len(mp3)} bytes)")
    log.close()


if __name__ == "__main__":
    main(sys.argv[1])

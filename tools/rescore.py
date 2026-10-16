"""Swap the music on queued, unpublished Reels to the picked library tracks.

    python3 tools/rescore.py                 # dry run: shows what would change
    python3 tools/rescore.py --apply         # re-scores and rewrites the Reel MP4s in media/reels/
    python3 tools/rescore.py --apply --only lf-reel-1017am-read,hb-reel-1018-school-email

Picks live in tools/music-picks.json:  {"fullyfunded": ["v3/ff-c-confident-build-el.mp3", ...], ...}
Each Reel gets one track from its page's list (alternating in publish order), so a
page's Reels don't all sound the same. Optional per-Reel override, and Reels to leave alone (e.g. edits cut to their own beat):
  {"overrides": {"<reel id>": "v3/lh-c-morning-drive-el.mp3"}, "keep": ["<reel id>"]}

What it does, per Reel:
- Only Reels (posts with "video", not stories) whose publish_at is still in the
  future and whose id is NOT in state/published.json. state/ is read, never written.
- Voiceover is kept: if media/reels/<id>-vo.(wav|mp3|m4a) exists, the VO is
  laid on top at -16 LUFS and the music is ducked under it (sidechain, about
  -8 dB while the voice speaks). Our current Reels carry music only (no VO
  track), so without a sidecar the old music is simply replaced.
- Music is looped to the Reel length, 0.05 s fade-in, 0.8 s fade-out.
- Video stream is copied untouched; it's re-encoded (x264, CRF stepped up) only
  if the file would exceed 19 MB. AAC 192 kbps, 48 kHz.
- The pre-rescore audio is kept once as media/reels/_orig-audio/<id>.m4a so a
  rescore can always be undone.
- Writes media/music/rescore-log.json.
Never publishes anything.
"""
import argparse
import datetime as dt
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEDIA = ROOT / "media"
LIB = MEDIA / "music" / "library"   # picks are paths relative to this folder, e.g. "v3/ff-c-confident-build-el.mp3"
MAX_BYTES = 19_000_000


def probe_duration(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True, check=True).stdout.strip())


def queued_reels(now):
    posts = json.load(open(ROOT / "schedule/posts.json"))["posts"]
    published = json.load(open(ROOT / "state/published.json")).get("posts", {})
    out = []
    for p in posts:
        if not p.get("video") or p.get("story") or p["id"] in published:
            continue
        if dt.datetime.fromisoformat(p["publish_at"]) <= now:
            continue
        out.append(p)
    return out


def pick_for(reel, picks, counters):
    """Alternate through the page's list in publish order, so neighbouring Reels sound different."""
    if reel["id"] in picks.get("overrides", {}):
        return picks["overrides"][reel["id"]]
    choices = picks.get(reel["account"]) or []
    if not choices:
        return None
    i = counters.get(reel["account"], 0)
    counters[reel["account"]] = i + 1
    return choices[i % len(choices)]


def find_vo(vid):
    for ext in ("wav", "mp3", "m4a"):
        p = vid.with_name(f"{vid.stem}-vo.{ext}")
        if p.exists():
            return p
    return None


def rescore(vid, track, dur, vo=None):
    tmp = vid.with_suffix(".rescore.mp4")
    fade = f"afade=t=in:d=0.05,afade=t=out:st={max(0, dur - 0.8):.3f}:d=0.8"
    inputs = ["-i", str(vid), "-stream_loop", "-1", "-i", str(track)]
    if vo:
        inputs += ["-i", str(vo)]
        fc = (f"[1:a]atrim=0:{dur:.3f},asetpts=PTS-STARTPTS,volume=-2dB[m];"
              f"[2:a]loudnorm=I=-16:TP=-1.5,apad,atrim=0:{dur:.3f}[v];[v]asplit[v1][v2];"
              f"[m][v1]sidechaincompress=threshold=0.03:ratio=6:attack=15:release=300[md];"
              f"[md][v2]amix=inputs=2:normalize=0,{fade},alimiter=limit=0.89[a]")
    else:
        fc = f"[1:a]atrim=0:{dur:.3f},asetpts=PTS-STARTPTS,{fade},alimiter=limit=0.89[a]"
    for crf in (None, 21, 23, 25, 27):
        venc = ["-c:v", "copy"] if crf is None else ["-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
                                                       "-pix_fmt", "yuv420p", "-r", "30"]
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", fc, "-map", "0:v:0",
                        "-map", "[a]", *venc, "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", f"{dur:.3f}",
                        "-movflags", "+faststart", str(tmp)], check=True)
        if tmp.stat().st_size <= MAX_BYTES:
            break
    else:
        tmp.unlink()
        raise RuntimeError(f"{vid.name}: still over 19 MB")
    return tmp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", default="")
    ap.add_argument("--picks", default=str(ROOT / "tools/music-picks.json"))
    a = ap.parse_args()
    picks = json.load(open(a.picks))
    now = dt.datetime.now(dt.timezone.utc)
    only = {x for x in a.only.split(",") if x}
    log, counters = [], {}
    for reel in sorted(queued_reels(now), key=lambda r: r["publish_at"]):
        if only and reel["id"] not in only:
            continue
        if reel["id"] in picks.get("keep", []):
            print(f"keep {reel['id']}: cut to its own beat, music left as is")
            continue
        vid = MEDIA / reel["video"]
        track = pick_for(reel, picks, counters)
        if not track or not vid.exists():
            print(f"skip {reel['id']}: {'no pick for ' + reel['account'] if not track else 'missing video'}")
            continue
        tpath = LIB / track
        if not tpath.exists():
            sys.exit(f"missing track {tpath}")
        vo = find_vo(vid)
        dur = probe_duration(vid)
        line = {"id": reel["id"], "publish_at": reel["publish_at"], "track": track, "voiceover": bool(vo), "seconds": dur}
        if a.apply:
            backup = MEDIA / "reels" / "_orig-audio" / f"{vid.stem}.m4a"
            if not backup.exists():
                backup.parent.mkdir(exist_ok=True)
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(vid), "-vn", "-c:a", "copy", str(backup)])
            tmp = rescore(vid, tpath, dur, vo)
            os.replace(tmp, vid)
            line["bytes"] = vid.stat().st_size
        log.append(line)
        print(("rescored " if a.apply else "would rescore ") + f"{reel['id']:34s} -> {track}" + (" (+VO)" if vo else ""))
    if a.apply:
        out = MEDIA / "music" / "rescore-log.json"
        prev = json.load(open(out)) if out.exists() else []
        json.dump(prev + [{"at": now.isoformat(), "reels": log}], open(out, "w"), indent=1)
    print(f"{len(log)} Reels {'re-scored' if a.apply else 'in scope (dry run)'}")


if __name__ == "__main__":
    main()

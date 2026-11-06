"""Intake for videos Muse (or any outside studio) delivers to incoming/muse/<id>/.

Each delivery folder holds: video.mp4, cover.jpg and post.json (see docs/muse-handoff.md).
This tool checks every new delivery, fixes what it safely can (re-encodes a video that is
too big or the wrong shape), copies passing ones into media/muse/<id>/ and writes the
result to incoming/muse/<id>/STATUS.md. It never schedules anything: the Social studio
reads READY deliveries, runs its clarity and rights gates, and adds them to
schedule/posts.json itself.

    python3 tools/intake_muse.py            # check every delivery without STATUS.md
    python3 tools/intake_muse.py --all      # re-check every delivery
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCOMING = ROOT / "incoming" / "muse"
MEDIA = ROOT / "media" / "muse"
MAX_BYTES = 19_500_000            # the posting robot's limit (autopost.MAX_VIDEO_BYTES)
MAX_SECONDS = 90.0
MIN_SECONDS = 3.0
ACCOUNTS = {"fullyfunded", "lockedhour", "hourback", "littlefold"}
REQUIRED = ["account", "title", "hook", "caption", "rights"]
RIGHTS_REQUIRED = ["characters", "art", "music", "voice"]


def probe(path: Path) -> dict:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(path)],
        capture_output=True, text=True, check=True).stdout
    data = json.loads(out)
    v = next((s for s in data["streams"] if s.get("codec_type") == "video"), {})
    a = next((s for s in data["streams"] if s.get("codec_type") == "audio"), None)
    return {"width": int(v.get("width", 0)), "height": int(v.get("height", 0)),
            "codec": v.get("codec_name"), "seconds": float(data["format"].get("duration", 0)),
            "bytes": path.stat().st_size, "audio": a is not None}


def reencode(src: Path, dst: Path, seconds: float) -> None:
    """1080x1920 H.264 + AAC sized to fit MAX_BYTES (pads or scales, never crops)."""
    kbps = int((MAX_BYTES * 8 * 0.92) / max(seconds, 1) / 1000) - 160
    kbps = max(800, min(kbps, 8000))
    vf = ("scale=1080:1920:force_original_aspect_ratio=decrease,"
          "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1,fps=30")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(src), "-vf", vf,
                    "-c:v", "libx264", "-preset", "medium", "-b:v", f"{kbps}k", "-maxrate", f"{kbps}k",
                    "-bufsize", f"{2 * kbps}k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                    "-movflags", "+faststart", str(dst)], check=True)


def check(folder: Path) -> tuple[str, list[str], list[str]]:
    problems, notes = [], []
    post_path, video, cover = folder / "post.json", folder / "video.mp4", folder / "cover.jpg"
    for p in (post_path, video, cover):
        if not p.exists():
            problems.append(f"missing {p.name}")
    if problems:
        return "REJECTED", problems, notes
    try:
        post = json.loads(post_path.read_text())
    except ValueError as e:
        return "REJECTED", [f"post.json is not valid JSON: {e}"], notes
    for k in REQUIRED:
        if not post.get(k):
            problems.append(f"post.json needs '{k}'")
    if post.get("account") not in ACCOUNTS:
        problems.append(f"account must be one of {sorted(ACCOUNTS)}")
    rights = post.get("rights") or {}
    for k in RIGHTS_REQUIRED:
        if not rights.get(k):
            problems.append(f"rights.{k} is required (who made it / which tool / licence)")
    if "example" in (post.get("caption", "") + post.get("hook", "")).lower():
        problems.append("never the word 'example' (brand rule)")
    if len(post.get("hook", "").split()) > 8:
        problems.append("hook is over 8 words")
    if post.get("ai_generated") and "ai" not in post.get("caption", "").lower():
        notes.append("AI-made visuals or voice: Instagram's AI label will be set when scheduling")
    info = probe(video)
    if not (MIN_SECONDS <= info["seconds"] <= MAX_SECONDS):
        problems.append(f"video is {info['seconds']:.1f} s; must be {MIN_SECONDS:g}-{MAX_SECONDS:g} s")
    if problems:
        return "REJECTED", problems, notes
    out_dir = MEDIA / folder.name
    out_dir.mkdir(parents=True, exist_ok=True)
    out_video = out_dir / "video.mp4"
    shape_ok = (info["width"], info["height"]) == (1080, 1920) and info["codec"] == "h264"
    if shape_ok and info["bytes"] <= MAX_BYTES:
        shutil.copy2(video, out_video)
    else:
        reencode(video, out_video, info["seconds"])
        notes.append(f"re-encoded from {info['width']}x{info['height']} {info['codec']} "
                     f"{info['bytes'] / 1e6:.1f} MB to 1080x1920 H.264 {out_video.stat().st_size / 1e6:.1f} MB")
    if out_video.stat().st_size > MAX_BYTES:
        return "REJECTED", [f"still over {MAX_BYTES / 1e6:g} MB after re-encode; send a shorter cut"], notes
    shutil.copy2(cover, out_dir / "cover.jpg")
    if not info["audio"]:
        notes.append("no audio track")
    notes.append(f"media/muse/{folder.name}/video.mp4 ({probe(out_video)['seconds']:.1f} s)")
    return "READY", problems, notes


def main(argv: list[str]) -> int:
    if not INCOMING.exists():
        print("no incoming/muse folder yet")
        return 0
    redo = "--all" in argv
    for folder in sorted(p for p in INCOMING.iterdir() if p.is_dir() and not p.name.startswith("_")):
        status_file = folder / "STATUS.md"
        if status_file.exists() and not redo:
            continue
        verdict, problems, notes = check(folder)
        lines = [f"# {folder.name}: {verdict}", ""]
        lines += [f"- PROBLEM: {p}" for p in problems] + [f"- {n}" for n in notes]
        if verdict == "READY":
            lines.append("- Next: the Social studio runs the clarity and rights gates, then schedules it.")
        status_file.write_text("\n".join(lines) + "\n")
        print(folder.name, verdict, "; ".join(problems or notes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

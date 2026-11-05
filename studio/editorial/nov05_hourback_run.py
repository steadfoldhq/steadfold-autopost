#!/usr/bin/env python3
"""Hourback real AI runs, Thu Nov 5 2026 (Hourback maker, Social studio).

Same ISOLATED method as studio/editorial/nov03_hourback_run.py (copied, not imported): each prompt runs ONCE, verbatim,
in a fresh Claude session via the Claude Code CLI in print mode, started in an EMPTY scratch folder, with
--setting-sources "" (no user/project settings or CLAUDE.md), --tools "", no session persistence, and the claude.ai
Project/account env vars removed (the plain `claude -p` call loaded the Project instructions and leaked the founder's
name in a Nov 3 test). The transcript is saved to studio/editorial/hb-nov05-run-<slug>.txt and quoted exactly on screen.
Every input (names, people, places, events) is made up for this post.

    python3 studio/editorial/nov05_hourback_run.py sitter chores
"""
import datetime
import os
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
SYS = "You are Claude, an AI assistant made by Anthropic."
MODEL = "claude-opus-5-5"
ISO = Path("/tmp/claude-0/nov05-hourback/empty")      # empty folder: no repo CLAUDE.md or docs nearby
STRIP = {"CLAUDE_PROJECT_UUID", "CLAUDE_PROJECT_TOOL", "CLAUDE_CODE_USER_EMAIL", "CLAUDE_CODE_ACCOUNT_UUID",
         "CLAUDE_CODE_ORGANIZATION_UUID", "CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_POST_TURN_MEMORY_SYNC",
         "CLAUDE_CODE_POST_TURN_MEMORY_CONFIG"}

RUNS = {
    "sitter": dict(
        used="hb-reel-1110-sitter-at-6 (Tue Nov 10, 7 pm)",
        prompt=("Our babysitter comes at 6 tonight and I haven't written anything down. Here's my brain dump, in no order: "
                "the kids are Maya (7) and Leo (3). Mac and cheese is in the fridge, heat it for 2 minutes. Leo goes to bed "
                "at 7:30 with his stuffed rabbit. Maya goes to bed at 8 and can read for 20 minutes first. No screens after 7. "
                "We're at a restaurant 10 minutes away and back by 10:30. Call, don't text, if anything comes up. Turn this "
                "into a short note for the fridge, sorted by time, one line each. Leave blanks for our phone numbers.")),
    "chores": dict(
        used="hb-day15-roommate-chores (Wed Nov 11, 5:45 pm, AI, for real · Day 15)",
        prompt=("I live with 3 roommates (Sam, Ana and Theo) and the kitchen is a mess because nobody knows whose turn it "
                "is. The chores: dishes every night, trash and recycling out on Tuesday night, counters and stove once a "
                "week, bathroom once a week. Theo works night shifts on weekends. Write a short, friendly text for our group "
                "chat that proposes a fair weekly rotation, so nobody feels blamed. Under 80 words.")),
}


def run(slug):
    r = RUNS[slug]
    prompt = r["prompt"]
    p = REPO / f"studio/editorial/hb-nov05-run-{slug}.txt"
    if p.exists():
        sys.exit(f"{p} exists: each prompt runs once")
    at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    env = {k: v for k, v in os.environ.items() if k not in STRIP}
    ISO.mkdir(parents=True, exist_ok=True)
    assert not any(ISO.iterdir()), "isolation folder must be empty"
    out = subprocess.run(["claude", "-p", "--model", MODEL, "--tools", "", "--no-session-persistence", "--setting-sources", "",
                          "--system-prompt", SYS, prompt], capture_output=True, text=True, timeout=300, stdin=subprocess.DEVNULL,
                         cwd=ISO, env=env)
    if out.returncode != 0 or not out.stdout.strip():
        sys.exit(f"run failed: {out.returncode} {out.stderr[:500]}")
    txt = (f"Hourback real run, Nov 5 2026 (studio maker, Hourback)\n"
           f"Used in: {r['used']}\n"
           f"Tool: Claude (Anthropic), model {MODEL}, fresh session via the Claude Code CLI in print mode (claude -p),\n"
           f"  no prior conversation, no tools (--tools \"\"), no session persistence, system prompt: \"{SYS}\"\n"
           f"  Isolated: empty working folder, --setting-sources \"\", claude.ai Project/account env vars removed (method of\n"
           f"  studio/editorial/nov03_hourback_run.py; see its ISOLATION FIX note).\n"
           f"Run at (UTC): {at}\n"
           f"Input: MADE UP FOR THIS POST (no real person, workplace or event).\n\n"
           f"===== PROMPT (verbatim) =====\n{prompt}\n\n===== REPLY (verbatim) =====\n{out.stdout.strip()}\n")
    p.write_text(txt)
    print(txt)




# ---------------------------------------------------------------- fresh stranger hook picker (no Agent tool in this
# maker session): ONE fresh isolated session that sees only a one-line page description and the 3 options per piece.
PICKER = ("Hourback is an Instagram page that shows one real, practical AI trick for everyday life, using made-up "
          "situations.\n\nPiece A (a 15-second Reel):\n1. Sitter at 6. No notes yet.\n2. Sitter's here at 6. Fridge note?\n"
          "3. Babysitter at 6. Messy brain dump?\n\nPiece C (a 2-slide carousel cover):\n1. 4 roommates. Whose turn is it?\n"
          "2. 4 roommates, 1 messy kitchen.\n3. Dishes piling up? One fair text.\n\n"
          "Which one would stop a stranger scrolling, and which is clearest? Pick one per piece, or say none works and why.")


def picker():
    p = REPO / "studio/editorial/hb-nov05-hook-picker.txt"
    if p.exists():
        sys.exit(f"{p} exists")
    env = {k: v for k, v in os.environ.items() if k not in STRIP}
    iso = ISO.parent / "empty-picker"
    iso.mkdir(parents=True, exist_ok=True)
    assert not any(iso.iterdir())
    out = subprocess.run(["claude", "-p", "--model", MODEL, "--tools", "", "--no-session-persistence", "--setting-sources", "",
                          "--system-prompt", SYS, PICKER], capture_output=True, text=True, timeout=300,
                         stdin=subprocess.DEVNULL, cwd=iso, env=env)
    at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    p.write_text(f"Hourback hook picker, Nov 5 2026, fresh isolated session ({MODEL}), {at}\n\n===== ASK =====\n{PICKER}\n\n"
                 f"===== VERDICT =====\n{out.stdout.strip()}\n")
    print(p.read_text())


if __name__ == "__main__":
    for s in sys.argv[1:]:
        picker() if s == "picker" else run(s)

#!/usr/bin/env python3
"""Hourback real AI runs, Wed Nov 4 2026 (Hourback maker, Social studio).

Same ISOLATED method as studio/editorial/nov03_hourback_run.py (copied, not imported): each prompt runs ONCE, verbatim,
in a fresh Claude session via the Claude Code CLI in print mode, started in an EMPTY scratch folder, with
--setting-sources "" (no user/project settings or CLAUDE.md), --tools "", no session persistence, and the claude.ai
Project/account env vars removed (the plain `claude -p` call loaded the Project instructions and leaked the founder's
name in a Nov 3 test). The transcript is saved to studio/editorial/hb-nov04-run-<slug>.txt and quoted exactly on screen.
Every input (names, people, places, events) is made up for this post.

    python3 studio/editorial/nov04_hourback_run.py nonna retire missed
"""
import datetime
import os
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
SYS = "You are Claude, an AI assistant made by Anthropic."
MODEL = "claude-opus-5-5"
ISO = Path("/tmp/claude-0/nov04-hourback/empty")      # empty folder: no repo CLAUDE.md or docs nearby
STRIP = {"CLAUDE_PROJECT_UUID", "CLAUDE_PROJECT_TOOL", "CLAUDE_CODE_USER_EMAIL", "CLAUDE_CODE_ACCOUNT_UUID",
         "CLAUDE_CODE_ORGANIZATION_UUID", "CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_POST_TURN_MEMORY_SYNC",
         "CLAUDE_CODE_POST_TURN_MEMORY_CONFIG"}

RUNS = {
    "nonna": dict(
        used="hb-reel-1108-nonna-90 (Sun Nov 8, 7 pm)",
        prompt=("My grandmother turns 90 tomorrow. She grew up in Italy and still reads Italian best, but my Italian is "
                "very basic. Write a short birthday message for her card in Italian: 3 sentences, warm and simple, and "
                "mention that she taught me to make gnocchi on Sundays. Put the English meaning under each Italian "
                "sentence. Sign it from Marco.")),
    "retire": dict(
        used="hb-reel-1109-retirement-speech (Mon Nov 9, 7 pm)",
        prompt=("My coworker Linda is retiring after 31 years at the front desk of our town library, and I'm giving a "
                "2-minute speech at her send-off tomorrow at 3 pm. Three true things about her: she knew every regular's "
                "name, she ran Saturday story time for 20 years, and she kept a jar of lemon candies at the desk for "
                "anyone having a rough day. Write a warm 2-minute speech (about 250 words) with one light joke, and end "
                "with a line everyone can raise a glass to. Use short sentences I can read out loud.")),
    "missed": dict(
        used="hb-day14-missed-30th (Mon Nov 9, 5:45 pm, AI, for real · Day 14)",
        prompt=("I missed my friend Jordan's 30th birthday dinner on Saturday. I had a migraine, fell asleep, and didn't "
                "text until Sunday morning. Write a short apology text I can send tonight: own it, no long excuses, and "
                "say I'd like to take Jordan out for dinner this week. Under 60 words.")),
}


def run(slug):
    r = RUNS[slug]
    prompt = r["prompt"]
    p = REPO / f"studio/editorial/hb-nov04-run-{slug}.txt"
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
    txt = (f"Hourback real run, Nov 4 2026 (studio maker, Hourback)\n"
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


if __name__ == "__main__":
    for s in sys.argv[1:]:
        run(s)

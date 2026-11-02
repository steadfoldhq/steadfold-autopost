#!/usr/bin/env python3
"""Hourback real AI runs, Mon Nov 2 2026 (Hourback maker, Social studio).

Each prompt runs ONCE, verbatim, in a fresh Claude session (Claude Code CLI print mode = a fresh agent with no tools,
no session persistence, no prior conversation). The transcript is saved to studio/editorial/hb-nov02-run-<slug>.txt and
quoted exactly on screen. Every input is made up for this post.

    python3 studio/editorial/nov02_hourback_run.py interview packing
"""
import datetime
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
SYS = "You are Claude, an AI assistant made by Anthropic."
MODEL = "claude-opus-5-5"

RUNS = {
    "interview": dict(
        used="hb-reel-1104-interview-9am (Wed Nov 4, 7 pm)",
        prompt=("My job interview is tomorrow at 9 am and I haven't prepared at all. Here's the job posting:\n\n"
                "\"Shift Supervisor, neighbourhood bakery café. Open the store at 6 am two days a week, lead a team of 4, "
                "handle customer complaints, count the cash drawer at close, and train new staff. 1+ year in food service. "
                "Weekend availability.\"\n\n"
                "Based on this posting, what are the 5 questions they're most likely to ask me? Keep each one short, and "
                "add one line on what they're really checking.")),
    "packing": dict(
        used="hb-reel-1105-flight-6am (Thu Nov 5, 7 pm)",
        prompt=("My flight is at 6 am tomorrow and I haven't packed. 3 nights in Vancouver, carry-on only. There's a "
                "wedding on Saturday (I'm wearing a suit), one day hike, and it'll probably rain. Make me a packing list "
                "sorted by room in my apartment (bedroom, bathroom, kitchen, front door) so I only walk through once. "
                "Keep it short.")),
}


def run(slug):
    r = RUNS[slug]
    prompt = r["prompt"]
    at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = subprocess.run(["claude", "-p", "--model", MODEL, "--tools", "", "--no-session-persistence", "--system-prompt", SYS,
                          prompt], capture_output=True, text=True, timeout=300, stdin=subprocess.DEVNULL)
    if out.returncode != 0 or not out.stdout.strip():
        sys.exit(f"run failed: {out.returncode} {out.stderr[:500]}")
    txt = (f"Hourback real run, Nov 2 2026 (studio maker, Hourback)\n"
           f"Used in: {r['used']}\n"
           f"Tool: Claude (Anthropic), model {MODEL}, fresh session via the Claude Code CLI in print mode (claude -p),\n"
           f"  no prior conversation, no tools (--tools \"\"), no session persistence, system prompt: \"{SYS}\"\n"
           f"Run at (UTC): {at}\n"
           f"Input: MADE UP FOR THIS POST (no real person, workplace or event).\n\n"
           f"===== PROMPT (verbatim) =====\n{prompt}\n\n===== REPLY (verbatim) =====\n{out.stdout.strip()}\n")
    p = REPO / f"studio/editorial/hb-nov02-run-{slug}.txt"
    p.write_text(txt)
    print(txt)


if __name__ == "__main__":
    for s in sys.argv[1:]:
        run(s)

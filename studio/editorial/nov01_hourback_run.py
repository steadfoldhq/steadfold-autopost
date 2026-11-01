#!/usr/bin/env python3
"""Hourback real AI runs, Sun Nov 1 2026 (Hourback maker, Social studio).

Each prompt runs ONCE, verbatim, in a fresh Claude session (Claude Code CLI print mode, no tools, no session persistence,
no prior conversation). The transcript is saved to studio/editorial/hb-nov01-run-<slug>.txt and quoted exactly on screen.
Every input is made up for this post.

    python3 studio/editorial/nov01_hourback_run.py toast tidy potluck
    python3 studio/editorial/nov01_hourback_run.py cue        # needs hb-nov01-run-toast.txt (pastes its reply verbatim)
"""
import datetime
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
SYS = "You are Claude, an AI assistant made by Anthropic."
MODEL = "claude-opus-5-5"


def toast_reply():
    t = (REPO / "studio/editorial/hb-nov01-run-toast.txt").read_text()
    return t.split("===== REPLY (verbatim) =====\n", 1)[1].strip()


RUNS = {
    "toast": dict(
        used="hb-reel-1101-wedding-toast (Sun Nov 1, 7 pm)",
        prompt=lambda: ("I'm giving a toast at my best friend's wedding tonight and I haven't written anything. Her name is Maya, "
                        "his name is Theo. Three things: we met in a college dorm when she set off the fire alarm making toast, "
                        "she drove six hours to help me move, and Theo is the only person who can beat her at Scrabble. "
                        "Write me a toast I can say in about one minute. Warm, a little funny.")),
    "cue": dict(
        used="hb-reel-1102-toast-cue-card (Mon Nov 2, 7 pm), Part 2 of hb-reel-1101-wedding-toast",
        prompt=lambda: ("I have to give this toast tonight and I can't memorize it. Turn it into a cue card: 5 short prompts, "
                        "a few words each, that I can glance at to remember each part. Here's the toast:\n\n" + toast_reply())),
    "tidy": dict(
        used="hb-reel-1103-guests-30-min (Tue Nov 3, 7 pm)",
        prompt=lambda: ("Guests arrive in 30 minutes and my apartment is a mess: dishes in the sink, laundry on the couch, "
                        "shoes and bags by the door, mail all over the table, and the bathroom hasn't been cleaned. "
                        "Give me a 30-minute plan, starting with what guests will see first. Keep it short.")),
    "potluck": dict(
        used="hb-day12-potluck (Wed Nov 4, 5:45 pm)",
        prompt=lambda: ("I'm bringing a dish to a potluck tomorrow. One guest is vegan, one can't eat nuts, and one is "
                        "gluten-free. I have about 30 minutes to cook and $20. Give me 3 dishes that work for all of them, "
                        "one line each.")),
}


def run(slug):
    r = RUNS[slug]
    prompt = r["prompt"]()
    at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = subprocess.run(["claude", "-p", "--model", MODEL, "--tools", "", "--no-session-persistence", "--system-prompt", SYS,
                          prompt], capture_output=True, text=True, timeout=300, stdin=subprocess.DEVNULL)
    if out.returncode != 0 or not out.stdout.strip():
        sys.exit(f"run failed: {out.returncode} {out.stderr[:500]}")
    txt = (f"Hourback real run, Nov 1 2026 (studio maker, Hourback)\n"
           f"Used in: {r['used']}\n"
           f"Tool: Claude (Anthropic), model {MODEL}, fresh session via the Claude Code CLI in print mode (claude -p),\n"
           f"  no prior conversation, no tools (--tools \"\"), no session persistence, system prompt: \"{SYS}\"\n"
           f"Run at (UTC): {at}\n"
           f"Input: MADE UP FOR THIS POST (no real person, workplace or event).\n\n"
           f"===== PROMPT (verbatim) =====\n{prompt}\n\n===== REPLY (verbatim) =====\n{out.stdout.strip()}\n")
    p = REPO / f"studio/editorial/hb-nov01-run-{slug}.txt"
    p.write_text(txt)
    print(txt)


if __name__ == "__main__":
    for s in sys.argv[1:]:
        run(s)

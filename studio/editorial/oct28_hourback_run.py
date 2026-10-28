#!/usr/bin/env python3
"""Hourback real AI runs, Wed Oct 28 2026 (Hourback maker, Social studio).

Each prompt runs ONCE, verbatim, in a fresh Claude session (Claude Code CLI print mode, no tools, no session persistence,
no prior conversation). The transcript is saved to studio/editorial/hb-oct28-run-<slug>.txt and quoted exactly on screen.
Every input is made up for this post.

    python3 studio/editorial/oct28_hourback_run.py card|costume|gift
"""
import datetime
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
SYS = "You are Claude, an AI assistant made by Anthropic."
MODEL = "claude-opus-5-5"

RUNS = {
    "card": dict(
        used="hb-reel-1029am-coworker-card (Thu Oct 29, 8:45 am)",
        prompt=("I have to sign a birthday card for a coworker I barely know. Her name is Dana and she works in accounting. "
                "Give me 3 short, warm lines I could write. Nothing cheesy.")),
    "costume": dict(
        used="hb-reel-1031-closet-costume (Sat Oct 31, 7 pm)",
        prompt=("Halloween party in an hour and I have no costume. Here's what I own: a white bedsheet, a black turtleneck, "
                "black jeans, a denim jacket, a red bandana, sunglasses, a striped T-shirt, a beanie, some cardboard and a black marker. "
                "Give me 3 costume ideas I can make from just these things, and what to wear for each. Keep it short.")),
    "gift": dict(
        used="hb-day11-gift-for-dad (Mon Nov 2, 5:45 pm)",
        prompt=("Help me pick a gift for my dad. He's 64, loves gardening and crossword puzzles, drinks his coffee black, "
                "and says he doesn't need anything. My budget is $40. Give me 5 ideas, one line each.")),
}


def run(slug):
    r = RUNS[slug]
    at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = subprocess.run(["claude", "-p", "--model", MODEL, "--tools", "", "--no-session-persistence", "--system-prompt", SYS,
                          r["prompt"]], capture_output=True, text=True, timeout=300, stdin=subprocess.DEVNULL)
    if out.returncode != 0 or not out.stdout.strip():
        sys.exit(f"run failed: {out.returncode} {out.stderr[:500]}")
    txt = (f"Hourback real run, Oct 28 2026 (studio maker, Hourback)\n"
           f"Used in: {r['used']}\n"
           f"Tool: Claude (Anthropic), model {MODEL}, fresh session via the Claude Code CLI in print mode (claude -p),\n"
           f"  no prior conversation, no tools (--tools \"\"), no session persistence, system prompt: \"{SYS}\"\n"
           f"Run at (UTC): {at}\n"
           f"Input: MADE UP FOR THIS POST (no real person, workplace or event).\n\n"
           f"===== PROMPT (verbatim) =====\n{r['prompt']}\n\n===== REPLY (verbatim) =====\n{out.stdout.strip()}\n")
    p = REPO / f"studio/editorial/hb-oct28-run-{slug}.txt"
    p.write_text(txt)
    print(txt)


if __name__ == "__main__":
    for s in sys.argv[1:]:
        run(s)

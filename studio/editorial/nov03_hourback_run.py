#!/usr/bin/env python3
"""Hourback real AI runs, Tue Nov 3 2026 (Hourback maker, Social studio).

Same method as nov02_hourback_run.py: each prompt runs ONCE, verbatim, in a fresh Claude session (Claude Code CLI print
mode = a fresh agent with no tools, no session persistence, no prior conversation). The transcript is saved to
studio/editorial/hb-nov03-run-<slug>.txt and quoted exactly on screen. Every input is made up for this post.

ISOLATION FIX (Nov 3): a test showed the plain `claude -p` call (as used Oct 24-Nov 2) also carries this account's attached
claude.ai Project instructions (the founder's name and job) into the "fresh" session; the first Nov 3 landlord run signed
the email with the founder's real name. So runs now start in an empty scratch folder with the Project/account env vars
removed and --setting-sources "" (no user/project settings or CLAUDE.md). A test of this mode still reported the account
email (attached by the CLI itself), but no name or Project text. The 3 first-pass transcripts were moved out of the repo
(not used for anything, not judged on quality); every prompt below then ran once in the isolated mode.

    python3 studio/editorial/nov03_hourback_run.py thanks dinners landlord
"""
import datetime
import os
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
SYS = "You are Claude, an AI assistant made by Anthropic."
MODEL = "claude-opus-5-5"
ISO = Path("/tmp/claude-0/nov03-hourback/empty")      # empty folder: no repo CLAUDE.md or docs nearby
STRIP = {"CLAUDE_PROJECT_UUID", "CLAUDE_PROJECT_TOOL", "CLAUDE_CODE_USER_EMAIL", "CLAUDE_CODE_ACCOUNT_UUID",
         "CLAUDE_CODE_ORGANIZATION_UUID", "CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_POST_TURN_MEMORY_SYNC",
         "CLAUDE_CODE_POST_TURN_MEMORY_CONFIG"}

RUNS = {
    "thanks": dict(
        used="hb-reel-1106-thank-you-20 (Fri Nov 6, 7 pm)",
        prompt=("My baby shower was on Saturday and I have 20 thank-you notes to write today. Here's who gave what:\n\n"
                "1. Aunt Rosa: a handmade quilt\n2. Priya: a baby carrier\n3. Grandpa Joe: a rocking chair he fixed up\n"
                "4. Mei: a stack of board books\n5. Daniel and Sam: a stroller\n6. Coworkers at the clinic: a diaper bag\n"
                "7. Lena: 3 frozen dinners for the first week\n8. Uncle Marco: a $50 gift card\n9. Fatima: a white noise machine\n"
                "10. Chris: a bath tub and towels\n11. Neighbour Ruth: a knitted hat\n12. Tom: a baby monitor\n"
                "13. Jess: a box of onesies\n14. Cousin Ana: a play mat\n15. Mr. and Mrs. Okafor: a savings bond\n"
                "16. Bea: a night light shaped like a moon\n17. Leo: a diaper caddy\n18. Grandma June: her own baby photo album\n"
                "19. Karin: a sling\n20. My book club: a basket of snacks for late nights\n\n"
                "Write a 2-sentence note for each one. Name the gift and say one specific way we'll use it. "
                "Don't make them all sound the same.")),
    "dinners": dict(
        used="hb-reel-1107-5-dinners (Sat Nov 7, 7 pm)",
        prompt=("The grocery store closes at 9 and I need to shop for the week. Plan 5 weeknight dinners for 2 adults, "
                "each under 30 minutes, that share ingredients so nothing goes to waste. Budget about $80. "
                "Give me the 5 dinners (one line each), then one shopping list, then tell me which ingredients get "
                "used more than once. Keep it short.")),
    "landlord": dict(
        used="hb-day13-landlord-email (Fri Nov 6, 5:45 pm, AI, for real · Day 13)",
        prompt=("The heat in my apartment has been off since Monday, 3 days now, and it's 16°C inside. I texted my "
                "landlord, Dan, on Monday and he said he'd look at it, but nothing has happened. Write me a short email "
                "to send him before 5 pm today. Polite but firm: what's wrong, since when, what I've already done, and "
                "what I'm asking for and by when. Sign it from Alex in unit 4B. Under 120 words.")),
    # Gate fix (Nov 3, coordinator CD note): the first landlord email carried the run day's dates (Monday text,
    # "tomorrow, Wednesday, November 4") on a Friday Nov 6 post. Dates now fit the post. Runs once, isolated.
    "landlord2": dict(
        used="hb-day13-landlord-email (Fri Nov 6, 5:45 pm, AI, for real · Day 13), replaces hb-nov03-run-landlord.txt",
        prompt=("Today is Friday, November 6. The heat in my apartment has been off since Wednesday, November 4, and it's "
                "16°C inside. I texted my landlord, Dan, on Wednesday and he said he'd look at it, but nothing has happened. "
                "Write me a short email to send him before 5 pm today. Polite but firm: what's wrong, since when, what I've "
                "already done, and that I need the heat repaired by Saturday, November 7. Sign it from Alex in unit 4B. "
                "Under 120 words.")),
}


def run(slug):
    r = RUNS[slug]
    prompt = r["prompt"]
    at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    env = {k: v for k, v in os.environ.items() if k not in STRIP}
    ISO.mkdir(parents=True, exist_ok=True)
    out = subprocess.run(["claude", "-p", "--model", MODEL, "--tools", "", "--no-session-persistence", "--setting-sources", "",
                          "--system-prompt", SYS, prompt], capture_output=True, text=True, timeout=300, stdin=subprocess.DEVNULL,
                         cwd=ISO, env=env)
    if out.returncode != 0 or not out.stdout.strip():
        sys.exit(f"run failed: {out.returncode} {out.stderr[:500]}")
    txt = (f"Hourback real run, Nov 3 2026 (studio maker, Hourback)\n"
           f"Used in: {r['used']}\n"
           f"Tool: Claude (Anthropic), model {MODEL}, fresh session via the Claude Code CLI in print mode (claude -p),\n"
           f"  no prior conversation, no tools (--tools \"\"), no session persistence, system prompt: \"{SYS}\"\n"
           f"  Isolated: empty working folder, --setting-sources \"\", claude.ai Project/account env vars removed (see the\n"
           f"  ISOLATION FIX note in studio/editorial/nov03_hourback_run.py; an earlier non-isolated run was discarded unused).\n"
           f"Run at (UTC): {at}\n"
           f"Input: MADE UP FOR THIS POST (no real person, workplace or event).\n\n"
           f"===== PROMPT (verbatim) =====\n{prompt}\n\n===== REPLY (verbatim) =====\n{out.stdout.strip()}\n")
    p = REPO / f"studio/editorial/hb-nov03-run-{slug}.txt"
    if p.exists():
        sys.exit(f"{p} exists: each prompt runs once")
    p.write_text(txt)
    print(txt)


if __name__ == "__main__":
    for s in sys.argv[1:]:
        run(s)

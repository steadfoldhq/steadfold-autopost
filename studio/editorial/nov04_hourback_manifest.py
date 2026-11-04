#!/usr/bin/env python3
"""Writes studio/editorial/nov04/hourback.json (Hourback maker, Wed Nov 4 2026). Entries are added as each piece is clean.

    python3 studio/editorial/nov04_hourback_manifest.py
"""
import json
import re
import subprocess
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
OUT = REPO / "studio/editorial/nov04/hourback.json"
FOLLOW = "Follow to learn one real AI trick a day."
PICKER = ("Fresh stranger picker (Nov 4): no Agent tool in this maker session, so the pick ran as ONE fresh, isolated Claude "
          "session (claude -p, empty folder, no tools/settings/Project) that saw only a one-line page description and the 3 "
          "options per piece; verdict saved at studio/editorial/hb-nov04-hook-picker.txt. ")


def dur(rel):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(REPO / "media" / rel)],
                         capture_output=True, text=True, check=True).stdout
    return round(float(out), 2)


def reply(slug, day="nov04"):
    t = (REPO / f"studio/editorial/hb-{day}-run-{slug}.txt").read_text()
    return t.split("===== PROMPT (verbatim) =====\n", 1)[1].split("\n\n===== REPLY (verbatim) =====\n")


def run_at(slug, day="nov04"):
    t = (REPO / f"studio/editorial/hb-{day}-run-{slug}.txt").read_text()
    return re.search(r"Run at \(UTC\): (\S+)", t).group(1)


ENTRIES = []

# ------------------------------------------------------------------ D2: send test + note 1 in frame 0 (replaces Nov 3 file)
old = next(e for e in json.loads((REPO / "studio/editorial/nov03/hourback.json").read_text()) if e["id"] == "hb-reel-1106-thank-you-20")
d2 = dict(old)
rosa = "Your handmade quilt is already folded over the back of the nursery chair, and I keep running my hand over the stitching. We'll spread it on the floor for tummy time so the baby is surrounded by something you made."
assert rosa in reply("thanks", "nov03")[1].replace("\n", " ")
SEND_D2 = "Send this to whoever just had a baby shower."
d2.update(
    caption=old["caption"].replace("Send this to whoever has a stack of cards to write.", SEND_D2),
    beats=[
        "[0.0 s] Baby shower's over. 20 notes left. | (chip, top) Real Claude reply · names and gifts made up for this post | (stack tag) 20 to write | (card) Thank you | (tray) OUT · mail today | (note card) Note 1 of 20, word for word · Aunt Rosa · " + rosa + " | (stamp) HOURBACK · YOUR EVENINGS BACK",
        "[2.0 s] try this | Paste who gave what. AI drafts all 20. | (sticky, 2.0-4.3 s, 52 px) gift list we made up for this post: · 1. Aunt Rosa: a handmade quilt · 2. Priya: a baby carrier · 3. Grandpa Joe: a rocking chair he fixed up · … 20 in all | (from 4.3 s) Claude's real notes, shortened:",
        "[4.3 s] Note 2 of 20 · Priya · Thank you for the baby carrier! I'm planning to wear the baby on our morning walks around the block… → [5.5-6.9 s, ~0.08 s each] Note 3…20 of 20 with each note's real first sentence + … ; stack tag counts 19 → 0 to write",
        "[7.5 s] every note is different | It names each gift and how you'll use it. | (note card) Note 3, word for word · Grandpa Joe · I can't believe how beautiful the rocking chair turned out after all your work on it. It's going right next to the crib, and every 3 a.m. feeding will happen in it.",
        "[10.7 s] Do this: | Paste names and gifts. Ask for notes. | In ChatGPT, Claude or Gemini. Edit before you send.",
        "[12.3 s to end, 2.3 s] (note card flips, yellow) Send this to whoever just had a baby shower. | Follow to learn one real AI trick a day.",
    ],
    duration_s=dur(old["video"]),
    send_test=True,
    replaces_existing=True,
    alt_text=old["alt_text"].replace(
        "and an empty note card that says 'Note 0 of 20' and 'Dear…'.",
        "and a note card already showing Claude's real note 1, word for word: 'Aunt Rosa. " + rosa + "'").replace(
        " Note 1 of 20, Aunt Rosa: 'Your handmade quilt is already folded over the back of the nursery chair, and I keep running my hand over the stitching. …'", "").replace(
        "Ends: 'Follow to learn one real AI trick a day.'",
        "Then the note card flips over to a yellow card: 'Send this to whoever just had a baby shower.' with 'Follow to learn one real AI trick a day.' above it."),
    notes=("D2 re-edit (Nov 4, Performance desk orders 1 + 4): SEND TEST Reel for HB (grade on the Sat read: >=1 send per 100 reach) "
           "and real output in frame 0. Overwrites media/studio-nov03/hourback/hb-reel-1106-thank-you-20.mp4 in place (same id, "
           "same slot Fri Nov 6 19:00, cover jpg unchanged). Changes vs the Nov 3 cut: (1) frame 0 note card shows Claude's real "
           "note 1 (Aunt Rosa) in full, word for word, under the hook (was an empty 'Note 0 of 20 / Dear…' card); (2) beat 1 cut "
           "6.0 -> 4.7 s (note 1 no longer re-lands; Priya at 3.25 s, riffle 4.55-5.95 s); (3) last 2.3 s: the note card flips to "
           "ONE send line 'Send this to whoever just had a baby shower.' (Caveat Brush 84 px) together with the follow pill "
           "(both from 12.3 s after the gate fix, paper-slap SFX on the flip); caption send line changed to the same words. Everything else is the "
           "Nov 3 cut: hook, payoff at 2.0 s, Do this, music hb-x-future-easy at -13.8 LUFS. 14.6 s after the gate fix. Builder: "
           "studio/editorial/nov04_hourback.py thanks. Self-review (QG-1): strip + frames 0 / 13.9 checked; note 1 fits the card "
           "(5 lines, 44 px); send text inside the card at 1080 wide. Doubt: frame 0 shows 'Note 1 of 20' while the stack tag "
           "still says '20 to write' (drafted vs written); read as fine. Not yet seen by an independent reviewer (QG-5). CD GATE FIXES (Nov 4, coordinator; template fix): the made-up gift-list sticky now holds 2.0 s (2.0-4.0 s, then flies in by 4.3 s) at 52 px (title 50 px), sits above the note card (no overlap), and the 'Claude's real notes, shortened:' subtitle is hidden while it shows; the 'Real Claude reply' chip moved from y 1572 (~82%) to the top band (y 228, ~12%, right of the stamp). Timing now: Priya 4.3 s, riffle 5.5-6.9 s, Grandpa Joe 7.5 s, Do this 10.7 s, send flip + follow 12.3 s (2.3 s on screen). 14.6 s. Strip re-checked."),
)
ENTRIES.append(d2)

# ------------------------------------------------------------------ A: Nonna turns 90 tomorrow, in Italian
pa, ra = reply("nonna")
IT = re.findall(r"^\*\*(.+?)\*\*$", ra, re.M)
EN = re.findall(r"^\*([^*].*?)\*$", ra, re.M)
NOTE1 = 'This uses the informal "tu" form, which is natural for a grandmother.'
NOTE = ra.strip().split("\n\n")[-1]
assert NOTE.startswith(NOTE1)
CARD = " ".join(IT[:3]) + " " + IT[3] + " " + IT[4]
A = dict(
    id="hb-reel-1108-nonna-90", account="hourback", publish_at="2026-11-08T19:00:00-05:00",
    video="studio-nov04/hourback/hb-reel-1108-nonna-90.mp4", cover="studio-nov04/hourback/hb-reel-1108-nonna-90-cover.jpg",
    caption=("Nonna turns 90 tomorrow and you want to write her card in Italian? Ask AI for the message in her language, "
             "with the English under each line.\n\n"
             "WHY IT WORKS: you know what you want to say; AI handles the grammar. Asking for the English under each line lets "
             "you check that every sentence says what you meant before you copy it into the card. Giving it one true memory "
             "(gnocchi on Sundays) turns a translation into a message that sounds like you.\n\n"
             f"THE REAL TEST: we made up a grandmother and a memory and asked Claude (Anthropic) on Nov 4, 2026: \"{pa.strip()}\"\n"
             f"Its card, word for word: \"{CARD}\"\n"
             f"It added a note: \"{NOTE1}\"\n\n"
             "HOW (5 minutes):\n1. Open ChatGPT, Claude or Gemini.\n2. Say who it's for, which language she reads best, and one "
             "true memory.\n3. Ask for 3 short sentences in her language, with the English meaning under each one.\n4. Read the "
             "English, change anything that isn't true, then copy her language into the card by hand, accents and all.\n\n"
             "THE CATCH: AI can be correct and still miss how your family talks: a dialect word, a nickname, the way she signs "
             "off. If you can, ask someone who speaks the language to read it before it goes in the card.\n\n"
             "PRIVACY TIP: a first name and one memory are enough. Leave out her full name, address and anything about her health.\n\n"
             "Names made up for this post.\n\n"
             "Do this: Ask for her language, English underneath.\n\n"
             "Send this to whoever has a grandparent's birthday coming up.\n\n"
             f"{FOLLOW}\n\n#ai #learnai #claude #birthdaycard #grandma"),
    first_comment=(f"How we made this: one real run in Claude (Anthropic), model claude-opus-5-5, in a fresh, isolated session "
                   f"(Claude Code CLI print mode in an empty folder, no tools, no earlier chat, no Project or settings context "
                   f"loaded), {run_at('nonna')[:10]} {run_at('nonna')[11:16]} UTC. Nonna, the memory and Marco are made up for "
                   "this post. On screen: the whole card word for word (3 Italian sentences + sign-off), each sentence's English "
                   "line word for word, and its note on 'tu' and 'Ti voglio bene' word for word. Full prompt and reply in our "
                   "public repo steadfold-autopost: studio/editorial/hb-nov04-run-nonna.txt. Results vary between apps and runs. "
                   "Fact check (Nov 4 2026): the only claims are the run itself, checked against the saved transcript; no outside "
                   "statistic or feature claim is made."),
    alt_text=("Illustrated Hourback Reel in periwinkle and cream: a kitchen table with a cake topped by '9' and '0' candles, a "
              "floured board of gnocchi with a fork labelled 'Sundays', and an open card. Words: 'Nonna turns 90 tomorrow. In "
              "Italian?' The card already shows Claude's real message, headed 'Claude's card for Nonna, in Italian': '"
              + CARD + "'. Then 'try this. Ask AI to write it in her language. With the English under each line:' A yellow note, "
              "'what we told it (made up for this post): Grandma turns 90 tomorrow, she reads Italian best, my Italian is basic, "
              "she taught me to make gnocchi on Sundays', flies into the card. Line by line, each Italian sentence appears with "
              f"its English: '{EN[0]}', '{EN[1]}', '{EN[2]}'. Then 'it explains its choices. It picks the words you'd use with "
              f"family.' with its note, word for word: '{NOTE}' Then 'Do this: Ask for her language, English underneath. In "
              "ChatGPT, Claude or Gemini. Then ask someone who speaks it.' The candles flare, the card lines highlight and get a "
              "tick. Ends: 'Follow to learn one real AI trick a day.' Names made up for this post."),
    beats=[
        "[0.0 s] Nonna turns 90 tomorrow. In Italian? | (chip, top) Real Claude reply · Nonna and Marco made up for this post | (cake candles) 9 0 | (board) Sundays | (card header) Claude's card for Nonna, in Italian | (card, word for word) " + " · ".join(IT[:3]) + " · " + IT[3] + " " + IT[4] + " | (stamp) HOURBACK · YOUR EVENINGS BACK",
        "[2.0 s] try this | Ask AI to write it in her language. | (from 4.3 s) With the English under each line: | (sticky, 2.0-4.3 s, 52 px) what we told it (made up for this post): · Grandma turns 90 tomorrow · she reads Italian best, my Italian is basic · she taught me to make gnocchi on Sundays",
        f"[4.3 s] Line 1 of 3, with its English · {IT[0]} · {EN[0]} → [5.4 s] Line 2 of 3, with its English · {IT[1]} · {EN[1]} → [6.5 s] Line 3 of 3, with its English · {IT[2]} · {EN[2]}",
        f"[7.6 s] it explains its choices | It picks the words you'd use with family. | (card) Its note, word for word · {NOTE}",
        "[10.6 s] Do this: | Ask for her language, English underneath. | In ChatGPT, Claude or Gemini. Then ask someone who speaks it. | (card) the full Italian card again, highlighted, tick",
        "[11.8 s to end, 2.7 s] Follow to learn one real AI trick a day.",
    ],
    hook_options=["Nonna turns 90 tomorrow. In Italian?", "Her 90th card. In her language.", "Card for Grandma's 90th, in Italian?"],
    hook_picker=PICKER + "Verdict A: #1 'Nonna turns 90 tomorrow. In Italian?' (person, milestone, deadline and problem in six words; #2 vague, #3 flat). Adopted.",
    duration_s=dur("studio-nov04/hourback/hb-reel-1108-nonna-90.mp4"),
    style=("Body: drawn occasion scene (desk order 4: deadline + number + the REAL output in frame 0), new composition: kitchen "
           "table, a cake with 9-0 candles, a gnocchi board ('Sundays'), and Nonna's card already filled with Claude's Italian "
           "at 0.00 s. Dedicated cover: 'Instead of… Write…' reframe (style 7, QUIET) with Claude's real first line. Grid: after "
           "Sat 7 pm dinners (follow the line, loud), before Mon 5:45 pm Day 14 (Look B, loud)."),
    send_test=False,
    sources=[f"studio/editorial/hb-nov04-run-nonna.txt (fresh, isolated verbatim Claude run via claude -p, {run_at('nonna')})"],
    notes=("Standalone, no Part 2, no callback, no on-screen send line (not a send-test Reel). No trial flag. Desk grade: >=5 s and "
           ">=30% on >=40. Number on frame 0 ('90', hook + candles) and caption line 1. Real output visible from 0.00 s (whole "
           "card, word for word, 44 px Caveat). Payoff words at 2.0 s; English line 1 at 4.3 s. Follow pill on screen 2.7 s. "
           "Music hb-x-smart-bounce (existing HB track, tools/music-library.json), -13.5 LUFS; SFX paper slap + sticker pops. "
           "1080x1920 30 fps H.264 + AAC, 2.0 MB, 14.5 s. Builder: studio/editorial/nov04_hourback.py nonna (scenes in "
           "nov04_hourback_ab.py; cover nov04_hourback_covers.py; run nov04_hourback_run.py nonna). Transcript scanned: no real "
           "personal name or employer (Marco, Nonna are ours). Italian read by the maker: grammatical and matches the English "
           "lines; NOT checked by a native speaker (the caption's CATCH says to ask one). Topic check: Oct 28 'Menu in another "
           "language?' (Google Translate camera) is a different job (reading vs writing); no birthday/language piece in 14 days. "
           "Self-review (QG-1) fixes: hook shrank on one long line (re-split 'Nonna turns 90 / tomorrow. In Italian?'); English "
           "of line 2 ran off the card (Italian 44 px, English 34 px, rewrapped); its note ran past the card edge (40 px, "
           "rewrapped); 'Sundays' sat on the fork; the follow pill covered the candle flames (cake scaled to 0.74 and lowered). "
           "Not yet seen by an independent reviewer (QG-5). CD GATE FIXES (Nov 4, coordinator): made-up-ask sticky held 2.0 s at 52 px, above the card, subtitle hidden while it shows; chip moved from ~84% to the top band (y 228); the 3 line cards now set the Italian (Caveat 52-72 px) and its English (Inter 600, 38-56 px) both in ink, sized per line to fill the card. Beat 2 3.4 -> 3.0 s, Do this 4.0 -> 3.9 s to stay <= 15. Strip re-checked."),
)
ENTRIES.append(A)

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("m2", REPO / "studio/editorial/nov04_hourback_manifest_bc.py")
    m2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m2)
    ENTRIES += m2.entries(dict(dur=dur, reply=reply, run_at=run_at, PICKER=PICKER, FOLLOW=FOLLOW))
except FileNotFoundError:
    pass

BANNED = re.compile(r"example|e\.g\.|for illustration|hypothetical", re.I)
for e in ENTRIES:
    s = json.dumps(e, ensure_ascii=False)
    assert not BANNED.search(s), (e["id"], BANNED.search(s).group(0))
    assert "Dharma" not in s and "Scotiabank" not in s
OUT.write_text(json.dumps(ENTRIES, indent=1, ensure_ascii=False) + "\n")
print(OUT, [e["id"] for e in ENTRIES])

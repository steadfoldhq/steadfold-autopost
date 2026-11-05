#!/usr/bin/env python3
"""Writes studio/editorial/nov05/hourback.json (Hourback maker, Thu Nov 5 2026). Quotes are pulled from the saved
real-run transcripts and asserted, so the manifest can't drift from what Claude actually wrote.

    python3 studio/editorial/nov05_hourback_manifest.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
ED = REPO / "studio/editorial"
sys.path.insert(0, str(ED))
sys.dont_write_bytecode = True


def run(slug):
    t = (ED / f"hb-nov05-run-{slug}.txt").read_text()
    at = re.search(r"Run at \(UTC\): (\S+)", t).group(1)
    prompt = t.split("===== PROMPT (verbatim) =====\n", 1)[1].split("\n\n===== REPLY", 1)[0].strip()
    reply = t.split("===== REPLY (verbatim) =====\n", 1)[1].strip()
    return at, prompt, reply


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout)


METHOD = ("in a fresh, isolated session (Claude Code CLI print mode in an empty folder, no tools, no earlier chat, "
          "no Project or settings context loaded)")
PICKER = ("Fresh stranger picker (Nov 5): no Agent tool in this maker session, so the pick ran as ONE fresh, isolated Claude "
          "session (claude -p, empty folder, no tools/settings/Project) that saw only a one-line page description and the 3 "
          "options per piece; verdict saved at studio/editorial/hb-nov05-hook-picker.txt. ")

# ------------------------------------------------------------------ A: babysitter
at_s, pr_s, rp_s = run("sitter")
assert "**10:30:** We're home. We're at a restaurant" in rp_s
Q = ["7:30:** Leo to bed with his stuffed rabbit.", "7:40:** Maya can read for 20 minutes.", "8:00:** Maya to bed.",
     "7:00:** No screens from now on.", "Dinner:** Mac and cheese is in the fridge. Microwave 2 minutes.", "Please CALL, don't text, if anything comes up."]
for q in Q:
    assert q in rp_s, q
NOTE = "You didn't give a dinner time, so I left it without one. If you want a time on it, \"6:15\" would fit well."
assert NOTE in rp_s
vid = REPO / "media/studio-nov05/hourback/hb-reel-1110-sitter-at-6.mp4"
DUMP = ("my brain dump (made up for this post): · back by 10:30 · call, don't text · Maya: bed 8, reads 20 min first · "
        "mac and cheese, heat 2 min · no screens after 7 · Leo: bed 7:30, stuffed rabbit")
SHEET = ("Babysitter Notes – Maya (7) & Leo (3) · Claude's real note, shortened · kids made up for this post · "
         "Dinner: Mac and cheese is in the fridge. Microwave 2 minutes. · 7:00: No screens from now on. · "
         "7:30: Leo to bed with his stuffed rabbit. · 7:40: Maya can read for 20 minutes. · 8:00: Maya to bed. · "
         "10:30: We're home. … · Please CALL, don't text, if anything comes up. · Mom: ________ Dad: ________")
A = dict(
    id="hb-reel-1110-sitter-at-6", account="hourback", publish_at="2026-11-10T19:00:00-05:00",
    video="studio-nov05/hourback/hb-reel-1110-sitter-at-6.mp4", cover="studio-nov05/hourback/hb-reel-1110-sitter-at-6-cover.jpg",
    caption=(
        "Babysitter at 6 and it's all still in your head? Paste the messy brain dump into AI and ask for a fridge note sorted by time.\n\n"
        "WHY IT WORKS: you remember things in the order they pop into your head; a sitter needs them in the order the evening happens. "
        "AI works from what you paste, so it reorders your facts instead of inventing new ones.\n\n"
        f"THE REAL TEST: we made up a family and asked Claude (Anthropic) on Nov 5, 2026: \"{pr_s}\"\n"
        "A few lines, word for word: \"7:30: Leo to bed with his stuffed rabbit.\" · \"7:40: Maya can read for 20 minutes.\" · "
        "\"8:00: Maya to bed.\" It worked out the 7:40 itself.\n"
        f"And it flagged the one gap it could see: \"{NOTE}\"\n\n"
        "HOW: open ChatGPT, Claude or Gemini, type everything in any order, ask for a note sorted by time, one line each, then read "
        "every line before you print it.\n\n"
        "THE CATCH: AI can't add what you never mentioned. Add these yourself: allergies and medicines, emergency numbers (911 and a "
        "neighbour you trust), your phone numbers and your home address.\n\n"
        "PRIVACY TIP: first names are enough. Write your address and phone numbers on the printed note by hand, not into the chat.\n\n"
        "Family made up for this post.\n\n"
        "Do this: Paste your brain dump. Ask: sorted by time.\n\n"
        "Send this to whoever has a sitter booked this week.\n\n"
        "Follow to learn one real AI trick a day.\n\n"
        "#ai #learnai #claude #parenting #babysitter"),
    first_comment=(
        f"How we made this: one real run in Claude (Anthropic), model claude-opus-5-5, {METHOD}, {at_s[:10]} {at_s[11:16]} UTC. "
        "The family, names, times and restaurant are made up for this post. On screen: Claude's note, shortened (its title, the Dinner, "
        "7:00, 7:30, 7:40 and 8:00 lines, the call line and the phone blanks, word for word; its 10:30 line cut to its first sentence, \"We're home. …\"; bold markdown shown "
        "as plain text; phone blanks drawn shorter), and its note about the dinner time, word for word. Full prompt and reply in our public "
        "repo steadfold-autopost: studio/editorial/hb-nov05-run-sitter.txt. Results vary between apps and runs. Fact check (checked Nov 5 "
        "2026): the only claims in this post are the run itself (prompt and reply), checked against the saved transcript; no outside "
        "statistic, feature or safety claim is made."),
    alt_text=(
        "Illustrated Hourback Reel in periwinkle and cream: a white fridge with a digital clock magnet reading 5:48 and a smiling-sun "
        "magnet. Words: 'Babysitter at 6. Messy brain dump?' A big yellow note on the fridge door, lines written at odd angles: "
        f"'{DUMP}'. Then 'try this. Paste the mess. AI sorts it by time.' The yellow note flies off and Claude's real note slams onto "
        f"the door: '{SHEET}', and each timed line lights up in order. Then 'it spots the gap. It flags what you forgot. Still add "
        f"allergies.' with a card below the list, 'Its note under the list, word for word: {NOTE}', and the Dinner line lights up. "
        "Then 'Do this: Paste your brain dump. Ask: sorted by time. In ChatGPT, Claude or Gemini. Write phone numbers by hand.' The "
        "phone blanks light up, a tick lands, the clock reads 5:51. Ends: 'Follow to learn one real AI trick a day.' Family made up "
        "for this post."),
    beats=[
        f"[0.0 s] Babysitter at 6. Messy brain dump? | (clock magnet) 5:48 | (big yellow note on the fridge, 62 px) {DUMP} | "
        "(stamp) HOURBACK · YOUR EVENINGS BACK",
        "[2.0 s] try this | Paste the mess. AI sorts it by time. | (2.0-2.35 s the yellow note flies off; 2.1-2.4 s Claude's note slams "
        f"on, frame shake) {SHEET} | (2.9-4.7 s) each timed row lights in order",
        f"[6.8 s] it spots the gap | It flags what you forgot. Still add allergies. | (card, below the list rows) Its note under the "
        f"list, word for word · {NOTE} | (Dinner row lights)",
        "[10.2 s] Do this: | Paste your brain dump. Ask: sorted by time. | In ChatGPT, Claude or Gemini. Write phone numbers by hand. | "
        "(phone blanks light, tick, clock 5:51)",
        "[11.4 s to end, 2.8 s] Follow to learn one real AI trick a day.",
    ],
    hook_options=["Babysitter at 6. Messy brain dump?", "Sitter at 6. No notes yet.", "Sitter's here at 6. Fridge note?"],
    hook_picker=PICKER + "Verdict A: #3 'Babysitter at 6. Messy brain dump?' (clearest: it points at the trick; 'Babysitter' reads "
                         "faster than 'Sitter', which some read as pet sitter; #1 the most urgent, #2 the weakest). Adopted, listed first.",
    duration_s=round(dur(vid), 2),
    style=("Body: drawn occasion scene, NEW composition (CD Nov 4 template-sameness order): a fridge front fills the lower frame with "
           "a 5:48 digital clock magnet on the freezer; no table line, no card at the bottom (the last 3 HB Reels, dinners / Nonna / "
           "retirement, all used the wall + table + bottom card template). Before -> after: frame 0 = hook + the big messy brain-dump "
           "note + the clock (picture + number, 2 text blocks, no empty box); at 2.1 s Claude's real sorted note slams onto the door. "
           "Motion: zoom punch-in on every cut, light-sweep wipe, frame shake as the note lands, rows light in order, clock colon "
           "blinks and jumps to 5:51, confetti on Do this. Dedicated cover: kinetic big text (style 5, LOUD): giant serif 'Babysitter "
           "at 6. / Messy brain dump?' with a yellow pill on line 2, 5:48 clock + 3 real rows (labelled shortened), Caveat line, "
           "stamp. Grid: after Mon 7 pm retirement (big number, quiet), before Wed 5:45 pm Day 15 (Look B, loud). Not Look B, not big "
           "number, not the taped lined note. 9-tile window Nov 5 flight -> Nov 11 Day 15: giant word, Look B, sticky note, follow "
           "the line, reframe, Look B, big number, kinetic, Look B = 7 styles."),
    send_test=False,
    sources=[f"studio/editorial/hb-nov05-run-sitter.txt (fresh, isolated verbatim Claude run via claude -p, {at_s})"],
    notes=(
        "Standalone, no Part 2, no on-screen send line (Fri test stays clean); one caption send line. No trial flag. Desk grade: >=5 s "
        "and >=30% on >=40 at the 29 h read. Number on frame 0 ('6' in the hook, clock 5:48) and in caption line 1. Payoff words at "
        "2.0 s, real sorted note fully in by 2.4 s. The 'Real Claude reply' chip of earlier builds is dropped; the honesty labels sit "
        "on the notes ('my brain dump (made up for this post)'; 'Claude's real note, shortened · kids made up for this post'). Music "
        "hb-x-future-easy (existing HB track in tools/music-library.json; the last 3 HB Reels used smart-bounce / ta-da-funk), "
        "-13.8 LUFS; SFX paper slap + sticker pops. 1080x1920 30 fps H.264 + AAC, 3.0 MB. Builder: studio/editorial/nov05_hourback.py "
        "sitter (cover nov05_hourback_covers.py; run nov05_hourback_run.py sitter). Transcript scanned: no real personal name or "
        "employer (Maya, Leo are ours). Topic check: no babysitter/childcare piece on HB in 14 days; not a speech. No children are "
        "drawn (names on the note only). CD GATE FIXES (Nov 5): (1) frame 0 is now hook + big messy brain-dump note (62 px Caveat, "
        "lines at odd angles, out of time order) + clock; the sorted real note lands on the 'AI sorts it by time' beat (2.1-2.4 s); "
        "(2) cover hook re-set on 2 lines with open leading so the pill no longer hits 'Babysitter'; (3) its-note card moved below the "
        "list rows (y 1318), and the call/blank lines it would half-cover are hidden during that beat; (4) the small taped prompt "
        "sticky (and its white tape strip, the ~2.5 s artifact) is gone, replaced by the big frame-0 note; (5) the contradictory "
        "10:30 row is cropped (note labelled 'shortened'; caption and first comment say so); (6) beat 2 now 'It flags what you "
        "forgot. Still add allergies.' and the caption's CATCH tells people to add allergies, medicines, emergency numbers, their "
        "phone numbers and home address by hand. Durations 2.0 / 4.8 / 3.4 / 4.0 = 14.2 s; follow line 2.8 s. Self-review (QG-1): "
        "frames 0 / 2.1 / 2.5 / 4.5 / 7.5 / 9.5 / 11 / 13.5, the full strip and the cover checked after the re-render. CD ROUND 3 FIXES (Nov 5): "
        "(1) the clock and sun magnets fade out 0.25 s before the follow pill lands on the freezer (no half-hidden 5:51); (2) fridge "
        "moved down 28 px so the 2-line Do-this sub clears its top edge, and the Do-this confetti bursts from the note, not over the "
        "sub; (3) the fridge is now a short fridge (ends y 1560, feet + floor shadow) so no empty white door below the note; note "
        "rows tightened (42 px Caveat) and all content sits above ~y 1530; (4) beat 2 headline leading opened (1.16) so 'flags/you' "
        "descenders clear the pill; (5) a 10:30 line is back on the note, cut word for word to its first sentence: 'We're home. …' "
        "(keeps 'back by 10:30', drops the contradictory restaurant sentence). Strip and frames 0 / 3.5 / 8 / 11 / 13.5 checked after "
        "the re-render. Doubts: the fridge now reads a little short and wide (like an under-counter fridge). Not yet seen by an independent reviewer (QG-5)."),
)

# ------------------------------------------------------------------ C: Day 15
at_c, pr_c, rp_c = run("chores")
import nov05_hourback_feed as F  # noqa: E402
assert F.REPLY == rp_c
PLAIN = rp_c.replace("**", "")
WORDS = len(PLAIN.split())
assert WORDS == 66, WORDS
LIGHT = "**Trash + recycling (Tue night):** me, since I only have one dish night"
assert LIGHT in rp_c
C = dict(
    id="hb-day15-roommate-chores", account="hourback", publish_at="2026-11-11T17:45:00-05:00",
    images=["studio-nov05/hourback/hb-day15-roommate-chores/01.jpg", "studio-nov05/hourback/hb-day15-roommate-chores/02.jpg"],
    caption=(
        "4 roommates and nobody knows whose turn it is? Tell AI the chores and who's busy when, and ask for one friendly group text "
        "with a fair rotation.\n\n"
        "AI, for real · Day 15. One real test of what AI can do, with the output shown.\n\n"
        "WHY IT WORKS: chore fights are rarely about the dishes, they're about feeling blamed. A text that proposes a plan (\"so nobody "
        "has to guess whose turn it is\") talks about the system, not the person. Telling AI who's busy when lets it work around real "
        "schedules: it gave Theo, who works weekend nights, Monday and Tuesday dishes.\n\n"
        "THE REAL TEST (names made up for this post), Claude (Anthropic), Nov 5, 2026:\n"
        f"Prompt: \"{pr_c}\"\n"
        f"Slide 2 shows what we told it and its text, word for word ({WORDS} words, counted).\n\n"
        "THE CATCH: check the maths before you send. It gave \"me\" (you) 1 dish night plus the Tuesday trash, and left \"me\" out of the "
        "weekly counters and bathroom, while the other three each get 2 dish nights and share the weekly jobs. Friendly, but not quite "
        "fair. Ask it to even things out, or fix it yourself, before it goes to the group.\n\n"
        "PRIVACY TIP: first names are enough. Don't paste your old group chat, anyone's work schedule details or your address; "
        "\"works weekend nights\" is all it needs.\n\n"
        "Do this: in ChatGPT, Claude or Gemini, list the chores and who's busy when. Then ask: \"Write a short, friendly text for our "
        "group chat that proposes a fair weekly rotation, so nobody feels blamed.\"\n\n"
        "Send this to the group chat that needs it.\n\n"
        "Follow to learn one real AI trick a day.\n\n"
        "#ai #learnai #claude #roommates #chores\n\n"
        "AI, for real · Day 16 lands Fri Nov 13 at 5:45 pm."),
    first_comment=(
        f"Made-up house, real output: run in Claude (Anthropic), model claude-opus-5-5, {METHOD}, {at_c[:10]} {at_c[11:16]} UTC. "
        "Sam, Ana, Theo and the chores are made up for this post. Slide 2 shows Claude's text word for word (its bold labels kept as "
        f"bold, its two emoji kept); {WORDS} words, counted in code. Full prompt and reply in our public repo steadfold-autopost: "
        "studio/editorial/hb-nov05-run-chores.txt. Results vary between apps and runs. Fact check (checked Nov 5 2026): the only "
        "claims in this post are the run itself and the chore count in the caption, checked against the saved transcript."),
    alt_text=(
        "Hourback 2-slide carousel. Slide 1: 'AI, for real · Day 15' badge, '4 roommates. Whose turn is it?' in a large serif with a "
        "periwinkle highlight, a drawn sink piled with plates and 4 mugs, and the handwritten note 'new one every Mon · Wed · Fri'. "
        "Slide 2: 'Tell AI the chores and who's busy when. It wrote this text:' above a white card headed 'Text to House group chat' "
        f"with one purple message bubble: '{PLAIN}' Below it, a yellow note: 'what we told it (made up for this post): {F.TOLD}'. "
        "Handwritten: 'Claude's real text, word for word · roommates made up for this post'."),
    beats=[
        "[slide 1] AI, FOR REAL · DAY 15 | 4 roommates. Whose turn is it? | (sink with plates and 4 mugs) | new one every Mon · Wed · Fri | "
        "(stamp) HOURBACK · YOUR EVENINGS BACK",
        f"[slide 2] 2/2 | Tell AI the chores and who's busy when. | It wrote this text: | TEXT TO | House group chat | {PLAIN} | "
        f"(yellow note) what we told it (made up for this post): · {F.TOLD} | Claude's real text, word for word · roommates made up for this post",
    ],
    hook_options=["4 roommates. Whose turn is it?", "4 roommates, 1 messy kitchen.", "Dishes piling up? One fair text."],
    hook_picker=PICKER + "Verdict C: #1 '4 roommates. Whose turn is it?' (an argument people have actually had; the cover only has to "
                         "earn the swipe and slide 2 delivers the text; #3 clearest, #2 no tension). Adopted, listed first.",
    duration_s=None,
    style=("Series layout 'AI, for real', SAME as Day 14 (Look B big-headline pills cover, kicker badge, one drawn object bottom-left, "
           "'new one every Mon · Wed · Fri', stamp; slide 2 = the indigo white-card slide with the real output + the yellow 'what we "
           "told it' note + the save line). Loud cover; series number and '4' on the cover."),
    send_test=False,
    sources=[f"studio/editorial/hb-nov05-run-chores.txt (fresh, isolated verbatim Claude run via claude -p, {at_c})"],
    notes=(
        "Fulfils Day 14's caption promise ('Day 15 lands Wed Nov 11 at 5:45 pm'); caption's last line promises Day 16 on Fri Nov 13 at "
        "5:45 pm: the next studio run must build it. Builder: studio/editorial/nov05_hourback_feed.py (copy of nov04_hourback_feed.py; "
        "run: nov05_hourback_run.py chores). Topic check: no chores/roommates piece in 14 days; the Oct 27 group-chat Reel summarised a "
        "family chat (different job). Transcript scanned: no real personal name or employer. The CATCH is real and counted: 'me' gets 1 "
        "dish night + trash and no weekly jobs. Bubble set at 31 px (Day 14: 40 px) because the text is 66 words vs 48; the yellow note "
        "and save line moved down 50 px to fit. Self-review (QG-1): both slides checked at full size side by side; fixes: bubble ran "
        "under the yellow note (smaller type, tighter paragraph gaps), the save line touched the note (moved), the cover object's "
        "'whose turn?' label repeated the hook (removed), faucet re-drawn on the sink rim. Doubt: the sink drawing is busier than Day "
        "14's phone (plates and mugs overlap as a pile). Effort kept to the desk's 'less feed effort' order. Not yet seen by an "
        "independent reviewer (QG-5)."),
)
del C["duration_s"]

BANNED = re.compile(r"example|e\.g\.|hypothetical|for illustration", re.I)
for e in (A, C):
    assert not BANNED.search(json.dumps(e, ensure_ascii=False)), e["id"]
for e in (A, C):
    assert len(e["caption"]) <= 2150 and len(e["first_comment"]) <= 2200, (e["id"], len(e["caption"]))
out = ED / "nov05/hourback.json"
out.write_text(json.dumps([A, C], ensure_ascii=False, indent=1) + "\n")
print(out, A["duration_s"])

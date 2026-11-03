#!/usr/bin/env python3
"""Writes studio/editorial/nov03/hourback.json (Hourback, Nov 3 2026 studio run). Quotes are checked against the saved
real-run transcripts before the file is written.

    python3 studio/editorial/nov03_hourback_manifest.py
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
MEDIA = REPO / "media"
OUTF = REPO / "studio/editorial/nov03/hourback.json"
FOLLOW = "Follow to learn one real AI trick a day."
ISO = ("in a fresh, isolated session (Claude Code CLI print mode in an empty folder, no tools, no earlier chat, no Project "
       "or settings context loaded)")


def run_text(slug):
    return (REPO / f"studio/editorial/hb-nov03-run-{slug}.txt").read_text()


def run_at(slug):
    for ln in run_text(slug).splitlines():
        if ln.startswith("Run at (UTC):"):
            return ln.split(": ", 1)[1].strip()


def check_quotes(slug, quotes):
    body = run_text(slug).split("===== REPLY (verbatim) =====", 1)[1].replace("\n", " ").replace("*", "")
    prompt = run_text(slug).split("===== PROMPT (verbatim) =====", 1)[1].split("===== REPLY")[0].replace("\n", " ")
    for q in quotes:
        if q not in body and q not in prompt:
            sys.exit(f"quote not in {slug} transcript: {q!r}")


def dur(rel):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(MEDIA / rel)],
                         capture_output=True, text=True, check=True).stdout
    return round(float(out), 2)


ENTRIES = []

# ---------------------------------------------------------------- A: Fri Nov 6, 7 pm
A_JOE = ("I can't believe how beautiful the rocking chair turned out after all your work on it. It's going right next to "
         "the crib, and every 3 a.m. feeding will happen in it.")
A_MARCO = "We're going to use it to stock up on diapers and wipes"
A_PROMPT_ASK = ("Write a 2-sentence note for each one. Name the gift and say one specific way we'll use it. "
                "Don't make them all sound the same.")
check_quotes("thanks", [A_JOE, A_MARCO, A_PROMPT_ASK, "My baby shower was on Saturday and I have 20 thank-you notes to write today.",
                        "Your handmade quilt is already folded over the back of the nursery chair, and I keep running my hand over the stitching.",
                        "Thank you for the baby carrier! I'm planning to wear the baby on our morning walks around the block",
                        "Thank you so much for the $50 gift card.", "You all know me too well."])
a_vid = "studio-nov03/hourback/hb-reel-1106-thank-you-20.mp4"
ENTRIES.append(dict(
    id="hb-reel-1106-thank-you-20", account="hourback", publish_at="2026-11-06T19:00:00-05:00",
    video=a_vid, cover="studio-nov03/hourback/hb-reel-1106-thank-you-20-cover.jpg",
    caption=(
        "Baby shower's over and 20 thank-you notes left to write? Paste who gave what into AI and ask for a short note for each one.\n\n"
        "WHY IT WORKS: the hard part of 20 notes isn't the writing, it's starting each one. Once AI knows the gift, it can "
        "say how you'll use it, and that's the line that makes a note feel personal. Asking for them to sound different "
        "stops 20 copies of the same sentence.\n\n"
        "THE REAL TEST: we made up a baby shower with 20 guests and gifts and asked Claude (Anthropic) on Nov 3, 2026: "
        "\"My baby shower was on Saturday and I have 20 thank-you notes to write today. Here's who gave what: "
        "[1. Aunt Rosa: a handmade quilt … 20. My book club: a basket of snacks for late nights] "
        f"{A_PROMPT_ASK}\"\n"
        f"It wrote all 20. Note 3 (Grandpa Joe, a rocking chair he fixed up), word for word: \"{A_JOE}\"\n\n"
        "HOW (about 15 minutes):\n"
        "1. Open ChatGPT, Claude or Gemini.\n"
        "2. Type each person and their gift, one per line.\n"
        f"3. Ask: \"{A_PROMPT_ASK}\"\n"
        "4. Read each note, change anything that isn't true for you, then copy it into the card by hand.\n\n"
        "THE CATCH: AI guesses details it can't know: read every note and fix anything that isn't true before you send. "
        "It wrote about a nursery chair, morning walks and the spot next to the crib, and for the $50 gift card it wrote "
        "\"We're going to use it to stock up on diapers and wipes\". None of that came from us. Add one real detail of "
        "your own where you can.\n\n"
        "PRIVACY TIP: first names and the gift are enough. Leave out addresses, last names and anything about anyone's health.\n\n"
        "Names and gifts made up for this post.\n\n"
        "Do this: Paste names and gifts. Ask for notes. Edit before you send.\n\n"
        "Send this to whoever has a stack of cards to write.\n\n"
        f"{FOLLOW}\n\n"
        "#ai #thankyounotes #babyshower #claude #learnai"),
    first_comment=(
        f"How we made this: one real run in Claude (Anthropic), model claude-opus-5-5, {ISO}, Nov 3 2026 "
        f"{run_at('thanks')[11:16]} UTC. The 20 guests and gifts are made up for this post. On screen: notes 1 and 2 shortened "
        "(marked …), the first sentence of notes 3-20 as the counter runs, and note 3 in full, all word for word. Full prompt "
        "and all 20 notes in our public repo steadfold-autopost: studio/editorial/hb-nov03-run-thanks.txt. Results vary "
        "between apps and runs. Fact check (Nov 3 2026): the only claims in this post are the run itself (prompt and reply), "
        "checked against the saved transcript; no outside statistic or feature claim is made."),
    alt_text=(
        "Illustrated Hourback Reel in periwinkle and cream: a desk with a stack of blank cards tagged '20 to write', a wire "
        "OUT tray labelled 'mail today', and an empty note card that says 'Note 0 of 20' and 'Dear…'. Words: 'Baby shower's "
        "over. 20 notes left.' Then 'try this. Paste who gave what. AI drafts all 20. Claude's real notes, shortened:' A yellow "
        "note, 'gift list we made up for this post: 1. Aunt Rosa: a handmade quilt, 2. Priya: a baby carrier, 3. Grandpa Joe: "
        "a rocking chair he fixed up … 20 in all', flies into the card. Note 1 of 20, Aunt Rosa: 'Your handmade quilt is "
        "already folded over the back of the nursery chair, and I keep running my hand over the stitching. …' Note 2 of 20, "
        "Priya: 'Thank you for the baby carrier! I'm planning to wear the baby on our morning walks around the block…' Then "
        "the counter runs to Note 20 of 20 while sealed envelopes fly into the tray and the stack drops to '0 to write'. "
        "Then 'every note is different. It names each gift and how you'll use it.' with Note 3, word for word, Grandpa Joe: "
        f"'{A_JOE}' The second sentence is highlighted. Then 'Do this: Paste names and gifts. Ask for notes. In ChatGPT, "
        f"Claude or Gemini. Edit before you send.' and a tick. Ends: '{FOLLOW}' Names and gifts made up for this post."),
    beats=[
        "[0.0 s] Baby shower's over. 20 notes left. | (stack tag) 20 to write | (card) Thank you | (tray) OUT · mail today | "
        "(note card) Note 0 of 20 · Dear… | (chip) Real Claude reply · names and gifts made up for this post | (stamp) HOURBACK · YOUR EVENINGS BACK",
        "[2.0 s] try this | Paste who gave what. AI drafts all 20. | Claude's real notes, shortened: | (note, 44-46 px, 2.0-3.25 s) "
        "gift list we made up for this post: · 1. Aunt Rosa: a handmade quilt · 2. Priya: a baby carrier · 3. Grandpa Joe: a rocking chair he fixed up … 20 in all",
        "[3.25 s] Note 1 of 20 · Aunt Rosa · Your handmade quilt is already folded over the back of the nursery chair, and I keep running my hand over the stitching. … "
        "→ [4.55 s] Note 2 of 20 · Priya · Thank you for the baby carrier! I'm planning to wear the baby on our morning walks around the block… "
        "→ [5.85-7.25 s, ~0.08 s each] Note 3…20 of 20 with each note's real first sentence + … (Grandpa Joe … My book club: 'You all know me too well. …'); stack tag counts 19 → 0 to write",
        f"[8.0 s] every note is different | It names each gift and how you'll use it. | (note card, 46 px) Note 3, word for word · Grandpa Joe · {A_JOE}",
        "[11.4 s] Do this: | Paste names and gifts. Ask for notes. | In ChatGPT, Claude or Gemini. Edit before you send.",
        f"[11.9 s to end, 2.7 s] {FOLLOW}",
    ],
    hook_options=["Baby shower's over. 20 notes left.", "20 thank-you notes. Due today.", "20 cards to write by tonight?"],
    duration_s=dur(a_vid),
    style=("Body: drawn occasion scene (desk order 4: deadline + number on frame 0), new composition: a desk with a 20-card "
           "stack that shrinks as the counter runs, an OUT tray that fills with sealed envelopes, and a note card where the "
           "real notes land. Dedicated cover: sticky-note list (style 13, QUIET) with a drawn x20 envelope stack. Grid: after "
           "Fri 5:45 pm Day 13 (series Look B, loud), before Sat 7 pm B (follow the line, loud). 9-tile window Nov 2 cue -> "
           "Nov 7: compare, Look B, kinetic, reframe, one giant word, sticky note, follow the line = 7 styles."),
    send_test=False,
    sources=[f"studio/editorial/hb-nov03-run-thanks.txt (fresh, isolated verbatim Claude run via claude -p, {run_at('thanks')})"],
    notes=("Standalone, no Part 2, no callback. No trial flag. Desk grade: >=5 s and >=30% on >=40. Number on frame 0 ('20') "
           "and in caption line 1. Payoff words at 2.0 s; first real note at 3.25 s; counter at 20 of 20 by 7.25 s; note 3 "
           "held 3.4 s with its 'how we'll use it' sentence highlighted. Follow pill on screen 2.7 s (from 11.9 s), placed in "
           "the gap under the Do-this line. Music hb-x-future-easy (existing HB track in tools/music-library.json), -13.9 LUFS integrated, 2.1 MB; SFX paper slap + sticker pops from the library. "
           "1080x1920 30 fps H.264 + AAC. Builder: studio/editorial/nov03_hourback.py thanks (+ nov03_hourback_covers.py; "
           "run: nov03_hourback_run.py thanks). Self-review (QG-1) fixes: '20 to write' tag hit the sub line and covered "
           "'Thank you' (moved beside the stack); 'mail today' sat under the envelopes (moved below the tray); note lines "
           "rewrapped to fill the card; a wrap bug doubled a line on the Lena riffle card (fixed); beat-2 header changed "
           "from 'Note 3 of 20' with a 3/20 bar to 'Note 3, word for word' with a full bar (all 20 are done by then); follow "
           "pill moved off the tray label. Gate rev (Nov 3, coordinator): frame-0 hook changed to the picker's choice 'Baby shower's over. 20 notes left.' (names the occasion; 6 words); cover unchanged. Round 3 (coordinator): 'Edit before you send.' added under the Do-this line (follow pill moved to y 724 to clear it) and the caption's CATCH now says plainly that AI guesses details it can't know. RUN NOTE: this run is the isolated re-run; an earlier non-isolated run of the "
           "same prompt was discarded unused because the CLI had loaded the account's Project context (see "
           "nov03_hourback_run.py). Not yet seen by an independent reviewer (QG-5)."),
))


# ---------------------------------------------------------------- B: Sat Nov 7, 7 pm
B_ASK = ("Plan 5 weeknight dinners for 2 adults, each under 30 minutes, that share ingredients so nothing goes to waste. "
         "Budget about $80.")
B_DAYS = ["Mon: Chicken fajitas.", "Tue: Chicken fried rice.", "Wed: Black bean quesadillas.",
          "Thu: Garlic chicken and broccoli pasta.", "Fri: Rice and bean burrito bowls."]
B_REUSE = ["Chicken: Mon, Tue, Thu", "Bell peppers: Mon, Wed, Fri", "Black beans: Wed, Fri"]
B_RICE = "Rice: Tue, Fri. Cook a double batch Tuesday, since day-old rice is better for fried rice anyway."
check_quotes("dinners", [B_ASK, B_RICE, "Shopping list (about $70 to $80)"] + B_DAYS + B_REUSE)
b_vid = "studio-nov03/hourback/hb-reel-1107-5-dinners.mp4"
ENTRIES.append(dict(
    id="hb-reel-1107-5-dinners", account="hourback", publish_at="2026-11-07T19:00:00-05:00",
    video=b_vid, cover="studio-nov03/hourback/hb-reel-1107-5-dinners-cover.jpg",
    caption=(
        "Store closes at 9 and no plan for the week? Ask AI for 5 dinners that share ingredients, with one shopping list.\n\n"
        "WHY IT WORKS: food goes to waste when each recipe needs its own half-bag of something. Asking for dinners that "
        "share ingredients makes AI plan the week as one shop: the same chicken, peppers and beans turn up on different "
        "nights, so the list gets shorter and less is left over.\n\n"
        "THE REAL TEST: we made up the ask and gave it to Claude (Anthropic) on Nov 3, 2026: \"The grocery store closes at 9 "
        f"and I need to shop for the week. {B_ASK} Give me the 5 dinners (one line each), then one shopping list, then tell "
        "me which ingredients get used more than once. Keep it short.\"\n"
        "Its 5 dinners, word for word: " + " · ".join(f'"{d}"' for d in B_DAYS) + "\n"
        "It priced the list at \"about $70 to $80\" (its estimate), and listed what gets reused, word for word: "
        + " · ".join(f'"{r}"' for r in B_REUSE) + ".\n\n"
        "HOW (5 minutes before you leave):\n"
        "1. Open ChatGPT, Claude or Gemini.\n"
        "2. Say how many dinners, for how many people, how much time and your budget.\n"
        "3. Ask for dinners \"that share ingredients so nothing goes to waste\", one shopping list, and which ingredients get used more than once.\n"
        "4. Cross off what you already have, then shop the list.\n\n"
        f"THE CATCH: read the plan before you trust it. One of its tips said \"{B_RICE}\" But the fried rice is on Tuesday, "
        "so to have day-old rice, cook it Monday night. Prices are its guesses, not your store's.\n\n"
        "PRIVACY TIP: \"2 adults, about $80\" is all it needs. No names, address or health details.\n\n"
        "Plan made up for this post.\n\n"
        "Do this: Ask for 5 dinners that share ingredients.\n\n"
        "Send this to whoever does the weekly shop.\n\n"
        f"{FOLLOW}\n\n"
        "#ai #mealplanning #groceries #claude #learnai"),
    first_comment=(
        f"How we made this: one real run in Claude (Anthropic), model claude-opus-5-5, {ISO}, Nov 3 2026 "
        f"{run_at('dinners')[11:16]} UTC. The ask (2 adults, 5 weeknights, about $80) is made up for this post. On screen: "
        "the 5 dinner names word for word (each line's ingredient list cut) and 3 of its 'used more than once' lines, word "
        "for word. Full plan, shopping list and tips in our public repo steadfold-autopost: "
        "studio/editorial/hb-nov03-run-dinners.txt. Prices are Claude's estimates, not checked against any store. Results "
        "vary between apps and runs. Fact check (Nov 3 2026): the only claims in this post are the run itself, checked "
        "against the saved transcript."),
    alt_text=(
        "Illustrated Hourback Reel in periwinkle and cream: a kitchen wall with a clock at about 8:10, a yellow note that "
        "says 'store closes at 9 pm', an empty paper grocery bag, and an empty week card that says 'Dinners 0 of 5'. Words: "
        "'Store closes at 9. 5 dinners?' Then 'try this. AI plans 5 dinners and one shopping list. Claude's real plan, "
        "shortened:' A yellow note, 'what we told it (made up for this post): 5 weeknight dinners for 2 adults, each under "
        "30 minutes, about $80 in total, share ingredients so nothing goes to waste', flies into the card. The rows land one by one "
        "while drawn groceries drop into the bag: 'Mon Chicken fajitas.', 'Tue Chicken fried rice.', 'Wed Black bean "
        "quesadillas.', 'Thu Garlic chicken and broccoli pasta.', 'Fri Rice and bean burrito bowls.' Then 'it reuses "
        "ingredients. So less food goes to waste. Its lines, word for word:' and the card header changes to 'Chicken: Mon, "
        "Tue, Thu', then 'Bell peppers: Mon, Wed, Fri', then 'Black beans: Wed, Fri', lighting the matching days. Then 'Do "
        "this: Ask for 5 dinners that share ingredients. In ChatGPT, Claude or Gemini.' The note glows and the card gets a "
        f"tick. Ends: '{FOLLOW}' Plan made up for this post."),
    beats=[
        "[0.0 s] Store closes at 9. 5 dinners? | (note) store closes · at 9 pm | (bag) groceries | (card) Dinners 0 of 5 · ? | "
        "(chip) Real Claude reply · plan made up for this post | (stamp) HOURBACK · YOUR EVENINGS BACK",
        "[2.0 s] try this | AI plans 5 dinners and one shopping list. | Claude's real plan, shortened: | (note, 44 px, 2.0-3.2 s) "
        "what we told it (made up for this post): · 5 weeknight dinners for 2 adults · each under 30 minutes, about $80 in total · share ingredients so nothing goes to waste",
        "[3.25-6.05 s, one row every 0.7 s, 44 px serif] Dinners 1…5 of 5 · Mon Chicken fajitas. · Tue Chicken fried rice. · "
        "Wed Black bean quesadillas. · Thu Garlic chicken and broccoli pasta. · Fri Rice and bean burrito bowls. | (bag item) RICE",
        "[8.0 s] it reuses ingredients | So less food goes to waste. | Its lines, word for word: | (card header, ~1.05 s each) "
        "Chicken: Mon, Tue, Thu → Bell peppers: Mon, Wed, Fri → Black beans: Wed, Fri (matching day rows light up)",
        "[11.4 s] Do this: | Ask for 5 dinners that share ingredients. | In ChatGPT, Claude or Gemini. | (card) Dinners 5 of 5 + the 5 rows",
        f"[11.9 s to end, 2.7 s] {FOLLOW}",
    ],
    hook_options=["Store closes at 9. 5 dinners?", "5 dinners. One grocery run.", "$80 for 5 dinners this week?"],
    duration_s=dur(b_vid),
    style=("Body: drawn occasion scene (deadline + number on frame 0), new composition: kitchen wall with a clock and a "
           "'store closes at 9 pm' note, a paper grocery bag that fills, and a Mon-Fri week card whose rows light up per "
           "shared ingredient. Dedicated cover: follow the line (LOUD): Claude's 3 reuse lines drawn as coloured lines from "
           "ingredient chips to weekday pills. Grid: after Fri 7 pm A (sticky note, quiet). Last HB follow-the-line cover was "
           "Oct 30 (group chat), outside the 9-tile window. Window Nov 2 Day 11 -> Nov 7: Look B, compare, kinetic, reframe, "
           "one giant word, sticky note, follow the line = 7 styles."),
    send_test=False,
    sources=[f"studio/editorial/hb-nov03-run-dinners.txt (fresh, isolated verbatim Claude run via claude -p, {run_at('dinners')})"],
    notes=("Standalone, different topic family from A (food planning vs writing). Food topics in the last 14 days: Day 10 "
           "pancakes (recipe scaling, Oct 30), Day 12 potluck (diets, Nov 4); this one is a week plan around one shop, a "
           "different job, but it is the 3rd food-adjacent HB piece in 9 days (doubt). No trial flag. Desk grade: >=5 s and "
           ">=30% on >=40. Payoff words at 2.0 s; first real row at 3.25 s, all 5 by 6.05 s; reuse lines 8.15-11.4 s. "
           "Follow pill on screen 2.7 s (from 11.9 s), above the scene, clear of the card. Music hb-x-ta-da-funk (existing HB track), -13.8 LUFS integrated, "
           "1.8 MB. Builder: studio/editorial/nov03_hourback.py dinners (+ covers; run: nov03_hourback_run.py dinners). "
           "Self-review (QG-1) fixes: the made-up ask note ran under the grocery bag (note now drawn on top, 44 px, moved "
           "down off the sub line); cover hand line repeated '5 dinners' (now 'AI plans them to share ingredients'); cover "
           "chips widened so 'Bell peppers'/'Black beans' fit. Gate rev (Nov 3, coordinator): follow pill moved up into the gap under 'In ChatGPT, Claude or Gemini.' (y 686; it overlapped the week card's border and tick) and the grocery bag moved 20 px down so the pill clears its items; payoff reworded from 'from one shopping list' (ambiguous: give or get?) to 'AI plans 5 dinners and one shopping list.', which is what the run returned. Hook kept: the coordinator's note that the run had no $80 budget is not right (the prompt says 'Budget about $80'), but option 3 stays third as asked. Round 3: made-up-ask note line now 'each under 30 minutes, about $80 in total' (it read as $80 a dinner); cover stamp moved from the top (straddled the 3:4 grid crop) to x 820, y 1480. The caption's CATCH names a real slip in the reply (day-old "
           "rice tip vs Tuesday fried rice); that line is deliberately NOT shown on screen. Isolated re-run (see A's note). "
           "Not yet seen by an independent reviewer (QG-5)."),
))

# ---------------------------------------------------------------- C: Fri Nov 6, 5:45 pm, AI, for real · Day 13
# Gate rev (Nov 3): re-run with dates that fit the Fri Nov 6 post -> hb-nov03-run-landlord2.txt (isolated, once).
C_PROMPT = ("Today is Friday, November 6. The heat in my apartment has been off since Wednesday, November 4, and it's 16°C "
            "inside. I texted my landlord, Dan, on Wednesday and he said he'd look at it, but nothing has happened. Write me "
            "a short email to send him before 5 pm today. Polite but firm: what's wrong, since when, what I've already done, "
            "and that I need the heat repaired by Saturday, November 7. Sign it from Alex in unit 4B. Under 120 words.")
C_SUBJ = "Heat Not Working in Unit 4B: Repair Needed by Saturday"
C_P1 = ("The heat in my apartment has not worked since Wednesday, November 4, and the indoor temperature is now 16°C. I "
        "texted you about it on Wednesday, and you said you'd look into it, but no repair has been made yet.")
C_P2 = ("The apartment is getting uncomfortably cold, so I need the heat repaired by Saturday, November 7. Please let me know "
        "today when someone will come, and I'll make sure they can get in.")
C_ASKLINE = "Please let me know today when someone will come, and I'll make sure they can get in."
check_quotes("landlord2", [C_PROMPT, C_SUBJ, C_P1, C_P2, "Thank you, Alex Unit 4B"])
C_IMGS = [f"studio-nov03/hourback/hb-day13-landlord-email/0{k}.jpg" for k in (1, 2)]
ENTRIES.append(dict(
    id="hb-day13-landlord-email", account="hourback", publish_at="2026-11-06T17:45:00-05:00",
    images=C_IMGS,
    caption=(
        "16°C inside and the landlord still hasn't fixed the heat? Tell AI what's wrong, since when, what you've done and "
        "what you need, and ask for a short, polite but firm email.\n\n"
        "AI, for real · Day 13. One real test of what AI can do, with the output shown.\n\n"
        "WHY IT WORKS: when you're cold and annoyed, the email comes out either too soft or too angry. Giving AI the four "
        "facts (what's wrong, since when, what you've already done, what you need by when) gets you a message that's calm, "
        "dated and hard to ignore, and a written record if you need one later.\n\n"
        f"THE REAL TEST (names, unit and dates made up for this post), Claude (Anthropic):\nPrompt: \"{C_PROMPT}\"\n"
        "Slide 2 is its email, word for word. Notice it turned our ask into one clear request with a time: "
        f"\"{C_ASKLINE}\"\n\n"
        "THE CATCH: AI doesn't know the rules where you live. Heat and repair rules for rentals depend on your province or "
        "city, so check your local tenant rules before you quote any of them. Keep a copy of the email and of your first "
        "text, and check every date in the draft before you send it.\n\n"
        "PRIVACY TIP: you don't need to paste your lease, your landlord's details or your phone number. A first name and "
        "unit number are enough to draft it.\n\n"
        "Do this: in ChatGPT, Claude or Gemini, type what's wrong, since when, what you've already done, and what you need "
        "by when. Then ask: \"Write me a short email. Polite but firm. Under 120 words.\"\n\n"
        "Send this to whoever's waiting on a repair.\n\n"
        f"{FOLLOW}\n\n"
        "#ai #renting #tenant #claude #learnai\n\n"
        "AI, for real · Day 14 lands Mon Nov 9 at 5:45 pm."),
    first_comment=(
        f"Made-up apartment, real output: run in Claude (Anthropic), model claude-opus-5-5, {ISO}, Nov 3 2026 "
        f"{run_at('landlord2')[11:16]} UTC. The names, unit and dates (Wed Nov 4 to Sat Nov 7) are made up for this post. "
        "Slide 2 shows Claude's email word for word, from the subject line to the sign-off. Full prompt and reply in our "
        "public repo steadfold-autopost: studio/editorial/hb-nov03-run-landlord2.txt. Not legal advice; tenant rules vary "
        "by province and city. Results vary between apps and runs. Fact check (Nov 3 2026): the only claims in this post "
        "are the run itself, checked against the saved transcript; the caption names no specific law."),
    alt_text=(
        "Hourback 2-slide carousel. Slide 1: 'AI, for real · Day 13' badge, '16°C inside. Landlord's not fixing it?' in a "
        "large serif with a periwinkle highlight, a drawn wall thermostat reading 16°C with a blue frost mark, and the "
        "handwritten note 'new one every Mon · Wed · Fri'. Slide 2: 'Tell AI what's wrong and what you need. It wrote this "
        f"email:' above a white email card. Subject: {C_SUBJ}. 'Hi Dan, {C_P1} {C_P2} Thank you, Alex, Unit 4B.' "
        "Handwritten: 'Claude's real email, word for word · names and dates made up for this post'."),
    beats=[
        "[slide 1] AI, FOR REAL · DAY 13 | 16°C inside. Landlord's not fixing it? | (thermostat) 16°C | new one every Mon · Wed · Fri | (stamp) HOURBACK · YOUR EVENINGS BACK",
        f"[slide 2] 2/2 | Tell AI what's wrong and what you need. | It wrote this email: | SUBJECT | {C_SUBJ} | Hi Dan, | {C_P1} | "
        f"{C_P2} | Thank you, Alex Unit 4B | Claude's real email, word for word · names and dates made up for this post",
    ],
    hook_options=["16°C inside. Landlord's not fixing it?", "Heat's been off since Wednesday?", "Need the landlord to reply today?"],
    style=("Series layout 'AI, for real', cover identical to Day 11/12 (Look B big-headline pills cover, kicker badge, one "
           "drawn object bottom-left, 'new one every Mon · Wed · Fri', stamp); cut to 2 slides per the Nov 3 desk order "
           "(slide 2 = the series' indigo white-card slide carrying the real output instead of the prompt; the prompt is in "
           "the caption). Loud cover; series number and 16°C on the cover."),
    send_test=False,
    sources=[f"studio/editorial/hb-nov03-run-landlord2.txt (fresh, isolated verbatim Claude run via claude -p, {run_at('landlord2')})"],
    notes=("Fulfils Day 12's caption promise ('Day 13 is Friday at 5:45 pm'). Caption's last line promises Day 14 on Mon "
           "Nov 9 at 5:45 pm: the next studio run must build it. Gate rev (Nov 3, coordinator CD fix): the first isolated "
           "run (hb-nov03-run-landlord.txt, kept as the record, no longer used) dated the email from the run day ('my text "
           "from Monday', 'tomorrow, Wednesday, November 4'), which read as recycled on a Friday post. Re-ran once, isolated, "
           "with dates that fit the post (heat off since Wed Nov 4, texted Wed, repair by Sat Nov 7, 'Today is Friday, "
           "November 6' in the prompt) -> hb-nov03-run-landlord2.txt; slide 2, caption, alt text and beats now quote it. "
           "Earlier RUN NOTE: the first, non-isolated landlord run signed the email with the founder's real name, pulled "
           "from the account's attached claude.ai Project; it was moved out of the repo unused, the run method was "
           "isolated, and the prompt gained 'Sign it from Alex in unit 4B.'. Builder: studio/editorial/nov03_hourback_feed.py. "
           "Self-review (QG-1) fixes: save line overlapped the email card (headline shrunk, card moved up, one-line save "
           "line); cover hook 'not answering' changed to 'not fixing it'. Not yet seen by an independent reviewer (QG-5)."),
))


def main():
    OUTF.parent.mkdir(parents=True, exist_ok=True)
    for e in ENTRIES:
        for k in ("video", "cover"):
            if e.get(k):
                assert (MEDIA / e[k]).exists(), e[k]
        for im in e.get("images", []):
            assert (MEDIA / im).exists(), im
        low = json.dumps(e).lower()
        for bad in ("example", "e.g.", "hypothetical", "for illustration"):
            assert bad not in low, (e["id"], bad)
    OUTF.write_text(json.dumps(ENTRIES, indent=1, ensure_ascii=False) + "\n")
    print(OUTF, [e["id"] for e in ENTRIES])


if __name__ == "__main__":
    main()

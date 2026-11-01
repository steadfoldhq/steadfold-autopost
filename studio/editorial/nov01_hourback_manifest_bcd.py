#!/usr/bin/env python3
"""B, C, D entries for studio/editorial/nov01/hourback.json (imported by nov01_hourback_manifest.py)."""
FOLLOW = "Follow to learn one real AI trick a day."

B = dict(
    id="hb-reel-1102-toast-cue-card", account="hourback", publish_at="2026-11-02T19:00:00-05:00",
    video="studio-nov01/hourback/hb-reel-1102-toast-cue-card.mp4",
    cover="studio-nov01/hourback/hb-reel-1102-toast-cue-card-cover.jpg",
    caption=(
        "Toast tonight and you can't memorize it? Paste the whole toast into AI and ask for a 5-line cue card you can glance at.\n\n"
        "Part 2 of our toast series. (Part 1, yesterday: AI writes the toast from 3 true stories.)\n\n"
        "WHY IT WORKS: you don't forget a toast because it's long. You forget what comes next. A cue card gives you one short "
        "prompt per part, so one look tells you where you are, and you say the rest in your own words.\n\n"
        "THE REAL TEST: we pasted yesterday's made-up toast (Maya and Theo) into a new Claude (Anthropic) chat on Nov 1, 2026 "
        "and asked: \"I have to give this toast tonight and I can't memorize it. Turn it into a cue card: 5 short prompts, a few "
        "words each, that I can glance at to remember each part.\"\n"
        "Its cue card, word for word:\n"
        "1. Intro: best friend since college, week one\n"
        "2. Fire alarm, 2 a.m. → \"Making toast.\" (pause)\n"
        "3. She shows up: six-hour drive, boxes (complained a little)\n"
        "4. Theo beat her at Scrabble → genius and the one\n"
        "5. Raise glasses: showing up, Scrabble, quiet smoke detector\n"
        "And a reminder, word for word: \"If you lose it, skip straight to the glasses. Nobody will notice.\"\n\n"
        "HOW (2 minutes):\n"
        "1. Open ChatGPT, Claude or Gemini.\n"
        "2. Paste your toast or speech.\n"
        "3. Ask: \"Turn it into a cue card: 5 short prompts, a few words each, that I can glance at to remember each part.\"\n"
        "4. Copy the 5 lines onto an index card or your phone's lock screen, and practise once with only the card.\n\n"
        "THE CATCH: the cue card only works if you've said the toast out loud at least once. It reminds you; it can't speak for you.\n\n"
        "PRIVACY TIP: a toast is full of other people's stories. Use first names only and leave out anything they'd want kept private.\n\n"
        "Toast and names made up for this post.\n\n"
        "Do this: Paste your toast. Ask for 5 cues.\n\n"
        "Send this to whoever's giving a toast.\n\n"
        f"{FOLLOW}\n\n"
        "#ai #wedding #publicspeaking #claude #learnai"),
    first_comment=(
        "How we made this: one real run in Claude (Anthropic), model claude-opus-5-5, in a fresh session (Claude Code CLI print "
        "mode, no tools, no earlier chat), Nov 1 2026 14:26 UTC. The prompt pasted Part 1's full reply (studio/editorial/"
        "hb-nov01-run-toast.txt) word for word. On screen: the start of each of the 5 cues, word for word and labelled "
        "'shortened' (the full cues are in the caption), and its reminder in short (word for word in the caption). Full transcript in our public repo steadfold-autopost: "
        "studio/editorial/hb-nov01-run-cue.txt. Results vary between apps and runs. Fact check (Nov 1 2026): the only claims are "
        "the run itself, checked against the saved transcript."),
    alt_text=(
        "Illustrated Hourback Reel: an evening room with string lights, a wall clock at 7:52 labelled 'toasts at 8', and a full "
        "page titled 'My toast (all of it):' covered in lines. Words: 'Toast tonight? Can't memorize it?' Then 'paste your toast "
        "into AI. Ask for a 5-line cue card. Claude's real cue card, shortened:' The page slides away and an index card titled "
        "'Cue card' fills in, one cue at a time: '1. Intro: best friend since college. 2. Fire alarm, 2 a.m. → \"Making "
        "toast.\" 3. She shows up: six-hour drive. 4. Theo beat her at Scrabble. 5. Raise glasses.' Then 'glance, don't read. One look per part.' "
        "with a note: 'its tip, in short: Lost your place? Skip to the end: raise your glasses.' Then 'Do "
        "this: Paste your toast. Ask for 5 cues. In ChatGPT, Claude or Gemini. send this to whoever's giving a toast'. Ends: "
        "'Follow to learn one real AI trick a day.' Toast and names made up for this post."),
    beats=[
        "[0.0 s] Toast tonight? Can't memorize it? | (page) My toast (all of it): | (clock) toasts at 8 | (chip) Real Claude reply · toast and names made up for this post | (stamp) HOURBACK · YOUR EVENINGS BACK",
        "[2.2 s] paste your toast into AI | Ask for a 5-line cue card. | Claude's real cue card, shortened: | (page slides out, card slides in) Cue card",
        "[2.95-5.4 s] (cues appear one by one, 58 px) 1. Intro: best friend since college · 2. Fire alarm, 2 a.m. → “Making toast.” · 3. She shows up: six-hour drive · 4. Theo beat her at Scrabble · 5. Raise glasses",
        "[7.6 s] glance, don't read | One look per part. | (note) its tip, in short: Lost your place? Skip to the end: raise your glasses. | (cue 2 highlighted)",
        "[10.8 s] Do this: | Paste your toast. Ask for 5 cues. | In ChatGPT, Claude or Gemini. | send this to whoever's giving a toast",
        "[11.4 s to end, 3.0 s] Follow to learn one real AI trick a day.",
    ],
    hook_options=["Toast tonight? Can't memorize it?", "Don't memorize your toast. Do this.", "Speech at 8. Blank mind?"],
    duration_s=14.4,
    style=("Body: drawn occasion scene, new composition (a full page that flips into a cue card; clock at 7:52 = the deadline). "
           "Dedicated cover: compare card (original simple templates family, style 8, QUIET): '1 page to learn' vs '5 cues to "
           "glance at', cream field, stamp. Grid: after Mon 5:45 pm Day 11 (Look B, loud), before Tue 7 pm C (kinetic, loud)."),
    send_test=False,
    part2_of="hb-reel-1101-wedding-toast",
    sources=["studio/editorial/hb-nov01-run-cue.txt (fresh verbatim Claude run via claude -p, Nov 1 2026 14:26:17 UTC; input = the toast run's reply, pasted verbatim)"],
    notes=("Part 2 promised on screen and in the caption of hb-reel-1101-wedding-toast; stands alone for a stranger (its own "
           "hook, the full toast shown as a page). No trial flag. Payoff words at 2.2 s, cues land from 2.95 s. Gate rev (Nov 1): "
           "cues at 58 px (the start of each cue, labelled shortened, so 'genius and the one' is gone from screen); squashed flip and "
           "pen removed; reminder shown 'in short' (a word-for-word quote can't be reworded, so the exact line stays in the caption); "
           "chip at y 1540; round 2: text cuts in 0.08 s; 1.5 MB. Cover cues are "
           "Claude's cues cut to their first words and labelled 'Claude's real cue card, shortened'. Music hb-x-smart-bounce, "
           "-13.6 LUFS. 14.4 s. Builder: studio/editorial/nov01_hourback.py cue (+ covers)."),
)

C = dict(
    id="hb-reel-1103-guests-30-min", account="hourback", publish_at="2026-11-03T19:00:00-05:00",
    video="studio-nov01/hourback/hb-reel-1103-guests-30-min.mp4",
    cover="studio-nov01/hourback/hb-reel-1103-guests-30-min-cover.jpg",
    caption=(
        "Guests in 30 minutes and the place is a mess? List the mess and ask AI for a 30-minute plan that starts with what "
        "guests see first.\n\n"
        "WHY IT WORKS: when time is short, the order matters more than the effort. AI sorts your list by what guests notice "
        "first (the door, the couch, the table) and gives each part a few minutes, so you stop starting five jobs at once.\n\n"
        "THE REAL TEST: we made up a messy apartment and asked Claude (Anthropic) on Nov 1, 2026: \"Guests arrive in 30 minutes "
        "and my apartment is a mess: dishes in the sink, laundry on the couch, shoes and bags by the door, mail all over the "
        "table, and the bathroom hasn't been cleaned. Give me a 30-minute plan, starting with what guests will see first. Keep "
        "it short.\"\n"
        "Its plan, headings word for word: 0–5 min: Entry (first impression) · 5–10 min: Living area · 10–14 min: Table · "
        "14–21 min: Kitchen · 21–28 min: Bathroom · 28–30 min: Final touch.\n"
        "Its tip, word for word: \"Carry one empty basket or bag as you go. Anything that doesn't belong goes in it, and the "
        "basket goes into the bedroom.\"\n\n"
        "HOW (1 minute to ask):\n"
        "1. Open ChatGPT, Claude or Gemini.\n"
        "2. List the mess, room by room, in one sentence.\n"
        "3. Ask: \"Give me a 30-minute plan, starting with what guests will see first. Keep it short.\"\n"
        "4. Set a timer and follow it.\n\n"
        "THE CATCH: the plan is a good-enough pass, not a deep clean. Its plan says \"sort it later\" for the mail, so put a "
        "reminder in for tomorrow.\n\n"
        "PRIVACY TIP: describe the mess in words. You don't need to upload photos of your home.\n\n"
        "Apartment made up for this post.\n\n"
        "Do this: List the mess. Ask AI for a 30-minute plan.\n\n"
        "Send this to whoever's hosting this week.\n\n"
        f"{FOLLOW}\n\n"
        "#ai #cleaningtips #hosting #claude #learnai"),
    first_comment=(
        "How we made this: one real run in Claude (Anthropic), model claude-opus-5-5, in a fresh session (Claude Code CLI print "
        "mode, no tools, no earlier chat), Nov 1 2026 14:26 UTC. The apartment is made up for this post. On screen: the plan's "
        "6 time headings word for word, one at a time, each with one action from under that heading, word for word (cut sentences end in …) (the steps under each heading are in the transcript) and the first sentence "
        "of its tip, word for word. The countdown timer is our drawing, sped up. Full transcript in our public repo "
        "steadfold-autopost: studio/editorial/hb-nov01-run-tidy.txt. Results vary between apps and runs. Fact check (Nov 1 "
        "2026): the only claims are the run itself, checked against the saved transcript."),
    alt_text=(
        "Illustrated Hourback Reel: a periwinkle living room with a front door, shoes and a bag dropped by the door, clothes piled "
        "on the couch, envelopes all over the coffee table and a kitchen timer at 30:00. Words: 'Guests in 30 minutes?' Then 'ask "
        "AI for a 30-minute plan. Start with what guests see first. Claude's real plan, shortened:' A large card shows one "
        "step at a time, 'Step 1 of 6: 0–5 min: Entry (first impression)' through 'Step 6 of 6: 28–30 min: Final touch', while the shoes line up, the bag is lifted off the floor, the "
        "clothes fly into a basket and the mail stacks up, and the timer counts down. Then 'the one-basket trick. Don't put things away "
        "yet. Toss them in one basket.' with a note: 'its tip, word for word: Carry one empty basket or bag as you go.' Then 'Do "
        "this: List the mess. Ask AI for a 30-minute plan. In ChatGPT, Claude or Gemini.' The timer hits 0:00 and the door opens. Ends: 'Follow to learn one "
        "real AI trick a day.' Apartment made up for this post."),
    beats=[
        "[0.0 s] Guests in 30 minutes? | (drawn mess: shoes and bag by the door, clothes on the couch, mail on the table) | (timer) 30:00 | (chip) Real Claude reply · apartment made up for this post | (stamp) HOURBACK · YOUR EVENINGS BACK",
        "[2.2 s] ask AI for a 30-minute plan | Start with what guests see first. | Claude's real plan, shortened: | (step card, one step at a time while that part tidies itself; heading 58 px + one quoted action 54 px) Step 1 of 6 · 0–5 min: Entry (first impression) · “Shoes go in a neat row or into a closet.” → Step 2 of 6 · 5–10 min: Living area · “Laundry goes into a basket or bin…” → Step 3 of 6 · 10–14 min: Table · “Sweep all the mail into one pile or bag…” → Step 4 of 6 · 14–21 min: Kitchen · “Load the dishwasher, or soak the dishes…” → Step 5 of 6 · 21–28 min: Bathroom · “Wipe the sink, faucet and mirror.” → Step 6 of 6 · 28–30 min: Final touch · “Open a window or light a candle…” | (timer counts down)",
        "[7.4 s] the one-basket trick | Don't put things away yet. Toss them in one basket. | (note) its tip, word for word: Carry one empty basket or bag as you go. | (step card) Step 6 of 6 · 28–30 min: Final touch · “Open a window or light a candle…”",
        "[10.8 s] Do this: | List the mess. Ask AI for a 30-minute plan. | In ChatGPT, Claude or Gemini. | (timer) 0:00, the door opens",
        "[11.4 s to end, 3.0 s] Follow to learn one real AI trick a day.",
    ],
    hook_options=["Guests in 30 minutes?", "Doorbell in 30. Place is a mess.", "30 minutes. Where do you start?"],
    duration_s=14.4,
    style=("Body: drawn occasion scene, new composition (living room, the mess tidies itself as each plan line lands, countdown "
           "timer = the deadline). Dedicated cover: kinetic big text (style 5, LOUD): stacked giant serif 'Guests in 30 minutes?', "
           "yellow pill, a drawn 30:00 timer, a drawn laundry basket, Caveat line, stamp. Grid: after Mon 7 pm B (compare, quiet), before Wed 5:45 pm Day 12 "
           "(Look B, loud): two louds touch because the series cover is fixed loud (same as Oct 31/Nov 2). Kinetic also on the Oct 31 "
           "costume cover, 4 tiles back; the 9-tile window still holds 6 styles (editorial demo, Look B, follow the line, kinetic, "
           "sticky note, compare)."),
    send_test=False,
    sources=["studio/editorial/hb-nov01-run-tidy.txt (fresh verbatim Claude run via claude -p, Nov 1 2026 14:26:02 UTC)"],
    notes=("No trial flag. Payoff words at 2.2 s; first plan step at 2.5 s. Gate rev (Nov 1): one big step card (58 px) instead of the "
           "27 px list, no empty card or diagonal flash, follow pill on the floor (clear of the door), the tilted orange shoes that read "
           "as an arrow turned flat, chip at y 1495, cover gets a drawn laundry basket. Round 2: each step card adds one quoted action (54 px); text cuts in 0.08 s; 1.7 MB. On-screen send line dropped (it collided with the "
           "door; the send line is in the caption). Music hb-x-ta-da-funk, -13.8 LUFS. 14.4 s. Builder: studio/editorial/"
           "nov01_hourback.py tidy (+ covers)."),
)

D = dict(
    id="hb-day12-potluck", account="hourback", publish_at="2026-11-04T17:45:00-05:00",
    images=["studio-nov01/hourback/hb-day12-potluck/01.jpg", "studio-nov01/hourback/hb-day12-potluck/02.jpg",
            "studio-nov01/hourback/hb-day12-potluck/03.jpg"],
    caption=(
        "Potluck tomorrow and 3 different diets? Tell AI who can't eat what, your time and your budget, and ask for 3 dishes that "
        "work for all of them.\n\n"
        "AI, for real · Day 12. One real test of what AI can do, with the output shown.\n\n"
        "WHY IT WORKS: one rule at a time is easy; three at once is where you get stuck. AI checks every idea against all of them "
        "at the same time (no animal products, no nuts, no gluten) and against your 30 minutes and $20.\n\n"
        "THE REAL TEST (guests made up for this post):\n"
        "Prompt: \"I'm bringing a dish to a potluck tomorrow. One guest is vegan, one can't eat nuts, and one is gluten-free. I "
        "have about 30 minutes to cook and $20. Give me 3 dishes that work for all of them, one line each.\"\n"
        "Claude's 3 dishes (names word for word, with its own time and cost):\n"
        "1. Black bean & corn salad: about 15 minutes and roughly $10\n"
        "2. Coconut chickpea curry over rice: about 30 minutes and roughly $12\n"
        "3. Roasted potatoes and veggies: about 30 minutes and roughly $10\n"
        "It added, word for word: \"Check the labels on canned goods and spice blends for hidden gluten, nut or dairy "
        "ingredients.\"\n\n"
        "THE CATCH: AI can't read your labels and prices are its estimates. Some people with nut allergies also avoid coconut, so "
        "ask the guest before you make the curry (or bring the salad). For any allergy, ask what they avoid and check every label "
        "yourself. The costs don't count the oil and spices you already have.\n\n"
        "PRIVACY TIP: say \"one guest is vegan\", not who. You don't need names or health details.\n\n"
        "Do this: in ChatGPT, Claude or Gemini, type \"I'm bringing a dish to a potluck tomorrow. One guest is vegan, one can't "
        "eat nuts, and one is gluten-free. I have about 30 minutes to cook and $20. Give me 3 dishes that work for all of them, "
        "one line each.\" Change the diets, time and budget to yours.\n\n"
        "Send this to whoever's hosting the potluck.\n\n"
        "AI, for real · Day 13 is Friday at 5:45 pm.\n\n"
        f"{FOLLOW}\n\n"
        "#ai #potluck #claude #mealideas #learnai"),
    first_comment=(
        "Made-up guests, real output: run in Claude (Anthropic), model claude-opus-5-5, in a fresh session (Claude Code CLI print "
        "mode, no prior conversation, no tools), Nov 1 2026 14:26 UTC. Slide 2 shows the run's prompt word for word (yellow "
        "chips = the parts to change). Slide 3 shows the 3 dish names word for word in Claude's order; the caption adds its "
        "times and costs word for word and its label tip. Full reply (ingredients, 425°F oven, soy sauce/tamari note) in our "
        "public repo steadfold-autopost: studio/editorial/hb-nov01-run-potluck.txt. Costs are Claude's estimates, not checked "
        "against any store. Not allergy advice. Results vary between apps and runs."),
    alt_text=(
        "Hourback 3-slide carousel. Slide 1: 'AI, for real · Day 12' badge, 'Potluck tomorrow. 3 diets?' in a large serif with a "
        "periwinkle highlight, a drawn orange casserole dish with a lid and three tags: vegan, no nuts, gluten-free, and the handwritten "
        "note 'new one every Mon · Wed · Fri'. Slide 2: 'In ChatGPT, Claude or Gemini, type this about your guests:' above a "
        "white prompt card: 'I'm bringing a dish to a potluck tomorrow. One guest is vegan, one can't eat nuts, and one is "
        "gluten-free. I have about 30 minutes to cook and $20. Give me 3 dishes that work for all of them, one line each.' with "
        "potluck, vegan, can't eat nuts, gluten-free, 30 minutes and $20 in yellow chips, and 'change the yellow words to "
        "yours'. Slide 3: 'Fits all 3 diets. It wrote:' and a list: 1 Black bean & corn salad, 2 Coconut chickpea curry over "
        "rice, 3 Roasted potatoes and veggies; 'real reply, shortened', 'cooking times, costs and its tip on checking labels are in "
        "the caption'."),
    beats=[
        "[slide 1] AI, FOR REAL · DAY 12 | Potluck tomorrow. 3 diets? | (dish tags) vegan · no nuts · gluten-free | new one every Mon · Wed · Fri | (stamp) HOURBACK · YOUR EVENINGS BACK",
        "[slide 2] 2/3 | In ChatGPT, Claude or Gemini, | type this about your guests: | COPY THIS PROMPT | ⧉ copy | I'm bringing a dish to a potluck tomorrow. One guest is vegan, one can't eat nuts, and one is gluten-free. I have about 30 minutes to cook and $20. Give me 3 dishes that work for all of them, one line each. | change the yellow words to yours",
        "[slide 3] 3/3 | Fits all 3 diets. It wrote: | 1 Black bean & corn salad | 2 Coconut chickpea curry over rice | 3 Roasted potatoes and veggies | real reply, shortened | cooking times, costs and its tip on checking labels are in the caption",
    ],
    hook_options=["Potluck tomorrow. 3 diets?", "Vegan, nut-free, gluten-free. One dish?", "One dish everyone can eat?"],
    style=("Series layout 'AI, for real' identical to hb-day11-gift-for-dad (Look B big-headline pills cover with one drawn "
           "object + indigo prompt-card slide + yellow white-list-card slide); loud cover; series number on the cover."),
    send_test=False,
    sources=["studio/editorial/hb-nov01-run-potluck.txt (fresh verbatim Claude run via claude -p, Nov 1 2026 14:26:02 UTC)"],
    notes=("Day 11's caption (queued, Mon Nov 2 5:45 pm) already promises 'Day 12 is Wednesday at 5:45 pm'. This caption "
           "promises Day 13 on Friday at 5:45 pm: the next studio run must build it. Slide 3 title says 'Fits all 3 diets', "
           "not 'safe' (no allergy-safety claim); the caption's catch says some people with nut allergies avoid coconut, to ask the "
           "guest, and to check labels. Gate rev (Nov 1): 'GF' tag spelled out, 'Claude's own order' dropped, plain-word save line. Builder: "
           "studio/editorial/nov01_hourback_feed.py."),
)

ENTRIES = [B, C, D]

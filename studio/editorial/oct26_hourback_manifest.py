#!/usr/bin/env python3
"""Writes studio/editorial/oct26/hourback.json (Hourback maker, Oct 26 2026). Pure data; renders nothing.
Media: oct26_hourback.py (Reel) and oct26_hourback_feed.py (feed, Day 10, Stories)."""
import json
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
FOLLOW = "Follow to learn what AI can really do, one real test a day."
M = "studio-oct26/hourback"

RET_PROMPT = ("Here's a store's return policy. I bought a jacket on sale on Oct 12 and it arrived Oct 20. What's my last day to return it, "
              "and what will I get back? Answer in 2 short sentences.\n\nRETURNS\nUnworn items with tags can be returned within 30 days of delivery.\n"
              "Sale items: store credit only.\nA $7.99 return shipping fee is taken off your refund.")
RET_REPLY = ("Your last day to return the jacket is November 19 (30 days from the Oct 20 delivery), as long as it's unworn with tags attached. "
             "Because it was a sale item, you'll get store credit only, likely the sale price you paid minus the $7.99 return shipping fee.")

MECH_PROMPT = "My car makes a squeal when I brake. Give me 5 short questions to ask the mechanic so I understand the quote before I say yes."
MECH_QS = ["What exactly is causing the squeal?",
           "How much pad life is left, and is this urgent or can it wait?",
           "Do the rotors really need replacing, or can they be resurfaced or reused?",
           "Can you break the quote into parts and labour, and what grade of parts is that?",
           "What warranty comes with the parts and the work, and what if it still squeals afterward?"]

entries = []

# ------------------------------------------------------------------ 1. Reel, Tue 8:45 am, NO trial
entries.append(dict(
    id="hb-reel-1027am-return-by", account="hourback", publish_at="2026-10-27T08:45:00-04:00",
    video=f"{M}/hb-reel-1027am-return-by.mp4", cover=f"{M}/hb-reel-1027am-return-by-cover.jpg",
    caption=("Returning something? Paste the store's return policy into AI and ask for your last day.\n\n"
             "WHY IT WORKS: the AI answers from the policy you paste, not from a guess. Add the day you bought it and the day it arrived, "
             "and it does the date maths and points out the catches, like sale items.\n\n"
             "THE REAL TEST (policy and dates made up for this post):\n"
             "We pasted a 3-line return policy (30 days from delivery, sale items store credit only, $7.99 return fee) and asked: "
             "\"I bought a jacket on sale on Oct 12 and it arrived Oct 20. What's my last day to return it, and what will I get back?\"\n"
             f"Claude's reply, word for word: \"{RET_REPLY}\"\n"
             "We checked the maths: Oct 20 plus 30 days is Nov 19.\n\n"
             "THE CATCH: the answer is only as good as what you paste. Copy the whole returns section from the store's site or receipt, "
             "and check the date against the policy before you count on it.\n\n"
             "PRIVACY TIP: you don't need your order number, name or address. The policy and two dates are enough.\n\n"
             "Do this: paste the return policy into ChatGPT, Claude or Gemini and ask, \"What's my last day to return it?\"\n\n"
             f"{FOLLOW}\n\n#ai #chatgpt #claude #aitips #shoppingtips"),
    first_comment=("Made-up policy and dates, real output: run in Claude (Anthropic), model claude-opus-5-5, in a fresh session with no other context "
                   "and no tools, Oct 26, 2026 13:56 UTC. Full prompt and reply saved in the Steadfold repo at "
                   "studio/editorial/hb-oct26-run-return-policy.txt. The reply is quoted exactly (its bold formatting removed); the Reel shows "
                   "the first sentence and the words \"store credit only\". The chat screen in the Reel is drawn. Results vary between apps and runs."),
    alt_text=("Hourback Reel. Frame 0: 'Returning it? Paste the policy.' in a large serif over a drawn chat app with a pasted return policy "
              "(30 days from delivery, sale items store credit only, $7.99 return fee) and the question 'Bought it on sale Oct 12. It arrived Oct 20. "
              "Last day to return it?'. Then 'Last day: Nov 19.' with Claude's reply quoted, a 'Sale item: store credit only' pill, "
              "a 'Do this' card and the follow line."),
    beats=["0.0 s (frame 0): Returning it? Paste the policy. | drawn chat screen: New chat | RETURNS · Unworn items with tags: 30 days from delivery. "
           "Sale items: store credit only. $7.99 return fee. | Bought it on sale Oct 12. It arrived Oct 20. Last day to return it? | Message | (0.3 s) typing dots pop | "
           "(stamp: HOURBACK · YOUR EVENINGS BACK)",
           "1.5 s: Last day: Nov 19. | CLAUDE'S REAL REPLY, WORD FOR WORD | Your last day to return the jacket is November 19 (30 days from the Oct 20 delivery), "
           "as long as it's unworn with tags attached. | (3.3 s) Sale item: store credit only | Policy and dates made up for this post.",
           "5.0 s: Do this: | Paste the policy. Ask: last day? | (6.0 s) Add the day you bought it and the day it arrived. | "
           "(6.9 s) Leave out your order number and address. | (7.3 s) Works in ChatGPT, Claude or Gemini.",
           "8.9 s: Follow to learn what AI can really do. | (9.4 s) one real test a day | (stamp)",
           "11.8 s: loop to the frame-0 hook (Returning it? Paste the policy. | chat screen)"],
    hook_options=["Returning it? Paste the policy.", "Return by when? Ask AI.", "Sale item? AI reads the fine print."],
    duration_s=12.6,
    style=("Dedicated cover = Kinetic big text (style 5 look: stacked giant serif, one pill, hand-drawn ring, Caveat line, stamp), loud, periwinkle. "
           "Chosen because the neighbouring HB tiles (Mon 7 pm photo eraser, Tue 7 pm homework hints, Wed hum, Thu bill) are all 'editorial demo' "
           "covers with a drawn object; this one has no object on the cover. Video = editorial §12 look, Take-Two kit recut."),
    send_test=False,
    sources=["studio/editorial/hb-oct26-run-return-policy.txt (fresh Claude run, Oct 26 2026 13:56 UTC)"],
    music="media/music/library/v4/hb-x-future-easy.mp3 (existing HB track, tools/music-library.json); mix measured -14.6 LUFS, -1.7 dBTP",
    notes=("NO trial flag (Performance desk order 4: HB morning Reels non-trial, action shown in frame 0). Frame 0 = one hook line (5 words) + one object "
           "(the chat screen showing the action: policy pasted, question asked). Payoff 'Last day: Nov 19.' on screen at 1.5 s. Rule/date in the first "
           "line per order 1. H.264 1080x1920 30 fps, AAC, 7.2 MB, 12.6 s (ffprobe). Strip + cover reviewed; frame 0 overlap of phone and hook fixed "
           "before the final encode. Not a send test (no on-screen send ask; no caption send line, per order 5).")))

# ------------------------------------------------------------------ 2. Feed post, Tue 12:00
qs = "\n".join(f"{i}. \"{q}\"" for i, q in enumerate(MECH_QS, 1))
entries.append(dict(
    id="hb-1027-mechanic-questions", account="hourback", publish_at="2026-10-27T12:00:00-04:00",
    images=[f"{M}/hb-1027-mechanic-questions/0{i}.jpg" for i in (1, 2, 3)],
    caption=("Before you say yes to the mechanic, ask AI for the questions to ask.\n\n"
             "WHY IT WORKS: you can't push back on a quote you don't understand. AI turns \"it makes a noise\" into the questions a mechanic "
             "should be able to answer: what's wrong, how urgent it is, and where the money goes.\n\n"
             "THE PROMPT (swap the parts in brackets for yours):\n"
             "\"My [car] makes [a squeal when I brake]. Give me 5 short questions to ask the [mechanic] so I understand the quote before I say yes.\"\n\n"
             "THE REAL TEST (the car and the squeal are made up for this post). Claude's 5 questions, word for word "
             "(it also explained each one; that part is left out for length):\n" + qs + "\n\n"
             "THE CATCH: AI doesn't know your car or your shop. Use the questions to understand the quote, not to diagnose the problem yourself.\n\n"
             "PRIVACY TIP: no plate number, VIN or address needed. \"My car\" is enough.\n\n"
             "Do this: before you call the shop, paste the prompt into ChatGPT, Claude or Gemini with your car and the noise.\n\n"
             f"{FOLLOW}\n\n#ai #chatgpt #claude #aitips #carrepair"),
    first_comment=("Made-up situation, real output: run in Claude (Anthropic), model claude-opus-5-5, in a fresh session with no other context and no tools, "
                   "Oct 26, 2026 13:56 UTC. Full prompt and reply saved in the Steadfold repo at studio/editorial/hb-oct26-run-mechanic-questions.txt. "
                   "Slide 2 shows questions 1 and 4 word for word; the caption lists all 5 (bold formatting removed; the explanation under each is left out). "
                   "Results vary between apps and runs."),
    alt_text=("Hourback 3-slide carousel. Slide 1: 'Before you say yes to the mechanic' in a large serif, and a white prompt card labelled 'Copy this prompt': "
              "'My [car] makes [a squeal when I brake]. Give me 5 short questions to ask the [mechanic] so I understand the quote before I say yes.' "
              "with the bracket words on yellow chips, and the note 'change the yellow words to yours'. Slide 2: 'It wrote 5. Here are 2:' with "
              "Claude's questions 1 ('What exactly is causing the squeal?') and 4 ('Can you break the quote into parts and labour, and what grade of parts is that?'). "
              "Slide 3: 'Do this: Paste it into ChatGPT, Claude or Gemini before you call the shop.' and 'No plate number or VIN needed. My car is enough.'"),
    beats=["Slide 1: Before you say yes to the mechanic | COPY THIS PROMPT | copy | My [car] makes [a squeal when I brake]. Give me 5 short questions to ask the [mechanic] "
           "so I understand the quote before I say yes. | change the yellow words to yours | swipe → | (stamp)",
           "Slide 2: 2/3 | It wrote 5. Here are 2: | CLAUDE'S REPLY, WORD FOR WORD · QUESTIONS 1 AND 4 | 1 “What exactly is causing the squeal?” | "
           "4 “Can you break the quote into parts and labour, and what grade of parts is that?” | all 5 are in the caption | (stamp)",
           "Slide 3: 3/3 | Do this: | Paste it into ChatGPT, Claude or Gemini | before you call the shop. | No plate number or VIN needed. “My car” is enough. | (stamp)"],
    hook_options=["Before you say yes to the mechanic", "Car quote? Ask AI first.", "5 questions your mechanic should answer"],
    style=("Prompt card with yellow [bracket] chips (Hourback signature object; quiet). Sits between the loud kinetic-big-text Reel cover at 8:45 "
           "and the loud editorial-demo homework cover at 7 pm, so loud/quiet alternates and no style repeats."),
    send_test=False,
    sources=["studio/editorial/hb-oct26-run-mechanic-questions.txt (fresh Claude run, Oct 26 2026 13:56 UTC)"],
    notes=("3 slides (desk order 4: 1-3). Fills the empty HB Tue feed slot. Questions quoted exactly; Claude's other claims in the reply "
           "(pad thickness etc.) are NOT used anywhere, so nothing needs a separate fact check. Gate fixes Oct 26: cover hook swapped to the stranger pick \"Before you say yes to the mechanic\" (fits cleanly at 3 lines, ~170 px serif); slide 3 stamp moved off the yellow box.")))

# ------------------------------------------------------------------ 3. AI, for real · Day 10, Fri 5:45 pm
entries.append(dict(
    id="hb-day10-pancakes-for-6", account="hourback", publish_at="2026-10-30T17:45:00-04:00",
    images=[f"{M}/hb-day10-pancakes-for-6/0{i}.jpg" for i in (1, 2, 3)],
    caption=("Recipe for 4 and six are coming? Paste the ingredient list and ask AI to rewrite it for 6.\n\n"
             "AI, for real · Day 10. One real test of what AI can do, with the output shown.\n\n"
             "WHY IT WORKS: scaling is multiplying every line by the same number (here 1.5), and the fiddly part is turning the answers back into "
             "cups and spoons you can measure. AI does both and keeps the list in the same order, so you can cook straight from it.\n\n"
             "THE REAL TEST (the recipe is made up for this post):\n"
             "Prompt: \"This pancake recipe serves 4. Rewrite the ingredient list for 6 people. Just the list.\" Then the list: 1 1/2 cups flour, "
             "2 tbsp sugar, 2 tsp baking powder, 1/2 tsp salt, 1 1/4 cups milk, 1 egg, 3 tbsp melted butter.\n"
             "Claude's reply, word for word: 2 1/4 cups flour · 3 tbsp sugar · 1 tbsp baking powder · 3/4 tsp salt · 1 3/4 cups + 2 tbsp milk · "
             "1 1/2 eggs (or 1 egg plus 1 yolk) · 4 1/2 tbsp melted butter.\n"
             "We checked every line: all 7 are exactly 1.5 times the original (2 tsp × 1.5 = 3 tsp = 1 tbsp; 1 1/4 cups × 1.5 = 1 7/8 cups = 1 3/4 cups + 2 tbsp).\n\n"
             "THE CATCH: the ingredients are the easy part. Pan size and cooking time don't simply multiply, so check those yourself.\n\n"
             "PRIVACY TIP: a recipe is safe to paste. Skip anything personal, like a family name on a recipe card.\n\n"
             "TIP: if you don't own a 1/8 cup or odd spoons, add \"Round to cups and spoons I own\" to the prompt.\n\n"
             "Do this: next time you cook for more people, in ChatGPT, Claude or Gemini type \"This pancake recipe serves 4. Rewrite the ingredient list "
             "for 6 people. Just the list.\" (change the recipe and the numbers to yours), then paste the recipe under it.\n\n"
             "AI, for real · Day 11 is Monday at 5:45 pm.\n\n"
             f"{FOLLOW}\n\n#ai #chatgpt #claude #aitips #learnai"),
    first_comment=("Made-up recipe, real output: run in Claude (Anthropic), model claude-opus-5-5, in a fresh session (Claude Code CLI print mode, "
                   "no prior conversation, no tools), Oct 25, 2026 13:39 UTC. Prompt and full reply saved in the Steadfold repo at "
                   "studio/editorial/hb-oct25-run-day9.txt. Slide 3 shows 3 of the 7 lines word for word; the caption lists all 7. "
                   "Slide 2 now shows the run's prompt word for word in the copy card. The 'round to cups and spoons I own' tip was not part of the run. "
                   "Results vary between apps and runs."),
    alt_text=("Hourback 3-slide carousel. Slide 1: 'AI, for real · Day 10' badge, 'Recipe for 4. Six are coming?' in a large serif with highlighted words, "
              "a drawn stack of pancakes with butter and syrup, and the handwritten note 'new one every Mon · Wed · Fri'. Slide 2: 'In ChatGPT, Claude or Gemini, "
              "type this above any recipe:' and a white 'Copy this prompt' card: '[This pancake recipe] serves [4]. Rewrite the ingredient list for [6] people. "
              "Just the list.' with the bracket words on yellow chips, and the note 'tip: add round to cups and spoons I own'. Slide 3: 'Pancakes for 6. It wrote:' "
              "1. 2¼ cups flour, 2. 1¾ cups + 2 tbsp milk, 3. 1½ eggs (or 1 egg plus 1 yolk); notes 'real reply, shortened' and "
              "'3 of 7 shown, all 7 in the caption, we checked every one'."),
    beats=["Slide 1: AI, FOR REAL · DAY 10 | Recipe for 4. Six are coming? | (drawn pancake stack) | new one every Mon · Wed · Fri | (stamp)",
           "Slide 2: 2/3 | In ChatGPT, Claude or Gemini, | type this above any recipe: | COPY THIS PROMPT | copy | "
           "[This pancake recipe] serves [4]. Rewrite the ingredient list for [6] people. Just the list. | tip: add “round to cups and spoons I own” | (stamp)",
           "Slide 3: 3/3 | Pancakes for 6. It wrote: | 1 2¼ cups flour | 2 1¾ cups + 2 tbsp milk | 3 1½ eggs (or 1 egg plus 1 yolk) | "
           "real reply, shortened | 3 of 7 shown, all 7 in the caption, we checked every one | (stamp)"],
    hook_options=["Recipe for 4. Six are coming?", "Cooking for 6? AI scales it.", "Pancakes for 6, no maths"],
    style=("Series layout (Look B big-headline pills cover + indigo line slide + white list card), identical to hb-day8-ask-me-first / hb-day9-kind-firm-no. "
           "Loud; follows Thu 7 pm bill Reel (editorial demo cover)."),
    send_test=False,
    sources=["studio/editorial/hb-oct25-run-day9.txt (fresh, verbatim Claude run via claude -p, Oct 25 2026 13:39 UTC)"],
    notes=("Relabel of the parked media/studio-oct25/hourback/hb-day9-pancakes-for-6 (Day 9 went to kind-firm-no). Transcript checked: the reply was from a "
           "fresh session run on the verbatim prompt, so no re-run was needed (that transcript's header still says 'Used in: hb-day9-pancakes-for-6'; "
           "same post, renamed). Changes: kicker Day 9 -> Day 10; save-line now 'new one every Mon · Wed · Fri' as on Day 8/9; slide 2 re-lettered "
           "from 'Rewrite this recipe for 6 people.' to 'Serves 4. Rewrite it for 6 people.' to sit closer to the real prompt (no quote marks, since it "
           "is not verbatim). Gate fixes Oct 26: drawn pancake stack replaces the chat bubbles on the cover; slide 2 is now the copy-prompt card with yellow [bracket] chips holding the run's exact prompt, under \"In ChatGPT, Claude or Gemini, type this above any recipe:\"; added the tip line; slide 3 note now says 3 of 7 shown. All 7 scaled lines re-checked by hand. Caption says Day 11 is Monday 5:45 pm: the Mon/Wed/Fri cadence assumes the "
           "next maker fills it.")))

# ------------------------------------------------------------------ 4. Stories Tue-Thu, 12:30 + 12:31
ST = [
    ("hb-st-1027-1", "2026-10-27T12:30:00-04:00", ["quick question", "Car repair quote? Ask before you say yes.", "AI can write the questions for you.", "tap for the answer →"]),
    ("hb-st-1027-2", "2026-10-27T12:31:00-04:00", ["the answer", "“What exactly is causing the squeal?”", "1 of the 5 questions Claude wrote for us.",
                                                  "All 5 + the prompt to copy: today's post on our page"]),
    ("hb-st-1028-1", "2026-10-28T12:30:00-04:00", ["quick question", "Google can name a song you only hum?", "tap for the answer →"]),
    ("hb-st-1028-2", "2026-10-28T12:31:00-04:00", ["the answer", "Google app → mic → Search a song.", "Then hum, whistle or sing the tune.",
                                                  "Tonight at 7 pm: a 15-second Reel on our page"]),
    ("hb-st-1029-1", "2026-10-29T12:30:00-04:00", ["quick question", "Bill went up? AI can tell you why.", "tap for the answer →"]),
    ("hb-st-1029-2", "2026-10-29T12:31:00-04:00", ["the answer", "Paste last month's and this month's bill into ChatGPT, Claude or Gemini. Ask: what changed?",
                                                  "Cover your account number and address first.", "Tonight at 7 pm: a 15-second Reel on our page"]),
]
for sid, at, beats in ST:
    entries.append(dict(id=sid, account="hourback", publish_at=at, story=True, image=f"{M}/stories/{sid}.jpg",
                        caption=f"Story {sid}: " + " | ".join(beats), beats=beats + ["(stamp: HOURBACK · YOUR EVENINGS BACK)"]))

out = REPO / "studio/editorial/oct26/hourback.json"
out.write_text(json.dumps(entries, indent=1, ensure_ascii=False) + "\n")
print(out, len(entries))

"""Writes the Nov 4 2026 per-page maker briefs (studio/editorial/nov04/BRIEF-<page>.md)."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
b = open('nov03/BRIEF-littlefold.md').read()
std = b[b.index('## THE STANDARD'):].replace('nov03', 'nov04').replace('Nov 3 2026', 'Nov 4 2026')

head = '''# Social studio, Wed Nov 4 2026: page build brief

You are the maker for ONE Steadfold Instagram page. Repo: /home/claude/steadfold-autopost (on main; do NOT git pull/commit/push, do NOT edit schedule/posts.json, never touch state/, keys/ or tokens). Studio engine already extracted to /home/claude/content (fonts + photos installed). The machine has only 2 CPUs / 7 GB RAM and 3 other makers render at the same time: render with 1 worker, one Reel at a time, and delete frame folders right after each encode (disk is limited). Use ffmpeg with -nostdin. Scratch dir: /tmp/claude-0/nov04-<page>/.

Clocks are EST (-05:00). Use "-05:00" in every publish_at.

**Budget:** do the jobs in the order listed. Write each manifest entry as soon as that piece is clean. Target: everything within ~4 h. If you run short, cut the LAST job rather than ship weak work; say why.

## Read first (they win over this brief)
- CLAUDE.md, docs/north-star.md (Founder lines win; your page's section + "All four live pages"), docs/brand-system-v4.md (addendum + your page's section), the top of docs/metrics.md (TEST-BATCH TABLE + "Today's orders", Wed Nov 4).
- The previous builds you EXTEND (copy into your own new script; don't edit shared kits or older scripts): Reels: studio/editorial/nov03_<page>*.py + studio/editorial/nov03/<page>.json + studio/editorial/nov03/BRIEF-<page>.md. Series tile: studio/editorial/nov03_<page>_feed.py (or nov03_<page>.py) + its entry in studio/editorial/nov03/<page>.json (the Fri Nov 6 episode).
- Recent topics on your page (no repeats from the last ~14 days): insights/latest.json `first_line`, queued items in schedule/posts.json for your account, and the nov01/nov02/nov03 manifests.

## What the data says (Performance desk, Nov 4; apply it)
1. **REPEAT the number in frame 0: it is the HOLD lever.** LF "Babies can drown in 5 cm of water" now 198 reach at 7.06 s / 49%; LH "24 minutes on, 6 off" 111 reach, 5.12 s / 35%, 2 saves; grapes 4 / rice grain / 90 min all held 46-53%. Opens without a number held 25-38%. Keep every Reel standalone (no Part 1/Part 2, no callbacks).
2. **SENDS are the missing expansion signal** (4 clean sends on ~3,400 Reel reach since Nov 1). Today we TEST an on-screen send beat: ONE line in the last ~2 s naming the person to send it to ("Send this to whoever does bath time."), together with the follow line. Only on the Reels named below as the send test; every other Reel stays as is so the test is clean.
3. **Batches come late too** (LH lamp 152 -> 323, HB cue card 14 -> 101 after 13 h). Nothing to change; don't read 5 h numbers as failure.
4. **HB: the batch now comes, the hold doesn't.** Panic-scene opens fail ("Guests in 30 minutes" 9 reach, 1.05 s; cue card 3.65 s). The wedding toast held 5.41 s because the page of AI text was visible by second 1. **Frame 0 shows the real AI output itself** (the note, the list, the email), with the deadline hook on top.
5. **FF: HOLD.** Account-level distribution problem suspected (2-33 reach whatever the topic). No topic or format change; keep Canadian partner/family rules, a felt moment + a number in frame 0, drawn style. No extra volume.
6. Follow lines (last beat, on screen >=1.5 s): LF "Follow for one calm thing a night, from bump to toddler."; LH "Follow for one small sleep or focus trick a day."; FF "Follow for one money rule a day, in plain words."; HB "Follow to learn one real AI trick a day."

## YOUR JOB TODAY (quality over count; cut a piece rather than ship filler, and say why)
'''

jobs = {
 'littlefold': '''1. **D) SEND TEST, quick (do first):** `lf-reel-1106-highchair-5-straps` (Fri Nov 6 19:00; built by studio/editorial/nov03_littlefold.py; media/studio-nov03/littlefold/). Add ONE on-screen send line to the end beat, e.g. "Send this to whoever feeds them lunch." (or better; plain, names the person), shown with the follow line for the last ~2 s. Total must stay <=15.0 s. Everything else identical. Overwrite the same mp4 (cover unchanged). Write the full entry (copied from nov03/littlefold.json, beats updated, `"send_test": true`, `"replaces_existing": true`) into your nov04 manifest. Look at the strip.
2. **A) Sun Nov 8 19:00 Reel** (no trial). Id `lf-reel-1108-<slug>`. Standalone, number in frame 0. No send line (control).
3. **C) Mon Nov 9 17:00 series: `lf-3amclub-07` "3 am Club No. 7"** (promised in Friday's caption). 2 slides, SAME cover layout as No. 6, number on the cover, cover hook <=8 words naming a 3 am moment. Caption last line: next episode lands Wed Nov 11 at 5 pm.
4. **B) Mon Nov 9 19:00 Reel** (no trial). Id `lf-reel-1109-<slug>`. Standalone, number in frame 0, different topic family from A. No send line.
''',
 'lockedhour': '''1. **D) SEND TEST, quick (do first):** `lh-reel-1106-mix-3-kinds` (Fri Nov 6 19:00; studio/editorial/nov03_lockedhour.py; media/studio-nov03/lockedhour/). Add ONE on-screen send line to the end beat, e.g. "Send this to someone with a maths test this week." (or better; plain, names the person), shown with the follow line for the last ~2 s. Total must stay <=15.0 s (tighten elsewhere if needed). Overwrite the same mp4 (cover unchanged). Full entry into your nov04 manifest with `"send_test": true`, `"replaces_existing": true`. Look at the strip.
2. **A) Sun Nov 8 19:00 Reel** (no trial). Id `lh-reel-1108-<slug>`. Standalone, number in frame 0. No send line.
3. **C) Mon Nov 9 17:00 series: `lh-oneword-08` "One Word No. 8"** (promised). 2 slides, SAME layout as No. 7, number on the cover, cover hook <=8 words. Caption last line: next episode lands Wed Nov 11 at 5 pm.
4. **B) Mon Nov 9 19:00 Reel** (no trial). Id `lh-reel-1109-<slug>`. Standalone, number in frame 0, different topic family from A. No send line.
''',
 'fullyfunded': '''(No send-test edit: FF's queued Thu/Fri/Sat Reels already end on "Send this to your parents / your partner / a new parent.")
1. **A) Sun Nov 8 19:00 Reel** (no trial). Id `ff-reel-1108-<slug>`. Standalone, number in frame 0, "Canada" on screen.
2. **C) Mon Nov 9 17:00 series: `ff-richhabits-07` "Rich Habits, Decoded No. 7"** (promised). 2 slides, SAME layout as No. 6, number on the cover, hook <=8 words naming a money moment. Caption last line: next episode lands Wed Nov 11 at 5 pm.
3. **B) Mon Nov 9 19:00 Reel** (no trial). Id `ff-reel-1109-<slug>`. Standalone, number in frame 0, different topic family from A.
''',
 'hourback': '''1. **D1) URGENT, do first, hard deadline 22:00 UTC today:** `hb-reel-1105-flight-6am` (Thu Nov 5 19:00; studio/editorial/nov02_hourback.py; media/studio-nov02/hourback/). Desk order 4: frame 0 must SHOW the real AI output (Claude's packing list, from studio/editorial/hb-nov02-run-packing.txt, quoted exactly, "shortened" where cut) under the hook "Flight at 6 am. Not packed.", not just the boarding pass. Keep the length <=15.0 s and the rest of the story. Overwrite the same mp4 (and the cover only if needed). Full entry into your nov04 manifest with `"replaces_existing": true`. As soon as it is clean, send a message/finish note saying "D1 READY" in the manifest notes; it must ship before 00:00 UTC. If you can't make it clean by 22:00 UTC, leave the original untouched and say so.
2. **D2) SEND TEST + output in frame 0:** `hb-reel-1106-thank-you-20` (Fri Nov 6 19:00; nov03_hourback.py; media/studio-nov03/hourback/). Frame 0 shows a real note from studio/editorial/hb-nov03-run-thanks.txt (word for word) under the hook; end beat adds ONE send line, e.g. "Send this to whoever just had a baby shower." with the follow line for the last ~2 s. <=15.0 s. Entry with `"send_test": true`, `"replaces_existing": true`.
3. **A) Sun Nov 8 19:00 Reel** (no trial). Id `hb-reel-1108-<slug>`. Deadline hook with a number (<=6 words) AND the real output visible in frame 0. No send line.
4. **C) Mon Nov 9 17:45 series: `hb-day14-<slug>` "AI, for real · Day 14"** (promised). 2 slides, SAME layout as Day 13, real run. Caption last line: Day 15 lands Wed Nov 11 at 5:45 pm.
5. **B) Mon Nov 9 19:00 Reel** (no trial). Id `hb-reel-1109-<slug>`. As A, different occasion family. No send line.
- **Real runs:** use the ISOLATED method in studio/editorial/nov03_hourback_run.py (empty folder, no setting sources, Project env vars removed). Never the plain `claude -p` call (it loads the claude.ai Project instructions and leaked the founder's name in a test on Nov 3). Save each transcript to studio/editorial/hb-nov04-run-<slug>.txt; scan it for any real personal name/employer before using it; quote exactly; label "shortened".
''',
}

page = {
 'littlefold': '- **LITTLEFOLD:** illustrated physical-rule format (sunny, warm, never gloomy), hook carries a picture-able size/amount/number (<=8 words). Official sources only. New topics only (NOT: grapes/round foods, sausage, nuts, 5 cm water/bath, toothpaste, burp, nails, bath elbow, swaddle, cord, neck check, tummy time, coat/car seat, honey, batteries, medicine mL, vitamin D, sleep position, gums, crying, hot drink, hand on baby, fever, vomiting, contact naps, 3 am play, high chair straps, hot tap 49°C, formula water 70°C). Candidates to verify on the official page using its own number: furniture/TV tip-over (anchor it), blind cords (keep cords out of reach / cleats), magnets, small-object choking size (toilet-roll tube if an official source says it), window opening limits, stair gates top and bottom, pot handles turned in, bottle-fed amounts by age, room temperature 16-20°C for sleep (Lullaby Trust), sun/sunscreen under 6 months, bath seat not a safety device. 3 am Club = a 3 am moment with one calm, official rule (not formula water, fever, vomiting, play, contact naps).',
 'lockedhour': '- **LOCKED HOUR:** "do this tonight/now" action with a number you can do, on ONE drawn object in the zine scene (warm shower = the model, 1,079 reach / 7 saves). Real peer-reviewed research cited exactly in caption/first_comment, never a study-claim open, and only findings that have held up (skip anything with failed replications). Avoid recent topics (shower before bed, lamp/ceiling light, break timer 24/6, get up after 20 min, slow sighs, workout 1 h, snooze, mix 3 kinds, calm music 45 min, doodle, head start, rereading, close eyes, grey phone, temptations, picture the win, new place, nap, batch, spacing, lyrics, planning fallacy, when-where, task switching, daydream, bedtime to-do, walk, write from memory, print it). Ideas to verify: caffeine cutoff hours before bed (Drake 2013: 400 mg 6 h before bed still cut sleep), bedroom temperature, 10-minute walk after a meal, phone in another room (Ward 2017; check replication status), morning light soon after waking, 2-minute rule for starting, retrieval practice with flashcards.',
 'fullyfunded': '- **FULLY FUNDED:** Canadian partner/family rules, felt moment + a number on frame 0, "Canada" on screen, drawn style, ONE drawn object doing the meaning (no pointing hand, piggy bank, table, penalty-fact opens, US). Avoid repeats (common-law, both file/CCB, POA, will, TFSA beneficiary/re-contribution, FHSA room, co-sign, late payment, promo end date, rule of 72, RESP grant SIN, pension splitting, Home Buyers Plan, Canada Learning Bond, CPP timing, EI). Candidates to verify on canada.ca: spousal RRSP 3-year attribution rule, RRSP rollover to a spouse at death (vs estate), TFSA successor holder, Canada caregiver credit, child care expense deduction (lower-income spouse claims), medical expenses claimed on one return for the family, the disability tax credit transfer to a supporting spouse/parent, Canada Child Benefit when separating (tell CRA by the end of the following month). Rich Habits = one money habit with a moment (not "sleep on it 24 h", money date, lunch, insurance divide, rent before payday).',
 'hourback': '- **HOURBACK:** drawn occasion scene, hook = a deadline you can feel with a number in <=6 words, the REAL AI output visible from frame 0. Real runs only (isolated method). Avoid recent topics (toast, cue card, guests 30 min/tidy, potluck, gift for dad, costume, office card, interview, packing, thank-you notes, 5 dinners, landlord heat email, pancakes, return policy, menu, hum, bill, group chat, recipe scaling, mechanic, homework, photo eraser, fridge dinner, kind-firm no). Ideas: a 2-minute retirement speech for a coworker, school permission form/reply due tomorrow, flight cancelled rebooking message, a birthday message in another language for a grandparent, a 1-page resume summary before a 5 pm deadline, a babysitter note for tonight, a 3-day trip itinerary, an apology text after missing a friend\'s event.',
}

os.makedirs('nov04', exist_ok=True)
for p in page:
    open(f'nov04/BRIEF-{p}.md', 'w').write(head + jobs[p] + '\nPage-specific direction:\n' + page[p] + '\n\n' + std)
print('ok')

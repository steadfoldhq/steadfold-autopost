"""Writes the Nov 5 2026 per-page maker briefs (studio/editorial/nov05/BRIEF-<page>.md)."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
b = open('nov04/BRIEF-littlefold.md').read()
std = b[b.index('## THE STANDARD'):].replace('nov04', 'nov05').replace('Nov 4 2026', 'Nov 5 2026')

head = '''# Social studio, Thu Nov 5 2026: page build brief

You are the maker for ONE Steadfold Instagram page. Repo: /home/claude/steadfold-autopost (on main; do NOT git pull/commit/push, do NOT edit schedule/posts.json, never touch state/, keys/ or tokens). Studio engine already extracted to /home/claude/content (fonts + photos installed; selftest passed). The machine has only 2 CPUs / 7 GB RAM and 3 other makers render at the same time: render with 1 worker, one Reel at a time, and delete frame folders right after each encode (disk is limited). Use ffmpeg with -nostdin. Scratch dir: /tmp/claude-0/nov05-<page>/. export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers.

Clocks are EST (-05:00). Use "-05:00" in every publish_at.

**Budget:** 2 pieces only today (the Performance desk says the queue is fine and feed effort should go DOWN). Do them in the order listed. Write the manifest entry as soon as each piece is clean. Target: both within ~2.5 h. If you run short, cut rather than ship weak work; say why.

## Read first (they win over this brief)
- CLAUDE.md, docs/north-star.md (Founder lines win; your page's section + "All four live pages"), docs/brand-system-v4.md (addendum + your page's section), the top of docs/metrics.md (TEST-BATCH TABLE + "Today's orders", Thu Nov 5).
- The previous builds you EXTEND (copy into your own new script; don't edit shared kits or older scripts): Reels: studio/editorial/nov04_<page>*.py + studio/editorial/nov04/<page>.json + nov04/BRIEF-<page>.md. Series tile: studio/editorial/nov04_<page>_feed.py (or the nov04 script that built it) + its entry in nov04/<page>.json (the Mon Nov 9 episode).
- Recent topics on your page (no repeats from the last ~14 days): insights/latest.json `first_line`, queued items in schedule/posts.json for your account, and the nov01-nov04 manifests.

## What the data says (Performance desk, Nov 5; apply it)
1. **ONE picture + ONE number in frame 0, at most 2 text blocks.** LF "5 cm of water" 215 reach at 7.18 s / 50%; grapes cut into 4: 1,330 at 7.25 s; HB "Guests in 30 min" (mess on the sofa + a 30:00 timer) 110 at 7.65 s / 53%. LF coin battery opened on 4 text blocks: 3.76 s / 33%. Safety or detail lines come in from second 2, not frame 0.
2. **Never open on an empty or "?" box.** HB "Interview at 9 am" frame 0 showed an empty "Their questions: ?" card: 1.88 s / 13%. HB frame 0 shows the filled real AI output (or a picture + number), with the deadline hook on top.
3. **Batches arrive 13-29 h late** (guests 2 -> 110, lamp 152 -> 323). Nothing to change; standalone Reels only (no Part 1/Part 2).
4. **Feed series tiles reach 0-3 and 0 follows.** Keep the promised episode, 2 slides, same layout, number visible; don't spend extra effort beyond that.
5. **Template sameness (CD, Nov 4):** the last LF Reels shared one scene template, LH another, and 3 covers across pages used the taped lined-note design. Today's Reel must use a DIFFERENT scene composition from your page's last 3 Reels and a cover style different from the previous 2 covers on your grid (no taped lined-note cover today).
6. No on-screen send line today (the Fri test must stay clean). One caption send line is fine.
7. Follow lines (last beat, on screen >=1.5 s): LF "Follow for one calm thing a night, from bump to toddler."; LH "Follow for one small sleep or focus trick a day."; FF "Follow for one money rule a day, in plain words."; HB "Follow to learn one real AI trick a day."

## YOUR JOB TODAY (quality over count)
'''

jobs = {
 'littlefold': '''1. **A) Tue Nov 10 19:00 Reel** (no trial). Id `lf-reel-1110-<slug>`. Standalone; ONE drawn object + ONE number in frame 0 (<=2 text blocks); new scene composition.
2. **C) Wed Nov 11 17:00 series: `lf-3amclub-08` "3 am Club No. 8"** (promised in Monday's caption). 2 slides, SAME cover layout as No. 7, number on the cover, cover hook <=8 words naming a 3 am moment. Caption last line: "3 am Club No. 9 lands Fri Nov 13 at 5 pm."
''',
 'lockedhour': '''1. **A) Tue Nov 10 19:00 Reel** (no trial). Id `lh-reel-1110-<slug>`. Standalone; ONE drawn object + ONE number in frame 0 (<=2 text blocks); new scene composition (not the scene template of the coffee/flashcards Reels).
2. **C) Wed Nov 11 17:00 series: `lh-oneword-09` "One Word No. 9"** (promised). 2 slides, SAME layout as No. 8, number on the cover, cover hook <=8 words. Caption last line: "One Word No. 10 lands Fri Nov 13 at 5 pm."
''',
 'fullyfunded': '''1. **A) Tue Nov 10 19:00 Reel** (no trial). Id `ff-reel-1110-<slug>`. Standalone; a felt moment + ONE number + ONE drawn object in frame 0 (<=2 text blocks), "Canada" on screen. (Desk order 5: FF holds; no topic-family change.)
2. **C) Wed Nov 11 17:00 series: `ff-richhabits-08` "Rich Habits, Decoded No. 8"** (promised). 2 slides, SAME layout as No. 7, number on the cover, hook <=8 words naming a money moment. Caption last line: "Rich Habits, Decoded No. 9 lands Fri Nov 13 at 5 pm."
''',
 'hourback': '''1. **A) Tue Nov 10 19:00 Reel** (no trial). Id `hb-reel-1110-<slug>`. Deadline hook with a number (<=6 words) AND the filled real AI output (or a picture + the number, like the 30:00 timer over the mess) visible in frame 0. Never an empty box.
2. **C) Wed Nov 11 17:45 series: `hb-day15-<slug>` "AI, for real · Day 15"** (promised). 2 slides, SAME layout as Day 14, real run. Caption last line: "AI, for real · Day 16 lands Fri Nov 13 at 5:45 pm."
- **Real runs:** use the ISOLATED method in studio/editorial/nov03_hourback_run.py / nov04_hourback_run.py (empty folder, no setting sources, Project env vars removed). Never the plain `claude -p` call (it loads the claude.ai Project instructions and leaked the founder's name in a test on Nov 3). Save each transcript to studio/editorial/hb-nov05-run-<slug>.txt; scan it for any real personal name/employer before using it; quote exactly; label "shortened".
''',
}

page = {
 'littlefold': '- **LITTLEFOLD:** illustrated physical-rule format (sunny, warm, never gloomy), hook carries a picture-able size/amount/number (<=8 words). Official sources only. New topics only (NOT: grapes/round foods, sausage, nuts, 5 cm water/bath, toothpaste, burp, nails, bath elbow, swaddle, cord, neck check, tummy time, coat/car seat, honey, batteries, medicine mL, vitamin D, sleep position, gums, crying, hot drink, hand on baby, fever, vomiting, contact naps, 3 am play, high chair straps, hot tap 49°C, formula water, windows 10 cm, room 16-20°C, breathing pauses). Candidates to verify on the official page using its own number: furniture/TV tip-over (anchor it), blind cords, magnets, small-object choking size (toilet-roll tube if an official source says it), stair gates top and bottom, pot handles turned in, sun/sunscreen under 6 months, bath seat not a safety device, baby walkers, cot mattress gap (2 fingers?), car seat 2-hour rule, button-battery is DONE (skip). 3 am Club = a 3 am moment with one calm, official rule (not formula water, fever, vomiting, play, contact naps, breathing pauses): e.g. night feeds in dim light, hiccups, stuffy nose (saline), feeding to sleep, nappy change only if dirty, safe sleep after falling asleep on the sofa.',
 'lockedhour': '- **LOCKED HOUR:** "do this tonight/now" action with a number you can do, on ONE drawn object in the zine scene (warm shower = the model, 1,080 reach / 7 saves). Real peer-reviewed research cited exactly in caption/first_comment, never a study-claim open, and only findings that have held up (skip anything with failed replications, e.g. Ward 2017 phone-in-another-room). Avoid recent topics (shower before bed, lamp/ceiling light, break timer 24/6, get up after 20 min, slow sighs, workout 1 h, snooze, mix 3 kinds, calm music 45 min, doodle, head start, rereading, close eyes, grey phone, temptations, picture the win, new place, nap, batch, spacing, lyrics, planning fallacy, when-where, task switching, daydream, bedtime to-do, walk, write from memory, print it, last coffee 2 pm, flashcards right 3 times, same wake time). Ideas to verify: bedroom temperature, 10-minute walk after a meal, morning light soon after waking, 2-minute rule for starting, teach it to someone (protégé effect), self-testing before reading the answer (pretesting), alcohol and sleep, implementation of "if-then" for a habit is DONE (skip).',
 'fullyfunded': '- **FULLY FUNDED:** Canadian partner/family rules, felt moment + a number on frame 0, "Canada" on screen, drawn style, ONE drawn object doing the meaning (no pointing hand, piggy bank, table, penalty-fact opens, US). Avoid repeats (common-law, both file/CCB, POA, will, TFSA beneficiary/re-contribution, FHSA room, co-sign, late payment, promo end date, rule of 72, RESP grant SIN, pension splitting, Home Buyers Plan, Canada Learning Bond, CPP timing, EI, family medical on one return, spousal RRSP 3-year). Candidates to verify on canada.ca: RRSP rollover to a spouse at death (vs estate), TFSA successor holder, Canada caregiver credit, child care expense deduction (lower-income spouse claims), the disability tax credit transfer to a supporting person, Canada Child Benefit when separating (tell CRA by the end of the following month), donation credits combined on one return (first $200). Rich Habits = one money habit with a moment (not "sleep on it 24 h", money date, lunch, insurance divide, rent before payday, trial reminder day 28).',
 'hourback': '- **HOURBACK:** drawn occasion scene, hook = a deadline you can feel with a number in <=6 words, the REAL AI output visible from frame 0 (filled, never an empty box). Real runs only (isolated method). Avoid recent topics (toast, cue card, guests 30 min/tidy, potluck, gift for dad, costume, office card, interview, packing/flight, thank-you notes, 5 dinners, landlord heat email, pancakes, return policy, menu, hum, bill, group chat, recipe scaling, mechanic, homework, photo eraser, fridge dinner, kind-firm no, Nonna Italian card, retirement speech, missed 30th apology). No more speech-type pieces this week. Ideas: school permission form/reply due tomorrow, flight cancelled rebooking message, a 1-page resume summary before a 5 pm deadline, a babysitter note for tonight, a 3-day trip itinerary, a lost-package complaint to a store, splitting a shared bill fairly among 4 roommates, a meal-prep plan for 3 days from a grocery receipt.',
}

os.makedirs('nov05', exist_ok=True)
for p in page:
    open(f'nov05/BRIEF-{p}.md', 'w').write(head + jobs[p] + '\nPage-specific direction:\n' + page[p] + '\n\n' + std)
print('ok')

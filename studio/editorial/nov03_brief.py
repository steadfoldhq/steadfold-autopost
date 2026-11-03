"""Writes the Nov 3 2026 per-page maker briefs (studio/editorial/nov03/BRIEF-<page>.md)."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
b = open('nov02/BRIEF.md').read()
std = b[b.index('## THE STANDARD'):].replace('nov02', 'nov03').replace('Nov 2 2026', 'Nov 3 2026')

head = '''# Social studio, Tue Nov 3 2026: page build brief

You are the maker for ONE Steadfold Instagram page. Repo: /home/claude/steadfold-autopost (on main; do NOT git pull/commit/push, do NOT edit schedule/posts.json, never touch state/, keys/ or tokens). Studio engine already extracted to /home/claude/content (fonts + photos installed). The machine has only 2 CPUs / 7 GB RAM and 3 other makers render at the same time: render with 1 worker, one Reel at a time, and delete frame folders right after each encode (disk is limited). Use ffmpeg with -nostdin. Scratch dir: /tmp/claude-0/nov03-<page>/.

Clocks are EST (-05:00). Use "-05:00" in every publish_at.

**Budget:** finish Reel A first and write its manifest entry as soon as it is clean. Target: everything within ~4 h. If you run short, cut the series tile (C) rather than ship weak Reels; say why.

## Read first (they win over this brief)
- CLAUDE.md, docs/north-star.md (Founder lines win; your page's section + "All four live pages"), docs/brand-system-v4.md (addendum + your page's section), the top of docs/metrics.md (TEST-BATCH TABLE + "Today's orders", Tue Nov 3).
- The previous builds you EXTEND (copy into your own new script; don't edit shared kits or older scripts): Reels: studio/editorial/nov02_<page>*.py + studio/editorial/nov02/<page>.json + studio/editorial/nov02/BRIEF.md. Series tile: studio/editorial/nov01_<page>_feed.py + its entry in studio/editorial/nov01/<page>.json (the Wed Nov 4 episode).
- Recent topics on your page (no repeats from the last ~14 days): insights/latest.json `first_line`, queued items in schedule/posts.json for your account, and the nov01/nov02 manifests.

## What the data says (Performance desk, Nov 3; apply it)
1. **REPEAT: a number you can picture or do, in frame 0 and the first line, on every Reel.** All 3 FAST BATCHES had one ("Cut each grape into 4" 1,327 / 51%; "Shower 90 minutes before bed" 1,079 / 46%, 7 saves + 3 sends; "grain of rice" 1,339 / 53%). Physical rules / study claims without a number got 100-171.
2. **KILL sequel framing on frame 0.** Part 2s got 1/8 of the Part 1 batch (110-152 vs ~1,070). No "PART 2" labels on screen, no callback openers. **No new Part 1/Part 2 pairs today**: every Reel is standalone and must make sense alone.
3. **Feed reach is 0-1 on every tile.** Keep only the promised Fri series episode, 2 slides, minimal hours. Move the effort to Reel frame 0.
4. **HB:** deadline-you-can-feel + real AI output on screen (wedding toast 5.41 s / 38% on 121). Callback/tool-tip opens die (cue card 2.05 s on 14).
5. **FF:** HOLD topic changes (account check is the lead suspect). Stay on Canadian partner/family rules with a felt moment AND a number in frame 0.
6. **Follow beat:** on screen >=1.5 s, names what they get. Followers +2 in 7 days on ~6,300 Reel reach; both on FAST BATCH nights.

## YOUR JOB TODAY (quality over count; cut a piece rather than ship filler, and say why)
- **A) Fri Nov 6, 19:00 Reel** (no trial). Id `<pp>-reel-1106-<slug>`. BUILD THIS FIRST. Standalone, number in frame 0.
- **B) Sat Nov 7, 19:00 Reel** (no trial). Id `<pp>-reel-1107-<slug>`. Standalone, number in frame 0, different topic family from A.
- **C) Fri Nov 6 series episode** (promised): LF `lf-3amclub-06` "3 am Club No. 6" 17:00; LH `lh-oneword-07` "One Word No. 7" 17:00; FF `ff-richhabits-06` "Rich Habits, Decoded No. 6" 17:00; HB `hb-day13-<slug>` "Day 13" 17:45 (real Claude run). 2 slides, SAME cover layout as the Wed episode (No. 5/6/5/Day 12), the number visible on the cover, cover hook <=8 words naming a moment in the viewer's own words. Caption last line says the next episode lands Mon Nov 9 at the same time.
- Follow lines (last beat): LF "Follow for one calm thing a night, from bump to toddler."; LH "Follow for one small sleep or focus trick a day."; FF "Follow for one money rule a day, in plain words."; HB "Follow to learn one real AI trick a day."
'''

extra = {
    'littlefold': '''- **LITTLEFOLD extra job D (do it first, it is quick):** `lf-reel-1105-battery-honey` (Thu Nov 5 19:00, built by studio/editorial/nov02_littlefold.py, media/studio-nov02/littlefold/) shows a "PART 2 · COIN BATTERIES" pill on every frame. Desk order: no sequel label on screen. Re-render it with the pill reading "COIN BATTERIES", everything else identical; overwrite the same mp4 (and the cover only if the cover has the label). Keep the caption's Part 2 mention. Write the full entry (caption etc. copied from nov02/littlefold.json, beats updated) into your nov03 manifest with `"replaces_existing": true`. Check the strip.
''',
    'lockedhour': '''- **LOCKED HOUR extra job D (quick):** `lh-reel-1105-workout-1h` (Thu Nov 5 19:00, nov02_lockedhour.py, media/studio-nov02/lockedhour/) beat 2 kicker reads "sleep, part 2". Desk order: no sequel framing on screen. Re-render with that kicker reading "the catch", everything else identical; overwrite the same mp4. Write the full entry (copied from nov02/lockedhour.json, beats updated) into your nov03 manifest with `"replaces_existing": true`. Check the strip.
''',
    'fullyfunded': '', 'hourback': '',
}

page = {
    'littlefold': '- **LITTLEFOLD:** illustrated physical-rule format (sunny, warm), hook carries a picture-able size/amount/number (<=8 words). Official sources only. New topics only (not grapes/round foods, sausage, nuts, 5 cm water/bath, toothpaste, burp, nails, bath elbow, swaddle, cord, neck check, tummy time, coat/car seat, honey, batteries, medicine mL, vitamin D, sleep position, gums, crying, hot drink, hand on baby, fever, vomiting, contact naps, 3 am play). Candidates to verify on the official page using its own number: furniture/TV tip-over (anchor it), blind cords, magnets, hot tap water/scald temperature, small-object choking size (toilet-roll tube if an official source says it), window limits, stair gates, high-chair straps, pot handles turned in. 3 am Club = a 3 am moment with one calm, official rule.',
    'lockedhour': '- **LOCKED HOUR:** "do this tonight/now" action with a number you can do on ONE drawn object in the zine scene (warm shower = the model). Real peer-reviewed research cited exactly in caption/first_comment, never a study-claim open. Avoid recent topics (shower before bed, lamp/ceiling light, break timer 24/6, get up after 20 min, slow sighs, workout 1 h, doodle, head start, rereading, close eyes, grey phone, temptations, picture the win, new place, nap, batch, spacing, lyrics, planning fallacy, when-where, task switching, daydream, bedtime to-do, walk, write from memory, print it). Ideas to verify: caffeine cutoff hours before bed (cite exactly, e.g. Drake 2013), bedroom temperature, 10-minute walk after a meal, phone in another room (Ward 2017), morning light soon after waking.',
    'fullyfunded': '- **FULLY FUNDED:** Canadian partner/family rules, felt moment + a number on frame 0, "Canada" on screen, drawn style, ONE drawn object doing the meaning (no pointing hand, piggy bank, table, penalty-fact opens, US). Avoid repeats (common-law, both file/CCB, POA, will, TFSA beneficiary/re-contribution, FHSA room, co-sign, late payment, promo end date, rule of 72, RESP grant SIN, pension splitting, CPP timing, EI). Candidates to verify on canada.ca: spousal RRSP 3-year attribution, RRSP beneficiary vs estate for a spouse (rollover), Canada Learning Bond ($500 first year, lower-income families, no contribution needed), Home Buyers Plan $60,000 each for a couple, TFSA successor holder (only if clearly different from beneficiary).',
    'hourback': '- **HOURBACK:** drawn occasion scene, hook = a deadline you can feel with a number in <=6 words ("Interview at 9 am", "Guests in 30 minutes"), the AI output visibly on screen, a REAL run (fresh subagent runs the prompt verbatim on made-up input; save transcript to studio/editorial/hb-nov03-run-<slug>.txt; quote exactly; label "shortened"). Avoid recent topics (toast, cue card, guests 30 min/tidy, potluck, gift for dad, costume, office card, interview, packing, pancakes, return policy, menu, hum, bill, group chat, recipe scaling, mechanic, homework, photo eraser, fridge dinner, kind-firm no). Ideas: 20 thank-you notes due today, landlord email before 5 pm, a 2-minute retirement speech, school form due tomorrow, 5 dinners from one grocery run, flight cancelled rebooking message, a birthday message in another language.',
}

os.makedirs('nov03', exist_ok=True)
for p in page:
    open(f'nov03/BRIEF-{p}.md', 'w').write(head + extra[p] + '\nPage-specific direction:\n' + page[p] + '\n\n' + std)
print('ok')

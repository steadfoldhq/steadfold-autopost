# Metrics (Performance desk, repo copy while the Learning Lab project is full)

## TEST-BATCH TABLE (Tue Oct 27, 2026, Performance desk)
Data: insights/latest.json, collected **Oct 27 04:37 UTC (12:37 am ET)**. Per-post curves rebuilt from **34** reads in git (Oct 19 04:37 → Oct 27 04:37 UTC). Reel lengths from ffprobe on each entry's MP4. Next read ~12:40 UTC (8:40 am ET).
- **Verdict rules (unchanged):** EXPANDED = reach still climbing after 24 h (≥ +25% and ≥ +10) AND sends/reach in the top third. STALLED = flat after 24 h. FAILED HOOK = average watch under 4 s or under 25% of length. PENDING = under 24 h.
- **Non-follower share** is a floor: (reach − current followers) / reach. follow_type still not read; per-post `follows` still HTTP 400.
- **⚠ Two more bursts, 3 in 24 h:**
  - **Oct 26 14:50 UTC:** FF 6, HB 5, LF 5 posts each gained exactly **+5 shares** (missed in yesterday's report).
  - **Oct 27 04:37 UTC, Littlefold only:** 15 posts dated Oct 21–26 gained exactly **+10 shares, +2 saves and +1–2 likes**; 4 more gained +5 / +1 (+207 shares, +38 saves). FF, LH and HB gained 0 shares in that window. LF profile views doubled (5 → 10), followers stayed at 6. The likely source is one or two visitors working through the back catalogue, not strangers in the feed. That's an inference.
  - Every send and save below has these windows removed (7 windows since Oct 19).
- **Comments per reach = 0 everywhere.** All counted comments are our own first comments; 0 texts returned (day 13).

| Page | Post (first line) | Format | Age | Reach curve (age → reach) | Non-follower ≥ | Sends/reach (clean) | Saves/reach (clean) | Avg watch / length | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LF | **"Gulping, then fussing, every feed? Pause and burp partway through"** | Reel 14.5 s (trial, out 1 h 53 m late) | 15 h | 1h 78 → 3h 142 → 7h 307 → 15h **365** | 98% | 0.003 (1) + 37 in the burst window | 0.00 (4 in the burst window) | **8.65 s / 60%** | PENDING, **still climbing**. **Biggest batch and best hold on any batch ≥40, ever.** Needs clean sends to be EXPANDED |
| LF | "It's OK to step away. Still crying…" | Reel 14.2 s | 29 h | 5h 148 → 16h 149 → 29h 154 | 96% | 0.00 | 0.00 | 2.7 s / 19% | FAILED HOOK + STALLED |
| LF | "Sore gums tonight? A cold cloth and a gentle rub." | Reel 11.7 s (trial) | 64 h | 8h 122 → 24h 124 → 64h 130 | 95% | 0.00 | 0.00 | 3.1 s / 27% | FAILED HOOK + STALLED |
| LF | "You can't spoil a newborn. Pick them up." | Reel 14.0 s (trial) | 40 h | 4h 107 → 16h 110 → 40h 114 | 95% | 0.00 | 0.00 | **5.04 s / 36%** | STALLED. Hold bars passed |
| FF | "Put TFSA money back too soon? …next January 1." | Reel 15.0 s | 29 h | 5h 106 → 16h 113 → 29h 114 | 94% | 0.00 | 0.00 | 4.9 s / 33% | FAILED HOOK (by 0.1 s) + STALLED |
| LH | "Studying with your playlist on? Check the words." | Reel 13.2 s | 53 h | 5h 105 → 29h 107 → 53h 108 | 96% | 0.01 (1) | 0.00 | 4.6 s / 35% | STALLED |
| LF | "New dad, feeling left out?…" | Reel 14.2 s | 53 h | 5h 102 → 29h 105 → 53h 108 | 94% | 0.00 | 0.00 | 2.5 s / 17% | FAILED HOOK + STALLED |
| LH | "New habit keeps not sticking? Floss before or after…" | Reel 13.7 s (trial) | 64 h | 15h 58 → 23h 104 → 63h 107 | 96% | 0.00 | 0.01 | 4.0 s / 29% | FAILED HOOK (by s) + STALLED |
| FF | "Not married? No will? In Ontario…" | Reel 14.8 s (trial) | 40 h | 8h 9 → 16h 31 → 26h 106 → 40h 107 | 93% | 0.00 | 0.00 | 1.8 s / 12% | FAILED HOOK + STALLED (late batch at 16–26 h) |
| LH | "Everything takes longer than you think?…" | Reel 12.9 s (trial) | 40 h | 3h 101 → 15h 105 → 39h 106 | 96% | 0.00 | 0.01 | 3.8 s / 29% | FAILED HOOK (by s) + STALLED |
| LH | **"For whoever studies on their phone: you understand more on paper."** | Reel 13.6 s (send-on-screen test) | 6 h | 5h **106** | 96% | **0.01 (1)** | 0.00 | 4.0 s / 29% | PENDING. 1 send per 106 (goal 1 per 50) |
| LF | **"Scratches on their face again? Keep those tiny nails short"** | Reel 14.9 s | 6 h | 6h **105** | 94% | burst window | burst window | **7.6 s / 51%** | PENDING. 2nd-best hold on a batch ≥100 |
| HB | "Open fridge, no plan? You already have dinner." | Reel 14.0 s | 53 h | 5h 101 → 53h 103 | 95% | 0.00 | 0.00 | 1.2 s / 9% | FAILED HOOK + STALLED |
| HB | "Stranger in your best photo? Your phone's AI can erase them" | Reel 12.6 s | 6 h | 6h **58** | 91% | 0.00 | 0.00 | 2.9 s / 23% | FAILED HOOK + PENDING. HB's 2nd-biggest 5 h batch |
| LH | "\"It'll take an hour.\" It won't." | Reel 13.6 s | 29 h | 5h 27 → 16h 43 → 29h 44 | 91% | 0.00 | 0.00 | 2.6 s / 19% | FAILED HOOK + STALLED |
| FF | "Your TFSA, after you die?…" | Reel 13.5 s | 53 h | 5h 4 → 17h 15 → 53h 19 | 63% | 0.00 (burst-cleaned) | 0.00 | 1.9 s / 14% | FAILED HOOK + STALLED |
| FF | "Your $10,000 earning 0% interest?…" | Reel 14.9 s (no trial) | 6 h | 6h **16** | 56% | 0.00 | 0.00 | 2.0 s / 13% | FAILED HOOK + PENDING. **Grade ≥60 at 5 h: missed** |
| FF | "Too sick to work for months? Here's what EI pays." | Reel 13.4 s (trial) | 64 h | 16h 8 → 64h 10 | 30% | 0.00 | 0.00 | 7.2 s (10 viewers) | STALLED, no stranger batch |
| HB | "That sparkle button? It's AI." | Reel 13.0 s (trial) | 40 h | 15h 6 → 39h 10 | 50% | 0.00 | 0.00 | 3.4 s / 26% | FAILED HOOK + STALLED, no batch |
| HB | "3-minute voice note, mid-meeting?…" | Reel 13.2 s | 63 h | 15h 6 → 63h 8 | 38% | 0.00 | 0.00 | 4.4 s / 33% | STALLED, no batch |
| FF | "How long until $10K is $20K? Divide 72…" | Reel 14.6 s (trial, 98 m late) | 15 h | 3h 3 → 7h 7 → 15h 7 | 0% | 0.00 | 0.00 | 2.6 s / 18% | FAILED HOOK + PENDING, no batch |
| LH | "Monday plans gone by noon? Write down when and where…" | Reel 14.3 s (trial, 83 m late) | 15 h | 3h 1 → 7h 3 → 15h 3 | 0% | 0.00 | 0.00 | 1.9 s / 13% | FAILED HOOK + PENDING, no batch |

**Feed posts in the window (16: 14 carousels, 2 singles):** all STALLED or PENDING at reach **0–10**, 0 clean sends, 0 clean saves. Best: LF "Just a little honey on the soother?" (7 sl), LF Small Wins No.2 (single) and LF vitamin D (single), 10 each. Yesterday's 4 feed posts reached 0–4.

**EXPANDED: 0 of 176.** What moved since yesterday:
1. **Littlefold's illustrated "physical rule, shown being done" Reels just posted the two best results we've had.**
   - "Burp partway through" reached **365** (LF's best before was 154) and held **8.65 s / 60%**. Reach went 78 → 142 → 307 → 365 over 1–15 h, and it's still climbing.
   - "Baby nails" held **7.6 s / 51% on 105** at 6 h.
   - Both are from the Oct 24 batch: felt question → one physical rule drawn being done, in the illustrated washing-line style.
   - Every other LF batch ≥100 held 2.5–6.7 s.
   - n = 2, medium-low confidence. It's the first time both hold bars have been cleared by this margin.
2. **The burp Reel's sends can't be counted yet.** It has 1 clean send. It gained +37 shares in the LF burst window, against the burst's +10 on every other post, so **about 27 of those may be real**. Can't be separated from a total.
3. **Locked Hour and Fully Funded morning trials got no batch.** The Mon 8:15–8:30 Reels went out 83–98 min late and reached 3 and 7 at 15 h. LH's three earlier morning trials got 101–107. So **the delay doesn't explain it**: the burp Reel was late too and got 365.
4. **FF's recovery didn't hold.** The non-trial Mon 7 pm "0% interest" Reel reached 16 at 6 h (goal ≥60). Saturday's TFSA trap got 106. FF has had 2 batches ≥100 in its last 6 Reels.
5. **The on-screen send test started:** LH "print it" got 1 send on 106. That's 1 per 106 against the goal of 1 per 50. The 3 remaining tests run Tue–Wed 7 pm; grade on Thursday's read.

- **TikTok:** manual (no API; no numbers logged).
- **YouTube Shorts:** no data yet. vidIQ checked this run: signed in as the Steadfold Gmail, **0 YouTube channels** and **0 Instagram accounts** connected.
- **Trial Reels:** 41 measured. Graduation to followers: no data yet (not in the API).

**3 orders**
1. **REPEAT:** the LF illustrated physical-rule format (felt question → one rule drawn being done, ≤15 s). Burp held 8.65 s / 60% on 365 and nails 7.6 s / 51% on 105. Today's bath-elbow and swaddle-hips Reels are the same batch; grade them on Wednesday's read.
2. **KILL:** the trial flag on LH and FF morning Reels until a trial gets a batch again (Mon: 3 and 7 at 15 h). Also kill reassurance opens (step away 2.7 s on 154, new dad 2.5 s on 108, fridge 1.2 s on 103).
3. **TEST:** the burp format ported to one HB and one LH Reel: a felt question, then the action drawn being done by second 2 in a single illustrated scene. Grade: ≥5 s and ≥30% on ≥40.

## Today's orders (Tue Oct 27, 2026, Performance desk)
Data: Oct 27 04:37 UTC read, 34 reads of per-post curves. 176 posts tracked (40 per page in the latest read), 22 followers. Direction: medium confidence. Three bursts landed in 24 h, so every order ranks on reach, hold and burst-cleaned sends.
1. **Social studio: FILL the empty slots in the next 48 h (to 7:40 am ET Thu Oct 29).**
   - **Wed Oct 28 has no morning Reel on any of the 4 pages.** Every page has 1 Reel on Wed (7 pm) and 1 on Thu.
   - **Stories: 2 per page per day** Tue–Thu, against the 3–5 cadence.
   - Priority: the LF Wed 8 am Reel, in the burp format (order 2). Then LH, FF and HB with no trial flag. Rollback record in docs/social-recovery/ as usual.
2. **Short-form studio (Littlefold): MORE illustrated physical-rule Reels; this is now LF's default format.**
   - Burp: 365 reach, 8.65 s / 60%. Nails: 105 at 6 h, 7.6 s / 51%. The 12 other LF batches ≥100 since Oct 19 held 2.5–6.7 s.
   - Build 2 more for Wed–Thu. Keep: one felt question in frame 0, the rule drawn being done by second 2, ≤15 s, official-source fact.
   - Don't scale past ~4 a week until Wednesday's read grades bath-elbow and swaddle-hips (QG-4).
   - **Grade:** ≥5 s AND ≥30% on ≥100.
3. **Social studio (Locked Hour + Fully Funded): DROP `"trial": "auto"` from LH and FF morning Reels.**
   - Mon's LH and FF trials reached 3 and 7 at 15 h. Today's lh-reel-1027am-head-start (8:30 am) still carries the flag and will publish before the studio's 9:17 run; apply this to every LH and FF morning Reel from Wed.
   - FF trial median since Oct 19 is 20 (n=7) against 55 for normal Reels (n=7).
   - **Grade:** ≥40 at 15 h.
4. **Short-form studio (Hourback + Locked Hour): TEST the burp format on one HB and one LH Reel by Thu.**
   - HB "photo eraser" got 58 strangers at 6 h and held 2.9 s. HB fridge held 1.2 s on 103. HB has never held ≥4 s on a batch ≥40.
   - Use a single illustrated scene with the action shown being done (the stranger rubbed out of the photo), not a phone screen-recording.
   - **Grade:** ≥5 s and ≥30% on ≥40.
5. **Social studio (Fully Funded): REPEAT the trap-with-a-date open and stop the inflation and abstract-number opens.**
   - TFSA trap: 114, 4.9 s / 33%. Wills: 122. One-year wait: 104.
   - Mon's "0% interest" Reel: 16 at 6 h, 2.0 s. Rule of 72: 7, 2.6 s.
   - Wed 7 pm FHSA room fits (a trap with a date). Check that frame 0 states the trap, not a number.
6. **Automation architect:**
   - **3 bursts in 24 h:** Oct 26 04:38 (all pages), Oct 26 14:50 (+5 each on FF/HB/LF) and Oct 27 04:37 (LF only, +10 shares / +2 saves / +1–2 likes on 15 posts). The LF one moved likes too, so it looks like real accounts working through the profile.
   - Check whether one account is doing this, and whether Facebook Page cross-posts count as post shares.
   - **Autopost delay:** the Mon 8:00–8:30 am Reels went out at 9:53 am ET, 83–113 min late, more than one run cycle. Check the runner queue.
   - Same open asks: per-post history lines (day 12), comment text (day 13), follow_type, the per-post `follows` HTTP 400.

**Grading yesterday's orders (owner check):**
1. **Fill the 48 h slots: done for Tue.** Every page has 2 Reels and a feed post on Tue, and Stories are back (2 a day). The Wed morning Reels are empty (order 1).
2. **FF non-trial trap Reels, ≥60 at 5 h: missed.** The Mon 7 pm "0% interest" Reel got 16. The Mon 8:15 rule of 72 still ran as a trial (7).
3. **LF rule-as-fact, ≥5 s AND ≥30% on ≥100: passed twice.** Burp 8.65 s / 60% on 365; nails 7.6 s / 51% on 105.
4. **HB morning non-trial: pending.** The Tue 8:45 Reel goes out today; grade ≥20 at 15 h on Wednesday's read.
5. **On-screen send test: 1 of 4 run.** LH 1 per 106; grade Thursday.
6. **Automation asks: not done.**

---

## Daily report: Tue Oct 27, 2026

### Scoreboard (insights read Oct 27 04:37 UTC)
Changes are vs the Oct 26 04:38 UTC read (1 day) and vs Oct 20 04:34 UTC (7 days). Sends and saves are burst-cleaned.

| Page | Followers (1d / 7d) | Feed posts 7d (slides) | Reels 7d | Median reach (all / Reels / feed) | Best by clean (saves+sends)/reach | Worst | Best by views | Worst by views (>24 h) |
|---|---|---|---|---|---|---|---|---|
| Fully Funded | 7 (+0 / −1) | 12 carousels (10, 10, 9, 9, 7, 7, 7, 7, 6, 5, 5, 3 sl) | 13 | 9 / 22 / 5 | Reel "one year costs you by 65" 1/104 = 0.01; no feed post scored | Reel "Not married? No will?" 0/122 | Reel "Not married? No will?" 143 | Reel "parents taking CPP early" 5 |
| Locked Hour | 4 (+0 / −2) | 12 carousels (10, 10, 10, 10, 7, 7, 7, 7, 6, 5, 3, 3 sl) | 12 | 5.5 / 41.5 / 3 | Reel "Missed a day?" 5/32 = 0.16 · "Check the words" 1/108 | Reel "For every parent who gets interrupted" 0/110 | Reel "Everything takes longer" 132 | Carousel "Sunday scaries" (7 sl) 6 |
| Hourback | 5 (+0 / −1) | 11 carousels (10, 9, 9, 9, 9, 7, 7, 7, 7, 6, 3 sl) | 11 | 7.5 / 13 / 3 | Carousel "Where do your AI chats go?" (9 sl) 5/5 (older burst likely; weak) | Reel "Open fridge, no plan?" 0/103 | Reel "Open fridge, no plan?" 109 | Carousel "25% faster" (6 sl) 5 |
| Littlefold | 6 (+0 / −1) | 13 (carousels 9, 9, 8, 7, 7, 7, 7, 6, 5, 3, 2 sl; 2 singles) | 13 | 32.5 / 108 / 6 | Reel "burp partway" 1/365 · carousel "meltdown" (9 sl) 1/4 | Reel "It's OK to step away" 0/154 | **Reel "burp partway" 461** | Carousel "5 minutes a day" (7 sl) 18 |

**Total: 22 followers (+0 since yesterday's read, −5 vs Oct 20).** Flat for 16 reads (since Oct 23 04:35 UTC).
- **Yesterday's posts (Oct 26 ET, 12 posts: 8 Reels, 4 feed):**
  - Best by clean (saves + sends)/reach: LH "print it", 1/106. LF burp is 1/365 clean, with +37 more in the burst window.
  - Best on strangers: **LF "burp partway", 365 reach, 8.65 s / 60%.**
  - Best by views: the same Reel, 461.
  - Worst: LH "when and where", 3 reach at 15 h; the feed posts got 0–4.
- **Sum of post reach (1 day, 40 newest posts):** FF 1,077 → 1,079, LH 1,099 → 1,157, HB 601 → 652, LF 2,282 → 2,596.

### Patterns (all pages ≥5 posts)
- **Reels vs feed (high confidence on direction):** since Oct 19, Reels have a median reach of 33 (n=53) against 5.5 for feed posts (n=52). The 24 batches of ≥100 are 93–98% non-follower.
- **Length (medium-high, n=53 Reels since Oct 19, ≥12 h old):** ≤15 s: 29% median watch-through, 3.6 s, reach 41.5 (n=36). 30–40 s: 11%, 4.0 s, reach 44 (n=14).
- **Format (medium-low, n=2):** LF illustrated physical-rule Reels (burp, nails) held 7.6–8.65 s / 51–60%. The 22 other ≥100 batches held 1.2–6.7 s, median about 3.9 s.
- **Open type (medium):** rule as fact: 5.0–5.6 s on ≥100 (coat, toddler play, spoil). Reassurance: 1.2–2.7 s (step away, fridge, new dad, bedtime).
- **Trial flag (medium):** median reach, trial vs normal since Oct 19: FF 20 vs 55 (n=7/7), HB 10.5 vs 18 (6/6), LH 61.5 vs 32 (6/7), LF 113 vs 107.5 (8/6). Mon's LH trial got 3, so the LH edge is fading.
- **Page (medium):** LF has 14 of the 24 batches ≥100 since Oct 19; LH 5, FF 4, HB 1.
- **Sends:** 3 clean sends in the last 72 h, on ~1,970 post reach (LH "check the words", LH "print it", LF burp).

### Comments
**No data yet.** 0 real comments; comment text has been empty for 13 days.

### Health
- **Published vs schedule:** all **356 of 356** entries due by 11:39 UTC Oct 27 are published, with 0 failed, 0 errors and 0 comment errors (last state push Oct 26 23:08 UTC).
  - **Late:** the Mon 8:00, 8:15 and 8:30 am Reels (LF, FF, LH) went out together at 9:53 am ET, 113, 98 and 83 min late. That's more than one run cycle. Everything else in 36 h was within 20 min.
- **Next 48 h (to 7:40 am ET Thu Oct 29):** each page has 3 Reels, 2 feed posts and 4 Stories.
  - **Empty: the Wed Oct 28 morning Reel on all 4 pages.** Stories run 2 a day per page (cadence 3–5).
  - All media files exist. The schedule runs to Fri Oct 30, 5:45 pm.
- **Data:** all 34 insight reads succeeded, with no token or account errors.
  - **Still broken:** comment text, follow_type, per-post `follows` (HTTP 400) and per-post history lines.
  - **New:** 2 more bursts (order 6).

### For the Automation architect
See order 6: the burst source (3 in 24 h, one with likes), the Monday 8 am runner delay, and the standing asks.

### Media kit
Updated (claude/media-kit.md).

---

## TEST-BATCH TABLE (Mon Oct 26, 2026, Performance desk)
Data: insights/latest.json, collected **Oct 26 04:38 UTC (12:38 am ET)**. Per-post curves rebuilt from **40** reads in git (Oct 16 16:35 → Oct 26 04:38 UTC). Reel lengths from ffprobe on the MP4 each schedule entry points to. Next read ~12:40 UTC (8:40 am ET).
- **Verdict rules (unchanged):** EXPANDED = reach still climbing after 24 h (≥ +25% and ≥ +10) AND sends/reach in the top third. STALLED = flat after 24 h. FAILED HOOK = average watch under 4 s or under 25% of length. PENDING = under 24 h.
- **Non-follower share** is a floor: (reach − current followers) / reach. follow_type still not read; per-post `follows` still HTTP 400.
- **⚠ NEW BURST in the Oct 26 04:38 UTC read, all 4 pages:** FF 9 of 39 posts, LH 22 of 39, HB 15 of 40, LF 10 of 38 gained shares and saves together (≈ +3 shares and +1 save each; +172 shares in one window, reach flat). It's the same shape as Oct 21 and Oct 23. **Every send and save below has 6 burst windows removed.** Last night's 3 new Reels got their first read inside the burst, so their 2–3 "sends" can't be counted.
- **Comments per reach = 0 everywhere.** 160 comments on 160 posts, all our own first comments; 0 texts returned (day 12).

| Page | Post (first line) | Format | Age | Reach curve (age → reach) | Non-follower ≥ | Sends/reach (clean) | Saves/reach (clean) | Avg watch / length | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LF | "It's OK to step away. Still crying, and you're at your limit?" | Reel 14.2 s | 5 h | 5h **148** | 96% | burst window | burst window | 2.5 s / 18% | FAILED HOOK + PENDING. **LF's biggest 5 h batch ever, lost at 2.5 s** |
| LF | "Sore gums tonight? A cold cloth and a gentle rub." | Reel 11.7 s (trial) | 40 h | 8h 122 → 24h 124 → 40h 127 | 95% | 0.00 | 0.00 | 2.8 s / 24% | FAILED HOOK + STALLED |
| LF | "You can't spoil a newborn. Pick them up." | Reel 14.0 s (trial) | 16 h | 4h 107 → 16h 110 | 95% | 0.00 | 0.00 | **4.99 s / 36%** | PENDING. Misses the 5 s bar by 0.01 s |
| LF | "Bedtime turned into a battle again? …best 20 minutes" | Reel 14.4 s (trial) | 65 h | 25h 107 → 41h 108 → 65h 110 | 95% | 0.00 | 0.00 | 2.5 s / 17% | FAILED HOOK + STALLED |
| LH | "Studying with your playlist on? Check the words." | Reel 13.2 s | 29 h | 5h 105 → 17h 106 → 29h 107 | 96% | **0.01 (1)** | 0.00 | 4.6 s / 34% | STALLED. Still the only clean send in 72 h |
| FF | **"Put TFSA money back too soon? The room… only comes back next January 1."** | Reel 15.0 s (no trial) | 5 h | 5h **106** | 93% | burst window | burst window | **5.0 s / 33%** | PENDING. **FF's first Reel ever to pass both hold bars**, and delivery is back |
| LF | "First cold morning? Coat off, then buckle." | Reel 14.4 s | 53 h | 21h 102 → 41h 102 → 53h 105 | 94% | 0.00 | 0.00 | **5.6 s / 39%** | STALLED. Hold bars passed, 0 sends |
| LH | "New habit keeps not sticking? Floss before or after brushing…" | Reel 13.7 s (trial) | 39 h | 7h 39 → 15h 58 → 23h 104 → 39h 105 | 96% | 0.00 | 0.00 | 3.6 s / 26% | FAILED HOOK (by s). Late batch (+46 from 15 h to 23 h), flat since |
| LF | "New dad, feeling left out?…" | Reel 14.2 s | 29 h | 5h 102 → 29h 105 | 94% | 0.00 | 0.00 | 2.4 s / 17% | FAILED HOOK + STALLED |
| LH | "Everything takes longer than you think? It's not just you." | Reel 12.9 s (trial) | 15 h | 3h 101 → 7h 101 → 15h 105 | 96% | 0.00 | 0.00 | 3.6 s / 28% | FAILED HOOK (by s) + PENDING |
| HB | "Open fridge, no plan? You already have dinner." | Reel 14.0 s | 29 h | 5h 101 → 29h 102 | 95% | 0.00 | 0.00 | 1.2 s / 9% | FAILED HOOK + STALLED |
| LH | "Coffee at 4 pm? Your sleep noticed…" | Reel 13.9 s | 53 h | 21h 33 → 53h 39 | 90% | 0.00 | 0.00 | 2.8 s / 20% | FAILED HOOK + STALLED |
| FF | "Not married? No will? In Ontario, your partner may get nothing." | Reel 14.8 s (trial) | 16 h | 4h 5 → 8h 9 → 16h 31 | 77% | 0.00 | 0.00 | 3.1 s / 21% | FAILED HOOK + PENDING, late batch |
| LH | "\"It'll take an hour.\" It won't." | Reel 13.6 s | 5 h | 5h 27 | 85% | burst window | burst window | 2.9 s / 22% | FAILED HOOK + PENDING |
| FF | "Your TFSA, after you die?…" | Reel 13.5 s | 29 h | 5h 4 → 17h 15 → 29h 17 | 59% | 0.00 | 0.00 | 1.6 s / 12% | FAILED HOOK + STALLED |
| HB | "Skimming just the AI summary?…" | Reel 13.6 s | 53 h | 21h 15 → 53h 16 | 69% | 0.00 | 0.00 | 2.7 s / 20% | FAILED HOOK + STALLED |
| FF | "Too sick to work for months? Here's what EI pays." | Reel 13.4 s (trial) | 40 h | 8h 4 → 24h 8 → 40h 9 | 22% | 0.00 | 0.00 | 6.1 s (9 viewers) | STALLED, no stranger batch |
| HB | "3-minute voice note, mid-meeting?…" | Reel 13.2 s | 39 h | 7h 5 → 23h 6 → 39h 7 | 29% | 0.00 | 0.00 | 4.2 s / 31% | STALLED, no stranger batch |
| HB | "That sparkle button? It's AI." | Reel 13.0 s (trial) | 15 h | 3h 1 → 7h 4 → 15h 6 | 17% | 0.00 | 0.00 | 5.2 s (6 viewers) | PENDING, no stranger batch |
| HB | "Weird light on your dashboard?…" | Reel 14.3 s (trial) | 63 h | 7h 3 → 63h 4 | 0% | 0.00 | 0.00 | 5.9 s (4 viewers) | STALLED, no stranger batch |
| FF | "Your parents taking CPP early?…" | Reel 13.0 s | 53 h | 21h 3 → 53h 4 | 0% | 0.00 | 0.00 | 5.0 s (4 viewers) | STALLED, near-zero delivery |

**Feed posts in the window (20: 18 carousels, 2 singles):** all STALLED or PENDING at reach **0–13**, 0 clean sends, 0 clean saves. Best: LH "Rereading the same line" (10 sl) 13. The 5 Oct 25 feed posts (1–5 slides) reached 2–4.

**EXPANDED: 0 of 160.** What moved since yesterday:
1. **Fully Funded's delivery is back.** The non-trial 7 pm Reel "Put TFSA money back too soon?" got 106 reach in 5 h (93% non-follower), after 3 Reels at 3–8. It also held 5.0 s / 33%, the first FF Reel to pass both hold bars. What changed: no trial flag, and a "trap rule with a date" open. The FF trial Reel that morning (wills) got 31 at 16 h. Since Oct 19, FF trial Reels have a median reach of 21 (n=6) against 39 for normal ones (n=6).
2. **Three Reels have now passed ≥5 s AND ≥30% on ≥40** (LF toddler play, LF coat, FF TFSA trap), and LF "You can't spoil a newborn" missed by 0.01 s. All four open on a **rule stated as a fact** ("Coat off, then buckle", "You can't spoil a newborn", "only comes back next January 1").
3. **Reassurance opens lost the biggest batch again.** LF "It's OK to step away" won 148 strangers in 5 h, LF's biggest early batch ever, and held 2.5 s. It joins HB fridge (1.2 s on 102), LF new dad (2.4 s on 105) and LF bedtime (2.5 s on 110).
4. **The caption send-line test has failed.** Over Oct 24–25, the Reels (most with a caption "Send this to…" line) reached about 940 people and earned 1 clean send (goal: 1 per 50). The on-screen send tests start tonight (Mon–Thu 7 pm).
5. **Hourback's morning Reels get no batch.** HB 8:45 Reels since Oct 23 reached 4, 7 and 6. HB trial median since Oct 19 is 10.5 (n=6) against 17.5 for normal (n=6).

- **TikTok:** manual (no API; no numbers logged).
- **YouTube Shorts:** no data yet. vidIQ checked this run: signed in as the Steadfold Gmail, **0 YouTube channels** connected.
- **Trial Reels:** 37 measured. Graduation to followers: no data yet (not in the API).

**3 orders**
1. **REPEAT:** a rule stated as a fact in frame 0, with the trap or date in the first line ("Put TFSA money back too soon? … only comes back January 1", "Coat off, then buckle", "You can't spoil a newborn"). 4 of 4 held 5.0–5.6 s / 33–39% on 105–110.
2. **KILL:** reassurance opens on the big LF/HB batches (step away 2.5 s on 148, fridge 1.2 s on 102, new dad 2.4 s on 105), and the trial flag on FF and HB (trial medians 21 and 10.5 vs 39 and 17.5).
3. **TEST:** tonight's on-screen send asks (Mon–Thu 7 pm, already queued). Grade on Wed's read: ≥1 clean send per 50 reach.

## Today's orders (Mon Oct 26, 2026, Performance desk)
Data: Oct 26 04:38 UTC read, 40 reads of per-post curves. 160 posts (78 Reels, 82 feed), 22 followers. Direction: medium confidence. A new share/save burst landed on all 4 pages overnight, so every order ranks on reach, hold and burst-cleaned sends.
1. **Social studio: FILL the empty slots in the next 48 h (to 7:30 am ET Wed Oct 28).**
   - **0 Stories are queued on any page.** The last Story went out Oct 25; the cadence is 3–5 a day per page.
   - **Hourback:** no Reel Mon 8:45 or Tue 8:45, and no Tue feed post. (Sun 7 pm and Sun feed also went out empty.)
   - **Locked Hour:** no Tue 8:30 Reel and no Tue feed post.
   - Priority: LH Tue 8:30 Reel. LH morning Reels now win ~100 batches (floss 104, planning fallacy 105). Use a ≤15 s rule-as-fact open, no reassurance. Rollback record in docs/social-recovery/ as usual.
2. **Social studio (Fully Funded): MORE non-trial "trap rule with a date" Reels.** The TFSA re-contribution trap got 106 at 5 h and 5.0 s / 33%, FF's first double pass, after 3 Reels at 3–8. Drop `"trial": "auto"` from today's 8:15 am rule-of-72 Reel if it can still change before it publishes; FF trial median 21 vs 39 normal. Tue's two FF Reels are already non-trial. **Grade:** ≥60 at 5 h on Mon and Tue 7 pm.
3. **Short-form studio (Littlefold): KILL the reassurance open; keep the rule-as-fact open.** "It's OK to step away" won 148 strangers and held 2.5 s. "You can't spoil a newborn" held 4.99 s / 36% on 110, and coat held 5.6 s / 39%. The 4 queued LF Reels (burp halfway, baby nails, bath elbow, swaddle hips) are physical rules, so they fit. Check that each frame 0 states the rule, not a feeling. **Grade:** ≥5 s AND ≥30% on ≥100 reach.
4. **Social studio (Hourback): TEST HB morning Reels without the trial flag, with the action shown in frame 0.** HB 8:45 Reels since Oct 23 reached 4, 7 and 6. HB's only batch of 100 came from a normal 7 pm Reel (fridge 102), though it held 1.2 s. If the empty HB 8:45 slots are filled (order 1), run them non-trial. **Grade:** ≥20 at 15 h.
5. **Short-form studio: HOLD the on-screen send test. Don't add caption-only send lines as the fix.** Caption lines got 1 clean send on ~940 Reel reach over Oct 24–25. The 4 queued on-screen tests (Mon–Thu 7 pm) are the real test. Grade on Wed's read: ≥1 clean send per 50 reach.
6. **Automation architect:**
   - **A 6th burst** landed Oct 26 04:38 UTC: 56 posts on 4 pages gained ≈ +3 shares and +1 save each. Check whether Story reshares or Story link stickers are being counted as post shares.
   - An alert when a Reel has ≤5 reach at its first read.
   - Per-post lines in history.jsonl (day 11), comment text (day 12), and the per-post `follows` HTTP 400.

**Grading yesterday's orders (owner check):**
1. **Recover FF delivery: done.** The non-trial 7 pm Reel got 106 at 5 h (goal ≥20). Whether the account-status check happened: no data. The Mon 8:15 rule-of-72 Reel still carries the trial flag.
2. **Fill 4 Reel slots + HB feed: half done.** FF Mon 7 pm (cash at zero) and LH Mon 7 pm (print it) are filled. HB Sun 7 pm, HB Mon 8:45 and HB Sun feed went or will go out empty, and Stories were not refilled (0 queued).
3. **Concrete rule by second 2: on track.** Oct 25: FF TFSA passed both bars and LF "spoil" missed by 0.01 s. LF "step away" (reassurance) failed. The full grade comes on the Oct 26–27 Reels.
4. **On-screen send line: queued.** 4 tests Mon–Thu 7 pm (commit 3cc1efb). Grade Wed.
5. **≤5 slides: done.** The Oct 25 feed posts were 1–5 slides.
6. **Automation asks: not done.**

---

## Daily report: Mon Oct 26, 2026

### Scoreboard (insights read Oct 26 04:38 UTC)
Changes are vs the Oct 25 04:35 UTC read (1 day) and vs the Oct 19 04:37 UTC read (7 days). Sends and saves are burst-cleaned.

| Page | Followers (1d / 7d) | Feed posts 7d (slides) | Reels 7d | Median reach (all / Reels / feed) | Best by clean (saves+sends)/reach | Worst | Best by views | Worst by views |
|---|---|---|---|---|---|---|---|---|
| Fully Funded | 7 (+0 / −1) | 13 carousels (10, 10, 10, 9, 9, 8, 7, 7, 7, 7, 6, 5, 5 sl) | 13 | 9 / 23 / 6 | Carousel "cheap coat" (10 sl) 5/8 = 0.62 · best Reel "life insurance" 6/20 = 0.30 | Reel "Not married? No will?" 0/122 | Reel "Not married? No will?" 143 | Carousel "CPP enough?" (9 sl) 4 |
| Locked Hour | 4 (+0 / −2) | 13 carousels (10, 10, 10, 10, 10, 8, 7, 7, 7, 7, 6, 5, 3 sl) | 12 | 6 / 29 / 4 | Carousel "2 minutes to a locked hour" 1/5 = 0.20 · best Reel "Missed a day?" 5/31 = 0.16 | Reel "For every parent who gets interrupted" 0/109 | Reel "Everything takes longer than you think?" 129 | Carousel "Sunday scaries" (7 sl) 6 |
| Hourback | 5 (+0 / −1) | 12 carousels (10, 10, 9, 9, 9, 9, 7, 7, 7, 7, 7, 6 sl) | 12 | 7 / 12 / 3 | Carousel "what happens when you ask AI" 2/7 = 0.29 · best Reel: none scored | Reel "Open fridge, no plan?" 0/102 | Reel "Open fridge, no plan?" 108 | Carousel "25% faster" (6 sl) 3 |
| Littlefold | 6 (+0 / −1) | 14 (carousels 9, 9, 9, 8, 7, 7, 7, 7, 6, 6, 5, 3 sl; 2 singles) | 13 | 9 / 108 / 4 | Carousel "meltdown in the cereal aisle" 1/4 = 0.25 · best Reel "5-step game" 2/105 = 0.02 | Reel "It's OK to step away" 0/148 (burst window) | Reel "bonding bubble" 165 | Carousel "RESP catch-up" (8 sl) 7 |

**Total: 22 followers (+0 since yesterday's read, −5 vs Oct 19).** Flat for 12 reads (since Oct 23 04:35 UTC).
- **Yesterday's posts (Oct 25 ET, 11 posts: 7 Reels, 4 feed):**
  - Best by clean (saves + sends)/reach: none scored. The 3 7 pm Reels' 2–3 sends landed in the burst window.
  - Best on strangers: FF Reel "Put TFSA money back too soon?", 106 reach, 5.0 s / 33%.
  - Best by views: LF Reel "It's OK to step away", 158 views on 148 reach.
  - Worst: HB Reel "That sparkle button?", 6 reach at 15 h. HB had only 1 post (no feed, no 7 pm Reel).
- **Sum of post reach (1 day):** FF 940 → 1,077 (+137), LH 930 → 1,099 (+169), HB 584 → 601 (+17), LF 2,001 → 2,282 (+281).

### Patterns (all pages ≥5 posts)
- **Reels vs feed (high confidence on direction):** since Oct 19, Reels have a median reach of 31 (n=47) against 4 for feed posts (n=50). Batches of ≥100 are 93–96% non-follower.
- **Length (medium-high, n=47 Reels since Oct 19, ≥12 h old):**

  | Length | Median watch-through | Median seconds | Median reach | n |
  |---|---|---|---|---|
  | ≤15 s | 30% | 3.6 s | 31 | 30 |
  | 21–30 s | 22% | 5.5 s | 13 | 3 |
  | 30–40 s | 11% | 4.1 s | 44 | 14 |

- **Open type (medium-low, n=4 vs 4 on batches ≥100):** rule stated as a fact held 5.0–5.6 s (coat, toddler play, TFSA trap, spoil). Reassurance held 1.2–2.5 s (step away, fridge, new dad, bedtime).
- **Trial flag (medium):** since Oct 19, trial vs normal median reach is FF 21 vs 39, HB 10.5 vs 17.5, LH 105 vs 28.5 and LF 110 vs 105. Trials help LH mornings, do nothing on LF, and hurt FF and HB.
- **Topic and page (medium):** LF holds 11 of the 18 batches of ≥100 since Oct 19. Every page has now had at least one.
- **Posting time (low):** 7 pm Reels get the batch within 5 h. Morning trials build over 8–24 h (LH floss 58 → 104 between 15 h and 23 h; FF wills 9 → 31 between 8 h and 16 h).
- **Sends:** 1 clean send in the last 72 h (LH "Check the words"), across ~1,440 post reach.

### Comments
**No data yet.** 0 real comments. All 160 counted are our own first comments, and comment text has been empty for 12 days.

### Health
- **Published vs schedule:** all **345 of 345** entries due by the last state push (Oct 25 23:11 UTC) are published, with 0 failed, 0 errors and 0 comment errors. In the last 36 h, 30 entries went out 15–42 min late (worst: LH done-list carousel, 42 min; worst Reels: LH floss and planning fallacy, 38 min). All are inside one run cycle.
- **Next 48 h (to 7:30 am ET Wed Oct 28):**
  - **FF:** 4 Reels, 2 feed, **0 Stories**. Full apart from Stories.
  - **LF:** 4 Reels, 2 feed, **0 Stories**. Full apart from Stories.
  - **LH:** 3 Reels, 1 feed, **0 Stories**. **Empty:** the Tue 8:30 Reel and the Tue feed post.
  - **HB:** 2 Reels, 1 feed, **0 Stories**. **Empty:** the Mon 8:45 and Tue 8:45 Reels and the Tue feed post.
  - The schedule runs to Oct 29, 7 pm.
- **Delivery:** FF has recovered (106 at 5 h). No Reel had ≤5 reach at first read last night. HB morning Reels are still at 4–7.
- **Data:** all 40 insight reads in git succeeded, with no token or account errors. **Still broken:** comment text, follow_type, the per-post `follows` read (HTTP 400) and per-post lines in history.jsonl. **New:** a 6th share/save burst (order 6).

### For the Automation architect
- Find the source of the burst (6 windows now, all ≈ +3 shares and +1 save per post). Check Story reshares first.
- Alert when any Reel has ≤5 reach at its first read.
- Per-post lines in history.jsonl; reach with breakdown=follow_type; comment text; the per-post `follows` HTTP 400.

### Media kit
Updated (claude/media-kit.md).

---

## TEST-BATCH TABLE (Sun Oct 25, 2026, Performance desk)
Data: insights/latest.json, collected **Oct 25 04:35 UTC (12:35 am ET)**. Per-post curves are rebuilt from all **43** reads in git (Oct 15 03:45 → Oct 25 04:35 UTC). Reel lengths come from ffprobe on the MP4 each schedule entry points to. The next read is ~12:40 UTC (8:40 am ET).
- **Verdict rules (unchanged):**
  - EXPANDED: reach still climbing after 24 h (≥ +25% and ≥ +10) AND sends/reach in the top third.
  - STALLED: flat after 24 h.
  - FAILED HOOK: average watch under 4 s, or under 25% of the Reel's length.
  - PENDING: under 24 h old.
- **Non-follower share** is a floor: (reach − current followers) / reach. follow_type is still not read, and the per-post `follows` read still returns HTTP 400 on every post.
- **No burst in the last 8 reads** (since Oct 23 12:41 UTC). Sends and saves have all 5 burst windows removed (Oct 15 20:30, Oct 19 20:36, Oct 21 12:44, Oct 22 04:35 and Oct 23 04:35 UTC).
- **Comments per reach = 0 everywhere.** There are 154 comments on 154 posts, and all are our own first comments. Two posts show 2 comments, but no text came back. Comment text has been empty for 11 days.

| Page | Post (first line) | Format | Age | Reach curve (age → reach) | Non-follower ≥ | Sends/reach (clean) | Saves/reach (clean) | Avg watch / length | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LF | "Sore gums tonight? A cold cloth and a gentle rub." | Reel 11.7 s (trial) | 16 h | 4h 57 → 8h 122 → 16h 124 | 95% | 0.00 | 0.00 | 2.6 s / 22% | FAILED HOOK + PENDING |
| LF | "Bedtime turned into a battle again? …best 20 minutes" | Reel 14.4 s (trial) | 41 h | 5h 28 → 17h 50 → 25h 107 → 41h 108 | 94% | 0.00 | 0.00 | 2.4 s / 17% | FAILED HOOK + STALLED |
| LH | **"Studying with your playlist on? Check the words."** | Reel 13.2 s | 5 h | 5h **105** | 96% | **0.01 (1)** | 0.00 | **4.6 s / 35%** | PENDING. Passes both FAILED HOOK bars. LH's biggest 5 h batch ever. **The only clean send in 2 days** |
| LF | "Sleep and screens by age, Canada edition 🇨🇦" | Reel 11.6 s (trial) | 63 h | 4h 100 → 24h 103 → 63h 103 | 94% | 0.00 | 0.00 | 3.4 s / 30% | FAILED HOOK (by s) + STALLED |
| LF | "New dad, feeling left out? You don't need to feed the baby to bond…" | Reel 14.2 s | 5 h | 5h 102 | 94% | 0.00 | 0.00 | 2.4 s / 17% | FAILED HOOK + PENDING |
| LF | "First cold morning? Coat off, then buckle." | Reel 14.4 s | 29 h | 5h 81 → 21h 102 → 29h 102 | 94% | 0.00 | 0.00 | **5.2 s / 36%** | STALLED. Hook bars passed, 0 sends |
| HB | "Open fridge, no plan? You already have dinner." | Reel 14.0 s (send-test control) | 5 h | 5h **101** | 95% | 0.00 | 0.00 | **0.8 s / 6%** | FAILED HOOK + PENDING. **HB's biggest batch ever, lost in under 1 s** |
| LH | "New habit keeps not sticking? Floss before or after brushing…" | Reel 13.7 s (trial) | 15 h | 3h 27 → 7h 39 → 15h 58 | 93% | 0.00 | 0.00 | 3.1 s / 23% | FAILED HOOK + PENDING, still climbing |
| LH | "Coffee at 4 pm? Your sleep noticed, even if you didn't." | Reel 13.9 s | 29 h | 5h 13 → 21h 33 → 29h 37 | 89% | 0.00 | 0.00 | 2.8 s / 20% | FAILED HOOK + STALLED |
| FF | "Spend the refund, or turn it into $29,000?" | Reel 13.7 s | 53 h | 5h 11 → 21h 20 → 53h 23 | 70% | 0.00 | 0.00 | 2.2 s / 16% | FAILED HOOK + STALLED |
| LH | "Can't crack it at your desk? Stand up." | Reel 14.0 s | 53 h | 5h 8 → 21h 22 → 53h 23 | 83% | 0.00 | 0.00 | 2.7 s / 19% | FAILED HOOK + STALLED |
| FF | "TFSA vs RRSP vs FHSA, in one look 🇨🇦" | Reel 11.3 s (trial) | 64 h | 4h 8 → 24h 16 → 64h 17 | 59% | 0.00 | 0.00 | 4.1 s / 36% | STALLED, no stranger batch |
| HB | "Skimming just the AI summary? Apple's AI wrote a headline…" | Reel 13.6 s | 29 h | 5h 12 → 21h 15 → 29h 15 | 67% | 0.00 | 0.00 | 2.5 s / 19% | FAILED HOOK + STALLED |
| HB | "Charges you forgot you pay. Everyone has a few 🙈" | Reel 15.0 s (trial) | 63 h | 4h 0 → 24h 10 → 63h 11 | 55% | 0.00 | 0.00 | 12.0 s (rewatches, likely followers) | STALLED, no stranger batch |
| FF | "Too sick to work for months? Here's what EI pays." | Reel 13.4 s (trial) | 16 h | 4h 3 → 16h 8 | 12% | 0.00 | 0.00 | 1.8 s / 13% | FAILED HOOK + PENDING. **Near-zero delivery** |
| HB | "3-minute voice note, mid-meeting? WhatsApp can turn it into text" | Reel 13.2 s (non-trial test) | 15 h | 3h 5 → 15h 6 | 17% | 0.00 | 0.00 | 1.5 s / 11% | FAILED HOOK + PENDING |
| LH | "Can't make yourself go to the gym? …" | Reel 11.9 s (trial) | 63 h | 4h 0 → 24h 5 → 63h 5 | 20% | 0.00 | 0.00 | 16.2 s (rewatches) | STALLED, no stranger batch |
| FF | "Your TFSA, after you die? If nobody is named on it…" | Reel 13.5 s | 5 h | 5h **4** | 0% | 0.00 | 0.00 | 1.6 s / 12% | PENDING. **Near-zero delivery** (same-minute siblings got 101–105) |
| FF | "Your parents taking CPP early? Here's what 60, 65 and 70 pay." | Reel 13.0 s | 29 h | 5h 0 → 21h 3 → 29h 3 | 0% | 0.00 | 0.00 | 4.7 s (3 viewers) | STALLED. **Near-zero delivery** |
| HB | "Weird light on your dashboard? Point your camera…" | Reel 14.3 s (trial) | 39 h | 3h 1 → 23h 3 → 39h 3 | 0% | 0.00 | 0.00 | 5.3 s (3 viewers) | STALLED, no stranger batch |

**Feed posts in the window (24 carousels and 1 single):** all STALLED or PENDING at reach **0–13**, with 0 clean sends and 0 clean saves. The best was LH "Rereading the same line" (10 slides) at 13. The 8 Oct 24 feed posts (1–9 slides) reached 0–4.

**EXPANDED: 0 of 154.** What moved since yesterday:
1. **Fully Funded has stopped getting stranger batches.** Its last 3 Reels reached 3, 8 and 4, with about 0% non-followers. Every FF 7 pm Reel from Oct 17 to Oct 22 had 11–61 at 5 h. Last night LH, LF and HB Reels published in the same minute got 101–105, while FF got 4. FF's account reach rose +27 in 24 h; LF's rose +314. The MP4 specs match the siblings (h264 1080×1920, 30 fps, AAC stereo) and so does the caption shape (5 hashtags, a "Send this to…" line). So the file and the caption don't explain it. **The likely cause is recommendation eligibility, which only the account owner can see** (see the ACTION line). This is an inference, not a confirmed cause.
2. **Three 7 pm Reels each won a ~100-stranger batch in 5 h** (LH 105, LF 102, HB 101). HB and LH have never had a batch this size so early. Holds decided the outcome:
   - LH "Check the words" held 4.6 s / 35%. It's a concrete check you can picture, and it earned the only send.
   - LF "New dad, feeling left out?" held 2.4 s. It's reassurance, with no action shown.
   - HB "Open fridge, no plan?" held 0.8 s, the worst hold ever on a batch over 40.
3. **The send-trigger test is failing so far.** The 7 Oct 24 Reels with a "Send this to…" line reached 407 people and got 1 clean send. The control (HB fridge) reached 101 and got 0. The goal was ≥1 clean send per 50 reach; the result is 1 per 407. The 16 feed posts with the line got 0 sends. The Oct 25 Reels are graded at Monday's read.
4. **The non-trial HB morning test lost.** HB voice notes went out at 8:45 without the trial flag and reached 6 at 15 h, against an HB trial median of 11.

- **TikTok:** manual (no API; no numbers logged).
- **YouTube Shorts:** no data yet. vidIQ checked this run: signed in as the Steadfold Gmail, with **0 YouTube channels** and **0 Instagram accounts** connected.
- **Trial Reels:** 31 measured. Graduation to followers: **no data yet** (not in the API).

**3 orders**
1. **REPEAT:** a concrete check or rule you can picture, shown by second 2, at ≤15 s. LH "Check the words" held 4.6 s / 35% on 105 and earned a send. LF "Coat off, then buckle" held 5.2 s / 36% on 102.
2. **KILL:** reassurance and "you already have it" opens on big batches: HB fridge 0.8 s on 101, LF new dad 2.4 s on 102, LF "best 20 minutes" 2.4 s on 108. Also the trial flag on FF morning Reels: since Oct 19, FF trial Reels reached 8–29 (median 18.5), against 23–122 for normal FF Reels.
3. **TEST:** a send-native frame 0 that names the person to send it to inside the hook, not in the caption ("For the friend who still studies with lyrics on"). Run it on 1 Reel per page, Oct 26–27. Caption-only send lines got 1 send on 407 reach.

## Today's orders (Sun Oct 25, 2026, Performance desk)
Data: the Oct 25 04:35 UTC read, with 43 reads of per-post curves. 154 posts (71 Reels, 83 feed), 22 followers. Direction: medium confidence. No burst in the last 8 reads.
1. **Social studio (Fully Funded) + Dharma: RECOVER FF delivery.** FF's last 3 Reels reached 3, 8 and 4 (about 0% non-follower), while same-minute siblings on the other pages got 101–105.
   - **Dharma (2 min):** in the Instagram app, open @fullyfundedhq → Settings → Account status, and check "Content that can't be recommended" or any recommendation flag.
   - **Social studio:** until that's checked, run FF's next 2 Reels **without** the trial flag. Today's ff-pan-1025am-paycheque-trail and tomorrow's ff-reel-1026am-rule-of-72 both carry `"trial": "auto"`. Use FF's proven batch shapes: a cost-of-waiting number (one-year wait, 104) or the wills question (122).
   - **Grade:** ≥20 reach at 5 h on the Sun 7 pm FF Reel.
2. **Social studio: FILL 4 empty Reel slots and 1 feed slot in the next 48 h.**
   - Reel slots: HB Sun 7 pm, HB Mon 8:45 am, FF Mon 7 pm and LH Mon 7 pm.
   - Feed slot: HB has no feed post on Sun (the week card was held). HB also has 0 Stories queued for Sun and Mon.
   - Priority: HB 7 pm Sun. HB's 7 pm slot just won a 101-stranger batch, so give it a concrete-action open, not a reassurance line.
   - Write a rollback record in docs/social-recovery/ as usual.
3. **Short-form studio (all pages): REPEAT a concrete check or rule shown by second 2; KILL reassurance opens.**
   - On ~100-stranger batches, LH "Check the words" held 4.6 s / 35% and LF "Coat off, then buckle" held 5.2 s / 36%.
   - Over the same week, HB "You already have dinner" held 0.8 s, LF "You don't need to feed the baby to bond" held 2.4 s, and LF teething held 2.6 s on 124.
   - Since Oct 19, ≤15 s Reels hold a median 27% (n=22), so length is solved; frame 0 is the lever.
   - **Grade:** ≥5 s and ≥30% on ≥40 reach on the Oct 26–27 Reels.
4. **Short-form studio: TEST the send line on screen, inside the hook.** Caption-only "Send this to…" lines got 1 clean send on 407 Reel reach (goal: 1 per 50) and 0 on 16 feed posts.
   - On 1 Reel per page, Oct 26–27, frame 0 names the person: "For the friend who…" or "Send this to whoever…".
   - The LH "For every parent who…" callout already won 109 strangers (0 sends). Add the explicit send ask on screen as the last beat.
   - **Grade:** ≥1 clean send per 50 reach.
5. **Social studio (all pages): HOLD feed at ≤5 slides. This order is done, so keep it.** Feed posts from Oct 19 to 25 had a median reach of **4** (n=48), against **29** for Reels (n=43). The Oct 25–26 carousels are now 1–5 slides.
6. **Automation architect:**
   - an alert when any Reel has ≤5 reach at its first read (FF has now had 3 in a row);
   - per-post lines in history.jsonl (day 10);
   - comment text (day 11);
   - the per-post `follows` HTTP 400.

**Grading yesterday's orders (owner check):**
1. **Fix the zero-delivery FF CPP Reel: not done, and the problem spread.** The CPP Reel has 3 reach at 29 h and was not re-queued. The next 2 FF Reels reached 8 and 4 (order 1).
2. **Felt question → physical rule, ≤15 s: done in form, mixed results.** LH lyrics 4.6 s / 35% on 105 (passes the FAILED HOOK bars, short of 5 s). LF coat held up at 5.2 s / 36% on 102. Teething (2.6 s), new dad (2.4 s) and fridge (0.8 s) failed. 0 new Reels passed ≥5 s AND ≥30% on ≥40.
3. **Hold the send-trigger test: done.** So far it has 1 clean send per 407 reach against a goal of 1 per 50. The final grade comes Monday with the Oct 25 Reels.
4. **MORE batch winners: half done.** LF kept 2 Reels a day (124 and 102). The FF wills ≤15 s Trial Reel isn't in the schedule; Sun 8:15 is the paycheque trail instead.
5. **≤5 slides: done.** Oct 25 FF tfsa-room and LH done-list are now 5 slides each, and Oct 26 feed posts are 1–3 slides.
6. **Automation asks: not done.** history.jsonl still has account lines only, and comment text is still empty.

---

## Daily report: Sun Oct 25, 2026

### Scoreboard (insights read Oct 25 04:35 UTC)
Changes are vs the Oct 24 04:33 UTC read (1 day) and the Oct 18 04:31 UTC read (7 days). Sends and saves are burst-cleaned.

| Page | Followers (1d / 7d) | Feed posts 7d (slides) | Reels 7d | Median reach (all / Reels / feed) | Best by clean (saves+sends)/reach | Worst | Best by views | Worst by views |
|---|---|---|---|---|---|---|---|---|
| Fully Funded | 7 (+0 / −1) | 14 (carousels 10, 10, 10, 10, 9, 9, 8, 8, 7, 7, 7, 7, 6, 5 sl) | 13 | 9 / 23 / 6.5 | Carousel "hold the dots and slide" 3/12 = 0.25 · best Reel: none scored | Reel "Not married? No will?" 0/122 | Reel "Not married? No will?" 143 | Carousel "2% fee… $394,000" (6 sl) 1 (7 h) |
| Locked Hour | 4 (+0 / −2) | 14 (carousels 10, 10, 10, 10, 10, 8, 7, 7, 7, 7, 6, 6, 3 sl; 1 n/a) | 12 | 11.5 / 27.5 / 3.5 | Carousel "can't focus? follow the line" 5/12 = 0.42 · best Reel "Check the words" 1/105 = 0.01 | Reel "For every parent who gets interrupted" 0/109 | Reel "Check the words" 118 | Carousel "Sunday scaries" (7 sl) 1 |
| Hourback | 5 (+0 / −1) | 14 (carousels 10, 10, 9, 9, 9, 9, 7, 7, 7, 7, 7, 6, 6, 3 sl) | 13 | 9 / 15 / 3.5 | Carousel "everything you paste into an AI chat leaves your phone" 4/10 = 0.40 · best Reel: none scored | Reel "Open fridge, no plan?" 0/101 | Reel "Open fridge, no plan?" 104 | Carousel "bank texts 'Was this you?'" (9 sl) 0 |
| Littlefold | 6 (+0 / +0) | 14 (carousels 9, 9, 9, 8, 7, 7, 7, 7, 7, 6, 6, 5, 4 sl; 1 single) | 13 | 15 / 108 / 4.5 | Carousel "baby has a fever? follow the line" 3/6 = 0.50 · best Reel: none scored | Reel "bonding bubble" 0/134 | Reel "bonding bubble" 165 | Single "Small Wins No.2" 1 (7 h) |

Every "best by ratio" is a 1-week-old carousel on reach of 6–12. **Since Oct 23, every post on every page has 0 clean saves, and the only clean send is LH "Check the words".**

**Total: 22 followers (+0 since yesterday's read, −4 vs Oct 18).** The drop came on Oct 21–22 (28 → 16), followed by a partial recovery to 22. Flat for 8 reads.
- **Yesterday's posts (Oct 24 ET, 16 posts: 8 Reels, 8 feed):**
  - Best by clean (saves + sends)/reach: LH Reel "Studying with your playlist on? Check the words.", 1/105 = 0.01. It's the only post that scored.
  - Best by views: LF Reel "Sore gums tonight? A cold cloth and a gentle rub.", 139 views on 124 reach.
  - Worst: FF Reel "Your TFSA, after you die?", 4 reach, and HB carousel "bank texts" (9 slides), 0.
- **Sum of post reach (1 day):** FF 913 → 940 (+27), LH 734 → 930 (+196), HB 466 → 584 (+118), LF 1,687 → 2,001 (+314). Some of these totals include new posts.

### Patterns (all pages ≥5 posts)
- **Reels vs feed, non-follower reach (high confidence on direction):** from Oct 19 to 25, Reels had a median reach of 29 (n=43) and feed posts a median of 4 (n=48). Stranger batches of ≥80 are 93–96% non-follower.
- **Length (medium-high, n=39 Reels since Oct 19, ≥12 h old):**

  | Length | Median watch-through | Median seconds | Median reach | n |
  |---|---|---|---|---|
  | ≤15 s | 27% | 3.3 s | 26 | 22 |
  | 21–30 s | 22% | 5.5 s | 12 | 3 |
  | 30–40 s | 11% | 4.1 s | 44 | 14 |

  Seconds watched stay at about 3–4 s whatever the length.
- **Open type (medium-low, n=4 vs 4 on batches ≥80):**
  - **Concrete check or rule, shown:** coat 5.2 s, toddler play 5.5 s, "check the words" 4.6 s.
  - **Reassurance or abstract promise:** fridge 0.8 s, new dad 2.4 s, bedtime 2.4 s, teething 2.6 s.
  - **🇨🇦 cheat sheets:** 3.4 s.
- **Topic and page (medium):** LF holds 10 of the 15 batches of ≥100 this week. HB (101) and LH (105) reached 100 at 5 h for the first time last night. FF fell from a 7 pm median of 27 at 5 h (Oct 17–22) to 0–4 (Oct 23–24).
- **Trial flag (medium-low):** since Oct 19, the median reach of trial vs normal Reels is FF 18.5 vs 63, LH 16 vs 23, HB 11 vs 15 and LF 104 vs 104. The flag hasn't won a bigger batch on any page.
- **Posting time (low):** the 7 pm slot won all 3 of last night's ~100 batches within 5 h. Morning batches build over 8–24 h (teething 57 → 122, floss 27 → 58).
- **Sends:** 2 clean sends from Oct 19 to 25 across 2,438 post reach.

### Comments
**No data yet.** 0 real comments. All 154 counted are our own first comments, and comment text has been empty for 11 days.

### Health
- **Published vs schedule:** all **320 of 320** entries due by the last state push (Oct 24 23:20 UTC) are published, with 0 failed, 0 errors and 0 comment errors.
  - In the last 36 h, 32 entries went out more than 15 min late. The worst is an HB Story (hb-ch-1023-2) at 67 min; the worst Reel is LH floss at 38 min.
- **Delivery:** 3 FF Reels in a row got ≤8 reach (order 1).
- **Next 48 h (to 7:30 am ET Tue Oct 27):**
  - **FF:** 3 Reels, 2 feed posts, 5 Stories. **Empty:** the Mon 7 pm Reel.
  - **LH:** 3 Reels, 2 feed posts, 5 Stories. **Empty:** the Mon 7 pm Reel.
  - **HB:** 2 Reels, 1 feed post, **0 Stories**. **Empty:** the Sun 7 pm Reel, the Mon 8:45 am Reel and Sun feed.
  - **LF:** full, with 4 Reels, 3 feed posts and 4 Stories.
  - All media files exist. The schedule runs to Oct 28, 5:45 pm.
- **Data:** all 43 insight reads succeeded, with no token or account errors.
  - **Still broken:** comment text, the follow_type split, the per-post `follows` read (HTTP 400) and per-post lines in history.jsonl.

### 4-week trend (Sunday)
The pages launched Oct 13, so 2 weeks exist. Reach is per-post reach as of today's read.

| Week (ET) | Followers (end) | Posts (feed / Reels) | Sum of post reach | Median Reel reach | Median feed reach | Clean sends | Reels with ≥100 reach | Reels passing ≥5 s AND ≥30% on ≥40 | Best Reel hold on ≥40 |
|---|---|---|---|---|---|---|---|---|---|
| Sep 28 | no data yet | | | | | | | | |
| Oct 5 | no data yet | | | | | | | | |
| Oct 12 (Oct 13–18) | 26 | 35 / 28 | 2,017 | 50 | 10 | 19 (before burst checks began) | 5 | 0 | 5.1 s (FF fee, 44) |
| **Oct 19 (Oct 19–24)** | **22** | 48 / 43 | 2,438 | 29 | 4 | **2** | **15** | **2** | 6.6 s (LF newborn cues, 136) |

Median Reel reach by page, week 1 → week 2: FF 46 → 22, LH 46 → 26.5, HB 20 → 12, LF 113 → 105.

**The single biggest lever for next week: frame 0 on the ~100-stranger batches we already win.** We got 3× more 100+ batches this week (15 vs 5), but every one stopped at 100–144, because strangers left in 0.8–3.4 s and nobody sent anything. The only two Reels that passed both hold bars, plus the only Reel that earned a send, all showed a concrete rule or check being done by second 2. Make that the default open on every 7 pm Reel, and put the send ask on screen. Recovering FF's delivery comes second (order 1).

### For the Automation architect
- Alert when any Reel has ≤5 reach at its first read.
- Per-post lines in history.jsonl (shares, saved, likes, reach, avg watch).
- Reach with breakdown=follow_type.
- Comment text.
- The per-post `follows` HTTP 400.

### Media kit
Updated (claude/media-kit.md).

---

## TEST-BATCH TABLE (Sat Oct 24, 2026, Performance desk)
Data: insights/latest.json, collected **Oct 24 04:33 UTC (12:33 am ET)**. Per-post curves rebuilt from the **26** reads in git (Oct 18 04:32 → Oct 24 04:33 UTC). Reel lengths come from ffprobe on the current MP4s. Next read ~12:40 UTC (8:40 am ET).
- **Verdict rules (unchanged):** EXPANDED = reach still climbing after 24 h (≥ +25% and ≥ +10) AND sends/reach in the top third. STALLED = flat after 24 h. FAILED HOOK = average watch under 4 s or under 25% of length. PENDING = under 24 h.
- **Non-follower share** is a floor: (reach − current followers) / reach. follow_type is still not read, and the per-post `follows` read still fails with HTTP 400 on every post.
- **No burst in the last 4 reads** (Oct 23 12:41 → Oct 24 04:33 UTC), so the Oct 23 numbers are clean. Sends and saves below have all 4 burst windows removed (Oct 19 20:36, Oct 21 12:44, Oct 22 04:35, Oct 23 04:35 UTC). Since Oct 19 there has been **1 clean send across 75 posts** and about 1,600 Reel reach.
- **⚠ FF "Your parents taking CPP early?" (7 pm Fri) has 0 views and 0 reach at 5 h.** The 3 Reels published in the same minute got 12–81. This is the first Reel with zero delivery. See the ACTION line and order 1.
- **Comments per reach = 0 everywhere.** 138 comments across 138 posts, all our own first comments. LH "Rereading the same line" shows 2, so 1 may be real, but no text came back. Comment text is still empty (day 10).

| Page | Post (first line) | Format | Age | Reach curve (age → reach) | Non-follower ≥ | Sends/reach (clean) | Saves/reach (clean) | Avg watch / length | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LF | "Toddler pulling you to come play? Give them 10 minutes where they lead" | Reel 14.2 s | 53 h | 5h 22 → 21h 71 → 29h 102† → 45h 104 → 53h 104 | 94% | 0.00 | 0.00 | **5.5 s / 39%** | STALLED at 45 h. Hold bars passed, 0 sends |
| FF | "What waiting just one year costs you by 65 🇨🇦" | Reel 11.6 s | 53 h | 5h 27 → 21h 77 → 29h 101† → 53h 103 | 93% | 0.00 | 0.00 | 3.5 s / 30% | FAILED HOOK (by s) + STALLED |
| LF | "Sleep and screens by age, Canada edition 🇨🇦" | Reel 11.6 s (trial) | 39 h | 4h 100 → 24h 103 → 39h 103 | 94% | 0.00 | 0.00 | 3.4 s / 30% | FAILED HOOK (by s) + STALLED |
| LF | **"First cold morning? Coat off, then buckle. The warm layer goes on top"** | Reel 14.4 s | 5 h | 5h **81** | 93% | 0.00 | 0.00 | **5.5 s / 38%** | PENDING. **2nd Reel ever to pass both hold bars on ≥40** |
| LF | "Money your family can get in Canada, for each child 🇨🇦" | Reel 11.6 s (trial) | 64 h | 4h 9 → 24h 47 → 64h 53 | 89% | 0.00 | 0.00 | 2.9 s / 25% | FAILED HOOK + STALLED |
| LF | "Bedtime turned into a battle again? Turn it into the best 20 minutes…" | Reel 14.4 s (trial) | 17 h | 5h 28 → 9h 42 → 17h 50 | 88% | 0.00 | 0.00 | **1.7 s / 12%** | FAILED HOOK + PENDING |
| LH | "Missed a day? Don't start over. The research is on your side." | Reel 13.9 s | 53 h | 5h 15 → 21h 19 → 45h 30 → 53h 30 | 87% | 0.00 | 0.00 | 4.3 s / 31% | Reach climbed after 24 h (+11, +58%) but 0 clean sends, so not EXPANDED. Now STALLED |
| FF | "A 1% fee sounds tiny. Here's what it takes 🇨🇦" | Reel 12.2 s (trial) | 64 h | 4h 16 → 24h 23 → 64h 27 | 74% | 0.00 | 0.00 | 2.5 s / 20% | FAILED HOOK + STALLED |
| LH | "Can't crack it at your desk? Stand up." | Reel 14.0 s | 29 h | 5h 8 → 21h 22 → 29h 23 | 83% | 0.00 | 0.00 | 2.7 s / 19% | FAILED HOOK + STALLED |
| FF | "Spend the refund, or turn it into $29,000?" | Reel 13.7 s | 29 h | 5h 11 → 21h 20 → 29h 22 | 68% | 0.00 | 0.00 | 2.2 s / 16% | FAILED HOOK + STALLED |
| FF | "TFSA vs RRSP vs FHSA, in one look 🇨🇦" | Reel 11.3 s (trial) | 40 h | 4h 8 → 24h 16 → 40h 16 | 56% | 0.00 | 0.00 | 4.3 s / 38% | STALLED, no stranger batch |
| LH | "Coffee at 4 pm? Your sleep noticed, even if you didn't." | Reel 13.9 s | 5 h | 5h 13 | 69% | 0.00 | 0.00 | 3.9 s / 28% | FAILED HOOK (by s) + PENDING |
| HB | "Skimming just the AI summary? Apple's AI wrote a headline. It was false." | Reel 13.6 s | 5 h | 5h 12 | 58% | 0.00 | 0.00 | 2.0 s / 15% | FAILED HOOK + PENDING |
| HB | "Set it up once. Never chase it again 🇨🇦" | Reel 25.1 s (trial) | 64 h | 4h 3 → 24h 11 → 64h 12 | 58% | 0.00 | 0.00 | 5.9 s / 24% | FAILED HOOK (by %) + STALLED |
| HB | "Charges you forgot you pay. Everyone has a few 🙈" | Reel 15.0 s (trial) | 39 h | 4h 0 → 24h 10 → 39h 11 | 55% | 0.00 | 0.00 | 12.0 s (rewatches, likely followers) | STALLED, no stranger batch |
| HB | "Engineers pasted secret code into ChatGPT." | Reel 13.5 s | 53 h | 5h 6 → 21h 7 → 53h 9 | 44% | 0.00 | 0.00 | 8.1 s / 60% | STALLED, no stranger batch |
| LH | "Can't make yourself go to the gym? Make the gym the only place…" | Reel 11.9 s (trial) | 39 h | 4h 0 → 24h 5 → 39h 5 | 20% | 0.00 | 0.00 | 16.2 s (rewatches, followers) | STALLED, no stranger batch |
| HB | "Weird light on your dashboard? Point your camera, ask out loud…" | Reel 14.3 s (trial) | 15 h | 3h 1 → 7h 3 → 15h 3 | ~0% | 0.00 | 0.00 | 5.3 s / 37% (3 viewers) | PENDING, no stranger batch |
| FF | "Your parents taking CPP early? Here's what 60, 65 and 70 pay." | Reel 13.0 s | 5 h | 5h **0** (0 views) | n/a | n/a | n/a | n/a | **NO DELIVERY** (order 1) |

† = the reach jump landed in the burst #4 window.

**Feed posts in the window (24 carousels):** all STALLED or PENDING at reach **0–11**, with 0 clean sends and 0 clean saves.
- The best were FF "$2,000 toward your child's education" (10 slides) at 11 and LH "Rereading the same line" (10 slides) at 9.
- The 8 Oct 23 carousels (5–10 slides) reached 0–9, median 1.5.

**EXPANDED: 0 of 138.** What moved since yesterday:
1. **The toddler-play pattern repeated.** LF "First cold morning? Coat off, then buckle" held 5.5 s and 38% on 81 strangers in 5 h. It's the 2nd ≤15 s Reel to pass both hold bars; the 1st was toddler play (5.5 s, 39% on 104). Both open on a felt question, then **one physical rule you can see being done**.
   - Same shape, abstract rule: LF "Bedtime turned into a battle? Turn it into the best 20 minutes" held **1.7 s** on 50.
   - My read is that the rule has to be concrete enough to picture. That's an inference from n = 2 wins and 1 loss, so low confidence.
2. **Big batches stop at about 100–135.** Every LF and FF batch ≥100 flattened by about 45 h. None got a second push, because none got sends.
3. **Sends are still the wall:** 1 clean send since Oct 19. The send-trigger test starts today (order 3).
4. **The LH/HB morning trials are still dead:** HB dashboard 3 at 15 h, LH gym 5 at 39 h. Today's HB 8:45 Reel runs without the trial flag (yesterday's order 4).

- **TikTok:** manual (no API; no numbers logged).
- **YouTube Shorts:** no data yet. vidIQ checked this run: signed in as the Steadfold Gmail, **0 YouTube channels** and **0 Instagram accounts** connected.
- **Trial Reels:** 27 measured. Graduation to followers: **no data yet** (not in the API).

**3 orders**
1. **REPEAT:** a felt question, then one physical rule shown being done, at ≤15 s. Toddler play got 5.5 s / 39% on 104, and cold-morning coat got 5.5 s / 38% on 81.
2. **KILL:** abstract-promise rules ("the best 20 minutes", 1.7 s) and 🇨🇦 cheat-sheet opens (2.5–3.5 s on 27–103). Also 9–10 slide carousels: 8 on Oct 23 had median reach 1.5.
3. **TEST:** the send trigger, now live. 13 of the 16 Reels on Oct 24–25 carry a "Send this to…" line. HB fridge-dinner, LF crying-peak and HB week-card don't, so they are the control. **Grade at the Sun and Mon reads:** ≥1 clean send per 50 reach.

## Today's orders (Sat Oct 24, 2026, Performance desk)
Data: Oct 24 04:33 UTC read, 26 reads of per-post curves. 138 posts (63 Reels, 75 feed), 22 followers. Direction: medium confidence. No burst in the last 4 reads.
1. **Social studio + Automation architect: FIX the zero-delivery FF Reel.** "Your parents taking CPP early? Here's what 60, 65 and 70 pay." (ff-reel-1023-cpp-60-or-70, https://www.instagram.com/reel/De2uajggV1l/) has 0 views and 0 reach at 5 h. HB, LF and LH Reels published in the same minute (23:20 UTC) got 12, 81 and 13.
   - **Check:** at the 8:40 am read, compare its MP4 (codec, audio, length) with the 3 siblings.
   - **If it's still 0:** re-queue it under a new id in an open FF slot, with a rollback record. Never delete the old one (repo rule).
   - **Context:** CPP is FF's topic of the week, with 2 CPP carousels at reach 1.
2. **Short-form + Social studio (all pages): REPEAT "felt question → one physical rule shown being done", ≤15 s.**
   - It worked twice: LF toddler play 5.5 s / 39% on 104, and LF cold-morning coat 5.5 s / 38% on 81 in 5 h.
   - It failed when the rule was abstract: LF bedtime "best 20 minutes" held 1.7 s / 12% on 50.
   - **For FF/LH/HB this means:** show the action (the form field, the phone setting, the hand on the timer) by second 2, not just the claim.
   - **Grade:** ≥5 s and ≥30% on ≥40 reach.
3. **Short-form studio: HOLD the send-trigger test as built.** 13 of the 16 Reels on Oct 24–25 carry "Send this to…" in the caption. HB fridge-dinner (7 pm Sat), LF crying-peak (8 am Sun) and HB week-card (7 pm Sun) don't, so leave those three as the control. I checked captions only; please confirm the line is also the last on-screen beat. **Grade:** ≥1 clean send per 50 reach (baseline: 1 clean send since Oct 19).
4. **Social studio (Fully Funded, Littlefold): MORE of the batch winners, recut tight.** FF's 3 biggest batches are wills 121, one-year cost 103 and car repair 81. The wills ≤15 s Trial Reel runs Sun 8:15 am. LF won 8 of the 10 biggest batches on any page. Keep LF at 2 Reels a day: every LF Reel since Oct 19 reached ≥50, and the median is 104.
5. **Social studio (all pages): LESS 9–10 slide carousels, day 5.** The 8 Oct 23 carousels reached 0–9 (median 1.5), and the 7-day feed medians are 4–8 against Reel medians of 17–105.
   - Oct 24 is better (3–9 slides).
   - Oct 25 still has FF tfsa-room (9 slides) and LH done-list (10 slides). Cut them to ≤5 slides, or turn one into a Reel.
6. **Automation architect:**
   - per-post lines in history.jsonl (day 9);
   - comment text (day 10);
   - the per-post `follows` HTTP 400;
   - the Publish Ledger's 2 HIGH findings on lh-pan-1021am-follow-the-line (day 4): its media id is shared with lh-1018-follow-the-line, so it was most likely never published.
   - New: alert when any Reel has 0 views at its first read.

**Grading yesterday's orders (owner check):**
1. **Fill the 5 empty Reel slots: 3 of 5.** LF 7 pm Fri got coat-off-buckle (81 reach, the day's best), LF 8 am Sat got teething, and HB 8:45 am Sat got voice transcripts. FF 8:15 am and LH 8:30 am Fri stayed empty. The LH follow-the-line re-id: **not done** (day 4).
2. **Toddler-play structure on 1 Reel per page, Oct 24–25: done in form.** All 4 pages queue felt-question + fix opens (teething, EI sick pay, floss, voice notes, TFSA trap). The first proof landed early: coat-off-buckle.
3. **Send trigger on 1 Reel per page: done, and more.** 13 of 16 Reels carry it in the caption, and 10 of 12 feed posts do too.
4. **One LH/HB 8 am Reel without the trial flag: done.** HB voice transcripts goes out today at 8:45 as a normal Reel. Graded Sun against HB's trial median of 11 (non-trial median 19).
5. **LESS 7–10 slide carousels: partly done.** Oct 23 ran 5–10 slides; Oct 24 runs 3–9; Oct 25 has a 9 and a 10.
6. **Burst logging: not done.** history.jsonl still has account lines only.

---

## Daily report: Sat Oct 24, 2026

### Scoreboard (insights read Oct 24 04:33 UTC)
Changes are vs the Oct 23 04:35 UTC read (1 day) and the Oct 17 04:32 UTC read (7 days). Sends and saves are burst-cleaned.

| Page | Followers (1d / 7d) | Feed posts 7d (slides) | Reels 7d | Median reach (all / Reels / feed) | Best by clean (saves+sends)/reach | Worst | Best by views | Worst by views |
|---|---|---|---|---|---|---|---|---|
| Fully Funded | 7 (+0 / +4) | 14 (carousels 10, 10, 10, 10, 9, 9, 8, 8, 7, 7, 7, 7, 3 sl; 1 single) | 13 | 11 / 36 / 8 | Carousel "borrow against investments" (3 sl) 6/9 = 0.67* · best Reel "Got a raise?" 6/36 = 0.17* | Reel "Not married? No will?" 0/121 | Reel "Not married? No will?" 142 | Reel "CPP early?" 0 (5 h, no delivery) |
| Locked Hour | 4 (+0 / +1) | 14 (carousels 10, 10, 10, 10, 10, 8, 7, 7, 7, 7, 6 sl; 2 singles; 1 n/a) | 12 | 9.5 / 24 / 4 | Carousel "can't focus? follow the line" (5 sl) 5/12 = 0.42* · best Reel "A new habit doesn't take 21 days" 4/46 = 0.09* | Reel "For every parent who gets interrupted" 0/109 | Reel "For every parent who gets interrupted" 118 | Carousel "Sunday scaries" (7 sl) 1 (8 h) |
| Hourback | 5 (+0 / +2) | 14 (carousels 10, 10, 9, 9, 9, 7, 7, 7, 7, 6, 6, 3, 3 sl; 1 single) | 13 | 9 / 17 / 6 | Carousel "Can you sublet?" (3 sl) 4/7 = 0.57* · best Reel "Plan tomorrow in one prompt" 4/67 = 0.06* | Reel "Two AIs" 0/33 | Reel "Plan tomorrow" 94 | Carousel "consultants 25% faster" (6 sl) 0 (7 h) |
| Littlefold | 6 (+0 / +3) | 14 (carousels 9, 9, 9, 8, 7, 7, 7, 7, 6, 6, 5, 4, 3 sl; 1 single) | 13 | 14 / 105 / 5.5 | Carousel "safe sleep: alone, back, crib" (3 sl) 4/10 = 0.40* · best Reel "Too little for books?" 4/25 = 0.16* | Reel "bonding bubble" 0/134 | Reel "bonding bubble" 165 | Carousel "No RESP yet?" (8 sl) 2 (13 h) |

\*Every "best" is an Oct 17–18 post whose saves include the Oct 17 save burst (it came before the git reads). **Posts from Oct 19 on have 1 clean send and 0 clean saves since Oct 21.**

**Total: 22 followers (+0 since yesterday's read, +10 in 7 days).** Flat for 4 reads. Profile views in the last day: FF 11, LH 3, HB 4, LF 8. `follows_from_posts`: LF 1, the others 0.
- **Yesterday's posts (Oct 23 ET, 14 posts: 6 Reels, 8 carousels). FF 8:15 am and LH 8:30 am Reels were empty slots:**
  - By clean (saves + sends)/reach, nothing scored: all 14 have 0 saves and 0 sends.
  - Best on strangers: LF Reel "First cold morning? Coat off, then buckle", 81 reach in 5 h (93% non-follower), 5.5 s, 38%.
  - Best by views: the same Reel, 99.
  - Worst: FF Reel "Your parents taking CPP early?", 0 views.
- **Sum of post reach (1 day):** FF 880 → 913, LH 685 → 734, HB 445 → 466, LF 1,539 → 1,687.

### Patterns (all pages ≥5 posts)
- **Reels vs feed, non-follower reach (high confidence on direction):** the 7-day Reel median is 36 / 24 / 17 / 105 (FF / LH / HB / LF), against a feed median of 8 / 4 / 6 / 5.5. Stranger batches of ≥80 are 88–96% non-follower, and feed posts stay at reach 0–11.
- **Length (medium-high, n=31 Reels since Oct 19, ≥12 h old):**

  | Length | Median watch-through | Median seconds | Median reach | n |
  |---|---|---|---|---|
  | ≤15 s | 30% | 3.9 s | 25 | 14 |
  | 21–30 s | 22% | 5.5 s | 12 | 3 |
  | 30–40 s | 11% | 4.1 s | 44 | 14 |

  Seconds watched are flat at about 4 s, so length is solved and the open is the lever.
- **Open type (low-medium, n=2 wins):**
  - Felt question + a physical rule shown being done: 5.5 s on 81–104.
  - Felt question + an abstract promise: 1.7 s on 50.
  - 🇨🇦 cheat-sheet / "money you can get" opens: 2.5–3.5 s on 16–103.
  - Number-cost opens (FF one-year): 3.5 s, but they win FF's big batches.
- **Topic still decides batch size (medium):** LF holds 8 of the 10 biggest batches (144, 136, 136, 134, 118, 105, 104, 103). The other 2 are FF wills 121 and LH 116 (Oct 16). Every LF Reel since Oct 19 reached ≥50.
- **Trial flag (low):** since Oct 19, trials vs normal Reels by median reach: FF 21 vs 79, LH 16 vs 18, HB 11 vs 19, LF 103 vs 105. On no page does the flag win a bigger batch, and on FF and HB normal Reels did better. Today's HB non-trial 8:45 Reel is the clean test.
- **Posting time (low):** LF 7 pm Reels get their batch within 5 h (coat 81, bonding 129). FF and LH 8 am batches arrive at 8–24 h. There's still no slot call: the topic swamps the time.
- **Sends:** 1 clean since Oct 19, on 75 posts.

### Comments
**No data yet.** 0 real comments. The 138 counted are our own first comments (LH "Rereading the same line" shows 2, but no text came back). Comment text has been empty for 10 days.

### Health
- **Published vs schedule:** all **284 of 284** entries due by 7:28 am ET Oct 24 are published. 0 failed, 0 errors, 0 comment errors.
  - In the last 27 h, 14 went out more than 15 min late. The worst is an HB Story (hb-ch-1023-2) at 67 min; the worst Reel is HB photo-search at 33 min.
  - The Publish Ledger has 2 HIGH findings, both on the same LH follow-the-line Reel (day 4).
- **Delivery:** the FF CPP Reel published fine, but at 5 h it had 0 views and 0 reach (order 1).
- **Next 48 h (to 7:30 am ET Oct 26):** full on all 4 pages.
  - **Reels:** 4 per page, all 11.7–14.8 s.
  - **Feed:** FF 3, LH 3, HB 2, LF 4.
  - **Stories:** FF and LH 10, LF 9, HB 5.
  - All media files exist, and the schedule runs to Mon Oct 26, 5:45 pm.
- **Data:** all 26 insight reads succeeded, with no token or account errors.
  - **Still broken:** comment text, follow_type, the per-post `follows` read (HTTP 400), and per-post lines in history.jsonl.
  - **No new burst.**

### Media kit
Updated (claude/media-kit.md).

---

## TEST-BATCH TABLE (Fri Oct 23, 2026, Performance desk)
Data: insights/latest.json, collected **Oct 23 04:35 UTC (12:35 am ET)**. Per-post curves rebuilt from the **18** reads in git (Oct 19 04:37 → Oct 23 04:35 UTC). Reel lengths come from ffprobe on each MP4 as it was when published. Next read ~12:40 UTC (8:40 am ET).
- **Verdict rules (unchanged):** EXPANDED = reach still climbing after 24 h (≥ +25% and ≥ +10) AND sends/reach in the top third. STALLED = flat after 24 h. FAILED HOOK = average watch under 4 s or under 25% of length. PENDING = under 24 h.
- **Non-follower share** is a floor: (reach − current followers) / reach. follow_type still not read; the per-post `follows` read still fails with HTTP 400 on every post.
- **⚠ Burst #4.** Between the Oct 22 20:35 and Oct 23 04:35 UTC reads (4:35 pm–12:35 am ET), **21 recent FF, HB and LF posts gained +137 shares, +38 saves, +35 likes**. Most got exactly **+8 shares and +2 saves**, whatever their reach, and that includes posts with reach 3–7. Locked Hour wasn't touched. Followers rose **18 → 22** in the same window, after falling 28 → 16 following burst #3. Every sends and saves number below has all 4 burst windows removed. Reach that jumped inside a burst window is marked †.
- **Comments per reach = 0 everywhere.** All 123 counted comments are our own first comments. Comment text is still empty (day 9).

| Page | Post (first line) | Format | Age | Reach curve (age → reach) | Non-follower ≥ | Sends/reach (clean) | Saves/reach (clean) | Avg watch / length | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LF | "The first 2 weeks: protect your bonding bubble." | Reel 39.5 s | 53 h | 5h 129 → 21h 133 → 53h 134 | 96% | 0.00 | 0.00 | **6.0 s** / 39.5 s = 15% | FAILED HOOK (by %) + STALLED |
| FF | "Not married? No will? Your partner may get nothing." | Reel 38.3 s | 53 h | 5h 61 → 13h 113† → 53h 116 | 94% | 0.00 | 0.00 | 4.2 s / 38 s = 11% | FAILED HOOK (by %) + STALLED |
| LH | "For every parent who gets interrupted halfway through everything." | Reel 39.0 s (trial) | 64 h | 16h 51 → 24h 107† → 64h 109 | 96% | 0.00 | 0.00 | 3.8 s / 39 s = 10% | FAILED HOOK + STALLED |
| LF | "Your baby is learning your voice before they're even born." | Reel 39.7 s (trial) | 64 h | 4h 70 → 25h 106† → 64h 108 | 94% | 0.00 | 0.00 | 3.0 s / 40 s = 7% | FAILED HOOK + STALLED |
| LF | "Sleep and screens by age, Canada edition 🇨🇦" | Reel 11.6 s (trial) | 16 h | 4h **100** → 8h 101 → 16h 103 | 94% | 0.00 | 0.00 | 3.4 s / 11.6 s = 30% | FAILED HOOK (by s) + PENDING. A held format, but it still won LF's batch in 4 h |
| LF | **"Toddler pulling you to come play? Give them 10 minutes where they lead"** | Reel 14.2 s | 29 h | 5h 22 → 8h 46 → 21h 71 → 29h 102† | 94% | 0.00 | 0.00 | **5.6 s / 14.2 s = 40%** | Climbing past 24 h (+31†) but 0 sends, so not EXPANDED. **First ≤15 s Reel to hit ≥5 s AND ≥30% on a batch ≥40** |
| FF | "What waiting just one year costs you by 65 🇨🇦" | Reel 11.6 s | 29 h | 5h 27 → 8h 46 → 21h 77 → 29h 101† | 93% | 0.00 | 0.00 | 3.5 s / 11.6 s = 31% | FAILED HOOK (by s), climbing (+24†). FF's 2nd-biggest batch ever |
| LF | "Money your family can get in Canada, for each child 🇨🇦" | Reel 11.6 s (trial) | 40 h | 4h 9 → 24h 47 → 40h 50† | 88% | 0.00 | 0.00 | 2.6 s / 11.6 s = 23% | FAILED HOOK + STALLED |
| HB | "Two AIs. One admits 'I don't know'. Which would you trust?" | Reel 38.9 s | 53 h | 5h 10 → 21h 31 → 53h 33 | 85% | 0.00 | 0.00 | 5.7 s / 39 s = 15% | FAILED HOOK (by %) + STALLED |
| LH | "Missed a day? Don't start over. The research is on your side." | Reel 13.9 s | 29 h | 5h 15 → 21h 19 → 29h 28† | 86% | 0.00 | 0.00 | 4.0 s / 13.9 s = 29% | STALLED (borderline on both bars; hold fell from 5.7 s as strangers came) |
| FF | "A 1% fee sounds tiny. Here's what it takes 🇨🇦" | Reel 12.2 s (trial) | 40 h | 4h 16 → 24h 23 → 40h 26 | 73% | 0.00 | 0.00 | 2.6 s / 12 s = 21% | FAILED HOOK + STALLED |
| FF | "TFSA or RRSP? One question decides it." | Reel 37.5 s (trial) | 64 h | 4h 9 → 24h 22 → 64h 22 | 68% | 0.00 | 0.00 | 3.8 s / 37.5 s = 10% | FAILED HOOK + STALLED |
| HB | "Spam texts and calls: the shut-off sheet 🇨🇦" | Reel 25.4 s (trial) | 64 h | 4h 1 → 24h 19 → 64h 22 | 77% | 0.00 | 0.00 | 3.6 s / 25 s = 14% | FAILED HOOK + STALLED |
| LH | "Lying awake thinking about tomorrow? … Give it paper." | Reel 39.6 s | 53 h | 5h 3 → 13h 11 → 53h 12 | 67% | 0.00 | 0.00 | 7.2 s / 40 s = 18% (likely followers) | FAILED HOOK (by %) + STALLED |
| HB | "Set it up once. Never chase it again 🇨🇦" | Reel 25.1 s (trial) | 40 h | 4h 3 → 24h 11 → 40h 12 | 58% | 0.00 | 0.00 | 5.9 s / 25 s = 24% | FAILED HOOK (by %) + STALLED |
| FF | "TFSA vs RRSP vs FHSA, in one look 🇨🇦" | Reel 11.3 s (trial) | 16 h | 4h 8 → 16h 11 | 36% | 0.00 | 0.00 | 4.4 s / 11.3 s = 39% | PENDING, no stranger batch |
| FF | "Spend the refund, or turn it into $29,000?" | Reel 13.7 s | 5 h | 5h 11 | 36% | 0.00 (3 raw, inside the burst window) | 0.00 | 2.6 s / 13.7 s = 19% | PENDING |
| HB | "Engineers pasted secret code into ChatGPT." | Reel 13.5 s | 29 h | 5h 6 → 29h 9 | 44% | 0.00 | 0.00 | 8.1 s / 13.5 s = 60% | STALLED, no stranger batch |
| LH | "Can't crack it at your desk? Stand up." | Reel 14.0 s | 5 h | 5h 8 | 50% | 0.00 | 0.00 | 3.8 s / 14 s = 27% | PENDING |
| HB | "Charges you forgot you pay. Everyone has a few 🙈" | Reel 15.0 s (trial) | 15 h | 7h 0 → 15h 7 | 29% | 0.00 | 0.00 | 18.5 s (rewatches, followers) | PENDING, no stranger batch |
| LH | "Can't make yourself go to the gym? Make the gym the only place…" | Reel 11.9 s (trial) | 15 h | 7h 4 → 15h 5 | 20% | 0.00 | 0.00 | 16.2 s (rewatches, followers) | PENDING, no stranger batch |

**Feed posts in the window (24):** all STALLED or PENDING at reach **1–9**, with 0 clean sends. The 8 Oct 22 carousels (5–10 slides) reached 1–7, median 3.

**EXPANDED: 0 of 124.** What moved since yesterday:
1. **≤15 s now lifts watch-through on big batches.** Three tight cuts held about 30%+ on ~100 strangers each: LF toddler play 40%, FF one-year 31%, LF sleep and screens 30%. Before Oct 21, no batch of ≥60 held more than 18%.
   - Across 27 Reels since Oct 19, ≤15 s holds a median **35%** (4.2 s, n=10) and 30–40 s holds **11%** (4.1 s, n=14).
   - Seconds watched are the same. So the next lever is the open, not the length.
2. **LF "Toddler pulling you to come play? Give them 10 minutes where they lead" is the first Reel to pass both bars:** ≥5 s (5.6 s) and ≥30% (40%) on ≥40 reach (102). Its hold *rose* as strangers came (1.9 → 7.7 → 5.6 s). The open pairs a felt question with one concrete rule that has a number in it.
3. **Sends are the wall.** 0 clean sends on all 21 Reels in the window, on about 1,300 stranger reach. Every send we saw came in a burst.
4. **8 am Trial Reels on LH and HB got no batch:** 5 and 7 reach at 15 h. The LF trial got 100 in 4 h.

- **TikTok:** manual (no API; no numbers logged).
- **YouTube Shorts:** no data yet. vidIQ checked this run: signed in as the Steadfold Gmail, **0 YouTube channels** and **0 Instagram accounts** connected.
- **Trial Reels:** 25 measured. Graduation to followers: **no data yet** (not in the API).

**3 orders**
1. **REPEAT:** "felt question + one rule with a number" at ≤15 s, the LF toddler-play structure (5.6 s, 40% on 102).
2. **KILL:** 30–40 s Reels for good (done in the queue: all 19 queued are 12.6–14.8 s). Also cheat-sheet opens (held Oct 22, done).
3. **TEST:** a send trigger. On 1 Reel per page on Oct 24–25, the last beat names who to send it to ("Send this to the friend who…"). **Grade:** ≥1 clean send per 50 reach.

## Today's orders (Fri Oct 23, 2026, Performance desk)
Data: Oct 23 04:35 UTC read, 18 reads of per-post curves. 124 posts (57 Reels, 67 feed), 22 followers. Direction: medium confidence. Four burst windows were removed from sends and saves.
1. **Social studio: FILL the 5 empty Reel slots in the next 48 h.** Yesterday's cheat-sheet hold left these slots empty:
   - FF 8:15 am and LH 8:30 am today (probably too late);
   - **LF 7 pm tonight**;
   - **LF 8 am and HB 8:45 am Sat**.

   Littlefold has 2 of its 4 Reels, and it's the page with the biggest batches (Reel median 105 against 6.5 for feed). The fastest fix: move the ready LF "You can't spoil a newborn. Pick them up." Reel (Oct 25 8 am, 14 s, rule open) to tonight's 7 pm, then backfill. Log a rollback record (repo rule).
   - **Also, day 3:** give `reels/lh-pan-1021am-follow-the-line-s15.mp4` a new id. The Publish Ledger still flags it as never published (2 HIGH findings).
2. **Short-form + Social studio (all pages): REPEAT the toddler-play structure on at least 1 Reel per page on Oct 24–25.** The structure is a felt question, then one rule with a number ("Give them 10 minutes where they lead"), at ≤15 s. It held 5.6 s and 40% on 102 strangers. "Missed a day? Don't start over" held 4.0 s and 29% on 28, and the 🇨🇦 cheat opens held 2.6–3.5 s. **Grade:** ≥5 s and ≥30% on ≥40 reach.
3. **Short-form studio (all pages): TEST a send trigger.** There were 0 clean sends on 21 Reels and about 1,300 stranger reach in 72 h, and sends are the #1 expansion signal. On 1 Reel per page on Oct 24–25, the last beat names the person to send it to: the partner on the night shift, the friend who just had a baby, the coworker in every meeting. Keep it to ≤6 words, and still ≤15 s. **Grade:** ≥1 clean send per 50 reach.
4. **Social studio (Locked Hour, Hourback): TEST one 8 am Reel without the trial flag.** The Oct 22 8 am trials reached 5 (LH) and 7 (HB) at 15 h. Across all their trials, HB's ran 7–22 and LH's 5–109. The LF and FF trials do get batches. Run LH or HB on Sat Oct 24 as a normal Reel and compare its 24 h reach with the trial history. Low confidence, n is small.
5. **Social studio: LESS 7–10 slide carousels, day 4.** The 8 Oct 22 carousels (5–10 slides) reached 1–7, median 3. The 7-day feed median is 4.5–8 on every page, against Reel medians of 18–105. Keep 1 feed post a day at ≤5 slides.
6. **Automation architect: burst #4.**
   - **What happened:** 21 FF/HB/LF posts gained exactly +8 shares and +2 saves each in one window, and followers rose +4. LH was untouched.
   - **Asks:** log shares, saves, likes and reach per post per read in history.jsonl, and flag any window where most posts move together.
   - **Bug:** the per-post `follows` read returns HTTP 400 on every post.
   - **New and worth keeping:** `follows_from_posts` (LF 1, the first non-zero) and `day_profile_views`.

**Grading yesterday's orders (owner check):**
1. **Re-queue LH follow-the-line under a new id: NOT done** (day 3). The ledger still flags it.
2. **Kill the 🇨🇦 cheat Reels: done.** 8 Reels were moved to schedule/held-oct22.json at 1:14 pm ET (reversible). The two 8 am cheats had already gone out, and LF sleep-and-screens still won a 103 batch. The cost was 5 empty Reel slots (order 1).
3. **≤15 s runtime: done.** All 19 queued Reels run 12.6–14.8 s (commit 3983b90).
4. **Rule + reassurance opens, 1 per page on Oct 23–24: partly done.** Most queued opens are a felt question followed by a fix ("Bedtime turned into a battle again?", "Coffee at 4 pm?"). Pure rule opens are on Oct 25 (LF "You can't spoil a newborn", LH "It'll take an hour. It won't.").
5. **FF wills ≤15 s Trial Reel: scheduled.** It goes out Sun Oct 25 8:15 am, 14.8 s, with the trial flag.
6. **Per-post logging: not done.** history.jsonl still has account lines only. `follows_from_posts` and `day_profile_views` were added.

---

## Daily report: Fri Oct 23, 2026

### Scoreboard (insights read Oct 23 04:35 UTC)
Changes are vs the Oct 22 04:35 UTC read (1 day) and the Oct 16 04:32 UTC read (7 days). Sends and saves are burst-cleaned.

| Page | Followers (1d / 7d) | Feed posts 7d (slides) | Reels 7d | Median reach (all / Reels / feed) | Best by (saves+sends)/reach | Worst | Best by views | Worst by views |
|---|---|---|---|---|---|---|---|---|
| Fully Funded | 7 (+2 / +5) | 14 (carousels 10, 10, 10, 10, 9, 8, 8, 7, 7, 7, 3, 3 sl; 2 singles) | 14 | 11 / 45 / 8 | Carousel "borrow against investments" (3 sl) 6/9 = 0.67* · best Reel "Got a raise?" 6/36 = 0.17* | Reel "TFSA vs RRSP vs FHSA" 0/11 | Reel "Not married? No will?" 137 | Carousel "every dollar" (7 sl) 8 (7 h old) |
| Locked Hour | 4 (+1 / +2) | 14 (carousels 10, 10, 10, 10, 8, 7, 7, 7, 7, 6 sl; 3 singles; 1 n/a) | 13 | 11 / 24 / 4.5 | Carousel "can't focus? follow the line" (5 sl) 5/11 = 0.45* · best Reel "inbox picks your morning" 3/15 = 0.20* | Reel "gym bundle" 0/5 | Reel "quiet hour" 146 | Carousel "desk" (5 sl) 1 (7 h old) |
| Hourback | 5 (+1 / +3) | 14 (carousels 10, 10, 9, 9, 7, 7, 7, 7, 7, 6, 3, 3 sl; 2 singles) | 13 | 9 / 18 / 6.5 | Carousel "can you sublet?" (3 sl) 4/6 = 0.67* · best Reel "per my last email" 5/13 = 0.38* | Reel "charges you forgot" 0/7 | Reel "plan tomorrow" 94 | Carousel "landlord email" (7 sl) 4 (7 h old) |
| Littlefold | 6 (+2 / +5) | 14 (carousels 9, 9, 9, 7, 7, 7, 6, 6, 6, 5, 4, 3 sl; 2 singles) | 13 | 14 / 105 / 6.5 | Single "8 to 12 feeds" 4/8 = 0.50* · best Reel "too little for books?" 4/25 = 0.16* | Reel "family money 🇨🇦" 0/50 | Reel "bonding bubble" 165 | Carousel "baby finally asleep" (6 sl) 10 (7 h old) |

\*Every "best" is an Oct 16–17 post whose saves include the Oct 17 save burst (it came before the git reads). **Posts from Oct 19 on have 0 clean saves and 0 clean sends almost everywhere.**

**Total: 22 followers (+6 since yesterday's read, +15 in 7 days).** The peak was 28 on Oct 21, then 16 after burst #3. Of the +6, 4 landed inside burst #4.
- **Yesterday's posts (Oct 22 ET, 14 posts: 6 Reels, 8 carousels; the HB and LF 7 pm Reels were held):**
  - By clean (saves + sends)/reach: nothing scored.
  - Best on strangers: LF Trial Reel "Sleep and screens by age 🇨🇦", 103 reach in 16 h (94% non-follower), 3.4 s, 30%.
  - Best by views: the same Reel, 118.
- **Sum of post reach (1 day):** FF 777 → 880, LH 654 → 685, HB 426 → 445, LF 1,351 → 1,539.

### Patterns (all pages ≥5 posts)
- **Reels vs feed, non-follower reach (high confidence on direction):** the 7-day Reel median is 45 / 24 / 18 / 105 (FF / LH / HB / LF), against a feed median of 8 / 4.5 / 6.5 / 6.5. Stranger-batch Reels are 85–96% non-follower. Feed posts stay at reach 1–9.
- **Length (medium-high, n=27 Reels since Oct 19, ≥12 h old):**

  | Length | Median watch-through | Median seconds | Median reach | n |
  |---|---|---|---|---|
  | ≤15 s | 35% | 4.2 s | 27 | 10 |
  | 21–30 s | 22% | 5.5 s | 12 | 3 |
  | 30–40 s | 11% | 4.1 s | 44 | 14 |

- **Open type (medium-low):**
  - A felt question plus a rule with a number won: toddler play 5.6 s on 102. The LF rule opens held 5.2–6.6 s on 105–136 at 37–40 s.
  - Cheat-sheet and "money you can get" opens held 2.6–3.5 s on 26–103.
  - Number-cost opens (FF one-year) hold about 3.5 s but win big FF batches (101).
- **Topic still decides batch size (medium):** LF won 7 of the 10 biggest batches this week. The other 3 are LH (116, 109) and FF (116). FF one-year (101) is just outside.
- **Trial Reels (low-medium):** LF trials get the batch in about 4 h (100, 70). LH and HB morning trials mostly don't (5, 7, 12, 22).
- **Sends:** 0 clean on every post since Oct 21. All the visible sends came in burst windows.

### Comments
**No data yet.** 0 real comments. The 123 counted are our own first comments, and comment text has been empty for 9 days.

### Health
- **Published vs schedule:** all **252 of 252** entries due by 7:35 am ET Oct 23 are published. 0 failed, 0 errors, 0 comment errors.
  - In the last 26 h, 33 went out late. The worst was the LF 8 am Reel at 65 min; LH Stories ran 49–50 min late.
  - The Publish Ledger has 2 HIGH findings, both the same never-published LH follow-the-line Reel (order 1).
- **Next 48 h (to 7:35 am ET Oct 25):**
  - **Reels: FF 3, LH 3, HB 3, LF 2.** 5 slots are empty after the Oct 22 hold: FF 8:15 am and LH 8:30 am today, LF 7 pm today, LF 8 am and HB 8:45 am Sat.
  - Feed: 4 per page. Stories: 9–10 per page.
  - All media files exist, and all 19 queued Reels are 12.6–14.8 s. The schedule runs to Mon Oct 26, 5:45 pm.
- **Data:** all 18 insight reads succeeded, with no token or account errors.
  - **Still broken:** comment text, follow_type, the per-post `follows` read (HTTP 400 on every post), and per-post lines in history.jsonl.
  - **Burst #4:** see the table note.

### Media kit
Updated (claude/media-kit.md).

---

## TEST-BATCH TABLE (Thu Oct 22, 2026, Performance desk)
Data: insights/latest.json, collected **Oct 22 07:06 UTC (3:06 am ET)**. Per-post curves rebuilt from the **18** reads in git from Oct 18 04:31 to Oct 22 07:06 UTC. Reel lengths come from ffprobe on each MP4 **as it was when published**. The next read is ~12:40 UTC (8:40 am ET).
- **Verdict rules (unchanged):** EXPANDED = reach still climbing after 24 h (≥ +25% and ≥ +10 accounts) AND sends/reach in the top third. STALLED = flat after 24 h. FAILED HOOK = average watch under 4 s or under 25% of length. PENDING = under 24 h.
- **Non-follower share** is a floor: (reach − current followers) / reach. The collector still doesn't read follow_type. The new per-post `follows` read fails on every post with HTTP 400 ("not supported for this media product type").
- **⚠ A third share burst, the biggest yet, followed by a follower drop.**
  - **The burst:** between the Oct 21 04:36 and 12:44 UTC reads (12:36–8:44 am ET), **41 posts on all 4 pages gained +274 shares, +100 saves and +113 likes**. In the same window, **reach jumped on the 4 biggest Reels**: LH nap-time 51 → 107, FF wills 61 → 113, LF movements 79 → 106 and HB Two AIs 10 → 27.
  - **The drop:** over the next two reads, **followers fell 28 → 24 → 16** (FF 8 → 5, LH 6 → 3, HB 7 → 4, LF 7 → 4).
  - **A smaller HB burst** hit Oct 22 04:35 UTC: +14 shares on 4 HB posts with flat reach, and shares ≥ reach on 3 of them.
  - **What it means:** this looks like the same few accounts sharing the whole catalogue (as on Oct 19), and then about 12 accounts unfollowing. It is not stranger behaviour.
  - **How the table treats it:** every sends number below has all three burst windows removed, and the Oct 21 reach jumps are marked †.
- **Comments per reach = 0 everywhere.** 109 comments across 110 posts, all our own first comments. Comment text is still empty (day 8).

| Page | Post (first line) | Format | Age | Reach curve (age → reach) | Non-follower ≥ | Sends/reach (clean) | Saves/reach (clean) | Avg watch / length | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LF | "Your newborn is talking to you long before they cry." | Reel 37.2 s (trial) | 67 h | 4h 130 → 24h 134 → 67h 136 | 97% | 0.01 (1) | 0.01 | **6.6 s** / 37 s = 18% | FAILED HOOK (by %) + STALLED |
| LF | "The first 2 weeks: protect your bonding bubble." | Reel 39.5 s | 32 h | 5h 129 → 21h 133 → 32h 134 | 97% | 0.00 | 0.00 | **5.8 s** / 39.5 s = 15% | FAILED HOOK (by %) + STALLED |
| FF | "Not married? No will? Your partner may get nothing." | Reel 38.3 s | 32 h | 5h 61 → 13h 113† → 32h 115 | 96% | 0.00 | 0.00 | 4.1 s / 38 s = 11% | FAILED HOOK (by %) + STALLED. Still FF's biggest batch |
| LH | "For every parent who gets interrupted halfway through everything." | Reel 39.0 s (trial) | 42 h | 4h 8 → 16h 51 → 24h 107† → 42h 109 | 97% | 0.00 | 0.00 | 3.8 s / 39 s = 10% (5.0 s at 51 reach) | FAILED HOOK + STALLED |
| LF | "Your baby is learning your voice before they're even born." | Reel 39.7 s (trial) | 43 h | 4h 70 → 16h 79 → 24h 106† → 43h 107 | 96% | 0.00 | 0.00 | 3.0 s / 40 s = 8% | FAILED HOOK + STALLED |
| LF | "The 5-step game that builds your baby's brain" | Reel 39.2 s | 56 h | 5h 57 → 21h 79 → 29h 103 → 56h 105 | 96% | 0.00 | 0.03 | 5.2 s / 39 s = 13% | FAILED HOOK (by %) + STALLED (the climb stopped at 29 h) |
| FF | "Started investing at 33, not 28? You can catch up." | Reel 37.2 s | 56 h | 5h 34 → 21h 54 → 56h 55 | 91% | 0.00 | 0.02 | 3.9 s / 37 s = 11% | FAILED HOOK + STALLED |
| FF | **"What waiting just one year costs you by 65 🇨🇦"** | Reel 11.6 s | 8 h | 5h 27 → 8h **46** | 89% | 0.00 | 0.02 | 3.2 s / 11.6 s = 28% | PENDING, still climbing. FF's fastest 8 h batch after wills |
| LF | "Toddler pulling you to come play? Give them 10 minutes…" | Reel 14.2 s | 8 h | 5h 22 → 8h 46 | 91% | 0.00 | 0.00 | 2.5 s / 14 s = 18% | FAILED HOOK + PENDING |
| LF | "Money your family can get in Canada, for each child 🇨🇦" | Reel 11.6 s (trial) | 19 h | 4h 9 → 19h 41 | 90% | 0.00 | 0.00 | **1.5 s** / 11.6 s = 13% | FAILED HOOK + PENDING |
| HB | "Two AIs. One admits 'I don't know'. Which would you trust?" | Reel 38.9 s | 32 h | 5h 10 → 13h 27† → 32h 33 | 88% | 0.00 | 0.00 | 5.7 s / 39 s = 15% | FAILED HOOK (by %) + STALLED. HB's best hold on ≥30 |
| FF | "TFSA or RRSP? One question decides it." | Reel 37.5 s (trial) | 42 h | 4h 9 → 24h 22 → 42h 22 | 77% | 0.00 | 0.00 | 3.5 s / 37.5 s = 9% | FAILED HOOK + STALLED |
| HB | "Spam texts and calls: the shut-off sheet 🇨🇦" | Reel 25.4 s (trial) | 42 h | 4h 1 → 24h 19 → 42h 22 | 82% | 0.00 | 0.00 | 3.6 s / 25 s = 14% | FAILED HOOK + STALLED |
| FF | "A 1% fee sounds tiny. Here's what it takes 🇨🇦" | Reel 12.2 s (trial) | 19 h | 4h 16 → 19h 21 | 76% | 0.00 | 0.00 | **1.6 s** / 12 s = 13% | FAILED HOOK + PENDING |
| FF | "New baby, new mortgage: which life insurance?" | Reel 38.8 s (trial) | 67 h | 4h 7 → 24h 17 → 67h 20 | 75% | 0.00 | 0.10 | 3.4 s / 39 s = 9% | FAILED HOOK + STALLED |
| HB | "AI made people 25% faster. Then it made them wrong." | Reel 37.7 s | 56 h | 5h 4 → 21h 7 → 29h 16 → 56h 19 | 79% | 0.00 | 0.00 | 3.7 s / 38 s = 10% | FAILED HOOK + STALLED |
| LH | "Every ping costs you more than time" | Reel 38.3 s (trial) | 66 h | 3h 3 → 23h 14 → 66h 16 | 81% | 0.00 | 0.06 | 4.2 s / 38 s = 11% | FAILED HOOK (by %) + STALLED |
| LH | **"Missed a day? Don't start over. The research is on your side."** | Reel 13.9 s | 8 h | 5h 15 → 8h 16 | 81% | 0.33 (5, unconfirmed: same window as the HB burst) | 0.00 | **5.7 s / 13.9 s = 41%** | PENDING. **Best watch-through of any Reel this week** |
| LH | "Which hour should you lock? Not the perfect one." | Reel 35.1 s | 56 h | 5h 4 → 21h 11 → 56h 12 | 75% | 0.00 | 0.08 | 3.8 s / 35 s = 11% | FAILED HOOK + STALLED |
| LH | "Lying awake thinking about tomorrow? … Give it paper." | Reel 39.6 s | 32 h | 5h 3 → 21h 11 → 32h 12 | 75% | 0.00 | 0.00 | 7.2 s / 40 s = 18% (small batch, likely followers) | FAILED HOOK (by %) + STALLED |
| HB | "Skip the CRA hold music 🇨🇦" | Reel 25.4 s (trial) | 66 h | 3h 0 → 23h 5 → 66h 10 | 60% | 0.00 | 0.10 | 5.5 s / 25 s = 22% | FAILED HOOK (by %) + STALLED |
| HB | "Set it up once. Never chase it again 🇨🇦" | Reel 25.1 s (trial) | 18 h | 4h 3 → 18h 10 | 60% | 0.00 (4 in the HB burst) | 0.00 | 2.5 s / 25 s = 10% | FAILED HOOK + PENDING |
| HB | "Engineers pasted secret code into ChatGPT." | Reel 13.5 s | 8 h | 5h 6 → 8h 6 | 33% | 0.00 (5 in the HB burst) | 0.17 | 3.2 s / 13.5 s = 23% | FAILED HOOK + PENDING |

† = the reach jump landed in the Oct 21 burst window. Treat it as shared-by-a-few, not an algorithm push.

**Feed posts in the window (24):** all STALLED or PENDING at reach **1–9**, with 0 clean sends.
- Oct 21: 8 carousels of 7–10 slides reached 1–3.
- Oct 19–20: carousels of 6–10 slides reached 3–9. The best was HB "agents do things" (7 slides) at 9.
- Slide count still makes no difference.

**EXPANDED: 0 of 110.** What moved since yesterday:
1. **Short alone did not fix the hold.** The six Oct 21 tight cuts (11.6–14.2 s) held a median **2.9 s and 20%**. The goal was ≥30%.
   - Only the LH "Missed a day? Don't start over" rule open cleared it: **5.7 s, 41%**.
   - The three 🇨🇦 cheat-sheet and "money you can get" opens held **1.5–1.6 s** on 21–41 strangers. They are the worst opens on the account.
2. **Cheat sheets now fail on 3 pages, not just Hourback.**

   | Cheat-sheet Reel | Hold | Reach |
   |---|---|---|
   | LF family money | 1.5 s | 41 |
   | FF fees | 1.6 s | 21 |
   | HB set-once | 2.5 s | 10 |
   | HB spam | 3.6 s | 22 |

   **6 of the 16 Reels due in the next 48 h are 🇨🇦 cheat sheets, 4 of them as 8 am Trial Reels.** That also breaks standard B19 (Canada topics at most 1 a week per page, as a labelled series).
3. **The rule/number open still holds best on big batches.**
   - LF hunger cues held 6.6 s on 136, bonding bubble 5.8 s on 134 and the 5-step game 5.2 s on 105.
   - The audience callout ("For every parent who…") fell from 5.0 s to 3.8 s as its batch doubled. That doubling came in the burst window.
4. **Followers fell 28 → 16** right after the share burst. Nothing in the content changed overnight that explains a 43% drop.

- **TikTok:** manual (no API; no numbers logged).
- **YouTube Shorts:** no data yet. vidIQ checked this run: signed in as the Steadfold Gmail, **0 YouTube channels** connected.
- **Trial Reels:** 21 measured. Graduation to followers: **no data yet** (the API doesn't return it).

**3 orders**
1. **REPEAT:** the rule-plus-reassurance open ("Missed a day? Don't start over. The research is on your side.", 5.7 s, 41% at 13.9 s) and the LF rule/number open (5.2–6.6 s on 105–136 strangers), now at ≤15 s.
2. **KILL:** the 🇨🇦 "X, in one look" cheat-sheet Reels on every page (1.5–3.6 s on 10–41). Swap the 6 queued for Oct 22–23 or hold them.
3. **TEST:** FF "Not married? No will?" recut at ≤15 s as a Trial Reel. It's still FF's biggest batch (115), and this is the 3rd day on this order. Also LH "Missed a day" structure on LF and FF. **Grade:** ≥30% and ≥5 s on ≥40 reach.

## Today's orders (Thu Oct 22, 2026, Performance desk)
Data: Oct 22 07:06 UTC read, 18 reads of per-post curves. 110 posts (51 Reels, 59 feed), 16 followers. Direction: medium confidence. Three burst windows were removed from sends.
1. **Social studio (Locked Hour) + Autopost owner: RE-QUEUE the LH Oct 21 8:30 am Trial Reel. It never published.**
   - **What happened:** entry `lh-pan-1021am-follow-the-line` reuses the id of the Oct 18 "Can't focus? follow the line" carousel, which is already published (Oct 18 21:18 UTC). Autopost saw the id as done and skipped it. state/published.json marks it "published" with the old carousel's permalink.
   - **The fix:** schedule `reels/lh-pan-1021am-follow-the-line-s15.mp4` under a new id at a future slot. Don't edit the past entry (D24).
   - **Prevention:** add a schedule check that fails when an id already in state has a later publish_at. That check finds exactly 1 such entry today.
2. **Short-form studio + Social studio (all pages): KILL the 🇨🇦 cheat-sheet Reels in the next 48 h.**
   - **Why:** cheat-sheet opens held 1.5–3.6 s on 10–41 strangers (LF family money 1.5 s on 41, FF fees 1.6 s on 21, HB set-once 2.5 s, HB spam 3.6 s), and short didn't save them.
   - **The 6 queued:** lf-cheat-1022am-sleep-screens, ff-cheat-1022am-tfsa-rrsp-fhsa, hb-cheat-1022-travel-admin (also 25.4 s), ff-cheat-1023am-cpp-oas, lh-cheat-1023am-focus-numbers and lf-cheat-1023-resp-catch-up.
   - **Also a standard breach:** 6 Canada-flag Reels in 2 days breaks B19 (max 1 Canada post a week per page).
   - **What to do:** swap in a rule/number open, or keep at most 1 a week as the labelled Canada series.
3. **Short-form studio (teach_reels.py owner): LESS runtime on Oct 22–23, 2nd day.**
   - **Done since yesterday:** 3 of the 5 Oct 22 Reels named yesterday were recut to 11.9–13.7 s (LH bundle, FF refund, LF CCB).
   - **Still long:** LH 7 pm walk 37.5 s and HB 7 pm travel-admin 25.4 s.
   - **New long ones:** Oct 23 has 5 Reels at 38.3–39.5 s (LF screens-bed, HB photo-search, FF CPP 60 or 70, HB duplicates, LH caffeine).
   - **The data:** across 47 Reels, ≤15 s holds a median 30% and 30–40 s holds 11%. Short is necessary but not enough (order 4).
4. **Short-form + Social studio (all pages): REPEAT "rule + reassurance" opens.**
   - **Why:** LH "Missed a day? Don't start over. The research is on your side." held **5.7 s, 41%** at 13.9 s, the only Oct 21 tight cut to clear 30%. The LF rule opens hold 5.2–6.6 s on 105–136 strangers: "The first 2 weeks: protect your bonding bubble", "Your newborn is talking to you long before they cry", "The 5-step game".
   - **Where to use it:** at least 1 Reel per page on Oct 23–24, ≤15 s.
   - **Grade:** ≥30% and ≥5 s on ≥40 reach.
5. **Short-form studio (Fully Funded): TEST "Not married? No will?" at ≤15 s as a Trial Reel. This is the 3rd day on this order.**
   - **Why:** it's FF's biggest batch (115, 96% non-follower) but held 4.1 s of 38 s.
   - **Also:** FF "What waiting just one year costs you by 65" is the other FF open worth keeping. It hit 46 in 8 h at 11.6 s and is still climbing, but holds 3.2 s.
6. **Automation architect + all desks: sends and followers are not stranger signals this week.**
   - **The burst:** Oct 21 12:36–8:44 am ET added +274 shares, +100 saves and +113 likes to 41 posts on all pages.
   - **The drop:** followers then fell 28 → 16.
   - **What to log:** shares, saves, likes and follows per post per read (the new per-post `follows` read fails with HTTP 400 on every post).
   - **What to flag:** any window where most posts move together.
   - **Feed:** keep 1 feed post a day at ≤5 slides. All 16 feed posts queued for Oct 22–23 are 5–10 slides, and the Oct 21 set (7–10 slides) reached 1–3.

**Grading yesterday's orders (owner check):**
1. **Recut the 5 long Oct 22 Reels to ≤15 s: 3 of 5 done** (LH bundle 11.9 s, FF refund 13.7 s, LF CCB 13.5 s). LH walk (37.5 s) and HB travel-admin (25.4 s) are still long, and Oct 23 adds 5 more at 38–40 s.
2. **LF rule/number open, ≥5 s on ≥60: not met.** The Oct 21 LF Reels used a cheat sheet ("Money your family can get", 1.5 s on 41) and a problem question ("Toddler pulling you to come play?", 2.5 s on 46).
3. **FF wills ≤15 s Trial Reel: not done.** The Oct 21 FF Reels were the fee and one-year cheats.
4. **LH "For every [person] who…" callout on Oct 22–23: not done.** The queued LH Reels open with "Can't make yourself go to the gym?", "Stuck on a problem?", "Focus science, in 5 numbers" and "Coffee at 4 pm?".
5. **Kill HB cheat sheets: not done.** "Set once" ran at 25.1 s and held 2.5 s, and HB travel-admin (25.4 s cheat) is queued for 7 pm tonight.
6. **LESS 7–10 slide carousels: not done.** The Oct 21 carousels ran 7–10 slides and reached 1–3, and 15 of the 16 queued run 6–10.

---

## Daily report: Thu Oct 22, 2026

### Scoreboard (insights read Oct 22 07:06 UTC)
Changes are measured against the Oct 21 04:36 UTC read (1 day) and Oct 15 04:32 UTC (7 days). Sends and saves have the burst windows removed. "Best/worst by (saves+sends)/reach" is ranked on posts with reach ≥40, because smaller posts score only from the same few accounts. Saves on Oct 15–17 posts still include the Oct 17 burst.

| Page | Followers (1d / 7d) | Feed posts 7d (slides) | Reels 7d | Median reach (all / Reels / feed) | Best by (saves+sends)/reach, reach ≥40 | Worst | Best by views | Worst by views |
|---|---|---|---|---|---|---|---|---|
| Fully Funded | **5 (−3 / +3)** | 13 (carousels 10, 10, 10, 10, 8, 8, 7, 7, 7, 3, 3 sl; 2 singles) | 13 | 16 / 46 / 9 | Reel "A 1% yearly fee looks tiny" 6/44 = 0.14 | Reel "Not married? No will?" 0/115 | Reel "Not married? No will?" 133 | Carousel "CLB who qualifies" (10 sl) 5 (15 h old) |
| Locked Hour | **3 (−3 / +1)** | 13 (carousels 10, 10, 10, 8, 7, 7, 7, 7, 6 sl; 3 singles; 1 n/a) | 12 | 12 / 29.5 / 8 | Reel "A new habit doesn't take 21 days" 4/44 = 0.09 | Reel "For every parent who gets interrupted" 0/109 | Reel "Get one quiet hour tomorrow" 146 | Carousel "Every habit has 4 steps" (7 sl) 3 (10 h old) |
| Hourback | **4 (−3 / +2)** | 13 (carousels 10, 9, 9, 7, 7, 7, 7, 7, 6, 3, 3 sl; 2 singles) | 13 | 9 / 19 / 7 | Reel "Out of eggs halfway through a recipe?" 4/62 = 0.06 | Reel "Plan tomorrow in one prompt" 4/67 = 0.06 (only 2 HB posts reach ≥40) | Reel "Plan tomorrow in one prompt" 94 | Carousel "10 hours to actually get AI" (7 sl) 4 (9 h old) |
| Littlefold | **4 (−3 / +4)** | 13 (carousels 9, 9, 9, 7, 7, 7, 7, 6, 6, 4, 3 sl; 2 singles) | 13 | 19 / 107 / 7 | Reel "You're doing better than you think" 4/66 = 0.06 | Reel "Money your family can get" 0/41 | Reel "It's 3 am" 161 | Carousel "5 minutes a day that build a brain" (7 sl) 1 (10 h old) |

**Total: 16 followers (−12 since yesterday's read, +10 since Oct 15).** All 4 pages lost 3 followers between 8:44 am and 12:37 pm ET Oct 21, right after the share burst.
- **Yesterday's posts (Oct 21 ET, 15 posts: 7 Reels, 8 carousels):**
  - **Best by (saves + sends)/reach:** LH Reel "Missed a day? Don't start over" at 5/16 = 0.31. Its 5 sends are unconfirmed, because they landed in the same window as the HB burst. On clean numbers, FF "What waiting just one year costs you" is 1/46.
  - **Best by views:** FF "What waiting just one year costs you by 65", 52 views on 46 reach in 8 h.
  - **Missing:** LH had no 8:30 am Reel. It was skipped (order 1).
- **Sum of post reach (1 day):** FF 637 → 777, LH 555 → 654, HB 343 → 426, LF 1,203 → 1,351.

### Patterns (all pages ≥5 posts)
- **Reels vs feed, non-follower reach (high confidence on direction):**

  | Format | Posts | Median reach | Median non-follower floor |
  |---|---|---|---|
  | Reels | 51 | 44 | 89% |
  | Feed | 59 | 8 | 44% |

- **Length (medium-high, n=47 Reels ≥12 h old):**

  | Length | Median watch-through | Median seconds watched | Median reach | n |
  |---|---|---|---|---|
  | ≤15 s | 30% | 4.3 s | 36 | 7 |
  | 15–21 s | 24% | 4.0 s | 62 | 11 |
  | 21–30 s | 14% | 3.6 s | 44 | 11 |
  | 30–40 s | 11% | 3.9 s | 44 | 18 |

  The six Oct 21 tight cuts (under 12 h old, not in this table) held a median 2.9 s and 20%. Length shapes the percentage; the open decides the seconds.
- **Open type (medium, n=6 vs 5 vs 6):**
  - **Rule, number or reassurance opens hold 5.2–6.6 s on big batches.** Hunger cues 6.6 s on 136, bonding 5.8 s on 134, 5-step game 5.2 s on 105; at small reach, "Missed a day" 5.7 s on 16.
  - **Problem-moment opens hold 2.5–3.8 s.** "Toddler pulling you to come play?" 2.5 s, "learning your voice" 3.0 s, "interrupted parent" 3.8 s at 109.
  - **🇨🇦 cheat-sheet opens hold 1.5–3.6 s** on all pages tested.
- **Topic still decides batch size (medium):**
  - Littlefold holds 7 of the 12 biggest batches.
  - FF: 115. LH: 109, 107. HB's best this week: 33.
- **Sends (burst-cleaned):** the 23 Reels in the 72 h window have **1 clean send** (LF hunger cues), plus 5 unconfirmed on LH "Missed a day". No Reel has earned a clean send from a stranger batch this week. **This is the gap to EXPANDED.**

### Comments
**No data yet.** 0 real comments. The 109 counted are our own first comments, and comment text has been empty for 8 days.

### Health
- **Published vs schedule:** state says all **219 of 219** entries due by 7:31 am ET Oct 22 are published, with 0 errors and 0 comment errors. **But one is false.** `lh-pan-1021am-follow-the-line` (LH Trial Reel, due 8:30 am Oct 21) reuses the Oct 18 carousel's id, so it never went out (order 1). It is the only id collision in the schedule.
- **Late in the last 24 h:** 16 entries were 10–36 min late, plus 1 HB Story (hb-ch-1021b-1) at **103 min**, more than one run cycle.
- **Next 48 h (to 7:30 am ET Oct 24): full on all 4 pages.** Each page has 4 Reels and 4 feed posts. Stories: FF and LH 10, HB 9, LF 8. All media files exist. The schedule runs to Oct 25, 7 pm.
- **Content flags (not faults):**
  - 6 of the 16 Reels are 🇨🇦 cheat sheets, which breaks B19 (order 2).
  - 7 run 25–40 s (order 3).
  - All 16 feed posts are 5–10 slides.
- **Data:** all 18 insight reads succeeded, with no token errors.
  - **New:** the per-post `follows` / `profile_visits` read returns HTTP 400 on every post ("not supported for this media product type").
  - **Still broken:** comment text, the follow_type split and per-post lines in history.jsonl.
  - **Burst windows:** 3 burst windows in 4 days (Oct 19, Oct 21 and an HB-only one on Oct 22).

### For the Automation architect
- Drop `follows` and `profile_visits` from the per-post insights call. It errors on every post. Read follows at account level instead (`follows_and_unfollows` with breakdown=follow_type), which would also show who left on Oct 21.
- Add a schedule lint: fail when a posts.json id already exists in state with an earlier published_at. Today's case is `lh-pan-1021am-follow-the-line`.
- Same asks as before:
  - per-post lines in history.jsonl;
  - reach with breakdown=follow_type;
  - comment text;
  - flag read windows where most posts move together;
  - log Reel length at publish.

### Media kit
Updated (claude/media-kit.md).

---


Older reports (Oct 15–21) are in claude/metrics.md in the Learning Lab project. The project is over its 2 MB limit (2,019,832 bytes on Oct 22), so new reports go here, newest first.

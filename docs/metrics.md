# Metrics (Performance desk, repo copy while the Learning Lab project is full)

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

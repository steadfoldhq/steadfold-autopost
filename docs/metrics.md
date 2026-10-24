# Metrics (Performance desk, repo copy while the Learning Lab project is full)

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

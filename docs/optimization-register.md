# Instagram Optimization Register (all four pages)

Loop: **Measure → Diagnose → Hypothesize → Experiment → Evaluate → Improve → Repeat.**
Owners: the **Performance desk** fills *Results* from `insights/` (real numbers only, "no data yet" otherwise); the **Social studio** runs the experiments and writes *Changes* and *Next action*. Started Oct 22 2026 by the v0.6 social recovery. Never invent a number; never call a result from fewer than 5 Reels with reach ≥ 40 (small samples are "inconclusive").

## Baseline (read of Oct 22 2026 16:39 UTC, `insights/latest.json` + `history.jsonl`)

| Page | Followers (now; peak) | Reels in data | Reel median reach | Reel median avg watch | Feed median reach | Follows from feed posts | Profile views / day |
|---|---|---|---|---|---|---|---|
| Fully Funded | 6 (8 on Oct 17) | 14 | 45 | 3.8 s | 9 | 0 | 3–7 |
| Locked Hour | 3 (6) | 13 | 24 | 4.2 s | 8.5 | 0 | 3 |
| Hourback | 4 (7) | 14 | 18.5 | 4.1 s | 7 | 0 | 4 |
| Littlefold | 4 (7) | 14 | 106.5 | 3.1 s | 6.5 | 0 | 5 |

Not available: follows per Reel (the API returns "not supported" — `follow_error`), unique viewers across posts (per-post reach can't be summed into people), returning viewers, completion/rewatch rates, follower/non-follower split (only a floor from reach − followers). Littlefold's ~1,600 Reel views across 14 Reels are **views, not people**.

## Diagnosis (Oct 22) — what the data supports, and how strongly

1. **Retention is the main failure (strong).** Reels reach 18–107 strangers per post (median), so the first test batch happens, but they hold 3–4 s on 11–40 s Reels (8–20% watch-through). Instagram doesn't expand posts people leave in 3 s. No Reel has expanded past its first batch (Performance desk: EXPANDED 0 of 110).
2. **Feed posts reach almost only followers (strong).** Median 6.5–9 reach with 3–6 followers: carousels can't grow a page this small; they serve the profile, not discovery.
3. **No reason to follow (moderate).** 0 follows from every feed post; profile visits come only from bold-claim covers; until Oct 22 no recurring series told a visitor what they'd miss. Each page mixed many unrelated topics (LF: sleep, crying, RESP grants, Ontario forms) — positioning is unclear to a stranger.
4. **Volume over quality (moderate).** Up to 2 feed + 2 Reels + 5 Stories per page per day, from a template that repeated the same clip-art (pointing hand, piggy bank). Cheat-sheet "table" Reels held 1.5–3.6 s and were held Oct 22.
5. **Follower counts are noise right now (strong).** All four pages rose Oct 16–18 and lost exactly 3 the same night Oct 21→22 — the same few accounts, not audience behaviour. Don't read follower deltas until organic follows exist.
6. **Distribution itself is not the binding constraint yet (moderate).** Reels do get stranger reach; the problem is what strangers do next. Paid reach would only buy more 3-second exits.

## Growth check — Oct 22 2026, evening (founder reported "about +2 followers")

The insights snapshots (`insights/history.jsonl`, taken 4× a day) confirm **+2 net today**:

- **Fully Funded 5 → 6** (between 12:44 and 16:39 UTC). Profile views that day rose 5 → 7 → 8.
- **Littlefold 4 → 5** (between 16:39 and 20:35 UTC).
- Locked Hour 3 and Hourback 4 were unchanged.

**Context:** every page is still below its Oct 20 count (FF 8, LH 6, HB 7, LF 7). All four lost followers in the same window on Oct 21 (12:44 → 16:37 UTC). In that same Oct 21 window, saves and shares also jumped on all four pages at once. That pattern looks like the same few accounts acting together, not audience behaviour.

**Attribution: none possible.** The API returns `follows` only for feed posts, and those show 0 on every post. Reels return "not supported". No post gained profile visits in either window.

What was active in each window:

- **FF window:** the "What waiting one year costs you by 65" Reel was still gaining reach (+5, then +13). The RRSP refund carousel was posted at 16:37.
- **LF window:** the "Give them 10 minutes" toddler-play Reel (+13 reach) and the "Sleep and screens by age" Reel (+100 reach in its first 3 hours).

Those posts are candidates only. Treat today's +2 as noise until at least 5 more net follows arrive under the 5-Reel rule above.

**Strongest emerging approaches (average watch time; small samples, directional only):**

| Page | Reel | Avg watch | Reach |
|---|---|---|---|
| LF | "Give them 10 minutes" | 6.9 s | 71 |
| LH | "Missed a day? Don't start over" | 5.0 s | 19 |
| HB | "Engineers pasted secret code" | 3.7 s | 7 |
| FF | "Waiting one year costs you" | 3.5 s | 77 |

- **Weakest:** table / "in one look" Reels. FF TFSA vs RRSP vs FHSA held 0.96 s; LF "Sleep and screens by age" held 3.1 s on 101 reach.
- **Direction this supports:** a rule or a concrete number with reassurance, shown as a picture, beats table formats. The v0.6.1 concepts (creative/v061 in the Steadfold repo) are built on that.

## Experiments (pre-registered; evaluate after ≥ 5 Reels with reach ≥ 40 per page, else "inconclusive")

| ID | Page(s) | Hypothesis | Change | Success | Failure | Status |
|---|---|---|---|---|---|---|
| OPT-IG-01 | all | ≤ 15 s, 3-beat Reels with the payoff on frame 0–3 s hold longer than 37–40 s Reels | All queued Reels recut ≤ 15 s (Oct 21–22); Oct 22 recovery rebuilt 10 Reels with the payoff by ~1.5–3 s | Median avg watch ≥ 5 s **and** ≥ 30% watch-through | Median < 3.5 s or < 20% | Running from Oct 23 |
| OPT-IG-02 | all | A numbered series gives a reason to return and follow | Series No. 1 on every page, Mon Oct 26 5 pm, same slot Mon/Wed/Fri | Profile views/day ≥ 2× the baseline above for 7 days **and** ≥ 1 follow from series posts | No change in profile views after 3 episodes | Starts Oct 26 |
| OPT-IG-03 | all | Recovery-floor visuals (v0.5 directions, no repeated clip-art) beat the old template on hold | Oct 24–26 rebuilt items (see `studio/recovery-oct22/*/inventory.md`) vs older template Reels | Rebuilt Reels' median avg watch ≥ 1.5 s above the template Reels in the same week | ≤ 0.5 s difference | **Graded 2026-10-28 at 24 h, n≥5, against earlier weeks** (no template Reels ran in the same week, so the pre-registered comparison wasn't possible). **FF: failed:** rebuilt median avg watch 2.32 s vs 3.39 s (−1.06 s). **LF: borderline:** sunlit 5.21 s vs 3.68 s for original+burgundy (+1.53 s, just over the bar) but −0.62 s against the original-only n=5. Not a clean pass. |
| OPT-IG-04 | Littlefold | One focused promise ("one calm thing a night, bump to toddler") beats mixed money/admin topics | Fewer money/forms posts on LF (B19 + Oct 22 holds) | LF follows from any post ≥ 3 in 14 days | 0 follows in 14 days | Running |
| OPT-IG-05 | all | Proposed (needs studio/founder agreement): fewer, better posts — e.g. 1 Reel + 1 feed a day per page — don't lose reach and free time for quality | Proposal only | Same median Reel reach at half the volume, higher hold | Reach falls > 30% | Proposed |

## Log (newest first)

| Date | Content id(s) | Page | Format | Hook / direction | Production effort | Reach / watch / saves / shares / follows / profile visits | Hypothesis | Change | Result vs baseline | Lesson | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-28 | 72 h re-read of Changes 3–4 + OPT-IG-03 grade | LF FF | Reel | sunlit LF builds; FF rebuilt (no pointing hand) | — | Snapshot 2026-10-28 12:55 UTC (33 insights snapshots in git history); nearest snapshot to the target age, cheat sheets excluded. **72 h:** crying-peak @72.5 h views 143, reach 115, saves 3, shares 13, avg watch 5.02 s; step-away @61.8 h (newest available) 168 / 155 / 3 / 12 / 2.73 s; ff-beneficiary @69.4 h 22 / 19 / 1 / 8 / 1.86 s. 72 h baselines: LF Oct 15–24 (n=11) median 131 / 110 / 3 / 8 / 2.97 s; FF Oct 15–23 (n=10) 51.5 / 41 / 4.5 / 3 / 3.94 s. **24 h cohorts (n≥5):** LF sunlit (n=7: coat-off, teething, crying-peak, step-away, burp, nails, bath) median 139 / 124 / 1 / 2 / 5.21 s vs LF original+burgundy (n=7) 119 / 106 / 2 / 0 / 3.68 s (original only, n=5: 119 / 106 / 3 / 5 / 5.82 s). FF rebuilt (n=6) 14 / 12 / 0 / 0 / 2.32 s vs FF old template (n=6) 25.5 / 21 / 2 / 3 / 3.39 s. Followers flat: LF 6, FF 7. | OPT-IG-03 | measurement + grade | LF: higher reach and views than every earlier baseline; hold beats the combined baseline but not the original-only. FF: rebuilt Reels below the old template on every metric. FF's reach also fell across the board, so an account-level distribution effect can't be separated from style at this volume. | The style alone isn't moving FF. Its hooks or topic fit are the next suspect, not the art. | FF: run a hook/topic test (pre-register before changing); LF: keep the sunlit direction; re-grade with a same-week control |
| 2026-10-27 | lf-reel-1028am-cord-stump, lh-reel-1028am-close-your-eyes, hb-reel-1028am-menu-translate; ff-reel-1028am-promo-end-date, ff-reel-1030-late-payment; lf-reel-1030-rice-grain, lh-reel-1030-fewer-temptations, hb-reel-1030-group-chat | all | Reel 13.0–14.9 s | LF illustrated physical rule shown being done (burp: 426 / 8.65 s); ported to LH and HB as one illustrated scene with the action by ~1.7 s (desk order 4); FF trap-with-a-date opens (order 5); no trial on FF/LH/HB (order 3); page follow line on the last beat | ~5 agent-hours (4 makers, clarity gate, hook picker, CD gate + fixes) | no data yet | burp format holds ≥ 5 s / 30% on other pages; on-screen page follow line converts profile visits | 8 new Reels; 9 Story frames re-lettered | pending | — | Performance desk: Wed 8 am Reels at 15 h (LH/HB ≥ 5 s and ≥ 30% on ≥ 40; FF ≥ 40 reach); follower deltas vs LF profile-visit days |
| 2026-10-26 | lh-reel-1027am-head-start, hb-reel-1027am-return-by, ff-reel-1028-fhsa-room, ff-reel-1029-fsa-expires, lh-reel-1029-picture-win, lf-reel-1029-tummy-to-play | all | Reel | rule/trap stated as a fact in frame 0 (desk order 1); no trial on FF/HB (order 2/4); LF first non-washing-line style | ~4 agent-hours | no data yet | OPT-IG-01; trial vs no-trial (HB 8:45 Tue ≥ 20 at 15 h) | New Reels, 2-round clarity gate + 2-round CD gate | pending | — | Performance desk: 5 h / 15 h reach and hold on these 6; HB 8:45 vs HB trial history |
| 2026-10-26 | lf-reel-1025am-crying-peak, lf-reel-1025-step-away; ff-reel-1024-beneficiary (Changes 3–4) | LF FF | Reel | sunlit animated washing-line (LF); drawn form + bar to scale (FF) | — | Insights snapshot 2026-10-26 04:38 UTC, compared at matched age with earlier Reels (nearest snapshot within ±6 h; cheat sheets excluded). **crying-peak** @16 h: views 132, reach 110, saves 1, shares 3, avg watch 4.99 s, vs Oct 15–24 LF Reels (n=8) median views 96, reach 90.5, saves 0, shares 0, avg watch 2.71 s. **step-away** @5.5 h: views 158, reach 148, saves 1, shares 2, avg watch 2.51 s, vs n=7 median 76 / 70 / 0 / 0 / 2.11 s (highest of the 8 on views, reach, saves and shares). **ff-beneficiary** @29 h: views 19, reach 17, saves 1, shares 3, avg watch 1.64 s, vs Oct 15–23 FF Reels (n=6) median 25.5 / 22 / 2 / 3 / 3.39 s (lowest avg watch of the 7). Follows per Reel: not available (API returns no follows metric for Reels). Account followers flat: LF 6, FF 7 from Oct 24 12:38 to Oct 26 04:38 UTC. | OPT-IG-03 | measurement only | LF: both Sunday Reels beat the earlier LF median. FF: the rebuild under-performed on watch and reach. **Inconclusive:** n=1 per style (<5 Reels); the Oct 24–25 send-trigger test and the time of day also differ; baselines mix the original and burgundy LF templates; the template of each baseline Reel was not checked frame by frame. | Early LF signal is positive and the FF one negative; neither is decidable yet. | 72 h re-read Wed Oct 28; grade OPT-IG-03 after ≥5 post-rebuild Reels per page at matched age |
| 2026-10-25 | ff-reel-1026-cash-at-zero, lh-reel-1026-print-it, ff-reel-1027-car-loan-send, lf-reel-1028-neck-check, lh-reel-1028-grey-phone, hb-reel-1028-hum-a-song, hb-reel-1029-bill-went-up | all | Reel 12.4–14.9 s | concrete check shown by ~2 s, one hook line + one object on frame 0 (desk order 3); send target named ON frame 0 + last beat on 4 of them (desk order 4: FF car loan, LH print it, LF neck check, HB hum); FF no trial (desk order 1) | ~5 agent-hours (4 makers, 3 clarity rounds, CD gate) | no data yet | on-screen send line beats caption-only send lines (1 per 407 reach); frame-0 checks hold ≥ 5 s | New Reels; trial flag removed on ff-reel-1027am-card-full-balance | pending | — | Performance desk: sends per 50 reach on the 4 send-test Reels vs the 3 others; FF Mon 7 pm reach at 5 h (≥ 20) |
| 2026-10-24 | lf-reel-1026am-burp-halfway, lf-reel-1026-baby-nails, lf-reel-1027am-bath-elbow, lf-reel-1027-swaddle-hips; ff-reel-1027am-card-full-balance, lh-reel-1027-write-from-memory, hb-reel-1026-photo-eraser, hb-reel-1027-homework-hints | all | Reel | felt question → one physical rule shown being done (desk order 2); LF all in the illustrated washing-line system (coat-off 102 reach / 5.1 s) | ~6 agent-hours incl. 3 gates | no data yet | OPT-IG-01/03; illustrated physical rule > text cards | 9 new Reels; FF/LH/HB show the action by ~2 s | pending | Gates on rendered frames caught a sleep-safety error the maker missed | Performance desk: hold/reach of the 4 LF illustrated Reels vs LF text-card Reels; FF/LH/HB vs their tight-card medians |
| 2026-10-24 | ff-1025-tfsa-room, lh-1025-done-list | FF LH | carousel | 9–10 slides → 5 (desk order 5) | ~0.3 agent-hours | no data yet | shorter carousels reach more | trimmed | pending | — | Compare reach with Oct 23's 9–10 slide carousels (median 1.5) |
| 2026-10-23 | lf-reel-1023-coat-off-buckle, lf-reel-1024am-teething-cold-cloth, hb-reel-1024am-voice-transcripts, ff-reel-1026am-rule-of-72, lh-reel-1026am-when-where | all | Reel | felt question + one rule (desk order 2); named send target on the last frame (desk test 3); HB Sat 8:45 without the trial flag (desk test 4) | ~3 agent-hours | no data yet | OPT-IG-01; send trigger; trial vs no-trial | New Reels; clarity gate on on-screen text before render | pending | — | Performance desk: sends per 50 reach on these 5; HB 8:45 24 h reach vs HB trial history (7–22) |
| 2026-10-23 | 15 queued pieces rewritten, 4 carousels held (docs/social-recovery/2026-10-23.md) | all | mixed | Clarity gate: 19 of 48 pieces CONFUSING to a stranger | ~2 agent-hours | no data yet | Plain-language on-screen text raises hold | Rewritten / held | pending | Unlabelled numbers and undefined terms ("room", "$750 tax") are the most common failure | Compare hold of rewritten Reels with the pre-Oct 23 cuts |
| 2026-10-22 | lf-reel-1025am-crying-peak, lf-1025-follow-crying, lf-ch-1025-4, lf-reel-1025-step-away; ff-reel-1024-beneficiary | LF FF | Reel/feed/story | LF: dark burgundy → sunlit "washing-line morning" (founder colour direction); FF: pointing hand → drawn form + bar to scale | ~3 agent-hours | see 2026-10-26 row | OPT-IG-03 (+ LF emotion) | Rebuilt (change 3, docs/social-recovery/2026-10-22.md) | Measured 2026-10-26: LF above the earlier-LF median on every metric; FF below the median on most. **Inconclusive** (1 Reel each, <5) | — | Re-read at 72 h; grade after ≥5 Reels per style |
| 2026-10-22 | 6 cheat-sheet Reels | FF LH HB LF | Reel | "X, in one look" tables | — | 1.5–3.6 s hold on 10–41 reach (prior sheets) | Table openers fail | Held (schedule/held-oct22.json) | n/a | Don't open on an empty table | Studio: no new table Reels |
| 2026-10-22 | 25 queued items | all | mixed | Interim floor rebuilds | ~4 agent-hours | no data yet | OPT-IG-01/03 | Rebuilt / re-captioned (docs/social-recovery/2026-10-22.md) | pending | — | Performance desk reads them at 24 h and 72 h |

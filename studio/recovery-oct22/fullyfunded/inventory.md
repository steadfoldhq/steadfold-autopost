# Fully Funded (@fullyfundedhq) · queue recovery, Thu Oct 22 2026

Scope: every `fullyfunded` entry in `schedule/posts.json` not in `state/published.json` at 13:15 Toronto (29 items: 7 feed, 7 Reels, 15 Stories).
Edit window: only items publishing **on or after Sat Oct 24 12:00** were changed. Machine-readable decisions are in `patch.json`. New media is in `media/recovery-oct22/fullyfunded/`, and the before/after sheets are in `before-after/`. Build scripts are in `build/`.

**Method.**
- Every cover and slide was viewed. For Reels, ffmpeg pulled frames at 0.2 s, 1.5 s, 3.5 s and the last second, and ffprobe gave duration, codec and size.
- All FF money maths in the window was re-run in code: fees, cost of waiting, TFSA room, refund.
- Legal facts were re-checked against the sources named in each first comment.

**Standard key.** S = Stop the scroll · O = Own the attention · V = Deliver the value · M = Make it memorable · K = Keep getting better. Each is scored 1–5.

**How the floor was reconciled.**
- The v0.5 "Drawn to Scale" blueprint is used inside brand-system v4. That means:
  - the soft paper field (FF paper `#F5F7FF` / cream `#F7F1E5`), not the saturated cobalt sheet;
  - a Fraunces ink hook with a soft-coral pill;
  - the round stamp, cobalt line drawings with coral annotations, and DejaVu Mono labels.
- Two v0.5 rules were **not** adopted, because v4 overrides them:
  - v0.5's "6% example" rate (v4: 8–10%; and the word "example" is banned, 12b);
  - the title block on Reel covers (v0.5 critique: too heavy).

## Inventory

| # | id | publish (Toronto) | format | hook (cover / frame 0) | caption line 1 | class | S O V M K | reason |
|---|---|---|---|---|---|---|---|---|
| 1 | ff-1022-streak-every-dollar | Thu 22 · 17:00 | carousel 7 | "Where did all my money go?" (emoji cash) | "Where did all my money go?" 30 days of writing down… | KEEP | 3 3 4 3 3 | <24 h, no rule broken. StatCan-sourced. The weak spots are the generic emoji cover and 7 slides |
| 2 | ff-reel-1022-refund-29k | Thu 22 · 19:00 | Reel 13.7 s | "Spend the refund, or grow it?" | Spend the refund, or turn it into $29,000? | KEEP | 3 3 4 3 3 | ≤15 s. A number is on screen by 3.5 s. Maths ✓ (≈$29,359). Pointing-hand template |
| 3 | ff-1023-cpp-enough | Fri 23 · 12:00 | carousel 9 | "Counting on CPP to pay your rent?" | same | KEEP | 3 3 4 3 3 | canada.ca figures. The caption has a cosmetic typo, "$1,620.0", for the owner to fix if wanted |
| 4 | ff-1023-roadmap-fhsa | Fri 23 · 17:00 | carousel 7 (route) | "First home someday? Open an FHSA now." | same + 👉 | KEEP | 3 3 4 3 3 | Facts match Finance Canada/CRA. "Returns vary" is present |
| 5 | ff-reel-1023-cpp-60-or-70 | Fri 23 · 19:00 | Reel 13.1 s | "Your parents taking CPP early?" | same | KEEP | 4 3 4 3 3 | The hook is in the viewer's words. "60: $965" shows at 3.5 s. Hourglass object |
| 6 | ff-reel-1024am-sick-pay-gap | Sat 24 · 08:15 (trial) | Reel 13.1 s | "Too sick to work for months?" | same | KEEP | 3 3 4 3 3 | Before the Sat 12:00 line, no rule broken. Pointing-hand template |
| 7 | ff-1024-paycheque-trail | Sat 24 · 12:00 | carousel 5 (panorama) | "Payday. Where should the money go first?" | …go first? 🇨🇦 A simple order a lot of planners use: | **IMPROVE** (caption) | 3 3 3 3 3 → 3 3 4 3 3 | 🇨🇦 on a non-Canada-specific order (B19). "A lot of planners use" is unsourced. No follow reason, no debt catch. Slides kept because the 12:15 Story shows this cover |
| 8 | ff-1024-follow-fees | Sat 24 · 17:00 | carousel 6 (follow-the-line) | "That 2% fee? About $394,000 by 60." | same | KEEP | 4 4 5 4 3 | Maths re-run ✓ ($1,081,819 / $882,535 / $688,165). Quiet style; good rotation |
| 9 | ff-reel-1024-beneficiary | Sat 24 · 19:00 | Reel 12.6 s | "Never named a TFSA beneficiary?" | same | KEEP | 4 3 4 3 3 | Rule open. "$750 tax" shows at 3.5 s. ontario.ca-sourced. Pointing hand again (see watch-outs) |
| 10 | ff-pan-1025am-paycheque-trail | Sun 25 · 08:15 (trial) | Reel 15.0 s pan | same as #7 (piggy on a path) | identical to #7's caption | **REPLACE** | 2 2 2 2 2 → 4 4 4 4 4 | Duplicates #7 (same art, same caption) the morning after. Piggy cut-out. Replaced with the Performance desk's order 5 ("Not married? No will?" ≤15 s Trial Reel) |
| 11 | ff-1025-tfsa-room | Sun 25 · 12:00 | carousel 9 | "Your TFSA room could be $109,000" | same | KEEP | 4 3 5 3 3 | CRA limits sum ✓ $109,000. Growth ✓. Money Foundations Part 7 |
| 12 | ff-1025-hold-cost-of-waiting | Sun 25 · 17:00 | carousel 8 (jar slider) | "Instead of… 'I'll start next year.'" | "I'll start next year." Waiting from 25 to 27 costs… | KEEP | 3 3 4 3 3 | Maths ✓. The log already marks it as the last "hold the dots" tile |
| 13 | ff-reel-1025-tfsa-withdrawal-trap | Sun 25 · 19:00 | Reel 12.4 s | "Putting TFSA money back? Wait." | same | **IMPROVE** (re-cut) | 3 2 4 2 3 → 4 4 4 4 4 | Third pointing-hand Reel in five, with the hook static until ~3 s. Now a calendar drawn to scale |
| 14 | ff-richhabits-01 | Mon 26 · 17:00 | carousel 3 (series cover) | "Paid Friday. Broke by Wednesday?" + piggy | same | **IMPROVE** | 4 3 3 3 4 → 4 4 4 4 4 | Piggy is overused. Slide 3's "Savings rose 3.5% → 13.6%" lacked "saving rate / one study". The caption said "about 3.5 years"; the paper says 40 months |
| 15–19 | ff-ch-1023-1…5 | Fri 23 · 11:00–12:15 | Story chain | quiz → $858 → $1,620 → 3 steps → post | n/a | KEEP | 3 3 4 3 3 | Matches #3, sources named |
| 20–24 | ff-ch-1024-1…5 | Sat 24 · 11:00–12:15 | Story chain | "Payday! Where does it all go?" → order → automatic → post | n/a | KEEP | 3 3 3 3 3 | Matches #7. Frame 1's street photo looks like New York (a US flag is visible); acceptable for a Story, but use a Canadian or neutral scene next time |
| 25–29 | ff-ch-1025-1…5 | Sun 25 · 11:00–12:15 | Story chain | quiz → $109,000 → never expires → 3 steps → post | n/a | KEEP | 3 3 4 3 3 | Matches #11. Frame 5's "tonight: the withdrawal trap" still matches the re-cut #13 |

**Counts:** 25 KEEP, 3 IMPROVE (#7, #13, #14), 1 REPLACE (#10), 0 HOLD.

**Rule checks across the queue.**
- No "Canada edition" labels.
- No Reel over 15 s.
- "Not guaranteed. Returns vary." appears wherever returns are shown.
- `grep example|e.g.|hypothetical` on the new copy: 0 hits.
- One duplicate (#7/#10), now resolved.

## Before → after

### #10 ff-pan-1025am-paycheque-trail → "Not married? No will?" (REPLACE)
Sheet: `before-after/ff-pan-1025am-paycheque-trail.jpg`.

**Before:**
- A 15.0 s pan of the piggy on a dotted path.
- It is the same illustration and the same caption, word for word, as the Saturday noon carousel 20 hours earlier.
- Frame 0 is legible, but there is no payoff until stop 1 (~3.5 s).

**After:** `ff-pan-1025am-wills-s15.mp4`, 14.84 s, H.264/AAC, 1080×1920, 6.6 MB, −13.9 LUFS, track `ff-c-confident-build` (FF pick).
- **Frame 0:** the hook "Not married? / No will?" with the estate diagram already drawn.
- **0.3 s:** a coral **$0** stamps into the dashed COMMON-LAW room (the payoff).
- **4.1 s:** whip to "In Ontario:", where the MARRIED bar is dimensioned "FIRST $350,000" and COMMON-LAW is a sliver labelled $0.
- **7.6 s:** slam to "The fix: one will.", where a document draws and signs itself.
- **9.8 s:** iris to "Do this: Book a wills call this week."
- **13.9 s:** zoom loop back to the hook.
- **Sources:** Steps to Justice (CLEO), plus Ontario SLRA Part II and Part V. The caption flags that other provinces differ.
- **Why this one:**
  - It's the Performance desk's TEST order 5 (3rd day): FF's biggest batch (115, 96% non-follower), which held only 4.1 s at 38 s.
  - It also uses the rule-plus-number open (order 4).
  - This slot already carries `"trial": "auto"`.

### #13 ff-reel-1025-tfsa-withdrawal-trap (IMPROVE)
Sheet: `before-after/ff-reel-1025-tfsa-withdrawal-trap.jpg`.

**Before:** 12.4 s. The pointing-hand template, the same as #2, #6 and #9. The hook card holds unchanged until ~3 s.

**After:** `ff-reel-1025-tfsa-trap-s15.mp4`, 14.84 s, same codec, track and loudness.
- **Frame 0:** the hook, with a Jan–Dec ruler drawn to scale (65 px a month). A coral arrow out at MAR draws in by 0.5 s and a cobalt arrow back at JUN.
- **3.5 s:** "Over by $5,000? $50 a month tax." June–Dec fills with 7 coral cells under a dimension line, and the counter rolls $50 → **$350**.
- **7.6 s:** "Room returns January 1." with an arc to next January.
- **10.4 s:** "Do this: Check CRA My Account first."
- Then it loops.
- **Caption:** the same facts. The first comment now cites canada.ca ("Before you contribute to a TFSA") instead of a bank page.

### #14 ff-richhabits-01 (IMPROVE)
Sheet: `before-after/ff-richhabits-01.jpg`.
- Same series layout: badge kicker, pills, "mon · wed · fri" save-line, stamp.
- The piggy becomes a small drawn chart, "PAYCHEQUE LEFT", with bars falling FRI → WED and an empty coral WED. It is an illustrative shape with no figures.
- Slide 3 now reads "Saving rate 3.5% → 13.6%", "in one study, as it rose with every raise", with "Source: Thaler & Benartzi, 2004" on the tile.
- The caption's "in about 3.5 years" is now "over 40 months", which matches the first comment and the paper.

### #7 ff-1024-paycheque-trail (IMPROVE, caption only)
Sheet: `before-after/ff-1024-paycheque-trail.jpg`.
- Line 1 is now "Payday. Where should the money go first? Follow this order." (no 🇨🇦, no unsourced "a lot of planners use").
- Adds a debt catch ("carrying card debt at 20% or more? Paying it down usually comes before step 3"), the follow reason, and CRA as the TFSA-limit source.
- The slides are unchanged on purpose: the 12:15 Story (ff-ch-1024-5) shows this cover.

## Critique pass (done once, applied before the final render)
- The first preview had a cramped "money back?" leading (the y descender was clipped), so leading went from .98 to 1.07.
- Kinetic pills split into word islands ("this │ week."), so adjacent pill words are now joined.
- "Book one wills / call" wrapped badly. It's now "Book a wills call / this week." at 108 px.
- The ruler and mono labels were too small for a phone, so the ruler is 840 px wide and the labels 40 px.
- On-screen words were cut until both Reels pass the kit's 0.4 s/word + 0.6 s reading rule within ≤15 s. The loop scene is exempt, because it repeats the hook.
- On the cover, the save-line sat below y 1400. It was moved into the safe zone, and the $0 was lifted off the room border.
- **Known cosmetic flaw left in the video:** on the wills Reel's frame 0 the coral $0 overlaps the dashed room's bottom edge by a few px. It reads as a stamp, so I did not re-render (~18 min) for it.

## Watch-outs (not changed; outside the window or not rule breaks)
- **Rotation:** four of FF's six remaining Reels (#2, #5 hourglass, #6, #9) still use the tight serif-card template, and three of those use the pointing hand. The weekend now alternates: Sat am and Sat pm stay on the hand; Sun am and Sun pm move to the drawn-to-scale Reels.
- **#9 beneficiary:** the next re-cut candidate, in the same blueprint grammar (estate path vs. named-beneficiary path).
- **Entry id:** after the patch, entry `ff-pan-1025am-paycheque-trail` holds the wills Reel. The id is kept so the patch applies cleanly. The id text no longer describes the content.
- **Carousel length:** the Performance desk wants ≤5 slides; #3, #11 and #12 run 8–9 (series parts already promoted in the Stories).
- **Blocked fetch:** the Steps to Justice page fetch was blocked by a permission timeout. The CLEO facts were cross-checked against Advisor.ca's report of the SLRA change ($350,000, deaths from March 1, 2021; common-law partners take nothing on intestacy, but may claim dependant support) and against the source text already used in the published Oct 20 Reel.

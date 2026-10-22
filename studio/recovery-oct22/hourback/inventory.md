# Hourback (@hourbackhq): queue recovery, Thu Oct 22, 2026

Written by the Hourback recovery editor at about 2 pm Toronto. Nothing in `schedule/`, `state/` or `media/reels|stories` was touched. Every change is in `patch.json`, the new media is in `media/recovery-oct22/hourback/`, and the comparisons are in `before-after/`.

**Scope:** every unpublished Hourback entry in `schedule/posts.json`: 12 feed posts and Reels, 14 Stories, plus 1 new entry for an empty slot. Three items were already held (`schedule/held-oct22.json`): `hb-cheat-1022-travel-admin` (Thu 7 pm), `hb-cheat-1024am-shortcuts` (Sat 8:45 am) and `hb-cheat-1025-voice-words` (Sun 7 pm).

**Checks run:**
- Looked at every cover and Story tile.
- Looked at Reel frames at 0.0, 0.2, 1.5, 3.5, 6, 9 s and the last second (ffmpeg).
- ffprobe on every video.
- Read every caption and first comment.
- Fact-checked anything new or doubtful. The 900M ChatGPT weekly users figure is confirmed by TechCrunch (Feb 27, 2026). The other figures match the sources named in the first comments.

**Scores** follow the Standard: Stop · Own · Value · Memorable · Improve, each out of 5.

## Feed posts and Reels

| id | publish (ET) | format | hook (cover / frame 0) | caption line 1 | class | scores | reason |
|---|---|---|---|---|---|---|---|
| hb-1022-split-prompt | Thu 22 17:45 | carousel 7 | Me: "Write an email to my landlord." | "Write an email to my landlord." Sound like your last prompt? | KEEP | 3·3·4·3·3 | Goes out in hours and breaks no rule. 7 slides against the ≤5 order; the "swipe to fix it" interactive tail |
| hb-reel-1023am-photo-search (trial) | Fri 23 08:45 | Reel 13.2 s | Weird light on your dashboard? | same | KEEP | 3·2·3·2·3 | Facts verified. The hook frame doesn't change from 0 to 3 s, the pointing hand is overused, and it's an AI-news topic. Recut it next week |
| hb-1023-renewal-reminders | Fri 23 13:00 | carousel 9 | How does ChatGPT know stuff? | How does ChatGPT actually know stuff? | KEEP | 3·3·4·3·3 | The id doesn't match the content. 9 slides |
| hb-1023-follow-frontier | Fri 23 17:45 | carousel 6 | 25% faster with AI. On some tasks, worse. | Consultants using AI were 25% faster… | KEEP | 4·3·4·3·3 | Numbers match HBS WP 24-013 |
| hb-reel-1023-duplicates | Fri 23 19:00 | Reel 12.8 s | Skimming just the AI summary? | same | KEEP | 3·2·4·3·3 | Apple/BBC facts correct. Static hook from 0 to 3 s |
| hb-1024-share-eta | Sat 24 13:00 | carousel 9 | "Was this you?" | Your bank texts "Was this you?"… | KEEP | 3·3·3·3·3 | Book ideas credited. 9 slides |
| hb-1024-climb-5-levels | Sat 24 17:45 | carousel 7 | Chatbot. Reasoner. Agent. What comes next? | same | KEEP | 4·3·4·3·3 | Labelled "reported, not official" |
| **hb-reel-1024-fridge-dinner** | Sat 24 19:00 | Reel 11.9 s → **14.0 s** | Your next coworker might be AI. → **Open fridge, no plan? You already have dinner.** | → Open fridge, no plan? You already have dinner. | **REPLACE** | 2·2·2·2·2 → **4·4·4·4·4** | Off-identity: an AI-news quote with no demo. Static hook, and the Do this was vague ("write one task's steps down") |
| **hb-reel-1025am-talk-dont-type** (trial) | Sun 25 08:45 | Reel 13.5 s → **13.0 s** | That sparkle button? It's AI. (same copy) | same | **IMPROVE** | 3·2·3·2·2 → **4·4·4·3·4** | **Rule break:** the caption promised "Part 2 tonight at 7: the full map", which was the held voice-words cheat sheet. The hook was also static from 0 to 3 s |
| hb-1025-family-calendar | Sun 25 13:00 | carousel 9 | Too much AI news? Keep 7 rules. | same | KEEP | 3·3·4·3·3 | Week recap, sourced. 9 slides |
| hb-1025-hold-task-length | Sun 25 17:45 | carousel 9 | AI, working alone: 2 seconds → 1 hour. | same | KEEP | 3·3·4·3·3 | METR figures and caveats correct. The interactive hook stays, per the Oct 22 studio decision |
| hb-day8-ask-me-first | Mon 26 17:45 | carousel 3 | AI's answer felt generic again? | same | KEEP | 4·3·4·4·4 | Real run, quoted and labelled |
| **hb-reel-1025-week-card (NEW)** | Sun 25 19:00 (empty slot) | Reel 14.5 s | **Sunday night? Your week fits on one card.** | same | **REPLACE (fills held slot)** | **4·4·5·4·4** | Take Two Reel on a real Claude run with made-up messages. The run's real slip is the "check" beat |

Sat Oct 24 8:45 am stays **empty**. One strong Reel was better than two thin ones.

## Stories

| id | publish (ET) | class | note |
|---|---|---|---|
| hb-ch-1022-5 | Thu 22 13:15 | **HOLD (if not already live)** | The pill reads "tonight: the jobs cheat sheet", which is held. Local state is from 1:14 pm, so it has probably already gone out |
| hb-ch-1023-1..3 | Fri 23 12:00–12:02 | KEEP | 900M (TechCrunch, Feb 27, 2026) and 1 in 9 both check out |
| hb-ch-1023-4 | Fri 23 13:15 | KEEP | "tonight: where AI's eyes go wrong" only loosely fits the Apple-summary Reel. Minor, and less than 24 h out |
| hb-ch-1024-1..4 | Sat 24 12:00–12:03 | KEEP | |
| **hb-ch-1024-5** | Sat 24 13:15 | **IMPROVE** | The pill pointed to the replaced Nvidia Reel. Now it reads "tonight: dinner from your fridge" (only the pill is repainted) |
| hb-ch-1025-1..3 | Sun 25 12:00–12:02 | KEEP | 26% vs 75% matches OpenAI (Sept 2025) |
| **hb-ch-1025-4** | Sun 25 13:15 | **IMPROVE** | The pill pointed to the held "where AI lives in your apps" cheat sheet. Now it reads "tonight: your week on one card" |

**Counts:** KEEP 9 feed/Reel + 11 Stories · IMPROVE 1 Reel + 2 Stories · REPLACE 1 Reel + 1 new Reel · HOLD 1 Story (conditional).

## What the new Reels are (before → after)

### Look
They reconcile brand-system v4 and v0.5. The v4 editorial look stays:
- DM Serif Display in #2A1D47 with pills under the words;
- HB soft fields (peach, periwinkle, cream) with paper grain;
- Caveat Brush notes;
- the round stamp;
- the B/W halftone phone object. The overused pointing hand is gone.

The structure is v0.5 **Take Two**:
- **payoff card on frame 0;**
- the yellow rewind coin spins back to a greyed TAKE 1 (the arrow runs anticlockwise, per the Oct 11 rule);
- a clapper slams TAKE 2;
- the one sentence types live;
- the real answer lands on the track's drop (7.93 s);
- Do this, then the check;
- the last frame returns to the frame-0 layout, so it loops.

Something moves within 0.1 s, there is a new beat every 0.4–1.2 s, and at least 7 transition kinds are used (zoom, spin, whip, slam with shake, wipe, wipe-down, iris).

### Real runs
`runs/run-a-fridge.txt` and `runs/run-b-week.txt` hold the inputs and outputs verbatim:
- Claude, by Anthropic, run Oct 22, 2026, by this agent, on made-up inputs.
- The fridge reply is shortened on screen and labelled so.
- The week reply is quoted exactly.
- Both runs' real flaws are shown as "the check": the fridge reply added oil, which wasn't listed, and the week reply put "before Tue" on Tue.

### Specs
| file | length | size | format | loudness |
|---|---|---|---|---|
| hb-reel-1024-fridge-dinner-r.mp4 | 14.0 s | 9.1 MB | H.264/AAC 1080×1920, 30 fps | −14.8 LUFS, −1.4 dBTP |
| hb-reel-1025-week-card.mp4 | 14.5 s | 9.8 MB | H.264/AAC 1080×1920, 30 fps | −14.7 LUFS, −1.4 dBTP |
| hb-reel-1025am-talk-dont-type-r.mp4 | 13.0 s | 6.2 MB | H.264/AAC 1080×1920, 30 fps | −14.6 LUFS, −1.5 dBTP |

- Covers are 1080×1920, rendered at 2× and downscaled with Lanczos.
- Music is the HB v4 library master `hb-x-ta-da-funk` (−14.2 LUFS master, QA pass).
- Total new media: about 27 MB.

### Critique and revision
The first pass had three problems, all fixed:
- the sparkle hook was cut off (wrapped line);
- a mid-roll fake number ("807 million") was replaced with a static "1 billion";
- app labels collided with the pills.

The second pass found white gaps behind the whip, wipe and iris transitions, because outgoing scenes ended on the cut. Each scene now stays 0.5 s under the incoming one. The loop frame was re-checked against frame 0.

## Uncertain / for the owner
- **hb-ch-1022-5** has probably already published. If so, there's nothing to do.
- The "made up / real reply" labelling follows brand v4 12b. The runs were done by this agent, not in a separate consumer app. The first comment says "run by our studio" rather than "fresh chat".
- **Off-identity queue (not rule breaks):** most of the queue is the "AI, for real" AI-literacy series rather than Hourback's "save time / real demos" identity. Several carousels also run 7–9 slides against the Performance desk's ≤5 order. Both are left for the daily studio, because changing them would mean rewriting an in-flight series.
- Next week's recut candidates: photo-search and duplicates. Both have a hook frame that stays the same for 3 s and use the pointing hand.

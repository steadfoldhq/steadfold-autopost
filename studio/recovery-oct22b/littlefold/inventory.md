# Littlefold: warm rebuild of the Sun Oct 25 crying-day items (Oct 22b, evening)

**Founder note:** the burgundy Night Light revision "improved the message but does not fully reflect the preferred emotional direction."

**What changed:**
- The **look** changed. The facts, words, sources, captions and first comments did not: they are copied verbatim from `schedule/posts.json` by `build/make_patch.py`.
- New look: **Washing-line Morning**, an original illustrated sunlit world.
  - A pastel dawn, morning or afternoon sky over sage hills, with a cottage.
  - A sleepy sun character that **wakes up on the "Do this" beat**.
  - The Littlefold washing line, with one tiny pastel garment pegged on per beat.
  - No dark or burgundy fields, and no people or children.
- Kept:
  - Fraunces hooks with pills, Lora italic, Caveat Brush and Poppins chips;
  - the round Littlefold stamp and paper grain;
  - rule + reassurance on frame 0 and the loop to frame 0.

**Where things are:**
- Media: `media/recovery-oct22b/littlefold/`
- Patch: `patch.json` (4 × `improve`)
- Side-by-sides and QA sheets: `before-after/`
- Build scripts: `build/` (`sunart.py`, `stills.py`, `reel.py`, `qa.py`, `make_patch.py`)

| Publish (ET) | id | Old (Oct 22 Night Light) | New | Media |
|---|---|---|---|---|
| Sun 8:00 | lf-reel-1025am-crying-peak | Berry lamp circle, 14.6 s | Dawn sky → morning, the sun rises a step per beat and wakes on "Next cry: pick them up first." Same 5 beats, CPS/AAP chips, same track `lf-c-sunny-morning-el` (cuts on its 120 bpm grid) plus soft peg pops. 14.4 s | `lf-reel-1025am-cant-spoil-sun.mp4` and `-cover.jpg` |
| Sun 11:30 | lf-1025-follow-crying | 3 berry/morning tiles | Slide 1 draws "the peak" as a soft pink hill with a flag, with the sun beyond it (labels: often 3 to 12 weeks / usually over by 3 to 4 months). Slide 2 is the same 3 steps on a cream card. Slide 3 is morning with the sun awake | `crying-peak-sun-01..03.jpg` |
| Sun 11:45 | lf-ch-1025-4 (Story) | Berry hand-off | Sunny hand-off: "It has a peak." with the new slide-1 mini and "full breakdown in today's post ↑" | `story-lf-ch-1025-4-sun.jpg` |
| Sun 19:00 | lf-reel-1025-step-away | Berry lamp circle, `lf-a-cosy-el`, 14.8 s | Soft afternoon sky, a resting sun, garments swaying on "Step out. Breathe." On "Do this" the sky brightens and the sun opens its eyes. "Never shake a baby. Never." stays full size and gets no peg pop. Music is now the warmer allowed `lf-b-tender-el` (84.7 bpm grid). 14.5 s | `lf-reel-1025-step-away-sun.mp4` and `-cover.jpg` |

## Verification

| File | Codec | Size | Length | Loudness | Peak | `music_check --kind mix` |
|---|---|---|---|---|---|---|
| cant-spoil-sun.mp4 | H.264 High + AAC 48 k stereo, 1080×1920, 30 fps | 3.8 MB | 14.37 s | −13.8 LUFS | tp −2.7 | PASS |
| step-away-sun.mp4 | H.264 High + AAC 48 k stereo, 1080×1920, 30 fps | 3.1 MB | 14.52 s | −13.8 LUFS | tp −2.8 | PASS |

- **Sizes:** covers and the Story are 1080×1920 JPG; carousel slides are 1080×1350. All were rendered at 2× and downsampled with Lanczos (q92, no chroma subsampling).
- **Frames I looked at:**
  - 0, 0.2, 1.5, 3.5, every beat, mid and last of both Reels (`before-after/*-qa.jpg`);
  - every still;
  - the before/after sheets.
- **What the frames show:**
  - the hook is fully legible at 0 s and the chip is in by 0.5 s;
  - the last frame matches the frame-0 layout, so the loop is clean;
  - text stays inside x 80–1000 and y 300–1400 (Reels) and y 250–1650 (Story).
- **Contrast:** ink on every sky stop is ≥ 9.3:1. The berry kicker is used only as large text (≥ 3.7:1).

## Critique and revision (one pass)
1. **Tree.** It sat in front of the sun's face. Moved it beside the cottage.
2. **Fifth garment.** The mitten read as a second sock. Replaced it with a little dress.
3. **Carousel slide 1.**
   - The "usually over by" label collided with the hill path. Moved it into clear sky.
   - The extra save-line crowded the hill. Dropped it; the same line is already in the caption, and slide 3 keeps "save this for 3 am".
4. **Slide 2.** Removed an empty washing line.
5. **Story.** The stamp overlapped the mini card. Moved it left.
6. **Reels, first render:**
   - "Next cry: pick them up first." wrapped to 4 lines. Lines are now no-wrap and auto-fit.
   - "Answer their cries" shrank too small. Re-broken into balanced lines.
   - Orphan words in the sub-lines. Widened the sub-line box and reduced its size.
   - The rising sun hid behind the chip on the last beat. Reduced the rise.
   - Both Reels were re-rendered and checked again.

## For the coordinator
- **Apply:** `patch.json`. I did not edit `posts.json` or git.
- **Stale Story caption.** The `lf-ch-1025-4` caption in the queue still reads "Baby won't stop crying?". It is an internal Story caption and was not part of my patch, so it is left as is.
- **Music change.** The 7 pm Reel now uses `lf-b-tender-el` instead of `lf-a-cosy-el`. Both are in the allowed ElevenLabs library, but `lf-b-tender-el` is not on the `music-picks.json` LF list. If only the picks list is allowed, swap it back with `reel.py stepaway` after changing the `music=` line.
- **Grid on Sunday:** four warm tiles (dawn, morning, sunny Story, afternoon). No dark tiles.

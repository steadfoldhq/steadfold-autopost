# Steadfold brand system v4: the one standard every agent follows (Oct 15, 2026)

Dharma approved this system on Oct 15, 2026. The visual reference is **`docs/grids-FINAL.png`**, the four approved profile grids. Its list tiles are the approved **sticky-note lists**.

This file covers the look and the format mix. For words and facts, `CONTENT-STANDARD-v3.md`, `PAYOFF-FIRST.md` and `copy-lint.py` still apply (in `steadfold-library/current/guides/`). Where those files talk about visuals, this file wins.

**Scope.** The same page palettes and styles apply to every surface:
- feed posts, Reels and Reel covers;
- YouTube Shorts and TikTok/Pinterest copies;
- **product listing images and covers on Gumroad and Etsy.**

A Fully Funded spreadsheet listing is Cobalt, white and coral. A Littlefold printable is Sherbet. They use the same fonts, the same signature objects and the same 2× render rule.

---

## 1. The four pages

Each page keeps its **original** palette and feel. Never borrow another page's colours.

### Fully Funded: "Money, made clear." Cobalt
| Role | Hex |
|---|---|
| Cobalt (main) | `#2B3FE0` |
| White / light surface | `#FFFFFF` / `#F5F7FF` |
| Ink | `#0E1440` |
| Coral highlight | `#FF6A3D` |
| Soft coral (pills, highlighter, italics on dark) | `#FFB08F` |
| Deep cobalt (Ep. deep surface) | `#16206B` |
| Cream (Ep. light surface) | `#F7F1E5` |
| Occasional accent: royal green | `#0F4D3A` |
| Occasional accent: butter (glove) | `#F8E07A` / `#FFF1C9`, gold `#F6D44C` |

- Royal green and butter appear only on the occasional glove post: a butter glove on green, or a green glove on butter. Use them at most once in 9 tiles.
- **Fonts:**
  - Inter Display 800 for big hooks;
  - Instrument Serif (and its italic) for editorial and one-word hooks;
  - Fraunces for Ep. titles;
  - Caveat Brush for save-lines;
  - Inter for body text.
- **Signature objects:** the halftone piggy bank, a coral glove, follow-the-line coloured lines, big example-math numbers, and the round brand stamp ("FULLY FUNDED · MONEY, MADE CLEAR ·").
- **Series: Rich Habits, Decoded** (No.1 shipped Oct 19). It uses the Ep.01 B/W photo editorial cover with the label "Rich Habits, Decoded · No.N" in Caveat.

### Littlefold: "Small days, gently." Warm Sherbet
| Role | Hex |
|---|---|
| Cream / butter base | `#FFF4E0` / `#FFF8E4` |
| Soft pink | `#FFD6E3` (blob `#FFC9D6`) |
| Peach | `#FFD3AE` / `#FFA35C` |
| Coral touch | `#FF8A70` / `#E8743B` |
| Berry (italic accent, labels) | `#D9497A` |
| Butter yellow blob | `#FFE27E` |
| Ink | `#2C2A3A` |
| Ep. deep / light | berry `#7A2149` / blush `#FCE5EB` |

- **Feel:** calm, happy and soft. Use blobs in the corners and a faint paper dot.
- **Fonts:**
  - Lora 600 with an italic berry word for hooks;
  - Instrument Serif for photo words;
  - Caveat and Caveat Brush for notes;
  - Inter for body text.
- **Signature objects:** soft paw prints, award rosettes, the halftone baby shoe, real silhouette photos at golden hour, and the arch card.
- **Series: Small Wins** (No.1 shipped Oct 21). The cover is a coral pill "SMALL WINS · No.N", then the hook "You drank *warm* tea today." with paws and "it counts ♡".
- **Content:** official sources only (NHS, CDC, PHAC, CPS, WHO). No medical advice. Nothing aimed at children.

### Locked Hour: "One hour at a time." Zine
| Role | Hex |
|---|---|
| Butter yellow (main) | `#FFE27A` |
| Cream | `#FFF4E0` |
| Highlighter yellow | `#FFD43B` |
| Highlighter pink | `#FF5CA8` (deep pink `#E8336F`) |
| Black ink | `#141414` |

- **Feel:** a zine with highlighter pops, thick ink borders and hard offset shadows, on a dot grid (`rgba(20,20,20,.12)` 2.4 px dots on a 30 px grid).
- **Never black-heavy.** Black is ink, labels and the occasional CTA scene, never a whole grid tile's background. (Photo tiles may be dark because of the photo.)
- **Fonts:** Inter Display 900 for hooks and Inter 700–800 for body text. Caveat Brush is allowed for one-line notes.
- **Signature objects:** the alarm clock (halftone or clean cut-out), the pink glove, the timer, the if-then card and the panorama path.
- **Series: One Word** (No.1 shipped Oct 17). The cover has a black label "ONE WORD · No.N", one huge word with a pink highlighter stripe, one line and one object or photo.

### Hourback: "Get your evenings back." Periwinkle/indigo + yellow
| Role | Hex |
|---|---|
| Indigo / periwinkle (main) | `#5E54C9` |
| Yellow highlight | `#FFC94D` |
| Orange touch | `#FF8A3D` |
| Cream | `#FFF8EF` / `#FFEEDC` |
| Ink | `#2A2238` |
| Ep. deep / light | plum `#3A2240` / peach `#FFE6D3` |

- **Fonts:** Poppins 700 for hooks; Instrument Serif for editorial and one-word hooks; Caveat Brush for notes; Inter for body text and prompts.
- **Signature objects:** chat bubbles, the prompt card with yellow `[bracket]` chips, the halftone pointing hand, a yellow glove and the pixelated reveal card.
- **Series: Prompt of the Week** (No.1 shipped Oct 20). The kicker is "Prompt of the Week · No.N"; the format is swipe-to-reveal or chat bubbles.
- **Captions:** keep the "Example made up…" line when an example is shown, and the privacy tip.

---

## 2. The full style menu (mix every style; remove nothing)

All paths are under `/home/claude/content/design/` unless they say otherwise. A **loud** tile stops the scroll; a **quiet** tile rewards the save.

| # | Style | L/Q | Made by |
|---|---|---|---|
| 1 | **Look B big-headline cover**: pills on key words, handwritten save-line + arrow, halftone cut-out object, round stamp | Loud | `samples-v5/build_grid_tiles.py` `cover(c, v)` with `B(...)`/`FF/LF/LH/HB(...)` copy and `V(...)` colours; colourways in `samples-v5/build_mix.py` `LOOKB`; object cut-outs `samples-v5/lib.py` `halftone_cutout()`; stamp `engine/feed.py` (`"stamp": true`) |
| 2 | **"Put a finger down" glove / countdown**: CLEAN cut-out, background continuous between the fingers, soft contact shadow | Loud | `samples-v5/build_final.py` `glove_tile()` + `tint_glove()` on `assets/cutouts/glove-pink-{1,2,3}.png` (mattes from `samples-v5/matte.py`); recolour via `samples-v5/recolor.py`; Littlefold soft countdown is `T["lf-count"]` (giant numeral, no photo) |
| 3 | **Ep.01 B/W photo editorial**: grain B/W photo panel, Fraunces title, Caveat label | Loud | `samples-v5/build_final.py` `photo_editorial()` + `bw()` (`lib.bw_grain`); full episodes `engine/episode.py` (`ep-cover`, `ep-step`, `ep-statement`, `ep-reframe`, `ep-handwritten`) via `render.py` |
| 4 | **One-word photo / slow-pan**: one huge word over a real photo; in video the background slow-pans and the text stays pixel-still | Loud | Still: `samples-v5/build_final.py` `word_tile()` (`build_mix.py` `still()`); video: `content/video/src/slowpan.py` `Scene/Move/render` with `oct16-21/reels_lib.py` `photo_layers()` |
| 5 | **Kinetic big text** (Reels only) | Loud | `content/video/src/vlab.py` `Video`, `el`, `words`, `count`, rendered at 2× by `oct16-21/reels_lib.py` `render_vlab_2x()` |
| 6 | **Panorama timeline** (seamless multi-slide path) | Quiet | `engine/interactive.py` template `panorama` via `render.py` |
| 7 | **Ep.01 reframes "Instead of… Say…"** | Quiet | `samples-v5/build_mix.py` `reframe()`; episode version `ep-reframe` |
| 8 | **Original simple templates** (cover, big-number, steps, checklist, compare, output, image, table, quote, cta) | Quiet | `engine/templates.py` via `render.py posts.json --out DIR`; covers `engine/covers.py`; palettes `engine/feed.py` `PALETTES`/`rotation()` |
| 9 | **Follow the line** | Quiet | `engine/interactive.py` template `follow-the-line` |
| 10 | **Awards** (rosettes / stars / medals) | Quiet | `engine/interactive.py` template `awards`; tile version `samples-v5/build_final.py` `rosettes()` |
| 11 | **Swipe to reveal** | Quiet | `engine/interactive.py` template `swipe-to-reveal` |
| 12 | **Emoji meme** | Quiet | `samples-v5/build_mix.py` `meme()` (bigger copy in `build_final.py` `T["lf-meme"]`, `T["lh-meme"]`) |
| 13 | **Sticky-note list**: lined note card, red margin line, tape strip, Caveat Brush title, Caveat items with ticks, on the page colour | Quiet | `samples-v5/build_mix.py` `paper_list(bg, paper, ink, accent, mark, brand, title, items, tilt)` |
| 14 | **Silhouette story** (Littlefold Reels): real silhouette photos, slow push-in, serif lines | Quiet | `slowpan.py` with photo scenes (`oct16-21/reels.py` `lf-reel-1016-doing-better`); fully code-drawn version `content/video/src/lf_silhouette_letters.py` |
| 15 | **Calm text Reel**: code-made paper, blobs or sky background, slow drift, static text | Quiet | `slowpan.py` + `slowpan_bg.py` generators `paper`, `blobs`, `sky`, `forest` |
| 16 | **Reel cover** (dedicated, never a raw frame) | n/a | `oct16-21/reels_lib.py` `render_cover()` (2×, safe-zone and hook-size QA); older `content/video/src/covers_v3.py` |

**"Put a finger down" rules (style 2; corrected Oct 15 against the format and Dharma's reference post):**
- The cover or title slide and the Reel's frame 0 show **5 fingers** (open hand).
- Each statement slide puts one finger down: **4, 3, 2, 1**. So at most 4 statements and 5 slides.
- Fewer statements still start at 5.
- Never start mid-count.
- Cut-outs in `assets/cutouts/`: `glove-pink-5.png` … `glove-pink-1.png`, all from the same Canva AI glove set (credit "Made with AI"). 5 and 4 were matted Oct 15 with `samples-v5/isnet_matte.py` (ISNet + guided-filter edge + despill; wrist trimmed at the cuff hem); 3, 2 and 1 use `samples-v5/matte.py`. Recolour with `build_final.tint_glove()`, and line the counts up with `oct16-21/restyle.py glove_place()` so the hand doesn't jump between steps.

**Retired, never use:**
- the folded-letter look (`samples-v5/build_original.py` `fold_layer()`);
- **plain handwritten lists** (text straight on the background with no note card). Lists are always sticky-note lists.

**Grid check:** run `python3 grid_preview.py newest.png … --theme <page> --out grid.png` before scheduling. It shows the phone 3:4 crop and flags look-alike neighbours.

---

## 3. Rotation rules
- **At least 6 different styles in any 9 consecutive tiles** on a page. Reel covers count as tiles: they sit in the grid.
- **Loud and quiet alternate.** Never put the same style twice in a row, and never three loud or three quiet tiles in a row.
- **Cadence (from Oct 16, Dharma: "be more aggressive, but strategic"):** each page, each day:
  - **2 Reels** (morning ~8:00 and evening 19:00). Reels are the reach engine: they reach non-followers.
  - **1 feed post** (carousel or single, in the rotation) at the page's usual midday slot. A **second feed post** is allowed when it is a quick single tile (a One Word, sticky note or meme) at least 6 hours apart.
  - **3–5 Stories** spread from morning to night: a teaser of today's post, a "new post" share, a poll-style question card, a behind-the-scenes or quote card, a link reminder. Stories keep followers warm; they don't sit in the grid, so the rotation rule doesn't apply to them.
  - Autopost ceilings (tested in `tests/test_autopost.py`): 2 feed, 2 Reels, 5 Stories per page per Toronto day.
  - The Performance desk compares reach per post before and after the ramp and can recommend dialling it back if reach per post drops for 7 days.
- **Reels rotate four styles:** one-word slow-pan photo, kinetic big text, calm text, and silhouette (Littlefold). In one day, no two pages use the same Reel style if there are four to pick from. One page repeating a style on a given day is allowed when it is unavoidable.
- **Each series runs about once a week per page.** Series covers share one layout so the grid looks planned.
- **Glove posts:** at most 1 in 9 tiles per page. The royal-green or butter Fully Funded colourway counts as that one.

## 4. Hooks
- **Cover hooks are at least 120 px (at 1080 wide) and 8 words or fewer.** The exception is a tile that is intentionally quiet (awards, follow-the-line, swipe-to-reveal, panorama, sticky-note list), where the template's own size is fine.
- **Reel covers:** 1080×1920, hook at least 120 px and 3–8 words. All text sits inside **x 90–990 and y 300–1400**. The cover is a dedicated image (no caption bar, no subtitles); `render_cover()` fails it otherwise.
- **Reel frame 0 is the hook**, readable with the sound off.
- **Payoff + action in "you" language** (PAYOFF-FIRST). Never headline with a study.

## 5. Clean-cutout rule
Every cut-out object (gloves, clocks, piggy, shoe, hand) must be **clean**:
- the background shows through **continuously between fingers and in every gap**, with no backdrop islands or haloes;
- the edge is soft at 1–2 px with no fringe (despill the edge from the object's own colour);
- there is a soft contact shadow (`drop-shadow(0 26px 30px rgba(0,0,0,.22)) drop-shadow(0 6px 8px rgba(0,0,0,.12))` or similar), never a hard outline unless the style calls for a sticker border.

Tools:
- `samples-v5/matte.py` (watershed and guided-filter mattes for photos shot on a similar backdrop);
- `samples-v5/lib.py` `_object_mask()` (objects on white);
- `halftone_cutout()` (sticker style).

Check every cut-out at 100% zoom before use.

## 6. Photo-reuse rule
- **One photo = one post.** Never reuse a photo on two posts within 30 days, or across pages at any time.
- A/B colourways of one post count as one post: publish only one of them.
- One Reel's own cover may reuse that Reel's photo, because it is the same post.
- Log every use in the set's `IMAGE-USE.md` (for example `content/design/samples-v5/IMAGE-USE.md`) and check it before building.
- **AI-generated images:** list them in `AI-IMAGES.md` and add "Made with AI" (for example "Photo made with AI.") to the caption.
- No stock photos and no real people's likeness.

Photo use, Oct 16–21:

| Photo | Post |
|---|---|
| street | `ff-reel-1017-raise-half` |
| silhouette1 + sil-lift + shoulders | `lf-reel-1016-doing-better` |
| forest | `lh-reel-1016-quiet` |
| clouds | `hb-reel-1017-offline` |
| wheat | `lf-reel-1018-breathe` |
| couple | `ff-1019-rich-habits-01` |
| clock | `lh-1017-one-word-later` |
| family (B/W) | `ff-reel-1019-late-start` (Reel + its own cover) |

Still unused: father, piggy (photo), halftone sheets 1 and 2. (family: used Oct 19 by B2.)

## 7. The 2× render rule
Everything is rendered at **2× and downsampled with Lanczos**:
- Chromium `device_scale_factor=2`, then `PIL.Image.resize(size, Image.LANCZOS)`.
- `render.py` and `samples-v5/lib.py` `render_many()` already do this for slides.
- `oct16-21/reels_lib.py` does it for Reel text layers (`text_png_2x`, which replaces `slowpan.text_png`), kinetic frames (`render_vlab_2x`) and covers (`render_cover`).
- Never ship a 1× browser screenshot, and never upscale a photo by more than about 10%.
- Feed JPEGs are 1080×1350 at quality 92 with no chroma subsampling.
- Reels:
  - 1080×1920 at 30 fps, H.264 + AAC;
  - 12–18 s;
  - music from the library in §10 (music2 `warm` is retired), at about −14 LUFS;
  - under 19 MB.

## 8. Canva images
The full-resolution fetch pipeline is in **`docs/canva-fetch.md`**:
1. generate the image (one job at a time);
2. place it on a page at its native size in the scratch design;
3. export it as a pro PNG;
4. run `canva_fetch.sh` through the GitHub `fetch-asset.yml` workflow;
5. the file lands in `assets/inbox/`.

Notes:
- The account's AI credit quota ran out on Oct 15 (`quota_exceeded`). Build from the photo library first, and use Canva only when a fresh photo is essential.
- Every Canva AI image gets an AI-IMAGES.md entry and "Made with AI" in the caption.

## 9. Where the engine lives
The full engine, with every sample build script and the cutouts, is packed at `studio/steadfold-studio.tgz`. See `studio/README.md` for setup and the self-test. Fonts are in `assets/fonts/`.

## 10. Music (Oct 16, 2026: music2 retired)
**Rule:** Social studio and Short-form studio score every Reel, Short and TikTok from the picked tracks in **`tools/music-picks.json`** (files in `media/music/library/v3/`). Never `music2.py` "warm": Dharma found it unpleasant and it screeched at high volume.
- **Brief:** build curiosity and pull people to keep watching (gentle forward pulse, rising motif, light "what's next"). Suspense only for a reveal, and then only via a stinger.
  - Fully Funded: confident, optimistic, curious lo-fi/pop. Locked Hour: focused, rhythmic, slight build. Hourback: playful, light, a "ta-da" lift. Littlefold: soft, tender, cosy, never sleepy.
- **Source:** ElevenLabs Eleven Music via `.github/workflows/music.yml` (key stays in the `ELEVENLABS_API_KEY` secret). Starter plan: online commercial use, no attribution, 30 min of downloads a month, no streaming-platform (Spotify etc.) release. Fallback: `media/music/library/v2/` (FluidSynth real-instrument beds, MIT soundfont). Free libraries: Pixabay only without the Content ID shield icon, keep its licence certificate; not the YouTube Audio Library off YouTube.
- **Stingers** (`st-1` soft rise, `st-2` ta-da, `st-3` wait-for-it): under 6 s, only at a reveal.
- **Mix:** bed at −14 LUFS, true peak ≤ −1.5 dBTP, low-passed at 9.5 kHz, −3.5 dB at 2.8 kHz to leave room for a voice. With voiceover, put it in `media/reels/<id>-vo.wav`; `tools/rescore.py` keeps it on top at −16 LUFS and ducks the music under it.
- **QA:** `python3 tools/music_check.py <file or folder>` must PASS (no clipping, no harsh highs, a hook in the first second, a click-free loop).
- **Re-score queued Reels after a new pick:** edit `tools/music-picks.json`, then run `python3 tools/rescore.py --apply` and commit `media/`. Reels cut to their own beat go in the `keep` list. The old audio is kept in `media/reels/_orig-audio/`.
- **Platform sounds:** Meta's Instagram Audio API (`audio_id` on Reel create, Facebook Login only) may let Autopost attach licensed library sounds. It's untested here: try it before you spend money. On TikTok, Business accounts use the free Commercial Music Library.

## 11. Motion: no slideshows (Dharma, Oct 16 2026, 12:42 am)
"We should do those amazing transitional videos, not just some slideshow, PPT presentation thing." Every Reel is now **edited**, not a
set of slides that fade. The tool is the motion kit in **`studio/motion/`** (README there). It renders HTML/CSS/JS frame by frame with
Playwright at 2×, adds real sub-frame motion blur, and cuts on the page's music tempo.

**The rule (every Reel, every page):**
- **Hook in frame 0.** The hook line is fully readable at 0.00 s, and something moves within 0.3 s (a sticker pops, an object lands).
- **A new visual beat every 0.6–1.2 s.** Scene lengths are counted in beats of the page's track (`media/music/library/*-inst-01.mp3`):
  LF 92, FF 95, LH 100, HB 108 bpm, so 1–2 beats per scene. A scene can hold longer only if something new happens inside it
  (a word lands, a tick pops, a number rolls).
- **A transition on every cut,** never a plain fade: whip pans, zoom punch-ins, iris/blob/slit/stripe wipes, card slams, parallax push,
  spin, light-leak flash, glitch, pixelate (Hourback), or a hard cut with a frame shake on impact. Mix at least 6 kinds per Reel.
- **Kinetic type:** big words, one at a time (`words()`), readable with the sound off. Body text is never the main beat.
- **Objects move:** stickers and emoji pop, cards fly in and land, rings and hand-drawn circles draw themselves, numbers roll, timers tick.
  Every scene has a camera move (push, pull, drift, rise, tilt), and the background layer moves less than the content (parallax).
- **Loop:** end on the hook layout (`r.loop()`), so the last frame flows into frame 0.
- **Story first:** open on a moment a stranger recognises ("that's me"), then the fix. A tutorial is the middle, never the hook.
- Keep everything else: brand palettes and fonts (section 1), text inside x 90–990 / y 300–1400, 12–20 s, H.264/AAC 1080×1920,
  under 19 MB, soft instrument bed faded out at the end, the content rules (no fake numbers, finance as education, official parenting sources,
  no real children).

**QA before a Reel ships:** the kit writes `<id>-qa.jpg` (frames at 0 s, every second and across every cut). Look at it, then score it as
a bored stranger at 8 am (stop? watch to the end? send?). Anything short of a strong yes gets re-edited.
This replaces the "calm text" and "kinetic big text" slide timing in section 2 (styles 5 and 15) and the 4-scene Reel timing in
section 7: those styles keep their look, but are cut with the kit.

---

## 12. Bold = the approved editorial look (restored Oct 17, 7:45 am)
**Bold = the approved editorial look (serif + pills + halftone object + handwritten line + stamp); never bare flat cards.**

**Why:** the overnight "bold one-idea" build turned FF and HB into bare colour fields with plain sans text and an emoji.
Dharma, Oct 17 7:39 am: "so plain and bad… why are we going backwards". He re-sent the references we had already agreed on
(yoursocialteam: "These visual trends are going viral right now", "These carousel trends…", "I have nothing to post") and
`docs/grids-FINAL.png`. That look is the standard. Plain flat cards are not a style.

**Every cover, slide 1, Reel frame 0 and Story tile has all five:**
1. **A huge editorial display serif** in a deep ink colour, tight leading, 4-6 words, readable at 200 px wide in one second.
   FF Fraunces (opsz 60, 700) in #141A55; HB DM Serif Display in #2A1D47; LH Instrument Serif in #1B1717; LF Fraunces soft in #3A1F3D.
2. **Rounded highlighter pills** behind the key words, in the page's two soft brand colours, drawn on a layer UNDER the words
   (tight leading must never let a pill cover the line above).
3. **A halftone black-and-white cut-out object or hand interacting with the type**: pointing at it, an OK sign, holding it.
   Signature objects: FF piggy bank, glove, coins, jar, pointing hand, OK hand; HB pointing hand, phone, chat bubbles;
   LH alarm clock, hourglass, megaphone; LF baby shoe, paw, blocks. Cut-outs live in `studio/motion/assets/ht-*.png`
   (make new ones with `studio/editorial/cutout.py`: clean edge, white sticker rim, dot screen, no fringe).
4. **A handwritten save-line** in the accent colour (Caveat Brush), e.g. "save this if your money disappears by the 20th".
5. **The round brand stamp** in a corner (`edkit.stamp`).

On **a soft single-colour field with subtle paper texture** from the page's palette: FF soft cobalt / cream / soft coral;
HB periwinkle / peach / cream; LH butter / pink / cream; LF Sherbet (cream / pink / butter / peach). No dark or saturated full fields.

**Vary the grid.** Rotate the layouts: pills + object, sticky-note list, mosaic photo wall ("I have nothing to post"),
follow-the-line, glove. Never the same layout twice in a row on one page.

**Kept from the pivot (content rules, still in force):**
- One idea per post; the hook is readable at 200 px; detail goes in the caption.
- Feed: 1-3 slides. Reels: hook at frame 0, payoff on the track's `drop_s`, readable pacing (0.4 s/word + 0.6 s), motion and
  transitions from `studio/pivot/TRANSITIONS.md`. The type, pills, objects and stamp are the editorial ones.
- Captions: 3 lines, then the hashtags.
- FF money maths from `studio/pivot/ff_math.py` (`FIG`), headline rate 10% a year, never above. Posts that show returns end the
  caption with **Not guaranteed. Returns vary.**, in the caption only, never on a tile.
- Never the word "example" (12b).
- Any benefit, grant or credit post ends with a clear 'Who qualifies' line or slide (thresholds, ages, how to check), in plain words.
  (Dharma, Oct 17, after the Canada Learning Bond post left readers unsure whether they qualify.)

**How to build it:**
- Feed tiles and Stories: `studio/editorial/specs.py` + `python3 studio/editorial/covers.py feed|story <ids>`
  (2x Chromium render, Lanczos, JPEG q92, writes `media/<id>/` or `media/stories/`).
- Reels: `studio/pivot/hits.py` (FF) and `studio/pivot/reels.py` (HB, LF), whose look now comes from `studio/editorial/edkit.py`
  through `studio/pivot/boldkit.py`: hook scene = the cover composition; every text beat gets the serif, pills and the stamp.
  Save-lines per Reel: `boldkit.SAVES`.
- **QA:** compare each cover side by side with the reference images at 200 px. If it doesn't feel like the same league, redo it.

### 12b. NEVER the word "example" (Dharma, Oct 17)
Never use **"example"**, **"e.g."**, **"for illustration"** or **"hypothetical"** anywhere on any page: on-screen text, captions,
first comments, alt text, Stories, kickers or labels. State the maths directly. Where honesty needs a note that a scenario isn't
real (Hourback AI runs, made-up statements), write **"Made up for this post."** Before you push, scan the queue:
`grep -niE "example|e\.g\.|for illustration|hypothetical" schedule/posts.json` must return nothing for queued posts, and OCR every
new image or Reel frame (`tesseract <img> - --psm 11`) for the same words.

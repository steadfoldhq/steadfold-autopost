# Reference transitions, measured to the frame (Oct 17, 2026)

Source: the 7 screen recordings Dharma shared (Oct 13-15). They're 60 fps screen captures of 30 fps Reels,
so one source frame is 33 ms. Each technique was measured with a per-frame difference signal
(mean absolute pixel change at 144x312) plus frame strips extracted with ffmpeg at every scene change and
±0.3 s around each transition. We copy the **technique only** (timing, motion path, easing, text behaviour).
None of their footage, people, logos, UI or audio is used: every frame is our own type on our own brand colours.

Where it lives: `studio/motion/motion.js` (runtime), `studio/motion/kit.py` (`REF_TD` durations, `flicker()`,
`oneword()`, `Reel.pin()`), `studio/pivot/hits.py` (the aggressive Reel builder that uses all of them).

| # | Technique | Reference (file · time) | Frames @30 | Timing | Easing / motion path | Ours |
|---|---|---|---|---|---|---|
| T1 | **Warm light-leak flash** | 00-05-28 · 4.03-4.23 s, 7.60-7.83 s, 11.47-11.70 s | 7 | 233 ms: 100 ms up, swap at the peak, 133 ms down | up `p^1.6`, down `(1-p)^1.4`; near-white core (97%), amber, then brand edge; bloom centred high (50% 18%) | `tin="leak"` |
| T2 | **Burn-away of the hook card** | 00-05-28 · 1.6-4.0 s | ~66 | burn grows for ~2.2 s, then T1 hides the swap | front starts bottom-centre, noisy edge, ember rim, flame tongues; never eats more than ~55-60% before the flash | `data-a="burn"` (`hook` with `burn=True`), ends in `leak` |
| T3 | **Font flicker** on one word | 00-06-41 · 2.30-2.57 s ("FONTS") | 8 | 1 look per source frame (33 ms), ~270 ms total, lands on the house style | hard swaps, no tween; size and colour change with the face | `kit.flicker(step=1/30)`, `say` with `flick=True` |
| T4 | **On-beat style swap** of a giant title | 00-06-41 · 3.72 / 5.00 / 6.27 s ("BEST FONTS") | 1 per swap | every 1.27 s (on the beat), hard cut | 2-line title fills the width; colour + face change together | `kit.flicker(step=beat)`, scene kind `swap` |
| T5 | **Word captions**: one word or chunk at a time, same spot | 00-06-41 · 0.7-2.3 s; 00-08-33 throughout | 2 per word in | each held 150-330 ms in the reference (we hold ≥0.4 s/word + 0.6 s, house reading rule) | hard swap, 2-frame pop scale 0.9 → 1.0 (67 ms, ease-out) | `kit.oneword()`, scene kind `words` |
| T6 | **Whip-pan with directional blur** | 00-06-41 · 8.37-8.53 s | 5 | 170 ms; text drops out at the start, next caption lands 33-67 ms after | expo in-out; heavy horizontal motion blur, cut at the blur peak | `tin="whipL"` (`REF_TD` 0.17 s, 12 blur samples) |
| T7 | **Punch-in on the hero number** | 00-08-33 · 3.95-4.12 s | 5 | 170 ms, then holds (no zoom back) | scale 1 → ~1.15 (we use 1.12), anchored on the number, ease-out, zoom blur | `data-a="punch"` in `num` (at 0.72 s) |
| T8 | **Card slam-up** over the last frame | 00-08-33 · 3.27-3.40 s | 4 | 130 ms | slides up from the bottom edge, ease-out cubic, rounded corners settle, vertical blur; old frame stays still underneath | `tin="slamup"` + scene kind `card` |
| T9 | **Hand-drawn circle** on the key figure | 00-08-33 · 6.4-7.2 s ("30 days") | 6 | ~200 ms draw, then hold to the next beat | red marker loop, slight overshoot past the start point | `scribble_circle(..., d=0.2)` in `num` (at 0.86 s) |
| T10 | **Pinned caption** above the transitions | 00-08-33, 22-06-18 (captions keep running through every cut) | — | stays across 2+ scenes | doesn't move with whips, pushes or slams | `Reel.pin(t0, t1, html)`, spec `pin=(from, to, text)` |
| T11 | **Hard cut + zoom-land** | 22-06-18 · 10.38-10.58 s | 6 | 200 ms after the cut | new frame lands from 125% to 100%, ease-out cubic, zoom blur fading | `tin="land"` (the payoff cut on the drop) |
| T12 | **Glide across one board** | 22-06-18 · 11.23-11.43 s | 6 | 200 ms | diagonal pan (camera moves up-left, next spot arrives from down-right), ease in-out, motion blur | `tin="glide"` |
| T13 | **Grow from small** | 22-06-18 · 0.10-0.40 s | 9 | 300 ms | card scales 25% → 100%, ease-out, no overshoot | `data-a="grow"` (`card` with `grow=True`) |
| T14 | **Emphasis size jump** in a caption | 22-06-18 · 0.6-1.4 s ("20 versions") | — | for the key phrase only | key words ~1.45× the caption size | `.big` (`^x^` in `oneword` chunks) |
| T15 | **Seamless loop** | 22-06-18 · 36.0 s = 0.0 s | — | last beat = frame 0 | ends on the clean hook layout so the replay feels continuous | `hits.py` loop scene (burn stripped) |
| T16 | **Carousel push** | 00-16-49 · 4.18-4.35 s | 5 | 170 ms | both frames travel together, ease-out cubic | `tin="swipe"` |
| T17 | **Hard cuts on the beat over one slow camera move** | 16-44-40 · cuts every ~1.2 s (2.83, 5.05, 6.22, 7.47 s…) | 1 | cut = 1 frame | the drift continues straight through each cut | `cam="drift"` + `tin="cut"` |
| T18 | **Typed text** | 16-44-40 · 7.0-9.5 s (search bar) | — | 2-3 characters per frame | linear, no cursor blink | `data-a="type"` (already in the kit) |

Not copied: the app UI chrome, the people, the real-world props (lighter, tossed card), screen-recorded
products and their audio. Stingers are not used; the cut timing comes from our own v4 tracks.

## How a Fully Funded Reel uses them (aggressive pivot)
`hook` (frame 0 readable, sticker pops at 0.12 s; optional T2 burn) → T1/T6/T16/T12 cuts on the 16th-note grid →
`card` via T8 if there's a setup figure → **the drop**: T11 land into `num`, count-up, T7 punch-in at 0.72 s, T9 circle at 0.86 s,
stage shake → T1 leak into the T15 loop. 10-15 s total; `hits.py --plan` refuses anything longer or too wordy for the drop.

## QA
`hits.py` writes `/tmp/pivot-hits/<id>/<id>-qa.jpg`: frames at -130, -67, -33, 0, +33, +67, +130 and +200 ms around every cut,
plus frame 0 and the cover frame. Check: no half-drawn text at the cut, the payoff lands on the drop frame, nothing leaves x 70-1010.

# Steadfold motion kit (no slideshows)

Reels made of beat-timed scenes with a transition on every cut, kinetic word-by-word type and motion blur.
Rendered frame by frame from HTML/CSS/JS with Playwright (Chromium at `/opt/pw-browsers/chromium-*`, never `playwright install`),
then encoded with ffmpeg at 30 fps, 1080×1920, H.264/AAC.

```
studio/motion/
  motion.js          runtime: window.seek(t) puts every element in its state at time t (deterministic)
  kit.py             authoring API (Reel, el, words, emoji, img, chip, ring, scribble_circle, arrow) + renderer + encoder + QA sheet
  reels_1016am.py    the Oct 16 morning Reels, the worked examples
  assets/            brand marks, halftone cut-outs (hourglass, cup, shoe, clock, piggy, pointing hand), FF family photo
```

## Use it
```bash
cd /home/claude/steadfold-autopost
python3 studio/motion/reels_1016am.py hb-reel-1016am-calm-reply --out /tmp/motion-out
# -> /tmp/motion-out/<id>/<id>.mp4  and  <id>-qa.jpg (frames at 0 s, every second and across every cut)
```
A new Reel is a function that builds a `Reel(rid, brand, bpm, css)` and calls `r.scene(beats, html, tin=..., cam=...)` per beat,
then `r.loop()`. Scene lengths are in **musical beats** of the page's track, so every cut lands on the music:
LF 92, FF 95, LH 100, HB 108 bpm (`media/music/library/*-inst-01.mp3`). 1–2 beats per scene = 0.55–1.3 s.

## Transitions (`tin=`)
| name | what it does | from the references |
|---|---|---|
| `whipL` `whipR` `whipU` `whipD` | whip pan with an expo speed ramp and real motion blur | whip/swipe cuts |
| `zoom` | punch-through: the scene rushes into a focus point (`focus=(x,y)`), the next lands from 2.6× | zoom punch-ins on the stat |
| `pull` | the scene shrinks away into a card, the next grows in | zoom-out to the full screen |
| `iris` | two-tone circle wipe from a point (brand colour leads) | shape/mask wipes |
| `blob` | rounded-rect blob wipe (soft, Littlefold) | mask wipes |
| `stripes` | three diagonal highlighter bars sweep the frame | highlighter / colour-block wipes |
| `slit` | the next scene opens from a horizontal slit with accent edges | split-screen opens |
| `spin` | rotate-and-shrink out, rotate-and-grow in | rotation |
| `slam` | the next scene rises like a card while the old one drops back (parallax) | object reveal / card slams |
| `push` | iOS-style parallax push with a shadow | parallax |
| `flash` | warm light-leak bloom hides the swap | the film-burn flash |
| `glitch` | slice offsets + RGB split (post effect) | glitch cut |
| `pixel` | pixelate out and in (post effect; Hourback's reveal card) | pixel reveal |
| `cut` | hard cut on the beat (pair with `shake=`) | impact cuts |

## Motion moves inside a scene (`el(..., a=...)`)
`pop` (overshoot), `stamp` (slams down with rotation), `fly` (object flies in and lands), `drop` (elastic drop), `up/down/left/right`,
`wipe` (write-on), `hl` (highlighter), `strike`, `bar`, `draw` (SVG rings, hand-drawn circles, arrows), `type` (typing),
`count` / `tick` (number roll, `data-mmss` for timers), `words` (kinetic captions, one word at a time), `stack` (notifications pile in).
Loops after the entrance: `float`, `wobble`, `pulse`, `buzz`, `shake`, `spin`. Every scene also has a camera move (`cam=`):
`push`, `pull`, `left`, `right`, `rise`, `tilt`; a `.par` background layer moves less than the content (parallax).
`shake=(t, dur, px)` on a scene shakes the whole frame on an impact.

## Motion blur
Frames inside fast transitions are the average of 8 sub-frames across a 0.8-frame shutter (rendered at 1×, since they are blurred anyway).
Every other frame renders at 2× and is Lanczos-downsampled (brand rule 7).

## Rules (see docs/brand-system-v4.md, "Motion: no slideshows")
- Hook in frame 0: the hook line is fully on screen at t=0 (`a="none"` or a negative `t`), and something moves within 0.3 s.
- A new visual beat every 0.6–1.2 s; a transition on every cut; big kinetic type you can read with the sound off.
- End with `r.loop()` so the last frame flows back into the hook.
- Memory: one renderer at a time (2 CPUs / ~4 GB here). The worker recycles Chromium every ~120 screenshots and retries a crashed frame.
  A 15 s Reel takes about 8–10 minutes.

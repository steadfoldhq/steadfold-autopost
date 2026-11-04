# Social studio, Wed Nov 4 2026: page build brief

You are the maker for ONE Steadfold Instagram page. Repo: /home/claude/steadfold-autopost (on main; do NOT git pull/commit/push, do NOT edit schedule/posts.json, never touch state/, keys/ or tokens). Studio engine already extracted to /home/claude/content (fonts + photos installed). The machine has only 2 CPUs / 7 GB RAM and 3 other makers render at the same time: render with 1 worker, one Reel at a time, and delete frame folders right after each encode (disk is limited). Use ffmpeg with -nostdin. Scratch dir: /tmp/claude-0/nov04-<page>/.

Clocks are EST (-05:00). Use "-05:00" in every publish_at.

**Budget:** do the jobs in the order listed. Write each manifest entry as soon as that piece is clean. Target: everything within ~4 h. If you run short, cut the LAST job rather than ship weak work; say why.

## Read first (they win over this brief)
- CLAUDE.md, docs/north-star.md (Founder lines win; your page's section + "All four live pages"), docs/brand-system-v4.md (addendum + your page's section), the top of docs/metrics.md (TEST-BATCH TABLE + "Today's orders", Wed Nov 4).
- The previous builds you EXTEND (copy into your own new script; don't edit shared kits or older scripts): Reels: studio/editorial/nov03_<page>*.py + studio/editorial/nov03/<page>.json + studio/editorial/nov03/BRIEF-<page>.md. Series tile: studio/editorial/nov03_<page>_feed.py (or nov03_<page>.py) + its entry in studio/editorial/nov03/<page>.json (the Fri Nov 6 episode).
- Recent topics on your page (no repeats from the last ~14 days): insights/latest.json `first_line`, queued items in schedule/posts.json for your account, and the nov01/nov02/nov03 manifests.

## What the data says (Performance desk, Nov 4; apply it)
1. **REPEAT the number in frame 0: it is the HOLD lever.** LF "Babies can drown in 5 cm of water" now 198 reach at 7.06 s / 49%; LH "24 minutes on, 6 off" 111 reach, 5.12 s / 35%, 2 saves; grapes 4 / rice grain / 90 min all held 46-53%. Opens without a number held 25-38%. Keep every Reel standalone (no Part 1/Part 2, no callbacks).
2. **SENDS are the missing expansion signal** (4 clean sends on ~3,400 Reel reach since Nov 1). Today we TEST an on-screen send beat: ONE line in the last ~2 s naming the person to send it to ("Send this to whoever does bath time."), together with the follow line. Only on the Reels named below as the send test; every other Reel stays as is so the test is clean.
3. **Batches come late too** (LH lamp 152 -> 323, HB cue card 14 -> 101 after 13 h). Nothing to change; don't read 5 h numbers as failure.
4. **HB: the batch now comes, the hold doesn't.** Panic-scene opens fail ("Guests in 30 minutes" 9 reach, 1.05 s; cue card 3.65 s). The wedding toast held 5.41 s because the page of AI text was visible by second 1. **Frame 0 shows the real AI output itself** (the note, the list, the email), with the deadline hook on top.
5. **FF: HOLD.** Account-level distribution problem suspected (2-33 reach whatever the topic). No topic or format change; keep Canadian partner/family rules, a felt moment + a number in frame 0, drawn style. No extra volume.
6. Follow lines (last beat, on screen >=1.5 s): LF "Follow for one calm thing a night, from bump to toddler."; LH "Follow for one small sleep or focus trick a day."; FF "Follow for one money rule a day, in plain words."; HB "Follow to learn one real AI trick a day."

## YOUR JOB TODAY (quality over count; cut a piece rather than ship filler, and say why)
1. **D) SEND TEST, quick (do first):** `lf-reel-1106-highchair-5-straps` (Fri Nov 6 19:00; built by studio/editorial/nov03_littlefold.py; media/studio-nov03/littlefold/). Add ONE on-screen send line to the end beat, e.g. "Send this to whoever feeds them lunch." (or better; plain, names the person), shown with the follow line for the last ~2 s. Total must stay <=15.0 s. Everything else identical. Overwrite the same mp4 (cover unchanged). Write the full entry (copied from nov03/littlefold.json, beats updated, `"send_test": true`, `"replaces_existing": true`) into your nov04 manifest. Look at the strip.
2. **A) Sun Nov 8 19:00 Reel** (no trial). Id `lf-reel-1108-<slug>`. Standalone, number in frame 0. No send line (control).
3. **C) Mon Nov 9 17:00 series: `lf-3amclub-07` "3 am Club No. 7"** (promised in Friday's caption). 2 slides, SAME cover layout as No. 6, number on the cover, cover hook <=8 words naming a 3 am moment. Caption last line: next episode lands Wed Nov 11 at 5 pm.
4. **B) Mon Nov 9 19:00 Reel** (no trial). Id `lf-reel-1109-<slug>`. Standalone, number in frame 0, different topic family from A. No send line.

Page-specific direction:
- **LITTLEFOLD:** illustrated physical-rule format (sunny, warm, never gloomy), hook carries a picture-able size/amount/number (<=8 words). Official sources only. New topics only (NOT: grapes/round foods, sausage, nuts, 5 cm water/bath, toothpaste, burp, nails, bath elbow, swaddle, cord, neck check, tummy time, coat/car seat, honey, batteries, medicine mL, vitamin D, sleep position, gums, crying, hot drink, hand on baby, fever, vomiting, contact naps, 3 am play, high chair straps, hot tap 49°C, formula water 70°C). Candidates to verify on the official page using its own number: furniture/TV tip-over (anchor it), blind cords (keep cords out of reach / cleats), magnets, small-object choking size (toilet-roll tube if an official source says it), window opening limits, stair gates top and bottom, pot handles turned in, bottle-fed amounts by age, room temperature 16-20°C for sleep (Lullaby Trust), sun/sunscreen under 6 months, bath seat not a safety device. 3 am Club = a 3 am moment with one calm, official rule (not formula water, fever, vomiting, play, contact naps).

## THE STANDARD (non-negotiable; identical to Oct 28)
- CLARITY: a stranger with zero context understands every piece in one watch. Every on-screen line is something a person would say out loud. No shorthand labels or noun-stacks, no leftover "because…" labels, no unlabelled numbers. The payoff states THE IDEA in plain words by second 3; study numbers go in the caption. Every "Do this" names the actual step/app/place.
- REELS: ≤15.0 s (ffprobe), 3–4 beats: hook (≤6 words on a Reel frame 0; the LF size-hook may run to 8) → plain payoff by second 3 → "Do this" (≤7 words) → follow line (+ "Part 2 tomorrow, 7 pm." where applicable). Understandable without sound. Purposeful motion. H.264 1080×1920 30 fps, AAC, <19 MB, a DEDICATED cover jpg. A small plain-word kicker on the payoff beat is allowed ("try this", "careful", "the catch", "habit tip"). Any hook emoji object from ED.EMOJI_OBJ; never the pointing hand or piggy bank. Music: reuse an EXISTING track for your page from tools/music-library.json at ~−14 LUFS. Never Instagram library music; never generate music.
- FEED (series): 2–3 slides, one idea per slide, same layout as the previous episode, the series number on the cover.
- CAPTIONS carry the value: line 1 = the hook in plain words; WHY; exact steps; THE CATCH; who qualifies (for benefits); "Do this: …"; ONE send line; the page FOLLOW line; 4–5 hashtags. Sources in `first_comment` (name + URL/title + what it says, "checked Nov 4 2026").
- Banned everywhere: "example", "e.g.", "hypothetical", "for illustration" (write "Made up for this post."); pointing hand, piggy bank; real children; fabricated stats/quotes/people/results; Dharma's employer; selling anything; "🇨🇦 Canada edition" labels.
- Page rules: LF official sources only (NHS, CPS/caringforkids, AAP/HealthyChildren, Health Canada/PHAC, CDC, WHO, Lullaby Trust), caption ends "General information only, not medical advice.", warm sunny palette, never gloomy. FF: education only, numbers sourced or labelled maths, ≤10%/yr, "Not guaranteed. Returns vary." in caption only when returns appear, "Education only, not financial advice." LH: real peer-reviewed research, cited exactly. HB: real runs only, privacy tip in caption, "Made up for this post." on inputs, label AI where required.
- Verify every fact with WebSearch/WebFetch against the official source today.
- 3 hook options per piece (different angles), your pick first; all 3 shippable.

## REVIEW YOUR OWN RENDERS (founder QG-1)
After each encode: extract a strip (`ffmpeg -nostdin -i X.mp4 -vf "fps=2,scale=216:-1,tile=10x3" -frames:v 1 strip.jpg`) and the cover, LOOK at them with the Read tool, fix clipping, small text, late payoff, cluttered frame 0, retired props, template leftovers, >15.0 s. Re-render until clean. Delete frames after encode.

## OUTPUT
- Media under media/studio-nov04/<page>/ ; builder script(s) under studio/editorial/nov04_<page>*.py (reproducible).
- Unique ids (check schedule/posts.json, schedule/held-*.json, state/published.json).
- Manifest: /home/claude/steadfold-autopost/studio/editorial/nov04/<page>.json = list of entries, same schema as oct28/<page>.json:
  {"id","account","publish_at","video","cover" (relative to media/) OR "images":[...], "caption","first_comment","alt_text",
   "beats":[EVERY on-screen word in order, incl. small handwritten lines], "hook_options":[3], "duration_s", "style", "send_test": false,
   "part2_of"/"part2_id" where used, "sources":[...], "notes"}
  Write the manifest after A is clean (so A can ship early), then update it as B, C, D finish.
- Final message: short summary (ids, slots, durations, styles, hooks, cuts + why, doubts). No file dumps.

## HOOKS (fresh stranger picker, before render)
Before you render A, B and C: write 3 hook options per piece (your pick first). Then launch ONE fresh subagent (Agent tool) that sees ONLY the options for each piece plus one line on what the page is (no drafts, no reasoning, no sources) and ask: "Which one would stop a stranger scrolling, and which is clearest? Pick one per piece, or say none works and why." Adopt its pick unless it is inaccurate or breaks a rule (say why in notes). Record options + picker verdict in the manifest (`hook_options`, `hook_picker`). If you have no Agent tool, note that and use your own pick.

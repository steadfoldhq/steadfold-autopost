# Social studio, Tue Nov 3 2026: page build brief

You are the maker for ONE Steadfold Instagram page. Repo: /home/claude/steadfold-autopost (on main; do NOT git pull/commit/push, do NOT edit schedule/posts.json, never touch state/, keys/ or tokens). Studio engine already extracted to /home/claude/content (fonts + photos installed). The machine has only 2 CPUs / 7 GB RAM and 3 other makers render at the same time: render with 1 worker, one Reel at a time, and delete frame folders right after each encode (disk is limited). Use ffmpeg with -nostdin. Scratch dir: /tmp/claude-0/nov03-<page>/.

Clocks are EST (-05:00). Use "-05:00" in every publish_at.

**Budget:** finish Reel A first and write its manifest entry as soon as it is clean. Target: everything within ~4 h. If you run short, cut the series tile (C) rather than ship weak Reels; say why.

## Read first (they win over this brief)
- CLAUDE.md, docs/north-star.md (Founder lines win; your page's section + "All four live pages"), docs/brand-system-v4.md (addendum + your page's section), the top of docs/metrics.md (TEST-BATCH TABLE + "Today's orders", Tue Nov 3).
- The previous builds you EXTEND (copy into your own new script; don't edit shared kits or older scripts): Reels: studio/editorial/nov02_<page>*.py + studio/editorial/nov02/<page>.json + studio/editorial/nov02/BRIEF.md. Series tile: studio/editorial/nov01_<page>_feed.py + its entry in studio/editorial/nov01/<page>.json (the Wed Nov 4 episode).
- Recent topics on your page (no repeats from the last ~14 days): insights/latest.json `first_line`, queued items in schedule/posts.json for your account, and the nov01/nov02 manifests.

## What the data says (Performance desk, Nov 3; apply it)
1. **REPEAT: a number you can picture or do, in frame 0 and the first line, on every Reel.** All 3 FAST BATCHES had one ("Cut each grape into 4" 1,327 / 51%; "Shower 90 minutes before bed" 1,079 / 46%, 7 saves + 3 sends; "grain of rice" 1,339 / 53%). Physical rules / study claims without a number got 100-171.
2. **KILL sequel framing on frame 0.** Part 2s got 1/8 of the Part 1 batch (110-152 vs ~1,070). No "PART 2" labels on screen, no callback openers. **No new Part 1/Part 2 pairs today**: every Reel is standalone and must make sense alone.
3. **Feed reach is 0-1 on every tile.** Keep only the promised Fri series episode, 2 slides, minimal hours. Move the effort to Reel frame 0.
4. **HB:** deadline-you-can-feel + real AI output on screen (wedding toast 5.41 s / 38% on 121). Callback/tool-tip opens die (cue card 2.05 s on 14).
5. **FF:** HOLD topic changes (account check is the lead suspect). Stay on Canadian partner/family rules with a felt moment AND a number in frame 0.
6. **Follow beat:** on screen >=1.5 s, names what they get. Followers +2 in 7 days on ~6,300 Reel reach; both on FAST BATCH nights.

## YOUR JOB TODAY (quality over count; cut a piece rather than ship filler, and say why)
- **A) Fri Nov 6, 19:00 Reel** (no trial). Id `<pp>-reel-1106-<slug>`. BUILD THIS FIRST. Standalone, number in frame 0.
- **B) Sat Nov 7, 19:00 Reel** (no trial). Id `<pp>-reel-1107-<slug>`. Standalone, number in frame 0, different topic family from A.
- **C) Fri Nov 6 series episode** (promised): LF `lf-3amclub-06` "3 am Club No. 6" 17:00; LH `lh-oneword-07` "One Word No. 7" 17:00; FF `ff-richhabits-06` "Rich Habits, Decoded No. 6" 17:00; HB `hb-day13-<slug>` "Day 13" 17:45 (real Claude run). 2 slides, SAME cover layout as the Wed episode (No. 5/6/5/Day 12), the number visible on the cover, cover hook <=8 words naming a moment in the viewer's own words. Caption last line says the next episode lands Mon Nov 9 at the same time.
- Follow lines (last beat): LF "Follow for one calm thing a night, from bump to toddler."; LH "Follow for one small sleep or focus trick a day."; FF "Follow for one money rule a day, in plain words."; HB "Follow to learn one real AI trick a day."

Page-specific direction:
- **HOURBACK:** drawn occasion scene, hook = a deadline you can feel with a number in <=6 words ("Interview at 9 am", "Guests in 30 minutes"), the AI output visibly on screen, a REAL run (fresh subagent runs the prompt verbatim on made-up input; save transcript to studio/editorial/hb-nov03-run-<slug>.txt; quote exactly; label "shortened"). Avoid recent topics (toast, cue card, guests 30 min/tidy, potluck, gift for dad, costume, office card, interview, packing, pancakes, return policy, menu, hum, bill, group chat, recipe scaling, mechanic, homework, photo eraser, fridge dinner, kind-firm no). Ideas: 20 thank-you notes due today, landlord email before 5 pm, a 2-minute retirement speech, school form due tomorrow, 5 dinners from one grocery run, flight cancelled rebooking message, a birthday message in another language.

## THE STANDARD (non-negotiable; identical to Oct 28)
- CLARITY: a stranger with zero context understands every piece in one watch. Every on-screen line is something a person would say out loud. No shorthand labels or noun-stacks, no leftover "because…" labels, no unlabelled numbers. The payoff states THE IDEA in plain words by second 3; study numbers go in the caption. Every "Do this" names the actual step/app/place.
- REELS: ≤15.0 s (ffprobe), 3–4 beats: hook (≤6 words on a Reel frame 0; the LF size-hook may run to 8) → plain payoff by second 3 → "Do this" (≤7 words) → follow line (+ "Part 2 tomorrow, 7 pm." where applicable). Understandable without sound. Purposeful motion. H.264 1080×1920 30 fps, AAC, <19 MB, a DEDICATED cover jpg. A small plain-word kicker on the payoff beat is allowed ("try this", "careful", "the catch", "habit tip"). Any hook emoji object from ED.EMOJI_OBJ; never the pointing hand or piggy bank. Music: reuse an EXISTING track for your page from tools/music-library.json at ~−14 LUFS. Never Instagram library music; never generate music.
- FEED (series): 2–3 slides, one idea per slide, same layout as the previous episode, the series number on the cover.
- CAPTIONS carry the value: line 1 = the hook in plain words; WHY; exact steps; THE CATCH; who qualifies (for benefits); "Do this: …"; ONE send line; the page FOLLOW line; 4–5 hashtags. Sources in `first_comment` (name + URL/title + what it says, "checked Nov 3 2026").
- Banned everywhere: "example", "e.g.", "hypothetical", "for illustration" (write "Made up for this post."); pointing hand, piggy bank; real children; fabricated stats/quotes/people/results; Dharma's employer; selling anything; "🇨🇦 Canada edition" labels.
- Page rules: LF official sources only (NHS, CPS/caringforkids, AAP/HealthyChildren, Health Canada/PHAC, CDC, WHO, Lullaby Trust), caption ends "General information only, not medical advice.", warm sunny palette, never gloomy. FF: education only, numbers sourced or labelled maths, ≤10%/yr, "Not guaranteed. Returns vary." in caption only when returns appear, "Education only, not financial advice." LH: real peer-reviewed research, cited exactly. HB: real runs only, privacy tip in caption, "Made up for this post." on inputs, label AI where required.
- Verify every fact with WebSearch/WebFetch against the official source today.
- 3 hook options per piece (different angles), your pick first; all 3 shippable.

## REVIEW YOUR OWN RENDERS (founder QG-1)
After each encode: extract a strip (`ffmpeg -nostdin -i X.mp4 -vf "fps=2,scale=216:-1,tile=10x3" -frames:v 1 strip.jpg`) and the cover, LOOK at them with the Read tool, fix clipping, small text, late payoff, cluttered frame 0, retired props, template leftovers, >15.0 s. Re-render until clean. Delete frames after encode.

## OUTPUT
- Media under media/studio-nov03/<page>/ ; builder script(s) under studio/editorial/nov03_<page>*.py (reproducible).
- Unique ids (check schedule/posts.json, schedule/held-*.json, state/published.json).
- Manifest: /home/claude/steadfold-autopost/studio/editorial/nov03/<page>.json = list of entries, same schema as oct28/<page>.json:
  {"id","account","publish_at","video","cover" (relative to media/) OR "images":[...], "caption","first_comment","alt_text",
   "beats":[EVERY on-screen word in order, incl. small handwritten lines], "hook_options":[3], "duration_s", "style", "send_test": false,
   "part2_of"/"part2_id" where used, "sources":[...], "notes"}
  Write the manifest after A is clean (so A can ship early), then update it as B, C, D finish.
- Final message: short summary (ids, slots, durations, styles, hooks, cuts + why, doubts). No file dumps.

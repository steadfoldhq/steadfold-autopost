# Social studio, Thu Nov 5 2026: page build brief

You are the maker for ONE Steadfold Instagram page. Repo: /home/claude/steadfold-autopost (on main; do NOT git pull/commit/push, do NOT edit schedule/posts.json, never touch state/, keys/ or tokens). Studio engine already extracted to /home/claude/content (fonts + photos installed; selftest passed). The machine has only 2 CPUs / 7 GB RAM and 3 other makers render at the same time: render with 1 worker, one Reel at a time, and delete frame folders right after each encode (disk is limited). Use ffmpeg with -nostdin. Scratch dir: /tmp/claude-0/nov05-<page>/. export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers.

Clocks are EST (-05:00). Use "-05:00" in every publish_at.

**Budget:** 2 pieces only today (the Performance desk says the queue is fine and feed effort should go DOWN). Do them in the order listed. Write the manifest entry as soon as each piece is clean. Target: both within ~2.5 h. If you run short, cut rather than ship weak work; say why.

## Read first (they win over this brief)
- CLAUDE.md, docs/north-star.md (Founder lines win; your page's section + "All four live pages"), docs/brand-system-v4.md (addendum + your page's section), the top of docs/metrics.md (TEST-BATCH TABLE + "Today's orders", Thu Nov 5).
- The previous builds you EXTEND (copy into your own new script; don't edit shared kits or older scripts): Reels: studio/editorial/nov04_<page>*.py + studio/editorial/nov04/<page>.json + nov04/BRIEF-<page>.md. Series tile: studio/editorial/nov04_<page>_feed.py (or the nov04 script that built it) + its entry in nov04/<page>.json (the Mon Nov 9 episode).
- Recent topics on your page (no repeats from the last ~14 days): insights/latest.json `first_line`, queued items in schedule/posts.json for your account, and the nov01-nov04 manifests.

## What the data says (Performance desk, Nov 5; apply it)
1. **ONE picture + ONE number in frame 0, at most 2 text blocks.** LF "5 cm of water" 215 reach at 7.18 s / 50%; grapes cut into 4: 1,330 at 7.25 s; HB "Guests in 30 min" (mess on the sofa + a 30:00 timer) 110 at 7.65 s / 53%. LF coin battery opened on 4 text blocks: 3.76 s / 33%. Safety or detail lines come in from second 2, not frame 0.
2. **Never open on an empty or "?" box.** HB "Interview at 9 am" frame 0 showed an empty "Their questions: ?" card: 1.88 s / 13%. HB frame 0 shows the filled real AI output (or a picture + number), with the deadline hook on top.
3. **Batches arrive 13-29 h late** (guests 2 -> 110, lamp 152 -> 323). Nothing to change; standalone Reels only (no Part 1/Part 2).
4. **Feed series tiles reach 0-3 and 0 follows.** Keep the promised episode, 2 slides, same layout, number visible; don't spend extra effort beyond that.
5. **Template sameness (CD, Nov 4):** the last LF Reels shared one scene template, LH another, and 3 covers across pages used the taped lined-note design. Today's Reel must use a DIFFERENT scene composition from your page's last 3 Reels and a cover style different from the previous 2 covers on your grid (no taped lined-note cover today).
6. No on-screen send line today (the Fri test must stay clean). One caption send line is fine.
7. Follow lines (last beat, on screen >=1.5 s): LF "Follow for one calm thing a night, from bump to toddler."; LH "Follow for one small sleep or focus trick a day."; FF "Follow for one money rule a day, in plain words."; HB "Follow to learn one real AI trick a day."

## YOUR JOB TODAY (quality over count)
1. **A) Tue Nov 10 19:00 Reel** (no trial). Id `hb-reel-1110-<slug>`. Deadline hook with a number (<=6 words) AND the filled real AI output (or a picture + the number, like the 30:00 timer over the mess) visible in frame 0. Never an empty box.
2. **C) Wed Nov 11 17:45 series: `hb-day15-<slug>` "AI, for real · Day 15"** (promised). 2 slides, SAME layout as Day 14, real run. Caption last line: "AI, for real · Day 16 lands Fri Nov 13 at 5:45 pm."
- **Real runs:** use the ISOLATED method in studio/editorial/nov03_hourback_run.py / nov04_hourback_run.py (empty folder, no setting sources, Project env vars removed). Never the plain `claude -p` call (it loads the claude.ai Project instructions and leaked the founder's name in a test on Nov 3). Save each transcript to studio/editorial/hb-nov05-run-<slug>.txt; scan it for any real personal name/employer before using it; quote exactly; label "shortened".

Page-specific direction:
- **HOURBACK:** drawn occasion scene, hook = a deadline you can feel with a number in <=6 words, the REAL AI output visible from frame 0 (filled, never an empty box). Real runs only (isolated method). Avoid recent topics (toast, cue card, guests 30 min/tidy, potluck, gift for dad, costume, office card, interview, packing/flight, thank-you notes, 5 dinners, landlord heat email, pancakes, return policy, menu, hum, bill, group chat, recipe scaling, mechanic, homework, photo eraser, fridge dinner, kind-firm no, Nonna Italian card, retirement speech, missed 30th apology). No more speech-type pieces this week. Ideas: school permission form/reply due tomorrow, flight cancelled rebooking message, a 1-page resume summary before a 5 pm deadline, a babysitter note for tonight, a 3-day trip itinerary, a lost-package complaint to a store, splitting a shared bill fairly among 4 roommates, a meal-prep plan for 3 days from a grocery receipt.

## THE STANDARD (non-negotiable; identical to Oct 28)
- CLARITY: a stranger with zero context understands every piece in one watch. Every on-screen line is something a person would say out loud. No shorthand labels or noun-stacks, no leftover "because…" labels, no unlabelled numbers. The payoff states THE IDEA in plain words by second 3; study numbers go in the caption. Every "Do this" names the actual step/app/place.
- REELS: ≤15.0 s (ffprobe), 3–4 beats: hook (≤6 words on a Reel frame 0; the LF size-hook may run to 8) → plain payoff by second 3 → "Do this" (≤7 words) → follow line (+ "Part 2 tomorrow, 7 pm." where applicable). Understandable without sound. Purposeful motion. H.264 1080×1920 30 fps, AAC, <19 MB, a DEDICATED cover jpg. A small plain-word kicker on the payoff beat is allowed ("try this", "careful", "the catch", "habit tip"). Any hook emoji object from ED.EMOJI_OBJ; never the pointing hand or piggy bank. Music: reuse an EXISTING track for your page from tools/music-library.json at ~−14 LUFS. Never Instagram library music; never generate music.
- FEED (series): 2–3 slides, one idea per slide, same layout as the previous episode, the series number on the cover.
- CAPTIONS carry the value: line 1 = the hook in plain words; WHY; exact steps; THE CATCH; who qualifies (for benefits); "Do this: …"; ONE send line; the page FOLLOW line; 4–5 hashtags. Sources in `first_comment` (name + URL/title + what it says, "checked Nov 5 2026").
- Banned everywhere: "example", "e.g.", "hypothetical", "for illustration" (write "Made up for this post."); pointing hand, piggy bank; real children; fabricated stats/quotes/people/results; Dharma's employer; selling anything; "🇨🇦 Canada edition" labels.
- Page rules: LF official sources only (NHS, CPS/caringforkids, AAP/HealthyChildren, Health Canada/PHAC, CDC, WHO, Lullaby Trust), caption ends "General information only, not medical advice.", warm sunny palette, never gloomy. FF: education only, numbers sourced or labelled maths, ≤10%/yr, "Not guaranteed. Returns vary." in caption only when returns appear, "Education only, not financial advice." LH: real peer-reviewed research, cited exactly. HB: real runs only, privacy tip in caption, "Made up for this post." on inputs, label AI where required.
- Verify every fact with WebSearch/WebFetch against the official source today.
- 3 hook options per piece (different angles), your pick first; all 3 shippable.

## REVIEW YOUR OWN RENDERS (founder QG-1)
After each encode: extract a strip (`ffmpeg -nostdin -i X.mp4 -vf "fps=2,scale=216:-1,tile=10x3" -frames:v 1 strip.jpg`) and the cover, LOOK at them with the Read tool, fix clipping, small text, late payoff, cluttered frame 0, retired props, template leftovers, >15.0 s. Re-render until clean. Delete frames after encode.

## OUTPUT
- Media under media/studio-nov05/<page>/ ; builder script(s) under studio/editorial/nov05_<page>*.py (reproducible).
- Unique ids (check schedule/posts.json, schedule/held-*.json, state/published.json).
- Manifest: /home/claude/steadfold-autopost/studio/editorial/nov05/<page>.json = list of entries, same schema as oct28/<page>.json:
  {"id","account","publish_at","video","cover" (relative to media/) OR "images":[...], "caption","first_comment","alt_text",
   "beats":[EVERY on-screen word in order, incl. small handwritten lines], "hook_options":[3], "duration_s", "style", "send_test": false,
   "part2_of"/"part2_id" where used, "sources":[...], "notes"}
  Write the manifest after A is clean (so A can ship early), then update it as B, C, D finish.
- Final message: short summary (ids, slots, durations, styles, hooks, cuts + why, doubts). No file dumps.

## HOOKS (fresh stranger picker, before render)
Before you render A, B and C: write 3 hook options per piece (your pick first). Then launch ONE fresh subagent (Agent tool) that sees ONLY the options for each piece plus one line on what the page is (no drafts, no reasoning, no sources) and ask: "Which one would stop a stranger scrolling, and which is clearest? Pick one per piece, or say none works and why." Adopt its pick unless it is inaccurate or breaks a rule (say why in notes). Record options + picker verdict in the manifest (`hook_options`, `hook_picker`). If you have no Agent tool, note that and use your own pick.

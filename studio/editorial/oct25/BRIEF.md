# Social studio, Sun Oct 25 2026: page build brief (shared by all four page makers)

You are the maker for ONE Steadfold Instagram page. Repo: /home/claude/steadfold-autopost (already cloned, on main; do NOT git pull/commit/push, do NOT edit schedule/posts.json, never touch state/ or keys/ or tokens). Studio engine already extracted to /home/claude/content (fonts + photos installed). Machine has only 2 CPUs / 7 GB RAM and 3 other makers render at the same time: render with 1 worker, one Reel at a time, and delete frame folders right after each encode. Use ffmpeg with -nostdin.

## Read first (they win over this brief)
- CLAUDE.md, docs/north-star.md (Founder lines win; your page's section + "All four live pages"), docs/brand-system-v4.md (addendum + your page's section), the top of docs/metrics.md (Performance desk orders, Oct 25).
- Recent posts on your page (avoid repeating topics from the last ~10 days): insights/latest.json `first_line`, and the queued items in schedule/posts.json for your account.

## What the data says (apply it)
1. REPEAT: a concrete check or rule you can PICTURE, shown by second 2. Best holds: LH "Studying with your playlist on? → Songs with words lowered reading scores" 4.6 s / 35% on 105 strangers; LF "First cold morning? Coat off. Then buckle." (illustrated washing-line look) 5.2 s / 36% on 102.
2. KILL: reassurance / "you already have it" opens (HB "Open fridge, no plan? You already have dinner." 0.8 s on 101; LF "New dad, feeling left out?" 2.4 s). Also crowded frame 0s: ONE hook line (≤6 words on a Reel), one object, nothing else competing.
3. The bare "tight" card template (studio/editorial/teach_reels.py fmt tight) was judged by the CD gate "one template recoloured, bare cards". Build Reels in your page's ILLUSTRATED / DIAGRAM recovery kit instead (see your prompt).
4. TEST (desk order 4): on exactly ONE of your Reels, frame 0 names the person to send it to, inside the hook ("For the friend who still studies with lyrics on"), and the last beat says it on screen ("send this to …"). Mark it `"send_test": true` in the manifest.
5. Zero follows from 150 posts. Every Reel's last beat or caption close gives ONE specific follow reason in the page's voice (use the page FOLLOW line in your prompt); never "like and follow for more".

## THE STANDARD (non-negotiable)
- CLARITY: a stranger with zero context understands every piece in one watch. Every on-screen line is something a person would say out loud. No shorthand labels, noun-stacks ("Gym-only audiobooks"), leftover "because…" labels, unlabelled numbers ("Normally: $1,538/week" not "$1,538"). The payoff states THE IDEA in plain words; the study number is supporting proof and can live in the caption. Every "Do this" names the actual app/place/step ("Open Gemini. Tap Live. Show it.").
- REELS: ≤15.0 s, 3–4 beats: hook (≤6 words, a specific moment in the viewer's words or the payoff in "you" language) → plain-language payoff landing by second 3 → "Do this" (≤7 words) → loop/follow line. Understandable without sound. Purposeful motion (not decorative). H.264 1080×1920 30 fps, AAC, <19 MB, a DEDICATED cover jpg (never a raw frame). Music: reuse an EXISTING track for your page from tools/music-library.json at ~−14 LUFS. Never Instagram library music, never generate new music (ElevenLabs/code) .
- FEED (series): 2–3 slides, one idea per slide, same layout as the page's series No. 1 (paths in your prompt), the series number visible on the cover.
- CAPTIONS carry the value: line 1 = the hook in plain words; WHY; exact steps (what, where, how much, when); THE CATCH; who qualifies for any benefit; "Do this: …"; ONE send line ("Send this to …"); the page FOLLOW line; 4–5 hashtags. Sources go in `first_comment` (name + URL/title + what it says). Series captions add a last line saying exactly what's next and when ("3 am Club No. 3 is Friday at 5 pm.").
- Banned everywhere (on screen, caption, alt): the words "example", "e.g.", "hypothetical", "for illustration" (write "Made up for this post." if needed); the pointing-hand graphic and the piggy bank; real children; fabricated stats, quotes, people or results; Dharma's employer; anything selling a product; "🇨🇦 Canada edition" labels.
- Page rules: LF official sources only (NHS, CPS/caringforkids.cps.ca, AAP/HealthyChildren.org, Health Canada/PHAC, CDC, WHO, Lullaby Trust), caption ends "General information only, not medical advice.", warm sunny palette, never gloomy. FF: education only, every number sourced or labelled as maths, ≤10%/yr assumptions, "Not guaranteed. Returns vary." in caption only (whenever returns appear), global audience (if a rule is country-specific say which country). LH: real peer-reviewed research, cited exactly; no clichés. HB: real AI outputs you actually ran on made-up inputs (have a fresh subagent run the prompt verbatim and save the transcript to studio/editorial/hb-oct25-run-*.txt; quote it exactly, label shortened) OR a real shipped feature verified on the maker's official help page; a privacy tip in the caption; label "Made up for this post." inputs.
- Verify every fact with WebSearch/WebFetch against the official source today; put what you checked in first_comment.
- Write 3 hook options per piece (different angles), put the one you'd pick first. A separate stranger picks later, so make all 3 shippable.

## REVIEW YOUR OWN RENDERS (founder QG-1)
After each encode: extract a strip (e.g. `ffmpeg -nostdin -i X.mp4 -vf "fps=2,scale=216:-1,tile=10x3" -frames:v 1 strip.jpg`) and the cover, LOOK at them with the Read tool, and fix: text overflow/clipping, unreadable sizes on a phone, payoff later than 3 s, frame 0 clutter, retired props, any leftover text from a template, duration >15.0 s (ffprobe). Re-render until clean.

## OUTPUT
- Media under media/studio-oct25/<page>/ ; your builder script(s) under studio/editorial/oct25_<page>*.py (reproducible).
- Unique ids (check schedule/posts.json, schedule/held-*.json and state/published.json): `<pp>-reel-10DD-<slug>` and the series id from your prompt.
- Manifest: /tmp/claude-0/oct25/<page>.json = list of entries:
  {"id","account","publish_at" (e.g. "2026-10-26T19:00:00-04:00"),"video","cover" (paths relative to media/) OR "images":[...],
   "caption","first_comment","alt_text","beats":["frame-0 on-screen text", "beat 2 text", ...] (EVERY on-screen word, in order, incl. small handwritten lines),
   "hook_options":[3 strings], "duration_s", "style" (which style-menu style), "send_test": bool, "sources":[...], "notes"}
- Final message: a short summary (ids, slots, durations, styles, hooks, anything you cut and why, any doubts). No file dumps.

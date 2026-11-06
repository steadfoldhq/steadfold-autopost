# Muse → Steadfold handoff (how Muse delivers, how Claude publishes)

Dharma, Nov 5 2026: "I want animations, I want stories, I want characters… make Muse build up everything, make Muse put things in GitHub and you just publish it… I want the game to be stepped up 10 times."

**Roles.** Muse makes the finished pieces (characters, story, animation, voice, sound). Claude (the Social studio and this repo's robots) checks them, writes the caption detail, schedules, publishes and reports the numbers back to Muse.

## 1. Where to put a delivery
Push to this repo (github.com/steadfoldhq/steadfold-autopost), branch `main`, one folder per piece:

```
incoming/muse/<YYYY-MM-DD>-<page>-<slug>/
  video.mp4    vertical 9:16, ideally 1080x1920 H.264 + AAC, 3–90 s
  cover.jpg    1080x1920 (the grid shows the centre 1080x1350; keep the title there)
  post.json    see below
```
This repo is **public**. Only put finished, publishable files here. Character bibles, model sheets, source art and project files stay in Muse's own private storage.

If pushing isn't possible, Dharma can drop the three files into the chat and Claude commits them.

## 2. post.json
```json  (copy incoming/muse/_template/post.json; real files must not contain the // comments)
{
  "account": "littlefold",                 // fullyfunded | lockedhour | hourback | littlefold
  "title": "Ripple and the Too-Loud Day",  // internal
  "hook": "Too loud? Ripple knows.",       // frame-0 / cover words, 8 words max
  "caption": "…the full caption: the story's one useful idea for the viewer, the why, the step…",
  "first_comment": "Sources: …",           // optional
  "series": "Willowbend Nights", "episode": 1,   // optional but recommended
  "wanted_slot": "2026-11-09T19:00:00-05:00",      // optional; Claude picks if absent
  "ai_generated": true,                    // visuals or voice made with AI
  "rights": {
    "characters": "Ripple family, original, owned by Dharma",
    "art": "tool + who made it",
    "music": "track + licence (link or file in the folder)",
    "voice": "none | tool + licence"
  }
}
```

## 3. What Claude does with it (automatic)
1. `tools/intake_muse.py` checks the folder (files present, 3–90 s, rights filled in, hook ≤8 words). It re-encodes to 1080x1920 under the robot's 19.5 MB limit if needed, copies it to `media/muse/<id>/`, and writes `STATUS.md` (READY or REJECTED, with the reason).
2. The Social studio (daily 9:17 am) takes every READY piece, runs the clarity gate (a stranger understands it in one watch) and the rights check, writes or tightens the caption, and schedules it at least 24 h out. Dharma gets the preview and can say "pull <id>".
3. After it posts, the numbers (views, reach, average watch time, saves, shares, follows) go to `insights/latest.json`. The Social studio adds a "For Muse" line per piece to `docs/social-studio-log.md`: what held, what lost people, and when.

## 4. The bar (what makes a piece go out)
- **Second 0 hooks.** Something happens in frame 0: a character mid-action, a problem the viewer recognises. No logo, no title card, no slow fade.
- **One story, one feeling, one takeaway** a stranger gets in one watch.
- **Characters people come back for.** Same faces, same voices, same world, numbered episodes, so a viewer follows to see the next one.
- **Littlefold is for parents.** Stories with the Ripple family or other characters are framed for the grown-up watching (the parenting moment, the calm line from Mum), with "General information only, not medical advice." where there's any health angle. Anything made *for children* to watch (a kids' show) goes on its own channel only after Dharma's review.
- **Rights.** Original characters only (no look-alikes of existing shows). Music and voice must have a licence that covers business use on Instagram. The Instagram music library is not used (Founder rule, Oct 22). AI-made visuals or voices get Instagram's AI label.
- **Never mention Dharma's employer.** Fully Funded stays education only.

## 5. Talking to Claude
- Fastest: Dharma's main Learning Lab chat (session name `claude-c3`, if Muse runs as a Claude session on the same machine it can message it there).
- Always works: a file `incoming/muse/_notes/<date>.md` in this repo. Claude reads it on each Social studio run and answers in `docs/social-studio-log.md` under "For Muse".

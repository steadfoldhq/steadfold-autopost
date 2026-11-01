#!/usr/bin/env python3
"""Writes studio/editorial/nov01/hourback.json (Hourback, Social studio Nov 1 2026). Entries are added as each piece is clean.
    python3 studio/editorial/nov01_hourback_manifest.py
"""
import json
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
FOLLOW = "Follow to learn one real AI trick a day."
TAGS_TOAST = "#ai #wedding #chatgpt #claude #learnai"

A = dict(
    id="hb-reel-1101-wedding-toast", account="hourback", publish_at="2026-11-01T19:00:00-05:00",
    video="studio-nov01/hourback/hb-reel-1101-wedding-toast.mp4",
    cover="studio-nov01/hourback/hb-reel-1101-wedding-toast-cover.jpg",
    caption=(
        "Best friend's wedding and no toast yet? Give AI 3 true stories about your friend and ask for a toast you can say in 1 minute.\n\n"
        "WHY IT WORKS: the hard part of a toast is shape, not memories. You already have the stories. AI is good at putting them "
        "in order (hello, a story, why they fit, raise your glass) and finding the joke that ties them together.\n\n"
        "THE REAL TEST: we made up a couple, Maya and Theo, and asked Claude (Anthropic) on Nov 1, 2026: \"I'm giving a toast at my "
        "best friend's wedding tonight and I haven't written anything. Her name is Maya, his name is Theo. Three things: we met in a "
        "college dorm when she set off the fire alarm making toast, she drove six hours to help me move, and Theo is the only person "
        "who can beat her at Scrabble. Write me a toast I can say in about one minute. Warm, a little funny.\"\n"
        "It turned the fire alarm into the opening joke, word for word: \"…Maya had set off the fire alarm. Making toast. So it feels "
        "right that I'm the one up here making one tonight.\"\n"
        "And it added a delivery tip, word for word: \"Pause after \"Making toast.\" The laugh lands there.\"\n\n"
        "HOW (5 minutes):\n"
        "1. Open ChatGPT, Claude or Gemini.\n"
        "2. Type who it's for and 3 true things: how you met, one time they showed up for you, one thing about their partner.\n"
        "3. Ask: \"Write me a toast I can say in about one minute. Warm, a little funny.\"\n"
        "4. Read it out loud once with a timer, and change any line that doesn't sound like you.\n\n"
        "THE CATCH: AI only knows the 3 stories you give it, so it can add small details that aren't true (ours added \"2 a.m.\" "
        "and \"pajamas\"). Cut anything that didn't happen before you say it.\n\n"
        "PRIVACY TIP: first names and the stories are enough. Leave out last names, the venue and anything the couple wouldn't "
        "want typed into an app.\n\n"
        "Names and stories made up for this post.\n\n"
        "Do this: Give AI 3 stories. Ask for a 1-minute toast.\n\n"
        "Send this to whoever's giving a toast this year.\n\n"
        f"{FOLLOW}\n\n"
        "Part 2 is tomorrow (Mon) at 7 pm: how to turn the toast into a 5-line cue card so you don't have to memorize it.\n\n"
        + TAGS_TOAST),
    first_comment=(
        "How we made this: one real run in Claude (Anthropic), model claude-opus-5-5, in a fresh session (Claude Code CLI print "
        "mode, no tools, no earlier chat), Nov 1 2026 14:26 UTC. Maya, Theo and the three stories are made up for this post. The "
        "two lines on the card are from the middle of the reply, word for word (shortened, marked …); the yellow note is Claude's "
        "first delivery tip, word for word. The full toast and tips are in our public repo steadfold-autopost: "
        "studio/editorial/hb-nov01-run-toast.txt. Results vary between apps and runs. Fact check (Nov 1 2026): the only claims in "
        "this post are the run itself (prompt and reply), checked against the saved transcript; no outside statistic or feature "
        "claim is made."),
    alt_text=(
        "Illustrated Hourback Reel in periwinkle and cream: an evening wedding reception with string lights, a microphone stand, "
        "and a tent card that says 'Toasts at 8 pm'. A blank index card titled 'My toast:' with a dashed empty "
        "space and a question mark. Words: 'Best friend's wedding. No toast yet.' Then 'Give AI 3 true stories about your friend. It writes you a "
        "1-minute toast.' Three yellow notes, 'stories we made up for this post: she set off the fire alarm making toast; she drove 6 "
        "hours to help me move; her fiancé Theo beats her at Scrabble', fly into the card, and two of Claude's real lines appear in large serif type: "
        "'…Maya had set off the fire alarm. Making toast.' Then 'it "
        "even coaches you. It tells you where to pause.' with a note: 'its tip, word for word: Pause after \"Making toast.\" The "
        "laugh lands there.' and a pause mark is drawn after 'Making toast.' Then 'Do this: Give AI 3 stories. Ask for a 1-minute "
        "toast. In ChatGPT, Claude or Gemini. Part 2 tomorrow, 7 pm: the cue card.' The string lights glow. Ends: 'Follow to learn one "
        "real AI trick a day.' Names and stories made up for this post."),
    beats=[
        "[0.0 s] Best friend's wedding. No toast yet. | (on the card) My toast: · ? | (tent card) Toasts at 8 pm | (chip) Claude's real lines, shortened · names and stories made up for this post | (stamp) HOURBACK · YOUR EVENINGS BACK",
        "[2.2 s] Give AI 3 true stories about your friend. | It writes you a 1-minute toast. | (label, 50 px) stories we made up for this post: | (notes, 46 px) she set off the fire alarm making toast · she drove 6 hours to help me move · her fiancé Theo beats her at Scrabble",
        "[3.95-4.55 s, then held to the end] (card, 72 px serif) …Maya had set off the fire alarm. / Making toast.",
        "[7.4 s] it even coaches you | It tells you where to pause. | (note, 56 px) its tip, word for word: Pause after “Making toast.” The laugh lands there. | (pause mark drawn after 'Making toast.')",
        "[10.6 s] Do this: | Give AI 3 stories. Ask for a 1-minute toast. | In ChatGPT, Claude or Gemini. | Part 2 tomorrow, 7 pm: the cue card.",
        "[11.2 s to end, 3.2 s] Follow to learn one real AI trick a day.",
    ],
    hook_options=["Best friend's wedding. No toast yet.", "Toast tonight? Nothing written.", "Speech at 8. Still blank?"],
    duration_s=14.4,
    style=("Body: drawn occasion scene (desk order 5: deadline you can feel, 4-word hook on frame 0), new composition: evening "
           "reception with string lights, mic stand, index card and a 'Toasts at 8 pm' tent card. Dedicated cover: sticky-note "
           "list (style 13, QUIET): lined note, red margin, tape, Caveat Brush title, Caveat items with ticks, drawn clinking "
           "flutes, stamp. Grid: after Sat 7 pm costume (kinetic big text, loud), before Mon 5:45 pm Day 11 (series Look B, loud)."),
    send_test=False,
    part2_id="hb-reel-1102-toast-cue-card",
    sources=["studio/editorial/hb-nov01-run-toast.txt (fresh verbatim Claude run via claude -p, Nov 1 2026 14:26:02 UTC)"],
    notes=("No trial flag. Desk grade: >=5 s on >=40. Payoff in words at 2.2 s; the 2 real joke lines are fully on the card from 4.55 s and held to the end (about 10 s). Part 2 "
           "test: frame 'Part 2 tomorrow, 7 pm: the cue card.' + follow pill on the last beat (3.2 s); B (hb-reel-1102-toast-cue-card) "
           "is that Part 2 and stands alone. Music hb-x-future-easy (tools/music-library.json), -14.0 LUFS integrated; SFX paper "
           "slap + sticker pops from the library. 14.4 s, 1080x1920 30 fps H.264 + AAC, 1.6 MB. Builder: studio/editorial/"
           "nov01_hourback.py toast (+ nov01_hourback_covers.py, run: nov01_hourback_run.py toast). Real-person check: Maya, Theo "
           "are made up. Caption names the run's two invented details ('2 a.m.', 'pajamas') as THE CATCH. Gate rev (Nov 1): picker's hook; "
           "'real stories about them' + notes labelled 'our made-up stories'; toast lines 54 px serif, no hand over text; notes 46 px; "
           "no diagonal flash, faster text fades; chip at y 1515 (nothing important in the bottom 18%). Round 2: 'Give AI 3 true stories "
           "about your friend.'; notes labelled 'stories we made up for this post:'; 'her fiancé Theo'; card cut to the 2 joke lines at 72 px, "
           "held ~10 s; 'Claude's real lines' moved into the chip; text cuts in 0.08 s."),
)

ENTRIES = [A]

if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(REPO / "studio/editorial"))
    extra = []
    try:
        import nov01_hourback_manifest_bcd as M2  # B, C, D appended when clean
        extra = M2.ENTRIES
    except ImportError:
        pass
    out = REPO / "studio/editorial/nov01/hourback.json"
    data = ENTRIES + extra
    for e in data:
        blob = json.dumps(e).lower()
        for w in ("example", "e.g.", "hypothetical", "for illustration"):
            assert w not in blob, (e["id"], w)
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(out, [e["id"] for e in data])

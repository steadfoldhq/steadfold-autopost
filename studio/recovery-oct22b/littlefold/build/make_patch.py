#!/usr/bin/env python3
"""Writes studio/recovery-oct22b/littlefold/patch.json. Captions and first comments are copied verbatim from the
live queue (same facts, sources and message); only media and alt text change. Read-only on schedule/posts.json."""
import json
import re
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
P = json.load(open(REPO / "schedule/posts.json"))
P = P if isinstance(P, list) else P["posts"]
Q = {x["id"]: x for x in P}
M = "recovery-oct22b/littlefold/"

items = [
    dict(id="lf-reel-1025am-crying-peak", action="improve",
         reason="Founder: the burgundy Night Light look 'improved the message but does not fully reflect the preferred emotional direction'. "
                "Rebuilt in the sunlit Washing-line Morning world: dawn pastel sky that warms to morning, sleepy sun that wakes on the "
                "'Do this' beat, a tiny pastel garment pegged onto the line each beat. Same 5 beats, same words, same CPS/AAP chips, "
                "same music (lf-c-sunny-morning-el, cuts on its 120 bpm grid) plus soft peg pops. 14.4 s, loops to frame 0.",
         new=dict(video=M + "lf-reel-1025am-cant-spoil-sun.mp4", cover=M + "lf-reel-1025am-cant-spoil-sun-cover.jpg",
                  alt_text="Illustrated Reel in soft dawn light: a pastel pink and blue sky over sage hills, a little cottage, and a sleepy "
                           "smiling sun rising. Tiny baby clothes are pegged on a washing line, one more each beat. Text: You can't spoil a "
                           "newborn. Pick them up. / Answer their cries, and they cry less. / Hungry? Diaper? Too hot or cold? / Hold close. "
                           "Sway. Shush. Walk. / The sky turns to morning and the sun opens its eyes: Do this: Next cry: pick them up first. "
                           "Source chips: CPS, AAP.")),
    dict(id="lf-1025-follow-crying", action="improve",
         reason="Same 3 slides, words and CPS source, re-drawn warm: slide 1 turns 'the peak' into a soft pink hill to walk over with "
                "the sun on the far side (labels: often 3 to 12 weeks; usually over by 3 to 4 months); slide 2 is the same 3-step list "
                "on a cream card with pastel garment numbers; slide 3 is full morning with the sun awake. No dark/burgundy fields.",
         new=dict(images=[M + f"crying-peak-sun-0{i}.jpg" for i in (1, 2, 3)],
                  alt_text="Littlefold 3-slide carousel, soft pastel illustrations. Slide 1, dawn sky: The crying has a peak. Often somewhere "
                           "around 3 to 12 weeks. Usually over by 3 to 4 months. A pink hill with a little flag at the top labelled the peak: "
                           "often 3 to 12 weeks, and a smiling sun beyond it labelled usually over by 3 to 4 months. Source: CPS, Colic and "
                           "crying. Slide 2: Check first. Then hold close. 1 Check first: hungry, wet diaper, too hot or cold, fever. 2 Hold "
                           "them. You can't spoil a baby by picking them up. 3 Calm it down: dim the lights, shush, sway, or walk them close "
                           "to you. Slide 3, morning hills with the sun waking: Next cry: check first, then hold close. Too much? Put baby in "
                           "their crib, step out and take a moment. It's OK to ask for help. Under 3 months with a fever? Get care right away. "
                           "Handwritten: save this for 3 am.")),
    dict(id="lf-ch-1025-4", action="improve",
         reason="Hand-off frame re-drawn to match the new sunlit 11:30 carousel (shows its new cover). Same words: 'It has a peak.' / "
                "'full breakdown in today's post'.",
         new=dict(image=M + "story-lf-ch-1025-4-sun.jpg")),
    dict(id="lf-reel-1025-step-away", action="improve",
         reason="Rebuilt warm: soft afternoon pastel sky, sun resting low with closed eyes (breathing), garments swaying in a breeze "
                "on 'Step out. Breathe.'; on 'Do this' the sky brightens and the sun opens its eyes. Same 5 beats, words and CPS chip, "
                "'Never shake a baby' kept at full size. Music changed to the warmer allowed library track lf-b-tender-el (ElevenLabs "
                "library, passes music_check), cuts on its 84.7 bpm grid. 14.5 s, loops to frame 0.",
         new=dict(video=M + "lf-reel-1025-step-away-sun.mp4", cover=M + "lf-reel-1025-step-away-sun-cover.jpg",
                  alt_text="Illustrated Reel in soft afternoon light: pastel sky, sage hills, a little cottage and a resting sun with closed "
                           "eyes. Tiny baby clothes sway on a washing line, one more each beat. Text: Still crying? At your limit? It's OK to "
                           "step away. / Crib first. On their back. / Step out. Breathe. Take a moment. / Never shake a baby. Never. / The sky "
                           "brightens and the sun opens its eyes: Do this: Tonight, pick who you'll text. “Can you come?” It's OK to ask for "
                           "help. Source chip: CPS, Colic and crying.")),
]
for it in items:
    q = Q[it["id"]]
    if "video" in it["new"] or "images" in it["new"]:
        it["new"]["caption"] = q["caption"]
        it["new"]["first_comment"] = q["first_comment"]
    # media must exist
    for k in ("video", "cover", "image"):
        if k in it["new"]:
            assert (REPO / "media" / it["new"][k]).exists(), it["new"][k]
    for im in it["new"].get("images", []):
        assert (REPO / "media" / im).exists(), im
    txt = json.dumps(it["new"])
    assert not re.search(r"\b(example|e\.g\.|hypothetical)\b", txt, re.I)
    # reorder so the new block reads like the old patch
    order = ["caption", "first_comment", "alt_text", "images", "image", "video", "cover"]
    it["new"] = {k: it["new"][k] for k in order if k in it["new"]}
out = REPO / "studio/recovery-oct22b/littlefold/patch.json"
json.dump(items, open(out, "w"), indent=1, ensure_ascii=False)
print(out, len(items))

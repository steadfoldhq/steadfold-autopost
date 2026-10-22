#!/usr/bin/env python3
"""Writes studio/recovery-oct22/littlefold/patch.json from the live queue + the decisions below."""
import json
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
posts = {p["id"]: p for p in json.load(open(REPO / "schedule/posts.json"))["posts"]}
R = "recovery-oct22/littlefold/"
DISC = "General information only, not medical advice."
FOLLOW = "Follow for one calm thing a night, from bump to toddler."

CPS_CRY = ("Canadian Paediatric Society, Caring for Kids, 'Colic and crying' (caringforkids.cps.ca): the peak crying period is "
           "'usually sometime around 3 to 12 weeks of age' and 'usually, it is over by the time your baby is 3 to 4 months of age'; "
           "check whether baby needs a diaper change, is hungry, too cold or hot, in pain or has a fever; 'Hold your baby. You cannot "
           "\"spoil\" a baby by picking them up'; dim the lights, gentle shushing, rock or sway, walk with baby held close or in a stroller; "
           "'If you are feeling frustrated, take a deep breath, put your baby in a safe place (like their crib) and take a moment to calm "
           "yourself'; 'It is OK to ask for help'; 'Never shake, smother, hit or throw your baby'; get care right away if baby has a fever "
           "and is less than 3 months old.")
AAP_CRY = ("American Academy of Pediatrics, healthychildren.org, 'Responding to your baby's cries': 'You cannot spoil a young baby with "
           "attention, and if you answer their calls for help, they'll cry less overall'; 'The best way to handle crying is to respond "
           "promptly during their first few months.'")

new = {}

new["lf-1023-resp-catch-up"] = dict(
    action="improve",
    reason="Caption promised 'Tonight at 7: how much you can still get, by your child's age', but that Reel (lf-cheat-1023-resp-catch-up) "
           "was held today, so the line points at nothing. Caption-only fix (rule break: false hand-off); slides, facts and sources unchanged.",
    new=dict(caption=posts["lf-1023-resp-catch-up"]["caption"].replace(
        "Tonight at 7: how much you can still get, by your child's age.\n\n", "").replace(
        "Send this to a parent who never opened one.\n\n", "Send this to a parent who never opened one.\n\n" + FOLLOW + "\n\n")))

new["lf-ch-1023-4"] = dict(
    action="improve",
    reason="Story hand-off carried the pill 'by age: tonight at 7' for the held cheat-sheet Reel. Re-rendered the same hand-off without it.",
    new=dict(image=R + "story-lf-ch-1023-4.jpg"))

new["lf-pan-1024am-newborn-bundle"] = dict(
    action="hold",
    reason="Duplicate: same topic and near-identical caption to lf-1022-newborn-bundle-trail, published today 11:30. Also the 3rd Canada-money "
           "post in 3 days (B19: max 1 a week) and it overlaps tonight's CCB Reel. Publishes Sat 8:00, inside the no-edit window, so hold, don't swap.",
    new={})

new["lf-reel-1022-ccb-at-birth"] = dict(
    action="hold",
    reason="Recommend HOLD (coordinator's call): same-day repeat of the published newborn-bundle post (which already says 'apply for the Canada "
           "child benefits'), B19 Canada-money breach flagged by the Performance desk, piggy-bank clip-art (overused). ~6 h to publish; no time to rebuild.",
    new={})

new["lf-1024-roadmap-bedtime"] = dict(
    action="replace",
    reason="Interactive 'take the route 👉' hook (killed: ≤8 reach, 0 visits), 7 slides (desk: ≤5), bedtime repeat of the Oct 23 8 am "
           "Brush-Book-Bed Reel, and its WHY rests on a single study (Mindell 2015), not an LF official source. Replaced with Small Wins No.2, "
           "a warm send-to-someone tile (v0.5 day mode, v4 series layout).",
    new=dict(
        images=[R + "small-wins-02-showered.jpg"],
        caption=("Small Wins No.2: you showered today.\n\n"
                 "Before noon, even. Nobody claps for this part of the newborn weeks, so we will. A shower, a hot drink, a meal sitting "
                 "down: in the early weeks, they count.\n\n"
                 "Do this: send this to someone who earned one today.\n\n"
                 "Small Wins is our award for the parts nobody sees. What should No.3 be? Tell us below.\n\n"
                 + FOLLOW + "\n\n#newparents #newborn #fourthtrimester #parenthood #smallwins"),
        first_comment="Who are you giving this one to? Nominate a Small Win for No.3 👇 (No health facts in this post, so no sources.)",
        alt_text=("Cream tile with a coral label, SMALL WINS · No.2. Big serif headline: You showered today. A pink award rosette with a "
                  "shower head reads SMALL WIN, Showered. Soft paw prints around it. Below: Before noon, even. Nobody claps for this part, "
                  "so we will. Handwritten: it counts.")))

new["lf-reel-1024-grandma-resp"] = dict(
    action="improve",
    reason="Video kept (≤15 s, legible, problem-moment hook is weaker but not a rule break). First comment cited a popular book "
           "(Medina, Brain Rules for Baby) as a source; LF is official sources only. Removed it; kept NHS Start for Life and Public Health Scotland.",
    new=dict(first_comment=posts["lf-reel-1024-grandma-resp"]["first_comment"].replace(
        " Ideas (not quotes) from John Medina, Brain Rules for Baby.", "")))

new["lf-reel-1025am-crying-peak"] = dict(
    action="improve",
    reason="Rebuilt to the v0.5 Night Light floor. Old: piggy-bank clip-art on a crying post (overused, off-topic), problem-question open, "
           "crying-peak number sourced to a hospital-trust leaflet. New: rule + reassurance open on frame 0 ('You can't spoil a newborn. "
           "Pick them up.'), CPS + AAP only, 14.6 s, 5 beats with 5 different transitions, morning-light 'Do this', loops to frame 0.",
    new=dict(
        video=R + "lf-reel-1025am-cant-spoil.mp4", cover=R + "lf-reel-1025am-cant-spoil-cover.jpg",
        caption=("You can't spoil a newborn. Pick them up.\n\n"
                 "Why it works: the Canadian Paediatric Society says you can't “spoil” a baby by picking them up, and the American "
                 "Academy of Pediatrics says that when you answer their calls for help, they cry less overall.\n\n"
                 "What helps, in order:\n1. Check first: hungry, wet diaper, too hot or cold, fever.\n2. Hold them close.\n"
                 "3. Dim the lights, shush, sway, or walk with them.\n\n"
                 "The catch: under 3 months with a fever? Get care right away.\n\n"
                 "Do this: next cry, pick them up first.\n\n"
                 "Tonight at 7: the plan for when you've tried everything.\n\n"
                 + FOLLOW + "\n\n" + DISC + "\n\n#newborn #newparents #babycrying #canadianparents #fourthtrimester"),
        first_comment="Who told you you'd spoil them? Sources: " + CPS_CRY + " " + AAP_CRY,
        alt_text=("Night Light Reel: a warm circle of lamp light on a deep berry night, with a small lamp. Text: You can't spoil a "
                  "newborn. Pick them up. / Answer their cries, and they cry less. / Hungry? Diaper? Too hot or cold? / Hold close. Sway. "
                  "Shush. Walk. / Morning light fills the frame: Do this: Next cry, pick them up first. Source chips: CPS, AAP.")))

new["lf-ch-1025-4"] = dict(
    action="improve",
    reason="Hand-off frame showed the old follow-the-line cover; the 11:30 post is replaced, so the frame now shows the new cover ('It has a peak.').",
    new=dict(image=R + "story-lf-ch-1025-4.jpg"))

new["lf-1025-follow-crying"] = dict(
    action="replace",
    reason="Follow-the-line 'pick the line 👉' hook (killed format), slide 2 was a filler ('Keep following your line'), and it repeated "
           "the 8 am Reel. Replaced with the v0.5 Night Light tile 'The crying has a peak' as a 3-slide carousel (fact → what helps → "
           "Do this), CPS only, matching the Story chain's hand-off.",
    new=dict(
        images=[R + "crying-peak-01.jpg", R + "crying-peak-02.jpg", R + "crying-peak-03.jpg"],
        caption=("The crying has a peak. It often lands somewhere around 3 to 12 weeks, and it's usually over by 3 to 4 months.\n\n"
                 "Why that helps: a hard week isn't proof you're doing it wrong. It's a stage, and for most babies it eases.\n\n"
                 "What helps, in order (Canadian Paediatric Society):\n1. Check first: hungry, wet diaper, too hot or cold, fever.\n"
                 "2. Hold them. You can't spoil a baby by picking them up.\n3. Dim the lights, shush, sway, or walk them close to you.\n\n"
                 "The catch: under 3 months with a fever? Get care right away. And if it's too much, put baby in their crib, step out "
                 "and take a moment. It's OK to ask for help.\n\n"
                 "Do this: next cry, check first, then hold close and sway.\n\n"
                 "Send this to someone in week 3.\n\n" + FOLLOW + "\n\n" + DISC +
                 "\n\n#newborn #babycrying #newparents #canadianparents #fourthtrimester"),
        first_comment="What week are you in? Sources: " + CPS_CRY,
        alt_text=("Littlefold 3-slide carousel in the Night Light look. Slide 1: a warm lamp-light circle on a deep berry night: The crying "
                  "has a peak. Often somewhere around 3 to 12 weeks. Usually over by 3 to 4 months. Source: CPS, Colic and crying. "
                  "Slide 2: Check first. Then hold close. 1 Check first: hungry, wet diaper, too hot or cold, fever. 2 Hold them. You "
                  "can't spoil a baby by picking them up. 3 Calm it down: dim the lights, shush, sway, or walk them close to you. "
                  "Slide 3, morning light: Do this: Next cry: check first, then hold close. Too much? Put baby in their crib, step out "
                  "and take a moment. It's OK to ask for help. Under 3 months with a fever? Get care right away.")))

new["lf-1025-hold-million-words"] = dict(
    action="replace",
    reason="'Hold the dots and slide' interactive hook (killed format), 7 slides, reading topic already covered (lf-reel-1017am-read), "
           "single-study source (Ohio State) instead of LF official sources. Replaced with the v0.5 'one number' tile: vitamin D 400 IU (CPS).",
    new=dict(
        images=[R + "vitamin-d-400.jpg"],
        caption=("Breastfed babies: 400 IU of vitamin D, every day.\n\n"
                 "Why: the Canadian Paediatric Society recommends a daily vitamin D supplement for breastfed babies, from birth until they "
                 "get enough from their diet.\n\n"
                 "Formula-fed? Vitamin D is already added to infant formula, so most full-term babies on formula don't need drops.\n\n"
                 "The catch: babies in northern communities or with other risk factors may need more. Ask your baby's doctor or nurse.\n\n"
                 "Do this: ask your pharmacist which infant vitamin D drops to buy, and set a daily phone reminder.\n\n"
                 "Save this for your next pharmacy run.\n\n" + FOLLOW + "\n\n" + DISC +
                 "\n\n#newborn #breastfeeding #vitamind #newparents #canadianparents"),
        first_comment=("Drops in the morning or at bedtime at your house? Source: Canadian Paediatric Society, Caring for Kids, 'Vitamin D' "
                       "(caringforkids.cps.ca): 'Babies who are breastfed should get 400 IU (international units) per day', from birth until "
                       "they get enough from their diet; vitamin D is already added to infant formula, so most full-term formula-fed babies "
                       "don't need a supplement; babies in northern communities or with other risk factors need more (800 IU a day, year-round)."),
        alt_text=("Cream tile with a soft butter glow. A peach drop labelled 400 IU. Big serif: Breastfed babies: 400 IU a day. Below: "
                  "Vitamin D drops, every day from birth, until they get enough from food. Formula already has it added. Northern community "
                  "or other risk factors? Ask about a higher dose. Handwritten: set a daily reminder. Source chip: CPS, Vitamin D.")))

new["lf-reel-1025-step-away"] = dict(
    action="improve",
    reason="Rebuilt to the Night Light floor. Old: pointing-hand clip-art (overused), 3.5 s frame showed one word ('Baby') mid-reveal, "
           "sources were a hospital-trust leaflet. New: rule + reassurance open on frame 0 ('It's OK to step away.'), CPS only, 14.8 s, "
           "morning-light 'Do this', loops to frame 0.",
    new=dict(
        video=R + "lf-reel-1025-step-away-nl.mp4", cover=R + "lf-reel-1025-step-away-nl-cover.jpg",
        caption=("It's OK to step away. Still crying, and you're at your limit? That happens to loving parents too.\n\n"
                 "Why it's OK: the Canadian Paediatric Society says that if you're feeling frustrated, take a deep breath, put your baby "
                 "in a safe place like their crib, and take a moment to calm yourself. Taking a break can help, and it's OK to ask for help.\n\n"
                 "The plan:\n1. Crib first: baby on their back.\n2. Step out. Breathe. Take a moment.\n"
                 "3. Text your person: “Can you come?”\n4. Go back when you're calmer.\n\n"
                 "Never shake a baby. Shaking can cause lifelong injury or even death.\n\n"
                 "If baby seems unwell, or is under 3 months with a fever, get care right away.\n\n"
                 "Do this: tonight, pick who you'll text, and tell them they're it.\n\n"
                 "Send this to every new parent. Part 2 of 2.\n\n" + FOLLOW + "\n\n" + DISC +
                 "\n\n#newparents #newborn #babycrying #parentingsupport #canadianparents"),
        first_comment=("Who's your person? Sources: " + CPS_CRY + " Government of Canada, 'Safe sleep for your baby': baby sleeps on their "
                       "back in a crib, cradle or bassinet."),
        alt_text=("Night Light Reel: a warm circle of lamp light on a deep berry night, with a small lamp. Text: Still crying? At your limit? "
                  "It's OK to step away. / Crib first. On their back. / Step out. Breathe. Take a moment. / Never shake a baby. Never. / "
                  "Morning light fills the frame: Do this: Tonight, pick who you'll text. Can you come? It's OK to ask for help. "
                  "Source chip: CPS, Colic and crying.")))

keep_reasons = {
    "lf-ch-1022-1": "Story chain frame 1 (today). Night-city photo is an odd match for 'she fell asleep on me', but no rule break; inside 24 h.",
    "lf-ch-1022-2": "Chat-bubble teaching frame; clear, matches HC safe-sleep guidance.",
    "lf-ch-1022-3": "Rule frame, legible, sourced to Health Canada.",
    "lf-1022-follow-safe-sleep": "Publishes in hours. Follow-the-line hook is a weak format and 6 slides is long, but safe-sleep content is accurate "
                                 "and the page's only save-earner; not a rule break. (Minor: also cites Government of New Brunswick.)",
    "lf-ch-1022-4": "Hand-off to today's post; fine.",
    "lf-reel-1023am-screens-bed": "≤15 s, CPS/AAP sourced, legible frame 0. Problem-moment hook ('Bedtime turned into a battle again?') is the "
                                  "weaker open type and the 3.5 s frame catches a half-revealed line, but no rule break; inside the no-edit window.",
    "lf-ch-1023-1": "Quiz frame; fine.",
    "lf-ch-1023-2": "$7,200 matches canada.ca CESG lifetime max.",
    "lf-ch-1023-3": "Fine.",
    "lf-1023-climb-first-words": "Panorama stairs, warm and useful. Sources are CDC milestones (built with AAP) plus one peer-reviewed study "
                                 "(Romeo 2018), described accurately. 7 slides is long. Inside the no-edit window; keep.",
    "lf-ch-1024-1": "Photo + quote hook; fine.",
    "lf-ch-1024-2": "Fine.",
    "lf-ch-1024-3": "Fine; matches Health Canada.",
    "lf-ch-1024-4": "Fine.",
    "lf-1024-no-honey": "Strong rule open, Health Canada sourced, grandparent script is sendable. 7 slides long but no rule break.",
    "lf-ch-1024-5": "Hand-off; fine.",
    "lf-ch-1025-1": "Quiz frame; fine.",
    "lf-ch-1025-2": "'6 to 8 weeks' (NHS) sits inside CPS's 3-12 weeks, so it stays consistent with the new carousel.",
    "lf-ch-1025-3": "'You can't spoil a newborn' (AAP) now also the 8 am Reel's open: chain and Reel reinforce each other.",
    "lf-3amclub-01": "New series cover (v4 gate passed today): bold editorial, alarm clock (not hand/piggy), sourced, disclaimer and follow reason present.",
}

patch = []
lf = sorted([p for p in posts.values() if p["account"] == "littlefold"], key=lambda p: p["publish_at"])
published = json.load(open(REPO / "state/published.json"))["posts"]
for p in lf:
    if p["id"] in published:
        continue
    if p["id"] in new:
        patch.append(dict(id=p["id"], **new[p["id"]]))
    else:
        patch.append(dict(id=p["id"], action="keep", reason=keep_reasons.get(p["id"], "No rule break."), new={}))

# sanity: referenced media exist; no banned words
for e in patch:
    for k in ("video", "cover", "image"):
        if k in e["new"]:
            assert (REPO / "media" / e["new"][k]).exists(), e["new"][k]
    for f in e["new"].get("images", []):
        assert (REPO / "media" / f).exists(), f
    blob = json.dumps(e["new"]).lower()
    for bad in ("example", "e.g.", "for illustration", "hypothetical"):
        assert bad not in blob, (e["id"], bad)

out = REPO / "studio/recovery-oct22/littlefold/patch.json"
json.dump(patch, open(out, "w"), indent=1, ensure_ascii=False)
from collections import Counter
print(out, Counter(e["action"] for e in patch))

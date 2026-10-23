#!/usr/bin/env python3
"""Oct 23 (Social studio): queue changes for this run. Writes docs/social-recovery/2026-10-23-before.json (every entry it
touches, as it was) first, then edits schedule/posts.json and moves held posts to schedule/held-oct23.json (nothing deleted).

    python3 studio/editorial/queue_oct23.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
NOT_MED = "General information only, not medical advice."
NG = "Not guaranteed. Returns vary."
F_LF = "Follow for one calm thing a night, from bump to toddler."
F_LH = "Follow for one small focus fix a day, each one backed by research."
F_FF = "Follow for one money move a day, in plain words."
F_HB = "Follow to learn what AI can really do, one real test a day."

HOLD = ["ff-1025-hold-cost-of-waiting", "hb-1025-family-calendar", "lh-1025-climb-one-percent", "hb-1025-hold-task-length",
        "hb-ch-1025-1", "hb-ch-1025-2", "hb-ch-1025-3", "hb-ch-1025-4"]
HOLD_WHY = {
    "ff-1025-hold-cost-of-waiting": "clarity gate CONFUSING (cover: 'hold the dots and slide', $212,200 shown before the $300/month at 10% setup); cover built outside this repo's renderers",
    "hb-1025-family-calendar": "clarity gate CONFUSING (cover line 'fluent isn't true. AI clicks, you press pay.' needs the series to make sense; jargon: hallucination, word-piece, human in the loop); 9-slide recap",
    "lh-1025-climb-one-percent": "clarity gate CONFUSING ('It's a handle' metaphor never said plainly; 'vs. baseline', 'Correlational' on the slide); rebuilt elsewhere",
    "hb-1025-hold-task-length": "clarity gate CONFUSING ('2 seconds -> 1 hour' doesn't say human-task length; METR / GPT-2 / '50% success' unexplained; 'hold the dots and slide')",
}
for k in ("hb-ch-1025-1", "hb-ch-1025-2", "hb-ch-1025-3", "hb-ch-1025-4"):
    HOLD_WHY[k] = "Story chain whose hand-off points to the held hb-1025-family-calendar"

UPDATE = {
    "lf-reel-1024-grandma-resp": dict(
        video="reels/lf-reel-1024-grandma-resp-s15c.mp4", cover="reels/lf-reel-1024-grandma-resp-s15c-cover.jpg",
        alt_text=("Short Reel in the Littlefold editorial look: big serif lines on soft pink and butter paper, highlighted words, "
                  "a halftone laundry-basket cut-out and the round stamp. Text: New dad, feeling left out? / You don't need to feed "
                  "baby to bond. Bath time counts. / Do this: Tonight: you give the bath. Handwritten: send this to a new dad.")),
    "ff-reel-1024-beneficiary": dict(
        video="reels/ff-reel-1024-beneficiary-s15c.mp4", cover="reels/ff-reel-1024-beneficiary-s15c-cover.jpg",
        caption_first="Your TFSA, after you die? If nobody is named on it, it goes through your estate.",
        alt_text=("Short Reel in the Fully Funded editorial look: big serif lines on soft cobalt and cream paper with highlighted words, "
                  "a halftone hourglass and the round stamp. Text: Your TFSA, after you die? / $100K TFSA, Ontario: Nobody named: "
                  "$750 probate. Named: $0. / Do this: Ask your bank who's named. Handwritten: send this to your partner.")),
    "ff-pan-1025am-paycheque-trail": dict(
        caption_replace=("Do this: this week, book one call with a wills lawyer", "Do this: this week, call a wills lawyer"),
        alt_text=("Edited video on a blueprint-grid sheet in the Fully Funded look. Frame 1: 'Not married? No will?' in a large serif "
                  "over a drawn diagram: an ESTATE box piped to two rooms, MARRIED (ticked) and COMMON-LAW, whose pipe is valved shut; "
                  "a coral $0 stamps into the common-law room. Then 'In Ontario:' with a bar drawn to scale: MARRIED SPOUSE gets the "
                  "first $350,000; COMMON-LAW PARTNER gets $0. Then 'Do this: Call a wills lawyer this week.' It loops back to the opening.")),
    "ff-reel-1025-tfsa-withdrawal-trap": dict(
        caption_replace=("The rule to remember: out this year? Back in January.", "The rule to remember: took it out this year? Put it back on or after January 1."),
        alt_text=("Edited video on a cream blueprint-grid sheet. Frame 1: 'Putting TFSA money back? Wait.' in a large serif over a "
                  "calendar ruler drawn to scale, January to December, with a coral arrow out at March and a blue arrow back in at June. "
                  "Then 'Took money out? It only goes back in tax-free next January 1.' as June to December is shaded. Then "
                  "'Do this: Wait for January 1.' It loops back to the opening.")),
    "hb-reel-1025-week-card": dict(
        alt_text=("Edited video in the Hourback look. Frame 1: big serif 'Sunday night? Your week fits on one card.' over a card titled "
                  "'Your week' with one line per day, Monday to Saturday. A rewind coin spins back to TAKE 1, in grey: five made-up "
                  "message bubbles pile up. TAKE 2: the prompt is typed and the real reply card drops in. Then 'Do this: Paste the "
                  "week's messages. Ask for one line a day.' with a card: 'Then check it. Ours slipped: it read \"before Tue\" as "
                  "\"on Tue.\"' It loops back to the opening.")),
}

NEW = [
    dict(id="lf-reel-1023-coat-off-buckle", account="littlefold", publish_at="2026-10-23T19:00:00-04:00",
         video="studio-oct23/littlefold/lf-reel-1023-coat-off-buckle.mp4", cover="studio-oct23/littlefold/lf-reel-1023-coat-off-buckle-cover.jpg",
         caption=("First cold morning? Coat off, then buckle. The warm layer goes on top of the straps.\n\n"
                  "Why: puffy coats and snowsuits squash flat in a crash. That leaves the harness loose, with room for a child to slip "
                  "out of the straps.\n\n"
                  "THE PINCH TEST: buckle up and tighten. Then try to pinch the strap flat at their chest. If you can pinch a fold of "
                  "strap, it's too loose. Tighten until you can't.\n\n"
                  "TO STAY WARM:\n1. Thin, close-fitting layers underneath (a thin fleece is fine).\n2. Buckle, tighten, pinch test.\n"
                  "3. Coat on backwards over the buckled straps, or a blanket on top.\n4. Hat, mittens and socks.\n"
                  "Babies usually need one more layer than you. Take the blanket off once the car warms up so they don't overheat.\n\n"
                  "Do this: coat off, buckle, blanket on. Every cold morning.\n\n"
                  "Send this to whoever does daycare drop-off.\n\n" + F_LF + "\n\n" + NOT_MED +
                  "\n\n#carseatsafety #winterbaby #newparents #canadianparents #toddlermom"),
         first_comment=("Source: American Academy of Pediatrics, HealthyChildren.org, 'Winter Car Seat Safety Tips': bulky clothing, "
                        "including winter coats and snowsuits, should not be worn underneath the harness of a car seat; padding can flatten "
                        "in a crash and leave the straps loose; 'If you can pinch the straps of the car seat harness, then it needs to be "
                        "tightened'; dress in thin layers; infants need one more layer than adults; put the coat on backwards or a blanket "
                        "over the buckled straps; hats, mittens and socks. Check your car seat's manual too. " + NOT_MED),
         alt_text=("Illustrated Reel in soft dawn light: pastel sky, sage hills, a smiling sun and a washing line of baby clothes. A puffy "
                   "pink coat lifts out of a car seat and the straps click in; the padding squashes flat and leaves a gap; fingers pinch "
                   "the slack strap and it pulls snug; a blanket falls over the straps. Text: first cold morning? Coat off. Then buckle. "
                   "/ because: Puffy padding squashes flat in a crash. / the pinch test: Pinch the strap at their chest. Extra? Tighten "
                   "it. / to stay warm: Thin layers. Blanket over the straps. / Do this: Coat off. Buckle. Blanket on. Source chip: AAP.")),
    dict(id="lf-reel-1024am-teething-cold-cloth", account="littlefold", publish_at="2026-10-24T08:00:00-04:00", trial="auto",
         video="studio-oct23/littlefold/lf-reel-1026am-teething-cold-cloth.mp4",
         cover="studio-oct23/littlefold/lf-reel-1026am-teething-cold-cloth-cover.jpg",
         caption=("Sore gums tonight? A cold cloth and a gentle rub. Two simple things that help.\n\n"
                  "THE RUB: wash your hands, then gently massage the sore spot with a fingertip or knuckle.\n\n"
                  "THE CLOTH: wet a clean washcloth, twist it, and chill it in the freezer for a bit. Let them chew it. Nothing "
                  "frozen rock-hard: hard objects can hurt tender gums.\n\n"
                  "SKIP: teething necklaces and beads (amber, wood, marble or silicone): choking and strangulation risk. And numbing "
                  "gels with benzocaine: they can be dangerous for children, and drool washes gels away anyway.\n\n"
                  "THE CATCH: a fever isn't a teething sign. Fever, diarrhea or a lot of crying? Call your baby's doctor.\n\n"
                  "Do this: tonight, twist a wet cloth and put it in the freezer, ready for the next sore night.\n\n"
                  "Send this to someone in the teething months.\n\n" + F_LF + "\n\n" + NOT_MED +
                  "\n\n#teething #babyteeth #newparents #canadianparents #babytips"),
         first_comment=("Source: American Academy of Pediatrics, HealthyChildren.org, 'Teething Pain': 'A light, gentle rub will soothe "
                        "your baby's gums'; twist a damp washcloth and place it in the freezer; don't let baby chew on anything frozen "
                        "solid; teething necklaces made of amber, wood, marble or silicone pose serious risks for choking and "
                        "strangulation; treatments with benzocaine can be dangerous for children; fever is not a sign of teething, call "
                        "your child's doctor for fever, diarrhea or excess crying. " + NOT_MED),
         alt_text=("Illustrated Reel in soft afternoon light: pastel sky, sage hills, a smiling sun and a washing line of baby clothes. "
                   "A frosty cloth and a fingertip rubbing in gentle circles; the cloth is wetted, twisted and chilled; a bead necklace "
                   "and a gel tube get 'no' rings. Text: sore gums tonight? Cold cloth. Gentle rub. / the cloth: Wet it. Twist it. "
                   "Chill it. / skip: Skip teething necklaces and numbing gels. Choking risk. Benzocaine gels can harm kids. / Do this: Chill a cloth "
                   "tonight. Fever isn't a teething sign. Call your baby's doctor. Source chip: AAP.")),
    dict(id="ff-reel-1026am-rule-of-72", account="fullyfunded", publish_at="2026-10-26T08:15:00-04:00", trial="auto",
         video="reels/ff-reel-1026am-rule-of-72-s15.mp4", cover="reels/ff-reel-1026am-rule-of-72-s15-cover.jpg",
         caption=("How long until $10K is $20K? Divide 72 by the yearly return. At 8% a year: about 9 years.\n\n"
                  "It's called the rule of 72. It's a shortcut for compounding: growth earning growth.\n\n"
                  "THE MATHS: $10,000 growing 8% a year is $19,990 after 9 years (1.08 to the power of 9 = 1.999). At 6%: 72 ÷ 6 = "
                  "about 12 years. At 10%: about 7 years.\n\n"
                  "WHY IT MATTERS: every doubling builds on the last one. $10K becomes $20K, then $40K, then $80K, about every 9 "
                  "years at 8%. Fees and starting late cut doublings off the end.\n\n"
                  "THE CATCH: real returns jump around year to year. The rule shows the shape, not a promise. Fees come off the "
                  "return first: 8% minus a 2% fee is 6%, and that's 12 years, not 9.\n\n"
                  "Do this: open your investing app, find the yearly return after fees, and divide 72 by it.\n\n"
                  "Send this to your \"I'll start later\" friend.\n\n" + F_FF + "\n\nEducation only, not financial advice. " + NG +
                  "\n\n#ruleof72 #compoundinterest #investing #personalfinance #moneytips"),
         first_comment=("Maths, not a forecast: 1.08^9 = 1.999, so $10,000 at 8% a year compounded yearly is $19,990 after 9 years; "
                        "72 ÷ 6 = 12 and 1.06^12 = 2.01; 72 ÷ 10 = 7.2 and 1.10^7.2 = 1.99. The rule of 72 is an approximation that works "
                        "best for rates around 6-10%. " + NG),
         alt_text=("Short Reel in the Fully Funded editorial look: big serif lines on soft cobalt, coral and cream paper with "
                   "highlighted words, a halftone hourglass and the round stamp. Text: How long until $10K is $20K? / the rule of 72: "
                   "72 ÷ the yearly return. 8%: about 9 years. / Do this: Investing app: 72 ÷ your return. Handwritten: send this to your "
                   "\"I'll start later\" friend.")),
    dict(id="lh-reel-1026am-when-where", account="lockedhour", publish_at="2026-10-26T08:30:00-04:00", trial="auto",
         video="reels/lh-reel-1026am-when-where-s15.mp4", cover="reels/lh-reel-1026am-when-where-s15-cover.jpg",
         caption=("Monday plans gone by noon? Write down when and where you'll do the one that matters.\n\n"
                  "Why it works: \"I'll do the report today\" is a wish. \"At 9, at my desk, I'll start the report\" is a plan your "
                  "brain can catch. When 9 o'clock and the desk show up, the next step is already decided.\n\n"
                  "THE RESEARCH: in a UK study of 248 people (Milne, Orbell & Sheeran, 2002), 91% of those who wrote down when and "
                  "where they'd exercise did it in the next week. In the other groups, fewer than 4 in 10 did.\n\n"
                  "HOW:\n1. Pick one task for today.\n2. Write: \"At [time], at [place], I'll [first step].\"\n3. Put it where you'll "
                  "see it: a sticky note on your screen, or a calendar event with the sentence as the title.\n\n"
                  "THE CATCH: one or two of these a day. Ten of them is just a new to-do list.\n\n"
                  "Do this: write one now on a sticky note: \"At 9, at my desk, I'll open the report.\"\n\n"
                  "Send this to your Monday-chaos friend.\n\n" + F_LH + "\n\n#productivity #habits #focus #mondaymotivation #lockedhour"),
         first_comment=("Source: Milne, S., Orbell, S. & Sheeran, P. (2002). Combining motivational and volitional interventions to promote "
                        "exercise participation: protection motivation theory and implementation intentions. British Journal of Health "
                        "Psychology, 7(2), 163-184. 248 participants randomly allocated to a control group or one of two intervention "
                        "groups; the group that also formed implementation intentions (when and where) exercised far more: 91%, against "
                        "under 40% in the other groups."),
         alt_text=("Short Reel in the Locked Hour zine look: big serif lines on butter, pink and cream paper with highlighter pills, a "
                   "halftone alarm clock and the round stamp. Text: Monday plans gone by noon? / habit tip: Write down when and where "
                   "you'll start. / Do this: Write: \"At 9, at my desk, I'll open it.\" Handwritten: send this to your Monday-chaos friend.")),
    dict(id="hb-reel-1024am-voice-transcripts", account="hourback", publish_at="2026-10-24T08:45:00-04:00",
         video="reels/hb-reel-1026am-voice-transcripts-s15.mp4", cover="reels/hb-reel-1026am-voice-transcripts-s15-cover.jpg",
         caption=("3-minute voice note, mid-meeting? WhatsApp can turn it into text so you can read it instead.\n\n"
                  "HOW: WhatsApp > Settings > Chats > Voice message transcripts. Turn it on and pick the language. Then press and "
                  "hold any voice message and tap Transcribe.\n\n"
                  "WHY IT'S PRIVATE: WhatsApp says the transcripts are made on your phone, so no one, including WhatsApp, hears or "
                  "reads your messages.\n\n"
                  "THE CATCH: names, slang and mixed languages can come out wrong. Anything important (an address, a time)? Play that "
                  "part.\n\n"
                  "Do this: Settings, Chats, Voice message transcripts. On. Try it on the last voice note you skipped.\n\n"
                  "Send this to your voice-note friend.\n\n" + F_HB + "\n\n#whatsapp #aitips #hourback #phonetips #learnai"),
         first_comment=("WhatsApp voice message transcripts launched in November 2024 (WhatsApp blog; Android Central, Nov 22, 2024): "
                        "Settings > Chats > Voice message transcripts; transcripts are generated on your device. Rolling out by language "
                        "and region; menus can differ by app version. Not sponsored."),
         alt_text=("Short Reel in the Hourback editorial look: big serif lines on butter, periwinkle and cream paper with highlighted "
                   "words, a drawn phone and the round stamp. Text: 3-minute voice note, mid-meeting? / try this: WhatsApp can turn "
                   "it into text. / Do this: Settings, Chats, Voice message transcripts. Then hold the note. Handwritten: send this to your voice-note friend.")),
]


def main():
    p = REPO / "schedule" / "posts.json"
    d = json.loads(p.read_text())
    by = {x["id"]: x for x in d["posts"]}
    published = json.loads((REPO / "state" / "published.json").read_text())
    pub_ids = set(published.get("posts", {}))
    for n in NEW:
        assert n["id"] not in by and n["id"] not in pub_ids, n["id"]
        for k in ("video", "cover"):
            assert (REPO / "media" / n[k]).exists(), n[k]
    before = {"touched": {k: by[k] for k in list(UPDATE) + HOLD}, "added": [n["id"] for n in NEW]}
    (REPO / "docs" / "social-recovery" / "2026-10-23-before.json").write_text(json.dumps(before, indent=2, ensure_ascii=False) + "\n")
    for k, u in UPDATE.items():
        x = by[k]
        for f in ("video", "cover", "alt_text"):
            if f in u:
                x[f] = u[f]
        if "caption_first" in u:
            lines = x["caption"].split("\n")
            lines[0] = u["caption_first"]
            x["caption"] = "\n".join(lines)
        if "caption_replace" in u:
            a, b = u["caption_replace"]
            assert a in x["caption"], (k, a)
            x["caption"] = x["caption"].replace(a, b)
        for f in ("video", "cover"):
            assert (REPO / "media" / x[f]).exists(), x[f]
    hp = REPO / "schedule" / "held-oct23.json"
    held = json.loads(hp.read_text()) if hp.exists() else {"_about": "Held by the Social studio on Oct 23 2026 (clarity gate). "
                                                                     "Reversible: move an entry back to posts.json.", "posts": []}
    for k in HOLD:
        held["posts"].append(dict(by[k], held_reason=HOLD_WHY[k]))
    d["posts"] = [x for x in d["posts"] if x["id"] not in HOLD] + NEW
    p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
    hp.write_text(json.dumps(held, indent=2, ensure_ascii=False) + "\n")
    print("updated", len(UPDATE), "held", len(HOLD), "added", len(NEW))


if __name__ == "__main__":
    main()

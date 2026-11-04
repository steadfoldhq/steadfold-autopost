#!/usr/bin/env python3
"""Writes studio/editorial/nov04/lockedhour.json (Locked Hour, Nov 4 studio build). Entries are added as each piece is clean.
Run: python3 studio/editorial/nov04_lockedhour_manifest.py"""
import copy
import json
import subprocess
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
OUTJ = REPO / "studio/editorial/nov04/lockedhour.json"


def dur(rel):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(REPO / "media" / rel)],
                         capture_output=True, text=True, check=True).stdout
    return round(float(out), 2)


ENTRIES = []

# ---------------------------------------------------------------- D) send test: lh-reel-1106-mix-3-kinds (replaces existing)
_n3 = json.loads((REPO / "studio/editorial/nov03/lockedhour.json").read_text())
D = copy.deepcopy(next(e for e in _n3 if e["id"] == "lh-reel-1106-mix-3-kinds"))
SEND_LINE = "Send this to a friend with a maths test this week."
assert "Send this to whoever has a maths test next week." in D["caption"]
D["caption"] = D["caption"].replace("Send this to whoever has a maths test next week.", SEND_LINE)
assert D["beats"][4].startswith("Maths test coming up? | Mix 3 kinds of problems. | Follow for one small sleep or focus trick a day.")
D["beats"][4] = D["beats"][4].replace("Follow for one small sleep or focus trick a day.",
                                      "Follow for one small sleep or focus trick a day. | " + SEND_LINE + " (pink pill)")
D["alt_text"] = D["alt_text"].rstrip() + f" Under the follow line, a pink pill: '{SEND_LINE}'"
D["duration_s"] = dur(D["video"])
D["send_test"] = True
D["replaces_existing"] = True
D["notes"] = ("SEND TEST (Performance desk order 1, Nov 4): ONE on-screen send line, '" + SEND_LINE + "', in a pink pill under the "
              "follow chip, fading in with it on the last beat (on screen 12.1-14.6 s, ~2.4 s). Everything else identical to the Nov 3 "
              "build (same spec, scenes, music, SFX, durations; total still 14.6 s by ffprobe). Overwrites "
              "media/studio-nov03/lockedhour/lh-reel-1106-mix-3-kinds.mp4; cover unchanged (it has no end beat). Caption send line "
              "changed to match the screen word for word. Grade on the Sat read: >=1 send per 100 reach. Strip + end frame reviewed "
              "(QG-1): follow chip kept at follow_y 700 so it does not touch the hook pill; send pill clears the shrunken card grid. "
              "Built by studio/editorial/nov04_lockedhour.py send. Previous notes: " + D["notes"])

ENTRIES.append(D)

FOLLOW = "Follow for one small sleep or focus trick a day."
NO_AGENT = ("No Agent tool in this maker session, so no fresh stranger picker could be launched; own pick used (brief: "
            "'If you have no Agent tool, note that and use your own pick').")

# ---------------------------------------------------------------- A) Sun Nov 8 19:00: last coffee 9 hours before bed
A = dict(
    id="lh-reel-1108-coffee-9h", account="lockedhour", publish_at="2026-11-08T19:00:00-05:00",
    video="studio-nov04/lockedhour/lh-reel-1108-coffee-9h.mp4", cover="studio-nov04/lockedhour/lh-reel-1108-coffee-9h-cover.jpg",
    caption=("Last coffee 9 hours before bed. Bed at 11? Your last coffee is at 2 pm. Caffeine keeps working long after you stop feeling it.\n\n"
             "WHY: caffeine blocks the signal that makes you sleepy as the day goes on, and it stays in your body for hours. So an afternoon "
             "coffee can still be working at bedtime. You may fall asleep fine and still get less sleep, and less deep sleep.\n\n"
             "HOW:\n1. Pick your usual bedtime.\n2. Count back 9 hours. Bed at 11 pm means your last coffee by 2 pm.\n"
             "3. After that: decaf or herbal tea.\n4. Count tea, cola and energy drinks too. Stronger drinks need even longer.\n\n"
             "THE RESEARCH: a 2023 review pooled 24 studies (Gardiner et al., Sleep Medicine Reviews). On average, caffeine cut total sleep "
             "by 45 minutes and sleep efficiency by 7%. To avoid losing sleep, the authors estimated a regular coffee (107 mg) should come at "
             "least 8.8 hours before bed, and a pre-workout drink (217.5 mg) at least 13.2 hours. In an earlier study (Drake et al. 2013), "
             "a large dose (400 mg) taken 6 hours before bed still cut measured sleep by more than an hour, and people didn't notice.\n\n"
             "THE CATCH: these are averages from mostly small studies, and people handle caffeine very differently. 9 hours is a guide for "
             "a regular cup, not an exact line. If you sleep well after an afternoon coffee, you may not need it.\n\n"
             "Do this tomorrow: Pick your bedtime. Count back 9 hours. Bed at 11? Last coffee by 2 pm. After that, decaf or herbal tea.\n\n"
             "Send this to whoever grabs a coffee at 4 pm.\n\n" + FOLLOW + "\n\n#sleep #caffeine #coffee #cantsleep #sleepbetter"),
    first_comment=("Sources (checked Nov 4 2026):\n"
                   "1) Gardiner, C., Weakley, J., Burke, L. M., Roach, G. D., Sargent, C., Maniar, N., Townshend, A. & Halson, S. L. (2023). "
                   "The effect of caffeine on subsequent sleep: A systematic review and meta-analysis. Sleep Medicine Reviews, 69, 101764. "
                   "doi:10.1016/j.smrv.2023.101764. 24 studies; caffeine reduced total sleep time by 45 min and sleep efficiency by 7%, "
                   "increased sleep onset latency by 9 min and wake after sleep onset by 12 min, reduced deep sleep (N3/N4) by 11.4 min. "
                   "To avoid a reduction in total sleep time, coffee (107 mg per 250 mL) should be consumed at least 8.8 h before bedtime "
                   "and a standard serve of pre-workout supplement (217.5 mg) at least 13.2 h before. Checked on PubMed (PMID 36870101) "
                   "and the ACU Research Bank record.\n"
                   "2) Drake, C., Roehrs, T., Shambroom, J. & Roth, T. (2013). Caffeine effects on sleep taken 0, 3, or 6 hours before "
                   "going to bed. Journal of Clinical Sleep Medicine, 9(11), 1195-1200. doi:10.5664/jcsm.3170. 12 healthy normal sleepers, "
                   "400 mg caffeine at 6, 3 or 0 h before bed vs placebo; at 6 h, objectively measured total sleep time fell by more than "
                   "1 hour, while self-reports suggested participants were unaware. Checked on the AASM release and ScienceDaily (Nov 2013).\n"
                   "Limits: averages from mostly small lab studies; individual sensitivity varies."),
    alt_text=("Locked Hour zine-style illustrated video on a butter-yellow dot grid. Opening line: 'Last coffee: 9 hours before bed.' "
              "A drawn wall clock with a pink coffee mug at 2 o'clock ('last coffee: 2 pm'); the hour hand sweeps to 11 while a pink "
              "wedge fills the 9 hours ('9 h') and a small bed appears at 11 ('9 hours later: bed'). On cream: 'the catch. It's still in "
              "you at bedtime. You can fall asleep fine and still sleep less, without noticing.' A person sleeps under a yellow blanket "
              "while the mug steams on the shelf ('asleep…', 'but sleeping less', 'coffee: still working'). 'the research: 24 studies: "
              "caffeine cut sleep by 45 minutes on average. For a regular coffee, the cutoff was about 9 hours before bed.' Source chip "
              "Gardiner et al. 2023, Sleep Medicine Reviews. Two bars: 'no caffeine' full, 'caffeine' shorter with a dashed gap '45 min "
              "less'. 'Do this tomorrow: Pick your bedtime. Count back 9 hours. Bed at 11? Last coffee by 2 pm. After that, decaf or "
              "herbal tea.' The clock hand counts back from 11 to 2 ('count back 9 hours'), a tea cup appears ('after 2 pm: decaf or "
              "herbal tea') and a tick. End: the hook again with 'Follow for one small sleep or focus trick a day.'"),
    beats=["Last coffee: 9 hours before bed. | last coffee: 2 pm (pill) | 9 h (on the clock wedge) | 9 hours later: bed (pill)",
           "the catch | It's still in you at bedtime. | You can fall asleep fine and still sleep less, without noticing. | asleep… (pill) | "
           "but sleeping less (pill) | coffee: still working (handwritten)",
           "the research | 24 studies: caffeine cut sleep by 45 minutes on average. | For a regular coffee, the cutoff was about 9 hours "
           "before bed. | Gardiner et al. 2023 · Sleep Medicine Reviews | no caffeine | caffeine | 45 min less (pill)",
           "Do this tomorrow: | Pick your bedtime. Count back 9 hours. | Bed at 11? Last coffee by 2 pm. After that, decaf or herbal tea. | "
           "count back 9 hours (pill) | after 2 pm: decaf or herbal tea (pill) | tick",
           "Last coffee: 9 hours before bed. | " + FOLLOW + " | stamp: LOCKED HOUR · ONE HOUR AT A TIME"],
    hook_options=["Last coffee: 9 hours before bed.", "Bed at 11? Coffee by 2.", "Coffee at 4? You may sleep less."],
    hook_picker=NO_AGENT + " Pick: option 1 (number in frame 0 and line 1, 6 words, states the rule itself). Option 2 was not "
                "picked because Thursday's Reel opens 'Bed at 11? Hard workout done by 10.' (same template 3 days earlier).",
    duration_s=None,
    style=("Body: LH zine drawn illustrated scene, ONE object (a wall clock with a coffee mug) doing the action by 1.7 s (hand sweeps 2 pm "
           "-> 11 pm, 9-hour wedge fills); new composition (clock wedge, bed + shelf mug, to-scale sleep bars, clock counting back). "
           "Cover: style 5 kinetic big text (loud), the warm-shower cover layout: 'Last coffee:' + giant '9' with pink stripe + 'hours "
           "before bed.' pill, Caveat 'bed at 11? last cup by 2', the drawn clock, stamp, butter dot grid. Neighbours: Sat 19:00 Look B "
           "(loud, pink) before, Mon 17:00 One Word No. 8 after; kinetic last used Nov 1 (warm shower)."),
    send_test=False,
    sources=["Gardiner C, Weakley J, Burke LM, Roach GD, Sargent C, Maniar N, Townshend A, Halson SL (2023). The effect of caffeine on "
             "subsequent sleep: A systematic review and meta-analysis. Sleep Medicine Reviews 69:101764. doi:10.1016/j.smrv.2023.101764",
             "Drake C, Roehrs T, Shambroom J, Roth T (2013). Caffeine effects on sleep taken 0, 3, or 6 hours before going to bed. "
             "J Clin Sleep Med 9(11):1195-1200. doi:10.5664/jcsm.3170"],
    notes=("Standalone (no Part 1/Part 2), no on-screen send line (not a send-test Reel). Number in frame 0 and line 1 ('9 hours'), "
           "payoff on screen at 2.4 s, Do-this 7 words, follow line on screen 12.0-14.6 s. Topic family: sleep (caffeine timing), not used "
           "on LH in the last 14+ days. The 9 hours is the review's 8.8 h estimate for a 107 mg coffee, rounded up; caption gives the "
           "exact figure. Drake 2013 (n=12, 400 mg) is in the caption as supporting evidence only, not the on-screen claim. Kicker changed "
           "from 'Do this tonight:' to 'Do this tomorrow:' because the Reel airs at 7 pm, after anyone's 2 pm cutoff. The 45-minute gap "
           "on the bars is drawn to scale against a 7-hour bar (no hours labelled). Music: existing LH v4 track lh-x-phone-down "
           "(loudnorm -14 LUFS) + library SFX. Strip, stills and cover reviewed (QG-1): fixed the mug missing from frame 0, a label "
           "sitting on the panel edge, a missing count-back wedge, a tea cup covering the clock hands, a stray arrow over the pill, and "
           "a mug floating between the bars. Considered and cut: phone in another room (Ward et al. 2017), because a pre-registered direct "
           "replication (Acta Psychologica 2022, 230:103717) found the effect did not replicate. Built by studio/editorial/nov04_lockedhour.py coffee."),
)
A["duration_s"] = dur(A["video"])
ENTRIES.append(A)

# ---------------------------------------------------------------- C) Mon Nov 9 17:00: One Word No. 8 "Same."
C = dict(
    id="lh-oneword-08", account="lockedhour", publish_at="2026-11-09T17:00:00-05:00", video=None, cover=None,
    images=["studio-nov04/lockedhour/lh-oneword-08/01.jpg", "studio-nov04/lockedhour/lh-oneword-08/02.jpg"],
    caption=("Slept in Sunday? Same alarm, all 7 days. Today's word: Same.\n\n"
             "One Word No. 8. Each episode is one word that guards your focus.\n\n"
             "WHY: your body clock runs on routine. Waking at very different times on different days keeps shifting it, a bit like "
             "flying across time zones every weekend. A steady wake-up time gives it one fixed point to set itself by.\n\n"
             "THE RESEARCH: 60,977 adults in the UK Biobank wore wrist trackers for about a week. Researchers scored how regular their "
             "sleep times were and followed them for about 6 years. Regularity predicted long-term health (risk of dying early, from any "
             "cause) better than how long people slept. The least regular sleepers did worst.\n\n"
             "HOW:\n1. Pick a wake-up time you can keep on a Saturday too.\n2. Set one alarm for it, 7 days a week.\n"
             "3. Tired on the weekend? Go to bed earlier rather than sleeping in.\n\n"
             "THE CATCH: this study shows a link, not proof that changing your schedule changes your health. Most people in it were "
             "older (average age 63), and the study adjusted for many other factors but can't rule out all of them. Shift workers and new "
             "parents can't always keep one time, and that's okay.\n\n"
             "Do this: Pick one wake-up time. Keep it all 7 days.\n\n"
             "Send this to whoever sleeps till noon on Sundays.\n\n" + FOLLOW + "\n\n"
             "#sleep #sleepschedule #morningroutine #focus #oneword\n\n"
             "One Word No. 9 lands Wed Nov 11 at 5 pm."),
    first_comment=("Source (checked Nov 4 2026):\n"
                   "Windred, D. P., Burns, A. C., Lane, J. M., Saxena, R., Rutter, M. K., Cain, S. W. & Phillips, A. J. K. (2024). "
                   "Sleep regularity is a stronger predictor of mortality risk than sleep duration: A prospective cohort study. Sleep, "
                   "47(1), zsad253 (online Sep 21 2023). doi:10.1093/sleep/zsad253. 60,977 UK Biobank participants (mean age 62.8), "
                   "Sleep Regularity Index from over 10 million hours of accelerometer data; 1,859 deaths over a mean 6.3 years. Compared "
                   "with the least regular fifth, the more regular fifths had 20%-48% lower all-cause mortality risk, adjusted for age, "
                   "sex, ethnicity and sociodemographic, lifestyle and health factors; regularity predicted mortality more strongly than "
                   "sleep duration. Checked on the Oxford UK Biobank publications record (bb30.ndph.ox.ac.uk) and the Broad Institute record (PMID 37738616).\n"
                   "Limits: observational; older UK adults; about one week of tracker data per person."),
    alt_text=("Locked Hour 2-slide carousel. Slide 1 on pink: black label 'One Word · No. 8', 'Slept in Sunday? Same alarm, all 7 days.' "
              "and the huge word 'Same.' over a pink highlighter stripe, with a drawn yellow alarm clock with pink bells, hands at 7:00 "
              "and '7 DAYS' on its top bar, the note 'one wake-up time, weekends too' and the line 'one word that guards your focus'. "
              "Slide 2 on cream: 'Steady sleep times mattered more than hours.' '60,977 adults wore wrist trackers for about a week. "
              "Over the next 6 years, how regular their sleep times were predicted their long-term health better than hours slept.' "
              "Do this: 'Pick one wake-up time. Keep it all 7 days.' Note: 'a link, not proof · average age 63'. Source Windred et al. "
              "2024, Sleep (UK Biobank)."),
    beats=["ONE WORD · No. 8 | Slept in Sunday? Same alarm, all 7 days. | Same. | 7 DAYS (on the drawn clock) | one wake-up time, "
           "weekends too | one word that guards your focus | @lockedhourhq | ONE WORD · No. 8",
           "Steady sleep times mattered more than hours. | 60,977 adults wore wrist trackers for about a week. Over the next 6 years, "
           "how regular their sleep times were predicted their long-term health better than hours slept. | Do this: Pick one wake-up "
           "time. Keep it all 7 days. | a link, not proof · average age 63 | Windred et al. 2024, Sleep (UK Biobank) / 60,977 adults; "
           "regularity beat sleep length | @lockedhourhq | ONE WORD · No. 8"],
    hook_options=["Slept in Sunday? Same alarm, all 7 days.", "One wake-up time, 7 days a week.", "7 days, 1 alarm time."],
    hook_picker=NO_AGENT + " Pick: option 1 (names the viewer's own Sunday moment the day after, number on the cover, 8 words).",
    duration_s=None,
    style=("Series One Word No. 8, the SAME 2-slide layout as No. 7 (cover on the LH pink dot field: black ONE WORD label, Instrument "
           "Serif hook with pink pill, huge riso word over a pink highlighter stripe, the drawn LH alarm clock as the one object, "
           "Caveat note, mono line; slide 2 on cream: headline pill, body, Do-this card, Caveat catch line, mono source)."),
    send_test=False,
    sources=["Windred DP, Burns AC, Lane JM, Saxena R, Rutter MK, Cain SW, Phillips AJK (2024). Sleep regularity is a stronger "
             "predictor of mortality risk than sleep duration: A prospective cohort study. Sleep 47(1):zsad253. doi:10.1093/sleep/zsad253"],
    notes=("Promised episode (No. 7 caption: 'One Word No. 8 lands Mon Nov 9 at 5 pm'). Caption last line promises No. 9 Wed Nov 11 at "
           "5 pm. Number on the cover ('7 days'), cover hook 8 words. Topic family: sleep timing (regularity); not used on LH in 14+ days "
           "(snooze No. 7 is about the alarm, not the schedule). Chosen over a second study topic because B (flashcards, 19:00) airs the "
           "same evening. The mortality outcome is stated plainly in the caption with the catch (observational, older adults); the "
           "slide says 'long-term health'. Slides reviewed (QG-1): removed a 7-day letter row under the clock that collided with the "
           "mono line, and replaced 'most were in their 60s' with the exact 'average age 63'. Volume/issue 47(1) checked on the Broad "
           "Institute publication record (PMID 37738616). Built by studio/editorial/nov04_lockedhour.py oneword."),
)
ENTRIES.append(C)

# ---------------------------------------------------------------- B) Mon Nov 9 19:00: get each flashcard right 3 times
B = dict(
    id="lh-reel-1109-flashcards-3x", account="lockedhour", publish_at="2026-11-09T19:00:00-05:00",
    video="studio-nov04/lockedhour/lh-reel-1109-flashcards-3x.mp4", cover="studio-nov04/lockedhour/lh-reel-1109-flashcards-3x-cover.jpg",
    caption=("Get each flashcard right 3 times before you drop it. Right once feels like you know it, but it isn't learned yet.\n\n"
             "WHY: pulling an answer out of memory is what makes it stick, and each extra right answer strengthens it. A card you get "
             "right once and set aside often slips away before the test. Coming back to the pile on later days locks it in.\n\n"
             "HOW:\n1. Go through the pile. Each time you get a card right, make a tally mark on its corner.\n"
             "2. Wrong? It goes to the back of the pile.\n3. 3 tallies: that card is done for tonight.\n"
             "4. Go through the whole pile again on 3 later days, until you get each card right once.\n\n"
             "THE RESEARCH: in 3 experiments with 533 students (Rawson & Dunlosky 2011), the authors' recommended schedule was 3 right "
             "answers in the first session, then 3 relearning sessions spread out over time; the later sessions mattered most on tests "
             "1 to 4 months later. In 4 experiments, Kornell & Bjork (2008) found that letting people drop flashcards had small but "
             "consistently negative effects on learning, and forcing a drop after one right answer hurt the most.\n\n"
             "THE CATCH: more right answers take more time, and after the first few the extra gain gets smaller. It works best for "
             "facts and definitions you can put on a card, not for practising problems.\n\n"
             "Do this tonight: Right 3 times? Then drop the card. Tally mark on the corner each time. Wrong? It goes to the back of the pile.\n\n"
             "Send this to whoever is making flashcards tonight.\n\n" + FOLLOW + "\n\n#studytips #flashcards #studying #exam #focus"),
    first_comment=("Sources (checked Nov 4 2026):\n"
                   "1) Rawson, K. A. & Dunlosky, J. (2011). Optimizing schedules of retrieval practice for durable and efficient "
                   "learning: How much is enough? Journal of Experimental Psychology: General, 140(3), 283-302. doi:10.1037/a0023956. "
                   "3 experiments, 533 students learning key concepts; initial criterion of 1 to 4 correct recalls, 1 to 5 relearning "
                   "sessions, retention tested 1 to 4 months later. The initial criterion had a strong early effect that weakened as "
                   "relearning increased; relearning had pronounced effects on long-term retention at little extra cost. Recommendation: "
                   "an initial criterion of 3 correct recalls, then relearning 3 times at widely spaced intervals. Checked on the "
                   "Memory-Key research summary of the paper.\n"
                   "2) Kornell, N. & Bjork, R. A. (2008). Optimizing self-regulated study: The benefits—and costs—of dropping "
                   "flashcards. Memory, 16(2), 125-136. doi:10.1080/09658210701763899. 4 experiments; being allowed to drop "
                   "flashcards had 'small but consistently negative effects on learning'; in Experiment 4, forced dropping after one "
                   "correct answer gave .21 vs .44 final-test accuracy without dropping. Checked on the authors' PDF (UCLA Bjork lab) "
                   "and Nate Kornell's publication list.\n"
                   "Related classroom replication: Rawson, Dunlosky & Sciartelli (2013), Educational Psychology Review, successive "
                   "relearning raised course exam scores (C to B).\n"
                   "Limits: lab and classroom studies with university students; materials were facts and concepts."),
    alt_text=("Locked Hour zine-style illustrated video on a butter-yellow dot grid. Opening line: 'Get each flashcard right 3 times.' "
              "A drawn flashcard gets pink tally marks one by one ('right once: keep it', 'right twice: keep it', 'right 3 times: "
              "done'), then flies to the 'done' pile; the 'to learn' pile sits on the left. On cream: 'the catch. Right once isn't "
              "learned yet. Drop a card after one right answer and you're more likely to forget it.' A card with one tally drops onto a "
              "pile ('right once… drop it?'), fades grey and shows a question mark ('later: forgotten'), with an X. 'the research: Best "
              "deal: 3 right tonight, then 3 quick reviews later. The later reviews mattered most on tests 1 to 4 months later.' Source "
              "chip Rawson & Dunlosky 2011, J Exp Psychology: General. Four cards under 'one card, over the weeks': 'tonight' 'right "
              "3×', 'review 1', 'review 2', 'review 3' each 'right 1×', and 'tested 1 to 4 months later'. 'Do this tonight: Right 3 "
              "times? Then drop the card. Tally mark on the corner each time. Wrong? It goes to the back of the pile.' The card gains "
              "tallies ('tally marks on the corner'), goes to the back of the pile with an X ('wrong? back of the pile'), then reaches "
              "3 and lands on 'done' ('3 tallies: done') with a tick. End: the hook again with 'Follow for one small sleep or focus "
              "trick a day.'"),
    beats=["Get each flashcard right 3 times. | right once: keep it (pill) | right twice: keep it (pill) | right 3 times: done (pill) | "
           "to learn | done | tick",
           "the catch | Right once isn't learned yet. | Drop a card after one right answer and you're more likely to forget it. | "
           "dropped | right once… drop it? (pill) | later: forgotten (pill) | ? (on the card) | X",
           "the research | Best deal: 3 right tonight, then 3 quick reviews later. | The later reviews mattered most on tests 1 to 4 "
           "months later. | Rawson & Dunlosky 2011 · J Exp Psychology: General | one card, over the weeks | tonight | review 1 | "
           "review 2 | review 3 | right 3× | right 1× | right 1× | right 1× | tested 1 to 4 months later (pill)",
           "Do this tonight: | Right 3 times? Then drop the card. | Tally mark on the corner each time. Wrong? It goes to the back of "
           "the pile. | the pile | done | tally marks on the corner (pill) | wrong? back of the pile (pill) | 3 tallies: done (pill) | tick",
           "Get each flashcard right 3 times. | " + FOLLOW + " | stamp: LOCKED HOUR · ONE HOUR AT A TIME"],
    hook_options=["Get each flashcard right 3 times.", "Got it right once? Keep the card.", "Flashcards: 3 right, then it's out."],
    hook_picker=NO_AGENT + " Pick: option 1 (number in frame 0 and line 1, 6 words, the action itself, no jargon).",
    duration_s=None,
    style=("Body: LH zine drawn illustrated scene, ONE object (a flashcard gaining tally marks) doing the action by 1.6 s (3 tallies, "
           "flies to 'done'); new composition (two piles + one card, a dropped card fading to '?', a 4-card review timeline, a card "
           "going to the back of the pile). Cover: style 13 sticky-note list (quiet) on the LH pink dot grid: lined note, red margin, "
           "tape, Caveat Brush title 'Get each flashcard right 3 times.', 3 ticked Caveat steps, the Reel's drawn card with 3 "
           "tallies, stamp. Neighbours: Mon 17:00 One Word No. 8 before, Sun 19:00 kinetic (loud) the day before; sticky last used "
           "Oct 28 (to-do list)."),
    send_test=False,
    sources=["Rawson KA, Dunlosky J (2011). Optimizing schedules of retrieval practice for durable and efficient learning: How much "
             "is enough? Journal of Experimental Psychology: General 140(3):283-302. doi:10.1037/a0023956",
             "Kornell N, Bjork RA (2008). Optimizing self-regulated study: The benefits—and costs—of dropping flashcards. "
             "Memory 16:125-136. doi:10.1080/09658210701763899"],
    notes=("Standalone (no Part 1/Part 2), no on-screen send line. Number in frame 0 and line 1 ('3 times'), payoff on screen at "
           "2.4 s, Do-this 7 words, follow line 12.0-14.6 s. Topic family: study (flashcard criterion), different from A (sleep/"
           "caffeine). Closest recent LH topics are 'write from memory' and 'spacing' (One Word No. 4, Oct 30): this one is a "
           "different, specific action (how many right answers before a card is dropped), and the brief listed 'retrieval practice "
           "with flashcards' as an idea. The review labels on screen are 'review 1/2/3' (the paper's spacing varied, so no day "
           "numbers are claimed). Music: existing LH v4 track lh-x-lock-in (loudnorm -14 LUFS) + library SFX. Stills, strip and "
           "cover reviewed (QG-1): made the tally marks big enough to read at phone size, made the step pills plain ('right once: "
           "keep it'), replaced 'a week later: gone' and 'still there months later' with wording the papers support ('later: "
           "forgotten', 'tested 1 to 4 months later'), cut two over-wrapped sub lines, held the card on screen longer before the drop, "
           "and rebuilt the cover list (items wrapped and spilled off the note). Built by studio/editorial/nov04_lockedhour.py cards."),
)
B["duration_s"] = dur(B["video"])
ENTRIES.append(B)

# ================================================================ Nov 4 gate verdicts (coordinator), applied after re-render
GATE_A = ("Gate (Nov 4): stranger picker chose option B ('Bed at 11? Coffee by 2.') and suggested 'last coffee' for clarity; adopted as "
          "'Bed at 11? Last coffee by 2 pm.' on frame 0, end beat and cover. Repeating Thursday's 'Bed at 11?' pattern 3 days apart was "
          "judged fine. CD nit applied: 'coffee: still working' is now a 46 px pill below the shelf, clear of the panel edge.")
GATE_B = ("Gate (Nov 4): clarity gate CONFUSING: 'Right 3 times? Then drop the card.' contradicted the research beat (viewers would drop "
          "cards for good). Rewritten to 'Right 3 times? Set it aside.' + 'Then review the pile again in a few days.'; pile label 'done' "
          "-> 'set aside'; end pill 'review again in a few days'. Stranger picker liked the stopping power of 'Got it right once? Keep the "
          "card.' but said it reads as 'you're done'; adopted 'Got it right once? Don't drop it yet.' (frame 0, end beat, cover). "
          "'Best deal:' -> 'What worked:'; the 'right 3× / right 1×' labels replaced by tally marks on each card plus the plain legend "
          "'each mark = one right answer'.")
GATE_C = ("Gate (Nov 4): no hook change. CD copy fixes: 'predicted their long-term health' -> 'predicted their risk of dying early' "
          "(the paper measured mortality); 'Over the next 6 years' -> 'Followed for about 6 years' (mean follow-up 6.30 years, up to "
          "7.8); age label: 'people averaging 63' (round 1) back to 'average age 63' (round 2: it read as '63 what?'). Round 2 CD fix: the pink highlighter bar on "
          "slide 01 was raised (top 760 -> 680) and trimmed to the word's width so it sits behind the lower third of 'Same.'.")


def sub(e, key, old, new):
    assert old in e[key], (e["id"], key, old)
    e[key] = e[key].replace(old, new)


# A) coffee
sub(A, "caption", "Last coffee 9 hours before bed. Bed at 11? Your last coffee is at 2 pm.", "Bed at 11? Last coffee by 2 pm. That's 9 hours before bed.")
sub(A, "alt_text", "Opening line: 'Last coffee: 9 hours before bed.'", "Opening line: 'Bed at 11? Last coffee by 2 pm.'")
sub(A, "alt_text", "End: the hook again", "End: the opening line again")
A["beats"][0] = A["beats"][0].replace("Last coffee: 9 hours before bed.", "Bed at 11? Last coffee by 2 pm.")
A["beats"][1] = A["beats"][1].replace("coffee: still working (handwritten)", "coffee: still working (pill)")
A["beats"][4] = A["beats"][4].replace("Last coffee: 9 hours before bed.", "Bed at 11? Last coffee by 2 pm.")
A["hook_options"] = ["Bed at 11? Last coffee by 2 pm.", "Last coffee: 9 hours before bed.", "Coffee at 4? You may sleep less."]
A["hook_picker"] = GATE_A
sub(A, "style", "'Last coffee:' + giant '9' with pink stripe + 'hours before bed.' pill, Caveat 'bed at 11? last cup by 2'",
    "'Bed at 11?' + 'Last coffee by' pill + giant '2 pm' with pink stripe, Caveat 'that's 9 hours before bed'")
sub(A, "notes", "Number in frame 0 and line 1 ('9 hours')", "Numbers in frame 0 and line 1 ('11', '2 pm'; the clock wedge reads '9 h')")
A["notes"] = GATE_A + " " + A["notes"]

# B) flashcards
B["caption"] = B["caption"].replace(
    "Get each flashcard right 3 times before you drop it. Right once feels like you know it, but it isn't learned yet.",
    "Got it right once? Don't drop the flashcard yet. Keep it in until you get it right 3 times, then review it again in a few days.")
sub(B, "caption", "3. 3 tallies: that card is done for tonight.", "3. 3 tallies: set that card aside for tonight.")
sub(B, "caption", "Do this tonight: Right 3 times? Then drop the card. Tally mark on the corner each time. Wrong? It goes to the back of the pile.",
    "Do this tonight: Right 3 times? Set it aside. Tally mark on the corner each time. Then review the pile again in a few days.")
B["alt_text"] = ("Locked Hour zine-style illustrated video on a butter-yellow dot grid. Opening line: 'Got it right once? Don't drop it yet.' "
                 "A drawn flashcard gets pink tally marks one by one ('right once: keep it', 'right twice: keep it', 'right 3 times: set "
                 "aside'), then flies to the 'set aside' pile; the 'to learn' pile sits on the left. On cream: 'the catch. Right once isn't "
                 "learned yet. Drop a card after one right answer and you're more likely to forget it.' A card with one tally drops onto a "
                 "pile ('right once… drop it?'), fades grey and shows a question mark ('later: forgotten'), with an X. 'the research: What "
                 "worked: 3 right tonight, then 3 reviews on later days. The later reviews mattered most on tests 1 to 4 months later.' "
                 "Source chip Rawson & Dunlosky 2011, J Exp Psychology: General. Under 'one card, over the weeks': a card with 3 tally marks "
                 "('tonight') and three cards with 1 mark each ('review 1', 'review 2', 'review 3'), the note 'each mark = one right answer' "
                 "and 'tested 1 to 4 months later'. 'Do this tonight: Right 3 times? Set it aside. Tally mark on the corner each time. Then "
                 "review the pile again in a few days.' The card gains tallies ('tally marks on the corner'), goes to the back of the pile "
                 "with an X ('wrong? back of the pile'), reaches 3 and lands on 'set aside' ('3 tallies: set it aside', then 'review again "
                 "in a few days') with a tick. End: the opening line again with 'Follow for one small sleep or focus trick a day.'")
B["beats"] = ["Got it right once? Don't drop it yet. | right once: keep it (pill) | right twice: keep it (pill) | right 3 times: set aside (pill) | to learn | set aside | tick",
              "the catch | Right once isn't learned yet. | Drop a card after one right answer and you're more likely to forget it. | dropped | right once… drop it? (pill) | later: forgotten (pill) | ? (on the card) | X",
              "the research | What worked: 3 right tonight, then 3 reviews on later days. | The later reviews mattered most on tests 1 to 4 months later. | Rawson & Dunlosky 2011 · J Exp Psychology: General | one card, over the weeks | tonight | review 1 | review 2 | review 3 | (tally marks on the cards: 3, 1, 1, 1) | each mark = one right answer (handwritten) | tested 1 to 4 months later (pill)",
              "Do this tonight: | Right 3 times? Set it aside. | Tally mark on the corner each time. Then review the pile again in a few days. | the pile | set aside | tally marks on the corner (pill) | wrong? back of the pile (pill) | 3 tallies: set it aside (pill) | review again in a few days (pill) | tick",
              "Got it right once? Don't drop it yet. | " + FOLLOW + " | stamp: LOCKED HOUR · ONE HOUR AT A TIME"]
B["hook_options"] = ["Got it right once? Don't drop it yet.", "Get each flashcard right 3 times.", "Flashcards: 3 right, then it's out."]
B["hook_picker"] = GATE_B
sub(B, "style", "Caveat Brush title 'Get each flashcard right 3 times.', 3 ticked Caveat steps",
    "Caveat Brush title 'Got it right once? Don't drop it yet.', 3 ticked Caveat steps ('right? tally on the corner', '3 tallies: set it aside', 'review it in a few days')")
sub(B, "notes", "Number in frame 0 and line 1 ('3 times')", "Number in frame 0 and line 1 ('once'; the drawn card shows 1-3 tally marks)")
sub(B, "notes", "Do-this 7 words", "Do-this 6 words")
B["notes"] = GATE_B + " " + B["notes"]

# C) One Word No. 8
sub(C, "caption", "followed them for about 6 years.", "followed them for about 6 years (mean 6.3, up to 7.8).")
pass
sub(C, "caption", "Regularity predicted long-term health (risk of dying early, from any cause)", "Regularity predicted the risk of dying early (from any cause)")
for k in ("alt_text",):
    sub(C, k, "Over the next 6 years, how regular their sleep times were predicted their long-term health better than hours slept.",
        "Followed for about 6 years, how regular their sleep times were predicted their risk of dying early better than hours slept.")
    pass
C["beats"][1] = (C["beats"][1].replace("Over the next 6 years, how regular their sleep times were predicted their long-term health better than hours slept.",
                                       "Followed for about 6 years, how regular their sleep times were predicted their risk of dying early better than hours slept.")
                 .replace("a link, not proof · people averaging 63", "a link, not proof · average age 63"))
assert "risk of dying early" in C["beats"][1] and "average age 63" in C["beats"][1]
C["hook_picker"] = C["hook_picker"] + " " + GATE_C
C["notes"] = GATE_C + " " + C["notes"]
pass

if __name__ == "__main__":
    OUTJ.write_text(json.dumps(ENTRIES, indent=1, ensure_ascii=False) + "\n")
    print(OUTJ, [e["id"] for e in ENTRIES])

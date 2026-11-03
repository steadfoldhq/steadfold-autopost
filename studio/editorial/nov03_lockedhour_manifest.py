#!/usr/bin/env python3
"""Writes studio/editorial/nov03/lockedhour.json (Locked Hour, Nov 3 studio run). Entries are added as each piece passes
its own render review: python3 studio/editorial/nov03_lockedhour_manifest.py [mix] [music] [oneword] [workout]"""
import copy
import json
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
MAN = REPO / "studio/editorial/nov03/lockedhour.json"
FOLLOW = "Follow for one small sleep or focus trick a day."


def dur(rel):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(REPO / "media" / rel)],
                         capture_output=True, text=True, check=True).stdout
    return round(float(out), 2)


def mix():
    v = "studio-nov03/lockedhour/lh-reel-1106-mix-3-kinds.mp4"
    return {
        "id": "lh-reel-1106-mix-3-kinds", "account": "lockedhour", "publish_at": "2026-11-06T19:00:00-05:00",
        "video": v, "cover": "studio-nov03/lockedhour/lh-reel-1106-mix-3-kinds-cover.jpg",
        "caption": (
            "Maths test coming up? Mix 3 kinds of problems in every practice set. It feels harder while you practise, and you remember more on the test.\n\n"
            "WHY: when every problem on the page is the same kind, you know the method before you even read the question. On the real test the kinds are mixed, "
            "so the hard part is spotting which method each problem needs. Mixed practice trains exactly that.\n\n"
            "HOW:\n1. Pick 3 kinds of problems the test will cover (say, one from each of your last 3 chapters).\n"
            "2. Take a few problems of each kind.\n"
            "3. Put them in order 1 of each kind, then repeat: A, B, C, A, B, C.\n\n"
            "THE RESEARCH: in a study by Rohrer and Taylor (University of South Florida), students learned to find the volume of 4 unusual shapes. "
            "While practising, the students who did one shape at a time scored 89% and the mixers 60%. A week later, on the test, it flipped: mixers 63%, one-at-a-time 20%. "
            "A 2019 review of 59 studies (Brunmair & Richter) found mixing helps on average, maths included.\n\n"
            "THE CATCH: that experiment was small (18 students), and mixing feels worse while you do it, so expect more mistakes in practice. "
            "It helps when you have to tell kinds of problems apart (maths, science, question types). For learning lists of words, the same review found mixing did worse.\n\n"
            "Do this tonight: 1 of each kind, then repeat. Take problems from your last 3 chapters and shuffle them into one set.\n\n"
            "Send this to whoever has a maths test next week.\n\n"
            f"{FOLLOW}\n\n#studytips #studying #maths #exam #focus"),
        "first_comment": (
            "Sources (checked Nov 3 2026):\n"
            "1) Rohrer, D. & Taylor, K. (2007). The shuffling of mathematics problems improves learning. Instructional Science, 35, 481–498. doi:10.1007/s11251-007-9015-8. "
            "Experiment 2: 18 undergraduates learned the volume of 4 obscure solids (wedge, spherical cone, spheroid, half cone) over 2 practice sessions a week apart. "
            "Practice scores: blocked 89%, mixed 60%. Test 1 week later: mixed 63%, blocked 20%. Authors: 'mixed practice produced superior test performance and inferior practice performance.' Checked on the paper (author PDF).\n"
            "2) Brunmair, M. & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. Psychological Bulletin, 145(11), 1029–1052. doi:10.1037/bul0000209. "
            "59 studies, 238 effect sizes: overall benefit of interleaving g = 0.42; mathematical tasks g = 0.34; words g = -0.39 (blocking did better). Checked on PubMed and the authors' manuscript.\n"
            "Limits: one small experiment for the headline numbers; the review's effects vary by material."),
        "alt_text": (
            "Locked Hour zine-style illustrated video on a butter-yellow dot grid. Opening line: 'Maths test coming up? Mix 3 kinds of problems.' "
            "Nine drawn problem cards (pink triangle, yellow circle, blue square) sit in rows of one kind ('one kind at a time…'), then fly into a mixed grid ('mixed together'). "
            "On cream: 'try this. It feels harder. You remember more. Mixed up, you have to pick the method each time, just like on the real test.' A student looks at one card that flips between kinds "
            "('which kind is this one?', then 'pick the method, then solve' and a tick). 'the research: A week later, mixed practice scored 63% vs 20% against doing one kind at a time, even though it felt harder while practising.' "
            "Bars for 'the test, a week later': 'one kind at a time' 20% ('felt easier'), 'mixed' 63% with a tick. Source chip Rohrer & Taylor 2007, Instructional Science. "
            "'Do this tonight: 1 of each kind, then repeat. Take problems from your last 3 chapters and shuffle them into one set.' Cards deal from three piles ('chapter 4', 'chapter 5', 'chapter 6') into 'one mixed set'. "
            "End: the hook again with 'Follow for one small sleep or focus trick a day.' and the Locked Hour stamp."),
        "beats": [
            "Maths test coming up? (small kicker) | Mix 3 kinds of problems. | one kind at a time… (pill) | mixed together (pill; cards shuffled by 1.6 s)",
            "try this | It feels harder. You remember more. | Mixed up, you have to pick the method each time, just like on the real test. | which kind is this one? (pill) | pick the method, then solve (pill) | tick",
            "the research | A week later, mixed practice scored 63% vs 20% | against doing one kind at a time, even though it felt harder while practising. | Rohrer & Taylor 2007 · Instructional Science | the test, a week later | 20% | 63% | one kind at a time | mixed | felt easier (pill) | tick",
            "Do this tonight: | 1 of each kind, then repeat. | Take problems from your last 3 chapters and shuffle them into one set. | chapter 4 | chapter 5 | chapter 6 | one mixed set (pill) | tick",
            f"Maths test coming up? | Mix 3 kinds of problems. | {FOLLOW} | stamp: LOCKED HOUR · ONE HOUR AT A TIME",
        ],
        "hook_options": [
            "Maths test coming up? Mix 3 kinds of problems.",
            "Studying maths tonight? 1 of each kind, then repeat.",
            "Practice feels easy? Mix 3 kinds and it'll stick.",
        ],
        "duration_s": dur(v),
        "style": ("Body: LH zine drawn illustrated scene, ONE object (practice-problem cards in 3 kinds) doing the action by 1.6 s (blocked rows shuffle into a mixed grid); "
                  "new composition (card grid, a student with one flipping card, a to-scale bar chart, three chapter piles dealt into one set). "
                  "Cover: style 8 compare (quiet) on the LH cream dot grid: Inter Display hook 'Maths test coming up? Mix 3 kinds of problems.' with pink pill, Caveat line "
                  "'1 of each kind, then repeat', two drawn card grids ('one kind at a time' X / 'mixed' tick), stamp. Neighbours: Fri 17:00 One Word No. 7 (series) before, "
                  "Sat 19:00 Look B (loud) after; compare last used Nov 2 (lamp)."),
        "send_test": False,
        "sources": [
            "Rohrer D, Taylor K (2007). The shuffling of mathematics problems improves learning. Instructional Science 35:481-498. doi:10.1007/s11251-007-9015-8 (Experiment 2: test 63% vs 20%, practice 60% vs 89%, n=18)",
            "Brunmair M, Richter T (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. Psychological Bulletin 145(11):1029-1052. doi:10.1037/bul0000209",
        ],
        "notes": ("Standalone (no Part 1/Part 2). Number in frame 0 and line 1 ('Mix 3 kinds'), payoff line on screen at 2.4 s, Do-this 6 words, follow line on screen 12.0-14.6 s (2.6 s). "
                  "Topic family: study/focus (not sleep); interleaving not used on LH in the last 14+ days (spacing was One Word No. 4 on Oct 30, a different trick). "
                  "Music: existing LH v4 track lh-x-tick-boom (loudnorm -14 LUFS) + library SFX. Strip and cover reviewed (QG-1): fixed the follow chip overlapping the hook "
                  "(follow_y 640 -> 700), the tick that covered '63%', and a pill that named letters the cards don't show. Considered and cut: Ramirez & Beilock 2011 "
                  "(writing worries before a test) because the Camerer et al. 2018 replication failed."),
    }


def music():
    v = "studio-nov03/lockedhour/lh-reel-1107-calm-music-45.mp4"
    return {
        "id": "lh-reel-1107-calm-music-45", "account": "lockedhour", "publish_at": "2026-11-07T19:00:00-05:00",
        "video": v, "cover": "studio-nov03/lockedhour/lh-reel-1107-calm-music-45-cover.jpg",
        "caption": (
            "Can't switch off? 45 minutes of calm music at bedtime, every night. In a 3-week study, calm music improved students' sleep. An audiobook didn't.\n\n"
            "WHY: slow, quiet music gives a busy mind something easy to follow, without the story or words that keep you listening. Done every night, it also becomes a cue that it's time to sleep.\n\n"
            "HOW:\n1. Pick a calm playlist: slow, quiet, no lyrics you'll sing along to.\n"
            "2. Volume low, phone face down out of reach.\n"
            "3. Set a sleep timer for 45 minutes. On Spotify: tap ••• on the song, then Sleep timer, then 45 minutes.\n"
            "4. Repeat every night for a few weeks.\n\n"
            "THE RESEARCH: 94 students with poor sleep were split into 3 groups. One listened to calm classical music for 45 minutes at bedtime, one to an audiobook, one did nothing, every night for 3 weeks. "
            "Sleep quality improved only in the music group (Harmat, Takács & Bódizs 2008). A 2022 Cochrane review of 13 trials (1,007 adults with insomnia) found music probably improves how well people "
            "feel they sleep (moderate-certainty evidence).\n\n"
            "THE CATCH: the improvement is in how people rated their sleep, and it builds over nights, not in one. Evidence that music makes you fall asleep faster is weaker (low certainty). "
            "If you've slept badly for weeks, talk to a doctor: insomnia has good treatments.\n\n"
            "Do this tonight: Calm playlist on. Sleep timer: 45 minutes.\n\n"
            "Send this to whoever is still scrolling at 1 am.\n\n"
            f"{FOLLOW}\n\n#sleep #insomnia #cantsleep #sleepbetter #focus"),
        "first_comment": (
            "Sources (checked Nov 3 2026):\n"
            "1) Harmat, L., Takács, J. & Bódizs, R. (2008). Music improves sleep quality in students. Journal of Advanced Nursing, 62(3), 327–335. "
            "94 students (19–28) with sleep complaints; relaxing classical music vs audiobook vs no intervention, 45 minutes at bedtime for 3 weeks; PSQI sleep quality improved significantly "
            "in the music group only, and depressive symptoms fell in the music group. Checked on Semmelweis University's page and the Cochrane review's study table.\n"
            "2) Jespersen, K. V., Pando-Naude, V., Koenig, J., Jennum, P. & Vuust, P. (2022). Listening to music for insomnia in adults. Cochrane Database of Systematic Reviews, Issue 8, CD010459. "
            "doi:10.1002/14651858.CD010459.pub3. 13 trials, 1,007 participants; prerecorded music daily for 25 to 50 minutes for 3 days to 3 months; music 'probably' gives a large improvement in "
            "subjective sleep quality (moderate certainty); effects on time to fall asleep and sleep duration low certainty. Checked on cochrane.org.\n"
            "Spotify sleep-timer steps and options (5, 10, 15, 30, 45 minutes, 1 hour, end of track): How-To Geek guide, checked Nov 3 2026."),
        "alt_text": (
            "Locked Hour zine-style illustrated video on a butter-yellow dot grid. Opening line: \"Can't switch off? 45 minutes of calm music.\" "
            "A drawn person lies awake in bed, a pulse line beside them ('still awake…'); a yellow speaker on the wall shelf switches on, music notes drift over the bed "
            "('calm music, low volume'), their eyes close and z's rise. On cream: 'try this. Calm music can help you sleep better. Play it every night for a few weeks, not just once. Quiet and slow.' "
            "A 3-week calendar fills square by square with music notes ('every night, not just once'), a small bed, a tick. 'the research: 94 students, 3 weeks: music helped. An audiobook didn't. "
            "45 minutes of calm classical music at bedtime, every night.' Source chip Harmat et al. 2008, J Adv Nursing. Three icons under 'did sleep get better?': 'nothing' X, 'audiobook' X, 'calm music' tick. "
            "'Do this tonight: Calm playlist on. Sleep timer: 45 minutes. Spotify: tap ••• on the song, then Sleep timer, then 45 minutes.' A drawn phone shows 'Sleep timer' with '15 min', '30 min', '45 min' (chosen), '1 hour'; "
            "notes play from the speaker, the screen goes dark with a moon, a tick. End: the hook again with 'Follow for one small sleep or focus trick a day.' and the Locked Hour stamp."),
        "beats": [
            "Can\'t switch off? 45 minutes of calm music. | still awake… (pill) | calm music, low volume (pill; speaker on at 0.8 s, eyes closed by 1.6 s) | z z",
            "try this | Calm music can help you sleep better. | Play it every night for a few weeks, not just once. Quiet and slow. | every night, not just once | tick",
            "the research | 94 students, 3 weeks: music helped. An audiobook didn't. | 45 minutes of calm classical music at bedtime, every night. | Harmat et al. 2008 · J Adv Nursing | did sleep get better? | nothing | audiobook | calm music | X | X | tick",
            "Do this tonight: | Calm playlist on. Sleep timer: 45 minutes. | Spotify: tap ••• on the song, then Sleep timer, then 45 minutes. | Sleep timer | 15 min | 30 min | 45 min | 1 hour | tick",
            f"Can't switch off? 45 minutes of calm music. | {FOLLOW} | stamp: LOCKED HOUR · ONE HOUR AT A TIME",
        ],
        "hook_options": [
            "Can't switch off? 45 minutes of calm music.",
            "Lying awake at midnight? Set a 45-minute music timer.",
            "Mind racing in bed? 45 minutes of slow music.",
        ],
        "duration_s": dur(v),
        "style": ("Body: LH zine drawn illustrated scene, ONE object (a yellow speaker on the bedroom shelf) doing the action by 1.2 s (switches on, notes drift, the sleeper's eyes close by 1.6 s); "
                  "new composition (bedroom with a shelf speaker, a 3-week calendar, three-way compare, a phone sleep-timer screen). "
                  "Cover: style 1 Look B big-headline (loud) on the LH pink dot grid: Inter Display hook \"Can't switch off? 45 minutes of calm music.\" at 136 px in 3 lines with pills (gate rev 2), Caveat save-line "
                  "'set a sleep timer tonight ↓', the Reel's bedroom scene (bed + shelf speaker + notes) large and centred, stamp on the scene's corner. Neighbours: Fri 19:00 compare (quiet) before; Look B last used Nov 3 (timer)."),
        "send_test": False,
        "sources": [
            "Harmat L, Takács J, Bódizs R (2008). Music improves sleep quality in students. Journal of Advanced Nursing 62(3):327-335 (PMID 18426457)",
            "Jespersen KV, Pando-Naude V, Koenig J, Jennum P, Vuust P (2022). Listening to music for insomnia in adults. Cochrane Database Syst Rev Issue 8: CD010459. doi:10.1002/14651858.CD010459.pub3",
            "How-To Geek, 'How to Set Up a Sleep Timer in Spotify' (sleep-timer options and steps)",
        ],
        "notes": ("Standalone. Number in frame 0 and line 1 ('45 minutes'), payoff line on screen at 2.4 s, Do-this 6 words, follow line on screen 12.0-14.6 s. "
                  "Different family from Fri (sleep vs study). Not a recent topic (no music-for-sleep post on LH; 'lyrics' Oct 24 was study music). "
                  "The Reel's own soundtrack is the existing LH v4 track lh-x-phone-down (the calmest of the 3, 110 bpm), loudnorm -14 LUFS; it is our licensed library audio, not the music the post recommends. "
                  "Spotify named only as the place the step is done (no logo, no brand art). Strip and cover reviewed (QG-1): speaker enlarged, notes made bigger and kept inside the panel. "
                  "Gate rev 2 (Nov 3): the hook-picker line is now frame 0 (no kicker) and caption line 1; the awake pill reads 'still awake…' so it no longer repeats the hook; "
                  "cover rebuilt (hook 136 px, the Reel's scene large and centred, stamp moved off the bottom-left)."),
    }


def workout():
    src = json.loads((REPO / "studio/editorial/nov02/lockedhour.json").read_text())
    e = copy.deepcopy(next(x for x in src if x["id"] == "lh-reel-1105-workout-1h"))
    assert e["beats"][1].startswith("sleep, part 2 | ")
    e["beats"][1] = e["beats"][1].replace("sleep, part 2 | ", "the catch | ", 1)
    assert "On cream: 'sleep, part 2. " in e["alt_text"]
    e["alt_text"] = e["alt_text"].replace("On cream: 'sleep, part 2. ", "On cream: 'the catch. ", 1)
    e["duration_s"] = dur(e["video"])
    e["replaces_existing"] = True
    e["notes"] = ("Nov 3 desk order (job D): beat-2 kicker 'sleep, part 2' -> 'the catch' (no sequel framing on screen); everything else identical "
                  "(spec deep-copied from nov02_lockedhour.py SPECS['workout'], re-rendered by nov03_lockedhour.py workout, same mp4 path overwritten; cover unchanged, it has no kicker). "
                  "Caption keeps 'Part 2' per desk order 1 ('Keep Part 2 in the caption'). Previous notes: " + e["notes"])
    return e


def oneword():
    return {
        "id": "lh-oneword-07", "account": "lockedhour", "publish_at": "2026-11-06T17:00:00-05:00",
        "video": None, "cover": None,
        "images": ["studio-nov03/lockedhour/lh-oneword-07/01.jpg", "studio-nov03/lockedhour/lh-oneword-07/02.jpg"],
        "caption": (
            "Hit snooze again? 30 minutes is okay. Today's word: Snooze.\n\n"
            "One Word No. 7. Each episode is one word that guards your focus.\n\n"
            "WHY: if you're someone who snoozes anyway and falls back asleep easily, a short snooze barely costs you sleep, "
            "and waking in stages may mean you're less likely to be pulled out of deep sleep.\n\n"
            "THE RESEARCH: 31 regular snoozers slept in a sleep lab. One morning they snoozed for 30 minutes; another morning the first alarm got them up. "
            "Snoozing cost about 6 minutes of sleep, and on tests right after waking they did as well or a bit better. Mood, sleepiness and the morning stress hormone showed no clear change.\n\n"
            "HOW:\n1. Set the first alarm no more than 30 minutes before you have to be up.\n"
            "2. Snooze if you like.\n"
            "3. The last alarm means feet on the floor.\n\n"
            "THE CATCH: it's one small lab study of people who already snooze, and only 30 minutes was tested. If you find it hard to fall back asleep, "
            "or you feel groggy all morning, one alarm at your real wake-up time is the simpler choice.\n\n"
            "Do this: Snoozing anyway? Stop at 30 minutes, then get up.\n\n"
            "Send this to whoever sets 5 alarms every morning.\n\n"
            f"{FOLLOW}\n\n#sleep #morningroutine #snooze #focus #oneword\n\n"
            "One Word No. 8 lands Mon Nov 9 at 5 pm."),
        "first_comment": (
            "Source (checked Nov 3 2026):\n"
            "Sundelin, T., Landry, S. & Axelsson, J. (2023). Is snoozing losing? Why intermittent morning alarms are used and how they affect sleep, cognition, cortisol, and mood. "
            "Journal of Sleep Research. doi:10.1111/jsr.14054. Study 1: survey of 1,732 people about waking habits. Study 2: 31 habitual snoozers, polysomnography in a sleep lab, "
            "30 minutes of snoozing vs waking at the final alarm. Abstract: snoozing 'resulted in about 6 min of lost sleep, while preventing awakenings from slow-wave sleep'; "
            "'30 min of snoozing improved or did not affect performance on cognitive tests directly upon rising'; no clear effects on the cortisol awakening response, morning sleepiness or mood. "
            "Checked on the abstract (reviewer.ly listing) and Stockholm University's release via ScienceDaily (Oct 2023).\n"
            "Limits: small sample of regular snoozers only, one snooze length, one morning in a lab."),
        "alt_text": (
            "Locked Hour 2-slide carousel. Slide 1 on pink: black label 'One Word · No. 7', 'Hit snooze again? 30 minutes is okay.' and the huge word 'Snooze.' over a pink highlighter stripe, "
            "with a drawn yellow alarm clock with pink bells, hands at 6:30, a pink SNOOZE bar and three z's, the note 'up to 30 minutes, then really get up' and the line 'one word that guards your focus'. "
            "Slide 2 on cream: 'Snoozing cost only about 6 minutes of sleep.' '31 regular snoozers slept in a sleep lab. After 30 minutes of snoozing, they did as well or a bit better on tests right after waking "
            "than when the first alarm got them up.' Do this: 'Snoozing anyway? Stop at 30 minutes, then get up.' Note: 'tested on regular snoozers · one small lab study'. Source Sundelin, Landry & Axelsson 2023."),
        "beats": [
            "ONE WORD · No. 7 | Hit snooze again? 30 minutes is okay. | Snooze. | SNOOZE (on the drawn clock) | z z z | up to 30 minutes, then really get up | one word that guards your focus | @lockedhourhq | ONE WORD · No. 7",
            "Snoozing cost only about 6 minutes of sleep. | 31 regular snoozers slept in a sleep lab. After 30 minutes of snoozing, they did as well or a bit better on tests right after waking than when the first alarm got them up. | Do this: Snoozing anyway? Stop at 30 minutes, then get up. | tested on regular snoozers · one small lab study | Sundelin, Landry & Axelsson 2023, J Sleep Research / 31 regular snoozers; about 6 minutes of sleep lost | @lockedhourhq | ONE WORD · No. 7",
        ],
        "hook_options": ["Hit snooze again? 30 minutes is okay.", "5 alarms every morning? Keep it to 30 minutes.", "Snoozing for 30 minutes cost about 6 minutes of sleep."],
        "duration_s": None,
        "style": "One Word series layout (same cover as lh-oneword-06: black label, serif hook with pill, huge riso word over pink stripe, one drawn object, Caveat line, mono footer); 2 slides pink/cream (desk order: 2 slides, minimal hours).",
        "send_test": False,
        "sources": ["Sundelin T, Landry S, Axelsson J (2023). Is snoozing losing? Why intermittent morning alarms are used and how they affect sleep, cognition, cortisol, and mood. Journal of Sleep Research. doi:10.1111/jsr.14054"],
        "notes": ("Gate rev 2 (Nov 3): slide 2 headline now 'Snoozing cost only about 6 minutes of sleep.' (reassurance, not a warning). Promised by lh-oneword-06's caption ('One Word No. 7 is Friday at 5 pm.'). Desk order 3: 2 slides (No. 6 had 3; the cover layout is identical, the research + Do-this share slide 2). "
                  "Number on the cover ('30 minutes'); cover hook 6 words in the viewer's words. No round stamp (No. 5/6 have none). Object: the LH signature alarm clock, drawn. "
                  "Caption last line promises No. 8 Mon Nov 9 at 5 pm; nothing built for No. 8 yet. The Wiley article page was blocked for this session, so the volume/issue "
                  "is not cited; abstract wording checked on a mirror of the abstract plus the university release."),
    }


BUILD = {"mix": mix, "music": music, "workout": workout, "oneword": oneword}

if __name__ == "__main__":
    cur = json.loads(MAN.read_text()) if MAN.exists() else []
    for key in sys.argv[1:]:
        e = BUILD[key]()
        cur = [x for x in cur if x["id"] != e["id"]] + [e]
    order = ["lh-oneword-07", "lh-reel-1106-mix-3-kinds", "lh-reel-1107-calm-music-45", "lh-reel-1105-workout-1h"]
    cur.sort(key=lambda x: order.index(x["id"]) if x["id"] in order else 99)
    MAN.write_text(json.dumps(cur, indent=1, ensure_ascii=False) + "\n")
    print(MAN, [x["id"] for x in cur])

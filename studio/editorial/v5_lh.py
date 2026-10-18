"""Locked Hour content, Oct 18-21. ONE-READ rewrite #2 (Oct 17, ~23:00): full sentences, one research finding per item,
told through an everyday moment. Uses post()/reel()/chain() from specs_teach. Only this page's entries live here.

Removed from the queue (replaced in the same slots): lh-reel-1018am-pick-3, lh-reel-1019am-pick-task,
lh-w2-08-lockin-kickoff, lh-w2-07-minute-by-minute."""
from specs_teach import post, reel, chain, FF, HB, LH, LF, NG, NOT_MED, MADE, PRIV, K  # noqa: F401


def _w(text, width=14):
    """Reel hook/say lines: the kinetic type does not wrap by itself, so break into short lines (<= width chars) here.
    Same logic as teach_reels.rewrap (kept local so this file stays import-light)."""
    toks, on = [], False
    for w in text.replace(" / ", " ").split():
        if w.startswith("*"):
            on = True
        toks.append((w.replace("*", ""), on))
        if on and w.endswith("*"):
            on = False
    lines, cur = [], []
    for t in toks:
        if cur and len(" ".join(x for x, _ in cur + [t])) > width:
            lines.append(cur)
            cur = []
        cur.append(t)
    if cur:
        lines.append(cur)
    out = []
    for ln in lines:
        parts, run = [], []
        for w, p in ln:
            if p:
                run.append(w)
            else:
                if run:
                    parts.append("*" + " ".join(run) + "*")
                    run = []
                parts.append(w)
        if run:
            parts.append("*" + " ".join(run) + "*")
        out.append(" ".join(parts))
    return " / ".join(out)

SRC_FRESH = ("Source: Dai, Milkman & Riis (2014), The Fresh Start Effect: Temporal Landmarks Motivate Aspirational Behavior, "
             "Management Science 60(10). University gym data: the chance of a gym visit rose 33.4% at the start of a week, "
             "14.4% at the start of a month and 7.5% after a birthday.")
SRC_MILNE = ("Sources: Milne, Orbell & Sheeran (2002), British Journal of Health Psychology 7(2), 248 people over 2 weeks: 91% of the "
             "group that wrote down day, time and place exercised, versus under 40% in the other groups. "
             "Gollwitzer & Sheeran (2006), meta-analysis of 94 tests of if-then plans, Advances in Experimental Social Psychology 38.")
SRC_WARD = ("Source: Ward, Duke, Gneezy & Bos (2017), Brain Drain: The Mere Presence of One's Own Smartphone Reduces Available "
            "Cognitive Capacity, Journal of the Association for Consumer Research 2(2). About 800 people. Phone in another room "
            "scored best, phone on the desk worst, whether it was on or off. Later replications found mixed results.")

# ================================================================== FEED (12:30)
post("lh-w2-05-restart", LH, "2026-10-18T12:30", "learning",
     dict(lay="sticky", f="pink", kicker="lock-in week · day 1/3", text="“I'll start Monday.” / *Science agrees.*", obj="clock", at="br",
          items=["Why Mondays work", "What a gym study found", "How to use tomorrow"], save="save this"),
     [dict(k="why", f="dots", label="what researchers found", text="At one university gym, / visits *jumped* / *by a third* / every Monday.",
           sub="a new week feels like a new chapter", src="Dai, Milkman & Riis, Management Science, 2014"),
      dict(k="say", f="cream", label="how to use it", text="Don't plan / a whole new life. / Plan *one hour* / for Monday. That's it."),
      dict(k="do", f="dots", text="Tonight, open your calendar / and book *one hour tomorrow* / for the thing you keep putting off.",
           save="send this to your “I'll start Monday” friend")],
     "\"I'll start Monday\" isn't just an excuse. It's a real effect, and tomorrow is Monday.\n\n"
     "Why it works: researchers tracked visits to a university gym. At the start of each week, the chance of a visit jumped by about a third. "
     "It went up at the start of each month and after birthdays too. A new week feels like a new chapter, so last week's mess feels like "
     "it belongs to the old one. They call it the fresh start effect.\n\n"
     "Do this: tonight, open your calendar and book one hour tomorrow for the thing you keep putting off. One hour, not a whole new routine.\n\n"
     "Send this to the friend who always starts on Monday.\n\n#productivity #habits #focus #freshstart #selfimprovement",
     SRC_FRESH)

post("lh-1019-one-sentence", LH, "2026-10-19T12:30", "deep",
     dict(lay="sticky", f="cream", kicker="lock-in week · day 2/3", text="One sentence got / *twice as many people* / to exercise", obj="clock", at="br",
          items=["The study", "The sentence", "Your version"], save="slide 3 has the sentence"),
     [dict(k="say", f="pink", label="the study", text="People were asked / to exercise more. / One group got / *one extra step.*",
           sub="here's what it was →"),
      dict(k="say", f="dots", label="the extra step", text="They filled in / one sentence: / “I'll exercise on *[day]* / at *[time]* in *[place].*”"),
      dict(k="say", f="cream", text="Of the people / who wrote it, / this many exercised:", num="91%", sub="the other groups? under 4 in 10",
           src="Milne, Orbell & Sheeran, British Journal of Health Psychology, 2002"),
      dict(k="why", f="pink", text="Decide *when and where* / ahead of time. / Then you just go.",
           sub="plans like this helped in 94 studies"),
      dict(k="do", f="dots", text="Fill in yours: “I'll work on ___ at ___ in ___.” Then *put it in your calendar.*",
           save="send this to your “someday” friend")],
     "One sentence more than doubled how many people exercised.\n\n"
     "Why it works: in a UK study, people were asked to exercise more for two weeks. One group also filled in a sentence: \"I'll exercise on "
     "[day] at [time] in [place].\" 91% of them exercised. In the other groups, fewer than 4 in 10 did. When you decide when and where ahead of "
     "time, there's nothing left to decide in the moment. You just go. Across 94 studies, plans like this helped people reach their goals.\n\n"
     "Do this: write one sentence for this week, \"I'll work on ___ at ___ in ___,\" and put it in your calendar.\n\n"
     "Send this to the friend who says \"I'll go when I feel like it.\"\n\n#habits #productivity #goals #focus #motivation",
     SRC_MILNE)

post("lh-1020-phone-other-room", LH, "2026-10-20T12:30", "learning",
     dict(lay="sticky", f="dots", kicker="lock-in week · day 3/3", text="Your phone is off. / It's still / *costing you.*", obj="clock", at="br",
          items=["The study", "The strange part", "The fix"], save="save this"),
     [dict(k="say", f="cream", label="the study", text="About 800 people / took tricky brain tests. / Some put their phone / *in another room.*"),
      dict(k="say", f="pink", text="Phone in another room? / *Best scores.* / Phone on the desk? / *Worst,* even switched off.",
           src="Ward, Duke, Gneezy & Bos, 2017"),
      dict(k="say", f="dots", label="the strangest part", text="Almost everyone said / their phone had / *no effect on them.*"),
      dict(k="why", f="cream", label="why it happens", text="Part of your brain / is busy *not checking* / your phone. / That's focus you lose."),
      dict(k="do", f="pink", text="Next time you work, put your phone *in another room.* Face down isn't enough.",
           save="send this to the friend who studies with their phone out")],
     "Your phone can drain your focus even when it's switched off.\n\n"
     "Why it works: in a study of about 800 people, those who left their phone in another room did best on brain tests. People with the phone "
     "on the desk did worst, even when it was face down and off. Almost everyone said the phone didn't affect them. Part of your brain stays "
     "busy not checking it, and that uses up focus. (To be fair: later studies found mixed results. Moving your phone takes ten seconds.)\n\n"
     "Do this: before your next hour of work, put your phone in another room, not just face down.\n\n"
     "Send this to the friend who studies with their phone on the desk.\n\n#focus #studytips #deepwork #productivity #phonefree",
     SRC_WARD)

# Oct 21, 12:30 · NEW · task switching (APA)
SRC_APA = ("Source: American Psychological Association, \"Multitasking: Switching costs\" (March 20, 2006): drawing on research by "
           "Rubinstein, Meyer and Evans (2001), even brief mental blocks created by shifting between tasks can cost as much as 40 percent "
           "of someone's productive time (David Meyer, University of Michigan).")

post("lh-1021-switching-cost", LH, "2026-10-21T12:30", "learning",
     dict(lay="sticky", f="pink", kicker="focus science", text="Multitasking / feels *fast.* / It isn't.", obj="clock", at="br",
          items=["What switching costs", "The 40% number", "The fix"], save="save this"),
     [dict(k="say", f="cream", label="sound familiar?", text="Email open. Chat pinging. / *Busy all morning,* / and the report / is half done."),
      dict(k="say", f="dots", text="Your brain can't do / two hard things at once. / It *switches,* / back and forth."),
      dict(k="say", f="pink", text="All that switching / can eat up to this much / of your productive time:", num="40%",
           src="American Psychological Association, Multitasking: Switching costs"),
      dict(k="why", f="cream", label="think of it like this", text="Every switch has / a little *loading screen.* / They add up fast."),
      dict(k="say", f="dots", label="the fix", text="Do *one task* at a time. / Put the small stuff, / like email, / in one block."),
      dict(k="do", f="pink", text="Tomorrow, close email and chat for your *first hour.* One task only.",
           save="send this to the friend with 30 tabs open")],
     "Multitasking feels fast. It isn't.\n\n"
     "Why it works: your brain can't really do two hard things at once. It switches back and forth, and every switch costs a little time "
     "while it gets back up to speed, like a tiny loading screen. The American Psychological Association says those switches can eat up "
     "to 40% of your productive time.\n\n"
     "Do this: tomorrow, close email and chat for your first hour and do one task only. Put the small stuff, like email, in one block later.\n\n"
     "Send this to the friend with 30 tabs open.\n\n#focus #multitasking #productivity #deepwork #worklife",
     SRC_APA)



# ================================================================== REELS (08:30 and 19:00)
reel("lh-reel-1018am-66-days", LH, "2026-10-18T08:30", "learning", "lh-x-lock-in", "save this for later", [
    dict(k="hook", f="cream", text="A habit takes / 21 days? / *Not quite.*", emo="⏰"),
    dict(k="because", f="pink", kicker="a real study", text="96 people built a new daily habit. It took *66 days* on average to feel automatic."),
    dict(k="say", f="dots", text="And missing / *one day* / didn't ruin it.", drop=True),
    dict(k="do", f="cream", text="Give your new habit *two months* before you quit on it."),
    dict(k="save", f="pink", text="Send this to the friend / who quit on day 4."),
], "A new habit doesn't take 21 days. It takes closer to two months.\n\n"
   "Why it works: researchers followed 96 people building one daily habit, like eating fruit with lunch or a short run before dinner. "
   "On average it took 66 days to feel automatic. For some people it was 18 days, for others much longer. And missing one day didn't ruin it.\n\n"
   "Do this: pick one habit today and give it two months before you decide it's not working.\n\n"
   "Send this to the friend who quit on day 4.\n\n#habits #selfimprovement #productivity #motivation #focus",
   "Source: Lally, van Jaarsveld, Potts & Wardle (2010), How are habits formed: Modelling habit formation in the real world, European "
   "Journal of Social Psychology 40(6). 96 people over 12 weeks; median 66 days to reach automaticity (range 18 to an estimated 254); "
   "missing one opportunity did not materially affect the process.")

reel("lh-reel-1018-mute-the-world", LH, "2026-10-18T19:00", "suggestion", "lh-x-phone-down", "save this for tomorrow morning", [
    dict(k="hook", f="pink", text="Busy all day, / but *nothing* / *got done?*", emo="⏳"),
    dict(k="because", f="cream", kicker="here's why", text="Every switch leaves part of your mind *on the last task.*"),
    dict(k="say", f="dots", text="It's called / *attention residue:* / like ten tabs / open in your head.", drop=True),
    dict(k="do", f="pink", text="Give *one task* one hour tomorrow. Phone in another room."),
    dict(k="save", f="cream", text="Send this to the friend / who's always “so busy.”", next="part 2 tomorrow"),
], "Busy all day, but nothing actually got done?\n\n"
   "Why it works: every time you switch tasks, part of your mind stays stuck on the last one. Researcher Sophie Leroy named it attention "
   "residue, and people with it did worse on the next task. It's like leaving ten tabs open in your head.\n\n"
   "Do this: pick tomorrow's hour right now and put it in your calendar. One task, phone in another room.\n\n"
   "Part 1 of 2. Tomorrow: which hour to pick.\n\nSend this to the friend who's always \"so busy.\"\n\n"
   "#focus #deepwork #productivity #studytips #timemanagement",
   "Source: Leroy (2009), Why is it so hard to do my work? The challenge of attention residue when switching between work tasks, "
   "Organizational Behavior and Human Decision Processes 109(2).", series="Lock one hour · part 1/2")

reel("lh-reel-1019am-pings", LH, "2026-10-19T08:30", "learning", "lh-x-tick-boom", "save this for your next busy day", [
    dict(k="hook", f="dots", text="Interruptions / don't slow you / down. *They do* / *something worse.*", emo="⏳"),
    dict(k="because", f="cream", kicker="the surprise", text="Interrupted workers finished *a bit faster.* Their work was just as good."),
    dict(k="say", f="dots", text="But their / *stress* shot up. / They were / racing the clock.", drop=True),
    dict(k="do", f="pink", text="Turn on *Do Not Disturb* for your most important hour."),
    dict(k="save", f="cream", text="Send this to the coworker / who answers every ping."),
], "Interruptions don't make you slower. They make you more stressed.\n\n"
   "Why it works: in a study led by Gloria Mark of UC Irvine, 48 people wrote work emails while being interrupted again and again. They finished a little "
   "faster than people who weren't interrupted, and their work was just as good. But their stress, frustration and effort went way up. "
   "They were racing to make up for lost time.\n\n"
   "Do this: today, turn on Do Not Disturb for one hour while you do your most important task.\n\n"
   "Send this to the coworker who answers every ping in ten seconds.\n\n#focus #worklife #productivity #stress #deepwork",
   "Source: Mark, Gudith & Klocke (2008), The cost of interrupted work: more speed and stress, Proceedings of CHI 2008. 48 participants; "
   "interrupted groups finished faster with no difference in quality, but reported higher stress, frustration, time pressure and effort.")

reel("lh-reel-1019-odd-hours", LH, "2026-10-19T19:00", "suggestion", "lh-x-lock-in", "send this to a friend on nights", [
    dict(k="hook", f="pink", text="Which hour? / *Right after* / *you wake up.*", emo="⏰"),
    dict(k="because", f="cream", kicker="here's why", text="Plans tied to something you *already do* stick better. Everyone wakes up."),
    dict(k="say", f="dots", text="So: *“After I* / *wake up, I work* / *one hour.”*", drop=True),
    dict(k="do", f="pink", text="Write that on a sticky note *by your coffee maker.*"),
    dict(k="save", f="cream", text="Send this to the friend / who works nights.", next="part 2 of 2"),
], "Which hour should you protect? The one right after you wake up, whenever that is.\n\n"
   "Why it works: plans tied to something you already do get done far more often. Across 94 studies, these \"after X, I'll do Y\" plans "
   "helped people reach their goals. And waking up happens every single day, even on night shifts.\n\n"
   "Do this: tonight, write \"After I wake up and make coffee, I work for one hour\" on a sticky note and put it on your coffee maker.\n\n"
   "Part 2 of 2.\n\nSend this to the friend who works nights.\n\n#shiftwork #nightshift #productivity #habits #focus",
   "Source: Gollwitzer & Sheeran (2006), Implementation intentions and goal achievement: a meta-analysis of effects and processes, "
   "Advances in Experimental Social Psychology 38. 94 independent tests, medium-to-large effect (d = .65).",
   series="Lock one hour · part 2/2")

reel("lh-reel-1020am-nap-time", LH, "2026-10-20T08:30", "keep", "lh-x-phone-down", "save this for the next nap", [
    dict(k="hook", f="cream", text="The baby's / finally asleep. / *Now what?*", emo="⏳"),
    dict(k="say", f="pink", text="Halfway through / a task, the / baby wakes up. / Your mind / *keeps chewing* / on it."),
    dict(k="because", f="dots", kicker="the fix", text="Researchers found a *one-minute note* helps your brain let go of it.", drop=True),
    dict(k="do", f="cream", text="When the baby wakes, write *“stopped at ___, next is ___.”*"),
    dict(k="save", f="pink", text="Send this to a friend / with a newborn."),
], "For every parent who gets interrupted halfway through everything.\n\n"
   "Why it works: when you stop a task halfway, your mind keeps chewing on it. Researchers Sophie Leroy and Theresa Glomb found that a quick "
   "note, where you stopped and what's next, helps your brain let go. People who wrote one did better on the next thing they did.\n\n"
   "Do this: next nap, keep a sticky note nearby. When the baby wakes, write \"stopped at ___, next is ___.\" It takes a minute.\n\n"
   "Send this to a friend with a newborn.\n\n#newparents #momlife #dadlife #focus #parenting",
   "Source: Leroy & Glomb (2018), Tasks interrupted: How anticipating time pressure on resumption of an interrupted task causes attention "
   "residue and low performance on interrupting tasks and how a 'ready-to-resume' plan mitigates the effects, Organization Science 29(3).")

reel("lh-reel-1020-shutdown", LH, "2026-10-20T19:00", "keep", "lh-x-lock-in", "save this for tonight", [
    dict(k="hook", f="dots", text="Lying awake, / thinking about / *tomorrow's* / *to-do list?*", emo="⏰"),
    dict(k="say", f="cream", text="In a sleep lab, / some people / wrote *tomorrow's* / *to-do list* / before bed."),
    dict(k="because", f="pink", kicker="the result", text="They fell asleep *10 minutes faster* than people who wrote about their day.", drop=True),
    dict(k="do", f="dots", text="Spend *5 minutes* writing tomorrow's list before bed tonight."),
    dict(k="save", f="cream", text="Send this to the friend / who texts you at 1 am."),
], "Lying awake thinking about tomorrow? Write it down.\n\n"
   "Why it works: in a sleep-lab study, people who spent 5 minutes writing tomorrow's to-do list fell asleep in about 15 minutes. People who "
   "wrote about what they'd already done took about 25. The more detailed the list, the faster they fell asleep. It was one small study of "
   "57 young adults, so it's a nudge, not a cure.\n\n"
   "Do this: tonight, keep paper by your bed and spend 5 minutes writing tomorrow's list.\n\n"
   "Send this to the friend who texts you at 1 am.\n\n#sleep #productivity #todolist #habits #bedtimeroutine",
   "Source: Scullin, Krueger, Ballard, Pruett & Bliwise (2018), The effects of bedtime writing on difficulty falling asleep, Journal of "
   "Experimental Psychology: General 147(1). 57 adults aged 18-30; to-do list group about 15 min to fall asleep vs about 25 min.")


# ================================================================== STORY CHAINS ("Lock-in week")
chain("lh-ch-1018", LH, "2026-10-18", "lh18", "lock-in week · day 1/3", [
    dict(k="photo", text="“I'll start / *Monday.*”", sub="turns out, that actually works →", ink="light", y=1150),
    dict(k="bubbles", f="cream", label="the fresh start effect", bubbles=[
        ("in", "wasted my whole week again"), ("out", "good news: tomorrow's Monday"),
        ("out", "in one study, gym visits jumped by *a third* every Monday"), ("in", "so Monday really is magic?")], obj="clock"),
    dict(k="payoff", f="pink", label="the trick", text="Keep it *small.* / One hour, / not a new life.", sub="tomorrow is your clean page", obj="clock"),
    dict(k="handoff", f="dots", text="Why Monday / *really works*", img="lh-w2-05-restart/01.jpg", next="day 2 tomorrow"),
])
chain("lh-ch-1019", LH, "2026-10-19", "lh19", "lock-in week · day 2/3", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="cream", label="quick quiz", title="They wrote down / *when* and *where…*", bubbles=[
        ("in", "how many actually exercised?"), ("out", "A) about 4 in 10"),
        ("out", "B) about 9 in 10")], obj="clock", tap="guess, then tap →"),
    dict(k="payoff", f="pink", label="the answer: B", text="*91%*", sub="the other groups? under 4 in 10", obj="clock",
         tap="source: Milne, Orbell & Sheeran, 2002 · tap →"),
    dict(k="payoff", f="dots", label="why it matters", text="Decide *when* / and *where.*", sub="then there's nothing left to decide",
         obj="hourglass", tap="next story →"),
    dict(k="handoff", f="dots", text="The sentence / *that works*", img="lh-1019-one-sentence/01.jpg", next="day 3 tomorrow"),
])
chain("lh-ch-1020", LH, "2026-10-20", "lh20", "lock-in week · day 3/3", [
    dict(k="photo", text="“My phone's off. / *It's fine.*”", sub="it's not →", ink="dark", y=1300),
    dict(k="bubbles", f="cream", label="a real study", bubbles=[
        ("in", "my phone's face down. it's fine"), ("out", "a study of 800 people says no"),
        ("out", "a phone *on the desk* lowered scores, even when off"), ("in", "wait, what?")], obj="hourglass"),
    dict(k="payoff", f="pink", label="what worked best", text="Phone in / *another room.*", sub="not face down. not on silent. gone.", obj="clock"),
    dict(k="handoff", f="dots", text="Your phone is / *still costing you*", img="lh-1020-phone-other-room/01.jpg", next="lock-in week · done"),
])

# Oct 21 · NEW · day B: guess-and-reveal quiz -> lh-1021-switching-cost
chain("lh-ch-1021", LH, "2026-10-21", "lh21", "focus science", [
    dict(k="bubbles", f="cream", label="quick quiz", title="Switching tasks / *all day…*", bubbles=[
        ("in", "how much of your productive time can it cost?"), ("out", "A) about 5%"), ("out", "B) up to 40%")],
         obj="clock", tap="guess, then tap →"),
    dict(k="payoff", f="pink", label="the answer: B", text="Up to / *40%*", sub="of your productive time", obj="clock",
         tap="source: American Psychological Association · tap →"),
    dict(k="payoff", f="dots", label="why it matters", text="Busy isn't / *done.*", sub="every switch costs a little time",
         obj="hourglass", tap="next story →"),
    dict(k="handoff", f="dots", text="Multitasking / feels *fast.*", img="lh-1021-switching-cost/01.jpg", next="save it for tomorrow"),
])


# ------------------------------------------------------------------ AIR PASS (Oct 18 am): rewrap lines over 19 characters.
def _fit_sizes(brand, em=0.33, cap=160, floor=88):
    """AIR PASS: keep the hand-written line breaks and pick each slide's size so its longest line fits the 920px text box
    (em = average glyph width for this page's serif) and all its lines fit the box height. Then nothing re-wraps.
    Oct 19-21 feed slides only."""
    import re as _re
    from specs_teach import POSTS, META

    def _len(s):
        return len(_re.sub(r"\*", "", s)) + 2 * len(_re.findall(r"[\U0001F300-\U0001FAFF]", s))

    for _pid, _sp in POSTS.items():
        if _sp["brand"] != brand or META[_pid]["at"][:10] not in ("2026-10-19", "2026-10-20", "2026-10-21"):
            continue
        for _s in _sp["slides"]:
            if _s.get("k") in ("do", "rows", "steps"):
                continue
            lines = _s["text"].split(" / ")
            box_h = 430 if (_s.get("num") or _s.get("bars")) else 540
            w = 900 / (em * max(_len(x) for x in lines))
            h = box_h / (0.9 * len(lines))
            _s["size"] = int(max(floor, min(cap, w, h)))



_fit_sizes(LH)

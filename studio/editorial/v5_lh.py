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
          items=["The sentence", "The result", "Your version"], save="slide 2 has the sentence"),
     [dict(k="say", f="pink", label="the study", text="People were asked / to exercise more. / One group also / filled in *one sentence:*",
           sub="“I'll exercise on [day] at [time] in [place].”"),
      dict(k="say", f="cream", label="the result", text="Of the people / who wrote it, / this many exercised:", num="91%",
           sub="the other groups? under 4 in 10", src="Milne, Orbell & Sheeran, British Journal of Health Psychology, 2002"),
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
     [dict(k="say", f="cream", label="about 800 people, tricky brain tests",
           text="Phone in another room? / *Best scores.* / Phone on the desk? / *Worst,* even switched off.",
           src="Ward, Duke, Gneezy & Bos, 2017"),
      dict(k="say", f="dots", label="the strangest part", text="Almost everyone said / their phone had / *no effect on them.*",
           sub="but part of your brain is busy not checking it"),
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
     [dict(k="say", f="cream", label="sound familiar?", text="Email open. Chat pinging. / *Busy all morning,* / and the report / is half done.",
           sub="your brain isn't multitasking. it's switching."),
      dict(k="say", f="dots", text="Every switch has / a little *loading screen.* / They can eat up to:", num="40%",
           sub="of your productive time", src="American Psychological Association, Multitasking: Switching costs"),
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


# ================================================================== Oct 22 (Story chain day)
SRC_BUNDLE = ("Source: Milkman, Minson & Volpp (2014), Holding the Hunger Games hostage at the gym: an evaluation of temptation bundling, "
              "Management Science 60(2). Participants who could only listen to tempting audiobooks at the gym initially visited the gym "
              "51% more often than the control group; the effect faded after the Thanksgiving break.")
SRC_WALK = ("Source: Oppezzo & Schwartz (2014), Give your ideas some legs: the positive effect of walking on creative thinking, Journal "
            "of Experimental Psychology: Learning, Memory, and Cognition 40(4). Stanford News (April 24, 2014): creative output rose by "
            "an average of 60% when people walked; walking on a treadmill facing a blank wall worked too.")

reel("lh-reel-1022am-bundle", LH, "2026-10-22T08:30", "learning", "lh-x-tick-boom", "save this for your next skipped workout", [
    dict(k="hook", f="cream", text="Can't make / yourself go / *to the gym?*", emo="🎧"),
    dict(k="say", f="pink", text="People could play / gripping audiobooks, / but *only at the gym.*"),
    dict(k="because", f="dots", kicker="the result", text="At first, they went to the gym *51% more often.*", drop=True),
    dict(k="say", f="cream", text="It's called / *temptation* / *bundling.*"),
    dict(k="do", f="pink", text="Save your favourite show for *the chore you avoid.*"),
    dict(k="save", f="cream", text="Send this to the friend / who skips the gym."),
], "Can't make yourself go to the gym? Make the gym the only place you get your favourite thing.\n\n"
   "Why it works: researchers at Wharton let people listen to gripping audiobooks, but only at the gym. At first, they went 51% more "
   "often than people with no deal. It's called temptation bundling: you pair something you want with something you keep putting off. "
   "The honest part: the boost faded after a holiday break, so restart it when life gets busy.\n\n"
   "Do this: pick one show or podcast you love, and only play it during the chore you avoid, like the treadmill or folding laundry.\n\n"
   "Send this to the friend who keeps skipping the gym.\n\n#habits #motivation #gymmotivation #productivity #behaviorchange",
   SRC_BUNDLE)

reel("lh-reel-1022-walk", LH, "2026-10-22T19:00", "suggestion", "lh-x-lock-in", "save this for the next time you're stuck", [
    dict(k="hook", f="pink", text="Stuck on / a problem? / *Stand up.*", emo="🚶"),
    dict(k="say", f="cream", text="Stanford tested / people's ideas, / *sitting* vs / *walking.*"),
    dict(k="because", f="dots", kicker="the result", text="Walking raised creative ideas by about *60%* on average.", drop=True),
    dict(k="say", f="pink", text="It even worked / on a treadmill / *facing a wall.*"),
    dict(k="do", f="cream", text="Next time you're stuck, take a *10-minute walk.* No phone."),
    dict(k="save", f="pink", text="Send this to the friend / glued to their desk."),
], "Stuck on a problem? Stand up.\n\n"
   "Why it works: Stanford researchers tested people's ideas while they sat and while they walked. Walking raised creative output by "
   "about 60% on average. It even worked on a treadmill facing a blank wall, so it's the walking itself, not the view.\n\n"
   "Do this: next time you're stuck, take a 10-minute walk. Bring the problem with you, and leave your phone behind.\n\n"
   "Send this to the friend stuck at their desk all day.\n\n#creativity #focus #productivity #walking #worklife",
   SRC_WALK)


SRC_SIX = ("Sources: Van Dongen, Maislin, Mullington & Dinges (2003), The cumulative cost of additional wakefulness, Sleep 26(2): "
           "restricting sleep to 6 hours a night for 14 days produced cognitive deficits equivalent to up to 2 nights of total sleep "
           "deprivation, while people rated themselves only slightly sleepy. Canadian 24-Hour Movement Guidelines for Adults (CSEP, "
           "2020): adults 18-64 should get 7 to 9 hours of good-quality sleep on a regular basis.")

post("lh-1022-six-hours", LH, "2026-10-22T12:30", "learning",
     dict(lay="sticky", f="pink", kicker="focus science", text="6 hours of sleep / *feels* fine.", obj="clock", at="br",
          items=["What 2 weeks did", "Why you can't tell", "The fix"], save="save this"),
     [dict(k="say", f="cream", label="a real sleep-lab study", text="People slept / *6 hours* a night / for two weeks.",
           sub="their focus got worse every day"),
      dict(k="say", f="dots", text="By day 14, focus / was as bad as / *1 to 2 nights* / with no sleep.",
           sub="and they barely felt sleepier", src="Van Dongen et al., Sleep, 2003"),
      dict(k="do", f="pink", text="Tonight, set a *bedtime alarm* 8 hours before your wake-up alarm.",
           save="send this to the friend who “runs on 6 hours”")],
     "6 hours of sleep feels fine. Your brain disagrees.\n\n"
     "Why it works: in a sleep-lab study, people slept 6 hours a night for two weeks. Their focus got worse every single day. By day 14, "
     "it was as bad as going 1 to 2 nights with no sleep at all. The scary part: they only felt a little sleepier, so they couldn't tell.\n\n"
     "Canada's sleep guidelines say adults need 7 to 9 hours.\n\n"
     "Do this: tonight, set a bedtime alarm 8 hours before your wake-up alarm. When it rings, start winding down.\n\n"
     "Send this to the friend who \"runs on 6 hours.\"\n\n#sleep #focus #productivity #sleepdeprivation #healthyhabits",
     SRC_SIX)

chain("lh-ch-1022", LH, "2026-10-22", "lh22", "focus science", [
    dict(k="photo", text="“I'm fine / on *6 hours.*”", sub="your brain *disagrees* →", ink="dark", y=560),
    dict(k="bubbles", f="cream", label="sound familiar?", bubbles=[
        ("in", "6 hours again. feel fine though"), ("out", "a sleep lab tested that"),
        ("out", "after 2 weeks, focus was like *1 to 2 nights with no sleep*"), ("in", "but I don't feel tired?")], obj="clock"),
    dict(k="payoff", f="pink", label="the scary part", text="You *can't feel* / the damage.", sub="they felt only a little sleepier",
         obj="hourglass"),
    dict(k="handoff", f="dots", text="6 hours of sleep / *feels* fine.", img="lh-1022-six-hours/01.jpg", next="save it for bedtime"),
])


# ================================================================== Oct 23 (day B: quiz)
SRC_GREEN = ("Source: Lee, Williams, Sargent, Williams & Johnson (2015), 40-second green roof views sustain attention: the role of "
             "micro-breaks in attention restoration, Journal of Environmental Psychology 42. During a sustained-attention task, people "
             "who looked at a flowering green roof for 40 seconds made fewer errors afterwards than people who looked at a concrete roof.")
SRC_CAFF = ("Source: Drake, Roehrs, Shambroom & Roth (2013), Caffeine effects on sleep taken 0, 3, or 6 hours before going to bed, "
            "Journal of Clinical Sleep Medicine 9(11). 400 mg of caffeine (about 2 to 3 cups of coffee, per the AASM summary) taken 6 "
            "hours before bed reduced objectively measured total sleep by more than 1 hour; participants didn't report the disruption.")

post("lh-1023-green-break", LH, "2026-10-23T12:30", "learning",
     dict(lay="sticky", f="dots", kicker="focus science", text="A *40-second* / break that / works.", obj="clock", at="br",
          items=["The green roof study", "What changed", "The fix"], save="save this"),
     [dict(k="say", f="cream", label="a real study", text="Tired people took / a *40-second* break / to look at a roof.",
           sub="some saw a green roof. some saw concrete."),
      dict(k="say", f="pink", text="The *green roof* / group made / fewer mistakes / afterwards.",
           sub="green gives tired attention a rest", src="Lee et al., Journal of Environmental Psychology, 2015"),
      dict(k="do", f="dots", text="Between tasks today, look at *trees or plants* for 40 seconds. Not your phone.",
           save="send this to the friend who scrolls on breaks")],
     "A 40-second break that actually works.\n\n"
     "Why it works: in a study at the University of Melbourne, people doing a long, boring focus task took a 40-second break to look at "
     "a roof. Some saw a roof covered in green plants, some saw plain concrete. The green-roof group made fewer mistakes afterwards. "
     "Green gives tired attention a short rest. Scrolling doesn't.\n\n"
     "Do this: between tasks today, look out a window at trees or plants for 40 seconds. Leave your phone face down.\n\n"
     "Send this to the friend who scrolls on every break.\n\n#focus #productivity #breaks #nature #worklife",
     SRC_GREEN)

chain("lh-ch-1023", LH, "2026-10-23", "lh22", "focus science", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="cream", label="quick quiz", title="A break that / *helps focus…*", bubbles=[
        ("in", "how long did they look at a green roof?"), ("out", "A) 40 seconds"), ("out", "B) 10 minutes")],
         obj="clock", tap="guess, then tap →"),
    dict(k="payoff", f="pink", label="the answer: A", text="*40* / seconds", sub="and they made fewer mistakes after", obj="clock",
         tap="source: Lee et al., 2015 · tap →"),
    dict(k="payoff", f="dots", label="why it matters", text="Look at *green,* / not your phone.", sub="a real rest for tired focus",
         obj="hourglass", tap="next story →"),
    dict(k="handoff", f="dots", text="A *40-second* / break that works.", img="lh-1023-green-break/01.jpg", next="save it for your next break"),
])

reel("lh-reel-1023-caffeine", LH, "2026-10-23T19:00", "keep", "lh-x-phone-down", "save this for your afternoon coffee", [
    dict(k="hook", f="dots", text="Coffee at 4 pm? / *Your sleep* / *noticed.*", emo="☕"),
    dict(k="say", f="cream", text="In a sleep study, / people had caffeine / *6 hours* before bed."),
    dict(k="because", f="pink", kicker="the result", text="They slept *over an hour less.* They didn't notice.", drop=True),
    dict(k="say", f="dots", text="About *2 to 3* / *cups* of coffee."),
    dict(k="do", f="cream", text="Have your last coffee *at least 6 hours* before bed."),
    dict(k="save", f="pink", text="Send this to / your coffee friend."),
], "Coffee at 4 pm? Your sleep noticed.\n\n"
   "Why it works: in a sleep study, people had 400 mg of caffeine, about 2 to 3 cups of coffee, 6 hours before bed. They slept more "
   "than an hour less, measured in the lab, and they didn't even notice it.\n\n"
   "Do this: have your last coffee at least 6 hours before bed. Going to bed at 10? Last cup by 4, earlier if you can.\n\n"
   "Send this to the friend on their 4th coffee.\n\n#sleep #caffeine #coffee #focus #healthyhabits",
   SRC_CAFF)


# ================================================================== Oct 24 (Story chain day; 12:30 = lh-1024-reveal-47-seconds in v5_formats)
# Facts checked Oct 18 pm. Avoided: Ariely & Wertenbroch 2002 (deadlines) - retracted in 2026 for data problems.
SRC_FLOSS = ("Source: Judah, Gardner & Aunger (2013), Forming a flossing habit: an exploratory study of the psychological determinants "
             "of habit formation, British Journal of Health Psychology 18(2). 50 people were randomly asked to floss before or after "
             "brushing; the after-brushing group built stronger flossing habits (automaticity), and still did at 8 months.")
SRC_LYRICS = ("Source: Perham & Currie (2014), Does listening to preferred music improve reading comprehension performance?, Applied "
              "Cognitive Psychology 28(2). 30 students read and answered questions in quiet, with instrumental music, or with lyrical "
              "music they liked or disliked. Lyrical music, liked or not, gave significantly worse scores than quiet; instrumental "
              "music was not significantly different from quiet. A small study.")
SRC_MARK = ("Source: Gloria Mark (UC Irvine), Attention Span (2023), and UC Newsroom (2024), 'How to sharpen your attention': attention "
            "on a single screen averaged about two and a half minutes in her 2004 study (2003 data) and 47 seconds in studies from "
            "2016 to 2020.")

reel("lh-reel-1024am-floss-after", LH, "2026-10-24T08:30", "learning", "lh-x-tick-boom", "save this for your next new habit", [
    dict(k="hook", f="cream", text="Floss *before* / or *after* / brushing?", emo="🪥"),
    dict(k="say", f="pink", text="Researchers asked / 50 people to floss, / *before* or *after* / brushing."),
    dict(k="because", f="dots", kicker="the result", text="The *after* group built the stronger habit. Still true 8 months later.",
         drop=True),
    dict(k="say", f="cream", text="Brushing became / the *reminder.*"),
    dict(k="do", f="pink", text="Tonight, floss *right after* you brush. Same spot, every night."),
    dict(k="save", f="cream", text="Send this to the friend / who never flosses."),
], "Floss before or after brushing? For building the habit, it matters.\n\n"
   "Why it works: researchers asked 50 people to floss every day, either just before or just after brushing. The \"after\" group built "
   "the stronger habit, and they still had it 8 months later. Brushing became the reminder for flossing. It's called habit stacking: "
   "you hang a new habit on one you already do.\n\n"
   "Do this: tonight, floss right after you brush. Same spot, every night. Then try the same trick with any habit you keep forgetting.\n\n"
   "Send this to the friend who never flosses.\n\n#habits #habitstacking #selfimprovement #productivity #behaviorchange",
   SRC_FLOSS)

chain("lh-ch-1024", LH, "2026-10-24", "lh18", "focus science", [
    dict(k="photo", text="“I'll just check / *one thing.*”", sub="45 minutes later… →", ink="light", y=1150),
    dict(k="bubbles", f="cream", label="sound familiar?", bubbles=[
        ("in", "opened my laptop to send *one email*"), ("out", "and?"), ("in", "45 min later I'm on *tab 14*")]),
    dict(k="bubbles", f="pink", label="the research", bubbles=[
        ("out", "a researcher timed how long we stay on *one screen*"), ("out", "in 2004: about *2.5 minutes*"),
        ("in", "and now??")], obj="clock"),
    dict(k="payoff", f="dots", label="guess first", text="It's *way* / shorter.", sub="the answer is in today's post", obj="hourglass"),
    dict(k="handoff", f="dots", text="*2.5 minutes* / then. Now?", img="lh-1024-reveal-47-seconds/01.jpg", next="swipe to reveal"),
])

reel("lh-reel-1024-lyrics", LH, "2026-10-24T19:00", "suggestion", "lh-x-lock-in", "save this for your next study session", [
    dict(k="hook", f="pink", text="Studying with / *your playlist* / on?", emo="🎧"),
    dict(k="say", f="cream", text="Researchers tested / reading while / people listened / to music."),
    dict(k="because", f="dots", kicker="the result", text="Songs *with words* lowered scores. Even songs people *liked.*", drop=True),
    dict(k="say", f="pink", text="Music *without* / words did about / as well as *quiet.*"),
    dict(k="do", f="cream", text="For your next focus hour, switch to music *without words,* or none."),
    dict(k="save", f="pink", text="Send this to / your study buddy."),
], "Studying with your playlist on? Check the words.\n\n"
   "Why it works: in a study, students read and answered questions in quiet, with instrumental music, or with songs with lyrics. "
   "Songs with words lowered their scores, even songs they liked. Music without words did about as well as quiet. Your brain tries to "
   "follow the lyrics and the page at the same time.\n\n"
   "The honest part: it was a small study (30 students), about reading. But it's an easy switch.\n\n"
   "Do this: for your next focus hour, switch to music without words, or none.\n\n"
   "Send this to your study buddy.\n\n#studytips #focus #studymusic #productivity #deepwork",
   SRC_LYRICS)


# ================================================================== Oct 25 (day B: quiz · Reels carry the planning lesson, part 1 -> 2)
SRC_PLAN = ("Source: Buehler, Griffin & Ross (1994), Exploring the 'planning fallacy': why people underestimate their task completion "
            "times, Journal of Personality and Social Psychology 67(3). 37 students predicted their senior thesis would take 33.9 days "
            "on average (48.6 days if everything went as poorly as possible); it took 55.5 days. About 30% finished in the time "
            "they predicted.")
SRC_UNPACK = ("Sources: Kruger & Evans (2004), If you don't want to be late, enumerate: unpacking reduces the planning fallacy, Journal "
              "of Experimental Social Psychology 40. Listing a task's parts before predicting led to longer, less optimistic estimates; "
              "it works less well for tasks with few parts (as summarised by Wiese, Buehler & Griffin, 2016, Judgment and Decision Making).")
SRC_PROGRESS = ("Source: Amabile & Kramer, The Progress Principle (Harvard Business Review Press, 2011) and HBS Working Knowledge: "
                "238 people at 7 companies filled in about 12,000 daily diaries; making progress in meaningful work, even a small win, "
                "was by far the most common event on people's best days, and setbacks on their worst.")

reel("lh-reel-1025am-planning-fallacy", LH, "2026-10-25T08:30", "learning", "lh-x-tick-boom", "save this before you plan your week", [
    dict(k="hook", f="dots", text="Why does / *everything* / take longer?", emo="⏳"),
    dict(k="say", f="cream", text="Students guessed / their thesis would / take *34 days.*"),
    dict(k="because", f="pink", kicker="the result", text="It took *56 days.* Even their worst case was too short.", drop=True),
    dict(k="say", f="dots", text="It's called the / *planning fallacy.*"),
    dict(k="do", f="cream", text="Today, add *half again* to your next time guess."),
    dict(k="save", f="pink", text="Send this to / your “quick” friend.", next="part 2 tonight: the fix"),
], "Why does everything take longer than you think?\n\n"
   "Why it happens: students guessed their thesis would take 34 days. It took 56, on average. Even their worst-case guess, 49 days, "
   "was too short. It's called the planning fallacy: we picture the day where everything goes right, not a real one.\n\n"
   "Do this: today, add half again to your next time guess. Think 2 hours? Plan 3.\n\n"
   "Send this to the friend who says \"it'll be quick.\" Part 2 tonight at 7: the fix that's backed by research.\n\n"
   "#planning #productivity #timemanagement #focus #procrastination",
   SRC_PLAN, series="Planning · part 1/2")

chain("lh-ch-1025", LH, "2026-10-25", "lh22", "focus science", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="cream", label="quick quiz", title="On people's / *best* work days…", bubbles=[
        ("in", "what mattered most?"), ("out", "A) praise from the boss"), ("out", "B) making *progress*")],
         obj="clock", tap="guess, then tap →"),
    dict(k="payoff", f="pink", label="the answer: B", text="*Progress*", sub="even a small win", obj="clock",
         tap="source: Amabile & Kramer, 12,000 diaries · tap →"),
    dict(k="payoff", f="dots", label="why it matters", text="Seeing it / *keeps you going.*", sub="so write it down",
         obj="hourglass", tap="next story →"),
    dict(k="handoff", f="dots", text="Felt like you / did *nothing?*", img="lh-1025-done-list/01.jpg", next="save it for Friday"),
])

post("lh-1025-done-list", LH, "2026-10-25T12:30", "learning",
     dict(lay="sticky", f="cream", kicker="focus science", text="Felt like you / did *nothing* / this week?", obj="clock", at="br",
          items=["The diary study", "What mattered most", "The fix"], save="save this"),
     [dict(k="say", f="pink", label="a real study", text="238 people wrote / a *work diary* / every day. About / *12,000* entries."),
      dict(k="say", f="dots", text="Their best days / had one thing / in common: / *progress.*", sub="even a small win counted",
           src="Amabile & Kramer, The Progress Principle, 2011"),
      dict(k="do", f="cream", text="Tonight, write down *3 things you finished* this week. Small ones count.",
           save="send this to the friend who feels behind")],
     "Felt like you did nothing this week? You probably did more than you think.\n\n"
     "Why it works: Harvard researchers had 238 people write a short diary every workday, about 12,000 entries in all. On people's "
     "best days, one thing showed up far more than anything else: making progress on work that mattered, even a small win. On their "
     "worst days: setbacks. A to-do list only shows what's left. A done list shows the progress.\n\n"
     "Do this: tonight, write down 3 things you finished this week. Small ones count. Then do it every Friday.\n\n"
     "Send this to the friend who feels behind.\n\n#productivity #motivation #worklife #focus #smallwins",
     SRC_PROGRESS)

reel("lh-reel-1025-unpack", LH, "2026-10-25T19:00", "suggestion", "lh-x-lock-in", "save this for Monday", [
    dict(k="hook", f="cream", text="Your *“quick”* task / isn't quick.", emo="📝"),
    dict(k="say", f="pink", text="Before you guess / how long, *list* / *every step.*"),
    dict(k="because", f="dots", kicker="the research", text="People who *listed the steps* guessed more realistic times.",
         drop=True),
    dict(k="say", f="cream", text="Best for tasks / with *lots of parts.*"),
    dict(k="do", f="pink", text="Tonight, write the *steps* of Monday's biggest task. Then guess the time."),
    dict(k="save", f="cream", text="Send this to / your Monday / planner friend.", next="planning · part 2/2"),
], "Your \"quick\" task isn't quick. Here's the fix.\n\n"
   "Why it works: in a study, people who listed every step of a task before guessing how long it would take made longer, more "
   "realistic guesses. Hidden steps are where the time goes. It works best for tasks with lots of parts, like moving, a report, "
   "or getting the kids out the door.\n\n"
   "Do this: tonight, take Monday's biggest task, write down its steps, then guess the time.\n\n"
   "Send this to your Monday planner friend. Part 2 of 2.\n\n#planning #productivity #timemanagement #focus #mondaymotivation",
   SRC_UNPACK, series="Planning · part 2/2")


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
        if _sp["brand"] != brand or META[_pid]["at"][:10] not in ("2026-10-19", "2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23", "2026-10-25"):
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

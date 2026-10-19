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
SRC_LALLY = ("Lally, van Jaarsveld, Potts & Wardle (2010), How are habits formed, European Journal of Social Psychology 40(6): "
             "96 people, median 66 days to automaticity (range 18 to an estimated 254); missing one opportunity did not materially "
             "affect the process.")
SRC_WARD = ("Source: Ward, Duke, Gneezy & Bos (2017), Brain Drain: The Mere Presence of One's Own Smartphone Reduces Available "
            "Cognitive Capacity, Journal of the Association for Consumer Research 2(2). About 800 people. Phone in another room "
            "scored best, phone on the desk worst, whether it was on or off. Later replications found mixed results.")

# ================================================================== FEED (12:30)
post("lh-w2-05-restart", LH, "2026-10-18T12:30", "learning",
     dict(lay="sticky", f="pink", kicker="lock-in week · day 1/3", text="“I'll start Monday.” / *Science agrees.*", obj="clock", at="br",
          items=["Why Mondays work", "What a gym study found", "How to use tomorrow"], save="save this"),
     [dict(k="say", f="cream", label="sound familiar?", text="You planned a great week. / By Wednesday, it was *gone.* / Now you're waiting / for Monday.",
           sub="turns out, that's not lazy →"),
      dict(k="why", f="dots", label="what researchers found", text="At one university gym, / visits *jumped by a third* / every Monday.",
           sub="it went up after birthdays, too", src="Dai, Milkman & Riis, Management Science, 2014"),
      dict(k="say", f="pink", label="why it happens", text="A new week feels like / *a new chapter.* / Last week's mess / belongs to the old one.",
           sub="it's called the fresh start effect"),
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

# DEPTH rewrite (Oct 18, 22:00): the full method (the study, the exact sentence, how to make it specific, plan B for bad
# days, the 94-study backing) and the rule that stays: "Decide once. Then just go."
post("lh-1019-one-sentence", LH, "2026-10-19T12:30", "deep",
     dict(lay="sticky", f="cream", kicker="lock-in week · day 2/3", text="One sentence got / *twice as many people* / to exercise", obj="clock", at="br",
          items=["The study", "The sentence", "Your version", "Plan B"], save="swipe for it"),
     [dict(k="say", f="pink", label="the study", text="248 UK students / were asked to exercise more. / One group got / *one extra step.*",
           sub="here's what it was →"),
      dict(k="say", f="dots", label="the extra step", text="They filled in / one sentence: / “I'll exercise on *[day]* / at *[time]* in *[place].*”",
           sub="no pep talk. just that."),
      dict(k="say", f="cream", text="Two weeks later, / of the people / who wrote it:", num="91%", sub="the other groups? under 4 in 10",
           src="Milne, Orbell & Sheeran, British Journal of Health Psychology, 2002"),
      dict(k="why", f="pink", text="You decide *once,* / ahead of time. / When the moment comes, / you *just go.*",
           sub="no new decision to fight. it held across 94 tests.", src="Gollwitzer & Sheeran, 2006"),
      dict(k="steps", f="dots", text="Write yours / *like this*",
           items=["Pick ONE task", "Name the exact time and place", "Copy it into your calendar"]),
      dict(k="say", f="cream", label="make it specific", text="Not *“I'll study* / *this week.”* / Try: *“Tuesday, 7 pm,* / *kitchen table,* / *chapter 4.”*",
           sub="vague plans don't fire"),
      dict(k="say", f="pink", label="plan B for bad days", text="Add one if-then: / *“If I'm too tired at 7,* / *I'll do just* / *10 minutes.”*",
           sub="a small win still counts"),
      dict(k="say", f="dots", label="picture this", text="Day 1: you *just go.* / Week 1: no more arguing. / Day 66: *autopilot.* / Year 1: *250 hours* done.",
           src="Lally et al., 2010: 66 days on average", sub="decide once. then just go."),
      dict(k="do", f="cream", text="Tonight, write: “I'll work on ___ on ___ at ___ in ___.” Put it in your calendar *with an alarm.*",
           save="send this to your “someday” friend")],
     "One sentence more than doubled how many people exercised. Here's the sentence, and how to write yours.\n\n"
     "THE STUDY: 248 students in the UK were asked to exercise more over two weeks. One group did one extra thing: they filled in a sentence, "
     "\"I'll exercise on [day] at [time] in [place].\" Two weeks later, 91% of them had exercised. In the other groups, fewer than 4 in 10 had.\n\n"
     "WHY IT WORKS: you make the decision once, ahead of time. When Tuesday at 7 comes, there's nothing to decide and nothing to argue with. "
     "The time and place become the trigger, so you just go. Researchers call these if-then plans, and across 94 tests they clearly helped "
     "people reach their goals.\n\n"
     "HOW TO WRITE YOURS:\n"
     "1. Pick ONE task. Not \"get my life together\". \"Chapter 4\" or \"the budget sheet\".\n"
     "2. Name the exact time: \"Tuesday, 7 pm\", not \"this week\".\n"
     "3. Name the exact place: \"kitchen table\", not \"at home\".\n"
     "4. Put it in your calendar with an alarm, using the same words.\n\n"
     "PLAN B FOR BAD DAYS: add one more if-then for the thing that usually stops you. \"If I'm too tired at 7, I'll do just 10 minutes.\" "
     "\"If the kids are still up, I'll start at 8:30.\" A small win still counts, and it keeps the habit alive.\n\n"
     "The rule that stays: decide once, then just go.\n\n"
     "WHAT TO EXPECT: the first week, you still have to remember. Then the time and place start doing the remembering for you. "
     "In a study of 96 people building a daily habit, it took about 66 days on average to feel automatic (anywhere from 18 to 254). "
     "Missing one day didn't undo it.\n\n"
     "PICTURE A YEAR FROM NOW: one locked hour, five days a week, is about 250 hours. That's more than six full work weeks spent on "
     "the thing you kept saying you'd get to.\n\n"
     "(This is the idea Atomic Habits calls an implementation intention. Same science, your sentence.)\n\n"
     "Do this: tonight, write \"I'll work on ___ on ___ at ___ in ___,\" and put it in your calendar with an alarm.\n\n"
     "Send this to the friend who says \"I'll go when I feel like it.\"\n\n#habits #productivity #goals #focus #motivation",
     SRC_MILNE + " " + SRC_LALLY)

# DEPTH rewrite (Oct 19, 00:40): the owner's own "not enough" example done properly. The study LOUD (brain drain, bag only
# halfway), then the full method: notifications first, what to text people, which room, the first minutes of the urge
# (Indistractable's 10-minute rule), the 2FA problem, the after-picture. Rule that stays: "Out of sight isn't enough. Out of reach."
post("lh-1020-phone-other-room", LH, "2026-10-20T12:30", "deep",
     dict(lay="sticky", f="dots", kicker="lock-in week · day 3/3", text="Your phone is off. / It's still / *costing you.*", obj="clock", at="br",
          items=["The study", "The setup", "The urge", "The 2FA problem"], save="swipe for it"),
     [dict(k="say", f="cream", label="the study", text="About 800 people / took tough brain tests. / Their phones were / *on the desk,* *in a bag,* / or *in another room.*"),
      dict(k="say", f="pink", label="the scores", text="Another room: *best.* / In a bag: *in between.* / On the desk: *worst.*",
           sub="even face down. even switched off.", src="Ward, Duke, Gneezy & Bos, 2017"),
      dict(k="why", f="dots", label="why it happens", text="Part of your brain / is busy *not checking it.* / That's focus / you don't get back.",
           sub="people didn't feel a thing"),
      dict(k="steps", f="pink", text="Before / *the hour*",
           items=["Do Not Disturb on", "Text: “Urgent? Call twice.”", "Phone into another room"]),
      dict(k="say", f="dots", label="which room?", text="Not your bag. / Not a drawer *in reach.* / A room you have / to *get up and walk to.*",
           sub="a bag is only halfway"),
      dict(k="say", f="cream", label="when the urge hits", text="Don't fight it. / Write the thought down. / Then *wait 10 minutes.* / Most urges *pass.*",
           sub="idea from Indistractable"),
      dict(k="say", f="pink", label="need it for 2FA?", text="Sign in to everything / *before* the hour. / Code mid-hour? Walk, / type it, *walk it back.*",
           sub="the walk is the point"),
      dict(k="say", f="cream", label="picture this", text="Day 1: you reach / for a *missing phone.* / Week 1: *5 locked hours.* / Year 1: *250 hours.*",
           sub="the rule: out of reach."),
      dict(k="do", f="dots", text="Tomorrow: Do Not Disturb on, phone in *another room,* timer for one hour.",
           save="send this to the friend who studies with their phone out")],
     "Your phone can drain your focus even when it's switched off. Here's the full method, not just \"put it away\".\n\n"
     "THE STUDY: about 800 people took tough brain tests. Some had their phone on the desk, some in a "
     "pocket or bag, some in another room. Another room: best scores. Desk: worst, even face down and switched off. The bag was in between.\n\n"
     "WHY, AND THIS IS THE SURPRISE: part of your brain stays busy NOT checking the phone, and that uses up focus you need for the task. "
     "The researchers called it brain drain. The scary part: people said the phone barely crossed their mind. You can't feel this one.\n\n"
     "THE SETUP (2 minutes, before the hour):\n"
     "1. Turn on Do Not Disturb.\n"
     "2. Text the people who matter, once: \"My phone's in the other room 9 to 10 most days. If it's urgent, call twice.\" "
     "(Turn on repeated calls so a second call rings through.)\n"
     "3. Put it in a room you'd have to stand up and walk to. Not your bag, not a drawer by your knee. Out of sight isn't enough. Out of reach is.\n"
     "4. Set a timer on a laptop, oven or watch for one hour.\n\n"
     "WHEN THE URGE HITS (it will, usually in the first few minutes): don't fight it and don't obey it. Write the thought on paper "
     "(\"check the parcel\"), then wait 10 minutes. Nir Eyal's Indistractable calls this the 10-minute rule. Urges rise and fall like "
     "a wave, and most are gone before the 10 minutes are up.\n\n"
     "NEED IT FOR A 2FA CODE? Sign in to everything you'll need before the hour starts. If a code still comes, walk to it, type the code, "
     "and walk it back. The walk is the point: it turns a reflex into a decision.\n\n"
     "WHAT CHANGES: Day 1, you'll reach for a phone that isn't there. Week 1, five locked hours, each one done. Same time and place: "
     "in one study, daily habits took about 66 days on average to feel automatic. A year from now, that's "
     "about 250 hours of your best focus.\n\n"
     "Honest note: later studies found mixed results. Moving your phone still takes ten seconds.\n\n"
     "The rule that stays: out of sight isn't enough. Out of reach.\n\n"
     "Do this: tomorrow, Do Not Disturb on, phone in another room, timer for one hour.\n\n"
     "Send this to the friend who studies with their phone on the desk.\n\n#focus #studytips #deepwork #productivity #phonefree",
     SRC_WARD + " Eyal, N. (2019), Indistractable, the 10-minute rule for internal triggers. " + SRC_LALLY)

# Oct 21, 12:30 · NEW · task switching (APA)
SRC_APA = ("Source: American Psychological Association, \"Multitasking: Switching costs\" (March 20, 2006): drawing on research by "
           "Rubinstein, Meyer and Evans (2001), even brief mental blocks created by shifting between tasks can cost as much as 40 percent "
           "of someone's productive time (David Meyer, University of Michigan).")

# DEPTH rewrite (Oct 19, 01:30): the 40% number made personal (up to 2 days of a 5-day week), the residue why, then the full
# one-block method: what to close, the status line to set (word for word), stray-thought list, batching 3x a day (Kushlev &
# Dunn), and the after-picture. Rule that stays: "One block, one task."
post("lh-1021-switching-cost", LH, "2026-10-21T12:30", "deep",
     dict(lay="sticky", f="pink", kicker="focus science", text="Multitasking / feels *fast.* / It isn't.", obj="clock", at="br",
          items=["The 40% cost", "Why it happens", "The one-block day", "What to tell your team"], save="save this"),
     [dict(k="say", f="cream", label="sound familiar?", text="Email open. Chat pinging. / *Busy all morning,* / and the report / is half done."),
      dict(k="say", f="dots", label="what's really happening", text="Your brain can't do / two hard things at once. / It *switches,* / back and forth, / all day."),
      dict(k="say", f="pink", text="All that switching / can cost up to this much / of your productive time:", num="40%",
           sub="that's up to 2 days of a 5-day week", src="American Psychological Association, Multitasking: Switching costs"),
      dict(k="why", f="cream", label="and it's not just time", text="Every switch leaves / part of your mind / *on the last task.*",
           sub="a researcher called it attention residue", src="Leroy, 2009"),
      dict(k="steps", f="dots", text="The *one-block* / *morning*",
           items=["Close email and chat", "One task, one hour", "Stray thought? Write it down"]),
      dict(k="say", f="pink", label="what to tell your team", text="Set your status: / *“Heads down till 10.* / *Urgent? Call me.”*",
           sub="then answer everything at 10"),
      dict(k="say", f="cream", label="then batch the small stuff", text="Check email and chat / *3 times a day,* / not 30. / Same times, *every day.*",
           sub="less stress, in a UBC study", src="Kushlev & Dunn, 2015"),
      dict(k="say", f="dots", label="picture this", text="Day 1: *one thing done* / by 10 am. / Week 1: *5 real hours.* / Month 1: you *finish things.*",
           sub="one block. one task."),
      dict(k="do", f="pink", text="Tomorrow, close email and chat for your *first hour.* One task only.",
           save="send this to the friend with 30 tabs open")],
     "Multitasking feels fast. It isn't. Here's what it really costs, and the one-block day that fixes it.\n\n"
     "THE COST: your brain can't do two hard things at once. It switches back and forth, and every switch costs a little time while it "
     "gets back up to speed. The American Psychological Association says those switches can eat up to 40% of your productive time. "
     "In a 5-day week, that's up to 2 days.\n\n"
     "WHY IT'S WORSE THAN TIME: every switch leaves part of your mind on the last task. Researcher Sophie Leroy called it attention "
     "residue: people who jumped to a new task while the old one was unfinished did worse on the new one. (Cal Newport's Deep Work "
     "builds a whole argument on this.)\n\n"
     "THE ONE-BLOCK MORNING:\n"
     "1. Close email and chat. Closed, not minimised. Phone in another room.\n"
     "2. One task for one hour. One document, one tab.\n"
     "3. A thought pops up (\"reply to Sam\")? Write it on paper and keep going. It'll be there at 10.\n\n"
     "WHAT TO TELL YOUR TEAM (copy this into your status): \"Heads down till 10. Urgent? Call me.\" Then answer everything at 10, "
     "so people learn they always hear back.\n\n"
     "THEN BATCH THE SMALL STUFF: check email and chat at set times, like 10, 1 and 4, not 30 times a day. In a University of British "
     "Columbia study, people who checked email 3 times a day for a week felt less stressed than in a week of checking whenever they liked.\n\n"
     "WHAT CHANGES: Day 1, one real thing is done by 10 am. Week 1, that's 5 real hours. Month 1, you stop ending days busy and empty.\n\n"
     "The rule that stays: one block, one task.\n\n"
     "Do this: tomorrow, close email and chat for your first hour and do one task only.\n\n"
     "Send this to the friend with 30 tabs open.\n\n#focus #multitasking #productivity #deepwork #worklife",
     SRC_APA + " Leroy (2009), Why is it so hard to do my work? The challenge of attention residue when switching between work tasks, "
     "Organizational Behavior and Human Decision Processes 109(2). Kushlev & Dunn (2015), Checking email less frequently reduces stress, "
     "Computers in Human Behavior 43. Newport, C. (2016), Deep Work.")



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

# DEPTH rewrite (Oct 18, 22:00): the full Do Not Disturb setup (who to allow, repeated calls, the "call twice" text,
# batch-check at the end) + why (Mark 2008: faster but more stressed; Kushlev & Dunn 2015: batching email lowered stress).
# Rule that stays: "Urgent calls twice."
reel("lh-reel-1019am-pings", LH, "2026-10-19T08:30", "deep", "lh-x-tick-boom", "save this for your next busy day", [
    dict(k="hook", f="dots", text="Every ping / costs you / *more than* / *time.*", emo="⏳"),
    dict(k="because", f="cream", kicker="a UC Irvine study", text="Interrupted workers finished *faster.* Same quality."),
    dict(k="say", f="dots", text="But their *stress* / and frustration / *shot up.*", drop=True),
    dict(k="say", f="pink", text="1. *Do Not Disturb,* / one hour. / 2. Allow *repeated* / *calls.*"),
    dict(k="say", f="cream", text="3. Text family: / *“Urgent?* / *Call twice.”*"),
    dict(k="do", f="pink", text="When the hour ends, check it all *once.*"),
    dict(k="say", f="dots", text="Day 1: *it's weird.* / Week 1: *less stress.* / Month 1: a quiet / hour that's *yours.*"),
    dict(k="save", f="cream", text="Send this to the / always-online coworker."),
], "Every ping costs you more than time. Here's the 2-minute setup that fixes it, and why it works.\n\n"
   "THE SURPRISE: in a UC Irvine study, 48 people wrote work emails while being interrupted again and again. They finished a little "
   "faster than people who weren't interrupted, and their work was just as good. But their stress and frustration went way up. They were "
   "racing to make up for lost time. Interruptions don't just steal minutes. They wind you up.\n\n"
   "THE SETUP (do it once, use it every day):\n"
   "1. Turn on Do Not Disturb for one hour. iPhone: Settings > Focus > Do Not Disturb. Android: Settings > Notifications > Do Not Disturb "
   "(names vary a little by phone).\n"
   "2. Allow 2 or 3 people only: your partner, your kid's school, whoever looks after a parent. Everyone else waits an hour.\n"
   "3. Turn on repeated calls. On iPhone, a second call from the same person within 3 minutes rings through. On most Android phones, "
   "\"repeat callers\" does the same within 15 minutes.\n"
   "4. Text the people who matter, once: \"I silence my phone 9 to 10 each morning. If it's ever urgent, call twice.\"\n"
   "5. At the end of the hour, check everything in one go.\n\n"
   "WHY BATCHING WORKS: in a University of British Columbia study, 124 adults spent one week checking email only three times a day and "
   "one week checking whenever they liked. In the three-times-a-day week, they felt less stressed.\n\n"
   "IF YOU SLIP: caught yourself checking? Don't write off the day. Put the phone back, turn Do Not Disturb on again and finish the hour.\n\n"
   "WHAT CHANGES:\n"
   "Day 1: it feels weird. You'll reach for the phone and find nothing new.\n"
   "Week 1: in that UBC study, one week of batching was enough to feel less stressed.\n"
   "Month 1: one quiet hour every day that nobody else gets to spend for you.\n\n"
   "The big idea (it runs through Indistractable and Deep Work): you don't beat distraction with willpower in the moment. "
   "You set it up once, ahead of time, so there's nothing to resist.\n\n"
   "The rule that stays: urgent calls twice. Everything else can wait an hour.\n\n"
   "Send this to the coworker who answers every ping in ten seconds.\n\n#focus #worklife #productivity #stress #deepwork",
   "Sources: Mark, Gudith & Klocke (2008), The cost of interrupted work: more speed and stress, Proceedings of CHI 2008. 48 participants; "
   "interrupted groups finished faster with no difference in quality, but reported higher stress, frustration, time pressure and effort. "
   "Kushlev & Dunn (2015), Checking email less frequently reduces stress, Computers in Human Behavior 43: 124 adults, one week limited to "
   "three checks a day vs one week unlimited; lower daily stress in the limited week. Repeated-calls windows: Apple Support (Focus settings, "
   "3 minutes) and Android Do Not Disturb settings (repeat callers, 15 minutes); menus vary by phone and software version.")

# DEPTH rewrite (Oct 18, 22:00): part 2 of "Lock one hour" (part 1 aired Oct 18, 19:00, promising "which hour to pick").
# Method: anchor the hour to something you already do (BJ Fogg's recipe + if-then plans), the cue on a sticky note where
# the cue happens, a 10-minute plan B. Rule that stays: "Anchor it. Don't float it."
reel("lh-reel-1019-odd-hours", LH, "2026-10-19T19:00", "deep", "lh-x-lock-in", "send this to a friend on nights", [
    dict(k="hook", f="pink", text="Which hour / should you / *lock?*", emo="⏰"),
    dict(k="because", f="cream", kicker="here's the trick", text="Tie it to something you *already do* daily."),
    dict(k="say", f="dots", text="*After coffee.* / *After drop-off.* / *After your shift.*", drop=True),
    dict(k="say", f="pink", text="Pick the one / you can *protect* / *every day,* not / your dream hour."),
    dict(k="say", f="cream", text="Write it: / *“After I ___,* / *I work one hour.”*"),
    dict(k="do", f="dots", text="Stick the note *where it happens,* like the coffee maker."),
    dict(k="save", f="pink", text="Send this to the friend / who works nights.", next="part 2 of 2"),
], "Which hour should you lock? Not the perfect one. The one that comes right after something you already do.\n\n"
   "WHY: a habit needs a trigger. Stanford researcher BJ Fogg's recipe is \"After I [something I already do], I will [new habit].\" "
   "If-then plans like this, tied to a clear when and where, helped people reach their goals across 94 tests. \"Sometime tomorrow\" "
   "has no trigger. \"After I pour my coffee\" does.\n\n"
   "PICK YOUR ANCHOR:\n"
   "- Office day: after you put your coffee down at your desk.\n"
   "- Parent: after school drop-off, or after the kids' bedtime.\n"
   "- Night shift: after you wake up and eat, whatever time that is.\n"
   "Choose the one you can protect most days, not your dream hour.\n\n"
   "MAKE IT STICK:\n"
   "1. Write it: \"After I ___, I work for one hour on ___.\"\n"
   "2. Put the note where the anchor happens: on the coffee maker, the car dashboard, the fridge.\n"
   "3. Book it in your calendar as a repeating event called \"Locked hour\", so meetings can't land on it.\n"
   "4. Plan B: \"If I only have 10 minutes, I'll do 10 minutes.\" Starting small still keeps the habit going.\n\n"
   "WHAT CHANGES: Day 1, the note does the remembering. Week 1, the coffee (or the drop-off, or the alarm) starts pulling you to the "
   "desk on its own. Around two months in, on average, it stops being a decision at all. A year from now: about 250 locked hours.\n\n"
   "The rule that stays: anchor it, don't float it.\n\n"
   "Do this: tonight, write your sentence on a sticky note and stick it where the anchor happens.\n\n"
   "Part 2 of 2.\n\nSend this to the friend who works nights.\n\n#shiftwork #nightshift #productivity #habits #focus",
   "Sources: Fogg, BJ (2019), Tiny Habits: The Small Changes That Change Everything (Houghton Mifflin Harcourt), the \"After I..., I will...\" "
   "recipe. Gollwitzer & Sheeran (2006), Implementation intentions and goal achievement: a meta-analysis of effects and processes, "
   "Advances in Experimental Social Psychology 38. 94 independent tests, medium-to-large effect (d = .65). " + SRC_LALLY,
   series="Lock one hour · part 2/2")

# DEPTH rewrite (Oct 19, 01:00): the full ready-to-resume method (3 lines, where the note lives, when to write it), the why
# (attention residue, Leroy & Glomb 2018) and the after-picture. Rule that stays: "Park it on paper."
reel("lh-reel-1020am-nap-time", LH, "2026-10-20T08:30", "deep", "lh-x-phone-down", "save this for the next nap", [
    dict(k="hook", f="cream", text="The baby's / finally asleep. / *Now what?*", emo="⏳"),
    dict(k="say", f="pink", text="Mid-task, the / baby wakes up. / Your mind / *keeps chewing* / on it."),
    dict(k="because", f="dots", kicker="the research", text="A *one-minute note* helped people let go, and do better at the next thing.",
         drop=True),
    dict(k="say", f="cream", text="Write 3 lines: / *where I stopped,* / *what's next,* / *what I need.*"),
    dict(k="do", f="dots", text="Baby stirs? Before you get up, write the *3 lines.* Then go."),
    dict(k="say", f="cream", text="Next nap: no / *“where was I?”* / You just / *pick up.*"),
    dict(k="save", f="pink", text="Send this to a friend / with a newborn."),
], "For every parent who gets interrupted halfway through everything. Here's the one-minute note that lets your brain put it down.\n\n"
   "WHY YOUR MIND KEEPS CHEWING: when you stop a task halfway, part of your attention stays stuck on it. Researchers call it attention "
   "residue. So you're feeding the baby while still drafting that email in your head, and doing neither well.\n\n"
   "WHAT THE RESEARCH FOUND: Sophie Leroy and Theresa Glomb gave interrupted people a quick \"ready-to-resume\" plan: write down where "
   "you are and what you'll do next. It took about a minute. People who wrote it carried less of the old task with them, and did better "
   "on the task that interrupted them.\n\n"
   "THE METHOD:\n"
   "1. Keep one sticky pad in one spot, on your laptop lid or next to the monitor.\n"
   "2. When the baby stirs, before you get up, write 3 lines:\n"
   "   Where I stopped: \"paragraph 2 of the daycare email\"\n"
   "   What's next: \"ask about the October fee\"\n"
   "   What I need: \"the invoice from my inbox\"\n"
   "3. Stick it on the screen, and go. You've parked it. Now you can be fully with the baby.\n"
   "4. Next nap, read the note and start with \"what's next\". No scrolling back, no \"where was I?\"\n\n"
   "WHAT CHANGES: Day 1, it feels like one more chore. Week 1, every nap starts with a clear first step instead of ten minutes of "
   "finding your place. And the bigger win: when you're with your baby, more of you is actually there.\n\n"
   "The rule that stays: park it on paper.\n\n"
   "Do this: put a sticky pad on your laptop right now, before the next nap.\n\n"
   "Send this to a friend with a newborn.\n\n#newparents #momlife #dadlife #focus #parenting",
   "Source: Leroy & Glomb (2018), Tasks interrupted: How anticipating time pressure on resumption of an interrupted task causes attention "
   "residue and low performance on interrupting tasks and how a 'ready-to-resume' plan mitigates the effects, Organization Science 29(3). "
   "Leroy (2009), Organizational Behavior and Human Decision Processes 109(2) (attention residue).")

# DEPTH rewrite (Oct 19, 01:00): the shutdown ritual (Deep Work's idea, our own steps) + the sleep-lab why (Scullin et al. 2018:
# a 5-minute detailed to-do list, about 9 minutes faster to sleep; more detail, faster sleep). Rule that stays: "Write it, then rest."
reel("lh-reel-1020-shutdown", LH, "2026-10-20T19:00", "deep", "lh-x-lock-in", "save this for tonight", [
    dict(k="hook", f="dots", text="Lying awake, / thinking about / *tomorrow's* / *to-do list?*", emo="⏰"),
    dict(k="say", f="cream", text="In a sleep lab, / some wrote / *tomorrow's list* / before bed."),
    dict(k="because", f="pink", kicker="the result", text="They fell asleep about *9 minutes faster.* More detail, faster sleep.",
         drop=True),
    dict(k="say", f="dots", text="Write the list, / close the laptop, / say *“done* / *for today.”*"),
    dict(k="do", f="pink", text="Tonight, write tomorrow's list *as detailed as you can.* 5 minutes."),
    dict(k="say", f="dots", text="Night 1: the paper / *holds it.* / Week 1: bed is / for *sleep* again."),
    dict(k="save", f="cream", text="Send this to the friend / who texts you at 1 am."),
], "Lying awake thinking about tomorrow? Your brain is trying not to forget. Give it paper.\n\n"
   "WHAT THE SLEEP LAB FOUND: 57 young adults spent 5 minutes writing before bed. Half wrote tomorrow's to-do list. Half wrote about "
   "what they'd already done. The to-do group fell asleep in about 16 minutes, the other group in about 25. And the more detailed the "
   "to-do list, the faster people fell asleep. (One small study, so it's a nudge, not a cure.)\n\n"
   "WHY: unfinished tasks keep pinging your mind. A specific list tells your brain it's handled.\n\n"
   "THE 5-MINUTE SHUTDOWN (Cal Newport's Deep Work makes the case for a fixed end-of-day ritual; here's ours):\n"
   "1. Open tomorrow's calendar. What's fixed?\n"
   "2. Write the list on paper, with detail: not \"dentist\", but \"call the dentist at 9:15 to move Thursday, have the insurance card\".\n"
   "3. Close the laptop. Phone on its charger, outside the bedroom if you can.\n"
   "4. Say one line out loud, the same every night: \"Done for today.\" It's your cue that work is over.\n\n"
   "WHAT CHANGES: Night 1, the paper holds it so your head doesn't have to. Week 1, the ritual starts to feel like the off switch. "
   "Month 1, bedtime stops being planning time.\n\n"
   "The rule that stays: write it, then rest.\n\n"
   "Do this: tonight, 5 minutes before bed, write tomorrow's list as detailed as you can.\n\n"
   "Send this to the friend who texts you at 1 am.\n\n#sleep #productivity #todolist #habits #bedtimeroutine",
   "Sources: Scullin, Krueger, Ballard, Pruett & Bliwise (2018), The effects of bedtime writing on difficulty falling asleep, Journal of "
   "Experimental Psychology: General 147(1). 57 adults aged 18-30, 5 minutes of writing, overnight polysomnography; to-do list group "
   "fell asleep in about 16 min vs about 25 min; more specific lists, faster sleep onset. Newport, C. (2016), Deep Work (shutdown ritual).")


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
    dict(k="bubbles", f="pink", label="the exact sentence", bubbles=[
        ("out", "“I'll exercise on *[day]* at *[time]* in *[place].*”"), ("in", "wait, that's it??"),
        ("out", "that's it. you decide *once*, ahead of time")], obj="hourglass", tap="tap →"),
    dict(k="payoff", f="dots", label="the rule", text="Decide *once.* / Then just go.", sub="do it daily: about 66 days to autopilot",
         obj="clock", tap="next story →"),
    dict(k="handoff", f="dots", text="The sentence / *that works*", img="lh-1019-one-sentence/01.jpg", next="day 3 tomorrow"),
])
chain("lh-ch-1020", LH, "2026-10-20", "lh20", "lock-in week · day 3/3", [
    dict(k="photo", text="“My phone's off. / *It's fine.*”", sub="it's not →", ink="dark", y=1300),
    dict(k="bubbles", f="cream", label="a real study", bubbles=[
        ("in", "my phone's face down. it's fine"), ("out", "a study of 800 people says no"),
        ("out", "a phone *on the desk* lowered scores, even when off"), ("in", "wait, what?")], obj="hourglass"),
    dict(k="payoff", f="pink", label="what worked best", text="Out of sight / isn't enough. / *Out of reach.*", sub="a room you have to walk to",
         obj="clock"),
    dict(k="bubbles", f="dots", label="but what if…", bubbles=[
        ("in", "I need my phone for 2FA codes"), ("out", "sign in to everything *before* the hour"),
        ("out", "code mid-hour? walk, type it, *walk it back*"), ("in", "ok that's actually doable")], obj="hourglass"),
    dict(k="handoff", f="dots", text="The full / *phone method*", img="lh-1020-phone-other-room/01.jpg", next="lock-in week · done"),
])

# Oct 21 · NEW · day B: guess-and-reveal quiz -> lh-1021-switching-cost

# Oct 21, 19:00 · NEW (Oct 19, 01:10): fills the empty evening Reel slot. Habit maintenance: Lally (missing once didn't undo it),
# the 2-minute version for bad days, restart at the same anchor, no "catching up". Atomic Habits' "never miss twice" idea, own words.
# Rule that stays: "One miss is a blip. Two is a new habit."
reel("lh-reel-1021-miss-once", LH, "2026-10-21T19:00", "deep", "lh-x-phone-down", "save this for the day you miss", [
    dict(k="hook", f="pink", text="Missed a day? / *Don't* / *start over.*", emo="📅"),
    dict(k="say", f="cream", text="96 people built / a daily habit / over *12 weeks.*"),
    dict(k="because", f="dots", kicker="the result", text="Missing *one day* didn't undo it. The habit kept building.", drop=True),
    dict(k="say", f="pink", text="The danger isn't / *the miss.* / It's the story: / *“I blew it.”*"),
    dict(k="say", f="cream", text="Bad day? Do the / *2-minute version:* / one page, / *one line.*"),
    dict(k="do", f="dots", text="Tomorrow: same time, same anchor. *No catching up.* Just start."),
    dict(k="save", f="pink", text="One miss is a blip. / Two is a new habit.", next="send this to a restarter"),
], "Missed a day? Don't start over. The research is on your side.\n\n"
   "THE STUDY: 96 people picked one daily habit and tracked it for 12 weeks. Missing a single day didn't materially set them back. "
   "The habit kept building. (It took 66 days on average to feel automatic, anywhere from 18 to 254.)\n\n"
   "WHY PEOPLE QUIT ANYWAY: it's not the miss. It's the story that comes after it: \"I blew it, I'll restart Monday.\" Then Monday "
   "becomes next month. Atomic Habits puts it simply: never miss twice. Here's how to make that real.\n\n"
   "THE METHOD:\n"
   "1. Decide your 2-minute version now, before the bad day: one page instead of a chapter, one line of the budget, one push-up.\n"
   "2. On a bad day, do only that. It counts. It keeps the trigger and the time connected.\n"
   "3. Missed it completely? Tomorrow, same time, same anchor. No doubling up to \"catch up\". Double days feel like punishment, "
   "and punishment is what makes people quit.\n"
   "4. Mark the miss on your calendar and move on. One mark is a blip, not a verdict.\n\n"
   "WHAT CHANGES: Week 1, a miss stops feeling like failure. Month 1, you have a plan for bad days instead of a guilt spiral. "
   "Year 1, you're still going, misses and all, because you never let one turn into two.\n\n"
   "The rule that stays: one miss is a blip. Two is a new habit.\n\n"
   "Do this: tonight, write your habit's 2-minute version on the same note as your anchor.\n\n"
   "Send this to the friend who restarts every Monday.\n\n#habits #consistency #selfimprovement #motivation #productivity",
   SRC_LALLY + " Clear, J. (2018), Atomic Habits (never miss twice; the two-minute rule).")

chain("lh-ch-1021", LH, "2026-10-21", "lh21", "focus science", [
    dict(k="bubbles", f="cream", label="quick quiz", title="Switching tasks / *all day…*", bubbles=[
        ("in", "how much of your productive time can it cost?"), ("out", "A) about 5%"), ("out", "B) up to 40%")],
         obj="clock", tap="guess, then tap →"),
    dict(k="payoff", f="pink", label="the answer: B", text="Up to / *40%*", sub="of your productive time", obj="clock",
         tap="source: American Psychological Association · tap →"),
    dict(k="bubbles", f="cream", label="so what do I do?", bubbles=[
        ("in", "but I HAVE to answer messages"), ("out", "set your status: *“heads down till 10. urgent? call me.”*"),
        ("out", "then answer everything *at 10*"), ("in", "ok. one hour I can do")], obj="hourglass", tap="tap →"),
    dict(k="payoff", f="dots", label="the rule", text="One block. / *One task.*", sub="check messages 3 times a day, not 30",
         obj="clock", tap="next story →"),
    dict(k="handoff", f="dots", text="The *one-block* / morning", img="lh-1021-switching-cost/01.jpg", next="save it for tomorrow"),
])


# ================================================================== Oct 22 (Story chain day)
SRC_BUNDLE = ("Source: Milkman, Minson & Volpp (2014), Holding the Hunger Games hostage at the gym: an evaluation of temptation bundling, "
              "Management Science 60(2). Participants who could only listen to tempting audiobooks at the gym initially visited the gym "
              "51% more often than the control group; the effect faded after the Thanksgiving break.")
SRC_WALK = ("Source: Oppezzo & Schwartz (2014), Give your ideas some legs: the positive effect of walking on creative thinking, Journal "
            "of Experimental Psychology: Learning, Memory, and Cognition 40(4). Stanford News (April 24, 2014): creative output rose by "
            "an average of 60% when people walked; walking on a treadmill facing a blank wall worked too.")

# DEPTH rewrite (Oct 19, 02:00): temptation bundling as a full method (list wants/shoulds, pair, LOCK the want to the should,
# restart after breaks) + the Atomic Habits tie-in + after-picture. Rule that stays: "Only here, only then."
reel("lh-reel-1022am-bundle", LH, "2026-10-22T08:30", "deep", "lh-x-tick-boom", "save this for your next skipped workout", [
    dict(k="hook", f="cream", text="Can't make / yourself go / *to the gym?*", emo="🎧"),
    dict(k="say", f="pink", text="People got gripping / audiobooks, but / *only at the gym.*"),
    dict(k="because", f="dots", kicker="the result", text="At first, they went to the gym *51% more often.*", drop=True),
    dict(k="say", f="cream", text="The lock matters: / the show plays / *only at the gym.* / Nowhere else."),
    dict(k="do", f="dots", text="Pick one show you love. Play it *only during* the chore you avoid."),
    dict(k="say", f="cream", text="Week 1: you go / *for the story.* / Month 1: you *want* / to go."),
    dict(k="save", f="pink", text="Send this to the friend / who skips the gym."),
], "Can't make yourself go to the gym? Make the gym the only place you get your favourite thing.\n\n"
   "THE STUDY: researchers at Wharton gave people gripping audiobooks they could only listen to at the gym. At first, they went 51% "
   "more often than people with no deal. Afterwards, most said they'd even pay to keep their audiobooks locked at the gym.\n\n"
   "WHY IT WORKS: you stop relying on willpower for the chore. The chore becomes the only door to something you already want. "
   "It's called temptation bundling (Atomic Habits gives it a whole chapter).\n\n"
   "HOW TO SET IT UP:\n"
   "1. List 2 wants (a show, a podcast, a fancy coffee) and 2 shoulds (the treadmill, laundry, the expense report).\n"
   "2. Pair one want with one should: true crime podcast + walking; the new season + folding laundry; the good coffee + the budget.\n"
   "3. LOCK it. The want happens only during the should. If you binge the show on the couch, the deal is dead.\n"
   "4. Make it easy: download the episodes to the gym headphones, leave the laundry basket by the TV.\n\n"
   "THE HONEST PART: in the study, the boost faded after a holiday break. So when life interrupts, restart the deal on purpose, "
   "with a fresh show.\n\n"
   "WHAT CHANGES: Day 1, you go because you want to know what happens next. Week 1, you catch yourself looking forward to it. "
   "Month 1, the chore is the good part of your day.\n\n"
   "The rule that stays: only here, only then.\n\n"
   "Do this: pick one show or podcast you love, and only play it during the chore you avoid.\n\n"
   "Send this to the friend who keeps skipping the gym.\n\n#habits #motivation #gymmotivation #productivity #behaviorchange",
   SRC_BUNDLE + " Clear, J. (2018), Atomic Habits, temptation bundling.")

# DEPTH rewrite (Oct 19, 02:00): the walk method + the nuance that makes it stick (walking helps brainstorming, not the one right
# answer; the boost carries over when you sit back down). Rule that stays: "Walk for ideas. Sit for answers."
reel("lh-reel-1022-walk", LH, "2026-10-22T19:00", "deep", "lh-x-lock-in", "save this for the next time you're stuck", [
    dict(k="hook", f="pink", text="Stuck on / a problem? / *Stand up.*", emo="🚶"),
    dict(k="say", f="cream", text="Stanford tested / people's ideas, / *sitting* vs / *walking.*"),
    dict(k="because", f="dots", kicker="the result", text="Walking raised creative ideas by about *60%* on average.", drop=True),
    dict(k="say", f="pink", text="Even on a treadmill / *facing a wall.* / And it lasted / *after they sat down.*"),
    dict(k="say", f="cream", text="But it didn't help / find *the one* / *right answer.*"),
    dict(k="do", f="pink", text="Stuck? Walk *10 minutes* with the question. Then sit and pick."),
    dict(k="save", f="dots", text="Walk for ideas. / Sit for answers.", next="send this to a desk friend"),
], "Stuck on a problem? Stand up. But know which kind of stuck you are.\n\n"
   "THE STUDY: Stanford researchers tested people's ideas while they sat and while they walked. Walking raised creative output by about "
   "60% on average. It worked on a treadmill facing a blank wall, so it's the walking, not the view. And the boost carried on when "
   "people sat back down after the walk.\n\n"
   "THE PART MOST PEOPLE MISS: walking did NOT help the kind of thinking where there's one right answer. Brainstorming? Walk. "
   "Checking the numbers? Sit.\n\n"
   "HOW TO DO IT:\n"
   "1. Write the question on one line: \"3 ways to fix the onboarding email.\"\n"
   "2. Walk for 10 minutes: around the block, the hallway, the parking lot. No podcast, no scrolling.\n"
   "3. Capture ideas as they come: a voice note or a pocket notebook. Don't judge them yet.\n"
   "4. Sit back down while the boost lasts, and now pick the best one.\n\n"
   "WHAT CHANGES: Day 1, you come back with more ideas than you left with. Week 1, \"I'm stuck\" turns into \"I'll walk on it\". "
   "Month 1, the walk becomes the first step of every hard problem.\n\n"
   "The rule that stays: walk for ideas, sit for answers.\n\n"
   "Do this: next time you're stuck, write the question down and walk 10 minutes with it. Then sit and pick.\n\n"
   "Send this to the friend glued to their desk all day.\n\n#creativity #focus #productivity #walking #worklife",
   SRC_WALK + " Same study: walking did not help convergent (single-answer) thinking; the creative boost persisted when people sat "
   "down shortly after walking.")


SRC_SIX = ("Sources: Van Dongen, Maislin, Mullington & Dinges (2003), The cumulative cost of additional wakefulness, Sleep 26(2): "
           "restricting sleep to 6 hours a night for 14 days produced cognitive deficits equivalent to up to 2 nights of total sleep "
           "deprivation, while people rated themselves only slightly sleepy. Canadian 24-Hour Movement Guidelines for Adults (CSEP, "
           "2020): adults 18-64 should get 7 to 9 hours of good-quality sleep on a regular basis, with consistent bed and wake times. "
           "American Academy of Sleep Medicine, Healthy Sleep Habits (sleepeducation.org): keep a consistent schedule, and if you "
           "can't fall asleep after about 20 minutes, get out of bed and do a quiet activity without screens.")

# DEPTH rewrite (Oct 19, 02:00): the 2-week study, the LOUD why (the damage grows, the feeling doesn't), the full 8-hour setup
# (fixed wake time, bedtime alarm, phone out, the wind-down order, the 20-minute rule) and the after-picture.
# Rule that stays: "Set the bedtime alarm. Obey it like the morning one."
post("lh-1022-six-hours", LH, "2026-10-22T12:30", "deep",
     dict(lay="sticky", f="pink", kicker="focus science", text="6 hours of sleep / *feels* fine. / It isn't.", obj="clock", at="br",
          items=["The study", "Why you can't tell", "The setup", "Can't sleep?"], save="save this"),
     [dict(k="say", f="cream", label="sound familiar?", text="“I'm fine on 6 hours.” / Coffee at 8. / Coffee at 11. / *Fog by 3.*"),
      dict(k="say", f="dots", label="a real sleep lab", text="People slept / *6 hours a night* / for two weeks. / Their focus was tested / *every day.*"),
      dict(k="say", f="pink", label="by day 14", text="Their focus was / as bad as going / *1 to 2 nights* / *with no sleep.*",
           src="Van Dongen et al., Sleep, 2003"),
      dict(k="why", f="cream", label="the scary part", text="They felt only / *a little sleepier.* / The damage grew. / *The feeling didn't.*",
           sub="you can't judge your own sleep debt"),
      dict(k="steps", f="dots", text="The *8-hour* / *setup*",
           items=["Same wake time, all 7 days", "Bedtime alarm 8 hours before", "Phone charges outside the bedroom"]),
      dict(k="say", f="pink", label="when the alarm rings", text="Lights low. Screens off. / Teeth, book, bed. / Same order, / *every night.*",
           sub="the routine becomes the cue"),
      dict(k="say", f="cream", label="can't fall asleep?", text="Don't lie there / fighting it. / After ~20 minutes, / *get up,* read in / dim light. *Then back.*",
           sub="sleep doctors' advice", src="American Academy of Sleep Medicine"),
      dict(k="say", f="dots", label="picture this", text="Night 1: an alarm / tells you *to stop.* / Week 1: about / *7 more hours* of sleep. / Week 2: meet *rested you.*"),
      dict(k="do", f="pink", text="Tonight, set a *bedtime alarm* 8 hours before your wake-up alarm.",
           save="send this to the friend who “runs on 6 hours”")],
     "6 hours of sleep feels fine. Your brain disagrees, and you won't feel it.\n\n"
     "THE STUDY: in a sleep lab, people slept 6 hours a night for two weeks, and their focus was tested every day. It got worse every "
     "single day. By day 14, it was as bad as going 1 to 2 nights with no sleep at all.\n\n"
     "WHY THIS IS THE SURPRISE: they only felt a little sleepier. The damage kept growing; the feeling didn't. So \"I feel fine\" "
     "tells you nothing. Canada's guidelines say adults need 7 to 9 hours, at regular times.\n\n"
     "THE 8-HOUR SETUP:\n"
     "1. Pick one wake time and keep it all 7 days, weekends too.\n"
     "2. Set a second alarm, the bedtime alarm, 8 hours before it. Up at 6:30? Alarm at 10:30.\n"
     "3. Phone charges outside the bedroom. Buy a $10 alarm clock if you need one.\n"
     "4. When the bedtime alarm rings: lights low, screens off, teeth, book, bed. Same order every night, so the routine becomes the cue.\n"
     "5. Can't fall asleep after about 20 minutes? Don't lie there fighting it. Get up, read something dull in dim light, and go back "
     "when you're sleepy. That's standard advice from sleep doctors.\n\n"
     "WHAT CHANGES: Night 1, an alarm tells you to stop instead of a show ending. Week 1, going from 6 to 7 hours is about 7 more hours "
     "of sleep. Week 2, you get to find out what rested you is actually like.\n\n"
     "The rule that stays: obey the bedtime alarm like the morning one.\n\n"
     "Do this: tonight, set a bedtime alarm 8 hours before your wake-up alarm.\n\n"
     "Send this to the friend who \"runs on 6 hours.\"\n\n#sleep #focus #productivity #sleepdeprivation #healthyhabits\n\n"
     "General information only, not medical advice.",
     SRC_SIX)

chain("lh-ch-1022", LH, "2026-10-22", "lh22", "focus science", [
    dict(k="photo", text="“I'm fine / on *6 hours.*”", sub="your brain *disagrees* →", ink="dark", y=560),
    dict(k="bubbles", f="cream", label="sound familiar?", bubbles=[
        ("in", "6 hours again. feel fine though"), ("out", "a sleep lab tested that"),
        ("out", "after 2 weeks, focus was like *1 to 2 nights with no sleep*"), ("in", "but I don't feel tired?")], obj="clock"),
    dict(k="payoff", f="pink", label="the scary part", text="The damage grew. / *The feeling didn't.*", sub="they felt only a little sleepier",
         obj="hourglass"),
    dict(k="bubbles", f="dots", label="so how do I fix it?", bubbles=[
        ("in", "ok but how do I actually get to 8?"), ("out", "same wake time, *all 7 days*"),
        ("out", "then a *bedtime alarm* 8 hours before it")], obj="clock"),
    dict(k="handoff", f="dots", text="The *8-hour* / setup", img="lh-1022-six-hours/01.jpg", next="save it for bedtime"),
])


# ================================================================== Oct 23 (day B: quiz)
SRC_GREEN = ("Source: Lee, Williams, Sargent, Williams & Johnson (2015), 40-second green roof views sustain attention: the role of "
             "micro-breaks in attention restoration, Journal of Environmental Psychology 42. During a sustained-attention task, people "
             "who looked at a flowering green roof for 40 seconds made fewer errors afterwards than people who looked at a concrete roof.")
SRC_CAFF = ("Source: Drake, Roehrs, Shambroom & Roth (2013), Caffeine effects on sleep taken 0, 3, or 6 hours before going to bed, "
            "Journal of Clinical Sleep Medicine 9(11). 400 mg of caffeine (about 2 to 3 cups of coffee, per the AASM summary) taken 6 "
            "hours before bed reduced objectively measured total sleep by more than 1 hour; participants didn't report the disruption.")

# DEPTH rewrite (Oct 19, 02:30): the 40-second study with the LOUD twist (it was a photo on a screen), the when (the signals),
# the where (window, plant, green wallpaper), the not-your-phone rule, and the after-picture. Rule that stays: "Rest your eyes on green."
post("lh-1023-green-break", LH, "2026-10-23T12:30", "deep",
     dict(lay="sticky", f="dots", kicker="focus science", text="A *40-second* / break that / works.", obj="clock", at="br",
          items=["The study", "The twist", "When to take it", "Where to look"], save="save this"),
     [dict(k="say", f="cream", label="sound familiar?", text="You've read / the same line / *three times.* / Your focus is *gone.*"),
      dict(k="say", f="pink", label="a real study", text="150 students did / a long, dull focus task. / Halfway, a *40-second* break / looking at a roof.",
           sub="green plants or bare concrete"),
      dict(k="say", f="dots", label="the result", text="The *green roof* / group made / *fewer mistakes* / afterwards.",
           src="Lee et al., Journal of Environmental Psychology, 2015"),
      dict(k="why", f="cream", label="the twist", text="It wasn't a real roof. / It was a *photo,* / *on a screen.*",
           sub="40 seconds of green was enough"),
      dict(k="say", f="pink", label="when to take it", text="Rereading lines? / Typos piling up? / That's your cue. / *Stop for 40 seconds.*"),
      dict(k="steps", f="dots", text="Where / *to look*",
           items=["A window with trees", "A plant on your desk", "A green photo as wallpaper"]),
      dict(k="say", f="cream", label="not your phone", text="Scrolling is *more input,* / not a rest. / Eyes on green, / *then straight back.*",
           sub="a break should lower the load"),
      dict(k="say", f="pink", label="picture this", text="Day 1: three / *40-second* breaks. / Week 1: fewer / *“wait, what?”* moments. / Under *2 minutes* a day."),
      dict(k="do", f="dots", text="Put a plant or a *green photo* where you look between tasks. Today.",
           save="send this to the friend who scrolls on every break")],
     "A 40-second break that actually works, and you don't even need to go outside.\n\n"
     "THE STUDY: at the University of Melbourne, 150 students did a long, boring focus task. Halfway through, they took a 40-second break "
     "looking at a city rooftop. Half saw a roof covered in flowering plants. Half saw bare concrete. The green-roof group made fewer "
     "mistakes and held their concentration better afterwards.\n\n"
     "THE TWIST: it wasn't a real roof. It was a photo on a computer screen. 40 seconds of looking at green was enough to give tired "
     "attention a short rest.\n\n"
     "WHEN TO TAKE IT: you're rereading the same line, typos are piling up, you've opened the same tab twice. That's the signal.\n\n"
     "WHERE TO LOOK:\n"
     "1. A window with trees or grass. Best.\n"
     "2. No window? A real plant on your desk, at eye level.\n"
     "3. Neither? Set a green landscape photo as your laptop wallpaper and look at it between tasks.\n\n"
     "NOT YOUR PHONE: a scroll is more things to read and react to. That's more load, not a rest. Eyes on green for 40 seconds, then "
     "straight back to the task.\n\n"
     "WHAT CHANGES: Day 1, three 40-second breaks, under 2 minutes in total. Week 1, fewer \"wait, what did I just read?\" moments in "
     "the afternoon. It's the cheapest focus upgrade there is.\n\n"
     "The rule that stays: rest your eyes on green.\n\n"
     "Do this: today, put a plant or a green photo where you look between tasks.\n\n"
     "Send this to the friend who scrolls on every break.\n\n#focus #productivity #breaks #nature #worklife",
     SRC_GREEN + " 150 university students; the roof views were images shown on a computer screen (University of Melbourne news "
     "release, 2015).")

chain("lh-ch-1023", LH, "2026-10-23", "lh22", "focus science", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="cream", label="quick quiz", title="A break that / *helps focus…*", bubbles=[
        ("in", "how long did they look at a green roof?"), ("out", "A) 40 seconds"), ("out", "B) 10 minutes")],
         obj="clock", tap="guess, then tap →"),
    dict(k="payoff", f="pink", label="the answer: A", text="*40* / seconds", sub="and they made fewer mistakes after", obj="clock",
         tap="source: Lee et al., 2015 · tap →"),
    dict(k="bubbles", f="dots", label="the twist", bubbles=[
        ("out", "it wasn't even a real roof"), ("out", "it was a *photo, on a screen*"), ("in", "so a plant on my desk would work??"),
        ("out", "that's the idea. eyes on *green*, not your feed")], obj="hourglass", tap="tap →"),
    dict(k="payoff", f="cream", label="the rule", text="Rest your eyes / *on green.*", sub="40 seconds. then straight back.",
         obj="hourglass", tap="next story →"),
    dict(k="handoff", f="dots", text="A *40-second* / break that works.", img="lh-1023-green-break/01.jpg", next="save it for your next break"),
])

# DEPTH rewrite (Oct 19, 02:30): the 6-hour study with the LOUD part (an hour less sleep and they didn't notice), the cutoff maths
# done for you, the hidden caffeine, what to do instead at 3 pm, and the after-picture. Rule that stays: "Bedtime minus 6."
reel("lh-reel-1023-caffeine", LH, "2026-10-23T19:00", "deep", "lh-x-phone-down", "save this for your afternoon coffee", [
    dict(k="hook", f="dots", text="Coffee at 4 pm? / *Your sleep* / *noticed.*", emo="☕"),
    dict(k="say", f="cream", text="Sleep study: / caffeine *6 hours* / before bed."),
    dict(k="because", f="pink", kicker="the result", text="They slept *over an hour less.* And didn't notice.", drop=True),
    dict(k="say", f="dots", text="Your cutoff: / *bedtime minus 6.* / Bed at 10? / *Last cup by 4.*"),
    dict(k="say", f="cream", text="Count *tea,* / *cola* and / *energy drinks* too."),
    dict(k="do", f="pink", text="Set a phone reminder at your *cutoff time:* “last coffee.”"),
    dict(k="say", f="dots", text="3 pm slump? / Walk *10 minutes,* / or look at *green.*"),
    dict(k="save", f="pink", text="Send this to / your coffee friend."),
], "Coffee at 4 pm? Your sleep noticed, even if you didn't.\n\n"
   "THE STUDY: in a sleep study, people had 400 mg of caffeine, about 2 to 3 cups of coffee, 6 hours before bed. Measured in the lab, "
   "they slept more than an hour less. And here's the loud part: they didn't notice. Their own reports said they slept fine. "
   "(It was a small study of 12 adults, but it's why sleep doctors say 6 hours is the minimum.)\n\n"
   "YOUR CUTOFF, DONE FOR YOU: bedtime minus 6 hours.\n"
   "Bed at 10 pm: last cup by 4 pm.\n"
   "Bed at 11 pm: last cup by 5 pm.\n"
   "Bed at midnight: last cup by 6 pm.\n"
   "Earlier is better if you can.\n\n"
   "COUNT THE SNEAKY ONES: black and green tea, cola, energy drinks, pre-workout powder and some pain relievers all contain caffeine. "
   "Decaf has a little, but far less.\n\n"
   "3 PM SLUMP INSTEAD: a 10-minute walk, or 40 seconds looking at something green, then back to work.\n\n"
   "WHAT CHANGES: Night 1, nothing you can feel, and that's the point: you're getting back sleep you never knew you lost. Week 1, "
   "that's up to an hour a night back, if you were drinking late.\n\n"
   "The rule that stays: bedtime minus 6.\n\n"
   "Do this: set a phone reminder at your cutoff time that just says \"last coffee\".\n\n"
   "Send this to the friend on their 4th coffee.\n\n#sleep #caffeine #coffee #focus #healthyhabits\n\n"
   "General information only, not medical advice.",
   SRC_CAFF + " AASM news release (Nov 14, 2013): 12 healthy adults; subjective reports suggest participants were unaware of the "
   "sleep disturbance.")


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

# DEPTH rewrite (Oct 19, 03:00): habit stacking as a method (anchor + tiny + visible cue), the flossing study as proof, the
# recipe to reuse on any habit, and the after-picture. Rule that stays: "Hang the new habit on an old one."
reel("lh-reel-1024am-floss-after", LH, "2026-10-24T08:30", "deep", "lh-x-tick-boom", "save this for your next new habit", [
    dict(k="hook", f="cream", text="Floss *before* / or *after* / brushing?", emo="🪥"),
    dict(k="say", f="pink", text="Researchers asked / 50 people to floss, / *before* or *after* / brushing."),
    dict(k="because", f="dots", kicker="the result", text="The *after* group built the stronger habit. Still there 8 months later.",
         drop=True),
    dict(k="say", f="cream", text="Brushing became / the *trigger.* / The new habit / *rides on it.*"),
    dict(k="say", f="pink", text="Start tiny: / *one tooth.* / Floss sits / *on the toothbrush.*"),
    dict(k="do", f="dots", text="Tonight: brush, then floss *right after.* Same sink, every night."),
    dict(k="say", f="pink", text="Week 1: skipping / *feels odd.* / Day 66: *automatic.*"),
    dict(k="save", f="cream", text="After I ___, / I will ___.", next="works for any habit"),
], "Floss before or after brushing? For building the habit, it matters, and the reason works for any habit you want.\n\n"
   "THE STUDY: researchers asked 50 people to floss every day, either just before or just after brushing. The \"after\" group built "
   "the stronger habit, and it was still there 8 months later.\n\n"
   "WHY: brushing is something you already do without thinking. Floss right after it, and brushing becomes the trigger. The new habit "
   "rides on the old one. Atomic Habits calls this habit stacking; Tiny Habits calls the old habit your anchor.\n\n"
   "THE METHOD:\n"
   "1. Anchor: pick something you already do every day, in the same place (brushing, the first coffee, sitting down at your desk).\n"
   "2. Tiny: make the new habit so small it's silly. BJ Fogg's famous version: floss one tooth. You'll often do more; one still counts.\n"
   "3. Visible: put the floss on top of the toothbrush, so you can't brush without seeing it.\n"
   "4. Right after: not \"sometime tonight\". The second the anchor ends.\n\n"
   "THE RECIPE TO KEEP: \"After I [old habit], I will [tiny new habit].\" After I pour my coffee, I'll open my budget sheet. After I "
   "sit on the train, I'll read one page.\n\n"
   "WHAT CHANGES: Day 1, one tooth. Week 1, you feel odd brushing without it. Around 2 months on average, it's automatic (in a study "
   "of 96 people, 66 days on average; anywhere from 18 to 254). Year 1: 365 nights of flossing, from one sentence.\n\n"
   "The rule that stays: hang the new habit on an old one.\n\n"
   "Do this: tonight, brush, then floss right after. Same sink, every night.\n\n"
   "Send this to the friend who never flosses.\n\n#habits #habitstacking #selfimprovement #productivity #behaviorchange",
   SRC_FLOSS + " Clear, J. (2018), Atomic Habits (habit stacking). Fogg, BJ (2019), Tiny Habits (anchors; floss one tooth). " + SRC_LALLY)

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

# DEPTH rewrite (Oct 19, 03:00): why lyrics hurt reading (words compete with words), the playlist method (what counts as
# instrumental, volume, same playlist as a start cue, lyrics saved for chores) and the after-picture. Rule: "Words or music. Not both."
reel("lh-reel-1024-lyrics", LH, "2026-10-24T19:00", "deep", "lh-x-lock-in", "save this for your next study session", [
    dict(k="hook", f="pink", text="Studying with / *your playlist* / on?", emo="🎧"),
    dict(k="say", f="cream", text="Students read / and answered questions / with and without / *music.*"),
    dict(k="because", f="dots", kicker="the result", text="Songs *with words* lowered scores. Even songs they *liked.*", drop=True),
    dict(k="say", f="pink", text="Music *without* / words did about / as well as *quiet.*"),
    dict(k="say", f="cream", text="Words in your ears / *fight the words* / on the page."),
    dict(k="do", f="pink", text="Make one *no-lyrics* playlist. Play it every focus hour."),
    dict(k="say", f="cream", text="Month 1: you / press play, / and *you're in.*"),
    dict(k="save", f="dots", text="Save the songs / for chores.", next="send this to your study buddy"),
], "Studying with your playlist on? Check the words.\n\n"
   "THE STUDY: students read passages and answered questions in quiet, with instrumental music, or with songs with lyrics. Songs with "
   "words lowered their scores, even songs they liked. Music without words did about as well as quiet.\n\n"
   "WHY: your brain has one channel for language. Lyrics and the page are both words, so they fight for it. Instrumental music doesn't.\n\n"
   "THE PLAYLIST METHOD:\n"
   "1. Build one focus playlist with no words: classical, film scores, video game soundtracks, lo-fi beats.\n"
   "2. Keep it low, just loud enough to cover the room.\n"
   "3. Play the same playlist every focus hour. Over time, the first track becomes your start signal.\n"
   "4. Save the songs you love for chores and workouts. That's a reward, not a distraction.\n\n"
   "THE HONEST PART: it was a small study (30 students), about reading. For tasks without words, like sorting files, lyrics may matter less.\n\n"
   "WHAT CHANGES: Day 1, the page gets your full channel. Week 1, the first track means \"we're working now\". Month 1, you sit down, "
   "press play, and you're in.\n\n"
   "The rule that stays: words or music, not both.\n\n"
   "Do this: make one no-lyrics playlist tonight and use it for your next focus hour.\n\n"
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

# DEPTH rewrite (Oct 19, 03:20): Planning part 1 = the fallacy + its why (we plan the best day, forget the last time) + the first
# fix (ask "how long did it take LAST time?", then add half). Part 2 tonight = unpack every step. Rule: "Plan from your past, not your hopes."
reel("lh-reel-1025am-planning-fallacy", LH, "2026-10-25T08:30", "deep", "lh-x-tick-boom", "save this before you plan your week", [
    dict(k="hook", f="dots", text="Why does / *everything* / take longer?", emo="⏳"),
    dict(k="say", f="cream", text="Students guessed / their thesis would / take *34 days.*"),
    dict(k="because", f="pink", kicker="the result", text="It took *56 days.* Even their worst case was too short.", drop=True),
    dict(k="say", f="dots", text="We plan the day / *everything goes right.* / Real days / *don't.*"),
    dict(k="say", f="cream", text="Ask: how long did / it take *last time?* / Not: how long / *should* it take?"),
    dict(k="do", f="pink", text="Today, add *half again* to your next time guess. 2 hours? Plan 3."),
    dict(k="save", f="dots", text="Send this to / your “quick” friend.", next="part 2 tonight: the fix"),
], "Why does everything take longer than you think? You're not bad at planning. Everyone is.\n\n"
   "THE STUDY: students guessed their thesis would take 34 days on average. It took 56. Even their worst-case guess, 49 days, was too "
   "short. Only about 3 in 10 finished in the time they predicted. It's called the planning fallacy.\n\n"
   "WHY IT HAPPENS: when we plan, we picture the day where everything goes right: no sick kid, no slow reply, no file that won't open. "
   "And we quietly ignore how long the last one actually took.\n\n"
   "THE FIRST FIX:\n"
   "1. Before you guess, ask \"how long did this take LAST time?\", not \"how long should it take?\"\n"
   "2. Look it up if you can: your calendar, old emails, the last report's date.\n"
   "3. Then add half again. Think 2 hours? Plan 3. Think a week? Plan a week and a half.\n\n"
   "WHAT CHANGES: Day 1, your plan looks worse on paper. Week 1, you finish when you said you would, maybe for the first time in a while. "
   "Month 1, people start trusting your \"by Friday\".\n\n"
   "The rule that stays: plan from your past, not your hopes.\n\n"
   "Do this: today, add half again to your next time guess.\n\n"
   "Send this to the friend who says \"it'll be quick.\" Part 2 tonight at 7: break it into steps, the fix that's backed by research.\n\n"
   "#planning #productivity #timemanagement #focus #procrastination",
   SRC_PLAN, series="Planning · part 1/2")

chain("lh-ch-1025", LH, "2026-10-25", "lh22", "focus science", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="cream", label="quick quiz", title="On people's / *best* work days…", bubbles=[
        ("in", "what mattered most?"), ("out", "A) praise from the boss"), ("out", "B) making *progress*")],
         obj="clock", tap="guess, then tap →"),
    dict(k="payoff", f="pink", label="the answer: B", text="*Progress*", sub="even a small win", obj="clock",
         tap="source: Amabile & Kramer, 12,000 diaries · tap →"),
    dict(k="bubbles", f="dots", label="but…", bubbles=[
        ("in", "my wins are tiny though"), ("out", "tiny counts. *“sent the quote”* is a win"),
        ("out", "write *3* tonight. you'll be surprised")], obj="hourglass", tap="tap →"),
    dict(k="payoff", f="cream", label="the rule", text="Write down / *what you moved.*", sub="a to-do list only shows what's left",
         obj="hourglass", tap="next story →"),
    dict(k="handoff", f="dots", text="Felt like you / did *nothing?*", img="lh-1025-done-list/01.jpg", next="save it for Friday"),
])

# DEPTH rewrite (Oct 19, 03:20): the diary study, the why (to-do lists only show what's left), the done-list method (when,
# what counts, where it lives), the bad-day rescue, the after-picture. Four Thousand Weeks tie-in. Rule: "Count what moved."
post("lh-1025-done-list", LH, "2026-10-25T12:30", "deep",
     dict(lay="sticky", f="cream", kicker="focus science", text="Felt like you / did *nothing* / this week?", obj="clock", at="br",
          items=["The diary study", "What mattered most", "The done list", "Bad-day rescue"], save="save this"),
     [dict(k="say", f="pink", label="sound familiar?", text="Friday, 5 pm. / Busy all week. / What did you / actually do? *Blank.*"),
      dict(k="say", f="dots", label="a real study", text="238 people wrote / a *work diary* / every day. About / *12,000* entries."),
      dict(k="say", f="cream", label="their best days", text="Their best days / had one thing / in common: / *progress.*", sub="even a small win counted",
           src="Amabile & Kramer, The Progress Principle, 2011"),
      dict(k="why", f="pink", label="why you feel behind", text="A to-do list shows / *what's left.* / It never shows / *how far you came.*",
           sub="so your progress stays invisible"),
      dict(k="steps", f="dots", text="The *done* / *list*",
           items=["Every evening, 2 minutes", "3 things you moved forward", "Same notebook, every day"]),
      dict(k="say", f="cream", label="what counts", text="“Sent the quote.” / “Fixed one bug.” / “Called Mom back.” / *Moved = counts.*"),
      dict(k="say", f="pink", label="bad-day rescue", text="Feeling behind? / Read *last week's* list / before you plan / *this week's.*",
           sub="proof beats feelings"),
      dict(k="say", f="dots", label="picture this", text="Day 1: *3 lines.* / Week 1: *15 wins* / you'd have forgotten. / Year 1: a notebook / full of *proof.*"),
      dict(k="do", f="cream", text="Tonight, write down *3 things you moved forward* this week. Small ones count.",
           save="send this to the friend who feels behind")],
     "Felt like you did nothing this week? You probably did more than you think. You just can't see it.\n\n"
     "THE STUDY: Harvard researchers had 238 people at 7 companies write a short diary every workday, about 12,000 entries in all. On "
     "people's best days, one thing showed up far more than anything else: making progress on work that mattered, even a small win. "
     "On their worst days: setbacks.\n\n"
     "WHY YOU FEEL BEHIND: a to-do list only shows what's left, and it never ends. Four Thousand Weeks makes the point bluntly: you will "
     "never get to the bottom of it. So if the list is your scoreboard, you lose every day. A done list shows how far you came.\n\n"
     "THE DONE LIST:\n"
     "1. Every evening, 2 minutes. Same notebook, same spot (next to the laptop, by the kettle).\n"
     "2. Write 3 things you moved forward. Finished or not.\n"
     "3. Small counts: \"sent the quote\", \"fixed one bug\", \"called Mom back\", \"10 minutes on the budget\".\n"
     "4. Friday: read the week's page before you plan next week.\n\n"
     "BAD-DAY RESCUE: when you feel behind, read last week's list before you open this week's to-do list. Proof beats feelings.\n\n"
     "WHAT CHANGES: Day 1, three lines. Week 1, 15 wins you would have forgotten by Saturday. Year 1, a notebook full of proof that "
     "you're moving.\n\n"
     "The rule that stays: count what moved, not what's left.\n\n"
     "Do this: tonight, write down 3 things you moved forward this week. Small ones count. Then do it every evening.\n\n"
     "Send this to the friend who feels behind.\n\n#productivity #motivation #worklife #focus #smallwins",
     SRC_PROGRESS + " Burkeman, O. (2021), Four Thousand Weeks (keep a 'done list').")

# DEPTH rewrite (Oct 19, 03:20): Planning part 2 = unpacking. Write every step INCLUDING the hidden ones (waiting, setup, reviews,
# travel), time each, add them up. Kruger & Evans 2004. Rule: "Guess the steps, not the task."
reel("lh-reel-1025-unpack", LH, "2026-10-25T19:00", "deep", "lh-x-lock-in", "save this for Monday", [
    dict(k="hook", f="cream", text="Your *“quick”* task / isn't quick.", emo="📝"),
    dict(k="say", f="pink", text="Before you guess / how long, *list* / *every step.*"),
    dict(k="because", f="dots", kicker="the research", text="People who *listed the steps* guessed more realistic times.",
         drop=True),
    dict(k="say", f="cream", text="Add the *hidden* / steps: *waiting,* / *setup, replies.*"),
    dict(k="say", f="pink", text="Time *each step.* / Add them up. / That's your / *real number.*"),
    dict(k="do", f="dots", text="Tonight, list the *steps* of Monday's biggest task. Then guess the time."),
    dict(k="say", f="pink", text="Day 1: Monday / *fits in Monday.* / Month 1: *“by Friday”* / means it."),
    dict(k="save", f="cream", text="Guess the steps, / not the task.", next="planning · part 2/2"),
], "Your \"quick\" task isn't quick. Here's the fix that's backed by research.\n\n"
   "THE RESEARCH: in a study, people who listed every step of a task before guessing how long it would take made longer, more "
   "realistic guesses. Hidden steps are where the time goes. It works best for tasks with lots of parts.\n\n"
   "HOW TO DO IT (\"update the website\", unpacked):\n"
   "1. Find the old photos (15 min)\n"
   "2. Wait for the new ones from Sam (1 day of waiting, 5 min of asking)\n"
   "3. Write the new text (45 min)\n"
   "4. Send it for a check, then fix the comments (30 min + a day)\n"
   "5. Upload and test on your phone (20 min)\n"
   "\"An hour\" was really about 2 hours of work and 2 days of waiting.\n\n"
   "THE HIDDEN STEPS TO ALWAYS ADD: waiting for someone, setup (logins, finding files), the back-and-forth, travel, and the check at the end.\n\n"
   "WITH THIS MORNING'S FIX: compare your total with how long it took last time, and if they disagree, trust last time.\n\n"
   "WHAT CHANGES: Day 1, Monday's plan fits inside Monday. Week 1, fewer 9 pm \"how is this not done?\" moments. Month 1, your "
   "estimates become the ones people plan around.\n\n"
   "The rule that stays: guess the steps, not the task.\n\n"
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

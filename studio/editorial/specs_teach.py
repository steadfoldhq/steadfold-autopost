"""§13 content for Oct 18-21 (rebuilt Oct 17 pm): every feed post, Reel and Story chain on all four pages.

Every post: an outcome hook where it fits, a WHY, ONE "Do this:" (what, where, how much, when), captions in the order
outcome -> "Why it works:" -> "Do this:" -> the catch, sources in the first comment.
FF figures come from studio/pivot/ff_math.py (8-10% a year, 10% max; ages 28/30/33 -> 60). No "example" anywhere.
Fact sources (checked Oct 17 pm) are listed per post in `src` (first comment).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pivot"))
from ff_math import FIG  # noqa: E402

FF, HB, LH, LF = "fullyfunded", "hourback", "lockedhour", "littlefold"
NG = "Not guaranteed. Returns vary."
NOT_MED = "General information only, not medical advice."
MADE = "Made up for this post. Check anything important yourself."
PRIV = "Tip: take names, numbers and addresses out before you paste."
K = FIG

# ======================================================================================================== FEED POSTS
POSTS = {}
META = {}  # id -> dict(at, fmt, caption, comment)


def post(pid, brand, at, fmt, cover, slides, caption, comment):
    POSTS[pid] = dict(brand=brand, cover=cover, slides=slides, fmt=fmt)
    META[pid] = dict(at=at, fmt=fmt, caption=caption, comment=comment, kind="feed")


# ------------------------------------------------------------------ Fully Funded
post("ff-1018-rate-call", FF, "2026-10-18T12:00", "learning",
     dict(lay="pills", f="cob", kicker="money moves · day 1/4", text="Cut your / *card rate* / in *one call*", obj="point", at="bl",
          save="the exact words are on slide 5"),
     [dict(k="say", f="lite", label="the move", text="Call your card. / Ask for a / *lower rate.*", sub="works on lines of credit too"),
      dict(k="why", f="coral", text="Interest = / balance × *rate ÷ 12,* / every month.",
           sub="a lower rate shrinks every single month"),
      dict(k="rows", f="lite", text=f"On *${K['card_bal']:,}*, one year", cap="interest if the balance stays put",
           rows=[("at 20%", f"${K['card_20']:,}"), ("at 14%", f"${K['card14']:,}"), ("you keep", f"${K['card_cut']:,}")],
           sub="84% who asked got a lower rate", src="LendingTree survey, 2026"),
      dict(k="steps", f="cob", text="What to *say*", items=["“I've been with you since [year].”", "“Can you lower my rate?”",
                                                       "“What's your best rate?”"], sub="a no? ask when to retry"),
      dict(k="catch", f="coral", text="A lower rate / still *charges / interest.*", sub="pay the balance down too"),
      dict(k="do", f="lite", text="Tonight, call the number / on the back of your card. / Ask: *“Can you lower / my rate?”*",
           save="save this for the call")],
     f"One phone call can cut what your card balance costs you.\n\nWhy it works: interest is your balance × your rate ÷ 12, charged every month. "
     f"Drop the rate and every month's charge shrinks. On ${K['card_bal']:,} left for a year, 20% costs ${K['card_20']:,}; 14% costs ${K['card14']:,}. "
     f"84% of people who asked last year got a lower rate.\n\nDo this: tonight, call the number on the back of your card and ask: \"Can you lower my rate?\"\n\n"
     f"The catch: a lower rate still charges interest. Pay the balance down too.\n\n#creditcards #debtfree #personalfinance #moneytips #interestrates",
     "Sources: LendingTree survey (Sept 2026): 84% of cardholders who asked for a lower APR in the past year got one; average cut 6.3 points. "
     "Interest maths: monthly compounding on a balance that stays put, no new spending.")

post("ff-1019-rich-habits-01", FF, "2026-10-19T12:00", "tip",
     dict(lay="line", f="lite", kicker="rich habits, decoded · no.1", text="The *cheap* coat / costs *5× more*", obj="ok", at="br",
          dots=[("$240 coat", "120 wears", f"${K['coat_a']} a wear"), ("$60 coat", "6 wears", f"${K['coat_b']} a wear")],
          save="follow the line: price ÷ uses"),
     [dict(k="why", f="cob", text="You pay *once.* / You *use* it / many times.", sub="so the real price is per use"),
      dict(k="steps", f="coral", text="How, in *3 steps*", items=["Guess the uses, honestly", "Price ÷ uses", "Lower number wins"],
           sub="the tag isn't the price"),
      dict(k="catch", f="lite", text="Only counts / if you *really* / use it.", sub="a $240 coat in the closet: $240 a wear"),
      dict(k="do", f="cob", text="Before your next buy / over *$50,* write: / *price ÷ uses.*", save="save this for your next cart")],
     f"The cheaper tag can cost you more.\n\nWhy it works: you pay once, but you use it many times. A $240 coat worn 120 times is ${K['coat_a']} a wear. "
     f"A $60 coat worn 6 times is ${K['coat_b']} a wear.\n\nDo this: before your next buy over $50, write down price ÷ uses.\n\n"
     f"The catch: it only counts if you really use it. Be honest about the uses.\n\nRich Habits, Decoded is our weekly series. This is No.1.\n\n"
     f"#moneytips #budgeting #personalfinance #frugalliving #richhabits",
     "Maths: price ÷ number of uses. $240 ÷ 120 = $2. $60 ÷ 6 = $10. Your numbers will differ: count your own uses.")

post("ff-1020-pick-its-home", FF, "2026-10-20T12:00", "learning",
     dict(lay="pills", f="cob", kicker="money moves · day 3/4", text="Same / *$10,000.* / Two *homes.*", obj="piggy", at="br",
          save="slide 4 is where it changes"),
     [dict(k="say", f="lite", label="before", text="Age 30. / *$10,000* in a / 0% account.", sub="at 60: still $10,000"),
      dict(k="say", f="coral", label="the move", text="Same $10,000, / in a *broad / index fund.*", sub="left alone for 30 years"),
      dict(k="why", f="lite", text="Growth *on growth.*", sub="each year's gain earns the next",
           bars=[("30", K["k10_steps"][0], "$10K"), ("40", K["k10_steps"][1], f"${K['k10_steps'][1] // 1000}K"),
                 ("50", K["k10_steps"][2], f"${K['k10_steps'][2] // 1000}K"), ("60", K["k10_steps"][3], f"${K['k10_steps'][3] // 1000}K")]),
      dict(k="rows", f="cob", text="At *60*, left alone", cap="$10,000 put in at 30",
           rows=[("at 0%", f"${K['k10_0']:,}"), ("at 8% a year", f"${K['k10_8']:,}"), ("at 10% a year", f"${K['k10_10']:,}")],
           sub="10%: the S&P 500's long-run average"),
      dict(k="catch", f="coral", text="It *can fall,* / some years / *a lot.*", sub="money you need within 5 years stays in cash"),
      dict(k="do", f="lite", text="Tonight, find the *rate* / on your savings. / Money you won't touch / for 10+ years: *move it / off 0%.*",
           save="save this for your next statement")],
     f"Where your money sits can matter more than how much you put in.\n\nWhy it works: growth on growth. Each year's gain earns the next year's. "
     f"$10,000 at 30, left alone to 60: still $10,000 at 0%, about ${K['k10_8']:,} at 8% a year, about ${K['k10_10']:,} at 10%.\n\n"
     f"Do this: tonight, find the rate on your savings. Money you won't touch for 10+ years shouldn't sit at 0%.\n\n"
     f"The catch: markets can fall, some years a lot. Money you need within 5 years stays in cash.\n\n{NG}\n\n"
     f"#investing #compoundinterest #personalfinance #moneytips #indexfunds",
     "Maths: $10,000, compounded monthly for 30 years (age 30 to 60), no fees or taxes. 10% a year is roughly the S&P 500's long-run "
     "average before inflation. Education, not advice.")

post("ff-1021-clb-who-qualifies", FF, "2026-10-21T12:00", "learning",
     dict(lay="pills", f="coral", kicker="money moves · day 4/4", text="Do you / *qualify* for / *$2,000?*", obj="piggy", at="br",
          save="the income check is on slide 4"),
     [dict(k="say", f="lite", label="the move", text="Open a *free RESP.* / The bond / lands in it.", sub="Canada Learning Bond"),
      dict(k="why", f="cob", text="*$500* the first year. / *$100* a year after. / Up to *$2,000.*", sub="no deposit needed from you",
           src="canada.ca · Canada Learning Bond"),
      dict(k="rows", f="lite", text="Who *qualifies*", cap="adjusted family net income · Jul 2025 to Jun 2026",
           rows=[("1 to 3 kids", "$57,375 or less"), ("4 kids", "under $64,733"), ("5 kids", "under $72,123")],
           sub="kids born 2004 or later", src="canada.ca · ESDC notice 2025-1095 · limits change each July"),
      dict(k="steps", f="cob", text="3 steps / to *claim*", items=["Open a free RESP", "Give your child's SIN", "Apply for the bond"],
           sub="no money needed"),
      dict(k="do", f="coral", text="This week, book an / *RESP appointment.* / Bring your child's *SIN.*",
           save="save this for your bank visit")],
     "Up to $2,000 for your child's education, with no deposit from you.\n\nWhy it works: the Canada Learning Bond pays $500 the first year "
     "and $100 a year after, up to $2,000, into an RESP.\n\nWho qualifies: kids born in 2004 or later, in families under the income limits on slide 4 "
     "(1 to 3 kids: adjusted family net income $57,375 or less).\n\nDo this: this week, book an RESP appointment at your bank or credit union. "
     "Bring your child's SIN.\n\nThe catch: the limits change each July.\n\n#RESP #canadalearningbond #parenting #personalfinance #canada",
     "Sources: canada.ca, Canada Learning Bond brochure ($500 + $100 a year to age 15, up to $2,000; born on or after Jan 1, 2004; RESP and SIN "
     "needed; no contributions required). Income limits: ESDC notice 2025-1095, July 2025 to June 2026.")

# ------------------------------------------------------------------ Locked Hour (verified research only)
post("lh-w2-05-restart", LH, "2026-10-18T12:30", "learning",
     dict(lay="sticky", f="pink", kicker="lock-in week · day 1/3", text="Day 1, again? / *Make it stick*", obj="clock", at="br",
          items=["Restart smaller", "One hour, not a routine", "Write one if-then"], save="the if-then: slide 4"),
     [dict(k="say", f="cream", label="the move", text="Restart with / *one hour,* / not a routine."),
      dict(k="why", f="dots", text="A new week feels / like a *clean page.*", sub="gym visits rose 33% at the start of a week",
           src="Dai, Milkman & Riis, Management Science, 2014"),
      dict(k="steps", f="pink", text="How, in *3 steps*", items=["Pick tomorrow or Monday", "One hour, one task", "“After dinner, I start the timer”"],
           sub="that last line is an if-then plan"),
      dict(k="catch", f="cream", text="Missed one? / *Don't wait* / for Monday.", sub="tomorrow is a fresh start too"),
      dict(k="do", f="dots", text="Tonight, write: / *“After dinner tomorrow, / I start a 60-minute timer.”*",
           save="save this for the restart")],
     "Restart smaller and it's more likely to stick.\n\nWhy it works: fresh starts are real. In one study, gym visits rose 33% at the start of a "
     "new week. A new day can feel like a clean page too.\n\nDo this: tonight, write \"After dinner tomorrow, I start a 60-minute timer.\"\n\n"
     "The catch: one hour, not a whole new routine. Big restarts fall over.\n\n#productivity #habits #focus #studytips #selfimprovement",
     "Source: Dai, Milkman & Riis (2014), The Fresh Start Effect, Management Science 60(10). Gym visits rose 33.4% at the start of a week "
     "(university gym data).")

post("lh-w2-08-lockin-kickoff", LH, "2026-10-19T12:30", "deep",
     dict(lay="line", f="cream", kicker="lock-in 90 · day 1", text="*90 hours* / by Jan 16", obj="clock", at="br",
          dots=[("Day 1", "today", "1 hour"), ("Day 90", "Jan 16", "90 hours")], save="one hour a day. that's it."),
     [dict(k="say", f="pink", label="before", text="Big plans. / *No hours.*", sub="sound familiar?"),
      dict(k="say", f="dots", label="the turning point", text="One hour. / *Same time* / every day."),
      dict(k="why", f="cream", text="*When + where* plans / get done more.", sub="94 tests: a medium-to-large effect",
           src="Gollwitzer & Sheeran, 2006"),
      dict(k="rows", f="pink", text="*After*", cap="one hour a day from Oct 19",
           rows=[("Day 30", "30 hours"), ("Day 60", "60 hours"), ("Day 90 · Jan 16", "90 hours")]),
      dict(k="steps", f="dots", text="Join in *3 steps*", items=["Pick your hour", "Pick one project", "Comment IN"]),
      dict(k="catch", f="cream", text="Missed a day? / *Never miss twice.*"),
      dict(k="do", f="pink", text="Right now, book / *tomorrow's hour* / in your calendar. / Then comment *IN.*",
           save="save this for day 2")],
     "90 hours of real work by Jan 16, one hour a day.\n\nWhy it works: plans that say when and where get done more often. Across 94 tests, "
     "if-then plans had a medium-to-large effect on reaching goals.\n\nDo this: right now, book tomorrow's hour in your calendar. Then comment IN "
     "so we can count you.\n\nThe catch: you'll miss a day. Never miss twice.\n\n#lockin #productivity #habits #focus #goals",
     "Source: Gollwitzer & Sheeran (2006), Implementation intentions and goal achievement: a meta-analysis, Advances in Experimental "
     "Social Psychology 38. 94 independent tests, d = .65.")

post("lh-w2-07-minute-by-minute", LH, "2026-10-20T12:30", "learning",
     dict(lay="sticky", f="dots", kicker="lock-in week · day 3/3", text="One hour, / *minute by minute*", obj="clock", at="br",
          items=["0:00 Wi-Fi off", "0:45 note the next step", "0:50 walk"], save="save this for tomorrow"),
     [dict(k="say", f="cream", label="the move", text="0:00 / *Wi-Fi off.* / One task."),
      dict(k="why", f="pink", text="Every switch / leaves *attention* / behind.", sub="it stays stuck on the last task",
           src="Leroy, 2009, Organizational Behavior and Human Decision Processes"),
      dict(k="steps", f="dots", text="The *clock*", items=["0:00 Wi-Fi off, one task", "0:45 write the next step", "0:50 walk with one question"]),
      dict(k="catch", f="cream", text="Interrupted? / You'll *rush* / to catch up.", sub="faster, but more stress",
           src="Mark, Gudith & Klocke, CHI 2008"),
      dict(k="do", f="pink", text="Tomorrow, run *one hour* / on this clock. / *Wi-Fi off* at 0:00.", save="save this for tomorrow")],
     "One hour, set up so you actually stay in it.\n\nWhy it works: when you switch tasks, part of your attention stays on the last one "
     "(researchers call it attention residue). Wi-Fi off cuts the switches.\n\nDo this: tomorrow, run one hour on this clock. Wi-Fi off at 0:00.\n\n"
     "The catch: interruptions make people work faster, but with more stress. Guard the hour, don't race it.\n\n"
     "#focus #deepwork #productivity #studytips #timemanagement",
     "Sources: Leroy (2009), Why is it so hard to do my work? Attention residue, OBHDP 109(2). Mark, Gudith & Klocke (2008), The cost of "
     "interrupted work: more speed and stress, CHI.")

# ------------------------------------------------------------------ Hourback (why the AI technique works)
post("hb-w02-4-renewal-changes", HB, "2026-10-18T13:00", "learning",
     dict(lay="pills", f="plum", kicker="ai evenings · day 1/4", text="Find what your / *renewal* / *changed*", obj="phone", at="br",
          save="the exact prompt is on slide 6"),
     [dict(k="say", f="indi", label="the move", text="Paste last year's / *next to* / this year's."),
      dict(k="why", f="yel", text="AI only compares / *what you paste.*", sub="give it both years and it checks line by line"),
      dict(k="steps", f="plum", text="How, in *3 steps*", items=["Copy both letters", "Ask for every change", "Check each one yourself"]),
      dict(k="catch", f="indi", text="It can *miss* one.", sub="ask: “what did you leave out?”"),
      dict(k="do", f="yel", text="When your renewal lands, / paste *both years* and ask: / *“List every change.”*",
           save="save this for your next renewal")],
     f"Find what changed in your renewal, not just the price.\n\nWhy it works: AI only works from what you paste. Give it last year's letter and "
     f"this year's, and it compares them line by line.\n\nDo this: when your renewal lands, paste both years and ask: \"List every change.\"\n\n"
     f"The catch: it can miss one. Ask \"What did you leave out?\", then check the letters yourself.\n\n{PRIV}\n\n#aitips #insurance #lifeadmin #renewal #moneytips",
     "Why it works: chat AIs answer from the text in the conversation, so pasting both versions gives it something concrete to compare. "
     "It can still skip or misread a line, so check every change against the letters.")

post("hb-1018-single-before-paste", HB, "2026-10-18T17:45", "keep",
     dict(lay="mosaic", f="indi", text="“Take the / names out / first.”", obj="point", at="bl", save="save this before you paste anything into AI"),
     [dict(k="do", f="yel", text="Before you paste, / swap names for / *[Name]* and numbers / for *[Number].*", save="keep this one")],
     f"Keep this: take the names out first.\n\nWhy it works: anything you paste leaves your device. Swap names, account numbers and addresses "
     f"for [Name], [Number], [Address], and the answer is just as useful.\n\nDo this: before you paste, swap every name for [Name] and every number for [Number].\n\n"
     f"The catch: it only helps if you do it every time.\n\n#aitips #privacy #lifeadmin #chatgpt #techtips",
     "Check your AI app's privacy settings too: some use chats to train models unless you turn it off.")

post("hb-w02-8-12-automations-kickoff", HB, "2026-10-19T13:00", "deep",
     dict(lay="pills", f="indi", kicker="12 weeks, 12 automations · no.1", text="Two calendars. / *One page.* / Clashes *flagged.*",
          obj="phone", at="br", save="save this for Sunday night"),
     [dict(k="say", f="yel", label="before", text="Two calendars. / A school note. / *Missed pickup.*"),
      dict(k="say", f="plum", label="the turning point", text="Paste all three. / Ask AI to / *flag the clashes.*"),
      dict(k="why", f="indi", text="It lines up / *every time* / side by side.", sub="clashes show up as two things at once"),
      dict(k="say", f="yel", label="after", text="It found: *nobody / free for Thursday / swim.*", sub="made up for this post"),
      dict(k="catch", f="plum", text="Check *every line* / against your / calendars."),
      dict(k="do", f="indi", text="Sunday night, paste / *both calendars* and ask: / *“Flag every clash / this week.”*",
           save="a new automation every Monday")],
     f"Your family's week on one page, with the clashes flagged.\n\nWhy it works: AI lines up every time from both calendars side by side, "
     f"so two things at once stand out.\n\nDo this: Sunday night, paste both calendars and ask: \"Flag every clash this week.\"\n\n"
     f"The catch: check every line against your calendars before you rely on it.\n\n12 Weeks, 12 Automations: a new one every Monday, 1 pm ET.\n\n"
     f"{MADE}\n\n#aitips #familycalendar #lifeadmin #momlife #organization",
     "Prompt: \"Here are two calendars and a school note. List this week's events by day and flag any time two things overlap.\" "
     "The week shown is made up for this post.")

post("hb-1019-single-group-chat", HB, "2026-10-19T17:45", "keep",
     dict(lay="pills", f="yel", text="*47 messages.* / Still no *plan.*", obj="chat", at="tr", save="send this to the group chat that needs it"),
     [dict(k="do", f="indi", text="Paste the chat. Ask: / *“Give 3 options and / the one most / people agreed on.”*",
           save="then you book it")],
     f"Keep this for the next group chat that goes in circles.\n\nWhy it works: asking for options plus the one most people agreed on makes AI pull "
     f"out what people actually said yes to.\n\nDo this: paste the chat and ask: \"Give 3 options and the one most people agreed on.\"\n\n"
     f"The catch: check it against the chat before you book.\n\n{PRIV}\n\n#groupchat #aitips #friends #lifeadmin #planning",
     "Remove names and phone numbers before you paste a group chat.")

post("hb-1020-prompt-week-01", HB, "2026-10-20T13:00", "learning",
     dict(lay="sticky", f="indi", kicker="prompt of the week · no.1", text="5 dinners, / *one list*", obj="point", at="bl",
          items=["30 min each", "Foods you skip", "Use up the fridge", "One list"], save="prompt: slide 5"),
     [dict(k="say", f="yel", label="the move", text="One prompt: / *5 dinners* + / one shopping list."),
      dict(k="why", f="plum", text="Rules in, / *fewer edits* out.", sub="time, foods you skip, what's in the fridge"),
      dict(k="steps", f="indi", text="How, in *3 steps*", items=["Fill the [brackets]", "Paste it into any AI", "Check the cupboards"]),
      dict(k="catch", f="yel", text="It doesn't *know* / your cupboards.", sub="tick the list against them"),
      dict(k="do", f="plum", text="Sunday, fill the / *[brackets]* in the caption / and paste it. *Shop once.*",
           save="save this for Sunday night")],
     "Plan 5 dinners and one shopping list with one prompt.\n\nWhy it works: the more rules you give it (time, foods you skip, what's in the "
     "fridge), the less you edit after.\n\nDo this: Sunday, fill the brackets and paste:\n\"Plan 5 dinners for [number] people, 30 minutes or less "
     "each. We don't eat [foods]. Use up [fridge] first. Then one shopping list, grouped by aisle.\"\n\nThe catch: it doesn't know your cupboards. "
     "Tick the list first.\n\nPrompt of the Week, No.1.\n\n#mealplanning #aitips #dinnerideas #familydinner #lifeadmin",
     "Prompt of the Week is a weekly series. Tip: leave out allergies' personal details; just list the foods to skip.")

post("hb-1020-single-stopped-doing", HB, "2026-10-20T17:45", "keep",
     dict(lay="pills", f="plum", text="I *stopped* / reading the / *boring bits*", obj="cup", at="bl", save="I still check every quote"),
     [dict(k="do", f="yel", text="Next long letter: ask / *“What do I need to do, / and by when? Quote / the line.”*",
           save="then check each quote")],
     "Keep this for the next long letter.\n\nWhy it works: asking for the exact line ties every answer to text you can find and check.\n\n"
     "Do this: next long letter, ask: \"What do I need to do, and by when? Quote the line.\"\n\nThe catch: find each quote in the letter yourself.\n\n"
     f"{PRIV}\n\n#aitips #lifeadmin #paperwork #productivity #techtips",
     "Why quotes help: a quoted line can be checked against the original; an answer without one can't.")

post("hb-1021-ai-said-what-bill", HB, "2026-10-21T13:00", "learning",
     dict(lay="mosaic", f="indi", text="“$96 dinner. / Ana didn't / drink.”", obj="point", at="bl", save="AI split it. we checked the math."),
     [dict(k="say", f="yel", label="the move", text="Ask AI to split it / *and show the math.*"),
      dict(k="why", f="plum", text="Shown math / is *checkable* math.", sub="you can add it up in 5 seconds"),
      dict(k="say", f="indi", label="the answer", text="Ana: *$18.* / The rest: *$26.*", sub="18 + 26 + 26 + 26 = 96"),
      dict(k="catch", f="yel", text="AI *can* get / sums wrong.", sub="that's why you check it"),
      dict(k="do", f="plum", text="Next shared bill, add: / *“Show the math and / check it adds up.”*", save="then add it yourself")],
     f"Split any bill fairly, and know it's right.\n\nWhy it works: math you can see is math you can check. Ana skipped drinks: AI said Ana $18, "
     f"everyone else $26, and 18 + 26 + 26 + 26 = 96.\n\nDo this: next shared bill, add \"Show the math and check it adds up.\"\n\n"
     f"The catch: AI can get sums wrong. Add it up yourself.\n\nMade up for this post; the reply is from a real AI run.\n\n"
     f"#billsplit #aitips #dinnerwithfriends #lifeadmin #moneytips",
     "Food split 4 ways, drinks split 3 ways. Any currency, same math.")

post("hb-1021-single-subscriptions", HB, "2026-10-21T17:45", "keep",
     dict(lay="sticky", f="yel", text="*5 subscriptions,* / one statement", obj="point", at="bl",
          items=["Streaming 12.99", "Cloud 2.99", "Fitness 9.99", "Phone 45.00", "News 7.50"], save="78.47 a month. made up for this post."),
     [dict(k="do", f="indi", text="Paste a statement. Ask: / *“List every repeat / charge and the / monthly total.”*",
           save="then cancel one")],
     "Keep this: find every subscription in one go.\n\nWhy it works: AI can spot charges that repeat across a statement and add them up.\n\n"
     "Do this: paste a statement and ask: \"List every repeat charge and the monthly total.\"\n\nThe catch: check the total yourself, and take out "
     f"your card and account numbers first.\n\n{MADE}\n\n#subscriptions #aitips #budgeting #moneytips #lifeadmin",
     "In our made-up statement the total was 78.47 a month; our own sum matched.")

# ------------------------------------------------------------------ Littlefold (official guidance only)
post("lf-04-sleep-when-baby-sleeps", LF, "2026-10-18T11:30", "learning",
     dict(lay="sticky", f="pink", kicker="first weeks home · part 1/2", text="Split *the night* / in two", obj="shoe", at="br",
          items=["You're on till 2 am", "Then swap", "Off means fully off"], save="part 2 tomorrow"),
     [dict(k="say", f="butter", label="the move", text="You're on / till 2 am. / *Then swap.*"),
      dict(k="why", f="cream", text="Rest when / *baby rests.* / Ask your partner *to help.*", sub="that's the NHS advice",
           src="NHS, Sleep and tiredness after having a baby"),
      dict(k="steps", f="pink", text="How, in *3 steps*", items=["Pick the swap time", "Off-shift sleeps elsewhere", "Formula or expressed milk? share feeds"]),
      dict(k="catch", f="butter", text="Breastfeeding? / Partner brings baby, / *then settles.*", sub="nappies and burps count too"),
      dict(k="do", f="cream", text="Tonight, agree a / *swap time.* / Write it on the fridge.", save="save this for week one")],
     f"Split the night so you both sleep.\n\nWhy it works: the NHS says rest when your baby sleeps and ask your partner to help. "
     f"If you formula feed or use expressed milk, they can share feeds.\n\nDo this: tonight, agree a swap time and write it on the fridge.\n\n"
     f"The catch: breastfeeding? Your partner can bring baby, then do the nappy and the settle.\n\nFirst weeks home, part 1 of 2. Part 2 tomorrow.\n\n"
     f"{NOT_MED}\n\n#newparents #newborn #postpartum #sleepdeprived #parenting",
     "Source: NHS, Sleep and tiredness after having a baby (nhs.uk): rest when your baby sleeps; ask a partner to help; partners can share "
     "formula or expressed-milk feeds.")

post("lf-1018-single-sign-say-it", LF, "2026-10-18T17:00", "keep",
     dict(lay="pills", f="pink", text="How are you, / *really?*", obj="ok", at="bl", save="low for more than 2 weeks? tell someone",
          src="NHS, Postnatal depression"),
     [dict(k="do", f="butter", text="Still low after / *2 weeks?* Call your / *GP or midwife* this week.",
           save="send this to a new parent", src="NHS, Postnatal depression")],
     f"Keep this for the hard weeks.\n\nWhy it works: the NHS says the baby blues usually pass within 2 weeks of the birth. If low feelings carry on, "
     f"get worse, or you're struggling, getting help matters.\n\nDo this: still low after 2 weeks? Call your GP, midwife or health visitor this week.\n\n"
     f"The catch: you don't need every sign to ask.\n\n{NOT_MED}\n\n#postpartum #newmom #maternalmentalhealth #newparents #postnataldepression",
     "Source: NHS, Postnatal depression, symptoms (nhs.uk): baby blues usually go within 2 weeks; see a GP, midwife or health visitor if you "
     "think you might have postnatal depression, even with only some of the signs.")

post("lf-05-partner-week-one", LF, "2026-10-19T11:30", "deep",
     dict(lay="sticky", f="cream", kicker="first weeks · 2/2", text="Own *5 jobs* / in week 1", obj="point", at="bl",
          items=["Bring baby to feeds", "The after-feed", "A night shift", "Visitors", "Meals + laundry"],
          save="send to partner"),
     [dict(k="say", f="butter", label="before", text="One parent / does *every* / night job."),
      dict(k="say", f="pink", label="the turning point", text="The partner / *owns 5 jobs.*"),
      dict(k="why", f="cream", text="Ask your partner / *to help:* nappies, / dressing, feeds.", src="NHS, Sleep and tiredness after having a baby"),
      dict(k="say", f="butter", label="after", text="The feeding parent / *gets back to sleep.*"),
      dict(k="catch", f="pink", text="Breastfeeding? / Partner does / *everything else.*"),
      dict(k="do", f="cream", text="Today, the partner picks / *2 of the 5 jobs* / and starts *tonight.*",
           save="send this to your partner")],
     f"Week one goes better when the partner owns the jobs.\n\nWhy it works: the NHS suggests asking a partner to help with nappies, dressing and "
     f"feeds so the feeding parent can get back to sleep.\n\nDo this: today, the partner picks 2 of the 5 jobs and starts tonight.\n\n"
     f"The catch: breastfeeding? The partner does everything around the feed.\n\nFirst weeks home, part 2 of 2.\n\n{NOT_MED}\n\n"
     f"#newdad #newparents #partners #newborn #postpartum",
     "Source: NHS, Sleep and tiredness after having a baby (nhs.uk).")

post("lf-1019-single-fever-under-3m", LF, "2026-10-19T17:00", "keep",
     dict(lay="pills", f="pink", text="Under 3 months / with a fever? / *Call now.*", obj="point", at="tr",
          save="save this. send it to your sitter.", src="American Academy of Pediatrics"),
     [dict(k="do", f="butter", text="Under 3 months and / *38.0°C (100.4°F)* or more? / *Call the doctor now.*",
           save="don't wait for morning", src="American Academy of Pediatrics, healthychildren.org")],
     f"Keep this on the fridge.\n\nWhy it works: for babies under 3 months, the American Academy of Pediatrics says a temperature of 38.0°C "
     f"(100.4°F) or higher is a reason to call your doctor right away.\n\nDo this: under 3 months and 38.0°C or more? Call your doctor now. "
     f"Out of hours, go to emergency.\n\nThe catch: older babies have different rules. Ask your doctor for yours.\n\n{NOT_MED}\n\n"
     f"#newborn #babyhealth #newparents #fever #parenting",
     "Source: American Academy of Pediatrics, healthychildren.org, Fever: when to call the pediatrician (younger than 3 months and 100.4°F / "
     "38.0°C or higher: call right away).")

post("lf-06-toddler-meltdown", LF, "2026-10-20T11:30", "learning",
     dict(lay="sticky", f="cream", text="Calmer meltdowns, / *starting today*", obj="ok", at="bl",
          items=["Calm yourself first", "Keep them safe", "Hold your no", "No treat to stop it"], save="save this for the next grocery run"),
     [dict(k="say", f="pink", label="the move", text="Said no? / *Keep it.*"),
      dict(k="why", f="butter", text="Give in once and / it teaches / *tantrums work.*", src="NHS, Temper tantrums"),
      dict(k="steps", f="cream", text="In the moment", items=["Breathe. Ignore onlookers.", "Keep them safe", "Hold your no, calmly"]),
      dict(k="catch", f="pink", text="Catch it early: / *point at something* / *interesting.*", sub="distraction works best at the start"),
      dict(k="do", f="butter", text="Next shop, keep it *short* / and give them *one job:* / “find the bananas.”",
           save="save this for the next grocery run")],
     f"Calmer meltdowns start with one rule: hold your no.\n\nWhy it works: the NHS says changing your answer to stop a tantrum teaches your child "
     f"that tantrums work.\n\nDo this: next shop, keep it short and give them one job, like \"find the bananas\".\n\nThe catch: if one is starting, "
     f"distraction works best early: point at something interesting.\n\n{NOT_MED}\n\n#toddlers #tantrums #parenting #toddlermom #gentleparenting",
     "Source: NHS, Temper tantrums (nhs.uk): stay calm, don't give in, keep shop trips short and involve your child, try distraction early.")

post("lf-1020-single-coat-check", LF, "2026-10-20T17:00", "suggestion",
     dict(lay="pills", f="butter", text="Puffy coat? / *Off* before / *buckling.*", obj="shoe", at="br",
          save="blanket over the straps, never under", src="American Academy of Pediatrics"),
     [dict(k="do", f="pink", text="Coat off. Buckle. / *Pinch test* the strap. / Coat or blanket *on top.*",
           save="can you pinch it? tighten it", src="American Academy of Pediatrics, healthychildren.org")],
     f"Try this before the first cold drive.\n\nWhy it works: the AAP says a puffy coat's padding flattens in a crash, leaving the harness loose.\n\n"
     f"Do this: coat off, buckle, pinch the strap at the shoulder. Then the coat or a blanket goes on top of the straps.\n\nThe catch: can you pinch "
     f"the strap? It's too loose. Tighten it.\n\n{NOT_MED}\n\n#carseatsafety #winter #newparents #toddlers #babysafety",
     "Source: American Academy of Pediatrics, healthychildren.org, Winter car seat safety tips.")

# ======================================================================================================== REELS
REELS = {}


def reel(rid, brand, at, fmt, track, save, scenes, caption, comment, series=None):
    REELS[rid] = dict(brand=brand, track=track, save=save, scenes=scenes, fmt=fmt)
    META[rid] = dict(at=at, fmt=fmt, caption=caption, comment=comment, kind="reel", series=series)


# ------------------------------------------------------------------ Fully Funded
reel("ff-reel-1018am-lower-rate", FF, "2026-10-18T08:15", "tip", "ff-x-big-reveal", "save this before your next statement", [
    dict(k="hook", f="cob", text="One call. / *Lower rate.*", emo="📞"),
    dict(k="say", f="lite", text="Call your card. / Ask for a / *lower rate.*"),
    dict(k="because", f="coral", text="*84%* who asked / got one."),
    dict(k="num", f="deep", label="$5,000, 20% → 14%:", value=K["card_cut"], pre="$", suf="less interest a year", drop=True),
    dict(k="do", f="lite", text="Tonight, call the / number on your card. / Ask: *“Can you lower / my rate?”*"),
    dict(k="save", f="cob", text="the exact words / are in today's post", next="today 12 pm"),
], f"One call can cut what your card costs you.\n\nWhy it works: interest is your balance × your rate ÷ 12, every month. 84% of people who asked "
   f"last year got a lower rate. On ${K['card_bal']:,} for a year, 20% to 14% keeps ${K['card_cut']:,} in your pocket.\n\n"
   f"Do this: tonight, call the number on the back of your card and ask: \"Can you lower my rate?\"\n\nThe catch: a lower rate still charges "
   f"interest. Pay it down too.\n\n#creditcards #debtfree #personalfinance #moneytips #interestrates",
   "Source: LendingTree survey (Sept 2026): 84% who asked for a lower APR in the past year got one; average cut 6.3 points. "
   "Maths: $5,000 balance for a year, compounded monthly, no new spending.")

reel("ff-reel-1018-start-28", FF, "2026-10-18T19:00", "deep", "ff-x-money-moves", "save this if you're under 35", [
    dict(k="hook", f="cob", text="Start at 28. / *Not 33.*", emo="⏳"),
    dict(k="say", f="lite", text="*$300* a month. / Stop at 60. / 10% a year."),
    dict(k="num", f="coral", label="Start at 33:", value=K["s33_60"], pre="$", size=230),
    dict(k="say", f="lite", text="Now start / *5 years earlier.*"),
    dict(k="because", f="coral", text="Early dollars / *grow the longest.*"),
    dict(k="num", f="deep", label="Start at 28:", value=K["s28_60"], pre="$", suf=f"${K['s_in_extra']:,} more put in", size=230, drop=True),
    dict(k="do", f="lite", text="This payday, set a / *$300 monthly transfer* / to your investing account."),
    dict(k="save", f="cob", text="started later? / part 2 tomorrow", next="part 2 · 7 pm"),
], f"Five years can be worth more than everything you add later.\n\nWhy it works: early dollars grow the longest. $300 a month from 28 to 60 at "
   f"10% a year: about ${K['s28_60']:,}. From 33: about ${K['s33_60']:,}. The 5 extra years add ${K['s_in_extra']:,} of deposits and about "
   f"${K['s_gap']:,} at 60.\n\nDo this: this payday, set a $300 monthly transfer to your investing account.\n\nThe catch: markets fall some years. "
   f"Keep 3 months' costs in cash first.\n\nPart 1 of 2. Part 2 tomorrow: started later?\n\n{NG}\n\n#investing #compoundinterest #personalfinance #moneytips #retirement",
   "Maths: $300 at the end of each month, compounded monthly at 10% a year (roughly the S&P 500's long-run average before inflation), "
   "no fees or taxes. Education, not advice.", series="Start at 28 · part 1/2")

reel("ff-reel-1019am-gift-per-person", FF, "2026-10-19T08:15", "keep", "ff-x-level-up", "save this before you start gift shopping", [
    dict(k="hook", f="cob", text="Gift budget: / *per person.*", emo="🎁"),
    dict(k="say", f="lite", text="List *every name* / first."),
    dict(k="because", f="coral", text="A cap *per person* / is easy to check / *in the store.*"),
    dict(k="num", f="deep", label=f"{K['gift_n']} people × ${K['gift_each']}:", value=K["gift_total"], pre="$", suf="before you shop", drop=True),
    dict(k="do", f="lite", text="Tonight, list *every name.* / Put *$25* next to each. / Total it."),
    dict(k="save", f="cob", text="save this before / gift shopping"),
], f"Keep this: budget gifts per person, not per total.\n\nWhy it works: a cap per person is easy to check in the store. {K['gift_n']} people × "
   f"${K['gift_each']} = ${K['gift_total']}, decided before you shop.\n\nDo this: tonight, list every name, put $25 next to each, and total it.\n\n"
   f"The catch: total too high? Lower the $25, not the list.\n\n#holidaybudget #giftideas #budgeting #moneytips #christmasshopping",
   f"Maths: {K['gift_n']} × ${K['gift_each']} = ${K['gift_total']}. Use your own number of names.")

reel("ff-reel-1019-late-start", FF, "2026-10-19T19:00", "suggestion", "ff-x-big-reveal", "save this if you feel late", [
    dict(k="hook", f="cob", text="Started at 33? / *Catch up.*", emo="⏳"),
    dict(k="say", f="lite", text="Want what *$300* / from 28 gets / by 60?"),
    dict(k="because", f="coral", text="Fewer years / means *bigger* / monthly deposits."),
    dict(k="num", f="deep", label="From 33 to 60:", value=K["catch_pmt"], pre="$", suf="a month, at 10% a year", drop=True),
    dict(k="do", f="lite", text="This payday, add *$100* / to your transfer. / Add more *each raise.*"),
    dict(k="save", f="cob", text="part 2 of 2 · save it", next="start at 28 · done"),
], f"Started later? You can still catch up.\n\nWhy it works: fewer years means bigger deposits. To match $300 a month from 28 by age 60 "
   f"(at 10% a year), you'd put in about ${K['catch_pmt']} a month from 33.\n\nDo this: this payday, add $100 to your monthly transfer, then more "
   f"with each raise.\n\nThe catch: returns vary year to year. Keep 3 months' costs in cash first.\n\nPart 2 of 2.\n\n{NG}\n\n"
   f"#investing #personalfinance #moneytips #retirement #compoundinterest",
   "Maths: monthly deposit from 33 to 60 that reaches the same value as $300 a month from 28 to 60, both compounded monthly at 10% a year. "
   "Education, not advice.", series="Start at 28 · part 2/2")

reel("ff-reel-1020am-three-numbers", FF, "2026-10-20T08:15", "keep", "ff-x-level-up", "send this to your person", [
    dict(k="hook", f="cob", text="Moving in? / Swap *3 numbers.*", emo="🏠"),
    dict(k="list", f="lite", items=["*Take-home*", "*Debts*", "*Savings*"], size=130),
    dict(k="because", f="coral", text="You can't split / fairly what / *you can't see.*"),
    dict(k="list", f="deep", items=["Rent *$2,000*", "Pay 60/40:", "*$1,200 · $800*"], size=120, drop=True),
    dict(k="do", f="lite", text="This Sunday, write your / *3 numbers* on paper. / *Swap* them over coffee."),
    dict(k="save", f="cob", text="send this to / your person"),
], f"Keep this before you move in together.\n\nWhy it works: you can't split fairly what you can't see. Swap take-home pay, debts and savings first. "
   f"Earn $6,000 and $4,000 a month? A $2,000 rent split by income is $1,200 and $800.\n\nDo this: this Sunday, write your 3 numbers on paper "
   f"and swap them over coffee.\n\nThe catch: 50/50 can feel fair and still not be. Pick together.\n\n#couplesandmoney #movingin #budgeting #moneytips #relationships",
   "Maths: split by share of income: $2,000 × 6,000 ÷ 10,000 = $1,200; the rest is $800.")

reel("ff-reel-1020-windfall-pause", FF, "2026-10-20T19:00", "suggestion", "ff-x-money-moves", "save this for your next bonus", [
    dict(k="hook", f="cob", text="Windfall? / *Park it first.*", emo="💰"),
    dict(k="say", f="lite", text="Bonus, refund, gift: / *30 days* / somewhere boring."),
    dict(k="because", f="coral", text="A pause turns / a *rush* / into a *plan.*"),
    dict(k="list", f="deep", items=["Then split it:", "*Debt*", "*Buffer*", "*Future*"], size=120, drop=True),
    dict(k="do", f="lite", text="Today, open a separate / *savings account* / just for windfalls."),
    dict(k="save", f="cob", text="save this for / your next bonus"),
], "Try this with your next bonus or refund.\n\nWhy it works: a pause turns a rush into a plan. Park it for 30 days, then split it three ways: "
   "debt, buffer, future.\n\nDo this: today, open a separate savings account just for windfalls.\n\nThe catch: high-interest debt? Pay that first, "
   "no pause needed.\n\n#bonus #taxrefund #moneytips #personalfinance #budgeting",
   "This is a habit, not a rule: if you carry high-interest debt, paying it down first usually wins.")

# ------------------------------------------------------------------ Locked Hour
reel("lh-reel-1018am-pick-3", LH, "2026-10-18T08:30", "tip", "lh-x-lock-in", "save this for Sunday night", [
    dict(k="hook", f="cream", text="Finish *3 things* / this week", emo="⏰"),
    dict(k="say", f="pink", text="Give each one / a *day and a time.*"),
    dict(k="because", f="dots", text="*When + where* plans / get done more: / 94 tests."),
    dict(k="list", f="cream", items=["Mon 7 pm · *Gym*", "Wed 8 pm · *Report*", "Fri 7 am · *Course*"], drop=True),
    dict(k="do", f="pink", text="Tonight, 10 minutes: / put *3 blocks* / in your calendar."),
    dict(k="save", f="dots", text="save this for / Sunday night"),
], "Finish 3 things this week.\n\nWhy it works: plans that say when and where get done more often. Across 94 tests, if-then plans had a "
   "medium-to-large effect on reaching goals.\n\nDo this: tonight, take 10 minutes and put 3 blocks in your calendar, each with a day and a time.\n\n"
   "The catch: treat them like meetings. Move them, never delete them.\n\n#productivity #weeklyplanning #habits #focus #timemanagement",
   "Source: Gollwitzer & Sheeran (2006), meta-analysis of implementation intentions, Advances in Experimental Social Psychology 38: 94 tests, d = .65.")

reel("lh-reel-1018-mute-the-world", LH, "2026-10-18T19:00", "suggestion", "lh-x-phone-down", "save this for tomorrow morning", [
    dict(k="hook", f="pink", text="Busy all day. / *Nothing done?*", emo="⏳"),
    dict(k="say", f="cream", text="Lock *one hour* / for one task."),
    dict(k="because", f="dots", text="Each switch / leaves *attention* / behind."),
    dict(k="list", f="pink", items=["*1* Notifications off", "*2* One task", "*3* Door shut"], drop=True),
    dict(k="do", f="cream", text="Tomorrow, *one hour,* / notifications *off.* / One task."),
    dict(k="save", f="dots", text="which hour? / part 2 tomorrow", next="part 2 · 7 pm"),
], "Busy all day and nothing done? Lock one hour.\n\nWhy it works: when you switch tasks, part of your attention stays on the last one. "
   "Researchers call it attention residue.\n\nDo this: tomorrow, one hour, notifications off, one task.\n\nThe catch: it won't feel productive at "
   "minute 5. Stay in.\n\nLock one hour, part 1 of 2. Part 2 tomorrow: which hour?\n\n#focus #deepwork #productivity #studytips #timemanagement",
   "Source: Leroy (2009), Why is it so hard to do my work? The challenge of attention residue when switching between work tasks, "
   "Organizational Behavior and Human Decision Processes 109(2).", series="Lock one hour · part 1/2")

reel("lh-reel-1019am-pick-task", LH, "2026-10-19T08:30", "tip", "lh-x-tick-boom", "save this for tomorrow morning", [
    dict(k="hook", f="dots", text="Pick the task / *before the timer*", emo="⏳"),
    dict(k="say", f="cream", text="*One task.* / One line."),
    dict(k="because", f="pink", text="Switching *mid-hour* / leaves attention / behind."),
    dict(k="list", f="dots", items=["Report → *intro*", "House → *desk*", "Course → *1 lesson*"], drop=True),
    dict(k="do", f="cream", text="Before the timer, write / *one task* on a / sticky note."),
    dict(k="save", f="pink", text="save this for / tomorrow morning"),
], "Pick the task before you start the timer.\n\nWhy it works: deciding mid-hour means switching, and each switch leaves part of your "
   "attention behind (attention residue).\n\nDo this: before the timer, write one task on a sticky note. Too big? Shrink it: report → intro.\n\n"
   "The catch: one task means one. The rest goes on a later list.\n\n#focus #productivity #studytips #deepwork #habits",
   "Source: Leroy (2009), attention residue, Organizational Behavior and Human Decision Processes 109(2).")

reel("lh-reel-1019-odd-hours", LH, "2026-10-19T19:00", "suggestion", "lh-x-lock-in", "send this to a friend on nights", [
    dict(k="hook", f="pink", text="Which hour? / *The one / after you wake.*", emo="⏰"),
    dict(k="say", f="cream", text="Nights, shifts, / *4 pm mornings:* / still works."),
    dict(k="because", f="dots", text="A plan tied to a *cue* / gets done more."),
    dict(k="say", f="pink", text="Waking up / *is the cue.*", drop=True),
    dict(k="do", f="cream", text="Tonight, write: / *“After I wake, / I lock one hour.”*"),
    dict(k="save", f="dots", text="part 2 of 2 · save it", next="lock one hour · done"),
], "Your morning might be 4 pm. Lock the hour after you wake.\n\nWhy it works: if-then plans tie an action to a cue. Across 94 tests they had a "
   "medium-to-large effect on reaching goals. Waking up is a cue you never miss.\n\nDo this: tonight, write \"After I wake, I lock one hour.\"\n\n"
   "The catch: the cue only works if the task is picked the night before.\n\nLock one hour, part 2 of 2.\n\n#shiftwork #nightshift #productivity #habits #focus",
   "Source: Gollwitzer & Sheeran (2006), implementation intentions meta-analysis, Advances in Experimental Social Psychology 38.",
   series="Lock one hour · part 2/2")

reel("lh-reel-1020am-nap-time", LH, "2026-10-20T08:30", "keep", "lh-x-phone-down", "save this for the next nap", [
    dict(k="hook", f="cream", text="Nap-time hour? / *Start with 20.*", emo="⏳"),
    dict(k="say", f="pink", text="Pick a *20-minute* task / before the nap."),
    dict(k="because", f="dots", text="A picked task / means *no switching* / mid-nap."),
    dict(k="list", f="cream", items=["One *email*", "One *page*", "One *form*"], drop=True),
    dict(k="do", f="pink", text="Today, write *3 tasks* / of 20 minutes / on a *sticky note.*"),
    dict(k="save", f="dots", text="save this for / the next nap"),
], "Keep this for nap time.\n\nWhy it works: a task picked in advance means no deciding (and no switching) once the nap starts. Each switch "
   "leaves attention behind.\n\nDo this: today, write 3 tasks of 20 minutes on a sticky note.\n\nThe catch: baby wakes at minute 19? You still showed up.\n\n"
   "#newparents #productivity #momlife #focus #parenting",
   "Source: Leroy (2009), attention residue, Organizational Behavior and Human Decision Processes 109(2).")

reel("lh-reel-1020-shutdown", LH, "2026-10-20T19:00", "keep", "lh-x-lock-in", "save this for tonight", [
    dict(k="hook", f="dots", text="Fall asleep / *faster tonight*", emo="⏰"),
    dict(k="say", f="cream", text="Before bed: / write *tomorrow's* / to-do list."),
    dict(k="because", f="pink", text="In one lab study, / list-writers fell asleep / *about 10 min faster.*"),
    dict(k="list", f="dots", items=["*1* First task", "*2* Start time", "*3* Where you stopped"], drop=True),
    dict(k="do", f="cream", text="Tonight, 5 minutes / before bed: write / *tomorrow's 3 lines.*"),
    dict(k="save", f="pink", text="save this for / tonight"),
], "Keep this for tonight.\n\nWhy it works: in a sleep-lab study, people who spent 5 minutes writing a to-do list for tomorrow fell asleep about "
   "10 minutes faster than people who wrote about what they'd already done.\n\nDo this: tonight, 5 minutes before bed, write tomorrow's 3 lines: "
   "first task, start time, where you stopped.\n\nThe catch: one small study, 57 young adults. Worth a try, not a cure.\n\n"
   "#sleep #productivity #todolist #habits #bedtimeroutine",
   "Source: Scullin, Krueger, Ballard, Pruett & Bliwise (2018), Journal of Experimental Psychology: General 147(1). 57 adults aged 18-30; "
   "to-do list group ~15 min to sleep vs ~25 min for the completed-tasks group.")

# ------------------------------------------------------------------ Hourback
reel("hb-reel-1018am-freeze-frame", HB, "2026-10-18T08:45", "tip", "hb-x-smart-bounce", "send this to the family chat", [
    dict(k="hook", f="indi", text="*147* unread. / Family chat.", emo="💬"),
    dict(k="say", f="yel", text="Copy it. / *Names out.*"),
    dict(k="ai", f="plum", text="What do I do, / by when?"),
    dict(k="because", f="indi", text="AI answers only / from *what you paste.*"),
    dict(k="list", f="yel", items=["Dessert · *Sat*", "Pick up Gran · *Sun 2 pm*"], size=104, drop=True),
    dict(k="do", f="plum", text="Paste the chat. Ask: / *“What do I need / to do, by when?”*"),
    dict(k="save", f="indi", text="send this to / the family chat"),
], f"147 unread in the family chat? Get your two jobs out of it.\n\nWhy it works: AI answers from what you paste, so the whole chat becomes "
   f"one short list.\n\nDo this: paste the chat and ask: \"What do I need to do, by when?\"\n\nThe catch: check each line against the chat.\n\n"
   f"{MADE}\n{PRIV}\n\n#familychat #aitips #lifeadmin #momlife #organization",
   "The chat in this Reel is made up; the list is from a real AI run on it.")

reel("hb-reel-1018-school-email", HB, "2026-10-18T19:00", "suggestion", "hb-x-ta-da-funk", "save this for the next newsletter", [
    dict(k="hook", f="indi", text="School newsletter. / *Again.*", emo="📩"),
    dict(k="say", f="plum", text="Dates buried in / *paragraph 6.*"),
    dict(k="because", f="yel", text="A *list* answer / gives one line / per date to check."),
    dict(k="list", f="indi", items=["Thu · *Photo day*", "Fri · *Costumes*"], size=120, drop=True),
    dict(k="do", f="yel", text="Paste it. Ask: / *“List every date, / earliest first.”*"),
    dict(k="save", f="plum", text="save this for / the next newsletter"),
], f"Never miss a date buried in a school newsletter.\n\nWhy it works: asking for a list gives you one line per date, easy to check.\n\n"
   f"Do this: paste the newsletter and ask: \"List every date, earliest first.\"\n\nThe catch: check each date in the newsletter before it goes in "
   f"your calendar.\n\n{MADE}\n\n#schoolmom #aitips #lifeadmin #parenting #organization",
   "The newsletter shown is made up for this post.")

reel("hb-reel-1019am-just-the-asks", HB, "2026-10-19T08:45", "tip", "hb-x-future-easy", "save this for your inbox", [
    dict(k="hook", f="indi", text="255 words. / *3 asks.*", emo="📧"),
    dict(k="ai", f="plum", text="What do they need / from me? *Quote it.*"),
    dict(k="because", f="yel", text="A quote ties each ask / to *a line / you can check.*"),
    dict(k="list", f="indi", items=["Move car · *Tue*", "Tag bike · *Fri*", "Party · *optional*"], size=104, drop=True),
    dict(k="do", f="plum", text="Next long email, ask: / *“What do you need / from me? Quote it.”*"),
    dict(k="save", f="yel", text="save this for / your inbox"),
], f"Get the asks out of any long email.\n\nWhy it works: asking for a quote ties each ask to a line you can find in the email.\n\n"
   f"Do this: next long email, ask: \"What do you need from me? Quote it.\"\n\nThe catch: find each quote in the email yourself.\n\n{MADE}\n{PRIV}\n\n"
   f"#inbox #aitips #email #productivity #lifeadmin", "The email shown is made up; all 3 quotes matched the email in our run.")

reel("hb-reel-1019-one-sorry", HB, "2026-10-19T19:00", "suggestion", "hb-x-smart-bounce", "save this before you hit send", [
    dict(k="hook", f="indi", text="4 sorries. / *One email.*", emo="🙇"),
    dict(k="say", f="yel", text="Sorry. Sorry. / Sorry. *Sorry.*"),
    dict(k="because", f="plum", text="*“Keep my words”* / stops it rewriting / *you.*"),
    dict(k="say", f="yel", text="1 sorry. / *Same promise.*", drop=True),
    dict(k="do", f="indi", text="Before you send, ask: / *“Keep my words. / Apologise once.”*"),
    dict(k="save", f="plum", text="part 2 tomorrow: / the neighbour text", next="calm replies · 1/2"),
], f"Say sorry once and still sound warm.\n\nWhy it works: \"Keep my words\" stops AI rewriting you into someone else. It only trims.\n\n"
   f"Do this: before you send, paste your draft and ask: \"Keep my words. Apologise once.\"\n\nThe catch: read it out loud. If it doesn't sound like "
   f"you, change it back.\n\nCalm replies, part 1 of 2. Part 2 tomorrow.\n\n{MADE}\n\n#email #aitips #communication #worklife #writing",
   "The email shown is made up for this post.", series="Calm replies · part 1/2")

reel("hb-reel-1020am-driveway-text", HB, "2026-10-20T08:45", "tip", "hb-x-future-easy", "save this for the next awkward text", [
    dict(k="hook", f="indi", text="7:52 am. / *Neighbour's text.*", emo="💬"),
    dict(k="say", f="yel", text="Your guest / *blocked their / driveway.*"),
    dict(k="because", f="plum", text="A *word limit* / keeps it calm / and short."),
    dict(k="say", f="yel", text="31 words. / *One sorry.*", drop=True),
    dict(k="do", f="indi", text="Ask: *“Calm reply, / under 40 words. / Own it, no grovelling.”*"),
    dict(k="save", f="plum", text="part 2 of 2 · save it", next="calm replies · 2/2"),
], f"Reply to an awkward text without grovelling.\n\nWhy it works: a word limit forces AI to keep the reply calm and short.\n\n"
   f"Do this: paste the text and ask: \"Calm reply, under 40 words. Own it, no grovelling.\"\n\nThe catch: send it in your own voice. Edit any word "
   f"you wouldn't say.\n\nCalm replies, part 2 of 2.\n\n{MADE} The reply is from a real AI run.\n\n#neighbours #aitips #communication #texting #lifeadmin",
   "The text shown is made up; the AI reply was 31 words with one apology in our run.", series="Calm replies · part 2/2")

reel("hb-reel-1020-three-tabs", HB, "2026-10-20T19:00", "suggestion", "hb-x-ta-da-funk", "save this before you buy", [
    dict(k="hook", f="indi", text="11 pm. 3 tabs. / *3 blenders.*", emo="🛒"),
    dict(k="say", f="yel", text="Paste the specs / and *how you'll use it.*"),
    dict(k="because", f="plum", text="Your use case / gives it *a reason* / to pick one."),
    dict(k="say", f="indi", text="Blender A. / *Tabs closed.*", drop=True),
    dict(k="do", f="yel", text="Ask: *“Which should I / get? One line first, / then a table.”*"),
    dict(k="save", f="plum", text="save this before / you buy"),
], f"Close the tabs and pick one.\n\nWhy it works: AI only knows the specs you paste. Add how you'll use it and it has a reason to pick.\n\n"
   f"Do this: paste the specs and ask: \"Which should I get? One line first, then a table.\"\n\nThe catch: check the specs on the shop page before "
   f"you buy.\n\nSpecs made up for this post; the reply is from a real AI run.\n\n#shoppingtips #aitips #kitchen #lifeadmin #techtips",
   "Never paste card details into an AI chat.")

reel("hb-reel-1021am-brand-email", HB, "2026-10-21T08:45", "deep", "hb-x-smart-bounce", "save this before you reply to a brand", [
    dict(k="hook", f="indi", text="$2,000 for / *one Reel?*", emo="📧"),
    dict(k="say", f="yel", text="“Reply within / *24 hours.*”"),
    dict(k="say", f="plum", text="Before: / *almost replied.*"),
    dict(k="ai", f="yel", text="Is this brand / email legit? / *List the red flags.*"),
    dict(k="because", f="indi", text="Asking for *red flags* / makes it look / for them."),
    dict(k="list", f="plum", items=["Asks for your *login*", "A *$49* fee", "A *24-hour* rush"], size=104, drop=True),
    dict(k="say", f="yel", text="After: / *deleted. Blocked.*"),
    dict(k="do", f="indi", text="Too-good brand email? / Paste it. Ask: / *“List the red flags.”*"),
    dict(k="save", f="plum", text="save this before / you reply to a brand"),
], f"A $2,000 brand deal in your inbox? Check it before you reply.\n\nWhy it works: asking AI for red flags makes it look for them, and it lists "
   f"each one so you can check it.\n\nDo this: paste the email and ask: \"Is this legit? List the red flags.\"\n\nThe catch: AI can't verify a "
   f"company. Real brands never ask for your login or a fee.\n\n{MADE} The reply is from a real AI run.\n\n#creators #scams #aitips #influencer #brandDeals",
   "Never paste your passwords or codes into an AI chat. Check a brand on its own website, not the links in the email.")

reel("hb-reel-1021-group-costume", HB, "2026-10-21T19:00", "suggestion", "hb-x-ta-da-funk", "send this to the group chat", [
    dict(k="hook", f="indi", text="6 friends. / *1 costume.*", emo="💬"),
    dict(k="say", f="plum", text="*63 messages.* / No plan."),
    dict(k="because", f="yel", text="*“From what we own”* / keeps it / free and fast."),
    dict(k="list", f="indi", items=["Priya · *rain*", "Theo · *cloud*", "Mila · *sun*", "Kai · *lightning*"], size=104, drop=True),
    dict(k="do", f="yel", text="Paste the chat. Ask: / *“3 group themes / from what we own.”*"),
    dict(k="save", f="plum", text="send this to / the group chat"),
], f"One group costume, decided tonight.\n\nWhy it works: \"from what we own\" gives AI a rule, so its themes cost nothing to make.\n\n"
   f"Do this: paste the chat and ask: \"3 group themes from what we own.\"\n\nThe catch: someone still wants pirates. Vote, then go.\n\n{MADE}\n\n"
   f"#halloween #groupcostume #aitips #friends #halloweencostume", "Names and chat made up for this post.")

# ------------------------------------------------------------------ Littlefold
reel("lf-reel-1018am-3am-windows", LF, "2026-10-18T08:00", "suggestion", "lf-x-sunny-bounce", "save this for the 3 am feed", [
    dict(k="hook", f="pink", text="3:07 am. / *Up again?*", emo="⏰"),
    dict(k="say", f="cream", text="Make night feeds / *boring.*"),
    dict(k="because", f="butter", text="Babies learn / *night is different* / from day."),
    dict(k="list", f="berry", items=["Lights *low*", "Voice *quiet*", "No *play*"], size=120, drop=True),
    dict(k="do", f="cream", text="Tonight, set a *dim lamp* / by the feeding chair. / Talk *softly.*"),
    dict(k="save", f="pink", text="save this for / the 3 am feed"),
], f"Make night feeds boring, on purpose.\n\nWhy it works: the NHS suggests keeping nights calm (lights down low, voice quiet, no play) so your "
   f"baby learns night is different from day.\n\nDo this: tonight, set a dim lamp by the feeding chair and talk softly.\n\nThe catch: it takes "
   f"time. Days bright and busy help too.\n\n{NOT_MED}\n\n#newborn #nightfeeds #newparents #babysleep #parenting",
   "Source: NHS, Helping your baby to sleep (nhs.uk): at night keep the lights down low, don't talk much, keep your voice quiet, don't play.")

reel("lf-reel-1018-breathe", LF, "2026-10-18T19:00", "tip", "lf-x-tiny-parade", "it's ok to put baby down safely", [
    dict(k="hook", f="butter", text="Crying / won't stop? / *Step away.*", emo="🧺"),
    dict(k="say", f="cream", text="Baby in the crib, / *on their back.*"),
    dict(k="because", f="pink", text="It's OK to *walk away* / once baby is safe."),
    dict(k="list", f="berry", items=["*1* Safe place", "*2* Step out, breathe", "*3* Go back calmer"], drop=True),
    dict(k="do", f="cream", text="Today, save *one number* / you can call / when it's too much."),
    dict(k="save", f="butter", text="never shake a baby."),
], f"When the crying won't stop, it's OK to step away.\n\nWhy it works: the NHS ICON advice says put your baby in a safe place and walk away "
   f"if the crying is getting to you. Calm down, then go back and check.\n\nDo this: today, save one number you can call when it's too much.\n\n"
   f"The catch: never, ever shake a baby.\n\n{NOT_MED}\n\n#newborn #crying #newparents #postpartum #parenting",
   "Source: NHS ICON programme (Infant crying is normal; Comforting methods; It's OK to walk away; Never shake a baby), Royal Wolverhampton NHS Trust leaflet.")

reel("lf-reel-1019am-hunger-cues", LF, "2026-10-19T08:00", "keep", "lf-x-sunny-bounce", "save this for the first feeds", [
    dict(k="hook", f="pink", text="Crying is / a *late* / hunger sign", emo="🌙"),
    dict(k="say", f="cream", text="Feed on the / *early cues.*"),
    dict(k="because", f="butter", text="A crying baby / is *harder to settle* / to feed."),
    dict(k="list", f="berry", items=["*1* Stirring", "*2* Mouth opening", "*3* Rooting"], drop=True),
    dict(k="do", f="cream", text="Next feed, watch for / *rooting* or a / *mouth opening.* Feed then."),
    dict(k="save", f="pink", text="save this for / the first feeds"),
], f"Keep this for the first feeds: crying is a late hunger sign.\n\nWhy it works: NHS infant-feeding guidance lists early cues (stirring, mouth "
   f"opening, rooting) and puts crying as the last signal.\n\nDo this: next feed, watch for rooting or a mouth opening, and feed then.\n\n"
   f"The catch: missed them? Every parent does. Calm baby first, then feed.\n\n{NOT_MED}\n\n#newborn #breastfeeding #feeding #newparents #babytips",
   "Source: NHS Norfolk & Waveney infant feeding, Feeding cues (early: stirring, mouth opening, turning head / rooting; late: crying).")

reel("lf-reel-1019-sick-day-plan", LF, "2026-10-19T19:00", "tip", "lf-x-tiny-parade", "save this before cold season", [
    dict(k="hook", f="cream", text="First cold coming? / *Plan now.*", emo="🤧"),
    dict(k="say", f="pink", text="Up to *8 to 10 colds* / before age 2.", size=150),
    dict(k="because", f="butter", text="A plan made *now* / beats one made / *at 7 am.*"),
    dict(k="list", f="berry", items=["Day 1 · *who?*", "Day 2 · *who?*", "Backup · *who?*"], drop=True),
    dict(k="do", f="cream", text="This week, ask *one backup* / to cover a sick day. / Save their number."),
    dict(k="save", f="pink", text="save this before / cold season"),
], f"Plan the sick days before the first cold.\n\nWhy it works: the Canadian Paediatric Society says children can get as many as 8 to 10 colds "
   f"a year before age 2. A plan made now beats one made at 7 am.\n\nDo this: this week, ask one backup person to cover a sick day and save their "
   f"number.\n\nThe catch: daycare rules on fever differ. Ask yours.\n\n{NOT_MED}\n\n#daycare #workingparents #toddlers #parenting #coldseason",
   "Source: Canadian Paediatric Society, Caring for Kids, Colds in children (up to 8 to 10 colds a year before age 2).")

reel("lf-reel-1020am-movements", LF, "2026-10-20T08:00", "tip", "lf-x-giggle-pop", "send this to someone expecting", [
    dict(k="hook", f="pink", text="Movements / *changed?* / Call *now.*", emo="🧺"),
    dict(k="say", f="cream", text="Don't wait / *until tomorrow.*"),
    dict(k="because", f="butter", text="The NHS says / *call immediately,* / any time."),
    dict(k="list", f="berry", items=["Moving *less*", "Not moving", "Pattern *changed*"], drop=True),
    dict(k="do", f="cream", text="Today, save your / *maternity unit's number* / in your phone."),
    dict(k="save", f="pink", text="send this to / someone expecting"),
], f"Baby's movements changed? Call now, not tomorrow.\n\nWhy it works: NHS maternity guidance says contact your midwife or maternity unit "
   f"immediately if movements slow, stop or change, day or night.\n\nDo this: today, save your maternity unit's number in your phone.\n\n"
   f"The catch: it's never a bother. Maternity units take calls day and night.\n\n{NOT_MED}\n\n#pregnancy #babymovements #pregnant #thirdtrimester #midwife",
   "Source: NHS, Cambridge University Hospitals, Reduced fetal movements: contact the midwives immediately; please do not wait until the next day.")

reel("lf-reel-1020-visitors", LF, "2026-10-20T19:00", "suggestion", "lf-x-sunny-bounce", "send this to the group chat", [
    dict(k="hook", f="cream", text="Visiting a / new baby? / *Come well.*", emo="🫶"),
    dict(k="say", f="pink", text="Unwell, or *cold sore?* / Send love / *by text.*"),
    dict(k="because", f="butter", text="A cold sore virus / can be *serious* / for a baby."),
    dict(k="list", f="berry", items=["*Wash hands* first", "No *kisses*", "Ill? *Not today*"], drop=True),
    dict(k="do", f="cream", text="Today, text your visitors: / *“Wash hands, no kisses, / come when well.”*"),
    dict(k="save", f="pink", text="send this to / the group chat"),
], f"Visiting a new baby? Come well.\n\nWhy it works: NHS advice says the cold sore virus can be mild in adults but life-threatening in babies. "
   f"Wash hands before touching a baby, and don't visit if you're ill.\n\nDo this: today, text your visitors: \"Wash hands, no kisses, come when well.\"\n\n"
   f"The catch: it can feel awkward. Blame the NHS.\n\n{NOT_MED}\n\n#newborn #newparents #visitors #babysafety #parenting",
   "Source: Gloucestershire Hospitals NHS, Keeping your baby safe: Think Hands And No Kisses (THANKS).")

# ======================================================================================================== STORY CHAINS
CHAINS = {}
CHAIN_TIMES = {
    FF: ["11:00", "11:15", "11:30", "11:45", "12:15"],
    LH: ["11:45", "12:00", "12:15", "12:45"],
    HB: ["12:00", "12:15", "12:30", "12:45", "13:15"],
    LF: ["10:30", "10:45", "11:00", "11:15", "11:45"],
}


def chain(cid, brand, day, photo, series, frames, times=None):
    CHAINS[cid] = dict(brand=brand, day=day, photo=photo, series=series, frames=frames,
                       times=times or CHAIN_TIMES[brand][:len(frames) - 1] + [CHAIN_TIMES[brand][-1]])


# ---- Fully Funded: "Money moves" (Day 1 is the rebuilt "Ask your lender" chain)
chain("ff-ch-1018", FF, "2026-10-18", "ff18", "money moves · day 1/4", [
    dict(k="photo", text="“Can you lower / my *rate?*”", sub="the call that *pays you back*", ink="dark", y=560),
    dict(k="bubbles", f="lite", label="why asking works", bubbles=[
        ("in", "do card companies really lower rates?"), ("out", "84% of people who asked last year *got one.*"),
        ("out", "the average cut: *6.3 points.*")], obj="point"),
    dict(k="bubbles", f="cob", label="the exact words · screenshot this", bubbles=[
        ("out", "Hi, I've been a customer since [year]."), ("out", "Can you *lower my rate?*"), ("out", "What's the best you can do?")], obj="phone"),
    dict(k="payoff", f="coral", label=f"${K['card_bal']:,} balance, one year", text=f"20% → 14%: / *${K['card_cut']} less* / interest",
         sub="realistic: the average cut was 6.3 points", obj="piggy"),
    dict(k="handoff", f="lite", text="Rate call: / *the full breakdown*", img="ff-1018-rate-call/01.jpg", next="day 2 tomorrow"),
])
chain("ff-ch-1019", FF, "2026-10-19", "ff19", "money moves · day 2/4", [
    dict(k="photo", text="“It was *on sale,* / though.”", sub="why it *costs more* →", ink="light", y=640),
    dict(k="bubbles", f="lite", label="the price isn't the price", bubbles=[
        ("in", "it was only $60!"), ("out", "how many times will you wear it?"), ("in", "maybe 6?"), ("out", "that's *$10 a wear.*")]),
    dict(k="payoff", f="cob", label="the rich habit", text="$240 coat, / 120 wears: / *$2 a wear.*", sub="price ÷ uses. screenshot this.", obj="ok"),
    dict(k="handoff", f="coral", text="Rich Habits, / *Decoded no.1*", img="ff-1019-rich-habits-01/01.jpg", next="day 3 tomorrow"),
])
chain("ff-ch-1020", FF, "2026-10-20", "ff20", "money moves · day 3/4", [
    dict(k="photo", text="“I'll invest / *when I'm older.*”", sub="same $10,000, *two homes* →", ink="light", y=760),
    dict(k="bubbles", f="lite", label="age 30, $10,000", bubbles=[
        ("out", "in a 0% account until 60:"), ("out", "*$10,000.*"), ("in", "and invested?"), ("out", "at 10% a year: *tap →*")]),
    dict(k="payoff", f="cob", label="at 60, left alone", text=f"*${K['k10_10']:,}*", sub="growth on growth. not guaranteed.", obj="piggy"),
    dict(k="handoff", f="coral", text="Where your money / *sleeps*", img="ff-1020-pick-its-home/01.jpg", next="day 4 tomorrow"),
])
chain("ff-ch-1021", FF, "2026-10-21", "ff21", "money moves · day 4/4", [
    dict(k="photo", text="“Do we even / *qualify?*”", sub="a *$2,000* bond for your kid →", ink="dark", y=640),
    dict(k="bubbles", f="lite", label="canada learning bond", bubbles=[
        ("in", "is the $2,000 bond real?"), ("out", "yes. *$500* first, then *$100* a year."), ("out", "no deposit. you just need an *RESP.*")]),
    dict(k="payoff", f="cob", label="who qualifies · 1 to 3 kids", text="Family income / *$57,375* / or less", sub="born 2004 or later", obj="point"),
    dict(k="handoff", f="coral", text="Do you / *qualify?*", img="ff-1021-clb-who-qualifies/01.jpg", next="money moves · done"),
])

# ---- Locked Hour: "Lock-in week"
chain("lh-ch-1018", LH, "2026-10-18", "lh18", "lock-in week · day 1/3", [
    dict(k="photo", text="“I'll start / *Monday.*”", sub="or tomorrow. *here's why* →", ink="light", y=1150),
    dict(k="bubbles", f="cream", label="the fresh start effect", bubbles=[
        ("in", "missed a whole week again"), ("out", "then tomorrow is a *clean page.*"),
        ("out", "gym visits rose *33%* at the start of a week."), ("out", "Dai, Milkman & Riis, 2014")], obj="clock"),
    dict(k="payoff", f="pink", label="restart smaller", text="One hour. / *Not a routine.*", sub="screenshot this", obj="clock"),
    dict(k="handoff", f="dots", text="Day 1, again? / *Make it stick*", img="lh-w2-05-restart/01.jpg", next="day 2 tomorrow"),
])
chain("lh-ch-1019", LH, "2026-10-19", "lh19", "lock-in week · day 2/3", [
    dict(k="photo", text="“Where did / *the year* go?”", sub="*90 hours* by Jan 16 →", ink="light", y=760),
    dict(k="bubbles", f="cream", label="why one hour works", bubbles=[
        ("out", "plans with a *when + where*"), ("out", "get done more often."), ("out", "94 tests. a medium-to-large effect."),
        ("in", "so… pick the hour?")], obj="clock"),
    dict(k="payoff", f="pink", label="lock-in 90", text="*90 hours* / by Jan 16", sub="comment IN on today's post", obj="hourglass"),
    dict(k="handoff", f="dots", text="Day 1 / *is today*", img="lh-w2-08-lockin-kickoff/01.jpg", next="day 3 tomorrow"),
])
chain("lh-ch-1020", LH, "2026-10-20", "lh20", "lock-in week · day 3/3", [
    dict(k="photo", text="“Just checking / *one thing.*”", sub="40 minutes later →", ink="dark", y=1300),
    dict(k="bubbles", f="cream", label="attention residue", bubbles=[
        ("in", "why is one hour so hard?"), ("out", "every switch leaves *attention behind.*"), ("out", "Leroy, 2009")], obj="hourglass"),
    dict(k="payoff", f="pink", label="the clock", text="0:00 *Wi-Fi off* / 0:45 stop / 0:50 *walk*", sub="screenshot this", obj="clock"),
    dict(k="handoff", f="dots", text="One hour, / *minute by minute*", img="lh-w2-07-minute-by-minute/01.jpg", next="lock-in week · done"),
])

# ---- Hourback: "AI evenings"
chain("hb-ch-1018", HB, "2026-10-18", "hb18", "ai evenings · day 1/4", [
    dict(k="photo", text="“Same price / as *last year.*”", sub="what *else* changed? →", ink="dark", y=560),
    dict(k="bubbles", f="indi", label="the move", bubbles=[
        ("in", "renewal letter came. looks the same."), ("out", "paste last year's *next to* this year's."), ("out", "then ask one thing →")], obj="phone"),
    dict(k="bubbles", f="yel", label="why it works", bubbles=[
        ("out", "AI only compares *what you paste.*"), ("out", "give it both years,"), ("out", "it checks line by line.")]),
    dict(k="payoff", f="plum", label="the prompt · screenshot this", text="*“List every / change.”*", sub="then: what did you leave out?", obj="point"),
    dict(k="handoff", f="indi", text="Find what your / *renewal changed*", img="hb-w02-4-renewal-changes/01.jpg", next="day 2 tomorrow"),
])
chain("hb-ch-1019", HB, "2026-10-19", "hb19", "ai evenings · day 2/4", [
    dict(k="photo", text="“Who's doing / *Thursday swim?*”", sub="two calendars, *one page* →", ink="light", y=640),
    dict(k="bubbles", f="indi", label="sunday night", bubbles=[
        ("in", "your calendar says free"), ("in", "mine says free too"), ("out", "…and the school note says *early pickup*")]),
    dict(k="bubbles", f="yel", label="the move", bubbles=[
        ("out", "paste *both calendars* + the note."), ("out", "ask it to *flag every clash.*"), ("out", "it lines them up side by side.")], obj="phone"),
    dict(k="payoff", f="plum", label="it found", text="Nobody free / for *Thursday swim.*", sub="made up for this post", obj="ok"),
    dict(k="handoff", f="indi", text="12 weeks, / *12 automations*", img="hb-w02-8-12-automations-kickoff/01.jpg", next="day 3 tomorrow"),
])
chain("hb-ch-1020", HB, "2026-10-20", "hb20", "ai evenings · day 3/4", [
    dict(k="photo", text="“What's for / *dinner* tonight?”", sub="*5 nights,* one prompt →", ink="dark", y=500),
    dict(k="bubbles", f="indi", label="why one prompt works", bubbles=[
        ("out", "give it the *rules:*"), ("out", "30 minutes, foods you skip,"), ("out", "what's in the fridge."), ("in", "less editing after")]),
    dict(k="bubbles", f="yel", label="you get", bubbles=[
        ("out", "*5 dinners*"), ("out", "*one* shopping list"), ("out", "grouped *by aisle*")], obj="phone"),
    dict(k="payoff", f="plum", label="prompt of the week · no.1", text="Shop / *once.*", sub="the full prompt is in today's post", obj="point"),
    dict(k="handoff", f="indi", text="5 dinners, / *one list*", img="hb-1020-prompt-week-01/01.jpg", next="day 4 tomorrow"),
])
chain("hb-ch-1021", HB, "2026-10-21", "hb21", "ai evenings · day 4/4", [
    dict(k="photo", text="“Just split it / *evenly?*”", sub="Ana didn't drink →", ink="light", y=700),
    dict(k="bubbles", f="indi", label="$96 dinner, 4 people", bubbles=[
        ("in", "Ana didn't drink"), ("out", "split it *and show the math*")], obj="chat"),
    dict(k="bubbles", f="yel", label="the answer", bubbles=[
        ("ai", "Ana: *$18*"), ("ai", "everyone else: *$26*"), ("ai", "18 + 26 + 26 + 26 = *96*")]),
    dict(k="payoff", f="plum", label="why it works", text="Shown math / is *checkable* / math.", sub="add it up yourself", obj="ok"),
    dict(k="handoff", f="indi", text="AI said / *what?*", img="hb-1021-ai-said-what-bill/01.jpg", next="ai evenings · done"),
])

# ---- Littlefold: "Night shift"
chain("lf-ch-1018", LF, "2026-10-18", "lf18", "night shift · day 1/3", [
    dict(k="photo", text="“Who's up / *at 2 am?*”", sub="split it, *both sleep* →", ink="light", y=620),
    dict(k="bubbles", f="cream", label="the nhs says", bubbles=[
        ("out", "rest when *baby rests.*"), ("out", "ask your partner *to help.*")], obj="shoe"),
    dict(k="bubbles", f="pink", label="the move", bubbles=[
        ("in", "you take till 2?"), ("out", "deal. then *you're off.* fully off."), ("in", "earplugs in the spare room")]),
    dict(k="payoff", f="butter", label="tonight", text="Agree a / *swap time.*", sub="write it on the fridge", obj="clock"),
    dict(k="handoff", f="cream", text="Split / *the night*", img="lf-04-sleep-when-baby-sleeps/01.jpg", next="day 2 tomorrow"),
])
chain("lf-ch-1019", LF, "2026-10-19", "lf19", "night shift · day 2/3", [
    dict(k="photo", text="“What can / *I* do?”", sub="partners, *this one's yours* →", ink="dark", y=560),
    dict(k="bubbles", f="cream", label="the nhs says", bubbles=[
        ("out", "partners can help with *nappies,*"), ("out", "*dressing* and *feeds*"), ("out", "so the feeding parent gets back to sleep.")], obj="ok"),
    dict(k="bubbles", f="pink", label="pick 2 tonight", bubbles=[
        ("out", "bring baby to the feed"), ("out", "take the *after-feed*"), ("out", "take a *night shift*")]),
    dict(k="payoff", f="butter", label="week one", text="Own *5 jobs.* / Start with *2.*", sub="send this to your partner", obj="point"),
    dict(k="handoff", f="cream", text="Own *5 jobs* / in week 1", img="lf-05-partner-week-one/01.jpg", next="day 3 tomorrow"),
])
chain("lf-ch-1020", LF, "2026-10-20", "lf20", "night shift · day 3/3", [
    dict(k="photo", text="“Not in the / *cereal aisle…*”", sub="*calmer* meltdowns →", ink="light", y=1050),
    dict(k="bubbles", f="cream", label="the nhs says", bubbles=[
        ("in", "should I just give her the biscuit?"), ("out", "giving in teaches *tantrums work.*"), ("out", "said no? *keep it.* calmly.")], obj="ok"),
    dict(k="bubbles", f="pink", label="before it starts", bubbles=[
        ("out", "keep the shop *short*"), ("out", "give them *one job*"), ("out", "point at *something interesting*")]),
    dict(k="payoff", f="butter", label="next shop", text="“Find the / *bananas.*”", sub="one job, short trip", obj="shoe"),
    dict(k="handoff", f="cream", text="Calmer / *meltdowns*", img="lf-06-toddler-meltdown/01.jpg", next="night shift · done"),
])

# Feed posts keep their slots; Story chains hand off to the noon post. Ids that leave the queue (cadence: weak format/slot):
DROPPED = {
    "ff-w03-3-guardian-will": "replaced by the rate-call Learning post (the 'Ask your lender' chain needed a target); moved to backlog",
    "ff-1018-single-24-hours": "FF singles 5 reach vs carousels 9 (cadence: 1 feed post)",
    "ff-1019-single-average-saver": "FF singles weak (cadence: 1 feed post)",
    "ff-1020-single-money-date": "FF singles weak (cadence: 1 feed post)",
    "lh-1018-single-finger-down": "LH singles 5 vs carousels 7 (cadence: 1 feed post)",
    "lh-1019-single-kitchen-table": "LH singles weak (cadence: 1 feed post)",
    "lh-1020-single-midterm": "LH singles weak (cadence: 1 feed post)",
    "ff-reel-1018-the-door": "from-birth horizon breaks §13.7; replaced by ff-reel-1018-start-28",
}

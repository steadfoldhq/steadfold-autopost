"""Hourback content, Oct 18-21. ONE-READ rewrite (Oct 17 night, see /home/claude/one-read-standard.md).
Each item: a real moment -> why AI helps (plain words) -> where not to trust it -> one thing to do today.
Uses post()/reel()/chain() from specs_teach. Only this page's entries live here."""
from specs_teach import post, reel, chain, FF, HB, LH, LF, NG, NOT_MED, MADE, PRIV, K  # noqa: F401

# ================================================================== Oct 18
post("hb-w02-4-renewal-changes", HB, "2026-10-18T13:00", "learning",
     dict(lay="pills", f="plum", kicker="ai evenings · day 1/4", text="The price / didn't change. / *Something else did.*", obj="phone", at="br",
          save="it hides in the pages you skip"),
     [dict(k="say", f="indi", label="the part nobody checks", size=118,
           text="Same price / as last year? / You skip the / other 11 pages. / But *your cover* / can quietly change."),
      dict(k="why", f="plum", label="why AI helps", size=124,
           text="Give AI both letters. / It lists / *what's different.* / But it can / *miss a line.*",
           sub="ask your insurer what a change means"),
      dict(k="do", f="yel", text="When your renewal comes, paste last year's letter and this one into AI and ask: *“What changed?”*",
           save="send this to whoever handles the insurance")],
     "Same price as last year doesn't mean nothing changed.\n\n"
     "A renewal can keep the price and still change what you're covered for. Those changes sit in the pages most of us skip.\n\n"
     "Why AI helps: give it last year's letter and this year's, and it lists what's different. Like spot-the-difference, for paperwork.\n\n"
     "Do this: when your renewal comes, paste both letters into AI and ask \"What changed?\" Take your policy number and address out first.\n\n"
     "Where not to trust it: it can miss a line, and it can't tell you what a change means for you. Check each change in the letters, "
     "and ask your insurer about anything that matters.\n\n"
     "Send this to whoever handles the insurance in your house.\n\n#aitips #insurance #lifeadmin #renewal #moneytips",
     "How it works: chat AIs answer from the text in the conversation, so pasting both letters gives them something real to compare. "
     "They can still skip or misread a line, so check every change against the letters and ask your insurer what it means for you.")

post("hb-1018-single-before-paste", HB, "2026-10-18T17:45", "keep",
     dict(lay="mosaic", f="indi", text="“What you paste / into AI leaves / your phone.”", obj="chat", at="bl",
          save="here's a 10-second habit"),
     [dict(k="say", f="yel", label="here's why", size=120,
           text="Most AI apps send / what you type to the / *company's computers.* / Names and numbers / *included.*"),
      dict(k="do", f="indi", text="Before you paste, swap real names for *“Sam”* and account numbers for *“1234”.* AI still gets it.",
           save="send this to the friend who pastes everything")],
     "Everything you paste into an AI chat leaves your phone.\n\n"
     "Most AI chat apps send what you type to the company's computers to work out the answer. So the letter you paste goes too, "
     "names and numbers included.\n\n"
     "Do this: before you paste, swap real names for \"Sam\" and account numbers for \"1234\". AI still understands the letter, "
     "and your real details stay with you.\n\n"
     "Send this to the friend who pastes everything.\n\n#aitips #privacy #lifeadmin #chatgpt #techtips",
     "Also worth 2 minutes: open your AI app's settings and check whether your chats are used to train its models. "
     "Most big apps let you turn that off.")

reel("hb-reel-1018am-freeze-frame", HB, "2026-10-18T08:45", "deep", "hb-x-smart-bounce", "it's in there somewhere…", [
    dict(k="hook", f="indi", text="*147 unread* / in the / family chat.", emo="💬"),
    dict(k="say", f="yel", text="Somewhere in there / is *your job.*"),
    dict(k="ai", f="plum", text="What do I need / to do, and / by *when?*"),
    dict(k="list", f="yel", items=["Bring dessert · *Sat*", "Pick up Gran · *Sun 2 pm*"], size=104, drop=True),
    dict(k="because", f="indi", kicker="here's why it works", text="AI is great at sorting *what you give it.*"),
    dict(k="say", f="plum", text="But if Mum changed / the plan *by phone,* / AI won't know."),
    dict(k="do", f="yel", text="Paste the chat into AI and ask: *“What do I need to do?”*"),
    dict(k="save", f="indi", text="send this to / the family chat"),
], "147 unread messages in the family chat, and one of them is your job.\n\n"
   "Paste the chat into AI and ask: \"What do I need to do, and by when?\" You get your jobs back as a short list.\n\n"
   "Why it works: AI is great at sorting what you give it.\n\n"
   "Where not to trust it: it only knows what's written in the chat. If plans changed on a phone call, it won't know.\n\n"
   f"Take names and numbers out before you paste.\n\n{MADE}\n\n#familychat #aitips #lifeadmin #momlife #organization",
   "The chat in this Reel is made up; the list is from a real AI run on it.")

reel("hb-reel-1018-school-email", HB, "2026-10-18T19:00", "deep", "hb-x-ta-da-funk", "one date matters. which one?", [
    dict(k="hook", f="indi", text="The school / newsletter. / *Four pages.*", emo="💬"),
    dict(k="say", f="plum", text="And picture day / is hiding in / *paragraph six.*"),
    dict(k="because", f="yel", kicker="here's why AI helps", text="AI is quick at pulling *dates* out of long writing."),
    dict(k="list", f="indi", items=["Thu · *Picture day*", "Fri · *Pyjama day*"], size=120, drop=True),
    dict(k="say", f="yel", text="It can still / *miss one.* / Glance at the / newsletter / before you / trust the list."),
    dict(k="do", f="plum", text="Paste the newsletter into AI and ask: *“List every date, soonest first.”*"),
    dict(k="save", f="indi", text="send this to the / parents' group chat"),
], "Picture day was in paragraph six. Of course it was.\n\n"
   "Paste the school newsletter into AI and ask: \"List every date, soonest first.\" Four pages become one short list.\n\n"
   "Why it works: AI is quick at pulling dates out of long writing. It's like a highlighter that reads for you.\n\n"
   "Where not to trust it: it can still miss one. Glance at the newsletter before the dates go in your calendar.\n\n"
   f"Send this to the parents' group chat.\n\n{MADE}\n\n#schoolmom #aitips #lifeadmin #parenting #organization",
   "The newsletter shown is made up for this post.")

chain("hb-ch-1018", HB, "2026-10-18", "hb18", "ai evenings · day 1/4", [
    dict(k="photo", text="“Same price as / *last year!*”", sub="but did anything else change? →", ink="dark", y=560),
    dict(k="bubbles", f="indi", label="sound familiar?", bubbles=[
        ("in", "insurance renewal came. *same price as last year* 🙌"), ("out", "did you read the other eleven pages?"), ("in", "…no")],
     obj="phone"),
    dict(k="bubbles", f="yel", label="here's the trick", bubbles=[
        ("out", "paste last year's letter and this year's into AI"), ("out", "ask it: *what changed?*"),
        ("ai", "Here are the 3 things that are different…")]),
    dict(k="payoff", f="plum", label="but don't trust it blindly", text="It can *miss* / a line.",
         sub="check each change, ask your insurer about it", obj="point", tap="next story →"),
    dict(k="handoff", f="indi", text="The price didn't change. / *Something else did.*", img="hb-w02-4-renewal-changes/01.jpg",
         next="day 2 tomorrow"),
])


# ================================================================== Oct 19
reel("hb-reel-1019am-just-the-asks", HB, "2026-10-19T08:45", "deep", "hb-x-future-easy", "what do they actually want?", [
    dict(k="hook", f="indi", text="A huge email / from your boss. / *Before coffee.*", emo="📧"),
    dict(k="say", f="plum", text="Somewhere in / there are the / *three things* / they need / from you."),
    dict(k="ai", f="yel", text="What do they / need from me? / *Quote the line.*"),
    dict(k="list", f="indi", items=["The slides · *Tue*", "The budget · *Fri*", "Lunch · *optional*"], size=104, drop=True),
    dict(k="because", f="plum", kicker="why ask for the quote?", text="AI sometimes guesses. A quote proves *it's really in there.*"),
    dict(k="do", f="yel", text="Next long email, ask AI what they need from you, and to *quote the line.*"),
    dict(k="save", f="indi", text="send this to / the long-email coworker", next="part 2 tonight: your reply →"),
], "A huge email from your boss, before coffee. What do they actually need from you?\n\n"
   "Paste it into AI and ask: \"What do they need from me? Quote the line.\" You get the asks as a short list.\n\n"
   "Why the quote matters: AI sometimes fills gaps with guesses. A quote shows you it's really in the email, and you can find it in seconds.\n\n"
   "Where not to trust it: if it can't quote a line, treat that ask as a guess. And check your work's rules before you paste work email into any AI.\n\n"
   f"Part 2 tonight: writing your reply.\n\nSend this to the long-email coworker.\n\n{MADE}\n\n#inbox #aitips #email #productivity #worklife",
   "The email shown is made up for this post. Many workplaces have rules about which AI tools you can use with work email; check yours first.")

chain("hb-ch-1019", HB, "2026-10-19", "hb19", "ai evenings · day 2/4", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="indi", label="quick quiz", title="Moms with a partner: / who runs the *kids' calendar?*", bubbles=[
        ("in", "how many say it's mostly them?"), ("out", "A) about half"),
        ("out", "B) about 8 in 10")], tap="guess, then tap →"),
    dict(k="payoff", f="yel", label="the answer: B", text="*78%*", sub="of moms say it's mostly them", obj="phone",
         tap="source: Pew Research Center, 2023 · tap →"),
    dict(k="payoff", f="plum", label="why it matters", text="That's a lot of / calendar in *one head.*", sub="let AI spot the clashes for you",
         obj="point", tap="next story →"),
    dict(k="handoff", f="indi", text="Who's doing / *Thursday swim?*", img="hb-w02-8-12-automations-kickoff/01.jpg", next="day 3 tomorrow"),
])

post("hb-w02-8-12-automations-kickoff", HB, "2026-10-19T13:00", "learning",
     dict(lay="pills", f="indi", kicker="ai evenings · day 2/4", text="Who's doing / *Thursday swim?*", obj="phone", at="br",
          save="nobody, it turns out"),
     [dict(k="say", f="yel", label="sunday night, every week", size=126,
           text="Your calendar / says free. / So does theirs. / Then the school note: / *early pickup.*"),
      dict(k="why", f="plum", label="why AI is good at this", size=126,
           text="Paste both calendars / and the note. / AI lines up the days, / so *clashes jump out.*"),
      dict(k="say", f="indi", label="it found", size=130,
           text="Nobody's free for / *Thursday swim.* / Better to know Sunday / than 4 pm Thursday."),
      dict(k="say", f="yel", label="but double-check", size=130,
           text="AI can mix up / *am and pm.* / Check what it flags / in the real calendars."),
      dict(k="do", f="plum", text="Sunday night, paste both calendars into AI and ask: *“Where do we clash this week?”*",
           save="send this to the other half of your calendar")],
     "Who's doing Thursday swim? Nobody, it turns out.\n\n"
     "Your calendar says free. Theirs says free. Then the school note says early pickup on Thursday.\n\n"
     "Why AI helps: paste both calendars and the note, and it lines everything up by day, so the clashes jump out.\n\n"
     "Do this: Sunday night, paste both calendars into AI and ask \"Where do we clash this week?\"\n\n"
     "Where not to trust it: AI can mix up times, or am and pm. Check anything it flags against the real calendars. "
     "Take out addresses and the kids' full names before you paste.\n\n"
     f"Send this to the other half of your calendar.\n\n{MADE}\n\n#aitips #familycalendar #lifeadmin #momlife #organization",
     "The week shown is made up for this post. AI tools can misread times and time zones, so treat its list as a starting point and check "
     "the calendars. Story quiz: Pew Research Center (May 2023, survey fall 2022): among U.S. mothers living with a spouse or partner and "
     "children under 18, 78% say they do more than their partner managing their children's schedules and activities.")

# Oct 19, 17:45 · was a 3-slide single; now a 7-slide carousel (singles are weakest everywhere)
post("hb-1019-single-homework", HB, "2026-10-19T17:45", "keep",
     dict(lay="pills", f="yel", text="Grade 5 math. / *I can't* / *do it anymore.*", obj="chat", at="tr", save="you're not the only one"),
     [dict(k="say", f="plum", label="sound familiar?", size=132,
           text="7 pm. Homework. / Your kid asks *“why?”* / and you have / *no idea.* 😅"),
      dict(k="say", f="indi", size=132,
           text="You could just / look up the answer. / But then *they* / still don't get it."),
      dict(k="why", f="yel", label="here's the trick", size=132,
           text="Ask AI to explain / the steps *like* / *they're 10.* / Then *you* explain it."),
      dict(k="say", f="plum", label="the magic words", size=128,
           text="“Explain it like / I'm 10. / *Don't tell me* / *the answer.*”"),
      dict(k="say", f="indi", label="but don't trust it blindly", size=132,
           text="AI can get / math *wrong.* / So check the answer / *together.*"),
      dict(k="do", f="yel", text="Tonight, paste one homework question into AI and ask: *“Explain it like I'm 10. No answer.”*",
           save="send this to a homework-night parent")],
     "Grade 5 math. You can't do it anymore either? Same.\n\n"
     "You could look up the answer, but then your kid still doesn't get it. Instead, paste the question into AI and ask it to explain "
     "the steps like you're 10, without giving the answer. Now you can explain it to your kid instead of guessing.\n\n"
     "Where not to trust it: AI can get math wrong. Use it for the steps, then check the answer together, "
     "or against the answer key if there is one.\n\n"
     "Do this: tonight, paste one homework question into AI and ask \"Explain it like I'm 10. No answer.\"\n\n"
     "Send this to a homework-night parent.\n\n#homework #aitips #parenting #schoollife #momlife",
     "AI chatbots can make arithmetic and reasoning mistakes, so check the final answer yourself. Asking it to hide the answer keeps the thinking with your kid.")

reel("hb-reel-1019-one-sorry", HB, "2026-10-19T19:00", "deep", "hb-x-smart-bounce", "count them…", [
    dict(k="hook", f="indi", text="Part 2: / your reply has / *four sorries.*", emo="🙇"),
    dict(k="say", f="yel", text="Sorry for the / delay. / *Sorry, sorry,* / *sorry.*"),
    dict(k="because", f="plum", kicker="here's the trick", text="Tell AI to *keep your words,* or it rewrites you into a robot."),
    dict(k="say", f="yel", text="Now there's / *one sorry,* / and it still / sounds like you.", drop=True),
    dict(k="say", f="plum", text="Read it out / loud. If a line / isn't you, / *change it back.*"),
    dict(k="do", f="indi", text="Paste your draft into AI and ask: *“Keep my words. Say sorry once.”*"),
    dict(k="save", f="plum", text="send this to the friend / who over-apologises", next="tomorrow: the awkward text"),
], "Part 2 of this morning's Reel: now you're writing the reply, and it has four sorries in it. Count them.\n\n"
   "Paste your draft into AI and ask: \"Keep my words. Say sorry once.\" You get the same message, with one sorry, still in your voice.\n\n"
   "Why \"keep my words\" matters: without it, AI tends to rewrite the whole thing in its own voice.\n\n"
   "Where not to trust it: read it out loud before you send. If a line doesn't sound like you, change it back.\n\n"
   f"Calm replies, part 1 of 2. Part 2 tomorrow.\n\nSend this to the friend who over-apologises.\n\n{MADE}\n\n"
   "#email #aitips #communication #worklife #writing",
   "The email shown is made up for this post.", series="Calm replies · part 1/2")

# ================================================================== Oct 20
reel("hb-reel-1020am-driveway-text", HB, "2026-10-20T08:45", "deep", "hb-x-future-easy", "deep breath…", [
    dict(k="hook", f="indi", text="7:52 am. / A text from / *your neighbour.*", emo="💬"),
    dict(k="say", f="yel", text="Your guest / *blocked their* / *driveway.* / Again."),
    dict(k="because", f="plum", kicker="here's the trick", text="Give AI a *word limit.* Short replies sound calm. Long ones sound guilty."),
    dict(k="say", f="indi", text="It wrote / one sorry and / a promise: / *car moved by 8.*", drop=True),
    dict(k="say", f="yel", text="Change any / word *you* / *wouldn't say.* / It's still / your text."),
    dict(k="do", f="indi", text="Paste the text into AI and ask for a *calm reply under 40 words.*"),
    dict(k="save", f="plum", text="send this to the friend / who over-explains", next="calm replies · 2/2"),
], "7:52 am. A text from your neighbour: your guest blocked their driveway. Again.\n\n"
   "Paste the text into AI and ask for a calm reply under 40 words. You get one sorry and a plan, not a paragraph.\n\n"
   "Why the word limit works: short replies sound calm. Long ones sound guilty.\n\n"
   "Where not to trust it: it's still your text. Change any word you wouldn't say, and take names out before you paste.\n\n"
   f"Calm replies, part 2 of 2.\n\nSend this to the friend who over-explains.\n\n{MADE}\n\n"
   "#neighbours #aitips #communication #texting #lifeadmin",
   "The text shown is made up for this post.", series="Calm replies · part 2/2")

chain("hb-ch-1020", HB, "2026-10-20", "hb20", "ai evenings · day 3/4", [
    dict(k="photo", text="“What's for / *dinner?*”", sub="asked every night at 5 pm →", ink="dark", y=500),
    dict(k="bubbles", f="indi", label="every single night", bubbles=[
        ("in", "what's for dinner?"), ("out", "there's half a chicken and some spinach"), ("in", "so… *pizza?*")]),
    dict(k="bubbles", f="yel", label="here's the trick", bubbles=[
        ("out", "tell AI what's in the fridge"), ("out", "ask for *5 dinners and one shopping list*"),
        ("ai", "Monday: chicken and spinach rice, 25 min…")], obj="phone"),
    dict(k="payoff", f="plum", label="but check this yourself", text="It doesn't know / *allergies.*",
         sub="tell it, then read every ingredient", obj="point", tap="next story →"),
    dict(k="handoff", f="indi", text="5 pm. / *What's for dinner?*", img="hb-1020-prompt-week-01/01.jpg", next="day 4 tomorrow"),
])

post("hb-1020-prompt-week-01", HB, "2026-10-20T13:00", "learning",
     dict(lay="sticky", f="indi", kicker="ai evenings · day 3/4", text="5 pm. / *What's for dinner?*", obj="point", at="bl",
          items=["Half a chicken", "Rice", "Spinach", "Two picky kids"], save="the fridge, honestly"),
     [dict(k="say", f="yel", label="every single night", size=130,
           text="5 pm. / Everyone's hungry. / You stare at / the fridge like it / *owes you an answer.*"),
      dict(k="why", f="plum", label="why it works", size=130,
           text="Tell AI what's in / the fridge and / who eats what. / *It plans around that.*"),
      dict(k="say", f="indi", label="and you get", size=136,
           text="*Five dinners* and / *one shopping list.* / You shop once. 🙌"),
      dict(k="say", f="yel", label="but check this yourself", size=130,
           text="AI won't know about / *allergies* unless / you tell it. / Read every ingredient."),
      dict(k="do", f="plum", text="Tonight, tell AI what's in your fridge and ask for *5 easy dinners and one shopping list.*",
           save="send this to whoever cooks at your place")],
     "5 pm. What's for dinner? Again.\n\n"
     "Tell AI what's in the fridge, who eats what, and how much time you have. It plans around your rules: five dinners and one "
     "shopping list, sorted by aisle. You shop once.\n\n"
     "Do this: tonight, tell AI what's in your fridge and ask \"Plan 5 easy dinners and one shopping list.\"\n\n"
     "Where not to trust it: AI doesn't know about allergies unless you tell it, and it can still make mistakes. Read every ingredient, "
     "and check the cupboards before you shop.\n\n"
     "Send this to whoever cooks at your place.\n\n#mealplanning #aitips #dinnerideas #familydinner #lifeadmin",
     "AI meal plans only know what you tell them. For allergies, always read the ingredients yourself; AI can still include something you said to avoid.")

# Oct 20, 17:45 · was a 3-slide single; now a 7-slide carousel
post("hb-1020-single-error-code", HB, "2026-10-20T17:45", "keep",
     dict(lay="pills", f="plum", text="The dishwasher / says *E24.* / *Now what?*", obj="phone", at="br", save="careful who you ask"),
     [dict(k="say", f="indi", label="sound familiar?", size=134,
           text="Beeping. Blinking. / *E24.* / You grab your phone / and ask AI."),
      dict(k="say", f="yel", label="here's the part nobody tells you", size=134,
           text="AI may *guess* / what E24 means, / and sound / *totally sure.*"),
      dict(k="why", f="plum", label="why it guesses", size=134,
           text="The same code / can mean *different* / *things* on / different brands."),
      dict(k="say", f="indi", label="the fix", size=134,
           text="Give AI / *your manual.* / Now it's reading, / not guessing. 📖"),
      dict(k="say", f="yel", label="no paper manual?", size=134,
           text="Search your / *model number* online. / Most brands post / the manual."),
      dict(k="do", f="plum", text="Snap the error-code page in your manual. Give it to AI and ask: *“What do I do first?”*",
           save="send this to the family fixer")],
     "The dishwasher says E24. Now what?\n\n"
     "Here's the part nobody tells you: ask AI what an error code means and it may guess, while sounding totally sure. "
     "The same code can mean different things on different brands.\n\n"
     "The fix: give it your manual. Take a photo of the error-code page, give it to AI, and ask what to do first. Now it's reading "
     "your manual, not guessing. No paper manual? Most brands have it online if you search the model number.\n\n"
     "Unplug it before you touch anything inside.\n\nSend this to the family fixer.\n\n#homehacks #aitips #lifeadmin #appliances #techtips",
     "Error codes differ by brand and model, and AI can state a wrong meaning confidently. Giving it your own manual page keeps the answer tied to your machine.")

reel("hb-reel-1020-three-tabs", HB, "2026-10-20T19:00", "deep", "hb-x-ta-da-funk", "they all look the same…", [
    dict(k="hook", f="indi", text="11 pm. / *Three tabs.* / Three blenders.", emo="🛒"),
    dict(k="say", f="yel", text="They all look / the same, and / you're *too tired* / *to compare.*"),
    dict(k="because", f="plum", kicker="here's the trick", text="Tell AI *how you'll use it.* Now it has a reason to pick."),
    dict(k="say", f="indi", text="Smoothies / every day? / It picked / *Blender B.* / Tabs closed.", drop=True),
    dict(k="say", f="yel", text="It can get / specs wrong. / *Check the* / *shop page* / before you pay."),
    dict(k="do", f="plum", text="Paste the three product pages into AI and ask: *“Which fits how I'll use it?”*"),
    dict(k="save", f="indi", text="send this to / the 40-tab friend"),
], "11 pm. Three tabs. Three blenders that all look the same.\n\n"
   "Paste the three product pages into AI and tell it how you'll use it. That gives it a reason to pick one.\n\n"
   "Do this: ask \"Which fits how I'll use it?\"\n\n"
   "Where not to trust it: AI can get specs wrong. Check the price and specs on the shop page before you pay.\n\n"
   f"Send this to the 40-tab friend.\n\n{MADE}\n\n#shoppingtips #aitips #kitchen #lifeadmin #techtips",
   "Products shown are made up for this post. Never paste card details into an AI chat.")

# ================================================================== Oct 21
reel("hb-reel-1021am-parcel-text", HB, "2026-10-21T08:45", "deep", "hb-x-smart-bounce", "you ARE waiting for a parcel…", [
    dict(k="hook", f="indi", text="“Your parcel is / on hold. / *Pay $1.99.*”", emo="💬"),
    dict(k="say", f="yel", text="You *are* / waiting for / a parcel. So / you almost tap."),
    dict(k="because", f="plum", kicker="here's why AI helps", text="AI has seen the *classic scam tricks,* so it spots them fast."),
    dict(k="list", f="indi", items=["A tiny *fee*", "A *rush*", "A strange *link*"], size=110, drop=True),
    dict(k="say", f="plum", text="“Looks fine” / doesn't mean / safe. *Check in* / *the courier's* / *own app.*"),
    dict(k="do", f="yel", text="Weird text? *Don't tap the link.* Screenshot it and ask AI for the red flags."),
    dict(k="save", f="indi", text="send this / to your mum"),
], "\"Your parcel is on hold. Pay $1.99.\" And you ARE waiting for a parcel.\n\n"
   "Before you tap, screenshot the text and ask AI: \"Is this a scam? What are the red flags?\" It has seen the classic tricks: "
   "a tiny fee, a rush, a strange link.\n\n"
   "Where not to trust it: if AI says it looks fine, that doesn't make it safe. Check your parcel in the courier's own app or website, "
   "never through the link.\n\n"
   f"Send this to your mum.\n\n{MADE}\n\n#scamalert #aitips #textscam #onlinesafety #lifeadmin",
   "Fake delivery texts asking for a small fee are a common scam; the Canadian Anti-Fraud Centre (antifraudcentre-centreantifraude.ca) "
   "lists them. Check deliveries only in the courier's own app or site.")

chain("hb-ch-1021", HB, "2026-10-21", "hb21", "ai evenings · day 4/4", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="indi", label="quick quiz", title="AI answering / *news questions…*", bubbles=[
        ("in", "how many answers had a big problem?"), ("out", "A) about 1 in 10"), ("out", "B) almost half")],
         tap="guess, then tap →"),
    dict(k="payoff", f="yel", label="the answer: B", text="*45%*", sub="had at least one big problem", obj="phone",
         tap="source: EBU and BBC study, Oct 2025 · tap →"),
    dict(k="payoff", f="plum", label="why it matters", text="Make AI / *show its work.*", sub="then you can check it in seconds", obj="ok",
         tap="next story →"),
    dict(k="handoff", f="indi", text="$96 dinner. / *Ana didn't drink.*", img="hb-1021-ai-said-what-bill/01.jpg", next="ai evenings · done"),
])

post("hb-1021-ai-said-what-bill", HB, "2026-10-21T13:00", "learning",
     dict(lay="mosaic", f="indi", kicker="ai evenings · day 4/4", text="“$96 dinner. / Ana didn't / drink.”", obj="chat", at="bl",
          save="so who pays what?"),
     [dict(k="say", f="yel", label="you know this moment", size=132,
           text="The bill lands. / Someone says / *“just split* / *it evenly.”* / Ana had water. 💧"),
      dict(k="say", f="plum", label="so ask AI", size=132,
           text="Tell it who / had what. Ask it to / *split it fairly* / *and show the math.*"),
      dict(k="say", f="indi", label="it said", size=140,
           text="Ana pays *$18.* / Everyone else / pays *$26.*", sub="that adds up to $96. we checked."),
      dict(k="why", f="yel", label="why show the math?", size=132,
           text="AI can get sums / *wrong.* With the math, / you can *check it* / *in 5 seconds.*"),
      dict(k="do", f="plum", text="Next shared bill, tell AI who had what and add: *“Show the math.”*",
           save="send this to the friend who always says “evenly”")],
     "$96 dinner. Ana didn't drink. Who pays what?\n\n"
     "Tell AI what everyone had and ask it to split it fairly and show the math. It said: Ana pays $18, everyone else $26. "
     "That adds up to $96.\n\n"
     "Why show the math: AI can get things wrong. When it shows its work, you can check it in 5 seconds.\n\n"
     "Do this: next shared bill, tell AI what everyone had and add \"Show the math.\"\n\n"
     f"Send this to the friend who always says \"evenly\".\n\n{MADE}\n\n#billsplit #aitips #dinnerwithfriends #lifeadmin #moneytips",
     "The bill: $72 of food split 4 ways ($18 each) and $24 of drinks split 3 ways ($8 each). Ana $18, everyone else $26. "
     "18 + 26 + 26 + 26 = 96. Chat AIs can make arithmetic mistakes, which is why you ask for the working. Story quiz: European "
     "Broadcasting Union and BBC, News Integrity in AI Assistants (Oct 2025): 45% of more than 3,000 AI answers to news questions had at "
     "least one significant issue (22 public service media organisations, 18 countries).")

# Oct 21, 17:45 · was a 3-slide single; now a 7-slide carousel
post("hb-1021-single-subscriptions", HB, "2026-10-21T17:45", "keep",
     dict(lay="sticky", f="yel", text="Charges / you *forgot* / you pay", obj="point", at="bl",
          items=["Streaming 12.99", "Cloud 2.99", "Fitness 9.99", "Phone 45.00", "News 7.50"], save="78.47 a month, made up for this post"),
     [dict(k="say", f="indi", label="sound familiar?", size=136,
           text="$12.99 here. / $2.99 there. / You *forgot* / half of them."),
      dict(k="say", f="plum", label="here's the trick", size=132,
           text="Paste one month / of your statement / into AI. Ask: / *“What repeats?”*"),
      dict(k="why", f="yel", label="why AI is good at this", size=132,
           text="Spotting the *same* / *charge every month* / is easy for AI. / Boring for you. 😴"),
      dict(k="say", f="indi", label="but don't trust it blindly", size=132,
           text="It can miss / *yearly* charges. / Scroll back a year / yourself."),
      dict(k="say", f="plum", label="before you paste", size=132,
           text="Take out *card* / *and account numbers.* / AI doesn't / need them."),
      dict(k="do", f="yel", text="Tonight, paste last month's statement into AI and ask: *“What repeats?”* Then cancel one.",
           save="send this to your money buddy")],
     "Charges you forgot you pay. Everyone has a few.\n\n"
     "Paste one month of your bank statement into AI and ask \"What repeats?\" Spotting the same charge every month is easy for AI, "
     "and boring for you.\n\n"
     "Where not to trust it: it can miss yearly charges, so scroll back through the year yourself. And take card and account numbers out "
     "before you paste.\n\n"
     "Do this: tonight, paste last month's statement into AI, ask \"What repeats?\", then cancel one you don't use.\n\n"
     f"Send this to your money buddy.\n\n{MADE}\n\n#subscriptions #aitips #budgeting #moneytips #lifeadmin",
     "The statement on the cover is made up; its five charges add up to 78.47 a month. Never paste full card or account numbers into an AI chat.")

reel("hb-reel-1021-group-costume", HB, "2026-10-21T19:00", "deep", "hb-x-ta-da-funk", "63 messages and counting…", [
    dict(k="hook", f="indi", text="6 friends. / *One group costume.* / 63 messages.", emo="💬"),
    dict(k="say", f="plum", text="Everyone has / ideas. *Nobody* / *has a plan.*"),
    dict(k="because", f="yel", kicker="here's the trick", text="Tell AI what everyone *already owns.* Then the ideas come from your closets."),
    dict(k="list", f="indi", items=["Priya · *rain*", "Theo · *cloud*", "Mila · *sun*", "Kai · *lightning*"], size=104, drop=True),
    dict(k="say", f="yel", text="It can't know / who'll actually / show up in it. / *That's what the* / *vote is for.*"),
    dict(k="do", f="plum", text="Paste the chat into AI and ask for *3 group costumes from what we own.*"),
    dict(k="save", f="indi", text="send this to / the group chat"),
], "6 friends. One group costume. 63 messages and no plan. Halloween is in 10 days.\n\n"
   "Paste the chat into AI, tell it what everyone already owns, and ask for 3 group costumes. The ideas come from your closets, "
   "not the shops. Ours: the weather.\n\n"
   "Where not to trust it: it can't know who'll actually show up in it. That's what the vote is for.\n\n"
   f"Send this to the group chat.\n\n{MADE}\n\n#halloween #groupcostume #aitips #friends #halloweencostume",
   "Names and chat made up for this post. Take real names and numbers out before you paste a group chat.")


# ------------------------------------------------------------------ AIR PASS (Oct 18 am): size each Oct 19-21 slide to its longest line,
# so forced line breaks never re-wrap (one line on screen = one line in the source).
def _fit_sizes(brand, em=0.39, cap=140, floor=88):
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



_fit_sizes(HB)

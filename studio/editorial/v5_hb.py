"""Hourback content. Oct 18: ONE-READ rewrite (Oct 17 night). Oct 19-22: "get an hour back" rebuild (Oct 18 am), see the Oct 19-22 header.
Each item: a real moment -> why AI helps (plain words) -> where not to trust it -> one thing to do today.
Uses post()/reel()/chain() from specs_teach. Only this page's entries live here."""
from specs_teach import post, reel, chain, FF, HB, LH, LF, NG, NOT_MED, MADE, PRIV, K  # noqa: F401

# ================================================================== Oct 18
post("hb-w02-4-renewal-changes", HB, "2026-10-18T13:00", "learning",
     dict(lay="pills", f="plum", kicker="ai evenings · day 1/4", text="The price / didn't change. / *Something else did.*", obj="phone", at="br",
          save="it hides in the pages you skip"),
     [dict(k="say", f="indi", label="sound familiar?", size=118,
           text="Your insurance renewal arrives. *Same price* as last year, so you file it without reading the *other eleven pages.*"),
      dict(k="say", f="yel", label="here's the part nobody checks", size=128,
           text="The price can stay the same while *what you're covered for* quietly changes."),
      dict(k="why", f="plum", label="why AI is good at this", size=120,
           text="Give AI last year's letter and this year's, and it lists *what's different.*",
           sub="like spot-the-difference, for paperwork"),
      dict(k="say", f="indi", label="but don't trust it blindly", size=118,
           text="It can *miss a line.* And it can't tell you what a change means for you. *Your insurer can.*"),
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



# ================================================================== Oct 19-25 · "AI, FOR REAL" (Oct 19, 00:30 re-plan)
# Owner, Oct 18 21:46: HOURBACK = REALLY TEACH AI. Same ids and slots as the Oct 18 rebuild; the noon posts, Story chains and
# Reels below now teach one AI idea a day (agents, hallucination, privacy, careers, how it works, prediction, AI in your apps).
# The 17:45 posts (Formats lead) are untouched. Older notes from the Oct 18 rebuild follow.
# -================================================================= Oct 19-22 · "GET AN HOUR BACK" REBUILD (Oct 18 am)
# Hourback = everyday time-savers you can set up in 2 minutes. AI is one tool among several (phone settings, email rules,
# calendar tricks, Canada life admin, AI). Each post: a time-sink moment -> the exact swap -> what you get back -> one "Do this:".
# Themes alternate post to post: plum/orng (pastel orange on cream) <-> indi/yel (purple + yellow).
# Cheat-sheet Reels live in v5_hb_cheats.py. Every path below was checked on Oct 18 (sources in each first comment).
import os as _os
from pathlib import Path as _Path
from specs_teach import DROPPED as _DROPPED, POSTS as _POSTS, META as _META

_MEDIA = _Path(__file__).resolve().parent.parent.parent / "media"
_ALL = _os.environ.get("HB_ALL") == "1"  # set by the renderer; the scheduler only sees items whose images exist


def hpost(pid, *a, **k):
    if _ALL or (_MEDIA / pid / "01.jpg").exists():
        post(pid, *a, **k)


def hchain(cid, brand, day, photo, series, frames, times=None):
    if _ALL or all((_MEDIA / "stories" / f"{cid}-{i + 1}.jpg").exists() for i in range(len(frames))):
        chain(cid, brand, day, photo, series, frames, times)


HBTAGS = "#timesaver #lifehacks #iphonetips #productivity #hourback"

# ================================================================== Oct 19 (quiz day)
# ---- "AI, FOR REAL" (Oct 19 00:30 re-plan, owner: "HOURBACK = REALLY TEACH AI"). Day 1: agents (noon) + AI at work (Reels).
# Every claim below traces to the source named in its first comment (checked Oct 19, 00:15-00:40 ET).
hchain("hb-ch-1019b", HB, "2026-10-19", "hb19", "ai, for real · quick quiz", [
    dict(k="bubbles", f="plum", label="quick quiz", title="AI agents can do / *longer jobs* each year.", bubbles=[
        ("in", "how often does that double?"), ("out", "A) every 7 years"), ("out", "B) every 7 months")],
         tap="guess, then tap →"),
    dict(k="payoff", f="orng", label="the answer: B", text="Every / *7 months.*", sub="measured across 6 years of AI models", obj="phone",
         tap="source: METR, 2025 · tap →"),
    dict(k="payoff", f="plum", label="what that means", text="From chatting / to *doing.*", sub="agents now click, scroll and fill in forms",
         obj="point", tap="next story →"),
    dict(k="handoff", f="orng", label="ai, for real · day 1", text="AI stopped talking. / *It started doing.*", img="hb-1019-text-shortcut/01.jpg",
         next="tonight: the jagged edge"),
])

hpost("hb-1019-text-shortcut", HB, "2026-10-19T13:00", "learning",
      dict(lay="pills", f="plum", kicker="ai, for real · day 1", text="AI stopped / talking. / *It started doing.*", obj="phone", at="br",
           save="here's what that means for you"),
      [dict(k="say", f="orng", label="2023", text="You typed / a question. / AI typed *an answer.* / Then it was / *your turn* again."),
       dict(k="say", f="plum", label="july 2025", text="OpenAI gave ChatGPT / *its own browser.* / It clicks, scrolls / and *fills in forms* / while you watch."),
       dict(k="say", f="orng", label="january 2026", text="Google's Chrome / *auto browse* can / book appointments / and *request quotes* / for you."),
       dict(k="rows", f="plum", text="Who's *shipping it*", cap="big tech's ai agents", rows=[
           ("OpenAI", "ChatGPT agent"), ("Google", "auto browse"), ("Anthropic", "Claude in Chrome"), ("Microsoft", "Copilot Actions")]),
       dict(k="why", f="orng", label="why it's different", text="A chatbot only / *reads your words.* / An agent *sees* / *the screen* and / picks the next click.",
            sub="like handing a helper your mouse"),
       dict(k="say", f="plum", label="how fast it's growing", text="The length of tasks / agents can finish / has *doubled* / about every / *7 months.*",
            src="METR · March 2025"),
       dict(k="say", f="orng", label="where it's heading", text="If the trend holds, / METR says agents / could do projects / that take / *a person a month* / by about 2030."),
       dict(k="catch", f="plum", text="A web page can / *hide orders* / that trick an agent. / So Google's agent / makes *you* press Buy.",
            sub="AI clicks. You press pay."),
       dict(k="do", f="orng", text="This week, give an agent *one dull errand:* compare 3 quotes. *You* press pay.",
            save="send this to someone who thinks AI just chats")],
      "AI stopped talking. It started doing.\n\n"
      "For three years, AI was a chat box: you typed, it typed back. Now the biggest companies are shipping agents, AI that "
      "opens a browser and does the clicking.\n\n"
      "July 2025: OpenAI launched ChatGPT agent. It works on its own virtual computer: it browses, fills in forms, builds slides "
      "and runs code.\n"
      "January 2026: Google added auto browse to Chrome. It can schedule appointments, fill in forms and request quotes while you "
      "keep browsing.\n"
      "Anthropic's Claude in Chrome and Microsoft's Copilot Actions do the same kind of work.\n\n"
      "Why it's different: a chatbot only reads your words. An agent sees the screen and decides the next click, like handing a "
      "helper your mouse.\n\n"
      "Why it matters: the research group METR measured how long a task AI agents can finish on their own. It has doubled about "
      "every 7 months for 6 years. If that holds, METR says agents could handle projects that take a person a month by about 2030.\n\n"
      "The catch: a web page can hide instructions that trick an agent (this is called prompt injection). That's why Google's auto "
      "browse never presses Buy or Post for you. Rule to keep: AI clicks. You press pay.\n\n"
      "Do this: this week, give an agent one dull errand, like comparing 3 quotes. Watch every step. Pay yourself.\n\n"
      "Availability varies: ChatGPT agent is in paid ChatGPT plans; Chrome auto browse launched in the US for Google AI Pro and "
      "Ultra subscribers.\n\n"
      "Send this to someone who still thinks AI just chats.\n\n#ai #aiagents #chatgpt #gemini #futureofwork #hourback",
      "Sources: OpenAI, 'Introducing ChatGPT agent' (July 17, 2025; TechCrunch coverage: browses, fills forms, makes slides, runs "
      "code; memory off because of prompt-injection risk). 9to5Google, 'Chrome auto browse' (Jan 28, 2026: schedules appointments, "
      "fills forms, requests quotes; US, AI Pro and Ultra; you press buy or post yourself). Anthropic, Claude in Chrome (general "
      "availability for paid plans, Aug 26, 2026, per GIGAZINE). Microsoft Copilot Actions (announced April 2025: book tables, "
      "tickets, rides). METR, 'Measuring AI Ability to Complete Long Tasks' (March 19, 2025): the length of tasks AI agents complete "
      "has doubled about every 7 months for 6 years; if the trend continues to the end of the decade, agents could carry out "
      "month-long projects.")

hpost("hb-1019-buzz-batch", HB, "2026-10-19T17:45", "keep",
      dict(lay="pills", f="indi", text="Buzz. Buzz. / It was / *a coupon.*", obj="phone", at="br", save="there's a setting for that"),
      [dict(k="say", f="yel", label="sound familiar?", size=126,
            text="You stop what / you're doing. / Check the phone. / *A flash sale.*"),
       dict(k="say", f="indi", label="the swap", size=126,
            text="Not-urgent apps / wait, then / arrive *together,* / when you pick.", sub="texts from people still come right away"),
       dict(k="steps", f="yel", text="iPhone", items=["Settings → Notifications", "Scheduled Summary → on",
                                                    "Add shopping and news apps"]),
       dict(k="do", f="indi", text="Today, put your *shopping apps* in a Scheduled Summary at *6 pm.* Leave Messages out.",
            save="send this to the friend whose phone never stops")],
      "Buzz. You stop what you're doing, check your phone, and it's a flash sale.\n\n"
      "The swap: a Scheduled Summary. The apps you choose stop buzzing and arrive together, at the times you pick. "
      "Apps you leave out, like Messages, still come through right away.\n\n"
      "Do this (iPhone): Settings → Notifications → Scheduled Summary → turn it on, add your shopping and news apps, and pick a time "
      "like 6 pm. The list even shows how many notifications each app sends you a day.\n\n"
      f"Send this to the friend whose phone never stops.\n\n{HBTAGS} #notifications #digitalwellbeing",
      "Source: Apple (Use notifications on your iPhone) and iOS guides: Settings → Notifications → Scheduled Summary, choose apps and "
      "times. Only the apps you add are held back.")

reel("hb-reel-1019-wifi-qr", HB, "2026-10-19T19:00", "deep", "hb-x-ta-da-funk", "where's the edge?", [
    dict(k="hook", f="plum", text="AI made workers / *25% faster.* / Then *wrong.*", emo="🧠"),
    dict(k="say", f="orng", text="Harvard and BCG / tested GPT-4 on / *758 consultants.*"),
    dict(k="list", f="plum", items=["*12%* more tasks", "*25%* faster", "*40%* better work"], size=118, drop=True),
    dict(k="say", f="orng", text="On one tricky task, / AI users were / *more often wrong.*"),
    dict(k="because", f="plum", kicker="here's why", text="AI is *jagged:* brilliant at one task, *wrong* at the next."),
    dict(k="do", f="orng", text="Test AI on work *you know cold.* See where it slips."),
    dict(k="save", f="plum", text="send this to / whoever trusts AI / with everything", next="ai, for real · day 1"),
], "AI made people 25% faster. Then it made them wrong.\n\n"
   "Harvard Business School and BCG gave 758 consultants GPT-4 for real consulting work. On tasks AI is good at, they finished "
   "12% more tasks, 25% faster, and their work was rated more than 40% higher in quality.\n\n"
   "Then the researchers slipped in a task that looked similar but sat just outside what AI does well. The consultants using AI "
   "were 19 percentage points less likely to get it right than those working alone.\n\n"
   "Why: AI's skills are jagged. It can be brilliant at one task and confidently wrong at the next, and the two can look the "
   "same from the outside. The researchers call it the jagged technological frontier. Ethan Mollick, one of the authors, builds "
   "his book Co-Intelligence around it.\n\n"
   "The rule to keep: you can't see the edge until you test it.\n\n"
   "Do this: test AI on work you know cold, where you can spot every mistake. That's how you learn where it slips in your job.\n\n"
   "Send this to whoever trusts AI with everything.\n\n#ai #futureofwork #chatgpt #careers #productivity #hourback",
   "Source: Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon & Lakhani, 'Navigating the "
   "Jagged Technological Frontier' (Harvard Business School Working Paper 24-013, Sept 2023): 758 BCG consultants; with GPT-4, "
   "12.2% more tasks, 25.1% faster, more than 40% higher quality; on a task outside the frontier, 19 percentage points less likely "
   "to be correct. Book: Ethan Mollick, Co-Intelligence (2024).")

# ================================================================== Oct 20 (Story chain day)
# ---- AI, FOR REAL · day 2: why AI makes things up, and how to catch it (Story chain carries the lesson today).
hchain("hb-ch-1020b", HB, "2026-10-20", "hb20", "ai, for real · day 2", [
    dict(k="photo", text="It sounded / *so sure.*", sub="and it was completely wrong →", ink="light", y=560),
    dict(k="bubbles", f="plum", label="OpenAI's own researchers tried this", bubbles=[
        ("out", "when is Adam Kalai's birthday?"), ("ai", "He was born on…"),
        ("in", "they asked 3 times. *3 different dates.* all wrong.")], obj="phone"),
    dict(k="bubbles", f="orng", label="here's why", bubbles=[
        ("out", "AI is trained like it's taking a *multiple-choice test*"), ("out", "a guess *might* score. a blank never does."),
        ("in", "so it learned to *guess* 😬")]),
    dict(k="payoff", f="plum", label="the rule to keep", text="Fluent / isn't *true.*", sub="sounds sure? check it anyway",
         obj="point", tap="next story →"),
    dict(k="handoff", f="orng", label="ai, for real · day 2", text="How to catch AI / *making it up.*", img="hb-1020-inbox-filter/01.jpg",
         next="tonight: the AI that says “I don't know”"),
])

hpost("hb-1020-inbox-filter", HB, "2026-10-20T13:00", "learning",
      dict(lay="pills", f="plum", kicker="ai, for real · day 2", text="AI sounds sure. / *That's not* / *the same as right.*", obj="chat", at="bl",
           save="4 ways to catch it"),
      [dict(k="say", f="orng", label="sound familiar?", text="You ask AI something. / It answers instantly, / *in perfect sentences.* / So you believe it."),
       dict(k="why", f="plum", label="why it makes things up", text="AI doesn't look / facts up. It predicts / *the next likely word,* / like autocomplete, / supersized.",
            sub="likely isn't the same as true"),
       dict(k="say", f="orng", label="OpenAI says it too", text="Training / *rewards guessing.* / A guess might score. / *“I don't know”* / never does.",
            src="OpenAI · Why language models hallucinate · Sept 2025"),
       dict(k="say", f="plum", label="check 1: the source", text="Ask where it's from. / Then *open the link.* / AI can invent / quotes, links / and *court cases.*"),
       dict(k="say", f="orng", label="check 2: ask twice", text="Ask the same / question again. / If the answers / *don't match,* / *neither* is safe."),
       dict(k="say", f="plum", label="check 3: hand it the facts", text="Paste the real / document. AI is / *far safer* summing up / *your text* than / recalling facts."),
       dict(k="catch", f="orng", label="check 4: the big stuff", text="Health, money, law: / AI can *start* / the research. / A real source / *finishes it.*",
            sub="fluent isn't true"),
       dict(k="do", f="plum", text="Next time AI gives you a fact that matters, *ask twice* and *open the source.*",
            save="send this to the friend who believes every AI answer")],
      "AI sounds sure. That's not the same as right.\n\n"
      "Why it makes things up: AI doesn't look facts up. It predicts the next likely word, like autocomplete on a huge scale. "
      "Likely isn't the same as true.\n\n"
      "OpenAI's own researchers explain the rest: training and testing reward guessing. On a multiple-choice test a guess might "
      "score, but a blank never does, so models learn to guess instead of saying \"I don't know\".\n\n"
      "4 ways to catch it:\n"
      "1. The source. Ask where it's from, then open the link. AI can invent quotes, links and even court cases.\n"
      "2. Ask twice. If the answers don't match, neither is safe.\n"
      "3. Hand it the facts. Paste the real document and ask it to work from that, not from memory.\n"
      "4. The big stuff. For health, money and law, AI can start the research. A real source finishes it.\n\n"
      "The rule to keep: fluent isn't true.\n\n"
      "Do this: next time AI gives you a fact that matters, ask twice and open the source.\n\n"
      "Send this to the friend who believes every AI answer.\n\n#ai #chatgpt #aitips #factcheck #criticalthinking #hourback",
      "Sources: OpenAI, 'Why language models hallucinate' (Sept 5, 2025): standard training and evaluation reward guessing over "
      "admitting uncertainty; asked for author Adam Tauman Kalai's birthday, a widely used chatbot gave three different wrong dates. "
      "Zhang v. Chen, 2024 BCSC 285 (CBC News, Feb 27, 2024): a B.C. lawyer filed two cases ChatGPT invented and was ordered to pay "
      "the other side's costs for dealing with them. 'Far safer working from your text' is general guidance: answers grounded in a "
      "document you provide can still contain errors, so check anything important.")

hpost("hb-1020-speedy-meetings", HB, "2026-10-20T17:45", "keep",
      dict(lay="pills", f="indi", text="Back-to-backs. / *No bathroom* / *break.*", obj="clock", at="br",
           save="your calendar can fix that"),
      [dict(k="say", f="yel", label="sound familiar?", size=126,
            text="One meeting / ends at 10. / The next starts at 10. / *Coffee? No.*"),
       dict(k="rows", f="indi", text="*Speedy* meetings", cap="a google calendar setting", rows=[("30 min", "ends at 25"),
                                                                                              ("60 min", "ends at 50")]),
       dict(k="steps", f="yel", text="Turn it *on*", items=["Google Calendar on a computer", "⚙ → Settings → Event settings",
                                                           "Tick Speedy meetings"]),
       dict(k="do", f="indi", text="Today, tick *Speedy meetings.* Every meeting *you* book now ends a few minutes early.",
            save="send this to the friend with back-to-backs")],
      "One meeting ends at 10. The next one starts at 10. Coffee? No.\n\n"
      "The swap: Speedy meetings in Google Calendar. Meetings you book end early on their own: 30-minute meetings end at 25, "
      "hour-long ones at 50. That's your gap for water, the bathroom, or a breath.\n\n"
      "Do this: Google Calendar on a computer → ⚙ → Settings → Event settings → tick Speedy meetings.\n\n"
      "It only changes meetings you create. Other people's invites keep their times.\n\n"
      f"Send this to the friend with back-to-backs.\n\n{HBTAGS} #googlecalendar #meetings #worklife",
      "Source: How-To Geek, 'How to automatically shorten meeting durations in Google Calendar': Settings → Event settings → "
      "Speedy meetings; 30 and 45 minute events end 5 minutes early, longer events 10 minutes early.")

reel("hb-reel-1020-grocery-list", HB, "2026-10-20T19:00", "deep", "hb-x-smart-bounce", "which one would you trust?", [
    dict(k="hook", f="indi", text="Two AIs. / One admits / *“I don't know.”*", emo="💬"),
    dict(k="say", f="yel", text="OpenAI tested both / on the *same* / hard questions."),
    dict(k="list", f="indi", items=["Guesser: *75%* wrong", "Honest one: *26%* wrong"], size=104, drop=True),
    dict(k="say", f="yel", text="The guesser: / a bit more right, / nearly *3×* / *more wrong.*"),
    dict(k="because", f="indi", kicker="here's why", text="Tests score *“I don't know”* as zero. So AI learns to *guess.*"),
    dict(k="do", f="yel", text="When AI says *“I'm not sure,”* believe it. *Check the rest.*"),
    dict(k="save", f="indi", text="send this to / the friend who loves / a confident answer", next="ai, for real · day 2"),
], "Two AIs. One admits \"I don't know\". Which would you trust?\n\n"
   "OpenAI tested two of its own models on the same set of hard fact questions. The older one almost never said \"I don't know\" "
   "(1% of the time): it got 24% right and 75% wrong. The newer one said \"I don't know\" about half the time: 22% right, "
   "26% wrong.\n\n"
   "So the guesser got a little more right, and nearly 3 times more wrong.\n\n"
   "Why: most AI tests only count right answers, and \"I don't know\" scores zero. So models learn to guess, and a guess comes out "
   "sounding exactly as sure as a fact.\n\n"
   "The rule to keep: an AI that admits doubt is more useful than one that never does.\n\n"
   "Do this: when AI says \"I'm not sure\", believe it. And check the confident answers that matter.\n\n"
   "Send this to the friend who loves a confident answer.\n\n#ai #chatgpt #openai #aitips #factcheck #hourback",
   "Source: OpenAI, 'Why language models hallucinate' (Sept 5, 2025), SimpleQA results: OpenAI o4-mini abstained 1%, accuracy "
   "24%, error 75%; gpt-5-thinking-mini abstained 52%, accuracy 22%, error 26%. Paper: Kalai, Nachum, Vempala & Zhang (2025).")

# ================================================================== Oct 21 (quiz day)
# ---- AI, FOR REAL · day 3: where your AI chats actually go (quiz day: the Reels carry it, 08:45 part 1 → 19:00 part 2).
hchain("hb-ch-1021b", HB, "2026-10-21", "hb21", "ai, for real · quick quiz", [
    dict(k="bubbles", f="plum", label="quick quiz", title="Can a *person* read / your AI chats?", bubbles=[
        ("in", "Gemini: true or false?"), ("out", "A) no, it's just a machine"), ("out", "B) yes, some of them")],
         tap="guess, then tap →"),
    dict(k="payoff", f="orng", label="the answer: B", text="Human / *reviewers.*", sub="Google says: don't type anything confidential",
         obj="phone", tap="source: Google Gemini privacy hub · tap →"),
    dict(k="payoff", f="plum", label="and they keep it", text="Up to / *3 years.*", sub="reviewed chats, even after you delete yours",
         obj="point", tap="next story →"),
    dict(k="handoff", f="orng", label="ai, for real · day 3", text="Where your AI chats / *actually go.*", img="hb-1021-copy-from-photo/01.jpg",
         next="tonight: the postcard rule"),
])

hpost("hb-1021-copy-from-photo", HB, "2026-10-21T13:00", "learning",
      dict(lay="pills", f="plum", kicker="ai, for real · day 3", text="Where your / AI chats / *actually go.*", obj="phone", at="br",
           save="follow one message, step by step"),
      [dict(k="say", f="orng", label="step 1: you hit send", text="Your message / *leaves your phone.* / It's answered on / the company's / *computers,* not yours."),
       dict(k="say", f="plum", label="step 2: it's saved", text="ChatGPT and Claude / keep chats until / *you delete them.* / Then about *30 days* / to clear out."),
       dict(k="say", f="orng", label="step 3: it may teach the AI", text="Unless you switch / it off, your chats / can help *train* / *the next model.*",
            sub="you can choose in settings"),
       dict(k="say", f="plum", label="step 4: a person may read it", text="Google says *human* / *reviewers* read / some Gemini chats, / and keep them up to / *3 years.*"),
       dict(k="say", f="orng", label="the different one", text="Apple's *Private Cloud* / *Compute* says your / request is used / to answer you, / *then deleted.*",
            sub="and outside experts can check it"),
       dict(k="why", f="plum", label="why it matters", text="Training data / *isn't a chat log.* / Once something / helps train a model, / you can't pull it back out."),
       dict(k="catch", f="orng", label="the rule to keep", text="Type it like / *a postcard,* / not a diary.", sub="anyone handling it could read it"),
       dict(k="do", f="plum", text="Today, open your AI app's *settings:* choose if chats *train it.* Personal stuff? Temporary Chat.",
            save="send this to the friend who tells AI everything")],
      "Where do your AI chats actually go? Follow one message.\n\n"
      "Step 1: you hit send. Your message leaves your phone and is answered on the company's computers, not yours.\n"
      "Step 2: it's saved. ChatGPT and Claude keep your chats until you delete them; deleted chats take about 30 days to clear out.\n"
      "Step 3: it may teach the AI. Unless you switch it off, your chats can be used to train future models. OpenAI, Google and "
      "Anthropic all let you choose.\n"
      "Step 4: a person may read it. Google says human reviewers read some Gemini chats, and keeps those for up to 3 years, even if "
      "you delete your activity.\n\n"
      "The different one: Apple says requests sent to its Private Cloud Compute are used only to answer you and are not stored, "
      "and it lets outside security researchers inspect the system.\n\n"
      "Why it matters: training data isn't a chat log you can tidy up. Once something has helped train a model, you can't pull it "
      "back out. That's why the choice in settings matters.\n\n"
      "The rule to keep: type it like a postcard, not a diary.\n\n"
      "Do this: today, open your AI app's settings and decide whether your chats train it. Use Temporary Chat for anything personal.\n"
      "ChatGPT: Settings → Data Controls → Improve the model for everyone.\n"
      "Gemini: Keep Activity (formerly Gemini Apps Activity).\n"
      "Claude: Settings → Privacy → model training setting.\n\n"
      "Send this to the friend who tells AI everything.\n\n#ai #privacy #chatgpt #gemini #dataprivacy #hourback",
      "Sources: OpenAI Help Center, 'Data Controls FAQ' (Improve the model for everyone; Temporary Chats not used for training, "
      "deleted after 30 days; deleted chats removed within 30 days). Anthropic, 'Updates to our consumer terms' (Aug 28, 2025: model "
      "training is the user's choice; kept 5 years if on, 30 days if off; Free, Pro and Max). Google, Gemini Apps Privacy Hub "
      "(human reviewers; 'Please don't enter confidential information'; reviewed chats kept up to 3 years) and Google blog, "
      "'Temporary Chats and new privacy controls' (Aug 13, 2025: Keep Activity). Apple Security Research, 'Private Cloud Compute' "
      "(June 2024: data used only to fulfil the request, not retained; images published for independent inspection).")

hpost("hb-1021-refund-email", HB, "2026-10-21T17:45", "keep",
      dict(lay="pills", f="indi", text="Still writing / that *refund* / *email?*", obj="chat", at="tr",
           save="this is where AI earns its keep"),
      [dict(k="say", f="yel", label="sound familiar?", size=126,
            text="Too angry. *Delete.* / Too polite. *Delete.* / An hour later, / *still not sent.*"),
       dict(k="say", f="indi", label="the swap", size=126,
            text="Give AI *the facts:* / what you bought, / what went wrong, / *what you want.*", sub="ask for 5 calm lines"),
       dict(k="say", f="yel", label="but don't trust it blindly", size=126,
            text="AI can *invent* / a policy or a law. / Cut anything / *you didn't tell it.*"),
       dict(k="do", f="indi", text="Tonight, give AI your 3 facts and ask for *a 5-line refund email.* Leave out card numbers.",
            save="send this to the friend still drafting it")],
      "Too angry. Delete. Too polite. Delete. An hour later, the refund email still isn't sent.\n\n"
      "The swap: give AI just the facts (what you bought, what went wrong, what you want) and ask for a calm 5-line email. "
      "You get a draft in seconds, and you only edit.\n\n"
      "Where not to trust it: AI can invent a return policy, a law or a date. Cut anything you didn't tell it. "
      "And leave out card numbers, account numbers and your address.\n\n"
      "Do this: tonight, give AI your 3 facts and ask for a 5-line refund email.\n\n"
      f"Send this to the friend still drafting it.\n\n{HBTAGS} #aitips #refund #customerservice",
      "Chat AIs can state rules or policies that don't exist, so keep the email to facts you gave it and check any policy on the "
      "store's own site. Never paste card or account numbers into an AI chat.")

reel("hb-reel-1021-camera-translate", HB, "2026-10-21T19:00", "deep", "hb-x-future-easy", "think before you paste", [
    dict(k="hook", f="plum", text="Engineers pasted / *secret code* / into ChatGPT.", emo="💬"),
    dict(k="say", f="orng", text="That was Samsung, / 2023. Then it *banned* / AI chat tools / on work devices."),
    dict(k="list", f="plum", items=["*Passwords*", "*SIN* and card numbers", "*Client* files"], size=110, drop=True),
    dict(k="because", f="orng", kicker="here's why", text="What you type is *stored* on their computers, and some chats are *read by people.*"),
    dict(k="say", f="plum", text="Think *postcard,* / not diary."),
    dict(k="do", f="orng", text="Before you paste, swap names for *“Sam”* and numbers for *“1234.”*"),
    dict(k="save", f="plum", text="send this to / the friend who / tells AI everything", next="ai privacy · part 2/2"),
], "Engineers pasted secret code into ChatGPT.\n\n"
   "That was Samsung in 2023. After staff uploaded sensitive internal code to ChatGPT, the company banned generative AI tools on "
   "its work devices.\n\n"
   "Never paste these into an AI chat: passwords, your SIN or card numbers, and anyone else's private files (clients, patients, "
   "students).\n\n"
   "Why: what you type is stored on the company's computers, and some chats are read by people. Google tells Gemini users "
   "directly: please don't enter confidential information.\n\n"
   "The rule to keep: think postcard, not diary.\n\n"
   "Do this: before you paste, swap real names for \"Sam\" and account numbers for \"1234\". The AI still understands it.\n\n"
   "Part 2 of 2. Part 1 (this morning): the privacy switch in each AI app.\n\n"
   "Send this to the friend who tells AI everything.\n\n#ai #privacy #chatgpt #cybersecurity #aitips #hourback",
   "Sources: Bloomberg, 'Samsung Bans Staff's AI Use After Spotting ChatGPT Data Leak' (May 2, 2023). Google, Gemini Apps "
   "Privacy Hub: human reviewers read some conversations; 'Please don't enter confidential information in your conversations.' "
   "Check your employer's AI policy before using AI with work files.",
   series="AI privacy · part 2/2")

# ================================================================== Oct 22 (Story chain day)
# ---- AI, FOR REAL · day 4: AI and your career (Story chain carries the lesson; noon = the 4 rules from Co-Intelligence).
hchain("hb-ch-1022", HB, "2026-10-22", "hb19", "ai, for real · day 4", [
    dict(k="photo", text="“Will AI / *take my job?*”", sub="here's what the biggest jobs report says →", ink="light", y=560),
    dict(k="bubbles", f="plum", label="the World Economic Forum asked employers", bubbles=[
        ("in", "so… how many jobs does AI kill?"), ("out", "by 2030: *92 million* jobs displaced"),
        ("out", "and *170 million* new ones created")], obj="phone"),
    dict(k="bubbles", f="orng", label="the part that matters", bubbles=[
        ("out", "*39%* of the skills in a job will change by 2030"), ("in", "which skill is growing fastest?"),
        ("out", "*AI and big data.* number one.")]),
    dict(k="payoff", f="plum", label="an economist put it best", text="AI won't take / your job. / *Someone using AI* / might.",
         sub="Richard Baldwin, 2023", obj="point", tap="next story →"),
    dict(k="handoff", f="orng", label="ai, for real · day 4", text="4 rules for / *working with AI.*", img="hb-1022-unknown-callers/01.jpg",
         next="tonight: the jobs cheat sheet"),
])

hpost("hb-1022-unknown-callers", HB, "2026-10-22T13:00", "learning",
      dict(lay="pills", f="plum", kicker="ai, for real · day 4", text="4 rules for / working / *with AI.*", obj="point", at="bl",
           save="from the book Co-Intelligence"),
      [dict(k="say", f="orng", label="sound familiar?", text="You try AI / *once.* It gives / a so-so answer. / You decide it's / *overhyped.*"),
       dict(k="say", f="plum", label="where these rules come from", text="Wharton professor / *Ethan Mollick* / co-led the study / of 758 consultants. / His book: *Co-Intelligence.*"),
       dict(k="say", f="orng", label="rule 1 · week 1", text="*Bring AI* / *to everything.* / It's the only way / to find where / it really helps.",
            sub="remember the jagged edge?"),
       dict(k="say", f="plum", label="rule 2 · always", text="Stay *the human* / *in the loop.* / You check it. / You decide. / *Your name* goes on it."),
       dict(k="say", f="orng", label="rule 3 · month 1", text="Tell it *who to be:* / “You're a tough / editor. Find the / *three weakest* / *points.*”",
            sub="a clear role gets sharper answers"),
       dict(k="say", f="plum", label="rule 4 · year 1", text="Assume today's AI / is *the worst* / you'll ever use. / Learn it now, / while it's *new.*"),
       dict(k="why", f="orng", label="why it works", text="You're not learning / one app. You're / learning to work with / *a coworker that* / *keeps improving.*"),
       dict(k="catch", f="plum", label="the catch", text="It still *makes* / *things up.* / Rule 2 never / takes a day off."),
       dict(k="do", f="orng", text="This week, bring AI into *one real task a day.* Note where it *helped* and where it *slipped.*",
            save="send this to your work bestie")],
      "4 rules for working with AI, from the book Co-Intelligence.\n\n"
      "Most of us try AI once, get a so-so answer, and decide it's overhyped. Ethan Mollick, a Wharton professor who co-led the "
      "Harvard and BCG study of 758 consultants, argues that's exactly backwards. His book's ideas, in our words:\n\n"
      "Rule 1 (week 1): bring AI to everything. It's the only way to find where it really helps in your work, because its "
      "skills are jagged.\n"
      "Rule 2 (always): stay the human in the loop. You check it, you decide, your name goes on it.\n"
      "Rule 3 (month 1): tell it who to be. \"You're a tough editor. Find the three weakest points.\" A clear role gets sharper "
      "answers.\n"
      "Rule 4 (year 1): assume today's AI is the worst you'll ever use. Learn it now, while it's new.\n\n"
      "Why it works: you're not learning one app. You're learning to work with a coworker that keeps improving.\n\n"
      "The catch: it still makes things up. Rule 2 never takes a day off.\n\n"
      "Do this: this week, bring AI into one real task a day. Note where it helped and where it slipped.\n\n"
      "Send this to your work bestie.\n\n#ai #futureofwork #careers #cointelligence #productivity #hourback",
      "Book: Ethan Mollick, 'Co-Intelligence: Living and Working with AI' (Portfolio, 2024): four rules (always invite AI to the "
      "table; be the human in the loop; treat AI like a person, but tell it what kind of person it is; assume this is the worst AI "
      "you will ever use), paraphrased here. Study: Dell'Acqua, Mollick et al., 'Navigating the Jagged Technological Frontier' "
      "(HBS Working Paper 24-013, 2023), 758 BCG consultants.")

hpost("hb-1022-brain-dump", HB, "2026-10-22T17:45", "keep",
      dict(lay="pills", f="indi", text="11 pm. / Your brain / *won't stop listing.*", obj="cup", at="bl", save="dump it, sort it, sleep"),
      [dict(k="say", f="yel", label="sound familiar?", size=126,
            text="Book the vet. / Email the school. / Buy a gift. / *And 20 more.*"),
       dict(k="say", f="indi", label="the swap", size=126,
            text="Talk it into / a *note.* / Then ask AI / to *sort it.*", sub="today · this week · later"),
       dict(k="say", f="yel", label="but don't trust it blindly", size=126,
            text="AI can *drop* / *a line.* / Skim your note / before you delete it."),
       dict(k="do", f="indi", text="Tonight, talk your list into *Notes.* Ask AI to sort it: *today, this week, later.*",
            save="send this to the friend who lies awake")],
      "11 pm. Book the vet, email the school, buy a gift, and 20 more things your brain won't stop listing.\n\n"
      "The swap: say it all into a note (tap the mic on your keyboard; messy is fine). Paste it into AI and ask it to sort it into "
      "today, this week, and later. You get a short list instead of a loop in your head.\n\n"
      "Where not to trust it: AI can drop a line or merge two. Skim your note before you delete it. "
      "Leave out names, addresses and anything private.\n\n"
      "Do this: tonight, talk your whole list into Notes, then ask AI to sort it.\n\n"
      f"Send this to the friend who lies awake listing things.\n\n{HBTAGS} #todolist #aitips #mentalload",
      "Chat AIs can leave items out when they reorganise a list, so check it against your original note. "
      f"{PRIV}")


# ================================================================== Oct 23-25 (built Oct 18 pm). Facts checked Oct 18 (sources in each first comment).
# Themes alternate post to post: Oct 22 ended plum (19:00 cheat) -> Oct 23 starts indi.
# Oct 23 = quiz day (Reels carry it: photo search part 1 -> duplicates part 2), Oct 24 = Story chain day, Oct 25 = quiz day.

# ------------------------------------------------------------------ Oct 23 (quiz day)
# ---- AI, FOR REAL · day 5: AI that sees and hears (quiz day: Reels carry it, 08:45 part 1 → 19:00 part 2; noon = what's inside ChatGPT).
reel("hb-reel-1023am-photo-search", HB, "2026-10-23T08:45", "deep", "hb-x-future-easy", "just show it", [
    dict(k="hook", f="indi", text="Point your camera. / *Ask out loud.*", emo="📸"),
    dict(k="say", f="yel", text="Google made / *Gemini Live's* camera / *free* on Android."),
    dict(k="list", f="indi", items=["It *sees* what you show", "It *hears* how you ask", "It *talks* back, live"], size=100, drop=True),
    dict(k="because", f="yel", kicker="here's why it's big", text="AI used to read only *text.* Now it *sees and hears.*"),
    dict(k="do", f="yel", text="Confused by an error light or a form? *Show it* to Gemini Live. Ask *why.*"),
    dict(k="save", f="indi", text="send this to / the friend who / still types everything", next="part 2 tonight: where it goes wrong"),
], "Point your camera. Ask out loud. AI answers.\n\n"
   "In April 2025, Google made Gemini Live's camera and screen sharing free for Android users. ChatGPT's voice mode has been "
   "able to see through your camera since December 2024. You show it something, ask in your own words, and it talks back.\n\n"
   "Why it's big: for most of its life, AI could only read text. Now it takes in the world the way you do: sight, sound, "
   "speech. Researchers call this multimodal AI.\n\n"
   "Where it helps: the blinking error light on the router, the form you don't understand, the chart in a report. Just show it.\n\n"
   "Do this: next time something's confusing, show it to Gemini Live or ChatGPT's voice mode and ask why. Then check anything "
   "important (part 2 tonight: where it goes wrong).\n\n"
   "Send this to the friend who still types everything.\n\n#ai #gemini #chatgpt #multimodal #techtips #hourback",
   "Sources: 9to5Google, 'Gemini Live camera and screen sharing now free for all Android users' (Apr 16, 2025); OpenAI, "
   "'Advanced Voice with video and screen sharing' (12 Days of OpenAI, Dec 12, 2024). Don't show it anything private: what the "
   "camera sees is sent to the company's servers.",
   series="AI that sees · part 1/2")

hchain("hb-ch-1023", HB, "2026-10-23", "hb19", "ai, for real · quick quiz", [
    dict(k="bubbles", f="plum", label="quick quiz", title="How many people / use ChatGPT *each week?*", bubbles=[
        ("in", "take a guess"), ("out", "A) 90 million"), ("out", "B) 900 million")], tap="guess, then tap →"),
    dict(k="payoff", f="orng", label="the answer: B", text="*900* / million.", sub="every week, says OpenAI (Feb 2026)", obj="phone",
         tap="source: OpenAI via TechCrunch · tap →"),
    dict(k="payoff", f="plum", label="put another way", text="About *1 in 9* / people on Earth.", sub="here's how it actually works",
         obj="point", tap="next story →"),
    dict(k="handoff", f="orng", label="ai, for real · day 5", text="What's actually / *inside ChatGPT?*", img="hb-1023-renewal-reminders/01.jpg",
         next="tonight: where AI's eyes go wrong"),
])

hpost("hb-1023-renewal-reminders", HB, "2026-10-23T13:00", "learning",
      dict(lay="pills", f="plum", kicker="ai, for real · day 5", text="What's actually / *inside* / ChatGPT?", obj="phone", at="br",
           save="5 steps, zero jargon"),
      [dict(k="say", f="orng", label="step 1: it read a library", text="It was trained on / *a huge amount* / of text: books, / websites, code."),
       dict(k="why", f="plum", label="step 2: it learned patterns", text="Not facts in a / filing cabinet. / *Patterns:* which / word tends / to *come next.*",
            sub="like a friend who's read everything"),
       dict(k="say", f="orng", label="step 3: it took a mountain of chips", text="Training runs on / *thousands* of / specialised chips, / mostly *Nvidia's.*",
            sub="that's why Nvidia became a giant"),
       dict(k="say", f="plum", label="step 4: people taught it manners", text="Humans *ranked* / its answers. It / learned to give / the ones *people* / *preferred.*"),
       dict(k="say", f="orng", label="step 5: you hit send", text="It builds the / reply *one word-piece* / *at a time,* / picking the / likeliest next one."),
       dict(k="why", f="plum", label="why this helps you", text="Now you know why / it's *great at writing* / and can still be / *wrong about facts.*"),
       dict(k="catch", f="orng", label="the rule to keep", text="A *pattern* / *machine,* / not a fact / machine.", sub="use it to draft, then verify"),
       dict(k="do", f="plum", text="Next time AI answers, ask yourself: is this *writing* (trust more) or *a fact* (check it)?",
            save="send this to the friend who calls it magic")],
      "What's actually inside ChatGPT? 5 steps, zero jargon.\n\n"
      "1. It read a library. Models like ChatGPT are trained on huge amounts of text: books, websites, code.\n"
      "2. It learned patterns, not facts. It doesn't store a filing cabinet of answers. It learns which word tends to come next, "
      "like a friend who's read everything but can't quote the page.\n"
      "3. It took a mountain of chips. Training runs on thousands of specialised chips, mostly made by Nvidia. That demand is why "
      "Nvidia became one of the world's most valuable companies.\n"
      "4. People taught it manners. Humans ranked its answers, and it learned to give the kind people preferred.\n"
      "5. You hit send. It builds the reply one word-piece at a time, picking a likely next piece each time.\n\n"
      "Why this helps you: it explains why AI is brilliant at writing and still wrong about facts.\n\n"
      "The rule to keep: it's a pattern machine, not a fact machine. Use it to draft, then verify.\n\n"
      "Do this: next time AI answers, ask yourself: is this writing (trust it more) or a fact (check it)?\n\n"
      "Send this to the friend who calls it magic.\n\n#ai #chatgpt #howitworks #nvidia #learnai #hourback",
      "Sources: OpenAI, 'Training language models to follow instructions with human feedback' (InstructGPT, 2022: human labelers "
      "ranked model outputs to train the model); OpenAI, 'Why language models hallucinate' (Sept 2025: models are trained to "
      "predict the next word); Nvidia's data-centre GPUs are the main chips used to train large AI models (Nvidia annual reports, "
      "2025). Simplified for a general audience.")

reel("hb-reel-1023-duplicates", HB, "2026-10-23T19:00", "deep", "hb-x-smart-bounce", "read the original", [
    dict(k="hook", f="plum", text="Apple's AI wrote / a *headline.* / It was *false.*", emo="📱"),
    dict(k="say", f="orng", text="It squeezed a / BBC news alert / and said a suspect / had *shot himself.* / He hadn't."),
    dict(k="list", f="plum", items=["Jan 2025:", "Apple *paused* it"], size=120, drop=True),
    dict(k="because", f="orng", kicker="here's why", text="A summary *squeezes* the facts. When AI squeezes, it can *change* them."),
    dict(k="do", f="plum", text="When AI sums up news or a letter, *open the original* before you act on it."),
    dict(k="save", f="orng", text="send this to / the friend who / only reads summaries", next="AI that sees · part 2/2"),
], "Apple's AI wrote a headline. It was false.\n\n"
   "In December 2024, Apple Intelligence's notification summaries condensed a BBC News alert and claimed that Luigi Mangione, "
   "the suspect in a high-profile shooting, had shot himself. He hadn't. After complaints from the BBC, Apple paused AI "
   "summaries for news apps in January 2025 and started showing other summaries in italics so you know they're AI-written.\n\n"
   "Why: a summary squeezes the facts. When AI squeezes, it can drop a word like \"not\" or merge two stories, and the result "
   "still sounds completely confident.\n\n"
   "The rule to keep: a summary is a pointer, not the story.\n\n"
   "Do this: when AI sums up news, an email or a letter, open the original before you act on it.\n\n"
   "Part 2 of 2. Part 1 (this morning): AI that sees through your camera.\n\n"
   "Send this to the friend who only reads summaries.\n\n#ai #apple #appleintelligence #fakenews #factcheck #hourback",
   "Sources: BBC News complaint and Apple's response (Jan 16, 2025), reported by CNN and Tom's Guide, 'Apple scraps Apple "
   "Intelligence news feature after misinformation complaints' (Jan 17, 2025): summaries for news and entertainment apps "
   "disabled in iOS 18.3; AI summaries shown in italics.",
   series="AI that sees · part 2/2")

# ------------------------------------------------------------------ Oct 24 (Story chain day)
# ---- AI, FOR REAL · day 6: AI makes prediction cheap (Power and Prediction / Prediction Machines). Story chain carries the lesson.
hchain("hb-ch-1024", HB, "2026-10-24", "hb21", "ai, for real · day 6", [
    dict(k="photo", text="Cheap things / get used / *everywhere.*", sub="AI is making prediction cheap →", ink="light", y=760),
    dict(k="bubbles", f="indi", label="three Toronto economists spotted this", bubbles=[
        ("out", "AI's real skill? *predicting.* the next word, the fraud, the traffic"), ("in", "so what gets valuable?"),
        ("out", "*judgment.* deciding what to do with the prediction")], obj="phone"),
    dict(k="bubbles", f="yel", label="like electricity", bubbles=[
        ("out", "factories first just swapped steam engines for *motors*"),
        ("out", "the big gains came *decades later,* when they redesigned the factory"), ("in", "so we're still early?")]),
    dict(k="payoff", f="indi", label="the rule to keep", text="AI predicts. / *You judge.*", sub="from the book Power and Prediction",
         obj="point", tap="next story →"),
    dict(k="handoff", f="yel", label="ai, for real · day 6", text="AI made prediction / *cheap.*", img="hb-1024-share-eta/01.jpg",
         next="tonight: Nvidia's boss on AI coworkers"),
])

hpost("hb-1024-share-eta", HB, "2026-10-24T13:00", "learning",
      dict(lay="pills", f="indi", kicker="ai, for real · day 6", text="AI made / prediction / *cheap.*", obj="phone", at="br",
           save="here's what gets valuable"),
      [dict(k="say", f="yel", label="sound familiar?", text="Your bank texts: / *“Was this you?”* / Your map says / *“12 min faster.”* / Both are predictions."),
       dict(k="why", f="indi", label="the big idea", text="AI's core skill is / *prediction:* filling / in what you don't / know from what / you do.",
            sub="from Prediction Machines"),
       dict(k="say", f="yel", label="when it gets cheap", text="When light got / cheap, we lit / *everything.* Now / prediction is / *getting cheap.*"),
       dict(k="say", f="indi", label="so what gets valuable?", text="*Judgment:* / knowing what / matters, and / *what to do* / about it."),
       dict(k="say", f="yel", label="in your job", text="AI drafts / three options. / Your value is / *picking the right one* / and knowing *why.*"),
       dict(k="say", f="indi", label="the electricity lesson", text="Factories took / *decades* to redesign / around electricity. / The big wins came / *after the redesign.*"),
       dict(k="catch", f="yel", label="the rule to keep", text="AI predicts. / *You judge.*", sub="the judging part is your career"),
       dict(k="do", f="indi", text="This week, spot one *prediction* AI makes for you. Ask: which *decision* is still mine?",
            save="send this to the friend planning their next move")],
      "AI made prediction cheap. Here's what gets valuable.\n\n"
      "Your bank texts \"Was this you?\" Your map says \"12 minutes faster this way.\" Both are AI predictions.\n\n"
      "The big idea, from three University of Toronto economists (Ajay Agrawal, Joshua Gans and Avi Goldfarb, in Prediction "
      "Machines and Power and Prediction): AI's core skill is prediction, filling in what you don't know from what you do.\n\n"
      "When light got cheap, we lit everything. Now prediction is getting cheap, and it's showing up everywhere.\n\n"
      "So what gets valuable? Judgment: knowing what matters and what to do about the prediction. AI drafts three options; your "
      "value is picking the right one and knowing why.\n\n"
      "The electricity lesson: factories first just swapped steam engines for electric motors. The big gains came decades later, "
      "when they redesigned the whole factory around electricity. The authors argue AI is in that in-between stage now.\n\n"
      "The rule to keep: AI predicts. You judge.\n\n"
      "Do this: this week, spot one prediction AI makes for you. Ask: which decision is still mine?\n\n"
      "Send this to the friend planning their next career move.\n\n#ai #futureofwork #careers #predictionmachines #books #hourback",
      "Books: Ajay Agrawal, Joshua Gans & Avi Goldfarb, 'Prediction Machines' (Harvard Business Review Press, 2018; AI as cheap "
      "prediction, judgment as its complement) and 'Power and Prediction' (2022; electricity and factory redesign, the 'between "
      "times'). Ideas paraphrased in our own words.")

reel("hb-reel-1024-fridge-dinner", HB, "2026-10-24T19:00", "deep", "hb-x-smart-bounce", "who manages the agents?", [
    dict(k="hook", f="indi", text="Nvidia's CEO: / IT will become / *HR for AI agents.*", emo="💬"),
    dict(k="say", f="yel", text="Jensen Huang, / CES 2025. Agents / will be *onboarded* / and *improved,* / like staff."),
    dict(k="list", f="indi", items=["*Hired*", "*Trained*", "*Reviewed*"], size=130, drop=True),
    dict(k="because", f="yel", kicker="here's why", text="Agents now *do tasks,* not just answer. Tasks need *a manager.*"),
    dict(k="say", f="indi", text="That manager / could be *you.*"),
    dict(k="do", f="yel", text="Pick one task you repeat. Write the *steps* you'd give a new hire. That's an *agent brief.*"),
    dict(k="save", f="indi", text="send this to / the friend who / manages people", next="ai, for real · day 6"),
], "Nvidia's CEO says your IT team will become HR for AI agents.\n\n"
   "At CES in January 2025, Jensen Huang said: \"In a lot of ways, the IT department of every company is going to be the HR "
   "department of AI agents in the future.\" Agents will be brought in, trained, checked and improved, a lot like staff.\n\n"
   "Why: agents don't just answer questions anymore, they do tasks. And anything that does tasks needs someone to give it "
   "clear instructions and review its work.\n\n"
   "That someone could be you. Writing clear instructions and checking results is a management skill, and it's becoming an AI "
   "skill too.\n\n"
   "Do this: pick one task you repeat at work. Write the steps you'd give a new hire, including what \"done\" looks like. "
   "That's an agent brief, and it's useful even before you hand it to an AI.\n\n"
   "Send this to the friend who manages people.\n\n#ai #aiagents #nvidia #futureofwork #leadership #hourback",
   "Source: Fortune, 'Nvidia CEO Jensen Huang says IT will become the HR department for AI agents' (Jan 9, 2025), CES 2025 "
   "keynote quote.")

# ------------------------------------------------------------------ Oct 25 (quiz day)
# ---- AI, FOR REAL · day 7: it's already in your apps (quiz day: 08:45 Reel part 1 → 19:00 cheat part 2) + the week's 7 rules at noon.
reel("hb-reel-1025am-talk-dont-type", HB, "2026-10-25T08:45", "deep", "hb-x-future-easy", "look for the button", [
    dict(k="hook", f="plum", text="You already / use AI. / *Every day.*", emo="📱"),
    dict(k="say", f="orng", text="Meta says about / *a billion people* / use Meta AI / every month."),
    dict(k="list", f="plum", items=["WhatsApp: *Meta AI*", "iPhone: *Writing Tools*", "Gmail: *Gemini*"], size=104, drop=True),
    dict(k="because", f="orng", kicker="here's why", text="Big tech isn't waiting for you to visit AI. It's putting AI *where you already are.*"),
    dict(k="do", f="plum", text="Today, find the *AI button* in one app you use daily. Try it on *one real task.*"),
    dict(k="save", f="orng", text="send this to / the friend who says / “I don't use AI”", next="part 2 tonight: the full map"),
], "You already use AI. Every day.\n\n"
   "Meta says about a billion people use Meta AI every month, mostly inside WhatsApp, Instagram, Facebook and Messenger. "
   "On newer iPhones, Apple Intelligence adds Writing Tools to almost every text box. In Gmail, Gemini can summarise long threads.\n\n"
   "Why: big tech isn't waiting for you to visit an AI website. It's putting AI where you already are, so the button is often "
   "right there and easy to scroll past.\n\n"
   "Do this: today, find the AI button in one app you use daily and try it on one real task. Then use this week's rules: "
   "check the facts, keep it a postcard, and you make the call.\n\n"
   "Part 2 tonight at 7: the full map of where AI lives in your apps.\n\n"
   "Send this to the friend who says \"I don't use AI\".\n\n#ai #metaai #appleintelligence #gemini #techtips #hourback",
   "Sources: CNBC, 'Mark Zuckerberg says Meta AI has 1 billion monthly active users' (May 28, 2025, Meta annual shareholder "
   "meeting); Apple, Apple Intelligence Writing Tools (iPhone 15 Pro and later); Google Workspace, Gemini in Gmail "
   "(summarise threads). Features vary by device, plan and country.",
   series="AI in your apps · part 1/2")

hchain("hb-ch-1025", HB, "2026-10-25", "hb20", "ai, for real · quick quiz", [
    dict(k="bubbles", f="indi", label="this week's quiz", title="The AI that says / *“I don't know”* is…", bubbles=[
        ("in", "remember day 2?"), ("out", "A) broken"), ("out", "B) more trustworthy")], tap="guess, then tap →"),
    dict(k="payoff", f="yel", label="the answer: B", text="*26%* wrong / vs *75%.*", sub="the honest AI vs the guesser, in OpenAI's test", obj="phone",
         tap="source: OpenAI, Sept 2025 · tap →"),
    dict(k="payoff", f="indi", label="one week, one idea", text="Know how it / works. Then / *use it well.*", sub="7 rules, all in one post",
         obj="point", tap="next story →"),
    dict(k="handoff", f="yel", label="ai, for real · day 7", text="One week. / *7 rules for AI.*", img="hb-1025-family-calendar/01.jpg",
         next="tonight: where AI lives in your apps"),
])

hpost("hb-1025-family-calendar", HB, "2026-10-25T13:00", "learning",
      dict(lay="pills", f="indi", kicker="ai, for real · day 7", text="One week. / *7 rules* / for the AI age.", obj="chat", at="bl",
           save="save this, live by it"),
      [dict(k="say", f="yel", label="day 1 · agents", text="AI now *clicks,* / *scrolls and fills* / *in forms.* / Rule: AI clicks. / *You press pay.*"),
       dict(k="say", f="indi", label="day 2 · hallucination", text="It's trained to / guess, not to / say “I don't know.” / Rule: *fluent* / *isn't true.*"),
       dict(k="say", f="yel", label="day 3 · privacy", text="Chats are stored, / may train it, and / some are *read.* / Rule: *a postcard,* / not a diary."),
       dict(k="say", f="indi", label="day 4 · your career", text="Skills are changing / fast. Rule: *bring AI* / *to everything,* / and stay the / human in the loop."),
       dict(k="say", f="yel", label="day 5 · how it works", text="It predicts the / next word-piece. / Rule: a *pattern* / *machine,* not a / fact machine."),
       dict(k="say", f="indi", label="day 6 · the big idea", text="Prediction got / cheap. Judgment / got valuable. / Rule: *AI predicts.* / *You judge.*"),
       dict(k="say", f="yel", label="day 7 · it's already here", text="It's in WhatsApp, / Gmail, your phone. / Rule: *learn it* / *on purpose,* / not by accident."),
       dict(k="do", f="indi", text="Pick the rule you needed most. *Screenshot it.* Use it the next time you open AI.",
            save="send this to the friend starting with AI")],
      "One week. 7 rules for the AI age.\n\n"
      "Day 1, agents: AI now clicks, scrolls and fills in forms for you. Rule: AI clicks. You press pay.\n"
      "Day 2, hallucination: AI is trained in a way that rewards guessing over \"I don't know\". Rule: fluent isn't true.\n"
      "Day 3, privacy: chats are stored, may train future models, and some are read by people. Rule: type it like a postcard, "
      "not a diary.\n"
      "Day 4, your career: the skills inside jobs are changing fast. Rule: bring AI to everything, and stay the human in the loop.\n"
      "Day 5, how it works: it predicts the next word-piece from patterns. Rule: a pattern machine, not a fact machine.\n"
      "Day 6, the big idea: prediction got cheap, so judgment got valuable. Rule: AI predicts. You judge.\n"
      "Day 7, it's already here: in WhatsApp, Gmail and your phone. Rule: learn it on purpose, not by accident.\n\n"
      "Do this: pick the rule you needed most, screenshot it, and use it the next time you open AI.\n\n"
      "Send this to the friend just starting with AI.\n\n#ai #learnai #chatgpt #futureofwork #aitips #hourback",
      "Every rule comes from this week's posts and their sources: OpenAI, Google and Anthropic product announcements; METR (2025); "
      "OpenAI, 'Why language models hallucinate' (2025); WEF Future of Jobs Report 2025; Statistics Canada (2024, 2026); "
      "Mollick, Co-Intelligence (2024); Agrawal, Gans & Goldfarb, Prediction Machines (2018) and Power and Prediction (2022).")

# ------------------------------------------------------------------ AIR PASS for Oct 23-25 (same rule as below)
_NEW_DAYS = ("2026-10-23", "2026-10-24", "2026-10-25")


# ================================================================== retired ids (Oct 18 am rebuild: "it has to be really Hourback")
for _old in ("hb-reel-1019am-just-the-asks", "hb-w02-8-12-automations-kickoff", "hb-1019-single-homework", "hb-reel-1019-one-sorry",
             "hb-reel-1020am-driveway-text", "hb-1020-prompt-week-01", "hb-1020-single-error-code", "hb-reel-1020-three-tabs",
             "hb-reel-1021am-parcel-text", "hb-1021-ai-said-what-bill", "hb-reel-1021-group-costume", "hb-1021-travel-subscriptions",
             *[f"hb-ch-1019-{i}" for i in range(1, 5)], *[f"hb-ch-1020-{i}" for i in range(1, 6)],
             *[f"hb-ch-1021-{i}" for i in range(1, 5)]):
    _DROPPED[_old] = "Hourback rebuild Oct 18 am: replaced by the 'get an hour back' time-saver content"

# hb-1021-travel-subscriptions is registered by v5_formats (imported after this file): load it now and take it back out.
import v5_formats as _v5f  # noqa: E402,F401

_POSTS.pop("hb-1021-travel-subscriptions", None)
_META.pop("hb-1021-travel-subscriptions", None)


# ------------------------------------------------------------------ AIR PASS (Oct 18 am): size each Oct 19-22 slide to its longest line,
# so forced line breaks never re-wrap (one line on screen = one line in the source).
def _fit_sizes(brand, em=0.39, cap=140, floor=88):
    """AIR PASS: keep the hand-written line breaks and pick each slide's size so its longest line fits the 920px text box
    (em = average glyph width for this page's serif) and all its lines fit the box height. Then nothing re-wraps.
    Oct 19-22 feed slides only."""
    import re as _re

    def _len(s):
        return len(_re.sub(r"\*", "", s)) + 2 * len(_re.findall(r"[\U0001F300-\U0001FAFF]", s))

    for _pid, _sp in _POSTS.items():
        if _sp["brand"] != brand or _META[_pid]["at"][:10] not in ("2026-10-19", "2026-10-20", "2026-10-21", "2026-10-22") + _NEW_DAYS:
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

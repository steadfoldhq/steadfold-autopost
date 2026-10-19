"""Hourback Canada-edition cheat-sheet Reels (Oct 18 am rebuild: "get an hour back").
Each sheet: Canada life admin you can do in minutes, from official or named sources (in `src` + first comment).
Rendered by cheatsheet.py; scheduled by add_to_schedule() below (morning ones go out as Trial Reels)."""

FF, HB, LH, LF = "fullyfunded", "hourback", "lockedhour", "littlefold"
TAGS = "#canada #lifeadmin #timesaver #hourback #canadatips"

CHEATS = {}
META = {}


def cheat(pid, at, spec, caption, comment):
    CHEATS[pid] = spec
    META[pid] = dict(at=at, caption=caption, comment=comment)


# ---------------------------------------------------------------- Oct 19 08:45 · AI at work in Canada: the real numbers (AI, for real · day 1)
# Re-planned Oct 19 00:20 (owner: "HOURBACK = REALLY TEACH AI"). Same id and slot; StatCan figures checked Oct 19.
cheat("hb-cheat-1019am-cra-online", "2026-10-19T08:45",
      dict(brand=HB, field="indi", track="hb-x-smart-bounce", beat=2.8,
           title="AI at work in Canada: / *the real numbers*", head=("StatCan found…", "share"),
           rows=[("Businesses using AI, 2024", "6%"), ("Businesses using AI, 2025", "12%"), ("Businesses using AI, 2026", "19%"),
                 ("Jobs where AI could help you", "29%"), ("Jobs where AI could take tasks", "31%"),
                 ("Jobs AI barely touches", "40%")],
           do="Circle the task in your week AI could *help with.* Learn that one first.",
           save="send this to the coworker who's worried about AI",
           src="Statistics Canada: AI use by businesses, Q2 2026 (June 11, 2026) · AI occupational exposure, Economic and Social Reports (Sept 3, 2024)."),
      "AI at work in Canada: the real numbers 🇨🇦\n\n"
      "Canadian businesses using AI to make their products or serve customers: 6% in 2024, 12% in 2025, 19% in 2026. "
      "It tripled in two years.\n\n"
      "And your job? Statistics Canada sorted every job by how exposed it is to AI:\n"
      "29% of workers are in jobs where AI could help them, because a person still has to make the call (family doctors, "
      "high school teachers, electrical engineers).\n"
      "31% are in jobs where AI could take over more of the tasks (data entry clerks, computer programmers).\n"
      "40% are in jobs AI barely touches (plumbers, carpenters, firefighters).\n\n"
      "Why it matters: exposed doesn't mean replaced. It means your tasks change. The people who learn to use AI on their own "
      "work are the ones who get the benefit.\n\n"
      "Do this: list the 3 tasks that take most of your week. Circle the one AI could help with, and learn that one first.\n\n"
      "Tonight at 7: what happened when Harvard gave 758 consultants AI.\n\n"
      f"Send this to the coworker who's worried about AI.\n\n#ai #futureofwork #canada #careers #statcan #hourback",
      "Which group is your job in? Sources: Statistics Canada, 'Analysis on artificial intelligence use by businesses in Canada, "
      "second quarter of 2026' (June 11, 2026): 19.2% of businesses used AI to produce goods or deliver services, up from 12.2% "
      "(Q2 2025) and 6.1% (Q2 2024). Statistics Canada, Economic and Social Reports, 'Experimental estimates of potential artificial "
      "intelligence occupational exposure in Canada' (Sept 3, 2024; May 2021 data): 29% high exposure and high complementarity, "
      "31% high exposure and low complementarity, 40% low exposure; occupations named in the report.")

# ---------------------------------------------------------------- Oct 20 08:45 · AI made it up: who paid? (AI, for real · day 2)
cheat("hb-cheat-1020am-spam-off", "2026-10-20T08:45",
      dict(brand=HB, field="orng", track="hb-x-future-easy", beat=4.2,
           title="AI made it up. / *Who paid?*", head=("what happened", "who paid"),
           rows=[("Bot invents a refund rule", "Air Canada"), ("Airline: “the bot's fault”", "rejected"),
                 ("ChatGPT invents 2 cases", "the lawyer"), ("AI's error in your email", "you")],
           do="Before you send anything AI wrote, *check every fact* you didn't give it.",
           save="send this to the friend who copy-pastes AI",
           src="Moffatt v. Air Canada, 2024 BCCRT 149 · Zhang v. Chen, 2024 BCSC 285 (CBC News, Feb 27, 2024)."),
      "AI made it up. Who paid? 🇨🇦\n\n"
      "2024, B.C.: Air Canada's website chatbot told a grieving passenger he could claim a bereavement fare after his trip. "
      "That wasn't the airline's policy. Air Canada argued the chatbot was responsible for its own words. The Civil Resolution "
      "Tribunal called that \"a remarkable submission\" and ordered the airline to pay him about $812.\n\n"
      "2024, B.C.: a lawyer filed two court cases that ChatGPT had invented. They didn't exist. The judge ordered her to "
      "personally pay the other side's costs for dealing with them.\n\n"
      "The rule to keep: when AI is wrong, the person who used it owns it. That's you.\n\n"
      "Do this: before you send anything AI wrote, check every fact you didn't give it yourself: names, dates, rules, numbers.\n\n"
      "Today at noon in Stories: why AI makes things up.\n\n"
      "Send this to the friend who copy-pastes AI.\n\n#ai #chatgpt #aitips #canada #factcheck #hourback",
      "Sources: Moffatt v. Air Canada, 2024 BCCRT 149 (B.C. Civil Resolution Tribunal): $650.88 damages plus $36.14 interest and "
      "$125 fees; the tribunal rejected the argument that the chatbot was a separate entity. Zhang v. Chen, 2024 BCSC 285 (CBC News, "
      "'B.C. lawyer reprimanded for citing fake cases invented by ChatGPT', Feb 27, 2024): two non-existent cases; costs ordered "
      "against the lawyer personally.")

# ---------------------------------------------------------------- Oct 21 08:45 · AI privacy part 1: the switch in each app (AI, for real · day 3)
cheat("hb-cheat-1021am-set-once", "2026-10-21T08:45",
      dict(brand=HB, field="yel", track="hb-x-ta-da-funk", beat=5.5, card_h=250, table_top=620, do_top=1375,
           title="Your AI chats: / *the privacy switch*",
           cards=[dict(name="ChatGPT", lines=["Settings → Data Controls", "“Improve the model”: off", "Temporary Chat: gone in 30 days"]),
                  dict(name="Gemini", lines=["Turn off Keep Activity", "Temporary Chat: kept 72 hours", "Some chats read by reviewers"]),
                  dict(name="Claude", lines=["Settings → Privacy", "Model training: your choice", "On: kept 5 years. Off: 30 days"])],
           do="Today, open your AI app and *choose* whether your chats train it.",
           save="send this to the friend who tells AI everything",
           src="OpenAI Help: Data Controls FAQ · Google: Gemini privacy hub, Temporary Chats (Aug 13, 2025) · Anthropic: Updates to consumer terms (Aug 28, 2025)."),
      "Your AI chats: the privacy switch 🔒 Part 1 of 2.\n\n"
      "ChatGPT: Settings → Data Controls → turn off \"Improve the model for everyone\" if you don't want your chats used for "
      "training. Temporary Chat isn't used for training and is deleted after 30 days.\n\n"
      "Gemini: turn off Keep Activity (it used to be called Gemini Apps Activity). Temporary Chats are kept up to 72 hours and "
      "aren't used for training. Google says human reviewers read some chats, so don't type anything confidential.\n\n"
      "Claude: Settings → Privacy → the model training setting. If it's on, chats are kept for 5 years; if it's off, 30 days.\n\n"
      "Why it matters: once something helps train a model, you can't take it back out.\n\n"
      "Do this: today, open the AI app you use most and choose whether your chats train it.\n\n"
      "Part 2 tonight at 7: what never to paste.\n\n"
      "Send this to the friend who tells AI everything.\n\n#ai #privacy #chatgpt #gemini #claude #hourback",
      "Which app do you use most? Sources: OpenAI Help Center, 'Data Controls FAQ' (Improve the model for everyone; Temporary "
      "Chats deleted after 30 days, not used for training). Google blog, 'Gemini adds Temporary Chats and new privacy controls' "
      "(Aug 13, 2025: Keep Activity; Temporary Chats kept up to 72 hours) and Gemini Apps Privacy Hub (human reviewers). "
      "Anthropic, 'Updates to our consumer terms' (Aug 28, 2025: 5-year retention if you allow training, 30 days if not; "
      "Free, Pro and Max plans). Menus can change between app versions.")

# ---------------------------------------------------------------- Oct 22 19:00 · AI and jobs: the big numbers (AI, for real · day 4)
cheat("hb-cheat-1022-travel-admin", "2026-10-22T19:00",
      dict(brand=HB, field="plum", track="hb-x-smart-bounce", beat=2.8,
           title="AI and jobs: / *the big numbers*", head=("by 2030, worldwide…", "WEF"),
           rows=[("New jobs created", "170M"), ("Jobs displaced", "92M"), ("Net change", "+78M"),
                 ("Skills in a job that change", "39%"), ("Fastest-growing skill", "AI & data"),
                 ("Canadian firms using AI now", "19%")],
           do="Pick *one AI skill* your job needs. Practise it *15 min a day.*",
           save="send this to the friend who's job hunting",
           src="World Economic Forum, Future of Jobs Report 2025 (Jan 2025) · Statistics Canada, AI use by businesses, Q2 2026."),
      "AI and jobs: the big numbers 🇨🇦🌍\n\n"
      "The World Economic Forum surveyed employers worldwide for its Future of Jobs Report 2025. By 2030 they expect:\n"
      "170 million new jobs created.\n92 million jobs displaced.\nA net gain of 78 million.\n"
      "39% of the core skills in a job to change.\n"
      "The fastest-growing skill: AI and big data.\n\n"
      "And in Canada right now, 19% of businesses already use AI to make their products or serve customers (Statistics Canada, 2026).\n\n"
      "Why it matters: the jobs don't simply vanish; the skills inside them change. The people who learn the new skills move up.\n\n"
      "Do this: pick one AI skill your job needs (summarizing reports, drafting, analysing a spreadsheet) and practise it 15 "
      "minutes a day this week.\n\n"
      "Send this to the friend who's job hunting.\n\n#ai #futureofwork #jobs #careers #wef #hourback",
      "Which number surprised you? Sources: World Economic Forum, 'Future of Jobs Report 2025' (Jan 2025): 170 million jobs "
      "created and 92 million displaced by 2030 (net 78 million); employers expect 39% of core skills to change; AI and big data "
      "is the fastest-growing skill. Statistics Canada, 'Analysis on artificial intelligence use by businesses in Canada, second "
      "quarter of 2026' (June 11, 2026): 19.2%.")

# ---------------------------------------------------------------- Oct 24 08:45 · AI words, decoded (AI, for real · day 6)
cheat("hb-cheat-1024am-shortcuts", "2026-10-24T08:45",
      dict(brand=HB, field="plum", track="hb-x-ta-da-funk", beat=2.8,
           title="AI words, / *decoded*", head=("the word", "what it means"),
           rows=[("Model", "the trained AI"), ("Prompt", "what you ask it"), ("Token", "a word-piece"),
                 ("Training", "how it learned"), ("Hallucination", "a confident mistake"), ("Agent", "AI that takes actions")],
           do="This week, use *one* of these words at work, and explain it in *one sentence.*",
           save="send this to the friend nodding along in meetings",
           src="Plain-English definitions: OpenAI Help Center (tokens), OpenAI research (hallucinations, Sept 2025), Google AI glossary."),
      "AI words, decoded 📖\n\n"
      "Model: the trained AI itself (GPT, Gemini, Claude and Llama are model families).\n"
      "Prompt: what you type or say to it.\n"
      "Token: a word-piece. AI reads and writes in tokens; a short English word is often one token, a long one can be several.\n"
      "Training: how it learned, by studying huge amounts of text and learning which words tend to come next.\n"
      "Hallucination: a confident mistake, an answer that sounds right and isn't.\n"
      "Agent: AI that takes actions, like clicking through a website for you, not just answering.\n\n"
      "Why it matters: when you can explain these in one sentence, AI stops being magic and starts being a tool you can judge.\n\n"
      "Do this: this week, use one of these words at work and explain it in one sentence.\n\n"
      "Send this to the friend nodding along in meetings.\n\n#ai #learnai #chatgpt #aiglossary #futureofwork #hourback",
      "Which word was new to you? Sources: OpenAI Help Center, 'What are tokens and how to count them?' (tokens are pieces of "
      "words); OpenAI, 'Why language models hallucinate' (Sept 2025); Google, Machine Learning Glossary (model, training). "
      "Definitions simplified for a general audience.")

# ---------------------------------------------------------------- Oct 25 19:00 · where AI already lives in your apps (AI, for real · day 7, part 2/2)
cheat("hb-cheat-1025-voice-words", "2026-10-25T19:00",
      dict(brand=HB, field="plum", track="hb-x-ta-da-funk", beat=2.8,
           title="Where AI already / *lives in your apps*", head=("the app", "the AI inside"),
           rows=[("WhatsApp, Instagram", "Meta AI"), ("iPhone 15 Pro and up", "Apple Intelligence"), ("Android, Gmail", "Gemini"),
                 ("Windows, Edge", "Copilot"), ("Google Search", "AI Overviews"), ("Chrome", "Gemini in Chrome")],
           do="Pick *one* of these. Use it on a real task, then *check its work.*",
           save="send this to the friend who says “I don't use AI”",
           src="Meta (1B monthly Meta AI users, May 2025) · Apple Intelligence · Google Gemini, AI Overviews, Gemini in Chrome · Microsoft Copilot."),
      "Where AI already lives in your apps 📱 Part 2 of 2.\n\n"
      "WhatsApp, Instagram, Facebook, Messenger: Meta AI (Meta says about a billion people use it every month).\n"
      "iPhone 15 Pro and newer: Apple Intelligence (Writing Tools, summaries, Clean Up in Photos).\n"
      "Android and Gmail: Gemini.\n"
      "Windows and the Edge browser: Copilot.\n"
      "Google Search: AI Overviews at the top of results.\n"
      "Chrome: Gemini in Chrome.\n\n"
      "Why it matters: you don't have to go looking for AI. It's already in the apps you open every day, so learning it on "
      "purpose beats using it by accident.\n\n"
      "Do this: pick one of these, use it on a real task, then check its work (fluent isn't true).\n\n"
      "Features vary by device, plan and country.\n\n"
      "Send this to the friend who says \"I don't use AI\".\n\n#ai #metaai #appleintelligence #gemini #copilot #hourback",
      "Which one do you use without noticing? Sources: CNBC (May 28, 2025), Meta AI 1 billion monthly active users; Apple, "
      "Apple Intelligence (iPhone 15 Pro and later); Google, Gemini app, Gemini in Gmail, AI Overviews in Search, Gemini in "
      "Chrome (Sept 2025); Microsoft, Copilot in Windows and Edge.")


def add_to_schedule(path):
    import json
    from pathlib import Path
    d = json.loads(Path(path).read_text())
    ids = {x["id"] for x in d["posts"]}
    for pid, m in META.items():
        if pid in ids:
            d["posts"] = [x for x in d["posts"] if x["id"] != pid]
        sp = CHEATS[pid]
        rows = sp.get("rows") or [(c["name"], "; ".join(c["lines"])) for c in sp["cards"]]
        alt = (f"Canada-edition cheat sheet in the Hourback editorial look. Title: {sp['title'].replace('*', '').replace(' / ', ' ')}. "
               + " · ".join(f"{a}: {b}" for a, b in rows) + f". Do this: {sp['do'].replace('*', '')}")
        e = dict(id=pid, account="hourback", publish_at=m["at"] + ":00-04:00", caption=m["caption"], first_comment=m["comment"],
                 alt_text=alt, video=f"reels/{pid}.mp4", cover=f"reels/{pid}-cover.jpg")
        if "am-" in pid:
            e["trial"] = "auto"
        d["posts"].append(e)
    d["posts"].sort(key=lambda x: (x["publish_at"], x["account"], x["id"]))
    Path(path).write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")

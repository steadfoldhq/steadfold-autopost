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


# ---------------------------------------------------------------- Oct 19 08:45 · CRA jobs you can do online
cheat("hb-cheat-1019am-cra-online", "2026-10-19T08:45",
      dict(brand=HB, field="indi", track="hb-x-smart-bounce",
           title="Skip the CRA / *hold music*", head=("instead of calling…", "do it online"),
           rows=[("Moved?", "new address"), ("Refund status?", "track it"), ("Proof of income?", "print it"),
                 ("Benefit dates?", "see them"), ("Return mistake?", "fix it")],
           do="Sign in to *CRA My Account* once. Skip the phone queue.",
           save="send this to whoever does the taxes",
           src="canada.ca · CRA My Account: change your address, follow your refund, print proof of income, check benefit payments, change your return."),
      "Skip the CRA hold music 🇨🇦\n\nThese are all jobs you can do yourself in CRA My Account:\n"
      "Moved? Change your address.\nWaiting on a refund? Track it.\nNeed proof of income for a lease or loan? Print it.\n"
      "Wondering when your benefit lands? See the payment dates.\nSpotted a mistake on your return? Change it online.\n\n"
      "Do this: sign in to CRA My Account once (search \"CRA My Account\" on canada.ca). Next time it's a few taps, not a phone queue.\n\n"
      f"Send this to whoever does the taxes in your house.\n\n{TAGS} #cra #taxes #personalfinancecanada",
      "Which one would you use first? Source: CRA, 'My Account' (canada.ca): check benefit and credit payments, view or change your "
      "tax return and follow your refund, update your address and set up direct deposit, view and print a proof of income statement.")

# ---------------------------------------------------------------- Oct 20 08:45 · spam shut-off
cheat("hb-cheat-1020am-spam-off", "2026-10-20T08:45",
      dict(brand=HB, field="orng", track="hb-x-future-easy",
           title="Spam texts and calls: / the *shut-off* sheet", head=("if you get…", "do this"),
           rows=[("Spam texts", "forward to 7726"), ("Sales calls", "join the DNCL"), ("No internet?", "1-866-580-3625"),
                 ("Store emails", "a Gmail filter")],
           do="Today, put your numbers on the *National Do Not Call List.*",
           save="send this to your parents",
           src="CRTC · National Do Not Call List (lnnte-dncl.gc.ca, 1-866-580-3625) · 7726 spells SPAM; free to report (Consumer Protection BC)."),
      "Spam texts and calls: the shut-off sheet 🇨🇦\n\n"
      "Spam text? Forward it to 7726 (it spells SPAM on the keypad). Reporting is free.\n"
      "Sales calls? Register your numbers on the National Do Not Call List: lnnte-dncl.gc.ca, or call 1-866-580-3625.\n"
      "Store emails every morning? One Gmail filter sends them past your inbox (how-to on our Oct 20 post).\n\n"
      "Do this: today, add your cell and home numbers to the Do Not Call List. It won't stop every call: some, like charities and "
      "political parties, are still allowed to call.\n\n"
      f"Send this to your parents.\n\n{TAGS} #spamcalls #scamalert #donotcall",
      "Sources: CRTC, 'What you should know about telemarketing in Canada' (register at lnnte-dncl.gc.ca or 1-866-580-3625, "
      "TTY 1-888-362-5889); Consumer Protection BC, forward spam texts to 7726 (SPAM), free to report.")

# ---------------------------------------------------------------- Oct 21 08:45 · set it up once
cheat("hb-cheat-1021am-set-once", "2026-10-21T08:45",
      dict(brand=HB, field="yel", track="hb-x-ta-da-funk",
           title="Set it up *once.* / Never chase it again", head=("instead of…", "set up"),
           rows=[("Waiting for a cheque", "direct deposit"), ("Answering e-Transfers", "Autodeposit"),
                 ("Missing CRA letters", "email alerts"), ("Paying bills by hand", "auto-pay")],
           do="Tonight, turn on *Autodeposit* in your *bank app.*",
           save="send this to whoever runs the house admin",
           src="CRA My Account: direct deposit, email notifications (canada.ca) · Interac Autodeposit: no security question (National Bank Help Centre)."),
      "Set it up once. Never chase it again 🇨🇦\n\n"
      "Waiting for a CRA cheque? Set up direct deposit in My Account.\n"
      "Answering e-Transfer security questions? Turn on Autodeposit in your bank app and money lands on its own.\n"
      "Missing CRA letters? Turn on email notifications in My Account.\n"
      "Paying the same bills by hand? Set up auto-pay with the company or your bank.\n\n"
      "Do this: tonight, open your bank app and turn on Interac e-Transfer Autodeposit.\n\n"
      f"Send this to whoever runs the house admin.\n\n{TAGS} #etransfer #cra #moneytips",
      "Sources: CRA My Account (canada.ca): set up direct deposit, receive email notifications; National Bank Help Centre, "
      "'What is Interac e-Transfer Autodeposit?' (funds are deposited automatically, no security question). Setup is in your own bank's app.")

# ---------------------------------------------------------------- Oct 22 19:00 · travel admin
cheat("hb-cheat-1022-travel-admin", "2026-10-22T19:00",
      dict(brand=HB, field="plum", track="hb-x-smart-bounce",
           title="Travel admin, / the *fast way*", head=("the job", "the fast way"),
           rows=[("Renew a passport", "online"), ("Standard wait", "20 business days"), ("Need it sooner?", "go in person"),
                 ("Flying home?", "declare ahead"), ("How early?", "up to 72 h")],
           do="Flying home? Do the *Advance Declaration* in *ArriveCAN.*",
           save="save this before your next trip ✈️",
           src="IRCC, July 2026: online passport renewal for eligible adults in Canada, 20 business days · CBSA: Advance Declaration in ArriveCAN, up to 72 h before arrival."),
      "Travel admin, the fast way 🇨🇦\n\n"
      "Passport: eligible adults in Canada can now renew online, with a digital photo from a commercial photographer. "
      "Standard processing is 20 business days. Need it sooner? Apply in person for faster service.\n"
      "Flying home: do your customs and immigration declaration in ArriveCAN up to 72 hours before you land "
      "(Advance Declaration, at participating airports).\n\n"
      "Do this: before your next flight home, open ArriveCAN and do the Advance Declaration.\n\n"
      f"Save this before your next trip.\n\n{TAGS} #passport #arrivecan #travelcanada",
      "Sources: IRCC news release, 'Canada expands online passport renewal to all eligible adults' (July 2026): 20-business-day "
      "standard, faster options in person only; CBSA, 'ArriveCAN: Advance CBSA Declaration' (submit up to 72 hours before arrival, "
      "participating airports).")

# ---------------------------------------------------------------- Oct 24 08:45 · computer shortcuts (built Oct 18 pm)
cheat("hb-cheat-1024am-shortcuts", "2026-10-24T08:45",
      dict(brand=HB, field="plum", track="hb-x-ta-da-funk",
           title="Computer shortcuts / that *save clicks*", head=("to…", "Windows · Mac"),
           rows=[("Reopen a closed tab", "Ctrl+Shift+T · ⌘+Shift+T"), ("Snip part of the screen", "Win+Shift+S · ⌘+Shift+4"),
                 ("Switch apps", "Alt+Tab · ⌘+Tab"), ("Open any app", "Win, type · ⌘+Space"),
                 ("Your last 25 copies", "Win+V · Windows only")],
           do="Close a tab by mistake today? Press *Ctrl+Shift+T.* It comes back.",
           save="send this to the friend who clicks everything",
           src="Microsoft: clipboard history (Win+V, 25 items), Snipping Tool (Win+Shift+S) · Apple: screenshots (⌘+Shift+4), Spotlight (⌘+Space) · Chrome, Edge, Firefox, Safari: reopen tab."),
      "Computer shortcuts that save clicks 💻\n\n"
      "Reopen a tab you just closed: Ctrl+Shift+T (Windows) or Command+Shift+T (Mac).\n"
      "Screenshot just part of the screen: Windows+Shift+S, or Command+Shift+4.\n"
      "Jump between open apps: Alt+Tab, or Command+Tab.\n"
      "Open any app or file: press the Windows key and type, or Command+Space and type.\n"
      "See the last 25 things you copied: Windows+V (turn it on the first time). Windows only.\n\n"
      "Do this: next time you close a tab by mistake, press Ctrl+Shift+T. It comes right back.\n\n"
      f"Send this to the friend who clicks everything.\n\n{TAGS} #keyboardshortcuts #windows #mac",
      "Which one did you not know? Sources: Microsoft, 'Clipboard history' (Windows logo key + V, turn on the first time, up to 25 "
      "items); Microsoft Snipping Tool (Windows logo key + Shift + S); Apple, 'Take a screenshot on your Mac' (Command-Shift-4) and "
      "Spotlight (Command-Space); Online Tech Tips, reopen closed tab: Ctrl+Shift+T on Windows (Chrome, Edge, Firefox), "
      "Command+Shift+T on Mac (Chrome, Safari, Firefox).")

# ---------------------------------------------------------------- Oct 25 19:00 · voice typing commands (part 2 of 2)
cheat("hb-cheat-1025-voice-words", "2026-10-25T19:00",
      dict(brand=HB, field="plum", track="hb-x-ta-da-funk",
           title="Talk-to-text: / the *magic words*", head=("say…", "you get"),
           rows=[("“comma”", ","), ("“period”", "."), ("“question mark”", "?"), ("“new line”", "a new line"),
                 ("“new paragraph”", "a blank line")],
           do="Next text, tap the *mic* and say *“question mark”* out loud.",
           save="send this to the slowest texter you know",
           src="Apple Support, Commands for dictating text (comma, period, question mark, new line, new paragraph). Android's Gboard voice typing has similar commands."),
      "Talk-to-text: the magic words 🎙️ Part 2 of 2.\n\n"
      "Say \"comma\" and you get a comma.\nSay \"period\" for a full stop.\nSay \"question mark\" for a question mark.\n"
      "Say \"new line\" to start a new line.\nSay \"new paragraph\" for a blank line.\n\n"
      "Newer iPhones add a lot of punctuation on their own, and these words fill the gaps.\n\n"
      "Do this: next text, tap the mic on your keyboard and say \"question mark\" out loud. Then read it once before you send.\n\n"
      f"Send this to the slowest texter you know.\n\n{TAGS} #voicetyping #iphonetips #texting",
      "Which word will you use most? Source: Apple Support, 'Commands for dictating text' (comma, period, question mark, "
      "exclamation mark, new line, new paragraph). Android's Gboard voice typing supports similar spoken punctuation; menus vary by phone.")


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

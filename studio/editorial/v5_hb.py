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



# ================================================================== Oct 19-22 · "GET AN HOUR BACK" REBUILD (Oct 18 am)
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
hchain("hb-ch-1019b", HB, "2026-10-19", "hb19", "hourback · quick quiz", [
    dict(k="bubbles", f="plum", label="quick quiz", title="On an iPhone, / type *omw.*", bubbles=[
        ("in", "what happens?"), ("out", "A) nothing"), ("out", "B) it turns into a whole sentence")], tap="guess, then tap →"),
    dict(k="payoff", f="orng", label="the answer: B", text="“On my / *way!*”", sub="it's built in, and you can add your own", obj="phone",
         tap="tap →"),
    dict(k="payoff", f="plum", label="make your own", text="Type *@@.* / Get your / whole email.", sub="same trick for your address",
         obj="point", tap="next story →"),
    dict(k="handoff", f="orng", label="today's swap", text="Stop typing / your *address.*", img="hb-1019-text-shortcut/01.jpg", next="tonight: fewer buzzes"),
])

hpost("hb-1019-text-shortcut", HB, "2026-10-19T13:00", "keep",
      dict(lay="pills", f="plum", kicker="hourback · the swap", text="Stop typing / your *address.* / Type *@@.*", obj="phone", at="br",
           save="your phone can finish it"),
      [dict(k="say", f="orng", label="sound familiar?", size=126,
            text="Forms. Emails. / Delivery apps. / Your *full address,* / again and again."),
       dict(k="rows", f="plum", text="The *swap*", cap="text replacement", rows=[("you type", "@@"), ("it writes", "your email"),
                                                                                 ("you type", "hhh"), ("it writes", "your address")]),
       dict(k="steps", f="orng", text="iPhone, *once*", items=["Settings → General → Keyboard", "Text Replacement → +",
                                                              "Phrase: your email. Shortcut: @@"]),
       dict(k="do", f="plum", text="Tonight, make one shortcut: *@@* for your email. Then try it in any app.",
            save="send this to the friend who types it all out")],
      "Forms, emails, delivery apps: you type your full address and email over and over.\n\n"
      "The swap: make a shortcut once. Type @@ and your phone writes your whole email. Type hhh and it writes your address.\n\n"
      "Do this (iPhone): Settings → General → Keyboard → Text Replacement → +. Phrase: your email. Shortcut: @@. "
      "Pick shortcuts you'd never type by accident.\n\n"
      "Android: Gboard has a personal dictionary where each word can have a shortcut; look under Gboard's Dictionary settings "
      "(menus vary by phone).\n\n"
      f"Send this to the friend who types it all out.\n\n{HBTAGS} #iphone #typing",
      "Source: AbilityNet, 'How to use text replacement in iOS 26' (Settings → General → Keyboard → Text Replacement). "
      "iPhones come with one shortcut already: omw → On my way!")

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

reel("hb-reel-1019-wifi-qr", HB, "2026-10-19T19:00", "deep", "hb-x-ta-da-funk", "there's a faster way", [
    dict(k="hook", f="plum", text="“What's the / *Wi-Fi?*”", emo="💬"),
    dict(k="say", f="orng", text="And you're / behind the TV, / reading a / *tiny sticker.*"),
    dict(k="because", f="plum", kicker="here's the swap", text="Your iPhone can turn the password into a *QR code.*"),
    dict(k="list", f="orng", items=["They *scan it.*", "They're *on.*"], size=130, drop=True),
    dict(k="say", f="plum", text="No more / *“capital Q,* / *zero, not O…”*"),
    dict(k="do", f="orng", text="Passwords app → Wi-Fi → your network → *Show Network QR Code.*"),
    dict(k="save", f="plum", text="send this to / whoever owns / the router"),
], "\"What's the Wi-Fi?\" And you're behind the TV reading a tiny sticker.\n\n"
   "The swap: your iPhone can show the Wi-Fi password as a QR code. Guests point their camera at it and they're on. "
   "No more \"capital Q, zero, not O…\"\n\n"
   "Do this (iPhone, iOS 18 or later): Passwords app → Wi-Fi → your network → Show Network QR Code.\n"
   "Android: open Wi-Fi settings, tap your network, then Share (menus vary by phone).\n\n"
   "Anyone who scans it gets the password, so share it with people you trust.\n\n"
   f"Send this to whoever owns the router.\n\n{HBTAGS} #wifi #guests",
   "Source: AppleInsider, 'How to share a Wi-Fi QR code in iOS 18' (Passwords → Wi-Fi → network → Show Network QR Code); "
   "Apple Passwords User Guide ('Show Network QR Code').")

# ================================================================== Oct 20 (Story chain day)
hchain("hb-ch-1020b", HB, "2026-10-20", "hb20", "hourback · the swap", [
    dict(k="photo", text="Delete. / Delete. / *Delete.*", sub="every morning, same store emails →", ink="light", y=560),
    dict(k="bubbles", f="plum", label="sound familiar?", bubbles=[
        ("in", "why is your inbox at *2,481?*"), ("out", "it's just store emails"), ("in", "so… delete them?"),
        ("out", "I do. *every morning* 😩")], obj="phone"),
    dict(k="bubbles", f="orng", label="the swap", bubbles=[
        ("out", "make *one filter* for that store"), ("out", "tick *Skip the Inbox*"), ("in", "and they just… go away?"),
        ("out", "yes. still there if you *search*")]),
    dict(k="payoff", f="plum", label="the catch", text="Do it on a / *computer.*", sub="the Gmail app can't make filters", obj="point",
         tap="next story →"),
    dict(k="handoff", f="orng", label="today's swap", text="Delete. Delete. / *Delete.*", img="hb-1020-inbox-filter/01.jpg", next="tonight: shorter meetings"),
])

hpost("hb-1020-inbox-filter", HB, "2026-10-20T13:00", "keep",
      dict(lay="pills", f="plum", kicker="hourback · the swap", text="Delete. Delete. / *Delete.* / Every morning.", obj="chat", at="bl",
           save="there's a one-time fix"),
      [dict(k="say", f="orng", label="the swap", size=126,
            text="Make a *filter* once. / That store's emails / *skip your inbox* / from now on.", sub="still there if you search"),
       dict(k="steps", f="plum", text="On a *computer*", items=["Open one of those emails", "⋮ → Filter messages like these",
                                                               "Create filter → Skip the Inbox"]),
       dict(k="say", f="orng", label="what you get back", size=126,
            text="Open your inbox: / *just people.* / Not stores."),
       dict(k="do", f="plum", text="Tonight, pick the *one store* that emails you most. Make its filter. Done.",
            save="send this to the friend at 2,481 unread")],
      "Delete. Delete. Delete. Every morning, the same store emails.\n\n"
      "The swap: one Gmail filter. That sender's emails skip your inbox from now on, and they're still there if you search.\n\n"
      "Do this, on a computer (the Gmail app can't make filters): open one of those emails → ⋮ → Filter messages like these → "
      "Create filter → tick Skip the Inbox (Archive it) → Create filter.\n\n"
      "What you get back: you open your inbox and it's just people.\n\n"
      f"Send this to the friend at 2,481 unread.\n\n{HBTAGS} #gmail #inboxzero #email",
      "Source: Gmail filter steps (open an email → ⋮ → Filter messages like these → Create filter → Skip the Inbox). "
      "Filters are made on the computer version of Gmail and then work on your phone too.")

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

reel("hb-reel-1020-grocery-list", HB, "2026-10-20T19:00", "deep", "hb-x-smart-bounce", "no reply…", [
    dict(k="hook", f="indi", text="“Do we need / *milk?*” / texted from / aisle 7.", emo="💬"),
    dict(k="say", f="yel", text="No reply. / You buy milk. / Now there are / *three milks.*"),
    dict(k="because", f="indi", kicker="here's the swap", text="One *shared list* the whole house adds to all week."),
    dict(k="list", f="yel", items=["Produce · *bananas*", "Dairy · *milk*", "Frozen · *peas*"], size=110, drop=True),
    dict(k="say", f="indi", text="On iPhone, / Reminders *sorts it* / *by section* / for you."),
    dict(k="do", f="yel", text="Reminders → Add List → List Type: *Groceries.* Then share it with your house."),
    dict(k="save", f="indi", text="send this to / whoever does / the shopping"),
], "\"Do we need milk?\" texted from aisle 7. No reply. Now there are three milks.\n\n"
   "The swap: one shared grocery list the whole house adds to all week. On iPhone, Reminders sorts it into sections like Produce "
   "and Frozen as you type.\n\n"
   "Do this (iPhone, iOS 17 or later, iCloud on for Reminders): Reminders → Add List → List Type → Groceries. Then share the list "
   "with your house.\n"
   "Android: a shared list in Google Keep works too.\n\n"
   f"Send this to whoever does the shopping.\n\n{HBTAGS} #grocerylist #mealplanning #familylife",
   "Source: Apple Support, 'Create grocery lists in Reminders on your iPhone' (List Type: Groceries, auto-sorted into categories, "
   "iOS 17 and later).")

# ================================================================== Oct 21 (quiz day)
hchain("hb-ch-1021b", HB, "2026-10-21", "hb21", "hourback · quick quiz", [
    dict(k="bubbles", f="plum", label="quick quiz", title="Your phone can / *copy text* / from a photo.", bubbles=[
        ("in", "on which phones?"), ("out", "A) only the newest ones"), ("out", "B) iPhones back to 2018")], tap="guess, then tap →"),
    dict(k="payoff", f="orng", label="the answer: B", text="*iPhone XS* / and newer", sub="on Android, Google Lens does it", obj="phone",
         tap="source: Apple Support · tap →"),
    dict(k="payoff", f="plum", label="so stop squinting", text="Copy it. / Don't *type it.*", sub="tracking numbers, phone numbers, recipes",
         obj="point", tap="next story →"),
    dict(k="handoff", f="orng", label="today's swap", text="Stop typing / what's *in a photo.*", img="hb-1021-copy-from-photo/01.jpg", next="tonight: the refund email"),
])

hpost("hb-1021-copy-from-photo", HB, "2026-10-21T13:00", "keep",
      dict(lay="pills", f="plum", kicker="hourback · the swap", text="Stop typing / what's already / *in a photo.*", obj="phone", at="br",
           save="your camera can copy it"),
      [dict(k="say", f="orng", label="sound familiar?", size=126,
            text="Squinting at a / tracking number. / Typing it in. / *One digit wrong.*"),
       dict(k="say", f="plum", label="the swap", size=126,
            text="Open the photo. / *Touch and hold* / the text. / Tap *Copy.*", sub="on iPhone it's called Live Text"),
       dict(k="rows", f="orng", text="Works *on*", rows=[("iPhone", "XS and newer"), ("Android", "Google Lens")]),
       dict(k="do", f="plum", text="Next code or number you see: *photo it,* touch and hold, *Copy.* Check it before you send.",
            save="send this to the friend who retypes everything")],
      "Squinting at a tracking number, typing it in, getting one digit wrong.\n\n"
      "The swap: copy the text straight out of a photo. On iPhone it's called Live Text: open the photo, touch and hold the words, "
      "tap Copy. Phone numbers and emails become tappable too. On Android, Google Lens does the same.\n\n"
      "Do this: next time you need a code, a number or a recipe, photo it, touch and hold, Copy.\n\n"
      "Where not to trust it: it can misread small or blurry text (0 and O look alike). Check it before you send or pay.\n\n"
      f"Send this to the friend who retypes everything.\n\n{HBTAGS} #livetext #googlelens",
      "Source: Apple Support, 'Copy and translate text from photos on your iPhone or iPad': Live Text works on iPhone XS, iPhone XR "
      "and later with iOS 15 or later (turn on in Settings → General → Language & Region).")

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

reel("hb-reel-1021-camera-translate", HB, "2026-10-21T19:00", "deep", "hb-x-future-easy", "your camera can read it", [
    dict(k="hook", f="plum", text="The school form / is *in French.* / Due tomorrow.", emo="📄"),
    dict(k="say", f="orng", text="You took French / in grade 9. / *That's it.*"),
    dict(k="because", f="plum", kicker="here's the swap", text="Point your *camera* at it. The English shows up on the page."),
    dict(k="list", f="orng", items=["Sortie scolaire · *field trip*", "Date limite · *deadline*"], size=104, drop=True),
    dict(k="say", f="plum", text="Small or fancy / text can come / out *wrong.* / Signing it? / *Ask the school.*"),
    dict(k="do", f="orng", text="Google Translate app → *Camera* → point at the page."),
    dict(k="save", f="plum", text="send this to / the parents' / group chat"),
], "The school form is in French. It's due tomorrow. You took French in grade 9, and that's it.\n\n"
   "The swap: point your camera at it. In the Google Translate app, tap Camera and the English shows up on top of the page. "
   "On iPhone, you can also open a photo, tap the Live Text button, then Translate.\n\n"
   "Where not to trust it: small, unclear or fancy text may not translate right. If you're signing something, ask the school "
   "what it says.\n\n"
   f"Send this to the parents' group chat.\n\n{HBTAGS} #googletranslate #schoolforms #canadianparents",
   "Sources: Google Translate Help, 'Translate images' (Camera; small, unclear or stylized text may not be accurate); "
   "Apple Support, 'Copy and translate text from photos' (Live Text → Translate).")

# ================================================================== Oct 22 (Story chain day)
hchain("hb-ch-1022", HB, "2026-10-22", "hb19", "hourback · the swap", [
    dict(k="photo", text="“Unknown / *number.*” / Again.", sub="third one today →", ink="light", y=560),
    dict(k="bubbles", f="plum", label="sound familiar?", bubbles=[
        ("in", "📞 Unknown caller"), ("out", "hello?"), ("in", "*Congratulations!* You've been selected…")], obj="phone"),
    dict(k="bubbles", f="orng", label="the swap", bubbles=[
        ("out", "Settings → Apps → Phone"), ("out", "Screen Unknown Callers → *Silence*"),
        ("in", "so mum still gets through?"), ("out", "if she's *in your contacts,* yes")]),
    dict(k="payoff", f="plum", label="the catch", text="Save the / *dentist.*", sub="silenced calls go to voicemail, so check it",
         obj="point", tap="next story →"),
    dict(k="handoff", f="orng", label="today's swap", text="Unknown number. / *Again.*", img="hb-1022-unknown-callers/01.jpg", next="tonight: the 11 pm list"),
])

hpost("hb-1022-unknown-callers", HB, "2026-10-22T13:00", "keep",
      dict(lay="pills", f="plum", kicker="hourback · the swap", text="Unknown / number. / *Again.*", obj="point", at="bl",
           save="you don't have to pick up"),
      [dict(k="say", f="orng", label="sound familiar?", size=126,
            text="You answer. / *“Congratulations,* / *you've been* / *selected…”*"),
       dict(k="say", f="plum", label="the swap", size=126,
            text="Unknown numbers / go straight / to *voicemail.*", sub="your people still ring through"),
       dict(k="steps", f="orng", text="iPhone", items=["Settings → Apps → Phone", "Screen Unknown Callers", "Choose Silence"]),
       dict(k="do", f="plum", text="Today, save your *doctor, school and dentist* as contacts. Then turn on *Silence.*",
            save="send this to the friend who still answers")],
      "Unknown number. Again. You answer and it's \"Congratulations, you've been selected…\"\n\n"
      "The swap: let unknown numbers go to voicemail. Calls from people in your contacts still ring through.\n\n"
      "Do this (iPhone): Settings → Apps → Phone → Screen Unknown Callers → Silence. First, save the numbers you can't miss: "
      "doctor, school, dentist, daycare.\n\n"
      "The catch: silenced calls still leave voicemails, so check them. On Android, look in your Phone app's settings for spam "
      "and unknown-caller options (menus vary by phone).\n\n"
      f"Send this to the friend who still answers.\n\n{HBTAGS} #spamcalls #iphone",
      "Source: Apple Support, 'Manage unknown callers on iPhone' (Settings → Apps → Phone → Screen Unknown Callers → Silence: "
      "unknown numbers are silenced and sent to voicemail).")

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
reel("hb-reel-1023am-photo-search", HB, "2026-10-23T08:45", "deep", "hb-x-future-easy", "stop scrolling for it", [
    dict(k="hook", f="indi", text="Scrolling for / *one photo.* / Again.", emo="📸"),
    dict(k="say", f="yel", text="The parking spot. / The receipt. / Somewhere in / *4,000 photos.*"),
    dict(k="because", f="indi", kicker="here's the swap", text="Your phone already knows *what's in* your photos."),
    dict(k="list", f="yel", items=["Type *receipt*", "Type *dog*", "Type *passport*"], size=120, drop=True),
    dict(k="say", f="indi", text="It can even find / *words* inside / a photo."),
    dict(k="do", f="yel", text="Open Photos, tap *Search,* and type one word: *receipt.*"),
    dict(k="save", f="indi", text="send this to / the friend with / 9,000 photos", next="part 2 tonight: storage full?"),
], "Scrolling for one photo. Again. The parking spot, the receipt, somewhere in 4,000 photos.\n\n"
   "The swap: search your photos by what's in them. Your phone already recognises things like receipts, dogs and documents, and it "
   "can find words written inside a photo too.\n\n"
   "Do this (iPhone): open Photos, tap Search (the magnifying glass at the bottom in iOS 26), and type one word, like \"receipt\".\n"
   "Android: open Google Photos, tap Search, and type the same.\n\n"
   "Where not to trust it: it can miss a photo, so if it's not there, scroll the date you think it was taken.\n\n"
   f"Send this to the friend with 9,000 photos. Part 2 tonight at 7: storage full?\n\n{HBTAGS} #iphonephotos #googlephotos",
   "Sources: Apple iPhone User Guide, 'Search for photos and videos in Photos'; SwitchingToMac, 'How to search photos on iPhone (iOS 26)': "
   "Search has its own tab in iOS 26 and matches against an on-device index of recognised faces, places, objects and text in images.",
   series="Photo time-savers · part 1/2")

hchain("hb-ch-1023", HB, "2026-10-23", "hb19", "hourback · quick quiz", [
    dict(k="bubbles", f="plum", label="quick quiz", title="Find the receipt / photo *fast.*", bubbles=[
        ("in", "what's quicker?"), ("out", "A) scroll back by date"), ("out", "B) type *receipt* in Search")], tap="guess, then tap →"),
    dict(k="payoff", f="orng", label="the answer: B", text="Type / *“receipt.”*", sub="Photos knows what's in your pictures", obj="phone",
         tap="source: Apple · tap →"),
    dict(k="payoff", f="plum", label="it even reads", text="Words *inside* / a photo.", sub="signs, labels, screenshots", obj="point",
         tap="next story →"),
    dict(k="handoff", f="orng", label="today's swap", text="Expired licence? / *Get a reminder.*", img="hb-1023-renewal-reminders/01.jpg",
         next="tonight: storage full?"),
])

hpost("hb-1023-renewal-reminders", HB, "2026-10-23T13:00", "keep",
      dict(lay="pills", f="plum", kicker="hourback · ontario", text="“Your licence / expired / *last month.*”", obj="point", at="bl",
           save="Ontario has a free fix"),
      [dict(k="say", f="orng", label="sound familiar?", size=126,
            text="Licence. Health card. / Plate. Photo card. / Each one expires / *on its own date.*"),
       dict(k="rows", f="plum", text="The *free* reminder", cap="ServiceOntario · Ontario only",
            rows=[("You pick", "email, text or call"), ("First one", "60 days before"), ("Second one", "30 days before")]),
       dict(k="do", f="orng", text="Today, search *ServiceOntario renewal reminders* and sign up. Have your licence and health card handy.",
            save="send this to your Ontario friends")],
      "\"Your licence expired last month.\" Not what you want to hear at the counter.\n\n"
      "The swap: ServiceOntario's free renewal reminders. Sign up once and get an email, text or phone call 60 days and 30 days before "
      "your driver's licence, health card, licence plate or Ontario Photo Card expires.\n\n"
      "Do this: search \"ServiceOntario renewal reminders\" (ontario.ca) and sign up. Have your licence, health card and plate number "
      "handy, and make sure your address is up to date first.\n\n"
      "Outside Ontario? Check your province's website for the same kind of reminder.\n\n"
      f"Send this to your Ontario friends.\n\n{HBTAGS} #ontario #serviceontario #lifeadmin",
      "Source: ontario.ca, 'Get ServiceOntario renewal reminders': free reminders by email, text or phone call for licence plates, "
      "driver's licences, health cards and Ontario Photo Cards, 60 and 30 days before expiry (plus one 30 days after, if not renewed).")

reel("hb-reel-1023-duplicates", HB, "2026-10-23T19:00", "deep", "hb-x-smart-bounce", "free up space tonight", [
    dict(k="hook", f="plum", text="*“Storage full.”* / Again.", emo="📱"),
    dict(k="say", f="orng", text="And some of it / is the *same photo,* / saved twice."),
    dict(k="because", f="plum", kicker="here's the swap", text="Photos gathers your *duplicates* into one album for you."),
    dict(k="list", f="orng", items=["Collections", "Utilities", "*Duplicates*"], size=120, drop=True),
    dict(k="say", f="plum", text="Tap *Merge.* / It keeps the / *best copy.*"),
    dict(k="do", f="orng", text="Tonight: Photos → Collections → Utilities → *Duplicates* → Merge."),
    dict(k="save", f="plum", text="send this to / whoever's phone / is always full", next="photo time-savers · part 2/2"),
], "\"Storage full.\" Again. And some of it is the same photo, saved twice.\n\n"
   "The swap: your iPhone's Photos app gathers duplicates into one album. Tap Merge and it keeps the best-quality copy, with the "
   "details from both. The extra copies go to Recently Deleted, so you can still get them back for a while.\n\n"
   "Do this (iPhone, iOS 16 or later): Photos → Collections → Utilities → Duplicates → Merge.\n\n"
   "Where not to trust it: some pairs are only near-copies. Look before you merge those.\n\n"
   f"Send this to whoever's phone is always full. Part 2 of 2.\n\n{HBTAGS} #iphonestorage #iphonephotos",
   "Sources: Technobezz, 'How to remove duplicate photos on iPhone' (Photos → Collections → Utilities → Duplicates; needs iOS 16 or "
   "later; Merge keeps the best-quality copy and relevant metadata, others go to Recently Deleted); Cult of Mac (merging only exact "
   "copies vs all selected).",
   series="Photo time-savers · part 2/2")

# ------------------------------------------------------------------ Oct 24 (Story chain day)
hchain("hb-ch-1024", HB, "2026-10-24", "hb21", "hourback · the swap", [
    dict(k="photo", text="“Leaving now!” / typed at a / *red light.*", sub="there's a safer way →", ink="light", y=560),
    dict(k="bubbles", f="indi", label="sound familiar?", bubbles=[
        ("in", "where are you??"), ("out", "5 min!"), ("in", "you said that *20 min ago*")], obj="phone"),
    dict(k="bubbles", f="yel", label="the swap", bubbles=[
        ("out", "start directions in Maps"), ("out", "tap *Share ETA*"), ("in", "so I can see you coming?"),
        ("out", "yes. it *updates* if I'm late")]),
    dict(k="payoff", f="indi", label="the catch", text="Do it / *before* / you drive.", sub="in Ontario, a red light still counts",
         obj="point", tap="next story →"),
    dict(k="handoff", f="yel", label="today's swap", text="Stop texting / *“5 more minutes.”*", img="hb-1024-share-eta/01.jpg",
         next="tonight: dinner from the fridge"),
])

hpost("hb-1024-share-eta", HB, "2026-10-24T13:00", "keep",
      dict(lay="pills", f="indi", kicker="hourback · the swap", text="Stop texting / *“5 more* / *minutes.”*", obj="phone", at="br",
           save="your map can do it"),
      [dict(k="say", f="yel", label="the swap", size=126,
            text="Start directions. / Tap *Share ETA.* / They see when / you'll *really* arrive.", sub="it updates if you're running late"),
       dict(k="rows", f="indi", text="Where to *find it*", cap="tap it before you pull out",
            rows=[("iPhone", "Maps · Share ETA"), ("Android", "Google Maps · Share trip")]),
       dict(k="do", f="yel", text="Next drive, tap *Share ETA* before you pull out. Pick the person waiting.",
            save="send this to the friend who's always 5 minutes away")],
      "\"Where are you?\" \"5 minutes!\" (It was not 5 minutes.)\n\n"
      "The swap: share your arrival time from your map app. They see when you'll really get there, and it updates if traffic slows "
      "you down. Sharing stops on its own when you arrive.\n\n"
      "Do this: start directions, then tap Share ETA (Apple Maps) or tap the trip card → Share trip progress (Google Maps), and pick "
      "the person waiting.\n\n"
      "The catch: set it up before you drive. In Ontario, holding your phone is illegal even when you're stopped at a red light.\n\n"
      f"Send this to the friend who's always 5 minutes away.\n\n{HBTAGS} #applemaps #googlemaps #commute",
      "Sources: Popular Science, 'How to share your ETA in Google Maps or Apple Maps' (Share ETA ends automatically on arrival; "
      "Google Maps: tap the bottom card → Share trip progress); Apple iPhone User Guide, 'Share your ETA in Maps'; ontario.ca, "
      "'What counts as distracted driving' (applies when stopped in traffic or at a red light; $615 fine for a first conviction "
      "settled out of court).")

reel("hb-reel-1024-fridge-dinner", HB, "2026-10-24T19:00", "deep", "hb-x-smart-bounce", "dinner, sorted", [
    dict(k="hook", f="indi", text="6 pm. / Full fridge. / *Nothing* for dinner.", emo="🥕"),
    dict(k="say", f="yel", text="Half a pepper. / Three eggs. / Some *spinach.*"),
    dict(k="because", f="indi", kicker="here's where AI helps", text="Snap the fridge. AI suggests *dinners* from what's really there."),
    dict(k="list", f="yel", items=["Spinach omelette · *10 min*", "Pepper fried eggs · *15 min*"], size=96, drop=True),
    dict(k="say", f="indi", text="But it *can't tell* / if food's gone off, / and it can / *misread* a label."),
    dict(k="do", f="yel", text="Tonight, photo your fridge, ask AI for *3 dinners,* and tell it any allergies."),
    dict(k="save", f="indi", text="send this to / whoever cooks / tonight"),
], "6 pm. Full fridge. Nothing for dinner.\n\n"
   "Where AI helps: take a photo of your fridge and ask a chat AI for 3 dinners using what's in it. Half a pepper, three eggs and "
   "some spinach become an omelette in 10 minutes.\n\n"
   "Where not to trust it: it can't tell if food has gone off, and it can misread what it sees. Check dates yourself, and always "
   "tell it about allergies.\n\n"
   "Do this: tonight, photo your fridge, ask AI for 3 dinners, and say any allergies.\n\n"
   f"Send this to whoever cooks tonight.\n\n{MADE}\n\n{HBTAGS} #mealideas #aitips #dinnerideas",
   "The fridge and dinner ideas in this Reel are made up for this post. Chat AIs that accept photos can misidentify foods and can't "
   "judge freshness or food safety: when in doubt, throw it out.")

# ------------------------------------------------------------------ Oct 25 (quiz day)
reel("hb-reel-1025am-talk-dont-type", HB, "2026-10-25T08:45", "deep", "hb-x-future-easy", "save your thumbs", [
    dict(k="hook", f="plum", text="Long text? / *Stop typing it.*", emo="🎙️"),
    dict(k="say", f="orng", text="Stanford tested / *talking* vs *typing* / on a phone."),
    dict(k="because", f="plum", kicker="the result", text="Talking was about *3 times faster,* with fewer mistakes.", drop=True),
    dict(k="say", f="orng", text="Tap the *mic* / on your keyboard. / Just talk."),
    dict(k="say", f="plum", text="Check *names* / and *numbers* / before you send."),
    dict(k="do", f="orng", text="Next long message, tap the *mic* on your keyboard and say it."),
    dict(k="save", f="plum", text="send this to / the slowest texter / you know", next="part 2 tonight: the magic words"),
], "Long text? Stop typing it.\n\n"
   "Stanford researchers tested talking against typing on a phone. Talking was about 3 times faster in English, with about 20% "
   "fewer errors.\n\n"
   "The swap: tap the microphone on your keyboard and just say it.\n\n"
   "Where not to trust it: names, numbers and addresses come out wrong the most. Read it once before you send.\n\n"
   "Do this: next long message, tap the mic and talk.\n\n"
   f"Send this to the slowest texter you know. Part 2 tonight at 7: the words that add punctuation.\n\n{HBTAGS} #voicetyping #texting",
   "Source: Stanford News (Aug 24, 2016), 'Smartphone speech recognition can write text messages three times faster than human "
   "typing': 32 people aged 19 to 32; speech was about 3x faster than typing in English with a 20.4% lower error rate (Ruan, "
   "Wobbrock, Liou, Ng & Landay, with Baidu).",
   series="Talk, don't type · part 1/2")

hchain("hb-ch-1025", HB, "2026-10-25", "hb20", "hourback · quick quiz", [
    dict(k="bubbles", f="indi", label="quick quiz", title="Family Sharing / on your iPhone?", bubbles=[
        ("in", "you already have…"), ("out", "A) nothing extra"), ("out", "B) a shared *Family* calendar")], tap="guess, then tap →"),
    dict(k="payoff", f="yel", label="the answer: B", text="A *Family* / calendar", sub="made for you, on everyone's iPhone", obj="phone",
         tap="source: Apple · tap →"),
    dict(k="payoff", f="indi", label="so use it", text="Who's driving / *to hockey?*", sub="add it once, everyone sees it", obj="point",
         tap="next story →"),
    dict(k="handoff", f="yel", label="today's swap", text="“Wait, *who's* / *driving?*”", img="hb-1025-family-calendar/01.jpg",
         next="tonight: the magic words"),
])

hpost("hb-1025-family-calendar", HB, "2026-10-25T13:00", "keep",
      dict(lay="pills", f="indi", kicker="hourback · the swap", text="“Wait, *who's* / *driving* / to hockey?”", obj="chat", at="bl",
           save="one calendar fixes it"),
      [dict(k="say", f="yel", label="sound familiar?", size=126,
            text="Dentist. Hockey. / Grandma's birthday. / All in *one* / person's head."),
       dict(k="say", f="indi", label="the swap", size=126,
            text="One *shared* / calendar. / Add it once, / *everyone* sees it.", sub="your phone may have made one already"),
       dict(k="rows", f="yel", text="Where to *find it*", cap="made when you set up a family group",
            rows=[("iPhone", "Calendar · Family"), ("Android", "Google Calendar · Family")]),
       dict(k="do", f="indi", text="Tonight, add *this week's* plans to the Family calendar. Then tell everyone to look there.",
            save="send this to your family group chat")],
      "Dentist, hockey, grandma's birthday: all in one person's head.\n\n"
      "The swap: one shared calendar the whole house can see. Add a plan once and it shows up on everyone's phone.\n\n"
      "You may already have one. On iPhone, Family Sharing creates a shared calendar called Family. On Google, creating a family "
      "group creates a Family calendar too.\n\n"
      "Do this: tonight, add this week's plans to the Family calendar, then tell everyone to check there before they ask.\n\n"
      f"Send this to your family group chat.\n\n{HBTAGS} #familycalendar #momlife #familylife",
      "Sources: Apple Family Sharing guide ('a shared calendar called Family is automatically created in the Calendar app'); Google "
      "Calendar Help, 'Use a family calendar on Google' ('When you create a family on Google, a calendar called \"Family\" is "
      "automatically created').")

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

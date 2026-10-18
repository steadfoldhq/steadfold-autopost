"""Interactive carousel formats (rendered by formats.py, scheduled like any feed post).
Each entry: a FORMATS spec for the renderer + a post() registration whose slide count matches the rendered images."""
import sys
from pathlib import Path

from specs_teach import post, FF, HB, LH, LF, NG, MADE, DROPPED  # noqa: F401

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pivot"))
from ff_math import fv_monthly  # noqa: E402

FORMATS = {}


def fmt(pid, brand, at, spec, cover_text, save, slide_texts, caption, comment):
    FORMATS[pid] = dict(spec, brand=brand)
    post(pid, brand, at, "learning",
         dict(lay="pills", f=spec["field"], text=cover_text, save=save),
         [dict(k="do" if i == len(slide_texts) - 1 else "say", f=spec["field"], text=t) for i, t in enumerate(slide_texts)],
         caption, comment)


# ------------------------------------------------------------------ Locked Hour · follow the line (today 17:00)
LH_LINES = [
    dict(col="#E0306C", icon="📱", start="My phone keeps / pulling me away",
         fix="Put it in *another room.* Even face-down, it pulls at you."),
    dict(col="#E8B800", icon="🐢", start="I can't get / started",
         fix="Write: *“At 7 pm, at the table, I'll start.”*"),
    dict(col="#3B3B98", icon="🔔", start="I keep getting / interrupted",
         fix="Before you switch, jot *“Next, I'll…”* Coming back is faster."),
]
fmt("lh-1018-follow-the-line", LH, "2026-10-18T17:00",
    dict(kind="follow", field="cream", do_field="pink", pano=4, lines=LH_LINES,
         hook="Can't focus? / Pick your *problem.*", notes=["keep following…", "almost there…"],
         src="Sources: Ward et al. 2017 · Gollwitzer & Sheeran 2006 · Leroy & Glomb 2018",
         do="Tonight, pick *your line* and try its fix tomorrow for one hour.", save="send this to the friend who's “so distracted”"),
    "Can't focus? Pick your problem. Follow its line.", "pick one · follow its line",
    ["Keep following your line.", "Almost there.",
     "Phone: another room. Starting: one when-and-where sentence. Interrupted: a one-line note before you switch.",
     "Tonight, pick your line and try its fix tomorrow for one hour."],
    "Can't focus? It's usually one of three things. Pick yours and follow the line 👉\n\n"
    "📱 Phone keeps pulling you away? Put it in another room. In one study, people did worse on focus tests with the phone on the desk, "
    "even face-down and silent, than with it in another room.\n\n"
    "🟡 Can't get started? Write one sentence: \"At 7 pm, at the kitchen table, I'll start.\" Plans with a when and a where get followed far more often.\n\n"
    "🔵 Keep getting interrupted? Before you switch, jot one line: \"Next, I'll…\". It helps your brain let go, and getting back in is faster.\n\n"
    "Do this: tonight, pick your line and try its fix tomorrow for one hour.\n\nWhich line was yours? Tell us below 👇\n\n"
    "#focus #deepwork #productivity #studytips #habits",
    "Which line was yours: 📱, 🟡 or 🔵? Sources: Ward, Duke, Gneezy & Bos 2017 (\"Brain Drain\"; a later replication was mixed); "
    "Gollwitzer & Sheeran 2006 (94 studies on if-then plans); Leroy & Glomb 2018 (ready-to-resume plans).")

# ------------------------------------------------------------------ Fully Funded · hold the dots (today 17:00)
FF_FRAMES = [(f"Age {a}", round(fv_monthly(300, a - 28), -2), f"you've put in ${300 * 12 * (a - 28):,}") for a in (40, 50, 60)]
FF_12 = round(fv_monthly(300, 32, 0.12), -3)
FF_FRAMES[-1] = (FF_FRAMES[-1][0], FF_FRAMES[-1][1], f"you put in $115,200 · at 12% a year: ${FF_12 / 1e6:.2f}M")
fmt("ff-1018-hold-the-jar", FF, "2026-10-18T17:00",
    dict(kind="hold", field="lite", do_field="cob", frames=FF_FRAMES,
         hook="Watch *$300 a month* / grow, from / *28 to 60*",
         do="This payday, set up *$300 a month* (or what you can) into an index fund. Then leave it alone.",
         save="send this to your “I'll start next year” friend"),
    "Watch $300 a month grow, from 28 to 60", "hold the dots and slide",
    [f"{lab}: ${v:,.0f}. {s}." for lab, v, s in FF_FRAMES]
    + ["This payday, set up $300 a month (or what you can) into an index fund. Then leave it alone."],
    "Hold the dots and slide to watch it grow 👀\n\n"
    f"$300 a month from age 28, growing 10% a year (the S&P 500's long-run average), reaches about ${FF_FRAMES[-1][1]:,.0f} by 60. "
    f"You put in ${300 * 12 * 32:,}. The rest is growth. If markets average 12%, it's about ${FF_12:,.0f}.\n\nWhy it speeds up: your money earns money, then that money earns money too. "
    "That's compounding. Notice how the jar barely moves for years, then jumps.\n\n"
    "Do this: this payday, set up $300 a month, or what you can, into a broad index fund. Then leave it alone.\n\n"
    f"Money Foundations, Part 1 bonus. Save this for payday.\n\n{NG} Education, not advice.\n\n#compounding #investing #indexfunds #personalfinance #moneytips",
    "How old were you when you started investing? Maths: $300 at the end of each month, 10% a year compounded monthly, no fees or taxes.")

# ------------------------------------------------------------------ Littlefold · swipe to reveal (Oct 21 17:00)
LF_VAL = round(fv_monthly(60, 18, 0.08), -2)
fmt("lf-1021-reveal-50-a-month", LF, "2026-10-21T17:00",
    dict(kind="reveal", field="pink", do_field="cream",
         hook="*$50 a month* / from birth to 18. / What does it / *grow into?*",
         guess="guess first!", levels=[64, 30],
         hang=["Compounding is slow at first. / *Keep sliding…*", "The early years look small. / Then it *takes off.* One more →"],
         ans_label="with the 20% grant, at 8% a year", answer=f"${LF_VAL:,.0f}",
         ans_sub=f"You put in *$10,800.* / The rest is grant / and growth.",
         why_label="here's why", why="The government adds *20%* to what you save in an RESP. Then it all grows *for 18 years.*",
         src="Canada Education Savings Grant: 20% on the first $2,500 a year (canada.ca). Growth not guaranteed.",
         do="This week, ask your bank to *open an RESP* and set up *$50 a month.*", save="send this to someone with a new baby"),
    "$50 a month from birth to 18. What does it grow into?", "slide to reveal",
    ["Compounding is slow at first. Keep sliding.", "The early years look small. Then it takes off.",
     f"About ${LF_VAL:,.0f}. You put in $10,800.",
     "This week, ask your bank to open an RESP and set up $50 a month."],
    f"Did you guess right? 👀\n\n$50 a month into an RESP from birth, plus the 20% government grant ($10 a month), growing 8% a year, "
    f"is about ${LF_VAL:,.0f} by 18. You put in $10,800.\n\nWhy: the Canada Education Savings Grant adds 20% on the first $2,500 you save each year. "
    "Free money, then 18 years of growth.\n\nDo this: this week, ask your bank to open an RESP for your baby and set up $50 a month. Have their SIN ready.\n\n"
    f"Send this to someone with a new baby.\n\n{NG} Education, not advice.\n\n#RESP #babymoney #newparents #canadianparents #savingforkids",
    "What was your guess? Source: canada.ca, Canada Education Savings Grant (20% on the first $2,500 a year, up to $500 a year, $7,200 lifetime). "
    "Maths: $60 a month at the end of each month, 8% a year compounded monthly, 18 years.")

# ------------------------------------------------------------------ Hourback · travelling icon (Oct 21 17:45, replaces the plain single)
fmt("hb-1021-travel-subscriptions", HB, "2026-10-21T17:45",
    dict(kind="travel", field="plum", do_field="yel", obj="phone",
         beats=[dict(text="Charges / you *forgot* / you pay", size=118),
                dict(label="sound familiar?", text="*$12.99* here. / *$2.99* there. / You forgot / half of them."),
                dict(label="here's the trick", text="Paste last month's / statement into AI. / Ask: *“What repeats?”*", size=84),
                dict(label="but check this", text="It can miss *yearly* / charges. Scroll back / a year yourself.")],
         do="Tonight, take out *card numbers,* paste last month's statement into AI, ask *“What repeats?”* Cancel one.",
         save="send this to your money buddy"),
    "Charges you forgot you pay", "follow the trail",
    ["$12.99 here. $2.99 there. You forgot half of them.", "Paste last month's statement into AI. Ask: What repeats?",
     "It can miss yearly charges. Scroll back a year yourself.",
     "Tonight, take out card numbers, paste last month's statement into AI, ask What repeats? Cancel one."],
    "Charges you forgot you pay. Everyone has a few 🙈\n\nPaste one month of your bank statement into AI and ask \"What repeats?\" "
    "Spotting the same charge every month is easy for AI, and boring for you.\n\nWhere not to trust it: it can miss yearly charges, "
    "so scroll back through the year yourself. And take card and account numbers out before you paste.\n\n"
    "Do this: tonight, paste last month's statement into AI, ask \"What repeats?\", then cancel one you don't use.\n\n"
    f"Send this to your money buddy.\n\n{MADE}\n\n#subscriptions #aitips #budgeting #moneytips #lifeadmin",
    "How many repeats did you find? Never paste full card or account numbers into an AI chat.")

# the travelling-icon version replaces the plain Oct 21 single
import specs_teach as _S  # noqa: E402
for _old in ("hb-1021-single-subscriptions",):
    _S.POSTS.pop(_old, None)
    _S.META.pop(_old, None)
    DROPPED[_old] = "replaced by hb-1021-travel-subscriptions (travelling-icon carousel)"

# ------------------------------------------------------------------ Littlefold · scenic travelling carousel (Oct 22 11:30)
fmt("lf-1022-newborn-bundle-trail", LF, "2026-10-22T11:30",
    dict(kind="trail", field="cream", do_field="pink", obj="shoe", cta="follow baby's first trip →",
         beats=[dict(text="New baby in Ontario? / *One form.* / *5 things done.*", size=100),
                dict(label="stop 1", sign="📝", text="Register the birth / + order the / *birth certificate*"),
                dict(label="stop 2", sign="🪪", text="Get baby's *SIN* / + start the / *Child Benefit*"),
                dict(label="stop 3", sign="🎓", text="Tick *Education* / *Savings.* It helps / you open an RESP")],
         do="Search *ontario.ca/newborn.* Do it in the *first 30 days.*", save="send this to someone expecting 🍼"),
    "New baby in Ontario? One form. 5 things done.", "follow baby's first trip",
    ["Register the birth and order the birth certificate.", "Get baby's SIN and start the Child Benefit.",
     "Tick Education Savings. It helps you open an RESP.", "Search ontario.ca/newborn. Do it in the first 30 days."],
    "New baby in Ontario? One online form does 5 things 👶\n\n1. Registers the birth\n2. Orders the birth certificate\n"
    "3. Applies for baby's SIN\n4. Applies for the Canada child benefits (including Ontario's)\n5. An Education Savings referral, to help you open an RESP\n\n"
    "Why it matters: the Child Benefit and the RESP grants need your baby's SIN. One form starts all of it.\n\n"
    "Do this: search ontario.ca/newborn and do it in the first 30 days. Still free online up to 12 months.\n\n"
    "Send this to someone expecting.\n\n#newparents #ontarioparents #canadianparents #newbaby #babymoney",
    "Did you do the bundle? Source: ontario.ca, Register a birth (new baby): the 5-in-1 newborn bundle; register within 30 days, "
    "free online within 12 months. Other provinces have their own service.")

# ------------------------------------------------------------------ Fully Funded · scenic travelling carousel (Oct 24 12:00)
fmt("ff-1024-paycheque-trail", FF, "2026-10-24T12:00",
    dict(kind="trail", field="lite", do_field="cob", obj="piggy", cta="follow your paycheque →",
         palette=dict(sky1="#F7F1E6", sky2="#CFD8F8", sun="#FFC6B2", h1="#E4E9FB", h2="#C9D3F7", h3="#A9B8F3", path="#E04E28"),
         beats=[dict(text="Payday. / Where should / *the money go first?*", size=100),
                dict(label="stop 1", sign="🛟", text="*One month* of bills / in savings. / Your safety net."),
                dict(label="stop 2", sign="🎁", text="Work matches your / savings? Take the / *full match.* Free money."),
                dict(label="stop 3", sign="📈", text="Then invest in / your *TFSA,* in a / *low-fee index fund.*")],
         do="This payday, set up *one automatic transfer* to stop 1. Add stop 2 and 3 as you go.",
         save="send this to your first-job friend"),
    "Payday. Where should the money go first?", "follow your paycheque",
    ["One month of bills in savings. Your safety net.", "Work matches your savings? Take the full match.",
     "Then invest in your TFSA, in a low-fee index fund.", "This payday, set up one automatic transfer to stop 1."],
    "Payday. Where should the money go first? 🇨🇦 A simple order a lot of planners use:\n\n"
    "1. A safety net: one month of bills in savings, then build toward 3 to 6 months.\n"
    "2. If your employer matches retirement savings, put in enough to get the full match. It's free money.\n"
    "3. Then invest in your TFSA, in a low-fee index fund, and leave it alone.\n\n"
    "Why this order: the safety net stops a surprise bill from landing on a credit card. The match is an instant return. Then time does the rest.\n\n"
    f"Do this: this payday, set up one automatic transfer to stop 1. Add the others as you go.\n\n{NG} Education, not advice.\n\n"
    "#personalfinancecanada #payday #tfsa #emergencyfund #moneytips",
    "Which stop are you at? Your situation may differ (high-interest debt usually comes before investing). 2026 TFSA limit: $7,000 (CRA).")

# ================================================================== Oct 24-25 interactives (built Oct 18 pm; FF's is ff-1024-paycheque-trail)
# ------------------------------------------------------------------ Locked Hour · swipe to reveal (Oct 24 12:30)
fmt("lh-1024-reveal-47-seconds", LH, "2026-10-24T12:30",
    dict(kind="reveal", field="cream", do_field="cream",
         hook="In 2004, people / stayed on one screen / *2.5 minutes.* / Now?",
         guess="guess first!", levels=[64, 30],
         hang=["It dropped in / *every* study. *Keep sliding…*", "Shorter than / *one song.* One more →"],
         ans_label="on one screen, before switching", answer="47 sec",
         ans_sub="Gloria Mark's studies, / *2016 to 2020.*",
         why_label="here's why", why="Every switch leaves part of your mind behind.",
         src="Gloria Mark, Attention Span (2023) · UC Newsroom 2024",
         do="For your next task, go *full screen.* One window. Nothing else.", save="send this to your 40-tabs friend"),
    "In 2004, people stayed on one screen 2.5 minutes. Now?", "slide to reveal",
    ["It dropped in every study. Keep sliding.", "Shorter than one song. One more.",
     "47 seconds on one screen, on average (2016 to 2020).", "For your next task, go full screen. One window. Nothing else."],
    "Did you guess lower or higher? 👀\n\n"
    "Researcher Gloria Mark has timed how long people stay on one screen before switching. In 2004: about two and a half minutes. "
    "In her studies from 2016 to 2020: 47 seconds, on average.\n\n"
    "Why it matters: every switch costs a little focus, and 47-second hops add up to a day that felt busy but didn't get far.\n\n"
    "Do this: for your next task, go full screen. One window, nothing else, until it's done.\n\n"
    "Send this to your 40-tabs friend.\n\n#focus #attentionspan #deepwork #productivity #studytips",
    "What was your guess? Source: Gloria Mark (UC Irvine), Attention Span (2023); UC Newsroom (2024), 'How to sharpen your "
    "attention': about two and a half minutes on one screen in her 2004 study (2003 data), 47 seconds on average in studies from 2016 to 2020.")

# ------------------------------------------------------------------ Hourback · follow the line (Oct 24 17:45)
HB_LINES = [
    dict(col="#E0306C", icon="⏰", start="I'm always / running late",
         fix="Turn on *Time to Leave.* Calendar tells you when to go, based on travel time."),
    dict(col="#E8B800", icon="🔢", start="My texts are / full of codes",
         fix="Turn on *Delete After Use.* Codes clear themselves once used."),
    dict(col="#3B3B98", icon="📸", start="I screenshot / all day",
         fix="Turn on *Back Tap.* Double-tap the back of your phone."),
]
fmt("hb-1024-follow-settings", HB, "2026-10-24T17:45",
    dict(kind="follow", field="plum", do_field="orng", pano=3, lines=HB_LINES,
         hook="3 iPhone settings. / Pick *your problem.*", notes=["keep following…"],
         src="Settings → Apps → Calendar → Default Alert Times · Settings → General → AutoFill & Passwords · Settings → Accessibility → Touch → Back Tap",
         do="Tonight, follow *your line* and turn on that one setting. It takes 2 minutes.",
         save="send this to the friend who's always late"),
    "3 iPhone settings. Pick your problem.", "pick one · follow its line",
    ["Keep following your line.",
     "Late: Time to Leave. Codes: Delete After Use. Screenshots: Back Tap.",
     "Tonight, follow your line and turn on that one setting. It takes 2 minutes."],
    "3 iPhone settings. Pick your problem and follow its line 👉\n\n"
    "⏰ Always running late? Settings → Apps → Calendar → Default Alert Times → turn on Time to Leave. Events with an address now "
    "alert you when it's time to go, based on travel time (Location Services on for Calendar).\n\n"
    "🔢 Texts full of verification codes? Settings → General → AutoFill & Passwords → turn on Delete After Use. Codes clear themselves "
    "once they've been filled in.\n\n"
    "📸 Screenshot all day? Settings → Accessibility → Touch → Back Tap → Double Tap → Screenshot. Then double-tap the back of your phone "
    "(iPhone 8 or later).\n\n"
    "Do this: tonight, turn on the one setting for your line. It takes 2 minutes.\n\nWhich line was yours? Tell us below 👇\n\n"
    "Send this to the friend who's always late.\n\n#iphonetips #iphonesettings #timesaver #lifehacks #hourback",
    "Which line was yours? Sources: Apple Support, 'Use Back Tap on your iPhone' (Settings → Accessibility → Touch → Back Tap; iPhone 8 "
    "or later); iPhone Life, Time to Leave (Settings → Apps → Calendar → Default Alert Times) and auto-delete verification codes "
    "(Settings → General → AutoFill & Passwords → Delete After Use). Paths checked for iOS 18; menus can move between iOS versions.")

# ------------------------------------------------------------------ Littlefold · follow the line (Oct 25 11:30)
LF_LINES = [
    dict(col="#E86A92", icon="🍼", start="Last feed / a while ago?",
         fix="Offer a *feed.* Hunger is often the reason."),
    dict(col="#E8A93A", icon="🧷", start="Fed, but still / fussing?",
         fix="Check the *diaper,* and whether they're *too hot or cold.*"),
    dict(col="#6E8FC4", icon="🤗", start="Fed, dry, / still crying?",
         fix="Hold them close and *sway,* or go for a *stroller walk.*"),
]
fmt("lf-1025-follow-crying", LF, "2026-10-25T11:30",
    dict(kind="follow", field="cream", do_field="pink", pano=3, lines=LF_LINES,
         hook="Baby won't stop / crying? Follow / *your line.*", notes=["keep following…"],
         src="Source: NHS, Soothing a crying baby · if baby seems unwell or the cry sounds different, call your doctor or 811",
         do="Save your health line now: *811* in most provinces. Then you're ready at 3 am.",
         save="send this to someone with a newborn"),
    "Baby won't stop crying? Follow your line.", "pick one · follow its line",
    ["Keep following your line.",
     "Hungry: offer a feed. Fussing: check the diaper and temperature. Still crying: hold, sway, or a stroller walk.",
     "Save your health line now: 811 in most provinces."],
    "Baby won't stop crying? Pick the line that fits and follow it 👉\n\n"
    "🍼 Last feed a while ago? Offer a feed. Hunger is often the reason.\n"
    "🧷 Fed, but still fussing? Check the diaper, and whether they're too hot or too cold.\n"
    "🤗 Fed, dry, still crying? Hold them close and sway, sing, or go for a walk with the stroller.\n\n"
    "If baby seems unwell (fever, not feeding) or the cry doesn't sound like their usual cry, call your doctor or your health line. "
    "And if it's all too much, put baby down safely on their back in the crib and step away for a few minutes. That's OK.\n\n"
    "Do this: save your health line in your phone now: 811 in most provinces (Manitoba: Health Links, 1-888-315-9257).\n\n"
    "Send this to someone with a newborn.\n\nGeneral information only, not medical advice.\n\n"
    "#newborn #babycrying #newparents #canadianparents #fourthtrimester",
    "Which line is your baby? Sources: NHS, 'Soothing a crying baby' (reasons babies cry: hunger, a wet or dirty nappy, tiredness, "
    "wanting a cuddle, wind, too hot or cold; soothing: hold close and sway, rock in a pram or go for a walk; call a doctor if baby "
    "seems unwell). Heart & Stroke, 'Medical services by phone': 811 in BC, AB, SK, ON, QC, NB, NS, PEI, NL and Yukon.")

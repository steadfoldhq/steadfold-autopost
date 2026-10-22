"""Interactive carousel formats (rendered by formats.py, scheduled like any feed post).
Each entry: a FORMATS spec for the renderer + a post() registration whose slide count matches the rendered images."""
import math
import sys
from pathlib import Path

from specs_teach import post, FF, HB, LH, LF, NG, MADE, NOT_MED, DROPPED  # noqa: F401

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
FF_FRAMES = [(f"Age {a}", round(fv_monthly(300, a - 28), -2), f"you've put in ${300 * 12 * (a - 28):,}") for a in range(32, 61, 4)]
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

# (lf-1021-reveal-50-a-month was here: retired Oct 19 by the Formats lead. Its "$50 a month to 18" maths now runs as the
#  page's Oct 19 Reel lf-reel-1019-resp-50-month, and Littlefold's afternoon slot goes to bonding: lf-1021-streak-serve-return.)
DROPPED["lf-1021-reveal-50-a-month"] = "duplicate of lf-reel-1019-resp-50-month; slot now lf-1021-streak-serve-return (Formats lead)"

# ------------------------------------------------------------------ Hourback · travelling icon (Oct 21 17:45, replaces the plain single)
fmt("hb-1021-travel-subscriptions", HB, "2026-10-21T17:45",
    dict(kind="travel", field="plum", do_field="yel", obj="phone",
         beats=[dict(text="Charges / you *forgot* / you pay", size=118),
                dict(label="sound familiar?", text="*$12.99* here. / *$2.99* there. / You forgot / half of them."),
                dict(label="here's the trick", text="Paste last month's / statement into AI. / Ask: *“What repeats?”*", size=84),
                dict(label="why it works", text="Spotting the *same* / *charge* every month / is easy for AI."),
                dict(label="but check this", text="It can miss *yearly* / charges. Scroll back / a year yourself.")],
         do="Tonight, take out *card numbers,* paste last month's statement into AI, ask *“What repeats?”* Cancel one.",
         save="send this to your money buddy"),
    "Charges you forgot you pay", "follow the trail",
    ["$12.99 here. $2.99 there. You forgot half of them.", "Paste last month's statement into AI. Ask: What repeats?",
     "Spotting the same charge every month is easy for AI.", "It can miss yearly charges. Scroll back a year yourself.",
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

# (hb-1024-follow-settings, three iPhone settings, was here: retired Oct 19 by the Formats lead. Hourback's afternoon slot now
#  teaches AI for real (owner, Oct 18 21:46: no settings/checklist gimmicks): hb-1024-climb-5-levels.)
DROPPED["hb-1024-follow-settings"] = "settings tips retired (Hourback = really teach AI); slot now hb-1024-climb-5-levels (Formats lead)"

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


# ==================================================================================================================
# FORMATS LEAD · Oct 19 00:xx rebuild: every page's afternoon slot is an interactive carousel (DEPTH + BEST BOOKS standard).
# Replacing a page-file post: the lead applies the DROPPED/_POSTS.pop change listed in formats-progress.md.
# ==================================================================================================================
# page-file posts that an interactive carousel here replaces (old id -> new id). specs_teach.py drops them after all
# page files are imported (one 3-line loop the lead adds once; see formats-progress.md).
REPLACES = {
    "lf-1019-single-fever-under-3m": "lf-1019-follow-fever",
    "hb-1019-buzz-batch": "hb-1019-trail-how-ai-answers",
}


def texts(spec, kind):
    """slide_texts for post() straight from the spec, so the registration always matches the rendered slide count."""
    if kind == "follow":
        mids = [f'{m.get("label", "")}: {m["text"]}'.replace(" / ", " ").replace("*", "") for m in spec["mids"]]
        fixes = " ".join(f'{ln["start"]}: {ln["fix"]}'.replace(" / ", " ").replace("*", "") for ln in spec["lines"])
        return mids + [fixes, spec["do"].replace("*", "")]
    if kind == "streak":
        return [(f'{fr["label"]}: ' if fr.get("label") else "") + (fr["text"] + (" " + fr["note"] if fr.get("note") else ""))
                .replace(" / ", " ").replace("*", "") for fr in spec["frames"]] + [spec["do"].replace("*", "")]
    if kind == "split":
        return [f'Fix {k}: {rw["after"]} ({rw["why"]})'.replace(" / ", " ").replace("*", "") for k, rw in enumerate(spec["rows"], 1)] \
            + [spec["do"].replace("*", "")]
    if kind in ("trail", "travel", "climb", "roadmap"):
        return [(f'{bt.get("label", "")}: ' if bt.get("label") else "") + (bt["text"] + (" " + bt["note"] if bt.get("note") else ""))
                .replace(" / ", " ").replace("*", "") for bt in spec["beats"][1:]] + [spec["do"].replace("*", "")]
    if kind == "hold":
        return [f'{fr[0]}: {spec["show"][k] if spec.get("show") else format(fr[1], ",." + str(spec.get("dec", 0)) + "f").join([spec.get("pre", "$"), spec.get("post", "")])}. {fr[2].rstrip(".")}.' + (" " + fr[3].replace(" / ", " ").replace("*", "") if len(fr) > 3 else "")
                for k, fr in enumerate(spec["frames"])] + [spec["do"].replace("*", "")]
    raise KeyError(kind)


def ifmt(pid, brand, at, spec, cover_text, save, caption, comment):
    fmt(pid, brand, at, spec, cover_text, save, texts(spec, spec["kind"]), caption, comment)


# ------------------------------------------------------------------ Littlefold · follow the line · Oct 19 17:00 (replaces lf-1019-single-fever-under-3m)
LF19_LINES = [
    dict(col="#E0306C", icon="👶", start="Under / 3 months",
         fix="*Be seen urgently.* Call your doctor now. Can't reach anyone? *Go to emergency.*"),
    dict(col="#E8A93A", icon="🍼", start="3 to 6 / months",
         fix="Any fever: *see a doctor.* Call them today, even if baby seems OK."),
    dict(col="#6E8FC4", icon="🧸", start="Over / 6 months",
         fix="Drinking and playing? Often fine at home. *See a doctor if it lasts 48–72 hours.*"),
]
ifmt("lf-1019-follow-fever", LF, "2026-10-19T17:00",
     dict(kind="follow", field="cream", do_field="pink", pano=5, lines=LF19_LINES,
          hook="Baby has / a fever? / Find *their age.*",
          mids=[dict(label="first, check it right", text="Under 2? A *rectal* / reading is the / most accurate. / Armpit is a / first check."),
                dict(label="what counts as a fever", text="Rectal: *over 37.9°C.* / Armpit: *over 37.5°C.* / Feels hot, seems unwell, / but the armpit says no? / *Check rectally.*"),
                dict(label="at any age, call if…", text="Very *sleepy,* hard / to wake, very *cranky,* / a *rash,* or a cough / that won't stop. / *Trust that feeling.*")],
          src="Sources: Canadian Paediatric Society (caringforkids.cps.ca) · American Academy of Pediatrics · General information, not medical advice",
          do="Right now, save your doctor's *after-hours number* and your *health line (811)* in your phone.",
          do_why="At 3 am, nobody wants to search. *Decide now,* calmly.",
          save="send this to your babysitter and the grandparents"),
     "Baby has a fever? Find their age.", "find their age · follow the line",
     "Baby has a fever? Find their age and follow the line 👉 The rule changes as they grow.\n\n"
     "👶 Under 3 months: be seen urgently. Call your doctor right away. If you can't reach anyone, go to emergency.\n"
     "🍼 3 to 6 months: any fever means a doctor visit. Call today.\n"
     "🧸 Over 6 months: if they're drinking and playing between fevers, it's often fine to care for them at home. "
     "See a doctor if it lasts more than 48 to 72 hours.\n\n"
     "Why age matters so much: a young baby's immune system is still new, and signs of a serious infection can be subtle. "
     "That's why the youngest babies get checked even when they seem OK.\n\n"
     "How to check it right: under 2, a rectal reading is the most accurate; armpit is a first check. "
     "A fever is over 37.9°C rectal, or over 37.5°C armpit.\n\n"
     "At any age, call your doctor if your child is very sleepy or hard to wake, very cranky, has a rash, a cough or wheeze that "
     "won't stop, or anything that worries you. You know your baby.\n\n"
     "Never give aspirin to children. Ask your doctor before giving ibuprofen to a baby under 6 months.\n\n"
     "Do this: right now, save your doctor's after-hours number and your health line (811 in most provinces) in your phone.\n\n"
     f"Send this to your babysitter and the grandparents.\n\n{NOT_MED}\n\n#newborn #babyfever #newparents #canadianparents #babyhealth",
     "Which age is your little one? Sources: Canadian Paediatric Society, caringforkids.cps.ca, 'Fever and temperature taking' "
     "(under 3 months: seen urgently; under 6 months with fever: see a doctor; older: see a doctor if fever lasts more than 48-72 hours; "
     "rectal most accurate from birth to 2; fever = rectal above 37.9°C, armpit above 37.5°C; no aspirin; ask a doctor before ibuprofen "
     "under 6 months). American Academy of Pediatrics, healthychildren.org (under 3 months, 38.0°C / 100.4°F or higher: call right away). "
     "811: Heart & Stroke, 'Medical services by phone' (most provinces and Yukon).")

# ------------------------------------------------------------------ Fully Funded · hold the dots · Oct 19 17:00 (new slot)
FF19 = [("Age 25", 1000, "day one: you put in $1,000", "Then you *never add* / another dollar."),
        ("Age 32", round(1000 * 1.1 ** 7), "about doubled. You did nothing.", "72 ÷ 10% a year = *7.2 years* / to double. The Rule of 72."),
        ("Age 39", round(1000 * 1.1 ** 14), "about doubled again", "Now the *growth* is / earning growth of its own."),
        ("Age 46", round(1000 * 1.1 ** 21), "a 3rd double", "Each double is *bigger* / than all the ones before."),
        ("Age 53", round(1000 * 1.1 ** 28), "a 4th double", "Same $1,000. Same 7 years. / A *$7,000* jump."),
        ("Age 60", round(1000 * 1.1 ** 35), "28 times what you put in", "The same $1,000 in a / 2% savings account: *$2,000.*")]
ifmt("ff-1019-hold-double", FF, "2026-10-19T17:00",
     dict(kind="hold", field="lite", do_field="cob", frames=FF19, cover_obj="piggy",
          hook="Leave *$1,000* / alone at 25. / Watch it *double,* / *and double…*",
          do="Next windfall (tax refund, bonus, birthday cash): put *$1,000* in a *broad index fund* in your TFSA. Then *leave it alone.*",
          do_size=70, do_why="Doubling needs two things: *growth* and *time.* You control the time.",
          save="send this to someone turning 25"),
     "Leave $1,000 alone at 25. Watch it double, and double…", "hold the dots and slide",
     "Hold the dots and slide. Watch one $1,000 double, and double, and double 👀\n\n"
     f"$1,000 invested at 25, growing 10% a year, is about ${round(1000 * 1.1 ** 35):,} by 60. You never add another dollar. "
     "The same $1,000 in a 2% savings account: about $2,000.\n\n"
     "The rule that stays with you forever: the Rule of 72. Divide 72 by your yearly growth rate, and you get the years it takes "
     "to double. At 10%, about 7 years. At 2%, 36 years.\n\n"
     "Why the jumps get bigger: each double adds as much as everything before it put together. That's compounding, and it's why "
     "the last 10 years do more than the first 25. Morgan Housel puts it simply in The Psychology of Money: the real secret is time.\n\n"
     "Do this: next windfall (tax refund, bonus, birthday cash), put $1,000 in a broad index fund in your TFSA. Then leave it alone.\n\n"
     f"Send this to someone turning 25.\n\n{NG} Education, not advice.\n\n#compounding #ruleof72 #investing #tfsa #personalfinancecanada",
     "How old were you when you invested your first $1,000? Maths: $1,000 once, 10% a year compounded yearly (about the S&P 500's "
     "long-run average; Damodaran, NYU Stern, historical returns 1928 onward), no fees or taxes: age 32 $1,949, 39 $3,797, 46 $7,400, "
     f"53 $14,421, 60 ${round(1000 * 1.1 ** 35):,}. At 2%: $1,999. The Rule of 72 is an approximation. 2026 TFSA limit: $7,000 (CRA). "
     "Ideas from The Psychology of Money (Housel) and The Richest Man in Babylon (Clason).")

# ------------------------------------------------------------------ Locked Hour · scenic trail · Oct 19 17:00 (new slot)
LH_PAL = dict(sky1="#FFF6E5", sky2="#FFD5E5", sun="#FFE27A", h1="#FFEFC2", h2="#FFC9DC", h3="#FFB0CB", path="#E0306C")
ifmt("lh-1019-trail-66-days", LH, "2026-10-19T17:00",
     dict(kind="trail", field="cream", do_field="pink", obj="clock", palette=LH_PAL, cta="follow the 66-day trail →",
          beats=[dict(text="From *2 minutes* / to a *locked hour.* / The 66-day trail.", size=104),
                 dict(label="day 1 · 2 minutes", sign="🌱", text="Sit down. Open it. / Do *2 minutes.* / Then stop.", size=88,
                      note="You're not training the work yet. / You're training *showing up.*"),
                 dict(label="week 2 · 10 minutes", sign="🪑", text="Same *time.* / Same *chair.*", size=96,
                      note="Add a few minutes each week. / The place becomes the cue: / sit down, and your brain knows."),
                 dict(label="week 4 · 20 minutes", sign="📅", text="Missed a day? / *Never miss twice.*", size=92,
                      note="One missed day barely dented / habits in the 66-day study. / Two in a row starts a new habit."),
                 dict(label="week 6 · 35 minutes", sign="📵", text="Phone in / *another room.*", size=96,
                      note="And end each session by writing / *tomorrow's first step.* / Starting gets easy."),
                 dict(label="week 8 · 50 minutes", sign="🔥", text="It stops / feeling like / *willpower.*", size=92,
                      note="Same place, same time, again and again: / that's how effort / turns into *autopilot.*"),
                 dict(label="day 66 · 60 minutes", sign="🔒", text="*One locked hour.* / On autopilot.", size=92,
                      note="In the study, habits took *66 days* / on average to feel automatic. / (Anywhere from 18 to 254.)")],
          do="Tonight, pick *one thing* and *one time.* Tomorrow, do just *2 minutes* of it. Stop on purpose.",
          do_why="Small enough that you never skip it. *That's the trick.*",
          save="send this to the friend who “starts Monday”"),
     "From 2 minutes to a locked hour. The 66-day trail.", "follow the trail",
     "From 2 minutes to a locked hour. Follow the trail 👉\n\n"
     "Most people start a new habit at full size: an hour of study, a 5 km run. Then life happens, they skip, and they quit.\n\n"
     "The trail goes the other way:\n"
     "🌱 Day 1: just 2 minutes. Sit down, open it, stop. You're training showing up, not the work.\n"
     "🪑 Week 2: 10 minutes, same time, same chair. Add a few minutes each week. The place becomes the cue.\n"
     "📅 Week 4: 20 minutes. Missed a day? Never miss twice. One slip barely dented habits in the study below.\n"
     "📵 Week 6: 35 minutes. Phone in another room, and end by writing tomorrow's first step.\n"
     "🔥 Week 8: 50 minutes. It stops feeling like willpower.\n"
     "🔒 Day 66: one locked hour, on autopilot.\n\n"
     "Why it works: habits form by repeating the same thing in the same context until the context triggers it for you. "
     "In a well-known study, that took 66 days on average, anywhere from 18 to 254. So don't panic on day 20.\n\n"
     "Do this: tonight, pick one thing and one time. Tomorrow, do just 2 minutes of it. Stop on purpose.\n\n"
     "Send this to the friend who \"starts Monday\".\n\n#habits #atomichabits #focus #deepwork #selfimprovement",
     "Where are you on the trail? Sources: Lally et al. 2010, European Journal of Social Psychology, 'How are habits formed' (median 66 days "
     "to reach automaticity, range 18-254; missing one opportunity did not materially affect the process). Wood & Rünger 2016, Annual "
     "Review of Psychology (habits are cued by context). Ward et al. 2017 (phone presence and focus; a later replication was mixed). "
     "Ideas from Atomic Habits (Clear: the two-minute rule, never miss twice) and Tiny Habits (Fogg). Minute steps are our suggested pace.")

# ------------------------------------------------------------------ Hourback · scenic trail · Oct 19 17:45 (replaces hb-1019-buzz-batch)
HB_PAL = dict(sky1="#FFF5EA", sky2="#DCDDFA", sun="#FFD4BD", h1="#E9E9FB", h2="#C9CAF5", h3="#ACAEEB", path="#D4532A")
ifmt("hb-1019-trail-how-ai-answers", HB, "2026-10-19T17:45",
     dict(kind="trail", field="plum", do_field="yel", obj="phone", palette=HB_PAL, cta="follow your question →",
          beats=[dict(text="What really happens / when you *ask AI* / a question?", size=100,
                      note="Follow it. By the last stop, / you'll *use AI better* than most."),
                 dict(label="stop 1 · tokens", sign="✂️", text="Your words get / cut into *tokens.*", size=96,
                      note="Small chunks of words, about / *4 letters* each in English. / 100 tokens ≈ 75 words."),
                 dict(label="stop 2 · patterns", sign="📚", text="It learned from / *huge amounts* / of text.", size=96,
                      note="It's not looking facts up in a database / (unless it searches the web). / It learned *how words follow words.*"),
                 dict(label="stop 3 · one piece at a time", sign="🎯", text="It *predicts* the / next token. / Again. And again.", size=92,
                      note="Every reply is built one small piece / at a time, each one a likely / *next piece* after the last."),
                 dict(label="stop 4 · the catch", sign="🎲", text="Doesn't know? / It may *guess anyway,* / and sound sure.", size=90,
                      note="OpenAI's own research (2025): / training has *rewarded guessing* / over saying “I don't know.”"),
                 dict(label="stop 5 · your move", sign="🗺️", text="Give it *context.* / Ask for *sources.*", size=96,
                      note="Who you are, what you need, an example. / Then check anything that matters, / like dates, numbers and names.")],
          do="Next time, start with: *“I'm a [role]. I need [task] for [who]. Ask me 3 questions first.”*",
          do_size=72, do_why="Better context, better predictions. It only knows *what you tell it.*",
          save="send this to the friend who thinks AI is magic"),
     "What really happens when you ask AI a question?", "follow your question",
     "What really happens when you ask AI a question? Follow it 👉\n\n"
     "✂️ Your words are cut into tokens: chunks of words, about 4 characters each in English (100 tokens is roughly 75 words).\n"
     "📚 The model learned from huge amounts of text. It isn't looking facts up in a database (unless it's searching the web); "
     "it learned patterns of how words follow words.\n"
     "🎯 It writes the reply one token at a time, each one a likely next piece after the last.\n"
     "🎲 The catch: when it doesn't know, it may guess, and sound just as sure. OpenAI's own 2025 research says training and testing "
     "have rewarded guessing over admitting uncertainty, like a student guessing on a multiple-choice test.\n"
     "🗺️ Your move: give it context, and ask for sources. Then check anything that matters.\n\n"
     "Why the context trick works: the model predicts from what's in front of it. Tell it who you are, what you need and for whom, "
     "and the likely next words become your words. Ethan Mollick's Co-Intelligence makes the same point: treat it like a very fast "
     "new colleague who needs a proper brief.\n\n"
     "Do this: next time, start with \"I'm a [role]. I need [task] for [who]. Ask me 3 questions first.\"\n\n"
     f"Send this to the friend who thinks AI is magic.\n\n#ai #chatgpt #howaiworks #aitips #hourback",
     "What surprised you most? Sources: OpenAI, 'Why language models hallucinate' (Sept 5, 2025: standard training and evaluation "
     "reward guessing over acknowledging uncertainty). OpenAI Help Center, 'What are tokens and how to count them?' (about 4 characters "
     "of English text per token; 100 tokens ≈ 75 words). Ethan Mollick, Co-Intelligence (2024).")


# ================================================================== Oct 20 · NEW KINDS (split, climb, streak, roadmap)
REPLACES.update({"lf-1020-single-coat-check": "lf-1020-split-car-seat", "hb-1020-speedy-meetings": "hb-1020-roadmap-agent"})

# ------------------------------------------------------------------ Littlefold · swipe to fix · Oct 20 17:00 (replaces lf-1020-single-coat-check)
ifmt("lf-1020-split-car-seat", LF, "2026-10-20T17:00",
     dict(kind="split", field="cream", do_field="pink",
          hook="Winter car seat, / *fixed in 5 swipes*", hook_size=84,
          rows=[dict(before="Puffy coat or snowsuit / under the straps",
                     after="Coat *off.* Thin layers: / leggings, long sleeves, a thin fleece.",
                     why="Puffy padding squashes flat in a crash. Straps go loose."),
                dict(before="Straps feel / “snug enough”",
                     after="*Pinch test:* can you pinch / the strap at the shoulder? Tighten.",
                     why="Snug on the chest. No slack you can pinch."),
                dict(before="Baby shivering / in the back seat",
                     after="Buckle first, *then* a blanket / or the coat on backwards *over* the straps.",
                     why="Warm on top. Nothing between baby and harness."),
                dict(before="Car seat left / in the cold car",
                     after="Keep the infant carrier / *inside* until you leave.",
                     why="A warm seat pulls less heat from baby."),
                dict(before="A cozy insert / from the stroller",
                     after="Nothing *under* baby or *behind* / the straps that didn't come with the seat.",
                     why="Add-ons weren't crash-tested with your seat.")],
          do="Tomorrow morning: coat *off,* buckle, *pinch test,* then the coat on backwards *over the straps.*",
          do_why="Two extra minutes at the door. *Every drive,* all winter.",
          save="send this to whoever does daycare drop-off"),
     "Winter car seat, fixed in 5 swipes", "swipe to fix it",
     "Winter car seat, fixed in 5 swipes 👉 Each swipe fixes one thing.\n\n"
     "1. Coat off. Dress baby in thin layers instead: leggings or tights, a long-sleeve top, a thin fleece. In a crash, puffy padding "
     "squashes flat and the straps end up too loose to hold them.\n"
     "2. Pinch test. Buckle up, then try to pinch the strap at the shoulder. If you can pinch it, tighten until it's snug on the chest.\n"
     "3. Warmth goes on top. Buckle first, then tuck a blanket over the straps, or put their coat on backwards over the harness. "
     "Take it off as the car warms up.\n"
     "4. Keep the infant carrier inside until you leave. A room-temperature seat pulls less heat from your baby.\n"
     "5. Nothing under baby or behind the straps that didn't come with the seat. Inserts and covers sold separately weren't "
     "crash-tested with it.\n\n"
     "Why it matters: a harness only works when it's snug against your child's body. Anything thick in between creates slack you can't see.\n\n"
     "Do this: tomorrow morning, coat off, buckle, pinch test, then the coat on backwards over the straps.\n\n"
     f"Send this to whoever does daycare drop-off.\n\n{NOT_MED}\n\n#carseatsafety #winterwithkids #newparents #canadianparents #babysafety",
     "Which fix was new to you? Source: American Academy of Pediatrics, healthychildren.org, 'Winter Car Seat Safety Tips' (no bulky "
     "coats or snowsuits under the harness, padding flattens in a crash; pinch test; thin layers; blanket or coat on backwards over the "
     "buckled harness; keep the infant carrier inside; nothing bulky under the child or between the child and the straps; products not "
     "sold with the seat haven't been crash tested). Always follow your car seat's manual.")


# ------------------------------------------------------------------ Fully Funded · staircase climb · Oct 20 17:00 (new slot)
def _months_to(target, pmt=500, rate=0.10):
    r = rate / 12
    return math.ceil(math.log(target * r / pmt + 1) / math.log(1 + r))


_FF20 = [(t, _months_to(t)) for t in (100_000, 200_000, 300_000, 400_000, 500_000)]


def _ym(m):
    y, mo = divmod(m, 12)
    return f"{y} years" + (f", {mo} months" if mo else "")


_ff20_beats = [dict(text="Your first / *$100,000* is the / *hardest* climb.", size=104,
                    note="$500 a month, growing 10% a year. / Watch each step get *shorter.*")]
_prev = 0
for _k, (_t, _m) in enumerate(_FF20):
    _put = 500 * _m
    _gain = round(fv_monthly(500, _m / 12) - _put, -2)
    _ff20_beats.append(dict(
        label=f"step {_k + 1} · ${_t // 1000}k", step=f"+{_ym(_m - _prev)}", sign=["🧗", "🪜", "⚡", "🚀", "🏔️"][_k],
        text=[f"*${_t:,}.* / {_ym(_m)} in.", f"*${_t:,}.* / Only {_ym(_m - _prev)} more.", f"*${_t:,}.* / {_ym(_m - _prev)} more.",
              f"*${_t:,}.* / {_ym(_m - _prev)} more.", f"*${_t:,}.* / {_ym(_m - _prev)}. The summit."][_k], size=86,
        note=[f"You put in ${_put:,}. Growth: about ${_gain:,.0f}. / The slowest step by far. / *Keep climbing.* This is the hard part.",
              f"Same $500 a month. Half the time. / Growth has now *out-earned you:* about ${_gain:,.0f}.",
              f"You put in ${_put:,}. / Growth: about *${_gain:,.0f}.* It's pulling you now.",
              f"At 10%, $300,000 grows about / *$30,000 a year.* 5 times what you add.",
              f"You put in ${_put:,}. / Growth did the rest: about *${_gain:,.0f}.*"][_k]))
    _prev = _m
ifmt("ff-1020-climb-first-100k", FF, "2026-10-20T17:00",
     dict(kind="climb", field="lite", do_field="cob", obj="piggy", beats=_ff20_beats, cta="climb it, one swipe at a time →",
          do="This payday, set up an *automatic $500 a month* (or what you can) into a *broad index fund* in your TFSA.",
          do_size=72, do_why="The first step is the slow one. *Don't judge the climb by it.*",
          save="send this to the friend stuck at step 1"),
     "Your first $100,000 is the hardest climb.", "climb it, one swipe at a time",
     "Your first $100,000 is the hardest. Then every step gets shorter 👉\n\n"
     f"$500 a month, growing 10% a year:\n"
     + "".join(f"• ${_t:,}: {_ym(_m)} in ({'+' + _ym(_m - _p) if _p else 'the long one'})\n"
               for (_t, _m), _p in zip(_FF20, [0] + [m for _, m in _FF20[:-1]]))
     + "\nWhy it speeds up: at first, almost all of the growth comes from you. Later, your money grows by more each year than you "
       "put in. That's the moment the climb flips. Charlie Munger famously called the first $100,000 the hardest part; Morgan Housel's "
       "Psychology of Money explains why: compounding is slow, slow, slow, then fast.\n\n"
       "Do this: this payday, set up an automatic $500 a month (or what you can) into a broad index fund in your TFSA. Then keep climbing.\n\n"
       f"Send this to the friend stuck at step 1.\n\n{NG} Education, not advice.\n\n#investing #compounding #first100k #tfsa #personalfinancecanada",
     "Which step are you on? Maths: $500 at the end of each month, 10% a year compounded monthly (about the S&P 500's long-run average), "
     "no fees or taxes, months rounded up. A TFSA holds $7,000 of new room in 2026 (CRA), so $6,000 a year fits. Ideas from The "
     "Psychology of Money (Housel) and The Wealthy Barber (Chilton).")

# ------------------------------------------------------------------ Locked Hour · streak calendar · Oct 20 17:00 (new slot)
ifmt("lh-1020-streak-30-ticks", LH, "2026-10-20T17:00",
     dict(kind="streak", field="cream", do_field="pink", days=30, marks={7: "⭐", 30: "🏆"},
          hook="*30 ticks.* / Watch a habit / *fill in.*", hook_size=110,
          frames=[dict(label="day 1", upto=1, text="One tick. / That's the *whole job* today.",
                       note="Pick it so small you can't fail. / *2 minutes counts.*"),
                  dict(label="week 1", upto=7, text="7 in a row. / Now you *want* to keep it.",
                       note="Seeing progress *feels good.* / That feeling is what brings you back."),
                  dict(label="day 11 · life happened", upto=12, missed=[11], text="A missed day. / *Not* the end.",
                       note="Back on the next day. Rough day? / Do the *tiny version.* The chain holds."),
                  dict(label="week 3", upto=21, missed=[11], text="Put it where / *you can see it.*",
                       note="In 138 studies, tracking helped most / when progress was *written down* or *shared.*"),
                  dict(label="day 30", upto=30, missed=[11], text="29 of 30. / *Not perfect. Better.*",
                       note="You didn't need a perfect streak. / You needed to *keep coming back.*")],
          do="Tonight, draw a *30-day grid.* Stick it where the habit happens. Tick it the *second* you finish.",
          do_why="Tick it right away: the reward lands *while the habit is fresh.*",
          save="send this to your accountability buddy"),
     "30 ticks. Watch a habit fill in.", "hold the dots and slide",
     "30 ticks. Hold the dots and slide, and watch a habit fill in 👀\n\n"
     "📅 Day 1: one tick. Pick something so small you can't fail. 2 minutes counts.\n"
     "⭐ Week 1: 7 in a row, and now you want to keep it. Seeing progress feels good, and that feeling brings you back.\n"
     "✗ Day 11: life happened. A missed day is not the end. Back on the next day, and on a rough day do the tiny version.\n"
     "📌 Week 3: put the tracker where you can see it. In a review of 138 studies, monitoring progress helped people reach goals, "
     "most of all when progress was written down or shared.\n"
     "🏆 Day 30: 29 of 30. Not perfect. Better.\n\n"
     "Why it works: Atomic Habits calls it making a habit satisfying. A habit you can see yourself doing is one you repeat, and the "
     "empty square tomorrow pulls you back.\n\n"
     "Do this: tonight, draw a 30-day grid. Stick it where the habit happens. Tick it the second you finish.\n\n"
     "Send this to your accountability buddy.\n\n#habittracker #habits #atomichabits #selfimprovement #focus",
     "What habit goes on your grid? Sources: Harkin et al. 2016, Psychological Bulletin (138 studies, 19,951 participants: prompting "
     "people to monitor progress made goal attainment more likely; stronger when progress was physically recorded or publicly reported; "
     "APA press release Oct 2015). Lally et al. 2010 (one missed day did not materially affect habit formation). Ideas from Atomic "
     "Habits (Clear: make it satisfying, habit tracking, scale it down on bad days).")

# ------------------------------------------------------------------ Hourback · road-trip map · Oct 20 17:45 (replaces hb-1020-speedy-meetings)
ifmt("hb-1020-roadmap-agent", HB, "2026-10-20T17:45",
     dict(kind="roadmap", field="plum", do_field="yel", car="🚗",
          beats=[dict(text="Give an *AI agent* / a job. / *Follow its route.*", size=104,
                      note="Chatbots answer. Agents *do things.* / Here's what happens in between."),
                 dict(label="stop 1 · the goal", sign="🎯", text="You give it a *goal,* / not a list of clicks.", size=86,
                      note="“Plan a Japanese breakfast for 4 / and buy the ingredients.” / That's from OpenAI's own demo."),
                 dict(label="stop 2 · the plan", sign="🧭", text="It *breaks the job* / into steps.", size=90,
                      note="Find a recipe, list ingredients, / pick a store, compare prices. / It *plans* before it acts."),
                 dict(label="stop 3 · the tools", sign="🖱️", text="It *uses a browser,* / the way you would.", size=86,
                      note="ChatGPT agent (July 2025) clicks, scrolls / and types in its own browser, and can / use a *terminal* and *connected apps.*"),
                 dict(label="stop 4 · the check-in", sign="✋", text="Before it *pays,* / it *asks you.*", size=92,
                      note="It asks permission before actions / that matter. You log in yourself, / and can *take over* any time."),
                 dict(label="stop 5 · arrived", sign="🏁", text="A *finished job,* / plus a summary.", size=92,
                      note="It can still make mistakes. / Check the cart, the dates / and the *total* before you confirm.")],
          do="This week, give an agent one *low-stakes* job (compare 3 options, or plan a meal) and *watch it work.*",
          do_size=72, do_why="You'll see where it's brilliant, and *where it stumbles.*",
          save="send this to the friend who still thinks AI just chats"),
     "Give an AI agent a job. Follow its route.", "follow the route",
     "Chatbots answer. Agents do things. Give an AI agent a job and follow its route 👉\n\n"
     "🎯 The goal: you describe the outcome, not the clicks. OpenAI's own launch demo: plan a Japanese breakfast for four and buy the ingredients.\n"
     "🧭 The plan: it breaks the job into steps (recipe, ingredients, store, prices) before acting.\n"
     "🖱️ The tools: ChatGPT agent (launched July 17, 2025) works in its own virtual browser, clicking, scrolling and typing like you, "
     "and can use a terminal and connected apps like Gmail.\n"
     "✋ The check-in: it asks for permission before actions of consequence, like a purchase. You log in to sites yourself, and you "
     "can pause it or take over at any time. It's trained to refuse high-risk jobs like bank transfers.\n"
     "🏁 Arrived: a finished task and a summary. It can still make mistakes, so check the details before you confirm.\n\n"
     "Why it matters: this is the shift from AI that talks to AI that acts. Anthropic (computer use, 2024) and Google (Project Mariner) "
     "are building the same idea.\n\n"
     "Do this: this week, give an agent one low-stakes job, like comparing 3 options or planning a meal, and watch it work.\n\n"
     f"Send this to the friend who still thinks AI just chats.\n\n#aiagents #chatgpt #ai #futureofwork #hourback",
     "What job would you hand an agent first? Source: OpenAI, 'Introducing ChatGPT agent' (July 17, 2025): visual browser, text "
     "browser, terminal, API access and connectors; asks permission before actions of consequence; you can interrupt or take over; "
     "refuses high-risk tasks such as bank transfers; can still make mistakes. Features and plans change; check what your plan includes.")


# ================================================================== Oct 21
REPLACES.update({"hb-1021-refund-email": "hb-1021-streak-10-hours"})

# ------------------------------------------------------------------ Littlefold · streak calendar · Oct 21 17:00 (bonding; replaces my lf-1021-reveal-50-a-month)
ifmt("lf-1021-streak-serve-return", LF, "2026-10-21T17:00",
     dict(kind="streak", field="cream", do_field="pink", days=30, marks={7: "⭐", 14: "🗣️", 30: "💛"},
          hook="*5 minutes* a day / that *build a brain.* / Watch 30 days / fill in.", hook_size=96,
          frames=[dict(label="day 1 · share the focus", upto=1, text="Watch what / *they're* looking at.",
                       note="A coo, a point, a long stare at the fan. / That's a *serve.* Notice it.", pill="🔥 day 1 · 5 minutes, phone away"),
                  dict(label="week 1 · return it", upto=7, text="Smile, nod, / *answer back.*",
                       note="“Yes! The fan!” A hug, a word, a smile. / Each back-and-forth *wires their brain.*"),
                  dict(label="week 2 · name it", upto=14, text="*Name* what they / see and feel.",
                       note="“That's a dog. He's fluffy. You're excited!” / The words they hear now, they'll *say later.*"),
                  dict(label="week 3 · take turns, then wait", upto=21, missed=[17], text="Then *wait.* / It's their turn.",
                       note="Count to 5 in your head. Little ones / need time to answer. *The pause is their turn.*"),
                  dict(label="day 30 · endings", upto=30, missed=[17], text="Notice when / they're *done.*",
                       note="Looking away? Fussing? Let them end it. / Tomorrow, *they'll start the next one.*")],
          do="Tonight: 5 minutes, phone away. *Follow their gaze,* answer back, *name it,* then *wait.*",
          do_why="Tiny back-and-forths, repeated daily, are how a brain *builds itself.*",
          save="send this to a new parent (or a new grandparent)"),
     "5 minutes a day that build a brain. Watch 30 days fill in.", "hold the dots and slide",
     "5 minutes a day that build a brain. Hold the dots and slide 👀\n\n"
     "Scientists at Harvard's Center on the Developing Child call it serve and return. Your baby \"serves\" (a coo, a look, a point). "
     "You \"return\" it (a smile, a word). Back and forth. Those moments build the connections in a young brain, and they're the "
     "heart of bonding.\n\n"
     "Their 5 steps, one a week:\n"
     "👀 Share the focus: notice what they're looking at.\n"
     "🙂 Return it: smile, nod, answer back, hug.\n"
     "🗣️ Name it: \"That's a dog. He's fluffy.\" Words they hear now, they'll say later.\n"
     "⏳ Take turns, and wait: give them time to answer. The pause is their turn.\n"
     "👋 Practice endings: when they look away, let them end it.\n\n"
     "Missed a day? That's real life. Pick it back up tomorrow. In The Power of Showing Up, Siegel and Bryson put it simply: kids "
     "need to feel seen, again and again. Not perfectly.\n\n"
     "Do this: tonight, 5 minutes, phone away. Follow their gaze, answer back, name it, then wait.\n\n"
     "Send this to a new parent, or a new grandparent.\n\n#bonding #servereturn #newparents #babydevelopment #canadianparents",
     "Which step does your little one love? Source: Harvard University Center on the Developing Child, '5 Steps for Brain-Building "
     "Serve and Return' (share the focus, support and encourage, name it, take turns and wait, practice endings and beginnings) and "
     "'Serve and Return' (these interactions shape brain architecture). The Power of Showing Up (Siegel & Bryson, 2020). "
     "5 minutes a day is our suggested start, not a rule.")

# ------------------------------------------------------------------ Fully Funded · swipe to fix · Oct 21 17:00 (new slot)
ifmt("ff-1021-split-autopilot", FF, "2026-10-21T17:00",
     dict(kind="split", field="lite", do_field="cob",
          hook="Your paycheque, / *on autopilot* in 5 swipes", hook_size=82,
          rows=[dict(before="Save whatever's left / at the end of the month",
                     after="*Pay yourself first:* an automatic / transfer the day your pay lands.",
                     why="What's left at month-end is usually nothing."),
                dict(before="Bills paid / when you remember",
                     after="Every bill on *autopay,* / set for 2 days after payday.",
                     why="No late fees. Nothing to remember."),
                dict(before="Invest “when I have / time to research”",
                     after="A *monthly automatic purchase* / of one broad index fund.",
                     why="Buying every month: no guessing the right moment."),
                dict(before="Get a raise, / spend all of it",
                     after="Next raise: *half* goes / straight to the auto-transfer.",
                     why="You still feel the raise. Future you gets the rest."),
                dict(before="Check your balance / with dread",
                     after="One *15-minute money date* / a month. Just check it ran.",
                     why="The system does the work. You steer.")],
          do="This payday, set *one automatic transfer:* 10% of your pay, the day it lands, into your TFSA.",
          do_size=72, do_why="The money you never see, you *don't miss.*",
          save="send this to the friend who “can't save”"),
     "Your paycheque, on autopilot in 5 swipes", "swipe to fix it",
     "Your paycheque, on autopilot in 5 swipes 👉\n\n"
     "1. Pay yourself first. An automatic transfer the day your pay lands, before you can spend it. The Wealthy Barber's rule of "
     "thumb is 10% of every paycheque; The Richest Man in Babylon said it 100 years ago: a part of all you earn is yours to keep.\n"
     "2. Every bill on autopay, set for 2 days after payday.\n"
     "3. A monthly automatic purchase of one broad index fund. You never have to guess the right moment to invest.\n"
     "4. Next raise: half goes straight to the auto-transfer. In the famous Save More Tomorrow study, workers who pre-committed future "
     "raises to savings went from saving 3.5% to 13.6% of pay in about 3 years.\n"
     "5. One 15-minute money date a month, just to check it all ran.\n\n"
     "Why it works: willpower runs out; automation doesn't. Ramit Sethi's I Will Teach You to Be Rich is built on this: make good "
     "choices once, then let the system repeat them.\n\n"
     "Do this: this payday, set one automatic transfer: 10% of your pay, the day it lands, into your TFSA.\n\n"
     f"Send this to the friend who \"can't save\".\n\n{NG} Education, not advice.\n\n#payyourselffirst #automateyourmoney #tfsa #budgeting #personalfinancecanada",
     "Which swipe will you do first? Sources: Thaler & Benartzi 2004, 'Save More Tomorrow', Journal of Political Economy (average saving "
     "rates rose from 3.5% to 13.6% over 40 months). Ideas from The Wealthy Barber (Chilton), The Richest Man in Babylon (Clason) and I "
     "Will Teach You to Be Rich (Sethi). 2026 TFSA limit: $7,000 (CRA).")

# ------------------------------------------------------------------ Locked Hour · staircase climb · Oct 21 17:00 (new slot)
ifmt("lh-1021-climb-4-steps", LH, "2026-10-21T17:00",
     dict(kind="climb", field="cream", do_field="pink", obj="hourglass", cta="climb the 4 steps →", y_hi=880,
          beats=[dict(text="Every habit / has *4 steps.* / Climb them.", size=112,
                      note="The core idea of Atomic Habits, on one habit: / *reading at night* instead of scrolling."),
                 dict(label="step 1 · the cue", step="make it obvious", sign="👀", size=86,
                      text="Book *on your pillow.* / Phone charging / *in the kitchen.*",
                      note="You can't start what you don't notice. / Put the cue *where your hand already goes.*"),
                 dict(label="step 2 · the craving", step="make it attractive", sign="✨", size=90,
                      text="Pair it with / something you *love.*",
                      note="Your favourite tea, only with the book. / Want the pairing, and the habit *comes along.*"),
                 dict(label="step 3 · the response", step="make it easy", sign="🪶", size=90,
                      text="Start with / *one page.*",
                      note="Book open at your page, lamp already on. / Every bit of friction you remove / is a reason *not* to skip."),
                 dict(label="step 4 · the reward", step="make it satisfying", sign="🏆", size=90,
                      text="Tick it off. / *Feel the win.*",
                      note="What feels good *right away* gets repeated. / A tick on the calendar, every night."),
                 dict(label="the summit", step="it runs itself", sign="🔒", size=90,
                      text="Cue, craving, / response, reward. / *On repeat.*",
                      note="Breaking a bad habit? *Flip all 4:* / invisible, unattractive, hard, unsatisfying.")],
          do="Tonight, pick one habit and set its *cue:* put the thing *where your hand already goes.*",
          do_why="Make it obvious first. *The other 3 steps get easier.*",
          save="send this to the friend who scrolls till 1 am"),
     "Every habit has 4 steps. Climb them.", "climb the 4 steps",
     "Every habit has 4 steps. Climb them with one example: reading at night instead of scrolling 👉\n\n"
     "👀 The cue: make it obvious. Book on your pillow, phone charging in the kitchen.\n"
     "✨ The craving: make it attractive. Pair it with something you love, like your favourite tea, only with the book. Researchers "
     "call it temptation bundling: in one study, people who could only hear their favourite audiobooks at the gym went more often.\n"
     "🪶 The response: make it easy. Start with one page. Book open at your page, lamp already on.\n"
     "🏆 The reward: make it satisfying. A tick on the calendar, every night. What feels good right away gets repeated.\n"
     "🔒 The summit: cue, craving, response, reward, on repeat.\n\n"
     "Why it works: this is the habit loop (Charles Duhigg's The Power of Habit), turned into 4 levers by James Clear in Atomic Habits. "
     "To break a bad habit, flip them: make it invisible, unattractive, hard and unsatisfying.\n\n"
     "Do this: tonight, pick one habit and set its cue. Put the thing where your hand already goes.\n\n"
     "Send this to the friend who scrolls till 1 am.\n\n#atomichabits #habits #readingathome #selfimprovement #focus",
     "Which step is your weak spot? Sources: Clear, Atomic Habits (2018): the four laws of behaviour change. Duhigg, The Power of Habit "
     "(2012): cue, routine, reward. Milkman, Minson & Volpp 2014, Management Science, 'Holding the Hunger Games hostage at the gym' "
     "(temptation bundling raised gym visits).")

# ------------------------------------------------------------------ Hourback · streak calendar · Oct 21 17:45 (replaces hb-1021-refund-email)
ifmt("hb-1021-streak-10-hours", HB, "2026-10-21T17:45",
     dict(kind="streak", field="plum", do_field="yel", days=30, marks={7: "⭐", 30: "🧠"},
          hook="*10 hours* to / actually *get* AI. / Watch 30 days / fill in.", hook_size=100,
          frames=[dict(label="day 1 · 20 minutes", upto=1, text="Bring it *one real task* / from your day.",
                       note="Ethan Mollick's rule 1: *always invite AI / to the table.* An email, a plan, a question.",
                       pill="⏱️ day 1 · 20 min of practice"),
                  dict(label="week 1 · 2 h 20 min", upto=7, text="Talk to it like / a *new colleague.*",
                       note="Give it a role and context: “You're a / patient tutor. I'm a nurse…” *Then push back.*",
                       pill="⏱️ 7 days · 2 h 20 min"),
                  dict(label="week 2 · 4 h 40 min", upto=14, text="Find its *edges.*",
                       note="Ask about something you know cold. / Where it's wrong, it's *confidently* wrong. / Now you know where to check.",
                       pill="⏱️ 14 days · 4 h 40 min"),
                  dict(label="week 3 · 7 hours", upto=21, text="Stay the / *human in the loop.*",
                       note="Rule 2: it drafts, you decide. You check / the facts, you sign your name. *You own it.*",
                       pill="⏱️ 21 days · 7 h"),
                  dict(label="day 30 · 10 hours", upto=30, text="Now you *get it.*",
                       note="Mollick's rough rule: about *10 hours* of use. / Rule 4: this is the *worst* AI you'll ever use.",
                       pill="🧠 30 days · 10 h")],
          do="Tomorrow, block *20 minutes.* Bring AI *one real task* from your day. Repeat for 30 days.",
          do_why="Explainers don't build intuition. *Use does.*",
          save="send this to the friend who keeps saying “I should learn AI”"),
     "10 hours to actually get AI. Watch 30 days fill in.", "hold the dots and slide",
     "10 hours to actually get AI. Hold the dots and slide 👀\n\n"
     "Wharton professor Ethan Mollick (Co-Intelligence) has a loose rule of thumb: you need about 10 hours of real use before AI "
     "\"clicks\". That's 20 minutes a day for 30 days:\n\n"
     "📅 Day 1: bring it one real task from your day. His rule 1: always invite AI to the table.\n"
     "⭐ Week 1: talk to it like a new colleague. Give it a role and context, then push back on its answer.\n"
     "🔎 Week 2: find its edges. Ask about something you know cold. Where it's wrong, it's confidently wrong, and now you know where to check.\n"
     "🧑 Week 3: stay the human in the loop (rule 2). It drafts, you decide.\n"
     "🧠 Day 30: you get it. And rule 4: assume this is the worst AI you will ever use.\n\n"
     "Why it works: AI is uneven. It's brilliant at some tasks and weak at others that look similar. Only hands-on use shows you "
     "where the line is for your work.\n\n"
     "Do this: tomorrow, block 20 minutes and bring AI one real task. Repeat for 30 days.\n\n"
     f"Send this to the friend who keeps saying \"I should learn AI\".\n\n#learnai #ai #chatgpt #futureofwork #hourback",
     "What's your day-1 task? Source: Ethan Mollick, Co-Intelligence (2024), and Stanford GSB, 'Co-Intelligence: An AI Masterclass "
     "with Ethan Mollick' (June 2024): \"Ten hours is my loose rule of thumb\" (he notes it's a rough estimate); his four rules: always "
     "invite AI to the table, be the human in the loop, treat AI like a human, assume this is the worst AI you will ever use.")


# ================================================================== Oct 22
REPLACES.update({"lf-1022-safe-sleep": "lf-1022-follow-safe-sleep", "hb-1022-brain-dump": "hb-1022-split-prompt"})

# ------------------------------------------------------------------ Littlefold · follow the line · Oct 22 17:00 (replaces lf-1022-safe-sleep)
LF22_LINES = [
    dict(col="#E0306C", icon="🛋️", start="Asleep on me, / on the couch",
         fix="*Move baby* to their crib, on their back. Never sleep together on a *couch or armchair.*"),
    dict(col="#E8A93A", icon="🚗", start="Asleep in the / car seat or swing",
         fix="Fine for the ride. Once you're home, *move them to their crib.*"),
    dict(col="#6E8FC4", icon="🛏️", start="Asleep in / our bed",
         fix="*Room-share, not bed-share:* their own crib, beside your bed, for the *first 6 months.*"),
]
ifmt("lf-1022-follow-safe-sleep", LF, "2026-10-22T17:00",
     dict(kind="follow", field="cream", do_field="pink", pano=5, lines=LF22_LINES,
          hook="Baby fell asleep. / *Where?* / Follow the line.",
          mids=[dict(label="the basics, every sleep", text="On their *back.* / On a *firm, flat* / mattress. / In their *own* space. / Naps too."),
                dict(label="what goes in the crib", text="A fitted sheet. / *That's it.* / No pillows, bumpers, / toys or loose blankets."),
                dict(label="chilly night?", text="A *sleep sack* or / onesie, *not* a blanket. / Keep them from / overheating, and keep / the home *smoke-free.*")],
          src="Sources: Health Canada & Public Health Agency of Canada, Safe sleep for your baby · Government of New Brunswick, Safe sleep for babies · General information",
          do="Tonight, take *everything* out of the crib except the fitted sheet, and move it *beside your bed.*",
          do_why="Close enough to hear them. *Safe enough to sleep.*",
          save="send this to someone expecting"),
     "Baby fell asleep. Where? Follow the line.", "follow the line",
     "Baby fell asleep. Where? Find your spot and follow the line 👉\n\n"
     "🛋️ Asleep on you, on the couch: gently move baby to their crib, on their back. Never sleep with a baby on a couch, sofa or armchair.\n"
     "🚗 Asleep in the car seat or swing: fine for the ride, but these aren't for long, unsupervised sleep. At home, move them to their crib.\n"
     "🛏️ Asleep in your bed: room-share, not bed-share. Their own crib, cradle or bassinet beside your bed, for the first 6 months.\n\n"
     "The basics, every sleep, naps too: on their back, on a firm, flat mattress, in their own space. In the crib: a fitted sheet, "
     "nothing else. No pillows, bumpers, toys or loose blankets. Chilly? A sleep sack or onesie instead of a blanket, and don't let them "
     "overheat. Keep your home smoke-free.\n\n"
     "Why it matters: these are the steps Canada's health agencies recommend to lower the risk of sudden infant death. Simple, and they "
     "work best when every sleep follows them.\n\n"
     "Do this: tonight, take everything out of the crib except the fitted sheet, and move it beside your bed.\n\n"
     f"Send this to someone expecting.\n\n{NOT_MED}\n\n#safesleep #newborn #newparents #canadianparents #babysleep",
     "Where does your little one fall asleep most? Sources: Health Canada and the Public Health Agency of Canada, 'Safe sleep for your "
     "baby' (back to sleep, firm flat surface, crib/cradle/bassinet in your room for the first 6 months, nothing in the crib but a fitted "
     "sheet). Government of New Brunswick, 'Safe sleep for babies' (never on a couch, sofa or armchair or sharing those surfaces with a "
     "sleeping person; not in car seats, swings or bouncers for long periods, especially unsupervised; sleep sack or onesie instead of a "
     "blanket; prevent overheating; smoke-free).")

# ------------------------------------------------------------------ Fully Funded · streak calendar · Oct 22 17:00 (new slot)
ifmt("ff-1022-streak-every-dollar", FF, "2026-10-22T17:00",
     dict(kind="streak", field="lite", do_field="cob", days=30, marks={7: "⭐", 30: "🔑"},
          hook="*30 days* of writing / down *every dollar.* / Watch it fill in.", hook_size=96,
          frames=[dict(label="day 1", upto=1, text="Write down / *every* purchase.",
                       note="Even the $2 one. Notes app, one line each. / *No judging yet.* Just look."),
                  dict(label="week 1", upto=7, text="Sort it into / *3 buckets.*",
                       note="Needs, wants, savings. A classic target: / *50/30/20* (from the book All Your Worth)."),
                  dict(label="week 2", upto=14, text="Find the *leaks.*",
                       note="Subscriptions you forgot. Fees. / Delivery charges. *Cancel one today.*"),
                  dict(label="week 3", upto=21, missed=[19], text="Then the *big 3.*",
                       note="Shelter, transport, food: about / *64%* of household spending (StatCan)."),
                  dict(label="day 30", upto=30, missed=[19], text="Now you *know* / *your number.*",
                       note="What a normal month really costs. / It sets your *emergency fund* and goals.")],
          do="Starting tomorrow, write down *every purchase* for 30 days. One line each, in your notes app.",
          do_why="You can't steer money *you can't see.*",
          save="send this to your money buddy"),
     "30 days of writing down every dollar. Watch it fill in.", "hold the dots and slide",
     "30 days of writing down every dollar. Hold the dots and slide 👀\n\n"
     "📅 Day 1: write down every purchase, even the $2 one. No judging yet. Just look.\n"
     "⭐ Week 1: sort it into 3 buckets: needs, wants, savings. A classic target from Elizabeth Warren's All Your Worth: 50% needs, 30% "
     "wants, 20% savings.\n"
     "🔍 Week 2: find the leaks. Forgotten subscriptions, fees, delivery charges. Cancel one.\n"
     "🏠 Week 3: then the big 3. Shelter, transportation and food were about 64% of what Canadian households spent in 2023. A better "
     "phone plan or insurance rate there beats skipping a latte.\n"
     "🔑 Day 30: you know your number: what a normal month really costs you.\n\n"
     "Why it works: The Millionaire Next Door found that the people who quietly built wealth tended to know exactly where their "
     "money went. Awareness comes first; the budget comes after.\n\n"
     "Do this: starting tomorrow, write down every purchase for 30 days. One line each.\n\n"
     "Send this to your money buddy.\n\nEducation, not advice.\n\n#budgeting #trackyourspending #moneytips #personalfinancecanada #savemoney",
     "Which bucket surprised you? Sources: Statistics Canada, The Daily, 'Survey of Household Spending, 2023' (May 21, 2025): shelter "
     "32.1%, transportation 15.8%, food 15.7% of total consumption. Warren & Tyagi, All Your Worth (2005): 50/30/20. Stanley & Danko, "
     "The Millionaire Next Door (1996).")

# ------------------------------------------------------------------ Locked Hour · swipe to fix · Oct 22 17:00 (new slot)
ifmt("lh-1022-split-desk", LH, "2026-10-22T17:00",
     dict(kind="split", field="cream", do_field="pink", after_size=52, why_size=36, before_size=50,
          hook="Your desk, / *rebuilt for focus* in 5 swipes", hook_size=92,
          rows=[dict(before="Phone on the desk, / face down",
                     after="Phone in *another room* / for the hour.",
                     why="Even silent and face down, it drained focus in one study."),
                dict(before="12 tabs and your inbox open",
                     after="*One window,* full screen.",
                     why="Every switch leaves “attention residue” behind."),
                dict(before="Notifications on",
                     after="*Do Not Disturb* for the hour. / Check messages at set times.",
                     why="Fewer email checks a day meant less stress in a study."),
                dict(before="Clutter: mail, snacks, / other projects",
                     after="The desk holds *only* / this task's stuff.",
                     why="What you see is what you're cued to do."),
                dict(before="Stop mid-task with / no idea where you were",
                     after="Before you stop: write / *tomorrow's first step.*",
                     why="A written plan quiets the unfinished task in your head.")],
          do="Before your next work block: *phone out,* one window, *Do Not Disturb* on, *one task* on the desk.",
          do_size=72, do_why="Design beats discipline: *fix the room once,* win every session.",
          save="send this to your study buddy"),
     "Your desk, rebuilt for focus in 5 swipes", "swipe to fix it",
     "Your desk, rebuilt for focus in 5 swipes 👉\n\n"
     "1. Phone in another room. In one study, people did worse on focus tests with their phone on the desk, even face down and silent.\n"
     "2. One window, full screen. When you switch tasks, part of your attention stays behind. Researcher Sophie Leroy called it attention residue.\n"
     "3. Do Not Disturb for the hour, and check messages at set times. In one experiment, people told to check email only 3 times a day felt less stressed.\n"
     "4. The desk holds only this task's stuff. What you see is what you're cued to do. Atomic Habits calls it environment design.\n"
     "5. Before you stop, write tomorrow's first step. Making a plan for an unfinished task quiets it in your head, so it stops nagging you.\n\n"
     "Why it works: willpower is a bad tool against a phone that buzzes all day. Change the room once and every session gets easier. "
     "Cal Newport's Deep Work makes the same bet.\n\n"
     "Do this: before your next work block, phone out, one window, Do Not Disturb on, one task on the desk.\n\n"
     "Send this to your study buddy.\n\n#deepwork #focus #studytips #productivity #desksetup",
     "Which swipe fixes your biggest leak? Sources: Ward et al. 2017, Journal of the Association for Consumer Research ('Brain Drain'; a "
     "later replication was mixed). Leroy 2009, Organizational Behavior and Human Decision Processes (attention residue). Kushlev & Dunn "
     "2015, Computers in Human Behavior (checking email less often reduced daily stress). Masicampo & Baumeister 2011, JPSP (making a plan "
     "for unfinished goals reduced their intrusion). Ideas from Atomic Habits (Clear) and Deep Work (Newport).")

# ------------------------------------------------------------------ Hourback · swipe to fix · Oct 22 17:45 (replaces hb-1022-brain-dump)
ifmt("hb-1022-split-prompt", HB, "2026-10-22T17:45",
     dict(kind="split", field="plum", do_field="yel",
          hook="Your AI prompt, / *fixed in 5 swipes*", hook_size=86,
          rows=[dict(before="“Write an email / to my landlord.”",
                     after="Add *who, what, why:* “Polite email, landlord, / leaky tap, 2nd ask, fixed by Friday.”",
                     why="It can't read your mind. Context is the biggest upgrade."),
                dict(before="“Make it sound good.”",
                     after="*Paste a message* in the tone / you want: “Like this one.”",
                     why="Showing the tone beats describing it."),
                dict(before="“Which plan should I pick?” / in one line",
                     after="“*Think it through step by step,* / then give me your answer.”",
                     why="Room to reason improves answers to hard questions."),
                dict(before="Trust the facts / it gives you",
                     after="“*Tell me if you're unsure.* / Show where each fact comes from.”",
                     why="It may guess and sound sure. Make it flag doubt."),
                dict(before="Take the first answer",
                     after="*Push back:* “Shorter. Warmer. / Drop the last line.”",
                     why="It's a conversation. The second draft is better.")],
          do="Take your *last prompt.* Rewrite it with all 5 fixes. Compare the two answers *side by side.*",
          do_why="See the difference once, and *you'll never prompt the old way again.*",
          save="send this to the friend who says AI gives bad answers"),
     "Your AI prompt, fixed in 5 swipes", "swipe to fix it",
     "Your AI prompt, fixed in 5 swipes 👉\n\n"
     "1. Add who, what and why. \"Write an email to my landlord\" becomes \"Polite email to my landlord about the leaky tap. Second time "
     "asking. I want it fixed by Friday.\" Both OpenAI's and Anthropic's own guides start here: clear, specific instructions with context.\n"
     "2. Paste a message written in the tone you want. Showing it steers the style better than adjectives like \"professional\".\n"
     "3. Ask it to think it through step by step before answering, for anything with trade-offs. Newer reasoning models do this on their own.\n"
     "4. Ask it to say when it's unsure and where each fact comes from. Models can guess and still sound confident.\n"
     "5. Push back. \"Shorter. Warmer. Drop the last line.\" The second draft is almost always better.\n\n"
     "Why it works: the model predicts its answer from what you give it. Better input, better prediction.\n\n"
     "Do this: take your last prompt, rewrite it with all 5 fixes, and compare the two answers side by side.\n\n"
     f"Send this to the friend who says AI gives bad answers.\n\n#promptengineering #chatgpt #claude #aitips #hourback",
     "Which fix made the biggest difference? Sources: OpenAI, prompt engineering guide (write clear instructions, provide reference text "
     "that shows what you want, give the model time to think). Anthropic, prompt engineering overview (be clear and direct, show the model what good "
     "looks like, let Claude think step by step). OpenAI, 'Why language models hallucinate' (Sept 2025).")


# ================================================================== Oct 23 (no page-file posts in these slots: all new)
# ------------------------------------------------------------------ Littlefold · staircase climb · Oct 23 17:00
ifmt("lf-1023-climb-first-words", LF, "2026-10-23T17:00",
     dict(kind="climb", field="cream", do_field="pink", obj="emoji:👶", cta="climb it together →",
          beats=[dict(text="From *first coo* / to *“mama.”* / Climb it together.", size=104,
                      note="Baby's first year of talking, / and what *you* do at each step."),
                 dict(label="by 2 months", step="2 months", sign="🍼", size=92, text="Sounds that / *aren't* crying.",
                      note="Answer every one. Copy the sound back: / you just had their *first conversation.*"),
                 dict(label="by 4 months", step="4 months", sign="🎵", size=92, text="*Cooing:* / “oooo,” “aahh.”",
                      note="They make sounds *back* when you talk. / Say something, then *pause:* their turn."),
                 dict(label="by 6 months", step="6 months", sign="😛", size=92, text="*Taking turns* / making sounds.",
                      note="Raspberries, squeals. *Blow one back!* / That back-and-forth is how talking grows."),
                 dict(label="by 9 months", step="9 months", sign="🗣️", size=92, text="“*mamamama*” / “*babababa*”",
                      note="Name what you touch: “Cup. *Your* cup.” / Short words, said often."),
                 dict(label="by 12 months", step="12 months", sign="💛", size=92, text="*“Mama,” “dada,”* / or a special name.",
                      note="Plus “bye-bye.” Every baby has their / own pace. *Worried? Ask your doctor.*")],
          do="Today, talk through *one routine* out loud (a diaper change, a bath): *name it,* then *pause* for their turn.",
          do_size=72, do_why="Talking *with* them beats talking *at* them.",
          save="send this to someone with a baby under 1"),
     "From first coo to mama. Climb it together.", "climb it together",
     "From first coo to \"mama\": baby's first year of talking, one step at a time 👉\n\n"
     "🍼 By 2 months: sounds that aren't crying. Answer every one. Copy the sound back.\n"
     "🎵 By 4 months: cooing (\"oooo\", \"aahh\"), and sounds back when you talk. Say something, then pause. That pause is their turn.\n"
     "😛 By 6 months: taking turns making sounds, raspberries, squeals. Blow one back.\n"
     "🗣️ By 9 months: \"mamamama\", \"babababa\". Name what you touch: \"Cup. Your cup.\" Short words, said often, in your home language.\n"
     "💛 By 12 months: \"mama\", \"dada\" or another special name, and a bye-bye wave.\n\n"
     "Why your part matters: a study at MIT found that the number of back-and-forth conversational turns, more than the number of words a "
     "child simply heard, was linked to activity in the brain's language areas. Talk with them, not at them.\n\n"
     "These are the CDC's milestones: what most babies (75% or more) do by each age. Every baby has their own pace. If you're worried, "
     "ask your doctor; early help works best.\n\n"
     "Do this: today, talk through one routine out loud (a diaper change, a bath). Name it, then pause for their turn.\n\n"
     f"Send this to someone with a baby under 1.\n\n{NOT_MED}\n\n#babytalk #babymilestones #bonding #newparents #canadianparents",
     "Which step is your little one on? Sources: CDC, 'Learn the Signs. Act Early.' milestones (2022 update; what 75% or more of children "
     "do by each age): 2 months sounds other than crying; 4 months cooing, sounds back when you talk; 6 months takes turns making sounds, "
     "raspberries, squeals; 9 months 'mamamama', 'babababa'; 12 months 'mama'/'dada' or another special name, waves bye-bye. Romeo et al. "
     "2018, Psychological Science, 'Beyond the 30-million-word gap' (conversational turns and brain activity).")

# ------------------------------------------------------------------ Fully Funded · road-trip map · Oct 23 17:00
_FHSA5 = round(sum(8000 * 1.1 ** k for k in range(1, 6)), -2)
ifmt("ff-1023-roadmap-fhsa", FF, "2026-10-23T17:00",
     dict(kind="roadmap", field="lite", do_field="cob", car="🚗",
          beats=[dict(text="Saving for a / *first home?* / Take the *FHSA* route.", size=104,
                      note="A tax break going in. / *Tax-free* coming out."),
                 dict(label="stop 1 · open it now", sign="🔑", text="*Open one now,* / even with $0.", size=96,
                      note="Room starts the year you open it: / *$8,000* a year, $40,000 lifetime. / Unused room carries forward (max $8,000)."),
                 dict(label="stop 2 · put money in", sign="🧾", text="Every dollar in / *cuts your tax.*", size=96,
                      note="Deductible, like an RRSP. At a 30% / tax rate, $8,000 in ≈ *$2,400 back.*"),
                 dict(label="stop 3 · let it grow", sign="📈", text="*Invest* it. / Don't just park it.", size=96,
                      note=f"$8,000 a year for 5 years at 10% / ≈ *${_FHSA5:,.0f}.* Buying sooner? / Safer investments make more sense."),
                 dict(label="stop 4 · buy your home", sign="🏡", text="Take it all out, / *tax-free.*", size=96,
                      note="Growth included, for a qualifying / first home. Can be combined with / the RRSP *Home Buyers' Plan.*"),
                 dict(label="stop 5 · plans changed?", sign="🛟", text="Move it to your / *RRSP,* tax-free.", size=96,
                      note="No tax, and no RRSP room used. / You have up to *15 years* from opening.")],
          do="This week, *open an FHSA* (even with $0) so your room starts counting this year.",
          do_why="Room you don't open *never piles up.* The clock starts when you do.",
          save="send this to a friend saving for their first place"),
     "Saving for a first home? Take the FHSA route.", "follow the route",
     "Saving for a first home? Take the FHSA route 👉 (First Home Savings Account, Canada)\n\n"
     "🔑 Open one now, even with $0. Your room only starts building the year you open it: $8,000 a year, $40,000 lifetime, and unused "
     "room carries forward (up to $8,000).\n"
     "🧾 Every dollar in cuts your tax, like an RRSP. At a 30% marginal tax rate, $8,000 in is about $2,400 back.\n"
     f"📈 Invest it. $8,000 a year for 5 years at 10% a year is about ${_FHSA5:,.0f}. Buying within a couple of years? Safer investments "
     "usually make more sense, because markets can drop right when you need the money.\n"
     "🏡 Take it all out tax-free, growth included, for a qualifying first home. You can combine it with the RRSP Home Buyers' Plan.\n"
     "🛟 Plans changed? Move it to your RRSP tax-free, without using RRSP room. You have up to 15 years from opening.\n\n"
     "Why it's special: most accounts give you a tax break going in OR coming out. The FHSA gives you both.\n\n"
     "Do this: this week, open an FHSA (even with $0) so your room starts counting this year.\n\n"
     f"Send this to a friend saving for their first place.\n\n{NG} Education, not advice.\n\n#fhsa #firsthome #firsttimehomebuyer #personalfinancecanada #tfsa",
     "Which stop are you at? Sources: Department of Finance Canada, 'Canadians can save for their first home with new tax-free First "
     "Home Savings Account' (Aug 2023: $8,000 a year, $40,000 lifetime, unused room up to $8,000 carries forward, deductible, tax-free "
     "qualifying withdrawal, can be combined with the Home Buyers' Plan, 15 years). CRA, FHSA pages (room starts the year you open your "
     "first FHSA; transfers to an RRSP don't use RRSP room). Eligibility: 18+, resident, first-time home buyer. Maths: $8,000 at the "
     "start of each year, 10% a year, 5 years, no fees; the $2,400 is an illustration at a 30% marginal rate.")

# ------------------------------------------------------------------ Locked Hour · road-trip map · Oct 23 17:00
ifmt("lh-1023-roadmap-sunday-plan", LH, "2026-10-23T17:00",
     dict(kind="roadmap", field="cream", do_field="pink", car="🚗",
          beats=[dict(text="Plan your week / in *20 minutes.* / The Sunday route.", size=104,
                      note="5 stops. Then Monday starts / with a plan, *not a scramble.*"),
                 dict(label="stop 1 · empty your head", sign="🧠", text="*Brain dump:* / every open loop, / on paper.", size=92,
                      note="Unfinished tasks keep nagging you / until they have a plan. Writing one / *quiets them* (studies show it)."),
                 dict(label="stop 2 · look back", sign="🔙", text="What *moved* / last week?", size=100,
                      note="In 12,000 work diary entries, small wins / were the biggest lift to motivation. / *Notice yours.*"),
                 dict(label="stop 3 · pick 3", sign="🎯", text="Pick *3 things* / that matter most.", size=96,
                      note="Not 12. Three. / Everything else is a *maybe.*"),
                 dict(label="stop 4 · block them", sign="📅", text="Give each one / a *time and a place.*", size=92,
                      note="Plans with a when and a where get done / *far more often* (94 studies)."),
                 dict(label="stop 5 · Monday's highlight", sign="🌅", text="Pick *Monday's* / *highlight.*", size=100,
                      note="One thing that would make tomorrow / a win. Do it *first.*")],
          do="This Sunday, set a *20-minute timer* and drive the route: dump, look back, pick 3, block them, *Monday's highlight.*",
          do_size=70, do_why="The week stops running you. *You run it.*",
          save="send this to the friend whose Mondays are chaos"),
     "Plan your week in 20 minutes. The Sunday route.", "follow the route",
     "Plan your week in 20 minutes. Follow the Sunday route 👉\n\n"
     "🧠 Stop 1: brain dump. Every open loop on paper. Unfinished tasks keep nagging at you; making a plan for them quiets them.\n"
     "🔙 Stop 2: look back. What moved last week? In a study of about 12,000 work diary entries, making progress, even small wins, was "
     "the biggest boost to people's motivation.\n"
     "🎯 Stop 3: pick 3 things that matter most. Not 12. Everything else is a maybe.\n"
     "📅 Stop 4: block them. Give each a time and a place. Plans with a when and a where get followed far more often.\n"
     "🌅 Stop 5: pick Monday's highlight, one thing that would make the day a win, and do it first.\n\n"
     "Why it works: you decide once, calmly, on Sunday, instead of 40 times under pressure during the week. Cal Newport's time-blocking "
     "and Make Time's daily highlight are both built on that idea.\n\n"
     "Do this: this Sunday, set a 20-minute timer and drive the route.\n\n"
     "Send this to the friend whose Mondays are chaos.\n\n#weeklyplanning #productivity #timeblocking #focus #habits",
     "Which stop do you skip? Sources: Masicampo & Baumeister 2011, Journal of Personality and Social Psychology (making a plan for "
     "unfinished goals reduced their intrusion). Amabile & Kramer, The Progress Principle (2011; about 12,000 diary entries from 238 "
     "people). Gollwitzer & Sheeran 2006 (94 studies on if-then plans). Ideas from Deep Work (Newport) and Make Time (Knapp & Zeratsky).")

# ------------------------------------------------------------------ Hourback · follow the line · Oct 23 17:45
HB23_LINES = [
    dict(col="#E0306C", icon="✍️", start="Draft, rewrite, / brainstorm",
         fix="*Inside the frontier.* Use it. In the study: faster, more tasks, *40%+ better* quality."),
    dict(col="#E8B800", icon="🔢", start="Facts, numbers, / recent news",
         fix="*Verify.* It can sound sure and be wrong. Ask for sources, then *check them.*"),
    dict(col="#3B3B98", icon="🧩", start="Judgement on / messy evidence",
         fix="*Outside the frontier.* Think it through yourself first. Use AI to *challenge* you, not decide."),
]
ifmt("hb-1023-follow-frontier", HB, "2026-10-23T17:45",
     dict(kind="follow", field="plum", do_field="orng", pano=5, lines=HB23_LINES,
          hook="Is AI good / at this? / *Pick your task.*",
          mids=[dict(label="the study", text="*758* consultants / at BCG. Some got / *GPT-4,* some didn't. / Same tasks. / Harvard-led, 2023."),
                dict(label="inside the frontier", text="With AI: / *12% more* tasks, / *25% faster,* / *40%+ better* / quality."),
                dict(label="outside the frontier", text="On a task built / to trip AI up: / *19 points less likely* / to get it right / than without AI.")],
          src="Source: Dell'Acqua et al. 2023, 'Navigating the Jagged Technological Frontier', Harvard Business School working paper 24-013",
          do="This week, sort your tasks into 3 piles: *AI drafts it,* *AI helps, I check,* and *mine alone.*",
          do_why="The frontier is jagged. *Knowing where it is* is the real skill.",
          save="send this to your team's AI skeptic (and its biggest fan)"),
     "Is AI good at this? Pick your task.", "pick one · follow its line",
     "Is AI good at this? Pick your task and follow the line 👉\n\n"
     "In 2023, researchers from Harvard, Wharton and MIT ran an experiment with 758 consultants at Boston Consulting Group. Some got GPT-4, "
     "some didn't, same tasks.\n\n"
     "✍️ Inside what they called the \"jagged frontier\" (drafting, rewriting, brainstorming, product ideas): consultants using AI finished "
     "12.2% more tasks, 25.1% faster, with over 40% higher quality.\n"
     "🔢 Facts and numbers: verify. AI can sound sure and be wrong. Ask for sources, then check them.\n"
     "🧩 Outside the frontier (a task built to trip AI up, mixing numbers and interviews): consultants using AI were 19 percentage points "
     "less likely to get the right answer than those working without it. They trusted it where they shouldn't have.\n\n"
     "Why it matters: AI isn't good or bad at \"work\". It's brilliant at some tasks and quietly weak at others that look similar. Ethan "
     "Mollick, one of the authors, calls learning that line the key skill.\n\n"
     "Do this: this week, sort your tasks into 3 piles: AI drafts it; AI helps and I check; mine alone.\n\n"
     f"Send this to your team's AI skeptic, and its biggest fan.\n\n#ai #futureofwork #chatgpt #productivity #hourback",
     "Which line was your task? Source: Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon & Lakhani "
     "(2023), 'Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker "
     "Productivity and Quality', HBS Working Paper 24-013: 758 BCG consultants, GPT-4; inside the frontier 12.2% more tasks, 25.1% faster, "
     "40%+ higher quality; outside it, 19 percentage points less likely to be correct. Models have improved since 2023, so the "
     "frontier keeps moving: test it on your own tasks.")


# ================================================================== Oct 24
# ------------------------------------------------------------------ Littlefold · road-trip map · Oct 24 17:00
ifmt("lf-1024-roadmap-bedtime", LF, "2026-10-24T17:00",
     dict(kind="roadmap", field="cream", do_field="pink", car="🚗",
          beats=[dict(text="Bedtime *battles?* / Take the / *calm route.*", size=104,
                      note="5 stops. Same order, every night. / The road *is* the routine."),
                 dict(label="stop 1 · lights down", sign="🌙", text="*Dim the lights.* / Same time / every night.", size=92,
                      note="Same order, same time: / their body learns *what comes next.*"),
                 dict(label="stop 2 · bath", sign="🛁", text="A warm, / *calm* bath.", size=100,
                      note="Calm, not splash-party. / The day *winds down* here."),
                 dict(label="stop 3 · teeth + pyjamas", sign="🪥", text="*Brush,* pyjamas, / screens *off.*", size=96,
                      note="From here on, everything / is *slow and quiet.*"),
                 dict(label="stop 4 · book", sign="📖", text="*Read together.* / Your lap, / their pick.", size=92,
                      note="The bonding stop: close, calm, your voice. / *The same book 10 times* is fine."),
                 dict(label="stop 5 · bed", sign="💤", text="*Cuddle,* a song, / lights out.", size=96,
                      note="The same goodnight words every night. / *Predictable feels safe.*")],
          do="Tonight, pick your *5 stops* and do them *in the same order.* Same time tomorrow.",
          do_why="In a study of 10,000+ families, more nights with a routine went with *better sleep.*",
          save="send this to the parent who's still up at 9:30 negotiating"),
     "Bedtime battles? Take the calm route.", "follow the route",
     "Bedtime battles? Take the calm route 👉 5 stops, same order, every night.\n\n"
     "🌙 Lights down, same time every night.\n🛁 A warm, calm bath.\n🪥 Teeth, pyjamas, screens off.\n"
     "📖 Read together: your lap, their pick. This is the bonding stop. The same book 10 times is fine.\n"
     "💤 Cuddle, a song, the same goodnight words, lights out.\n\n"
     "Why it works: in a study of more than 10,000 mothers in 14 countries, young children with a bedtime routine every night fell "
     "asleep faster, woke less at night and slept more than an hour longer than children who never had one. The more nights a week, "
     "the better. The American Academy of Pediatrics sums it up as Brush, Book, Bed.\n\n"
     "Do this: tonight, pick your 5 stops and do them in the same order. Same time tomorrow.\n\n"
     f"Send this to the parent who's still up at 9:30 negotiating.\n\n{NOT_MED}\n\n#bedtimeroutine #toddlersleep #bonding #parenting #canadianparents",
     "What's your favourite stop? Sources: Mindell et al. 2015, Sleep, 'Bedtime routines for young children: a dose-dependent association "
     "with sleep outcomes' (10,085 mothers, 14 countries, children up to 6; an association, not proof of cause; AASM release, May 2015). "
     "American Academy of Pediatrics, healthychildren.org, 'Brush, Book, Bed'.")

# ------------------------------------------------------------------ Fully Funded · follow the line · Oct 24 17:00
from ff_math import fv_monthly as _fv  # noqa: E402
_F = {f: round(_fv(300, 35, 0.10 - f), -3) for f in (0.002, 0.01, 0.02)}
FF24_LINES = [
    dict(col="#2B9A66", icon="🟢", start="Index ETF / about 0.2% fee",
         fix=f"About *${_F[0.002]:,.0f}* at 60. Most of your growth *stays yours.*"),
    dict(col="#E8B800", icon="🟡", start="A fund with / a 1% fee",
         fix=f"About *${_F[0.01]:,.0f}.* That 1% quietly took *${_F[0.002] - _F[0.01]:,.0f}.*"),
    dict(col="#E0306C", icon="🔴", start="A fund with / a 2% fee",
         fix=f"About *${_F[0.02]:,.0f}.* The fee took *${_F[0.002] - _F[0.02]:,.0f},* more than / 3 times what you put in."),
]
ifmt("ff-1024-follow-fees", FF, "2026-10-24T17:00",
     dict(kind="follow", field="lite", do_field="cob", pano=5, lines=FF24_LINES,
          hook="Same $300 a month. / *Pick your fee.* / Follow it to 60.",
          mids=[dict(label="the setup", text="*$300 a month,* / age 25 to 60. / Markets grow / *10% a year.* / Only the fee changes."),
                dict(label="how fees work", text="A fee is a % / of *everything* / you've saved, / taken *every year,* / for 35 years."),
                dict(label="why it's huge", text="Every dollar / the fee takes / can't *grow* / for the rest / of the trip.")],
          src="Maths: $300 at the end of each month for 35 years; 10% a year minus the fee; no taxes. Not guaranteed. Returns vary.",
          do="Today, look up your fund's *MER* (search its name + “MER”). Over 1%? Compare a *broad index ETF.*",
          do_why="You can't control the market. *You can control the fee.*",
          save="send this to the friend with “a guy at the bank”"),
     "Same $300 a month. Pick your fee. Follow it to 60.", "pick one · follow its line",
     "Same $300 a month. Pick your fee and follow it to 60 👉\n\n"
     f"🟢 Index ETF, about 0.2% a year: about ${_F[0.002]:,.0f}.\n"
     f"🟡 A fund charging 1%: about ${_F[0.01]:,.0f}.\n"
     f"🔴 A fund charging 2%: about ${_F[0.02]:,.0f}.\n\n"
     f"You put in $126,000 either way. The 2% fee costs about ${_F[0.002] - _F[0.02]:,.0f}, more than 3 times everything you saved.\n\n"
     "Why it's so big: a fee (the MER) is a percentage of your whole balance, taken every year. Every dollar it takes also loses all the "
     "growth it would have earned for the rest of the trip. John Bogle's line says it best: in investing, you get what you don't pay for. "
     "The Simple Path to Wealth makes the same case for low-cost index funds.\n\n"
     "Do this: today, look up your fund's MER (search its name plus \"MER\"). Over 1%? Compare a broad, low-cost index ETF.\n\n"
     f"Send this to the friend with \"a guy at the bank\".\n\n{NG} Education, not advice.\n\n#investingfees #mer #indexfunds #etf #personalfinancecanada",
     "What's your MER? Maths: $300 at the end of each month from 25 to 60 (35 years), 10% a year gross (about the S&P 500's long-run "
     "average) minus 0.2%, 1% or 2%, compounded monthly, no taxes. Fees vary by fund and advice service; some advice is worth paying for. "
     "Ideas from John C. Bogle (Vanguard founder) and JL Collins, The Simple Path to Wealth.")

# ------------------------------------------------------------------ Locked Hour · follow the line · Oct 24 17:00
LH24_LINES = [
    dict(col="#E0306C", icon="🥱", start="It's / boring",
         fix="*Make it a game:* a 25-minute timer and a small treat when it rings."),
    dict(col="#E8B800", icon="🏔️", start="It's / too big",
         fix="Write the *next physical step:* “Open the doc. Type the title.” Do only that."),
    dict(col="#3B3B98", icon="😰", start="I'm scared / it'll be bad",
         fix="Allow a *bad first draft.* Fixing something is easier than starting from nothing."),
]
ifmt("lh-1024-follow-cant-start", LH, "2026-10-24T17:00",
     dict(kind="follow", field="cream", do_field="pink", pano=5, lines=LH24_LINES,
          hook="Can't make / yourself *start?* / Pick your reason.",
          mids=[dict(label="the surprise", text="Putting it off isn't / a *time* problem. / It's a *mood* problem.", size=80),
                dict(label="what's really happening", text="We dodge the / *bad feeling* the task / gives us, not the task. / Researchers call it / *short-term mood repair.*", size=76),
                dict(label="and be kind to yourself", text="Students who *forgave* / themselves for putting / off studying did it / *less* before the / next exam.", size=76)],
          src="Sources: Sirois & Pychyl 2013 · Wohl, Pychyl & Bennett 2010 · Ideas: Getting Things Done, Bird by Bird, the Pomodoro Technique",
          do="Right now, pick the task you're avoiding. *Name the feeling* (bored, overwhelmed, scared), then follow its line for *2 minutes.*",
          do_size=70, do_why="You don't need to feel ready. *You need a first step small enough to take.*",
          save="send this to the friend who cleans the whole house instead of studying"),
     "Can't make yourself start? Pick your reason.", "pick one · follow its line",
     "Can't make yourself start? Pick your reason and follow the line 👉\n\n"
     "🥱 It's boring: make it a game. Set a 25-minute timer (the Pomodoro Technique) and a small treat when it rings.\n"
     "🏔️ It's too big: write the next physical step, like \"Open the doc. Type the title.\" Do only that. (Getting Things Done calls it the next action.)\n"
     "😰 You're scared it'll be bad: allow a bad first draft. Anne Lamott's Bird by Bird made this famous. Fixing beats starting from nothing.\n\n"
     "Why it works: researchers Fuschia Sirois and Tim Pychyl describe procrastination as short-term mood repair. We're not avoiding the "
     "task; we're avoiding the feeling it gives us. So the fix is to change how the first 2 minutes feel, not to buy a new planner.\n\n"
     "And be kind to yourself: in one study, students who forgave themselves for procrastinating before a first exam procrastinated less "
     "before the next one.\n\n"
     "Do this: right now, pick the task you're avoiding. Name the feeling, then follow its line for 2 minutes.\n\n"
     "Send this to the friend who cleans the whole house instead of studying.\n\n#procrastination #focus #studytips #productivity #habits",
     "Which line was yours? Sources: Sirois & Pychyl 2013, Social and Personality Psychology Compass, 'Procrastination and the priority of "
     "short-term mood regulation'. Wohl, Pychyl & Bennett 2010, Personality and Individual Differences (self-forgiveness for procrastinating "
     "reduced later procrastination). Ideas from Getting Things Done (Allen), Bird by Bird (Lamott) and the Pomodoro Technique (Cirillo).")

# ------------------------------------------------------------------ Hourback · staircase climb · Oct 24 17:45 (replaces my hb-1024-follow-settings)
ifmt("hb-1024-climb-5-levels", HB, "2026-10-24T17:45",
     dict(kind="climb", field="plum", do_field="yel", obj="phone", cta="climb the 5 levels →", y_hi=900,
          beats=[dict(text="OpenAI's *5 levels* / on the way to *AGI.* / Climb them.", size=102,
                      note="Reported by Bloomberg, 2024. Here's what / each level *really* looks like."),
                 dict(label="level 1 · chatbots", step="level 1", sign="💬", size=92, text="AI that *talks* / like a person.",
                      note="ChatGPT, November 2022. Great with / words. Weak at *hard reasoning.*"),
                 dict(label="level 2 · reasoners", step="level 2", sign="🧠", size=92, text="AI that *thinks* / before it answers.",
                      note="OpenAI o1, September 2024: it works / step by step *before* replying."),
                 dict(label="level 3 · agents", step="level 3", sign="🤖", size=92, text="AI that *does things* / for you.",
                      note="Claude computer use, ChatGPT agent: / it clicks, types, books. *Shipping now.*"),
                 dict(label="level 4 · innovators", step="level 4", sign="🔬", size=92, text="AI that helps / *discover* new things.",
                      note="Early signs in science: AlphaFold / (protein shapes) shared the *2024 Nobel.*"),
                 dict(label="level 5 · organizations", step="level 5", sign="🏢", size=92, text="AI that runs / *a whole company's* work.",
                      note="Not here. This is the level / people mean by *AGI.*")],
          do="Next time a headline says “AGI,” ask: *which level?* Then check what actually *shipped.*",
          do_why="Levels beat hype. *Know where we really are.*",
          save="send this to the friend who reads every AI headline"),
     "OpenAI's 5 levels on the way to AGI. Climb them.", "climb the 5 levels",
     "OpenAI's 5 levels on the way to AGI. Climb them 👉\n\n"
     "In July 2024, Bloomberg reported that OpenAI uses five levels to track progress toward AGI (OpenAI hasn't published it as an "
     "official framework). What each one looks like in the real world:\n\n"
     "💬 Level 1, chatbots: AI with natural conversation. ChatGPT, November 2022.\n"
     "🧠 Level 2, reasoners: human-level problem solving. OpenAI's o1 (September 2024) was built to think step by step before answering.\n"
     "🤖 Level 3, agents: AI that takes actions for you. Anthropic's computer use (October 2024) and ChatGPT agent (July 2025) click, type "
     "and complete tasks in a browser, asking before anything important.\n"
     "🔬 Level 4, innovators: AI that helps invent and discover. Early signs are in science: Google DeepMind's AlphaFold, which predicts "
     "protein structures, earned Demis Hassabis and John Jumper a share of the 2024 Nobel Prize in Chemistry.\n"
     "🏢 Level 5, organizations: AI that can do all the work of an organization. Not here.\n\n"
     "Why it matters: \"AGI is here\" and \"AI is just autocomplete\" are both lazy. The levels let you place any announcement on the map.\n\n"
     "Do this: next time a headline says AGI, ask which level, then check what actually shipped.\n\n"
     f"Send this to the friend who reads every AI headline.\n\n#ai #agi #openai #aiagents #hourback",
     "Which level surprises you most? Sources: Bloomberg (July 2024), reported via Tom's Guide and others: OpenAI's five levels (chatbots, "
     "reasoners, agents, innovators, organizations), not officially confirmed. OpenAI, 'Introducing OpenAI o1' (Sept 12, 2024); Anthropic, "
     "computer use (Oct 22, 2024); OpenAI, 'Introducing ChatGPT agent' (July 17, 2025); NobelPrize.org, Chemistry 2024 (Hassabis & "
     "Jumper for protein structure prediction; David Baker for protein design).")


# ================================================================== Oct 25
# ------------------------------------------------------------------ Littlefold · hold the dots · Oct 25 17:00
LF25 = [("Never read to", 4662, "words heard from books by age 5", "The study counted a book *every other month.* / That's where some kids start."),
        ("1–2 books a week", 63570, "about 13 times more", "One bedtime story, twice a week. / Already a *different* number."),
        ("3–5 books a week", 169520, "most evenings", "10 minutes on your lap, / most nights. *That's the bonding part.*"),
        ("1 book a day", 296660, "every day, by kindergarten", "Board books first, picture books later. / *Same one again* counts."),
        ("5 books a day", 1483300, "about 1.4 million more words", "Than a child who's never read to. / Before they even *start school.*")]
ifmt("lf-1025-hold-million-words", LF, "2026-10-25T17:00",
     dict(kind="hold", field="cream", do_field="pink", frames=LF25, pre="", post="", cover_obj="ok",
          hook="Words your child / hears from *books* / by age 5. / *Watch it grow.*",
          do="Tonight, read *one book* together. Tomorrow, the same. *The same book again* is fine.",
          do_why="Close, calm, your voice: *the bonding and the words come together.*",
          save="send this to someone building a bedtime routine"),
     "Words your child hears from books by age 5. Watch it grow.", "hold the dots and slide",
     "Hold the dots and slide: the words your child hears from books by age 5 👀\n\n"
     "📕 Never read to: about 4,662 words.\n📗 1–2 books a week: 63,570.\n📘 3–5 a week: 169,520.\n📙 One a day: 296,660.\n"
     "📚 Five a day: 1,483,300. About 1.4 million more words than a child who's never read to.\n\n"
     "That's from researchers at Ohio State, who counted the words in the most-borrowed board books and picture books at their library.\n\n"
     "Why it matters: the words in books are words kids may not hear in everyday talk, and reading is also 10 calm minutes on your lap, "
     "with your full attention. That's bonding and brain-building at the same time.\n\n"
     "Do this: tonight, read one book together. Tomorrow, the same. The same book again is fine.\n\n"
     "Send this to someone building a bedtime routine.\n\n#readaloud #bonding #earlyliteracy #parenting #canadianparents",
     "How many books a day at your house? Source: Logan, Justice, Yumuş, Chaparro-Moreno (2019), Journal of Developmental & Behavioral "
     "Pediatrics, 'When children are not read to at home: the million word gap' (Ohio State News, April 2019): estimates assume one book per "
     "reading session, board books (avg 140 words) to age 3 and picture books (avg 228) to 5; 'never' = a book every other month.")

# ------------------------------------------------------------------ Fully Funded · hold the dots (shrinking) · Oct 25 17:00
FF25 = []
_base = round(fv_monthly(300, 35), -2)
for _a in (25, 27, 29, 31, 33, 35):
    _v = round(fv_monthly(300, 60 - _a), -2)
    _left = _v / _base
    FF25.append((f"Start at {_a}", _v,
                 "the full jar, at 60" if _a == 25 else f"waiting cost ${_base - _v:,.0f}",
                 {25: "*$300 a month* from 25 to 60, / growing 10% a year.",
                  27: f"Those 2 years were *$7,200* of deposits. / They were worth *${_base - _v:,.0f}* at 60.",
                  29: "The earliest dollars grow the longest. / *They're the most valuable ones.*",
                  31: f"6 years late: *{1 - _left:.0%}* of the jar, gone. / Same $300 a month.",
                  33: f"Only *{_left:.0%}* of the jar left. / You'd need *${300 / _left:,.0f} a month* to catch up.",
                  35: f"About *a third* of the jar. / *Only the start date changed.*"}[_a]))
ifmt("ff-1025-hold-cost-of-waiting", FF, "2026-10-25T17:00",
     dict(kind="hold", field="lite", do_field="cob", frames=FF25, cover_obj="hourglass",
          hook="Watch what each / *2-year wait* / costs you at 60.", cta="swipe and watch it shrink →",
          do="Start *this payday,* even at $50. You can raise it later. *You can't get the years back.*",
          do_why="The cheapest money you'll ever invest is *the money you invest first.*",
          save="send this to your “I'll start next year” friend"),
     "$300 a month to 60. Watch what each 2-year wait costs.", "hold the dots and slide",
     "Hold the dots and slide: watch what each 2-year wait costs 👀\n\n"
     f"$300 a month until 60, growing 10% a year:\n"
     + "".join(f"• Start at {lab.split()[-1]}: about ${v:,.0f}\n" for lab, v, *_ in FF25)
     + f"\nWaiting from 25 to 27 skips $7,200 of deposits, and costs about ${_base - FF25[1][1]:,.0f} at 60. Those first dollars have the "
       "most years to grow, so they're the most valuable dollars you'll ever invest.\n\n"
       "Started later? You haven't lost; you just need a bigger monthly amount. The second-best time to start is today.\n\n"
       "Do this: start this payday, even at $50 a month. You can raise it later.\n\n"
       f"Send this to your \"I'll start next year\" friend.\n\n{NG} Education, not advice.\n\n#compoundinterest #investing #startearly #tfsa #personalfinancecanada",
     "What age did you start? Maths: $300 at the end of each month until 60, 10% a year compounded monthly (about the S&P 500's long-run "
     "average), no fees or taxes. Ideas from The Psychology of Money (Housel) and The Wealthy Barber (Chilton).")

# ------------------------------------------------------------------ Locked Hour · staircase climb · Oct 25 17:00
_LH25 = [(1, 1.0)] + [(d, 1.01 ** d) for d in (73, 146, 219, 292, 365)]
ifmt("lh-1025-climb-one-percent", LH, "2026-10-25T17:00",
     dict(kind="climb", field="cream", do_field="pink", obj="hourglass", y_hi=860, cta="climb 1% a day →",
          beats=[dict(text="*1% better* / every day. / Climb the year.", size=112,
                      note="The famous maths from Atomic Habits, / one step every *73 days.*")]
                + [dict(label=f"day {d}", step=f"{v:.1f}×", sign=s, size=96, text=t, note=n)
                   for (d, v), s, t, n in zip(_LH25[1:], ["🌱", "📈", "🔥", "⚡", "🏔️"],
                                              [f"*{_LH25[1][1]:.1f}× better.* / About double.", f"*{_LH25[2][1]:.1f}×.* / Doubled again.",
                                               f"*{_LH25[3][1]:.1f}×.* / Same 1%. / Bigger jump.", f"*{_LH25[4][1]:.1f}×.* / Still just 1% a day.",
                                               f"*{_LH25[5][1]:.0f}× better.* / One year."],
                                              ["1% compounds like interest: / it doubles about every *10 weeks.*",
                                               "Nothing changed in your effort. / *The gains are stacking on gains.*",
                                               "This is why the early days / feel like nothing. *They're the base.*",
                                               "The flip side: *1% worse* a day / leaves you at 0.03× after a year.",
                                               "Real life is lumpier than maths. / The point stays: *small gains stack.*"])],
          do="Pick *one habit.* Tomorrow, do it *1% better:* one more page, one more minute, one less tab.",
          do_why="You don't need a big change. *You need a small one, every day.*",
          save="send this to the friend waiting for a “fresh start”"),
     "1% better every day. Climb the year.", "climb 1% a day",
     "1% better every day. Climb the year 👉\n\n"
     f"Day 73: {_LH25[1][1]:.1f}x. Day 146: {_LH25[2][1]:.1f}x. Day 219: {_LH25[3][1]:.1f}x. Day 292: {_LH25[4][1]:.1f}x. "
     f"Day 365: {_LH25[5][1]:.0f}x.\n\n"
     "That's the famous maths in James Clear's Atomic Habits: 1.01 multiplied by itself 365 times is about 37.8. And the flip side: "
     "0.99 to the 365th is about 0.03. Tiny daily habits decide which way you go.\n\n"
     "Why the climb looks slow, then steep: improvements build on improvements, like compound interest. At 1% a day, you roughly double "
     "every 10 weeks, so the early weeks feel like nothing. That's the base everything else stands on.\n\n"
     "Real life is lumpier than maths, and nobody improves by exactly 1% a day. The lesson stays: small gains, repeated, stack.\n\n"
     "Do this: pick one habit. Tomorrow, do it 1% better: one more page, one more minute, one less tab.\n\n"
     "Send this to the friend waiting for a \"fresh start\".\n\n#atomichabits #1percentbetter #habits #selfimprovement #focus",
     "What's your 1% tomorrow? Maths: 1.01^73 ≈ 2.07, ^146 ≈ 4.28, ^219 ≈ 8.86, ^292 ≈ 18.3, ^365 ≈ 37.8; 0.99^365 ≈ 0.03. An "
     "illustration, not a measurement. Idea from James Clear, Atomic Habits (2018), chapter 1.")

# ------------------------------------------------------------------ Hourback · hold the dots · Oct 25 17:45
HB25 = [("2019", 2, "on METR's trend line", "GPT-2 could finish tasks that take / a person about *2 seconds.*"),
        ("+14 months", 8, "doubled twice", "The length of task AI agents can finish / has doubled about *every 7 months.*"),
        ("+28 months", 32, "doubled twice more", "Measured on real software and research / tasks, timed against *skilled humans.*"),
        ("+42 months", 128, "about 2 minutes", "Still tiny. *This is the part* / people laugh at."),
        ("+56 months", 512, "about 9 minutes", "A small coding fix. / Doubling keeps going."),
        ("+70 months", 2048, "about 34 minutes", "A real chunk of work. / The jar is *suddenly* filling."),
        ("early 2025", 3600, "measured: about 1 hour", "Claude 3.7 Sonnet, METR's study (2025): / *about an hour,* at 50% success.")]
ifmt("hb-1025-hold-task-length", HB, "2026-10-25T17:45",
     dict(kind="hold", field="plum", do_field="yel", frames=HB25, cover_obj="hourglass", vmax=3600,
          show=["2 sec", "8 sec", "32 sec", "2 min", "9 min", "34 min", "~1 hour"],
          hook="How long a task / can *AI finish alone?* / Watch it *double.*",
          do="Track the trend, not the hype: next AI launch, ask *“how long a task can it do on its own?”*",
          do_size=72, do_why="That one question tells you *what it can take off your plate.*",
          save="send this to the friend who thinks AI peaked"),
     "How long a task can AI finish alone? Watch it double.", "hold the dots and slide",
     "Hold the dots and slide: how long a task can AI finish on its own? 👀\n\n"
     "METR, an AI research nonprofit, timed skilled people on software and research tasks, then measured which tasks AI agents could "
     "complete. Their key number is the \"time horizon\": the length of task (in human time) an AI finishes with 50% success.\n\n"
     "In 2019, GPT-2: about 2 seconds. In early 2025, Claude 3.7 Sonnet: about an hour. Over those six years, it doubled roughly every "
     "7 months. The jar shows that trend line, two doublings per swipe.\n\n"
     "Why it matters: doubling looks like nothing for years, then fills the jar fast. METR's own caveats: these are mostly software "
     "tasks, 50% success isn't reliable, and trends can change. Newer models have been measured since; check metr.org for the latest.\n\n"
     "Do this: next AI launch, skip the hype and ask one question: how long a task can it do on its own?\n\n"
     f"Send this to the friend who thinks AI peaked.\n\n#ai #aiagents #futureofwork #metr #hourback",
     "Surprised? Sources: METR, 'Measuring AI Ability to Complete Long Tasks' (Kwa, West et al., March 2025, arXiv 2503.14499): GPT-2 "
     "50% time horizon about 2 seconds; Claude 3.7 Sonnet about one hour; doubling about every 7 months over 6 years. Middle frames are "
     "the doubling trend (2 s × 4 per 14 months), not individual model measurements.")

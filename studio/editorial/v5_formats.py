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
    dict(col="#E0306C", start="My phone keeps / pulling me away",
         fix="Put it in *another room.* Even face-down, it pulls at you."),
    dict(col="#E8B800", start="I can't get / started",
         fix="Write: *“At 7 pm, at the table, I'll start.”*"),
    dict(col="#3B3B98", start="I keep getting / interrupted",
         fix="Before you switch, jot *“Next, I'll…”* Coming back is faster."),
]
fmt("lh-1018-follow-the-line", LH, "2026-10-18T17:00",
    dict(kind="follow", field="cream", do_field="pink", pano=5, lines=LH_LINES,
         hook="Can't focus? / Pick your *problem.*", notes=["keep following…", "two more swipes…", "almost there…"],
         src="Sources: Ward et al. 2017 · Gollwitzer & Sheeran 2006 · Leroy & Glomb 2018",
         do="Tonight, pick *your line* and try its fix tomorrow for one hour.", save="send this to the friend who's “so distracted”"),
    "Can't focus? Pick your problem. Follow its line.", "pick one · follow its line",
    ["Phone, starting, or interruptions: three problems, three lines.", "Keep following your line.", "Two more swipes.",
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
    f"You put in ${300 * 12 * 32:,}. The rest is growth.\n\nWhy it speeds up: your money earns money, then that money earns money too. "
    "That's compounding. Notice how the jar barely moves for years, then jumps.\n\n"
    "Do this: this payday, set up $300 a month, or what you can, into a broad index fund. Then leave it alone.\n\n"
    f"Money Foundations, Part 1 bonus. Save this for payday.\n\n{NG} Education, not advice.\n\n#compounding #investing #indexfunds #personalfinance #moneytips",
    "How old were you when you started investing? Maths: $300 at the end of each month, 10% a year compounded monthly, no fees or taxes.")

# ------------------------------------------------------------------ Littlefold · swipe to reveal (Oct 21 17:00)
LF_VAL = round(fv_monthly(60, 18, 0.08), -2)
fmt("lf-1021-reveal-50-a-month", LF, "2026-10-21T17:00",
    dict(kind="reveal", field="pink", do_field="cream",
         hook="*$50 a month* / from birth to 18. / What does it / *grow into?*",
         guess="guess first!", ans_label="with the 20% grant, at 8% a year", answer=f"${LF_VAL:,.0f}",
         ans_sub=f"You put in *$10,800.* / The rest is grant / and growth.",
         why_label="here's why", why="The government adds *20%* to what you save in an RESP. Then it all grows *for 18 years.*",
         src="Canada Education Savings Grant: 20% on the first $2,500 a year (canada.ca). Growth not guaranteed.",
         do="This week, ask your bank to *open an RESP* and set up *$50 a month.*", save="send this to someone with a new baby"),
    "$50 a month from birth to 18. What does it grow into?", "slide to reveal",
    ["(blurred)", "(less blurred)", "(almost)", "(clearer)", f"About ${LF_VAL:,.0f}. You put in $10,800.",
     "The government adds 20% to RESP savings, then it grows for 18 years.",
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

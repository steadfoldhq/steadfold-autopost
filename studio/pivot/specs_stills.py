"""Pivot (Oct 17) feed posts. One idea each; slide 1 is the thumbnail and must read at 200 px wide in one second.
f = colour field (boldkit.FIELDS). *x* = accent, ' / ' = line break. Detail lives in the caption, not on the tile."""

from ff_math import FIG

FF, HB, LH, LF = "fullyfunded", "hourback", "lockedhour", "littlefold"

POSTS = {
    # ------------------------------------------------------------------ Fully Funded (aggressive, Oct 17 1:15 am)
    # 1 or 3 slides, a 3-5 word hook, ONE hero number. Figures from ff_math.FIG.
    "ff-w03-2-borrow-dont-sell": dict(brand=FF, slides=[
        dict(f="cob", text="The rich / *borrow.*", emo="🏦"),
        dict(f="lite", text="Stocks *sold:*", num="0", num_px=420, sub="They borrow against them."),
        dict(f="coral", text="Stocks fall? / *Lender sells.*", sub="Ask the rate and the sell level first."),
    ]),
    "ff-1017-single-yearly-check": dict(brand=FF, slides=[
        dict(f="cob", text="*5* checks, / once a year.", emo="🔍"),
    ]),
    "ff-w03-3-guardian-will": dict(brand=FF, slides=[
        dict(f="cob", text="Kids? / Name a *guardian.*", emo="📝"),
        dict(f="deep", text="No will? / A *court* decides."),
        dict(f="coral", text="Pick *1* person. / Write it down."),
    ]),
    "ff-1018-single-24-hours": dict(brand=FF, slides=[
        dict(f="coral", text="Want it? / Wait *24 hours.*", emo="⏳"),
    ]),
    "ff-1019-rich-habits-01": dict(brand=FF, slides=[
        dict(f="cob", text="Price ÷ / *uses.*", emo="🧥"),
        dict(f="lite", text="$240 coat, / 120 wears:", num=f"${FIG['coat_a']}", num_px=380),
        dict(f="coral", text="$60 coat, / 6 wears:", num=f"${FIG['coat_b']}", num_px=380, sub="Cheaper tag. 5× the cost."),
    ]),
    "ff-1019-single-average-saver": dict(brand=FF, slides=[
        dict(f="lite", text="Averages / *lie.*", emo="🫠", sub="One big balance skews them."),
    ]),
    "ff-1020-pick-its-home": dict(brand=FF, slides=[
        dict(f="cob", text="Same *$10,000.* / 20 years.", emo="🏠"),
        dict(f="lite", text="Cash at 0%:", num=f"${FIG['home_0']:,}", num_px=280),
        dict(f="coral", text="Invested at 10%:", num=f"${FIG['home_10']:,}", num_px=280, sub="Can fall. Keep cash you'll need soon."),
    ]),
    "ff-1020-single-money-date": dict(brand=FF, slides=[
        dict(f="deep", text="Free hour? / Bring *3 numbers.*", emo="🕐", sub="In. Out. Left."),
    ]),
    # ------------------------------------------------------------------ Hourback
    "hb-w02-7-prove-it": dict(brand=HB, slides=[
        dict(f="indi", text="Make AI / *quote the lease.*", emo="📄"),
        dict(f="yel", kicker="Add this line", text="“Quote the / exact sentence. / Not in it? *Say so.*”", size=104),
        dict(f="plum", text="No matching quote? / *Don't trust it.*", sub="Find every quote in your lease, word for word."),
    ]),
    "hb-1017-single-ai-awards": dict(brand=HB, slides=[
        dict(f="yel", text="Logged off / *by 8?*", emo="🏆", sub="Let AI plan tomorrow. You rest."),
    ]),
    "hb-w02-4-renewal-changes": dict(brand=HB, slides=[
        dict(f="indi", text="Renewal came in? / *Not just the price.*", emo="📬"),
        dict(f="yel", text="Paste last year's / *next to* this year's."),
        dict(f="plum", text="Ask AI: / *list every change.*", sub="Then match each one to the letters."),
    ]),
    "hb-1018-single-before-paste": dict(brand=HB, slides=[
        dict(f="yel", text="Names out / *before you paste.*", emo="✂️", sub="Swap them for [name] and [address]."),
    ]),
    "hb-w02-8-12-automations-kickoff": dict(brand=HB, slides=[
        dict(f="indi", kicker="12 Weeks, 12 Automations · No.1", text="Two calendars. / *One page.*", emo="🗓️"),
        dict(f="yel", text="Paste both. / Ask AI to / *flag the clashes.*"),
        dict(f="plum", text="It found: / *nobody free for / Thursday swim.*", sub="A new automation every Monday, 1 pm ET."),
    ]),
    "hb-1019-single-group-chat": dict(brand=HB, slides=[
        dict(f="indi", text="*47* messages. / Still no plan.", emo="💬"),
    ]),
    # ------------------------------------------------------------------ Littlefold
    "lf-03-safe-sleep-tonight": dict(brand=LF, slides=[
        dict(f="cream", kicker="Safe sleep · tonight", text="Alone. Back. / *Crib.*", emo="🌙"),
        dict(f="pink", text="*Alone:* / nothing in the crib / but baby."),
        dict(f="butter", text="*Back:* every sleep. / Naps too.", sub="In a crib in your room for the first 6 months.",
             src="Public Health Agency of Canada · Canadian Paediatric Society"),
    ]),
    "lf-04-sleep-when-baby-sleeps": dict(brand=LF, slides=[
        dict(f="cream", text="Split / *the night.*", emo="🌙"),
        dict(f="pink", text="You're on / till 2 am. / *Then swap.*"),
        dict(f="berry", text="Off means / *fully off.*", sub="Breastfeeding? Partner brings baby, then settles.",
             src="Public Health Agency of Canada postpartum guide"),
    ]),
    "lf-1018-single-sign-say-it": dict(brand=LF, slides=[
        dict(f="pink", text="How are you, / *really?*", emo="🫶", sub="Low for more than 2 weeks? Tell your doctor or midwife.",
             src="NHS, Postnatal depression"),
    ]),
    "lf-05-partner-week-one": dict(brand=LF, slides=[
        dict(f="cream", kicker="For partners", text="Own *5 jobs* / in week 1.", emo="🧺"),
        dict(f="butter", text="Bring baby / to *every feed.*", sub="Then water and a snack for whoever's feeding."),
        dict(f="pink", text="Take a *night shift.* / Without being asked."),
    ]),
    "lf-1019-single-fever-under-3m": dict(brand=LF, slides=[
        dict(f="pink", text="Under 3 months / with a fever? / *Get seen urgently.*", emo="🌡️",
             src="Canadian Paediatric Society"),
    ]),
    # ------------------------------------------------------------------ Locked Hour
    "lh-1017-single-one-thing-meme": dict(brand=LH, slides=[
        dict(f="cream", text="“Just one thing.” / *40 min later.*", emo="🐇", sub="Keep a “later” list instead."),
    ]),
    "lh-w2-05-restart": dict(brand=LH, slides=[
        dict(f="dots", text="Day 1. / *Again.*", emo="⏰"),
        dict(f="cream", text="Restart *smaller:* / one hour.", sub="Not a whole new routine."),
        dict(f="pink", text="When I sit down / after dinner, / *I start the timer.*"),
    ]),
    "lh-1018-single-finger-down": dict(brand=LH, slides=[
        dict(f="dots", text="Pick a / *start time.*", emo="⏱️", sub="Not “after one more thing.”"),
    ]),
    "lh-w2-08-lockin-kickoff": dict(brand=LH, slides=[
        dict(f="dots", kicker="90-Day Lock-In · Day 1", text="*90 hours* / by Jan 16.", emo="🔒"),
        dict(f="cream", text="One hour. / *Every day.*", sub="Miss one? Never miss twice."),
        dict(f="pink", text="Day 1 is / *today.*", sub="Comment IN to join."),
    ]),
    "lh-1019-single-kitchen-table": dict(brand=LH, slides=[
        dict(f="dots", text="Claim one hour, / *out loud.*", emo="📣", sub="“Locked in 10 to 11. Shout if it's urgent.”"),
    ]),
}

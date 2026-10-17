"""Editorial feed posts (restored approved look, Oct 17). Slide 1 = the cover; slides 2-3 keep their one idea each.

cover keys: lay = pills | sticky | mosaic | line;  text = 4-6 word serif hook (*x* = pill, ' / ' = break);
obj = halftone object (edkit.OBJ, or phone / chat), at = where it sits (tr, bl, br, tl), save = handwritten save-line.
Layouts rotate per page so the grid never shows the same layout twice in a row. No "example" anywhere."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pivot"))
from ff_math import FIG  # noqa: E402

FF, HB, LH, LF = "fullyfunded", "hourback", "lockedhour", "littlefold"

POSTS = {
    # ------------------------------------------------------------------ Fully Funded (Fraunces, cobalt/coral softened)
    "ff-w03-2-borrow-dont-sell": dict(brand=FF, cover=dict(
        lay="pills", f="cob", text="The rich / *borrow.* They / don't *sell.*", obj="point", at="tr",
        save="save this before you sell your investments"), slides=[
        dict(f="lite", text="Stocks *sold:*", num="0", sub="they borrow against them instead"),
        dict(f="coral", text="Stocks fall? / The *lender sells.*", sub="ask the rate + the sell level first"),
    ]),
    "ff-1017-single-yearly-check": dict(brand=FF, cover=dict(
        lay="sticky", f="coral", text="*5 money checks,* / once a year", obj="point", at="bl",
        items=["Fees", "Beneficiaries", "Loan rates", "Insurance cover", "Your freedom number"],
        save="save this for your yearly check")),
    "ff-w03-3-guardian-will": dict(brand=FF, cover=dict(
        lay="pills", f="lite", text="Kids? Name / a *guardian* / in your *will.*", obj="ok", at="bl",
        save="save this if you don't have a will yet"), slides=[
        dict(f="cob", text="No will? / A *court* decides."),
        dict(f="coral", text="Pick *1 person.* / Write it down.", sub="then tell them where the will is"),
    ]),
    "ff-1018-single-24-hours": dict(brand=FF, cover=dict(
        lay="mosaic", f="cob", text="“Want it? / Wait / 24 hours.”", obj="hourglass", at="bl",
        save="save this for your next cart")),
    "ff-1019-rich-habits-01": dict(brand=FF, cover=dict(
        lay="line", f="lite", text="The *cheap* coat / costs *5× more*", obj="ok", at="br",
        dots=[("$240 coat", "120 wears", f"${FIG['coat_a']} a wear"), ("$60 coat", "6 wears", f"${FIG['coat_b']} a wear")],
        save="follow the line: price ÷ uses"), slides=[
        dict(f="cob", text="$240 coat, / 120 wears:", num=f"${FIG['coat_a']}", sub="a wear"),
        dict(f="coral", text="$60 coat, / 6 wears:", num=f"${FIG['coat_b']}", sub="cheaper tag. 5× the cost."),
    ]),
    "ff-1019-single-average-saver": dict(brand=FF, cover=dict(
        lay="pills", f="coral", text="The *average* / saver is / *lying* to you", obj="point", at="tr",
        save="save this before you compare yourself")),
    "ff-1020-pick-its-home": dict(brand=FF, cover=dict(
        lay="pills", f="cob", text="Same / *$10,000.* / Two *homes.*", obj="piggy", at="br",
        save="save this before you park your savings"), slides=[
        dict(f="lite", text="Cash at 0%, / 20 years:", num=f"${FIG['home_0']:,}"),
        dict(f="coral", text="Invested at 10%, / 20 years:", num=f"${FIG['home_10']:,}", sub="can fall. keep cash you need soon"),
    ]),
    "ff-1020-single-money-date": dict(brand=FF, cover=dict(
        lay="sticky", f="lite", text="Free hour? / Have a *money date*", obj="clock", at="br",
        items=["What came in", "What went out", "What's left", "One thing to change"],
        save="clocks go back. use the hour.")),
    # ------------------------------------------------------------------ Hourback (DM Serif Display, periwinkle/peach)
    "hb-w02-7-prove-it": dict(brand=HB, cover=dict(
        lay="pills", f="indi", text="Make AI / *quote* your / *lease* back", obj="point", at="tr",
        save="save this before you trust an AI answer"), slides=[
        dict(f="yel", text="Add one line: / *“Quote the exact / sentence.”*", sub="not in it? it has to say so"),
        dict(f="plum", text="No matching quote? / *Don't trust it.*", sub="find each quote in the lease yourself"),
    ]),
    "hb-1017-single-ai-awards": dict(brand=HB, cover=dict(
        lay="sticky", f="yel", text="The *logged off / by 8* awards", obj="ok", at="bl",
        items=["Took the names out", "Made it quote the source", "Checked the math", "Logged off by 8"],
        save="how many did you get tonight?")),
    "hb-w02-4-renewal-changes": dict(brand=HB, cover=dict(
        lay="pills", f="plum", text="Your renewal / changed *more* / than *the price*", obj="phone", at="br",
        save="save this for your next renewal letter"), slides=[
        dict(f="indi", text="Paste last year's / *next to* this year's."),
        dict(f="yel", text="Ask AI: / *list every change.*", sub="then match each one to the letters"),
    ]),
    "hb-1018-single-before-paste": dict(brand=HB, cover=dict(
        lay="mosaic", f="indi", text="“Take the / names out / first.”", obj="point", at="bl",
        save="save this before you paste anything into AI")),
    "hb-w02-8-12-automations-kickoff": dict(brand=HB, cover=dict(
        lay="pills", f="indi", kicker="12 weeks, 12 automations · no.1", text="Two calendars. / *One page.* / Clashes *flagged.*",
        obj="phone", at="br", save="save this for Sunday night"), slides=[
        dict(f="yel", text="Paste both. / Ask AI to / *flag the clashes.*"),
        dict(f="plum", text="It found: *nobody / free for Thursday / swim.*", sub="a new automation every Monday, 1 pm ET"),
    ]),
    "hb-1019-single-group-chat": dict(brand=HB, cover=dict(
        lay="pills", f="yel", text="*47 messages.* / Still no *plan.*", obj="chat", at="tr",
        save="send this to the group chat that needs it")),
    "hb-1020-prompt-week-01": dict(brand=HB, cover=dict(
        lay="sticky", f="indi", kicker="prompt of the week · no.1", text="5 dinners, / *one list*", obj="point", at="bl",
        items=["5 dinners, 30 min each", "Foods you skip", "Use up the fridge", "One list, by aisle"],
        save="save this for Sunday night"), slides=[
        dict(f="yel", text="Paste / *one prompt.*", sub="the full prompt is in the caption"),
        dict(f="plum", text="Shop / *once.*", sub="check the list against your cupboards"),
    ]),
    "hb-1020-single-stopped-doing": dict(brand=HB, cover=dict(
        lay="pills", f="plum", text="I *stopped* / reading the / *boring bits*", obj="cup", at="bl",
        save="I still check every quote")),
}

# ------------------------------------------------------------------ Littlefold (Fraunces soft, Sherbet) + Locked Hour (Instrument Serif)
# Lifted Oct 17 from the bare pivot tiles. src = source line kept small on the tile (health posts).
POSTS.update({
    "lf-03-safe-sleep-tonight": dict(brand=LF, cover=dict(
        lay="pills", f="cream", kicker="safe sleep · tonight", text="Alone. *Back.* / In a *crib.*", obj="shoe", at="br",
        save="save this for tonight's bedtime"), slides=[
        dict(f="pink", text="*Alone:* nothing / in the crib / but baby."),
        dict(f="butter", text="*Back:* every sleep. / Naps too.", sub="in a crib in your room for the first 6 months",
             src="Public Health Agency of Canada · Canadian Paediatric Society"),
    ]),
    "lf-1017-single-rest": dict(brand=LF, cover=dict(
        lay="mosaic", f="berry", text="“Baby's covered? / Lie down.”", obj="shoe", at="bl", save="the dishes can wait")),
    "lf-04-sleep-when-baby-sleeps": dict(brand=LF, cover=dict(
        lay="sticky", f="pink", text="Split *the night* / in two", obj="shoe", at="br",
        items=["You're on till 2 am", "Then swap", "Off means fully off"], save="save this for week one"), slides=[
        dict(f="butter", text="You're on / till 2 am. / *Then swap.*"),
        dict(f="cream", text="Off means / *fully off.*", sub="breastfeeding? partner brings baby, then settles",
             src="Public Health Agency of Canada postpartum guide"),
    ]),
    "lf-1018-single-sign-say-it": dict(brand=LF, cover=dict(
        lay="pills", f="pink", text="How are you, / *really?*", obj="ok", at="bl",
        save="low for more than 2 weeks? tell your doctor or midwife", src="NHS, Postnatal depression")),
    "lf-05-partner-week-one": dict(brand=LF, cover=dict(
        lay="sticky", f="cream", kicker="for partners", text="Own *5 jobs* / in week 1", obj="point", at="bl",
        items=["Bring baby to every feed", "Take the after-feed", "Take a night shift", "Run the visitors", "Run meals + laundry"],
        save="send this to your partner"), slides=[
        dict(f="butter", text="Bring baby / to *every feed.*", sub="then water and a snack for whoever's feeding"),
        dict(f="pink", text="Take a *night shift.* / Without being asked."),
    ]),
    "lf-1019-single-fever-under-3m": dict(brand=LF, cover=dict(
        lay="pills", f="pink", text="Under 3 months / with a fever? / *Get seen urgently.*", obj="point", at="tr",
        save="save this. send it to your sitter.", src="Canadian Paediatric Society")),
    "lf-06-toddler-meltdown": dict(brand=LF, cover=dict(
        lay="sticky", f="cream", text="Public meltdown? / *Hold your no*", obj="ok", at="bl",
        items=["Calm yourself first", "Keep them safe", "Hold your no", "No treat to stop it"], save="save this for the next grocery run"), slides=[
        dict(f="pink", text="Calm *you* / first.", sub="slow breath. ignore the onlookers."),
        dict(f="butter", text="Treat to stop it? / *Skip it.*", sub="it teaches that tantrums work", src="NHS · American Academy of Pediatrics"),
    ]),
    "lf-1020-single-coat-check": dict(brand=LF, cover=dict(
        lay="pills", f="butter", text="Puffy coat? / *Off* before / *buckling.*", obj="shoe", at="br",
        save="blanket over the straps, never under", src="American Academy of Pediatrics")),
    "lh-1017-one-word-later": dict(brand=LH, cover=dict(
        lay="pills", f="dots", kicker="one word · no.1", text="New thought? / Write it. / *Later.*", obj="clock", at="br",
        save="save this for your next focus hour")),
    "lh-1017-single-one-thing-meme": dict(brand=LH, cover=dict(
        lay="mosaic", f="cream", text="“Just one thing.” / 40 min / later.", obj="hourglass", at="bl", save="keep a “later” list instead")),
    "lh-w2-05-restart": dict(brand=LH, cover=dict(
        lay="sticky", f="pink", text="Day 1. / *Again.*", obj="clock", at="br",
        items=["Restart smaller", "One hour, not a routine", "After dinner: start the timer"], save="save this for the restart"), slides=[
        dict(f="cream", text="Restart *smaller:* / one hour.", sub="not a whole new routine"),
        dict(f="dots", text="When I sit down / after dinner, / *I start the timer.*"),
    ]),
    "lh-1018-single-finger-down": dict(brand=LH, cover=dict(
        lay="pills", f="dots", text="Pick a / *start time.*", obj="point", at="tr", save="not “after one more thing”")),
    "lh-w2-08-lockin-kickoff": dict(brand=LH, cover=dict(
        lay="line", f="cream", text="*90 hours* / by Jan 16", obj="clock", at="br",
        dots=[("Day 1", "today", "1 hour"), ("Day 90", "Jan 16", "90 hours")], save="comment IN to join"), slides=[
        dict(f="pink", text="One hour. / *Every day.*", sub="miss one? never miss twice."),
        dict(f="dots", text="Day 1 is / *today.*", sub="comment IN to join"),
    ]),
    "lh-1019-single-kitchen-table": dict(brand=LH, cover=dict(
        lay="mosaic", f="dots", text="Claim one hour, / out loud.", obj="megaphone", at="bl",
        save="“locked in 10 to 11. shout if it's urgent.”")),
    "lh-w2-07-minute-by-minute": dict(brand=LH, cover=dict(
        lay="sticky", f="dots", text="One hour, / *minute by minute*", obj="clock", at="br",
        items=["0:00 Wi-Fi off, one task", "0:45 stop mid-sentence", "0:50 walk with one question"], save="save this for tomorrow"), slides=[
        dict(f="cream", text="0:00 to 0:45: / *deep work.*", sub="wi-fi off. one task."),
        dict(f="pink", text="0:45: *stop / mid-sentence.*", sub="0:50: walk with one question"),
    ]),
    "lh-1020-single-midterm": dict(brand=LH, cover=dict(
        lay="pills", f="pink", text="Midterm? / Lock *3 hours.*", obj="hourglass", at="bl", save="one topic per hour")),
})

# Story tiles (1080x1920). k = question | newpost | tip | evening. img = the post's NEW cover.
STORIES = {
    "ff-st-1017-1230-newpost": dict(brand=FF, k="newpost", f="coral", text="New post: / the rich *borrow.*", img="ff-w03-2-borrow-dont-sell/01.jpg"),
    "ff-st-1017-1535-tip": dict(brand=FF, k="tip", f="lite", text="Ask your / lender: / *“Best rate?”*", sub="once a year. takes 5 minutes.", obj="point"),
    "ff-st-1017-2105-evening": dict(brand=FF, k="evening", f="cob", text="Save half / *your next raise?*", img="reels/ff-reel-1017-raise-half-cover.jpg", a="Yes", b="Not yet"),
    "ff-st-1018-0750-question": dict(brand=FF, k="question", f="cob", text="Got a *will?*", a="Yes", b="Not yet", obj="ok"),
    "ff-st-1018-1230-newpost": dict(brand=FF, k="newpost", f="lite", text="New post: name / a *guardian.*", img="ff-w03-3-guardian-will/01.jpg"),
    "ff-st-1018-1535-tip": dict(brand=FF, k="tip", f="coral", text="Tell *1 person* / where your / will is.", sub="that's the whole tip.", obj="point"),
    "ff-st-1018-2105-evening": dict(brand=FF, k="evening", f="cob", text="$100 a month / *for a kid?*", img="reels/ff-reel-1018-the-door-cover.jpg", a="Yes", b="Not yet"),
    "ff-st-1019-0750-question": dict(brand=FF, k="question", f="coral", text="Gift list: / *how many?*", a="Under 10", b="10 or more", obj="point"),
    "ff-st-1019-1230-newpost": dict(brand=FF, k="newpost", f="cob", text="New post: / price ÷ *uses.*", img="ff-1019-rich-habits-01/01.jpg"),
    "ff-st-1019-1535-tip": dict(brand=FF, k="tip", f="lite", text="Big buy? / *Price ÷ uses.*", sub="the real price is per wear.", obj="ok"),
    "ff-st-1019-2105-evening": dict(brand=FF, k="evening", f="coral", text="Transfer set / *for payday?*", img="reels/ff-reel-1019-late-start-cover.jpg", a="Done", b="Not yet"),
    "ff-st-1020-0750-question": dict(brand=FF, k="question", f="lite", text="Money talk / *at home?*", a="Easy", b="Awkward", obj="ok"),
    "ff-st-1020-1230-newpost": dict(brand=FF, k="newpost", f="coral", text="New post: same / *$10,000.*", img="ff-1020-pick-its-home/01.jpg"),
    "ff-st-1020-1535-tip": dict(brand=FF, k="tip", f="cob", text="Find *1 rate* / on your / savings.", sub="it's on your statement.", obj="piggy"),
    "ff-st-1020-2105-evening": dict(brand=FF, k="evening", f="lite", text="Money coming? / *Park it first.*", img="reels/ff-reel-1020-windfall-pause-cover.jpg", a="Parked", b="Not yet"),
    # ------------------------------------------------------------------ Hourback Stories
    "hb-st-1017-1330-newpost": dict(brand=HB, k="newpost", f="yel", text="New post: make AI / *quote your lease.*", img="hb-w02-7-prove-it/01.jpg"),
    "hb-st-1017-1545-tip": dict(brand=HB, k="tip", f="indi", text="Add one line: / *“Quote the / line you used.”*", sub="works on any document.", obj="point"),
    "hb-st-1017-2115-evening": dict(brand=HB, k="evening", f="plum", text="Planned tomorrow / *in one prompt?*", img="reels/hb-reel-1017-offline-cover.jpg", a="Yes", b="Not yet"),
    "hb-st-1018-0800-question": dict(brand=HB, k="question", f="indi", text="Do you *check* / AI answers?", a="Every time", b="Sometimes", obj="ok"),
    "hb-st-1018-1330-newpost": dict(brand=HB, k="newpost", f="indi", text="New post: what your / *renewal changed.*", img="hb-w02-4-renewal-changes/01.jpg"),
    "hb-st-1018-1545-tip": dict(brand=HB, k="tip", f="yel", text="After any / summary, ask: / *“What did you / leave out?”*", sub="screenshot this one.", obj="phone"),
    "hb-st-1018-2115-evening": dict(brand=HB, k="evening", f="plum", text="Got the dates / *out of the newsletter?*", img="reels/hb-reel-1018-school-email-cover.jpg", a="Yes", b="Not yet"),
    "hb-st-1019-1": dict(brand=HB, k="question", f="indi", text="Unread emails / *right now?*", opts=["Under 10", "10 to 100", "Don't ask"], obj="point"),
    "hb-st-1019-2": dict(brand=HB, k="tip", f="plum", text="We ran it / *for real.*", sub="255-word email (made up). 3 asks. all 3 quotes matched.", obj="ok"),
    "hb-st-1019-3": dict(brand=HB, k="newpost", f="yel", text="New post: / *47 messages.*", img="hb-1019-single-group-chat/01.jpg"),
    "hb-st-1019-4": dict(brand=HB, k="question", f="plum", text="Your group chat / *plans by…*", opts=["47 messages", "One person books"], obj="chat"),
    "hb-st-1020-1": dict(brand=HB, k="question", f="yel", text="Sorries in your / *last email?*", opts=["0", "1", "4 or more"], obj="point"),
    "hb-st-1020-2": dict(brand=HB, k="tip", f="indi", text="31 words. / *Under 40.*", sub="text made up. reply from a real AI run.", obj="ok"),
    "hb-st-1020-3": dict(brand=HB, k="newpost", f="plum", text="New post: what I / *stopped doing.*", img="hb-1020-single-stopped-doing/01.jpg"),
    "hb-st-1020-4": dict(brand=HB, k="question", f="indi", text="One thing you'd / *stop doing?*", opts=["Reading the renewal", "Rewriting one text", "Something else"], obj="point"),
}

"""Pivot (Oct 17) Reel scripts. One idea each. k = scene kind, f = colour field, drop=True = the payoff on the track's drop.
Money maths is stated directly (standard: MONEY MATHS, DEFINITIVE); the legal line stays in the caption."""

REELS = {
    # ------------------------------------------------------------------ Fully Funded
    "ff-reel-1017am-match": dict(brand="fullyfunded", track="ff-x-money-moves", scenes=[
        dict(k="hook", f="cob", text="Never checked / your *match?*", emo="🙈"),
        dict(k="say", f="lite", text="Pay: *50,000.*"),
        dict(k="say", f="coral", text="They add half, / up to *6%.*"),
        dict(k="say", f="lite", text="Put in 3%: / *+750.*"),
        dict(k="num", f="deep", label="Put in 6%:", value=1500, pre="+", drop=True),
        dict(k="say", f="cob", text="Search *“match”* / in your benefits."),
    ]),
    "ff-reel-1017-raise-half": dict(brand="fullyfunded", track="ff-x-level-up", scenes=[
        dict(k="hook", f="cob", text="Got a raise? / *Save half.*", emo="🎉"),
        dict(k="say", f="lite", text="Raise: *+200* / a month."),
        dict(k="say", f="coral", text="Save 100. / *20 years.*"),
        dict(k="num", f="deep", label="At 6% a year:", value=46204, suf="from 24,000 put in.", drop=True),
        dict(k="say", f="cob", text="Automate it / *day one.*"),
    ]),
    "ff-reel-1018am-lower-rate": dict(brand="fullyfunded", track="ff-x-big-reveal", scenes=[
        dict(k="hook", f="cob", text="One call. / *Lower rate.*", emo="📞"),
        dict(k="say", f="lite", text="5,000 on a card / at *20%:*"),
        dict(k="num", f="coral", label="Interest:", value=1097),
        dict(k="num", f="deep", label="At 16%:", value=861, suf="236 less.", drop=True),
        dict(k="say", f="cob", text="Ask: *“Can you / lower my rate?”*"),
    ]),
    "ff-reel-1018-the-door": dict(brand="fullyfunded", track="ff-x-money-moves", scenes=[
        dict(k="hook", f="cob", text="100 a month. / *From birth.*", emo="🍼"),
        dict(k="say", f="lite", text="Stop at *18.*"),
        dict(k="say", f="coral", text="Never / touch it."),
        dict(k="say", f="lite", text="At 65, at *8%* / a year:"),
        dict(k="num", f="deep", label="It becomes", value=2036000, suf="409,000 in today's money.", size=190, drop=True),
        dict(k="say", f="cob", text="Start small. / *Start early.*"),
    ]),
    "ff-reel-1019am-gift-per-person": dict(brand="fullyfunded", track="ff-x-level-up", scenes=[
        dict(k="hook", f="cob", text="Budget *per person.* / Not per total.", emo="🎁"),
        dict(k="say", f="lite", text="*14* people."),
        dict(k="say", f="coral", text="× 25 *each.*"),
        dict(k="num", f="deep", label="Total:", value=350, pre="= ", suf="Before you shop.", drop=True),
        dict(k="say", f="cob", text="Won't fit? / *Lower the 25.*"),
    ]),
    "ff-reel-1019-late-start": dict(brand="fullyfunded", track="ff-x-big-reveal", scenes=[
        dict(k="hook", f="cob", text="Started at 34? / *Still worth it.*", emo="⏳"),
        dict(k="say", f="lite", text="300 a month / to 65, at *6%:*"),
        dict(k="num", f="coral", label="From 24:", value=638000, size=260),
        dict(k="num", f="deep", label="From 34:", value=323600, suf="Still big.", size=260, drop=True),
        dict(k="say", f="cob", text="Start now. / *Not in 10.*"),
    ]),
    # ------------------------------------------------------------------ Hourback
    "hb-reel-1017am-swap": dict(brand="hourback", track="hb-x-ta-da-funk", scenes=[
        dict(k="hook", f="indi", text="Halfway in. / *No eggs.*", emo="🥚"),
        dict(k="say", f="yel", text="Skip / *the shop.*"),
        dict(k="ai", f="plum", text="Out of eggs. / 2 swaps?"),
        dict(k="list", f="yel", items=["¼ cup *banana*", "¼ cup *yogurt*", "per egg"], drop=True),
        dict(k="say", f="indi", text="Save this for / *the next recipe.*"),
    ]),
    "hb-reel-1017-offline": dict(brand="hourback", track="hb-x-future-easy", scenes=[
        dict(k="hook", f="indi", text="Off work. / *Brain still on?*", emo="🧠"),
        dict(k="say", f="plum", text="Dump it all / into *AI.*"),
        dict(k="ai", f="yel", text="Pick my / 3 must-dos."),
        dict(k="list", f="indi", items=["*Report*", "*Reply Jo*", "*Gym*"], size=140, drop=True),
        dict(k="say", f="plum", text="The rest: *later.* / Laptop shut."),
    ]),
    "hb-reel-1018am-freeze-frame": dict(brand="hourback", track="hb-x-smart-bounce", scenes=[
        dict(k="hook", f="indi", text="*147* unread. / Family chat.", emo="💬"),
        dict(k="say", f="yel", text="Copy it. / *Names out.*"),
        dict(k="ai", f="plum", text="What do I do, / by when?"),
        dict(k="list", f="yel", items=["Dessert · *Sat*", "Pick up Gran · *Sun 2 pm*"], size=104, drop=True),
        dict(k="say", f="indi", text="Check each line. / *Done.*"),
    ]),
    "hb-reel-1018-school-email": dict(brand="hourback", track="hb-x-ta-da-funk", scenes=[
        dict(k="hook", f="indi", text="School newsletter. / *Again.*", emo="📩"),
        dict(k="say", f="plum", text="Dates buried in / *paragraph 6.*"),
        dict(k="ai", f="yel", text="List every date, / earliest first."),
        dict(k="list", f="indi", items=["Thu · *Photo day*", "Fri · *Costumes*"], size=120, drop=True),
        dict(k="say", f="yel", text="Check it. / *Add to calendar.*"),
    ]),
    "hb-reel-1019am-just-the-asks": dict(brand="hourback", track="hb-x-future-easy", scenes=[
        dict(k="hook", f="indi", text="255 words. / *3 asks.*", emo="📧"),
        dict(k="ai", f="plum", text="What do they need / from me?"),
        dict(k="say", f="yel", text="Quote / *each line.*"),
        dict(k="list", f="indi", items=["Move car · *Tue*", "Tag bike · *Fri*", "Party · *optional*"], size=104, drop=True),
        dict(k="say", f="plum", text="All 3 checked / *against the email.*"),
    ]),
    "hb-reel-1019-one-sorry": dict(brand="hourback", track="hb-x-smart-bounce", scenes=[
        dict(k="hook", f="indi", text="4 sorries. / *One email.*", emo="🙇"),
        dict(k="say", f="yel", text="Sorry. Sorry. / Sorry. *Sorry.*"),
        dict(k="ai", f="plum", text="Keep my words. / Apologise once."),
        dict(k="say", f="yel", text="1 sorry. / *Same promise.*", drop=True),
        dict(k="say", f="indi", text="Warm. Short. / *Sent.*"),
    ]),
    # ------------------------------------------------------------------ Littlefold (did not match its best performers)
    "lf-reel-1019-sick-day-plan": dict(brand="littlefold", track="lf-x-tiny-parade", scenes=[
        dict(k="hook", f="cream", text="First cold coming? / *Plan now.*", emo="🤧"),
        dict(k="say", f="pink", text="Under 2s get / up to *10 colds* / a year.", size=150),
        dict(k="say", f="butter", text="Who covers / *day 1?*"),
        dict(k="say", f="berry", text="Who covers / *day 2?*", drop=True),
        dict(k="say", f="cream", text="Name one *backup.* / Ask them / this week.", size=150),
    ]),
}

# ------------------------------------------------------------------ Littlefold + Locked Hour, editorial re-render (Oct 17 pm)
# The seven Reels whose covers were lifted this morning but whose videos still came from the old hand-built scripts.
# Same beats as the old cuts (alt text), tightened so every beat reads at 0.4 s/word + 0.6 s inside 18 s.
REELS.update({
    "lf-reel-1017-one-job": dict(brand="littlefold", track="lf-x-sunny-bounce", scenes=[
        dict(k="hook", f="cream", text="Someone / offers help? / Give *one job.*", emo="🫶"),
        dict(k="say", f="pink", text="*1* Dinner / on Tuesday."),
        dict(k="say", f="butter", text="*2* Fold / one load."),
        dict(k="say", f="berry", text="*3* Hold baby / while I shower.", drop=True),
        dict(k="say", f="cream", text="Then let them / do it *their way.*"),
    ]),
    "lh-reel-1017-one-tab": dict(brand="lockedhour", track="lh-x-tick-boom", scenes=[
        dict(k="hook", f="dots", text="How many / tabs are / *open?*", emo="🔍"),
        dict(k="say", f="cream", text="Close every tab / *but one.*"),
        dict(k="say", f="pink", text="Need it later? / *Jot it down.*"),
        dict(k="say", f="dots", text="One tab. One task. / *One hour.*", drop=True),
        dict(k="say", f="cream", text="Try it / *next hour.*"),
    ]),
    "lf-reel-1018am-3am-windows": dict(brand="littlefold", track="lf-x-sunny-bounce", scenes=[
        dict(k="hook", f="pink", text="3:07 am. / *Up again?*", emo="⏰"),
        dict(k="say", f="cream", text="See the / *lit windows?*"),
        dict(k="say", f="butter", text="Some are parents, / *up like you.*", drop=True),
        dict(k="list", f="berry", items=["At night:", "Lights *low*", "Voice *soft*", "Feed, then *down*"], size=110),
    ]),
    "lh-reel-1018am-pick-3": dict(brand="lockedhour", track="lh-x-lock-in", scenes=[
        dict(k="hook", f="cream", text="Sunday. / *10 minutes.*", emo="⏰"),
        dict(k="say", f="pink", text="Pick *3 things* / for the week."),
        dict(k="list", f="dots", items=["Mon · *Gym*", "Wed · *Report*", "Fri · *Course*"], drop=True),
        dict(k="say", f="cream", text="Like a meeting: / move it, *never delete.*"),
    ]),
    "lf-reel-1018-breathe": dict(brand="littlefold", track="lf-x-giggle-pop", scenes=[
        dict(k="hook", f="butter", text="Crying / won't stop? / *Step away.*", emo="🧺"),
        dict(k="say", f="cream", text="*1* Crib, / on their back.", drop=True),
        dict(k="say", f="pink", text="*2* Step out. / *Breathe.*"),
        dict(k="say", f="berry", text="*3* Go back / when calmer."),
        dict(k="say", f="butter", text="Never shake a baby. / *Call someone in.*"),
    ]),
    "lh-reel-1018-mute-the-world": dict(brand="lockedhour", track="lh-x-phone-down", scenes=[
        dict(k="hook", f="pink", text="Busy / all day. / *Nothing done.*", emo="⏳"),
        dict(k="say", f="cream", text="Lock / *one hour.*"),
        dict(k="list", f="dots", items=["*1* Phone out", "*2* One task", "*3* Door shut"], drop=True),
        dict(k="say", f="pink", text="The world can wait / *an hour.*"),
    ]),
    "lf-reel-1019am-hunger-cues": dict(brand="littlefold", track="lf-x-sunny-bounce", scenes=[
        dict(k="hook", f="pink", text="Crying is / a *late* / hunger sign", emo="🌙"),
        dict(k="say", f="cream", text="Watch for / *the early cues.*"),
        dict(k="list", f="butter", items=["*1* Lip smacking", "*2* Rooting", "*3* Squirming"], drop=True),
        dict(k="say", f="berry", text="Missed them? / *Every parent does.*"),
    ]),
})

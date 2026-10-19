"""Fully Funded content, Oct 18-21. Rewritten to the ONE-READ standard (see /home/claude/one-read-standard.md).
Uses post()/reel()/chain() from specs_teach. Only this page's entries live here."""
from specs_teach import post, reel, chain, FF, HB, LH, LF, NG, NOT_MED, MADE, PRIV, K  # noqa: F401

# ================================================================== Oct 18 · Money Foundations, Part 1: the snowball
reel("ff-reel-1018am-emergency-fund", FF, "2026-10-18T08:15", "deep", "ff-x-big-reveal", "save this before the next surprise bill", [
    dict(k="hook", f="cob", text="Your car breaks down. / The bill is *$1,500.*", emo="🚗"),
    dict(k="say", f="lite", text="With no savings, / that bill goes on / a credit card. / Then it costs you / *interest* every month.", size=112),
    dict(k="because", f="coral", kicker="here's the fix", text="An *emergency fund:* money you keep only for surprises like this.", size=118),
    dict(k="list", f="deep", items=["Start with *1 month*", "of must-pay bills.", "Then build to *3 to 6 months.*"], size=104, drop=True),
    dict(k="do", f="lite", text="Today, open a separate *savings account* and name it *Emergency.*"),
    dict(k="save", f="cob", text="Send this to / the friend with / no backup plan."),
], "Your car breaks down and the bill is $1,500. With no savings, it goes on a credit card, and then it costs you interest every month.\n\n"
   "The fix is an emergency fund: money you keep only for surprises. Start with one month of must-pay bills (rent, food, phone, "
   "transport), then slowly build to 3 to 6 months. Keep it in a separate high-interest savings account, not in investments, so it's "
   "there the day you need it.\n\nDo this today: open a separate savings account and name it Emergency. Even $20 counts.\n\n"
   "Send this to the friend with no backup plan. Money Foundations, Part 1 is in today's post.\n\n"
   "#emergencyfund #personalfinance #moneytips #savingmoney #canadianfinance",
   "Source: CIRO (Canadian Investment Regulatory Organization), \"What is an emergency fund?\": a general guideline is three to six "
   "months of regular living expenses, kept in liquid, low-risk accounts such as high-interest savings. ciro.ca. Education, not advice.")

post("ff-1018-foundations-1-snowball", FF, "2026-10-18T12:00", "learning",
     dict(lay="pills", f="cob", kicker="money foundations · part 1", text="Money that / *makes its own* / *money*", obj="point", at="bl",
          save="slide 5 is the surprising part"),
     [dict(k="say", f="lite", text="When your money earns money, that new money starts earning *too.* / That's called *compounding.*",
           size=118),
      dict(k="why", f="coral", label="it's a snowball",
           text="Think of a snowball rolling downhill. / The *bigger* it gets, the more snow it picks up.", size=118),
      dict(k="say", f="lite", text="Invest *$10,000* at 30. / If it grows 10% a year, the first year earns you about:",
           num=f"${K['snow_y1']:,}", size=96, src="10% a year: the S&P 500's long-run average"),
      dict(k="say", f="cob", text="Leave it alone until 60. / Now it earns this much in *one* year, with nothing added:",
           num=f"${K['snow_y30']:,}", size=96),
      dict(k="say", f="lite", text="Here's the whole snowball. / Most of the growth shows up in the *last 10 years.*", size=104,
           sub="$10,000 at 30, at 10% a year",
           bars=[("30", K["k10_steps"][0], "$10K"), ("40", K["k10_steps"][1], f"${K['k10_steps'][1] // 1000}K"),
                 ("50", K["k10_steps"][2], f"${K['k10_steps'][2] // 1000}K"), ("60", K["k10_steps"][3], f"${K['k10_steps'][3] // 1000}K")]),
      dict(k="say", f="coral", label="the honest part",
           text="Some years, markets drop a lot. / So this is for money you won't need for *10+ years.*", size=112),
      dict(k="do", f="lite", text="Open your banking app and check what your savings earned *last month.* Near $0? Your snowball hasn't started.",
           size=84, save="send this to your “next year” friend")],
     f"Money can make its own money. It's called compounding, and it works like a snowball rolling downhill: the bigger it gets, "
     f"the more snow it picks up.\n\nInvest $10,000 at age 30. If it grows 10% a year, the first year earns you about ${K['snow_y1']:,}. "
     f"Leave it alone until 60, and in that final year it earns about ${K['snow_y30']:,}, with nothing added. "
     f"The whole thing grows to about ${K['k10_10']:,}, and most of that growth shows up in the last 10 years.\n\n"
     f"The honest part: markets drop some years, sometimes a lot. This is for money you won't need for 10+ years. "
     f"Your emergency fund stays in savings.\n\nDo this today: open your banking app and check what your savings earned last month. "
     f"Near $0? Your snowball hasn't started.\n\nMoney Foundations is a series. Part 2 tomorrow: the cheap coat that costs 5 times more.\n\n"
     f"Send this to your \"I'll start next year\" friend. Save it for later.\n\n{NG}\n\n"
     f"#compoundinterest #investing #personalfinance #moneytips #moneyfoundations",
     f"Maths: $10,000 invested at 30, compounded monthly at 10% a year, no fees or taxes. Year 1 interest ≈ ${K['snow_y1']:,}; interest earned "
     f"from age 59 to 60 ≈ ${K['snow_y30']:,}; value at 60 ≈ ${K['k10_10']:,}. Source for 10%: Fidelity, \"S&P 500 average return\": "
     f"\"about 10% since its launch in 1957\" (before inflation). Education, not advice.")

reel("ff-reel-1018-start-28", FF, "2026-10-18T19:00", "deep", "ff-x-money-moves", "save this if you're under 35", [
    dict(k="hook", f="cob", text="Two friends. / Same plan. / *Different* endings.", emo="⏳"),
    dict(k="say", f="lite", text="Maya invests / *$300 a month* / from age 28. / Sam does the same / from *33.*", size=116),
    dict(k="num", f="coral", label="Sam at 60:", value=K["s33_60"], pre="$", suf="at 10% a year", size=220),
    dict(k="num", f="deep", label="Maya at 60:", value=K["s28_60"], pre="$", suf=f"about ${K['s_gap_r']:,} more", size=220, drop=True),
    dict(k="because", f="coral", kicker="the secret?", text=f"Maya only put in *${K['s_in_extra']:,} more.* / Her money just had longer to grow.",
         size=112),
    dict(k="do", f="lite", text="This payday, set up an *automatic monthly transfer* to investing. Any amount counts.", size=96, chars=18),
    dict(k="save", f="cob", text="Send this to / your “I'll start / later” friend.", next="part 2 tomorrow: started late?"),
], f"Two friends, same plan, different endings.\n\nMaya invests $300 a month from 28 to 60. Sam does the same, but starts at 33. "
   f"At 10% a year, Sam ends with about ${K['s33_60']:,}. Maya ends with about ${K['s28_60']:,}.\n\nHere's the secret: Maya only put in "
   f"${K['s_in_extra']:,} more. Her early dollars just had more years to grow, like a snowball that started rolling sooner.\n\n"
   f"Do this: this payday, set up an automatic monthly transfer to your investing account. Any amount counts.\n\n"
   f"Send this to the friend who's \"waiting for a better time.\" Part 2 tomorrow: what if you started late?\n\n{NG}\n\n"
   f"#investing #compoundinterest #personalfinance #moneytips #moneyfoundations",
   "Maths: $300 at the end of each month, compounded monthly at 10% a year, no fees or taxes; 28 to 60 vs 33 to 60. "
   "Source for 10%: Fidelity, \"S&P 500 average return\": about 10% a year since 1957 (before inflation). Maya and Sam are made-up "
   "names for the comparison. Education, not advice.", series="Start early · part 1/2")

chain("ff-ch-1018", FF, "2026-10-18", "ff18", "money foundations · part 1", [
    dict(k="photo", text="“I'll start / investing / *next year.*”", sub="what that year *really* costs →", ink="dark", y=560),
    dict(k="bubbles", f="lite", label="sound familiar?", bubbles=[
        ("in", "is it bad if I wait till next year to invest?"), ("out", "waiting feels free. it isn't."),
        ("out", "money you invest earns money. then *that* money earns money too.")]),
    dict(k="bubbles", f="cob", label="the part nobody tells you", bubbles=[
        ("out", "$10,000 invested at 30, growing 10% a year:"), ("out", f"year one, it earns about *${K['snow_y1']:,}.*"),
        ("out", f"by 60, it earns about *${K['snow_y30']:,}* in ONE year.")], obj="phone"),
    dict(k="payoff", f="coral", label="money that makes money", text="It's called / *compounding.*",
         sub="the earlier it starts, the bigger it gets", obj="piggy"),
    dict(k="handoff", f="lite", text="Money Foundations, / *Part 1*", img="ff-1018-foundations-1-snowball/01.jpg", next="part 2 tomorrow"),
])

# ================================================================== Oct 19 · Part 2: the cheap coat (DEPTH pass, Oct 18 night)
# Facts checked Oct 18 night: PolicyMe "How much is life insurance in Canada?" (rates as of Sept 2026): 20-year term, $500,000,
# non-smoker age 30: about $20/month (women), $28/month (men); whole life, woman 30: about $50/month for $100,000.
# FSRA (Ontario regulator), "Life insurance policy types": term usually has lower premiums and no cash value; group coverage
# "usually terminates when you leave your job". ATB Wealth: most group life is based on one to two times your salary.
# Statistics Canada, Survey of Household Spending 2023: households spent an average of $2,739 on clothing and accessories.
SRC_LIFE = ("Sources: PolicyMe, \"How Much Is Life Insurance in Canada?\" (rates as of September 2026): 20-year term, $500,000, "
            "non-smoker age 30: about $20 a month for women and $28 for men; whole life for a 30-year-old woman: about $50 a month "
            "for $100,000. FSRA (Financial Services Regulatory Authority of Ontario), \"Life insurance policy types\": term "
            "\"usually [has] lower premiums than permanent policies\" and no cash value; group coverage \"usually terminates when you "
            "leave your job\". ATB Wealth, \"Are my group benefits enough?\": \"Most group life insurance policies are based on one to "
            "two times your salary.\" Your own price depends on age, health and smoking. Education, not advice: talk to a licensed "
            "advisor about your needs.")

reel("ff-reel-1019am-term-vs-whole", FF, "2026-10-19T08:15", "deep", "ff-x-level-up", "save this before you buy life insurance", [
    dict(k="hook", f="cob", text="New baby. / New mortgage. / *Which life insurance?*", emo="🛡️"),
    dict(k="say", f="lite", text="*Term life* covers / a set time, like / *20 years.*", size=112),
    dict(k="num", f="deep", label="$500,000 of 20-year / term, woman, 30:", value=20, pre="$", suf="a month, on average",
         size=240, drop=True),
    dict(k="say", f="coral", text="*Whole life* lasts / forever. Same woman: / *$50 a month* buys / just *$100,000.*", size=106),
    dict(k="because", f="coral", kicker="why term fits",
         text="At 30: *big* mortgage, *tiny* kids. By 50: mortgage *paid down,* kids *grown.*", size=100),
    dict(k="do", f="lite", text="Tonight, open your *benefits portal.* Write down your *life insurance* amount.", size=94, chars=18),
    dict(k="save", f="cob", text="Cover the years / people *need* you."),
], "New baby, new mortgage: which life insurance? Here's the difference in plain words.\n\n"
   "TERM LIFE covers you for a set time, like 20 years. If you die in that time, your family gets the full amount. If you don't, "
   "it ends. Average price for a non-smoking 30-year-old, $500,000 for 20 years: about $20 a month for a woman, $28 for a man.\n\n"
   "WHOLE LIFE covers you for your whole life and builds some cash value inside the policy. That costs more: the same 30-year-old "
   "woman pays about $50 a month for just $100,000.\n\n"
   "Why term fits most young families: you need the most cover while the kids are small and the mortgage is big. Every year, the "
   "mortgage shrinks, the kids grow, and your savings grow. A 20- or 25-year term covers exactly those years.\n\n"
   "The part people miss about work coverage: most group life pays 1 to 2 times your salary, and it usually ends when you leave "
   "your job.\n\n"
   "Do this tonight (10 minutes):\n"
   "1. Open your benefits portal (or booklet) and find \"Life insurance\". Write down the amount.\n"
   "2. On paper, add up: your mortgage balance + the years your kids would need your pay.\n"
   "3. Big gap? Get 2 or 3 term quotes for that gap, for as many years as the kids need you. Ask each one: \"Is this price "
   "fixed for the whole term?\"\n\n"
   "The rule to remember: cover the years people need you.\n\n"
   "Send this to your partner.\n\n#lifeinsurance #termlife #newparents #personalfinancecanada #moneyfoundations",
   SRC_LIFE)

post("ff-1019-rich-habits-01", FF, "2026-10-19T12:00", "learning",
     dict(lay="line", f="lite", text="The *cheap* coat / costs *5 times more*", obj="ok", at="br",
          dots=[("$240 coat", "worn 120 times", f"${K['coat_a']} a wear"), ("$60 coat", "worn 6 times", f"${K['coat_b']} a wear")],
          save="money foundations · part 2"),
     [dict(k="say", f="cob", label="sound familiar?", text="A *$60 coat* / on sale. / By February / it's pilling. / *Done after 6 wears.*"),
      dict(k="say", f="lite", text="Your friend paid / *$240* for hers. / She wears it / all winter: / *120 times* in 3 years."),
      dict(k="rows", f="coral", text="What each coat / *really* costs", cap="the price, split over every wear",
           rows=[("Sale coat", f"${K['coat_b']} a wear"), ("Good coat", f"${K['coat_a']} a wear")],
           sub="5 times less, every wear"),
      dict(k="say", f="cob", label="it has a name", text="It's called / *cost per wear.* / The price tag is / today's cost. / "
           "Cost per wear is / the *real* cost."),
      dict(k="why", f="lite", label="why sales fool us", text="A sale shows / what you *save today.* / It hides how soon / "
           "you'll *buy it again.*"),
      dict(k="steps", f="coral", text="The *60-second* check", items=["Guess your uses this year", "Divide the price by that",
                                                                     "Do the same for the cheap one"],
           sub="lower number wins"),
      dict(k="say", f="cob", label="Canada edition", text="Canadian households / spent *$2,739* / on clothes in 2023. / "
           "Wear things *twice as long,* / buy *half as often.*", src="Statistics Canada, Survey of Household Spending 2023"),
      dict(k="say", f="coral", label="the honest part", text="Pricey isn't always / better. A $240 coat / that never leaves / "
           "the closet is / *$240 a wear.*"),
      dict(k="do", f="lite", text="Before any buy over *$50,* divide the price by *uses this year.* Lower wins. Unsure? *Wait 48 hours.*",
           size=92, save="send this to your sale-loving friend")],
     f"The cheap coat can cost you 5 times more.\n\n"
     f"You buy a $60 coat on sale. By February it's pilling, and you're done after 6 wears. That's ${K['coat_b']} every time you "
     f"put it on. Your friend paid $240 for hers and wears it all winter: 120 times in 3 years. That's ${K['coat_a']} a wear.\n\n"
     f"It's called cost per wear. The price tag is today's cost. Cost per wear is the real cost.\n\n"
     f"Why sales fool us: a sale shows what you save today. It hides how soon you'll buy it again.\n\n"
     f"The 60-second check, before any buy over $50:\n"
     f"1. Guess honestly how many times you'll use it this year (look at how often you used the last one).\n"
     f"2. Divide the price by that number.\n"
     f"3. Do the same for the cheaper option. The lower number wins.\n"
     f"Still unsure? Put it in your cart and wait 48 hours. If you've forgotten about it, you didn't need it.\n\n"
     f"Canada edition: households spent an average of $2,739 on clothing and accessories in 2023 (Statistics Canada). Wear "
     f"things twice as long and you buy them half as often.\n\n"
     f"The honest part: pricey isn't always better. Check the seams, the reviews and the return policy. A $240 coat that never "
     f"leaves the closet is $240 a wear.\n\n"
     f"Money Foundations, Part 2. Part 3 tomorrow: index funds, in plain words.\n\n"
     f"Send this to your sale-loving friend. Save it for your next shopping trip.\n\n"
     f"#moneytips #budgeting #personalfinancecanada #costperwear #moneyfoundations",
     f"Maths: price divided by times used. $240 ÷ 120 = ${K['coat_a']}. $60 ÷ 6 = ${K['coat_b']}. $10 is 5 times $2. Count your own "
     f"uses: they will differ. Canada figure: Statistics Canada, The Daily, May 21, 2025, Survey of Household Spending 2023: "
     f"\"households spent an average of $2,739 on clothing and accessories\". Story quiz: Ellen MacArthur Foundation, A New "
     f"Textiles Economy (2017): the average number of times a garment is worn has fallen 36% compared with 15 years earlier.")

reel("ff-reel-1019-late-start", FF, "2026-10-19T19:00", "deep", "ff-x-big-reveal", "save this if you feel behind", [
    dict(k="hook", f="cob", text="Started at 33? / *You can* / *catch up.*", emo="⏳"),
    dict(k="say", f="lite", text=f"Friend: *$300 a month* / from 28. At 60: / *${K['s28_60']:,}.*", size=108),
    dict(k="say", f="coral", text=f"You: same $300, / from 33. At 60: / *${K['s33_60']:,}.*", size=108),
    dict(k="because", f="deep", kicker="why so big?", text="Her first dollars grew the *longest.*", size=116),
    dict(k="num", f="lite", label="Fix 1: invest", value=K["catch_pmt"], pre="$", suf="a month from 33, not $300",
         size=260, drop=True),
    dict(k="say", f="cob", text=f"Fix 2: keep $300, / invest until *65.* / Same *${K['s28_60']:,}.*", size=108),
    dict(k="do", f="lite", text="This payday, raise your *TFSA auto-transfer* by *$25.*", size=94, chars=18),
    dict(k="save", f="coral", text="Late? Pay a bit more, / or go a bit longer."),
], f"Started investing at 33, not 28? You can catch up. Here's exactly how.\n\n"
   f"Your friend invests $300 a month from 28. At 10% a year, by 60 that's about ${K['s28_60']:,}.\n"
   f"You invest the same $300 a month, but from 33. By 60: about ${K['s33_60']:,}.\n\n"
   f"Why the gap is so big: her first 5 years of deposits had the longest to grow. Like a snowball that started rolling sooner.\n\n"
   f"Two ways to catch up:\n"
   f"1. Invest about ${K['catch_pmt']} a month instead of $300, until 60. That's ${K['catch_pmt'] * 12:,} a year, which fits inside "
   f"one year's TFSA room ($7,000 in 2026).\n"
   f"2. Keep $300 a month and keep investing until 65. You land at about the same ${K['s28_60']:,}.\n"
   f"Or mix them: a bit more each month, a couple of years longer.\n\n"
   f"Do this, this payday (5 minutes):\n"
   f"1. Open your bank app and go to Transfers, then Scheduled or Recurring transfers.\n"
   f"2. Find the automatic transfer into your TFSA (no transfer yet? set one up for payday).\n"
   f"3. Raise it by $25. Every time you get a raise, raise it again.\n\n"
   f"The rule to remember: start 5 years late, and you either pay a bit more or go 5 years longer.\n\n"
   f"Send this to the friend who thinks it's too late. Part 2 of 2.\n\n{NG}\n\n"
   f"#investing #TFSA #personalfinancecanada #retirement #moneyfoundations",
   f"Maths: $300 at the end of each month, compounded monthly at 10% a year, no fees or taxes: 28 to 60 ≈ ${K['s28_60']:,}; "
   f"33 to 60 ≈ ${K['s33_60']:,}; 33 to 65 ≈ ${K['s28_60']:,} (the same 32 years of deposits). ${K['catch_pmt']} a month from 33 to "
   f"60 reaches the same total as $300 from 28. Source for 10%: Fidelity, \"S&P 500 average return\": about 10% a year since 1957 "
   f"(before inflation). TFSA limit 2026: $7,000 (CRA). Education, not advice.", series="Start early · part 2/2")

chain("ff-ch-1019", FF, "2026-10-19", "ff19", "money foundations · part 2", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="lite", label="quick quiz", title="Each piece of clothing: / worn *more* or *less?*", bubbles=[
        ("in", "2015 vs 2000, on average…"), ("out", "A) about the same"), ("out", "B) about a third less")],
         tap="guess, then tap →"),
    dict(k="payoff", f="coral", label="the answer: B", text="*36%* / fewer", sub="wears per piece, 2000 to 2015", obj="ok",
         tap="source: Ellen MacArthur Foundation, 2017 · tap →"),
    dict(k="bubbles", f="cob", label="what that costs you", bubbles=[
        ("out", "Canadian households spent *$2,739* on clothes in 2023."),
        ("out", "fewer wears means you pay it *again, sooner.*"),
        ("in", "so how do I check before I buy?")], obj="phone", tap="source: Statistics Canada · tap →"),
    dict(k="payoff", f="lite", label="the 60-second check", text="Price, divided / by *uses this year*",
         sub="do it for the cheap one too. lower wins.", obj="piggy", tap="next story →"),
    dict(k="handoff", f="cob", text="The *cheap* coat / costs *5 times more*", img="ff-1019-rich-habits-01/01.jpg", next="part 3 tomorrow"),
])


# ================================================================== Oct 20 · Part 3: index funds
reel("ff-reel-1020am-tfsa-rrsp", FF, "2026-10-20T08:15", "deep", "ff-x-level-up", "save this for tax season", [
    dict(k="hook", f="cob", text="TFSA or RRSP? / Here's the / *simple* difference.", emo="🇨🇦"),
    dict(k="say", f="lite", text="An *RRSP* saves you / tax now. You pay it / later, when you / take money out.", size=106),
    dict(k="say", f="coral", text="A *TFSA* is the / opposite. No tax / break now, but no tax / on the growth, ever.", size=106),
    dict(k="because", f="deep", kicker="so which one?",
         text="Higher tax rate now than in retirement? The RRSP often wins. If not, the TFSA.", size=96, drop=True),
    dict(k="do", f="lite", text="Tonight, check your TFSA and RRSP room in your *CRA account.*", size=96, chars=18),
    dict(k="save", f="cob", text="Send this to / the friend who asks / every tax season."),
], "TFSA or RRSP? Here's the simple difference.\n\nAn RRSP saves you tax now: what you put in can lower your taxes this year. You pay "
   "the tax later, when you take the money out.\n\nA TFSA is the opposite. No tax break when you put money in, but you never pay tax on "
   "the growth or when you take it out.\n\nSo which one? If your tax rate is higher now than it will be in retirement, the RRSP often wins. "
   "If not, the TFSA often does. Plenty of people use both.\n\nDo this tonight: log in to your CRA My Account and check your TFSA "
   "room and RRSP limit.\n\nSend this to the friend who asks every tax season.\n\n"
   "#TFSA #RRSP #canadianfinance #personalfinance #moneyfoundations",
   "Source: CIBC, \"Should you contribute to your TFSA or your RRSP?\": RRSP contributions may be tax-deductible and withdrawals are "
   "taxable; TFSA contributions are not deductible and withdrawals are tax-free if you follow the rules. Your TFSA contribution room and "
   "RRSP deduction limit are shown in CRA My Account (canada.ca). Education, not tax advice.")

post("ff-1020-foundations-3-index-funds", FF, "2026-10-20T12:00", "learning",
     dict(lay="pills", f="coral", kicker="money foundations · part 3", text="Own a tiny piece / of *500 companies*", obj="point", at="bl",
          save="index funds, in plain words"),
     [dict(k="say", f="lite", label="picking stocks is hard", text="In 2025, about / *8 in 10* pro funds / did worse than / the market.",
           size=124, src="S&P Dow Jones Indices, SPIVA U.S. Year-End 2025 (large-cap funds)"),
      dict(k="say", f="cob", label="the other way", text="An *index fund* / buys a bit of / *everything.*",
           size=130, sub="no guessing needed"),
      dict(k="why", f="lite", label="think of a fruit basket", text="Don't bet on / one apple. / Buy the *whole* / *basket.*",
           size=130, sub="one bad apple barely matters"),
      dict(k="say", f="coral", text="Since 1957, the / S&P 500 grew, / on average:", num="10%", size=116, sub="a year, before inflation",
           src="Fidelity, S&P 500 average return, before inflation"),
      dict(k="say", f="lite", label="the honest part", text="Some years / it drops hard. / In 2008, it / fell about *37%.*", size=120,
           sub="so leave it alone for years"),
      dict(k="do", f="cob", text="Open your investing app and search *“S&P 500 index fund.”* Just look today.",
           size=100, save="send this to the friend who picks stocks")],
     "Picking the winning stock is hard. In 2025, about 8 in 10 professional US big-company funds did worse than the S&P 500.\n\n"
     "An index fund skips the guessing. It buys a little of every company on a list, like the 500 big US companies in the S&P 500. "
     "Think of a fruit basket: instead of betting on one apple, you buy the whole basket, so one bad apple barely matters.\n\n"
     "Since 1957, the S&P 500 has grown about 10% a year on average. The honest part: some years it drops hard. In 2008 it fell about 37%. "
     "Index funds work best when you leave them alone for years.\n\nDo this: open your investing app and search \"S&P 500 index fund.\" "
     f"Just look. No need to buy today.\n\nMoney Foundations, Part 3. Part 4 tomorrow: free money for your kid's education.\n\n"
     f"Send this to the friend who picks stocks.\n\n{NG}\n\n#indexfunds #investing #personalfinance #moneyfoundations #canadianfinance",
     "Sources: S&P Dow Jones Indices, SPIVA U.S. Year-End 2025: 79% of active large-cap U.S. equity funds underperformed the S&P 500 in "
     "2025. Fidelity, \"S&P 500 average return\": about 10% a year since 1957 (before inflation). S&P 500 total return in 2008: about -37% "
     "(S&P Dow Jones Indices). Education, not advice.")

reel("ff-reel-1020-wills", FF, "2026-10-20T19:00", "deep", "ff-x-money-moves", "save this and talk about it tonight", [
    dict(k="hook", f="cob", text="Not married? / No will? Your / partner may get / *nothing.*", emo="📝"),
    dict(k="say", f="lite", text="In Ontario, if you / die without a will, / the law decides who / gets your things.", size=112),
    dict(k="because", f="coral", kicker="here's the shock", text="Those rules give *nothing* to a common-law partner, even after years together.",
         size=108, drop=True),
    dict(k="do", f="lite", text="This week, find a *wills lawyer* near you and book a first call. Do it together.", size=96, chars=18),
    dict(k="save", f="cob", text="Send this to / your partner. / Tonight."),
], "Not married? No will? Your partner may get nothing.\n\nIn Ontario, if you die without a will, the law decides who gets your things. "
   "Those rules give nothing to a common-law partner, even after years together. Other provinces have their own rules, so check yours.\n\n"
   "A will is how you decide, not the law.\n\nDo this: this week, find a wills lawyer near you and book a first call. Do it together.\n\n"
   "Send this to your partner. Tonight.\n\n#wills #estateplanning #commonlaw #personalfinance #moneyfoundations",
   "Source: Steps to Justice (CLEO, Community Legal Education Ontario): under Ontario's intestacy rules, \"The intestacy rules give "
   "nothing to a common-law partner\" (a partner may be able to make other claims in court). stepstojustice.ca. Rules differ by province. "
   "General information, not legal advice.")

chain("ff-ch-1020", FF, "2026-10-20", "ff20", "money foundations · part 3", [
    dict(k="photo", text="“I don't know / which stocks / *to pick.*”", sub="good news: you *don't have to* →", ink="light", y=760),
    dict(k="bubbles", f="lite", label="sound familiar?", bubbles=[
        ("in", "everyone at work talks stocks. I have no clue 😅"), ("out", "you don't have to pick one."),
        ("out", "you can buy a little of *all of them.*")]),
    dict(k="bubbles", f="cob", label="here's how", bubbles=[
        ("out", "an *index fund* buys a little of every company on a list."),
        ("out", "like the S&P 500: 500 big US companies.")], obj="phone"),
    dict(k="payoff", f="coral", label="since 1957, on average", text="about / *10% a year*",
         sub="not every year. some years it drops.", obj="piggy"),
    dict(k="handoff", f="lite", text="Money Foundations, / *Part 3*", img="ff-1020-foundations-3-index-funds/01.jpg", next="part 4 tomorrow"),
])


# ================================================================== Oct 21 · Part 4: the Canada Learning Bond
post("ff-1021-clb-who-qualifies", FF, "2026-10-21T12:00", "learning",
     dict(lay="pills", f="coral", kicker="money foundations · part 4", text="Free *$2,000* / for your kid's / *education*", obj="point", at="bl",
          save="check if you qualify on slide 4"),
     [dict(k="say", f="lite", label="sound too good?", text="The government / can put up to / *$2,000* toward / your kid's school.",
           size=124, sub="and you add $0"),
      dict(k="say", f="cob", label="the Canada Learning Bond", text="*$500* to start. / *$100* more / each year. / Up to $2,000.", size=124),
      dict(k="rows", f="lite", text="Who *qualifies*", cap="family net income, July 2026 to June 2027",
           rows=[("1 to 3 kids", "$58,523 or less"), ("4 kids", "under $66,036"), ("5 kids", "under $73,577")],
           sub="kids born in 2004 or later", src="canada.ca · ESDC notice 2026-1138 · limits change each July"),
      dict(k="say", f="coral", label="the part nobody mentions", text="It only lands / in an *RESP:* / a savings account / for school.",
           size=124),
      dict(k="say", f="cob", label="you're not alone", text="In 2022, / *2.5 million* / eligible kids / never got it.",
           size=124, src="C.D. Howe Institute, using ESDC 2022 data"),
      dict(k="say", f="lite", label="good news", text="You can still / apply until your / child turns *21.*", size=128,
           src="canada.ca · Canada Learning Bond"),
      dict(k="do", f="cob", text="This week, ask your bank for an *RESP with the Learning Bond.* Bring your child's SIN.",
           size=100, save="send this to a new parent")],
     "The government will put up to $2,000 toward your child's education, and you don't have to add a dollar.\n\n"
     "It's called the Canada Learning Bond. It starts with $500, then adds $100 every year, up to $2,000.\n\n"
     "Who qualifies (July 2026 to June 2027): kids born in 2004 or later, in families with net income of $58,523 or less for 1 to 3 kids, "
     "under $66,036 for 4 kids, or under $73,577 for 5 kids. The limits change each July.\n\nThe part nobody mentions: the money only lands "
     "in an RESP, a savings account for school. Many banks open one for free. In 2022, about 2.5 million eligible kids had never received it. "
     "Didn't apply when they were a baby? You can still apply until your child turns 21.\n\n"
     "Do this: this week, ask your bank to open an RESP with the Canada Learning Bond. Bring your child's SIN.\n\n"
     "Money Foundations, Part 4. Send this to a new parent.\n\n#RESP #canadalearningbond #parenting #canadianfinance #moneyfoundations",
     "Sources: canada.ca (CRA), Canada Learning Bond: up to $2,000; $500 for the first eligible year plus $100 for each additional year "
     "up to age 15; children born in 2004 or later; personal contributions are not required; the beneficiary must be under 21 when applying. "
     "Income limits: ESDC notice 2026-1138, July 1, 2026 to June 30, 2027 (adjusted family net income). Take-up: Godbout & Samoisette, "
     "C.D. Howe Institute, \"On Its Anniversary, Has the Goal of the Canada Learning Bond Been Achieved?\", citing ESDC's 2022 Canada "
     "Education Savings Program statistical review: take-up rose from 29.1% (2013) to 42.5% (2022); 2.5 million of 4.4 million eligible "
     "children had not received it.")

chain("ff-ch-1021", FF, "2026-10-21", "ff21", "money foundations · part 4", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="lite", label="quick quiz", title="A *free $2,000* / for kids' school…", bubbles=[
        ("in", "how many eligible kids never got it?"), ("out", "A) about 250,000"), ("out", "B) about 2.5 million")],
         tap="guess, then tap →"),
    dict(k="payoff", f="coral", label="the answer: B", text="*2.5 million*", sub="eligible kids, never paid (2022)", obj="ok",
         tap="source: C.D. Howe Institute, ESDC data · tap →"),
    dict(k="payoff", f="cob", label="why it matters", text="No RESP, / *no bond.*", sub="the money only lands in an RESP", obj="piggy",
         tap="next story →"),
    dict(k="handoff", f="lite", text="Free *$2,000* / for your kid", img="ff-1021-clb-who-qualifies/01.jpg", next="save it for your bank visit"),
])


# ================================================================== Oct 22 · Part 5: the RRSP refund (Story chain day)
# Facts checked Oct 18: Ontario 2026 combined marginal rate 29.65% on taxable income $58,523-$94,907 (Richter, 2026 Ontario
# income tax tables). 2026 RRSP contributions count if made by March 1, 2027 (first 60 days of 2027, CRA).
REFUND = int(round(5000 * 0.2965 / 10) * 10)                      # 1,480
REFUND_60 = int((REFUND * (1 + 0.10 / 12) ** 360) // 1000 * 1000)  # 29,000 (rounded down)
assert (REFUND, REFUND_60) == (1480, 29000), (REFUND, REFUND_60)
SRC_REFUND = ("Sources: Richter, \"2026 Ontario Income Tax Tables\": combined federal + Ontario marginal rate of 29.65% on taxable "
              "income from $58,523 to $94,907 (2026). So a $5,000 RRSP deduction at $80,000 of income lowers tax by about $1,480. "
              "CRA (canada.ca), RRSPs: contributions are deductible, and withdrawals are taxed as income; contributions made in the "
              "first 60 days of 2027 (by March 1, 2027) can be deducted on your 2026 return. Your RRSP deduction limit is on your "
              "notice of assessment and in CRA My Account. Education, not tax advice.")

reel("ff-reel-1022-refund-29k", FF, "2026-10-22T19:00", "deep", "ff-x-big-reveal", "save this for refund day", [
    dict(k="hook", f="cob", text="Spend the refund, / or turn it into / *$29,000?*", emo="💸"),
    dict(k="say", f="lite", text=f"An RRSP refund / of *${REFUND:,}* / feels like / a little bonus.", size=112),
    dict(k="because", f="coral", kicker="the part nobody tells you",
         text="Invest it at 30, growing *10% a year,* and leave it alone until 60.", size=110),
    dict(k="num", f="deep", label="by age 60:", value=REFUND_60, pre="$", suf="from one refund", size=220, drop=True),
    dict(k="do", f="lite", text="When the refund lands, move it into your *TFSA* that same day.", size=96, chars=18),
    dict(k="save", f="cob", text="Send this to / the friend planning / a refund trip."),
], f"Spend the refund, or turn it into $29,000?\n\nPut $5,000 in an RRSP while earning $80,000 in Ontario, and your tax drops by "
   f"about ${REFUND:,}. It feels like a little bonus.\n\nHere's the part nobody tells you: invest that ${REFUND:,} at 30, let it grow 10% "
   f"a year, and leave it alone. By 60 it's about ${REFUND_60:,}. One refund. Like a snowball, it just needs time.\n\n"
   f"Do this: when the refund lands, move it into your TFSA that same day, before it disappears into everyday spending.\n\n"
   f"Send this to the friend planning a refund trip.\n\n{NG}\n\n#RRSP #taxrefund #TFSA #canadianfinance #moneyfoundations",
   SRC_REFUND + f" Maths: ${REFUND:,} invested at 30, compounded monthly at 10% a year for 30 years, no fees or taxes ≈ $29,400 "
   "(shown rounded down). 10% = the S&P 500's long-run average (Fidelity), before inflation.",
   series="RRSP refund · part 2/2")


post("ff-1022-rrsp-refund", FF, "2026-10-22T12:00", "learning",
     dict(lay="pills", f="coral", kicker="money foundations · part 5", text="Your RRSP refund / isn't a *bonus*", obj="point", at="bl",
          save="here's where it comes from"),
     [dict(k="say", f="lite", label="earn $80,000 in Ontario?", text="Put *$5,000* / in an RRSP. / Your tax drops / by about:",
           num=f"${REFUND:,}", src="2026 Ontario combined rate: 29.65% · Richter 2026 tax tables"),
      dict(k="say", f="cob", label="the part nobody tells you", text="It's *your own tax,* / coming back. / You pay it when / you *take it out.*",
           sub="a head start, not a gift"),
      dict(k="do", f="lite", text="Before *March 1, 2027,* check your RRSP limit in *CRA My Account.*",
           size=96, save="send this to the friend who spends the refund")],
     f"Your RRSP refund isn't a bonus. Here's where it comes from.\n\n"
     f"Earn $80,000 in Ontario and put $5,000 in an RRSP, and your tax for the year drops by about ${REFUND:,}. Your job already "
     f"took tax off every paycheque, so the CRA sends the extra back as a refund.\n\n"
     f"The part nobody tells you: it's your own tax, coming back. You pay tax on that money later, when you take it out, ideally in "
     f"retirement when your income (and tax rate) is lower. So the refund is a head start, not a gift.\n\n"
     f"Do this: before March 1, 2027 (the deadline for your 2026 taxes), check your RRSP limit in CRA My Account.\n\n"
     f"Money Foundations, Part 5. Tonight at 7: what one refund can grow into.\n\n"
     f"Send this to the friend who spends the refund.\n\n#RRSP #taxrefund #canadianfinance #personaltax #moneyfoundations",
     SRC_REFUND)

chain("ff-ch-1022", FF, "2026-10-22", "ff22", "money foundations · part 5", [
    dict(k="photo", text="“Refund's in. / *Trip time!*”", sub="wait, where did it *come from?* →", ink="dark", y=930),
    dict(k="bubbles", f="lite", label="sound familiar?", bubbles=[
        ("in", f"got ${REFUND:,} back from my RRSP 🎉"), ("out", "nice! but it's not free money."),
        ("out", "it's *your own tax,* coming back.")]),
    dict(k="bubbles", f="cob", label="here's how", bubbles=[
        ("out", "your job already took tax off every paycheque."),
        ("out", "the RRSP lowered your tax bill, so the CRA *sends the extra back.*")], obj="phone"),
    dict(k="payoff", f="coral", label="and later?", text="You pay it / *when you* / *take it out.*",
         sub="a head start, not a bonus", obj="piggy"),
    dict(k="handoff", f="lite", text="Your RRSP refund / isn't a *bonus*", img="ff-1022-rrsp-refund/01.jpg", next="part 2 tonight at 7"),
])


# ================================================================== Oct 23 · Part 6: CPP (day B: Reels carry it, Story = quiz)
# Facts checked Oct 18 on canada.ca: average new CPP retirement pension at 65 $858.34/month; 2026 maximum at 65 $1,507.65;
# 0.6% less per month before 65 (36% at 60), 0.7% more per month after 65 (42% at 70).
CPP_MAX = 1507.65
CPP_70 = int(CPP_MAX * 1.42 // 10 * 10)  # 2,140
assert CPP_70 == 2140
SRC_CPP = ("Sources (canada.ca): Canada Pension Plan, Pensions and benefits monthly amounts: retirement pension at 65, average for "
           "new beneficiaries $858.34 a month, 2026 maximum $1,507.65 a month. When to start your pension: payments decrease 0.6% each "
           "month before 65 (up to 36% at 60) and increase 0.7% each month after 65 (up to 42% at 70). The CPP is designed to replace "
           "part of your earnings, not all of them. Education, not advice.")

post("ff-1023-cpp-enough", FF, "2026-10-23T12:00", "learning",
     dict(lay="pills", f="cob", kicker="money foundations · part 6", text="Will CPP / *pay your bills?*", obj="point", at="bl",
          save="the real number: slide 2"),
     [dict(k="say", f="lite", label="canada.ca, 2026", text="The average new / CPP pension / at 65 is about:", num="$858",
           sub="a month. the most is about $1,508", src="canada.ca, CPP monthly amounts"),
      dict(k="say", f="coral", label="the part nobody tells you", text="CPP replaces / *part* of your pay, / not all of it. / *Your savings* / fill the gap."),
      dict(k="do", f="cob", text="This payday, set up *$50 a month* into your TFSA. That's your gap-filler.",
           size=96, save="send this to the friend counting on CPP")],
     "Will CPP pay your bills? Here's the real number.\n\n"
     "The average new CPP pension at 65 is about $858 a month (canada.ca, 2026). The most anyone can get at 65 is about $1,508.\n\n"
     "The part nobody tells you: CPP was built to replace part of your pay, not all of it. Think of it as the floor of your house, not "
     "the whole house. Your own savings, like a TFSA or RRSP, build the rest.\n\n"
     "Do this: this payday, set up $50 a month into your TFSA. Raise it with every raise.\n\n"
     "Money Foundations, Part 6. Tonight at 7: take CPP at 60, or wait until 70?\n\n"
     f"Send this to the friend counting on CPP.\n\n{NG}\n\n#CPP #retirementcanada #TFSA #personalfinancecanada #moneyfoundations",
     SRC_CPP)

reel("ff-reel-1023-cpp-60-or-70", FF, "2026-10-23T19:00", "deep", "ff-x-money-moves", "save this for your parents", [
    dict(k="hook", f="cob", text="Take CPP at 60, / or wait / *until 70?*", emo="⏳"),
    dict(k="say", f="lite", text="Start at *60,* / and your cheque / is up to *36%* / smaller. For life.", size=112),
    dict(k="because", f="coral", kicker="the part nobody tells you",
         text="Wait until *70,* and it's up to 42% bigger. Every month, for life.", size=110),
    dict(k="num", f="deep", label="the 2026 max at 70:", value=CPP_70, pre="$", suf="a month, vs $1,508 at 65", size=220, drop=True),
    dict(k="do", f="lite", text="Tonight, check your *CPP estimate* in My Service Canada Account.", size=96, chars=18),
    dict(k="save", f="cob", text="Send this to / your parents. / Seriously."),
], f"Take CPP at 60, or wait until 70?\n\n"
   f"Start at 60, and your cheque is up to 36% smaller, for life. Wait until 70, and it's up to 42% bigger, every month, for life. "
   f"At the 2026 maximum, that's about ${CPP_MAX:,.0f} a month at 65, or about ${CPP_70:,} at 70.\n\n"
   f"The honest part: waiting isn't right for everyone. Your health, your savings and when you stop working all matter.\n\n"
   f"Do this: tonight, check your CPP estimate in My Service Canada Account.\n\n"
   f"Send this to your parents. Seriously.\n\n#CPP #retirementcanada #retirementplanning #personalfinancecanada #moneyfoundations",
   SRC_CPP + f" Maths: $1,507.65 × 1.42 ≈ ${CPP_70:,} (shown rounded down; the pension is also indexed to inflation).",
   series="CPP · part 2/2")

chain("ff-ch-1023", FF, "2026-10-23", "ff22", "money foundations · part 6", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="lite", label="quick quiz", title="The average new / *CPP at 65…*", bubbles=[
        ("in", "how much is it a month?"), ("out", "A) about $858"), ("out", "B) about $1,500")], tap="guess, then tap →"),
    dict(k="payoff", f="coral", label="the answer: A", text="*$858*", sub="a month, on average (2026)", obj="ok",
         tap="source: canada.ca · tap →"),
    dict(k="payoff", f="cob", label="why it matters", text="CPP is a / *floor,* not a plan.", sub="your savings build the rest", obj="piggy",
         tap="next story →"),
    dict(k="handoff", f="lite", text="Will CPP / *pay your bills?*", img="ff-1023-cpp-enough/01.jpg", next="60 or 70? tonight at 7"),
])


# ================================================================== Oct 24 (Story chain day; 12:00 = ff-1024-paycheque-trail, the page's interactive)
# Facts checked Oct 18 pm. EI sickness 2026: 55% of average insurable weekly earnings, max $729/week, up to 26 weeks (canada.ca).
# Ontario estate administration tax: $0 on the first $50,000, $15 per $1,000 above; RRSP/RRIF/TFSA with a beneficiary designation
# and life insurance paid to a named beneficiary are left out of the estate value (ontario.ca).
EI_MAX = 729
EI_SHARE_80K = EI_MAX / (80000 / 52)          # 0.47 -> "less than half"
assert EI_SHARE_80K < 0.5
EAT_100K = (100000 - 50000) // 1000 * 15      # 750
assert EAT_100K == 750

reel("ff-reel-1024am-sick-pay-gap", FF, "2026-10-24T08:15", "deep", "ff-x-level-up", "check this before you need it", [
    dict(k="hook", f="cob", text="Too sick to work / for months? / *Here's what EI pays.*", emo="🩺"),
    dict(k="say", f="lite", text="EI sickness pays / *55%* of your pay, / up to *$729 a week.*", size=112),
    dict(k="say", f="coral", text="Earn *$80,000?* / That's *less than* / *half* your pay.", size=112),
    dict(k="because", f="deep", kicker="the part nobody tells you",
         text="After 26 weeks, it stops. That's what *disability insurance* is for.", size=104, drop=True),
    dict(k="do", f="lite", text="This week, ask HR: do I have *long-term disability,* and what does it pay?", size=92, chars=18),
    dict(k="save", f="cob", text="Send this to / the friend who / says “I'm healthy.”"),
], f"Too sick to work for months? Here's what EI pays.\n\n"
   f"EI sickness benefits pay 55% of your average weekly earnings, up to ${EI_MAX} a week in 2026, for up to 26 weeks. Earn $80,000 "
   f"a year and that's less than half your usual pay. After 26 weeks, EI sickness stops.\n\n"
   f"The part nobody tells you: some illnesses and injuries keep people off work much longer. Disability insurance replaces part of "
   f"your pay while you can't work. Many people have some through work (group long-term disability), but don't know how much.\n\n"
   f"Do this: this week, ask HR or check your benefits booklet: do I have long-term disability, how much does it pay, and for how long?\n\n"
   f"Send this to the friend who says \"I'm healthy.\"\n\n#disabilityinsurance #EI #personalfinancecanada #insurance #moneyfoundations",
   "Source: canada.ca, 'EI sickness benefits: How much you could receive': 55% of your average insurable weekly earnings, up to a "
   "maximum of $729 a week in 2026, for up to 26 weeks. Maths: $80,000 ÷ 52 ≈ $1,538 a week; $729 is about 47% of that. "
   "Education, not advice: talk to a licensed advisor about your own coverage.")

chain("ff-ch-1024", FF, "2026-10-24", "ff19", "money foundations", [
    dict(k="photo", text="“Payday! / Where does it / *all go?*”", sub="start with *stop 1* →", ink="dark", y=560),
    dict(k="bubbles", f="lite", label="sound familiar?", bubbles=[
        ("in", "payday was friday. it's *already gone* 😩"), ("out", "did any of it go to *you* first?"), ("in", "…like, savings?")]),
    dict(k="bubbles", f="cob", label="here's the order", bubbles=[
        ("out", "1. a month of bills in *savings*"), ("out", "2. any *work match* on savings"), ("out", "3. then your *TFSA*")],
         obj="phone"),
    dict(k="payoff", f="coral", label="the trick", text="Make it / *automatic.*", sub="it moves on payday, before you can spend it",
         obj="piggy"),
    dict(k="handoff", f="lite", text="Payday. Where should / *the money go first?*", img="ff-1024-paycheque-trail/01.jpg",
         next="follow the trail"),
])

reel("ff-reel-1024-beneficiary", FF, "2026-10-24T19:00", "deep", "ff-x-money-moves", "check this tonight", [
    dict(k="hook", f="cob", text="Your TFSA has / a blank line. / *Fill it in.*", emo="📝"),
    dict(k="say", f="lite", text="It asks who gets / the money *if you die.* / It's called a / *beneficiary.*", size=108),
    dict(k="because", f="coral", kicker="here's why it matters",
         text="With a name there, the money goes *straight to them,* outside your estate.", size=108),
    dict(k="num", f="deep", label="Ontario estate tax on $100,000:", value=EAT_100K, pre="$", suf="a named beneficiary skips it",
         size=220, drop=True),
    dict(k="do", f="lite", text="Tonight, log in to your bank and check who's named on your *TFSA* and *RRSP.*", size=96, chars=18),
    dict(k="save", f="cob", text="Send this to / your partner."),
], f"Your TFSA has a blank line. Fill it in.\n\n"
   f"When you open a TFSA or RRSP, it asks who gets the money if you die. That person is your beneficiary (for a spouse on a TFSA, "
   f"it can be a \"successor holder\").\n\n"
   f"Why it matters: with a name there, the money can go straight to that person, outside your estate. In Ontario, the estate "
   f"administration tax is $15 for every $1,000 over $50,000, so $100,000 going through the estate costs about ${EAT_100K}. "
   f"Money paid to a named beneficiary isn't counted. It's also usually faster.\n\n"
   f"Do this: tonight, log in to your bank and check who's named on your TFSA and RRSP. Moved in with someone, had a baby, "
   f"or split up since you opened it? Update it.\n\n"
   f"Rules differ by province (in Quebec, most designations go in your will). Send this to your partner.\n\n"
   f"#beneficiary #TFSA #RRSP #estateplanning #moneyfoundations",
   "Source: ontario.ca, 'Estate Administration Tax': no tax on the first $50,000, $15 per $1,000 (or part) above it; RRSPs, RRIFs "
   "and TFSAs with a beneficiary designation, and life insurance paid to a named beneficiary, are not included in the estate's value. "
   f"Maths: ($100,000 − $50,000) ÷ 1,000 × $15 = ${EAT_100K}. General information, not legal or tax advice.")


# ================================================================== Oct 25 (day B: quiz; 08:15 = ff-pan-1025am-paycheque-trail)
# TFSA: room since 2009 = $109,000 for someone 18+ and resident since 2009; withdrawals come back January 1 of the next year;
# excess contributions are taxed 1% a month (CRA rules, summarised by TD).
TFSA_LIMITS = {2009: 5000, 2010: 5000, 2011: 5000, 2012: 5000, 2013: 5500, 2014: 5500, 2015: 10000, 2016: 5500, 2017: 5500,
               2018: 5500, 2019: 6000, 2020: 6000, 2021: 6000, 2022: 6000, 2023: 6500, 2024: 7000, 2025: 7000, 2026: 7000}
TFSA_TOTAL = sum(TFSA_LIMITS.values())
assert TFSA_TOTAL == 109000
SRC_TFSA = ("Sources: CRA TFSA dollar limits 2009 to 2026 (total $109,000 if you were 18 or older and a resident of Canada since "
            "2009); TD, 'TFSA contribution room and withdrawal rules': withdrawals are added back to your room the following year "
            "(January 1); over-contributions are taxed 1% per month on the highest excess amount, for every month it stays in. "
            "Your exact room is in CRA My Account (as of January 1, so subtract this year's deposits). Education, not tax advice.")

post("ff-1025-tfsa-room", FF, "2026-10-25T12:00", "learning",
     dict(lay="pills", f="coral", kicker="money foundations · part 7", text="Your TFSA room / could be / *$109,000*", obj="point", at="bl",
          save="if you were 18 by 2009"),
     [dict(k="rows", f="lite", text="How it *adds up*", cap="TFSA room, CRA limits",
           rows=[("18 by 2009?", "$109,000 total"), ("New room in 2026", "$7,000"), ("Never used it?", "still all there")],
           src="CRA TFSA limits, 2009 to 2026"),
      dict(k="say", f="coral", label="the part nobody tells you", text="Put in *too much,* / and the CRA / charges *1%* / every month.",
           sub="on the extra, until it comes out"),
      dict(k="do", f="cob", text="Before your next deposit, check your *TFSA room* in CRA My Account.",
           size=96, save="send this to the friend who just opened a TFSA")],
     f"Your TFSA room could be ${TFSA_TOTAL:,}.\n\n"
     f"If you were 18 or older in 2009 and have lived in Canada since, every year's limit has added up: ${TFSA_TOTAL:,} by 2026. "
     f"Unused room never expires. It just waits for you.\n\n"
     f"The part nobody tells you: put in more than your room, and the CRA charges 1% a month on the extra, every month it stays in. "
     f"The number in CRA My Account is as of January 1, so subtract anything you've already put in this year.\n\n"
     f"Do this: before your next deposit, check your TFSA room in CRA My Account.\n\n"
     f"Money Foundations, Part 7. Tonight at 7: the withdrawal trap.\n\n"
     f"Send this to the friend who just opened a TFSA.\n\n#TFSA #personalfinancecanada #CRA #investingcanada #moneyfoundations",
     SRC_TFSA)

chain("ff-ch-1025", FF, "2026-10-25", "ff22", "money foundations · part 7", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="lite", label="quick quiz", title="Total TFSA room / *since 2009…*", bubbles=[
        ("in", "if you were 18 in 2009?"), ("out", "A) about $70,000"), ("out", "B) about $109,000")], tap="guess, then tap →"),
    dict(k="payoff", f="coral", label="the answer: B", text="*$109,000*", sub="if you've never put a dollar in", obj="ok",
         tap="source: CRA limits · tap →"),
    dict(k="payoff", f="cob", label="why it matters", text="Unused room / *never expires.*", sub="it waits for you", obj="piggy",
         tap="next story →"),
    dict(k="handoff", f="lite", text="Your TFSA room / could be *$109,000*", img="ff-1025-tfsa-room/01.jpg", next="tonight: the withdrawal trap"),
])

reel("ff-reel-1025-tfsa-withdrawal-trap", FF, "2026-10-25T19:00", "deep", "ff-x-big-reveal", "save this before you withdraw", [
    dict(k="hook", f="cob", text="Took money out / of your TFSA? / *Don't rush it back.*", emo="⚠️"),
    dict(k="say", f="lite", text="You take out / *$5,000* in March. / You put it back / in *June.*", size=112),
    dict(k="because", f="coral", kicker="here's the trap",
         text="The room from a withdrawal comes back on *January 1.* Not the same year.", size=108),
    dict(k="say", f="deep", text="No room left? / The CRA charges / *1% a month* / on the extra.", size=112, drop=True),
    dict(k="do", f="lite", text="Before you put money back, check your *room* in CRA My Account.", size=96, chars=18),
    dict(k="save", f="cob", text="Send this to / your TFSA friend."),
], "Took money out of your TFSA? Don't rush it back in.\n\n"
   "You take out $5,000 in March and put it back in June. Feels harmless. But the room from a withdrawal only comes back on "
   "January 1 of the next year. If you had no other room left, that $5,000 is an over-contribution, and the CRA charges 1% a month "
   "on it until it's out.\n\n"
   "Do this: before you put money back, check your room in CRA My Account (it shows your room as of January 1). Moving money "
   "between banks? Ask for a direct transfer, which doesn't count as a withdrawal.\n\n"
   "Send this to your TFSA friend.\n\n#TFSA #personalfinancecanada #CRA #taxtips #moneyfoundations",
   SRC_TFSA + " Direct transfers between your own TFSAs at different institutions are not withdrawals (CRA).",
   series="TFSA · part 2/2")


# ------------------------------------------------------------------ AIR PASS (Oct 18 am): size each Oct 19-21 slide to its longest line,
# so forced line breaks never re-wrap (one line on screen = one line in the source).
def _fit_sizes(brand, em=0.47, cap=136, floor=88):
    """AIR PASS: keep the hand-written line breaks and pick each slide's size so its longest line fits the 920px text box
    (em = average glyph width for this page's serif) and all its lines fit the box height. Then nothing re-wraps.
    Oct 19-21 feed slides only."""
    import re as _re
    from specs_teach import POSTS, META

    def _len(s):
        return len(_re.sub(r"\*", "", s)) + 2 * len(_re.findall(r"[\U0001F300-\U0001FAFF]", s))

    for _pid, _sp in POSTS.items():
        if _sp["brand"] != brand or META[_pid]["at"][:10] not in ("2026-10-19", "2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23", "2026-10-25"):
            continue
        for _s in _sp["slides"]:
            if _s.get("k") in ("do", "rows", "steps"):
                continue
            lines = _s["text"].split(" / ")
            box_h = 430 if (_s.get("num") or _s.get("bars")) else 540
            w = 900 / (em * max(_len(x) for x in lines))
            h = box_h / (0.9 * len(lines))
            _s["size"] = int(max(floor, min(cap, w, h)))



_fit_sizes(FF)

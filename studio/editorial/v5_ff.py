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
          save="slide 2 will surprise you"),
     [dict(k="say", f="cob", label="it grows like a snowball",
           text=f"Invest *$10,000* at 30. / Year one, it earns / about ${K['snow_y1']:,}. / By 60, it earns this / in *one* year:",
           num=f"${K['snow_y30']:,}", size=104, src="10% a year: the S&P 500's long-run average"),
      dict(k="say", f="coral", label="the honest part",
           text="Some years, markets / drop a lot. / So this is for money / you won't need / for *10+ years.*", size=118),
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

# ================================================================== Oct 19 · Part 2: the cheap coat
reel("ff-reel-1019am-term-vs-whole", FF, "2026-10-19T08:15", "deep", "ff-x-level-up", "save this before you buy life insurance", [
    dict(k="hook", f="cob", text="One kind of / life insurance / costs *much less.*", emo="🛡️"),
    dict(k="say", f="lite", text="*Term life* covers / you for a set time, / like 20 years. / It costs *less.*", size=112),
    dict(k="say", f="coral", text="*Whole life* covers / you forever and / builds some savings / inside. It costs / *much more.*", size=106),
    dict(k="because", f="deep", kicker="so which one?", text="Term is built for the years people depend on your pay: young kids, a big mortgage.",
         size=104, drop=True),
    dict(k="do", f="lite", text="Tonight, ask your HR or benefits team how much *life insurance* you already have.", size=96, chars=18),
    dict(k="save", f="cob", text="Send this to / your partner."),
], "There are two main kinds of life insurance, and one costs much less.\n\nTerm life covers you for a set time, like 20 years. If you die "
   "in that time, your family gets paid. It usually costs less.\n\nWhole life covers you for your whole life and builds some savings "
   "inside the policy. It usually costs much more each month.\n\nTerm is built for the years people depend on your pay: young kids, a "
   "big mortgage. Many people get some life insurance through work, so check what you already have first.\n\nDo this tonight: ask your "
   "HR or benefits team how much life insurance you already have.\n\nSend this to your partner.\n\n"
   "#lifeinsurance #termlife #personalfinance #newparents #moneyfoundations",
   "Source: Financial and Consumer Services Commission (FCNB, a Canadian provincial regulator), \"Life insurance\": term covers you for a "
   "specific time period and its premiums are \"generally less expensive\"; permanent covers you for life and generally builds cash value. "
   "fcnb.ca/en/insurance/life-insurance. Education, not advice: talk to a licensed advisor about your own needs.")

post("ff-1019-rich-habits-01", FF, "2026-10-19T12:00", "learning",
     dict(lay="line", f="lite", text="The *cheap* coat / costs *5 times more*", obj="ok", at="br",
          dots=[("$240 coat", "worn 120 times", f"${K['coat_a']} a wear"), ("$60 coat", "worn 6 times", f"${K['coat_b']} a wear")],
          save="money foundations · part 2"),
     [dict(k="say", f="cob", label="sound familiar?", text="Your *$60* sale coat / lasts *6 wears.* / Each wear costs you:",
           num=f"${K['coat_b']}", sub=f"her $240 coat, 120 wears: ${K['coat_a']} a wear"),
      dict(k="say", f="coral", label="it has a name", text="The price tag is / what you pay *today.* / *Cost per wear* is / what you *really* pay.",
           sub="never worn? $240 a wear"),
      dict(k="do", f="lite", text="Before your next buy over $50, ask: how many times will I *really* use this?",
           size=100, save="send this to your sale-loving friend")],
     f"The cheap coat can cost you 5 times more.\n\nYou buy a $60 coat on sale and it's done after 6 wears. That's ${K['coat_b']} "
     f"every time you put it on. Your friend pays $240 for a good one and wears it 120 times. That's ${K['coat_a']} a wear.\n\n"
     f"It's called cost per wear: the price, divided by how often you'll use it. The price tag tells you what you pay today. "
     f"The cost per wear tells you what you really pay.\n\nThe honest part: it only works if "
     f"you really use it. A $240 coat that stays in the closet is $240 a wear.\n\nDo this: before your next buy over $50, ask yourself "
     f"how many times you'll really use it.\n\nMoney Foundations, Part 2. Part 3 tomorrow: index funds, in plain words.\n\n"
     f"Send this to your sale-loving friend. Save it for your next shopping trip.\n\n"
     f"#moneytips #budgeting #personalfinance #costperwear #moneyfoundations",
     f"Maths: price divided by times used. $240 ÷ 120 = ${K['coat_a']}. $60 ÷ 6 = ${K['coat_b']}. $10 is 5 times $2. Count your own uses: "
     f"they will differ. Story quiz: Ellen MacArthur Foundation, A New Textiles Economy (2017): the average number of times a garment is "
     f"worn has fallen 36% compared with 15 years earlier.")

reel("ff-reel-1019-late-start", FF, "2026-10-19T19:00", "deep", "ff-x-big-reveal", "save this if you feel behind", [
    dict(k="hook", f="cob", text="Started / investing late? / *It's not too late.*", emo="⏳"),
    dict(k="say", f="lite", text="A friend invests / *$300 a month* / from age 28. / You start at *33.*", size=116),
    dict(k="num", f="deep", label="To catch up by 60, / invest about:", value=K["catch_pmt"], pre="$", suf="a month, at 10% a year", drop=True),
    dict(k="because", f="coral", kicker="here's why", text="You have fewer years, so each dollar has to do *more work.*", size=116),
    dict(k="do", f="lite", text="This payday, raise your automatic transfer by *$25.* Raise it again with every raise.", size=96, chars=18),
    dict(k="save", f="cob", text="Send this to / the friend who / thinks it's too late.", next="start early · part 2/2"),
], f"Started investing late? It's not too late.\n\nA friend invests $300 a month from age 28. You start at 33. To catch up by 60, at 10% "
   f"a year, you'd invest about ${K['catch_pmt']} a month. You have fewer years, so each dollar has to do more work.\n\n"
   f"Do this: this payday, raise your automatic transfer by $25. Raise it again with every raise at work.\n\n"
   f"Send this to the friend who thinks it's too late. Part 2 of 2.\n\n{NG}\n\n"
   f"#investing #personalfinance #moneytips #retirement #moneyfoundations",
   "Maths: the monthly amount from 33 to 60 that reaches the same total as $300 a month from 28 to 60, both compounded monthly at 10% a "
   "year, no fees or taxes. Source for 10%: Fidelity, \"S&P 500 average return\": about 10% a year since 1957 (before inflation). "
   "Education, not advice.", series="Start early · part 2/2")

chain("ff-ch-1019", FF, "2026-10-19", "ff19", "money foundations · part 2", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="lite", label="quick quiz", title="Each piece of clothing: / worn *more* or *less?*", bubbles=[
        ("in", "2015 vs 2000, on average…"), ("out", "A) about the same"), ("out", "B) about a third less")],
         tap="guess, then tap →"),
    dict(k="payoff", f="coral", label="the answer: B", text="*36%* / fewer", sub="wears per piece, 2000 to 2015", obj="ok",
         tap="source: Ellen MacArthur Foundation, 2017 · tap →"),
    dict(k="payoff", f="cob", label="why it matters", text="Fewer wears means / *paying more*", sub="for every single wear", obj="piggy",
         tap="next story →"),
    dict(k="handoff", f="lite", text="The *cheap* coat / costs *5 times more*", img="ff-1019-rich-habits-01/01.jpg", next="part 3 tomorrow"),
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
     [dict(k="say", f="lite", label="picking stocks is hard", text="In 2025, nearly / *8 in 10* pro funds / did worse than / the market.",
           sub="an index fund just buys all of them", src="S&P Dow Jones Indices, SPIVA U.S. Year-End 2025 (large-cap funds)"),
      dict(k="say", f="coral", text="Since 1957, the / S&P 500 grew, / on average:", num="10%",
           sub="a year, but some years it drops: about 37% in 2008",
           src="Fidelity, S&P 500 average return, before inflation · S&P Dow Jones Indices"),
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
          save="check if you qualify on slide 3"),
     [dict(k="say", f="cob", label="Canada Learning Bond", text="*$500* to start, / then *$100* a year, / up to *$2,000.*",
           sub="you add $0. it goes into an RESP, a school savings account", src="canada.ca · Canada Learning Bond"),
      dict(k="rows", f="lite", text="Who *qualifies*", cap="family net income, July 2026 to June 2027",
           rows=[("1 to 3 kids", "$58,523 or less"), ("4 kids", "under $66,036"), ("5 kids", "under $73,577")],
           sub="kids born in 2004 or later", src="canada.ca · ESDC notice 2026-1138 · limits change each July"),
      dict(k="say", f="coral", label="you're not alone", text="In 2022, / *2.5 million* / eligible kids / never got it.",
           sub="good news: you can apply until your child turns 21",
           src="C.D. Howe Institute, using ESDC 2022 data · canada.ca"),
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
        if _sp["brand"] != brand or META[_pid]["at"][:10] not in ("2026-10-19", "2026-10-20", "2026-10-21"):
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

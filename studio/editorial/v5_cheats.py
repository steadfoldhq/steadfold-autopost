"""Canada-edition cheat-sheet Reels (Oct 18). Every figure computed here or quoted from a named official source.
Scheduled by add_to_schedule() below (not teach_schedule), as Trial Reels in the morning."""
import math

FF, HB, LH, LF = "fullyfunded", "hourback", "lockedhour", "littlefold"
NG = "Not guaranteed. Returns vary. Education, not advice."


def per_month_for_million(age, rate=0.10, end=65):
    r, n = rate / 12, (end - age) * 12
    return 1e6 * r / ((1 + r) ** n - 1)


CHEATS = {}
META = {}


def cheat(pid, at, spec, caption, comment):
    CHEATS[pid] = spec
    META[pid] = dict(at=at, caption=caption, comment=comment)


# ---------------------------------------------------------------- FF · what fees cost you (Oct 21 08:15)
def fv(pmt, years, rate):
    r, n = rate / 12, years * 12
    return pmt * ((1 + r) ** n - 1) / r


BASE = fv(300, 32, 0.10)
FEES = [0.25, 0.5, 1.0, 1.5, 2.0, 2.5]
cheat("ff-cheat-1021am-fees-eat", "2026-10-21T08:15",
      dict(brand=FF, field="lite", track="ff-x-level-up",
           title="A *1% fee* sounds tiny. / Here's what it *takes*", head=("yearly fee (MER)", "fees take from you"),
           rows=[(f"{f:g}%", f"${BASE - fv(300, 32, 0.10 - f / 100):,.0f}") for f in FEES],
           do="Look up your fund's *MER* this week. Over 1%? Ask what a *low-fee index fund* costs.",
           save="send this to someone with a bank mutual fund", do_top=1300,
           src="$300 a month from 28 to 60, 10% a year before fees, compounded monthly. Fee shown = value lost by 60. Not guaranteed."),
      "A 1% fee sounds tiny. Here's what it takes 🇨🇦\n\n$300 a month from 28 to 60, growing 10% a year before fees:\n"
      + "\n".join(f"{f:g}% fee → fees take about ${BASE - fv(300, 32, 0.10 - f / 100):,.0f}" for f in FEES)
      + "\n\nWhy: the fee comes out every year, from your whole balance, and the money it takes can't grow for you anymore.\n\n"
      "Do this this week (10 minutes):\n1. Log in to your investing account and open each fund.\n"
      "2. Find the MER (management expense ratio), usually on the fund's page or its \"Fund Facts\" sheet.\n"
      "3. Over 1%? Ask your bank or broker: \"What would a broad, low-fee index fund cost me instead?\" Ask about any fee to switch.\n\n"
      "The mindset: you can't control the market, but you can control what you pay. The Simple Path to Wealth makes the same "
      "case: own the whole market, as cheaply as you can.\n\n"
      "The rule to remember: every 1% you pay is 1% that stops growing for you.\n\n"
      "Send this to someone with a bank mutual fund.\n\n"
      f"{NG}\n\n#mer #investingcanada #indexfunds #personalfinancecanada #fees",
      "What's your fund's MER? Maths: $300 at the end of each month for 32 years, 10% a year minus the fee, compounded monthly; "
      "shown is the difference vs no fee.")

# ---------------------------------------------------------------- FF · the price of waiting one year (Oct 21 19:00)
WAIT = [25, 28, 30, 33, 35]
cheat("ff-cheat-1021-one-year-wait", "2026-10-21T19:00",
      dict(brand=FF, field="cob", track="ff-x-big-reveal",
           title="What waiting *just 1 year* / costs you by 65", head=("if you're", "one year of waiting costs"),
           rows=[(f"{a}", f"${fv(300, 65 - a, 0.10) - fv(300, 64 - a, 0.10):,.0f}") for a in WAIT],
           do="Start this payday with *any amount,* even $50. Raise it later.", save="send this to your “next year” friend",
           do_top=1220,
           src="$300 a month to 65, 10% a year (S&P 500 long-run average), compounded monthly. Not guaranteed."),
      "What waiting just one year costs you by 65 🇨🇦\n\n$300 a month, growing 10% a year:\n"
      + "\n".join(f"Age {a}: waiting one year costs about ${fv(300, 65 - a, 0.10) - fv(300, 64 - a, 0.10):,.0f}" for a in WAIT)
      + "\n\nWhy so much? The year you skip is the one that would have grown the longest. You don't lose the first year, "
      "you lose the last one, the biggest.\n\n"
      "Do this, this payday (5 minutes):\n1. Open your bank app and set a recurring transfer into your TFSA for payday.\n"
      "2. Start with any amount, even $50. Starting matters more than the size.\n"
      "3. Every time you get a raise, raise the transfer too.\n\n"
      "The mindset: The Psychology of Money's big lesson is that time does the heavy lifting. Waiting for the perfect moment "
      "costs more than starting small.\n\n"
      f"The rule to remember: the best year to start was last year. The second best is this payday.\n\n{NG}\n\n"
      "#investingcanada #tfsa #compounding #startnow #personalfinancecanada",
      "How old are you? Maths: $300 at the end of each month to 65 at 10% a year compounded monthly; cost = value starting now minus value starting a year later.")

# ---------------------------------------------------------------- LF · money for families (Oct 21 08:00)
cheat("lf-cheat-1021am-family-money", "2026-10-21T08:00",
      dict(brand=LF, field="cream", track="lf-x-sunny-bounce",
           title="Money your family / can get *for each child*", head=("what", "up to"),
           rows=[("Canada Child Benefit, under 6", "$8,157/yr"), ("Canada Child Benefit, 6 to 17", "$6,883/yr"),
                 ("RESP grant (20% match)", "$500/yr"), ("RESP grant, lifetime", "$7,200"), ("Canada Learning Bond", "$2,000")],
           do="File your taxes *every year,* both parents, even with no income. That's how you get the benefit.",
           save="send this to a new parent 🍼",
           src="canada.ca: CCB July 2026–June 2027 maximums (income-tested) · CESG · Canada Learning Bond (family income limits apply)."),
      "Money your family can get in Canada, for each child 🇨🇦\n\nCanada Child Benefit: up to $8,157 a year under 6, up to $6,883 a year age 6 to 17 "
      "(July 2026 to June 2027, less as family income rises).\nRESP grant: 20% on what you save, up to $500 a year and $7,200 lifetime.\n"
      "Canada Learning Bond: up to $2,000 for lower-income families, no deposit needed.\n\n"
      "The part people miss: the Child Benefit is based on your tax return. Both parents need to file every year, even with no income.\n\n"
      "Do this: file your taxes every year, and open an RESP to collect the grants.\n\nSend this to a new parent.\n\n"
      "#canadachildbenefit #newparents #canadianparents #RESP #babymoney",
      "Did you know both parents have to file? Sources: canada.ca (CCB: how much you can get, July 2026–June 2027), "
      "Canada Education Savings Grant, ESDC notice 2026-1138 (Learning Bond).")

# ---------------------------------------------------------------- FF · TFSA vs RRSP vs FHSA (Oct 22 08:15)
cheat("ff-cheat-1022am-tfsa-rrsp-fhsa", "2026-10-22T08:15",
      dict(brand=FF, field="lite", track="ff-x-money-moves", beat=0.9, card_h=250, table_top=620,
           title="TFSA vs RRSP vs FHSA / in *one look*",
           cards=[dict(name="TFSA", lines=["$7,000 room in 2026", "No tax break going in", "Tax-free coming out"]),
                  dict(name="RRSP", lines=["18% of income, max $33,810", "Tax break now", "Taxed when you take it out"]),
                  dict(name="FHSA", lines=["$8,000 a year, $40,000 total", "Tax break now", "Tax-free for your first home"])],
           do="Buying a first home? *FHSA first.* Otherwise, start with the *TFSA.*", do_top=1420,
           save="save this before tax season 🔖",
           src="CRA 2026 limits: TFSA $7,000 · RRSP 18% of 2025 earned income up to $33,810 · FHSA $8,000/yr, $40,000 lifetime."),
      "TFSA vs RRSP vs FHSA, in one look 🇨🇦\n\nTFSA: $7,000 of new room in 2026. No tax break going in, tax-free coming out. Use it for anything.\n"
      "RRSP: 18% of last year's income, up to $33,810. Tax break now, taxed when you take it out. Best for retirement, especially on a higher income.\n"
      "FHSA: $8,000 a year, $40,000 total. Tax break going in AND tax-free out, if it's for your first home.\n\n"
      "How to pick, in order:\n1. Buying a first home in the next 15 years? Open the FHSA first. Room only starts building once "
      "it's open, so even $0 inside today counts.\n"
      "2. Higher income now than you expect in retirement? The RRSP's tax break is worth more to you.\n"
      "3. Everything else, or not sure? The TFSA. Take money out any time; the room comes back next January 1.\n\n"
      "Do this tonight: log in to CRA My Account and write down your TFSA room and RRSP deduction limit.\n\n"
      "The rule to remember: home first? FHSA. Big tax bracket? RRSP. Everything else? TFSA.\n\nSave this before tax season.\n\n"
      "#tfsa #rrsp #fhsa #personalfinancecanada #firsthome",
      "Which one did you open first? Sources: CRA 2026 limits (TFSA $7,000; RRSP $33,810 or 18% of 2025 earned income; FHSA $8,000/yr, $40,000 lifetime).")


# ---------------------------------------------------------------- LF · sleep and screens by age (Oct 22 08:00)
cheat("lf-cheat-1022am-sleep-screens", "2026-10-22T08:00",
      dict(brand=LF, field="cream", track="lf-x-giggle-pop",
           title="Sleep and screens, / *by age* (0 to 4)", head=("age", "sleep a day · screens"),
           rows=[("0 to 3 months", "14–17 h · none"), ("4 to 11 months", "12–16 h · none"), ("1 year", "11–14 h · none"),
                 ("2 years", "11–14 h · under 1 h"), ("3 to 4 years", "10–13 h · under 1 h")],
           do="Make *family meals* screen-free, starting with dinner tonight.", save="send this to a tired parent 🌙",
           do_top=1300,
           src="Sleep includes naps. Canadian 24-Hour Movement Guidelines for the Early Years (CSEP) · Canadian Paediatric Society, Screen time and young children (video chats are fine)."),
      "Sleep and screens by age, Canada edition 🇨🇦\n\n0 to 3 months: 14 to 17 hours of sleep a day, no screens\n"
      "4 to 11 months: 12 to 16 hours, no screens\n1 year: 11 to 14 hours, no screens\n2 years: 11 to 14 hours, under 1 hour of screens\n"
      "3 to 4 years: 10 to 13 hours, under 1 hour of screens\n\nSleep counts naps. Video chats with grandma don't count as screen time.\n\n"
      "Do this: make family meals screen-free, starting with dinner tonight.\n\nSend this to a tired parent.\n\n"
      "General information only, not medical advice.\n\n#toddlersleep #screentime #babysleep #canadianparents #newparents",
      "Which row surprised you? Sources: Canadian 24-Hour Movement Guidelines for the Early Years (0-4 years), Canadian Society for "
      "Exercise Physiology: sleep including naps, 14-17 h (0-3 months), 12-16 h (4-11 months), 11-14 h (1-2 years), 10-13 h (3-4 years); "
      "screen time not recommended under 2, no more than 1 hour a day for ages 2-4. Canadian Paediatric Society position statement, "
      "Screen time and young children (2017): screen time for children under 2 is not recommended, except video-chatting; under 1 hour a "
      "day for ages 2 to 5; screen-free times, especially family meals.")

# ---------------------------------------------------------------- FF · CPP and OAS (Oct 23 08:15)
cheat("ff-cheat-1023am-cpp-oas", "2026-10-23T08:15",
      dict(brand=FF, field="lite", track="ff-x-level-up",
           title="What CPP and OAS / *pay you* in 2026", head=("CPP and OAS", "per month"),
           rows=[("Average new CPP at 65", "$858"), ("Max CPP at 65", "$1,508"), ("Start CPP at 60", "up to 36% less"),
                 ("Wait to 70", "up to 42% more"), ("OAS, ages 65 to 74", "up to $763")],
           do="Check your *CPP estimate* in My Service Canada Account.", save="send this to the friend counting on CPP",
           do_top=1300,
           src="canada.ca: CPP average for new pensions at 65 and 2026 maximum · when to start CPP · OAS maximum, October to December 2026."),
      "What your government pension pays, 2026 🇨🇦\n\nAverage new CPP at 65: about $858 a month\nMost you can get at 65: about $1,508 a month\n"
      "Start CPP at 60: up to 36% less, for life\nWait until 70: up to 42% more, for life\nOAS at 65 to 74: up to about $763 a month\n\n"
      "Why it matters: together, that's well short of most people's bills. Your TFSA and RRSP fill the gap.\n\n"
      "Do this (5 minutes):\n1. Log in to My Service Canada Account.\n2. Open \"Canada Pension Plan\" and find your estimated "
      "monthly pension at 65.\n3. Write it next to your monthly bills. The gap between the two is what your TFSA and RRSP need "
      "to cover.\n\n"
      "The rule to remember: CPP is the floor, not the house.\n\n"
      "Send this to the friend counting on CPP.\n\n#CPP #OAS #retirementcanada #personalfinancecanada #moneyfoundations",
      "Did you guess higher? Sources (canada.ca): CPP retirement pension at 65, average for new beneficiaries $858.34/month and 2026 "
      "maximum $1,507.65/month; when to start: 0.6% less per month before 65 (up to 36% at 60), 0.7% more per month after 65 (up to 42% "
      "at 70); OAS maximum, October to December 2026: $762.50/month (ages 65 to 74), $838.75 (75+).")

# ---------------------------------------------------------------- LH · focus science, in numbers (Oct 23 08:30)
cheat("lh-cheat-1023am-focus-numbers", "2026-10-23T08:30",
      dict(brand=LH, field="cream", track="lh-x-lock-in",
           title="Focus science / in *5 numbers*", head=("the study", "found"),
           rows=[("New habit feels automatic", "66 days"), ("Switching tasks can eat", "40% of time"), ("A walk lifts new ideas", "+60%"),
                 ("Wrote down when and where", "91% did it"), ("Coffee 6 h before bed", "−1 h sleep")],
           do="Try *one row* this week. Start with *the walk.*", save="save this for a slow Monday",
           do_top=1300,
           src="Lally et al. 2010 · APA 2006 · Oppezzo & Schwartz 2014 · Milne, Orbell & Sheeran 2002 · Drake et al. 2013 (400 mg caffeine)."),
      "Focus science, in 5 numbers\n\nA new habit takes about 66 days to feel automatic.\nSwitching tasks can eat up to 40% of your "
      "productive time.\nA walk lifted creative ideas by about 60%.\nPeople who wrote down when and where they'd exercise: 91% did it.\n"
      "Strong coffee 6 hours before bed cut sleep by more than an hour.\n\n"
      "Do this: this week, try one row. Start with a 10-minute walk before your hardest task.\n\nSave this for a slow Monday.\n\n"
      "#focus #habits #productivity #deepwork #studytips",
      "Which one will you try? Sources: Lally et al. (2010), European Journal of Social Psychology: median 66 days to automaticity. "
      "American Psychological Association (2006), Multitasking: switching costs, up to 40% of productive time. Oppezzo & Schwartz (2014): "
      "creative output up about 60% when walking. Milne, Orbell & Sheeran (2002), British Journal of Health Psychology: 91% of the "
      "implementation-intention group exercised. Drake et al. (2013), Journal of Clinical Sleep Medicine: 400 mg caffeine 6 hours "
      "before bed reduced total sleep by more than 1 hour.")

# ---------------------------------------------------------------- LF · RESP catch-up by age (Oct 23 19:00)
def cesg_catch_up(start_age):
    """Most CESG still collectable if the RESP starts at `start_age` and you put in enough each year: $500/yr of grant room
    builds from birth, at most $1,000 of grant a year, paid to the end of the year the child turns 17, $7,200 lifetime."""
    room, got = 0, 0
    for age in range(0, 18):
        room += 500
        if age >= start_age:
            g = min(1000, room, 7200 - got)
            got, room = got + g, room - g
    return got


CATCH = [0, 5, 10, 12, 14]
assert [cesg_catch_up(a) for a in CATCH] == [7200, 7200, 7200, 6000, 4000]
cheat("lf-cheat-1023-resp-catch-up", "2026-10-23T19:00",
      dict(brand=LF, field="butter", track="lf-x-sunny-bounce",
           title="Late on the RESP? / Grant you can *still get*", head=("start when they're", "grant still there"),
           rows=[("a newborn" if a == 0 else f"{a} years old", f"${cesg_catch_up(a):,}") for a in CATCH],
           do="Opening late? Ask your bank about *catch-up grants.*", save="send this to a parent who never opened one",
           do_top=1300,
           src="canada.ca, Canada Education Savings Grant: 20% match, up to $500 a year or $1,000 with unused room, $7,200 lifetime, to age 17. Assumes up to $5,000 a year to catch up."),
      "Late on the RESP? Here's the grant you can still get 🇨🇦\n\n"
      + "\n".join(f"Start at {'birth' if a == 0 else 'age ' + str(a)}: up to ${cesg_catch_up(a):,}" for a in CATCH)
      + "\n\nWhy: grant room builds up every year from birth, even with no RESP. Later, the government can pay up to $1,000 a year "
      "(20% of $5,000) until the full $7,200 is used, as long as you start in time.\n\n"
      "Do this: opening late? Ask your bank about catch-up grants, and bring your child's SIN.\n\n"
      "Send this to a parent who never opened one.\n\n#RESP #canadianparents #savingforkids #CESG #babymoney",
      "How old was your kid when you opened it? Source: canada.ca, Canada Education Savings Grant: 20% on the first $2,500 a year "
      "(up to $500), up to $1,000 a year with unused grant room, $7,200 lifetime, paid until the end of the calendar year the child "
      "turns 17. Children aged 16 or 17 qualify only if at least $2,000 was contributed before the end of the year they turned 15 (or "
      "$100 a year in any 4 earlier years). Maths: $500 of room a year from birth, max $1,000 of grant a year, starting at each age.")


def add_to_schedule(path):
    import json
    from pathlib import Path
    d = json.loads(Path(path).read_text())
    ids = {x["id"] for x in d["posts"]}
    acct = {FF: "fullyfunded", LF: "littlefold", HB: "hourback", LH: "lockedhour"}
    for pid, m in META.items():
        if pid in ids:
            d["posts"] = [x for x in d["posts"] if x["id"] != pid]
        sp = CHEATS[pid]
        rows = sp.get("rows") or [(c["name"], "; ".join(c["lines"])) for c in sp["cards"]]
        alt = (f"Canada-edition cheat sheet in the {sp['brand']} editorial look. Title: {sp['title'].replace('*', '').replace(' / ', ' ')}. "
               + " · ".join(f"{a}: {b}" for a, b in rows) + f". Do this: {sp['do'].replace('*', '')}")
        e = dict(id=pid, account=acct[sp["brand"]], publish_at=m["at"] + ":00-04:00", caption=m["caption"], first_comment=m["comment"],
                 alt_text=alt, video=f"reels/{pid}.mp4", cover=f"reels/{pid}-cover.jpg")
        if "am-" in pid:
            e["trial"] = "auto"
        d["posts"].append(e)
    d["posts"].sort(key=lambda x: (x["publish_at"], x["account"], x["id"]))
    Path(path).write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")

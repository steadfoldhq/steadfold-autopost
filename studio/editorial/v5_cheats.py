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
      "Do this: look up your fund's MER (the yearly fee) this week. Over 1%? Ask what a low-fee index fund would cost you.\n\n"
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
      + "\n\nWhy so much? The year you skip is the one that would have grown the longest.\n\n"
      f"Do this: start this payday with any amount, even $50. You can raise it later.\n\n{NG}\n\n"
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
      "Do this: buying a first home? Open the FHSA first. Otherwise, start with the TFSA.\n\nSave this before tax season.\n\n"
      "#tfsa #rrsp #fhsa #personalfinancecanada #firsthome",
      "Which one did you open first? Sources: CRA 2026 limits (TFSA $7,000; RRSP $33,810 or 18% of 2025 earned income; FHSA $8,000/yr, $40,000 lifetime).")


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

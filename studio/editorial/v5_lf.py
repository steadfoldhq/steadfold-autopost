"""Littlefold content, Oct 18-20. Rewritten Oct 17 night to the ONE-READ standard (/home/claude/one-read-standard.md).
Uses post()/reel()/chain() from specs_teach. Only this page's entries live here.
Kids' money figures checked on canada.ca (Oct 17): CESG 20% on the first $2,500 a year (max $500/yr basic, $7,200 lifetime,
catch-up up to $1,000 a year); CLB $500 + $100/yr up to $2,000, no contribution, born 2004+, ADFNI <= $57,375 for 1-3 kids
(Jul 2025 - Jun 2026, ESDC notice 2025-1095)."""
from specs_teach import post, reel, chain, FF, HB, LH, LF, NG, NOT_MED, MADE, PRIV, K  # noqa: F401


# ------------------------------------------------------------------ RESP growth, computed (never typed by hand)
def _resp(monthly=50, grant=0.20, rate=0.08, years=18, grant_years=17):
    """$monthly into an RESP from birth, the 20% CESG on top while the grant is paid (to the year the child turns 17),
    growing at `rate` a year, compounded monthly. Returns (value at 18, total you put in)."""
    i, v = rate / 12, 0.0
    for m in range(years * 12):
        v = v * (1 + i) + monthly * (1 + (grant if m < grant_years * 12 else 0))
    return v, monthly * years * 12


_V, _IN = _resp()
RESP_18 = int(_V // 1000) * 1000  # 28,681 -> "about $28,000" (rounded down, never up)
RESP_IN = _IN                     # 10,800
assert RESP_18 == 28000 and RESP_IN == 10800, (RESP_18, RESP_IN)

CESG_SRC = ("Government of Canada, canada.ca, Canada Education Savings Grant: the government adds 20% of the first $2,500 you put "
            "into an RESP each year (up to $500 a year), up to $7,200 per child in total. Unused grant room carries forward, up to "
            "$1,000 of grant in one year, until the end of the year the child turns 17.")
CLB_SRC = ("Government of Canada, canada.ca, Canada Learning Bond: $500 the first year, then $100 for each year you qualify, up to "
           "$2,000. No personal contribution needed. Children born in 2004 or later, from lower-income families. Income limit for "
           "July 2025 to June 2026: adjusted family net income of $57,375 or less for 1 to 3 children (ESDC notice 2025-1095).")

# ================================================================== FEED
# Oct 18, 11:30 · REPLACES lf-04-sleep-when-baby-sleeps · kids' money 1/2
post("lf-1018-resp-free-500", LF, "2026-10-18T11:30", "learning",
     dict(lay="sticky", f="pink", kicker="baby money · part 1", text="Free *$500* / a year",
          obj="point", at="bl", items=["For your baby's RESP", "Save $2,500", "Get $500 added"], save="part 2 tomorrow"),
     [dict(k="say", f="butter", text="An *RESP* is a / savings account for / your child's college / or university. The / government adds to it.",
           size=120),
      dict(k="say", f="cream", label="here's how it works", text="For every *$100* you / save, the government / adds *$20.* It's called / the education / savings grant.",
           size=120),
      dict(k="say", f="pink", text="Save *$2,500* a year / and the government / adds the full *$500.* / Over the years, that / can reach *$7,200.*",
           size=120, src="canada.ca, Canada Education Savings Grant"),
      dict(k="say", f="butter", label="the part nobody tells you", text="You don't need $2,500. / Even *$25 a month* / gets 20% added. / Small amounts / count too.",
           size=120),
      dict(k="say", f="cream", text="Started late? / It's not too late. / You can *catch up* / later: up to $1,000 / of grant in one year.",
           size=120),
      dict(k="do", f="pink", text="This week, ask your bank to *open an RESP* for your baby. Have their SIN ready.",
           save="send this to someone with a new baby")],
     "Your baby can get up to $500 a year from the government, just for saving for their school.\n\n"
     "It works through an RESP, a savings account for your child's college, university or trade school. For every $100 you put in, "
     "the government adds $20. Save $2,500 in a year and they add the full $500. Over the years that can reach $7,200 per child.\n\n"
     "You don't need $2,500. Any amount gets 20% added, and if you start late you can catch up (up to $1,000 of grant in one year).\n\n"
     "Do this: this week, ask your bank to open an RESP for your baby. Bring their SIN.\n\n"
     "Part 2 tomorrow: the money some families get with no deposit at all.\n\n"
     "Send this to someone with a new baby.\n\n"
     "#RESP #newparents #babymoney #canadianparents #savingforkids",
     "Source: " + CESG_SRC)

# Oct 18, 17:00 · REWRITE (same id) · postpartum low mood
post("lf-1018-single-sign-say-it", LF, "2026-10-18T17:00", "keep",
     dict(lay="pills", f="pink", text="Still feeling low / *weeks after* / the birth?", obj="ok", at="bl", save="you're not failing. it's common.",
          src="NHS, Postnatal depression"),
     [dict(k="say", f="butter", text="Feeling low in the / first days is common. / It's called the / *baby blues,* and it / usually passes / within *2 weeks.*",
           size=120),
      dict(k="say", f="cream", text="If it lasts longer / or gets worse, / it might be / *postnatal depression.* / It's common, and / you deserve help.",
           size=120, src="NHS, Postnatal depression"),
      dict(k="do", f="pink", text="Still feeling low after *2 weeks?* Call your *doctor or midwife* this week and tell them.",
           save="send this to a new mum you love")],
     "Still feeling low, weeks after the birth? You're not failing, and you're not alone.\n\n"
     "Feeling low, teary or anxious in the first days is very common. It's called the baby blues, and the NHS says it usually passes "
     "within 2 weeks of the birth. If it lasts longer or gets worse, it might be postnatal depression. It's common, and it's not your fault.\n\n"
     "Do this: still feeling low after 2 weeks? Call your doctor or midwife this week and tell them how you feel. You don't need to have "
     "every sign to ask.\n\n"
     "In crisis, or thinking about harming yourself? In Canada, call or text 9-8-8, any time. In an emergency, call 911.\n\n"
     "Send this to a new mum you love.\n\n"
     f"{NOT_MED}\n\n#postpartum #newmom #maternalmentalhealth #newparents #postnataldepression",
     "Source: NHS, Postnatal depression (nhs.uk): the baby blues usually go away within 2 weeks of the birth; if you think you might have "
     "postnatal depression, speak to your GP, midwife or health visitor, even if you only have some of the signs. Canada: 9-8-8 Suicide "
     "Crisis Helpline (call or text 988).")

# Oct 19, 11:30 · REPLACES lf-05-partner-week-one · kids' money 2/2
post("lf-1019-learning-bond", LF, "2026-10-19T11:30", "deep",
     dict(lay="sticky", f="cream", kicker="baby money · part 2", text="Up to / *$2,000,* / no deposit",
          obj="point", at="bl", items=["$500 to start", "$100 a year after", "Into your child's RESP"], save="see who qualifies"),
     [dict(k="say", f="butter", text="It's called the / *Canada Learning Bond.* / It goes into your / child's RESP, and / you don't add a cent.",
           size=120),
      dict(k="say", f="pink", text="It starts with *$500.* / Then the government / adds *$100* for each / year you qualify, / up to *$2,000.*",
           size=120, src="canada.ca, Canada Learning Bond"),
      dict(k="say", f="cream", label="who qualifies", text="Families with 1 to 3 / kids and a net / income of *$57,375* / or less can qualify.",
           sub="for July 2025 to June 2026", size=120),
      dict(k="say", f="butter", label="the part nobody tells you", text="Missed it? Kids born / in *2004 or later* can / claim it any time / *before they turn 21.*",
           size=120),
      dict(k="do", f="pink", text="This week, ask your bank for a *free RESP* with the Learning Bond. Bring your child's SIN.",
           save="send this to a parent who should check")],
     "Up to $2,000 for your child's education, and you don't have to put in a cent.\n\n"
     "It's called the Canada Learning Bond. The government puts $500 into your child's RESP, then $100 for each year your family "
     "qualifies, up to $2,000. No deposit is needed.\n\n"
     "Who can get it: for July 2025 to June 2026, families with 1 to 3 children and an adjusted family net income of $57,375 or less. "
     "Children born in 2004 or later can apply any time before they turn 21, so it's not too late if you missed it.\n\n"
     "Do this: this week, ask your bank for a free RESP with the Canada Learning Bond. Bring your child's SIN.\n\n"
     "Send this to a parent who should check.\n\n"
     "#RESP #CanadaLearningBond #newparents #canadianparents #babymoney",
     "Source: " + CLB_SRC)

# Oct 19, 17:00 · REWRITE (same id) · fever under 3 months
post("lf-1019-single-fever-under-3m", LF, "2026-10-19T17:00", "keep",
     dict(lay="pills", f="pink", text="Baby under / 3 months / *with a fever?*", obj="point", at="bl",
          save="this one can't wait for morning", src="American Academy of Pediatrics"),
     [dict(k="say", f="butter", text="For babies this young, / a fever of *38°C* or / higher means you call / the doctor *right away.*",
           size=120, src="American Academy of Pediatrics, healthychildren.org"),
      dict(k="say", f="cream", text="Older babies have / different rules. This / one is only for the / *first 3 months.* / Don't wait to see / if it passes.",
           size=120),
      dict(k="do", f="pink", text="Today, find the number to call your doctor *at night,* and save it. Can't reach anyone? Go to *emergency.*",
           save="send this to your babysitter")],
     "A fever in a baby under 3 months can't wait for morning.\n\n"
     "The American Academy of Pediatrics says: if your baby is younger than 3 months and has a temperature of 38.0°C (100.4°F) or "
     "higher, call the doctor right away. Older babies have different rules, so ask your doctor about yours.\n\n"
     "Do this: today, save your doctor's after-hours number in your phone. If you can't reach anyone, go to emergency.\n\n"
     "Send this to your babysitter, and anyone who looks after your baby.\n\n"
     f"{NOT_MED}\n\n#newborn #babyhealth #newparents #fever #parenting",
     "Source: American Academy of Pediatrics, healthychildren.org, Fever: when to call the pediatrician (younger than 3 months and "
     "100.4°F / 38.0°C or higher: call right away).")

# Oct 20, 11:30 · REWRITE (same id) · toddler meltdowns
post("lf-06-toddler-meltdown", LF, "2026-10-20T11:30", "learning",
     dict(lay="sticky", f="cream", text="Meltdown / in the *cereal aisle?*", obj="ok", at="bl",
          items=["Stay calm", "Keep your no", "Distract early"], save="save this for the next shop"),
     [dict(k="say", f="pink", text="Tantrums often start / around *18 months.* / Your toddler wants / to tell you something / but doesn't have / the words yet.",
           size=120, src="NHS, Temper tantrums"),
      dict(k="say", f="butter", label="here's the hard part", text="If you give in to / stop it, your child / learns that / *tantrums work.* / So keep your no, / calmly.",
           size=120),
      dict(k="say", f="cream", label="catch it early", text="When you see one / building, point at / something fun: / *“Look, a red truck!”* / Sound excited.",
           size=120),
      dict(k="say", f="pink", text="Ignore the people / staring. Shouting / back won't end it, / so *breathe* and / stay close.", size=120),
      dict(k="do", f="butter", text="Next shop, keep it *short* and give your toddler *one job,* like finding the bananas.",
           save="send this to a parent of a two-year-old")],
     "Meltdown in the cereal aisle? Here's what actually helps.\n\n"
     "The NHS says tantrums usually start around 18 months. Your toddler wants to tell you something but doesn't have the words yet.\n\n"
     "The hard part: if you give in to stop it, your child learns that tantrums work. So keep your no, calmly. Shouting back won't end "
     "it either. And if you see one building, distract them straight away: point at something interesting and sound excited.\n\n"
     "Do this: next shop, keep it short and give your toddler one job, like finding the bananas.\n\n"
     "Send this to a parent of a two-year-old.\n\n"
     f"{NOT_MED}\n\n#toddlers #tantrums #parenting #toddlermom #gentleparenting",
     "Source: NHS, Temper tantrums (nhs.uk): tantrums usually start around 18 months; giving in will not help in the long term; "
     "shouting back will not end it; distract early; keep shopping trips short and involve your child.")

# Oct 20, 17:00 · REWRITE (same id) · winter coats and car seats
post("lf-1020-single-coat-check", LF, "2026-10-20T17:00", "suggestion",
     dict(lay="pills", f="butter", text="Puffy coat / in the *car seat?*", obj="shoe", at="bl",
          save="take it off first. here's why."),
     [dict(k="say", f="pink", text="In a crash, a puffy / coat *squashes flat.* / That leaves the / straps loose, and a / child can slip out.",
           size=120, src="American Academy of Pediatrics, healthychildren.org"),
      dict(k="say", f="cream", label="the 2-second check", text="Buckle up, then try / to *pinch the strap* / at the shoulder. / If you can pinch it, / it's too loose.",
           size=120),
      dict(k="do", f="pink", text="Next drive, take the coat off, *buckle up,* then put the coat on backwards *over the straps.*",
           save="send this to whoever does drop-off")],
     "Puffy coat in the car seat? Take it off first.\n\n"
     "The American Academy of Pediatrics explains why: in a crash, the padding in a puffy coat squashes flat. That leaves the straps "
     "loose, and a child can slip out.\n\n"
     "The 2-second check: buckle up, then try to pinch the strap at the shoulder. If you can pinch it, tighten it.\n\n"
     "Do this: next drive, take the coat off, buckle up, then put the coat on backwards over the straps (or tuck a blanket on top).\n\n"
     "Send this to whoever does daycare drop-off.\n\n"
     f"{NOT_MED}\n\n#carseatsafety #winter #newparents #toddlers #babysafety",
     "Source: American Academy of Pediatrics, healthychildren.org, Winter car seat safety tips (bulky coats should not be worn under "
     "the harness; padding flattens in a crash; pinch test; coat on backwards or blanket over the buckled straps).")


# ================================================================== REELS
# Oct 18, 08:00 · REWRITE (same id) · night feeds
reel("lf-reel-1018am-3am-windows", LF, "2026-10-18T08:00", "suggestion", "lf-x-sunny-bounce", "send this to someone doing night feeds", [
    dict(k="hook", f="pink", text="It's 3 am and / baby is *wide awake* / again.", emo="⏰"),
    dict(k="say", f="cream", text="Make night feeds / *boring* on purpose."),
    dict(k="because", f="butter", kicker="here's why", text="It helps baby learn / *night* is different / from *day.*"),
    dict(k="list", f="berry", items=["Lights *low*", "Voice *quiet*", "*Screens* away"], size=120, drop=True),
    dict(k="do", f="cream", text="Tonight, feed by a / *small lamp,* not / the big light."),
    dict(k="save", f="pink", text="send this to someone / doing night feeds"),
], "It's 3 am and the baby is wide awake again.\n\n"
   "Public health guides say to make night feeds calm and boring on purpose: lights down low, voice quiet, screens away. "
   "It helps your baby learn that night is different from day. It takes time, so be gentle with yourselves.\n\n"
   "Do this: tonight, put a small lamp by the feeding chair and leave the big light off.\n\n"
   "Send this to someone doing night feeds.\n\n"
   f"{NOT_MED}\n\n#newborn #nightfeeds #newparents #babysleep #parenting",
   "Source: Public Health Agency (HSC Northern Ireland), Birth to five, Chapter 3: at night keep the lights down low, don't talk much, "
   "keep your voice quiet; teach your baby from the start that night time is different to day time.")

# Oct 18, 19:00 · REWRITE (same id) · crying that won't stop (ICON)
reel("lf-reel-1018-breathe", LF, "2026-10-18T19:00", "tip", "lf-x-tiny-parade", "send this to every new parent", [
    dict(k="hook", f="butter", text="Crying *won't stop* / and you're / at your limit?", emo="🧺"),
    dict(k="because", f="pink", kicker="the NHS says", text="Crying is normal. / It's OK to *walk away* / once baby is *safe.*"),
    dict(k="list", f="berry", items=["Crib, *on their back*", "Step out, *breathe*", "Go back *calmer*"], drop=True),
    dict(k="do", f="cream", text="Save *one number* / to call when / it's too much."),
    dict(k="save", f="butter", text="Never shake a baby. / Send this to / a new parent."),
], "When the crying won't stop, it's OK to step away for a few minutes.\n\n"
   "Lots of crying is normal. It often builds until about 8 weeks, then eases. The NHS ICON advice says: if it's getting to you, put "
   "your baby somewhere safe, like their crib, on their back. Walk away for a few minutes to calm down, then go back and check.\n\n"
   "Do this: today, save one number you can call when it gets too much: your partner, a friend, or your doctor.\n\n"
   "Never, ever shake a baby.\n\n"
   "Send this to every new parent you know.\n\n"
   f"{NOT_MED}\n\n#newborn #crying #newparents #postpartum #parenting",
   "Source: NHS ICON programme (Infant crying is normal; Comfort methods can help; It's OK to walk away if you have checked your baby "
   "is safe; Never, ever shake a baby), Royal Wolverhampton NHS Trust leaflet 'How to manage when a baby cries' (crying may increase "
   "until about 8 weeks).")

# Oct 19, 08:00 · REWRITE (same id) · hunger cues
reel("lf-reel-1019am-hunger-cues", LF, "2026-10-19T08:00", "keep", "lf-x-sunny-bounce", "send this to someone expecting", [
    dict(k="hook", f="pink", text="By the time / baby *cries,* they're / already *very* hungry.", emo="🌙"),
    dict(k="say", f="cream", text="Watch for the / *earlier* signs."),
    dict(k="because", f="butter", kicker="here's why", text="A crying baby needs / *calming* before / they can feed."),
    dict(k="list", f="berry", items=["*Stirring*", "*Mouth* opening", "*Head* turning"], drop=True),
    dict(k="do", f="cream", text="Next feed, watch for / a *mouth opening* or / *head turning.* Feed then."),
    dict(k="save", f="pink", text="send this to / someone expecting"),
], "By the time your baby cries, they're already very hungry.\n\n"
   "NHS feeding guidance says crying is often the last hunger sign. Earlier ones come first: stirring, mouth opening, and turning "
   "their head to search for the breast or bottle. A crying baby usually needs calming before they can feed well.\n\n"
   "Do this: next feed, watch for a mouth opening or head turning, and feed then. Missed them? Every parent does. Calm first, then feed.\n\n"
   "Send this to someone expecting.\n\n"
   f"{NOT_MED}\n\n#newborn #breastfeeding #feeding #newparents #babytips",
   "Source: Cambridge University Hospitals NHS (Rosie Hospital), Tips for successful breastfeeding: when you see early feeding cues, "
   "try to feed as soon as possible; crying is often the last cue, and the baby needs calming before feeding.")

# Oct 19, 19:00 · REPLACES lf-reel-1019-sick-day-plan · kids' money Reel
reel("lf-reel-1019-resp-50-month", LF, "2026-10-19T19:00", "learning", "lf-x-tiny-parade", "send this to a new parent", [
    dict(k="hook", f="cream", text="What *$50 a month* / turns into / by age 18", emo="🐣"),
    dict(k="because", f="butter", kicker="here's how", text="In an RESP, the government / adds *20%,* and it grows / like a *snowball.*"),
    dict(k="num", f="berry", label="by 18, about", value=RESP_18, pre="$", drop=True, min=5),
    dict(k="say", f="cream", text=f"You put in / *${RESP_IN:,}.*"),
    dict(k="do", f="pink", text="This week, ask your bank / to *open an RESP.*"),
    dict(k="save", f="butter", text="send this to / a new parent"),
], f"What $50 a month turns into by the time your baby is 18.\n\n"
   f"Put $50 a month into an RESP from birth. The government adds 20% through the Canada Education Savings Grant, so it's really $60 a "
   f"month. If it grows at 8% a year, that's about ${RESP_18:,} by 18. You put in ${RESP_IN:,}. The rest is the grant and the growth.\n\n"
   f"It's like a snowball: the earlier it starts rolling, the bigger it gets.\n\n"
   f"Do this: this week, ask your bank to open an RESP and set up $50 a month.\n\n"
   f"Send this to a new parent.\n\n"
   f"Assumes 8% a year, compounded monthly, with the 20% grant paid until the year your child turns 17. {NG}\n\n"
   f"#RESP #newparents #babymoney #canadianparents #compoundinterest",
   "Source: " + CESG_SRC + " Growth figure: $50 a month plus the 20% grant, 8% a year compounded monthly for 18 years, grant paid "
   "to the end of the year the child turns 17; rounded down to the nearest $1,000.")

# Oct 20, 08:00 · REWRITE (same id) · baby's movements in pregnancy
reel("lf-reel-1020am-movements", LF, "2026-10-20T08:00", "tip", "lf-x-giggle-pop", "send this to someone expecting", [
    dict(k="hook", f="pink", text="Baby in your bump / moving *less* / than usual?", emo="🫶"),
    dict(k="say", f="cream", text="Don't wait to see / if it's better / *tomorrow.*"),
    dict(k="because", f="butter", kicker="the NHS says", text="Call your midwife or / hospital *right away,* / even at *night.*"),
    dict(k="list", f="berry", items=["Moving *less*", "Not moving", "A *new pattern*"], drop=True),
    dict(k="do", f="cream", text="Today, save your / *hospital's birth unit* / number in your phone."),
    dict(k="save", f="pink", text="send this to / someone expecting"),
], "Baby moving less than usual today? Don't wait until tomorrow.\n\n"
   "The NHS says to call your midwife or maternity unit right away if your baby is moving less than usual, you can't feel them moving, "
   "or their usual pattern changes. Even in the middle of the night. You are never a bother.\n\n"
   "Do this: today, save your hospital's birth unit number in your phone.\n\n"
   "Send this to someone expecting.\n\n"
   f"{NOT_MED}\n\n#pregnancy #babymovements #pregnant #thirdtrimester #midwife",
   "Source: NHS, Your baby's movements (nhs.uk): call your midwife or maternity unit immediately if your baby is moving less than "
   "usual, you cannot feel your baby moving anymore, or there is a change to the usual pattern. Do not wait until the next day.")

# Oct 20, 19:00 · REWRITE (same id) · visitors and cold sores
reel("lf-reel-1020-visitors", LF, "2026-10-20T19:00", "suggestion", "lf-x-sunny-bounce", "send this to the family group chat", [
    dict(k="hook", f="cream", text="Visitors coming / to see the *baby?*", emo="🫶"),
    dict(k="say", f="pink", text="A cold sore can pass / to a baby through / *one kiss.*"),
    dict(k="because", f="butter", kicker="here's why", text="Newborns can't fight / it off well. It can / get *serious.*"),
    dict(k="list", f="berry", items=["*Wash* hands", "*No* kisses", "Sick? *Visit later*"], drop=True),
    dict(k="do", f="cream", text="Text your visitors: / *“Wash hands, no kisses, / come when well.”*"),
    dict(k="save", f="pink", text="send this to the / family chat"),
], "Visitors coming to meet the new baby? One small ask keeps them safe.\n\n"
   "The NHS says a cold sore can pass to a baby through a kiss, and it can be very serious for a newborn, whose immune system isn't "
   "ready to fight it yet. Anyone with a cold sore shouldn't kiss the baby, and everyone should wash their hands first.\n\n"
   "Do this: today, text your visitors: \"Wash hands, no kisses, come when you're well.\"\n\n"
   "Send this to the family group chat.\n\n"
   f"{NOT_MED}\n\n#newborn #newparents #visitors #babysafety #parenting",
   "Source: NHS, Neonatal herpes (nhs.uk): the virus can pass to a baby through a cold sore when someone kisses them; herpes can be "
   "very serious for a young baby; wash hands before handling the baby; don't kiss the baby if you have a cold sore.")


# ================================================================== STORY CHAINS (hook photo -> mini-story -> payoff -> today's post)
# Oct 18 · REPLACES lf-ch-1018 · hands off to lf-1018-resp-free-500
chain("lf-ch-1018-resp", LF, "2026-10-18", "lf18", "baby money · part 1", [
    dict(k="photo", text="“Should we be / saving for *her* / already?”", sub="the government *will help* →", ink="light", y=620),
    dict(k="bubbles", f="cream", label="10 pm, on the couch", bubbles=[
        ("in", "should we start saving for the baby's school?"),
        ("out", "we barely have anything left over 😅"),
        ("in", "even a little gets *20% added* by the government")], obj="shoe"),
    dict(k="payoff", f="butter", label="it's called the education savings grant", text="Save $100. / *Get $20 added.*",
         sub="up to $500 every year", obj="clock"),
    dict(k="handoff", f="cream", text="Your baby's / *$500 a year*", img="lf-1018-resp-free-500/01.jpg", next="part 2 tomorrow"),
])

# Oct 19 · REPLACES lf-ch-1019 · hands off to lf-1019-learning-bond
chain("lf-ch-1019-clb", LF, "2026-10-19", "lf19", "baby money · part 2", [
    dict(k="photo", text="“We can't / afford to save / *right now.*”", sub="some help needs *no deposit* →", ink="dark", y=560),
    dict(k="bubbles", f="cream", label="a text from a friend", bubbles=[
        ("in", "we can't afford to put anything in an RESP"),
        ("out", "you might not have to"),
        ("out", "the *Canada Learning Bond* adds up to *$2,000.* no deposit.")], obj="ok"),
    dict(k="payoff", f="butter", label="families with 1 to 3 kids can qualify", text="Net income / *$57,375* or less",
         sub="July 2025 to June 2026", obj="point"),
    dict(k="handoff", f="cream", text="Up to / *$2,000,* / no deposit", img="lf-1019-learning-bond/01.jpg", next="who qualifies, inside"),
])

# Oct 20 · REWRITE (same id) · hands off to lf-06-toddler-meltdown
chain("lf-ch-1020", LF, "2026-10-20", "lf20", "calmer toddler days", [
    dict(k="photo", text="“Not in the / *cereal aisle…*”", sub="here's what *actually helps* →", ink="light", y=1050),
    dict(k="bubbles", f="cream", label="the parents' group chat", bubbles=[
        ("in", "she screamed until I gave her the cookie"),
        ("out", "been there. but giving in teaches her *tantrums work*"),
        ("out", "next time, keep your no. *calmly.*")], obj="ok"),
    dict(k="payoff", f="butter", label="see one building? point at something fun", text="“Look, a / *big red truck!*”",
         sub="sound excited", obj="shoe"),
    dict(k="handoff", f="cream", text="Calmer / *meltdowns*", img="lf-06-toddler-meltdown/01.jpg", next="save it for the next shop"),
])

"""Littlefold content, Oct 18-21. Rewritten Oct 17 night to the ONE-READ standard (/home/claude/one-read-standard.md).
Uses post()/reel()/chain() from specs_teach. Only this page's entries live here.
Kids' money figures checked on canada.ca (Oct 17): CESG 20% on the first $2,500 a year (max $500/yr basic, $7,200 lifetime,
catch-up up to $1,000 a year); CLB $500 + $100/yr up to $2,000, no contribution, born 2004+, ADFNI <= $58,523 for 1-3 kids
(Jul 2026 - Jun 2027, ESDC notice 2026-1138)."""
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
           "July 2026 to June 2027: adjusted family net income of $58,523 or less for 1 to 3 children (ESDC notice 2026-1138).")

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
     [dict(k="say", f="butter", text="It's called the / *Canada Learning* / *Bond.* You don't / add a cent.",
           size=124),
      dict(k="say", f="pink", text="*$500* to start. / *$100* more / each year. / Up to *$2,000.*",
           size=128, src="canada.ca, Canada Learning Bond"),
      dict(k="say", f="cream", label="who qualifies", text="1 to 3 kids, and / family net income / of *$58,523* / or less.",
           sub="for July 2026 to June 2027", size=124),
      dict(k="say", f="butter", label="the part nobody tells you", text="Missed it? / Kids born *2004* / *or later* can apply / *before 21.*",
           size=124),
      dict(k="do", f="pink", text="This week, ask your bank for a *free RESP* with the Learning Bond. Bring your child's SIN.",
           save="send this to a parent who should check")],
     "Up to $2,000 for your child's education, and you don't have to put in a cent.\n\n"
     "It's called the Canada Learning Bond. The government puts $500 into your child's RESP, then $100 for each year your family "
     "qualifies, up to $2,000. No deposit is needed.\n\n"
     "Who can get it: for July 2026 to June 2027, families with 1 to 3 children and an adjusted family net income of $58,523 or less. "
     "Children born in 2004 or later can apply any time before they turn 21, so it's not too late if you missed it. In 2022, only about "
     "4 in 10 eligible kids had received it.\n\n"
     "Do this: this week, ask your bank for a free RESP with the Canada Learning Bond. Bring your child's SIN.\n\n"
     "Send this to a parent who should check.\n\n"
     "#RESP #CanadaLearningBond #newparents #canadianparents #babymoney",
     "Source: " + CLB_SRC + " Take-up: C.D. Howe Institute (Godbout & Samoisette), citing ESDC's 2022 Canada Education Savings Program "
     "statistical review: 42.5% of eligible children had received the bond in 2022, up from 29.1% in 2013.")

# Oct 19, 17:00 · REWRITE (same id) · fever under 3 months
post("lf-1019-single-fever-under-3m", LF, "2026-10-19T17:00", "keep",
     dict(lay="pills", f="pink", text="Baby under / 3 months / *with a fever?*", obj="point", at="bl",
          save="this one can't wait for morning", src="American Academy of Pediatrics"),
     [dict(k="say", f="butter", text="Under 3 months / and *38°C* or higher? / Call the doctor / *right away.*",
           size=128, src="American Academy of Pediatrics, healthychildren.org"),
      dict(k="say", f="cream", text="This rule is / for the *first* / *3 months.* / Don't wait to see / if it passes.",
           size=124),
      dict(k="do", f="pink", text="Today, save your doctor's *after-hours number.* Can't reach anyone? Go to *emergency.*",
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
     [dict(k="say", f="pink", text="Tantrums often / start around / *18 months.* / They don't have / the words yet.",
           size=124, src="NHS, Temper tantrums"),
      dict(k="say", f="butter", label="here's the hard part", text="Give in, and / they learn / *tantrums work.* / So keep your no, / calmly.",
           size=124),
      dict(k="say", f="cream", label="catch it early", text="See one building? / Point at / something fun: / *“Look, a red truck!”*",
           size=124),
      dict(k="say", f="pink", text="Ignore the stares. / *Breathe,* and / stay close.", size=132),
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
     [dict(k="say", f="pink", text="In a crash, / a puffy coat / *squashes flat.* / The straps end up / *loose.*",
           size=124, src="American Academy of Pediatrics, healthychildren.org"),
      dict(k="say", f="cream", label="the 2-second check", text="Buckle up. Then / *pinch the strap* / at the shoulder. / Can you pinch it? / Too loose.",
           size=120),
      dict(k="do", f="pink", text="Take the coat off, *buckle up,* then put the coat on backwards *over the straps.*",
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

# Oct 21, 11:30 · NEW · kids' money: naming a guardian in your will
WILL_SRC = ("Sources: Angus Reid Institute (January 2018): 51% of Canadians say they do not have a will. Ontario: under the Children's "
            "Law Reform Act, a parent can appoint in a will a person to care for their children after death; the appointment is "
            "temporary (90 days) and the person must then apply to court. Rules differ by province. General information, not legal advice.")

post("lf-1021-name-a-guardian", LF, "2026-10-21T11:30", "learning",
     dict(lay="pills", f="pink", kicker="baby money · the big one", text="Who would / raise *your kids?*", obj="point", at="bl",
          save="a hard question, a 2-minute talk"),
     [dict(k="say", f="butter", label="the question nobody asks", text="If something / happened to / you both, who / would *raise* / *your kids?*",
           size=124),
      dict(k="say", f="cream", text="You can write / your answer down. / You *name a guardian* / in your will.", size=124),
      dict(k="say", f="pink", text="Yet this many / Canadians say they / have *no will:*", num="51%", size=124,
           src="Angus Reid Institute, 2018"),
      dict(k="say", f="butter", label="without one", text="Your family has / to ask a court, and / *your wish isn't* / *written down.*",
           size=124),
      dict(k="say", f="cream", label="start tonight", text="Ask your partner: / *who would we pick?* / Then ask them / if they'd say yes.",
           size=124),
      dict(k="do", f="pink", text="This week, book a call with a *wills lawyer.* Bring the name you both chose.",
           save="send this to your partner")],
     "Who would raise your kids if something happened to you both? It's the question nobody wants to ask.\n\n"
     "Your will is where you write the answer down: you can name a guardian, the person you'd trust to raise them. Yet 51% of Canadians "
     "say they have no will at all. Without one, your family has to go to court, and your wish isn't written down anywhere.\n\n"
     "Start small: tonight, ask your partner who you'd pick. Then ask that person if they'd say yes.\n\n"
     "Do this: this week, book a call with a wills lawyer, and bring the name you both chose.\n\n"
     "Rules differ by province. General information, not legal advice.\n\n"
     "Send this to your partner.\n\n#wills #guardianship #newparents #canadianparents #estateplanning",
     WILL_SRC)



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
chain("lf-ch-1019-clb", LF, "2026-10-19", "lf19", "baby money · part 2", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="cream", label="quick quiz", title="A *free $2,000* / for kids' school…", bubbles=[
        ("in", "how many eligible kids actually get it?"), ("out", "A) about 9 in 10"), ("out", "B) about 4 in 10")],
         obj="shoe", tap="guess, then tap →"),
    dict(k="payoff", f="butter", label="the answer: B", text="Only / *42.5%*", sub="of eligible kids had it in 2022", obj="point",
         tap="source: C.D. Howe Institute, ESDC data · tap →"),
    dict(k="payoff", f="pink", label="why it matters", text="Open the RESP. / *Get the bond.*", sub="most families just never opened one",
         obj="clock", tap="next story →"),
    dict(k="handoff", f="cream", text="Up to / *$2,000,* / no deposit", img="lf-1019-learning-bond/01.jpg", next="who qualifies, inside"),
])

# Oct 20 · REWRITE (same id) · hands off to lf-06-toddler-meltdown
chain("lf-ch-1020", LF, "2026-10-20", "lf20", "calmer toddler days", [
    dict(k="photo", text="“Not in the / *cereal aisle…*”", sub="here's what *actually helps* →", ink="light", y=1050),
    dict(k="bubbles", f="cream", label="the parents' group chat", bubbles=[
        ("in", "she screamed until I gave her the cookie"),
        ("out", "been there. but now she knows *tantrums work*"),
        ("out", "next time, keep your no. *calmly.*")], obj="ok"),
    dict(k="payoff", f="butter", label="see one building? point at something fun", text="“Look, a / *big red truck!*”",
         sub="sound excited", obj="shoe"),
    dict(k="handoff", f="cream", text="Calmer / *meltdowns*", img="lf-06-toddler-meltdown/01.jpg", next="save it for the next shop"),
])

# Oct 21 · NEW · day B: guess-and-reveal quiz -> lf-1021-name-a-guardian
chain("lf-ch-1021", LF, "2026-10-21", "lf21", "baby money · the big one", [
    dict(k="bubbles", f="cream", label="quick quiz", title="Canadians / with *no will…*", bubbles=[
        ("in", "what share say they don't have one?"), ("out", "A) about 1 in 10"), ("out", "B) about half")],
         obj="shoe", tap="guess, then tap →"),
    dict(k="payoff", f="butter", label="the answer: B", text="*51%*", sub="say they have no will", obj="point",
         tap="source: Angus Reid Institute, 2018 · tap →"),
    dict(k="payoff", f="pink", label="why it matters", text="A will is where / you *name a guardian.*", sub="the person who'd raise your kids",
         obj="ok", tap="next story →"),
    dict(k="handoff", f="cream", text="Who would / raise *your kids?*", img="lf-1021-name-a-guardian/01.jpg", next="a 2-minute talk tonight"),
])


# ================================================================== Oct 22 (11:30 is reserved for the orchestrator's travelling carousel)
CCB_SRC = ("Source: CRA (canada.ca), RC4476-ON, Birth Registration and Canada Child Benefits (Ontario): register online with "
           "ServiceOntario's Newborn Registration Service and choose the option 'Canada child benefits'; with your consent your "
           "information goes to the CRA, and you should not re-apply through CRA My Account or Form RC66. The primary caregiver "
           "applies and gives their SIN. Maximum CCB, July 2026 to June 2027: up to $8,157 a year per child under 6 (canada.ca; "
           "income-tested).")

reel("lf-reel-1022-ccb-at-birth", LF, "2026-10-22T19:00", "learning", "lf-x-tiny-parade", "send this to someone expecting", [
    dict(k="hook", f="pink", text="New baby in Ontario? / *One click* starts / your Child Benefit.", emo="🍼"),
    dict(k="say", f="cream", text="Register the birth / online, and tick / *Canada child* / *benefits.*"),
    dict(k="because", f="butter", kicker="here's why", text="Your info goes *straight to the CRA.* No extra form."),
    dict(k="say", f="berry", text="Then *don't* / *apply again.*", drop=True),
    dict(k="do", f="cream", text="Have the main caregiver's *SIN* ready when you register."),
    dict(k="save", f="pink", text="send this to / someone expecting"),
], "New baby in Ontario? One click can start your Canada Child Benefit.\n\n"
   "When you register the birth online with ServiceOntario's Newborn Registration Service, choose the option \"Canada child benefits\". "
   "With your OK, your information goes straight to the CRA, so there's no separate form. Then don't apply again: the CRA already has it.\n\n"
   "Why it matters: the benefit can be up to $8,157 a year for a child under 6 (July 2026 to June 2027, less as family income rises).\n\n"
   "Do this: have the main caregiver's SIN ready when you register the birth. The main caregiver is the parent who applies.\n\n"
   "Send this to someone expecting a baby.\n\n#newparents #canadachildbenefit #ontarioparents #babymoney #expectingparents",
   CCB_SRC)


SLEEP_SRC = ("Sources: Health Canada, Safe sleep for your baby (canada.ca): put your baby to sleep on their back, every time, including "
             "naps; use a crib, cradle or bassinet that meets current Canadian regulations, with a firm, flat mattress and only a fitted "
             "sheet (no pillows, quilts, comforters, bumper pads or toys); room-share (baby in their own sleep space in your room) for at "
             "least the first 6 months. Canadian Paediatric Society, caringforkids.cps.ca, Safe sleep for babies: same guidance.")

# Oct 22, 17:00 · NEW · safe sleep (the 11:30 slot belongs to the orchestrator)
post("lf-1022-safe-sleep", LF, "2026-10-22T17:00", "learning",
     dict(lay="pills", f="pink", kicker="safe sleep", text="Where should / baby *sleep?*", obj="ok", at="bl",
          save="Health Canada's rules, in one look"),
     [dict(k="rows", f="cream", text="Every sleep, *naps too*", cap="Health Canada's safe sleep basics",
           rows=[("Position", "On their back"), ("Where", "Own crib, your room"), ("Mattress", "Firm and flat"),
                 ("In the crib", "Only a fitted sheet")],
           src="Health Canada · Canadian Paediatric Society"),
      dict(k="say", f="butter", label="the part people miss", text="Share your *room,* / not your *bed,* / for at least the / first *6 months.*",
           sub="baby close by, in their own crib", src="Health Canada, Safe sleep for your baby"),
      dict(k="do", f="pink", text="Tonight, take *everything* out of the crib except the fitted sheet.",
           save="send this to someone expecting")],
     "Where should your baby sleep? Health Canada keeps it simple.\n\n"
     "Every sleep, naps too: on their back, in their own crib, cradle or bassinet, on a firm, flat mattress, with nothing in there but a "
     "fitted sheet. No pillows, blankets, bumpers or toys.\n\n"
     "The part people miss: keep baby's crib in your room for at least the first 6 months. Share your room, not your bed.\n\n"
     "Do this: tonight, take everything out of the crib except the fitted sheet. A sleep sack can keep them warm instead of a blanket.\n\n"
     "Send this to someone expecting.\n\n"
     f"{NOT_MED}\n\n#safesleep #newborn #newparents #canadianparents #babysleep",
     SLEEP_SRC)

chain("lf-ch-1022", LF, "2026-10-22", "lf22", "safe sleep", [
    dict(k="photo", text="“She *finally* / fell asleep / on me.”", sub="do I move her? *yes* →", ink="light", y=1000),
    dict(k="bubbles", f="cream", label="2 am, the group chat", bubbles=[
        ("in", "she fell asleep on my chest. do I move her?"), ("out", "yes. gently, on her back, in her crib"),
        ("out", "and *nothing* else in there. no blanket, no toys")], obj="shoe"),
    dict(k="payoff", f="butter", label="Health Canada's rule", text="On her *back.* / Own crib. / *Nothing else.*",
         sub="every sleep, naps too", obj="ok"),
    dict(k="handoff", f="cream", text="Where should / baby *sleep?*", img="lf-1022-safe-sleep/01.jpg", next="the rules, in one look"),
], times=["16:30", "16:31", "16:32", "17:15"])


# ================================================================== Oct 23 (day B: quiz) · RESP catch-up + screens before bed
SCREEN_SRC = ("Source: Canadian Paediatric Society, Screen time and young children: promoting health and development in a digital "
              "world (2017, reaffirmed), and caringforkids.cps.ca: avoid screens for at least 1 hour before bedtime; keep daily "
              "screen-free times, especially family meals and book-sharing.")

reel("lf-reel-1023am-screens-bed", LF, "2026-10-23T08:00", "tip", "lf-x-giggle-pop", "send this to someone in bedtime battles", [
    dict(k="hook", f="butter", text="Bedtime battles / *every night?*", emo="🌙"),
    dict(k="say", f="cream", text="Screens right before / bed can make it / *harder* to settle."),
    dict(k="because", f="pink", kicker="here's why", text="Canada's paediatricians say *no screens* in the hour before bed."),
    dict(k="say", f="berry", text="Swap that hour / for a *book* / *together.*", drop=True),
    dict(k="do", f="cream", text="Tonight, put the tablet *away 1 hour* before bed."),
    dict(k="save", f="pink", text="send this to someone / in bedtime battles"),
], "Bedtime battles every night? Look at the hour before bed.\n\n"
   "The Canadian Paediatric Society says to avoid screens for at least 1 hour before bedtime, and to keep screen-free times every day, "
   "especially meals and reading together.\n\n"
   "Do this: tonight, put the tablet and TV away 1 hour before bed. Swap it for a book together.\n\n"
   "Send this to someone in bedtime battles.\n\n"
   f"{NOT_MED}\n\n#toddlerlife #bedtimeroutine #screentime #canadianparents #toddlersleep",
   SCREEN_SRC)

post("lf-1023-resp-catch-up", LF, "2026-10-23T11:30", "learning",
     dict(lay="pills", f="butter", kicker="baby money", text="Never opened / an *RESP?*", obj="point", at="bl",
          save="it's not too late"),
     [dict(k="say", f="cream", label="the part nobody tells you", text="Grant room builds / *every year* from birth, / even with *no RESP.*",
           src="canada.ca, Canada Education Savings Grant"),
      dict(k="say", f="pink", text="Start late, and / the government can / add up to:", num="$1,000",
           sub="a year, until the full $7,200 is used", src="canada.ca, Canada Education Savings Grant"),
      dict(k="do", f="butter", text="This week, ask your bank to open an RESP and *use your catch-up room.*",
           save="send this to a parent who never opened one")],
     "Never opened an RESP? It's not too late.\n\n"
     "The part nobody tells you: your child's grant room builds up every year from birth, even if you never opened an RESP. "
     "The government matches 20% of what you save. Usually that's up to $500 a year, but with unused room it can add up to $1,000 a year "
     "(when you put in $5,000), until the full $7,200 per child is used. Grants stop at the end of the year your child turns 17.\n\n"
     "Do this: this week, ask your bank to open an RESP and use your catch-up room. Bring your child's SIN.\n\n"
     "Tonight at 7: how much you can still get, by your child's age.\n\n"
     "Send this to a parent who never opened one.\n\n#RESP #canadianparents #savingforkids #CESG #babymoney",
     "Source: " + CESG_SRC + " Children aged 16 or 17 qualify only if at least $2,000 was contributed before the end of the year they "
     "turned 15, or $100 a year in any 4 earlier years.")

chain("lf-ch-1023", LF, "2026-10-23", "lf22", "baby money", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="cream", label="quick quiz", title="Free RESP money, / *per child…*", bubbles=[
        ("in", "what's the most grant one child can get?"), ("out", "A) $2,500"), ("out", "B) $7,200")],
         obj="shoe", tap="guess, then tap →"),
    dict(k="payoff", f="butter", label="the answer: B", text="*$7,200*", sub="per child, over the years", obj="point",
         tap="source: canada.ca · tap →"),
    dict(k="payoff", f="pink", label="why it matters", text="Started late? / You can *catch up.*", sub="up to $1,000 of grant a year",
         obj="clock", tap="next story →"),
    dict(k="handoff", f="cream", text="Never opened / an *RESP?*", img="lf-1023-resp-catch-up/01.jpg", next="by age: tonight at 7"),
])


# ================================================================== Oct 24 (Story chain day; 08:00 = lf-pan-1024am-newborn-bundle)
# Facts checked Oct 18 pm (sources in each first comment).
HONEY_SRC = ("Source: Health Canada (canada.ca), Infant botulism: 'Do not give any type of honey to infants (babies who are less than "
             "one year old)'; 'Never add honey to an infant's food, water, formula, or soother.' Spores can be in pasteurized and "
             "unpasteurized honey and resist heat. Contact your doctor immediately if a baby has constipation, weak muscles, is too "
             "weak to cry or suck as usual, has a wobbly head, trouble breathing or can't swallow. After 1, healthy children's gut "
             "bacteria protect them.")
GRAN_SRC = ("Sources: canada.ca, 'How the RESP and related benefits work together': 'Any adult can open an RESP account for a child: "
            "parents, guardians, grandparents, other relatives, and friends'; contributions are needed to receive the CESG. "
            + CESG_SRC + " The grant limits are per child, across all of that child's RESPs.")

chain("lf-ch-1024", LF, "2026-10-24", "lf18", "baby safety", [
    dict(k="photo", text="“Just a little / honey on / *the soother?*”", sub="not before age 1 →", ink="light", y=620),
    dict(k="bubbles", f="cream", label="sound familiar?", bubbles=[
        ("in", "grandma says honey helps her settle 🍯"), ("out", "not before her *first birthday*"), ("in", "even a tiny bit?")],
         obj="shoe"),
    dict(k="bubbles", f="pink", label="here's why", bubbles=[
        ("out", "honey can carry *botulism spores*"), ("out", "a baby's tummy can't fight them yet"),
        ("out", "and cooking *doesn't* kill them")]),
    dict(k="payoff", f="butter", label="Health Canada's rule", text="*No honey* / before 1.", sub="not in food, water, formula or soothers",
         obj="ok"),
    dict(k="handoff", f="cream", text="Honey for baby? / *Not yet.*", img="lf-1024-no-honey/01.jpg", next="the rule, in one look"),
])

post("lf-1024-no-honey", LF, "2026-10-24T11:30", "learning",
     dict(lay="pills", f="butter", kicker="baby safety", text="Honey for baby? / *Not before 1.*", obj="ok", at="bl",
          save="not even a tiny bit"),
     [dict(k="rows", f="cream", text="*No honey* before 1", cap="Health Canada",
           rows=[("In food", "no"), ("In water or formula", "no"), ("On a soother", "no"), ("Cooked or pasteurized", "still no")],
           src="Health Canada, Infant botulism"),
      dict(k="say", f="pink", label="here's why", text="Honey can carry / *botulism* spores. / A baby's gut / can't fight them *yet.*",
           sub="after 1, healthy kids are fine", src="Health Canada, Infant botulism"),
      dict(k="do", f="butter", text="Today, check baby's snacks and cereals for *honey* on the label. Then tell the grandparents.",
           save="send this to the grandparents")],
     "Honey for baby? Not before their first birthday. Not even a tiny bit.\n\n"
     "Health Canada says: no honey of any kind for babies under 1. Not in food, water or formula, and never on a soother. "
     "Cooked or pasteurized honey isn't safe either.\n\n"
     "Here's why: honey can carry botulism spores. Heat doesn't kill them, and a baby's gut can't fight them yet. After age 1, "
     "healthy kids have the gut bacteria to handle them.\n\n"
     "Call your doctor right away if a baby is constipated, floppy, too weak to cry or suck as usual, or has trouble breathing or swallowing.\n\n"
     "Do this: today, check baby's snacks and cereals for honey on the label. Then tell the grandparents.\n\n"
     f"Send this to the grandparents.\n\n{NOT_MED}\n\n#babyfood #newparents #canadianparents #babysafety #startingsolids",
     HONEY_SRC)

reel("lf-reel-1024-grandma-resp", LF, "2026-10-24T19:00", "learning", "lf-x-tiny-parade", "send this to grandma", [
    dict(k="hook", f="pink", text="Grandma's gift / could get a / *20% top-up.*", emo="🎂"),
    dict(k="say", f="cream", text="Put her *$100* / in the *RESP.*"),
    dict(k="because", f="butter", kicker="here's why", text="The government adds *20%.* So $100 becomes *$120.*"),
    dict(k="say", f="berry", text="Up to *$500* / a year, / *per child.*", drop=True),
    dict(k="do", f="cream", text="This birthday, ask for *gift money in the RESP.*"),
    dict(k="save", f="pink", text="send this to / grandma"),
], "Grandma's birthday money could get a 20% top-up.\n\n"
   "Put her $100 in your child's RESP, and the Canada Education Savings Grant adds $20. The government matches 20% of what goes in, "
   "up to $500 a year and $7,200 per child in total. Then it all grows until school.\n\n"
   "Did you know? Any adult can open an RESP for a child, grandparents included. The grant limit is per child, though, so it's "
   "shared across all of that child's RESPs.\n\n"
   "Do this: this birthday, ask family for gift money in the RESP, and deposit it at your bank.\n\n"
   "Send this to grandma.\n\n#RESP #grandparents #canadianparents #savingforkids #babymoney",
   GRAN_SRC)


# ================================================================== Oct 25 (day B: quiz · Reels carry the crying lesson, part 1 -> 2)
CRY_SRC = ("Sources: NHS (South Tees Hospitals, ICON 'Babies cry, you can cope'): crying often starts around 2 weeks, peaks at around "
           "6 to 8 weeks for a term baby, then gradually decreases; 'It's OK to walk away if you have checked the baby is safe and the "
           "crying is getting to you'; 'Never ever shake or hurt a baby.' NHS, 'Soothing a crying baby': if it's overwhelming, put "
           "baby safely in their cot, step into another room for a set time like 10 minutes, then go back; contact a doctor if baby "
           "seems unwell or the cry doesn't sound like their normal cry.")

reel("lf-reel-1025am-crying-peak", LF, "2026-10-25T08:00", "tip", "lf-x-sunny-bounce", "send this to someone in the newborn weeks", [
    dict(k="hook", f="butter", text="Baby crying / *more* each week?", emo="🍼"),
    dict(k="say", f="cream", text="It often starts / building around / *2 weeks.*"),
    dict(k="because", f="pink", kicker="the NHS says", text="It usually peaks at *6 to 8 weeks.* Then it eases."),
    dict(k="say", f="berry", text="It's a *normal* / *stage.*", drop=True),
    dict(k="do", f="cream", text="Today, ask someone to take *one hour* so you can rest."),
    dict(k="save", f="pink", text="send this to / a new parent", next="part 2 tonight at 7"),
], "Baby crying more every week? You're not alone.\n\n"
   "The NHS says crying often starts building around 2 weeks, usually peaks around 6 to 8 weeks, and then slowly eases. "
   "It's a normal stage, not a sign you're doing it wrong.\n\n"
   "If the cry sounds different from usual, or baby seems unwell (fever, not feeding), call your doctor or your health line "
   "(811 in most provinces).\n\n"
   "Do this: today, ask someone to take one hour so you can rest. Asking for help is normal.\n\n"
   f"Send this to someone in the newborn weeks. Part 2 tonight at 7.\n\n{NOT_MED}\n\n"
   "#newborn #newparents #babycrying #canadianparents #fourthtrimester",
   CRY_SRC, series="Crying · part 1/2")

chain("lf-ch-1025", LF, "2026-10-25", "lf22", "calmer newborn days", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="cream", label="quick quiz", title="Newborn crying / *peaks* at…", bubbles=[
        ("in", "when is it usually worst?"), ("out", "A) the first week"), ("out", "B) 6 to 8 weeks")],
         obj="shoe", tap="guess, then tap →"),
    dict(k="payoff", f="butter", label="the answer: B", text="*6 to 8* / weeks", sub="then it slowly eases", obj="point",
         tap="source: NHS · tap →"),
    dict(k="payoff", f="pink", label="so for now", text="Try one thing / *at a time.*", sub="feed, diaper, cuddle", obj="clock",
         tap="next story →"),
    dict(k="handoff", f="cream", text="Baby won't stop / *crying?*", img="lf-1025-follow-crying/01.jpg", next="follow your line"),
])

reel("lf-reel-1025-step-away", LF, "2026-10-25T19:00", "suggestion", "lf-x-tiny-parade", "send this to every new parent", [
    dict(k="hook", f="pink", text="Crying won't stop. / You're *at* / *your limit.*", emo="🤍"),
    dict(k="say", f="cream", text="It's OK to / *step away.*"),
    dict(k="because", f="butter", kicker="the NHS says", text="Put baby *on their back* in the crib. Step out *10 minutes.*"),
    dict(k="say", f="berry", text="*Never* shake / a baby.", drop=True),
    dict(k="do", f="cream", text="Tonight, pick the *person you'll text* when it's too much."),
    dict(k="save", f="pink", text="send this to / every new parent", next="crying · part 2/2"),
], "Crying won't stop, and you're at your limit? That happens to loving parents too.\n\n"
   "The NHS says it's OK to step away. Put baby down safely on their back in the crib, close the door, and go to another room for "
   "a set time, like 10 minutes. Breathe. Then go back.\n\n"
   "And never shake a baby. Shaking can cause brain damage.\n\n"
   "If baby seems unwell, or the cry sounds different, call your doctor or your health line (811 in most provinces).\n\n"
   "Do this: tonight, pick your step-away person, the one you'll text when it's too much.\n\n"
   f"Send this to every new parent. Part 2 of 2.\n\n{NOT_MED}\n\n#newparents #newborn #babycrying #parentingsupport #canadianparents",
   CRY_SRC, series="Crying · part 2/2")


# ------------------------------------------------------------------ AIR PASS (Oct 18 am): size each Oct 19-21 slide to its longest line,
# so forced line breaks never re-wrap (one line on screen = one line in the source).
def _fit_sizes(brand, em=0.45, cap=136, floor=88):
    """AIR PASS: keep the hand-written line breaks and pick each slide's size so its longest line fits the 920px text box
    (em = average glyph width for this page's serif) and all its lines fit the box height. Then nothing re-wraps.
    Oct 19-21 feed slides only."""
    import re as _re
    from specs_teach import POSTS, META

    def _len(s):
        return len(_re.sub(r"\*", "", s)) + 2 * len(_re.findall(r"[\U0001F300-\U0001FAFF]", s))

    for _pid, _sp in POSTS.items():
        if _sp["brand"] != brand or META[_pid]["at"][:10] not in ("2026-10-19", "2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24"):
            continue
        for _s in _sp["slides"]:
            if _s.get("k") in ("do", "rows", "steps"):
                continue
            lines = _s["text"].split(" / ")
            box_h = 430 if (_s.get("num") or _s.get("bars")) else 540
            w = 900 / (em * max(_len(x) for x in lines))
            h = box_h / (0.9 * len(lines))
            _s["size"] = int(max(floor, min(cap, w, h)))



_fit_sizes(LF)

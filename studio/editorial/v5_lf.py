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

# Oct 19, 11:30 · DEPTH REWRITE (same id, Oct 19 00:25) · kids' money part 2 (part 1 aired Oct 18 promising "part 2 tomorrow:
# the money some families get with no deposit at all"). Watch-it-grow table, who qualifies, retroactive, 4 steps, the exact words.
# Rule that stays: "No deposit. Just the account."
post("lf-1019-learning-bond", LF, "2026-10-19T11:30", "deep",
     dict(lay="sticky", f="cream", kicker="baby money · part 2", text="Up to / *$2,000,* / no deposit",
          obj="point", at="bl", items=["$500 to start", "$100 a year after", "Into your child's RESP"], save="who qualifies + 3 steps"),
     [dict(k="say", f="butter", label="yesterday: the 20% grant", text="Today: money / your child can get / *without you* / *saving a cent.*"),
      dict(k="say", f="pink", text="It's called the / *Canada Learning* / *Bond.* The government / puts it straight / into an *RESP.*",
           src="canada.ca, Canada Learning Bond"),
      dict(k="rows", f="cream", text="Watch it *grow*", cap="if your family qualifies every year",
           rows=[("First year", "$500"), ("Age 5", "$1,000"), ("Age 10", "$1,500"), ("Age 15", "$2,000")],
           src="canada.ca, Canada Learning Bond"),
      dict(k="say", f="butter", label="who qualifies", text="1 to 3 kids, and / family net income / of *$58,523* / or less.",
           sub="July 2026 to June 2027 · higher limit for 4+ kids"),
      dict(k="say", f="pink", label="the part nobody tells you", text="*It's retroactive.* / Missed years / can still be paid, / up to *$2,000.*",
           sub="parents ask before 18, kids before 21", src="canada.ca, Canada Learning Bond"),
      dict(k="steps", f="cream", text="Get it in *3 steps*",
           items=["Get your child a SIN", "Open an RESP, no deposit", "Ask for the Learning Bond"]),
      dict(k="say", f="butter", label="then one habit: file taxes", text="The bond checks / your income / *every year.* / No tax return, / *no $100.*"),
      dict(k="do", f="pink", text="This week, call your bank and say: *“I'd like a no-fee RESP with the Canada Learning Bond.”*",
           save="send this to a parent who should check")],
     "Up to $2,000 for your child's education, and you don't have to put in a cent. Part 2 of baby money.\n\n"
     "Yesterday was the 20% grant you get when you save. Today is the one you get without saving: the Canada Learning Bond. "
     "The government puts it straight into your child's RESP.\n\n"
     "WATCH IT GROW (if your family qualifies every year):\n"
     "• First year: $500\n• Age 5: $1,000\n• Age 10: $1,500\n• Age 15: $2,000 (the maximum)\n\n"
     "WHO QUALIFIES (July 2026 to June 2027): children born in 2004 or later, in families with 1 to 3 children and an adjusted family "
     "net income of $58,523 or less. The limit is higher for 4 or more children.\n\n"
     "THE PART NOBODY TELLS YOU: it's retroactive. If you qualified in past years and never asked, those years can still be paid. "
     "Parents can ask until the day before the child turns 18. After that, your child can ask for it themselves until the day before "
     "they turn 21. Only about 4 in 10 eligible kids had it in 2022.\n\n"
     "3 STEPS AND 1 HABIT:\n"
     "1. Get your child a SIN (in Ontario you can ask for it when you register the birth).\n"
     "2. Open an RESP. No deposit is needed for the bond. Ask for one with no fees.\n"
     "3. Ask your bank or RESP provider for the Canada Learning Bond. They have the form.\n"
     "Then the habit: file your taxes every year, even with little or no income. That's how the government checks if you qualify again.\n\n"
     "Do this: this week, call your bank and say: \"I'd like a no-fee RESP with the Canada Learning Bond.\" Have your child's SIN and "
     "yours ready.\n\n"
     "The rule that stays: no deposit, just the account.\n\n"
     "Send this to a parent who should check.\n\n"
     "#RESP #CanadaLearningBond #newparents #canadianparents #babymoney",
     "Sources: " + CLB_SRC + " canada.ca also says: 'The CLB is retroactive'; amounts accumulate each year of eligibility until "
     "December 31 of the year the child turns 15; the primary caregiver can request it until the day before the child turns 18, and the "
     "child can request it from 18 until the day before they turn 21; no contributions are needed; SINs for the child and primary "
     "caregiver are required, and the caregiver must file income tax returns (ESDC InfoCapsule 9). Ontario Newborn Registration "
     "Service lets parents apply for the baby's SIN when registering the birth (ServiceOntario). Take-up: C.D. Howe Institute "
     "(Godbout & Samoisette), citing ESDC's 2022 Canada Education Savings Program statistical review: 42.5% of eligible children "
     "had received the bond in 2022.")

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

# Oct 20, 11:30 · BONDING/DEPTH REWRITE (same id, Oct 19) · toddler meltdown: connect first, then redirect, then repair.
# Ideas from The Whole-Brain Child (Siegel & Bryson: connect and redirect, name it to tame it) and How to Talk So Little Kids Will
# Listen (acknowledge the feeling, keep the limit), facts from the NHS. Rule that stays: "Connect, then redirect."
MELT_SRC = ("Sources: NHS, Temper tantrums (nhs.uk): tantrums usually start around 18 months and are very common; toddlers want to "
            "express themselves but find it difficult; giving in will not help in the long term; shouting back will not end it; "
            "distract early; keep shopping trips short and involve your child. Lieberman et al. (2007), Putting feelings into words, "
            "Psychological Science: labelling a feeling reduced activity in the brain's alarm centre (amygdala). Ideas (not quotes) "
            "from Siegel & Bryson, The Whole-Brain Child ('connect and redirect', 'name it to tame it') and Faber & King, How to Talk "
            "So Little Kids Will Listen (acknowledge feelings while keeping the limit). Scripts are our own.")

post("lf-06-toddler-meltdown", LF, "2026-10-20T11:30", "deep",
     dict(lay="sticky", f="cream", text="Meltdown / in the *cereal aisle?*", obj="ok", at="bl",
          items=["Connect first", "Name the feeling", "Then redirect"], save="4 steps + what to say"),
     [dict(k="say", f="pink", label="first, the why", text="At 2, the *feelings* / part of the brain / is loud. The *calm-* / *down* part is still / being built."),
      dict(k="say", f="butter", text="Tantrums often / start around / *18 months.* Words / can't keep up / with feelings yet.",
           src="NHS, Temper tantrums"),
      dict(k="say", f="cream", label="step 1: get low", text="Kneel to their / *eye level.* / Soft, slow voice. / Stay close."),
      dict(k="say", f="pink", label="step 2: name it", text="*“You really* / *wanted that cereal.* / You're so cross.”",
           sub="naming a feeling helps calm it"),
      dict(k="say", f="butter", label="step 3: keep the no", text="*“The answer is* / *still no.* / I'm right here.”",
           sub="give in, and they learn tantrums work"),
      dict(k="say", f="cream", label="step 4: redirect", text="Calmer now? / *“Can you help me* / *find the bananas?”*",
           sub="connect, then redirect"),
      dict(k="say", f="pink", label="later: the repair", text="At bedtime: / *“That was hard.* / *We got through it* / *together.”*"),
      dict(k="do", f="butter", text="Next shop, keep it *short* and give your toddler *one job:* finding the bananas.",
           save="send this to a parent of a two-year-old")],
     "Meltdown in the cereal aisle? Here's what to do, step by step, and exactly what to say.\n\n"
     "FIRST, THE WHY: at 2, the feelings part of your child's brain is loud, and the calm-down part is still being built. The NHS says "
     "tantrums usually start around 18 months. Your toddler has big feelings and not enough words yet. It's not bad behaviour you caused.\n\n"
     "THE 4 STEPS:\n"
     "1. Get low. Kneel to their eye level. Soft, slow voice. Stay close.\n"
     "2. Name it. \"You really wanted that cereal. You're so cross.\" Putting a feeling into words helps calm the brain's alarm.\n"
     "3. Keep the no. \"The answer is still no. I'm right here.\" If you give in, they learn tantrums work. Shouting back won't end it either.\n"
     "4. Redirect. Once they're a little calmer: \"Can you help me find the bananas?\"\n\n"
     "LATER, THE REPAIR: at bedtime, \"That was hard in the store. You were so cross, and we got through it together.\" This is where "
     "they learn feelings pass and you stay.\n\n"
     "WEEK 1 → MONTH 1: in week 1 you'll mostly remember step 1. By month 1, \"You really wanted…\" comes out on its own, and your "
     "toddler starts to know what comes next: you get low, you name it, you stay.\n\n"
     "Do this: next shop, keep it short and give your toddler one job, like finding the bananas.\n\n"
     "The rule that stays: connect, then redirect.\n\n"
     "Send this to a parent of a two-year-old.\n\n"
     f"{NOT_MED}\n\n#toddlers #tantrums #gentleparenting #toddlermom #wholebrainchild",
     MELT_SRC)

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

# Oct 21, 11:30 · BONDING REPLACEMENT (same id/slot, Oct 19; the guardian/will post moves to backlog: Oct 21 already carries the
# 08:00 family-money cheat Reel and the 17:00 $50-a-month reveal) · SPECIAL TIME: 10 minutes, they lead, you follow.
# NHS Lothian 'Special Time' + PCIT child-led play (PRIDE skills). Rule that stays: "They lead. You follow."
SPECIAL_SRC = ("Sources: NHS Lothian, Let's Talk, Special Time (lets-talk.scot.nhs.uk): 10 minutes, at least 3-4 times a week; your "
               "child chooses the activity (puzzles, building, playdough, drawing, dolls, cars) and leads; TV, devices and background "
               "noise off; face to face at their level, undivided attention; use comments rather than lots of questions; stop at 10 "
               "minutes even if they want more and thank your child; a predictable routine helps children know what to expect. "
               "University of Iowa Psychiatry, Child-led play (Parent-Child Interaction Therapy): PRIDE skills (praise, reflect, "
               "imitate, describe, enjoyment); avoid commands, questions and criticism. Ideas (not quotes) from Siegel & Bryson, The "
               "Power of Showing Up. Scripts are our own.")

post("lf-1021-name-a-guardian", LF, "2026-10-21T11:30", "deep",
     dict(lay="pills", f="pink", kicker="special time", text="The *10 minutes* / your toddler / will ask for", obj="point", at="bl",
          save="they lead. you follow."),
     [dict(k="say", f="butter", label="sound familiar?", text="With them all day, / but *half on your* / *phone,* half on / the dishes."),
      dict(k="say", f="cream", label="the fix", text="*Special Time.* / 10 minutes. / *They lead.* / You follow.",
           sub="an NHS speech and play tip"),
      dict(k="rows", f="pink", text="The *setup*", cap="NHS Lothian, Special Time",
           rows=[("How long", "10 minutes"), ("How often", "3–4 a week+"), ("Who picks", "Your child"), ("TV, phone", "Off")],
           src="NHS Lothian, Special Time"),
      dict(k="say", f="butter", label="say what you see", text="*“You're building* / *a tall tower.”* / Copy their moves. / *“Gentle hands!”*"),
      dict(k="say", f="cream", label="skip the quiz", text="No *“what colour* / *is that?”* / No instructions. / Just *follow.*"),
      dict(k="say", f="pink", label="when time's up", text="*“Special time* / *is over. I loved* / *playing with you.”*",
           sub="stop at 10, even if they beg"),
      dict(k="say", f="butter", label="why it works", text="Your full attention, / *on their terms,* / *at a time they* / *can count on.*"),
      dict(k="do", f="cream", text="Tonight, set a timer for *10 minutes,* phone in another room, and say: *“You choose. I'll follow.”*",
           save="send this to your partner")],
     "The 10 minutes your toddler will start asking for.\n\n"
     "SOUND FAMILIAR? You're with them all day, but half on your phone and half on the dishes. They can tell.\n\n"
     "THE FIX: Special Time. It's a tip NHS speech and language therapists give parents, and it comes from the same child-led play "
     "that child therapists use. 10 minutes. Your child leads. You follow.\n\n"
     "THE SETUP:\n"
     "• 10 minutes, at least 3 to 4 times a week. Same time each day if you can (after dinner works for lots of families).\n"
     "• Your child picks: blocks, playdough, drawing, cars, dolls. Not screens, and not books or chasing games for this one: you want "
     "face-to-face back and forth.\n"
     "• TV, music and phones off. Sit at their level.\n\n"
     "WHAT TO DO:\n"
     "• Say what you see: \"You're building a tall tower. You put the red one on top.\"\n"
     "• Copy them: they stack, you stack.\n"
     "• Praise the exact thing: \"Gentle hands with the blocks!\"\n"
     "• Repeat their words: \"Big truck!\" \"A big truck!\"\n\n"
     "WHAT TO SKIP: questions (\"what colour is that?\"), instructions (\"put it here\"), and corrections. Even friendly quizzing takes "
     "the lead back.\n\n"
     "ENDING: when the timer goes, \"Special time is over. I loved playing with you.\" Stop at 10, even if they beg. That's what makes "
     "it something they can count on.\n\n"
     "DAY 1 → WEEK 1 → MONTH 1: day 1 feels awkward (not asking questions is hard!). By week 1, saying what you see starts to feel natural. "
     "Imagine month 1: a child who knows that every day, for 10 minutes, they have all of you.\n\n"
     "Do this: tonight, set a 10-minute timer, put your phone in another room, and say: \"You choose. I'll follow.\"\n\n"
     "The rule that stays: they lead, you follow.\n\n"
     "Send this to your partner. You can take turns.\n\n"
     "#toddlers #bonding #playtime #gentleparenting #specialtime",
     SPECIAL_SRC)



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

# Oct 19, 08:00 · BONDING REWRITE (same id, Oct 19 00:20) · hunger cues = baby's first conversation (Trial Reel)
# Built on NHS responsive-feeding guidance (early / mid / late cues) + the serve-and-return idea (Harvard CDC).
# Rule that stays: "Answer the whisper, not the scream."
CUES_SRC = ("Sources: NHS Norfolk & Waveney (Just One Norfolk), Feeding cues: early cues 'I'm hungry' (stirring, mouth opening, "
            "turning head, seeking/rooting); mid cues 'I'm really hungry' (stretching, increasing physical movement, hand to mouth); "
            "late cues 'calm me, then feed me' (crying, agitated body movements, colour turning red); feed as soon as you notice early "
            "or mid cues; a very upset baby may find it harder to latch, so calm them first; feeds also give comfort, reassurance and "
            "warmth. Cambridge University Hospitals NHS (Rosie Hospital), Tips for successful breastfeeding: crying is often the last "
            "cue. UNICEF UK Baby Friendly Initiative, Responsive bottle feeding: hold baby close, look into their eyes, pace the feed "
            "and watch for cues. Harvard Center on the Developing Child, Serve and return: back-and-forth responses build the "
            "foundations of brain architecture.")

reel("lf-reel-1019am-hunger-cues", LF, "2026-10-19T08:00", "deep", "lf-x-sunny-bounce", "send this to someone expecting", [
    dict(k="hook", f="pink", text="Your newborn / *talks to you* / before they cry.", emo="🫶"),
    dict(k="because", f="cream", kicker="here's the secret", text="Hunger comes in *3 waves.* Crying is the *last.*"),
    dict(k="say", f="butter", text="Wave 1: *“I'm hungry.”* / Mouth opens, / head turns.", drop=True),
    dict(k="say", f="cream", text="Wave 2: / *“Really hungry.”* / *Hands to mouth.*"),
    dict(k="say", f="pink", text="Wave 3: crying. / *Calm first,* / *then feed.*"),
    dict(k="say", f="butter", text="Answer early, and / baby learns: / *“Someone hears me.”*"),
    dict(k="do", f="cream", text="Next feed: *mouth opens* or *head turns?* Feed then."),
    dict(k="save", f="pink", text="Answer the whisper, / not the scream."),
], "Your newborn is talking to you long before they cry. Here's how to hear it.\n\n"
   "HUNGER COMES IN 3 WAVES (NHS feeding guidance):\n"
   "1. \"I'm hungry\": stirring, mouth opening, turning their head to search (rooting).\n"
   "2. \"I'm really hungry\": stretching, wriggling more, hands to mouth.\n"
   "3. \"Calm me, then feed me\": crying, agitated movements, going red.\n\n"
   "WHY IT MATTERS: catch wave 1 or 2 and feeds start calmer. By wave 3, a very upset baby often finds it harder to latch, so you "
   "soothe first (skin to skin, gentle rocking, your voice) and feed second.\n\n"
   "THE BONDING PART: every cue you answer is a tiny conversation. Baby \"serves\" (a stir, a little mouth open), you \"return\" "
   "(you pick them up, you talk to them). Child-development scientists at Harvard call this serve and return, and it's how a baby's "
   "brain starts building its wiring. Feeds are comfort and closeness too, not just food.\n\n"
   "Bottle-feeding? Same cues, same conversation. Hold baby close and upright, look at them, and let them set the pace.\n\n"
   "DAY 1 → WEEK 1 → MONTH 1: on day 1 you'll miss most cues (everyone does). By week 1 you'll spot the head turn. By month 1 you'll "
   "know your baby's own \"I'm hungry\" face before anyone else in the room.\n\n"
   "Do this: next feed, watch the face for a minute. Mouth opening or head turning? Feed then. Missed it and baby's crying? Calm first, then feed.\n\n"
   "The rule that stays: answer the whisper, not the scream.\n\n"
   "Send this to someone expecting.\n\n"
   f"{NOT_MED}\n\n#newborn #breastfeeding #bonding #newparents #responsivefeeding",
   CUES_SRC)

# Oct 19, 19:00 · BONDING REWRITE (same id; the $50-a-month RESP growth now lives in the 17:00 Oct 21 reveal) · serve and return
# Harvard Center on the Developing Child's 5 steps, with our own word-for-word scripts by age. Part 2 of the morning Reel
# ("your newborn talks to you before they cry"). Rule that stays: "Wait for their turn."
SR_SRC = ("Sources: Harvard University, Center on the Developing Child, '5 Steps for Brain-Building Serve and Return': 1. notice the "
          "serve and share the child's focus of attention; 2. return the serve by supporting and encouraging; 3. give it a name; "
          "4. take turns and wait (children need time to form their responses); 5. practice endings and beginnings. Same centre, "
          "'Brain Architecture': in the first few years of life, more than 1 million new neural connections form every second, and "
          "serve-and-return interactions shape that architecture. Scripts by age are our own illustrations of the 5 steps.")

reel("lf-reel-1019-resp-50-month", LF, "2026-10-19T19:00", "deep", "lf-x-tiny-parade", "send this to a new parent", [
    dict(k="hook", f="cream", text="The *5-step game* / that builds / baby's brain", emo="🐣"),
    dict(k="because", f="butter", kicker="Harvard calls it", text="*Serve and return.* Baby serves. *You return.*"),
    dict(k="say", f="pink", text="1. *Notice* it: / a look, a coo, / a point.", drop=True),
    dict(k="say", f="cream", text="2. *Return it.* / Smile. Coo back."),
    dict(k="say", f="butter", text="3. *Name it.* / “A *dog!* / A big dog.”"),
    dict(k="say", f="pink", text="4. *Then wait.* / Count to 5. / Let them reply."),
    dict(k="say", f="cream", text="5. Looks away? / *That's the end.*"),
    dict(k="do", f="pink", text="Tonight at bath time: *2 minutes* of serve and return."),
    dict(k="save", f="butter", text="Wait for / their turn."),
], "The 5-step game that builds your baby's brain. No toys, no apps, no cost.\n\n"
   "Child-development scientists at Harvard call it serve and return. Your baby \"serves\" (a look, a coo, a point, a babble) and "
   "you \"return\" it. In the first few years, more than a million new brain connections form every second, and these "
   "back-and-forth moments help shape them.\n\n"
   "THE 5 STEPS:\n"
   "1. Notice the serve. What is baby looking at, reaching for, pointing at?\n"
   "2. Return it. Smile, nod, touch, coo back.\n"
   "3. Name it. \"That's a dog! A big brown dog.\"\n"
   "4. Take turns, then wait. Count to 5 in your head. Babies need time to answer.\n"
   "5. Notice the end. They look away or drop the toy? That's the end. Catch the next serve.\n\n"
   "WHAT IT SOUNDS LIKE, BY AGE:\n"
   "• 2 months: baby coos. You: \"Ooh, is that right?\" Pause. Baby coos again. That's a conversation.\n"
   "• 6 months: baby says \"ba-ba\". You: \"Ba-ba! You're talking!\" Wait. \"Ba!\"\n"
   "• 12 months: baby points at a bird. You point too: \"A bird! It's flying.\" Wait for the next point.\n"
   "• 2 years: \"Truck!\" You: \"A big red truck. Where's it going?\" Wait. Let them answer, even if it's just \"there!\"\n\n"
   "DAY 1 → YEAR 1: on day 1 it's eye contact and your voice. By month 3, the coo-and-pause game. By month 9, pointing together. By "
   "year 1, every first word gets a reply.\n\n"
   "Do this: tonight at bath time, play 2 minutes of serve and return. Follow what they look at, name it, then wait.\n\n"
   "The rule that stays: wait for their turn.\n\n"
   "Send this to a new parent.\n\n"
   "#bonding #babydevelopment #newparents #serveandreturn #babybrain",
   SR_SRC)

# Oct 20, 08:00 · BONDING REWRITE (same id, Oct 19) · bonding with the bump + learn the pattern (the reduced-movements safety
# rule stays word-for-word strong: call right away, don't wait). Rule that stays: "Talk to the bump. Trust the kicks."
BUMP_SRC = ("Sources: Tommy's (UK pregnancy charity, midwife-reviewed), 18 weeks pregnant: baby can hear more sounds outside your "
            "body and may jump at loud noises. DeCasper & Fifer (1980), Of human bonding: newborns prefer their mothers' voices, "
            "Science 208: newborns worked to hear their own mother's voice over another woman's. NHS, Your baby's movements "
            "(nhs.uk): most people start to feel movements between 16 and 24 weeks; there is no set number of normal movements, get "
            "to know your baby's own pattern; call your midwife or maternity unit immediately if your baby is moving less than "
            "usual, you cannot feel them moving, or the pattern changes. Do not wait until the next day. Do not use a home "
            "doppler or app to check.")

reel("lf-reel-1020am-movements", LF, "2026-10-20T08:00", "deep", "lf-x-giggle-pop", "send this to someone expecting", [
    dict(k="hook", f="pink", text="Your baby / *learns your voice* / before birth.", emo="🫶"),
    dict(k="because", f="cream", kicker="here's when", text="From about *18 weeks,* baby can *hear* sounds outside the bump."),
    dict(k="say", f="butter", text="Newborns *prefer* / *mum's voice.* / They learned it / in the womb.", drop=True),
    dict(k="say", f="cream", text="So talk. Sing. / Read out loud. / *Partners too.*"),
    dict(k="say", f="pink", text="And learn their / *pattern* of moves."),
    dict(k="say", f="berry", text="Moving *less?* / Call your midwife / or hospital *now.* / Don't wait."),
    dict(k="do", f="cream", text="Tonight, hand on the bump: *talk or sing for 5 minutes.*"),
    dict(k="save", f="pink", text="Talk to the bump. / Trust the kicks."),
], "Your baby is learning your voice before they're even born.\n\n"
   "WHEN: from about 18 weeks, babies start to hear sounds from outside the bump (some jump at loud music). Most people feel the "
   "first movements somewhere between 16 and 24 weeks.\n\n"
   "THE PROOF: in a classic study, newborns just days old worked harder to hear their own mother's voice than a stranger's. They "
   "learned it in the womb.\n\n"
   "HOW TO BOND WITH THE BUMP:\n"
   "• Talk to baby at the same time each day: \"Good morning, little one. Today we're going to the market.\"\n"
   "• Sing one song every night. The same one. It can become their lullaby after birth.\n"
   "• Partners: put your hand on the bump and talk too. It's your first hello.\n\n"
   "LEARN THEIR PATTERN: there's no \"right\" number of kicks. Notice when your baby is usually busy (after dinner? when you lie "
   "down?).\n\n"
   "THE SAFETY RULE (NHS): if your baby is moving less than usual, you can't feel them moving, or the pattern changes, call your "
   "midwife or maternity unit right away, even in the middle of the night. Don't wait until tomorrow, and don't use a home "
   "heartbeat monitor or app to check. You are never a bother.\n\n"
   "WEEK 18 → WEEK 28 → BIRTH: first, sounds reach baby. Then you know their busy times. At birth, the voice they hear on your chest "
   "is the one they already know.\n\n"
   "Do this: tonight, hand on the bump, talk or sing for 5 minutes, and notice when they move. Save your hospital's birth unit "
   "number in your phone while you're at it.\n\n"
   "The rule that stays: talk to the bump, trust the kicks.\n\n"
   "Send this to someone expecting.\n\n"
   f"{NOT_MED}\n\n#pregnancy #bondingwithbump #pregnant #babymovements #expectingparents",
   BUMP_SRC)

# Oct 20, 19:00 · BONDING REWRITE (same id, Oct 19) · the bonding bubble: skin to skin + visitor rules (cold-sore safety kept).
# Rule that stays: "Visitors help. You hold the baby."
VIS_SRC = ("Sources: NHS Start for Life, Skin-to-skin contact with your newborn (nhs.uk): holding your baby naked against your skin, "
           "usually under your top or a blanket; helps regulate baby's temperature, breathing and heart rate; baby hears your heartbeat "
           "and voice, which can calm them; releases oxytocin; helps you bond; keep doing it at home, especially in the first days "
           "and weeks. UNICEF UK Baby Friendly Initiative, skin-to-skin safety: baby's face visible, nose and mouth clear, head turned "
           "to one side; if you feel sleepy, put baby down in their own safe sleep space. NHS, Neonatal herpes (nhs.uk): the virus can "
           "pass to a baby through a cold sore when someone kisses them; it can be very serious for a young baby; wash hands before "
           "handling the baby; don't kiss the baby if you have a cold sore.")

reel("lf-reel-1020-visitors", LF, "2026-10-20T19:00", "deep", "lf-x-sunny-bounce", "send this to the family group chat", [
    dict(k="hook", f="cream", text="The first *2 weeks:* / protect your / *bonding bubble.*", emo="🫶"),
    dict(k="because", f="butter", kicker="the NHS says", text="*Skin to skin* steadies baby's *heart rate,* breathing and warmth."),
    dict(k="say", f="pink", text="Baby on your / *bare chest,* / a blanket over / you both.", drop=True),
    dict(k="say", f="cream", text="Visitors? / *Wash hands first.* / *No kisses.*"),
    dict(k="say", f="butter", text="A cold sore can / pass to a baby / through *one kiss.*"),
    dict(k="say", f="pink", text="Helpers get a job: / *dishes or dinner.* / You hold the baby."),
    dict(k="do", f="cream", text="Text visitors today: *“Wash hands, no kisses, bring dinner.”*"),
    dict(k="save", f="pink", text="Protect / the bubble."),
], "The first 2 weeks: protect your bonding bubble.\n\n"
   "WHY SKIN TO SKIN: the NHS says holding your baby naked against your bare chest helps steady their heart rate, breathing and "
   "temperature. They hear your heartbeat and voice, which calms them, and your body releases oxytocin, the feel-good hormone that "
   "helps you bond. Partners can do it too.\n\n"
   "HOW: baby in just a diaper on your bare chest, a blanket over you both, their face turned to one side so you can see their nose "
   "and mouth. If you start to feel sleepy, put baby down on their back in their own crib or bassinet.\n\n"
   "THE VISITOR RULES:\n"
   "1. Wash hands before holding the baby.\n"
   "2. No kisses on the baby. A cold sore can pass to a newborn through a kiss, and it can be very serious.\n"
   "3. Feeling unwell? Visit later.\n"
   "4. Come with a job: dishes, laundry, a meal. Not \"Let me hold the baby so you can clean.\" The other way round.\n\n"
   "DAY 1 → WEEK 2: on day 1, the first hour skin to skin. By week 1, skin to skin is how you calm a fussy evening. By week 2, your "
   "visitors know the rules and you've barely let go of the baby.\n\n"
   "Do this: today, text your visitors: \"We'd love to see you. Wash hands, no kisses, and bring dinner if you can.\"\n\n"
   "The rule that stays: protect the bubble. Visitors help, you hold the baby.\n\n"
   "Send this to the family group chat.\n\n"
   f"{NOT_MED}\n\n#newborn #skintoskin #newparents #fourthtrimester #bonding",
   VIS_SRC)


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
    dict(k="payoff", f="pink", label="and missed years?", text="*It's retroactive.* / Ask before 18.", sub="no deposit. just open the RESP.",
         obj="clock", tap="next story →"),
    dict(k="handoff", f="cream", text="Up to / *$2,000,* / no deposit", img="lf-1019-learning-bond/01.jpg", next="who qualifies + 3 steps"),
])

# Oct 20 · REWRITE (same id) · hands off to lf-06-toddler-meltdown
chain("lf-ch-1020", LF, "2026-10-20", "lf20", "calmer toddler days", [  # day A: the chain carries the lesson
    dict(k="photo", text="“Not in the / *cereal aisle…*”", sub="the 4 steps that *actually help* →", ink="light", y=1050),
    dict(k="bubbles", f="cream", label="the parents' group chat", bubbles=[
        ("in", "she screamed until I gave her the cookie"),
        ("out", "been there. try this first: kneel down, then *name it*"),
        ("out", "*“you really wanted that cookie. you're so cross.”*")], obj="ok"),
    dict(k="payoff", f="butter", label="then keep the no, kindly", text="“Still no. / *I'm right here.*”",
         sub="connect first. then redirect.", obj="shoe"),
    dict(k="handoff", f="cream", text="Calmer / *meltdowns*", img="lf-06-toddler-meltdown/01.jpg", next="4 steps + what to say"),
])


# Oct 21 · BONDING (same id) · day B: guess-and-reveal quiz -> lf-1021-name-a-guardian (now Special Time)
chain("lf-ch-1021", LF, "2026-10-21", "lf21", "special time", [
    dict(k="bubbles", f="cream", label="quick quiz", title="Time that *bonds* / a toddler most…", bubbles=[
        ("in", "how much one-on-one play does the NHS tip ask for?"), ("out", "A) an hour a day"), ("out", "B) 10 minutes")],
         obj="shoe", tap="guess, then tap →"),
    dict(k="payoff", f="butter", label="the answer: B", text="*10* / minutes", sub="at least 3 to 4 times a week", obj="point",
         tap="source: NHS Lothian, Special Time · tap →"),
    dict(k="payoff", f="pink", label="the one rule", text="*They lead.* / You follow.", sub="no quizzing, no phone", obj="ok",
         tap="next story →"),
    dict(k="handoff", f="cream", text="The *10 minutes* / they'll ask for", img="lf-1021-name-a-guardian/01.jpg", next="the setup + what to say"),
])


# ================================================================== Oct 22 (11:30 is reserved for the orchestrator's travelling carousel)
CCB_SRC = ("Source: CRA (canada.ca), RC4476-ON, Birth Registration and Canada Child Benefits (Ontario): register online with "
           "ServiceOntario's Newborn Registration Service and choose the option 'Canada child benefits'; with your consent your "
           "information goes to the CRA, and you should not re-apply through CRA My Account or Form RC66. The primary caregiver "
           "applies and gives their SIN. Maximum CCB, July 2026 to June 2027: up to $8,157 a year per child under 6 (canada.ca; "
           "income-tested).")

reel("lf-reel-1022-ccb-at-birth", LF, "2026-10-22T19:00", "deep", "lf-x-tiny-parade", "send this to someone expecting", [
    dict(k="hook", f="pink", text="New baby in Ontario? / *One box* starts / your Child Benefit.", emo="🍼"),
    dict(k="because", f="cream", kicker="here's how", text="Register the birth online. Tick *Canada child benefits.*"),
    dict(k="say", f="butter", text="Up to *$8,157* / a year, per child / *under 6.*", drop=True),
    dict(k="say", f="cream", text="*Income-tested:* / less as income / goes up."),
    dict(k="say", f="berry", text="Then *don't* apply / again. The CRA / *already has it.*"),
    dict(k="say", f="pink", text="Keep it coming: / *both parents* / *file taxes* / every year."),
    dict(k="do", f="cream", text="Before the birth, put *both SINs* in one note on your phone."),
    dict(k="save", f="pink", text="One box. / Every month."),
], "New baby in Ontario? One box on the birth registration starts your Canada Child Benefit.\n\n"
   "HOW IT WORKS: when you register the birth online with ServiceOntario's Newborn Registration Service, choose \"Canada child "
   "benefits\". With your OK, your details go straight to the CRA. No separate form.\n\n"
   "HOW MUCH: up to $8,157 a year for each child under 6, paid monthly (July 2026 to June 2027). It's income-tested, so it gets "
   "smaller as family income goes up.\n\n"
   "THE 3 MISTAKES TO AVOID:\n"
   "1. Applying again through My Account or form RC66 after you ticked the box. The CRA already has it.\n"
   "2. Forgetting the SIN. The main caregiver (the parent who applies) needs theirs ready.\n"
   "3. Skipping tax returns. Both parents need to file every year, even with little or no income, or the payments can stop.\n\n"
   "THE SAME 15 MINUTES ALSO: the Newborn Registration Service bundle can order the birth certificate and apply for baby's SIN, "
   "which you'll need for an RESP later.\n\n"
   "Do this: before the birth, put both parents' SINs in one note on your phone, so registration takes one sitting.\n\n"
   "The rule that stays: one box, every month.\n\n"
   "Send this to someone expecting a baby.\n\n#newparents #canadachildbenefit #ontarioparents #babymoney #expectingparents",
   CCB_SRC + " CRA (canada.ca), Canada child benefit, how to keep getting it: you and your spouse or common-law partner must each "
             "file a tax return every year, even if you had no income. ServiceOntario Newborn Registration Service: register the "
             "birth, apply for a birth certificate and the baby's SIN, and apply for Canada child benefits in one online bundle.")


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
    dict(k="handoff", f="cream", text="Where should / baby *sleep?*", img="lf-1022-follow-safe-sleep/01.jpg", next="the rules, in one look"),
], times=["16:30", "16:31", "16:32", "17:15"])


# ================================================================== Oct 23 (day B: quiz) · RESP catch-up + screens before bed
SCREEN_SRC = ("Source: Canadian Paediatric Society, Screen time and young children: promoting health and development in a digital "
              "world (2017, reaffirmed), and caringforkids.cps.ca: avoid screens for at least 1 hour before bedtime; keep daily "
              "screen-free times, especially family meals and book-sharing.")

reel("lf-reel-1023am-screens-bed", LF, "2026-10-23T08:00", "deep", "lf-x-giggle-pop", "send this to someone in bedtime battles", [
    dict(k="hook", f="butter", text="Turn bedtime / *battles* into the / *best 20 minutes.*", emo="🌙"),
    dict(k="because", f="pink", kicker="Canada's paediatricians say", text="*No screens* in the *hour* before bed."),
    dict(k="say", f="berry", text="Then the same / 3 steps, every night: / *Brush. Book. Bed.*", drop=True),
    dict(k="say", f="cream", text="*Brush:* you help. / Spit out the extra. / *Don't rinse.*"),
    dict(k="say", f="butter", text="*Book:* about / *15 minutes,* / snuggled close."),
    dict(k="say", f="pink", text="*Bed:* lights low. / *“What was the best* / *part of today?”*"),
    dict(k="do", f="cream", text="Tonight, tablet off *1 hour* before bed. Then *brush, book, bed.*"),
    dict(k="save", f="pink", text="Same steps. / Same words. / Every night."),
], "Turn bedtime battles into the best 20 minutes of the day.\n\n"
   "STEP 0, THE HOUR BEFORE: the Canadian Paediatric Society says no screens for at least 1 hour before bedtime. Tablet and TV off, "
   "lights a little lower.\n\n"
   "THEN THE SAME 3 STEPS, EVERY NIGHT (the American Academy of Pediatrics calls it Brush, Book, Bed):\n"
   "1. Brush. You help, because little hands miss spots. Spit out the extra toothpaste, don't rinse: the fluoride left behind keeps "
   "working. (A rice-grain smear under 3, a pea-size blob from 3 to 6.)\n"
   "2. Book. About 15 minutes, snuggled close. Let them pick, even if it's the same one for the 40th night.\n"
   "3. Bed. Lights low, same time every night. Our favourite last line: \"What was the best part of today?\" Then tell them yours.\n\n"
   "WHY IT WORKS: when the steps never change, your child knows exactly what comes next, and there's less to fight about. The book "
   "and the chat are pure connection time, every single day.\n\n"
   "NIGHT 1 → WEEK 1 → YEAR 1: night 1, they test it. By week 1, the steps start to run themselves. Picture year 1: 365 bedtime "
   "stories, and a child who saves the best part of their day to tell you.\n\n"
   "Do this: tonight, tablet off 1 hour before bed. Then brush, book, bed, and ask the best-part question.\n\n"
   "The rule that stays: same steps, same words, every night.\n\n"
   "Send this to someone in bedtime battles.\n\n"
   f"{NOT_MED}\n\n#bedtimeroutine #toddlerlife #screentime #canadianparents #bonding",
   SCREEN_SRC + " American Academy of Pediatrics, healthychildren.org, Brush, Book, Bed: a nightly routine so children know what "
                "comes next; help young children brush, spit out extra toothpaste without rinsing, a rice-grain amount of fluoride "
                "toothpaste under 3 and a pea-size amount from 3 to 6; read together about 15 minutes a day; keep a regular bedtime. "
                "The 'best part of today' question is our own idea.")

post("lf-1023-resp-catch-up", LF, "2026-10-23T11:30", "deep",
     dict(lay="pills", f="butter", kicker="baby money", text="Never opened / an *RESP?*", obj="point", at="bl",
          save="it's not too late. here's the plan."),
     [dict(k="say", f="cream", label="sound familiar?", text="“We'll start / *next year.*” / Then the baby / is *five.*"),
      dict(k="say", f="pink", label="the part nobody tells you", text="Grant room builds / *every year* from birth, / even with *no RESP.*",
           src="canada.ca, Canada Education Savings Grant"),
      dict(k="rows", f="butter", text="You put in, they *add*", cap="Canada Education Savings Grant, per year",
           rows=[("$1,000", "+$200"), ("$2,500", "+$500"), ("$5,000*", "+$1,000")],
           sub="*with unused room", src="canada.ca, CESG"),
      dict(k="say", f="cream", text="Start late, and / the government can / add up to:", num="$1,000",
           sub="a year, using your unused room", src="canada.ca, Canada Education Savings Grant"),
      dict(k="say", f="pink", label="can't do $5,000?", text="*$2,500 a year* / still gets the / *full $500.* / Any amount / gets *20%.*"),
      dict(k="say", f="butter", label="the deadline", text="Grants stop at / the end of the year / your child *turns 17.*",
           sub="at 16 and 17, only if you saved earlier"),
      dict(k="do", f="cream", text="This week, ask your bank to open an RESP and *use your catch-up room.*",
           save="send this to a parent who never opened one")],
     "Never opened an RESP? It's not too late. Here's the catch-up plan.\n\n"
     "SOUND FAMILIAR? \"We'll start next year.\" Then the baby is five.\n\n"
     "THE PART NOBODY TELLS YOU: your child's grant room builds up every year from birth, even if you never opened an RESP. "
     "The government matches 20% of what you save through the Canada Education Savings Grant.\n\n"
     "YOU PUT IN, THEY ADD (per year):\n"
     "• $1,000 in → $200 added\n• $2,500 in → $500 added (the normal yearly max)\n"
     "• $5,000 in → $1,000 added (*only if you have unused room from past years)\n\n"
     "Catching up, the grant can be up to $1,000 a year, until the full $7,200 per child is used.\n\n"
     "CAN'T DO $5,000? $2,500 a year still gets the full $500, and any amount gets 20% added.\n\n"
     "THE DEADLINE: grants stop at the end of the year your child turns 17. At 16 and 17 they only qualify if at least $2,000 went in "
     "before the end of the year they turned 15, or $100 a year in any 4 earlier years. So for an older child, start now.\n\n"
     "Do this: this week, ask your bank to open an RESP and use your catch-up room. Bring your child's SIN.\n\n"
     "The rule that stays: the room waits for you, but not forever.\n\n"
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

post("lf-1024-no-honey", LF, "2026-10-24T11:30", "deep",
     dict(lay="pills", f="butter", kicker="baby safety", text="Honey for baby? / *Not before 1.*", obj="ok", at="bl",
          save="not even a tiny bit"),
     [dict(k="rows", f="cream", text="*No honey* before 1", cap="Health Canada",
           rows=[("In food", "no"), ("In water or formula", "no"), ("On a soother", "no"), ("Cooked, pasteurized", "still no")],
           src="Health Canada, Infant botulism"),
      dict(k="say", f="pink", label="here's why", text="Honey can carry / *botulism* spores. / A baby's gut / can't fight them *yet.*",
           sub="and cooking doesn't kill them", src="Health Canada, Infant botulism"),
      dict(k="say", f="cream", label="call the doctor now if baby is", text="*Constipated,* / *floppy,* too weak / to cry or suck, / or can't swallow.",
           src="Health Canada, Infant botulism"),
      dict(k="say", f="butter", label="the grandparent script", text="*“No honey before* / *her first birthday.* / Not even a little / on the soother.”"),
      dict(k="say", f="pink", label="after age 1", text="A healthy child's / gut can *handle* / *the spores.* / Then honey is OK.",
           src="Health Canada, Infant botulism"),
      dict(k="do", f="butter", text="Today, check baby's snacks and cereals for *honey* on the label. Then tell the grandparents.",
           save="send this to the grandparents")],
     "Honey for baby? Not before their first birthday. Not even a tiny bit.\n\n"
     "Health Canada says: no honey of any kind for babies under 1. Not in food, water or formula, and never on a soother. "
     "Cooked or pasteurized honey isn't safe either.\n\n"
     "Here's why: honey can carry botulism spores. Heat doesn't kill them, and a baby's gut can't fight them yet. After age 1, "
     "healthy kids have the gut bacteria to handle them.\n\n"
     "Call your doctor right away if a baby is constipated, floppy, too weak to cry or suck as usual, or has trouble breathing or swallowing.\n\n"
     "THE GRANDPARENT SCRIPT: \"No honey before her first birthday. Not even a little on the soother. The doctor's rule, not mine.\"\n\n"
     "Do this: today, check baby's snacks and cereals for honey on the label. Then tell the grandparents.\n\n"
     "The rule that stays: no honey before 1. Not a drop.\n\n"
     f"Send this to the grandparents.\n\n{NOT_MED}\n\n#babyfood #newparents #canadianparents #babysafety #startingsolids",
     HONEY_SRC)

# Oct 24, 19:00 · BONDING REPLACEMENT (same id/slot, Oct 19; the grandma-gift RESP angle goes to backlog to keep kids' money to
# ~1 in 4 of my slots) · dads and partners: bond through daily care, not feeds. Parent Club (Scottish Government) + NHS skin to skin.
# Rule that stays: "Don't wait for a turn. Take a job."
DAD_SRC = ("Sources: Parent Club (Scottish Government / Public Health Scotland), Bonding tips for dads and partners: skin to skin "
           "on your bare chest can release oxytocin and build feelings of love, calm and connection (cover baby with a blanket; only "
           "lie baby on your chest when you're fully awake and sober); chat and play peekaboo during nappy changes; play and chat at "
           "bath time; read a daily story, baby enjoys hearing your voice; bonding can take time. NHS Start for Life, Skin-to-skin "
           "contact with your newborn. Ideas (not quotes) from John Medina, Brain Rules for Baby. Scripts are our own.")

reel("lf-reel-1024-grandma-resp", LF, "2026-10-24T19:00", "deep", "lf-x-tiny-parade", "send this to a new dad", [
    dict(k="hook", f="pink", text="Partners: you don't / need to feed baby / *to bond.*", emo="🫶"),
    dict(k="because", f="cream", kicker="here's how it's built", text="In *small, daily* care. The same jobs, *every day.*"),
    dict(k="say", f="butter", text="*Own bath time.* / Same song, / every night.", drop=True),
    dict(k="say", f="cream", text="Skin to skin / works for *you too.*"),
    dict(k="say", f="berry", text="Diaper change? / *Talk the whole way.*"),
    dict(k="say", f="pink", text="*One story* a night. / Your voice becomes / *bedtime.*"),
    dict(k="do", f="cream", text="Tonight, take bath time: *same time, same song, your job.*"),
    dict(k="save", f="pink", text="Don't wait for a turn. / Take a job."),
], "Partners: you don't need to feed the baby to bond with them.\n\n"
   "Bonding is built in small, daily care: the same jobs, done by the same person, every day. Here's how to own a few.\n\n"
   "1. OWN BATH TIME. Same time, same song, every night. Chat and play the whole way through. It becomes your thing.\n"
   "2. SKIN TO SKIN. It works for partners too: shirt off, baby in just a diaper on your bare chest, a blanket over you both. Only "
   "when you're fully awake. Feeling sleepy? Baby goes on their back in their own crib.\n"
   "3. TALK THROUGH THE DIAPER CHANGE. \"Left leg… right leg! Where did your toes go? There they are!\" Peekaboo counts.\n"
   "4. ONE STORY, EVERY NIGHT. Babies enjoy hearing your voice long before they follow the words.\n\n"
   "GIVE IT TIME: bonding doesn't always feel like a lightning bolt. Week 1 can feel like you're just the helper. By month 1, bath "
   "time is your routine together. Picture year 1: the one they reach for when the water's running.\n\n"
   "Do this: tonight, take bath time. Same time, same song, your job, from now on.\n\n"
   "The rule that stays: don't wait for a turn. Take a job.\n\n"
   "Send this to a new dad, or any partner who feels like a spare pair of hands.\n\n"
   f"{NOT_MED}\n\n#newdad #dadsofinstagram #bonding #newparents #skintoskin",
   DAD_SRC)


# ================================================================== Oct 25 (day B: quiz · Reels carry the crying lesson, part 1 -> 2)
CRY_SRC = ("Sources: NHS (South Tees Hospitals, ICON 'Babies cry, you can cope'): crying often starts around 2 weeks, peaks at around "
           "6 to 8 weeks for a term baby, then gradually decreases; 'It's OK to walk away if you have checked the baby is safe and the "
           "crying is getting to you'; 'Never ever shake or hurt a baby.' NHS, 'Soothing a crying baby': if it's overwhelming, put "
           "baby safely in their cot, step into another room for a set time like 10 minutes, then go back; contact a doctor if baby "
           "seems unwell or the cry doesn't sound like their normal cry.")

reel("lf-reel-1025am-crying-peak", LF, "2026-10-25T08:00", "deep", "lf-x-sunny-bounce", "send this to someone in the newborn weeks", [
    dict(k="hook", f="butter", text="“You'll *spoil her.*” / *Not true.*", emo="🍼"),
    dict(k="because", f="pink", kicker="the AAP says", text="You *can't spoil* a young baby with *attention.*"),
    dict(k="say", f="berry", text="Answer cries early, / and they *cry less.*", drop=True),
    dict(k="say", f="cream", text="Crying peaks at / *6 to 8 weeks.* / Then it eases."),
    dict(k="say", f="butter", text="Rock. Sing. / *Walk.* Warm bath."),
    dict(k="say", f="pink", text="*One at a time,* / a few minutes each."),
    dict(k="do", f="cream", text="Next cry: check *fed, changed, warm.* Then *rock and sing.*"),
    dict(k="save", f="pink", text="Pick them up. / You can't spoil / a newborn.", next="part 2 tonight at 7"),
], "\"Don't pick her up, you'll spoil her.\" You've heard it. It's not true.\n\n"
   "THE SCIENCE: the American Academy of Pediatrics says you cannot spoil a young baby with attention, and that if you answer their "
   "calls for help, they'll cry less overall. Responding quickly in the first few months is the best way to handle crying.\n\n"
   "THE TIMELINE (NHS): crying often starts building around 2 weeks, peaks around 6 to 8 weeks, then slowly eases. It's a normal "
   "stage, not a sign you're doing it wrong.\n\n"
   "YOUR CALM-DOWN KIT (check fed, changed, warm first):\n"
   "• Rock: in a chair, or sway in your arms.\n"
   "• Sing or talk: the same song every time.\n"
   "• Walk: in your arms or the stroller.\n"
   "• Steady soft sounds, gentle back pats, a burp, a warm bath.\n"
   "Try one at a time for a few minutes before switching.\n\n"
   "If the cry sounds different from usual, or baby seems unwell (fever, not feeding, floppy), call your doctor or your health line "
   "(811 in most provinces).\n\n"
   "WEEK 2 → WEEK 8 → MONTH 3: the build, the peak, the ease. Every time you pick them up on the way through, baby learns the "
   "world answers.\n\n"
   "Do this: next cry, check fed, changed, warm. Then rock and sing, the same song every time.\n\n"
   "The rule that stays: pick them up. You can't spoil a newborn.\n\n"
   f"Send this to someone in the newborn weeks. Part 2 tonight at 7: what to do when nothing works.\n\n{NOT_MED}\n\n"
   "#newborn #newparents #babycrying #canadianparents #fourthtrimester",
   CRY_SRC + " American Academy of Pediatrics, healthychildren.org, Responding to your baby's cries: 'You cannot spoil a young baby "
             "with attention, and if you answer their calls for help, they'll cry less overall'; respond promptly during the first "
             "few months; soothing ideas include rocking, gentle stroking or patting, singing or talking, soft music, walking, "
             "rhythmic sounds, burping and a warm bath.", series="Crying · part 1/2")

chain("lf-ch-1025", LF, "2026-10-25", "lf22", "calmer newborn days", [  # day B: guess-and-reveal quiz
    dict(k="bubbles", f="cream", label="quick quiz", title="Newborn crying / *peaks* at…", bubbles=[
        ("in", "when is it usually worst?"), ("out", "A) the first week"), ("out", "B) 6 to 8 weeks")],
         obj="shoe", tap="guess, then tap →"),
    dict(k="payoff", f="butter", label="the answer: B", text="*6 to 8* / weeks", sub="then it slowly eases", obj="point",
         tap="source: NHS · tap →"),
    dict(k="payoff", f="pink", label="and pick them up", text="You *can't spoil* / a newborn.", sub="answer early, they cry less · AAP", obj="clock",
         tap="next story →"),
    dict(k="handoff", f="cream", text="Baby won't stop / *crying?*", img="lf-1025-follow-crying/01.jpg", next="follow your line"),
])

reel("lf-reel-1025-step-away", LF, "2026-10-25T19:00", "deep", "lf-x-tiny-parade", "send this to every new parent", [
    dict(k="hook", f="pink", text="Still crying. / *You're at your limit.*", emo="🤍"),
    dict(k="because", f="butter", kicker="the NHS says", text="It's *OK to walk away* once baby is *safe.*"),
    dict(k="say", f="cream", text="1. Baby *on their back* / in the crib.", drop=True),
    dict(k="say", f="pink", text="2. Close the door. / *Another room,* / *10 minutes.*"),
    dict(k="say", f="butter", text="3. Breathe. Text: / *“Can you come?”*"),
    dict(k="say", f="cream", text="4. Go back *calmer.*"),
    dict(k="say", f="berry", text="*Never* shake / a baby. *Never.*"),
    dict(k="do", f="cream", text="Tonight, pick your *step-away person* and tell them they're it."),
    dict(k="save", f="pink", text="Safe crib. Closed door. / Ten minutes.", next="crying · part 2/2"),
], "Tried everything, still crying, and you're at your limit? That happens to loving parents too. Here's the plan.\n\n"
   "THE NHS ICON ADVICE: crying is normal, comfort can help, and it's OK to walk away if you've checked baby is safe and the crying "
   "is getting to you. Never, ever shake a baby: shaking can cause serious brain injury.\n\n"
   "THE 10-MINUTE RESET:\n"
   "1. Put baby on their back in their crib or bassinet, with nothing else in it.\n"
   "2. Close the door and go to another room for a set time, like 10 minutes.\n"
   "3. Breathe out slowly. Make a tea. Text your person: \"Can you come?\" or \"Can you talk?\"\n"
   "4. Go back, check baby, and start again calmer.\n\n"
   "If baby seems unwell, or the cry sounds different from usual, call your doctor or your health line (811 in most provinces). "
   "In an emergency, call 911.\n\n"
   "AND FOR YOU: if the crying leaves you feeling hopeless for weeks, tell your doctor or midwife. That's part of postpartum care too.\n\n"
   "Do this: tonight, pick your step-away person (partner, friend, sister) and tell them they're it.\n\n"
   "The rule that stays: safe crib, closed door, ten minutes.\n\n"
   f"Send this to every new parent. Part 2 of 2.\n\n{NOT_MED}\n\n#newparents #newborn #babycrying #parentingsupport #canadianparents",
   CRY_SRC + " NHS ICON programme (iconcope.org): Infant crying is normal; Comfort methods can help; It's OK to walk away; Never, "
             "ever shake a baby. Shaking a baby can cause serious brain injury.", series="Crying · part 2/2")


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

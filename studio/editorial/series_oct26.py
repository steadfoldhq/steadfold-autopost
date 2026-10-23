#!/usr/bin/env python3
"""Follow engine (Social studio v4, Oct 22): one numbered recurring series per page, Mon/Wed/Fri at the 5 pm feed slot,
same cover layout every episode (pills + series badge kicker + the series promise in the handwritten line), number on
the cover. Episode 1 of each ships Mon Oct 26. Hooks picked by a fresh stranger-test subagent from 3 options each.

    python3 studio/editorial/series_oct26.py          -> media/<id>/0N.jpg + schedule entries
"""
import json, sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import specs  # noqa: E402
import covers as C  # noqa: E402

FF, HB, LH, LF = "fullyfunded", "hourback", "lockedhour", "littlefold"
NOT_MED = "General information only, not medical advice."
NG = "Not guaranteed. Returns vary."
FOLLOW = {
    LF: "Follow for one calm thing a night, from bump to toddler.",
    LH: "Follow for one small focus fix a day, each one backed by research.",
    FF: "Follow for one money move a day, in plain words.",
    HB: "Follow to learn what AI can really do, one real test a day.",
}

EP = {}


def ep(pid, brand, at, cover, slides, caption, comment):
    specs.POSTS[pid] = dict(brand=brand, cover=cover, slides=slides, fmt="series")
    EP[pid] = dict(brand=brand, at=at, caption=caption, comment=comment)


# ------------------------------------------------------------------ Littlefold · 3 am Club No. 1
ep("lf-3amclub-01", LF, "2026-10-26T17:00:00-04:00",
   dict(lay="pills", f="berry", kicker="3 am club · no. 1", text="It's 3 am. / You're feeding. / *Eyes closing.*", obj="clock", at="br",
        save="night tips: mon · wed · fri"),
   [dict(f="cream", text="Never the / *sofa.* Never / the *armchair.*", sub="sleepy? put baby in their crib, on their back")],
   ("It's 3 am. You're feeding. Your eyes keep closing.\n\n"
    "3 am Club No. 1: where you feed matters most on the nights you're running on empty.\n\n"
    "THE RULE: falling asleep with your baby on a sofa or armchair is one of the riskiest places to doze off together. "
    "If there's any chance you'll nod off, move before you sit down.\n\n"
    "SET UP YOUR 3 AM SPOT BEFORE BED (5 minutes):\n"
    "1. Pick the spot now, while you're awake: never the sofa or armchair. Safest is baby back in their own crib beside you.\n"
    "2. If you feed in bed and might doze, keep pillows and duvets away from baby.\n"
    "3. Baby's own sleep space (crib or bassinet, flat, firm, empty) within arm's reach.\n"
    "4. Water, a dim light and your phone charger by the spot, so you don't end up on the sofa.\n"
    "5. After the feed, baby goes back in their own space, on their back.\n\n"
    "THE CATCH: no spot is risk-free if you've been drinking, smoke, or take medicine that makes you drowsy, or if your baby was premature or low birth weight. Then baby sleeps in their own space only.\n\n"
    "Do this: tonight, set up your 3 am spot before you go to bed.\n\n"
    "3 am Club No. 2 is Wednesday at 5 pm: what to do when the baby is wide awake at 3 am.\n\n"
    + FOLLOW[LF] + "\n\n" + NOT_MED + "\n\n#newborn #nightfeeds #safesleep #newparents #3amclub"),
   ("Sources: NHS, 'Sudden infant death syndrome (SIDS)': do not sleep on a sofa or armchair with your baby; put baby on their back "
    "in their own cot or Moses basket. The Lullaby Trust, 'Safer sleep advice': if you think you might fall asleep while feeding, it is "
    "safer to do so in an adult bed clear of pillows and duvets than on a sofa or armchair; risk is much higher after alcohol, drugs or "
    "smoking. Government of Canada, 'Safe sleep for your baby': avoid sleeping with your baby on a sofa, armchair or couch; baby sleeps on "
    "their back in a crib, cradle or bassinet."))

# ------------------------------------------------------------------ Locked Hour · One Word No. 1
ep("lh-oneword-01", LH, "2026-10-26T17:00:00-04:00",
   dict(lay="pills", f="pink", kicker="one word · no. 1", text="Inbox open / *all day* / again?", obj="clock", at="bl",
        save="mon · wed · fri"),
   [dict(f="cream", text="*Batch.*", sub="3 email checks a day, not all day"),
    dict(f="dots", text="Less / *stress.*", sub="fewer checks, calmer days")],
   ("Inbox open all day again? Today's word: Batch.\n\n"
    "One Word No. 1. Each episode is one word that guards your focus.\n\n"
    "THE RESEARCH: in a 2-week study, people who checked email only 3 times a day felt less stressed than when they could check as often "
    "as they liked.\n\n"
    "HOW TO BATCH:\n"
    "1. Pick 3 times: say 9:30, 1:00 and 4:30.\n"
    "2. Close the email tab (and turn off email notifications) between them.\n"
    "3. At each check: reply, file or schedule. Nothing stays \"unread to deal with later\".\n"
    "4. Worried about missing something urgent? Tell people to call or text for urgent things.\n\n"
    "THE CATCH: if your job is answering email (support, dispatch), batch something else, like chat or news.\n\n"
    "Do this: tomorrow, write your 3 check times on a sticky note and close the tab.\n\n"
    "One Word No. 2 is Wednesday at 5 pm.\n\n"
    + FOLLOW[LH] + "\n\n#focus #productivity #email #deepwork #oneword"),
   ("Source: Kushlev, K. & Dunn, E. W. (2015), 'Checking email less frequently reduces stress', Computers in Human Behavior 43, 220-228: "
    "124 adults; limiting email checks to 3 times a day for one week lowered daily stress compared with unlimited checking."))

# ------------------------------------------------------------------ Fully Funded · Rich Habits, Decoded No. 1
ep("ff-richhabits-01", FF, "2026-10-26T17:00:00-04:00",
   dict(lay="pills", f="coral", kicker="rich habits, decoded · no. 1", text="Paid Friday. / *Broke by* / *Wednesday?*", obj="piggy", at="br",
        save="mon · wed · fri"),
   [dict(f="lite", text="Pay *yourself* / first.", sub="move it the day it lands"),
    dict(f="cob", text="Savings rose / *3.5% → 13.6%*", sub="when savings rose with every raise")],
   ("Paid Friday. Broke by Wednesday? The habit: pay yourself first.\n\n"
    "Rich Habits, Decoded No. 1. Each episode takes one money habit and shows you how to do it on a normal paycheque.\n\n"
    "WHAT IT MEANS: savings come out the day your pay lands, automatically, before you can spend it. You live on what's left, "
    "instead of saving what's left.\n\n"
    "WHY IT WORKS: you don't rely on willpower. In the 'Save More Tomorrow' study, workers who signed up to save automatically, "
    "with the rate rising at each raise, went from saving 3.5% of pay to 13.6% in about 3.5 years.\n\n"
    "HOW TO DO IT (10 minutes in your banking app):\n"
    "1. Open a separate savings account (ideally one that pays interest and that you don't see every day).\n"
    "2. Set an automatic transfer for payday. Start at 10%; if that's too much, start at 1% or 2%.\n"
    "3. Every raise: add 1 percentage point.\n"
    "4. Leave it. The point is not having to decide again.\n\n"
    "THE CATCH: if you carry card debt at 20%+, point the automatic payment at that first. Keep a small buffer so the transfer never bounces.\n\n"
    "Do this: set one automatic transfer for your next payday, even if it's $10.\n\n"
    "Rich Habits, Decoded No. 2 is Wednesday at 5 pm.\n\nEducation only, not financial advice.\n\n"
    + FOLLOW[FF] + "\n\n#personalfinance #savingmoney #payyourselffirst #moneytips #richhabits"),
   ("Source: Thaler, R. H. & Benartzi, S. (2004), 'Save More Tomorrow: Using Behavioral Economics to Increase Employee Saving', "
    "Journal of Political Economy 112(S1): average saving rates for participants rose from 3.5% to 13.6% over 40 months. "
    "Education only, not financial advice."))

# ------------------------------------------------------------------ Hourback · AI, for real · Day 8
HB_RUN = ("Request (made up): \"Plan a birthday dinner for 6 people, $150 budget. Before you answer, ask me 3 questions.\"\n\n"
          "The AI's reply (Claude, by Anthropic, run Oct 22, 2026), the 3 questions as asked; each came with a line on why it matters:\n"
          "\"Before I plan the birthday dinner, I have 3 questions:\n1. Dining out or cooking at home?\n"
          "2. Any dietary restrictions, allergies, or cuisine preferences in the group?\n"
          "3. Does the $150 need to cover everything, or only food?\"\n"
          "Then: \"Once you answer, I'll build the full plan: menu or restaurant shortlist, itemized budget, timeline, and shopping or booking list.\"")
ep("hb-day8-ask-me-first", HB, "2026-10-26T17:45:00-04:00",
   dict(lay="pills", f="orng", kicker="ai, for real · day 8", text="AI's answer / felt *generic* / *again?*", obj="chat", at="bl",
        save="mon · wed · fri"),
   [dict(f="indi", text="Before you answer, / *ask me* / *3 questions.*", sub="add this line to any request"),
    dict(f="yel", text="Birthday dinner, / 6 people, $150. / *It asked me:*", items=["Out, or at home?", "Any allergies or diets?", "Does $150 cover it all?"], sub="real reply, shortened")],
   ("AI's answer felt generic again? Add one line: \"Before you answer, ask me 3 questions.\"\n\n"
    "AI, for real · Day 8. One real test of what AI can do, with the output shown.\n\n"
    "WHY IT WORKS: a chatbot fills every gap in your request with the most average guess. Asking it to question you first "
    "makes it name the gaps, and you fill them with your real details.\n\n"
    "THE REAL TEST:\n" + HB_RUN + "\n\n"
    "Answer those 3, and the plan you get is yours, not a generic one.\n\n"
    "WHERE IT HELPS: trip plans, cover letters, meal plans, gift ideas, anything where \"it depends\".\n\n"
    "PRIVACY TIP: answer the questions without full names, addresses or account numbers. \"My sister\" works fine.\n\n"
    "Do this: next time you ask AI for a plan, end with \"Before you answer, ask me 3 questions.\"\n\n"
    "AI, for real · Day 9 is Wednesday at 5:45 pm.\n\n"
    + FOLLOW[HB] + "\n\n#ai #chatgpt #claude #aitips #learnai"),
   ("Made-up request, real output: run in Claude (Anthropic) on Oct 22, 2026, in a fresh chat with no other context. The 3 questions and the closing line are quoted exactly; the explanation under each question is left out for length. Results vary between apps and runs."))


def main():
    built = C.build_feed(list(EP))
    p = REPO / "schedule" / "posts.json"
    d = json.loads(p.read_text())
    have = {x["id"] for x in d["posts"]}
    for pid, m in EP.items():
        entry = dict(id=pid, account=m["brand"], publish_at=m["at"], caption=m["caption"], first_comment=m["comment"],
                     alt_text=C.alt_text(pid), images=built[pid])
        if pid in have:
            d["posts"] = [entry if x["id"] == pid else x for x in d["posts"]]
        else:
            d["posts"].append(entry)
    d["posts"].sort(key=lambda x: (x["publish_at"], x["id"]))
    p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()

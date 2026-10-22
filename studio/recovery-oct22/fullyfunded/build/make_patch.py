#!/usr/bin/env python3
"""Writes ../patch.json (all queued FF items, keep/improve/replace) from the queue snapshot + the new copy below."""
import json
from pathlib import Path
REPO = Path("/home/claude/steadfold-autopost")
P = {p["id"]: p for p in json.loads((REPO / "schedule/posts.json").read_text())["posts"]}
S = json.loads((REPO / "state/published.json").read_text())["posts"]
Q = sorted([p for p in P.values() if p.get("account") == "fullyfunded" and p["id"] not in S], key=lambda p: p["publish_at"])
FOLLOW = "Follow for one money move a day, in plain words."
NEW = {}

# ---------------------------------------------------------------- Sat 12:00 carousel: caption only
NEW["ff-1024-paycheque-trail"] = dict(
    action="improve",
    reason="Caption only. Drops the 🇨🇦 flag (B19 Canada cap; the order itself isn't Canada-specific) and the unsourced 'a lot of planners use'; adds the debt catch and the follow reason. Slides kept: the 12:15 Story (ff-ch-1024-5) shows this exact cover.",
    new=dict(
        caption=("Payday. Where should the money go first? Follow this order.\n\n"
                 "1. A safety net: one month of bills in savings, then build toward 3 to 6 months.\n"
                 "2. If your employer matches retirement savings, put in enough to get the full match. Skip it and you leave part of your pay on the table.\n"
                 "3. Then invest in your TFSA, in a low-fee index fund, and leave it alone.\n\n"
                 "Why this order: the safety net keeps a surprise bill off your credit card. The match only pays if you put money in. Then time does the rest.\n\n"
                 "The catch: carrying card debt at 20% or more? Paying it down usually comes before step 3.\n\n"
                 "Do this: this payday, set up one automatic transfer to stop 1. Add the others as you go.\n\n"
                 "Not guaranteed. Returns vary. Education, not advice.\n\n" + FOLLOW +
                 "\n\n#personalfinancecanada #payday #tfsa #emergencyfund #moneytips"),
        first_comment=("Which stop are you at? Your situation may differ: high-interest debt usually comes before investing. "
                       "2026 TFSA dollar limit: $7,000 (CRA, canada.ca, 'TFSA contribution room'). Education, not advice."),
    ))

# ---------------------------------------------------------------- Sun 8:15 am Trial Reel: replaced
NEW["ff-pan-1025am-paycheque-trail"] = dict(
    action="replace",
    reason="Duplicate of Sat noon carousel ff-1024-paycheque-trail (same illustration, same caption word for word, piggy cut-out). Replaced with the Performance desk's order 5 (3rd day): 'Not married? No will?' (FF's biggest batch, 115) re-cut to 14.8 s as this Trial Reel slot, in the v0.5 drawn-to-scale look; payoff ($0) lands at 0.3 s.",
    new=dict(
        video="recovery-oct22/fullyfunded/ff-pan-1025am-wills-s15.mp4",
        cover="recovery-oct22/fullyfunded/ff-pan-1025am-wills-s15-cover.jpg",
        caption=("Not married? No will? In Ontario, your partner may get nothing.\n\n"
                 "If you die without a will in Ontario, the law decides who inherits:\n"
                 "Married spouse: everything if the estate is under $350,000; otherwise the first $350,000, and the rest is shared with your children.\n"
                 "Common-law partner: nothing under these rules, even after years together. They may have to go to court to ask for support.\n\n"
                 "The fix is one will. It says who gets what, and who you'd want to raise your kids.\n\n"
                 "Do this: this week, book one call with a wills lawyer and ask, \"What does a will and power of attorney cost for both of us?\"\n\n"
                 "Other provinces have different rules, so check yours.\n\n"
                 "Send this to your partner.\n\n" + FOLLOW +
                 "\n\n#wills #estateplanning #commonlaw #personalfinancecanada #moneyfoundations"),
        first_comment=("Sources: Steps to Justice (CLEO, Community Legal Education Ontario), 'Learn what happens to your property if you die without a will' "
                       "(stepstojustice.ca): a married spouse gets everything if the estate is under $350,000, otherwise the first $350,000 (deaths on or after "
                       "March 1, 2021) and the rest is shared with the children; the intestacy rules leave nothing to a common-law partner, who may be able to "
                       "make a dependant's support claim in court. Ontario Succession Law Reform Act, R.S.O. 1990, c. S.26, Part II (intestacy) and Part V "
                       "(dependants' support), ontario.ca/laws. Rules differ by province. General information, not legal advice."),
        alt_text=("Edited video on a blueprint-grid sheet in the Fully Funded look. Frame 1: 'Not married? No will?' in a large serif, over a drawn "
                  "diagram: an ESTATE box piped to two rooms, MARRIED (ticked) and COMMON-LAW, whose pipe is valved shut; a coral $0 stamps into the "
                  "common-law room. Then 'In Ontario:' with a bar drawn to scale, MARRIED: first $350,000, and COMMON-LAW: $0. Then 'The fix: one will.' "
                  "as a document draws itself and is signed. Then 'Do this: Book a wills call this week.' It loops back to the opening."),
    ))

# ---------------------------------------------------------------- Sun 7 pm Reel: re-cut
NEW["ff-reel-1025-tfsa-withdrawal-trap"] = dict(
    action="improve",
    reason="Same facts and hook, re-cut: the 3rd pointing-hand template in 5 FF Reels (clip-art overused) with a static hook until ~3 s. Now a calendar drawn to scale: out in March / back in June on frame 0, '$5,000 over = $50 a month' and the $350 roll-up by ~4 s, 'Room returns January 1', 'Do this'. 14.8 s.",
    new=dict(
        video="recovery-oct22/fullyfunded/ff-reel-1025-tfsa-trap-s15.mp4",
        cover="recovery-oct22/fullyfunded/ff-reel-1025-tfsa-trap-s15-cover.jpg",
        caption=("Putting TFSA money back? Wait. Here's the trap.\n\n"
                 "You take out $5,000 in March and put it back in June. Feels harmless. But the room from a withdrawal only comes back on January 1 "
                 "of the next year. If you had no other room left, that $5,000 is an over-contribution, and the CRA charges 1% a month on it until it's "
                 "out: $50 a month, about $350 from June to December.\n\n"
                 "Do this: before you put money back, check your room in CRA My Account (it shows your room as of January 1). Moving money between banks? "
                 "Ask for a direct transfer, which doesn't count as a withdrawal.\n\n"
                 "Already did it? Take the extra out as soon as you can, and look up form RC243 (the TFSA return) on canada.ca.\n\n"
                 "The rule to remember: out this year? Back in January.\n\n"
                 "Send this to your TFSA friend.\n\n" + FOLLOW +
                 "\n\n#TFSA #personalfinancecanada #CRA #taxtips #moneyfoundations"),
        first_comment=("Sources: CRA (canada.ca), 'Before you contribute to a TFSA' and the TFSA withdrawal pages: withdrawals are added back to your "
                       "contribution room at the beginning of the following year; an excess amount is taxed 1% per month for each month it stays in the "
                       "account; direct transfers between your own TFSAs are not withdrawals; excess amounts are reported on form RC243. Your room as of "
                       "January 1 is in CRA My Account (subtract this year's deposits). Maths: 1% of $5,000 = $50 for each month the excess stays in; "
                       "June through December = 7 months = $350. Education, not tax advice."),
        alt_text=("Edited video on a cream blueprint-grid sheet. Frame 1: 'Putting TFSA money back? Wait.' in a large serif over a calendar ruler "
                  "drawn to scale, January to December, with a coral arrow out at March and a blue arrow back in at June. Then 'Over by $5,000? "
                  "$50 a month tax.' as June to December fills with seven coral cells and a counter rolls to $350. Then 'Room returns January 1.' with "
                  "an arc to next January. Then 'Do this: Check CRA My Account first.' It loops back to the opening."),
    ))

# ---------------------------------------------------------------- Mon 5 pm series cover
rh = P["ff-richhabits-01"]
NEW["ff-richhabits-01"] = dict(
    action="improve",
    reason="Series layout kept (badge kicker, pills, save-line, stamp). The overused halftone piggy becomes a drawn-to-scale 'paycheque left, Fri → Wed' chart; slide 3 now says 'saving rate … in one study' with the source on the tile; the caption's 'about 3.5 years' (the paper says 40 months) is corrected.",
    new=dict(
        images=[f"recovery-oct22/fullyfunded/ff-richhabits-01/0{i}.jpg" for i in (1, 2, 3)],
        caption=rh["caption"].replace("went from saving 3.5% of pay to 13.6% in about 3.5 years.", "went from saving 3.5% of pay to 13.6% over 40 months."),
        alt_text=("Fully Funded 3-slide carousel. Slide 1: 'Rich Habits, Decoded · No. 1' badge, then 'Paid Friday. Broke by Wednesday?' in a large serif "
                  "with highlighted words, the handwritten note 'mon · wed · fri' and a small drawn chart, 'paycheque left', with bars shrinking from "
                  "Friday to an empty Wednesday. Slide 2: Pay yourself first. (move it the day it lands). Slide 3: Saving rate 3.5% → 13.6% (in one "
                  "study, as it rose with every raise). Source: Thaler & Benartzi, 2004."),
    ))
assert "over 40 months" in NEW["ff-richhabits-01"]["new"]["caption"]

KEEP = {
    "ff-1022-streak-every-dollar": "Publishes in <24 h, no rule broken; sourced (StatCan SHS 2023). 7 slides and an emoji-cash cover are weak spots for the next build.",
    "ff-reel-1022-refund-29k": "<24 h; 13.7 s, hook in the viewer's words, number on screen by 3.5 s, maths checked ($1,480 → ≈$29,400 at 10%).",
    "ff-1023-cpp-enough": "<24 h; canada.ca-sourced. Caption line 4 has a typo '$1,620.0' (cosmetic; owner may fix, not a rule break).",
    "ff-1023-roadmap-fhsa": "<24 h; FHSA facts match Finance Canada/CRA; 'returns vary' present.",
    "ff-reel-1023-cpp-60-or-70": "<24 h; 13.1 s, hourglass object, canada.ca figures; education framing kept.",
    "ff-reel-1024am-sick-pay-gap": "Before the Sat 12:00 line; 13.1 s; EI figures sourced. Pointing-hand template (overused) is the only flaw, not a rule break.",
    "ff-1024-follow-fees": "Maths re-run: $1,081,819 / $882,535 / $688,165 (gap ≈$393,700); quiet follow-the-line style; disclaimers present.",
    "ff-reel-1024-beneficiary": "12.6 s rule open, payoff ($750) by 3.5 s, ontario.ca-sourced. Kept on the pointing-hand template so FF's weekend Reels still alternate styles (hand → drawn-to-scale → hand-free); re-cut candidate for next week.",
    "ff-1025-tfsa-room": "CRA limits re-added: $109,000 ✓; growth maths re-run ✓ ($111,562 / $400,925 / $1,151,458). Set up by the Story chain and Part 7 of the series.",
    "ff-1025-hold-cost-of-waiting": "Maths re-run ✓ ($1,138,991 … $398,050). Last queued 'hold the dots' tile (log: kept as the last of its kind).",
}
out = []
for p in Q:
    pid = p["id"]
    if pid in NEW:
        out.append(dict(id=pid, **NEW[pid]))
    elif pid in KEEP:
        out.append(dict(id=pid, action="keep", reason=KEEP[pid]))
    elif p.get("story"):
        out.append(dict(id=pid, action="keep", reason="Story chain frame: matches its day's post, inside y 250-1650, sources named; no rule broken."))
    else:
        raise SystemExit("unclassified " + pid)
(REPO / "studio/recovery-oct22/fullyfunded/patch.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(len(out), {a: sum(1 for x in out if x["action"] == a) for a in ("keep", "improve", "replace", "hold")})

#!/usr/bin/env python3
"""Writes studio/editorial/nov03/fullyfunded.json (Fully Funded, Nov 3 studio run). Re-run after each piece is clean.
    python3 studio/editorial/nov03_fullyfunded_manifest.py [A] [B] [C]
"""
import json, subprocess, sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
OUTF = REPO / "studio/editorial/nov03/fullyfunded.json"
FOLLOW = "Follow for one money rule a day, in plain words."


def dur(rel):
    p = REPO / "media" / rel
    return round(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                               stdin=subprocess.DEVNULL).decode().strip()), 2)


A = dict(
    id="ff-reel-1106-hbp-couple", account="fullyfunded", publish_at="2026-11-06T19:00:00-05:00",
    video="studio-nov03/fullyfunded/ff-reel-1106-hbp-couple.mp4", cover="studio-nov03/fullyfunded/ff-reel-1106-hbp-couple-cover.jpg",
    caption=(
        "Buying together? Up to $60,000 each. In Canada, the Home Buyers' Plan (HBP) lets each first-time buyer take up to $60,000 "
        "out of their own RRSP to buy a home, without paying tax on it, as long as they pay it back a bit each year.\n\n"
        "WHY: the limit is per person, not per home. So a couple who both qualify and both have the money in their RRSPs can use up to "
        "$120,000 between them for the same home. The CRA's own first-home guide walks through a couple doing exactly this.\n\n"
        "HOW:\n"
        "1. Sign a written agreement to buy (or build) the home first.\n"
        "2. Each of you fills in form T1036 (Home Buyers' Plan request) and gives it to the bank or provider that holds your RRSP. "
        "One form for each withdrawal.\n"
        "3. Buy or build the home before October 1 of the year after your first withdrawal, and plan to live in it.\n"
        "4. Pay it back a bit each year, over 15 years: at least 1/15 of the total a year once repayments start (after the grace "
        "period, per CRA). The CRA shows your minimum each year on your HBP statement of account, with your notice of assessment. "
        "You can always pay back more.\n\n"
        "THE CATCH: it's a loan to yourself, not free money. You can only take what's already in your RRSP. Money you put into an RRSP in the 89 days before you take "
        "it out may not be deductible. A missed or short yearly payment is added to your income that year and taxed. And it all comes out of your retirement savings until you pay it back.\n\n"
        "WHO THIS IS FOR: residents of Canada who count as first-time buyers: in the year you withdraw or the 4 years before it, you "
        "didn't live in a home that you owned. A home your current spouse or common-law partner owned counts too: if you lived in "
        "their home in that time, you don't qualify (CRA). Right now, for a first withdrawal from "
        "2022 to 2028, repayments start the fifth year after it (CRA).\n\n"
        "Do this: sign the deal to buy, then each ask your RRSP bank for form T1036.\n\n"
        "Send this to the person you're house-hunting with.\n\n"
        "Education only, not financial advice.\n\n"
        f"{FOLLOW}\n\n"
        "#personalfinancecanada #firsthome #homebuyersplan #rrsp #canadianmoney"),
    first_comment=(
        "Sources (checked Nov 3 2026, rules for 2026):\n"
        "• CRA, 'Saving for the first home' (canada.ca/en/revenue-agency/campaigns/life-events/saving-first-home.html, modified 2026-02-25): "
        "in its story about a couple, the HBP 'allows each of them to withdraw up to $60,000 from their RRSPs, tax-free.'\n"
        "• CRA, 'How to make withdrawals from your RRSPs under the Home Buyers' Plan' (canada.ca): 'You cannot withdraw more than $60,000 in "
        "total under the HBP'; form T1036, a separate form for each withdrawal.\n"
        "• CRA, 'How to participate in the Home Buyers' Plan' (canada.ca, modified 2026-01-20): first-time buyer rule (no home you or your "
        "current spouse or common-law partner owned and lived in, this year or the 4 years before); written agreement to buy or build; "
        "resident of Canada; home acquired before October 1 of the year after the first withdrawal; 89-day contribution rule.\n"
        "• CRA, 'How to repay the amounts withdrawn from your RRSPs under the HBP' (canada.ca, modified 2026-01-20): up to 15 years; for a "
        "first withdrawal from Jan 1 2022 to Dec 31 2028 the repayment period starts the fifth year after; a missed minimum is included "
        "as RRSP income on line 12900."),
    alt_text=(
        "Fully Funded Reel. On cream dot paper, a blue pill says CANADA · HOME BUYERS' PLAN. Headline: 'Buying together? Up to "
        "$60,000 each.' A drawn house with a blue roof reading OUR FIRST HOME; its body is split in two. The left half fills blue and "
        "reads YOU, UP TO $60,000, then the right half fills coral and reads PARTNER, UP TO $60,000. Then: 'Each of you can borrow it "
        "from your own RRSP.' Next: 'Together: up to $120,000 for your home.' The roof reads UP TO and counts up to $120,000; "
        "handwritten: pay back a bit each year, over 15 years; then 'First-time buyers only: no home of your own in 4 years.' On "
        "cobalt: 'do this: Ask your RRSP bank for form T1036.' over a drawn FORM T1036 (Home Buyers' Plan, withdraw from RRSP, AMOUNT "
        "$60,000) whose box SIGNED AGREEMENT TO BUY gets ticked, and a white card: 'One each, once you sign to buy. Only money already "
        "in your RRSP.' Last: 'Send this to your partner.' above the full house with UP TO $120,000 on the roof, the handwritten line "
        "Follow for one money rule a day, in plain words, and the round brand stamp."),
    beats=[
        "CANADA · HOME BUYERS’ PLAN | Buying together? | Up to $60,000 each. | OUR FIRST HOME (house) | YOU | UP TO | $60,000 "
        "(left half fills 0.3 s) | PARTNER | UP TO | $60,000 (right half fills 0.7 s) | Each of you can borrow it from your own RRSP. "
        "(1.4 s)",
        "Together: up to $120,000 for your home. | roof: UP TO | $60,000 → $120,000 (counts) | YOU UP TO $60,000 | PARTNER UP TO "
        "$60,000 | pay back a bit each year, over 15 years | First-time buyers only: no home of your own in 4 years.",
        "(cobalt field) do this: | Ask your RRSP bank for form T1036. | FORM T1036 | HOME BUYERS' PLAN · WITHDRAW FROM RRSP | AMOUNT "
        "$60,000 | SIGNED AGREEMENT TO BUY (box ticks 0.45 s) | One each, once you sign to buy. Only money already in your RRSP.",
        "(cobalt field) Send this to your partner. | house roof: UP TO $120,000 | YOU UP TO $60,000 | PARTNER UP TO $60,000 | Follow "
        "for one money rule a day, in plain words. | (round brand stamp)",
        "(loop, hard cut) the frame-0 layout",
        "cover only (awards): CANADA · HOME BUYERS’ PLAN | Buying together? | Up to $60,000 each. | YOU UP TO $60,000 (blue "
        "rosette) | PARTNER UP TO $60,000 (coral rosette) | = up to $120,000 from your RRSPs | FIRST-TIME BUYERS · REPAY OVER 15 YEARS "
        "| (round brand stamp)",
    ],
    hook_options=["Buying together? Up to $60,000 each.", "Two RRSPs, one home: up to $120,000.",
                  "First home together? Up to $60,000 each."],
    style=("Reel body: illustrated 'rule drawn happening' scene (a drawn HOUSE split down the middle: the YOU half fills cobalt, the PARTNER "
           "half fills coral, each UP TO $60,000; then the roof counts to UP TO $120,000) on cream dot paper, then a do-this beat on cobalt with a drawn "
           "FORM T1036 (the SIGNED AGREEMENT TO BUY box ticks) and the end beat on cobalt with the full house kept on the end card; hard "
           "cuts. New vs Nov 4-5: the object fills up like two bars instead of a coin or a cut. Dedicated COVER: style 10 awards (quiet) on "
           "cream dot paper: serif hook + soft-coral pill, two drawn rosettes (YOU / PARTNER, UP TO $60,000), handwritten total, mono "
           "line, round stamp."),
    send_test=False,
    sources=[
        "https://www.canada.ca/en/revenue-agency/campaigns/life-events/saving-first-home.html",
        "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/withdraw-funds-rrsp-s-under-home-buyers-plan.html",
        "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/participate-home-buyers-plan.html",
        "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/repay-funds-withdrawn-rrsp-s-under-home-buyers-plan.html",
    ],
    notes=(
        "Standalone (no Part 2, no sequel framing). Desk order 5 (Nov 3): stays on Canadian partner/family rules; felt moment ('Buying "
        "together?') + a number you can picture ('$60,000 each') in frame 0 and caption line 1; 'Canada' on screen. Hook 5 words; payoff "
        "line at 1.4 s; do-this 7 words; follow beat 2.5 s. Facts checked Nov 3 2026 on canada.ca (4 CRA pages, tax year 2026). The CRA "
        "withdrawal pages state the limit per person but don't spell out 'both spouses for one home'; the CRA 'Saving for the first home' "
        "guide does (couple, 'each of them ... up to $60,000'). The Spring Economic Update 2026 (budget.canada.ca, 2026-04-28) mentions "
        "extending the repayment grace period; CRA's repay page already shows 2022-2028, so the caption uses CRA's wording only. "
        "Built by studio/editorial/nov03_fullyfunded.py (extends nov02/nov01). H.264 1080x1920 30 fps + AAC, 4.8 MB, -13.9 LUFS / -1.4 "
        "dBTP; music: existing ff-x-money-moves (tools/music-library.json; Nov 4 uses level-up, Nov 5 big-reveal). Grid: Nov 6 17:00 "
        "ff-richhabits-06 (series, loud) -> this cover style 10 awards (quiet); the 9 tiles Nov 1-6 then hold styles 13,3,1,9,8,10 (6 in 9). "
        "QG-1: QA frames + 2 fps strip of the final MP4 + cover reviewed by eye; fixed: do-this card overflow (shorter line, 56 px), layout "
        "moved toward vertical centre, house labels 80 px, end-card roof total in Inter Display, cover headline clipped at 120 px -> 104 "
        "px, rosette amounts spilling out of the circles -> bigger rosettes; 'within 15 years' -> 'over 15 years' (repayment can start years later), re-rendered 13.61 s. GATE r2 (Nov 3, clarity CONFUSING): 'up to' added on frame 0, both halves, the roof total, the end card and the cover (hook now 7 words, per the gate's wording); repayment on screen now 'pay back a bit each year, over 15 years'; caption adds the 1/15-a-year minimum once repayments start (after the grace period), a missed payment added to income that year, and that a home your spouse/partner owned counts for the 4-year rule (CRA). Re-rendered 13.61 s, 4.8 MB, -13.9 LUFS / -1.4 dBTP; 2 fps strip, the 5.6 s frame and the cover reviewed; cover mono line cut to 33 px to stay inside x 90-990. GATE r3: frame 0 + cover hook -> 'Buying together? Up to $60,000 each.' (6 words, inside the Reel cap); re-rendered; strip + cover reviewed."),
)
A["duration_s"] = None


def load_extra(name):
    p = REPO / "studio/editorial/nov03" / f".ff_{name}.json"
    return json.loads(p.read_text()) if p.exists() else None


def main():
    want = sys.argv[1:] or ["A", "B", "C"]
    out = []
    if "A" in want:
        A["duration_s"] = dur(A["video"])
        out.append(A)
    for k in ("B", "C"):
        if k in want:
            import nov03_fullyfunded_entries as E  # noqa: E402
            out.append(getattr(E, k)(dur))
    OUTF.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print("wrote", OUTF, [e["id"] for e in out], [e.get("duration_s") for e in out])


if __name__ == "__main__":
    sys.path.insert(0, str(REPO / "studio/editorial"))
    main()

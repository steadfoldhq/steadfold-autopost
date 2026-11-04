#!/usr/bin/env python3
"""Writes studio/editorial/nov04/fullyfunded.json (Fully Funded, Nov 4 studio run). Re-run after each piece is clean.
    python3 studio/editorial/nov04_fullyfunded_manifest.py [A] [C] [B]
"""
import json, subprocess, sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
OUTF = REPO / "studio/editorial/nov04/fullyfunded.json"
FOLLOW = "Follow for one money rule a day, in plain words."
PICKER = ("No Agent tool was available in this session (no fresh-stranger subagent could be launched), so the maker's own pick "
          "(first option) is used. Flag for the reviewer.")


def dur(rel):
    p = REPO / "media" / rel
    return round(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                               stdin=subprocess.DEVNULL).decode().strip()), 2)


A = dict(
    id="ff-reel-1108-medical-one-return", account="fullyfunded", publish_at="2026-11-08T19:00:00-05:00",
    video="studio-nov04/fullyfunded/ff-reel-1108-medical-one-return.mp4",
    cover="studio-nov04/fullyfunded/ff-reel-1108-medical-one-return-cover.jpg",
    caption=(
        "Dentist, glasses, pills: $2,000 this year? Claim them all on the lower earner's return.\n\n"
        "In Canada, one of you can claim the medical bills for both partners and your kids under 18, all together, on one tax "
        "return (line 33099).\n\n"
        "WHY: only the part of the bills above a floor counts. The floor is 3% of the claimer's net income, or a fixed amount if "
        "that is lower ($2,834 for 2025). A lower income means a lower floor, so more of the same bills count.\n\n"
        "The maths (made up for this post): $2,000 of bills. You earn $90,000: 3% is $2,700, so $0 counts. Your partner earns "
        "$40,000: 3% is $1,200, so $800 can be claimed. That $800 is not money back: the federal credit is 14% of it in 2026 "
        "(about $112 off the tax you owe), plus your province's own credit.\n\n"
        "HOW:\n"
        "1. Gather every receipt: dentist, prescription glasses, prescription drugs, and the rest of the CRA's list.\n"
        "2. Pick any 12-month period that ends in the tax year.\n"
        "3. Try line 33099 on both returns in your tax app, and keep the one that counts more.\n\n"
        "THE CATCH: it's a non-refundable credit, so it only lowers tax the claimer owes. If the lower earner owes little or no "
        "tax, the other return may work better, which is why you try both. Purely cosmetic work and over-the-counter medicine "
        "don't count. Keep the receipts.\n\n"
        "WHO THIS IS FOR: you, your spouse or common-law partner, and your or their kids under 18. Bills for other relatives who "
        "depend on you (an adult child, a parent) go on line 33199, with their own rules.\n\n"
        "Do this: Claim them on line 33099, on the return that counts more.\n\n"
        "Send this to whoever does the taxes in your home.\n\n"
        "Education only, not financial advice.\n\n"
        f"{FOLLOW}\n\n"
        "#personalfinancecanada #canadiantaxes #taxtips #medicalexpenses #canadianmoney"),
    first_comment=(
        "Sources (checked Nov 4 2026):\n"
        "• CRA, 'Medical Expenses 2025' (RC4065, canada.ca/en/revenue-agency/services/forms-publications/publications/rc4065/"
        "medical-expenses.html, modified 2026-01-20): line 33099 covers eligible expenses 'you or your spouse or common-law partner "
        "paid' for you, your spouse or partner, and your or their children under 18; you claim the total minus the lesser of $2,834 "
        "or 3% of your net income (line 23600); any 12-month period ending in 2025. In its worked story, 'Either Richard or Pauline "
        "can claim this amount on line 33099', and the lower-income partner (Richard, $42,000) gets the bigger claim ($5,040 vs "
        "$4,650). Lists dental services, prescription eyeglasses and prescription drugs; excludes purely cosmetic procedures and "
        "over-the-counter medicine.\n"
        "• Finance Canada, 'Report on the Impact of Reducing the Lowest Marginal Personal Income Tax Rate on Non-Refundable Tax "
        "Credits' (canada.ca): the rate for most non-refundable credits, including the medical expense credit, is based on the "
        "lowest personal income tax rate (14% in 2026). CRA 'Current year tax rates and income brackets (2026)': 14% on the "
        "first $58,523.\n"
        "The $2,000 of bills and the $90,000 / $40,000 incomes are made up for this post; the maths is ours (3% of income)."),
    alt_text=(
        "Fully Funded Reel. On cream dot paper, a blue pill says CANADA · MEDICAL EXPENSES. Headline: 'Dentist, glasses, pills: "
        "$2,000 this year?' A drawn receipt, FAMILY MEDICAL: DENTIST $900, GLASSES $650, PRESCRIPTIONS $450, TOTAL $2,000. Text: 'Claim them "
        "all on the lower earner's return.' Next: 'Only bills above 3% of income count.' Two drawn receipts side by side: YOU, "
        "EARNS $90,000, BILLS $2,000, 3% OF INCOME −$2,700, and a coral box: $0 CAN BE CLAIMED; PARTNER, EARNS $40,000, BILLS "
        "$2,000, 3% OF INCOME −$1,200, and a green box: $800 CAN BE CLAIMED. Handwritten: 'same bills, a bigger claim'. On cobalt: "
        "'do this: Claim them on line 33099.' A drawn tax-return card, YOUR TAX RETURN, LINE 33099 $2,000, with a ticked box: ON "
        "THE LOWER EARNER'S RETURN. A card: 'Try both returns in your tax app. Keep the one that counts more.' End: 'One return. "
        "The whole family's bills.' with the receipt, 'Follow for one money rule a day, in plain words.' and the round brand stamp."),
    beats=[
        "CANADA · MEDICAL EXPENSES | Dentist, glasses, pills: | $2,000 this year? | FAMILY MEDICAL (receipt) | DENTIST $900 | GLASSES $650 | "
        "PRESCRIPTIONS $450 | TOTAL $2,000 (fades in 0.3 s) | Claim them all on | the lower earner's return. (1.3 s)",
        "Only bills above | 3% of income count. | YOU | EARNS $90,000 | BILLS $2,000 | 3% OF INCOME | −$2,700 | $0 CAN BE CLAIMED "
        "| PARTNER | EARNS $40,000 | BILLS $2,000 | 3% OF INCOME | −$1,200 | $800 CAN BE CLAIMED | same bills, a bigger claim",
        "(cobalt field) do this: | Claim them on | line 33099. | YOUR TAX RETURN | LINE 33099 $2,000 | ON THE LOWER EARNER'S RETURN "
        "(box ticks 0.45 s) | Try both returns in your tax app. | Keep the one that counts more.",
        "(cobalt field) One return. | The whole family's bills. | receipt: FAMILY MEDICAL, DENTIST $900, GLASSES $650, "
        "PRESCRIPTIONS $450, TOTAL $2,000 | Follow for one money rule a day, in plain words. | (round brand stamp)",
        "(loop, hard cut) the frame-0 layout",
        "cover only: CANADA · MEDICAL EXPENSES | Dentist, glasses, pills: | $2,000 this year? | receipt (DENTIST $900, GLASSES $650, "
        "PRESCRIPTIONS $450, TOTAL $2,000) | claim them on the lower earner's return | LINE 33099 · YOU, PARTNER, KIDS UNDER 18 | "
        "(round brand stamp)",
    ],
    hook_options=["Dentist, glasses, pills: $2,000 this year?", "$2,000 in family medical bills?", "$2,000 of bills. Whose return?"],
    hook_picker=("Stranger picker (gate, Nov 4) chose 'Dentist, glasses, pills: $2,000 this year?' (was option 2), flagging that it "
                 "must not imply $2,000 always earns a credit; adopted on frame 0 and the cover, with the lower-earner payoff on "
                 "screen at 1.3 s."),
    style=("Reel body: illustrated 'rule drawn happening' scene (a drawn FAMILY MEDICAL receipt, $2,000; then the same bills "
           "measured on two tall receipts, one per return: YOU $90,000 → $0 CAN BE CLAIMED, PARTNER $40,000 → $800 CAN BE CLAIMED) on cream dot paper, a "
           "do-this beat on cobalt with a drawn tax-return card (LINE 33099, the ON THE LOWER EARNER'S RETURN box ticks) and the "
           "end beat on cobalt with the receipt kept; land / hard cuts. Dedicated COVER: style 1 Look B big-number cover (loud) "
           "on cream dot paper: serif hook + soft-coral pill, drawn receipt, handwritten line, mono line, round stamp."),
    send_test=False,
    sources=["CRA RC4065 'Medical Expenses 2025' (modified 2026-01-20), lines 33099/33199, threshold, 12-month period, Richard/Pauline story",
             "Finance Canada report on reducing the lowest rate and non-refundable credits: credit rate = lowest rate, 14% in 2026"],
    notes=(
        "Sun Nov 8 19:00 (no trial). Desk order 5 (FF HOLD): Canadian partner/family rule, felt moment + number on frame 0 "
        "('$2,000' in the hook, 6 words), 'Canada' on screen, drawn style, ONE drawn object (the receipt) doing the meaning. New "
        "topic family (tax return / credits), not on the 14-day list. No send line on screen: not a send-test Reel (send_test "
        "false); the caption has its one send line. Music: existing FF track media/music/library/v4/ff-x-big-reveal.mp3 "
        "(tools/music-library.json), -13.9 LUFS. 'Only bills above 3% of income count' simplifies the 'lesser of 3% or $2,834' "
        "floor; at the incomes shown 3% is the lower one, and the caption states the full rule. QG-1: strip + cover checked; "
        "fixed overlapping side receipts, a stamp over the card edge and a cover save-line past x 990 before the final encode. "
        "CD gate fix (Nov 4): comparison rebuilt as two taller receipts with ~95 px side margins, the 3% line at 42 px, the "
        "result boxes inside the borders and relabelled '$X CAN BE CLAIMED'; caption says the credit is 14% of it "
        "(Finance Canada: credit rate = lowest rate, 14% in 2026); hook switched to the picker's choice."),
)

B = dict(
    id="ff-reel-1109-spousal-rrsp-3yr", account="fullyfunded", publish_at="2026-11-09T19:00:00-05:00",
    video="studio-nov04/fullyfunded/ff-reel-1109-spousal-rrsp-3yr.mp4",
    cover="studio-nov04/fullyfunded/ff-reel-1109-spousal-rrsp-3yr-cover.jpg",
    caption=(
        "Earn twice what your partner does? Save in their RRSP, and you still get the tax break.\n\n"
        "In Canada, a spousal (or common-law partner) RRSP is an RRSP in your partner's name that you pay into. You claim the "
        "deduction on your own return. When the money comes out later, it's normally taxed as your partner's income, not yours.\n\n"
        "WHY: the higher earner gets the deduction now, and later the money is taxed in the hands of the partner with less "
        "income, often at a lower rate.\n\n"
        "THE 3-YEAR RULE: if you paid into any spousal RRSP in the year your partner takes money out, or in the 2 years before, "
        "that withdrawal is taxed as your income instead (form T2205). Last deposit in 2026? A withdrawal in 2029 or later is "
        "clear, as long as you add nothing in 2027 or 2028. Every new deposit restarts the 3-year clock.\n\n"
        "HOW:\n"
        "1. Ask your bank or brokerage to open a spousal RRSP: your partner owns it, you pay in.\n"
        "2. Pay in from your own RRSP room. It counts against your limit, not theirs.\n"
        "3. Claim the deduction on your return.\n"
        "4. Count 3 calendar years from your LAST deposit (not from opening the account) before your partner takes any out.\n\n"
        "THE CATCH: it uses your own RRSP room, and the money legally belongs to your partner. Take it out too soon and it's taxed "
        "as yours.\n\n"
        "WHO THIS IS FOR: married or common-law couples. You can keep paying in until the December your partner turns 71.\n\n"
        "Do this: Ask your bank for a spousal RRSP.\n\n"
        "Send this to your partner.\n\n"
        "Education only, not financial advice.\n\n"
        f"{FOLLOW}\n\n"
        "#personalfinancecanada #rrsp #spousalrrsp #canadiantaxes #canadianmoney"),
    first_comment=(
        "Sources (checked Nov 4 2026):\n"
        "• CRA, 'Withdrawing from spousal or common-law partner RRSPs' (canada.ca/en/revenue-agency/services/tax/individuals/topics/"
        "rrsps-related-plans/making-withdrawals/withdrawing-spousal-common-law-partner-rrsps.html, modified 2026-06-26): to avoid the "
        "contributor including the amount in income, they must not have contributed to any of their spouse's or partner's RRSPs in "
        "the withdrawal year or the two years before; form T2205.\n"
        "• CRA, 'Contributing to your spouse's or common-law partner's RRSPs' (canada.ca, modified 2026-01-29): the contributor "
        "claims the deduction; spousal contributions reduce the contributor's own RRSP deduction limit; you can contribute until "
        "the December of the year your spouse or partner turns 71.\n"
        "No incomes are shown in this post; 'twice' is the scenario, not a threshold."),
    alt_text=(
        "Fully Funded Reel. On pale blue dot paper, a blue pill says CANADA · SPOUSAL RRSP. Headline: 'Earn twice what your "
        "partner does?' A drawn account card, SPOUSAL RRSP: IN THE NAME OF, YOUR PARTNER (coral); TAX BREAK GOES TO, YOU (blue). "
        "Text: 'Save in their RRSP. You get the tax break.' Next: 'Leave it 3 years after your last deposit.' A drawn strip of four year "
        "cards: 2026 (coral, +$, LAST DEPOSIT), 2027 and 2028 (padlocks, WAIT), 2029 (green tick, TAKE OUT). Text: 'Take it out "
        "sooner? It's taxed as your income.' Handwritten: 'later, it's taxed as theirs'. On cobalt: 'do this: Ask your bank for a "
        "spousal RRSP.' with the account card and a card: 'It uses your own RRSP room. For married or common-law couples.' End: "
        "'Last deposit? Then wait 3 years.' with the year strip, 'Follow for one money rule a day, in plain words.' and the round "
        "brand stamp."),
    beats=[
        "CANADA · SPOUSAL RRSP | Earn twice what | your partner does? | SPOUSAL RRSP (card) | IN THE NAME OF | YOUR PARTNER | "
        "TAX BREAK GOES TO | YOU (fades in 0.3 s) | Save in their RRSP. | You get the tax break. (1.3 s)",
        "Leave it 3 years | after your last deposit. | 2026 +$ LAST DEPOSIT | 2027 WAIT (lock) | 2028 WAIT (lock) | 2029 (tick) TAKE OUT | "
        "Take it out sooner? | It's taxed as your income. | later, it's taxed as theirs",
        "(cobalt field) do this: | Ask your bank for | a spousal RRSP. | SPOUSAL RRSP card (IN THE NAME OF YOUR PARTNER, TAX BREAK "
        "GOES TO YOU) | It uses your own RRSP room. | For married or common-law couples.",
        "(cobalt field) Last deposit? | Then wait 3 years. | year strip (2026 +$ LAST DEPOSIT | 2027 WAIT | 2028 WAIT | 2029 TAKE "
        "OUT) | Follow for one money rule a day, in plain words. | (round brand stamp)",
        "(loop, hard cut) the frame-0 layout",
        "cover only (follow the line): CANADA · SPOUSAL RRSP | Earn twice what | your partner does? | year strip with a dotted "
        "coral line | wait 3 years after your last deposit | (round brand stamp)",
    ],
    hook_options=["Earn twice what your partner does?", "You earn $90,000? Partner earns $40,000?", "Spousal RRSP? Leave it 3 years."],
    hook_picker=("Stranger picker (gate, Nov 4) chose 'Earn twice what your partner does?' (was option 3): the $90,000 / $40,000 "
                 "version needs two questions and two numbers before you know why. Adopted on frame 0 and the cover; the "
                 "incomes were dropped (90/40 is not twice)."),
    style=("Reel body: illustrated 'rule drawn happening' scene (a drawn SPOUSAL RRSP account card: IN THE NAME OF YOUR PARTNER / "
           "TAX BREAK GOES TO YOU; then a 4-year calendar strip: 2026 deposit, 2027-2028 locked, 2029 ticks open) on pale blue "
           "dot paper, a do-this beat on cobalt with the card, the end beat on cobalt with the year strip; land / hard cuts. "
           "Dedicated COVER: style 9 follow-the-line (quiet) on pale blue dot paper: serif hook + soft-coral pill, year strip "
           "with a dotted coral line, handwritten line, round stamp."),
    send_test=False,
    sources=["CRA 'Withdrawing from spousal or common-law partner RRSPs' (modified 2026-06-26)",
             "CRA 'Contributing to your spouse's or common-law partner's RRSPs' (modified 2026-01-29)"],
    notes=(
        "Mon Nov 9 19:00 (no trial). Different topic family from A (retirement savings vs tax-return credits). Felt moment + "
        "numbers on frame 0 ($90,000 / $40,000, 5 words), 'Canada' on screen, ONE drawn object per beat doing the meaning (card, "
        "then year strip). Not on the 14-day avoid list; the Fri HBP Reel is also RRSP but a different rule (first home). No "
        "send line on screen (send_test false). Music: existing FF track media/music/library/v4/ff-x-money-moves.mp3. The page's "
        "'3 calendar years' = the deposit year + the 2 years after it (CRA: withdrawal year or the two years before). Exceptions "
        "(separation, death, non-residence) not covered on the page checked, so not claimed. QG-1: QA frames + strip + cover "
        "checked; fixed overlapping card labels, a stray lock shackle and an overflowing card line before the final encode. "
        "CD gate fix (Nov 4): hook switched to the picker's choice; year-strip labels enlarged to 40-44 px (>=34 px on "
        "screen); screen and caption now say the 3 years run from the LAST deposit (each deposit restarts the clock)."),
)

C = dict(
    id="ff-richhabits-07", account="fullyfunded", publish_at="2026-11-09T17:00:00-05:00",
    images=["studio-nov04/fullyfunded/ff-richhabits-07/01.jpg", "studio-nov04/fullyfunded/ff-richhabits-07/02.jpg"],
    caption=(
        "Free 30-day trial? Set a day-28 reminder. The habit: the minute you start a free trial, set a phone reminder for 2 days "
        "before it ends.\n\n"
        "Rich Habits, Decoded No. 7. Each episode takes one money habit and shows you how to do it on a normal paycheque.\n\n"
        "WHY IT WORKS: many trials take your card and roll into a monthly charge on their own. Canada's Competition Bureau warns "
        "that some 'free trials' are subscription traps. A reminder turns an automatic charge into a choice you make on purpose.\n\n"
        "HOW:\n"
        "1. Before you sign up, find the end date and how to cancel in the terms.\n"
        "2. In your phone's calendar or reminders app, set an alert 2 days before the end date: 'Still using it?'\n"
        "3. When it goes off: still using it? Keep it. If not, cancel, and save the cancellation email.\n"
        "4. Next month, check your card bill for the charge, to be sure it stopped (or that you meant to keep it).\n\n"
        "THE CATCH: some services end your access the moment you cancel, and some charge the minute the trial ends. Read the "
        "terms first. If you can't cancel, call your credit card provider.\n\n"
        "Do this: Set a day-28 reminder the day you start a 30-day trial.\n\n"
        "Send this to the friend who just signed up for a free trial.\n\n"
        "Education only, not financial advice.\n\n"
        f"{FOLLOW}\n\n"
        "#personalfinance #budgeting #moneyhabits #richhabits #subscriptions\n\n"
        "Rich Habits, Decoded No. 8 lands Wednesday, Nov 11 at 5 pm."),
    first_comment=(
        "Sources (checked Nov 4 2026):\n"
        "• Competition Bureau Canada, 'Subscription traps' (competition-bureau.canada.ca/en/fraud-and-scams/tips-and-advice/"
        "subscription-traps, modified 2022-01-19): fraudsters 'trick you into a monthly subscription'; don't sign up if you can't "
        "find or understand the terms; 'If you go ahead with a free trial, keep all documents, receipts, emails, and text "
        "messages'; 'Regularly check your credit card statements for frequent or unknown charges'; if you have trouble cancelling, "
        "contact your credit card provider.\n"
        "The day-28 reminder is the habit's own rule of thumb, not a study result. The 30-day trial card is made up for this post."),
    alt_text=(
        "Fully Funded 2-slide carousel. Slide 1, on the coral field: 'Rich Habits, Decoded · No. 7' badge, 'Free 30-day trial? "
        "Set a day-28 reminder.' in a large serif with the last lines on a white pill, the handwritten note 'new one every Mon · Wed · "
        "Fri', the round brand stamp, and a drawn sign-up card: START FREE TRIAL, 30 DAYS in big coral letters, FREE, THEN BILLED "
        "MONTHLY, with a coral rubber stamp REMIND ME ON DAY 28 across the button. Slide 2, on cream: 'Still using it? Keep "
        "it. If not, cancel.' (last line on a soft-coral pill) Handwritten: 'check your bill for the charge'. A drawn phone reminder card: DAY 28 · ENDS IN 2 "
        "DAYS, 'Still using it?', with YES · KEEP and NO · CANCEL buttons."),
    beats=[
        "Slide 1: RICH HABITS, DECODED · NO. 7 | Free 30-day trial? | Set a day-28 reminder. | new one every Mon · Wed · Fri | "
        "START FREE TRIAL | 30 DAYS | FREE, THEN BILLED MONTHLY | REMIND ME ON | DAY 28 (stamp over the button) | (round brand stamp)",
        "Slide 2: 2/2 | Still using it? | Keep it. | If not, cancel. | check your bill for the charge | DAY 28 · ENDS IN 2 "
        "DAYS | Still using it? | YES · KEEP | NO · CANCEL | (round brand stamp)",
    ],
    hook_options=["Free 30-day trial? Set a day-28 reminder.", "Gave your card for a free trial?", "Free for 30 days, then monthly?"],
    hook_picker="Stranger picker (gate, Nov 4) agreed with option 1.",
    duration_s=None,
    style=("Series cover (Rich Habits, Decoded: pills + drawn object + series badge + handwritten series line + stamp), same "
           "layout as No. 6 (coral field, drawn card bottom-right; built on nov01_fullyfunded_feed.py). 2 slides."),
    send_test=False,
    sources=["Competition Bureau Canada 'Subscription traps' (modified 2022-01-19)"],
    notes=(
        "Promised in No. 6's caption ('Rich Habits, Decoded No. 7 lands Monday, Nov 9 at 5 pm'); same layout and slot (17:00, "
        "-05:00). Hook 7 words naming the money moment, numbers 30 and 28 on the cover. Not a repeat of No. 1-6 (pay yourself "
        "first, lunch, insurance /12, one month ahead, money date, sleep on it 24 h). Caption's last line promises No. 8 on Wed "
        "Nov 11 at 5 pm, per the brief. QG-1: both slides checked at full size. CD gate fix (Nov 4): the lavender highlight "
        "pill (read as Hourback periwinkle) swapped in-process for white on the coral cover and soft coral #FFB08F on slide 2 "
        "(kit not edited; a colour change from No. 6, same layout); slide 2 line now says what to check for."),
)

PIECES = {"A": A, "B": B, "C": C}


def main(keys):
    out = []
    for k in keys:
        e = dict(PIECES[k])
        if "video" in e:
            e["duration_s"] = dur(e["video"])
            assert e["duration_s"] <= 15.0
        for f in (e.get("video"), e.get("cover"), *(e.get("images") or [])):
            if f:
                assert (REPO / "media" / f).exists(), f
        blob = json.dumps(e).lower()
        for w in ("example", "e.g.", "hypothetical", "for illustration"):
            assert w not in blob, (k, w)
        out.append(e)
    OUTF.parent.mkdir(parents=True, exist_ok=True)
    OUTF.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print("wrote", OUTF, [e["id"] for e in out])


if __name__ == "__main__":
    main(sys.argv[1:] or ["A"])

#!/usr/bin/env python3
"""Writes studio/editorial/nov05/fullyfunded_fix.json: corrected full entry for the queued ff-reel-1108-medical-one-return.
    python3 studio/editorial/nov05_fullyfunded_fix_manifest.py
"""
import json, re, subprocess
from pathlib import Path
REPO = Path("/home/claude/steadfold-autopost")
RID = "ff-reel-1108-medical-one-return"
old = [x for x in json.load(open(REPO / "studio/editorial/nov04/fullyfunded.json")) if x["id"] == RID][0]
e = dict(old)
e["caption"] = """Dentist, glasses, pills: $2,000 this year? Claim them on one return, usually the lower earner's.

In Canada, one of you can claim the medical bills for both partners and your kids under 18, all together, on one tax return (line 33099).

WHY: only the part of the bills above a floor counts. The floor is 3% of the claimer's net income, or a fixed amount if that is less ($2,891 for 2026; $2,834 for 2025). A lower income means a lower floor, so more of the same bills count.

The maths (made up for this post): $2,000 of bills.
• You earn $90,000: 3% is $2,700, more than the bills, so $0 counts.
• Your partner earns $40,000: 3% is $1,200, so $800 counts for the credit.
That $800 is not money back. It's the amount the credit is worked out on: $800 x 14% = $112 off your federal tax for 2026, plus your province's own credit.

HOW:
1. Gather every receipt: dentist, prescription glasses, prescription drugs, and the rest of the CRA's list.
2. Pick any 12-month period that ends in the tax year.
3. In your tax app, enter the bills on the lower earner's return first, then check the other return too, and keep the one that cuts more tax.

THE CATCH: it's a non-refundable credit, so it only lowers tax the claimer owes. If the lower earner owes little or no tax, the other return may work better. Purely cosmetic work and over-the-counter medicine don't count. Keep the receipts.

WHO THIS IS FOR: you, your spouse or common-law partner, and your or their kids under 18. Bills for other relatives who depend on you (an adult child, a parent) go on line 33199, with their own rules.

Do this: Claim them on line 33099, usually on the lower earner's return. Check both in your tax app.

Send this to whoever does the taxes in your home.

Education only, not financial advice.

Follow for one money rule a day, in plain words.

#personalfinancecanada #canadiantaxes #taxtips #medicalexpenses #canadianmoney"""
e["first_comment"] = old["first_comment"].replace("(checked Nov 4 2026)", "(checked Nov 4 2026; updated Nov 5 2026)") + (
    "\n• TaxTips.ca, 'Tax credits 2026' (taxtips.ca/nrcredits/tax-credits-2026.htm, checked Nov 5 2026): federal medical expense "
    "threshold $2,891 for 2026 (line 33099); federal credit rate 14%. (CRA's 2026 RC4065 isn't published yet; the 2025 amount, $2,834, "
    "is from CRA RC4065.)\nThe $112 is our maths: $800 x 14% (federal only, 2026).")
e["alt_text"] = ("Fully Funded Reel. On cream dot paper, a blue pill says CANADA · MEDICAL EXPENSES. Headline: 'Dentist, glasses, pills: "
    "$2,000 this year?' A drawn receipt, FAMILY MEDICAL: DENTIST $900, GLASSES $650, PRESCRIPTIONS $450, TOTAL $2,000. Text: 'Usually "
    "best on the lower earner's return.' Next: 'Only bills above 3% of income count.' Handwritten: 'or above $2,891 (2026), if that's "
    "less'. Two drawn receipts side by side: YOU, EARNS $90,000, BILLS $2,000, 3% OF INCOME −$2,700, and a coral box: $0 COUNTS FOR "
    "CREDIT; PARTNER, EARNS $40,000, BILLS $2,000, 3% OF INCOME −$1,200, and a green box: $800 COUNTS FOR CREDIT. Handwritten: '$800 × "
    "14% = $112 off federal tax'. On cobalt: 'do this: Claim them on line 33099.' A drawn tax-return card, PARTNER'S TAX RETURN, LINE "
    "33099 $800, BILLS $2,000 − 3% OF INCOME $1,200, with a ticked box: THE LOWER EARNER'S RETURN. A card: 'Usually the lower earner's "
    "return. Check both in your tax app.' End: 'One return. The whole family's bills.' with the receipt, 'Follow for one money rule a "
    "day, in plain words.' and the round brand stamp.")
e["beats"] = [
    "CANADA · MEDICAL EXPENSES | Dentist, glasses, pills: | $2,000 this year? | FAMILY MEDICAL (receipt) | DENTIST $900 | GLASSES $650 | "
    "PRESCRIPTIONS $450 | TOTAL $2,000 (all visible at frame 0) | Usually best on | the lower earner's return. (1.3 s)",
    "Only bills above | 3% of income count. | or above $2,891 (2026), if that's less | YOU | EARNS $90,000 | BILLS $2,000 | 3% OF INCOME | "
    "−$2,700 | $0 | COUNTS FOR CREDIT | PARTNER | EARNS $40,000 | BILLS $2,000 | 3% OF INCOME | −$1,200 | $800 | COUNTS FOR CREDIT | "
    "$800 × 14% = $112 off federal tax",
    "(cobalt field) do this: | Claim them on | line 33099. | PARTNER'S TAX RETURN | LINE 33099 $800 | BILLS $2,000 − 3% OF INCOME $1,200 | "
    "THE LOWER EARNER'S RETURN (box ticks 0.45 s) | Usually the lower earner's return. | Check both in your tax app.",
    "(cobalt field) One return. | The whole family's bills. | receipt: FAMILY MEDICAL, DENTIST $900, GLASSES $650, PRESCRIPTIONS $450, "
    "TOTAL $2,000 | Follow for one money rule a day, in plain words. | (round brand stamp)",
    "(loop, hard cut) the frame-0 layout",
    "cover only: CANADA · MEDICAL EXPENSES | Dentist, glasses, pills: | $2,000 this year? | receipt (DENTIST $900, GLASSES $650, "
    "PRESCRIPTIONS $450, TOTAL $2,000) | usually on the lower earner's return | LINE 33099 · YOU, PARTNER, KIDS UNDER 18 | (round brand stamp)",
]
e["sources"] = old["sources"] + ["TaxTips.ca 'Tax credits 2026': medical expense threshold $2,891 (2026), federal rate 14%"]
e["duration_s"] = round(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                                       str(REPO / "media" / e["video"])], text=True)), 2)
e["replaces_existing"] = True
e["notes"] = old["notes"] + (" FIX Nov 5 (stranger gate CONFUSING), re-rendered in place by studio/editorial/nov05_fullyfunded_fix.py: "
    "each number labelled (BILLS $2,000 / 3% OF INCOME / $800 COUNTS FOR CREDIT); line 33099 now shows $800 (CRA: total minus the floor) "
    "with 'BILLS $2,000 − 3% OF INCOME $1,200' under it; the saving shown as labelled maths ($800 × 14% = $112 off federal tax; 14% is the "
    "2026 lowest rate, not the 15% in the gate note); one instruction on screen ('Usually the lower earner's return. Check both in your "
    "tax app.'); the cap on screen ('or above $2,891 (2026), if that's less'; 2026 figure from TaxTips.ca, CRA's 2025 figure $2,834 in "
    "the caption). Cover's handwritten line now 'usually on the lower earner's return'. Timing 3.4/4.6/3.8/2.4/0.4 s. Round 3 nit: the TOTAL $2,000 row is now visible at frame 0 (no fade-in). QG-1: 2 fps strip "
    "of the encode and the cover viewed.")
assert not re.search(r"example|e\.g\.|hypothetical|for illustration", json.dumps(e), re.I)
assert e["duration_s"] <= 15.0
out = REPO / "studio/editorial/nov05/fullyfunded_fix.json"
out.write_text(json.dumps([e], indent=1, ensure_ascii=False) + "\n")
print(out, e["duration_s"])

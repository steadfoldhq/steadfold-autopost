# Etsy listing audit: Thu Oct 22, 2026 (Commerce QA)

**Bottom line:** 16 listings are live: 15 are in `listings/live.json`, and 1 more on LittlefoldHQ has no spec. One is a **BLOCKER**: the AI Product Governance Kit is on sale at CA$68 while QA holds it as a BLOCKER, and its copy promises a behaviour the tested file does not have. Ten findings are **MAJOR**:
- 3 listings claim a "launch sale" that is not running.
- 3 listings do not disclose that AI was used to make them.
- 3 live products are still on QA hold.
- The SteadfoldHQ shop still shows the retired brand and the founder's town.
- 5 approved print specs on QA hold would be published by the workflow's default run.
- The tooling cannot deactivate a listing, and the spec path form makes 3 modes do nothing.

All shops show 0 sales and 0 reviews, so no buyer has been affected yet as far as public pages show.

**Nothing on Etsy was changed by this audit.** Everything below is read-only evidence plus prepared changes. The plan is in CHANGE_PLAN.md, and the evidence and methods are in VERIFICATION_LOG.md.

## Summary table

Prices are CAD (spec = Etsy page metadata on Oct 22). Page = public page read logged out on Oct 22 via WebFetch.

| ID | Shop | Live? | Price | QA gate (Oct 21 log) | Approval | Worst | Main issue | Prepared fix |
|---|---|---|---|---|---|---|---|---|
| SF-AIGOV | SteadfoldHQ | Yes | 68.00 | **HOLD BLOCKER** (v1.0) | APPROVED | **BLOCKER** | Launch Gate says GO 100% with 8 of 9 evals not run; the listing says it shows NOT READY | **Deactivate** (patch 0001 or by hand) |
| DP-CALM-P | SteadfoldHQ | Yes | 22.00 | PASS | APPROVED | MAJOR | "Launch sale: 25% off" but no sale is running | Sync description |
| DP-CALM-T | SteadfoldHQ | Yes | 22.00 | PASS | APPROVED | MAJOR | Same false sale line | Sync description |
| DP-RIV | LittlefoldHQ | Yes | 14.99 | PASS (minor) | APPROVED | MAJOR | "Launch sale: 30% off" but no sale is running | Sync description |
| FF-HMP | SteadfoldHQ | Yes | 12.00 | PASS (minor) | APPROVED | MAJOR | No disclosure that AI was used to make it | Sync description |
| FF-MPB | SteadfoldHQ | Yes | 26.00 | PASS (minor) | APPROVED | MAJOR | No AI-creation disclosure | Sync description |
| FF-MSP | SteadfoldHQ | Yes | 19.00 | PASS (minor) | APPROVED | MAJOR | No AI-creation disclosure | Sync description |
| HB-LIFEADMIN | SteadfoldHQ | Yes | 19.00 | **HOLD MAJOR** (v1.0) | APPROVED | MAJOR | Copy claims PIN/code/login detection; v1.0 misses it and image 04 shows the narrower rule | Sync description; swap file after QA |
| FF-FREEDOM | SteadfoldHQ | Yes | 17.00 | **HOLD MAJOR** (v1.0) | APPROVED | MAJOR | v1.0 file says "before inflation"; Morningstar source misdated | Sync description; swap file after QA |
| LF-FIRSTS-HOL | LittlefoldHQ | Yes | 4.99 | **HOLD MAJOR** (v1.0 code) | APPROVED | MAJOR | Cover star overlaps the Year line in the file | Swap file to v1.2 after QA |
| HB-CREATOR-LITE | SteadfoldHQ | Yes | 19.00 | Lite PASS | APPROVED | MINOR | Points buyers to the Pro edition, which is on QA hold and sold off Etsy | Sync description |
| FF-CF-CA | SteadfoldHQ | Yes | 14.00 | PASS | APPROVED | MINOR | "Launch price until Mon Nov 30, then CA$22" needs a founder price change on Dec 1 | Founder decision |
| HB-SUB | SteadfoldHQ | Yes | 9.99 | PASS (minor) | APPROVED | MINOR | The 1.1 zip still says "VERSION 1.0" inside; image 02 zoom | Factory fix |
| FF-SCOPE | SteadfoldHQ | Yes | 17.00 | 1.0 PASS; 1.1 untested | APPROVED | MINOR | The listed file (v1.1) was never QA-tested | QA re-test |
| LBM1 | LittlefoldHQ | Yes | 9.99 | no hold | APPROVED | none | Clean | none |
| (no spec) Hospital Bag Checklist | LittlefoldHQ | Yes (since Oct 14) | 6.99 | not in any QA record | none in repo | MINOR | Untracked: tooling can't sync or deactivate it | Add spec + live.json entry |
| LBP-SET, LBP1, LBP2, LBP3, LBP4 | LittlefoldHQ | **No** | 12.99 / 5.99 | **HOLD MAJOR** | APPROVED | MAJOR | Would be listed by a default `spec=all, mode=list` run; "300 dpi … A2" claim is false (~254 dpi) | Corrected copies; do not list until QA lifts the hold |
| Shop: SteadfoldHQ profile | — | — | — | — | — | MAJOR | Owner shown as "ToqueLabs" on all 12 pages; About text tells the Toque Labs story; location and About show the founder's town | Founder only (RQ-57, extended) |
| Shop: SteadfoldHQ FAQ | — | — | — | — | — | MINOR | Says "Canadian editions use CRA rules and GST/HST…" on non-tax products, and "Every file also works in Google Sheets" on the PDF-only workbook | Founder only |
| Tooling | — | — | — | — | — | MAJOR | No deactivate mode; path form `listings/X.json` makes sync fail and titles/hero exit 0 doing nothing | Patches 0001 and 0003 (tested) |

Prices: every live listing's CAD price matches its spec, live.json and the ledger's range (CA$4.99–68). Every page's USD display is the CAD price × 0.7455 (AIGOV 68 → 50.70, Calm 22 → 16.40, Riverbank 14.99 → 11.18). That is the same conversion everywhere, so **no listing has a discount applied**, and none shows a strike-through price.

## Etsy rules checked (official pages, Oct 22)

- **Creativity Standards** (etsy.com/legal/creativity, "Last updated on Jun 10, 2025"):
  - Digital downloads of a seller's original designs are "Designed by a seller".
  - "Seller-prompted AI creations" are allowed.
  - "Sellers must disclose within their listing description if an item is created with the use of AI."
  - "AI prompt bundles" are not allowed as designs.
- **Seller Policy** (etsy.com/legal/sellers, "Last updated on Oct 5, 2026"):
  - "If an item is created through the use of artificial intelligence, you must disclose this in your relevant listings."
  - "Sales, discounts, and price comparisons must reflect real, accurate pricing."
  - "Promotions should not mislead buyers about the value or timing of a deal."
  - Sellers must not encourage "an off-platform transaction".
- **Deactivating** (help.etsy.com article 360000336187):
  - A deactivated listing is removed from the shop, and buyers can't buy it.
  - It stays in Shop Manager. "There's no fee for reactivating a listing that hasn't expired."
  - "If your item expires while it's inactive, you'll be asked to renew the item for a $0.20 USD fee."

No separate AI listing field or attribute was found on Etsy's own pages. The rule is a line in the description. A third-party blog (beancount.io) says the AI rules tightened in 2026, but it cites no Etsy page, so it is not relied on here.

## Per-listing detail

### SF-AIGOV · AI Product Governance Kit · listing 4598264717 · BLOCKER
- **Live:** active on the page Oct 22, CA$68 (US$50.70 displayed), 7 photos, 0 reviews. Owner is shown as ToqueLabs.
- **Spec:** APPROVED Oct 18 (batch oct17-new-2). The spec file was switched to `AI-Product-Governance-Kit-v1.1.zip` (515,514 bytes) on Oct 21. v1.0 (`…-v1.0.zip.age`) is still in the repo.
- **QA (Oct 21):** v1.0 is "HOLD: BLOCKER". The recalculated scenarios give:
  - 8 of 9 evals not run: GO 100%.
  - A must-have set to N/A: GO.
  - High risk with a blank residual: GO.
  - "100% of tests pass" shown with 1 test run.

  The v1.1 fix is "not testable: code is not in the project".
- **Which file buyers get is unknown.** Etsy shows listing files only to the seller and the API, and this session has neither. No run log in the repo shows a `sync` of SF-AIGOV.
- **Copy vs file:** the description says the Launch Gate "says NOT READY until every eval has a result". That is false for v1.0 and unproven for v1.1. A governance product that says GO on missing evidence is the core defect, and CA$68 is the shop's top price.
- **Previews:** image 02 shows a correctly filled sample (9 tests run, GO WITH CONDITIONS), so it is not wrong. Its callout box clips text (MINOR).
- **Recommendation:** deactivate now. It is reversible: the listing, photos, files and URL are kept, and reactivation is free before the listing expires. Today's tooling cannot do this (see Tooling). Reactivate only when QA passes the saved v1.1 code and v1.1 is confirmed on the listing.

### DP-CALM-P · 2027 Calm Planner Printable · 4598245397 · MAJOR
- **Live:** CA$22, 10 photos plus a video (the video did not load in the fetch, so it is not verified), 0 reviews.
- **Copy:** the last line reads "Launch sale: 25% off until 30 Nov 2026. Regular price CA$22." But the page shows the full price with no strike-through, and the price ratio matches every non-sale listing. The CALMLAUNCH sale was meant to be started by hand (spec `by_hand`, docs/etsy-setup.md, Oct 21 launch pack Part B), and it is not running. This breaks Etsy's "real, accurate pricing" rule.
- **QA:** PASS (383/383 plus 22,742 date checks). Files: 5 zips, 1.4–10.5 MB each, all under Etsy's 20 MB limit.
- **Fix ready:** the corrected spec drops the sale line and its CAD override, and `by_hand` now says a sale must be started before it is mentioned. If the founder wants the sale, he starts it first. Either way, the false claim goes.

### DP-CALM-T · 2027 Calm Digital Planner · 4598250927 · MAJOR
- Same false "Launch sale: 25%" line, CA$22, no sale running. QA PASS. Files: 2 PDFs (7.8 and 8.3 MB) plus the Extras zip.
- The ledger notes it is not on Gumroad. That is not an Etsy issue.
- **Fix ready:** same as DP-CALM-P.

### DP-RIV · Riverbank Routines (visual schedule) · 4598282022 · LittlefoldHQ · MAJOR
- **Live:** CA$14.99. The copy says "Launch sale: 30% off until 30 Nov 2026", but the page shows US$11.18, which is the full price converted. 10 photos plus a video (did not load in the fetch).
- **QA:** PASS (minor: "Pages 2 to 14"). Files: EN/FR/BI zips of about 9.4 MB each, plus 2 quick-start PDFs.
- **MINOR:** images 02–06 carry a "STEADFOLD" wordmark on a Littlefold listing. The copy credits "original Steadfold artwork", which is consistent with "Littlefold, a Steadfold studio" but is a brand-consistency note only.
- **Price history:** an Oct record proposed US$7.99/12.99. The approved spec and the live price are CA$14.99, so live matches the approval.
- **Fix ready:** the sale line and its USD override are removed. Alt text for images 1–6 was written after viewing the images; 7–10 are flagged "pending review".

### FF-HMP · Holiday Money Plan · 4598252317 · MAJOR
- **Live:** CA$12, 10 photos plus a video.
- **MAJOR:** the copy says only "The file itself doesn't use AI". It never says the product was made with AI. The QA log shows it is built from Claude-written code (`hmp_build.py`), and every sibling listing discloses this. The fix adds the same disclosure line the Canadian Freelancer listing uses.
- **MINOR:**
  - "Launch price until Mon Nov 30, then CA$19" is a dated price promise. It needs a founder price change on Dec 1, or the line must be removed.
  - The copy says "1,937 automated checks" while QA ran 1,942. That is accurate as a "before release" figure.
  - Product minor (QA): the KPI shows "Every gift has a payday ✓" while Dec 15 is $140 over.

### FF-MPB · Money Planner Bundle · 4598247027 · MAJOR
- **Live:** CA$26. live.json has no price field for it, because the lister found it already live (MINOR record gap).
- Same missing AI-creation disclosure as FF-HMP, and the same launch-price promise ("then CA$33").
- QA PASS (minor).

### FF-MSP · Money Steps Planner · 4598254995 · MAJOR
- **Live:** CA$19, 8 photos, no video.
- Same missing AI disclosure, and the same launch-price promise ("then CA$24"). QA PASS (minor: "Step N of 5").

### HB-LIFEADMIN · AI Life Admin OS · 4598280684 · MAJOR
- **Live:** CA$19.
- **QA:** v1.0 is "HOLD: MAJOR". The detector flags only 5+ digits and the word "password". "PIN 4821", "Passcode 1234" and "Login sam / hunter2" all return OK.
- **Copy vs file:** the live copy says it "warns about … passwords (PIN, code or login too)". Listing image 04 itself says "if you type 5 or more digits or the word 'password'". So the copy contradicts the product's own preview, and it overclaims for v1.0.
- **MINOR:** image 04's "safety check" callout zooms on date rows, not on the flagged row (the QA log noted the same zoom box).
- **Files:** the spec points to v1.1 (619,562 bytes), which QA has not tested. v1.0 is still in the repo, and which file is live is unknown.
- **Fix ready:** the copy is narrowed to what v1.0 does, which stays true for v1.1. Swap the file after QA passes v1.1.
- The shop FAQ also shows the CRA/GST answer on this non-tax product (MINOR, founder).

### FF-FREEDOM · Freedom Number Workbook · 4598259371 · MAJOR
- **Live:** CA$17.
- **QA:** v1.0 is "HOLD: MAJOR". build.py:181 says "before inflation", while the listing and image 04 say "after inflation", so the file and the listing disagree.
- **Morningstar line:** the copy says "3.9% is Morningstar's 2026 safe starting withdrawal rate". Morningstar's page "The State of Retirement Income for 2026" (published Dec 2, 2025) says retirees "can withdraw as much as 3.9% in 2026". The corrected line says "for people retiring in 2026 from Morningstar's December 2025 research".
  - The 30-year horizon and the 30–50% equity range were kept from the original copy. They were not visible on the page fetched, so they are not verified.
- **Files:** the spec points to v1.1, which QA has not tested.
- **FAQ:** the shop FAQ says "Every file also works in Google Sheets" on a PDF-only product (MINOR, founder).

### LF-FIRSTS-HOL · Little Firsts: First Holidays · 4598279192 · LittlefoldHQ · MAJOR
- **Live:** CA$4.99, 7 photos.
- **QA:** "HOLD: MAJOR". In the v1.0 code the cover star overlaps the Year line by 74×28 px, and the p10 star sits in the heading box.
- **Preview:** the listing hero (image 1) is a separate graphic and shows no overlap, so it is not a wrong preview.
- **Files:** the spec points to v1.2, which QA has not tested.
- **Fix:** no copy change needed. Swap the file after QA passes.

### HB-CREATOR-LITE · Creator Rate Card & Media Kit · 4598279124 · MINOR
- QA: Lite PASS.
- **MINOR:** the copy ends with "Look for the Pro edition". Pro is "HOLD: MAJOR" (its quote-builder total is wrong) and is sold on Gumroad. The line points buyers to a held product off Etsy. The fix removes it.

### FF-CF-CA · Canadian Freelancer Tax & Budget Tracker · 4598277772 · MINOR
- CA$14, 10 photos plus a video. QA PASS (580/580). The copy carries an AI disclosure and "version 7.3".
- **MINOR:** "Launch price until Mon Nov 30, then CA$22" requires a founder price change on Dec 1.

### HB-SUB · Subscription Audit & Cancel Kit · 4598257567 · MINOR
- CA$9.99. QA PASS (minor): the file shows "VERSION 1.0" inside the 1.1 zip, image 02's zoom covers the chart title, and a test uses `or True`.
- The shop FAQ shows the CRA/GST answer (MINOR).

### FF-SCOPE · Freelancer Scope-Reply Pack · 4598279058 · MINOR
- CA$17 (US$12.68 displayed). The spec ships v1.1; QA tested only 1.0 because "1.1 not saved".
- The CA$17 price was derived by rounding (source_note), not taken from a kit.

### LBM1 · Littlefold Milestone Cards · 4598261879 · clean
- CA$9.99, 6 photos, AI disclosure present. The "300 dpi" claim is consistent with QA ("the other 16 files are a true 300 dpi").

### Hospital Bag Checklist · 4595692022 · LittlefoldHQ · MINOR
- **Live:** since Oct 14, CA$6.99, 7 photos, AI disclosure present ("with help from AI tools"), and a "not medical advice" disclaimer.
- It has no spec, is not in live.json and has no QA record in the repo, so the tooling can neither sync nor deactivate it.

### LBP-SET, LBP1–LBP4 · Littlefold nursery prints · not live · MAJOR (process)
- **Not live:** they are not in live.json and not on the LittlefoldHQ shop page (4 items). The QA log's "LBP prints (LIVE)" is wrong.
- They are **APPROVED** in the "all" batch. The workflow's default inputs are `spec: all`, `mode: list`, so one default click would publish 5 products that QA holds as MAJOR:
  - The A2 files are 4200×5940 px, about 254 dpi, while the copy says "300 dpi".
  - LBP4's title leads with "First Christmas", but the art shows only a tree.
- **Prepared:** corrected copies (A2 dpi caveat, LBP4 title). Recommendation: do not list them until QA lifts the hold.

### Shop level (founder only; agents don't touch profile settings)
- **SteadfoldHQ profile (MAJOR):**
  - All 12 listing pages show the owner as "ToqueLabs".
  - The shop About section still tells the "Toque Labs" founding story.
  - Both the location field and the About text name the founder's home town.
  - RQ-57 asks to change the display name and the location, but it **does not mention the About text**.
  - LittlefoldHQ is already correct: "Littlefold", "Ontario, Canada".
- **SteadfoldHQ FAQ (MINOR):** the CRA/GST answer appears on non-tax products, and "Every file also works in Google Sheets" appears on the PDF-only workbook. The QA log flagged both on Oct 21.

### Tooling (tools/etsy.py, .github/workflows/etsy-list.yml)
- **No deactivate (MAJOR):**
  - The tool only ever sets `state: active`. The modes are list, check, dry-run, hero, titles and sync.
  - Etsy's updateListing can deactivate a listing (developers.etsy.com Listings tutorial: deactivate "with `updateListing`").
  - Patch 0001 adds `deactivate` and `reactivate`. They take explicit IDs only, never "all". Before and after each change they read the state back. They refuse to reactivate a draft, delete nothing, and record `state: inactive` in live.json. The patch includes 3 tests.
- **Spec input form (MAJOR):**
  - The workflow passes `spec` straight through. `sync`, `titles` and `hero` match bare IDs only.
  - With `listings/FF-FREEDOM.json`, sync fails ("not in listings/live.json"), and titles and hero **exit 0 having made no Etsy call**. A run can look green while changing nothing.
  - Use bare IDs today. Patch 0003 makes both forms work.
- **Tests pin the old sale text (MAJOR for applying fixes):**
  - The workflow runs the test suite before any Etsy call.
  - `test_each_spec_matches_its_prompt_rules` asserts that DP-CALM-P ends with the "Launch sale" line, and that DP-RIV contains "Regular price US$10.99.".
  - Dropping the corrected specs into `listings/` without patch 0002 makes the Tests step fail, and nothing syncs.
  - Patch 0002 replaces those assertions with a guard: no spec may claim a sale, and every spec must disclose AI use. On today's specs the guard fails on exactly the 6 affected listings.
- **No tag or alt-text sync:**
  - No mode updates tags. None of the prepared fixes change tags.
  - The tool never sends alt text. The corrected specs carry an `alt_text` field drafted from file names and copy, which the validator accepts and the tooling ignores.
  - Whether Etsy's image upload takes alt text was not verified this session.
- **Listings don't auto-renew:** `should_auto_renew` is false, so the Oct 18 listings reach the end of Etsy's 4-month period around mid-February 2027.

## Records that disagree
- **QA log Oct 21:** says "LBP prints (LIVE)". They are not live (shop page and live.json, Oct 22).
- **Money Ledger rev 40:** 16 Etsy listings = 15 in live.json + Hospital Bag. This matches the shop pages (12 + 4).
- **Recovered RQ-56:** says "4 held products live since Oct 18" (AIGOV, LIFEADMIN, FREEDOM, FIRSTS). Confirmed live on Oct 22.
- **Approval trail (MINOR):** batches cf-etsy, oct17-new and oct17-new-2 record as their approval quote "Our products, everything is live, right? So please give me the prompt right now … Every single thing, nothing should be missed.", where the review queue asked for "list batch …". It is recorded as founder words, but it is an indirect approval. The founder may want to confirm it.

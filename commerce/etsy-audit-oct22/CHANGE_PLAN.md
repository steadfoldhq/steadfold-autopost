# Etsy change plan: from the Oct 22 audit

**One line:** after one commit and two workflow runs, the BLOCKER is off sale and 9 live listings stop making false or missing claims. File swaps, sales, prices and the shop profile wait for QA or the founder.

**Nothing here has been applied.** This session has no GitHub token and makes no Etsy calls. Every step below is something a person or the Launch desk still has to run.

## Before any run: what to know about the inputs
- **`spec` must be bare IDs** for `sync`, `titles`, `hero` and the new `deactivate`/`reactivate`, for example `SF-AIGOV` or `DP-CALM-P,DP-CALM-T`.
  - `listings/X.json` makes `sync` fail. Worse, it makes `titles` and `hero` finish green without touching Etsy (verified, see VERIFICATION_LOG).
  - After patch 0003 both forms work.
- **`sync` defaults to `parts: files,description`.** For copy-only fixes always set `parts: description`. Otherwise the run also swaps in the v1.1/v1.2 files that QA has not tested yet.
- **Never run the defaults (`spec: all`, `mode: list`) while the LBP hold is open.** That would publish LBP-SET and LBP1–4, which are on QA hold.
- The workflow runs the test suite first. A failing test stops the run before any Etsy call, which is why patch 0002 must land with the corrected specs.

## Step 1: Deactivate the AI Governance Kit (BLOCKER) · routine, reversible
**Why:** the kit is live at CA$68 while QA holds it as a BLOCKER, and its copy promises "NOT READY until every eval has a result", which the tested file does not do. It has 0 sales, so no refund is in play.

**Reversible:**
- The listing, photos, files and URL are kept.
- Etsy charges nothing to reactivate before the listing expires (Etsy Help 360000336187).
- Nothing is deleted, and the price is unchanged.
- RQ-56 already offered the founder "pause AIGOV" as an option.

Pick one:
- **A. By hand, now (about 1 min, no code):** Etsy → SteadfoldHQ → Shop Manager → Listings → tick "AI Product Governance Kit…" → Deactivate. Then add `"state": "inactive"` to the SF-AIGOV entry in `listings/live.json`, so agents know.
- **B. Through the pipeline:**
  1. Apply `patches/0001-etsy-deactivate-reactivate.patch` (`git apply` from the repo root, then commit and push).
  2. Actions → **Etsy list** → Run workflow with:

     | input | value |
     |---|---|
     | spec | `SF-AIGOV` |
     | mode | `deactivate` |
     | parts | (ignored) |
     | photos | (ignored) |

     The job reads the state back, writes "active -> inactive" to the Summary, and commits `listings/live.json` with `"state": "inactive"`.

**Check afterwards:** open https://www.etsy.com/listing/4598264717 logged out. It should be unavailable, and the SteadfoldHQ shop page should list 11 items.

**Undo:** mode `reactivate`, spec `SF-AIGOV` (patch 0001), or Shop Manager → Listings → Inactive → Activate.

## Step 2: One commit with the corrected copy · routine
Put these in **one commit**, because the Tests step fails if they are separated:
1. Copy these 9 files from `commerce/etsy-audit-oct22/specs/` over the same names in `listings/`:
   - `DP-CALM-P.json`, `DP-CALM-T.json`, `DP-RIV.json`
   - `FF-HMP.json`, `FF-MPB.json`, `FF-MSP.json`
   - `HB-LIFEADMIN.json`, `FF-FREEDOM.json`, `HB-CREATOR-LITE.json`
2. Optionally copy the LBP-SET and LBP1–4 copies too, so the not-yet-listed prints carry honest dpi wording before anyone lists them.
3. `git apply commerce/etsy-audit-oct22/patches/0002-tests-no-false-sale-ai-disclosed.patch`
4. Optionally `git apply …/0003-accept-listings-path-in-spec-input.patch`. It needs 0001 first.
5. Optional offline check before pushing: `python3 tools/etsy.py validate` should print 20/20 OK, and `python3 -m unittest discover -s tests -q` should pass. Both were run on a copy here: 127 tests with 0001+0002, 128 with 0003.

The other 6 copies (FF-CF-CA, HB-SUB, FF-SCOPE, LF-FIRSTS-HOL, LBM1, SF-AIGOV) differ from `listings/` **only** by the new `alt_text` field. Copying them is harmless, but it changes nothing on Etsy today.

## Step 3: Sync the copy fixes · routine, one run
Actions → **Etsy list** → Run workflow with:

| input | value |
|---|---|
| spec | `DP-CALM-P,DP-CALM-T,DP-RIV,FF-HMP,FF-MPB,FF-MSP,HB-LIFEADMIN,FF-FREEDOM,HB-CREATOR-LITE` |
| mode | `sync` |
| parts | `description` |
| photos | (empty) |

`sync-listing` handles both shops in one run. DP-RIV is LittlefoldHQ, and the rest are SteadfoldHQ. For each listing it PATCHes only the description and reads it back. A mismatch fails that row.

Field by field (exact text is in each spec copy and in `spec_changes.json`):

| Listing | Field | Change | Reason |
|---|---|---|---|
| DP-CALM-P | description | Delete "• Launch sale: 25% off until 30 Nov 2026. Regular price US$16." (shown in CAD as CA$22) | No sale is running; Etsy Seller Policy |
| DP-CALM-P | currency_overrides | Removed; its only target was that line | The validator requires the target text |
| DP-CALM-P | by_hand | A sale is optional and must be started before it is mentioned | Stops a repeat |
| DP-CALM-T | same 3 changes | as DP-CALM-P | as DP-CALM-P |
| DP-RIV | description, currency_overrides, by_hand | Delete "• Launch sale: 30% off until 30 Nov 2026. Regular price CA$14.99." and the USD override | No sale is running |
| FF-HMP, FF-MSP, FF-MPB | description | After the "doesn't use AI" line, add "• Made by Steadfold with AI help: the formulas and pages were built with Claude, then tested with automated checks before release" | Etsy: AI use must be disclosed in the description |
| HB-LIFEADMIN | description | The privacy line becomes "if you type 5 or more digits in a row or the word "password", it asks you to remove them. Keep PINs, codes and logins out of the file" | True for v1.0 and v1.1, and matches image 04 |
| FF-FREEDOM | description | "3.9% is the safe starting withdrawal rate for people retiring in 2026 from Morningstar's December 2025 research, for a 30-year retirement (30% to 50% in stocks)" | Morningstar's page is dated Dec 2, 2025 |
| HB-CREATOR-LITE | description | Delete "• Want a quote builder, deal tracker, invoice and 12 replies? Look for the Pro edition" | Pro is on QA hold and sold off Etsy |

Titles, tags, prices and photos are unchanged for all 9. **Check afterwards:** re-read the 9 public pages. The sale lines should be gone, and the AI line should be present on HMP, MPB and MSP.

## Step 4: File swaps · needs QA pass, then founder OK (RQ-56 "swap now")
Do this only after the factory's code for AIGOV 1.1, LIFEADMIN 1.1, FREEDOM 1.1 and FIRSTS 1.2 is saved and QA passes it. The specs already name those files, and the .age files are in the repo.

| input | value |
|---|---|
| spec | `HB-LIFEADMIN,FF-FREEDOM,LF-FIRSTS-HOL` |
| mode | `sync` |
| parts | `files` |

`sync` uploads first and deletes old listing files only after every upload is visible on Etsy.

**Undo:** point the spec back at the old .age file, which is still in the repo, and sync files again.

**AIGOV:** run the same sync with spec `SF-AIGOV`, parts `files` while it is inactive. Uploading to an inactive listing was not verified this session; if Etsy refuses, upload by hand in Shop Manager. Then run mode `reactivate`, spec `SF-AIGOV`.

## Needs the founder (agents can't or shouldn't)
| # | What | Why it's founder-only | Where |
|---|---|---|---|
| F1 | SteadfoldHQ profile: change the display name "ToqueLabs" to Steadfold, the location to "Ontario, Canada", **and rewrite the About section** (it tells the Toque Labs story and names the home town) | Account and profile settings; privacy | Etsy profile + Shop Manager → Settings → About. RQ-57 covers only the first two |
| F2 | SteadfoldHQ FAQ: limit "Canadian editions use CRA rules…" to the tax products, and fix "Every file also works in Google Sheets" for the PDF-only workbook | Shop-level setting; the API path is not in the tooling | Shop Manager |
| F3 | Run CALMLAUNCH (25%) and RIVERBANKLAUNCH (30%) to Nov 30, **or not** | A price change (sale). Values were approved Oct 18, but they're not running and a sale costs margin | Oct 21 launch pack Part B. If started, add a sale line back afterwards |
| F4 | Dec 1 promises: "Launch price until Mon Nov 30, then CA$22/19/33/24" on CF-CA, HMP, MPB, MSP. Either raise the prices on Dec 1, or remove the lines before then | Price change | Price edit is by hand (the tooling has no price mode); line removal is a description sync |
| F5 | AIGOV relist decision after QA (and RQ-56 "fixed zips uploaded / pause / swap now") | Re-listing a product | Step 4 |
| F6 | Bring the Hospital Bag listing (4595692022, LittlefoldHQ) under a spec and live.json | Needs the customer files encrypted with `tools/etsy.py encrypt` from the originals | Then the tooling can sync or deactivate it |
| F7 | LBP prints: keep them off Etsy until QA lifts the hold, and decide whether "all" should keep including them | Approval scope | Avoid `spec: all, mode: list`. Corrected copies are ready |
| F8 | Confirm the batch approvals for cf-etsy, oct17-new and oct17-new-2 (the recorded quote is indirect) | Approval record | Review queue |
| F9 | Alt text: the tooling doesn't send it. Paste from the spec copies' `alt_text` in Shop Manager, or approve a small future code change | Manual work or new code | Spec copies |

None of these is a deletion, refund or new listing. All 16 live listings show 0 sales, so no refund is indicated.

## Order and timing
1. **Today:** Step 1 (BLOCKER).
2. **Today or tomorrow:** Steps 2 and 3, about 10 minutes plus one run.
3. **This week:** F1 and F2, about 5 minutes. They are also in RQ-57, extended.
4. **By Nov 30:** F3 and F4.
5. **When QA passes:** Step 4.

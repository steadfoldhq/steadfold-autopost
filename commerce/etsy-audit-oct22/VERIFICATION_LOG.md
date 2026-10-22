# Verification log: Etsy audit, Thu Oct 22, 2026

All times are Toronto time, and every check ran between about 13:30 and 14:50.

Every check here was **read-only**. No Etsy API call was made, no workflow was dispatched, no git command was run, and nothing in `listings/` or `tools/` was edited. Customer `.age` files were not decrypted; only their names and sizes were read. No secrets were read.

## Sources read
| What | How | Result |
|---|---|---|
| `listings/live.json` | read the file | 15 listings: 12 SteadfoldHQ + 3 LittlefoldHQ, listed Oct 18 21:12–21:49 UTC. No drafts |
| 20 specs, `listings/*.json` | parsed with Python | All APPROVED. 5 (LBP-SET, LBP1–4) are not in live.json |
| `listings/files/**` | `ls -la` (names and sizes only) | v1.0 and v1.1 zips both present for AIGOV, LIFEADMIN and FREEDOM; v1.1 and v1.2 for FIRSTS |
| `tools/etsy.py`, `.github/workflows/etsy-list.yml`, `tests/test_etsy.py`, `docs/etsy-setup.md`, `docs/review-queue-oct21.md`, `docs/launch/*` | read | Tooling findings are in AUDIT.md |
| Product QA log, Oct 21 (founder doc, artifact SSWrbKnFKWHLHGsKqUUmsp) | Claude Docs `read`, treated as data | Holds, versions, RQ-56 |
| Steadfold Money Ledger, rev 40 (artifact PDewFa3B8c76iELXQE1BLC) | Claude Docs `read` | 16 listings, CA$0 recorded revenue, AIGOV/sale risk |
| Recovered records (scratchpad recovery-products.md #22, recovery-ip.md #40) | read | Same claims as the docs above |
| `/home/claude/steadfold/docs/v05/RECONCILIATION_PLAN.md` (R-01, FD-01) | read | FD-01 asks the founder to pause/fix the held listings, the sale labels and the profile |
| `/home/claude/steadfold/docs/v06/MUSE_RECOVERY.md` | grep for Etsy/AIGOV | Only the brand-kit Etsy banners (A01). Nothing about listings |

## Public Etsy pages (WebFetch, logged out, US proxy)
Etsy **did not block** these reads. All 15 live.json URLs, both shop pages and the Hospital Bag listing loaded.

What was captured: title, displayed price (a USD conversion) and the CAD metadata price, any strike-through or sale marker, the Add-to-cart state, owner name, location, photo and video presence, chosen description phrases, and reviews.

| Check | Result |
|---|---|
| All 15 live.json listings active | Yes. Every page has Add to cart and 0 reviews; the shops show 0 sales |
| Titles match the specs | Yes, all 15 |
| CAD prices match the specs | Yes, all 15. FF-SCOPE's CAD was derived from US$12.68 ÷ 0.7455 = 17.01, since its metadata was not captured |
| Any sale running | **No.** No strike-through on any page. Every USD display is CAD × 0.7455 (68→50.70, 22→16.40, 14.99→11.18, 4.99→3.72) |
| Photo counts match the specs | Yes: Calm P 10, Calm T 10, HMP 10, MPB 10, MSP 8, CF 10, SUB 7, SCOPE 6, CREATOR 6, FIRSTS 7, LIFEADMIN 7, FREEDOM 7, RIV 10, LBM1 6, AIGOV 7 |
| Videos | 6 listings show a video, but each showed "trouble loading this video" to the fetcher. **Not verified:** likely the fetcher, not Etsy |
| SteadfoldHQ shop page | 12 items, owner shown as "ToqueLabs", About text names Toque Labs and the founder's town, no sale banner |
| LittlefoldHQ shop page | 4 items (Milestone Cards, Riverbank, Little Firsts, Hospital Bag), "Littlefold", "Ontario, Canada", no sale banner |
| Hospital Bag listing | Live since Oct 14, CA$6.99, 7 photos, AI disclosed |
| LBP prints live? | **No.** Not on the shop page, not in live.json |

**Not verified:**
- Which customer file each listing actually serves. Only the seller or the API can see listing files, so the v1.0 vs v1.1/v1.2 question stays open.
- Listing tags on Etsy. Tags are not shown on public pages, so the tags in AUDIT.md are the spec's.
- Etsy's shop FAQ text beyond the quotes the fetcher returned.
- Whether Etsy's image upload accepts alt text.
- Whether files can be uploaded to an inactive listing.

The fetcher returns summaries; the quotes are as it returned them.

## Etsy policy pages
| Page | Fetched | Key text (as returned) |
|---|---|---|
| etsy.com/legal/creativity | Oct 22 | "Last updated on Jun 10, 2025"; "Sellers must disclose within their listing description if an item is created with the use of AI." |
| etsy.com/legal/sellers | Oct 22 | "Last updated on Oct 5, 2026"; "If an item is created through the use of artificial intelligence, you must disclose this in your relevant listings."; "Sales, discounts, and price comparisons must reflect real, accurate pricing." |
| help.etsy.com/hc/en-us/articles/360000336187 | Oct 22 | Deactivating removes the listing from sale; "There's no fee for reactivating a listing that hasn't expired." |
| developers.etsy.com/documentation/tutorials/listings | Oct 22 | Deactivated = "deliberately deactivated, unsearchable, and unsellable", done with `updateListing` |
| developers.etsy.com reference (updateListing) | Oct 22 | **Not readable:** the page loads by script. The exact `state` enum was not verified. The patch uses `"inactive"`, the listing state the tool's own code already queries in `find_by_title` |
| morningstar.com/business/insights/research/the-state-of-retirement-income | Oct 22 | "retirees can withdraw as much as 3.9% in 2026", published Dec 2, 2025. The 30-year horizon and equity range were not visible on the page |
| beancount.io (third party) | Oct 22 | Cites no Etsy page, so it was not relied on |

## Listing images viewed
I opened and looked at these images:
- AIGOV-02
- FREEDOM-04
- FIRSTS-01 (square hero)
- LIFEADMIN-04
- Riverbank 02–06

Results:
- LIFEADMIN-04 states the 5-digit/"password" rule, which contradicts the copy, and its callout zooms on the wrong rows.
- AIGOV-02's callout text is clipped.
- The other images are consistent with their copy.
- The other ~100 images were **not viewed**. Their alt text is drafted from file names and marked as such.

## Tests run (on copies in the scratchpad, never in the repo)
I built a sandbox in the scratchpad (`…/scratchpad/etsyqa/`). It symlinks the large repo folders and holds its own copies of `tools/`, `tests/`, `.github/` and the specs. Every run used `PYTHONDONTWRITEBYTECODE=1` and the same command the workflow uses: `python -m unittest discover -s tests`.

| Stage | Contents | Result |
|---|---|---|
| base | repo as is | **115 tests OK** (2 skipped) |
| s1 | + patch 0001 (deactivate/reactivate) | **126 OK.** The 3 new tests pass. The other 8 are the inherited ListingFlow tests, the same pattern as SyncListing |
| s2 | + corrected specs + patch 0002 | **127 OK**; `etsy.py validate` 20/20 OK; dry-run of `all` still lists BY HAND notes |
| neg | s2's tests on the **current** specs | The new guard fails on exactly DP-CALM-P, DP-CALM-T, DP-RIV, FF-HMP, FF-MPB and FF-MSP, plus the updated pin. This shows the guard catches the defects |
| s3 | + patch 0003 | **128 OK** |
| apply | fresh copy of the real `tools/`, `tests/` and `.github/`, then `patch -p1` 0001 → specs → 0002 → 0003 | Each patch applied cleanly; OK after each step; workflow YAML parses with modes `[list, check, dry-run, hero, titles, sync, deactivate, reactivate]` |
| current-code probe | s1 tools, FakeEtsy | `sync-listing --spec listings/FF-FREEDOM.json` gives rc 1 "not in listings/live.json"; `sync-titles` and `replace-hero` with the same path give **rc 0, 0 Etsy calls, no output** |

The patches are not applied in the repo.

## Privacy
- The founder's town appears only as "[founder's town]" in these files. `grep -ri` for the town name over this folder returns nothing.
- No emails, addresses or payment details are written here.

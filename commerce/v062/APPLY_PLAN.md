# Apply plan: corrected listing images (v0.6.2)

> **Update (same day, at the coordinator's request):** §D is now implemented, and the gated ops `hero` action has been added too.
> - `tools/etsy.py`: `overwrite_photos`, `_ops_photo_gate` and `cmd_replace_photos`.
> - `tests/test_etsy.py`: 7 new tests.
> - The 5 "now" images are staged under their `-v062` names, and their spec `photos` entries point at them.
> - Ready-to-append ops are in `commerce/v062/ops-queue-proposed.json`.
>
> §C's manual runs are now optional; the ops queue can do the same job with read-back.

**Nothing here has been applied.** This session made no git commits, no workflow runs and no Etsy calls, and edited nothing in `listings/`, `tools/` or `.github/`. Every step below is for a person (or the Launch desk) to run.

## A. Can the existing integration replace a non-hero image?
**Yes, through the manual workflow only, and with no check that it worked.**
- `tools/etsy.py sync-listing --parts photos --photos <ranks>` (the **Etsy list** workflow, mode `sync`) POSTs `spec.photos[rank-1]` to `/shops/{shop}/listings/{id}/images` with `rank=<r>` and `overwrite=true`. That is the same call `replace-hero` makes for rank 1.

Precise limits:
1. **The ops route refuses it.** `cmd_ops` allows only `OPS_SYNC_PARTS = {"description"}`, so a `listings/ops/queue.json` entry with `parts: photos` is REFUSED. Photos need a person to click **Actions → Etsy list → Run workflow**.
2. **No read-back.** For photos, `cmd_sync_listing` records "photos 2" without reading the images back. The description and hero paths do read back. A run can be green without the image having changed.
3. **One rank list per run.** `--photos` applies the same ranks to every spec in `--spec`, so listings whose image sits at a different rank need separate runs.
4. **Dangerous default.** `parts` defaults to `files,description`. Always set `parts` to exactly `photos`. Otherwise the run also uploads the v1.1 customer files that QA has not tested (HB-LIFEADMIN).
5. **Alt text is never sent.** `alt_text` in the specs is ignored by the tool (audit F9).
6. `overwrite=true` at ranks above 1 has not been observed on this shop. The hero path uses it, but its result for other ranks has not been verified.

## B. Images to apply
Stage each corrected file next to the original under a new name, so the original stays for rollback. Then change one entry in that spec's `photos` array. Both files are under 20 MB, which `validate` accepts.

| Listing | Rank | Spec field to change (`listings/<ID>.json`) | New file (copy from `commerce/v062/images/…`) | sha256 (first 16) | Defect | When |
|---|---|---|---|---|---|---|
| HB-SUB | 2 | `photos[1]` | `listings/media/subscription-audit/HB-SUB-02-one-yearly-bill-v062.jpg` | 2764787aa5749452 | Callout covered the chart title and 2 values (audit MINOR) | now |
| HB-LIFEADMIN | 4 | `photos[3]` | `listings/media/life-admin/HB-LIFEADMIN-04-where-its-kept-v062.jpg` | 2a3f3208d62d1ba4 | Subtitle overclaimed; zoom on the wrong rows (audit MAJOR/MINOR) | now. Matches the synced copy, true for v1.0 and v1.1 |
| HB-LIFEADMIN | 5 | `photos[4]` | `listings/media/life-admin/HB-LIFEADMIN-05-warranties-v062.jpg` | add2c4037664cace | Nine dates showed ### (found by v0.6.2, not by the audit) | **only with the file swap**: the image shows dates the v1.0 file renders as ###. Apply after QA confirms v1.1 shows them |
| DP-CALM-P | 5 | `photos[4]` | `listings/media/calm-planner-2027/print/05-calm-check-v062.jpg` | e8d03a407fadfa20 | Banned word "example" (brand rule 12b) | now (MINOR) |
| DP-CALM-T | 5 | `photos[4]` | `listings/media/calm-planner-2027/tablet/05-calm-check-v062.jpg` | 98c94657cd53c253 | same | now (MINOR) |
| FF-MPB | 1 (hero) | `photos[0]` | `listings/media/money-planner/bundle-01-ONEGLANCE-v062-SQ.jpg` | 4e82cad29e5ae394 | "paycheck" instead of the line's "paycheque" | now (MINOR) |
| SF-AIGOV | 2 | `photos[1]` | `listings/media/ai-governance/SF-AIGOV-02-launch-gate-v062.jpg` | e58275c3fd849f99 | Clipped callout (audit MINOR) | with the v1.2 file swap, before reactivation (aigov/REACTIVATION.md) |

Before/after sheets: `commerce/v062/images/before-after/*.jpg`. All 7 were viewed at full size.

The FF-MPB name keeps `-SQ` last, because `_which_hero` derives the old file's name by stripping `-SQ.jpg`.

## C. Runs (Actions → Etsy list → Run workflow)
**One commit first:** the 6 staged files plus the 5 spec `photos` edits for the "now" rows. CI runs `validate` and the tests before any Etsy call. To check offline first: `python3 tools/etsy.py validate` and `python -m unittest discover -s tests -q`.

| Run | spec | mode | parts | photos |
|---|---|---|---|---|
| 1 | `HB-SUB` | sync | `photos` | `2` |
| 2 | `HB-LIFEADMIN` | sync | `photos` | `4` |
| 3 | `DP-CALM-P,DP-CALM-T` | sync | `photos` | `5` |
| 4 | `FF-MPB` | hero | (ignored) | (ignored) |
| later | `HB-LIFEADMIN` | sync | `files,photos` | `5`, after QA passes v1.1 (audit Step 4) |
| later | `SF-AIGOV` | sync | `files,photos` | `2`, while inactive, after QA passes v1.2; then reactivate (REACTIVATION.md) |

Use bare IDs, never `all` and never `listings/X.json`.

**Check after each run:** open the public listing logged out and confirm the image at that rank is the new one. Etsy's cache took about 45 min on Oct 22. The photo count must not change.

**Undo:** point the `photos` entry back at the original file, which is still in place, and repeat the same run.

## D. Proposal: the smallest safe extension to the ops route (not applied; `tools/` is untouched)
**Goal:** let a queued op swap one non-hero photo with the same safety the description path has. Customer files stay forbidden.

1. `OPS_SYNC_PARTS = {"description", "photos"}`.
2. In `cmd_ops`, for `parts` containing `photos`, require:
   - `op["photos"]`: explicit ranks, each an int from 2 to `len(spec["photos"])`. Rank 1 stays with `hero`.
   - `op["sha256"]`: a map of rank to the sha256 of `spec.photos[rank-1]`.

   Refuse the op if any rank is missing or out of range, or if a hash differs from the file in the commit. This proves the agent queued exactly the reviewed image.
3. In `cmd_sync_listing`, `photos` branch: read `c.images(lid)` before and after.
   - Fail the row if the image count changed, or if the image at the rank still has the old `listing_image_id`.
   - Report "photo r: <old id> -> <new id>".
4. **Tests (FakeEtsy):**
   - an op with `parts: photos` and a matching hash replaces rank r and passes;
   - a hash mismatch is REFUSED;
   - rank 1 is REFUSED;
   - `parts: files,photos` is still REFUSED;
   - a failed overwrite (same id) fails the row.

This is about 25 lines in `tools/etsy.py` plus 5 tests. No workflow change is needed, because `etsy-ops.yml` already triggers on `listings/ops/queue.json`.

**Example op once the extension lands:**
`{"id": "2026-10-23-photo-hb-sub-02", "action": "sync", "spec": "HB-SUB", "parts": "photos", "photos": [2], "sha256": {"2": "<full sha256>"}, "reason": "Audit MINOR: callout covered chart title"}`

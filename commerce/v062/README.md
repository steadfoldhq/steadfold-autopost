# commerce/v062 — Etsy listing-image fixes (Oct 22–23, 2026)

- `images/` holds the corrected listing images. `images/before-after/` has a sheet for each image; every one was viewed at full size.
- `APPLY_PLAN.md` explains how each fix is applied through the existing Etsy integration, and how to undo it.
- `ops-queue-proposed.json` lists the gated photo/hero ops, each pinned to a sha256 hash. They become live entries in `listings/ops/queue.json` only after the code is on main.
- The product builds (Registered Room Tracker draft, AI Governance Kit Launch Gate reference) are customer files. They are kept out of this public repo, in the private Steadfold build workspace.

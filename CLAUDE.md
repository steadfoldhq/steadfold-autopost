# Agent instructions: steadfold-autopost (the live publishing system)

Every agent working here reads this file first. That includes the scheduled studio, performance, launch and chief-of-staff desks, Claude sessions, and ChatGPT reviews.

## Before any substantive change
1. **Read `docs/north-star.md`, the Steadfold North Star & Decision Register.**
   - Lines marked **Founder** are the founder's own decisions and stay in force until he changes them.
   - Lines marked _AI_ are interpretations and can be revised with evidence.
   - A change that contradicts a Founder line is an identity change and needs his approval.
2. **Read `docs/brand-system-v4.md`**, including the addendum at the top. It is the approved design system.
3. **Read `docs/optimization-register.md`.** Use real numbers only, and pre-register experiments before changing anything.

## Founder doctrine (Oct 22 2026): "Think five steps ahead. Execute at a 10/10 standard. Improve continuously."
- Understand the real objective, look for a better idea, anticipate consequences, execute and challenge your own output, and make it reusable.
- **Review the actual rendered images and videos** before queuing them. A prompt or a description is not enough.
- Minimalism is not blandness, colourfulness is not clutter, and animation must carry meaning.
- Don't scale an unproven direction into a big batch because automation makes it easy.
- Protect the founder's attention:
  - Make ordinary reversible improvements yourself and log them.
  - Escalate spending, material brand changes, legal or licensing doubt, and irreversible actions.

## Hard rules in this repo
- **Before pushing a queue change:** run `python3 -m unittest discover -s tests -q`, `python3 tools/queue_lint.py` and `python3 autopost.py --dry-run`. Run `git pull --rebase` first, because bots commit every 15 minutes.
- **Rollback records:** every change to `schedule/posts.json` gets one in `docs/social-recovery/`. Hold posts by moving them to `schedule/held-*.json`. Never delete them.
- **Audio:** never use Instagram library music or trending songs in auto-posts. ElevenLabs licensing is pending a founder decision (see the register), so generate no new tracks.
- **Etsy:**
  - Only the guarded ops route, `listings/ops/queue.json`: deactivate, reactivate, description sync, and photo or hero swaps pinned by sha256.
  - Never change prices, customer files or deletions, and never publish new listings without founder approval.
  - Customer product files never go into this public repo unencrypted.
- **Secrets:** never print or commit them.

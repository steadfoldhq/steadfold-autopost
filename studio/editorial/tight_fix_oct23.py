#!/usr/bin/env python3
"""Oct 23 (Social studio): clarity-gate rewrites of two queued Reels (fresh stranger read said CONFUSING).
  lf-reel-1024-grandma-resp: "Own bath time. Same song, every night." never said why -> the idea in plain words.
  ff-reel-1024-beneficiary:  "$100,000, Ontario:" / "LEFT THROUGH THE ESTATE" didn't say what the numbers are. The Oct 22
                             recovery build's source isn't in the repo, so this is a tight 3-beat rebuild with labelled numbers
                             (same facts: Ontario estate administration tax, $15 per $1,000 above $50,000 -> $750 on $100,000).
Same ids, new files (<id>-s15c.mp4); the old media stays in place for rollback.

    python3 studio/editorial/tight_fix_oct23.py [ids...] [--plan]
"""
import argparse
import subprocess
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import tight_oct22  # noqa: E402,F401  (stranger-picked hooks)
import tight as TT  # noqa: E402
import teach_reels as T  # noqa: E402

TT.TIGHT["lf-reel-1024-grandma-resp"] = ("New dad, / *feeling left out?*", 2,
                                         dict(text="You don't need / to feed baby / *to bond.* / *Bath time counts.*"),
                                         dict(text="Tonight: you give / *the bath.*"))
TT.TIGHT["ff-reel-1024-beneficiary"] = ("Your TFSA, / *after you die?*", 3,
                                        dict(items=["$100K TFSA, Ontario:", "Nobody named: *$750 probate*", "Named: *$0*"]),
                                        dict(text="Ask your bank / *who's named.*"))
TT.HOOK_EMO["ff-reel-1024-beneficiary"] = "⏳"
SAVE = {"ff-reel-1024-beneficiary": "send this to your partner", "lf-reel-1024-grandma-resp": "send this to a new dad"}
TT.HOOK_EMO["lf-reel-1024-grandma-resp"] = "🧺"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--out", default="/tmp/claude-0/tight-fix")
    a = ap.parse_args()
    for rid in a.ids or ["lf-reel-1024-grandma-resp", "ff-reel-1024-beneficiary"]:
        spec = TT.tight_spec(rid)
        spec["id"] = rid + "-s15c"
        spec["scenes"][0]["save"] = SAVE.get(rid, spec["scenes"][0].get("save"))
        for sc in spec["scenes"]:
            if sc.get("kicker") is None:
                sc.pop("kicker", None)
        T.lint(spec)
        if a.plan:
            T.report(spec)
        else:
            TT.check_len(spec, T.build(spec, a.out))
            subprocess.run(["rm", "-rf", a.out])

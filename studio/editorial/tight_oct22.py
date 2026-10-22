#!/usr/bin/env python3
"""Oct 22 (Social studio v4): renders the remaining <=15 s tight cuts of queued Reels, with the hooks a fresh
stranger-test subagent picked (3 options each), plus a tight cut of lf-reel-1025-step-away and <=15 s versions of
the three Hourback cheat-sheet Reels (rows pop faster, shorter hold, moment-hook title).

    python3 studio/editorial/tight_oct22.py [ids...] [--plan]
"""
import argparse, copy, subprocess, sys, tempfile
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import tight as TT  # noqa: E402
import teach_reels as T  # noqa: E402

HOOKS = {
    "lh-reel-1022-walk": "Can't crack it / *at your desk?*",
    "lf-reel-1023am-screens-bed": "Bedtime turned into / *a battle again?*",
    "hb-reel-1023am-photo-search": "Weird light / *on your dashboard?*",
    "ff-reel-1023-cpp-60-or-70": "Your parents taking / *CPP early?*",
    "hb-reel-1023-duplicates": "Skimming just / *the AI summary?*",
    "lh-reel-1023-caffeine": None,
    "ff-reel-1024am-sick-pay-gap": "Too sick to work / *for months?*",
    "lh-reel-1024am-floss-after": "New habit keeps / *not sticking?*",
    "ff-reel-1024-beneficiary": "Never named a / *TFSA beneficiary?*",
    "hb-reel-1024-fridge-dinner": "Your next coworker / *might be AI.*",
    "lf-reel-1024-grandma-resp": "New dad, / *feeling left out?*",
    "lh-reel-1024-lyrics": None,
    "lf-reel-1025am-crying-peak": "Worried you're / *spoiling your baby?*",
    "lh-reel-1025am-planning-fallacy": None,
    "hb-reel-1025am-talk-dont-type": "That sparkle button? / *It's AI.*",
    "ff-reel-1025-tfsa-withdrawal-trap": "Putting TFSA money / *back? Wait.*",
    "lh-reel-1025-unpack": "“It'll take an hour.” / *It won't.*",
    "lf-reel-1025-step-away": None,
}
TT.TIGHT["lf-reel-1025-step-away"] = (None, 1, dict(text="Baby safe in the crib. / *Step out 10 minutes.*", kicker=None),
                                      dict(text="Tonight: pick your *step-away person.*"))
for rid, h in HOOKS.items():
    old = TT.TIGHT[rid]
    if h:
        TT.TIGHT[rid] = (h,) + tuple(old[1:])

CHEAT_HOOKS = {
    "hb-cheat-1022-travel-admin": "Will AI take / *your job?*",
    "hb-cheat-1024am-shortcuts": "Nodding along in / *AI meetings?*",
    "hb-cheat-1025-voice-words": "That AI button / *in your apps?*",
}


def build_cheat(pid):
    import cheatsheet as CS
    import v5_hb_cheats as H
    spec = copy.deepcopy(H.CHEATS[pid])
    spec["title"] = CHEAT_HOOKS[pid]
    if pid == "hb-cheat-1022-travel-admin":  # keep only the WEF rows we can source in the caption
        spec["rows"] = [r for r in spec["rows"] if not r[0].startswith("Canadian firms")]
        spec["src"] = "World Economic Forum, Future of Jobs Report 2025 (Jan 2025)."
    n = len(spec.get("rows") or spec.get("cards"))
    # 1.2 s hook + rows at 0.7 s + 6.0 s hold -> 11.4 s for 6 rows
    orig = CS.build
    src = Path(CS.__file__).read_text()
    src = src.replace('durs = [1.6] + [spec.get("beat", 0.6)] * n + [7.0]', 'durs = [1.2] + [0.7] * n + [6.0]')
    ns = {"__file__": CS.__file__, "__name__": "cheat15"}
    exec(compile(src, CS.__file__, "exec"), ns)
    out = ns["build"](pid + "-s15", spec)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)],
                               capture_output=True, text=True).stdout)
    want = 1.2 + 0.7 * n + 6.0
    if dur > 15.0 or abs(dur - want) > 0.3:
        out.unlink()
        raise SystemExit(f"{pid}: encoded {dur:.2f}s, planned {want:.2f}s -> removed")
    print(pid, "ok", round(dur, 2))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--out", default="/tmp/tight-reels")
    a = ap.parse_args()
    for rid in a.ids or (list(HOOKS) + list(CHEAT_HOOKS)):
        try:
            if rid in CHEAT_HOOKS:
                if not a.plan:
                    build_cheat(rid)
                continue
            spec = TT.tight_spec(rid)
            for sc in spec["scenes"]:
                if sc.get("kicker") is None:
                    sc.pop("kicker", None)
            T.lint(spec)
            if a.plan:
                T.report(spec)
            else:
                TT.check_len(spec, T.build(spec, a.out))
                subprocess.run(["rm", "-rf", a.out])
        except SystemExit as e:
            print(f"!! {rid}: {e}", flush=True)

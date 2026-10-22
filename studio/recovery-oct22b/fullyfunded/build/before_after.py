#!/usr/bin/env python3
"""Before/after sheet for ff-reel-1024-beneficiary (Oct 22b). Builder of the new Reel:
/home/claude/steadfold/creative/v061/fullyfunded/_build/reels61.py beneficiary --full"""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("ba", "/home/claude/steadfold-autopost/studio/recovery-oct22/fullyfunded/build/before_after.py")
ba = importlib.util.module_from_spec(spec); spec.loader.exec_module(ba)
ba.OUT = Path("/home/claude/steadfold-autopost/studio/recovery-oct22b/fullyfunded/before-after")
M = Path("/home/claude/steadfold-autopost/media")
ba.reel(M / "reels/ff-reel-1024-beneficiary-s15.mp4", M / "reels/ff-reel-1024-beneficiary-s15-cover.jpg",
        M / "recovery-oct22b/fullyfunded/ff-reel-1024-beneficiary-s15b.mp4", M / "recovery-oct22b/fullyfunded/ff-reel-1024-beneficiary-s15b-cover.jpg",
        "ff-reel-1024-beneficiary", "pointing-hand template (retired clip-art), $750 shown as text only",
        "drawn account form with the blank BENEFICIARY line; $100,000 bar to scale, $750 sliver vs $0")

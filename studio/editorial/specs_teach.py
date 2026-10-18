"""§13 content for Oct 18-21 (rebuilt Oct 17 pm): every feed post, Reel and Story chain on all four pages.

Every post: an outcome hook where it fits, a WHY, ONE "Do this:" (what, where, how much, when), captions in the order
outcome -> "Why it works:" -> "Do this:" -> the catch, sources in the first comment.
FF figures come from studio/pivot/ff_math.py (8-10% a year, 10% max; ages 28/30/33 -> 60). No "example" anywhere.
Fact sources (checked Oct 17 pm) are listed per post in `src` (first comment).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pivot"))
from ff_math import FIG  # noqa: E402

FF, HB, LH, LF = "fullyfunded", "hourback", "lockedhour", "littlefold"
NG = "Not guaranteed. Returns vary."
NOT_MED = "General information only, not medical advice."
MADE = "Made up for this post. Check anything important yourself."
PRIV = "Tip: take names, numbers and addresses out before you paste."
K = FIG

# ======================================================================================================== FEED POSTS
POSTS = {}
META = {}  # id -> dict(at, fmt, caption, comment)


def post(pid, brand, at, fmt, cover, slides, caption, comment):
    POSTS[pid] = dict(brand=brand, cover=cover, slides=slides, fmt=fmt)
    META[pid] = dict(at=at, fmt=fmt, caption=caption, comment=comment, kind="feed")


# ======================================================================================================== REELS
REELS = {}


def reel(rid, brand, at, fmt, track, save, scenes, caption, comment, series=None):
    REELS[rid] = dict(brand=brand, track=track, save=save, scenes=scenes, fmt=fmt)
    META[rid] = dict(at=at, fmt=fmt, caption=caption, comment=comment, kind="reel", series=series)


# ======================================================================================================== STORY CHAINS
CHAINS = {}
CHAIN_TIMES = {  # story frames go out back-to-back (one minute apart, so viewers tap straight through); the handoff follows the feed post
    FF: ["11:00", "11:01", "11:02", "11:03", "12:15"],
    LH: ["11:45", "11:46", "11:47", "11:48", "12:45"],
    HB: ["12:00", "12:01", "12:02", "12:03", "13:15"],
    LF: ["10:30", "10:31", "10:32", "10:33", "11:45"],
}


def chain(cid, brand, day, photo, series, frames, times=None):
    CHAINS[cid] = dict(brand=brand, day=day, photo=photo, series=series, frames=frames,
                       times=times or CHAIN_TIMES[brand][:len(frames) - 1] + [CHAIN_TIMES[brand][-1]])


# Feed posts keep their slots; Story chains hand off to the noon post. Ids that leave the queue (cadence: weak format/slot):
DROPPED = {
    "ff-w03-3-guardian-will": "replaced by the rate-call Learning post (the 'Ask your lender' chain needed a target); moved to backlog",
    "ff-1018-single-24-hours": "FF singles 5 reach vs carousels 9 (cadence: 1 feed post)",
    "ff-1019-single-average-saver": "FF singles weak (cadence: 1 feed post)",
    "ff-1020-single-money-date": "FF singles weak (cadence: 1 feed post)",
    "lh-1018-single-finger-down": "LH singles 5 vs carousels 7 (cadence: 1 feed post)",
    "lh-1019-single-kitchen-table": "LH singles weak (cadence: 1 feed post)",
    "lh-1020-single-midterm": "LH singles weak (cadence: 1 feed post)",
    "ff-reel-1018-the-door": "from-birth horizon breaks §13.7; replaced by ff-reel-1018-start-28",
}

# Page content lives in v5_<page>.py (ONE-READ rewrite, Oct 17 night).
import v5_ff, v5_lh, v5_hb, v5_lf, v5_formats  # noqa: E402,F401

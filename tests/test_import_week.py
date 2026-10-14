"""Tests for tools/import_week.py: prompt-file parsing and the re-dating rules."""

from __future__ import annotations

import sys
import unittest
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import import_week as iw  # noqa: E402

SAMPLE = """\
STEADFOLD PROMPT · header text that should be ignored
CAPTION (paste exactly, between the lines):
<<<
not a post: this is in the instructions
>>>

---------- LOCKED HOUR POST 1 of 2 ----------
WHEN: Wed Oct 14, 2026 at 12:30 pm Toronto
INSTAGRAM ACCOUNT: @lockedhourhq
FOLDER: Downloads/steadfold-lockedhour/2026-10-14_1230_lockedhour_lh-a/   (8 slides: 01.png to 08.png)
CAPTION (paste exactly, between the lines):
<<<
Line one.

Line three with "quotes" and #hashtags
>>>
ALT TEXT:
<<<
Alt words.
>>>
FIRST COMMENT (BY HAND: owner posts it after it goes live):
<<<
Comment A
>>>

---------- LOCKED HOUR POST 2 of 2 ----------
WHEN: Wed Oct 14, 2026 at 7:30 pm Toronto (folder name still says 2026-10-13; that's fine)
INSTAGRAM ACCOUNT: @lockedhourhq
FOLDER: Downloads/steadfold-lockedhour/2026-10-13_1930_lockedhour_lh-b/   (9 slides)
CAPTION (paste exactly, between the lines):
<<<
Caption B
>>>
FIRST COMMENT (BY HAND: after it goes live):
<<<
Comment B
>>>

=========================== END ===========================
"""


def P(pid, acct, y, m, d, hh=12, mm=0):
    return iw.Post(id=pid, account=acct, folder=pid,
                   original=datetime(y, m, d, hh, mm, tzinfo=iw.TORONTO),
                   caption="c", first_comment="f")


class Parse(unittest.TestCase):
    def test_parse_blocks(self):
        posts = iw.parse_prompt_file(SAMPLE, "lockedhour")
        self.assertEqual([p.id for p in posts], ["lh-a", "lh-b"])
        a, b = posts
        self.assertEqual(a.caption, 'Line one.\n\nLine three with "quotes" and #hashtags')
        self.assertEqual(a.alt_text, "Alt words.")
        self.assertEqual(a.first_comment, "Comment A")
        self.assertEqual(a.original, datetime(2026, 10, 14, 12, 30, tzinfo=iw.TORONTO))
        self.assertEqual(b.original.hour, 19)          # 7:30 pm, from WHEN not the folder
        self.assertEqual(b.folder, "2026-10-13_1930_lockedhour_lh-b")
        self.assertEqual(b.alt_text, "")

    def test_wrong_account_rejected(self):
        with self.assertRaises(ValueError):
            iw.parse_prompt_file(SAMPLE, "hourback")

    def test_real_prompt_files_if_present(self):
        for acct, fname in iw.PROMPT_FILES.items():
            path = iw.DEFAULT_PROMPTS / fname
            if not path.exists():
                self.skipTest("prompt files not on this machine")
            posts = iw.parse_prompt_file(path.read_text(encoding="utf-8"), acct)
            self.assertGreaterEqual(len(posts), 5)
            for p in posts:
                self.assertTrue(p.caption and p.first_comment and p.alt_text, p.id)
                self.assertNotIn("<<<", p.caption + p.first_comment)
                self.assertNotIn(">>>", p.caption + p.first_comment)


class Schedule(unittest.TestCase):
    def test_shift_and_one_per_day(self):
        posts = [P("a1", "fullyfunded", 2026, 10, 14), P("a2", "fullyfunded", 2026, 10, 14, 19),
                 P("a3", "fullyfunded", 2026, 10, 15), P("a4", "fullyfunded", 2026, 10, 17)]
        iw.schedule(posts, date(2026, 10, 15), {}, [])
        self.assertEqual([p.new_date.day for p in posts], [15, 16, 17, 18])
        self.assertEqual(posts[1].publish_at.isoformat(), "2026-10-16T12:00:00-04:00")

    def test_pins_hold_and_overflow_goes_after(self):
        posts = [P("h1", "hourback", 2026, 10, 14, 13), P("h2", "hourback", 2026, 10, 14, 20),
                 P("h3", "hourback", 2026, 10, 15, 13), P("h4", "hourback", 2026, 10, 16, 13),
                 P("h5", "hourback", 2026, 10, 17, 13), P("kick", "hourback", 2026, 10, 19, 13)]
        warnings = iw.schedule(posts, date(2026, 10, 15), {"kick": date(2026, 10, 19)}, [])
        got = {p.id: p.new_date.day for p in posts}
        self.assertEqual(got, {"h1": 15, "h2": 16, "h3": 17, "h4": 18, "kick": 19, "h5": 20})
        self.assertTrue(any("h5" in w for w in warnings))
        self.assertEqual(posts[-1].publish_at.isoformat(), "2026-10-19T13:00:00-04:00")

    def test_defer_goes_after_last_pin(self):
        posts = [P("l1", "lockedhour", 2026, 10, 14, 12, 30), P("l2", "lockedhour", 2026, 10, 14, 19, 30),
                 P("l3", "lockedhour", 2026, 10, 15, 12, 30), P("l4", "lockedhour", 2026, 10, 16, 12, 30),
                 P("l5", "lockedhour", 2026, 10, 18, 12, 30), P("l6", "lockedhour", 2026, 10, 19, 12, 30),
                 P("l7", "lockedhour", 2026, 10, 20, 12, 30)]
        iw.schedule(posts, date(2026, 10, 15),
                    {"l5": date(2026, 10, 18), "l6": date(2026, 10, 19)}, ["l1"])
        got = {p.id: p.new_date.day for p in posts}
        self.assertEqual(got, {"l2": 15, "l3": 16, "l4": 17, "l5": 18, "l6": 19, "l1": 20, "l7": 21})

    def test_dst_offset(self):
        p = P("x", "hourback", 2026, 11, 2, 13)
        iw.schedule([p], date(2026, 11, 2), {}, [])
        self.assertEqual(p.publish_at.isoformat(), "2026-11-02T13:00:00-05:00")


if __name__ == "__main__":
    unittest.main()

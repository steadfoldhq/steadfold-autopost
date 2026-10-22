"""tools/queue_lint.py: the pre-publication checks (Oct 22 2026). No network, no Instagram."""
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import queue_lint as ql  # noqa: E402

NOW = datetime(2026, 10, 22, 18, 0, tzinfo=timezone.utc)
GOOD_VIDEO = {"format": {"size": "6000000", "duration": "14.2"},
              "streams": [{"codec_type": "video", "codec_name": "h264", "width": 1080, "height": 1920},
                          {"codec_type": "audio", "codec_name": "aac"}]}


class QueueLint(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.media = Path(self.tmp.name)
        for f in ("a.jpg", "b.jpg", "r.mp4", "r-cover.jpg", "s.jpg"):
            (self.media / f).write_bytes(b"x")

    def tearDown(self):
        self.tmp.cleanup()

    def run_lint(self, posts, published=None, probe=lambda f: GOOD_VIDEO, **kw):
        return ql.lint(posts, published or {}, NOW, media_root=self.media, prober=probe, **kw)

    def post(self, pid, when="2026-10-24T12:00:00-04:00", acct="fullyfunded", **extra):
        p = {"id": pid, "account": acct, "publish_at": when, "caption": "Hook.\n\nValue."}
        p.update(extra or {"images": ["a.jpg"]})
        return p

    def test_clean_queue_passes(self):
        e, w = self.run_lint([self.post("ff-1"), self.post("ff-2", images=["b.jpg"]),
                              self.post("ff-r", video="r.mp4", cover="r-cover.jpg")])
        self.assertEqual((e, w), ([], []))

    def test_reused_published_id_is_an_error(self):
        published = {"lh-follow": {"published_at": "2026-10-18T21:18:48Z"}}
        e, _ = self.run_lint([self.post("lh-follow", "2026-10-23T08:30:00-04:00")], published)
        self.assertTrue(any("reuses an old id" in x for x in e), e)
        e, _ = self.run_lint([self.post("lh-follow", "2026-10-21T08:30:00-04:00")], published)
        self.assertEqual(e, [], "past entries are only reported with --all")
        e, _ = self.run_lint([self.post("lh-follow", "2026-10-21T08:30:00-04:00")], published, check_all=True)
        self.assertTrue(any("reuses an old id" in x for x in e))

    def test_structural_errors(self):
        posts = [self.post("x"), self.post("x"), self.post("y", images=["missing.jpg"]),
                 {"id": "z", "account": "fullyfunded", "publish_at": "2026-10-24T12:00:00", "caption": ""}]
        e, _ = self.run_lint(posts)
        self.assertTrue(any("duplicate id" in x for x in e))
        self.assertTrue(any("missing media file media/missing.jpg" in x for x in e))
        self.assertTrue(any("without UTC offset" in x for x in e))

    def test_reel_limits(self):
        bad = {"format": {"size": "20000000", "duration": "38.0"},
               "streams": [{"codec_type": "video", "codec_name": "hevc", "width": 1080, "height": 1080},
                           {"codec_type": "audio", "codec_name": "aac"}]}
        e, w = self.run_lint([self.post("r", video="r.mp4", cover="r-cover.jpg")], probe=lambda f: bad)
        self.assertEqual(len([x for x in e if "Reel" in x]), 3, e)
        self.assertTrue(any("38.0 s" in x for x in w))
        e, _ = self.run_lint([self.post("r", video="r.mp4")], probe=lambda f: None)
        self.assertTrue(any("ffprobe failed" in x for x in e))

    def test_creative_warnings(self):
        posts = [self.post("ff-a", caption="Payday 🇨🇦 Canada edition, for example", images=["a.jpg"]),
                 self.post("ff-b", "2026-10-25T12:00:00-04:00", caption="Pension 🇨🇦", images=["a.jpg"]),
                 self.post("lf-a", acct="littlefold", caption="Sleep tip", images=["b.jpg"]),
                 self.post("ff-c", "2026-10-24T19:00:00-04:00", caption="Part 2 drops tonight.", images=["s.jpg"])]
        _, w = self.run_lint(posts)
        text = "\n".join(w)
        for needle in ("banned word 'example'", "'Canada edition' label", "2 Canada-flag posts",
                       "same media media/a.jpg", "not medical advice", "promises something 'tonight'"):
            self.assertIn(needle, text)

    def test_no_false_positives(self):
        posts = [self.post("ff-d", "2026-10-24T19:00:00-04:00", caption="Do this tonight (10 minutes): log in.", images=["d.jpg"]),
                 self.post("lf-b", acct="littlefold", caption="No RESP yet? It's not too late.", images=["e.jpg"]),
                 self.post("lf-c", acct="littlefold", caption="Small Wins No.2: you showered today.", images=["f.jpg"])]
        for n in "def":
            (self.media / f"{n}.jpg").write_bytes(b"x")
        _, w = self.run_lint(posts)
        self.assertFalse(any("tonight" in x or "medical" in x for x in w), w)

    def test_daily_ceiling(self):
        posts = [self.post(f"ff-{i}", f"2026-10-24T{10 + i}:00:00-04:00", images=[f"{i}.jpg"]) for i in range(3)]
        for i in range(3):
            (self.media / f"{i}.jpg").write_bytes(b"x")
        _, w = self.run_lint(posts)
        self.assertTrue(any("3 feed posts (ceiling 2)" in x for x in w), w)

    def test_cli_exit_codes(self):
        d = Path(self.tmp.name)
        (d / "posts.json").write_text(json.dumps({"posts": []}))
        self.assertEqual(ql.main(["--posts", str(d / "posts.json"), "--state", str(d / "none.json"),
                                  "--now", "2026-10-22T18:00:00+00:00"]), 0)
        self.assertEqual(ql.main(["--posts", str(d / "nope.json")]), 2)
        self.assertEqual(ql.main(["--posts", str(d / "posts.json"), "--now", "2026-10-22T18:00:00"]), 2)


if __name__ == "__main__":
    unittest.main()

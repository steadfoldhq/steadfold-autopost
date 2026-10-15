"""Tests for autopost.py. Run with:  python -m unittest discover -s tests -v
(or python -m pytest tests).  No network: Instagram is simulated by tests/fakes.py."""

from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import autopost  # noqa: E402
from fakes import FakeGraph  # noqa: E402

TOK_FF = "IGAAtokenFULLYFUNDED0001"
TOK_LH = "IGAAtokenLOCKEDHOUR0002"
TOK_HB = "IGAAtokenHOURBACK0003"
UID = {"fullyfunded": "17841400000000001", "lockedhour": "17841400000000002",
       "hourback": "17841400000000003"}
ENV = {"IG_TOKEN_FULLYFUNDED": TOK_FF, "IG_TOKEN_LOCKEDHOUR": TOK_LH,
       "IG_TOKEN_HOURBACK": TOK_HB, "GITHUB_REPOSITORY": "dharma/steadfold-autopost"}
NOW = datetime(2026, 10, 15, 16, 5, tzinfo=timezone.utc)   # 12:05 Toronto
BASE = "https://raw.githubusercontent.com/dharma/steadfold-autopost/main/media"


def graph(**over) -> FakeGraph:
    tokens = {TOK_FF: (UID["fullyfunded"], "fullyfundedhq"),
              TOK_LH: (UID["lockedhour"], "lockedhourhq"),
              TOK_HB: (UID["hourback"], "hourbackhq")}
    tokens.update(over)
    return FakeGraph(tokens)


def post(pid="ff-test-1", account="fullyfunded", at="2026-10-15T12:00:00-04:00",
         n_images=3, comment="First comment!", alt="Alt text for slide 1"):
    return {"id": pid, "account": account, "publish_at": at,
            "caption": f"Caption for {pid}\n\nSecond paragraph.\n\n#tag1 #tag2",
            "first_comment": comment, "alt_text": alt,
            "images": [f"{pid}/{i:02d}.jpg" for i in range(1, n_images + 1)]}


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.posts_file = self.dir / "posts.json"
        self.state_file = self.dir / "published.json"
        self.media = self.dir / "media"
        self.sleeps: list[float] = []

    def tearDown(self):
        self.tmp.cleanup()

    def write_posts(self, posts):
        for p in posts:
            for rel in [p[k] for k in ("video", "cover") if p.get(k)]:
                f = self.media / rel
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_bytes(b"fake media")
            for rel in p.get("images", []):
                f = self.media / rel
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_bytes(b"\xff\xd8\xff fake jpeg")
        self.posts_file.write_text(json.dumps({"posts": posts}), encoding="utf-8")

    def run_main(self, g, *args, now=NOW, env=None, timeout=300):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = autopost.main(
                ["--posts", str(self.posts_file), "--state", str(self.state_file),
                 "--media-dir", str(self.media), *args],
                session=g, env=dict(ENV if env is None else env), now=now,
                sleep=self.sleeps.append, poll_interval=10, poll_timeout=timeout)
        self.output = out.getvalue()
        return code

    def state(self):
        if not self.state_file.exists():
            return {}
        return json.loads(self.state_file.read_text())["posts"]


class CarouselFlow(Base):
    def test_call_order_and_params(self):
        self.write_posts([post()])
        g = graph()
        g.status_script = ["FINISHED"]
        self.assertEqual(self.run_main(g), 0, self.output)

        seq = [(c.method, c.path) for c in g.calls]
        u = UID["fullyfunded"]
        self.assertEqual(seq[0], ("GET", "me"))
        self.assertEqual(seq[1], ("GET", f"{u}/media"))           # double-post guard
        self.assertEqual([m for m, _ in seq[2:5]], ["HEAD"] * 3)  # public image check
        self.assertEqual(seq[5:8], [("POST", f"{u}/media")] * 3)  # 3 carousel items
        self.assertEqual(seq[8], ("POST", f"{u}/media"))          # carousel container
        self.assertEqual(seq[9][0], "GET")                        # status poll
        self.assertEqual(seq[10], ("POST", f"{u}/media_publish"))
        self.assertEqual(seq[11][0], "GET")                       # permalink
        self.assertTrue(seq[12][0] == "POST" and seq[12][1].endswith("/comments"))
        self.assertEqual(len(seq), 13)

        items = g.calls[5:8]
        for i, c in enumerate(items, 1):
            self.assertEqual(c.data["image_url"], f"{BASE}/ff-test-1/{i:02d}.jpg")
            self.assertEqual(c.data["is_carousel_item"], "true")
        self.assertEqual(items[0].data["alt_text"], "Alt text for slide 1")
        self.assertNotIn("alt_text", items[1].data)
        carousel = g.calls[8]
        self.assertEqual(carousel.data["media_type"], "CAROUSEL")
        self.assertEqual(carousel.data["children"], "1001,1002,1003")
        self.assertTrue(carousel.data["caption"].startswith("Caption for ff-test-1"))
        self.assertEqual(g.calls[9].params["fields"], "status_code,status")
        carousel_id = str(1004)
        self.assertEqual(g.calls[10].data["creation_id"], carousel_id)
        self.assertEqual(g.calls[12].data["message"], "First comment!")
        # Tokens are sent in the POST body, never in a URL.
        for c in g.calls:
            self.assertNotIn("access_token", c.url)
        self.assertNotIn(TOK_FF, self.output)

        st = self.state()["ff-test-1"]
        self.assertEqual(st["status"], "published")
        self.assertEqual(st["comment_status"], "done")
        self.assertEqual(st["container_id"], carousel_id)
        self.assertEqual(st["children"], ["1001", "1002", "1003"])
        self.assertTrue(st["permalink"].startswith("https://www.instagram.com/p/"))
        self.assertFalse(st["late"])

    def test_not_yet_due_is_left_alone(self):
        self.write_posts([post(at="2026-10-15T13:00:00-04:00")])
        g = graph()
        self.assertEqual(self.run_main(g), 0)
        self.assertEqual(g.calls, [])
        self.assertEqual(self.state(), {})

    def test_reel_post(self):
        reel = {"id": "lf-reel-1", "account": "fullyfunded", "publish_at": "2026-10-15T12:00:00-04:00",
                "caption": "Reel caption\n\n#tag", "first_comment": "Hi!",
                "video": "reels/lf-reel-1.mp4", "cover": "reels/lf-reel-1-cover.jpg"}
        self.write_posts([reel])
        g = graph()
        self.assertEqual(self.run_main(g, env={**ENV, "GITHUB_SHA": "abc123"}), 0, self.output)
        create = [c for c in g.posts() if c.path.endswith("/media")]
        self.assertEqual(len(create), 1)
        self.assertEqual(create[0].data["media_type"], "REELS")
        self.assertEqual(create[0].data["video_url"],
                         "https://cdn.jsdelivr.net/gh/dharma/steadfold-autopost@abc123/media/reels/lf-reel-1.mp4")
        self.assertTrue(create[0].data["cover_url"].endswith("/media/reels/lf-reel-1-cover.jpg"))
        self.assertEqual(create[0].data["share_to_feed"], "true")
        self.assertEqual(len(g.publishes()), 1)
        self.assertEqual(self.state()["lf-reel-1"]["status"], "published")

    def test_reel_must_be_mp4(self):
        reel = {"id": "r2", "account": "fullyfunded", "publish_at": "2026-10-15T12:00:00-04:00",
                "caption": "c", "video": "reels/r2.mov"}
        self.write_posts([reel])
        self.assertNotEqual(self.run_main(graph()), 0)
        self.assertIn("not an .mp4", self.output)

    def test_single_image_post(self):
        self.write_posts([post(n_images=1)])
        g = graph()
        self.assertEqual(self.run_main(g), 0, self.output)
        create = [c for c in g.posts() if c.path.endswith("/media")]
        self.assertEqual(len(create), 1)
        self.assertNotIn("is_carousel_item", create[0].data)
        self.assertNotIn("media_type", create[0].data)
        self.assertEqual(len(g.publishes()), 1)

    def test_alt_text_rejected_falls_back(self):
        self.write_posts([post()])
        g = graph()
        g.reject_alt_text = True
        self.assertEqual(self.run_main(g), 0, self.output)
        self.assertEqual(len(g.publishes()), 1)
        self.assertIn("alt text was rejected", self.output)


class Polling(Base):
    def test_polls_until_finished(self):
        self.write_posts([post()])
        g = graph()
        g.status_script = ["IN_PROGRESS", "IN_PROGRESS", "FINISHED"]
        self.assertEqual(self.run_main(g), 0, self.output)
        polls = [c for c in g.calls if c.method == "GET" and c.params.get("fields") == "status_code,status"]
        self.assertEqual(len(polls), 3)
        self.assertEqual(self.sleeps, [10, 10])
        # media_publish only after the FINISHED poll
        idx_pub = g.calls.index(g.publishes()[0])
        self.assertGreater(idx_pub, g.calls.index(polls[-1]))

    def test_error_status_means_no_publish(self):
        self.write_posts([post()])
        g = graph()
        g.status_script = ["ERROR"]
        self.assertEqual(self.run_main(g), 1)
        self.assertEqual(g.publishes(), [])
        st = self.state()["ff-test-1"]
        self.assertEqual(st["status"], "failed")
        self.assertIn("ERROR", st["error"])
        self.assertEqual(st["attempts"], 1)

    def test_timeout_resumes_same_container_next_run(self):
        self.write_posts([post()])
        g = graph()
        g.status_script = ["IN_PROGRESS"] * 4
        self.assertEqual(self.run_main(g, timeout=20), 0, self.output)
        self.assertEqual(g.publishes(), [])
        st = self.state()["ff-test-1"]
        self.assertEqual(st["status"], "publishing")
        container = st["container_id"]
        n_creates = len([c for c in g.posts() if c.path.endswith("/media")])
        # Next run: no new containers, same container gets published.
        g.calls.clear()
        g.status_script = ["FINISHED"]
        self.assertEqual(self.run_main(g, now=NOW + timedelta(minutes=15)), 0, self.output)
        self.assertEqual([c for c in g.posts() if c.path.endswith("/media")], [])
        self.assertEqual(g.publishes()[0].data["creation_id"], container)
        self.assertEqual(n_creates, 4)
        self.assertEqual(self.state()["ff-test-1"]["status"], "published")


class Idempotency(Base):
    def test_second_run_does_nothing(self):
        self.write_posts([post()])
        g = graph()
        self.assertEqual(self.run_main(g), 0, self.output)
        self.assertEqual(len(g.publishes()), 1)
        g.calls.clear()
        self.assertEqual(self.run_main(g, now=NOW + timedelta(minutes=15)), 0)
        self.assertEqual(g.calls, [])  # no requests at all, let alone POSTs

    def test_lost_state_does_not_double_post(self):
        self.write_posts([post()])
        g = graph()
        self.assertEqual(self.run_main(g), 0)
        self.state_file.unlink()   # e.g. the state commit failed to push
        g.calls.clear()
        self.assertEqual(self.run_main(g, now=NOW + timedelta(minutes=15)), 0, self.output)
        self.assertEqual(g.posts(), [])
        st = self.state()["ff-test-1"]
        self.assertEqual(st["status"], "published")
        self.assertTrue(st["recovered"])

    def test_crash_after_publish_call_is_recovered(self):
        """State says publish was called but no media id was saved (crash)."""
        self.write_posts([post()])
        g = graph()
        self.assertEqual(self.run_main(g), 0)
        st = json.loads(self.state_file.read_text())
        entry = st["posts"]["ff-test-1"]
        for k in ("media_id", "permalink", "comment_status", "comment_id"):
            entry.pop(k, None)
        entry["status"] = "publishing"
        self.state_file.write_text(json.dumps(st))
        g.comments.clear()
        g.calls.clear()
        self.assertEqual(self.run_main(g, now=NOW + timedelta(minutes=15)), 0, self.output)
        self.assertEqual(g.publishes(), [])
        st = self.state()["ff-test-1"]
        self.assertEqual(st["status"], "published")
        self.assertEqual(st["comment_status"], "done")  # ours, so the comment is posted

    def test_one_post_per_account_per_run(self):
        self.write_posts([post("a1", at="2026-10-14T12:00:00-04:00"),
                          post("a2", at="2026-10-15T12:00:00-04:00"),
                          post("b1", account="lockedhour", at="2026-10-15T12:00:00-04:00")])
        g = graph()
        self.assertEqual(self.run_main(g), 0, self.output)
        self.assertEqual(len(g.publishes()), 2)       # a1 + b1
        self.assertNotIn("a2", self.state())
        self.assertEqual(self.run_main(g, now=NOW + timedelta(minutes=15)), 0)
        self.assertEqual(self.state()["a2"]["status"], "published")


class Late(Base):
    def test_late_post_is_published_and_flagged(self):
        self.write_posts([post(at="2026-10-15T03:00:00-04:00")])  # 9h05m ago
        g = graph()
        self.assertEqual(self.run_main(g), 0, self.output)
        self.assertEqual(len(g.publishes()), 1)
        self.assertIn("LATE", self.output)
        self.assertTrue(self.state()["ff-test-1"]["late"])

    def test_within_six_hours_is_not_late(self):
        self.write_posts([post(at="2026-10-15T07:00:00-04:00")])  # 5h05m ago
        g = graph()
        self.assertEqual(self.run_main(g), 0)
        self.assertNotIn("LATE", self.output)
        self.assertFalse(self.state()["ff-test-1"]["late"])


class Accounts(Base):
    def test_username_mismatch_refuses(self):
        self.write_posts([post()])
        g = graph(**{TOK_FF: (UID["fullyfunded"], "someoneelse")})
        self.assertEqual(self.run_main(g), 1)
        self.assertEqual(g.posts(), [])
        self.assertIn("belongs to @someoneelse", self.output)
        self.assertIn("Refusing to post", self.output)
        self.assertEqual(self.state(), {})  # nothing recorded; it'll try again once fixed

    def test_missing_token_only_matters_when_a_post_is_due(self):
        self.write_posts([post(), post("hb-1", account="hourback",
                                       at="2026-10-20T13:00:00-04:00")])
        env = dict(ENV)
        env.pop("IG_TOKEN_HOURBACK")
        g = graph()
        self.assertEqual(self.run_main(g, env=env), 0, self.output)
        env.pop("IG_TOKEN_FULLYFUNDED")
        self.state_file.unlink()
        g2 = graph()
        self.assertEqual(self.run_main(g2, env=env), 1)
        self.assertIn("IG_TOKEN_FULLYFUNDED is not set", self.output)
        self.assertEqual(g2.calls, [])

    def test_expired_token(self):
        self.write_posts([post()])
        g = graph()
        env = dict(ENV, IG_TOKEN_FULLYFUNDED="IGAAexpiredTOKEN999")
        self.assertEqual(self.run_main(g, env=env), 1)
        self.assertIn("expired or revoked", self.output)
        self.assertNotIn("IGAAexpiredTOKEN999", self.output)


class Comments(Base):
    def test_comment_failure_does_not_republish(self):
        self.write_posts([post()])
        g = graph()
        g.fail_comment = 1
        self.assertEqual(self.run_main(g), 1)        # non-zero so GitHub emails
        st = self.state()["ff-test-1"]
        self.assertEqual(st["status"], "published")
        self.assertEqual(st["comment_status"], "failed")
        self.assertIn("LIVE but the first comment failed", self.output)
        self.assertEqual(len(g.publishes()), 1)

        g.calls.clear()
        self.assertEqual(self.run_main(g, now=NOW + timedelta(minutes=15)), 0, self.output)
        self.assertEqual(g.publishes(), [])          # never published again
        self.assertEqual([c.path.split("/")[-1] for c in g.posts()], ["comments"])
        self.assertEqual(self.state()["ff-test-1"]["comment_status"], "done")

        g.calls.clear()
        self.assertEqual(self.run_main(g, now=NOW + timedelta(minutes=30)), 0)
        self.assertEqual(g.calls, [])

    def test_comment_retry_skips_if_comment_already_there(self):
        self.write_posts([post()])
        g = graph()
        self.assertEqual(self.run_main(g), 0)
        st = json.loads(self.state_file.read_text())
        st["posts"]["ff-test-1"]["comment_status"] = "failed"   # response was lost
        st["posts"]["ff-test-1"]["comment_attempts"] = 1
        self.state_file.write_text(json.dumps(st))
        g.calls.clear()
        self.assertEqual(self.run_main(g, now=NOW + timedelta(minutes=15)), 0)
        self.assertEqual(g.posts(), [])
        self.assertEqual(self.state()["ff-test-1"]["comment_status"], "done")

    def test_comment_gives_up_after_max_attempts(self):
        self.write_posts([post()])
        g = graph()
        g.fail_comment = 99
        t = NOW
        for _ in range(autopost.MAX_COMMENT_ATTEMPTS):
            self.assertEqual(self.run_main(g, now=t), 1)
            t += timedelta(minutes=15)
        g.calls.clear()
        self.assertEqual(self.run_main(g, now=t), 0)
        self.assertEqual(g.calls, [])
        self.assertEqual(len(g.publishes()), 0)


class Failures(Base):
    def test_failed_post_does_not_block_others_and_retries(self):
        self.write_posts([post(), post("lh-1", account="lockedhour")])
        g = graph()
        g.fail_publish = 1
        self.assertEqual(self.run_main(g), 1)
        st = self.state()
        self.assertEqual(st["ff-test-1"]["status"], "failed")
        self.assertEqual(st["lh-1"]["status"], "published")
        # next run retries the failed one, reusing its FINISHED container
        g.calls.clear()
        self.assertEqual(self.run_main(g, now=NOW + timedelta(minutes=15)), 0, self.output)
        self.assertEqual(self.state()["ff-test-1"]["status"], "published")
        self.assertEqual(len([c for c in g.posts() if c.path.endswith("/media")]), 0)

    def test_gives_up_after_max_attempts_then_retry_flag(self):
        self.write_posts([post()])
        g = graph()
        g.fail_publish = autopost.MAX_PUBLISH_ATTEMPTS
        t = NOW
        for _ in range(autopost.MAX_PUBLISH_ATTEMPTS):
            self.assertEqual(self.run_main(g, now=t), 1)
            t += timedelta(minutes=15)
        g.calls.clear()
        self.assertEqual(self.run_main(g, now=t), 0)   # gave up quietly (noted)
        self.assertEqual(g.calls, [])
        self.assertIn("gave up", self.output)
        self.assertEqual(self.run_main(g, "--retry-failed", now=t), 0, self.output)
        self.assertEqual(self.state()["ff-test-1"]["status"], "published")

    def test_invalid_post_is_reported(self):
        bad = post()
        bad["images"] = [f"x/{i}.jpg" for i in range(11)]
        self.write_posts([bad])
        g = graph()
        self.assertEqual(self.run_main(g), 1)
        self.assertIn("1 to 10", self.output)
        self.assertEqual(g.calls, [])

    def test_png_rejected(self):
        bad = post()
        bad["images"] = ["ff-test-1/01.png", "ff-test-1/02.png"]
        self.write_posts([bad])
        self.assertEqual(self.run_main(graph()), 1)
        self.assertIn("not a .jpg", self.output)

    def test_private_repo_images_fail_clearly(self):
        self.write_posts([post()])
        g = graph()
        g.head_status = 404
        self.assertEqual(self.run_main(g), 1)
        self.assertIn("Is the repo public", self.output)
        self.assertEqual([c for c in g.posts()], [])


class DryRun(Base):
    def test_dry_run_makes_no_posts_and_saves_nothing(self):
        self.write_posts([post(), post("lh-1", account="lockedhour")])
        g = graph()
        self.assertEqual(self.run_main(g, "--dry-run"), 0, self.output)
        self.assertEqual(g.posts(), [])
        self.assertFalse(self.state_file.exists())
        self.assertIn("WOULD publish a CAROUSEL of 3 image(s)", self.output)
        self.assertIn("WOULD comment", self.output)

    def test_dry_run_with_now_and_no_tokens(self):
        self.write_posts([post()])
        g = graph()
        code = self.run_main(g, "--dry-run", "--now", "2026-10-15T12:01:00-04:00",
                             env={}, now=None)
        self.assertEqual(code, 0, self.output)
        self.assertEqual(g.calls, [])

    def test_now_requires_dry_run(self):
        self.write_posts([post()])
        self.assertEqual(self.run_main(graph(), "--now", "2026-10-15T12:01:00-04:00"), 2)


class Redaction(unittest.TestCase):
    def test_redact(self):
        autopost.register_secret("IGAAsupersecret123")
        s = autopost.redact("GET https://x/me?fields=a&access_token=IGAAsupersecret123&x=1 "
                            "and IGAAsupersecret123 and access_token=other")
        self.assertNotIn("supersecret", s)
        self.assertNotIn("other", s)


class RealSchedule(unittest.TestCase):
    """The generated schedule/posts.json must be valid and point at real files."""

    def test_repo_schedule_is_valid(self):
        root = Path(__file__).resolve().parent.parent
        posts = autopost.load_posts(root / "schedule" / "posts.json")
        self.assertGreater(len(posts), 0)
        for p in posts:
            self.assertEqual(autopost.validate_post(p, root / "media"), [], p["id"])
        # at most one feed post and one Reel per account per Toronto day
        seen = set()
        for p in posts:
            key = (p["account"], p["publish_at"][:10], "reel" if p.get("video") else "feed")
            self.assertNotIn(key, seen)
            seen.add(key)


if __name__ == "__main__":
    unittest.main()

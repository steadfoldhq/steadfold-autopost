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
            for rel in [p[k] for k in ("video", "cover", "image") if p.get(k)]:
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

    def test_trial_reel_auto(self):
        reel = {"id": "t1", "account": "fullyfunded", "publish_at": "2026-10-15T12:00:00-04:00",
                "caption": "c", "video": "reels/t1.mp4", "trial": "auto"}
        self.write_posts([reel])
        g = graph()
        self.assertEqual(self.run_main(g), 0, self.output)
        create = [c for c in g.posts() if c.path.endswith("/media")][0]
        self.assertEqual(json.loads(create.data["trial_params"]), {"graduation_strategy": "SS_PERFORMANCE"})
        self.assertNotIn("share_to_feed", create.data)

    def test_trial_rejected_falls_back_to_normal_reel(self):
        reel = {"id": "t2", "account": "fullyfunded", "publish_at": "2026-10-15T12:00:00-04:00",
                "caption": "c", "video": "reels/t2.mp4", "trial": "manual"}
        self.write_posts([reel])
        g = graph(); g.reject_trial = True
        self.assertEqual(self.run_main(g), 0, self.output)
        self.assertEqual(len(g.publishes()), 1)
        self.assertIn("Trial Reel not accepted", self.output)

    def test_bad_trial_value(self):
        reel = {"id": "t3", "account": "fullyfunded", "publish_at": "2026-10-15T12:00:00-04:00",
                "caption": "c", "video": "reels/t3.mp4", "trial": "yes"}
        self.assertTrue(autopost.validate_post(reel, None))

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


def mixed_post(pid="ff-mix-1", images=None, **kw):
    p = post(pid, **kw)
    p["images"] = images or [f"{pid}/01.jpg", f"{pid}/02.mp4", f"{pid}/03.jpg"]
    return p


JSD = "https://cdn.jsdelivr.net/gh/dharma/steadfold-autopost@abc123/media"
ENV_SHA = {**ENV, "GITHUB_SHA": "abc123"}


class CarouselVideo(Base):
    """Carousels whose "images" list mixes .jpg photos and .mp4 video slides."""

    def creates(self, g):
        return [c for c in g.posts() if c.path.endswith("/media")]

    def test_mixed_carousel_is_created_and_published(self):
        self.write_posts([mixed_post()])
        g = graph()
        g.video_item_script = ["IN_PROGRESS", "FINISHED"]
        self.assertEqual(self.run_main(g, env=ENV_SHA), 0, self.output)
        u = UID["fullyfunded"]

        heads = [c for c in g.calls if c.method == "HEAD"]
        self.assertEqual([c.url for c in heads], [f"{BASE}/ff-mix-1/01.jpg", f"{JSD}/ff-mix-1/02.mp4",
                                                  f"{BASE}/ff-mix-1/03.jpg"])
        creates = self.creates(g)
        self.assertEqual(len(creates), 4)                           # 3 items + the carousel
        photo1, video, photo2, carousel = creates
        self.assertEqual(photo1.data["image_url"], f"{BASE}/ff-mix-1/01.jpg")
        self.assertEqual(photo1.data["alt_text"], "Alt text for slide 1")
        self.assertEqual(video.data, {"media_type": "VIDEO", "video_url": f"{JSD}/ff-mix-1/02.mp4",
                                      "is_carousel_item": "true", "access_token": TOK_FF})
        self.assertEqual(photo2.data["image_url"], f"{BASE}/ff-mix-1/03.jpg")
        self.assertNotIn("alt_text", photo2.data)
        self.assertEqual(carousel.data["media_type"], "CAROUSEL")
        self.assertEqual(carousel.data["children"], "1001,1002,1003")

        # The video item is polled until FINISHED *before* the carousel container exists.
        video_polls = [i for i, c in enumerate(g.calls) if c.method == "GET" and c.path == "1002"]
        self.assertEqual(len(video_polls), 2)
        self.assertLess(video_polls[-1], g.calls.index(carousel))
        self.assertEqual(self.sleeps, [10])
        self.assertEqual(len(g.publishes()), 1)
        self.assertEqual(g.publishes()[0].data["creation_id"], "1004")
        self.assertEqual(g.publishes()[0].path, f"{u}/media_publish")
        st = self.state()["ff-mix-1"]
        self.assertEqual(st["status"], "published")
        self.assertEqual(st["children"], ["1001", "1002", "1003"])
        self.assertEqual(st["comment_status"], "done")
        self.assertIn("1 video, 2 image", self.output)

    def test_video_first_puts_alt_text_on_first_photo(self):
        self.write_posts([mixed_post(images=["v/01.mp4", "v/02.jpg", "v/03.jpg"])])
        g = graph()
        self.assertEqual(self.run_main(g, env=ENV_SHA), 0, self.output)
        video, photo1, photo2, _ = self.creates(g)
        self.assertEqual(video.data["media_type"], "VIDEO")
        self.assertEqual(photo1.data["alt_text"], "Alt text for slide 1")
        self.assertNotIn("alt_text", photo2.data)
        self.assertEqual(len(g.publishes()), 1)

    def test_video_falls_back_to_raw_github_when_jsdelivr_fails(self):
        self.write_posts([mixed_post()])
        g = graph()
        g.head_fail_hosts = {"cdn.jsdelivr.net"}
        self.assertEqual(self.run_main(g, env=ENV_SHA), 0, self.output)
        video = self.creates(g)[1]
        self.assertEqual(video.data["video_url"], f"{BASE}/ff-mix-1/02.mp4")
        self.assertIn("video host check failed", self.output)

    def test_video_child_that_never_finishes_times_out_cleanly(self):
        self.write_posts([mixed_post()])
        g = graph()
        g.video_never_finishes = True
        self.assertEqual(self.run_main(g, env=ENV_SHA, timeout=30), 0, self.output)
        self.assertEqual(len(self.creates(g)), 3)                   # items only
        self.assertFalse(any(c.data.get("media_type") == "CAROUSEL" for c in g.posts()))
        self.assertEqual(g.publishes(), [])
        self.assertEqual(self.sleeps, [10, 10, 10])
        self.assertIn("still IN_PROGRESS after 30s", self.output)
        self.assertIn("still processing", self.output)
        st = self.state()["ff-mix-1"]
        self.assertEqual(st["status"], "publishing")
        self.assertNotIn("container_id", st)
        self.assertEqual(st["children"], ["1001", "1002", "1003"])
        self.assertEqual(st.get("attempts", 0), 0)                  # not counted as a failure

        # Next run: Instagram has finished; the same items are reused (no re-upload).
        g.calls.clear()
        g.video_never_finishes = False
        self.assertEqual(self.run_main(g, env=ENV_SHA, now=NOW + timedelta(minutes=15)), 0,
                         self.output)
        creates = self.creates(g)
        self.assertEqual(len(creates), 1)
        self.assertEqual(creates[0].data["children"], "1001,1002,1003")
        self.assertEqual(len(g.publishes()), 1)
        self.assertIn("reusing 3 item containers", self.output)
        self.assertEqual(self.state()["ff-mix-1"]["status"], "published")

    def test_video_child_error_fails_then_rebuilds(self):
        self.write_posts([mixed_post()])
        g = graph()
        g.video_item_script = ["ERROR"]
        self.assertEqual(self.run_main(g, env=ENV_SHA), 1)
        self.assertEqual(g.publishes(), [])
        st = self.state()["ff-mix-1"]
        self.assertEqual(st["status"], "failed")
        self.assertIn("status ERROR", st["error"])
        g.calls.clear()
        self.assertEqual(self.run_main(g, env=ENV_SHA, now=NOW + timedelta(minutes=15)), 0,
                         self.output)
        self.assertIn("rebuilding all items", self.output)
        self.assertEqual(len(self.creates(g)), 4)                   # fresh items + carousel
        self.assertEqual(self.state()["ff-mix-1"]["status"], "published")

    # -- validation ------------------------------------------------------------------------
    def problems(self, p, make_files=True):
        if make_files:
            self.write_posts([p])
        return "; ".join(autopost.validate_post(p, self.media))

    def test_valid_mixed_carousel(self):
        self.assertEqual(self.problems(mixed_post()), "")

    def test_more_than_ten_items_in_total(self):
        p = mixed_post(images=[f"x/{i:02d}.jpg" for i in range(6)] + [f"x/{i:02d}.mp4" for i in range(6, 11)])
        self.assertIn("1 to 10", self.problems(p))
        self.write_posts([p])
        g = graph()
        self.assertEqual(self.run_main(g), 1)
        self.assertEqual(g.calls, [])

    def test_missing_video_file(self):
        p = mixed_post()
        self.write_posts([p])
        (self.media / "ff-mix-1/02.mp4").unlink()
        self.assertIn("video file media/ff-mix-1/02.mp4 is missing",
                      self.problems(p, make_files=False))

    def test_video_over_size_limit(self):
        p = mixed_post()
        self.write_posts([p])
        with open(self.media / "ff-mix-1/02.mp4", "r+b") as f:
            f.truncate(autopost.MAX_VIDEO_BYTES + 1)              # sparse file, no disk cost
        self.assertIn("is over 19.5 MB", self.problems(p, make_files=False))
        g = graph()
        self.assertEqual(self.run_main(g), 1)
        self.assertIn("invalid post, skipped", self.output)
        self.assertEqual(g.calls, [])

    def test_other_video_formats_rejected(self):
        self.assertIn("not a .jpg (Instagram only accepts JPEG) or an .mp4 video",
                      self.problems(mixed_post(images=["m/01.jpg", "m/02.mov"])))

    def test_single_video_must_be_a_reel(self):
        self.assertIn("post it as a Reel", self.problems(mixed_post(images=["m/01.mp4"])))

    def test_dry_run_lists_video_items(self):
        self.write_posts([mixed_post()])
        g = graph()
        self.assertEqual(self.run_main(g, "--dry-run", env=ENV_SHA), 0, self.output)
        self.assertEqual(g.posts(), [])
        self.assertIn("WOULD publish a CAROUSEL of 3 items (1 video, 2 images)", self.output)
        self.assertIn(f"video {JSD}/ff-mix-1/02.mp4", self.output)


class Redaction(unittest.TestCase):
    def test_redact(self):
        autopost.register_secret("IGAAsupersecret123")
        s = autopost.redact("GET https://x/me?fields=a&access_token=IGAAsupersecret123&x=1 "
                            "and IGAAsupersecret123 and access_token=other")
        self.assertNotIn("supersecret", s)
        self.assertNotIn("other", s)


def story(pid="ff-story-1", account="fullyfunded", at="2026-10-15T12:00:00-04:00", video=False):
    p = {"id": pid, "account": account, "publish_at": at, "story": True, "caption": "note"}
    p["video" if video else "image"] = f"stories/{pid}.{'mp4' if video else 'jpg'}"
    return p


class Stories(Base):
    def test_image_story(self):
        self.write_posts([story()])
        g = graph()
        self.assertEqual(self.run_main(g), 0, self.output)
        create = [c for c in g.posts() if c.path.endswith("/media")]
        self.assertEqual(len(create), 1)
        self.assertEqual(create[0].data["media_type"], "STORIES")
        self.assertEqual(create[0].data["image_url"], f"{BASE}/stories/ff-story-1.jpg")
        self.assertNotIn("caption", create[0].data)
        self.assertEqual(len(g.publishes()), 1)
        st = self.state()["ff-story-1"]
        self.assertEqual((st["status"], st["kind"]), ("published", "story"))

    def test_video_story_uses_video_host(self):
        self.write_posts([story(video=True)])
        g = graph()
        self.assertEqual(self.run_main(g, env={**ENV, "GITHUB_SHA": "abc"}), 0, self.output)
        create = [c for c in g.posts() if c.path.endswith("/media")][0]
        self.assertTrue(create.data["video_url"].startswith("https://cdn.jsdelivr.net/gh/"))
        self.assertEqual(len(g.publishes()), 1)

    def test_story_does_not_block_feed_post_same_run(self):
        self.write_posts([post(), story()])
        g = graph()
        self.assertEqual(self.run_main(g), 0, self.output)
        self.assertEqual(len(g.publishes()), 2)

    def test_one_story_per_account_per_run(self):
        self.write_posts([story("s1"), story("s2")])
        g = graph()
        self.assertEqual(self.run_main(g), 0, self.output)
        self.assertEqual(len(g.publishes()), 1)
        self.assertEqual(self.run_main(g), 0, self.output)
        self.assertEqual(len(g.publishes()), 2)
        self.assertEqual(self.run_main(g), 0, self.output)
        self.assertEqual(len(g.publishes()), 2)   # never re-posted

    def test_never_republished_after_unrecorded_publish(self):
        self.write_posts([story()])
        self.state_file.write_text(json.dumps({"posts": {"ff-story-1": {
            "account": "fullyfunded", "status": "publishing", "publish_called": True}}}))
        g = graph()
        self.assertNotEqual(self.run_main(g), 0)
        self.assertEqual(len(g.publishes()), 0)
        self.assertEqual(self.state()["ff-story-1"]["attempts"], autopost.MAX_PUBLISH_ATTEMPTS)

    def test_refused_story_publish_is_retried(self):
        self.write_posts([story()])
        g = graph()
        g.fail_publish = 1
        self.assertNotEqual(self.run_main(g), 0)
        self.assertEqual(self.state()["ff-story-1"]["status"], "failed")
        self.assertFalse(self.state()["ff-story-1"]["publish_called"])
        self.assertEqual(self.run_main(g), 0, self.output)
        self.assertEqual(self.state()["ff-story-1"]["status"], "published")

    def test_story_validation(self):
        bad = story()
        bad["video"] = "stories/x.mp4"
        self.assertTrue(any("exactly one" in e for e in autopost.validate_story(bad, None)))
        bad = story()
        bad["first_comment"] = "hi"
        self.assertTrue(autopost.validate_story(bad, None))
        bad = story()
        bad["image"] = "stories/x.png"
        self.assertTrue(any("not a .jpg" in e for e in autopost.validate_story(bad, None)))
        ok = story()
        del ok["caption"]
        self.assertEqual(autopost.validate_story(ok, None), [])

    def test_dry_run_describes_story(self):
        self.write_posts([story()])
        g = graph()
        self.assertEqual(self.run_main(g, "--dry-run"), 0, self.output)
        self.assertIn("WOULD publish a STORY (image)", self.output)
        self.assertEqual(len(g.publishes()), 0)


class RealSchedule(unittest.TestCase):
    """The generated schedule/posts.json must be valid and point at real files."""

    def test_repo_schedule_is_valid(self):
        root = Path(__file__).resolve().parent.parent
        posts = autopost.load_posts(root / "schedule" / "posts.json")
        self.assertGreater(len(posts), 0)
        for p in posts:
            self.assertEqual(autopost.validate_post(p, root / "media"), [], p["id"])
        # daily ceilings per account per Toronto day (brand-system-v4 cadence, Oct 15):
        # 2 feed posts, 2 Reels, 5 Stories
        caps = {"feed": 2, "reel": 2, "story": 5}
        count: dict = {}
        for p in posts:
            kind = "story" if p.get("story") else ("reel" if p.get("video") else "feed")
            key = (p["account"], p["publish_at"][:10], kind)
            count[key] = count.get(key, 0) + 1
            self.assertLessEqual(count[key], caps[kind], key)


if __name__ == "__main__":
    unittest.main()

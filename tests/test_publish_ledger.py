"""Tests for tools/publish_ledger.py (read-only Publish Ledger). unittest only, no network, no third-party packages.

STAGING COPY (steadfold docs/v062). Intended path in steadfold-autopost: tests/test_publish_ledger.py.
It finds the tool at <repo>/tools/publish_ledger.py, or next to this file while staged.

Real-files test: copies schedule/posts.json, state/published.json and insights/latest.json into a temp dir and
runs there. It never writes into the repo. Source: $PUBLISH_LEDGER_REAL_REPO, else the repo this file sits in.
It is skipped when those files are absent.
"""
from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import math
import os
import shutil
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
_CANDIDATES = [ROOT / "tools" / "publish_ledger.py", HERE / "publish_ledger.py"]
_PATH = next(p for p in _CANDIDATES if p.exists())
_spec = importlib.util.spec_from_file_location("publish_ledger", _PATH)
pl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pl)

NOW = pl.parse_ms("2026-10-22T16:00:00Z")


def pub(account, media_id, published_at, **extra):
    return {"account": account, "status": "published", "media_id": media_id, "published_at": published_at, "error": None, **extra}


def own(p):
    return {**p, "caption": f"{p['id']}: its own caption"} if p.get("caption") == "x" else p


QUEUE = {"posts": [own(p) for p in [
    {"id": "p1-carousel", "account": "a1", "publish_at": "2026-10-18T17:00:00-04:00", "caption": "Follow the line 👉\nmore", "images": ["p1/01.jpg", "p1/02.jpg"]},
    {"id": "p2-reel-reused", "account": "a1", "publish_at": "2026-10-21T08:30:00-04:00", "caption": "Follow the line 👉\nreel", "video": "reels/p2.mp4", "cover": "reels/p2.jpg"},
    {"id": "p3-never-ran", "account": "a1", "publish_at": "2026-10-22T10:00:00-04:00", "caption": "x", "images": ["p3/01.jpg", "p3/02.jpg"]},
    {"id": "p4-not-yet-due", "account": "a1", "publish_at": "2026-10-22T11:30:00-04:00", "caption": "x", "images": ["p4/01.jpg", "p4/02.jpg"]},
    {"id": "p5-story", "account": "a1", "publish_at": "2026-10-20T12:00:00-04:00", "story": True, "image": "s/p5.jpg"},
    {"id": "p6-late-image", "account": "a1", "publish_at": "2026-10-20T12:00:00-04:00", "caption": "x", "images": ["p6/01.jpg"]},
    {"id": "p7-not-on-platform", "account": "a1", "publish_at": "2026-10-20T09:00:00-04:00", "caption": "x", "images": ["p7/01.jpg", "p7/02.jpg"]},
    {"id": "p8-after-collection", "account": "a1", "publish_at": "2026-10-22T11:00:00-04:00", "caption": "x", "images": ["p8/01.jpg", "p8/02.jpg"]},
    {"id": "p9-dupe", "account": "a1", "publish_at": "2026-11-01T12:00:00-04:00", "caption": "x", "images": ["p9/01.jpg", "p9/02.jpg"]},
    {"id": "p9-dupe", "account": "a1", "publish_at": "2026-11-02T12:00:00-04:00", "caption": "y", "images": ["p9/01.jpg", "p9/02.jpg"]},
    {"id": "p10-old", "account": "a1", "publish_at": "2026-10-10T12:00:00-04:00", "caption": "x", "images": ["p10/01.jpg", "p10/02.jpg"]},
    {"id": "bad-no-time", "account": "a1", "caption": "x"},
]]}
STATE = {"version": 1, "posts": {
    "p1-carousel": pub("a1", "M1", "2026-10-18T21:16:53Z", permalink="https://example.test/p/M1"),
    "p2-reel-reused": pub("a1", "M1", "2026-10-18T21:18:48+0000", recovered=True, permalink="https://example.test/p/M1"),
    "p5-story": pub("a1", "S1", "2026-10-20T16:02:00Z", kind="story"),
    "p6-late-image": pub("a1", "M6", "2026-10-20T19:00:00Z"),
    "p7-not-on-platform": pub("a1", "M7", "2026-10-20T13:05:00Z"),
    "p8-after-collection": pub("a1", "M8", "2026-10-22T15:10:00Z"),
    "p10-old": pub("a1", "M10", "2026-10-10T16:05:00Z"),
    "ghost-renamed": pub("a1", "MG", "2026-10-19T16:00:00Z"),
}}
PLATFORM = {"collected_at": "2026-10-22T15:00:00+00:00", "accounts": {"a1": {"media_count": 4, "posts": [
    {"media_id": "M1", "type": "CAROUSEL_ALBUM", "permalink": "https://example.test/p/M1", "at": "2026-10-18T21:16:53+0000", "first_line": "Follow the line 👉"},
    {"media_id": "M6", "type": "IMAGE", "permalink": "https://example.test/p/M6", "at": "2026-10-20T19:00:00+0000", "first_line": "x"},
    {"media_id": "MG", "type": "IMAGE", "permalink": "https://example.test/p/MG", "at": "2026-10-19T16:00:00+0000", "first_line": "g"},
    {"media_id": "M9", "type": "CAROUSEL_ALBUM", "permalink": "https://example.test/p/M9", "at": "2026-10-15T12:00:00+0000", "first_line": "posted by hand"},
]}}}
T = (json.dumps(QUEUE), json.dumps(STATE), json.dumps(PLATFORM))


def only(r):
    return {c: n for c, n in r["counts"].items() if n}


def keys(r, code):
    return [f["key"] for f in r["findings"] if f["code"] == code]


class PostHoc(unittest.TestCase):
    def test_planted_findings_exactly(self):
        r = pl.run(*T, NOW)
        self.assertEqual(only(r), {"due_not_published": 1, "state_predates_schedule": 1, "state_without_platform_media": 1, "published_not_in_queue": 1,
                                   "platform_media_not_in_state": 1, "duplicate_media_id": 1, "duplicate_queue_id": 1, "late_publish": 1, "type_mismatch": 1, "invalid_entry": 1})
        self.assertEqual(keys(r, "state_predates_schedule"), ["p2-reel-reused"])
        self.assertRegex(next(f["detail"] for f in r["findings"] if f["code"] == "state_predates_schedule"), r"63\.2 h before its own slot \(recovered: true.*also recorded for p1-carousel")
        self.assertEqual(keys(r, "duplicate_media_id"), ["M1"])
        self.assertEqual(keys(r, "type_mismatch"), ["p2-reel-reused"])
        self.assertEqual(keys(r, "due_not_published"), ["p3-never-ran"])
        self.assertEqual(keys(r, "late_publish"), ["p6-late-image"])
        self.assertEqual(r["results"]["checkability"], {"stateChecked": 4, "stateStories": 1, "stateOutsideWindow": 1, "stateAfterCollection": 1})
        self.assertEqual(r["findings"][0]["severity"], "high")

    def test_thresholds_and_edges(self):
        self.assertEqual(keys(pl.run(*T, pl.parse_ms("2026-10-22T16:30:00Z")), "due_not_published"), ["p3-never-ran", "p4-not-yet-due"])
        self.assertEqual(keys(pl.run(*T, NOW, late_min=180), "late_publish"), [])
        self.assertEqual(keys(pl.run(*T, NOW, late_min=10), "late_publish"), ["p1-carousel", "p6-late-image"])
        no_plat = pl.run(T[0], T[1], None, NOW)
        self.assertEqual(no_plat["counts"]["state_predates_schedule"], 1)
        self.assertEqual(no_plat["counts"]["type_mismatch"] + no_plat["counts"]["platform_media_not_in_state"], 0)
        with self.assertRaisesRegex(ValueError, "non-negative"):
            pl.run(*T, NOW, late_min=-1)
        with self.assertRaisesRegex(ValueError, "--now"):
            pl.run(*T, math.nan)

    def test_malformed_inputs(self):
        with self.assertRaisesRegex(ValueError, r"state/published\.json is not valid JSON"):
            pl.run(T[0], "{nope", None, NOW)
        with self.assertRaisesRegex(ValueError, "must be a list"):
            pl.run('{"posts": 3}', T[1], None, NOW)
        with self.assertRaisesRegex(ValueError, "collected_at"):
            pl.run(T[0], T[1], '{"accounts": {}}', NOW)
        pl.run("﻿" + T[0], T[1], None, NOW)  # BOM tolerated

    def test_time_parsing(self):
        self.assertEqual(pl.parse_ms("2026-10-22T16:37:56+0000"), pl.parse_ms("2026-10-22T16:37:56Z"))
        self.assertEqual(pl.parse_ms("2026-10-21T08:30:00-04:00"), pl.parse_ms("2026-10-21T12:30:00Z"))
        self.assertTrue(math.isnan(pl.parse_ms("2026-02-30T00:00:00Z")))
        self.assertEqual(pl.toronto_day(pl.parse_ms("2026-10-25T03:30:00Z")), "2026-10-24")
        self.assertEqual(pl.toronto_day(pl.parse_ms("2026-11-01T05:30:00Z")), "2026-11-01")  # 01:30 EDT/EST fall-back day
        self.assertEqual(pl.jround(2.5), 3)


# ------------------------------------------------------------------ pre-flight
PF_NOW = pl.parse_ms("2026-10-23T05:00:00Z")
LONG = "Can't focus? It's usually one of three things. Pick yours and follow the line 👉\n\n" + "Body text that goes on. " * 20


def pq(i, account, publish_at, **extra):
    return {"id": i, "account": account, "publish_at": publish_at, **extra}


PF_QUEUE = {"posts": [
    pq("old-carousel", "lh", "2026-10-18T17:00:00-04:00", caption=LONG, images=["old/01.jpg", "old/02.jpg"]),
    pq("old-other-acct", "ff", "2026-10-18T12:00:00-04:00", caption="Shared caption across pages", images=["ff/01.jpg"]),
    pq("reel-same-caption", "lh", "2026-10-24T08:30:00-04:00", caption=LONG + "A different ending after character 300.", video="reels/r1.mp4", cover="reels/r1.jpg"),
    pq("twin-a", "hb", "2026-10-24T12:00:00-04:00", caption="Twin   caption\n", images=["hb/a1.jpg", "hb/a2.jpg"]),
    pq("twin-b", "hb", "2026-10-25T12:00:00-04:00", caption="Twin caption", images=["hb/b1.jpg", "hb/a2.jpg"]),
    pq("other-page-same-cap", "lh", "2026-10-24T13:00:00-04:00", caption="Shared caption across pages", images=["lh/x1.jpg"]),
    pq("no-file", "hb", "2026-10-26T12:00:00-04:00", caption="Needs a file", images=["hb/missing.jpg"]),
    pq("st1", "ff", "2026-10-24T09:00:00-04:00", story=True, image="st/1.jpg"),
    pq("st2", "ff", "2026-10-24T09:05:00-04:00", story=True, image="st/1.jpg"),
    pq("ff-1", "ff", "2026-10-24T10:00:00-04:00", caption="ff one", images=["ff/1.jpg"]),
    pq("ff-2", "ff", "2026-10-24T14:00:00-04:00", caption="ff two", images=["ff/2.jpg"]),
    pq("ff-3", "ff", "2026-10-24T23:30:00-04:00", caption="ff three", images=["ff/3.jpg"]),  # Oct 25 in UTC, Oct 24 in Toronto
    pq("ff-4-next-day", "ff", "2026-10-25T00:30:00-04:00", caption="ff four", images=["ff/4.jpg"]),
]}
PF_STATE = {"posts": {"old-carousel": pub("lh", "O1", "2026-10-18T21:01:00Z"), "old-other-acct": pub("ff", "O2", "2026-10-18T16:01:00Z")}}
ALL_MEDIA = ["old/01.jpg", "old/02.jpg", "ff/01.jpg", "reels/r1.mp4", "reels/r1.jpg", "hb/a1.jpg", "hb/a2.jpg", "hb/b1.jpg", "lh/x1.jpg",
             "st/1.jpg", "ff/1.jpg", "ff/2.jpg", "ff/3.jpg", "media/ff/4.jpg"]
PRE = ["missing_media", "duplicate_content_hash", "caption_collision_with_published", "cap_breach"]


def pf(queue=PF_QUEUE, state=PF_STATE, now=PF_NOW, **kw):
    kw.setdefault("media_index", ALL_MEDIA)
    return pl.run(json.dumps(queue), json.dumps(state), None, now, **kw)


class PreFlight(unittest.TestCase):
    def test_each_check_fires_on_its_planted_case(self):
        r = pf()
        got = {c: keys(r, c) for c in PRE}
        self.assertEqual(got["missing_media"], ["no-file"])
        self.assertEqual(sorted(k.split(":")[1] for k in got["duplicate_content_hash"]), ["caption", "media"])
        self.assertIn("hb:media:twin-a,twin-b", got["duplicate_content_hash"])
        self.assertEqual(got["caption_collision_with_published"], ["reel-same-caption"])
        self.assertEqual(got["cap_breach"], ["ff:2026-10-24:feed"])
        self.assertEqual(next(f for f in r["findings"] if f["code"] == "missing_media")["severity"], "high")
        self.assertTrue(all(f["severity"] == "medium" for f in r["findings"] if f["code"] in PRE[1:]))
        self.assertRegex(next(f["detail"] for f in r["findings"] if f["code"] == "cap_breach"), r"3 feed posts slotted on 2026-10-24 \(Toronto\), ceiling 2: ff-1, ff-2, ff-3")
        self.assertEqual(r["totals"]["queue_upcoming"], 11)

    def test_no_false_positives_on_edges(self):
        r = pf()
        self.assertNotIn("other-page-same-cap", keys(r, "caption_collision_with_published"))
        self.assertFalse(any("st1" in f["key"] + f["detail"] or "st2" in f["key"] + f["detail"] for f in r["findings"]), "Stories may reuse a frame")
        later = pf(now=pl.parse_ms("2026-10-26T23:00:00Z"))
        self.assertEqual({c: later["counts"][c] for c in PRE}, {c: 0 for c in PRE}, "nothing upcoming any more")
        self.assertEqual(keys(pf(ceilings={"feed": 3, "reel": 2, "story": 5}), "cap_breach"), [])
        self.assertEqual(sorted(keys(pf(ceilings={"feed": 2, "reel": 2, "story": 1}), "cap_breach")), ["ff:2026-10-24:feed", "ff:2026-10-24:story"])
        no_idx = pl.run(json.dumps(PF_QUEUE), json.dumps(PF_STATE), None, PF_NOW)
        self.assertEqual(no_idx["counts"]["missing_media"], 0)
        self.assertTrue(any("no media index given" in a for a in no_idx["assumptions"]))

    def test_short_captions_collide_only_when_equal_and_cap_counts_published_entries(self):
        q2 = {"posts": PF_QUEUE["posts"] + [pq("short-repeat", "ff", "2026-10-26T10:00:00-04:00", caption="Shared caption across pages", images=["ff/4.jpg"])]}
        self.assertIn("short-repeat", keys(pf(queue=q2), "caption_collision_with_published"))
        q3 = {"posts": PF_QUEUE["posts"] + [pq("ff-pub-same-day", "ff", "2026-10-24T08:00:00-04:00", caption="already out", images=["ff/01.jpg"])]}
        st3 = {"posts": {**PF_STATE["posts"], "ff-pub-same-day": pub("ff", "P3", "2026-10-24T12:00:00Z")}}
        r3 = pf(queue=q3, state=st3, now=pl.parse_ms("2026-10-24T15:00:00Z"))
        self.assertRegex(next(f["detail"] for f in r3["findings"] if f["code"] == "cap_breach"), "4 feed posts")

    def test_oct21_trigger_is_caught_before_the_slot(self):
        """The real incident shape: an upcoming Reel with the same caption as a published carousel."""
        q = {"posts": [pq("lh-1018-follow-the-line", "lockedhour", "2026-10-18T17:00:00-04:00", caption=LONG, images=["a/01.jpg", "a/02.jpg"]),
                       pq("lh-pan-1021am-follow-the-line", "lockedhour", "2026-10-21T08:30:00-04:00", caption=LONG, video="reels/x.mp4", cover="reels/x.jpg")]}
        st = {"posts": {"lh-1018-follow-the-line": pub("lockedhour", "17907130110595501", "2026-10-18T21:16:53Z")}}
        r = pf(queue=q, state=st, now=pl.parse_ms("2026-10-20T12:00:00Z"), media_index=["a/01.jpg", "a/02.jpg", "reels/x.mp4", "reels/x.jpg"])
        self.assertEqual(keys(r, "caption_collision_with_published"), ["lh-pan-1021am-follow-the-line"])
        self.assertEqual(pl.blocking(r), [], "a warning, not a red run")


class AcksAndCli(unittest.TestCase):
    def test_acks_mark_but_never_hide_and_stale_acks_are_listed(self):
        r = pl.run(*T, NOW)
        self.assertGreater(len(pl.blocking(r)), 0)
        acks = pl.load_acks(json.dumps([{"code": f["code"], "key": f["key"], "reason": "reviewed"} for f in pl.blocking(r)] + [{"code": "late_publish", "key": "gone", "reason": "old"}]))
        pl.apply_acks(r, acks)
        self.assertEqual(pl.blocking(r), [])
        self.assertEqual(r["acks"]["stale"], [{"code": "late_publish", "key": "gone"}])
        self.assertTrue(all(f.get("acknowledged") == "reviewed" for f in r["findings"] if f["severity"] == "high"))
        self.assertIn("acknowledged: reviewed", pl.to_markdown(r))
        for bad in ['{"code": "x"}', '[{"code": "nope", "key": "k", "reason": "r"}]', '[{"code": "late_publish", "key": "k", "reason": " "}]']:
            with self.assertRaises(ValueError):
                pl.load_acks(bad)

    def _repo(self, queue, state, platform=None):
        d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, d)
        for rel, obj in (("schedule/posts.json", queue), ("state/published.json", state), ("insights/latest.json", platform)):
            if obj is not None:
                (d / rel).parent.mkdir(parents=True, exist_ok=True)
                (d / rel).write_text(json.dumps(obj), encoding="utf-8")
        return d

    def _main(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            rc = pl.main(list(args))
        return rc, out.getvalue(), err.getvalue()

    def test_cli_exit_codes_summary_and_read_only(self):
        repo = self._repo(QUEUE, STATE, PLATFORM)
        before = sorted((p.relative_to(repo).as_posix(), hashlib.sha256(p.read_bytes()).hexdigest()) for p in repo.rglob("*") if p.is_file())
        out = Path(tempfile.mkdtemp()); self.addCleanup(shutil.rmtree, out)
        summary = out / "summary.md"
        rc, so, _ = self._main("--repo", str(repo), "--now", "2026-10-22T16:00:00Z", "--out", str(out / "r"), "--summary", str(summary))
        self.assertEqual(rc, 1)
        self.assertIn("HIGH state_predates_schedule p2-reel-reused", so)
        self.assertIn("## Publish Ledger", summary.read_text(encoding="utf-8"))
        self.assertTrue((out / "r" / "report.json").exists() and (out / "r" / "report.md").exists())
        clean = self._repo({"posts": [QUEUE["posts"][0]]}, {"posts": {"p1-carousel": STATE["posts"]["p1-carousel"]}}, PLATFORM)
        rc2, _, _ = self._main("--repo", str(clean), "--now", "2026-10-22T16:00:00Z", "--summary", str(summary))
        self.assertEqual(rc2, 0, "low findings (platform media not in state) never fail the run")
        rc3, _, err = self._main("--repo", str(repo), "--now", "2026-10-22T16:00:00Z", "--out", str(repo / "inside"))
        self.assertEqual(rc3, 2); self.assertIn("outside the repo", err)
        self.assertEqual(self._main("--repo", str(repo / "nope"), "--now", "2026-10-22T16:00:00Z")[0], 2)
        self.assertEqual(self._main("--repo", str(repo), "--now", "yesterday")[0], 2)
        after = sorted((p.relative_to(repo).as_posix(), hashlib.sha256(p.read_bytes()).hexdigest()) for p in repo.rglob("*") if p.is_file())
        self.assertEqual(before, after, "the audited repo is unchanged")

    def test_deterministic(self):
        a, b = pl.run(*T, NOW), pl.run(*T, NOW)
        self.assertEqual(json.dumps(a), json.dumps(b))
        self.assertEqual(a["fingerprints"]["report"], pl.report_hash(a))
        self.assertRegex(a["fingerprints"]["inputs"]["schedule/posts.json"], "^[0-9a-f]{64}$")

    def test_no_network_code(self):
        src = _PATH.read_text(encoding="utf-8")
        for bad in ("urllib", "http.client", "requests", "socket", "subprocess"):
            self.assertNotIn(f"import {bad}", src)


REAL = Path(os.environ.get("PUBLISH_LEDGER_REAL_REPO", ROOT))
_REAL_FILES = ["schedule/posts.json", "state/published.json", "insights/latest.json"]


@unittest.skipUnless(all((REAL / f).is_file() for f in _REAL_FILES[:2]), "real Autopost files not present")
class RealFilesCopy(unittest.TestCase):
    def test_runs_on_a_copy_and_leaves_the_originals_untouched(self):
        before = {f: hashlib.sha256((REAL / f).read_bytes()).hexdigest() for f in _REAL_FILES if (REAL / f).is_file()}
        d = Path(tempfile.mkdtemp()); self.addCleanup(shutil.rmtree, d)
        for f in before:
            (d / f).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REAL / f, d / f)
        r = pl.run((d / _REAL_FILES[0]).read_text(encoding="utf-8"), (d / _REAL_FILES[1]).read_text(encoding="utf-8"),
                   (d / _REAL_FILES[2]).read_text(encoding="utf-8") if (d / _REAL_FILES[2]).exists() else None,
                   pl.parse_ms(os.environ.get("PUBLISH_LEDGER_NOW", "2026-10-23T05:15:00Z")))
        self.assertGreater(r["totals"]["queue_posts"], 0)
        self.assertEqual(r["counts"]["invalid_entry"], 0, "every real queue/state entry parses")
        # while the Oct 21 history is in the state file, the incident must still be detected
        if "lh-pan-1021am-follow-the-line" in json.loads((d / _REAL_FILES[1]).read_text(encoding="utf-8"))["posts"]:
            self.assertIn("lh-pan-1021am-follow-the-line", keys(r, "state_predates_schedule"))
        self.assertEqual(before, {f: hashlib.sha256((REAL / f).read_bytes()).hexdigest() for f in before})


if __name__ == "__main__":
    unittest.main()

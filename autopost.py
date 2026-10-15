#!/usr/bin/env python3
"""
Steadfold Autopost: publish scheduled Instagram carousel posts (and their first
comment) for the three Steadfold Instagram professional accounts.

Runs every 15 minutes inside GitHub Actions (see .github/workflows/autopost.yml).
Each run:

  1. Reads schedule/posts.json (what to post, when) and state/published.json
     (what has already been posted).
  2. Picks the posts whose publish_at time has arrived and that are not posted yet.
  3. For each one: verifies the account's token really belongs to the expected
     @username, creates one container per image, creates the carousel container,
     waits until Instagram says it is FINISHED, publishes it, then posts the
     first comment.
  4. Writes progress into state/published.json after every step, so a crash or a
     re-run can never post the same thing twice.

API: Instagram API with Instagram Login (host graph.instagram.com). No Facebook
Page needed. Python 3.11+, standard library + requests only.

Tokens are read from environment variables and are never printed: every line
of output passes through redact().
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable

import requests

# --------------------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent
DEFAULT_POSTS_FILE = ROOT / "schedule" / "posts.json"
DEFAULT_STATE_FILE = ROOT / "state" / "published.json"
DEFAULT_MEDIA_DIR = ROOT / "media"

API_HOST = "https://graph.instagram.com"
# Version used in Meta's Instagram Platform docs examples as of Oct 2026 (v25.0).
# Graph API v26.0 also exists (released 2026-07-29). Override with IG_API_VERSION.
API_VERSION = os.environ.get("IG_API_VERSION", "").strip() or "v25.0"

# The three accounts. The key is what posts.json uses in its "account" field.
ACCOUNTS: dict[str, dict[str, str]] = {
    "fullyfunded": {"username": "fullyfundedhq", "token_env": "IG_TOKEN_FULLYFUNDED"},
    "lockedhour": {"username": "lockedhourhq", "token_env": "IG_TOKEN_LOCKEDHOUR"},
    "hourback": {"username": "hourbackhq", "token_env": "IG_TOKEN_HOURBACK"},
    # Littlefold (parenting page). The handle is set by repo variable IG_USERNAME_LITTLEFOLD
    # once Dharma registers the account; posts for it are only added after that.
    "littlefold": {"username": os.environ.get("IG_USERNAME_LITTLEFOLD", "").strip() or "littlefoldhq",
                   "token_env": "IG_TOKEN_LITTLEFOLD"},
}

LATE_AFTER = timedelta(hours=6)       # older than this: still publish, but log LATE
MAX_CAROUSEL_ITEMS = 10               # Instagram limit
MAX_VIDEO_BYTES = 19_500_000          # jsDelivr serves GitHub files up to 20 MB
CAPTION_MAX_CHARS = 2200              # Instagram caption limit
CAPTION_MAX_HASHTAGS = 30             # Instagram hashtag limit
POLL_INTERVAL_SECONDS = 10            # how often to ask "is the container ready?"
POLL_TIMEOUT_SECONDS = 300            # Meta suggests polling for at most 5 minutes
CONTAINER_MAX_AGE = timedelta(hours=23)  # containers expire after 24h; reuse only if younger
MAX_PUBLISH_ATTEMPTS = 3              # after this many failed runs, stop retrying a post
MAX_COMMENT_ATTEMPTS = 5              # after this many failed runs, stop retrying a comment
MAX_POSTS_PER_ACCOUNT_PER_RUN = 1     # a backlog drains one post per account per run
SAFETY_CAP_PER_24H = 25               # our own cap, far below Meta's 100 posts / 24h
HTTP_TIMEOUT_SECONDS = 60

# --------------------------------------------------------------------------------------
# Output helpers: everything printed goes through redact() so tokens never leak.
# --------------------------------------------------------------------------------------

_SECRETS: set[str] = set()
_TOKEN_IN_TEXT = re.compile(r"(access_token=)[^&\s'\"]+", re.IGNORECASE)
_BEARER_IN_TEXT = re.compile(r"(Bearer\s+)[A-Za-z0-9._\-]+", re.IGNORECASE)


def register_secret(value: str | None) -> None:
    """Remember a secret so it is scrubbed from any later output."""
    if value and len(value) >= 6:
        _SECRETS.add(value)


def redact(text: Any) -> str:
    s = str(text)
    for secret in sorted(_SECRETS, key=len, reverse=True):
        s = s.replace(secret, "***")
    s = _TOKEN_IN_TEXT.sub(r"\1***", s)
    s = _BEARER_IN_TEXT.sub(r"\1***", s)
    return s


def log(msg: str = "") -> None:
    print(redact(msg), flush=True)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_time(value: str) -> datetime:
    """Parse an ISO time that MUST carry an offset (e.g. 2026-10-15T12:00:00-04:00)."""
    v = value.strip()
    if v.endswith("Z"):
        v = v[:-1] + "+00:00"
    dt = datetime.fromisoformat(v)
    if dt.tzinfo is None:
        raise ValueError(f"time {value!r} has no UTC offset (expected e.g. -04:00)")
    return dt


# --------------------------------------------------------------------------------------
# Errors
# --------------------------------------------------------------------------------------

class IGError(Exception):
    """An error from the Instagram API (or the network on the way to it)."""

    def __init__(self, message: str, *, http_status: int | None = None,
                 code: int | None = None, subcode: int | None = None,
                 network: bool = False):
        super().__init__(redact(message))
        self.http_status = http_status
        self.code = code
        self.subcode = subcode
        self.network = network  # True = we don't know whether the request went through


class DoNotRetry(IGError):
    """A problem that needs a human; retrying automatically could double-post."""


class AccountError(Exception):
    """The account can't be used this run (missing token, wrong username, ...)."""


class StillProcessing(Exception):
    """Container not FINISHED within the polling window; try again next run."""


# --------------------------------------------------------------------------------------
# Instagram API client
# --------------------------------------------------------------------------------------

class IGClient:
    """Tiny wrapper over graph.instagram.com for one account's token."""

    def __init__(self, token: str, session: Any = None, version: str = API_VERSION,
                 sleep: Callable[[float], None] = time.sleep,
                 poll_interval: float = POLL_INTERVAL_SECONDS,
                 poll_timeout: float = POLL_TIMEOUT_SECONDS):
        register_secret(token)
        self._token = token
        self.session = session or requests.Session()
        self.version = version
        self.sleep = sleep
        self.poll_interval = poll_interval
        self.poll_timeout = poll_timeout

    # -- low level ---------------------------------------------------------------------
    def _url(self, path: str) -> str:
        return f"{API_HOST}/{self.version}/{path.lstrip('/')}"

    def _request(self, method: str, path: str, params: dict | None = None,
                 data: dict | None = None) -> dict:
        params = dict(params or {})
        data = dict(data or {})
        if method == "GET":
            params["access_token"] = self._token
        else:
            # For POSTs the token goes in the form body, never in the URL.
            data["access_token"] = self._token
        try:
            resp = self.session.request(method, self._url(path), params=params or None,
                                        data=data or None, timeout=HTTP_TIMEOUT_SECONDS)
        except requests.RequestException as exc:  # network trouble: outcome unknown
            raise IGError(f"{method} {path}: network error: {exc}", network=True) from None
        return self._handle(method, path, resp)

    @staticmethod
    def _handle(method: str, path: str, resp: Any) -> dict:
        try:
            body = resp.json()
        except ValueError:
            body = None
        if resp.status_code >= 400 or (isinstance(body, dict) and "error" in body):
            err = (body or {}).get("error", {}) if isinstance(body, dict) else {}
            msg = err.get("error_user_msg") or err.get("message") or (resp.text or "")[:300]
            raise IGError(
                f"{method} {path}: HTTP {resp.status_code}: {msg} "
                f"(code={err.get('code')}, subcode={err.get('error_subcode')}, "
                f"fbtrace_id={err.get('fbtrace_id')})",
                http_status=resp.status_code, code=err.get("code"),
                subcode=err.get("error_subcode"),
                # 5xx: the server may or may not have acted on it.
                network=resp.status_code >= 500,
            )
        if not isinstance(body, dict):
            raise IGError(f"{method} {path}: unexpected non-JSON response "
                          f"(HTTP {resp.status_code})", http_status=resp.status_code)
        return body

    # -- endpoints ---------------------------------------------------------------------
    def me(self) -> dict:
        """GET /me?fields=user_id,username -> {"user_id": ..., "username": ...}."""
        body = self._request("GET", "me", params={"fields": "user_id,username"})
        # The docs show a {"data": [{...}]} wrapper in one example; real responses
        # are usually flat. Accept both.
        if isinstance(body.get("data"), list) and body["data"]:
            body = body["data"][0]
        if not body.get("user_id") or not body.get("username"):
            raise IGError("GET me: response did not include user_id and username")
        return {"user_id": str(body["user_id"]), "username": str(body["username"])}

    def create_carousel_item(self, ig_user_id: str, image_url: str,
                             alt_text: str | None = None) -> str:
        data = {"image_url": image_url, "is_carousel_item": "true"}
        if alt_text:
            data["alt_text"] = alt_text
        return str(self._request("POST", f"{ig_user_id}/media", data=data)["id"])

    def create_carousel(self, ig_user_id: str, children: list[str], caption: str) -> str:
        data = {"media_type": "CAROUSEL", "children": ",".join(children), "caption": caption}
        return str(self._request("POST", f"{ig_user_id}/media", data=data)["id"])

    def create_single_image(self, ig_user_id: str, image_url: str, caption: str,
                            alt_text: str | None = None) -> str:
        data = {"image_url": image_url, "caption": caption}
        if alt_text:
            data["alt_text"] = alt_text
        return str(self._request("POST", f"{ig_user_id}/media", data=data)["id"])

    def create_reel(self, ig_user_id: str, video_url: str, caption: str,
                    cover_url: str | None = None, thumb_offset_ms: int | None = None) -> str:
        data = {"media_type": "REELS", "video_url": video_url, "caption": caption,
                "share_to_feed": "true"}
        if cover_url:
            data["cover_url"] = cover_url
        elif thumb_offset_ms is not None:
            data["thumb_offset"] = str(int(thumb_offset_ms))
        return str(self._request("POST", f"{ig_user_id}/media", data=data)["id"])

    def container_status(self, container_id: str) -> tuple[str, str]:
        body = self._request("GET", container_id, params={"fields": "status_code,status"})
        return str(body.get("status_code", "")), str(body.get("status", ""))

    def wait_until_finished(self, container_id: str) -> None:
        """Poll status_code until FINISHED. Raises IGError on ERROR/EXPIRED,
        StillProcessing if it is still IN_PROGRESS when the time is up."""
        waited = 0.0
        while True:
            code, detail = self.container_status(container_id)
            if code == "FINISHED":
                return
            if code in ("ERROR", "EXPIRED"):
                raise IGError(f"container {container_id} status {code}: {detail}")
            if code == "PUBLISHED":
                raise IGError(f"container {container_id} is already PUBLISHED")
            if waited >= self.poll_timeout:
                raise StillProcessing(
                    f"container {container_id} still {code or 'unknown'} after "
                    f"{int(waited)}s; will check again next run")
            self.sleep(self.poll_interval)
            waited += self.poll_interval

    def publish(self, ig_user_id: str, creation_id: str) -> str:
        body = self._request("POST", f"{ig_user_id}/media_publish",
                             data={"creation_id": creation_id})
        return str(body["id"])

    def media_info(self, media_id: str) -> dict:
        return self._request("GET", media_id, params={"fields": "id,permalink,timestamp"})

    def recent_media(self, ig_user_id: str, limit: int = 25) -> list[dict]:
        body = self._request("GET", f"{ig_user_id}/media",
                             params={"fields": "id,caption,permalink,timestamp",
                                     "limit": str(limit)})
        return list(body.get("data", []))

    def comment(self, media_id: str, message: str) -> str:
        return str(self._request("POST", f"{media_id}/comments",
                                 data={"message": message})["id"])

    def list_comments(self, media_id: str) -> list[dict]:
        body = self._request("GET", f"{media_id}/comments",
                             params={"fields": "id,text,username", "limit": "50"})
        return list(body.get("data", []))


# --------------------------------------------------------------------------------------
# State file (state/published.json). Written atomically after every step.
# --------------------------------------------------------------------------------------

class State:
    def __init__(self, path: Path, read_only: bool = False):
        self.path = path
        self.read_only = read_only
        if path.exists() and path.read_text(encoding="utf-8").strip():
            self.data = json.loads(path.read_text(encoding="utf-8"))
        else:
            self.data = {}
        self.data.setdefault("version", 1)
        self.data.setdefault("posts", {})

    def get(self, post_id: str) -> dict:
        return dict(self.data["posts"].get(post_id, {}))

    def update(self, post_id: str, **fields: Any) -> dict:
        entry = self.data["posts"].setdefault(post_id, {})
        entry.update(fields)
        entry["updated_at"] = iso(utcnow())
        self.save()
        return dict(entry)

    def save(self) -> None:
        if self.read_only:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        text = json.dumps(self.data, indent=2, ensure_ascii=False, sort_keys=False) + "\n"
        fd, tmp = tempfile.mkstemp(dir=str(self.path.parent), prefix=".published.", suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, self.path)

    def published_last_24h(self, account: str, now: datetime) -> int:
        n = 0
        for entry in self.data["posts"].values():
            if entry.get("account") == account and entry.get("published_at"):
                try:
                    if now - parse_time(entry["published_at"]) < timedelta(hours=24):
                        n += 1
                except ValueError:
                    pass
        return n


# --------------------------------------------------------------------------------------
# Schedule loading and validation
# --------------------------------------------------------------------------------------

def load_posts(path: Path) -> list[dict]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    posts = raw["posts"] if isinstance(raw, dict) else raw
    if not isinstance(posts, list):
        raise ValueError("posts.json must be a list of posts or {\"posts\": [...]}")
    return posts


def validate_post(post: dict, media_dir: Path | None) -> list[str]:
    """Return a list of problems with one post (empty list = OK)."""
    problems: list[str] = []
    required = ("id", "account", "publish_at", "caption") + (() if post.get("video") else ("images",))
    for field in required:
        if not post.get(field):
            problems.append(f"missing '{field}'")
    if problems:
        return problems
    if post["account"] not in ACCOUNTS:
        problems.append(f"unknown account {post['account']!r} "
                        f"(expected one of {', '.join(ACCOUNTS)})")
    try:
        parse_time(post["publish_at"])
    except ValueError as exc:
        problems.append(f"bad publish_at: {exc}")
    caption = post["caption"]
    if len(caption) > CAPTION_MAX_CHARS:
        problems.append(f"caption is {len(caption)} characters (max {CAPTION_MAX_CHARS})")
    if len(re.findall(r"(?<!\w)#\w", caption)) > CAPTION_MAX_HASHTAGS:
        problems.append(f"caption has more than {CAPTION_MAX_HASHTAGS} hashtags")
    if post.get("video"):
        video = str(post["video"])
        if not video.lower().endswith(".mp4"):
            problems.append(f"video {video} is not an .mp4")
        elif media_dir is not None:
            vp = media_dir / video
            if not vp.is_file():
                problems.append(f"video file media/{video} is missing from the repo")
            elif vp.stat().st_size > MAX_VIDEO_BYTES:
                problems.append(f"video media/{video} is over {MAX_VIDEO_BYTES // 1_000_000} MB")
        cover = post.get("cover")
        if cover:
            if not str(cover).lower().endswith((".jpg", ".jpeg")):
                problems.append(f"cover {cover} is not a .jpg")
            elif media_dir is not None and not (media_dir / cover).is_file():
                problems.append(f"cover file media/{cover} is missing from the repo")
        return problems
    images = post["images"]
    if not isinstance(images, list) or not (1 <= len(images) <= MAX_CAROUSEL_ITEMS):
        problems.append(f"images must be a list of 1 to {MAX_CAROUSEL_ITEMS} files")
    else:
        for rel in images:
            if not str(rel).lower().endswith((".jpg", ".jpeg")):
                problems.append(f"image {rel} is not a .jpg (Instagram only accepts JPEG)")
            elif media_dir is not None and not (media_dir / rel).is_file():
                problems.append(f"image file media/{rel} is missing from the repo")
    return problems


def media_base_url(env: dict) -> str | None:
    base = (env.get("MEDIA_BASE_URL") or "").strip()
    if base:
        return base.rstrip("/")
    repo = (env.get("GITHUB_REPOSITORY") or "").strip()
    if repo:
        branch = (env.get("MEDIA_BRANCH") or "").strip() or "main"
        return f"https://raw.githubusercontent.com/{repo}/{branch}/media"
    return None


def video_base_url(env: dict) -> str | None:
    """Videos are served through jsDelivr (correct video/mp4 type, pinned to the commit),
    because Instagram's video fetch is pickier than its image fetch."""
    base = (env.get("VIDEO_BASE_URL") or "").strip()
    if base:
        return base.rstrip("/")
    repo = (env.get("GITHUB_REPOSITORY") or "").strip()
    if repo:
        ref = (env.get("GITHUB_SHA") or "").strip() or (env.get("MEDIA_BRANCH") or "").strip() or "main"
        return f"https://cdn.jsdelivr.net/gh/{repo}@{ref}/media"
    return media_base_url(env)


def normalize_caption(text: str | None) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip()


# --------------------------------------------------------------------------------------
# The runner
# --------------------------------------------------------------------------------------

class Runner:
    def __init__(self, posts: list[dict], state: State, *, env: dict, now: datetime,
                 session: Any = None, dry_run: bool = False, retry_failed: bool = False,
                 media_dir: Path | None = DEFAULT_MEDIA_DIR,
                 sleep: Callable[[float], None] = time.sleep,
                 poll_interval: float = POLL_INTERVAL_SECONDS,
                 poll_timeout: float = POLL_TIMEOUT_SECONDS):
        self.posts = posts
        self.state = state
        self.env = env
        self.now = now
        self.session = session or requests.Session()
        self.dry_run = dry_run
        self.retry_failed = retry_failed
        self.media_dir = media_dir
        self.sleep = sleep
        self.poll_interval = poll_interval
        self.poll_timeout = poll_timeout
        self.base_url = media_base_url(env)
        self.video_url = video_base_url(env)
        self.errors: list[str] = []
        self.notes: list[str] = []
        self._clients: dict[str, tuple[IGClient, str] | AccountError] = {}
        self._recent: dict[str, list[dict]] = {}
        self._published_this_run: dict[str, int] = {}
        for acct in ACCOUNTS.values():
            register_secret(env.get(acct["token_env"]))

    # -- accounts ------------------------------------------------------------------------
    def account(self, key: str) -> tuple[IGClient, str]:
        """Return (client, ig_user_id) after checking the token's username.
        Raises AccountError if the token is missing or belongs to someone else."""
        cached = self._clients.get(key)
        if isinstance(cached, AccountError):
            raise cached
        if cached:
            return cached
        info = ACCOUNTS[key]
        token = (self.env.get(info["token_env"]) or "").strip()
        try:
            if not token:
                raise AccountError(f"secret {info['token_env']} is not set, so "
                                   f"@{info['username']} can't post")
            client = IGClient(token, self.session, sleep=self.sleep,
                              poll_interval=self.poll_interval,
                              poll_timeout=self.poll_timeout)
            try:
                me = client.me()
            except IGError as exc:
                raise AccountError(f"could not check the {info['token_env']} token "
                                   f"(expired or revoked?): {exc}") from None
            if me["username"].lower() != info["username"].lower():
                raise AccountError(
                    f"{info['token_env']} belongs to @{me['username']}, but this account "
                    f"must be @{info['username']}. Refusing to post with it.")
            log(f"  token OK: {info['token_env']} -> @{me['username']} "
                f"(user id {me['user_id']})")
            self._clients[key] = (client, me["user_id"])
            return self._clients[key]
        except AccountError as exc:
            self._clients[key] = exc
            raise

    def find_existing(self, client: IGClient, ig_user_id: str, post: dict) -> dict | None:
        """Look for the post among the account's latest media (matched on caption).
        This protects against double-posting if our state was lost."""
        if ig_user_id not in self._recent:
            self._recent[ig_user_id] = client.recent_media(ig_user_id)
        want = normalize_caption(post["caption"])
        for m in self._recent[ig_user_id]:
            have = normalize_caption(m.get("caption"))
            if have and (have == want or (len(want) > 80 and have[:300] == want[:300])):
                return m
        return None

    # -- main loop -----------------------------------------------------------------------
    def run(self) -> int:
        mode = "DRY RUN (nothing will be posted or saved)" if self.dry_run else "LIVE"
        log(f"Steadfold Autopost - {mode} - now {iso(self.now)} - API {API_VERSION}")
        if not self.base_url:
            msg = ("MEDIA_BASE_URL is not set and GITHUB_REPOSITORY is unknown, so image "
                   "URLs can't be built")
            if self.dry_run:
                self.base_url = "https://raw.githubusercontent.com/<owner>/<repo>/main/media"
                log(f"note: {msg}; showing placeholder URLs")
            else:
                log(f"ERROR: {msg}")
                return 2
        log(f"Images are served from {self.base_url}/...")

        valid: list[tuple[datetime, dict]] = []
        seen: set[str] = set()
        for post in self.posts:
            pid = str(post.get("id") or "<no id>")
            problems = validate_post(post, self.media_dir)
            if pid in seen:
                problems.append("duplicate id in posts.json")
            seen.add(pid)
            if problems:
                self.error(f"[{pid}] invalid post, skipped: " + "; ".join(problems))
                continue
            valid.append((parse_time(post["publish_at"]), post))
        valid.sort(key=lambda t: (t[0], t[1]["id"]))

        due = [(t, p) for t, p in valid if t <= self.now]
        upcoming = [(t, p) for t, p in valid if t > self.now]
        log(f"{len(valid)} scheduled post(s): {len(due)} due, {len(upcoming)} upcoming")

        for when, post in due:
            self.handle(post, when)

        if upcoming:
            log("")
            log("Next up:")
            for when, post in upcoming[:6]:
                log(f"  {post['publish_at']}  @{ACCOUNTS[post['account']]['username']:<14} "
                    f"{post['id']}")

        log("")
        for n in self.notes:
            log(f"NOTE: {n}")
        if self.errors:
            log(f"FINISHED WITH {len(self.errors)} PROBLEM(S):")
            for e in self.errors:
                log(f"  - {e}")
            return 1
        log("Finished OK.")
        return 0

    def error(self, msg: str) -> None:
        self.errors.append(msg)
        log(f"ERROR: {msg}")

    def handle(self, post: dict, when: datetime) -> None:
        pid, acct = post["id"], post["account"]
        st = self.state.get(pid)
        status = st.get("status")

        if status == "published":
            needs_comment = (post.get("first_comment") and
                             st.get("comment_status") in ("pending", "failed"))
            if not needs_comment:
                return  # done; nothing to do (the normal case on every later run)
            if st.get("comment_attempts", 0) >= MAX_COMMENT_ATTEMPTS:
                return  # gave up; reported when it happened
            self.retry_comment(post, st)
            return

        if status == "failed" and st.get("attempts", 0) >= MAX_PUBLISH_ATTEMPTS:
            if not self.retry_failed:
                self.notes.append(f"[{pid}] gave up after {st.get('attempts')} failed "
                                  f"attempts (last error: {st.get('error')}). Run the "
                                  f"workflow by hand with 'retry failed' to try again.")
                return

        late = self.now - when > LATE_AFTER
        log("")
        log(f"[{pid}] @{ACCOUNTS[acct]['username']} due {post['publish_at']}"
            + (f"  LATE by {(self.now - when).total_seconds() / 3600:.1f}h - publishing "
               f"anyway" if late else ""))

        if self._published_this_run.get(acct, 0) >= MAX_POSTS_PER_ACCOUNT_PER_RUN:
            log(f"  waiting: already published {MAX_POSTS_PER_ACCOUNT_PER_RUN} post(s) "
                f"for this account in this run; it goes out next run")
            return

        if self.dry_run:
            self.describe(post, st, late)
            return

        if self.state.published_last_24h(acct, self.now) >= SAFETY_CAP_PER_24H:
            self.error(f"[{pid}] safety cap: {SAFETY_CAP_PER_24H} posts in the last 24h "
                       f"for this account; not posting")
            return

        try:
            client, ig_user_id = self.account(acct)
        except AccountError as exc:
            self.error(f"[{pid}] {exc}")
            return

        try:
            self.publish(post, st, client, ig_user_id, late)
        except StillProcessing as exc:
            log(f"  {exc}")
            self.notes.append(f"[{pid}] Instagram is still processing it; next run "
                              f"continues with the same container")
        except IGError as exc:
            attempts = st.get("attempts", 0) + 1
            if self.retry_failed and status == "failed":
                attempts = 1
            if isinstance(exc, DoNotRetry):
                attempts = max(attempts, MAX_PUBLISH_ATTEMPTS)
            self.state.update(pid, account=acct, status="failed", error=str(exc),
                              attempts=attempts, failed_at=iso(self.now))
            more = ("will retry next run" if attempts < MAX_PUBLISH_ATTEMPTS
                    else "giving up (use 'retry failed' to try again)")
            self.error(f"[{pid}] publish failed (attempt {attempts}, {more}): {exc}")

    # -- dry run -------------------------------------------------------------------------
    def describe(self, post: dict, st: dict, late: bool) -> None:
        acct = post["account"]
        info = ACCOUNTS[acct]
        token = (self.env.get(info["token_env"]) or "").strip()
        if token:
            try:
                self.account(acct)
            except AccountError as exc:
                self.error(f"[{post['id']}] {exc}")
        else:
            log(f"  (no {info['token_env']} here, so the token check is skipped)")
        if post.get("video"):
            log(f"  WOULD publish a REEL{' (late)' if late else ''}:")
            log(f"    {self.video_url}/{post['video']}")
            if post.get("cover"):
                log(f"    cover {self.base_url}/{post['cover']}")
        else:
            n = len(post["images"])
            kind = "CAROUSEL" if n > 1 else "single IMAGE"
            log(f"  WOULD publish a {kind} of {n} image(s){' (late)' if late else ''}:")
            for rel in post["images"]:
                log(f"    {self.base_url}/{rel}")
        first_line = post["caption"].splitlines()[0]
        log(f"  caption ({len(post['caption'])} chars): {first_line[:90]}")
        if post.get("alt_text"):
            log(f"  alt text on image 1: {len(post['alt_text'])} chars")
        if post.get("first_comment"):
            log(f"  WOULD comment: {post['first_comment'][:90]}")
        if st:
            log(f"  current state: {st.get('status')}")
        self._published_this_run[acct] = self._published_this_run.get(acct, 0) + 1

    # -- publishing ----------------------------------------------------------------------
    def check_image_urls(self, urls: list[str]) -> None:
        """Make sure every image URL is publicly reachable before Meta tries."""
        for url in urls:
            try:
                r = self.session.request("HEAD", url, timeout=30, allow_redirects=True)
            except requests.RequestException as exc:
                raise IGError(f"image URL check failed for {url}: {exc}") from None
            if r.status_code != 200:
                raise IGError(
                    f"image {url} returned HTTP {r.status_code}. Is the repo public and "
                    f"the file pushed? (Instagram must be able to download it)")

    def publish(self, post: dict, st: dict, client: IGClient, ig_user_id: str,
                late: bool) -> None:
        pid, acct = post["id"], post["account"]
        is_reel = bool(post.get("video"))
        if is_reel:
            urls = [f"{self.video_url}/{post['video']}"]
            cover_url = f"{self.base_url}/{post['cover']}" if post.get("cover") else None
            if cover_url:
                urls.append(cover_url)
        else:
            urls = [f"{self.base_url}/{rel}" for rel in post["images"]]

        # 1) Already on Instagram? (state lost, or an earlier run died mid-publish)
        try:
            existing = self.find_existing(client, ig_user_id, post)
        except IGError as exc:
            if st.get("publish_called") or st.get("container_id"):
                raise  # an earlier attempt may have gone live: don't guess, retry later
            log(f"  warning: couldn't list recent posts for the double-post check ({exc}); "
                f"this post was never attempted before, so continuing")
            existing = None
        if existing:
            ours = bool(st.get("publish_called"))
            self.state.update(
                pid, account=acct, status="published", media_id=str(existing["id"]),
                permalink=existing.get("permalink"), published_at=existing.get("timestamp")
                or iso(self.now), recovered=True, error=None,
                comment_status=("pending" if post.get("first_comment") and ours
                                else ("skipped" if post.get("first_comment") else "none")))
            if ours:
                log(f"  already live (found {existing.get('permalink')}); recorded it, "
                    f"not posting again")
                if post.get("first_comment"):
                    self.retry_comment(post, self.state.get(pid))
            else:
                log(f"  already on Instagram but not posted by this tool "
                    f"({existing.get('permalink')}); recorded it, skipping the first "
                    f"comment in case it was added by hand")
                self.notes.append(f"[{pid}] found already live on Instagram; not "
                                  f"posted again")
            return

        if is_reel:
            # Video host: jsDelivr first; if it can't serve the file, fall back to raw GitHub.
            try:
                self.check_image_urls(urls[:1])
            except IGError as exc:
                raw = f"{self.base_url}/{post['video']}"
                log(f"  video host check failed ({exc}); trying {raw}")
                urls[0] = raw
                self.check_image_urls(urls[:1])
            self.check_image_urls(urls[1:])
        else:
            self.check_image_urls(urls)

        # 2) Reuse a container from an earlier run if it is still fresh and usable.
        container_id = st.get("container_id")
        if container_id:
            created = st.get("container_created_at")
            fresh = created and self.now - parse_time(created) < CONTAINER_MAX_AGE
            code = ""
            if fresh:
                code, _ = client.container_status(container_id)
            if code == "PUBLISHED":
                raise DoNotRetry(
                    f"container {container_id} says PUBLISHED but the post wasn't found "
                    f"among the account's latest posts. Not posting again; please check "
                    f"Instagram and record it in state/published.json by hand")
            if code in ("FINISHED", "IN_PROGRESS"):
                log(f"  reusing container {container_id} ({code})")
            else:
                log(f"  old container {container_id} is {code or 'too old'}; rebuilding")
                container_id = None

        # 3) Build containers: one per image, then the carousel.
        if not container_id:
            alt = (post.get("alt_text") or "").strip() or None
            if is_reel:
                container_id = client.create_reel(
                    ig_user_id, urls[0], post["caption"], cover_url=cover_url,
                    thumb_offset_ms=post.get("thumb_offset_ms"))
                children = []
            elif len(urls) == 1:
                container_id = self._with_alt_fallback(
                    lambda a: client.create_single_image(ig_user_id, urls[0],
                                                         post["caption"], a), alt, pid)
                children: list[str] = []
            else:
                children = []
                for i, url in enumerate(urls):
                    if i == 0:  # alt text describes the whole carousel; put it on slide 1
                        cid = self._with_alt_fallback(
                            lambda a, u=url: client.create_carousel_item(ig_user_id, u, a),
                            alt, pid)
                    else:
                        cid = client.create_carousel_item(ig_user_id, url)
                    children.append(cid)
                    self.state.update(pid, account=acct, status="publishing",
                                      children=list(children))
                log(f"  created {len(children)} image containers")
                container_id = client.create_carousel(ig_user_id, children, post["caption"])
            self.state.update(pid, account=acct, status="publishing", children=children,
                              container_id=container_id,
                              container_created_at=iso(self.now), publish_called=False)
            log(f"  created {'reel' if is_reel else ('carousel' if children else 'image')} "
                f"container {container_id}")

        # 4) Wait until Instagram has processed it.
        client.wait_until_finished(container_id)
        log("  container FINISHED")

        # 5) Publish. Record that we're about to, so a crash can be recovered safely.
        self.state.update(pid, publish_called=True, publish_called_at=iso(self.now))
        media_id = client.publish(ig_user_id, container_id)
        self._published_this_run[acct] = self._published_this_run.get(acct, 0) + 1
        self.state.update(pid, status="published", media_id=media_id,
                          published_at=iso(self.now), late=late, error=None,
                          comment_status="pending" if post.get("first_comment") else "none",
                          comment_attempts=0)
        try:
            info = client.media_info(media_id)
            self.state.update(pid, permalink=info.get("permalink"))
            log(f"  PUBLISHED media {media_id} {info.get('permalink') or ''}")
        except IGError as exc:  # cosmetic only; the post is live
            log(f"  PUBLISHED media {media_id} (couldn't fetch permalink: {exc})")

        # 6) First comment.
        if post.get("first_comment"):
            self.post_comment(post, client, media_id, attempts_so_far=0)

    def _with_alt_fallback(self, make: Callable[[str | None], str], alt: str | None,
                           pid: str) -> str:
        """Create a container with alt text; if Meta rejects it, retry once without."""
        if not alt:
            return make(None)
        try:
            return make(alt)
        except IGError as exc:
            if exc.network or exc.http_status is None or exc.http_status >= 500:
                raise
            log(f"  alt text was rejected ({exc}); retrying this image without alt text")
            self.notes.append(f"[{pid}] alt text rejected by Instagram; posted without it")
            return make(None)

    def post_comment(self, post: dict, client: IGClient, media_id: str,
                     attempts_so_far: int) -> None:
        pid = post["id"]
        try:
            comment_id = client.comment(media_id, post["first_comment"])
        except IGError as exc:
            attempts = attempts_so_far + 1
            self.state.update(pid, comment_status="failed", comment_attempts=attempts,
                              comment_error=str(exc))
            self.error(f"[{pid}] post is LIVE but the first comment failed (attempt "
                       f"{attempts}/{MAX_COMMENT_ATTEMPTS}; only the comment is retried, "
                       f"never the post): {exc}")
            return
        self.state.update(pid, comment_status="done", comment_id=comment_id,
                          comment_error=None, commented_at=iso(self.now))
        log(f"  first comment posted ({comment_id})")

    def retry_comment(self, post: dict, st: dict) -> None:
        pid = post["id"]
        log("")
        log(f"[{pid}] retrying the first comment (the post itself is already live)")
        if self.dry_run:
            log(f"  WOULD comment: {post['first_comment'][:90]}")
            return
        try:
            client, _ = self.account(post["account"])
        except AccountError as exc:
            self.error(f"[{pid}] {exc}")
            return
        media_id = st["media_id"]
        # If an earlier attempt actually went through, don't comment twice.
        try:
            for c in client.list_comments(media_id):
                if normalize_caption(c.get("text")) == normalize_caption(post["first_comment"]):
                    self.state.update(pid, comment_status="done", comment_id=str(c.get("id")),
                                      comment_error=None)
                    log("  the comment is already there; marked done")
                    return
        except IGError as exc:
            log(f"  (couldn't list comments: {exc}; trying to comment anyway)")
        self.post_comment(post, client, media_id,
                          attempts_so_far=int(st.get("comment_attempts", 0)))


# --------------------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------------------

def main(argv: list[str] | None = None, *, session: Any = None, env: dict | None = None,
         now: datetime | None = None, sleep: Callable[[float], None] = time.sleep,
         poll_interval: float = POLL_INTERVAL_SECONDS,
         poll_timeout: float = POLL_TIMEOUT_SECONDS) -> int:
    ap = argparse.ArgumentParser(description="Publish due Instagram posts from schedule/posts.json")
    ap.add_argument("--dry-run", action="store_true",
                    help="show what would happen; make no POST requests and save nothing")
    ap.add_argument("--retry-failed", action="store_true",
                    help="try again posts that already failed the maximum number of times")
    ap.add_argument("--now", help="pretend it is this time (ISO with offset). Dry runs only.")
    ap.add_argument("--posts", type=Path, default=DEFAULT_POSTS_FILE)
    ap.add_argument("--state", type=Path, default=DEFAULT_STATE_FILE)
    ap.add_argument("--media-dir", type=Path, default=DEFAULT_MEDIA_DIR)
    args = ap.parse_args(argv)

    env = dict(os.environ if env is None else env)
    if args.now:
        if not args.dry_run:
            log("ERROR: --now is only allowed together with --dry-run")
            return 2
        now = parse_time(args.now)
    now = now or utcnow()

    try:
        posts = load_posts(args.posts)
    except (OSError, ValueError, KeyError) as exc:
        log(f"ERROR: can't read {args.posts}: {exc}")
        return 2
    try:
        state = State(args.state, read_only=args.dry_run)
    except (OSError, ValueError) as exc:
        log(f"ERROR: can't read {args.state}: {exc}")
        return 2

    runner = Runner(posts, state, env=env, now=now, session=session, dry_run=args.dry_run,
                    retry_failed=args.retry_failed, media_dir=args.media_dir, sleep=sleep,
                    poll_interval=poll_interval, poll_timeout=poll_timeout)
    try:
        return runner.run()
    except Exception as exc:  # last-resort guard: never dump a traceback with secrets
        log(f"ERROR: unexpected {type(exc).__name__}: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

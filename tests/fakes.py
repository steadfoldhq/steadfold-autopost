"""A fake Instagram Graph API + GitHub API, used by the tests instead of the network."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlparse


@dataclass
class Call:
    method: str
    url: str
    params: dict
    data: dict
    json: Any = None
    headers: dict = field(default_factory=dict)

    @property
    def path(self) -> str:
        """URL path without the /vNN.N prefix, e.g. '17841400000000001/media'."""
        p = urlparse(self.url).path.lstrip("/")
        return re.sub(r"^v\d+\.\d+/", "", p)


class FakeResponse:
    def __init__(self, status: int, body: Any = None):
        self.status_code = status
        self._body = body
        self.text = json.dumps(body) if body is not None else ""

    def json(self) -> Any:
        if self._body is None:
            raise ValueError("no JSON")
        return self._body


def ig_error(message: str, code: int = 100, status: int = 400) -> FakeResponse:
    return FakeResponse(status, {"error": {"message": message, "type": "OAuthException",
                                           "code": code, "fbtrace_id": "TRACE"}})


class FakeGraph:
    """Simulates graph.instagram.com for a few accounts.

    tokens: token -> (user_id, username)
    """

    def __init__(self, tokens: dict[str, tuple[str, str]]):
        self.stories: dict[str, list[str]] = {}
        self.reject_trial = False
        self.tokens = tokens
        self.calls: list[Call] = []
        self._n = 1000
        self.containers: dict[str, dict] = {}
        self.media: dict[str, list[dict]] = {}       # user_id -> published media
        self.comments: dict[str, list[dict]] = {}    # media_id -> comments
        self.status_script: list[str] = []           # statuses returned for the carousel
        self.fail_comment = 0                        # number of comment POSTs to fail
        self.fail_publish = 0
        self.reject_alt_text = False
        self.head_status = 200
        self.head_fail_hosts: set[str] = set()       # HEAD returns 404 for these hosts
        self.video_item_script: list[str] = []       # statuses returned for VIDEO carousel items
        self.video_never_finishes = False            # VIDEO carousel items stay IN_PROGRESS
        self.refresh_map: dict[str, str] = {}        # old token -> new token

    # requests.Session-compatible entry point
    def request(self, method: str, url: str, params: dict | None = None,
                data: dict | None = None, json: Any = None, headers: dict | None = None,
                timeout: Any = None, allow_redirects: bool = True) -> FakeResponse:
        call = Call(method, url, dict(params or {}), dict(data or {}), json, dict(headers or {}))
        self.calls.append(call)
        host = urlparse(url).netloc
        if method == "HEAD":
            return FakeResponse(404 if host in self.head_fail_hosts else self.head_status)
        if host == "graph.instagram.com":
            return self._graph(call)
        raise AssertionError(f"unexpected host {host}")

    def _id(self) -> str:
        self._n += 1
        return str(self._n)

    def _graph(self, c: Call) -> FakeResponse:
        token = c.params.get("access_token") or c.data.get("access_token")
        if c.path == "refresh_access_token":
            if token not in self.refresh_map:
                return ig_error("Invalid OAuth access token", code=190)
            return FakeResponse(200, {"access_token": self.refresh_map[token],
                                      "token_type": "bearer", "expires_in": 5184000})
        if token not in self.tokens:
            return ig_error("Invalid OAuth access token", code=190)
        user_id, username = self.tokens[token]
        parts = c.path.split("/")

        if c.method == "GET" and c.path == "me":
            return FakeResponse(200, {"user_id": user_id, "username": username, "id": "app-scoped"})

        if c.method == "POST" and parts == [user_id, "media"]:
            if c.data.get("is_carousel_item") == "true":
                if c.data.get("media_type") == "VIDEO":     # video slide in a carousel
                    if "image_url" in c.data or "alt_text" in c.data:
                        return ig_error("Invalid parameter for a VIDEO carousel item")
                    if not str(c.data.get("video_url", "")).endswith(".mp4"):
                        return ig_error("video_url must be an mp4")
                    cid = self._id()
                    self.containers[cid] = {"kind": "video_item", "status": "IN_PROGRESS", **c.data}
                    return FakeResponse(200, {"id": cid})
                if "media_type" in c.data or "image_url" not in c.data:
                    return ig_error("bad carousel item")
                if self.reject_alt_text and "alt_text" in c.data:
                    return ig_error("Invalid parameter alt_text")
                cid = self._id()
                self.containers[cid] = {"kind": "item", "status": "FINISHED", **c.data}
                return FakeResponse(200, {"id": cid})
            if c.data.get("media_type") == "CAROUSEL":
                kids = c.data.get("children", "").split(",")
                if not (1 <= len(kids) <= 10):
                    return ig_error("A carousel takes up to 10 children")
                for k in kids:   # like Meta: every child must exist and be FINISHED
                    ch = self.containers.get(k)
                    if not ch or ch["kind"] not in ("item", "video_item") or ch["status"] != "FINISHED":
                        return ig_error(f"Media ID {k} is not available", code=9007)
                cid = self._id()
                self.containers[cid] = {"kind": "carousel", "status": "IN_PROGRESS",
                                        "user": user_id, **c.data}
                return FakeResponse(200, {"id": cid})
            if c.data.get("media_type") == "REELS":
                if "trial_params" in c.data and self.reject_trial:
                    return ig_error("Invalid parameter trial_params")
                if not str(c.data.get("video_url", "")).endswith(".mp4"):
                    return ig_error("video_url must be an mp4")
                cid = self._id()
                self.containers[cid] = {"kind": "reel", "status": "IN_PROGRESS",
                                        "user": user_id, **c.data}
                return FakeResponse(200, {"id": cid})
            if c.data.get("media_type") == "STORIES":
                if "caption" in c.data or ("image_url" in c.data) == ("video_url" in c.data):
                    return ig_error("bad story request")
                is_vid = "video_url" in c.data
                cid = self._id()
                self.containers[cid] = {"kind": "story", "status": "IN_PROGRESS" if is_vid else "FINISHED",
                                        "user": user_id, **c.data}
                return FakeResponse(200, {"id": cid})
            if "image_url" in c.data:  # single image post
                cid = self._id()
                self.containers[cid] = {"kind": "image", "status": "FINISHED",
                                        "user": user_id, **c.data}
                return FakeResponse(200, {"id": cid})
            return ig_error("bad media request")

        if c.method == "GET" and len(parts) == 1 and parts[0] in self.containers:
            cont = self.containers[parts[0]]
            if cont["status"] == "IN_PROGRESS" and cont["kind"] == "video_item":
                if self.video_never_finishes:
                    return FakeResponse(200, {"status_code": "IN_PROGRESS", "id": parts[0]})
                cont["status"] = self.video_item_script.pop(0) if self.video_item_script else "FINISHED"
                if cont["status"] == "IN_PROGRESS":
                    return FakeResponse(200, {"status_code": "IN_PROGRESS", "id": parts[0]})
            if cont["status"] == "IN_PROGRESS":
                cont["status"] = self.status_script.pop(0) if self.status_script else "FINISHED"
                if cont["status"] == "IN_PROGRESS":
                    return FakeResponse(200, {"status_code": "IN_PROGRESS", "id": parts[0]})
            return FakeResponse(200, {"status_code": cont["status"], "id": parts[0],
                                      "status": "Error: test" if cont["status"] == "ERROR" else ""})

        if c.method == "POST" and parts == [user_id, "media_publish"]:
            if self.fail_publish:
                self.fail_publish -= 1
                return ig_error("Temporary publish failure", code=9007)
            cid = c.data["creation_id"]
            cont = self.containers[cid]
            assert cont["status"] == "FINISHED", "published a container that wasn't FINISHED"
            cont["status"] = "PUBLISHED"
            mid = "m" + self._id()
            if cont["kind"] == "story":   # Stories never show in /media
                self.stories.setdefault(user_id, []).append(mid)
                return FakeResponse(200, {"id": mid})
            self.media.setdefault(user_id, []).insert(0, {
                "id": mid, "caption": cont.get("caption"), "timestamp": "2026-10-15T16:00:00+0000",
                "permalink": f"https://www.instagram.com/p/{mid}/"})
            return FakeResponse(200, {"id": mid})

        if c.method == "GET" and parts == [user_id, "media"]:
            return FakeResponse(200, {"data": list(self.media.get(user_id, []))})

        all_media = {m["id"]: m for ms in self.media.values() for m in ms}
        if c.method == "GET" and len(parts) == 1 and parts[0] in all_media:
            return FakeResponse(200, all_media[parts[0]])

        if len(parts) == 2 and parts[1] == "comments" and parts[0] in all_media:
            if c.method == "POST":
                if self.fail_comment:
                    self.fail_comment -= 1
                    return ig_error("Comment failed (test)", code=2, status=500)
                cmid = "c" + self._id()
                self.comments.setdefault(parts[0], []).append(
                    {"id": cmid, "text": c.data["message"], "username": username})
                return FakeResponse(200, {"id": cmid})
            return FakeResponse(200, {"data": self.comments.get(parts[0], [])})

        return ig_error(f"unknown path {c.method} {c.path}")

    # helpers for assertions
    def posts(self) -> list[Call]:
        return [c for c in self.calls if c.method == "POST"]

    def publishes(self) -> list[Call]:
        return [c for c in self.calls if c.method == "POST" and c.path.endswith("media_publish")]

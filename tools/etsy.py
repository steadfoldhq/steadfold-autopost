#!/usr/bin/env python3
"""
Steadfold Etsy auto-lister (Etsy Open API v3).

Lists APPROVED digital products on the Etsy shops SteadfoldHQ and LittlefoldHQ
from the specs in listings/<ID>.json, with no browser and no copy-paste.

Commands (all run inside GitHub Actions; see .github/workflows/etsy-*.yml):
  auth-start   --shop STEADFOLD|LITTLEFOLD
      makes a PKCE verifier, saves it as the secret ETSY_PKCE_<SHOP> and writes
      the Etsy "Allow access" link to the job summary.
  auth-finish  --shop STEADFOLD|LITTLEFOLD     (code in env ETSY_AUTH_CODE)
      swaps the one-time code for tokens, checks the right shop signed in and
      saves ETSY_REFRESH_TOKEN_<SHOP>.
  list --spec listings/<ID>.json | all | batch:<name>   [--dry-run | --check]
      "all" = every APPROVED spec with no "batch" (the original 12). A spec with
      "batch": "<name>" is listed only by "batch:<name>" (or go.json "batch").
  list --go listings/go.json             [--dry-run | --check]
      --dry-run  validates and prints the plan. No network, no secrets.
      --check    read-only Etsy calls (shop, currency, category, duplicates).
      (neither)  creates, fills, publishes and verifies each listing, then
                 records it in listings/live.json and prints only its URL.
  validate                                     offline check of every spec
  approve --batch NAME --said "owner's words" --at "when"
      flips every WAITING spec in that batch to APPROVED with the owner's words
      (source claude/review-queue.md) and writes listings/go.json for the batch.
      Only ever run with words the owner actually said.
  deactivate --spec ID[,ID]   take LIVE listings off sale (Etsy state "inactive"); reversible
  reactivate --spec ID[,ID]   put a listing this tool deactivated back on sale (state "active")
  ops                         run new entries of listings/ops/queue.json once each (deactivate/reactivate/
                              sync parts=description only); results in listings/ops/done.json
  store-secret --name NAME --from-file PATH    write one repo secret (GH_PAT)
  encrypt --src FILE --dest listings/files/... age-encrypt one customer file
                                               with keys/etsy-files.pub

Secrets it reads (env, set by the workflows from repo secrets):
  ETSY_KEYSTRING / ETSY_SHARED_SECRET                (SteadfoldHQ's Etsy app)
  ETSY_KEYSTRING_LITTLEFOLD / ETSY_SHARED_SECRET_LITTLEFOLD  (LittlefoldHQ's app;
      falls back to the plain names when the shops share one app)
  ETSY_REFRESH_TOKEN_<SHOP>, ETSY_PKCE_<SHOP>, ETSY_FILES_AGE_KEY, GH_PAT
Nothing secret is ever printed: every token is masked in Actions logs and
scrubbed from messages.

Never touches payments, payouts, billing or tax. Etsy's own US$0.20 listing fee
applies when a listing is published (pre-approved for the APPROVED specs only).
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import os
import re
import secrets as pysecrets
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
LISTINGS = ROOT / "listings"
LIVE_PATH = LISTINGS / "live.json"
PUBKEY_PATH = ROOT / "keys" / "etsy-files.pub"

API = "https://api.etsy.com/v3/application"
AUTHORIZE_URL = "https://www.etsy.com/oauth/connect"
TOKEN_URL = "https://api.etsy.com/v3/public/oauth/token"
# Etsy sends the browser back here with ?code=...&state=... in the address bar.
# Must match the app's registered callback exactly (https, no trailing slash).
DEFAULT_REDIRECT = "https://github.com/steadfoldhq/steadfold-autopost"
SCOPES = ("listings_r", "listings_w", "shops_r")

SHOPS = {"STEADFOLD": "SteadfoldHQ", "LITTLEFOLD": "LittlefoldHQ"}
CURRENCIES = ("USD", "CAD")
APPROVAL_SOURCES = (
    "claude/automation/prompt-21b-approved-uploads.txt",
    "claude/automation/prompt-24-launch-oct16.txt",
    "claude/review-queue.md",          # batch approvals recorded by `approve`
)
WAITING = "WAITING"                    # built + spec'd, owner hasn't approved: never listed
BATCH_OK = re.compile(r"^[a-z0-9][a-z0-9-]{1,40}$")
WHEN_MADE = ("2020_2026", "2020_2025", "2020_2024")   # tried in order ("2020 - 2026")

MAX_TITLE = 140
MAX_TAGS = 13
MAX_TAG_LEN = 20
MAX_PHOTOS = 10
MAX_FILES = 5
MAX_FILE_BYTES = 20 * 1024 * 1024        # Etsy: 20 MB per digital file
MAX_PHOTO_BYTES = 20 * 1024 * 1024
MAX_VIDEO_BYTES = 100 * 1024 * 1024
PHOTO_EXT = (".jpg", ".jpeg", ".png", ".gif")
VIDEO_EXT = (".mp4", ".mov")
TITLE_OK = re.compile(r"^[\w\s.,:;!?'\"()&%+/\-–—*#@$€£₹×=<>\[\]™©®]+$", re.UNICODE)
TAG_OK = re.compile(r"^[^\W_]+(?:[ \-'][^\W_]+)*$", re.UNICODE)
MATERIAL_OK = re.compile(r"^[^\W_]+(?: [^\W_]+)*$", re.UNICODE)
NO_HEALTH_WORDS = re.compile(r"\b(sleep|pajamas?|pyjamas?|soothing|safe)\b", re.IGNORECASE)


# ----------------------------------------------------------------- secrets / log
_SECRETS: set[str] = set()


def register_secret(value: str | None) -> None:
    """Remember a secret: masked in GitHub Actions logs, scrubbed from our output."""
    for line in str(value or "").splitlines():
        line = line.strip()
        if len(line) >= 6 and line not in _SECRETS:
            _SECRETS.add(line)
            if os.environ.get("GITHUB_ACTIONS") == "true":
                print(f"::add-mask::{line}", flush=True)


def redact(text: Any) -> str:
    s = str(text)
    for secret in sorted(_SECRETS, key=len, reverse=True):
        s = s.replace(secret, "***")
    s = re.sub(r"(?i)(bearer\s+)[A-Za-z0-9._\-]+", r"\1***", s)
    s = re.sub(r"(?i)((?:refresh_token|access_token|code|code_verifier)[\"'=:\s]+)[A-Za-z0-9._\-]{8,}",
               r"\1***", s)
    return s


def log(msg: str = "") -> None:
    print(redact(msg), flush=True)


SUMMARY_FILE: str | None = None


def summary(md: str) -> None:
    """Append to the GitHub job summary (when running in Actions)."""
    path = SUMMARY_FILE
    if path:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(redact(md) + "\n")


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ----------------------------------------------------------------- shop config
def shop_creds(shop: str, env: dict) -> tuple[str, str]:
    """(keystring, shared_secret) for a shop: <NAME>_<SHOP> first, then the plain name."""
    k = (env.get(f"ETSY_KEYSTRING_{shop}") or env.get("ETSY_KEYSTRING") or "").strip()
    s = (env.get(f"ETSY_SHARED_SECRET_{shop}") or env.get("ETSY_SHARED_SECRET") or "").strip()
    register_secret(s)
    if not k or not s:
        raise SetupError(
            f"Missing Etsy app keys for {SHOPS[shop]}. Add the repo secrets "
            f"ETSY_KEYSTRING and ETSY_SHARED_SECRET (or ETSY_KEYSTRING_{shop} and "
            f"ETSY_SHARED_SECRET_{shop} for this shop's own app). See docs/etsy-setup.md.")
    return k, s


def expected_shop_name(shop: str, env: dict) -> str:
    return (env.get(f"ETSY_SHOP_NAME_{shop}") or SHOPS[shop]).strip()


def redirect_uri(env: dict) -> str:
    return (env.get("ETSY_REDIRECT_URI") or DEFAULT_REDIRECT).strip()


class SetupError(RuntimeError):
    """Something the owner must set up first (message says exactly what)."""


class EtsyError(RuntimeError):
    def __init__(self, msg: str, status: int = 0, body: str = ""):
        super().__init__(redact(msg))
        self.status = status
        self.body = redact(body)


# ----------------------------------------------------------------- OAuth (PKCE)
def pkce_pair() -> tuple[str, str]:
    """(verifier, S256 challenge). Verifier: 86 chars of [A-Za-z0-9_-] (Etsy: 43-128)."""
    verifier = b64url(os.urandom(64))
    challenge = b64url(hashlib.sha256(verifier.encode("ascii")).digest())
    return verifier, challenge


def _pct_all(s: str) -> str:
    """Percent-encode every byte. Equivalent for Etsy, but keeps GitHub's secret
    masking from turning the keystring inside the link into '***'."""
    return "".join(f"%{b:02X}" for b in s.encode("utf-8"))


def authorize_url(keystring: str, redirect: str, challenge: str, state: str,
                  scopes: Iterable[str] = SCOPES) -> str:
    from urllib.parse import quote
    q = [("response_type", "code"), ("redirect_uri", quote(redirect, safe="")),
         ("scope", quote(" ".join(scopes), safe="")), ("client_id", _pct_all(keystring)),
         ("state", state), ("code_challenge", challenge), ("code_challenge_method", "S256")]
    return AUTHORIZE_URL + "?" + "&".join(f"{k}={v}" for k, v in q)


def parse_code(text: str) -> tuple[str, str | None]:
    """Accept the raw code or the whole address-bar URL Etsy sent you back to."""
    t = (text or "").strip().strip('"').strip("'")
    if not t:
        raise SetupError("No code given. Paste the whole address from the browser bar "
                         "after clicking Allow access.")
    if "code=" in t or "error=" in t:
        qs = parse_qs(urlparse(t if "://" in t else "https://x/?" + t.split("?", 1)[-1]).query)
        if "error" in qs:
            raise SetupError(f"Etsy said: {qs.get('error', [''])[0]} "
                             f"{qs.get('error_description', [''])[0]}. Run 'start' again.")
        code = (qs.get("code") or [""])[0].strip()
        state = (qs.get("state") or [None])[0]
    else:
        code, state = t, None
    if not re.fullmatch(r"[A-Za-z0-9._~\-]{10,}", code or ""):
        raise SetupError("That doesn't look like an Etsy code. Paste the whole address "
                         "from the browser bar after clicking Allow access.")
    register_secret(code)
    return code, state


def _token_call(session: Any, keystring: str, shared: str, data: dict) -> dict:
    headers = {"x-api-key": f"{keystring}:{shared}", "Accept": "application/json"}
    try:
        r = session.request("POST", TOKEN_URL, data=data, headers=headers, timeout=60)
    except Exception as exc:  # network
        raise EtsyError(f"Etsy token endpoint unreachable: {exc}") from None
    if r.status_code != 200:
        raise EtsyError(f"Etsy token request failed (HTTP {r.status_code}): {r.text[:300]}",
                        r.status_code, r.text)
    body = r.json()
    for k in ("access_token", "refresh_token"):
        register_secret(body.get(k))
    if not body.get("access_token") or not body.get("refresh_token"):
        raise EtsyError("Etsy token response had no tokens")
    return body


def exchange_code(session, keystring, shared, redirect, code, verifier) -> dict:
    return _token_call(session, keystring, shared, {
        "grant_type": "authorization_code", "client_id": keystring,
        "redirect_uri": redirect, "code": code, "code_verifier": verifier})


def refresh_access(session, keystring, shared, refresh_token) -> dict:
    return _token_call(session, keystring, shared, {
        "grant_type": "refresh_token", "client_id": keystring, "refresh_token": refresh_token})


# ----------------------------------------------------------------- Etsy client
class EtsyClient:
    def __init__(self, keystring: str, shared: str, access_token: str | None = None,
                 session: Any = None, sleep: Callable[[float], None] = time.sleep):
        import requests  # noqa: F401  (only needed for real network use)
        self.keystring, self._shared, self._token = keystring, shared, access_token
        register_secret(shared)
        register_secret(access_token)
        self.session = session or requests.Session()
        self.sleep = sleep

    def _headers(self, auth: bool) -> dict:
        h = {"x-api-key": f"{self.keystring}:{self._shared}", "Accept": "application/json"}
        if auth and self._token:
            h["Authorization"] = f"Bearer {self._token}"
        return h

    def call(self, method: str, path: str, *, params=None, data=None, files=None,
             auth: bool = True, retry_5xx: bool | None = None) -> Any:
        url = API + path
        retry_5xx = (method == "GET") if retry_5xx is None else retry_5xx
        for attempt in range(4):
            try:
                r = self.session.request(method, url, params=params, data=data, files=files,
                                         headers=self._headers(auth), timeout=300)
            except Exception as exc:
                if method == "GET" and attempt < 3:
                    self.sleep(2 * (attempt + 1))
                    continue
                raise EtsyError(f"{method} {path}: network error: {exc}") from None
            if r.status_code == 429 and attempt < 3:      # rate limited: not processed
                self.sleep(float(getattr(r, "headers", {}).get("Retry-After", 0) or 3 * (attempt + 1)))
                continue
            if r.status_code >= 500 and retry_5xx and attempt < 3:
                self.sleep(3 * (attempt + 1))
                continue
            if r.status_code not in (200, 201, 204):
                raise EtsyError(f"{method} {path} failed (HTTP {r.status_code}): {r.text[:400]}",
                                r.status_code, r.text)
            if r.status_code == 204 or not r.text:
                return {}
            return r.json()
        raise EtsyError(f"{method} {path}: gave up after retries")

    # read
    def me(self) -> dict:
        return self.call("GET", "/users/me")

    def shop(self, shop_id: int) -> dict:
        return self.call("GET", f"/shops/{shop_id}")

    def taxonomy(self) -> list:
        return self.call("GET", "/seller-taxonomy/nodes", auth=False).get("results", [])

    def shop_listings(self, shop_id: int, state: str) -> list:
        out, offset = [], 0
        while True:
            body = self.call("GET", f"/shops/{shop_id}/listings",
                             params={"state": state, "limit": 100, "offset": offset})
            res = body.get("results", [])
            out += res
            offset += len(res)
            if not res or offset >= int(body.get("count", 0)):
                return out

    def listing(self, listing_id: int) -> dict:
        return self.call("GET", f"/listings/{listing_id}")

    def images(self, listing_id: int) -> list:
        return self.call("GET", f"/listings/{listing_id}/images").get("results", [])

    def videos(self, listing_id: int) -> list:
        return self.call("GET", f"/listings/{listing_id}/videos").get("results", [])

    def files(self, shop_id: int, listing_id: int) -> list:
        return self.call("GET", f"/shops/{shop_id}/listings/{listing_id}/files").get("results", [])

    # write (listings_w only)
    def create_draft(self, shop_id: int, fields: dict) -> dict:
        return self.call("POST", f"/shops/{shop_id}/listings", data=fields)

    def update(self, shop_id: int, listing_id: int, fields: dict) -> dict:
        return self.call("PATCH", f"/shops/{shop_id}/listings/{listing_id}", data=fields)

    def upload_image(self, shop_id, listing_id, path: Path, rank: int) -> dict:
        return self.call("POST", f"/shops/{shop_id}/listings/{listing_id}/images",
                         data={"rank": str(rank)},
                         files={"image": (path.name, path.read_bytes(), _mime(path))})

    def upload_video(self, shop_id, listing_id, path: Path) -> dict:
        return self.call("POST", f"/shops/{shop_id}/listings/{listing_id}/videos",
                         data={"name": path.name},
                         files={"video": (path.name, path.read_bytes(), _mime(path))})

    def upload_file(self, shop_id, listing_id, path: Path, name: str, rank: int) -> dict:
        return self.call("POST", f"/shops/{shop_id}/listings/{listing_id}/files",
                         data={"name": name, "rank": str(rank)},
                         files={"file": (name, path.read_bytes(), _mime(path))})


def _mime(p: Path) -> str:
    return {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".gif": "image/gif",
            ".mp4": "video/mp4", ".mov": "video/quicktime", ".pdf": "application/pdf",
            ".zip": "application/zip"}.get(p.suffix.lower(), "application/octet-stream")


# ----------------------------------------------------------------- specs
def all_spec_paths() -> list[Path]:
    return sorted(p for p in LISTINGS.glob("*.json") if p.name not in ("live.json", "go.json"))


def spec_batch(spec: dict) -> str:
    """The batch a spec belongs to. No "batch" field = the original "all" batch."""
    return str(spec.get("batch") or "all")


def _sorted(specs: list[tuple[dict, Path]]) -> list[Path]:
    specs.sort(key=lambda sp: (sp[0].get("order", 999), sp[0]["id"]))
    return [p for _, p in specs]


def batch_paths(name: str) -> list[Path]:
    """Every spec in batch <name>, whatever its status (validation refuses WAITING ones)."""
    name = name.strip()
    if not BATCH_OK.match(name) or name == "all":
        raise SetupError(f"Not a batch name: {name!r}. Use batch:<name>, e.g. batch:oct17-new.")
    specs = [(load_spec(p), p) for p in all_spec_paths()]
    hits = [(s, p) for s, p in specs if spec_batch(s) == name]
    if not hits:
        known = sorted({spec_batch(s) for s, _ in specs} - {"all"})
        raise SetupError(f"No specs in batch {name!r}. Batches: {known}")
    return _sorted(hits)


def spec_paths(selector: str) -> list[Path]:
    selector = (selector or "").strip()
    if selector in ("all", "listings/all", "all-approved"):
        specs = [(load_spec(p), p) for p in all_spec_paths()]
        specs = [(s, p) for s, p in specs if s.get("status") == "APPROVED" and spec_batch(s) == "all"]
        return _sorted(specs)
    if selector.startswith("batch:"):
        return batch_paths(selector[len("batch:"):])
    p = Path(selector)
    p = p if p.is_absolute() else ROOT / p
    if not p.exists():
        raise SetupError(f"No listing spec at {selector}")
    return [p]


def load_spec(path: Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _inside(root: Path, rel: str) -> Path | None:
    p = (ROOT / rel).resolve()
    try:
        p.relative_to(root.resolve())
    except ValueError:
        return None
    return p


def validate_spec(spec: dict, path: Path | None = None, check_files: bool = True,
                  allow_waiting: bool = False) -> list[str]:
    """Return a list of problems (empty = OK). Pure: no network.
    allow_waiting: a WAITING spec (built, not yet approved) passes as a well-formed spec.
    Listing never sets it, so a WAITING spec is never sent to Etsy."""
    e: list[str] = []
    sid = spec.get("id", "")
    for k in ("id", "shop", "status", "approval", "title", "description", "price", "tags",
              "taxonomy", "photos", "files", "quantity"):
        if k not in spec:
            e.append(f"missing field '{k}'")
    if e:
        return e
    if path is not None and path.stem != sid:
        e.append(f"file name {path.name} must be {sid}.json")
    ap = spec["approval"] if isinstance(spec["approval"], dict) else {}
    waiting = allow_waiting and spec["status"] == WAITING
    if waiting:
        if not str(ap.get("review_queue", "")).strip():
            e.append("WAITING spec needs approval.review_queue (where the owner decides)")
        if spec_batch(spec) == "all":
            e.append("WAITING spec must name its own batch, never the 'all' batch")
    else:
        if spec["status"] != "APPROVED":
            e.append("status must be APPROVED (nothing else is ever listed)"
                     + (" — this spec is WAITING for the owner's approval" if spec["status"] == WAITING else ""))
        if ap.get("source") not in APPROVAL_SOURCES:
            e.append(f"approval.source must be one of {APPROVAL_SOURCES}")
        for k in ("approved_by", "approved_at", "quote"):
            if not str(ap.get(k, "")).strip():
                e.append(f"approval.{k} is empty")
    if "batch" in spec and not (isinstance(spec["batch"], str) and BATCH_OK.match(spec["batch"])):
        e.append("batch must be lower-case letters, digits and dashes, e.g. oct17-new")
    if spec["shop"] not in SHOPS:
        e.append(f"shop must be one of {list(SHOPS)}")

    t = spec["title"]
    if not isinstance(t, str) or not t.strip() or t != t.strip():
        e.append("title is empty or has leading/trailing spaces")
    else:
        if len(t) > MAX_TITLE:
            e.append(f"title is {len(t)} characters (Etsy max {MAX_TITLE})")
        if not TITLE_OK.match(t):
            e.append("title has characters Etsy does not allow")
        for ch in "%:&+":
            if t.count(ch) > 1:
                e.append(f"title uses '{ch}' more than once (Etsy allows it once)")
    d = spec["description"]
    if not isinstance(d, str) or len(d.strip()) < 40:
        e.append("description is missing or too short")

    price = spec["price"]
    if not isinstance(price, dict) or not price:
        e.append("price must map currency -> amount, e.g. {\"USD\": 16.0}")
    else:
        for cur, amt in price.items():
            if cur not in CURRENCIES:
                e.append(f"price currency {cur} not supported")
            if not isinstance(amt, (int, float)) or amt <= 0:
                e.append(f"price {cur} must be a positive number")
    for cur, ov in (spec.get("currency_overrides") or {}).items():
        if cur not in (price or {}):
            e.append(f"currency_overrides.{cur} has no matching price")
        for old, _new in ov.get("replace", []):
            if isinstance(d, str) and d.count(old) != 1:
                e.append(f"currency_overrides.{cur}: text to replace must appear exactly once: {old!r}")

    q = spec["quantity"]
    if not isinstance(q, int) or not 1 <= q <= 999:
        e.append("quantity must be 1-999")

    tags = spec["tags"]
    if not isinstance(tags, list) or not 1 <= len(tags) <= MAX_TAGS:
        e.append(f"tags: need 1-{MAX_TAGS}")
    else:
        seen = set()
        for tg in tags:
            if not isinstance(tg, str) or len(tg) > MAX_TAG_LEN or not TAG_OK.match(tg):
                e.append(f"tag not allowed by Etsy (max {MAX_TAG_LEN} letters/numbers/spaces): {tg!r}")
            if str(tg).lower() in seen:
                e.append(f"duplicate tag {tg!r}")
            seen.add(str(tg).lower())
    mats = spec.get("materials", [])
    if not isinstance(mats, list) or len(mats) > 13:
        e.append("materials: up to 13")
    for m in mats if isinstance(mats, list) else []:
        if not isinstance(m, str) or not MATERIAL_OK.match(m) or len(m) > 45:
            e.append(f"material not allowed by Etsy (letters, numbers, spaces): {m!r}")

    tax = spec["taxonomy"]
    if not isinstance(tax, dict) or not (isinstance(tax.get("id"), int) or tax.get("names")):
        e.append("taxonomy needs an 'id' or a list of 'names' to look up")

    photos = spec["photos"]
    if not isinstance(photos, list) or not 1 <= len(photos) <= MAX_PHOTOS:
        e.append(f"photos: need 1-{MAX_PHOTOS}")
    else:
        for ph in photos:
            p = _inside(LISTINGS / "media", ph)
            if p is None:
                e.append(f"photo must be under listings/media/: {ph}")
                continue
            if p.suffix.lower() not in PHOTO_EXT:
                e.append(f"photo type not allowed: {ph}")
            if check_files:
                if not p.exists():
                    e.append(f"photo not found: {ph}")
                elif p.stat().st_size > MAX_PHOTO_BYTES:
                    e.append(f"photo too large: {ph}")
    video = spec.get("video")
    if video:
        p = _inside(LISTINGS / "media", video)
        if p is None or p.suffix.lower() not in VIDEO_EXT:
            e.append(f"video must be an .mp4/.mov under listings/media/: {video}")
        elif check_files and (not p.exists() or p.stat().st_size > MAX_VIDEO_BYTES):
            e.append(f"video missing or over 100 MB: {video}")

    files = spec["files"]
    if not isinstance(files, list) or not 1 <= len(files) <= MAX_FILES:
        e.append(f"files: need 1-{MAX_FILES} (Etsy's limit)")
    else:
        names = set()
        for f in files:
            if not isinstance(f, dict):
                e.append("each file needs name, enc, sha256, size")
                continue
            name, enc = f.get("name", ""), f.get("enc", "")
            if not name or name in names:
                e.append(f"file name missing or repeated: {name!r}")
            names.add(name)
            p = _inside(LISTINGS / "files", enc)
            if p is None or not enc.endswith(".age"):
                e.append(f"customer file must be encrypted (.age under listings/files/): {enc}")
            elif check_files and not p.exists():
                e.append(f"encrypted file not found: {enc}")
            if not re.fullmatch(r"[0-9a-f]{64}", str(f.get("sha256", ""))):
                e.append(f"{name}: sha256 of the original file is missing")
            size = f.get("size")
            if not isinstance(size, int) or not 0 < size <= MAX_FILE_BYTES:
                e.append(f"{name}: size missing or over Etsy's 20 MB per file")

    if "littlefold-no-health-words" in spec.get("content_rules", []):
        blob = " ".join([t, d, " ".join(tags if isinstance(tags, list) else [])])
        bad = sorted({m.group(0).lower() for m in NO_HEALTH_WORDS.finditer(blob)})
        if bad:
            e.append(f"Littlefold rule: remove the word(s) {bad}")
        if spec.get("personalization"):
            e.append("Littlefold rule: personalisation must stay OFF")
    return e


def description_for(spec: dict, currency: str) -> str:
    d = spec["description"]
    for old, new in (spec.get("currency_overrides") or {}).get(currency, {}).get("replace", []):
        d = d.replace(old, new)
    return d


def listing_fields(spec: dict, currency: str, taxonomy_id: int, when_made: str) -> dict:
    """Form fields for createDraftListing (application/x-www-form-urlencoded)."""
    f = {
        "quantity": str(spec["quantity"]),
        "title": spec["title"],
        "description": description_for(spec, currency),
        "price": f"{float(spec['price'][currency]):.2f}",
        "who_made": "i_did",
        "when_made": when_made,
        "is_supply": "false",
        "taxonomy_id": str(taxonomy_id),
        "type": "download",
        "should_auto_renew": "false",
        "is_personalizable": "false",
        "tags": ",".join(spec["tags"]),
    }
    if spec.get("materials"):
        f["materials"] = ",".join(spec["materials"])
    return f


# ----------------------------------------------------------------- taxonomy
def flatten_taxonomy(nodes: list, path: tuple = ()) -> list[tuple[int, str, tuple]]:
    out = []
    for n in nodes:
        p = path + (n.get("name", ""),)
        out.append((int(n["id"]), n.get("name", ""), p))
        out += flatten_taxonomy(n.get("children") or [], p)
    return out


def resolve_taxonomy(tax: dict, nodes: list) -> tuple[int, str]:
    if isinstance(tax.get("id"), int):
        return tax["id"], f"id {tax['id']} (pinned)"
    flat = flatten_taxonomy(nodes)
    for want in tax.get("names", []):
        parts = [x.strip().lower() for x in want.split(">")]
        hits = [(i, p) for i, name, p in flat
                if [x.lower() for x in p[-len(parts):]] == parts]
        if hits:
            hits.sort(key=lambda h: len(h[1]))
            i, p = hits[0]
            return i, " > ".join(p)
    words = {w for n in tax.get("names", []) for w in re.findall(r"[a-z]{4,}", n.lower())}
    near = sorted({" > ".join(p) for _, name, p in flat if any(w in name.lower() for w in words)})[:12]
    raise EtsyError(f"No Etsy category matched {tax.get('names')}. Closest: {near}. "
                    f"Pin one by adding \"id\": <number> to the spec's taxonomy.")


# ----------------------------------------------------------------- live record
def load_live() -> dict:
    if LIVE_PATH.exists():
        return json.loads(LIVE_PATH.read_text(encoding="utf-8"))
    return {"listings": {}, "drafts": {}}


def save_live(live: dict) -> None:
    LIVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    LIVE_PATH.write_text(json.dumps(live, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def norm_title(t: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(t or "")).strip().lower()


# ----------------------------------------------------------------- files (age)
def decrypt_files(spec: dict, key_text: str, outdir: Path,
                  run: Callable = subprocess.run) -> list[tuple[Path, str]]:
    """Decrypt the spec's .age files into outdir; verify each sha256. Returns [(path, name)]."""
    if not key_text.strip():
        raise SetupError("ETSY_FILES_AGE_KEY is empty: run the 'Etsy files key' workflow first.")
    register_secret(key_text)
    outdir.mkdir(parents=True, exist_ok=True)
    fd, keyfile = tempfile.mkstemp(dir=outdir, prefix=".k")
    try:
        os.write(fd, key_text.encode())
        os.close(fd)
        os.chmod(keyfile, 0o600)
        out = []
        for i, f in enumerate(spec["files"]):
            enc = ROOT / f["enc"]
            dest = outdir / f"{i + 1:02d}-{f['name']}"
            r = run(["age", "--decrypt", "-i", keyfile, "-o", str(dest), str(enc)],
                    capture_output=True, text=True)
            if r.returncode != 0:
                raise EtsyError(f"could not decrypt {f['name']}: {redact(r.stderr)[:200]}")
            if sha256_file(dest) != f["sha256"]:
                raise EtsyError(f"{f['name']}: decrypted file does not match its sha256")
            out.append((dest, f["name"]))
        return out
    finally:
        try:
            os.remove(keyfile)
        except OSError:
            pass


def encrypt_file(src: Path, dest: Path, pubkey: str, run: Callable = subprocess.run) -> dict:
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = run(["age", "--encrypt", "-r", pubkey.strip(), "-o", str(dest), str(src)],
            capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"age failed for {src.name}: {r.stderr[:200]}")
    return {"name": src.name, "enc": str(dest.relative_to(ROOT)), "sha256": sha256_file(src),
            "size": src.stat().st_size}


# ----------------------------------------------------------------- GitHub secrets
def github_secrets(env: dict, session: Any = None, gh_factory: Callable | None = None):
    repo = (env.get("GITHUB_REPOSITORY") or "").strip()
    pat = (env.get("GH_PAT") or "").strip()
    register_secret(pat)
    if not repo or not pat:
        raise SetupError("GH_PAT and GITHUB_REPOSITORY must be set (the workflow does this).")
    if gh_factory:
        return gh_factory(repo, pat)
    sys.path.insert(0, str(ROOT))
    from refresh_tokens import GitHubSecrets  # same pattern as the Instagram tokens
    return GitHubSecrets(repo, pat, session=session)


# ----------------------------------------------------------------- commands
def cmd_auth_start(shop: str, env: dict, gh_factory=None) -> int:
    keystring, _ = shop_creds(shop, env)
    gh = github_secrets(env, gh_factory=gh_factory)
    verifier, challenge = pkce_pair()
    state = b64url(os.urandom(18))
    register_secret(verifier)
    gh.put(f"ETSY_PKCE_{shop}", json.dumps({"verifier": verifier, "state": state,
                                            "created": now_iso()}))
    url = authorize_url(keystring, redirect_uri(env), challenge, state)
    name = expected_shop_name(shop, env)
    log(f"Saved a fresh sign-in key for {name}. Open the link in the job summary.")
    summary(f"## Connect Etsy shop {name}\n\n"
            f"1. Make sure you're signed in to Etsy as the owner of **{name}** "
            f"(sign out of any other Etsy account first).\n"
            f"2. **[Click here to open Etsy]({url})** and press **Allow access**.\n"
            f"3. Etsy sends you to the GitHub repo page. Copy the **whole address** from the "
            f"browser's address bar (it contains `?code=`).\n"
            f"4. Run **Etsy auth** again with mode **finish**, shop **{shop}**, and paste "
            f"that address into **code**. Do it within a few minutes; the code is single-use.\n")
    return 0


def cmd_auth_finish(shop: str, env: dict, session=None, gh_factory=None) -> int:
    keystring, shared = shop_creds(shop, env)
    raw = env.get(f"ETSY_PKCE_{shop}") or ""
    register_secret(raw)
    try:
        pk = json.loads(raw)
        verifier = pk["verifier"]
        register_secret(verifier)
    except (ValueError, KeyError, TypeError):
        raise SetupError(f"No pending sign-in for {SHOPS[shop]}: run Etsy auth with mode "
                         f"'start' first, then 'finish'.") from None
    code, state = parse_code(env.get("ETSY_AUTH_CODE", ""))
    if state is not None and state != pk.get("state"):
        raise SetupError("This code came from an older 'start'. Run 'start' again and use "
                         "the newest link.")
    if session is None:
        import requests
        session = requests.Session()
    tok = exchange_code(session, keystring, shared, redirect_uri(env), code, verifier)
    client = EtsyClient(keystring, shared, tok["access_token"], session=session)
    me = client.me()
    shop_id = me.get("shop_id")
    if not shop_id:
        raise SetupError("The Etsy account you allowed has no shop. Sign in as the shop "
                         "owner and run 'start' again.")
    info = client.shop(int(shop_id))
    want = expected_shop_name(shop, env)
    got = info.get("shop_name", "")
    if got.lower() != want.lower():
        raise SetupError(f"You allowed access as shop '{got}', but this is the {want} "
                         f"slot. Sign out of Etsy, sign in as {want}'s owner, and run "
                         f"'start' again. Nothing was saved.")
    gh = github_secrets(env, gh_factory=gh_factory)
    gh.put(f"ETSY_REFRESH_TOKEN_{shop}", tok["refresh_token"])
    gh.put(f"ETSY_PKCE_{shop}", json.dumps({"used": now_iso()}))
    log(f"Connected {got} (currency {info.get('currency_code', '?')}). "
        f"Refresh token saved as ETSY_REFRESH_TOKEN_{shop}.")
    summary(f"## {got} connected\n\nShop currency: {info.get('currency_code', '?')}. "
            f"The lister can now publish approved listings to this shop.")
    return 0


class ShopSession:
    """An authenticated shop: refreshes the token and saves the rotated one."""

    def __init__(self, shop: str, env: dict, session=None, gh_factory=None):
        self.shop = shop
        keystring, shared = shop_creds(shop, env)
        rt = (env.get(f"ETSY_REFRESH_TOKEN_{shop}") or "").strip()
        register_secret(rt)
        if not rt:
            raise SetupError(f"{SHOPS[shop]} is not connected yet: run Etsy auth "
                             f"(start, then finish) for shop {shop}. See docs/etsy-setup.md.")
        if session is None:
            import requests
            session = requests.Session()
        tok = refresh_access(session, keystring, shared, rt)
        if tok["refresh_token"] != rt:
            # Save the rotated token straight away, before anything else can fail.
            github_secrets(env, gh_factory=gh_factory).put(f"ETSY_REFRESH_TOKEN_{shop}",
                                                           tok["refresh_token"])
        self.client = EtsyClient(keystring, shared, tok["access_token"], session=session)
        me = self.client.me()
        self.shop_id = int(me["shop_id"])
        self.info = self.client.shop(self.shop_id)
        want = expected_shop_name(shop, env)
        if self.info.get("shop_name", "").lower() != want.lower():
            raise SetupError(f"Token for {shop} opens shop '{self.info.get('shop_name')}', "
                             f"not {want}. Re-run Etsy auth for {shop}.")
        self.currency = self.info.get("currency_code", "")
        self.name = self.info.get("shop_name", want)
        self._tax: list | None = None

    def taxonomy(self) -> list:
        if self._tax is None:
            self._tax = self.client.taxonomy()
        return self._tax

    def find_by_title(self, title: str) -> dict | None:
        want = norm_title(title)
        for state in ("active", "draft", "inactive"):
            for L in self.client.shop_listings(self.shop_id, state):
                if norm_title(L.get("title", "")) == want:
                    L = dict(L)
                    L.setdefault("state", state)
                    return L
        return None


def plan_text(spec: dict) -> str:
    wait = "  (WAITING approval: will not list)" if spec.get("status") == WAITING else ""
    lines = [f"[{spec['id']}] {SHOPS[spec['shop']]} :: {spec['title']}{wait}",
             f"  batch: {spec_batch(spec)}",
             f"  price: " + ", ".join(f"{c} {a:.2f}" for c, a in spec["price"].items()),
             f"  category lookup: {spec['taxonomy'].get('id') or spec['taxonomy'].get('names')}",
             f"  tags ({len(spec['tags'])}): {', '.join(spec['tags'])}",
             f"  photos: {len(spec['photos'])}; video: {'yes' if spec.get('video') else 'no'}",
             "  files: " + "; ".join(f"{f['name']} ({f['size'] / 1e6:.1f} MB)" for f in spec["files"])]
    for b in spec.get("by_hand", []):
        lines.append(f"  BY HAND after publish: {b}")
    return "\n".join(lines)


def list_one(spec: dict, ss: ShopSession, live: dict, env: dict, check: bool,
             workdir: Path, run: Callable = subprocess.run,
             sleep: Callable[[float], None] = time.sleep) -> dict:
    """List one spec. Returns a result dict (status: live | exists | checked | failed)."""
    sid = spec["id"]
    c = ss.client
    if sid in live["listings"]:
        return {"id": sid, "status": "exists", "url": live["listings"][sid]["url"],
                "note": "already in listings/live.json"}
    cur = ss.currency
    if cur not in spec["price"]:
        raise EtsyError(f"{ss.name} is priced in {cur}; this spec has prices for "
                        f"{list(spec['price'])} only. Not converting: add a {cur} price.")
    tax_id, tax_path = resolve_taxonomy(spec["taxonomy"], ss.taxonomy())
    existing = ss.find_by_title(spec["title"])
    draft_id = (live.get("drafts", {}).get(sid) or {}).get("listing_id")
    if existing and existing.get("state") == "active":
        url = existing.get("url") or f"https://www.etsy.com/listing/{existing['listing_id']}"
        if not check:
            live["listings"][sid] = {"listing_id": existing["listing_id"], "url": url,
                                     "shop": ss.name, "listed_at": now_iso(),
                                     "note": "found already live (not created by the lister)"}
        return {"id": sid, "status": "exists", "url": url, "note": "already live on Etsy"}
    if existing:
        draft_id = existing["listing_id"]
    if check:
        return {"id": sid, "status": "checked",
                "note": f"{cur} {spec['price'][cur]:.2f} · category {tax_path} · "
                        + (f"will finish draft {draft_id}" if draft_id else "will create new")}

    files = decrypt_files(spec, env.get("ETSY_FILES_AGE_KEY", ""), workdir / sid, run=run)
    fields = listing_fields(spec, cur, tax_id, WHEN_MADE[0])
    if draft_id:
        L = c.listing(int(draft_id))
        p = L.get("price") or {}
        amount = (p.get("amount", 0) / (p.get("divisor") or 100)) if p else None
        if amount is not None and abs(amount - float(spec["price"][cur])) > 0.001:
            raise EtsyError(f"draft {draft_id} has price {amount:.2f}; expected "
                            f"{spec['price'][cur]:.2f}. Fix the price on that draft by hand.")
        upd = {k: v for k, v in fields.items() if k not in ("price", "quantity", "when_made")}
        c.update(ss.shop_id, int(draft_id), upd)
        lid = int(draft_id)
        log(f"[{sid}] finishing existing draft {lid}")
    else:
        created = None
        for wm in WHEN_MADE:
            fields["when_made"] = wm
            try:
                created = c.create_draft(ss.shop_id, fields)
                break
            except EtsyError as exc:
                if exc.status == 400 and "when_made" in exc.body and wm != WHEN_MADE[-1]:
                    continue
                raise
        lid = int(created["listing_id"])
        log(f"[{sid}] draft {lid} created ({cur} {spec['price'][cur]:.2f}, {tax_path})")
    live.setdefault("drafts", {})[sid] = {"listing_id": lid, "shop": ss.name, "at": now_iso()}

    have_imgs = len(c.images(lid))
    for i, ph in enumerate(spec["photos"][have_imgs:], start=have_imgs + 1):
        c.upload_image(ss.shop_id, lid, ROOT / ph, i)
    if spec.get("video") and not c.videos(lid):
        c.upload_video(ss.shop_id, lid, ROOT / spec["video"])
    have_files = {f.get("filename") or f.get("name") for f in c.files(ss.shop_id, lid)}
    for rank, (path, name) in enumerate(files, start=1):
        if name not in have_files:
            c.upload_file(ss.shop_id, lid, path, name, rank)
    log(f"[{sid}] {len(spec['photos'])} photos, {'1 video, ' if spec.get('video') else ''}"
        f"{len(files)} files attached")

    c.update(ss.shop_id, lid, {"state": "active"})
    L = {}
    for attempt in range(5):
        L = c.listing(lid)
        if L.get("state") == "active":
            break
        sleep(4)
    if L.get("state") != "active":
        raise EtsyError(f"listing {lid} did not go active (state {L.get('state')}); "
                        f"it is saved as a draft")
    if norm_title(L.get("title", "")) != norm_title(spec["title"]):
        raise EtsyError(f"listing {lid} is live but its title differs from the spec")
    url = (L.get("url") or f"https://www.etsy.com/listing/{lid}").split("?")[0]
    live["listings"][sid] = {"listing_id": lid, "url": url, "shop": ss.name,
                             "listed_at": now_iso(), "price": f"{cur} {spec['price'][cur]:.2f}"}
    live["drafts"].pop(sid, None)
    return {"id": sid, "status": "live", "url": url}


def select_specs(args, env: dict) -> list[tuple[dict, Path]]:
    if args.go:
        gp = Path(args.go)
        gp = gp if gp.is_absolute() else ROOT / gp
        go = json.loads(gp.read_text(encoding="utf-8"))
        if not str(go.get("owner_said", "")).strip() or not str(go.get("at", "")).strip():
            raise SetupError("listings/go.json needs the owner's words ('owner_said') and 'at'.")
        ids = go.get("ids")
        if go.get("batch"):
            if ids not in (None, "all"):
                raise SetupError("go.json: give either 'batch' or 'ids', not both.")
            paths = batch_paths(str(go["batch"]))
        elif ids == "all":
            paths = spec_paths("all")
        else:
            want = set(ids or [])
            approved = [p for p in all_spec_paths() if load_spec(p).get("status") == "APPROVED"]
            paths = _sorted([(load_spec(p), p) for p in approved if p.stem in want])
            missing = want - {p.stem for p in paths}
            if missing or not want:
                raise SetupError(f"go.json names IDs with no APPROVED spec: {sorted(missing)}")
    else:
        paths = spec_paths(args.spec)
    return [(load_spec(p), p) for p in paths]


def cmd_list(args, env: dict, session=None, gh_factory=None, run=subprocess.run,
             sleep=time.sleep) -> int:
    specs = select_specs(args, env)
    if not specs:
        log("No APPROVED specs selected. Nothing listed.")
        return 0
    bad = False
    for spec, p in specs:
        errs = validate_spec(spec, p, allow_waiting=bool(args.dry_run))
        if errs:
            bad = True
            log(f"[{spec.get('id', p.stem)}] spec problems:\n  - " + "\n  - ".join(errs))
    if bad:
        log("Fix the spec problems above. Nothing was sent to Etsy.")
        return 2
    if args.dry_run:
        log("DRY RUN: no Etsy calls, no secrets used. Plan:")
        for spec, _ in specs:
            log(plan_text(spec))
        return 0

    live = load_live()
    shops: dict[str, ShopSession] = {}
    results = []
    workdir = Path(env.get("RUNNER_TEMP") or tempfile.mkdtemp()) / "etsy-files"
    for spec, _ in specs:
        sid = spec["id"]
        try:
            if spec["shop"] not in shops:
                shops[spec["shop"]] = ShopSession(spec["shop"], env, session=session,
                                                  gh_factory=gh_factory)
            res = list_one(spec, shops[spec["shop"]], live, env, args.check, workdir,
                           run=run, sleep=sleep)
        except (EtsyError, SetupError) as exc:
            res = {"id": sid, "status": "failed", "note": str(exc)}
        res["by_hand"] = spec.get("by_hand", []) if res["status"] == "live" else []
        results.append(res)
        if res["status"] in ("live", "exists"):
            log(res["url"])
        else:
            log(f"[{sid}] {res['status']}: {res.get('note', '')}")
        if not args.check:
            save_live(live)
    if not args.check:
        save_live(live)

    rows = ["| ID | Result | URL / note |", "|----|--------|------------|"]
    for r in results:
        rows.append(f"| {r['id']} | {r['status']} | {r.get('url') or r.get('note', '')} |")
    hand = [f"- {r['id']}: {b}" for r in results for b in r["by_hand"]]
    summary(("## Etsy check (read-only)\n\n" if args.check else "## Etsy listings\n\n")
            + "\n".join(rows) + ("\n\n### BY HAND (Etsy's API can't do these)\n" + "\n".join(hand)
                                 if hand else "") + "\n")
    for line in hand:
        log("BY HAND " + line)
    return 1 if any(r["status"] == "failed" for r in results) else 0


def cmd_validate() -> int:
    paths = all_spec_paths()
    bad, waiting, batches = 0, 0, {}
    for p in paths:
        spec = load_spec(p)
        errs = validate_spec(spec, p, allow_waiting=True)
        waiting += spec.get("status") == WAITING
        batches.setdefault(spec_batch(spec), []).append(f"{spec.get('id')}"
                                                        + ("*" if spec.get("status") == WAITING else ""))
        if errs:
            bad += 1
            log(f"{p.name}:\n  - " + "\n  - ".join(errs))
    for b, ids in sorted(batches.items()):
        log(f"batch {b}: {', '.join(ids)}")
    log(f"{len(paths) - bad}/{len(paths)} specs OK ({waiting} WAITING approval, marked *)")
    return 1 if bad else 0


def cmd_approve(batch: str, said: str, at: str, go_path: Path | None = None) -> int:
    """Record the owner's approval of a batch: WAITING -> APPROVED, then write go.json."""
    if not str(said).strip() or not str(at).strip():
        raise SetupError("approve needs the owner's exact words (--said) and when (--at).")
    paths = batch_paths(batch)
    flipped = []
    for p in paths:
        spec = load_spec(p)
        if spec.get("status") == WAITING:
            rq = spec.get("approval", {}).get("review_queue", "")
            spec["status"] = "APPROVED"
            spec["approval"] = {"source": "claude/review-queue.md", "approved_by": "Dharma",
                                "approved_at": at.strip(), "quote": said.strip(), "review_queue": rq}
            p.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            flipped.append(spec["id"])
        errs = validate_spec(spec, p)
        if errs:
            raise SetupError(f"{p.name} is not listable after approval: {errs}")
    go_path = go_path or (LISTINGS / "go.json")
    go_path.write_text(json.dumps({"batch": batch, "owner_said": said.strip(), "at": at.strip()},
                                  indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    log(f"batch {batch}: approved {flipped or 'nothing new'}; wrote {go_path.name}. "
        f"Commit and push both to list them.")
    return 0


def cmd_store_secret(name: str, src: str, env: dict, gh_factory=None) -> int:
    if not re.fullmatch(r"[A-Z][A-Z0-9_]{2,}", name):
        raise SetupError("secret name must be UPPER_CASE")
    value = Path(src).read_text(encoding="utf-8")
    register_secret(value)
    github_secrets(env, gh_factory=gh_factory).put(name, value)
    log(f"Saved repo secret {name}.")
    return 0


def _which_hero(first: dict, new_img: Path, spec: dict) -> str:
    """Download Etsy's rank-1 image and say whether it matches the new square-safe hero or the old one."""
    try:
        import io, requests
        from PIL import Image, ImageChops, ImageStat
        url = first.get("url_570xN") or first.get("url_fullxfull")
        got = Image.open(io.BytesIO(requests.get(url, timeout=60).content)).convert("RGB").resize((200, 150))
        old = new_img.with_name(new_img.name.replace("-SQ.jpg", "")).with_suffix("")
        cands = {"NEW": new_img}
        for ext in (".jpg", ".png"):
            if Path(str(old) + ext).exists():
                cands["OLD"] = Path(str(old) + ext)
        score = {k: sum(ImageStat.Stat(ImageChops.difference(got, Image.open(v).convert("RGB").resize((200, 150)))).mean)
                 for k, v in cands.items()}
        return f"{min(score, key=score.get)} " + ", ".join(f"{k}={v:.0f}" for k, v in score.items())
    except Exception as exc:  # noqa: BLE001
        return f"unknown ({exc.__class__.__name__})"


def cmd_replace_hero(ids: list[str] | None, env: dict, session=None, gh_factory=None) -> int:
    """Replace image 1 (the thumbnail) of live listings with the spec's current photos[0] (Etsy overwrite at rank 1)."""
    live = load_live()
    shops: dict[str, ShopSession] = {}
    rows, failed = ["| ID | Result |", "|----|--------|"], False
    for sid, rec in live.get("listings", {}).items():
        if ids and sid not in ids:
            continue
        p = ROOT / "listings" / f"{sid}.json"
        spec = json.loads(p.read_text())
        img = ROOT / spec["photos"][0]
        try:
            if spec["shop"] not in shops:
                shops[spec["shop"]] = ShopSession(spec["shop"], env, session=session, gh_factory=gh_factory)
            ss = shops[spec["shop"]]
            ss.client.call("POST", f"/shops/{ss.shop_id}/listings/{rec['listing_id']}/images",
                           data={"rank": "1", "overwrite": "true"},
                           files={"image": (img.name, img.read_bytes(), _mime(img))})
            imgs = sorted(ss.client.images(rec["listing_id"]), key=lambda x: x.get("rank", 99))
            first = imgs[0] if imgs else {}
            rows.append(f"| {sid} | image 1 replaced ({img.name}); {len(imgs)} images |")
            log(f"[{sid}] image 1 replaced; {len(imgs)} images; rank1 id {first.get('listing_image_id')} "
                f"created {first.get('created_timestamp')}")
            print(f"::notice::{sid}: {len(imgs)} images; thumbnail now {_which_hero(first, img, spec)}", flush=True)
        except (EtsyError, SetupError) as exc:
            failed = True
            rows.append(f"| {sid} | FAILED: {redact(exc)} |")
            log(f"[{sid}] FAILED: {exc}")
    summary("## Etsy thumbnails\n\n" + "\n".join(rows) + "\n")
    return 1 if failed else 0


def cmd_sync_titles(ids: list[str] | None, env: dict, session=None, gh_factory=None) -> int:
    """Set the Etsy title of live listings to the spec's title, then read it back to confirm."""
    live = load_live()
    shops: dict[str, ShopSession] = {}
    rows, failed = ["| ID | Result |", "|----|--------|"], False
    for sid, rec in live.get("listings", {}).items():
        if ids and sid not in ids:
            continue
        spec = json.loads((ROOT / "listings" / f"{sid}.json").read_text())
        try:
            if spec["shop"] not in shops:
                shops[spec["shop"]] = ShopSession(spec["shop"], env, session=session, gh_factory=gh_factory)
            ss = shops[spec["shop"]]
            L = ss.client.listing(rec["listing_id"])
            if norm_title(L.get("title", "")) == norm_title(spec["title"]):
                rows.append(f"| {sid} | already matches |")
                print(f"::notice::{sid}: title already matches", flush=True)
                continue
            ss.client.update(ss.shop_id, rec["listing_id"], {"title": spec["title"]})
            got = ss.client.listing(rec["listing_id"]).get("title", "")
            ok = norm_title(got) == norm_title(spec["title"])
            failed |= not ok
            rows.append(f"| {sid} | {'title updated' if ok else 'MISMATCH: ' + got} |")
            print(f"::notice::{sid}: {'title updated' if ok else 'MISMATCH ' + got}", flush=True)
        except (EtsyError, SetupError) as exc:
            failed = True
            rows.append(f"| {sid} | FAILED: {redact(exc)} |")
            log(f"[{sid}] FAILED: {exc}")
    summary("## Etsy titles\n\n" + "\n".join(rows) + "\n")
    return 1 if failed else 0


def _plain(t: str) -> str:
    """Compare descriptions the way a buyer reads them (Etsy escapes HTML characters)."""
    import html
    return " ".join(html.unescape(html.unescape(t or "")).replace("\u2019", "'").split())


def cmd_sync_listing(ids: list[str], parts: set[str], photo_ranks: list[int], env: dict,
                     session=None, gh_factory=None, run: Callable = subprocess.run) -> int:
    """Bring LIVE listings in line with their spec after an approved fix.
    parts: "files" (upload the spec's customer files, then remove listing files whose names are not
    in the spec; nothing is removed unless every upload succeeded), "description" (PATCH the
    description), "photos" (overwrite the given photo ranks with the spec's photos)."""
    if not ids:
        raise SetupError("sync-listing needs explicit --spec IDs (never 'all').")
    live = load_live()
    shops: dict[str, ShopSession] = {}
    workdir = Path(env.get("RUNNER_TEMP") or tempfile.mkdtemp()) / "etsy-files"
    rows, failed = ["| ID | Result |", "|----|--------|"], False
    for sid in ids:
        rec = live.get("listings", {}).get(sid)
        try:
            if not rec:
                raise EtsyError("not in listings/live.json")
            spec = load_spec(ROOT / "listings" / f"{sid}.json")
            if spec["shop"] not in shops:
                shops[spec["shop"]] = ShopSession(spec["shop"], env, session=session, gh_factory=gh_factory)
            ss = shops[spec["shop"]]
            c, lid, done = ss.client, int(rec["listing_id"]), []
            if "files" in parts:
                want = decrypt_files(spec, env.get("ETSY_FILES_AGE_KEY", ""), workdir / sid, run=run)
                have = c.files(ss.shop_id, lid)
                have_names = {f.get("filename") for f in have}
                for i, (path, name) in enumerate(want):
                    if name not in have_names:
                        c.upload_file(ss.shop_id, lid, path, name, i + 1)
                after = c.files(ss.shop_id, lid)
                names = {f.get("filename") for f in after}
                missing = [n for _, n in want if n not in names]
                if missing:
                    raise EtsyError(f"upload not visible on Etsy: {missing}; old files left in place")
                keep = {n for _, n in want}
                for f in after:
                    if f.get("filename") not in keep:
                        c.call("DELETE", f"/shops/{ss.shop_id}/listings/{lid}/files/{f['listing_file_id']}")
                final = sorted(f.get("filename") for f in c.files(ss.shop_id, lid))
                if final != sorted(keep):
                    raise EtsyError(f"files now {final}, expected {sorted(keep)}")
                done.append("files=" + ",".join(final))
            if "description" in parts:
                c.update(ss.shop_id, lid, {"description": description_for(spec, ss.currency)})
                got = c.listing(lid).get("description", "")
                if _plain(got) != _plain(description_for(spec, ss.currency)):
                    raise EtsyError(f"description did not update (Etsy starts: {_plain(got)[:80]!r})")
                done.append("description")
            if "photos" in parts:
                for r in photo_ranks:
                    img = ROOT / spec["photos"][r - 1]
                    c.call("POST", f"/shops/{ss.shop_id}/listings/{lid}/images",
                           data={"rank": str(r), "overwrite": "true"},
                           files={"image": (img.name, img.read_bytes(), _mime(img))})
                done.append("photos " + ",".join(map(str, photo_ranks)))
            rows.append(f"| {sid} | {'; '.join(done)} |")
            print(f"::notice::{sid}: {'; '.join(done)}", flush=True)
        except (EtsyError, SetupError) as exc:
            failed = True
            rows.append(f"| {sid} | FAILED: {redact(exc)} |")
            print(f"::error::{sid}: {redact(exc)}", flush=True)
    summary("## Etsy listing sync\n\n" + "\n".join(rows) + "\n")
    return 1 if failed else 0


def spec_ids(text: str) -> list[str]:
    """'SF-AIGOV', 'SF-AIGOV,FF-FREEDOM' or 'listings/SF-AIGOV.json' -> ['SF-AIGOV', ...]; 'all' is dropped."""
    out = []
    for x in text.replace(",", " ").split():
        x = x.strip()
        if x.startswith("listings/"):
            x = x[len("listings/"):]
        if x.endswith(".json"):
            x = x[:-len(".json")]
        if x and x != "all":
            out.append(x)
    return out


def cmd_set_state(ids: list[str], state: str, env: dict, session=None, gh_factory=None) -> int:
    """deactivate (state "inactive") or reactivate (state "active") LIVE listings, named one by one.
    Reversible: an inactive listing keeps its photos, files and URL, and Etsy charges nothing to
    reactivate it before its 4-month period ends (Etsy Help 360000336187). Nothing is deleted.
    reactivate only undoes a deactivate: it refuses drafts, expired or sold-out listings."""
    if state not in ("inactive", "active"):
        raise SetupError(f"unknown state {state!r}")
    if not ids:
        raise SetupError("deactivate/reactivate need explicit --spec IDs (never 'all').")
    live = load_live()
    shops: dict[str, ShopSession] = {}
    rows, failed, changed = ["| ID | Result |", "|----|--------|"], False, False
    for sid in ids:
        rec = live.get("listings", {}).get(sid)
        try:
            if not rec:
                raise EtsyError("not in listings/live.json")
            spec = load_spec(ROOT / "listings" / f"{sid}.json")
            if spec["shop"] not in shops:
                shops[spec["shop"]] = ShopSession(spec["shop"], env, session=session, gh_factory=gh_factory)
            ss = shops[spec["shop"]]
            c, lid = ss.client, int(rec["listing_id"])
            before = c.listing(lid).get("state")
            if before == state:
                rows.append(f"| {sid} | already {state} |")
            else:
                if state == "active" and before != "inactive":
                    raise EtsyError(f"listing is '{before}', not 'inactive': reactivate only undoes a deactivate")
                if state == "inactive" and before != "active":
                    raise EtsyError(f"listing is '{before}', not 'active': nothing to deactivate")
                c.update(ss.shop_id, lid, {"state": state})
                got = c.listing(lid).get("state")
                if got != state:
                    raise EtsyError(f"Etsy still shows state '{got}' after the change")
                rows.append(f"| {sid} | {before} -> {state} |")
            if state == "inactive":
                rec["state"] = "inactive"
                rec.setdefault("deactivated_at", now_iso())
            else:
                rec.pop("state", None)
                rec.pop("deactivated_at", None)
            changed = True
            print(f"::notice::{sid}: {rows[-1].split('|')[2].strip()}", flush=True)
        except (EtsyError, SetupError) as exc:
            failed = True
            rows.append(f"| {sid} | FAILED: {redact(exc)} |")
            print(f"::error::{sid}: {redact(exc)}", flush=True)
    if changed:
        save_live(live)
    summary(("## Etsy deactivate\n\n" if state == "inactive" else "## Etsy reactivate\n\n")
            + "\n".join(rows) + "\n")
    return 1 if failed else 0


OPS_PATH = LISTINGS / "ops" / "queue.json"
OPS_DONE_PATH = LISTINGS / "ops" / "done.json"
OPS_ALLOWED = {"deactivate", "reactivate", "sync"}
OPS_SYNC_PARTS = {"description"}


def cmd_ops(env: dict, session=None, gh_factory=None) -> int:
    """Run the routine, reversible operations queued in listings/ops/queue.json (pushed by an agent or a person),
    each exactly once (ids recorded in listings/ops/done.json). Allowed: deactivate / reactivate named live
    listings, and sync with parts "description" only. Anything else (listing, files, photos, prices,
    deletion) is refused, so a push can never publish a new listing or swap customer files.
    ops.json: {"ops": [{"id": "...", "action": "deactivate", "spec": "SF-AIGOV", "reason": "..."}, ...]}"""
    if not OPS_PATH.exists():
        print("No listings/ops/queue.json; nothing to do.")
        return 0
    ops = json.loads(OPS_PATH.read_text()).get("ops", [])
    done = json.loads(OPS_DONE_PATH.read_text()) if OPS_DONE_PATH.exists() else {"done": []}
    done_ids = {d["id"] for d in done["done"]}
    failed = False
    rows = ["| Op | Action | Result |", "|----|--------|--------|"]
    for op in ops:
        oid, action, spec = op.get("id"), op.get("action"), op.get("spec", "")
        if not oid or oid in done_ids:
            continue
        if action not in OPS_ALLOWED:
            failed = True
            rows.append(f"| {oid} | {action} | REFUSED: only {sorted(OPS_ALLOWED)} are allowed here |")
            continue
        ids = spec_ids(spec)
        if not ids:
            failed = True
            rows.append(f"| {oid} | {action} | REFUSED: needs explicit spec IDs |")
            continue
        if action == "sync":
            parts = {x.strip() for x in str(op.get("parts", "")).split(",") if x.strip()}
            if not parts or not parts <= OPS_SYNC_PARTS:
                failed = True
                rows.append(f"| {oid} | sync | REFUSED: parts must be {sorted(OPS_SYNC_PARTS)} |")
                continue
            rc = cmd_sync_listing(ids, parts, [], env, session=session, gh_factory=gh_factory)
        else:
            rc = cmd_set_state(ids, "inactive" if action == "deactivate" else "active", env,
                               session=session, gh_factory=gh_factory)
        if rc == 0:
            done["done"].append({"id": oid, "action": action, "spec": ",".join(ids), "at": now_iso()})
            done_ids.add(oid)
            rows.append(f"| {oid} | {action} | done |")
        else:
            failed = True
            rows.append(f"| {oid} | {action} | FAILED (will retry on the next push) |")
    OPS_DONE_PATH.write_text(json.dumps(done, indent=2, ensure_ascii=False) + "\n")
    summary("## Etsy ops\n\n" + "\n".join(rows) + "\n")
    return 1 if failed else 0


def main(argv: list[str] | None = None, env: dict | None = None, **kw) -> int:
    ap = argparse.ArgumentParser(description="Steadfold Etsy auto-lister")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for c in ("auth-start", "auth-finish"):
        s = sub.add_parser(c)
        s.add_argument("--shop", required=True, choices=list(SHOPS))
    s = sub.add_parser("list")
    g = s.add_mutually_exclusive_group(required=True)
    g.add_argument("--spec")
    g.add_argument("--go")
    m = s.add_mutually_exclusive_group()
    m.add_argument("--dry-run", action="store_true")
    m.add_argument("--check", action="store_true")
    sub.add_parser("validate")
    s = sub.add_parser("replace-hero")
    s.add_argument("--spec", default="")
    s = sub.add_parser("sync-titles")
    s.add_argument("--spec", default="")
    s = sub.add_parser("sync-listing")
    s.add_argument("--spec", required=True)
    s.add_argument("--parts", default="files,description")
    s.add_argument("--photos", default="")
    for c in ("deactivate", "reactivate"):
        s = sub.add_parser(c)
        s.add_argument("--spec", required=True)
    sub.add_parser("ops")
    s = sub.add_parser("approve")
    s.add_argument("--batch", required=True)
    s.add_argument("--said", required=True)
    s.add_argument("--at", required=True)
    s = sub.add_parser("store-secret")
    s.add_argument("--name", required=True)
    s.add_argument("--from-file", required=True)
    s = sub.add_parser("encrypt")
    s.add_argument("--src", required=True)
    s.add_argument("--dest", required=True)
    args = ap.parse_args(argv)
    env = dict(os.environ if env is None else env)
    global SUMMARY_FILE
    SUMMARY_FILE = env.get("GITHUB_STEP_SUMMARY") or None
    try:
        if args.cmd == "auth-start":
            return cmd_auth_start(args.shop, env, gh_factory=kw.get("gh_factory"))
        if args.cmd == "auth-finish":
            return cmd_auth_finish(args.shop, env, session=kw.get("session"),
                                   gh_factory=kw.get("gh_factory"))
        if args.cmd == "list":
            return cmd_list(args, env, **kw)
        if args.cmd == "replace-hero":
            ids = spec_ids(args.spec)
            return cmd_replace_hero(ids or None, env, session=kw.get("session"), gh_factory=kw.get("gh_factory"))
        if args.cmd == "sync-titles":
            ids = spec_ids(args.spec)
            return cmd_sync_titles(ids or None, env, session=kw.get("session"), gh_factory=kw.get("gh_factory"))
        if args.cmd == "sync-listing":
            ids = spec_ids(args.spec)
            parts = {x.strip() for x in args.parts.split(",") if x.strip()}
            ranks = [int(x) for x in args.photos.replace(",", " ").split() if x.strip()]
            return cmd_sync_listing(ids, parts, ranks, env, session=kw.get("session"),
                                    gh_factory=kw.get("gh_factory"))
        if args.cmd == "ops":
            return cmd_ops(env, session=kw.get("session"), gh_factory=kw.get("gh_factory"))
        if args.cmd in ("deactivate", "reactivate"):
            return cmd_set_state(spec_ids(args.spec), "inactive" if args.cmd == "deactivate" else "active",
                                 env, session=kw.get("session"), gh_factory=kw.get("gh_factory"))
        if args.cmd == "validate":
            return cmd_validate()
        if args.cmd == "approve":
            return cmd_approve(args.batch, args.said, args.at)
        if args.cmd == "store-secret":
            return cmd_store_secret(args.name, args.from_file, env, gh_factory=kw.get("gh_factory"))
        if args.cmd == "encrypt":
            info = encrypt_file(Path(args.src), ROOT / args.dest, PUBKEY_PATH.read_text())
            print(json.dumps(info, indent=2))
            return 0
    except (SetupError, EtsyError) as exc:
        log(f"ERROR: {exc}")
        summary(f"**Stopped:** {redact(exc)}")
        return 2
    return 1


if __name__ == "__main__":
    sys.exit(main())

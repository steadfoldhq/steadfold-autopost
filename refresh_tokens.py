#!/usr/bin/env python3
"""
Steadfold Autopost: keep the three Instagram tokens alive.

Instagram Login long-lived tokens last 60 days. Refreshing one (it must be at
least 24 hours old and not yet expired) gives a token that is valid for another
60 days. This script runs weekly in GitHub Actions
(.github/workflows/refresh-tokens.yml) and, for each account:

  1. calls GET https://graph.instagram.com/refresh_access_token
         ?grant_type=ig_refresh_token&access_token=<current token>
  2. checks the new token still belongs to the right @username,
  3. saves it back into the repo's GitHub Actions secret (IG_TOKEN_...) through
     the GitHub REST API. GitHub requires secret values to be encrypted with the
     repo's public key using a libsodium "sealed box" (PyNaCl).

Needs these environment variables (all set from repo secrets by the workflow):
  IG_TOKEN_FULLYFUNDED, IG_TOKEN_LOCKEDHOUR, IG_TOKEN_HOURBACK
  GH_PAT            a GitHub token allowed to write this repo's Actions secrets
  GITHUB_REPOSITORY owner/repo (GitHub sets this automatically)

Tokens are never printed.
"""

from __future__ import annotations

import argparse
import base64
import os
import sys
from typing import Any, Callable

import requests

from autopost import ACCOUNTS, IGClient, IGError, log, register_secret

REFRESH_URL = "https://graph.instagram.com/refresh_access_token"
GITHUB_API = "https://api.github.com"
GITHUB_HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "steadfold-autopost",
}


def seal(public_key_b64: str, value: str) -> str:
    """Encrypt a secret value the way GitHub requires (libsodium sealed box)."""
    from nacl import encoding, public  # imported here so tests can run without PyNaCl

    key = public.PublicKey(public_key_b64.encode("utf-8"), encoding.Base64Encoder())
    sealed = public.SealedBox(key).encrypt(value.encode("utf-8"))
    return base64.b64encode(sealed).decode("utf-8")


class GitHubSecrets:
    """Writes repository Actions secrets through the GitHub REST API."""

    def __init__(self, repo: str, pat: str, session: Any = None,
                 encrypt: Callable[[str, str], str] = seal):
        register_secret(pat)
        self.repo = repo
        self._pat = pat
        self.session = session or requests.Session()
        self.encrypt = encrypt
        self._key: dict | None = None

    def _headers(self) -> dict:
        return {**GITHUB_HEADERS, "Authorization": f"Bearer {self._pat}"}

    def public_key(self) -> dict:
        if self._key is None:
            url = f"{GITHUB_API}/repos/{self.repo}/actions/secrets/public-key"
            r = self.session.request("GET", url, headers=self._headers(), timeout=30)
            if r.status_code != 200:
                raise RuntimeError(
                    f"GitHub: can't read the repo's secrets public key (HTTP {r.status_code}). "
                    f"Check that GH_PAT is set, not expired, and has 'Secrets: read and write' "
                    f"for {self.repo}.")
            self._key = r.json()
        return self._key

    def put(self, name: str, value: str) -> None:
        key = self.public_key()
        body = {"encrypted_value": self.encrypt(key["key"], value), "key_id": key["key_id"]}
        url = f"{GITHUB_API}/repos/{self.repo}/actions/secrets/{name}"
        r = self.session.request("PUT", url, headers=self._headers(), json=body, timeout=30)
        if r.status_code not in (201, 204):
            raise RuntimeError(f"GitHub: saving secret {name} failed (HTTP {r.status_code})")


def refresh_token(token: str, session: Any) -> tuple[str, int]:
    """Return (new_token, expires_in_seconds)."""
    try:
        r = session.request("GET", REFRESH_URL,
                            params={"grant_type": "ig_refresh_token", "access_token": token},
                            timeout=60)
    except requests.RequestException as exc:
        raise IGError(f"refresh: network error: {exc}", network=True) from None
    body = IGClient._handle("GET", "refresh_access_token", r)
    new = str(body.get("access_token") or "")
    if not new:
        raise IGError("refresh: response had no access_token")
    register_secret(new)
    return new, int(body.get("expires_in") or 0)


def main(argv: list[str] | None = None, *, session: Any = None, env: dict | None = None,
         encrypt: Callable[[str, str], str] = seal) -> int:
    ap = argparse.ArgumentParser(description="Refresh Instagram tokens and update GitHub secrets")
    ap.add_argument("--dry-run", action="store_true",
                    help="only check that tokens and GH_PAT work; refresh and save nothing")
    args = ap.parse_args(argv)

    env = dict(os.environ if env is None else env)
    session = session or requests.Session()
    for info in ACCOUNTS.values():
        register_secret(env.get(info["token_env"]))
    repo = (env.get("GITHUB_REPOSITORY") or "").strip()
    pat = (env.get("GH_PAT") or "").strip()
    if not repo or not pat:
        log("ERROR: GITHUB_REPOSITORY and GH_PAT must both be set")
        return 2
    gh = GitHubSecrets(repo, pat, session=session, encrypt=encrypt)

    problems: list[str] = []
    try:
        gh.public_key()  # fail early (before refreshing anything) if GH_PAT can't write
        log(f"GitHub access OK for {repo}")
    except RuntimeError as exc:
        log(f"ERROR: {exc}")
        return 1

    for key, info in ACCOUNTS.items():
        name, want = info["token_env"], info["username"]
        token = (env.get(name) or "").strip()
        if not token:
            log(f"skip {name}: not set")
            continue
        try:
            if args.dry_run:
                me = IGClient(token, session).me()
                ok = me["username"].lower() == want.lower()
                log(f"{name}: current token works for @{me['username']}"
                    + ("" if ok else f" (EXPECTED @{want})"))
                if not ok:
                    problems.append(f"{name} belongs to @{me['username']}, expected @{want}")
                continue
            new, expires_in = refresh_token(token, session)
            me = IGClient(new, session).me()
            if me["username"].lower() != want.lower():
                problems.append(f"{name}: refreshed token belongs to @{me['username']}, "
                                f"expected @{want}; secret NOT updated")
                log(f"ERROR: {problems[-1]}")
                continue
            gh.put(name, new)
            log(f"{name}: refreshed for @{me['username']}, valid ~{expires_in // 86400} "
                f"days; GitHub secret updated")
        except (IGError, RuntimeError) as exc:
            problems.append(f"{name}: {exc}")
            log(f"ERROR: {name}: {exc}")

    if problems:
        log(f"FINISHED WITH {len(problems)} PROBLEM(S). If a token has expired, make a new "
            f"one in the Meta app dashboard and paste it into the GitHub secret (README, "
            f"step 9).")
        return 1
    log("All tokens OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

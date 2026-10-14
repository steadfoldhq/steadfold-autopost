"""Tests for refresh_tokens.py (Instagram + GitHub APIs simulated, no network)."""

from __future__ import annotations

import base64
import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import refresh_tokens  # noqa: E402
from fakes import FakeGraph, FakeResponse  # noqa: E402

OLD = {"IG_TOKEN_FULLYFUNDED": "IGAAoldFF0001", "IG_TOKEN_LOCKEDHOUR": "IGAAoldLH0002",
       "IG_TOKEN_HOURBACK": "IGAAoldHB0003"}
NEW = {"IGAAoldFF0001": "IGAAnewFF1001", "IGAAoldLH0002": "IGAAnewLH1002",
       "IGAAoldHB0003": "IGAAnewHB1003"}
PAT = "github_pat_SECRET_123456"


class FakeWorld(FakeGraph):
    """Instagram + GitHub in one fake session."""

    def __init__(self, tokens):
        super().__init__(tokens)
        self.secrets: dict[str, dict] = {}
        self.gh_status = 200

    def request(self, method, url, params=None, data=None, json=None, headers=None,
                timeout=None, allow_redirects=True):
        if url.startswith("https://api.github.com/"):
            from fakes import Call
            self.calls.append(Call(method, url, {}, {}, json, dict(headers or {})))
            assert headers["Authorization"] == f"Bearer {PAT}"
            if url.endswith("/actions/secrets/public-key"):
                if self.gh_status != 200:
                    return FakeResponse(self.gh_status, {"message": "Bad credentials"})
                return FakeResponse(200, {"key_id": "KEY123", "key": "cHVibGlja2V5"})
            name = url.rsplit("/", 1)[-1]
            self.secrets[name] = json
            return FakeResponse(201, {})
        return super().request(method, url, params, data, json, headers, timeout)


def fake_encrypt(key_b64: str, value: str) -> str:
    return base64.b64encode(f"sealed[{key_b64}]{value[::-1]}".encode()).decode()


def world(**usernames):
    names = {"FF": "fullyfundedhq", "LH": "lockedhourhq", "HB": "hourbackhq", **usernames}
    tokens = {}
    for old, new in NEW.items():
        short = old[7:9]
        tokens[old] = ("1784" + short, names[short])
        tokens[new] = ("1784" + short, names[short])
    w = FakeWorld(tokens)
    w.refresh_map = dict(NEW)
    return w


class RefreshTests(unittest.TestCase):
    def run_main(self, w, *args, env=None):
        out = io.StringIO()
        e = {**OLD, "GH_PAT": PAT, "GITHUB_REPOSITORY": "dharma/steadfold-autopost"}
        if env is not None:
            e = env
        with contextlib.redirect_stdout(out):
            code = refresh_tokens.main(list(args), session=w, env=e, encrypt=fake_encrypt)
        self.output = out.getvalue()
        return code

    def test_refresh_and_store_all_three(self):
        w = world()
        self.assertEqual(self.run_main(w), 0, self.output)
        self.assertEqual(sorted(w.secrets), sorted(OLD))
        for name, old in OLD.items():
            body = w.secrets[name]
            self.assertEqual(body["key_id"], "KEY123")
            decoded = base64.b64decode(body["encrypted_value"]).decode()
            self.assertEqual(decoded, f"sealed[cHVibGlja2V5]{NEW[old][::-1]}")
        refreshes = [c for c in w.calls if c.path == "refresh_access_token"]
        self.assertEqual(len(refreshes), 3)
        self.assertEqual(refreshes[0].params["grant_type"], "ig_refresh_token")
        for secret in list(OLD.values()) + list(NEW.values()) + [PAT]:
            self.assertNotIn(secret, self.output)

    def test_wrong_username_is_not_saved(self):
        w = world(LH="impostor")
        self.assertEqual(self.run_main(w), 1)
        self.assertNotIn("IG_TOKEN_LOCKEDHOUR", w.secrets)
        self.assertIn("IG_TOKEN_FULLYFUNDED", w.secrets)
        self.assertIn("NOT updated", self.output)

    def test_bad_pat_stops_before_refreshing(self):
        w = world()
        w.gh_status = 401
        self.assertEqual(self.run_main(w), 1)
        self.assertEqual([c for c in w.calls if c.path == "refresh_access_token"], [])
        self.assertIn("GH_PAT", self.output)

    def test_expired_token_reported(self):
        w = world()
        w.refresh_map.pop("IGAAoldHB0003")
        self.assertEqual(self.run_main(w), 1)
        self.assertIn("IG_TOKEN_HOURBACK", self.output)
        self.assertEqual(len(w.secrets), 2)

    def test_dry_run_changes_nothing(self):
        w = world()
        self.assertEqual(self.run_main(w, "--dry-run"), 0, self.output)
        self.assertEqual(w.secrets, {})
        self.assertEqual([c for c in w.calls if c.path == "refresh_access_token"], [])

    def test_missing_pat(self):
        self.assertEqual(self.run_main(world(), env=dict(OLD)), 2)


@unittest.skipUnless(__import__("importlib").util.find_spec("nacl"), "PyNaCl not installed")
class RealSealedBox(unittest.TestCase):
    def test_seal_round_trip(self):
        from nacl import encoding, public
        sk = public.PrivateKey.generate()
        pk_b64 = sk.public_key.encode(encoding.Base64Encoder()).decode()
        sealed = refresh_tokens.seal(pk_b64, "hello-token")
        plain = public.SealedBox(sk).decrypt(base64.b64decode(sealed))
        self.assertEqual(plain, b"hello-token")


if __name__ == "__main__":
    unittest.main()

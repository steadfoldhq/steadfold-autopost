"""Tests for tools/etsy.py: spec validation, the no-network dry run, OAuth PKCE,
and the full listing flow against a fake Etsy + fake GitHub (no network)."""

from __future__ import annotations

import base64
import contextlib
import hashlib
import io
import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import etsy  # noqa: E402
from fakes import FakeResponse  # noqa: E402

KEY, SHARED = "abcd1234keystring", "sharedSECRETvalue99"
RT_OLD, RT_NEW, AT = "111.refreshOLDtoken000", "111.refreshNEWtoken999", "111.accessTOKENabcdef"
PAT = "github_pat_SECRET_etsy_123"
SPEC_IDS = ["DP-CALM-P", "DP-CALM-T", "FF-HMP", "FF-MPB", "FF-MSP", "DP-RIV",
            "LBM1", "LBP-SET", "LBP4", "LBP1", "LBP2", "LBP3"]


def real_spec(sid: str) -> dict:
    return etsy.load_spec(etsy.LISTINGS / f"{sid}.json")


class NoNetwork:
    def request(self, *a, **k):
        raise AssertionError("network used in a dry run")


class FakeGH:
    def __init__(self):
        self.secrets: dict[str, str] = {}

    def factory(self, repo, pat):
        assert pat == PAT
        return self

    def put(self, name, value):
        self.secrets[name] = value


class FakeEtsy:
    """Just enough of api.etsy.com for the lister."""

    def __init__(self, shop_name="SteadfoldHQ", currency="USD", existing=None, reject_when_made=()):
        self.shop_name, self.currency = shop_name, currency
        self.listings: dict[int, dict] = {}
        self.calls: list[tuple[str, str]] = []
        self.next_id = 5000
        self.reject_when_made = set(reject_when_made)
        for L in existing or []:
            self.listings[L["listing_id"]] = dict(L, images=[], videos=[], files=[])

    def request(self, method, url, params=None, data=None, files=None, headers=None, timeout=None,
                **kw):
        path = urlparse(url).path
        self.calls.append((method, path))
        assert headers["x-api-key"] == f"{KEY}:{SHARED}"
        if url == etsy.TOKEN_URL:
            if data["grant_type"] == "refresh_token":
                assert data["refresh_token"] == RT_OLD
            else:
                assert data["code_verifier"] and data["code"] == "ONEtimeCODE123"
            return FakeResponse(200, {"access_token": AT, "refresh_token": RT_NEW,
                                      "expires_in": 3600, "token_type": "Bearer"})
        if path != "/v3/application/seller-taxonomy/nodes":
            assert headers.get("Authorization") == f"Bearer {AT}"
        p = path.replace("/v3/application", "")
        if p == "/users/me":
            return FakeResponse(200, {"user_id": 111, "shop_id": 42})
        if p == "/shops/42":
            return FakeResponse(200, {"shop_id": 42, "shop_name": self.shop_name,
                                      "currency_code": self.currency})
        if p == "/seller-taxonomy/nodes":
            return FakeResponse(200, {"results": [
                {"id": 1, "name": "Paper & Party Supplies", "children": [
                    {"id": 2, "name": "Paper", "children": [
                        {"id": 3, "name": "Calendars & Planners", "children": []}]}]},
                {"id": 10, "name": "Art & Collectibles", "children": [
                    {"id": 11, "name": "Prints", "children": [
                        {"id": 12, "name": "Digital Prints", "children": []}]}]}]})
        m = re.fullmatch(r"/shops/42/listings", p)
        if m and method == "GET":
            res = [L for L in self.listings.values() if L["state"] == params["state"]]
            return FakeResponse(200, {"count": len(res), "results": res})
        if m and method == "POST":
            if data["when_made"] in self.reject_when_made:
                return FakeResponse(400, {"error": "when_made must be one of ..."})
            lid = self.next_id
            self.next_id += 1
            self.listings[lid] = {"listing_id": lid, "state": "draft", "title": data["title"],
                                  "fields": dict(data), "images": [], "videos": [], "files": [],
                                  "price": {"amount": int(round(float(data["price"]) * 100)),
                                            "divisor": 100, "currency_code": self.currency}}
            return FakeResponse(201, {"listing_id": lid, "state": "draft"})
        m = re.fullmatch(r"/shops/42/listings/(\d+)(?:/(images|videos|files))?", p)
        if m:
            L = self.listings[int(m.group(1))]
            kind = m.group(2)
            if method == "PATCH":
                if data.get("state") == "active":
                    assert L["images"] and L["files"], "activated without images/files"
                    L["state"] = "active"
                    L["url"] = f"https://www.etsy.com/listing/{L['listing_id']}/x?utm=1"
                L["fields"].update({k: v for k, v in data.items() if k != "state"})
                return FakeResponse(200, {"listing_id": L["listing_id"]})
            if method == "POST":
                part = {"images": "image", "videos": "video", "files": "file"}[kind]
                assert part in files
                L[kind].append({"name": (data or {}).get("name") or files[part][0],
                                "filename": (data or {}).get("name") or files[part][0]})
                return FakeResponse(201, {"ok": True})
            if method == "GET" and kind == "files":
                return FakeResponse(200, {"results": L["files"]})
        m = re.fullmatch(r"/listings/(\d+)(?:/(images|videos))?", p)
        if m and method == "GET":
            L = self.listings[int(m.group(1))]
            if m.group(2):
                return FakeResponse(200, {"results": L[m.group(2)]})
            return FakeResponse(200, {k: v for k, v in L.items() if k not in ("images", "videos", "files")})
        return FakeResponse(404, {"error": f"no route {method} {p}"})


def base_env(**extra):
    env = {"ETSY_KEYSTRING": KEY, "ETSY_SHARED_SECRET": SHARED, "GH_PAT": PAT,
           "GITHUB_REPOSITORY": "steadfoldhq/steadfold-autopost",
           "ETSY_REFRESH_TOKEN_STEADFOLD": RT_OLD, "ETSY_REFRESH_TOKEN_LITTLEFOLD": RT_OLD,
           "ETSY_FILES_AGE_KEY": "AGE-SECRET-KEY-1FAKEFAKEFAKE"}
    env.update(extra)
    return env


class SpecValidation(unittest.TestCase):
    def test_every_repo_spec_is_valid_and_approved(self):
        paths = sorted(p for p in etsy.LISTINGS.glob("*.json") if p.name not in ("live.json", "go.json"))
        self.assertEqual(sorted(p.stem for p in paths), sorted(SPEC_IDS))
        for p in paths:
            with self.subTest(spec=p.name):
                self.assertEqual(etsy.validate_spec(etsy.load_spec(p), p), [])

    def test_no_unencrypted_customer_files_in_repo(self):
        for f in (ROOT / "listings" / "files").rglob("*"):
            if f.is_file():
                self.assertTrue(f.name.endswith(".age"), f)
                self.assertTrue(f.read_bytes().startswith(b"age-encryption.org/v1"), f)
        for base in (ROOT / "listings", ROOT / "keys"):
            for f in base.rglob("*"):
                self.assertNotIn(f.suffix.lower(), (".zip", ".pdf", ".xlsx", ".ics", ".key"), f)
        pub = (ROOT / "keys" / "etsy-files.pub").read_text().strip()
        self.assertTrue(pub.startswith("age1") and "SECRET" not in pub.upper())

    def test_each_spec_matches_its_prompt_rules(self):
        s = real_spec("DP-CALM-P")
        self.assertEqual(len(s["photos"]), 10)
        self.assertEqual(len(s["files"]), 5)
        self.assertEqual(s["price"], {"USD": 16.0, "CAD": 22.0})
        self.assertTrue(s["description"].endswith("• Launch sale: 25% off until 30 Nov 2026. Regular price US$16."))
        self.assertEqual(real_spec("DP-RIV")["price"], {"CAD": 14.99})
        self.assertNotIn("video", real_spec("FF-MSP"))          # the kit video shows the bundle
        self.assertEqual(len(real_spec("FF-MSP")["photos"]), 8)
        for sid in ("LBM1", "LBP-SET", "LBP1", "LBP2", "LBP3", "LBP4"):
            s = real_spec(sid)
            self.assertIn("ONEGLANCE", s["photos"][0])
            self.assertEqual(list(s["price"]), ["CAD"])
        for sid in SPEC_IDS:
            self.assertEqual(len(real_spec(sid)["tags"]), 13, sid)

    def test_cad_description_override(self):
        s = real_spec("FF-HMP")
        self.assertIn("then CA$19", etsy.description_for(s, "CAD"))
        self.assertNotIn("then CA$19", etsy.description_for(s, "USD"))

    def bad(self, **changes):
        s = json.loads(json.dumps(real_spec("LBP4")))
        for k, v in changes.items():
            if v is None:
                s.pop(k, None)
            else:
                s[k] = v
        return etsy.validate_spec(s, etsy.LISTINGS / "LBP4.json")

    def test_rejects_unapproved(self):
        self.assertTrue(self.bad(status="WAITING"))
        self.assertTrue(self.bad(approval={"source": "somewhere-else.txt", "approved_by": "x",
                                           "approved_at": "y", "quote": "z"}))
        self.assertTrue(self.bad(approval=None))

    def test_rejects_plain_customer_file(self):
        f = dict(real_spec("LBP4")["files"][0], enc="listings/files/littlefold-drop01/LBP4-little-tree.zip")
        self.assertTrue(any("encrypted" in e for e in self.bad(files=[f])))
        f2 = dict(real_spec("LBP4")["files"][0], enc="../secret.zip.age")
        self.assertTrue(self.bad(files=[f2]))

    def test_rejects_etsy_limit_breaks(self):
        self.assertTrue(self.bad(tags=[f"tag {i}" for i in range(14)]))
        self.assertTrue(self.bad(tags=["this tag is far too long for etsy"]))
        self.assertTrue(self.bad(tags=["dup", "Dup"]))
        self.assertTrue(self.bad(title="A: B: C"))
        self.assertTrue(self.bad(title="x" * 141))
        self.assertTrue(self.bad(files=[real_spec("LBP4")["files"][0]] * 6))
        self.assertTrue(self.bad(photos=["README.md"]))
        self.assertTrue(self.bad(price={"EUR": 5}))
        self.assertTrue(self.bad(quantity=0))

    def test_littlefold_words_rule(self):
        errs = self.bad(description=real_spec("LBP4")["description"] + " Safe for babies.")
        self.assertTrue(any("Littlefold" in e for e in errs))
        self.assertFalse(self.bad())   # "sleepy" is fine; whole words only


class DryRun(unittest.TestCase):
    def test_dry_run_calls_nothing_and_needs_no_secrets(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = etsy.main(["list", "--spec", "all", "--dry-run"], env={}, session=NoNetwork())
        self.assertEqual(rc, 0)
        text = out.getvalue()
        for sid in SPEC_IDS:
            self.assertIn(f"[{sid}]", text)
        self.assertIn("CALMLAUNCH", text)

    def test_go_file_needs_owner_words(self):
        with tempfile.TemporaryDirectory() as d:
            go = Path(d) / "go.json"
            go.write_text(json.dumps({"ids": ["LBP4"]}))
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(etsy.main(["list", "--go", str(go), "--dry-run"], env={}), 2)
            go.write_text(json.dumps({"ids": ["NOPE"], "owner_said": "list approved", "at": "now"}))
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(etsy.main(["list", "--go", str(go), "--dry-run"], env={}), 2)
            go.write_text(json.dumps({"ids": "all", "owner_said": "list approved", "at": "now"}))
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(etsy.main(["list", "--go", str(go), "--dry-run"], env={}), 0)


class OAuth(unittest.TestCase):
    def test_pkce(self):
        v, c = etsy.pkce_pair()
        self.assertTrue(43 <= len(v) <= 128 and re.fullmatch(r"[A-Za-z0-9._~\-]+", v))
        want = base64.urlsafe_b64encode(hashlib.sha256(v.encode()).digest()).decode().rstrip("=")
        self.assertEqual(c, want)

    def test_authorize_url(self):
        url = etsy.authorize_url(KEY, etsy.DEFAULT_REDIRECT, "CHAL", "STATE")
        self.assertNotIn(KEY, url)            # survives GitHub's secret masking
        q = parse_qs(urlparse(url).query)
        self.assertEqual(q["client_id"], [KEY])
        self.assertEqual(q["redirect_uri"], [etsy.DEFAULT_REDIRECT])
        self.assertEqual(q["scope"], ["listings_r listings_w shops_r"])
        self.assertEqual(q["code_challenge_method"], ["S256"])
        self.assertNotIn(SHARED, unquote(url))

    def test_parse_code(self):
        self.assertEqual(etsy.parse_code("https://github.com/steadfoldhq/steadfold-autopost?code=ONEtimeCODE123&state=S1"),
                         ("ONEtimeCODE123", "S1"))
        self.assertEqual(etsy.parse_code("  ONEtimeCODE123 "), ("ONEtimeCODE123", None))
        with self.assertRaises(etsy.SetupError):
            etsy.parse_code("https://x/?error=access_denied")
        with self.assertRaises(etsy.SetupError):
            etsy.parse_code("")

    def test_start_saves_verifier_and_writes_link(self):
        gh = FakeGH()
        with tempfile.TemporaryDirectory() as d:
            summ = Path(d) / "summary.md"
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rc = etsy.main(["auth-start", "--shop", "STEADFOLD"],
                               env=base_env(GITHUB_STEP_SUMMARY=str(summ)), gh_factory=gh.factory)
            self.assertEqual(rc, 0)
            pk = json.loads(gh.secrets["ETSY_PKCE_STEADFOLD"])
            md = summ.read_text()
            self.assertIn("https://www.etsy.com/oauth/connect?", md)
            self.assertNotIn(pk["verifier"], md + out.getvalue())
            self.assertIn(pk["state"], md)

    def finish(self, fake, code_text, gh, pk=None):
        pk = pk or {"verifier": "v" * 60, "state": "S1"}
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = etsy.main(["auth-finish", "--shop", "STEADFOLD"],
                           env=base_env(ETSY_PKCE_STEADFOLD=json.dumps(pk), ETSY_AUTH_CODE=code_text),
                           session=fake, gh_factory=gh.factory)
        return rc, out.getvalue()

    def test_finish_saves_refresh_token(self):
        gh = FakeGH()
        rc, out = self.finish(FakeEtsy(), "https://github.com/x?code=ONEtimeCODE123&state=S1", gh)
        self.assertEqual(rc, 0)
        self.assertEqual(gh.secrets["ETSY_REFRESH_TOKEN_STEADFOLD"], RT_NEW)
        self.assertIn("used", json.loads(gh.secrets["ETSY_PKCE_STEADFOLD"]))
        for s in (RT_NEW, AT, SHARED, "ONEtimeCODE123"):
            self.assertNotIn(s, out)

    def test_finish_wrong_shop_saves_nothing(self):
        gh = FakeGH()
        rc, out = self.finish(FakeEtsy(shop_name="SomeoneElse"), "ONEtimeCODE123", gh)
        self.assertEqual(rc, 2)
        self.assertEqual(gh.secrets, {})
        self.assertIn("SomeoneElse", out)

    def test_finish_stale_state(self):
        gh = FakeGH()
        rc, _ = self.finish(FakeEtsy(), "https://github.com/x?code=ONEtimeCODE123&state=OLD", gh)
        self.assertEqual(rc, 2)
        self.assertEqual(gh.secrets, {})


class ListingFlow(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self._live = etsy.LIVE_PATH
        etsy.LIVE_PATH = Path(self.tmp.name) / "live.json"
        self._dec = etsy.decrypt_files

        def fake_decrypt(spec, key_text, outdir, run=None):
            self.assertTrue(key_text)
            outdir.mkdir(parents=True, exist_ok=True)
            res = []
            for f in spec["files"]:
                p = outdir / f["name"]
                p.write_bytes(b"customer file")
                res.append((p, f["name"]))
            return res
        etsy.decrypt_files = fake_decrypt

    def tearDown(self):
        etsy.LIVE_PATH = self._live
        etsy.decrypt_files = self._dec
        self.tmp.cleanup()

    def run_list(self, fake, spec="listings/DP-CALM-P.json", extra=(), **env):
        gh = FakeGH()
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = etsy.main(["list", "--spec", spec, *extra],
                           env=base_env(RUNNER_TEMP=self.tmp.name, **env),
                           session=fake, gh_factory=gh.factory, sleep=lambda s: None)
        return rc, out.getvalue(), gh

    def test_lists_publishes_verifies_and_records(self):
        fake = FakeEtsy()
        rc, out, gh = self.run_list(fake)
        self.assertEqual(rc, 0, out)
        L = fake.listings[5000]
        self.assertEqual(L["state"], "active")
        f = L["fields"]
        self.assertEqual(f["price"], "16.00")
        self.assertEqual(f["type"], "download")
        self.assertEqual(f["who_made"], "i_did")
        self.assertEqual(f["is_supply"], "false")
        self.assertEqual(f["should_auto_renew"], "false")
        self.assertEqual(f["taxonomy_id"], "3")
        self.assertEqual(f["tags"].count(","), 12)
        self.assertEqual(len(L["images"]), 10)
        self.assertEqual(len(L["videos"]), 1)
        self.assertEqual([x["name"] for x in L["files"]],
                         [x["name"] for x in real_spec("DP-CALM-P")["files"]])
        live = json.loads(etsy.LIVE_PATH.read_text())
        self.assertEqual(live["listings"]["DP-CALM-P"]["url"], "https://www.etsy.com/listing/5000/x")
        self.assertEqual(live["drafts"], {})
        self.assertIn("https://www.etsy.com/listing/5000/x", out)
        self.assertEqual(gh.secrets["ETSY_REFRESH_TOKEN_STEADFOLD"], RT_NEW)   # rotated token saved
        for s in (RT_OLD, RT_NEW, AT, SHARED, PAT):
            self.assertNotIn(s, out)
        # second run: nothing new is created
        n = len(fake.calls)
        rc, out, _ = self.run_list(fake)
        self.assertEqual(rc, 0)
        self.assertFalse([c for c in fake.calls[n:] if c[0] in ("POST", "PATCH")
                          and "oauth" not in c[1]])

    def test_cad_shop_gets_cad_price_and_text(self):
        fake = FakeEtsy(currency="CAD")
        rc, out, _ = self.run_list(fake, spec="listings/FF-HMP.json")
        self.assertEqual(rc, 0, out)
        f = fake.listings[5000]["fields"]
        self.assertEqual(f["price"], "12.00")
        self.assertIn("then CA$19", f["description"])
        self.assertEqual(f["materials"], "Excel,Google Sheets,PDF")

    def test_wrong_currency_is_not_converted(self):
        fake = FakeEtsy(shop_name="LittlefoldHQ", currency="USD")
        rc, out, _ = self.run_list(fake, spec="listings/LBP4.json")
        self.assertEqual(rc, 1)
        self.assertIn("Not converting", out)
        self.assertFalse([c for c in fake.calls if c == ("POST", "/v3/application/shops/42/listings")])

    def test_existing_live_title_is_not_duplicated(self):
        t = real_spec("DP-CALM-P")["title"].replace("&", "&amp;")
        fake = FakeEtsy(existing=[{"listing_id": 77, "state": "active", "title": t,
                                   "url": "https://www.etsy.com/listing/77/a"}])
        rc, out, _ = self.run_list(fake)
        self.assertEqual(rc, 0)
        self.assertNotIn(("POST", "/v3/application/shops/42/listings"), fake.calls)
        self.assertIn("https://www.etsy.com/listing/77/a", out)

    def test_check_mode_writes_nothing(self):
        fake = FakeEtsy()
        rc, out, _ = self.run_list(fake, extra=("--check",))
        self.assertEqual(rc, 0, out)
        self.assertFalse([c for c in fake.calls if c[0] in ("POST", "PATCH") and "oauth" not in c[1]])
        self.assertFalse(etsy.LIVE_PATH.exists())

    def test_wrong_shop_token_stops(self):
        fake = FakeEtsy(shop_name="LittlefoldHQ")
        rc, out, _ = self.run_list(fake)
        self.assertEqual(rc, 1)
        self.assertNotIn(("POST", "/v3/application/shops/42/listings"), fake.calls)

    def test_when_made_fallback(self):
        fake = FakeEtsy(reject_when_made={"2020_2026"})
        rc, out, _ = self.run_list(fake)
        self.assertEqual(rc, 0, out)
        self.assertEqual(fake.listings[5000]["fields"]["when_made"], "2020_2025")

    def test_not_connected_shop_says_what_to_do(self):
        rc, out, _ = self.run_list(FakeEtsy(), ETSY_REFRESH_TOKEN_STEADFOLD="")
        self.assertEqual(rc, 1)
        self.assertIn("not connected yet", out)


class Decrypt(unittest.TestCase):
    def test_decrypt_checks_sha_and_removes_key(self):
        data = b"paid file bytes"
        spec = {"files": [{"name": "A.zip", "enc": "listings/files/x/A.zip.age",
                           "sha256": hashlib.sha256(data).hexdigest(), "size": len(data)}]}
        seen = {}

        def run(cmd, **kw):
            keyfile = cmd[cmd.index("-i") + 1]
            seen["key"] = Path(keyfile).read_text()
            seen["mode"] = oct(os.stat(keyfile).st_mode & 0o777)
            Path(cmd[cmd.index("-o") + 1]).write_bytes(data)
            return type("R", (), {"returncode": 0, "stderr": ""})()

        with tempfile.TemporaryDirectory() as d:
            res = etsy.decrypt_files(spec, "AGE-SECRET-KEY-1ABC", Path(d), run=run)
            self.assertEqual(res[0][1], "A.zip")
            self.assertEqual(seen, {"key": "AGE-SECRET-KEY-1ABC", "mode": "0o600"})
            self.assertEqual([p.name for p in Path(d).iterdir()], ["01-A.zip"])   # key file gone

            def bad_run(cmd, **kw):
                Path(cmd[cmd.index("-o") + 1]).write_bytes(b"tampered")
                return type("R", (), {"returncode": 0, "stderr": ""})()
            with self.assertRaises(etsy.EtsyError):
                etsy.decrypt_files(spec, "AGE-SECRET-KEY-1ABC", Path(d), run=bad_run)


if __name__ == "__main__":
    unittest.main()

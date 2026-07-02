"""Tests for tools/model_catalog.py — the model-fleet registry loader/gate.

Locks the invariants that make the catalog trustworthy: the real catalog passes
its referential gate, dangling refs are caught, routing.prefer must be selected,
status is derived honestly, and the resolved export round-trips.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import model_catalog as mc


class TestRealCatalog:
    def test_real_catalog_validates_clean(self):
        errors, _warnings, summary = mc.validate()
        assert errors == [], f"referential errors: {errors}"
        assert summary["models"] > 0
        assert summary["profiles"] > 0
        # ternary/bitnet is the dominant weight class in this fleet.
        assert summary["ternary_like"] >= summary["models"] // 2

    def test_resolved_export_shape(self):
        resolved = mc.load_resolved()
        assert set(resolved) == {"bands", "models", "groups", "profiles"}
        # every profile carries routing_resolved with full model records.
        for p in resolved["profiles"]:
            for r in p["routing_resolved"]:
                assert r["model"]["record_type"] in {"model", "group", "unresolved"}
                # a resolved group must keep its own kind (moe/merged/replicated).
                if r["model"]["record_type"] == "group":
                    assert r["model"]["kind"] in {"moe", "merged", "ensemble", "replicated"}
        # every model in the resolved contract carries a status.
        for m in resolved["models"]:
            assert m["status"] in mc.KNOWN_STATUS


class TestReferentialGate:
    def test_dangling_group_member_is_error(self):
        cat = mc.load_catalog()
        cat["groups"].append({"id": "g-bad", "kind": "merged", "members": ["no-such-model"]})
        errors, _w, _s = mc.validate(cat)
        assert any("no-such-model" in e for e in errors)

    def test_profile_selection_must_resolve(self):
        cat = mc.load_catalog()
        cat["profiles"].append({
            "id": "p-bad", "task": "coding",
            "selections": {"cpu": ["ghost-model"]},
        })
        errors, _w, _s = mc.validate(cat)
        assert any("ghost-model" in e for e in errors)

    def test_routing_prefer_must_be_in_selections(self):
        cat = mc.load_catalog()
        real_id = cat["models"][0]["id"]
        cat["profiles"].append({
            "id": "p-route", "task": "coding",
            "selections": {"cpu": []},           # prefer a real model NOT selected here
            "routing": [{"band": "trivial", "prefer": real_id}],
        })
        errors, _w, _s = mc.validate(cat)
        assert any(real_id in e and "selections" in e for e in errors)


class TestDerivedStatus:
    def test_source_implies_real(self):
        assert mc.derived_status({"id": "x", "source": "org/repo"}) == "real"

    def test_no_source_is_unverified(self):
        assert mc.derived_status({"id": "x", "source": None}) == "unverified"

    def test_explicit_status_wins(self):
        assert mc.derived_status({"id": "x", "source": "org/repo", "status": "aspirational"}) == "aspirational"

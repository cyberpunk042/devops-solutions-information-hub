#!/usr/bin/env python3
"""Loader / resolver / exporter for wiki/config/model-catalog/.

The model catalog (models.yaml + groups.yaml + profiles.yaml) is a flexible,
config-driven registry for the local-inference model fleet. This module is its
single source of logic:

  * ``load_catalog()``   — read the three YAMLs into a dict.
  * ``validate()``       — referential-integrity gate (P4). Hard-fails on a
                           dangling group member / profile selection /
                           ``routing.prefer``; warns (never fails) on unknown
                           enum values so the catalog stays extensible.
  * ``load_resolved()``  — the machine contract AICP consumes: profiles with
                           their ``routing`` bands expanded to full model
                           records and groups resolved to their members.
  * ``export(path)``     — write the resolved contract as JSON.

CLI::

    python3 -m tools.model_catalog validate
    python3 -m tools.model_catalog export [OUT.json]
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

CATALOG_DIR = Path(__file__).resolve().parent.parent / "wiki" / "config" / "model-catalog"
DEFAULT_EXPORT = CATALOG_DIR / "model-catalog.generated.json"

# Advisory enums — unknown values warn but do not fail (the catalog is extensible).
KNOWN_QUANT = {"ternary", "bitnet-1.58", "fp16", "int8", "native", "unknown"}
KNOWN_TIERS = {"cpu", "rtx-4090", "rtx-pro"}
KNOWN_KINDS = {"moe", "merged", "ensemble", "replicated"}
KNOWN_TASKS = {
    "coding", "general", "orchestration", "analysis", "agents", "dna",
    "protein", "particles", "reasoning", "specialist",
}
KNOWN_STATUS = {"real", "aspirational", "unverified"}


def derived_status(model: dict) -> str:
    """Honest status: explicit field wins; else a real `source` implies `real`,
    otherwise `unverified`. Never asserted from memory."""
    explicit = model.get("status")
    if explicit in KNOWN_STATUS:
        return explicit
    return "real" if model.get("source") else "unverified"
# Ordered complexity bands (low -> high).
BANDS = ["trivial", "simple", "moderate", "hard", "expert"]
KNOWN_BANDS = set(BANDS)


def _load_list(name: str, key: str) -> list[dict]:
    data = yaml.safe_load((CATALOG_DIR / name).read_text(encoding="utf-8")) or {}
    items = data.get(key, [])
    if not isinstance(items, list):
        raise SystemExit(f"ERROR: {name}: top-level key '{key}' must be a list")
    return items


def load_catalog() -> dict[str, list[dict]]:
    """Raw catalog: {'models': [...], 'groups': [...], 'profiles': [...]}."""
    return {
        "models": _load_list("models.yaml", "models"),
        "groups": _load_list("groups.yaml", "groups"),
        "profiles": _load_list("profiles.yaml", "profiles"),
    }


def validate(catalog: dict[str, list[dict]] | None = None) -> tuple[list[str], list[str], dict]:
    """Return (errors, warnings, summary). Errors are referential (hard fail)."""
    cat = catalog or load_catalog()
    models, groups, profiles = cat["models"], cat["groups"], cat["profiles"]
    errors: list[str] = []
    warnings: list[str] = []

    model_ids: set[str] = set()
    for m in models:
        mid = m.get("id")
        if not mid:
            errors.append(f"model missing id: {m.get('name', '<no name>')}")
            continue
        if mid in model_ids:
            errors.append(f"duplicate model id: {mid}")
        model_ids.add(mid)
        if m.get("quantization") not in KNOWN_QUANT:
            warnings.append(f"model {mid}: unknown quantization '{m.get('quantization')}'")
        if m.get("status") is not None and m.get("status") not in KNOWN_STATUS:
            warnings.append(f"model {mid}: unknown status '{m.get('status')}'")
        for t in m.get("tiers", []) or []:
            if t not in KNOWN_TIERS:
                warnings.append(f"model {mid}: unknown tier '{t}'")

    group_ids: set[str] = set()
    for g in groups:
        gid = g.get("id")
        if not gid:
            errors.append(f"group missing id: {g.get('name', '<no name>')}")
            continue
        if gid in group_ids:
            errors.append(f"duplicate group id: {gid}")
        group_ids.add(gid)
        if g.get("kind") not in KNOWN_KINDS:
            warnings.append(f"group {gid}: unknown kind '{g.get('kind')}'")
        for member in g.get("members", []) or []:
            if member not in model_ids:
                errors.append(f"group {gid}: member '{member}' is not a known model id")

    routable = model_ids | group_ids
    profile_ids: set[str] = set()
    for p in profiles:
        pid = p.get("id")
        if not pid:
            errors.append(f"profile missing id: {p.get('name', '<no name>')}")
            continue
        if pid in profile_ids:
            errors.append(f"duplicate profile id: {pid}")
        profile_ids.add(pid)
        if p.get("task") not in KNOWN_TASKS:
            warnings.append(f"profile {pid}: unknown task '{p.get('task')}'")

        selected: set[str] = set()
        selections = p.get("selections", {}) or {}
        if not selections:
            warnings.append(f"profile {pid}: no selections")
        for tier, ids in selections.items():
            if tier not in KNOWN_TIERS:
                warnings.append(f"profile {pid}: unknown tier '{tier}'")
            for ref in ids or []:
                if ref not in routable:
                    errors.append(f"profile {pid}[{tier}]: selection '{ref}' is not a known model or group id")
                selected.add(ref)

        # routing is optional; when present each prefer must resolve AND be selected.
        seen_bands: list[str] = []
        for entry in p.get("routing", []) or []:
            band, prefer = entry.get("band"), entry.get("prefer")
            if band not in KNOWN_BANDS:
                warnings.append(f"profile {pid}: unknown routing band '{band}'")
            seen_bands.append(band)
            if prefer not in routable:
                errors.append(f"profile {pid}: routing band '{band}' prefers '{prefer}' — not a known model or group id")
            elif prefer not in selected:
                errors.append(f"profile {pid}: routing band '{band}' prefers '{prefer}' which is not in this profile's selections")
        # bands should be listed low->high (advisory).
        ordered = [b for b in seen_bands if b in KNOWN_BANDS]
        if ordered != sorted(ordered, key=BANDS.index):
            warnings.append(f"profile {pid}: routing bands not in ascending order {ordered}")

    quant_counts = Counter(m.get("quantization") for m in models)
    ternary_like = sum(v for k, v in quant_counts.items() if k in {"ternary", "bitnet-1.58"})
    tier_counts: Counter = Counter()
    for m in models:
        for t in m.get("tiers", []) or []:
            tier_counts[t] += 1

    status_counts = Counter(derived_status(m) for m in models)

    summary = {
        "models": len(model_ids),
        "groups": len(group_ids),
        "profiles": len(profile_ids),
        "ternary_like": ternary_like,
        "by_quantization": dict(quant_counts),
        "by_tier": dict(tier_counts),
        "by_status": dict(status_counts),
    }
    return errors, warnings, summary


def load_resolved(catalog: dict[str, list[dict]] | None = None) -> dict[str, Any]:
    """The AICP contract: models by id, groups with member records, profiles
    with routing bands expanded to full model/group records."""
    cat = catalog or load_catalog()
    # Annotate every model with its derived status so the AICP contract carries it.
    for m in cat["models"]:
        m.setdefault("status", derived_status(m))
    models_by_id = {m["id"]: m for m in cat["models"] if m.get("id")}
    groups_by_id = {g["id"]: g for g in cat["groups"] if g.get("id")}

    def record(ref: str) -> dict:
        # `record_type` is the discriminator; a group's own `kind`
        # (moe/merged/replicated) is preserved as data (don't collide).
        if ref in models_by_id:
            return {"record_type": "model", **models_by_id[ref]}
        if ref in groups_by_id:
            g = groups_by_id[ref]
            return {"record_type": "group", **g,
                    "member_records": [models_by_id[m] for m in g.get("members", []) if m in models_by_id]}
        return {"record_type": "unresolved", "id": ref}

    resolved_profiles = []
    for p in cat["profiles"]:
        rp = dict(p)
        rp["routing_resolved"] = [
            {"band": e.get("band"), "prefer": e.get("prefer"), "model": record(e.get("prefer"))}
            for e in p.get("routing", []) or []
        ]
        resolved_profiles.append(rp)

    return {
        "bands": BANDS,
        "models": cat["models"],
        "groups": [dict(g, member_records=[models_by_id[m] for m in g.get("members", []) if m in models_by_id])
                   for g in cat["groups"]],
        "profiles": resolved_profiles,
    }


def export(path: Path | str = DEFAULT_EXPORT) -> Path:
    errors, _, _ = validate()
    if errors:
        raise SystemExit(f"refusing to export — {len(errors)} referential error(s); run validate")
    out = Path(path)
    out.write_text(json.dumps(load_resolved(), indent=2, sort_keys=False) + "\n", encoding="utf-8")
    return out


def _print_summary(summary: dict) -> None:
    print("Model catalog")
    print(f"  models:   {summary['models']}")
    print(f"  groups:   {summary['groups']}")
    print(f"  profiles: {summary['profiles']}")
    print(f"  ternary/bitnet-1.58: {summary['ternary_like']}/{summary['models']}")
    print(f"  by quantization: {summary['by_quantization']}")
    print(f"  by tier: {summary['by_tier']}")
    print(f"  by status: {summary['by_status']}")


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else "validate"
    if cmd == "validate":
        errors, warnings, summary = validate()
        _print_summary(summary)
        if warnings:
            print(f"\n  {len(warnings)} advisory warning(s):")
            for w in warnings:
                print(f"    - {w}")
        if errors:
            print(f"\n  {len(errors)} referential ERROR(s):")
            for e in errors:
                print(f"    - {e}")
            print("\nStatus: FAIL")
            return 1
        print("\nStatus: PASS (referential integrity clean)")
        return 0
    if cmd == "export":
        target = Path(argv[1]) if len(argv) > 1 else DEFAULT_EXPORT
        out = export(target)
        print(f"wrote resolved catalog contract: {out}")
        return 0
    print(f"unknown command: {cmd!r} (use 'validate' or 'export')", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

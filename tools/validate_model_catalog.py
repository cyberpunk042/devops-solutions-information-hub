#!/usr/bin/env python3
"""Referential-integrity + summary check for wiki/config/model-catalog/.

The model catalog (models.yaml + groups.yaml + profiles.yaml) is a flexible,
config-driven registry for the model fleet. This is its verification gate
(P4 — Declarations Aspirational Until Verified): every group member and every
profile selection MUST resolve to a real model or group id, or the catalog is
lying about what it can route.

Referential errors are hard failures (exit 1). Unknown enum values are advisory
warnings only — the catalog is deliberately extensible, so a new quantization /
tier / kind / task token is allowed but surfaced so typos don't hide.

Usage:  python3 -m tools.validate_model_catalog
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import yaml

CATALOG_DIR = Path(__file__).resolve().parent.parent / "wiki" / "config" / "model-catalog"

# Advisory enums (warn on unknown, do not fail — the catalog is extensible).
KNOWN_QUANT = {"ternary", "bitnet-1.58", "fp16", "int8", "native", "unknown"}
KNOWN_TIERS = {"cpu", "rtx-4090", "rtx-pro"}
KNOWN_KINDS = {"moe", "merged", "ensemble", "replicated"}
KNOWN_TASKS = {
    "coding", "general", "orchestration", "analysis", "agents", "dna",
    "protein", "particles", "reasoning", "specialist",
}


def _load(name: str, key: str) -> list[dict]:
    path = CATALOG_DIR / name
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    items = data.get(key, [])
    if not isinstance(items, list):
        raise SystemExit(f"ERROR: {name}: top-level key '{key}' must be a list")
    return items


def main() -> int:
    models = _load("models.yaml", "models")
    groups = _load("groups.yaml", "groups")
    profiles = _load("profiles.yaml", "profiles")

    errors: list[str] = []
    warnings: list[str] = []

    # ---- model ids: unique + present ----
    model_ids: set[str] = set()
    for m in models:
        mid = m.get("id")
        if not mid:
            errors.append(f"model missing id: {m.get('name', '<no name>')}")
            continue
        if mid in model_ids:
            errors.append(f"duplicate model id: {mid}")
        model_ids.add(mid)
        q = m.get("quantization")
        if q not in KNOWN_QUANT:
            warnings.append(f"model {mid}: unknown quantization '{q}'")
        for t in m.get("tiers", []) or []:
            if t not in KNOWN_TIERS:
                warnings.append(f"model {mid}: unknown tier '{t}'")

    # ---- group ids unique; members resolve to models ----
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

    # ---- profile selections resolve to a model OR group id ----
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
        selections = p.get("selections", {}) or {}
        if not selections:
            warnings.append(f"profile {pid}: no selections")
        for tier, ids in selections.items():
            if tier not in KNOWN_TIERS:
                warnings.append(f"profile {pid}: unknown tier '{tier}'")
            for ref in ids or []:
                if ref not in routable:
                    errors.append(
                        f"profile {pid}[{tier}]: selection '{ref}' is not a known model or group id"
                    )

    # ---- summary ----
    quant_counts = Counter(m.get("quantization") for m in models)
    ternary_like = sum(
        v for k, v in quant_counts.items() if k in {"ternary", "bitnet-1.58"}
    )
    tier_counts: Counter = Counter()
    for m in models:
        for t in m.get("tiers", []) or []:
            tier_counts[t] += 1

    print("Model catalog validation")
    print(f"  models:   {len(model_ids)}")
    print(f"  groups:   {len(group_ids)}  ({Counter(g.get('kind') for g in groups)})")
    print(f"  profiles: {len(profile_ids)}")
    print(f"  ternary/bitnet-1.58 models: {ternary_like}/{len(model_ids)}")
    print(f"  by quantization: {dict(quant_counts)}")
    print(f"  by tier: {dict(tier_counts)}")

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


if __name__ == "__main__":
    sys.exit(main())

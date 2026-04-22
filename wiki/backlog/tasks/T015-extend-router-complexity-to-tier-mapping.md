---
title: "T015 — Extend router.py Complexity-to-Tier Mapping for 5 Tiers"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 90
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: S
epic: "E011"
module: "E011-m001"
depends_on:
  - "T014"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m001-tier-definitions-update
    type: wiki
    file: wiki/backlog/modules/e011-m001-tier-definitions-update.md
  - id: aicp-router
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/router.py
tags: [task, p1, e011, aicp, router, complexity-scorer, tier-mapping, k2-6]
---

# T015 — Extend router.py Tier Mapping for 5 Tiers

## Summary

Update `classify_task_with_reason()` in `/home/jfortin/devops-expert-local-ai/aicp/core/router.py` (current 2-threshold / 3-tier logic near line 154) so it supports N thresholds → N+1 bands, reading the optional `router.tier_map` from config. Keep the legacy 2-threshold path as fallback. When the chosen tier's backend is unavailable, walk `failover_chain` for the first available backend.

## Done When

- [ ] `classify_task_with_reason()` reads `config.get("router", {}).get("tier_map")` and selects band index based on N thresholds
- [ ] Legacy 2-threshold behavior preserved when `tier_map` is absent (backward compat)
- [ ] Availability check: chosen backend's `is_available()` consulted before commit; falls through `failover_chain` on False
- [ ] Reason string includes band index + chosen backend name + fallback reason (if applicable)
- [ ] Unit test: score=0.5, mode=act, config with `tier_map` + 4 thresholds → routes to `k2_6_openrouter`
- [ ] Unit test: score=0.95 → routes to `claude`
- [ ] Unit test: chosen=`k2_6_local` but backend unavailable → falls to `k2_6_openrouter`
- [ ] All existing router tests still pass
- [ ] Change committed with message: `feat(router): support N-tier mapping with availability fallback`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
grep -n "classify_task_with_reason\|complexity_thresholds" aicp/core/router.py

# Apply edit per e011-m001 Step 4 pseudo-diff
$EDITOR aicp/core/router.py

python3 -m pytest tests/ -k router -v
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/core/router.py
```

## Relationships

- PART OF: [[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T014-add-k2-6-backend-entries-to-default-yaml|T014-add-k2-6-backend-entries-to-default-yaml]]

## Backlinks

[[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T014-add-k2-6-backend-entries-to-default-yaml|T014-add-k2-6-backend-entries-to-default-yaml]]

---
title: "T025 — Fallback-Chain Integration Test (3 failures → next tier)"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 80
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: S
epic: "E011"
module: "E011-m004"
depends_on:
  - "T024"
  - "T018"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m004-circuit-breakers-and-fallback-chain
    type: wiki
    file: wiki/backlog/modules/e011-m004-circuit-breakers-and-fallback-chain.md
tags: [task, p1, e011, aicp, fallback-chain, integration-test, reliability]
---

# T025 — Fallback-Chain Integration Test

## Summary

Add `tests/test_fallback_chain.py` that proves: (1) injecting N failures into `k2_6_openrouter`'s breaker opens it, (2) a task that would normally route there lands on the next tier per `failover_chain`, (3) the routing event log records the fallback reason.

## Done When

- [ ] `tests/test_fallback_chain.py` exists
- [ ] Test `test_k2_6_openrouter_open_falls_through_to_openrouter` passes
- [ ] Test `test_k2_6_local_unavailable_skipped_silently` passes (is_available=False means breaker stays CLOSED, router just skips)
- [ ] Test uses `monkeypatch` to force scorer output; does NOT make real network calls
- [ ] Event-log emission includes `route: "failover:<next_backend>"` + `reason: "<prev_backend> OPEN"` field
- [ ] All tests run in <5s combined
- [ ] Change committed with message: `test: fallback-chain integration scenarios for K2.6 tiers`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
$EDITOR tests/test_fallback_chain.py
# Scaffold per e011-m004 Step 3

python3 -m pytest tests/test_fallback_chain.py -v
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
rm tests/test_fallback_chain.py
```

## Relationships

- PART OF: [[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T024-extend-build-breakers-for-per-backend-overrides|T024-extend-build-breakers-for-per-backend-overrides]]
- DEPENDS ON: [[T018-register-k2-6-openrouter-instance-in-cli-main|T018-register-k2-6-openrouter-instance-in-cli-main]]

## Backlinks

[[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T024-extend-build-breakers-for-per-backend-overrides|T024-extend-build-breakers-for-per-backend-overrides]]
[[T018-register-k2-6-openrouter-instance-in-cli-main|T018-register-k2-6-openrouter-instance-in-cli-main]]

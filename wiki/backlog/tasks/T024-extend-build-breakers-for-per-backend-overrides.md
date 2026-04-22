---
title: "T024 — Extend build_breakers() to Honor per_backend Overrides"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 85
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: S
epic: "E011"
module: "E011-m004"
depends_on:
  - "T023"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m004-circuit-breakers-and-fallback-chain
    type: wiki
    file: wiki/backlog/modules/e011-m004-circuit-breakers-and-fallback-chain.md
  - id: aicp-circuit-breaker
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/circuit_breaker.py
tags: [task, p1, e011, aicp, circuit-breaker, build-breakers]
---

# T024 — Extend build_breakers() for per_backend Overrides

## Summary

Inspect the current `build_breakers()` in `/home/jfortin/devops-expert-local-ai/aicp/core/circuit_breaker.py`. If it does not already read `config.circuit_breaker.per_backend.<name>`, extend it to deep-merge per-backend thresholds over the global defaults. All backend keys from the `backends` dict must get a breaker — including the new `k2_6_openrouter` and `k2_6_local`.

## Done When

- [ ] `build_breakers(config, backends)` returns a breaker for every key in `backends`
- [ ] Per-backend overrides from `config.circuit_breaker.per_backend.<name>` are applied on top of defaults
- [ ] Missing per-backend entry falls through to global defaults (no crash)
- [ ] Unit test: config with only global defaults → every breaker uses defaults
- [ ] Unit test: config with `per_backend.k2_6_local.failure_threshold: 1` → that breaker has `failure_threshold == 1`, others at default
- [ ] Change committed with message: `feat(circuit_breaker): honor per_backend threshold overrides`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
grep -n "def build_breakers\|CircuitBreaker(\|per_backend" aicp/core/circuit_breaker.py

$EDITOR aicp/core/circuit_breaker.py

python3 -m pytest tests/ -k "breaker or circuit" -v
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/core/circuit_breaker.py
```

## Relationships

- PART OF: [[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T023-add-per-backend-circuit-breaker-config|T023-add-per-backend-circuit-breaker-config]]

## Backlinks

[[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T023-add-per-backend-circuit-breaker-config|T023-add-per-backend-circuit-breaker-config]]

---
title: "T023 — Add Per-Backend circuit_breaker Config Stanzas"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 100
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: XS
epic: "E011"
module: "E011-m004"
depends_on: []
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
tags: [task, p1, e011, aicp, circuit-breaker, config, reliability]
---

# T023 — Per-Backend circuit_breaker Config

## Summary

Add a `circuit_breaker.per_backend` section to `config/default.yaml` with tuned thresholds for each of the 5 tiers. Tight thresholds for local tiers (fail-fast; TCP probe already filtered out unreachable), moderate for online tiers, loose for Anthropic-direct (last-resort).

## Done When

- [ ] `config/default.yaml` contains `circuit_breaker.per_backend.{local, k2_6_local, k2_6_openrouter, openrouter, claude}` with thresholds per `e011-m004` Step 1
- [ ] Global defaults (`failure_threshold: 3`, `recovery_timeout: 30`, `half_open_max: 1`) remain present as fallback
- [ ] YAML parses cleanly
- [ ] Change committed with message: `feat(config): per-backend circuit_breaker thresholds for 5-tier stack`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
grep -n "circuit_breaker\|failure_threshold\|recovery_timeout" config/default.yaml

$EDITOR config/default.yaml
# Paste per-backend block per e011-m004 Step 1

python3 -c "import yaml; yaml.safe_load(open('config/default.yaml'))"
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- config/default.yaml
```

## Relationships

- PART OF: [[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]

## Backlinks

[[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]

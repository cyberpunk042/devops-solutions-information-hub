---
title: "T014 — Add K2.6 Backend Entries to config/default.yaml"
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
module: "E011-m001"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m001-tier-definitions-update
    type: wiki
    file: wiki/backlog/modules/e011-m001-tier-definitions-update.md
  - id: aicp-default-config
    type: repository
    file: /home/jfortin/devops-expert-local-ai/config/default.yaml
tags: [task, p1, e011, aicp, config, default-yaml, k2-6, tier, openrouter, local]
---

# T014 — Add K2.6 Backend Entries to config/default.yaml

## Summary

Add two new backend stanzas (`k2_6_openrouter` and `k2_6_local`) and extend the `router.complexity_thresholds` + `router.failover_chain` in `/home/jfortin/devops-expert-local-ai/config/default.yaml` so AICP's config layer recognizes K2.6 as tiered choices. `k2_6_local.enabled` starts at `false` until E008 M002 + E011 M003 land.

## Done When

- [ ] `backends.k2_6_openrouter` stanza added with `model: moonshotai/kimi-k2.6`, `max_tokens: 8192`, `timeout: 300`, `enabled: true`, cost hints
- [ ] `backends.k2_6_local` stanza added with `base_url: http://localhost:8091`, `model: kimi-k2.6-q2`, `max_tokens: 8192`, `timeout: 600`, `enabled: false`
- [ ] `router.complexity_thresholds` updated from `[0.3, 0.6]` to `[0.25, 0.45, 0.70, 0.90]` (four cut-points, five tiers)
- [ ] `router.failover_chain` updated to `[local, k2_6_local, k2_6_openrouter, openrouter, claude]`
- [ ] Optional `router.tier_map` block documents band→backend mapping explicitly (for router.py pickup in T015)
- [ ] `python3 -c "import yaml; yaml.safe_load(open('config/default.yaml'))"` parses without error
- [ ] `python3 -m aicp.cli.main --help` runs without config errors
- [ ] Change committed with message: `feat(config): add K2.6 tiers (openrouter + local) to default.yaml`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
cp config/default.yaml config/default.yaml.bak.$(date +%s)     # safety net
$EDITOR config/default.yaml
# Apply changes per e011-m001 Step 2 + Step 3

python3 -c "import yaml; yaml.safe_load(open('config/default.yaml'))"
python3 -m aicp.cli.main --help
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
mv config/default.yaml.bak.<ts> config/default.yaml
# OR
git checkout -- config/default.yaml
```

## Relationships

- PART OF: [[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]

## Backlinks

[[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]

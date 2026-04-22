---
title: "T016 — Update failover_chain + Add quality / fast Profiles"
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
estimate: XS
epic: "E011"
module: "E011-m001"
depends_on:
  - "T015"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m001-tier-definitions-update
    type: wiki
    file: wiki/backlog/modules/e011-m001-tier-definitions-update.md
  - id: aicp-profiles
    type: repository
    file: /home/jfortin/devops-expert-local-ai/config/profiles
tags: [task, p1, e011, aicp, profiles, failover-chain, quality, fast, k2-6]
---

# T016 — Update failover_chain + Add Profiles

## Summary

Finalize the `router.failover_chain` ordering in `config/default.yaml` so the 5-tier fallback walks in the intended order, and add a `quality.yaml` profile that biases routing toward K2.6. `fast.yaml` already exists; update it to include `k2_6_openrouter` in its chain where appropriate.

## Done When

- [ ] `config/default.yaml` `router.failover_chain`: `[local, k2_6_local, k2_6_openrouter, openrouter, claude]`
- [ ] `config/profiles/quality.yaml` created with: tighter thresholds favoring K2.6 (`[0.20, 0.40, 0.65, 0.92]`), `max_tokens: 16384` for k2_6_openrouter, description comment
- [ ] `config/profiles/fast.yaml` updated: thresholds tuned for quick local → K2.6 escalation, chain `[local, k2_6_openrouter]` (skip local K2.6 since "fast" should stay cheap)
- [ ] `AICP_PROFILE=quality python3 -m aicp.cli.main run --help` loads without error
- [ ] `AICP_PROFILE=fast python3 -m aicp.cli.main run --help` loads without error
- [ ] Unit test loads each profile and asserts the merged `complexity_thresholds` length == 4
- [ ] Change committed with message: `feat(config): add quality profile + refresh failover_chain for K2.6 tiers`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
ls config/profiles/
$EDITOR config/default.yaml
$EDITOR config/profiles/fast.yaml
cat > config/profiles/quality.yaml <<'EOF'
# See e011-m001 Step 5 for canonical content
name: quality
description: "Maximize reasoning quality per dollar — K2.6 by default, Opus only for top 10%."
router:
  complexity_thresholds: [0.20, 0.40, 0.65, 0.92]
backends:
  k2_6_openrouter:
    max_tokens: 16384
EOF

AICP_PROFILE=quality python3 -m aicp.cli.main run --help
AICP_PROFILE=fast python3 -m aicp.cli.main run --help
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- config/default.yaml config/profiles/fast.yaml
rm -f config/profiles/quality.yaml
```

## Relationships

- PART OF: [[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T015-extend-router-complexity-to-tier-mapping|T015-extend-router-complexity-to-tier-mapping]]

## Backlinks

[[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T015-extend-router-complexity-to-tier-mapping|T015-extend-router-complexity-to-tier-mapping]]

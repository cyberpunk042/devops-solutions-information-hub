---
title: "T018 — Register k2_6_openrouter Instance in aicp/cli/main.py"
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
module: "E011-m002"
depends_on:
  - "T017"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m002-k2-6-openrouter-backend-adapter
    type: wiki
    file: wiki/backlog/modules/e011-m002-k2-6-openrouter-backend-adapter.md
  - id: aicp-cli-main
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/cli/main.py
tags: [task, p1, e011, aicp, cli, backend-registration, k2-6]
---

# T018 — Register k2_6_openrouter Instance in cli/main.py

## Summary

Instantiate a second `OpenRouterBackend` object in `/home/jfortin/devops-expert-local-ai/aicp/cli/main.py` (around lines 440–513 where existing `backends` dict is populated), passing `config_key="k2_6_openrouter"`. Gate registration on `config.backends.k2_6_openrouter.enabled`. This is the change that actually makes K2.6 routable end-to-end.

## Done When

- [ ] `backends["k2_6_openrouter"] = OpenRouterBackend(config, config_key="k2_6_openrouter")` present in the backends-build block, guarded by `if config.get("backends", {}).get("k2_6_openrouter", {}).get("enabled", True)`
- [ ] `aicp run --backend k2_6_openrouter "Identify yourself."` returns a K2.6 response (mentions Kimi/Moonshot, not Claude)
- [ ] `last_usage["model"]` starts with `moonshotai/kimi-k2.6`
- [ ] `last_usage["estimated_cost_usd"]` > 0 and is in the expected range ($0.0002–$0.001 for a short prompt)
- [ ] `aicp run --stream --backend k2_6_openrouter "haiku about storage"` streams chunks
- [ ] Breaker key `k2_6_openrouter` exists in `breakers` dict after Controller init
- [ ] Change committed with message: `feat(cli): register k2_6_openrouter backend instance`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
grep -n "backends\[\"openrouter\"\]\|OpenRouterBackend(" aicp/cli/main.py

# Apply edit per e011-m002 Step 2
$EDITOR aicp/cli/main.py

source .env
python3 -m aicp.cli.main run --backend k2_6_openrouter "Identify yourself."
python3 -m aicp.cli.main run --stream --backend k2_6_openrouter "Write a haiku about disk I/O."
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/cli/main.py
```

## Relationships

- PART OF: [[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T017-parameterize-openrouter-backend-config-key|T017-parameterize-openrouter-backend-config-key]]

## Backlinks

[[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T017-parameterize-openrouter-backend-config-key|T017-parameterize-openrouter-backend-config-key]]

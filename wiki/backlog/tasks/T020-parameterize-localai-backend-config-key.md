---
title: "T020 — Parameterize LocalAIBackend __init__ to accept config_key"
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
estimate: S
epic: "E011"
module: "E011-m003"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m003-k2-6-local-backend-adapter
    type: wiki
    file: wiki/backlog/modules/e011-m003-k2-6-local-backend-adapter.md
  - id: aicp-localai-backend
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/backends/localai.py
tags: [task, p1, e011, aicp, localai, backend, refactor, k2-6, local]
---

# T020 — Parameterize LocalAIBackend __init__

## Summary

Mirror T017's pattern on `LocalAIBackend` in `/home/jfortin/devops-expert-local-ai/aicp/backends/localai.py`. Add optional `config_key: str = "local"` so the same class can serve both the existing `local` tier (Qwen3-8B at localhost:8090) and the new `k2_6_local` tier (KTransformers at localhost:8091). Zero behavior change when called with no `config_key`.

## Done When

- [ ] `__init__` signature: `def __init__(self, config: Dict[str, Any], config_key: str = "local")`
- [ ] `self.config_key = config_key`
- [ ] `self.config = config.get("backends", {}).get(config_key, {})`
- [ ] `self.name = config_key`
- [ ] `self.base_url`, `self.model`, `self.max_tokens` read from `self.config` (already should)
- [ ] All existing LocalAI tests pass (default arg = backward compat)
- [ ] New unit test: `LocalAIBackend(cfg, config_key="k2_6_local")` picks up `http://localhost:8091` + `kimi-k2.6-q2`
- [ ] Change committed with message: `refactor(localai): parameterize config_key to support multiple local tiers`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
grep -n "class LocalAIBackend\|def __init__\|self.base_url\s*=\|self.model\s*=" aicp/backends/localai.py

$EDITOR aicp/backends/localai.py

python3 -m pytest tests/ -k "localai or local_backend" -v
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/backends/localai.py
```

## Relationships

- PART OF: [[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]

## Backlinks

[[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]

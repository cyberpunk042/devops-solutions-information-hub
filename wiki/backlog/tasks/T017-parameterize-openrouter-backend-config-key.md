---
title: "T017 — Parameterize OpenRouterBackend __init__ to accept config_key"
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
module: "E011-m002"
depends_on:
  - "T014"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m002-k2-6-openrouter-backend-adapter
    type: wiki
    file: wiki/backlog/modules/e011-m002-k2-6-openrouter-backend-adapter.md
  - id: aicp-openrouter-backend
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/backends/openrouter.py
tags: [task, p1, e011, aicp, openrouter, backend, refactor, k2-6]
---

# T017 — Parameterize OpenRouterBackend __init__

## Summary

Modify `OpenRouterBackend.__init__` in `/home/jfortin/devops-expert-local-ai/aicp/backends/openrouter.py` to accept an optional `config_key: str = "openrouter"` parameter so the same class can serve both the classic `openrouter` (for Opus/GPT fallback) and the new `k2_6_openrouter` tier. Also extend the pricing table to recognize `moonshotai/kimi-k2.6` prefix.

## Done When

- [ ] `__init__` signature: `def __init__(self, config: Dict[str, Any], config_key: str = "openrouter")`
- [ ] `self.config_key = config_key`
- [ ] `self.config = config.get("backends", {}).get(config_key, {})`
- [ ] `self.name = config_key` (used by metrics + breaker registration)
- [ ] Pricing table entry for `moonshotai/kimi-k2.6` → `{"prompt": 0.60, "completion": 2.50}`
- [ ] Pricing lookup is prefix-matched so `moonshotai/kimi-k2.6-20260420` resolves correctly
- [ ] All existing tests in `tests/` pass (default arg preserves backward compat)
- [ ] New unit test in `tests/test_openrouter_backend.py`: instantiate with `config_key="k2_6_openrouter"`, assert `self.model == "moonshotai/kimi-k2.6"`
- [ ] Change committed with message: `refactor(openrouter): parameterize config_key to support multiple tiers`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
grep -n "class OpenRouterBackend\|self.config\s*=\|PRICING\s*=" aicp/backends/openrouter.py

# Apply edit per e011-m002 Step 1 + Step 3
$EDITOR aicp/backends/openrouter.py

python3 -m pytest tests/ -k openrouter -v
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/backends/openrouter.py
```

## Relationships

- PART OF: [[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T014-add-k2-6-backend-entries-to-default-yaml|T014-add-k2-6-backend-entries-to-default-yaml]]

## Backlinks

[[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T014-add-k2-6-backend-entries-to-default-yaml|T014-add-k2-6-backend-entries-to-default-yaml]]

---
title: "T019 — Extend Pricing Table with moonshotai/kimi-k2.6"
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
  - id: aicp-openrouter-backend
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/backends/openrouter.py
tags: [task, p1, e011, aicp, pricing, cost, openrouter, k2-6]
---

# T019 — Extend Pricing Table for K2.6

## Summary

Add pricing entry for `moonshotai/kimi-k2.6` in `/home/jfortin/devops-expert-local-ai/aicp/backends/openrouter.py` so `last_usage.estimated_cost_usd` reports correctly. OpenRouter returns the model id with a date suffix (`-20260420`), so pricing lookup MUST match by prefix, not exact equality. Empirical smoke test (2026-04-22) showed $0.00047 for a short thinking-block prompt — cross-check that the pricing table predicts this order of magnitude.

## Done When

- [ ] `PRICING` (or equivalent) dict in `openrouter.py` contains `"moonshotai/kimi-k2.6": {"prompt": 0.60, "completion": 2.50}` per 1M tokens
- [ ] Lookup function performs prefix match so `moonshotai/kimi-k2.6-20260420` resolves correctly
- [ ] After a live K2.6 round-trip, `last_usage["estimated_cost_usd"]` is within ±10% of OpenRouter's dashboard figure
- [ ] Unit test: `_lookup_price("moonshotai/kimi-k2.6-20260420")["prompt"] == 0.60`
- [ ] Change committed with message: `feat(openrouter): add K2.6 pricing entry + prefix lookup`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
grep -n "PRICING\|_lookup_price\|cost_per_1m\|estimated_cost_usd" aicp/backends/openrouter.py

# Apply edit per e011-m002 Step 3
$EDITOR aicp/backends/openrouter.py

python3 -m pytest tests/ -k "openrouter or pricing" -v

# Live sanity check
source .env
python3 -c "
from aicp.config.loader import load_config
from aicp.backends.openrouter import OpenRouterBackend
cfg = load_config()
b = OpenRouterBackend(cfg, config_key='k2_6_openrouter')
result = b.execute('hi', None, None)
print('last_usage:', b.last_usage)
assert b.last_usage.get('estimated_cost_usd', 0) > 0
"
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/backends/openrouter.py
```

## Relationships

- PART OF: [[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T017-parameterize-openrouter-backend-config-key|T017-parameterize-openrouter-backend-config-key]]

## Backlinks

[[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T017-parameterize-openrouter-backend-config-key|T017-parameterize-openrouter-backend-config-key]]

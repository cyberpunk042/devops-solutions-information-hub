---
title: "E011 M002 — K2.6 OpenRouter Backend Adapter (reuse OpenRouterBackend)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 95
progress: 0
stages_completed: [document]
artifacts: []
epic: "E011"
depends_on:
  - "E011-m001"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-routing-integration-aicp-tiers
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E011-routing-integration-aicp-tiers.md
  - id: aicp-openrouter-backend
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/backends/openrouter.py
  - id: aicp-cli-main
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/cli/main.py
tags: [module, p1, e011, aicp, openrouter, k2-6, backend, adapter, reuse]
---

# E011 M002 — K2.6 OpenRouter Backend Adapter

## Summary

Wire Kimi K2.6 (via OpenRouter) into AICP as a first-class backend named `k2_6_openrouter`. **The heavy lifting already exists**: `aicp/backends/openrouter.py` speaks OpenAI-compatible HTTP to OpenRouter. Since K2.6 exposes the same OpenAI-compat surface at `https://openrouter.ai/api/v1/chat/completions`, we reuse the existing `OpenRouterBackend` class — no new class file needed. The work is: (a) parameterize the class to read a different config section, (b) register a second instance in `cli/main.py`, (c) extend pricing lookup with K2.6 rates.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T017 | Parameterize OpenRouterBackend __init__ to accept config_key | 100% | 0% | draft |
| T018 | Register k2_6_openrouter instance in cli/main.py backends dict | 100% | 0% | draft |
| T019 | Extend pricing table with moonshotai/kimi-k2.6 cost_per_1m | 100% | 0% | draft |

## Dependencies

- **E011 M001** — tier + backend config entries must exist in `config/default.yaml`.
- Operator's OpenRouter key at `/home/jfortin/devops-expert-local-ai/.env` (already loaded by AICP's env mechanism).
- Empirical cost numbers from smoke test (2026-04-22): $0.00047 for a K2.6 prompt with thinking blocks. Use OpenRouter's advertised rates of $0.60/$2.50 per 1M prompt/completion tokens.

## Done When

- [ ] `OpenRouterBackend.__init__` accepts an optional `config_key: str = "openrouter"` param; defaults preserve backward compatibility
- [ ] `aicp/cli/main.py` instantiates two `OpenRouterBackend` objects — one for classic OpenRouter (Opus / GPT fallback) and one keyed on `k2_6_openrouter`
- [ ] `backends` dict in `Controller` contains key `"k2_6_openrouter"`
- [ ] Pricing table in `openrouter.py` recognizes `moonshotai/kimi-k2.6` (and `-<date>` variants) and reports correct `estimated_cost_usd`
- [ ] `aicp run --backend k2_6_openrouter "hello"` returns a reply that originated from K2.6 (confirm via `last_usage["model"]`)
- [ ] Streaming path works — `aicp run --stream --backend k2_6_openrouter "write a 5-line haiku"` emits incremental chunks
- [ ] Health check `k2_6_openrouter.is_available()` returns True when network + key are good, False otherwise
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Parameterize OpenRouterBackend

Current signature (approx, `aicp/backends/openrouter.py:52`):

```python
class OpenRouterBackend(Backend):
    def __init__(self, config: Dict[str, Any]):
        self.config = config.get("backends", {}).get("openrouter", {})
        ...
```

Change to:

```python
class OpenRouterBackend(Backend):
    def __init__(self, config: Dict[str, Any], config_key: str = "openrouter"):
        self.config_key = config_key
        self.config = config.get("backends", {}).get(config_key, {})
        self.name = config_key        # used by metrics + circuit-breaker registration
        ...
```

All existing callers keep working; new `k2_6_openrouter` instance passes `config_key="k2_6_openrouter"`.

### Step 2 — Register second instance in cli/main.py

At `aicp/cli/main.py` around line 504–511 (where `backends["openrouter"]` is created):

```python
# Existing
if config.get("backends", {}).get("openrouter", {}).get("enabled", True):
    backends["openrouter"] = OpenRouterBackend(config)

# Add
if config.get("backends", {}).get("k2_6_openrouter", {}).get("enabled", True):
    backends["k2_6_openrouter"] = OpenRouterBackend(config, config_key="k2_6_openrouter")
```

### Step 3 — Extend pricing table

In `aicp/backends/openrouter.py` wherever the pricing dict lives (grep for existing model names like `anthropic/claude-opus-4.6`), add:

```python
PRICING = {
    # ... existing entries ...
    "moonshotai/kimi-k2.6": {"prompt": 0.60, "completion": 2.50},  # per 1M tokens, USD (2026-04-22 rates)
    # OpenRouter returns the id as "moonshotai/kimi-k2.6-20260420" — match on prefix.
}

def _lookup_price(model: str) -> Dict[str, float]:
    for prefix, rates in PRICING.items():
        if model.startswith(prefix):
            return rates
    return {"prompt": 0.0, "completion": 0.0}
```

### Step 4 — Smoke test within AICP

```bash
cd /home/jfortin/devops-expert-local-ai
source .env
python3 -m aicp.cli.main run --backend k2_6_openrouter "Identify yourself."
# Expected: response mentions Kimi/Moonshot; last_usage["model"] starts with "moonshotai/kimi-k2.6"

python3 -m aicp.cli.main run --stream --backend k2_6_openrouter "Write a haiku about disk I/O."
# Expected: incremental chunks, total tokens > 0, cost_usd > 0
```

### Step 5 — Automated test

Add `tests/test_k2_6_backend.py`:

```python
def test_k2_6_backend_registered(monkeypatch, config_with_k2_6):
    backends = build_backends(config_with_k2_6)
    assert "k2_6_openrouter" in backends
    assert backends["k2_6_openrouter"].config_key == "k2_6_openrouter"

def test_k2_6_pricing_lookup():
    from aicp.backends.openrouter import _lookup_price
    p = _lookup_price("moonshotai/kimi-k2.6-20260420")
    assert p["prompt"] == 0.60
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/backends/openrouter.py aicp/cli/main.py
# config/default.yaml revert happens via E011 M001 rollback
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| OpenRouter might rename the K2.6 model id | external | 2026-04-22 | no | Pin to `moonshotai/kimi-k2.6` and match by prefix so `-<date>` suffixes resolve |
| Existing tests hardcoded to old OpenRouterBackend signature | test | 2026-04-22 | no | Default arg makes change backward-compatible |

## Relationships

- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
- FEEDS INTO: [[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]
- FEEDS INTO: [[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]

## Backlinks

[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
[[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]
[[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]

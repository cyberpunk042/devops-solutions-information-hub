---
title: "E011 M004 — Circuit Breakers and Fallback Chain (per-backend tuning)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 85
progress: 0
stages_completed: [document]
artifacts: []
epic: "E011"
depends_on:
  - "E011-m002"
  - "E011-m003"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-routing-integration-aicp-tiers
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E011-routing-integration-aicp-tiers.md
  - id: aicp-circuit-breaker
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/circuit_breaker.py
  - id: aicp-controller
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/controller.py
tags: [module, p1, e011, aicp, circuit-breaker, failover, reliability, k2-6]
---

# E011 M004 — Circuit Breakers and Fallback Chain

## Summary

AICP already ships a `CircuitBreaker` class (`aicp/core/circuit_breaker.py`, lines 1–166) with CLOSED / OPEN / HALF_OPEN states wired into the `Controller` (`aicp/core/controller.py:170–176`). What's missing is per-backend tuning for the new K2.6 tiers and a documented, tested fallback chain. This module defines per-backend thresholds (local has different failure semantics than a paid online tier), ensures `build_breakers()` picks up the new backends, and adds an integration test proving the fallback cascade works end-to-end.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T023 | Add per-backend circuit_breaker config stanzas to default.yaml | 100% | 0% | draft |
| T024 | Verify build_breakers() creates breakers for k2_6_openrouter + k2_6_local | 90% | 0% | draft |
| T025 | Write fallback-chain integration test (simulate 3 failures → next tier) | 80% | 0% | draft |
| T026 | Document fallback chain in wiki/spine/standards/aicp-fallback-chain.md | 90% | 0% | draft |

## Dependencies

- **E011 M002** + **M003** — backends must be registered so `build_breakers()` has something to wrap.
- **E011 M001** — `failover_chain` list already contains the new tiers.

## Done When

- [ ] `config/default.yaml` has a `circuit_breaker:` section with per-backend overrides
- [ ] `build_breakers()` returns a breaker for every backend key in `backends` dict (including `k2_6_openrouter`, `k2_6_local`)
- [ ] Breaker for `k2_6_local` has tighter thresholds (1 failure → OPEN) since failures are nearly instant (TCP refused)
- [ ] Breaker for `k2_6_openrouter` has moderate thresholds (3 failures → OPEN, 30s recovery)
- [ ] Breaker for `claude` (Anthropic-direct) has loose thresholds (5 failures → OPEN, 120s recovery) — it's the last resort
- [ ] Integration test: inject 3 consecutive HTTP 500s from `k2_6_openrouter` → breaker opens → router falls through to `openrouter` (classic Opus/GPT) on attempt 4
- [ ] Documentation page `wiki/spine/standards/aicp-fallback-chain.md` exists with diagram + threshold table + "what does OPEN mean operationally" explainer
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Per-backend breaker config

Add to `config/default.yaml`:

```yaml
circuit_breaker:
  # Global defaults (already present in AICP if set)
  failure_threshold: 3
  recovery_timeout: 30
  half_open_max: 1

  # Per-backend overrides — deep-merged into each backend's breaker on build
  per_backend:
    local:
      failure_threshold: 2          # local should recover fast; fail fast
      recovery_timeout: 10
    k2_6_local:
      failure_threshold: 1          # TCP probe already in is_available(); one fail = broken
      recovery_timeout: 15
    k2_6_openrouter:
      failure_threshold: 3          # transient network hiccups common
      recovery_timeout: 30
    openrouter:
      failure_threshold: 3
      recovery_timeout: 30
    claude:
      failure_threshold: 5          # last-resort; avoid opening prematurely
      recovery_timeout: 120
```

### Step 2 — Confirm build_breakers() picks these up

In `aicp/core/circuit_breaker.py`, search for `build_breakers`:

```python
def build_breakers(config, backends):
    defaults = {
        "failure_threshold": config.get("circuit_breaker", {}).get("failure_threshold", 3),
        "recovery_timeout":  config.get("circuit_breaker", {}).get("recovery_timeout", 30),
        "half_open_max":     config.get("circuit_breaker", {}).get("half_open_max", 1),
    }
    per_backend = config.get("circuit_breaker", {}).get("per_backend", {})
    return {
        name: CircuitBreaker(name=name, **{**defaults, **per_backend.get(name, {})})
        for name in backends
    }
```

If the current implementation doesn't support `per_backend`, extend it; otherwise just drop in config.

### Step 3 — Integration test

`tests/test_fallback_chain.py`:

```python
def test_k2_6_openrouter_open_falls_through_to_openrouter(monkeypatch, config_all_backends):
    backends = build_backends(config_all_backends)
    breakers = build_breakers(config_all_backends, backends)
    ctrl = Controller(config_all_backends, backends, breakers)

    # Simulate 3 consecutive failures on k2_6_openrouter
    for _ in range(3):
        breakers["k2_6_openrouter"].record_failure()
    assert breakers["k2_6_openrouter"].state == "OPEN"

    # Route a task that would normally land in k2_6_openrouter band
    monkeypatch.setattr("aicp.core.router.analyze_complexity",
                        lambda p, m, c: ComplexityScore(score=0.5, signals={}, recommended_tier="k2_6_openrouter"))
    chosen = ctrl.select_backend(prompt="test", mode=Mode.ACT)
    assert chosen.name == "openrouter"  # next in failover_chain
```

### Step 4 — Document fallback chain

Create `wiki/spine/standards/aicp-fallback-chain.md` with:

- Mermaid diagram showing the 5-tier cascade
- Per-tier trigger conditions (OPEN via breaker vs. `is_available()==False` vs. HTTP timeout)
- Recovery semantics (HALF_OPEN probe behavior)
- Operator playbook: "if k2_6_openrouter opens, what do I look for in logs?"

### Step 5 — Smoke the live chain

```bash
cd /home/jfortin/devops-expert-local-ai
# Kill local KTransformers, verify fallback
pkill -f ktransformers
python3 -m aicp.cli.main run --force-tier k2_6_local "test"
# Expected: breaker opens fast (is_available false), router falls to k2_6_openrouter,
# logged event: {"route": "failover:k2_6_openrouter", "reason": "k2_6_local OPEN"}
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- config/default.yaml aicp/core/circuit_breaker.py
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| `build_breakers()` may not currently accept per-backend overrides | code | 2026-04-22 | no | Extend the function; backward-compatible since missing entries fall back to defaults |
| Defining "failure" for streaming calls — partial response is success or failure? | design | 2026-04-22 | no | Treat >1 chunk delivered as success even if stream terminates early |

## Relationships

- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
- DEPENDS ON: [[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]
- FEEDS INTO: [[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]

## Backlinks

[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
[[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]
[[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]

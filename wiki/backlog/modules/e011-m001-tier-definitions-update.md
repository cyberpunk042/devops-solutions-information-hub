---
title: "E011 M001 — Tier Definitions Update (default.yaml + router.py thresholds)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 90
progress: 0
stages_completed: [document]
artifacts: []
epic: "E011"
depends_on:
  - "E007-m002"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-routing-integration-aicp-tiers
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E011-routing-integration-aicp-tiers.md
  - id: aicp-default-config
    type: repository
    file: /home/jfortin/devops-expert-local-ai/config/default.yaml
  - id: aicp-router
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/router.py
tags: [module, p1, e011, aicp, tier-config, router, complexity-scorer, k2-6, default-yaml]
---

# E011 M001 — Tier Definitions Update

## Summary

Update AICP's backend and routing configuration so Kimi K2.6 becomes a recognized tier — both as a premium-cheap online tier (via OpenRouter) and as a local offline frontier tier (via KTransformers, added in E008). The heart of the change lives in two files: `config/default.yaml` (backend + router config) and `aicp/core/router.py` (complexity-score → tier mapping). This module does ONLY the config + mapping; backend adapter code lives in M002 and M003; circuit-breaker tuning lives in M004.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T014 | Add K2.6 backend entries to config/default.yaml | 100% | 0% | draft |
| T015 | Extend router.py complexity → tier mapping for k2_6_openrouter + k2_6_local | 90% | 0% | draft |
| T016 | Update failover_chain + add fast / quality profiles | 80% | 0% | draft |

## Dependencies

- **E007-m002** — OpenRouter K2.6 route must be proven healthy (done: smoke tests PASSED 2026-04-22).
- None from E008 for this module's M001 scope (local backend comes online via M003; config accepts future `k2_6_local` regardless).
- Operator's OpenRouter key already at `/home/jfortin/devops-expert-local-ai/.env` (73 chars, verified).

## Done When

- [ ] `config/default.yaml` contains a `backends.k2_6_openrouter` stanza with model, max_tokens, timeout, cost hints
- [ ] `config/default.yaml` contains a `backends.k2_6_local` stanza (disabled by default — `enabled: false` — until E008 M002 delivers weights)
- [ ] `config/default.yaml` `router.complexity_thresholds` extended to 4 thresholds → 5 tiers (`local`, `k2_6_openrouter`, `openrouter` for Opus/GPT as fallback premium, `claude`, plus `k2_6_local` when enabled)
- [ ] `config/default.yaml` `router.failover_chain` updated: `[local, k2_6_local, k2_6_openrouter, openrouter, claude]`
- [ ] `aicp/core/router.py` `classify_task_with_reason()` returns `k2_6_openrouter` for scores in its threshold band (e.g., 0.3–0.7)
- [ ] `aicp/core/router.py` recognizes `k2_6_local` when `is_available()` returns True and score is in reasoning-heavy band
- [ ] `config/profiles/fast.yaml` and a new `config/profiles/quality.yaml` demonstrate K2.6 usage
- [ ] Unit test added under `tests/` that asserts score=0.5 with mode=act routes to `k2_6_openrouter`
- [ ] `python3 -m aicp.cli.main --help` still loads (no config-load regressions)
- [ ] All child tasks at status: done

## Procedure (reference — operator / implementer executes in devops-expert-local-ai)

### Step 1 — Inspect current state

```bash
cd /home/jfortin/devops-expert-local-ai
cat config/default.yaml
grep -n "complexity_thresholds\|failover_chain\|classify_task" aicp/core/router.py
```

### Step 2 — Add K2.6 entries to default.yaml

Add under `backends:` block:

```yaml
backends:
  # ... existing entries ...
  k2_6_openrouter:
    # Reuses OpenRouterBackend class in aicp/backends/openrouter.py.
    # K2.6 speaks OpenAI-compatible protocol at openrouter.ai/api/v1/chat/completions.
    model: "moonshotai/kimi-k2.6"
    max_tokens: 8192
    timeout: 300         # K2.6 runs long agentic sessions
    cost_per_1m_prompt_usd: 0.60
    cost_per_1m_completion_usd: 2.50
    enabled: true
  k2_6_local:
    # Adapter landed in E011 M003. Served by KTransformers on /mnt/models.
    # Expects an OpenAI-compatible HTTP endpoint at http://localhost:8091.
    base_url: "http://localhost:8091"
    model: "kimi-k2.6-q2"
    max_tokens: 8192
    timeout: 600
    enabled: false        # flip to true once E008 M002 + M003 delivered
```

### Step 3 — Update router thresholds + failover chain

```yaml
router:
  # Four cut-points → five tier bands.
  # 0.00–0.25 local (Qwen3-8B / gpt-oss-20b in VRAM)
  # 0.25–0.45 k2_6_local when enabled, else k2_6_openrouter
  # 0.45–0.70 k2_6_openrouter (default agentic / coding)
  # 0.70–0.90 openrouter (Opus 4.7 / GPT-5.4 online fallback)
  # 0.90–1.00 claude (Anthropic-direct — edge-case only)
  complexity_thresholds: [0.25, 0.45, 0.70, 0.90]
  failover_chain: [local, k2_6_local, k2_6_openrouter, openrouter, claude]
  tier_map:
    # Optional explicit map if router.py elects a config-driven mapping over hardcoded bands.
    0: local
    1: k2_6_local
    2: k2_6_openrouter
    3: openrouter
    4: claude
```

### Step 4 — Extend aicp/core/router.py

Modify `classify_task_with_reason()` (current logic at lines 154–166) so it reads `router.tier_map` if present, otherwise falls through to hardcoded bands. Skip-tier logic: if a chosen tier's backend returns `is_available() == False`, step sideways along `failover_chain`.

Pseudo-diff anchor (NOT authoritative — read the file before writing the patch):

```python
# aicp/core/router.py, around line 154
thresholds = config.get("router", {}).get("complexity_thresholds", [0.3, 0.6])
tier_map   = config.get("router", {}).get("tier_map")
chain      = config.get("router", {}).get("failover_chain", ["local", "openrouter", "claude"])

if tier_map:
    # N thresholds → N+1 bands; pick band index for score.
    idx = sum(1 for t in thresholds if score >= t)
    chosen = tier_map.get(idx, chain[-1])
else:
    # Legacy 2-threshold path kept for backward compat.
    chosen = chain[0] if score < thresholds[0] else (chain[1] if score < thresholds[1] else chain[2])

# Availability fallback
chosen = _first_available(chosen, chain, backends)
```

### Step 5 — Add profiles

```bash
# config/profiles/quality.yaml (new file)
cat > config/profiles/quality.yaml <<'EOF'
name: quality
description: "Maximize reasoning quality per dollar — K2.6 by default, Opus only for top 10%."
router:
  complexity_thresholds: [0.20, 0.40, 0.65, 0.92]
backends:
  k2_6_openrouter:
    max_tokens: 16384
EOF
```

### Step 6 — Test

```bash
cd /home/jfortin/devops-expert-local-ai
python3 -m aicp.cli.main --help     # loads without error
python3 -m pytest tests/ -k router  # existing tests still green
python3 -m pytest tests/ -k k2_6    # new tests for K2.6 classification
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- config/default.yaml aicp/core/router.py
rm -f config/profiles/quality.yaml
```

Backups of operator-modified configs (`~/.aicp/config.yaml`, `.aicp/config.yaml` under project) remain untouched; they override defaults and are safe.

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| K2.6 local backend not yet live | dependency | 2026-04-22 | no | Resolves via E008 M002 + E011 M003; `enabled: false` preserves forward-compat |
| Complexity scorer may need new signals for agentic/tool-heavy prompts | design | 2026-04-22 | no | Noted for E011 M005 (observation-driven tuning) |

## Relationships

- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[e007-m002-harness-interactive-validation|e007-m002-harness-interactive-validation]]
- FEEDS INTO: [[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
- FEEDS INTO: [[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]

## Backlinks

[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[e007-m002-harness-interactive-validation|e007-m002-harness-interactive-validation]]
[[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
[[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]

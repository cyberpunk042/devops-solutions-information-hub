---
title: "Decision — 4-Tier Router with Configurable Profiles over Hardcoded Routing"
aliases:
  - "Decision — 4-Tier Router with Configurable Profiles over Hardcoded Routing"
  - "Decision: 4-Tier Router with Profiles"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: high
maturity: seed
reversibility: easy
derived_from:
  - model-local-ai
  - gateway-centric-routing
created: 2026-04-18
updated: 2026-04-18
sources:
  - id: aicp-router
    type: file
    file: aicp/core/router.py
    description: "4-tier router implementation with score-based dispatch (AICP project)"
  - id: aicp-profiles
    type: directory
    file: config/profiles/
    description: "9 profile YAML files: default, fast, offline, thorough, code-review, fleet-light, reliable, dual-gpu, benchmark (AICP project)"
  - id: aicp-circuit-breaker
    type: file
    file: aicp/core/circuit_breaker.py
    description: "Per-backend state machine wired into router dispatch (AICP project)"
  - id: profile-tests
    type: file
    file: tests/test_profiles.py
    description: "49 profile tests (AICP project)"
  - id: aicp-contribution-staging
    type: wiki
    file: raw/articles/from-aicp/decisions/01_drafts/4-tier-router-with-profiles-over-hardcoded-routing.md
    description: "AICP's original submission, 2026-04-18 staged in raw/ before ingestion here"
tags: [decision, router, profiles, architecture, aicp, local-first, transferable, pattern]
contributed_by: "aicp"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-18"
contribution_status: accepted
---

# Decision — 4-Tier Router with Configurable Profiles over Hardcoded Routing

## Summary

AICP routes inference requests through a 4-tier escalation chain (local LocalAI → fleet peer → OpenRouter free tier → Claude) with confidence-scoring at each tier and auto-escalation when quality scores below threshold. The chain order, complexity thresholds, escalation cutoff, and per-mode cloud overrides are all driven by named **configuration profiles** (9 shipped: default, fast, offline, thorough, code-review, fleet-light, reliable, dual-gpu, benchmark) rather than hardcoded in the router. A single `make profile-use PROFILE=<name>` switch coordinates backends + router thresholds + RAG depth + budget + cache + timeouts + circuit breaker config + Docker envs. This is the right design because it lets the same router serve heartbeat duty (Tier-1 only, $0), production fleet operation (full chain, reliability mode), and architecture review (full chain, thorough mode) without code changes.

## Decision

> [!success] Use the 4-tier router with profile-driven configuration. Never hardcode tier order, thresholds, or backend selection.
>
> | Scenario | Profile | Chain |
> |----------|---------|-------|
> | Air-gapped / no cloud | `offline` | local → fleet |
> | Heartbeat duty / status checks | `fleet-light` | local → fleet |
> | Quick interactive responses | `fast` | local → openrouter |
> | Balanced everyday use | `default` | local → fleet → openrouter → claude |
> | Code review / structured output | `code-review` | local → openrouter → claude |
> | Architecture / security audit | `thorough` | full chain (long context, deep RAG) |
> | Production fleet operation | `reliable` | full chain + breaker threshold=2 + warmup + DLQ retries=5 + reports/4h |
> | Dual-GPU MoE inference (19 GB) | `dual-gpu` | full chain + qwen3-30b-a3b primary |
> | Deterministic evaluation | `benchmark` | local only, temp=0, seed=42 |

The router (`aicp/core/router.py`) reads thresholds from the active profile at request time. Adding a new profile is a YAML file; adding a new tier is a code change with backwards-compatible defaults.

## Alternatives

### Alternative 1 — Hardcoded routing (single tier order, fixed thresholds)

Hardcode `local → openrouter → claude` with constant complexity thresholds (e.g., `[0.3, 0.6]`). No profiles, no per-mode overrides.

> [!warning] Rejected: AICP's mission spans heartbeat duty (1B-class local model is enough, $0 target) AND architecture review (Opus required, no compromise). One hardcoded threshold cannot serve both — heartbeat wants `[0.5, 0.9]` (push to local), audit wants `[0.1, 0.3]` (escalate aggressively). Hardcoded thresholds force every operator to fork the router.

### Alternative 2 — Per-request explicit backend (no scoring, no escalation)

Caller specifies `backend=local` or `backend=claude` per request. Router becomes a thin dispatcher.

> [!warning] Rejected: pushes routing decisions to every caller. Fleet agents calling AICP would score complexity themselves, defeating the purpose of a centralized router. Breaks the $0 target — without auto-escalation on quality score, callers either over-call Claude (waste budget) or accept low-quality local-only responses.

### Alternative 3 — Two-tier (local-or-cloud) without intermediate fallback

Router has only `local` and `claude`. No fleet peer tier, no OpenRouter free tier.

> [!warning] Rejected: fleet peer tier (LocalAI cluster ↔ cluster) is the path to Stage 4 reliability — a single LocalAI failure shouldn't immediately escalate to paid Claude. OpenRouter free tier (qwen3-8b:free) is the path to Stage 5 — free cloud fallback when local is degraded but the task doesn't warrant Claude. Removing intermediate tiers makes the chain brittle and expensive.

### Alternative 4 — Single profile with runtime CLI flags only

One default profile + CLI flags (`--no-cloud`, `--max-tokens`, `--temperature`) override at request time.

> [!warning] Rejected: profiles coordinate ~10 settings (backends, router, RAG, budget, cache, timeouts, circuit_breaker, warmup, dlq, metrics, reports, Docker). Asking callers to pass 10 flags per request is unusable. Profiles also let `make profile-use` write `.env` so Docker containers restart with matching `CONTEXT_SIZE`, `THREADS`, etc. — runtime flags can't reach the container.

## Rationale

> [!info] Evidence-backed reasons
>
> 1. **The 5-stage LocalAI Independence mission requires variable routing per stage.** Stage 1 (LocalAI functional) needs heartbeat-friendly thresholds. Stage 2 (route simple ops) needs balanced thresholds. Stage 3 (progressive offload) needs aggressive local-first thresholds. Stage 5 (near-independence) needs `force_cloud_modes: []`. One hardcoded set cannot serve all five without recompiling.
>
> 2. **9 profiles in production use**, tested against `tests/test_profiles.py` (49 tests covering load order, inheritance via `extends:`, deep merge, circular detection). Not theoretical — operational interface.
>
> 3. **Circuit breaker at the per-backend level**, not per-request, means the router is stateful — needs config (failure_threshold, recovery_timeout) per profile. Aggressive `reliable` profile uses threshold=2; permissive `default` uses higher. Hardcoding either breaks the other.
>
> 4. **Docker context size and parallel slots are profile-coupled.** Long-context profiles (`thorough`) want CONTEXT_SIZE=32768 / LLAMACPP_PARALLEL=1; latency-sensitive (`fast`) want CONTEXT_SIZE=8192 / LLAMACPP_PARALLEL=4. The profile must write `.env` AND restart the container, not just tune the router.
>
> 5. **Per-mode cloud overrides** (`force_cloud_modes: [edit, act]`) implement the Three Permission Modes rule that Edit/Act use Claude. Profile-driven means configurable per deployment (research instance can disable; production can enforce).
>
> 6. **Quality escalation threshold** (`score < 0.25 → auto-retry on next tier`) is tunable. `benchmark` sets it to 0 (no escalation, deterministic); `reliable` sets 0.5 (aggressive escalation). Hardcoded would make benchmark meaningless.

## Reversibility

**Easy** — `make profile-use PROFILE=<name>` switches behavior with one command. Remove a profile: delete the YAML, no code change. Add a new tier (5th for Bedrock, e.g.): code change in `router.py` with backwards-compatible default ignoring the new tier in profiles that don't reference it.

The only non-reversible aspect: profile names in operational tooling (Makefile, `.env`, docker-compose) reference profile filenames. Renaming `default` breaks scripts. Adding new profiles is fully reversible.

## Dependencies

If reversed (switch back to hardcoded routing):

- `aicp/core/profiles.py` (~600 lines) becomes dead code
- `tests/test_profiles.py` (49 tests) become dead
- Makefile targets (`profile-list`, `profile-show`, `profile-diff`, `profile-validate`, `profile-use`) become dead
- 9 YAML files in `config/profiles/` become dead config
- Reliability stack (circuit_breaker, dlq, warmup, health_report) loses per-profile tuning
- Docker compose envs become unmanaged (operators edit `.env` directly — regression)
- Fleet integration loses per-agent tier selection

If extended (add a 5th tier):

- `aicp/core/router.py`: add tier dispatch + scoring
- All 9 profiles: opt in by adding the new tier to `failover_chain`
- New backend module (e.g., `aicp/backends/bedrock.py`)
- Circuit breaker config per new backend
- New tests for the 5th tier

## Relationships

- BUILDS ON: [[model-local-ai|Model — Local AI ($0 Target)]]
- IMPLEMENTS: [[gateway-centric-routing|Gateway-Centric Routing]]
- ENABLES: [[per-backend-circuit-breaker-with-failover-chain|Per-Backend Circuit Breaker with Failover Chain]] (per-backend state machine, profile-tuned)
- ENABLES: [[per-day-jsonl-dlq-with-retry-budget|Per-Day JSONL DLQ with Retry Budget]] (failed task persistence, retry count per profile)
- ENABLES: [[single-active-backend-with-lru-eviction|Single-Active Backend with LRU Eviction]] (router coordinates with single-active; tier changes force model swaps)
- RELATES TO: [[profile-as-coordination-bundle|Profile as Coordination Bundle]] (the `~12-setting` bundle switched together by profile activation)
- RELATES TO: [[three-permission-modes-think-edit-act|Three Permission Modes]] (mode is a routing dimension via `force_cloud_modes`)
- RELATES TO: [[skills-as-primary-extension-pattern|Decision — Skills as Primary Extension Pattern]] (skills load conditionally; router selects backend conditionally — same per-request config principle)
- RELATES TO: [[localai-over-ollama-vllm-for-multi-model-orchestration|Decision — LocalAI over Ollama/vLLM]] (the runtime this router's Tier 1 uses)

## Backlinks

[[model-local-ai|Model — Local AI ($0 Target)]]
[[gateway-centric-routing|Gateway-Centric Routing]]
[[per-backend-circuit-breaker-with-failover-chain|Per-Backend Circuit Breaker with Failover Chain]]
[[per-day-jsonl-dlq-with-retry-budget|Per-Day JSONL DLQ with Retry Budget]]
[[single-active-backend-with-lru-eviction|Single-Active Backend with LRU Eviction]]
[[profile-as-coordination-bundle|Profile as Coordination Bundle]]
[[three-permission-modes-think-edit-act|Three Permission Modes]]
[[Decision — Skills as Primary Extension Pattern]]
[[Decision — LocalAI over Ollama/vLLM]]

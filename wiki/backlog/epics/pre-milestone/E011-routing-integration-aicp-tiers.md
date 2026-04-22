---
title: "E011 — Routing Integration (AICP Tiers Updated for K2.6 + Local Stack)"
type: epic
domain: backlog
status: draft
priority: P1
task_type: epic
current_stage: document
readiness: 10
progress: 0
stages_completed: []
artifacts: []
confidence: medium
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md
  - id: model-local-ai
    type: wiki
    file: wiki/spine/models/depth/model-local-ai.md
    title: "Model — Local AI ($0 Target)"
  - id: 2026-consumer-hardware-stack
    type: wiki
    file: wiki/spine/references/2026-consumer-hardware-ai-stack.md
    title: "2026 Consumer-Hardware AI Stack"
tags: [epic, p1, aicp, routing, complexity-scorer, tiers, k2-6, openrouter, local-inference, circuit-breaker, post-anthropic]
---

# E011 — Routing Integration (AICP Tiers Updated for K2.6 + Local Stack)

## Summary

Update AICP's complexity scorer and backend-routing layer to treat the full tier stack as peers: local-interactive (Qwen3-8B, gpt-oss-20b in VRAM) → local-reasoning (Qwopus-27B, gpt-oss-120b disk-offload) → local-batch-frontier (K2.6 Q2 via KTransformers) → **premium-cheap-online (K2.6 via OpenRouter) as the new DEFAULT for agentic/coding** → cloud-premium (Opus 4.7 xhigh) as edge-case only. Includes circuit-breaker configuration per tier, routing-split metric monitoring, and a weekly review ritual.

## Operator Directive

> "We will make this workstation self-autonomous and also integrate the OpenRouter like the rest."

> "I don't want to have to deal with Anthropic and Claude and Opus in the future."

## Goals

- AICP complexity scorer recognizes a new `premium-cheap-online` tier (K2.6 via OpenRouter) and routes agentic/coding workloads there by default.
- Backend adapters exist for: K2.6 OpenRouter, K2.6 local (via E008), and optionally Moonshot-direct as premium/swarm specialty.
- Circuit breaker per backend with sensible thresholds (failures → OPEN → HALF_OPEN probe → CLOSED).
- Routing-split metric (what % goes where) collected daily; weekly review ritual documented.
- Claude (Anthropic-direct) becomes a hard-gated fallback for pure-math / max-stakes only — not the default.

## Done When

- [ ] AICP config file updated (wherever AICP's tier config lives — operator to confirm exact path) with `premium-cheap-online` tier definition + K2.6-OpenRouter backend
- [ ] K2.6-OpenRouter backend adapter exists and responds to health checks
- [ ] K2.6-local backend adapter exists (depends on E008 M008.4) and integrates with AICP router
- [ ] Circuit breaker configured per backend — documented thresholds for failure-count, OPEN timeout, HALF_OPEN probe count
- [ ] Routing-split metric emitting to logs or time-series store; sample 24h window shows K2.6-OpenRouter capturing majority of agentic/coding traffic
- [ ] Weekly routing-review ritual documented in `wiki/spine/standards/routing-review-ritual.md` — what to inspect, what to tune
- [ ] Fallback chain documented: K2.6 OpenRouter OPEN → K2.6 local (if warm) → Opus 4.7 via OpenRouter → Anthropic-direct (only if OpenRouter unavailable)
- [ ] `wiki/log/2026-04-25-*-routing-integration-active.md` records the first day's routing-split metric
- [ ] `python3 -m tools.pipeline post` returns 0 validation errors after all E011 work commits

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper (integration with AICP — production routing logic) |
> | **Estimated modules** | 5 |
> | **Estimated tasks** | 15-20 |
> | **Dependencies** | E007 (OpenRouter backend available), E008 (local K2.6 backend), E010 (hardware ready) |

## Module Breakdown

| Module | Delivers | Est. Tasks |
|--------|----------|-----------|
| [[e011-m001-tier-definitions-update]] | AICP config: 7-tier stack with K2.6-cheap-online as primary agentic | 3 |
| [[e011-m002-k2-6-openrouter-backend-adapter]] | Python adapter wrapping OpenRouter K2.6 as an AICP backend | 3 |
| [[e011-m003-k2-6-local-backend-adapter]] | Python adapter wrapping KTransformers local K2.6 as an AICP backend | 3 |
| [[e011-m004-circuit-breakers-and-fallback-chain]] | Per-backend circuit breaker + documented fallback chain | 3-4 |
| [[e011-m005-routing-metric-and-review-ritual]] | Routing-split metric emission + weekly review doc | 3 |

## Dependencies

- [[E007-openrouter-deadline-de-risk]] (OpenRouter K2.6 route proven)
- [[E008-local-k2-6-offline-frontier-tier]] (local K2.6 usable)
- [[E010-storage-and-hardware-enablement]] (64 GB RAM for local inference headroom)
- AICP codebase / repository — operator to confirm current state and update path. Likely at `/home/jfortin/devops-expert-local-ai/` based on env path.

## Open Questions

> [!question] What's the exact AICP tier-config file path and schema?
> Operator-known; clarify during M011.1 discovery.

> [!question] Does AICP's complexity scorer currently support cost-per-token as a routing dimension, or only complexity class?
> If not, extending it to prefer K2.6-cheap-online (cheap + high-quality) becomes its own task.

> [!question] Where should routing-split metric be emitted — existing AICP metric pipeline, OpenTelemetry, or just structured logs?
> Operator preference; infrastructure fit determines answer.

> [!question] Should Moonshot's Agent Swarm (300 sub-agents) be accessible programmatically via a dedicated tier, or is that future work?
> Parked as future follow-up; not in this epic's scope unless OpenRouter exposes it before milestone close.

## Relationships

- PART OF: [[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
- DEPENDS ON: [[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]
- DEPENDS ON: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
- DEPENDS ON: [[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
- BUILDS ON: [[model-local-ai|Model — Local AI]]
- BUILDS ON: [[2026-consumer-hardware-ai-stack|2026 Consumer-Hardware AI Stack]]

## Backlinks

[[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
[[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]
[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
[[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
[[Model — Local AI]]
[[2026 Consumer-Hardware AI Stack]]

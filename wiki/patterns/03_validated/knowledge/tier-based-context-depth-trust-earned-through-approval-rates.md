---
title: Tier-Based Context Depth — Trust Earned Through Approval Rates
aliases:
  - "Tier-Based Context Depth — Trust Earned Through Approval Rates"
type: pattern
domain: ai-agents
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Three Lines of Defense — Immune System for Agent Quality"
  - "Model: Quality and Failure Prevention"
instances:
  - {'page': 'Three Lines of Defense — Immune System for Agent Quality', 'context': 'Tier profiles control what the doctor shows vs hides from agents at different trust levels'}
  - {'page': 'Harness-Owned Loop — Deterministic Agent Execution', 'context': 'Orchestrator uses tier to determine context depth for dispatch — lightweight agents get minimal context'}
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: openfleet-tiers
    type: observation
    file: raw/articles/openfleet-methodology-scan.md
    description: OpenFleet tier-profiles.yaml (56 lines) + tier_progression.py (352 lines) — data-driven trust progression
tags: [tier-progression, context-depth, trust, approval-rates, agent-quality, cost-optimization, openfleet]
---

# Tier-Based Context Depth — Trust Earned Through Approval Rates

## Summary

Different AI models and agents receive different DEPTHS of context based on their demonstrated reliability. A trainee model gets minimal context (title + stage only), an expert gets full context (contributions inline, complete protocol, full role data). Trust is earned through measured approval rates per task type, not claimed or configured manually. This simultaneously controls QUALITY (untrusted models get guardrails via reduced context) and COST (lightweight context = fewer tokens = cheaper calls).

> [!info] Pattern Reference Card
>
> | Tier | Approval Threshold | Context Depth | Use Case |
> |------|-------------------|---------------|----------|
> | **Expert** | Established track record | Full: task detail, contributions inline, full protocol, full role data, 10 events | Primary model, complex tasks |
> | **Capable** | ≥85% approval rate | Core fields, contribution status only, MUST/MUST NOT, top-3 role items, 5 events | Standard operations |
> | **Flagship-local** | Specialized tier | Core fields, contribution summary, MUST/MUST NOT, top-5 role items, 8 events | Local models (cost optimization) |
> | **Lightweight** | ≥70% approval rate | Title + stage only, contribution names only, short rules, counts only, 0 events | Simple tasks, heartbeats |

## Pattern Description

> [!abstract] What Each Context Depth Controls
>
> | Dimension | Expert | Capable | Lightweight |
> |-----------|--------|---------|-------------|
> | **task_detail** | Full (SP, description, PR, all fields) | Core fields only | Title + stage only |
> | **contributions** | Full inline (architect design, QA tests embedded) | Status only ("received" / "pending") | Names only |
> | **protocol** | Full MUST/MUST NOT + tool sequence | MUST/MUST NOT only | Short rules (1 line each) |
> | **role_data** | Full formatted (all items, messages, directives) | Counts + top 3 items | Counts only |
> | **events_limit** | 10 recent events shown | 5 events | 0 events |
> | **standing_orders** | Full standing orders shown | Omitted | Omitted |

The mechanism: an AI model's approval rate is tracked per task type across rolling 20-record windows. When the approval rate crosses a threshold (70% → lightweight eligible, 85% → capable), the system signals the tier is available. The PO decides actual promotion — data informs but doesn't automate trust.

**Per-task-type overrides:** An agent might be `expert` on feature tasks but `trainee` on security tasks. Trust is NOT global — it's scoped to what the model has demonstrated competence in.

**Cost dimension:** A lightweight heartbeat call might cost 500 tokens. The same heartbeat at expert tier costs 5,000 tokens. For 10 agents heartbeating every 30 seconds, the tier difference is 10x cost reduction on routine calls.

> [!warning] Context Depth Is Not Capability Restriction
>
> A lightweight agent has the same MODEL capabilities — it's the same LLM. What changes is the INFORMATION it receives. Less context means less opportunity to deviate, less to misinterpret, less to overwhelm the context window. For simple tasks (heartbeat, status check, trivial fix), minimal context produces better results than full context because there's less noise.

## Instances

> [!example]- OpenFleet: Full Tier Implementation (4 tiers, production)
>
> **Data tracking:** `PerformanceRecord` stores model, task_type, approved (bool), challenge_passed (bool), timestamp per completed task. Rolling 20-record windows calculate approval rate per model per task type.
>
> **Tier profiles** (config/tier-profiles.yaml, 56 lines):
> - Expert tier: all context dimensions at maximum
> - Capable tier: reduced but functional — agent can still do complex work
> - Flagship-local tier: optimized for local models (cost = $0, quality = variable)
> - Lightweight tier: minimal — suitable for heartbeats, status checks, simple updates
>
> **TierRenderer:** Single class that takes a tier name and renders context at the appropriate depth. Called by orchestrator during dispatch and heartbeat. Same task data, different rendering — no code duplication.
>
> **Promotion flow:** System detects `eligible_for: capable` based on approval rates → PO reviews → PO promotes → tier stored per model per task type. Demotion: 3+ consecutive rejections → auto-flag for review.

> [!example]- OpenArms: Implicit Tiers (no formal system)
>
> OpenArms doesn't have explicit tiers but demonstrates the PRINCIPLE implicitly:
> - Research model: caps at 50% readiness, gets simplified validation (no src/ artifact checks)
> - Feature-development model: full validation, all 5 stages, strict gates
> - Hotfix model: minimal process (implement + test only), trusts the developer knows the fix
>
> The model SELECTION acts as an implicit tier — simpler models get less process overhead. But there's no data-driven progression. The operator manually selects which model applies.

## When To Apply

> [!tip] Conditions for Tier-Based Context
>
> - **Multiple model backends** — flagship vs local, expensive vs cheap, different capability levels
> - **High call volume** — heartbeats, status checks, routine operations that don't need full context
> - **Cost sensitivity** — token usage matters, especially for fleet operations at scale
> - **Measurable approval rates** — you have a review process that generates pass/fail data per task
> - **Heterogeneous task complexity** — some tasks need full context, others need minimal

## When Not To

> [!warning] When Tiers Add Complexity Without Value
>
> - **Solo agent, single model** — no model variation to tier. Use methodology models (feature-dev vs research) for complexity scaling instead.
> - **No approval data** — without measured outcomes, tier assignment is guesswork. Start with a single tier and add progression after you have data.
> - **All tasks are complex** — if every task needs full context, tiers just add configuration overhead.
> - **Cost is not a constraint** — if token usage doesn't matter, full context for everything is simpler.

## Open Questions

> [!question] ~~Can tier progression be automated safely?~~
> **RESOLVED:** Yes with guardrails. Auto-measure approval rate over N tasks. >90% over 10+ tasks = auto-promote candidate. Tier DOWN = instant on critical failure. Automation measures, human confirms.
> Currently PO decides promotions. Could the system auto-promote at 95%+ approval across 50+ records? Risk: one bad auto-promotion on security-critical tasks.

> [!question] ~~Should context depth be continuous rather than discrete tiers?~~
> **RESOLVED:** Discrete tiers. Actionable — agent knows its tier and gets corresponding tools/depth. Continuous scores are harder to act on. Tiers with measurable promotion criteria.
> Instead of 4 tiers, a continuous scale (0.0 to 1.0) that interpolates between minimal and full context. More granular but harder to reason about.

### How This Connects — Navigate From Here

> [!abstract] From This Pattern → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **How is trust earned?** | [[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]] — approval rates per model per task type, rolling 20-record windows |
> | **How does context depth relate to structured context?** | [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]] — same structural skeleton at every tier, content depth varies |
> | **What about cost optimization?** | 10x cost reduction on routine calls (500 tokens lightweight vs 5,000 expert). Budget mode changes propagate to CRON intervals. |
> | **How does this fit Goldilocks?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — trust tier is one of 7 identity dimensions. Expert gets full context. Trainee gets minimal. |
> | **Solo agent version?** | No formal tiers. Implicit: methodology model selection (research = light, feature-dev = full) acts as tier approximation. |

## Relationships

- DERIVED FROM: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
- DERIVED FROM: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
- RELATES TO: [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
- RELATES TO: [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-context-engineering|Model — Context Engineering]]
[[identity-profile|OpenFleet — Identity Profile]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]]
[[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]]

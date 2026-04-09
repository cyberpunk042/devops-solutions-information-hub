---
title: "Model: Quality + Failure Prevention"
type: learning-path
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [model, learning-path, spine, quality, failure-prevention, harness, immune-system, rework]
---

# Model: Quality + Failure Prevention

## Summary

The Quality + Failure Prevention model describes how to prevent AI agent mistakes before they propagate into irreversible state. The core thesis: LLM-level prompt guidance is insufficient — quality must be enforced at execution time through deterministic mechanisms (hooks, runtime guardrails, 3-strike rules, immune system checks) that cannot be bypassed by a well-crafted prompt. The model is grounded in four converging evidence sources: harness engineering (TypeScript guardrail engine with 13 rules), OpenFleet's doctor.py (24 rules from 16 post-mortems), rework prevention cost modeling (2.5-3.5x rework multiplier), and the wiki's own operational lessons about what goes wrong when stages are skipped or sources are described rather than read.

## Prerequisites

- Familiarity with Claude Code hooks (PreToolUse, PostToolUse, Stop)
- Understanding of the Plan → Execute → Review cycle
- Basic DevOps background: what a circuit breaker is, what a post-mortem produces

## Sequence

### Layer 2 — Core Concepts

1. **Harness Engineering** ([[Harness Engineering]])
   Entry point. Explains the shift from prompt guidance to runtime enforcement. Covers the 5-verb workflow (Setup → Plan → Work → Review → Release), the 13 TypeScript guardrail rules (R01-R13) enforced via hooks, and the enforcement level hierarchy: Level 0 (CLAUDE.md, hope) → Level 3 (runtime guardrails) → Level 4 (deterministic orchestration). The Breezing mode's Planner+Critic pre-review quantifies the rework prevention ROI: ~5.5x planning overhead vs ~4x without it, but break-even at only 22% rework probability.

2. **Immune System Rules** ([[Immune System Rules]])
   The production-grade implementation. 24 rules extracted from 16 post-mortems, codified in OpenFleet's doctor.py. Five rule categories: liveness, loop detection, state integrity, behavioral security, resource exhaustion. The 3-strike rule tolerates transient anomalies while catching persistent failures. Zero LLM calls — pure Python state evaluation. Runs at step 6 of the 9-step orchestrator cycle, before any dispatch.

3. **Rework Prevention** ([[Rework Prevention]])
   The cost model. Rework is not additive — it's multiplicative: revert + re-plan + re-execute + re-verify ≈ 2.5T to 3.5T. In a multi-agent fleet with 5 dependent tasks, one bad dispatch corrupts the entire sprint. Four prevention layers: planning quality, execution guardrails, review gates, context management. Maps directly to the wiki's three ingestion modes (guided = maximum prevention, smart = risk-calibrated, auto = throughput-first).

4. **Deterministic Shell, LLM Core** ([[Deterministic Shell, LLM Core]])
   The architectural pattern that unifies harness engineering and immune system rules. The LLM operates only in the execution phase — surrounded on both sides by deterministic Python (pre-checks before, validation after). The shell provides infrastructure-level enforcement that cannot be social-engineered. The core provides the reasoning capability that deterministic code cannot replicate.

### Layer 4 — Lessons

5. **Never Synthesize from Descriptions Alone** ([[Never Synthesize from Descriptions Alone]])
   The wiki-specific lesson: read the source, never summarize from someone else's summary of it. One application of the broader principle that quality gates must be at primary sources, not secondhand accounts.

6. **Never Skip Stages Even When Told to Continue** ([[Never Skip Stages Even When Told to Continue]])
   The agent must not treat "continue" as permission to skip validation, post-chain steps, or review gates. Instructions that push forward do not override hard quality constraints.

7. **Shallow Ingestion Is Systemic, Not Isolated** ([[Shallow Ingestion Is Systemic, Not Isolated]])
   What happens when quality gates are soft: thin pages accumulate, relationships stay sparse, and the wiki's evolution pipeline never has enough signal to promote good candidates. One skipped gate creates systematic downstream degradation.

8. **Infrastructure Must Be Reproducible, Not Manual** ([[Infrastructure Must Be Reproducible, Not Manual]])
   Manual steps are quality gaps. Any setup step not encoded in a script, service template, or IaC file will silently diverge across environments and sessions.

9. **The Agent Must Practice What It Documents** ([[The Agent Must Practice What It Documents]])
   Operational integrity: if the wiki documents a quality gate as required, the agent must actually enforce it — not write about enforcing it while skipping it.

### Layer 6 — Decisions

10. **Decision: MCP vs CLI for Tool Integration** ([[Decision: MCP vs CLI for Tool Integration]])
    Relevant to quality: MCP schemas loaded into every session create context pressure that degrades accuracy. The decision to use CLI-first tools for wiki operations is itself a quality decision — fewer tokens, higher accuracy per the degradation curve.

## Outcomes

After completing this path you understand:

- Why runtime enforcement (hooks, doctor.py) is categorically stronger than prompt guidance
- The 5-category immune system rule taxonomy and how each maps to real failure modes
- The compound rework cost model and the 22% break-even threshold for prevention investment
- How the Deterministic Shell + LLM Core pattern allocates responsibility between code and model
- The wiki's specific quality lessons (never describe, never skip, shallow is systemic)
- How to configure Claude Code hooks to implement wiki-level guardrails (block deletion of high-connectivity pages, require post-chain completion)

## Relationships

- BUILDS ON: [[Harness Engineering]]
- BUILDS ON: [[Immune System Rules]]
- BUILDS ON: [[Rework Prevention]]
- IMPLEMENTS: [[Deterministic Shell, LLM Core]]
- RELATES TO: [[Model: Automation + Pipelines]]
- RELATES TO: [[Model: SFIF + Architecture]]
- FEEDS INTO: Model: Local AI ($0 Target)

## Backlinks

[[Harness Engineering]]
[[Immune System Rules]]
[[Rework Prevention]]
[[[[Deterministic Shell]]
[[LLM Core]]]]
[[Model: Automation + Pipelines]]
[[Model: SFIF + Architecture]]
[[Model: Local AI ($0 Target)]]
[[Model: Design.md + IaC]]

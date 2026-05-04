---
title: "Learning Path — Post-Anthropic 3-Layer Stack Assembly (Multica + Harness + AICP, Session Arc 2026-04-28)"
aliases:
  - "3-Layer Stack Learning Path"
  - "Multica + AICP + 3090 Reading Order"
  - "Post-Anthropic Stack 2026-04-28 Path"
type: learning-path
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-28
updated: 2026-04-28
last_reviewed: 2026-04-28
sources:
  - id: parent-epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md
    description: "The epic this path navigates. Authored 2026-04-28 to capture the milestone-class assembly of orchestrator + harness + provider layers."
  - id: multica-synth
    type: wiki
    file: wiki/sources/tools-integration/src-multica-managed-agents-platform.md
    description: "The Layer-1 source synthesis for Multica — the new orchestrator-layer artifact that this path's reading order flows from."
  - id: decision-page
    type: wiki
    file: wiki/decisions/01_drafts/adopt-multica-as-orchestrator-layer-post-anthropic-stack-2026-04.md
    description: "The architectural decision artifact. Captures alternatives, rationale, reversibility."
tags: [learning-path, spine, post-anthropic, 3-layer-stack, multica, harness, aicp, orchestrator, anti-vendor-lock-in, mission-2026-04-28, navigation, curated-reading]
---

# Learning Path — Post-Anthropic 3-Layer Stack Assembly (Session Arc 2026-04-28)

## Summary

Curated reading order for the **~12 wiki artifacts** produced during the 2026-04-28 session arc that assembled the post-Anthropic 3-layer AI stack: Multica (orchestrator) × harness (Claude Code / OpenCode / others) × AICP (provider routing) × Ollama Cloud / OpenRouter / local providers × incoming RTX 3090 hardware × MIT RLM-Qwen3-8B HF checkpoint. Designed for a reader who wants to internalize the assembly efficiently — whether picking up cold tomorrow, deciding whether to adopt the same architecture, executing the smoke-test runbook, or auditing the wiki's coverage of the orchestrator-layer documentation gap that 2026-04-28 closed. Total reading time for the full path: **~2-3 hours**; the 30-minute fast-path (Goal A) covers the architectural shape without the implementation detail.

## Prerequisites

> [!info] Before starting this path
>
> | Prerequisite | Why |
> |---|---|
> | Familiarity with [Anti-Vendor-Lock-In Lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) Evidence 1-9 | Evidence 10 (orchestrator layer) builds on these |
> | Familiarity with [4 governing principles](../../lessons/04_principles/hypothesis/) | The 3-layer stack maps directly to P1 (Infrastructure>Instructions), P3 (Goldilocks), P4 (Declarations Aspirational) |
> | Optional: skim [RLM thread learning-path](rlm-thread-evidence-chain-2026-04-27.md) | Same session-arc-pattern from 2026-04-27 — comparable shape |
> | Optional: AICP authoritative state at `~/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md` | The AICP-side context the 3-layer stack composes with |

## Sequence

### Goal A — Understand the 3-Layer Architecture (30 minutes)

For a reader who wants the headline architecture + key decisions without the implementation detail.

> [!abstract] Path A — Architecture in 30 Minutes
>
> | # | Read | Why | Rough time |
> |---|---|---|---|
> | 1 | [Multica Synthesis](../../sources/tools-integration/src-multica-managed-agents-platform.md) — Summary + Reference Card + Operator-Validated section | The new orchestrator layer; the canonical source. The "Operator-Validated Per-Agent Shaping (2026-04-28)" section is load-bearing. | 10 min |
> | 2 | [Decision: Adopt Multica](../../decisions/01_drafts/adopt-multica-as-orchestrator-layer-post-anthropic-stack-2026-04.md) — Decision matrix + Rationale | Why Multica chosen, alternatives rejected, the 5 properties grounding the decision | 10 min |
> | 3 | [Anti-Vendor-Lock-In Lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) Evidence 10 only | Mission alignment — 3-layer composability is anti-vendor-lock-in at three structural layers, not two | 10 min |
>
> **Outcome**: you can articulate (a) what the 3-layer stack is, (b) why Multica was chosen at the orchestrator layer, (c) how it advances the anti-vendor-lock-in mission claim.

### Goal B — Decide Whether to Adopt (1 hour)

For an operator (or fleet PM) deciding whether the 3-layer pattern fits their own stack.

> [!abstract] Path B — Decision-Maker Sequence
>
> | # | Read | Focus on |
> |---|---|---|
> | 1 | [Decision: Adopt Multica](../../decisions/01_drafts/adopt-multica-as-orchestrator-layer-post-anthropic-stack-2026-04.md) | Full Decision Matrix + Alternatives + Reversibility |
> | 2 | [Multica Synthesis](../../sources/tools-integration/src-multica-managed-agents-platform.md) | Architecture + Operator-Validated Per-Agent Shaping (the 7 dimensions) |
> | 3 | [AI Model × Provider × Harness Decision Matrix 2026](../references/ai-model-provider-harness-decision-matrix-2026.md) § Orchestrator Layer | 3-axis matrix update (orchestrator × harness × provider) |
> | 4 | [Anti-Vendor-Lock-In Lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) Evidence 10 | Mission framing |
> | 5 | [Tier-0 Candidate Comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) — Phase-1 Path section | Concrete model + hardware fit alongside the 3-layer architecture |
>
> **Outcome**: you can answer for your own stack: should I adopt Multica? With what alternatives? At what cost? With what migration risk if reversed?

### Goal C — Execute the Smoke Test (1.5 hours including hands-on)

For an operator ready to validate the 3-layer composability empirically on their own machine.

> [!abstract] Path C — Smoke-Test Execution Sequence
>
> | # | Read | Focus on |
> |---|---|---|
> | 1 | [M001 — Multica `custom_env` Mechanism](../../backlog/modules/post-anthropic-3-layer-m001-multica-per-agent-provider-config.md) | The 6 wiring recipes (Recipe 1 = AICP-routed; Recipe 2 = Ollama Cloud direct; Recipe 5 = `custom_args`; Recipe 6 = skills) |
> | 2 | [M002 — Harness-Level Integration](../../backlog/modules/post-anthropic-3-layer-m002-harness-level-integration-mcp-wiring-opencode-config.md) | Per-harness comparison matrix + research-wiki MCP integration recipe + OpenCode gotchas |
> | 3 | [M003 — Smoke-Test Runbook](../../backlog/modules/post-anthropic-3-layer-m003-multica-aicp-ollama-cloud-smoke-test-runbook.md) | Variant A + Variant B with pre-flight checks + diagnostics |
> | 4 | (Hands-on) Run M003's Variant A → Variant B in Multica's UI | The empirical verification gate — converts the architecture from documented to operator-validated |
> | 5 | (After validation) Capture the actual URLs (Ollama Cloud Anthropic-compat endpoint + AICP local endpoint) and feed back to M001 / M003 for future reference |
>
> **Outcome**: you have empirically verified 3-layer composability on your own hardware. The stack works end-to-end.

### Goal D — Full Internalization (2-3 hours)

For thorough internalization of the entire session arc.

> [!info] Path D — Complete Sequence (12 artifacts in origin order)
>
> | # | Read | Type | Why |
> |---|---|---|---|
> | 1 | [Multica Synthesis](../../sources/tools-integration/src-multica-managed-agents-platform.md) | source-synthesis | The Layer-1 anchor |
> | 2 | [AI Decision Matrix 2026](../references/ai-model-provider-harness-decision-matrix-2026.md) § Orchestrator Layer (added 2026-04-28) | reference (spine) | 3-axis matrix update |
> | 3 | [Anti-Vendor-Lock-In Lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) Evidence 10 | lesson | Mission-claim extension to 3-layer empirical |
> | 4 | [Tier-0 Candidate Comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) — Phase-1 Path section (revised 2026-04-28) | comparison | Concrete model selection within the 3-layer architecture |
> | 5 | [RLM-Qwen3.6-27B Operations Plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) Phase-1 vs Phase-2 framing (revised 2026-04-28) | operations-plan | The deferred fine-tune option, properly Phase-2-conditional |
> | 6 | [Epic — Post-Anthropic 3-Layer Stack Assembly](../../backlog/epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md) | epic | The milestone-class assembly framing |
> | 7 | [Milestone — Post-Anthropic Self-Autonomous Stack](../../backlog/milestones/post-anthropic-self-autonomous-stack.md) (3-layer extended acceptance criteria) | milestone | Parent context |
> | 8 | [M001 — Multica `custom_env` Mechanism](../../backlog/modules/post-anthropic-3-layer-m001-multica-per-agent-provider-config.md) | module | The unblocking mechanism + 6 recipes |
> | 9 | [M002 — Harness-Level Integration](../../backlog/modules/post-anthropic-3-layer-m002-harness-level-integration-mcp-wiring-opencode-config.md) | module | Per-harness specifics + MCP integration |
> | 10 | [M003 — Smoke-Test Runbook](../../backlog/modules/post-anthropic-3-layer-m003-multica-aicp-ollama-cloud-smoke-test-runbook.md) | module | Operator-actionable validation |
> | 11 | [Decision: Adopt Multica](../../decisions/01_drafts/adopt-multica-as-orchestrator-layer-post-anthropic-stack-2026-04.md) | decision | Architectural choice formalized |
> | 12 | (Memory) `project_multica_self_hosted_2026_04_28.md` + `project_rtx_3090_acquired_2026_04_27.md` + `project_rlm_qwen3_8b_hf_checkpoint_live.md` + `project_ollama_cloud_consensus_2026_04.md` | project memory | Operator-specific facts (paths, hardware ETA, registered tools) |

### Goal E — Audit the Mission Claim at 3 Layers (45 minutes)

For a reader auditing the wiki's anti-vendor-lock-in claim with the new orchestrator-layer evidence.

> [!abstract] Path E — Mission-Claim Auditor Sequence
>
> | # | Read | Why |
> |---|---|---|
> | 1 | [Anti-Vendor-Lock-In Lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) — Insight + Evidence 1-10 | The mission claim with all 10 evidence items including the new orchestrator layer |
> | 2 | [Multica Synthesis](../../sources/tools-integration/src-multica-managed-agents-platform.md) — Mission Alignment section | Three substitution dimensions composable; Apache 2.0 + 10 harnesses + self-host = no single-vendor multi-layer control |
> | 3 | [AI Decision Matrix 2026](../references/ai-model-provider-harness-decision-matrix-2026.md) § Orchestrator Layer + Lock-in Risk table | Per-layer lock-in risk assessment |
> | 4 | [Decision: Adopt Multica](../../decisions/01_drafts/adopt-multica-as-orchestrator-layer-post-anthropic-stack-2026-04.md) — Reversibility section | Honest scoping of what's preserved vs migrated vs lost on reversal |
>
> **Outcome**: you can independently audit whether anti-vendor-lock-in holds at 3 structural layers (orchestrator × harness × provider) per the wiki's claim. Distinct from Goal A's architecture-level reading because this audit is per-layer empirical verification, not just structural awareness.

> [!success]- **EXTENDED 2026-04-30 — 4th-layer extension via the Trust-Layer Learning Path**
>
> This 3-layer path is now followed by the [Trust-Layer Learning Path (2026-04-30)](trust-layer-tamper-proof-inference-2026-04-30.md), which adds a fourth substitutable layer (trust / confidential-compute) with cypher + decypher + compression composed for **80–90% space saved on large context**, seamless and performance-positive. The two paths compose: this 3-layer path delivers the substrate (orchestrator × harness × provider); the trust-layer path delivers the security stance and compression-encryption pipeline that runs *on top of* whichever orchestrator × harness × provider triple is selected. Per [anti-vendor-lock-in lesson Evidence 11](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md), the mission claim now extends to 4 structural layers, not 3.

## Outcomes

> [!success] After completing this path you should be able to:
>
> 1. **Articulate the 3-layer post-Anthropic stack architecture**: orchestrator (Multica) × harness (Claude Code / OpenCode / 8 others) × provider (10+ via AICP routing). Independent layers, no single vendor controls more than one.
> 2. **Decide whether Multica fits a given stack** based on its 7-row decision matrix (solo single-harness no, solo multi-harness yes, team yes, governance-heavy no, etc.) and the 4 alternatives evaluated and rejected.
> 3. **Configure a Multica agent for any provider routing** using `custom_env` (per M001's 6 recipes) including AICP-routed, Ollama Cloud direct, multi-agent multi-provider, etc.
> 4. **Wire research-wiki MCP into Multica Claude Code agents** (M002's recipe) — making 28 wiki tools available inside Multica's task lifecycle.
> 5. **Execute the empirical 3-layer smoke test** (M003's runbook with Variant A and B) and diagnose 6 documented failure modes.
> 6. **Articulate the anti-vendor-lock-in mission claim at 3 structural layers** (Evidence 10) — and explain why this is structurally stronger than 2-layer claims.
> 7. **Identify the architectural decision's reversibility**: moderate, with explicit migration paths if Multica is ever swapped.

## Relationships

- BUILDS ON: [[post-anthropic-stack-3-layer-assembly-multica-aicp-3090|Epic — Post-Anthropic 3-Layer Stack Assembly]] — the parent epic this path navigates
- BUILDS ON: [[src-multica-managed-agents-platform|Multica Synthesis]]
- BUILDS ON: [[adopt-multica-as-orchestrator-layer-post-anthropic-stack-2026-04|Decision: Adopt Multica]]
- BUILDS ON: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] (Evidence 10 specifically)
- BUILDS ON: [[ai-model-provider-harness-decision-matrix-2026|AI Decision Matrix 2026]] (orchestrator dimension)
- PARALLELS: [[rlm-thread-evidence-chain-2026-04-27|RLM Thread Learning Path (2026-04-27)]] (same session-arc pattern, different topic — paired curated paths for the operator's two major mission threads)
- RELATES TO: [[methodology-fundamentals|Methodology Fundamentals Learning Path]] (the wiki's broader learning-path system)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (concrete 2026 stack assembly with empirical components)
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (operationalizes the Specialty Routing + Resilience Playbook sections)

## Backlinks

[[Epic — Post-Anthropic 3-Layer Stack Assembly]]
[[src-multica-managed-agents-platform|Multica Synthesis]]
[[Decision: Adopt Multica]]
[[Anti-Vendor-Lock-In Lesson]]
[[ai-model-provider-harness-decision-matrix-2026|AI Decision Matrix 2026]]
[[RLM Thread Learning Path (2026-04-27)]]
[[Methodology Fundamentals Learning Path]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]

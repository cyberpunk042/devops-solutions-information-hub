---
title: "Learning Path — Trust Layer: Tamper-Proof Inference Pipeline (Cypher + Decypher + Compression for 80–90% Space Saved on Large Context, Session Arc 2026-04-30)"
aliases:
  - "Trust-Layer Learning Path"
  - "Tamper-Proof Inference Reading Order"
  - "Cypher Decypher Compression Path"
  - "4th-Layer Path"
type: learning-path
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-30
updated: 2026-04-30
last_reviewed: 2026-04-30
sources:
  - id: parent-epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md
    description: "The Trust-Layer Epic this path navigates — milestone-class assembly of the 4th substitutable layer (trust / confidential-compute) on top of orchestrator × harness × provider"
  - id: design-synthesis
    type: wiki
    file: wiki/domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md
    description: "Concept page that captures the operator-authored design — the synthesis grounding for the 80–90% composition math, integration levers L0–L4, and supporting paths"
  - id: caveman-synth
    type: wiki
    file: wiki/sources/tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md
    description: "Layer-1 source synthesis for the operator-confirmed compression reference — Wenyan-Full mode delivers 80–90% character reduction at a single layer"
  - id: session-log
    type: wiki
    file: wiki/log/2026-04-30-session-log-trust-layer-arc-tamper-proof-inference-cypher-decypher-compression.md
    description: "Session log capturing the arc — verbatim directives, phase-by-phase narrative, state delta, artifact inventory, pending items"
  - id: prior-path
    type: wiki
    file: wiki/spine/learning-paths/post-anthropic-3-layer-stack-2026-04-28.md
    description: "The prior session arc's learning path (3-layer stack, 2026-04-28) — this path is its 4th-layer extension"
tags: [learning-path, spine, trust-layer, fourth-layer, tamper-proof, cypher, decypher, compression, caveman, wenyan, rlm, anti-vendor-lock-in, post-anthropic, mission-2026-04-30, navigation, curated-reading]
---

# Learning Path — Trust Layer: Tamper-Proof Inference Pipeline (Session Arc 2026-04-30)

## Summary

Curated reading order for the **~13 wiki artifacts** produced during the 2026-04-30 session arc that authored the **4th substitutable layer (trust / confidential-compute)** on top of the post-Anthropic 3-layer stack (orchestrator × harness × provider). The arc grounds the operator's tamper-proof-inference design — cypher + decypher + compression for **80–90% space saved on large context, seamless and performance-positive**. Designed for a reader who wants to internalize the design efficiently — whether picking up cold tomorrow, deciding whether to adopt the L2 default on RTX 3090, designing the M001 reference pipeline when 3090 hardware lands, or auditing the wiki's 4-layer mission claim. Total reading time for the full path: **~2–3 hours**; the 30-minute fast-path (Goal A) covers the architectural shape and the 80–90% composition math without the implementation detail.

## Prerequisites

> [!info] Before starting this path
>
> | Prerequisite | Why |
> |---|---|
> | Familiarity with [Anti-Vendor-Lock-In Lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) Evidence 1–10 | Evidence 11 (trust layer) builds on these; the 4-layer claim composes cleanly with the prior 3-layer claim |
> | Familiarity with the [Post-Anthropic 3-Layer Stack Learning Path](post-anthropic-3-layer-stack-2026-04-28.md) | The 4th layer extends that assembly — same structural pattern at one layer up |
> | Familiarity with [4 governing principles](../../lessons/04_principles/hypothesis/) | The trust layer maps to P1 (Infrastructure > Instructions for tamper-resistance), P4 (Declarations Aspirational Until Verified for security claims) |
> | Optional: skim [RLM Synthesis](../../sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md) | RLM is the script-orientation substrate the trust layer composes with |
> | Optional: skim [Markdown-as-IaC Model](../models/agent-config/model-markdown-as-iac.md) | The Markdown-rules DSL pattern the operator named |

## Sequence

### Goal A — Understand the 4th Layer Architecture (30 minutes)

For a reader who wants the headline architecture + the 80–90% composition math without implementation detail.

> [!abstract] Path A — Architecture in 30 Minutes
>
> | # | Read | Why | Rough time |
> |---|---|---|---|
> | 1 | [Concept — Secure Tamper-Proof Model on Shared GPU](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) — Summary + Verbatim Directive + Operational Properties + Key Insights | Operator-authored design ground truth; 80–90% composition math; L0–L4 opt-ins | 15 min |
> | 2 | [Synthesis — Caveman](../../sources/tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md) — Reference Card + Wenyan-Full row | The prompt-layer empirical anchor — 80–90% character reduction at a single layer | 5 min |
> | 3 | [Anti-Vendor-Lock-In Lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) Evidence 11 only | Mission alignment — 4-layer empirical claim with 6 substitution axes within the trust layer | 10 min |
>
> **Outcome**: you can articulate (a) what the 4th (trust) layer is, (b) the 80–90% composition math composed of caveman + UD-IQ2 + KV-cache + cypher overlay, (c) how it advances the anti-vendor-lock-in mission claim from 3 to 4 layers.

### Goal B — Decide Whether to Adopt the L2 Default (1 hour)

For an operator (or peer evaluating their own stack) deciding whether the trust-layer L2 default fits.

> [!abstract] Path B — Decision-Maker Sequence
>
> | # | Read | Focus on |
> |---|---|---|
> | 1 | [Concept page](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) | Full Integration Levers table (L0 → L4) + Path on Operator's Stack table |
> | 2 | [Trust-Layer Epic](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md) | Goals + Done When + Scale and Model + Candidate Module Breakdown |
> | 3 | [Caveman Synthesis](../../sources/tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md) | Mission Alignment section + Operator's adoption checklist |
> | 4 | [AI Decision Matrix 2026](../references/ai-model-provider-harness-decision-matrix-2026.md) § Trust / Confidential-Compute Layer | 4-axis matrix + Trust selection table |
> | 5 | [2026 Consumer Hardware AI Stack](../references/2026-consumer-hardware-ai-stack.md) § 2026-04-30 Addendum | Hardware tier mapping (RTX 3090 = L2 default, H100/H200 = L3 additive) |
>
> **Outcome**: you can answer for your own stack: should I adopt L2 default on existing GPU? Does L3 additive make sense for any specific workload? Which auth surface (key file / passphrase / cert / HSM)? With what migration cost if reversed?

### Goal C — Design the M001 Reference Pipeline (1.5 hours, hands-on)

For an operator preparing to author M001 (the L2 reference pipeline) when RTX 3090 lands mid-May 2026.

> [!abstract] Path C — Implementation Prep
>
> | # | Read | Focus on |
> |---|---|---|
> | 1 | [Trust-Layer Epic](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md) — M001 row + Goals + Open Questions | Define M001's empirical targets concretely |
> | 2 | [Concept page](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) — Key Insights composition math + How to Apply | Composition math reproducible · L2 default's 5 concrete next moves |
> | 3 | [Caveman Synthesis](../../sources/tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md) — full | Caveman as the prompt-layer substrate; install paths; eval harness; sub-skills (caveman-compress for memory-file slice) |
> | 4 | [RLM Synthesis](../../sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md) — REPL + LocalREPL primitives | RLM substrate integration for compressed-encrypted context as REPL variable (M003 territory) |
> | 5 | [Unsloth Synthesis](../../sources/tools-integration/src-unsloth-fast-lora-consumer-hardware.md) | UD-IQ2 / Q2_K weight quantization (the weights-layer slice of the 80–90% envelope) |
> | 6 | [2026 Consumer Hardware AI Stack](../references/2026-consumer-hardware-ai-stack.md) § Hardware-tier reframing | RTX 3090 capabilities post-delivery |
>
> **Outcome**: you have the full toolchain mapped — Caveman + Q2_K + KV-cache + AES-256-GCM + Triton + RLM — and can author M001 with concrete dependencies, target metrics, and validation gates.

### Goal D — Audit the 4-Layer Mission Claim (45 minutes)

For an evaluator auditing whether the wiki's 4-layer claim is empirically defensible.

> [!abstract] Path D — Mission Audit Sequence
>
> | # | Read | Focus on |
> |---|---|---|
> | 1 | [Anti-Vendor-Lock-In Lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) — Evidence 1–11 in order | The full 4-layer empirical claim; each layer with its substitution axes |
> | 2 | [Concept page](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) — Mission Alignment section | The 4th layer's structural framing |
> | 3 | [Caveman Synthesis](../../sources/tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md) — Mission Alignment + Compression-Substrate slot | The compression-substrate paper evidence |
> | 4 | [AI Infrastructure Decision Framework 2026](../references/ai-infrastructure-decision-framework-2026.md) § Resilience Playbook | 4-layer substitution map operationalized |
>
> **Outcome**: you can independently verify the 4-layer empirical claim, identify each layer's substitutes, and stress-test the substitution axes against any specific vendor disruption scenario.

### Goal E — Behavioral Lessons from the Arc (30 minutes)

For a future agent or operator picking up the methodology lesson from this arc.

> [!abstract] Path E — Behavioral Lessons
>
> | # | Read | Why |
> |---|---|---|
> | 1 | [Session Log 2026-04-30](../../log/2026-04-30-session-log-trust-layer-arc-tamper-proof-inference-cypher-decypher-compression.md) — Verbatim Directives + Operator Correction + Closing Reflection | The arc's behavioral pattern (do-not-undermine + recognize milestone scope + scaffold without overstepping) |
> | 2 | [`feedback_do_not_undermine_operator_design_assertions.md`](file:///home/jfortin/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_do_not_undermine_operator_design_assertions.md) | The feedback memory captured this session — when operator names operational properties, ground them with research; don't impose research-found ceilings |
> | 3 | [Saturation Lesson](../../lessons/01_drafts/saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work.md) | The third verification cycle of Hard Rule #11; this arc's existence is forward work refuting any premature saturation claim about the 3-layer stack being "complete" |
>
> **Outcome**: you understand the behavioral discipline that made this arc productive — verbatim quoting + operator-as-master + scaffold work-tracking without pre-committing modules.

## Artifact Inventory (13 artifacts navigable from this path)

### Authored fresh in this arc (4 substantive forward artifacts)

1. [Concept — Secure Tamper-Proof Model on Shared GPU](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) — design ground truth
2. [Trust-Layer Epic — Cypher + Decypher + Compression](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md) — milestone-class assembly with 6 candidate modules
3. [Synthesis — Caveman](../../sources/tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md) — operator-confirmed compression substrate
4. [Session Log 2026-04-30](../../log/2026-04-30-session-log-trust-layer-arc-tamper-proof-inference-cypher-decypher-compression.md) — continuity capture

### Augmented in this arc (6 existing-page edits)

5. [Anti-Vendor-Lock-In Lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) — Evidence 11 added
6. [Post-Anthropic 3-Layer Stack Epic](../../backlog/epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md) — EXTENDED-2026-04-30 cross-reference
7. [Post-Anthropic Self-Autonomous Stack Milestone](../../backlog/milestones/post-anthropic-self-autonomous-stack.md) — trust-layer epic added; 2 new acceptance criteria
8. [AI Decision Matrix 2026](../references/ai-model-provider-harness-decision-matrix-2026.md) — 4-axis Trust × Orchestrator × Harness × Provider section
9. [2026 Consumer Hardware AI Stack](../references/2026-consumer-hardware-ai-stack.md) — 2026-04-30 Addendum
10. [AI Infrastructure Decision Framework 2026](../references/ai-infrastructure-decision-framework-2026.md) — 4-layer Resilience Playbook reframe

### Memory + raw provenance

11. [`feedback_do_not_undermine_operator_design_assertions.md`](file:///home/jfortin/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_do_not_undermine_operator_design_assertions.md) — behavioral correction
12. `raw/notes/2026-04-30-secure-tamper-proof-model-on-shared-gpu-cypher-decypher-rlm-script.md` — verbatim directive log
13. `raw/articles/juliusbrusseecaveman.md` — Caveman repo ingestion (1,713 lines)

### Adjacent paths

- [Post-Anthropic 3-Layer Stack Learning Path (2026-04-28)](post-anthropic-3-layer-stack-2026-04-28.md) — the prior arc this path extends
- [Methodology Fundamentals Learning Path](methodology-fundamentals.md) — for readers needing the wiki's methodology background

## Outcomes

After completing the full path:

- **You can articulate the 4-layer mission claim**: trust × orchestrator × harness × provider, each independently substitutable with paper evidence.
- **You can reproduce the 80–90% composition math**: Caveman Wenyan-Full ~80–90% prompt × UD-IQ2/Q2_K ~87.5% weights × KV-cache compression × cypher overlay.
- **You can identify the L0 → L4 opt-ins** and pick the appropriate stance per workload.
- **You can author M001** with the full toolchain mapped (Caveman + Q2_K + KV-cache + AES-256-GCM + Triton + RLM substrate).
- **You can audit the trust layer's substitution axes**: hardware vendor / TEE provider / key management / compression substrate / decypher kernels / inference substrate.
- **You internalize the do-not-undermine behavioral lesson** and the recognize-milestone-scope discipline.

## Relationships

- BUILDS ON: [[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]]
- BUILDS ON: [[secure-tamper-proof-model-on-shared-gpu-research-synthesis|Concept — Secure Tamper-Proof Model on Shared GPU]]
- BUILDS ON: [[src-caveman-prompt-output-compressor-julius-brussee|Caveman Synthesis]]
- BUILDS ON: [[2026-04-30-session-log-trust-layer-arc-tamper-proof-inference-cypher-decypher-compression|2026-04-30 Session Log]]
- BUILDS ON: [[post-anthropic-3-layer-stack-2026-04-28|Post-Anthropic 3-Layer Stack Learning Path]] — adjacent path; 4th layer extends 3-layer
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — Evidence 11
- DEMONSTRATES: [[saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work|Saturation Lesson]] — third verification cycle
- FEEDS INTO: [[post-anthropic-self-autonomous-stack|Milestone — Post-Anthropic Self-Autonomous Stack]]

## Backlinks

[[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]]
[[Concept — Secure Tamper-Proof Model on Shared GPU]]
[[src-caveman-prompt-output-compressor-julius-brussee|Caveman Synthesis]]
[[2026-04-30 Session Log]]
[[Post-Anthropic 3-Layer Stack Learning Path]]
[[Anti-Vendor-Lock-In Lesson]]
[[Saturation Lesson]]
[[Milestone — Post-Anthropic Self-Autonomous Stack]]

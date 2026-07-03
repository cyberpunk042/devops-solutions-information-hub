---
title: "Learning Path — Custom-Tailored Senior-Engineer-Tier Model Group + Recreated Intelligence Layer (Mission Arc 2026-05-04)"
aliases:
  - "Custom-Tailored Model Group Learning Path"
  - "Senior-Engineer-Tier Model Mission Learning Path"
  - "Custom-Model + Intelligence Layer Reading Order"
type: learning-path
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-05-04
updated: 2026-05-04
last_reviewed: 2026-05-04
sources:
  - id: concept-synthesis
    type: wiki
    file: wiki/domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md
    description: "Goal A entry — design ground truth"
  - id: epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-2026-05.md
    description: "Goal B entry — work scope and 6 candidate modules"
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Goal C entry — mission claim and Evidence 12 (5th layer candidate)"
  - id: e012-tactical-predecessor
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E012-custom-model-library-unsloth-loras.md
    description: "Goal D entry — tactical predecessor that the new strategic-tier epic nests"
  - id: second-brain-custom-model-strategy
    type: wiki
    file: wiki/spine/references/second-brain-custom-model-strategy.md
    description: "Goal D supporting — 5-candidate matrix + 2026-05-04 addendum"
  - id: trust-layer-concept
    type: wiki
    file: wiki/domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md
    description: "Goal E entry — composition with trust layer (operator: 'with and without cypher / decypher with or without I/O Compression')"
  - id: spec-driven-convergence-lesson
    type: wiki
    file: wiki/lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md
    description: "Goal F entry — methodology applied to model-creation workflow ('like we teach')"
  - id: session-log
    type: wiki
    file: wiki/log/2026-05-04-session-log-custom-tailored-model-mission-and-root-ghostproxy-pain-point.md
    description: "Goal G entry — pain-point root-cause analysis + arc continuity"
  - id: raw-directive
    type: file
    file: raw/notes/2026-05-04-custom-tailored-model-group-moe-intelligence-layer-and-root-ghostproxy-pain-point.md
    description: "Verbatim operator directive log"
tags: [learning-path, custom-model, senior-engineer-tier, moe-group, intelligence-layer, behavioral-alignment, navigation, mission-2026-05-04, post-anthropic, fifth-layer-candidate]
---

# Learning Path — Custom-Tailored Senior-Engineer-Tier Model Group + Recreated Intelligence Layer

## Summary

This learning path navigates the operator-authored 2026-05-04 mission arc: **a custom-tailored senior-engineer-tier model group + recreated intelligence layer at I/O boundaries** that carries operator's behavioral core in the weights, supports multi-version release discipline, propagates as positive *information virus* across sister projects, and composes operator-toggle-able with the trust + compression + orchestrator + harness + provider layers. The arc was triggered by operator's experience setting up `root-ghostproxy` on a fresh non-GUI Debian 13 host, identifying the root cause of repeated AI-alignment overhead: *alignment substrate external to the model = repeated per-session cost*. Seven goals cover the arc end-to-end — from concept ground truth through epic scope, mission-claim positioning, predecessor nesting, trust-layer composition, methodology application ("like we teach"), and continuity context. **Total reading time: ~90 minutes** for full arc internalization; ~25 minutes for Goal A (concept only) for orientation.

## Prerequisites

Before starting this path, you should have read OR be prepared to read in parallel:
- [CLAUDE.md](../../CLAUDE.md) — project's operational program (always loaded in Claude Code sessions)
- [AGENTS.md](../../AGENTS.md) — universal cross-tool context
- [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — at least Evidence 1, 8, 11 (mission claim baseline)
- [Trust-Layer Concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) — composes with this arc

If pre-4090 (which is the operator's stack as of 2026-05-04, 4090 ETA mid-May 2026): treat this learning path as **future-state architecture** — Phase 0 toolchain bootstrap is hardware-blocked.

## Sequence

The arc is navigable in 7 goals (A–G), totaling ~90 minutes for full internalization or ~30 minutes for Goal A alone (orientation only).

### Goal A — Internalize the design (concept synthesis) — **30 min**

> [!info] Outcome: understand the operator-authored architecture (model group + intelligence layer + composition); pain-point root-cause and 80-90% composition math; 8 open design questions.

**Read in this order:**

1. **[Concept — Custom-Tailored Senior-Engineer-Tier Model Group + Recreated Intelligence Layer](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md)** — Summary + Verbatim Operator Directive + Operational Properties Registered + Pain-Point Anchor.
2. The **7 Key Insights** in the same page (senior-engineer-tier specialization · behavioral-alignment via DPO/IPO preference fine-tune · MoE-group via Mixture-of-LoRAs · recreated intelligence layer at I/O boundaries · Python-as-programming hyperstructure · multi-version + information-virus framing · trust+compression composition orthogonality).
3. The **Architecture Sketch + 7-Phase Realistic Phase Sketch** sections (one ASCII diagram + one 7-row table).
4. The **8 Open Questions** (operator design calls).

**Self-check after Goal A:** can you answer the *"why operator-authored model and not vendor-supplied + better prompting?"* question in your own words? If not, re-read the Pain-Point Anchor section.

### Goal B — Internalize the work scope (epic) — **20 min**

> [!info] Outcome: understand the strategic-tier epic, 6 candidate modules M001–M006, dependencies, mission-claim Option A vs B framing.

**Read in this order:**

1. **[Custom-Tailored Senior-Engineer-Tier Model Group Epic](../../backlog/epics/pre-milestone/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-2026-05.md)** — Summary + Operator Directive + Pain-Point Anchor.
2. The **Goals + Done When** sections (operator-confirmable success criteria).
3. The **Scale and Model + Candidate Module Breakdown** (6 modules: M001 Toolchain+Data+Constitution v0.1 · M002 First Specialist LoRA + Group Expansion · M003 Recreated Intelligence Layer · M004 Behavioral Preference Fine-Tune · M005 Trust+Compression Composition · M006 Multi-Version + Ecosystem + Mission Update).
4. The **Mission Framing — Option A vs B** + the **9 Open Questions** (operator design calls).

**Self-check after Goal B:** which module(s) deliver the *"naturally WANT to do things right"* property? (Answer: M004 — behavioral preference fine-tune via DPO/IPO over hack-vs-right preference pairs.)

### Goal C — Position in the mission claim (5th layer candidate) — **15 min**

> [!info] Outcome: understand how the custom-model layer extends the 4-layer empirical mission (orchestrator × harness × provider + trust) to a candidate 5-layer empirical claim.

**Read in this order:**

1. **[[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]]** § Summary + Evidence 1 + Evidence 8 + Evidence 10 + Evidence 11 (the 4-layer empirical baseline before this arc).
2. **Evidence 12 (the new candidate)** — the 8 substitution axes within the custom-model layer (open-weight base · fine-tune method · training framework · preference-data source · behavioral-constitution authoring · composition mechanism · evaluation gate · distribution channel).
3. The **Option A vs Option B** layer-count framing — operator-decision in M006 of the epic.

**Self-check after Goal C:** what would change about the lesson's structure if operator picks Option A vs Option B? (Answer: Option A keeps the lesson at 4 layers with a `vendor-supplied vs operator-authored` axis WITHIN provider; Option B explicitly adds a 5th layer with operator-controlled training-data + alignment-data + constitution as the structural distinguisher.)

### Goal D — Understand the predecessor and the nesting (E012 + strategy) — **15 min**

> [!info] Outcome: understand how the new strategic-tier epic NESTS the existing tactical [E012 Custom Model Library](../../backlog/epics/pre-milestone/E012-custom-model-library-unsloth-loras.md) without replacing it. Wiki-Router (E012 D) becomes input-boundary intelligence-layer router; Wiki-Assistant (E012 A) becomes a small-LoRA specialist in the model group.

**Read in this order:**

1. **[E012 Custom Model Library Epic](../../backlog/epics/pre-milestone/E012-custom-model-library-unsloth-loras.md)** — the tactical P2 epic (Wiki-Assistant + Wiki-Router + Multi-LoRA on small bases for AICP routing efficiency).
2. **[Second-Brain Custom Model Strategy](../../spine/references/second-brain-custom-model-strategy.md)** § Candidate Matrix — the 5 candidates (A Wiki-Assistant · B Wiki-Reasoner · C Wiki-Opus-Distilled · D Wiki-Router · E Multi-LoRA).
3. **[Second-Brain Custom Model Strategy § 2026-05-04 Addendum](../../spine/references/second-brain-custom-model-strategy.md)** — the 6-dimension extension table (senior-engineer-tier core · behavioral-alignment via preference data · MoE-style group · recreated intelligence layer · multi-version+virus · trust/compression composition).

**Self-check after Goal D:** does authoring this new strategic-tier epic deprecate E012? (Answer: no — E012 stays P2 tactical; Wiki-Router becomes a component of the new epic's M003 input-boundary intelligence layer; Wiki-Assistant nests as a methodology-fluency specialist LoRA in the model group. Compose, don't replace.)

### Goal E — Understand the composition with trust + compression (operator-toggle-able opt-ins) — **10 min**

> [!info] Outcome: understand operator's *"with and without cypher / decypher with or without I/O Compression"* — the custom-model layer composes orthogonally with the trust + compression layers, operator-toggle-able per workload.

**Read in this order:**

1. **[Trust-Layer Concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md)** § L0–L4 Integration Levers (the trust opt-ins).
2. **[Custom-Tailored Model Group Concept § Composition with Trust + Compression](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md)** — the orthogonality claim and default L2 stance on RTX 4090.
3. **[AI Model/Provider/Harness Decision Matrix 2026 § Custom-Model Layer](../../spine/references/ai-model-provider-harness-decision-matrix-2026.md)** — the C0–C5 opt-ins matrix and the 5-axis composability stack diagram.

**Self-check after Goal E:** can the same custom model run at L0 (no encryption) for development and L3 (NVIDIA CC mode) for production-grade workloads? (Answer: yes — opt-ins compose forward; operator picks per workload.)

### Goal F — Understand the methodology application ("like we teach") — **5 min**

> [!info] Outcome: understand operator's *"like we teach"* — apply the wiki's spec-driven methodology to the model-creation workflow itself; the workflow becomes the 9th instance of the convergent pattern.

**Read in this order:**

1. **[[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Agentic Build Convergence Lesson]]** § Summary + the 8 evidence instances + the wiki self-application open question.
2. **[Custom-Tailored Model Group Concept § Connection to Spec-Driven Convergence](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md)** — the table mapping spec-driven elements to model-creation instantiations (preference data + instruction data + constitution as version-controlled specs; verification checklist per LoRA; closed-loop sync rule applied to deviations).

**Self-check after Goal F:** what's the closed-loop sync rule applied to model creation? (Answer: when the model deviates from operator standards, *fix the preference data first, re-train, then update downstream*. The preference data is the spec; the weights are the code.)

### Goal G — Continuity context (session log + pain-point root-cause) — **5 min**

> [!info] Outcome: understand the session arc, the pain-point root-cause analysis through the layered configuration stack, and the carry-forward open questions.

**Read in this order:**

1. **[2026-05-04 Session Log — Custom-Tailored Model Mission + Root-Ghostproxy Pain Point Arc](../../log/2026-05-04-session-log-custom-tailored-model-mission-and-root-ghostproxy-pain-point.md)** § Summary + Pain-Point Root-Cause Analysis (the 5-layer config stack analysis: system → project → harness → ecosystem → model weights → root cause at the model-weights layer).
2. **[Verbatim Operator Directive Log](../../../raw/notes/2026-05-04-custom-tailored-model-group-moe-intelligence-layer-and-root-ghostproxy-pain-point.md)** — full operator words including the root-ghostproxy context (a separate new IaC + IPS + system-AI-safety-setup project the operator is bootstrapping; not yet registered in `sister-projects.yaml`; operator-decision).

**Self-check after Goal G:** the pain root cause is operator-named through the configuration stack. What is it? (Answer: alignment substrate external to the model means alignment cost paid per session, not per training. Baking standards into the weights is the *solution at the right place*.)

## Decision Matrix — Where do you land first?

> [!tip] Pick by your immediate need:
>
> | Your situation | Read first |
> |---|---|
> | **Quick orientation** (~30 min) | Goal A only — concept synthesis |
> | **Operator picking module ordering or making M006 layer-count decision** | Goal A → Goal B → Goal C |
> | **Reviewing E012 nesting / wondering if existing custom-model work is deprecated** | Goal D → Goal A → Goal B |
> | **Composing with trust layer or operator-toggle workload-stance design** | Goal E → Goal A |
> | **Sister-project consumer wanting to integrate** | Goal A → Goal F → Goal G |
> | **Full arc internalization** | All 7 goals in order, ~90 min |

## Outcomes

After completing the 7 goals in sequence, the reader will:

- **Understand the operator-authored design** — model group + recreated intelligence layer + composition orthogonality with trust + compression layers; the 80-90% composition math (Caveman ~75–90% prompt × UD-IQ2/Q2_K ~87.5% weights × KV-cache 50–87% × cypher overlay +0%); the 7-phase realistic rollout
- **Recognize the strategic-tier scope** — milestone-class epic with 6 candidate modules M001–M006, $0 cash budget for the L2 path on RTX 4090, 4 weeks critical-path target post-4090-delivery for `v0.1-seed`
- **Position the work in the mission claim** — candidate 5-layer empirical (custom-model × trust × orchestrator × harness × provider); Option A (provider axis) vs Option B (5th layer) operator-decision pending in M006
- **Know how the new epic nests E012** — Wiki-Router becomes input-boundary intelligence-layer router; Wiki-Assistant becomes a small-LoRA specialist; E012 stays P2 tactical alongside the new P0 strategic-tier epic
- **Apply the spec-driven methodology to the model-creation workflow** — preference data + instruction data + constitution as version-controlled specs; verification checklist per LoRA; closed-loop sync rule (fix preference data first, then re-train)
- **Trace the pain-point root cause** through the layered configuration stack (system → project → harness → ecosystem → model weights) and understand why baking standards into the weights is the *solution at the right place*
- **Be ready to confirm operator-decision items** in M006 (layer count, module ordering, base choice, propagation channel, constitution authoring, behavior-test thresholds, pain-point reduction metric, root-ghostproxy registration)

## Implementation Sequence (post-RTX 4090 delivery)

> [!info] When operator commits to Phase 0 (RTX 4090 in hand, ~mid-May 2026 ETA)
>
> 1. **Wire toolchain** — Unsloth + prime-rl + Triton on RTX 4090 (M001 Phase 0)
> 2. **Author preference data v0.1** — operator-curated hack-vs-right pairs from the wiki's existing lessons + raw/notes operator-corrections corpus (M001 Phase 1)
> 3. **Author constitution v0.1** — operator's standards as alignment-by-constitution document (M001 Phase 1)
> 4. **First specialist LoRA train** — pick base, DPO/IPO loss, rank 32–64 (M002 Phase 2 → `v0.1-seed`)
> 5. **Held-out behavior evaluation** — operator-graded; iterate before promotion (M004)
> 6. **AICP integration** — register as routing tier; Wiki-Router (E012 D) routes appropriate workloads to custom tier
> 7. **Trust + compression composition** — wire L2 default (M005)
> 8. **Group expansion** — Mixture-of-LoRAs across senior-engineer task surfaces (M002/M003 Phase 3)
> 9. **Recreated intelligence layer** — Python hyperstructure for I/O-boundary intelligence (M003 Phase 4)
> 10. **Multi-version manifest + ecosystem propagation** — `v0.1-seed` → `v0.5-growing` → `v1.0-validated`; sister-project consumer integration (M006 Phase 7)

## Connection to Prior Mission Arcs

This arc compounds with the prior 2026-04-30 trust-layer arc and the 2026-04-28 post-Anthropic 3-layer stack arc:

| Mission arc | Arc date | Layer added | Cumulative claim |
|---|---|---|---|
| Post-Anthropic 3-Layer Stack | 2026-04-28 | Orchestrator (Multica) + Harness (Claude Code/OpenCode) + Provider (AICP routing) | 3-layer empirical |
| Trust-Layer | 2026-04-30 | Trust / confidential-compute (cypher + decypher + compression for 80-90% space saved) | 4-layer empirical |
| **Custom-Tailored Model Group (THIS ARC)** | **2026-05-04** | **Custom-model / operator-authored tier (candidate 5th layer)** | **5-layer candidate (operator-decision M006)** |

Each arc is independently substantive AND composes orthogonally with the others. The mission claim's empirical traceability extends layer-by-layer.

## Open Questions Carried Forward

> [!question] Operator-decision items pending (carry-forward to next session)
>
> 1. Mission-claim layer count — Option A (substitutable axis WITHIN provider) vs Option B (5th layer); default proposal Option B
> 2. Single bundled epic vs split into 2–3 sub-epics by phase
> 3. First specialist LoRA base choice for `v0.1-seed`
> 4. MoE-as-architecture vs Mixture-of-LoRAs (or both)
> 5. Information-virus propagation channel (bundled with sister-project setup vs Multica-deployable vs HuggingFace publish vs operator-internal only)
> 6. Behavioral-constitution authoring (single document vs per-domain split)
> 7. Behavior-test pass-rate thresholds for `v0.5-growing` and `v1.0-validated`
> 8. Pain-point reduction metric definition
> 9. root-ghostproxy registration in `sister-projects.yaml` and use as first non-wiki integration consumer

## Relationships

- BUILDS ON: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]] — Goal A entry
- BUILDS ON: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-2026-05|Custom-Tailored Model Group Epic]] — Goal B entry
- BUILDS ON: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — Goal C entry
- BUILDS ON: [[[[E012-custom-model-library-unsloth-loras|E012 — Custom Model Library (Unsloth LoRAs)]] — Goal D entry (predecessor)]]
- BUILDS ON: [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]] — Goal D supporting
- BUILDS ON: [[secure-tamper-proof-model-on-shared-gpu-research-synthesis|Trust-Layer Concept]] — Goal E entry
- BUILDS ON: [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Convergence Lesson]] — Goal F entry
- BUILDS ON: [[2026-05-04-session-log-custom-tailored-model-mission-and-root-ghostproxy-pain-point|2026-05-04 Session Log]] — Goal G entry
- PARALLELS: [[trust-layer-tamper-proof-inference-2026-04-30|Trust-Layer Learning Path]] — sibling arc learning path
- PARALLELS: [[post-anthropic-3-layer-stack-2026-04-28|Post-Anthropic 3-Layer Stack Learning Path]] — predecessor arc learning path
- FEEDS INTO: [[post-anthropic-self-autonomous-stack|Milestone — Post-Anthropic Self-Autonomous Stack]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]] — via Goal F
- DEMONSTRATES: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] — wiki methodology applied to model-creation workflow

## Backlinks

[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]]
[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-2026-05|Custom-Tailored Model Group Epic]]
[[Anti-Vendor-Lock-In Lesson]]
[[E012 — Custom Model Library (Unsloth LoRAs)]]
[[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]
[[Trust-Layer Concept]]
[[Spec-Driven Convergence Lesson]]
[[2026-05-04 Session Log]]
[[trust-layer-tamper-proof-inference-2026-04-30|Trust-Layer Learning Path]]
[[Post-Anthropic 3-Layer Stack Learning Path]]
[[Milestone — Post-Anthropic Self-Autonomous Stack]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]

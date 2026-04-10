---
title: "Rework Prevention"
type: concept
layer: 2
maturity: growing
domain: ai-agents
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-harness-engineering-article
    type: article
    url: "https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0"
    title: "Building Claude Code with Harness Engineering"
    ingested: 2026-04-08
  - id: src-openfleet-local
    type: documentation
    file: ../openfleet/CLAUDE.md
    title: "OpenFleet — Local Project Documentation"
    ingested: 2026-04-08
tags: [rework-prevention, planning, quality-gates, spec-compliance, agent-behavior, harness-engineering, openfleet, test-driven, context-management, cost-of-rework]
---

# Rework Prevention

## Summary

Rework prevention is the practice of designing AI agent workflows so that work requiring repetition — due to misaligned scope, incorrect assumptions, failed quality gates, or context drift — is caught and corrected before it propagates into irreversible state. The cost of rework is not linear: it compounds as revert + re-plan + re-execute + re-verify, and each cycle degrades the agent's remaining context budget while consuming wall-clock time. Prevention operates through four layers: planning quality (surface assumptions early), execution guardrails (detect drift during work), review gates (prevent unreviewed output from advancing), and context management (prevent regression from forgotten decisions). The break-even math is stark: prevention is net-positive if it reduces rework probability by more than 12%.

> [!info] Prevention Economics Reference Card
>
> | Metric | Value | Source |
> |--------|-------|--------|
> | Single rework cycle cost | 2.5T–3.5T (T = correct-first-time cost) | Harness Engineering |
> | Prevention investment | 0.2T–0.4T per task | Planner+Critic data |
> | Break-even rework reduction | >12% | Calculated (0.3T / 2.5T) |
> | Typical rework rate without gates | 20–40% on complex tasks | Engineering experience |
> | Breezing mode planning overhead | 5.5x planning tokens | Harness Engineering |
> | Cascade multiplier (fleet) | Up to N× for N dependent tasks | OpenFleet design |

## Key Insights

### Why Rework Is Worse Than It Looks

> [!warning] Rework compounds — it does not add
> A single rework cycle on a 3-hour coding task costs more than 3 hours: the revert must be clean (often non-trivial for multi-file changes), the cause must be diagnosed, the plan must be revised, execution must restart, and the review gate must be re-cleared. In a multi-agent context, one task's rework cascades: downstream tasks built on incorrect state must also be reverted. In a fleet with 5 dependent tasks, one root-cause failure can trigger 5 downstream reworks.

> [!abstract] Different phases produce different rework signatures
>
> | Skipped Phase | Rework Signature | How It Appears |
> |---------------|-----------------|----------------|
> | Planning | Scope creep | Correct-looking partial work that misses critical requirements |
> | Review | Silent accumulation | Errors compound across cycles before becoming visible |
> | Context management | Regression | Early decisions forgotten, re-made incorrectly, conflicting with later work |

### Prevention Principles

**Prevention is orders of magnitude cheaper than correction.** The Breezing mode's Planner+Critic review costs ~5.5x planning tokens (vs ~4x without pre-review). This sounds like overhead — until the pre-review catches a scoping error that would require reworking 2 hours of coding. Any rework consuming more than 5.5 planning cycles' worth of effort was cheaper to prevent.

> [!tip] Hard gates vs soft gates
> Soft quality gates ("should review before committing") are routinely skipped under time pressure or when the agent has high local confidence. Hard quality gates (the harness TypeScript rule blocks the commit operation if the review verb was not executed) cannot be skipped without deliberate circumvention. Hard gates prevent the single most common rework trigger: "I thought it was fine but it wasn't."

**Spec compliance is distinct from functional review.** Functional review asks "does this work?" Spec compliance review asks "does this match what was asked for?" An agent implementing a caching layer that works perfectly but uses the wrong eviction policy has passed functional review and failed spec compliance review. The distinction matters because most review processes only check function, not intent.

**TDD shifts rework cost forward.** Writing tests before implementation forces explicit acceptance criteria before code is written. When implementation is complete, the tests ARE the spec compliance gate — deviations are caught automatically. TDD automates spec compliance review at the unit level.

## Deep Analysis

### The Compound Cost Model

> [!warning] The math of rework
>
> Let T = time to complete the task once correctly.
>
> **Without prevention (one rework cycle):**
> `T (first attempt) + R (revert) + D (diagnosis) + P (re-plan) + T (re-execute) + V (re-verify) ≈ 2.5T–3.5T`
>
> **With cascade (fleet context):**
> `2.5T (root task) + Σ(downstream rework) → potentially N × 2.5T`
>
> **Prevention investment:**
> `0.2T–0.4T per task (spec review + Planner+Critic + pre-checks)`
>
> **Break-even:** Prevention is net-positive at >12% rework reduction (0.3T / 2.5T). Typical rework rates without gates: 20–40%. Prevention ROI is strongly positive in nearly all realistic scenarios.

This is why OpenFleet's orchestrator invests heavily in upstream quality (security scan, doctor run, readiness gating) before dispatch — a single task dispatched in bad state can corrupt the entire sprint.

### The Four Prevention Layers

> [!info] Prevention Strategy Reference Card
>
> | Layer | Goal | Key Mechanisms | Failure When Missing |
> |-------|------|---------------|---------------------|
> | **1. Planning Quality** | Prevent scope drift | Explicit spec/acceptance criteria, Planner+Critic review, scope confirmation, ambiguity resolution | Scope creep — partial work missing requirements |
> | **2. Execution Guardrails** | Prevent silent drift | Hooks detecting out-of-scope writes, bounded task scope (max N files), checkpoints at phase boundaries, running todo/plan | Unbounded drift — output diverges silently from plan |
> | **3. Review Gates** | Prevent unreviewed advancement | Hard gate before promotion, spec compliance vs functional review, integration tests, OpenFleet step 7 | Silent accumulation — errors compound before detection |
> | **4. Context Management** | Prevent regression | Externalize plans to files, reset context at phase boundaries, scoped sub-agents, periodic spec re-reads | Regression — early decisions forgotten, remade incorrectly |

### Rework Diagnostic Table

> [!abstract] Pattern → Root Cause → Prevention
>
> | Rework Pattern | Root Cause | Prevention |
> |---|---|---|
> | "It works but it's the wrong thing" | Missing spec compliance review | Write acceptance criteria; compare output against spec |
> | "It was fine then something broke it" | Context drift; forgotten decisions | Externalize decisions to files; re-read spec periodically |
> | "The scope kept growing" | No scope gate during execution | Guardrail rules flagging out-of-scope writes; bounded dispatch |
> | "It passed tests but failed in production" | Integration context not considered | Integration tests; spec includes deployment context |
> | "I had to redo it because requirements changed" | Premature execution | Guided/smart modes; confirm spec before work begins |
> | "Multiple agents produced conflicting output" | No canonical state between agents | Single source of truth; validate before making canonical |

### Connection to Planning

Rework prevention and planning are the same investment viewed from different angles. Planning before execution is rework prevention in the future tense — "if I plan now, I avoid reworking later." Rework prevention analysis is planning in the past tense — "if I had planned better, I would not be here now."

The Harness Engineering insight quantifies this: 5.5x planning overhead at the start vs. 2.5x rework cost later. Planning-as-prevention breaks even at a rework probability of 5.5/2.5 = 22%. For LLM agents on complex tasks, rework probability without explicit planning is typically well above 22%.

### This Wiki as Practitioner Instance

> [!example]- Rework prevention in the wiki ingestion pipeline
>
> The three ingestion modes encode different prevention postures:
>
> | Mode | Prevention Posture | When Appropriate |
> |------|-------------------|-----------------|
> | **guided** | Maximum — shows extraction plan, waits for approval before writing | New domains, complex sources, high-stakes content |
> | **smart** (default) | Risk-calibrated — auto when confident, escalates on: new domain, contradictions, ambiguity, low-quality source | Most ingestion (default) |
> | **auto** | Minimal — post-chain validation is the only hard gate | High-confidence, low-complexity sources |
>
> The 6-step post-chain (`pipeline post`) is itself a rework prevention mechanism: validation, manifest, lint, and index checks run after every ingestion. If any step fails, ingestion is not complete. This is the equivalent of the harness's commit gate — work is not "done" until quality checks pass.

## Open Questions

> [!question] Can rework rate be measured per agent or per task type?
> Requires: per-agent rework tracking in OpenFleet's orchestrator. The existing audit ledger tracks task state transitions but does not currently classify which transitions represent rework cycles vs. normal flow. This would enable calibrated prevention investment — spending more on prevention for task types with historically high rework rates.

## Answered Open Questions

> [!example]- Should smart ingestion mode learn from past rework instances?
> Yes, and the mechanism already exists structurally. Smart mode's escalation heuristics are currently static (new domain, contradictions, ambiguity, low-quality source). The practical path for learning: the wiki's `## Open Questions` tagged with rework signals (contradictions, domain gaps, thin pages) are exactly the corpus for refining heuristics. `pipeline gaps` already surfaces thin pages and orphans — a `pipeline crossref` pass after every smart-mode ingestion would identify whether new pages integrated cleanly or created link gaps, serving as a proxy rework signal. Full heuristic learning requires logging which sources triggered manual corrections.

> [!example]- What is the rework cost model for an incorrect decision page?
> The cost follows the compound model with an additional amplification factor — decision pages are read by downstream pages via `DERIVED FROM` and `BUILDS ON` relationships. An incorrect decision linked by N downstream pages requires: (1) identifying all N pages via relationship traversal, (2) updating the decision page, (3) reviewing each downstream page for derived content. The cost amplification equals the number of `BUILDS ON` edges. Prevention: decisions at `status: verified` should require explicit confirmation before modification, forcing awareness of downstream impact.

> [!example]- Can spec compliance review be automated for wiki pages?
> Partial automation is feasible. The post-chain validates schema compliance (frontmatter) but not content compliance (does the page reflect the source?). Content-level compliance requires comparing generated `## Summary` and `## Key Insights` against the source in `raw/`. Extending the linter with a "summary faithfulness check" would automate this — but requires LLM inference at lint time. The wiki's guided mode implements manual spec compliance review; automation would use the same inputs (source text + generated page) with an LLM judge.

## Relationships

- ENABLED BY: [[Always Plan Before Executing]]
- BUILDS ON: [[Agent Orchestration Patterns]]
- RELATES TO: [[Harness Engineering]]
- RELATES TO: [[OpenFleet]]
- RELATES TO: [[Plan Execute Review Cycle]]
- RELATES TO: [[Claude Code Best Practices]]
- RELATES TO: [[Wiki Ingestion Pipeline]]
- FEEDS INTO: [[Research Pipeline Orchestration]]

## Backlinks

[[Always Plan Before Executing]]
[[Agent Orchestration Patterns]]
[[Harness Engineering]]
[[OpenFleet]]
[[Plan Execute Review Cycle]]
[[Claude Code Best Practices]]
[[Wiki Ingestion Pipeline]]
[[Research Pipeline Orchestration]]
[[Decision: Execution Mode Edge Cases]]
[[Immune System Rules]]
[[Model: Quality and Failure Prevention]]
[[Spec-Driven Development]]
[[Task Lifecycle Stage-Gating]]

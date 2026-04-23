---
title: "Context Depth Must Vary Per Task Type, Not Per Project — Tier Selection Extends Beyond Identity"
aliases:
  - "Context Depth Must Vary Per Task Type, Not Per Project"
  - "Tier Selection Is Per-Task, Not Per-Project"
type: lesson
domain: ai-agents
layer: 4
status: synthesized
confidence: medium
maturity: growing
derived_from:
  - "Model: Context Engineering"
  - "Right-Size the Methodology Model to the Actual Work"
  - "Tier-Based Context Depth — Trust Earned Through Approval Rates"
created: 2026-04-16
updated: 2026-04-22
sources:
  - id: openarms-integration-notes
    type: file
    project: openarms
    path: wiki/log/2026-04-16-second-brain-integration-notes.md
    description: "OpenArms Part 17 and Part 22 — identified that skill injection gives same context depth to every task regardless of complexity"
  - id: right-sizing-lesson
    type: wiki
    file: wiki/lessons/02_synthesized/contributed/right-size-the-methodology-model-to-the-actual-work-not-the.md
    description: "Right-size lesson: T116 $9.07 vs T117 $1.20, 86.8% reduction by using integration model for mechanical work"
  - id: tier-context-depth-pattern
    type: wiki
    file: wiki/patterns/03_validated/knowledge/tier-based-context-depth-trust-earned-through-approval-rates.md
    description: "The pattern this lesson extends — tier selection framed as trust-earned-per-task-type, not only per-agent"
contributed_by: "openarms-operator-claude"
contribution_source: "/home/jfortin/openarms/wiki/log/2026-04-16-second-brain-integration-notes.md (Parts 17, 22)"
contribution_date: 2026-04-16
contribution_status: pending-review
contribution_reason: "Context Engineering gap observed from the consumer side — tier selection is currently project-level but should be task-type-level for cost-quality routing"
tags: [lesson, context-engineering, tier-selection, right-sizing, context-depth, contributed, openarms]
---

# Context Depth Must Vary Per Task Type, Not Per Project

## Summary

Context engineering defines three tier budgets (Expert 5-10K / Capable 2-5K / Lightweight 500-1K tokens) with a 10× cost differential. The [[tier-based-context-depth-trust-earned-through-approval-rates|tier-based context depth pattern]] frames tier selection as earned through trust (approval rates per task type). But in practice, projects adopt a single tier for ALL tasks — context injection gives the same depth to simple and complex work. This wastes context on trivial tasks and starves complex tasks. The right-sizing lesson (T116 $9.07 vs T117 $1.20, 86.8% reduction) proved model selection is per-task; **context-depth selection must follow the same logic**. Tier selection should parameterize on `(agent_trust × task_complexity × task_novelty)`, not just `agent_trust`.

## Context

> [!warning] When does this lesson apply?
>
> - Your skill injection system gives the same context depth to every task
> - You observe that simple mechanical tasks carry the same context footprint as novel research tasks
> - You've adopted the right-sizing lesson for methodology models but not for context depth
> - You're writing a Context Engineering Standards document for your project
> - You're building or evolving a harness that injects skills/context into agent sessions

## Insight

> [!tip] The insight
>
> **Context depth is a ROUTING dimension, not a project-level default.** The same logic that drove right-sizing methodology models applies one level deeper: context that a feature-development task needs would be overkill for a mechanical integration task. The tier-based context depth pattern already defines the tiers (Expert/Capable/Lightweight) — the gap is that tier selection is framed around AGENT trust ("this agent has earned Expert tier") when it should also parameterize on TASK properties ("this task needs Expert context; that task needs Lightweight"). A capable agent on a trivial task should get Lightweight context. An expert agent on a novel task should get Expert context.

The mechanism:
- **Task novelty** (known solution vs requires discovery) predicts how much protocol context helps
- **Task complexity** (narrow mechanical vs broad architectural) predicts how much domain context helps
- **Task type** (integration vs feature-development vs research) is a rough proxy for both
- Right-sizing methodology model and right-sizing context tier are the SAME selection problem at two layers

## Evidence

**Evidence 1: OpenArms Part 17 observation (2026-04-16)**

After reading the Tier-Based Context Depth pattern, OpenArms noted:

> "Our skill injection gives the SAME context depth to every task regardless of complexity. [...] Gap: our skill injection gives the same context depth to every task regardless of complexity."

OpenArms runs 5 methodology skills that load the same context on every task invocation. T117 (integration model, mechanical 18-min task, $1.20) received the same skill depth as T116 (feature-development, novel 35-min task, $9.07). The cost savings came from model selection (5 stages → 3 stages), not from context depth adaptation. Further savings are available from context tier selection if the harness can detect task type and pick an appropriate tier at injection time.

**Evidence 2: Right-sizing lesson quantified 86.8% cost reduction at model layer**

The [[right-size-the-methodology-model-to-the-actual-work-not-the|right-size methodology model]] lesson (contributed by OpenArms, evolved to `02_synthesized`) proved that selecting `task_type: integration` over `task_type: task` (feature-development) for mechanical extensions saved 86.8% cost and 49% time on T117 vs T116. Model selection is a per-task routing dimension. Context depth is a parallel per-task routing dimension at a finer layer — same logic, same expected savings order-of-magnitude, different mechanism.

**Evidence 3: Tier budgets have 10× cost differential per message**

The [[model-context-engineering|Context Engineering model]] quantifies tier budgets: Expert 5-10K tokens, Capable 2-5K, Lightweight 500-1K. Every message in a session carries the injection cost. A 54-min multi-task run making ~150 tool calls at Expert tier (say 7K avg context) costs ~1.05M tokens in context alone — compare to Lightweight (say 750 avg) at 112K tokens. **10× differential per message compounds across 150+ tool calls.** This compounds in the same compounding way the Opus 4.7 tokenizer adds ×1.35 — the costs multiply, not add.

**Evidence 4: Cost Optimization Stack names right-sizing as layer 2**

The [[agent-execution-cost-optimization-stack|Cost Optimization Stack]] pattern lists 5 compounding layers. Layer 1 is methodology-model right-sizing (5-10× savings). Layer 2 is effort-level right-sizing (2-3×). Context-depth right-sizing should be a named layer: between model selection and effort, sitting at the skill-injection point. OpenArms's right-sizing implementation covered layer 1 but not the context layer.

## Applicability

| Context | Apply this lesson |
|---|---|
| **Solo agent, POC, L1** | Not needed. Single tier is fine at this scale. |
| **Solo agent, MVP+, L2** | Apply selectively. At minimum, detect `task_type` and vary skill injection depth: integration → Lightweight/Capable; feature-development → Capable/Expert; research → Expert. |
| **Harness, L2-L3** | Apply structurally. Harness prompt builder queries task's `task_type` + `novelty` and selects tier. Gateway query `--task <type>` should return recommended tier. |
| **Fleet, L3** | Apply mandatorily. MCP server context budget varies per agent × task type × novelty × phase. Compounds with tool-level blocking. |
| **Ingestion / creative work** | Start at Expert and narrow. Exploratory tasks need broad context; narrowing is premature. |

> [!warning] When NOT to apply this lesson
>
> - When you have <3 task types. Tier variation adds complexity; needs enough task types to justify.
> - When all tasks are genuinely novel (pure research). Everything is Expert; there's nothing to narrow.
> - When token cost is not a material constraint (rare — token cost compounds fast at fleet scale).
> - Premature optimization: if your methodology-model right-sizing isn't done yet, do that FIRST — it's the higher-leverage savings.

## Self-Check

> [!warning] Questions to confirm this lesson applies to your project
>
> 1. Does your skill injection give the same depth to all tasks?
> 2. Have you implemented methodology-model right-sizing (Layer 1 of the Cost Optimization Stack)?
> 3. Do you track context-injection token cost per tool call, per task type?
> 4. Can you point to a task type where Lightweight context would not degrade quality?
>
> If 1=yes, 2=yes, 3=no or yes, 4=yes: this lesson applies. Implement tier routing on task_type first, then add novelty + complexity dimensions as you measure.

## How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The pattern this extends** | [[tier-based-context-depth-trust-earned-through-approval-rates\|Tier-Based Context Depth]] — extends trust dimension with task-properties dimension |
> | **The sibling lesson at model layer** | [[right-size-the-methodology-model-to-the-actual-work-not-the\|Right-Size Methodology Model]] — same logic at higher layer |
> | **The governing model** | [[model-context-engineering\|Model — Context Engineering]] — defines the three-tier budget system |
> | **The compounding stack** | [[agent-execution-cost-optimization-stack\|Cost Optimization Stack]] — 5 layers; this is the tier-budget layer |
> | **The principle** | [[right-process-for-right-context-the-goldilocks-imperative\|Goldilocks]] — process adapts to context; so should context itself |

## Relationships

- DERIVED FROM: [[model-context-engineering|Model — Context Engineering]]
- DERIVED FROM: [[right-size-the-methodology-model-to-the-actual-work-not-the|Right-Size Methodology Model]]
- EXTENDS: [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
- RELATES TO: [[agent-execution-cost-optimization-stack|Agent Execution Cost Optimization Stack]]
- RELATES TO: [[right-process-for-right-context-the-goldilocks-imperative|Principle — Goldilocks]]
- FEEDS INTO: [[model-context-engineering-standards|Context Engineering Standards]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[model-context-engineering|Model — Context Engineering]]
[[Right-Size Methodology Model]]
[[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[agent-execution-cost-optimization-stack|Agent Execution Cost Optimization Stack]]
[[Principle — Goldilocks]]
[[Context Engineering Standards]]
[[methodology-adoption-guide|Methodology Adoption Guide]]

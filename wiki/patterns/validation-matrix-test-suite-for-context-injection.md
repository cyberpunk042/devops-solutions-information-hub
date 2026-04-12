---
title: "Validation Matrix — Test Suite for Context Injection"
type: pattern
domain: ai-agents
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Structured Context Is Proto-Programming for AI Agents"
  - "Three Lines of Defense — Immune System for Agent Quality"
instances:
  - page: "Structured Context Is Proto-Programming for AI Agents"
    context: "29 validation scenarios demonstrate the structural consistency principle — same skeleton across all injection types"
  - page: "Three Lines of Defense — Immune System for Agent Quality"
    context: "Validation matrix verifies that the immune system's context modifications produce correct structured output"
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: openfleet-matrix
    type: observation
    file: raw/articles/openfleet-validation-matrix-samples.md
    description: "OpenFleet validation-matrix/ — 29 scenario files (2,444 lines) defining expected context injection per condition"
tags: [validation-matrix, testing, context-injection, quality-assurance, structured-context, openfleet]
---

# Validation Matrix — Test Suite for Context Injection

## Summary

Context injection for AI agents is code — it programs behavior through structured markdown. Like all code, it needs tests. A validation matrix is a collection of scenario files, each defining: the CONDITION (what state the agent is in), the EXPECTED CONTEXT (exactly what the agent should receive), and the EXPECTED BEHAVIOR (what the agent should do next). This is unit testing for prompt engineering — verifiable, reproducible, regression-detectable.

> [!info] Pattern Reference Card
>
> | Component | Purpose | Example |
> |-----------|---------|---------|
> | **Scenario ID** | Unique identifier for the condition | TK-01, HB-02, FL-03 |
> | **Condition** | State that triggers this injection | "Work stage, full contributions received" |
> | **Expected context** | Exact markdown the agent receives | task-context.md + knowledge-context.md content |
> | **Expected behavior** | What the agent should do | "Follow plan, commit, complete. No fleet_read_context needed." |
> | **Category** | Scenario type | TK (task), HB (heartbeat), FL (fleet-level) |

## Pattern Description

> [!abstract] The Three Categories of Validation Scenarios
>
> | Category | Count | What It Tests |
> |----------|-------|---------------|
> | **TK (Task)** | 20 scenarios | Context injection during active task execution — work stage, reasoning, conversation, rework, contribution, blocking, spike, concern |
> | **HB (Heartbeat)** | 7 scenarios | Context injection during idle/monitoring — idle, has-work, has-messages, reviews, unassigned, urgent, lightweight |
> | **FL (Fleet)** | 2 scenarios | Context injection for fleet-level states — planning phase, crisis |

Each scenario file contains TWO sections that together form a test case:

**1. Expected context (the "input"):** The exact markdown that the context builder should produce. This includes the metadata line (`MODE: task | injection: full | model: feature-development`), role declaration, task data, stage protocol (MUST/MUST NOT), confirmed plan, contribution inputs, and action directive.

**2. Expected behavior (the "assertion"):** A one-line statement of what the agent should do when it receives this context. Example: "Engineer has everything. Follow plan, commit, complete. fleet_read_context NOT needed."

The structural consistency principle: every scenario follows the SAME skeleton. Headers are identical. Sections appear in the same order. The CONTENT varies (different task, different stage, different contributions) but the STRUCTURE is constant. This means:
- The context builder can be tested: does it produce output matching the scenario?
- Regressions are detectable: if a code change alters a scenario's output, the diff shows exactly what changed
- New scenarios compose from existing blocks: a new stage + existing task type = predictable new scenario

> [!warning] Without a Validation Matrix
>
> Context injection changes are invisible. Someone modifies the heartbeat template, it starts omitting the standing orders section, no test catches it. An agent that previously received full protocol now gets a shortened version. The behavioral change appears weeks later when an agent violates a rule that was quietly dropped from its context. Without the matrix, there's no way to know what the agent SHOULD be receiving, so there's no way to know what broke.

## Instances

> [!example]- OpenFleet: 29 Scenarios (2,444 lines, production)
>
> **Task scenarios (20):**
> - TK-01: Work stage, full contributions — engineer has architect design + QA tests embedded
> - TK-02: Work stage, no contributions — contributions not required for this task type
> - TK-03: Reasoning — collecting contributions, planning approach
> - TK-04: Conversation — PO interaction, clarifying requirements
> - TK-06: Rejection rework — task rejected, must fix root cause, labor_iteration ≥ 2
> - TK-07: Architect contribution — specialist producing design input for another agent
> - TK-11: Analysis — examining codebase, producing analysis document
> - TK-12: Investigation — root cause discovery, technical findings
> - TK-13: Blocked — agent cannot proceed, waiting for input
> - TK-27: Spike — research task, no work stage
> - TK-30: Capable tier — reduced context depth for trusted model
> - TK-31: Lightweight tier — minimal context for simple operations
> - TK-42: Concern — agent filing a quality/architecture concern
>
> **Heartbeat scenarios (7):**
> - HB-01: Idle, no tasks — agent waiting for dispatch
> - HB-02: Has work task — agent currently executing
> - HB-04: Fleet-ops reviews — review queue pending
> - HB-05: PM unassigned — tasks need triage
> - HB-06: Urgent directive — PO instruction takes priority
> - HB-20: Lightweight — minimal heartbeat for cost savings
>
> **Fleet scenarios (2):**
> - FL-01: Planning phase — fleet inactive, no dispatch
> - FL-03: Crisis — fleet-ops emergency protocol
>
> **What it revealed:** The 29 scenarios share ~5 structural templates. The same metadata line, the same MUST/MUST NOT format, the same contribution section structure. The content varies but the skeleton is constant — confirming the [[Structured Context Is Proto-Programming for AI Agents]] principle.

> [!example]- Research Wiki: Implicit Validation (no formal matrix)
>
> The research wiki's pipeline post chain acts as a partial validation matrix — it checks that pages have correct frontmatter, required sections, and valid relationships. But there's no validation of the CONTEXT that agents receive when working on the wiki. CLAUDE.md, skills, and MCP tool responses are untested injections.
>
> **Gap:** A validation matrix for the wiki would define: "when an agent runs `/continue`, it should receive: current page count, pending raw files, evolution candidates, gap analysis. Here is the expected format."

## When To Apply

> [!tip] Conditions for a Validation Matrix
>
> - **Multiple context injection points** — skills, heartbeats, task context, commands — each needs verification
> - **Context changes frequently** — features being added to the context builder
> - **Agent behavior regressions** — "it used to work" scenarios where a context change broke compliance
> - **Multiple tiers or modes** — different agents get different context; each combination needs a scenario
> - **Team maintaining the system** — the matrix serves as documentation of "what the agent should see"

## When Not To

> [!warning] When the Overhead Exceeds the Value
>
> - **Static CLAUDE.md only** — if context doesn't change dynamically, a matrix is unnecessary
> - **Solo agent, simple tasks** — one agent, one context template, visual inspection suffices
> - **No context builder code** — if context is hand-written, not generated, the matrix has nothing to test against
> - **Early exploration** — context is changing hourly. Freeze the design first, then validate.

## Relationships

- DERIVED FROM: [[Structured Context Is Proto-Programming for AI Agents]]
- DERIVED FROM: [[Three Lines of Defense — Immune System for Agent Quality]]
- RELATES TO: [[Tier-Based Context Depth — Trust Earned Through Approval Rates]]
- RELATES TO: [[Harness-Owned Loop — Deterministic Agent Execution]]
- RELATES TO: [[Enforcement Hook Patterns]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Structured Context Is Proto-Programming for AI Agents]]
[[Three Lines of Defense — Immune System for Agent Quality]]
[[Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[Harness-Owned Loop — Deterministic Agent Execution]]
[[Enforcement Hook Patterns]]
[[Methodology Standards — What Good Execution Looks Like]]

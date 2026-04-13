---
title: Contribution Gating — Cross-Agent Inputs Before Work
aliases:
  - "Contribution Gating — Cross-Agent Inputs Before Work"
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
  - {'page': 'Three Lines of Defense — Immune System for Agent Quality', 'context': "Contribution requirements are Line 1 (structural prevention) — agents can't skip to work without cross-agent review"}
  - {'page': 'Harness-Owned Loop — Deterministic Agent Execution', 'context': 'Orchestrator Step 2.5 checks contribution completeness before allowing dispatch to WORK stage'}
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: openfleet-contributions
    type: observation
    file: raw/articles/openfleet-methodology-scan.md
    description: OpenFleet contribution system — synergy-matrix.yaml defines cross-role requirements, contributions.py gates WORK stage
  - id: openfleet-synergy
    type: observation
    file: raw/articles/openfleet-methodology-scan.md
    description: "Synergy matrix: 115 lines YAML defining required/recommended/conditional contributions per role pair"
tags: [contribution-gating, cross-agent, multi-agent, synergy-matrix, quality, rework-prevention, openfleet]
---

# Contribution Gating — Cross-Agent Inputs Before Work

## Summary

In multi-agent systems, contributions from specialist roles (architect design, QA test definitions, security review) are collected BEFORE the implementing agent begins work — not after. A declarative synergy matrix defines which roles must contribute to which task types, at what priority (required/recommended/conditional). The orchestrator blocks dispatch to WORK stage until all required contributions are received. This prevents rework: the implementing agent works FROM designs, WITH predefined tests, FOLLOWING security requirements — instead of producing work that later fails review.

> [!info] Pattern Reference Card
>
> | Component | Purpose |
> |-----------|---------|
> | **Synergy matrix** | Declarative YAML defining which roles contribute to which roles, at what priority |
> | **Contribution subtasks** | Auto-created when task enters REASONING stage |
> | **Completeness gate** | Blocks dispatch to WORK until all required contributions received |
> | **fleet_contribute tool** | MCP tool for agents to post contributions to other agents' tasks |
> | **fleet_request_input tool** | MCP tool for agents to request missing contributions |

## Pattern Description

> [!abstract] Three Priority Levels
>
> | Priority | Behavior | Example |
> |----------|----------|---------|
> | **Required** | Always created. BLOCKS work stage until received. | Architect design_input for software-engineer |
> | **Recommended** | Created unless PO opts out. Does not block. | QA qa_test_definition for software-engineer |
> | **Conditional** | Created only when specific conditions met (auth, data, security-relevant). | DevSecOps security_review for auth-related tasks |

The mechanism:

1. Task enters REASONING stage → `detect_contribution_opportunities()` reads synergy matrix
2. For the target agent's role, all `required` and `recommended` specs spawn parallel contribution subtasks
3. Specialist agents (architect, QA, devsecops) produce their contributions independently
4. `check_contribution_completeness()` returns missing list + percentage
5. Orchestrator Step 5 (dispatch) checks: if `all_required_received == False`, task stays in REASONING
6. When all required contributions arrive, task becomes eligible for WORK dispatch

The implementing agent receives contributions AS CONTEXT — architect's design, QA's test definitions, security requirements are embedded in the task-context.md. The agent works FROM these inputs, not in isolation.

> [!warning] The Rework Prevention Principle
>
> Without contribution gating, the implementing agent produces work first, then specialist agents review it. Reviews find design flaws, missing test coverage, security issues. Rework follows.
>
> With contribution gating, specialist inputs arrive BEFORE work. The implementing agent builds to spec from the start. Review becomes verification (does it match the design?) instead of discovery (what's wrong with this?).
>
> OpenArms's rework economics: planning costs 1x, rework costs 5.5x. Contribution gating front-loads the planning cost and eliminates most rework.

**Anti-pattern detection:** The system flags `siloed_work` when required contributions are missing but a task somehow advanced. This catches bypass attempts or orchestrator bugs.

**Skip logic:** Subtask, blocker, concern, and spike task types skip contribution requirements entirely — they don't benefit from cross-agent input.

## Instances

> [!example]- OpenFleet: Full Implementation (10 agents, production)
>
> **Synergy matrix** (115 lines YAML): Defines contribution requirements for all role pairs. Example: software-engineer tasks require `design_input` from architect (required) and `qa_test_definition` from qa-engineer (recommended).
>
> **Contribution flow:**
> - Task assigned to software-engineer enters REASONING
> - Orchestrator Step 2.5 creates: architect contribution subtask + qa contribution subtask
> - Architect produces design (component hierarchy, target files, patterns, constraints)
> - QA produces test definitions (TC-001 through TC-007 with unit/integration/e2e classification)
> - Both delivered via `fleet_contribute` MCP tool
> - Software-engineer receives both in `INPUTS FROM COLLEAGUES` context section
> - Software-engineer's CONFIRMED PLAN references architect's design + QA's test cases
> - Only then does orchestrator dispatch to WORK
>
> **Result:** Engineer works FROM design, WITH test definitions. PR review becomes "does it match the plan?" instead of "is this the right approach?"

> [!example]- OpenArms: Solo-Agent Approximation
>
> OpenArms has no contribution system (solo agent). The approximation: the same agent produces requirements spec, infrastructure analysis, and gap analysis during Document stage, then uses those as inputs during later stages. The stage skill for Implement shows "prior scaffolds" from Scaffold stage.
>
> This is the same PRINCIPLE (earlier stages produce inputs for later stages) but without cross-agent specialization. The implementing agent and the designing agent are the same entity — which means the same biases carry through.

## When To Apply

> [!tip] Conditions for Contribution Gating
>
> - **Multi-agent fleet** — multiple specialized roles that can produce inputs in parallel
> - **Task complexity warrants review** — not every task needs architect design (skip logic for subtasks/spikes)
> - **Rework is costly** — long implementation cycles where discovering design flaws late burns significant tokens
> - **Quality reviews are failing** — PRs routinely rejected for design issues, not implementation issues
> - **Orchestrator exists** — someone needs to manage the contribution lifecycle

## When Not To

> [!warning] When Contribution Gating Adds Overhead Without Value
>
> - **Solo agent** — no one to contribute. Use stage gates instead (same principle, same entity).
> - **Trivial tasks** — bug fixes, hotfixes, documentation. Skip logic should exclude these.
> - **Time-critical work** — waiting for contributions when the fix is obvious adds latency. Hotfix model skips to implement.
> - **Homogeneous agents** — if all agents have the same capabilities, cross-agent input doesn't add specialization.

### How This Connects — Navigate From Here

> [!abstract] From This Pattern → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What is the synergy matrix?** | [[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]] — 115 lines YAML, required/recommended/conditional per role pair |
> | **Why rework prevention matters** | [[always-plan-before-executing|Always Plan Before Executing]] — planning costs 1x, rework costs 5.5x |
> | **How does this fit the immune system?** | [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]] — contributions are Line 1 (structural prevention) |
> | **Solo agent approximation?** | Same principle: document stage produces inputs for later stages. Same entity does both — no cross-agent specialization. |
> | **What readiness threshold gates work?** | [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] — readiness (definition) gates progress (execution). Contributions are part of readiness. |

## Relationships

- DERIVED FROM: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
- DERIVED FROM: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
- BUILDS ON: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
- RELATES TO: [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
- RELATES TO: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
- FEEDS INTO: [[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]

## Backlinks

[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[identity-profile|OpenFleet — Identity Profile]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]]

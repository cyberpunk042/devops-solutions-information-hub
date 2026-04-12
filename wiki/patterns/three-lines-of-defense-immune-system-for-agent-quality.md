---
title: "Three Lines of Defense — Immune System for Agent Quality"
type: pattern
domain: ai-agents
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Model: Quality and Failure Prevention"
  - "Enforcement Hook Patterns"
instances:
  - page: "Model: Quality and Failure Prevention"
    context: "Three-layer defense model defined: structural prevention, teaching, review — the immune system instantiates this at runtime"
  - page: "Infrastructure Enforcement Proves Instructions Fail"
    context: "Structural prevention (Line 1) proven by OpenArms hooks — 75% → 0% stage violations"
  - page: "Agent Failure Taxonomy — Six Classes of Behavioral Failure"
    context: "6 behavioral failure classes that Line 2 (detection) and Line 3 (correction) address"
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: openfleet-immune
    type: observation
    file: raw/articles/openfleet-immune-system.md
    description: "OpenFleet immune system design — 3 lines of defense, doctor cycle, 746 lines across 3 files"
  - id: openarms-hooks
    type: observation
    file: raw/articles/openarms-agent-behavior-failures.md
    description: "OpenArms hooks as Line 1 implementation — 215 lines, 100% stage boundary enforcement"
tags: [immune-system, three-lines-defense, enforcement, detection, correction, quality, agent-fleet, pattern]
---

# Three Lines of Defense — Immune System for Agent Quality

## Summary

AI agents are "sick by default" — LLMs are trained for plausible output, not correct output. The immune system pattern applies three lines of defense: structural PREVENTION (make correct behavior the easy path), automated DETECTION (observe behavior, identify disease patterns), and graduated CORRECTION (teach, compact, prune, escalate). The immune system is HIDDEN from agents — they experience consequences but don't see the detection machinery.

> [!info] Pattern Reference Card
>
> | Line | What It Does | Mechanism | When It Fires |
> |------|-------------|-----------|---------------|
> | **1. Prevention** | Make violations impossible | Stage-gated tool access, contribution gates, verbatim anchoring | Before agent acts |
> | **2. Detection** | Identify disease patterns | Doctor cycle (30s): protocol violation, laziness, stuck, correction threshold | While agent works |
> | **3. Correction** | Respond to detected diseases | TEACH (inject lesson), COMPACT (strip stale context), PRUNE (kill + regrow), ESCALATE (alert human) | After detection |

## Pattern Description

> [!abstract] The Five Named Diseases
>
> | Disease | Symptom | Detection Method |
> |---------|---------|-----------------|
> | **Deviation** | Work doesn't match verbatim requirement — code works but isn't what was asked | Compare output against requirement anchors |
> | **Laziness** | Addresses 3 of 5 acceptance criteria, calls it done | Check criteria coverage against completion claim |
> | **Protocol violation** | Uses work tools in analysis stage, commits during reasoning | Monitor tool calls against stage-allowed list |
> | **Confident-but-wrong** | Same mistake repeated 3+ times despite corrections | Track correction count per issue |
> | **Scope creep** | Adds features not in requirement, "while I'm here" syndrome | Compare produced artifacts against required artifacts |

**Line 1: Structural Prevention** makes correct behavior the EASY path. Tools are blocked per stage at the MCP server level — `fleet_commit` is impossible in non-work stages. Contributions from other agents (architect design, QA tests, security review) are required BEFORE work can start. The operator's verbatim words are injected into every context, not paraphrased.

Prevention doesn't require the agent to have willpower. It reshapes the environment so the correct path has less friction than the incorrect one.

**Line 2: Detection** runs a doctor cycle every 30 seconds during the orchestrator loop. Four detection functions check every active agent-task pair:
- `detect_protocol_violation()` — tools called outside allowed stage
- `detect_laziness()` — fast completion with partial criteria coverage
- `detect_stuck()` — no progress for 60+ minutes
- `detect_correction_threshold()` — 3+ corrections on same issue

Plus behavioral security scanning: credential exfiltration, DB destruction, security disabling, supply chain attacks.

**Line 3: Correction** graduates response based on severity and history:

> [!warning] Correction Escalation Ladder
>
> | Action | When | What Happens | Reversible? |
> |--------|------|-------------|-------------|
> | **TEACH** | First offense, low/medium severity | Inject lesson into agent context via gateway | Yes — agent keeps working |
> | **COMPACT** | Agent stuck, stale context | Strip old context, preserve memories + current task | Yes — agent continues with fresh context |
> | **PRUNE** | 3+ corrections, critical severity, repeat offender | Kill session, regrow fresh. All in-session memory lost. | No — clean restart |
> | **ESCALATE** | Human judgment needed | Alert PO via notification. Dispatch blocked until PO responds. | N/A — human decides |

Key design principle: "seeing the pattern does not break the pattern — it's forging the right path multiple times that does." TEACH works because it changes the agent's context, not just its awareness. PRUNE works because it's a clean restart, not a retry.

## Instances

> [!example]- OpenFleet: Full 3-Line Implementation (746 lines, production)
>
> **Line 1:** Stage-gated tool access (methodology.yaml `tools_blocked` per stage), contribution requirements as gates (synergy-matrix.yaml), verbatim anchoring in every context injection.
>
> **Line 2:** Doctor cycle runs in orchestrator Step 2 every 30 seconds. Produces DoctorReport with detections, interventions, agents_to_skip, tasks_to_block. AgentHealth profiles persist across cycles — repeat offenders get harsher responses.
>
> **Line 3:** Four correction actions implemented via gateway communication. PRUNE kills session and regrows fresh. ESCALATE sends ntfy notification to PO.
>
> **Key design:** Immune system is HIDDEN from agents. Agents experience tool blocks, context changes, session restarts — but never see the detection logic. This prevents agents from gaming the enforcement.

> [!example]- OpenArms: Line 1 Only (215 lines, production)
>
> **Line 1:** 4 Claude Code hooks — pre-bash blocks git ops, pre-write blocks methodology config edits, post-write tracks artifacts, post-compact rebuilds task instructions.
>
> **Result:** 0% stage boundary violations (was 75% before hooks).
>
> **Lines 2-3 missing:** No doctor cycle, no automated detection. Agent behavioral failures (6 classes) are detected only when operator reviews output manually. This is why clean completion rate is 20% — infrastructure prevents process violations but doesn't detect or correct behavioral failures.

## When To Apply

> [!tip] Conditions for the Immune System Pattern
>
> - **Multiple agents or autonomous operation** — human review can't catch everything at scale
> - **Recurring failure patterns** — the same diseases appear across agents and tasks
> - **Infrastructure enforcement already in place** — Line 1 (prevention) is necessary but insufficient
> - **Orchestrator or harness exists** — someone needs to run the doctor cycle
> - **Cost of undetected failure is high** — agent produces wrong work, burns tokens, compounds errors

## When Not To

> [!warning] When This Pattern Is Overkill
>
> - **Solo human-supervised agent** — the human IS the immune system. Detection is manual, correction is immediate.
> - **Simple tasks only** — if tasks are trivial enough that any completion is correct, detection overhead exceeds value.
> - **No orchestrator** — without a loop that runs the doctor cycle, Lines 2-3 have no execution environment.
> - **No behavioral data** — detection requires observing tool calls, timing, criteria coverage. If you can't observe, you can't detect.

## Relationships

- DERIVED FROM: [[Model: Quality and Failure Prevention]]
- DERIVED FROM: [[Enforcement Hook Patterns]]
- BUILDS ON: [[Infrastructure Enforcement Proves Instructions Fail]]
- RELATES TO: [[Agent Failure Taxonomy — Six Classes of Behavioral Failure]]
- RELATES TO: [[CLAUDE.md Structural Patterns for Agent Compliance]]
- RELATES TO: [[Ecosystem Feedback Loop — Wiki as Source of Truth]]
- FEEDS INTO: [[Methodology Adoption Guide]]

## Backlinks

[[Model: Quality and Failure Prevention]]
[[Enforcement Hook Patterns]]
[[Infrastructure Enforcement Proves Instructions Fail]]
[[Agent Failure Taxonomy — Six Classes of Behavioral Failure]]
[[CLAUDE.md Structural Patterns for Agent Compliance]]
[[Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[Methodology Adoption Guide]]
[[Context Compaction Is a Reset Event]]
[[Contribution Gating — Cross-Agent Inputs Before Work]]
[[Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[Harness-Owned Loop — Deterministic Agent Execution]]
[[Structured Context Is Proto-Programming for AI Agents]]
[[Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[Validation Matrix — Test Suite for Context Injection]]

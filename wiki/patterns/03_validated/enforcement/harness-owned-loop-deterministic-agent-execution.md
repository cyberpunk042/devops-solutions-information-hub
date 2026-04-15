---
title: Harness-Owned Loop — Deterministic Agent Execution
aliases:
  - "Harness-Owned Loop — Deterministic Agent Execution"
type: pattern
domain: ai-agents
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Model: Quality and Failure Prevention"
  - "Infrastructure Enforcement Proves Instructions Fail"
instances:
  - {'page': 'Model: Quality and Failure Prevention', 'context': 'Three-layer defense model — harness owns the outer loop as the highest enforcement layer'}
  - {'page': 'Three Lines of Defense — Immune System for Agent Quality', 'context': 'OpenFleet orchestrator is a harness-owned loop with 6-step deterministic cycle'}
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: openarms-harness
    type: observation
    file: raw/articles/openarms-agent-behavior-failures.md
    description: OpenArms agent-run-harness.ts — harness dispatches one task at a time, agent never sees backlog
  - id: openfleet-orchestrator
    type: observation
    file: raw/articles/openfleet-methodology-scan.md
    description: OpenFleet orchestrator.py (2,246 lines) — 6-step deterministic cycle with storm response and budget sync
tags: [harness, deterministic, orchestration, agent-execution, loop-ownership, pattern]
---

# Harness-Owned Loop — Deterministic Agent Execution

## Summary

The agent NEVER controls its own execution loop. An external harness (or orchestrator) owns task dispatch, stage validation, git operations, context management, and session lifecycle. The agent sees only the current task, calls commands when ready for transitions, and produces artifacts. Everything else — which task to work on, when to commit, when to compact, when to stop — is decided by deterministic infrastructure outside the agent's context.

> [!info] Pattern Reference Card
>
> | Component | Owner | Agent Sees |
> |-----------|-------|-----------|
> | **Task selection** | Harness/orchestrator | Only current task — never the backlog |
> | **Stage validation** | validate-stage.cjs / generic validator | Pass/fail result after calling /stage-complete |
> | **Git operations** | Harness (via commands) | Nothing — git is blocked by pre-bash hook |
> | **Frontmatter updates** | Harness (during /stage-complete) | Nothing — frontmatter edits blocked by pre-write hook |
> | **Session lifecycle** | Harness (pressure thresholds) | Rebuilt context after compaction |
> | **Completion criteria** | Harness (verify-done-when.cjs) | Pass/fail after calling /task-done |

## Pattern Description

> [!abstract] Why the Agent Must Not Own the Loop
>
> | What Happens When Agent Owns... | Failure Mode |
> |-------------------------------|-------------|
> | **Task selection** | Panic-rushes through easy tasks, avoids complex ones. Cherry-picks to maximize completion count. |
> | **Git operations** | Wrong stage labels on commits. Commits partial work. `git add -A` includes methodology config files. |
> | **Stage advancement** | Claims stage complete without validation. Skips stages when "told to continue." |
> | **Session management** | Burns entire context on one task. Doesn't compact when context pressure rises. |
> | **Backlog visibility** | Sees 10 remaining tasks → rushes current task to "make progress." Quality drops per-task. |

The pattern separates WHAT the agent does (produce artifacts, reason about code, write implementations) from HOW the process flows (which task, which stage, when to commit, when to stop). The agent is excellent at the WHAT. The harness is deterministic at the HOW.

**OpenArms implementation:**
- `agent-run-harness.ts` spawns Claude CLI subprocess
- Dispatches ONE task at a time from filtered backlog
- Agent calls `/stage-complete` → harness runs `validate-stage.cjs` → validates artifacts → commits → updates frontmatter → advances stage
- Agent calls `/task-done` → harness runs `verify-done-when.cjs` → recalculates epic readiness → logs completion
- Session pressure: continue ≤0.70, compact 0.70-0.80, fresh >0.80

**OpenFleet implementation:**
- `orchestrator.py` (2,246 lines) runs 6-step deterministic cycle every 30s
- Step 0: refresh context files. Step 1: security scan. Step 2: doctor (immune system). Step 2.5: contribution management. Step 3: ensure approvals. Step 4: wake drivers. Step 5: dispatch (max 2/cycle). Step 6: process directives. Step 7: evaluate parents. Step 8: health check.
- Brain decisions are PURE PYTHON — no Claude calls in the orchestrator loop
- Storm monitor graduates response: CRITICAL → full stop, STORM → no dispatch, WARNING → limit to 1, WATCH → monitor
- Budget mode changes propagate to CRON heartbeat intervals automatically

## Instances

> [!example]- OpenArms: Single-Agent Harness (TypeScript)
>
> **Loop:** harness.ts selects task → spawns Claude session → agent works → agent calls /stage-complete → harness validates + commits → agent continues or harness dispatches next task.
>
> **Key constraint:** Agent never sees backlog. Harness picks task based on epic priority + dependency order. Agent gets one task file with current stage and requirements.
>
> **Result:** No panic-rushing, no cherry-picking. Agent focus is 100% on current task.

> [!example]- OpenFleet: Multi-Agent Orchestrator (Python, 10 agents)
>
> **Loop:** orchestrator cycle every 30s → evaluate all agents → dispatch unblocked tasks (max 2/cycle) → monitor health.
>
> **Key constraints:**
> - Dispatch blocked without required contributions (architect design, QA tests)
> - Doctor can SKIP agents (flagged for behavioral issues)
> - Storm severity controls dispatch rate
> - Budget sync adjusts CRON intervals in real time
>
> **Result:** Deterministic — same agent/task state always produces same decision. No AI judgment in the control loop.

> [!example]- Anthropic Claude Agent SDK: Initializer + Coding Agent (Production)
>
> **Loop:** Initializer agent (first session only) writes `init.sh` + `feature_list.json` (~200 features marked `passes:false`) + `claude-progress.txt` + initial git commit. Every subsequent session = coding agent that reads progress + git log + init.sh, picks ONE feature, implements it, tests end-to-end (browser automation), flips `passes:true` only after verification, commits with descriptive message, updates progress.
>
> **Key constraint:** The system prompt and tools are IDENTICAL across both — only the initial USER prompt differs. Specialization without architectural separation. The harness owns the cross-session continuity; the agent owns the single-feature work.
>
> **Result:** Even Opus 4.5 fails at building a claude.ai clone WITHOUT this harness pattern (one-shots the app, leaves env messy, declares premature victory). With it, succeeds across many context windows. Source: [[src-anthropic-effective-harnesses-long-running-agents|Anthropic — Effective Harnesses for Long-Running Agents]] (Nov 2025).

## Convergent Evidence — Cross-Source Validation (NEW 2026-04-15)

This pattern has been independently validated across 5 sources crystallizing the harness-engineering discipline:

| Source | Validation |
|--------|------------|
| [[src-anthropic-building-effective-ai-agents\|Anthropic — Building Effective Agents]] (Dec 2024) | "Maintain simplicity, prioritize transparency, carefully craft the ACI" — three principles match the loop's design |
| [[src-anthropic-effective-harnesses-long-running-agents\|Anthropic — Effective Harnesses for Long-Running Agents]] (Nov 2025) | Production pattern (initializer + coding agent + artifacts) is harness-owned-loop applied to multi-context-window tasks |
| [[src-arxiv-natural-language-agent-harnesses\|NLAH paper]] (Tsinghua, March 2026) | Academic formalization: harness as portable text artifact, runtime as lightweight adapter — same architecture as harness.ts/harness.py |
| [[src-arxiv-meta-harness-outer-loop-search\|Meta-Harness paper]] (Stanford, March 2026) | Outer-loop search produces +7.7 points with 4× fewer context tokens — proves the harness-side has dramatic optimization headroom |
| [[src-rethinking-ai-agents-harness-engineering-rise\|Rethinking AI Agents (YouTube)]] (March 2026) | "6× performance variation from harness alone" + LangChain's TerminalBench-2 jump (rank 30+ → 5) via harness-only changes |

The harness-owned-loop pattern is now **field-validated**, not just project-validated. See [[harness-engineering-is-the-dominant-performance-lever|Lesson — Harness Engineering Is the Dominant Performance Lever]] for the synthesis.

## When To Apply

> [!tip] Conditions for Harness-Owned Loop
>
> - **Autonomous operation** — agent runs without human oversight for 30+ minutes
> - **Multi-stage processes** — stages must execute in order with validation between them
> - **Git integrity matters** — commits must be correct (message, scope, stage label)
> - **Multiple tasks** — backlog has 5+ tasks and order/priority matters
> - **Quality > speed** — clean completion rate matters more than task count

## When Not To

> [!warning] When Harness Overhead Exceeds Value
>
> - **Human-supervised interactive** — the human IS the harness. Adding infrastructure between them adds latency without safety.
> - **Single simple task** — one task, one stage, no git complexity. The overhead of harness setup exceeds the value.
> - **Exploration/research** — open-ended investigation where the agent SHOULD control direction. Harness constrains creativity.
> - **No existing infrastructure** — building a harness is weeks of work. Start with hooks (days) and commands (hours) first.

### How This Connects — Navigate From Here

> [!abstract] From This Pattern → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Why does this converge independently?** | [[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently Across Projects]] — 3 projects, same conclusion |
> | **How do the implementations compare?** | [[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]] — solo harness.ts vs fleet orchestrator.py |
> | **What commands does the agent use?** | /stage-complete (validate + commit + advance), /task-done (verify Done When + recalculate epic), /concern (file issue) |
> | **What is deterministic dispatch?** | [[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]] — 6-step cycle, pure Python brain, no LLM in loop |
> | **Goldilocks: do I need a harness?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — v1 (no harness), v2 (harness), v3 (full orchestrator). Match to PM level. |

## Relationships

- DERIVED FROM: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
- BUILDS ON: [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
- RELATES TO: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
- RELATES TO: [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]
- RELATES TO: [[enforcement-hook-patterns|Enforcement Hook Patterns]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently Across Projects]]
[[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]]
[[identity-profile|OpenFleet — Identity Profile]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic — Effective Harnesses for Long-Running Agents]]
[[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]]
[[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
[[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]]

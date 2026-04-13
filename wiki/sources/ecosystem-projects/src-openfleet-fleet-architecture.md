---
title: Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers
aliases:
  - "Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers"
  - "Synthesis: OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers"
type: source-synthesis
domain: ai-agents
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: openfleet-immune-system
    type: documentation
    file: raw/articles/openfleet-immune-system.md
    description: OpenFleet immune system design — 3 lines of defense (566 lines)
  - id: openfleet-methodology-scan
    type: documentation
    file: raw/articles/openfleet-methodology-scan.md
    description: Full OpenFleet methodology scan (798 lines)
  - id: openfleet-validation-matrix
    type: documentation
    file: raw/articles/openfleet-validation-matrix-samples.md
    description: 5 representative validation matrix scenarios (649 lines)
  - id: openfleet-synergy-matrix
    type: documentation
    file: raw/articles/openfleet-synergy-matrix.yaml
    description: Cross-agent contribution requirements (115 lines)
  - id: openfleet-tier-profiles
    type: documentation
    file: raw/articles/openfleet-tier-profiles.yaml
    description: Tier-based context depth profiles (56 lines)
  - id: openfleet-standing-orders
    type: documentation
    file: raw/articles/openfleet-standing-orders.yaml
    description: Per-role autonomous authority levels (161 lines)
tags: [openfleet, fleet, immune-system, orchestrator, tiers, contributions, dispatch, standing-orders, source-synthesis]
---

# Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers
## Summary

OpenFleet implements five novel systems for multi-agent orchestration: a 3-line immune system (prevention→detection→correction) with 5 named diseases and a 30-second doctor cycle, deterministic dispatch via a 6-step orchestrator with storm graduation, tier-based context depth earned through measured approval rates, contribution gating requiring cross-agent inputs before work, and standing orders defining autonomous authority per role. The fleet has 10 specialized agents with role-specific hooks, producing the most evolved multi-agent enforcement architecture in the ecosystem.

> [!info] Source Reference
>
> | Attribute | Value |
> |-----------|-------|
> | Source | OpenFleet project — fleet/, config/, docs/systems/, validation-matrix/ |
> | Type | Ecosystem project codebase (3,815 .md files, 2,246-line orchestrator) |
> | Author | Operator + fleet agents |
> | Date | 2026-04-12 (scan) |
> | Key claim | Multi-agent coordination requires 5 independent systems single-agent harnesses don't need |

## Key Insights

1. **Immune system is HIDDEN from agents.** Agents experience consequences but never see detection machinery. Prevents gaming. 3 lines: structural prevention (tool blocking + contribution gates), detection (30s doctor cycle: protocol violations, laziness, stuck, correction threshold), correction (TEACH→COMPACT→PRUNE→ESCALATE).

2. **5 named diseases with detection.** Deviation (output ≠ requirement), Laziness (partial criteria), Protocol violation (wrong tools per stage), Confident-but-wrong (3+ corrections), Scope creep (extra artifacts). Each has a specific detection function.

3. **Deterministic dispatch.** Orchestrator (2,246 lines Python) runs 6-step cycle every 30s. Brain decisions are PURE PYTHON — no LLM calls in the control loop. Storm severity graduates: CRITICAL→full stop, STORM→no dispatch, WARNING→limit to 1.

4. **Tier progression by approval data.** `PerformanceRecord`: model + task_type + approved + timestamp. Rolling 20-record windows. Trainee→standard (≥85%)→expert. PO confirms — data recommends, human decides. Per-task-type overrides: expert on features, trainee on security.

5. **Context depth controlled by tier.** Expert: full (all fields, contributions inline, 10 events). Lightweight: title+stage only, 0 events. 10x cost difference on routine calls.

6. **Contribution gating prevents rework.** Synergy matrix (115 lines YAML): required/recommended/conditional per role pair. Task blocked in REASONING until required contributions received. Engineer works FROM architect design + QA test definitions.

7. **Standing orders define autonomous authority.** Conservative (tasks only), standard (proactive within role), autonomous (full authority). Escalation: 2 autonomous actions without feedback → PO alert. Suspended when fleet paused or over budget.

8. **Readiness vs progress: two fields.** `task_readiness` (0-99, pre-dispatch, PO sets) vs `task_progress` (0-100, post-dispatch, agent reports). Readiness gates at 99.

9. **Validation matrix = 29 context injection tests.** TK-* (20 task), HB-* (7 heartbeat), FL-* (2 fleet). Each: exact expected context + expected behavior. Same structural skeleton — content varies, shape constant.

10. **MCP tool blocking at server level.** `tools_blocked` per stage in methodology.yaml. Stronger than hooks — tool call refused before it reaches any handler.

11. **Stage model: 6 stages.** conversation→analysis→investigation→reasoning→work→review. Different from OpenArms (5 stages) — valid instance of the same methodology framework.

12. **Budget sync to CRON.** Budget mode changes propagate to heartbeat intervals in real time. Gateway CRON tempo adjusts automatically.

## Deep Analysis

### Immune System (746 lines, 3 files)

Detection runs every 30 seconds in orchestrator Step 2. For each active agent-task pair:
1. Get or create AgentHealth profile (persistent across cycles)
2. Skip if already in lesson or pruned
3. Run 4 detection functions + security scanner
4. Decide response per detection (severity + history)
5. Build DoctorReport: detections, interventions, agents_to_skip, tasks_to_block

Correction graduation: in-lesson already → NONE (don't pile on). 3+ corrections → PRUNE. Critical → PRUNE. High + repeat → PRUNE. Stuck → FORCE_COMPACT. Medium/Low → TRIGGER_TEACHING.

### Orchestrator 6-Step Cycle

Step A: Brain decisions (pure Python) → per-agent `.brain-decision.json`. Step B: MC liveness heartbeats. Step 0: Refresh context files. Step 1: Security scan. Step 2: Doctor (immune). Step 2.5: Contributions. Step 3: Approvals. Step 4: Wake drivers. Step 5: Dispatch (max 2/cycle, storm-limited). Step 6: Directives. Step 7: Parent evaluation. Step 8: Health check.

### Contribution Flow

Task enters REASONING → `detect_contribution_opportunities()` reads synergy matrix → spawns parallel contribution subtasks → specialist agents produce design/tests/security → `check_contribution_completeness()` returns missing list + percentage → dispatch blocked until `all_required_received == True`.

Skip logic: subtask, blocker, concern, spike types skip contributions entirely.

## Open Questions

> [!question] ~~Minimum fleet size for immune system ROI?~~
> **RESOLVED:** 3+ concurrent agents. With 1-2, manual review suffices. At 3+, concurrent behavioral drift becomes invisible to manual monitoring.
> The 30-second doctor overhead may not justify for 2 agents. Breakeven: where automated detection saves more time than manual review costs.

> [!question] ~~Validation matrix drift detection?~~
> **RESOLVED:** Periodic regression testing against the 29-scenario matrix. Drift = scenarios that used to pass now fail. Run as scheduled test.
> If context builder changes without updating scenarios, they desync. Automated comparison needed.

> [!question] ~~Should wiki offer OpenFleet stage names as alternative configuration?~~
> **RESOLVED:** No. Wiki defines GENERIC stage names. OpenFleet names are their instance. Projects choose their own labels. Methodology defines stages, not labels.
> conversation/analysis/investigation/reasoning/work vs document/design/scaffold/implement/test. Both valid. Configurable per SDLC chain?

### How This Connects — Navigate From Here

> [!abstract] From This Source → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principles derive from this?** | Check FEEDS INTO relationships above |
> | **What is the Goldilocks framework?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- FEEDS INTO: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
- FEEDS INTO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
- FEEDS INTO: [[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
- FEEDS INTO: [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
- FEEDS INTO: [[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]]
- FEEDS INTO: [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
- FEEDS INTO: [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]]
- RELATES TO: [[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]

## Backlinks

[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
[[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently Across Projects]]
[[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]]
[[identity-profile|OpenFleet — Identity Profile]]

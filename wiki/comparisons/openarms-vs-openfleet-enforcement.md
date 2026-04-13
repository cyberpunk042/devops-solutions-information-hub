---
title: OpenArms vs OpenFleet Enforcement Architecture
aliases:
  - "OpenArms vs OpenFleet Enforcement Architecture"
type: comparison
domain: ai-agents
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: openarms-synthesis
    type: wiki
    file: wiki/sources/src-openarms-v10-enforcement.md
    description: OpenArms v10 enforcement synthesis — hooks, validator, commands
  - id: openfleet-synthesis
    type: wiki
    file: wiki/sources/src-openfleet-fleet-architecture.md
    description: OpenFleet fleet architecture synthesis — immune system, dispatch, tiers
tags: [comparison, enforcement, openarms, openfleet, hooks, immune-system, architecture]
---

# OpenArms vs OpenFleet Enforcement Architecture

## Summary

OpenArms and OpenFleet both enforce methodology compliance through infrastructure, but their architectures reflect fundamentally different scales: solo agent vs 10-agent fleet. OpenArms uses Claude Code hooks (shell scripts intercepting tool calls) + a harness-owned loop + model-aware validation. OpenFleet uses MCP tool blocking (server-level refusal) + a deterministic orchestrator + a 3-line immune system with automated detection and correction. The comparison reveals 6 constraints that change at fleet scale — and that both share the same foundational principle: the agent must not control its own execution.

## Comparison Matrix

> [!abstract] Enforcement Architecture Comparison
>
> | Dimension | OpenArms (solo) | OpenFleet (fleet) | Winner |
> |-----------|----------------|-------------------|--------|
> | **Agent count** | 1 | 10 | Context-dependent |
> | **Stage boundary enforcement** | 4 Claude Code hooks (215 lines shell) | MCP tool blocking per stage (YAML config) | OpenFleet — declarative, no code per rule |
> | **Validation engine** | validate-stage.cjs (1,033 lines, model-aware) | Per-stage tool restrictions + doctor cycle | OpenArms — deeper per-stage artifact checking |
> | **Loop ownership** | agent-run-harness.ts spawns Claude subprocess | orchestrator.py (2,246 lines) deterministic cycle | OpenFleet — pure Python, no LLM in loop |
> | **Git control** | Commands (/stage-complete, /task-done) | fleet_commit MCP tool (conventional commit enforced) | Comparable — both own git |
> | **Behavioral detection** | None (manual review) | Immune system: 30s doctor cycle, 5 diseases | OpenFleet — automated, continuous |
> | **Correction** | None (operator fixes) | TEACH→COMPACT→PRUNE→ESCALATE | OpenFleet — graduated, automatic |
> | **Context compaction** | post-compact hook rebuilds from files | PRUNE (kill + regrow fresh) | Different strategies — both address the problem |
> | **Cross-agent coordination** | N/A (solo) | Contribution gating + synergy matrix | OpenFleet — prevents rework structurally |
> | **Trust management** | N/A | Tier progression (approval rates → context depth) | OpenFleet — data-driven, adaptive |
> | **Readiness gating** | readiness field in frontmatter (advisory) | task_readiness gates dispatch at 99 | OpenFleet — structural enforcement |
> | **Clean completion rate** | 20% (4/5 need fixes) | Not measured same way (fleet-ops reviews) | Unknown — different measurement approaches |
> | **Implementation effort** | ~1,300 lines (hooks + validator + commands) | ~3,000+ lines (orchestrator + immune + tiers + contributions) | OpenArms — simpler, faster to build |
> | **Configuration model** | Shell scripts + CJS + YAML | YAML-driven (methodology.yaml + synergy-matrix + tier-profiles) | OpenFleet — more declarative |

## Key Insights

> [!warning] The Scale Transition Creates 6 New Requirements
>
> Solo → fleet is NOT just "run more agents." Six entirely new requirements appear:
>
> | # | Requirement | Solo (OpenArms) | Fleet (OpenFleet) |
> |---|-----------|----------------|-------------------|
> | 1 | **Behavioral detection** | Operator spots problems manually | Doctor must detect automatically — operator can't watch 10 agents |
> | 2 | **Correction** | Operator fixes, reruns | System must self-correct — TEACH, COMPACT, PRUNE |
> | 3 | **Cross-agent inputs** | Same agent does design + implement | Different agents specialize — contributions must flow before work |
> | 4 | **Trust differentiation** | One model, full context | Multiple models/tiers — context depth must adapt per trust level |
> | 5 | **Dispatch ordering** | One task at a time, linear | Priority × dependency × contribution-readiness × storm severity |
> | 6 | **Budget awareness** | Token cost per session | Budget mode affects dispatch tempo, CRON intervals, tier selection |

The convergent principle: both own the loop, both block git, both enforce stages through infrastructure. The DIVERGENCE is what happens AFTER enforcement: OpenArms stops (human reviews). OpenFleet continues (automated detection + correction + dispatch).

## Deep Analysis

### OpenArms: Deep Enforcement, No Detection

> [!tip] When to choose OpenArms architecture
> Solo agent, TypeScript/Node stack, operator reviews every output, existing Claude Code setup. Add hooks (1 day), commands (hours), validator (days). Total: ~1 week.

**Strengths:**
- Business logic detection (parses function bodies, counts control flow, strips strings/comments)
- Model-aware validation (reads current-model-config.json, adapts per task type)
- Phantom file filtering (reverted files don't count as artifacts)
- Simple to understand — 4 shell scripts + 1 CJS validator

**Weaknesses:**
- No automated behavioral detection — operator must review every run
- No correction mechanism — failures are caught post-hoc, not in real-time
- No cross-agent coordination — solo agent limitation
- Clean completion rate: 20% (80% still need manual fixes for behavioral issues)

> [!warning] Where OpenArms fails
> Overnight unattended runs with no operator review. The harness prevents stage violations but can't detect or correct behavioral failures (weakest-checker, fatigue cliff, silent conflict resolution).

### OpenFleet: Automated Detection + Correction, Less Per-Stage Depth

> [!tip] When to choose OpenFleet architecture
> Multi-agent fleet, Python stack, autonomous operation required, budget-conscious at scale. Requires: orchestrator infrastructure, MCP server, Plane integration. Total: weeks-months.

**Strengths:**
- Immune system detects 5 disease types every 30 seconds — no human needed
- Graduated correction (TEACH before PRUNE — proportional response)
- Contribution gating structurally prevents rework
- Tier progression reduces cost 10x on routine operations
- Deterministic dispatch — pure Python, same state → same decision
- Standing orders enable per-role autonomous authority

**Weaknesses:**
- Less deep per-stage artifact validation than OpenArms (no function body parsing)
- Massive implementation (3,000+ lines for core orchestrator + immune + tiers)
- Requires full MCP server infrastructure
- Doctor cycle overhead may not justify for <3 agents

> [!warning] Where OpenFleet is overkill
> Solo agent projects, POC/early-stage work, projects without MCP infrastructure. The immune system and orchestrator add operational complexity that doesn't pay back at small scale.

## Recommendation

> [!success] Choose Based on Scale and Phase
>
> | Your Situation | Recommendation |
> |---------------|---------------|
> | Solo agent, interactive | OpenArms hooks + commands (L2 enforcement) |
> | Solo agent, autonomous | OpenArms full harness (L2+, with validator) |
> | 2-3 agents, semi-autonomous | OpenArms harness + basic dispatch (L2, growing toward L2+) |
> | 4+ agents, autonomous | OpenFleet architecture (L2→L3) |
> | Fleet with budget constraints | OpenFleet + tier progression (cost optimization via context depth) |
>
> **The migration path:** Start with OpenArms hooks (1 day). Add commands (hours). Add validator (days). When you need multiple agents or overnight operation without review, add orchestrator + immune system (OpenFleet architecture).

## Open Questions

> [!question] Can OpenArms add detection without becoming OpenFleet?
> A lightweight doctor (checks stage-files.log for anomalies, flags repeated retries) could add Line 2 detection to the solo harness without the full orchestrator. Worth prototyping.

> [!question] Can the validation engines merge?
> OpenArms's business logic detection + OpenFleet's disease detection could combine into a single validation layer. The function body parsing is useful for fleet agents too.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- COMPARES TO: [[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]], [[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]]
- BUILDS ON: [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
- RELATES TO: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
- RELATES TO: [[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently Across Projects]]
- RELATES TO: [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]]
[[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently Across Projects]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
[[methodology-adoption-guide|Methodology Adoption Guide]]

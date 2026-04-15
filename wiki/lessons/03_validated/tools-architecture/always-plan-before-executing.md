---
title: Always Plan Before Executing
aliases:
  - "Always Plan Before Executing"
type: lesson
domain: ai-agents
layer: 4
status: synthesized
confidence: high
maturity: growing
created: 2026-04-08
updated: 2026-04-13
sources:
  - id: src-harness-engineering-article
    type: article
    url: https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0
    title: Building Claude Code with Harness Engineering
    ingested: 2026-04-08
  - id: src-harness-engineering-github
    type: documentation
    url: https://github.com/Chachamaru127/claude-code-harness
    title: claude-code-harness GitHub
    ingested: 2026-04-08
  - id: src-openfleet-local
    type: documentation
    project: openfleet
    path: CLAUDE.md
    title: OpenFleet — Local Project Documentation
    ingested: 2026-04-08
derived_from:
  - "Harness Engineering"
  - "OpenFleet"
  - "Claude Code"
  - "Synthesis: Claude Code Harness Engineering"
tags: [planning, agent-behavior, harness-engineering, openfleet, claude-code, plan-work-review, orchestration, rework-prevention, spec-driven]
---

# Always Plan Before Executing

## Summary

LLM agents produce dramatically better results when they produce an explicit plan before taking action — not as a soft heuristic, but as an enforced workflow step. This lesson is validated independently across three systems (OpenFleet, Harness Engineering, superpowers) that all converged on the same Plan → Execute → Review structure, each finding that skipping the planning phase causes rework, scope drift, and low-quality output that is expensive to recover from.

## Context

This lesson applies whenever an LLM agent is about to undertake a task with meaningful scope: modifying multiple files, dispatching subagents, ingesting a complex source, or making architectural decisions. It is most critical in autonomous or semi-autonomous contexts where human oversight is low and correction is expensive. It is less critical for trivial, single-step, easily reversible actions.

The triggering signal is any task that has multiple possible approaches, unclear scope, or downstream consequences that are hard to undo. In those cases, an agent that jumps directly to execution is likely to produce output that requires rework — which costs more tokens, more time, and more human attention than the planning step would have.

## Insight

> [!warning] LLM agents are token-greedy executors by default
> Given a task, the model's natural tendency is to start doing. This is efficient for simple tasks but catastrophic for complex ones — early decisions narrow the solution space in ways that may be incorrect, and partial work is often harder to correct than starting over.

Planning forces assumptions to be explicit before they are baked into actions. A written plan surfaces ambiguity the agent can resolve cheaply via a single question, rather than discovering it mid-execution after multiple file edits.

> [!tip] 5.5x planning cost prevents far costlier rework
> A Planner + Critic reviewing a proposed approach before coding costs ~5.5x the planning tokens. But it avoids rework whose cost would be far higher. Investing upfront in understanding consistently beats investing downstream in correction. This holds for single sessions, harness workflows, and 10-agent fleets alike.

## Evidence

**Harness Engineering (claude-code-harness, Chachamaru127):**
The 5-verb workflow makes planning non-optional at the tool level: `/harness-plan` is a distinct phase that produces a spec with acceptance criteria before any coding begins via `/harness-work`. In Breezing mode, a Planner and Critic agent review the task quality before the coding worker executes. The ~5.5x token cost of the planning discussion (vs ~4x without) is explicitly justified as rework prevention. The workflow mirrors the superpowers pattern (brainstorm → plan → execute → verify) and the wiki's own ingestion pipeline (extract → analyze → synthesize → write → integrate).

**OpenFleet Deterministic Orchestrator:**
The 12-step 30-second orchestration cycle separates task definition from task dispatch. Tasks are created, blocked, scheduled, and reviewed through distinct states before they reach an agent for execution. The orchestrator never dispatches a task that has not passed the "readiness" state axis — a deterministic gate that enforces planning before execution at the system level, completely independent of any LLM's judgment. The multi-dimensional state model (lifecycle, execution, progress, readiness, validation, context) exists precisely to prevent premature dispatch.

**Superpowers Workflow:**
The superpowers skill set encodes planning as a required phase (`superpowers:writing-plans`, `superpowers:brainstorming`) that precedes execution (`superpowers:executing-plans`). These are separate skills with separate invocation — the architecture itself enforces the sequence. The `superpowers:brainstorming` skill is marked as something that "MUST" be used before any creative or implementation work, reflecting a hard-won understanding that skipping it degrades output quality.

**Claude Code Context Management:**
Even at the individual agent level, Claude Code's best practices recommend using Plans and Todos to externalize work structure before beginning complex tasks. This converts an implicit "I'll figure it out as I go" approach into an explicit decomposition that can be reviewed, corrected, and tracked. The plan becomes an external memory artifact that survives context compression and keeps the agent on track across a long session.

## Applicability

**Domains:** This lesson applies to any domain where an LLM agent has meaningful autonomy and actions have non-trivial cost or reversibility. Strongest applicability: coding agents, ingestion pipelines, deployment automation, multi-agent orchestration.

**Projects in the ecosystem:**
- **OpenFleet** — Already implements this at the orchestration layer via readiness gating. Lesson is confirmed, not new, for this project.
- **Research wiki ingestion** — The `guided` and `smart` ingestion modes implement planning gates (show extraction plan, wait for approval). The `auto` mode skips this and is appropriate only for high-confidence, low-complexity sources.
- **AICP / DSPD** — Any Claude Code session working on multi-file changes benefits from explicit `/plan` before `/execute`.
- **devops-control-plane** — Post-mortem analysis (24 rules from 16 post-mortems) represents the lesson encoded as system policy.

**When to skip:** Single-step reversible actions (reading a file, running a status command, generating a manifest). The overhead of formal planning exceeds the benefit when the action space is trivially small.

**Anti-pattern to avoid:** Treating planning as an optional courtesy step ("here's what I'm going to do...") rather than an enforced workflow gate. The lesson's value comes from making planning a blocker on execution, not a preamble that can be skimmed or skipped.

> [!success] OpenArms Evidence: Specific Done When Items = Quality Forcing Function
>
> Overnight run T066-T088 comparison:
> - **T066 (7 specific Done When items):** "Pre-commit hook checks git lock," "src/hooks/event-firing.ts imports and calls workspace-coordinator," "Zero manual coordination calls in agent-directive.md." Result: 3 clean stage commits, completion log, real concern raised, proper integration.
> - **T067-T088 (4 generic Done When items):** "Implementation exists and compiles," "Tests pass with 0 failures." Result: progressive quality degradation, stage compression, no completion logs.
> - **T073 (wrong Done When for task type):** Research spike with "Implementation exists and compiles" — nonsensical for a 2-stage research model.
>
> **Mechanism:** Specific items ARE integration instructions. "src/hooks/event-firing.ts imports X" tells the agent WHERE to wire. "Wired into runtime" lets the agent decide cheaply under fatigue. Generic templates enable self-justification: "Implementation exists and compiles" is trivially true for ANY code.
>
> **Fix options (from OpenArms E016 findings):** (A) Reject protocol — agent blocks on bad items (high operator burden). (B) Dispatch-time generation — harness generates criteria from methodology.yaml artifact definitions (recommended). (C) One-time migration — rewrite all existing task Done When items.
>
> This connects directly to planning: planning IS defining specific Done When items. Generic Done When = no plan. Specific Done When = plan encoded as verifiable criteria.

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself BEFORE writing any code or producing any artifact:
>
> 1. **Do I have a plan?** Not a vague idea — a specific plan with steps. If not, I'm about to prompt-react.
> 2. **Did the user approve the plan?** If I planned in my head without presenting it, it's not an approved plan.
> 3. **Am I skipping Document/Design stages because "the solution is obvious"?** The solution felt obvious to the OpenArms agent that produced 2,073 orphaned lines too.
> 4. **Am I investing in planning or gambling on rework?** Breezing mode planning costs ~5.5x tokens upfront. Rework after a bad implementation costs far more. The exact rework multiplier is unquantified, but the direction is clear.

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What methodology enforces planning?** | [[model-methodology|Model — Methodology]] — Document and Design stages come BEFORE Scaffold/Implement/Test. Stage gates prevent skipping. |
> | **What is the cost of NOT planning?** | OpenArms evidence: Breezing mode costs ~5.5x planning tokens but prevents rework. 686 passing tests but 0 verified features because tests weren't planned against specs. |
> | **How does contribution gating enforce planning?** | [[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]] — architect design + QA tests collected BEFORE work starts. Planning is STRUCTURAL, not optional. |
> | **What readiness threshold gates execution?** | [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] — readiness (planning completeness) must cross threshold before progress (execution) begins |
> | **What is the explicit method of work?** | [[follow-the-method-of-work-not-the-methodology-label|Follow the Method of Work Not the Methodology Label]] — record requirements → research → synthesize → investigate → suggest solutions |
> | **Goldilocks for planning depth** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] — POC: brief plan. Production: full requirements spec + design + tech spec |

## Relationships

- DERIVED FROM: [[harness-engineering|Harness Engineering]]
- DERIVED FROM: [[openfleet|OpenFleet]]
- DERIVED FROM: [[claude-code|Claude Code]]
- DERIVED FROM: [[src-harness-engineering|Synthesis — Claude Code Harness Engineering]]
- RELATES TO: [[claude-code-best-practices|Claude Code Best Practices]]
- RELATES TO: [[claude-code-skills|Claude Code Skills]]
- RELATES TO: [[research-pipeline-orchestration|Research Pipeline Orchestration]]
- ENABLES: [[rework-prevention|Rework Prevention]]
- BUILDS ON: [[agent-orchestration-patterns|Agent Orchestration Patterns]]

## Backlinks

[[harness-engineering|Harness Engineering]]
[[openfleet|OpenFleet]]
[[claude-code|Claude Code]]
[[src-harness-engineering|Synthesis — Claude Code Harness Engineering]]
[[claude-code-best-practices|Claude Code Best Practices]]
[[claude-code-skills|Claude Code Skills]]
[[research-pipeline-orchestration|Research Pipeline Orchestration]]
[[rework-prevention|Rework Prevention]]
[[agent-orchestration-patterns|Agent Orchestration Patterns]]
[[E005-agent-compliance-framework|Agent Compliance Framework]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]]
[[follow-the-method-of-work-not-the-methodology-label|Follow the Method of Work Not the Methodology Label]]
[[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]]
[[immune-system-rules|Immune System Rules]]
[[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]]
[[model-claude-code|Model — Claude Code]]
[[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]
[[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
[[new-content-must-integrate-into-existing-pages|New Content Must Integrate Into Existing Pages]]
[[src-plannotator|Plannotator — Interactive Plan & Code Review for AI Agents]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]

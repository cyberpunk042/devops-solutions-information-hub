---
title: Spec-Driven Development
aliases:
  - "Spec-Driven Development"
type: concept
layer: 2
maturity: growing
domain: ai-agents
status: synthesized
confidence: high
created: 2026-04-09
updated: 2026-04-14
sources:
  - id: src-openfleet-methodology-scan
    type: documentation
    file: raw/articles/openfleet-methodology-scan.md
    title: OpenFleet Methodology Scan — Deep Research Findings
    ingested: 2026-04-09
  - id: src-openarms-methodology-scan
    type: documentation
    file: raw/articles/openarms-methodology-scan.md
    title: OpenArms Methodology Scan — Deep Research Findings
    ingested: 2026-04-09
  - id: src-superpowers-end-of-vibe-coding
    type: youtube-transcript
    file: raw/articles/superpowers-end-of-vibe-coding.md
    title: Claude Code + SUPERPOWERS = The End of Vibe Coding? (Full Tutorial)
    ingested: 2026-04-08
  - id: src-shanraisshan-claude-code-best-practice
    type: documentation
    file: raw/articles/shanraisshan-claude-code-best-practice.md
    title: shanraisshan/claude-code-best-practice
    ingested: 2026-04-08
  - id: openspec-github
    type: repo
    url: "https://github.com/Fission-AI/OpenSpec"
    title: "Fission-AI/OpenSpec — Spec-Driven Development Framework"
    ingested: 2026-04-14
tags: [spec-driven-development, bmad, spec-kit, superpowers, openfleet, planning, artifacts, immutable-checkpoints, multi-agent, sdlc, design-before-code, spec-to-code, phase-gating, brownfield, delta-specs, openspec]
---

# Spec-Driven Development

## Summary

Spec-driven development (SDD) is the discipline of producing structured, artifact-bound specification documents before any implementation begins, using those specs as immutable checkpoints between phases of AI-assisted work. Across at least four independent frameworks — BMAD-METHOD, Spec Kit, the Superpowers plugin, and OpenFleet's SPEC-TO-CODE pattern — the same principle has converged: when an LLM or agent executes work without a pre-committed spec, it will hallucinate scope, conflate phases, and produce output that does not match intent. The spec is not a planning aid; it is a corruption barrier between understanding and execution.

## Key Insights

> [!warning] Universal convergence — 10 frameworks, same cycle
> BMAD-METHOD, Superpowers, Spec Kit, GSD, OpenSpec, gstack, and more independently arrived at: Research/Understand → Spec → Plan → Execute → Review. They differ only in tooling; the structure is identical. This is an emergent property of how LLMs fail without spec gates.

> [!abstract] The spec is a phase boundary, not documentation
> The spec artifact separates "understand" from "plan" and "plan" from "execute." Crossing the boundary without the artifact is the root cause of scope creep, rework, and context drift. BMAD: PRD/architecture artifacts. Superpowers: explicit spec document. OpenFleet: SPEC-TO-CODE.md. OpenArms: wiki pages as design artifacts before src/ files.

- **SPEC-TO-CODE as alignment infrastructure**: OpenFleet formalizes spec-to-code as a living mapping document (69 specs → 94 modules), tracking three states per spec: ✅ implemented and matches, ⚠️ PARTIAL (gap documented), ❌ NOT DONE (read spec, implement from scratch). This document prevents "spec drift" — code evolving away from design. A contamination cleanup pass (2026-04-01) removed 70 fabricated tests for behavior that was never specified: "spec first, code second."

- **Verbatim provenance is spec integrity**: All three production systems (OpenFleet, OpenArms, this wiki) enforce that original operator/PO directives are never paraphrased. OpenFleet chains this verbatim quote through: PO log → design spec → OCMC task field → agent context → fleet-ops review check. Any paraphrase breaks the chain and produces work that is compliant with an interpretation rather than the original intent.

- **Standards document before code**: OpenFleet elevates this to: "No code without meeting its standard." Every artifact type has a standards document created before any implementation begins. These standards gate delivery milestones — you cannot close milestone B1 (CLAUDE.md ×10) without the `claude-md-standard.md` existing first. This is SDD applied to infrastructure artifacts, not just features.

- **The superpowers workflow as the accessible entry point**: The Superpowers plugin for Claude Code operationalizes SDD for solo developers: brainstorm (understand the ticket, explore the codebase, propose UI mockups) → spec generation (edge cases, acceptance criteria, API routes, component architecture) → implementation plan (11 tasks, each with test files, implementation steps, checkpoints) → sub-agent execution (fresh context window per task) → code review agent. No manual coding required. The spec document is the product of the brainstorm phase and the precondition for the plan phase.

- **BMAD's multi-agent specialization of SDD**: BMAD-METHOD (44k stars) structures the spec phase as a multi-agent process where different agent personas (Business Analyst, Architect, Product Manager) each contribute their domain view to the spec before development begins. This prevents a single-agent spec that has implicit blind spots. The spec becomes a multi-perspective artifact before any code agent touches it.

- **"Not live tested = not finished" extends to specs**: OpenFleet maintains a strict distinction between "spec exists" (📐), "code exists" (🔨), and "verified" (✅). A system can have 200 unit tests and still be 🔨 if no real agent has used it in a real task. The SDD principle extends beyond the spec phase: every stage boundary requires an artifact demonstrating that the phase was completed, not just initiated.

## Deep Analysis

### What Spec-Driven Development Solves

The fundamental problem SDD solves is **phase conflation** — when an AI agent or developer begins implementing while still understanding the problem, or begins understanding the next problem while still implementing the current one. Without explicit phase boundaries enforced by artifact checkpoints, the agent oscillates between phases and produces output that is:

1. **Locally coherent but globally misaligned** — correct code for the wrong spec
2. **Scope-contaminated** — implementation details that were never asked for
3. **Unverifiable** — no spec to compare the output against
4. **Irreversible at cost** — rework is exponentially more expensive after implementation

SDD creates **immutable checkpoints** at each phase boundary. The checkpoint is not a flag in a config file — it is a concrete artifact (spec document, design doc, wiki page, plan document) that must exist before the next phase can begin. This is the structural insight: gates work only when they require physical evidence.

### Framework Comparison Matrix

| Dimension | BMAD-METHOD | Spec Kit | Superpowers | OpenFleet SDD |
|-----------|-------------|----------|-------------|---------------|
| **Spec phase name** | PRD + Architecture | Constitution → Specify | Brainstorm → Spec | CONVERSATION → ANALYSIS → REASONING |
| **Plan phase name** | Stories / Tasks | Plan | Plan (11 tasks) | REASONING (plan doc) |
| **Execute phase name** | Dev agent | Tasks | Sub-agent execution | WORK (fleet_task_accept) |
| **Enforcement mechanism** | Agent personas + checklist | Human review gates | Sub-agent isolation (fresh context) | MCP tool blocking (fleet_commit, fleet_task_complete) |
| **Spec artifact type** | PRD.md, ARCHITECTURE.md | spec.md (templated) | Structured spec document | Design spec + standards doc |
| **Multi-agent?** | Yes (specialized agents per phase) | No (single agent workflow) | Yes (brainstorm → subagents) | Yes (10 agents, contribution matrix) |
| **Spec→Code traceability** | Story → code | Not formalized | Acceptance criteria → tasks | SPEC-TO-CODE.md (living, 69→94 mapping) |
| **Verbatim provenance** | Not explicit | Not explicit | Not explicit | Core protocol (chain through 6 steps) |
| **Standards gates** | PRD quality criteria | Not formalized | Code review agent | 8 standards docs, per-type gates |
| **Contamination protection** | Persona boundaries | Human review | Fresh context window per task | Teaching system + MCP blocking + fleet-ops review |
| **Scale** | 44k stars, 22+ platforms | Community | Production (BookWorm.ai demo) | 10-agent production system |

### The "Spec as Anti-Corruption Layer" Insight

OpenFleet's contamination cleanup (2026-04-01) reveals a critical insight about SDD that is not obvious from the framework documentation alone: without a spec, an agent will **invent specifications**. The contamination was not random code — it was coherent code with 70 tests, all implementing behavior that someone (likely an agent) had imagined and then treated as real requirements. The spec document is not just a planning tool; it is the **boundary between reality and fabrication**.

This explains why the Superpowers framework calls the pre-spec phase "brainstorm" rather than "plan" — the brainstorm phase is explicitly about exploring and constraining the problem space before any output is locked in. The spec document that emerges from brainstorm is the contract between "what was actually requested" and "what will be built."

### OpenArms' Adaptation: Wiki Pages as Spec Artifacts

OpenArms adapts the SDD pattern for a solo agent operating without a PO: each task's "Document" stage produces a wiki page (not a spec document in a separate artifacts folder). The wiki page serves the same function — it is the artifact that proves the understanding phase was completed. The design stage produces a design doc (also a wiki page). This means the wiki IS the spec system, and the wiki's commit log IS the audit trail.

The rule: "Document stage: wiki pages ONLY — no src/ files." This is SDD in its purest form — the artifact boundary is enforced at the file-system level, not just by convention.

### The Injection Order Insight (OpenFleet)

OpenFleet's "autocomplete chain engineering" reveals that SDD has a context dimension in addition to the document dimension. The agent context is assembled in this order: identity → values → role rules → stage protocol → tools → colleagues → fleet state → current task with verbatim → stage instructions (MUST/MUST NOT) → contributions → trail → context awareness. This sequence is designed so that "the correct next action is the natural continuation." The spec (task verbatim + design spec) is injected late in the sequence — after the agent has been fully grounded in who it is, what values it holds, and what its role is. The spec cannot corrupt the agent's identity because the identity comes first.

### Spec Document Quality Standards

All surveyed frameworks include quality requirements on the spec itself:

- **OpenFleet `plan_quality.py`**: Validates plans at `fleet_task_accept()`. Plan must: reference verbatim, specify target files, map criteria to steps. Plan submitted before commits allowed.
- **Superpowers**: Spec must include edge cases, acceptance criteria, API routes, component architecture. Each task in the plan includes test files and implementation steps.
- **BMAD**: PRD must be reviewed by multiple agent personas before development begins.
- **OpenArms**: Design stage: "Make decisions, define config shape." Produces design doc and type sketches in documentation (not in code). The design doc must exist in wiki pages before any scaffold stage begins.

The convergence: a spec is insufficient if it is vague, missing acceptance criteria, or not traceable to a requirement.

### OpenSpec: Fluid Actions vs. Phase Gates — A New SDD Architecture

OpenSpec v1.0 (OPSX) introduces a structurally different enforcement model compared to earlier SDD frameworks. Rather than phase gates that must be sequentially cleared, OPSX uses an **artifact dependency graph** — a directed acyclic graph (DAG) where artifacts enable rather than block. The key shift:

| Aspect | Phase-Gate SDD (BMAD, Superpowers) | Dependency-Graph SDD (OpenSpec OPSX) |
|--------|-------------------------------------|--------------------------------------|
| **Constraint mechanism** | Stage readiness gates | Artifact dependency graph |
| **Enforcement** | Phase boundary artifacts block progress | Dependencies enable creation, not block |
| **Iteration** | Within a stage | Edit any artifact anytime |
| **Backtracking** | Awkward; phase gates don't let you go back | Natural — just edit the artifact |
| **Context** | Agent workflow, batch operations | Code project, incremental delivery |

OpenSpec's dependency graph for the default `spec-driven` schema:

```
proposal (root)
    ├──► specs (requires: proposal)
    └──► design (requires: proposal)
              └──► tasks (requires: specs + design)
                         └──► APPLY (requires: tasks)
```

The philosophy: "dependencies are enablers, not gates." If you're implementing and discover the design is wrong, you edit `design.md` and continue. There's no phase gate preventing backtracking. This works for code projects where requirements legitimately emerge during implementation. Phase gates (our wiki's methodology, BMAD) are appropriate for knowledge synthesis and infrastructure design where the cost of wrong-direction work is higher and early-stage artifacts genuinely must mature before later stages are attempted.

### Delta Specs: SDD for Brownfield Development

All surveyed SDD frameworks were primarily designed for 0→1 (greenfield) development. OpenSpec's delta spec format extends SDD to 1→N (brownfield) modification, which represents the majority of real software work.

A delta spec describes only what's changing relative to the existing behavioral specification:

```markdown
## ADDED Requirements
### Requirement: Two-Factor Authentication
The system MUST support TOTP-based two-factor authentication.

## MODIFIED Requirements
### Requirement: Session Expiration
The system MUST expire sessions after 15 minutes.
(Previously: 30 minutes)

## REMOVED Requirements
### Requirement: Remember Me
(Deprecated in favor of 2FA.)
```

On archive, each section is processed semantically at the requirement level — appended, replaced, or deleted in the living `openspec/specs/` folder. Two parallel changes can touch the same spec file as long as they modify different requirements, making conflict avoidance structural rather than procedural.

The key architectural distinction: OpenSpec separates `openspec/specs/` (behavioral truth, stable) from `openspec/changes/` (proposed modifications, ephemeral). Changes are self-contained folders with all related artifacts (proposal, specs delta, design, tasks) that merge atomically into the living spec on archive. This "change as folder" model enables: parallel work without conflict, clean audit history with preserved WHY/HOW context, and review efficiency (one folder = one complete picture).

### Progressive Rigor: Spec Weight Must Match Change Risk

OpenSpec explicitly names the bureaucracy trap: applying full spec rigor to every change kills adoption. The framework distinguishes:

- **Lite specs** (default): short behavior-first requirements, clear scope and non-goals, a few concrete acceptance checks
- **Full specs** (high-risk): RFC 2119 keywords throughout, complete Given/When/Then coverage, cross-team coordination, API/contract changes, migrations, security/privacy concerns

The heuristic: "use the lightest level that still makes the change verifiable." This calibration principle is absent from most SDD documentation but is critical for real-world adoption. The same principle appears in our methodology as model selection — `hotfix` and `documentation` models avoid full stage-gate overhead for cases where the overhead exceeds the risk.

## Open Questions

- How do spec artifacts handle mid-project discovery? All frameworks assume spec precedes implementation, but real projects often discover requirements during implementation. OpenFleet has a REASONING stage that collects contributions before WORK — is that sufficient for mid-flight spec evolution?
- The BMAD multi-agent spec model produces higher-quality specs but at higher cost. Is there a lightweight multi-perspective spec approach for solo developers that approximates the multi-agent benefit?

## Answered Open Questions

> [!example]- Can spec quality be evaluated automatically?
> Resolved in [[stage-gate-operational-decisions|Decision — Stage-Gate Operational Decisions]]. Partially — lint checks can validate required fields (verbatim reference, target files, step mapping). Semantic completeness remains a human judgment, but structural completeness is automatable.

> [!example]- Minimum viable spec for small tasks?
> Resolved in [[stage-gate-operational-decisions|Decision — Stage-Gate Operational Decisions]]. Task type determines spec scope: `docs` = Document stage only, `spike` = Document + Design, `task` = Scaffold + Implement + Test. The tiered approach matches spec overhead to task complexity.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[design-md-pattern|Design.md Pattern]] (spec artifacts as first-class project documents)
- BUILDS ON: [[rework-prevention|Rework Prevention]] (spec gates prevent the rework that occurs without them)
- IMPLEMENTS: [[plan-execute-review-cycle|Plan Execute Review Cycle]] (spec is the output of the Plan phase and the input to Execute)
- RELATES TO: [[task-lifecycle-stage-gating|Task Lifecycle Stage-Gating]] (spec-driven development requires stage enforcement to prevent spec-skipping)
- RELATES TO: [[agent-orchestration-patterns|Agent Orchestration Patterns]] (BMAD uses multi-agent spec production)
- RELATES TO: [[openfleet|OpenFleet]] (primary source — SPEC-TO-CODE.md, contamination cleanup, plan_quality.py)
- RELATES TO: [[harness-engineering|Harness Engineering]] (harness is the spec-driven development tooling layer)
- FEEDS INTO: [[wiki-backlog-pattern|Wiki Backlog Pattern]] (when wiki pages are spec artifacts, the wiki IS the spec system)
- BUILDS ON: [[src-openspec-spec-driven-development-framework|Synthesis: OpenSpec — Spec-Driven Development Framework]] (primary new source: delta specs, OPSX fluid actions, dependency graph model)

## Backlinks

[[design-md-pattern|Design.md Pattern]]
[[rework-prevention|Rework Prevention]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[task-lifecycle-stage-gating|Task Lifecycle Stage-Gating]]
[[agent-orchestration-patterns|Agent Orchestration Patterns]]
[[openfleet|OpenFleet]]
[[harness-engineering|Harness Engineering]]
[[wiki-backlog-pattern|Wiki Backlog Pattern]]
[[src-openspec-spec-driven-development-framework|Synthesis: OpenSpec — Spec-Driven Development Framework]]
[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[stage-gate-operational-decisions|Decision — Stage-Gate Operational Decisions]]
[[methodology-framework|Methodology Framework]]
[[model-methodology|Model — Methodology]]
[[specs-as-code-source-inverts-hierarchy|Specs-as-Code-Source Inverts the Traditional Hierarchy]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[src-autobe-compiler-verified-backend-generation|Synthesis — AutoBE: Compiler-Verified Backend Generation]]
[[src-shanraisshan-claude-code-best-practice|Synthesis — Claude Code Best Practice (shanraisshan)]]
[[src-pydantic-ai-typed-agent-framework|Synthesis — Pydantic AI: Typed Agent Framework]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]

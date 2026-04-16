---
title: "Progressive Structural Enrichment in Agent Config"
aliases:
  - "Progressive Structural Enrichment in Agent Config"
  - "Progressive Structural Enrichment"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: medium
maturity: seed
instances:
  - page: "OpenArms AGENTS.md 2026-04-16 trajectory"
    context: "471 lines (encyclopedia, bullets only, 0 tables) → 124 lines (lean routing table + 12 companion rule files) → 144 lines (added Goldilocks identity table + Three Principles table with measured evidence). Two enrichment steps after the lean foundation. Each step added STRUCTURE, not prose. Compliance improvements measurable (5/8 CLAUDE.md Structural Patterns applied in one session)."
  - page: "Research Wiki CLAUDE.md 2026-04-11 to 2026-04-16 trajectory"
    context: "Started ~170 lines. Added gateway orient as first essential command, MCP tool count update, second-brain/sister context detection. Each change added structured content (tables, command lists) to the lean foundation. Stayed under 200 lines throughout — the <200 line target enforced the 'enrich structurally, not with prose' discipline."
derived_from:
  - "CLAUDE.md Structural Patterns for Agent Compliance"
  - "Models Are Built in Layers, Not All at Once"
  - "Hardcoded Instances Fail — Build Frameworks Not Solutions"
created: 2026-04-16
updated: 2026-04-16
sources:
  - id: openarms-agents-restructure
    type: file
    project: openarms
    path: wiki/log/openarms-agents.md-restructure-confirms-structural-patterns-.md
    description: "OpenArms marker note documenting the 471 → 124 → 144 line trajectory with 5/8 structural patterns applied"
  - id: openarms-integration-notes
    type: file
    project: openarms
    path: wiki/log/2026-04-16-second-brain-integration-notes.md
    description: "Parts 15, 22, 23 — documents the AGENTS.md evolution across the session"
  - id: sfif-pattern
    type: wiki
    file: wiki/patterns/03_validated/architecture/scaffold-foundation-infrastructure-features.md
    description: "SFIF applied to agent config: scaffold (lean) → foundation (routing) → infrastructure (structured additions) → features (richer compliance signals)"
tags: [pattern, agent-config, claude-md, agents-md, progressive-enrichment, structural, contributed, openarms]
---

# Progressive Structural Enrichment in Agent Config

## Summary

Agent configuration files (CLAUDE.md, AGENTS.md, companion rule files) are most compliant when evolved in layers: start lean (routing table, sacrosanct section, essential pointers), then ENRICH with structured additions (tables, typed lists, principle tables with measured evidence) — NOT with prose paragraphs. The pattern inverts the usual "document everything" impulse: the first version should be aggressively small (<200 lines) and route to companion files; subsequent evolutions add STRUCTURE (tables, numbered sequences, ALLOWED/FORBIDDEN blocks), staying under the size ceiling. Each enrichment step is a measurable compliance improvement, not a content dump. OpenArms's AGENTS.md went 471 → 124 → 144 over one session — shrinking first, then enriching with structure twice, and measurably improving CLAUDE.md Structural Patterns coverage (5/8 patterns applied) throughout.

## Pattern Description

The pattern has four structural steps — apply in order:

**Step 1 — Shrink to a routing table.** The starting document is usually an encyclopedia: 400-700 lines of accumulated prose, bullet lists, and inline details. The first move is aggressive: identify the 3-5 sections that program behavior on every message (sacrosanct directives, identity, hard rules, methodology pointers, routing table) and extract everything else to companion rule files (`.claude/rules/*.md`, `.agents/rules/*.md`). Target: <200 lines. Expect 60-75% line reduction.

**Step 2 — Add the Goldilocks / identity structure.** Once lean, add a structured identity table declaring the STABLE project properties (type, domain, phase, scale, second-brain relationship). NOT consumer properties (execution mode, SDLC profile, methodology model — those are per-task/per-connection). The identity table programs every downstream decision: model selection, enforcement level, context tier. It is the highest-leverage structure to add after the routing table.

**Step 3 — Add the governing principles with measured evidence.** If the project has internalized its principles (from the second brain or its own operation), add them as a structured table with columns: principle name / what it says / measured evidence. Prose principles are ignorable. Evidence-bound principles in a table are proto-programming. This is the second enrichment step — typically 15-30 lines that raises compliance measurably.

**Step 4 — Iterate with structural additions only.** Subsequent changes ADD structured content (a new table, a new numbered sequence, a typed callout with evidence) — NOT prose paragraphs. If a change doesn't fit in a structural form, it belongs in a companion rule file. The size ceiling (<200 lines) enforces this discipline: exceeding it forces extraction. The ceiling is not arbitrary — it is the empirical threshold where compliance starts degrading (per Context Engineering's tier budgets and Opus 4.7's ×1.35 tokenizer amplification).

**The compounding property:** each step builds on the previous. Enriching with principles before shrinking to routing produces a 600-line monster with great principles buried in noise. Shrinking first, then enriching, produces a 144-line document with dense structural signal. The ORDER is what makes the compliance gain possible.

## Instances

> [!example]- Instance 1: OpenArms AGENTS.md 2026-04-16 (three-step trajectory)
>
> **Before (start of session, v1):** 471 lines. 0 tables. 0 section dividers. 44 bullet lists. 0 numbered lists. Topic-based organization (identity section, methodology section, skills section, hooks section — each 20-40 lines of prose with bullets). 75% stage boundary violations per overnight runs (v8 baseline). This is the "encyclopedia" anti-pattern.
>
> **Step 1 — shrink to routing table (commit `0507a2ad`):** 471 → 124 lines. Extracted 12 companion rule files to `.claude/rules/` (methodology, stages, skills, concerns, hooks, learnings, etc.). AGENTS.md retained: sacrosanct section, identity pointer, methodology pointer, skills/commands pointer, hooks pointer, routing table. 74% line reduction.
>
> **Step 2 — add identity structure (commit `a6c13c8c`):** 124 → ~135 lines. Added Goldilocks Identity Profile table declaring STABLE project fields (type, domain, phase, scale, second-brain relationship). Explicitly omitted consumer properties (execution mode, SDLC profile, methodology model) per the execution-mode-is-consumer-property lesson. Compliance: gateway `status` now detects identity correctly.
>
> **Step 3 — add principles table (commit `73f89612`):** ~135 → 144 lines. Added Three Principles table with measured evidence per row: Infrastructure > Instructions (OpenArms v8 75% → v10 0%), Goldilocks (T116 $9.07 vs T117 $1.20 = 86.8% reduction), Structured Context > Content (AGENTS.md 0 tables vs agent-directive.md 3 tables = 65pp compliance difference). Evidence-bound principles program every design decision downstream.
>
> **Measured result:** 5 of 8 CLAUDE.md Structural Patterns applied in one session (Sacrosanct retained, Progressive Disclosure via routing, Command Checkpoints /stage-complete+/task-done, Section Dividers in restructured learnings.md, Hard/Soft Rule Separation in learnings.md tables). Still missing: Anchor Phrases (Pattern 7) and Concrete Examples (Pattern 8). Final state: 144 lines, under 200 target, compliance improvements measurable.

> [!example]- Instance 2: Research Wiki CLAUDE.md 2026-04-11 to 2026-04-16
>
> Started at ~170 lines when ingestion pipeline was established. The <200 line target was declared early (per ETH Zurich research on context file length degrading task success). Evolution across 5 days:
>
> **Enrichment step 1:** Added gateway orient as first Essential Command. Structured as routed table entry, not prose.
>
> **Enrichment step 2:** Added MCP tool count update (21 → 26+) and "Use gateway MCP tools" pointer. Structured as list entry.
>
> **Enrichment step 3:** Added second-brain/sister context detection and Gateway Output Contract pointer. Structured as new Essential Commands table row.
>
> **Total delta across 5 days:** ~25 lines added, all structured. Zero prose paragraphs. Line count stayed well under 200. Each addition raised gateway's ability to route agents correctly (enforcement visible in E022 module tests).

## When To Apply

- **When inheriting an encyclopedia-style agent config** (400+ lines of prose, few tables, no routing)
- **When compliance is below target** and restructuring the same content produces different results (per CLAUDE.md Structural Patterns)
- **When the project has multiple cognitive contexts reading the same file** (operator + agent + sub-agent + persona template + provisioned agent) — structure is the only way to separate per-context rules
- **When a companion file system already exists** (`.claude/rules/`, `.agents/skills/`, etc.) to absorb the extracted content

## When Not To

- When the current file is already lean (<200 lines, well-structured, high compliance measurable). Don't restructure for its own sake.
- When there's no companion file system to extract TO. The pattern requires somewhere to put the extracted prose.
- When the project is too small (single-person, single-session) for structural overhead to be worth it. Use judgment: if a 400-line document actually works at your scale, don't "fix" it.
- At the wrong stage: restructuring CLAUDE.md during active agent runs creates a race (see [[the-pre-write-hook-prevents-operator-claude-from-racing-the-|Pre-Write Hook Race Prevention]]).

## Self-Check

> [!warning] Before applying this pattern, ask:
>
> 1. What's the current line count of my primary agent config file?
> 2. How many tables does it contain? How many dividers? How many numbered sequences?
> 3. Is there a companion file system I can extract to, or do I need to create one?
> 4. What's my measurable compliance baseline (stage violations, skill-invocation rates, etc.)? Record it before restructuring so you can measure the improvement.
> 5. Do I have an identity profile I can add as a structured table (distinguishing stable project properties from consumer properties)?
> 6. Do I have governing principles with measured evidence (not aspirational statements)?
>
> If line count >300 AND tables/dividers count is low AND companion file system exists (or can be created): the pattern fits. Execute in the three-step order.

## Structural Properties

| Property | Description |
|---|---|
| **Composability** | Composes with CLAUDE.md Structural Patterns — this pattern is the EVOLUTION PROCESS; that pattern is the TARGET STRUCTURE |
| **Reversibility** | Easy. Git history preserves each step. Rolling back an enrichment step = one revert. |
| **Scale** | Applies at project level. Fleet scale requires per-agent variation (SOUL.md + HEARTBEAT.md) but the same three-step logic |
| **Cost** | Low effort: 2-4 hours for the initial shrink; 30-60 min per enrichment step |
| **Evidence bar** | Instances require before/after line counts, structural element counts (tables/dividers/numbered), and at least one measurable compliance delta (violation rate, structural patterns coverage, gateway detection success) |

## How This Connects — Navigate From Here

> [!abstract] From This Pattern → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The target structure** | [[claude-md-structural-patterns\|CLAUDE.md Structural Patterns for Agent Compliance]] — 8 patterns this pattern progressively applies |
> | **The governing principle** | [[structured-context-governs-agent-behavior-more-than-content\|Principle — Structured Context Governs Behavior]] — structure > content |
> | **The SFIF analog** | [[scaffold-foundation-infrastructure-features\|SFIF]] — same logic at build-lifecycle level (lean scaffold, enrich by stage, don't build features-first) |
> | **The layering lesson** | [[models-are-built-in-layers-not-all-at-once\|Models Are Built in Layers]] — same anti-pattern avoided |
> | **The size-ceiling rationale** | [[model-context-engineering\|Model — Context Engineering]] — <200 line target from tier budget + tokenizer evidence |
> | **The consumer-property guard** | [[execution-mode-is-consumer-property-not-project-property\|Execution Mode Is a Consumer Property]] — what NOT to put in the identity table |
> | **The first adoption** | [[identity-profile\|OpenArms — Identity Profile]] — Instance 1 project reference |

## Relationships

- DERIVED FROM: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
- DERIVED FROM: [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- PARALLELS: [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
- RELATES TO: [[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property]]
- RELATES TO: [[model-context-engineering|Model — Context Engineering]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- FEEDS INTO: [[model-claude-code-standards|Claude Code Standards]]

## Backlinks

[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property]]
[[model-context-engineering|Model — Context Engineering]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[Claude Code Standards]]
[[consumer-integration-roadmap-exemplar|Consumer Integration Roadmap — OpenArms Exemplar (First Full Plan)]]

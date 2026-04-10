---
title: "Model: Methodology"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources:
  - id: src-openarms-methodology
    type: documentation
    file: raw/articles/openarms-methodology-yaml-full.md
    title: "OpenArms Methodology YAML + Agent Directive"
    ingested: 2026-04-09
  - id: src-openfleet-methodology-scan
    type: documentation
    file: raw/articles/openfleet-methodology-scan.md
    title: "OpenFleet Methodology Deep Scan"
    ingested: 2026-04-09
  - id: src-openarms-methodology-evolution
    type: documentation
    file: raw/articles/openarms-methodology-evolution-2026-04-09.md
    title: "OpenArms Methodology Evolution — 7 Bugs, 6 Versions"
    ingested: 2026-04-09
  - id: src-openarms-integration-sprint
    type: documentation
    file: raw/articles/openarms-integration-sprint-learnings.md
    title: "OpenArms Integration Sprint Learnings"
    ingested: 2026-04-09
tags: [methodology, model, stage-gate, task-types, composable, backlog, execution-modes, framework, spine, flexible, multi-track, multi-model]
---

# Model: Methodology

## Summary

The Methodology model defines a flexible FRAMEWORK for defining, selecting, composing, and adapting work processes. It is NOT one fixed pipeline — it is a system that CONTAINS multiple named methodology models (Feature Development, Research, Knowledge Evolution, Hotfix, Documentation, and more), selects between them based on conditions (task type, project phase, domain, scale, urgency), composes them (sequentially, nested, conditionally, in parallel), and adapts them per-instance through overrides. Three parallel tracks run on every project simultaneously: execution (how things get built), PM (what gets tracked), and knowledge (what gets learned). Where the [[Model: LLM Wiki]] defines WHAT the wiki IS, this model defines HOW all work proceeds. The canonical definition lives in [[Methodology Framework]]. The executable configuration lives in `wiki/config/methodology.yaml` and `wiki/config/agent-directive.md`.

## Key Insights

- **Multiple models, not one pipeline.** Feature Development has 5 stages. Research has 2. Knowledge Evolution has 4 with different stage names. Hotfix has 2. These are INDEPENDENT models, not subsets of one sequence. A project may use all of them at different times for different work.

- **Conditions select which model runs.** Task type is one condition. But also: project phase (Foundation emphasizes Document+Design; Features emphasizes Implement+Test), domain (code vs knowledge vs infrastructure), scale (single function vs new module), urgency (critical bug → Hotfix model), current state (greenfield vs legacy). Selection is multi-dimensional — all conditions evaluate simultaneously.

- **Models compose at every scale.** SFIF runs at project level. Inside each SFIF stage, task-level models run. Inside a task, stages execute. This is fractal — the same vocabulary (stages, gates, artifacts, readiness) at every level. Plus: three tracks run in PARALLEL on every project (execution, PM, knowledge) — not one sequence.

- **Stage boundaries are enforced, not suggested.** ALLOWED and FORBIDDEN artifact lists per stage. Document may not produce code. Scaffold may not implement business logic. Implement MUST wire into the runtime. This was learned from real failures — OpenArms Bug 5 (scaffold produced 135 lines of business logic) and Bug 6 (2,073 lines of orphaned code nobody imported).

- **The quality dimension is an explicit parameter.** Skyscraper (full process), Pyramid (deliberate compression), Mountain (accidental chaos). The choice is made per-situation, not accidentally.

- **The methodology was hardened by 7 real bugs in one day of autonomous operation.** Every design decision traces to a failure that proved it necessary. This is not theory — it is battle-tested from OpenArms' first autonomous agent run.

## Deep Analysis

### What Is a Methodology Model

A methodology model is a named, first-class entity defined in configuration (not hardcoded in logic). Every model has:

| Component | What it defines | Example |
|-----------|----------------|---------|
| **Name** | Unique identifier | `feature-development`, `research`, `hotfix` |
| **Stages** | Ordered sequence of phases | document → design → scaffold → implement → test |
| **Artifacts** | What each stage must produce | Wiki page, spec, type definitions, working code, passing tests |
| **Gates** | Transition rules between stages | Automatic, human-reviewed, score-based |
| **Protocols** | Per-stage ALLOWED and FORBIDDEN lists | Scaffold ALLOWED: types, schemas. FORBIDDEN: business logic. |
| **Parameters** | Configurable values | Readiness ranges, max retries, commit style |

A model is DATA. It is defined in `methodology.yaml`, not embedded in code. This means models can be created, versioned, compared across projects, and selected at runtime.

For the full structural definition, see [[Methodology Framework]].

### The Model Catalog

These are the named methodology models available in the framework. Each is a DIFFERENT stage sequence for a different kind of work:

**Feature Development** — document → design → scaffold → implement → test
The full 5-stage model for complex work. Used for epics, modules, and refactors. Each stage has ALLOWED and FORBIDDEN artifact lists (see Stage Boundaries below). This is the most common model but NOT the only one.

**Research** — document → design
Investigation without implementation. Produces understanding and options, never code. Capped at 50% readiness by design — 50% IS completion for a research task. Used for spikes and exploratory work.

**Knowledge Evolution** — document → implement
Generate evolved pages (lessons, patterns, decisions) from existing wiki knowledge. Document stage = cross-reference existing pages, identify the insight. Implement stage = write the evolved page. No scaffold or design needed — the "design" is the existing knowledge being distilled.

**Documentation** — document
Single-stage model for writing wiki pages, guides, specs. Done when the document passes quality gates.

**Bug Fix** — document → implement → test
Restore correct behavior. Document stage = understand what's broken and why. No design stage — bug fixes should not introduce new architecture. Implement = fix it. Test = verify it's fixed AND nothing else broke.

**Refactor** — document → scaffold → implement → test
Restructure without changing behavior. Document = understand current structure and target. Scaffold = create new structure. Implement = move code into new structure. Test = verify behavior unchanged.

**Hotfix** — implement → test
Emergency fix when the problem and solution are already understood. No documentation, no design, no scaffolding. Just fix and verify. Used when urgency overrides process — the EXPLICIT choice to operate at Pyramid tier for this one task.

**Ingestion Pipeline** — ingest → synthesize → cross-reference → evolve
The knowledge track's model. Completely different stage names — this is NOT a subset of the 5-stage model. Ingest = fetch and save raw source. Synthesize = create source-synthesis page. Cross-reference = find connections to existing pages. Evolve = generate higher-layer pages (lessons, patterns).

**Project Lifecycle (SFIF)** — scaffold → foundation → infrastructure → features
The project-level model. See [[Scaffold → Foundation → Infrastructure → Features]]. Runs at a macro level; other models run INSIDE its stages.

### Model Selection — How Conditions Pick a Model

Selection is not a lookup table — it's a multi-dimensional evaluation. Here's how it works in practice:

**The 5 condition dimensions:**

| Dimension | What it evaluates | How it affects selection |
|-----------|------------------|------------------------|
| **Task type** | What kind of work is this? | `spike` → Research model. `docs` → Documentation model. `module` → Feature Development model. |
| **Project phase** | Where is the project in its lifecycle? | Foundation phase → emphasize Document + Design. Features phase → emphasize Implement + Test. |
| **Domain** | What kind of system is this? | Code domain → Feature Development family. Knowledge domain → Ingestion Pipeline family. |
| **Scale** | How big is this change? | Single function → skip Document (context already known). New subsystem → full model + design review gate. |
| **Urgency/State** | How urgent? What's the current codebase state? | Critical production bug → Hotfix model. Legacy codebase at Mountain tier → Pyramid quality target. |

**Worked example — multi-dimensional selection:**

A user says: "Research how OpenArms does methodology enforcement."

Evaluating conditions:
- task_type = `research` (no code output expected)
- phase = Foundation (wiki is still building its knowledge base)
- domain = knowledge-systems (this is wiki research, not code)
- scale = single topic (one investigation)
- urgency = normal

Result: **Research model** (document → design). The agent reads OpenArms sources (document stage), produces a wiki page synthesizing findings (document artifact), then proposes design implications for the wiki's own methodology (design stage). Stops at 50% readiness. Does NOT scaffold, implement, or test anything.

**Another example — same task type, different conditions:**

A user says: "Build the backlog system for this wiki."

Evaluating conditions:
- task_type = `epic` (large initiative)
- phase = Infrastructure (wiki has its foundation, adding infrastructure)
- domain = tools-and-platforms (Python tooling)
- scale = new subsystem (schema, directories, pipeline, commands, MCP)
- urgency = normal

Result: **Feature Development model** (all 5 stages). Document → Design (brainstorm → spec) → Scaffold (schema changes, directory structure) → Implement (Python code, commands, MCP tools) → Test (pipeline health check). Each stage with its own commit, artifacts, and gate.

### Model Composition — How Models Chain, Nest, and Branch

Real work never runs one model in isolation. Four composition modes:

**Sequential:** Research model runs first, produces a spec. Feature Development model runs next, consuming the spec. The "Build the backlog system" example above ACTUALLY ran this way — first a research phase (reading OpenArms methodology), then a brainstorm/spec phase, then implementation.

**Nested:** SFIF runs at project level. Inside SFIF's Infrastructure stage, the backlog system epic ran the Feature Development model. Inside that epic, individual tasks ran subset models (task = scaffold+implement+test). Three levels of nesting, each with its own model.

**Conditional:** An agent picks up a backlog task. task_type=`bug` → Bug Fix model. task_type=`spike` → Research model. task_type=`module` → Feature Development model. The condition BRANCHES to completely different models, not different subsets of one pipeline.

**Parallel (multi-track):** Three tracks running simultaneously on THIS project RIGHT NOW:

| Track | Model | What it does | Artifacts |
|-------|-------|-------------|-----------|
| **Execution** | Brainstorm → Spec → Plan → Implementation | HOW things get built | Specs, plans, code, wiki pages |
| **PM** | Epics → Modules → Tasks with stage gates | WHAT gets tracked | Backlog entries, readiness scores |
| **Knowledge** | Ingest → Synthesize → Cross-Reference → Evolve | WHAT gets learned | Source pages, concept pages, lessons, patterns |

These interact but never merge: PM triggers execution, execution feeds knowledge, knowledge informs PM.

### Stage Boundaries — ALLOWED and FORBIDDEN

Stage names alone do not prevent violations. Each stage needs explicit ALLOWED and FORBIDDEN artifact lists. This was proven by OpenArms Bug 5: the agent produced 135 lines of business logic during the scaffold stage because nothing explicitly said "business logic is FORBIDDEN in scaffold."

**Scaffold:**
- ALLOWED: type definitions, static constants, schema objects, .env entries, empty test files with placeholder assertions
- FORBIDDEN: business logic (parsers, resolvers, evaluators), env var readers with parsing logic, functions beyond stub bodies, real test implementations

**Implement:**
- ALLOWED: business logic, helper functions, modifying existing files to import new code
- REQUIRED: at least one existing runtime file must import the new code (OpenArms Bug 6: 2,073 lines orphaned)
- FORBIDDEN: modifying test files, writing test assertions

**Test:**
- ALLOWED: fill scaffolded tests, add edge cases
- REQUIRED: 0 test failures before marking done
- FORBIDDEN: proceeding with failing tests

These lists are defined in `methodology.yaml` per stage. They adapt per domain — a wiki project's "implement" ALLOWED list includes "wiki pages, skills, commands" instead of "business logic functions."

### What Goes Wrong Without This — 7 Bugs From Real Operation

Every design decision in this model traces to a real failure. These 7 bugs were found during OpenArms' first day of autonomous agent operation (2026-04-09). Each bug led to a methodology version bump:

**Bug 1: Binary status.** Tasks were done/not-done. No stage tracking. Agent checked "Done When" boxes without verification and skipped from "active" to "done" after one stage.
→ **Design input:** Stage-level tracking with readiness percentages. `stages_completed` list. Every transition updates frontmatter and commits.

**Bug 2: Epic status manual.** Epics could be marked "done" with zero children complete.
→ **Design input:** Status/readiness computed from children. Max agent-settable = "review." Human confirms "done."

**Bug 3: Rogue task creation.** Agent ignored existing tasks and created its own, reusing IDs.
→ **Design input:** "Pick from existing tasks ONLY. Do NOT create new task files." Task creation is operator responsibility.

**Bug 4: Lost files.** Write tool succeeded but files vanished — destructive `git revert` killed untracked files.
→ **Design input:** "Commit immediately after creating files. Never destructive git without git status."

**Bug 5: Stage boundary violation.** Scaffold produced business logic. Test marked done with failures.
→ **Design input:** ALLOWED/FORBIDDEN lists per stage. Gate requires passing commands.

**Bug 6: Orphaned implementation.** 2,073 lines of code that nothing imported. Tests pass ≠ feature works.
→ **Design input:** Implement MUST wire into runtime. Done When must name the consumer file.

**Bug 7: Unreadable logs.** Raw JSON stream events. Impossible to monitor or report.
→ **Design input:** Observability tooling (agent-report.py). Cost per stage. Compliance checking.

**Methodology version history:** v1 (initial) → v2 (stage tracking) → v3 (hierarchy + no rogue tasks) → v4 (ALLOWED/FORBIDDEN) → v5 (integration requirement) → v6 (bridge pattern + compliance). Six versions in one day — each hardened by a real failure.

### Model Adaptation — Overrides Per Instance

Every model definition is a template. Every execution is an instance with potential overrides:

**Stage overrides:** Hotfix skips Document and Design. Security-sensitive work adds a Security Review stage. Research may run Design before Document.

**Artifact overrides:** Research produces wiki pages, not code. A small task needs only a summary, not a full gap analysis. Compliance-sensitive work adds a risk assessment at every stage.

**Readiness overrides:** Spike caps at 50%. POC caps at 80%. MVP targets 95%. Production targets 100%.

**Gate overrides:** Code projects: compilation + lint + tests. Wiki projects: validation + links + word count. Infrastructure: provisioning + health checks. Same gate STRUCTURE, domain-specific CONDITIONS.

**Protocol overrides:** OpenArms: one-commit-per-stage. OpenFleet: MCP tool blocking. This wiki: post-chain validation. Each project adapts enforcement to its tooling.

### The Quality Dimension

Every model instance has a quality target:

- **Skyscraper** — every stage runs, every artifact produced, every gate checked. For complex or high-stakes work.
- **Pyramid** — stages may be compressed, artifacts lighter, gates softer. Deviations are DELIBERATE and documented. For pragmatic delivery under constraints.
- **Mountain** — stages skipped accidentally, artifacts missing, gates ignored. The anti-pattern.

The framework mandates that quality level is an EXPLICIT choice per situation. A hotfix at Pyramid tier is a valid choice. Accidentally producing Mountain-tier work because you didn't choose is the failure mode.

See [[Skyscraper, Pyramid, Mountain]].

### How to Adopt

**What you need:**
1. `methodology.yaml` — defines your models (stages, task types, modes, end conditions). Start by copying from `wiki/config/methodology.yaml` and adapting.
2. `agent-directive.md` — defines the work loop, stage enforcement rules, git management, quality gates. Start by copying from `wiki/config/agent-directive.md` and adapting commands for your project.

**What is INVARIANT (never change):**
- Stage boundaries are hard (ALLOWED/FORBIDDEN enforced)
- Readiness derived from stage completion, not subjective assessment
- Backlog hierarchy: epic → module → task, readiness flows upward
- One commit per stage
- Models are DATA defined in config, not CODE

**What is PER-PROJECT (always adapt):**
- Which models exist and their stage sequences
- Per-stage artifact requirements (code vs wiki pages vs Terraform)
- Gate mechanisms (hooks vs CI vs manual review vs post-chain)
- Which task types exist
- Execution mode defaults and end conditions

**What goes wrong if you skip this:**
See the 7 bugs above. Every one was found within hours of starting autonomous agent operation. Without explicit methodology: binary status (Bug 1), unchecked epics (Bug 2), rogue tasks (Bug 3), lost files (Bug 4), stage violations (Bug 5), orphaned code (Bug 6), invisible work (Bug 7). The methodology exists because these failures HAPPENED.

### Real Example: End-to-End Task Execution

Here's how a single task flows through the methodology, from selection to completion:

**Task: "Tune the evolution scorer"** (from this wiki's actual history)

**Selection:** task_type=`task`, domain=tools, scale=focused change in one file. Conditions select the **Feature Development model**, subset for task type: scaffold → implement → test.

**Scaffold stage:**
- ALLOWED: modify the signal weights dict, add the `_GENERIC_TAGS` set, change the tag co-occurrence threshold
- FORBIDDEN: rewrite the scoring algorithm, add new signal functions
- Artifact: modified `SIGNAL_WEIGHTS` in evolve.py, added `_GENERIC_TAGS` filter
- Gate: `pipeline evolve --score` still runs without errors
- Commit: `feat(evolve): tune scorer weights and add generic tag filter`

**Implement stage:**
- ALLOWED: update the deduplication logic, change overlap thresholds
- REQUIRED: the scorer produces different output (verified by running `--score`)
- Artifact: rewritten `_deduplicate()` function with source overlap check
- Gate: `pipeline evolve --score --top 10` shows diverse candidates (not all tag-pair patterns)
- Commit: `feat(evolve): improve dedup — check source overlap with evolved pages`

**Test stage:**
- Run: `pipeline evolve --score --top 10` — verify diverse candidates
- Run: `pipeline post` — verify 0 validation errors
- Verify: candidates include convergence lessons, hub pages, open-question decisions (not just tag pairs)
- Commit: `feat: tune evolution scorer — better weights, dedup, and generic tag filter`

**Completion:** stages_completed=[scaffold, implement, test], readiness=100, status=done. Parent epic readiness recalculated from children.

### Relationship to Other Models

The Methodology model GOVERNS all other models in the wiki. Every other model operates WITHIN this framework:

- [[Model: LLM Wiki]] defines WHAT the wiki IS. This model defines HOW wiki work proceeds through stages.
- [[Model: Claude Code]] defines the agent's capabilities. This model defines how those capabilities are sequenced and gated.
- [[Model: Skills, Commands, and Hooks]] defines the tooling. This model defines WHEN each tool is permitted (per-stage protocols).
- [[Model: Ecosystem Architecture]] defines the project topology. This model defines how work flows through that topology.

This is not a peer relationship — it is governance. The Methodology model is the super-model.

## Open Questions

- Should model selection be encoded as a declarative config (condition → model lookup table) or evaluated dynamically? Currently it's implicit in task_type mapping. (Requires: testing a formal selection engine)
- Can stage gates be FULLY automated (no human in the loop) for certain model instances? OpenArms' autonomous agent run suggests yes for routine tasks but no for architectural decisions. (Requires: more autonomous operation data)
- What is the minimum viable methodology for a project that just wants stage tracking without the full framework? (Requires: a minimal adoption test)

## Relationships

- GOVERNS: [[Model: LLM Wiki]], [[Model: Claude Code]], [[Model: Ecosystem Architecture]], [[Model: Skills, Commands, and Hooks]], [[Model: Second Brain]]
- BUILDS ON: [[Methodology Framework]]
- BUILDS ON: [[Stage-Gate Methodology]]
- BUILDS ON: [[Task Type Artifact Matrix]]
- BUILDS ON: [[Backlog Hierarchy Rules]]
- BUILDS ON: [[Execution Modes and End Conditions]]
- BUILDS ON: [[Skyscraper, Pyramid, Mountain]]
- RELATES TO: [[Spec-Driven Development]]
- RELATES TO: [[Scaffold → Foundation → Infrastructure → Features]]
- RELATES TO: [[Adoption Guide — How to Use This Wiki's Standards]]
- IMPLEMENTS: wiki/config/methodology.yaml, wiki/config/agent-directive.md

## Backlinks

[[Model: LLM Wiki]]
[[Model: Claude Code]]
[[Model: Ecosystem Architecture]]
[[[[Model: Skills]]
[[Commands]]
[[and Hooks]]]]
[[Model: Second Brain]]
[[Methodology Framework]]
[[Stage-Gate Methodology]]
[[Task Type Artifact Matrix]]
[[Backlog Hierarchy Rules]]
[[Execution Modes and End Conditions]]
[[[[Skyscraper]]
[[Pyramid]]
[[Mountain]]]]
[[Spec-Driven Development]]
[[Scaffold → Foundation → Infrastructure → Features]]
[[Adoption Guide — How to Use This Wiki's Standards]]
[[wiki/config/methodology.yaml]]
[[wiki/config/agent-directive.md]]
[[Model: Skills, Commands, and Hooks]]

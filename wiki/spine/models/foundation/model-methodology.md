---
title: Model — Methodology
aliases:
  - "Model — Methodology"
  - "Model: Methodology"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-09
updated: 2026-04-13
sources:
  - id: src-openarms-methodology
    type: documentation
    file: raw/articles/openarms-methodology-yaml-full.md
    title: OpenArms Methodology YAML + Agent Directive
    ingested: 2026-04-09
  - id: src-openfleet-methodology-scan
    type: documentation
    file: raw/articles/openfleet-methodology-scan.md
    title: OpenFleet Methodology Deep Scan
    ingested: 2026-04-09
  - id: src-openarms-methodology-evolution
    type: documentation
    file: raw/articles/openarms-methodology-evolution-2026-04-09.md
    title: OpenArms Methodology Evolution — 7 Bugs, 6 Versions
    ingested: 2026-04-09
  - id: src-openarms-integration-sprint
    type: documentation
    file: raw/articles/openarms-integration-sprint-learnings.md
    title: OpenArms Integration Sprint Learnings
    ingested: 2026-04-09
tags: [methodology, model, stage-gate, task-types, composable, backlog, execution-modes, framework, spine, flexible, multi-track, multi-model]
---
# Model — Methodology
> [!tip] AI Quick Start — What You Do With This Page
>
> 1. **Determine your task type** (epic, module, task, bug, spike, docs, refactor, hotfix, integration, evolve)
> 2. **Find the model** in the Model Catalog section below — it tells you which stages apply
> 3. **Check ALLOWED/FORBIDDEN** per stage in the Stage Boundaries section — know what you CAN and CANNOT produce
> 4. **Check your domain chain** for concrete artifacts: [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]], [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]], [[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]], or [[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]
> 5. **Before declaring done**: run the Methodology Execution Checklist in [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Summary

The Methodology model defines a flexible FRAMEWORK for defining, selecting, composing, and adapting work processes. It is NOT one fixed pipeline — it is a system that CONTAINS multiple named methodology models (Feature Development, Research, Knowledge Evolution, Hotfix, Documentation, and more), selects between them based on conditions (task type, project phase, domain, scale, urgency), composes them (sequentially, nested, conditionally, in parallel), and adapts them per-instance through overrides. Three parallel tracks run on every project simultaneously: execution (how things get built), PM (what gets tracked), and knowledge (what gets learned). Where the [[model-llm-wiki|Model — LLM Wiki]] defines WHAT the wiki IS, this model defines HOW all work proceeds. The canonical definition lives in [[methodology-framework|Methodology Framework]]. The portable methodology engine lives in `wiki/config/methodology.yaml` (9 models with full artifact chains), `wiki/config/artifact-types.yaml` (17 page types with templates and thresholds), and `wiki/config/domain-profiles/` (TypeScript, Python/wiki, Infrastructure overrides). For the complete system map showing every component, see [[methodology-system-map|Methodology System Map]]. For adoption, see [[methodology-adoption-guide|Methodology Adoption Guide]]. For execution quality standards, see [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]].

## Key Insights

- **Multiple models, not one pipeline.** Feature Development has 5 stages. Research has 2. Knowledge Evolution has 4 with different stage names. Hotfix has 2. These are INDEPENDENT models, not subsets of one sequence. A project may use all of them at different times for different work.

- **Conditions select which model runs.** Task type is one condition. But also: project phase (Foundation emphasizes Document+Design; Features emphasizes Implement+Test), domain (code vs knowledge vs infrastructure), scale (single function vs new module), urgency (critical bug → Hotfix model), current state (greenfield vs legacy). Selection is multi-dimensional — all conditions evaluate simultaneously.

- **Models compose at every scale.** SFIF runs at project level. Inside each SFIF stage, task-level models run. Inside a task, stages execute. This is fractal — the same vocabulary (stages, gates, artifacts, readiness) at every level. Plus: three tracks run in PARALLEL on every project (execution, PM, knowledge) — not one sequence.

- **Stage boundaries are enforced, not suggested.** ALLOWED and FORBIDDEN artifact lists per stage. Document may not produce code. Scaffold may not implement business logic. Implement MUST wire into the runtime. This was learned from real failures — OpenArms Bug 5 (scaffold produced 135 lines of business logic) and Bug 6 (2,073 lines of orphaned code nobody imported).

- **The quality dimension is an explicit parameter.** Skyscraper (full process), Pyramid (deliberate compression), Mountain (accidental chaos). The choice is made per-situation, not accidentally.

- **The methodology was hardened by 7 real bugs in one day of autonomous operation.** Every design decision traces to a failure that proved it necessary. Cost dropped from $3.50/task (v1) to $1.32/task (v7) through iterative fixes. This is not theory — it is battle-tested from OpenArms' first autonomous agent run.

- **Enforcement must be infrastructure, not instructions.** Instructions achieve ~25% compliance for stage boundaries. Hooks achieve 100%. See [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]. But enforcement must be MINDFUL — every block needs a reason and a bypass. See [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]].

- **The Goldilocks principle governs methodology adoption.** Not every project needs every model, every stage, every artifact. The right process is a FUNCTION of identity (solo/harness/fleet), phase (POC→Production), scale (10k→15M), and PM level (L1→L3). See [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]].

- **Readiness and progress are TWO independent dimensions.** Readiness = definition completeness (left side of SDLC). Progress = execution completeness (right side). They advance in parallel and converge. 99→100 is human-only on BOTH. See [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]].

- **Three SDLC chains adapt the methodology to project context.** Simplified (POC, 2-3 stages, advisory enforcement), Default (MVP→Staging, all stages, hooks optional), Full (Production, all stages, full infrastructure enforcement). See [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]].

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

For the full structural definition, see [[methodology-framework|Methodology Framework]].

### The Model Catalog

Nine named methodology models. Each is a DIFFERENT stage sequence solving a different problem. Each entry shows: what it is, its stages with per-stage artifacts, when it's selected, and a real instance from the ecosystem.

---

#### Feature Development

> [!info] **Stages:** document → design → scaffold → implement → test
> The full 5-stage model for complex work. Used when the solution isn't already known and needs to be designed, scaffolded, built, and verified.

| Stage | What you produce | Gate |
|-------|-----------------|------|
| document | Wiki page mapping existing code + gap analysis | Page exists with Summary + gaps identified |
| design | Spec or design decision document, type sketches IN DOCS | Spec reviewed and approved |
| scaffold | Type definitions, schemas, .env entries, empty test files | Types compile, no business logic in diff |
| implement | Working code wired into runtime, wiki pages, skills | Code compiles, lint passes, ≥1 runtime file imports new code |
| test | All tests pass, manual verification | 0 test failures, health check clean |

> [!abstract] **Selected when**
> task_type = `epic`, `module`, or `refactor`. Any complex work where the solution isn't already known.

> [!example]- **Real instance: Building the wiki backlog system**
> 1. **Document** — Read OpenArms methodology model, understand what we need, map the gap between our wiki and OpenArms' backlog structure
> 2. **Design** — Brainstorm with user (5 design sections, each approved), spec written to `docs/superpowers/specs/`
> 3. **Scaffold** — Schema changes (4 new types, 7 new statuses, 5 new enums), directory structure (`wiki/backlog/`, `wiki/log/`, `wiki/config/`), methodology.yaml created
> 4. **Implement** — Python validation, pipeline `backlog` command, `/backlog` + `/log` slash commands, `wiki_backlog` + `wiki_log` MCP tools
> 5. **Test** — `pipeline chain health` clean, `pipeline backlog` shows 2 epics + 1 task, 0 validation errors

---

#### Research

> [!info] **Stages:** document → design
> Investigation without implementation. Produces understanding and options, never code. Capped at 50% readiness — 50% IS completion.

| Stage | What you produce | Gate |
|-------|-----------------|------|
| document | Wiki page synthesizing findings, source mapping | Page with Summary + Key Insights |
| design | Options document, decision recommendation, implications | Options presented to operator |

> [!abstract] **Selected when**
> task_type = `spike` or `research`. Investigation needed, no code output expected.

> [!example]- **Real instance: Researching second brain / PKM methodologies**
> 1. **Document** — Read Zettelkasten + PARA + hybrid approaches from web research. Created [[second-brain-architecture|Second Brain Architecture]] with full mapping of PARA buckets and Zettelkasten principles to wiki structure.
> 2. **Design** — Proposed how wiki maps to both methodologies. Identified 5 gaps: FAQs per domain, comparison matrices, review cadence, personal annotations, task management integration.

> [!tip] **Why it stops at design**
> Research produces UNDERSTANDING, not implementation. If the research leads to building something, that becomes a NEW task using a different model (Feature Development or Documentation). The research model's output becomes the next model's input — this is sequential composition.

---

#### Knowledge Evolution

> [!info] **Stages:** document → implement
> Generate higher-layer pages (lessons, patterns, decisions) from existing wiki knowledge. No scaffold or design — the "design" is the existing knowledge being distilled.

| Stage | What you produce | Gate |
|-------|-----------------|------|
| document | Cross-reference existing pages, identify convergence / insight | Candidate identified with source pages listed |
| implement | Complete evolved page (lesson, pattern, or decision) | Page passes validation, ≥0.25 ratio to sources, real evidence |

> [!abstract] **Selected when**
> task_type = `evolve`. Existing pages converge on an insight worth distilling.

> [!example]- **Real instance: Generating "CLI Tools Beat MCP for Token Efficiency" lesson**
> 1. **Document** — Cross-reference accuracy tips source, harness engineering source, Playwright comparison. Identify the convergence: three independent sources all say CLI beats MCP.
> 2. **Implement** — Write the 122-line lesson page with 8 evidence items from 4 independent sources. Each evidence item has a bold source label, a specific claim with data, and a sourcing parenthetical.

---

#### Documentation

> [!info] **Stages:** document
> Single-stage model. Done when the document is written and passes quality gates.

| Stage | What you produce | Gate |
|-------|-----------------|------|
| document | Wiki page, guide, spec, directive log entry | Passes quality gates (Summary ≥30 words, frontmatter valid) |

> [!abstract] **Selected when**
> task_type = `docs`. Writing or updating documentation only.

> [!example]- **Real instance: Logging an operator directive**
> User says something → create `wiki/log/` entry with verbatim quote + interpretation → validate frontmatter → commit. One stage, one artifact.

---

#### Bug Fix

> [!info] **Stages:** document → implement → test
> Restore correct behavior. No design stage — bug fixes should NOT introduce new architecture.

| Stage | What you produce | Gate |
|-------|-----------------|------|
| document | Understanding of what's broken and why | Root cause identified in writing |
| implement | The fix — code change, config change, or content correction | Fix applied, compiles/validates |
| test | Verification the fix works AND nothing else broke | Health check clean, regression-free |

> [!abstract] **Selected when**
> task_type = `bug`. Something is broken and needs to be restored to correct behavior.

> [!example]- **Real instance: Fixing the sync service startup**
> 1. **Document** — Sync daemon crashes on start. Root cause: `cmd.exe` not available in systemd environment, `get_win_user()` fails silently.
> 2. **Implement** — Add `WIKI_SYNC_TARGET` env var to service template, resolve at install time instead of runtime auto-detection.
> 3. **Test** — Reinstall service via `setup.py --services wiki-sync`, verify `systemctl --user status wiki-sync` shows active, verify files synced to Windows.

---

#### Refactor

> [!info] **Stages:** document → scaffold → implement → test
> Restructure without changing behavior. Skips design — the target structure is defined in the document stage.

| Stage | What you produce | Gate |
|-------|-----------------|------|
| document | Current structure mapped, target structure defined | Gap between current and target documented |
| scaffold | New directory structure, new type definitions, empty files | Structure exists, no logic moved yet |
| implement | Code/content moved into new structure | Everything compiles/validates in new structure |
| test | Behavior unchanged, all tests pass | Regression suite clean |

> [!abstract] **Selected when**
> task_type = `refactor`. Restructuring without changing behavior.

> [!example]- **Real instance: Renaming `config/schema.yaml` → `wiki/config/wiki-schema.yaml`**
> 1. **Document** — Identify all references: tools/pipeline.py, tools/validate.py, tools/common.py, CLAUDE.md
> 2. **Scaffold** — Create the new file name via `mv`
> 3. **Implement** — Update all references with sed, verify pipeline still finds the schema
> 4. **Test** — `pipeline post` passes, no broken imports, validation clean

---

#### Hotfix

> [!info] **Stages:** implement → test
> Emergency fix when the problem and solution are already understood. Skip all other stages.

| Stage | What you produce | Gate |
|-------|-----------------|------|
| implement | The fix | Applied and compiles/validates |
| test | Verification | Works and no regressions |

> [!warning] **Selected when**
> Urgency = critical AND the problem and solution are already understood. This is an EXPLICIT choice to operate at Pyramid tier — you're skipping stages knowingly, not accidentally.

> [!example]- **Real instance: Fixing the argparse `--top` / `--topic` prefix collision**
> The bug was immediately clear — argparse abbreviation matching consumed `--top` as `--topic`.
> 1. **Implement** — Add `allow_abbrev=False` to the ArgumentParser constructor
> 2. **Test** — Verify `--top 2` now scaffolds exactly 2 candidates, not 10
>
> Two commits, no documentation needed. The fix was obvious; the process was correctly compressed.

---

#### Ingestion Pipeline

> [!info] **Stages:** ingest → synthesize → cross-reference → evolve
> The knowledge track's model. **Completely different stage names** — this is NOT a subset of the 5-stage Feature Development model.

| Stage | What you produce | Gate |
|-------|-----------------|------|
| ingest | Raw file saved to raw/ | File exists in raw/articles/ or raw/transcripts/ |
| synthesize | Source-synthesis page in wiki/sources/ | Page ≥0.25 ratio to raw, passes validation |
| cross-reference | Updated relationships, new connections identified | pipeline crossref shows 0 missing backlinks |
| evolve | Higher-layer pages (lessons, patterns, decisions) | Evolved pages pass quality gates |

> [!abstract] **Selected when**
> domain = knowledge, operation = ingestion. Runs on the knowledge track.

> [!example]- **Real instance: Ingesting the context-mode repo**
> 1. **Ingest** — `pipeline fetch` saved 1,057-line README to `raw/articles/`
> 2. **Synthesize** — Read FULL source with multiple offsets. Created 254-line source-synthesis page covering all 12 platforms, FTS5/BM25 knowledge base, session continuity, benchmarks.
> 3. **Cross-reference** — Updated MCP vs CLI decision, CLI lesson, context-aware loading pattern with new evidence.
> 4. **Evolve** — Not triggered this cycle (synthesis was the primary output).

> [!warning] **Depth verification applies here**
> During the synthesize stage, you MUST read the actual THING, not just the description. The first attempt at context-mode produced a 60-line shallow page from the first chunk. The rewrite (after depth verification) produced a 254-line deep synthesis. See [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]].

---

#### Project Lifecycle (SFIF)

> [!info] **Stages:** scaffold → foundation → infrastructure → features
> The project-level MACRO model. Other models run INSIDE its stages. See [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]].

| Stage | What you produce | Gate |
|-------|-----------------|------|
| scaffold | Project structure, tech stack, AI config files | Directory exists, CLAUDE.md written, schema defined |
| foundation | Core modules, design system, build entry point | Single entry point works, architecture documented |
| infrastructure | Common components others depend on, basic interface | Build produces output, base is ready for features |
| features | Specialized product features | Features work end-to-end |

> [!abstract] **Selected when**
> scale = project. This runs at macro level; task-level models run inside.

> [!example]- **Real instance: This research wiki's own lifecycle**
> 1. **Scaffold** — CLAUDE.md, raw/, wiki/, tools/ directories, Python venv, tech stack chosen
> 2. **Foundation** — tools/common.py, wiki/config/wiki-schema.yaml, wiki/config/templates/, validation tooling
> 3. **Infrastructure** — tools/pipeline.py (13 chains), MCP server (17 tools), sync service, watcher daemon, evolve engine
> 4. **Features** — Evolution pipeline, backlog system, model-building skill, 14 named models, standards documents

> [!tip] **The recursive property**
> Inside the Infrastructure stage, building the backlog system ran the Feature Development model. Inside that, individual tasks ran their subset models. Three levels of nesting, each with its own methodology model. This is [[methodology-framework|Methodology Framework]]'s fractal property in practice.

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

> [!example]- **Worked example: "Research how OpenArms does methodology enforcement"**
> **Evaluating conditions:**
> | Dimension | Value | Why |
> |-----------|-------|-----|
> | task_type | `research` | No code output expected |
> | phase | Foundation | Wiki is still building its knowledge base |
> | domain | knowledge-systems | Wiki research, not code |
> | scale | single topic | One investigation |
> | urgency | normal | Not blocking anything |
>

> [!success] **Result → Research model** (document → design)
> The agent reads OpenArms sources (document stage), produces a wiki page synthesizing findings (document artifact), then proposes design implications for the wiki's own methodology (design stage). Stops at 50% readiness. Does NOT scaffold, implement, or test anything.

> [!example]- **Another example: "Build the backlog system for this wiki"**
> | Dimension | Value | Why |
> |-----------|-------|-----|
> | task_type | `epic` | Large initiative |
> | phase | Infrastructure | Wiki has its foundation, adding infra |
> | domain | tools-and-platforms | Python tooling |
> | scale | new subsystem | Schema, directories, pipeline, commands, MCP |
> | urgency | normal | Not a hotfix |
>
> [!success] **Result → Feature Development model** (all 5 stages)
> Document → Design (brainstorm → spec) → Scaffold (schema changes, directory structure) → Implement (Python code, commands, MCP tools) → Test (pipeline health check). Each stage with its own commit, artifacts, and gate.

### Model Composition — How Models Chain, Nest, and Branch

Real work never runs one model in isolation. Four composition modes:

> [!info] **Composition modes at a glance**
> | Mode | How it works | Example |
> |------|-------------|---------|
> | **Sequential** | One model's output feeds the next model's input | Research → Feature Development |
> | **Nested** | Models run inside other models' stages | SFIF → Feature Dev → task subsets |
> | **Conditional** | Conditions branch to completely different models | `bug` → Bug Fix, `spike` → Research |
> | **Parallel** | Multiple tracks run simultaneously | Execution + PM + Knowledge |

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

#### Scaffold

> [!success] **ALLOWED**
> Type definitions, static constants, schema objects, `.env` entries, empty test files with placeholder assertions.

> [!warning] **FORBIDDEN**
> Business logic (parsers, resolvers, evaluators), env var readers with parsing logic, functions beyond stub bodies, real test implementations.

#### Implement

> [!success] **ALLOWED**
> Business logic, helper functions, modifying existing files to import new code.

> [!tip] **REQUIRED**
> ==At least one existing runtime file must import the new code.== (OpenArms Bug 6: 2,073 lines orphaned because nothing imported them.)

> [!warning] **FORBIDDEN**
> Modifying test files, writing test assertions.

#### Test

> [!success] **ALLOWED**
> Fill scaffolded tests, add edge cases.

> [!tip] **REQUIRED**
> 0 test failures before marking done.

> [!warning] **FORBIDDEN**
> Proceeding with failing tests.

These lists are defined in `methodology.yaml` per stage. They adapt per domain — a wiki project's "implement" ALLOWED list includes "wiki pages, skills, commands" instead of "business logic functions."

### What Goes Wrong Without This — 7 Bugs From Real Operation

Every design decision in this model traces to a real failure. These 7 bugs were found during OpenArms' first day of autonomous agent operation (2026-04-09). Each bug led to a methodology version bump:

> [!bug]- **Bug 1: Binary status** → Design input: stage-level tracking (v2)
> Tasks were done/not-done. No stage tracking. Agent checked "Done When" boxes without verification and skipped from "active" to "done" after one stage.
> **Fix:** Added `task_type`, `current_stage`, `readiness`, `stages_completed` to frontmatter. Reset 22 tasks. 6 moved from "done" back to "in-progress."

> [!bug]- **Bug 2: Epic status manual** → Design input: computed hierarchy (v3)
> Epics could be marked "done" with zero children complete.
> **Fix:** Status/readiness computed from children. Max agent-settable = "review." Human confirms "done."

> [!bug]- **Bug 3: Rogue task creation** → Design input: operator-only task creation (v3)
> Agent ignored existing tasks and created its own, reusing IDs (T026-T029). Naming collisions and diverged backlog.
> **Fix:** "Pick from existing tasks ONLY. Do NOT create new task files." Task creation is operator responsibility.

> [!bug]- **Bug 4: Lost files** → Design input: commit immediately (v3)
> Write tool succeeded but files vanished — destructive `git revert` killed untracked files in shared workspace.
> **Fix:** "Commit immediately after creating files. Never destructive git without git status."

> [!bug]- **Bug 5: Stage boundary violation** → Design input: ALLOWED/FORBIDDEN (v4)
> Scaffold produced 135-line env reader with business logic. Test marked done with 1 failing test.
> **Fix:** Added explicit ALLOWED/FORBIDDEN lists per stage. Gate requires passing commands.

> [!bug]- **Bug 6: Orphaned implementation** → Design input: integration requirement (v5)
> 2,073 lines of production code — network rules, cost tracking, hook events. None imported by runtime. Tests pass ≠ feature works.
> **Fix:** Implement MUST wire into runtime. Done When must name the specific consumer file.

> [!bug]- **Bug 7: Unreadable logs** → Design input: observability tooling (v5)
> Raw JSON stream events (95% token chunks). Impossible to monitor live or produce reports.
> **Fix:** Built `agent-report.py` (stream aggregation, stage tracking, compliance checking, cost per stage).

> [!abstract] **Methodology version history**
> v1 (initial) → v2 (stage tracking) → v3 (hierarchy + no rogue tasks) → v4 (ALLOWED/FORBIDDEN) → v5 (integration requirement) → v6 (bridge pattern + compliance). **Six versions in one day** — each hardened by a real failure.

### Model Adaptation — Overrides Per Instance

Every model definition is a template. Every execution is an instance with potential overrides:

**Stage overrides:** Hotfix skips Document and Design. Security-sensitive work adds a Security Review stage. Research may run Design before Document.

**Artifact overrides:** Research produces wiki pages, not code. A small task needs only a summary, not a full gap analysis. Compliance-sensitive work adds a risk assessment at every stage.

**Readiness overrides:** Spike caps at 50%. POC caps at 80%. MVP targets 95%. Production targets 100%.

**Gate overrides:** Code projects: compilation + lint + tests. Wiki projects: validation + links + word count. Infrastructure: provisioning + health checks. Same gate STRUCTURE, domain-specific CONDITIONS.

**Protocol overrides:** OpenArms: one-commit-per-stage. OpenFleet: MCP tool blocking. This wiki: post-chain validation. Each project adapts enforcement to its tooling.

### The Quality Dimension

Every model instance has a quality target. The choice is EXPLICIT — made per-situation, never accidental.

> [!success] **Skyscraper** — the full process
> Every stage runs, every artifact produced, every gate checked. For complex or high-stakes work. This is the default expectation for epics and new subsystems.

> [!warning] **Pyramid** — deliberate compression
> Stages may be compressed, artifacts lighter, gates softer. Deviations are DELIBERATE and documented. For pragmatic delivery under constraints. A hotfix at Pyramid tier is a valid, honest choice.

> [!bug]- **Mountain** — accidental chaos (the anti-pattern)
> Stages skipped accidentally, artifacts missing, gates ignored. Not a choice — a failure mode. The difference between Pyramid and Mountain is INTENT: Pyramid documents why stages were skipped; Mountain doesn't notice they were skipped.

==The failure mode is not choosing Pyramid — it is accidentally producing Mountain-tier work because quality level was never an explicit decision.==

See [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]].

### How to Adopt

**Full guide:** [[methodology-adoption-guide|Methodology Adoption Guide]] — 4 tiers of adoption with per-domain quick starts.

> [!abstract] Adoption Tiers
>
> | Tier | What You Get | Effort |
> |------|-------------|--------|
> | **1. Read** | Read this page + standards pages, follow manually | Minutes |
> | **2. Configure** | Copy `wiki/config/methodology.yaml` + domain profile, reference in CLAUDE.md | Hours |
> | **3. Validate** | Add `wiki/config/artifact-types.yaml` checks to your validation pipeline | Days |
> | **4. Enforce** | Add hooks, stage skills, deterministic dispatch (see [[enforcement-hook-patterns|Enforcement Hook Patterns]]) | Weeks |

> [!info] **The Methodology Engine — config stack**
>
> | File | What It Defines |
> |------|----------------|
> | `wiki/config/methodology.yaml` | 9 models with artifact chains, execution modes, end conditions, quality tiers |
> | `wiki/config/artifact-types.yaml` | 17 page types with content thresholds, styling directives, verification methods |
> | `wiki/config/domain-profiles/*.yaml` | Per-domain overrides: path patterns, gate commands, forbidden zones (TypeScript, Python/wiki, Infrastructure) |
> | `wiki/config/templates/` | 16 wiki page templates + 6 methodology document templates |
> | `wiki/config/wiki-schema.yaml` | Frontmatter schema, required sections, relationship verbs |
>
> **Resolution order:** methodology.yaml (models) → artifact-types.yaml (type detail) → domain profile (project-specific)

> [!warning] **INVARIANTS — never change these**
> - Stage boundaries are hard (ALLOWED/FORBIDDEN enforced)
> - Readiness derived from stage completion, not subjective assessment
> - Backlog hierarchy: epic → module → task, readiness flows upward
> - One commit per stage
> - Models are DATA defined in config, not CODE
> - "Continue" = advance within current stage, NOT skip ahead

> [!tip] **PER-PROJECT — always adapt these**
> - Which models exist and their stage sequences
> - Per-stage artifact requirements (resolved by domain profile)
> - Gate commands (pnpm tsgo for TypeScript, pipeline post for wiki, terraform validate for IaC)
> - Execution mode defaults and end conditions
> - Enforcement depth (Tier 1-4 per [[methodology-adoption-guide|Methodology Adoption Guide]])

See also: [[model-composition-rules|Model Composition Rules]] for how models combine, [[methodology-evolution-protocol|Methodology Evolution Protocol]] for how the methodology evolves, [[artifact-chains-by-model|Artifact Chains by Methodology Model]] for full per-model artifact chains.

> [!bug]- **What goes wrong if you skip this**
> See the 7 bugs above. Every one was found within hours of starting autonomous agent operation. Without explicit methodology: binary status (Bug 1), unchecked epics (Bug 2), rogue tasks (Bug 3), lost files (Bug 4), stage violations (Bug 5), orphaned code (Bug 6), invisible work (Bug 7). The methodology exists because these failures HAPPENED.

### Agent Compliance — The Enforcement Hierarchy

Agents ignore methodology due to confusion, broadness, and poor instruction formatting. Five levels of enforcement address this, each with measured compliance data:

> [!abstract] Enforcement Hierarchy (quantified)
>
> | Level | Mechanism | Measured Compliance | Key Pages |
> |-------|-----------|-------------------|-----------|
> | 1. Instructions | CLAUDE.md prose rules | 25% (OpenArms v4-v8) | [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]] |
> | 2. Structured instructions | ALLOWED/FORBIDDEN tables, numbered rules | ~60% | Same page — 8 patterns documented |
> | 3. Hooks | PreToolUse/PostToolUse shell scripts | 100% stage boundaries (OpenArms v10) | [[enforcement-hook-patterns|Enforcement Hook Patterns]] |
> | 4. Commands + harness | Agent calls /stage-complete, harness validates | 100% workflow (OpenArms v10) | [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]] |
> | 5. Immune system | 3-line defense: prevent → detect → correct | Production-tested (OpenFleet) | [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]] |

**Critical insight:** Even with 100% stage boundary compliance (Level 3+), behavioral failures persist. Clean completion rate = 20% (4 of 5 OpenArms runs needed manual fixes). The remaining 6 failure classes are about JUDGMENT, not process: weakest-checker optimization, environment patching without escalation, fatigue cliff, sub-agent non-compliance, silent conflict resolution, artifact pollution. See [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]].

**Mindful enforcement:** Every block must explain WHY and offer justified bypass. Blind enforcement creates its own failures — an agent's correct fix was reverted twice because it looked like scope creep. See [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]].

**Structured context as proto-programming:** Markdown IS the programming language of AI agents. Consistent structure across injections (frontmatter, MUST/MUST NOT, stage protocols) creates patterns agents follow mechanically. See [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]].

Supporting systems:

- **[[stage-aware-skill-injection|Stage-Aware Skill Injection]]** — Which skills are recommended, mandatory, or blocked per stage. Prevents wrong-phase skill usage.
- **[[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]** — All corrections lost after compaction. Post-compact hooks rebuild state.
- **[[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]** — Cross-agent inputs required before work starts. Prevents rework.
- **[[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]** — Trust earned through data. Context depth adapts per tier.

### Artifact Taxonomy — The Full Spectrum

The real-world SDLC has 78+ distinct artifact types across 11 categories. Our methodology models produce a SUBSET based on the model and domain. The complete taxonomy and per-domain chains are documented separately:

> [!info] Artifact System
>
> | Resource | What It Covers |
> |----------|---------------|
> | [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]] | All 78 types across 11 categories — the complete reference |
> | [[methodology-artifact-taxonomy-research|Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research]] | Online research behind the taxonomy (10 sources) |
> | [[initiation-and-planning-artifacts|Initiation and Planning Artifacts — Standards and Guide]] | Pre-methodology: charters, WBS, risk, planning |
> | [[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]] | Document + Design stages: specs, ADRs, test plans |
> | [[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]] | Scaffold + Implement + Test: per-domain variations |
> | [[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]] | Post-implementation: operations, lessons, compliance |
> | [[ai-agent-artifacts|AI Agent Artifacts — Standards and Guide]] | Agent-specific: personas, skills, hooks, compliance |

> [!info] Per-Domain Artifact Chains
>
> | Domain | Chain Page |
> |--------|-----------|
> | TypeScript/Node | [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]] — 24-artifact chain from OpenArms |
> | Python/Wiki | [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]] — pipeline-based, config scaffolding |
> | Infrastructure/IaC | [[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]] — Terraform stages, drift detection |
> | Knowledge/Evolution | [[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]] — L0-L6 progressive distillation |

### SDLC Customization — Phase × Scale × Chain

The methodology models define WHAT stages a task goes through. But HOW MUCH process wraps around those stages depends on the project's phase and scale:

> [!info] Process Weight Selection
>
> | Dimension | Values | Impact |
> |-----------|--------|--------|
> | **Project phase** | POC → MVP → Staging → Production | POC: short loops, minimal docs. Production: full traceability. |
> | **Codebase scale** | 10k → 100k → 1M → 5M → 15M | 10k: one person holds context. 1M+: full SDLC governance. |
> | **Chain type** | Simplified, Middle Ground (default), Full | Simplified: 2-3 stages. Full: all 5 stages + complete artifacts. |
>
> See [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]] for the full decision matrix with recommended chain by phase × scale.

### Readiness vs Progress — Two-Dimensional Tracking

Work tracking requires TWO independent fields: `readiness` (is this DEFINED enough to start?) and `progress` (how far is the EXECUTION?). These are the left and right sides of the SDLC.

> [!info] Two Dimensions at Every Level
>
> | Level | Readiness = | Progress = | Gate |
> |-------|------------|-----------|------|
> | Milestone | All epics defined, scope clear | All epics progressing | Target date |
> | Epic | Requirements + design complete | Modules/tasks completing | Acceptance criteria |
> | Module | Design done, tasks decomposed | Tasks completing | All children done → review |
> | Task | Done When specific, contributions received | Stages completing, artifacts produced | 99→100 = human |
>
> See [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] for full model with OpenFleet evidence.

### Three PM Levels

The methodology operates within a PM infrastructure that may be L1 (wiki only), L2 (fleet/harness), or L3 (full PM tool). Each level wraps the previous and adds enforcement + observability. See [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] for the architecture and harness version mapping (v1→v2→v3).

> [!warning] Corrected Execution Mode Semantics
> Execution mode (solo, harness-v1, harness-v2, harness-v3, full-system) is a RUNTIME property — the harness decides its own version at startup based on what infrastructure exists, not what the project declares. A project does not "have" harness v2; it has infrastructure that ENABLES harness v2. The version is discovered, not configured. This distinction prevents projects from claiming capabilities they haven't built.

### Real Example: End-to-End Task Execution

Here's how a single task flows through the methodology, from selection to completion.

> [!info] **Task: "Tune the evolution scorer"** (from this wiki's actual history)
> task_type=`task`, domain=tools, scale=focused change in one file. Conditions select the **Feature Development model**, subset for task scale: scaffold → implement → test.

> [!example]- **Scaffold stage**
> | | |
> |---|---|
> | **ALLOWED** | Modify the signal weights dict, add the `_GENERIC_TAGS` set, change the tag co-occurrence threshold |
> | **FORBIDDEN** | Rewrite the scoring algorithm, add new signal functions |
> | **Artifact** | Modified `SIGNAL_WEIGHTS` in evolve.py, added `_GENERIC_TAGS` filter |
> | **Gate** | `pipeline evolve --score` still runs without errors |
> | **Commit** | `feat(evolve): tune scorer weights and add generic tag filter` |

> [!example]- **Implement stage**
> | | |
> |---|---|
> | **ALLOWED** | Update the deduplication logic, change overlap thresholds |
> | **REQUIRED** | The scorer produces different output (verified by running `--score`) |
> | **Artifact** | Rewritten `_deduplicate()` function with source overlap check |
> | **Gate** | `pipeline evolve --score --top 10` shows diverse candidates (not all tag-pair patterns) |
> | **Commit** | `feat(evolve): improve dedup — check source overlap with evolved pages` |

> [!example]- **Test stage**
> | | |
> |---|---|
> | **Run** | `pipeline evolve --score --top 10` — verify diverse candidates |
> | **Run** | `pipeline post` — verify 0 validation errors |
> | **Verify** | Candidates include convergence lessons, hub pages, open-question decisions (not just tag pairs) |
> | **Commit** | `feat: tune evolution scorer — better weights, dedup, and generic tag filter` |

> [!success] **Completion**
> `stages_completed=[scaffold, implement, test]`, `readiness=100`, `status=done`. Parent epic readiness recalculated from children.

### Battle-Tested Through Operation — Not Theory

> [!success] OpenArms Methodology Evolution: 7 Bugs, 7 Versions, 1 Day
>
> The first autonomous agent session (2026-04-09) found 7 systemic bugs and evolved the methodology through v1→v7 in 10 hours:
>
> | Bug | Version Fixed | Discovery | Impact |
> |-----|--------------|-----------|--------|
> | No stage tracking | v2 | Tasks "done" after 1 stage | Agent skipped stages |
> | Epic readiness not computed | v3 | All epics stuck on "draft" | Dashboard lies |
> | Agent creates rogue tasks | v3 | Colliding IDs (T026-T029) | Backlog corruption |
> | Files lost to git revert | v3 | Files disappeared between creation and commit | Silent data loss |
> | Stage boundaries violated | v4 | Scaffold produced 135 lines of business logic | Wrong artifacts per stage |
> | Code orphaned from runtime | v5 | 2,073 lines not imported by anything | Wasted effort, false completion |
> | Logs unreadable | v5 | Raw JSON stream | No observability |
>
> **Cost efficiency improved with each version:** v1-v2: $3.50/task. v5-v7: $1.32/task. The 62% cost reduction came from methodology fixes, not code optimizations.
>
> **Self-hosting feedback loop:** run agent → observe behavior → fix methodology → run again. 20 minutes per iteration average. 10 cycles in one session. Compressed months of theoretical methodology development into hours of operational testing.
>
> **Fix persistence:** Every fix held across ALL subsequent runs. Zero regressions. The methodology is stable not because it was well-designed initially, but because it was stress-tested by real operation.
>
> This validates Principle 1 ([[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]): each bug was first "fixed" with a directive rule. Only when the fix became infrastructure (schema enforcement, hooks, harness commands) did it HOLD.

### Relationship to Other Models

> [!abstract] **Governance, not peer relationship**
> The Methodology model GOVERNS all other models in the wiki. Every other model operates WITHIN this framework. This is the super-model.

| Model | What it defines | How Methodology governs it |
|-------|----------------|---------------------------|
| [[model-llm-wiki|Model — LLM Wiki]] | WHAT the wiki IS | HOW wiki work proceeds through stages |
| [[model-claude-code|Model — Claude Code]] | The agent's capabilities | How those capabilities are sequenced and gated |
| [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] | The tooling | WHEN each tool is permitted (per-stage protocols) |
| [[model-ecosystem|Model — Ecosystem Architecture]] | The project topology | How work flows through that topology |

### How This All Weaves Together — Navigation from This Page

This page is ONE thread in a woven system. Here's how to navigate from here to ANY part of the framework:

> [!abstract] From Methodology → Everywhere
>
> | You Want To Know... | Go To |
> |---------------------|-------|
> | **"What am I? What level of process do I need?"** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — 7 identity questions that determine your chain, enforcement, and context depth |
> | **"How much process is right for MY project?"** | [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]] — phase (POC→Production) × scale (10k→15M) × chain (simplified/default/full) |
> | **"How do I track readiness AND progress?"** | [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] — definition completeness vs execution completeness, two independent dimensions |
> | **"What PM infrastructure do I need?"** | [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] — L1 (Wiki), L2 (Fleet/Harness), L3 (Full PM). Each wraps the previous. |
> | **"How do I make agents ACTUALLY follow this?"** | [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]] → [[enforcement-hook-patterns|Enforcement Hook Patterns]] → [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]] |
> | **"What fails even after enforcement works?"** | [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] — 7 behavioral failures that persist after 100% stage compliance |
> | **"What does the full artifact chain look like?"** | [[artifact-chains-by-model|Artifact Chains by Methodology Model]] + domain chains: [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]], [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]], [[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]] |
> | **"How do I organize my work?"** | [[backlog-hierarchy-rules|Backlog Hierarchy Rules]] — Milestone → Epic → Module → Task, 8 impediment types, when to use what: [[when-to-use-milestone-vs-epic-vs-module-vs-task|Decision — When to Use Milestone vs Epic vs Module vs Task]] |
> | **"What fields do my pages need?"** | [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]] — every field, what it means, what automation it enables |
> | **"Where does this project fit in the ecosystem?"** | [[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]] — bidirectional flow, framework over instance, constant evolution |
> | **"What global standards should I follow?"** | CloudEvents for events, OpenAPI for APIs, SFIF for build lifecycle, DDD for domains, Onion for layer isolation, SRP for responsibilities |
> | **"How do I adopt this for my project?"** | [[methodology-adoption-guide|Methodology Adoption Guide]] — 4 tiers (Read→Configure→Validate→Enforce) + SDLC chain selection + per-domain quick starts |
> | **"Show me the complete system map"** | [[methodology-system-map|Methodology System Map]] — every component, where it lives, what it does, how they connect |

> [!tip] The Core Weave
>
> **Identity** (who am I?) → **Selection** (what methodology/chain/enforcement?) → **Execution** (stages, artifacts, gates) → **Tracking** (readiness + progress, hierarchy, impediments) → **Enforcement** (hooks, harness, immune system) → **Evolution** (lessons feed back, patterns emerge, decisions refine) → **Identity** (evolved understanding feeds the next cycle).
>
> This is not a linear path — it's a LOOP. Every execution produces learnings that evolve the methodology that changes the selection criteria. The Goldilocks point shifts as the project matures. The framework adapts because it's designed to adapt.

### Lessons Learned (from building and operating this model)

| Lesson | What Was Learned | Evidence |
|--------|-----------------|---------|
| [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]] | Instructions=25%, hooks=100% for stage boundaries | OpenArms v8 (75% violations) → v10 (0% violations) |
| [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] | 7 behavioral failures persist after 100% stage enforcement | 4/5 runs need manual fixes. 20% clean rate. |
| [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]] | Over-enforcement blocks correct work (T086 fnm fix reverted) | Every block needs WHY + bypass mechanism |
| [[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently Across Projects]] | 3 independent projects → same conclusion: agent must not own loop | OpenArms, OpenFleet, harness engineering article |
| [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] | All behavioral corrections lost after compaction | Post-compact hook (29 lines) rebuilds from files |
| [[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]] | Copying values ≠ building framework. Phase 1: 37 files of "crap" | Portability test: can another project adopt without rewriting? |
| [[follow-the-method-of-work-not-the-methodology-label|Follow the Method of Work Not the Methodology Label]] | "Follow methodology" ≠ "enter Document stage" | Explicit 5-step method broke the research-produce loop |
| [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]] | Structure governs behavior more than content | Same rules: prose=25%, tables=60%. Structure > content. |
| [[the-wiki-is-a-hub-not-a-silo|The Wiki Is a Hub, Not a Silo]] | The wiki aggregates from projects AND feeds back to them | 22 OpenArms lessons + OpenFleet architecture fed back the 2026-04-12 session |

### State of Knowledge

> [!success] **Well-covered (quantified evidence from multiple projects)**
> - 9 named models with stage sequences, artifact chains, and template references (methodology.yaml, 517 lines)
> - Stage boundaries hardened by 7 real bugs from OpenArms autonomous operation (v1→v7, $3.50→$1.32/task)
> - Enforcement hierarchy quantified: instructions=25%, structured=60%, hooks=100% (OpenArms v10, 5 production runs)
> - 7 behavioral failure classes persisting after infrastructure enforcement (20% clean completion rate)
> - 3 SDLC chains defined as YAML configs (simplified, default, full) backed by CMMI + Lean Startup research
> - Goldilocks identity protocol with 7 dimensions, auto-detection for 2 of them
> - Readiness vs progress as two independent fields, OpenFleet implementation evidence
> - 3 PM levels (solo, harness, full system) with corrected execution mode semantics
> - Methodology battle-tested: 10 observe-fix-verify cycles in first session, fix persistence verified
> - 3 principles distilled: Infrastructure Over Instructions, Structured Context, Goldilocks Imperative

> [!warning] **Thin or unverified**
> - Model composition in practice — documented but only 1 worked example (wiki's own methodology initiative)
> - SDLC chain adoption — configs exist but no project has adopted from them yet (E016 will prove this)
> - Context engineering — scattered across lessons, not formalized as its own model (E017)
> - Formal model selection engine — Goldilocks protocol recommends but no automated selection tool
> - Cross-project methodology comparison — OpenArms vs OpenFleet stage names differ, not formally reconciled
> - Model evolution protocol — how models version when updated (methodology.yaml has no version field)

## Open Questions

> [!question] ~~**Should model selection be declarative or dynamic?**~~
> **RESOLVED:** Declarative in frontmatter (task_type field), with the methodology engine selecting the model. Dynamic selection by the agent would bypass the methodology.
> **Partially resolved.** The Goldilocks protocol suggests declarative: identity profile → chain → model. OpenFleet implements this: `methodology.yaml` defines models, orchestrator selects based on task type + readiness + contributions. OpenArms is more implicit (task_type mapping in harness). The wiki should support BOTH: declarative config for known mappings, dynamic override for edge cases. (Remaining: test a formal selection engine that reads identity profiles)

> [!question] ~~****Can stage gates be fully automated?****~~
> **RESOLVED:** Mechanical gates yes (schema, type checking, tests). Judgment gates no (design quality, requirement completeness). Full enforcement = both.
> **Partially resolved.** OpenArms v10: 100% stage compliance via hooks. Stage GATES are fully automatable. Stage QUALITY is not — 7 behavioral failures persist at 80% rate. The boundary: anything checkable at the tool-call level (did you write to src/ during document?) = automate. Anything requiring judgment (is this requirements spec good enough?) = human gate. See [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] for the full boundary analysis.

> [!question] ~~****What is the minimum viable methodology?****~~
> **RESOLVED:** The simplified chain. One gate (pipeline post), advisory stages, operator as reviewer. Everything else is progressive addition.
> **Resolved via Goldilocks.** Depends on identity profile: Solo + POC + micro = simplified chain (2 models: Feature Dev + Hotfix, CLAUDE.md rules only, 2-3 stages). Solo + MVP + medium = default chain (5 models, hooks + commands, 3-5 stages). Fleet + Production + large = full chain (all 9 models, harness + immune system, all 5 stages + all artifacts). See [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] for the complete selection matrix.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Quality standards for methodology** | [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]] |
> | **Super-model (all models)** | [[super-model|Super-Model]] |
> | **System map (find anything)** | [[methodology-system-map|Methodology System Map]] |
> | **SDLC chain selection** | [[sdlc-customization-framework|SDLC Customization Framework]] |
> | **Domain chains** | [[domain-chain-typescript|TypeScript]], [[domain-chain-python-wiki|Python-Wiki]], [[domain-chain-infrastructure|Infrastructure]], [[domain-chain-knowledge|Knowledge]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |
> | **Adoption guide** | [[methodology-adoption-guide|Methodology Adoption Guide]] |

## Relationships

- GOVERNS: [[model-llm-wiki|Model — LLM Wiki]], [[model-claude-code|Model — Claude Code]], [[model-ecosystem|Model — Ecosystem Architecture]], [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]], [[model-second-brain|Model — Second Brain]]
- BUILDS ON: [[methodology-framework|Methodology Framework]]
- BUILDS ON: [[stage-gate-methodology|Stage-Gate Methodology]]
- BUILDS ON: [[task-type-artifact-matrix|Task Type Artifact Matrix]]
- BUILDS ON: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- BUILDS ON: [[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
- BUILDS ON: [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
- CONTAINS: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- CONTAINS: [[model-composition-rules|Model Composition Rules]]
- CONTAINS: [[methodology-adoption-guide|Methodology Adoption Guide]]
- CONTAINS: [[methodology-evolution-protocol|Methodology Evolution Protocol]]
- CONTAINS: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
- CONTAINS: [[enforcement-hook-patterns|Enforcement Hook Patterns]]
- CONTAINS: [[stage-aware-skill-injection|Stage-Aware Skill Injection]]
- RELATES TO: [[spec-driven-development|Spec-Driven Development]]
- RELATES TO: [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
- RELATES TO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-llm-wiki|Model — LLM Wiki]]
[[model-claude-code|Model — Claude Code]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-second-brain|Model — Second Brain]]
[[methodology-framework|Methodology Framework]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
[[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[model-composition-rules|Model Composition Rules]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[methodology-evolution-protocol|Methodology Evolution Protocol]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[stage-aware-skill-injection|Stage-Aware Skill Injection]]
[[spec-driven-development|Spec-Driven Development]]
[[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[ai-agent-artifacts|AI Agent Artifacts — Standards and Guide]]
[[identity-profile|AICP — Identity Profile]]
[[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
[[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]
[[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
[[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
[[E003-artifact-type-system|Artifact Type System]]
[[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
[[artifact-system-design-decisions|Decision — Artifact System Design Decisions]]
[[methodology-stage-extension-decisions|Decision — Methodology Stage Extension Decisions]]
[[when-to-use-milestone-vs-epic-vs-module-vs-task|Decision — When to Use Milestone vs Epic vs Module vs Task]]
[[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
[[e003-artifact-type-system-requirements|E003 Artifact Type System — Requirements Spec]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[epic-page-standards|Epic Page Standards]]
[[methodology-evolution-history|Evolution — Methodology System]]
[[follow-the-method-of-work-not-the-methodology-label|Follow the Method of Work Not the Methodology Label]]
[[goldilocks-flow|Goldilocks Flow — From Identity to Action]]
[[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]]
[[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]
[[initiation-and-planning-artifacts|Initiation and Planning Artifacts — Standards and Guide]]
[[methodology-fundamentals|Learning Path — Methodology Fundamentals]]
[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[methodology-config-architecture|Methodology Config Architecture — How the Pieces Fit Together]]
[[2026-04-09-directive-methodology-is-flexible-not-fixed|Methodology Is Flexible — Multiple Chains, Not One Fixed Pipeline]]
[[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
[[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
[[methodology-system-map|Methodology System Map]]
[[model-registry|Model Registry]]
[[model-knowledge-evolution|Model — Knowledge Evolution]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[model-sfif-architecture|Model — SFIF and Architecture]]
[[model-wiki-design|Model — Wiki Design]]
[[note-page-standards|Note Page Standards]]
[[identity-profile|OpenArms — Identity Profile]]
[[identity-profile|OpenFleet — Identity Profile]]
[[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]]
[[operator-decision-queue|Operator Decision Queue]]
[[E004-portable-methodology-engine|Portable Methodology Engine]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]]
[[research-gaps|Research Gaps — Empirical Questions Requiring Data]]
[[identity-profile|Research Wiki — Identity Profile]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[sdlc-rules-and-structure-customizable-project-lifecycle|SDLC Rules and Structure — Customizable Project Lifecycle]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[2026-04-09-session-summary|Session 2026-04-09 Summary]]
[[2026-04-10-session-summary|Session 2026-04-10 Summary]]
[[standards-must-preach-by-example|Standards Must Preach by Example]]
[[methodology-artifact-taxonomy-research|Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research]]
[[src-sdlc-frameworks-research|Synthesis — SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC]]
[[three-classes-of-methodology-output|Three Classes of Methodology Output]]
[[universal-stages-domain-specific-artifacts|Universal Stages, Domain-Specific Artifacts]]
[[model-wiki-design-standards|Wiki Design Standards — What Good Styling Looks Like]]
[[identity-profile|devops-control-plane — Identity Profile]]

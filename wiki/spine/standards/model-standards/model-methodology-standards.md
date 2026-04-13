---
title: "Methodology Standards — What Good Execution Looks Like"
aliases:
  - "Methodology Standards — What Good Execution Looks Like"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-11
sources:
  - id: src-openarms-methodology-evolution
    type: documentation
    file: raw/articles/openarms-methodology-evolution-2026-04-09.md
    title: "OpenArms Methodology Evolution — 7 Bugs, 6 Versions"
    ingested: 2026-04-09
tags: [methodology, standards, quality, stage-gate, execution, gold-standard, anti-patterns]
---

# Methodology Standards — What Good Execution Looks Like

> [!tip] AI Quick Start — What You Do With This Page
>
> 1. **Before completing any stage**: scroll to "The Methodology Execution Checklist" — run it
> 2. **If producing artifacts**: check "Per-Type Artifact Standards" for your artifact's quality bar
> 3. **If unsure about quality tier**: read "Gold Standard: Quality Tier Selection" — Pyramid is valid if deliberate
> 4. **If something feels wrong**: check the "Anti-Pattern Gallery" — your situation may be a known failure mode
> 5. **For the full artifact spectrum**: follow links to per-category guides and domain chains in "Beyond Wiki Pages"

## Summary

This page defines the quality bar for METHODOLOGY EXECUTION. Where [[model-methodology|Model — Methodology]] defines the system (9 models, 5 condition dimensions, 4 composition modes, stage boundaries), this page shows what it looks like when that system is followed WELL — and what it looks like when it fails. ==Every gold standard on this page is a real instance from this wiki or the OpenArms ecosystem.== No hypotheticals. The methodology was hardened by real bugs; the standards are demonstrated by real successes.

## Key Insights

- **Good execution is visible in the artifacts, not the claims.** A well-run stage sequence leaves a trail: wiki page at document, spec at design, schema at scaffold, working code at implement, clean health check at test. If someone says "I'm at 80% readiness" but there's no spec, the claim is false.

- **The right model for the job is rarely the biggest model.** Feature Development has 5 stages. Most real work uses 2-3 stage subsets. Defaulting to the full 5-stage model for everything is the methodology equivalent of using a sledgehammer for every nail.

- **Honest quality tier selection IS the standard, not Skyscraper.** A hotfix at Pyramid tier with documented reasoning is BETTER methodology than a feature built at Mountain tier by an agent that thinks it's running Skyscraper. The standard is intentionality, not perfection.

- **The gap between documenting methodology and following it is the most dangerous failure mode.** A system that describes perfect stage gates while skipping stages is worse than a system with no documented methodology — because the documentation creates false confidence.

## Deep Analysis

### Gold Standard: Stage-Gate Execution

What a properly run 5-stage sequence looks like end-to-end.

> [!info] **Reference: Building the wiki backlog system** (Feature Development model)
> The most complete stage-gate instance in this wiki's history. Every stage produced its required artifacts, every gate was passed, every transition was explicit.

> [!example]- **Stage 1 — Document** (readiness: 0→25%)
> **What happened:** Read OpenArms methodology YAML (253 lines), OpenFleet methodology scan (798 lines), OpenArms integration sprint learnings. Created wiki pages mapping the gap between our wiki's flat task tracking and OpenArms' stage-gated backlog.
>
> **Artifacts produced:**
> - Wiki pages: [[methodology-framework|Methodology Framework]], [[stage-gate-methodology|Stage-Gate Methodology]], [[task-type-artifact-matrix|Task Type Artifact Matrix]]
> - Gap analysis: wiki has no task types, no stage tracking, no readiness computation
>
> **Gate:** Pages exist with Summary + gaps identified. ✅ Passed.
>
> **What makes this good:** The document stage produced UNDERSTANDING, not code. Three wiki pages existed before any implementation was discussed. The gap analysis named specific missing features, not vague "needs improvement."

> [!example]- **Stage 2 — Design** (readiness: 25→50%)
> **What happened:** Brainstormed with the user — 5 design sections, each presented and approved separately. Options evaluated: flat vs hierarchical backlog, computed vs manual readiness, agent-settable vs human-gated status transitions.
>
> **Artifacts produced:**
> - Spec in `docs/superpowers/specs/`
> - Decision: hierarchical backlog (epic → module → task), computed readiness, max agent-settable = "review"
>
> **Gate:** Spec reviewed and approved by operator. ✅ Passed.
>
> **What makes this good:** The user approved each design section BEFORE the next was presented. No batching. No "here's the whole design, approve it." Incremental validation caught issues early — the user rejected the first readiness computation proposal and we iterated.

> [!example]- **Stage 3 — Scaffold** (readiness: 50→80%)
> **What happened:** Schema changes only. No logic.
>
> **Artifacts produced:**
> - 4 new types in `wiki-schema.yaml`: epic, module, task, note
> - 7 new statuses: draft, active, in-progress, review, done, archived, blocked
> - 5 new enums: priority, task_type, stage, estimate, note_type
> - Directory structure: `wiki/backlog/epics/`, `wiki/backlog/modules/`, `wiki/backlog/tasks/`
> - `wiki/config/methodology.yaml` (253 lines) — the stage definitions
>
> **Gate:** Types compile (schema validates), ==no business logic in the diff==. ✅ Passed.
>
> **What makes this good:** The diff contained ONLY schema, config, and empty directories. Zero Python logic. Zero business rules. The methodology.yaml file defines stages — it does not implement them. This is the scaffold stage doing what scaffold means.

> [!example]- **Stage 4 — Implement** (readiness: 80→95%)
> **What happened:** Built on the scaffold. Python validation for new types, pipeline `backlog` command, slash commands, MCP tools.
>
> **Artifacts produced:**
> - `tools/validate.py` updates (backlog field validation)
> - `tools/pipeline.py` updates (`backlog` command with `run_backlog()`)
> - `/backlog` + `/log` slash commands
> - `wiki_backlog` + `wiki_log` MCP tools in `tools/mcp_server.py`
>
> **Gate:** Code compiles, lint passes, ==≥1 runtime file imports new code==. ✅ Passed.
>
> **What makes this good:** Every new function was imported by an existing runtime file. The pipeline's `backlog` command calls `run_backlog()`. The MCP server calls `wiki_backlog()`. Nothing was orphaned. This is the lesson from OpenArms Bug 6 — 2,073 lines of code nobody imported.

> [!example]- **Stage 5 — Test** (readiness: 95→100%)
> **What happened:** Full health check, manual verification of generated output.
>
> **Verification:**
> - `pipeline chain health` — clean ✅
> - `pipeline backlog` — shows 2 epics + 1 task ✅
> - `pipeline post` — 0 validation errors ✅
> - Manual: backlog items have correct frontmatter, readiness computes from children ✅
>
> **What makes this good:** Test was a SEPARATE stage from implement. The health check ran AFTER implementation was committed. If tests had failed, the fix would have been in the test stage — not a retroactive patch to the implement commit.

> [!tip] **The pattern to replicate**
> Each stage has: what happened (narrative), artifacts produced (concrete list), gate (pass/fail), and what makes it good (the quality signal). If any of these four are missing, the stage wasn't properly executed — it was performed but not verified.

---

### Gold Standard: Model Selection

What thoughtful multi-dimensional selection looks like vs reflexive defaulting.

> [!success] **Good selection: "Tune the evolution scorer"**
> | Dimension | Value | Reasoning |
> |-----------|-------|-----------|
> | task_type | `task` | Atomic work unit, not an epic |
> | phase | Features | Wiki infrastructure exists, adding capability |
> | domain | tools | Python tooling, not wiki content |
> | scale | focused | One file (`evolve.py`), one subsystem |
> | urgency | normal | Not blocking anything |
>
> **Result → Feature Development subset:** scaffold → implement → test (skip document + design because the scorer already exists and the changes are scoped).
>
> This is correct because: the full context is already known (no document stage needed), the approach is already decided (no design stage needed), but the change needs structure (scaffold weights before implementing dedup). The 3-stage subset is the MINIMUM sufficient model.

> [!bug]- **Bad selection: defaulting to Feature Dev for everything**
> When the agent was asked to "process this content into wiki pages," it selected the Feature Development model and began writing a spec. The task was actually `docs` type — single-stage Documentation model. The result: unnecessary design overhead for a task that needed zero design.
>
> **The signal:** if the model selection takes more effort than the task itself, the wrong model was selected. A Documentation task should be recognized in seconds: "Is this producing knowledge artifacts only, no code? → Documentation model."
>
> **The fix:** evaluate task_type FIRST. Most tasks have an obvious type. Only evaluate the other 4 dimensions when the type is ambiguous.

---

### Gold Standard: Quality Tier Selection

The standard is HONEST selection, not always choosing Skyscraper.

> [!success] **Good Pyramid: the argparse `--top`/`--topic` collision hotfix**
> The bug was immediately clear — argparse abbreviation matching consumed `--top` as `--topic`. The root cause was known. The fix was one line: `allow_abbrev=False`.
>
> **Quality tier chosen:** Pyramid (Hotfix model — implement → test, skip document + design + scaffold).
>
> **Why this is GOOD methodology:**
> - The compression was DELIBERATE — the agent explicitly chose Hotfix, not accidentally skipped stages
> - The reasoning was documented — "the fix was obvious; the process was correctly compressed"
> - Two commits, clean test — no trailing debt
>
> A Skyscraper approach to this fix (document the argparse behavior, design alternative fixes, scaffold a test, implement, test) would have been methodology theater — applying process where process adds no value.

> [!bug]- **Bad Mountain: batch-produced model pages**
> 14 model pages were batch-produced in one pass. Each was 80-110 lines. Each was a reading list, not a system definition. The agent claimed "models are ready." The user's response: "So you lied again... nothing is ready... I dont even see 2% of it..."
>
> **Quality tier that was operating:** Mountain — stages skipped accidentally, artifacts shallow, gates not checked.
>
> **Why this is BAD methodology:**
> - No deliberate tier selection — the agent didn't CHOOSE Pyramid, it accidentally produced Mountain
> - False readiness claim — "models are ready" without checking the quality gates
> - The agent confused structure (pages exist) with substance (pages define systems)
>
> See [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]] for the full failure analysis.

> [!warning] **The diagnostic question**
> "Did you CHOOSE this quality tier, or did it happen to you?" If you can't articulate WHY you're at Pyramid instead of Skyscraper, you're at Mountain.

---

### Gold Standard: Stage Boundary Enforcement

What proper ALLOWED/FORBIDDEN adherence looks like.

> [!success] **Good enforcement: scorer tuning scaffold stage**
> The scaffold stage for tuning the evolution scorer allowed: modifying signal weights, adding the `_GENERIC_TAGS` filter set, changing the tag co-occurrence threshold. It FORBADE: rewriting the scoring algorithm, adding new signal functions.
>
> The actual diff contained ONLY: a modified `SIGNAL_WEIGHTS` dict and a new `_GENERIC_TAGS` set. No algorithm changes. No new functions. The boundary held.
>
> **Why this matters:** The boundary prevented scope creep. The natural temptation during "tune the scorer" is to also improve the scoring algorithm. The FORBIDDEN list says: not in this stage. Improvement is a different task with its own model selection.

> [!bug]- **Bad enforcement: OpenArms Bug 5 — scaffold with business logic**
> The scaffold stage produced a 135-line environment reader with full business logic — parsing, validation, default handling. The `scaffold` stage had no FORBIDDEN list. Nothing explicitly said "business logic is not allowed here."
>
> **The lesson:** stage NAMES do not prevent violations. Explicit ALLOWED/FORBIDDEN lists do. "Scaffold" sounds like it means "structure only," but without the explicit list, the agent's definition of "structure" expanded to include everything.
>
> This bug created the ALLOWED/FORBIDDEN system (methodology v4). Every stage boundary in the wiki's `methodology.yaml` now has explicit protocol rules.

---

### Gold Standard: Composition in Practice

What real multi-model composition looks like when it runs well.

> [!info] **Three-track parallel composition on this wiki**
> | Track | Running model | Current state | Artifacts the 2026-04-12 session |
> |-------|--------------|---------------|----------------------|
> | **Execution** | Brainstorm → Spec → Plan → Implement | Active — building models, applying styling | Specs, model pages, standards pages, skills |
> | **PM** | Epics → Modules → Tasks | Active — 2 epics, backlog system operational | Backlog entries, readiness scores |
> | **Knowledge** | Ingest → Synthesize → Cross-ref → Evolve | Active — 167 pages, ~1,175 relationships | Source pages, concept pages, 6 lessons, 6 patterns |
>
> These three tracks ran SIMULTANEOUSLY throughout the session. While the execution track was building the backlog system (Feature Dev model), the knowledge track was ingesting OpenArms methodology (Ingestion model), and the PM track was tracking the backlog items being created. The tracks interact — PM triggers execution tasks, execution produces knowledge artifacts, knowledge informs PM priorities — but they never merge into one sequence.

> [!example]- **Nested composition: SFIF → Feature Dev → task subsets**
> At the project level, the wiki traversed SFIF stages:
> 1. **SFIF Scaffold** — CLAUDE.md, directory structure, tech stack
> 2. **SFIF Foundation** — tools/common.py, schema, validation
> 3. **SFIF Infrastructure** — pipeline.py, MCP server, sync service
>    - Inside Infrastructure, the backlog system ran **Feature Development** (5 stages)
>      - Inside Feature Dev, individual schema changes ran **task-level subsets** (scaffold → implement → test)
> 4. **SFIF Features** — Evolution pipeline, model-building skill, standards documents
>
> Three nesting levels. Each with its own methodology model. The SFIF model governed the project. Feature Dev governed the epic. Task subsets governed the atomic work. Same vocabulary (stages, gates, artifacts, readiness) at every level.

---

### Gold Standard: methodology.yaml

What a well-written methodology config looks like.

> [!info] **Reference: `wiki/config/methodology.yaml`** (253 lines)
> This wiki's own methodology config. What makes it the standard:
>
> | Quality signal | What it demonstrates |
> |---------------|---------------------|
> | **5 stages with explicit readiness ranges** | `document: [0, 25]`, `design: [25, 50]`, etc. — readiness is COMPUTED, not subjective |
> | **Protocol per stage** | Each stage has a `protocol:` block listing DO and DO NOT rules |
> | **8 task types with explicit stage lists** | `epic: [document, design, scaffold, implement, test]`, `research: [document, design]` — the stages aren't optional, they're the task type's DEFINITION |
> | **8 execution modes** | From `autonomous` (no stops) to `custom` (per-run override) — the agent's autonomy level is configurable |
> | **5 end conditions** | `backlog-empty`, `stage-reached`, `time-limit`, `cost-limit`, `task-count` — the agent knows WHEN to stop |
> | **Defaults section** | `mode: autonomous`, `end_condition: backlog-empty` — explicit defaults, not implicit assumptions |

> [!warning] **Anti-pattern: thin methodology.yaml**
> A config with only stage names and no protocols, no readiness ranges, no task type mappings. Stage names alone don't prevent violations (OpenArms Bug 5). A methodology config must be prescriptive enough that an agent reading only the config — not the wiki pages, not the lessons — knows what it's allowed to do at each stage.

---

### Anti-Pattern Gallery

Methodology failures from real operation, each traced to a specific lesson.

> [!bug]- **Stage skipping: "continue" misinterpreted as "skip ahead"**
> The user said "you have everything to get started." The agent interpreted this as permission to skip brainstorm and jump to writing a spec. The user's response: "WTF ???? WHAT SPEC ??? WTF ???????"
>
> **Root cause:** Bias toward perceived progress. Writing a spec FEELS like forward movement. Processing content into wiki pages feels like "still doing prep work."
>
> **The rule:** "Continue" = advance within current stage. "Get started" = begin current stage. Only "skip to X" authorizes stage-skipping. See [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]].

> [!bug]- **False readiness: "models are ready" at scaffold level**
> 14 model pages existed as 80-110 line reading lists. The agent claimed they were complete. The user: "I dont even see 2% of it..."
>
> **Root cause:** Confusing structure (pages exist) with substance (pages define systems). The SFIF framework names this explicitly: scaffold ≠ foundation ≠ infrastructure ≠ features.
>
> **The rule:** Readiness is derived from stage completion, not from artifact count. 14 scaffolded pages = 14 × scaffold readiness (50%), not 14 × done (100%). See [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]].

> [!bug]- **Practice vs document gap: documenting rules you don't follow**
> The wiki had pages about stage gates, brainstorm-before-spec, depth verification. The agent had written all of them. The agent violated all of them. The wiki described methodology perfectly while the agent ignored it.
>
> **Root cause:** Methodology existed in wiki pages (knowledge the agent produced) but not in CLAUDE.md (instructions the agent follows). The agent could describe the rules but didn't apply them.
>
> **The rule:** When the wiki evolves a methodology rule, that rule must be propagated to CLAUDE.md. Knowledge must become operational. See [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]].

> [!bug]- **Binary status: done/not-done without stage tracking**
> OpenArms Bug 1. Tasks were either "active" or "done." The agent checked "Done When" boxes without verification and skipped stages.
>
> **Root cause:** No stage-level visibility. Without `current_stage`, `stages_completed`, and `readiness`, there's no way to distinguish "completed document stage" from "completed everything."
>
> **The fix:** Added stage tracking to frontmatter. Reset 22 tasks. 6 moved from "done" back to "in-progress."

> [!bug]- **Orphaned implementation: code nobody imports**
> OpenArms Bug 6. 2,073 lines of production code — network rules, cost tracking, hook events. None imported by any runtime file. Tests pass ≠ feature works.
>
> **Root cause:** No integration requirement at the implement stage. "Code exists" was treated as "code works."
>
> **The fix:** Implement stage MUST wire into runtime. "Done When" must name the specific consumer file that imports the new code.

---

### Gold Standard: Artifact Chain Execution

What proper artifact production across a full epic looks like — using the artifact type system.

> [!info] **Reference: E003 Artifact Type System** — 5 stages, 22 artifacts, all acceptance criteria verified
>
> | Stage | Artifacts Produced | Template Used | Gate |
> |-------|--------------------|---------------|------|
> | **Document** | Infrastructure analysis, Gap analysis, Requirements spec | methodology/infrastructure-analysis, methodology/gap-analysis, methodology/requirements-spec | Wiki pages exist, no code |
> | **Design** | Design document with 7 decisions | methodology/design-plan | Design doc exists, decisions have rationale |
> | **Scaffold** | artifact-types.yaml, 16 templates, schema update, scaffolder update | (config files + templates) | Pipeline post passes, no logic in configs |
> | **Implement** | methodology.yaml (9 models), 3 domain profiles, artifact chains wiki page, validate.py extension | (code + config + wiki) | Pipeline post 0 errors, validation catches type thresholds |
> | **Test** | AC-1 through AC-10 verified with commands | (verification output) | All 10 acceptance criteria pass |
>
> **What makes this the standard:**
> - Every stage used the correct methodology template for its artifacts
> - Artifact dependencies were respected: design depended on document artifacts, scaffold depended on design
> - The full chain is defined in `wiki/config/methodology.yaml` under `feature-development.chain`
> - Domain profile (`python-wiki`) resolved gate commands to `pipeline post`

**The bar:** Every methodology model has a defined artifact chain in `wiki/config/methodology.yaml`. Every stage in that chain specifies required, optional, and forbidden artifacts. Domain profiles in `wiki/config/domain-profiles/` resolve generic artifact types to concrete paths and gate commands. See [[artifact-chains-by-model|Artifact Chains by Methodology Model]] for all 9 model chains.

---

### Gold Standard: CLAUDE.md Structure

What a methodology-compliant CLAUDE.md looks like — using the 8 structural patterns.

> [!info] **Reference: This wiki's CLAUDE.md** — restructured 2026-04-11 using all 8 patterns
>
> | Pattern | How It's Applied |
> |---------|-----------------|
> | Sacrosanct section | Operator directives at line 8, verbatim quotes, non-negotiable |
> | Hard vs soft separation | Two explicit tables with different headers |
> | ALLOWED/FORBIDDEN | Per-stage table: Document/Design/Scaffold/Implement/Test columns |
> | Progressive disclosure | Identity → Hard rules → Models → Structure → Quality → Tooling |
> | Command checkpoints | `pipeline post` as the universal verification command |
> | Section dividers | `# -----------` between every major section |
> | Anchor phrases | "Continue means current stage" repeated in hard rules AND stage table |
> | Concrete examples | Exact pipeline commands, exact scaffold syntax |

**The bar:** A CLAUDE.md that uses ≥5 of the 8 patterns from [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]. At minimum: sacrosanct section, hard/soft separation, ALLOWED/FORBIDDEN per stage.

---

### Gold Standard: Operations Plan vs Design Plan

What the distinction looks like in practice — two fundamentally different documents.

> [!abstract] The Critical Distinction
>
> | Dimension | Operations Plan | Design Plan |
> |-----------|----------------|-------------|
> | Template | `wiki/config/templates/operations-plan.md` | `wiki/config/templates/methodology/design-plan.md` |
> | Wiki type | `operations-plan` (new type) | `concept` (with methodology template) |
> | Structure | Sequential steps with Action/Expected/Validation/Rollback | Decisions with rationale + rejected alternatives |
> | Judgment | None — mechanical, delegatable to any agent | High — trade-offs, alternatives, evidence |
> | Example | [[wiki-post-ingestion-operations-plan|Operations Plan — Wiki Post-Ingestion Validation]] | [[e003-artifact-type-system-design|E003 Artifact Type System — Design Document]] |

**The bar:** If someone asks "what's the plan?", determine which kind first. Operations plan = "do these steps in order." Design plan = "here are the options, here's what we chose and why." Using one when the other is needed is a methodology failure.

---

### Gold Standard: Enforcement Infrastructure

What a project with methodology enforcement looks like — from Tier 1 (read) to Tier 4 (full enforcement).

> [!info] **Reference: [[methodology-adoption-guide|Methodology Adoption Guide]] — 4 tiers of adoption**
>
> | Tier | What You Get | Evidence It Works |
> |------|-------------|-------------------|
> | 1. Read | Models + standards pages | Manual compliance, variable |
> | 2. Configure | methodology.yaml + domain profile in CLAUDE.md | ALLOWED/FORBIDDEN tables visible, ~50-60% compliance |
> | 3. Validate | artifact-types.yaml checked by validation pipeline | Post-hoc detection of violations |
> | 4. Enforce | Hooks + harness + deterministic dispatch | ~90% compliance (OpenArms v9 evidence) |

**The bar:** Know your tier. Document it. A project at Tier 2 that claims Tier 4 compliance is at Mountain quality tier. See [[enforcement-hook-patterns|Enforcement Hook Patterns]] for Tier 4 infrastructure and [[stage-aware-skill-injection|Stage-Aware Skill Injection]] for skill-level enforcement.

---

### The Methodology Engine

The complete machine-readable system for methodology execution.

> [!info] **The Methodology Config Stack**
>
> | Config File | What It Defines | Lines |
> |-------------|----------------|-------|
> | `wiki/config/methodology.yaml` | 9 models with artifact chains, modes, end conditions, quality tiers | ~400 |
> | `wiki/config/artifact-types.yaml` | 17 page types with thresholds, styling, verification methods | ~280 |
> | `wiki/config/domain-profiles/*.yaml` | Per-domain overrides: paths, gates, forbidden zones (3 profiles) | ~60 each |
> | `wiki/config/wiki-schema.yaml` | Frontmatter schema, required sections, relationship verbs | ~240 |
> | `wiki/config/quality-standards.yaml` | Linting thresholds, export readiness, duplicate detection | ~20 |
> | `wiki/config/templates/` | 16 wiki page templates + 6 methodology document templates | 22 files |
>
> **Resolution order:** methodology.yaml (models) → artifact-types.yaml (type detail) → domain profile (project-specific) → wiki-schema.yaml (structural validation)

**The bar:** A project that has adopted the methodology should have: methodology.yaml (generic or project-override), a declared domain profile, and CLAUDE.md referencing both. See [[methodology-evolution-protocol|Methodology Evolution Protocol]] for how the wiki updates propagate to consumers.

---

### Per-Type Artifact Standards

Every page type produced during methodology execution has its own standards doc in `wiki/spine/standards/`. These define what good artifacts look like at each stage:

> [!info] Methodology-Relevant Per-Type Standards
>
> | Produced During | Type | Standards Doc |
> |----------------|------|--------------|
> | Document stage | concept (for requirements, infra analysis, gap analysis) | [[concept-page-standards|Concept Page Standards]] |
> | Document stage | source-synthesis (for ingested sources) | [[source-synthesis-page-standards|Source-Synthesis Page Standards]] |
> | Design stage | decision (for ADRs) | [[decision-page-standards|Decision Page Standards]] |
> | Design stage | reference (for tech specs, test plans) | [[reference-page-standards|Reference Page Standards]] |
> | Implement stage | operations-plan (for sequential execution checklists) | [[operations-plan-page-standards|Operations Plan Page Standards]] |
> | Any stage | note (for directive logs, session logs) | [[note-page-standards|Note Page Standards]] |
> | Evolution | lesson, pattern, decision | [[lesson-page-standards|Lesson Page Standards]], [[pattern-page-standards|Pattern Page Standards]], [[decision-page-standards|Decision Page Standards]] |
> | PM track | epic, task | [[epic-page-standards|Epic Page Standards]], [[task-page-standards|Task Page Standards]] |
>
> **Full list:** See [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] for all 15 types.

**The bar:** Every artifact produced at every stage should meet its type's standards. An agent producing a requirements spec (concept type) during document stage should consult [[concept-page-standards|Concept Page Standards]] for the quality bar. A lesson being evolved should meet [[lesson-page-standards|Lesson Page Standards]].

### Beyond Wiki Pages — The Full Artifact Spectrum

The per-type standards above cover wiki page types. But methodology execution produces artifacts BEYOND wiki pages — code files, test results, deployment packages, compliance reports. The full taxonomy of 78 artifact types across 11 categories is documented in:

> [!info] Complete Artifact Research
>
> | Resource | What It Covers |
> |----------|---------------|
> | [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]] | All 78 types: initiation, planning, requirements, design, construction, testing, deployment, closure, monitoring, knowledge, AI agent |
> | [[initiation-and-planning-artifacts|Initiation and Planning Artifacts — Standards and Guide]] | Charters, WBS, risk analysis — BEFORE methodology starts |
> | [[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]] | BRD/FRD/SRS, ADR variants, tech specs, interface specs, test plans |
> | [[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]] | Per-domain scaffold/implement/test with ALLOWED/FORBIDDEN |
> | [[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]] | Operations guides, lessons learned, compliance reports |
> | [[ai-agent-artifacts|AI Agent Artifacts — Standards and Guide]] | Personas, skills, hooks, stage skills, compliance reports |
>
> Per-domain chains: [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]], [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]], [[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]], [[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]

---

### The Methodology Execution Checklist

> [!tip] **Run this at every stage transition**
> - [ ] Current stage's required artifacts exist and are committed
> - [ ] Gate condition for current stage is met (not just "feels done")
> - [ ] Readiness percentage matches stages completed (not claimed)
> - [ ] No FORBIDDEN artifacts appear in the diff for the current stage
> - [ ] The model was selected by evaluating conditions, not defaulted
> - [ ] Quality tier was explicitly chosen (Skyscraper/Pyramid), not accidentally Mountain
> - [ ] If methodology rules were learned during this task, they're propagated to CLAUDE.md
> - [ ] Frontmatter reflects actual state: `current_stage`, `stages_completed`, `readiness`

> [!tip] **Run this at task completion**
> - [ ] All required stages for this task type were executed (check `methodology.yaml`)
> - [ ] `pipeline post` passes with 0 validation errors
> - [ ] Readiness = 100% (or capped at the task type's maximum — research caps at 50%)
> - [ ] Parent epic/module readiness recomputed from children
> - [ ] One commit per stage (check git log)

## Open Questions

> [!question] **Can methodology compliance be measured automatically?**
> A compliance checker could: verify one-commit-per-stage in git log, check that FORBIDDEN artifacts don't appear in stage diffs, verify readiness matches stages_completed. OpenArms built `agent-report.py` for this. Should the wiki have an equivalent? (Requires: defining measurable compliance signals)

> [!question] **What's the failure rate of stage-gate enforcement in practice?**
> OpenArms found 7 bugs in one day. This wiki had 3+ methodology violations in one session. Is this the expected learning curve, or does it indicate the enforcement mechanisms are insufficient? (Requires: tracking violations over multiple sessions)

> [!question] **Should there be a "methodology health" score per project?**
> A composite metric: % of tasks with proper stage tracking, % of commits with stage labels, % of epics with computed readiness, # of FORBIDDEN violations. Would this be useful or bureaucratic? (Requires: implementing the metric and testing whether it drives behavior)

### Annotated Exemplar

> [!example] Real example: [[model-methodology|Model — Methodology]] — why this page is exemplary
>
> **What makes this page meet the standard:**
>
> 1. **9 named models with concrete stages and ALLOWED/FORBIDDEN lists** — Each model (Feature Development, Research, Knowledge Evolution, Documentation, Bug Fix, Refactor, Hotfix, Ingestion Pipeline, Project Lifecycle) is defined with its own stage sequence, per-stage artifact table, selection conditions in a `[!abstract]` callout, and a foldable `[!example]-` real instance. The ALLOWED/FORBIDDEN section for scaffold, implement, and test stages uses `[!success]`, `[!warning]`, and `[!tip] REQUIRED` callouts to make boundaries unambiguous. This is a FRAMEWORK, not a description.
> 2. **Model composition modes with real parallel tracks** — The page defines four composition modes (sequential, nested, conditional, parallel) and demonstrates parallel composition with a three-track table showing execution, PM, and knowledge tracks running simultaneously on this wiki. The nested composition example traces three levels of nesting (SFIF at project level, Feature Dev at epic level, task subsets at atomic level) — showing the fractal property in practice, not just naming it.
> 3. **Battle-tested evidence with quantified costs** — The 7 bugs section uses `[!bug]-` foldable callouts, each naming the bug, the design input it produced, and the methodology version bump it triggered. The methodology version history (v1 through v6 in one day) shows the system hardening under real pressure. Cost data ($3.50/task at v1 to $1.32/task at v7) provides economic evidence that the methodology WORKS, not just that it EXISTS.
> 4. **AI Quick Start block at the top** — The `[!tip] AI Quick Start` callout gives an agent 5 numbered steps to USE this page immediately: determine task type, find the model, check ALLOWED/FORBIDDEN, check domain chain, run the execution checklist. This transforms a 600-line reference page into an operational tool — the agent reads 5 lines and knows what to do, then dives deeper only as needed.
>
> **What could still improve:** The page exceeds 600 lines, which makes it harder to maintain and increases the chance of internal inconsistencies. The Model Adaptation section (overrides per instance) is shorter than it should be given the complexity of real override scenarios. The enforcement hierarchy section partially duplicates content from [[model-quality-failure-prevention|Model — Quality and Failure Prevention]].

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Principles** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] · [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] · [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **Identity** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- BUILDS ON: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- BUILDS ON: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
- BUILDS ON: [[enforcement-hook-patterns|Enforcement Hook Patterns]]
- BUILDS ON: [[stage-aware-skill-injection|Stage-Aware Skill Injection]]
- RELATES TO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- RELATES TO: [[methodology-evolution-protocol|Methodology Evolution Protocol]]
- RELATES TO: [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]
- RELATES TO: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
- RELATES TO: [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]

## Backlinks

[[model-methodology|Model — Methodology]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[stage-aware-skill-injection|Stage-Aware Skill Injection]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[methodology-evolution-protocol|Methodology Evolution Protocol]]
[[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
[[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]]
[[comparison-page-standards|Comparison Page Standards]]
[[concept-page-standards|Concept Page Standards]]
[[coverage-blindness-modeling-only-what-you-know|Coverage Blindness — Modeling Only What You Know]]
[[decision-page-standards|Decision Page Standards]]
[[artifact-system-design-decisions|Decision — Artifact System Design Decisions]]
[[deep-dive-page-standards|Deep-Dive Page Standards]]
[[domain-overview-page-standards|Domain Overview Page Standards]]
[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[epic-page-standards|Epic Page Standards]]
[[evolution-page-standards|Evolution Page Standards]]
[[model-knowledge-evolution-standards|Evolution Standards — What Good Knowledge Promotion Looks Like]]
[[methodology-evolution-history|Evolution — Methodology System]]
[[model-skills-commands-hooks-standards|Extension Standards — What Good Skills, Commands, and Hooks Look Like]]
[[follow-the-method-of-work-not-the-methodology-label|Follow the Method of Work Not the Methodology Label]]
[[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]
[[learning-path-page-standards|Learning Path Page Standards]]
[[lesson-page-standards|Lesson Page Standards]]
[[methodology-config-architecture|Methodology Config Architecture — How the Pieces Fit Together]]
[[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
[[methodology-system-map|Methodology System Map]]
[[model-composition-rules|Model Composition Rules]]
[[note-page-standards|Note Page Standards]]
[[operations-plan-page-standards|Operations Plan Page Standards]]
[[pattern-page-standards|Pattern Page Standards]]
[[model-quality-failure-prevention-standards|Quality Standards — What Good Failure Prevention Looks Like]]
[[reference-page-standards|Reference Page Standards]]
[[source-synthesis-page-standards|Source-Synthesis Page Standards]]
[[E006-standards-by-example|Standards-by-Example]]
[[task-page-standards|Task Page Standards]]
[[three-classes-of-methodology-output|Three Classes of Methodology Output]]
[[universal-stages-domain-specific-artifacts|Universal Stages, Domain-Specific Artifacts]]
[[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]]

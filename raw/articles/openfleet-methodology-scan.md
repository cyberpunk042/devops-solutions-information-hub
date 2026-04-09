# OpenFleet Methodology Scan — Deep Research Findings

**Date:** 2026-04-09
**Researcher:** Claude Code (research agent, devops-solutions-research-wiki)
**Source project:** `/home/jfortin/openfleet/`
**Purpose:** Complete structural scan of OpenFleet's methodology, document types,
artifact standards, workflow patterns, and cross-document relationships.

---

## 1. Project Overview

OpenFleet is an **autonomous AI agent workforce** — 10 specialized agents managed
through OpenClaw gateway and Mission Control (OCMC). Its core architecture:

- **Fleet** (openfleet): agent operations, MCP tools, orchestrator, infrastructure
- **AICP** (devops-expert-local-ai): AI Control Platform, LocalAI independence
- **DSPD** (devops-solution-product-development): project management via Plane
- **NNRT** (Narrative-to-Neutral-Report-Transformer): report transformation NLP

The fleet operates as a 3-layer surface system:
1. **Plane (DSPD):** project management (PO + PM agent)
2. **OCMC (Mission Control):** agent operations (fleet agents)
3. **GitHub + IRC + ntfy:** code + communications (agent execution outputs)

---

## 2. Documentation Architecture — Three Layers

OpenFleet uses a deliberate 3-layer documentation system. This is explicit in CLAUDE.md:

### Layer 1: Wiki (LLM-friendly, planning-first)

Located at `wiki/`. Karpathy-style YAML-frontmatter wiki:
- `wiki/backlog/_index.md` — 17 epics (E001-E017), modules, tasks
- `wiki/log/` — PO directives verbatim, chronological, sacrosanct
- `wiki/domains/` — knowledge pages by domain
- Feeds cross-project second brain at `../devops-solutions-research-wiki`

### Layer 2: Docs (front-facing, architecture and systems)

Located at `docs/`. Hierarchical by function:
- `docs/README.md` — master navigation index for ~100 docs, 5-layer hierarchy
- `docs/ARCHITECTURE.md` — 20 systems, interconnection matrix
- `docs/INTEGRATION.md` — 12 cross-system data flows
- `docs/SPEC-TO-CODE.md` — 69 specs mapped to 94 modules (living doc)
- `docs/systems/01-22` — per-system reference (22 files, ~10,283 lines)
- `docs/milestones/` — planning, tracking, standards, vision

### Layer 3: Code Docs (inner, collocated with code)

Module docstrings, type hints, inline comments. Lives with the code.

---

## 3. Document Types — Taxonomy

### 3.1 Design Specifications (`docs/milestones/active/fleet-elevation/`)

31 documents defining the complete agent architecture redesign. Never directly
implemented — they define the target state. Key specs:
- `02: Agent Architecture` — file structure, injection order, SRP, onion, template system
- `03: Delivery Phases` — phase progressions, standards per phase, PO gates
- `04: The Brain` — orchestrator, autocomplete chains, pre-computation
- `05-14: Per-Role Specifications` — one spec per agent role (10 total)
- `15: Cross-Agent Synergy` — contribution matrix, parallel contributions
- `17: Standards Framework` — artifact types, quality criteria, per-phase standards
- `20: AI Behavior` — anti-corruption rules, structural prevention, disease catalogue
- `21: Task Lifecycle Redesign` — PRE/PROGRESS/POST
- `23: Agent Lifecycle` — IDLE, brain-evaluated heartbeats, strategic Claude calls

**Status:** Design only — 0/31 fully implemented.

### 3.2 Milestone Documents (`docs/milestones/active/`)

Work-tracking documents with checklist items. Each maps to PO requirements (quoted verbatim).
Examples: `fleet-autonomy-milestones.md` (29 items), `fleet-operations-protocol.md` (19 items),
`storm-prevention-system.md` (M-SP01-09), `labor-attribution-and-provenance.md` (M-LA01-08).

**Status symbols used:**
- ✅ Live tested and verified
- 🔨 Code exists, unit tested, NOT live tested
- 📐 Design complete, code not written
- 📝 Design/planning reference
- ⏳ Future (depends on hardware/ecosystem)

### 3.3 Standards Documents (`docs/milestones/active/standards/`)

8 per-type quality standards that gate all agent work. Created 2026-04-01.
Rule: **standards document FIRST, then build. No code without meeting its standard.**

| Standard | Gates | Key Content |
|----------|-------|-------------|
| claude-md-standard.md | B1 (CLAUDE.md ×10) | 8 required sections, 4000 char limit |
| heartbeat-md-standard.md | B2 (HEARTBEAT.md ×5) | 5 heartbeat types, priority protocol |
| agent-yaml-standard.md | B4 (agent.yaml ×10) | 14 required fields |
| identity-soul-standard.md | U-01 (agent identity) | 10 anti-corruption rules |
| tools-agents-standard.md | U-09 (self-knowledge) | chain-aware (generated), synergy |
| context-files-standard.md | H3 (pre-embed) | autocomplete chain (10 sections) |
| iac-mcp-standard.md | B3 (template deploy) | 6 scripts, idempotent, config-driven |
| brain-modules-standard.md | H1, H5, U-18 | 8 new modules, 13-step orchestrator |

### 3.4 System Reference Documents (`docs/systems/01-22`)

22 per-system deep-dive documents. Code-verified (every claim checked against source).
~10,283 lines total. Not design fiction — these describe what is actually implemented.

Systems covered: methodology, immune system, teaching, event bus, control surface,
agent lifecycle, orchestrator, MCP tools, standards, transpose, storm prevention,
budget, labor attribution, router, challenge, models, plane, notifications, session,
infrastructure, agent tooling, agent intelligence.

### 3.5 Spec-to-Code Mapping (`docs/SPEC-TO-CODE.md`)

**Type:** Living alignment document. Maps 69 design specs to 94 modules.
Purpose: "Without this mapping, the design docs and the code are disconnected."

Tracks four states per spec:
- ✅ Implemented and matches spec
- ⚠️ PARTIAL — read Gap column
- ❌ NOT DONE — read spec, implement from scratch

Also tracks: code that diverges from spec (critical mismatches), code with no spec
(built without design), and the critical path (what blocks live testing).

### 3.6 Architecture Document (`docs/ARCHITECTURE.md`)

**Type:** System map, code-verified.
- 20 systems and their interconnection matrix
- Critical data flow paths (task dispatch, review, disease detection, cost control)
- Module inventory (94 modules, line counts, test counts, status)
- Configuration overview
- Agent file structure
- Infrastructure services map
- Honest status section (updated regularly)
- Deep documentation reference (links to all major docs)

### 3.7 Vision Architecture (`docs/milestones/active/fleet-vision-architecture.md`)

**Type:** Master reference document. 4400+ lines, 43 sections.
Built by reading all 94 modules. Everything verified against source code.
"Only states what is verified in code or explicitly noted as 'design doc only.'"

Covers: complete system map, all flows, all gaps, 18 diagrams, path to live.

### 3.8 Path to Live (`docs/milestones/active/path-to-live.md`)

**Type:** Ordered execution plan. 24 steps across 8 phases.
Depends on vision architecture §33 (complete gap registry).
Each step has: what to build, why it's at this position, time estimate,
and links to the standard and design docs that enable it.

### 3.9 Knowledge Map (`docs/knowledge-map/`)

**Type:** Intent-driven injection metadata system. 7 files.

| File | Purpose |
|------|---------|
| methodology-manual.md | Per-stage tool/skill/command/MCP recommendations |
| standards-manual.md | Dense reference for all standards |
| agent-manuals.md | Per-role mission, tools, chains, wake triggers |
| module-manuals.md | Per-module descriptions |
| cross-references.yaml | System→module→tool→agent relationship graph |
| intent-map.yaml | Situation (role+stage) → what to inject |
| injection-profiles.yaml | How much content per context size (4 tiers) |

### 3.10 Status Tracker (`docs/milestones/STATUS-TRACKER.md`)

**Type:** Source of truth for current state. Updated per session.
Tracks: all services (running/stopped), setup IaC status, bugs fixed this session,
vendor patches, DSPD status, AICP status, event bus status, tools system elevation status,
what's actually next (numbered checklist with ✅ completed).

### 3.11 PO Verbatim Log (`docs/milestones/active/po-vision-2026-04-08-verbatim.md`)

**Type:** Sacrosanct PO requirements. Direct quotes, never paraphrased.
Instruction: "Do not minimize or compact or compress or conflate anything I said, quote me verbatim."
Contains 41 verbatim requirements, each numbered, plus extracted themes for milestone planning.

### 3.12 Per-Agent Files

Each agent has a structured file set under `agents/{name}/`:
- `agent.yaml` — gateway config, committed (14 required fields)
- `CLAUDE.md` — role-specific rules, committed, max 4000 chars
- `HEARTBEAT.md` — action protocol, committed
- `context/fleet-context.md` — generated by brain every 30s
- `context/task-context.md` — generated at dispatch
- `IDENTITY.md` — who the agent is (innermost layer)
- `SOUL.md` — values, anti-corruption rules
- `TOOLS.md` — chain-aware tool reference (generated)
- `AGENTS.md` — knowledge of colleagues (generated)
- `USER.md` — who the agent serves

**Injection order:** IDENTITY → SOUL → CLAUDE → TOOLS → AGENTS → context/ → HEARTBEAT

---

## 4. Methodology System — Five Stages

The methodology is the core operational pattern. Every task progresses through stages:

### Stages

1. **CONVERSATION** — understand the requirement, ask questions, extract knowledge
   - MUST: Discuss, ask specific questions, identify gaps, propose understanding
   - MUST NOT: Write code, commit, create PRs, produce finished deliverables
   - Advance when: PO confirms understanding, verbatim requirement populated

2. **ANALYSIS** — examine what exists (codebase, architecture, dependencies)
   - MUST: Read and examine codebase, produce analysis document with file references
   - MUST NOT: Produce solutions (that's reasoning), write implementation code
   - CAN PRODUCE: Analysis documents, current state assessments, gap analysis

3. **INVESTIGATION** — research what's possible, explore multiple options
   - MUST: Research solutions, explore MULTIPLE options, cite sources
   - MUST NOT: Decide on approach (that's reasoning), write implementation code
   - CAN PRODUCE: Research findings, option comparisons with tradeoffs

4. **REASONING** — plan the approach, create implementation plan
   - MUST: Decide approach from all inputs, produce plan referencing verbatim
   - MUST NOT: Start implementing, commit code
   - Required: Contributions from specialists arrive here before WORK

5. **WORK** — execute the confirmed plan
   - Required tool sequence: fleet_read_context → fleet_task_accept → fleet_commit(s) → fleet_task_complete
   - MUST NOT: Deviate from plan, add unrequested scope, skip tests

### Stage Gating

- `fleet_commit` blocked in CONVERSATION stage only (should be stages 2-5)
- `fleet_task_complete` blocked in all stages except WORK
- Stage gating is structural prevention (Line 1 anti-corruption)
- Task readiness score (0-100) drives progression; PO confirms REASONING→WORK at readiness 99

### Methodology in Context

The brain injects stage-specific content (MUST/MUST NOT/CAN lists) into every
agent context file. The methodology manual maps tools, skills, commands, MCP servers,
and plugins to each stage. This is "ALWAYS full — never compress process."

---

## 5. Agent Identity System — Onion Architecture

Agent identity follows an 8-layer onion pattern with deliberate injection order:

```
IDENTITY.md   (layer 1 — who you are, deepest grounding)
SOUL.md       (layer 2 — values, full 10 anti-corruption rules)
CLAUDE.md     (layer 3 — role rules, high influence zone, max 4000 chars)
TOOLS.md      (layer 4 — chain-aware tool reference, generated)
AGENTS.md     (layer 5 — colleague knowledge, synergy map, generated)
context/      (layer 6 — dynamic fleet state + task data, every 30s)
HEARTBEAT.md  (layer 7 — action protocol, outermost behavioral instruction)
```

### The 10 Anti-Corruption Rules (in SOUL.md, sacrosanct)

Shared across all 10 agents verbatim:
1. Do not deform or summarize the PO's words
2. Do not replace words or compress verbatim
3. Do not add scope not in verbatim
4. Do not compress — reproduce full detail
5. Do not skip reading files before modifying
6. No code outside WORK stage
7. Three corrections = wrong direction (stop, ask)
8. Follow autocomplete chain
9. Ask don't guess
10. Not infallible — update assumptions

### CLAUDE.md — 8 Required Sections

1. Core Responsibility (ONE sentence)
2. Role-Specific Rules (largest, unique per role)
3. Stage Protocol (behavior per methodology stage)
4. Tool Chains (4-8 tools with chain patterns)
5. Contribution Model (gives/receives per synergy matrix)
6. Boundaries (min 3 explicit refusals with role redirects)
7. Context Awareness (both countdowns: context %, rate limit %)
8. Anti-Corruption (brief summary, reinforcement)

---

## 6. Orchestrator — The Brain

30-second cycle, 9-step execution (target: 13-step per spec):

```
Step 0: _refresh_agent_contexts()   — write FULL context to all agents
Step 1: _security_scan()            — check tasks for suspicious content
Step 2: _run_doctor()               — immune system: detect + respond
Step 3: _ensure_review_approvals()  — create approval objects for review tasks
Step 4: _wake_drivers()             — inject wake messages to PM/fleet-ops
Step 5: _dispatch_ready_tasks()     — dispatch unblocked inbox tasks (max 2/cycle)
Step 6: _process_directives()       — parse PO directives from board memory
Step 7: _evaluate_parents()         — all children done → parent to review
Step 8: _health_check()             — stuck tasks, offline agents
```

Pre-step gates: storm monitor check (CRITICAL=halt), fleet mode check (work_mode),
budget check (OAuth quota), gateway duplication check.

### Orchestrator Role Providers

The brain provides role-specific context to each agent:
- **fleet-ops:** pending_approvals, review_queue, offline_agents
- **project-manager:** unassigned_tasks, blocked_tasks, sprint progress
- **architect:** tasks needing design review
- **workers:** artifact completeness + contributions received

---

## 7. Knowledge Map — Intent-Driven Injection

The knowledge map is a metadata system that controls what content gets injected
into agent context based on situation (role + stage + model + context size).

### Four Injection Profiles (by model/context tier)

| Profile | Model | Context Budget | Depth |
|---------|-------|----------------|-------|
| opus-1m | opus-4-6 (1M) | ~50K tokens | Everything: full system docs, full methodology, full skills |
| sonnet-200k | sonnet-4-6 | ~15K tokens | Condensed: key concepts, essential guidance |
| localai-8k | hermes-3b / phi | ~2K tokens | Minimal: mission + stage MUST/MUST NOT + tool reference |
| heartbeat | any | ~1K tokens | Fleet state + directives + tasks only |

**Key principle:** "methodology is ALWAYS full — never compress process" (even at sonnet-200k tier)

### Intent Map Structure

Per-role per-situation injection specifications. Each intent defines:
- What agent manual section to inject (which agent, which detail level)
- Which methodology stage to inject (ALWAYS full)
- Which skills to reference (names only or full descriptions)
- Which commands are relevant
- Which tool chains to include
- Which MCP servers and plugins to mention
- Whether to include contributions and trail data

Examples: `engineer-work` injects engineer manual (full), work methodology (full),
6 skills + 4 superpowers skills, 4 commands, 4 MCP servers, all contributions received.

### Cross-Reference Graph (`cross-references.yaml`)

22 systems, each entry contains:
- ID (S01-S22)
- Python modules list
- Tools (uses/produces/gates)
- Connected systems (with relationship type)
- Agent roles (primary/reads/operates/monitors)
- Skills, commands, hooks, plugins

This is the machine-readable relationship graph used by the intent-map injection logic.

---

## 8. Spec-to-Code Methodology

The SPEC-TO-CODE pattern is central to OpenFleet's development approach:

### The Mapping Document Pattern

`docs/SPEC-TO-CODE.md` is a living document that:
1. Lists every design document (69 specs)
2. Maps each to implementation modules (94 modules)
3. Tracks status (✅ / ⚠️ PARTIAL / ❌ NOT DONE)
4. Documents gaps (what's missing from the implementation)
5. Documents divergences (where code does something DIFFERENT from spec)
6. Lists code built without any spec
7. Defines the critical path (ordered blockers to live operation)

### How to Use It (from the document itself)

For each milestone/task:
1. Find the spec in this document
2. Check "Code Status" column
3. ✅ → code matches spec, proceed to testing
4. ⚠️ PARTIAL → read Gap column, implement what's missing
5. ❌ NOT DONE → read spec, implement from scratch
6. After implementation → update this document's status

### Contamination Control (2026-04-01)

A contamination cleanup pass removed "fabricated specifics" — code that had been
written based on imagined details not in any spec. The test count dropped from ~1800 to
1730 (removed tests for invented behavior). Principle: "spec first, code second."

---

## 9. Document Production Order

Based on the path-to-live and SPEC-TO-CODE methodology, documents are produced in this order:

### Phase 0: Vision + Strategy (done first, enables everything)
1. PO verbatim requirements log (sacrosanct — never paraphrased)
2. Fleet vision architecture (code-verified system map, 43 sections)
3. Fleet master diagrams (18 diagrams)

### Phase 1: Design Specifications (before any code)
4. Per-system design specs (fleet-elevation/02-31)
5. Per-subsystem specs (methodology, immune, teaching, context)
6. Strategic system designs (storm, budget, router, labor, challenge, models)

### Phase 2: Standards (before implementing per-type work)
7. Per-type quality standards (claude-md-standard, heartbeat-md-standard, etc.)
8. Master standards index

### Phase 3: Architecture Reference (code-verified, after code exists)
9. Per-system reference docs (docs/systems/01-22)
10. Architecture document (system map with interconnections)
11. SPEC-TO-CODE mapping (living alignment document)

### Phase 4: Milestone Tracking (continuously updated)
12. Milestone documents per system/feature
13. MASTER-INDEX.md
14. STATUS-TRACKER.md (source of truth, per-session updates)
15. Path-to-live (24-step ordered execution plan)

### Phase 5: Knowledge Map (after systems are understood)
16. Agent manuals (per-role manual with mission, tools, chains)
17. Methodology manual (per-stage tool/skill/command recommendations)
18. Standards manual (dense reference)
19. Module manuals
20. Cross-references.yaml (machine-readable relationship graph)
21. Intent-map.yaml (situation → injection rules)
22. Injection-profiles.yaml (context tier → depth rules)

---

## 10. Cross-Document Relationship Patterns

### PO Requirements → Design Specs → Standards → Code → System Docs

Every design spec traces back to a PO requirement (quoted verbatim).
Every standard gates a specific set of spec implementations.
Every system doc is code-verified (not spec fiction).
The SPEC-TO-CODE doc bridges all three.

### Living Document Principle

Key documents are explicitly "living":
- `SPEC-TO-CODE.md` — "As specs are implemented, status changes from ❌ to ⚠️ to ✅"
- `STATUS-TRACKER.md` — last updated date, per-session changes
- `MASTER-INDEX.md` — "honest assessment of every document and milestone"
- `fleet-vision-architecture.md` — built from reading actual code, not summaries

### The "Not Live Tested = Not Finished" Rule

From MASTER-INDEX.md: "Rule: 'Not live tested = not finished.' Code existing ≠ done."
This is enforced in the milestone status symbols. A system with 90 unit tests is still
marked 🔨 (code exists) not ✅ (verified). This prevents false completion signals.

### Verbatim Preservation Chain

PO requirements flow verbatim through the system:
1. PO says something → logged verbatim in `po-vision-{date}-verbatim.md`
2. Verbatim quote appears in design spec that addresses it
3. `requirement_verbatim` field set on OCMC task (TaskCustomFields)
4. Agents read verbatim from task context
5. Fleet-ops verifies agent work AGAINST verbatim (not their interpretation)
6. SPEC-TO-CODE.md cites PO quotes to justify design decisions

---

## 11. Agent Role System

### 10 Roles in Two Categories

**Drivers (orchestration/governance):**
- `fleet-ops` — board lead, reviews, quality, methodology compliance
- `project-manager` — sprint planning, task assignment, Plane bridge
- `devsecops-expert` — security reviews, vulnerability scanning
- `accountability-generator` — governance, compliance, audit trails

**Workers (execution/contribution):**
- `architect` — system design, technical decisions
- `software-engineer` — implementation
- `qa-engineer` — testing, quality assurance
- `devops` — infrastructure, CI/CD, IaC
- `technical-writer` — documentation, specs
- `ux-designer` — UI/UX design, user flows

### Synergy Matrix (Contribution Flow)

The contribution model defines who contributes what to whom, and when:
- **QA** predefined test criteria (TC-001 format) BEFORE engineer implements
- **Architect** provides design_input when task enters REASONING
- **DevSecOps** provides security_requirement (phase-appropriate: POC basic, production full)
- **DevOps** provides deployment_manifest
- **UX** provides ux_spec (all states: loading/error/empty/success/partial)
- **Writer** provides documentation_outline

Workers receive contributions into their `INPUTS FROM COLLEAGUES` context section.
The brain creates contribution subtasks automatically when a task reaches REASONING.

### Heartbeat Types (5, not 10)

1. **PM heartbeat** — fleet state + unassigned tasks + blocked tasks + sprint progress
2. **Fleet-ops heartbeat** — pending approvals + review queue + offline agents + health
3. **Architect heartbeat** — tasks needing design + complexity flags + architecture decisions
4. **DevSecOps heartbeat** — security alerts + PRs needing review + infra health
5. **Worker heartbeat** (template, per-role variation) — assigned tasks + artifact state + contributions received

---

## 12. Agent Lifecycle Model

```
ACTIVE   — currently running a session
  ↓ (task complete or timeout)
IDLE     — between tasks, heartbeating normally
  ↓ (no new tasks, N heartbeat OKs)
SLEEPING — brain evaluates (no Claude call), reduced heartbeat
  ↓ (extended inactivity)
OFFLINE  — no heartbeat
```

**Brain evaluation (SLEEPING+):** Brain evaluates wake triggers in Python ($0, no Claude call):
- Direct mention? Task assigned? Contribution received? Directive? Role trigger?
- Wake trigger found → fire real heartbeat with strategic config
- Nothing found → silent OK (no Claude call)
- Impact: ~70% cost reduction on idle fleet

---

## 13. Infrastructure and Tooling Patterns

### IaC-Only Principle

"Every manual step is a bug." All configuration changes must go in scripts.
Setup is reproducible from zero with `./setup.sh`. Key scripts:
- `setup.sh` — master setup, zero to running fleet
- `generate-tools-md.py` — Python pipeline, generates 7-layer TOOLS.md per agent
- `generate-agents-md.py` — generates per-agent AGENTS.md (synergy + colleagues)
- `validate-tooling-configs.py` — cross-validation, 0 errors
- `configure-agent-settings.sh` — reads agent-hooks.yaml, deploys hooks

### Vendor Patch Pattern

Patches to vendored dependencies (Mission Control) stored in `patches/` directory.
Applied by `scripts/apply-patches.sh`. Survive fresh git clone.
Currently 3 patches (0001, 0002, 0003).

### MCP Server Pattern

13 core MCP tools + role-specific group calls (36 role-specific, 30 generic = 66 total).
The MCP server is the primary agent interface — tools enforce stage gating, emit events,
record labor stamps, sync to all 6 surfaces.

**6 surfaces triggered by fleet_task_complete:**
git push, create PR, update MC task, create approval, post to IRC #reviews, notify ntfy,
update Plane issue, post Plane comment, emit fleet.task.completed event.

---

## 14. Quality Gates and Testing Strategy

### Testing Taxonomy

- **Unit tests:** Pure logic tests (currently 2075+ passing, 0 failures)
- **Integration tests:** Cross-system wiring (23 tests, pass)
- **Live tests:** Real agents doing real work (0/35 designed scenarios ever run)

### Quality Gate per Artifact Type (7 types)

From `fleet/core/standards.py`:
1. plan_document — requires verbatim reference, target files, stage mapping
2. analysis_document — requires file references, findings, implications
3. investigation_document — requires multiple options (min 3), tradeoffs
4. pull_request — title, body, labels, tests referenced
5. completion_claim — acceptance criteria met, tests pass, verbatim addressed
6. qa_test_definition — structured test cases with IDs (TC-001 format)
7. compliance_report — trail events, methodology adherence metrics

### Plan Quality Enforcement

`plan_quality.py` validates plans at `fleet_task_accept()`:
- Must reference verbatim
- Must specify target files
- Must map criteria to steps
- Must be submitted before commits allowed

---

## 15. Budget and Cost Control System

### Multi-Axis Control

The fleet has 3 control axes (set by PO via OCMC):
1. **work_mode** — work-paused, finish-current-work, normal-work, full-autonomy
2. **cycle_phase** — current delivery phase (POC, MVP, staging, production)
3. **backend_mode** — which backends to use (7 combinations)

### Budget Modes

Budget tempo controls dispatch frequency:
- turbo: 5s cycle
- aggressive: 15s cycle
- standard: 30s cycle
- economic: 60s cycle

Budget monitor reads real Claude OAuth quota before every dispatch.
Dispatch paused at 90% usage, hard-stopped at 95%.

### Local-First Strategy

The core mission (AICP project): offload routine work to LocalAI.
Model routing:
- Drivers (PM, fleet-ops, architect, devsecops): always Claude Opus
- Workers (engineer, devops, QA, writer, UX): Claude Sonnet (brain can override)
- Heartbeats: target hermes-3b (10s cold, 1.2s warm) at $0 cost
- Routine tasks: LocalAI when available and capable

### Labor Attribution (LaborStamp)

Every completed task gets a LaborStamp:
- Agent identity + backend + model used
- Challenge rounds (adversarial validation count)
- Confidence tier
- Cost delta
- Trainee flag (LocalAI = trainee, Claude = expert)

---

## 16. Immune System Pattern

Three subsystems working together (all built and live-verified):

### Doctor (`doctor.py`)

Detects disease patterns in agent behavior. 4/11 detections implemented:
- `detect_protocol_violation()` — fleet_commit in wrong stage
- `detect_laziness()` — fast completion relative to story points
- `detect_stuck()` — no activity for threshold minutes
- `detect_correction_threshold()` — 3 corrections = prune

### Teaching System (`teaching.py`)

8/11 lesson templates. When doctor detects a disease:
1. Adapt lesson to agent's specific violation
2. Inject lesson via gateway `inject_content()`
3. Evaluate agent's next response for comprehension
4. Track lesson results (LessonTracker)

### Disease Catalogue (11 disease categories)

All 11 defined as DiseaseCategory enum. Key diseases:
- abstraction, code_without_reading, scope_creep, cascading_fix
- context_contamination, not_listening, compression
- contribution_avoidance, synergy_bypass (2 new)

**Response escalation:** NONE → MONITOR → FORCE_COMPACT → TRIGGER_TEACHING → PRUNE → ESCALATE_TO_PO

---

## 17. Milestone Lifecycle Pattern

### Status Transitions

```
📝 Planning/reference      — document exists, design not started
📐 Design complete         — spec written, code not started
🔨 Code exists             — implemented, unit tested, NOT live tested
✅ Live tested             — verified with real agents doing real work
```

### Critical Distinction

The project maintains a strict distinction between "code exists" and "done."
A system with 200+ unit tests and 5 integration tests is still 🔨 (not done)
until a real agent uses it in a real task and the outcome is verified.

### Milestone Numbering

Different systems have different prefixes:
- M-SP (storm prevention), M-BM (budget mode), M-BR (backend router)
- M-LA (labor attribution), M-IV (iterative validation), M-MU (model upgrade)
- M-EB (event bus), AR (agent rework), CB (context bundles)
- U (unified implementation plan)
- B (blockers), H (hardening), E (ecosystem)

---

## 18. Key Architectural Decisions and Patterns

### Anti-Corruption Line 1: Structural Prevention

Stage gating (MCP tools blocked outside appropriate stage) is the structural
prevention layer — it makes bad behavior impossible, not just discouraged.

### Anti-Corruption Line 2: Teaching

When structural prevention doesn't catch it, the immune system detects it
and injects corrective lessons (no human intervention required).

### Anti-Corruption Line 3: Review

Fleet-ops review is the last line of defense. 7-step protocol:
1. Read verbatim requirement
2. Read completion claim
3. Check acceptance criteria
4. Verify trail (trail must be complete — tasks with incomplete trails CANNOT be approved)
5. Check plan was followed
6. Run tests / check artifacts
7. Approve or reject with specific feedback and stage regression instructions

### Autocomplete Chain Engineering

The core design principle: context is structured so that the correct next action
is the natural continuation. Context files are assembled in order:
1. Identity and values (static, inner layer)
2. Role rules and stage protocol
3. Chain-aware tool reference
4. Colleague knowledge and synergy
5. Dynamic fleet state
6. Current task with verbatim
7. Stage-specific instructions (MUST/MUST NOT/CAN)
8. Contributions received
9. Trail
10. Context awareness (% remaining, rate limit)

This sequence is designed to "make the moment to create the artifact easy and natural."

### Scaffold → Foundation → Infrastructure → Features

Explicit PO requirement that this pattern applies at every level:
- **Scaffolding:** core config files, project structure, tech stack
- **Foundation:** modules/packages, design system, architecture documents
- **Infrastructure:** build on foundation (services, data layer, integrations)
- **Features:** product-specific functionality

Applied to every domain, every task.

---

## 19. Integration with devops-solutions-research-wiki

The wiki (`../devops-solutions-research-wiki`) serves as OpenFleet's:
- Second brain for cross-project knowledge synthesis
- LightRAG graph source (via `## Relationships` sections in wiki pages)
- Feed for the AICP project documentation

The wiki is explicitly listed as one of the three documentation layers in CLAUDE.md.
Wiki pages use YAML frontmatter with relationships in `^([A-Z][A-Z /\-]+?):\s*(.+)$` format,
compatible with `kb_sync.py` for LightRAG ingestion.

---

## 20. Gaps and What's Missing (as of 2026-04-07)

From SPEC-TO-CODE.md and path-to-live.md:

### Critical Blockers (before any live test)

1. **Gateway injection order not implemented** — gateway reads ONLY CLAUDE.md + context/.
   Does NOT read IDENTITY, SOUL, TOOLS, AGENTS, HEARTBEAT. (2-4 hours to fix)
2. **0/10 agent CLAUDE.md follow spec** — none have correct 8 sections, stage protocol,
   contribution model, anti-corruption (20-40 hours total)
3. **Contribution flow not built** — `fleet_contribute` MCP tool doesn't exist.
   Brain doesn't create contribution subtasks. (8-16 hours)

### Major Missing Systems

- Autocomplete chain builder (`autocomplete.py`) — not built
- Trail recorder (`trail_recorder.py`) — not built
- Session manager (`session_manager.py`) — not built
- Phase system (`phase_system.py`) — not built
- 5 MCP tools not built: fleet_contribute, fleet_request_input, fleet_gate_request,
  fleet_phase_advance, fleet_transfer
- 7/11 disease detections not implemented

### Zero Live Tests

Despite 2075+ unit tests and 23 integration tests: **zero end-to-end live tests**
with real agents doing real work through the full lifecycle.

---

## Sources Read

- `/home/jfortin/openfleet/CLAUDE.md`
- `/home/jfortin/openfleet/docs/SPEC-TO-CODE.md`
- `/home/jfortin/openfleet/docs/ARCHITECTURE.md`
- `/home/jfortin/openfleet/docs/milestones/README.md`
- `/home/jfortin/openfleet/docs/milestones/STATUS-TRACKER.md`
- `/home/jfortin/openfleet/docs/milestones/active/MASTER-INDEX.md`
- `/home/jfortin/openfleet/docs/milestones/active/path-to-live.md`
- `/home/jfortin/openfleet/docs/milestones/active/po-vision-2026-04-08-verbatim.md`
- `/home/jfortin/openfleet/docs/knowledge-map/methodology-manual.md`
- `/home/jfortin/openfleet/docs/knowledge-map/cross-references.yaml`
- `/home/jfortin/openfleet/docs/knowledge-map/intent-map.yaml`
- `/home/jfortin/openfleet/docs/knowledge-map/injection-profiles.yaml`
- `/home/jfortin/openfleet/docs/knowledge-map/agent-manuals.md` (partial)
- `/home/jfortin/openfleet/docs/knowledge-map/standards-manual.md` (partial)
- `/home/jfortin/openfleet/docs/milestones/active/fleet-vision-architecture.md` (partial)
- `/home/jfortin/openfleet/.claude/settings.json`
- `/home/jfortin/openfleet/.claude/agents/` (directory listing — 12 agents)
- `/home/jfortin/openfleet/.claude/skills/` (directory listing — 78 skills)

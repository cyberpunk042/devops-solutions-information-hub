---
title: "Wiki Backlog Pattern"
type: concept
layer: 2
maturity: growing
domain: knowledge-systems
status: synthesized
confidence: authoritative
created: 2026-04-09
updated: 2026-04-09
sources:
  - id: src-openarms-methodology-scan
    type: documentation
    file: raw/articles/openarms-methodology-scan.md
    title: "OpenArms Methodology Scan — Deep Research Findings"
    ingested: 2026-04-09
  - id: src-openfleet-methodology-scan
    type: documentation
    file: raw/articles/openfleet-methodology-scan.md
    title: "OpenFleet Methodology Scan — Deep Research Findings"
    ingested: 2026-04-09
tags: [wiki-backlog, frontmatter-state-machine, auto-loop, pm-in-wiki, epics, tasks, llm-wiki, knowledge-base, project-management, autonomous-agents, operator-directives, verbatim-log, second-brain, openarms, openfleet]
---

# Wiki Backlog Pattern

## Summary

The Wiki Backlog Pattern is an approach to project management where the wiki knowledge base also serves as the complete task tracking system: epics, modules, tasks, and issues live as typed wiki pages with YAML frontmatter that encodes status, stage, readiness, and artifact provenance. An autonomous agent can read the wiki, determine the highest-priority unblocked task, execute the next required stage, update the frontmatter, commit, and loop — indefinitely, without any external board, ticket system, or human coordination. The wiki IS the control surface. This pattern is fully implemented in OpenArms (22 tasks, 8 epics, infinite auto-loop), partially in OpenFleet (wiki/backlog/ with 17 epics), and is the target architecture for this research wiki's own evolution pipeline.

## Key Insights

- **The wiki and the backlog are the same file system**: In the Wiki Backlog Pattern, there is no separate "wiki" and "task board." Domain knowledge pages and task pages coexist in the same vault, with different `type` values in their frontmatter. An agent reading `wiki/backlog/tasks/T023.md` and `wiki/domains/architecture/network-rules-config-design.md` is reading the same system. The task file links to the knowledge page it produced. The knowledge page links to the epic that motivated it.

- **Frontmatter as state machine**: Task frontmatter fields form a complete, inspectable, auditable state machine without any external process dependency. The critical fields: `status` (draft → active → in-progress → blocked → done → archived), `current_stage` (document / design / scaffold / implement / test), `stages_completed` (list), `readiness` (0-100), `artifacts` (file paths proving work was done). Setting `readiness: 100` while `stages_completed` is missing entries is an absolute prohibition — the frontmatter itself enforces the gate.

- **The infinite auto-loop makes the wiki self-executing**: OpenArms' auto-loop algorithm: read config → pick highest-priority unblocked task → determine next required stage → execute stage → produce artifact → update frontmatter → one commit → verify → loop. The loop continues until the end condition is met (backlog-empty, time-limit, cost-limit, task-count). This is not a cron job or a CI pipeline — it is the agent reading the wiki and doing the next thing. No external scheduler required.

- **Operator directives are sacrosanct verbatim log entries**: Both OpenArms and OpenFleet store founding operator directives as dated verbatim log files (`wiki/log/2026-04-08-initial-vision.md`) that are never paraphrased, compressed, or overridden. The log is the primary source of truth. All design decisions, task priorities, and feature choices trace back to verbatim quotes from this log. This turns the wiki's log directory into a chain-of-custody document for intent.

- **Priority and dependency structure in frontmatter**: OpenArms' schema includes `priority` (P0-P3), `epic` (E001-E008), `module`, `depends_on`, and `blocked_by` fields. The task selection algorithm filters on these: filter by epic/module scope if restricted, sort by priority, skip blocked and archived, prefer tasks whose dependencies are completed. The agent does not need a PM tool to determine what to do next — it reads the YAML.

- **The backlog _index.md is the control dashboard**: The backlog `_index.md` file contains the full overview table: epic IDs, names, priorities, task counts, completion status. The agent reads this first to understand the current state of the project. The index is not a generated artifact — it is actively maintained, updated after each task completion. The index is the project's single source of truth for "what is there to do."

- **Commit log as stage audit trail**: OpenArms' one-commit-per-stage convention (`feat(wiki): T023 document — ...`) turns git history into a stage-gating audit log. The full lifecycle of every task is recoverable from git log. If a task was never staged (no scaffold commit), that is visible. If a task was completed without a test commit, that is visible. The wiki and the git log together form a complete project history.

- **Multiple page types coexist in the same schema**: The Wiki Backlog Pattern extends the standard wiki schema (concept, reference, decision, pattern, lesson) with backlog types (epic, module, task, note). Each type has its own required sections and frontmatter fields. The schema is the unifying layer — the same YAML parser reads knowledge pages and task pages. This makes it possible to query across the entire wiki: "which tasks relate to which knowledge pages?"

- **This wiki's own evolution pipeline is a partial implementation**: The `wiki/manifest.json`, `python3 -m tools.pipeline evolve --score`, and `python3 -m tools.pipeline gaps` commands implement the knowledge-side of this pattern. What is missing: a `wiki/backlog/` directory with typed epic/task pages, a `wiki/log/` directory for operator directives, and an auto-loop that processes the backlog and produces wiki pages as stage artifacts. The OpenArms implementation is the reference to adopt.

## Deep Analysis

### Full Schema: Knowledge + Backlog Types

The Wiki Backlog Pattern requires a unified schema that covers both knowledge pages and operational/project pages:

**Knowledge types** (standard wiki):
- `concept`: Summary, Key Insights, Deep Analysis, Relationships
- `reference`: Summary, Reference Data, Relationships
- `decision`: Summary, Context, Decision, Consequences, Relationships
- `pattern`: Summary, Problem, Solution, Examples, Relationships
- `lesson`: Summary, Context, Insight, Application, Relationships

**Backlog types** (project management layer):
- `epic`: Summary, Goals, Modules, Success Criteria, Relationships
- `module`: Summary, Details, Done When, Relationships (sub-unit of an epic)
- `task`: Summary, Details, Done When, Relationships (executable unit)
- `note`: Unstructured capture (session log, finding, retrospective)

**Task-specific required frontmatter** (not in knowledge pages):
```yaml
task_type: task | bug | spike | docs | refactor | epic/module
current_stage: document | design | scaffold | implement | test
readiness: 0-100
stages_completed: [document, design]
artifacts:
  - wiki/domains/architecture/design-doc.md
  - src/types/config.ts
  - src/config.test.ts
depends_on: [T019, T020]
blocked_by: []
epic: E003
priority: P1
estimate: 4h
assignee: solo-agent
```

### The Backlog Directory Structure

OpenArms' production implementation:

```
wiki/
  config/
    schema.yaml         — page type definitions, status lifecycles, quality gates
    methodology.yaml    — 5 stages, task types, modes, end conditions
    agent-directive.md  — solo agent bootstrap: 14-step work loop
    modes.yaml          — autonomy spectrum documentation
  domains/              — knowledge pages by domain (same as this wiki)
  backlog/
    _index.md           — overview table: 8 epics, status, task counts
    epics/
      E001.md           — Solo Agent Mode (P1), phases, modules, success criteria
      E002.md           — Network Rules Engine (P1)
      ...E008.md
    modules/            — mid-level groupings within epics
    tasks/
      _index.md         — full task table: ID, epic, status, stage, readiness
      T001.md → T022.md — individual task files with full frontmatter
  log/
    2026-04-08-initial-vision.md   — founding directives (sacrosanct, verbatim)
    2026-04-09-first-agent-run-findings.md  — retrospective + findings
```

The `backlog/_index.md` is the critical dashboard. It shows at a glance: which epics are active, which tasks are in-progress, which tasks are blocked. The agent reads this first on every loop iteration.

### OpenFleet's Parallel Implementation

OpenFleet implements a similar pattern but with key structural differences:

- `wiki/backlog/_index.md` — 17 epics (E001-E017) with modules and tasks
- `wiki/log/` — PO directives verbatim, chronological
- `wiki/domains/` — knowledge pages by domain

The key difference: OpenFleet has an external board (Plane/DSPD) as the authoritative task tracker. The wiki backlog is a "first brain" — it exists to give agents context, but Plane is the source of truth for task state. OpenArms eliminates this duality — the wiki IS the board, no external system required.

The advantage of OpenArms' approach: zero external dependencies for task tracking. The disadvantage: no human-facing project management UI (Plane provides Gantt charts, burndown, sprint views). The tradeoff is clear: wiki-only is optimal for solo-agent systems; external board is optimal when humans need visibility.

### The Auto-Loop Algorithm in Detail

OpenArms' 14-step agent work loop (from `wiki/config/agent-directive.md`) is the reference implementation:

1. Read CLAUDE.md → methodology.yaml → agent-directive.md → backlog/_index.md
2. Pick highest priority task (filter: epic/module scope if restricted, priority P0→P3, dependencies resolved; skip: done/archived/blocked)
3. Determine next required stage from methodology.yaml based on task_type
4. Read stage protocol from methodology.yaml (full MUST/MUST NOT/CAN list for that stage)
5. Execute ONLY that stage — produce ONLY the artifacts defined for that stage
6. Update task frontmatter: `current_stage`, `stages_completed`, `readiness`, `artifacts`, `status`
7. Git: stage ALL changed files and commit — ONE COMMIT PER STAGE (conventional commit format)
8. VERIFY: re-read task file, confirm frontmatter matches actual state
9. If more stages remain for this task, go to step 3
10. When all required stages are completed: set `status: done`, `readiness: 100`
11. Update backlog `_index.md` (move task to Completed section)
12. Write log entry to `wiki/log/` (what was done, what was found, what was deferred)
13. Check end condition (backlog-empty? time-limit? cost-limit? task-count?) — if not met, go to step 1
14. Final: commit remaining changes, print session summary

This loop is self-contained. It does not require a human to push tasks onto the agent — the agent reads the backlog and determines its own next action. The human's role shifts from "task assignment" to "backlog curation and end-condition configuration."

### The Log Directory as Operator Directive Chain

The `wiki/log/` directory in both OpenArms and OpenFleet stores operator directives as dated files treated with the same immutability as source control history. The rules:

1. **Verbatim, never paraphrased**: Operator words are logged character-for-character. OpenFleet: "Do not minimize or compact or compress or conflate anything I said, quote me verbatim." OpenArms: "Quote verbatim from wiki/log/. Never paraphrase." This research wiki's own MEMORY.md enforces the same rule.

2. **Never overridden**: Directives in `wiki/log/` supersede all other instructions. A new CLAUDE.md cannot contradict a founding directive in `wiki/log/`. The log has higher authority than the config.

3. **Date-stamped and cumulative**: Each session or founding event produces a new log file. The log is an append-only record. The full history of operator intent is recoverable.

4. **Referenced by tasks and designs**: Every task that implements a founding directive includes a direct quote. Every design doc that addresses a directive references it by log file and date. The chain from intent to implementation is traceable through the wiki's own structure.

### This Wiki's Path to Full Wiki Backlog Pattern

This research wiki (`devops-solutions-research-wiki`) currently implements the **knowledge side** of the pattern fully: domain pages, YAML frontmatter, typed relationships, quality gates, evolution pipeline, manifest generation. What is not yet implemented:

| Component | Current State | Target State |
|-----------|--------------|--------------|
| `wiki/backlog/` | Not present | epics/ + tasks/ + _index.md |
| `wiki/log/` | `raw/notes/` (raw, not wiki-typed) | Dated wiki-typed log pages |
| Backlog schema | Not in config/schema.yaml | epic/module/task types with stage fields |
| Auto-loop | `pipeline chain continue` (partial) | Full 14-step agent-directive loop |
| Task stage-gating | Not implemented | readiness + stages_completed in frontmatter |
| Operator directive chain | MEMORY.md (external) | wiki/log/ as primary source of truth |

The OpenArms implementation (`/home/jfortin/openarms/wiki/`) is the direct reference for this adoption. The wiki/config/schema.yaml, wiki/config/methodology.yaml, and wiki/config/agent-directive.md files are the templates.

### Relationship to PM Tools

The Wiki Backlog Pattern does not replace PM tools in multi-stakeholder contexts — it provides an agent-native alternative that works where PM tools fail:

- **PM tools fail when**: The agent cannot read the board natively, when tasks require LLM context to understand, when the board state drifts from the code reality
- **Wiki backlog fails when**: Human stakeholders need visual project management (burndown, Gantt), when multiple human contributors need assignment tracking, when the project has external compliance reporting requirements

OpenFleet's hybrid model (wiki backlog as "first brain" + Plane as external board) is the appropriate architecture for multi-stakeholder projects. OpenArms' wiki-only model is optimal for solo-agent, single-operator systems.

### The "Wiki IS the Task Queue" Insight

The deepest insight in the Wiki Backlog Pattern is that the wiki and the task queue are **ontologically identical**. A "task" to write the documentation for feature X IS a knowledge page about feature X at readiness 0. When the agent completes the task, the same file becomes a knowledge page at readiness 100 with `status: done`. The task completion artifact (a wiki page or code file) is not separate from the task record — the artifact IS the task, proven done.

This eliminates the most common failure mode in project management: tasks that are marked "done" but whose artifacts are missing, incomplete, or don't match what was requested. In the Wiki Backlog Pattern, you cannot mark a task done without the artifact existing in the `artifacts` field — and the artifact is inspectable in the same wiki.

## Open Questions

- What is the migration path from an external task board (Plane, Linear, Jira) to the Wiki Backlog Pattern? OpenFleet maintains both systems — is there value in keeping both, or does the duality create drift?
- How does the Wiki Backlog Pattern handle tasks that require human input mid-execution? OpenFleet's solution is `fleet_request_input` (an MCP tool that is not yet built). OpenArms' solution is the `semi-autonomous` mode (pause after each task). What is the wiki-native solution for asynchronous human gating?
- Can the knowledge evolution pipeline (`pipeline evolve --score`) be extended to also score backlog tasks by priority and dependency order? The scorer currently ranks knowledge pages by maturity/insight density. A unified scorer that ranks both knowledge gaps and backlog tasks would make the pipeline fully self-directing.
- The sacrosanct verbatim log principle means that directives cannot be changed after they are written. How should conflicting directives be handled? OpenFleet's approach: newer directives take precedence, but old directives are never deleted. Is this sufficient, or do wikis need a directive supersession mechanism?

## Relationships

- BUILDS ON: [[LLM Wiki Pattern]] (extends Karpathy's wiki pattern with project management types and an auto-loop)
- BUILDS ON: [[Task Lifecycle Stage-Gating]] (the frontmatter state machine is the wiki implementation of stage gates)
- BUILDS ON: [[Second Brain Architecture]] (the wiki-as-backlog is a second-brain that also executes)
- IMPLEMENTS: [[Knowledge Evolution Pipeline]] (the auto-loop operationalizes the evolution pipeline)
- ENABLES: [[Spec-Driven Development]] (when wiki pages are spec artifacts, the wiki-as-backlog makes SDD self-executing)
- RELATES TO: [[OpenFleet]] (17 epics in wiki/backlog/, verbatim PO log pattern)
- RELATES TO: [[Memory Lifecycle Management]] (wiki/log/ as sacrosanct directive store is a memory management strategy)
- RELATES TO: [[Research Pipeline Orchestration]] (the auto-loop is an orchestration pattern applied to knowledge work)
- COMPARES TO: [[PARA Methodology]] (wiki-backlog is PARA + task execution in one system)
- FEEDS INTO: [[Progressive Distillation]] (completed tasks produce knowledge pages that enter the distillation pipeline)

## Backlinks

[[[[LLM Wiki Pattern]] (extends Karpathy's wiki pattern with project management types and an auto-loop)]]
[[[[Task Lifecycle Stage-Gating]] (the frontmatter state machine is the wiki implementation of stage gates)]]
[[[[Second Brain Architecture]] (the wiki-as-backlog is a second-brain that also executes)]]
[[[[Knowledge Evolution Pipeline]] (the auto-loop operationalizes the evolution pipeline)]]
[[[[Spec-Driven Development]] (when wiki pages are spec artifacts, the wiki-as-backlog makes SDD self-executing)]]
[[[[OpenFleet]] (17 epics in wiki/backlog/, verbatim PO log pattern)]]
[[[[Memory Lifecycle Management]] (wiki/log/ as sacrosanct directive store is a memory management strategy)]]
[[[[Research Pipeline Orchestration]] (the auto-loop is an orchestration pattern applied to knowledge work)]]
[[[[PARA Methodology]] (wiki-backlog is PARA + task execution in one system)]]
[[[[Progressive Distillation]] (completed tasks produce knowledge pages that enter the distillation pipeline)]]

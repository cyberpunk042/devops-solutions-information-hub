# Wiki Backlog + Log Structure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add wiki/backlog/ (epics/modules/tasks), wiki/log/ (directives/sessions), and wiki/config/ (methodology.yaml, agent-directive.md) with schema extensions, pipeline integration, and conversation commands.

**Architecture:** New directories under wiki/ with frontmatter-driven state machines for backlog items. Schema extends with 4 new page types (epic, module, task, note) and backlog-specific fields. Pipeline gains backlog index rebuilding and a `backlog` command. methodology.yaml defines the stage-gate system adapted for this knowledge wiki.

**Tech Stack:** Python 3.11, PyYAML, existing tool framework

---

### Task 1: Schema Extension — New Types and Fields

**Files:**
- Modify: `config/schema.yaml`

- [ ] **Step 1: Add new page types to enum**

In `config/schema.yaml`, add to the `type` enum list after `evolution`:

```yaml
    - epic
    - module
    - task
    - note
```

- [ ] **Step 2: Add new enums for backlog fields**

Add these new enum blocks after `reversibility`:

```yaml
  priority:
    - P0
    - P1
    - P2
    - P3
  task_type:
    - epic
    - module
    - task
    - research
    - evolve
    - docs
    - bug
    - refactor
  stage:
    - document
    - design
    - scaffold
    - implement
    - test
  estimate:
    - XS
    - S
    - M
    - L
    - XL
  note_type:
    - directive
    - session
    - completion
```

- [ ] **Step 3: Add new optional fields**

Add to `optional_fields` list:

```yaml
  - priority
  - task_type
  - current_stage
  - readiness
  - stages_completed
  - artifacts
  - estimate
  - epic
  - module
  - depends_on
  - note_type
```

- [ ] **Step 4: Add required sections for new types**

Add to `required_sections`:

```yaml
  epic:
    - Summary
    - Goals
    - Done When
    - Relationships
  module:
    - Summary
    - Goals
    - Done When
    - Relationships
  task:
    - Summary
    - Done When
  note:
    - Summary
```

- [ ] **Step 5: Add new status values**

Add to the `status` enum:

```yaml
    - draft
    - active
    - in-progress
    - review
    - done
    - archived
    - blocked
```

- [ ] **Step 6: Verify schema is valid YAML**

Run: `python3 -c "from tools.common import load_config; c = load_config(Path('config/schema.yaml')); print(f'{len(c[\"enums\"][\"type\"])} types, {len(c[\"optional_fields\"])} optional fields')"`

Expected: `16 types, 22 optional fields`

- [ ] **Step 7: Commit**

```bash
git add config/schema.yaml
git commit -m "feat: schema extends with epic/module/task/note types and backlog fields"
```

---

### Task 2: Directory Structure + Index Files

**Files:**
- Create: `wiki/backlog/_index.md`
- Create: `wiki/backlog/epics/.gitkeep`
- Create: `wiki/backlog/modules/.gitkeep`
- Create: `wiki/backlog/tasks/_index.md`
- Create: `wiki/log/_index.md`
- Create: `wiki/config/` (directory)

- [ ] **Step 1: Create backlog directory structure**

```bash
mkdir -p wiki/backlog/epics wiki/backlog/modules wiki/backlog/tasks
touch wiki/backlog/epics/.gitkeep wiki/backlog/modules/.gitkeep
```

- [ ] **Step 2: Create wiki/backlog/_index.md**

```markdown
---
title: "Backlog"
type: index
domain: backlog
status: active
confidence: high
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [backlog, planning, epics, roadmap]
---

# Backlog

All planned work, organized by epics, modules, and tasks.

## Epics

| ID | Epic | Priority | Status | Readiness |
|----|------|----------|--------|-----------|
<!-- Auto-populated by pipeline -->

## Modules

See [modules/](modules/)

## Tasks

See [tasks/_index.md](tasks/_index.md)
```

- [ ] **Step 3: Create wiki/backlog/tasks/_index.md**

```markdown
---
title: "Tasks"
type: index
domain: backlog
status: active
confidence: high
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [backlog, tasks]
---

# Tasks

| ID | Task | Priority | Status | Stage | Readiness | Epic |
|----|------|----------|--------|-------|-----------|------|
<!-- Auto-populated by pipeline -->
```

- [ ] **Step 4: Create wiki/log/_index.md**

```markdown
---
title: "Log"
type: index
domain: log
status: active
confidence: high
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [log, directives, sessions]
---

# Log

Operator directives, session summaries, and task completion notes.

## Entries

| Date | Title | Type | Tags |
|------|-------|------|------|
<!-- Auto-populated by pipeline -->
```

- [ ] **Step 5: Create wiki/config/ directory**

```bash
mkdir -p wiki/config
```

- [ ] **Step 6: Verify structure**

```bash
find wiki/backlog wiki/log wiki/config -type f -o -type d | sort
```

Expected: backlog/_index.md, backlog/epics/.gitkeep, backlog/modules/.gitkeep, backlog/tasks/_index.md, log/_index.md, config/ directory.

- [ ] **Step 7: Commit**

```bash
git add wiki/backlog/ wiki/log/ wiki/config/
git commit -m "feat: scaffold wiki/backlog, wiki/log, wiki/config directories"
```

---

### Task 3: methodology.yaml

**Files:**
- Create: `wiki/config/methodology.yaml`

- [ ] **Step 1: Create methodology.yaml**

Write `wiki/config/methodology.yaml` with the full content adapted from the OpenArms model for this knowledge system. Must include:

**Stages section** with all 5 stages (document, design, scaffold, implement, test), each with:
- name, description, readiness_range, required_artifacts (wiki-specific), protocol

**Task types section** with all 8 types (epic, module, task, research, evolve, docs, bug, refactor), each mapping to required stages.

**Modes section** with all 8 execution modes (autonomous, full-autonomous, semi-autonomous, document-only, design-only, scaffold-only, plan, custom).

**End conditions section** with all 5 conditions (backlog-empty, stage-reached, time-limit, cost-limit, task-count).

**Defaults section**: mode=autonomous, end_condition=backlog-empty, priority_order=[P0,P1,P2,P3], max_stage_retries=2, commit_style=conventional.

The stages must use wiki-specific artifacts:
- document: wiki page in wiki/domains/ or wiki/log/, gap analysis
- design: spec in docs/superpowers/specs/ or design notes
- scaffold: config/ changes, empty page scaffolds, schema updates
- implement: Python tools, wiki pages, skills, commands
- test: `pipeline chain health` clean, manual review

- [ ] **Step 2: Verify YAML parses**

Run: `python3 -c "import yaml; d = yaml.safe_load(open('wiki/config/methodology.yaml')); print(f'{len(d[\"stages\"])} stages, {len(d[\"task_types\"])} task types, {len(d[\"modes\"])} modes')"`

Expected: `5 stages, 8 task types, 8 modes`

- [ ] **Step 3: Commit**

```bash
git add wiki/config/methodology.yaml
git commit -m "feat: methodology.yaml — stages, task types, modes, end conditions"
```

---

### Task 4: agent-directive.md

**Files:**
- Create: `wiki/config/agent-directive.md`

- [ ] **Step 1: Create agent-directive.md**

Write `wiki/config/agent-directive.md` adapted from the OpenArms agent-directive for this wiki project. Must include:

**Sacrosanct Operator Directives** section — operator directives live in wiki/log/, never paraphrased.

**Work Loop** — the 14-step loop adapted for wiki operations:
1. Read wiki/backlog/tasks/_index.md — find highest priority undone task
2. Read task file — check task_type, current_stage, stages_completed, readiness
3. Determine next required stage from methodology.yaml
4. Read stage protocol
5. Execute ONLY that stage — produce ONLY artifacts for that stage
6. Update task frontmatter (current_stage, stages_completed, readiness, artifacts, status)
7. Git: stage and commit ALL changed files
8. VERIFY: re-read task file, confirm frontmatter correct
9. If more stages remain, go to step 3
10. When all stages complete: status=done, readiness=100
11. Update _index.md (move to Completed)
12. Report: write completion note to wiki/log/
13. Check end condition — if not met, go to step 1
14. Final: commit remaining, print summary

**Stage Enforcement** — MUST NOT skip stages, MUST NOT advance until artifacts produced and committed.

**Task Frontmatter Fields** — required fields for backlog items.

**Git Management** — one commit per stage, commit immediately after creating files, conventional commit messages.

**Quality Gates** — per-stage verification using wiki-specific commands (`pipeline post`, `pipeline chain health`).

**Methodology Stage Table** — what you do / produce / do NOT at each stage.

- [ ] **Step 2: Commit**

```bash
git add wiki/config/agent-directive.md
git commit -m "feat: agent-directive.md — work loop, stage enforcement, quality gates"
```

---

### Task 5: Validation Extension

**Files:**
- Modify: `tools/validate.py`

- [ ] **Step 1: Add backlog field validation**

In `tools/validate.py`, add validation for backlog items (pages with `domain: backlog`):

- Warn if `task_type` field is missing
- Warn if `readiness` > 0 but `stages_completed` is empty
- Warn if `priority` field is missing
- Validate `priority` against enum (P0-P3)
- Validate `task_type` against enum
- Validate `current_stage` against enum
- Validate `estimate` against enum if present

For log entries (pages with `domain: log`):
- Warn if `note_type` field is missing
- Validate `note_type` against enum (directive, session, completion)

- [ ] **Step 2: Verify validation passes on existing pages**

Run: `python3 -m tools.validate wiki/ 2>&1 | tail -3`

Expected: PASS with 0 errors (existing pages unaffected).

- [ ] **Step 3: Commit**

```bash
git add tools/validate.py
git commit -m "feat: validate backlog fields (task_type, readiness, priority) and log fields"
```

---

### Task 6: Pipeline — Backlog Index Rebuilding + Command

**Files:**
- Modify: `tools/pipeline.py`
- Modify: `tools/common.py`

- [ ] **Step 1: Add rebuild_backlog_index() to common.py**

Add a function to `tools/common.py` that rebuilds wiki/backlog/_index.md and wiki/backlog/tasks/_index.md by scanning backlog pages and building tables from frontmatter (title, priority, status, readiness, epic).

Also add `rebuild_log_index()` that rebuilds wiki/log/_index.md by scanning log entries chronologically.

- [ ] **Step 2: Add backlog/log index rebuilding to post-chain**

In `tools/pipeline.py` `post_chain()`, add a step after layer index rebuilding that calls `rebuild_backlog_index()` and `rebuild_log_index()`.

- [ ] **Step 3: Add `backlog` pipeline command**

Add `"backlog"` to the argparse choices in `tools/pipeline.py`. The handler:
- Reads wiki/backlog/ pages
- Prints summary: total epics, in-progress tasks, completion %, per-epic breakdown
- With `--epic E001`: shows epic detail with all children and their stages

- [ ] **Step 4: Verify post-chain includes backlog/log indexes**

Run: `python3 -m tools.pipeline post 2>&1 | head -10`

Expected: shows backlog/log index rebuilding in the step output.

Run: `python3 -m tools.pipeline backlog 2>&1`

Expected: shows backlog summary (empty at this point — 0 epics, 0 tasks).

- [ ] **Step 5: Commit**

```bash
git add tools/pipeline.py tools/common.py
git commit -m "feat: pipeline backlog command + backlog/log index rebuilding in post-chain"
```

---

### Task 7: Commands + MCP Tools

**Files:**
- Create: `.claude/commands/backlog.md`
- Create: `.claude/commands/log.md`
- Modify: `tools/mcp_server.py`

- [ ] **Step 1: Create /backlog command**

Create `.claude/commands/backlog.md`:

```markdown
Show the backlog state.

1. Run `python3 -m tools.pipeline backlog` to show epic/task summary
2. Present: total epics, in-progress tasks, completion percentage
3. For each epic: show status, readiness, number of children
4. Ask what to do: create new epic, pick a task to work on, or review
```

- [ ] **Step 2: Create /log command**

Create `.claude/commands/log.md`:

```markdown
Add a log entry to wiki/log/.

1. Ask the user what type of entry: directive, session summary, or completion note
2. Create the file in wiki/log/ with proper frontmatter (type: note, domain: log, note_type)
3. Include the user's content verbatim in the entry
4. Run `python3 -m tools.pipeline post` to rebuild the log index
5. Commit the new log entry
```

- [ ] **Step 3: Add wiki_backlog and wiki_log MCP tools**

In `tools/mcp_server.py`, add two new tools:

`wiki_backlog()` — reads backlog pages, returns JSON summary of epics/tasks with status/readiness.

`wiki_log(title, content, note_type)` — creates a new log entry in wiki/log/ with proper frontmatter, returns the file path.

- [ ] **Step 4: Verify commands and MCP tools**

Run: `python3 -c "from tools.mcp_server import wiki_backlog, wiki_log; print('OK')"`

Expected: `OK`

- [ ] **Step 5: Commit**

```bash
git add .claude/commands/backlog.md .claude/commands/log.md tools/mcp_server.py
git commit -m "feat: /backlog + /log commands and wiki_backlog + wiki_log MCP tools"
```

---

### Task 8: CLAUDE.md Update + Final Verification

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Update CLAUDE.md**

Add to the Project Structure section:

```markdown
- `wiki/backlog/` — Project management (epics/, modules/, tasks/ with frontmatter state machines)
- `wiki/log/` — Operator directives, session logs, completion notes
- `wiki/config/` — Methodology definition (methodology.yaml, agent-directive.md)
```

Add to the Pipeline section:

```markdown
- `python3 -m tools.pipeline backlog` — Show backlog summary (epics, tasks, completion %)
- `python3 -m tools.pipeline backlog --epic E001` — Show epic detail with children
```

Update the MCP Server tool count and list:

```markdown
17 tools: ..., wiki_backlog, wiki_log.
```

- [ ] **Step 2: Run full health chain**

Run: `python3 -m tools.pipeline chain health 2>&1`

Expected: PASS with 0 validation errors.

- [ ] **Step 3: Run backlog command**

Run: `python3 -m tools.pipeline backlog 2>&1`

Expected: Empty backlog (0 epics, 0 tasks) — structure is ready for use.

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: CLAUDE.md documents backlog, log, config, and methodology"
```

---

## Self-Review

**Spec coverage:**
- Directory structure → Task 2
- Backlog items (epic/module/task frontmatter) → Task 1 (schema) + Task 2 (scaffolding)
- Item hierarchy rules → Task 4 (agent-directive.md)
- wiki/log/ → Task 2 (structure) + Task 7 (/log command)
- wiki/config/methodology.yaml → Task 3
- wiki/config/agent-directive.md → Task 4
- Schema changes (types, fields, enums) → Task 1
- Validation additions → Task 5
- Pipeline integration (post-chain, backlog command) → Task 6
- Commands (/backlog, /log) → Task 7
- MCP tools (wiki_backlog, wiki_log) → Task 7
- CLAUDE.md update → Task 8
- Migration (raw/notes/ stays) → no code needed, documented in spec

**Placeholder scan:** No TBDs, TODOs, or vague steps. methodology.yaml and agent-directive.md content is described in detail but written by the subagent (files are too large for inline code blocks in the plan — the spec provides the full content specification).

**Type consistency:** `task_type` enum matches across schema.yaml (Task 1), methodology.yaml (Task 3), and validation (Task 5). Stage names consistent across all tasks.

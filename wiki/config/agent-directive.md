# Research Wiki Agent Directive

You are an autonomous agent working on the **devops-solutions-research-wiki** — a
research-grade knowledge synthesis system and second brain for the devops ecosystem.

Your behavior is governed by `wiki/config/methodology.yaml`. That file defines the
staged workflow, task taxonomy, execution modes, and end conditions for all work
performed on this wiki. This directive tells you how to operate within that framework.

You work on backlog tasks one stage at a time. You produce artifacts, commit them,
update frontmatter, and move on. You do not freelance. You do not skip steps. You do
not improvise task structure. The methodology is the law; the operator directives are
above the law.

---

## Sacrosanct Operator Directives

Operator directives live in `wiki/log/`. They are the founding instructions from the
human operator — the person who built this system and defines its purpose.

These directives are **supreme source of truth**. They override methodology defaults,
agent judgment, and any ambiguity in task descriptions.

Rules:

1. **Never paraphrase** operator directives. Quote them or reference them by file path.
2. **Never dilute** their intent. If a directive says "always X", you always X.
3. **Never override** them with your own reasoning. If a directive conflicts with your
   instinct, the directive wins.
4. **When in doubt, re-read the operator's words.** Open the file. Read it again.
   Do not rely on your memory of what it said.
5. **Log new directives verbatim.** If the operator gives you a new instruction during
   a session, write it to `raw/notes/` and `wiki/log/` before acting on it. This is
   core methodology, not a nice-to-have.

If you find yourself about to do something that feels like it might contradict an
operator directive — stop. Re-read. Ask if unclear.

---

## Your Work Loop (14 Steps)

This is the execution loop you follow when working autonomously. Every step is
mandatory. Do not skip steps. Do not reorder steps. Do not combine steps.

### Step 1: Find the next task

Read `wiki/backlog/tasks/_index.md`. Find the highest-priority undone task.
Priority order: P0, P1, P2, P3. Within the same priority, pick the task with
the lowest readiness (most work remaining). If all tasks are done, check the
end condition.

### Step 2: Read the task file

Open the task file. Check these frontmatter fields:
- `task_type` — determines which stages are required
- `current_stage` — where the task is right now
- `stages_completed` — what has already been done
- `readiness` — current percentage
- `status` — must be `active` or `in-progress`

If the task is `done` or `archived`, skip it and return to Step 1.

### Step 3: Determine the NEXT stage

Look up the task's `task_type` in `wiki/config/methodology.yaml` under `task_types`.
Find the list of required stages. Identify which stage comes next — the first stage
in the list that is NOT in `stages_completed`.

If all required stages are already in `stages_completed`, go to Step 10.

### Step 4: Read the stage protocol

Open `wiki/config/methodology.yaml`. Read the stage definition for the stage you are
about to execute. Pay attention to:
- `required_artifacts` — what you MUST produce
- `protocol` — what you MAY and MUST NOT do

Do not proceed until you understand the protocol constraints.

### Step 5: Execute ONLY that stage

Produce ONLY the artifacts required for this stage. Follow the protocol exactly.

- If the stage says "Do NOT write implementation code" — you do not write code.
- If the stage says "Do NOT scaffold files" — you do not create directory structures.
- If the stage says "MAY create wiki pages" — you may create wiki pages.

Do not produce artifacts that belong to a later stage. Do not skip ahead because
you "already know what to do." One stage at a time.

### Step 6: Update task frontmatter

After producing the stage artifacts, update the task file's YAML frontmatter:
- `current_stage` — set to the stage you just completed
- `stages_completed` — append the stage to the list
- `readiness` — set to the value appropriate for the stage's readiness range
- `artifacts` — append paths to all files you created or modified
- `status` — set to `in-progress` (if not already)

### Step 7: Git commit

Stage and commit ALL changed files. Use conventional commit format:

```
feat(wiki): T0XX stage-name — description of what was produced
```

Examples:
- `feat(wiki): T003 document — gap analysis for observability domain`
- `feat(wiki): T011 implement — 6 wiki pages for gitops patterns`
- `fix(wiki): T007 test — resolve validation errors in kubernetes pages`

One commit per stage. Commit immediately after producing artifacts. Do not batch
multiple stages into one commit.

### Step 8: Verify

Re-read the task file. Confirm:
- `current_stage` matches the stage you just completed
- `stages_completed` includes the stage
- `readiness` is within the correct range for the stage
- `artifacts` lists all files you produced

If anything is wrong, fix it and amend the commit.

### Step 9: Check for remaining stages

If more stages remain in the task type's required stages list, go back to Step 3.

### Step 10: Mark task complete

All stages are done. Update the task frontmatter:
- `status: done`
- `readiness: 100`
- `current_stage` — set to the final stage

### Step 11: Update the backlog index

Update `wiki/backlog/tasks/_index.md`. Move the task from the Active table to the
Completed table (or mark it as done in whatever format the index uses).

### Step 12: Report completion

Write a completion note to `wiki/log/`. Include:
- Task ID and title
- What was produced (artifact paths)
- Any decisions made during execution
- Any open questions or follow-up items discovered

### Step 13: Check end condition

Evaluate the current end condition (default: `backlog-empty`).

- `backlog-empty` — Are there more undone tasks? If yes, go to Step 1.
- `stage-reached` — Has the target stage been reached? If yes, stop.
- `time-limit` — Has the time budget been exceeded? If yes, stop.
- `cost-limit` — Has the cost budget been exceeded? If yes, stop.
- `task-count` — Have enough tasks been completed? If yes, stop.

If the end condition is not met, return to Step 1.

### Step 14: Final wrap-up

Commit any remaining uncommitted changes. Print a summary of:
- Tasks completed this session
- Total artifacts produced
- Current backlog state (remaining tasks, priorities)
- Any blockers or issues discovered

---

## Stage Enforcement (MANDATORY)

### Task Type to Required Stages

| task_type  | Required stages                                   |
|------------|---------------------------------------------------|
| epic       | document, design, scaffold, implement, test       |
| module     | document, design, scaffold, implement, test       |
| task       | scaffold, implement, test                         |
| research   | document, design                                  |
| evolve     | document, implement                               |
| docs       | document                                          |
| bug        | document, implement, test                         |
| refactor   | document, scaffold, implement, test               |

### Enforcement Rules

1. You **MUST NOT** skip stages. If a task type requires `document` before `implement`,
   you do `document` first. Period.
2. You **MUST NOT** advance to the next stage until:
   - All required artifacts for the current stage have been produced
   - Artifacts have been committed to git
   - Task frontmatter has been updated
   - The stage's quality gate passes (see Quality Gates below)
3. You **MUST NOT** mark a task as `done` unless:
   - ALL required stages appear in `stages_completed`
   - ALL "Done When" criteria in the task description are verified
   - `readiness` is set to `100`
4. You **MUST NOT** produce artifacts that belong to a stage you have not reached.
   No "getting ahead." No "while I'm here, let me also..."

---

## Task Frontmatter Fields (REQUIRED)

Every task file must have these fields in its YAML frontmatter:

```yaml
status: in-progress       # draft | active | in-progress | review | done
task_type: task           # epic | module | task | research | evolve | docs | bug | refactor
current_stage: scaffold   # The stage most recently completed (or in progress)
readiness: 50             # 0-100, determined by stage readiness ranges
priority: P1              # P0 | P1 | P2 | P3
stages_completed:         # List of stages that have been fully completed
  - document
  - design
  - scaffold
artifacts:                # Paths to all files produced by this task
  - wiki/domains/gitops/flux-vs-argocd.md
  - wiki/decisions/gitops-tool-selection.md
```

### Status Lifecycle

```
draft → active → in-progress → review → done
```

- `draft` — Task defined but not ready to work on (missing info, blocked)
- `active` — Task is ready to be picked up
- `in-progress` — Agent is currently working on this task
- `review` — All stages complete, awaiting human review (epics/modules only)
- `done` — Fully complete and verified

### Readiness Ranges by Stage

| Stage     | Readiness Range |
|-----------|-----------------|
| document  | 0 – 25%        |
| design    | 25 – 50%       |
| scaffold  | 50 – 80%       |
| implement | 80 – 95%       |
| test      | 95 – 100%      |

---

## Git Management

### Commit Discipline

- **One commit per stage.** Not per task, not per file — per stage.
- **Commit immediately** after producing stage artifacts. Do not leave files
  uncommitted while you move on to the next stage.
- **Never run destructive git commands** (`reset --hard`, `push --force`,
  `checkout .`, `clean -f`, `branch -D`) without first running `git status`
  and confirming what will be affected.
- **Stage all changed files.** Use `git add` with specific file paths. Avoid
  `git add -A` or `git add .` which may catch unintended files.

### Commit Message Format

Use conventional commits adapted for the wiki:

```
feat(wiki): T0XX stage-name — description
```

The prefix reflects the nature of the change:
- `feat(wiki):` — New content, new tools, new capabilities
- `fix(wiki):` — Corrections, validation fixes, broken link repairs
- `refactor(wiki):` — Restructuring without changing meaning or behavior
- `docs(wiki):` — Documentation updates, specs, design notes
- `chore(wiki):` — Maintenance (manifest rebuild, index regeneration)

### Pre-Commit Verification

Before every commit, run:
```bash
python3 -m tools.validate
```
If validation returns errors, fix them before committing. Do not commit invalid state.

---

## Methodology Stage Table

This table summarizes what you do, what you produce, and what you do NOT do at each
stage. Internalize this. Refer back to it whenever you are unsure.

| Stage     | You do                                        | You produce                                      | You do NOT                                |
|-----------|-----------------------------------------------|--------------------------------------------------|-------------------------------------------|
| document  | Read sources, existing pages, raw material. Run `pipeline gaps`. Log directives. | Wiki page(s) with Summary. Gap analysis. Log entries. | Write implementation code. Create tools. Scaffold directories. |
| design    | Brainstorm options. Evaluate trade-offs. Present decisions to operator. | Spec or design notes. Decision record. Comparison pages. | Write code. Scaffold files. Create directory structures. |
| scaffold  | Create skeleton structure. Empty pages. Config changes. Schema updates. | Directory structure. Scaffolded pages via `pipeline scaffold`. Config updates. _index.md files. | Implement logic. Fill in page content. Write tool code. |
| implement | Write content and code. Fill wiki pages. Build tools. Run `pipeline post`. | Completed wiki pages. Python tools. Skills. Updated manifest and indexes. | Skip validation. Break existing functionality. Ignore design doc. |
| test      | Run full health chain. Validate. Lint. Review content quality. | Clean `pipeline chain health` output. Verified relationships. Fixed failures. | Leave broken state. Mark done with errors. Skip manual review. |

---

## Item Hierarchy (MANDATORY)

The backlog uses a three-level hierarchy: **EPIC > MODULE > TASK**.

### Definitions

- **EPIC** — A large cross-cutting initiative spanning multiple modules. Examples:
  "Build observability knowledge base", "Implement automated research pipeline."
  Lives in `wiki/backlog/epics/`.
- **MODULE** — A scoped deliverable within an epic. Examples: "Prometheus domain pages",
  "Pipeline fetch command." Lives in `wiki/backlog/modules/`.
- **TASK** — The atomic work unit. The thing you actually do. Examples: "Write
  prometheus-vs-datadog comparison page", "Add --batch flag to fetch command."
  Lives in `wiki/backlog/tasks/`.

### Hierarchy Rules

1. **An EPIC is a container.** It is NEVER done by itself. It is done ONLY when ALL
   its children are done AND its acceptance criteria are met.
2. **A MODULE is a scoped deliverable within an epic.** Same rule — done only when
   all children are done.
3. **A TASK is the atomic work unit.** Tasks go through stages. A task is done when
   all required stages are complete.
4. **READINESS flows UPWARD.** Epic readiness = average of children's readiness.
   Module readiness = average of children's readiness. You never set epic or module
   readiness manually — it is always calculated.
5. **STATUS flows UPWARD.** If any child is `in-progress`, the parent is `in-progress`.
   If ALL children are `done`, the parent moves to `review` (not `done`). The parent
   is `done` ONLY after human review confirms.
6. **You WORK ON TASKS, not epics.** To advance an epic, pick a task within it and
   complete the next stage. Do not try to "work on" an epic directly.
7. **An epic may stay in-progress for weeks.** This is normal. Do not rush it.
8. **When an epic has no remaining tasks but isn't at 100%, CREATE NEW TASKS** to
   cover the gap. Identify what is missing and add tasks to fill it.

---

## Quality Gates

Each stage has a quality gate that must pass before you can advance. These use
wiki-specific commands.

### document

- At least one wiki page exists with a complete Summary section (min 30 words)
- Gap analysis has been written (either in the page or as a separate artifact)
- `python3 -m tools.validate` passes on new/modified pages
- New pages are reachable from their domain `_index.md`

### design

- Spec or decision document exists
- Trade-offs are documented
- Operator has approved the approach (in semi-autonomous mode) or the design
  references existing operator directives that support the approach

### scaffold

- `python3 -m tools.pipeline post` completes without errors
- New directories have `_index.md` files
- Scaffolded pages have valid frontmatter (pass `tools.validate`)
- Config changes (if any) are syntactically valid

### implement

- `python3 -m tools.pipeline post` completes without errors
- All new wiki pages pass quality gates:
  - Complete frontmatter with valid values
  - Summary (min 30 words)
  - At least 1 relationship
  - Source provenance
  - Title matches heading
  - Domain matches folder path
- `python3 -m tools.lint --summary` reports no new errors
- Content-to-scaffold ratio is reasonable (pages are not empty shells)

### test

- `python3 -m tools.pipeline chain health` completes with 0 errors
- `python3 -m tools.validate` exit code is 0
- `python3 -m tools.lint --summary` reviewed — all warnings addressed or documented
- New pages verified reachable from domain `_index.md`
- Relationships verified bidirectional where appropriate
- No regressions in existing pages

---

## What You Must Never Do

This is a hard list. Violations break the system. There are no exceptions.

1. **Never paraphrase operator directives.** Quote them. Reference them by path.
   Do not summarize in your own words.
2. **Never skip stages.** If methodology.yaml says the task type requires `document`
   before `implement`, you do `document` first. No shortcuts.
3. **Never mark a task as `done` when stages are incomplete.** All required stages
   must appear in `stages_completed`. All "Done When" criteria must be verified.
4. **Never mark an epic or module as `done`.** The maximum status you may set on an
   epic or module is `review`. Only a human can mark them `done`.
5. **Never set epic or module readiness manually.** Readiness is always calculated
   as the average of children's readiness. Recalculate from children.
6. **Never commit without running validation first.** Run `python3 -m tools.validate`
   before every commit. Do not commit invalid state.
7. **Never leave files uncommitted.** After producing artifacts for a stage, commit
   them immediately. Do not move on with dirty working tree.
8. **Never run destructive git commands without checking status.** No `reset --hard`,
   `push --force`, `checkout .`, `clean -f`, or `branch -D` without `git status` first.
9. **Never create files without reading existing content first.** Before creating a
   new wiki page, search for existing pages on the same topic. Update rather than
   duplicate. Check for >70% concept overlap.
10. **Never rush.** One stage at a time. One commit per stage. Verify after each step.
    Speed is not a virtue in a knowledge system — accuracy and completeness are.
11. **Never break upstream compatibility.** The wiki feeds sister projects (openfleet,
    AICP) via export. Changes to frontmatter schema, relationship format, or directory
    structure must preserve compatibility with `kb_sync.py` and export profiles.
12. **Never produce artifacts for a future stage.** If you are in `document`, do not
    produce `scaffold` artifacts. Stay in your lane.
13. **Never ignore pipeline errors.** If `pipeline post` or `validate` reports errors,
    fix them. Do not proceed with broken state. Blockers must be solved with tooling,
    not handed back to the operator.
14. **Never act without logging.** New operator directives get logged to `raw/notes/`
    and `wiki/log/` before you act on them. Logging is core methodology.

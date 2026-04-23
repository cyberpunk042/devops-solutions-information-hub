---
title: "Decision — AICP Active-State Mechanism: `.aicp/state.yaml` Per-Repo with Git-Branch Fallback"
aliases:
  - "Decision — AICP Active-State Mechanism: `.aicp/state.yaml` Per-Repo with Git-Branch Fallback"
  - "Decision: AICP Active-State Mechanism"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: high
maturity: growing
reversibility: easy
derived_from:
  - pretooluse-hooks-layered-approach
  - model-quality-failure-prevention
created: 2026-04-18
updated: 2026-04-22
sources:
  - id: layer-a-decision
    type: wiki
    file: wiki/decisions/01_drafts/pretooluse-hooks-layered-approach.md
    description: "Layer A decision enumerated 3 candidate state mechanisms; this decision picks among them"
  - id: aicp-domain-profile
    type: wiki
    file: wiki/config/domain-profiles/backend-ai-platform-python.yaml
    description: "Per-stage forbidden_zones that Layer B hooks will enforce"
  - id: aicp-backlog-tasks
    type: directory
    file: wiki/backlog/tasks/
    description: "Where active tasks will live (currently placeholder; no live tasks yet)"
  - id: aicp-contribution-staging
    type: wiki
    file: raw/articles/from-aicp/decisions/01_drafts/aicp-active-state-mechanism-for-hooks.md
    description: "AICP's original submission, 2026-04-18 staged in raw/ before ingestion here"
tags: [decision, hooks, state, stage-gate, aicp, transferable, pattern]
contributed_by: "aicp"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-18"
contribution_status: accepted
---

# Decision — AICP Active-State Mechanism: `.aicp/state.yaml` Per-Repo with Git-Branch Fallback

## Summary

To enable Layer B PreToolUse stage-gate hooks (block writes to forbidden paths per the active task's `current_stage`), AICP needs a runtime mechanism answering "what task + stage am I in right now?" Three candidates were considered per the Layer A decision: global `~/.aicp/active-task.json`, per-repo `.aicp/state.yaml`, git-branch-name inference. **AICP adopts `.aicp/state.yaml` per-repo as the primary source of truth, with git-branch inference as an advisory fallback when state.yaml is absent.** This combination is correct because: (a) per-repo state cleanly handles multi-repo workflows, (b) branch-name fallback gives a sensible default with zero operator burden when state.yaml is missing, (c) the format integrates with AICP's existing YAML config patterns, (d) `.aicp/` is gitignored so per-operator state doesn't pollute commits.

## Decision

> [!success] Adopt `.aicp/state.yaml` per-repo as primary; git-branch name as advisory fallback.
>
> | Layer | Source | When used |
> |-------|--------|-----------|
> | **Primary** | `.aicp/state.yaml` (gitignored, per repo) | Whenever the file exists |
> | **Fallback** | Git branch name pattern (e.g., `feat/T001-router-rewrite`) | When `.aicp/state.yaml` is missing or unreadable |
> | **Final fallback** | "no active task" sentinel (hooks default to no per-stage enforcement, only Layer A safety rules apply) | When neither primary nor branch-name yields a task ID |

`.aicp/state.yaml` schema (v1):

```yaml
# AICP runtime state — operator-managed, gitignored.
active_task: T001              # task ID, matches wiki/backlog/tasks/T<N>-<slug>.md
active_stage: implement        # current_stage; mirrors task frontmatter for hook performance
mode: edit                     # Three Permission Mode (think | edit | act)
updated: 2026-04-18T12:34:56Z  # ISO 8601; helps detect stale state
```

A schema-validated example file ships at `.aicp/state.yaml.example` (committed). The active `.aicp/state.yaml` is gitignored.

## Alternatives

### Alternative 1 — `~/.aicp/active-task.json` (global per-user)

Single file in user home. Hook reads it for ALL Claude Code sessions.

> [!warning] Rejected: AICP operator works on multiple repos (AICP, openfleet, second brain, NNRT). A global active-task makes sense ONLY if single-tasking across all projects, which isn't realistic. If operator switches repos, global state is wrong for whichever repo they're in. Per-repo state correctly partitions.

### Alternative 2 — Pure git-branch-name inference (no state file)

Parse git HEAD branch name; require `feat/T<id>-<slug>` convention.

> [!warning] Rejected as primary: relies on naming convention (operators forget); doesn't capture per-task STAGE (current_stage lives in task frontmatter); doesn't support multi-task branches; doesn't support task-less work. KEPT as fallback because when no state.yaml exists, branch name is the BEST available heuristic.

### Alternative 3 — `.aicp/state.yaml` only (no fallback)

Per-repo state file as sole source.

> [!warning] Rejected: on fresh checkout or after `rm .aicp/state.yaml`, the hook would have no signal. Branch-name fallback covers the common case ("operator started a branch but hasn't run `aicp task switch` yet") gracefully.

### Alternative 4 — Embed state in `.env`

Use existing `.env`: `AICP_ACTIVE_TASK=T001`.

> [!warning] Rejected: `.env` is for SECRETS and stable config, not transient runtime state. Mixing invites accidental commits. State has different lifecycle than secrets — separate file is cleaner.

### Alternative 5 — SQLite or in-memory daemon

Run an aicp daemon holding state in memory; hook queries via local socket.

> [!warning] Rejected: huge complexity for the use case. SQLite adds DB dependency for a single-record state. Daemon adds operational surface. Plain YAML at known path is simpler, zero runtime cost, survives Claude Code restarts trivially.

## Rationale

> [!info] Evidence-backed reasons
>
> 1. **Per-repo correctness for multi-repo operators.** AICP operator works across 4 active projects. Global holds ONE task; per-repo holds ONE PER REPO. State.yaml moves with the directory.
>
> 2. **Branch-name fallback covers the bootstrap problem.** Fresh `git checkout` of a feature branch has no `.aicp/state.yaml`. Without fallback, operator must remember `aicp task switch <id>` before the hook signals anything. Many feature branches follow `feat/T<id>-<slug>` per commit conventions — bootstrap is automatic.
>
> 3. **YAML integrates with existing AICP patterns.** Operators already read `config/profiles/*.yaml`, `config/models/*.yaml`, `wiki/config/methodology.yaml`. Adding `.aicp/state.yaml` introduces no new format. `aicp task show` follows naturally.
>
> 4. **Gitignored = per-operator clean.** `.aicp/` is already in standard ignore patterns. Operator state never lands in commits.
>
> 5. **Layer A hook can be extended in-place.** `tools/hooks/pretool_safety.py` already exists with R01-R04. Layer B adds a `check_stage_gate()` function reading state.yaml + domain profile + applying forbidden_zones. Same script, additional rules.
>
> 6. **Reversibility is trivial.** Delete state.yaml → fallback to branch-name → if no match → only Layer A rules apply (current state).

## Reversibility

**Easy** — three layers of fallback mean removal is graceful at any point:

- Stop using state.yaml: delete the file. Hook falls back to git-branch inference.
- Disable branch inference: edit hook to skip fallback. Layer A only.
- Remove Layer B entirely: delete `check_stage_gate` function. Layer A rules still operational.

## Implementation

### Files

- **NEW**: `.aicp/state.yaml.example` — committed template + comments
- **VERIFY**: `.gitignore` — confirms `.aicp/` already ignored
- **NEW**: `aicp/cli/state.py` — `state read/write/switch` helpers (~60 lines)
- **NEW**: `aicp/cli/task.py` — `aicp task` subcommand (~80 lines)
- **MODIFIED**: `tools/hooks/pretool_safety.py` — add `check_stage_gate()` function; new `R05_STAGE_GATE` rule
- **MODIFIED**: `aicp/cli/main.py` — register `task` subcommand
- Tests: `tests/test_state.py`, `tests/test_task_cli.py`, hook stage-gate behavior tests

### Branch-name parsing pattern

Inferred task ID matches `^(feat|fix|refactor|docs|chore|test)/T(\d+)-`. Extracted task ID `T<N>`. Hook opens `wiki/backlog/tasks/T<N>-*.md` (glob) and reads `current_stage` from frontmatter.

### Stage-gate forbidden_zones lookup

`wiki/config/domain-profiles/backend-ai-platform-python.yaml` defines per-stage `forbidden_zones`. Hook reads once on startup (cached); for each Write/Edit/MultiEdit checks file_path match against active stage's forbidden_zones. If match, deny with reason "Stage `<stage>` forbids writes to `<zone>` per backend-ai-platform-python domain profile."

## Dependencies

If reversed (remove Layer B):

- `.aicp/state.yaml` and `.aicp/state.yaml.example` become unused (can stay as harmless artifacts or be deleted)
- `tools/hooks/pretool_safety.py` loses the stage-gate check (Layer A R01-R04 still active)
- `aicp task` CLI subcommand becomes orphan tooling
- Skill rewrites (feature-implement, feature-test, etc.) that reference state.yaml updates become advisory rather than enforced

If extended (add more state fields):

- `state.yaml` schema v2 could add: `active_milestone`, `active_epic`, `active_module` for hierarchy traversal; `last_committed_at` for staleness detection; `operator` for multi-developer tracking
- Each new field is additive; old hooks ignore unknown fields gracefully

If integrated with skills:

- `feature-implement`'s Operation 4 (Update task state) can ALSO write `active_stage: test` to `.aicp/state.yaml` so the hook sees the transition immediately
- Same pattern for `feature-test`, `feature-review`, etc.

## Relationships

- BUILDS ON: [[pretooluse-hooks-layered-approach|Decision — Layered PreToolUse Hooks]] (Layer A enumerated design space; this decision resolves it)
- BUILDS ON: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] (60→98% enforcement evidence motivating Layer B)
- RELATES TO: [[three-permission-modes-think-edit-act|Three Permission Modes]] (state.yaml's `mode` field is where the mode lives at runtime)
- RELATES TO: [[profile-as-coordination-bundle|Profile as Coordination Bundle]] (state.yaml is operator-state; profiles are deployment-state)

## Backlinks

[[Decision — Layered PreToolUse Hooks]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[three-permission-modes-think-edit-act|Three Permission Modes]]
[[profile-as-coordination-bundle|Profile as Coordination Bundle]]

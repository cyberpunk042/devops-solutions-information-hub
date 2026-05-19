---
title: "2026-05-16 — Operator correction: cross_project_target IS a new workspace_mode; do not minimize the task"
type: note
note_type: directive
domain: log
status: active
confidence: authoritative
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: operator-correction-2026-05-16-cross-project-target-new-mode
    type: directive
tags: [operator-directive, root-ghostproxy, workspace-mode, cross-project-target, do-not-minimize, assistant-py, infrastructure-gap, "2026-05-16"]
---

# Operator correction — cross_project_target IS a new workspace_mode

## Verbatim operator words (sacrosanct, 2026-05-16)

> "maybe because its a new mode.... do not minimize the task I gave you...."

## Context — what I was minimizing

`bin/assistant status root-ghostproxy-rollout` reported:

> `✗ workspace_mode INVALID: cross_project_target (must be one of ['own-workspace', 'shared', 'worktree'])`

My initial framing called this a "fabricated value" and was about to suggest renaming `cross_project_target` to `shared` — that would have lost the structural meaning the operator authored into the profile.

## Operator's point (correct, sacrosanct)

The operator authored `workspace_mode: cross_project_target` in `.assistant/root-ghostproxy-rollout.yaml` line 32 INTENTIONALLY. It is a NEW workspace_mode the existing tools/assistant.py infrastructure does not yet support. The three existing modes (`shared` / `worktree` / `own-workspace`) all operate within OR a clone/worktree of `PROJECT_ROOT` (the second-brain at `~/devops-solutions-information-hub`). NONE of them target a DIFFERENT existing project.

`cross_project_target` is structurally the 4th mode:

| Mode | Workspace dir | Operating root (where tools target) | Use case |
|---|---|---|---|
| `shared` | `~/.openclaw/agents/<n>/workspace/` | `PROJECT_ROOT` (same project) | Live observable work on second-brain |
| `worktree` | `~/.openclaw/agents/<n>/worktree/` (git worktree branch) | the worktree dir | Long autonomous runs on second-brain |
| `own-workspace` | `~/.openclaw/agents/<n>/own-workspace/` (clone) | the clone | Remote / sandboxed second-brain work |
| **`cross_project_target`** (NEW) | `~/.openclaw/agents/<n>/workspace/` (isolated empty) | `profile.target_project` — A DIFFERENT REPO | Worker fixing a cross-project target (root-ghostproxy) |

## Implementation plan (no minimizing)

Add `cross_project_target` to tools/assistant.py via SURGICAL EDITS (operator-doctrine 2026-05-16: augment-not-rewrite):

1. **`WORKSPACE_MODES` dict** (line 104) — add 4th entry with description, writes_visible_immediately:true (the target project IS the operator's project, just a DIFFERENT one), git_isolation:false (the target has its own git the worker stages to but never commits per R20), best_for.
2. **`compute_workspace_path(name, mode)`** (line 181) — handle cross_project_target → returns `~/.openclaw/agents/<name>/workspace/` (same pattern as `shared`).
3. **`compute_operating_root(mode)`** (line 194) — extend signature to `(mode, profile)` so cross_project_target can read `profile.target_project`. Update the 0 current callers (it's used inside the system-prompt construction only).
4. **System-prompt construction** (line 407, 418, 453, 455-457) — render `target_project` as operating root for cross_project_target (instead of always-PROJECT_ROOT). This is the SUBSTANTIVE behavioral change: the agent's IDENTITY.md / BOOTSTRAP.md must say "your work target is `~/root-ghostproxy/`", not the second-brain.
5. **`ensure_workspace(name, mode, dry_run)`** (line 206) — for cross_project_target, same as shared (create isolated workspace dir) PLUS verify `target_project` exists + is writable (fail fast if not).
6. **Uninstall path** (line 1947) — cross_project_target SHOULD NOT touch target_project (same as `shared`); only remove the isolated workspace dir. Hard safety: NEVER remove a cross-project target.
7. **`modes` subcommand** (line 3457-3466) — cross_project_target appears automatically once added to WORKSPACE_MODES dict.

## Why this matters (operator concern, sacrosanct framing)

> "do not minimize the task I gave you"

Minimizing path: rename to `shared` → install passes validation but tools target PROJECT_ROOT instead of target_project → worker tries to write fixes to the second-brain instead of root-ghostproxy → wrong shape entirely → first real fire = catastrophic failure.

Substantive path: implement the new mode in tools/assistant.py → install passes validation with cross_project_target → workspace dir is isolated under ~/.openclaw/ (OpenClaw scaffolds its own state there) → tools target `~/root-ghostproxy/` (per profile.target_project) → worker writes fixes to the right place → first real fire CAN work.

## Status

Logged verbatim. Implementing tools/assistant.py edits next.

---
title: "Decision — Layered PreToolUse Hooks: Universal R01-R04 Baseline First, Stage-Gate Enforcement Later"
aliases:
  - "Decision — Layered PreToolUse Hooks: Universal R01-R04 Baseline First, Stage-Gate Enforcement Later"
  - "Decision: Layered PreToolUse Hooks"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: high
maturity: growing
reversibility: easy
derived_from:
  - model-quality-failure-prevention
  - model-claude-code
  - model-skills-commands-hooks
created: 2026-04-18
updated: 2026-04-22
sources:
  - id: aicp-settings
    type: file
    file: .claude/settings.json
    description: "AICP's Claude Code settings — currently has permissions allowlist but no hooks (AICP project)"
  - id: aicp-guardrails
    type: directory
    file: aicp/guardrails/
    description: "AICP's BACKEND-LAYER guardrails (paths, response, checks) — server-side enforcement; this decision adds CLIENT-LAYER hooks"
  - id: claude-code-harness-r01-r13
    type: external
    url: https://github.com/shanraisshan/claude-code-best-practice
    description: "13 baseline hook rules per claude-code-harness conventions"
  - id: quality-standards
    type: wiki
    file: wiki/spine/standards/model-standards/model-quality-failure-prevention-standards.md
    description: "Quality Standards: instructions alone ~25% compliance, hooks ~98%"
  - id: aicp-contribution-staging
    type: wiki
    file: raw/articles/from-aicp/decisions/01_drafts/pretooluse-hooks-layered-approach.md
    description: "AICP's original submission, 2026-04-18 staged in raw/ before ingestion here"
tags: [decision, hooks, claude-code, enforcement, security, aicp, transferable]
contributed_by: "aicp"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-18"
contribution_status: accepted
---

# Decision — Layered PreToolUse Hooks: Universal R01-R04 Baseline First, Stage-Gate Enforcement Later

## Summary

AICP adds Claude Code PreToolUse hooks in TWO layers, shipped sequentially. **Layer A (NOW)** is a universal safety baseline (R01-R04 from claude-code-harness conventions: block `sudo`, `.git/` writes, `.env` writes, `--force` git operations) — STATELESS, no task-state tracking required, applies to every Claude Code session in this repo. **Layer B (LATER)** is stage-gate enforcement (block `Write`/`Edit` to forbidden paths per the active task's `current_stage`) — STATEFUL, requires AICP's `wiki/backlog/tasks/` to have live tasks with `current_stage` frontmatter that the hook can read. Layer A delivers the well-documented 60% → 98% compliance jump for safety-critical operations immediately. Layer B requires harness/state-mechanism design first; deferred. This split is correct because: (a) Layer A's value is independent of AICP-specific state, (b) Layer B's design depends on resolving where task state lives at runtime, (c) shipping Layer A now removes a class of incidents (accidental `.env` commits, force-pushes to main) without blocking on Layer B.

## Decision

> [!success] Ship Layer A (R01-R04 baseline) NOW. Defer Layer B (stage-gate) to a separate task once AICP has live task-state tracking.
>
> | Layer | Scope | State required | Status |
> |-------|-------|----------------|--------|
> | **A — Universal safety baseline** | sudo, `.git/` writes, `.env` (+secrets) writes, `--force` pushes | NONE — stateless rules always applied | **Ship in this decision** |
> | **B — Stage-gate enforcement** | Block writes to forbidden paths per active task's current_stage | Needs `current_stage` from active task | **Deferred — separate task once state mechanism lands** |

Implementation of Layer A: single Python hook script at `tools/hooks/pretool_safety.py` registered in `.claude/settings.json` under `hooks.PreToolUse`. Matches `Bash`, `Write`, `Edit` tools. Returns `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "..."}}` for matches, otherwise allows.

## Alternatives

### Alternative 1 — Skip hooks, rely on AGENTS.md "Hard rules" + backend guardrails

Continue with current state — no Claude Code hooks. Methodology in AGENTS.md (10 hard rules); `aicp/guardrails/` enforces at BACKEND when AICP routes a request.

> [!warning] Rejected: `aicp/guardrails/` enforces SERVER-SIDE — when AICP itself is the runtime executing tool calls. But Claude Code is a SEPARATE agent runtime using its own tool calls (Bash, Edit, Write) BEFORE AICP enters the picture. A Claude Code session writing to `.env` directly via `Write` bypasses AICP's backend guardrails entirely. Per Quality Standards: instructions ~25% compliance, hooks ~98%. AGENTS.md hard rules without enforcement leave a 73-point gap.

### Alternative 2 — Implement all 13 R01-R13 rules at once

Full claude-code-harness rule set immediately: R01-R04 (denial) + R05-R07 (query) + R08-R10 (security) + R11-R13 (post-execution).

> [!warning] Rejected: R05-R07 (query rules) return `ask` not `deny`, depending on harness supporting interactive ask-and-defer. Claude Code supports `ask`, but UX routing needs careful work. R11-R13 need PostToolUse hooks (different event). Layer A intentionally limits to R01-R04 (denial-only, PreToolUse-only) so the first hook ships clean. R05-R13 follow as separate decisions once R01-R04 is operationally proven.

### Alternative 3 — Implement Layer B first (stage-gate enforcement)

Build the stage-gate hook now: read `current_stage`, block writes to that stage's `forbidden_zones`.

> [!warning] Rejected: AICP doesn't currently have a "live active task" mechanism. `wiki/backlog/tasks/` has `_index.md` placeholders but no tasks with `current_stage` frontmatter. Without state to read, the hook would have no source of truth — would either block everything (false positive) or block nothing (no enforcement). Layer A doesn't block on this; ship it and queue Layer B.

### Alternative 4 — One bash script per rule (4 separate hook scripts)

4 separate hook entries, one per rule. Each is a bash one-liner.

> [!warning] Rejected: bash one-liners can't easily produce the structured JSON response Claude Code hooks expect. They also can't match multiple tool types (Bash + Write + Edit) without 12 separate hook entries (4 rules × 3 tools). One Python script with a routing function is cleaner.

## Rationale

> [!info] Evidence-backed reasons
>
> 1. **The compliance gap is quantified.** Per Quality Standards, instruction-only enforcement is ~25% compliance, structured rules ~60%, hooks ~98%. AICP's AGENTS.md "Hard rule 9: Preserve working state" is at the 25% layer. Hooks for the safety subset move it to 98%.
>
> 2. **Layer A's rules are universally correct.** No AICP profile or task type should EVER write to `.env` directly via Edit/Write — `.env` is edited out-of-band. No session should `git push --force` to main without explicit approval. These rules have no edge cases requiring context.
>
> 3. **Layer A is independent of AICP's task-state design.** A safety hook blocking `sudo` doesn't need to know which methodology stage we're in. Shipping Layer A doesn't preempt Layer B's design space — orthogonal.
>
> 4. **Bypass exists for legitimate cases.** Per Extension Standards "Enforcement Must Be Mindful", when an operator needs to edit `.env`, they do it OUT-OF-BAND. The hook's deny message names the bypass: "Edit .env directly in your terminal — this hook is for AI agent safety, not for you."
>
> 5. **AICP's existing `aicp/guardrails/` is server-side**; this hook is client-side. Both layers are needed (defense in depth). Server-side catches what Claude Code lets through; client-side catches what Claude Code does directly.
>
> 6. **Reversibility is trivial.** A hook is one entry in `settings.json`. Remove = delete entry.

## Reversibility

**Easy** — `.claude/settings.json` is one file; removing the `hooks` block disables all hooks. The hook script (`tools/hooks/pretool_safety.py`) becomes dead code if disabled but doesn't break anything else.

## Implementation (Layer A, this decision)

### Files

- **NEW**: `tools/hooks/pretool_safety.py` — ~80 lines, implements R01-R04 deny rules
- **MODIFIED**: `.claude/settings.json` — add `hooks.PreToolUse` entry pointing to the script
- **MODIFIED**: `AGENTS.md` — note that hooks are now in place for the safety subset

### R01-R04 Specifics

| Rule | Tool | Match | Deny reason |
|------|------|-------|-------------|
| R01 | Bash | command starts with `sudo ` or contains ` sudo ` | "sudo blocked — AICP's IaC must work without elevated privileges" |
| R02 | Write/Edit | path contains `/.git/` (except `.gitignore`, `.gitattributes` at root) | ".git/ writes blocked — modifying git internals risks corruption" |
| R03 | Write/Edit | path matches `**/.env*` (except `.env.example`, `.env.template`) | ".env writes blocked — secrets must be edited out-of-band" |
| R04 | Bash | command matches `git push.*--force\|git push.*-f ` | "git --force push blocked — confirm out-of-band; force pushes can lose remote work" |

### Verification

After landing, manually verify each rule fires:
1. `Bash: sudo apt-get install foo` → expect denial
2. `Write: .git/config` → expect denial
3. `Write: .env` → expect denial
4. `Bash: git push --force origin main` → expect denial

## Dependencies

If reversed (remove Layer A):

- AGENTS.md hard rules return to ~25% compliance for safety operations
- Risk of accidental `.env` commits, force-pushes to main, sudo-mediated state changes increases
- `aicp/guardrails/` (server-side) still catches operations reaching the AICP backend, but Claude Code's direct tool use bypasses

If extended (add Layer B):

- Requires "live active task" mechanism. Candidates:
  - **A**: `~/.aicp/active-task.json` symlink/file pointing to `wiki/backlog/tasks/<id>.md`
  - **B**: `.aicp/state.yaml` per repo root tracking `current_task` + `current_stage`
  - **C**: Inferred from git branch name pattern
- Separate decision on mechanism choice
- Hook script extension to read state + apply per-stage `forbidden_zones`

## Relationships

- BUILDS ON: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] (25%/60%/98% compliance evidence)
- BUILDS ON: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] (Extension Standards hook patterns)
- COMPLEMENTS: [[skills-as-primary-extension-pattern|Decision — Skills as Primary Extension Pattern]] (skills teach 60%; this decision adds the 38% hook layer)
- COMPLEMENTS: [[three-permission-modes-think-edit-act|Three Permission Modes]] (both Layer 2 enforcement — hooks universal; modes per-session)

## Backlinks

[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[Decision — Skills as Primary Extension Pattern]]
[[three-permission-modes-think-edit-act|Three Permission Modes]]

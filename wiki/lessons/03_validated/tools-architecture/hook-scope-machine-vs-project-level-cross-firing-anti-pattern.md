---
title: "Lesson — Hook scope: machine-level hooks fire across all projects (cross-firing anti-pattern); project-level scope is more precise"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: empirical-2026-05-05-opt-write-block-cross-fire
    type: empirical-evidence
    project: root-ghostproxy
    path: /root/.claude/hooks/opt-write-block.sh
    description: "The /root user's machine-level opt-write-block.sh hook fired against an second-brain-cwd session attempting a legitimate write to the second-brain, because the hook is at /root/.claude/hooks/ (root-user $HOME) and applies to ALL root-user sessions including non-/root-project ones"
  - id: companion-lesson-cross-project-boundary
    type: lesson
    file: wiki/lessons/03_validated/enforcement-compliance/second-brain-agent-must-respect-sister-project-boundaries-no-direct-cross-project-file-edits.md
    description: "Composes with second-brain-agent-must-respect-sister-project-boundaries — that's about WHO writes; this is about HOW the enforcement is scoped"
tags: [lesson, hook-scope, machine-vs-project, cross-firing, two-layer-architecture, sister-project-applicable, layer-2, hook-design]
---

# Lesson — Hook scope: machine-level vs project-level (cross-firing anti-pattern)

## Summary

Hooks placed at the **machine level** (`$HOME/.claude/hooks/`) fire for ALL Claude Code sessions of that user, regardless of which project's cwd. This is a feature for safety hooks (credential blocking, malware blocking) but an anti-pattern for **project-scoped rules** that should only apply to a specific project.

The opt-write-block hook authored at `/root/.claude/hooks/opt-write-block.sh` blocks writes to `the second-brain` from ALL root-user Claude Code sessions — including legitimate second-brain agent sessions whose cwd is the second-brain repo and whose role is to author second-brain content. The hook fires correctly against root-ghostproxy (`/root` cwd) sessions writing to the second-brain; it incorrectly fires against second-brain-cwd sessions doing their own work.

**The fix**: machine-level hooks for universal safety; project-level hooks for project-specific enforcement.

## Context

This lesson applies when:
- A project authors a hook to enforce a project-specific rule
- The project's path overlaps with the user's home directory (e.g., `/root` project = root user's $HOME)
- Sibling projects also operate as the same user, in different cwd
- A machine-level hook ends up cross-firing against legitimate operations in those sibling projects

Does NOT apply to: universal safety hooks (credential blocking, malware blocking, leak detection) — those SHOULD fire across all projects.

## Insight

> [!success] **Hook scope is a design decision: machine-level vs project-level**
>
> Hook scope is a design decision: **machine-level** (fires for all sessions of that user, every project) vs **project-level** (fires only for sessions in that project's cwd). The two-layer architecture is the structural pattern; cross-firing is the anti-pattern.

> [!tip] **The key heuristic — universal vs project-specific**
>
> If the rule is universal (safety floor that should always hold), hook goes at machine-level. If the rule is project-specific (e.g., *"this project's agent must not write to that path"*), hook goes at project-level. Putting a project-specific rule at machine-level produces spurious blocks against legitimate sibling-project operations.

> [!warning] **Hook diagnostic messages must match enforcement scope**
>
> Hook diagnostic messages should be **honest about what's being enforced**. A hook that says *"X agent must not write to Y"* but fires regardless of agent context is lying about what it's checking. The diagnostic message must match the enforcement scope, or the hook is misleading.

## Evidence

Empirical, 2026-05-05 cross-firing event:

- /root project agent authored `/root/.claude/hooks/opt-write-block.sh` to enforce "root-side rule: don't write to the second-brain"
- /root is root user's $HOME → /root/.claude/hooks/ doubles as machine-level
- second-brain agent (this agent, cwd=second-brain repo) attempted a legitimate write to the second-brain
- Hook fired against the second-brain agent and blocked the write — cross-fire
- Hook diagnostic message implied the agent was the /root agent ("/root agent must not write into the second-brain") which was incorrect — the agent was the second-brain agent
- Operator confirmed: *"sorry the root project had put an overly aggrive hook"* — acknowledging the cross-firing

Two viable fixes:
- Hook self-gating: check `pwd` in the hook; only fire if cwd is /root
- Move to project-level wiring: register hook in `<project>/.claude/settings.json` only, not at machine-level

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Project-specific enforcement** | Place hook at project-level; machine-level only for universal rules |
| **Universal safety** | Machine-level: credentials, malware, leaks |
| **Mixed scope** | Machine-level for safety floor; project-level for project-specific addition |
| **Project-path-overlaps-home (e.g., /root)** | Self-gating in hook script (check cwd); diagnostic messages must match what's actually being checked |
| **Sister-project ecosystems** | Each project's hooks should be project-scoped unless the rule is universal |
| **NOT applicable** | Universal-safety scenarios where ALL sessions should be checked regardless of project |

## Failure mode (empirical, 2026-05-05)

Operator was running:
- /root project session (test session, cwd=/root) — should not write to the second-brain directly
- second-brain session (this agent, cwd=second-brain repo) — second-brain authoring is its job

The /root project agent authored `/root/.claude/hooks/opt-write-block.sh` as a structural fix for root-side rule "don't write to the second-brain." Hook deployed at /root/.claude/hooks/ — which is also the root user's $HOME machine-level hook directory.

When the second-brain-cwd agent attempted a legitimate write to the second-brain (authoring a second-brain lesson), the machine-level hook fired and blocked the write. The hook's diagnostic message correctly identified the rule but mislabeled the agent ("/root agent must not write into the second-brain") because the hook can't distinguish project context — it fires on any root-user session.

Operator confirmed: *"sorry the root project had put an overly aggrive hook"* — acknowledging the cross-firing.

## The two-layer hook architecture (per Claude Code convention)

| Layer | Path | Scope | When to use |
|---|---|---|---|
| **Machine-level** | `$HOME/.claude/hooks/` (e.g. `/root/.claude/hooks/`) | Fires for ALL Claude Code sessions of that user, in every project | Safety hooks that should ALWAYS fire: credential blocking, malware blocking, leak detection |
| **Project-level** | `<project>/.claude/hooks/` (e.g. `/root/<project>/.claude/hooks/`) | Fires ONLY for sessions in that project's cwd | Project-specific enforcement: project's own scope rules, project-specific verifiers |

A rule that's specific to ONE project (e.g., "root-ghostproxy must not write to the second-brain") belongs at project-level, NOT machine-level. Putting it at machine-level cross-fires.

## The cross-firing anti-pattern

When a project-specific enforcement is implemented at machine-level:
- The hook fires on sessions OTHER than the target project
- Those sessions face spurious blocks
- The hook's diagnostic message either lies (claims agent is X when it's Y) or is generic (doesn't tell the agent what's actually being enforced)
- Workarounds proliferate (env-var bypass, exception lists)
- The system gets harder to reason about

## The corrective discipline

When authoring a hook script that enforces a rule:

1. **Ask: does this rule apply to ALL Claude Code sessions on this machine, or only to sessions of a specific project?**
2. **If universal (safety, malware, credentials)** → machine-level (`$HOME/.claude/hooks/`)
3. **If project-specific** → project-level (`<project>/.claude/hooks/`)
4. **If mixed (safety floor + project-specific addition)** → machine-level for the safety floor; project-level for the project-specific addition

## Special case: when the project IS the user's home

For `root-ghostproxy` specifically, the project IS at `/root` which IS the root user's home. So:
- `/root/.claude/hooks/` doubles as both "root-user machine-level" AND "root-ghostproxy project-level"
- This is the SOURCE of the cross-firing — there's no path-distinction

Mitigations:
- Hook scripts can check the cwd or session-context to decide whether to fire
- Or: project-level hooks can be placed in a different subdirectory (e.g., `/root/.claude/hooks/project-only/`) and wired in `settings.json` only for project-cwd sessions
- Or: the project's settings.json (which is read per-project) wires project-specific hooks at project-level paths even if the path overlaps with $HOME

## Concrete fix for the opt-write-block case

Two viable corrections:

**Option A — Hook self-gating**: the hook script itself checks `pwd` and only fires if cwd is /root or below:
```bash
case "$PWD" in
  /root|/root/*) ;;          # /root project → enforce
  *) exit 0 ;;               # other cwd → skip
esac
```

**Option B — Move to project-level wiring**: register the hook in the project's `.claude/settings.json` only, not in machine-level config. (Requires settings.json layering that respects project context.)

Either approach removes the cross-firing while preserving the rule for the project that authored it.

## Sister-project applicability

Universal. Every project that authors hooks should consider scope:
- Universal safety → machine-level
- Project-specific enforcement → project-level

The two-layer architecture is the structural pattern. Cross-firing is the anti-pattern to avoid.

## Relationships


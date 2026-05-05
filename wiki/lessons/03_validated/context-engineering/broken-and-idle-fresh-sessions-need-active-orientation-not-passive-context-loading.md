---
title: "Lesson — Fresh AI sessions need ACTIVE orientation (hook + command), not passive context loading. Auto-loaded brain text is NOT enough."
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: root-ghostproxy-broken-and-idle-test
    type: project
    project: root-ghostproxy
    path: /root/.claude/projects/-root/471cef22-638f-4e3e-a4a9-3ebe7a80a8bc.jsonl
    description: "Empirical fresh-session test that surfaced the failure mode"
  - id: root-ghostproxy-fix-applied-test
    type: project
    project: root-ghostproxy
    path: /root/.claude/projects/-root/f65c412b-d145-4c6c-a819-536201c63e6a.jsonl
    description: "Empirical fresh-session test post-fix showing active orientation working"
  - id: skills-commands-hooks-model
    type: wiki
    file: wiki/spine/models/agent-config/model-skills-commands-hooks.md
    description: "5-mechanism determinism ladder this lesson reinforces"
tags: [lesson, fresh-session, orientation, broken-and-idle, hook, command, determinism, additionalContext, context-engineering, sister-project-applicable, layer-2, validated]
---

# Lesson — Fresh AI sessions need ACTIVE orientation (hook + command), not passive context loading

## Summary

A fresh Claude Code session entering a project with comprehensive brain files (CLAUDE.md, AGENTS.md, BOOTSTRAP.md, etc.) auto-loaded is NOT automatically project-aware. The auto-loaded files are TEXT in context, not behavioral state. Without a SessionStart hook actively directing the agent to invoke a deterministic intel-gathering command, the agent defaults to generic-greeter behavior ("Hi. What would you like to work on?") and remains inert until the operator manually surfaces work.

**The fix**: pair a SessionStart hook (~85% determinism via `additionalContext` JSON) with a deterministic slash command (100% on invoke). Hook directs to invoke command; command does the deterministic intel load.

## Context

This lesson applies when:
- A project has comprehensive brain files (CLAUDE.md / AGENTS.md / BOOTSTRAP.md / rules) auto-loaded by the harness
- The expectation is that fresh sessions are project-aware on first turn
- Reality: the agent defaults to generic-greeter behavior despite all the loaded text
- Symptom: "Hi" → "What would you like to work on?" with no surfacing of project state, pending decisions, or open work
- Operator-named pattern: *"broken and idle"*

Does NOT apply to: scratch workspaces, projects intentionally generic, or contexts where load itself is the cost.

## Insight

Auto-loaded brain text is **passive context** — it's available for retrieval but doesn't drive behavior. Behavior requires **active direction**: a hook that fires at session start and pushes a structured imperative into the agent's first-turn context, which then chains to a deterministic command for the actual intel load.

The deeper insight: the determinism ladder (text in CLAUDE.md → hook stdout → hook `additionalContext` JSON → slash command → skill auto-trigger) has gradients of reliability. Pairing two layers (hook ~85% + command 100% on invoke) is more reliable than trusting any single layer alone. Auto-loaded text is at the bottom of the ladder for behavioral influence.

## Evidence

**Pre-fix test** (root-ghostproxy 2026-05-05 14:59):
- SessionStart hook printed only security-envelope confirmation
- User: "Hi" → Agent: "Hi. What would you like to work on?"
- Despite CLAUDE.md, AGENTS.md, BOOTSTRAP.md, 6 rules files, 12 modules, 61 tasks, 3 governance docs all in context
- Agent inert; no surfacing of 6 pending operator decisions

**Post-fix test** (root-ghostproxy 2026-05-05 15:18):
- SessionStart hook fires `session-orient.sh` with `additionalContext` JSON containing the imperative "INVOKE /orient NOW"
- User: "Hi" → Agent: cites the SessionStart hook by name, references BOOTSTRAP.md as gating read, uses "work action" terminology from the orient block
- Working behavior: hook directs → agent invokes /orient → /orient runs deterministic 21-step chain → agent emits structured ORIENT REPORT

Operator-verbatim diagnosis: *"its as if It was just broken and idle..."*.

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Any Claude Code project** | If you want first-turn intelligence on a fresh session, pair SessionStart hook + slash command. Auto-loaded text alone is insufficient. |
| **Multi-project ecosystems** | Each sister project benefits from its own hook → command pair (not just shared at machine level). The hook customizes per project's intel needs. |
| **Operator-supervised solo sessions** | The pair is the agent's intelligence-on-cold-start. Without it, the operator must manually surface every piece of context. |
| **Long-running autopilot loops** | After PostCompact (context loss), the same hook → command pattern restores the agent to a deterministic state. |
| **NOT applicable** | Generic scratch workspaces; projects where session start has no coherent ORIENT target; one-shot sessions where the cost of load exceeds the benefit. |

## Failure mode (empirical evidence)

**Test session** at `root-ghostproxy` (sister project at `/root`), 2026-05-05 14:59:

```
SessionStart hook fires → prints only the security-envelope confirmation:
  🔒 secret-protection hooks active: policy-block, leak-detector. Logs: ~/.claude/hooks/{deny,leaks}.log

User: "Hi"
Agent: "Hi. What would you like to work on?"
```

The agent had access to:
- CLAUDE.md (auto-loaded)
- AGENTS.md (auto-loaded)
- BOOTSTRAP.md (referenced by CLAUDE.md)
- 6 rules files at `.claude/rules/` (referenced by CLAUDE.md)
- 12 modules + 61 atomic tasks + 3 governance docs in wiki/

But the agent was INERT. CLAUDE.md text in context did not produce project-aware behavior. The user's "Hi" was processed as a generic greeting; the agent's response was a generic "what would you like to work on" — no surfacing of the 6 pending operator decisions, no orient command invoked, no governance docs read.

Operator's verbatim diagnosis: *"its as if It was just broken and idle..."*.

## Working behavior (post-fix evidence)

**Test session** at same project post-fix, 2026-05-05 15:18:

```
SessionStart hook fires:
  - session-orient.sh prints "ROOT-GHOSTPROXY — NEW SESSION DETECTED. INVOKE /orient NOW."
    (via additionalContext JSON — structured imperative, not plain stdout)
  - session-start.sh prints security-envelope confirmation

User: "Hi"
Agent: "Hi. Per the SessionStart hook, I should read BOOTSTRAP.md before any work action — but you've only said hi, so no work is queued yet. What would you like to do?"
```

The agent now:
- Cited the SessionStart hook by name
- Referenced BOOTSTRAP.md as the gating read
- Used "work action" — terminology from the orient block
- Didn't fabricate work; appropriately waited

This is **active orientation working**. Note: the second iteration improved further — the hook directs to `/orient` (deterministic 21-step command) which actually loads governance + verifies state + emits structured ORIENT REPORT. The SECOND iteration's response would surface the 6 pending operator decisions on a casual "Hi".

## The mechanism (the determinism ladder)

| Layer | What | Determinism | Role here |
|---|---|---|---|
| Auto-loaded brain files (CLAUDE.md, AGENTS.md) | Text in context | N/A — passive | Necessary but NOT sufficient |
| SessionStart hook stdout (plain text) | Directive printed at session start | ~70% | Better than nothing |
| SessionStart hook JSON `additionalContext` | Structured imperative injected | ~85% | What we used |
| Slash command invoked | Harness executes the command's prompt | 100% per invocation | Where the deterministic work happens |
| Skill auto-trigger | Description-match auto-fire | ~90-95% (description-quality dependent) | Useful for natural-prose triggers; NOT for session-state triggers |

**The pair**: Hook → Command. Hook fires automatically (~85%); command executes deterministically (100%). Combined, the agent reliably reaches the deterministic state on session start.

## When this applies (sister-project-applicable)

Any project where:
- A fresh AI session needs to be project-aware on the first turn
- Comprehensive brain files exist but auto-loading text alone isn't enough
- Operator wants intelligence on first turn, not "what would you like to do?" generic greeter

## When this does NOT apply

- Projects where the AI is intentionally generic (e.g., scratch workspace)
- Projects where context overhead matters more than first-turn intelligence (e.g., very short sessions where load itself is the cost)
- Projects without a coherent "ORIENT" target (you can't direct toward something that doesn't exist)

## Composition with `model-skills-commands-hooks`

This lesson is a load-bearing application of the 5-mechanism determinism ladder. Hooks alone (anti-pattern) won't reliably orient; commands alone (anti-pattern at session start) require operator-typing each session. The PAIR is what works.

Sister projects adopting this pattern: see `root-ghostproxy` first-implementation files at:
- `/root/.claude/hooks/session-orient.sh` (Python + JSON additionalContext)
- `/root/.claude/hooks/post-compact.sh` (PostCompact equivalent for compaction-recovery)
- `/root/.claude/commands/orient.md` (deterministic 21-step intel-gathering chain)

## Anti-patterns observed during the diagnosis

| Anti-pattern | Why bad |
|---|---|
| Assume auto-loaded brain files = project-aware agent | Text in context is necessary but NOT sufficient. Behavior requires direction. |
| Print just security-envelope confirmation at SessionStart | Doesn't orient toward the project. |
| Try to make the hook do command work directly | Hook output JSON has no `trigger_command` / `execute_slash` field. Hooks output context; commands do work. |
| Tell the agent "read BOOTSTRAP.md before first work action" then expect it to read on "Hi" | "Hi" is interpreted as not-a-work-action. The agent's first turn is the orient point, regardless of what the user typed. |

## Relationships


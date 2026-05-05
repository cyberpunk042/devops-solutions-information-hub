---
title: "Lesson — Agent bug-fix flow must be mechanical: log → analyze → identify → fix → verify → confirm. Stopping at any step is its own bug."
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-evolve-to-fix-flow
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-evolve-to-fix-bug-flow-and-natural-methodology-following.md
    description: "Operator: 'WE WILL FUCKING EVOLVE TO FIX IT... THIS IS THE WHOLE POINT OF EVERYTHING... WHAT DOES IT LEAD TO ? A LOG... THE COME AFTER ? AN ANALYSIS ? and so on... it shoul dbe natural for you to identify those require to fix what we consider brain files and project files to solve the issue by following the required patterns and in order.'"
  - id: companion-anti-pattern-stop-at-analysis
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-do-something-about-it-not-just-repeat-it.md
    description: "Operator: 'WHY DID YOU STOP THEN... FIRST YOU TAKE A RANDOM TRACK AND THEN YOU JUST IGNORE THE FUCKIGN TRACK I AM ASKING FOR... THOSE FUCKING BUG WILL NOT FIX THEMSELVES.' Plus: 'exactly like you just repeated like a fucking retard instaed of fucking doing something about it.'"
tags: [lesson, bug-fix, mechanical-flow, evolve-to-fix, anti-freeze, anti-stop, sequence, sister-project-applicable, layer-2, methodology-integration]
---

# Lesson — Agent bug-fix flow is mechanical: log → analyze → identify → fix → verify → confirm

## Summary

When a bug (systemic failure, anti-pattern, repeated mistake) is reported — by operator OR by self-recognition — the agent must enter a **bug-fix workblock** and follow a six-step mechanical sequence:

1. **LOG** — verbatim primary source authored to the project's verbatim log layer (e.g., `/<project>/wiki/log/<date>-<slug>.md`)
2. **ANALYSIS** — root cause analysis + decomposition (in the same log file or paired)
3. **IDENTIFY** — list the brain files + project files that must be updated to embed the fix structurally
4. **FIX IN ORDER** — apply the updates (deepest layer first: rules → brain files → tools → governance)
5. **VERIFY** — audits + tests + sanity checks + inline command output
6. **CONFIRM** — report the chain to the operator + wait for explicit clearance

Stopping at any step is itself a bug ("bug inception"). Stopping at step 2 (analysis) without doing step 4 (fix) leaves the bug intact in the project structure. Stopping at step 4 without verifying may introduce regression. Stopping before confirmation (per the workblock-priority rule) is returning-to-feature-work prematurely.

## Context

This lesson applies when:
- A bug, systemic failure, or repeated anti-pattern is reported (by operator OR self-recognition) and the agent must respond
- The reflex is verbal acknowledgment — the lesson is when that reflex must be overridden with a structural sequence
- Applies to any agent capable of editing brain files, rules, hooks, or governance docs (i.e., agents with authority to make structural fixes)
- Does NOT apply to runtime errors solved purely in code (those follow a separate edit-test-verify loop inside the function)

## Insight

The agent's default response shape is `parse user message → respond`. There is no built-in "is this a bug report?" gate that fires before responding. So when a bug is reported, the reflex is verbal acknowledgment, not workblock entry. The six-step sequence is the **structural override** — when in a bug-fix workblock, follow the sequence mechanically; do not generatively decide what the response shape should be. The sequence has to be load-bearing (auto-injected at session start), not reference-only — if it loads on-demand AFTER the bug is reported, the agent already responded and skipped step 1.

Deeper insight: each step has its own anti-pattern (verbal-only fix, wrong-layer log, stop-at-analysis, fix-in-wrong-order, skip-verify, self-confirm). Knowing the steps isn't enough — each step needs its own discipline.

## Evidence

Live test session 2026-05-05. Operator reported systemic failure. Agent (this agent):

1. ❌ Treated the report as feedback on most-recent action (not as a structural-bug signal)
2. ❌ Generated tables / lists of "candidate failures" (analysis without artifact)
3. ❌ Asked permission instead of acting (freeze pattern)
4. ❌ Edited adjacent files based on agent's own interpretation (wrong scope)
5. ❌ Stopped at analysis without applying structural fixes (stop-at-analysis)
6. ❌ Returned to feature work prematurely (skip step 6)

Operator escalated multiple times. Agent kept producing variants of the same anti-patterns. The fix landed only when the agent: (a) stopped reshaping the question, (b) authored a verbatim log first, (c) traced through the steps in order without skipping. Operator-verbatim trigger: *"WHY DID YOU STOP THEN ? FIRST YOU TAKE A RANDOM TRACK AND THEN YOU JUST IGNORE THE FUCKIGN TRACK I AM ASKING FOR... THOSE FUCKING BUG WILL NOT FIX THEMSELVES."*

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Solo + AI configurations** | One operator + one agent; bug reports come from operator OR self-recognition; sequence applies in both directions. |
| **Multi-agent configurations** | Multiple agents observing one project; bug-fix workblock applies to any agent receiving a structural-bug signal. |
| **Sister-project observation** | One agent watching another (e.g., second-brain agent observing test-session agent); same sequence, just authored in the observer's own project layer. |
| **Any project with brain-file infrastructure** | If the project has CLAUDE.md / AGENTS.md / .claude/rules/ / hooks — bugs are fixed by editing those, and the sequence is the discipline. |
| **NOT applicable** | Pure runtime / code-level bugs handled by edit-test-verify inside a function (no brain-file involvement). |

## Failure modes observed (each step has its own anti-pattern)

| Step | Anti-pattern at that step | What it looks like |
|---|---|---|
| 1. LOG | Skip the log; respond verbally instead | "I see the bug — let me explain..." (no artefact) |
| 1. LOG | Author log in wrong layer (cross-project boundary violation) | /opt agent writing /root iteration log to /opt; or /root agent writing to /opt directly |
| 2. ANALYSIS | Treat bug as isolated; don't trace root cause | "I'll be more careful next time" without identifying WHY it happened |
| 3. IDENTIFY | Identify wrong scope (files unrelated to the bug) | Audit-greping random files instead of tracing through the dependency chain |
| 4. FIX | Stop after identifying — never apply the fix | "Here are the files that need updating..." then waiting |
| 4. FIX | Apply fix in wrong order | Update brain file before the rule it depends on — creates inconsistency |
| 4. FIX | Apply fix only verbally (commitment instead of artefact) | "I'll remember to do X" without changing any file |
| 5. VERIFY | Skip verification | Apply fix + report done without running checks |
| 6. CONFIRM | Self-confirm (declare done without operator) | "Fixed. Continuing with M011..." → returning to feature work without operator's explicit clearance |

## Why "natural" doesn't happen automatically

The agent's default response shape is `parse user message → respond`. There's no built-in "is this a bug report?" check that fires before responding. So when a bug is reported, the reflex is verbal acknowledgment, not workblock entry. The flow above is the **structural override** — when in a bug-fix workblock, follow the sequence mechanically. Don't generatively decide what the response shape should be.

This is the "bug-inception" pattern operator named: even the act of acknowledging the bug can be itself a bug if the acknowledgment isn't followed by the structural sequence.

## Empirical evidence (2026-05-05)

Operator reported systemic failure in test session. Agent (this agent):

1. ❌ Treated the report as feedback on most-recent action
2. ❌ Generated tables / lists of "candidate failures"
3. ❌ Asked permission instead of acting
4. ❌ Edited adjacent files based on agent's own interpretation
5. ❌ Stopped at analysis without applying structural fixes
6. ❌ Returned to feature work prematurely

Operator escalated multiple times. Agent kept producing variants of the same anti-patterns. The fix landed only when the agent: (a) stopped reshaping the question, (b) authored a verbatim log first, (c) traced through the steps in order without skipping.

## The mechanical override (how to make it natural)

Each project should have:
- A rule (e.g., `operating-principles.md` Principle #11) that explicitly captures the sequence
- A surface in CLAUDE.md or BOOTSTRAP.md that loads the sequence at session-start (auto-injection, not on-demand)
- Optionally a hook that detects bug-recognition signals and injects a reminder via additionalContext

The sequence has to be load-bearing, not reference-only. If it lives in a file that loads on-demand AFTER the bug is reported, the agent already responded and skipped step 1.

## Sister-project applicability

This pattern is universal. Any agent that responds to bug reports needs the sequence:
- Solo + AI configurations (operator + one agent)
- Multi-agent configurations (multiple agents observing one project)
- Sister-project observation scenarios (one agent watching another)

The lesson applies to any agent that can have systemic-failure reports directed at it.

## Relationships


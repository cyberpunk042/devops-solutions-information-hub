---
title: "Lesson — Bug vs systemic-bug nuance: systemic bugs live at the meta level (harness, ecosystem, brain files); regular bugs live inside the code"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-bug-vs-systemic-nuance
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-bug-vs-systemic-bug-meta-level-nuance.md
    description: "Operator: 'its important to know the nuance between a bug and a systmic bug too.. I see you writting and I realize that now... systemic bug are often happening at the meta level not at the inside. not that some case its not inside though, but with agents its often the harness and ecosystem and brains files'"
tags: [lesson, bug-categorization, systemic-vs-regular, meta-level, harness, ecosystem, brain-files, agent-bugs, sister-project-applicable, layer-2]
---

# Lesson — Bug vs systemic-bug: meta-level vs inside-the-code

## Summary

Not every bug is a systemic bug. The distinction matters for HOW it's fixed and WHERE the fix lives.

| Category | Where it lives | Where the fix goes |
|---|---|---|
| **Regular bug** | Inside the code/data | Code change, data fix, config update |
| **Systemic bug** | Meta level: harness, ecosystem, brain files | Rule update, hook authoring, brain-file evolution, methodology change, ecosystem-pattern update |

For **agents specifically**, systemic bugs tend to live at the meta layer — not in the agent's individual responses, but in:

- **The harness** (Claude Code's mechanism, hook system, tool catalog)
- **The ecosystem** (cross-project relationships, second-brain ↔ sister-project flows, contribute channels)
- **Brain files** (CLAUDE.md, AGENTS.md, .claude/rules/, .claude/modes/, .claude/hooks/, BOOTSTRAP.md, methodology config)

A regular agent bug looks like: "this regex misses two entries." Fix: regex code change.

A systemic agent bug looks like: "agent doesn't naturally orient on session start." Fix: SessionStart hook + /orient command + brain-file routing + rule that captures the pattern.

The systemic fix is multi-layer; the regular fix is single-point.

## Context

This lesson applies when:
- A bug or failure has been reported and the agent must classify before fixing
- The agent is choosing where the fix should land (code vs rule vs hook vs brain-file vs methodology)
- Operator's frustration may signal a recurring pattern (systemic) vs a one-off (regular)
- Multi-layer projects (with rules, brain files, hooks, code, methodology, ecosystem) need bug-routing discipline

Does NOT apply to: trivial localized issues with no behavioral pattern; cases where classification is obvious (a `KeyError` is regular).

## Insight

The classification of bug vs systemic-bug determines **where the fix lives**. Mis-classification produces structural waste: regular bugs treated as systemic over-engineer rules and hooks for what's just a code change; systemic bugs treated as regular leave the underlying pattern intact, recurring in adjacent contexts.

**Agent-specific insight** (operator's): for agents, systemic bugs tend to live at the meta layer — harness (Claude Code mechanism, hook system), ecosystem (cross-project flows, contribute channels), brain files (CLAUDE.md, AGENTS.md, .claude/rules/, modes, hooks, methodology config). The agent's "code" rarely contains the bug; the bug is in the surrounding configuration.

The deeper insight: classification is the FIRST step of bug-fix-flow's IDENTIFY phase. Until the bug is classified, the agent can't list the right files to fix. Get the classification right, and the fix-location follows.

## Evidence

Empirical, 2026-05-05 root-ghostproxy + second-brain session:

- Operator surfaced the distinction directly: *"its important to know the nuance between a bug and a systmic bug too... systemic bug are often happening at the meta level not at the inside. not that some case its not inside though, but with agents its often the harness and ecosystem and brains files."*
- Multiple agent failures observed: doesn't naturally orient on session start (systemic — fix in hook + command + brain-file), treats every operator complaint as feature-work pivot (systemic — fix in rule + brain-file routing), freezes when corrected (systemic — fix in operating-principles)
- Single-file fixes (regex update in `tools.decisions` parser) tracked as regular — fixed in code, no rule layer touched
- The lesson canonicalizes the distinction so future bugs route correctly at the IDENTIFY step

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Agent debugging (general)** | Classify first; agent-bug fix usually lives in meta layer |
| **Multi-layer projects** | Each layer (code / rule / hook / brain / mode / methodology / ecosystem) hosts a distinct fix shape |
| **Pattern-recognition skill** | Operator-frustration about recurring failures is a systemic signal |
| **Sister-project ecosystems** | Cross-project pattern bugs are systemic (e.g., contribute channel not wired) |
| **Code-level bugs in agent tools** | Still classified as regular; the fix is a code change in `tools/`, no rule update |
| **Methodology violations** | Often systemic; fix lives in rule + verifier + ALLOWED/FORBIDDEN list |
| **NOT applicable** | Trivial localized issues with no behavioral pattern |

## Why this distinction matters

Operator's verbatim insight: *"systemic bug are often happening at the meta level not at the inside."*

When the agent (or human) misclassifies:

| Misclassification | Result |
|---|---|
| Treats a systemic bug as a regular bug | Patches the symptom; underlying pattern recurs in adjacent contexts |
| Treats a regular bug as a systemic bug | Over-engineering; adds rules/hooks for what's just a coding fix |
| Mixes both in the same register | The dumping-ground anti-pattern (per fake-blockers lesson) |

The categorization should be **the FIRST step of bug-fix flow** — before logging, before analyzing, classify which kind. The classification determines where the fix lives.

## Heuristics for classification

### Signs it's a regular bug

- Localized to a single function / file / data record
- Reproducible with a specific input
- Fix is a code change (or data fix, or config update)
- Doesn't affect agent behavior in unrelated contexts
- Doesn't require updating rules, hooks, brain files

Example: `tools.decisions` parser regex misses entries with trailing whitespace.
Fix: change the regex from `$` to `\s*$`. Single file. Done.

### Signs it's a systemic bug

- Pattern recurs across cycles, sessions, or contexts
- Agent's behavior reveals the issue (not data)
- Fixing one instance doesn't prevent others
- Fix requires updating rules, hooks, brain files, or methodology
- Operator's frustration is about a PATTERN, not a single failure

Example: agent doesn't naturally orient on session start; treats every operator complaint as a feature-work pivot; freezes when corrected.
Fix: rule layer (operating-principles #11), hook layer (session-orient.sh), brain-file layer (CLAUDE.md routing), command layer (/orient). Multi-layer.

### Edge case: bug INSIDE the agent's code

Operator clarification: *"not that some case its not inside though, but with agents its often the harness and ecosystem and brains files."*

Sometimes a bug IS inside the agent's code (e.g., a tool's regex bug). That's still a regular bug, fixed at the code level. The distinction holds: it's where the LIVING bug is, not where the agent is.

## For agents: where systemic bugs typically live

| Layer | Examples of systemic bugs |
|---|---|
| **Harness (Claude Code)** | Hook configuration cross-firing; tool-permission mis-classification; sub-agent dispatch behavior; deferred-tool loading patterns |
| **Ecosystem** | Cross-project boundary violations; second-brain ↔ sister-project flow gaps; contribute channel not yet wired; sister-project registry stale |
| **Brain files** | CLAUDE.md missing routing entry; BOOTSTRAP.md doesn't surface a critical pattern; rule loaded on-demand AFTER it's needed; methodology yaml doesn't include a relevant model |
| **Rules** | Principle exists but isn't load-bearing; rule conflicts with another rule; rule is advisory when it should be enforced |
| **Hooks** | Hook fires too eagerly; hook fires too rarely; hook scope too broad (machine-level when should be project-level) |
| **Modes** | Mode definition incomplete; mode lacks /cycle integration; mode doesn't update active-state file |
| **Methodology config** | Stage gate too strict; ALLOWED/FORBIDDEN list incomplete; gate command path wrong |

## For each layer, the structural fix uses different artefacts

| Bug layer | Fix layer |
|---|---|
| Harness | Hook script (`.sh` / `.py`) wired in `settings.json` |
| Ecosystem | Pattern in second-brain `wiki/patterns/`; sister-projects.yaml update; contribute channel work |
| Brain files | Edit the file (CLAUDE.md / AGENTS.md / BOOTSTRAP.md / etc.) |
| Rules | New principle in operating-principles.md OR new rule file |
| Hooks | New hook script + settings.json wiring |
| Modes | Update `.claude/modes/<name>.md` |
| Methodology | Edit `wiki/config/methodology.yaml` |

## Composition with the bug-fix flow

The bug-fix-flow lesson (log → analyze → identify → fix → verify → confirm) should integrate this categorization at the IDENTIFY step:

3. **Identify** — list the brain files + project files that must be updated to embed the fix structurally:
   - First classify: is this a regular bug or systemic?
   - If regular: identify the single-point fix location
   - If systemic: identify which META LAYER (harness / ecosystem / brain files / rules / hooks / modes / methodology) the fix belongs in
   - Then list the specific files within that layer

This makes the IDENTIFY step concrete + categorical.

## Anti-patterns

| Anti-pattern | Why bad |
|---|---|
| Treat every bug as systemic | Over-engineers for what's just a code fix |
| Treat every bug as regular | Symptoms get patched but patterns recur |
| Skip classification | The flow's IDENTIFY step gets vague; fix may go in the wrong layer |
| Misclassify operator's frustration | If operator says "this keeps happening" — that's a systemic signal, not a one-off |

## Sister-project applicability

Universal. Every project with both code AND meta-layer (rules, brain files, harness config) has both bug categories. The classification skill is universal.

For agents: the systemic-bug discipline (per operator) is especially important because agent behavior emerges from the meta layer, not from the agent's "code" alone. Most agent fixes are in the meta layer.

## Relationships


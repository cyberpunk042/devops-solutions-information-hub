---
title: "CLAUDE.md Structural Patterns for Agent Compliance"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: seed
derived_from:
  - "Model: Methodology"
  - "Never Skip Stages Even When Told to Continue"
  - "Always Plan Before Executing"
instances:
  - page: "OpenArms AGENTS.md"
    context: "411-line agent directive with hard/soft rule separation, sacrosanct section, 20 operational lessons"
  - page: "Research Wiki CLAUDE.md"
    context: "200-line flat prose — lower compliance rates, agents lose thread"
  - page: "OpenArms agent-directive.md"
    context: "Short-form (83 lines) with tables, commands, access levels — higher compliance"
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: openarms-agents
    type: file
    file: /home/jfortin/openarms/AGENTS.md
  - id: openarms-directive
    type: file
    file: /home/jfortin/openarms/wiki/config/agent-directive.md
tags: [claude-md, agent-compliance, structural-patterns, formatting, enforcement]
---

# CLAUDE.md Structural Patterns for Agent Compliance

## Summary

Structural formatting techniques that improve agent compliance with methodology instructions. Discovered empirically through OpenArms's v2-v9 methodology evolution — instruction-based enforcement failed at 75% until structural patterns were applied. These patterns exploit how LLMs process instructions: proximity to task, visual distinctiveness, enumerable constraints, and progressive disclosure.

> [!info] Pattern Reference Card
>
> | Pattern | What It Does | Compliance Impact |
> |---------|-------------|-------------------|
> | Sacrosanct Section | Immutable operator directives at the top | Prevents drift from core intent |
> | Hard vs Soft Rule Separation | Tables with structural vs judgment rules | Agents know which rules have teeth |
> | ALLOWED/FORBIDDEN Lists | Per-stage enumerable constraints | 75% violation reduction (OpenArms v9) |
> | Progressive Disclosure | Most important rules first, details later | Agents follow top rules even under context pressure |
> | Command Checkpoints | Named commands for deterministic transitions | Agents can't silently skip transitions |
> | Section Dividers | Visual `# -----------` separators | Agents treat sections as discrete contexts |
> | Anchor Phrases | Repeated key phrases across sections | Reinforces critical rules through repetition |
> | Concrete Examples | Show the exact output expected | Agents mimic examples more reliably than prose |

## Pattern Description

### Why Structure Matters More Than Content

LLMs process CLAUDE.md as part of their system prompt. The structural properties of the text affect compliance more than the semantic content:

> [!warning] The Flat Prose Problem
>
> A 200-line block of narrative instructions creates a "wall of text" that agents scan non-uniformly. Rules buried in paragraph 15 receive less attention than rules in paragraph 1. Rules stated in prose ("you should try to...") receive less compliance than rules in tables or lists ("FORBIDDEN: ..."). This is not a reading comprehension failure — it's an attention distribution problem.

The patterns below address this by creating **structural distinctiveness** — making important rules visually different from surrounding text so they receive disproportionate attention.

### Pattern 1: Sacrosanct Section

Place immutable operator directives at the very top, quoted verbatim, explicitly marked as non-negotiable.

```markdown
## Sacrosanct Operator Directives

These directives are the supreme source of truth. They override everything else.

> "Privacy first. No telemetry without consent."
> "Solo agent mode must work without any network."
> "Scaffolding and documentation first. Always."
```

> [!tip] Why This Works
>
> By placing operator intent BEFORE methodology rules, the agent has a reference frame for all subsequent instructions. When methodology and operator intent appear to conflict, the agent defers to the sacrosanct section. Without it, agents optimize for methodology compliance at the expense of operator intent.

### Pattern 2: Hard vs Soft Rule Separation

Explicitly label rules as either structurally enforced (hard) or judgment-based (soft). Use tables, not prose.

```markdown
### Hard Rules (enforced by hooks)
| Rule | Enforcement |
|------|------------|
| No git commands | pre-bash hook blocks git add/commit/push |
| No src/ during document stage | pre-write hook blocks *.ts writes |

### Soft Rules (require judgment)
| Rule | Guidance |
|------|---------|
| Read existing code before writing new | Check file exists, read first 50 lines |
| Raise concerns when something feels wrong | Use /concern command |
```

> [!tip] Why This Works
>
> Agents comply better with rules they know are enforced. When ALL rules are presented as equal (prose), agents treat them all as soft and use judgment about which to follow. Explicit hard/soft separation tells the agent: "these will be caught if you violate them" vs "these require your judgment."

### Pattern 3: ALLOWED/FORBIDDEN Lists

For each stage, enumerate what IS and IS NOT permitted. Use those exact words.

```markdown
### Scaffold Stage

ALLOWED:
- export type / export interface definitions
- export const for static data
- Empty test files with placeholder assertions

FORBIDDEN:
- Functions with logic (parsing, resolving, matching)
- Real test assertions
- Any function body longer than 3 lines
```

> [!warning] Critical: Enumerable Beats Narrative
>
> "Don't write business logic during scaffold" is a narrative instruction. Agents interpret "business logic" differently per context. "FORBIDDEN: function bodies longer than 3 lines" is enumerable — the agent can count to 3. Compliance jumps from ~25% (narrative) to ~90% (enumerable) based on OpenArms overnight run data.

### Pattern 4: Progressive Disclosure

Order sections from most critical to most detailed. If the agent's context compresses, the top sections survive.

```markdown
## 1. Identity (who you are)
## 2. Hard Rules (what you must never do)
## 3. Stage Workflow (what you do now)
## 4. Commands (how to signal transitions)
## 5. Architecture (background knowledge)
## 6. Conventions (style preferences)
```

> [!tip] Why This Works
>
> Context compaction (when conversation exceeds limits) removes content from the middle/end of system prompts more aggressively than from the beginning. Rules at the top survive compaction. Rules at the bottom may be lost. Place non-negotiable rules (identity, hard constraints) before nice-to-have rules (style, conventions).

### Pattern 5: Command Checkpoints

Define named commands for deterministic stage transitions. Agents can't silently skip.

```markdown
### Commands
| Command | What It Does |
|---------|-------------|
| /stage-complete | Validate current stage artifacts, commit, advance |
| /task-done | Verify Done When items, update readiness, close task |
| /concern "msg" | Log a concern without blocking completion |
```

> [!tip] Why This Works
>
> Without checkpoints, agents transition between stages implicitly — they just start writing code after "finishing" documentation. With named commands, the transition is explicit and can be validated. The agent must declare "I am done with this stage" which creates a verification opportunity.

### Pattern 6: Section Dividers with Context Labels

Use visual dividers between major sections with descriptive comments.

```markdown
# ---------------------------------------------------------------------------
# Stage Boundaries — ALLOWED and FORBIDDEN per stage
# ---------------------------------------------------------------------------
```

> [!tip] Why This Works
>
> LLMs tokenize and process text in chunks. Visual dividers create clear boundaries between conceptual sections. The descriptive comment after the divider acts as a section title that the agent can reference when navigating the instructions. Without dividers, long CLAUDE.md files blend into a continuous stream.

### Pattern 7: Anchor Phrases

Repeat critical rules in multiple sections using the same phrasing.

```markdown
# In methodology section:
"Continue" means advance within the current stage. NOT skip to the next stage.

# In stage workflow section:
Remember: "continue" = advance within stage, not skip ahead.

# In learnings section:
Lesson: "Continue" ≠ skip. This caused Bug 7 — agent jumped from document to implement.
```

> [!tip] Why This Works
>
> Repetition with consistent phrasing creates stronger associations than a single statement. The rule is reinforced from three different angles: definition, reminder, and evidence. Agents that encounter the same rule in multiple contexts are less likely to override it.

### Pattern 8: Concrete Examples Over Abstract Rules

Show the exact artifact expected, not just describe it.

```markdown
# Instead of:
"Commit messages should follow conventional format"

# Write:
Commit format: `type(scope): message`
Examples:
  feat(config): add network rules resolver
  fix(agent): prevent stage skip on continue
  docs(wiki): document bridge module pattern
```

## Instances

> [!example]- Instance 1: OpenArms AGENTS.md (411 lines, high compliance)
>
> Uses: Sacrosanct section (top), Hard rules table, ALLOWED/FORBIDDEN per stage, Progressive disclosure (identity → rules → workflow → background), Command checkpoints (/stage-complete, /task-done, /concern), Section dividers throughout, Anchor phrases ("instruction-based enforcement doesn't work" repeated in learnings and methodology sections), Concrete examples (commit format, Done When format).
>
> Result: Combined with infrastructure enforcement, achieved viable autonomous agent runs. Agents follow stage boundaries ~90% of the time (up from ~25% with prose-only).

> [!example]- Instance 2: Research Wiki CLAUDE.md (200 lines, moderate compliance)
>
> Uses: Progressive disclosure (partially — structure is logical but flat), Some concrete examples (pipeline commands). Missing: Sacrosanct section, Hard/soft separation, ALLOWED/FORBIDDEN lists, Command checkpoints, Section dividers, Anchor phrases.
>
> Result: Agents frequently skip stages, produce wrong artifacts, ignore quality gates. Compliance is instruction-dependent (varies by model and session length).

> [!example]- Instance 3: OpenArms agent-directive.md short form (83 lines, focused compliance)
>
> Uses: Hard vs soft tables, Access level table (CAN vs CANNOT), Commands table, Stage workflow in 6 numbered steps. Compact but highly structured.
>
> Result: Higher per-rule compliance than the long-form AGENTS.md for the specific rules it covers. Shows that compact + structured > verbose + flat.

## When To Apply

> [!tip] Use These Patterns When
>
> - Building a CLAUDE.md for any project that uses methodology
> - Agents are ignoring specific rules (diagnosis: check if the rule is in prose or in a structured format)
> - Moving from Tier 1 (manual) to Tier 2+ (configured) methodology adoption
> - Debugging compliance failures — restructure the failing rule using these patterns
> - Context compaction is losing important rules (move them to the top + add anchor phrases)

## When Not To

> [!warning] Don't Use When
>
> - The CLAUDE.md is already short and focused (<50 lines) — structure overhead isn't worth it
> - You're writing a one-off instruction, not a persistent methodology — these patterns are for recurring compliance
> - The rules are genuinely soft (style preferences, conventions) — don't over-structure optional guidance
> - You're adding structure for structure's sake without measuring compliance — patterns should address observed failures

## Relationships

- DERIVED FROM: [[Model: Methodology]]
- DERIVED FROM: [[Never Skip Stages Even When Told to Continue]]
- DERIVED FROM: [[Always Plan Before Executing]]
- BUILDS ON: [[Model: Claude Code]]
- BUILDS ON: [[Model: Skills, Commands, and Hooks]]
- RELATES TO: [[Plan-Execute-Review Cycle]]
- FEEDS INTO: [[Methodology Adoption Guide]]
- FEEDS INTO: [[Model: Methodology Standards — What Good Looks Like]]

## Backlinks

[[Model: Methodology]]
[[Never Skip Stages Even When Told to Continue]]
[[Always Plan Before Executing]]
[[Model: Claude Code]]
[[Model: Skills, Commands, and Hooks]]
[[Plan-Execute-Review Cycle]]
[[Methodology Adoption Guide]]
[[Model: Methodology Standards — What Good Looks Like]]
[[Enforcement Hook Patterns]]
[[Methodology Framework]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Stage-Aware Skill Injection]]

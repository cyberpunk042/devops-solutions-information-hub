---
title: CLAUDE.md Structural Patterns for Agent Compliance
aliases:
  - "CLAUDE.md Structural Patterns for Agent Compliance"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Model: Methodology"
  - "Never Skip Stages Even When Told to Continue"
  - "Always Plan Before Executing"
instances:
  - {'page': 'OpenArms AGENTS.md', 'context': "410 lines, 0 tables, 0 dividers, 44 bullet lists, 0 numbered lists — documents what fails but doesn't use structural techniques"}
  - {'page': 'OpenArms agent-directive.md', 'context': '424 lines, 3 tables, 9 dividers, 31 numbered lists, 14-step work loop — implements all 6 structural techniques, highest compliance'}
  - {'page': 'Research Wiki CLAUDE.md', 'context': '170 lines, restructured 2026-04-11 with tables, dividers, ALLOWED/FORBIDDEN — intermediate compliance'}
  - {'page': 'OpenArms stage skills (5 files)', 'context': '29-43 lines each, MUST/MUST NOT lists, runtime state injection, stage-specific narrowing — highest per-stage compliance'}
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

LLMs process CLAUDE.md as part of their system prompt. The structural properties of the text affect compliance more than the semantic content.

> [!warning] The Evidence: 75% Violation Rate From Prose Instructions
>
> OpenArms ran autonomous agents overnight (2026-04-10). Instructions about stage boundaries existed in AGENTS.md since v4. Violation rate: 75%. The same rules reformatted as numbered sequences + tables + per-stage skills achieved ~90% compliance. The CONTENT was identical — the STRUCTURE changed compliance by 65 percentage points.

> [!abstract] Quantified Comparison: Two Documents With the Same Rules
>
> | Metric | AGENTS.md (low compliance) | agent-directive.md (high compliance) |
> |--------|---------------------------|--------------------------------------|
> | Lines | 410 | 424 |
> | Tables | 0 | 3 major tables |
> | Divider lines | 0 | 9 visual breaks |
> | Numbered lists | 0 | 31 (14-step loop, 8 hierarchy rules, etc.) |
> | Bullet lists | 44 | 18 |
> | Code blocks | 2 | 10 |
> | Sections avg length | 19 lines (shallow) | 42 lines (deep, sequential) |
> | Organization | Topic-based (independent) | Process-based (sequential) |
>
> AGENTS.md documents what FAILED. agent-directive.md implements what WORKS. Same information, different structure, vastly different compliance.

The core insight: compliance comes from **removing choice** — tables eliminate interpretation, numbered sequences create cognitive chains that are hard to skip, stage-specific injection prevents seeing ahead, command checkpoints make transitions explicit.

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

> [!example]- Instance 1: OpenArms agent-directive.md (424 lines — HIGHEST compliance)
>
> **Uses ALL 6 techniques:**
> - 14-step numbered work loop (31% of document) — creates cognitive chain agents must follow sequentially
> - 3 major tables: task_type→stages, readiness ranges, stage methodology (what you DO / do NOT)
> - 9 divider lines at major section breaks
> - Sections labeled MANDATORY/REQUIRED in headings
> - Per-stage Quality Gates (5 separate subsections, 3-4 checkpoints each)
> - "What You Must Never Do" section with 14 numbered items + causal explanations
>
> **Result:** Combined with infrastructure enforcement (hooks + harness), achieved ~90% stage boundary compliance. The 14-step loop is the core — agents can't skip a numbered step without acknowledging the skip.

> [!example]- Instance 2: OpenArms AGENTS.md (410 lines — LOW compliance despite good content)
>
> **Uses 0 of the 6 techniques:**
> - 0 tables, 0 dividers, 0 numbered lists
> - 44 bullet lists (pick-and-choose, not sequential)
> - Topic-based organization (independent sections, no sequence)
> - 19-line average sections (shallow, browsable but not enforcing)
> - Contains the BEST wisdom in the ecosystem (20 operational lessons, each traced to a specific bug)
>
> **Result:** 75% violation rate on stage boundaries despite clear prose rules. The Learnings section DOCUMENTS why agent-directive.md works better — but AGENTS.md itself doesn't use those lessons in its own format. The irony is the evidence.

> [!example]- Instance 3: OpenArms Stage Skills (5 files, 29-43 lines each — HIGHEST per-stage compliance)
>
> **The key technique: stage-specific narrowing**
> - Agent sees ONLY its current stage's skill — no cross-stage visibility
> - Each skill reads runtime state: `!cat .openarms/current-task-id`
> - MUST/MUST NOT lists (3-5 items, not 14)
> - Ends with explicit checkpoint: "When Done: Call /stage-complete"
> - Shortest, most focused instructions produce highest compliance per-rule
>
> **Result:** "One task at a time. Seeing 8 tasks causes rushing. Seeing 1 task causes focus." Same principle applied to stages.

> [!example]- Instance 4: Research Wiki CLAUDE.md (170 lines — INTERMEDIATE, restructured 2026-04-11)
>
> **Uses 5 of 6 techniques (after restructure):**
> - Sacrosanct section with operator quotes at top
> - ALLOWED/FORBIDDEN per-stage table
> - Hard vs Soft rule separation as tables
> - 7 divider lines
> - Model selection table
> - Missing: numbered work loop (not applicable — wiki doesn't have a harness)
>
> **Result:** Improved from flat prose. Not yet measured quantitatively — needs multiple sessions to assess.

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

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[model-methodology|Model — Methodology]]
- DERIVED FROM: [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]
- DERIVED FROM: [[always-plan-before-executing|Always Plan Before Executing]]
- BUILDS ON: [[model-claude-code|Model — Claude Code]]
- BUILDS ON: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[plan-execute-review-cycle|Plan Execute Review Cycle]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-methodology|Model — Methodology]]
[[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[model-claude-code|Model — Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[ai-agent-artifacts|AI Agent Artifacts — Standards and Guide]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[methodology-framework|Methodology Framework]]
[[model-context-engineering|Model — Context Engineering]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[stage-aware-skill-injection|Stage-Aware Skill Injection]]
[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]

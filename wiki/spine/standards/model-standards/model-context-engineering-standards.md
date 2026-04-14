---
title: "Context Engineering Standards — What Good Structured Context Looks Like"
aliases:
  - "Context Engineering Standards — What Good Structured Context Looks Like"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-13
updated: 2026-04-13
sources:
  - id: context-model
    type: wiki
    file: wiki/spine/models/depth/model-context-engineering.md
  - id: proto-programming-lesson
    type: wiki
    file: wiki/lessons/03_validated/structured-context-is-proto-programming-for-ai-agents.md
  - id: validation-matrix
    type: observation
    file: raw/articles/openfleet-validation-matrix-samples.md
    description: 29 structured context scenarios (2,444 lines)
tags: [standards, context-engineering, proto-programming, structured-context, quality, gold-standard, anti-patterns]
---

# Context Engineering Standards — What Good Structured Context Looks Like

> [!tip] AI Quick Start — What You Do With This Page
>
> 1. **Before writing ANY context injection** (CLAUDE.md section, skill, hook response, task prompt): check "The Three Levels" table — are you working at the right level?
> 2. **Before designing a CLAUDE.md**: read "Gold Standard: CLAUDE.md Structure" — structure beats content
> 3. **Before writing a skill**: read "Gold Standard: Skill Injection" — stage-aware, tier-adaptive
> 4. **If agent compliance is low**: check "Anti-Pattern Gallery" — your injection may be prose-formatted
> 5. **For context budget decisions**: read "Tier Budget Standards" — right depth for right trust level

## Summary

This page defines the quality bar for CONTEXT ENGINEERING — the discipline of designing what information reaches an AI agent, in what structure, at what depth, for what context. Where [[model-context-engineering|Model — Context Engineering]] defines the SYSTEM (three levels, autocomplete chain, tiers, five cognitive contexts), this page shows what it looks like when context injections are designed WELL — and what they look like when they fail. The core principle: ==structure governs agent behavior more than content.== Same rules delivered as prose achieve ~25% compliance; delivered as structured tables achieve ~60%; delivered as infrastructure (hooks) achieve ~100%.

## Key Insights

- **The three levels are not optional tiers — they're mandatory layers.** Prompt engineering (word choice) + context engineering (selection + ordering) + structural engineering (form + consistency) = complete context design. Skipping structural engineering means your carefully selected content is delivered in a form the agent processes poorly.

- **Consistency across injections matters more than any single injection's quality.** OpenFleet's validation matrix: 29 scenarios, same structural skeleton, content varies. The agent learns the PATTERN; content fills the slots. If every injection uses a different format, the agent can't build recognition.

- **Context compaction destroys content, preserves structure.** After compaction, prose corrections are gone. But YAML files, typed fields, and stage declarations survive because post-compact hooks can rebuild them from authoritative files. Design injections as structures that survive compaction.

- **Per-context targeting eliminates cross-context pollution.** Five cognitive contexts (operator, solo agent, sub-agent, persona template, provisioned agent) read CLAUDE.md. Rules meant for the operator confuse sub-agents. Rules meant for harness-managed agents restrict solo operators. Mark which context each section addresses.

- **Tier budgets are not about cost — they're about noise.** Expert tier (5,000-10,000 tokens) gives maximum context. Lightweight tier (500-1,000 tokens) gives minimum viable. The budget isn't about saving money — it's about preventing context noise that degrades decision quality. More context ≠ better decisions above a threshold.

## Deep Analysis

### Gold Standard: CLAUDE.md Structure

What a well-structured CLAUDE.md looks like — the primary context injection point.

> [!success] Gold Standard Elements
>
> | Element | What It Does | Why It Works |
> |---------|-------------|-------------|
> | **Sacrosanct section** | Operator words verbatim at top, clearly marked immutable | Agent cannot reinterpret. Preserved across 10+ methodology versions (OpenArms evidence). |
> | **Identity Profile table** | 7 Goldilocks dimensions in YAML-style table | Each field narrows behavior space. `domain: typescript` selects TypeScript artifact chains. `phase: production` activates full enforcement. |
> | **ALLOWED / FORBIDDEN table** | Per-stage permissions in table format | Binary constraints. No interpretation needed. Agent finds its current stage, reads the row. Compliance: 25%→60% from restructuring alone (OpenArms v8→v9). |
> | **Numbered hard rules** | Sequential, non-negotiable rules with numbers | Numbers create sequence. "Rule 3: ALWAYS read full files" is processed as ordered constraint. Unnumbered bullets get reordered or skipped. |
> | **Soft rules as judgment table** | Rule + Guidance columns | Separates mandatory from judgment. Agent knows which rules allow exceptions and which don't. |
> | **Tooling reference** | Commands with exact syntax, grouped by category | Agent copies commands verbatim. No hallucinated flag names. No invented subcommands. |

> [!warning] Common CLAUDE.md Failures
>
> | Failure | What It Looks Like | Why It Fails |
> |---------|-------------------|-------------|
> | **Prose rules** | "Try to follow the stage gates when possible" | "Try" and "when possible" are escape hatches. Agent takes them. Use MUST/MUST NOT. |
> | **Mixed contexts** | Operator instructions and agent instructions in one section | Sub-agents inherit CLAUDE.md but shouldn't follow operator-specific rules. Context pollution. |
> | **Encyclopedia CLAUDE.md** | 500+ lines of everything the agent might need | Context window pollution. Agent drowns in information. Keep CLAUDE.md as a routing table (<200 lines), delegate depth to skills. |
> | **Stale rules** | Rules referencing removed files or old commands | Agent follows stale rule, hits error, loses trust in the file. Stale rules are worse than no rules. |

### Gold Standard: Skill Injection

What a well-designed skill looks like — on-demand context injection.

> [!success] Skill Design Standards
>
> | Aspect | Standard | Why |
> |--------|---------|-----|
> | **Stage awareness** | Skill declares which stages it applies to | A TDD skill in document stage wastes context and confuses the agent. skill-stage-mapping.yaml (299 lines, 3 layers) blocks incompatible skills. |
> | **Structural consistency** | Same section order across all skills | Agent builds recognition. Header → checklist → constraints → examples → done-when. Every skill, same skeleton. |
> | **MUST/MUST NOT format** | Binary constraints in bulleted lists | Not "consider doing X" but "MUST: X. MUST NOT: Y." Binary constraints have 2-3x higher compliance than suggestive guidance. |
> | **Tier adaptation** | Expert gets full protocol, lightweight gets title + stage only | Same structure at every tier — only content depth varies. 10x cost difference, same behavioral programming. |
> | **Exit criteria** | Explicit "this skill is complete when:" section | Without exit criteria, the agent runs the skill indefinitely or exits prematurely. Named artifacts + gate commands = deterministic completion. |

### Gold Standard: Task Context Template

What well-designed task context looks like — injected per-task by harness or operator.

> [!success] Task Context Elements
>
> | Element | What It Contains | Why It's There |
> |---------|-----------------|---------------|
> | **Task identity** | Title, type, current stage, Done When | Immediate orientation. Agent knows what it's doing and when it's done. |
> | **Contributions** | Inputs from other tasks/stages | Agent has what it needs without searching. Contribution gating: these inputs were validated before dispatch. |
> | **Stage rules** | MUST/MUST NOT for current stage | Duplicated from CLAUDE.md but FOCUSED. Only this stage's rules, not all stages. |
> | **Prior artifacts** | What previous stages produced (file paths) | Agent can reference without re-reading. "Design doc: docs/design-plan.md" — the path IS the context. |
> | **Confirmed plan** | What the human approved (if applicable) | Prevents agent from re-planning. The plan was confirmed; execute it, don't redesign it. |

### Tier Budget Standards

> [!abstract] Context Budget by Tier — What Goes In, What Stays Out
>
> | Tier | Token Budget | Includes | Excludes | When to Use |
> |------|-------------|----------|----------|-------------|
> | **Expert** | 5,000-10,000 | Full task detail, contributions inline, full protocol, 10 events history, standing orders | Nothing — maximum context | Trusted agents, complex tasks, production critical |
> | **Capable** | 2,000-5,000 | Core fields, contribution status (not full text), MUST/MUST NOT, top-3 items, 5 events | Standing orders, full contribution text, events beyond 5 | Standard agents, moderate tasks |
> | **Lightweight** | 500-1,000 | Title + stage only, contribution names (not content), short rules, counts only, 0 events | Everything detailed — minimum viable context | New/untrusted agents, simple tasks, cost-constrained |
>
> **The budget is a MAXIMUM, not a target.** A simple task at expert tier shouldn't be padded to 5,000 tokens. The budget prevents EXCEEDING the threshold, not missing it.

### The Autocomplete Chain — How Context Builds

> [!info] Progressive Context Assembly (8 Steps)
>
> | Step | What Gets Added | When | Survives Compaction? |
> |------|----------------|------|---------------------|
> | 1. CLAUDE.md | Project identity, hard rules, stage gates | Session start | YES (file-based) |
> | 2. Identity Profile | Goldilocks dimensions | Session start | YES (CLAUDE.md table) |
> | 3. Chain Selection | Simplified/default/full | Session or task start | YES (config file) |
> | 4. Model Selection | Feature-dev/research/bug-fix | Task dispatch | YES (frontmatter) |
> | 5. Stage Skill | Per-stage MUST/MUST NOT, tools, artifacts | Stage entry | YES (skill files) |
> | 6. Task Context | Title, stage, Done When, contributions, plan | Per-task | PARTIAL (frontmatter yes, prose no) |
> | 7. Prior Artifacts | What previous stages produced | Per-stage | YES (stage-files.log) |
> | 8. Post-Compact Rebuild | Full state from authoritative files | After compaction | BY DESIGN (hook rebuilds) |
>
> Steps 1-5 are FILE-BASED — they survive compaction because a post-compact hook can re-read them. Steps 6-7 are PARTIALLY file-based — task frontmatter survives but prose context doesn't. Step 8 is the safety net — it rebuilds everything from files.

### Anti-Pattern Gallery

> [!warning] Context Engineering Anti-Patterns
>
> | Anti-Pattern | What It Looks Like | Why It Fails | The Fix |
> |-------------|-------------------|-------------|---------|
> | **Prose instructions** | "Please follow the stage gates and produce the required artifacts" | ~25% compliance. Agent parses intent, not structure. | MUST/MUST NOT lists in table format. |
> | **Context dump** | 10,000 tokens of everything possibly relevant | Agent drowns. Important rules buried in noise. Quality DROPS above a threshold. | Tier-appropriate budget. Expert gets everything; lightweight gets essentials only. |
> | **Stale context** | Post-compact hook doesn't exist or doesn't rebuild | Agent forgets corrections, reverts to pre-correction behavior | Post-compact hook reads authoritative files, reconstructs full state. |
> | **Format inconsistency** | CLAUDE.md uses tables, skills use prose, task context uses bullets | Agent can't build pattern recognition across injections. Each format is a new language. | Same structural skeleton everywhere. Content varies; structure is constant. |
> | **Cross-context pollution** | Sub-agent receives operator-level rules | Sub-agent has no CLAUDE.md access. Rules designed for interactive sessions confuse it. | Mark sections by context (A-E). Sub-agents get spawn-prompt rules only. |
> | **Implicit ordering** | "These rules apply" with no priority | Agent picks whichever rule is most convenient. Priority conflicts silently resolved. | Numbered sequential rules. Or explicit priority: "Rule 3 overrides Rule 7 when..." |

### Annotated Exemplar: [[model-context-engineering|Model — Context Engineering]]

> [!example]- Full Walkthrough — Why This Model Exemplifies Its Own Standards
>
> **1. Three-level framework with measured compliance** — The model defines prompt engineering (~25%), context engineering (~60%), and structural engineering (~90%+) with MEASURED compliance percentages from OpenArms v4-v10 data. ← This is not theoretical — the compliance gap was observed in production and the numbers come from real overnight runs. The model practices what it preaches: structure (the table format) delivers the information better than prose would.
>
> **2. Five cognitive contexts with per-context design** — The model identifies A through E (operator, solo, sub-agent, persona, provisioned) and provides a table mapping each context to what it needs and how to deliver. ← This section demonstrates per-context targeting — the model itself is structured so a reader can find THEIR context's row and ignore the rest.
>
> **3. Autocomplete chain as progressive assembly** — 8-step table showing how context BUILDS from CLAUDE.md through stage skills through task context. Each step names: what gets added, source, when. ← Progressive assembly is the model's key architectural insight. The table makes it mechanical — an agent or harness can implement each step without design decisions.
>
> **4. Honest State of Knowledge** — Well-covered lists 6 items with specific evidence. Thin/unverified lists 4 genuine gaps (smart autocomplete not implemented, budgets are estimates, formal grammar undefined, per-context CLAUDE.md splitting not done). ← The model doesn't claim completeness. The gaps are genuine research questions, not polish items.
>
> **What could still improve:** The model lacks worked examples showing a real CLAUDE.md section annotated with "this is prompt engineering / this is context engineering / this is structural engineering." The tier budgets (500/2,000/5,000) are estimates, not empirically measured.

### How This Connects — Navigate From Here

> [!abstract] From This Standards Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The model this standards page serves** | [[model-context-engineering|Model — Context Engineering]] |
> | **The principle behind it** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] |
> | **The proto-programming lesson** | [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]] |
> | **The tier system** | [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]] |
> | **The validation matrix** | [[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]] |
> | **CLAUDE.md patterns** | [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]] |
> | **Global wiki standards** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] |
> | **Model Registry** | [[model-registry|Model Registry]] |

## Relationships

- BUILDS ON: [[model-context-engineering|Model — Context Engineering]]
- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- RELATES TO: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
- RELATES TO: [[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]]
- RELATES TO: [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-context-engineering|Model — Context Engineering]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]]
[[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

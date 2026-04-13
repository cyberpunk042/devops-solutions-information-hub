---
title: Model — Context Engineering
aliases:
  - "Model — Context Engineering"
  - "Model: Context Engineering"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: proto-programming-lesson
    type: wiki
    file: wiki/lessons/03_validated/structured-context-is-proto-programming-for-ai-agents.md
  - id: five-contexts
    type: observation
    file: raw/articles/openarms-all-distilled-lessons.md
    description: Five cognitive contexts reading one CLAUDE.md
  - id: validation-matrix
    type: observation
    file: raw/articles/openfleet-validation-matrix-samples.md
    description: 29 structured context scenarios (2,444 lines)
  - id: operator-directive
    type: directive
    file: raw/notes/2026-04-12-mega-vision-directive.md
tags: [model, spine, context-engineering, proto-programming, prompt-engineering, structure, tiers]
---

# Model — Context Engineering
## Summary

Context engineering is the discipline of designing WHAT information reaches an AI agent, in WHAT STRUCTURE, at WHAT DEPTH, for WHAT CONTEXT. It goes beyond prompt engineering (word choice) into structural engineering — using markdown's native constructs (headers, tables, callouts, YAML blocks, code fences) as a programming language for AI behavior. The model covers three levels: prompt engineering (content), context engineering (selection + ordering), and structural engineering (form + consistency). It also covers context capacity management: tiers, budgets, compaction survival, and the autocomplete chain (how context builds progressively from identity through chain through stage through artifacts).

## Key Insights

1. **Three levels of agent configuration — structure wins.**

> [!abstract] The Three Levels
>
> | Level | What It Controls | Mechanism | Measured Compliance |
> |-------|-----------------|-----------|-------------------|
> | **Prompt engineering** | What the agent is TOLD | Word choice, emphasis, phrasing | ~25% (degrades under context pressure) |
> | **Context engineering** | What information the agent RECEIVES | Selection, ordering, filtering | ~60% (right info helps, format matters) |
> | **Structural engineering** | What SHAPE the information takes | Headers, tables, YAML, callouts, MUST/MUST NOT | ~90%+ (agent processes structure before content) |

2. **Markdown IS the programming language of AI.** Not a metaphor. When an agent sees `### MUST NOT:` followed by a bulleted list, it processes the pattern as a constraint. When it sees a `> [!warning]` callout, it processes it as high-priority. The STRUCTURE programs behavior through FORM, not meaning.

3. **Consistent structure across all injections = predictable behavior.** OpenFleet's validation matrix: 29 scenarios, same structural skeleton, content varies. Same pattern at every tier (expert gets full content, lightweight gets titles only — but the STRUCTURE is identical). Consistency is what the agent learns; content is what varies.

4. **Five cognitive contexts reading one file = structural failure.** OpenArms discovered that CLAUDE.md is read by 5 different contexts (operator, solo agent, sub-agent, persona template, provisioned agent). Rules meant for one context mislead another. Fix: structurally MARK which context each section addresses, or separate into context-specific injection points (skills, commands).

5. **Context compaction destroys content, preserves structure.** After compaction, prose corrections are lost. But structured state (YAML files, typed fields, stage declarations) can be rebuilt by post-compact hooks. Design injections as structures that survive compaction, not prose that requires re-reading.

6. **Tier-based depth controls cost without changing structure.** Expert tier: full content inline. Lightweight: title + stage only. 10x cost difference. Same structural skeleton at every tier — the agent processes the same pattern regardless of depth.

## Deep Analysis

### The Context Autocomplete Chain

How context BUILDS progressively from first contact to full execution:

> [!info] The Chain
>
> | Step | What Gets Added | Source | When |
> |------|----------------|--------|------|
> | 1. CLAUDE.md | Project identity, hard rules, stage gates | Loaded at session start | Always |
> | 2. Identity Profile | Goldilocks dimensions: type, mode, domain, phase, scale | CLAUDE.md table or auto-detect | Always |
> | 3. Chain Selection | Simplified/default/full → determines process weight | From identity + gateway | Session start or task start |
> | 4. Model Selection | Feature-dev/research/bug-fix → determines stages | From task type | Task dispatch |
> | 5. Stage Skill | Per-stage protocol: MUST/MUST NOT, recommended tools, artifact requirements | Skill injection | Stage entry |
> | 6. Task Context | Current task: title, stage, Done When, contributions, confirmed plan | Harness builds | Per-task |
> | 7. Prior Artifacts | What previous stages produced (for reference during later stages) | From stage-files.log | Per-stage |
> | 8. Post-Compact Rebuild | Full task state reconstructed from authoritative files | Post-compact hook | After compaction |

Each step ADDS to the context. The chain is PROGRESSIVE — later steps build on earlier ones. If step 2 (identity) is wrong, every later step is miscalibrated.

### Context Capacity and Budgeting

> [!abstract] Context Budget by Tier
>
> | Tier | Approximate Tokens | What's Included | What's Excluded |
> |------|-------------------|-----------------|-----------------|
> | Expert | 5,000-10,000 | Full task detail, contributions inline, full protocol, 10 events, standing orders | Nothing — maximum context |
> | Capable | 2,000-5,000 | Core fields, contribution status, MUST/MUST NOT, top-3 items, 5 events | Standing orders, full contribution text, events beyond 5 |
> | Lightweight | 500-1,000 | Title + stage only, contribution names, short rules, counts only, 0 events | Everything detailed — minimum viable context |

**The budget tradeoff:** More context = more information for better decisions. But also: more context = more noise, higher cost, faster degradation. The Goldilocks principle applies to context too — "just right" is the tier that matches the agent's trust level and the task's complexity.

### Structural Patterns That Work

> [!info] Proven Structural Patterns for AI Context
>
> | Pattern | What It Does | Where Used | Evidence |
> |---------|-------------|-----------|---------|
> | **Sacrosanct section** | Verbatim operator words at top, clearly marked immutable | CLAUDE.md | OpenArms: operator directives preserved across 10 methodology versions |
> | **MUST / MUST NOT lists** | Binary constraints as bulleted lists under labeled headers | Stage skills, task context | OpenFleet: every task context uses this exact format |
> | **ALLOWED / FORBIDDEN tables** | Per-stage artifact permissions in table format | CLAUDE.md, methodology.yaml | OpenArms: stage boundary compliance 25%→60% from restructuring alone |
> | **Numbered sequences** | Steps that must follow order | Work loops, methodology stages | Cognitive chain: numbered items create sequential processing |
> | **Typed callouts** | `> [!warning]` for risks, `> [!tip]` for guidance, `> [!info]` for reference | Wiki pages, standards | Semantic: callout type tells the reader KIND of information |
> | **YAML frontmatter** | Typed fields that narrow behavior space | Every wiki page | Each field programs one dimension: type → rules, maturity → evolution |
> | **Reference cards** | Compact table at page top summarizing key attributes | Source syntheses, patterns | Immediate orientation: reader decides relevance in seconds |
> | **Decision tables** | Scenario → action mapping | Goldilocks flow, model selection | Agent finds its row, reads the action — no parsing required |

### Per-Context Injection Design

> [!warning] The Five Contexts Problem and Its Solution
>
> | Context | What It Is | What It Needs | How to Deliver |
> |---------|-----------|---------------|---------------|
> | A. Interactive operator | Human in terminal | Operator-level rules, investigation tools | CLAUDE.md shared section |
> | B. Solo agent (run mode) | Harness-spawned session | Methodology hooks, stage rules, artifact requirements | Stage SKILLS (injected by harness) |
> | C. Sub-agents | Throwaway research workers | Minimal behavioral rules | In the spawn PROMPT (can't access CLAUDE.md) |
> | D. Persona template | Source-of-truth for provisioning | Not read at runtime | Separate template files |
> | E. Provisioned agent | Continuously alive, heartbeat-driven | Heartbeat rules, persistent memory | Workspace-specific AGENTS.md |
>
> **Design principle:** Shared rules in CLAUDE.md (clearly marked). Context-specific rules in their injection point (skills for B, prompt text for C, workspace files for E). NEVER mix contexts without markers.

### Lessons Learned

| Lesson | What Was Learned |
|--------|-----------------|
| [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]] | Structure governs behavior more than content. Same rules: prose=25%, tables=60%. |
| [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] | Prose corrections lost. Structured state rebuilds from files. |
| [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] | Class 5 (sub-agent non-compliance): sub-agents don't inherit CLAUDE.md. ~33% compliance in prompts. |
| [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]] | 8 patterns quantified. Sacrosanct + numbered + ALLOWED/FORBIDDEN = highest compliance. |

### State of Knowledge

> [!success] **Well-covered**
> - Three levels of configuration (prompt/context/structural) with measured compliance per level
> - 8 structural patterns documented with evidence from OpenArms/OpenFleet
> - Five cognitive contexts identified with per-context injection design
> - Tier-based context depth with 3 tiers and cost data (10x difference)
> - Context autocomplete chain (8 steps from CLAUDE.md to post-compact rebuild)
> - Validation matrix concept (29 scenarios = test suite for context injection)

> [!warning] **Thin or unverified**
> - Smart autocomplete chain not implemented in tooling (documented but not automated)
> - Context capacity budgets are estimates (500/2,000/5,000 tokens) — not measured empirically
> - Formal structural grammar not defined (what are the "language constructs" of markdown as programming?)
> - Per-context CLAUDE.md splitting not implemented (OpenArms still has one file for 5 contexts)

## Open Questions

> [!question] ~~Can we define a formal grammar for structured context?~~
> **RESOLVED:** Partially. Informal grammar in model-context-engineering. Formal grammar needs research into LLM markdown parsing behavior.
> Headers = scope. Callouts = typed blocks. Tables = decision matrices. YAML = typed parameters. Can we formalize this into a grammar that GENERATES valid context injections? (Requires: analysis of all validation matrix scenarios for common constructs.)

> [!question] What is the optimal context budget per tier?
> The 500/2,000/5,000 estimates are from OpenFleet's tier profiles. Are they optimal? (Requires: measuring output quality vs context size across tasks.)

### How This Connects — Navigate From Here

> [!abstract] From This Model → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The principle this implements** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] |
> | **The sub-super-model** | [[knowledge-architecture|Sub-Model — Knowledge Architecture — Layers, Maturity, and Evolution]] |
> | **The enforcement hierarchy** | [[enforcement-hierarchy|Sub-Model — Enforcement Hierarchy — From Instructions to Immune System]] |
> | **The validation matrix pattern** | [[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]] |
> | **The tier system** | [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]] |
> | **The Goldilocks flow** | [[goldilocks-flow|Goldilocks Flow — From Identity to Action]] — context depth adapts per identity |
> | **Templates as proto-programming** | [[e012-template-enrichment-rich-proto-programming-examples|E012 — Template Enrichment — Rich Proto-Programming Examples]] |

## Relationships

- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- BUILDS ON: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
- RELATES TO: [[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]]
- RELATES TO: [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
- RELATES TO: [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
- FEEDS INTO: [[goldilocks-flow|Goldilocks Flow — From Identity to Action]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]]
[[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]
[[model-claude-code|Model — Claude Code]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[goldilocks-flow|Goldilocks Flow — From Identity to Action]]
[[methodology-adoption-guide|Methodology Adoption Guide]]

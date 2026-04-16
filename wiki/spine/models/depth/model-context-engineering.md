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
updated: 2026-04-14
sources:
  - id: src-openspec-spec-driven-development-framework
    type: wiki
    file: wiki/sources/tools-integration/src-openspec-spec-driven-development-framework.md
    title: Synthesis — OpenSpec Spec-Driven Development Framework
  - id: src-github-spec-kit-specification-driven-development
    type: wiki
    file: wiki/sources/tools-integration/src-github-spec-kit-specification-driven-development.md
    title: "Synthesis — GitHub Spec Kit: Specification-Driven Development"
  - id: src-bmad-method-agile-ai-development-framework
    type: wiki
    file: wiki/sources/tools-integration/src-bmad-method-agile-ai-development-framework.md
    title: Synthesis — BMAD-METHOD Agile AI-Driven Development Framework
  - id: src-skillmd-claudemd-agentsmd-three-layer-context
    type: wiki
    file: wiki/sources/tools-integration/src-skillmd-claudemd-agentsmd-three-layer-context.md
    title: Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md Three-Layer Context
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

### Key Pages

| Page | Layer | Role in the model |
|------|-------|-------------------|
| [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]] | lesson | The core insight — structure programs behavior |
| [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]] | pattern | 8 quantified patterns for agent context |
| [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] | lesson | Why structured state survives compaction |
| [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth]] | pattern | Expert/capable/lightweight tier system |
| [[validation-matrix-test-suite-for-context-injection|Validation Matrix]] | pattern | 29-scenario test suite for context injection |
| [[model-markdown-as-iac|Model — Markdown as IaC]] | model | How markdown files configure agent behavior |
| [[model-context-engineering-standards|Context Engineering Standards — What Good Structured Context Looks Like]] | standards | What good injections look like — gold standards + anti-patterns |
| [[block-with-reason-and-justified-escalation\|Block With Reason and Justified Escalation]] | L5 | Structured escalation-protocol: 4-part schema (Block + Reason + Offer + Justification). The proto-programming principle applied to agent-operator communication at decision boundaries. Added 2026-04-15. |
| [[adapters-never-raise-failure-as-data-at-integration-boundaries\|Adapters Never Raise — Failure as Data]] | L5 | Structured-result-type pattern at integration boundaries — format-as-enforcement at the function-return level. Same principle as "JSON over Markdown" finding in §Format-as-Enforcement, applied to Python return values. Added 2026-04-15. |
| [[observe-fix-verify-loop\|Observe-Fix-Verify Loop]] | L5 | The iteration pattern that produces structural refinement. Every OFV cycle Observes what current structure fails to enforce and Fixes the structure (not the instructions). Added 2026-04-15. |
| [[execution-mode-is-consumer-property-not-project-property\|Execution Mode Is a Consumer Property]] | L4 | Three-layer orthogonality — context authority comes from project (stable), project-declared (phase/scale), and consumer-declared (per-connection) layers. Conflating layers produces the "detect what the consumer must declare" failure mode. Added 2026-04-15. |
| [[consumer-runtime-signaling-via-mcp-config\|Decision — Consumer Runtime Signaling via MCP Config]] | L6 | Implementation of the consumer layer: `MCP_CLIENT_RUNTIME` env var carries the declaration via MCP's standard `env:` block. Context engineering at the protocol boundary. Added 2026-04-15. |

### Worked Examples — Context Engineering in Practice

> [!example]- Example 1: CLAUDE.md Identity Profile — Three Levels in Action
>
> **Prompt engineering (Level 1):** "This project uses TypeScript and should follow stage gates."
> → Agent knows the words but compliance is ~25%. "Should" is an escape hatch.
>
> **Context engineering (Level 2):** The Identity Profile table is placed BEFORE the rules section, so the agent processes identity before constraints. The domain field is listed first (most specific), execution mode last (requires inference).
> → Right information in right order improves compliance to ~60%.
>
> **Structural engineering (Level 3):**
> ```
> | Dimension | Value |
> |-----------|-------|
> | **Domain** | typescript |
> | **Phase** | production |
> ```
> → Table format. Bold dimension names. Each row narrows one behavioral axis. Agent processes the STRUCTURE (table = parameters, bold = field name, value = constraint) before the content. Compliance ~90%+.
>
> **The insight:** Same information, three delivery formats, 4x compliance difference. The structure IS the engineering.

> [!example]- Example 2: Stage Skill Injection — Per-Stage Context
>
> **What gets injected at the DOCUMENT stage:**
> ```markdown
> ### DOCUMENT STAGE — Rules for This Stage
>
> **MUST:**
> - Read all existing wiki pages in the domain before creating new ones
> - Log operator directives verbatim in raw/notes/
> - Run `pipeline post` after every wiki change
>
> **MUST NOT:**
> - Write implementation code
> - Modify tool files
> - Skip to scaffold without completing research
>
> **RECOMMENDED TOOLS:** wiki_search, wiki_read_page, wiki_status
> **BLOCKED TOOLS:** (none at document stage)
> **EXIT GATE:** `pipeline post` returns 0 errors
> ```
>
> **Why this works:** MUST/MUST NOT format is binary — no interpretation. Tool recommendations guide without restricting. The exit gate is a concrete command that returns a concrete result. The agent doesn't decide when the stage is done; the gate command does.
>
> **What changes per tier:** Expert gets the full block above. Lightweight gets: "Stage: document. MUST: research before writing. EXIT: pipeline post." Same structure, 10x less content.

> [!example]- Example 3: Post-Compact Hook — Surviving Context Reset
>
> **The problem:** After compaction, the agent loses: which stage it's in, what corrections were made, which files were produced, what the confirmed plan was. All prose context is gone.
>
> **The hook (PostCompact event):**
> ```
> 1. Read task frontmatter → rebuild: current_stage, readiness, progress, artifacts
> 2. Read stage-files.log → rebuild: prior stage artifacts (file paths)
> 3. Read confirmed-plan.md → rebuild: what was approved
> 4. Inject via additionalContext → agent receives full state
> ```
>
> **Why this works:** Every piece of state has a FILE SOURCE. The hook reads files (which survive compaction) and reconstructs the context that prose couldn't preserve. This is structural engineering at its purest — designing state to be reconstructable from persistent storage.
>
> **The invariant:** If a piece of context can't be rebuilt from files, it will be lost after compaction. Design accordingly: write state to files, not to conversation.

### How to Adopt

> [!info] What you need
> - CLAUDE.md with structured sections (headers, tables, MUST/MUST NOT lists)
> - Consistent formatting across ALL context injections (skills, prompts, stage protocols)
> - Per-context markers if multiple cognitive contexts read the same file

> [!warning] Invariants (do not change per project)
> - Structure governs behavior more than content — this is the fundamental principle
> - Compaction destroys prose, preserves structure — design for survival
> - Sub-agents don't inherit CLAUDE.md — inject rules in the spawn prompt

> [!tip] Per-project adaptations
> - Tier system (expert/capable/lightweight) adapts to your trust levels
> - Context budget depends on your typical task complexity and context window size
> - Structural patterns can be customized but the CONSISTENCY matters more than the specific patterns

### Industry Frameworks — Structured Context in Production (NEW 2026-04-14)

Four production frameworks from 2026 independently converge on the same structural context principles this model defines — validating that context engineering is a domain-level pattern, not an ecosystem-specific practice.

**[[src-openspec-spec-driven-development-framework|OpenSpec]]: Fluid vs Phase-Locked Context + Delta Specs**

OpenSpec is a spec-driven development framework with 25+ AI tools in production. It introduces two context modes that directly map to our tier system: *fluid actions* (context adapts continuously as implementation reveals information) versus *phase-locked actions* (context frozen at phase boundaries, preventing retroactive scope expansion). The delta spec mechanism — structuring changes as ADDED/MODIFIED/REMOVED blocks — is a structural pattern for communicating context *differences* rather than full state, solving the compaction problem: a delta spec survives context resets because it describes what changed, not the full prior state. The OPSX command system provides a unified vocabulary for agent interaction — the same design goal as our per-role command segmentation. OpenSpec demonstrates that structural context engineering at 25+ tool scale requires vocabulary discipline: consistent verbs, consistent section headers, consistent change notation.

**[[src-github-spec-kit-specification-driven-development|spec-kit]]: Specs Generate Code, Not Guide It**

The spec-kit project formalizes the SDD (Specification-Driven Development) philosophy: a specification is the primary artifact, and code is a derived output. The kit provides 6 structural mechanisms — abstraction enforcement (verifies spec maps to code), uncertainty markers (`?:` prefix flags unresolved decisions inline), section checklists (completeness gates embedded in the spec itself), constitutional compliance (AI behavior constraints in the spec), plus standard template and example library. The key structural insight: *uncertainty markers in a spec are the equivalent of our `> [!warning]` callouts* — they tell the agent which decisions require escalation versus auto-resolution. Checklists embedded in specs are the equivalent of our MUST/MUST NOT lists in stage skills. This validates the claim that structural context engineering converges on similar patterns across different tools and domains.

**[[src-bmad-method-agile-ai-development-framework|BMAD]]: Scale-Adaptive Context Ceremony**

BMAD-METHOD implements Scale-Domain-Adaptive context: the amount of structured ceremony (formal specs, approvals, documentation) adapts based on project scale and domain. For a solo project, a single markdown spec file is sufficient; for a 12-agent coordinated workflow, each persona requires a dedicated context specification. BMAD's 12+ specialized agent personas each carry a context specification calibrated to that persona's role — the same per-context injection design as our Five Contexts section (A through E). The 60+ brainstorming techniques in BMAD are all *structured prompts* — not free-form questions but context engineering artifacts that program how the agent explores a problem space. BMAD demonstrates at scale (active community, 12+ personas) that structured context engineering is not overhead — it is what makes multi-agent coordination tractable.

**[[src-skillmd-claudemd-agentsmd-three-layer-context|Three-Layer Context Architecture]]: ETH Zurich Feb 2026 Finding**

The cross-tool analysis of SKILL.md vs CLAUDE.md vs AGENTS.md documents the emergence of a three-layer context standard: AGENTS.md (universal cross-tool, <100 lines, always loaded) + CLAUDE.md (tool-specific minimal config, <20 lines) + Skills (conditional, <500 lines, on-demand). This is precisely the context-aware loading principle expressed as a file architecture standard. The critical empirical finding: ETH Zurich (Feb 2026) measured that AI-generated context files *hurt success by 3%* compared to human-written context files. The mechanism: AI-generated context files include LLM-optimized phrases ("As an AI assistant...") that consume tokens without improving behavior — they are structurally correct but content-bloated. This is quantitative evidence that *content discipline matters as much as structural discipline* in context engineering. The principle: every line in a context file must earn its place, not just conform to format.

> [!info] **Four-framework convergence summary**
>
> | Framework | Key structural mechanism | Maps to our model |
> |-----------|------------------------|-------------------|
> | OpenSpec | Delta specs (ADDED/MODIFIED/REMOVED) | Compaction-survival design |
> | spec-kit | Uncertainty markers + constitutional compliance | `> [!warning]` callouts + MUST NOT lists |
> | BMAD | Scale-adaptive ceremony, persona-specific specs | Tier system + per-context injection |
> | Three-layer | AGENTS.md (<100L) + CLAUDE.md (<20L) + Skills (<500L) | Context-aware loading principle |
>
> Convergence across 4 independent frameworks on structured context, tiered depth, and per-context injection validates that these are domain-level patterns — not preferences or ecosystem quirks.

### The OS Analogy — Context as RAM (NEW 2026-04-15)

The harness-engineering field has crystallized a powerful pedagogical reframing of the entire LLM stack — and context is the load-bearing piece in the middle:

| LLM system | OS analog | Context-engineering implication |
|------------|-----------|-------------------------------|
| Raw LLM | CPU | Powerful but inert — needs context to act |
| **Context window** | **RAM** | **Fast but volatile + size-limited — what's in context governs what the model does this call** |
| External databases / wiki / RAG | Disk | Slow but persistent — context fetches from here |
| Tool integrations (MCP, CLI) | Device drivers | Mediated I/O — context contains tool descriptions |
| Harness | Operating system | Decides what gets loaded into RAM (context) at each call |

Source: [[src-rethinking-ai-agents-harness-engineering-rise|Rethinking AI Agents — The Rise of Harness Engineering]] meta-synthesis. This analogy reframes context engineering as **RAM management for LLMs** — and context engineering's tier system (lightweight / capable / expert) becomes RAM allocation policy. The Goldilocks principle in this lens: don't load expert-tier RAM for a lightweight task; you waste the limited window.

### Quantified Context Efficiency — Meta-Harness (NEW 2026-04-15)

[[src-arxiv-meta-harness-outer-loop-search|Meta-Harness (Stanford, March 2026)]] empirically measured the leverage of better context management:

> **+7.7 points improvement over a state-of-the-art context management system, while using 4× FEWER context tokens.**

Same task, same model. Better context engineering = better accuracy AND lower cost simultaneously. Two implications for this model:

1. **The tier-system + per-context injection design has measurable upside** — quantification was previously qualitative; now there's a citable +7.7 / 4× number.
2. **Context efficiency is searchable** — Meta-Harness used outer-loop search to discover better context strategies. The wiki could adopt the same pattern for self-improvement (proposer + verifier + filesystem memory of prior candidates). See [[harness-engineering-is-the-dominant-performance-lever|Harness Engineering Is the Dominant Performance Lever]] for the broader pattern.

### Format-as-Enforcement — JSON over Markdown for State Files (NEW 2026-04-15)

[[src-anthropic-effective-harnesses-long-running-agents|Anthropic — Effective Harnesses for Long-Running Agents]] documents a load-bearing micro-finding:

> "We landed on using JSON for [the feature list], as the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files."

This is **format-as-enforcement** — the structural rigidity of the file format itself constrains the agent's behavior. Same insight as [[structured-context-governs-agent-behavior-more-than-content|Structured Context Governs Agent Behavior More Than Content]] applied to the FILE FORMAT level rather than the content level.

For this wiki: methodology.yaml is YAML (structurally rigid) for the same reason — the agent doesn't casually rewrite YAML the way it casually rewrites prose. Wiki page frontmatter is YAML for the same reason. The choice of file FORMAT is itself enforcement infrastructure. Add to context-engineering's structural principles section as a tactical guideline.

---

### Three-Layer Orthogonality — Context Authority by Layer (NEW 2026-04-15)

A context-engineering principle surfaced by the [[execution-mode-is-consumer-property-not-project-property|Consumer Property lesson]] that this model previously did not explicitly articulate: **context dimensions are not uniform** — they come from **three different authorities**, each with distinct loading mechanisms, caching policies, and failure modes when conflated.

> [!abstract] The Three Authorities of Agent Context
>
> | Layer | Properties | Declared by | Loading mechanism | Changes |
> |---|---|---|---|---|
> | **Stable project identity** | type, domain, second-brain, repo topology | The project (CLAUDE.md, CONTEXT.md, AGENTS.md) | Loaded at session start from repo files — authoritative | Rarely (quarters/years) |
> | **Phase / scale state** | phase, scale, PM level, trust tier | The project (declared; reviewed periodically) | Loaded at session start from declarations; heuristics as sanity-check signals | Slowly (weeks/quarters) |
> | **Consumer / task properties** | execution mode, SDLC profile, methodology model, current stage | The **consumer** at connect time (for session-level) OR per-task | Consumer declares via `MCP_CLIENT_RUNTIME` env ([[consumer-runtime-signaling-via-mcp-config\|decision]]); per-task from task frontmatter | Per-session (consumer) / per-task (model/stage) |

### Why this matters for context injection

Each layer has a different **caching policy** and a different **failure mode when conflated**:

- **Stable identity**: load once per session, bake into base context. Failure mode if re-queried per task: wasted context tokens repeating the same identity block.
- **Phase/scale**: load once per session from declaration. Failure mode if heuristically "detected": wrong recommendations for the project as a whole ([[execution-mode-is-consumer-property-not-project-property|the consumer-property failure caught 2026-04-15]]).
- **Consumer properties**: attach to session at connect time from the consumer's declaration. Failure mode if the wiki tries to "detect" these from inside: tautology (solo-if-no-harness-code-here is trivially true locally) or wrong guess (containers, pipes, remote clients obscure the invoker).
- **Task properties**: compute per task from task frontmatter. Failure mode if bound project-wide: the "project frozen to one model" conflation — a production project running a hotfix doesn't want `default` profile; it wants `simplified` for THAT task.

### The symmetric rule

> [!tip] Context-engineering corollary: declared > detected
>
> For every identity/context dimension, prefer the DECLARED value from the authoritative layer over any HEURISTIC-DETECTED value. Heuristics are sanity-check signals at best — never override declarations. Tools that claim to "detect" what the consumer must declare (execution mode) are lying; tools that claim to pick a per-task value (SDLC profile) for the whole project are conflating layers.
>
> This is the same structural principle as [[structured-context-governs-agent-behavior-more-than-content|Structured Context Governs Agent Behavior]] applied at the AUTHORITY level: the STRUCTURE of declarations (who declares what, when) programs context behavior more than the content of any individual field.

### Worked example — `gateway what-do-i-need` before/after

**Before the fix (2026-04-15 morning):** the tool conflated all three layers. It claimed "DETECTED IDENTITY" for fields that were actually declared, auto-detected execution mode from filesystem heuristics, bound one SDLC profile to the whole project. Output was confidently wrong — production projects got `simplified` profile recommendations because heuristics didn't read declarations.

**After the fix:** three distinct output blocks match the three authorities — `PROJECT IDENTITY` (declared, ✓-marked), `CONSUMER / TASK PROPERTIES` (solo default; consumer declares non-default), `SUGGESTED DEFAULT PROFILE` (per-task, with explicit "override per task" caveat). The tool now honors the orthogonality structurally, not just in prose.

Full analysis: [[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]].

---

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
[[model-context-engineering-standards|Context Engineering Standards — What Good Structured Context Looks Like]]
[[context-file-taxonomy|Context File Taxonomy — The 8 Dimensions of Agent Context]]
[[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
[[gateway-output-contract|Gateway Output Contract — What Good Tool Output Looks Like]]
[[harness-engineering-is-the-dominant-performance-lever|Harness Engineering Is the Dominant Performance Lever]]
[[src-claude-code-prompt-patch-rebalancing|Source — Claude Code Prompt Patch: Rebalancing System Prompt Instructions]]
[[src-7-levels-claude-code-rag|Source — The 7 Levels of Claude Code & RAG]]
[[src-arxiv-meta-harness-outer-loop-search|Synthesis — Meta-Harness — End-to-End Optimization of Model Harnesses via Outer-Loop Search]]
[[src-skillmd-claudemd-agentsmd-three-layer-context|Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md — Three-Layer Agent Context Architecture]]
[[src-bmad-method-agile-ai-development-framework|Synthesis: BMAD-METHOD — Agile AI-Driven Development Framework]]
[[src-openspec-spec-driven-development-framework|Synthesis: OpenSpec — Spec-Driven Development Framework]]
[[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]

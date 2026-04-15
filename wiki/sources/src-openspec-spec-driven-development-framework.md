---
title: "Synthesis: OpenSpec — Spec-Driven Development Framework"
type: source-synthesis
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: openspec-github
    type: repo
    url: "https://github.com/Fission-AI/OpenSpec"
tags: [spec-driven-development, ai-agents, methodology, artifacts, commands, workflows, brownfield, sdlc]
---

# Synthesis: OpenSpec — Spec-Driven Development Framework

## Summary

OpenSpec is a lightweight, spec-driven development framework for AI coding assistants that solves the fundamental problem of AI unpredictability when requirements live only in chat history. It enforces a human-AI alignment contract through structured artifact folders (proposal → specs → design → tasks) before any code is written, then archives completed changes back into a living spec repository. The v1.0 OPSX rewrite replaced rigid phase gates with a fluid, dependency-graph-driven action model — specs and design update as understanding deepens, not when a phase gate permits.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source    | Fission-AI/OpenSpec GitHub repository (README, docs/, concepts, CLI reference, OPSX workflow guide, customization guide, migration guide, CHANGELOG) |
> | Type      | repo (30+ files fetched) |
> | Author    | Tabish Bidiwale (@TabishB), lead maintainer; Hari Krishnan, advisor |
> | Date      | 2026-04-14 (ingested); repo at v1.3.0 |
> | Key claim | AI coding without specs means vague prompts and unpredictable results; OpenSpec's artifact layer brings predictability without ceremony |

## Key Insights

### 1. The Four-Pillar Philosophy: Fluid, Iterative, Easy, Brownfield-First

OpenSpec's founding principles are stated as a manifesto in the README:

```
→ fluid not rigid
→ iterative not waterfall
→ easy not complex
→ built for brownfield not just greenfield
```

The brownfield-first emphasis is architecturally important. Traditional spec frameworks (Spec Kit, Kiro) shine for 0→1 greenfield work. OpenSpec separates `openspec/specs/` (current truth) from `openspec/changes/` (proposed updates) precisely because most real work is 1→N modification, where diffs matter more than full re-statements. The delta format was designed for this. Specs and Kiro both spread updates across spec folders making feature-level tracking harder; OpenSpec groups everything for a feature in one folder.

### 2. The Artifact System: Changes as Self-Contained Folders

Every proposed change gets a self-contained folder with a defined artifact set:

```
openspec/changes/add-dark-mode/
├── proposal.md      # WHY + WHAT — intent, scope, non-goals, approach
├── design.md        # HOW — technical decisions, architecture, data flow
├── tasks.md         # STEPS — numbered checkboxes [ ] 1.1, 1.2, 2.1...
├── .openspec.yaml   # Change metadata (schema used, created date)
└── specs/           # Delta specs — what's CHANGING relative to current truth
    └── ui/
        └── spec.md  # ADDED/MODIFIED/REMOVED requirements
```

This "change-as-folder" design has concrete benefits: parallel work (multiple changes simultaneously without conflict), clean history (archive preserves full context including the WHY), and review efficiency (one folder = one complete picture).

### 3. Delta Specs: Semantic Patching for Requirements

Delta specs are the mechanism that makes OpenSpec work for existing codebases. Instead of re-stating the entire spec, a delta describes only what's changing:

```markdown
## ADDED Requirements
### Requirement: Two-Factor Authentication
The system MUST support TOTP-based two-factor authentication.
#### Scenario: 2FA login
- GIVEN a user with 2FA enabled
- WHEN the user submits valid credentials
- THEN an OTP challenge is presented

## MODIFIED Requirements
### Requirement: Session Expiration
The system MUST expire sessions after 15 minutes of inactivity.
(Previously: 30 minutes)

## REMOVED Requirements
### Requirement: Remember Me
(Deprecated in favor of 2FA.)
```

Four delta sections: `ADDED`, `MODIFIED`, `REMOVED`, and `RENAMED`. On archive, each section is processed semantically — not brittle header matching, but requirement-level parsing that appends, replaces, or deletes as appropriate. Two parallel changes can touch the same spec file as long as they modify different requirements (conflict avoidance is structural, not procedural).

### 4. Spec Format: RFC 2119 Keywords + Given/When/Then Scenarios

Specs follow a disciplined format that separates behavioral contracts from implementation:

```markdown
## Requirements
### Requirement: User Authentication
The system SHALL issue a JWT on successful login.
#### Scenario: Valid credentials
- GIVEN a user with valid credentials
- WHEN the user submits login form
- THEN a JWT token is returned
- AND the user is redirected to dashboard
```

RFC 2119 keywords (SHALL/MUST = absolute, SHOULD = recommended, MAY = optional) communicate intent strength. The spec format deliberately excludes implementation details — no class names, library choices, or execution plans. Those belong in `design.md` and `tasks.md`. The test: if implementation can change without changing externally visible behavior, it doesn't belong in the spec.

### 5. The OPSX Command System: Actions Not Phases

OpenSpec v1.0 replaced three phase-locked commands (`/openspec:proposal`, `/openspec:apply`, `/openspec:archive`) with an action-based OPSX system driven by an artifact dependency graph. The key shift:

| Legacy (phase-locked) | OPSX (fluid actions) |
|----------------------|---------------------|
| Creates ALL artifacts at once | Creates one or all, your choice |
| Linear: plan → implement → archive | Any order that makes sense |
| Phase gates block backtracking | Edit any artifact anytime |
| Hardcoded in TypeScript source | External YAML schemas, hackable |

**Core profile commands** (default for new installs):

| Command | Purpose |
|---------|---------|
| `/opsx:propose` | Create change + all planning artifacts in one step |
| `/opsx:explore` | Think through ideas before committing to a change |
| `/opsx:apply` | Implement tasks from `tasks.md` |
| `/opsx:archive` | Finalize, merge delta specs, move to archive |

**Expanded profile commands** (opt-in via `openspec config profile`):

| Command | Purpose |
|---------|---------|
| `/opsx:new` | Scaffold change folder only |
| `/opsx:continue` | Create next ready artifact (dependency-aware) |
| `/opsx:ff` | Fast-forward: create all planning artifacts at once |
| `/opsx:verify` | Validate implementation completeness/correctness/coherence |
| `/opsx:sync` | Merge delta specs to main without archiving |
| `/opsx:bulk-archive` | Archive multiple changes with conflict detection |
| `/opsx:onboard` | Guided 11-phase tutorial on actual codebase (~15-30 min) |

### 6. The Dependency Graph Engine: State-Aware Artifact Creation

The OPSX engine tracks artifact state using a directed acyclic graph (DAG). The default `spec-driven` schema:

```
proposal (root)
    │
    ├──► specs (requires: proposal)
    │
    └──► design (requires: proposal)
              │
              └──► tasks (requires: specs + design)
                         │
                         └──► APPLY (requires: tasks)
```

State transitions: `BLOCKED → READY → DONE`. "Ready" means all dependencies exist on the filesystem. The key semantic distinction: **dependencies are enablers, not gates**. When the agent runs `/opsx:continue`, it queries the CLI for real-time state (`openspec status --change name --json`), identifies the first ready artifact, fetches rich instructions including template + project context + dependency content, creates that one artifact, and shows what's newly unlocked. This is the opposite of static instructions — the AI queries for context at execution time.

> [!warning] Context Hygiene Required
> OpenSpec recommends clearing context between planning and implementation sessions. "OpenSpec benefits from a clean context window. Clear your context before starting implementation." The artifact folder is designed to be the persistent context — not chat history.

### 7. Schema System: Customizable Workflow Definitions

Schemas define artifact types and their dependency graphs. The default `spec-driven` schema is built-in; teams can fork it or create their own:

```yaml
# openspec/schemas/rapid/schema.yaml
name: rapid
version: 1
artifacts:
  - id: proposal
    generates: proposal.md
    requires: []
  - id: tasks
    generates: tasks.md
    requires: [proposal]
apply:
  requires: [tasks]
  tracks: tasks.md
```

Schema precedence (highest to lowest): CLI flag `--schema` → change metadata `.openspec.yaml` → project `config.yaml` → default `spec-driven`. Teams version-control their schemas in `openspec/schemas/` alongside their code. This means workflow customization is a git artifact, not a configuration that lives outside the repository.

### 8. Project Configuration: Context Injection Architecture

`openspec/config.yaml` is injected into every AI planning request as structured XML:

```xml
<context>
Tech stack: TypeScript, React, Node.js
API: RESTful, documented in docs/api.md
</context>
<rules>
- Include rollback plan for risky changes
- Use Given/When/Then format for scenarios
</rules>
<template>
[Schema's built-in template for this artifact]
</template>
```

Context appears in ALL artifact instructions. Per-artifact rules ONLY appear for the matching artifact (e.g., spec rules don't appear when writing `design.md`). Context is capped at 50KB. This is the opposite of the old `project.md` passive markdown file — it's active injection that runs on every request, not a file the agent might or might not read.

### 9. The Archive Process: Living Spec Repository

Archive is not just file movement. It is a semantic merge operation:

1. Validate the change (unless `--no-validate`)
2. Parse delta specs at the requirement level
3. Apply ADDED/MODIFIED/REMOVED operations to `openspec/specs/`
4. Move `openspec/changes/add-feature/` to `openspec/changes/archive/2025-01-24-add-feature/`
5. Specs now reflect the new behavior

The archive preserves ALL artifacts — proposal, design, tasks, and the original delta specs — creating an audit trail of not just what changed but WHY (proposal), HOW (design), and WHAT WORK was done (tasks). Specs grow organically: each archive contributes a layer, and over time `openspec/specs/` becomes a comprehensive behavioral specification of the entire system.

### 10. Tool Ecosystem: 25+ AI Assistants via Skills Standard

OpenSpec supports 25+ AI tools including Claude Code, Cursor, Windsurf, Gemini CLI, GitHub Copilot, Amazon Q, Cline, RooCode, Codex, and more. The v1.0 OPSX release migrated from tool-specific command files to a unified skills standard:

```
.claude/skills/
├── openspec-propose/SKILL.md
├── openspec-explore/SKILL.md
├── openspec-apply-change/SKILL.md
└── openspec-archive-change/SKILL.md
```

Skills are auto-detected by Claude Code, Cursor, and Windsurf. Each `SKILL.md` contains YAML frontmatter + markdown instructions that the AI reads when the corresponding command is invoked. The CLI (`openspec init`, `openspec update`) generates these files; teams don't write them manually. Configuration differences between tools are handled entirely by the adapter layer in the package.

### 11. The OPSX Information Flow: Dynamic vs Static Instructions

The architecture deep dive reveals the core innovation. Legacy workflow: AI received static instructions, created everything at once, had no awareness of what existed. OPSX workflow:

```
User: /opsx:continue
  → AI queries: openspec status --change "add-auth" --json
  → Receives: {proposal: done, specs: ready, design: ready, tasks: blocked}
  → AI queries: openspec instructions specs --change "add-auth" --json
  → Receives: {template: "...", dependencies: [{id: "proposal", path: "...", done: true}], unlocks: ["tasks"]}
  → AI reads proposal.md → creates specs/auth/spec.md → reports what's unlocked
```

This dynamic pattern is significant: the AI is not working from memory or static instructions but from real-time filesystem state. The CLI is the source of truth for what exists, what's ready, and what the template should look like. This is a concrete instance of structured context as proto-programming for agents.

### 12. Progressive Rigor: Lite vs Full Specs

OpenSpec explicitly addresses the bureaucracy risk. Most changes use "Lite specs" — short behavior-first requirements, clear scope, a few concrete acceptance checks. "Full specs" (RFC 2119 + complete Given/When/Then + cross-team coordination) are reserved for high-risk cases: API/contract changes, migrations, security/privacy concerns, cross-repo changes. The guiding principle is to use the lightest level that still makes the change verifiable.

## Deep Analysis

### The Two-Folder Model Solves the Brownfield Problem

The architectural decision to separate `openspec/specs/` (source of truth) from `openspec/changes/` (proposed modifications) is the cornerstone of the framework. Most spec systems treat the spec as monolithic — you either have a spec or you modify the spec. OpenSpec treats the spec as a living document that is stable while changes are proposed, then updated atomically when changes are archived.

This maps cleanly to how version control works for code (stable main branch + feature branches) but applied to behavioral specifications. The delta format is equivalent to a structured diff at the requirement level. Two changes can coexist without conflict unless they modify the same specific requirement in the same spec file — and even then, `bulk-archive` detects conflicts and resolves them by inspecting what's actually implemented.

### Comparison: Our Stage-Gate System vs. OpenSpec's Fluid Actions

Our wiki's methodology uses explicit stage gates with readiness percentages (DOCUMENT 0→25%, DESIGN 25→50%, SCAFFOLD 50→80%, IMPLEMENT 80→95%, TEST 95→100%). OpenSpec explicitly rejects phase gates: "no phase gates, work on what makes sense." These are not contradictory positions — they represent different contexts and trade-offs.

| Dimension | Our Stage-Gate Methodology | OpenSpec Fluid Actions |
|-----------|---------------------------|------------------------|
| **Primary constraint** | Stage readiness (0→100%) | Artifact dependency graph |
| **Enforcement** | Hard rules, no skipping | Dependencies are enablers, not blockers |
| **Iteration** | Within a stage | Edit any artifact anytime |
| **Context** | Wiki system, knowledge evolution | Code project, feature implementation |
| **Backtracking** | Via methodology model selection | Natural — just edit the artifact |
| **Verification** | `pipeline post` validates everything | `/opsx:verify` checks implementation vs specs |
| **Archive** | Stage completion artifacts persist | `openspec archive` merges deltas + preserves history |

OpenSpec's fluidity is appropriate for code projects where implementation reveals design flaws that should update specs. Our stage gates are appropriate for knowledge synthesis where depth at each stage prevents shallow artifacts from being built on. The two systems are not alternatives — they address different problem spaces.

### Spec Format as Structured Context

The OpenSpec spec format (Purpose → Requirements → Scenarios with RFC 2119) is a concrete instance of structured context for AI agents. Requirements state what the system must do without specifying how. Scenarios provide concrete testable examples. This separation — behavioral contract separate from implementation plan — is exactly what enables the AI to reason about completeness (does the implementation cover all scenarios?) and correctness (does the implementation match spec intent?) without coupling the spec to the implementation.

The `design.md` artifact captures the coupling: technology choices, architecture decisions, data flows. By keeping this in a separate artifact that doesn't merge into the living spec, the approach preserves the behavioral contract while providing implementation guidance in context. This is a clean application of the "spec as proto-programming" principle — the spec constrains AI behavior during implementation the same way CLAUDE.md constrains AI behavior during development sessions.

### Command Pattern: Skills as Structured Instructions

The OPSX skills system (YAML-fronted `SKILL.md` files in `.claude/skills/`) is identical in concept to our wiki's own skills system in `skills/`. Both implement the pattern of structured markdown instructions that AI coding tools auto-detect and execute when the corresponding command is invoked. OpenSpec generates these files from schemas and templates; our wiki has them statically defined in `skills/`. The convergence confirms the pattern — slash commands backed by structured markdown files are becoming the standard mechanism for human-AI collaboration in development workflows.

### The Config Injection Pattern

`openspec/config.yaml` with its `context:` and per-artifact `rules:` is structurally identical to our `CLAUDE.md`'s SACROSANCT OPERATOR DIRECTIVES. Both:
- Define persistent context that shapes all AI behavior in the project
- Separate global context (appears everywhere) from domain-specific rules (appear only where relevant)
- Are version-controlled and deliberately constrained in size (50KB cap for OpenSpec config; CLAUDE.md complexity is bounded by practice)

The OPSX migration guide explicitly describes the architectural improvement: passive `project.md` that agents "might or might not read" was replaced by actively injected `config.yaml` context. This is exactly the "Instructions fail 25%, hooks 100%" problem from our OpenArms research — passive instructions are unreliable; active injection (via injection into every request) is deterministic.

## Open Questions

- How does OpenSpec handle long-running changes (weeks of development) where the codebase evolves significantly during the change? Does the proposal/spec need retroactive updates? (Requires: OpenSpec documentation + case studies — not answerable from this wiki's state.)
- ~~What is the empirical evidence for "AI unpredictability without specs"?~~ **PARTIALLY RESOLVED (2026-04-15):** Ecosystem evidence converges on the claim. OpenArms instruction-only compliance was 25% before hooks, 60% with structured instructions, ~100% with infrastructure enforcement ([[infrastructure-enforcement-proves-instructions-fail|quantified proof]]). [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Seven distinct failure classes]] persist even with infrastructure — unpredictability is real and class-structured, not amorphous. Specs reduce unpredictability by replacing free-form prose interpretation with structured artifact reading ([[structured-context-governs-agent-behavior-more-than-content|Structured Context Principle]]). The remaining question — whether OpenSpec specifically measured the delta their framework produces vs unstructured — is OpenSpec-internal and still genuinely open.
- How does the delta spec parsing handle edge cases — what if a requirement is renamed but not using the RENAMED section? Does the system have conflict detection for semantically overlapping requirements in different delta sections? (Requires: OpenSpec implementation inspection.)
- Does the `/opsx:verify` command (completeness/correctness/coherence) produce measurable differences in implementation quality compared to unverified changes? No benchmarks are cited. (Requires: empirical measurement from OpenSpec users.)
- ~~OpenSpec recommends "Opus 4.5 and GPT 5.2 for best results." How degraded is the experience on smaller/cheaper models? Is there a capability floor?~~ **PARTIALLY RESOLVED (2026-04-15):** The capability floor is **lower than the recommendation suggests** when structured verification exists. [[src-autobe-compiler-verified-backend-generation|AutoBE]] shows Qwen 3.5-27B achieving 100% compilation at **25× lower cost than Opus 4.6** — model capability differences affected retry count, not final quality, because the compiler verification loop closed the gap. [[src-hrm-trm-tiny-recursion-models|HRM/TRM]] (7-27M params) beat GPT-5 on ARC-AGI via recursive inference. [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Qwopus]] distilled Opus reasoning into Qwen 27B running on consumer hardware. **For OpenSpec specifically:** the recommendation likely reflects use-without-verification; with `/opsx:verify` in the loop, smaller models should close the gap (but empirical measurement by OpenSpec users is needed to confirm).
- The custom schema system (`openspec schemas/`) enables teams to define their own artifact flows. How much real-world adoption exists beyond the default `spec-driven` schema? (Requires: OpenSpec community data.)

### Answered Open Questions

**Partially resolved by wiki cross-reference** (2026-04-15):

- **AI-unpredictability-without-specs claim** — supported by this wiki's quantified enforcement data (25→60→100%) + 7-class agent failure taxonomy. OpenSpec's own framework-delta measurement remains open.
- **Capability floor for smaller models** — lower than the recommendation suggests when verification is in the loop (AutoBE, HRM/TRM, Qwopus evidence). OpenSpec-specific measurement needed.

**Genuinely deferred** (require OpenSpec-internal documentation / community data):

- Long-running change evolution handling
- Delta spec edge-case parsing
- /opsx:verify measurable impact
- Custom schema real-world adoption

## Relationships

- COMPARES TO: [[model-methodology|Model — Methodology]] (stage-gate vs. fluid action-based approaches; parallel structures for different contexts)
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] (OPSX skills system is the same pattern — SKILL.md files auto-detected by Claude Code)
- RELATES TO: [[model-context-engineering|Model — Context Engineering]] (config.yaml injection, spec format as structured context for AI)
- BUILDS ON: [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]] (OpenSpec specs are the coding project equivalent of structured context)
- RELATES TO: [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]] (schema YAML + markdown templates as infrastructure-as-code for workflows)
- FEEDS INTO: [[spec-driven-development|Spec-Driven Development]] (concept page — updated with OpenSpec's delta spec and fluid action models)
- COMPARES TO: [[src-sdlc-frameworks-research|Synthesis — SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC]] (broader landscape of spec/SDLC approaches)

## Backlinks

[[model-methodology|Model — Methodology]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-context-engineering|Model — Context Engineering]]
[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[spec-driven-development|Spec-Driven Development]]
[[src-sdlc-frameworks-research|Synthesis — SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC]]
[[specs-as-code-source-inverts-hierarchy|Specs-as-Code-Source Inverts the Traditional Hierarchy]]

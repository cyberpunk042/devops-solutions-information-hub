---
title: "Synthesis — GitHub Spec Kit: Specification-Driven Development"
aliases:
  - "Synthesis — GitHub Spec Kit: Specification-Driven Development"
  - "Synthesis: GitHub Spec Kit"
type: source-synthesis
layer: 1
maturity: growing
domain: cross-domain
status: synthesized
confidence: high
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: src-github-spec-kit
    type: documentation
    url: https://github.com/github/spec-kit
    file: raw/articles/githubspec-kit.md
    title: GitHub Spec Kit — Specification-Driven Development Toolkit
    ingested: 2026-04-14
tags:
  - spec-driven-development
  - sdd
  - ai-agents
  - methodology
  - templates
  - slash-commands
  - constitutional-compliance
  - workflow-automation
  - extensions
  - presets
  - claude-code
  - cross-domain
---

# Synthesis — GitHub Spec Kit: Specification-Driven Development

## Summary

GitHub's Spec Kit is an open-source toolkit that implements Specification-Driven Development (SDD) — a methodology that inverts the traditional code-first model by making specifications the primary source of truth and code their generated output. It ships as a Python CLI (`specify`) that bootstraps a project with slash commands (`/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`), structured templates that constrain LLM output, a constitutional enforcement mechanism, and a layered extensions/presets system. As of v0.6.2 (April 2026), it supports 27+ AI coding agents and has an active community of 55+ extensions and 8+ presets.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source    | GitHub Spec Kit — Specification-Driven Development Toolkit |
> | Type      | documentation (repo — README, spec-driven.md, AGENTS.md, templates, changelogs) |
> | Author    | GitHub (influenced by John Lam) |
> | Date      | Active development; v0.6.2 released 2026-04-13 |
> | Key claim | Specifications become executable — they generate working implementations rather than just guiding them |

## Key Insights

> [!abstract] SDD is a power inversion, not an improvement
> For decades, code was the source of truth and specs were scaffolding discarded after "the real work" began. SDD inverts this: **specs drive code, not the other way around**. Maintaining software means evolving specifications. Debugging means fixing specs that generate incorrect code. The entire development workflow reorganizes around the specification as the central artifact.

**1. The five-phase command workflow is the core interface**

Spec Kit defines a reproducible, ordered pipeline:

| Phase | Command | What it does |
|-------|---------|--------------|
| 0 | `/speckit.constitution` | Create project governing principles (immutable DNA) |
| 1 | `/speckit.specify` | Convert a natural-language description → structured spec with user stories, acceptance criteria, and `[NEEDS CLARIFICATION]` markers |
| 2 | `/speckit.clarify` | Resolve ambiguities before planning (up to 5 targeted questions) |
| 3 | `/speckit.plan` | Convert spec + tech stack → implementation plan with data model, API contracts, research.md, quickstart |
| 4 | `/speckit.tasks` | Convert plan → ordered task list with `[P]` parallel markers and file-path specs |
| 5 | `/speckit.implement` | Execute the task list systematically |

Optional: `/speckit.analyze` (cross-artifact consistency check), `/speckit.checklist` (requirements quality validation).

**2. Template-driven quality: structured prompts constrain LLM behavior**

The templates are not cosmetic — they are the primary mechanism for producing high-quality, consistent specifications. Six constraints are baked in:

- **Abstraction enforcement**: `spec-template.md` explicitly forbids HOW (no tech stack, APIs, code structure); forces focus on WHAT and WHY. This prevents the LLM from jumping to implementation before requirements are stable.
- **Forced uncertainty markers**: `[NEEDS CLARIFICATION: specific question]` is mandatory for any ambiguity. Eliminates the common failure mode of LLMs making plausible but incorrect assumptions.
- **Checklists as "unit tests for English"**: Requirements checklists do not test implementation behavior; they test whether requirements are complete, clear, consistent, and measurable. This is a distinct concept worth naming.
- **Constitutional compliance gates (Phase -1)**: Before implementation, the plan template enforces checkpoints: Simplicity Gate (≤3 projects?), Anti-Abstraction Gate (framework used directly?), Integration-First Gate (contracts defined?). Constitution violations are always CRITICAL.
- **Hierarchical detail management**: Main plan docs stay high-level and readable; complexity is extracted to `implementation-details/` subdirectories.
- **Test-first ordering**: File creation order in tasks is: contracts → test files (contract → integration → e2e → unit) → source files. Tests must fail (Red) before implementation begins.

> [!warning] Templates are runtime artifacts, not documentation
> The command files in `.claude/commands/` (or `.gemini/commands/`, etc.) are the actual prompts executed by the AI agent. They include frontmatter with `description`, `scripts` (bash/ps variants to call), and `handoffs` (agent-to-agent delegation). This is not documentation about a workflow — it IS the workflow, materially constraining LLM output at execution time.

**3. The constitution (`memory/constitution.md`) is architectural DNA**

The spec-driven.md source defines Nine Articles that govern all code generation:

- **Article I — Library-First**: Every feature begins as a standalone library; no direct application-code implementation.
- **Article II — CLI Interface Mandate**: All libraries expose functionality via CLI (stdin/stdout/JSON). Forces observability and testability.
- **Article III — Test-First Imperative (NON-NEGOTIABLE)**: Tests must be written, approved, and confirmed to FAIL before any implementation code is written. Completely inverts standard AI code generation.
- **Articles VII + VIII — Simplicity + Anti-Abstraction**: Maximum 3 projects for initial implementation; use framework directly, no wrapping layers.
- **Article IX — Integration-First Testing**: Real databases over mocks; actual service instances over stubs; contract tests mandatory before implementation.

The constitution has an amendment process requiring documented rationale, maintainer approval, and backwards-compatibility assessment. It shows its own evolution with dated amendments.

**4. Extensions and presets form a layered customization system**

| Priority | Component | Location | Effect |
|----------|-----------|----------|--------|
| 1 (highest) | Project-Local Overrides | `.specify/templates/overrides/` | One-off adjustments |
| 2 | Presets | `.specify/presets/templates/` | Customize how core + extensions behave |
| 3 | Extensions | `.specify/extensions/templates/` | Add new capabilities (new commands, templates) |
| 4 (lowest) | Spec Kit Core | `.specify/templates/` | Built-in SDD commands |

Templates are resolved at runtime (top-down, first match wins). Extension/preset commands are applied at install time. If multiple presets provide the same command, highest-priority wins; on removal, next-highest is restored automatically.

- **Extensions** expand WHAT Spec Kit can do: Jira integration, code review, V-Model test traceability, CI guard, MAQA multi-agent orchestration, worktree isolation.
- **Presets** change HOW it works without adding capabilities: enforce regulatory formats, adapt vocabulary (pirate-speak demo shows full terminology replacement), require security review gates.
- As of v0.6.2, the community catalog lists 55+ extensions and 8+ presets across 5 categories: `docs`, `code`, `process`, `integration`, `visibility`.

**5. Integration architecture: per-agent subpackage registry**

Each AI agent is a self-contained Python subpackage under `src/specify_cli/integrations/<key>/` implementing one of four base classes:

- `MarkdownIntegration` — standard `.md` command files (most agents)
- `TomlIntegration` — TOML format (Gemini)
- `YamlIntegration` — YAML recipe format (Goose)
- `SkillsIntegration` — skill directory layout, e.g., `speckit-<name>/SKILL.md` (Claude Code, Codex)

For Claude Code specifically, spec kit installs skills in `.claude/skills/` and exposes commands as `/speckit-constitution`, `/speckit-specify`, etc. (note: hyphen not dot when using skills vs. slash-command format).

**6. Brownfield and greenfield modes are explicitly supported**

Spec Kit is not greenfield-only. The community has walkthroughs demonstrating:
- Adding features to a 307,000-line C# CMS (ASP.NET brownfield)
- Extending a 420,000-line Jakarta EE Java runtime (Piranha, 180 Maven modules)
- Working with Go + React codebases via CLI terminal only

The `SPECIFY_FEATURE` environment variable allows non-git workflows; `--offline` flag (being retired in v0.6.0) allows air-gapped operation using wheel-bundled assets.

**7. The specification-to-implementation timeline compression is claimed to be significant**

The source's worked example (chat feature) contrasts:
- Traditional: ~12 hours of documentation work (PRD + design + structure + specs + test plans)
- SDD with commands: ~15 minutes to produce: structured spec with user stories + implementation plan with rationale + API contracts + data models + test scenarios + feature branch, all versioned

This claim is unvalidated in the source but provides the motivating value proposition.

**8. Before/after hooks in extensions enable workflow orchestration**

Extension commands can declare `before_specify`, `after_specify`, `before_plan`, `after_plan`, `before_tasks`, `after_implement` hook events. The command templates check for `extensions.yml` at runtime and either execute mandatory hooks inline or surface optional hooks for user decision. This creates a composable middleware layer around the core workflow.

> [!tip] Hook execution pattern mirrors our methodology's stage gates
> The extension hook system (`before_plan`, `after_implement`, etc.) is structurally equivalent to our stage gate model. Where our gates block progression until evidence exists, hooks inject pre/post behavior. The key difference: our stage gates are enforced by methodology; spec kit's are enforced by templates at execution time.

**9. The `/speckit.analyze` command is a cross-artifact consistency engine**

This command runs AFTER `/speckit.tasks` and BEFORE `/speckit.implement`. It:
- Builds semantic models from spec.md, plan.md, tasks.md, and constitution.md
- Runs 6 detection passes: duplication, ambiguity, underspecification, constitution alignment, coverage gaps, inconsistency
- Assigns severity (CRITICAL / HIGH / MEDIUM / LOW)
- Outputs a structured analysis report with coverage % and a requirement-to-task mapping table
- Limit: 50 findings; remainder summarized in overflow
- STRICTLY READ-ONLY — never modifies files; offers remediation plan only with explicit user approval

**10. The `/speckit.checklist` command introduces a novel concept: requirements as the unit under test**

Checklists are "unit tests for English." They do NOT test implementation behavior. They test whether requirements are:
- Complete (are all necessary requirements present?)
- Clear (are requirements unambiguous and specific?)
- Consistent (do they align without conflicts?)
- Measurable (can success be objectively verified?)
- Covered (are all scenarios/edge cases addressed?)

The distinction matters: `"Verify landing page displays 3 episode cards"` is wrong (tests implementation). `"Are the exact number and layout of featured episodes specified?"` is correct (tests requirements quality). This is a methodology insight with broad applicability.

**11. Active velocity: 102+ releases in 7 months, 27+ agent integrations**

The CHANGELOG shows v0.0.1 in August 2025 to v0.6.2 in April 2026. Key evolution:
- v0.0.56 (Oct 2025): First Amazon Q support
- v0.0.80 (Nov 2025): taskstoissues, GitHub MCP integration
- v0.1.x (Feb-Mar 2026): Extension system foundation, preset system
- v0.3.x (Mar 2026): Pluggable preset system, extension catalog, priority-based resolution
- v0.4.x (Apr 2026): Full plugin architecture migration (19 agents in stage 3, TOML agents in stage 4, skills/generic in stage 5)
- v0.5.x (Apr 2026): DEVELOPMENT.md, bundled assets offline mode
- v0.6.x (Apr 2026): Lean preset, CI guard, Goose/YAML integration, brownfield bootstrap

## Deep Analysis

### The SDD Philosophy: Intent-Driven Development

The spec-driven.md document articulates the core inversion with precision: historically, code was truth and specs were scaffolding discarded once "the real work of coding began." Three drivers make this inversion viable now:

1. **AI threshold reached**: Natural language specifications can reliably generate working code. This enables mechanical translation to be automated while human creativity stays in specification.
2. **Exponential complexity**: Modern systems integrate dozens of services and frameworks. Spec-driven generation provides systematic alignment that manual processes cannot scale to.
3. **Accelerating change**: Pivots are now expected, not exceptional. When specifications drive code, requirement changes become systematic regenerations rather than manual rewrites.

The "power inversion" framing is stronger than the term "spec-first development" captures: it is not just writing specs before code — it is making specifications the *governing artifact* whose evolution drives code regeneration. The spec does not become stale as code moves forward; code is continuously regenerated from the spec.

### Structural Comparison: Spec Kit vs. Our Methodology

| Dimension | Spec Kit (SDD) | Our Wiki Methodology |
|-----------|---------------|---------------------|
| Primary artifact | Specification (spec.md) | Artifact chain (per stage + domain) |
| Phase structure | constitution → specify → clarify → plan → tasks → implement | document → design → scaffold → implement → test |
| Stage gates | Enforced by template checklists and `/speckit.analyze` | Enforced by CLAUDE.md hard rules and pipeline validation |
| Constitutional compliance | `memory/constitution.md` (Nine Articles) | SACROSANCT OPERATOR DIRECTIVES in CLAUDE.md |
| Customization | Extensions (add capability) + Presets (reshape workflow) | Domain chains override default stages |
| Quality validation | Template-forced markers, analyze command, checklist command | `pipeline post` (6-step chain) |
| Agent integration | CLI with per-agent subpackage + slash commands | Skills (.claude/skills/) + MCP server |
| Knowledge retention | Spec artifacts versioned in branches | Wiki pages + lessons/patterns/decisions |
| Team workflow | Branch-per-feature, PRDs reviewed via PR | Solo operator-supervised, task-based |

Key convergences:
- Both treat structured context as the primary mechanism for constraining AI behavior (our CLAUDE.md = their `memory/constitution.md`; our stage gates = their template gates).
- Both use slash commands / skills as the primary human-AI interface.
- Both separate "what" from "how" (our document stage = their specify command; our design stage = their plan command).

Key divergences:
- Spec Kit optimizes for feature velocity and team collaboration; our methodology optimizes for knowledge synthesis and progressive distillation.
- Spec Kit generates ephemeral feature specs (per-branch, per-feature); our wiki is a permanent, growing second brain.
- Our methodology has an explicit knowledge evolution layer (L0→L6, lessons/patterns/decisions) that Spec Kit lacks.
- Spec Kit's constitution is customizable per-project; our CLAUDE.md is operator-owned and project-specific.

### Template Mechanics: How LLM Output Is Actually Constrained

Examining the actual command files reveals that spec-kit's power comes from a specific pattern: each command is a **markdown prompt file with structured sections** that the agent reads and executes verbatim. Key mechanisms:

1. **Frontmatter schema**: `description`, `scripts` (bash/ps), `handoffs` (agent delegation targets). This makes commands self-describing and machine-parseable.
2. **Script injection**: `{SCRIPT}` placeholder is replaced with the actual script path at runtime. Scripts output JSON with `FEATURE_DIR` and `AVAILABLE_DOCS`, which the agent parses for context.
3. **Argument threading**: `$ARGUMENTS` (markdown agents) or `{{args}}` (TOML agents) pass user text into the command prompt.
4. **Phase -1 gates**: The plan template enforces pre-implementation checks as gated checklists that the LLM must evaluate and document exceptions for.
5. **Hook awareness**: Every command checks `extensions.yml` for before/after hooks and either executes or surfaces them — making extensions first-class participants in the workflow.

This is the `model-skills-commands-hooks` pattern applied to SDD: the command file IS the specification of agent behavior, constraining it to a structured, reproducible process rather than a free-form conversation.

### The `/speckit.analyze` Command as a Quality Gateway

The analyze command deserves special attention because it demonstrates a mature pattern: **cross-artifact consistency checking as a formal pre-implementation gate**. It:

- Builds internal semantic models from three artifacts without modifying them
- Detects 6 classes of issues with severity assignments
- Maps every requirement to tasks (coverage analysis)
- Surfaces constitution violations as always CRITICAL
- Limits output to 50 findings (token-efficient, actionable)
- Offers remediation only with explicit user approval

This is not a lint check — it is a semantic consistency engine. The distinction between CRITICAL (constitution violation, missing core artifact, zero coverage blocking baseline functionality) vs HIGH vs MEDIUM vs LOW makes it actionable rather than noise.

### Community Ecosystem Health Indicators

The 55+ extensions and 8+ presets — many shipping within weeks of the core extension system (v0.0.93, Feb 2026) — suggest genuine community adoption. Notable extensions:

- **MAQA (Multi-Agent & Quality Assurance)**: Coordinator → feature → QA agent workflow with parallel worktree implementation and Azure DevOps, Jira, Linear, Trello integrations
- **Fleet Orchestrator**: Full feature lifecycle with human-in-the-loop gates across all SpecKit phases
- **Verify Tasks Extension**: Detects phantom completions — tasks marked `[X]` in tasks.md with no real implementation (a critical failure mode for LLM agents)
- **CI Guard**: Spec compliance gates for CI/CD — blocks merges on spec gaps
- **Spec Sync**: Detects and resolves drift between specs and implementation with AI-assisted resolution

The `Verify Tasks Extension` in particular addresses a known failure mode in LLM-driven development: the agent marks tasks complete without actually implementing them. This is a defense mechanism that our own methodology addresses via the rule "never claim done without evidence."

## Open Questions

- How does Spec Kit handle long-running features where the specification evolves mid-implementation? The `spec-kit-refine` and `spec-kit-iterate` extensions address this, but the core workflow assumes stable specs before tasking begins.
- What is the empirical reduction in rework when `/speckit.analyze` catches issues before implement? The 15-minute vs 12-hour claim is motivational but unsourced.
- How does the constitution conflict with team disagreement? The Nine Articles are presented as immutable, but real teams have exceptions. The amendment process requires "maintainer approval" — fine for one project, potentially friction for distributed teams.
- Does spec kit have a knowledge accumulation mechanism? Feature specs are per-branch artifacts. There is no equivalent of our lessons/patterns/decisions evolution layer — insights from completed features do not feed back into improving future specifications.
- How does `/speckit.clarify`'s structured 5-question limit interact with genuinely complex requirements? The cap prevents interrogation fatigue but may not be sufficient for enterprise-scale features.
- The `[NEEDS CLARIFICATION]` marker pattern in spec templates: has anyone built a tool to extract and track these across all features? The `spec-kit-reconcile` extension touches on this but focuses on drift, not initial gaps.

## Relationships

- RELATES TO: [[model-methodology|Model — Methodology]] (stage-gate methodology; SDD is an alternative with equivalent stage separation but specification-centric framing)
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] (spec-kit slash commands are the pattern this model describes; /speckit.* commands are skills installed per-agent)
- RELATES TO: [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]] (spec-kit templates are the clearest applied example of structured context constraining LLM output)
- RELATES TO: [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]] (spec-kit command files are markdown-as-IaC: they define executable workflows, not documentation)
- COMPARES TO: [[model-methodology|Model — Methodology]] (both use stage gates; SDD gates are template-enforced at execution time, our gates are methodology-rule-enforced at planning time)

## Backlinks

[[model-methodology|Model — Methodology]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[specs-as-code-source-inverts-hierarchy|Specs-as-Code-Source Inverts the Traditional Hierarchy]]
[[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]

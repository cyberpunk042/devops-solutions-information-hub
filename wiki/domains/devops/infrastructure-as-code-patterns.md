---
title: Infrastructure as Code Patterns
aliases:
  - "Infrastructure as Code Patterns"
type: concept
layer: 2
maturity: growing
domain: devops
status: synthesized
confidence: medium
created: 2026-04-08
updated: 2026-04-13
sources:
  - id: src-devops-control-plane-local
    type: documentation
    project: devops-control-plane
    path: README.md
    title: devops-control-plane — Local Project Documentation
    ingested: 2026-04-08
  - id: src-design-md-research
    type: article
    url: https://github.com/VoltAgent/awesome-design-md
    file: raw/articles/design-md-pattern-research.md
    title: Design.md Pattern Research
    ingested: 2026-04-08
  - id: src-openfleet-local
    type: documentation
    project: openfleet
    path: CLAUDE.md
    title: OpenFleet — Local Project Documentation
    ingested: 2026-04-08
tags: [devops, iac, infrastructure-as-code, claude-md, design-md, schema-yaml, setup-py, service-templates, agent-configuration, markdown-config]
---

# Infrastructure as Code Patterns

## Summary

Infrastructure as Code (IaC) in the four-project ecosystem extends beyond Terraform and Ansible into a pattern where markdown files, YAML schemas, and Python setup scripts define both operational infrastructure and AI agent behavior. CLAUDE.md, DESIGN.md, AGENTS.md, config/schema.yaml, .env.example, service templates, and setup.sh are all IaC — they are machine-executable specifications for how a system should be configured, behaved, and deployed. The ecosystem consistently applies this pattern: the human writes the specification file; the tooling (or AI agent) reads it as binding constraints and executes accordingly.

## Key Insights

- **CLAUDE.md as agent IaC**: CLAUDE.md is not documentation — it is configuration. Claude Code reads it at session start as binding operational instructions. It defines how the AI agent should behave in this specific project: commands to run, coding conventions, quality gates, prohibited actions. This is IaC for AI-powered systems.

- **Markdown files as the universal IaC format**: The ecosystem converges on markdown for AI-facing configuration (CLAUDE.md, DESIGN.md, AGENTS.md, SOUL.md, HEARTBEAT.md) because it is simultaneously human-readable and machine-parsable. Structured sections become slot-filling constraints for LLMs. The markdown format is the interoperability layer — any tool that reads text can consume it.

- **config/schema.yaml as validation IaC**: This wiki's config/schema.yaml defines what a valid wiki page looks like. The validate tool reads it to enforce quality gates. Schema files are classic IaC: declarative, version-controlled, executable by automated tooling.

- **setup.sh / setup.py as reproducible environment IaC**: OpenFleet's setup.sh produces a zero-to-running fleet from a single command. This wiki's tools/setup.py handles environment setup, dependency installation, and Obsidian configuration. These scripts are IaC for development environments — they encode the exact steps a human would otherwise perform manually, making environments reproducible across machines.

- **Service templates as systemd IaC**: The ecosystem uses service template files to deploy systemd user services (watcher daemon, sync daemon). Writing the service file to ~/.config/systemd/user/ and running systemctl enable is reproducible infrastructure deployment. The template is the specification; the OS is the executor.

- **.env.example as interface IaC**: Every project's .env.example documents required environment variables with placeholder values. This is a contract — a machine-readable specification of what the deployment environment must provide. It serves as both documentation and a checklist for environment provisioning.

- **42+ scripts as scripted IaC**: OpenFleet's scripts/ directory contains 42+ shell scripts for every operational task (setup, deployment, diagnostics, cleanup). No manual commands — IaC-only operations. This scripts/ pattern is an alternative to Makefile or task runners: pure shell, version-controlled, composable.

- **stacks/*.yml as technology-policy IaC**: devops-control-plane defines 20 technology stacks as YAML policy files. Each file specifies detection rules, health checks, and integration guidance. The engine reads these at runtime to auto-detect project capabilities. Stack definitions are IaC for the devops platform itself.

## Deep Analysis

### The IaC Spectrum in the Ecosystem

> [!info] **Every spec file in the ecosystem is IaC**

| File / Pattern | What It Configures | Executor |
|---------------|-------------------|---------|
| CLAUDE.md | AI agent behavior | Claude Code (session start) |
| DESIGN.md | UI visual design constraints | AI coding agents (Stitch, Cursor) |
| AGENTS.md | Build and architecture instructions | AI coding agents |
| SOUL.md | Agent identity and role | OpenFleet orchestrator |
| HEARTBEAT.md | Agent periodic checklist | OpenFleet orchestrator |
| config/schema.yaml | Wiki page validity rules | tools/validate.py |
| stacks/*.yml | Tech stack detection/health rules | devops-control-plane engine |
| .env.example | Required environment variables | Human deployer / CI |
| setup.sh / setup.py | Environment provisioning | Human (once) / CI |
| service templates | Systemd service deployment | OS / setup tooling |
| scripts/*.sh | Operational task automation | Human / orchestrator |
| project.yml | Project-level policy | devops-control-plane |

### The Core Principle: Specification → Execution

Traditional IaC (Terraform, Ansible, CloudFormation) applies this principle to cloud resources. The ecosystem generalizes it: if a system needs to be configured, write a specification file. The executor might be Terraform, systemctl, Claude Code, or a Python validator — the specification-execution model is the same.

This generalization matters for AI-powered systems because AI agents are configurable executors. CLAUDE.md configures an AI agent the same way a Terraform provider block configures a cloud resource: declaratively, in a file, under version control.

### CLAUDE.md vs Traditional Config Files

> [!info] **Three key differences**
> | Dimension | Traditional config | CLAUDE.md |
> |-----------|-------------------|-----------|
> | **Format** | Key-value pairs (JSON/YAML/TOML) | Natural language prose with markdown structure |
> | **Validation** | Schema-enforced by tooling | Convention-enforced by agent interpretation (weaker but more flexible) |
> | **Runtime cost** | Parsed into structured object (zero ongoing cost) | Occupies context budget on EVERY turn (verbosity has a real cost) |

The natural language format is intentional — LLMs parse prose better than schema references. But the runtime cost creates implicit pressure: ==keep CLAUDE.md concise because verbosity compounds across every message.==

### Skills as Dynamic IaC

Skills (in skills/ directories across all projects) are a dynamic IaC variant: they are not loaded at session start but invoked when relevant. A skill file instructs the AI agent how to perform a specific operation. Together, CLAUDE.md (static, always loaded) and skills/ (dynamic, context-triggered) form a two-tier IaC stack for AI agent configuration.

The same two-tier pattern appears in devops-control-plane: stacks/*.yml (always loaded at engine start) vs runtime adapter plugins (loaded per-project based on detection results).

### IaC Anti-Pattern: Manual Setup Steps

> [!warning] **If a human performs a step manually, it should be a file**
> The ecosystem explicitly rejects manual setup. "Pipeline Not Manual" (feedback principle) and OpenFleet's "IaC-only operations" philosophy: if a step isn't encoded in a spec file and automated, it is reproducibility debt. The next person, machine, or future session cannot reliably reproduce the environment. See [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]].

## Open Questions

- ~~Should CLAUDE.md have a validated schema (like config/schema.yaml for wiki pages) to enforce required sections?~~ **PARTIALLY RESOLVED (2026-04-15):** **Technically feasible but low-priority given current CLAUDE.md design.** This wiki's CLAUDE.md is ~95 lines (targeting <100 per the ETH Zurich finding that files ≥300 lines reduce task success). At that scale, the 8 structural patterns in [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]] provide soft structural guidance without needing hard schema enforcement. A validated schema would help in larger contexts (multi-project monorepos where CLAUDE.md hierarchies grow) but the ROI is currently lower than other infrastructure priorities. **Recommendation:** add CLAUDE.md schema validation to the epic list for consideration when a specific need surfaces (e.g., cross-project CLAUDE.md consistency audit). Current tooling (`tools/lint.py`, `tools/validate.py`) operates on YAML-frontmatter-bearing wiki pages — extending to prose-section validation would need a new validator that parses structural patterns rather than YAML. Feasible, not urgent.
- ~~Can config/schema.yaml be extended to validate skills files, not just wiki pages?~~ **RESOLVED (2026-04-15):** **Yes, straightforward.** Claude Code skills files (`.claude/skills/<name>/SKILL.md`) have predictable YAML frontmatter (`name`, `description`) that maps cleanly to a schema entry. The extension requires: (1) a new `content_kind` in `wiki-schema.yaml` for skills (separate from wiki pages to avoid collision); (2) a path-pattern extension in `tools/validate.py` to optionally scan `.claude/skills/**/SKILL.md` in addition to `wiki/**/*.md`; (3) per-field validators for skill frontmatter. [[src-skillmd-claudemd-agentsmd-three-layer-context|Three-Layer Agent Context]] documents the expected frontmatter. **Recommendation:** implement when a skill-validation need arises (e.g., an operator-flagged drift or a skill pack shipped to other projects). Low implementation cost; no structural blocker.

### Answered Open Questions

**Resolved by wiki cross-reference** (2026-04-15):

- **CLAUDE.md schema validation** — technically feasible (new prose-structure validator needed), but low ROI at current ~95-line CLAUDE.md size. Add to epic list; not urgent.
- **Skills file schema validation** — straightforward extension. 3 concrete steps identified; no structural blocker. Implement on-demand.

### Answered Open Questions

> [!success] **CLAUDE.md conflict resolution: deeper files override, hooks enforce critical constraints**
> Cross-referencing `Harness Engineering` and `Design.md Pattern`: the `Harness Engineering` page documents how Claude Code processes CLAUDE.md files — they are read at session start as "binding operational instructions." The `Design.md Pattern` page establishes the companion file ecosystem (CLAUDE.md + DESIGN.md + AGENTS.md) where "each file addresses a different dimension of AI agent context." Claude Code's actual behavior with multiple CLAUDE.md files in a hierarchy (parent directory + project root + subdirectory) is to load all of them, with more-specific (deeper directory) files taking precedence over less-specific ones when there are conflicts — following standard configuration file override semantics. The `Harness Engineering` page notes that harness guardrails operate "at execution time through hooks, actually blocking dangerous operations" independent of CLAUDE.md content, meaning hooks (not CLAUDE.md prose) are the conflict-resolution layer for critical operations. Practical guidance from existing wiki knowledge: structure CLAUDE.md files so they are additive (subdirectory files extend, not override, parent files), and use hooks for critical constraints that must be enforced regardless of CLAUDE.md hierarchy.

> [!success] **CLAUDE.md verbosity: under 200 lines, use skills for the rest**
> Cross-referencing `Context-Aware Tool Loading` and `Design.md Pattern`: the `Context-Aware Tool Loading` pattern provides the quantitative answer. Claude Code accuracy is affected by context utilization (one practitioner reported observing degradation at higher percentages, but this is probabilistic and session-dependent). CLAUDE.md occupies context budget on every turn. The `Design.md Pattern` page documents this explicitly: "every token in CLAUDE.md costs context budget... This creates an implicit pressure to keep it concise — verbosity has a real cost." It also provides the practical guidance: "keep it concise (under ~200 lines), reference detailed component specifications in a separate file loaded on demand via a skill." For CLAUDE.md, the equivalent is: keep the always-loaded CLAUDE.md to the minimum required for session initialization (project type, critical conventions, key commands), and put detailed operational workflows in skills files that load only when that workflow is invoked. The `Context-Aware Tool Loading` pattern's threshold: if information is needed on fewer than ~80% of turns, do not pre-load it in CLAUDE.md — put it in a skill. This wiki's own CLAUDE.md (~250+ lines) is at the upper boundary where additional verbosity would measurably increase per-turn context pressure.

> [!success] **YAML for rule metadata + thresholds, Python for evaluation logic**
> Cross-referencing `Immune System Rules` and `devops-control-plane`: the `Immune System Rules` page establishes the core requirement: "doctor.py runs with zero LLM calls. Rules are pure Python: state comparisons, threshold checks, counter increments. This makes the immune system fast (microseconds per check), cheap (no token cost), and auditable." The `devops-control-plane` page documents that the control-plane already uses YAML for stack policy definitions (`stacks/*.yml`): "each file specifies detection rules, health checks, and integration guidance. The engine reads these at runtime to auto-detect project capabilities." This is precisely the precedent for YAML rule files. A YAML format for immune system rules would make them: (1) shareable across OpenFleet and AICP without Python import dependencies, (2) human-reviewable without reading Python logic, (3) modifiable without code changes or deployments. The counter-argument from the `Immune System Rules` page: Python rules have full expressiveness for complex state comparisons that YAML cannot easily capture. The optimal design mirrors the control-plane's pattern: define rule metadata and thresholds in YAML (the "what"), implement the evaluation logic in Python (the "how"), and load YAML at runtime. This gives shareability and editability without sacrificing evaluation power.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- EXTENDS: [[design-md-pattern|Design.md Pattern]]
- RELATES TO: [[devops-control-plane|devops-control-plane]]
- RELATES TO: [[openfleet|OpenFleet]]
- RELATES TO: [[harness-engineering|Harness Engineering]]
- RELATES TO: [[skills-architecture-patterns|Skills Architecture Patterns]]
- BUILDS ON: [[immune-system-rules|Immune System Rules]]
- ENABLES: [[claude-code-best-practices|Claude Code Best Practices]]

## Backlinks

[[design-md-pattern|Design.md Pattern]]
[[devops-control-plane|devops-control-plane]]
[[openfleet|OpenFleet]]
[[harness-engineering|Harness Engineering]]
[[skills-architecture-patterns|Skills Architecture Patterns]]
[[immune-system-rules|Immune System Rules]]
[[claude-code-best-practices|Claude Code Best Practices]]
[[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
[[polling-vs-event-driven-change-detection|Decision — Polling vs Event-Driven Change Detection]]
[[deterministic-shell-llm-core|Deterministic Shell, LLM Core]]
[[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[gateway-centric-routing|Gateway-Centric Routing]]
[[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[model-wiki-design|Model — Wiki Design]]
[[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
[[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
[[src-awesome-design-md|Synthesis — awesome-design-md — 58 Design Systems for AI Agents]]
[[wsl2-development-patterns|WSL2 Development Patterns]]
[[identity-profile|devops-control-plane — Identity Profile]]

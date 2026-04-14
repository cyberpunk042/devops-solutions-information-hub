---
title: AI Agent Artifacts — Standards and Guide
aliases:
  - "AI Agent Artifacts — Standards and Guide"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: taxonomy
    type: wiki
    file: wiki/domains/cross-domain/methodology-artifact-taxonomy.md
  - id: nxcode-agentic
    type: article
    url: https://www.nxcode.io/resources/news/agentic-engineering-complete-guide-vibe-coding-ai-agents-2026
  - id: openarms-chain
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms artifact chain (24 artifacts at Default SDLC level)"
  - id: openarms-directive
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms agent directive configuration"
  - id: operator-rules
    type: file
    file: raw/notes/2026-04-12-restart-directive.md
tags: [methodology, ai-agents, artifacts, persona, skills, hooks, enforcement, compliance, standards]
---

# AI Agent Artifacts — Standards and Guide

> [!tip] AI Quick Start — Artifacts That Govern HOW AGENTS WORK
>
> 1. **These are about YOU** — persona templates, skill definitions, hooks, stage skills define how agents behave
> 2. **CLAUDE.md is IaC for agent behavior** — human writes config, machine reads it as binding constraints
> 3. **Stage skills narrow your visible scope** — you only see your current stage's rules (prevents rushing ahead)
> 4. **Hooks enforce at tool level** — pre-bash blocks git commands, pre-write blocks wrong-scope writes
> 5. **The operator's .agent/ rule system** is a third enforcement tier — per-prompt rule injection with self-tests. Study it as research material.

## Summary

Guide to artifacts specific to AI agent workflows — document types that don't exist in traditional SDLC because they govern HOW AGENTS WORK, not what they build. These include agent persona templates, skill definitions, stage skills for context injection, hook configurations for enforcement, prompt queues for batch execution, and compliance reports for monitoring. This category is the NEWEST in the taxonomy — emerging from 2025-2026 agentic engineering practice. The operator's own `.agent/` rule system (documented in the operator directive log) is a real-world instance of production-grade AI agent methodology artifacts.

## Key Insights

1. **AI agent artifacts govern the EXECUTOR, not the PRODUCT.** Traditional SDLC artifacts describe what to build and how. AI agent artifacts describe how the BUILDER should behave. CLAUDE.md is configuration, not documentation. Agent directives are constraint sets, not style guides. Hook configs are enforcement rules, not suggestions.

2. **The operator's .agent/ rule system is the most evolved instance we've seen.** 16+ rules covering: anti-rogue constraints, no-abstraction enforcement, correction escalation, echo-first protocol, grep-first debugging, one-scope focus, read-before-write tracing, refactoring integrity (copy machine protocol), post-checkpoint quarantine. Each rule traces to a specific AI failure post-mortem.

3. **Multi-agent orchestration creates NEW artifact types.** From the agentic engineering research (2026): Feature Author → Test Generator → Code Reviewer → Architecture Guardian → Security Scanner → Documentation Writer → Release Manager. Each agent in the pipeline needs: a persona (who am I), skills (what can I do), constraints (what can't I do), and handoff artifacts (what I pass to the next agent).

4. **Agent enforcement exists at 4 levels.** From our CLAUDE.md structural patterns research: (1) Instruction-level (prose rules — 25% compliance), (2) Structured instruction-level (tables, ALLOWED/FORBIDDEN — 50-60%), (3) Advisory hooks (warn but don't block — 70%), (4) Blocking hooks (prevent the action — 90%+). Each level produces different artifacts.

### SDLC Profile Level — What Applies Where

> [!abstract] Not all chains require all artifacts
>
> | Chain Level | What's Required | What's Optional | What's Skipped |
> |-------------|----------------|-----------------|----------------|
> | **Simplified** (POC, 2-3 stages) | CLAUDE.md + persona only | — | Stage skills, hooks, rule files, compliance validation, prompt queues |
> | **Default** (MVP-Prod, 5 stages) | CLAUDE.md + persona + stage skills + selected hooks | Prompt queues, compliance reports | Full rule system, multi-agent handoff artifacts |
> | **Full** (Production fleet, all stages) | All hooks + rule files + compliance validation + prompt queues | Multi-agent orchestration artifacts | — |
>
> See [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]] for profile details.

## Deep Analysis

### Agent Persona Template

> [!info] WHO the agent IS — identity, capabilities, constraints, working style
>
> | Aspect | Content |
> |--------|---------|
> | **Identity** | Name, role, expertise domain, relationship to operator |
> | **Capabilities** | Tools available, skills loaded, what this agent CAN do |
> | **Constraints** | What this agent CANNOT do, boundaries, forbidden actions |
> | **Working style** | Verbosity level, proactive vs reactive, when to ask vs act |
> | **Sacrosanct directives** | Operator intent that overrides everything else |
>
> **OpenArms instance:** `docs/reference/templates/personas/software-engineer/IDENTITY.md` + `SOUL.md` — defines the software engineer agent's identity and philosophical approach.
>
> **The operator's instance:** The "ANTI-ROGUE CONSTRAINT" rule — explicitly defines: "USER = Expert, Commander, Architect, Owner. YOU = Novice, Soldier, Laborer, Tool." This IS a persona template, encoded as enforcement rules.

### Skill Definition

> [!info] WHAT the agent can do — invocable capabilities with triggers and parameters
>
> | Aspect | Content |
> |--------|---------|
> | **Name** | Skill identifier (kebab-case) |
> | **Description** | What this skill does, when to invoke |
> | **Trigger** | Natural language patterns or slash commands that activate it |
> | **Parameters** | What input the skill needs |
> | **Output** | What the skill produces |
> | **Stage restrictions** | Which methodology stages this skill is allowed/blocked in |
>
> **Our wiki instance:** skills/ directory — wiki-agent, evolve, model-builder, continue, notebooklm. Each has a skill.md with operations, quality gates, and styling standards.
>
> **Quality bar:** A skill definition must be complete enough that a DIFFERENT agent could invoke it correctly from the definition alone. If the definition requires "see the code" to understand, it's incomplete.

### Stage Skill (Context Injection)

> [!info] Per-stage instructions INJECTED into agent context at stage transitions
>
> | Aspect | Content |
> |--------|---------|
> | **Stage name** | Which stage this skill activates for |
> | **Runtime state** | Current task ID, current model, current stage — read from state files |
> | **Artifact requirements** | What this stage MUST produce — read from methodology.yaml |
> | **MUST/MUST NOT rules** | 3-5 specific constraints for this stage |
> | **Recommended skills** | Other skills to use during this stage |
> | **Completion signal** | "When Done: Call /stage-complete" |
>
> **OpenArms instance:** 5 stage skills in `.claude/skills/methodology-{document,design,scaffold,implement,test}/SKILL.md` — each 29-43 lines, injected at runtime.
>
> **Key insight from research:** Stage skills achieve the HIGHEST per-stage compliance because they NARROW the agent's visible scope to just the current stage. The agent doesn't see other stages' rules — preventing rushing ahead.

### Hook Configuration

> [!info] Enforcement rules that PREVENT violations at the tool level
>
> | Hook Type | What It Does | Implementation |
> |-----------|-------------|---------------|
> | **Scope Guard** (PreToolUse:Bash) | Blocks commands the agent shouldn't run | Shell script checking command against blocklist |
> | **Write Guard** (PreToolUse:Write/Edit) | Blocks writes to wrong-scope paths per stage | Shell script checking file path against current stage |
> | **Artifact Tracker** (PostToolUse:Write/Edit) | Logs files created/modified for verification | Shell script appending to stage-files.log |
> | **Context Rebuilder** (PostToolUse:Compact) | Rebuilds instructions after context compaction | Script that re-injects methodology context |
>
> **OpenArms instance:** 4 hooks in `scripts/methodology/hooks/` — pre-bash.sh, pre-write.sh, post-write.sh, post-compact.sh.
>
> **The operator's instance:** The `.agent/rules/` system with 16+ rule files, each triggered "always_on" — these are essentially documentation-level hooks that rely on instruction compliance rather than tool-level blocking.

### Agent Rule System (The Operator's Innovation)

> [!warning] This is research material captured from the operator's own agent management system
>
> The operator's complete `.agent/` rule system (captured in raw/notes/2026-04-12-restart-directive.md) represents a THIRD enforcement approach beyond instruction-level and hook-level: **rule-file injection** with mandatory processing.
>
> | Rule | What It Prevents | Post-Mortem Origin |
> |------|-----------------|-------------------|
> | **ANTI-ROGUE CONSTRAINT** | AI substituting judgment for user's request | "13 AI instances obliterated — same root cause" |
> | **PROCESS OR DIE** | Reading rules without processing them for THIS prompt | "16 AIs read every rule, acknowledged every rule, violated every rule" |
> | **CORRECTION-ESCALATION** | Applying corrections through a corrupt model | "AI #17 received 10+ corrections, produced same wrong output 10 times" |
> | **ECHO-FIRST** | Acting on misunderstood request | "AI #17 spent 10 turns solving the wrong problem" |
> | **GREP-FIRST** | Speculating before searching | "10+ rounds speculating instead of one grep" |
> | **NO-ABSTRACTION** | Elevating concrete instructions to abstract goals | "13 AI instances obliterated — abstracted user's words" |
> | **ONE-SCOPE** | Stacking unrelated fixes | "8/14 post-mortems involved cascading fix-on-fix" |
> | **READ-BEFORE-WRITE** | Writing code without tracing state | "14 AI instances wrote code based on guesses" |
> | **REFACTORING INTEGRITY** | Generating code from memory during refactoring | "Post-Mortem #13: 40+ regressions from inference-based rewrites" |
> | **POST-CHECKPOINT QUARANTINE** | Contaminating new request with old context | "AI #17 warped posture request through mediator lens for 10+ turns" |
>
> **Each rule has:** A trigger condition, a self-test (questions the agent must answer), a "why this exists" section tracing to a specific failure, and an enforcement mechanism (usually: STOP and escalate).
>
> **Key structural patterns from the rule system:**
> - Rules are SEPARATE FILES (one concern per file)
> - Each rule has a SELF-TEST (questions, not just instructions)
> - Each rule traces to a SPECIFIC FAILURE (not theoretical)
> - Rules use NUMBERED STEPS (not bullets — creates cognitive chain)
> - The CORRECTION-ESCALATION ladder (1 = normal, 2 = warning, 3 = corrupted, 4+ = suggest new session)

### Prompt Queue

> [!info] Queued prompts for batch execution — used in evolution and automation
>
> | Aspect | Content |
> |--------|---------|
> | **Queue file** | .evolve-queue/*.prompt.md — one file per candidate |
> | **Prompt content** | Source pages to read, target page to produce, quality requirements |
> | **Execution** | Consumed by local model (AICP) or Claude session |
> | **Verification** | Generated page runs through pipeline post |
>
> **Our wiki instance:** `pipeline evolve --auto --backend openai` reads the prompt queue and feeds prompts to LocalAI via AICP routing. Each prompt produces one evolved wiki page.

### Agent Compliance Report

> [!info] Post-session methodology adherence analysis — the monitoring artifact for agents
>
> | Section | Content |
> |---------|---------|
> | **Session ID** | Which run, which agent, which mode |
> | **Tasks completed** | List with stage sequences |
> | **Stage boundary compliance** | Per stage: any FORBIDDEN artifacts in diff? |
> | **Artifact chain completeness** | All required artifacts exist? |
> | **Readiness accuracy** | Computed vs claimed |
> | **Violations** | Specific violations with evidence (file:line) |
> | **Concerns raised** | Agent-flagged issues |
> | **Recommendations** | What methodology rules need updating based on evidence |
>
> **Currently missing from all projects.** OpenArms has `agent-report.py` for basic analysis. No project has automated compliance reporting against the full artifact chain. This is the highest-priority monitoring gap.

### How AI Agent Artifacts Map to the Stage-Gate System

> [!abstract] When each AI agent artifact is produced
>
> | Methodology Stage | AI Agent Artifacts Produced |
> |------------------|---------------------------|
> | **Pre-methodology** (project setup) | Persona Template, CLAUDE.md, Hook Configurations, Rule Files |
> | **Planning** (epic breakdown) | Skill Definitions, Stage Skills, Prompt Queue templates |
> | **Document stage** | — (agents consume artifacts, don't produce AI-specific ones) |
> | **Design stage** | Stage skill refinements, hook rule adjustments |
> | **Scaffold stage** | — |
> | **Implement stage** | — |
> | **Test stage** | — |
> | **Closure** (post-session) | Completion Log, Compliance Report, Concern Log |
> | **Monitoring** (ongoing) | Compliance trend reports, violation pattern analysis |

## Open Questions

> [!question] ~~Should the operator's .agent/ rule system be studied as a methodology model for the wiki?~~
> **RESOLVED:** Document as a PATTERN (structured rule enforcement), not a methodology model (no stages). Sits between CLAUDE.md and hooks.
> **DEFERRED:** Needs operator brainstorm session about the "magic tricks." The rule system is captured as research material in `raw/notes/2026-04-12-restart-directive.md`. Represents a THIRD enforcement tier: per-prompt rule injection with mandatory processing.

> [!question] ~~Should agent persona templates be wiki page types or external config files?~~
> **RESOLVED:** External config files in the project (IDENTITY.md, SOUL.md). Wiki documents the PATTERN, project has the INSTANCE.
> **DEFERRED:** Needs operator input. Currently external (CLAUDE.md, skills/). The knowledge in them SHOULD be in the wiki for discoverability, but the configs must remain external for agent consumption. Likely answer: wiki pages DOCUMENT the persona, config files ARE the persona.

> [!question] ~~How do multi-agent handoff artifacts work?~~
> **RESOLVED:** DEFERRED to E027. No source defines a handoff format yet. Future work.
> **DEFERRED:** Needs deeper research into multi-agent orchestration patterns. The agentic engineering research (nxcode.io) describes the pipeline (Feature Author → Test Generator → Code Reviewer) but doesn't specify the handoff artifact format.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Claude Code model** | [[model-claude-code|Model — Claude Code]] — how CLAUDE.md structures agent behavior |
> | **Skills and hooks** | [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] — skill/hook architecture |
> | **Enforcement patterns** | [[enforcement-hook-patterns|Enforcement Hook Patterns]] — hook implementation patterns |

## Relationships

- BUILDS ON: [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
- BUILDS ON: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
- BUILDS ON: [[enforcement-hook-patterns|Enforcement Hook Patterns]]
- BUILDS ON: [[stage-aware-skill-injection|Stage-Aware Skill Injection]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- FEEDS INTO: [[methodology-evolution-protocol|Methodology Evolution Protocol]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[stage-aware-skill-injection|Stage-Aware Skill Injection]]
[[model-claude-code|Model — Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-methodology|Model — Methodology]]
[[methodology-evolution-protocol|Methodology Evolution Protocol]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]

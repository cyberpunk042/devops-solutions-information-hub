---
title: Stage-Aware Skill Injection
aliases:
  - "Stage-Aware Skill Injection"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Model: Skills, Commands, and Hooks"
  - "Model: Methodology"
instances:
  - {'page': 'OpenArms skill-stage-mapping.yaml', 'context': '299-line mapping: 3 layers (generic, role, plugin) with per-stage recommendations and restrictions'}
  - {'page': 'Research Wiki skills/', 'context': '5 skills loaded globally with no stage-awareness'}
created: 2026-04-11
updated: 2026-04-13
sources:
  - id: openarms-mapping
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms project reference"
tags: [skills, stage-gate, injection, agent-compliance, methodology]
---

# Stage-Aware Skill Injection

## Summary

Dynamically loading or restricting skills based on the current methodology stage. Prevents wrong-phase skill usage (brainstorming during test, TDD during document) and ensures critical skills are used at the right time (verification before claiming done). Three-layer architecture: generic skills (all agents), role-specific skills (engineer vs PM), and plugin skills (project-specific tools).

> [!info] Pattern Reference Card
>
> | Layer | Scope | Examples |
> |-------|-------|---------|
> | Generic | All agents, all stages | methodology-stage-guide, code-exploration |
> | Role | Engineer or PM specific | adr-creation (engineer), sprint-planning (PM) |
> | Plugin | Project-specific tools | superpowers, context7, safety-net |

## Pattern Description

> [!abstract] The Three Mapping Dimensions
>
> | Dimension | What It Controls | Configured Where |
> |-----------|-----------------|-----------------|
> | **Recommended** | Skills that SHOULD be used at this stage | `stages.{stage}.skills[]` |
> | **Mandatory** | Skills that MUST be used — gate fails without them | `stages.{stage}.mandatory[]` |
> | **Blocked** | Skills that MUST NOT be used at this stage | `restrictions.{stage}.blocked_skills[]` |

### How It Works

1. Agent enters a methodology stage (e.g., `document`)
2. The harness or skill system reads the mapping for the current stage
3. Recommended skills are surfaced in the agent's context
4. Mandatory skills are injected and the agent must invoke them
5. Blocked skills are hidden or produce errors if invoked

### The Mapping Schema

```yaml
# skill-stage-mapping.yaml
generic:
  all_stages:
    - methodology-stage-guide  # always available
  document:
    skills: [code-exploration, gap-analysis, brainstorming]
    mandatory: [brainstorming]  # must brainstorm before designing
  design:
    skills: [writing-plans, architecture-review]
    mandatory: [writing-plans]
  scaffold:
    skills: []  # mechanical stage — no skills needed
  implement:
    skills: [executing-plans, systematic-debugging]
  test:
    skills: [test-driven-development, verification-before-completion]
    mandatory: [verification-before-completion]

restrictions:
  document:
    blocked_skills: [TDD, executing-plans, code-review]
    reason: "Document stage is analysis-only — no execution or testing"
  design:
    blocked_skills: [TDD, executing-plans, code-review]
    reason: "Design stage produces decisions, not code"
  scaffold:
    blocked_skills: [brainstorming, writing-plans, code-review, debugging]
    reason: "Scaffold is mechanical — type copying, not creative"
  implement:
    blocked_skills: [brainstorming, writing-plans, code-review]
    reason: "Implement follows the design — no redesigning mid-build"
  test:
    blocked_skills: [brainstorming, writing-plans, executing-plans]
    reason: "Test verifies — no planning or execution"
```

### Why Blocking Matters

> [!warning] Without Blocking, Agents Use Wrong Skills at Wrong Times
>
> | Anti-Pattern | What Happens | Cost |
> |-------------|-------------|------|
> | Brainstorming during implement | Agent redesigns mid-build, creates scope creep | Rework, abandoned scaffolds |
> | TDD during document | Agent writes test stubs before understanding the problem | Tests test the wrong thing |
> | Code review during implement | Agent reviews its own code before finishing | Perfectionism loop, no progress |
> | Planning during test | Agent plans new features when it should verify existing | Scope creep, unverified code |

### Mandatory Skills as Quality Gates

Mandatory skills create soft quality gates — the agent should not advance without invoking them:

> [!tip] Key Mandatory Skills
>
> | Stage | Mandatory Skill | What It Ensures |
> |-------|----------------|----------------|
> | Document | brainstorming | Agent explores the problem space before deciding |
> | Design | writing-plans | Agent produces a structured plan, not ad-hoc decisions |
> | Test | verification-before-completion | Agent verifies with evidence before claiming done |

## Instances

> [!example]- Instance 1: OpenArms (Full 3-Layer Implementation)
>
> **299-line skill-stage-mapping.yaml** with:
> - Generic layer: 5 stage-specific skill sets
> - Engineer role: architecture-health, design-pattern-selection, domain-boundary-enforcement
> - PM role: pm-orchestration, blocker-resolution, epic-breakdown
> - Plugin layer: superpowers (14 skills), context7 (MCP), pr-review-toolkit
> - Restrictions: 5 stages × 3-11 blocked skills each
>
> The harness reads this config and injects the right skills into the agent's context at each stage transition. Skills not in the recommended list are hidden. Blocked skills produce warnings.

> [!example]- Instance 2: Research Wiki (No Stage-Awareness)
>
> 5 skills (wiki-agent, evolve, model-builder, continue, notebooklm) loaded globally. No stage-based filtering. Agent can invoke any skill at any stage. The wiki-agent skill has internal guidance ("during ingest, do X; during query, do Y") but this is advisory, not enforced.
>
> **Gap:** The wiki would benefit from marking brainstorming as mandatory before design, and verification-before-completion as mandatory before claiming ingestion is done.

## When To Apply

> [!tip] Use Stage-Aware Skill Injection When
>
> - Moving to Tier 3+ methodology adoption
> - Agents consistently use wrong skills at wrong stages (e.g., planning during execution)
> - You have mandatory quality gates (brainstorm before design, verify before done)
> - Running autonomous agents where skill misuse causes silent quality degradation

## When Not To

> [!warning] Don't Use When
>
> - Your project has <5 skills total (the overhead exceeds the benefit)
> - Skills are genuinely stage-agnostic (e.g., web search, file exploration)
> - You're in exploratory mode where stage boundaries are fluid
> - The agent needs creative freedom (research spikes, brainstorming sessions)

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

- DERIVED FROM: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- DERIVED FROM: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
- BUILDS ON: [[enforcement-hook-patterns|Enforcement Hook Patterns]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-methodology|Model — Methodology]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[ai-agent-artifacts|AI Agent Artifacts — Standards and Guide]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]

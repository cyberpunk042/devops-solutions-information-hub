---
title: "Project Self-Identification Protocol — The Goldilocks Framework"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: operator-goldilocks
    type: directive
    file: raw/notes/2026-04-12-goldilocks-higher-ground-directive.md
    description: "Operator: 'AM I a system? Am I a harness? V2? V3? Am I just a solo agent session? What is my domain? What makes this work? Where is all the magic?'"
  - id: openarms-five-contexts
    type: observation
    file: raw/articles/openarms-all-distilled-lessons.md
    description: "OpenArms discovered 5 cognitive contexts reading one CLAUDE.md — rules meant for one context mislead another"
  - id: openfleet-tiers
    type: observation
    file: raw/articles/openfleet-tier-profiles.yaml
    description: "OpenFleet tier progression: trainee→standard→expert controls context depth and autonomy"
tags: [goldilocks, self-identification, protocol, context-detection, adaptive, framework]
---

# Project Self-Identification Protocol — The Goldilocks Framework

## Summary

Every agent session, every harness run, every tool invocation must be able to answer: "What am I? What is my context? What level of process is appropriate HERE?" The Goldilocks Framework defines the self-identification protocol — a structured set of questions that any consumer of the second brain must answer BEFORE selecting methodology, chain, enforcement level, and tool scope. "Just right" is not a fixed point — it is a FUNCTION of identity × context × capability. Getting it wrong in either direction kills: too much process kills POC velocity, too little process kills production quality.

## Key Insights

1. **Self-identification is prerequisite to methodology selection.** Before an agent or system can choose a methodology model, SDLC chain, or enforcement level, it must know WHAT it is. OpenArms discovered this the hard way: 5 cognitive contexts reading one CLAUDE.md, each needing different rules, none marked.

2. **Seven identity dimensions determine "just right."**

> [!abstract] The Seven Questions
>
> | # | Question | Why It Matters | Where the Answer Comes From |
> |---|---------|---------------|---------------------------|
> | 1 | **What am I?** | Solo mode (human + Claude) / harness-managed agent / provisioned fleet agent / sub-agent | Execution context (who spawned me, what wraps me) |
> | 2 | **What execution mode?** | solo (no harness) / harness v1 (basic loop) / harness v2 (enforced) / harness v3 (full SDLC) / full system (fleet+orchestrator) | What wraps the agent — solo has nothing, harness wraps one agent, system orchestrates many |
> | 3 | **What domain?** | TypeScript / Python / Infrastructure / Knowledge / Mixed | Project tech stack, domain-profiles/*.yaml |
> | 4 | **What project phase?** | POC / MVP / Staging / Production | Project metadata, operator declaration |
> | 5 | **What scale?** | 10k / 100k / 1M / 5M / 15M lines | Codebase analysis, project metadata |
> | 6 | **What PM level?** | L1 (Wiki only) / L2 (Fleet) / L3 (Full PM) | Available infrastructure, orchestrator presence |
> | 7 | **What trust tier?** | Trainee / Standard / Expert | Approval rate data (if L2+), operator declaration (if L1) |

3. **The answers compose into a profile that selects everything downstream.** Identity → SDLC chain → methodology model → enforcement level → context depth → tool scope. Each step narrows based on the identity profile. An expert-tier agent on a v3 harness in a Production/1M TypeScript project gets FULL chain with FULL enforcement. A trainee-tier solo agent on v1 in a POC/10k Python project gets SIMPLIFIED chain with advisory rules only.

4. **Dual-scope tools must know the identity of BOTH the caller and the target.** When a project calls the second brain tools, the tools need to know: am I operating on the second brain itself, or on the project's internal wiki? The same query ("what artifacts does Document stage need?") returns different answers based on the target project's domain profile.

5. **The five cognitive contexts from OpenArms are instances of this problem.** Interactive operator (Context A) is a human + system. Solo agent (Context B) is a harness session. Sub-agents (Context C) are trustless workers. Provisioned agents (Context E) are persistent live systems. Each needs different rules from the same knowledge base. The self-identification protocol solves this: declare your context upfront, receive context-appropriate rules.

## Deep Analysis

### The Identity Profile

When an agent, harness, or tool connects to the second brain, it should declare (or the system should detect) a profile:

```yaml
# Example: OpenArms harness-managed agent (harness v2)
identity:
  execution_mode: harness-v2     # solo | harness-v1 | harness-v2 | harness-v3 | full-system
  domain: typescript             # from domain-profiles/*.yaml
  project_phase: mvp             # poc | mvp | staging | production
  codebase_scale: medium         # micro | small | medium | large | massive
  pm_level: L2                   # L1 | L2 | L3
  trust_tier: standard           # trainee | standard | expert
  second_brain: connected        # self | connected | none
```

```yaml
# Example: Research wiki (solo mode — human + Claude, no harness)
identity:
  execution_mode: solo           # no harness, no loop, just conversation
  domain: knowledge
  project_phase: production
  codebase_scale: medium
  pm_level: L1
  trust_tier: operator-supervised
  second_brain: self             # IS the second brain
```

```yaml
# Example: OpenFleet agent (full system — fleet with orchestrator)
identity:
  execution_mode: full-system    # orchestrator + immune system + 10 agents
  domain: typescript
  project_phase: staging
  codebase_scale: large
  pm_level: L3
  trust_tier: data-driven        # approval rates per model per task type
  second_brain: connected
```

This profile determines:

> [!info] What the Identity Profile Selects
>
> | From Profile | Selects | Example |
> |-------------|---------|---------|
> | type + harness_version | Which rules apply to ME | Solo agent gets methodology hooks. Human operator gets investigation tools. Sub-agent gets trustless rules. |
> | domain | Which domain profile and artifact chain | TypeScript: pnpm gates, src/ paths. Python: pipeline post, wiki/ paths. |
> | project_phase + codebase_scale | SDLC chain | POC + micro = simplified. Production + large = full. See [[SDLC Customization Framework — Phases, Scale, and Chain Selection]] |
> | pm_level | Available enforcement infrastructure | L1: CLAUDE.md only. L2: hooks + commands + dispatch. L3: + sprint planning + Plane sync. |
> | trust_tier | Context depth and autonomy | Expert: full context, all stages. Trainee: minimal context, restricted stages. See [[Tier-Based Context Depth — Trust Earned Through Approval Rates]] |
> | second_brain | Tool scope | Connected: query second brain for methodology + standards. Local-only: use project's own wiki. None: CLAUDE.md rules only. |

### The Goldilocks Selection Matrix

> [!abstract] "Just Right" Process by Identity
>
> | Identity | Too Little (Mountain) | Just Right (Pyramid) | Too Much (Skyscraper) |
> |----------|----------------------|---------------------|----------------------|
> | Solo agent, POC, micro, L1 | No process at all — chaos | Simplified chain, advisory rules, 2-3 stages | Full chain + hooks + validator = kills velocity |
> | Harness agent, MVP, medium, L2 | CLAUDE.md rules only — 25% compliance | Default chain, hooks + commands, 3-5 stages | Full chain + immune system + fleet = overkill for 1 agent |
> | Fleet agent, Production, large, L3 | Default chain — insufficient traceability | Full chain, immune system, contribution gating, sprints | N/A — at this scale, full process IS just right |
> | Sub-agent, any | Behavioral rules in prompt (33% compliance) | Trustless verification (accept non-compliance, verify output) | Hook injection into sub-agents (high cost, low ROI) |
> | Human operator, any | No second brain reference | Connected to second brain, queries methodology as needed | Forced to follow agent methodology — wrong context |

### What Makes It Work — Where Is the Magic?

The operator asked: "What makes this work? Where is all the magic? What is the intelligence, the structure and the way?"

> [!tip] The Three Sources of Intelligence
>
> 1. **Structure** — YAML frontmatter, consistent markdown patterns, typed fields, stage protocols, MUST/MUST NOT blocks. Structure IS the programming language. See [[Structured Context Is Proto-Programming for AI Agents]].
>
> 2. **Infrastructure** — Hooks block wrong actions. Commands own state transitions. Harness owns the loop. Immune system detects and corrects. Each layer is invisible to the layer below it (agents don't see the doctor). See [[Infrastructure Enforcement Proves Instructions Fail]], [[Three Lines of Defense — Immune System for Agent Quality]].
>
> 3. **Knowledge** — The second brain contains methodology, standards, lessons, patterns, decisions. Projects don't invent from scratch — they query the brain, adapt to their domain, and feed learnings back. The brain is always AHEAD of any individual project. See [[Ecosystem Feedback Loop — Wiki as Source of Truth]].
>
> The magic is in the COMPOSITION of all three: the right structure (Goldilocks profile → chain selection) + the right infrastructure (hooks/commands/harness appropriate to the PM level) + the right knowledge (second brain queried at the appropriate depth for the trust tier).

### Connection to Global Standards

The Goldilocks Framework should adhere to recognized standards where applicable:

> [!info] Standards Alignment
>
> | Standard | How It Applies |
> |----------|---------------|
> | **CloudEvents** | Event-driven automation (post-write hooks, dispatch events) should follow CloudEvents spec for interoperability |
> | **OpenAPI** | Gateway tools API should be OpenAPI-documented for machine consumption |
> | **SFIF** | The 4-stage build lifecycle (Scaffold→Foundation→Infrastructure→Features) governs how projects BUILD the Goldilocks infrastructure itself |
> | **Domain-Driven Design** | Domain boundaries (ai-agents, devops, knowledge-systems) follow DDD bounded context principles |
> | **Onion Architecture** | The layered enforcement (instructions → hooks → harness → immune system) follows onion principles: inner layers don't know about outer layers |
> | **SRP** | Each tool, hook, command has a SINGLE responsibility. Validators validate. Hooks block. Commands transition. |
> | **OOP / Design Patterns** | Observer (immune system watches agents), Strategy (methodology model selection), Factory (template scaffolding), Chain of Responsibility (enforcement hierarchy) |

### Real-World Identity Profiles — Ecosystem Evidence

> [!example]- OpenArms: Five Contexts, One CLAUDE.md (the problem)
>
> OpenArms discovered that its SINGLE CLAUDE.md is read by 5 cognitive contexts (interactive operator, solo agent, sub-agents, persona templates, provisioned live agents). Rules meant for Context A (operator) actively mislead Context B (solo agent). Example: "After compaction, re-read ALL memories" — Context A has persistent memory, Context B does not.
>
> **Goldilocks lesson:** A project can't be Goldilocks with ONE context file serving FIVE contexts. The identity profile must be DECLARED per context, and rules must be FILTERED by that declaration. OpenArms's recommended fix: move solo-agent rules to skills (infrastructure injection), keep CLAUDE.md for shared + operator rules (clearly marked).

> [!example]- OpenFleet: Identity Built Into Orchestration
>
> OpenFleet's 10 agents each have: a ROLE (software-engineer, architect, QA, PM, fleet-ops, devsecops), a TIER (trainee→expert), a LIFECYCLE STATE (active/idle/sleeping/offline), and STANDING ORDERS (conservative/standard/autonomous authority). The orchestrator reads ALL of these before making dispatch decisions.
>
> **Goldilocks lesson:** At fleet scale, identity isn't a one-time declaration — it's a CONTINUOUS profile that changes with trust (approval rates), state (active vs stuck), and context (what task, what stage, what contributions received).

> [!example]- Research Wiki: The Self-Referential Case
>
> This wiki is simultaneously: the FRAMEWORK (defines methodology for all projects), an INSTANCE (follows its own methodology), and the SECOND BRAIN (other projects query it). Its identity profile: type=system, domain=knowledge, phase=production (used daily), scale=medium (264 pages), pm_level=L1 (wiki only, no fleet), trust_tier=operator-supervised.
>
> **Goldilocks lesson:** The framework must work when applied to ITSELF. If the wiki's own methodology is too heavy to follow (Skyscraper chain for every wiki page), that's evidence the chain is miscalibrated.

### How This Connects to Everything

> [!abstract] From Goldilocks → Every Part of the System
>
> | Identity Answer | Leads To |
> |-----------------|----------|
> | What am I? → system/harness/solo/sub-agent | [[Three PM Levels — Wiki to Fleet to Full Tool]] — determines enforcement infrastructure |
> | What version? → v1/v2/v3 | [[Enforcement Hook Patterns]] (v2) → [[Three Lines of Defense — Immune System for Agent Quality]] (v2+) → [[Harness-Owned Loop — Deterministic Agent Execution]] (v2+) |
> | What domain? | Domain profiles in `wiki/config/domain-profiles/` → artifact chains per domain |
> | What phase? + What scale? | [[SDLC Customization Framework — Phases, Scale, and Chain Selection]] → chain selection matrix |
> | What PM level? | [[Readiness vs Progress — Two-Dimensional Work Tracking]] — tracking depth matches PM level |
> | What trust tier? | [[Tier-Based Context Depth — Trust Earned Through Approval Rates]] — context depth adapts per tier |
> | All answers combined | [[Methodology Adoption Guide]] — selects tier + chain + domain + enforcement |

## Open Questions

> [!question] Can the identity profile be auto-detected or must it be declared?
> Some dimensions are detectable (domain from package.json, scale from loc count, harness version from available tools). Others require declaration (project phase, trust tier). Which should be auto-detected vs declared?

> [!question] Should the second brain tools accept an identity profile parameter?
> When a project queries `gateway query --stage document --domain typescript`, should it also pass `--phase mvp --scale medium`? This would enable the gateway to return phase-appropriate artifacts.

> [!question] How do we prevent projects from over-declaring their trust tier?
> A project claiming "expert" when it should be "trainee" gets inappropriate autonomy. OpenFleet solves this with data-driven tiers. Can the second brain verify claims?

## Relationships

- BUILDS ON: [[SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- BUILDS ON: [[Three PM Levels — Wiki to Fleet to Full Tool]]
- BUILDS ON: [[Tier-Based Context Depth — Trust Earned Through Approval Rates]]
- RELATES TO: [[Structured Context Is Proto-Programming for AI Agents]]
- RELATES TO: [[Readiness vs Progress — Two-Dimensional Work Tracking]]
- RELATES TO: [[Infrastructure Enforcement Proves Instructions Fail]]
- RELATES TO: [[Ecosystem Feedback Loop — Wiki as Source of Truth]]
- FEEDS INTO: [[Wiki Gateway Tools — Unified Knowledge Interface]]
- FEEDS INTO: [[Methodology Adoption Guide]]
- FEEDS INTO: [[Super-Model: Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[Three PM Levels — Wiki to Fleet to Full Tool]]
[[Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[Structured Context Is Proto-Programming for AI Agents]]
[[Readiness vs Progress — Two-Dimensional Work Tracking]]
[[Infrastructure Enforcement Proves Instructions Fail]]
[[Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[Wiki Gateway Tools — Unified Knowledge Interface]]
[[Methodology Adoption Guide]]
[[Super-Model: Research Wiki as Ecosystem Intelligence Hub]]
[[Global Standards Adherence — Engineering Principles the Wiki Follows]]
[[Principle: Infrastructure Over Instructions for Process Enforcement]]
[[Principle: Right Process for Right Context — The Goldilocks Imperative]]
[[Principle: Structured Context Governs Agent Behavior More Than Content]]
[[The Wiki Is a Hub, Not a Silo]]

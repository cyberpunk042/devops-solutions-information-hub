---
title: Project Self-Identification Protocol — The Goldilocks Framework
aliases:
  - "Project Self-Identification Protocol — The Goldilocks Framework"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: operator-goldilocks
    type: directive
    file: raw/notes/2026-04-12-goldilocks-higher-ground-directive.md
    description: "Operator: 'AM I a system? Am I a harness? V2? V3? Am I just a solo agent session? What is my domain? What makes this work? Where is all the magic?'"
  - id: openarms-five-contexts
    type: observation
    file: raw/articles/openarms-all-distilled-lessons.md
    description: OpenArms discovered 5 cognitive contexts reading one CLAUDE.md — rules meant for one context mislead another
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

1. **Self-identification is prerequisite to methodology selection.** Before an agent or system can choose a methodology model, SDLC profile, or enforcement level, it must know WHAT it is. OpenArms discovered this the hard way: 5 cognitive contexts reading one CLAUDE.md, each needing different rules, none marked.

2. **Seven identity dimensions determine "just right."**

> [!abstract] The Seven Questions
>
> | # | Question | Values | Source | Auto-Detectable? |
> |---|---------|--------|--------|-----------------|
> | 1 | **What am I?** | Solo / harness-managed / fleet agent / sub-agent | The PROGRAM that launched you decides this | **No** — the harness/system tells you at runtime, or you're in solo mode (certain if no harness code exists) |
> | 2 | **What execution mode?** | solo / harness v1 / harness v2 / harness v3 / full system | The harness decides its own version at launch based on its flags and capabilities | **No** — filesystem shows what CAPABILITIES exist, not what mode is RUNNING. Declare in CLAUDE.md or pass at runtime. |
> | 3 | **What domain?** | TypeScript / Python / Infrastructure / Knowledge / Mixed | package.json, pyproject.toml, main.tf, wiki/config/ | **Yes** — detectable from project marker files |
> | 4 | **What project phase?** | POC / MVP / Staging / Production | CI presence, test presence, Docker/deployment markers | **Partially** — heuristic from CI+tests+deploy markers. Operator should confirm. |
> | 5 | **What scale?** | micro / small / medium / large / massive | Source file count (excluding vendored deps) | **Yes** — detectable by counting source files |
> | 6 | **What PM level?** | L1 (Wiki only) / L2 (Fleet) / L3 (Full PM) | What infrastructure is available AND running | **No** — same problem as execution mode. Infrastructure may exist but not be active. |
> | 7 | **What trust tier?** | Trainee / Standard / Expert | Approval rate data (fleet), operator declaration (solo) | **No** — requires operational data (approval rates) or explicit declaration |
>
> **Critical distinction:** Questions 3 and 5 are auto-detectable from the filesystem. Questions 1, 2, 6, 7 CANNOT be auto-detected — they depend on RUNTIME state or operational data that the project files don't contain. Question 4 is partially detectable (heuristic). When auto-detection can't determine the answer, the gateway says "unknown — declare in CLAUDE.md or pass at runtime" and warns the user.

3. **The answers compose into a profile that selects everything downstream.** Identity → SDLC profile → methodology model → enforcement level → context depth → tool scope. Each step narrows based on the identity profile. An expert-tier agent on a v3 harness in a Production/1M TypeScript project gets FULL profile with FULL enforcement. A trainee-tier solo agent on v1 in a POC/10k Python project gets SIMPLIFIED profile with advisory rules only.

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
> | project_phase + codebase_scale | SDLC profile | POC + micro = simplified. Production + large = full. See [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]] |
> | pm_level | Available enforcement infrastructure | L1: CLAUDE.md only. L2: hooks + commands + dispatch. L3: + sprint planning + Plane sync. |
> | trust_tier | Context depth and autonomy | Expert: full context, all stages. Trainee: minimal context, restricted stages. See [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]] |
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
> 1. **Structure** — YAML frontmatter, consistent markdown patterns, typed fields, stage protocols, MUST/MUST NOT blocks. Structure IS the programming language. See [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]].
>
> 2. **Infrastructure** — Hooks block wrong actions. Commands own state transitions. Harness owns the loop. Immune system detects and corrects. Each layer is invisible to the layer below it (agents don't see the doctor). See [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]], [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]].
>
> 3. **Knowledge** — The second brain contains methodology, standards, lessons, patterns, decisions. Projects don't invent from scratch — they query the brain, adapt to their domain, and feed learnings back. The brain is always AHEAD of any individual project. See [[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]].
>
> The magic is in the COMPOSITION of all three: the right structure (Goldilocks profile → SDLC profile selection) + the right infrastructure (hooks/commands/harness appropriate to the PM level) + the right knowledge (second brain queried at the appropriate depth for the trust tier).

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
> | What am I? → system/harness/solo/sub-agent | [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] — determines enforcement infrastructure |
> | What version? → v1/v2/v3 | [[enforcement-hook-patterns|Enforcement Hook Patterns]] (v2) → [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]] (v2+) → [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]] (v2+) |
> | What domain? | Domain profiles in `wiki/config/domain-profiles/` → artifact chains per domain |
> | What phase? + What scale? | [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]] → profile selection matrix |
> | What PM level? | [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] — tracking depth matches PM level |
> | What trust tier? | [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]] — context depth adapts per tier |
> | All answers combined | [[methodology-adoption-guide|Methodology Adoption Guide]] — selects tier + profile + domain + enforcement |

## Open Questions

> [!question] ~~Can the identity profile be auto-detected or must it be declared?~~
> **RESOLVED:** Both — different dimensions. Domain and scale are auto-detectable from filesystem (package.json, file count). Execution mode, PM level, and trust tier cannot be auto-detected — they depend on runtime state. Phase is partially detectable (CI + tests + deploy markers). The gateway reports what it can detect and says "unknown — declare in CLAUDE.md" for the rest. See [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]].

> [!question] ~~Should the second brain tools accept an identity profile parameter?~~
> **RESOLVED:** Yes. Gateway already has --wiki-root for dual-scope. Add --identity to pass a profile. PARTIALLY RESOLVED — gateway supports it conceptually. **PARTIALLY RESOLVED**
> The gateway auto-detects domain (used for `--stage` queries). Other dimensions should be passable but NOT required — the gateway warns when it can't detect and suggests declaring. The `what-do-i-need` command shows detected + unknown dimensions together.

> [!question] ~~How do we prevent projects from over-declaring their trust tier? **OPEN**~~
> **RESOLVED:** Compliance rate verification. A project claiming "expert" with 60% compliance gets flagged. Trust is EARNED through approval rates, not declared.
> Trust tier is a runtime/operational property. A project in solo mode has no approval rate data — the operator declares it. A fleet has data. The second brain could theoretically verify claims by checking operational evidence, but this requires the project to SHARE its data. OpenFleet shares via Plane sync. Solo projects have no mechanism. This remains open.

## Relationships

- BUILDS ON: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]]
- BUILDS ON: [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
- BUILDS ON: [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
- RELATES TO: [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
- RELATES TO: [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
- RELATES TO: [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
- RELATES TO: [[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
- FEEDS INTO: [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- FEEDS INTO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
[[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[e013-super-model-evolution-v2-0-with-sub-super-models|E013 — Super-Model Evolution — v2.0 with Sub-Super-Models]]
[[e014-goldilocks-navigable-system-identity-to-action-in-continuous-flow|E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow]]
[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property — Guard Against Conflation Drift]]
[[global-standards-adherence|Global Standards Adherence — Engineering Principles the Wiki Follows]]
[[goldilocks-flow|Goldilocks Flow — From Identity to Action]]
[[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[the-wiki-is-a-hub-not-a-silo|The Wiki Is a Hub, Not a Silo]]

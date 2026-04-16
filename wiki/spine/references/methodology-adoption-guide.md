---
title: Methodology Adoption Guide
aliases:
  - "Methodology Adoption Guide"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-11
updated: 2026-04-13
sources:
  - id: methodology-config
    type: file
    file: wiki/config/methodology.yaml
  - id: domain-profiles
    type: file
    file: wiki/config/domain-profiles/
  - id: artifact-types
    type: file
    file: wiki/config/artifact-types.yaml
  - id: openarms-evidence
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms methodology.yaml configuration"
tags: [methodology, adoption, guide, onboarding, ecosystem]
---

# Methodology Adoption Guide

> [!tip] AI Quick Start — Setting Up Methodology for Your Project
>
> 1. **Identify yourself first**: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — answer the 7 questions (What am I? What version? What domain? What phase? What scale? What PM level? What trust tier?)
> 2. **Pick your SDLC profile**: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]] — simplified (POC), default (MVP/Staging), or full (Production)
> 3. **Pick your enforcement tier**: Tier 1 (read) → Tier 2 (configure) → Tier 3 (validate) → Tier 4 (enforce) — matched to your PM level
> 4. **Pick your domain**: TypeScript, Python/Wiki, Infrastructure, or Knowledge — see per-domain quick starts below
> 5. **Connect to the second brain**: query methodology + standards via gateway tools (or read wiki pages directly)
> 6. **Invariants that NEVER change**: stage boundaries are hard, readiness AND progress are computed, 99→100 is human-only

## Summary

Step-by-step guide for any project to adopt the research wiki's methodology. Covers the four adoption tiers — from reading the wiki models to running full infrastructure enforcement. Includes concrete configuration examples for TypeScript, Python/wiki, and infrastructure projects. The wiki produces the methodology; projects consume it at whatever depth matches their needs.

## Reference Content

### Adoption Tiers

> [!info] Four Tiers of Adoption
>
> | Tier | What You Get | Effort | Prerequisites |
> |------|-------------|--------|---------------|
> | **1. Read** | Read models + standards pages, follow manually | Minutes | None — just read the wiki |
> | **2. Configure** | Copy methodology.yaml + domain profile, reference in CLAUDE.md | Hours | Access to wiki config/ |
> | **3. Validate** | Add artifact-type checks to your validation pipeline | Days | Tier 2 + validation tooling |
> | **4. Enforce** | Add hooks, stage skills, deterministic dispatch | Weeks | Tier 3 + harness infrastructure |

> [!tip] Start at Tier 1, climb when you feel the pain
>
> Most projects should start by reading the models and following them manually. When agents start skipping stages or producing wrong artifacts, move to Tier 2. When you can't tell if methodology was followed, add Tier 3. When you run autonomous agents overnight, you need Tier 4.

> [!warning] Two reading orders — pick yours (NEW 2026-04-16, from first consumer integration)
>
> | You are... | Read this order | Why |
> |---|---|---|
> | **Learning** (no existing methodology) | Models first → then standards | Models teach WHAT the system IS; standards come after understanding |
> | **Integrating** (existing methodology infrastructure) | Standards first → then models | Standards tell you "what good looks like" — you assess your gaps against them. Models explain the system you're aligning with. |
>
> **Scale reality check:** Full integration from Tier 1 to Tier 4 is approximately **23 epics, 125-185 tasks, 5 milestones across months of sustained effort.** Tier 1 is minutes. Tier 2 is hours. Tier 3 is days-to-weeks. Tier 4 is weeks-to-months. Don't plan for a weekend — plan for graduated adoption over time. Evidence: OpenArms first consumer integration (2026-04-16).

> [!success] First Consumer Adoption Evidence — OpenArms Tier 0 → Tier 2 in one session (2026-04-16)
>
> What actually happened vs what was documented in the guide. OpenArms (TypeScript/Node harness project, 5 months of prior methodology evolution) integrated with the second brain over one session producing 15 adoption items and 14 contributions.
>
> **What took less time than expected (under ~1 hour each):**
>
> | Work | Why it was fast |
> |---|---|
> | Adopt page templates (7 files) | `gateway template <type>` returned full templates with inline guidance. Copy + adapt, done. |
> | Apply compliance checker | `gateway compliance` (after functional-equivalence fix) pointed at exact gaps |
> | Contribute first lesson back | `gateway contribute` normalized format on intake — no format conversion needed |
> | Declare Identity Profile (stable fields only) | Separating stable-from-consumer properties prevented the overload trap |
>
> **What took more time than expected (half-day to full-day each):**
>
> | Work | Why it was slow |
> |---|---|
> | AGENTS.md restructure (471 → 124) | Extracting 12 companion rule files + deciding what routes where. Required real design thinking. |
> | Progress field across 4 CJS scripts + schema | Two-field model touched every frontmatter reader. Plus a progress-cap bug found during adoption. |
> | Typed impediments (8-value taxonomy in `/concern`) | Updating every concern trigger and documentation site |
> | Artifact path verification | Integrating fs.existsSync check into gate-close flow, handling edge cases |
>
> **What was revealed but NOT shipped this session (Milestone 1+ work):**
>
> - Mandatory skills as gates (skill invocation verification) — requires `invoked-skills.log` infrastructure
> - Tier-based context depth per task type — requires harness prompt builder evolution
> - Rule files adopting Patterns 7-8 (Anchor Phrases, Concrete Examples) — per-rule-file restructure
> - Validation Matrix for the 5 skills — test suite infrastructure (see [[validation-matrix-test-suite-for-context-injection|the pattern]])
> - Stage return mechanism — harness architecture change
> - Full Rule 8 auto-generation — semantic understanding of epic scope
>
> **Practical implication for adopters:** the "quick wins" are templates + compliance + first contribution. Expect half a day for identity+AGENTS.md restructure. Expect a full day per schema field you add (progress, impediment_type). Plan M1+ for the infrastructure-level work (mandatory-as-gate, tier routing, validation matrix). See [[identity-profile|OpenArms — Identity Profile]] for the full 22-item adoption log with commits.
>
> **Structural vs operational compliance distinction (critical):** OpenArms's session continued past "Tier 2" and reached **Tier 4 STRUCTURAL compliance** (compliance checker: all 4 tiers 3/3) by adding `wiki/patterns/` + `wiki/decisions/` directories, an `export-profiles.yaml` config, and a `tools/evolve.py` stub. These satisfy the structural checks that `gateway compliance` measures. They do NOT constitute operational Tier 3-4 — the evolve.py is a stub, the export profiles have no runtime pipeline. Honest reporting: "Tier 4 structural / Tier 2+ operational." See [[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]]. Adopters should separate the two dimensions in their own reporting from day 1.

### Tier 1: Read (learning path) / Assess (integration path)

**Learning path** (no existing methodology):

1. **Start here:** [[model-methodology|Model — Methodology]] — the 9 named models and when to use each
2. **Understand stages:** [[stage-gate-methodology|Stage-Gate Methodology]] — the 5 stages and their boundaries
3. **Know the artifacts:** [[artifact-chains-by-model|Artifact Chains by Methodology Model]] — what each stage produces
4. **Quality tiers:** [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]] — choose your quality level explicitly

**Integration path** (existing methodology, need alignment):

1. **Standards first:** `python3 -m tools.view standards` — what "good" looks like per artifact type
2. **Check compliance:** `python3 -m tools.gateway compliance` — which tier you're functionally at
3. **Query your gaps:** `python3 -m tools.gateway query --model <your-task-type> --full-chain` — what the canonical chain expects
4. **Then models:** `python3 -m tools.view model methodology` — the full system to understand WHY
5. **Then health:** `python3 -m tools.gateway health --verbose` — page-level validation against your own schema

Then in your CLAUDE.md, add a reference:

```markdown
## Methodology

This project follows the methodology defined in the devops-solutions-research-wiki.
See: wiki/spine/models/foundation/model-methodology.md for models, wiki/spine/standards/model-standards/model-methodology-standards.md for quality bar.

Stage gates: Document → Design → Scaffold → Implement → Test
Never skip stages. "Continue" means advance within the current stage, not skip ahead.
```

### Tier 2: Configure

Copy the methodology config and declare your domain profile.

**Step 1: Copy the methodology config**

```bash
# From the research wiki
cp wiki/config/methodology.yaml /your-project/config/methodology.yaml
```

Or reference it directly if your project has access to the wiki repo.

**Step 2: Select your domain profile**

```bash
# Choose the profile matching your stack
cp wiki/config/domain-profiles/typescript.yaml /your-project/config/domain-profile.yaml
# or: python-wiki.yaml, infrastructure.yaml
```

**Step 3: Add project-specific overrides**

Create a project override file layered on top:

```yaml
# /your-project/config/methodology-overrides.yaml
# Extends the generic methodology.yaml with project-specific details

project: my-project
domain_profile: typescript  # or python-wiki, infrastructure

overrides:
  # Add project-specific gate commands
  stages:
    implement:
      gate_commands:
        - "pnpm tsgo"
        - "pnpm check"
        - "pnpm my-project-specific-check"

  # Restrict models if your project only needs a subset
  enabled_models:
    - feature-development
    - bug-fix
    - hotfix
    - documentation

  # Project-specific forbidden zones
  forbidden_zones:
    document: ["src/", "tests/"]
    design: ["src/", "tests/"]
```

**Step 4: Reference in CLAUDE.md**

```markdown
## Methodology

This project uses the research wiki methodology engine.
Config: wiki/config/methodology.yaml (generic) + config/methodology-overrides.yaml (project)
Domain profile: typescript

### Stage Gates (enforced)
- Document (0-25%): Wiki pages only. No src/ writes.
- Design (25-50%): Design docs only. No src/ writes.
- Scaffold (50-80%): Types and stubs only. No business logic.
- Implement (80-95%): Business logic. Must wire into existing runtime.
- Test (95-100%): Real assertions. 0 failures.

### Model Selection
- epic/module/task → feature-development (5 stages)
- bug → bug-fix (3 stages: document, implement, test)
- hotfix → hotfix (2 stages: implement, test)
- docs → documentation (1 stage: document)
```

### Tier 3: Validate

Extend your project's validation to check methodology compliance.

**Option A: Use artifact-types.yaml for per-type validation**

```bash
cp wiki/config/artifact-types.yaml /your-project/config/artifact-types.yaml
```

Then extend your validation tool to read it (see research wiki's tools/validate.py for the pattern — it reads artifact-types.yaml for content thresholds, styling requirements, and per-type frontmatter checks).

**Option B: Add stage-gate checks to CI**

```yaml
# In your CI config
methodology-check:
  script:
    - python3 scripts/check-stage-gate.py
  rules:
    - "No src/ files in document-stage commits"
    - "No test files in implement-stage commits"
    - "Scaffold commits have no function bodies >3 lines"
```

### Tier 4: Enforce

Full infrastructure enforcement — hooks, stage skills, deterministic dispatch.

> [!warning] Tier 4 Requires a Harness
>
> Infrastructure enforcement means the agent doesn't control git, task selection, or stage advancement. A harness owns the loop. Quantified evidence: instructions alone = 25% compliance, hooks = 100% stage boundary compliance (OpenArms v10, 5 production runs). See [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]].

**Components needed:**

| Component | Purpose | Real Implementation |
|-----------|---------|---------------------|
| Pre-bash hook | Block git commands from agent | OpenArms: 48 lines, blocks `git add/commit/push/revert`, gates test commands to test stage |
| Pre-write hook | Block wrong-scope writes per stage | OpenArms: 106 lines, 5 enforcement layers including frontmatter protection and test assertion counting |
| Post-write hook | Track files created per stage | OpenArms: 36 lines, logs `stage:filepath` for artifact verification |
| Post-compact hook | Rebuild context after compaction | OpenArms: 29 lines, rebuilds full task state from files. See [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] |
| Stage validation script | Check artifacts before advancing | OpenArms: 1,033 lines, model-aware, business logic detection, phantom file filtering |
| Commands | /stage-complete, /task-done | Agent calls command → harness validates + commits + advances |
| Stage skills | Per-stage instructions injected into context | OpenArms: 5 skills, dynamically populated from model config |

> [!tip] Reference Implementations (updated 2026-04-12)
>
> **OpenArms (v10)** — Solo agent, TypeScript:
> - 14 enforcement scripts + 4 hooks (215 lines) + 3 commands + 5 stage skills
> - Model-aware validation (reads current-model-config.json, adapts per task type)
> - Result: 0% stage violations. But 80% of runs still need manual fixes (behavioral failures persist). See [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
>
> **OpenFleet** — 10-agent fleet, Python:
> - MCP tool blocking per stage (enforcement at server level, stronger than hooks)
> - 3-line immune system: prevention → detection (30s doctor cycle) → correction (TEACH/COMPACT/PRUNE/ESCALATE). See [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
> - Contribution gating: cross-agent inputs required BEFORE work stage. See [[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
> - Tier-based context depth: trust earned through approval rates. See [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
>
> **Key principle:** Every block must be mindful — explain WHY, offer justified bypass. See [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]

### SDLC Profile Selection

> [!info] Choose Your Process Weight
>
> Not every project needs full Tier 4 enforcement. Process weight depends on project phase and codebase scale:
>
> | Profile | When | Stages | Artifacts | Enforcement |
> |---------|------|--------|-----------|-------------|
> | **Simplified** | POC, micro/small scale | 2-3 | Minimal | Tier 1-2 (instructions + config) |
> | **Middle Ground** (default) | MVP→Staging, small→medium | 3-5 | Core + important | Tier 2-3 (config + validation) |
> | **Full** | Production, medium→massive | All 5 | Complete artifact chain | Tier 3-4 (validation + enforcement) |
>
> See [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]] for the full decision matrix.

### Per-Domain Quick Start

> [!abstract] TypeScript Project Quick Start
>
> 1. Copy: `methodology.yaml`, `domain-profiles/typescript.yaml`, `artifact-types.yaml`
> 2. CLAUDE.md: Add stage gate rules with `pnpm tsgo` / `pnpm check` / `pnpm test` gates
> 3. Hooks (optional): pre-write blocks `src/` during document/design stages
> 4. Verify: agent produces wiki pages before code, types before logic, tests last

> [!abstract] Python/Wiki Project Quick Start
>
> 1. Copy: `methodology.yaml`, `domain-profiles/python-wiki.yaml`, `artifact-types.yaml`
> 2. CLAUDE.md: Add stage gate rules with `pipeline post` / `validate` gates
> 3. Hooks (optional): pre-write blocks `tools/` during document stage
> 4. Verify: agent reads existing pages before writing new ones, runs post-chain after changes

> [!abstract] Infrastructure Project Quick Start
>
> 1. Copy: `methodology.yaml`, `domain-profiles/infrastructure.yaml`, `artifact-types.yaml`
> 2. CLAUDE.md: Add stage gate rules with `terraform validate` / `terraform plan` gates
> 3. Hooks (optional): pre-write blocks `*.tf` during document/design stages
> 4. Verify: agent documents current infrastructure before making changes

### PM Level Selection

The adoption tier (what enforcement) and PM level (what infrastructure) are independent choices:

> [!info] PM Level → Harness Version → Capabilities
>
> | PM Level | System | Harness | Readiness Enforcement | Progress Tracking |
> |----------|--------|---------|----------------------|-------------------|
> | **L1: Wiki LLM** | In-repo backlog, CLAUDE.md | v1 (standalone) | Advisory — agent may ignore | Frontmatter only |
> | **L2: Fleet** | Orchestrator, hooks, immune system | v2 (enforced) | Structural — dispatch gated | Real-time via fleet tools |
> | **L3: Full PM** | Plane/DSPD, SCRUM/agile | v3 (integrated) | Organizational — sprint scope | Burndown, velocity, time |
>
> Each level wraps the previous. L2 reads L1's data. L3 syncs with L2's state.
> See [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] for the full architecture.

### Readiness vs Progress

Track BOTH dimensions independently. Readiness = is it defined? Progress = is it built?

> [!warning] Key Rules
>
> - Readiness gates progress — don't start building until readiness crosses a threshold
> - Both are derived for containers (epics, modules) — never set manually
> - 99→100 = HUMAN ONLY on both dimensions — adversarial review required
> - See [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] for the full model

### Invariants (All Tiers, All PM Levels)

> [!warning] These Rules Apply Everywhere
>
> 1. **Never skip stages** — "continue" means advance within current stage, not skip ahead
> 2. **Quality tier is explicit** — choose Skyscraper, Pyramid, or Mountain deliberately. Mountain is the anti-pattern.
> 3. **Artifacts are evidence** — stages produce verifiable deliverables, not claims
> 4. **Readiness AND progress are computed** — from stage completion and child propagation, never manually claimed
> 5. **Done When items are specific** — name files, functions, endpoints. Generic boilerplate lets agents cheat.
> 6. **99→100 is human-only** — no automated system marks work as complete. Review is adversarial.
> 7. **Enforcement must be mindful** — every block explains WHY and offers justified bypass. See [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]].

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Principles** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] · [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] · [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **Identity** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- BUILDS ON: [[model-composition-rules|Model Composition Rules]]
- RELATES TO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[four-project-ecosystem|Four-Project Ecosystem]]
- FEEDS INTO: [[model-ecosystem|Model — Ecosystem Architecture]]
- FEEDS INTO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[model-methodology|Model — Methodology]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[model-composition-rules|Model Composition Rules]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[ai-agent-artifacts|AI Agent Artifacts — Standards and Guide]]
[[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
[[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]
[[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
[[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
[[artifact-path-verification-at-gate-close|Artifact Path Verification at Gate Close]]
[[aspirational-declaration-without-enforcement|Aspirational Declaration Produces False Confidence at Every Layer]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[consumer-integration-roadmap-exemplar|Consumer Integration Roadmap — OpenArms Exemplar (First Full Plan)]]
[[context-depth-must-vary-per-task-type-not-per-project|Context Depth Must Vary Per Task Type, Not Per Project — Tier Selection Extends Beyond Identity]]
[[when-to-use-milestone-vs-epic-vs-module-vs-task|Decision — When to Use Milestone vs Epic vs Module vs Task]]
[[defense-layer-progression-is-expensive|Defense Layer Progression Is Expensive — Prevention Is Cheap, Detection and Correction Are Milestones]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]]
[[global-standards-adherence|Global Standards Adherence — Engineering Principles the Wiki Follows]]
[[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]]
[[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently Across Projects]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[methodology-fundamentals|Learning Path — Methodology Fundamentals]]
[[machine-specific-config-in-vcs-is-aspirational-portability|Machine-Specific Config in Version Control Is Aspirational Portability]]
[[mandatory-without-verification-is-not-enforced|Mandatory Without Verification Is Not Enforced — Skill-Layer Instance of Infrastructure > Instructions]]
[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[methodology-config-architecture|Methodology Config Architecture — How the Pieces Fit Together]]
[[methodology-evolution-protocol|Methodology Evolution Protocol]]
[[methodology-framework|Methodology Framework]]
[[methodology-system-map|Methodology System Map]]
[[model-context-engineering|Model — Context Engineering]]
[[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]]
[[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[progressive-structural-enrichment-in-agent-config|Progressive Structural Enrichment in Agent Config]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]]
[[sdlc-rules-and-structure-customizable-project-lifecycle|SDLC Rules and Structure — Customizable Project Lifecycle]]
[[stage-aware-skill-injection|Stage-Aware Skill Injection]]
[[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance — Compliance Checkers Measure Presence, Not Depth]]
[[src-sdlc-frameworks-research|Synthesis — SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
[[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[universal-stages-domain-specific-artifacts|Universal Stages, Domain-Specific Artifacts]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]

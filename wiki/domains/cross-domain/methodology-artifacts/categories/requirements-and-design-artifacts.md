---
title: Requirements and Design Artifacts — Standards and Guide
aliases:
  - "Requirements and Design Artifacts — Standards and Guide"
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
  - id: openarms-chain
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms artifact chain (24 artifacts at Default SDLC level)"
  - id: adr-github
    type: documentation
    url: https://adr.github.io/
  - id: martin-fowler-adr
    type: article
    url: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
tags: [methodology, requirements, design, artifacts, adr, tech-spec, interface-spec, standards]
---

# Requirements and Design Artifacts — Standards and Guide

> [!tip] AI Quick Start — You're in Document or Design Stage
>
> 1. **Document stage?** Produce: Requirements Spec (FR/NFR/AC), Infrastructure Analysis (file:line tables), Gap Analysis (per-gap with complexity)
> 2. **Design stage?** Produce: ADR (decision + alternatives + rationale), Tech Spec (components + API tables), Test Plan (test IDs + inputs + expected)
> 3. **Templates:** `wiki/config/templates/methodology/` has templates for all of these — scaffold from them
> 4. **The chain has dependencies:** ADR depends on requirements. Tech Spec depends on ADR. Interface Spec depends on Tech Spec. Test Plan depends on Interface Spec. Don't skip upstream documents.
> 5. **Scale matters:** Epic = full 8 documents. Module = sections in epic docs. Task = inherits from epic.

## Summary

Complete guide to the artifacts produced during the Document and Design stages — the specifications that CONSTRAIN all subsequent work. Requirements define WHAT must be built. Design defines HOW it will be built. Together they are the blueprints — without them, scaffold/implement/test stages have nothing to build from. Production evidence shows: "The documents ARE the gates. You CANNOT skip documents. The scaffold stage won't pass validation if there's no interface spec to scaffold FROM." This page covers 17 artifact types across requirements (7) and design (10), with quality standards, templates, domain variations, and the critical chain dependencies between them.

## Key Insights

1. **Requirements and design artifacts are the CONSTRAINING documents.** Unlike code artifacts (produced as side effects of building) or documentation (produced to explain what exists), these documents are DELIBERATELY CREATED to constrain what the agent or developer does next. A Requirements Spec says "you MUST build this." An ADR says "you MUST build it THIS way." An Interface Spec says "the types MUST look like this." They are binding, not aspirational.

2. **The Document stage produces 3 artifacts; the Design stage produces 5.** From the OpenArms 24-artifact chain: Document stage = Requirements Spec + Infrastructure Analysis + Gap Analysis. Design stage = ADR + Tech Spec + Interface Spec + Config Spec + Test Plan. These 8 document types are the foundation that everything else builds on.

3. **Requirements are DOMAIN-AGNOSTIC; design artifacts have domain-specific sections.** A Requirements Spec (FR/NFR/AC) looks the same whether building TypeScript code or Terraform infrastructure. But a Tech Spec for TypeScript includes "TypeScript types, function signatures" while a Tech Spec for infrastructure includes "Terraform resource definitions, provider configurations."

4. **The chain has dependencies — each document references the prior ones.** The ADR references the Requirements Spec (what problem it's solving). The Tech Spec references the ADR (what decision drives the design). The Interface Spec references the Tech Spec (what components need types). The Test Plan references the Interface Spec (what functions need tests). Breaking this chain means building without blueprints.

## Deep Analysis

### The Document Stage Artifacts (3 types)

These are produced during the Document stage (0-25% readiness). They answer: WHAT exists today, WHAT is needed, and WHAT is the gap.

#### Requirements Specification

> [!info] Defines WHAT must be built — FR, NFR, AC, Out of Scope
>
> | Aspect | Standard |
> |--------|---------|
> | **Sections** | Functional Requirements (FR-N), Non-Functional Requirements (NFR-N), Acceptance Criteria (AC-N), Out of Scope |
> | **FR format** | FR-N: "The system must [behavior]." Input: [trigger]. Output: [result]. Constraints: [limits]. |
> | **NFR format** | NFR-N: [Quality attribute] — [specific measurable metric] |
> | **AC format** | AC-N: [Verifiable statement that maps to Done When] |
> | **Quality bar** | Every FR has Input/Output/Constraints. Every AC is testable by running a command. Out of Scope explicitly names exclusions. |
> | **Anti-pattern** | "The system should be good" — vague, unverifiable. Must be: "FR-1: When X happens, the system must produce Y within Z seconds." |
> | **Template** | wiki/config/templates/methodology/requirements-spec.md |
> | **Variants** | BRD (business language, epic-level), FRD (functional detail, task-level), SRS (IEEE 830 formal, regulated systems) |
>
> **Good example from OpenArms:** "FR-1: When the agent calls /stage-complete during scaffold stage, the harness must verify that no new src/ files contain function bodies with control flow. Input: list of files from stage-files.log. Output: PASSED with next stage instructions or FAILED with file:line direction. Constraint: must complete in < 10 seconds."
>
> **Bad example:** "The system should validate stages" — no input, no output, no constraint, not testable.

#### Infrastructure Analysis

> [!info] Maps EXACTLY what exists today — files, components, data flow, dependencies
>
> | Aspect | Standard |
> |--------|---------|
> | **Sections** | Existing Infrastructure (File:line:export table), Data Flow, Dependencies, Integration Points |
> | **Quality bar** | Every referenced file VERIFIED to exist. Integration points have file:function:line. Data flow shows actual path, not theoretical. |
> | **Anti-pattern** | "There are config files" — must be: "src/config/types.agents.ts (45 LOC, exports AgentConfig type, relevant: add optional team field)" |
> | **Template** | wiki/config/templates/methodology/infrastructure-analysis.md |
>
> | Domain | What "infrastructure" means |
> |--------|---------------------------|
> | TypeScript | Source files, types, exports, test files, config files, package.json |
> | Python/Wiki | Wiki pages, config YAML, tool scripts, templates, schemas |
> | Infrastructure | Terraform state, resource definitions, provider configs, module structure |
> | Knowledge | Existing wiki pages on the topic, relationships, gaps, domain coverage |

#### Gap Analysis

> [!info] What's MISSING between current state and requirements
>
> | Aspect | Standard |
> |--------|---------|
> | **Format per gap** | Gap N: Title. Current state (with file refs). Required state. Impact. Affected files. Complexity (S/M/L/XL). |
> | **Quality bar** | At least one gap identified. Each gap references existing files. Impact is specific ("blocks scaffold stage") not vague. |
> | **Anti-pattern** | "More research needed" — that's a task, not a gap. Name WHAT specifically is missing. |
> | **Template** | wiki/config/templates/methodology/gap-analysis.md |

### The Design Stage Artifacts (5 types)

These are produced during the Design stage (25-50% readiness). They answer: HOW will the system work, WHAT decisions were made, WHAT will the code look like.

#### Architecture Decision Record (ADR)

> [!info] WHAT was decided and WHY — with alternatives and consequences
>
> | Aspect | Standard |
> |--------|---------|
> | **Sections** | Status, Context, Decision, Consequences (positive/negative/risks), Alternatives Considered |
> | **Quality bar** | ≥1 alternative with specific rejection reason. Decision is ONE clear statement. Consequences include risks. |
> | **Variants** | Nygard (lightweight), MADR (tradeoff analysis), Y-Statement ("In context C, facing F, we decided D...") |
> | **Status lifecycle** | Proposed → Accepted → Superseded (with link to replacement) |
> | **Template** | wiki/config/templates/decision.md (our decision type IS an ADR) |
> | **Anti-pattern** | "We decided to use X" — no context, no alternatives, no consequences. |
>
> **Extended record types beyond ADR:** Pattern Descriptions (documenting recurring solutions), Approved Standards (establishing norms), Exception Requests (when standards can't be met), Compliance Assessments (verifying adherence).

#### Technical Specification

> [!info] HOW the system works at a technical level — components, APIs, algorithms, errors
>
> | Aspect | Standard |
> |--------|---------|
> | **Sections** | Component Specs (responsibility/location/dependencies/consumers), API Table (function/input/output/side effects), Algorithm (pseudocode), Error Handling (error→response table), State Management |
> | **Quality bar** | Every exported function has an API entry. Every error case has a handling strategy. Component locations are real paths. |
> | **Template** | wiki/config/templates/methodology/tech-spec.md |
> | **Anti-pattern** | "The system will process data" — must specify WHICH data, WHAT processing, WHERE the result goes. |
>
> | Domain | Tech Spec variations |
> |--------|---------------------|
> | TypeScript | Function signatures, Zod schemas, middleware chains |
> | Python | Function signatures, YAML schema definitions, CLI arg parsing |
> | Infrastructure | Terraform resource specs, provider configs, module interfaces |
> | Knowledge | Page structure specs, relationship schemas, validation rules |

#### Interface Specification

> [!info] COMPLETE types, signatures, data contracts — scaffold COPIES from this
>
> | Aspect | Standard |
> |--------|---------|
> | **Sections** | Types (every export type/interface), Function Signatures (every export function), Data Contracts (every file format), Command Interfaces (input/output/side effects), Hook Interfaces (stdin/stdout/exit codes) |
> | **Quality bar** | Every type is COMPLETE — no TBD fields. Every function has full signature. Ready to copy to src/ during scaffold. |
> | **Anti-pattern** | "type Config = { /* TODO */ }" — types must be complete at design time, not filled in during scaffold. |
>
> **Why this matters:** The scaffold stage's job is to COPY types from this document into source files. If the Interface Spec is incomplete, the scaffold has to INVENT types — which means the agent is doing design during scaffold (a stage boundary violation).

#### Configuration Specification

> [!info] Every configuration surface — YAML shapes, env vars, CLI flags, defaults, precedence
>
> | Aspect | Standard |
> |--------|---------|
> | **Sections** | Config Shape (concrete YAML), Environment Variables (table: var/type/default/description), CLI Flags (table), Defaults (where each comes from), Precedence (CLI > env > config > built-in) |
> | **Quality bar** | Config shape is CONCRETE YAML, not placeholder. Every env var has a default. Precedence is explicit. |
> | **Template** | wiki/config/templates/methodology/tech-spec.md (config section) |

#### Test Plan

> [!info] WHAT will be tested, HOW, and what pass/fail looks like — BEFORE any code exists
>
> | Aspect | Standard |
> |--------|---------|
> | **Sections** | Unit Tests (table: ID/component/input/expected), Integration Tests (table: setup/steps/expected), E2E Tests, Regression Tests, Test Data requirements |
> | **Quality bar** | ≥5 unit tests defined. ≥2 integration tests. ≥1 e2e test. Every exported function has ≥1 test. Test IDs used in scaffold stubs. |
> | **Template** | wiki/config/templates/methodology/test-plan.md |
> | **Anti-pattern** | "We will test the system" — must name specific test cases with inputs and expected outputs. |
>
> **The chain dependency:** Test Plan defines test IDs → Scaffold creates test stubs matching those IDs → Test stage fills stubs with real assertions. Without the Test Plan, the scaffold creates arbitrary stubs that don't match what needs testing.

### The Artifact Chain Dependencies

> [!warning] Each document DEPENDS on prior documents — the chain is ordered
>
> ```
> Requirements Spec ──→ ADR (what problem to solve)
>         │              │
>         │              ├──→ Tech Spec (how to solve it)
>         │              │         │
>         │              │         ├──→ Interface Spec (exact types)
>         │              │         │         │
>         │              │         │         └──→ Scaffold (copies types)
>         │              │         │
>         │              │         └──→ Config Spec (exact configs)
>         │              │
>         │              └──→ Test Plan (what to verify)
>         │                        │
>         │                        └──→ Test Stubs (scaffold from plan)
>         │
> Infrastructure Analysis ──→ Gap Analysis ──→ Requirements refinement
> ```
>
> Breaking this chain means: implementing without knowing what to build (no requirements), building without knowing how (no tech spec), scaffolding without knowing the shapes (no interface spec), testing without knowing what to verify (no test plan).

### Which Artifacts Apply at Which Scale

> [!abstract] Not every task needs all 8 document/design artifacts
>
> | Artifact | Project | Epic | Module | Task | Hotfix |
> |----------|---------|------|--------|------|--------|
> | Requirements Spec | Full (BRD+FRD+SRS) | Full (FRD+AC) | Summary | Inherits | None |
> | Infrastructure Analysis | Full | Full | Targeted | Inherits | None |
> | Gap Analysis | Full | Full | Targeted | Inherits | None |
> | ADR | Multiple | 1-3 | Optional | Inherits | None |
> | Tech Spec | Full | Full | Section | Inherits | None |
> | Interface Spec | Full | Full | Section | Inherits | None |
> | Config Spec | Full | Full | Section if needed | Inherits | None |
> | Test Plan | Full | Full | Section | Inherits | None |
>
### SDLC Chain Level — What Applies Where

> [!abstract] Not all chains require all artifacts
>
> | Chain Level | What's Required | What's Optional | What's Skipped |
> |-------------|----------------|-----------------|----------------|
> | **Simplified** (POC, 2-3 stages) | Informal requirements only, NO design stage | — | ADR, tech spec, interface spec, config spec, test plan, gap analysis, infrastructure analysis |
> | **Default** (MVP-Prod, 5 stages) | Requirements spec + ADR + tech spec | Gap analysis, infrastructure analysis, test plan | Interface spec, config spec (folded into tech spec) |
> | **Full** (Production fleet, all stages) | All 8 document types required | — | — |
>
> See [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]] for chain details.

> **"Inherits"** means the task uses the epic/module's documents as its blueprints. A task doesn't write its own ADR — it follows the epic's ADR. This is why the OpenArms integration model (task_type: integration) starts at scaffold, not document — the design docs already exist at the epic level.

## Open Questions

> [!question] ~~Should the Requirements Spec template have variant modes (BRD for epics, FRD for tasks, SRS for regulated)?~~
> **RESOLVED:** One template with scale-aware guidance sections. See [[artifact-system-design-decisions|Decision — Artifact System Design Decisions]].

> [!question] ~~Should the Interface Spec be a separate document or always a section in the Tech Spec?~~
> **RESOLVED:** Section in Tech Spec by default, separate when interface exceeds 100 lines. See [[artifact-system-design-decisions|Decision — Artifact System Design Decisions]].

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Domain chains** | [[domain-chain-typescript|TypeScript Domain Chain]], [[domain-chain-python-wiki|Python-Wiki Domain Chain]], [[domain-chain-infrastructure|Infrastructure Domain Chain]], [[domain-chain-knowledge|Knowledge Domain Chain]] |
> | **Decision standards** | [[decision-page-standards|Decision Page Standards]] — ADR quality bar for the wiki |
> | **ADR template** | `wiki/config/templates/decision.md` — our decision type IS an ADR |

## Relationships

- BUILDS ON: [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
- BUILDS ON: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[decision-page-standards|Decision Page Standards]]
- RELATES TO: [[reference-page-standards|Reference Page Standards]]
- FEEDS INTO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]

## Backlinks

[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[model-methodology|Model — Methodology]]
[[decision-page-standards|Decision Page Standards]]
[[reference-page-standards|Reference Page Standards]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
[[artifact-system-design-decisions|Decision — Artifact System Design Decisions]]

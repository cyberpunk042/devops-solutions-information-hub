---
title: Artifact Chain — TypeScript-Node Domain
aliases:
  - "Artifact Chain — TypeScript-Node Domain"
  - "Artifact Chain — TypeScript/Node Domain"
  - "Artifact Chain: TypeScript-Node Domain"
  - "Artifact Chain: TypeScript/Node Domain"
type: reference
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: taxonomy
    type: wiki
    file: wiki/domains/cross-domain/methodology-artifact-taxonomy.md
  - id: openarms-profile
    type: wiki
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms as one validated example of this domain"
tags: [methodology, artifact-chain, typescript, node, domain-specific, flexible]
---

# Artifact Chain — TypeScript-Node Domain

> [!tip] AI Quick Start — Working in a TypeScript/Node Project
>
> 1. **Identify your context first** — What kind of project? (CLI tool, API backend, agent platform, frontend SPA, library). The artifact chain adapts.
> 2. **Pick your SDLC level** — Simplified (POC): 2-3 stages, minimal artifacts. Default (MVP-Production): 5 stages, standard artifacts. Full (Production fleet): all stages, full artifact chain.
> 3. **Common gates:** Type checking (`tsc` or equivalent), linting, test suite. Specific tools vary by project.
> 4. **Scaffold first, implement second** — Type definitions + test stubs before business logic. This is universal across TypeScript projects.

## Summary

Artifact chain framework for TypeScript/Node.js projects. This is NOT a single fixed pipeline — it defines the OPTIONS available at each stage, the common patterns across TypeScript projects, and how the chain adapts based on project type, SDLC level, and execution mode. Projects choose their subset based on their [[goldilocks-flow|Goldilocks identity]]. For a validated example of a full 24-artifact chain at the Default SDLC level, see [[identity-profile|OpenArms — Identity Profile]].

## Reference Content

### Common TypeScript Toolchain Options

> [!info] Toolchain varies by project — these are common options, not requirements
>
> | Concern | Options | Notes |
> |---------|---------|-------|
> | Package manager | npm, pnpm, yarn, bun | pnpm common for monorepos, bun for performance |
> | Type checking | tsc, tsgo, swc | tsgo = experimental fast checker |
> | Linting | eslint, oxlint, biome | oxlint is faster, biome combines lint+format |
> | Formatting | prettier, oxfmt, biome | Often bundled with linter |
> | Testing | vitest, jest, node:test | vitest gaining dominance, native test runner for minimal deps |
> | Runtime validation | zod, valibot, typebox | Zod most popular, valibot smaller bundle |
> | Module system | ESM, CJS | ESM preferred for new projects |
> | Build | esbuild, tsup, unbuild | Often not needed for Node.js (direct TS execution via tsx) |

### Feature Development — Generic Artifact Chain

The stages are universal. The specific artifacts at each stage depend on SDLC level and project type.

> [!abstract] Artifact Chain by Stage and SDLC Level
>
> | Stage | Simplified (POC) | Default (MVP-Prod) | Full (Production Fleet) |
> |-------|------------------|--------------------|------------------------|
> | **Document** | Informal requirements notes | Requirements spec + infrastructure analysis + gap analysis (3 docs) | + stakeholder analysis, risk register, compliance mapping |
> | **Design** | Quick ADR or none | ADR + tech spec + interface spec + config spec + test plan (5 docs) | + API contract (OpenAPI), security spec, performance spec, deployment spec |
> | **Scaffold** | Type stubs | Type definitions + validation schemas + test stubs + config wiring (4-5 artifacts) | + mock implementations, contract tests stubs, monitoring stubs |
> | **Implement** | Working code | Implementation + integration wiring + bridge modules (3-4 artifacts) | + observability instrumentation, feature flags, migration scripts |
> | **Test** | Manual verification | Unit + integration tests passing (2 gates) | + e2e tests, load tests, contract tests, security scan |
> | **Harness** | Git commit | Task frontmatter + conventional commits + completion log (3-4 artifacts) | + compliance check, deployment verification, rollback plan |

### Scaffold Stage — TypeScript Patterns

These patterns apply across TypeScript projects regardless of specific toolchain:

> [!warning] Universal Scaffold Rules
>
> **ALLOWED in scaffold:**
> - Type definitions (`type`, `interface`, `enum`)
> - Static data constants (`const X: Record<...> = {...}`)
> - Validation schemas (Zod, Valibot, etc.)
> - Stub functions that `throw new Error("not implemented")`
> - Test blocks with placeholder assertions (`expect(true).toBe(true)`)
>
> **FORBIDDEN in scaffold:**
> - Business logic (if/for/while with real conditions)
> - I/O operations (file reads, env parsing, API calls)
> - Real test assertions (testing actual behavior)
>
> **Why:** Scaffold establishes the TYPE CONTRACT. Implementation fills the logic. This separation catches design errors before implementation begins.

### Implement Stage — Integration Requirement

> [!tip] The Integration Principle
>
> Every implementation should modify at least one EXISTING file to import and use the new code. This prevents orphaned code — modules that exist but nothing calls them. The specific mechanism varies:
>
> | Project Type | How Integration Manifests |
> |-------------|-------------------------|
> | **CLI tool** | Command registry imports new command |
> | **API backend** | Router imports new handler |
> | **Agent platform** | Dispatch/execution loop calls new capability |
> | **Library** | Index/barrel file re-exports new module |
> | **Frontend** | Component tree renders new component |

### Other Models — Chain Subsets

> [!abstract] Each methodology model uses a SUBSET of the full chain
>
> | Model | What's Used | What's Skipped |
> |-------|------------|----------------|
> | **Feature Dev** | Full chain (all stages) | Nothing — this IS the full chain |
> | **Research** | Document + Design only | No code artifacts |
> | **Bug Fix** | Document (as bug analysis) + Implement + Test | No design, no scaffold |
> | **Integration** | Scaffold + Implement + Test | No document/design (uses epic's design) |
> | **Hotfix** | Implement + Test only | Everything else — problem and solution known |
> | **Refactor** | Document (current→target map) + Scaffold + Implement + Test | No design docs |
> | **Documentation** | Document only (wiki page) | No code |

### Ecosystem Examples

> [!example] Validated Implementations
>
> | Project | SDLC Level | Artifacts | Details |
> |---------|-----------|-----------|---------|
> | **OpenArms** | Default | 24-artifact chain | [[identity-profile\|OpenArms — Identity Profile]] — 93 tasks, 9 methodology versions, harness v2 |
> | **OpenFleet** | Full | Estimated 40+ (orchestrator + 10 agents) | Multi-agent dispatch adds contribution gating, tier-based context, standing orders |
>
> These are EXAMPLES at specific SDLC levels. Your project will have its own artifact count based on its identity.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **Full artifact taxonomy** | [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]] (78 types across 11 categories) |
> | **Generic chains by model** | [[artifact-chains-by-model|Artifact Chains by Methodology Model]] |
> | **SDLC levels** | [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
- BUILDS ON: [[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
- BUILDS ON: [[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]]
- RELATES TO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
[[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[model-methodology|Model — Methodology]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
[[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]
[[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
[[universal-stages-domain-specific-artifacts|Universal Stages, Domain-Specific Artifacts]]

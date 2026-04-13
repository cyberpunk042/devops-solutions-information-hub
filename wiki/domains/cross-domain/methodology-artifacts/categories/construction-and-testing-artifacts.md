---
title: Construction and Testing Artifacts — Standards and Guide
aliases:
  - "Construction and Testing Artifacts — Standards and Guide"
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
  - id: nxcode-agentic
    type: article
    url: https://www.nxcode.io/resources/news/agentic-engineering-complete-guide-vibe-coding-ai-agents-2026
tags: [methodology, construction, testing, artifacts, scaffold, implement, test, domain-specific, standards]
---

# Construction and Testing Artifacts — Standards and Guide

> [!tip] AI Quick Start — You're in Scaffold, Implement, or Test Stage
>
> 1. **These stages are DOMAIN-SPECIFIC** — what you produce depends entirely on your tech stack
> 2. **Check your domain chain page** for concrete file paths, gate commands, and ALLOWED/FORBIDDEN code examples
> 3. **Scaffold rule:** ZERO behavior. Types, schemas, stubs only. Function bodies ≤ 3 lines.
> 4. **Implement rule:** MUST wire into existing runtime. Code nobody imports is orphaned (Bug 6: 2,073 lines).
> 5. **Test rule:** ZERO failures. Replace ALL placeholders with real assertions. Run the gate command.

## Summary

Guide to the artifacts produced during the Scaffold, Implement, and Test stages — the stages where THINGS GET BUILT AND VERIFIED. Unlike requirements and design artifacts (which are domain-agnostic documents), construction and testing artifacts are HIGHLY DOMAIN-SPECIFIC. A TypeScript project scaffolds .ts type files; a Python project scaffolds .yaml configs; an infrastructure project scaffolds .tf variable definitions. This page defines the universal patterns that apply across all domains, then specifies the per-domain variations.

## Key Insights

1. **Construction/testing artifacts are where domain profiles matter most.** Document and Design stage artifacts are 95% domain-agnostic (same template everywhere). Scaffold, Implement, and Test artifacts change COMPLETELY based on the technology stack. This is why the artifact system needs two layers: universal (documents) and domain-specific (code/config/infra).

2. **Scaffold = structure without behavior. Implement = behavior wired into runtime. Test = proof.** This three-stage separation is the core of the stage-gate system. The boundaries are HARD: scaffold CANNOT contain business logic (OpenArms Bug 5: 135 lines of logic in scaffold). Implement MUST wire into existing runtime (OpenArms Bug 6: 2,073 lines nobody imported). Test MUST show 0 failures.

3. **The bridge/adapter pattern is universal across domains.** OpenArms discovered this during integration sprints — a thin adapter between new module and existing consumer keeps diffs small and modules testable. This pattern applies to ANY domain: Python wrapper functions, Terraform module interfaces, wiki relationship wiring.

4. **"Code exists" ≠ "code works."** The integration wiring artifact is the proof that new code is CONNECTED to the runtime. Without it, the code is orphaned — it compiles, tests pass in isolation, but nothing in production uses it. This is the most common implementation failure.

## Deep Analysis

### The Universal Pattern (all domains)

> [!abstract] Stage → What You Produce → What's FORBIDDEN → Gate
>
> | Stage | Produce | Forbidden | Gate |
> |-------|---------|-----------|------|
> | **Scaffold** | Structure: types, schemas, stubs, config wiring — ZERO behavior | Business logic, real implementations, real test assertions | Structure compiles/validates, no behavior in diff |
> | **Implement** | Behavior: logic filling stubs, wired into existing runtime | Test modifications, orphaned code nobody imports | Compiles, lints, ≥1 existing file imports new code |
> | **Test** | Proof: real assertions replacing placeholders, 0 failures | New features, scope changes | All tests pass, no placeholder assertions remaining |

### SDLC Chain Level — What Applies Where

> [!abstract] Not all chains require all artifacts
>
> | Chain Level | What's Required | What's Optional | What's Skipped |
> |-------------|----------------|-----------------|----------------|
> | **Simplified** (POC, 2-3 stages) | Implement + manual test | — | Scaffold stage entirely, automated tests, bridge/adapter |
> | **Default** (MVP-Prod, 5 stages) | Scaffold + implement + automated tests | Bridge/adapter pattern, coverage evidence | E2E tests, compliance validation |
> | **Full** (Production fleet, all stages) | Scaffold + implement + unit + integration + e2e + compliance | — | — |
>
> See [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]] for chain details.

### Scaffold Stage Artifacts — Per Domain

> [!info] Structure without behavior — the skeleton

#### TypeScript Domain (OpenArms, OpenFleet)

| Artifact | File Pattern | Content | Gate |
|----------|-------------|---------|------|
| Type Definitions | `src/**/*.ts` | `export type`, `export interface`, `export const` for static data | `pnpm tsgo` passes |
| Zod Schemas | `src/**/*.schema.ts` | `z.object()` definitions matching type interfaces | Schemas match types |
| Test Stubs | `src/**/*.test.ts` | `describe`/`it` blocks with `expect(true).toBe(true)` | ≥3 it() blocks, 0 real assertions |
| Config Wiring | existing config types | Optional field added to parent config | `import type` only |
| Env Example | `.env.example` | New env var entries matching Config Spec | Entries match spec |

> [!warning] FORBIDDEN in TypeScript scaffold
> - Function bodies with `if`/`for`/`while`/`switch`/`try`
> - Function bodies longer than 3 lines (stub only: `throw new Error("not implemented")`)
> - `z.transform()` with logic
> - Real test assertions (anything beyond `toBe(true)` or `toBeDefined()`)

#### Python/Wiki Domain (Research Wiki)

| Artifact | File Pattern | Content | Gate |
|----------|-------------|---------|------|
| Config Schemas | `config/**/*.yaml` | YAML structure definitions, enum values, required fields | YAML parses without errors |
| Template Files | `wiki/config/templates/**/*.md` | Frontmatter defaults, section headings, inline guidance | Template variables resolve |
| Tool Stubs | `tools/**/*.py` | Function signatures with `pass` or `raise NotImplementedError` | `python -c "import tools.X"` succeeds |
| Schema Updates | `wiki/config/wiki-schema.yaml` | New types, sections, enums | `pipeline post` passes |

> [!warning] FORBIDDEN in Python/Wiki scaffold
> - Business logic in tool files (parsing, validation, transformation)
> - Real content in template files (just structure and guidance comments)
> - Modifying existing tool behavior

#### Infrastructure Domain (devops-control-plane)

| Artifact | File Pattern | Content | Gate |
|----------|-------------|---------|------|
| Variable Definitions | `**/*.tf` | `variable` blocks with type, description, default | `terraform validate` passes |
| Output Definitions | `**/*.tf` | `output` blocks with value and description | `terraform validate` passes |
| Module Interface | `modules/**/variables.tf` | Input variables defining the module contract | Module structure valid |
| Backend Config | `backend.tf` | State storage configuration | `terraform init` succeeds |

> [!warning] FORBIDDEN in Infrastructure scaffold
> - `resource` blocks (actual infrastructure)
> - `data` sources that query real infrastructure
> - `provisioner` blocks

#### Knowledge Domain

> [!info] Knowledge Scaffold Artifacts
>
> | Artifact | Content | Gate |
> |----------|---------|------|
> | **Page template** | Frontmatter + section structure from `wiki/config/templates/{type}.md` | Scaffolder creates valid structure |
> | **Schema update** | New type/field in `wiki/config/wiki-schema.yaml` | YAML parses, pipeline post passes |
> | **Config update** | New entries in methodology.yaml or artifact-types.yaml | Config loads without errors |

> [!warning] FORBIDDEN in Knowledge scaffold
> - Real content in wiki pages (just frontmatter and section headings)
> - Business logic in tool files (parsing, validation, transformation)
> - Modifying existing tool behavior

### Implement Stage Artifacts — Per Domain

> [!info] Behavior filling the scaffold — MUST wire into existing runtime

#### TypeScript Domain

| Artifact | Content | Gate |
|----------|---------|------|
| Implementation Files | Business logic: parsers, resolvers, evaluators, env readers | `pnpm tsgo` + `pnpm check` |
| Bridge/Adapter Module | Thin adapter (<80 LOC) between new module and existing consumer | < 80 LOC, adapter only |
| Integration Wiring | EXISTING file modified with `import` + call site | Diff shows added import, file preexisted |

#### Python/Wiki Domain

| Artifact | Content | Gate |
|----------|---------|------|
| Tool Implementation | Python functions with real logic (validation, transformation, generation) | `pipeline post` passes |
| Wiki Pages | Content pages filling template structure with real knowledge | Validation 0 errors |
| Pipeline Integration | Existing pipeline.py modified to call new tool | Import added to existing file |

#### Infrastructure Domain

| Artifact | Content | Gate |
|----------|---------|------|
| Resource Definitions | `resource` blocks creating actual infrastructure | `terraform plan` succeeds |
| Module Implementation | Real module logic with resource + data + local blocks | `terraform validate` |
| Environment Wiring | Existing environment configs reference new modules | `terraform plan` shows expected changes |

#### Knowledge Domain

> [!info] Knowledge Implement Artifacts
>
> | Artifact | Content | Gate |
> |----------|---------|------|
> | **Wiki page content** | Real content filling every section, ≥30 word summary | Pipeline post 0 errors |
> | **Tool logic** | Python functions with real processing logic | Import succeeds, function runs |
> | **Pipeline integration** | New command/chain wired into pipeline.py | Command callable from CLI |
> | **Relationships** | Forward relationships to related pages | ≥1 relationship, backlinks generated |

> [!warning] The Integration Requirement — Universal Across All Domains
>
> Implement is NOT done until at least one EXISTING file imports/references the new code. This is the lesson from OpenArms Bug 6 (2,073 orphaned lines). For each domain:
>
> | Domain | "Integration wiring" means |
> |--------|--------------------------|
> | TypeScript | Existing .ts file has new `import { X } from "./new-module"` |
> | Python | Existing .py file has new `from tools.new_module import X` |
> | Infrastructure | Existing .tf file has new `module "X" { source = "./modules/new" }` |
> | Wiki | Existing wiki page has new `- RELATES TO: `[[New Page]]`` |

### Test Stage Artifacts — Per Domain

> [!info] Proof that the system works — replace placeholders, 0 failures

#### Universal Pattern

| Artifact | Content | Gate |
|----------|---------|------|
| Test Implementations | Real assertions replacing every placeholder | 0 placeholder assertions remaining |
| Test Results | Gate command output showing pass count + 0 failures | Exit code 0 |
| Coverage Evidence | Which functions/paths are tested (optional but encouraged) | ≥1 test per exported function |

#### Per-Domain Gate Commands

| Domain | Gate Command | What It Proves |
|--------|-------------|---------------|
| TypeScript | `pnpm test -- path/to/test.ts` | vitest passes with 0 failures |
| Python/Wiki | `python3 -m tools.pipeline post` | Full 6-step validation chain passes |
| Infrastructure | `terraform plan` + `terraform apply` (staging) | Infrastructure creates without errors |
| Knowledge | `python3 -m tools.validate` + `python3 -m tools.lint` | Page quality gates pass |

### The Bridge/Adapter Pattern

> [!tip] Universal pattern for clean integration across all domains
>
> ```
> New Module (clean interface)
>     ↓
> Bridge/Adapter (thin wrapper, <80 LOC)
>     ↓
> Existing Consumer (minimal edit — one import line)
> ```
>
> **Why:** Keeps new module testable independently. Keeps existing consumer's diff small. Adapter handles interface mismatches. If the new module's interface changes, only the bridge changes — not the consumer.
>
> | Domain | Bridge looks like |
> |--------|------------------|
> | TypeScript | `src/{location}/{slug}-bridge.ts` — imports from new, exports shaped for consumer |
> | Python | `tools/{slug}_adapter.py` — wraps new function with consumer-compatible signature |
> | Infrastructure | `modules/{slug}/main.tf` — wraps resources with clean variable interface |
> | Wiki | N/A (wiki pages connect via relationships, not code imports) |

## Open Questions

> [!question] ~~Should the bridge pattern be REQUIRED for integration tasks or RECOMMENDED?~~
> **RESOLVED:** Recommended, not required. Required when interface mismatch detected. See [[artifact-system-design-decisions|Decision — Artifact System Design Decisions]].

> [!question] ~~Should there be a "Scaffold Checklist" that agents run BEFORE calling /stage-complete?~~
> **RESOLVED:** Yes — advisory self-check before gate. Blocking when harness exists. See [[artifact-system-design-decisions|Decision — Artifact System Design Decisions]].

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **TypeScript chain** | [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]] — concrete file paths and gates |
> | **Python/Wiki chain** | [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]] — wiki-specific scaffold/implement |
> | **Infrastructure chain** | [[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]] — Terraform scaffold/implement |
> | **Knowledge chain** | [[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]] — knowledge artifact lifecycle |
> | **Enforcement hooks** | [[enforcement-hook-patterns|Enforcement Hook Patterns]] — how stage boundaries are enforced |

## Relationships

- BUILDS ON: [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
- BUILDS ON: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[enforcement-hook-patterns|Enforcement Hook Patterns]]
- FEEDS INTO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]

## Backlinks

[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[model-methodology|Model — Methodology]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
[[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
[[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
[[artifact-system-design-decisions|Decision — Artifact System Design Decisions]]
[[three-classes-of-methodology-output|Three Classes of Methodology Output]]

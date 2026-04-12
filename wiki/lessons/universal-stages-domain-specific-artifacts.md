---
title: "Universal Stages, Domain-Specific Artifacts"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: seed
derived_from:
  - "Methodology Artifact Taxonomy"
  - "Artifact Chain: TypeScript/Node Domain"
  - "Artifact Chain: Python/Wiki Domain"
  - "Artifact Chain: Infrastructure/IaC Domain"
  - "Artifact Chain: Knowledge/Evolution Domain"
created: 2026-04-12
updated: 2026-04-12
sources: []
tags: [methodology, domain-specific, universal, stages, artifacts, lesson]
---

# Universal Stages, Domain-Specific Artifacts

## Summary

The methodology's stage sequence (Document → Design → Scaffold → Implement → Test) is universal across all domains. But the ARTIFACTS produced at each stage change completely based on the technology domain. Document and Design stages are 95% domain-agnostic — a Requirements Spec and an ADR look the same whether the project is TypeScript, Python, Terraform, or knowledge work. Scaffold, Implement, and Test stages are 95% domain-specific — a TypeScript scaffold produces .ts type files while an infrastructure scaffold produces .tf variable definitions. This split is the key to building a portable methodology that works across the entire ecosystem.

## Context

This lesson applies when:
- Designing a methodology system that must work across multiple technology domains
- Creating domain profiles for different project types
- Deciding which templates and quality standards are shared vs per-domain
- An agent encounters a methodology model and needs to know which artifacts to produce for ITS domain
- Building portable methodology configs (like methodology.yaml) that projects adopt

## Insight

> [!tip] The Two-Layer Architecture
>
> | Layer | Stages | Domain Dependence | Reuse |
> |-------|--------|------------------|-------|
> | **Universal** (documents) | Document, Design | 5% domain-specific | Same templates, same quality bars across ALL projects |
> | **Domain-specific** (code/config/infra) | Scaffold, Implement, Test | 95% domain-specific | Different file types, gate commands, and ALLOWED/FORBIDDEN per domain |
>
> This means: ONE set of templates for requirements specs, ADRs, tech specs, test plans (the document/design layer). FOUR sets of scaffold/implement/test guidance (TypeScript, Python/Wiki, Infrastructure, Knowledge).

> [!abstract] Same Stage, Different Artifacts
>
> | Stage | TypeScript | Python/Wiki | Infrastructure | Knowledge |
> |-------|-----------|-------------|---------------|-----------|
> | **Document** | Wiki page with gaps | Wiki page with gaps | Wiki page with gaps | Wiki page with gaps |
> | **Design** | ADR + TS types in doc | ADR + YAML shapes in doc | ADR + TF specs in doc | ADR + page structure in doc |
> | **Scaffold** | `.ts` exports, `.test.ts` stubs | `.yaml` configs, `.py` stubs | `.tf` variables, module interfaces | Template files, schema updates |
> | **Implement** | `.ts` business logic, bridge modules | `.py` tool code, wiki content | `.tf` resources, module impl | Wiki pages with real content |
> | **Test** | `pnpm test -- file.ts` | `pipeline post` | `terraform plan/apply` | `pipeline post + validate` |
>
> The STAGE NAMES are identical. The STAGE PURPOSES are identical. The ARTIFACTS are completely different.

## Evidence

> [!success] Validated: 4 Domain Chain Pages Show the Same Pattern
> When documenting the per-domain artifact chains (TypeScript, Python/Wiki, Infrastructure, Knowledge), the same split emerged independently in each domain. The document/design rows were nearly identical across all 4 chains. The scaffold/implement/test rows were completely different. This wasn't designed — it was discovered by mapping real artifacts.

> [!success] Evidence from OpenArms → Research Wiki Transfer
> OpenArms's methodology.yaml was built for TypeScript. When the research wiki adopted it, the document/design stages worked unchanged (same stage definitions, same quality gates). But the scaffold/implement/test stages needed complete replacement: `pnpm tsgo` → `pipeline post`, `src/**/*.ts` → `config/**/*.yaml`, vitest assertions → pipeline validation. The universal layer transferred; the domain layer didn't.

> [!bug]- Failure: Hardcoded Domain-Specific Content in "Generic" Config
> The first attempt at a "portable" methodology.yaml still contained TypeScript-specific artifact types (type_definition, zod_schema, test_stub with vitest patterns). This was called "hardcoded" by the operator. The fix: separate the universal stage definitions from the domain-specific artifact types. Universal definitions go in methodology.yaml. Domain-specific resolutions go in domain-profiles/.

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Ecosystem-wide methodology** | Define stages and models ONCE (universal). Define artifact types and gates PER DOMAIN (domain profiles). |
| **New project adoption** | Copy the universal layer (methodology.yaml models + document/design templates). Create or select a domain profile for the scaffold/implement/test layer. |
| **Template design** | Document/design templates: ONE set shared across all projects. Scaffold/implement/test guidance: separate per domain. |
| **Validation tooling** | Gate commands are domain-specific (pnpm tsgo vs pipeline post vs terraform validate). The CONCEPT of a gate is universal. |

> [!tip] When This Lesson Does NOT Apply
>
> Projects that operate in a single domain and will never share methodology across domains don't need the two-layer split. A TypeScript-only team can hardcode everything. The split matters when methodology must be PORTABLE — shared across the research wiki, OpenArms, OpenFleet, AICP, and devops-control-plane, each with different technology stacks.

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself BEFORE defining artifacts or building methodology configs:
>
> 1. **Am I putting domain-specific content in the universal layer?** If my methodology.yaml mentions `pnpm tsgo` or `.ts` files, it's not portable. Domain specifics go in domain-profiles ONLY.
> 2. **Am I reinventing document/design templates per domain?** Requirements Specs and ADRs look the same everywhere. Don't create TypeScript-flavored requirements templates — use the universal one.
> 3. **Did I check the domain chain page for MY domain?** The scaffold/implement/test artifacts are COMPLETELY different per domain. Don't guess — read the chain page.
> 4. **Am I hardcoding when I should be configuring?** If the same artifact works for 3 domains with different paths, it should be a generic artifact + domain profile override, not 3 separate artifact definitions.

## Relationships

- DERIVED FROM: [[Methodology Artifact Taxonomy]]
- DERIVED FROM: [[Artifact Chain: TypeScript/Node Domain]]
- DERIVED FROM: [[Artifact Chain: Python/Wiki Domain]]
- DERIVED FROM: [[Artifact Chain: Infrastructure/IaC Domain]]
- DERIVED FROM: [[Artifact Chain: Knowledge/Evolution Domain]]
- RELATES TO: [[Stage-Gate Methodology]]
- RELATES TO: [[Model: Methodology]]
- FEEDS INTO: [[Methodology Adoption Guide]]
- FEEDS INTO: [[Model: Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Methodology Artifact Taxonomy]]
[[Artifact Chain: TypeScript/Node Domain]]
[[Artifact Chain: Python/Wiki Domain]]
[[Artifact Chain: Infrastructure/IaC Domain]]
[[Artifact Chain: Knowledge/Evolution Domain]]
[[Stage-Gate Methodology]]
[[Model: Methodology]]
[[Methodology Adoption Guide]]
[[Model: Methodology Standards — What Good Execution Looks Like]]

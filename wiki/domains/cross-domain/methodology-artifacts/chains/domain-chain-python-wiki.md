---
title: Artifact Chain — Python-Wiki Domain
aliases:
  - "Artifact Chain — Python-Wiki Domain"
  - "Artifact Chain — Python/Wiki Domain"
  - "Artifact Chain: Python-Wiki Domain"
  - "Artifact Chain: Python/Wiki Domain"
type: reference
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
  - id: wiki-pipeline
    type: file
    file: tools/pipeline.py
  - id: wiki-validate
    type: file
    file: tools/validate.py
tags: [methodology, artifact-chain, python, wiki, domain-specific, flexible]
---

# Artifact Chain — Python-Wiki Domain

> [!tip] AI Quick Start — Working in a Python Tool or Knowledge Wiki Project
>
> 1. **Identify your context** — Python CLI tool? Data pipeline? Knowledge wiki? API backend? Each has different artifacts.
> 2. **Pick your SDLC level** — Simplified: informal docs + working code. Default: stage-gated with validation. Full: comprehensive with compliance.
> 3. **Common gates:** `python -m pytest`, type checking (mypy/pyright optional), linting (ruff/flake8), project-specific validation.
> 4. **Wiki projects** have a unique artifact: the wiki PAGE is both a deliverable and a validation target.

## Summary

Artifact chain framework for Python-based tool projects and knowledge wikis. Python projects span a wide range: CLI tools, data pipelines, web APIs, automation scripts, and knowledge systems. Knowledge wikis add a unique dimension where CONTENT is a first-class artifact alongside code. This chain shows the options at each stage and how they adapt to project type and SDLC level. For a validated example of a 20-artifact wiki chain, see [[identity-profile|Research Wiki — Identity Profile]].

## Reference Content

### Common Python Toolchain Options

> [!info] Toolchain varies by project — these are options, not requirements
>
> | Concern | Options | Notes |
> |---------|---------|-------|
> | Package manager | pip, uv, poetry, pdm | uv gaining fast adoption |
> | Virtual env | venv, uv venv, conda | venv is standard, uv is faster |
> | Type checking | mypy, pyright, pytype | Optional but recommended for larger projects |
> | Linting | ruff, flake8, pylint | ruff is fastest, replaces multiple tools |
> | Formatting | ruff format, black, autopep8 | ruff format replacing black |
> | Testing | pytest, unittest, nose2 | pytest dominant |
> | Validation (wiki) | Custom (schema YAML + pipeline) | Project-specific quality gates |
> | Config | YAML, TOML, JSON, .env | YAML common for structured config |

### Feature Development — Generic Artifact Chain

> [!abstract] Artifact Chain by Stage and SDLC Level
>
> | Stage | Simplified (POC) | Default (MVP-Prod) | Full (Production) |
> |-------|------------------|--------------------|-------------------|
> | **Document** | Informal notes | Requirements spec + infrastructure analysis + gap analysis | + compliance mapping, stakeholder analysis |
> | **Design** | Quick decision notes | ADR + tech spec + schema spec + test plan | + API spec (OpenAPI), data model spec, migration plan |
> | **Scaffold** | Empty modules | Config schemas (YAML) + templates + tool stubs + schema updates | + mock data generators, contract stubs |
> | **Implement** | Working code | Tool logic + content pages + pipeline integration | + observability, feature flags, data migrations |
> | **Test** | Manual run | pytest + validation pipeline + lint | + integration tests, performance tests, compliance checks |
> | **Harness** | Git commit | Task frontmatter + session log | + compliance report, deployment verification |

### Scaffold Stage — Python Patterns

> [!warning] Universal Python Scaffold Rules
>
> **ALLOWED in scaffold:**
> - Config schemas (YAML structure definitions)
> - Type stubs and dataclass definitions
> - Template files with variables (`{{title}}`)
> - Function stubs that `raise NotImplementedError("scaffold only")`
> - Empty test files with `pass` or `pytest.skip()`
>
> **FORBIDDEN in scaffold:**
> - Business logic (real if/for/while with data processing)
> - I/O operations (file reads, API calls, database queries)
> - Real test assertions
>
> **Why:** Same principle as TypeScript — establish the CONTRACT (schemas, types, interfaces) before filling logic.

### Wiki-Specific Artifacts

Knowledge wiki projects have unique artifacts that don't exist in pure code projects:

> [!info] Wiki Artifact Types
>
> | Artifact | Stage | What It Is | Gate |
> |----------|-------|-----------|------|
> | **Wiki page** | implement | Markdown with YAML frontmatter, required sections | Schema validation + lint |
> | **YAML config** | scaffold | Schema definitions, methodology engine, domain profiles | YAML parses, pipeline uses it |
> | **Templates** | scaffold | Structural skeletons for page types | Variables resolve, sections match schema |
> | **Pipeline chain** | implement | Orchestrated validation + generation steps | Pipeline runs end-to-end, 0 errors |
> | **Domain index** | implement (auto) | Auto-generated table of domain pages | Rebuilt by pipeline post |
> | **Manifest** | implement (auto) | JSON index of all pages + metadata | Rebuilt by pipeline post |

### Other Models — Chain Subsets

> [!abstract] Each methodology model uses a SUBSET
>
> | Model | Document | Design | Scaffold | Implement | Test |
> |-------|----------|--------|----------|-----------|------|
> | **Feature Dev** | Req + infra + gaps | ADR + specs | Config + templates + stubs | Tool logic + wiki pages + integration | Full validation |
> | **Research** | Wiki research pages | Findings | — | — | — |
> | **Knowledge Evolution** | Source inventory | — | — | Evolved wiki page | Pipeline validation |
> | **Documentation** | Wiki page | — | — | — | Pipeline validation |
> | **Bug Fix** | Bug analysis | — | — | Tool fix | Validation + regression |
> | **Refactor** | Current→target map | — | New config schema | Restructured code/config | Full validation |

### Ecosystem Examples

> [!example] Validated Implementations
>
> | Project | SDLC Level | Artifacts | Details |
> |---------|-----------|-----------|---------|
> | **Research Wiki** | Default | 20-artifact chain | [[identity-profile|Research Wiki — Identity Profile]] — 300 pages, Python tooling, self-referential |
> | **AICP** | Simplified | ~10 artifacts (estimated) | Python backend, 78 skills, lighter process |

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
- RELATES TO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
- RELATES TO: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[model-methodology|Model — Methodology]]
[[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
[[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]
[[identity-profile|Research Wiki — Identity Profile]]
[[universal-stages-domain-specific-artifacts|Universal Stages, Domain-Specific Artifacts]]

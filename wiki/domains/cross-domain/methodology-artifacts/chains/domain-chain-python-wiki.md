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
maturity: seed
created: 2026-04-12
updated: 2026-04-12
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
tags: [methodology, artifact-chain, python, wiki, domain-specific, research-wiki]
---

# Artifact Chain — Python-Wiki Domain
> [!tip] AI Quick Start — Working in the Research Wiki or a Python Tool Project
>
> 1. **Gate command for EVERYTHING:** `python3 -m tools.pipeline post` — run it after every change, 0 errors = pass
> 2. **Scaffold:** `wiki/config/*.yaml` schemas + `wiki/config/templates/*.md` templates. YAML declarations only, no Python logic.
> 3. **Implement:** `tools/*.py` with real logic + wiki pages with real content + pipeline.py modified to call new tools
> 4. **Test:** `pipeline post` 0 errors + `tools/validate` 0 errors + new lint issues should not increase
> 5. **Knowledge operations below:** ingestion (raw→synthesis), evolution (synthesis→lesson/pattern/decision), curation (domain overviews)

## Summary

Complete artifact chain resolution for Python tool projects and knowledge wikis (the research wiki itself). Maps every methodology model's stages to concrete Python/wiki artifacts — file paths, validation commands, and real examples from this wiki's own development. The document/design stages use universal artifacts (same as all domains). The scaffold stage produces YAML configs and markdown templates. The implement stage produces Python tool code and wiki content pages. The test stage uses `pipeline post` as the universal gate.

## Reference Content

### Toolchain

> [!info] Python/Wiki Domain Stack
>
> | Tool | Purpose | Gate Command |
> |------|---------|-------------|
> | Python 3.11+ (.venv) | Runtime | `.venv/bin/python` |
> | PyYAML | Config parsing | Part of pipeline |
> | tools/pipeline.py | Orchestration (13 chains) | `python3 -m tools.pipeline post` |
> | tools/validate.py | Schema + artifact-type validation | `python3 -m tools.validate` |
> | tools/lint.py | Health checks | `python3 -m tools.lint` |
> | Obsidian | Vault rendering | Manual verification |

### Feature Development — Python/Wiki Chain

> [!abstract] Full Chain — Document through Test
>
> | # | Stage | Artifact | File Pattern | Gate |
> |---|-------|----------|-------------|------|
> | 1 | document | Requirements Spec | `wiki/domains/{domain}/{slug}-requirements.md` | FR items with Input/Output/Constraint |
> | 2 | document | Infrastructure Analysis | `wiki/domains/{domain}/{slug}-infrastructure.md` | Page references verified |
> | 3 | document | Gap Analysis | `wiki/domains/{domain}/{slug}-gaps.md` | Gaps reference existing pages/tools |
> | 4 | design | ADR | `wiki/decisions/{slug}.md` | ≥1 alternative with rejection reason |
> | 5 | design | Tech Spec | `wiki/domains/{domain}/{slug}-tech-spec.md` | Functions/operations defined |
> | 6 | design | Schema Spec | `wiki/domains/{domain}/{slug}-schema-spec.md` | YAML shapes concrete, not placeholder |
> | 7 | design | Test Plan | `wiki/domains/{domain}/{slug}-test-plan.md` | Validation scenarios defined |
> | 8 | scaffold | Config Schema | `config/{name}.yaml` | YAML parses, structure matches spec |
> | 9 | scaffold | Templates | `wiki/config/templates/{type}.md` | Variables resolve, sections match schema |
> | 10 | scaffold | Schema Update | `wiki/config/wiki-schema.yaml` | New types/sections added, pipeline post passes |
> | 11 | scaffold | Tool Stub | `tools/{name}.py` | `python -c "import tools.{name}"` succeeds |
> | 12 | implement | Tool Logic | `tools/{name}.py` | Functions with real logic, `pipeline post` passes |
> | 13 | implement | Wiki Pages | `wiki/{domain}/{slug}.md` | Valid frontmatter, required sections, ≥30 word summary |
> | 14 | implement | Pipeline Integration | `tools/pipeline.py` modified | New command/chain wired in |
> | 15 | test | Pipeline Post | gate output | `python3 -m tools.pipeline post` → 0 errors |
> | 16 | test | Validation | gate output | `python3 -m tools.validate` → 0 errors |
> | 17 | test | Lint | gate output | `python3 -m tools.lint` → advisory only |
> | 18 | harness | Task Frontmatter | epic/task .md file | stages_completed updated |
> | 19 | harness | Git Commits | git log | One per stage |
> | 20 | harness | Completion Log | `raw/notes/` or `wiki/log/` | Session recorded |

### Scaffold Stage — Python/Wiki Specifics

> [!warning] What's ALLOWED vs FORBIDDEN
>
> **ALLOWED:**
> ```yaml
> # Config schema (wiki/config/artifact-types.yaml)
> types:
>   concept:
>     category: knowledge-pages
>     template: wiki/config/templates/concept.md
>     content_thresholds:
>       summary_min_words: 30
> ```
>
> ```markdown
> <!-- Template file (wiki/config/templates/concept.md) -->
> ---
> title: "{{title}}"
> type: concept
> ---
> # {{title}}
> ## Summary
> <!-- 2-3 sentences: what this concept IS -->
> ```
>
> ```python
> # Tool stub (tools/new_tool.py)
> def process_something(input_path: Path) -> Dict[str, Any]:
>     raise NotImplementedError("scaffold only")
> ```
>
> **FORBIDDEN:**
> ```python
> # Business logic in scaffold
> def process_something(input_path: Path) -> Dict[str, Any]:
>     text = input_path.read_text()     # ← FORBIDDEN
>     meta = yaml.safe_load(text)       # ← FORBIDDEN
>     return {"title": meta["title"]}   # ← FORBIDDEN
> ```

### Implement Stage — Python/Wiki Specifics

> [!tip] Integration Requirement for Python/Wiki
>
> **For tool code:** At least one EXISTING tool (pipeline.py, validate.py, lint.py) must import and call the new function.
>
> **For wiki pages:** At least one EXISTING wiki page must have a relationship pointing to the new page (wired by `pipeline post` backlink generation, but the forward relationship must be added manually).
>
> **For config changes:** The validation tool must be updated to read the new config (or it's invisible to the system).

### Real Examples from This Wiki

> [!example]- E003: Artifact Type System (Feature Dev, 5 stages)
>
> **Document:** Requirements spec, infrastructure analysis, gap analysis — all as wiki pages in wiki/domains/cross-domain/
>
> **Design:** Design document with 7 decisions — as wiki page
>
> **Scaffold:**
> - `wiki/config/artifact-types.yaml` — 17 types defined (config schema)
> - `wiki/config/templates/*.md` — 16 wiki templates + 6 methodology templates
> - `wiki/config/wiki-schema.yaml` — operations-plan type added
> - `tools/pipeline.py` — scaffolder updated for new types (stub integration)
>
> **Implement:**
> - `wiki/config/methodology.yaml` — 9 models with artifact chains
> - `wiki/config/domain-profiles/*.yaml` — 3 domain profiles
> - `tools/validate.py` — reads artifact-types.yaml for per-type thresholds
> - `wiki/domains/cross-domain/artifact-chains-by-model.md` — documentation page
>
> **Test:**
> - `python3 -m tools.pipeline post` → 0 validation errors
> - All templates scaffold correctly
> - Validation catches type-specific thresholds

> [!example]- Knowledge Evolution: Lesson from 3 Sources (Evolve, 2 stages)
>
> **Document:** Source inventory identifying 3 convergent pages
>
> **Implement:** 122-line lesson page "CLI Tools Beat MCP for Token Efficiency" with 8 evidence items from 4 sources, CONTRADICTS relationship, When MCP Is Still Right counterexamples
>
> **Gate:** `pipeline post` → 0 errors, derived_from references valid pages

### Other Models — Python/Wiki Subsets

> [!abstract] Model → Artifacts
>
> | Model | Document Stage | Design Stage | Scaffold Stage | Implement Stage | Test Stage |
> |-------|---------------|-------------|---------------|----------------|-----------|
> | **Feature Dev** | Req spec + infra + gaps | ADR + tech spec + schema spec + test plan | Config YAML + templates + schema update + tool stub | Tool logic + wiki pages + pipeline integration | pipeline post + validate |
> | **Research** | Research wiki pages | Findings + recommendation | — | — | — |
> | **Knowledge Evolution** | Source inventory | — | — | Evolved wiki page | pipeline post |
> | **Documentation** | Wiki page | — | — | — | pipeline post |
> | **Bug Fix** | Bug analysis | — | — | Tool fix + pipeline fix | pipeline post |
> | **Refactor** | Current→target map | — | New config schema | Restructured tools/config | pipeline post |

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
- BUILDS ON: [[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
- RELATES TO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[model-methodology|Model — Methodology]]
[[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
[[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]
[[universal-stages-domain-specific-artifacts|Universal Stages, Domain-Specific Artifacts]]

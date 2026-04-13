---
title: "Artifact Chain: Knowledge/Evolution Domain"
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
  - id: wiki-evolve
    type: file
    file: tools/evolve.py
  - id: zettelkasten
    type: article
    url: "https://zettelkasten.de/posts/building-a-second-brain-and-zettelkasten/"
tags: [methodology, artifact-chain, knowledge, evolution, wiki, domain-specific, second-brain]
---

# Artifact Chain: Knowledge/Evolution Domain

> [!tip] AI Quick Start — Working on Wiki Knowledge (Ingestion, Evolution, Curation)
>
> 1. **Ingesting a source?** Fetch → read FULL file → synthesize (≥25% ratio to raw) → `pipeline post` → cross-reference
> 2. **Evolving a lesson/pattern/decision?** Find ≥2 convergent pages → write evolved page with evidence → `pipeline post`
> 3. **Scaffold in this domain** = `pipeline scaffold <type> "Title"` — creates frontmatter + section headings
> 4. **Implement in this domain** = write real content in every section, meeting per-type quality bar
> 5. **Progressive distillation layers:** L0 raw → L1 synthesis → L2 concept → L3 comparison → L4 lesson → L5 pattern → L6 decision

## Summary

Artifact chain resolution for knowledge work — source ingestion, synthesis, evolution, and domain curation. This domain is UNIQUE because the artifacts are THEMSELVES wiki pages — the product and the methodology documentation are the same medium. The "scaffold" equivalent is frontmatter + section structure. The "implement" equivalent is substantive content. The "test" equivalent is pipeline post validation. This domain primarily uses two methodology models: Documentation (single wiki page) and Knowledge Evolution (distill from existing pages).

## Reference Content

### Toolchain

> [!info] Knowledge Domain Stack
>
> | Tool | Purpose | Gate Command |
> |------|---------|-------------|
> | tools/pipeline.py | Orchestration, ingestion, validation | `python3 -m tools.pipeline post` |
> | tools/validate.py | Schema + artifact-type validation | `python3 -m tools.validate` |
> | tools/lint.py | Health checks (orphans, dead rels, thin pages) | `python3 -m tools.lint` |
> | tools/evolve.py | Evolution scoring, scaffolding, maturity review | `python3 -m tools.pipeline evolve --score` |
> | Obsidian | Vault rendering, graph visualization | Manual review |
> | NotebookLM | Grounded research verification | External tool |

### Knowledge Lifecycle — The Progressive Distillation Chain

Unlike code domains where artifacts flow through stages linearly (document → design → scaffold → implement → test), knowledge artifacts follow a **progressive distillation** pattern:

> [!abstract] The Knowledge Evolution Layers
>
> | Layer | Type | How Produced | Examples |
> |-------|------|-------------|---------|
> | **L0: Raw** | raw/ files | Ingestion (fetch, scan, paste) | Articles, transcripts, papers, notes |
> | **L1: Synthesis** | source-synthesis | Processing raw into structured knowledge | "Synthesis: Context Mode — MCP Sandbox" |
> | **L2: Concept** | concept | Cross-referencing multiple syntheses | "Stage-Gate Methodology" |
> | **L3: Comparison** | comparison | Structured evaluation of alternatives | "Cross-Domain Patterns" |
> | **L4: Lesson** | lesson | Convergent learning from ≥3 sources | "CLI Tools Beat MCP for Token Efficiency" |
> | **L5: Pattern** | pattern | Recurring structure across ≥2 instances | "Plan-Execute-Review Cycle" |
> | **L6: Decision** | decision | Resolution of open question with evidence | "Decision: MCP vs CLI for Tool Integration" |
> | **Spine** | model, standards, index | Meta-navigation and governance | "Model: Methodology", standards pages |

### Ingestion Pipeline — Source to Synthesis

> [!info] Methodology model: Documentation (single stage) or custom Ingestion Pipeline
>
> | # | Step | Artifact | File Pattern | Gate |
> |---|------|----------|-------------|------|
> | 1 | Fetch | Raw file | `raw/articles/{slug}.md` or `raw/transcripts/` | File exists, non-empty |
> | 2 | Read | — (understanding, not an artifact) | — | Full file read (offset reads for >200 lines) |
> | 3 | Synthesize | Source-synthesis page | `wiki/sources/{slug}.md` | ≥0.25 ratio to raw, valid frontmatter, summary ≥30 words |
> | 4 | Cross-reference | Updated relationships | Existing pages modified | New relationships wired, pipeline crossref clean |
> | 5 | Validate | Pipeline post output | — | 0 validation errors |
>
> **Depth verification:** If the source DESCRIBES a tool/format/pattern, you MUST examine a real INSTANCE. A README about design.md files ≠ understanding design.md — download and read an actual one. This is the Layer 0 → Layer 1 transition.

### Knowledge Evolution — Concept to Lesson/Pattern/Decision

> [!info] Methodology model: Knowledge Evolution (document → implement)
>
> | # | Stage | Artifact | What You Produce | Gate |
> |---|-------|----------|-----------------|------|
> | 1 | document | Source Inventory | List of wiki pages showing convergence. "These 3 pages all show X pattern." | ≥2 source pages, convergence stated |
> | 2 | implement | Evolved Page | Lesson, pattern, or decision distilled from sources with evidence | Pipeline post 0 errors, derived_from references valid, evidence from sources |
>
> **Quality gates per evolved type:**
>
> | Type | Quality Bar |
> |------|-----------|
> | **Lesson** | ≥3 evidence items from different sources. Mechanism (WHY) explained, not just observation. Applicability with boundaries. |
> | **Pattern** | ≥2 concrete instances with wiki page references. When Not To equally detailed as When To Apply. |
> | **Decision** | ≥2 alternatives with specific rejection reasons. Reversibility honest. Evidence-backed rationale ≥100 words. |

### Domain Curation — Overview and Navigation

> [!info] Methodology model: Documentation (single stage)
>
> | Artifact | Purpose | Gate |
> |----------|---------|------|
> | **Domain Overview** | State of knowledge, maturity map, gaps, priorities | Maturity Map reflects actual page distribution |
> | **Learning Path** | Curated sequence for topic learning | ≥3 pages in order, each annotated |
> | **Evolution Page** | Historical narrative of concept development | ≥5 dated entries, ≥2 key shifts |
> | **Index Page** | Navigation hub for a directory | Curated content above auto-generated list |

### Knowledge-Specific Artifacts NOT in Code Domains

> [!abstract] Unique to Knowledge Domain
>
> | Artifact | Purpose | When |
> |----------|---------|------|
> | **Relationship Graph** | Network of VERB: target connections between pages | Maintained per page, visualized in Obsidian |
> | **Maturity Assessment** | seed → growing → mature → canonical per page | Periodic review via `pipeline evolve --review` |
> | **Evolution Score** | Numeric signal strength for evolution candidates | Computed by `pipeline evolve --score` |
> | **Staleness Detection** | Pages whose sources have been updated since synthesis | `pipeline evolve --stale` |
> | **Gap Inventory** | Missing pages, orphaned targets, weak domains | `pipeline gaps` |
> | **Cross-reference Analysis** | Missing backlinks, domain bridges, comparison candidates | `pipeline crossref` |
> | **Manifest** | JSON snapshot of all pages with metadata | `wiki/manifest.json`, regenerated on every post |

### Scaffold vs Implement in Knowledge Domain

> [!warning] The distinction is STRUCTURAL vs SUBSTANTIVE
>
> | Dimension | Scaffold (structure) | Implement (substance) |
> |-----------|---------------------|----------------------|
> | **What exists** | Frontmatter + section headings + inline guidance comments | Real content filling every section |
> | **Looks like** | `## Summary\n<!-- 2-3 sentences -->` | `## Summary\n\nThe Methodology model defines a flexible FRAMEWORK...` |
> | **Gate** | Page exists, frontmatter valid, required sections present | Summary ≥30 words, relationships ≥1, per-type thresholds met |
> | **Produced by** | `pipeline scaffold <type> <title>` | Human or agent writing |
>
> For knowledge work, "scaffold" = run the scaffolder to create the template structure. "Implement" = fill it with real knowledge. The template IS the scaffold.

### The Self-Referential Property

> [!tip] This wiki's methodology pages ARE knowledge artifacts ABOUT methodology
>
> The Methodology Artifact Taxonomy page is simultaneously:
> - A **knowledge artifact** (type: reference) in the Knowledge domain
> - A **methodology document** describing the artifact system
> - An **instance** of its own taxonomy (Category 10: Knowledge Artifacts)
>
> This self-referential property means the wiki validates its own methodology by producing methodology pages that follow the methodology. If a methodology page fails its own quality gates, the methodology has a self-consistency problem. This is the "Standards Must Preach by Example" lesson in action.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[Principle: Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[Methodology System Map]] |

## Relationships

- BUILDS ON: [[Methodology Artifact Taxonomy]]
- BUILDS ON: [[Model: Knowledge Evolution]]
- BUILDS ON: [[Model: LLM Wiki]]
- RELATES TO: [[Artifact Chains by Methodology Model]]
- RELATES TO: [[Model: Methodology]]
- RELATES TO: [[Artifact Chain: TypeScript/Node Domain]]
- RELATES TO: [[Artifact Chain: Python/Wiki Domain]]
- RELATES TO: [[Artifact Chain: Infrastructure/IaC Domain]]
- FEEDS INTO: [[Methodology Adoption Guide]]

## Backlinks

[[Methodology Artifact Taxonomy]]
[[Model: Knowledge Evolution]]
[[Model: LLM Wiki]]
[[Artifact Chains by Methodology Model]]
[[Model: Methodology]]
[[Artifact Chain: TypeScript/Node Domain]]
[[Artifact Chain: Python/Wiki Domain]]
[[Artifact Chain: Infrastructure/IaC Domain]]
[[Methodology Adoption Guide]]
[[Universal Stages, Domain-Specific Artifacts]]

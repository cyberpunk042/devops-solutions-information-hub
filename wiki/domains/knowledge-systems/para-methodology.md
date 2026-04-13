---
title: "PARA Methodology"
type: concept
layer: 2
maturity: growing
domain: knowledge-systems
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-second-brain-research
    type: article
    file: raw/articles/second-brain-pkm-research.md
    title: "Second Brain / PKM Research"
    ingested: 2026-04-08
  - id: src-zettelkasten-basb
    type: article
    url: "https://zettelkasten.de/posts/building-a-second-brain-and-zettelkasten/"
    title: "Combining Zettelkasten and Building a Second Brain"
    ingested: 2026-04-08
tags: [para, pkm, second-brain, tiago-forte, projects, areas, resources, archives, code-workflow, progressive-summarization, knowledge-management, action-oriented]
---

# PARA Methodology

## Summary

PARA is Tiago Forte's action-oriented personal knowledge management framework that organizes all information into four buckets — Projects (active, outcome-bound), Areas (ongoing responsibilities), Resources (reference material), and Archives (inactive items) — and pairs them with the CODE workflow (Capture, Organize, Distill, Express) and progressive summarization to move material from raw capture toward usable knowledge. Where Zettelkasten optimizes for idea density and connection discovery, PARA optimizes for retrieval speed in service of active work. This wiki maps directly onto PARA: raw/ is Capture, wiki/domains/ is Areas, wiki/sources/ is Resources, and the evolution pipeline's maturity promotion is progressive summarization implemented as code.

## Key Insights

> [!tip] Action drives organization, not taxonomy
> PARA buckets are defined by actionability, not subject. The same book about ML can live in Projects (reading for a deliverable), Areas (ongoing responsibility), Resources (reference, not active), or Archives (consumed). PARA is an activity-relative filing system — the same material belongs in different buckets at different lifecycle stages.

> [!warning] The Project/Area distinction is the critical classification
> A Project has a specific outcome and a deadline. An Area is an ongoing responsibility with no terminal state. Misclassifying Areas as Projects → perpetual "projects" that never complete. Misclassifying Projects as Areas → un-owned work with no delivery accountability.

> [!abstract] Progressive summarization = this wiki's page structure
> Pass 1: Full source (raw/). Pass 2: Highlighted material (## Deep Analysis). Pass 3: Bold highlights (## Key Insights). Pass 4: Executive summary (## Summary). The goal: actionable in 30 seconds from the summary, 2 minutes from highlights, full depth on demand.

**Archives are the secret to a healthy system.** Most PKM systems fail because people fear archiving. PARA treats it as first-class: inactive items move to Archives (retrievable but not cluttering active view). A clean active layer is what makes the system feel fast.

**PARA's weakness is what Zettelkasten fills.** PARA manages lifecycle of resources but does not process them into permanent knowledge. A book in Resources is still just a book — PARA gives it a bucket, not a place in your thinking. Zettelkasten processes Resources into permanent linked notes.

## Deep Analysis

### The Four Buckets

**Projects** — Short-horizon, outcome-bound, has a deadline:
- Specific deliverable: "Deploy monitoring stack for production by Q2"
- Narrowly defined scope
- Once complete, the project moves to Archives
- Rule of thumb: if you cannot describe when it will be done, it is not a Project

**Areas** — Ongoing responsibilities with no end date:
- "Infrastructure reliability", "Team knowledge management", "Security posture"
- Requires maintenance and attention indefinitely
- Associated with a role or identity (you are responsible for this area)
- Rule of thumb: if it ends when you change jobs or roles, it was an Area

**Resources** — Reference material collected for potential future use:
- Saved articles, books, research, tool documentation
- No current activation — just "might be useful"
- Organized by topic, not by project or responsibility
- Rule of thumb: if someone else might benefit from it, it is a Resource

**Archives** — Inactive items from the above three:
- Completed projects
- No-longer-relevant areas
- Consumed or outdated resources
- Archives are not deleted — they are available for search but do not appear in active views

### The CODE Workflow

The CODE workflow is how information moves through the system:

1. **Capture**: Get anything potentially useful into the system immediately. Quantity over quality at this stage — capture everything, sort nothing. The raw/ directory in this wiki is the capture layer.

2. **Organize**: Move captured items to their PARA bucket as quickly as possible. No deep processing at this stage — just filing. The goal is to clear the capture queue and get material into its correct context.

3. **Distill**: Process items toward their essential value. Progressive summarization happens here. Extract the key insight. Write the permanent note. Reduce to what will be useful 2 years from now, not just today.

4. **Express**: Use the distilled knowledge to produce something: a document, a decision, a recommendation, a system change. Expression is the test of whether knowledge was actually internalized. This wiki's `decisions/` and `wiki/spine/` layers are the expression layer.

### Progressive Summarization in Detail

Progressive summarization is a layered reading technique designed for future retrieval:

| Pass | Action | Reading time |
|------|--------|-------------|
| 1 — Capture | Save the full source (note, article, transcript) | — |
| 2 — Highlight | Bold or highlight the most important 10-20% | 5-10 minutes |
| 3 — Bold highlights | Bold the most essential 5-10% of the highlighted material | 2-3 minutes |
| 4 — Executive summary | Write a 1-3 sentence summary in your own words | 1 minute |

The layers accumulate — the full text is always preserved below the summary. This means the system adapts to retrieval context: quick decision → read the summary; detailed reference → read the highlighted text; deep research → read the full source.

This wiki maps progressive summarization directly onto its page structure:
- `## Summary` = executive summary (pass 4)
- `## Key Insights` = bolded highlights (pass 3)
- `## Deep Analysis` = highlighted material (pass 2)
- Source file in `raw/` = full capture (pass 1)

### How This Wiki Maps to PARA

| PARA Element | This Wiki's Implementation |
|---|---|
| Projects | `wiki/decisions/` — bound decisions with specific outcomes |
| Areas | `wiki/domains/*/` — ongoing knowledge domains (ai-agents, knowledge-systems, etc.) |
| Resources | `wiki/sources/` — synthesized individual source pages |
| Archives | Pages with `status: stale`; superseded entries with `SUPERSEDES` relationship |
| Capture (CODE) | `raw/` — all source material, kept permanently for provenance |
| Organize (CODE) | Ingestion pipeline routes to correct domain; frontmatter assigns type/domain |
| Distill (CODE) | `## Summary` + `## Key Insights` + evolution pipeline maturity promotion |
| Express (CODE) | Export pipeline → openfleet, AICP; decisions/; spine/ cross-cutting synthesis |

### PARA vs. Zettelkasten: Complementary Layers

The two methodologies solve different problems:

| Dimension | PARA | Zettelkasten |
|-----------|------|-------------|
| Primary question | "Where does this live? Is it active?" | "What does this connect to? What does it mean?" |
| Organization unit | Bucket (project/area/resource/archive) | Note with links |
| Navigation model | Folder hierarchy | Graph traversal |
| Processing output | Highlighted/summarized source | Permanent linked note in your own words |
| Strength | Action orientation, fast retrieval, lifecycle management | Deep synthesis, connection discovery, emergent insight |
| Weakness | Does not extract ideas from sources | No lifecycle management, no project tracking |

The recommended hybrid: PARA manages what lives outside the Zettelkasten (active projects, resource filing, archiving). Zettelkasten processes the most valuable materials into permanent linked knowledge. Every project completion is an opportunity to feed project-specific insights back into the Zettelkasten as new permanent notes.

## Open Questions

- What is the right trigger for moving a wiki domain from "Areas" to "Archives" status — inactivity threshold, explicit decision, or relevance scoring? (Requires: a curator decision on archiving policy; the pipeline gaps command can surface domains with no recently updated pages as candidates, but the promotion trigger itself is a policy decision not resolved by existing wiki pages)

### Answered Open Questions

> [!example]- Should decisions/ be Projects or Areas in PARA?
> Projects during deliberation, Resources after resolution. Each decision page is a bounded deliberation with a resolved outcome. `status: verified` marks the transition from active project to archived reference. Decisions are the Expression output of the CODE workflow.

> [!example]- What constitutes "expression" for a knowledge system?
> Three forms: (1) export to consuming systems (LightRAG → OpenFleet, docs/kb/ → AICP); (2) decisions that change ecosystem behavior (canonical patterns informing sprint decisions); (3) research priorities driving new ingestion (gaps → queue → fetch). Expression for a wiki = whether synthesized knowledge changes behavior in the ecosystem.

> [!example]- Progressive summarization: page sections or domain-level FAQs?
> Both needed, different audiences. Page-level sections (Summary → Key Insights → Deep Analysis) implement per-concept progressive summarization. `domain-overview` pages (Summary, State of Knowledge, Maturity Map, Gaps, Priorities) implement domain-level executive summaries. Domain-overview pages are the more urgently missing layer.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[Principle: Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[Methodology System Map]] |

## Relationships

- BUILDS ON: [[Second Brain Architecture]]
- COMPARES TO: [[Zettelkasten Methodology]]
- IMPLEMENTS: [[Memory Lifecycle Management]]
- RELATES TO: [[Wiki Ingestion Pipeline]]
- RELATES TO: [[Knowledge Evolution Pipeline]]
- FEEDS INTO: [[Research Pipeline Orchestration]]
- RELATES TO: [[LLM Wiki Pattern]]

## Backlinks

[[Second Brain Architecture]]
[[Zettelkasten Methodology]]
[[Memory Lifecycle Management]]
[[Wiki Ingestion Pipeline]]
[[Knowledge Evolution Pipeline]]
[[Research Pipeline Orchestration]]
[[LLM Wiki Pattern]]
[[Cross-Domain Patterns]]
[[Model: Second Brain]]
[[Progressive Distillation]]
[[Wiki Backlog Pattern]]

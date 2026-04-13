---
title: Second Brain Integration System — Full Chain Requirements
aliases:
  - "Second Brain Integration System — Full Chain Requirements"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: mega-vision
    type: directive
    file: raw/notes/2026-04-12-mega-vision-directive.md
  - id: goldilocks
    type: directive
    file: raw/notes/2026-04-12-goldilocks-higher-ground-directive.md
  - id: full-chain
    type: directive
    file: raw/notes/2026-04-12-full-chain-requirement-directive.md
  - id: dual-perspective
    type: directive
    file: raw/notes/2026-04-12-dual-perspective-directive.md
  - id: iterate-everything
    type: directive
    file: raw/notes/2026-04-12-iterate-everything-directive.md
tags: [requirements, second-brain, integration, full-chain, goldilocks, methodology]
---

# Second Brain Integration System — Full Chain Requirements

## Summary

Complete requirements spec for the second brain integration system — covering the FULL chain from project init through brain integration, methodology adoption, standards adherence, work loop execution, and feedback. 44 distinct requirements extracted from 9 operator directives from the 2026-04-12 session. This document is the AUTHORITY for what needs to be built, updated, and proven.

## Key Insights

1. **The operator asked for something CLEAN and POTENT, not complex.** The system must be navigable at every layer with the right level of information. SOLID and KISS principles.

2. **Everything must be PROVEN end-to-end.** Not described — demonstrated. A clearly sequence of operations that works from init through feedback.

3. **Dual-perspective is fundamental.** Every tool, page, and chain must work TOWARD the second brain (querying) AND toward the project's own wiki (applying).

4. **Models, standards, and examples must be UPDATED** — not just referenced. The super-model, all sub-models, all standards pages, all templates need to reflect the current state of knowledge.

5. **The Goldilocks principle governs everything.** Auto-detect defaults. Warn on detection. Override when needed. Right process for right context. Always flexible, always explained.

## Deep Analysis

### Functional Requirements — Honest Status Assessment

> [!abstract] A. Tools & Gateway (6 requirements)
>
> | ID | Requirement | Status | What's Done | What's Missing |
> |----|------------|--------|------------|---------------|
> | FR-A1 | Python gateway — archive, move, update refs, backup, factory reset | **Partial** | gateway.py: 649 lines, 10 commands. Archive, backup, move work. | Move doesn't update all refs. No factory reset. |
> | FR-A2 | External API — query by stage, domain, chain, template, artifacts | **Partial** | Queries work: stage, model, chain, field, identity, template, config. | No query by artifact name. No "give me everything for this task type." |
> | FR-A3 | Human + AI + MCP — same interface | **Partial** | Gateway is CLI (human + AI). MCP server has 17 tools but NOT gateway ops. | MCP server doesn't expose gateway queries. |
> | FR-A4 | Operational queries — backlog status, logs, lessons | **Missing** | Pipeline has `status` and `backlog`. Gateway doesn't expose them. | Need: `gateway query --backlog`, `gateway query --lessons`, `gateway query --logs`. |
> | FR-A5 | Config visualization — markdown or YAML | **Done** | `gateway config methodology.models` works. Renders any config section. | — |
> | FR-A6 | Agent write access — contribute remarks, lessons, corrections | **Done** | `gateway contribute --type lesson/remark/correction` works. Creates in 00_inbox. | — |

> [!abstract] B. SDLC & Chains (9 requirements)
>
> | ID | Requirement | Status | What's Done | What's Missing |
> |----|------------|--------|------------|---------------|
> | FR-B1 | SDLC customization framework | **Done** | Concept page with phase × scale × chain. CMMI + Lean Startup research. | Needs more real examples per combination. |
> | FR-B2 | Scale-aware rigor | **Done** | Scale tiers defined (micro→massive). Mapped to chains. | Not yet enforced — advisory only. |
> | FR-B3 | Three SDLC chains as configs | **Done** | simplified.yaml, default.yaml, full.yaml in wiki/config/sdlc-chains/. | Chain configs not yet consumed by any tool (gateway queries them but pipeline doesn't). |
> | FR-B4 | Readiness vs Progress dual tracking | **Done** | Concept page. Both fields in schema + all templates. OpenFleet evidence. | Not implemented in any validation tool. Frontmatter only. |
> | FR-B5 | 99→100 = human only | **Documented** | In readiness page, adoption guide, principles. | No tooling enforces it. |
> | FR-B6 | Milestone hierarchy | **Done** | Type added to schema. Template created. Scaffolder support. | No milestones actually created yet. |
> | FR-B7 | Impediment types | **Done** | 8 types in schema. Documentation in backlog hierarchy rules. | Not enforced — advisory only. |
> | FR-B8 | Full demonstrated chain | **NOT DONE** | Partial: gateway can walk through steps. Chain not proven end-to-end with a REAL project. | **THE MAIN GAP.** Need to walk OpenArms or a new project through the ENTIRE chain, step by step, and show it works. |
> | FR-B9 | Proven sub-chains | **NOT DONE** | Sub-chains listed but not individually demonstrated. | Each sub-chain (init, methodology, standards, work loop, feedback) needs its own proven walkthrough. |

> [!abstract] C. Goldilocks & Identity (4 requirements)
>
> | ID | Requirement | Status | What's Done | What's Missing |
> |----|------------|--------|------------|---------------|
> | FR-C1 | Goldilocks principle | **Done** | Concept page. Principle page. Identity protocol. Selection matrix. | Needs more worked examples per identity profile. |
> | FR-C2 | Self-identification protocol | **Done** | 7 dimensions. YAML profile schema. 3 example profiles. Auto-detection function. | Auto-detection needs testing across more projects. |
> | FR-C3 | Auto-detect with warnings | **Partial** | Auto-detection works for domain, scale, execution mode, phase. | No WARNING output when auto-detecting. Should say "Auto-detected: typescript. Override with --domain if wrong." |
> | FR-C4 | Flexibility always explained | **Partial** | Each concept page has "When To / When Not To." Principles have "Boundaries." | Not every page shows HOW to adapt — some just say "it's flexible." |

> [!abstract] D. Models & Standards & Examples (6 requirements)
>
> | ID | Requirement | Status | What's Done | What's Missing |
> |----|------------|--------|------------|---------------|
> | FR-D1 | Global standards adherence | **Done** | Concept page mapping 12 standards to wiki components. | Standards are REFERENCED, not DEMONSTRATED in code. Need OpenAPI spec for gateway, CloudEvents for hooks. |
> | FR-D2 | Template exemplars | **Partial** | 6 templates upgraded (note, epic, learning-path, evolution, milestone, principle). 13 were already STRONG. | Templates have guidance but most lack INLINE EXAMPLE CONTENT. A lesson template should show a REAL lesson inside it. |
> | FR-D3 | Proper artifact examples | **Partial** | 3 annotated exemplars in standards pages (lesson, pattern, decision). | 12 other standards pages have exemplar REFERENCES but not inline annotations. |
> | FR-D4 | Strong model updates | **Partial** | 8 model pages updated with session evidence. | Models need FULL iteration — not just new sections added, but existing content reviewed against current state. |
> | FR-D5 | Standards with real examples | **Partial** | Standards pages reference exemplars. 3 have inline walkthroughs. | Need inline walkthroughs for ALL 15 per-type standards. |
> | FR-D6 | Context engineering formalized | **Partial** | Structured Context lesson + principle. Five Cognitive Contexts. Validation matrix. | Not formalized as a CHAIN LINK. No "here's how to engineer context for your identity profile." |

> [!abstract] E. Structure & Navigation (5 requirements)
>
> | ID | Requirement | Status | What's Done | What's Missing |
> |----|------------|--------|------------|---------------|
> | FR-E1 | Maturity-based folder structure | **Done** | lessons/ and patterns/ reorganized. 00_inbox→04_principles. Scaffolder updated. | decisions/ and sources/ have folders but no content moved into them yet. |
> | FR-E2 | Validated vs hypothesis | **Done** | 03_validated + 04_principles/hypothesis structure exists. | No 04_principles/validated yet (need operator confirmation to promote). |
> | FR-E3 | Scalability rule (>10) | **Done** | Documented. Current validated folders have 40 lessons (may need clusters). | No clustering implemented yet. |
> | FR-E4 | Browsable from any entry point | **Partial** | 81% weave coverage. Navigate command. System map. | 19% of pages (mostly log entries) lack navigation. Some weave is generic, not contextual. |
> | FR-E5 | Location mapping memory | **Done** | Archive creates JSON mapping. Query --mapping reads it. | Not yet used in practice (no pages archived yet). |

> [!abstract] F. Integration & Dual-Perspective (6 requirements)
>
> | ID | Requirement | Status | What's Done | What's Missing |
> |----|------------|--------|------------|---------------|
> | FR-F1 | Dual-scope tools | **Done** | Gateway has --wiki-root and --brain. Auto-detects second brain location. | --brain auto-detection needs more fallback paths. |
> | FR-F2 | Projects query brain then apply locally | **Partial** | Gateway queries work from external project. | No "apply to my project" command. Query returns data but doesn't WRITE to the project's config. |
> | FR-F3 | Brain = source of truth | **Done** | Ecosystem Feedback Loop pattern. Super-model as hub. | Working in practice the 2026-04-12 session (OpenArms/OpenFleet fed back knowledge). |
> | FR-F4 | Sister project integration | **Done** | 22 OpenArms lessons + OpenFleet architecture deeply integrated. | Need to return regularly, not one-time scan. |
> | FR-F5 | New sources pipeline | **Documented** | Pipeline has fetch/ingest/post chain. | 10-15 sources from operator not yet provided. |
> | FR-F6 | Every layer addressed per source | **Documented** | Ingestion methodology defined (extract → cross-ref → gaps → deepen). | Not yet proven with new sources the 2026-04-12 session. |

> [!abstract] G. Knowledge & Iteration (8 requirements)
>
> | ID | Requirement | Status | What's Done | What's Missing |
> |----|------------|--------|------------|---------------|
> | FR-G1 | Continuous improvement | **Active** | Multiple iteration passes the 2026-04-12 session. | Needs to be ongoing, not session-bounded. |
> | FR-G2 | Human confirmation at each level | **Documented** | 99→100 rule. Principles need operator promotion. | No tooling blocks promotion without confirmation. |
> | FR-G3 | Constant evolution | **Active** | Evolution pipeline running. 3 principles extracted. | Needs regular evolution sweeps, not just session-driven. |
> | FR-G4 | Iterate existing pages | **Done the 2026-04-12 session** | 13 OpenArms lessons integrated. 8 model pages deepened. All lessons promoted to validated. | One pass. Operator says "multiple times." |
> | FR-G5 | Strongest vision | **Partial** | Super-model v1.3. 3 principles. Goldilocks protocol. | Vision is scattered across pages. Needs ONE cohesive document showing the complete picture. |
> | FR-G6 | Practice own methodology | **Partial** | CLAUDE.md has identity profile. Followed methodology for the 2026-04-12 session. | Not all work the 2026-04-12 session followed proper stages. Some was reactive. |
> | FR-G7 | Consistent structures across injections | **Partial** | Structured Context principle. Five Cognitive Contexts. Validation matrix. | Not yet applied to THIS wiki's own injections (CLAUDE.md, skills, templates). |
> | FR-G8 | Proto-programming mindset | **Documented** | Lesson + principle. Evidence from OpenArms/OpenFleet. | Not yet the DEFAULT approach. Templates don't demonstrate proto-programming. |

### Acceptance Criteria

> [!success] The system is DONE when:
>
> | ID | Criterion | Verification |
> |----|-----------|-------------|
> | AC-1 | A new project can walk from `gateway what-do-i-need` through full integration in under 30 minutes | Demonstrated with a real project (OpenArms or new) |
> | AC-2 | Every sub-chain (init, methodology, standards, work loop, feedback) is individually proven | Each sub-chain documented with commands + expected output |
> | AC-3 | All 15 model pages reflect current session knowledge | Human review confirms each model is current |
> | AC-4 | All 15 per-type standards have inline annotated exemplars | Human review confirms quality |
> | AC-5 | Super-model reflects complete current state | v1.4+ with all new concepts, principles, chains |
> | AC-6 | Gateway serves human + AI + MCP with same interface | MCP server exposes gateway operations |
> | AC-7 | Templates demonstrate proto-programming (rich inline examples) | Human review of 5 key templates |
> | AC-8 | Operator says "I can browse this from any entry point and find what I need" | Human confirmation |

### Out of Scope

> [!warning] Not in this requirements spec:
>
> - 10-15 new source ingestions (operator will provide separately)
> - OpenAPI spec for gateway (future — after gateway stabilizes)
> - Full fleet integration (OpenFleet immune system integration into wiki tools)
> - Automated compliance checking tooling (separate epic)
> - Harness v3 implementation (future)

## Open Questions

> [!question] ~~Should the requirements spec itself follow the 2026-04-12 session methodology? (Document → Design → Scaffold → Implement → Test)~~
> **RESOLVED:** Yes. The wiki practices what it preaches. Methodology is self-referential.
> This document is the Document stage. Design stage = architecture decisions on how to meet each requirement. Scaffold = stubs. Implement = build. Test = prove the chain works.

> [!question] ~~Which requirements need operator confirmation before building?~~
> **RESOLVED:** All acceptance criteria + any requirement that changes the methodology itself. Implementation details (paths, names) don't need confirmation.
> FR-B8 (full demonstrated chain) and FR-B9 (sub-chains) need the operator to DEFINE what "proven" means. What sequence of commands constitutes proof?

> [!question] ~~What is the priority order?~~
> **RESOLVED:** Operator stated repeatedly: iterate existing > update models > fill gaps > new sources. Depth over breadth.
> The operator keeps repeating: iterate existing pages, update models, prove the chain. NOT build new tools. The priority is: D (models/standards) → E (navigation) → B8/B9 (proven chain) → A (tools) → C (Goldilocks refinement).

### How This Connects — Navigate From Here

> [!abstract] From Requirements → Implementation Plan
>
> | Direction | Go To |
> |-----------|-------|
> | **What epics implement this?** | [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]], [[sdlc-rules-and-structure-customizable-project-lifecycle|SDLC Rules and Structure — Customizable Project Lifecycle]] |
> | **What principles govern this?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]], [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]], [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is the identity protocol?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **What is the system map?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- IMPLEMENTS: [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
- IMPLEMENTS: [[sdlc-rules-and-structure-customizable-project-lifecycle|SDLC Rules and Structure — Customizable Project Lifecycle]]
- BUILDS ON: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
- BUILDS ON: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[model-llm-wiki|Model — LLM Wiki]]
- RELATES TO: [[global-standards-adherence|Global Standards Adherence — Engineering Principles the Wiki Follows]]
- FEEDS INTO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
[[sdlc-rules-and-structure-customizable-project-lifecycle|SDLC Rules and Structure — Customizable Project Lifecycle]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[model-methodology|Model — Methodology]]
[[model-llm-wiki|Model — LLM Wiki]]
[[global-standards-adherence|Global Standards Adherence — Engineering Principles the Wiki Follows]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 15 Models Reflect Current Knowledge]]
[[e011-standards-exemplification-all-15-per-type-standards-with-inline-annotated-e|E011 — Standards Exemplification — All 15 Per-Type Standards with Inline Annotated Exemplars]]
[[e012-template-enrichment-rich-proto-programming-examples|E012 — Template Enrichment — Rich Proto-Programming Examples]]
[[e013-super-model-evolution-v2-0-with-sub-super-models|E013 — Super-Model Evolution — v2.0 with Sub-Super-Models]]
[[e014-goldilocks-navigable-system-identity-to-action-in-continuous-flow|E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow]]
[[e015-gateway-tools-completion-all-requirements-implemented-with-mcp-integration|E015 — Gateway Tools Completion — All Requirements Implemented with MCP Integration]]
[[e016-integration-chain-proof-end-to-end-with-openarms|E016 — Integration Chain Proof — End to End with OpenArms]]
[[e017-context-engineering-framework-formalized-as-model-with-standards|E017 — Context Engineering Framework — Formalized as Model with Standards]]
[[e018-global-standards-implementation-actual-adherence-not-just-reference|E018 — Global Standards Implementation — Actual Adherence Not Just Reference]]
[[e019-obsidian-navigation-complete-browse-experience-with-folder-cleanup|E019 — Obsidian Navigation — Complete Browse Experience with Folder Cleanup]]
[[e020-knowledge-sweep-global-quality-confirmation-by-human-review|E020 — Knowledge Sweep — Global Quality Confirmation by Human Review]]
[[e021-new-source-ingestion-10-15-sources-through-full-pipeline|E021 — New Source Ingestion — 10-15 Sources Through Full Pipeline]]
[[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
[[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]]

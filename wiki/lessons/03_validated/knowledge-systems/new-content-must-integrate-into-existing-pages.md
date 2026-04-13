---
title: New Content Must Integrate Into Existing Pages
aliases:
  - "New Content Must Integrate Into Existing Pages"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Methodology Standards Initiative — Honest Assessment"
  - "Model: LLM Wiki"
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: phase1-disconnect
    type: observation
    file: docs/SESSION-2026-04-12-handoff.md
    description: 37 new pages created alongside existing pages without any wiring — operator could not find deliverables
  - id: discoverability-test
    type: observation
    file: docs/SESSION-2026-04-12-handoff.md
    description: Operator navigated wiki cold and found 'just flim traces... no way to piece anything together'
tags: [wiki, discoverability, integration, anti-pattern, lesson-learned, agent-failure]
---

# New Content Must Integrate Into Existing Pages

## Summary

Creating new wiki pages next to existing ones without weaving the new content INTO the existing high-traffic pages produces an invisible system. The pages exist but nobody finds them. The discoverability test — can someone navigate to the new content starting from the pages they already know? — is the only validation that matters. Link count is not discoverability. If the entry points don't mention the new system, the new system doesn't exist.

## Context

> [!warning] When does this lesson apply?
>
> - You are producing a batch of new wiki pages (5+)
> - The new pages form a system or subsystem
> - Existing pages already cover the parent domain (methodology, tooling, etc.)
> - Users/agents will look for the new content starting from the pages they already read

## Insight

> [!tip] The Discoverability Principle
>
> **The test:** Can the operator find the new system COLD — starting from the pages they already know, with no guidance?
>
> **Why it fails:** Agent creates 37 new files. Model: Methodology (581 lines, the page everyone reads) gets 14 lines added. Someone reading it would never find the new system. The new files have relationships pointing AT each other, forming an isolated cluster invisible from the main graph.
>
> **The fix:** Integration means updating the ENTRY POINTS — the high-traffic pages that people already navigate to. Every new subsystem needs:
>
> 1. A section in its parent model page (not just a link — a SECTION)
> 2. A table row in the system map
> 3. A link from the standards page
> 4. A mention in the learning path
> 5. Backlinks from the pages it references

The mechanism: creating new pages is easy and feels productive. Updating existing pages to reference them is harder — it requires reading the existing page, understanding its structure, finding the right place, and making it flow naturally. Agents default to "create new" because it's additive. But without integration, the new content is orphaned in practice even if it has relationships in frontmatter.

## Evidence

> [!bug]- Phase 1: Invisible System (2026-04-12)
>
> **What happened:** 37 new methodology pages created — standards, taxonomy, domain chains, adoption guide, system map. Each page had relationships to other new pages. But the existing high-traffic pages (model-methodology.md, methodology-framework.md, model-methodology-standards.md) received minimal updates.
>
> **What the operator saw:**
> "Are you done or are you not done? Why do I not find anything?"
> "anywhere all I find is just flim traces... no way to piece anything together... just a few little fragment here and there"
>
> **Root cause:** 37 pages created, but model-methodology.md (the page everyone starts from) got 14 lines added. The entry points didn't know the new system existed.

> [!success] Phase 2: Integration-First Recovery
>
> After the restart, integration was done BEFORE creating new standalone pages:
> - model-methodology.md gained an Artifact Taxonomy section with domain chain links
> - methodology-framework.md gained a Portable Methodology Engine section
> - model-methodology-standards.md gained Per-Type Artifact Standards and Beyond Wiki Pages sections
> - model-llm-wiki-standards.md gained a Per-Type Standards Index table
> - 16 pages received AI Quick Start callouts pointing into the new system
>
> Result: the operator could navigate from any known page to any new page within 2 clicks.

## Applicability

> [!abstract] The Integration Checklist
>
> | When you create... | You MUST update... |
> |--------------------|--------------------|
> | Pages in a new subsystem | The parent model page (add a section, not just a link) |
> | New standards | The standards page AND the model page |
> | New templates | The system map and the adoption guide |
> | New domain pages | The domain overview (_index.md) |
> | New lessons/patterns | The learning path that covers the topic |
> | Any batch of 5+ pages | Run the discoverability test: navigate cold from the spine |

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself:
>
> 1. **If I delete all my new pages, can the operator tell anything changed?** — If no, the integration is missing. The new content exists but is invisible from the pages people actually navigate to.
> 2. **Have I updated the ENTRY POINTS — the pages the operator navigates to first?** — Creating new pages is easy. Updating existing high-traffic pages to reference them is harder and more important. Every new subsystem needs a section (not just a link) in its parent model page.
> 3. **Do the existing high-traffic pages have SECTIONS pointing to the new content, not just links?** — A link buried in a Relationships section is not discoverable. A dedicated section with context is. Integration means structural presence in the entry points.
> 4. **Can someone find my work starting from the model registry, navigating cold with no guidance?** — The discoverability test is the only validation that matters. Run it: start from spine pages and try to reach your new content in 2 clicks.

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What entry points exist?** | [[methodology-system-map|Methodology System Map]] — every component listed. [[model-registry|Model Registry]] — all 15 models. |
> | **How does the wiki's own structure help?** | [[model-llm-wiki|Model — LLM Wiki]] — domain indexes, manifest, wikilink generation |
> | **What does good integration look like?** | Phase 2 of the 2026-04-12 session: 6 spine pages updated with "How This Weaves Together" navigation tables |
> | **How does the Goldilocks protocol help?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — identity-based entry points: who you are determines where you start |

## Relationships

- DERIVED FROM: [[methodology-standards-initiative-honest-assessment|Methodology Standards Initiative — Honest Assessment]]
- BUILDS ON: [[model-llm-wiki|Model — LLM Wiki]]
- RELATES TO: [[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]]
- RELATES TO: [[always-plan-before-executing|Always Plan Before Executing]]
- RELATES TO: [[coverage-blindness-modeling-only-what-you-know|Coverage Blindness — Modeling Only What You Know]]
- FEEDS INTO: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]

## Backlinks

[[methodology-standards-initiative-honest-assessment|Methodology Standards Initiative — Honest Assessment]]
[[model-llm-wiki|Model — LLM Wiki]]
[[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[coverage-blindness-modeling-only-what-you-know|Coverage Blindness — Modeling Only What You Know]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]

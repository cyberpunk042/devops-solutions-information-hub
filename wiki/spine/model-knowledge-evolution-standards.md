---
title: "Evolution Standards — What Good Knowledge Promotion Looks Like"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-10
updated: 2026-04-10
sources: []
tags: [knowledge-evolution, standards, maturity, promotion, scoring, gold-standard, anti-patterns]
---

# Evolution Standards — What Good Knowledge Promotion Looks Like

## Summary

This page defines the quality bar for KNOWLEDGE EVOLUTION. Where [[Model: Knowledge Evolution]] defines the system (scorer, prompt builder, backends, maturity lifecycle), this page shows what GOOD evolution looks like — from proper candidate scoring through quality generation to honest maturity promotion. ==Every gold standard is a real evolved page from this wiki.==

## Key Insights

- **A good evolved page has visible provenance.** The `derived_from` field names its source concepts. The Evidence section cites specific data points with `(source-id)` parentheticals. The reader can trace any claim back to its origin.

- **Good scoring surfaces convergence, not popularity.** The best evolution candidates are pages where independent sources converge on the same insight. A page with 12 backlinks from one domain is popular. A page with 4 backlinks from 3 domains is a convergence candidate — that's the evolution signal.

- **Good maturity promotion is conservative.** Most pages should stay at `growing` for weeks. Premature promotion to `mature` or `canonical` creates false authority. The standard is: would you stake a production decision on this page's claims?

- **The evolution cadence matters more than individual runs.** One excellent evolution run followed by months of neglect is worse than weekly `pipeline chain review` that catches 2-3 candidates each time. Steady-state improvement beats burst effort.

## Deep Analysis

### Gold Standard: Evolved Lesson Page

> [!success] **Gold standard: [[CLI Tools Beat MCP for Token Efficiency]]** (122 lines, L4, growing)
> **What makes it the standard:**
> - **`derived_from`**: 3 sources (Accuracy Tips, Harness Engineering, Claude Code). Not one source extrapolated — three independent sources CONVERGING.
> - **Evidence section**: 8 discrete evidence items. Each has a **bold source label**, a specific claim with data ("12x cost differential"), and a `(src-xxx)` parenthetical. Every claim is traceable.
> - **Insight explains the MECHANISM**: WHY CLI beats MCP, not just THAT it does. "Schema tokens from unused tools occupy space that could hold task context — context pollution." The lesson teaches the underlying principle.
> - **Applicability names 4 domains** AND has "When MCP is still the right choice" with 4 counterexamples. Honest about its own boundaries.
> - **CONTRADICTS relationship**: brave — explicitly contradicts "the default assumption that MCP is the standard tool integration pattern." Lessons that challenge assumptions are higher-value than lessons that confirm them.

> [!bug]- **Anti-pattern: the restated concept**
> A "lesson" that is really just the source concept page rewritten with slightly different words. No new insight. No mechanism explanation. No multi-source convergence. Just "X is true because X is true."
>
> **The test:** Remove the lesson page. Does the wiki lose any insight that wasn't already on the source concept page? If not, the evolution produced no value — the concept should stay a concept until real distillation is possible.

---

### Gold Standard: Evolved Pattern Page

> [!success] **Gold standard: [[Scaffold → Foundation → Infrastructure → Features]]** (176 lines, L5, growing)
> **What makes it the standard:**
> - **`instances` frontmatter field**: 4 concrete occurrences (Research Wiki, OpenFleet, AICP, Front-Middleware-Backend). Not "this appears in many projects" — WHICH projects and HOW.
> - **Pattern Description with testable exit criteria**: "Scaffold is done when direction is set." "Foundation is done when there's a single entry point." Criteria you can CHECK, not feelings about completeness.
> - **When Not To section is honest**: POCs (deliberately skip stages), hotfixes (go straight to features), exploratory scripts (don't benefit from SFIF). A pattern that "always applies" is not useful.
> - **The recursive property declared**: SFIF applies at project level, feature level, component level, design level. This elevates it from a sequence to a fractal principle.

> [!bug]- **Anti-pattern: the pattern without instances**
> A "pattern" page that describes a structural template but names zero concrete occurrences. "This pattern appears in many systems" without naming ONE. A pattern without instances is a hypothesis.
>
> **The test:** Can you link to ≥2 wiki pages that demonstrate this pattern? If not, it's not a pattern yet — it's a concept that MIGHT become a pattern when more evidence appears.

---

### Gold Standard: Evolved Decision Page

> [!success] **Gold standard: [[Decision: MCP vs CLI for Tool Integration]]** (121 lines, L6, growing)
> **What makes it the standard:**
> - **Decision section is ONE clear statement**: "Default to CLI+Skills for project-internal tooling. Use MCP for external service bridges." No hedging, no "it depends on many factors."
> - **3 rejected alternatives with specific reasons**: MCP-First ("loads all schemas at startup"), Skills-Only ("can't block dangerous operations"), CLI-Only ("loses MCP's genuine advantages for external services").
> - **Reversibility is explicit**: `reversibility: easy` — "swap a config." The reader knows the cost of being wrong.
> - **Dependencies section**: 6 downstream effects if reversed. What changes if this decision is overturned.
> - **Evidence-backed rationale**: 12x cost differential, Microsoft recommendation, Google Trends convergence, harness engineering principle. Not "we felt this was better."

> [!bug]- **Anti-pattern: the decision without alternatives**
> A "decision" that documents what was chosen but not what was rejected. Without alternatives, there's no evidence that options were evaluated — the "decision" might just be the first idea that worked.
>
> **The test:** Does the Alternatives section have ≥2 entries with concrete rejection reasons? If not, the page should be a concept, not a decision.

---

### Gold Standard: Scorer Output

What good scorer output looks like — diverse candidates, not tag-pair noise.

> [!success] **Good scorer output (after tuning)**
> Top 10 candidates include:
> - Cross-source convergence lessons (3+ sources agreeing on a principle)
> - Relationship hub pages (concepts connected to many domains)
> - Domain layer gaps (domains with concepts but no lessons/patterns)
> - Open question clusters (multiple pages asking the same unresolved question)
>
> Diversity across types, domains, and evolution reasons.

> [!bug]- **Bad scorer output (before tuning)**
> Top 10 candidates were all tag co-occurrence matches: pages sharing the same 2 tags. No convergence signal. No domain diversity. Just "these pages have similar tags." The tag co-occurrence weight was 0.25 (too high) — rebalanced to 0.10. Generic tags (model, concept, spine) were not filtered — added `_GENERIC_TAGS` set.

---

### Gold Standard: Maturity Promotion

> [!success] **Good promotion: seed → growing**
> The page has: 3+ relationships to other pages, 2+ distinct sources, at least one other page references it. The scorer surfaces it. Human reviews: "Yes, this page has real cross-references and multi-source backing."

> [!success] **Good promotion: growing → mature**
> The page has: passed human review for content accuracy. Evidence section has ≥3 independent data points. The insight has been applied (not just documented) — there's a real instance in the ecosystem that validates it. `derived_from` links to source concepts.

> [!warning] **The canonical bar**
> Canonical should be RARE. A canonical page means: tested against real implementation, no known contradictions in the knowledge base, stable for 30+ days, would you stake a production decision on its claims? Most pages should never reach canonical — growing and mature are the healthy steady-state.

> [!bug]- **Anti-pattern: promoting everything to growing**
> Batch-promoting all seed pages to growing because they "have frontmatter and relationships." Growing requires: 3+ REAL relationships (not just backlinks from an index page), 2+ DISTINCT sources (not the same source cited twice), and at least one inbound reference from another page that adds new context.

---

### The Evolution Checklist

> [!tip] **Run this before any evolution batch**
> - [ ] `pipeline evolve --score --top 10` — review the candidate list for diversity (domains, types, evolution reasons)
> - [ ] `pipeline evolve --dry-run --top 3` — review assembled context for the top candidates (is there enough source material?)
> - [ ] Each evolved page has `derived_from` naming source concepts
> - [ ] Each lesson has ≥3 evidence items from independent sources
> - [ ] Each pattern has ≥2 concrete instances with page references
> - [ ] Each decision has ≥2 alternatives with rejection reasons
> - [ ] `pipeline post` passes with 0 validation errors after evolution
> - [ ] Maturity promotion reviewed: seed → growing has 3+ relationships + 2+ sources; growing → mature has human review + operational validation

## Open Questions

> [!question] **Should evolution candidates be diversified automatically?**
> If the top 10 are all from the same domain, should the scorer inject diversity (e.g., max 3 per domain in top 10)? Or should the human reviewer handle diversity? (Requires: testing with both approaches)

> [!question] **What's the minimum evidence bar for a lesson?**
> Currently suggested: ≥3 independent sources. Is this right? A lesson from 2 strong sources might be more valid than one from 4 weak sources. Should evidence quality be weighted, not just counted? (Requires: analyzing existing lesson quality vs evidence count)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Principles** | [[Principle: Infrastructure Over Instructions for Process Enforcement]] · [[Principle: Structured Context Governs Agent Behavior More Than Content]] · [[Principle: Right Process for Right Context — The Goldilocks Imperative]] |
> | **Identity** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[Methodology System Map]] |

## Relationships

- BUILDS ON: [[Model: Knowledge Evolution]]
- RELATES TO: [[LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[Methodology Standards — What Good Execution Looks Like]]
- RELATES TO: [[CLI Tools Beat MCP for Token Efficiency]] (lesson gold standard)
- RELATES TO: [[Scaffold → Foundation → Infrastructure → Features]] (pattern gold standard)
- RELATES TO: [[Decision: MCP vs CLI for Tool Integration]] (decision gold standard)

## Backlinks

[[Model: Knowledge Evolution]]
[[LLM Wiki Standards — What Good Looks Like]]
[[Methodology Standards — What Good Execution Looks Like]]
[[CLI Tools Beat MCP for Token Efficiency]]
[[Scaffold → Foundation → Infrastructure → Features]]
[[Decision: MCP vs CLI for Tool Integration]]

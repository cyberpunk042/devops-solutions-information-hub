---
title: Evolution Standards — What Good Knowledge Promotion Looks Like
aliases:
  - "Evolution Standards — What Good Knowledge Promotion Looks Like"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-10
updated: 2026-04-10
sources: []
tags: [knowledge-evolution, standards, maturity, promotion, scoring, gold-standard, anti-patterns]
---

# Evolution Standards — What Good Knowledge Promotion Looks Like

## Summary

This page defines the quality bar for KNOWLEDGE EVOLUTION. Where [[model-knowledge-evolution|Model — Knowledge Evolution]] defines the system (scorer, prompt builder, backends, maturity lifecycle), this page shows what GOOD evolution looks like — from proper candidate scoring through quality generation to honest maturity promotion. ==Every gold standard is a real evolved page from this wiki.==

## Key Insights

- **A good evolved page has visible provenance.** The `derived_from` field names its source concepts. The Evidence section cites specific data points with `(source-id)` parentheticals. The reader can trace any claim back to its origin.

- **Good scoring surfaces convergence, not popularity.** The best evolution candidates are pages where independent sources converge on the same insight. A page with 12 backlinks from one domain is popular. A page with 4 backlinks from 3 domains is a convergence candidate — that's the evolution signal.

- **Good maturity promotion is conservative.** Most pages should stay at `growing` for weeks. Premature promotion to `mature` or `canonical` creates false authority. The standard is: would you stake a production decision on this page's claims?

- **The evolution cadence matters more than individual runs.** One excellent evolution run followed by months of neglect is worse than weekly `pipeline chain review` that catches 2-3 candidates each time. Steady-state improvement beats burst effort.

## Deep Analysis

### Gold Standard: Evolved Lesson Page

> [!success] **Gold standard: [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]** (122 lines, L4, growing)
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

> [!success] **Gold standard: [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]** (176 lines, L5, growing)
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

> [!success] **Gold standard: [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]** (121 lines, L6, growing)
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

> [!question] ~~**Should evolution candidates be diversified automatically?**~~
> **RESOLVED:** No. Evolution scoring already uses multiple signals (convergence, relationship density, staleness). Diversity is emergent from signal variety.
> If the top 10 are all from the same domain, should the scorer inject diversity (e.g., max 3 per domain in top 10)? Or should the human reviewer handle diversity? (Requires: testing with both approaches)

> [!question] ~~****What's the minimum evidence bar for a lesson?****~~
> **RESOLVED:** ≥3 evidence items from ≥2 independent sources with mechanism explained. Single-source = observation, not lesson. Already in lesson-page-standards.
> Currently suggested: ≥3 independent sources. Is this right? A lesson from 2 strong sources might be more valid than one from 4 weak sources. Should evidence quality be weighted, not just counted? (Requires: analyzing existing lesson quality vs evidence count)

### Annotated Exemplar

> [!example] Real example: [[model-knowledge-evolution|Model — Knowledge Evolution]] — why this page is exemplary
>
> **What makes this page meet the standard:**
>
> 1. **7-layer density architecture with promotion criteria** — The page defines layers L0 through L6 (plus L5+ Principles) in a structured table showing type, maturity, what it contains, and the transformation at each layer. The gap at Layer 3 is explicitly explained ("the jump from concept to lesson is a qualitative shift, not just compression") — this demonstrates intellectual honesty about the architecture rather than forcing a neat sequence.
> 2. **Scoring signals with explicit weights** — Six signals are listed with their exact weights (cross-source convergence at 0.30, relationship hub at 0.20, down to tag co-occurrence at 0.10). The tuning history is documented in a `[!tip]` callout: initial weights overvalued tag co-occurrence (0.25), which produced candidates that were just tag-pair matches. This is a model page that shows its EVOLUTION, not just its current state.
> 3. **8-step generation loop with the critical step identified** — The generation pipeline is listed as 8 numbered steps (SCORE through LOOP), and a `[!warning]` callout explicitly calls out ASSEMBLE as "where quality is won or lost." This identifies the leverage point — the step where intervention has the highest impact — rather than treating all steps as equal.
> 4. **Honest State of Knowledge with quantified coverage** — The `[!success]` block lists specific counts (40 validated lessons, 15 validated patterns, 3 principles, 1,321-line scorer implementation). The `[!warning]` block names 6 specific gaps including "scorer gaming — manual cross-linking could inflate scores artificially." The page does not pretend the pipeline is complete.
>
> **What could still improve:** The Three LLM Backends section is thin — it lists the backends in a table but provides no quality comparison data between them, which the Open Questions section acknowledges. The weekly evolution cadence section shows the pipeline commands but lacks evidence of how many candidates the cadence actually surfaces in practice.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Principles** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] · [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] · [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **Identity** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[model-knowledge-evolution|Model — Knowledge Evolution]]
- RELATES TO: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
- RELATES TO: [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] (lesson gold standard)
- RELATES TO: [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]] (pattern gold standard)
- RELATES TO: [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]] (decision gold standard)

## Backlinks

[[model-knowledge-evolution|Model — Knowledge Evolution]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
[[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]

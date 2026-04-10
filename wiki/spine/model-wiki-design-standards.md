---
title: "Wiki Design Standards — What Good Styling Looks Like"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [wiki-design, standards, styling, callouts, examples, gold-standard, anti-patterns]
---

# Wiki Design Standards — What Good Styling Looks Like

## Summary

This page defines the quality bar for VISUAL DESIGN in the wiki. Where [[Model: Wiki Design]] defines the system (callout vocabulary, formatting contexts, layout patterns), this page shows what GOOD looks like — gold-standard examples of each pattern, anti-patterns to avoid, and before/after comparisons. Use this when styling pages — don't just use callouts randomly, match the standard.

## Key Insights

- The difference between a raw page and a styled page is not beauty — it is USABILITY. Styled pages are scannable. Raw pages require reading every word.
- Every callout has a specific semantic purpose. Using the wrong type is worse than using no callout — it misleads the reader.
- Foldable callouts (`-` suffix) are the key to long pages — they let the page be both scannable AND deep.
- Anti-patterns are as important as patterns — knowing what NOT to do prevents the most common mistakes.

## Deep Analysis

### Gold Standard: Model Catalog Entry

**Reference:** [[Model: Methodology]], Model Catalog section

> [!success] **What makes it the standard**
> The Feature Development entry demonstrates the complete pattern:
>
> 1. **`> [!info]`** opens with a blue header stating stages + purpose. The reader sees "Feature Development: document → design → scaffold → implement → test" and knows WHAT this is immediately.
> 2. **Markdown table** follows with stages × artifacts × gates. Structured data that can be scanned row by row.
> 3. **`> [!abstract]`** states selection conditions. "Selected when: task_type = epic, module, or refactor." The reader knows WHEN this applies.
> 4. **`> [!example]-`** (foldable) contains a real instance with numbered steps. COLLAPSED by default — the page stays scannable. Expand for proof.
> 5. **`> [!tip]`** provides design insight. "Why it stops at design" — optional, only when there's a non-obvious design decision to explain.
>
> The page has 9 model entries. Each follows this exact pattern. The reader can scan all 9 by reading info headers, or dive deep by expanding examples.

> [!warning] **Anti-pattern: model entry WITHOUT styling**
> Before callouts, each model was:
> ```markdown
> #### Feature Development
> **Stages:** document → design → scaffold → implement → test
> | Stage | What you produce | Gate |
> ...table...
> **Selected when:** task_type = epic, module, or refactor.
> **Real instance:** Building the wiki backlog system. Document (read OpenArms model...
> ```
> Everything looks the same. No visual hierarchy. No foldability. The reader must read every paragraph to find what they need. Bold labels help but don't create STRUCTURE.

---

### Gold Standard: Bug/Failure Report

**Reference:** [[Model: Methodology]], "What Goes Wrong" section

> [!success] **What makes it the standard**
> Each of 7 bugs uses `> [!bug]-` (foldable, red icon):
> - **Title** shows: bug name + design input + version bump. "Bug 5: Stage boundary violation → Design input: ALLOWED/FORBIDDEN (v4)"
> - **Body** shows: what happened, how found, what the fix was
> - **Collapsed view**: all 7 bugs visible as a scannable list with titles
> - **Expanded view**: full detail per bug
>
> This pattern works because bugs are REFERENCE material — you scan the list to find the relevant one, then expand for detail. The foldability is what makes 7 detailed bugs fit in a page without overwhelming it.

> [!warning] **Anti-pattern: bugs as a table**
> Before callouts, the bugs were a 7-row table with 4 columns. Tables work for small data but 7 multi-paragraph bugs in table cells become unreadable — cells expand vertically, alignment breaks, and the table dominates the page.

---

### Gold Standard: Worked Example / Selection Walkthrough

**Reference:** [[Model: Methodology]], Model Selection section

> [!success] **What makes it the standard**
> Each worked example uses:
> - **`> [!example]-`** (foldable) with a scenario title: "Research how OpenArms does methodology enforcement"
> - **Inside**: condition evaluation TABLE (dimension | value | why) — structured, not prose
> - **`> [!success]`** nested inside: the selection result with what the model produces
>
> Two examples exist side-by-side. Reader sees "2 worked examples available" from the folded titles without being overwhelmed. Expand one to see the full evaluation.

> [!warning] **Anti-pattern: worked examples as inline prose**
> "The user says 'research how OpenArms does methodology enforcement.' The conditions are: task_type is research, the phase is foundation, the domain is knowledge-systems..." — this buries the structure. A condition evaluation TABLE is scannable; prose conditions are not.

---

### Gold Standard: Information Reference Block

**Reference:** [[Model: Wiki Design]], Emphasis Hierarchy section

> [!success] **What makes it the standard**
> The emphasis hierarchy uses `> [!info]` containing a TABLE:
> | Level | Syntax | Semantic meaning | Use for |
> This puts structured reference data in a visually distinct box. The blue background says "this is reference material" and the table says "scan for your level."
>
> Key: the callout ADDS to the table. A bare table looks like data. A table inside `> [!info]` looks like a REFERENCE CARD — something you come back to repeatedly.

> [!warning] **Anti-pattern: tables without callout context**
> A bare table of emphasis levels floating in prose looks like it might be a one-time comparison. Inside `> [!info]`, it's clearly a REFERENCE that you're expected to internalize and return to. The callout provides semantic framing.

---

### Gold Standard: Callout Vocabulary Demonstration

**Reference:** [[Model: Wiki Design]], The Callout Vocabulary section

> [!success] **What makes it the standard**
> Each callout type is demonstrated BY BEING THAT CALLOUT TYPE. The `[!info]` definition IS an info callout. The `[!warning]` definition IS a warning callout. The page preaches by example — you SEE each callout while reading ABOUT it.
>
> This self-referential property is the highest form of the standard: the document that defines the callout vocabulary uses the callout vocabulary to define itself.

> [!warning] **Anti-pattern: describing callouts in prose**
> "The info callout has a blue background and an info icon. Use it for context and definitions." — this TELLS without SHOWING. The reader has to imagine what it looks like. The standard SHOWS by BEING the thing it describes.

---

### Gold Standard: Page Layout Pattern

**Reference:** [[Model: Wiki Design]], Page Layout Patterns section

> [!success] **What makes it the standard**
> Each layout pattern uses `> [!example]-` (foldable) with a bold title naming the pattern and its reference page. Inside: numbered steps showing the callout sequence.
>
> 8 patterns exist. All foldable. The section is scannable — you see 8 pattern titles and expand the one you need. This is the meta-pattern: the section about patterns USES the pattern it defines (foldable examples).

---

### Gold Standard: Emphasis Usage

**Reference:** [[Model: Methodology]], full page

> [!success] **What makes it the standard**
> Emphasis is used consistently throughout:
> - **Bold** for key terms on first significant use: "**Feature Development**", "**Research**", "**ALLOWED**", "**FORBIDDEN**"
> - *Italic* sparingly for stress within prose
> - `code` for technical values: `` `task_type` ``, `` `> [!info]` ``, `` `methodology.yaml` ``
> - ==Highlight== not used on the Methodology page (reserved for truly critical information)
> - No bold-everything, no italic-everything — each format carries its semantic weight

> [!warning] **Anti-pattern: emphasis soup**
> "**The** *methodology* `model` **is** a **framework** for *defining* **work** *processes*." — when everything is emphasized, nothing is. The reader can't tell what matters. Bold should appear on ~5-10% of terms, not 50%.

---

### Gold Standard: Graceful Degradation

> [!success] **What makes it the standard**
> On the Methodology page, if you strip ALL callouts, the content still reads correctly. Info callout bodies are complete paragraphs. Example bodies are numbered lists. Bug bodies explain the bug. The callouts ADD visual structure but the TEXT carries the meaning.
>
> Test: open any styled page in a plain text editor or GitHub. Can you still understand it? If yes, the styling is correct. If the meaning is lost without the callout rendering, the styling is carrying too much load.

> [!warning] **Anti-pattern: meaning in styling only**
> - A `> [!success]` callout with body "Yes" — if the callout doesn't render, the reader sees `> Yes` with no context.
> - A foldable example with no summary in the title — collapsed, the reader sees `> [!example]-` and nothing about WHAT the example demonstrates.
> - Critical information only in a `==highlight==` — in plain text, it's surrounded by `==` which might confuse.

---

### Anti-Pattern Catalog

| Anti-pattern | What it looks like | Why it fails | Fix |
|-------------|-------------------|-------------|-----|
| **Bold everything** | Every other word is **bold** | Nothing stands out when everything stands out | Bold only key terms (~5-10% of text) |
| **Wrong callout type** | Bug report in `[!info]`, guidance in `[!bug]` | Misleading — colors and icons carry semantic meaning | Match type to purpose per vocabulary |
| **Non-foldable long examples** | 30-line example blocking the page | Page becomes unscrollable, reader loses context | Always use `[!example]-` (foldable) for examples |
| **Callout for everything** | Every paragraph wrapped in a callout | Visual noise — callouts lose meaning when overused | Use callouts for semantic CATEGORIES, prose for flow |
| **Nested 3+ deep** | Callout inside callout inside callout | Unreadable — indentation compounds, lines get narrow | Max 2 nesting levels |
| **Table in a table** | Trying to nest tables (markdown doesn't support) | Renders broken | Use separate tables or restructure data |
| **Raw lists as catalog** | 9 models listed as `- **Name:** description` | No visual hierarchy, not scannable | Use the model entry pattern (info + table + abstract + example) |
| **Heading skip** | H1 → H3 (skipping H2) | Breaks Obsidian outline, violates hierarchy | Always use sequential heading levels |
| **Blockquote as callout** | `>` used for non-quotes | Confusing — blockquotes are for actual quotations | Use callouts `> [!type]` for semantic boxes |
| **File paths in text** | `wiki/domains/ai-agents/claude-code.md` | Not clickable, not semantic | Use `[[Claude Code]]` wikilinks |

## Open Questions

- Should there be a formal "design review" step before pages are marked growing — checking styling against this standard? (Requires: testing with a review workflow)
- At what point do we create CSS snippets to enhance the built-in callout types? (Requires: the callout vocabulary to stabilize across 20+ pages first)
- Should the before/after examples include actual screenshots from Obsidian? (Requires: screenshot tooling in WSL → Windows)

## Relationships

- BUILDS ON: [[Model: Wiki Design]]
- BUILDS ON: [[LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[Model: Methodology]] (the first page to demonstrate all patterns)
- RELATES TO: [[The Agent Must Practice What It Documents]]

## Backlinks

[[Model: Wiki Design]]
[[LLM Wiki Standards — What Good Looks Like]]
[[Model: Methodology]] (the first page to demonstrate all patterns)]]
[[The Agent Must Practice What It Documents]]

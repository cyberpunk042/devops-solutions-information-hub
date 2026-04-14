# DESIGN.md — Wiki Visual Design System

Audience: anyone creating or modifying wiki pages.
Source authority: [Model — Wiki Design](wiki/spine/models/foundation/model-wiki-design.md) ·
[Wiki Design Standards](wiki/spine/standards/model-standards/model-wiki-design-standards.md) ·
[Model — Markdown as IaC](wiki/spine/models/agent-config/model-markdown-as-iac.md)

---

## Design Philosophy

The wiki's visual design IS its operational design. Structure programs agent behavior, not just human
comprehension. Three levels of compliance:

| Technique | Compliance | Mechanism |
|-----------|-----------|-----------|
| Prompt engineering (prose instructions) | ~25% | Content read and may be ignored |
| Context engineering (structured instructions) | ~60% | Tables and ALLOWED/FORBIDDEN lists narrow interpretation |
| Structural engineering (callouts, headers, tables) | ~90%+ | Form declares intent — agent cannot misread a `[!warning]` |

**Implication:** a wiki page is not just documentation. It is a specification that agents execute.
How you structure a page determines how reliably it is followed. Design for the agent reader, not
only the human reader.

The three standard layers of the wiki:

| Layer | What it defines | Authority |
|-------|----------------|-----------|
| Content Structure | Types, fields, sections, schema | `wiki/config/wiki-schema.yaml` |
| Content Quality | What "good" looks like per type | [LLM Wiki Standards](wiki/spine/standards/model-standards/model-llm-wiki-standards.md) |
| Visual Design | How pages look and how structure signals meaning | This file + [Model — Wiki Design](wiki/spine/models/foundation/model-wiki-design.md) |

---

## Callout Vocabulary

Eight callout types with fixed semantic purposes. Using the wrong type misleads faster than using
no callout. **Colors carry meaning — treat them as a typed API.**

| Type | Color | Semantic purpose | Foldable? | Phrase test |
|------|-------|-----------------|-----------|-------------|
| `> [!info]` | Blue | Context, definitions, reference data | Optional | "Here is information to absorb." |
| `> [!abstract]` | Teal | Conditions, summaries, TL;DR | Optional | "Here is the distilled essence." |
| `> [!tip]` | Cyan | Guidance, best practices, actionable advice | Optional | "Here is something useful to apply." |
| `> [!warning]` | Orange | Cautions, anti-patterns, risks | Optional | "Be careful here." |
| `> [!example]-` | Purple | Real instances, demonstrations | **Always** | "Here is proof." |
| `> [!success]` | Green | Verified outcomes, confirmed facts | Optional | "This is verified." |
| `> [!bug]-` | Red | Failure instances, incidents | **Always** | "This went wrong." |
| `> [!question]` | Lavender | Open questions, unresolved gaps | Optional | "This is unknown." |

**`[!example]-` and `[!bug]-` are always foldable** (`-` suffix). They are proof and reference
material — scannable as titles, expandable for detail. If there are 7 bugs, you want to see 7
titles, not 7 expanded blocks.

**Anti-pattern:** using `[!info]` for everything. When every callout is blue, callouts lose
meaning. Use prose between callout groups to preserve contrast.

**Anti-pattern:** nesting more than 2 levels deep. Each level steals indentation. By level 3,
content wraps every few words.

---

## Emphasis Hierarchy

Six levels, each with a distinct semantic meaning. Using multiple levels simultaneously is
intentional — they do different jobs and must not be interchanged.

| Level | Syntax | Semantic meaning | Use for |
|-------|--------|-----------------|---------|
| 1 (highest) | `==highlight==` | ==Critical attention== | Must-not-miss rules. **Rare — at most 1-2 per page.** |
| 2 | `> [!type]` title | Callout header | Section-level categorization |
| 3 | `**bold**` | **Importance** | Key terms, field names, critical rules in prose |
| 4 | `*italic*` | *Emphasis* | Stress, nuance, first use of a term, titles of works |
| 5 | `` `code` `` | `Technical reference` | Commands, filenames, field values, syntax |
| 6 (lowest) | plain text | Normal prose | Everything else |

**Anti-pattern — emphasis soup:** "**The** *methodology* `model` **is** a **framework** for
*defining* **work** *processes*." When everything is emphasized, nothing is. Bold should appear
on ~5-10% of words — the key terms only.

---

## Tables vs Prose

| Need | Use | Not |
|------|-----|-----|
| Compare 2+ things across dimensions | Table | Prose paragraphs describing each |
| Decision matrix, per-stage rules, per-role specs | Table | Numbered list |
| List discrete items (no order) | Unordered list | Table with one column |
| Explain WHY something works | Prose | Table or list |
| Track completion | Task list `- [x]` | Ordered list |
| Quote a person or external source | Blockquote `>` | Callout (callouts are for categories) |

**Tables inside `[!info]`** become reference cards — the callout frame signals "internalize this."
**Bare tables** signal one-time comparisons. Use the frame when the table is reference material.

---

## Page Layout Patterns

Every page follows this section order:

```
# Title
## Summary          ← 2-3 sentences minimum; used by LightRAG for description
## Key Insights     ← condensed resolution boundary
## Deep Analysis    ← full resolution (concept, comparison, deep-dive types)
## Open Questions   ← gaps (optional but encouraged)
## Relationships    ← VERB: target format, one per line
```

### Layout by Page Type

**Model catalog entry** (used in [Model — Methodology](wiki/spine/models/foundation/model-methodology.md)):
1. `> [!info]` — blue header with stage overview + purpose
2. Markdown table — stages × artifacts × gates
3. `> [!abstract]` — selection conditions
4. `> [!example]-` — real instance, always foldable
5. `> [!tip]` or `> [!warning]` — non-obvious design insight (optional)

**Lesson page:**
1. Summary — the lesson stated clearly in one actionable sentence
2. Context — specific trigger conditions (not "useful in many situations")
3. Insight — the MECHANISM (why it works, not just that it works)
4. Evidence — each item: **bold source label** + specific claim + `(source-id)`
5. Applicability — domains where it applies + `> [!tip]` for "when NOT to apply"
6. Relationships — `[[wikilinks]]` with ALL_CAPS verbs

**Decision page:**
1. Summary — the recommendation in 2-3 sentences
2. Decision — `> [!success]` callout with the clear decision statement
3. Alternatives — each as `> [!abstract]-` foldable with rejection reasoning
4. Rationale — evidence-backed prose with **bold source labels**
5. Reversibility — `> [!info]` stating how hard to undo
6. Dependencies — downstream impacts

**Comparison page:**
1. Summary — what is being compared and why
2. Comparison Matrix — markdown TABLE (never prose). Rows = criteria, columns = alternatives.
3. Key Insights — bullet points from the comparison
4. Deep Analysis — per-alternative or per-criteria deep dives
5. `> [!tip]` — decision guidance ("use X when..., use Y when...")

**Source-synthesis page:**
1. Summary — what the source IS and the headline finding
2. Key Insights — each as **bold label** + prose. Subsection headings for deep sources (250+ lines).
3. Open Questions — each with `(Requires: ...)` tag
4. Relationships — `[[wikilinks]]`

**Domain overview page:**
1. Summary — domain scope
2. State of Knowledge — what's known, what's thin
3. Gaps — `> [!question]` callouts for major gaps
4. Key Pages — table of essential reading
5. FAQ — each as `### Q: Question?` with 2-3 sentence answer linking to deeper pages

**Backlog task** (minimal by design):
Frontmatter carries state. Summary + Done-When (task list `- [ ]`). No callouts needed.

---

## YAML Frontmatter as Programmatic Interface

Frontmatter is not metadata — it is a programmatic declaration that determines validation,
search, export, and agent behavior. Each field narrows one behavior dimension.

### Required Fields

```yaml
title: "Page Title"          # Must match the # Heading exactly
type: concept                # Page type — determines required sections + templates
domain: cross-domain         # Must match folder path segment
status: draft                # draft | synthesized | validated | archived
confidence: low              # low | medium | high
created: 2026-04-14          # ISO date
updated: 2026-04-14          # ISO date (update on every change)
sources: []                  # List of source objects with id, type, url/file, title
tags: []                     # Flat list of lowercase hyphenated tags
```

### Valid Page Types

```
concept, source-synthesis, comparison, reference, deep-dive, index,
lesson, pattern, decision, principle, domain-overview, learning-path,
evolution, operations-plan, milestone, epic, module, task, note
```

Every type has a template: `python3 -m tools.pipeline scaffold <type> <title>`

### Evolved Pages — Additional Fields

Lessons, patterns, and decisions require maturity tracking:

```yaml
maturity: seed               # seed | growing | mature | principle
layer: 4                     # 0-6 knowledge distillation level
derived_from: []             # Source page IDs this was distilled from
instances: []                # For patterns: list of {page, context} objects
```

---

## Relationship Format

Relationships are programmatic — they are indexed, cross-referenced, and navigated by tooling.

```markdown
## Relationships

- BUILDS ON: [[model-llm-wiki|Model — LLM Wiki]]
- ENABLES: [[wiki-agent-skill|Wiki Agent Skill]]
- COMPARES TO: [[model-methodology|Model — Methodology]], [[model-claude-code|Model — Claude Code]]
- CONTRADICTS: [[eager-loading-pattern|Eager Loading Pattern]]
```

**Rules:**
- ALL_CAPS verbs only
- `[[slug|display title]]` format — slug is the filename without extension
- One relationship per line (comma-separated targets allowed when semantically equivalent)
- Minimum 1 relationship per page (unless first in a new domain)

**Valid verbs:** `BUILDS ON`, `ENABLES`, `COMPARES TO`, `CONTRADICTS`, `USED BY`, `RELATES TO`,
`FEEDS INTO`, `DERIVED FROM`, `SUPERSEDES`, `IMPLEMENTS`, `EXTENDS`

---

## Maturity Folder Structure

Evolved knowledge pages (lessons, patterns, decisions) use maturity-based subfolders:

| Folder | Meaning | Promotion criteria |
|--------|---------|-------------------|
| `00_inbox` | Fresh scaffold — content incomplete | Automatic on scaffold |
| `01_drafts` | Filled but not cross-referenced | Content sections complete |
| `02_synthesized` | Cross-referenced, confidence high | ≥1 relationship, sources cited |
| `03_validated` | Evidence sufficient | ≥3 independent evidence items (lessons), ≥2 instances (patterns) |
| `04_principles` | Governing truths | ≥3 derived validated lessons converge on one principle |

**Rule:** new scaffolds always go to `00_inbox`. Promote as evidence accumulates. Never
manually place a page in `03_validated` without verifying its evidence count.

> 10 items in a folder = time to create sub-structure.

---

## Styling Checklist

Run before marking any page as styled or complete:

- [ ] Every callout type matches its semantic purpose
- [ ] All examples and bugs longer than 5 lines are foldable (`[!example]-` or `[!bug]-`)
- [ ] No more than 2 nesting levels anywhere on the page
- [ ] Bold used for key terms only (~5-10% of text)
- [ ] Tables inside `[!info]` for reference cards; bare tables for one-time comparisons
- [ ] Heading levels are sequential — no skips (H1 → H2 → H3)
- [ ] Page is scannable in 10 seconds by reading callout titles and headings alone
- [ ] `==highlight==` used at most 1-2 times on the entire page
- [ ] Prose sections exist between callout groups — callouts don't touch callouts without breathing room
- [ ] Summary field is ≥30 words

---

## Before/After: The Impact of Structural Engineering

### Raw version (Version 1)

```markdown
#### Feature Development
**Stages:** document → design → scaffold → implement → test
Used for complex work where the solution isn't known.
| Stage | What you produce | Gate |
...table...
**Selected when:** task_type = epic, module, or refactor.
**Real instance:** Building the wiki backlog system: 1. Document...
```

Everything has the same visual weight. No hierarchy. Walls of text.
The reader must read every word to find what they need.

### Styled version (Version 3)

```markdown
> [!info] **Feature Development:** document → design → scaffold → implement → test
> Used for complex work where the solution isn't already known.

| Stage | What you produce | Gate |
...table...

> [!abstract] **Selected when**
> task_type = `epic`, `module`, or `refactor`.

> [!example]- **Real instance: Building the wiki backlog system**
> 1. Document — Read existing methodology, map the gap...
```

The blue header catches your eye in 2 seconds. The table gives structure. The teal abstract gives
context. The purple example hides behind a fold until you need it. **Four semantic layers, each
doing one job.** The information is identical; the usability is dramatically different.

---

## Graceful Degradation

The wiki must read well in Obsidian, GitHub, Docusaurus, and plain text. No styling should be
**required** for comprehension — only enhance it.

| Feature | Obsidian | GitHub | VS Code | Plain text |
|---------|----------|--------|---------|------------|
| `**bold**`, `*italic*`, `` `code` `` | Full | Full | Full | `**visible**` |
| `==highlight==` | Yellow bg | `==visible==` | `==visible==` | `==visible==` |
| `> [!tip] Title` | Styled colored box | Blockquote | Blockquote | `> Title` |
| `[[Page]]` wikilinks | Clickable link | `[[visible]]` | `[[visible]]` | `[[visible]]` |
| Mermaid diagrams | Rendered | Rendered | Code block | Code block |
| Foldable callouts `[!example]-` | Fold/expand | Always visible | Always visible | Always visible |
| `%% comment %%` | Hidden | Visible | Visible | Visible |

**Hard constraint:** never put critical content ONLY in a callout title, an embed, or a highlight.
The information must survive in plain text. Test: strip all callouts mentally — does the page still
make sense?

---

## Rendering Contexts

This wiki has three distinct rendering contexts. They coexist for different purposes — they are
not evolution stages.

| Context | What works | What does not | Adaptation |
|---------|-----------|--------------|-----------|
| Obsidian (wiki) | Full callout vocabulary, graph view, CSS classes | Custom callout types need CSS | Reference implementation |
| GitHub/GitLab | Standard markdown | Callouts show as blockquotes | Use blockquote-compatible patterns |
| Docusaurus/MkDocs | Admonitions (similar syntax) | Different callout names (`:::tip`) | Map per framework |
| AI agent (raw text) | Structure: headers, tables, lists | Visual formatting invisible | **Structure IS the design** |

For Docusaurus, the Obsidian → remark mapping is:

| Obsidian (wiki) | Remark/Docusaurus (docs) |
|-----------------|------------------------|
| `> [!tip] Title` | `:::tip[Title]` |
| `> [!warning]` | `:::danger` |
| `[[Page Title]]` | `[text](./path)` |

---

## Exemplar Pages

These pages demonstrate the standards above in their natural form:

| Page | What it demonstrates |
|------|---------------------|
| [Model — Methodology](wiki/spine/models/foundation/model-methodology.md) | Model catalog entry pattern — `[!info]` + table + `[!abstract]` + `[!example]-` |
| [Wiki Design Standards](wiki/spine/standards/model-standards/model-wiki-design-standards.md) | Self-referential — the page IS what it teaches |
| [CLI Tools Beat MCP for Token Efficiency](wiki/lessons/03_validated/) | Gold-standard lesson: 8 evidence items, mechanism explained, `CONTRADICTS` relationship |
| [Decision — MCP vs CLI](wiki/decisions/02_validated/) | Gold-standard decision: 3 alternatives, reversibility, downstream dependencies |

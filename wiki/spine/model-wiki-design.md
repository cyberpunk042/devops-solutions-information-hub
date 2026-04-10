---
title: "Model: Wiki Design"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-09
updated: 2026-04-09
sources:
  - id: src-obsidian-basic-syntax
    type: documentation
    url: "https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax"
    file: raw/articles/obsidian-basic-formatting-syntax.md
    title: "Obsidian Basic Formatting Syntax"
    ingested: 2026-04-09
  - id: src-obsidian-advanced-syntax
    type: documentation
    url: "https://help.obsidian.md/Editing+and+formatting/Advanced+formatting+syntax"
    file: raw/articles/obsidian-advanced-formatting-syntax.md
    title: "Obsidian Advanced Formatting Syntax"
    ingested: 2026-04-09
  - id: src-obsidian-callouts
    type: documentation
    url: "https://help.obsidian.md/Editing+and+formatting/Callouts"
    file: raw/articles/obsidian-callouts-reference.md
    title: "Obsidian Callouts Reference"
    ingested: 2026-04-09
  - id: src-markdown-basic
    type: documentation
    url: "https://www.markdownguide.org/basic-syntax/"
    title: "Markdown Guide — Basic Syntax"
    ingested: 2026-04-09
  - id: src-markdown-extended
    type: documentation
    url: "https://www.markdownguide.org/extended-syntax/"
    title: "Markdown Guide — Extended Syntax"
    ingested: 2026-04-09
  - id: src-remarkjs
    type: documentation
    url: "https://github.com/remarkjs/remark"
    file: raw/articles/remarkjsremark.md
    title: "remarkjs/remark — Markdown processor with plugins"
    ingested: 2026-04-09
tags: [wiki-design, model, formatting, obsidian, markdown, callouts, styling, remark, visual-design, standards]
---

# Model: Wiki Design

## Summary

The Wiki Design model defines the VISUAL layer of the knowledge system — how pages look and feel, not just what they contain. It covers three distinct formatting contexts (universal markdown, Obsidian extensions, and remark/Docusaurus for public docs), a semantic callout vocabulary for styled information blocks, text and structural formatting rules, internal navigation patterns, visual elements (diagrams, math, embeds), per-page CSS customization via properties, and page layout patterns per page type. This model complements the [[Model: LLM Wiki]] (content structure) and [[LLM Wiki Standards — What Good Looks Like]] (content quality) as the third standard layer. It is not finished — it is an evolving standard that grows as the wiki applies and discovers what works.

## Key Insights

- **Three formatting contexts, not tiers.** Universal markdown (works everywhere), Obsidian Flavored Markdown (for the wiki), and remark/Docusaurus (for public docs) are DIFFERENT CONTEXTS with different syntax. The wiki uses Obsidian. Public docs use Docusaurus. Both build on universal markdown. They are not evolution stages — they coexist for different purposes.

- **Callouts are the primary styling tool.** Obsidian's 14 built-in callout types — with colors, icons, foldability, and nesting — transform raw markdown into visually structured, scannable pages. No plugins needed. They degrade gracefully to blockquotes in non-Obsidian renderers.

- **`cssclasses` in frontmatter enables per-page-type styling.** A model page with `cssclasses: [model-page]` can be targeted by a CSS snippet for consistent visual treatment across all model pages. This is the mechanism for systematic styling.

- **Formatting is semantic, not decorative.** Bold means importance. Italic means emphasis. Highlight means attention. Callout types map to semantic purposes (info=context, tip=guidance, warning=caution, bug=failure, example=instance). Choosing a format is a MEANING decision.

- **Graceful degradation is a design constraint.** Core content (Tier 1 markdown) must be readable outside Obsidian. Callouts degrade to blockquotes. Wikilinks degrade to plain text. Pages must be USEFUL in GitHub, VS Code, and plain text — not just beautiful in Obsidian.

## Deep Analysis

### The Three Formatting Contexts

#### Context 1: Universal Markdown

The baseline that works in every renderer — Obsidian, GitHub, VS Code, Docusaurus, any text editor.

> [!info] **Text Formatting**
> | Syntax | Renders as | Semantic meaning |
> |--------|-----------|-----------------|
> | `**bold**` | **bold** | Importance — key terms, critical rules |
> | `*italic*` | *italic* | Emphasis — stress, nuance, foreign terms |
> | `***bold italic***` | ***bold italic*** | Maximum emphasis — rare, use sparingly |
> | `~~strikethrough~~` | ~~strikethrough~~ | Deletion, outdated content, corrections |
> | `` `inline code` `` | `inline code` | Technical terms, file names, commands, values |
> | `> blockquote` | Blockquote | Actual quotations from sources |

> [!info] **Structural Elements**
> | Element | Syntax | Rule |
> |---------|--------|------|
> | **Headings** | `#` through `######` | Strict hierarchy — never skip levels (H1 → H2 → H3, never H1 → H3). H1 = page title only. |
> | **Paragraphs** | Blank line between | One idea per paragraph. Short paragraphs > wall of text. |
> | **Ordered lists** | `1. ` | Sequential steps, ranked items, numbered procedures |
> | **Unordered lists** | `- ` | Non-sequential items. Use `-` consistently (not `*` or `+`) |
> | **Task lists** | `- [ ]` / `- [x]` | Done When checklists, verification items |
> | **Horizontal rules** | `---` | Section separators in catalogs. Blank lines before and after. |
> | **Tables** | `\| col \| col \|` | Structured data. Align with `:--`, `:--:`, `--:`. Headers required. |
> | **Code blocks** | Triple backticks + language | Always specify language (`python`, `yaml`, `bash`, `markdown`). |
> | **Links** | `[text](URL)` | External URLs only. For internal links, use wikilinks (Context 2). |
> | **Images** | `![alt](URL)` | Always include descriptive alt text. |
> | **Footnotes** | `[^1]` + `[^1]: text` | Citations, tangential notes that would break flow |

> [!tip] **When to use tables vs prose vs lists**
> - **Table**: when data has 2+ dimensions and benefits from scanning across rows/columns. Comparison matrices, stage/artifact mappings, feature matrices.
> - **List**: when items are discrete and order matters (steps) or doesn't (features). One dimension.
> - **Prose**: when relationships between ideas need to be explained, not just listed. When "why" matters more than "what."

#### Context 2: Obsidian Flavored Markdown (for the wiki)

Everything Obsidian adds on top of universal markdown. These features render in Obsidian and Obsidian Publish but degrade gracefully elsewhere.

> [!info] **Wikilinks — Internal Navigation**
> | Syntax | Purpose | Example |
> |--------|---------|---------|
> | `[[Page Title]]` | Link to another wiki page | `[[Methodology Framework]]` |
> | `[[Page Title\|Display Text]]` | Link with custom display text | `[[Methodology Framework\|the meta-system]]` |
> | `[[Page Title#Heading]]` | Link to specific section | `[[Model: LLM Wiki#Quality Gates]]` |
> | `[[Page Title#^block-id]]` | Link to specific paragraph | Deep references to exact content |
> | `![[Page Title]]` | Embed entire page | Use sparingly — heavy |
> | `![[Page Title#Heading]]` | Embed specific section | More targeted embedding |
> | `![[image.png\|640]]` | Embed image with width | Always specify width for consistency |

> [!warning] **Wikilink rules for this wiki**
> - ALL relationship targets use wikilinks: `- BUILDS ON: [[Page Title]]`
> - NEVER use file paths in body text — use `[[Page Title]]` not `wiki/path/file.md`
> - Wikilinks that resolve show in the Obsidian graph. Broken wikilinks show as unresolved nodes.

> [!info] **Highlights and Comments**
> - `==highlighted text==` — renders with yellow background. Use for CRITICAL information that must not be missed. Rarer than bold.
> - `%% hidden comment %%` — visible in edit mode only, invisible in reading view. Use for editorial notes, reminders to self, WIP markers.

> [!info] **Properties (YAML Frontmatter)**
> Special frontmatter fields that Obsidian interprets:
> | Property | Purpose | Example |
> |----------|---------|---------|
> | `tags` | Searchable tags (MUST be list) | `tags: [methodology, model]` |
> | `aliases` | Alternative page names for search | `aliases: [SFIF, "Build Lifecycle"]` |
> | `cssclasses` | CSS classes applied to the page | `cssclasses: [model-page, wide-tables]` |
>
> `cssclasses` is the key to SYSTEMATIC styling — a CSS snippet targeting `.model-page` styles all model pages consistently.

### The Callout Vocabulary

Callouts are the primary visual styling tool. Obsidian provides 14 built-in types. We use 8 with specific semantic meanings:

> [!info] Definition: Context, background, stage overviews
> Use `[!info]` when introducing a concept, providing context, or defining what something IS. The blue color signals "here is information to absorb."

> [!abstract] Summary: Selection conditions, TL;DR, key takeaways
> Use `[!abstract]` for condensed information — when to use something, preconditions, the executive summary. The teal color signals "here is the distilled essence."

> [!tip] Guidance: Best practices, adoption advice, design insights
> Use `[!tip]` for actionable guidance — what to DO with the information. The cyan/flame color signals "here is something useful to apply."

> [!warning] Caution: Anti-patterns, things that go wrong, limitations
> Use `[!warning]` for things that can go WRONG. Pyramid-tier compromises, depth verification violations, stage boundary risks. The orange color signals "be careful here."

> [!example]- Instance: Real examples, worked cases, demonstrations
> Use `[!example]` for concrete instances from the ecosystem. ALWAYS foldable (`-` suffix) — collapsed by default so the page is scannable, expandable for detail. The purple color signals "here is proof."
>
> The `-` suffix is CRITICAL for examples — they're often the longest callouts and would overwhelm the page if always expanded.

> [!success] Confirmed: Verified outcomes, selection results, validated facts
> Use `[!success]` for things that are PROVEN. Model selection results, test outcomes, confirmed decisions. The green color signals "this is verified."

> [!bug]- Failure: Bugs from real operation, incidents, things that broke
> Use `[!bug]` for real failures. Always foldable — collapsed shows the summary, expanded shows the detail and fix. The red color signals "this went wrong."

> [!question] Open: Needs research, unresolved, requires investigation
> Use `[!question]` for genuinely open items. The purple/yellow color signals "this is not yet answered."

> [!tip] **Callout syntax reference**
> ```markdown
> > [!type] Custom Title
> > Content with **all markdown** supported inside.
> > Including [[wikilinks]], `code`, tables, and nested callouts.
>
> > [!type]- Foldable (collapsed by default)
> > Content hidden until expanded.
>
> > [!type]+ Foldable (expanded by default)
> > Content visible but can be collapsed.
> ```
>
> **Nesting**: add another `>` level for nested callouts.
> **Title-only**: omit the body for a compact label.
> **Custom types**: define via CSS snippets in `.obsidian/snippets/`.

### The 6 Remaining Built-In Callout Types

Not in our primary vocabulary but available for specific needs:

| Type | Aliases | Color | Use for |
|------|---------|-------|---------|
| `note` | — | Gray | Generic notes (prefer specific types) |
| `todo` | — | Blue | Task-related callouts (prefer task lists) |
| `failure` | fail, missing | Red | Missing functionality (prefer bug for real failures) |
| `danger` | error | Red | Critical errors (prefer warning for most cases) |
| `quote` | cite | Gray | Extended quotations from external sources |
| `success` variant: `check`, `done` | — | Green | Completion indicators |

### Visual Elements

> [!info] **Mermaid Diagrams**
> Rendered natively in Obsidian. Use for:
> - **Flow charts**: model selection logic, pipeline flows, decision trees
> - **Sequence diagrams**: interaction between tracks, stage progression
> - **Mind maps**: concept relationships, domain overviews
>
> ````markdown
> ```mermaid
> graph TD
>     A[Task arrives] --> B{Evaluate conditions}
>     B -->|spike| C[Research model]
>     B -->|module| D[Feature Dev model]
>     B -->|bug| E[Bug Fix model]
>     B -->|hotfix| F[Hotfix model]
> ```
> ````
>
> **Internal links in Mermaid**: add `class NodeName internal-link;` to make nodes clickable wikilinks. Note: these don't appear in the graph view.

> [!info] **Math / LaTeX**
> Rendered via MathJax. Use when mathematical notation is genuinely needed:
> - Inline: `$E = mc^2$` renders as $E = mc^2$
> - Block: `$$` on own lines wrapping the expression
>
> Don't use for emphasis or decoration — only for actual mathematical content.

> [!info] **Embeds**
> Embed content from other pages directly:
> - `![[Page]]` — embed entire page (use sparingly — heavy)
> - `![[Page#Section]]` — embed one section (more targeted)
> - `![[Page#^block-id]]` — embed one paragraph (most precise)
> - `![[image.png|640]]` — embed image with width
>
> **When to embed vs link**: embed when the reader NEEDS to see the content inline without navigating away. Link when the content is supplementary.

### Page Layout Patterns

These are the visual patterns we've established for different page types:

> [!example]- **Model entry pattern** (from Model: Methodology catalog)
> Each model in a catalog gets:
> 1. `> [!info]` — stage overview + purpose (the blue header)
> 2. Markdown table — stages with artifacts and gates
> 3. `> [!abstract]` — selection conditions (when this model runs)
> 4. `> [!example]-` — real instance (foldable, with numbered steps)
> 5. `> [!tip]` or `> [!warning]` — design insight or caution (if applicable)
>
> This pattern provides: scannable headers (info), structured data (table), context (abstract), proof (foldable example), and guidance (tip/warning).

> [!example]- **Bug report pattern** (from Methodology bugs section)
> Each bug gets:
> 1. `> [!bug]-` — foldable with title showing bug name + design input + version
> 2. Inside: what happened, how it was found, what the fix was
>
> Collapsed view shows all 7 bugs as a scannable list. Expanded view shows full detail per bug.

> [!example]- **Worked example pattern** (from Model Selection section)
> Each worked example gets:
> 1. `> [!example]-` — foldable with title describing the scenario
> 2. Inside: condition evaluation table (dimension | value | why)
> 3. `> [!success]` — the result (which model was selected and what it produces)
>
> Foldable so the reader sees "2 worked examples available" without being overwhelmed.

### Context 3: Remark / Docusaurus (for public docs)

A different formatting context for web-facing documentation. NOT for the wiki — for `docs/` content rendered via Docusaurus or similar static site generators.

> [!info] **Remark Directives**
> remark-directive adds three syntax types for custom markdown extensions:
>
> **Container directive** (multi-line block):
> ```markdown
> :::note[Custom Title]
> Content inside the container.
> Can span multiple lines.
> :::
> ```
>
> **Leaf directive** (single-line):
> ```markdown
> ::youtube[Video Title]{#dQw4w9WgXcQ}
> ```
>
> **Text directive** (inline):
> ```markdown
> :abbr[HTML]{title="HyperText Markup Language"}
> ```

> [!info] **Tabs** (via remark-directive)
> ```markdown
> :::tabs
> ::tab[JavaScript]
> ```js
> console.log('hello');
> ```
> ::tab[Python]
> ```python
> print('hello')
> ```
> :::
> ```

> [!info] **Admonitions** (Docusaurus equivalent of Obsidian callouts)
> ```markdown
> :::tip
> Helpful guidance here.
> :::
>
> :::danger
> Critical warning here.
> :::
> ```
>
> The mapping: `:::tip` = `> [!tip]`, `:::danger` = `> [!danger]`, `:::note` = `> [!note]`

> [!abstract] **Key distinction**
> - **Obsidian callouts** (`> [!type]`) = blockquote-based. For the wiki.
> - **Remark directives** (`:::type`) = container-based. For public docs.
> - Both achieve similar visual results with different syntax.
> - Content CAN be converted between them with tooling (remark plugins).

> [!info] **The Remark Ecosystem**
> remark is a markdown processor with 150+ plugins operating on ASTs (abstract syntax trees):
> - **remark-gfm**: GitHub Flavored Markdown (tables, strikethrough, task lists)
> - **remark-frontmatter**: YAML/TOML frontmatter parsing
> - **remark-directive**: custom containers, tabs, component injection
> - **remark-toc**: auto-generated table of contents
> - **remark-lint**: markdown style checking
> - **remark-rehype**: markdown → HTML bridge
> - **MDX**: markdown + JSX for React component embedding
>
> For projects using Docusaurus, remark plugins extend markdown into a full component system. This is not used in Obsidian but is the path for rendering wiki content on the web.

### CSS Customization

> [!info] **CSS Snippets**
> `.obsidian/snippets/` — any `.css` file here is loaded by Obsidian.
>
> **Custom callout types:**
> ```css
> .callout[data-callout="model"] {
>     --callout-color: 0, 120, 200;
>     --callout-icon: lucide-box;
> }
> ```
> Icons from [lucide.dev](https://lucide.dev). Colors as RGB 0-255.
>
> **Per-page styling via cssclasses:**
> ```css
> .model-page h2 { border-bottom: 2px solid var(--interactive-accent); }
> .model-page table { font-size: 0.9em; }
> ```
> Apply with `cssclasses: [model-page]` in frontmatter.
>
> **Other customizations:**
> - Table styling (borders, alternating rows, compact mode)
> - Tag colors
> - Graph view node colors (already configured in this wiki)
> - Heading hierarchy visual weight

### Graceful Degradation

What happens when wiki content is viewed OUTSIDE Obsidian:

| Feature | In Obsidian | In GitHub | In VS Code | In plain text |
|---------|------------|-----------|-----------|---------------|
| `**bold**` | **bold** | **bold** | **bold** | **bold** |
| `==highlight==` | Yellow background | Plain text with `==` | Plain text with `==` | Plain text with `==` |
| `> [!tip] Title` | Styled colored box | Blockquote with `[!tip]` prefix | Blockquote | `>` prefixed text |
| `[[Page Title]]` | Clickable link | Plain text `[[Page Title]]` | Plain text | Plain text |
| `![[embed]]` | Embedded content | Plain text | Plain text | Plain text |
| Mermaid blocks | Rendered diagram | Rendered diagram | Code block | Code block |
| `$math$` | Rendered formula | Plain text | Plain text | Plain text |
| `%% comment %%` | Hidden | Visible as text | Visible | Visible |

> [!warning] **Design constraint**
> Core content MUST be readable without Obsidian. Callouts degrade to blockquotes (still readable). Wikilinks degrade to plain text (still shows the page name). The INFORMATION survives; the STYLING doesn't. This means: never put critical content ONLY in a callout title — always include it in the body too.

### Compatibility Matrix

| Feature | Standard MD | GFM | Obsidian | Remark | Docusaurus |
|---------|-----------|-----|----------|--------|------------|
| Bold/italic/strike | ✓ | ✓ | ✓ | ✓ | ✓ |
| Tables | ✗ | ✓ | ✓ | plugin | ✓ |
| Task lists | ✗ | ✓ | ✓ | plugin | ✓ |
| Highlight (`==`) | ✗ | ✗ | ✓ | plugin | plugin |
| Callouts (`> [!type]`) | ✗ | ✗ | ✓ | plugin | ✗ |
| Admonitions (`:::type`) | ✗ | ✗ | ✗ | plugin | ✓ |
| Wikilinks (`[[]]`) | ✗ | ✗ | ✓ | plugin | plugin |
| Embeds (`![[]]`) | ✗ | ✗ | ✓ | ✗ | ✗ |
| Math/LaTeX | ✗ | ✗ | ✓ | plugin | ✓ |
| Mermaid | ✗ | ✓ | ✓ | plugin | ✓ |
| Footnotes | ✗ | ✗ | ✓ | plugin | ✓ |
| Comments (`%%`) | ✗ | ✗ | ✓ | ✗ | ✗ |
| Properties/frontmatter | ✗ | ✗ | ✓ | plugin | ✓ |
| cssclasses | ✗ | ✗ | ✓ | ✗ | ✗ |
| Block references | ✗ | ✗ | ✓ | ✗ | ✗ |
| Canvas | ✗ | ✗ | ✓ | ✗ | ✗ |
| Tabs | ✗ | ✗ | ✗ | plugin | ✓ |
| Custom directives (`:::`) | ✗ | ✗ | ✗ | plugin | ✓ |
| MDX/JSX components | ✗ | ✗ | ✗ | plugin | ✓ |

## Open Questions

- Should we create custom callout types via CSS snippets (e.g., `[!model]`, `[!stage]`, `[!instance]`) or keep to the 8 built-in types? (Requires: testing whether custom types add value or add confusion)
- Should `cssclasses` be standardized per page type (all model pages get `model-page`, all lessons get `lesson-page`)? (Requires: designing the CSS snippet and testing in Obsidian)
- How should wiki content be converted for Docusaurus rendering if needed? Callouts → admonitions, wikilinks → markdown links. (Requires: remark plugin development or selection)
- Should Mermaid diagrams be used for model selection flows? (Requires: testing readability of complex Mermaid charts in Obsidian)

## Relationships

- BUILDS ON: [[Model: LLM Wiki]] (content structure is the foundation; design is the visual layer)
- BUILDS ON: [[LLM Wiki Standards — What Good Looks Like]] (quality standards inform design patterns)
- RELATES TO: [[Design.md Pattern]] (DESIGN.md is for UI systems; this model is for wiki pages — same principle, different domain)
- RELATES TO: [[Infrastructure as Code Patterns]] (CSS snippets and cssclasses are IaC for visual design)
- RELATES TO: [[Model: Methodology]] (the methodology model page is the first to use the callout vocabulary extensively)
- ENABLES: All model pages (the callout vocabulary applies to every page in the wiki)

## Backlinks

[[Model: LLM Wiki]] (content structure is the foundation; design is the visual layer)]]
[[LLM Wiki Standards — What Good Looks Like]] (quality standards inform design patterns)]]
[[Design.md Pattern]] (DESIGN.md is for UI systems; this model is for wiki pages — same principle, different domain)]]
[[Infrastructure as Code Patterns]] (CSS snippets and cssclasses are IaC for visual design)]]
[[Model: Methodology]] (the methodology model page is the first to use the callout vocabulary extensively)]]
[[All model pages (the callout vocabulary applies to every page in the wiki)]]

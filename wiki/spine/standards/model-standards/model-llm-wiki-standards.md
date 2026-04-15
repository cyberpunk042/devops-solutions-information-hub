---
title: LLM Wiki Standards — What Good Looks Like
aliases:
  - "LLM Wiki Standards — What Good Looks Like"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-09
updated: 2026-04-11
sources: []
tags: [standards, quality, examples, wiki-model, best-practices, gold-standard]
---

# LLM Wiki Standards — What Good Looks Like

> [!tip] AI Quick Start — What You Do With This Page
>
> 1. **Before creating any wiki page**: find your page type in the "Per-Type Standards Index" table below
> 2. **Read the dedicated standards doc** for that type (e.g., [[concept-page-standards|Concept Page Standards]] for concept pages)
> 3. **Look at the exemplar** referenced in the standards doc — your page should LOOK like that
> 4. **Check the anti-patterns table** at the bottom — are you about to make a known mistake?
> 5. **Three properties of every good page**: SPECIFIC (data points, not vague claims), CONNECTED (rich relationships), ACTIONABLE (reader knows what to do)

## Summary

This page defines the quality bar for every page type in the LLM Wiki model. For each type, it identifies the gold-standard example from this wiki, explains WHY it's the standard, and extracts the concrete patterns that make it good. Use this when creating new pages — don't just follow the template, match the standard.

## Key Insights

- A template defines STRUCTURE (which sections to include). A standard defines QUALITY (what good content looks like in each section).
- The difference between a seed page and a growing page is not length — it's evidence density, specificity, and actionability.
- Every claim must point to a source. Every example must be concrete. Every insight must be stated plainly, not hinted at.
> [!tip] The Three Properties of a Gold-Standard Page
> The best pages in the wiki share three properties: they are SPECIFIC (data points, not vague claims), they are CONNECTED (rich relationships to other pages), and they are ACTIONABLE (the reader knows what to do after reading).

## Deep Analysis

### Per-Type Standards System

Every page type now has its own dedicated standards document in `wiki/spine/standards/`. Each standards doc includes: section-by-section quality bar, gold-standard exemplar with reasoning, common failures, content thresholds from `wiki/config/artifact-types.yaml`, and template reference.

> [!info] Per-Type Standards Index
>
> | Type | Standards Doc | Exemplar |
> |------|--------------|----------|
> | concept | [[concept-page-standards|Concept Page Standards]] | [[methodology-framework|Methodology Framework]] |
> | source-synthesis | [[source-synthesis-page-standards|Source-Synthesis Page Standards]] | [[src-context-mode|Synthesis — Context Mode — MCP Sandbox for Context Saving]] |
> | comparison | [[comparison-page-standards|Comparison Page Standards]] | [[cross-domain-patterns|Cross-Domain Patterns]] |
> | reference | [[reference-page-standards|Reference Page Standards]] | [[methodology-adoption-guide|Methodology Adoption Guide]] |
> | deep-dive | [[deep-dive-page-standards|Deep-Dive Page Standards]] | [[adoption-guide|Adoption Guide — How to Use This Wiki's Standards]] |
> | lesson | [[lesson-page-standards|Lesson Page Standards]] | [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] |
> | pattern | [[pattern-page-standards|Pattern Page Standards]] | [[plan-execute-review-cycle|Plan Execute Review Cycle]] |
> | decision | [[decision-page-standards|Decision Page Standards]] | [[execution-mode-edge-cases|Decision — Execution Mode Edge Cases]] |
> | domain-overview | [[domain-overview-page-standards|Domain Overview Page Standards]] | [[cross-domain-domain-overview|Cross-Domain — Domain Overview]] |
> | evolution | [[evolution-page-standards|Evolution Page Standards]] | [[methodology-evolution-history|Evolution — Methodology System]] |
> | learning-path | [[learning-path-page-standards|Learning Path Page Standards]] | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |
> | operations-plan | [[operations-plan-page-standards|Operations Plan Page Standards]] | [[wiki-post-ingestion-operations-plan|Operations Plan — Wiki Post-Ingestion Validation]] |
> | epic | [[epic-page-standards|Epic Page Standards]] | [[E003-artifact-type-system|Artifact Type System]] |
> | task | [[task-page-standards|Task Page Standards]] | [[T001-test-openai-backend|Test OpenAI backend with LocalAI]] |
> | note | [[note-page-standards|Note Page Standards]] | [[2026-04-09-directive-models-are-not-documents|Models Are Not Documents — They Must Be Usable Systems]] |

The summaries below are quick reference. For full quality bars, common failures, and styling requirements, read the dedicated standards doc.

---

### Exemplar Policy

> [!info] How exemplars are chosen and presented — policy governing all 15+ per-type standards pages
>
> This is the cross-cutting policy every per-type standards page follows. Resolves operator decision queue **Q9 (BEST vs TYPICAL)**, **Q10 (annotation format)**, and **Q17 (inline vs companion)**. If you are creating a new standards page, follow this policy.
>
> | Dimension | Policy | Rationale |
> |-----------|--------|-----------|
> | **Selection** | **Best available page, not typical.** Standards should RAISE the bar, not describe the average. The exemplar is aspirational: "this is what good looks like at its best right now." | A typical-good exemplar freezes mediocrity as the target. An aspirational exemplar creates upward pull. |
> | **Placement** | **Inline in the standards page, not companion.** The standards page and the annotated exemplar live together — the reader sees rule + demonstration in one place. | Companion documents break the teach-by-example loop. The reader shouldn't have to click to another page to see the standard demonstrated. |
> | **Format** | **Foldable `> [!example]- Full Walkthrough — Why Each Section Works`** with numbered annotation points per structural element (frontmatter, summary, key sections, evidence/analysis, relationships). Minimum 5 annotation points per exemplar. | Standardized format across 15+ standards pages makes every annotation scannable and comparable. Foldable so the standards page stays navigable; readers expand when they want depth. |
> | **Annotation content** | **Explain WHY, not WHAT.** An annotation "has 8 evidence items" is useless — the reader can count. "Each evidence item has bold source + specific data + source reference, which is what makes the convergence claim credible" teaches. | Annotations that restate the visible content are noise. The teaching happens when the annotation reveals the rule behind the choice. |
> | **Honest improvement notes** | **Every exemplar MUST end with "What could still improve"** — honest assessment of what the exemplar still lacks, even though it is the best available. | Prevents exemplars from becoming sacred, frozen, unquestionable. Documents the improvement direction. Aligns with operator's "none of this is static" stance. |
> | **Single-best vs span of exemplars** | **Default: single best exemplar.** Use a span of exemplars ONLY when the page type's "good" shape varies structurally by instance (e.g., session-handoff varies by session shape; not all handoffs should look the same). Document WHY if using span. | Most page types have one optimal shape (lesson, pattern, decision, concept, reference). Shape-dependent types need to show the range to teach correctly. |
> | **Self-validation** | **The standards page itself MUST pass the quality bar it defines.** If a standard says "≥3 evidence items," the standards page's own Evidence/Insights sections must demonstrate that. | Preach by example. A standards page that violates its own rules is worse than no standards page. |
>
> **When to update an exemplar:** when a new page of that type clearly surpasses the current exemplar on multiple dimensions, OR when the current exemplar has been refactored in ways that invalidate the annotation. Replacing an exemplar is a decision that should be logged in the `updated:` frontmatter field of the standards page.

---

### Template Policy

> [!info] How templates are structured — policy governing all files in wiki/config/templates/
>
> This is the cross-cutting policy every page template follows. Resolves operator decision queue **Q11 (structure vs structure+example split)**. If you are creating or editing a template, follow this policy. Live templates: `wiki/config/templates/*.md` (18 page types) + `wiki/config/templates/methodology/*.md` (7 methodology artifacts).
>
> | Dimension | Policy | Rationale |
> |-----------|--------|-----------|
> | **Structure** | **UNIFIED, not two-section.** The structure IS the example. One canonical skeleton with rich example content inside HTML comments. Do NOT split into "structure section" + "example section" — this produces duplicate headers when scaffolded and drifts over time. | Per E012 inline resolution 2026-04-13: "the structure IS the example. One section, rich content." Templates with both structure and separate examples developed duplicate `## Evidence` / `## Insight` headers when edited by different agents (observed in `lesson.md`, `reference.md`). |
> | **Example placement** | **Inside HTML comments** (`<!-- EXAMPLE: ... -->`), not as pre-filled live content. The agent reads the example, sees what good looks like, then replaces placeholders with real content. | Pre-filled live content risks being left in final pages. HTML comments are clearly not-real-content and get stripped/ignored by the rendered page if they survive. |
> | **Example content quality** | **Concrete and specific** — names actual projects/data/files that the wiki has synthesized, not hypothetical "Foo/Bar." The example SHOULD look like a real wiki page from the corpus. | A template example that says "replace with your domain" teaches less than one that shows "TypeScript \| Scaffold empty modules before writing business logic; prevents type-coupling creep." The concrete example shows what the abstract rule LOOKS LIKE when applied. |
> | **Placeholders** | **`{{double-brace}}` markers** for fields the agent must replace (title, date, domain, derived_page_N). Scaffolder substitutes these at generation time. Everything else stays — agent may edit, but doesn't HAVE to. | Typed substitution points keep mechanical fields (frontmatter) deterministic while keeping content fields (example narratives) as guidance. |
> | **Self-validation** | **Scaffolding from the template produces a page that passes `pipeline post` with 0 errors on first run.** If a template's example content violates the page type's standards (missing required section, insufficient word count), the template is bugged — not the agent. | Preach by example at the template level. A template that scaffolds to a failing page teaches the agent that failure is acceptable. |
> | **Styling callouts** | **Match the page-type standard's required callouts** — e.g., lesson templates MUST show `> [!warning]` or `> [!tip]` wrapping the Insight example, because the lesson standard requires that callout on the real page. | The template demonstrates compliance with the standard it scaffolds. If the standard requires semantic callouts, the template must show them. |
> | **Methodology templates** | **Same policy, applied to `wiki/config/templates/methodology/*.md`.** These scaffold methodology documents (ADR, requirements-spec, design-plan, etc.) — not wiki page types. They inherit structure from their parent wiki type (concept/reference/decision) and layer methodology-specific sections on top. | Methodology templates are specialized instances of wiki page types, not a separate template system. They validate against the same wiki-schema + artifact-types.yaml rules. |
>
> **Anti-patterns observed in the corpus** (flagged for E012 cleanup):
>
> - `wiki/config/templates/lesson.md` — has `## Evidence` heading twice (once at line 33 with HTML comment, once at line 83 with live example callout). Scaffolds to a page with duplicate headers.
> - `wiki/config/templates/reference.md` — has HTML-comment example AND live example section outside comments. Same risk: duplicate or conflicting structure on scaffold.
>
> **Gold-standard template examples:**
> - [decision.md](wiki/config/templates/decision.md) — rich `EXAMPLE:` blocks inside HTML comments for every section. Concrete names (MCP vs CLI decision, work hierarchy decision) drawn from real wiki pages. No duplicate sections.
> - [pattern.md](wiki/config/templates/pattern.md), [operations-plan.md](wiki/config/templates/operations-plan.md) — similar clean structure per E012 classification ("ALREADY RICH").

---

### Gold Standard: Concept Page

**Reference**: [[methodology-framework|Methodology Framework]] — 347 lines, 17 relationships

What makes it the standard:
- **Key Insights section has 8 discrete, numbered insights** — each is a self-contained statement, not a vague bullet. "Models are selected per-condition" not "models can be flexible."
- **Deep Analysis has 8 subsections** — each covering a distinct facet of the concept. Not one long essay — structured sub-topics.
- **Every subsection defines a concrete mechanism** — "Model Selection" explains the 5 condition dimensions (task type, project phase, domain, scale, current state). Not "models can be selected based on various conditions."
- **Open Questions are specific** — "Can model selection be encoded as a declarative config rather than imperative logic?" not "What else could we do?"
- **Relationships use precise verbs** — CONTAINS, IMPLEMENTS, EXTENDS — not just RELATES TO for everything.

**The bar for a concept page**: if someone reads only the Key Insights, they should understand the concept well enough to explain it to a colleague. If they read Deep Analysis, they should be able to IMPLEMENT it.

### Gold Standard: Source-Synthesis Page

**Reference**: [[src-context-mode|Synthesis — Context Mode — MCP Sandbox for Context Saving]] — 254 lines from a 1,057-line source

What makes it the standard:
- **The raw source was 1,057 lines. The synthesis is 254.** Not a 60-line summary — a 254-line extraction that captures the MECHANISM, not just the surface.
- **11 Key Insight subsections** — each covering a distinct aspect: sandbox tools, FTS5/BM25 knowledge base, session continuity, 12-platform matrix, benchmarks, Think in Code paradigm, routing enforcement gap, security model, OpenClaw integration, two-layer optimization, privacy.
- **Concrete data points throughout** — "315 KB becomes 5.4 KB. 98% reduction." "Playwright snapshot: 56 KB. After 30 minutes, 40% of context gone." Not "significant reduction."
- **The actual instance was examined** — not just the README. The synthesis was REWRITTEN after the first version was caught being surface-level (only 60 lines from first chunk).
- **Platform comparison table** — 12 platforms compared across hook support, session continuity, routing enforcement. Structured data, not prose.

**The bar for a source-synthesis page**: a reader should be able to DECIDE whether to use this tool/pattern/technique after reading the synthesis alone, without needing to read the raw source. If they need to read the original to understand it, the synthesis failed.

### Gold Standard: Lesson Page

**Reference**: [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] — 122 lines, 9 relationships

What makes it the standard:
- **Summary states the lesson in ONE sentence** that is immediately actionable: "CLI tools paired with skill files consistently outperform MCP server integrations on token cost and output accuracy."
- **Context section lists 5 specific trigger conditions** — not "this is useful in many situations." Each trigger is a concrete scenario (e.g., "Debugging unexplained hallucinations... looking for root causes beyond prompt quality").
- **Insight section explains the MECHANISM** — WHY CLI beats MCP, not just THAT it does. Schema tokens from unused tools occupy space that could hold task context. This is "context pollution" — high-entropy JSON boilerplate displacing high-signal task context.
- **Evidence section has 8 discrete evidence items**, each with:
  - A **bold label** identifying the source
  - A **specific claim** with data (e.g., "12x cost differential," "CLI was both cheaper and more accurate," "3x more features")
  - A **sourcing parenthetical** (e.g., `(src-claude-code-accuracy-tips)`)
- **Applicability names 4 specific domains** where the lesson applies, AND has a "When MCP is still the right choice" section with 4 counterexamples.
- **CONTRADICTS relationship** — the lesson explicitly contradicts the "default assumption that MCP is the standard tool integration pattern." This is brave — most pages only use soft verbs.

**The bar for a lesson page**: the Evidence section must contain AT LEAST 3 independent data points from different sources. If a lesson has only one source, it's an observation, not a lesson. The Insight section must explain the MECHANISM (why), not just the observation (what).

### Gold Standard: Pattern Page

**Reference**: [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]] — 176 lines, 13 relationships

What makes it the standard:
- **The `instances` frontmatter field lists 4 concrete occurrences** — each with `page` (where to find it) and `context` (how it manifests there). Not "this appears in many projects" — WHICH projects and HOW.
- **Pattern Description has exit criteria per stage** — Scaffold is done when direction is set. Foundation is done when there's a single entry point. Infrastructure is done when the base is in place. Features is done when specialized value is delivered. These are TESTABLE criteria.
- **Instances section expands each occurrence** into a multi-paragraph deep dive showing the stage-by-stage progression in that project.
- **When Not To section is honest** — "This pattern assumes you have the luxury of ordered stages. In a production emergency (hotfix), you skip directly to Features."
- **The pattern is declared RECURSIVE** — it applies at project level, feature level, component level. This elevates it from a simple sequence to a fractal principle.

**The bar for a pattern page**: MUST have ≥2 concrete instances with page references. A pattern without instances is a hypothesis. The When Not To section must be as thoughtful as When To Apply — a pattern that supposedly applies everywhere is not useful.

### Gold Standard: Decision Page

**Reference**: [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]] — 121 lines, 9 relationships

What makes it the standard:
- **Decision section is ONE clear statement** — "Default to CLI+Skills for project-internal tooling. Use MCP for external service bridges and cross-conversation tool discovery."
- **Alternatives section lists 3 rejected options** — each with a specific reason for rejection. Not "we considered other options" — WHICH options and WHY they lost.
- **Rationale is evidence-backed** — 12x cost differential, Playwright CLI vs MCP proof video, Google Trends signal, multiple independent sources converging. Not "we felt this was better."
- **Reversibility is explicit** — `reversibility: easy` with explanation: "swap a config." This tells the reader the cost of being wrong.
- **Dependencies section explains downstream impact** — what changes if this decision is reversed.

**The bar for a decision page**: the Alternatives section must have ≥2 alternatives with concrete reasons for rejection. The Rationale must reference specific evidence, not general reasoning. Reversibility must be honest — don't claim "easy" if it requires refactoring.

### Gold Standard: Comparison Page

**Reference**: [[cross-domain-patterns|Cross-Domain Patterns]] — 189 lines, 10 relationships

What makes it the standard:
- **Comparison Matrix is a TABLE** — not paragraphs of prose. Columns: pattern name, domains it appears in, instances, underlying constraint. Each row is a data point.
- **Deep Analysis expands each matrix row** into a subsection with instance-level comparison tables.
- **The comparison DISCOVERS something** — the 6 patterns reduce to 3 underlying constraints (bounded context, probabilistic LLM, deployment drift). The comparison is not just listing — it's synthesizing.

**The bar for a comparison page**: the Comparison Matrix MUST be a markdown table with ≥3 rows and ≥3 columns. If you can't structure it as a table, it's not ready to be a comparison page — keep it as a concept with prose analysis.

### Gold Standard: Epic

**Reference**: [[E003-artifact-type-system|Artifact Type System]] — 105 lines, 95% readiness, all 5 stages complete

What makes it the standard:
- **Goals are concrete and measurable** — "Create templates for all 8 page types currently missing" not "improve templates."
- **Done When uses checkboxes with specific outputs** — "Templates exist for all page types agents create" can be verified with `ls wiki/config/templates/`.
- **Dependencies are explicit** — "None — this is the foundation epic."
- **Artifacts list tracks ALL stage outputs** — 22 artifacts across document, design, scaffold, implement. Every deliverable is named.
- **Readiness reflects actual stage completion** — 95% because all 5 stages are done, pending operator review.

Also strong: [[E001-local-inference-engine|Local Inference Engine (Subsystem 3)]] — good Blocked section, good artifact tracking from document stage.

### Gold Standard: Task

**Reference**: [[T001-test-openai-backend|Test OpenAI backend with LocalAI]] — 33 lines

What makes it the standard:
- **Short and focused** — a task is NOT an essay. Summary + Done When, that's it.
- **Done When items are VERIFIABLE** — "Generated page passes `pipeline post` validation" can be checked with a command. "Make it work well" cannot.
- **Frontmatter tracks state fully** — status, priority, epic, task_type, current_stage, readiness, estimate. Everything a project manager needs.

### Gold Standard: Note (Directive)

**Reference**: [[2026-04-09-directive-models-are-not-documents|Models Are Not Documents — They Must Be Usable Systems]] — 49 lines

What makes it the standard:
- **Operator's words are VERBATIM** — quoted exactly, not paraphrased. This is sacrosanct.
- **Interpretation section is the agent's understanding** — clearly separated from the operator's words.
- **Summary is actionable** — states the problem and what needs to change, not just "the user said something."

### Gold Standard: Reference Page

**Reference**: [[methodology-adoption-guide|Methodology Adoption Guide]] — 259 lines, 8 relationships

What makes it the standard:
- **Progressive disclosure structure** — 4 tiers of adoption, each more detailed than the last. Reader finds their tier and stops. Doesn't force experts through basics.
- **Concrete code examples** — YAML blocks, bash commands, CLAUDE.md snippets. Not "configure your project" — shows EXACTLY what to configure.
- **Per-domain quick starts** — TypeScript, Python/wiki, Infrastructure each get their own callout with 4-step checklist. Actionable in minutes.
- **Invariants section at the bottom** — rules that apply at ALL tiers. Ensures the core principles survive even at Tier 1 adoption.

**The bar for a reference page**: the reader should be able to LOOK UP what they need and ACT on it without reading the entire page. If the page must be read linearly to be useful, it's a concept, not a reference.

### Gold Standard: Deep-Dive Page

**Reference**: [[adoption-guide|Adoption Guide — How to Use This Wiki's Standards]] — 325 lines

What makes it the standard:
- **Substantial depth** (325 lines) — a deep-dive earns its name through exhaustive analysis, not surface coverage.
- **5 core principles in Key Insights** — each principle is a complete idea, not a pointer to another section.
- **Multi-subsection Deep Analysis** — step-by-step walkthrough with recursive framework explanation.
- **Multiple callout types** (abstract, warning, tip) — structural variety aids scanning.

**The bar for a deep-dive page**: Deep Analysis must be ≥200 words with ≥3 subsections. If the analysis fits in one section, it's a concept, not a deep-dive. Callouts are REQUIRED — deep-dives must structure their analysis visually.

### Gold Standard: Domain Overview Page

**Reference**: [[cross-domain-domain-overview|Cross-Domain — Domain Overview]] — 126 lines

What makes it the standard:
- **State of Knowledge has 3 tiers** — Authoritative, Good, and Thin coverage. Honest assessment of where the domain stands.
- **Maturity Map groups pages by maturity** — seed, growing, mature, canonical. Shows the domain's internal quality distribution.
- **Gaps section is specific and actionable** — names exactly what's missing, not "more research needed."
- **Key Pages list is curated** — recommended reading order, not alphabetical dump.

**The bar for a domain overview page**: the Maturity Map must reflect the ACTUAL distribution of pages in the domain. Gaps must name specific missing topics. Key Pages must have a recommended reading order.

### Gold Standard: Evolution Page

**Reference**: [[methodology-evolution-history|Evolution — Methodology System]] — 120 lines

What makes it the standard:
- **Timeline entries have dates AND significance** — not just "something happened" but why it mattered. Each entry explains the impact.
- **Key Shifts section identifies turning points** — not a restatement of the timeline but an interpretation: what CHANGED direction?
- **Current State is honest** — states what's done AND what's next. Not just a victory lap.

**The bar for an evolution page**: Timeline must have ≥5 dated entries. Key Shifts must identify ≥2 turning points. Current State must name next frontiers.

### Gold Standard: Learning Path Page

**Reference**: [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] — 68 lines

What makes it the standard:
- **Sequence has 8 ordered pages** — each with a `[[wikilink]]` AND a 1-sentence annotation explaining WHY this page is at this position.
- **Prerequisites are specific** — not "basic knowledge" but exact pages to read first.
- **Outcomes are testable** — "you should be able to select the correct methodology model for any task type" is verifiable. "You should understand methodology" is not.

**The bar for a learning-path page**: Sequence must have ≥3 pages in recommended order. Each page must have a 1-sentence annotation. Outcomes must be testable capabilities, not vague understanding.

### Gold Standard: Operations Plan Page

**Reference**: [[wiki-post-ingestion-operations-plan|Operations Plan — Wiki Post-Ingestion Validation]] — 90 lines

What makes it the standard:
- **Every step has 4 components** — Action, Expected output, Validation, Rollback. A "dumb" agent can follow this mechanically.
- **Prerequisites are checkboxes** — verifiable BEFORE step 1 begins.
- **Rollback section covers partial failure** — what to do if step 3 fails after steps 1-2 succeeded.
- **Completion Criteria are checkboxes** — verifiable AFTER all steps complete.

**The bar for an operations plan**: ≥3 sequential steps. Each step has Action + Expected output + Validation + Rollback. A different agent could follow this plan and get the same result. If judgment is required, it's a design plan, not an operations plan.

### Annotated Exemplar: [[model-llm-wiki|Model — LLM Wiki]]

> [!example]- Full Walkthrough — Why the LLM Wiki Model Exemplifies Its Own Standards
>
> **1. Schema as product** — The model defines 9 required frontmatter fields, 22 optional fields, and a typed page catalog. Every page in the wiki validates against this schema. ← The schema IS the standard. A wiki where frontmatter is optional decays into inconsistency. The model doesn't just describe the schema — it explains WHY each field narrows agent behavior.
>
> **2. Three core operations** — Ingest, Query, Lint are presented as a table with tooling per operation. Not "the wiki does many things" but three named operations with exact tools. ← Operations are the verbs of the system. Naming them constrains scope — anything that isn't ingest/query/lint is a feature request, not a core operation.
>
> **3. Knowledge layers** — L0 (raw) through L6 (decision) + Spine + Backlog + Log + Config, each with page types and examples. ← Progressive distillation is the model's core insight. Each layer is denser than the previous. The table makes the layer system concrete, not aspirational.
>
> **4. Honest State of Knowledge** — "Well-covered: schema validation, 3 core operations, maturity lifecycle." "Thin: multi-agent co-authoring untested, approaching 280-page scale ceiling." ← The model practices what it preaches: transparent about limitations. A model that claims completeness has stopped learning.
>
> **What could still improve:** The model has 566 lines — close to the threshold where it should consider splitting into a model page + a separate deep-dive on operations. The Key Insights section (4 bullets) is thin relative to the page's depth.

### Anti-Patterns — What Bad Looks Like

| Anti-Pattern | What it looks like | Why it fails |
|-------------|-------------------|-------------|
| **Surface synthesis** | 60-line page from a 1,000-line source | Missed 90% of the content. Layer 0 description, not Layer 1 understanding. |
| **Vague insights** | "This tool is useful for many things" | No specificity. Reader learns nothing actionable. |
| **Missing evidence** | Lesson with 0 data points | An opinion, not a lesson. Lessons require convergent evidence. |
| **RELATES TO everything** | 10 relationships, all "RELATES TO" | Lazy verbs. Use BUILDS ON, ENABLES, CONTRADICTS — they carry meaning. |
| **Prose comparison** | "X is good at A, Y is good at B" | Should be a matrix table. Prose comparisons can't be scanned. |
| **Task as essay** | 200-line task description | Tasks are atomic. If it needs that much text, it's an epic. |
| **Paraphrased directive** | "The user wanted us to improve quality" | Must be VERBATIM. The operator's exact words are the source of truth. |
| **No instances in patterns** | "This pattern appears everywhere" | WHERE? Name 2+ pages. A pattern without instances is a hypothesis. |
| **Overclaiming readiness** | "The model is complete" without evidence | Claiming done without running the quality gates is a methodology violation. |

## Open Questions

- Should there be a formal review process for promoting pages from growing to mature? Currently it's ad-hoc. (Requires: testing with a formal review workflow)
- What's the minimum Evidence count for a lesson to be credible? Currently suggested ≥3 independent sources. Is that right? (Requires: analysis of existing lesson quality vs evidence count)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Principles** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] · [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] · [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **Identity** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[model-llm-wiki|Model — LLM Wiki]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[methodology-framework|Methodology Framework]]
- RELATES TO: [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
- RELATES TO: [[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic, Not Isolated]]
- RELATES TO: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]

## Backlinks

[[model-llm-wiki|Model — LLM Wiki]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[methodology-framework|Methodology Framework]]
[[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
[[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic, Not Isolated]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
[[E003-artifact-type-system|Artifact Type System]]
[[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]]
[[comparison-page-standards|Comparison Page Standards]]
[[concept-page-standards|Concept Page Standards]]
[[decision-page-standards|Decision Page Standards]]
[[deep-dive-page-standards|Deep-Dive Page Standards]]
[[domain-overview-page-standards|Domain Overview Page Standards]]
[[e003-artifact-type-system-requirements|E003 Artifact Type System — Requirements Spec]]
[[e011-standards-exemplification-all-15-per-type-standards-with-inline-annotated-e|E011 — Standards Exemplification — All 15 Per-Type Standards with Inline Annotated Exemplars]]
[[evolution-page-standards|Evolution Page Standards]]
[[model-knowledge-evolution-standards|Evolution Standards — What Good Knowledge Promotion Looks Like]]
[[model-skills-commands-hooks-standards|Extension Standards — What Good Skills, Commands, and Hooks Look Like]]
[[learning-path-page-standards|Learning Path Page Standards]]
[[methodology-fundamentals|Learning Path — Methodology Fundamentals]]
[[lesson-page-standards|Lesson Page Standards]]
[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[methodology-system-map|Methodology System Map]]
[[model-wiki-design|Model — Wiki Design]]
[[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
[[new-content-must-integrate-into-existing-pages|New Content Must Integrate Into Existing Pages]]
[[operations-plan-page-standards|Operations Plan Page Standards]]
[[pattern-page-standards|Pattern Page Standards]]
[[model-quality-failure-prevention-standards|Quality Standards — What Good Failure Prevention Looks Like]]
[[reference-page-standards|Reference Page Standards]]
[[source-synthesis-page-standards|Source-Synthesis Page Standards]]
[[E006-standards-by-example|Standards-by-Example]]
[[methodology-artifact-taxonomy-research|Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research]]
[[model-wiki-design-standards|Wiki Design Standards — What Good Styling Looks Like]]

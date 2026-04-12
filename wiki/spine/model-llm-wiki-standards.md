---
title: "LLM Wiki Standards — What Good Looks Like"
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
> 2. **Read the dedicated standards doc** for that type (e.g., [[Concept Page Standards]] for concept pages)
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

Every page type now has its own dedicated standards document in `wiki/spine/standards/`. Each standards doc includes: section-by-section quality bar, gold-standard exemplar with reasoning, common failures, content thresholds from `config/artifact-types.yaml`, and template reference.

> [!info] Per-Type Standards Index
>
> | Type | Standards Doc | Exemplar |
> |------|--------------|----------|
> | concept | [[Concept Page Standards]] | [[Methodology Framework]] |
> | source-synthesis | [[Source-Synthesis Page Standards]] | [[Synthesis: Context Mode — MCP Sandbox for Context Saving]] |
> | comparison | [[Comparison Page Standards]] | [[Cross-Domain Patterns]] |
> | reference | [[Reference Page Standards]] | [[Methodology Adoption Guide]] |
> | deep-dive | [[Deep-Dive Page Standards]] | [[Adoption Guide — How to Use This Wiki's Standards]] |
> | lesson | [[Lesson Page Standards]] | [[CLI Tools Beat MCP for Token Efficiency]] |
> | pattern | [[Pattern Page Standards]] | [[Plan-Execute-Review Cycle]] |
> | decision | [[Decision Page Standards]] | [[Execution Mode Edge Cases]] |
> | domain-overview | [[Domain Overview Page Standards]] | [[Cross-Domain — Domain Overview]] |
> | evolution | [[Evolution Page Standards]] | [[Evolution: Methodology System]] |
> | learning-path | [[Learning Path Page Standards]] | [[Learning Path: Methodology Fundamentals]] |
> | operations-plan | [[Operations Plan Page Standards]] | [[Operations Plan: Wiki Post-Ingestion Validation]] |
> | epic | [[Epic Page Standards]] | [[Artifact Type System]] |
> | task | [[Task Page Standards]] | [[Test OpenAI backend with LocalAI]] |
> | note | [[Note Page Standards]] | [[Models Are Not Documents — They Must Be Usable Systems]] |

The summaries below are quick reference. For full quality bars, common failures, and styling requirements, read the dedicated standards doc.

---

### Gold Standard: Concept Page

**Reference**: [[Methodology Framework]] — 347 lines, 17 relationships

What makes it the standard:
- **Key Insights section has 8 discrete, numbered insights** — each is a self-contained statement, not a vague bullet. "Models are selected per-condition" not "models can be flexible."
- **Deep Analysis has 8 subsections** — each covering a distinct facet of the concept. Not one long essay — structured sub-topics.
- **Every subsection defines a concrete mechanism** — "Model Selection" explains the 5 condition dimensions (task type, project phase, domain, scale, current state). Not "models can be selected based on various conditions."
- **Open Questions are specific** — "Can model selection be encoded as a declarative config rather than imperative logic?" not "What else could we do?"
- **Relationships use precise verbs** — CONTAINS, IMPLEMENTS, EXTENDS — not just RELATES TO for everything.

**The bar for a concept page**: if someone reads only the Key Insights, they should understand the concept well enough to explain it to a colleague. If they read Deep Analysis, they should be able to IMPLEMENT it.

### Gold Standard: Source-Synthesis Page

**Reference**: [[Synthesis: Context Mode — MCP Sandbox for Context Saving]] — 254 lines from a 1,057-line source

What makes it the standard:
- **The raw source was 1,057 lines. The synthesis is 254.** Not a 60-line summary — a 254-line extraction that captures the MECHANISM, not just the surface.
- **11 Key Insight subsections** — each covering a distinct aspect: sandbox tools, FTS5/BM25 knowledge base, session continuity, 12-platform matrix, benchmarks, Think in Code paradigm, routing enforcement gap, security model, OpenClaw integration, two-layer optimization, privacy.
- **Concrete data points throughout** — "315 KB becomes 5.4 KB. 98% reduction." "Playwright snapshot: 56 KB. After 30 minutes, 40% of context gone." Not "significant reduction."
- **The actual instance was examined** — not just the README. The synthesis was REWRITTEN after the first version was caught being surface-level (only 60 lines from first chunk).
- **Platform comparison table** — 12 platforms compared across hook support, session continuity, routing enforcement. Structured data, not prose.

**The bar for a source-synthesis page**: a reader should be able to DECIDE whether to use this tool/pattern/technique after reading the synthesis alone, without needing to read the raw source. If they need to read the original to understand it, the synthesis failed.

### Gold Standard: Lesson Page

**Reference**: [[CLI Tools Beat MCP for Token Efficiency]] — 122 lines, 9 relationships

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

**Reference**: [[Scaffold → Foundation → Infrastructure → Features]] — 176 lines, 13 relationships

What makes it the standard:
- **The `instances` frontmatter field lists 4 concrete occurrences** — each with `page` (where to find it) and `context` (how it manifests there). Not "this appears in many projects" — WHICH projects and HOW.
- **Pattern Description has exit criteria per stage** — Scaffold is done when direction is set. Foundation is done when there's a single entry point. Infrastructure is done when the base is in place. Features is done when specialized value is delivered. These are TESTABLE criteria.
- **Instances section expands each occurrence** into a multi-paragraph deep dive showing the stage-by-stage progression in that project.
- **When Not To section is honest** — "This pattern assumes you have the luxury of ordered stages. In a production emergency (hotfix), you skip directly to Features."
- **The pattern is declared RECURSIVE** — it applies at project level, feature level, component level. This elevates it from a simple sequence to a fractal principle.

**The bar for a pattern page**: MUST have ≥2 concrete instances with page references. A pattern without instances is a hypothesis. The When Not To section must be as thoughtful as When To Apply — a pattern that supposedly applies everywhere is not useful.

### Gold Standard: Decision Page

**Reference**: [[Decision: MCP vs CLI for Tool Integration]] — 121 lines, 9 relationships

What makes it the standard:
- **Decision section is ONE clear statement** — "Default to CLI+Skills for project-internal tooling. Use MCP for external service bridges and cross-conversation tool discovery."
- **Alternatives section lists 3 rejected options** — each with a specific reason for rejection. Not "we considered other options" — WHICH options and WHY they lost.
- **Rationale is evidence-backed** — 12x cost differential, Playwright CLI vs MCP proof video, Google Trends signal, multiple independent sources converging. Not "we felt this was better."
- **Reversibility is explicit** — `reversibility: easy` with explanation: "swap a config." This tells the reader the cost of being wrong.
- **Dependencies section explains downstream impact** — what changes if this decision is reversed.

**The bar for a decision page**: the Alternatives section must have ≥2 alternatives with concrete reasons for rejection. The Rationale must reference specific evidence, not general reasoning. Reversibility must be honest — don't claim "easy" if it requires refactoring.

### Gold Standard: Comparison Page

**Reference**: [[Cross-Domain Patterns]] — 189 lines, 10 relationships

What makes it the standard:
- **Comparison Matrix is a TABLE** — not paragraphs of prose. Columns: pattern name, domains it appears in, instances, underlying constraint. Each row is a data point.
- **Deep Analysis expands each matrix row** into a subsection with instance-level comparison tables.
- **The comparison DISCOVERS something** — the 6 patterns reduce to 3 underlying constraints (bounded context, probabilistic LLM, deployment drift). The comparison is not just listing — it's synthesizing.

**The bar for a comparison page**: the Comparison Matrix MUST be a markdown table with ≥3 rows and ≥3 columns. If you can't structure it as a table, it's not ready to be a comparison page — keep it as a concept with prose analysis.

### Gold Standard: Epic

**Reference**: [[Artifact Type System]] — 105 lines, 95% readiness, all 5 stages complete

What makes it the standard:
- **Goals are concrete and measurable** — "Create templates for all 8 page types currently missing" not "improve templates."
- **Done When uses checkboxes with specific outputs** — "Templates exist for all page types agents create" can be verified with `ls config/templates/`.
- **Dependencies are explicit** — "None — this is the foundation epic."
- **Artifacts list tracks ALL stage outputs** — 22 artifacts across document, design, scaffold, implement. Every deliverable is named.
- **Readiness reflects actual stage completion** — 95% because all 5 stages are done, pending operator review.

Also strong: [[Local Inference Engine (Subsystem 3)]] — good Blocked section, good artifact tracking from document stage.

### Gold Standard: Task

**Reference**: [[Test OpenAI backend with LocalAI]] — 33 lines

What makes it the standard:
- **Short and focused** — a task is NOT an essay. Summary + Done When, that's it.
- **Done When items are VERIFIABLE** — "Generated page passes `pipeline post` validation" can be checked with a command. "Make it work well" cannot.
- **Frontmatter tracks state fully** — status, priority, epic, task_type, current_stage, readiness, estimate. Everything a project manager needs.

### Gold Standard: Note (Directive)

**Reference**: [[Models Are Not Documents — They Must Be Usable Systems]] — 49 lines

What makes it the standard:
- **Operator's words are VERBATIM** — quoted exactly, not paraphrased. This is sacrosanct.
- **Interpretation section is the agent's understanding** — clearly separated from the operator's words.
- **Summary is actionable** — states the problem and what needs to change, not just "the user said something."

### Gold Standard: Reference Page

**Reference**: [[Methodology Adoption Guide]] — 259 lines, 8 relationships

What makes it the standard:
- **Progressive disclosure structure** — 4 tiers of adoption, each more detailed than the last. Reader finds their tier and stops. Doesn't force experts through basics.
- **Concrete code examples** — YAML blocks, bash commands, CLAUDE.md snippets. Not "configure your project" — shows EXACTLY what to configure.
- **Per-domain quick starts** — TypeScript, Python/wiki, Infrastructure each get their own callout with 4-step checklist. Actionable in minutes.
- **Invariants section at the bottom** — rules that apply at ALL tiers. Ensures the core principles survive even at Tier 1 adoption.

**The bar for a reference page**: the reader should be able to LOOK UP what they need and ACT on it without reading the entire page. If the page must be read linearly to be useful, it's a concept, not a reference.

### Gold Standard: Deep-Dive Page

**Reference**: [[Adoption Guide — How to Use This Wiki's Standards]] — 325 lines

What makes it the standard:
- **Substantial depth** (325 lines) — a deep-dive earns its name through exhaustive analysis, not surface coverage.
- **5 core principles in Key Insights** — each principle is a complete idea, not a pointer to another section.
- **Multi-subsection Deep Analysis** — step-by-step walkthrough with recursive framework explanation.
- **Multiple callout types** (abstract, warning, tip) — structural variety aids scanning.

**The bar for a deep-dive page**: Deep Analysis must be ≥200 words with ≥3 subsections. If the analysis fits in one section, it's a concept, not a deep-dive. Callouts are REQUIRED — deep-dives must structure their analysis visually.

### Gold Standard: Domain Overview Page

**Reference**: [[Cross-Domain — Domain Overview]] — 126 lines

What makes it the standard:
- **State of Knowledge has 3 tiers** — Authoritative, Good, and Thin coverage. Honest assessment of where the domain stands.
- **Maturity Map groups pages by maturity** — seed, growing, mature, canonical. Shows the domain's internal quality distribution.
- **Gaps section is specific and actionable** — names exactly what's missing, not "more research needed."
- **Key Pages list is curated** — recommended reading order, not alphabetical dump.

**The bar for a domain overview page**: the Maturity Map must reflect the ACTUAL distribution of pages in the domain. Gaps must name specific missing topics. Key Pages must have a recommended reading order.

### Gold Standard: Evolution Page

**Reference**: [[Evolution: Methodology System]] — 120 lines

What makes it the standard:
- **Timeline entries have dates AND significance** — not just "something happened" but why it mattered. Each entry explains the impact.
- **Key Shifts section identifies turning points** — not a restatement of the timeline but an interpretation: what CHANGED direction?
- **Current State is honest** — states what's done AND what's next. Not just a victory lap.

**The bar for an evolution page**: Timeline must have ≥5 dated entries. Key Shifts must identify ≥2 turning points. Current State must name next frontiers.

### Gold Standard: Learning Path Page

**Reference**: [[Learning Path: Methodology Fundamentals]] — 68 lines

What makes it the standard:
- **Sequence has 8 ordered pages** — each with a [[wikilink]] AND a 1-sentence annotation explaining WHY this page is at this position.
- **Prerequisites are specific** — not "basic knowledge" but exact pages to read first.
- **Outcomes are testable** — "you should be able to select the correct methodology model for any task type" is verifiable. "You should understand methodology" is not.

**The bar for a learning-path page**: Sequence must have ≥3 pages in recommended order. Each page must have a 1-sentence annotation. Outcomes must be testable capabilities, not vague understanding.

### Gold Standard: Operations Plan Page

**Reference**: [[Operations Plan: Wiki Post-Ingestion Validation]] — 90 lines

What makes it the standard:
- **Every step has 4 components** — Action, Expected output, Validation, Rollback. A "dumb" agent can follow this mechanically.
- **Prerequisites are checkboxes** — verifiable BEFORE step 1 begins.
- **Rollback section covers partial failure** — what to do if step 3 fails after steps 1-2 succeeded.
- **Completion Criteria are checkboxes** — verifiable AFTER all steps complete.

**The bar for an operations plan**: ≥3 sequential steps. Each step has Action + Expected output + Validation + Rollback. A different agent could follow this plan and get the same result. If judgment is required, it's a design plan, not an operations plan.

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

## Relationships

- BUILDS ON: [[Model: LLM Wiki]]
- RELATES TO: [[Stage-Gate Methodology]]
- RELATES TO: [[Methodology Framework]]
- RELATES TO: [[Never Synthesize from Descriptions Alone]]
- RELATES TO: [[Shallow Ingestion Is Systemic, Not Isolated]]
- RELATES TO: [[The Agent Must Practice What It Documents]]

## Backlinks

[[Model: LLM Wiki]]
[[Stage-Gate Methodology]]
[[Methodology Framework]]
[[Never Synthesize from Descriptions Alone]]
[[Shallow Ingestion Is Systemic, Not Isolated]]
[[The Agent Must Practice What It Documents]]
[[Claude Code Standards — What Good Agent Configuration Looks Like]]
[[Comparison Page Standards]]
[[Concept Page Standards]]
[[Decision Page Standards]]
[[Deep-Dive Page Standards]]
[[Domain Overview Page Standards]]
[[Evolution Page Standards]]
[[Evolution Standards — What Good Knowledge Promotion Looks Like]]
[[Extension Standards — What Good Skills, Commands, and Hooks Look Like]]
[[Learning Path Page Standards]]
[[Lesson Page Standards]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Model: Wiki Design]]
[[Models Are Built in Layers, Not All at Once]]
[[Operations Plan Page Standards]]
[[Pattern Page Standards]]
[[Quality Standards — What Good Failure Prevention Looks Like]]
[[Reference Page Standards]]
[[Source-Synthesis Page Standards]]
[[Wiki Design Standards — What Good Styling Looks Like]]

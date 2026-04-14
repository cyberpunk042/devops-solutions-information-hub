# Session Handoff — 2026-04-14

> **Scope:** A multi-phase session covering: batch ingestion of 15 new sources through all 4 tiers, creation of the root documentation architecture (8 root .md files), three-layer agent context implementation, config architecture overhaul (methodology-profiles + Flexibility Principle + contribution policy), and resolution of ALL 8 P1 architecture decisions in the operator decision queue.
>
> **Audience:** The operator, future Claude sessions, and any agent who needs to understand what this day changed in the wiki.
>
> **How to read:** Start at "Executive Summary" for the one-screen view. Skip to "What Was Done (Phase by Phase)" for the detail. End with "How to Resume" for a fresh-agent checklist.

---

## Executive Summary

This session crystallized the wiki's architecture. When we started, the wiki had 297 pages, a 315-line CLAUDE.md doing the job of three files, an implicit "SDLC chain" naming that was a category error, and 73 unresolved architecture questions in the operator decision queue. When we finished, the wiki has **319 pages**, **2089 relationships**, **0 validation errors, 0 lint issues**, a properly layered 4-layer config architecture, 8 thematic root docs implementing the three-layer agent context pattern, a full Context File Taxonomy (8 dimensions), a trust-tiered contribution policy, and **all 8 P1 architecture decisions resolved** with concrete tooling changes to back each one.

Key outputs of the session:

- **16 source syntheses + 4 model integrations** from a batch ingestion (OpenSpec, spec-kit, BMAD-METHOD, Claude Agent SDK, Pydantic AI, AutoBE, HRM/TRM, 27 Questions, Claude Code patch gist, SKILL vs CLAUDE vs AGENTS, LLM architecture gallery, Vercel opensrc, code-review-graph, openclaw-billing-proxy, 7 Levels of Claude Code + RAG) — all accessible via `gateway query --page <title>` and the MCP `wiki_gateway_query` tool.
- **8 root-level .md files** implementing the three-layer architecture: README, AGENTS, CLAUDE (slimmed 315→107 lines), CONTEXT, ARCHITECTURE, DESIGN, TOOLS, SKILLS. Each file has ONE responsibility, audience, and loading mode.
- **1 spine reference page** formalizing the Context File Taxonomy — 8 independent dimensions every context file varies along, with a complete catalog of every source in the ecosystem and 5 worked examples.
- **1 spine reference page** (Root Documentation Map) tying the 8 root docs into the wiki graph.
- **3 evolved pages** distilled from convergent evidence in the batch ingestion: "If You Can Verify, You Converge" (lesson), "Three-Layer Agent Context Architecture" (pattern), "Specs-as-Code-Source Inverts the Traditional Hierarchy" (lesson).
- **New config layer — methodology-profiles/** — 4 profiles (stage-gated, spec-driven, agile-ai, test-driven) + README. Gives external standards (BMAD/SDD/spec-kit/TDD) a first-class home in config.
- **New domain profile** — knowledge.yaml (pure knowledge projects, no code).
- **New config** — contribution-policy.yaml — 4-tier trust model for agent write-back.
- **Thorough config README** — wiki/config/README.md (830 lines) documenting every config file.
- **Flexibility Principle** — documented in wiki/config/README.md: "the wiki is a menu, not a law". Nothing in wiki/config/ is mandatory for consuming projects.
- **Gateway tool improvements** — `query --profile`, `query --profiles`, `query --docs`, `contribute --contributor/--source/--reason`, `flow` walks through 8-step Goldilocks. Relationship auto-fixer in pipeline post automatically resolves bare title references to `[[slug|title]]` wikilinks.
- **Lint + parser fixes** — parse_relationships strips em-dash comments only AFTER ]], preserving titles like "Model — Methodology". Lint extracts slug side of `[[slug|title]]` format.

Everything is committed. Pipeline steady state verified across every change. No loose ends in the tooling.

---

## Session Context and Trajectory

### Where We Started

The day began with the operator asking *"regather context, long and deep."* The session that followed was not a feature sprint — it was a **crystallization**. The wiki had accumulated substantive knowledge across 297 pages but the architecture around it was implicit, inconsistent, and partially wrong. The naming of core concepts ("SDLC chain") was a category error. The CLAUDE.md file was 315 lines — well above ETH Zurich's 300-line harm threshold from the three-layer context research we had just ingested. The config directory was flat and unannotated. The operator decision queue had 73 questions; the first 8 (P1 Architecture Decisions) were blocking downstream work.

### The Arc

The session arc was roughly:

1. **Rediscovery and batch ingestion (Tier 1–4)** — processing 15 new sources the operator had provided from an earlier message. This phase surfaced new knowledge about external standards (BMAD, SDD, spec-kit, TDD), Claude API surfaces (Agent SDK, Managed Agents), and small-model breakthroughs (HRM, TRM, AutoBE). It also uncovered the *structural* problems in our own wiki — the CLAUDE.md monolith, the missing AGENTS.md, the implicit config layering.

2. **Infrastructure improvements triggered by the ingestion itself** — the ingestion couldn't proceed well until the pipeline could fetch GitHub repos deeply (not just READMEs) and auto-fix relationship wikilinks. Both were fixed mid-ingestion and committed. This is the "fix the tool, then use the tool" principle the operator had reinforced earlier.

3. **Knowledge integration** — synthesis pages produced from every source, with direct cross-links into the models and standards that needed the new evidence. Three strong-evidence convergent patterns distilled into evolved pages (lesson/pattern).

4. **Root documentation architecture** — the operator specifically asked for proper READMEs, AGENTS.md, CLAUDE.md, CONTEXT, DESIGN, ARCHITECTURE, TOOLS, SKILLS files with clear concerns. We implemented the full three-layer pattern from the batch ingestion evidence. CLAUDE.md went 315 → 107 lines.

5. **Wiring the root docs into the wiki graph** — new spine reference page (Root Documentation Map), gateway `query --docs` command, MCP `wiki_gateway_docs` tool. Root docs are now first-class citizens of the graph, discoverable via Obsidian, CLI, MCP.

6. **Operator decision queue, one question at a time** — starting with Q1 ("Should SDLC chains be YAML configs or wiki pages?"). Each question resolved by examining the current state, proposing options, getting operator input, and encoding the decision into config + tooling + docs. The process uncovered several deeper issues: Q1 revealed the "chain" category error; Q5 revealed that OpenArms's "5 cognitive contexts" was an oversimplification; Q7 revealed that the methodology document type system was already correct (just undocumented); Q8 revealed that the existing maturity-folder system WAS the trust model (just not declared).

7. **This handoff document** — preserving the work, the decisions, the trajectory, and the next steps.

### The Operator's Voice

Key corrections and framings from the operator during the session:

- *"do not minimize what I said... what you are talking about are overlay, what I am talking about is the definitions themselves"* — after I described domain profiles as overlays without addressing that methodology profiles were missing as a definition layer.
- *"chain are inside the methodology"* — clarifying that "chain" is a methodology-level concept (artifact chains per stage), not an SDLC-level concept. The fix was renaming "SDLC chain" to "SDLC profile".
- *"everything is flexible..... things can be defined in the wiki, take or not and adapted or not"* — answering Q4 in one sentence and giving us the Flexibility Principle.
- *"openarms was just discovering things and making assumption, we have a much higher ground"* — pushing past the "5 cognitive contexts" framing into the 8-dimension taxonomy.
- *"things like context and tools and skills and etc.. they can open to a folder with more"* — identifying the 8th taxonomy dimension: expansion pattern (flat file vs file+folder vs folder vs runtime-generated tree).
- *"pipeline stuff in pipeline and gateway stuff in gateway"* — the clean directive for Q2.
- *"gateway if for the external mainly but for us too"* — refining Q2: gateway's primary audience is external consumers, with the operator as first-class user.
- *"why do you still want to remove --chain ?"* — critical correction when I was about to destroy the `--chain` flag. `--chain` is legitimate for methodology chains; it was just pointed at the wrong target.
- *"sometimes its okay to be redundant... especially when its at a different level or type of entries"* — validating that `gateway query --chain X` and `gateway query --model X --full-chain` can coexist at different levels.
- *"openarms was just discovering... we have a much higher ground"* — consistent theme. We are not imitating sister projects; we are **the brain** that aggregates their discoveries and produces higher-ground framings.

---

## What Was Done (Phase by Phase)

### Phase 1 — Batch Ingestion (Tiers 1–4)

**Input:** The operator provided 17 source URLs at the start of the session:
- Tier 1 (methodology frameworks): OpenSpec, spec-kit, BMAD-METHOD
- Tier 2 (agent architecture): Claude Agent SDK, Claude Managed Agents tools, code-review-graph, openclaw-billing-proxy, Vercel opensrc
- Tier 3 (skills & LLM patterns): SKILL/CLAUDE/AGENTS comparison, Pydantic AI, AutoBE, Raschka's LLM architecture gallery, 27 Questions, Claude Code patch gist
- Tier 4 (videos): 7 Levels of Claude Code + RAG, HRM/TRM "27M model beat ChatGPT"

**Infrastructure fix needed first:** GitHub repo fetches were returning README only (200-1000 lines). We enhanced `tools/ingest.py` to fetch the repo tree via the GitHub API and pull up to 30 key files from priority directories (docs/, spec/, templates/, etc.). This took BMAD-METHOD from 116 → 5,286 lines of raw source, OpenSpec from 211 → 6,979, spec-kit from 936 → 5,907. The deep fetch was committed and is now the default behavior for any future GitHub ingestion.

**Outputs — 16 synthesis pages:**
- `wiki/sources/src-openspec-spec-driven-development-framework.md` (316 lines)
- `wiki/sources/src-github-spec-kit-specification-driven-development.md` (281 lines)
- `wiki/sources/src-bmad-method-agile-ai-development-framework.md` (205 lines)
- `wiki/sources/src-claude-agent-sdk-and-managed-agents.md` (297 lines) — combined synthesis of SDK + Managed Agents Tools
- `wiki/sources/src-code-review-graph-automated-review.md` (~200 lines)
- `wiki/sources/src-vercel-opensrc-toolkit.md` (~200 lines)
- `wiki/sources/src-openclaw-billing-proxy.md` (~200 lines)
- `wiki/sources/src-skillmd-claudemd-agentsmd-three-layer-context.md` (264 lines)
- `wiki/sources/src-pydantic-ai-typed-agent-framework.md` (176 lines)
- `wiki/sources/src-autobe-compiler-verified-backend-generation.md` (216 lines)
- `wiki/sources/src-llm-architecture-gallery-raschka.md` (236 lines)
- `wiki/sources/src-27-questions-llm-selection.md` (~180 lines)
- `wiki/sources/src-claude-code-prompt-patch-rebalancing.md` (~180 lines)
- `wiki/sources/src-7-levels-claude-code-rag.md` (294 lines)
- `wiki/sources/src-hrm-trm-tiny-recursion-models.md` (151 lines)

**Outputs — 3 evolved pages (convergent evidence distilled):**
- `wiki/lessons/01_drafts/if-you-can-verify-you-converge.md` (170 lines) — AutoBE + HRM/TRM + our own pipeline post chain + OpenArms hooks all converge on this: when a verification mechanism exists, model quality differences affect retry COUNT, not final quality. Cost-quality trade-off dissolves when retry is cheap.
- `wiki/patterns/01_drafts/three-layer-agent-context-architecture.md` (174 lines) — Claude Code ecosystem (60k+ repos) + BMAD-METHOD + our own CLAUDE.md gap all converge on the three-layer pattern: AGENTS.md (universal) + CLAUDE.md (tool-specific delta) + Skills (on-demand).
- `wiki/lessons/01_drafts/specs-as-code-source-inverts-hierarchy.md` (176 lines) — spec-kit + OpenSpec + BMAD + our own methodology all converge on: when AI can generate code from specs precisely, specs become the source of truth and code becomes regenerable output. Inverts the traditional hierarchy.

**Outputs — 4 model integrations (new evidence woven into existing models):**
- Model — Local AI: "Breakthrough Evidence — Small Models Can Win" section with AutoBE (Qwen 25x cheaper), HRM/TRM (27M beats GPT-5 on ARC-AGI), architecture convergence (MLA+MoE 3-10% active params).
- Model — Quality and Failure Prevention: "External Validation — Industry Evidence for Our Principles" with AutoBE's verify-to-converge, code-review-graph's 31.6→68.4% accuracy, Claude Code prompt patch (11 patches) cross-validating our 7-class failure taxonomy.
- Model — Context Engineering: "Industry Frameworks — Structured Context in Production" with OpenSpec/spec-kit/BMAD + the three-layer architecture and ETH Zurich's 3% harm finding for AI-generated context files.
- Model — Skills, Commands, and Hooks: "Ecosystem Context — SDK, Standards, and Progression" with Agent SDK (query vs ClaudeSDKClient), Managed Agents 8-tool toolset, AGENTS.md as emerging universal standard, 7 Levels positioning this wiki at Level 4-5 targeting 6-7.

### Phase 2 — Root Documentation Architecture

The operator asked for proper README and thematic root files with clear concerns, referencing the three-layer pattern we had just distilled. The structure:

| File | Lines | Audience | Loading | Concern |
|------|-------|----------|---------|---------|
| README.md | 200 | First visitor (human/AI) | Facultative | Project overview, entry points by role |
| AGENTS.md | 159 | Any AI tool (Claude, Codex, Copilot, Gemini, Cursor) | Auto-injected | Universal cross-tool rules + methodology |
| CLAUDE.md | 107 (was 315) | Claude Code specifically | Auto-injected | Claude-specific overrides; references AGENTS.md |
| CONTEXT.md | 227 | Anyone understanding scope | Facultative | Identity profile, current state, active epics, constraints |
| ARCHITECTURE.md | 585 | Anyone modifying structure | Facultative | Data flow, tool topology, page schema, integration points |
| DESIGN.md | 355 | Page creators | Facultative | Visual design principles, callout vocabulary, page layouts |
| TOOLS.md | 806 | Operators | Facultative | Complete CLI reference (pipeline, gateway, view, sync, MCP) |
| SKILLS.md | 275 | Skill users/authors | Facultative | Skills catalog, SKILL.md format, extension hierarchy |

Total: 2,714 lines across 8 files vs 315 lines crammed into one. Each file has ONE responsibility. AGENTS.md slightly over the 100-line target (pragmatic — this is a complex system with many sacrosanct rules). CLAUDE.md at 107 is well below ETH Zurich's 300-line harm threshold.

Then wired into the wiki graph:

- `wiki/spine/references/root-documentation-map.md` — the spine page that catalogs all 8 root files, explains the three-layer pattern, and documents loading flow per consumer.
- Gateway: `query --docs` subcommand (list all 8 with line counts) and `query --docs <name>` (metadata + 500-char preview).
- MCP: `wiki_gateway_docs` tool (22nd MCP tool) exposing the root docs to external clients.
- Methodology system map: added "Entry Layer" as the 4th layer (was 3 layers: Knowledge / Configuration / Tooling; now 4: Entry / Knowledge / Configuration / Tooling).
- Super-model: updated Key Pages table + v2.0 architecture notes to include the root-docs and batch ingestion.

### Phase 3 — Context File Taxonomy

Triggered by Q5 of the decision queue. The 5-cognitive-context framing from OpenArms was an oversimplification. Taxonomy page created at `wiki/spine/references/context-file-taxonomy.md` (451 lines).

The 8 dimensions:
1. Loading mode (auto-injected / directed / facultative / just-in-time)
2. Origin / Authority (operator / repo / workspace / agent-specific / external / runtime)
3. Scope / Perspective (global / project / workspace / session / task)
4. Responsibility (identity / rules / methodology / tools / knowledge / state / navigation)
5. Audience (operator / any-AI / Claude-Code / sub-agent / provisioned-agent / MCP-client)
6. Aggregation role (authoritative / synthesis / index / override / pointer)
7. Depth relationship (condensed / authoritative / index / orphan — relative to wiki knowledge)
8. Expansion pattern (flat file / file+companion folder / folder README-indexed / runtime-generated tree)

The 8th dimension was the operator's insight: `SKILLS.md + .claude/skills/` is the pattern — flat root file + companion folder. OpenFleet's `SOUL.md + tasks/heartbeat/feed` is the scale-up example. Flexibility + structure in one pattern.

Complete catalog of every context source in the ecosystem classified across all 8 dimensions. 5 worked examples:
- Solo operator session (this wiki today)
- Harness-managed agent (OpenArms v10)
- Provisioned fleet agent (OpenFleet)
- Sub-agent dispatched from Claude
- External MCP client (sister project agent)

Each example shows which files load, in what order, at what scope, with override chain when rules conflict.

### Phase 4 — Config Architecture Overhaul

Resolved Q3 and Q4 with substantive changes:

**New: wiki/config/methodology-profiles/** — Layer 2 of the 4-layer config stack. 4 profiles + README:
- `stage-gated.yaml` (110L) — current default style made explicit
- `spec-driven.yaml` (130L) — SDD/spec-kit inspired, specs as source of truth, 45% effort weight on Document stage, `[NEEDS CLARIFICATION]` markers as hard gates
- `agile-ai.yaml` (155L) — BMAD inspired, 5 specialized personas, party mode, 60+ brainstorming techniques, PRFAQ stress-testing
- `test-driven.yaml` (145L) — TDD style, Red/Green/Refactor mapped to methodology stages, tests-must-fail scaffold gate
- `README.md` (170L) — explains methodology profiles, composition, adding new profiles

This gives BMAD/SDD/spec-kit/TDD first-class homes in config. Each profile's `derived_from` field references the source synthesis pages.

**New: wiki/config/domain-profiles/knowledge.yaml** (~100L) — the missing domain profile for pure knowledge projects (no code). Distinct from python-wiki (tools + wiki) and typescript/infrastructure (code projects). Documentation-only repos would use this.

**New: wiki/config/README.md** (830 lines) — the thorough reference. Every config file documented with: Purpose, What it contains, Consumed by, Overrides/Layered on by, Real example snippet, Related wiki pages, Modification notes. Plus the 4-layer architecture diagram, composition order, override precedence, how-to-add-new-X sections.

**New: The Flexibility Principle section in wiki/config/README.md**. Per Q4: "Nothing in wiki/config/ is mandatory for a consuming project. The wiki provides authoritative reference definitions. Projects choose: take as-is, take and adapt, take part of it, or ignore entirely. The only mandatory layer is project-local overrides (CLAUDE.md/AGENTS.md). The wiki is a menu, not a law." This is Goldilocks applied to configuration.

**Archived: wiki/config/agent-directive.md** → `wiki/log/archived/agent-directive-original.md` with frontmatter explaining supersession by AGENTS.md + CLAUDE.md + CONTEXT.md + ARCHITECTURE.md.

### Phase 5 — Methodology Composition Rules + Document Types

Resolved Q6 and Q7.

**Q6 — Composition rules encoded where they belong:**

Added `composition_rules:` section to methodology.yaml declaring all 4 patterns with their implementation locations:
- **Nested** — fully in methodology.yaml (model.composition + chain.composition_model)
- **Conditional (initial selection)** — fully in methodology.yaml (model_selection)
- **Conditional (runtime promotion)** — `valid_promotions:` graph in methodology.yaml + 4 new frontmatter fields (promoted_from/promoted_to/promotion_reason/promoted_at)
- **Sequential** — task frontmatter (depends_on existed; followed_by NEW)
- **Parallel** — NOT in methodology.yaml (orchestration layer, not methodology)

Terminal vs promotable models declared: documentation/research/refactor are promotable; hotfix/bug-fix/feature-development/integration/knowledge-evolution are terminal.

**Q7 — Methodology document types:**

Most methodology documents reuse existing wiki types (concept, reference, decision) with specialized templates. Only operations-plan has its own type because it's structurally different (sequential checklist, no judgment). The rule was made explicit in artifact-types.yaml: "A new wiki page type is justified ONLY if it has STRUCTURALLY DIFFERENT rules from existing types. Methodology-specific CONTEXT alone isn't enough."

New template: `wiki/config/templates/methodology/adr.md` — formal ADR variant of decision page with Context/Decision/Consequences structure. Maps to `wiki_type: decision` with `methodology_doc_type: ADR` frontmatter.

New frontmatter field: `methodology_doc_type` (optional, enum {requirements-spec, infrastructure-analysis, gap-analysis, design-plan, tech-spec, test-plan, operations-plan, ADR}). Makes methodology identity queryable without new wiki types.

### Phase 6 — Trust Model for Contributions

Resolved Q8.

**Answer:** NEITHER pure approval NOR pure auto-merge. Trust-tiered via maturity lifecycle. Already baked into the architecture (00_inbox → 01_drafts → ... → 04_principles) but not declared. Now declared.

**New: wiki/config/contribution-policy.yaml** (~150L):
- 4 tiers: operator / harness-trusted / fleet-agent / external-unknown
- known_contributors registry (e.g. openarms-harness-v10 → harness-trusted)
- Per-gate promotion requirements (manual review + automated gate commands)
- 4 contribution_status values (pending-review / accepted / rejected / superseded)
- Audit trail spec (required fields per contribution)

**New frontmatter fields** in wiki-schema.yaml: contributed_by, contribution_source, contribution_date, contribution_status (+ enum).

**gateway contribute extended:** `--contributor`, `--source`, `--reason` flags. Auto-detects contributor as `user@host` when not specified. Writes full audit trail to frontmatter.

**MCP tool updated:** `wiki_gateway_contribute` exposes the new parameters.

### Phase 7 — Gateway + Lint + Parser Infrastructure

Throughout the session, infrastructure changes went in alongside the content work:

**Relationship parser (tools/common.py):**
- Em-dash/hyphen comment stripping now happens ONLY after `]]` close, preserving titles like "Model — Methodology" that have em-dashes inside.

**Relationship auto-fixer (tools/obsidian.py):**
- `fix_all_relationships()` wired into `pipeline post` chain (step 4a, before backlink regeneration). Every `pipeline post` now automatically rewrites bare title references to `[[slug|title]]` wikilinks using the manifest lookup.

**Lint (tools/lint.py):**
- Dead relationship check now extracts slug side of `[[slug|title]]` wikilinks from the raw line. Em-dash-style comments no longer corrupt the parse.
- `_strip_context` handles em-dash/hyphen/en-dash comments + wikilink display titles.

**Gateway (tools/gateway.py):**
- New subcommands: `query --docs`, `query --profile`, `query --profiles`, `flow`, `flow --step N`, `factory-reset` (with --confirm).
- `query --chain` repointed from SDLC to methodology chains (fixes the category error).
- `move` fully implements reference updates + domain-field inference (was stub).
- `what-do-i-need` emits auto-detect warnings per dimension.
- Auto-detect warnings + detected-identity output per 8 taxonomy dimensions.

**MCP server (tools/mcp_server.py):**
- 5 new gateway tools: wiki_gateway_query, wiki_gateway_template, wiki_gateway_contribute, wiki_gateway_flow, wiki_gateway_docs.
- Total MCP tools now 22.

**view.py:**
- Fixed "Models (0)" bug — title prefix matcher was looking for "Model:" but our titles use "Model —" (em dash).

---

## Architecture Decisions Made

All 8 P1 Architecture Decisions resolved. Each decision has concrete tooling + config backing it.

| # | Question | Resolution | Concrete Changes |
|---|----------|-----------|------------------|
| Q1 | Should SDLC chains be YAML configs or wiki pages? | YAML authoritative; wiki explains. Renamed "SDLC chain" → "SDLC profile" (category error — chains belong to methodology). | Directory renamed, YAML keys renamed, gateway `--profile`/`--profiles` added, `--chain` repointed to methodology chains, ~80 files updated |
| Q2 | Should gateway extend pipeline.py or be separate? | Separate, audience-based. Pipeline = internal WRITE ops. Gateway = external-facing knowledge interface + selected write-back. | `pipeline backlog` deprecated → `gateway query --backlog`. ARCHITECTURE.md has authoritative "Pipeline vs Gateway" section. |
| Q3 | Should artifact chains be in methodology.yaml? | Yes, already correct. Added methodology-profiles/ layer for external standards (BMAD/SDD/TDD). | 4 methodology profiles + README + knowledge.yaml domain profile + archive agent-directive.md + wiki/config/README.md (830L) |
| Q4 | Wiki vs per-project for domain profiles? | Both. Flexibility Principle. Wiki is a menu, not a law. | "The Flexibility Principle" section in wiki/config/README.md documents the policy |
| Q5 | Should CLAUDE.md be split per cognitive context? | Wrong framing. 8 dimensions, not 5 contexts. | `wiki/spine/references/context-file-taxonomy.md` (451L) + "Root Doc + Companion Folder" as first-class pattern |
| Q6 | Composition rules in methodology.yaml? | Yes, each pattern at its natural config layer. | `composition_rules:` section + valid_promotions graph + 5 new frontmatter fields (followed_by + 4 promotion audit fields) |
| Q7 | Methodology doc types as new wiki types? | No for most, yes only if structurally different. New rule documented. | ADR template added + `methodology_doc_type` frontmatter field + enum |
| Q8 | Approval vs auto-merge for contributions? | Neither. Trust-tiered via maturity lifecycle. | `contribution-policy.yaml` + 4 audit frontmatter fields + `--contributor`/`--source`/`--reason` flags + MCP tool update |

---

## Current State

### Wiki Metrics (at end of session)

| Metric | Value |
|--------|-------|
| Pages | 319 |
| Relationships | 2,089 |
| Validation errors | 0 |
| Lint issues | 0 |
| Models | 16 |
| Standards | 22 (all with annotated exemplars) |
| Sub-super-models | 5 |
| Ecosystem project profiles | 5 |
| Validated lessons | ~42 |
| Validated patterns | ~16 |
| Validated decisions | ~16 |
| Principles | 3 |
| Source syntheses | ~44 (16 added this session) |
| Root-level .md docs | 8 |
| Config YAMLs | ~20 (across 4 layers) |

### Config Stack (post-session)

```
Layer 0 — Schema/Catalog
  wiki/config/wiki-schema.yaml
  wiki/config/artifact-types.yaml
  wiki/config/domains.yaml
  wiki/config/quality-standards.yaml
  wiki/config/export-profiles.yaml
  wiki/config/contribution-policy.yaml   ← NEW

Layer 1 — Methodology Definitions
  wiki/config/methodology.yaml
    (now includes composition_rules: section with valid_promotions)

Layer 2 — Methodology Profiles   ← NEW LAYER
  wiki/config/methodology-profiles/
    stage-gated.yaml
    spec-driven.yaml
    agile-ai.yaml
    test-driven.yaml
    README.md

Layer 3 — Domain Profiles
  wiki/config/domain-profiles/
    typescript.yaml
    python-wiki.yaml
    infrastructure.yaml
    knowledge.yaml                       ← NEW

Layer 4 — SDLC Profiles
  wiki/config/sdlc-profiles/
    simplified.yaml
    default.yaml
    full.yaml

Plus: wiki/config/README.md (830L thorough reference)
Plus: wiki/config/templates/methodology/adr.md   ← NEW
```

### Root-Level Files (post-session)

```
README.md              200 lines   First visitor entry
AGENTS.md              159 lines   Universal cross-tool context
CLAUDE.md              107 lines   Claude-specific (was 315)
CONTEXT.md             227 lines   Identity + state
ARCHITECTURE.md        585 lines   Data flow + topology
DESIGN.md              355 lines   Visual design principles
TOOLS.md               806 lines   Complete CLI reference
SKILLS.md              275 lines   Skills catalog + conventions
```

### MCP Tools (22 total)

17 pipeline tools (wiki_status, wiki_search, wiki_read_page, wiki_list_pages, wiki_post, wiki_fetch, wiki_fetch_topic, wiki_scan_project, wiki_gaps, wiki_crossref, wiki_sync, wiki_mirror_to_notebooklm, wiki_integrations, wiki_continue, wiki_evolve, wiki_backlog, wiki_log) + 5 gateway tools (wiki_gateway_query, wiki_gateway_template, wiki_gateway_contribute, wiki_gateway_flow, wiki_gateway_docs).

---

## Ready for Human Review

The operator's eyes are required for:

1. **The 3 evolved pages** in drafts — should they promote to 02_synthesized?
   - `wiki/lessons/01_drafts/if-you-can-verify-you-converge.md`
   - `wiki/patterns/01_drafts/three-layer-agent-context-architecture.md`
   - `wiki/lessons/01_drafts/specs-as-code-source-inverts-hierarchy.md`

2. **The 16 source syntheses** — confirm they accurately represent the sources and that cross-references are useful.

3. **The 4 model integrations** — are the new 2026-04-14 sections well-placed?

4. **The 8 root .md docs** — did the split land correctly? Is anything misfiled between files?

5. **The Context File Taxonomy** — is the 8-dimension framing correct? Any dimensions missing?

6. **The 4 methodology profiles** — do stage-gated / spec-driven / agile-ai / test-driven capture the right landscape? Anything missing?

7. **The contribution-policy.yaml** — do the 4 trust tiers match your intended granularity?

8. **Obsidian browse experience** — with 8 root docs + 451-line taxonomy page + 830-line config README, does the graph view still make sense? Any orphans?

---

## What's Blocked

These items still need operator involvement, external systems, or time:

- **E016 Integration Chain Proof** — needs the 17-step chain actually executed against OpenArms.
- **E019 Obsidian Navigation** — needs the operator browsing from Obsidian and reporting broken paths.
- **E020 Knowledge Sweep** — needs human eyes on every validated page.
- **E021 New Source Ingestion** — mostly complete with this batch; partial as the operator provides more sources.
- **AICP Stage 3** — blocked on hardware upgrade (19GB VRAM).
- **Per-agent trust tier graduation** — `harness-trusted` tier exists in contribution-policy but no automated graduation path. Needs manual operator decision per contributor.
- **Archive of agent-directive.md** — contributing content merged; content review still valuable.

---

## What's Next

### The Operator Decision Queue (73 → 64 open)

P1 Architecture Decisions: **ALL 8 RESOLVED** ✓

P2 Standards & Format Decisions (Q9-Q17): **9 open**
- Q9: Exemplars BEST or TYPICAL?
- Q10: Annotation format standardization
- Q11: Templates — structure + example split?
- Q12: AI Quick Start callout blocks on key methodology pages?
- Q13: Lessons with <3 evidence items — flag for demotion?
- Q14: Concept pages >300 lines — split into concept + deep-dive?
- Q15: Formal styling review gate?
- Q16: Before/after examples — Obsidian screenshots?
- Q17: Annotated exemplars — inline or companion documents?
- Q17a: **Should we have a standards page for session handoff documents?** (added 2026-04-14 — this very doc is evidence of the need)

P3 Tooling & Enforcement: 10 open (Q18-Q27)
P4 Agent & Ecosystem: 8 open (Q28-Q35)
P5 Methodology Engine Details: 16 open (Q36-Q51)
Deferred (research required): 22 open (Q52-Q73)

### Immediate Next Session Candidates

- **Continue P2 decisions** — start with Q9 (exemplar policy), since E011 is deeply affected.
- **Create a session-handoff page standard** (Q17a) — the operator flagged this; we have 9 prior session handoffs in docs/ with no formal quality bar.
- **Push 3 evolved pages up the maturity ladder** — from 01_drafts → 02_synthesized. Evidence is strong.
- **Write an operations-plan** for "How to apply the three-layer context pattern to a sister project" — tangible follow-through on the Flexibility Principle.
- **Ingest the remaining operator decision queue questions systematically** — same approach as Q1-Q8.
- **Check wiki/backlog/research-gaps.md** — 18 empirical research questions that were queued earlier.

### Longer-Term Candidates

- **LightRAG integration** for Level 6 of the 7 Levels of Claude Code (we have the graph; need the layer).
- **E016 integration chain proof** against OpenArms — prove end-to-end the ecosystem flow works.
- **AICP Stage 3** with routing — once the 19GB VRAM upgrade lands, AutoBE/HRM/TRM-style local inference with verification loops becomes viable.
- **Harness trust graduation process** — declare a policy (via decision page) for how a sister-project harness earns `harness-trusted` tier.

---

## How to Resume

If you're a fresh Claude session and the operator asks you to continue this work, read in this order:

1. **CLAUDE.md** (auto-loaded) — know who we are and what we're doing.
2. **AGENTS.md** (auto-loaded) — know the universal rules.
3. **This handoff document** — understand what was just done.
4. **The operator decision queue** (`wiki/backlog/operator-decision-queue.md`) — see what's resolved and what's next.
5. **wiki/config/README.md** — understand the 4-layer config architecture.
6. **wiki/spine/references/context-file-taxonomy.md** — understand how context files compose.
7. **wiki/spine/super-model/super-model.md** — the dashboard.

Then run `python3 -m tools.pipeline post` to verify everything is still clean. If it is, you're ready to continue.

### Skill Invocation

- `/continue` skill resumes the mission from whatever state we're in.
- `/status` shows pipeline state + gateway dashboard.
- For a new batch ingestion: `python3 -m tools.pipeline fetch URL1 URL2 ...` (deep GitHub fetch enabled by default).
- For a new wiki page: `python3 -m tools.pipeline scaffold <type> "<title>"`.

### The Only Things I Haven't Committed (safety check)

None. Everything in this session was committed across approximately 12 commits, each with detailed rationale in the message. `git log --oneline -20` should show them all.

### Where Quality Could Drift If Left Untended

- **Contribution audit trail**: new fields exist but no tool validates that external-agent contributions have `contributed_by` set. Could be a lint check later.
- **Methodology profile compatibility**: `compatible_with_sdlc_profiles` is declared in each profile YAML but no code enforces the matching at gateway-time.
- **Promotion rules**: documented in `contribution-policy.yaml` but no automated gate checks them on promotion. Operator-manual for now.
- **Orphan risk**: 8 root docs + taxonomy + methodology-profiles README + contribution-policy don't have explicit inbound links from every model. May need Obsidian graph audit.

---

## Key Files and References

### Session-Produced (new)

- `README.md`, `AGENTS.md`, `CLAUDE.md` (slimmed), `CONTEXT.md`, `ARCHITECTURE.md`, `DESIGN.md`, `TOOLS.md`, `SKILLS.md` — 8 root docs
- `wiki/spine/references/context-file-taxonomy.md` — 8-dimension taxonomy
- `wiki/spine/references/root-documentation-map.md` — spine map of the 8 root docs
- `wiki/config/README.md` — thorough config reference (830L)
- `wiki/config/methodology-profiles/` — 4 profiles + README
- `wiki/config/domain-profiles/knowledge.yaml` — missing domain profile
- `wiki/config/contribution-policy.yaml` — trust model
- `wiki/config/templates/methodology/adr.md` — ADR template
- 16 `wiki/sources/src-*.md` files (batch ingestion)
- 3 evolved pages (2 lessons + 1 pattern)
- `wiki/log/archived/agent-directive-original.md` — preserved history
- `docs/SESSION-2026-04-14-handoff.md` — this document

### Session-Modified (key ones)

- `tools/pipeline.py` — relationship auto-fixer integration
- `tools/gateway.py` — new subcommands, audit trail, composition rules query
- `tools/mcp_server.py` — 5 new gateway MCP tools
- `tools/obsidian.py` — `fix_all_relationships` function
- `tools/common.py` — parse_relationships em-dash fix
- `tools/lint.py` — slug-side matching for wikilinks
- `tools/ingest.py` — GitHub deep fetch
- `tools/view.py` — Models (0) bug fix
- `wiki/config/methodology.yaml` — composition_rules: section
- `wiki/config/wiki-schema.yaml` — 10+ new optional frontmatter fields, 2 new enums
- `wiki/config/artifact-types.yaml` — ADR entry, "the rule" for new types
- `wiki/spine/super-model/super-model.md` — Key Pages + v2.0 notes + updated metrics
- `wiki/spine/references/methodology-system-map.md` — 4-layer config architecture
- `wiki/patterns/01_drafts/three-layer-agent-context-architecture.md` — Instance 3 updated (post-refactor)
- `wiki/backlog/operator-decision-queue.md` — 8 questions marked RESOLVED
- 5 ecosystem project profiles — three-layer adoption status rows
- 4 core models (Local AI, Quality, Context Engineering, Skills/Commands/Hooks) — new 2026-04-14 sections

### Related Wiki Pages (deep reference)

- `wiki/spine/models/foundation/model-methodology.md`
- `wiki/spine/models/depth/model-context-engineering.md`
- `wiki/spine/models/agent-config/model-claude-code.md`
- `wiki/spine/models/agent-config/model-skills-commands-hooks.md`
- `wiki/domains/cross-domain/model-composition-rules.md`
- `wiki/domains/cross-domain/methodology-framework/sdlc-customization-framework.md`
- `wiki/lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md`

### Source Syntheses Produced (for follow-up reading)

Highest-impact for future work:
- `wiki/sources/src-skillmd-claudemd-agentsmd-three-layer-context.md` — evidence base for root docs architecture
- `wiki/sources/src-openspec-spec-driven-development-framework.md` — evidence for spec-driven profile
- `wiki/sources/src-bmad-method-agile-ai-development-framework.md` — evidence for agile-ai profile
- `wiki/sources/src-autobe-compiler-verified-backend-generation.md` — evidence for "If you can verify, you converge"
- `wiki/sources/src-hrm-trm-tiny-recursion-models.md` — evidence for small-model-wins-on-bounded-problems

---

## Reflection

What worked in this session:

- **Iterative commit cycles**: Each resolved question got a commit with detailed rationale. If anything breaks, we can bisect cleanly.
- **"Fix the tool then use the tool"**: Mid-ingestion we fixed GitHub deep fetch, mid-taxonomy-work we fixed the parser. The operator's directive is vindicated.
- **Operator correction as a first-class input**: Several questions (Q1, Q2, Q5) had framings that were wrong. The operator's corrections (chain is methodology; gateway is external; 5 contexts is oversimplified) reshaped the solutions significantly. The willingness to say "no wait" produced better architecture.
- **Dispatching sub-agents for substantial writing**: The 4 methodology profiles, the config README, and the context taxonomy page were dispatched with explicit direction. They came back substantive and validated.
- **Pipeline post as the continuous gate**: After every significant change we ran it. 0 errors, 0 lint became the heartbeat.

What could have gone better:

- **Taxonomy discovery was iterative** — the 8th dimension (expansion pattern) was surfaced by the operator, not by me. I initially produced 7 dimensions; the operator had to point at SKILLS.md + `.claude/skills/` and ask "you're ignoring this?" to get me to see it. Needed to exhaust the real ecosystem before defining the abstract taxonomy.
- **"SDLC chain" category error existed for weeks** — the first 30 commits never questioned whether "chain" was the right word. Operator corrected it when reviewing Q1. Shows that unchallenged vocabulary can persist through months of design.
- **Context file pressure during handoff** — this document is being written at 2% remaining context. A small amount of reflection has been compressed relative to what would be ideal. The next session should budget for it.

---

## Closing

At the start of this session the operator said we would proceed "one question at a time" for the decision queue. We did, and 8 of 73 questions are now resolved — not as prose answers but as **config changes, schema changes, tool changes, and documented principles**. Each decision has a tangible artifact you can point at.

The wiki at this moment is more **internally coherent** than at any prior point. The architecture is explicit. The layering is documented. The naming is consistent. The extension points are named. The operator's answer to "everything is flexible... things can be defined in the wiki, take or not and adapted or not" is encoded as The Flexibility Principle. The operator's insight that "chains are inside methodology" is encoded in the SDLC-chain → SDLC-profile rename. The operator's insight that root docs can expand to companion folders is encoded as dimension 8 of the Context File Taxonomy.

The next session can continue P2 of the decision queue, or pivot to the knowledge sweep (E020), or tackle the integration chain proof (E016), or run a fresh batch ingestion. Any of these is viable. The pipeline is green. The graph is dense. The brain is thinking.

End of handoff.

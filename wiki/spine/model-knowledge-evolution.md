---
title: "Model: Knowledge Evolution"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-10
sources:
  - id: src-karpathy-llm-wiki-idea-file
    type: documentation
    file: raw/articles/karpathy-llm-wiki-idea-file.md
    title: "Karpathy LLM Wiki Idea File"
  - id: src-llm-wiki-v2-agentmemory
    type: documentation
    file: raw/articles/llm-wiki-v2-extending-karpathys-llm-wiki-pattern-with-lessons-from-building-agen.md
    title: "LLM Wiki v2 — Extending Karpathy's Pattern with Agentmemory Lessons"
tags: [model, spine, knowledge-evolution, maturity, progressive-distillation, wiki-lifecycle, scoring, evolution-pipeline, second-brain]
---

# Model: Knowledge Evolution

## Summary

The Knowledge Evolution model describes how raw sources become lessons, patterns, and decisions through a structured, automated promotion pipeline. Raw files enter as seed-maturity pages; a deterministic scorer ranks them by six signals; the prompt builder assembles generation context from wiki relationships; an LLM backend generates evolved content; and a human review gate validates promotion. ==The pipeline is self-compounding: promoted pages add relationship edges that improve neighbor scores in subsequent runs.== The outer loop — ingest → evolve → gap-analyze → research → repeat — is the wiki's steady-state improvement mechanism.

## Key Insights

- **The scorer is deterministic; the generator is not.** Ranking uses six reproducible signals with no LLM inference — auditable, schedulable, immune to hallucination. The LLM is invoked only AFTER a candidate is selected. Separation is deliberate.

- **Maturity is a lifecycle, not a tag.** seed → growing → mature → canonical is a promotion path with defined criteria. Premature canonicalization produces false authority. Neglecting promotion produces orphaned seeds.

- **The pipeline has increasing returns.** Every evolved page creates new relationship edges. Those edges increase source scores in subsequent runs. A well-linked wiki evolves faster than a sparse one.

- **Prompt engineering is where pipeline intelligence lives.** The prompt builder assembles the candidate + all referenced pages + all referencing pages + domain context. Builder quality scales with wiki density — another form of increasing returns.

- **Three LLM backends for three operating contexts.** `claude-code` = human-in-the-loop, highest quality. `openai` = zero-cost local inference via LocalAI. `aicp` = fleet-integrated, complexity-routed.

## Deep Analysis

### The 6-Layer Density Architecture

> [!info] **Six layers of increasing knowledge distillation**
> | Layer | Type | Maturity | What it contains | Transformation |
> |-------|------|----------|-----------------|----------------|
> | 0 | Raw files | — | Unprocessed transcripts, articles, notes in `raw/` | None — source of truth |
> | 1 | Source synthesis | seed | What the source says, evidence preserved | Extraction — pull key claims |
> | 2 | Concepts | seed → growing | Multi-source integration, synthesized understanding | Synthesis — merge across sources |
> | 4 | Lessons | growing → mature | Validated insight — what was learned, with evidence | Distillation — WHY, not just WHAT |
> | 5 | Patterns | mature | Structural template generalizing across 2+ instances | Abstraction — reusable form |
> | 6 | Decisions | canonical | Resolved choice with rationale and alternatives | Resolution — actionable guidance |

The gap (no Layer 3) is intentional — the jump from concept to lesson is a qualitative shift, not just compression. A lesson is a validated principle with operational evidence, not a dense concept. See [[Progressive Distillation]].

---

### The Six Scoring Signals

> [!info] **Deterministic scorer — no LLM inference**
> | Signal | What it measures | Why it matters |
> |--------|-----------------|----------------|
> | **Cross-source convergence** (weight: 0.30) | How many distinct sources back the page | Multi-source = higher epistemic weight |
> | **Relationship hub** (weight: 0.20) | How many pages reference or are referenced by this page | High connectivity = pattern candidate |
> | **Domain layer gap** (weight: 0.15) | Missing layers in the page's domain | Domains with concepts but no lessons need evolution |
> | **Open question density** (weight: 0.15) | How many open questions the page has | Questions = evolution directions |
> | **Tag co-occurrence** (weight: 0.10) | Shared tags between this page and evolved pages | Tag overlap signals related evolution opportunity |
> | **Orphaned references** (weight: 0.10) | Relationship targets that don't exist yet | Missing pages = evolution candidates |

Full implementation: `tools/evolve.py` (1,321 lines). Run with `pipeline evolve --score --top 10 --json`.

> [!tip] **Scorer tuning history**
> Initial weights overvalued tag co-occurrence (0.25) — produced candidates that were just tag-pair matches. Rebalanced to emphasize cross-source convergence (0.30) and relationship hubs (0.20). Added `_GENERIC_TAGS` filter to exclude low-signal tags (model, concept, spine). Dedup checks source overlap with existing evolved pages. See the scorer tuning task in [[Model: Methodology]] Real Example section.

---

### The 8-Step Generation Loop

> [!info] **The evolution pipeline end-to-end**
> ```
> 1. SCORE    → rank all eligible pages by composite score
> 2. SELECT   → choose top N candidates (human-reviewed or automated)
> 3. ASSEMBLE → prompt builder gathers candidate + all related pages + domain context
> 4. GENERATE → LLM backend produces evolved page (lesson/pattern/decision type)
> 5. WRITE    → scaffolded page with full frontmatter to correct directory
> 6. POST     → post-chain validates, rebuilds indexes, regenerates wikilinks
> 7. REVIEW   → human gate: verify maturity promotion before marking mature/canonical
> 8. LOOP     → re-score; newly added relationships shift neighbor scores
> ```

> [!warning] **The ASSEMBLE step is where quality is won or lost**
> A candidate with 12 strong relationships to primary sources produces context that almost writes the lesson itself. A candidate with 3 thin relationships to other seed pages produces weak generation context. ==Ingestion quality directly determines evolution quality.== See [[Multi-Stage Ingestion Beats Single-Pass Processing]].

---

### The Four Maturity Levels

> [!info] **Promotion criteria per level**
> | Level | Criteria | How you get there |
> |-------|---------|-------------------|
> | **seed** | Valid frontmatter + Summary | Auto-generated or scaffolded |
> | **growing** | 3+ relationships, 2+ sources, referenced by ≥1 page | Human review confirms |
> | **mature** | Passed human review, validated against operational evidence, `derived_from` linked | Time + inbound references + review |
> | **canonical** | Tested against real implementation, no known contradictions | Marked manually — should be RARE |

> [!warning] **No auto-promotion**
> The system SUGGESTS promotions (`pipeline evolve --review`). A human confirms. Premature canonicalization is worse than no promotion — it creates false authority that other pages cite.

---

### The Three LLM Backends

> [!info] **Backend selection is separate from evolution logic**
> | Backend | How it works | Cost | Quality | Best for |
> |---------|-------------|------|---------|----------|
> | `--backend claude-code` | Writes prompt queue for human session execution | API cost | Highest (human reviews context) | Mature → canonical promotions |
> | `--backend openai` | Direct API call (LocalAI when configured) | Free (local) | Good for routine | seed → growing bulk evolution |
> | `--backend aicp` | Routes through AICP complexity scorer | Mixed (auto-routed) | Adaptive | Fleet-integrated evolution |

---

### Two Documented Failure Modes

> [!bug]- **Premature distillation**
> Promoting a page to pattern/canonical before it has enough cross-domain evidence, source diversity, or relationship density. A single-source pattern page looks authoritative but is one person's observation. When cited as canonical, the authority claim is unsupported.
>
> **Guard:** Minimum signal thresholds before promotion eligibility. The scorer won't rank a page with <3 relationships and <2 sources.

> [!bug]- **Distillation arrest**
> Seeds that accumulate enough relationships to qualify for evolution but never get promoted. The value is there — cited, cross-linked, multi-sourced — but locked in seed format. No distilled lesson, no structural template, no decision rationale.
>
> **Guard:** `pipeline evolve --review` surfaces pages in growing maturity with scores above the promotion threshold that haven't been acted on. The weekly review cadence catches these.

> [!tip] **Both failure modes have the same fix**
> Run the evolution pipeline regularly AND act on its output. A pipeline that runs but whose output is never reviewed is equivalent to no pipeline.

---

### Source Page Coexistence

When a concept evolves into a lesson or pattern, the source page is PRESERVED, not deleted.

> [!abstract] **Why coexistence matters**
> 1. **Evidence layer** — the evolved page makes a generalized claim. The source page contains the specific evidence. Deleting the source removes the evidence layer.
> 2. **Graph needs both nodes** — LightRAG gains value from the parent-child relationship. Source = evidence node. Evolved = synthesis node. Queries traverse both directions.
> 3. **Stale marking is honest** — `status: stale` signals supersession without deleting evidence value. The `derived_from` link navigates to the evolved version.

---

### The Weekly Evolution Cadence

> [!info] **Codified in `pipeline chain review`**
> ```
> 1. post              → validate, manifest, lint (catch decay since last run)
> 2. review            → surface pages ready for maturity promotion
> 3. gaps              → orphans, thin pages, open questions, weak domains
> 4. crossref          → missing backlinks, comparison candidates, domain bridges
>
> When evolution is queued:
> 5. evolve --score --top 10   → rank candidates
> 6. evolve --dry-run --top 3  → preview assembled context
> 7. Execute top candidates     → generate lessons/patterns/decisions
> 8. post                       → validate new evolved pages
> 9. gaps                       → see what promotions unlocked
> ```

---

### Key Pages

| Page | Layer | Role in the model |
|------|-------|-------------------|
| [[Knowledge Evolution Pipeline]] | L2 | The pipeline concept — scorer, builder, backends, loop |
| [[Progressive Distillation]] | L5 | The governing pattern — raw → synthesis → concept → lesson → pattern → decision |
| [[Wiki Ingestion Pipeline]] | L2 | The input to evolution — ingestion quality determines evolution quality |
| [[Multi-Stage Ingestion Beats Single-Pass Processing]] | L4 | Lesson: each ingestion pass discovers what the previous missed |
| [[LLM Knowledge Linting]] | L2 | Automated quality — detecting orphans, contradictions, staleness |
| [[Decision: Wiki-First with LightRAG Upgrade Path]] | L6 | The scale decision — when graph-enhanced retrieval becomes necessary |
| [[Decision: Local Model vs Cloud API for Routine Operations]] | L6 | Backend selection for routine evolution — local vs cloud trade-off |
| [[Second Brain Architecture]] | L2 | PKM theory (PARA + Zettelkasten) that influenced the layer model |
| [[Lesson: Schema Is the Real Product — Not the Content]] | L4 | Why the schema matters more than content — content is regenerable |
| [[Shallow Ingestion Is Systemic, Not Isolated]] | L4 | Why evolution fails when ingestion was shallow — garbage in, garbage out |

---

### Lessons Learned

| Lesson | What was learned |
|--------|-----------------|
| [[Multi-Stage Ingestion Beats Single-Pass Processing]] | Each ingestion pass discovers what the previous missed. Evolution quality depends on ingestion quality. |
| [[Shallow Ingestion Is Systemic, Not Isolated]] | One shallow page → thin evolution candidates → weak lessons. Quality compounds across layers. |
| [[Lesson: Schema Is the Real Product — Not the Content]] | Content is regenerable from sources. The schema that constrains evolution encodes irreplaceable operational knowledge. |
| [[Models Are Built in Layers, Not All at Once]] | Evolution itself follows SFIF — scaffold the pipeline, build the foundation (scorer), add infrastructure (backends), then features (review cadence). |

---

### State of Knowledge

> [!success] **Well-covered (built and operational)**
> - 6-layer density architecture with promotion criteria per level
> - Deterministic scorer with 6 signals, tuned weights, dedup logic (1,321-line implementation)
> - 8-step generation loop with prompt builder
> - Three LLM backends (claude-code, openai/LocalAI, aicp)
> - Two failure modes documented with guards
> - Weekly evolution cadence codified as pipeline chain
> - Source page coexistence policy
> - 10+ evolved pages generated (lessons, patterns, decisions)

> [!warning] **Thin or unverified**
> - LocalAI backend quality vs Claude — no systematic comparison exists
> - The 200-page threshold for LightRAG — set empirically, no density metric defined
> - Scorer gaming — manual cross-linking during ingestion could inflate scores artificially
> - AICP backend integration — planned but not yet tested with real evolution runs
> - Auto-evolution scheduling — `claude-code-scheduling` + `evolve` chain untested as a cron job
> - Cross-wiki evolution — can one project's wiki evolve from another project's pages?

---

### How to Adopt

> [!info] **Setting up the evolution pipeline for a new wiki**
> 1. **Build the wiki first** — you need 20+ pages before evolution produces value. Ingest sources, create concept pages, build relationships.
> 2. **Run `pipeline evolve --score`** — see what the scorer surfaces. If the top candidates make sense, the wiki is ready for evolution.
> 3. **Start with `--backend claude-code`** — human-in-the-loop produces the highest quality evolved pages. Use these as the quality standard.
> 4. **Add the weekly cadence** — `pipeline chain review` after every session or weekly. This catches both decay and missed promotion opportunities.
> 5. **Add LocalAI backend** — once the quality standard is established, route routine seed → growing evolution to local inference for zero cost.

> [!warning] **INVARIANT — never change these**
> - Scorer is deterministic — no LLM in ranking. Auditable, schedulable, immune to hallucination.
> - Human reviews maturity promotion — no auto-promotion from growing to mature or canonical.
> - Source pages are preserved — evolved pages coexist with sources, never replace them.
> - Post-chain runs after every evolution — validation errors block publication.
> - `derived_from` links are mandatory on evolved pages — provenance is not optional.

> [!tip] **PER-PROJECT — always adapt these**
> - Scorer weights (which signals matter most depends on wiki content distribution)
> - Backend selection (projects without LocalAI skip the openai backend)
> - Evolution cadence (weekly for active wikis, monthly for stable ones)
> - Promotion thresholds (how many relationships/sources before a page is eligible)
> - Which layers exist (not every wiki needs all 6 layers — some projects only need L0-L2-L4)

## Open Questions

> [!question] **What graph density metric triggers the need for LightRAG?**
> The 200-page threshold was set empirically. Is there a specific relationship-to-page ratio, average path length, or clustering coefficient that predicts when index navigation breaks down? (Requires: measuring navigation accuracy at different wiki sizes)

> [!question] **Does manual cross-linking inflate scores?**
> Pages cross-linked during ingestion start with higher relationship counts than organically connected pages. Should the scorer distinguish manually-seeded connections from organic ones? (Requires: comparing scorer output on manually-linked vs organically-linked candidate sets)

> [!question] **What is the quality delta between LocalAI and Claude-generated evolution?**
> Is the quality difference material for seed → growing promotion? Or does the human review gate catch quality issues regardless of backend? (Requires: blind comparison of pages generated by each backend on the same candidates)

## Relationships

- BUILDS ON: [[Knowledge Evolution Pipeline]]
- BUILDS ON: [[Progressive Distillation]]
- BUILDS ON: [[Multi-Stage Ingestion Beats Single-Pass Processing]]
- RELATES TO: [[Model: LLM Wiki]]
- RELATES TO: [[Model: Methodology]]
- RELATES TO: [[Model: Second Brain]]
- RELATES TO: [[Model: Automation and Pipelines]]
- ENABLES: [[Decision: Wiki-First with LightRAG Upgrade Path]]
- ENABLES: [[Decision: Local Model vs Cloud API for Routine Operations]]

## Backlinks

[[Knowledge Evolution Pipeline]]
[[Progressive Distillation]]
[[Multi-Stage Ingestion Beats Single-Pass Processing]]
[[Model: LLM Wiki]]
[[Model: Methodology]]
[[Model: Second Brain]]
[[Model: Automation and Pipelines]]
[[Decision: Wiki-First with LightRAG Upgrade Path]]
[[Decision: Local Model vs Cloud API for Routine Operations]]
[[Decision Page Standards]]
[[Evolution Standards — What Good Knowledge Promotion Looks Like]]
[[Lesson Page Standards]]
[[Model: Ecosystem Architecture]]
[[Model: NotebookLM]]
[[Model: SFIF and Architecture]]
[[Pattern Page Standards]]

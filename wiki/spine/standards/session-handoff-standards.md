---
title: Session Handoff Standards
aliases:
  - "Session Handoff Standards"
  - "Session Handoff Standards — What Good Handoffs Look Like"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: handoff-corpus-2026-04-08
    type: file
    file: docs/SESSION-2026-04-08.md
    description: First handoff — primitive, task enumeration style
  - id: handoff-corpus-2026-04-10-final
    type: file
    file: docs/SESSION-2026-04-10-final.md
    description: Same-day supersession pattern (part → part2 → final)
  - id: handoff-corpus-2026-04-12
    type: file
    file: docs/SESSION-2026-04-12-handoff.md
    description: Directive-driven format (13 operator directives sections)
  - id: handoff-corpus-2026-04-12-v2
    type: file
    file: docs/SESSION-2026-04-12-handoff-v2.md
    description: Comprehensive format with Mistakes section (meta-learning)
  - id: handoff-corpus-2026-04-14
    type: file
    file: docs/SESSION-2026-04-14-handoff.md
    description: Mature format — phase-by-phase + decisions table + review gates
  - id: operator-directive-q17a
    type: directive
    file: docs/SESSION-2026-04-14-handoff.md
    description: "Operator: 'Maybe we should have standards for those too, we fast put that on that list' — 2026-04-14"
tags: [standards, session-handoff, continuity, meta-documentation, non-wiki-genre, context-recovery]
---

# Session Handoff Standards

> [!tip] AI Quick Start — Writing a Session Handoff
>
> 1. **Start with the skeleton** — Header + Executive Summary + Session Context + What Was Done + Current State + What's Next + How to Resume. Everything else is optional.
> 2. **Metrics come from `pipeline post`, not memory** — run it fresh, paste the output. Estimated metrics are a lie.
> 3. **Operator directives VERBATIM** — never paraphrase. Use `> "quoted text"` blockquote format.
> 4. **File paths with line numbers where possible** — `[filename.md:42](path#L42)`. Prose like "the spec is in docs" is worthless next session.
> 5. **"How to Resume" is a CHECKLIST** — numbered actionable steps a fresh agent follows top-to-bottom. Not narrative.
> 6. **Filename**: `docs/SESSION-YYYY-MM-DD[-suffix].md`. Suffix only when multiple in one day (`-part2`, `-final`, `-v2`).
> 7. **Length follows content** — 4KB for a quiet session is fine; 47KB for a 13-directive session is fine. Padding is an anti-pattern.

## Summary

Standards for session handoff documents — the non-wiki genre that lives in `docs/SESSION-*.md` and exists to bridge conversation boundaries. A handoff is written at the end of a session for the NEXT agent (often future-self after context compaction) and for the operator reviewing what was done. It is explicitly NOT a wiki page, never ingested, has its own structural rules, and is the only project document whose audience is "the next version of me about to resume this work."

## Why This Standard Exists

9 handoffs existed in `docs/` ranging 4KB → 47KB with no formal quality bar. The format evolved organically — primitive task lists (Apr 8) → directive-driven (Apr 12) → mature phase+decisions+gates (Apr 14) — but without explicit rules, each session reinvented the structure. This document freezes the evolution into a framework that future sessions can follow, extend, or deliberately compress. It also recognizes that session handoffs are the one genre that doesn't fit the wiki page model — they are ephemeral operational artifacts, not durable knowledge — yet they are critical infrastructure for continuity. They deserve standards of their own.

Added to the operator decision queue as Q17a during the 2026-04-14 session; resolved by this document.

## Key Insights

1. **A session handoff has THREE audiences, not one.** Future-self (continuity), next agent (cold context recovery), operator (review). Each needs different sections. The skeleton below ensures all three are served.

2. **A session handoff has THREE temporal scopes.** LOCAL (what happened), FORWARD (what's next + how to resume), CORRECTIVE (what went wrong + what was learned). A handoff that omits CORRECTIVE for a session that HAD mistakes is dishonest.

3. **The handoff is NOT a wiki page.** Different lifecycle (ephemeral), different audience (agents, not readers), different quality bar (completeness of recall over concision). Do not apply wiki page standards blindly. Specifically: no frontmatter required, no backlinks required, no maturity progression.

4. **Verbatim operator speech is load-bearing.** Paraphrased directives lose the corrective signal. The Apr 12-v2 handoff's "Mistakes" section is valuable precisely because it quotes the operator directly: "you stopped at 10%", "do not confuse everything. the words are important." Paraphrasing this as "operator wanted more depth" discards the lesson.

5. **Length is not a quality signal — it is a content signal.** The Apr 10-final handoff (4KB) is GOOD for a session of focused fixes. The Apr 14 handoff (41KB) is GOOD for a session with 15 source ingestions + 8 P1 decisions + root docs refactor. A 4KB handoff for a 15-decision session is MALPRACTICE; a 40KB handoff for a 2-commit session is PADDING.

6. **Handoffs are quoteable, not ingested.** Wiki pages may link TO a handoff as historical record (the super-model already sources `docs/SESSION-2026-04-12-handoff-v2.md` under `operator-vision`). The handoff stays in `docs/`; the wiki references it. Never reverse this.

## When to Write a Handoff

A handoff is warranted when the next session would otherwise lose useful context. Multiple distinct triggers — any one is sufficient justification. Not every session needs a handoff; many focused-fix sessions are fully recoverable from the git log + commit messages alone.

> [!info] Triggers — write a handoff when ANY apply
>
> | Trigger | Why it warrants a handoff |
> |---------|---------------------------|
> | **Operator request** | Operator explicitly asks for one. The most common trigger. Operator may know the next session will need cold-start recovery. |
> | **End of a long session** | Substantial work accumulated (rough threshold: ≥5 commits OR ≥4 hours OR ≥2 distinct work phases). The git log alone won't show *why* the work flowed the way it did. |
> | **Multiple decisions resolved** | Several operator/architecture decisions made (rough threshold: ≥3). Decisions need their rationale preserved — commit messages capture WHAT changed, handoff captures WHY this resolution over alternatives. |
> | **Milestone reached** | A backlog milestone, epic completion, or queue tier closed. Worth marking explicitly so the next session sees the milestone, not just the diff. |
> | **Anticipated context compaction** | Defensive write before a likely compaction. The handoff persists what the in-conversation context is about to lose. See [[context-compaction-is-a-reset-event\|Context Compaction Is a Reset Event]]. |
> | **Mistakes or course corrections** | Operator had to redirect the session ≥1 time. The Mistakes section is the meta-lesson; without it, the next session may repeat the failure. The Apr 12 v2 handoff is the canonical example — it exists *because* the original Apr 12 handoff didn't capture the corrections. |
> | **Cross-session work continuing** | Current session set up work that explicitly continues next session (drafts queued for promotion, blocked items awaiting operator, ingestions partially processed). Without a handoff, "what's next" lives only in memory. |
> | **Ingestion of multiple substantive sources** | Batch source ingestions create a lot of new material that needs context for next-session integration. The Apr 14 handoff is an example. |
> | **Cross-agent handoff** | Work transitioning to another agent (different operator, different tool, fresh Claude session after a break). Sub-agents and successor agents lack conversation continuity. |
>
> **Don't write a handoff when:** single focused fix, no decisions made, no operator directives, work fully captured in commit messages and existing wiki pages. Padding a quiet session is itself an anti-pattern (see Anti-Patterns section below).

The triggers compose: a 10-commit day with 5 decisions resolved AND an ingestion AND a milestone reached has four reasons stacked — that's a strong case. A 1-commit fix with 0 decisions has zero reasons — skip it.

## The Genre — What a Session Handoff Is

| Property | Value |
|----------|-------|
| **Location** | `docs/SESSION-YYYY-MM-DD[-suffix].md` |
| **Audience** | Next-session agent, future-self (after context compaction), operator |
| **Lifecycle** | Ephemeral — created at session end, consumed at next session start, then archive |
| **Quality bar** | Completeness of recall, accuracy of state, actionability of resume checklist |
| **Frontmatter** | Not required (this is not a wiki page) |
| **Validation** | Not validated by `pipeline post` (not in `wiki/`) |
| **Graph membership** | NONE — handoffs do not join the wiki graph |
| **Ingestion** | FORBIDDEN — handoffs are never copied into wiki pages or the graph |
| **Supersession** | Same-day handoffs can supersede each other (`-part2`, `-final`, `-v2`); prior drafts remain for audit |

## Invariant Sections (Minimum Viable Handoff)

Every handoff, even the smallest, MUST have these six sections.

### 1. Header + Disclaimer

```markdown
# Session Handoff — YYYY-MM-DD

> **Purpose:** Context recovery document. Read this to resume work.
> **NOT a wiki page.** Lives in docs/, not wiki/. Do not ingest.
```

The disclaimer is not ceremonial — it stops an auto-ingest pipeline from treating the handoff as a wiki source.

### 2. Executive Summary

One-screen view. Answers: *What was the scope? What changed? What is the state at the end?* Must include final metrics pulled from a fresh `python3 -m tools.pipeline status`. Estimated metrics are an anti-pattern.

Minimum: 3-5 sentences and a metrics snapshot.

### 3. What Was Done

The work log. Choose ONE organizing structure based on session shape:

| Session Shape | Recommended Structure |
|---------------|----------------------|
| Directive-driven (operator corrections shaped the arc) | Directive-by-directive — `## Directive N: <title>` with verbatim quotes |
| Phase-driven (multiple distinct work phases) | Phase-by-phase — `### Phase 1 — <name>` with outputs per phase |
| Decision-driven (P1/P2 decisions were the scope) | Decisions table — one row per decision, before/after columns |
| Focused fix (single objective, short session) | Flat list of specific changes with file paths |

Whichever structure you pick, every entry should cite file paths. Prose like "fixed the scaffolder" is worthless; "fixed `tools/pipeline.py:214` — argparse abbreviation collision" is useful.

### 4. Current State

Snapshot. ALWAYS from `pipeline post` output (fresh). Include:
- Page count, relationship count, validation errors, lint issues
- Git state (current branch, ahead-of-main, uncommitted changes)
- Raw files pending ingestion
- Open question delta (pages with `[!question]` callouts)

### 5. What's Next

Forward-pointing. Include three subsections when they apply:
- **Immediate candidates** — what the next session could pick up
- **What's blocked** — items dependent on operator or external input (with dependency stated)
- **Ready for human review** — items that hit 99% readiness/progress and need operator sign-off

### 6. How to Resume

A numbered checklist a fresh agent follows top-to-bottom. NOT narrative. Example from [SESSION-2026-04-14-handoff.md](docs/SESSION-2026-04-14-handoff.md#L436):

```markdown
## How to Resume

1. CLAUDE.md (auto-loaded)
2. AGENTS.md (auto-loaded)
3. This handoff
4. wiki/backlog/operator-decision-queue.md
5. wiki/config/README.md
6. Run python3 -m tools.pipeline post to verify state
```

## Extended Sections (Conditional)

Add these only when the session warrants.

| Section | When to Include | Rationale |
|---------|----------------|-----------|
| **Session Context and Trajectory** | Long sessions (>20KB) where the arc matters | Captures the narrative shape for recall |
| **Operator Voice / Directives Verbatim** | Any session with ≥2 operator corrections | Preserves the corrective signal |
| **Architecture Decisions Made** | Any session that resolved queue items | Explicit before/after per decision |
| **Mistakes** | Any session where the operator had to correct course | META-LESSON — this is how the wiki learns from its own execution. Cite quotes, don't paraphrase. |
| **Reflection** | Deep sessions with generalizable insight | "What Worked / What Could Improve" |
| **Key Files and References** | Sessions with ≥10 file changes | Easier cross-session linking later |

## Quality Bar

| Dimension | Requirement |
|-----------|-------------|
| **Operator directives** | Verbatim. Use blockquote `> "quoted text"`. Never paraphrase, never summarize, never translate into third person. |
| **Metrics** | From fresh `pipeline post` or `pipeline status`. NOT from memory. Copy-paste the output. |
| **File references** | Absolute from repo root. Link format `[filename.md](path/to/file.md)` or with line: `[file.md:42](path#L42)`. |
| **Resume checklist** | Numbered, actionable, verifiable. Each step either reads a specific file or runs a specific command. |
| **Honesty** | If the session had mistakes, INCLUDE the Mistakes section. Claiming clean completion when it wasn't is worse than no handoff. |
| **Length** | Follows content, not prescription. Judge by whether the next agent can actually resume from what's written. |
| **Filename** | `SESSION-YYYY-MM-DD[-suffix].md`. Date MUST be the actual session date. Suffix ONLY when multiple files exist for that date. |

## Anti-Patterns (Observed in the Corpus)

> [!warning] Duplicate sections
>
> `SESSION-2026-04-08.md` has "Cross-Session Memory" appearing twice. Evidence of drafting without review. Before committing a handoff, scan for duplicate H2 headers.

> [!warning] Estimated metrics
>
> "~184 pages, roughly 1200 relationships" is worthless. The number must be exact and recent. If you haven't run `pipeline status` in the last 30 minutes, run it again.

> [!warning] Paraphrased operator speech
>
> Bad: "The operator emphasized quality."
> Good: `> "not only not dumb raw dump but smart content and then to the full requirements / standards"`
>
> The paraphrase discards the exact vocabulary the operator is trying to install as methodology. The quote is what future sessions will search for.

> [!warning] Narrative "How to Resume"
>
> Bad: "To resume, read the main files and understand the current state, then check what's next."
> Good: A numbered list of specific files and commands.
>
> Narrative resume instructions become prose the next agent skims; checklists get followed.

> [!warning] Missing file paths
>
> Bad: "Fixed the pipeline bug."
> Good: "Fixed `tools/pipeline.py:214` — argparse `allow_abbrev=False` to prevent `--top`/`--topic` collision."
>
> The first is unverifiable. The second points a future agent directly to the fix if it regresses.

> [!warning] Claiming "done" without evidence
>
> Bad: "E015 completed."
> Good: "E015 — 5 of 7 requirements implemented and tested (see commits `badbbf8`..`eb3feda`). 2 remaining: `factory-reset` safety Q, MCP tool parity. At 70% progress / 80% readiness. Review recommended before marking done."
>
> The pattern of claiming false completion is documented in `SESSION-2026-04-12-handoff-v2.md` Mistake 3. Don't repeat it.

> [!warning] Padding a quiet session
>
> If the session produced 2 commits and a fix, the handoff should be 2-4KB. Padding with restated principles, reprinted CLAUDE.md content, or generic "reflections" makes the corpus noisier without adding signal.

> [!warning] "-handoff" suffix when only one file exists
>
> `SESSION-2026-04-14-handoff.md` has a redundant `-handoff` suffix — SESSION-*.md is already unambiguous. Reserve suffixes for within-day supersession (`-part2`, `-final`, `-v2`). Going forward: bare date.

## Filename Conventions

| Pattern | When |
|---------|------|
| `SESSION-YYYY-MM-DD.md` | Default. One handoff per session. |
| `SESSION-YYYY-MM-DD-partN.md` | Multiple checkpoints within the same day (rare — prefer one final). |
| `SESSION-YYYY-MM-DD-final.md` | Supersedes earlier drafts for the same date. Previous drafts retained for audit. |
| `SESSION-YYYY-MM-DD-vN.md` | Rewrite of a prior handoff for the same date (e.g., more structured pass). |

Do NOT use `-handoff` suffix — it is redundant. Existing files with that suffix are kept as-is (don't rename), but new handoffs drop it.

## Lifecycle

```
CREATE at session end (sometimes mid-session for checkpoint)
  ↓
CONSUMED at next session start (first read after CLAUDE.md + AGENTS.md)
  ↓
ARCHIVED in docs/ indefinitely (never deleted — shows evolution of the project)
  ↓
QUOTEABLE by wiki pages (wiki links TO docs/SESSION-*.md, never reverse)
```

The handoff may be quoted by wiki pages as historical record. Example: [[super-model|Super-Model]] sources `docs/SESSION-2026-04-12-handoff-v2.md` under its `operator-vision` field. This is the ONLY legitimate wiki→handoff reference pattern: as a source, not as content.

## Relationship to Other Recording Mechanisms

| Where | What Goes There | Lifecycle |
|-------|-----------------|-----------|
| `docs/SESSION-*.md` | Session handoff — what happened this session, continuity for next | Ephemeral → archive |
| `raw/notes/` | Operator directives verbatim, logged BEFORE acting | Permanent raw source |
| `wiki/log/` | Formal log pages (per-directive, dated, frontmatter) | Permanent wiki pages |
| Claude Code memory (`~/.claude/.../memory/`) | User profile, feedback rules, quick pointers | Permanent, private, cross-session |
| `wiki/lessons/` `wiki/patterns/` `wiki/decisions/` | Synthesized knowledge extracted from sessions | Permanent, promoted through maturity lifecycle |

**Rule of thumb for what goes where:** if the next session needs it → handoff. If the ecosystem needs it (other projects, future-forever) → wiki. If only THIS agent on THIS operator's machine needs it → memory. If it came verbatim from the operator → `raw/notes/` PLUS the wiki log. See also [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]] Class 7 (Memory/Wiki Conflation).

## Template

A template handoff skeleton lives at [docs/SESSION-HANDOFF-TEMPLATE.md](docs/SESSION-HANDOFF-TEMPLATE.md). Copy, fill in, commit. The template is opinionated — it includes all invariant sections pre-labeled and leaves extended sections commented out so you can uncomment the ones you need.

## Examples from the Corpus

> [!info] Why this page uses a span of exemplars, not a single best
>
> Per the [[model-llm-wiki-standards|LLM Wiki Standards]] Exemplar Policy: standards pages default to a SINGLE BEST exemplar. Session-handoff is an explicit exception — the "good" shape varies structurally by session shape. A directive-heavy correction session has a different optimal structure than a productive multi-phase session. Showing ONE "best" handoff would mis-teach by implying all sessions should produce that shape. The span (minimum viable → directive-driven → mature phase+decisions → meta-learning) teaches the reader to match shape to context.

### Primary Annotated Exemplar — Mature Phase+Decisions Format

Reference: [SESSION-2026-04-14-handoff.md](docs/SESSION-2026-04-14-handoff.md) — 554 lines, produced alongside this standard

> [!example]- Full Walkthrough — Why Each Section Works
>
> **1. Header + Disclaimer.** The three-line header block declares (a) the date in the title, (b) the purpose in one sentence, (c) the non-wiki status. ← The disclaimer is not ceremonial — an auto-ingest pipeline reading `docs/*.md` needs this line to skip the file. The single-sentence "How to read" bullet orients the three audiences (future-self, next agent, operator) in one line.
>
> **2. Executive Summary is one screen.** One paragraph of prose + metrics snapshot (319 pages, 2089 relationships, 0 errors, 0 lint). ← Metrics are from a fresh `pipeline post`, not remembered. A reader who reads ONLY this section knows what the session produced and whether the system is healthy.
>
> **3. Session Context and Trajectory has three subsections** — Where We Started, The Arc, The Operator's Voice. ← The Arc captures the narrative shape (7 phases) so future-self can reconstruct the mental journey. The Operator's Voice section contains 7 verbatim quotes, each prefixed with what the quote corrected. These quotes are searchable by future sessions — paraphrased versions would not be.
>
> **4. What Was Done uses phase-by-phase structure** — 7 phases, each with Input / Infrastructure-fix-needed / Outputs. ← The session produced multiple parallel workstreams; flat lists would conflate them. Phases also map naturally to commits (each phase closed with a commit) so a reader can correlate narrative to git log.
>
> **5. Architecture Decisions Made is a TABLE** — 8 rows, one per P1 decision, with "Decision → Resolution → Commit" columns. ← Decisions are discrete items; prose would lose the atomicity. The commit column makes each resolution independently auditable.
>
> **6. Ready for Human Review and What's Blocked are explicit sections** — 8 items and 4 items respectively. ← Without these, operator review is implicit and items fall through cracks. Declaring "blocked on operator" externalizes the dependency instead of leaving it in the agent's head.
>
> **7. How to Resume is a numbered checklist, not prose** — 6 actionable steps, each either reading a specific file or running a specific command. ← A fresh agent can follow top-to-bottom without judgment. Narrative "resume" instructions become skimmed prose; checklists get executed.
>
> **8. Reflection section is retrospective, not self-congratulatory** — What Worked / What Could Improve as parallel bullet lists. ← Honest retrospection distinguishes "the session succeeded" from "everything went smoothly." The Could Improve notes seed future sessions.
>
> **What could still improve:** The handoff's 554 lines is approaching the upper bound where a reader may skim rather than read. The "Key Files and References" section (with 3 sub-tables totaling ~40 file references) could itself be extracted into a companion artifact-index. The Architecture Decisions table has no "confidence level" column — some decisions were more settled than others, and that nuance is lost.

### Secondary Exemplars — Other Valid Shapes

> [!example]- Minimum viable — good for a quiet session (Apr 10 final, ~4KB)
>
> Structure: Executive Summary → Final State (metrics) → What Was Done (flat list) → What's Next → How to Resume. No directives section because the session had no directives. No mistakes section because the session had no mistakes. Length matches content.
>
> See: [SESSION-2026-04-10-final.md](docs/SESSION-2026-04-10-final.md)
>
> **What could still improve:** Missing explicit "What's Blocked" subsection — quiet sessions rarely have blockers but declaring "none" explicitly is more honest than omitting.

> [!example]- Directive-driven — good for correction-heavy session (Apr 12, ~47KB)
>
> Structure: The Vision → Directive 1 → Directive 2 → ... → Directive 13 → Wiki Statistics. 13 sections each capturing a specific operator correction with verbatim quotes. The CORRECTIVE scope dominates because the session arc WAS the corrections.
>
> See: [SESSION-2026-04-12-handoff.md](docs/SESSION-2026-04-12-handoff.md)
>
> **What could still improve:** The 13 directives are presented without weighting. Some were course-corrections; some were ongoing refinements. A "significance" column or per-directive duration ("took 30% of session to resolve") would help future sessions distinguish critical vs minor corrections.

> [!example]- Meta-learning — good for sessions where mistakes happened (Apr 12 v2, ~24KB)
>
> Adds a Mistakes section with 5 numbered meta-failures, each with a verbatim operator quote. This section is what makes the handoff valuable for the next session — it encodes "what the agent did wrong this time so it doesn't happen again."
>
> See: [SESSION-2026-04-12-handoff-v2.md](docs/SESSION-2026-04-12-handoff-v2.md) — Mistake 1 through Mistake 5
>
> **What could still improve:** The Mistakes section doesn't connect to the wiki's lesson-promotion pipeline. A mistake that recurs across 3+ handoffs should trigger a lesson/principle evolution. Currently this connection is manual; it could be a scorer signal.

## How to Extend This Standard

- **New invariant section**: proven needed across ≥3 consecutive handoffs → promote from Extended to Invariant.
- **New extended section**: appeared once with clear value → add with "When to Include" guidance.
- **Drop an invariant**: missing from ≥3 consecutive handoffs with no loss of usefulness → demote to Extended or remove.
- **Retire an anti-pattern**: no occurrences in the last 5 handoffs → retain as historical warning but mark as rare.

Changes to this standard should be versioned in the page's `updated:` frontmatter field. The handoff corpus itself serves as the training set — this standard evolves by observing the corpus and promoting patterns.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Per-wiki-type standards** | [[concept-page-standards|Concept Page Standards]], [[lesson-page-standards|Lesson Page Standards]], [[reference-page-standards|Reference Page Standards]], …15 total in `wiki/spine/standards/` |
> | **What goes in wiki vs memory vs docs** | [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]] Class 7 (Memory/Wiki Conflation) |
> | **Root documentation structure** | [[root-documentation-map|Root Documentation Map]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Context files taxonomy** | [[context-file-taxonomy|Context File Taxonomy]] — handoffs are runtime-generated ephemeral context |
> | **Why verbatim logging** | [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]] and operator memory `feedback_verbatim_logging.md` |

## Relationships

- PART OF: [[model-wiki-design|Model — Wiki Design]]
- RELATES TO: [[root-documentation-map|Root Documentation Map]]
- RELATES TO: [[context-file-taxonomy|Context File Taxonomy]]
- RELATES TO: [[methodology-system-map|Methodology System Map]]
- RELATES TO: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
- BUILDS ON: [[reference-page-standards|Reference Page Standards]]

## Backlinks

[[model-wiki-design|Model — Wiki Design]]
[[Root Documentation Map]]
[[Context File Taxonomy]]
[[methodology-system-map|Methodology System Map]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[reference-page-standards|Reference Page Standards]]

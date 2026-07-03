---
title: "Synthesis — Cavekit v4: Compressed Spec-Driven Development for Claude Code (Julius Brussee, MIT-Licensed, SPEC.md + 3 Commands + Caveman Encoding + Backprop Reflex)"
aliases:
  - "Cavekit"
  - "Cavekit Synthesis"
  - "Cavekit v4"
  - "JuliusBrussee/cavekit"
  - "SPEC.md format"
  - "Caveman Ecosystem Build Layer"
type: source-synthesis
domain: tools-integration
layer: 1
status: synthesized
confidence: high
maturity: seed
created: 2026-05-04
updated: 2026-05-04
last_reviewed: 2026-05-04
sources:
  - id: cavekit-github
    type: repository
    url: https://github.com/JuliusBrussee/cavekit
    file: raw/articles/juliusbrusseecavekit.md
    title: "JuliusBrussee/cavekit — README + 9 deep-fetched files"
    description: "Authoritative open-source repository — MIT licensed, npm + Claude Code marketplace distribution. v4 default; v3.1.0 frozen at tag. Ingested 2026-05-04 per Hard Rule 6 (corpus URL routes through `pipeline fetch`)."
    ingested: 2026-05-04
  - id: caveman-synth
    type: wiki
    file: wiki/sources/tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md
    description: "Sister project — caveman (output compression). Cavekit v4 reuses caveman grammar as default for SPEC.md writes (v3 was opt-in for inter-agent chatter; v4 made it default)."
  - id: cavemem-synth
    type: wiki
    file: wiki/sources/tools-integration/src-cavemem-cross-agent-persistent-memory-julius-brussee.md
    description: "Sister project — cavemem (cross-agent memory). Same author, same caveman compression engine. Three-tool ecosystem: cavekit orchestrates · caveman compresses what agent says · cavemem compresses what agent remembers."
  - id: convergence-lesson
    type: wiki
    file: wiki/lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md
    description: "PRIMARY — cavekit is the 8th independent instance of the 2026 spec-driven agentic-build convergent pattern. Tagline 'compressed spec-driven development for claude code' is the lesson's territory verbatim. SPEC.md is the durable version-controlled first-class artifact the lesson centers on."
  - id: jsmastery-six-file-synth
    type: wiki
    file: wiki/sources/wiki-methodology/src-jsmastery-six-file-context-system-agentic-build.md
    description: "Adjacent — Six-File context system uses 6 separate markdown files; cavekit v4 distills to 1 file with 6 addressable sections (§G §C §I §V §T §B). Same convergent pattern, different shape — both valid by workload class."
  - id: fowler-spdd-synth
    type: wiki
    file: wiki/sources/wiki-methodology/src-fowler-structured-prompt-driven-development-spdd.md
    description: "Adjacent — Fowler's REASONS Canvas has 7 sections (R·E·A·S·O·N·S); cavekit's SPEC.md has 6 (§G §C §I §V §T §B). Both treat the structured spec as a durable version-controlled artifact with closed-loop sync (cavekit's backprop reflex parallels SPDD's 'fix prompt first')."
  - id: trust-layer-concept
    type: wiki
    file: wiki/domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md
    description: "Adjacent — cavekit v4's caveman-encoded SPEC.md is itself a strong instance of the trust-layer's compression-with-technical-preservation pattern at the spec-artifact layer. Same shape (compress + preserve technical substance + retrieve) at a different layer."
  - id: schema-is-the-real-product-lesson
    type: wiki
    file: wiki/lessons/03_validated/knowledge-systems/schema-is-the-real-product.md
    description: "Validated lesson — cavekit's central thesis ('the spec is the only artifact that earns its tokens') is a direct restatement of this lesson at the AI-build layer."
tags: [source-synthesis, cavekit, julius-brussee, spec-driven, claude-code, sdd, spec-md, caveman-encoding, backprop, six-section-spec, paragon-of-distillation, two-version-architecture, mit-licensed, layer-1, paper-evidence, mission-2026-05-04, operator-named-ecosystem, convergence-instance-8]
---

# Synthesis — Cavekit v4: Compressed Spec-Driven Development for Claude Code

## Summary

Cavekit ([JuliusBrussee/cavekit](https://github.com/JuliusBrussee/cavekit), MIT) is an open-source spec-driven development tool for Claude Code with two coexisting versions: **v4 (default branch) is a radical distillation** of v3.1.0 (frozen at tag) — *"one file · three commands · zero sub-agents."* v4's entire surface is **`SPEC.md` at repo root** with **six fixed addressable sections** (§G goal · §C constraints · §I interfaces · §V invariants · §T tasks · §B bugs), three slash commands (`/ck:spec` · `/ck:build` · `/ck:check`), and two utility skills (`caveman` for encoding · `backprop` for bug-to-spec protocol). Every spec write is **caveman-encoded by default** (~75% fewer tokens than prose, technical tokens preserved byte-for-byte) and uses a **mathematical-symbol vocabulary** (→ ∴ ∀ ∃ ! ? ⊥ ≠ ∈ ∉ ≤ ≥ & |) for unambiguous machine-readable shorthand. The **backprop reflex** is the load-bearing mechanism: every test failure or bug becomes a `§B` entry, and classes of bug become `§V` invariants the spec never forgets — turning bugs into permanent invariants the spec carries forward across iterations. Pipe-table shapes for `§T` (tasks: id|status|task|cites) and `§B` (bugs: id|date|cause|fix) make repeating records efficient. Cavekit v4 is **the 8th independent instance** of the [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|2026 spec-driven agentic-build convergent pattern]] — explicitly "compressed spec-driven development for claude code." Notably, v4 replaced v3.1.0's overbuilt 16-command / 12-sub-agent / 21-skill / Go-binary / autonomous-loop architecture (4,977 lines of commands → 226 lines) after the author concluded *"native Claude Code plan-then-execute is already good... it was often losing to the baseline — same work, more ceremony, more tokens."* v3 stays reachable at tag for projects that depended on the autonomous loop / parallel waves / peer review / design-system / knowledge-graph features. The two-tool ecosystem decision (caveman + cavemem + cavekit) shares a single `@cavemem/compress` engine across all three. Operator-named source 2026-05-04 (the third of three caveman-ecosystem tools the operator surfaced 2026-04-30 → completing the operator-named ecosystem at 3 of 3 ingested).

## Reference Card

> [!info] Cavekit reference card

| Field | Value |
|---|---|
| **Repository** | [JuliusBrussee/cavekit](https://github.com/JuliusBrussee/cavekit) |
| **License** | MIT |
| **Author** | Julius Brussee |
| **Tagline** | *"compressed spec-driven development for claude code — one file · three commands · zero sub-agents"* |
| **Versions** | v4 (default; the distilled core) · v3.1.0 (frozen at tag; the overbuilt original) — two-way door, both still installable |
| **Distribution** | `npx skills add JuliusBrussee/cavekit` (skills CLI) OR Claude Code marketplace `/plugin marketplace add juliusbrussee/cavekit` + `/plugin install ck@cavekit` |
| **Surface (v4)** | `SPEC.md` at repo root + 3 slash commands + 2 utility skills |
| **Six SPEC.md sections** | §G goal · §C constraints · §I interfaces · §V invariants · §T tasks · §B bugs |
| **Three commands (v4)** | `/ck:spec` (sole mutator — create/amend/backprop) · `/ck:build` (native plan→execute against spec, auto-backprops on failure) · `/ck:check` (read-only drift report) |
| **Two utility skills** | `caveman` (encoding) · `backprop` (six-step bug→spec protocol) |
| **Spec encoding** | Caveman grammar by default (in v3 it was opt-in for inter-agent chatter; v4 made it default for spec writes) |
| **Symbol vocabulary** | `→ ∴ ∀ ∃ ! ? ⊥ ≠ ∈ ∉ ≤ ≥ & \|` plus `§<S>.<n>` for section addressing |
| **Pipe-table shapes** | §T `id\|status\|task\|cites` (status: `x` done · `~` wip · `.` todo) · §B `id\|date\|cause\|fix` |
| **Sub-agents** | Zero (v4) — main Claude does the work. v3.1.0 had 12. |
| **Backprop reflex** | Every test failure → §B entry · classes of bug → §V invariants. Reflex, not opt-in. |
| **Distillation evidence** | v3 → v4: 16 commands → 3 · 12 sub-agents → 0 · 21 skills → 2 · Go binary → none · 4,977 LoC commands → 226. Self-corrected by the author who built the overbuilt version first. |
| **Confidence** | high — full README + 9 deep-fetched files (CHANGELOG · FORMAT · LAUNCH-POST · UPGRADE · 5 SKILL.md files) read at L1 depth |
| **Mission relevance** | Critical — cavekit is the **8th independent convergence instance** of [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts\|the 2026 spec-driven agentic-build pattern]] and the most distilled instance documented (1 file, 3 commands, 2 skills) — the convergent pattern's **minimum viable shape**. Completes the operator-named caveman-ecosystem coverage at 3 of 3. |

## Key Insights

> [!success] **Cavekit v4 IS the 8th convergence-lesson instance — and the most distilled.**
>
> The [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|2026 spec-driven agentic-build convergence lesson]] catalogued 7 independent instances. Cavekit v4 is **instance 8** — explicitly "compressed spec-driven development for claude code" with `SPEC.md` as the durable version-controlled first-class artifact at repo root. It is also **the most distilled** of the 8 instances: one file, three commands, two skills. Where Six-File Context System has 6 separate files for project context, cavekit v4 has 6 addressable sections in one file. Where Fowler's REASONS Canvas has 7 dimensions, cavekit's SPEC.md has 6 (§G §C §I §V §T §B). Where openspdd has 7 commands, cavekit has 3. Same convergent pattern, **distilled to its irreducible kernel.**

> [!success] **The backprop reflex — turn bugs into permanent invariants the spec never forgets.**
>
> Cavekit's structurally novel contribution: the `backprop` skill enforces a six-step protocol (TRACE · ANALYZE · PROPOSE · GENERATE TEST · VERIFY · LOG) where every test failure or bug becomes a `§B` entry, and classes of bug become `§V` invariants the spec carries forward. *"Plan-then-execute fixes the code & forgets. SDD fixes the code AND edits spec so recurrence is impossible. That edit is backprop."* This is the lesson's "closed-loop sync rule" specialized to bugs: when reality diverges via a bug, fix the spec FIRST (add §B + new §V invariant), then verify the code conforms. The §B → §V upgrade path turns isolated bugs into structural prevention.

> [!success] **Caveman encoding default for spec writes — symbol-based vocabulary multiplies the savings.**
>
> Same `@cavemem/compress` engine as the [caveman synthesis](src-caveman-prompt-output-compressor-julius-brussee.md) but with a **mathematical-symbol overlay**: `→ ∴ ∀ ∃ ! ? ⊥ ≠ ∈ ∉ ≤ ≥ & |` for unambiguous machine-readable shorthand, plus `§<S>.<n>` for section addressing. Example transformation:
>
> | Form | Token cost |
> |---|---|
> | **Prose**: "The authentication middleware must verify the token expiry on every request before allowing the handler to execute." | ~25 tokens |
> | **Caveman v1**: "auth mw ! verify token expiry @ every req before handler." | ~12 tokens |
> | **Caveman v2 with symbols**: `V1: ∀ req → auth check before handler` | ~7 tokens |
>
> Spec is loaded every invocation. **75% fewer tokens = 75% fewer dollars + faster reads.** Humans read symbols faster than prose paraphrases for invariant-shaped statements. Symbols are unambiguous (∀ has one meaning).

> [!success] **The §B → §V backprop chain is operationally identical to the convergence-lesson's "fix prompt first."**
>
> Per the [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|convergence lesson]]: *"when reality diverges, fix the prompt first — then update the code."* Per cavekit's backprop protocol: bug → §B (always) + §V (usually, when class of bug detected) → test that fails → fix code → verify → commit. **Spec change comes first; code change follows; commit captures both atomically.** This is the convergent pattern's closed-loop sync rule applied to the bug case specifically, with structural enforcement via skill protocol.

> [!success] **Six addressable sections, fixed-order, fixed-headers — the spec's structural contract.**
>
> | Section | Purpose | Shape |
> |---|---|---|
> | **§G GOAL** | One line. What code must do. | Single sentence, caveman |
> | **§C CONSTRAINTS** | Non-negotiable boundaries; tech/lang/lib locked in. | Bulleted caveman fragments |
> | **§I INTERFACES** | External surface — what world sees. | `<kind>: <name> → <shape>` (api · cmd · file · env) |
> | **§V INVARIANTS** | Numbered, testable. Each `!` MUST hold. | `V<n>: <subject> <relation> <condition>` |
> | **§T TASKS** | Pipe table. Status: `x` done · `~` wip · `.` todo. IDs monotonic. | `id\|status\|task\|cites` |
> | **§B BUGS** | Pipe table. Backprop log. Each row = bug + invariant that catches recurrence. | `id\|date\|cause\|fix` |
>
> Addressing: `§<S>.<n>` = section.item. `§V.2` = invariants section, item 2. **Commands, commits, PRs all reference by §. Zero ambiguity.** This is structured context with hard contractual shape — proto-programming for spec writes.

> [!info] **Pipe tables for §T and §B — efficient shape for repeating records.**
>
> Cavekit chose pipe tables (not JSON, not YAML, not bullet lists) for §T (tasks) and §B (bugs). Rationale named explicitly: *"that's the efficient shape for repeating records."* Markdown-renderable, grep-able, AI-readable, human-skimmable. Cell rules: literal `|` → escape as `\|`; backticks OK; cells trimmed; empty = `-`. **The format choice IS the constraint.** No JSON spec body means agents can't generate inconsistent shapes; the table contract IS the type system.

> [!info] **One-file rule — big project means more sections, not more files.**
>
> Per FORMAT.md: *"grep ceremony kills agent speed. If SPEC.md > 500 lines, compact §B (old bugs drop oldest) before splitting."* Even at scale, cavekit refuses to fragment the spec across files. Compaction (drop oldest §B entries) is the scaling primitive. The rationale: every grep/find/glob the agent runs is friction; one file = one read.

> [!info] **No sub-agents (v4) — main Claude does the work.**
>
> v4 explicitly removed all 12 of v3's named sub-agents. *"Parallel agents... look impressive. In practice they shatter flow, coordinate via tedious ledger files, and need a separate review agent to merge their disagreements. I'd rather plan once, execute serially, and ship."* This is a deliberate distillation — sub-agent orchestration is named as the primary v3 ceremony that v4 cut.

## The v3 → v4 Self-Correction (Author's Own Reflection)

> [!warning] **Cavekit v4 carries a meta-lesson — the author distilled the framework after building the overbuilt version first.**
>
> Per [LAUNCH-POST.md](https://github.com/JuliusBrussee/cavekit/blob/main/LAUNCH-POST.md):
>
> > *"I built cavekit v3 to prove that spec-driven development could give AI agents enough context to stop guessing. On that, it delivered. The part I got wrong is everything else I wrapped around it."*
>
> > *"Native Claude Code plan-then-execute is already good. It's the baseline cavekit v3 was supposed to beat. After enough sessions I realized it was often losing to the baseline — same work, more ceremony, more tokens."*
>
> > *"The spec is the only artifact that earns its tokens. Everything else that costs tokens must either save more tokens later, or the user's attention, or it gets cut."*
>
> v3 had 16 slash commands · 12 named sub-agents · 21 skills · 4,977 LoC commands · Go binary · shell hooks · stop-hook state machine · autonomous execution loop · per-task token budgets · model-tier routing · Codex peer-review bridge · knowledge-graph integration · design-system enforcement · parallel wave execution · team mode with path-scoped claims. **All cut in v4.** What kept its place: SPEC.md (the durable artifact) + caveman compression (already worked) + backprop reflex (the one mechanism SDD adds beyond plan-then-execute). The author's framing: *"That's the shape a working version of this idea was supposed to have all along. I just had to build the overbuilt version first to find it out."*
>
> **For the wiki's own discipline, this is empirical evidence at the methodology layer of [Skyscraper Pyramid Mountain](../../comparisons/cross-domain-patterns.md): the v3 → v4 distillation IS the Skyscraper-to-Pyramid path executed publicly, with the trade-offs documented in `UPGRADE.md`.**

## The Caveman Ecosystem — All 3 Tools Now Ingested

> [!info] **Three tools, one philosophy, one shared compression engine** — all 3 now in the wiki at L1 depth

| Tool | What | Layer of operation | Synthesis |
|---|---|---|---|
| [**caveman**](src-caveman-prompt-output-compressor-julius-brussee.md) | Output compression skill | What the agent **says** (~75% output token reduction) | Ingested 2026-04-30 |
| [**cavemem**](src-cavemem-cross-agent-persistent-memory-julius-brussee.md) | Cross-agent persistent memory | What the agent **remembers** (cross-session, compressed at rest) | Ingested 2026-05-04 |
| **cavekit** *(this synthesis)* | Spec-driven development | What the agent **does** (SPEC.md + 3 commands + backprop reflex) | Ingested 2026-05-04 |

**The composition**: cavekit orchestrates the build · caveman compresses what the agent says · cavemem compresses what the agent remembers. **They share `@cavemem/compress`** as the underlying engine — operationally one less thing to learn for an operator adopting any subset.

For the operator's stack, the full ecosystem stack now stacks operationally with:
- The [trust-layer epic](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md)'s 80–90% combined envelope (caveman provides the prompt-layer slice; cavemem extends to memory; cavekit extends to spec persistence — three layers of compression-with-technical-substance-preservation under one engine)
- The [[src-jsmastery-six-file-context-system-agentic-build|Six-File Context System]] — cavekit v4 is the alternative shape (1 file, 6 sections vs 6 files at project root) for the same convergent pattern
- The [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Convergence Lesson]] — **cavekit is now the 8th instance**

## Mission Alignment

Cavekit instantiates **multiple wiki concepts simultaneously**:

| Wiki concept | Cavekit instance |
|---|---|
| [Markdown-as-IaC model](../../spine/models/agent-config/model-markdown-as-iac.md) | SPEC.md is the canonical Markdown-as-IaC artifact at the spec layer — every command reads it, every command (mutating or read-only) treats it as the source of truth |
| [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts\|Spec-Driven Convergence Lesson]] | **8th independent convergence instance** — the most distilled of the 8 |
| [Schema Is the Real Product validated lesson](../../lessons/03_validated/knowledge-systems/schema-is-the-real-product.md) | Cavekit's central thesis — *"the spec is the only artifact that earns its tokens"* — is a direct restatement of this lesson at the AI-build layer |
| [P1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) | The §-addressing scheme + pipe-table shapes are infrastructure for unambiguous spec references; the backprop skill is infrastructure for the §B → §V upgrade path; the `/ck:check` drift detector is infrastructure for spec-vs-code conformance |
| [P2 — Structured Context Governs Behavior](../../lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md) | SPEC.md's six fixed sections + symbol vocabulary + pipe-table contracts program agent behavior structurally — proto-programming at the spec layer |
| [P4 — Declarations Aspirational Until Verified](../../lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md) | Every §V invariant is testable; backprop's step 4 enforces *"new invariant without test = lie. Add failing test first."* |
| [Trust-Layer compression-at-rest concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) | Cavekit's caveman-encoded SPEC.md is compression-with-technical-preservation at the spec-artifact layer — paralleling the trust-layer's concept at weights/context/memory layers |

## Open Questions

> [!question] How does cavekit v4's SPEC.md interoperate with the Six-File Context System?
> Six-File splits project context across 6 files (project-overview · architecture · code-standards · ai-workflow-rules · ui-context · progress-tracker). Cavekit v4 collapses to 1 file with 6 sections (§G · §C · §I · §V · §T · §B). Different shape, same convergent pattern. They're not direct mappings — Six-File's `ui-context` and `code-standards` don't have direct cavekit analogs (covered implicitly in §C constraints). For an operator deciding between them, the question is: project context-density preference (file-per-concern vs section-per-concern). Empirical evaluation across project sizes would close the gap.

> [!question] Can cavekit's backprop reflex be applied to the wiki's own §B-equivalent?
> The wiki's failure-mode log lives in `.claude/rules/learnings.md` (13 hard rules + judgment rules + failure-mode mappings). That IS the wiki's §B + §V combined. Could the wiki adopt a per-issue addressable scheme (`§L.13` for learning #13) so corrections, audits, and self-checks can reference issues unambiguously? Worth experiment.

> [!question] Does the v3 → v4 distillation pattern apply to the wiki's own evolution?
> The wiki has a similar overbuilt-vs-distilled tension: 16 named models · 4 principles · 26 standards pages · multiple methodology models. Some are load-bearing; some may be ceremony. The cavekit author's question — *"is this earning its tokens?"* — is operationally answerable for each wiki artifact. Worth a Skyscraper-to-Pyramid review session.

> [!question] How does cavekit v4 (no sub-agents) interact with the operator's Multica stack (orchestrator + harness + provider × 4 layers)?
> Multica orchestrates harnesses; cavekit operates within a single Claude Code session via SPEC.md. They sit at different layers and don't conflict — but operator's mental model could simplify: SPEC.md as the source-of-truth artifact, Multica as the orchestrator, AICP as the provider-routing layer, trust-layer as the compression+encryption layer. Cavekit v4 fits cleanly into the 4-layer stack at the spec-artifact layer.

> [!question] Caveman ecosystem — convergent compression engine across 3 tools; could the wiki's own export profiles use the same engine?
> The wiki has `wiki/config/export-profiles.yaml` for transforming wiki content to consumer formats. Could the export pipeline use `@cavemem/compress` to produce caveman-compressed exports for token-efficient consumer ingestion? Empirical token-savings measurement on the wiki corpus export would close a real gap and connect the trust-layer arc to the export-pipeline arc.

## How to Apply

> [!tip] Adoption checklist (for an operator considering cavekit v4 for a project)
>
> 1. **Decide which version** — v4 (default branch) for distilled core; v3.1.0 (frozen at tag) only if the project has live `context/kits/` investment OR depends on autonomous loop / parallel waves / peer review / design-system features. Per `UPGRADE.md`: it's a two-way door.
> 2. **Install** — `npx skills add JuliusBrussee/cavekit` (skills CLI, fastest) OR `/plugin marketplace add juliusbrussee/cavekit` + `/plugin install ck@cavekit` (Claude Code marketplace) OR git clone directly
> 3. **Author SPEC.md** — invoke `/ck:spec` with the project idea. Cavekit walks §G → §C → §I → §V → §T → §B and produces the file.
> 4. **For existing projects with code** — invoke `/ck:spec from-code` to distill SPEC.md from the built code. Code is the source of truth; spec follows.
> 5. **Build by tasks** — invoke `/ck:build` to plan-then-execute against §T tasks. On failure, the backprop reflex auto-records §B + drafts §V invariant.
> 6. **Audit drift** — invoke `/ck:check` for read-only drift report (§V violations · §I drift · §T stale rows). Decide remediation: spec amend OR code fix OR backprop.
> 7. **Compose with caveman + cavemem** — three tools, one ecosystem. `npx skills add JuliusBrussee/caveman` + `npm install -g cavemem && cavemem install` complete the trio. All three share `@cavemem/compress` so the spec, the agent's output, and the agent's memory all speak the same caveman dialect.
> 8. **Watch the spec grow** — when SPEC.md > 500 lines, compact §B (drop oldest entries) before splitting. The one-file rule is load-bearing.

## Relationships

- BUILDS ON: [[src-caveman-prompt-output-compressor-julius-brussee|Caveman Synthesis]] (sister project — shared `@cavemem/compress` engine; cavekit v4 made caveman default for spec writes)
- BUILDS ON: [[src-cavemem-cross-agent-persistent-memory-julius-brussee|Cavemem Synthesis]] (sister project — same compression engine; complementary memory layer)
- BUILDS ON: [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Convergence Lesson]] (**cavekit is the 8th independent instance** — the most distilled documented)
- BUILDS ON: [[model-markdown-as-iac|Model — Markdown as IaC]] (SPEC.md is the canonical Markdown-as-IaC artifact at the spec-driven-development layer)
- BUILDS ON: [[schema-is-the-real-product|Schema Is the Real Product]] (cavekit's central thesis IS this lesson restated at the AI-build layer)
- PARALLELS: [[src-jsmastery-six-file-context-system-agentic-build|JS Mastery Six-File Context System]] (alternative shape of the same convergent pattern — 6 sections in 1 file vs 6 files at project root)
- PARALLELS: [[src-fowler-structured-prompt-driven-development-spdd|Fowler SPDD]] (alternative shape — 6-section SPEC vs 7-dimension REASONS Canvas; cavekit's backprop reflex parallels SPDD's "fix prompt first" closed-loop sync)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] (§-addressing + pipe-table contracts + backprop skill + drift detector are infrastructure for spec discipline, not prose policy)
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Behavior]] (six fixed sections + symbol vocabulary + pipe-table contracts program agent behavior structurally)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] (backprop step 4: *"new invariant without test = lie. Add failing test first."*)
- RELATES TO: [[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]] (caveman-encoded SPEC.md is compression-with-technical-preservation at the spec-artifact layer; same shape at a different layer)
- RELATES TO: [[skyscraper-pyramid-mountain|Skyscraper / Pyramid / Mountain Pattern]] (cavekit v3 → v4 IS the Skyscraper-to-Pyramid distillation executed publicly with documented trade-offs)
- RELATES TO: [[methodology-evolution-protocol|Methodology Evolution Protocol]] (cavekit's two-version architecture — frozen v3.1.0 + active v4 — is a clean instance of evidence-driven versioned methodology improvement; UPGRADE.md is the protocol artifact)
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]] (cavekit v4 is a candidate concrete instantiation for solo/small-team adoption)

## Backlinks

[[src-caveman-prompt-output-compressor-julius-brussee|Caveman Synthesis]]
[[src-cavemem-cross-agent-persistent-memory-julius-brussee|Cavemem Synthesis]]
[[Spec-Driven Convergence Lesson]]
[[Model — Markdown as IaC]]
[[Schema Is the Real Product]]
[[JS Mastery Six-File Context System]]
[[src-fowler-structured-prompt-driven-development-spdd|Fowler SPDD]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[Principle 2 — Structured Context Governs Behavior]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]]
[[Skyscraper / Pyramid / Mountain Pattern]]
[[methodology-evolution-protocol|Methodology Evolution Protocol]]
[[methodology-adoption-guide|Methodology Adoption Guide]]

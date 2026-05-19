---
title: "2026-05-16 — Operator directive: RGP worker must respect second-brain knowledge, do SDD+TDD, follow SFIF, augment not rewrite, super-strong before launch"
type: note
note_type: directive
domain: log
status: active
confidence: authoritative
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: operator-directive-2026-05-16-rgp-worker-quality-bar
    type: directive
tags: [operator-directive, root-ghostproxy, ai-assistant-profile, sdd, tdd, sfif, augment-not-rewrite, super-strong-before-launch, high-standards-artifacts, second-brain-respect, "2026-05-16"]
---

# Operator directive — RGP worker quality bar (SDD+TDD, SFIF, augment-not-rewrite, super-strong-before-launch)

## Verbatim operator words (sacrosanct, 2026-05-16)

> "This AI assistant will have to respect the knowledge of the second-brain
> and respecte the super-models and models and standards and Wiki LLM and
> do proper Spec Driven Development combined with Test Driven Development.
> It will need to be super strong before we launch it. take your time I
> know this is complex, you can read more file. process more the knowledge
> and a clear intelligence so that the work is reliable. do not rewrite
> everything everytime make augmentations, improvements, upgrades,
> evolutions. it has to produce high standards artifact and do the
> workflow/things in order and properly, SFIF and all."

## Parsed constraints (the spec the YAML augmentation must satisfy)

1. **Respect second-brain knowledge** — super-models, models, standards, Wiki LLM. Profile must REFERENCE + INVOKE the methodology engine + schema + artifact-types + per-type standards + per-model standards. Not just cite — actively bind to them at gate-time.

2. **SDD + TDD combined** — Spec Driven Development AND Test Driven Development. Per-task discipline: spec exists (or author it if missing per "since it was incomplete") → test authored before code → code makes test pass → verification gate runs → status:review.

3. **Super strong before launch** — quality > velocity. Profile must NOT be installed until proven solid. Pre-launch readiness gates required.

4. **Take time, read more, process knowledge** — operator granting time budget. Methodical synthesis preferred over rushed shipping.

5. **Augment, don't rewrite** — incremental improvements / upgrades / evolutions. Surgical Edit calls preserving structure; not Write-from-scratch wholesale replacement. The v4 YAML I authored 2026-05-16 ~15:50 ET was a rewrite — operator is correcting that pattern.

6. **High-standards artifacts** — every output (task fix in root-ghostproxy / missing-task authoring / profile updates) must meet per-type page standards + per-model standards + methodology quality gates.

7. **Order + SFIF** — Scaffold → Foundation → Infrastructure → Features. Stage discipline (ALLOWED/FORBIDDEN per stage). No skipping stages.

## My error pattern (must correct going forward)

I jumped from "understand the framing" to "rewrite 480 lines of YAML" in one move. The right pattern per operator's directive is:

1. Read the second-brain's relevant knowledge (super-model, methodology, SFIF, Wiki LLM, SDD lesson, TDD pattern, standards)
2. Identify what's MISSING from the current v4 YAML versus what's required
3. Make TARGETED SURGICAL EDITS via Edit tool (not Write tool)
4. Each edit is one augmentation, addressing one missing constraint, citing the second-brain source

Going forward: augment v4 incrementally; never `Write` over the whole file again unless explicitly asked.

## Reading queue before next edit

| File | Why |
|---|---|
| `wiki/spine/models/quality/model-sfif-architecture.md` | SFIF stages + recursive application |
| `wiki/spine/models/foundation/model-methodology.md` | 9 models × 5 stages, stage discipline, ALLOWED/FORBIDDEN, gates |
| `wiki/spine/models/foundation/model-llm-wiki.md` | Wiki structure, operations, quality gates the profile must respect |
| `wiki/spine/standards/model-standards/model-methodology-standards.md` | What good methodology execution looks like |
| `wiki/spine/standards/model-standards/model-llm-wiki-standards.md` | What good Wiki LLM execution looks like |
| `wiki/log/2026-05-04-session-log-spec-driven-convergence-arc-fowler-spdd-jsmastery-six-file-context-7-instance-lesson.md` | SDD as defined / converged in this second-brain (Fowler SPDD + jsmastery + 6-file context + 7-instance lesson) |
| `wiki/spine/standards/per-type/` (sample relevant ones) | Page-type quality gates for outputs |

## Status

Logged. Reading in progress. Next augmentation will be incremental Edit-tool surgery on v4 YAML, citing each second-brain source the augmentation invokes.

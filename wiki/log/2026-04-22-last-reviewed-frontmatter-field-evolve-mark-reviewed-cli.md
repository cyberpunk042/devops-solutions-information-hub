---
title: "last_reviewed frontmatter field + evolve mark-reviewed CLI"
type: note
domain: log
note_type: completion
status: active
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources: []
tags: [log, completion]
---

# last_reviewed frontmatter field + evolve mark-reviewed CLI

## Summary

Added `last_reviewed` as an optional frontmatter field and wired `detect_stale` to honor it, resolving the aspirational-date hazard that made bulk stale-refresh unsafe. `updated:` now strictly means "content was changed." `last_reviewed:` means "operator compared the evolved page to its derived_from sources and confirmed still-current." Separate signals, separate semantics, no more false closure-by-date-bump.

## Why this was needed

`tools.evolve detect_stale` flags pages where `source.updated > page.updated`. It surfaced 22 stale pages against evolved content. But the date gap conflated two distinct realities:

1. Source got a substantive revision that invalidates or modifies the evolved page → real staleness
2. Source got a metadata bump (backlink regen, alias added, `fix: date updates` sweep) → false-positive staleness

Option 1 requires editorial work. Option 2 requires zero content change. But both manifested as identical `source_date > page_date` signals. The natural fix — bump `page.updated` to close the flag — violates [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Are Aspirational Until Infrastructure Verifies Them]]: you'd be declaring "content reconciled" without having actually compared.

Evidence of the false-positive mechanism in git: commit `6f00e1f` ("fix: L2 sweep — weave test + 100% reachability + date updates") touched 189 files, almost all with a 2-line diff. That's a bulk date-field churn that flipped dozens of pages' `updated:` forward without content changes, which then cascaded into derived-page staleness flags.

## What changed

| File | Change |
|------|--------|
| `wiki/config/wiki-schema.yaml` | Added `last_reviewed` as optional field |
| `tools/manifest.py` | Propagates `last_reviewed` into the manifest so consumers can read it |
| `tools/evolve.py` | `detect_stale` compares `source.updated` against `max(page.updated, page.last_reviewed)`. New `mark_reviewed()` function. New `mark-reviewed` CLI mode with `--page <slug\|title\|path>` flag. |

## Usage

```bash
# See what's flagged
python3 -m tools.evolve stale

# After reading both the evolved page and its source, if still current:
python3 -m tools.evolve mark-reviewed --page "Harness Ownership Converges Independently Across Projects"

# Or use slug / path:
python3 -m tools.evolve mark-reviewed --page harness-ownership-converges-independently-across-projects
python3 -m tools.evolve mark-reviewed --page lessons/.../harness-ownership-converges-independently-across-projects.md
```

If the source change DOES require revising the evolved page: edit the evolved page's content AND set a newer `updated:` — `last_reviewed` is only for the "still current, no revision needed" signal.

## Invariants to preserve going forward

- Do not edit `updated:` to close a stale flag unless the content genuinely changed. Use `mark-reviewed`.
- `last_reviewed` must only be set by an operator (or automation) that has actually compared the evolved page against each newer source. Automated sweeps that don't read the pages would re-create the aspirational-declaration problem.
- Do not propagate `last_reviewed` via pipeline auto-edits — it is a human-in-the-loop signal.

## Verified

- Ran `evolve stale`: 22 flagged.
- Ran `evolve mark-reviewed --page "Context Compaction Is a Reset Event"`: stamped `last_reviewed: 2026-04-22`, kept `updated: 2026-04-13` untouched.
- Re-ran `evolve stale`: 21 flagged. The newly-marked page dropped off.
- Ran `evolve mark-reviewed` on "Principle — Declarations Are Aspirational…" (its 3 stale sources are pages I promoted seed→growing today, content-neutral).
- Pipeline post: 0 validation errors, A+ grade held at 99.

## Remaining stale list (20 pages) — editorial, not mechanical

The 20 remaining stale flags need per-page review. Grep the `6f00e1f` commit for a given source file — if the diff shows only aliases/backlinks/whitespace/date fields, the evolved page is safe to `mark-reviewed`. If the diff shows body-section or matrix-row changes, the evolved page needs real revision first.

## Relationships

- BUILDS ON: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Are Aspirational Until Infrastructure Verifies Them]]
- RELATES TO: [[aspirational-naming-in-lifecycle-code|Aspirational Naming in Lifecycle Code]]
- RELATES TO: [[schema-aspirationalism-defining-required-sections-you-neve|Schema aspirationalism]]

## Backlinks

[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Are Aspirational Until Infrastructure Verifies Them]]
[[aspirational-naming-in-lifecycle-code|Aspirational Naming in Lifecycle Code]]
[[Schema aspirationalism]]

---
title: "Lint tooling fixes + backlog modules index gap — wiki health D → A+"
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

# Lint tooling fixes + backlog modules index gap — wiki health D → A+

## Summary

Pickup-cold session on fresh Ubuntu-24.04 WSL (post-migration). Per [[wsl-ubuntu-migration-handoff|wsl-ubuntu-migration-handoff]], the migration's P0 items were all already done (CUDA 12.6, uv, AICP venv, ktransformers loads, dual-GPU detected). Main remaining setup gap was `.mcp.json` (operator ran `tools.setup` — generated + auto-connected authorized sisters). Then regathered health via `gateway health` and found the wiki was flagged D/69. Traced it and fixed two real tool bugs that were inflating the issue count.

## What was actually wrong

### 1. Lint exemplar check was broken for piped wikilinks (69 false positives)

`_check_standards_exemplars` in [[tools/lint.py]] built a title-only set and compared the raw wikilink body (`slug|Title`) as one string against that set. Every piped wikilink in a standards page's Gold Standard section was flagged "not found" — 69 false positives across 5 standards files.

**Fix:** reuse `_collect_page_titles` (already includes slugs AND titles), split on `|`, accept either half. Also strip inline code spans so bare `` `[[wikilink]]` `` prose in standards docs isn't flagged (was hitting `model-llm-wiki-standards.md:316`).

### 2. rebuild_backlog_index skipped modules/ (24 orphans)

`rebuild_backlog_index` in [[tools/common.py]] built indexes for `milestones/`, `epics/`, and `tasks/`, but `backlog/modules/` had no `_index.md` ever generated. The `_check_orphan_pages` lint defines orphan as "not listed in any `_index.md`" — so every module in `modules/` was counted as orphaned despite parent epics linking to them. Backlog `_index.md` said `See [modules/](modules/)` — unhelpful dir link.

**Fix:** added module collection (reads frontmatter: id from first two dash-segments, title, priority, status, current_stage, readiness, epic) + writer for `modules/_index.md` mirroring the `tasks/_index.md` pattern. Updated top-level backlog index to point at `modules/_index.md`.

### 3. Six filenames with illegal characters (breaking markdown link parse + operator-readability)

The filename lint was already flagging parentheses / non-ASCII em-dashes / `+` characters. The walkthrough-c file's parens specifically broke the orphan check's markdown regex (`\[title\]\(file-with-\(parens\).md\)` — regex stops at first `)`). Renamed all 6 + rewrote 14 inbound wikilinks in a single Python pass.

## Scorecard

| Dimension | Before | After |
|-----------|-------:|------:|
| Composite | 69 / D | 99 / A+ |
| validation (weight 30) | 0 | 100 |
| Blocking lint issues | 25 | 0 |
| Advisory lint issues | 73 | 3 |

Remaining 3 advisories are lesson-pages ≥80 lines without `> [!...]` callouts — content-aware work (needs authorial judgment on what to pull out), not mechanical. Left as-is.

## Files changed

- [[tools/lint.py]] — exemplar check: reuse `_collect_page_titles`, handle `slug|Title` split, strip inline code spans
- [[tools/common.py]] — `rebuild_backlog_index` now generates `wiki/backlog/modules/_index.md`
- `wiki/backlog/modules/_index.md` — new, 24 rows
- `wiki/backlog/_index.md` — points at `modules/_index.md` now
- 6 lesson/log filenames renamed to ASCII-safe slugs; 14 wiki pages had wikilinks updated:
  - `per-task-cost-grows-monotonically-across-multi-task-runs-(co` → `...-multi-task-runs`
  - `schema-aspirationalism-—-defining-required-sections-you-neve` → no em-dash
  - `aicp-stage-3-hardware-unlocked-2026-04-17-—-19gb-vram-dual-g` → no em-dash
  - `gateway-identity-parser-fragility-+-forwarder-contribute-tar` → no plus
  - `openfleet-identity-profile-—-agents.md-layer-1-upgrade-compl` → no em-dash, no mid-name `.md`
  - `walkthrough-c-(openfleet)-ground-truth-verification-2026-04-` → no parens

## Lessons surfaced

1. **"Blocking" in the health composite ≠ "blocking" in pipeline post.** `pipeline post` returned Status: PASS with 25 lint issues. The gateway health dim counted those same 25 as 0/30 and dropped the grade to D. Two different definitions of "blocking" for the same numbers — future readers will hit the same confusion.

2. **Filename validation and markdown-link parsing are coupled.** Parens in filenames don't just fail a style check — they silently break markdown link resolution in `_index.md` files (regex stops at first `)`), which manifests as false orphan flags downstream. The filename lint is load-bearing for the orphan lint.

3. **rebuild_backlog_index completeness gap.** Modules were added as a first-class backlog artifact after the initial `rebuild_backlog_index` was authored. The function wasn't updated to produce their index, and since `pipeline post` passed (orphans are advisory-ish in the renderer but not in the composite), the gap went unnoticed until we ran `gateway health`.

## Next steps (handoff)

- K2.6 smoke test (migration handoff step 4.8) still pending — deferred because LocalAI setup is running in parallel and the dual-GPU optimization config (E008 M003) isn't authored yet; naive run risks OOM per handoff pitfall #3.
- 3 unstyled lessons remain advisory — revisit if authoring a callout-richness pass.
- Queue items Q53, Q57, Q58, Q59 still open — operator decisions, not agent-closeable.

## Relationships

- BUILDS ON: [[wsl-ubuntu-migration-handoff|wsl-ubuntu-migration-handoff]]
- RELATES TO: [[2026-04-22-wsl-migration-to-ubuntu-24-04|2026-04-22-wsl-migration-to-ubuntu-24-04]]

## Backlinks

[[wsl-ubuntu-migration-handoff|wsl-ubuntu-migration-handoff]]
[[2026-04-22-wsl-migration-to-ubuntu-24-04|2026-04-22-wsl-migration-to-ubuntu-24-04]]

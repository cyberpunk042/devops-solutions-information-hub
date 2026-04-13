---
title: Operations Plan — Wiki Post-Ingestion Validation
aliases:
  - "Operations Plan — Wiki Post-Ingestion Validation"
  - "Operations Plan: Wiki Post-Ingestion Validation"
type: operations-plan
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: pipeline-post
    type: file
    file: tools/pipeline.py
tags: [operations-plan, post-ingestion, validation, pipeline]
---

# Operations Plan — Wiki Post-Ingestion Validation
## Summary

Sequential operations plan for validating the wiki after any content change. This is the deterministic 6-step pipeline post chain — any agent can execute it mechanically. Run after every ingestion, every edit, every evolution. If any step fails, the change is not complete.

## Prerequisites

- [ ] Python 3.11+ installed with venv at `.venv/` (verify: `.venv/bin/python --version`)
- [ ] Wiki pages exist in `wiki/` directory (verify: `ls wiki/`)
- [ ] Config files present: `wiki/config/wiki-schema.yaml`, `wiki/config/quality-standards.yaml` (verify: `ls wiki/config/*.yaml`)
- [ ] At least one wiki page was created or modified since last run

## Steps

### Step 1: Rebuild Domain Indexes

- **Action:** Regenerate `_index.md` in every domain folder and layer folder (lessons/, patterns/, decisions/, spine/)
- **Expected output:** Index files updated with current page listings. Curated content above `## Pages` marker preserved.
- **Validation:** `ls wiki/domains/*/_index.md wiki/lessons/_index.md wiki/patterns/_index.md wiki/decisions/_index.md` — all exist
- **Rollback:** Indexes are regenerated from page metadata — re-run this step to fix

### Step 2: Regenerate Manifest

- **Action:** Rebuild `wiki/manifest.json` from all page frontmatter
- **Expected output:** JSON file with page count, type distribution, domain stats, relationship count, maturity distribution
- **Validation:** `python3 -c "import json; d=json.load(open('wiki/manifest.json')); print(d.get('total_pages', 0))"` — returns a number >0
- **Rollback:** Manifest is regenerated from pages — re-run

### Step 3: Validate All Pages

- **Action:** Check every page against `wiki/config/wiki-schema.yaml` (required fields, enums, sections) and `wiki/config/artifact-types.yaml` (per-type thresholds)
- **Expected output:** 0 validation errors. Warnings are advisory.
- **Validation:** Exit code 0 from the validate step. If errors >0, the chain reports FAIL.
- **Rollback:** Fix the page(s) with errors, re-run from step 3

### Step 4: Regenerate Wikilinks

- **Action:** Convert ``[[Page Title]]`` wikilinks to Obsidian-compatible format for graph view
- **Expected output:** Wikilinks updated in all pages. Backlinks sections regenerated.
- **Validation:** Spot-check one page: `grep "## Backlinks" wiki/spine/model-methodology.md` — section exists
- **Rollback:** Re-run — wikilinks are regenerated from relationship sections

### Step 5: Run Lint Checks

- **Action:** Health checks: orphan pages, dead relationships, thin pages, stale pages, duplicate detection, filename hygiene
- **Expected output:** Lint report with issue count. Issues are advisory — they don't block the chain.
- **Validation:** Review lint output for new issues. Acceptable: existing advisory issues. Not acceptable: new errors introduced by the change.
- **Rollback:** Fix lint issues in the pages, re-run from step 1

### Step 6: Rebuild Layer Indexes

- **Action:** Rebuild `_index.md` for layer directories (lessons/, patterns/, decisions/, spine/), including spine/domain-overviews/ and spine/learning-paths/
- **Expected output:** Layer indexes reflect current page listings
- **Validation:** `grep -c ".md" wiki/lessons/_index.md` — returns count matching actual lesson pages
- **Rollback:** Re-run

## Rollback

If the pipeline fails partway through:
1. Check which step failed (the pipeline reports step-by-step)
2. Fix the underlying issue (usually a page with invalid frontmatter or missing section)
3. Re-run `python3 -m tools.pipeline post` from the beginning — all steps are idempotent

The pipeline never modifies page content — it only regenerates indexes, manifests, and wikilinks. Rollback is always "fix the page, re-run."

## Completion Criteria

- [ ] `python3 -m tools.pipeline post` exits with `Status: PASS`
- [ ] Validation errors: 0
- [ ] No new lint issues introduced (compare before/after lint count)
- [ ] manifest.json page count matches expected total

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- IMPLEMENTS: [[model-llm-wiki|Model — LLM Wiki]]
- RELATES TO: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]

## Backlinks

[[model-llm-wiki|Model — LLM Wiki]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[stage-gate-methodology|Stage-Gate Methodology]]

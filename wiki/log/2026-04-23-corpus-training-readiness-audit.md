---
title: "Corpus Training Readiness Audit (T060) — E012 Wiki-Assistant"
type: note
domain: knowledge-systems
note_type: completion
status: synthesized
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: t060-audit-wiki-corpus-training-readiness
    type: wiki
    file: wiki/backlog/tasks/T060-audit-wiki-corpus-training-readiness.md
  - id: e012-m002-wiki-assistant-candidate-a
    type: wiki
    file: wiki/backlog/modules/e012-m002-wiki-assistant-candidate-a.md
tags: [note, completion, t060, e012, corpus, audit, training-readiness, wiki-assistant, sft, qa-pairs]
---

# Corpus Training Readiness Audit (T060)

## Summary

Audited the 455-page wiki corpus on 2026-04-22 to determine whether it supports Wiki-Assistant (Candidate A) SFT training with the 200–500 pair target. **Verdict: READY with margin.** The corpus has 260 Q&A-shape candidate pages; at 1–2 pairs per page, the supply is 260–520 pairs — comfortably above the target floor. Spine-layer content (71 pages) provides the most canonical training material; `concept` and `reference` types dominate the Q&A-friendly surface.

## What Was Done

Ran a direct analysis of `wiki/manifest.json` to count pages by type, domain, status, maturity, and layer. Cross-referenced against E012 M002's training-data requirements. No wiki content changed; pure analytical pass.

## Corpus shape (2026-04-22)

**Total pages: 455**

### By type (top 10)

| Type | Count | Q&A-friendly? |
|------|-------|---------------|
| concept | 113 | ✓ prime target |
| lesson | 60 | ✓ (narrative but Q-extractable) |
| source-synthesis | 54 | ✓ prime target |
| reference | 34 | ✓ prime target |
| task | 32 | ✗ (too short + procedural) |
| note | 31 | ✗ (too session-specific) |
| pattern | 30 | ✓ prime target |
| epic | 28 | ✗ (structural, not domain content) |
| decision | 25 | ✓ (rationale-rich) |
| module | 24 | ✗ (structural) |

### By status

| Status | Count | % | Usable for SFT? |
|--------|-------|---|-----------------|
| synthesized | 340 | 75% | ✓ yes |
| draft | 71 | 16% | ⚠ review case-by-case |
| active | 34 | 7% | ✓ yes |
| other (done, in-progress, stale) | 10 | 2% | mixed |

Most corpus content is status=synthesized, which means it has been processed through the ingestion pipeline and meets the schema. Only a small tail (10 pages) is non-synthesized mature content; that tail is not a concern for training.

### By layer

- **Spine**: 71 pages (most canonical; methodology, standards, references)
- **Non-spine**: 384 pages (lessons, notes, backlog items, source syntheses)

Spine content is the highest-signal training material because it encodes the project's invariants (principles, models, standards) rather than ephemeral session state.

### Relationships density

- **Relationships total**: 2,767
- **Rels per page**: 6.08

That's a well-connected knowledge graph. High relationship density means the cross-link-suggester adapter (E012 M004) has strong ground-truth labels to learn from.

## Q&A-shape candidate count

Pages whose type is `concept`, `standard`, `model`, `pattern`, `principle`, `verb`, `reference`, `decision`, or `synthesis`:

**260 pages in the right shape.** (standards in this corpus use `type: concept` with `layer: spine`; see schema notes in memory.)

### SFT pair estimate

| Strategy | Pages | Pairs/page | Total pairs |
|----------|-------|-----------|-------------|
| Conservative (1 per page) | 260 | 1 | 260 |
| Typical (1.5 per page) | 260 | 1.5 | 390 |
| Ambitious (2 per page, multiple facets per page) | 260 | 2 | 520 |

Wiki-Assistant target: **200–500 pairs** (from [[e012-m002-wiki-assistant-candidate-a]] Done-When). All three strategies hit or exceed the floor; the typical case lands dead-center. **Corpus supply is adequate.**

## Recommendations for T061 (SFT dataset generator)

1. **Prime targets first**: 113 concepts + 34 references + 4 principles + 30 patterns = 181 canonical methodology pages. Generate 2 pairs per page from these = ~360 pairs. That alone covers the target.
2. **Secondary pool**: 54 source-syntheses + 25 decisions = 79 pages, 1 pair per page = 79 pairs. Reserve as holdout pool or augmentation if primary pool under-delivers.
3. **Exclude**: task, note, epic, module, milestone, operations-plan, learning-path types — these are structural, session-specific, or procedural, not Q&A-shaped.
4. **Template types**:
   - Concept pages → "What is X? / Why does X exist? / When to use X?" questions
   - Reference pages → "Look up <field> for <entity>" questions
   - Pattern pages → "When do I apply pattern X? What problem does it solve?" questions
   - Principle pages → "Why does the methodology require X?" questions
   - Decision pages → "Why was X chosen over Y?" questions

## Validation

> [!success] Corpus is ready for Wiki-Assistant training
> 260 Q&A-shape candidate pages, 2,767 relationships, 75% synthesized status. Supply 260–520 SFT pairs against a 200–500 target. No content-expansion blocker for T061.

## Concerns Raised

- **Maturity field is mostly "growing"** (282 pages) or empty (117 pages). Only 1 page is `mature`. This reflects the wiki's rapid-growth phase; it's not a quality issue for training, but it does mean the content is still evolving. Recommendation: lock Wiki-Assistant v1 to a tagged snapshot so future wiki edits don't invalidate the training set.
- **Draft pages (71)** should be excluded from SFT generation unless individually promoted to `synthesized` first. T061's generator must filter by status.
- **Q&A template quality matters more than page count now.** With 260 pages already in-shape, the binding constraint shifts to template design (T070 covered adapter datasets; extend that methodology here).

## Next Steps

- **T061** (SFT dataset generator) can proceed — corpus supply is not the blocker.
- **T060 → done**. No corpus-expansion follow-up required before E012 kicks off.
- When RAM lands (2026-04-23) and Unsloth installs (T058), training can move immediately to T061 without corpus prep.

## Relationships

- RELATES TO: [[T060-audit-wiki-corpus-training-readiness|T060-audit-wiki-corpus-training-readiness]]
- RELATES TO: [[e012-m002-wiki-assistant-candidate-a|e012-m002-wiki-assistant-candidate-a]]
- RELATES TO: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]

## Backlinks

[[T060-audit-wiki-corpus-training-readiness|T060-audit-wiki-corpus-training-readiness]]
[[e012-m002-wiki-assistant-candidate-a|e012-m002-wiki-assistant-candidate-a]]
[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]

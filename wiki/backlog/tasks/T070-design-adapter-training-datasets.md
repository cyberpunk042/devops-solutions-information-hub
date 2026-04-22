---
title: "T070 — Design 3 Adapter Training Datasets (methodology, compliance, relationship)"
type: task
domain: backlog
status: draft
priority: P2
task_type: task
current_stage: design
readiness: 90
progress: 0
stages_completed: [document, design]
artifacts:
  - wiki/log/2026-04-23-adapter-dataset-design.md
estimate: M
epic: "E012"
module: "E012-m004"
depends_on: []
confidence: medium
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e012-m004-multi-lora-adapter-architecture-e
    type: wiki
    file: wiki/backlog/modules/e012-m004-multi-lora-adapter-architecture-e.md
tags: [task, p2, e012, dataset-design, multi-lora, adapters, methodology, compliance, relationships]
---

# T070 — Design 3 Adapter Training Datasets

## Summary

Design the SFT dataset schema for each of the 3 planned adapters: **methodology-assistant**, **compliance-checker**, **relationship-suggester**. Specifies the prompt template, expected output format, example sources (where to mine training data from), target pair count, and holdout split per adapter. Pure design work — no compute, no GPU. Runnable today.

## Done When

- [ ] For each of the 3 adapters, documented:
  - prompt template (jinja or equivalent)
  - expected output format (free-text, structured JSON, markdown)
  - data sources (which wiki pages / pipeline logs / cross-ref graph to mine)
  - target pair count (≥100 per adapter)
  - holdout split (typically 10–20%)
  - accuracy metric (exact match / BLEU / structured-field match)
- [ ] Sample 5 hand-authored pairs per adapter demonstrate the template works
- [ ] Output at `wiki/log/2026-04-23-adapter-dataset-design.md`
- [ ] Decision: which adapter to train first (ordering by data-availability × expected value)

## Procedure

### methodology-assistant

Input: short question about a methodology concept.
Output: cite-correct explanation referencing the appropriate wiki page.
Source: wiki/spine/standards/, wiki/spine/models/, wiki/spine/principles/ pages — generate Q&A from their summaries + examples sections.

Template (example):
```
Q: What does the "<verb>" verb mean in this wiki's methodology?
A: The <verb> verb is defined at <path>. It means <summary>. Typical usage: <example>. Preconditions: <list>.
```

### compliance-checker

Input: a draft wiki page with known lint/schema issues.
Output: a numbered list of specific fixes with line references.
Source: pipeline lint logs + git history of "fix schema" commits — each commit's diff forms (buggy_page, fixed_page) pair. Synthesize from real lint output.

Template (example):
```
Input:
---
title: "..."
type: task
...
---
...

Output:
1. Line 10: "estimate: 15min" → use enum value "XS"
2. Line 23: missing "Relationships" section (schema requires it)
3. Line 45: dead wikilink [[missing-page]] — target not found in manifest
```

### relationship-suggester

Input: a new page's summary + frontmatter.
Output: top-N suggested relationships (BUILDS ON, FEEDS INTO, RELATES TO) with target page titles.
Source: mine wiki-manifest.json — treat existing relationships as positive labels; use page-title similarity + cross-references as features.

Template (example):
```
Input:
Title: "<new page title>"
Type: <type>
Summary: <1-2 paragraphs>

Output:
BUILDS ON: [[target-1-slug]]    (reason: same domain, foundational concept)
FEEDS INTO: [[target-2-slug]]   (reason: produces artifacts this page consumes)
RELATES TO: [[target-3-slug]], [[target-4-slug]]
```

### Write the design doc

```bash
cd /home/jfortin/devops-solutions-research-wiki
python3 -m tools.pipeline scaffold note "2026-04-23-adapter-dataset-design"
$EDITOR wiki/log/2026-04-23-adapter-dataset-design.md
# Include 5 hand-authored examples per adapter
python3 -m tools.pipeline post
```

## Rollback

Design doc can stay as a historical design artifact. No code artifacts produced.

## Relationships

- PART OF: [[e012-m004-multi-lora-adapter-architecture-e|e012-m004-multi-lora-adapter-architecture-e]]
- PART OF: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]

## Backlinks

[[e012-m004-multi-lora-adapter-architecture-e|e012-m004-multi-lora-adapter-architecture-e]]
[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]

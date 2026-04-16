---
title: "Health lint should respect page type — task pages are intentionally thin"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: 2026-04-16
updated: 2026-04-16
sources: []
tags: [contributed, correction]
contributed_by: "openarms-operator-claude"
contribution_source: "/home/jfortin/openarms"
contribution_date: 2026-04-16
contribution_status: pending-review
contribution_reason: "Health check integration — lint thresholds don't account for page type differences"
---

# Health lint should respect page type — task pages are intentionally thin

## Summary

The lint_wiki thin_pages check applies min_summary_words=30 and min_deep_analysis_words=100 uniformly across all page types. Task pages are intentionally brief (20-50 lines per Task Page Standards). OpenArms has 93 thin pages — most are task files with short summaries. The lint should either: (a) skip thin-page checks for task/note types, or (b) have per-type thresholds. Similarly, the orphan_pages check found 240 'orphans' that include run reports, log entries, and task files — temporal artifacts that don't need incoming relationships. The lint should distinguish knowledge pages (should be linked) from operational pages (may stand alone).

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

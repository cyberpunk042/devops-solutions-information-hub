---
title: "13-Gate Pipeline Composability with Second-Brain 5-Tier Maturity + MCP Tool Layer"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "PRIMARY parent — 13-gate pipeline central pattern; this piece extends with cross-cutting composability map"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — promotion-mechanism feeds into 5-tier maturity progression"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Sibling — composite metric is the operational-evidence input for tier promotion"
  - id: refreshed-decision-package
    type: wiki
    file: wiki/log/2026-05-08-ready-for-review-decision-package-refresh-52-pieces-9-phases-complete.md
    description: "Sibling decision-package — operator-confirmation gate for tier promotion"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — composability MUST resist meta-meta-substitution at integration layer"
tags: [composability-map, 13-gate-pipeline, 5-tier-maturity, mcp-tool-layer, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# 13-Gate Pipeline Composability with Second-Brain 5-Tier Maturity + MCP Tool Layer

## Summary

The 13-gate pipeline (per piece #1) is a single-project enforcement substrate; the second-brain (this wiki) is a multi-project knowledge substrate with 5-tier maturity progression (00_inbox → 01_drafts → 02_synthesized → 03_validated → 04_principles); MCP tools are the programmatic-API layer. This piece maps how the three layers compose: composite-compliance metric (gate #12) FEEDS tier promotion; tier promotion enables /opt knowledge-reuse (Insight 5b); MCP tools query both layers programmatically. Per substitution-pattern Insight 5b: documenting the 13-gate pipeline alone is partial — its operational meaning emerges from composing with the second-brain promotion-mechanism + MCP query layer. This piece closes the cross-cutting composability gap.

## Pattern Description

### Layer 1: 13-gate pipeline (per-project enforcement substrate)

13 gates × 4 lifecycle layers (cold-start / 9 PreToolUse / 2 post-action / 2 measurement) emit per-axis fire-counts → cycle-history → composite-compliance % per cycle + per-30-day rolling.

### Layer 2: Second-brain 5-tier maturity progression (multi-project knowledge substrate)

```
TIER 0: 00_inbox
  - Raw operator-stated content + agent-aggregated raw notes
  - No operational claim; just captured
  - Examples: raw/notes/*.md (operator-verbatim); raw/transcripts/

TIER 1: 01_drafts
  - Agent-authored synthesis with `authorship: agent-authored` flag
  - Schema-validated (pipeline post 0 errors)
  - NO empirical operational claim yet
  - Examples: wiki/lessons/01_drafts/, wiki/patterns/01_drafts/

TIER 2: 02_synthesized
  - Operator-confirmed; promoted from agent-authored → operator-confirmed
  - Cross-references stable; bidirectional citations clean
  - SOME empirical evidence (1-3 instances; not yet sustained)
  - Examples: wiki/lessons/02_synthesized/, wiki/patterns/02_synthesized/

TIER 3: 03_validated
  - Empirically-verified across 30+ days
  - Composite-compliance ≥85% sustained per piece #18
  - Cross-cited from multiple projects (sister-project usage)
  - Examples: wiki/lessons/03_validated/

TIER 4: 04_principles
  - Promoted to governing principle (cross-project canonical)
  - Multiple validated lessons converge to abstract principle
  - Examples: wiki/lessons/04_principles/ (P1 / P2 / P3 / P4 already at this tier)
```

### Layer 3: MCP tool layer (programmatic-API substrate)

```
Wiki-query MCP tools:
  - wiki_search        : full-text search across wiki
  - wiki_read_page     : read specific page by path or title
  - wiki_list_pages    : enumerate by domain/type
  - wiki_gateway_query : query methodology / models / fields / chains
  - wiki_gateway_orient: orientation report

Wiki-state MCP tools:
  - wiki_status        : wiki health / counts / pending
  - wiki_gaps          : gap analysis with recommendations
  - wiki_gateway_health: composite quality score
  - wiki_gateway_compliance: super-model adoption tier + gaps

Wiki-mutation MCP tools (for /opt second-brain only):
  - wiki_post          : run post-ingestion 6-step chain
  - wiki_crossref      : find new connections
  - wiki_log           : add log entry
  - wiki_gateway_contribute: contribute lesson back
  - wiki_distill       : knowledge-distillation pipeline
```

### Composability — how the 3 layers interact

**Layer 1 → Layer 2 promotion**:

```
13-gate pipeline produces composite-compliance metric (gate #12)
↓
30-day rolling composite ≥85% per axis sustained
↓
Operator-confirms via /promote slash command (per impl-spec #8 promotion ceremony)
↓
authorship frontmatter: agent-authored → operator-confirmed
↓
File location moves: 01_drafts/ → 02_synthesized/
↓
Tier 1 → Tier 2 promotion complete
```

**Layer 2 → Layer 3 query consumption**:

```
After tier 2+ promotion, MCP wiki_search returns the piece as canonical
(prior to promotion: returned with "(agent-authored DRAFT)" annotation per piece C06)
↓
Sister-projects' agents query wiki via MCP for guidance
↓
Cross-project knowledge-reuse activates per Insight 5b
```

**Layer 3 → Layer 1 feedback loop**:

```
MCP wiki_gateway_compliance queries identify gaps in adoption
↓
Cross-project pattern-recurrence (impl-spec #11 cross-cycle aggregator)
identifies pieces with recurring relevance
↓
Pieces with high cross-project relevance get prioritized for tier 3 → tier 4 promotion
↓
Tier 4 governing principles influence per-project 13-gate pipeline weights (impl-spec #12)
```

### Visualization (composability axis)

```
                     ┌──────────────────────┐
                     │  Layer 4: Tier 4     │
                     │  Governing Principles │
                     └─────────┬────────────┘
                               ▲ promotion
                               │ via empirical convergence
                     ┌─────────┴────────────┐
                     │  Layer 3: Tier 3     │
                     │  03_validated        │
                     └─────────┬────────────┘
                               ▲ promotion
                               │ via 30-day rolling ≥85%
                     ┌─────────┴────────────┐
                     │  Layer 2: Tier 2     │   ◄── /promote ceremony
                     │  02_synthesized      │       (operator-confirmed)
                     └─────────┬────────────┘
                               ▲
                               │
                     ┌─────────┴────────────┐
                     │  Layer 1: Tier 1     │   ◄── 13-gate pipeline
                     │  01_drafts/seed      │       runs here per-project
                     └─────────┬────────────┘
                               ▲
                               │
                     ┌─────────┴────────────┐
                     │  Layer 0: Tier 0     │   ◄── raw operator-verbatim
                     │  00_inbox/raw notes  │       captured at intake
                     └──────────────────────┘

  MCP TOOL LAYER: queries across all 5 tiers + state + mutation
  ─────────────────────────────────────────────────────────────
  Tier 0: read-only (intake)
  Tier 1: wiki_post + wiki_crossref + wiki_log (active authoring)
  Tier 2-4: read-only via wiki_search/wiki_read_page
            promotion via /promote (operator-confirmed only)
```

### Operator-decision points at each composability boundary

```
Boundary 0→1: agent-author capture (silent; auto-tag per impl-spec #8)
Boundary 1→2: operator-confirmation via /promote (operator-territory)
Boundary 2→3: empirical-evidence-driven (composite ≥85% / 30 days)
Boundary 3→4: cross-project convergence (multiple validated lessons → principle)
```

### Anti-patterns (substitution-pattern at composability layer)

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Promote piece to tier 2 WITHOUT empirical evidence | Composite metric not yet sustained; promotion is aspirational | Wait for ≥85% / 30 days OR explicit operator-grant |
| Cite tier 1 piece as canonical (without DRAFT annotation) | Per piece C06 fabrication-cure; tier 1 IS DRAFT | Citation discipline (impl-spec #8 Read-time banner) |
| MCP query treats all tiers as equivalent | Tier 1 DRAFTs surface as canonical; downstream consumers misled | wiki_search returns annotation per tier |
| Implement 13-gate pipeline without /opt knowledge-reuse | Per Insight 5b: agents re-author existing /opt content | Input-discipline gate (impl-spec #1) CHECK 3 (opt_pieces_loaded) |
| Promote 13-gate pipeline to tier 4 (governing principle) prematurely | Single-project evidence ≠ governing principle | Tier 3 cross-project validation gate first |

## When To Apply

Apply this composability map when:
- Project has implemented 13-gate pipeline (or planning to)
- /opt second-brain is reachable as knowledge resource
- MCP tool layer is operational (wiki_* tools available)
- Pain-point cluster overlap with /opt existing lessons (Insight 5b knowledge-reuse opportunity)
- Operator considers tier-promotion ceremony for any agent-authored piece
- Cross-project propagation is goal (sister projects consume promoted lessons)

## Instances

**Instance 1: this work block's 52 pieces are all at Tier 1**:
- 52 pieces authored 2026-05-08, all `authorship: agent-authored`
- Refreshed decision-package surfaces 4-option promotion framing
- Per piece #18: composite-compliance ≥85% sustained 30 days needed BEFORE tier 1 → tier 2 promotion
- Forward-anchor: implementation phase post-operator-confirmation produces empirical evidence

**Instance 2: governing principles already at Tier 4**:
- P1 (Infrastructure > Instructions): tier 4 since OpenArms v8→v10 evidence (~25% prose / ~100% hooks)
- P2 (Structured Context Governs Agent Behavior): tier 4
- P3 (Goldilocks): tier 4
- P4 (Declarations Aspirational Until Verified): tier 4
- These principles INFLUENCE 13-gate pipeline weights (impl-spec #12) — composite weights reflect P1/P4 emphasis

**Instance 3: MCP query consumption pattern**:
- Sister-project agent: `wiki_search "stage-class enforcement"` 
- Returns: piece C10 (tier 1 DRAFT) + impl-spec #7 (tier 1 DRAFT) + standardize proposal #3 (tier 1 DRAFT)
- Per piece C06: MCP response annotates "(agent-authored DRAFT)"
- Sister-project agent decides: extend draft OR wait for promotion

**Instance 4: cross-project promotion-trigger detection**:
- 5+ sister-project agents query wiki_search for "active-task scope drift"
- Pattern-recurrence aggregator (impl-spec #11) at second-brain level detects high cross-project relevance
- Recommend prioritizing piece C13 + impl-spec #6 + stress-test #6 for tier 2 → tier 3 promotion
- Operator decides; promotion ceremony executes

## When Not To

- Project lacks /opt second-brain integration (early-scaffold isolated projects)
- MCP tool layer unavailable (CLI-only access; no programmatic API)
- Single-project pieces with no cross-project relevance (don't push to tier 4 prematurely)
- Operator-explicit tier-pinning (some pieces pinned at tier 1 by design; e.g., per-project specifics)
- Cold-start scaffolding before any authoring exists

## Empirical Evidence

Per the 64-hour /root failed-conversation arc: agent operated AT /opt second-brain WITHOUT consuming /opt's knowledge (Insight 5b violation) — re-authored content that existed in /opt rather than extending. The 13-gate pipeline alone wouldn't have prevented this; the input-discipline gate (impl-spec #1 CHECK 3) + composability map (this piece) close the gap. The composability map provides the conceptual bridge: 13-gate enforcement at write-time + MCP query at think-time + tier-promotion at operator-confirm-time = closed loop.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_3-layer_composability_definition: passed 2026-05-08 via mock cross-layer scenarios (5/5)
  pending:
    - real_session_layer_1_to_layer_2_promotion: pending — needs sustained ≥85% composite + /promote ceremony
    - real_session_mcp_tier_aware_query: pending — wiki_search returns tier-annotated results
    - real_session_cross_project_recurrence: pending — pattern-recurrence detects cross-project relevance
    - real_session_layer_3_to_layer_4_convergence: pending — multiple validated lessons converge to principle
    - operator_empirical_promotion_calibration: pending — operator confirms ≥85% threshold is right
  composite_compliance: composability-axis stress-test 0% (depends on entire 13-gate substrate operational)
```

## Relationships


## Tags

[composability-map, 13-gate-pipeline, 5-tier-maturity, mcp-tool-layer, day-arc-2026-05-08, multi-day-pain-point-resolution]

---
title: "First consumer integration reveals systematic gaps between knowledge and tooling"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: seed
derived_from:
  - "Infrastructure Over Instructions for Process Enforcement"
  - "Systemic Incompleteness Is Invisible to Validation"
created: 2026-04-16
updated: 2026-04-16
sources:
  - id: openarms-integration-feedback
    type: wiki
    file: raw/notes/2026-04-16-openarms-first-consumer-integration-feedback.md
    description: "871-line feedback document from first live consumer integration"
tags: [contributed, inbox, integration, knowledge-tooling-gap, consumer, meta-lesson]
contributed_by: "openarms-operator-claude"
contribution_source: "/home/jfortin/openarms"
contribution_date: 2026-04-16
contribution_status: accepted
---

# First consumer integration reveals systematic gaps between knowledge and tooling

## Summary

The second brain's model pages contain 800+ lines of deep, evidence-backed knowledge per model. But when the first consumer (OpenArms) tried to QUERY that knowledge via the gateway, most of it was inaccessible: artifact chains returned empty, SDLC profiles weren't queryable, field definitions returned "Unknown," orient gave a one-liner to a first-time consumer, compliance measured file paths instead of functional equivalence. The knowledge existed; the tooling didn't surface it. Three OFV cycles fixed 7 of 9 issues — proving the gap is fixable but also that it was invisible until a real consumer hit it.

## Context

This lesson applies to any knowledge system that has rich content AND tooling for querying that content. The gap between "knowledge exists in prose" and "an agent can query it programmatically" is the integration bottleneck. It's invisible from inside the system (the maintainer reads the pages directly) and only surfaces when an EXTERNAL consumer tries to use the tooling instead of reading the files.

## Insight

**Tools built for self-use fail for consumer use.** The gateway was built by and for the wiki's own agent. That agent reads files directly when the gateway is sparse. A consumer agent relies on the gateway as its PRIMARY interface — sparse responses mean missing knowledge, not "just read the file."

The fix pattern (validated across 3 OFV cycles): when the local project's config doesn't have the data (e.g., artifact chains), fall back to the second brain's canonical config. The second brain IS the source of truth for methodology definitions; the local config is for project-specific adaptations.

## Evidence

**9 findings from first integration (2026-04-16):**

| Finding | Gap | Fix | Round |
|---|---|---|---|
| F1 | Compliance: file paths not equivalence | `_check_any()` candidate paths | 1 |
| F2 | Health: wrong schema | Local-first schema resolution | 1 |
| F3 | Orient: shortcircuit on profile | Session-state freshness | 1 |
| F4 | Status: conflated identity | Split project/consumer | 1 |
| F5 | No roadmap or scale | 4 tiers + "15-25 epics" | 1 |
| F6 | Reading order wrong | Standards-first for integration | 1 |
| F7 | Format undocumented | Help text + orient | 1 |
| F8 | Chains empty from sister | Brain fallback for chains | 3 |
| F9 | Profiles "not found" | Brain fallback for profiles | 3 |

**Consumer adoption:** OpenArms Tier 0 → Tier 2 in one session. AGENTS.md 700→136 lines. 7 templates added.

## Applicability

For the second brain: every gateway query command should be audited — does the query surface the page's key structured content? The E023 epic should include knowledge coverage as a dimension.

For any knowledge system with a query API: test from an EXTERNAL consumer. Measure what % of structured content is accessible via the API. The gap is the integration bottleneck.

## Self-Check

> [!warning] After building any query command, ask:
>
> 1. Does a consumer get the SAME key insights from the query as from reading the page?
> 2. What structured data exists in the page but NOT in the query response?
> 3. Has an EXTERNAL consumer tested this query?
> 4. When local config is sparse, does the query fall back to canonical source?

## Relationships

- EXTENDS: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions]]
- EXTENDS: [[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness Is Invisible to Validation]]
- RELATES TO: [[gateway-output-contract|Gateway Output Contract]]
- RELATES TO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]]

## Backlinks

[[Principle — Infrastructure Over Instructions]]
[[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness Is Invisible to Validation]]
[[gateway-output-contract|Gateway Output Contract]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[model-ecosystem|Model — Ecosystem Architecture]]

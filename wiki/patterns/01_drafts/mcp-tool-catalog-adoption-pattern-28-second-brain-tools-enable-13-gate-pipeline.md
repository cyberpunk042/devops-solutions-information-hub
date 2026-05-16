---
title: "MCP Tool Catalog Adoption Pattern — 28 Second-Brain Tools Enable 13-Gate Pipeline"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: composability-map
    type: wiki
    file: wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md
    description: "Sibling — composability map's Layer 3 (MCP tool layer); this piece details the 28-tool catalog adoption per-tool"
  - id: input-discipline-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/input-discipline-gate-implementation-spec-pre-action-context-load-verification.md
    description: "Source — input-discipline gate CHECK 3 invokes MCP gateway query; this catalog identifies which tools"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — pipeline gates invoke MCP for cross-project knowledge consumption"
  - id: sister-project-propagation
    type: wiki
    file: wiki/patterns/01_drafts/sister-project-propagation-pattern-from-second-brain-to-5-project-ecosystem.md
    description: "Sibling — propagation Channel #1 (gateway contribute) is enabled by MCP tools detailed here"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — promotion-mechanism activated via MCP tools (wiki_post + wiki_distill)"
tags: [mcp-adoption, tool-catalog, 28-tools, 13-gate-pipeline, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# MCP Tool Catalog Adoption Pattern — 28 Second-Brain Tools Enable 13-Gate Pipeline

## Summary

The the second-brain second-brain exposes 28 MCP tools (per `tools/mcp_server.py`); these tools are the programmatic substrate enabling the 13-gate pipeline's cross-project capabilities (knowledge-reuse per Insight 5b, propagation channel #1 gateway contribute, tier-promotion ceremony). This piece maps each MCP tool to its role in the 13-gate pipeline + 5-tier lifecycle. Per substitution-pattern Insight 5b: documenting MCP tools alone is partial — must be paired with concrete adoption-points + invocation discipline. This piece closes the MCP-adoption gap.

## Pattern Description

### The 28 MCP tools (per the second-brain tools/mcp_server.py)

Per `.claude/rules/routing.md` row catalog (verification: count from @server.tool() decorators):

#### Gateway tools (9)
- `wiki_gateway_query` — query methodology, stages, models, fields, chains
- `wiki_gateway_orient` — context-aware orientation
- `wiki_gateway_flow` — Goldilocks step-by-step routing
- `wiki_gateway_health` — composite methodology+quality health score
- `wiki_gateway_compliance` — super-model adoption tier + gaps
- `wiki_gateway_template` — get a page template
- `wiki_gateway_timeline` — cross-project temporal view
- `wiki_gateway_contribute` — contribute lesson back to second-brain
- `wiki_gateway_docs` — root-level docs lookup

#### Ingestion tools (4)
- `wiki_fetch` — fetch a URL into raw/
- `wiki_fetch_topic` — search-and-fetch by topic
- `wiki_post` — run post-ingestion 6-step chain
- `wiki_crossref` — find new connections across pages

#### Knowledge tools (7)
- `wiki_search` — full-text search
- `wiki_read_page` — read specific page
- `wiki_list_pages` — enumerate by domain/type
- `wiki_backlog` — backlog status
- `wiki_gaps` — gap analysis with recommendations
- `wiki_log` — add log entry
- `wiki_checkin` — mission state-and-options checkin

#### Maintenance tools (6)
- `wiki_distill` — knowledge-distillation pipeline
- `wiki_scan_project` — scan sister-project for ingestible content
- `wiki_sister_project` — sister-project ops
- `wiki_mirror_to_notebooklm` — NotebookLM source sync
- `wiki_integrations` — integrations management
- `wiki_sync` — Obsidian sync ops

#### Status / meta tools (2)
- `wiki_status` — wiki stats
- `wiki_methodology_guide` — methodology guidance

### MCP tool → 13-gate pipeline adoption mapping

| MCP tool | 13-gate adoption-point | Scenario |
|---|---|---|
| `wiki_search` | Input-discipline gate (impl-spec #1) CHECK 3 | Agent queries before authoring lesson at the second-brain; surfaces existing related pieces |
| `wiki_read_page` | Input-discipline gate CHECK 3 | Agent reads identified related piece to understand what exists |
| `wiki_gateway_query` | Stage-class gate (impl-spec #7) SOURCE 3 | Hook reads methodology engine via gateway (vs reading yaml directly) |
| `wiki_post` | Authorship gate (impl-spec #8) | Post-write validation of new agent-authored piece |
| `wiki_crossref` | Pattern-recurrence (impl-spec #11) | Cross-cycle aggregator finds new connections across cycles |
| `wiki_gateway_contribute` | Sister-project propagation Channel #1 | Sister-project agent contributes lesson up to second-brain |
| `wiki_log` | Operator-directive registration (M-E001-1 type 8) | Sacrosanct verbatim quotes registered during cycle |
| `wiki_gateway_compliance` | Composite-compliance metric (impl-spec #12) | Cross-project compliance dashboard query |
| `wiki_gateway_health` | Composite-compliance dashboard | System-level health composed with per-axis metrics |
| `wiki_gateway_orient` | Post-compact orientation gate (impl-spec #10) | PostCompact /orient invocation reads orientation report |
| `wiki_gateway_template` | Authorship gate promotion ceremony | Template fetch when authoring new piece type |
| `wiki_gaps` | Pattern-recurrence cross-cycle aggregator | Gap analysis as input to improvement-candidate detection |
| `wiki_distill` | Tier 1 → tier 2 promotion ceremony | Knowledge-distillation pipeline candidate-scoring |
| `wiki_status` | Composite-compliance metric trend | Wiki stats feed into 30-day rolling aggregator |
| `wiki_backlog` | Drift-detection gate (impl-spec #6) SOURCE 2 | Active-task scope read from backlog frontmatter |
| `wiki_checkin` | Cycle context grounding | Mission state checkin before strategic edits |
| `wiki_gateway_flow` | Goldilocks step-by-step | Sister-project's identity-profile guided through 13-gate adoption |
| `wiki_gateway_timeline` | Cross-cycle pattern-recurrence | Cross-project temporal view of recurring patterns |
| `wiki_methodology_guide` | Stage-class gate methodology consultation | When axis taxonomy-gap suggests methodology engine inquiry |
| `wiki_list_pages` | Per-axis cross-reference validation matrix | Enumerate pieces per domain/type for orphan-detection |
| `wiki_fetch` | Tier 0 ingestion (raw notes) | Operator's pivotal directives ingested as raw |
| `wiki_fetch_topic` | Pattern-recurrence cross-cycle | Auto-fetch new content matching recurring pattern |
| `wiki_scan_project` | Sister-project propagation Channel #1 init | Sister-project scanned for ingestible content |
| `wiki_sister_project` | Sister-project propagation Channel #2 init | Sister-project ops + identity-profile substitution |
| `wiki_mirror_to_notebooklm` | (out-of-scope of 13-gate; auxiliary) | NotebookLM external mirror |
| `wiki_integrations` | (out-of-scope of 13-gate; auxiliary) | Cross-system integration management |
| `wiki_sync` | (out-of-scope of 13-gate; auxiliary) | Obsidian sync |
| `wiki_gateway_docs` | (auxiliary) | Root-level docs (CLAUDE.md / AGENTS.md) lookup |

**24 of 28 tools** map directly to 13-gate adoption-points; 4 tools are auxiliary (mirror / integrations / sync / docs).

### Adoption-discipline rules

**Rule 1**: ToolSearch deferred-load before invocation
- MCP tools are deferred-loaded per session via ToolSearch
- Loading via `select:wiki_search,wiki_read_page,...` brings tool schemas into context
- Bulk-load all 28 tools? NO — per piece compound-and-waterfall.md context-economy: load on-demand per topic

**Rule 2**: Invocation parameter discipline
- Every MCP invocation must pass valid parameters per JSONSchema
- Errors emit specific guidance: "param X is required; type Y; example Z"
- Invocation logs to ~/.claude/hooks/mcp-invocations.log (audit trail)

**Rule 3**: Cross-project query discipline
- `wiki_search` cross-project: returns annotation per piece's tier (DRAFT vs canonical)
- Per piece C06 (authorship): downstream consumers must respect annotation
- DO NOT aggregate tier 1 + tier 2 + tier 4 results indistinguishably

**Rule 4**: Mutation-tool discipline (write-tools)
- `wiki_post`, `wiki_crossref`, `wiki_log`, `wiki_gateway_contribute`, `wiki_distill` are MUTATION tools
- Each requires operator-confirmation OR is operator-territory action
- Per impl-spec #2 (decision-territory): mutations to the second-brain are operator-territory by default

**Rule 5**: Read-tool discipline (read-tools)
- `wiki_search`, `wiki_read_page`, `wiki_list_pages`, `wiki_status`, `wiki_gaps`, `wiki_methodology_guide`, `wiki_gateway_*` (queries) are READ tools
- Free to invoke without operator-confirmation (read-only operations)
- Subject to input-discipline gate (impl-spec #1): query results inform context-load decisions

### Adoption phases (when to introduce which tools)

```
Phase A — Read-tools first (Week 1 of M1)
  - Adopt wiki_search + wiki_read_page + wiki_gateway_query
  - These power input-discipline gate CHECK 3 (Insight 5b knowledge-reuse)

Phase B — Status-tools (Week 1-2)
  - Adopt wiki_status + wiki_gaps + wiki_gateway_health
  - These feed composite-compliance baseline

Phase C — Authoring-tools (Week 2-3 of M1)
  - Adopt wiki_post + wiki_log + wiki_crossref
  - These activate authorship gate + log discipline

Phase D — Promotion-tools (Week 3-4 of M5-M6)
  - Adopt wiki_distill + wiki_gateway_compliance + wiki_gateway_template
  - These power tier-promotion ceremony

Phase E — Cross-project-tools (Week 5+ of M7)
  - Adopt wiki_gateway_contribute + wiki_sister_project + wiki_scan_project
  - These activate sister-project propagation Channel #1
```

### Anti-patterns at MCP adoption layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Use WebFetch for the second-brain URLs instead of MCP tools | Bypasses provenance + ratio gate; pre-webfetch hook blocks anyway | Routing rule #1 + pre-webfetch hook |
| Bulk-load all 28 MCP tools at session start | Context bloat; cache miss; cost spike | On-demand ToolSearch deferred-load |
| Treat tier 1 DRAFT search results as canonical | Per piece C06; promotion ceremony hasn't happened | Tier-aware MCP responses (per composability map) |
| Mutate the second-brain via wiki_post without operator-confirmation | Per impl-spec #2 decision-territory: the second-brain mutations are operator-territory | Mutation-tool discipline (Rule 4) |
| Re-author content existing in the second-brain despite wiki_search returning it | Insight 5b violation | Input-discipline gate CHECK 3 |

## When To Apply

Apply this MCP adoption pattern when:
- the second-brain second-brain is reachable as MCP server
- Sister-project has MCP client capability (Claude Code, opencode, etc.)
- 13-gate pipeline implementation underway (per implementation-roadmap M1+)
- Cross-project knowledge-reuse is operational goal
- Pain-point cluster overlap with second-brain content (Insight 5b activation)

## Instances

**Instance 1: input-discipline gate (impl-spec #1) CHECK 3 invokes wiki_search**:
- Agent intends to author lesson at `$HOME/devops-solutions-information-hub/wiki/lessons/01_drafts/<topic>.md`
- PreToolUse on Write fires input-discipline gate
- CHECK 3: invoke `wiki_search "<topic>"` → returns 3 related existing pieces
- Banner emits: "FAILED: opt-pieces — 3 related pieces not consulted. CHECK: <results>."
- Agent reads related pieces (wiki_read_page) → state-file mutates → re-runs gate → passes

**Instance 2: composite-compliance dashboard via wiki_gateway_compliance**:
- /compliance-report slash command invokes
- Composite-compliance metric (impl-spec #12) reads cycle-history
- ALSO invokes `wiki_gateway_compliance` for cross-project compliance state
- Returns combined report: per-project axes + cross-project sister-project gaps

**Instance 3: tier-promotion via wiki_distill**:
- M5-M6 milestone: tier 1 → tier 2 promotion ceremony
- Operator invokes /promote → impl-spec #8 promotion ceremony
- ALSO invokes `wiki_distill --score` → identifies promotion-candidates
- Operator confirms candidates passing operator-review checklist 7/7

**Instance 4: sister-project propagates lesson via wiki_gateway_contribute**:
- root-ghostproxy authored impl-spec #2 (decision-territory)
- After tier 2+ promotion: sister-project (e.g., OpenArms) wants the pattern
- Sister-project agent: `wiki_gateway_contribute --type pattern --title "..." --content "..."`
- Lands at $HOME/devops-solutions-information-hub/00_inbox/contribute/ → tier 0 → operator confirms → tier 1+

## When Not To

- the second-brain second-brain unreachable (sister-project isolated; pre-M007 connect)
- Sister-project lacks MCP client (alternative: CLI fallback per routing.md row catalog)
- Read-only research mode (read-tools allowed; mutation-tools deferred)
- Auxiliary tools (mirror / integrations / sync / docs) — out-of-scope for 13-gate pipeline
- Operator-explicit deferral (REASON= bypass on entire MCP integration)

## Empirical Evidence

Per the 64-hour /root failed-conversation arc: agent operated AT the second-brain second-brain WITHOUT consuming the second-brain's existing knowledge — Insight 5b violation. The MCP tool layer (28 tools) was always available but not adopted as substrate for input-discipline gate CHECK 3. The MCP adoption pattern (this piece) closes that gap by mapping each tool to specific 13-gate pipeline adoption-point — agent has structural access to the second-brain knowledge at every gate firing.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_28_tool_catalog_definition: passed 2026-05-08 via mock per-tool scenarios
  pending:
    - real_session_phase_a_read_tools: pending — needs Phase A adoption + verification
    - real_session_phase_b_status_tools: pending
    - real_session_phase_c_authoring_tools: pending
    - real_session_phase_d_promotion_tools: pending
    - real_session_phase_e_cross_project_tools: pending
    - composability_with_input_discipline_check_3: pending — paired wiki_search invocation
    - composability_with_authorship_gate_promotion: pending — paired wiki_distill invocation
    - mutation_tool_operator_confirmation_audit: pending
    - tier_aware_search_response: pending — wiki_search annotates per-tier
  composite_compliance: mcp-adoption-axis stress-test 0% (depends on phased adoption A-E)
```

## Relationships


## Tags

[mcp-adoption, tool-catalog, 28-tools, 13-gate-pipeline, day-arc-2026-05-08, multi-day-pain-point-resolution]

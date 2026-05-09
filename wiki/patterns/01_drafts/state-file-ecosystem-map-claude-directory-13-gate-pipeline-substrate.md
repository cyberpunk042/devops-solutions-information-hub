---
title: "State-File Ecosystem Map — ~/.claude/ Directory as 13-Gate Pipeline Substrate"
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
    description: "Integration pattern — state-file ecosystem IS the cross-hook communication contract"
  - id: composability-map
    type: wiki
    file: wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md
    description: "Sibling — composability across 3 layers; this piece details Layer 1 substrate"
  - id: input-discipline-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/input-discipline-gate-implementation-spec-pre-action-context-load-verification.md
    description: "Source — last-context-load.json owner; this map references all 12 impl-spec state-files"
  - id: post-compact-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-orientation-gate-implementation-spec-handoff-and-mirror-enforcement.md
    description: "Source — post-compact-pending-orient.flag owner; lifecycle-event state"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Source — composite-compliance-dashboard.json owner + cycle-history/composite-history aggregator"
tags: [state-file-ecosystem, 13-gate-pipeline, claude-directory, substrate, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# State-File Ecosystem Map — ~/.claude/ Directory as 13-Gate Pipeline Substrate

## Summary

The 13-gate pipeline's cross-hook communication is anchored by a state-file ecosystem at `~/.claude/`. Each state-file is owned by ONE implementation-spec but READ BY MULTIPLE hooks — this is the substrate enabling banner-stacking + per-axis state independence + cross-hook composability. Per substitution-pattern Insight 5b: documenting state-files alone is partial — must be paired with ownership-discipline + lifecycle-management. This piece closes the state-file-ecosystem gap.

## Pattern Description

### Complete state-file inventory (12 owned + 7 derived = 19 total)

#### State files OWNED by implementation-specs (one per axis)

| State file | Owner spec | Purpose | Lifecycle |
|---|---|---|---|
| `~/.claude/last-context-load.json` | impl-spec #1 input-discipline | Track per-cycle: recent-messages-loaded-at, mode-pieces-loaded[], opt-pieces-loaded[] | Refresh per cycle (UserPromptSubmit) |
| `~/.claude/active-task.json` | impl-spec #6 drift-detection | Track active-task: task_id, task_scope, drift_event_count, drift_events[] | Refresh on /task set or operator prose detection |
| `~/.claude/active-correction.json` | impl-spec #5 correction-shape | Track pending operator-correction: dimension, prior_position, direction_demanded, consecutive_corrections_count | Lifecycle: pending → resolved-one-notch → archived |
| `~/.claude/regression-baseline.json` | impl-spec #3 regression-test | Per-cycle baseline: total/passed/failed/runtime_seconds + post_edit_runs[] | Refresh per cycle (PreToolUse first edit) |
| `~/.claude/post-compact-pending-orient.flag` | impl-spec #10 post-compact | Single-line timestamp; presence = pending orient required | Set by PostCompact; cleared by /orient invocation |
| `~/.claude/last-cycle-anchors.json` | impl-spec #9 semantic-conflation | Demonstrative-pronoun referent lookup: recent_topics[], recent_targets[] | Append per cycle |
| `~/.claude/active-mode` | (mode-system; pre-existing) | Single-line current mode name | Set by /mode-* slash commands |
| `~/.claude/active-mission` | (objective layer; pre-existing) | Single-line mission text | Set by /mission slash command |
| `~/.claude/active-focus` | (objective layer; pre-existing) | Single-line focus text | Set by /focus slash command |
| `~/.claude/active-impediment` | (objective layer; pre-existing) | Single-line impediment text | Set by /impediment slash command |
| `~/.claude/active-priorities` | (priorities tier SB-127; pre-existing) | Multi-line priorities list | Set by /priorities slash commands |
| `~/.claude/composite-compliance-dashboard.json` | impl-spec #12 composite-compliance | Dashboard mirror: current_cycle, 30day, per_axis, improvement_candidates | Refresh per cycle (Stop hook) |

#### Derived state directories (lifecycle artifacts)

| Directory | Owner | Purpose | Cardinality |
|---|---|---|---|
| `~/.claude/cycle-history/<cycle_id>.json` | impl-spec #11 pattern-recurrence | Per-cycle aggregate: gate_metrics, recurrence_flags, composite_compliance_preview | One JSON per cycle |
| `~/.claude/correction-history/<correction_id>.json` | impl-spec #5 correction-shape | Resolved correction archive | One JSON per resolved correction |
| `~/.claude/drift-history/<cycle_id>.json` | impl-spec #6 drift-detection | Per-cycle drift events archive | One JSON per cycle with drift events |
| `~/.claude/composite-history.jsonl` | impl-spec #12 composite-compliance | Per-cycle composite percentage trend | Append per cycle (single file, JSONL) |
| `~/.claude/circuit-breaker-pending.flag` | impl-spec #11 pattern-recurrence | Pending circuit-breaker per dimension | Set on threshold trip; cleared on operator clarification |
| `~/.claude/composite-weights.json` | impl-spec #12 composite-compliance | Operator-revised composite weights | Set by /compliance-weights slash command |
| `~/.claude/composite-weight-revisions.log` | impl-spec #12 composite-compliance | Audit log of weight revisions | Append per revision |

#### Audit logs (write-only, append-mode)

| Log file | Owner | Format | Purpose |
|---|---|---|---|
| `~/.claude/hooks/severity-t1-block.log` | impl-spec #4 severity | JSONL | T1 attempts (blocked or bypassed) |
| `~/.claude/hooks/severity-t2-warn.log` | impl-spec #4 severity | JSONL | T2 warnings |
| `~/.claude/hooks/severity-t3-note.log` | impl-spec #4 severity | JSONL | T3 audit logs |
| `~/.claude/hooks/decision-territory-bypass.log` | impl-spec #2 decision-territory | JSONL | Operator-grant bypasses on operator-territory edits |
| `~/.claude/hooks/stage-class-violation.log` | impl-spec #7 stage-class | JSONL | Stage-class violations (blocked or bypassed) |
| `~/.claude/hooks/input-discipline-bypass.log` | impl-spec #1 input-discipline | JSONL | Input-discipline bypasses with REASON= citation |
| `~/.claude/hooks/authorship-autotag.log` | impl-spec #8 authorship | JSONL | Auto-tag events for new agent-authored files |
| `~/.claude/hooks/authorship-promotion.log` | impl-spec #8 authorship | JSONL | Promotion ceremony audit (agent-authored → operator-confirmed) |
| `~/.claude/hooks/post-compact-bypass.log` | impl-spec #10 post-compact | JSONL | Skip-orient bypasses post-compact |
| `~/.claude/hooks/regression-test-bypass.log` | impl-spec #3 regression-test | JSONL | Regression-test bypasses (e.g., refactor mode) |
| `~/.claude/hooks/mcp-invocations.log` | mcp-adoption pattern | JSONL | MCP tool invocation audit |

### Cross-hook read patterns (composability map)

For each state-file, document who READS it across hook events:

| State file | Owner spec | Read by |
|---|---|---|
| last-context-load.json | #1 | input-discipline (own) + composability-aware queries |
| active-task.json | #6 | drift-detection (own) + stage-class (#7 SOURCE 1) + post-compact orient |
| active-correction.json | #5 | correction-shape (own) + pattern-recurrence (#11 escalation trigger) |
| regression-baseline.json | #3 | regression-test (own) + composability with stage-class (implement-stage edits) |
| post-compact-pending-orient.flag | #10 | post-compact (own) + ALL PreToolUse hooks (first-action enforcement) |
| last-cycle-anchors.json | #9 | semantic-conflation Detector 3 (own) + composability with correction-shape |
| active-mode | mode-system | mode-enforcement banner (per-prompt) + drift-detection scope |
| active-mission/focus/impediment | objective layer | mode-enforcement banner + cycle stamp |
| active-priorities | priorities tier | mode-enforcement banner + cycle stamp |
| composite-compliance-dashboard.json | #12 | mode-enforcement banner (compound axis) + /compliance-report |
| circuit-breaker-pending.flag | #11 | ALL PreToolUse hooks (block on flag for matching dimension) |

### Cross-hook write patterns (lifecycle management)

| Hook event | Writes to state files |
|---|---|
| UserPromptSubmit | last-cycle-anchors.json (#9) + active-correction.json (#5 detection) + active-task.json (#6 if /task set) |
| PreToolUse (first edit per cycle) | regression-baseline.json (#3) + last-context-load.json (#1 if updating from Read) |
| PostToolUse (Read) | last-context-load.json (#1 mode_pieces_loaded array update) |
| PostToolUse (Write) | authorship-autotag.log (#8 if missing frontmatter) + cycle-history aggregator (#11) |
| PostToolUse (Edit) | regression-baseline.json (#3 post_edit_runs) + active-correction.json (#5 resolution) + drift-events (#6) |
| Stop | cycle-history/<cycle_id>.json (#11) + composite-history.jsonl (#12) + composite-compliance-dashboard.json (#12) + circuit-breaker-pending.flag (#11 if threshold tripped) |
| PreCompact | wiki/log/<ISO>-pre-compact-handoff.md (#10 if missing) |
| PostCompact | post-compact-pending-orient.flag (#10) |

### Ownership-discipline rules

**Rule 1**: Single-owner per state file
- Each state file has ONE owning impl-spec
- Other impl-specs READ but do not WRITE
- Prevents write-collision; ownership-clear

**Rule 2**: Lifecycle bounded
- Per-cycle state files (e.g., last-context-load.json, regression-baseline.json) refresh on cycle boundaries
- Persistent state files (e.g., active-mode, composite-history.jsonl) span sessions

**Rule 3**: Append-mode for audit logs
- All `~/.claude/hooks/*.log` files are JSONL append-mode
- Never rewritten; rotation via separate ops if needed

**Rule 4**: Atomic writes
- State-file writes use temp-file + rename pattern
- Prevents corruption from interrupted writes

**Rule 5**: Schema validation
- Each state file has implicit JSON schema per owning impl-spec
- Hook reads handle missing files gracefully (cold-start path)
- Hook reads fail-safe on schema violations (assume cold-start, log warning)

### State-file dependencies (read-write graph)

```
                  ┌─────────────────────┐
                  │ active-mode         │
                  └─────────┬───────────┘
                            │ read
                            ▼
        ┌───────────────────────────────────────┐
        │  mode-enforcement banner              │
        │  (compound axis)                      │
        │  reads: active-mode, mission, focus,  │
        │         impediment, priorities,       │
        │         composite-compliance-dashboard│
        └───────────────────────────────────────┘

  active-task.json ◄────┐
        ▲ owns          │ reads
        │ #6            │
        │               │
  drift-detection ─────┐│
        │              ▼▼
        │      ┌────────────────────┐
        │ stage-class (#7 SOURCE 1) │
        │      └────────────────────┘
        │
  active-correction.json
        ▲ owns #5
        │
        │ reads
        ▼
  pattern-recurrence (#11 escalation trigger)
        │
        │ writes
        ▼
  circuit-breaker-pending.flag ◄── (read by ALL PreToolUse hooks)

  cycle-history/<cycle_id>.json (per cycle)
        ▲ writes #11
        │
        │ reads
        ▼
  composite-history.jsonl (append per cycle)
        ▲ writes #12
        │
        │ reads
        ▼
  composite-compliance-dashboard.json
        ▲ writes #12
        │
        │ reads (per-prompt)
        ▼
  mode-enforcement banner (compound axis)
```

### Anti-patterns at state-file ecosystem layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Multi-owner (multiple impl-specs WRITE same state file) | Write collisions; ambiguous lifecycle | Rule 1 single-owner |
| State file overflows (e.g., last-cycle-anchors.json grows unbounded) | Performance + parser failures | Cycle-boundary refresh + cap on array sizes |
| Hook reads stale state across cycle boundary | Stale data; logic errors | Cycle_id field; rotation per cycle |
| Audit logs grow without rotation | Disk pressure | Out-of-scope; periodic rotate via separate ops |
| Hook fails on missing state file | Hard error in cold-start path | Rule 5 fail-safe + cold-start defaults |
| State-file path conflicts across projects | Sister-project state collisions | Per-project state dir (alternative: namespace via cycle_id prefix) |

## When To Apply

Apply this state-file ecosystem map when:
- 13-gate pipeline implementation underway (per implementation-roadmap M2)
- Hook scripts require cross-hook state communication
- Operator + agent + sister-projects expect deterministic state-file conventions
- Pain-point cluster overlap with state-management gaps
- Composite-compliance metric needs persistent across cycles

## Instances

**Instance 1: cycle-end Stop hook reads 9 audit logs**:
- pattern-recurrence aggregator (impl-spec #11) at Stop hook
- Reads ALL 9 PreToolUse audit logs (severity-t1-block.log + severity-t2-warn.log + decision-territory-bypass.log + stage-class-violation.log + input-discipline-bypass.log + authorship-autotag.log + authorship-promotion.log + active-task.json drift_events + active-correction.json)
- Aggregates → cycle-history/<cycle_id>.json
- Composite-compliance metric (impl-spec #12) reads cycle-history → composite-history.jsonl

**Instance 2: cross-hook composability — drift-detection reads active-task**:
- impl-spec #6 active-task.json owner
- impl-spec #7 stage-class reads active-task.json SOURCE 1 for current_stage
- Both gates compose without interference (read-only access from #7 to #6's owned state)

**Instance 3: PostCompact triggers cascade state-refresh**:
- post-compact-pending-orient.flag set by impl-spec #10
- ALL subsequent PreToolUse hooks read this flag (Rule 4 cross-hook read pattern)
- /orient invocation clears flag + triggers input-discipline state-file refresh (impl-spec #1)
- Subsequent edits silent (state-files all fresh)

**Instance 4: circuit-breaker auto-escalation cascade**:
- impl-spec #11 detects consecutive_corrections_count ≥ 3
- Writes circuit-breaker-pending.flag
- ALL subsequent PreToolUse hooks read this flag
- BLOCK on dimension matching the correction
- Operator-clarification clears flag

## When Not To

- Project lacks `~/.claude/` directory convention (rare; Claude Code provides)
- Cold-start scaffolding before any state-files exist
- Read-only research mode (no state-file writes)
- Sister-project state-file conventions differ (alternative state-dir patterns)
- Operator-explicit state-isolation (per-session ephemeral state)

## Empirical Evidence

The 12 impl-specs reference 12 distinct state-file ownership claims; the 11 audit logs document complete write-trace. Without this map, ownership is implicit (each impl-spec mentions its state file individually); with this map, ownership + cross-read patterns + lifecycle are explicit. Per piece #18: state-file ecosystem becomes operationally testable per implementation-roadmap M2.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_19_state_file_definition: passed 2026-05-08 via mock state-file scenarios
    - synthetic_5_ownership_rules_validation: passed 2026-05-08 via mock scenario set
  pending:
    - real_session_per_owner_state_lifecycle: pending — needs M2 implementation phase
    - real_session_cross_hook_read_patterns: pending — verifies non-collision
    - real_session_atomic_write_pattern: pending — verifies temp-file+rename works
    - real_session_cold_start_resilience: pending — missing files don't break hooks
    - real_session_audit_log_jsonl_format: pending — log consumers parse correctly
  composite_compliance: state-file-axis stress-test 0% (depends on M2 implementation)
```

## Relationships


## Tags

[state-file-ecosystem, 13-gate-pipeline, claude-directory, substrate, day-arc-2026-05-08, multi-day-pain-point-resolution]

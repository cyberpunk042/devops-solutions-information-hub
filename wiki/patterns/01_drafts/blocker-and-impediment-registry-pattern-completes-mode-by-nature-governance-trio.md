---
title: "Blocker & Impediment Registry Pattern — Completes Mode-By-Nature Governance Trio"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: operator-directive-2026-05-08-mode-by-nature
    type: file
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "PRIMARY operator directive (sacrosanct 2026-05-08): 'creating blockers, impediment, questions, for anyone too' — blocker + impediment + question trio"
  - id: question-registry-pattern
    type: wiki
    file: wiki/patterns/01_drafts/question-registry-discipline-bidirectional-question-answering-with-audience-taxonomy.md
    description: "PRIMARY parent (Fire 99) — question-registry; this pattern is parallel for blockers + impediments completing the trio"
  - id: mode-by-nature-pattern
    type: wiki
    file: wiki/patterns/01_drafts/mode-by-nature-active-governance-pm-architect-dual-expert-generates-blockers-impediments-questions.md
    description: "PRIMARY parent (Fire 98) — mode-by-nature surfaces blockers + impediments by nature; this pattern operationalizes their registry"
  - id: 100-piece-milestone-closing-arc-summary
    type: wiki
    file: wiki/log/2026-05-08-100-piece-milestone-closing-arc-summary-pre-compact-preservation.md
    description: "Sibling — 100-piece milestone (Fire 100); pre-compact preservation context; this fire continues per /loop"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — blockers + impediments surfaced but not registered IS substitution at governance layer"
tags: [blocker-registry, impediment-registry, governance-trio, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Blocker & Impediment Registry Pattern — Completes Mode-By-Nature Governance Trio

## Summary

Per operator directive 2026-05-08 (sacrosanct verbatim): "creating blockers, impediment, questions, for anyone too". Per Fire 99 question-registry: question-half of trio operationalized. This pattern operationalizes the OTHER TWO members: blockers + impediments. Per Fire 98 mode-by-nature: PM-mode by nature surfaces all three. Per /root work-mode.md PO approval boundary: blockers vs impediments are distinct concepts. Per operator's "not yet" deferral: this piece DOCUMENTS the registry; actual blocker/impediment-creation deferred to operator-confirmation + M1+ implementation. Per substitution-pattern Insight 5b: blockers/impediments surfaced but not registered IS substitution at governance layer.

## Pattern Description

### Blocker vs impediment vs question — distinction matrix

```
BLOCKER (operator-pending decision required):
  Definition: work cannot proceed until operator decides X
  Example: "T011 Foundation IaC approach (greenfield vs extend)" — operator-territory choice
  Resolution: operator-empirical decision; logged in decisions logbook
  State-file: ~/.claude/blockers/<id>.json
  Storage convention: distinct from questions (questions can be agent-resolvable)
  
IMPEDIMENT (focus-blocker; operator-empirical):
  Definition: operator's CURRENT FOCUS is blocked by X (could be agent's progress OR operator's circumstance)
  Example: "operator on call; can't review until tomorrow" OR "agent context budget low; review pending"
  Resolution: time-passing OR operator-action OR agent-action depending on impediment-source
  State-file: ~/.claude/active-impediment (single-line per /root convention)
  Storage convention: per-active impediment ONE; multiple impediments queue

QUESTION (clarification needed):
  Definition: clarification of meaning or intent (per Fire 99)
  Example: "should we promote feature-flag pattern to tier-2 first?"
  Resolution: bidirectional Q&A per Fire 99
  State-file: ~/.claude/active-questions/<audience>/<id>.json
  Storage convention: per Fire 99 4-audience taxonomy
```

The three are DISTINCT but RELATED:
- A QUESTION can become a BLOCKER (when operator-empirical answer needed AND work blocks until answer)
- An IMPEDIMENT can spawn a BLOCKER (when impediment requires operator-decision to clear)
- A BLOCKER can spawn a QUESTION (when blocker needs clarification before decision)

### Blocker-registry structure

```
~/.claude/blockers/
├── pending/<blocker-uuid>.json    # operator-decision required
├── deferred/<blocker-uuid>.json   # operator-acknowledged but deferred
└── resolved/<blocker-uuid>.json   # operator-decided (archive)

Each blocker JSON:
{
  "blocker_id": "<uuid>",
  "surfaced_by": "agent|operator|sister-project",
  "surfaced_at": "<ISO>",
  "blocker_text": "<verbatim>",
  "blocker_kind": "decision|approval|dependency|external",
  "context": "<what work is blocked>",
  "active_mode_when_surfaced": "pm-scrum-master|devops-architect|dual-expert|<none>",
  "related_pieces": ["<path>", ...],
  "decision_options": ["<R>", "<K>", "<D>"],  // R=resolve, K=keep, D=defer per the second-brain /blockers slash command convention
  "priority": "high|medium|low",
  "status": "pending|deferred|resolved",
  "resolution": "<if resolved>",
  "resolved_at": "<ISO if resolved>",
  "resolved_by": "operator|agent (with grant)|external"
}
```

### Impediment-registry structure (single-active simpler)

Per /root active-impediment convention (single-line state-file):

```
~/.claude/active-impediment
  Single-line text describing current impediment
  Empty/missing = no current impediment
  
~/.claude/impediments-history/<timestamp>.json
  Archive when impediment cleared
  
Each impediment JSON (when archived):
{
  "impediment_id": "<uuid>",
  "surfaced_at": "<ISO>",
  "cleared_at": "<ISO>",
  "impediment_text": "<verbatim>",
  "impediment_kind": "operator-circumstance|agent-state|external|technical",
  "duration_seconds": <int>,
  "cleared_how": "operator-action|agent-action|time-passing|external-resolution"
}
```

Impediments queue if multiple emerge: most-pressing surfaced via `~/.claude/active-impediment`; others in `pending-impediments/<id>.json` for FIFO.

### Audience taxonomy (per Fire 99 generalization)

For BLOCKERS:
- AUDIENCE 1 OPERATOR: operator-pending-decision blockers (most-common; per the second-brain /blockers slash command)
- AUDIENCE 2 AGENT: agent-needed-decision blockers (rare; agent self-resolves with operator-grant)
- AUDIENCE 3 SISTER-PROJECT: cross-project blockers (route via gateway-contribute)
- AUDIENCE 4 FUTURE-AGENTS: handoff-blockers (preserve to handoff-doc)

For IMPEDIMENTS:
- AUDIENCE 1 SELF (operator/agent on the receiving end)
- AUDIENCE 2 OBSERVERS (sister-projects observing impediment-pattern across cycles)

### Bidirectional flow per audience (BLOCKERS)

```
AUDIENCE 1 OPERATOR (most-common):
  Agent surfaces blocker → state-file pending/<id>.json
  Cycle stamp: emits "BLOCKER-PENDING: <id> — <text> (R/K/D options)"
  Operator decides → state-file moves: pending/ → resolved/
  Decision-logbook entry per impl-spec #8 promotion-ceremony

AUDIENCE 2 AGENT (with grant):
  Operator: "agent, you can decide X with grant"
  → state-file: pending/ with grant-citation in resolution_options
  Agent decides + cites grant + logs to audit
  → state-file moves to resolved/

AUDIENCE 3 SISTER-PROJECT:
  Cross-project blocker (e.g., shared infrastructure decision)
  → routes via wiki_gateway_contribute MCP
  → the second-brain agent processes; operator confirms cross-project scope

AUDIENCE 4 FUTURE-AGENT:
  Pre-compact handoff: blocker preserved
  → handoff-doc + state-file
  → future agent re-surfaces OR resolves
```

### Slash-command surface (forward-anchored, parallels Fire 99)

```
/blockers add <text> [--kind decision|approval|dependency|external] [--priority high|medium|low]
  - Adds blocker to pending/

/blockers show [--audience X] [--status pending|deferred|resolved]
  - Lists blockers per filter

/blockers resolve <id> --decision <option> [--rationale "<text>"]
  - Resolves blocker; moves to resolved/; appends to decision-logbook

/blockers defer <id>
  - Status → deferred; remains pending; not actively-required this cycle

/impediment set <text>
  - Sets ~/.claude/active-impediment

/impediment clear [--how operator-action|agent-action|time-passing]
  - Archives current impediment to impediments-history/

/impediment show
  - Display current impediment

/impediment queue add <text>
  - Adds to pending-impediments/ FIFO queue
```

### Per-cycle scan (mode-by-nature integration)

When PM mode active (per Fire 98), per-cycle output includes:

```
Mode-by-nature governance scan (extended from Fire 98):
  Blockers:
    Surfaced this cycle: [<id>] "<text>" (R/K/D options)
    Resolved this cycle: [<id>] → "<decision>"
    Deferred: [<id>] (not active this cycle)
  Impediments:
    Active: ~/.claude/active-impediment value (or "none")
    Cleared this cycle: <impediment-text> via <how>
    Queued: [<id>] (waiting for active-clear)
  Questions: (per Fire 99)
    [...]
```

### Composability with body

| Existing piece | Composability with blocker/impediment registry |
|---|---|
| /root tools.blockers + /blockers slash | impl-spec; this pattern operationalizes registry-discipline |
| /root active-impediment state-file | this pattern adopts the convention + queue extension |
| Mode-by-nature pattern (Fire 98) | mode-by-nature surfaces blockers + impediments; this pattern stores them |
| Question-registry (Fire 99) | parallels structure; bidirectional flow; audience taxonomy |
| Backlog-decomposition (Fire 97) | Epic + Module + Task hierarchy can include per-task BLOCKED-BY field referring to blockers/<id> |
| Decisions logbook (per /root tools.decisions) | blocker resolution → decision-logbook entry |

### Anti-patterns at blocker/impediment registry layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Blocker surfaced but not registered | Lost when context-compaction; recurring blockers | State-file persistence |
| Impediment unrecognized; agent operates as if no impediment | Operator-empirical wrong-state assumption | Active-impediment state-file convention |
| Blocker resolved but not logged to decisions | Loss of decision-rationale | Decision-logbook integration |
| Question→blocker→decision flow not connected | Triple-entries with no linkage | Cross-reference fields in JSON |
| Multiple impediments without queue | Operator-empirical confusion which active | Pending-impediments/ FIFO queue |

## When To Apply

Apply this blocker/impediment registry when:
- Mode-by-nature pattern (Fire 98) operational
- Question-registry (Fire 99) operational (parallel structure)
- /root tools.blockers + /blockers slash + active-impediment infrastructure exists
- Operator-empirical wants registry discipline beyond per-cycle ephemerality
- Cross-cycle persistence matters (especially pre-compact)

## Instances

**Instance 1: PM-mode active; agent surfaces operator-pending blocker**:
- Cycle output: "BLOCKER-PENDING: T015-decision (greenfield-vs-extend); R/K/D options provided"
- Storage: ~/.claude/blockers/pending/<uuid>.json
- Operator decides next cycle: "extend" + rationale
- Storage moves to resolved/
- Decision-logbook entry per impl-spec #8

**Instance 2: Operator-circumstance impediment**:
- Operator types: "I'm on call; can't review until tomorrow"
- Agent: /impediment set "operator-on-call until tomorrow"
- ~/.claude/active-impediment populated
- Cycle stamp: surfaces impediment
- Tomorrow: operator types "back; ready to review"
- Agent: /impediment clear --how operator-action
- Archive in impediments-history/

**Instance 3: Cross-project blocker**:
- Agent: "shared schema decision needed across root-ghostproxy + AICP"
- Storage: blockers/sister-pending/<id>.json
- MCP gateway-contribute lands at the second-brain 00_inbox/contribute
- AICP operator + root operator joint-decide
- Cross-cited resolution in both projects' decision-logbooks

**Instance 4: Pre-compact handoff blocker preservation**:
- Pre-compact event approaching
- Active blockers → handoff-doc blocker section + ~/.claude/blockers/handoff/<id>.json
- Post-compact agent reads handoff + resumes blocker-pending state

## When Not To

- Single-stakeholder cold-start (no audience-multiplicity)
- Operator-explicit "no governance registry" preference
- Compaction in progress
- Impl-phase impl-tasks (focused work; defer registry-management)

## Empirical Evidence

Per /root work-mode.md PO approval boundary + decisions logbook (40 entries D001-D040): existing /root has blocker + decision tracking. the second-brain similarly has /blockers slash command + tracker. This pattern unifies the convention + adds impediment queue + sister-project + future-agent audience taxonomy.

Without registry, blockers + impediments surfaced in cycle prose but lost cross-compaction. With registry: persistent + bidirectional + audience-routed.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_blocker_state_file_schema: passed 2026-05-08 via mock JSON scenarios
    - synthetic_impediment_queue_FIFO: passed 2026-05-08 via mock multiple-impediment scenarios
  pending:
    - real_session_blocker_lifecycle: pending — depends on /blockers slash command implementation
    - real_session_impediment_lifecycle: pending — depends on /impediment slash command
    - real_session_cross_project_blocker_routing: pending
    - real_session_handoff_preservation: pending
    - operator_empirical_blocker_kind_taxonomy: pending — operator confirms 4-kind classification
  composite_compliance: blocker-impediment-axis stress-test 0% (forward-anchored; M1+ implementation)
```

## Relationships


## Tags

[blocker-registry, impediment-registry, governance-trio, day-arc-2026-05-08, multi-day-pain-point-resolution]

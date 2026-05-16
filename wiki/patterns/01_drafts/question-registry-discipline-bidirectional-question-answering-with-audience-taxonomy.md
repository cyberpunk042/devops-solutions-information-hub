---
title: "Question-Registry Discipline — Bidirectional Question-Answering with Audience Taxonomy"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: operator-directive-2026-05-08-mode-by-nature-inception
    type: file
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "PRIMARY operator directive (sacrosanct 2026-05-08): 'creating blockers, impediment, questions, for anyone too.. registering and answering questions and writing and updating to docs, not yet'"
  - id: mode-by-nature-pattern
    type: wiki
    file: wiki/patterns/01_drafts/mode-by-nature-active-governance-pm-architect-dual-expert-generates-blockers-impediments-questions.md
    description: "PRIMARY parent (Fire 98) — mode-by-nature surfaces questions; this pattern operationalizes question-registry"
  - id: operator-empirical-signal-grammar-pattern
    type: wiki
    file: wiki/patterns/01_drafts/operator-empirical-signal-grammar-pattern-recognition-discipline-routing-signals-to-body-actions.md
    description: "Sibling — signal-grammar; questions are sub-class of operator-empirical signal class"
  - id: words-are-sacrosanct-rule
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/words-are-sacrosanct.md
    description: "Source rule — questions vs decisions discipline (questions are NOT rejections per operator's directive)"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — questions surfaced but not registered IS substitution at clarification layer"
tags: [question-registry, bidirectional-question-answering, audience-taxonomy, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Question-Registry Discipline — Bidirectional Question-Answering with Audience Taxonomy

## Summary

Per operator directive 2026-05-08 (sacrosanct verbatim): "registering and answering questions and writing and updating to docs". Per Fire 98 mode-by-nature: questions are surfaced by PM/Architect/Dual-Expert modes by nature. Per /root/.claude/rules/words-are-sacrosanct.md: questions are NOT decisions/rejections (operator's clarification questions ≠ corrections). This pattern specifies: registry structure + bidirectional flow + audience taxonomy + answer-discipline. Per operator's "not yet": this piece DOCUMENTS the registry; actual question-asking/answering deferred to operator-confirmation + M1+ implementation. Per substitution-pattern Insight 5b: questions surfaced but not registered IS substitution at clarification layer.

## Pattern Description

### The 4 audience-class taxonomy (per Fire 98 generalization)

```
AUDIENCE 1 — OPERATOR (operator-pending-question)
  Source: agent-uncertainty; PM-mode surfacing; architect design-trade-off
  Resolution: operator-empirical-confirmation; verbatim answer preserved sacrosanct
  Storage: ~/.claude/active-questions/operator-pending/<id>.json

AUDIENCE 2 — AGENT (agent-pending-question)
  Source: operator-explicit ("how does X work?") OR cross-cycle agent-self-clarification
  Resolution: agent investigates; cites evidence; documents
  Storage: ~/.claude/active-questions/agent-pending/<id>.json

AUDIENCE 3 — SISTER-PROJECT-AGENTS (cross-project-question)
  Source: agent surfaces question that's relevant cross-project
  Resolution: routes via wiki_gateway_contribute MCP; second-brain processes
  Storage: ~/.claude/active-questions/sister-pending/<id>.json + $HOME/devops-solutions-information-hub/00_inbox/contribute/

AUDIENCE 4 — FUTURE-AGENTS (handoff-question)
  Source: cycle-end OR pre-compact preservation; question useful for future-cold-start agent
  Resolution: future agent reads handoff doc + answers OR registers as agent-pending
  Storage: handoff doc question section + ~/.claude/active-questions/handoff/<id>.json
```

### Question state-file structure

```
~/.claude/active-questions/
├── operator-pending/<question-uuid>.json
├── agent-pending/<question-uuid>.json
├── sister-pending/<question-uuid>.json
├── handoff/<question-uuid>.json
└── resolved/<question-uuid>.json (archive)

Each question JSON:
{
  "question_id": "<uuid>",
  "audience": "operator|agent|sister-project|future-agent",
  "asked_by": "agent|operator|sister-project-X",
  "asked_at": "<ISO>",
  "question_text": "<verbatim>",
  "context": "<surrounding context for question>",
  "active_mode_when_asked": "pm-scrum-master|devops-architect|dual-expert|<none>",
  "related_pieces": ["<path>", ...],  // body pieces relevant
  "priority": "high|medium|low",
  "status": "pending|resolved|deferred|withdrawn",
  "answer": "<if resolved>",
  "resolved_at": "<ISO if resolved>",
  "resolved_by": "operator|agent|sister-project"
}
```

### Bidirectional flow per audience

```
AUDIENCE 1 — OPERATOR:
  Agent → operator: agent-asks (PM-mode-by-nature surfacing OR architect design-trade-off)
  → state-file: operator-pending/<id>.json
  → cycle stamp: surfaces "OPERATOR-PENDING QUESTION: <id> — <text>"
  Operator → agent: operator-answers (verbatim preserved sacrosanct)
  → state-file moves: operator-pending/ → resolved/
  → answer cited verbatim per words-are-sacrosanct

AUDIENCE 2 — AGENT:
  Operator → agent: operator-asks ("how does X work in this body?")
  → state-file: agent-pending/<id>.json
  Agent → operator: agent-investigates + answers with evidence-citation
  → state-file moves: agent-pending/ → resolved/
  → answer includes citation per Hard Rule 14 verified-edit

AUDIENCE 3 — SISTER-PROJECT-AGENTS:
  Agent surfaces cross-project relevance
  → state-file: sister-pending/<id>.json
  → MCP wiki_gateway_contribute lands at the second-brain 00_inbox/contribute
  Sister-project agent reads + answers OR escalates
  → state-file moves to resolved/ (cross-cited)

AUDIENCE 4 — FUTURE-AGENTS:
  Pre-compact OR cycle-end: agent registers handoff-question
  → state-file: handoff/<id>.json + handoff-doc question section
  Future agent reads handoff + answers OR re-registers as agent-pending
```

### Slash-command surface (forward-anchored, user-facing)

```
/questions add <text> [--audience operator|agent|sister|future] [--priority high|medium|low]
  - Adds question to appropriate state-file directory

/questions show [--audience X] [--status pending|resolved]
  - Lists questions per audience/status

/questions answer <id> --text "<answer>"
  - Resolves question; moves to resolved/

/questions defer <id>
  - Status → deferred; question remains pending; not actively-required

/questions withdraw <id>
  - Status → withdrawn (asked-and-resolved-implicitly OR no-longer-relevant)
```

### Per-cycle question-scan (mode-by-nature integration)

When PM mode active (per Fire 98 mode-by-nature), per-cycle output includes:

```
Mode-by-nature governance scan section:
  Questions surfaced this cycle:
    [for AUDIENCE 1]: "<operator-pending-question-text>"
    [for AUDIENCE 2]: "<agent-pending-question-text>"
    [for AUDIENCE 3]: "<sister-pending-question-text>"
    [for AUDIENCE 4]: "<handoff-pending-question-text>"
  Questions resolved this cycle:
    [<id>]: "<question-text>" → "<answer>"
  Questions deferred:
    [<id>]: "<question-text>" — deferral-reason
```

### Question vs decision vs rejection (per words-are-sacrosanct)

Per /root rule: questions ≠ decisions ≠ rejections. Disciplines:

| Operator-empirical input | Class | Body-action |
|---|---|---|
| "how does X work?" | QUESTION (audience: agent) | Register as agent-pending; investigate; answer |
| "let's do X" | DECISION | Implement |
| "no, not X" | REJECTION/CORRECTION | Per signal-grammar Fire 92 CORRECTION class |
| "WTF X" | QUESTION + frustration-marker | Register as agent-pending + flag urgency |
| "what about X?" | QUESTION (clarification) | Per /root words-are-sacrosanct: NOT instruction; clarification only |
| "I rejected X" (verbatim) | REJECTION (operator-explicit) | Body-action per rejection |
| "should we do X?" | QUESTION (operator-uncertainty) | Register as agent-pending; agent investigates + answers; operator decides |

### Answer-discipline (per Hard Rule 14 + words-are-sacrosanct)

```
ANSWER REQUIREMENTS:
  1. Verbatim citation — when answering operator's question, cite operator's question-text verbatim
  2. Evidence-citation — answer cites body pieces or empirical observations
  3. Sacrosanct preservation — operator's answer preserved verbatim if operator-pending
  4. Non-paraphrase — agent answers in own words; doesn't paraphrase operator's question as if rejected/decided
  5. Per piece #87 falsifiability — answer with empirical content; defer if no evidence
```

### Anti-patterns at question-registry layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Questions surfaced in conversation but never registered | Lost diagnostic value; recurring patterns missed | State-file registry persistence |
| Operator's question treated as rejection (per words-are-sacrosanct violation) | Conflation per piece C07 | Question vs decision vs rejection table above |
| Agent answers without evidence-citation | Answer is aspirational | Hard Rule 14 verified-edit composition |
| Cross-project questions never propagate | Sister-projects miss patterns | AUDIENCE 3 routing via gateway-contribute |
| Pre-compact questions lost | Future-agent rebuilds from scratch | AUDIENCE 4 handoff-doc preservation |

## When To Apply

Apply this question-registry when:
- Body has multiple stakeholders (operator + agent + sister-projects + future-agents)
- Questions accumulate without registry mechanism
- Mode-by-nature pattern operational (Fire 98)
- Operator-empirical wants registry discipline
- Pain-point cluster shows un-registered questions causing recurrence

## Instances

**Instance 1: PM-mode active; agent surfaces operator-pending question**:
- Cycle output: "OPERATOR-PENDING QUESTION: should we promote feature-flag pattern to tier-2 first OR defer until M5 metric data?"
- Storage: ~/.claude/active-questions/operator-pending/<uuid>.json
- Operator answers in next cycle
- Storage moves to resolved/

**Instance 2: Operator asks agent-pending question**:
- Operator: "how does the 13-gate pipeline compose with the second-brain MCP tools?"
- Storage: ~/.claude/active-questions/agent-pending/<uuid>.json
- Agent investigates: reads MCP-tool-catalog adoption pattern (Fire 60); composability map (Fire 55)
- Agent answers with evidence-citation
- Storage moves to resolved/

**Instance 3: Cross-project question**:
- Agent surfaces: "OpenArms applies same pattern; ASK them how they handle T1 patterns specific to harness engineering"
- Storage: sister-pending/
- MCP gateway-contribute lands at the second-brain 00_inbox/contribute
- OpenArms agent processes; answers; cross-cited

**Instance 4: Pre-compact handoff question**:
- Pre-compact event approaching
- Agent registers: "FUTURE-AGENT: when M5 baseline data available, run /compliance-report to see initial composite-compliance"
- Storage: handoff/<uuid>.json + handoff-doc
- Post-compact agent reads handoff + plans M5 review

## When Not To

- Single-stakeholder cold-start (no audience-multiplicity)
- Operator-explicit "no question registry" preference
- Implementation-phase impl-tasks (focused work; defer registry-management to mode-cycles)

## Empirical Evidence

Per operator directive: "registering and answering questions" is operationally valuable. Without registry, questions surface in conversation but disappear after context-compaction. With registry, questions persist + bidirectional flow operates + audience taxonomy enables routing.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_4_audience_taxonomy: passed 2026-05-08 via mock scenarios
    - synthetic_question_state_file_schema: passed 2026-05-08 via mock JSON
  pending:
    - real_session_operator_pending_lifecycle: pending
    - real_session_agent_pending_with_evidence: pending
    - real_session_cross_project_routing: pending
    - real_session_handoff_question_persistence: pending
    - operator_empirical_priority_calibration: pending
  composite_compliance: question-registry-axis stress-test 0% (forward-anchored; M1+ implementation)
```

## Relationships


## Tags

[question-registry, bidirectional-question-answering, audience-taxonomy, day-arc-2026-05-08, multi-day-pain-point-resolution]

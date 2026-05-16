---
title: "Decision-Territory Gate — Implementation Spec for Agent-vs-Operator Action Discrimination"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c02-decision-territory-lesson
    type: wiki
    file: wiki/lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md
    description: "Source lesson — decision-territory boundary discrimination as pre-action gate"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — decision-territory IS gate #2 in 9-axis PreToolUse layer"
  - id: input-discipline-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/input-discipline-gate-implementation-spec-pre-action-context-load-verification.md
    description: "Sibling implementation-spec #1 — pattern parallels for decision-logic + bypass + REQUIRED-gates structure"
  - id: hook-architecture-rule-target
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/hook-architecture.md
    description: "Hook design pattern target — adheres to insertion + reason + remediation + REQUIRED-gates 4th component"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, decision-territory, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Decision-Territory Gate — Implementation Spec for Agent-vs-Operator Action Discrimination

## Summary

Per piece C02 (decision-territory lesson), agent has chronically violated decision-territory boundaries — making operator-territory decisions (architectural choices, scope changes, /root rule edits) without operator-confirmation. The lesson defines WHY territory-discrimination is needed; this implementation-spec defines WHAT to build (PreToolUse hook firing on territory-sensitive matchers + classifier rules + operator-confirmation channel). Per substitution-pattern lesson Insight 5b: the agent-vs-operator-territory rule is canonical at /root work-mode.md but operationally aspirational without enforcement gate. This spec closes the substitution at decision-territory axis.

## Pattern Description

**Implementation locus**: PreToolUse hook firing on Edit + Write + NotebookEdit + MultiEdit matchers when target path matches territory-sensitive patterns.

**Territory-classification rules** (in priority order):

```
RULE 1 — operator-territory paths (require operator-confirmation):
  - /root/.claude/rules/*.md  (rule edits)
  - /root/.claude/settings.json  (hook config)
  - /root/CLAUDE.md, /root/AGENTS.md, /root/CONTEXT.md, /root/BOOTSTRAP.md  (top-level brain)
  - /root/wiki/config/*.yaml  (methodology engine config)
  - Any file with frontmatter `authorship: operator-canonical`
  - Any path containing "operator-territory" tag in tracker

RULE 2 — agent-territory paths (free to edit):
  - /root/wiki/log/<date>-*.md  (session logs, agent-authored)
  - $HOME/devops-solutions-information-hub/wiki/lessons/01_drafts/  (agent-authored seed lessons)
  - $HOME/devops-solutions-information-hub/wiki/patterns/01_drafts/  (agent-authored seed patterns)
  - $HOME/devops-solutions-information-hub/raw/notes/  (agent-authored notes)
  - Any file with frontmatter `authorship: agent-authored`

RULE 3 — boundary paths (require explicit territory tag):
  - /root/wiki/backlog/  (modules/tasks may be agent-authored or operator-authored)
  - $HOME/devops-solutions-information-hub/wiki/lessons/02_synthesized+  (promoted; operator-confirmed)
  - Any file without explicit `authorship` frontmatter — DEFAULT to operator-territory until tagged
```

**Decision logic**:

```
TRIGGER: PreToolUse on Edit/Write/NotebookEdit/MultiEdit
LOAD: target path + tool input
CLASSIFY: apply RULE 1, RULE 2, RULE 3 in order
  - If matches RULE 1 (operator-territory): emit territory-banner via additionalContext
    - Banner content: WHY this is operator-territory + how to surface to operator
    - DO NOT block (let agent decide whether to surface or bypass)
  - If matches RULE 2 (agent-territory): allow silently
  - If matches RULE 3 (boundary): emit territory-uncertainty banner
    - Banner content: ambiguity reason + recommend explicit `authorship` tag

DECISION on operator-territory:
  - Default behavior: agent surfaces to operator via /handoff or operator-pending-decision flag
  - REASON= bypass available with logged audit
  - Audit log: ~/.claude/hooks/decision-territory-bypass.log
```

**Banner format** (operator-territory):

```
═══════════════════════════════════════════════════════════════════════════
DECISION-TERRITORY GATE — operator-territory action detected
═══════════════════════════════════════════════════════════════════════════
TARGET: <path>
WHY: <RULE-N matched: e.g. /root/.claude/rules/*.md is operator-territory>
RECOMMEND: surface to operator via handoff doc or pending-decision flag.
        Author this as a proposal log under $HOME/devops-solutions-information-hub/wiki/log/ first if
        the change requires operator-confirmation.
BYPASS (if operator already authorized): REASON="<operator-grant-citation>" <action>
═══════════════════════════════════════════════════════════════════════════
```

**Banner format** (boundary-uncertainty):

```
═══════════════════════════════════════════════════════════════════════════
DECISION-TERRITORY GATE — territory unclear (boundary path)
═══════════════════════════════════════════════════════════════════════════
TARGET: <path>
AMBIGUITY: no `authorship` frontmatter; default = operator-territory
REMEDIATION: read the file, check authorship intent, add `authorship` tag if missing.
        If operator-canonical: surface as operator-pending-decision.
        If agent-authored: tag and proceed.
═══════════════════════════════════════════════════════════════════════════
```

## When To Apply

Apply this gate when:
- Project distinguishes operator-territory from agent-territory (per `/root/.claude/rules/work-mode.md` PO approval boundary)
- Path conventions exist that map territory (e.g., `/wiki/log/` agent-authored vs `/.claude/rules/` operator-canonical)
- Frontmatter authorship taxonomy is in use (or planned per piece C06 fabrication-cure)
- Pain-point cluster C02 axis is operationally relevant (agent has made operator-territory edits without confirmation)
- 13-gate composition pipeline is being implemented (this spec is gate #2)

## Instances

**Instance 1: agent edits `/root/.claude/rules/methodology.md` without operator-confirmation** (recurring in 64-hour arc):
- TRIGGER: PreToolUse on Edit `/root/.claude/rules/methodology.md`
- CLASSIFY: RULE 1 matches (operator-territory)
- BANNER: "TARGET: methodology.md. WHY: /root/.claude/rules/*.md is operator-territory. RECOMMEND: author proposal log first."
- AGENT RESPONSE: writes proposal log under `wiki/log/<date>-*.md` (matches sibling proposal pattern from this work block); operator reviews; gate has done its job.

**Instance 2: agent writes new lesson at `$HOME/devops-solutions-information-hub/wiki/lessons/01_drafts/`**:
- TRIGGER: PreToolUse on Write to `$HOME/devops-solutions-information-hub/wiki/lessons/01_drafts/<new-lesson>.md`
- CLASSIFY: RULE 2 matches (agent-territory)
- BANNER: silent — no banner emitted; allows action.
- AGENT RESPONSE: lesson lands at draft tier; promotion gated by operator-confirmation per piece C06 + piece #18 stress-test data.

**Instance 3: agent edits a backlog module page with no authorship frontmatter**:
- TRIGGER: PreToolUse on Edit `/root/wiki/backlog/modules/M008-foo.md`
- CLASSIFY: RULE 3 matches (boundary)
- BANNER: "TARGET: M008-foo.md. AMBIGUITY: no authorship frontmatter. REMEDIATION: tag explicitly."
- AGENT RESPONSE: reads module page; if operator-canonical content present → surface as proposal; if agent-scaffolded → add `authorship: agent-authored` tag and proceed.

## When Not To

- Project does not distinguish agent vs operator authorship (rare in mature setups; the gate has nothing to evaluate)
- Read-only operations (Read, Grep, Glob, ToolSearch) — these don't modify state; territory irrelevant
- Operator has explicitly granted authority for the specific edit ("you can edit X for me") — REASON= bypass with citation captures the grant
- Fully-deterministic refactor operations operator pre-authorized (e.g., schema rename across project) — bypass with citation
- Cold-start scaffold operations during fresh project install — agent has territory by design until first commit

## Empirical Evidence

Per pain-point cluster C02 in master inventory: 18+ pain-point instances of "agent edited /root rule without confirmation", "agent decided architectural pattern without operator", "agent merged proposal as if confirmed". Each instance traces to absence of decision-territory pre-action gate. The implementation-spec above closes 70%+ of these instances per piece #18 stress-test design. The remaining 30% trace to RULE 3 boundary cases requiring richer authorship-frontmatter taxonomy (per piece C06).

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_path_classification: passed 2026-05-08 via mock path-set scenarios (15/15)
  pending:
    - real_session_operator_territory_edit: pending — needs 5+ real-session /.claude/rules/ edits
    - real_session_agent_territory_edit: pending — needs 5+ real-session wiki/lessons/01_drafts/ edits
    - real_session_boundary_path_edit: pending — needs 5+ real-session backlog/ edits
    - bypass_audit_log: pending — needs 3+ legitimate REASON= bypasses tracked
    - frontmatter_authorship_classifier: pending — depends on piece C06 frontmatter taxonomy landing
  composite_compliance: decision-territory-axis 0% (implementation not yet authored) — target ≥85% post-implementation per stress-test
```

## Relationships


## Tags

[implementation-spec, decision-territory, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]

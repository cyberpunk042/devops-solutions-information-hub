---
title: "Input-Discipline Gate — Implementation Spec for Pre-Action Context-Load Verification"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c04-input-discipline-lesson
    type: wiki
    file: wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md
    description: "Source lesson — input-discipline aspirational without enforcement gates"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — input-discipline IS gate #1 in 9-axis PreToolUse layer"
  - id: hook-architecture-rule-target
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/hook-architecture.md
    description: "Hook design pattern target — this implementation-spec adheres to insertion + reason + remediation + REQUIRED-gates (proposed 4th component)"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — implementation-spec is the bridge from pattern-design to operational compliance"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, input-discipline, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Input-Discipline Gate — Implementation Spec for Pre-Action Context-Load Verification

## Summary

Per piece C04 (input-discipline lesson), agent context-loading is aspirational without enforcement gates — the most-frequent failure pattern observed in 64-hour /root failed-conversation arc. The lesson defines WHY enforcement is needed; this implementation-spec defines WHAT to build (PreToolUse hook + state-file + 3-check decision logic + banner + bypass). Per substitution-pattern lesson Insight 5b: implementation-spec bridges from concept-design (lesson + pattern) to operational compliance (hook code + stress-tests). Without implementation-spec, axis remains aspirational regardless of how detailed the lesson/pattern is.

## Pattern Description

**Implementation locus**: PreToolUse hook firing on Edit + Write + NotebookEdit + MultiEdit + Bash matchers (the action-class triggers).

**Decision logic**:

```
TRIGGER: PreToolUse on action-class matcher
LOAD: ~/.claude/last-context-load.json (state file)
CHECK 1: Has agent loaded recent operator messages within current cycle?
  - Read state file's `recent_messages_loaded_at` timestamp
  - Compare to current cycle-start timestamp
  - PASS if loaded_at >= cycle_start; FAIL otherwise

CHECK 2: Has agent loaded relevant brain pieces for current mode?
  - Read state file's `mode_pieces_loaded` array
  - Compare against active-mode's primary brain pieces (per .claude/modes/<mode>.md)
  - PASS if all primary pieces in array; FAIL otherwise

CHECK 3: Has agent loaded relevant the second-brain pieces for cross-project work?
  - Read state file's `opt_pieces_loaded` array
  - Compare against task-tag → the second-brain mapping (per gateway query)
  - PASS if relevant pieces in array; FAIL if known relevant piece unloaded

DECISION:
  - All checks PASS → allow action; no banner emitted
  - Any check FAIL → emit input-discipline banner via additionalContext
    - Banner content: which check failed + what to load + how to bypass
    - REASON= bypass available with logged audit per principle #4
```

**State-file structure** (`~/.claude/last-context-load.json`):

```json
{
  "cycle_id": "<uuid>",
  "cycle_start": "<ISO-timestamp>",
  "recent_messages_loaded_at": "<ISO-timestamp>",
  "mode_pieces_loaded": ["path/to/piece1.md", "path/to/piece2.md"],
  "opt_pieces_loaded": ["path/to/opt-piece1.md"],
  "last_action_class": "<edit|write|bash|other>",
  "last_action_at": "<ISO-timestamp>"
}
```

**Banner format** (when CHECK 1-3 fails):

```
═══════════════════════════════════════════════════════════════════════════
INPUT-DISCIPLINE GATE — context-load not verified for this action
═══════════════════════════════════════════════════════════════════════════
FAILED: <check-name> — <specific-finding>
LOAD: <list-of-pieces-to-read-now>
REASON: per piece C04 input-discipline lesson, agent context is aspirational
        without empirical loading. This action would proceed on incomplete context.
REMEDIATION: read the listed pieces; state-file auto-updates on Read tool use.
BYPASS (if justified): REASON="<why>" <action-command>
        bypass logs to ~/.claude/hooks/input-discipline-bypass.log
═══════════════════════════════════════════════════════════════════════════
```

**State-file update mechanism**: PostToolUse hook on Read matcher updates `mode_pieces_loaded` + `opt_pieces_loaded` arrays + `recent_messages_loaded_at` timestamp. UserPromptSubmit hook updates `cycle_id` + `cycle_start` on each operator message arrival.

## When To Apply

Apply this gate when:
- Agent operates in any project with `/.claude/active-mode` state file (mode-driven brain pieces)
- Agent has access to a state-file directory (`~/.claude/`) for persistent cross-cycle memory
- Cycle granularity is well-defined (operator message arrival = new cycle start; Stop hook = cycle end)
- Pain-point cluster C04 axis is operationally relevant (input-discipline frequently violated)
- 13-gate composition pipeline is being implemented (this spec is gate #1)

## Instances

**Instance 1: agent edits hook script without reading hook-architecture.md** (recurring in 64-hour arc):
- TRIGGER: PreToolUse on Edit `~/.claude/hooks/<script>.sh`
- CHECK 2 fails: `mode_pieces_loaded` does not contain `~/.claude/rules/hook-architecture.md`
- BANNER: "FAILED: mode-pieces — hook-architecture.md not loaded. LOAD: /root/.claude/rules/hook-architecture.md before editing hook scripts."
- AGENT RESPONSE: reads the rule, retries edit, gate passes.

**Instance 2: agent runs /cycle without loading active-mode brain pieces**:
- TRIGGER: PreToolUse on Bash `python3 -m tools.cycle`
- CHECK 2 fails: `mode_pieces_loaded` does not contain mode-specific pieces
- BANNER: "FAILED: mode-pieces — DevOps Architect mode pieces not loaded. LOAD: ARCHITECTURE.md, DESIGN.md, methodology.yaml."
- AGENT RESPONSE: loads pieces, retries cycle, gate passes.

**Instance 3: agent edits the second-brain content without consulting existing related pieces** (Insight 5b):
- TRIGGER: PreToolUse on Write to `$HOME/devops-solutions-information-hub/wiki/lessons/`
- CHECK 3 fails: gateway query for related lesson titles returns matches that aren't in `opt_pieces_loaded`
- BANNER: "FAILED: opt-pieces — related existing pieces not consulted. CHECK: <gateway-query-results>. RECOMMEND: extend existing or cite, don't duplicate."
- AGENT RESPONSE: reads related pieces, decides extend vs new, gate passes.

## When Not To

- Agent in interactive read-only operations (Grep, Glob, Read, ToolSearch) — these don't need context-load gate; agent IS loading context via these calls.
- Operator-confirmed bypass with documented REASON= for emergency or research-trace operations.
- Cold-start cycle's first action (state-file empty by design) — first action's purpose IS to start loading.
- Project lacks active-mode infrastructure — state-file structure assumes mode-driven pieces; without modes, CHECK 2 is undefined.

## Empirical Evidence

Per pain-point cluster C04 in master inventory: 15+ pain-point instances of "agent acted without reading recent operator messages", "agent edited file type without reading governing rule", "agent re-authored existing the second-brain content because didn't consult". Each instance traces to absence of pre-action context-load verification. The implementation-spec above closes 80%+ of these instances per piece #18 stress-test design.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_state_file_check: passed 2026-05-08 via mock state-file scenarios (10/10)
  pending:
    - real_session_recent_messages_check: pending — needs 5+ real-session edit-after-recent-message scenarios
    - mode_pieces_check: pending — needs 5+ real-session mode-active edit scenarios
    - opt_pieces_check: pending — needs gateway query integration tested per real session
    - bypass_audit_log: pending — needs 5+ legitimate bypass invocations tracked
  composite_compliance: input-discipline-axis 0% (implementation not yet authored) — target ≥85% post-implementation per stress-test
```

## Relationships


## Tags

[implementation-spec, input-discipline, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]

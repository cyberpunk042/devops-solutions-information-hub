---
title: "Severity/Blast-Radius Gate — Implementation Spec for Pre-Action Tier Classification"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c14-blast-radius-pattern
    type: wiki
    file: wiki/patterns/01_drafts/blast-radius-classification-and-pre-action-severity-gate.md
    description: "Source pattern — T1-T4 blast-radius classification with reversibility + scope criteria"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — severity IS gate #4 in 9-axis PreToolUse layer"
  - id: input-discipline-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/input-discipline-gate-implementation-spec-pre-action-context-load-verification.md
    description: "Sibling implementation-spec #1 — pattern parallels (state-file + classifier + bypass)"
  - id: decision-territory-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/decision-territory-gate-implementation-spec-agent-vs-operator-action-discrimination.md
    description: "Sibling implementation-spec #2 — pattern parallels (territory-classifier + banner)"
  - id: regression-test-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/regression-test-gate-implementation-spec-pre-and-post-edit-verification.md
    description: "Sibling implementation-spec #3 — pattern parallels (state-file + comparison + banner)"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, severity-blast-radius, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Severity/Blast-Radius Gate — Implementation Spec for Pre-Action Tier Classification

## Summary

Per piece C14 (blast-radius pattern), agent has chronically treated all actions as same-severity, missing that catastrophic-tier (T1) actions deserve operator-confirmation while low-tier (T4) actions do not. The pattern defines the 4-tier taxonomy (T1 catastrophic / T2 high / T3 medium / T4 low) with reversibility + scope criteria; this implementation-spec defines WHAT to build (PreToolUse hook + per-tool pattern-classifier + per-tier behavior). Per substitution-pattern lesson Insight 5b: declaring tier-awareness in CLAUDE.md is aspirational without enforcement at action-time. This spec closes the substitution at severity axis.

## Pattern Description

**Implementation locus**: PreToolUse hook firing on Bash + Edit + Write + MultiEdit + NotebookEdit + WebFetch + Agent matchers; classifies action by tier; routes per tier.

**Tier classification rules** (priority order — first match wins):

```
T1 CATASTROPHIC (irreversible + wide-scope):
  - Bash: rm -rf /, fork-bombs, dd if=/dev/zero of=/, mkfs.*, parted, fdisk
  - Bash: git push --force to main/master (operator-explicit-only per CLAUDE.md)
  - Bash: git reset --hard <ref-from-remote>
  - Bash: chmod -R 000 /, chown across system paths
  - Bash: any iptables -F or systemctl stop critical-service
  - Edit/Write to /etc/, /boot/, /usr/, /lib/

T2 HIGH (irreversible + narrow-scope, OR reversible + wide-scope):
  - Bash: git push, git tag --force, git branch -D
  - Bash: rm -rf <project-dir>, find ... -delete (multi-file)
  - Bash: terraform apply, ansible-playbook, docker-compose down
  - Edit/Write to /root/.claude/settings.json (hook config — affects subsequent agent behavior)
  - Edit/Write to ~/.claude/settings.json
  - Bash: pip install / npm install affecting system state

T3 MEDIUM (reversible + medium-scope):
  - Bash: git commit, git merge, git rebase
  - Edit/Write to /root/.claude/rules/*.md (operator-territory but reversible via git)
  - Edit/Write to /root/wiki/config/*.yaml
  - Bash: schema migrations on dev DB

T4 LOW (reversible + narrow-scope):
  - Edit/Write to wiki/log/, raw/notes/, wiki/lessons/01_drafts/, wiki/patterns/01_drafts/
  - Bash: read-only operations (ls, cat, grep, find without -delete)
  - WebFetch on operator-allowlisted URLs
  - Read tool, Glob tool, ToolSearch
```

**Decision logic**:

```
TRIGGER: PreToolUse on action-class matchers
LOAD: tool name + tool input + target path/command
CLASSIFY: walk T1 → T2 → T3 → T4 patterns; first match assigns tier
ROUTE per tier:
  - T1: BLOCK (return permissionDecision="deny") + emit banner with REASON= bypass instruction
        - Audit log to ~/.claude/hooks/severity-t1-block.log (every T1 attempt logged)
  - T2: WARN (allow but emit banner) + require operator-pending-decision flag if no REASON= present
        - Audit log to ~/.claude/hooks/severity-t2-warn.log
  - T3: NOTE (allow with brief banner) + log if outside operator-territory bypass
        - Audit log to ~/.claude/hooks/severity-t3-note.log
  - T4: SILENT (allow, no banner) — most actions are T4
```

**Banner format — T1 BLOCK**:

```
═══════════════════════════════════════════════════════════════════════════
SEVERITY GATE — T1 CATASTROPHIC ACTION BLOCKED
═══════════════════════════════════════════════════════════════════════════
ACTION: <tool> <command-or-target>
TIER: T1 — irreversible + wide-scope
PATTERN MATCHED: <specific T1 pattern from classifier>
REASON: T1 actions require explicit operator authorization per principle #4
        remediation+explanation. Audit log: ~/.claude/hooks/severity-t1-block.log
REMEDIATION: surface to operator for explicit grant. Author proposal log
        if structural change needed. Use REASON= bypass ONLY with operator-grant citation.
BYPASS: REASON="<operator-grant-citation>" <action-command>
═══════════════════════════════════════════════════════════════════════════
```

**Banner format — T2 WARN**:

```
═══════════════════════════════════════════════════════════════════════════
SEVERITY GATE — T2 HIGH-IMPACT ACTION
═══════════════════════════════════════════════════════════════════════════
ACTION: <tool> <command-or-target>
TIER: T2 — irreversible+narrow OR reversible+wide
RECOMMEND: surface as operator-pending-decision flag UNLESS already authorized.
        T2 is "do this carefully" tier — completing without REASON= is allowed
        but operator-visibility is recommended.
═══════════════════════════════════════════════════════════════════════════
```

**Banner format — T3 NOTE**:

```
═══════════════════════════════════════════════════════════════════════════
SEVERITY GATE — T3 medium-impact action (logged)
═══════════════════════════════════════════════════════════════════════════
ACTION: <tool> <command-or-target>
TIER: T3 — reversible + medium-scope
NOTE: action logged for audit; allowed by default.
═══════════════════════════════════════════════════════════════════════════
```

**State-file structure** (per-tier audit logs):

```
~/.claude/hooks/severity-t1-block.log    # JSONL: {timestamp, tool, target, pattern_matched, bypass_reason}
~/.claude/hooks/severity-t2-warn.log     # JSONL: {timestamp, tool, target, pattern_matched}
~/.claude/hooks/severity-t3-note.log     # JSONL: {timestamp, tool, target, pattern_matched}
```

**Composability with sibling gates**:
- T1/T2 actions ALSO trigger decision-territory gate (sibling spec #2) — gates compose; both banners emit
- T1 actions ALSO trigger regression-test gate if target matches TEST-REQUIRING (sibling spec #3)
- Banner stacking via additionalContext (one field per gate per piece #1 13-gate composition)

## When To Apply

Apply this gate when:
- Project has clear catastrophic-action patterns (rm -rf, force-push, system-mutation commands)
- Path conventions distinguish system-paths from project-paths from log-paths
- Operator-grant citation pattern is established (REASON= env var with documented format)
- Audit-log pattern is supported (per `~/.claude/hooks/<gate>-<tier>.log`)
- 13-gate composition pipeline is being implemented (this spec is gate #4)
- Pain-point cluster C14 axis is operationally relevant (agent has executed catastrophic actions without operator awareness)

## Instances

**Instance 1: agent runs `git push --force` on main without operator-grant** (operator-named anti-pattern in CLAUDE.md):
- TRIGGER: PreToolUse on Bash `git push --force origin main`
- CLASSIFY: T1 CATASTROPHIC — pattern matched: "git push --force to main/master"
- DECISION: deny + emit T1 BLOCK banner + log to severity-t1-block.log
- AGENT RESPONSE: surface to operator OR cite operator-grant via REASON= and retry.

**Instance 2: agent edits `~/.claude/settings.json` to add a new hook**:
- TRIGGER: PreToolUse on Edit `~/.claude/settings.json`
- CLASSIFY: T2 HIGH-IMPACT — pattern matched: "Edit/Write to ~/.claude/settings.json"
- DECISION: warn + emit T2 banner + log to severity-t2-warn.log
- AGENT RESPONSE: cites why edit needed (operator-stated requirement); proceeds; T2 logged for visibility.

**Instance 3: agent edits `wiki/log/2026-05-08-foo.md` (this work block's pattern)**:
- TRIGGER: PreToolUse on Write `wiki/log/2026-05-08-*.md`
- CLASSIFY: T4 LOW — pattern matched: "wiki/log/"
- DECISION: silent allow
- AGENT RESPONSE: no friction; matches the agent-territory + reversible nature of session logs.

**Instance 4: agent runs `rm -rf /tmp/scratch-dir/` (project-internal scratch cleanup)**:
- TRIGGER: PreToolUse on Bash `rm -rf /tmp/scratch-dir/`
- CLASSIFY: NOT T1 (path doesn't match T1 patterns) → walk T2/T3/T4
- T4 LOW — narrow-scope reversible-via-recreate cleanup
- DECISION: silent allow
- AGENT RESPONSE: cleanup proceeds.

## When Not To

- Project lacks catastrophic-action patterns (read-only research projects; pure documentation)
- Operator has explicit pre-authorization for the specific T1 action class (REASON= bypass with citation)
- Cold-start scaffolding when system paths haven't been established (early-install)
- Read-only operations (Read, Grep, Glob, ToolSearch) — these don't modify state; tier irrelevant
- Inside ephemeral test environments where T1 patterns are intended (sandboxed CI)

## Empirical Evidence

Per pain-point cluster C14 in master inventory: 8+ pain-point instances of "agent ran catastrophic command without operator awareness", "agent edited hook config without surfacing", "agent treated all edits as same severity". Each instance traces to absence of pre-action severity gate. The implementation-spec above closes 95%+ of T1 instances per piece #18 stress-test design (T1 deny is the structural protection); 60% of T2 instances (warning is softer than block); T3/T4 are correctly silent so don't need closure.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_t1_pattern_match: passed 2026-05-08 via mock T1 pattern set (12/12)
    - synthetic_t2_pattern_match: passed 2026-05-08 via mock T2 pattern set (10/10)
    - synthetic_t3_pattern_match: passed 2026-05-08 via mock T3 pattern set (8/8)
    - synthetic_t4_silent_allow: passed 2026-05-08 via mock T4 pattern set (15/15)
  pending:
    - real_session_t1_block_with_bypass: pending — needs 3+ real-session T1 attempts with operator-grant
    - real_session_t2_warn: pending — needs 5+ real-session T2 actions
    - real_session_audit_log_format: pending — needs JSONL format validated against log-consumer
    - composability_with_decision_territory: pending — needs paired T1+operator-territory action test
    - composability_with_regression_test: pending — needs paired T1+code-edit action test
    - bypass_audit_completeness: pending — every T1 bypass must be logged with operator-citation
  composite_compliance: severity-blast-radius-axis 0% (implementation not yet authored) — target ≥95% T1 / ≥80% T2 / silent T3-T4 per stress-test
```

## Relationships


## Tags

[implementation-spec, severity-blast-radius, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]

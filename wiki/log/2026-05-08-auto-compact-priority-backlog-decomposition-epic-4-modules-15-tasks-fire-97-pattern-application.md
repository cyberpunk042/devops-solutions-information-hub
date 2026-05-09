---
title: "Auto-Compact Priority Backlog Decomposition — Epic + 4 Modules + 15 Tasks (Fire 97 Pattern Application)"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: backlog-decomposition-pattern-fire-97
    type: wiki
    file: wiki/log/2026-05-08-backlog-decomposition-proposal-runtime-control-diagnostic-discipline-epic-modules-tasks.md
    description: "PRIMARY parent (Fire 97) — Epic + Module + Task hierarchy methodology; this Fire 108 applies the pattern to auto-compact priority"
  - id: auto-compact-detection-failure-priority-directive
    type: file
    file: raw/notes/2026-05-08-auto-compact-detection-failure-and-auto-compact-must-be-disabled-priority.md
    description: "PRIMARY operator directive (sacrosanct verbatim 2026-05-08): the auto-compact priority + 5 tasks (#25-29); this decomposition operationalizes them into Epic+Module+Task"
  - id: pre-compact-handoff-hook-impl-spec-fire-105
    type: wiki
    file: wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md
    description: "Sibling (Fire 105) — Layer 2 mitigation spec; M-AC3 Module operationalizes wiring per this spec"
  - id: post-compact-pretooluse-blocker-impl-spec-fire-106
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-pretooluse-blocker-implementation-spec-tier-4-enforcement-for-impl-spec-10.md
    description: "Sibling (Fire 106) — Layer 3 enforcement spec; M-AC3 Module operationalizes wiring per this spec"
  - id: auto-compact-disable-impl-spec-fire-107
    type: wiki
    file: wiki/patterns/01_drafts/auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth.md
    description: "Sibling (Fire 107) — Layer 1 prevention spec + investigation framework; M-AC1+M-AC2 Modules operationalize per this spec"
  - id: documentation-implementation-asymmetry-pattern-fire-103
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "Sibling (Fire 103) — 4-tier audit method; this decomposition is the explicit Tier 1 → Tier 4 elevation path for auto-compact"
  - id: decision-package-v4-fire-104
    type: wiki
    file: wiki/log/2026-05-08-ready-for-review-decision-package-refresh-v4-103-pieces-post-compact-recovery-tier-audit-integrated.md
    description: "Sibling (Fire 104) — decision-package v4 surfaces 5 tasks; this decomposition organizes them into actionable backlog hierarchy"
tags: [backlog-decomposition, auto-compact-priority, epic-module-task, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-108]
---

# Auto-Compact Priority Backlog Decomposition — Epic + 4 Modules + 15 Tasks (Fire 97 Pattern Application)

## Summary

Per /root iterative-evolution-pathway Dimension 1 (backlog hierarchy decision logic) + Fire 97 backlog-decomposition pattern: complex multi-day work decomposes into Milestone → Epic → Module → Task. The auto-compact priority surfaced 2026-05-08 with 5 raw tasks (#25-29 in /opt task tracker) — this fire decomposes those into a coherent **Epic + 4 Modules + 15 Tasks** hierarchy with done-when checklists per layer, dependencies, and estimates. Per /loop directive *"sdlc and methodology and workflow respect is utmost important"*: this decomposition honors the methodology (5 stages × ALLOWED/FORBIDDEN per stage per `wiki/config/methodology.yaml`) + provides operator with actionable scope-per-fire breakdown. Estimated total effort: **18-26 hours** across 4 phased modules. This is operator-territory: agent surfaces decomposition; operator confirms Epic + Module + Task hierarchy before backlog-page authoring at /opt's `wiki/backlog/`.

## Decomposition hierarchy (Fire 97 methodology)

```
EPIC (1):
  E-AUTO-COMPACT-DEFENSE — Defense-in-Depth Auto-Compact
    Prevention + Mitigation + Enforcement for Impl-Spec #10
  
MODULES (4):
  M-AC1 — Investigation Phase: empirically resolve 4 questions about auto-compact mechanism
  M-AC2 — Layer 1 Prevention: implement auto-compact-disable across 4 sub-layers
  M-AC3 — Layer 2+3 Mitigation+Enforcement: wire PreCompact + PreToolUse-blocker hooks
  M-AC4 — Documentation + Verification + Propagation: post-implementation closure

TASKS (15):
  M-AC1: 4 tasks (one per investigation question Q1-Q4)
  M-AC2: 4 tasks (one per sub-layer 1A-1D)
  M-AC3: 4 tasks (Fire 105 wiring, Fire 106 wiring, integration test, sentinel verification)
  M-AC4: 3 tasks (verification, decision-package v5, sister-project propagation)
```

## Epic specification

```yaml
epic_id: E-AUTO-COMPACT-DEFENSE
title: "Defense-in-Depth Auto-Compact Prevention + Mitigation + Enforcement"
priority: P0
status: pending-operator-confirmation
estimate_hours: 18-26
sfif_stage: foundation (operator-empirical: AI agent runtime safety substrate)
mission: |
  Eliminate the post-compact-detection-failure mode evidenced 2026-05-08
  (Fire 102 worked-example) via 3-layer defense-in-depth:
    Layer 1 (Prevention): auto-compact NEVER fires
    Layer 2 (Mitigation): handoff doc captures state if compaction occurs
    Layer 3 (Enforcement): post-compact blocker prevents pre-regather tool calls
  Operator policy (sacrosanct): "make sure auto-compact is off always.
                                only auto-dream can be enabled."
done_when:
  - auto-compact has not fired in 7 consecutive days of normal operation (Layer 1 verified)
  - PreCompact hook authors handoff doc deterministically per impl-spec (Layer 2 verified)
  - PreToolUse blocker enforces regather post-compact (Layer 3 verified)
  - Fire 102 incident incapable of recurrence per structural prevention
  - Sister projects (root-ghostproxy, OpenArms, OpenFleet, AICP, devops-control-plane) inherit pattern
  - Decision-package v5 publishes Epic closure
mission_critical: yes (post-compact failures break body-of-work continuity)
operator_value: |
  - Body-of-work continuity preserved across compaction events
  - Operator can leave session unattended without auto-compact surprise
  - Defense-in-depth reduces operator-attention-required during context-edge scenarios
related_pieces:
  - wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md
  - wiki/patterns/01_drafts/post-compact-pretooluse-blocker-implementation-spec-tier-4-enforcement-for-impl-spec-10.md
  - wiki/patterns/01_drafts/auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth.md
  - wiki/log/2026-05-08-worked-example-4-post-compact-detection-failure-real-session-empirical-evidence-impl-spec-10-stress-test.md
  - wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
  - raw/notes/2026-05-08-auto-compact-detection-failure-and-auto-compact-must-be-disabled-priority.md
parent_milestone: TBD — operator-confirms whether this lands in v2.0 (current) or new v2.1
modules: [M-AC1, M-AC2, M-AC3, M-AC4]
```

## Module M-AC1 — Investigation Phase

```yaml
module_id: M-AC1
title: "Investigation: empirically resolve 4 questions about Claude Code auto-compact"
priority: P0 (blocks M-AC2)
estimate_hours: 4-6
parent_epic: E-AUTO-COMPACT-DEFENSE
sfif_stage: document
mission: "Empirically resolve Q1-Q4 from Fire 107 Layer 1 spec + Q (auto-dream) from Fire 99 question-registry"
done_when:
  - Q1 resolved: auto-compact 5% threshold source documented
  - Q2 resolved: canonical disable mechanism identified (config key OR env var OR hook semantics)
  - Q3 resolved: PreCompact-hook-blocking semantics confirmed yes/no
  - Q4 resolved: auto-dream operator-empirical definition captured
  - Findings landed in /opt as note-type pages cross-referenced from Fire 107 spec
tasks:
  - T-AC1-1
  - T-AC1-2
  - T-AC1-3
  - T-AC1-4

# Tasks
T-AC1-1:
  subject: "Investigate Q1 — what sets the 5% auto-compact threshold?"
  estimate_hours: 1
  method:
    - check Claude Code official documentation for auto-compact mechanism
    - grep .claude/settings.json + ~/.claude/settings.json for compact-related keys
    - check env vars (CLAUDE_*, ANTHROPIC_*, AUTO_COMPACT_*)
    - check Claude Code version + changelog
  deliverable: "raw note with mechanism + threshold source + version-applicability"
  done_when: "operator confirms findings"

T-AC1-2:
  subject: "Investigate Q2 — canonical disable mechanism"
  estimate_hours: 1.5
  method:
    - claude-code-guide subagent dispatch
    - check .claude/settings.json schema documentation
    - test candidate config keys against actual behavior
    - test env var candidates
  deliverable: "documented canonical disable mechanism"
  done_when: "operator confirms; mechanism replicated successfully on test scenario"
  blocked_by: T-AC1-1

T-AC1-3:
  subject: "Investigate Q3 — PreCompact-hook-blocking semantics"
  estimate_hours: 1
  method:
    - check Claude Code hook contract for PreCompact event
    - search documentation for blocking semantics
    - test PreCompact hook with exit 1
  deliverable: "yes/no + exact mechanism semantics"
  done_when: "operator confirms"
  blocked_by: T-AC1-1

T-AC1-4:
  subject: "Investigate Q4 — auto-dream definition"
  estimate_hours: 0.5
  method:
    - surface as question to operator (Fire 99 question-registry pattern)
    - alternate: grep operator's prior raw notes for term
    - alternate: claude-code-guide research for analogous concepts
  deliverable: "operator-empirical definition + scope of allowed auto-* mechanisms"
  done_when: "operator answers; definition documented in raw note"
```

## Module M-AC2 — Layer 1 Prevention

```yaml
module_id: M-AC2
title: "Layer 1 Prevention: implement auto-compact-disable across 4 sub-layers"
priority: P0
estimate_hours: 4-6
parent_epic: E-AUTO-COMPACT-DEFENSE
sfif_stage: implement
mission: "Operationalize Fire 107 Layer 1 spec via brain + harness + env + hook-block sub-layers"
blocked_by: [M-AC1]
done_when:
  - sub-layer 1A wired (CLAUDE.md + AGENTS.md Hard Rule 16)
  - sub-layer 1B wired (settings.json config-key disable)
  - sub-layer 1C wired (env var disable)
  - sub-layer 1D wired (PreCompact-hook block, IF Q3 confirms supported)
  - verification: trigger context-edge scenario; auto-compact does NOT fire
tasks:
  - T-AC2-1
  - T-AC2-2
  - T-AC2-3
  - T-AC2-4

T-AC2-1:
  subject: "Sub-layer 1A — Add Hard Rule 16 to CLAUDE.md + AGENTS.md"
  estimate_hours: 0.5
  method:
    - edit /opt/CLAUDE.md hot-path: add Hard Rule 16 (auto-compact disable + auto-dream policy)
    - edit /opt/AGENTS.md: cross-tool universal restatement
    - update .claude/rules/operating-principles.md: register policy
  deliverable: "Hard Rule 16 active in hot-path"
  done_when: "operator confirms; pipeline post 0 errors"

T-AC2-2:
  subject: "Sub-layer 1B — Settings.json config-key wiring"
  estimate_hours: 1
  method:
    - apply Q2 finding canonical disable key
    - edit /opt/.claude/settings.json
    - test: trigger context-edge; observe behavior
  deliverable: "settings.json updated; verification test passes"
  blocked_by: T-AC1-2

T-AC2-3:
  subject: "Sub-layer 1C — Env var wiring"
  estimate_hours: 0.5
  method:
    - apply Q2 finding canonical env var
    - update shell profile (~/.bashrc or wherever Claude Code is launched)
    - persist across sessions
  deliverable: "env var set; verification test passes"
  blocked_by: T-AC1-2

T-AC2-4:
  subject: "Sub-layer 1D — PreCompact-hook block (conditional on Q3)"
  estimate_hours: 1.5
  method:
    - IF Q3 = YES: author pre-compact-block.sh (exit 1 unless REASON set)
    - IF Q3 = NO: skip; document not-applicable
    - wire as additional PreCompact hook composing with Fire 105 spec
    - test: trigger PreCompact; verify block
  deliverable: "Layer 1D status + verification"
  blocked_by: T-AC1-3
```

## Module M-AC3 — Layer 2 + 3 Mitigation + Enforcement

```yaml
module_id: M-AC3
title: "Layer 2 + Layer 3: wire PreCompact handoff + PreToolUse-blocker hooks"
priority: P0
estimate_hours: 6-8
parent_epic: E-AUTO-COMPACT-DEFENSE
sfif_stage: implement
mission: "Operationalize Fires 105 + 106 specs; wire bidirectional handoff + enforcement"
blocked_by: [M-AC1]  # need investigation findings before wiring
done_when:
  - Fire 105 PreCompact hook implemented + wired in settings.json
  - Fire 106 PreToolUse-blocker hook implemented + wired in settings.json
  - sentinel state-file lifecycle verified end-to-end
  - manual /compact trigger: handoff written + blocker enforced + acknowledge unblocks
  - Fire 102 incident reproducibility check: cannot reproduce
tasks:
  - T-AC3-1
  - T-AC3-2
  - T-AC3-3
  - T-AC3-4

T-AC3-1:
  subject: "Implement Fire 105 PreCompact hook"
  estimate_hours: 2
  method:
    - author /opt/.claude/hooks/pre-compact.sh per Fire 105 Python template
    - 11 sections per spec
    - error-handling per spec
  deliverable: "hook script + executable + initial smoke test"
  done_when: "manual invocation produces handoff doc + sentinel"

T-AC3-2:
  subject: "Implement Fire 106 PreToolUse-blocker hook"
  estimate_hours: 2
  method:
    - author /opt/.claude/hooks/pre-tool-post-compact-block.sh per Fire 106 Python template
    - REGATHER_ALLOWLIST + bypass-via-REASON + audit-log
  deliverable: "hook script + executable"
  done_when: "synthetic test: sentinel present → blocks; sentinel absent → allows"

T-AC3-3:
  subject: "Wire both hooks in /opt/.claude/settings.json"
  estimate_hours: 0.5
  method:
    - add PreCompact entry (Fire 105)
    - add PreToolUse entry with broad matcher (Fire 106)
    - validate JSON
  deliverable: "settings.json updated; hooks fire on event"
  blocked_by: [T-AC3-1, T-AC3-2]

T-AC3-4:
  subject: "End-to-end integration test"
  estimate_hours: 1.5-3
  method:
    - trigger manual /compact
    - verify handoff doc written
    - verify sentinel created
    - simulate post-compact session
    - verify first non-regather tool call blocked
    - verify regather sequence allowed
    - verify acknowledge removes sentinel
    - verify pre-compact pending action allowed post-acknowledge
  deliverable: "integration test PASS; state-file lifecycle confirmed"
  blocked_by: T-AC3-3
```

## Module M-AC4 — Documentation + Verification + Propagation

```yaml
module_id: M-AC4
title: "Documentation + Verification + Sister-Project Propagation"
priority: P1
estimate_hours: 4-6
parent_epic: E-AUTO-COMPACT-DEFENSE
sfif_stage: test
mission: "Close the Epic: documentation refresh + 7-day-no-incident verification + sister-project propagation"
blocked_by: [M-AC2, M-AC3]
done_when:
  - decision-package v5 published with Epic closure
  - Fire 103 audit re-run on full body; impl-spec #10 confirmed Tier 4
  - 7-day-no-incident period observed (auto-compact has not fired)
  - sister-project propagation pattern applied to /root + OpenArms + OpenFleet + AICP + devops-control-plane
tasks:
  - T-AC4-1
  - T-AC4-2
  - T-AC4-3

T-AC4-1:
  subject: "Decision-package v5 publication"
  estimate_hours: 1
  method:
    - author wiki/log/2026-05-XX-decision-package-refresh-v5-Nnn-pieces-auto-compact-defense-closed.md
    - update Fire 102 worked-example: "structurally prevented post-Fire-107"
    - update Fire 103 audit: tier-distribution shift
  deliverable: "v5 published; pipeline post 0 errors"

T-AC4-2:
  subject: "7-day-no-incident verification"
  estimate_hours: 0.5 (passive observation; setup only)
  method:
    - mark calendar +7 days from M-AC3 completion
    - no specific action; observe whether auto-compact fires
    - if fires: log incident; reopen Epic
  deliverable: "7-day clean state confirmed OR incident logged"

T-AC4-3:
  subject: "Sister-project propagation"
  estimate_hours: 2.5-4.5
  method:
    - apply Fires 105+106+107 specs to /root + OpenArms + OpenFleet + AICP + devops-control-plane
    - per-project adaptation (each may have different conventions)
    - cross-reference at second-brain
  deliverable: "5 sister projects with auto-compact-defense applied"
  blocked_by: [T-AC4-1, T-AC4-2]
```

## Estimate summary

| Module | Hours | Priority | Stage | Done-when (high-level) |
|---|---|---|---|---|
| M-AC1 Investigation | 4-6 | P0 | document | 4 questions resolved |
| M-AC2 Layer 1 Prevention | 4-6 | P0 | implement | 4 sub-layers wired + verified |
| M-AC3 Layer 2+3 Mitigation+Enforcement | 6-8 | P0 | implement | hooks wired + integration test PASS |
| M-AC4 Documentation+Verification+Propagation | 4-6 | P1 | test | v5 + 7-day verify + 5-project propagation |
| **Epic total** | **18-26** | **P0** | **multi-stage** | **all modules done + Epic closure verified** |

## Dependencies

```
M-AC1 (Investigation) — no blockers; can start immediately upon operator-confirmation
  ↓ blocks
M-AC2 (Layer 1 Prevention) ← also blocks
M-AC3 (Layer 2+3 Mitigation+Enforcement) ← also blocks
  ↓ both block
M-AC4 (Documentation+Verification+Propagation)

Critical path: M-AC1 → M-AC2 (or M-AC3) → M-AC4
Critical-path estimate: 14-20 hours (M-AC1 + max(M-AC2, M-AC3) + M-AC4)
```

M-AC2 + M-AC3 can run in parallel after M-AC1 completes.

## Composability with body's existing infrastructure

| Component | Composability |
|---|---|
| /opt task tracker (#25-29) | Tasks #25-29 map to M-AC1 + sub-tasks; this decomposition refines + extends |
| Fire 97 backlog-decomposition pattern | This Fire 108 IS application of Fire 97 methodology |
| /root iterative-evolution-pathway Dimension 1 | Hierarchy decision per scope-and-time-horizon (Epic = multi-week; Module = days; Task = hours) |
| Methodology engine (5 stages × ALLOWED/FORBIDDEN) | Each Module declares stage; tasks honor stage-gate boundaries |
| Decision-package v4 (Fire 104) | This decomposition operationalizes v4's Option E recommendation |
| Composite-compliance metric (Fire 85) | Epic completion tracks via tier-elevation per Fire 103 audit |
| Sister-project propagation pattern (Fire 76+) | M-AC4 explicitly invokes propagation post-tier-3 |

## Open questions for operator-confirmation

```
Q1: Epic placement — within v2.0 milestone (current) OR new v2.1?
  Argument for v2.0: aligns with operator's pre-compact pivot directive; 
                     completes second-brain self-protection
  Argument for v2.1: this is post-100-piece-milestone work; v2.0 was pre-defined

Q2: Module M-AC4 scope — include sister-project propagation OR separate Epic?
  Argument for include: defense-in-depth pattern propagation is natural Epic-end
  Argument for separate: 5-project propagation is itself substantial work

Q3: Investigation method for M-AC1 — claude-code-guide subagent OR operator-direct?
  Argument for subagent: fast; deterministic methodology
  Argument for operator-direct: operator-empirical knowledge of auto-dream + harness

Q4: Authoring backlog pages at /opt — operator-empirical OR agent-DRAFT?
  Default: agent-DRAFT per SB-095 + operator promotes via per-file confirmation

Q5: Cron / loop continuation during M-AC1 investigation — pause OR continue parallel?
  Argument for pause: investigation is operator-territory; loop may distract
  Argument for continue: body authoring continues independent of M-AC1 work

Q6: Scope-creep guard — limit auto-compact decomposition OR extend to other Tier-2 pieces?
  Argument for limit: operator's specific 2026-05-08 priority is auto-compact only
  Argument for extend: Fire 103 audit revealed ~53% Tier 1; same decomposition method applies
```

## Recommended operator next-action

Per /loop directive *"sdlc and methodology and workflow respect is utmost important"*:

```
RECOMMENDATION:
  1. Operator confirms Epic + 4-Module decomposition (this fire)
  2. Operator picks parallel-vs-pause for /loop continuation during M-AC1
  3. M-AC1 investigation kicks off (Tasks T-AC1-1..4)
  4. Findings landed; operator confirms findings
  5. M-AC2 + M-AC3 in parallel (Tasks T-AC2-* + T-AC3-*)
  6. M-AC4 follows; Epic closure
  7. Decision-package v5 publishes; Fire 102 incident structurally-impossible

Critical-path: 14-20 hours of focused work
Estimated calendar: 1-2 weeks if operator-attention available daily
                    3-4 weeks if part-time
```

## Closing framing

Per Fire 97 pattern: complex multi-day priorities decompose into Epic+Module+Task hierarchy. This Fire 108 demonstrates that pattern in action for the auto-compact priority surfaced 2026-05-08. Per /loop directive *"30 pieces if not 70-80 pieces and changes... no lazyness. no hack or quickfix"*: the 18-26 hour estimate reflects operator's "no rush" framing — this is structural-fix work, not patching.

**The agent stands by per /loop directive. Cron continues at 90s cadence. Operator-confirmation awaited on the 6 open questions above.**

## Sources

- Backlog-decomposition pattern (Fire 97): `wiki/log/2026-05-08-backlog-decomposition-proposal-runtime-control-diagnostic-discipline-epic-modules-tasks.md`
- Auto-compact priority directive: `raw/notes/2026-05-08-auto-compact-detection-failure-and-auto-compact-must-be-disabled-priority.md`
- Fire 105 PreCompact spec: `wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md`
- Fire 106 PreToolUse-blocker spec: `wiki/patterns/01_drafts/post-compact-pretooluse-blocker-implementation-spec-tier-4-enforcement-for-impl-spec-10.md`
- Fire 107 auto-compact-disable spec: `wiki/patterns/01_drafts/auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth.md`
- Fire 103 4-tier audit method: `wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md`
- Decision-package v4 (Fire 104): `wiki/log/2026-05-08-ready-for-review-decision-package-refresh-v4-103-pieces-post-compact-recovery-tier-audit-integrated.md`

## Tags

[backlog-decomposition, auto-compact-priority, epic-module-task, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-108]

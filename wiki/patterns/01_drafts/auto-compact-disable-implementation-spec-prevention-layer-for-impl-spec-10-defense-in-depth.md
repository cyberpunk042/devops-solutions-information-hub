---
title: "Auto-Compact Disable Implementation-Spec — Prevention Layer for Impl-Spec #10 Defense-in-Depth"
type: pattern
domain: agent-config
status: synthesized
confidence: medium
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: auto-compact-detection-failure-priority
    type: file
    file: raw/notes/2026-05-08-auto-compact-detection-failure-and-auto-compact-must-be-disabled-priority.md
    description: "PRIMARY operator directive (sacrosanct verbatim 2026-05-08): 'make sure auto-compact is off always. only auto-dream can be enabled' — this spec operationalizes that policy"
  - id: pre-compact-handoff-hook-impl-spec
    type: wiki
    file: wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md
    description: "Sibling (Fire 105) — Layer 2 mitigation when compaction DOES occur; this Fire 107 spec is Layer 1 prevention"
  - id: post-compact-pretooluse-blocker-impl-spec
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-pretooluse-blocker-implementation-spec-tier-4-enforcement-for-impl-spec-10.md
    description: "Sibling (Fire 106) — Layer 3 enforcement when post-compact session resumes; this spec is Layer 1 prevention (defense-in-depth)"
  - id: documentation-implementation-asymmetry-pattern
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "PRIMARY parent (Fire 103) — 4-tier audit method; this spec elevates auto-compact-disable from Tier 0 (no policy) to Tier 4 (policy + implementation + enforcement)"
  - id: worked-example-4-real-session-failure
    type: wiki
    file: wiki/log/2026-05-08-worked-example-4-post-compact-detection-failure-real-session-empirical-evidence-impl-spec-10-stress-test.md
    description: "Empirical evidence (Fire 102) — auto-compact triggered at 5% remaining, operator-surprise; Layer 1 prevention prevents recurrence"
  - id: opt-claude-settings-json
    type: file
    file: .claude/settings.json
    description: "Existing the second-brain settings — investigation target for auto-compact-disable mechanism (location TBD)"
tags: [implementation-spec, auto-compact-disable, prevention-layer, defense-in-depth, opt-second-brain, harness-policy, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-107]
---

# Auto-Compact Disable Implementation-Spec — Prevention Layer for Impl-Spec #10 Defense-in-Depth

## Summary

Per operator directive 2026-05-08 (sacrosanct verbatim, post-compact incident): *"make sure auto-compact is off always. only auto-dream can be enabled"*. Per Fire 102 worked-example: auto-compact triggered at 5% remaining without operator-confirmation gate — fire-102 incident. Fires 105 + 106 specs handle compaction WHEN IT OCCURS (mitigation + enforcement). This Fire 107 spec handles **PREVENTION** — preventing auto-compact from firing at all. Defense-in-depth: Layer 1 prevention (this spec) + Layer 2 mitigation (Fire 105 handoff doc) + Layer 3 enforcement (Fire 106 PreToolUse blocker). Investigation required: locate the actual mechanism Claude Code uses for auto-compact (settings key, env var, harness-default policy). Confidence: **medium** — spec authors policy + 4-layer disable strategy + investigation requirements; per-layer implementation depends on harness-specifics not currently empirically known to agent.

## Pattern Description

### Defense-in-depth — 3-layer model

```
LAYER 1 — PREVENTION (this Fire 107 spec):
  Auto-compact NEVER fires
  Manual /compact requires explicit operator invocation
  Operator-surprise impossible
  Failure mode: harness-default behavior overrides config (TBD per investigation)

LAYER 2 — MITIGATION (Fire 105 spec):
  IF compaction does occur, capture state to handoff doc
  Sentinel dropped for post-compact agent
  Failure mode: hook fails to fire OR runs out of time

LAYER 3 — ENFORCEMENT (Fire 106 spec):
  IF post-compact agent resumes, block first non-regather tool call
  Sentinel-driven structural prevention
  Failure mode: agent uses bypass mechanism without operator-grant (audit-logged)

Combined: Layer 1 fails → Layer 2 catches → Layer 3 catches → operator catches
Each layer's failure is independent; defense-in-depth maximizes prevention coverage.
```

### Investigation requirements (Task #25 territory)

Before this spec can be fully implemented, the following empirical data MUST be captured:

```yaml
investigation_questions:
  Q1_threshold_source:
    question: "What sets the 5% auto-compact threshold? Harness default? settings.json? env var?"
    investigation_method:
      - check Claude Code official docs for auto-compact configuration
      - grep .claude/settings.json + .claude/settings.local.json for compact-related keys
      - check ~/.claude/settings.json for user-level auto-compact config
      - check env vars: CLAUDE_AUTO_COMPACT, ANTHROPIC_*, etc.
      - observe Claude Code version (claude --version) + check changelog for auto-compact behavior
    deliverable: "documented mechanism + location of auto-compact threshold"
  
  Q2_disable_mechanism:
    question: "What is the canonical way to disable auto-compact in Claude Code?"
    investigation_method:
      - claude-code-guide subagent dispatch for empirical answer
      - check .claude/settings schema for auto-compact-related fields
      - test: set candidate config; trigger 5% scenario; observe behavior
    deliverable: "canonical disable mechanism (config key + value)"
  
  Q3_precompact_hook_blocking:
    question: "Can a PreCompact hook with exit 1 PREVENT compaction (vs allowing then capturing)?"
    investigation_method:
      - check Claude Code hook contract for PreCompact event
      - search documentation for blocking semantics on PreCompact
      - test: PreCompact hook with exit 1; observe if compaction proceeds
    deliverable: "yes/no + mechanism semantics"
  
  Q4_auto_dream_definition:
    question: "What is 'auto-dream' (operator-known term)?"
    investigation_method:
      - surface as question to operator (per Fire 99 question-registry)
      - alternate: grep operator's prior raw notes for term
      - alternate: claude-code-guide research for analogous concepts
    deliverable: "operator-empirical definition + scope of allowed auto-* mechanisms"
```

These investigations are pre-requisite for Layer 1 implementation. This spec PROVIDES the structural framework + investigation framework; the actual disable-key resolution depends on findings.

### Layer 1 disable strategy (4 sub-layers)

```
SUB-LAYER 1A — BRAIN LAYER (CLAUDE.md hot-path Hard Rule):
  Add Hard Rule 16: "Auto-compact MUST be disabled. Manual /compact only.
                     Auto-dream is the only allowed auto-* mechanism."
  Effect: agent reads hot-path; will not auto-trigger /compact;
          will warn operator if context approaches limit
  Tier (per Fire 103 audit): Tier 1 (declared only) → Tier 3 if hook
                              monitors agent compliance
  Limitation: agent doesn't trigger auto-compact (harness does); declarative only

SUB-LAYER 1B — HARNESS LAYER (.claude/settings.json):
  Configure auto-compact to OFF via canonical config key (TBD per Q2 investigation)
  Possible keys: "autoCompact: false", "compact: { auto: false }",
                 "permissions.autoCompact: false", or similar
  Effect: harness checks config + suppresses auto-compact firing
  Tier: Tier 4 if config-key-respected (full enforcement at harness layer)
  Limitation: depends on Q2 investigation finding canonical disable mechanism

SUB-LAYER 1C — ENV-VAR LAYER (shell environment):
  Set environment variable to suppress auto-compact (TBD per Q2 investigation)
  Possible vars: CLAUDE_NO_AUTO_COMPACT=1, ANTHROPIC_AUTO_COMPACT=disable
  Effect: harness checks env + suppresses auto-compact firing
  Tier: Tier 4 if env-var-respected
  Limitation: env-var must persist across sessions (ensure in shell profile)

SUB-LAYER 1D — PRECOMPACT-HOOK BLOCKING LAYER (last-resort prevention):
  IF Q3 investigation confirms PreCompact hook can block via exit 1:
    Author additional hook: pre-compact-block.sh exits 1 to PREVENT compaction
    With exception: REASON env var allows manual /compact through
  Effect: harness-default ignored; hook-layer takes over
  Tier: Tier 4
  Limitation: depends on Q3 investigation; may not be supported by Claude Code
```

### Combined Layer 1 implementation flow

```
PHASE 1: Investigation (Task #25 work)
  Sub-task 1.1: claude-code-guide subagent research
  Sub-task 1.2: .claude/settings.json + ~/.claude/settings.json grep
  Sub-task 1.3: env var inventory
  Sub-task 1.4: PreCompact-hook-blocking semantics
  Sub-task 1.5: auto-dream definition (Task #29)

PHASE 2: Layer 1A wiring (after Phase 1 complete)
  Edit CLAUDE.md hot-path: add Hard Rule 16
  Edit AGENTS.md: add Hard Rule 16 (cross-tool universal)
  Document policy in .claude/rules/operating-principles.md

PHASE 3: Layer 1B + 1C wiring (after Phase 1 reveals canonical mechanism)
  Edit settings.json: disable-config-key = false
  Edit shell profile: env var = disable-value
  Verify: try forcing context to low; observe whether auto-compact fires

PHASE 4: Layer 1D wiring (conditional on Phase 1 Q3 finding)
  IF PreCompact hook can block:
    Author pre-compact-block.sh (exit 1 unless REASON set)
    Wire as additional PreCompact hook (composes with Fire 105 spec)
  ELSE:
    Layer 1D not implementable; rely on 1A+1B+1C

PHASE 5: Verification
  Trigger context-edge scenario (verify no auto-compact)
  Trigger manual /compact (verify it still works for explicit operator-invocation)
  Trigger PreCompact (verify Fire 105 spec handoff still authored)
  Trigger PostCompact (verify Fire 106 spec blocker still enforces)

PHASE 6: Documentation closure
  Update Fire 102 worked-example with "structurally prevented post-Fire-107"
  Update Fire 103 audit: impl-spec #10 + auto-compact-disable now Tier 4
  Update Fire 104 decision-package v4 → v5 with Layer 1 closure
  Update CONTEXT.md: auto-compact-disable policy active
```

### Auto-dream definition surfacing (Task #29)

Per operator's verbatim: *"only auto-dream can be enabled"*. The term "auto-dream" is operator-known but not currently defined in the second-brain second-brain corpus. This spec surfaces it as a question per Fire 99 question-registry pattern (forward-anchored: /questions slash command not yet implemented):

```
QUESTION (audience: OPERATOR):
  Q-id: auto-dream-definition
  Q-text: "What is 'auto-dream'? Per operator directive 2026-05-08, this is the
           only auto-* mechanism allowed. Need operator-empirical definition + scope.
           Possible meanings:
             - Auto-summarization at session end?
             - Background-knowledge-synthesis?
             - Periodic reflection / consolidation?
             - Sister-project propagation?
             - Sleep / overnight processing?
           Operator-empirical answer determines this spec's scope-of-allowed-auto."
  Surfaced-at: Fire 107 (this spec)
  Path-to-resolution: surface in next operator-facing checkpoint
                       (Fire 99 question-registry slash command Tier 1 → Tier 4 dependent)
  Forward-anchored: until operator answers, "only auto-dream" interpreted
                    conservatively — NO auto-* mechanisms enabled in the second-brain brain
```

### Composability with Fires 105 + 106 (defense-in-depth)

| Layer | Fire | Mechanism | Failure Mode | Combined Effect |
|---|---|---|---|---|
| Layer 1 (Prevention) | **107 (this)** | Brain + harness + env + hook block | Harness-default overrides config | Auto-compact never fires (when fully implemented) |
| Layer 2 (Mitigation) | 105 | PreCompact hook authors handoff doc | Hook fails to fire | State captured for post-compact agent |
| Layer 3 (Enforcement) | 106 | PreToolUse blocker on first post-compact tool call | Bypass abused | Agent CANNOT skip regather without REASON |

If Layer 1 succeeds: Layers 2-3 are dormant (unused infrastructure for safety).
If Layer 1 fails (manual /compact OR harness-bypass): Layers 2-3 catch.
If Layers 1-2 both fail: Layer 3 still catches (any post-compact agent blocked).
All layers fail simultaneously: extremely unlikely; operator catches (per Fire 102 baseline).

### Anti-patterns this spec avoids

| Anti-pattern | Why bad | How avoided |
|---|---|---|
| Implement Layer 1 without investigation | Wrong key/var/hook; auto-compact still fires | Phase 1 investigation pre-requisite |
| Skip Layer 1; rely on Layers 2-3 | Compaction still occurs; lost time + context-switch overhead | Defense-in-depth philosophy |
| Implement Layer 1A only (declarative) | Agent reads brain but harness ignores | Layer 1B + 1C harness-level |
| Block manual /compact entirely | Operator's explicit /compact invocation broken | REASON bypass for explicit /compact |
| Conflate auto-compact with manual /compact | Disable everything; lose user-facing control | Differentiate auto vs manual; only auto disabled |
| Treat "auto-dream" as known | Wrong scope-of-allowed-auto; possible auto-conflation | Surface as Q to operator (Fire 99 pattern) |
| Apply spec without operator-confirmation | Could break working harness behavior | Operator-territory; confirm before wiring |

### Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_3_layer_model: passed via mock incident scenarios
    - investigation_questions_4_articulated: passed (Q1-Q4 documented above)
  pending:
    - Q1_threshold_source_resolved: pending — investigation
    - Q2_disable_mechanism_canonical: pending — investigation
    - Q3_precompact_blocking_semantics: pending — investigation
    - Q4_auto_dream_definition: pending — operator-empirical
    - layer_1A_brain_wiring: pending Q1-Q4 + operator-confirmation
    - layer_1B_settings_wiring: pending Q2 + operator-confirmation
    - layer_1C_envvar_wiring: pending Q2 + operator-confirmation
    - layer_1D_hook_wiring: pending Q3 + operator-confirmation
    - phase_5_verification_complete: pending all phases
    - operator_empirical_phase_5_acceptance: pending operator validates no-auto-compact behavior
  composite_compliance: auto-compact-disable-axis stress-test 0% (forward-anchored; Tasks #25 + #26 + #29 + this spec implementation)
```

## Path-to-Tier-4 (per Fire 103 audit method)

Currently auto-compact-disable is at **Tier 0** (no policy in body). This spec elevates it:

```
TIER 0 (no policy): CURRENT
  ↓ (this spec authoring)
TIER 1 (designed only): TARGET via this fire's authoring
  ↓ (operator confirms; agent or operator implements per phases)
TIER 2 (partial): if only some sub-layers implemented (e.g., 1A only)
  ↓ (full layer 1 implementation)
TIER 3 (implemented but not enforced): if all 4 sub-layers implemented but no
  verification gate ensures harness behavior matches
  ↓ (Phase 5 verification + Fire 106 enforcement composition)
TIER 4 (designed + implemented + enforced): combined Layer 1 + Layer 2 + Layer 3
  At this state: auto-compact structurally impossible; manual /compact still works
```

## When To Apply

Apply this auto-compact-disable spec when:
- Real-session evidence of auto-compact triggering unexpectedly (per Fire 102)
- Operator policy declared (per directive 2026-05-08)
- Defense-in-depth design preferred (Layer 1 + Layer 2 + Layer 3)
- Body of work depends on session continuity (auto-compact disrupts continuity)
- Sister-project propagation possible (Fire 105 + Fire 106 + this spec form a triplet)

## Instances

**Instance 1: This the second-brain second-brain (Tasks #25 + #26 + #29 target)**
- Current: auto-compact fired at 5% (Fire 102 evidence); the second-brain at Tier 0
- Apply: investigation phase first → Layer 1 implementation → verification
- Combined with Fires 105+106 wiring: full defense-in-depth coverage
- Tier-elevation: auto-compact-disable Tier 0 → Tier 4

**Instance 2: /root root-ghostproxy (sister-project parallel)**
- Current state: unknown auto-compact policy at /root
- Apply: this spec adapts to /root via bidirectional inheritance
- Investigation: same Q1-Q4 apply

**Instance 3: Sister projects (forward-anchored)**
- Per propagation-pattern: post-tier-3 deployment
- Each may need adaptation per project conventions
- Cross-project consistency: same auto-compact-disable policy expected

## When Not To

- Project explicitly wants auto-compact (e.g., long-running agent that benefits from auto-summary)
- Investigation cannot proceed (Q2 unknowable; canonical mechanism doesn't exist)
- Operator-explicit "advisory only; no harness-level disable"
- Harness layer not modifiable (e.g., managed Claude Code instance with locked config)

## Empirical Evidence

Per Fire 102 worked-example (2026-05-08): auto-compact fired at 5% remaining; operator surprise. Without Layer 1 prevention, recurrence very likely (per Fire 95 pattern-recurrence cluster). Per Fires 105 + 106: Layer 2 + Layer 3 mitigation/enforcement specced but not implemented. This Fire 107 completes the defense-in-depth triplet at the spec-level.

This spec is **medium confidence** (vs Fires 105+106 high confidence) because:
- Layer 1 implementation depends on investigation findings (Q1-Q4)
- Without empirical answer to Q2 (canonical disable mechanism), Layer 1B + 1C are placeholder
- Layer 1D depends on PreCompact-hook-blocking semantics (Q3) not currently confirmed
- Operator-empirical definition of "auto-dream" (Q4) determines scope

The spec PROVIDES the framework + investigation requirements + path-to-resolution. Implementation depends on operator confirmation + investigation completion.

## Auto-compact-disable triplet (Fires 105 + 106 + 107)

| Fire | Spec | Layer | Trigger | Action |
|---|---|---|---|---|
| 105 | PreCompact handoff hook | Layer 2 (mitigation) | PreCompact event | Author handoff doc + drop sentinel |
| 106 | PreToolUse-blocker | Layer 3 (enforcement) | First post-compact tool call | Block until regather + sentinel removed |
| **107** | **Auto-compact-disable** | **Layer 1 (prevention)** | **N/A — prevents trigger** | **Disable harness-auto-compact via 4 sub-layers** |

Combined wiring:
- Fire 107 prevents auto-compact firing (Layer 1)
- Fire 105 captures state if compaction does occur (Layer 2)
- Fire 106 enforces regather post-compact (Layer 3)
- Operator's catch (per Fire 102) is the final safety net

## Relationships

- COMPOSES WITH: Fire 105 PreCompact handoff hook spec (Layer 2 of triplet)
- COMPOSES WITH: Fire 106 PreToolUse-blocker spec (Layer 3 of triplet)

## Tags

[implementation-spec, auto-compact-disable, prevention-layer, defense-in-depth, opt-second-brain, harness-policy, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-107]

## Backlinks

[[Fire 105 PreCompact handoff hook spec (Layer 2 of triplet)]]
[[Fire 106 PreToolUse-blocker spec (Layer 3 of triplet)]]

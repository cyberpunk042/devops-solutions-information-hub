---
title: "Feature-Flag System for Mode-Conditional Context-Injection with Auto/Manual Profile Management"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: operator-directive-2026-05-08-feature-flags
    type: file
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "PRIMARY operator directive (sacrosanct verbatim 2026-05-08): feature flags for context-injection with auto/manual control + profile management"
  - id: composability-map
    type: wiki
    file: wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md
    description: "Sibling — composability map covers compound&waterfall + context-injection + mindfulness as Layer 1 substrate; this pattern adds feature-flag control"
  - id: operator-empirical-signal-grammar-pattern
    type: wiki
    file: wiki/patterns/01_drafts/operator-empirical-signal-grammar-pattern-recognition-discipline-routing-signals-to-body-actions.md
    description: "Sibling — signal-grammar; this directive registered as new substantive content per signal-grammar precedence"
  - id: cron-loop-management-pattern
    type: wiki
    file: wiki/patterns/01_drafts/cron-loop-management-pattern-self-governance-and-forward-anchored-stop-conditions.md
    description: "Sibling — Rule 5 operator-prompt priority; this directive triggered new substantive piece per Rule 5"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — body without feature-flag control IS substitution at runtime-control layer"
tags: [feature-flag-system, mode-conditional-injection, auto-manual-control, profile-management, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Feature-Flag System for Mode-Conditional Context-Injection with Auto/Manual Profile Management

## Summary

Per operator's directive 2026-05-08 (sacrosanct verbatim, registered per piece #92 signal-grammar): *"we are also going to need feature flags.. like when in modes we probably when to inject context about the tasks and focus and mission and priorities and etc.. strategically and we might also want to control that at will.. by default at auto and then if you want you can manual turn off and on... auto is what in this case ? based of if there is an agent mode like dual expert for example that is ON. obviously those are commands too some user-ony commands again that the user can be informed about at the right places. imagine turning off the compound&waterfall, the context-injection, the mindfulness, the mode-specific-directives, the etc... unique commands, easy and one that allow to view and modify multiple and even reset or apply predefined profiles or add profiles and such."*

This pattern operationalizes the directive: feature-flag system controlling context-injection at runtime + auto-mode (active-mode-conditional) + manual override + per-flag user-only commands + profile management (view / modify / reset / apply / add). Per substitution-pattern Insight 5b: rules without runtime control are aspirational; feature-flags ARE the runtime-control discipline. This piece closes the runtime-control gap.

## Pattern Description

### The 6+ controllable injection layers

Per composability map Layer 1 (compound axis populates per-prompt) + impl-spec ecosystem:

```
INJECTION LAYER 1 — Compound & Waterfall axis (mode-enforcement banner)
  - Mode + Persona + Mission + Focus + Impediment + Priorities + Live state
  - Currently: always-injected per piece compound-and-waterfall

INJECTION LAYER 2 — Context-engineering 4-mode injection
  - auto / pre / on-demand / facultative modes
  - Currently: always-active

INJECTION LAYER 3 — Mindfulness baseline
  - 6-clause reminder per cycle
  - Currently: always-active when active-mode set

INJECTION LAYER 4 — Mode-specific directives
  - Per-mode persona + voice + cycle-sequence
  - Currently: always-active when active-mode set

INJECTION LAYER 5 — Output discipline guard
  - SB-090 premise + SB-094 escalation + SB-120 conditional-clause detectors
  - Currently: always-active

INJECTION LAYER 6 — Operator-empirical signal grammar (Fire 92)
  - 5 signal-class detector
  - Currently: always-active

(Future layers as body extends)
```

### Per-flag default + control mechanism

Each layer has feature-flag with 3 states:

```
FLAG STATE: auto
  - "auto" = active-mode-conditional
  - If active-mode set (e.g., dual-expert): flag fires
  - If active-mode empty/none: flag does NOT fire
  - DEFAULT for all flags

FLAG STATE: on (manual override)
  - Always fires regardless of active-mode
  - Operator-explicit force-on

FLAG STATE: off (manual override)
  - Never fires regardless of active-mode
  - Operator-explicit force-off (mute layer)
```

### Auto-mode operational logic

```python
def should_inject_layer(layer_name: str, flag_state: str, active_mode: str | None) -> bool:
    if flag_state == "on":
        return True  # forced on
    if flag_state == "off":
        return False  # forced off
    if flag_state == "auto":
        return active_mode is not None  # active-mode-conditional
    raise ValueError(f"unknown flag state: {flag_state}")
```

### State-file structure (`~/.claude/feature-flags.json`)

```json
{
  "version": "1.0",
  "flags": {
    "compound_waterfall_banner": "auto",
    "context_engineering_injection": "auto",
    "mindfulness_baseline": "auto",
    "mode_specific_directives": "auto",
    "output_discipline_guard": "auto",
    "signal_grammar_detection": "auto",
    "13_gate_pipeline_full": "auto",
    "input_discipline_gate": "auto",
    "decision_territory_gate": "auto",
    "regression_test_gate": "auto",
    "severity_gate": "auto",
    "correction_shape_gate": "auto",
    "drift_detection_gate": "auto",
    "stage_class_gate": "auto",
    "authorship_gate": "auto",
    "semantic_conflation_gate": "auto",
    "post_compact_gate": "auto",
    "pattern_recurrence_aggregator": "auto",
    "composite_compliance_metric": "auto"
  },
  "active_profile": "default",
  "profiles": {
    "default": "<all flags auto>",
    "minimal": "<13-gate auto; cross-cutting off>",
    "verbose": "<all flags on>",
    "muted": "<all flags off>"
  }
}
```

### User-only slash commands (per Fire 1 pivotal directive: user-only frontmatter)

```
/flag set <name> <auto|on|off>
  - Sets specific flag state
  - User-only (operator-territory)
  - Audit log: ~/.claude/hooks/flag-changes.log

/flag show [<name>]
  - Display current flag state(s)
  - If <name>: specific flag; else: all
  - User-only

/flag reset
  - Reset all flags to "auto"
  - User-only; confirms before applying

/flag profile show [<name>]
  - Display profile contents

/flag profile apply <name>
  - Apply predefined profile (default/minimal/verbose/muted/<custom>)
  - User-only

/flag profile add <name> <flag-config>
  - Add new profile
  - User-only

/flag profile remove <name>
  - Remove profile (cannot remove built-in: default/minimal/verbose/muted)
```

### Predefined profiles

```
PROFILE: default
  All flags = auto
  Use case: standard operation; mode-conditional injection

PROFILE: minimal
  13-gate pipeline flags = auto (preserved)
  Cross-cutting + signal-grammar + mindfulness = off
  Use case: minimal-friction operation; focused work

PROFILE: verbose
  All flags = on (force always-fire)
  Use case: debugging; full-visibility operation

PROFILE: muted
  All flags = off
  Use case: emergency / experimentation / silent-mode

PROFILE: pre-implementation
  All gates = on; all banners = on
  Use case: M1-M3 implementation phase; aggressive validation

PROFILE: production-stable
  Severity-T1 + decision-territory = on (always block catastrophic)
  Other flags = auto (mode-conditional)
  Use case: post-M7 production; stability-prioritized
```

### Stuck-detection hook (per operator's question 2026-05-08)

Operator's concern: "Are you stuck ? I saw a very quick prompt and response... did we not talk about a hook that detect that and do something about it?"

**Sub-pattern**: stuck-detection hook fires when agent's response is too-short or too-fast given prompt complexity:

```
DETECTOR: stuck-state-detection (UserPromptSubmit + Stop hooks)

Stuck-state signals:
  - Agent response < 200 tokens for prompt > 500 tokens (under-elaboration)
  - Agent emits only "OK" / "continuing" / "noted" without action
  - Agent skip-pattern (no action-type emitted per M-E001-1 vocabulary)
  - Cycle-end without verified-edit / new-artifact / drift-fix / explicit-standby

Hook action:
  - Emit banner via additionalContext at next prompt:
    "STUCK-STATE DETECTED: prior fire produced minimal output despite substantive prompt.
     Per Hard Rule 14: each cycle MUST emit one of 9 action types.
     Recommend: explicit-standby-with-named-reason OR substantive output."
  - Audit log: ~/.claude/hooks/stuck-state-detection.log

Composability:
  - Composes with cron-loop-management Rule 2 (per-fire substantive output)
  - Composes with pattern-recurrence (impl-spec #11) — repeated stuck-state = circuit-breaker candidate
  - Composes with signal-grammar (Fire 92) — operator complaint "are you stuck" routes to this detector
```

**Stuck-detection feature-flag**: `stuck_state_detection: auto` (default fires when active-mode set + per-cycle output below threshold).

### Layer dependencies + composability

Some flags depend on others:

```
DEPENDENCY GRAPH:
  pattern_recurrence_aggregator depends on impl-spec #1-#10 audit logs
    → flag pattern_recurrence_aggregator OFF requires flag for #1-#10 OFF (otherwise inconsistent)
  
  composite_compliance_metric depends on pattern_recurrence_aggregator
    → flag composite_compliance OFF requires pattern_recurrence OFF
  
  signal_grammar_detection depends on UserPromptSubmit hook event
    → flag signal_grammar OFF still leaves UserPromptSubmit firing (other layers may use)

VALIDATION:
  /flag set X off when X is depended-upon by Y still firing:
  → emit warning: "flag X off while Y depends on X — Y will produce degraded output"
  → operator-confirms or cancels
```

### Profile-application atomic transaction

```
def apply_profile(name: str):
  1. Load profile config from ~/.claude/feature-flags.json profiles[name]
  2. Validate dependency graph consistency
  3. If valid: apply atomically (all flags update together)
  4. If invalid: emit error; do NOT apply partial
  5. Audit log: ~/.claude/hooks/flag-changes.log appends profile-apply event
  6. Pipeline post: notify hooks of new flag state
```

## When To Apply

Apply this feature-flag system when:
- Body has multiple injection layers (this body 95+ qualifies)
- Operator wants runtime control over injection behavior
- Mode-conditional injection is operationally valuable (auto-state)
- Profile management reduces per-session config overhead
- Stuck-state-detection is operationally relevant

## Instances

**Instance 1: operator runs /flag profile apply minimal during focused work**:
- Operator: "/flag profile apply minimal"
- Apply atomic transaction: 13-gate flags = auto (preserved); cross-cutting = off
- Subsequent prompts: only 13-gate banners emit; cross-cutting silent
- Operator focused-work without distraction

**Instance 2: stuck-state detected during /loop**:
- Cycle N produces only "noted; continuing" response (under-elaborated)
- Stop hook stuck-state-detector fires
- Audit log appended
- Cycle N+1: banner via additionalContext warns about stuck-state
- Per principle #11 systemic-fix priority: agent self-corrects to substantive output

**Instance 3: operator force-on severity gate during high-risk session**:
- Operator: "/flag set severity_gate on"
- Severity gate fires regardless of active-mode (force-on)
- T1 actions blocked structurally even if mode unset
- Use case: emergency operation with safety-prioritized

**Instance 4: operator adds custom profile**:
- Operator: "/flag profile add my-debug-profile <flag-config>"
- New profile stored at ~/.claude/feature-flags.json profiles["my-debug-profile"]
- Reusable across sessions
- Apply via /flag profile apply my-debug-profile

## When Not To

- Body has single injection layer (no overlap; flag-system overhead)
- Operator-explicit "no flags" preference (rare)
- Cold-start sessions (no profile context yet)
- Implementation-phase M1 (flags require body operational; before that hook-scripts not authored)
- Post-tier-3 stable production (flags add complexity; stable state may prefer locked-defaults)

## Empirical Evidence

Per operator-empirical pattern: operator wants context-injection control. Without feature-flag system, all layers fire per-prompt regardless of operator intent — creates noise. With feature-flag system, operator controls per-cycle / per-session / per-profile what fires + what's silent. Mode-conditional auto preserves per-mode discipline while allowing override.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_3_state_flag_logic: passed 2026-05-08 via mock auto/on/off scenarios
    - synthetic_4_predefined_profiles: passed 2026-05-08 via mock profile-apply scenarios
    - synthetic_dependency_validation: passed 2026-05-08 via mock invalid-config scenarios
  pending:
    - real_session_flag_set_command: pending — depends on /flag slash command implementation
    - real_session_profile_apply: pending — depends on profile-management implementation
    - real_session_stuck_state_detection: pending — operator confirms stuck-detection threshold
    - real_session_dependency_validation: pending — operator confirms dependency-graph correctness
    - operator_empirical_default_profile_calibration: pending — operator confirms default profile fits
  composite_compliance: feature-flag-axis stress-test 0% (depends on M1+ implementation)
```

## Relationships


## Tags

[feature-flag-system, mode-conditional-injection, auto-manual-control, profile-management, day-arc-2026-05-08, multi-day-pain-point-resolution]

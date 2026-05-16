---
title: "Sister-Project Propagation Spec for Auto-Compact Triplet — 5-Projects Adaptation Matrix"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: sister-project-propagation-pattern-fire-76
    type: wiki
    file: wiki/patterns/01_drafts/sister-project-propagation-pattern-from-second-brain-to-5-project-ecosystem.md
    description: "PRIMARY parent (Fire 76+) — propagation-pattern methodology; this Fire 113 applies it to specific triplet"
  - id: pre-compact-handoff-hook-impl-spec-fire-105
    type: wiki
    file: wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md
    description: "PRIMARY parent (Fire 105) — Layer 2 mitigation spec; propagated per this fire's adaptation matrix"
  - id: post-compact-pretooluse-blocker-impl-spec-fire-106
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-pretooluse-blocker-implementation-spec-tier-4-enforcement-for-impl-spec-10.md
    description: "PRIMARY parent (Fire 106) — Layer 3 enforcement spec; propagated per this fire's adaptation matrix"
  - id: auto-compact-disable-impl-spec-fire-107
    type: wiki
    file: wiki/patterns/01_drafts/auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth.md
    description: "PRIMARY parent (Fire 107) — Layer 1 prevention spec; propagated per this fire's adaptation matrix"
  - id: auto-compact-priority-backlog-decomposition-fire-108
    type: wiki
    file: wiki/log/2026-05-08-auto-compact-priority-backlog-decomposition-epic-4-modules-15-tasks-fire-97-pattern-application.md
    description: "Sibling (Fire 108) — Module M-AC4-T-AC4-3 = sister-project propagation; this Fire 113 specs that task"
  - id: bidirectional-inheritance-rule
    type: file
    file: /root/.claude/rules/self-reference.md
    description: "Bidirectional inheritance pattern: $HOME source-of-truth for operational tooling; the second-brain inherits with adaptations; sister projects inherit from the second-brain OR /root depending on tooling-class"
  - id: opt-self-reference-rule
    type: file
    file: .claude/rules/self-reference.md
    description: "the second-brain self-reference rule — defines 5-project ecosystem (research-wiki + OpenArms + OpenFleet + AICP + devops-control-plane)"
tags: [sister-project-propagation, auto-compact-triplet, 5-projects-adaptation, fires-105-106-107, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-113]
---

# Sister-Project Propagation Spec for Auto-Compact Triplet — 5-Projects Adaptation Matrix

## Summary

Per Fire 76+ sister-project-propagation pattern: post-Tier-3 patterns propagate from the second-brain second-brain (or /root sister) to the 5-project ecosystem (research-wiki itself + OpenArms + OpenFleet + AICP + devops-control-plane). Per Fires 105+106+107: auto-compact triplet (Layer 1 prevention + Layer 2 mitigation + Layer 3 enforcement) is candidate for propagation post-implementation. This spec authors the **5-project adaptation matrix**: per-project deviations from the canonical the second-brain design, accounting for each project's identity (type/domain/scale/PM-level/trust-tier) + existing hook infrastructure + bidirectional-inheritance flow direction. Per /root self-reference rule + bidirectional-inheritance: operational tooling (hooks, slash-commands, state-files) flows $HOME source-of-truth → the second-brain + sisters inherit + adapt. Each project's adaptation honors the source pattern but accommodates project-specific conventions.

## Pattern Description

### 5-project ecosystem context

| Project | Path | Type | Phase | Existing PreCompact? | Existing PostCompact? | Auto-compact policy |
|---|---|---|---|---|---|---|
| **research-wiki** (this) | `$HOME/devops-solutions-information-hub/` | knowledge / second-brain | production | NO (Fire 102 evidence) | YES (post-compact.sh + post-orient.sh) | unknown — investigation per Task #25 |
| **root-ghostproxy** ($HOME) | `/root/` (or `$HOME`) | system / OS-setup | foundation | YES (per /root .claude/hooks/pre-compact.sh) | YES | unknown |
| **OpenArms** | `~/openarms/` | harness / agent-runtime | production | unknown | unknown | unknown |
| **OpenFleet** | `~/openfleet/` | fleet-orchestrator | production | unknown | unknown | unknown |
| **AICP** | `~/aicp/` (path TBD) | local-AI-inference | development | unknown | unknown | unknown |
| **devops-control-plane** | path TBD | infrastructure-governance | unknown | unknown | unknown | unknown |

Investigation pre-requisite: capture each project's existing hook state per the matrix above. Empirically grep each project's `.claude/settings.json` + `.claude/hooks/`.

### Per-project adaptation matrix

```
PROJECT 1: $HOME/devops-solutions-information-hub (research-wiki)
  Triplet status: Layer 2 partial (PostCompact only); Layer 3 absent; Layer 1 absent
  Adaptation: implement Fires 105+106+107 specs as canonical
    - Layer 1 (Fire 107): all 4 sub-layers per second-brain conventions
    - Layer 2 (Fire 105): Python hook with 11-section handoff doc; pipeline-status integration
    - Layer 3 (Fire 106): PreToolUse-blocker with second-brain REGATHER_ALLOWLIST
                          (gateway orient + view + pipeline status + raw notes)
  Effort estimate: 18-26h (per Fire 108 backlog-decomposition)
  This is the canonical reference implementation

PROJECT 2: /root or $HOME (root-ghostproxy)
  Triplet status: Layer 2 wired (per /root .claude/hooks/pre-compact.sh existence);
                   Layer 1 + Layer 3 status unknown (investigation needed)
  Adaptation: align /root pattern with the second-brain pattern via bidirectional inheritance
    - Per /root self-reference rule: $HOME source-of-truth for operational tooling
    - IF /root pre-compact.sh is more advanced: the second-brain inherits FROM /root
    - IF the second-brain pre-compact.sh is more advanced: /root may inherit FROM the second-brain
                                                (reverses normal direction; confirm operator)
    - Layer 3 PreToolUse-blocker: novel; /root may benefit from same pattern
    - Layer 1 prevention: same operator-policy applies
  Effort estimate: 6-12h (alignment work; may be partial)
  Critical: confirm bidirectional-inheritance direction via operator-empirical

PROJECT 3: OpenArms (~/openarms/)
  Triplet status: unknown (investigation needed)
  Adaptation: harness-engineering project; auto-compact may already be configured
    - PreCompact handoff: adapt 11-section template to harness-conventions
    - PostCompact: align with the second-brain's post-orient.sh pattern
    - PreToolUse-blocker: REGATHER_ALLOWLIST adapted to harness's tools
                          (e.g., agent-runtime entrypoints, runtime-state queries)
    - Layer 1: same prevention design
  Effort estimate: 8-15h (harness-specific adaptations)
  Cross-reference: the second-brain OpenArms identity profile
                   (wiki/ecosystem/project_profiles/openarms/identity-profile.md)

PROJECT 4: OpenFleet (~/openfleet/)
  Triplet status: unknown (investigation needed)
  Adaptation: fleet-orchestrator; multi-agent patterns
    - PreCompact handoff: needs FLEET-state capture (multi-agent state per project)
    - PostCompact: per-agent regather + fleet-aware
    - PreToolUse-blocker: fleet-specific REGATHER_ALLOWLIST (e.g., fleet-orient command)
    - Layer 1: same prevention design
  Effort estimate: 10-18h (fleet-multi-agent complexity)
  Cross-reference: the second-brain OpenFleet identity profile

PROJECT 5: AICP (path TBD)
  Triplet status: unknown
  Adaptation: local-AI-inference; possibly NO compaction (different agent model)
    - May not need full triplet; reduced spec
    - Layer 2 + Layer 3 may not apply
    - Layer 1 still relevant if any session-context-window
  Effort estimate: 2-4h (possibly minimal scope)
  Cross-reference: the second-brain AICP identity profile

PROJECT 6: devops-control-plane (path TBD)
  Triplet status: unknown
  Adaptation: infrastructure-governance; possibly different runtime
    - Investigation required
    - Tier-3 candidate after research-wiki + root-ghostproxy ship
  Effort estimate: TBD (investigation prerequisite)
```

### Adaptation dimensions per project

When propagating to a sister project, adapt these dimensions:

```
DIMENSION 1: Project identity (per Goldilocks profile)
  - type: knowledge / system / agent-runtime / fleet / inference / governance
  - phase: POC / development / production / decommissioning
  - scale: micro / small / medium / large
  - PM-level: L0-L4
  - trust-tier: operator-supervised / semi-autonomous / autonomous
  - SDLC profile: simplified / default / full
  
DIMENSION 2: Existing infrastructure
  - Hook stack (PreCompact / PostCompact / PreToolUse / etc. — what's wired)
  - Slash commands (orient analog / cycle analog / handoff analog)
  - State files (~/.claude/active-mode / active-focus / etc.)
  - Tools layer (project's tools/* modules)

DIMENSION 3: Conventions
  - Bash vs Python hook scripts (project preference)
  - Path conventions (the second-brain vs ~/ vs $HOME)
  - Command naming (gateway orient vs cycle vs orient)
  - Brain files (CLAUDE.md / AGENTS.md / CONTEXT.md / BOOTSTRAP.md presence)

DIMENSION 4: Operational risk profile
  - Production vs development (production = stricter enforcement)
  - Multi-user vs solo (multi-user = audit-log heavier)
  - High-security vs low-security (security = bypass logging mandatory)
  - Body-of-work persistence (knowledge project = persistent; experimental = ephemeral)

DIMENSION 5: Bidirectional-inheritance direction
  - Source-of-truth project for THIS particular pattern (operational tooling = $HOME usually;
                                                        knowledge content = the second-brain usually)
  - Inheriting projects' adaptation freedom (high vs low)
  - Cross-project propagation cadence (manual operator-coordinated vs automatic)
```

### Per-spec adaptation requirements

For Fire 105 (PreCompact handoff):
| Adaptation | Per-project guidance |
|---|---|
| Handoff doc location | `wiki/log/` for knowledge projects; `notes/` or `logs/` for code projects |
| Handoff doc sections | 11 canonical; remove sections N/A per project (e.g., AICP no body-of-work-state) |
| Pipeline-status invocation | Adapt to project's status command (gateway orient / fleet status / etc.) |
| State-file paths | Use project-specific Path conventions |
| Subprocess command | Use project's Python virtualenv path (.venv/bin/python varies) |

For Fire 106 (PreToolUse-blocker):
| Adaptation | Per-project guidance |
|---|---|
| Sentinel state-file path | `.claude/post-compact-recovery-required` (universal) |
| REGATHER_ALLOWLIST | Project-specific orient/cycle/state commands |
| Block message | Project-specific guidance + project-name in header |
| Bypass via REASON | Universal pattern (REASON env var) |
| Audit-log path | `.claude/hooks/post-compact-bypass.log` (universal) |

For Fire 107 (Layer 1 prevention):
| Adaptation | Per-project guidance |
|---|---|
| Hard Rule numbering | Per project's existing rules (HR 16 for the second-brain; varies for others) |
| Verbatim citation | Same operator directive (universal) |
| Sub-layer 1A text | Adapt to project's CLAUDE.md style (concise vs verbose) |
| Sub-layer 1B+1C+1D | Same harness investigation; possibly different finding per project |
| Auto-dream policy | Same operator policy (universal) |

### Propagation cadence + sequencing

```
PHASE 1: the second-brain research-wiki implementation (canonical reference)
  Per Fire 108 backlog-decomposition: M-AC1 through M-AC3 complete
  Tier 4 reached for Fires 105+106+107
  Pipeline post 0 errors
  7-day-no-incident verification (M-AC4)
  
PHASE 2: /root root-ghostproxy alignment
  Investigation: empirical state of /root pre-compact.sh
  Adaptation: per Dimension 1-5 matrix
  Verification per /root conventions
  Bidirectional-inheritance reconciliation (which side source-of-truth)
  
PHASE 3: OpenArms propagation
  Identity profile consultation: the second-brain wiki/ecosystem/project_profiles/openarms/
  Investigation: existing harness state
  Adaptation: harness-specific REGATHER_ALLOWLIST
  Verification per OpenArms test suite
  
PHASE 4: OpenFleet propagation
  Identity profile consultation
  Adaptation: fleet-multi-agent state-capture extensions
  Verification: fleet-coordination test scenarios
  
PHASE 5: AICP propagation
  Identity profile consultation
  Adaptation: possibly reduced triplet (Layer 1 only or N/A)
  Verification: AICP-specific session-context behavior
  
PHASE 6: devops-control-plane propagation
  Investigation: project state empirical
  Adaptation: infrastructure-governance specific
  Verification: governance-decision-flow tests

PHASE 7: Cross-project synchronization
  Per the second-brain's bidirectional-inheritance rule: any improvements found in propagation
                                              feed back to the second-brain (or /root) source
  Update Fire 105+106+107 specs with cross-project lessons learned
  Re-run Fire 103 audit on all 5 projects
```

### Composability with body's existing patterns

| Component | Composability |
|---|---|
| Fire 76+ propagation pattern | This Fire 113 IS the propagation methodology applied to specific triplet |
| Fires 105+106+107 specs | Source canonical for propagation |
| Fire 108 backlog-decomposition | M-AC4-T-AC4-3 = sister-project propagation; this Fire 113 specs that task |
| Bidirectional-inheritance rule | Honored: $HOME source-of-truth for operational tooling; the second-brain may have refinements that flow back |
| Multi-project ecosystem index pattern | Per-project identity profiles consulted |
| the second-brain sister-projects.yaml | Provides each project's metadata for adaptation |
| Fire 109 tier-elevation pathway | Each project's triplet implementation follows same T0→T4 path |

### Anti-patterns this spec avoids

| Anti-pattern | Why bad | How avoided |
|---|---|---|
| Copy-paste the second-brain hooks to other projects | Project conventions ignored; unsynchronized | Adaptation matrix per Dimension 1-5 |
| Skip identity-profile consultation | Wrong adaptation for project's phase/scale | Per-project guidance from the second-brain's profiles |
| Apply triplet to ALL projects equally | AICP may not need triplet | Per-project assessment phase |
| Bypass bidirectional-inheritance | /root and the second-brain diverge; no source-of-truth | Phase 2 alignment + Phase 7 sync |
| Sequential propagation only | Long calendar; high WIP | Phases 3-5 can run in parallel post-Phase-1 |
| Manual cross-project sync | Drift accumulates | Phase 7 explicit synchronization |
| Document propagation without operator-confirmation | Sister-project owners may dissent | Operator-territory boundary explicit per project |

## When To Apply

Apply this propagation spec when:
- the second-brain or /root reaches Tier 4 for the auto-compact triplet (Phase 1 complete)
- Sister-project propagation pattern (Fire 76+) is operator-confirmed
- Each sister project has identity-profile capturing project conventions
- Bidirectional-inheritance direction has been operator-confirmed for this pattern
- Cross-project synchronization cadence is established

## Instances

**Instance 1: the second-brain → /root alignment (Phase 2)**
- /root has existing pre-compact.sh; the second-brain now has Fire 105 spec
- Adaptation: align both per bidirectional-inheritance
- Critical decision: source-of-truth direction (operator-confirms)

**Instance 2: the second-brain → OpenArms (Phase 3)**
- Adaptation: harness-engineering specifics
- New REGATHER_ALLOWLIST: fleet-aware operations not applicable; agent-runtime ones replace

**Instance 3: the second-brain → OpenFleet (Phase 4)**
- Adaptation: fleet-multi-agent state capture
- Handoff doc extends to multi-agent state

**Instance 4: the second-brain → AICP (Phase 5)**
- Adaptation: possibly Layer 1 only (if AICP has no compaction)
- Cross-reference: AICP's identity profile guides scope

## When Not To

- the second-brain reference implementation not yet Tier 4 (premature propagation)
- Sister-project owners haven't confirmed adoption
- Each project has different operator (multi-tenancy concerns)
- Bidirectional-inheritance direction unresolved

## Empirical Evidence

Per Fire 76+ propagation pattern: methodology established for cross-project sync. Per Fires 105+106+107: triplet authored at the second-brain as candidate for propagation. Per the second-brain sister-projects.yaml + identity profiles: each project's metadata available for per-project adaptation. Per /root self-reference rule: bidirectional-inheritance direction depends on tooling-class (operational vs knowledge).

This spec demonstrates how the body's pattern-authoring at the second-brain can scale to the 5-project ecosystem via systematic adaptation. Without this spec: each sister-project would need ad-hoc adaptation; bidirectional-inheritance unmaintained; drift accumulates.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - 5_project_adaptation_matrix_authored: passed
    - 5_dimensions_per_project_articulated: passed
    - per_spec_adaptation_requirements: passed (per Fire 105/106/107)
    - 7_phase_propagation_cadence: passed
    - bidirectional_inheritance_direction_explicit: passed
  pending:
    - operator_empirical_5_project_state_investigation: pending
    - operator_empirical_per_project_adaptation_confirmation: pending
    - phase_1_canonical_reference_implementation: pending Tasks #25-29
    - cross_project_synchronization_phase_7: pending Phases 1-6 complete
    - identity_profile_consultation_per_project: pending Phase 1 + per-project investigation
  composite_compliance: sister-project-propagation-axis stress-test 0% (forward-anchored;
                       Phase 1 prerequisite)
```

## Operator-pending decisions

```
Q-FIRE-113-1: Propagation cadence
  Sequential (Phase 1 → 2 → 3 → 4 → 5 → 6 → 7) OR
  Parallel post-Phase-1 (Phases 2-6 in parallel; Phase 7 sync)

Q-FIRE-113-2: AICP scope
  Full triplet OR Layer 1 only OR N/A (no compaction in AICP context)

Q-FIRE-113-3: Bidirectional-inheritance for THIS pattern
  $HOME → the second-brain (default per operational tooling rule) OR
  the second-brain → $HOME (reverses; if the second-brain's spec is more comprehensive)

Q-FIRE-113-4: devops-control-plane investigation timing
  Phase 6 (last) OR earlier batch (depends on operator's investment in DCP)

Q-FIRE-113-5: Phase 7 synchronization mechanism
  Manual operator-coordinated OR semi-automated (cross-project diff tools) OR
  forward-anchored (post-tier-3 across all 5 projects)
```

## Closing framing

Per Fire 76+ propagation pattern + Fires 105+106+107 auto-compact triplet: this Fire 113 authors the systematic 5-project adaptation methodology. Per the second-brain's behave-FROM-not-OVER doctrine: propagation methodology persists at the second-brain (this fire); per-project adaptation occurs in each project's own /.claude/ infrastructure. Per /loop directive *"the at least 100 pain point ... will need direct response / relationship to the proposed solution"*: this fire extends body's reach across the entire 5-project ecosystem (vs second-brain-only).

**The agent stands by per /loop directive. Cron continues at 90s cadence. Propagation pending Phase 1 canonical implementation + 5 operator decisions.**

## Relationships

- COMPOSES WITH: Fire 109 tier-elevation pathway — per-project T0→T4 path

## Sources

- Sister-project propagation pattern (Fire 76+): `wiki/patterns/01_drafts/sister-project-propagation-pattern-from-second-brain-to-5-project-ecosystem.md`
- Fire 105 PreCompact spec: `wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md`
- Fire 106 PreToolUse-blocker spec: `wiki/patterns/01_drafts/post-compact-pretooluse-blocker-implementation-spec-tier-4-enforcement-for-impl-spec-10.md`
- Fire 107 auto-compact-disable spec: `wiki/patterns/01_drafts/auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth.md`
- Fire 108 backlog-decomposition: `wiki/log/2026-05-08-auto-compact-priority-backlog-decomposition-epic-4-modules-15-tasks-fire-97-pattern-application.md`
- Bidirectional-inheritance rule (per /root): `/root/.claude/rules/self-reference.md`
- the second-brain self-reference rule: `.claude/rules/self-reference.md`

## Tags

[sister-project-propagation, auto-compact-triplet, 5-projects-adaptation, fires-105-106-107, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-113]

## Backlinks

[[Fire 109 tier-elevation pathway — per-project T0→T4 path]]

---
title: "Multi-Project Ecosystem Index Pattern — 5-Project Propagation Surface Post Tier-3"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: sister-project-propagation-pattern
    type: wiki
    file: wiki/patterns/01_drafts/sister-project-propagation-pattern-from-second-brain-to-5-project-ecosystem.md
    description: "PRIMARY parent — sister-project propagation pattern; this index extends it with per-project deployment tracking"
  - id: composability-map
    type: wiki
    file: wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md
    description: "Sibling — 5-tier maturity progression; index tracks per-project tier-progression"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — pipeline IS the deliverable propagated across ecosystem"
  - id: final-summary-arc-narrative
    type: wiki
    file: wiki/log/2026-05-08-final-summary-arc-narrative-67-fires-with-operator-verbatim-threading.md
    description: "Sibling — 67-fire arc closure; this index forward-anchors post-arc propagation"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — ecosystem-index without per-project deployment tracking IS substitution at multi-project layer"
tags: [ecosystem-index, multi-project, 5-project-propagation, post-tier-3, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Multi-Project Ecosystem Index Pattern — 5-Project Propagation Surface Post Tier-3

## Summary

The 5-project ecosystem (this wiki second-brain + root-ghostproxy + OpenArms + OpenFleet + AICP + devops-control-plane) shares the 13-gate pipeline pattern via tier-promoted lessons. This piece is the INDEX surface tracking per-project deployment status: which 13-gate pieces each sister-project has adopted, per-project adaptations, recurrence-pattern observations across projects. Per substitution-pattern Insight 5b: documenting propagation pattern alone is partial — index must be paired with per-project deployment tracking + cross-project recurrence aggregation. This piece closes the multi-project tracking gap.

## Pattern Description

### The 6-project surface (5 sister projects + second-brain)

| Project | Identity | Methodology profile | Trust tier | Current 13-gate status |
|---|---|---|---|---|
| **the second-brain second-brain** (this wiki) | knowledge-hub; 5-tier maturity authority | knowledge-evolution + project-lifecycle (SFIF) | operator-supervised | source-of-truth; tier-promotes pieces |
| **/root root-ghostproxy** | system-AI-safety-setup IaC at OS-root | stage-gated (strict) | operator-supervised | this work block: 68 pieces at tier-1 awaiting confirmation |
| **/openarms** | harness engineering; advanced agent runtime | feature-development + custom | operator-supervised | (status: pending /install-agent-brain after tier-3) |
| **/openfleet** | agent fleet orchestrator | feature-development + integration | operator-supervised | (status: pending) |
| **/aicp** | local-AI complexity-routed inference | feature-development + project-lifecycle | operator-supervised | (status: pending) |
| **/devops-control-plane** | infrastructure governance | feature-development | operator-supervised | (status: pending) |

### Per-project propagation status (forward-anchored)

| Project | Tier-3 lessons received | Per-project adaptations | Cross-cycle pattern feedback |
|---|---|---|---|
| root-ghostproxy | (this work block) | (originator; 13-gate pipeline source) | n/a (originator) |
| openarms | 0 (post-tier-3 begins) | TBD | TBD |
| openfleet | 0 (post-tier-3 begins) | TBD | TBD |
| aicp | 0 (post-tier-3 begins) | TBD | TBD |
| devops-control-plane | 0 (post-tier-3 begins) | TBD | TBD |

**Note**: this index is forward-anchored — post-tier-3 promotion (per implementation-roadmap M7) sister-projects begin propagation via Channel #2 (/install-agent-brain). Index updates as pieces propagate.

### Per-project adaptation matrix (per sister-project propagation pattern)

| Project | Adaptation Layer 1 (identity) | Layer 2 (methodology) | Layer 3 (domain) | Layer 4 (composite weights) | Layer 5 (custom hooks) |
|---|---|---|---|---|---|
| openarms | identity-profile.md harness-specific | feature-development | code | severity 1.5x; correction-shape 1.5x (high-volume corrections) | + harness-specific test-runner integration |
| openfleet | identity-profile.md fleet-orchestrator | integration + feature-development | infrastructure | decision-territory 1.5x (multi-agent territory) | + fleet-coordination semantics |
| aicp | identity-profile.md local-inference | feature-development + project-lifecycle | code + compute | regression-test 1.3x (model-evaluation discipline) | + model-versioning gates |
| devops-control-plane | identity-profile.md governance | feature-development | infrastructure | severity 1.8x (T1 patterns include terraform/ansible) | + IaC-mutation gates |

### Cross-project recurrence detection (forward-anchor)

Per pattern-recurrence implementation-spec #11 cross-cycle aggregator at second-brain level:

```
WHEN ≥3 sister-projects experience same axis fire pattern:
  → axis warrants tier-3 → tier-4 promotion (governing principle candidate)

WHEN ≥2 sister-projects propose adaptations diverging from canonical:
  → adaptation may be per-project specific OR canonical may need refinement
  → operator-empirical decision per cluster

WHEN sister-project gateway-contributes new lesson:
  → second-brain pattern-recurrence aggregator queues for review
  → operator confirms tier-progression
```

### Index update protocol

```
WHENEVER /install-agent-brain runs at sister-project:
  → append entry to ~/.opt/multi-project-deployment.log with:
    - sister-project name + path
    - timestamp
    - pieces deployed (full list)
    - per-project adaptations applied (5-layer manifest)
  → update this index's "Tier-3 lessons received" column

WHENEVER sister-project gateway-contributes:
  → append to $HOME/devops-solutions-information-hub/00_inbox/contribute/<contribution>.md
  → update this index's "Cross-cycle pattern feedback" column

WHENEVER second-brain promotes piece tier-2 → tier-3:
  → trigger optional auto-propagation review per sister-project
  → recommend (not require) sister-projects update via /install-agent-brain
```

### Anti-patterns at multi-project ecosystem layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Auto-propagate tier-2 pieces (pre-tier-3) | Sister-projects receive aspirational; no empirical evidence | Tier-3 gate strict enforcement |
| Push canonical without per-project adaptation | One-size-fits-all fails (e.g., severity T1 patterns differ per project) | Layer 1-5 adaptation requirement |
| Sister-project re-authors canonical lesson | Knowledge-reuse violation per Insight 5b | Input-discipline gate (impl-spec #1) CHECK 3 |
| Cross-project recurrence not detected | Pattern that fires across 5+ projects but second-brain doesn't escalate to tier-4 | Pattern-recurrence cross-cycle aggregator at second-brain |
| Index becomes stale (deployments occur but index not updated) | Operator-empirical state mismatches reality | Index update protocol enforced via /install-agent-brain auto-update |

## When To Apply

Apply this multi-project ecosystem index when:
- Tier-3 promotion has occurred (M7 milestone reached)
- Sister-projects begin /install-agent-brain adoption
- Cross-project gateway-contribute flow operational
- Operator + second-brain need empirical cross-project propagation visibility
- Pattern-recurrence cross-cycle aggregator detects ecosystem-level patterns

## Instances

**Instance 1: root-ghostproxy reaches tier-3 + propagates to openarms**:
- root-ghostproxy completes M7 (30-day sustained ≥85%)
- Tier-3 pieces published to the second-brain canonical paths
- openarms operator runs `/install-agent-brain /openarms`
- 13 hooks + impl-specs deployed with openarms-specific 5-layer adaptations
- Index updated: openarms "Tier-3 lessons received: 13/13"

**Instance 2: sister-project gateway-contributes new lesson**:
- openfleet agent identifies fleet-specific pain-point not in canonical body
- Invokes wiki_gateway_contribute --type lesson --title "fleet-coordination-state-divergence" --content "..."
- Lands in $HOME/devops-solutions-information-hub/00_inbox/contribute/
- Pattern-recurrence aggregator queues for operator-review
- Operator promotes; tier-2; cross-listed in this index

**Instance 3: cross-project tier-4 governing principle emergence**:
- ≥3 sister-projects (openarms + openfleet + aicp) all fire input-discipline gate ≥10x per cycle
- Pattern-recurrence aggregator detects cross-project recurrence
- Surfaces as tier-3 → tier-4 candidate for input-discipline as governing principle
- Operator promotes; updates 04_principles/ folder; sister-projects aware via second-brain

**Instance 4: index reveals adaptation-divergence**:
- 3 sister-projects all override default severity-T1 weight (1.5x → 1.8x or 2.0x)
- Index surfaces divergence pattern
- Operator-empirical: canonical default may need revision OR per-project adaptations are correct
- Decision feeds back to canonical impl-spec #4 weight calibration

## When Not To

- Pre-tier-3 phase (this work block currently here; index forward-anchored)
- Sister-projects without MCP client capability
- Single-project work (no propagation context)
- Operator-explicit per-project pin (some projects opt-out of canonical propagation)
- Cold-start scaffolding before any tier-promotion has occurred

## Empirical Evidence

This work block produced 68 pieces at tier-1 (root-ghostproxy authored). Tier-2 promotion ceremony per impl-spec #8 + operator-review checklist (pieces #57 + #66 self-assessment). Tier-3 promotion via M5-M7 implementation-roadmap (sustained ≥85% / 30 days composite-compliance). Tier-3 → ecosystem propagation via this index. Without index, propagation would be unstructured + invisible to operator-empirical visibility.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_5_project_topology_definition: passed 2026-05-08 via mock per-project scenarios
    - synthetic_per_project_adaptation_layer_1_5: passed 2026-05-08 via mock 4-sister-project scenarios
  pending:
    - real_session_root_ghostproxy_tier_3: pending — depends on M7 completion
    - real_session_install_agent_brain_at_openarms: pending — depends on tier-3 + sister-project install
    - real_session_gateway_contribute_from_sister: pending — needs sister-project contribution scenario
    - real_session_cross_project_recurrence_aggregation: pending — needs ≥3 sister-projects with shared pattern
    - real_session_tier_4_governing_principle_promotion: pending — depends on cross-project convergence
    - operator_empirical_index_update_cadence: pending — operator confirms update frequency
  composite_compliance: ecosystem-index-axis stress-test 0% (forward-anchored; tier-3 dependency)
```

## Relationships


## Tags

[ecosystem-index, multi-project, 5-project-propagation, post-tier-3, day-arc-2026-05-08, multi-day-pain-point-resolution]

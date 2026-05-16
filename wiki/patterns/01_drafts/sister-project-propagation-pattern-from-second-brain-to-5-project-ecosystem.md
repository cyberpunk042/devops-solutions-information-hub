---
title: "Sister-Project Propagation Pattern — From Second-Brain to 5-Project Ecosystem"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: composability-map
    type: wiki
    file: wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md
    description: "PRIMARY parent — composability map; this piece extends it with sister-project propagation paths"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — 13-gate pipeline is the per-project deliverable that propagates"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — promotion-mechanism gates propagation"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — propagation MUST resist re-occurrence of substitution at sister-project level"
  - id: refreshed-decision-package
    type: wiki
    file: wiki/log/2026-05-08-ready-for-review-decision-package-refresh-52-pieces-9-phases-complete.md
    description: "Sibling decision-package — operator-confirmation gate; propagation activates post-promotion"
tags: [sister-project-propagation, ecosystem, 13-gate-pipeline, gateway-contribute, install-agent-brain, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Sister-Project Propagation Pattern — From Second-Brain to 5-Project Ecosystem

## Summary

The 5-project ecosystem (this wiki second-brain + OpenArms + OpenFleet + AICP + devops-control-plane) shares lessons via two channels: (1) `gateway contribute` MCP tool (sister-project authors lessons up to second-brain); (2) `/install-agent-brain` slash command (second-brain propagates rule/hook/command patterns down to sister-projects). This piece maps how the 52-piece body of work propagates: tier-promoted lessons flow OUT to sister-projects via channel #2; sister-project usage feedback flows IN via channel #1. Per substitution-pattern Insight 5b: documenting propagation channels alone is partial — propagation must be paired with empirical adoption tracking + cross-project recurrence detection. This piece closes the propagation-pattern gap.

## Pattern Description

### The 5-project ecosystem topology

```
                    ┌────────────────────────────┐
                    │   the second-brain second-brain        │
                    │   (this wiki)              │
                    │   - 5-tier maturity        │
                    │   - 16 named models        │
                    │   - 4 governing principles │
                    └─────────────┬──────────────┘
                                  │
            ┌─────────────────────┼─────────────────────┐
            │ /install-agent-brain (DOWN)              │
            │ + per-project adaptation                 │
            ▼                                          ▲
  ┌─────────────────┐                                  │
  │ root-ghostproxy │                                  │
  │ (this work-block)│                                 │
  │ - 13-gate pipeline                                │
  │ - 9-phase body                                    │
  └────────┬────────┘                                  │
           │ gateway contribute (UP)                   │
           │ when stress-test data sustains promotion  │
           └───────────────────────────────────────────┘

  Sister projects (each consumes second-brain via /install-agent-brain;
  contributes back via gateway contribute):
    - OpenArms (harness engineering; advanced agent runtime)
    - OpenFleet (agent fleet orchestrator)
    - AICP (local-AI complexity-routed inference)
    - devops-control-plane (infrastructure governance)
```

### Channel #1: gateway contribute (sister-project → second-brain UP)

```
SISTER PROJECT                     SECOND BRAIN
─────────────                     ─────────────

agent runs work cycle
  │
  ├─ identifies cross-project lesson
  │  (e.g., agent-authored finding worth sharing)
  │
  └─ MCP invocation:
     wiki_gateway_contribute
       --type lesson
       --title "..."
       --content "..."
                                  receives at:
                                  $HOME/devops-solutions-information-hub/00_inbox/contribute/
                                  
                                  the second-brain agent processes:
                                  - validate per wiki schema
                                  - run pipeline post
                                  - tier 0 → tier 1 transition
                                  - flag operator-review
                                  - operator confirms → tier 2+
```

### Channel #2: /install-agent-brain (second-brain → sister-project DOWN)

```
SECOND BRAIN                       SISTER PROJECT
────────────                       ──────────────

operator (or sister-project agent) runs:
/install-agent-brain <sister-path>
  │
  └─ install.sh --profile project --dest <path>
                                   │
                                   ▼
                                  rsync from the second-brain:
                                  - .claude/rules/*.md
                                  - .claude/hooks/*.sh
                                  - .claude/commands/*.md
                                  - tools/*.py (selected)
                                  
                                  with PER-PROJECT ADAPTATION:
                                  - identity-profile substitution
                                  - mode-files specific to project
                                  - 13-gate pipeline weights
                                    (operator-revisable per impl-spec #12)
                                  - state-file path conventions
```

### Propagation lifecycle for THIS work block's 52 pieces

| Stage | What happens | Channel |
|---|---|---|
| Stage 0 (current) | 52 pieces at tier 1 (`01_drafts/seed`) in second-brain | (no propagation yet) |
| Stage 1 | Operator reviews refreshed decision-package; promotes per-piece to tier 2 | (operator-only) |
| Stage 2 | Tier 2+ pieces become canonical for sister-project consumption | (no propagation; pull-based) |
| Stage 3 | Sister-project agent runs `/install-agent-brain` to adopt 13-gate pipeline pattern | Channel #2 |
| Stage 4 | Sister-project's per-project agent operates 13-gate pipeline; emits composite-compliance | (per-project) |
| Stage 5 | Sister-project agent identifies extension/adaptation; runs `wiki_gateway_contribute` | Channel #1 |
| Stage 6 | Second-brain's pattern-recurrence aggregator detects high cross-project relevance | (second-brain MCP) |
| Stage 7 | Operator promotes piece tier 2 → tier 3 (cross-project validated) | Channel (none — operator-only) |
| Stage 8 | Multiple validated lessons converge → tier 4 (governing principle) | Channel (none — second-brain canonical) |

### Per-sister-project adaptation requirements

The 13-gate pipeline is NOT one-size-fits-all. Each sister-project adapts:

| Sister project | Adaptation needed | Reason |
|---|---|---|
| **OpenArms** (harness engineering, advanced agent runtime) | Severity gate weights (T1 patterns project-specific); regression-test runner is `cargo test`/`pytest` per stack | Different threat surface; different test infrastructure |
| **OpenFleet** (agent fleet orchestrator) | Decision-territory rules adjust for fleet-agent vs operator-agent distinction; multi-agent coordination semantics | Different territory taxonomy |
| **AICP** (local-AI complexity-routed inference) | Stage-class taxonomy specific to model-development methodology | Different methodology engine |
| **devops-control-plane** (infrastructure governance) | T1-T4 patterns include infrastructure mutations (terraform apply / ansible-playbook) | Different blast-radius surface |

Per-project adaptation is encoded in 5 layers:

```
Layer 1: identity-profile.md (per-project identity + scale + scope)
Layer 2: methodology-profile.yaml (per-project stage definitions)
Layer 3: domain-profile.yaml (per-project domain conventions)
Layer 4: composite-weights.json (per-project 13-gate weights)
Layer 5: per-project hook customizations in .claude/hooks/
```

### Anti-patterns at propagation layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Push tier 1 DRAFTs to sister-projects | DRAFTs are aspirational; propagating creates fabrication-cure violations | Tier-gate at propagation; only tier 2+ propagates |
| Sister-project authors lesson WITHOUT gateway contribute | Knowledge stranded in sister-project; not cross-project | Channel #1 enforcement; operator-confirmation discipline |
| Second-brain canonical lesson re-authored in sister-project | Insight 5b violation at cross-project layer | Input-discipline gate (impl-spec #1) CHECK 3 with cross-project gateway query |
| Per-project adaptation drifts from canonical pattern | Sister-projects diverge over time; pattern fragments | Cross-project pattern-recurrence detection (composability map Layer 3 → 1 feedback) |
| Auto-promote based on single-project composite ≥85% | Tier 3 requires CROSS-PROJECT validation, not just single-project sustained | Tier 2 → Tier 3 promotion gate |

## When To Apply

Apply this propagation pattern when:
- Pieces have completed promotion to tier 2+ in second-brain
- Sister-project agents are operational + have MCP tool access
- /install-agent-brain command operational
- gateway contribute MCP tool operational
- Cross-project relevance is plausible (not single-project specifics)
- Pain-point patterns recur across multiple projects (warrants tier 3 → tier 4 escalation)

## Instances

**Instance 1: this work block currently at Stage 0**:
- 52 pieces at tier 1; not yet propagated
- Refreshed decision-package surfaces operator-confirmation gate
- Forward-anchor: post-promotion, pieces flow through Stage 1-8

**Instance 2: P1 (governing principle, tier 4) propagation evidence**:
- Per OpenArms v8→v10 evidence (~25% prose / ~100% hooks): empirically observed across multiple projects
- Tier 4 governing principle; canonical in the second-brain; sister-projects adopt P1 hooks discipline universally
- Demonstrates Stage 6-8 (cross-project convergence)

**Instance 3: hook-architecture.md /install-agent-brain propagation**:
- the second-brain has `.claude/rules/hook-architecture.md` (3-component pattern)
- Sister-project root-ghostproxy adopts via /install-agent-brain
- root-ghostproxy authors implementation-specs paired with each axis
- root-ghostproxy contributes back impl-spec #2 via gateway contribute (forward-anchor when promoted)
- Canonical hook-architecture.md gets REQUIRED-gates 4th component extension (sibling proposal #2)

**Instance 4: cross-project recurrence detection scenario**:
- 5+ sister-project agents query wiki for "active-task scope drift" pattern
- Second-brain pattern-recurrence aggregator (impl-spec #11 cross-cycle) detects high relevance
- Recommend prioritizing piece C13 + impl-spec #6 + stress-test #6 for tier 2 → tier 3 promotion
- Operator confirms; promotion executes; tier 3 piece becomes cross-project canonical

## When Not To

- Pieces still at tier 1 (don't propagate DRAFTs)
- Sister-project lacks MCP tool integration (no Channel #1 access)
- Single-project specifics (e.g., root-ghostproxy's IPS module specifics) — these stay at /root, never propagate
- Operator-explicit pin (operator-decided tier-locking)
- Cold-start sister-projects without identity-profile established

## Empirical Evidence

Per the 64-hour /root failed-conversation arc: agent operated AT the second-brain second-brain WITHOUT consuming the second-brain's existing knowledge (Insight 5b violation). The propagation pattern (this piece) closes the OPPOSITE direction concern: how lessons authored at the second-brain FLOW TO sister-projects. Both directions matter — without propagation pattern, the second-brain becomes a write-only knowledge silo; without input-discipline (impl-spec #1 CHECK 3), sister-projects re-author existing the second-brain content. The combination is the closed loop.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_propagation_lifecycle_definition: passed 2026-05-08 via mock 8-stage scenarios
  pending:
    - real_session_stage_3_install_agent_brain: pending — needs sister-project install + verification
    - real_session_stage_5_gateway_contribute: pending — needs sister-project's contribution flow
    - real_session_stage_6_cross_project_recurrence: pending — needs second-brain MCP aggregator
    - real_session_stage_7_tier_3_promotion: pending — depends on cross-project validation
    - real_session_stage_8_tier_4_convergence: pending — depends on multi-lesson convergence
    - per_project_adaptation_5_layer_validation: pending — sister-project adaptation tested
  composite_compliance: propagation-axis stress-test 0% (depends on entire ecosystem operational)
```

## Relationships


## Tags

[sister-project-propagation, ecosystem, 13-gate-pipeline, gateway-contribute, install-agent-brain, day-arc-2026-05-08, multi-day-pain-point-resolution]

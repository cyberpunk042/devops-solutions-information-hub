---
title: "Cascade candidate — root-ghostproxy ↔ selfdef scope-clarification (operator-verbatim 2026-05-15: 'not just going to use the selfdef project')"
type: note
domain: cross-domain
status: draft
confidence: high
created: 2026-05-16
updated: 2026-05-16
last_reviewed: 2026-05-16
authored: 2026-05-16T00:18:00-04:00
note_type: directive
authorship: agent-authored
profile: root-ghostproxy-rollout
cascade_target: root-ghostproxy
target_module: cross-cutting (M005 + scope dimension)
target_epic: root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05
decision_needed: root-ghostproxy-vs-selfdef-scope-boundary
sources:
  - id: operator-verbatim-2026-05-15
    type: directive
    file: AGENTS.md (this Profile workspace)
    description: "Operator-stated, sacrosanct: 'some of the things root-ghostproxy were going to do its not just going to use the selfdef project. so root-ghostproxy can focus more on its thing.'"
  - id: sister-projects-yaml
    type: file
    file: wiki/config/sister-projects.yaml
    description: "Registry entry for root-ghostproxy: 'Planned modules: suricata (IPS), polarproxy (TLS inspection).' Same 9-module catalog appears in selfdef entry."
  - id: epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05.md
    description: "Epic Stream 2 M5: 'Operator picks: suricata IPS module OR polarproxy TLS inspection module.'"
tags:
  - cascade-candidate
  - root-ghostproxy
  - selfdef
  - scope-clarification
  - operator-verbatim-2026-05-15
  - multi-vision
  - cross-project-cascade
  - sprint
related:
  - wiki/config/sister-projects.yaml
  - wiki/backlog/epics/pre-milestone/root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05.md
  - wiki/backlog/modules/root-ghostproxy-m005-first-specialized-feature-module.md
---

# Cascade candidate — root-ghostproxy ↔ selfdef scope-clarification (operator-verbatim 2026-05-15)

## Summary

The operator stated verbatim on 2026-05-15 that "some of the things root-ghostproxy were going to do its not just going to use the selfdef project. so root-ghostproxy can focus more on its thing." The second-brain's record shows substantial overlap between root-ghostproxy's planned module catalog (suricata IPS + polarproxy TLS inspection per sister-projects.yaml line "Planned modules: suricata (IPS), polarproxy (TLS inspection)") and selfdef's shipped 9-module catalog (detect-host daemon, bridge-l2, suricata, polarproxy, vpn-bridge, integrity-sentinel, tetragon, agent-guard, observability per sister-projects.yaml selfdef entry). The operator's statement implies a scope-rebalancing is required, but does NOT state which modules stay where. This candidate surfaces the boundary question with three operator-decision options. This Profile does NOT decide what selfdef's scope is, what root-ghostproxy's "thing" is, or which modules move where — those are operator-territory decisions.

## Operator-stated requirements (verbatim, sacrosanct)

> *"some of the things root-ghostproxy were going to do its not just going to use the selfdef project. so root-ghostproxy can focus more on its thing."* — operator, 2026-05-15

> *"we can discuss this profile but I think if you look into root-ghostproxy and probably even here in the second-brain there is already probably report of the situation and my request for the resolutions."* — operator, 2026-05-15

> *"obviously on this machine here its not installed yet, its normal."* — operator, 2026-05-15 (root-ghostproxy specifically, contextualizing observation-only posture)

## Observed module-catalog overlap (from sister-projects.yaml inline)

| Module | Listed in root-ghostproxy entry | Listed in selfdef entry |
|---|---|---|
| suricata (IPS) | YES ("Planned modules: suricata...") | YES (shipped 9-module catalog: "suricata") |
| polarproxy (TLS inspection) | YES ("...polarproxy (TLS inspection)") | YES (shipped 9-module catalog: "polarproxy") |
| detect-host (daemon) | not listed | YES |
| bridge-l2 | not listed | YES |
| vpn-bridge | not listed | YES |
| integrity-sentinel | not listed | YES |
| tetragon | not listed | YES |
| agent-guard | not listed | YES |
| observability | not listed | YES |

The two overlap modules (suricata, polarproxy) are exactly the two operator named for root-ghostproxy's M5 ("Operator picks: suricata IPS module OR polarproxy TLS inspection module") in the 2026-05-04 epic. Selfdef appears to have already shipped both. This Profile cannot verify selfdef's shipped status without reading selfdef's repo (cross-project boundary) — the "shipped" claim comes only from the second-brain's sister-projects.yaml description.

## Alternative Visions

### Vision A — Operator confirms root-ghostproxy owns suricata + polarproxy, selfdef owns the rest

Operator-decision-text might read: "root-ghostproxy is the OS-level security envelope; suricata + polarproxy are its load-bearing IPS/TLS features. Selfdef owns the broader 9-module self-defense surface but root-ghostproxy can use selfdef's implementations of suricata + polarproxy as upstream substrates if helpful. Independence preserved at the module-boundary."

Implications: M5 stays as-is in the root-ghostproxy epic. sister-projects.yaml notes selfdef as optional-substrate, not dependency. No second-brain rewrite needed beyond a one-line clarification in both project descriptions.

Trade-offs: (+) minimal change; (+) honors "focus more on its thing" by keeping the OS-security framing; (–) does not actually narrow root-ghostproxy's scope much.

### Vision B — Selfdef owns suricata + polarproxy; root-ghostproxy drops them

Operator-decision-text might read: "selfdef has the 9-module catalog including suricata + polarproxy. root-ghostproxy's 'thing' is something narrower (e.g., Claude-Code/opencode AI-safety hooks + OS hardening only). M5 in the epic is wrong; root-ghostproxy's specialized features are TBD and do NOT include suricata or polarproxy."

Implications: M5 needs operator-defined replacement scope. Epic Stream 2 M5 reframed. sister-projects.yaml root-ghostproxy entry "Planned modules: suricata (IPS), polarproxy (TLS inspection)" deleted.

Trade-offs: (+) maximally narrows root-ghostproxy per operator's "focus more on its thing"; (+) sharpens distinct project identities; (–) requires operator to define what M5 becomes; (–) sister-projects.yaml rewrite (operator-territory).

### Vision C — Per-module operator pick (1-by-1, no class decision)

Operator-decision-text might read: "for suricata: lives in [X]. for polarproxy: lives in [Y]. for any future module: decide at filing time, not via class rule." No general rule; per-module operator picks documented as they happen.

Implications: M5 becomes "operator picks a specific module at module-filing time" not "operator picks suricata OR polarproxy." Both projects' module lists become editorial-mutable per operator decisions.

Trade-offs: (+) operator retains maximal flexibility; (+) no premature class-decision risk; (–) every future module requires explicit operator pick (cron overhead); (–) sister-projects.yaml descriptions need to flag "module list per operator-decision-queue history" not "planned modules."

## What this candidate does NOT do

- Does NOT decide what root-ghostproxy's "thing" is. Operator-territory per sacrosanct rule.
- Does NOT decide what selfdef's scope is. Operator-territory.
- Does NOT propose moving any module anywhere. Surfaces the question + options.
- Does NOT read selfdef's repo. Cross-project boundary; observation-via-second-brain-record only.
- Does NOT touch root-ghostproxy. Observation-only via gh api (this candidate didn't even need that).
- Does NOT conflate the two projects under any meta-framing. They remain distinct.

## Context Boundaries

- The operator-verbatim is one sentence. It STATES a fact (overlap exists, refocus is desired) but does NOT prescribe the resolution. This candidate honors that ambiguity by surfacing options rather than picking one.
- The "selfdef has shipped 9 modules" claim is from the second-brain's sister-projects.yaml description, not from a direct selfdef-repo read. If the description is wrong, vision picks should be revisited.
- Whatever the operator picks affects M5 + the sister-projects.yaml descriptions for BOTH root-ghostproxy and selfdef. Those are operator-territory edits.
- A "selfdef-boundary-candidate" (companion artifact mentioned in this Profile's sprint plan) is FOLDED INTO this candidate — the boundary question and the scope-clarification question are the same operator-decision in different framings; surfacing them as one keeps the operator's decision-load Goldilocks-sized at one item, not two.

## Cascade Marker

- `cascade: root-ghostproxy`
- `target_module: M005` + scope dimension across the epic
- `decision_needed: root-ghostproxy-vs-selfdef-scope-boundary (A | B | C)`
- `operator_action: pick vision A/B/C in operator-decision-queue.md (Q88)`
- `folds_in: selfdef-boundary-candidate (same operator-decision)`

## Relationships


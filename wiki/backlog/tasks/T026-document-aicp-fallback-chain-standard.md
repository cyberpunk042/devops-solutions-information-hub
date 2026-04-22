---
title: "T026 — Document AICP Fallback Chain as Standard Page"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 90
progress: 0
stages_completed: [document, design]
artifacts:
  - wiki/spine/standards/aicp-fallback-chain.md
estimate: S
epic: "E011"
module: "E011-m004"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m004-circuit-breakers-and-fallback-chain
    type: wiki
    file: wiki/backlog/modules/e011-m004-circuit-breakers-and-fallback-chain.md
tags: [task, p1, e011, aicp, standard, documentation, fallback-chain, wiki-page]
---

# T026 — Document AICP Fallback Chain

## Summary

Create `wiki/spine/standards/aicp-fallback-chain.md` as a living standard describing the 5-tier cascade: trigger conditions per tier (breaker OPEN vs `is_available()==False` vs HTTP timeout), recovery semantics (HALF_OPEN probe), an operator playbook for common failure modes, and a mermaid diagram of the chain.

## Done When

- [ ] `wiki/spine/standards/aicp-fallback-chain.md` exists with full frontmatter (type: standard, domain: reliability, status: growing)
- [ ] Page length ≥150 lines (per operator's wiki minimums)
- [ ] Includes a mermaid flowchart showing the 5-tier cascade with trigger labels
- [ ] Threshold table matches T023's config values
- [ ] Operator playbook section: "if k2_6_openrouter opens repeatedly, look at X, Y, Z"
- [ ] Relationships section links to E011 epic + m004 module + configuration sources
- [ ] `python3 -m tools.pipeline post` passes after commit

## Procedure

```bash
cd /home/jfortin/devops-solutions-research-wiki
python3 -m tools.pipeline scaffold standard "aicp-fallback-chain"
# OR create manually with the outline below

$EDITOR wiki/spine/standards/aicp-fallback-chain.md

python3 -m tools.pipeline post
```

### Outline

- Summary
- Context: why a fallback chain exists, failure modes captured
- The 5 Tiers — table with backend, trigger, expected latency, cost ratio
- Mermaid diagram
- Breaker states and transitions (CLOSED → OPEN → HALF_OPEN → CLOSED)
- Operator playbook: 5 scenarios with diagnostic commands
- Threshold rationale (why 1 for local, 3 for online, 5 for claude)
- Relationships

## Rollback

```bash
cd /home/jfortin/devops-solutions-research-wiki
rm wiki/spine/standards/aicp-fallback-chain.md
python3 -m tools.pipeline post
```

## Relationships

- PART OF: [[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]

## Backlinks

[[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]

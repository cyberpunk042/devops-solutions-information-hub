---
title: "T029 — Author Routing Review Ritual Standard"
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
  - wiki/spine/standards/routing-review-ritual.md
estimate: S
epic: "E011"
module: "E011-m005"
depends_on:
  - "T028"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m005-routing-metric-and-review-ritual
    type: wiki
    file: wiki/backlog/modules/e011-m005-routing-metric-and-review-ritual.md
tags: [task, p1, e011, aicp, standard, ritual, weekly-review, observability]
---

# T029 — Author Routing Review Ritual

## Summary

Create `wiki/spine/standards/routing-review-ritual.md` per the outline in `e011-m005` Step 3. Weekly cadence, inputs, checklist, red-flag thresholds, escalation steps. Solo-operator friendly.

## Done When

- [ ] `wiki/spine/standards/routing-review-ritual.md` exists with full frontmatter (type: standard, domain: reliability, status: growing)
- [ ] Page length ≥150 lines
- [ ] Cadence section specifies weekly rhythm + trigger conditions
- [ ] Inputs section lists `aicp routing-report --window 7d`, OpenRouter dashboard URL, breaker-open log grep
- [ ] Checklist has ≥5 items covering traffic distribution, cost, reliability, quality
- [ ] Red-flag thresholds table has ≥4 rows
- [ ] Escalation section defines when to open a follow-up epic
- [ ] Log template `wiki/log/YYYY-MM-DD-routing-first-week.md` created as a stub
- [ ] `python3 -m tools.pipeline post` passes after commit

## Procedure

```bash
cd /home/jfortin/devops-solutions-research-wiki
python3 -m tools.pipeline scaffold standard "routing-review-ritual"
# OR create manually — see e011-m005 Step 3 for canonical outline

$EDITOR wiki/spine/standards/routing-review-ritual.md

# Create stub log template (fill after first review)
$EDITOR wiki/log/2026-04-29-routing-integration-first-week.md

python3 -m tools.pipeline post
```

## Rollback

```bash
cd /home/jfortin/devops-solutions-research-wiki
rm wiki/spine/standards/routing-review-ritual.md
rm -f wiki/log/2026-04-29-routing-integration-first-week.md
python3 -m tools.pipeline post
```

## Relationships

- PART OF: [[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T028-add-routing-report-cli-command|T028-add-routing-report-cli-command]]

## Backlinks

[[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T028-add-routing-report-cli-command|T028-add-routing-report-cli-command]]

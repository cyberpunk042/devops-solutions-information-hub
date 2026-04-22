---
title: "T028 — Add `aicp routing-report` CLI Command (7d Rollup)"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 85
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: M
epic: "E011"
module: "E011-m005"
depends_on:
  - "T027"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m005-routing-metric-and-review-ritual
    type: wiki
    file: wiki/backlog/modules/e011-m005-routing-metric-and-review-ritual.md
  - id: aicp-cli-main
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/cli/main.py
  - id: aicp-metrics
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/metrics.py
tags: [task, p1, e011, aicp, cli, routing-report, metrics-rollup, reporting]
---

# T028 — Add `aicp routing-report` CLI Command

## Summary

Add a `routing-report` subcommand to AICP's CLI that produces a concise per-backend table for a configurable time window (1d/7d/30d). Shows requests, share %, tokens, cost, avg latency, breaker-open events. Supports `--format table|json`. Adds an `aggregate_window(window: str)` helper to `aicp/core/metrics.py` that walks the JSONL log and buckets by backend.

## Done When

- [ ] `aicp routing-report --window 7d` prints a sorted table with 6 columns
- [ ] `aicp routing-report --window 1d --format json` emits valid JSON
- [ ] `aggregate_window()` in `aicp/core/metrics.py` walks `$AICP_LOG_FILE`, filters by ISO timestamp, buckets by `backend`
- [ ] Missing log file → empty table with clear note (no crash)
- [ ] Unit test: feed synthetic JSONL → assert aggregates match manual computation
- [ ] `aicp routing-report --help` shows the full help text
- [ ] Change committed with message: `feat(cli): routing-report subcommand + aggregate_window helper`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
grep -n "@app.command\|def aggregate" aicp/cli/main.py aicp/core/metrics.py

$EDITOR aicp/cli/main.py      # add routing-report command per e011-m005 Step 2
$EDITOR aicp/core/metrics.py  # add aggregate_window helper

python3 -m pytest tests/ -k "metrics or routing_report" -v

# Smoke test — requires seeded log
python3 -m aicp.cli.main routing-report --window 7d
python3 -m aicp.cli.main routing-report --window 1d --format json
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/cli/main.py aicp/core/metrics.py
```

## Relationships

- PART OF: [[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T027-verify-metrics-capture-k2-6-backends|T027-verify-metrics-capture-k2-6-backends]]

## Backlinks

[[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T027-verify-metrics-capture-k2-6-backends|T027-verify-metrics-capture-k2-6-backends]]

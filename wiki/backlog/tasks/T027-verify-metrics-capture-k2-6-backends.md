---
title: "T027 — Verify Metrics (Prometheus + aggregate) Capture k2_6 Backends"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 100
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: XS
epic: "E011"
module: "E011-m005"
depends_on:
  - "T018"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m005-routing-metric-and-review-ritual
    type: wiki
    file: wiki/backlog/modules/e011-m005-routing-metric-and-review-ritual.md
  - id: aicp-prometheus
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/prometheus.py
  - id: aicp-metrics
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/metrics.py
tags: [task, p1, e011, aicp, metrics, prometheus, verification, observability]
---

# T027 — Verify Metrics Capture K2.6 Backends

## Summary

Run real K2.6-via-OpenRouter traffic through AICP and verify the three metric channels (JSONL log, `metrics.aggregate()`, Prometheus endpoint) all capture `k2_6_openrouter` by key/label. If any channel hardcodes the backend list, fix it.

## Done When

- [ ] 3+ K2.6 prompts routed via `aicp run --backend k2_6_openrouter`
- [ ] `tail -20 $AICP_LOG_FILE | jq 'select(.backend == "k2_6_openrouter")'` returns ≥3 entries
- [ ] `metrics.aggregate(count=50)` returns dict with `by_backend["k2_6_openrouter"]` populated
- [ ] `curl -s http://localhost:9101/metrics | grep k2_6_openrouter` returns ≥1 counter
- [ ] Any hardcoded backend list in `prometheus.py` or `metrics.py` is replaced by dynamic enumeration
- [ ] Change (if any) committed with message: `fix(metrics): dynamic backend enumeration for K2.6 tiers`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
source .env

# Seed some traffic
for q in "hi" "write a haiku about disks" "what is 2+2" "list 3 colors"; do
  python3 -m aicp.cli.main run --backend k2_6_openrouter "$q"
done

# Channel 1: JSONL event log
tail -20 "${AICP_LOG_FILE:-$HOME/.aicp/events.jsonl}" | jq 'select(.backend == "k2_6_openrouter")'

# Channel 2: aggregate
python3 -c "
from aicp.core.metrics import aggregate
import json
print(json.dumps(aggregate(count=50)['by_backend'], indent=2))
"

# Channel 3: Prometheus
curl -s http://localhost:9101/metrics | grep k2_6_openrouter
```

## Rollback

If code edits were required to fix hardcoded lists:

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/core/metrics.py aicp/core/prometheus.py
```

## Relationships

- PART OF: [[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T018-register-k2-6-openrouter-instance-in-cli-main|T018-register-k2-6-openrouter-instance-in-cli-main]]

## Backlinks

[[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T018-register-k2-6-openrouter-instance-in-cli-main|T018-register-k2-6-openrouter-instance-in-cli-main]]

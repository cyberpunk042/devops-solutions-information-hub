---
title: "E011 M005 — Routing-Split Metric and Weekly Review Ritual"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 90
progress: 0
stages_completed: [document]
artifacts: []
epic: "E011"
depends_on:
  - "E011-m002"
  - "E011-m004"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-routing-integration-aicp-tiers
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E011-routing-integration-aicp-tiers.md
  - id: aicp-prometheus
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/prometheus.py
  - id: aicp-metrics
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/metrics.py
  - id: aicp-history
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/history.py
tags: [module, p1, e011, aicp, metrics, prometheus, observability, ritual, review]
---

# E011 M005 — Routing-Split Metric and Weekly Review Ritual

## Summary

AICP already emits routing telemetry in three places: JSONL event log (`aicp/core/history.py`), aggregate metrics (`aicp/core/metrics.py`), and Prometheus endpoint (`aicp/core/prometheus.py`). This module (a) confirms the new K2.6 tiers are captured end-to-end, (b) defines the weekly review ritual as a documented standard, and (c) adds a `aicp routing-report` CLI helper that summarizes last-7-day routing-split in one table. The ritual produces input for ongoing tier-threshold tuning and catches tier drift early.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T027 | Verify Prometheus + metrics.aggregate() capture k2_6_* backends | 100% | 0% | draft |
| T028 | Add `aicp routing-report` CLI command (7d rollup) | 85% | 0% | draft |
| T029 | Author wiki/spine/standards/routing-review-ritual.md with checklist | 90% | 0% | draft |

## Dependencies

- **E011 M002** — K2.6 OpenRouter adapter live so real traffic flows through.
- **E011 M004** — circuit-breaker events surfaced in metrics (open/close counts are review input).

## Done When

- [ ] `metrics.aggregate(count=1000)` returns rows that include `k2_6_openrouter` and (when enabled) `k2_6_local` keys under `by_backend`
- [ ] Prometheus endpoint at `:9101/metrics` shows counters with label `backend="k2_6_openrouter"`
- [ ] `aicp routing-report --window 7d` prints a table: backend | requests | share % | total tokens | total cost | avg latency | open events
- [ ] `aicp routing-report --window 7d --format json` returns the same data as JSON (for automation)
- [ ] `wiki/spine/standards/routing-review-ritual.md` exists with: cadence, inputs, red-flag thresholds, what to tune, escalation steps
- [ ] `wiki/log/2026-04-25-*-routing-integration-active.md` log page template created (to be filled on first review)
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Verify existing emission captures K2.6

```bash
cd /home/jfortin/devops-expert-local-ai
# Run a few K2.6 tasks
source .env
for q in "hello" "write a haiku" "what's 2+2" "refactor this function: def f(): pass"; do
  python3 -m aicp.cli.main run --backend k2_6_openrouter "$q"
done

# Inspect JSONL log
tail -20 "${AICP_LOG_FILE:-$HOME/.aicp/events.jsonl}" | jq 'select(.backend | startswith("k2_6"))'

# Inspect Prometheus
curl -s http://localhost:9101/metrics | grep k2_6

# Inspect aggregate
python3 -c "
from aicp.core.metrics import aggregate
import json; print(json.dumps(aggregate(count=50), indent=2))
"
```

If any of the three paths is missing K2.6, grep the emission site (search for hardcoded backend names) and add the new keys.

### Step 2 — Implement `aicp routing-report` CLI

New file or extension in `aicp/cli/main.py`:

```python
@app.command("routing-report")
def routing_report(
    window: str = typer.Option("7d", help="Time window: 1d, 7d, 30d"),
    format: str = typer.Option("table", help="Output: table|json"),
):
    from aicp.core.metrics import aggregate_window
    data = aggregate_window(window)  # returns dict keyed by backend with requests/tokens/cost/latency/open_events

    if format == "json":
        typer.echo(json.dumps(data, indent=2))
        return

    # Table
    total_requests = sum(v["requests"] for v in data["by_backend"].values())
    headers = ["Backend", "Requests", "Share", "Tokens", "Cost (USD)", "Avg Latency (ms)", "Breaker Opens"]
    rows = []
    for backend, v in sorted(data["by_backend"].items(), key=lambda kv: -kv[1]["requests"]):
        share = (v["requests"] / total_requests * 100) if total_requests else 0
        rows.append([
            backend, v["requests"], f"{share:.1f}%",
            v["tokens"], f"${v['cost_usd']:.4f}",
            f"{v['avg_latency_ms']:.0f}",
            v.get("breaker_opens", 0),
        ])
    print(tabulate(rows, headers=headers))
```

If `aggregate_window(window)` doesn't exist, add it to `aicp/core/metrics.py` — walk the JSONL log, filter by timestamp.

### Step 3 — Author the ritual standard

Create `wiki/spine/standards/routing-review-ritual.md` with this outline:

```markdown
---
title: "AICP Routing Review Ritual"
type: standard
domain: reliability
status: growing
tags: [standard, aicp, routing, ritual, weekly]
---

# AICP Routing Review Ritual

## Cadence
Every Monday 9am (or at start of operator's weekly planning block).

## Inputs
- `aicp routing-report --window 7d`
- Cost dashboard (OpenRouter web UI)
- `grep -c "breaker.*OPEN" $AICP_LOG_FILE`

## Review checklist
1. [ ] Does k2_6_openrouter share match expected band (>60% of agentic/coding)?
2. [ ] Any tier capturing <5% that was expected to carry real load?
3. [ ] Did any breaker open >3 times this week? (flag for reliability follow-up)
4. [ ] Total cost trend — inside daily/weekly budget?
5. [ ] Any tasks routed to `claude` (Anthropic-direct) that should have landed on K2.6?

## Red-flag thresholds
| Signal | Threshold | Action |
|--------|-----------|--------|
| claude share | >5% of total | Investigate complexity scorer — why so high? |
| k2_6_openrouter share | <40% of agentic | Scorer tuning; bands may need widening |
| breaker_opens(k2_6_openrouter) | >10 / week | Network stability issue or OpenRouter degradation |
| avg_latency(k2_6_local) | >60s | KTransformers tuning (see E008 M003) |

## What to tune
- `router.complexity_thresholds` (widen/narrow K2.6 bands)
- `circuit_breaker.per_backend.<name>` (reliability)
- `backends.<name>.timeout` (latency tolerance)

## Escalation
If three consecutive weeks show cost drift >20% or quality degradation, open a follow-up epic.
```

### Step 4 — Log template for first review

Create `wiki/log/2026-04-29-routing-integration-first-week.md` (or whichever date is 7 days after M002 lands) as a stub operator fills in.

## Rollback

Metrics are additive; rollback just removes the CLI command and standards doc. No data loss.

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/cli/main.py aicp/core/metrics.py
# In wiki repo:
# git checkout -- wiki/spine/standards/routing-review-ritual.md
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| `aggregate_window` function may need to be added to metrics.py | code | 2026-04-22 | no | Part of T028 — simple JSONL scan + bucket |
| Review ritual has no operator yet (solo operator today) | ops | 2026-04-22 | no | Self-review; documented cadence ensures it happens even solo |

## Relationships

- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
- DEPENDS ON: [[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]

## Backlinks

[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
[[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]

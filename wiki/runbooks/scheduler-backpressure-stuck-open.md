---
title: "Operator runbook — scheduler backpressure stuck open"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-05-20
updated: 2026-05-20
sources:
  - id: avx-plus-plus-dump-2026-05-18
    type: directive
    project: devops-solutions-information-hub
    path: raw/dumps/2026-05-18-the-ultimate-exploitation-of-the-tech-stack-AVX-plus-plus.md
    note: "Source dump lines 18175-18205 (backpressure surfaces + responses)"
  - id: selfdef-sdd-031
    type: internal
    project: selfdef
    path: docs/sdd/031-goldilocks-scheduler.md
    note: "SDD-031 — Goldilocks Scheduler spec"
  - id: selfdef-ms048
    type: internal
    project: selfdef
    path: backlog/milestones/MS048-goldilocks-scheduler-hardware-aware-resource-routing.md
    note: "MS048 R11333-R11362 (backpressure thresholds + hysteresis)"
tags: [runbook, scheduler, backpressure, psi, dcgm, blackwell, ram-pressure, hysteresis, selfdef, ips]
---

# Operator runbook — scheduler backpressure stuck open

## Symptom

One or more backpressure surfaces remain `true` in `selfdefctl scheduler show --json | jq .recent_decisions[0].backpressure` for ≥ 5 minutes after the originating resource pressure has cleared.

OR `selfdefctl trio` shows scheduler `[BACKPRESSURE ]` aggregate persistently.

## Why this matters

Per dump lines 18175-18205 + MS048 R11275-R11280, each backpressure surface triggers a specific response policy:

| Surface | Response (verbatim dump) |
|---|---|
| Blackwell VRAM high | reduce context, evict low-value KV, switch smaller oracle |
| 3090 busy | reduce branch width, use CPU classifiers |
| CPU pressure high | defer background indexing/evals |
| RAM pressure high | hibernate branches, compact memory |
| IO pressure high | delay cold scans, avoid large snapshots |
| Human gate queue high | batch approvals, lower autonomy |

When a surface is stuck open beyond its source pressure clearing, the scheduler is **degrading routing without need** — slower inference, missed Blackwell oracle calls, deferred indexing, etc. The operator's perceived AI workstation throughput drops without explanation.

Hysteresis is designed (R11357, `HYSTERESIS_MARGIN = 0.10`) so a surface that entered pressure at threshold X stays open until value drops below `X - 0.10`. A stuck-open surface means either:

1. The source measurement IS still above `threshold - hysteresis` (real persistent pressure)
2. The source-of-measurement (PSI / DCGM / human-gate-tracker) is wedged
3. The threshold or hysteresis was operator-tuned too tight

## Diagnosis

```bash
# 1. Which surfaces are stuck open?
selfdefctl scheduler show --json | python3 -c '
import json, sys
d = json.load(sys.stdin)
if not d["recent_decisions"]:
    print("no decisions yet")
    sys.exit(0)
bp = d["recent_decisions"][0]["backpressure"]
for k, v in bp.items():
    flag = "OPEN" if v else "clean"
    print(f"  {flag:<5} {k}")'

# 2. What does the kernel actually measure?
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io

# 3. What does DCGM see for GPU utilization?
nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv,noheader 2>/dev/null
# Or DCGM CLI:
dcgmi dmon -c 1 -e 252,253 2>/dev/null

# 4. What's the human-gate queue depth?
# (Tracked internally by selfdefd's authority dispatcher; surfaced
#  through MS027 traces — query the latest trace span)
journalctl -u selfdefd -n 100 | grep human_gate_queue_depth
```

## Common stuck-open patterns

### Pattern A — Blackwell VRAM stuck high but no model running

```bash
nvidia-smi --query-gpu=memory.used --format=csv,noheader
```

If a process holds VRAM but no inference is active, it's a leaked allocation. Identify the process:

```bash
fuser /dev/nvidia0 /dev/nvidiactl 2>/dev/null
```

Restart the leaking process; the scheduler's hysteresis will let the surface clear on the next decision after VRAM drops below 80%.

### Pattern B — CPU PSI stuck high

```bash
# Find the noisy process.
ps auxf | sort -rk 3 | head -5
top -bn1 | head -20
```

If a known-noisy workload is running (a batch index, a one-off compile), let it complete. If it's runaway, kill it.

### Pattern C — RAM PSI stuck high after the trigger workload ended

```bash
free -h
cat /proc/meminfo | grep -E "^(MemTotal|MemFree|Buffers|Cached|SwapCached)"
```

If buffers/cache are high but actual memory is fine, the PSI signal can lag. Wait 1-2 minutes for PSI to decay. If still stuck after 5 minutes, the threshold/hysteresis pair may be too tight for the workload pattern.

### Pattern D — Human gate queue high but no pending approvals

```bash
# The human-gate queue is tracked by selfdefd; if it disagrees with
# reality, the tracker may have lost an approval-completed signal.
journalctl -u selfdefd -n 200 | grep -i "human.*gate"
```

If the tracker is wedged, restart selfdefd:

```bash
sudo systemctl restart selfdefd
```

The scheduler will see a 0 queue depth on the next sample.

## Recovery procedure (per-surface)

### Blackwell VRAM stuck

```bash
# 1. Find what's holding VRAM.
nvidia-smi
# 2. If it's a leaked process, restart the holder.
# 3. If it's the inference daemon overcommitted, reduce its max_tokens budget in config.
# 4. Verify the scheduler sees the clean state:
sleep 30
selfdefctl scheduler show --json | jq .recent_decisions[0].backpressure.blackwell_vram_high
```

### CPU / RAM / IO PSI stuck

```bash
# 1. Identify the workload causing it (Diagnosis step 2).
# 2. Either let it complete or terminate it.
# 3. Verify scheduler sees clean state.
```

### Human gate queue stuck

```bash
# 1. Verify pending count.
journalctl -u selfdefd -n 200 | grep human_gate_queue_depth | tail -5
# 2. If wedged, restart selfdefd (the scheduler reads queue depth on each decision).
sudo systemctl restart selfdefd
```

## Operator decision tree

- **Threshold tuned too tight**: edit `/etc/selfdef/scheduler.toml` (operator action; MS003 multi-sig required for production-tier values per R11353). Lower threshold values reduce false positives but also reduce safety margin.
- **Multiple surfaces stuck open simultaneously**: real overload. Don't tune away — investigate the root cause. The Goldilocks scheduler's job is to surface this.
- **Stuck-open after a kernel/driver upgrade**: PSI or DCGM may have changed semantics. Compare /proc/pressure/* before/after and the DCGM version.
- **One surface stuck open intermittently for years**: there's a measurement bug. Capture a 1-hour PSI/DCGM trace and file an issue.

## Relationships

### Cross-references

- SDD-031 §Deliverable 2 (BackpressureMonitor + hysteresis logic)
- MS048 R11333-R11362 (backpressure thresholds + hysteresis)
- Sister runbook: [scheduler-not-running](scheduler-not-running.md)
- Sister runbook: [scheduler-weight-matrix-rotation](scheduler-weight-matrix-rotation.md) (related operator-tuning surface)
- Upstream: [friction-audit-memory](friction-audit-memory.md) (RAM pressure root cause)

---
title: "Per-Day JSONL Dead-Letter Queue with Retry Budget and Status Tracking"
aliases:
  - "Per-Day JSONL Dead-Letter Queue with Retry Budget and Status Tracking"
  - "Per-Day JSONL DLQ with Retry Budget"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: seed
derived_from:
  - model-quality-failure-prevention
  - per-backend-circuit-breaker-with-failover-chain
instances:
  - page: "AICP controller failure path (aicp/core/controller.py lines 487-499)"
    context: "When breaker + failover chain exhaust, controller calls `dlq.enqueue()` with full task context (prompt, mode, backend, project, error, failover_chain). Enqueue happens inside the except clause; DLQ failures don't mask the original exception — it still re-raises after persistence."
  - page: "AICP CLI `--retry-dlq` + MCP `dlq_status` tool"
    context: "Two invocation surfaces on one store. Human: `aicp --retry-dlq` invokes `dlq.retry_pending(controller, max_items=10)`. Agent: MCP `dlq_status` polling. Same `~/.aicp/dlq/` files; different callers."
  - page: "AICP reliable profile (config/profiles/reliable.yaml)"
    context: "Production-leaning overrides — `dlq.max_retries: 5` vs default 3; reduced `retry_delay_seconds`. Same DLQ code path, different operational policy. Profile bundles this with breaker + warmup + reports."
created: 2026-04-19
updated: 2026-04-19
sources:
  - id: aicp-dlq
    type: file
    file: aicp/core/dlq.py
    description: "260-line implementation — enqueue/list_entries/count/retry_pending/_prune_oldest/_mark_entry/status; per-day JSONL files in ~/.aicp/dlq/ keyed by UTC date (AICP project)"
  - id: aicp-controller-failure-path
    type: file
    file: aicp/core/controller.py
    description: "Lines 487-499 — DLQ persistence inside except clause AFTER failover exhaustion; original error still propagates upstream after DLQ write (AICP project)"
  - id: aicp-contribution-staging
    type: wiki
    file: raw/articles/from-aicp/patterns/01_drafts/per-day-jsonl-dlq-with-retry-budget.md
    description: "AICP's original submission, 2026-04-19 staged in raw/ before ingestion here"
tags: [pattern, reliability, dlq, dead-letter-queue, persistence, retry, jsonl, aicp, transferable]
contributed_by: "aicp"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-19"
contribution_status: accepted
---

# Per-Day JSONL Dead-Letter Queue with Retry Budget and Status Tracking

## Summary

When a layered reliability stack (per-backend circuit breakers → failover chain → final fallback) can still fail end-to-end — every backend in the chain is unavailable, or the failure is structurally irrecoverable in the moment — the workload that triggered the cascade is about to be LOST unless something captures it. AICP's pattern: **append a JSONL line per failed task to `~/.aicp/dlq/<UTC-date>.jsonl`** with full reconstruction context (prompt, mode, backend, project_path, error, failover_chain attempted, retry_count starting at 0, status="pending", timestamp). One file per UTC date (auto-rotation implicit in filename), append-only writes (no locks for single-writer), per-line independent JSON (corrupt lines don't poison the file). Retry is a separate operator-invoked or scheduler-invoked operation: `retry_pending()` filters by `status=pending` + `retry_count < max_retries` + `now - enqueued_at >= retry_delay_seconds`. A bounded queue (`max_entries`, default 1000) with `_prune_oldest` keeps disk usage bounded. The distinctive choice is per-day JSONL files over a single growing file or database: rotation implicit, archival is `tar`, querying is `tail`, operators can edit directly — no schema, no DB, no daemon.

> [!info] Pattern Reference Card
>
> | Component | Role | Why this shape |
> |-----------|------|----------------|
> | Per-day file (`<UTC-date>.jsonl`) | Storage with implicit rotation | No rotation daemon; date encoded in filename |
> | Append-only JSONL | Concurrency-safe for single-writer | No locks needed; corrupt line doesn't poison file |
> | Full task context per entry | Faithful retry | prompt + mode + backend + project + failover_chain — no external state |
> | `status` + `retry_count` | Retry history per entry | Status: pending → succeeded/exhausted; count caps at `max_retries` |
> | `enqueued_at` + `retry_delay_seconds` | Tight-loop prevention | Entries eligible only after delay; permits backoff without scheduler |
> | `max_entries` + `_prune_oldest` | Bounded disk usage | Evicts oldest half on overflow (amortized O(1) per insert) |
> | Profile-configurable `dlq.*` | Per-workload tuning | Reliable profile: max_retries=5 vs default 3 |
> | Two invocation surfaces (CLI + MCP) | Operator AND programmatic | `aicp --retry-dlq` for humans; `dlq_status` MCP tool for agents |

## Pattern Description

The pattern captures WORK that would otherwise be lost when the reliability stack exhausts. It is the **third layer** in AICP's reliability composition:

1. **Per-backend circuit breakers** (fast-fail per backend)
2. **Failover chain** (try next backend)
3. **DLQ** (persist when chain exhausts)

Each layer handles a different failure scope. Breaker handles per-backend repeated failure. Failover handles per-request "this one's bad, try another." DLQ handles "the whole chain failed, save for retry." Additive composition; removing any layer leaves a known failure mode uncovered.

## Instances

### Instance 1 — AICP controller failure path

`aicp/core/controller.py` lines 487-499 wrap the entire backend-call-and-failover block in a final except. Inside: write to DLQ via `dlq.enqueue()` with full context, then re-raise the original error. This ordering matters — DLQ captures what the user/agent sees fail; upstream still gets the exception.

### Instance 2 — Two invocation surfaces on one store

`aicp --retry-dlq` (CLI, per CLAUDE.md `## Reliability`) invokes `dlq.retry_pending(controller, max_items=10)`. MCP `dlq_status` tool (per CLAUDE.md `## Intelligent Infrastructure` 11-tool listing) lets fleet agents poll status. Same `~/.aicp/dlq/` store; different readers. The storage shape IS the API.

### Instance 3 — Profile-tunable retry budget

`config/profiles/reliable.yaml` sets `dlq.max_retries: 5` (vs default 3), `dlq.retry_delay_seconds` typically reduced. Same DLQ code; different operational policy. Profile system bundles this with circuit breaker + warmup + reports — operators tune the whole reliability stack with one profile switch.

## Alternatives

### Alternative 1 — SQLite DLQ table

Store entries with indexes (backend, status, retry_count).

> [!warning] Rejected: adds dependency for what is fundamentally an append log + occasional scan. Gives indexed queries (real) but adds schema migrations, connection management, `.db` operators can't `cat`/`grep` (regression). Query patterns AICP uses (most-recent-first, count-by-status, filter-by-delay) are well-served by linear scans capped at 1000 entries.

### Alternative 2 — Single growing JSONL file (no rotation)

`dlq.jsonl` grows forever or until manually truncated.

> [!warning] Rejected: rotation is the operationally-expensive part. Per-day files: archival is `mv 2026-04-12.jsonl /backup/`. Single file: rotation needs logrotate-style mechanism, copy-then-truncate races. Per-day also lets operators answer "what failed yesterday?" with `cat` + `jq`.

### Alternative 3 — In-memory ring buffer (no persistence)

Deque in the controller process. No disk.

> [!warning] Rejected: defeats the point. Process restart loses the queue. AICP controllers restart during config reload, OOM, stuck-watchdog recovery. A DLQ that loses entries on restart is WORSE than no DLQ — operators expect persistence.

### Alternative 4 — Real message queue (Redis Streams / Kafka / RabbitMQ)

Purpose-built queue with consumer groups, ack/nack, exactly-once.

> [!warning] Rejected at current scale: correct for high-throughput multi-consumer. AICP's DLQ throughput is "occasional failure" — single-digit per day normal, dozens during outage. Redis operational cost (process, port, persistence, AOF) dwarfs benefit. Migration is straightforward since entry shape is JSON — revisit when AICP scales to multi-process fleet operation.

### Alternative 5 — Re-raise without persistence

Don't capture. Caller deals with it.

> [!warning] Rejected: fine for interactive CLI, breaks for automated invocation. Fleet agents calling AICP via MCP can't re-type a prompt. Centralizing persistence in AICP gives every caller the same durability guarantee without coordination.

## When To Apply

Use when ALL apply:

1. **Bounded, replayable workloads** — each unit has finite context serializable and re-runnable (AI inference: prompt + mode + project — fits; streaming sessions — don't)
2. **Reliability stack already exists** handling common-case retries. DLQ catches what the stack missed; not the first line of defense
3. **Single-writer or coordinated multi-writer** — append-only JSONL is safe for one writer per file
4. **Operators want to inspect / surgically edit** the failed-work store — JSONL is `cat`/`grep`/`jq`-able

## When Not To

- **Real high-throughput** (>100 failed tasks/sec) — JSONL becomes hot file; use Redis Streams / Kafka
- **Strong ordering / exactly-once** — JSONL doesn't enforce ordering across files; retry doesn't dedupe across runs
- **Multi-process writers without coordination** — race conditions on append are possible; use a real queue

## Tradeoffs

- **+** Durability across process restarts, OOMs, container redeploys
- **+** No external dependencies (no Redis, no DB, no daemon)
- **+** Operator-inspectable with standard tools (`cat`, `grep`, `jq`, `tail`)
- **+** Per-line independence — corruption local, not catastrophic
- **+** Two retry surfaces (CLI + MCP) on one store — stable contract
- **−** No indexing — "all entries for backend X" requires scan (OK at <1000; broken at 10K+)
- **−** Single-writer assumption — multi-process writers would race on append
- **−** Retry counter is best-effort — `_mark_entry` rewrites whole file; crash mid-rewrite could lose the file
- **−** No exactly-once — successful retry that crashes before `_mark_entry` will retry again. Workloads must tolerate at-least-once
- **−** Bounded queue silently drops oldest on overflow. High-failure scenarios lose oldest history

## Detection / Measurement

- **`dlq.count()`** — total entries on disk. Healthy = near-zero. Sustained growth = upstream failure not addressed
- **`dlq.status()`** — pending/succeeded/exhausted ratios. High `exhausted` = real failures (not transient); investigate root cause
- **Time-since-oldest-pending** — >24h = retries not running (broken scheduler or operator forgot `--retry-dlq`)
- **Exhausted count crossing alert threshold** — wire to ntfy/Prometheus. Class of work structurally unable to complete; human triage
- **DLQ growth rate during incidents** — should spike during outage, decay after recovery as retries clear. Flat-high post-recovery = retries not being invoked

## Relationships

- BUILDS ON: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] (durability + graceful-degradation principles)
- COMPLEMENTS: [[per-backend-circuit-breaker-with-failover-chain|Per-Backend Circuit Breaker with Failover Chain]] (DLQ is the third layer in the reliability stack)
- COMPLEMENTS: [[profile-as-coordination-bundle|Profile as Coordination Bundle]] (`dlq.*` settings are part of the profile-switched reliability stack)

## Backlinks

[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[per-backend-circuit-breaker-with-failover-chain|Per-Backend Circuit Breaker with Failover Chain]]
[[profile-as-coordination-bundle|Profile as Coordination Bundle]]

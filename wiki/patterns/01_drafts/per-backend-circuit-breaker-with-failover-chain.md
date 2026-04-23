---
title: "Per-Backend Three-State Circuit Breaker with Failover-Chain Integration"
aliases:
  - "Per-Backend Three-State Circuit Breaker with Failover-Chain Integration"
  - "Per-Backend Circuit Breaker with Failover Chain"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - model-quality-failure-prevention
  - profile-as-coordination-bundle
instances:
  - page: "AICP controller failover (aicp/core/controller.py)"
    context: "Per-backend CircuitBreaker instances built once at controller init via `build_breakers()`; wrapped around `backend.execute()` at call time; `CircuitBreakerOpen` caught alongside generic Exception → enters failover chain (local → fleet → openrouter → claude). Breaker doesn't fight failover — it short-circuits the timeout wait so failover triggers in milliseconds."
  - page: "AICP reliable profile (config/profiles/reliable.yaml)"
    context: "Aggressive thresholds — `failure_threshold: 2` (vs default 3), `recovery_timeout: 20s` (vs default 30s). Same breaker code, profile-tunable thresholds per workload."
  - page: "AICP DLQ integration"
    context: "When all failover backends fail, controller persists the failed task to JSONL via `dlq.enqueue()` before re-raising. Breaker + failover + DLQ form a three-layer reliability stack — fast-fail per backend, graceful failover across backends, durable persistence when the chain exhausts."
created: 2026-04-19
updated: 2026-04-22
sources:
  - id: aicp-circuit-breaker
    type: file
    file: aicp/core/circuit_breaker.py
    description: "207-line implementation — State enum (CLOSED/OPEN/HALF_OPEN), CircuitBreaker class with thread-safe transitions, build_breakers() factory, CircuitBreakerOpen exception (AICP project)"
  - id: aicp-controller-failover
    type: file
    file: aicp/core/controller.py
    description: "Wires breakers per backend; wraps backend.execute() in breaker.call(); catches CircuitBreakerOpen with generic Exception clause to trigger failover (AICP project)"
  - id: reliable-profile
    type: file
    file: config/profiles/reliable.yaml
    description: "Aggressive breaker config — demonstrates profile-tunable thresholds (AICP project)"
  - id: aicp-contribution-staging
    type: wiki
    file: raw/articles/from-aicp/patterns/01_drafts/per-backend-circuit-breaker-with-failover-chain.md
    description: "AICP's original submission, 2026-04-19 staged in raw/ before ingestion here"
tags: [pattern, reliability, circuit-breaker, failover, backend, state-machine, aicp, transferable]
contributed_by: "aicp"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-19"
contribution_status: accepted
---

# Per-Backend Three-State Circuit Breaker with Failover-Chain Integration

## Summary

When a system orchestrates multiple interchangeable backends behind a failover chain (try local → fleet → cloud → escalation), the failure mode that ruins reliability isn't *individual* backend failure — it's **repeated synchronous waits on a known-bad backend** that block the failover chain from triggering. AICP's circuit-breaker pattern solves this with a per-backend three-state machine (`CLOSED → OPEN → HALF_OPEN`) where backend failures count toward a threshold (default 3 consecutive), tripping OPEN; OPEN raises a specific `CircuitBreakerOpen` exception caught alongside generic exceptions, immediately advancing to the next failover backend; OPEN auto-transitions to HALF_OPEN after `recovery_timeout`; HALF_OPEN allows ONE probe request, and its success/failure decides whether to close (recovered) or re-open. Two non-obvious correctness properties: (a) the breaker raises a distinct exception type but is caught by the same except clause as generic failures — failover doesn't need to know whether the backend slow-failed or fast-failed, only that it failed; (b) the breaker is per-backend, not per-controller — a tripped local breaker doesn't affect the cloud breaker, so failover to a healthy backend works even when one is fully out. Composes with the failover chain and DLQ into a three-layer reliability stack: per-backend fast-fail → cross-backend failover → durable persistence.

> [!info] Pattern Reference Card
>
> | Component | Role | Why it matters |
> |-----------|------|----------------|
> | State machine (CLOSED/OPEN/HALF_OPEN) | Tracks per-backend health | OPEN avoids synchronous-wait; HALF_OPEN avoids permanent abandonment |
> | Per-backend instance | Isolates fault domains | A bad cloud doesn't trip local; a stuck local doesn't trip fleet |
> | `failure_threshold` | Tunable sensitivity | Default 3; reliable profile uses 2 |
> | `recovery_timeout` | Tunable forgiveness | Default 30s; reliable profile uses 20s |
> | `half_open_max` | Prevents thundering herd | Default 1; only one request tests recovery |
> | `CircuitBreakerOpen` exception | Distinguishes fast-fail from slow-fail for diagnostics | Controller catches via generic Exception — same failover path |
> | `breaker.call(fn)` wrapper | Single integration point | Controller wraps `backend.execute()` once |
> | State-change callbacks | Metrics + alerting hooks | Wired to Prometheus for ops visibility |

## Pattern Description

The breaker has only ONE auto-transition: OPEN → HALF_OPEN by elapsed time. All other transitions (CLOSED → OPEN, HALF_OPEN → OPEN, HALF_OPEN → CLOSED) require a request to flow through. The breaker doesn't run a background timer — it acts only when called. This makes the implementation simple (no thread, no scheduler) and correct under low-traffic conditions.

The state machine:
- **CLOSED** → `fn()` → success: count=0; failure: count++. If count ≥ threshold: → OPEN, record `_open_since=now`.
- **OPEN** → check `(now - _open_since) ≥ recovery_timeout`? If yes: → HALF_OPEN. If no: raise `CircuitBreakerOpen`.
- **HALF_OPEN** → if `half_open_active ≥ max`: raise OPEN. Else: increment, run `fn()`. Success: → CLOSED. Failure: → OPEN.

Controller integration shape:

```
breaker = self._breakers[task.backend_name]
try:
    result = breaker.call(lambda: backend.execute(prompt))
except (Exception, CircuitBreakerOpen):
    for fb_name in self.failover_chain:
        if fb_name == task.backend_name: continue
        try: result = backends[fb_name].execute(...); break
        except Exception: continue
    if result is None: enqueue_to_dlq(task)
```

## Instances

### Instance 1 — AICP controller failover

`aicp/core/controller.py` lines 169-171 build per-backend breakers via `build_breakers()`. Lines 432-435 wrap `backend.execute(...)` in `breaker.call(lambda: ...)`. Line 446: `except (Exception, CircuitBreakerOpen) as local_err:` — generic and breaker-specific caught together; recovery action is failover in both cases.

### Instance 2 — AICP `reliable` profile

`config/profiles/reliable.yaml` sets `failure_threshold: 2, recovery_timeout: 20s, half_open_max: 1`. Same code, different config. Reliable workloads trip earlier and probe sooner; default workloads are more permissive. Demonstrates profile-tunable thresholds per workload.

### Instance 3 — Three-layer reliability stack composition

Breaker (per-backend fast-fail) + failover chain (cross-backend try-next) + DLQ (persist when chain exhausts) in sequence in `controller.py` lines 432-499. Each layer handles a different failure scope; stacking is additive. Removing any layer leaves a known failure mode uncovered.

## Alternatives

### Alternative 1 — No breaker, timeouts drive failover

Wrap each backend call in a 60 s timeout; jump to next failover on error.

> [!warning] Rejected: timeouts are necessary but insufficient. The failure mode this prevents is *repeated synchronous timeout waits*: local takes 60 s to time out × 1000 concurrent requests = 60,000 wait-seconds before failover starts. Breaker compresses to: first 3 failures wait 60 s each, subsequent fail-fast in microseconds. Low-traffic: overkill. Multi-agent concurrent: load-bearing.

### Alternative 2 — Single global circuit breaker

One shared breaker for "the system."

> [!warning] Rejected: couples failure domains. If cloud fails 3×, the global breaker trips, blocking local too. Failover chains exist because backends fail INDEPENDENTLY; per-backend breakers preserve that independence.

### Alternative 3 — Closed/open-only (no HALF_OPEN)

Two states. Once OPEN, stay OPEN until manually reset.

> [!warning] Rejected: produces permanent abandonment. Backends recover (LocalAI container restart, network blip, cloud transient outage). Manual reset requires operator intervention for normal recovery. HALF_OPEN's auto-probe after `recovery_timeout` is what makes the pattern operationally hands-off.

### Alternative 4 — Sliding-window rate breaker

Trip on failure RATE over last N requests.

> [!warning] Rejected (deferred): conceptually cleaner but operationally harder to reason about. Consecutive-failure threshold gives a clear "3 in a row → trip" rule debuggable from logs. Sliding-window is sensitive to traffic pattern (low traffic + 1 failure = 100% rate). May revisit at high-concurrency multi-agent fleet scale.

### Alternative 5 — Breaker that hides failures (cached fallback response)

Return a cached value on OPEN. Common in HTTP microservices.

> [!warning] Rejected for AICP: a model response cannot be "approximated" by a cached different model's response without changing correctness. Breaker's job here is to fail fast so failover can CHOOSE a different backend — not substitute fake answers.

## When To Apply

Use when ALL apply:

1. Multiple interchangeable backends exist behind a failover chain (not just primary + spare)
2. Backend failure modes include slow timeouts (not just fast errors)
3. Calls are issued frequently (low-traffic systems may never accumulate threshold during outage)
4. A configurable failover chain exists downstream

## When Not To

- "Backends" are different *operations* on the same backend (read vs write on one DB) — use per-operation timeout instead
- Failures are always fast (refused connections, immediate 4xx) — breaker adds detection latency without saving wait time
- No failover downstream — a tripped breaker with nowhere to go just produces faster errors, not better outcomes

## Tradeoffs

- **+** Failover triggers in microseconds (after threshold), not per-call timeout
- **+** Per-backend isolation preserves failover correctness when individual backends are unhealthy
- **+** Profile-tunable thresholds let operators dial reliability vs permissiveness per workload
- **+** Three-layer composition (breaker + failover + DLQ) covers the full failure spectrum
- **−** Adds detection latency under low-traffic: if you call once a minute, threshold may never accumulate
- **−** Operators must understand the state machine to debug "why is the breaker open?"
- **−** `half_open_max=1` → recovery is single-threaded; slow probe blocks N waiting requests
- **−** Per-backend statefulness is process-resident; horizontal scaling needs sticky routing or shared store

## Detection / Measurement

- **Trip rate** (CLOSED → OPEN transitions/hour/backend): high = unhealthy backend or threshold too tight
- **Recovery rate** (HALF_OPEN → CLOSED): low after trips = `recovery_timeout` too short (probing before recovery)
- **HALF_OPEN re-open rate** (HALF_OPEN → OPEN): high = backend flapping, investigate root cause not threshold
- **DLQ depth**: near-empty = breakers + failover working. Growing = entire chain failing, fix backends not tune breaker

## Relationships

- BUILDS ON: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] (fail-fast over fail-slow principle)
- COMPLEMENTS: [[profile-as-coordination-bundle|Profile as Coordination Bundle]] (breaker thresholds are profile-tunable settings)
- COMPLEMENTS: [[single-active-backend-with-lru-eviction|Single-Active Backend with LRU Eviction]] (when a model swap times out, breaker prevents cascading swap attempts)
- COMPLEMENTS: [[per-day-jsonl-dlq-with-retry-budget|Per-Day JSONL DLQ with Retry Budget]] (DLQ is the third layer when breaker + failover exhaust)

## Backlinks

[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[profile-as-coordination-bundle|Profile as Coordination Bundle]]
[[single-active-backend-with-lru-eviction|Single-Active Backend with LRU Eviction]]
[[per-day-jsonl-dlq-with-retry-budget|Per-Day JSONL DLQ with Retry Budget]]

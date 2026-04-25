---
title: "Provider Pricing Monitoring — Operations Plan"
aliases:
  - "Provider Pricing Monitoring — Operations Plan"
  - "provider-check Operations Plan"
  - "Price Drift Detection"
type: operations-plan
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
priority: P1
created: 2026-04-23
updated: 2026-04-23
sources:
  - id: ai-infra-framework-2026
    type: wiki
    file: wiki/spine/references/ai-infrastructure-decision-framework-2026.md
    description: "Parent framework — the 'Price-monitoring and change-detection' section declared the need; this plan implements it."
  - id: decision-matrix-2026
    type: wiki
    file: wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md
    description: "Consumer — the matrix cites verified cache values; the tool keeps those values honest."
  - id: openrouter-models-api
    type: api-documentation
    url: https://openrouter.ai/api/v1/models
    title: "OpenRouter public models endpoint"
    ingested: 2026-04-23
tags: [operations-plan, monitoring, provider-pricing, openrouter, resilience, infrastructure-over-instructions, p1]
---

# Provider Pricing Monitoring — Operations Plan

## Summary

Turns the framework's declaration "monitor for 20% price changes" into infrastructure. [[tools/provider_check|tools/provider_check.py]] fetches live pricing from OpenRouter's public `/api/v1/models` endpoint, diffs against a cached snapshot at `wiki/config/provider-pricing-cache.json`, and reports material changes. Integrated into the pipeline as `python3 -m tools.pipeline provider-check`. Watchlist currently covers 10 mission-relevant models (verified 2026-04-23 snapshot). Designed to be run **weekly via cron or systemd timer**, or ad-hoc during sessions. When material changes are detected, operator reviews and accepts via `--snapshot` flag — no auto-accept (prevents aspirational cache drift). **The tool enforces Principle 4: the "prices can change" claim in the framework is now verified by infrastructure, not declared.**

## Prerequisites

> [!info] Environment
>
> | Requirement | Status | Action if missing |
> |---|---|---|
> | Python 3.11+ | ✅ operator has | — |
> | Network access to `openrouter.ai` | ✅ | — |
> | Wiki repo cloned + `tools/` importable | ✅ | — |
> | Initial cache snapshot at `wiki/config/provider-pricing-cache.json` | ✅ (created 2026-04-23) | Run `python3 -m tools.pipeline provider-check --snapshot` |

No API key required — OpenRouter's `/api/v1/models` is a public catalog endpoint.

## Steps

### Step 1 — Verify the initial snapshot

```bash
python3 -m tools.pipeline provider-check
```

Expected output on day 1: `No changes ≥ 20% since last snapshot.` — confirms cache matches live data.

### Step 2 — Regular check (weekly recommended)

Same command. Exit code semantics:
- `0` — no material changes (or cache matches)
- `1` — material changes detected (review before accepting)
- `2` — fetch failed / cache missing / usage error

### Step 3 — Review and accept changes

When step 2 reports changes:
1. Read the change list (which models, which fields, % delta)
2. Cross-check against [[ai-model-provider-harness-decision-matrix-2026|decision matrix]] — are any rows affected enough to shift routing defaults?
3. If changes are acceptable drift (minor re-pricing within tier), accept:
   ```bash
   python3 -m tools.pipeline provider-check --snapshot
   ```
4. If changes warrant routing updates (>30% shift, model disappearance, new model landing), ALSO update the decision matrix page + AICP `tier_map` before accepting the new baseline.

### Step 4 — Optional automation

Deploy as a periodic check via systemd user timer:

```ini
# ~/.config/systemd/user/wiki-provider-check.service
[Unit]
Description=Wiki provider pricing check

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 -m tools.pipeline provider-check
WorkingDirectory=/home/jfortin/devops-solutions-information-hub
StandardOutput=journal
```

```ini
# ~/.config/systemd/user/wiki-provider-check.timer
[Unit]
Description=Weekly wiki provider pricing check

[Timer]
OnCalendar=weekly
Persistent=true

[Install]
WantedBy=timers.target
```

Enable: `systemctl --user enable --now wiki-provider-check.timer`. Check with `journalctl --user -u wiki-provider-check`.

### Step 4b — Liveness / availability check

In addition to pricing diff, the tool supports a **provider-health check** that pings each of 11 mission-relevant providers and reports whether they respond:

```bash
python3 -m tools.pipeline provider-check --health
```

Expected output: `Provider Health Check — 11/11 providers reachable` with per-provider status, latency, and auth-required notes. A 401 or 403 status is **good** (means "server alive, authentication required" — correct for unauthenticated liveness probes). Only 404, 5xx, or timeouts indicate a genuine outage.

Providers covered: **OpenRouter, OpenAI, Anthropic, Groq, Cerebras, Together, Google AI, DeepSeek, Moonshot, Z.ai, Ollama Cloud**.

Exit codes for `--health`:
- `0` — all providers alive
- `1` — one or more providers unreachable (review the output to identify which)

Combine with pricing check in a weekly script:
```bash
python3 -m tools.pipeline provider-check --health && python3 -m tools.pipeline provider-check
```

### Step 5 — Extending the watchlist

Edit `MODEL_WATCHLIST` in [tools/provider_check.py](tools/provider_check.py) to add/remove models. Any model ID that appears in OpenRouter's catalog works (check with their models endpoint). Run `--snapshot` after editing to incorporate new models into the cache.

## Rollback

- **Revert the cache**: `git checkout wiki/config/provider-pricing-cache.json` — returns to last-committed snapshot
- **Remove the systemd timer**: `systemctl --user disable --now wiki-provider-check.timer`
- **Remove the tool entirely**: delete `tools/provider_check.py` and the `provider-check` entry in `tools/pipeline.py` — no other code depends on it

## Completion Criteria

1. **Tool runs idempotently** — two successive runs without `--snapshot` both report "no changes" ✅ (verified 2026-04-23)
2. **Cache captured for 10 mission-watchlist models** ✅ (verified 2026-04-23; DeepSeek V3 + Gemini 3.1 Pro need correct OpenRouter IDs looked up and added)
3. **Pipeline subcommand wired** — `pipeline provider-check` works ✅ (verified 2026-04-23)
4. **Decision matrix reflects verified numbers** ✅ (updated 2026-04-23 with tool-sourced pricing; K2.6 output corrected to $4.655, Opus OpenRouter corrected to $5/$25)
5. **Periodic execution configured** — systemd timer running or cron entry exists (optional; manual weekly runs acceptable)

## Limitations and next steps

> [!warning] What this tool does NOT do
>
> - **Only covers OpenRouter public pricing** — Anthropic-direct, OpenAI-direct, Moonshot-direct, Ollama Cloud subscription prices require manual verification (their pricing isn't machine-readable from public APIs without scraping).
> - **No free-tier tracking** — Cerebras/Groq/Gemini free-tier allowances aren't in the cache. Manual quarterly review.
> - **No SLA / availability monitoring** — if a provider goes DOWN (not just changes prices), this tool won't detect it. A future `--health` subcommand could add endpoint liveness checks against each provider's `/models` endpoint.
> - **No historical trend** — current cache is a single snapshot. Committing cache changes to git provides history via `git log wiki/config/provider-pricing-cache.json`; a future enhancement could store rolling history.

> [!info] Future enhancements (low priority unless triggered by need)
>
> 1. **Health-check subcommand**: ping each provider's public endpoint with a test model, report latency + availability
> 2. **Direct-API adapters**: fetch pricing for DeepSeek / Z.ai / Moonshot direct pages (needs per-provider scraping logic or their docs APIs)
> 3. **Free-tier allowance tracking**: quarterly manual update prompted by the tool when >90 days since last verification
> 4. **Alert integration**: if running in a fleet context, post to operator's notification channel (OpenArms, IRC, etc.) when material changes detected
> 5. **Snapshot-per-date**: optional `--archive` flag to keep dated historical snapshots for trend analysis

## Mission framing

This tool is a direct implementation of [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]. The framework's "we monitor for 20% price changes" was an aspirational declaration until `tools/provider_check.py` existed. Now it's infrastructure — measurable, enforceable, verifiable by the operator or any future session that runs the command.

Specific implementation alignments:
- **Infrastructure > Instructions** (Principle 1): a script is 100% compliant with "check prices"; an operator remembering to check quarterly is variable compliance
- **Structured Context > Content** (Principle 2): the cache is structured JSON; the diff output is structured and machine-readable via `--json`
- **Declarations Aspirational Until Verified** (Principle 4): every cell in the decision matrix now traces to a cache entry that was once a live API response, not a narrative assertion

## Relationships

- IMPLEMENTS: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] § Price-Monitoring
- FEEDS INTO: [[ai-model-provider-harness-decision-matrix-2026|AI Model × Provider × Harness Decision Matrix 2026]] — tool-verified pricing keeps the matrix honest
- RELATES TO: [[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]] — this tool validates the provider layer
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Aspirational Until Infrastructure Verifies Them]]
- RELATES TO: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions]]

## Backlinks

[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[ai-model-provider-harness-decision-matrix-2026|AI Model × Provider × Harness Decision Matrix 2026]]
[[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Aspirational Until Infrastructure Verifies Them]]
[[Principle — Infrastructure Over Instructions]]

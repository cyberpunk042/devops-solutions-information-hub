---
title: "Flagged pages — Gemini Spark / Gemini Intelligence (Google agent-tier entry, 2026-05-12 + 2026-05-14) requires operator-review update on three existing pages"
type: note
domain: log
status: active
confidence: medium
created: 2026-05-16
updated: 2026-05-16
tags: [research-watch, frontier-delta-2026-05-16, flagged-pages, gemini-spark, gemini-intelligence, google, agent-runtime, vendor-agent-tier, "2026-05-16"]
sources:
  - id: triggering-synthesis-2026-05-16
    type: synthesis
    file: wiki/sources/ai-models/src-gemini-spark-intelligence-google-agent-tier-2026-05-12-14.md
    description: "Triggering source-synthesis page (Gemini Spark + Gemini Intelligence, 2026-05-16) — this flagged-pages log was authored in the same tick."
related_synthesis:
  - wiki/sources/ai-models/src-gemini-spark-intelligence-google-agent-tier-2026-05-12-14.md
---

# Flagged pages — Gemini Spark + Gemini Intelligence

## Summary

Google's 2026-05-12 Android Show announcement of **Gemini Intelligence** + 2026-05-14 9to5Google APK Insight leak of **Gemini Spark** (the agent component inside the Gemini app) brings all three frontier-LLM vendors to parity at the per-vendor consumer-agent-runtime tier (Anthropic Claude Managed Agents · OpenAI ChatGPT agent mode · Google Gemini Spark). This log flags three existing wiki pages whose claims/structure may now be incomplete and surfaces a conditional follow-up tick for post-I/O 2026 keynote (week of 2026-05-19) verification of the Spark leak. No autonomous edits are made to operator-territory pages — flags only.

> [!info] Context
> Triggering synthesis: `wiki/sources/ai-models/src-gemini-spark-intelligence-google-agent-tier-2026-05-12-14.md`
>
> Google formalized its entry into the per-vendor agent-runtime tier on 2026-05-12 (Android Show: "Gemini Intelligence" umbrella) + 2026-05-14 (9to5Google APK Insight teardown surfaced "Gemini Spark" as the agent-component brand). With this, all three frontier-LLM vendors (Anthropic, OpenAI, Google) now have a vendor-branded consumer-agent surface — which makes several existing pages incomplete or out-of-date.
>
> These are FLAGS for operator review. None are auto-modified.

## Affected pages (operator-decides if/how to update)

### 1. `wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md`

**What may be stale:** The decision matrix currently treats model-tier and harness-tier as the principal axes. With Gemini Spark joining Claude Managed Agents (2026-05-07) and ChatGPT agent mode, **per-vendor agent-runtime** is a third axis at the consumer-stack tier — distinct from the infrastructure coding-harness axis (Claude Code / Codex / Gemini CLI / etc.).

**Suggested addendum (operator review):**
- Add a row or column for vendor-agent-runtime tier: Anthropic = Claude Managed Agents, OpenAI = ChatGPT agent mode, Google = Gemini Spark (in Gemini app, OS-integrated on Android)
- Note that the **trust-budget primitive** (agent's autonomous-action authority) is now a per-row evaluation field, with Google explicitly disclosing "may do things like share your info or make purchases without asking" as its launch posture

### 2. `wiki/spine/references/ai-infrastructure-decision-framework-2026.md`

**What may be stale:** Framework's vendor-tier coverage table likely shows Anthropic + OpenAI at the consumer-agent layer but Google blank or partial. Gemini Spark fills the Google cell.

**Suggested addendum (operator review):**
- Update vendor-tier coverage to reflect three-vendor parity at the consumer-agent-runtime tier as of mid-May 2026
- Note OS-level-integration as Google's differentiation bet (vs. Anthropic's agent-loop-sophistication bet of Dreaming + Outcomes + Multiagent Orchestration; vs. OpenAI's consumer-reach bet via default-model-swap GPT-5.5 Instant on 2026-05-05)

### 3. `wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md`

**What may be stale:** The harness landscape (Claude Code, Codex, OpenCode, Aider, Cline, Cursor, Gemini CLI, Continue, Crush, Goose) is correctly the infrastructure-side coding-harness tier. With per-vendor consumer-agent runtimes now firmly distinct (Spark + Managed Agents + ChatGPT agent), the landscape page benefits from an explicit "this page is NOT about the vendor-agent-runtime tier" cross-reference.

**Suggested addendum (operator review):**
- Add a "tier scope" note clarifying this page covers infrastructure-side coding-harnesses (used by engineers in dev environments), not per-vendor consumer-agent runtimes (used by end-users in vendor apps)
- Cross-reference the new Gemini Spark synthesis + the Claude Managed Agents synthesis as the consumer-agent-tier complement

## Conditional follow-up after Google I/O 2026 keynote (week of 2026-05-19)

The Gemini Spark synthesis is currently authored at `confidence: medium` because the agent brand + behavior is APK-teardown + leak, awaiting the I/O 2026 keynote confirmation. Post-I/O (target window 2026-05-19 to 2026-05-23), a follow-up tick should:

- Verify the Gemini Spark name + two-tab Chat/Agent layout + signal pool + experimental warning against the keynote announcement
- Capture any I/O-only reveals: developer-facing Spark API, Agent-to-Agent (A2A) protocol formalization for Gemini 4.0, Gemini 4.0 model-tier announcement if any
- Either update the existing synthesis confidence to `high` with a `verified: 2026-05-XX` field, OR author a follow-up synthesis if the I/O reveal contains material new content beyond the leak

## No autonomous edits made

Per AUTONOMY.md, operator-territory pages (decision frameworks, harness-landscape syntheses already in operator-curated state) are FLAGGED, not modified by this Profile. Operator decides whether to amend, when, and how.

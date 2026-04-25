---
title: "Synthesis — Firecrawl: Web Scraper API for AI Agents (Search · Scrape · Agent · Change-Tracking)"
aliases:
  - "Synthesis — Firecrawl"
  - "Firecrawl — Web Data API"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-25
updated: 2026-04-25
layer: 1
sources:
  - id: src-firecrawl-github-readme
    type: documentation
    url: https://github.com/firecrawl/firecrawl
    file: raw/articles/firecrawlfirecrawl.md
    title: "firecrawl/firecrawl — GitHub Repository"
    ingested: 2026-04-24
tags: [synthesis, firecrawl, web-scraping, ai-agents, mcp-server, fire-1, change-tracking, llmstxt, search-and-scrape, javascript-rendering, agent-skill, self-hosting, agpl, alternative-to-pipeline-fetch, ingestion-tool-comparison]
---

# Synthesis — Firecrawl: Web Scraper API for AI Agents

## Summary

Firecrawl is an **open-source (AGPL-3.0) web scraper API** purpose-built for AI agents — it converts any URL into clean LLM-ready markdown / structured JSON / screenshots, handles JavaScript-heavy pages and proxy rotation transparently, and exposes seven endpoints (`search`, `scrape`, `interact`, `agent`, `crawl`, `map`, `batch-scrape`) plus an MCP server, CLI skill, FIRE-1 action agent, and Change Tracking layer. P95 latency 3.4s, 96% web coverage. Backed by Y Combinator + $14.5M Series A from Nexus Venture Partners (Aug 2025). For this wiki's purposes: **Firecrawl is a candidate alternative or complement to the project's own `tools/pipeline.py fetch` ingestion path** — it solves what the current fetcher cannot (JS rendering, complex anti-bot bypass, autonomous discovery via the Agent endpoint, Change Tracking for source freshness). Trade-off: cloud cost or self-hosted Docker stack (Redis + RabbitMQ + Postgres + Playwright service) vs the current free-and-simple in-process Python fetcher.

> [!info] Source Reference
> | Attribute | Value |
> |---|---|
> | Source | github.com/firecrawl/firecrawl |
> | Type | GitHub repository (deep fetch — README + 30 key files) |
> | License | AGPL-3.0 (core) + MIT (SDKs) |
> | Stars | ~48k+ as of Aug 2025 |
> | Funding | $14.5M Series A (Nexus, Y Combinator, Zapier, Tobias Lütke, Abhinav Asthana, Matt McClure) |
> | Hosted at | firecrawl.dev (paid tiers) |
> | MCP server | `firecrawl-mcp` (npx) |
> | Key claim | "Power AI agents with clean web data — covers 96% of the web including JS-heavy pages, P95 3.4s" |

## Key Insights

### 1. Seven core endpoints, each solving a different agent-data problem

> [!abstract] Endpoint catalog
>
> | Endpoint | What it does | Use when |
> |---|---|---|
> | **Search** | Web search **+ scrape full page content** in one call | Agent needs to find AND read pages — eliminates discover-then-scrape two-step |
> | **Scrape** | URL → markdown / JSON / screenshots | Single-page extraction, the fundamental primitive |
> | **Interact** | Scrape, then send AI prompts that click/scroll/type on the page | Pages behind logins, forms, modals — agent describes intent in natural language |
> | **Agent** | Describe what you need; the AI agent searches, navigates, retrieves — **no URLs required upfront** | Cross-site research, "find the founders of X" type questions |
> | **Crawl** | Scrape every URL of a website (limit-bounded, async) | Documentation ingestion, full-site indexing |
> | **Map** | Discover all URLs on a website instantly (no scraping) | Site audit, discovering scope before deciding what to scrape |
> | **Batch Scrape** | N URLs concurrently | Bulk ingestion of a known URL list |
>
> The **Agent** endpoint is the evolution of the older `/extract` path: faster, more reliable, doesn't require URL knowledge upfront. Two model tiers — `spark-1-mini` (default, 60% cheaper, "most tasks") and `spark-1-pro` (complex research, multi-site comparison, critical accuracy). Pydantic-style schema support for structured output.

### 2. The Agent endpoint with structured-output schema is THE killer feature for wiki ingestion

```python
from firecrawl import Firecrawl
from pydantic import BaseModel, Field

app = Firecrawl(api_key="fc-YOUR_API_KEY")

class Founder(BaseModel):
    name: str
    role: Optional[str]

class FoundersSchema(BaseModel):
    founders: List[Founder]

result = app.agent(
    prompt="Find the founders of Firecrawl",
    schema=FoundersSchema
)
```

Returns:

```json
{
  "founders": [
    {"name": "Eric Ciarla", "role": "Co-founder"},
    {"name": "Nicolas Camara", "role": "Co-founder"},
    {"name": "Caleb Peffer", "role": "Co-founder"}
  ]
}
```

**Wiki implication:** for source-synthesis pages where we want STRUCTURED data (e.g., model benchmark tables, library feature lists, comparison matrices), Firecrawl's schema-driven Agent could replace prompt-the-LLM-after-fetch with prompt-the-fetcher-directly — saving the synthesis-stage LLM cost and reducing extraction errors.

### 3. Engine forcing — domain-aware scraper selection

The `FORCED_ENGINE_DOMAINS` env var maps URL patterns to scraping engines:

```json
{
  "linkedin.com": "playwright",
  "twitter.com": "playwright",
  "*.cloudflare.com": "fire-engine;tlsclient;stealth",
  "wikipedia.org": "fetch",
  "google.com": ["fire-engine;chrome-cdp", "playwright"]
}
```

Available engines: `fire-engine;chrome-cdp` · `fire-engine;tlsclient` · `fire-engine;chrome-cdp;stealth` · `fire-engine;tlsclient;stealth` · `playwright` · `fetch` · `pdf` · `document`. **The list itself is operationally interesting** — it codifies the dominant anti-bot bypass strategies as 2026 (chrome-cdp via Fire-Engine = JS rendering at scale; tlsclient = TLS fingerprint mimicry). Self-hosted instances DO NOT have access to Fire-Engine (cloud-only feature) — this is the practical limit of self-hosting.

### 4. FIRE-1 web action agent — for sites that require interaction

FIRE-1 is Firecrawl's first action agent (April 2025). Activated via:

```json
"agent": {
  "model": "FIRE-1",
  "prompt": "Search for firecrawl and go to the company page."
}
```

It clicks, fills forms, navigates dynamic content. Use cases per the docs: **paginate through product listings · log into walled content · interact with modals**. Available on `/scrape` AND `/extract v2` endpoints. **Cost note:** consumes more credits proportional to interaction complexity.

### 5. /extract v2 + FIRE-1 — structured extraction with navigation

The `/extract v2` endpoint combines:
- JSON Schema → structured output
- FIRE-1 → multi-page navigation
- Built-in search → no URLs required (Search-and-Extract pattern)

Example: extracting forum comments across paginated threads with a single call:

```bash
curl -X POST https://api.firecrawl.dev/v1/extract \
  -d '{
    "urls": ["https://example-forum.com/topic/123"],
    "prompt": "Extract all user comments from this forum thread.",
    "schema": {...},
    "agent": {"model": "FIRE-1"}
  }'
```

**Note:** the older `/llmstxt` and `/deep-research` alpha endpoints have been deprecated (no further updates after June 30, 2025) — replaced by /search and the `firesearch` open-source alternative.

### 6. Change Tracking — automatic detection of website updates

> [!success] **Mission-relevant for the wiki:** Change Tracking solves the staleness problem
>
> Firecrawl compares current scrapes against previous versions (per URL × team_id × markdown format) and returns:
>
> | Field | Values |
> |---|---|
> | `previousScrapeAt` | ISO timestamp or null |
> | `changeStatus` | `new` · `same` · `changed` · `removed` |
> | `visibility` | `visible` (via crawling) or `hidden` (via memory) |
> | `diff` (optional) | Git-style line-by-line diff |
> | `json` (optional) | Structured JSON comparison via custom schema |
>
> Modes: **Git-Diff** (free) and **JSON** (5 credits/page, custom schema for tracking specific fields like prices, times, product details). Resilient to whitespace and content order changes; iframe URLs are ignored to avoid captcha false-positives.
>
> **Wiki application:** the existing `pipeline lint` flags `status: stale` based on raw-vs-page modification time, but cannot detect WHAT changed in the source. Firecrawl's git-diff Change Tracking would tell us "this paragraph was rewritten" — direct input to the [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]'s "should this evolved page be re-derived?" decision.

### 7. CLI skill + MCP server — designed for first-class agent integration

Two installation paths give an agent immediate access:

**Skill (works with Claude Code, Antigravity, OpenCode):**
```bash
npx -y firecrawl-cli@latest init --all --browser
```

**MCP (any MCP-compatible client):**
```json
{
  "mcpServers": {
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {"FIRECRAWL_API_KEY": "fc-YOUR_API_KEY"}
    }
  }
}
```

**Agent-onboarding hook:**
```bash
curl -s https://firecrawl.dev/agent-onboarding/SKILL.md
```

The agent can fetch its own onboarding skill, sign up the user, and bootstrap with an API key autonomously. This pattern — **tool-self-onboarding-via-skill-fetch** — is novel and worth tracking as a meta-pattern (see Open Questions below).

### 8. Multi-language SDK coverage

Official SDKs: **Python**, **Node.js**, **Java** (Gradle/Maven), **Elixir**, **Rust**. Community: **Go**. All SDKs handle async polling automatically (call `app.crawl(url, limit=50)`, get back full results without manual job-status loops). The Python SDK was overhauled (Apr 2025) for async support + named parameters + return types. The Rust SDK gained batch scraping, crawl cancellation, and `llms.txt` generation.

### 9. Self-hosting — Docker Compose stack with caveats

> [!warning] Self-hosted limitations
>
> Self-hosted instances **do NOT have access to Fire-Engine** (the cloud-only stealth/JS-bypass engine). Self-hosted = playwright + fetch + pdf engines only. For sites with strict anti-bot or heavy JS, self-hosting hits walls the cloud version doesn't.
>
> **Required services (Docker Compose):**
> - Redis (queueing + rate-limit storage)
> - RabbitMQ (NuQ queue worker coordination)
> - PostgreSQL (`nuq-postgres` — queueing DB, NOT user data)
> - Playwright service (browser-as-a-service for JS rendering)
> - API server + worker pool (4 CPU, 8 GB RAM recommended per `docker-compose.yaml`)
>
> Each service has resource limits in the compose file (api: 4 CPU / 8GB; playwright: 2 CPU / 4GB). Total minimum: ~6 CPU + 12+ GB RAM. **This is a non-trivial infra commitment** — comparable to running a small fleet, not a side daemon.
>
> Kubernetes Helm chart available for production-grade deployment (`examples/kubernetes/firecrawl-helm/`) with separate deployments for api / extract-worker / nuq-worker / nuq-prefetch-worker / nuq-postgres / playwright / rabbitmq.

### 10. Pricing model — credits, with mode-specific rates

Cloud pricing is credit-based; rates vary per operation:
- Basic scraping/crawling: 1 credit/page
- JSON Change Tracking mode: **5 credits/page** (additional LLM processing)
- FIRE-1 actions: variable, proportional to interaction depth
- Agent endpoint: model-dependent (`spark-1-mini` 60% cheaper than `spark-1-pro`)

For the wiki's volume (~6 raws/session × few sessions/week = <100 fetches/week), even cloud Firecrawl is likely <$10/month — far below the operator's API budget threshold for the post-Anthropic stack. Self-hosting only makes sense if the wiki ingestion volume scales to thousands/week OR if data-residency / compliance concerns are present.

### 11. Industry adoption signal

Customers cited in the Series A blog post: **Zapier · Shopify · Replit · top hedge funds**. Tobias Lütke (Shopify CEO) is an investor. Zapier integrated Firecrawl in "a single afternoon." 350,000+ developers signed up. 15× growth in past year. **This is a market-leader signal**, not a niche tool — adoption data this strong implies a stable API surface and continued maintenance.

## Open Questions

> [!question] Should the wiki adopt Firecrawl as the default fetcher, or keep `tools/ingest.py`?
> The current fetcher (in-process Python with youtube-transcript-api, GitHub README scrape, arxiv-aware PDF) is free, simple, and integrated. Firecrawl adds JS rendering, anti-bot bypass, Change Tracking, structured extraction. The decision needs:
>
> | Dimension | Current `tools/ingest.py` | Firecrawl |
> |---|---|---|
> | Cost | $0 (in-process) | ~$5-10/month at wiki volume (cloud) OR ~6 CPU + 12GB RAM (self-hosted) |
> | JS-heavy pages | Fails | Handles |
> | Schema-driven extraction | Manual (LLM after fetch) | Built-in via Pydantic schema |
> | Change tracking | None | Git-diff or JSON |
> | Maintenance | Project-internal | External dependency |
> | Operator effort to integrate | None (status quo) | New tools/firecrawl_fetch.py wrapper + API key management |
>
> Requires: operator decision; could be tested as `pipeline fetch --engine firecrawl <url>` opt-in. ADR candidate.

> [!question] Does the agent-self-onboarding-via-SKILL.md pattern generalize?
> Firecrawl's `curl -s https://firecrawl.dev/agent-onboarding/SKILL.md` is a novel meta-pattern: a remote skill that any AI agent can fetch and immediately become a Firecrawl-using agent (via API-key signup flow embedded in the skill). Could the wiki publish a similar `wiki-onboarding/SKILL.md` for sister projects? Connects to the [[model-skills-commands-hooks|Skills, Commands, and Hooks]] model and the dual-scope principle. Requires: design exploration.

> [!question] What about the deprecated /llmstxt — does the wiki need llms.txt output?
> Firecrawl deprecated `/llmstxt` in June 2025, redirecting to `firesearch` and `create-llmstxt-py`. The wiki currently does NOT generate `llms.txt` — should it, for consumption by sister projects' AI agents? Requires: assess whether AICP / OpenFleet would benefit from a wiki-published llms-full.txt.

## Relationships

- DERIVED FROM: [[src-firecrawl-github-readme|Firecrawl GitHub README]]
- COMPARES TO: [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]] (Firecrawl ships BOTH MCP and CLI; relevant to the choice framework)
- RELATES TO: [[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
- RELATES TO: [[model-automation-pipelines|Model — Automation and Pipelines]]
- RELATES TO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]
- RELATES TO: [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]] (the depth-verification rule applies; Firecrawl's structured extraction reduces but doesn't eliminate the rule)
- FEEDS INTO: [[model-llm-wiki|Model — LLM Wiki]] (potential ingestion-layer enhancement)
- FEEDS INTO: [[model-knowledge-evolution|Model — Knowledge Evolution]] (Change Tracking → staleness detection)

## Backlinks

[[Firecrawl GitHub README]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
[[model-automation-pipelines|Model — Automation and Pipelines]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
[[model-llm-wiki|Model — LLM Wiki]]
[[model-knowledge-evolution|Model — Knowledge Evolution]]

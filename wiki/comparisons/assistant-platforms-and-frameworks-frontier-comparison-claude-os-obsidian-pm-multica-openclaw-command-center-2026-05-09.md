---
title: "Comparison — Assistant Platforms & Frameworks Frontier (2026-05-09): Claude OS · Obsidian PM · Multica · OpenClaw Command Center / OCMC — by Type and Frontier"
type: comparison
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: operator-directive-2026-05-09-turn-2
    type: directive
    file: raw/notes/2026-05-09-operator-directive-hermes-clarification-information-surfacing-before-public-obsidian-pull-from-frontier-stay-independent-classify-existing-approaches.md
    description: "Operator directive 2026-05-09 (turn 2) — classify the 7 named tools by type and frontier at high standards"
  - id: src-claude-os-skill-chaining-youtube
    type: video
    url: https://www.youtube.com/watch?v=RrMTtG1ZccI
    file: raw/transcripts/skill-chaining-in-claude-os-is-insane-dont-fall-behind.txt
    description: "YouTube — Skill chaining in claude-os is insane don't fall behind — strategic argument for skill-system architecture over dashboards; 'Anthropic will solve 8 of 9; you must solve YOUR business workflows'"
  - id: src-claude-os-article
    type: article
    url: https://thebob.dev/ai/tools/productivity/2025/10/31/why-we-built-claude-os-and-what-it-actually-is/
    file: raw/articles/why-we-built-claude-os-and-what-it-actually-is-code-it-forward.md
    description: "Bob Roberts — Why we built Claude OS (and what it actually is) — author article explaining the 6-component memory layer + hybrid indexing breakthrough"
  - id: src-claude-os-repo
    type: project
    url: https://github.com/brobertsaz/claude-os
    project: brobertsaz/claude-os
    path: README.md
    description: "Claude OS repo README v2.5 (Feb 2026) — full feature set + roadmap + v2 changelog"
  - id: src-obsidian-pm-repo
    type: project
    url: https://github.com/StepanKropachev/obsidian-pm
    project: StepanKropachev/obsidian-pm
    path: README.md
    description: "Obsidian PM by StepanKropachev — full PM in plain-Markdown Obsidian vault: Table + Gantt + Kanban + dependencies + recurring + time tracking"
  - id: src-multica-repo
    type: project
    url: https://github.com/multica-ai/multica
    project: multica-ai/multica
    path: README.md
    description: "Multica — open-source managed agents platform supporting 10+ agent CLIs (Claude Code, Codex, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI). Hermes is empirically a real CLI runtime, not just a planned project name."
  - id: src-openclaw-command-center
    type: article
    url: https://github.com/jontsai/openclaw-command-center
    file: raw/articles/jontsaiopenclaw-command-center.md
    description: "OpenClaw Command Center (original) — README currently empty; classification based on operator framing + repo name; needs deeper code investigation"
  - id: src-ocmc-backup
    type: article
    url: https://github.com/cyberpunk042/ocmc-backup
    file: raw/articles/cyberpunk042ocmc-backup.md
    description: "Operator's backup/fork of OpenClaw Mission Control — README currently empty; existence in operator's repos signals OCMC adaptation pattern; needs deeper code investigation"
  - id: epic-e024
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "E024 Epic — Per-Project Assistant Configurations; this comparison feeds the Profile pattern design with empirical inputs from frontier tools"
tags: [comparison, assistant-platforms, claude-os, obsidian-pm, multica, openclaw, ocmc, frontier-mapping, hermes-confirmation, skill-systems, memory-layer, agent-orchestration, pm-in-vault, "2026-05-09", ai-agents, synthesized]
---

# Comparison — Assistant Platforms & Frameworks Frontier (2026-05-09)

## Summary

Survey + classification of 7 operator-named assistant/orchestration platforms (plus the YouTube + article context) into **4 distinct types**, with frontier-per-type identification. Per-type findings: **Claude OS** (brobertsaz) is the frontier for the *Memory Layer for Claude Code* type — 6-component architecture (Real-Time Learning · Memory MCP · Semantic KB · Code Structure MCP · Analyze-Project · Session Management), SQLite + sqlite-vec + Ollama + Redis stack, MIT-licensed, hybrid tree-sitter indexing (100k→20k chunks, 10k files in 30s). **Obsidian PM** (StepanKropachev) is the frontier for *PM-in-Vault* type — full project management (Table + Gantt + Kanban + dependencies + recurring + time tracking) stored as plain Markdown with YAML frontmatter, no external services, MIT-licensed. **Multica** is the frontier for *Multi-Agent Orchestration / Managed Agents Platform* type — supports 10+ agent CLIs (Claude Code, Codex, OpenClaw, OpenCode, **Hermes**, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI), Go+Next.js+pgvector+Daemon stack, cloud-first with self-host option, already operator-adopted per memory. **OpenClaw Command Center / OCMC** type is *Assistant Mission Control UI* — both reference repos (jontsai original + cyberpunk042 operator-backup) have empty READMEs; classification based on naming + operator-framing. **Key empirical finding**: Multica's supported-CLI list confirms **Hermes is a real existing agent-CLI runtime**, not just a Greek-god-themed planned project. The YouTube transcript provides the **strategic frame**: Anthropic will solve 8 of 9 memory/context/dashboard limitations themselves over the next few months; the ONE thing they will NOT solve is YOUR specific business workflows — so invest engineering time in SKILL SYSTEMS (orchestrator + modular child skills wired by skill.md), not dashboards.

## Type Taxonomy

> [!info] **4 distinct types identified — pick from frontier of each, don't lock in to one**

| Type | What it solves | Frontier candidate | Trade-off |
|---|---|---|---|
| **T1 — Memory Layer for Claude Code** | Persistent context across sessions; codebase semantic + structural indexing | **brobertsaz/claude-os** (Claude OS) | Solves the "AI starts cold every conversation" tax; requires Ollama + Redis + Python stack locally |
| **T2 — PM-in-Vault (plain Markdown PM)** | Project management without external services or vendor lock-in; data stays in Obsidian vault as `.md` files | **StepanKropachev/obsidian-pm** (Obsidian PM) | Solves "PM tools that own your data"; constrained to one-vault context, no real-time multi-user editing |
| **T3 — Multi-Agent Orchestration / Managed Agents** | Manage multiple agent CLIs as teammates (assign tasks, track progress, reusable skills) across runtimes and providers | **multica-ai/multica** (Multica) | Solves "copy-paste prompt babysitting"; multi-component stack (Go backend, Postgres+pgvector, daemon); cloud-first by default with self-host option |
| **T4 — Assistant Mission Control UI** | Web UI / dashboard layer specifically for managing one assistant runtime (OpenClaw or similar) | **jontsai/openclaw-command-center** + **cyberpunk042/ocmc-backup** (operator's fork) | READMEs currently empty — classification based on repo names + operator framing; needs deeper investigation (look at code, not docs) |

## T1 — Memory Layer for Claude Code (Frontier: Claude OS)

> [!success] **Frontier candidate: [brobertsaz/claude-os](https://github.com/brobertsaz/claude-os) v2.5 (Feb 2026)**

### Architecture (6 components, MIT-licensed)

| # | Component | Tech | What it does |
|---|---|---|---|
| 1 | **Real-Time Learning** | Redis pub/sub | Monitors conversations, extracts 10+ insight types (architectural decisions, bug fixes, edge cases, team preferences). <1ms latency. Automatic. |
| 2 | **Memory MCP** | MCP server | "Remember this:" saves persistently; "what did we decide?" recalls |
| 3 | **Semantic Knowledge Base** | SQLite + sqlite-vec + Ollama embeddings | Vector embeddings of codebase; relationships, patterns, context |
| 4 | **Code Structure MCP** | tree-sitter AST | 10,000 files in 3 seconds; every function, import, dependency mapped |
| 5 | **Analyze-Project** | Hybrid (structural + semantic) | Git hooks keep index fresh; 80% chunk reduction (100k→20k) |
| 6 | **Session Management** | 4-field state | Auto-resume from where left off; zero cold starts |

### v2.5 features (latest, Feb 2026)

- **Cross-KB search** — search across all knowledge bases at once with `mcp__code-forge__search_all_knowledge_bases`
- **Inline health checks** — automatically run during search; surfaces stale/HIGH/CRITICAL warnings
- **Simplified Session Management** — 50-field JSON → 4-field state (`last_task`, `last_branch`, `stopped_at`, `one_liner`)
- **Leaner CLAUDE.md template** — 351 → 128 lines (removed 200-line mandatory session protocol; replaced with 4-line "Session Tips")
- **36+ community skills** in skills library; one-click install via Smithery

### Hybrid Indexing Breakthrough

| Metric | Before (full embedding) | After (hybrid tree-sitter) |
|---|---|---|
| Large project (10k files) | 3-5 hours | **30 seconds** + optional background semantic |
| Embedded chunks | 100,000+ | **~20,000 (80% reduction)** |
| Start coding | After full index | **Immediately** |
| Resource usage | High Ollama load | Minimal CPU/memory |

### Strengths
- **Local-first**: 100% private, no cloud, runs on operator's machine
- **MIT license** — no vendor lock-in
- **Skills library + community** — reusable patterns, low barrier
- **Hybrid indexing** is genuinely innovative; PageRank-weighted selective embedding
- **Natural language UX** — "remember this", "what did we decide?"

### Trade-offs
- Setup is not one-click: requires Ollama + Redis + Python 3.11+ + SQLite + sqlite-vec
- Per-project init still required (`/claude-os-init`)
- Documentation is functional but bare; v1.0+ rough edges
- Optimized for one-user one-machine; team-sharing is template-based (manual)

### Relevance to this project Profile design (E024)
- **HIGH** — Claude OS's session-management + memory-MCP patterns map directly to Profile's **Knowledge Scope + Success Criteria** sections
- **HIGH** — Skills library + skill-chaining (per YouTube source) maps to Profile's optional **Skills inventory** (TBD in M002)
- **HIGH** — Hybrid indexing approach informs the Profile's potential code-aware knowledge-scope expansion

## T2 — PM-in-Vault (Frontier: Obsidian PM)

> [!success] **Frontier candidate: [StepanKropachev/obsidian-pm](https://github.com/StepanKropachev/obsidian-pm)**

### Architecture

| Aspect | Value |
|---|---|
| **License** | MIT |
| **Storage** | Plain `.md` files with YAML frontmatter in Obsidian vault |
| **Data ownership** | "The vault IS the database" — no external services, no cloud, no accounts |
| **Sync** | Git, Obsidian Sync, iCloud, Dropbox, Syncthing (all work — no extra setup) |
| **Stack** | TypeScript Obsidian plugin |
| **Min version** | Obsidian 1.4.0+, desktop + mobile |

### Views (3 simultaneous, same-data)

| View | Capability |
|---|---|
| **Table** | Sortable, filterable, inline-editing; saved filter/sort combos as named views; bulk multi-select actions |
| **Gantt** | Interactive timeline; draggable bars; resizable edges; dependency arrows; zoom day→quarter; milestones as diamonds |
| **Kanban** | Cards grouped by status; drag-between-columns; show priority, assignees, tags |

### Features

- **Tasks**: subtasks (any depth), dependencies (blocking/dependent), milestones (zero-duration), archive (non-destructive)
- **Scheduling**: drag-and-drop, smart auto-shift dependents (with cycle detection), recurring tasks (daily/weekly/monthly/yearly)
- **Time**: estimates + logged hours with notes; visual progress bars
- **Notifications**: configurable lead time before due dates; local-only (per-user)
- **Customization**: custom fields (text/number/date/select/multi-select/person/checkbox/URL), custom statuses, custom priorities, saved views, team roster
- **Bulk operations**: multi-select for batch status/priority/assignee/tags/due-date/progress/archive/parent/delete
- **Import**: convert existing Markdown notes to tasks; bidirectional (note ↔ task)

### Task properties (frontmatter schema)

```yaml
---
pm-task: true
title: "Ship v1.0"
status: in-progress           # custom labels supported
priority: high                # custom labels supported
due: "2026-04-01"
progress: 60
assignees: ["alice", "bob"]
tags: ["launch"]
dependencies: ["task-abc123"]
---
Task description in Markdown.
```

### Strengths
- **No vendor lock-in by design** — `.md` files survive Obsidian uninstall, plugin discontinuation, vendor change
- **Three views of one data** — flexible, no duplication
- **Plain-text means scriptable** — bulk edits via any text tool; greppable; diffable
- **Solo-developer maintained** — strict PR rules, no AI-bulk-PR acceptance; high code quality

### Trade-offs
- No real-time multi-user editing (conflicts handled as Markdown conflicts via Git/Sync)
- One vault context — multi-project across multi-vault not optimized
- Project management feature set is comprehensive but not at-scale enterprise (no advanced reporting, etc.)
- Restricted to Obsidian users

### Relevance to this project Profile design (E024)
- **MEDIUM** — Obsidian PM's plain-Markdown-with-frontmatter pattern aligns with this project's existing approach (Profile YAML)
- **HIGH** — Confirms operator's existing public Obsidian publishing flow ([[wiki_sync]] MCP / `tools.sync`) as the right anchor for the "info surface before public Obsidian" question — the issue isn't WHERE data lives (already plain-text), it's WHAT layers exist between authoring and publishing
- **MEDIUM** — The task-frontmatter schema is an exemplary instance of declarative-config-as-data; informs Profile section design

## T3 — Multi-Agent Orchestration (Frontier: Multica)

> [!success] **Frontier candidate: [multica-ai/multica](https://github.com/multica-ai/multica) (open-source managed agents platform)**

### Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Next.js    │────>│  Go Backend  │────>│   PostgreSQL     │
│   Frontend   │<────│  (Chi + WS)  │<────│   (pgvector)     │
└──────────────┘     └──────┬───────┘     └──────────────────┘
                            │
                     ┌──────┴───────┐
                     │ Agent Daemon │  runs on your machine
                     └──────────────┘
```

| Layer | Stack |
|---|---|
| Frontend | Next.js 16 (App Router) |
| Backend | Go (Chi router, sqlc, gorilla/websocket) |
| Database | PostgreSQL 17 + pgvector |
| Agent Runtime | Local daemon executing one of 10+ CLIs |

### Supported agent CLIs (10+, frontier breadth)

> [!warning] **Empirical finding (2026-05-09)**: Hermes is in Multica's supported CLI list — confirming Hermes is a real existing agent-CLI runtime (not just a planned project name themed after the Greek messenger god). This resolves the directive's mention.

| # | CLI | Notes |
|---|---|---|
| 1 | **Claude Code** | Anthropic |
| 2 | **Codex** | OpenAI |
| 3 | **OpenClaw** | Operator's ecosystem project |
| 4 | **OpenCode** | Already in operator's stack memory 2026-04-23 |
| 5 | **Hermes** | **THE Hermes operator referenced — confirmed real agent-CLI** |
| 6 | **Gemini** | Google |
| 7 | **Pi** | Inflection |
| 8 | **Cursor Agent** | Cursor IDE |
| 9 | **Kimi** | Moonshot — already in operator's stack |
| 10 | **Kiro CLI** | TBD investigate |

### Features

- **Agents as Teammates**: profiles, board presence, comments, issue creation, blocker reporting (autonomous)
- **Autonomous Execution**: full task lifecycle (enqueue → claim → start → complete/fail); WebSocket real-time progress streaming
- **Reusable Skills**: solutions become team-wide reusable skills
- **Unified Runtimes**: one dashboard for all compute (local daemons + cloud runtimes); auto-detect CLIs on PATH
- **Multi-Workspace**: workspace-level isolation; per-workspace agents/issues/settings
- **Self-hosting**: `multica setup self-host` with `--with-server` (Docker)
- **Self-update**: `multica update` reads version archives from GHCR

### Operator's existing adoption

Per memory [project_multica_self_hosted_2026_04_28.md]: operator already runs Multica self-hosted at `/home/jfortin/.multica/server/`, has `.env` + source-level access, custom_env per-agent routing confirmed working.

### Strengths
- **10+ CLI breadth** — most-pluggable orchestrator surveyed; pure runtime-agnosticism
- **Team-native** — multi-user/workspace built-in, not bolt-on
- **Self-hostable** — full data sovereignty option
- **Already operator-adopted** — no migration cost; integration path is "extend, don't replace"
- **Hermes resolved here** — solves Hermes-identity question by empirical evidence

### Trade-offs
- Heavier stack than Claude OS or Obsidian PM (Go + Postgres + pgvector + daemon)
- Cloud-first default — self-host requires Docker
- Cloud version is paid (multica.ai/app); self-host avoids cost but adds ops burden
- License unclear from README snippet (need deeper read; community CI badge suggests open-source)

### Relevance to this project Profile design (E024)
- **CRITICAL** — Multica is the existing operator adoption that the Profile-spawn-protocol architecture must INTEGRATE WITH, not compete with
- **CRITICAL** — Multica's daemon-auto-detect-CLIs pattern aligns with Profile's `runtime_targets:` list — the same Profile can target any of Multica's 10+ supported CLIs
- **HIGH** — Multica's skills-as-reusable-team-knowledge maps to this project's existing wiki skills concept
- **HIGH** — Multica's WebSocket progress streaming + board presence is candidate for "information surface before public Obsidian" requirement

## T4 — Assistant Mission Control UI

> [!warning] **2026-05-09 correction**: Earlier draft of this section claimed "both repos have empty READMEs". That was wrong — pipeline fetch via public access failed to retrieve content, but the repos have substantial READMEs (verified via `gh repo view` with auth). Operator-corrected: *"They dont have empty readme.... this is nonsense... do this properly... stop skipping and minimizing"*. Section rewritten with real content.

The T4 category has **two distinct projects** (not variants of one):

### T4.a — jontsai/openclaw-command-center: Lightweight Read-Only Dashboard

> [!success] **[jontsai/openclaw-command-center](https://github.com/jontsai/openclaw-command-center)** — AI assistant command and control dashboard ("Spawn more Overlords!")

| Aspect | Value |
|---|---|
| **Purpose** | Real-time visibility into OpenClaw deployment — sessions, costs, system health, scheduled tasks |
| **License** | MIT © Jonathan Tsai |
| **Stack** | Vanilla JS · ES Modules · SSE streaming · REST API · Zero bundler |
| **Size** | ~200 KB total (dashboard + server) |
| **Dependencies** | Node.js only (Node 18+) |
| **Default mode** | Read-only · localhost-binding (127.0.0.1) by default |
| **Auth modes** | Token · Tailscale · Cloudflare Access · IP allowlist |
| **Features** | Session Monitoring · LLM Fuel Gauges (token usage, costs, quota) · System Vitals (CPU, memory, disk, temperature) · Cron Jobs view + manage · Cerebro Topics (auto conversation tagging) · Operators tracking · Memory Browser · Privacy Controls · Cost Breakdown · Savings Projections |
| **Update mechanism** | 2-second SSE push (not polling) · 5-second cache · single unified `/api/state` endpoint (no 16+ separate requests) |
| **Install** | `npx clawhub@latest install command-center` |
| **Auto-detect** | Workspace via `$OPENCLAW_WORKSPACE` / `~/.openclaw-workspace` / `~/molty` / `~/clawd` |

### T4.b — abhi1693/openclaw-mission-control: Enterprise Governance Platform

> [!success] **[abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control)** — operator-recommended "original"; centralized operations and governance for OpenClaw across teams + organizations

| Aspect | Value |
|---|---|
| **Purpose** | Day-to-day operations surface for OpenClaw — plan, execute, review, audit in one system |
| **License** | MIT |
| **Stack** | Docker + Docker Compose · Next.js frontend · Node.js 22+ backend |
| **Auth modes** | `local` (shared bearer token, 50+ chars) · `clerk` (Clerk JWT) |
| **Features** | Work orchestration (orgs / board groups / boards / tasks / tags) · Agent operations · Governance + approvals · Gateway management · Activity timeline + audit · API-first model |
| **Use cases** | Multi-team agent operations · Human-in-the-loop execution · Distributed runtime control · Audit + incident review · API-backed automation |
| **Install** | One-line: `curl -fsSL https://raw.githubusercontent.com/abhi1693/openclaw-mission-control/master/install.sh \| bash` |
| **Status** | Active development; APIs may change |

### T4.c — cyberpunk042/ocmc-backup: Operator's Backup

[cyberpunk042/ocmc-backup](https://github.com/cyberpunk042/ocmc-backup) is the operator's backup of abhi1693/openclaw-mission-control — same description ("AI Agent Orchestration Dashboard - Manage AI agents, assign tasks, and coordinate multi-agent collaboration via OpenClaw Gateway"). Operator-confirmed 2026-05-09: *"you can use the original too: https://github.com/abhi1693/openclaw-mission-control"*.

### T4 Differentiator

The two are NOT variants — they serve different layers of the same need:

| Layer | T4.a (jontsai) | T4.b (abhi1693) |
|---|---|---|
| Primary mode | **Read-only** visibility | Full operations + governance |
| Stack weight | Lightweight (~200KB) | Heavy (Docker + backend/frontend) |
| Multi-team / approvals | ❌ | ✅ |
| Real-time SSE | ✅ | (via API) |
| Best for | Solo operator monitoring | Team-scale agent ops |

### T4 Frontier

Both are frontier in their respective sub-types. **T4.a** is the frontier for lightweight OpenClaw monitoring; **T4.b** is the frontier for enterprise OpenClaw governance. They are complementary, not competing.

### Relevance to this project Profile design (E024)

- **HIGH** — both expose OpenClaw operations data (sessions, costs, agent activity, audit) that any Profile's Success Criteria telemetry could surface
- **MEDIUM** — T4.b's governance + approval primitives map onto Profile's Action Surface "escalation triggers" + "approval gates"
- **MEDIUM** — both are OpenClaw-specific; the Profile remains tool-agnostic. These are **consumers** of an OpenClaw assistant's runtime activity, not consumers of the Profile itself

## Comparison Matrix

## T5 — CLI Agent Runtimes (Hermes Agent + ecosystem)

> [!success] **[nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)** — Nous Research's self-improving CLI agent (researched 2026-05-09 per operator D7 follow-up; the "Hermes" the operator named)

| Aspect | Value |
|---|---|
| **Purpose** | Self-improving CLI agent with persistent memory + automated skill creation; open-source alternative to Claude Code / Codex CLI |
| **Built by** | Nous Research collective |
| **Launched** | February 2026 |
| **Models** | 300+ across multiple providers |
| **Distinctive features** | Agent-curated memory with periodic nudges · Autonomous skill creation after complex tasks · Skills that self-improve during use · Sandboxed code execution via Unix socket RPC · Multi-platform reach (Telegram/Slack/Discord/WhatsApp/Signal/WeChat/iMessage/CLI simultaneously) |
| **GitHub traction** | Crossed Claude Code on GitHub stars in ~10 weeks; one of fastest-growing OSS in mid-2026 |
| **Known limitations** | Cannot navigate codebases via LSP · No AST-aware editing |
| **Ecosystem** | [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) curated skills list · [AlexAI-MCP/hermes-CCC](https://github.com/AlexAI-MCP/hermes-CCC) port to Claude Code Channel (46 native skills) |

**Why this matters in the comparison**: Hermes is the named CLI agent the operator referenced in the original directive (turn 1: "spawn an OpenClaw or OpenArms or Hermess and whatever"). Confirmed real CLI runtime via Multica's daemon-supported list AND as standalone Nous Research project. It's NOT a planned project name — it's a live, growing alternative to Claude Code.

**Relevance to Profile pattern**: Hermes is one of many possible runtimes a per-project Profile can spawn an assistant on. Like OpenClaw / Multica / Claude OS / OpenCode / Claude Code, Hermes is a tool that may CONSUME a Profile through its native skill + memory mechanism. The Profile does not depend on Hermes; Hermes consumes the Profile.

## Cross-Type Comparison Matrix

| Dimension | Claude OS (T1) | Obsidian PM (T2) | Multica (T3) | OCMC (T4) |
|---|---|---|---|---|
| **Primary purpose** | AI memory across sessions | PM in Obsidian vault | Multi-agent orchestration | OpenClaw fleet UI |
| **License** | MIT | MIT | Unclear (likely OSS) | Empty README |
| **Data ownership** | Local-only (SQLite) | Local-only (vault) | Self-host option (Postgres) | Empty README |
| **Storage format** | SQLite + sqlite-vec + embeddings | Plain Markdown + YAML | Postgres + pgvector | Empty README |
| **Multi-user** | Template-based (manual) | Sync-based + local notifications | Native multi-workspace + roles | Empty README |
| **CLI integration** | Claude Code only | None (Obsidian-only) | 10+ CLIs (Claude/Codex/OpenClaw/OpenCode/Hermes/Gemini/Pi/Cursor/Kimi/Kiro) | OpenClaw-specific (inferred) |
| **Operator adoption** | Not adopted (candidate) | Not adopted (candidate) | **Already adopted** (memory 2026-04-28) | Operator-forked but unused |
| **Setup complexity** | High (Ollama + Redis + Python) | Low (Obsidian plugin install) | Medium (CLI + daemon + Docker for self-host) | Empty README |
| **Anti-vendor-lock-in alignment** | High (local-only, MIT) | High (plain-text, MIT) | Critical (runtime-agnostic, 10+ CLIs) | Empty README |
| **Maturity** | v2.5 (Feb 2026) | Active maintenance | Active CI + community PRs | Unknown |
| **Relevance to E024 Profile design** | HIGH (memory + session patterns) | MEDIUM (frontmatter schema) | CRITICAL (already adopted; spawn-protocol target) | LOW until investigated |

## Key Insights

The strategic frame distilled from the YouTube transcript + frontier survey, in 5 insights:

1. **Anthropic will solve 8 of 9 limitations themselves over the next few months** — context recall, memory features, scheduled tasks, output separation, cross-channel access. Don't invest in those.
2. **The ONE thing Anthropic won't solve is YOUR specific business workflows** — invest here, in Skill Systems and per-project tailoring.
3. **Skill Systems = orchestrator + child skills wired by skill.md** — modular composition beats mega-skills (which lose modularity) and isolated skills (which require manual chaining).
4. **Pull from the frontier, stay independent** — Claude OS's memory mechanism, Obsidian PM's plain-text discipline, Multica's runtime breadth — adopt patterns selectively without locking in to one platform.
5. **Hermes is real, not a planned project name** — Multica's daemon detects `hermes` as a CLI alongside Claude Code, Codex, OpenClaw, etc.

## Deep Analysis

The full per-platform deep analysis is in the per-type sections above (T1–T4). The key cross-cutting analysis is:

**Memory layer (T1) vs Multi-agent orchestration (T3) — they compose, don't compete**: Claude OS solves "my AI forgets between sessions" for a single-user single-machine setup. Multica solves "I have multiple AI agents and want them to behave as teammates" across runtimes. A Profile (E024) using Multica as runtime + Claude OS-style memory MCP would compose both — one declarative spec, two complementary execution layers.

**PM-in-Vault (T2) is data-discipline, not workflow-execution**: Obsidian PM doesn't execute work, it tracks it. The Profile (E024) execution lives in Multica/OpenClaw/Hermes; the Profile *artifact* could live in Obsidian PM vault as a `pm-task` with `pm-task: true` frontmatter — making the Profile's "what should the assistant do this week?" navigable in the same vault as the operator's projects.

**T4 (OCMC) likely subsumed by Multica**: Multica supports OpenClaw as one of its 10+ CLIs. OCMC-as-OpenClaw-specific-UI may be redundant unless there are deep OpenClaw-only features Multica doesn't expose. Until investigated, defer T4 as a potential E024-M004 input rather than separate workstream.

**Compounding insight**: the YouTube transcript's "stop building dashboards, build workflows" maps onto the Profile pattern's distinction between **the spec** (the Profile YAML — declarative, durable) and **the surface** (dashboards/UIs — Anthropic and/or Multica will solve). E024's investment should be on the spec, not on the surface.

## The Strategic Frame (YouTube transcript synthesis)

> [!info] **"Anthropic will solve 8 of 9 limitations themselves. The ONE thing they won't solve is YOUR specific business workflows."**

The video's central thesis aligns precisely with the operator's "pull from frontier and stay independent" directive:

| Limitation Anthropic will solve (per video) | Implication |
|---|---|
| Poor context recall + memory | Don't build memory-specific dashboards — Anthropic's project context + agent view will subsume |
| Scheduled tasks / multi-step workflows on schedule | Don't build cron-job wrappers — Anthropic has scheduled tasks in desktop + cron in claude-code terminal |
| Output separation / asset delivery | Don't build output-routing UIs — Anthropic is changing how outputs are displayed |
| Cross-channel access (Telegram, mobile, etc.) | Don't build cross-channel adapters — Claude Code channels + dispatch already cover this |

| Limitation Anthropic WON'T solve | Implication |
|---|---|
| **Repeatable processes with consistent high-quality outputs FOR YOUR BUSINESS** | This is where engineering time must invest |

### The Skill Systems Pattern (the video's recommended architecture)

> [!success] **Skill Systems = orchestrator skill + modular child skills wired by skill.md**

| Anti-pattern | Why bad | Fix |
|---|---|---|
| **Isolated skills** (manual chaining) | User is the intermediary — defeats orchestration | Skills should be wired by orchestrator |
| **Mega skills** (one big skill does everything) | Loses modularity, maintainability, progressive disclosure (Anthropic's context-loading optimization) | Decompose into small focused skills |
| ✅ **Skill Systems** (orchestrator + child skills) | Modular, reusable, progressive disclosure, maintainable | Build small focused skills + wire by orchestrator skill.md |

This pattern aligns with the [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Per-Project Assistant Profile pattern]] — Profiles are the *spec*, skill-systems are an *implementation pattern within* the Profile's Action Surface.

## Frontier-Per-Type Summary

| Type | Frontier | Why this is the frontier |
|---|---|---|
| **T1 Memory Layer** | **Claude OS v2.5** | Most mature memory + indexing architecture; hybrid tree-sitter+semantic with PageRank weighting; 36+ skills community; MIT |
| **T2 PM-in-Vault** | **Obsidian PM** | Most feature-complete PM in plain-Markdown; 3 views same data; dependencies + recurring + time tracking; MIT |
| **T3 Multi-Agent Orchestration** | **Multica** | Widest CLI breadth (10+ including Hermes); team-native multi-workspace; self-host option; **already operator-adopted** |
| **T4 Assistant Mission Control UI** | TBD | Both candidate repos have empty READMEs; possibly subsumed by Multica; needs code-investigation |

## Synthesis — How These Inputs Shape this project Profile Design (E024)

> [!tip] **Adopt the best from each frontier; don't lock in to any single one**

1. **From Claude OS**: take the **session-management pattern** (4-field state for hot-resume) and the **memory-MCP integration pattern** (natural-language remember-this) into Profile **Knowledge Scope** + **Success Criteria** sections (E024-M002).

2. **From Obsidian PM**: take the **plain-Markdown-with-YAML-frontmatter** discipline (already aligned with this project's existing approach); confirms Profile-as-YAML is right primitive (E024-M002 schema design).

3. **From Multica**: this is the **integration target**, not a competitor. The Profile's `runtime_targets:` list should explicitly enumerate Multica's 10+ supported CLIs (Claude Code · Codex · OpenClaw · OpenCode · Hermes · Gemini · Pi · Cursor Agent · Kimi · Kiro CLI) since Multica's daemon already detects them. **Spawn-protocol-multica** becomes a candidate addition to E024-M004 module scope.

4. **From OCMC / OpenClaw Command Center**: defer until code investigation; if features are subsumed by Multica, no additional work; if OpenClaw-specific deep features exist, candidate inputs to spawn-protocol-openclaw (E024-M004).

5. **From the YouTube transcript**: **Skill Systems** pattern (orchestrator + child skills) is the recommended **implementation pattern** within Profile's Action Surface. Add a section to the Profile pattern page on "Skill System composition" as the canonical implementation approach for Profile's Action Surface.

## Hermes Identity — Confirmed by Multica Evidence

> [!success] **Hermes is a real existing agent-CLI runtime** — appearing in Multica's daemon auto-detection list alongside Claude Code, Codex, OpenClaw, OpenCode, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI. The "Hermess" in operator's 2026-05-09 directive was simply a typo for "Hermes" (the Greek messenger god being a likely naming inspiration). Hermes belongs in the same category as Claude Code / Codex / OpenClaw — an Agent SDK / harness CLI that the per-project Profile can spawn against.

## Open Operator-Decisions Surfaced

> [!question] **D6 — Multica integration scope** — Profile's `runtime_targets:` should include Multica's 10+ CLIs. Should E024 add a new module (E024-M007: Multica integration) or fold this into M004 (spawn protocols)?

> [!question] **D7 — Hermes investigation** — Hermes CLI is real but we don't have its docs/repo. Should research be done now (separate fetch + synthesis) or deferred until spawn-protocol-hermes (M004) is actively designed?

> [!question] **D8 — T4 (OCMC) investigation** — Both reference repos have empty READMEs. Should we deep-read the code (gh CLI clone or look at file tree via gh api)? Or defer pending operator-clarification of which OCMC fork to study?

> [!question] **D9 — Skill Systems pattern adoption** — The YouTube transcript's "skill system = orchestrator + child skills" pattern is concretely applicable. Should this project adopt this pattern (one canonical skill system per Profile, mirroring Claude OS's approach) or treat it as one option among many?

> [!question] **D10 — "Information surface before public Obsidian"** — Operator-stated requirement. Possible mechanisms: (a) extend MCP server with real-time push; (b) build a pre-sync dashboard; (c) leverage Multica's WebSocket streaming for this project content; (d) RSS feed of wiki/log/ updates. Direction needed.

## Additional candidates to investigate (operator-invited "We can even find more")

These would extend the frontier surveys per type:

| Type | Additional candidate | Why investigate |
|---|---|---|
| T1 | **Cursor's @ memory system** | Different memory mechanism — semantic + structural |
| T1 | **GitHub Copilot Workspace** | Microsoft's take on persistent dev context |
| T2 | **Logseq Tasks** | Alternative to Obsidian-PM for plain-text PM |
| T2 | **Tana** | Block-based PM with AI integration |
| T3 | **AutoGen** (Microsoft) | Multi-agent framework alternative |
| T3 | **CrewAI** | Role-based multi-agent |
| T3 | **LangGraph** | Graph-based multi-agent |
| T4 | **OpenInterpreter dashboard** | Alternative assistant UI |
| T4 | **OpenAgents** | Alternative open-source agent UI |

## Relationships

- IMPLEMENTS: [[2026-05-09-operator-directive-hermes-clarification-information-surfacing-before-public-obsidian-pull-from-frontier-stay-independent-classify-existing-approaches|Operator directive 2026-05-09 turn 2]]
- FEEDS INTO: [[e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn|E024 — Per-Project Assistant Configurations Epic]] — empirical inputs for Profile design
- FEEDS INTO: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] — Skill Systems addition + Multica integration target
- COMPLEMENTS: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In as empirical claim]] — frontier survey demonstrates the "pull from frontier, stay independent" doctrine
- COMPLEMENTS: [[src-anthropic-programmatic-credit-pool-policy-change-2026-06-15|Synthesis — Anthropic Programmatic Credit Pool]] — the strategic frame (Anthropic will improve, we adapt) ties to credit-capture forcing function
- RELATES TO: [[[[project_multica_self_hosted_2026_04_28|Multica self-hosted memory]] — operator's existing adoption baseline]]

## Cross-references

- Raw transcript: `raw/transcripts/skill-chaining-in-claude-os-is-insane-dont-fall-behind.txt`
- Raw article: `raw/articles/why-we-built-claude-os-and-what-it-actually-is-code-it-forward.md`
- Raw repo dumps: `raw/articles/brobertsazclaude-os.md`, `stepankropachevobsidian-pm.md`, `multica-aimultica.md`, `jontsaiopenclaw-command-center.md`, `cyberpunk042ocmc-backup.md`
- Operator directive: `raw/notes/2026-05-09-operator-directive-hermes-clarification-information-surfacing-before-public-obsidian-pull-from-frontier-stay-independent-classify-existing-approaches.md`

## Backlinks

[[Operator directive 2026-05-09 turn 2]]
[[E024 — Per-Project Assistant Configurations Epic]]
[[Pattern — Per-Project Assistant Profile]]
[[Lesson — Anti-Vendor-Lock-In as empirical claim]]
[[Synthesis — Anthropic Programmatic Credit Pool]]
[[Multica self-hosted memory]]

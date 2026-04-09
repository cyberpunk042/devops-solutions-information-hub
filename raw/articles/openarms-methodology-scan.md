# OpenArms Methodology Scan — Deep Research Findings

**Scanned:** 2026-04-09
**Source project:** `/home/jfortin/openarms/`
**Repo:** https://github.com/openarms/openarms
**Researcher note:** Full read of CLAUDE.md, AGENTS.md, VISION.md, CONTRIBUTING.md, docs/concepts/, docs/automation/, skills/, wiki/ structure.

---

## 1. Project Identity & Core Values

**Document:** `VISION.md` — Type: Vision / Strategic directive

OpenArms started as a personal playground (Warelay → Clawdbot → Moltbot → OpenArms), forked from OpenClaw. It is a privacy-first, augmented AI assistant gateway.

**Core identity (operator directive, verbatim):**
> "OpenArms is about privacy and freedom and security. Its the anonymity and supercharged and augmented AI assistant, ready to work alone or in fleets."
> "FREEDOM! PRIVACY!"

**Non-negotiable values:** Privacy, freedom, security. These are the supreme source of truth, stored verbatim in `wiki/log/2026-04-08-initial-vision.md`.

**Architecture:** TypeScript (ESM), orchestration-first (prompts, tools, protocols, integrations). Terminal-first UX by design — keeps setup explicit with visible security posture.

**Fork model:** Augment, do not completely refactor. Must preserve upstream pull capability from OpenClaw. All features are additive. Patches flow both ways.

---

## 2. Document Standards — CLAUDE.md / AGENTS.md

**Documents:** `CLAUDE.md` (351 lines) and `AGENTS.md` (identical content, symlinked). Type: Comprehensive operating specification for AI agents.

These files are **the same file** — `AGENTS.md` is the canonical name; `CLAUDE.md` is a symlink (enforced by a rule: "When adding a new `AGENTS.md` anywhere in the repo, also add a `CLAUDE.md` symlink pointing to it"). This pattern is replicated at boundary directories (e.g., `src/plugin-sdk/AGENTS.md`, `src/channels/AGENTS.md`).

### Structure of CLAUDE.md

The file is organized into these major sections:

1. **Repository Guidelines** — file reference conventions, CODEOWNERS policy
2. **Operator Directives (Sacrosanct)** — verbatim founding directives, core identity, fork model, working philosophy
3. **OpenArms Vision & Direction** — key feature directions (Solo Agent, Fleet, Network Rules, Cost, Tracing, Extensibility), ecosystem map
4. **Methodology & Agent Execution** — stages, modes, end conditions, ephemeral override patterns, the auto-loop concept
5. **Wiki & Backlog** — schema, domain structure, backlog, log, operator directive handling
6. **Project Structure & Module Organization** — source layout, plugin naming, bundled plugin constraints, messaging channels, import boundaries
7. **Architecture Boundaries** — plugin boundary, channel boundary, provider/model boundary, gateway protocol boundary, bundled plugin contract boundary, extension test boundary
8. **Docs Linking (Mintlify)** — internal link conventions, i18n pipeline, doc content standards
9. **Build, Test, and Development Commands** — Node 22+, pnpm/bun setup, gate system (local/landing/CI), test infrastructure
10. **Coding Style & Naming Conventions** — TypeScript strict, Oxlint/Oxfmt, type discipline rules
11. **Release / Advisory Workflows** — release maintainer skill, GHSA skill references
12. **Testing Guidelines** — Vitest, coverage thresholds (70%), naming, pool constraints, live test patterns
13. **Commit & Pull Request Guidelines** — `scripts/committer` usage, PR template, PR maintainer skill
14. **Git Notes** — multi-agent safety rules (no stash, no worktree manipulation, no branch switching without explicit request)
15. **Security & Configuration Tips** — credentials, secrets policy, release signing
16. **Local Runtime / Platform Notes** — macOS, iOS, Android platform specifics, voice wake, gateway restart
17. **Collaboration / Safety Notes** — multi-agent coordination rules, lint churn handling, tool schema guardrails

### Key Standards Enforced

- **Sacrosanct operator directives**: Quote verbatim from `wiki/log/`. Never paraphrase.
- **Architecture boundary enforcement**: Each boundary has public docs + definition files + rules. Violations are tracked in `check-additional` CI gate (intentionally excluded from local dev loop).
- **Import discipline**: Extensions access core only through `openarms/plugin-sdk/*`. Core must not reach into bundled plugin internals.
- **Multi-agent safety rules**: No git stash, no worktree manipulation, no branch switching, no merge commits on main — all enforced to support concurrent agents.
- **Gate system**: "gate" = verification command set. Three levels: local dev gate (`pnpm check`), landing gate (`pnpm check + test + build`), CI gate (workflow-specific).
- **Dynamic import guardrail**: No mixing of `await import()` and static `import` for same module in production. Use `*.runtime.ts` boundaries for lazy loading.
- **File size guideline**: ~700 LOC (CLAUDE.md) and ~500 LOC (Collaboration section) — guideline, not hard guardrail.

---

## 3. Contributing Methodology

**Document:** `CONTRIBUTING.md` — Type: Contributor guide / Process specification

### PR Policy
- One PR = one issue/topic. No bundled fixes.
- PRs over ~5,000 changed lines: reviewed only in exceptional circumstances.
- No large batches of tiny PRs.
- Refactor-only PRs: rejected unless maintainer explicitly requested.
- Test/CI-only PRs for known main failures: auto-closed.

### Review Conversation Ownership
- Review conversations are **author-owned**. Authors must resolve or reply.
- Codex review required (`codex review --base origin/main`) — treat as highest standard of AI review.
- Applies to both human-authored and AI-assisted PRs.

### AI/Vibe-Coded PRs
- Explicitly welcomed. Must be marked as AI-assisted.
- Required disclosures: AI tool used, degree of testing, prompts/session logs if possible.
- AI PRs are "first-class citizens" — transparency is the requirement.

### Before Any PR
- `pnpm build && pnpm check && pnpm test`
- Extension changes: `pnpm test:extension <name>`, shared surfaces: `pnpm test:contracts`
- Screenshots required for visual/UI changes
- American English only in code, comments, docs, UI strings
- CODEOWNERS paths: restricted surfaces, not opportunistic cleanup targets

---

## 4. The Wiki Pattern — Embedded LLM Knowledge Base

**Documents:** `wiki/config/schema.yaml`, `wiki/config/methodology.yaml`, `wiki/config/agent-directive.md`, `wiki/config/modes.yaml`

OpenArms embeds an entire LLM wiki inside the project at `wiki/`, adapted from the devops-solutions-research-wiki pattern. This is the control surface for autonomous agent work.

### Schema (`wiki/config/schema.yaml`)

**Frontmatter fields:**

Required: `title`, `type`, `domain`, `status`, `created`, `updated`, `tags`

Optional: `confidence`, `maturity`, `priority`, `epic`, `module`, `assignee`, `estimate`, `sources`, `depends_on`, `blocked_by`

Task-specific required: `task_type`, `current_stage`, `readiness` (0-100), `stages_completed`, `artifacts`

**Page types:**
- Knowledge types: `concept`, `reference`, `decision`, `deep-dive`, `comparison`, `pattern`, `lesson`, `index`
- Backlog types: `epic`, `module`, `task`, `note`

**Required sections per type:**
- `concept`: Summary, Key Insights, Deep Analysis, Relationships
- `decision`: Summary, Context, Decision, Consequences, Relationships
- `pattern`: Summary, Problem, Solution, Examples, Relationships
- `lesson`: Summary, Context, Insight, Application, Relationships
- `epic`: Summary, Goals, Modules, Success Criteria, Relationships
- `task`: Summary, Details, Done When, Relationships

**Status lifecycle:**
- Wiki: `draft → active → stale → archived`
- Backlog: `draft → active → in-progress → blocked → done → archived`

**Priority:** P0 (critical) → P1 (this sprint) → P2 (planned) → P3 (backlog)

**Relationship verbs:** BUILDS_ON, ENABLES, BLOCKS, BLOCKED_BY, DEPENDS_ON, RELATES_TO, FEEDS_INTO, DERIVED_FROM, SUPERSEDES, IMPLEMENTS, EXTENDS, CONSTRAINS, PART_OF, PARENT_OF, COMPARES_TO, CONTRADICTS

**Quality gates:** Summary min 20 words, deep analysis min 80 words, min 1 relationship, max 70% concept overlap, stale threshold 30 days.

### Directory Structure

```
wiki/
  config/          — methodology.yaml, schema.yaml, agent-directive.md, modes.yaml
  domains/         — vision/, architecture/, capabilities/, ecosystem/
  backlog/         — epics/ (E001-E008), modules/, tasks/ (T001-T022+)
  log/             — operator directives (sacrosanct), session notes, findings
  agent-directive.md — what a solo agent reads when spawned
```

**Domain contents as of scan:**
- `wiki/domains/architecture/`: auto-loop.md, solo-agent-runtime.md, solo-agent-config-design.md, agent-run-operations.md, branding-boundary.md, cost-tracking-config-design.md, hook-events-design.md, network-rules-config-design.md
- `wiki/domains/vision/`: openarms-identity.md
- `wiki/domains/ecosystem/`: openfleet-patch-parity.md

**Active backlog (as of 2026-04-09):**
- 8 epics (E001-E008): Solo Agent Mode (P1), Network Rules Engine (P1), Cost Optimization (P1), Live Tracing (P2), Fleet Integration (P1), Privacy & Anonymity (P2), Extensibility (P2), Branding & Docs (P1)
- 22 tasks (T001-T022), with 21 completed and T007 in-progress

---

## 5. Methodology System — Staged Development Protocol

**Document:** `wiki/config/methodology.yaml` — Type: Process specification

The methodology system defines how autonomous agents work through tasks. It is a deliberate, staged approach that prevents implementation-first thinking.

### The 5 Stages

| Stage | Readiness Range | What Agent Does | What Agent Produces | What Agent Must NOT Do |
|-------|----------------|-----------------|---------------------|------------------------|
| **Document** | 0–25% | Read code, understand the problem | Wiki page, gap analysis | Write implementation code |
| **Design** | 25–50% | Make decisions, define config shape | Design doc, type sketches in documentation | Write src/ files |
| **Scaffold** | 50–80% | Create the skeleton | Types, .env.example entries, empty test files | Implement business logic |
| **Implement** | 80–95% | Write the logic | Working implementation, passing compile + lint | Skip type checks |
| **Test** | 95–100% | Prove it works | Passing test suite, no regressions | Leave broken tests |

### Task Types and Required Stages

| task_type | Required Stages |
|-----------|----------------|
| `docs` | document |
| `spike` | document, design |
| `task` | scaffold, implement, test |
| `bug` | document, implement, test |
| `refactor` | document, scaffold, implement, test |
| `epic/module` | document, design, scaffold, implement, test |

A task is **NOT done** until all required stages are in `stages_completed` AND readiness is 100.

### Execution Modes (Autonomy Spectrum)

```
full-autonomous ──── autonomous ──── semi-autonomous ──── plan ──── custom
```

- `full-autonomous`: Skips document stage on tasks, no human review, backlog-empty end condition
- `autonomous` (default): All stages enforced, no stops, continues until end condition
- `semi-autonomous`: Pauses after each task for human review
- `document-only` / `design-only` / `scaffold-only`: Stop after that stage
- `plan`: Alias for design-only
- `custom`: Ephemeral, per-run configuration

### End Conditions

- `backlog-empty`: No tasks in draft/active/in-progress status
- `stage-reached`: Current task reaches specified stage
- `time-limit`: Agent has worked N hours
- `cost-limit`: Agent has spent $N on API calls
- `task-count`: Agent has completed N tasks

### Commit Convention

**ONE COMMIT PER STAGE.** Format: `feat(wiki): T0XX stage-name — short description`

Example:
- `feat(wiki): T023 document — document network rules evaluation engine`
- `feat(wiki): T023 scaffold — scaffold NetworkRulesConfig types and empty tests`

---

## 6. The Infinite Auto-Loop Pattern

**Document:** `wiki/domains/architecture/auto-loop.md` — Type: Architecture concept

The auto-loop is the core execution model for solo autonomous agents. It is self-hosting: the agent uses this methodology to build the features that make the methodology better.

### Loop Steps

1. Read CLAUDE.md → methodology.yaml → agent-directive.md → backlog/_index.md
2. Pick highest priority task (filter: epic/module scope, priority, dependencies; skip: done/archived/blocked)
3. Determine next required stage from methodology.yaml task_types
4. Read stage protocol from methodology.yaml
5. Execute ONLY that stage — produce ONLY the artifacts for that stage
6. Update task frontmatter (current_stage, stages_completed, readiness, artifacts, status)
7. Git: stage and commit ALL changed files — ONE COMMIT PER STAGE
8. VERIFY: re-read task file, confirm frontmatter is correct
9. If more stages remain, go to step 3
10. When all stages complete: set status "done", readiness 100
11. Update backlog index (move task to Completed)
12. Write completion log entry to wiki/log/
13. Check end condition — if not met, loop back to step 1
14. Final: commit remaining, print summary

### Stage Boundaries (Critical)

- Document stage: wiki pages ONLY — no src/ files
- Design stage: design docs ONLY — no src/ files (type sketches go in documentation, not code)
- Scaffold stage: types + empty tests — NO business logic
- These boundaries are enforced by protocol (CLAUDE.md instructions), not by MCP tool blocking (contrast with OpenFleet which uses fleet_commit tool blocking)

### What the Agent Must Never Do

- Paraphrase operator directives — quote verbatim
- Break OpenClaw upstream compatibility
- Skip stages without explicit mode permission
- Mark task "done" with incomplete stages
- Check "Done When" boxes without verifying the actual artifact exists
- Commit code that doesn't compile or lint
- Create files without reading existing code first
- Ask questions that operator directives already answer
- Set readiness 100 with missing stages_completed entries

### Adapted from OpenFleet

| OpenFleet Stage | OpenArms Stage | Key Difference |
|----------------|----------------|----------------|
| Conversation | (merged into Document) | No PO — operator directives are pre-written |
| Analysis | Document | Read code, map existing state |
| Investigation | Design | Explore options, make decisions |
| Reasoning | Scaffold | OpenArms adds scaffolding as explicit stage |
| Work | Implement + Test | Split into code then verify |

OpenFleet enforces via MCP tools (fleet_commit blocked in wrong stage). OpenArms enforces via CLAUDE.md protocol instructions.

---

## 7. Agent Directive Template

**Document:** `wiki/config/agent-directive.md` — Type: Agent bootstrap / Runtime operating spec

This is the document a solo agent reads when spawned. It contains:

1. Sacrosanct operator directives (verbatim)
2. Work loop (14-step numbered procedure)
3. Stage enforcement rules (mandatory table)
4. Task frontmatter requirements (YAML template)
5. Git management rules (one commit per stage, push policy, conventional format)
6. Methodology stages summary table
7. Mode configuration (env vars OPENARMS_AGENT_MODE, OPENARMS_AGENT_END_CONDITION)
8. Task selection algorithm (filter → sort by priority → skip blocked → prefer unblocked deps → resume in-progress)
9. Quality gates per stage (what must be verified before advancing)
10. Absolute prohibitions list
11. Reporting format (what to include in wiki/log/ entries)

**Push policy:** In local workspace (default), do NOT push. Operator pushes when ready. In isolated workspace, push only if `OPENARMS_AGENT_PUSH=true`.

---

## 8. Gateway Architecture

**Document:** `docs/concepts/architecture.md` — Type: Technical architecture reference

Standard frontmatter pattern for concept docs:
```yaml
---
summary: "WebSocket gateway architecture, components, and client flows"
read_when:
  - Working on gateway protocol, clients, or transports
title: "Gateway Architecture"
---
```

The `read_when` field is a key discovery — docs self-declare their own relevance context. This enables agents to know WHEN to load a doc rather than loading everything.

### System Components

- **Gateway (daemon)**: Single long-lived process, owns all messaging surfaces (WhatsApp/Baileys, Telegram/grammY, Slack, Discord, Signal, iMessage, WebChat). Exposes typed WebSocket API.
- **Clients**: macOS app, CLI, web admin — one WS connection each.
- **Nodes**: macOS/iOS/Android/headless — connect with `role: node`, provide device capabilities (canvas, camera, screen recording, location).
- **Canvas host**: Served by gateway HTTP at `/__openarms__/canvas/` (agent-editable) and `/__openarms__/a2ui/`.

### Wire Protocol

- First frame MUST be `connect`
- Requests: `{type:"req", id, method, params}` → `{type:"res", id, ok, payload|error}`
- Events: `{type:"event", event, payload, seq?, stateVersion?}`
- Idempotency keys required for side-effecting methods (send, agent)
- TypeBox schemas define protocol → JSON Schema generated → Swift models generated (codegen pipeline)

---

## 9. Agent Loop & Hook System

**Document:** `docs/concepts/agent-loop.md` — Type: Technical concept reference

### Entry Points
- Gateway RPC: `agent` and `agent.wait`
- CLI: `agent` command

### Hook Points (Two Systems)

**Internal (Gateway) hooks — triggered by commands/lifecycle:**
- `agent:bootstrap`: modify bootstrap context files before system prompt
- Command hooks: `/new`, `/reset`, `/stop`

**Plugin hooks (agent + gateway lifecycle):**
- `before_model_resolve`: override provider/model before resolution
- `before_prompt_build`: inject context into system prompt
- `before_agent_start`: legacy compatibility
- `agent_end`: post-completion inspection
- `before_compaction` / `after_compaction`
- `before_tool_call` / `after_tool_call`: intercept tool params/results
- `before_install`: gate skill/plugin installs
- `tool_result_persist`: transform tool results before transcript write
- `message_received` / `message_sending` / `message_sent`
- `session_start` / `session_end`
- `gateway_start` / `gateway_stop`

**Hook decision semantics:** `{ block: true }` is terminal and stops lower-priority handlers. `{ block: false }` is a no-op (does NOT clear prior block).

### Agent Timeout
- Default runtime: 172800 seconds (48 hours)
- `agent.wait` default: 30 seconds

---

## 10. Automation Subsystem

**Documents:** `docs/automation/hooks.md`, `docs/automation/tasks.md`, `docs/automation/clawflow.md`

### Hooks Discovery Hierarchy (increasing override precedence)
1. Bundled hooks: `dist/hooks/bundled/` (shipped with install)
2. Plugin hooks: bundled inside installed plugins
3. Managed hooks: `~/.openarms/hooks/` (user-installed)
4. Workspace hooks: `<workspace>/hooks/` (disabled by default, explicit enable required)

Workspace hooks CANNOT override bundled/managed/plugin hooks with same name.

**Hook directory structure:**
```
my-hook/
├── HOOK.md          # Metadata + documentation
└── index.ts         # Implementation
```

**Bundled hooks:** session-memory, bootstrap-extra-files, command-logger, boot-md

### Background Tasks

Task lifecycle: `queued → running → (succeeded | failed | timed_out | cancelled | lost)`

Task sources:
- ACP runs → runtime: `acp`, notify: `done_only`
- Subagent spawns → runtime: `subagent`, notify: `done_only`
- Cron jobs → runtime: `cron`, notify: `silent`
- CLI operations → runtime: `cli`, notify: `done_only`

NOT tasks: heartbeat turns, normal interactive chat, direct /command responses.

**Storage:** SQLite at `$OPENARMS_STATE_DIR/tasks/runs.sqlite`. Sweeper every 60s. 7-day retention.

**Notification policies:** `done_only` (default), `state_changes`, `silent`

### ClawFlow

Flow = job-level wrapper above tasks. One flow ID for the whole job. Linear execution model: create flow → run task → wait → resume → next task or finish. Does NOT own branching/business logic (that belongs in authoring layers: Lobster, acpx, TypeScript helpers, bundled skills).

---

## 11. Multi-Agent Routing

**Document:** `docs/concepts/multi-agent.md` — Type: Configuration reference

### Agent Isolation Model

Each agent is a fully isolated "brain" with its own:
- Workspace (files, AGENTS.md/SOUL.md/USER.md, persona rules)
- State directory (`agentDir`) for auth profiles, model registry, per-agent config
- Session store (`~/.openarms/agents/<agentId>/sessions/`)
- Auth profiles (NOT shared — never reuse `agentDir` across agents)
- Skills (per-agent via workspace `skills/`, shared via `~/.openarms/skills`)

### Routing Rules (Deterministic, Most-Specific Wins)

1. `peer` match (exact DM/group/channel id)
2. `parentPeer` match (thread inheritance)
3. `guildId + roles` (Discord role routing)
4. `guildId` (Discord)
5. `teamId` (Slack)
6. `accountId` match for channel
7. Channel-level match (`accountId: "*"`)
8. Fallback to default agent

Multiple matching bindings at same tier: first in config order wins.

### Workspace Contract

Bootstrap files (agent identity layer):
- `AGENTS.md` — operating instructions + memory
- `SOUL.md` — persona, boundaries, tone
- `TOOLS.md` — user-maintained tool notes
- `BOOTSTRAP.md` — one-time first-run ritual (deleted after)
- `IDENTITY.md` — agent name/vibe/emoji
- `USER.md` — user profile + preferred address

---

## 12. Skills System

**Directory:** `skills/` (50+ skill directories, each containing a single `SKILL.md`)

### Skill File Structure (`SKILL.md`)

```yaml
---
name: github
description: "GitHub operations via gh CLI: issues, PRs, CI runs..."
metadata:
  {
    "openarms":
      {
        "emoji": "🐙",
        "requires": { "bins": ["gh"] },
        "install": [
          {
            "id": "brew",
            "kind": "brew",
            "formula": "gh",
            "bins": ["gh"],
            "label": "Install GitHub CLI (brew)"
          }
        ]
      }
  }
---

# Skill Title

[Documentation content]
```

**Frontmatter fields:**
- `name`: skill identifier
- `description`: capability summary + WHEN TO USE / NOT TO USE signals
- `metadata.openarms.emoji`: display emoji
- `metadata.openarms.requires`: binary requirements (`bins` or `anyBins`)
- `metadata.openarms.install`: installation steps with `id`, `kind` (brew/apt/node), `package/formula`, `bins`, `label`

**Key discovery:** The `description` field in skills follows a "Use when: ... NOT for: ..." pattern that explicitly defines the skill's activation triggers and exclusion zones. This is optimized for agent skill-selection logic.

### Sample Skills Directory (50+ skills)
1password, apple-notes, apple-reminders, bear-notes, blogwatcher, blucli, bluebubbles, camsnap, canvas, clawflow, clawflow-inbox-triage, clawhub, coding-agent, discord, eightctl, gemini, gh-issues, github, gog, goplaces, healthcheck, himalaya, imsg, mcporter, model-usage, nano-pdf, node-connect, notion, obsidian, openai-whisper, openai-whisper-api, openhue, oracle, ordercli, peekaboo, sag, session-logs, sherpa-onnx-tts, skill-creator, slack, songsee, sonoscli, spotify-player, summarize, things-mac, tmux, trello, video-frames, voice-call, wacli, weather, xurl

**Policy:** New skills should be published to ClawHub first (`clawhub.ai`), not added to core. Core skill additions require strong product or security reason.

---

## 13. Plugin Architecture Pattern

**Documents:** `docs/plugins/architecture.md`, `docs/plugins/manifest.md`, `docs/plugins/sdk-overview.md`

### Plugin Contract

All plugins access core exclusively through `openarms/plugin-sdk/*`. Three plugin categories:

1. **Channel plugins** — add new messaging surfaces
2. **Provider plugins** — add new AI model providers
3. **Bundled plugins** — workspace packages shipped with OpenArms (Matrix, Zalo, Voice Call, etc.)

**Naming convention:** Plugin id anchored across:
- `openarms.plugin.json:id`
- Default workspace folder name
- Package names (`@openarms/<id>` or approved suffix forms: `-provider`, `-plugin`, `-speech`, `-sandbox`, `-media-understanding`)
- `openarms.install.npmSpec` = package name
- `openarms.channel.id` = plugin id

**Install constraint:** `npm install --omit=dev` in plugin dir. Runtime deps in `dependencies`. No `workspace:*` in `dependencies`.

**Boundary rule:** Plugin production code MUST NOT import `src/**`, `src/plugin-sdk-internal/**`, or another extension's `src/**` directly.

**MCP integration:** Via `mcporter` bridge (https://github.com/steipete/mcporter) rather than first-class MCP runtime in core. Keeps MCP flexible and decoupled.

---

## 14. Document Infrastructure Standards

### Mintlify Docs (`docs/`)

- Hosted at `docs.openarms.ai` via Mintlify
- Internal links: root-relative, no `.md`/`.mdx` extension (e.g., `[Config](/configuration)`)
- Section cross-references: anchors on root-relative paths (e.g., `[Hooks](/configuration#hooks)`)
- Heading rule: no em dashes or apostrophes (break Mintlify anchor links)
- README uses absolute URLs (GitHub compatibility)
- Docs content: generic — no personal device names/hostnames/paths; use placeholders

### i18n Pipeline (`docs/zh-CN/`)

- Generated content — do not manually edit
- Pipeline: English docs → glossary update → `scripts/docs-i18n` → targeted fixes only
- Translation memory: `docs/.i18n/zh-CN.tm.jsonl`
- `pnpm docs:check-i18n-glossary` enforces glossary coverage before translation reruns

### Generated Baseline Artifacts

- Location: `docs/.generated/`
- Config schema drift: `pnpm config:docs:gen` / `pnpm config:docs:check`
- Plugin SDK API drift: `pnpm plugin-sdk:api:gen` / `pnpm plugin-sdk:api:check`
- Rule: when changing config schema or public Plugin SDK surface, update matching baseline artifact

---

## 15. Release & Maintenance Workflows

### Release Coordination (via Agent Skills)

- `$openarms-release-maintainer` at `.agents/skills/openarms-release-maintainer/SKILL.md` — release naming, version coordination, changelog-backed release notes
- `$openarms-ghsa-maintainer` at `.agents/skills/openarms-ghsa-maintainer/SKILL.md` — GHSA advisory inspection, patch/publish flow

### Version Locations (All Must Be Updated)

- `package.json` (CLI)
- `apps/android/app/build.gradle.kts` (versionName/versionCode)
- `apps/ios/Sources/Info.plist` + `apps/ios/Tests/Info.plist`
- `apps/macos/Sources/OpenArms/Resources/Info.plist`
- `docs/install/updating.md` (pinned npm version)
- Peekaboo Xcode projects/Info.plists
- `appcast.xml` ONLY when cutting a new macOS Sparkle release

### Changelog Rules

- User-facing changes only; no internal/meta notes
- Append to END of target section (not top) within active version block
- One contributor mention per line: prefer `Thanks @author` not `by @author`

---

## 16. Coding Standards Summary

### TypeScript Discipline

- Strict typing; avoid `any` — use real types, `unknown`, or narrow adapters
- `zod` for external boundaries (config, webhooks, CLI/JSON, persisted JSON, third-party API responses)
- Discriminated unions when parameter shape changes runtime behavior
- `Result<T, E>` style for recoverable runtime decisions
- No `@ts-nocheck`; no inline lint suppressions by default (fix root causes)
- No prototype mutation — use explicit inheritance/composition

### File Organization

- Source: `src/` (CLI in `src/cli`, commands in `src/commands`, web in `src/provider-web.ts`, infra in `src/infra`, media in `src/media`)
- Tests: colocated `*.test.ts`; e2e: `*.e2e.test.ts`
- Files under ~700 LOC (guideline only)

### Naming

- Product/app/docs: "OpenArms"
- CLI command, package/binary, paths, config keys: "openarms"
- American English in all code, comments, docs, UI strings

---

## 17. Operational Patterns Observed

### The "Log as Sacrosanct Directive" Pattern

All operator directives are stored verbatim in `wiki/log/` and referenced by date. These are treated as primary source of truth — quoted, never paraphrased. CLAUDE.md explicitly says operator directives live at `wiki/log/2026-04-08-initial-vision.md` and must never be paraphrased, diluted, or overridden.

This mirrors the verbatim logging methodology in the research wiki — the same operator established the same anti-paraphrase rule in both projects.

### The "Auto-Notification Pattern"

Long-running background tasks should append completion notification to the agent prompt:
```
When completely finished, run:
openarms system event --text "Done: [brief summary]" --mode now
```
This triggers immediate heartbeat wake instead of waiting for next scheduled interval.

### The "Skill Self-Declaration Pattern"

Each skill's frontmatter `description` field encodes:
1. What the skill does (capability)
2. WHEN to activate it (trigger conditions)
3. When NOT to use it (explicit anti-triggers)

This is a deliberate design for LLM-readable skill routing without requiring vector search.

### The "Boundary AGENTS.md" Pattern

Each major subsystem boundary has its own `AGENTS.md` file co-located with the code:
- `bundled-plugin-tree/AGENTS.md`
- `src/plugin-sdk/AGENTS.md`
- `src/channels/AGENTS.md`
- `src/plugins/AGENTS.md`
- `src/gateway/protocol/AGENTS.md`

Each `AGENTS.md` is symlinked as `CLAUDE.md` in the same directory. This provides "progressive disclosure" of context — agents load only the boundary guide relevant to the code they're touching.

### The "Frontmatter as State Machine" Pattern

Task frontmatter fields form a state machine:
- `status` transitions: `draft → active → in-progress → done`
- `current_stage` + `stages_completed` track precise progress
- `readiness` (0-100) derived from stage completion
- `artifacts` lists concrete file evidence of work done

No external board or MCP tool required — state lives in the wiki files themselves.

### The "Gate System" Pattern

Three verification levels with explicit semantics:
1. **Local dev gate**: `pnpm check` — fast loop, excludes architecture policy guards
2. **Landing gate**: `pnpm check + test + build` — for pushing to main
3. **CI gate**: workflow-specific — `check`, `check-additional` (architecture policy), `build-smoke`

The architecture policy is deliberately excluded from local dev gate to avoid friction, but enforced in CI. This is a deliberate tradeoff between developer velocity and consistency.

---

## 18. Cross-Project Ecosystem Relationships

OpenArms is one node in a 6-project ecosystem:

| Project | Role | Relationship |
|---------|------|--------------|
| OpenArms | Privacy-first AI gateway | Subject of this scan |
| OpenFleet | 10-agent orchestrator | OpenArms is the runtime; patches flow both ways |
| AICP (devops-expert-local-ai) | Local AI inference (78 skills, LocalAI) | OpenArms routes to AICP for local model execution |
| DSPD | Project management via Plane | OpenArms integrates for task tracking |
| Research Wiki (devops-solutions-research-wiki) | LLM knowledge spine | OpenArms wiki ADAPTED from Research Wiki pattern |
| Control Plane | Infrastructure visibility | OpenArms integrates for infra observability |

**Fork model:** OpenArms forks OpenClaw. 13 patches maintained in OpenFleet that also apply to OpenClaw/OpenArms. Must maintain upstream pull capability.

**Wiki adaptation:** The OpenArms wiki directly reuses the LLM wiki pattern from devops-solutions-research-wiki. Same: YAML frontmatter schema (adapted), typed relationships, domain/_index.md pattern, status lifecycle, quality gates. Different: backlog types added (epic/module/task), stage tracking fields, methodology integration.

---

## 19. Key Files Reference Map

```
/home/jfortin/openarms/
  CLAUDE.md                              — Main operating spec (351 lines); symlink to AGENTS.md
  AGENTS.md                              — Canonical file; identical to CLAUDE.md
  VISION.md                              — Project vision, priorities, what will not be merged
  CONTRIBUTING.md                        — Contributor guide, PR process, maintainers list

  wiki/
    config/
      schema.yaml                        — Page type definitions, status lifecycles, quality gates
      methodology.yaml                   — 5 stages, task types, modes, end conditions
      agent-directive.md                 — Solo agent bootstrap — 14-step work loop
      modes.yaml                         — Autonomy spectrum documentation
    domains/
      architecture/auto-loop.md         — The infinite auto-loop pattern (key concept)
      architecture/solo-agent-*.md      — Solo agent design docs
      vision/openarms-identity.md       — Identity concept page
      ecosystem/openfleet-patch-parity.md — Upstream compatibility analysis
    backlog/
      _index.md                          — 8 epics overview table
      epics/E001-E008.md                 — Epic definitions with phases
      tasks/_index.md                    — Task index with completed/in-progress tables
      tasks/T001-T022.md                 — Individual task files
    log/
      2026-04-08-initial-vision.md       — Founding directives (sacrosanct source of truth)
      2026-04-09-first-agent-run-findings.md — First agent run retrospective

  docs/
    concepts/architecture.md            — Gateway architecture (read_when pattern)
    concepts/agent-loop.md              — Agent lifecycle and hook points
    concepts/multi-agent.md             — Multi-agent routing and isolation
    concepts/agent.md                   — Agent runtime, workspace contract, bootstrap files
    automation/hooks.md                 — Hook discovery, trust boundaries, bundled hooks
    automation/tasks.md                 — Background task tracking
    automation/clawflow.md              — Flow layer above tasks
    plugins/architecture.md             — Plugin contract, hook types, boundary rules

  skills/
    coding-agent/SKILL.md              — Delegate coding to Codex/Claude Code/Pi
    github/SKILL.md                    — GitHub operations via gh CLI
    [50+ more skills]
```

---

## 20. Methodology Patterns for Synthesis

The following patterns are candidates for synthesis into wiki pages:

1. **"Verbatim Operator Directive" pattern** — Storing founding directives verbatim in a log file treated as sacrosanct source of truth. Never paraphrase the operator. Quote, do not interpret.

2. **"LLM Wiki as Task Queue" pattern** — Using frontmatter fields as a state machine for task tracking. No external board. Status/stage/readiness in YAML. Wiki IS the control surface.

3. **"Staged Development Protocol" pattern** — 5 explicit stages (document → design → scaffold → implement → test) with hard boundaries. Stage gates prevent implementation-first thinking. One commit per stage.

4. **"Skill Self-Declaration with Anti-Triggers" pattern** — Skill description field encodes activation triggers AND exclusion zones explicitly. Optimized for agent routing without vector search.

5. **"Progressive Boundary AGENTS.md" pattern** — Co-locate AGENTS.md at every major subsystem boundary. Progressive disclosure — agents load only the relevant boundary context.

6. **"Autonomy Spectrum with End Conditions" pattern** — Modes as a spectrum from full-autonomous to plan-only. Pluggable end conditions (backlog-empty, time-limit, cost-limit, task-count). Ephemeral per-run override without modifying persistent config.

7. **"read_when Doc Metadata" pattern** — Docs declare their own relevance context via `read_when:` frontmatter field. Agents know when to load a doc without reading everything.

8. **"Gate System with Architecture Policy Isolation" pattern** — Architecture policy guards excluded from local dev gate (developer velocity), enforced in CI (consistency). Three-tier gate: local → landing → CI.

9. **"Flow Above Tasks" pattern** — ClawFlow is a job-level wrapper above background task records. Tasks = execution ledger. Flows = job-level ownership with return context. Authoring layers (Lobster, TypeScript helpers) sit above both.

10. **"Auto-Notification on Completion" pattern** — Background agents append completion notification command to their own prompt, triggering immediate wake event instead of waiting for heartbeat schedule.

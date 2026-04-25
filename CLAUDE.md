# CLAUDE.md — Research Wiki (Claude Code delta)

> The brain in this project IS the layered Markdown configuration. For universal cross-tool context: [AGENTS.md](AGENTS.md). For detailed rules: [.claude/rules/](.claude/rules/).

## Operator Directives (Sacrosanct — verbatim, never paraphrase)

- "we need to establish a strong method of work with the Wiki LLM structure and Methodology"
- "do not confuse everything. the words are important. goldilock is not model and model is not standard and standard is not example and example is not template and none of this is knowledge but knowledge is at all their layers."
- "fix it at the root instead.. its not hard" — solve problems with tooling, not manual work
- "Preach by example."
- "behave FROM the project, not OVER it" (2026-04-24)
- "the project is intelligent. the intelligence comes from USING the project" (2026-04-24)
- "this is the base of what this fucking project is supposed to teach and enforce" (2026-04-24)
- "everything evolves and everything is flexible" (2026-04-24)

Full history: `wiki/log/` (verbatim, sacrosanct). Latest session: `wiki/log/2026-04-24-*.md` + `raw/notes/2026-04-24-operator-directives-session-verbatim.md`.

## Identity Profile (Goldilocks — stable fields only)

| Dimension | Value |
|-----------|-------|
| **Type** | system (framework + instance + second brain) |
| **Domain** | knowledge (Python/wiki tools) |
| **Phase** | production (used daily, 477+ pages) |
| **Scale** | medium |
| **PM Level** | L1 (wiki backlog + CLAUDE.md directives) |
| **Trust Tier** | operator-supervised |
| **Second Brain** | IS the second brain (self-referential) |

Execution mode, SDLC profile, methodology model are **task properties** — declared per session, not hardcoded.
Full profile + active milestones: [CONTEXT.md](CONTEXT.md).

## 4 Governing Principles (cross-project quantified)

| # | Principle | Statement | Quantified evidence |
|---|-----------|-----------|---------------------|
| **1** | Infrastructure > Instructions | Tool-call rules MUST be infrastructure (hooks/MCP-blocking), not prose. | Prose 25% → Hooks 100% (OpenArms v8→v10) |
| **2** | Structured Context > Content | Tables / MUST-lists / YAML program agents better than prose. Markdown is proto-programming. | Prose 25% → Tables 60% → Infra 100%+ |
| **3** | Goldilocks | Process scales with identity × phase × scale × trust tier. | Integration model $1.20/task vs feature-dev $9.07/task |
| **4** | Declarations Aspirational Until Verified | Every declared element needs a verification gate or it's aspirational. | 5 cross-layer instances (variable, schema, skill-attribute, VCS, compliance) |

Detail: [wiki/lessons/04_principles/hypothesis/](wiki/lessons/04_principles/hypothesis/).

## Hard Rules (every-message hot path)

| # | Rule | Enforcement |
|---|------|-------------|
| 1 | **Read command output IN FULL.** Never default to truncation. State a REASON before any `\| head` / `\| tail` / `\| grep`. Internal-tool output (gateway/view/pipeline) is curated — read every line. | pre-bash hook (`.claude/hooks/pre-bash.sh`) blocks truncation pipes — backstop only. |
| 2 | **When told to execute, execute.** Don't explain, don't ask, don't probe `--help`. Don't propose when asked to do. | Recurring drift. |
| 3 | **Use dedicated tools.** Read not cat. Grep not grep. Glob not find. Edit not sed. | System rule. |
| 4 | **Operator words are SACROSANCT — quote verbatim ALL THE TIME.** Never paraphrase, never dilute, never summarize. Verbatim quoting is the alignment mechanism: it lets the operator track that I processed their requirements correctly. Log to `raw/notes/` BEFORE acting (AGENTS.md Hard Rule #3). | `.claude/rules/work-mode.md` |
| 4a | **Adding ≠ discarding.** When the operator adds direction, layer it onto prior direction — never overwrite or drop earlier rules. Operator directive 2026-04-24: *"its not because I add something that you can discard everything I asked you before... when I add information, I add... I do not ask you to ignore the past...."* | Self-discipline; verbatim log preserves the full chain. |
| 5 | **Use `.venv/bin/python` for `tools.*` invocations.** System `python3` lacks venv-only deps. | Settings allow both; venv canonical. |
| 6 | **URL ingestion → pipeline fetch / `wiki_fetch` MCP. NEVER WebFetch for corpus URLs.** | pre-webfetch hook (`.claude/hooks/pre-webfetch-corpus-check.sh`) — see `.claude/rules/ingestion.md`. |
| 7 | **Status claims must inline verification.** "Done" / "loaded" / "regathered" without command-output evidence is P4 violation. | `.claude/rules/learnings.md` (2026-04-24 incident) |
| 8 | **Behave FROM the project, not OVER it.** MCP/CLI/loaded knowledge are the operating system, not external citations. | `.claude/rules/self-reference.md` |
| 9 | **Don't fabricate.** Operator never said it = don't claim they did. Investigate via project tools (`gateway query`, `pipeline status`, `lint`, `validate`) before asserting. | 2026-04-24 incident — `python3` bug invented. |
| 10 | **`pipeline post` after every wiki change.** 0 errors required. Don't claim done without inline output. | AGENTS.md Hard Rule #6. |

## Routing (operator intent → tool — summary)

Full 30-tool MCP catalog + 24-row routing table + CLI catalog: **[.claude/rules/routing.md](.claude/rules/routing.md)**.

| Operator says... | First action |
|---|---|
| `"ingest <url>"` / "new ingestions" / URL list | `pipeline fetch <urls>` OR `wiki_fetch` MCP. Then read raws → synthesis pages → `pipeline post` → `crossref`. |
| `"continue"` / "resume" / "where are we" | `gateway orient` OR `wiki_continue` MCP. |
| `"status"` / "what's next" | `pipeline status` OR `wiki_status` MCP. |
| `"log <directive>"` / verbatim quote | Write `raw/notes/YYYY-MM-DD-<slug>.md` BEFORE acting OR `wiki_log` MCP. |
| `"gaps"` / "what's missing" | `pipeline gaps` OR `wiki_gaps` MCP. |
| `"search"` / "read page" / "show me X" | `wiki_search` / `wiki_read_page` MCP, OR `tools.view search`. |
| `"evolve"` / "promote" | `pipeline evolve --score` OR `wiki_evolve` MCP. |
| `"validate"` / wiki change committed | `pipeline post` (MANDATORY). |
| Build/review model | Read `.claude/commands/build-model.md`. |
| Health / compliance / flow | `wiki_gateway_health` / `_compliance` / `_flow` MCPs. |

## Methodology Pointer

- Engine: [wiki/config/methodology.yaml](wiki/config/methodology.yaml) — 9 models, 5 universal stages, ALLOWED/FORBIDDEN per stage, gates.
- Schema: [wiki/config/wiki-schema.yaml](wiki/config/wiki-schema.yaml) — 9 required fields, 19 page types, 17 relationship verbs.
- Artifact types: [wiki/config/artifact-types.yaml](wiki/config/artifact-types.yaml) — 17 types, content thresholds, 3 artifact classes (document/artifact/documentation).
- All 16 named models: [wiki/spine/references/model-registry.md](wiki/spine/references/model-registry.md).
- Super-model: [wiki/spine/super-model/super-model.md](wiki/spine/super-model/super-model.md).

Detail: **[.claude/rules/methodology.md](.claude/rules/methodology.md)**.

## Self-Reference (this project IS the second brain)

The wiki at this repo IS the central intelligence hub for the 5-project ecosystem (this · OpenArms · OpenFleet · AICP · devops-control-plane). When operating here, the AI's brain = CLAUDE.md + AGENTS.md + .claude/rules/ + .claude/commands/ + the loaded super-model / principles / methodology / schema. The "second brain" the wiki teaches about IS this wiki itself.

Detail: **[.claude/rules/self-reference.md](.claude/rules/self-reference.md)**.

## Hook Layer (deterministic enforcement)

`.claude/hooks/` populated. Wired via [.claude/settings.json](.claude/settings.json) `hooks` block.

| Hook | Fires on | Purpose |
|---|---|---|
| `pre-webfetch-corpus-check.sh` | PreToolUse on WebFetch | Denies WebFetch on corpus URL patterns; redirects to pipeline fetch / wiki_fetch MCP |
| `pre-bash.sh` | PreToolUse on Bash | Blocks `\| head` / `\| tail` / `\| grep` truncation by default; requires `REASON=` env var to bypass |
| `session-start.sh` | SessionStart | (planned) Prints loaded-knowledge digest reminder |
| `post-compact.sh` | PostCompact | (planned) Restores key state references after compaction |

Detail: **[.claude/rules/hook-architecture.md](.claude/rules/hook-architecture.md)**.

## Pointers to Depth

| For... | Read |
|---|---|
| Universal cross-tool rules | [AGENTS.md](AGENTS.md) |
| Identity profile + active epics | [CONTEXT.md](CONTEXT.md) |
| Tool reference (full CLI catalog) | [TOOLS.md](TOOLS.md) |
| Architecture + data flow | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Page design + callouts | [DESIGN.md](DESIGN.md) |
| Skills directory context (skills not yet built; project uses commands + MCP + loaded knowledge) | [SKILLS.md](SKILLS.md) |
| Detailed topic rules | [.claude/rules/](.claude/rules/) |
| Operator-invoked slash commands | [.claude/commands/](.claude/commands/) |
| What this system IS | [wiki/spine/super-model/super-model.md](wiki/spine/super-model/super-model.md) |
| All 16 named models | [wiki/spine/references/model-registry.md](wiki/spine/references/model-registry.md) |

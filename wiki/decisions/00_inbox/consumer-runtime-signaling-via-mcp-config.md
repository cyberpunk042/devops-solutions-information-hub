---
title: "Decision — Consumer Runtime Signaling via MCP Config"
aliases:
  - "Decision — Consumer Runtime Signaling via MCP Config"
  - "Consumer Runtime Signaling"
  - "MCP Runtime Field"
type: decision
domain: cross-domain
layer: 6
status: draft
confidence: medium
maturity: seed
reversibility: easy
derived_from:
  - "Execution Mode Is a Consumer Property, Not a Project Property — Guard Against Conflation Drift"
  - "Model — MCP and CLI Integration"
  - "Adapters Never Raise — Failure As Data at Integration Boundaries"
contribution_status: pending-review
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: operator-directive-consumer-property
    type: directive
    file: raw/notes/2026-04-15-directive-execution-mode-is-consumer-property-not-project.md
    description: "Operator's proposal to explore: 'it would require development in back and forth with openarms and openfleet to allow them to use the tool and it detect automatically or simply maybe just inside the mcp config ? to explore.'"
  - id: consumer-property-lesson
    type: wiki
    file: wiki/lessons/00_inbox/execution-mode-is-consumer-property-not-project-property.md
    description: Lesson establishing that execution mode, SDLC profile, methodology model, and stage are consumer/task properties — not project properties. Names this decision as Open Question.
  - id: mcp-spec-config-format
    type: documentation
    url: https://modelcontextprotocol.io/docs/concepts/architecture
    description: MCP architecture spec — client-server handshake includes configuration dict that servers can inspect. The `runtime:` field is within the MCP protocol's extensibility surface.
tags: [decision, mcp, runtime, consumer-property, harness-signaling, fleet-signaling, declared-over-detected, execution-mode, cross-project]
---

# Decision — Consumer Runtime Signaling via MCP Config

## Summary

When a consumer (OpenArms harness, OpenFleet orchestrator, solo Claude session, or any other MCP client) connects to this wiki's MCP server, the consumer declares its runtime identity via the `MCP_CLIENT_RUNTIME` environment variable — set in the consumer's `.mcp.json` entry's `env:` block, which MCP clients propagate to spawned server subprocesses. The wiki reads `MCP_CLIENT_RUNTIME` on startup; absence defaults to `solo`. This is purely additive, backwards-compatible, uses a standard MCP mechanism (the `env:` field is part of the MCP client configuration spec), and is inherently honest about the limit of what can be known from inside the wiki — **only the consumer can state its own mode**. Alternatives (custom MCP-config field, handshake tool, per-call parameter, process-metadata inspection) were rejected for being non-standard, adding a round-trip, or re-introducing the detection-from-outside conflation this decision exists to prevent.

## Decision

> [!success] Decision
>
> | Scenario | Action |
> |---|---|
> | OpenArms v10 harness connects to wiki MCP | Consumer sets `"env": {"MCP_CLIENT_RUNTIME": "harness-openarms-v10"}` in its `.mcp.json` entry for `research-wiki` |
> | OpenFleet orchestrator connects | Consumer sets `"env": {"MCP_CLIENT_RUNTIME": "fleet-openfleet-v1"}` |
> | Solo Claude Code session | No declaration needed — default is `solo` |
> | Any MCP client | Optional env var; when set, wiki attaches it to session context + surfaces it in tools that care |
> | Wiki-side tool behavior | Tools that need runtime call `get_consumer_runtime()` from `tools.common`; fall back to `"solo"` when unset |

### Reference form

Example `.mcp.json` entry that a consuming project (e.g., OpenArms) would use to declare its runtime identity to the wiki:

```json
{
  "mcpServers": {
    "research-wiki": {
      "command": "python3",
      "args": ["-m", "tools.mcp_server"],
      "cwd": "/home/jfortin/devops-solutions-research-wiki",
      "env": {
        "MCP_CLIENT_RUNTIME": "harness-openarms-v10"
      }
    }
  }
}
```

The wiki's `tools/common.py` exposes `get_consumer_runtime()` which reads `MCP_CLIENT_RUNTIME` from the environment (defaulting to `"solo"` when absent or empty). The wiki's MCP server, gateway, and any tool that cares about runtime identity reads via this single helper. Valid values and the naming convention are documented in `wiki/config/mcp-runtime-values.yaml`.

### Why the env var and not a custom config field

Our initial framing proposed a custom `runtime:` field directly on the `.mcp.json` server entry. This does not work: MCP clients do not forward unknown config fields to the spawned server — only `command`, `args`, `cwd`, and `env` cross the process boundary. The `env:` block is the standard MCP-spec mechanism for passing configuration to a server subprocess, and every MCP client (Claude Code, Cursor, Continue, etc.) implements it. Using `env:` is therefore the only mechanism that works across all MCP clients without client-specific extensions.

## Alternatives

### Alternative A — Custom `runtime:` field on the MCP server entry (initial proposal)

Consumer adds a non-standard field `"runtime": "harness-openarms-v10"` directly on its `.mcp.json` server entry; wiki reads it on connect.

> [!warning] Rejected (after investigation)
>
> **MCP clients do not forward unknown fields to the spawned server.** Only `command`, `args`, `cwd`, and `env` cross the subprocess boundary. A custom field like `runtime:` would be silently ignored by Claude Code, Cursor, Continue, and other MCP clients — it never reaches the server's process environment. The `env:` block is the only MCP-spec-standard mechanism to pass configuration into a server subprocess. Using a custom field would require client-specific patches (add support in Claude Code, in Cursor, etc.), which defeats the goal of a cross-client declaration mechanism. The chosen `env:`-based approach (decision above) uses the same declarative channel the operator imagined, routed through the standard MCP mechanism.

### Alternative B — Initial handshake MCP tool `wiki_declare_runtime`

Consumer calls a dedicated `wiki_declare_runtime(runtime="harness-openarms-v10")` MCP tool immediately after connecting; the wiki attaches the result to the session.

> [!warning] Rejected
>
> **Adds a protocol round-trip to every session.** This works but costs one tool call per session that could be avoided by reading config on connect. Worse, it is **skippable** — a consumer that forgets to call it leaves the wiki uncertain about runtime. Silent skipping is exactly the failure mode the consumer-property lesson warns against: corrections that decay. A config field read at connect time cannot be forgotten. The handshake approach also conflates "declaration" (which is static per-consumer) with "tool use" (which is dynamic per-task).

### Alternative C — Per-call `runtime:` parameter on every MCP tool

Every MCP tool that cares about runtime accepts an optional `runtime:` parameter; caller passes it on each call.

> [!warning] Rejected
>
> **N-way repetition of a static-per-session value.** If a consumer's runtime is `fleet-openfleet-v1`, that's true for the entire session — asking callers to repeat it on every tool call creates duplication, drift risk, and noise. The consumer's runtime doesn't change mid-session; static-per-session declarations belong in connect-time config, not per-call parameters. Per-call parameters are right when a value varies per call (e.g., which page to read); wrong when it's a session-level constant.

### Alternative D — No signaling; rely on per-consumer client identification

The wiki inspects the connecting MCP client's process metadata (parent PID, executable name, command line) to guess the consumer.

> [!warning] Rejected
>
> **Heuristic detection of the exact thing the consumer-property lesson says is undetectable.** This is the failure mode the lesson caught: claiming to "detect" a consumer property from outside the consumer's declaration. Even if process-inspection happens to work for some consumers today, it breaks on: containerized deployments where parent PID is `docker`, Unix pipes that obscure the invoker, future consumers that don't match any known signature, and cases where the consumer WANTS to declare a different runtime than its process name suggests (a harness running in test mode, for example). Heuristics lie under edge conditions; declarations don't.

## Rationale

Four convergent reasons select Alternative 1 (MCP config field):

**1. Honesty about detection limits.** The consumer-property lesson establishes that execution mode cannot be detected from inside the project — only the consumer's runtime knows it. Any design that requires the wiki to "figure out" the consumer repeats the exact conflation the lesson prevents. An explicit declared field in the consumer's own config is the minimal structurally-enforced way to record this truth.

**2. MCP-native mechanism.** The MCP protocol already supports arbitrary config dict entries that the server can inspect. Using MCP config as the declaration channel means the declaration lives in the same file consumers already edit to configure wiki connection — no new file, no new mechanism, no parallel channel. This is the [[adapters-never-raise-failure-as-data-at-integration-boundaries|Adapters Never Raise]] principle applied at protocol layer: structured data carried at the integration boundary.

**3. Zero-cost backward compatibility.** The `runtime:` field is optional. Existing consumers that don't set it continue to work — the wiki defaults to `solo`. This satisfies the consumer-property lesson's rule that "solo is the default for every project." No consumer is forced to migrate; the field is purely additive. Upgrade path for OpenArms/OpenFleet is one config line each.

**4. Enables downstream precision without forcing it.** Tools that today give bad recommendations (e.g., `gateway what-do-i-need` recommending `simplified` because it can't tell harness from solo) gain a reliable signal. Tools that don't care about runtime (e.g., `wiki_search`, `wiki_read_page`) ignore it. No existing tool is forced to change; tools that want precision can opt in.

Empirical evidence supporting the choice:
- **Anthropic's own Effective Harnesses post** ([[src-anthropic-effective-harnesses-long-running-agents|Synthesis]]) uses JSON config for harness-level state that LLMs respect better than Markdown. Declaring runtime in MCP config (structured JSON-dict) follows the same principle.
- **OpenFleet's dispatch model** already passes agent context at invocation — consumer-declared runtime matches that shape. OpenFleet extending its MCP config to include `runtime:` is a one-line change.
- **The wiki's own gateway.py fix** (in this session) already reads declared identity as authoritative and defaults unset fields. Adding `runtime:` as another declared field fits the same pattern.

## Reversibility

**Rating: easy.** The `runtime:` field is purely additive:

- **Removing the field from the MCP server** — straightforward: delete the config-read call, tools default to `solo` as they already do when the field is absent. No consumer changes required (consumers can leave their unused `runtime:` declarations; the field is just ignored).
- **Migrating to a different mechanism** (e.g., if the MCP spec evolves to standardize this in a different field name) — trivial: rename on both sides with a one-release deprecation window where both forms are read.
- **Rolling back in a single project** — a consumer can simply omit the field; the wiki treats it as solo. No force-unbind step needed.

Downstream impact if reversed:
- `gateway what-do-i-need` loses the CONSUMER row's authoritative data → falls back to the current "solo is the default" honesty (still correct, just less specific when a harness is actually present).
- Any `wiki_*` tool that later added runtime-aware branching loses its signal → falls back to solo-default behavior.
- Wiki-side session logs lose the consumer-runtime column → gain less observability over who's using the brain.

None of these impacts corrupt data; they reduce observability. The decision is safe to make and safe to undo.

## Dependencies

**Wiki side — implemented this session (2026-04-15):**

1. ✅ **`tools/common.py`** — exposes `get_consumer_runtime()` (reads `MCP_CLIENT_RUNTIME` env var, defaults to `"solo"`) and `consumer_runtime_is_declared()` (true when env var set). Shared helper, imported by any tool that cares.
2. ✅ **`tools/gateway.py` `query_what_do_i_need`** — surfaces declared runtime with `✓ declared by consumer (via MCP_CLIENT_RUNTIME)` when set; shows "solo (default)" + configuration hint when unset.
3. ✅ **`wiki/config/mcp-runtime-values.yaml`** (new) — enumerates the convention (`<mode>-<project>-<version>[-<role>]`) + known values for current ecosystem projects (openarms, openfleet, aicp, devops-control-plane) + coordination process for new consumers.
4. ⏳ **Reference page** `wiki/domains/cross-domain/mcp-runtime-signaling.md` — TODO this session or next. Short integration guide for consumers.

**Required from each consuming project (their side):**

- **OpenArms** — add `"env": {"MCP_CLIENT_RUNTIME": "harness-openarms-v10"}` to its MCP server entry for `research-wiki`. Harness version bumps (`v10 → v11`) update the string.
- **OpenFleet** — add `"env": {"MCP_CLIENT_RUNTIME": "fleet-openfleet-v1"}` to its MCP dispatch configuration.
- **AICP** — add `"env": {"MCP_CLIENT_RUNTIME": "full-system-aicp-v1"}` when AICP's control-platform consumes the wiki.
- **devops-control-plane** — add `"env": {"MCP_CLIENT_RUNTIME": "solo-control-plane"}` if/when it adopts declared signaling.
- **Solo Claude** (including this wiki's own `.mcp.json` when connecting to another project's MCP) — no change needed; absence is correct default.

**Tools that benefit from the declared signal (but degrade gracefully when absent):**

- `gateway what-do-i-need` — shows declared runtime vs solo-default.
- Future `wiki_methodology_guide` enhancement — could route recommendations based on declared runtime (e.g., a fleet-consumer gets different suggestions than solo).
- Observability/compliance tools — can audit declared runtimes across consumer projects.

**Tools unaffected:**

- `wiki_search`, `wiki_read_page`, `wiki_list_pages`, etc. — these don't care about consumer runtime; they work identically regardless.

## Open Questions

> [!question] ~~Should `runtime:` values be namespaced by consumer project?~~
> **RESOLVED (v1):** Free-form strings like `harness-openarms-v10`. The namespacing convention lives in the value format `<mode>-<project>-<version>[-<role>]` documented in `wiki/config/mcp-runtime-values.yaml` — this gives the benefits of namespacing (parseable structure, grouping) without requiring nested YAML. Revisit if >3 consumers appear with need for programmatic comparison.

> [!question] ~~Should the wiki REJECT unknown runtime values?~~
> **RESOLVED (v1):** No — accept any string, log it. Implementation in `tools/common.py` returns the raw string to callers; observability tooling can filter on known vs unknown. Rejection would break new consumers on every wiki release before their values are registered in `mcp-runtime-values.yaml`. Accept-and-log preserves flexibility; a later opt-in validation mode can be added when observability data shows high typo/drift rates.

> [!question] How does runtime signaling interact with sub-agent dispatch?
> An OpenFleet orchestrator dispatches sub-agents that may independently connect to the wiki's MCP. Does each sub-agent inherit `fleet-openfleet-v1` or declare its own (e.g., `fleet-openfleet-v1-subagent-qa`)? This is similar to the [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]] question of sub-agent identity. Probably: sub-agents declare their own runtime; parent runtime is available via trace. Defer until OpenFleet design surfaces this concretely.

> [!question] Does the protocol belong in the MCP spec itself eventually?
> If multiple wikis adopt consumer-runtime signaling, this becomes a general-purpose MCP extension. The MCP spec team may want to standardize a `client_runtime` field. For now, this is a wiki-specific convention; upstream standardization is a future possibility.

## Relationships

- DERIVED FROM: [[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
- DERIVED FROM: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]
- DERIVED FROM: [[adapters-never-raise-failure-as-data-at-integration-boundaries|Adapters Never Raise — Failure As Data at Integration Boundaries]]
- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- RELATES TO: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
- ENABLES: [[four-project-ecosystem|Four-Project Ecosystem]]
- FEEDS INTO: [[model-ecosystem|Model — Ecosystem Architecture]]

## Backlinks

[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[adapters-never-raise-failure-as-data-at-integration-boundaries|Adapters Never Raise — Failure As Data at Integration Boundaries]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[mcp-runtime-signaling|MCP Runtime Signaling — Integration Guide for Consumers]]

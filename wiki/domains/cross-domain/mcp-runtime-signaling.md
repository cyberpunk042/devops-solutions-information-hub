---
title: "MCP Runtime Signaling — Integration Guide for Consumers"
aliases:
  - "MCP Runtime Signaling — Integration Guide for Consumers"
  - "MCP Runtime Signaling"
  - "MCP_CLIENT_RUNTIME"
type: reference
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: decision-consumer-runtime-signaling
    type: wiki
    file: wiki/decisions/00_inbox/consumer-runtime-signaling-via-mcp-config.md
    description: The decision establishing MCP_CLIENT_RUNTIME as the declaration mechanism.
  - id: consumer-property-lesson
    type: wiki
    file: wiki/lessons/00_inbox/execution-mode-is-consumer-property-not-project-property.md
    description: The lesson on why the consumer (not the wiki) must declare runtime.
  - id: runtime-values-config
    type: file
    file: wiki/config/mcp-runtime-values.yaml
    description: Enumeration of valid runtime values + convention + coordination process.
  - id: common-py-helper
    type: file
    file: tools/common.py
    description: "Wiki-side implementation: get_consumer_runtime() + consumer_runtime_is_declared()."
tags: [reference, mcp, runtime-signaling, consumer-declaration, integration-guide, harness, fleet, openarms, openfleet, aicp]
---

# MCP Runtime Signaling — Integration Guide for Consumers

## Summary

This page is for anyone integrating a consuming project (harness, fleet, orchestrator, solo session) with this wiki's MCP server. It tells you **what to set, where to set it, and what to expect** — the minimum viable integration. Full design rationale lives in the decision page; this is the operator-facing how-to.

## The one thing you need to do

Add `MCP_CLIENT_RUNTIME` to the `env` block of your `.mcp.json` entry for `research-wiki`:

```json
{
  "mcpServers": {
    "research-wiki": {
      "command": "python3",
      "args": ["-m", "tools.mcp_server"],
      "cwd": "/path/to/devops-solutions-research-wiki",
      "env": {
        "MCP_CLIENT_RUNTIME": "<your-runtime-value>"
      }
    }
  }
}
```

That's it. Everything else is optional.

## What value to use

Pick the value that matches your consumer's mode. The convention is `<mode>-<project>-<version>[-<role>]`.

| Your consumer | Value to use |
|---|---|
| OpenArms harness v10 | `harness-openarms-v10` |
| OpenArms harness v11 (when released) | `harness-openarms-v11` |
| OpenFleet orchestrator v1 | `fleet-openfleet-v1` |
| AICP full-system v1 | `full-system-aicp-v1` |
| devops-control-plane (solo Claude sessions) | `solo-control-plane` |
| Solo Claude Code (no harness) | **Don't set the var.** Absence defaults to `solo` — the correct value. |
| Sub-agent dispatched by a fleet | `sub-agent-openfleet-v1-<role>` (e.g., `...-qa`) |
| Your new consumer | See `wiki/config/mcp-runtime-values.yaml` — register your value there via PR |

## What happens when you set it

The wiki's gateway-level tools (e.g., `gateway what-do-i-need`) surface the declared runtime:

```
CONSUMER / TASK PROPERTIES (not project properties):
  execution mode: harness-openarms-v10  ✓ declared by consumer (via MCP_CLIENT_RUNTIME)
```

The wiki does NOT currently branch tool behavior on the declared runtime — this is observability infrastructure, not enforcement. Future tools may read the runtime to tailor recommendations (e.g., a fleet-consumer gets different suggestions than a solo-consumer), but the current set (`wiki_search`, `wiki_read_page`, etc.) works identically regardless.

## What happens when you DON'T set it

Nothing breaks. The wiki defaults to `solo`:

```
CONSUMER / TASK PROPERTIES (not project properties):
  execution mode: solo (default — no consumer declared otherwise)
                  A harness or fleet that wraps this project DECLARES non-default via its
                  `.mcp.json` entry's env block: {"env": {"MCP_CLIENT_RUNTIME": "harness-<name>-<version>"}}.
                  From inside this project we cannot detect which consumer (if any) is using us.
```

Solo IS the default for every project. You only set the env var if you are NOT solo.

## Why this mechanism and not another

If you were expecting a `"runtime":` field directly on the MCP config entry, you'd be in good company — that was our initial proposal. It doesn't work: MCP clients only forward `command`, `args`, `cwd`, and `env` to the spawned server subprocess. Other fields are silently ignored. `env:` is the standard MCP mechanism for passing configuration into a server, which is why we use it.

For the full reasoning (including why env vars aren't "out of band", why handshake tools were rejected, and why process-metadata inspection was rejected), see [[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]].

## Registering a new value

If your consumer doesn't fit any existing value:

1. Pick a value matching the convention `<mode>-<project>-<version>[-<role>]`.
2. Add an entry to `wiki/config/mcp-runtime-values.yaml` under `known_values` with project, description, project_remote, and status.
3. Open a PR. Registration is advisory — the wiki accepts any string — but it makes your runtime visible to observability and to other consumers.

## Implementation reference (wiki side)

Wiki-side code that consumes the declared runtime:

```python
from tools.common import get_consumer_runtime, consumer_runtime_is_declared

runtime = get_consumer_runtime()             # "solo" or the declared value
declared = consumer_runtime_is_declared()    # bool — was MCP_CLIENT_RUNTIME actually set?
```

See `tools/common.py` for the implementation (~15 LOC). Any wiki tool can call these helpers.

## Why only the consumer can declare this

The wiki lives inside a repository on disk. A harness or fleet consumes the wiki from elsewhere — possibly a different machine, a different process, or a container. **From inside the wiki's own directory, we cannot observe which consumer is using us.** The consumer's own runtime is the only authoritative source of this information. Any attempt to "auto-detect" execution mode from within the wiki is a tautology at best (solo-if-no-harness-code-here, which is always trivially true locally) or incorrect at worst (guessing wrong when containers, pipes, or remote clients obscure process metadata).

This is the three-layer orthogonality established in [[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]:

| Layer | Properties | Who declares |
|---|---|---|
| Stable project identity | type, domain, second-brain | The project (in CLAUDE.md/CONTEXT.md) |
| Phase / scale state | phase, scale | The project (owner reviews periodically) |
| Consumer / task properties | execution mode, SDLC profile, methodology model, current stage | **The consumer** (per-session/per-task) |

MCP_CLIENT_RUNTIME is how the consumer expresses the first property in that third row. SDLC profile and methodology model are per-task and don't need session-level declaration.

## Open Questions

> [!question] Should the wiki reject unknown runtime values?
> Currently: accept any string, log it. Alternative: validate against `mcp-runtime-values.yaml` and reject unknowns. We picked acceptance for v1 — rejection would break new consumers on release. Will revisit if observability data shows high rates of typos/drift.

> [!question] How do sub-agents inherit runtime from a dispatching fleet?
> If OpenFleet dispatches a sub-agent that also connects to the wiki's MCP, should the sub-agent set `sub-agent-openfleet-v1-<role>` or inherit `fleet-openfleet-v1`? The current answer: sub-agents declare their own role-specific value. Open for coordination with OpenFleet.

> [!question] Could this become an MCP-spec upstream feature?
> If multiple MCP servers independently adopt a `client_runtime` convention, there's a case for standardizing it in the MCP spec itself. For now it's a wiki-specific env var; upstream is a future consideration.

## Relationships

- BUILDS ON: [[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]]
- BUILDS ON: [[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
- RELATES TO: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
- RELATES TO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]
- ENABLES: [[four-project-ecosystem|Four-Project Ecosystem]]

## Backlinks

[[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]]
[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[four-project-ecosystem|Four-Project Ecosystem]]

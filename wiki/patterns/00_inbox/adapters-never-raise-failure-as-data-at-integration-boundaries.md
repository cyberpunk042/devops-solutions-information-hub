---
title: "Adapters Never Raise — Failure As Data at Integration Boundaries"
aliases:
  - "Adapters Never Raise"
  - "Failure As Data"
  - "Receipt Pattern"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: medium
maturity: seed
derived_from:
  - "Infrastructure Over Instructions for Process Enforcement"
  - "Three Lines of Defense — Immune System for Agent Quality"
  - "Block With Reason and Justified Escalation"
instances:
  - page: "devops-control-plane Adapter/Receipt system"
    context: "Canonical form. Adapters (shell/filesystem/git/docker/python/node) execute Actions from the engine and return Receipts. Explicit rule: `Adapters never raise exceptions. All failures are captured in the Receipt.` validate() returns (ok, error_message); execute() returns Receipt.success or Receipt.failure; AdapterRegistry integrates circuit-breaker — repeated failures short-circuit to failure receipts."
  - page: "Research Wiki integrations.py"
    context: "Obsidian + NotebookLM wrappers follow the same shape. is_available() gates execution, subprocess errors caught and returned as {ok: False, error: ...}, timeout handling produces failure dicts not exceptions, fallback paths (grep when Obsidian CLI absent) preserve the contract that callers never handle exceptions."
  - page: "Research Wiki validate.py"
    context: "Failure-as-data in the schema-validation domain. validate_page() returns {errors: [...], warnings: [...]} — never raises. Each error has a code + message + field for programmatic handling. Pipeline post aggregates across pages and gates commit on error count — the structured form is what makes the gate mechanical."
  - page: "OpenFleet immune-system detection functions"
    context: "detect_protocol_violation / detect_laziness / detect_stuck / detect_correction_threshold all return health reports (detections, interventions, agents_to_skip) — not exceptions. The 30s doctor cycle reads these reports as data and chooses TEACH/COMPACT/PRUNE/ESCALATE responses. Structured failure signal enables graduated response."
  - page: "Research Wiki MCP tool surfaces"
    context: "wiki_* MCP tools return JSON payloads including error dicts ({'error': ...}) instead of raising — crucial because the MCP caller (Claude Code) cannot handle Python exceptions. Same pattern enforced by the protocol: results are data."
  - page: "Research Wiki sister_project.py"
    context: "list_epics / list_tasks / read_doc / read_all all return Dict or List — errors become {'error': 'message'} entries inline, never raised. Recently-discovered bug (NotADirectoryError on file-sentinel layout entries) was a REGRESSION of this pattern — fix added is_dir() guard to restore the contract."
contribution_status: pending-review
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: devops-control-plane-adapters
    type: observation
    project: devops-control-plane
    path: docs/ADAPTERS.md
    description: "Canonical specification — 'An adapter is a pluggable component that executes actions against external tools. Adapters never raise exceptions. All failures are captured in the Receipt.' Includes circuit-breaker integration, mock mode for testing, raw command fallback, explicit Adapter ABC with name/is_available/validate/execute methods. Verified 2026-04-15."
  - id: research-wiki-integrations-py
    type: file
    file: tools/integrations.py
    description: "Our integration wrappers — same shape as control-plane's Adapter. is_available() check, subprocess with timeout, graceful fallback, structured dict returns. Natural instance on this-wiki side."
  - id: research-wiki-validate-py
    type: file
    file: tools/validate.py
    description: "Schema validation using failure-as-data. validate_page returns {errors, warnings} — 356 lines, never raises, entire pipeline-post quality contract runs through it."
tags: [pattern, adapter, receipt, failure-as-data, fault-tolerance, integration-boundary, no-exceptions, cross-domain, convergent-evidence]
---

# Adapters Never Raise — Failure As Data at Integration Boundaries

## Summary

At integration boundaries between a system and anything external — another process, a filesystem, a network call, a sister project's API, an LLM — **failure must be returned as data, not raised as an exception**. The caller receives a structured result (Receipt, ValidationResult, health report, error-dict) that encodes success, failure mode, and enough diagnostic information to route the next action. The rule is simple and absolute: **the boundary function never raises.** This pattern recurs across the entire 5-project ecosystem (devops-control-plane adapters, OpenFleet immune-system detection, our wiki's integrations/validation/MCP/sister-project tooling) because at integration boundaries the caller cannot practically handle exceptions — either the caller is a different process (MCP over stdio), a different language (the agent consuming tool output), or a loop that must continue (doctor cycle, retry chain, multi-file validator). Raising exceptions crosses boundaries poorly; data crosses them cleanly.

> [!info] Pattern Reference Card
>
> | Element | What it produces | Failure if omitted |
> |---|---|---|
> | **Structured result type** | Receipt / ValidationResult / {ok, error, ...} — fixed shape | Caller can't program against arbitrary exception types |
> | **is_available / validate pre-flight** | Fast rejection before committing to execution | Full execution cost spent on known-failure inputs |
> | **try/except inside the adapter** | Unknown exceptions converted to failure results at the boundary | Exceptions leak across boundary; caller must know every exception type |
> | **Diagnostic payload** | code + message + field/context the caller can route on | Caller gets a generic failure; can't build graduated response (like doctor's TEACH/COMPACT/PRUNE) |

## Pattern Description

The adapter/receipt pattern is the dual of exception-propagation at system boundaries. Inside a tight module, exceptions are fine — they flow up the stack in the same language/runtime/process with full context. Across a boundary, they break: the receiving side doesn't share the stack, the runtime, or sometimes the language. The pattern substitutes **structured data** at the boundary and reserves **exception propagation** for intra-module concerns.

**Three rules that together constitute the pattern:**

1. **Boundary functions have a total type.** `execute()` returns `Receipt`, always. `validate_page()` returns `{errors, warnings}`, always. `is_available()` returns `bool`, always. No code path raises. If internal logic raises, the adapter catches and converts.
2. **Failures are as structured as successes.** A Receipt.failure carries `error` + `adapter` + `action_id` — the same fields as Receipt.success minus the output. Callers can route on failure shape as easily as on success shape.
3. **The boundary is where the pattern applies, not everywhere.** Internal helpers within the adapter can and should raise on programming errors (assertion failures, impossible states) — those exceptions get caught at the public method and converted. The pattern is about the public API surface, not about eliminating exceptions globally.

### Why this pattern matters specifically for agent-integrated systems

AI agents making tool calls are fundamentally cross-boundary consumers. An MCP tool called by Claude Code is a different process speaking JSON-RPC; Claude cannot pattern-match Python exception types. A sub-agent executing a tool call receives the output as text or JSON — exception tracebacks arrive as unstructured noise. A harness validating a stage gate reads a command's stdout/stderr and exit code — same story. **The consumer is always external to the producer's runtime.** Data crosses cleanly; exceptions don't.

Secondary consequence: **the pattern enables graduated response.** The immune system's TEACH/COMPACT/PRUNE/ESCALATE ladder works because detection functions return structured reports, not exception spew. The ladder routes on the shape of the signal. If detections raised, the doctor would have to catch-and-classify — pushing the structure back to where it already should have been.

### Relationship to the principles

- **Infrastructure Over Instructions**: the pattern IS infrastructure — the structured result is what enables mechanical handling downstream. Prose "please return an error message" is instruction; `Receipt` as a type enforced by tests is infrastructure.
- **Structured Context Principle**: the same rule applied at the code level. Structured results program caller behavior the same way structured markdown programs agent behavior.
- **Three Lines of Defense**: Line 2 (Detection) depends on this pattern — the detection functions must return failure as data, or the doctor cycle can't route.

## Instances

| Instance | Boundary crossed | Structured shape | Notable property |
|---|---|---|---|
| **devops-control-plane Adapters** | Engine ↔ external CLI tools (shell/git/docker/python/node) | `Receipt.success(output=...)` / `Receipt.failure(error=...)` | Circuit-breaker at registry level — repeated failure receipts open the breaker |
| **Research Wiki integrations.py** | Python ↔ Obsidian CLI / NotebookLM daemon (external processes) | `{ok: bool, result?, error?}` dict | Graceful fallback: when Obsidian CLI unavailable, falls back to grep — caller contract preserved |
| **Research Wiki validate.py** | Python ↔ user page content (filesystem data) | `{errors: [...], warnings: [...]}` list-of-dicts | Each issue has `code` + `message` + optional `field` — programmable downstream |
| **OpenFleet immune-system detection** | Doctor ↔ running agent sessions | `{detections, interventions, agents_to_skip, tasks_to_block}` report | Enables TEACH/COMPACT/PRUNE/ESCALATE graduated response |
| **Research Wiki MCP tools** | MCP server (Python) ↔ Claude Code (subprocess, JSON-RPC) | JSON dict, error cases return `{"error": "..."}` | Protocol-required: MCP callers cannot catch Python exceptions |
| **Research Wiki sister_project.py** | Browser ↔ sister-project filesystem (other repos) | Dict (single-read) or List (bulk-read) with `error` keys inline | Never raises; recent `is_dir()` fix was a regression-repair to maintain this contract |

> [!example]- Detailed: control-plane canonical form vs our integrations.py
>
> **control-plane:**
> ```python
> class MyAdapter(Adapter):
>     def validate(self, context) -> tuple[bool, str]: ...
>     def execute(self, context) -> Receipt:
>         try:
>             result = do_something(context.action.params)
>             return Receipt.success(adapter=self.name, output=result, ...)
>         except Exception as e:
>             return Receipt.failure(adapter=self.name, error=str(e), ...)
> ```
>
> **Our integrations.py (Obsidian):**
> ```python
> def search(self, query: str, ...) -> Dict[str, Any]:
>     if self.is_available():
>         return self._run("search", f"query={query}", ...)  # → {ok, result|error}
>     # Fallback: grep wiki files — still returns same-shape dict
>     results = []
>     for page in find_wiki_pages(self._vault_path):
>         text = page.read_text(encoding="utf-8", errors="ignore")
>         if query.lower() in text.lower():
>             results.append(...)
>     return {"ok": True, "results": results, "fallback": "grep"}
> ```
>
> Same contract. Different domain. Same invariant: **no raise at the boundary.** The fallback path in our code is a refinement — when the preferred backend is unavailable, return a successful result with a different backend and a flag indicating the degradation. This is what "failure-as-data" enables: a richer vocabulary than success/failure (partial / fallback / degraded / cached / stale / ...).

## When To Apply

> [!tip] Apply this pattern at boundaries where
>
> - The caller is a different process (subprocess, MCP, WebSocket, HTTP)
> - The caller is a different language (Python function called from JSON agent, TypeScript harness consuming Python output)
> - The caller is a loop that must continue (doctor cycle, retry chain, batch validator)
> - The failure vocabulary is richer than success/failure (fallback, cached, degraded, partial)
> - Circuit-breaker or graduated-response patterns depend on counting structured failures
> - You are integrating a tool whose errors are recoverable (vs. programming errors that should crash)
> - Tests need to assert specific failure modes (easier to assert on {error: "X"} than on raised exception types across module boundaries)

## When Not To

> [!warning] Do NOT apply when
>
> - The caller IS in the same module/runtime and can handle exceptions richly — pattern adds noise for zero benefit
> - The failure is a programming error, not a runtime error (AssertionError, KeyError on a dict you built yourself) — those should crash
> - The function is a tight inner loop where the allocation cost of building a result object dominates — measure first, but this is rare
> - You don't control the caller and the caller expects exceptions (language/library convention) — matching the convention matters more than the pattern
>
> The most common mistake: applying this pattern EVERYWHERE, including internal helpers. That defeats exception propagation inside the module where it's useful. The pattern is about BOUNDARY functions specifically — the public surface the adapter exposes to external consumers.

## Convergence Across the Ecosystem

This pattern was independently arrived at by:

- **devops-control-plane**: designed adapter/receipt explicitly with "never raise" as an axiom
- **OpenFleet**: designed immune-system detection to return health reports, enabling graduated correction
- **Our MCP server**: forced by MCP protocol constraints to return JSON, can't raise across process boundary
- **Our validation pipeline**: designed to aggregate per-page issues across hundreds of files — single exception would halt the batch, defeating the tool's purpose
- **Our integrations wrappers**: subprocess failures and timeouts would otherwise need try/except at every caller

Five projects, five different drivers, one convergent structure. That convergence is evidence of the pattern's strength — each project arrived at the same answer solving related but distinct problems. The pattern is not a preference; it is structural for multi-process / multi-agent / multi-runtime systems.

## Open Questions

> [!question] Should we formalize a `Receipt` type in tools/common.py and refactor integrations.py + sister_project.py to use it?
> Current state: each module uses ad-hoc dict shapes ({ok, error}, {errors, warnings}, etc.). A shared type would enforce consistency but is intrusive. Worth it? Open.

> [!question] Does this pattern extend to the wiki's contribution flow (gateway contribute)?
> Currently gateway contribute returns a dict. Could benefit from Receipt-shaped result. Unclear if the caller population (agents, humans) benefits enough to justify.

> [!question] How should this pattern interact with the [[block-with-reason-and-justified-escalation|Block With Reason and Justified Escalation]] pattern?
> They compose: a boundary function that needs operator input returns a failure-result whose diagnostic payload is a block-with-reason escalation structure. Worth explicit composition docs.

## Relationships

- DERIVED FROM: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- DERIVED FROM: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
- BUILDS ON: [[block-with-reason-and-justified-escalation|Block With Reason and Justified Escalation]]
- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
- RELATES TO: [[observe-fix-verify-loop|Observe-Fix-Verify Loop]]
- FEEDS INTO: [[four-project-ecosystem|Four-Project Ecosystem]]

## Backlinks

[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[block-with-reason-and-justified-escalation|Block With Reason and Justified Escalation]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[observe-fix-verify-loop|Observe-Fix-Verify Loop]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]]

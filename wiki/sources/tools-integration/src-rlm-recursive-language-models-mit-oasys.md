---
title: "Synthesis — RLM (Recursive Language Models): Task-Agnostic Inference for Near-Infinite Contexts via REPL + Recursion (MIT OASYS, Dec 2025)"
aliases:
  - "Recursive Language Models"
  - "RLMs"
  - "RLM — Recursive Language Models"
  - "Synthesis — Recursive Language Models"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: rlm-paper-arxiv
    type: paper
    url: https://arxiv.org/abs/2512.24601
    title: "Recursive Language Models (Zhang, Kraska, Khattab — MIT OASYS — Dec 2025)"
    description: "The arXiv preprint expanding the Oct 2025 blogpost into a formal paper with experimental results"
  - id: rlm-blogpost
    type: article
    url: https://alexzhang13.github.io/blog/2025/rlm/
    title: "Recursive Language Models Blogpost (Oct 2025)"
    description: "Original idea + initial experiments that preceded the arXiv paper"
  - id: rlm-repo
    type: documentation
    url: https://github.com/alexzhang13/rlm
    file: raw/articles/alexzhang13rlm.md
    title: "alexzhang13/rlm — Reference Implementation"
    ingested: 2026-04-27
  - id: rlm-minimal
    type: documentation
    url: https://github.com/alexzhang13/rlm-minimal
    title: "RLM Minimal — Stripped-down companion repo"
  - id: rlm-docs-site
    type: documentation
    url: https://alexzhang13.github.io/rlm/
    title: "RLM Documentation Site"
tags: [rlm, recursive-language-models, repl, context-engineering, harness, inference-paradigm, mit-oasys, near-infinite-context, task-agnostic, dec-2025-arxiv, mission-2026-04-27, tier-0-candidate, tools-integration, llm-query, rlm-query, depth-recursion, sandbox-environments, anthropic-harness-precedent]
---

# Synthesis — RLM (Recursive Language Models)

## Summary

Recursive Language Models (RLMs) are a task-agnostic inference paradigm from MIT's OASYS lab (Alex L. Zhang, Tim Kraska, Omar Khattab — [arXiv 2512.24601](https://arxiv.org/abs/2512.24601), December 2025) that replace the canonical `llm.completion(prompt, model)` call with `rlm.completion(prompt, model)`. The mechanism: the LM receives its input as a VARIABLE in a Python REPL environment rather than as a concatenated input string, and can *programmatically* examine, decompose, and recursively call itself over its own input. The reference implementation at [alexzhang13/rlm](https://github.com/alexzhang13/rlm) wraps three cooperating pieces — an `RLM` iteration loop, a per-completion `LMHandler` TCP socket server that routes LM API calls, and a `LocalREPL` (or isolated cloud sandbox: docker, modal, prime, daytona, e2b) that executes model-generated code via Python `exec()` in a persistent namespace. Two primitives are exposed inside the REPL: `llm_query()` (a plain non-recursive LM completion) and `rlm_query()` (which spawns a child RLM with its own REPL + iteration loop, falling back to `llm_query` at `max_depth`). The model decides WHEN to spend tokens recursively versus directly answer, can decompose long contexts (the original prompt becomes the `context` variable, addressable as `context[:5000]` or `len(context)` etc.), and can batch sub-calls via `llm_query_batched`/`rlm_query_batched`. This is a *structural* answer to the long-context problem that does not depend on growing context windows — instead it treats context as data the LM operates on through code, the same way human researchers operate on documents through Python notebooks rather than by reading every line into working memory simultaneously.

## Reference Card

> [!info] Source reference card
>
> | Field | Value |
> |---|---|
> | **Type** | Inference paradigm + reference SDK + paper |
> | **Authors** | Alex L. Zhang · Tim Kraska · Omar Khattab |
> | **Lab** | MIT OASYS (Optimization And Systems Yielding Speed?) — Kraska's group; Khattab is the DSPy / ColBERT author |
> | **arXiv** | 2512.24601 (Dec 2025) |
> | **Blogpost** | alexzhang13.github.io/blog/2025/rlm/ (Oct 2025) |
> | **Repo** | github.com/alexzhang13/rlm |
> | **Minimal companion** | github.com/alexzhang13/rlm-minimal |
> | **Documentation site** | alexzhang13.github.io/rlm |
> | **Pip** | `pip install rlms` |
> | **Python** | 3.11+ (3.12 recommended) |
> | **Backends supported** | openai · anthropic · portkey · openrouter · vllm |
> | **Environments supported** | local (default) · docker · modal · prime · daytona · e2b |
> | **CI** | GitHub Actions (style + test workflows) |
> | **Status** | "Functional for most use cases" but "isn't super fast yet" per CONTRIBUTING.md |
> | **Maintainers** | MIT OASYS lab authors; open-source contributions welcomed |
> | **Confidence label for this synthesis** | high — read the README, AGENTS.md, CONTRIBUTING.md, full API reference (api/rlm.md, ~600 lines), full architecture doc (architecture.md, ~340 lines), and getting-started.md as Layer 1 implementation evidence; only the package-lock.json dependency tree was skipped as Layer 0 noise |

## Key Insights

1. **The paradigm shift is moving context from INPUT to VARIABLE.** Canonical inference: the entire prompt is concatenated into a single input string the LM consumes in one forward pass. RLM: the prompt becomes the value of a Python variable named `context` in a REPL the LM operates on through code. The LM can write `print(len(context))`, `chunk = context[:10000]`, `metrics = llm_query("Extract metrics: " + chunk)`, etc. The model is no longer a function `f(prompt) → answer`; it's an iterative program that interacts with its own input over many turns. This is structurally different from "longer context windows."

2. **`llm_query()` and `rlm_query()` are the two primitives that distinguish flat vs recursive sub-calls.** `llm_query(prompt, model=None)` makes a single, plain, non-iterative LM completion — fast, cheap, no REPL of its own. `rlm_query(prompt, model=None)` spawns a *child RLM* with its OWN REPL environment + iteration loop, recursing into the same paradigm one level deeper. When `depth >= max_depth`, `rlm_query` falls back to `llm_query` (terminating recursion at a leaf). Together: the model can choose decomposition strategies the user did not pre-specify.

3. **Depth is bounded; resources propagate.** `max_depth=2` permits one level of `rlm_query` recursion (root → child → leaf); deeper calls become plain `llm_query` automatically. Critically, the parent passes *remaining* budget/timeout/tokens to children, not the original totals — so a child cannot consume all of the parent's resources by accident. Each child gets its own fresh `LMHandler` (TCP server on a different auto-assigned port) and its own `LocalREPL` (isolated namespace). State doesn't leak between parent and child.

4. **In-process `exec()` is the default — fast but not a security boundary.** `LocalREPL` runs model-generated code in the SAME Python interpreter via `exec(code, globals, locals)`. There is no subprocess, no fork, no IPC for code execution. Variables persist across iterations (state accumulates in `self.locals`). Helper functions like `llm_query` are plain Python closures in `self.globals`. Dangerous builtins (`eval`, `exec`, `compile`, `input`) are removed from the namespace as a "soft sandbox" — explicitly NOT a security boundary; for adversarial inputs use Docker/Modal/Prime sandboxes instead.

5. **Five cloud-sandbox environments supported for isolation: docker, modal, prime, daytona, e2b.** Isolated environments cannot directly connect to the host's `LMHandler` socket server, so they use an HTTP broker pattern: a Flask broker server runs INSIDE the sandbox; sandbox code POSTs LM requests to `localhost:8080/enqueue` (which blocks); the host polls the broker's tunnel URL on `/pending`, forwards requests to `LMHandler` over its socket, and POSTs responses back to `/respond`. Polling interval 100ms; serialization via `dill` to `/tmp/rlm_state.dill`. This is a complete, reusable architecture for any cloud-sandbox environment that can't share a process.

6. **The wire protocol is 4-byte big-endian length prefix + UTF-8 JSON payload.** Implemented in `socket_send()` / `socket_recv()` in `rlm/core/comms_utils.py`. Same protocol whether the REPL is in-process (LocalREPL talks to LMHandler over `127.0.0.1`) or cloud-sandboxed (broker forwards to LMHandler). Consistency by design — the protocol does not branch on environment type.

7. **Five LM backends supported with depth-based routing.** Backends: `openai`, `anthropic`, `portkey`, `openrouter`, `vllm`. The `LMHandler` can hold multiple clients and routes by `(model, depth)` in the request: explicit model name → that client; `depth == 1` AND `other_backend_client` set → route to the other backend (cheaper sub-calls); else → default client. So a user can configure: "root uses Claude Sonnet 4; sub-calls use GPT-4o-mini" by passing `other_backends=["openai"]` + `other_backend_kwargs=[{"model_name": "gpt-4o-mini"}]`. Cost optimization is a first-class routing dimension.

8. **Trajectory logging is opt-in but designed-in.** Pass `RLMLogger()` for in-memory metadata-on-completion (`result.metadata` becomes a full trajectory dict); pass `RLMLogger(log_dir="./logs")` to also write JSONL files for the included Node.js/shadcn visualizer (`cd visualizer && npm run dev`). Each iteration's response, code blocks, sub-LM calls, and final answer are captured with a metadata tree that recurses through child RLMs (children's trajectories nest in the parent's `rlm_calls` list). This is the project's debugging affordance — without it, recursive trajectories are opaque.

9. **Resource limits are explicit exceptions, not silent caps.** `BudgetExceededError`, `TimeoutExceededError`, `TokenLimitExceededError`, `ErrorThresholdExceededError`, `CancellationError` are all importable from the top-level package; each carries `partial_answer` so the caller can extract whatever was computed before the limit hit. The default config has all of these as `None` (no limits) — the user opts in. This is the "fail fast, fail loud" philosophy stated explicitly in AGENTS.md ("Missing API key → immediate `ValueError`, not graceful fallback").

10. **Persistence + compaction are real, not advisory.** `persistent=True` reuses the same environment across multiple `rlm.completion()` calls, with versioned contexts (`context_0`, `context_1`, ...) and conversation histories (`history_0`, `history_1`, ...) — usable as a multi-turn session where each call layers on more context. `compaction=True` auto-summarizes the conversation history when token usage exceeds `compaction_threshold_pct=0.85` of the model's context window; the full history (including summaries) remains available in the REPL as `history`. Both are off by default; both are concrete features rather than design intentions.

11. **Custom tools at the REPL level + separate `custom_sub_tools` for children.** Pass `custom_tools={"fetch_data": my_fn, "API_KEY": "..."}` and the model can call `fetch_data(...)` inside the REPL. Tools support a dict-with-description form `{"tool": fn, "description": "..."}` whose descriptions auto-inject into the system prompt. Reserved names (`llm_query`, `rlm_query`, `context`, `history`, `FINAL_VAR`, `SHOW_VARS`) cannot be overridden as tool names. `custom_sub_tools` lets parent and children expose different tool sets — pass `{}` to disable for children, or a different dict for delegation.

12. **The default RLM system prompt teaches the model how to use the REPL.** The default prompt covers: how to use `context`, when to call `llm_query()` vs `rlm_query()`, the batched variants, how to signal completion via `FINAL()` / `FINAL_VAR(variable_name)` / `SHOW_VARS()`. Override via `custom_system_prompt`. This is structured-context-as-IaC at the system-prompt level — the prompt is the program that teaches the model the REPL contract.

13. **The repo is small and readable on purpose.** CONTRIBUTING.md says explicitly: "I'd like to keep the repo as minimal as possible for as long as possible so it's still easy for users to read the entire repo in a short sitting." The minimal companion repo at `alexzhang13/rlm-minimal` strips it further. This is a research-paper-with-reference-implementation — the code IS the artifact, not infrastructure for production deployments.

14. **Convergence with Anthropic's Nov 2025 long-running-agents pattern.** The wiki's existing source [Anthropic — Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) (Nov 2025) found that compaction alone is insufficient for tasks spanning multiple context windows; the fix was explicit harness artifacts (`feature_list.json`, `claude-progress.txt`, `init.sh`) that the agent reads at session start. RLMs encode the SAME insight at a different abstraction: context becomes a *variable* the agent reads through code, not a string concatenated into the prompt. Both arrive at "context as data, not input" by independent paths.

15. **Mission-relevant: smaller models + recursion may approach larger models' capability on long-context tasks.** The implication operator's mission cares about: a Qwen3.6-27B local instance with `max_depth=2` and `rlm_query` could potentially handle context tasks normally requiring Opus 4.7's 200K window — by chunking the context, processing chunks in parallel sub-calls, and synthesizing. This is structural cost reduction, complementary to the wiki's existing $540→$100 smart-routing finding. (Empirical validation pending — this insight is structural; benchmark comparison vs Opus on operator's tier-0 hardware is the load-bearing next test.)

## Deep Analysis

### 1. The Paradigm Shift — Context as Variable, Not Input

> [!info] Two views of the same task: "summarize this document"
>
> **Canonical LM:**
> ```python
> response = openai.chat.completions.create(
>     model="gpt-4o",
>     messages=[{"role": "user", "content": f"Summarize this:\n{long_doc}"}]
> )
> # Document is concatenated into the prompt; consumed in one forward pass
> # If long_doc exceeds context window → truncate or fail
> ```
>
> **RLM:**
> ```python
> rlm = RLM(backend="openai", backend_kwargs={"model_name": "gpt-4o"})
> result = rlm.completion(long_doc, root_prompt="Summarize this document")
> # Document becomes `context` variable in the REPL
> # Model can: print(len(context)), chunk = context.split('\n\n'),
> #   summaries = llm_query_batched([f"Summarize: {c}" for c in chunk]),
> #   final = llm_query("Combine: " + "\n".join(summaries))
> # Document length is bounded only by the model's ability to programmatically chunk it
> ```

The shift is structural: the LM's relationship to its input changes from "consume in one shot" to "operate on iteratively, with code, with sub-calls, until a `FINAL()` is signaled." This is closer to how a human researcher with a long document uses Python in a notebook — chunking, extracting, combining — than how a chat completion API works.

The README phrases it precisely:

> "RLMs replace the canonical `llm.completion(prompt, model)` call with a `rlm.completion(prompt, model)` call. RLMs offload the context as a variable in a REPL environment that the LM can interact with and launch sub-LM calls inside of."

### 2. Architecture: RLM + LMHandler + LocalREPL — Three Cooperating Pieces

The reference implementation has three primary components, all in `rlm/core/`:

> [!info] The three pieces
>
> | Component | File | Role |
> |---|---|---|
> | **RLM** | `rlm/core/rlm.py` | The main iteration loop. Accepts a prompt, runs iterations until `FINAL()` or limits exceeded, returns `RLMChatCompletion`. |
> | **LMHandler** | `rlm/core/lm_handler.py` | A per-completion multi-threaded TCP socket server. Wraps LM clients. Routes requests by (model, depth). Spawns on auto-assigned port; runs in daemon thread; tears down when completion finishes. |
> | **LocalREPL** | `rlm/environments/local_repl.py` | The Python execution environment. Maintains `globals` + `locals` namespaces. Executes model-generated code via `exec(code, combined, combined)`. Provides `llm_query`, `rlm_query`, `context`, `FINAL_VAR`, `SHOW_VARS` to executed code. |

The complete flow per `RLM.completion(prompt)`:

```
1. _spawn_completion_context():
   - Create LM client(s) from backend_kwargs
   - Wrap in LMHandler, .start() the TCP server
   - Create LocalREPL with prompt as `context` variable
2. Iterate (max_iterations):
   a. Send message history → LMHandler → LM API → response
   b. Extract ```repl``` code blocks from response
   c. Execute code in LocalREPL.execute_code()
      - llm_query/rlm_query calls inside code go OUT to LMHandler over TCP
   d. Append stdout/stderr to message history
   e. If FINAL_VAR or FINAL detected → exit loop
3. Tear down handler + environment
4. Return RLMChatCompletion(response, metadata, usage_summary, ...)
```

### 3. The Two Primitives — `llm_query` vs `rlm_query`

These are the functions available to model-generated code inside the REPL.

> [!abstract] llm_query — flat, fast, leaf
>
> ```python
> answer = llm_query("Extract key metrics from: " + context[:5000])
> ```
>
> Always makes a single, direct LM completion. No REPL, no iteration. Fast and lightweight. Used for: summarization, extraction, Q&A on a chunk, anything that doesn't need multi-step reasoning of its own.
>
> Routing: at depth `d`, by default routes to `default_client` unless an `other_backend` is configured AND `d >= 1`, in which case sub-calls go to the cheaper alternate backend.

> [!abstract] rlm_query — recursive, deep, expensive-but-thorough
>
> ```python
> answer = rlm_query("Solve this complex problem with multiple constraints: " + subtask)
> ```
>
> Spawns a CHILD RLM that gets its own LMHandler, its own LocalREPL, and runs its own iteration loop. The child can decompose the subtask further, call its own `llm_query`/`rlm_query`, and signal `FINAL_VAR` when done.
>
> Falls back to `llm_query` when `next_depth >= max_depth` — bounded recursion is enforced structurally, not by prompt instructions.

> [!abstract] Batched variants
>
> `llm_query_batched(prompts: list[str])` — sends all prompts in one batched request to the handler, processed concurrently via `asyncio.gather`.
>
> `rlm_query_batched(prompts: list[str])` — calls `subcall_fn` SEQUENTIALLY for each prompt (each child RLM is a blocking call, since each spawns its own handler+environment).
>
> The asymmetry is structural: batched plain LM calls are concurrent (cheap, server-side parallelism); batched recursive calls are sequential (each child has full machinery; running them concurrently would multiply resource consumption).

### 4. Recursion Semantics — How `max_depth` Bounds the Tree

```
max_depth=3
                                                          
RLM (depth=0)                                             ← root, user calls this
 └─ rlm_query() spawns                                    
    └─ Child RLM (depth=1)                                ← own handler + REPL
       └─ rlm_query() spawns                              
          └─ Child RLM (depth=2)                          ← own handler + REPL
             └─ rlm_query() at depth=2 + max_depth=3:    
                next_depth=3 >= max_depth=3              
                → falls back to plain client.completion() ← LEAF (no REPL, no iteration)
```

> [!warning] Resource isolation — children get REMAINING, not original
>
> ```python
> # In _subcall():
> remaining_timeout = self.max_timeout - elapsed     # NOT self.max_timeout
> remaining_budget  = self.max_budget  - spent       # NOT self.max_budget
> child = RLM(..., max_timeout=remaining_timeout,
>                 max_budget=remaining_budget)
> ```
>
> This prevents a child from consuming all of the parent's resources by accident — a child that recurses into its own sub-calls inherits *what's left* after parent overhead, not the original totals. Without this, a `max_budget=$1.00` parent could spawn 5 children each thinking they have $1.00 to spend.

### 5. Environment Matrix — Local + 5 Cloud Sandboxes

| Environment | Class | Isolation | Setup cost | Latency | When to use |
|---|---|---|---|---|---|
| `local` (default) | `LocalREPL` | None — shares process | None | Lowest (in-process exec) | Trusted prompts, fast iteration, dev/research |
| `docker` | `DockerREPL` | Container (default `python:3.11-slim`) | Docker installed | +seconds (image start) | Reproducible env, untrusted code from trusted prompts |
| `modal` | `ModalREPL` | Cloud sandbox via Modal | Modal account + setup | +seconds (sandbox creation) | Scalable, fully isolated, cloud-native |
| `prime` | `PrimeREPL` | Prime Intellect sandbox (BETA) | API key | High per repo's own warning | Beta — has slow runtime issues |
| `daytona` | `DaytonaREPL` | Daytona sandbox | API key | Provider-dependent | Daytona-aligned environments |
| `e2b` | `E2BREPL` | E2B sandbox | API key | Provider-dependent | E2B-aligned environments |

> [!info] How isolated environments solve the LM-call problem
>
> Cloud sandboxes can't directly connect to the host's `LMHandler` TCP server (different network, isolated process). The HTTP broker pattern bridges this:
>
> ```
> Sandbox-side:  llm_query() → POST localhost:8080/enqueue (blocks)
>                              ↓
>                Flask broker server inside the sandbox queues the request
>                              ↓
> Host-side:     ModalREPL polls {tunnel}/pending every 100ms
>                              ↓
>                Forwards request to LMHandler over socket → LM API → response
>                              ↓
>                POST {tunnel}/respond with the response
>                              ↓
>                Broker unblocks the original /enqueue call
> ```
>
> The broker exposes 4 endpoints: `/enqueue` (POST from sandbox; blocks), `/pending` (GET from host poller), `/respond` (POST from host poller), `/health`. State persistence between code blocks via `dill` to `/tmp/rlm_state.dill`. This pattern is reusable for any new cloud sandbox provider.

### 6. Backend Matrix — 5 Providers + Cost-Aware Routing

| Backend | Required `backend_kwargs` | Optional |
|---|---|---|
| `openai` | `model_name` | `api_key`, `base_url` |
| `anthropic` | `model_name` | `api_key` |
| `portkey` | `model_name`, `api_key` | `base_url` |
| `openrouter` | `model_name` | `api_key` |
| `vllm` | `model_name`, `base_url` | — |

> [!tip] Cost-aware routing via `other_backends` / `other_backend_kwargs`
>
> ```python
> rlm = RLM(
>     backend="anthropic",
>     backend_kwargs={"model_name": "claude-sonnet-4-20250514"},   # ROOT (depth=0)
>
>     other_backends=["openai"],
>     other_backend_kwargs=[{"model_name": "gpt-4o-mini"}],         # SUB-CALLS (depth>=1)
> )
> ```
>
> Inside the REPL, `llm_query(prompt)` at depth>=1 routes automatically to the other backend (`gpt-4o-mini`). At depth=0, it routes to the default backend (Sonnet). The model can override per-call with `llm_query(prompt, model="claude-sonnet-4-20250514")` to force the root model even at sub-call depth.
>
> **The cost intuition**: root-level reasoning needs the strongest model; sub-call extraction/summarization can run on a cheaper-faster model with no measurable quality loss. RLM makes this routing automatic without operator intervention.

> [!example]- Recommended for local sovereignty: vLLM backend
>
> ```python
> rlm = RLM(
>     backend="vllm",
>     backend_kwargs={
>         "model_name": "Qwen/Qwen3.6-27B",  # or any vLLM-served model
>         "base_url": "http://localhost:8000/v1",
>     },
> )
> ```
>
> vLLM exposes an OpenAI-compatible API on a local port; RLM's `vllm` backend points at it. Combined with the wiki's existing recommendation of Qwen3.6-27B as the tier-0 dense reasoning model, this gives a path: local Qwen3.6-27B running on RTX 2080 Ti via llama.cpp/vLLM, RLM wraps it with `max_depth=2` recursive thinking, total system handles long-context tasks normally requiring Opus 4.7. Empirical validation pending.

### 7. Resource Limits — Explicit Exceptions, Not Silent Caps

> [!info] All limits are off by default; the user opts in
>
> | Constructor arg | Triggers | Exception | `partial_answer` available? |
> |---|---|---|---|
> | `max_budget` | Total USD cost exceeded | `BudgetExceededError` | No (caller has spent/budget on the exc) |
> | `max_timeout` | Wall-clock seconds exceeded | `TimeoutExceededError` | YES — last computed answer |
> | `max_tokens` | Total input+output tokens exceeded | `TokenLimitExceededError` | YES |
> | `max_errors` | Consecutive REPL errors exceeded | `ErrorThresholdExceededError` | YES |
> | (KeyboardInterrupt) | User Ctrl+C during completion | `CancellationError` | YES |
>
> The error counter for `max_errors` resets on a successful execution — so transient errors don't accumulate. The exceptions all import from the top-level `rlm` package: `from rlm import RLM, TimeoutExceededError, CancellationError`.

This is "fail fast, fail loud" applied to inference budgeting. The user knows exactly which limit was hit, and can extract the partial work from the exception.

### 8. Trajectory Logging + the Visualizer

> [!info] Two logging modes
>
> ```python
> from rlm.logger import RLMLogger
>
> # Mode 1: in-memory only
> logger = RLMLogger()
> rlm = RLM(..., logger=logger)
> result = rlm.completion(...)
> # result.metadata is a full trajectory dict
>
> # Mode 2: also save JSONL to disk
> logger = RLMLogger(log_dir="./logs")
> # Each completion writes ./logs/rlm_TIMESTAMP_UUID.jsonl
> ```

The JSONL format:
```json
{"type": "metadata", "root_model": "gpt-4o", "max_iterations": 30, ...}
{"type": "iteration", "iteration": 1, "response": "...", "code_blocks": [...]}
{"type": "iteration", "iteration": 2, "response": "...", "final_answer": "..."}
```

The visualizer (Node.js + shadcn/ui, runs `cd visualizer && npm run dev` on `localhost:3001`) loads `.jsonl` files and shows: iteration timeline, code execution results, sub-LM call traces, token usage. For a recursive RLM with sub-calls, this nesting is essential — the metadata tree mirrors the call tree.

### 9. Persistence — Multi-Turn Mode

```python
with RLM(..., persistent=True) as rlm:
    result1 = rlm.completion("First context")
    # context_0 set; locals accumulated
    result2 = rlm.completion("Second context")
    # context_1 set; context_0 still available; locals from result1 still available
    # Model can reference context_0 + context_1 + history_0 + history_1
```

> [!info] Versioned contexts in persistent mode
>
> | Variable | What it is |
> |---|---|
> | `context` | Alias for `context_0` (the FIRST context) |
> | `context_0`, `context_1`, ... | Each completion's prompt becomes the next context_N |
> | `history_0`, `history_1`, ... | Conversation history from each completion |
>
> Reserved name handling: even in persistent mode, after every `exec()` LocalREPL restores `llm_query`, `rlm_query`, `context`, `history`, `FINAL_VAR`, `SHOW_VARS` — so model code that accidentally writes `context = None` doesn't break the next iteration.

### 10. Compaction — Auto-Summarize When Context Fills

```python
rlm = RLM(
    ...,
    compaction=True,
    compaction_threshold_pct=0.85,   # default; trigger at 85% of model's context window
)
```

When token usage in the conversation history exceeds the threshold, RLM auto-summarizes earlier parts of the conversation. The full history (including summaries) remains available in the REPL as the `history` variable — so model code can inspect what got compacted.

> [!warning] Compaction interacts with persistent mode
>
> If `persistent=True` AND `compaction=True`, each completion can compact independently. But because `context_0`, `context_1`, ... persist across completions, the total state grows. Heavy multi-turn workflows should set explicit `max_tokens` budgets per completion to avoid runaway state.

### 11. Custom Tools — Domain-Specific Functions in the REPL

```python
def fetch_weather(city: str) -> str:
    return weather_api.get(city)

def calc_shipping(weight: float, distance: float) -> float:
    return weight * 0.5 + distance * 0.1

rlm = RLM(
    ...,
    custom_tools={
        # Plain form
        "fetch_weather": fetch_weather,
        "API_KEY": "sk-...",  # non-callable → variable

        # Dict-with-description form
        "calc_shipping": {
            "tool": calc_shipping,
            "description": "Calculate shipping cost given weight (kg) and distance (km)",
        },
    },
)
```

The descriptions auto-inject into the system prompt:
```
6. Custom tools and data available in the REPL:
- `fetch_weather`: Fetch current weather for a city
- `calc_shipping`: Calculate shipping cost given weight (kg) and distance (km)
- `API_KEY`: API key for the weather service
```

Reserved names (`llm_query`, `rlm_query`, `context`, `history`, `FINAL_VAR`, `SHOW_VARS`, batched variants) cannot be overridden as custom tools. `custom_sub_tools={}` disables custom tools for child RLMs; `custom_sub_tools=None` (default) means children inherit parent's `custom_tools`; passing a different dict gives children a different tool set.

For isolated environments (Modal, Daytona), custom tools must be serializable: code-string form for functions, JSON-compatible values for data.

### 12. Convergence with Anthropic's Effective Harnesses Pattern (Nov 2025)

The wiki's existing source [Anthropic — Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) (Nov 2025) found:

> "Compaction alone is NOT sufficient for tasks spanning multiple context windows. Even Opus 4.5 + Claude Agent SDK fails without explicit harness artifacts."

Anthropic's solution was explicit *files* the agent operates on: `init.sh`, `feature_list.json`, `claude-progress.txt`, `git history`. The structural lesson there: "JSON over Markdown for `feature_list.json` because the model is less likely to inappropriately change or overwrite JSON files."

RLMs encode the SAME insight at a different abstraction level:

| Anthropic (Nov 2025) | RLMs (Dec 2025) |
|---|---|
| Context split across explicit files agent reads | Context split across `context_0`, `context_1`, ... variables in a REPL |
| Model writes/reads files via tool calls | Model writes/reads variables via REPL exec |
| `feature_list.json` chosen for format-as-enforcement | Python variables in `LocalREPL.locals` chosen for namespace-as-enforcement |
| Linear file-based memory | Tree-shaped recursive memory via `rlm_query` |
| Single-process agent + filesystem | Process tree of RLM instances, each with own REPL |

Both papers/projects arrive at: **the model needs to OPERATE ON its context, not just RECEIVE it.** RLMs go further by formalizing this into a recursive paradigm where the operating-on can itself be done by sub-models with their own operating environments.

### 13. Connection to Wiki Principles — Where RLM Fits

| Wiki principle / model | RLM connection |
|---|---|
| **P2 — Structured Context Governs Behavior More Than Content** | RLM is structural-context taken to the limit: the prompt is no longer a string of natural language, it's a Python variable in a REPL. The "structure" governing the model's behavior IS the REPL grammar (variables, function calls, control flow). |
| **[Model — Context Engineering](../../spine/models/depth/model-context-engineering.md)** § OS analogy | The model's "context = RAM" mapping extends: with RLM, RAM has a virtual-memory layer. `context_0` lives in "fast RAM" (current iteration), `context_1` lives in "slower RAM" (different iteration), recursive children get their own RAM. The harness (LMHandler+REPL) is the OS managing this. |
| **[Model — Skills, Commands, and Hooks](../../spine/models/agent-config/model-skills-commands-hooks.md)** § 4-level cost gradient | RLM is a NEW point on this gradient: not skill (instruction-only), not command (one-shot trigger), not hook (lifecycle enforcement) — it's a *runtime substrate* that wraps the LM call itself, structurally adding code execution + recursion. The 4-level table extends to 5 if RLM-as-runtime is accepted as its own layer. |
| **[Model — Claude Code](../../spine/models/agent-config/model-claude-code.md)** § Harness Engineering | RLM is harness-engineering at the inference-call boundary, complementary to Claude Code's harness-engineering at the session/agent-loop boundary. They compose: Claude Code's session loop could use RLM as its `llm.completion` substrate. |
| **Anthropic Nov 2025 long-running-agents pattern** | Direct lineage as documented above. |
| **The 7 Levels of Claude Code & RAG framework** (existing wiki source) | RLM occupies a level between 4 (Obsidian / linked-knowledge graph) and 6 (Graph RAG) — it's structural context-traversal but at the inference-call level, not at the storage level. Possibly Level 4.5 or its own dimension. |

### 14. Mission Implications — Tier-0 Local + RLM as Cost Multiplier

The operator's [post-Anthropic mission](../../spine/references/2026-consumer-hardware-ai-stack.md) targets Stage 5 (80% Claude reduction) by 2026-04-27 (today). The wiki's existing recommendation: smart cloud routing alone drops $540 → $100 CAD/mo (per [AICP 2026-04-24 handoff](../../../../devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md)). Tier-0 hardware optional.

> [!success] How RLM extends the cost story
>
> | Capability | Without RLM | With RLM |
> |---|---|---|
> | Long-context Q&A (e.g., 200K-token doc) | Need Opus 4.7 (200K window) — $5/$25 per 1M | Use Qwen3.6-27B local (32K window) + RLM `max_depth=2` recursion + chunking — $0 (electricity only) |
> | Cross-document synthesis | Need Sonnet (200K) | Use small local model + `rlm_query_batched` over chunks |
> | Agentic coding with deep reasoning | Need Opus extended thinking | Local model + RLM iteration + custom tools (file ops, search) |
>
> The structural argument: **the bottleneck isn't single-shot reasoning quality, it's working-memory size.** RLM gives small models virtual working memory through the REPL + recursion. If validated empirically on operator's RTX 2080 Ti hardware (Action 18 in the [2026 consumer hardware spine reference](../../spine/references/2026-consumer-hardware-ai-stack.md) addendum), this is a force-multiplier on the existing local-AI strategy.
>
> **Empirical validation pending** — this synthesis ranks the connection as `seed` maturity / `confidence: high` *for the description of what RLM IS* but the cost/quality claim above is theoretical until benchmarked. The arXiv paper has experimental results we have not yet ingested (the paper PDF was not in the README dump; would need a separate ingestion).

### 15. CONTRIBUTING.md TODO List — Roadmap Signals

The repo's CONTRIBUTING.md is unusually frank about what's done vs aspirational. Three priority tiers:

> [!info] Urgent TODOs (acknowledged-needed-now)
> - Additional sandboxes (Prime Sandboxes are WIP)
> - **Persistent REPL across the client.** Currently REPL is persistent only across a single completion call — for multi-turn settings a `flag` would handle persistence with `context_{x}` versioning. Author hasn't decided the design.
> - Finding interesting benchmarks/examples
> - Improve documentation
>
> Low-hanging fruit: better unit tests (Mock LM class inspired by `verifiers`); comprehensive bug finding.

> [!info] Would-be-nice TODOs
> - Multi-modal / arbitrary input support (currently `str` / standard LM dict messages only; should support picklable inputs)
> - File-system based environments (REPLs + bash + filesystem)
> - Improved UI for visualization
> - Better data storage for training/statistics

> [!info] "If you can tackle these, thanks LOL" TODOs
> - **Pipelining / asynchrony of LM calls.** "This could be a paper of its own IMO" — author flags this as a major research project, not a feature.
> - Efficient prefix caching (requires restructuring core logic; "could also be a paper")
> - **Training models to work as RLMs.** References `verifiers` library's `rlm_env` — implies RL training of RLM-aware models is a research direction. This is potentially the biggest follow-up: models trained to be GOOD at the RLM paradigm, not just compatible with it.

The roadmap is honest about what's prototype vs product. Anyone adopting RLM as production infrastructure should expect to contribute back or fork.

## Open Questions

> [!question] How does RLM compare to DSPy and ColBERT (Khattab's prior work) on long-context retrieval?
> Khattab (co-author) is the DSPy and ColBERT author. DSPy decomposes LM programs into modules with examples; ColBERT is dense retrieval. RLM is a third paradigm: programmatic decomposition at inference time without prior compilation. The arXiv paper likely compares against DSPy+ColBERT but we haven't ingested the paper PDF. (Requires: ingesting [arXiv 2512.24601](https://arxiv.org/abs/2512.24601) directly.)

> [!question] What is the empirical token-cost / quality tradeoff vs single-shot Opus 4.7?
> The structural claim "small model + RLM ≈ large model + big context" needs benchmarking. Specific benchmarks to track: long-context Q&A (NIAH variants, RULER), agentic coding (SWE-bench), document summarization. (Requires: reading the arXiv paper's experimental section + running benchmarks on operator's hardware.)

> [!question] Does the in-process `exec()` security model hold up for production?
> Soft sandbox (removed `eval`/`exec`/`compile`/`input` builtins) is documented as NOT a security boundary. Production deployment with adversarial prompts must use docker/modal/prime. But the broker pattern adds ~100ms/poll latency. What's the empirical p50/p99 latency penalty vs `local`? (Requires: benchmark across environments.)

> [!question] How does compaction interact with recursive sub-calls?
> The README says compaction summarizes the conversation history when token usage exceeds 85% of the model's context window. But child RLMs have their own context windows + their own potential compaction triggers. If a parent compacts, do the child trajectory metadata structures still resolve correctly to the original context? (Requires: code reading of `rlm/core/rlm.py`'s compaction handler + child metadata propagation.)

> [!question] Could RLM serve as the substrate for AICP's local backend?
> AICP currently routes between `local` (LocalAI) / `k2_6_local` (llama.cpp) / `k2_6_openrouter` / `claude` / `ollama_cloud`. Adding an `rlm_local` backend that wraps `local` with RLM's recursive paradigm could give long-context capability to local-tier work without changing the underlying model. (Requires: AICP-side feasibility assessment per the AICP repo's tier_map architecture.)

> [!question] What's the relationship to "verifiers" library and Prime Intellect?
> CONTRIBUTING.md references `verifiers` (`PrimeIntellect-ai/verifiers` `rlm_env`) as a starting point for training models to work as RLMs. The repo also natively supports Prime Intellect's sandboxes. Is RLM aligned with Prime Intellect's broader RL-for-agents stack? (Requires: ingestion of the verifiers repo + prime-intellect docs.)

> [!question] Does the wiki's own ingestion pipeline benefit from RLM?
> The wiki's `tools/pipeline.py fetch` ingests URLs into raw/, then synthesizes into wiki pages. The synthesis step (which produces THIS page) currently uses a single LM call. If the raw is 4000+ lines, this hits context limits or quality degrades. Wrapping the synthesis call with RLM would let the synthesizer programmatically chunk the raw, summarize sections, then synthesize a top-level page. (Requires: design discussion + small experiment on a real raw.)

## Applicability

> [!info] When RLM applies
>
> - **Long-context tasks** (>50K tokens) where iterative chunked processing is meaningful — document Q&A, codebase analysis, multi-source synthesis
> - **Agentic coding tasks** that benefit from deep reasoning per subtask — RLM gives the model a way to "think harder" on hard subtasks via `rlm_query`, and "think cheaply" on easy subtasks via `llm_query`
> - **Cost-constrained deployments** where smaller-cheaper-faster models can substitute for larger ones IF given a recursive substrate
> - **Research on long-context strategies** — RLM is itself a research artifact, ideal for benchmarking the recursive-paradigm hypothesis
> - **Sovereignty-tier local AI** combined with vLLM backend — local Qwen3.6-27B + RLM may match cloud Opus on certain task classes

> [!warning] When RLM does NOT apply
>
> - **Latency-sensitive production** — the iteration loop adds latency; even a 5-iteration recursion at 5s per iteration is 25s minimum
> - **Single-shot tasks** (chat, simple Q&A, classification) — RLM overhead is pure cost, no benefit
> - **Tasks where the LM doesn't need to iterate** — e.g., a 200-token classification — RLM adds machinery without value
> - **Adversarial-input deployments without isolated environments** — `local` mode is NOT a security boundary; would need docker/modal/prime, which adds setup cost
> - **Production agent loops requiring guarantees beyond best-effort** — RLM is research-grade per CONTRIBUTING.md ("functional for most use cases" but "isn't super fast yet")

## How to Apply (within this ecosystem)

> [!tip] Concrete adoption paths
>
> 1. **Local experiment** — `pip install rlms` in a scratch venv; run `rlm = RLM(backend="openai", backend_kwargs={"model_name": "gpt-5-nano"})`; pass a long document; observe trajectory via the visualizer. Cost: trivial.
> 2. **vLLM + local model substitution** — point RLM's `vllm` backend at a local llama.cpp/vLLM server running Qwen3.6-27B; run RLM with `max_depth=2`; benchmark a long-context task vs Opus 4.7 single-shot. This is Action 18 from the spine reference, extended.
> 3. **Wiki-pipeline integration prototype** — wrap `tools/pipeline.py fetch+synth` step with RLM; let the synthesizer programmatically chunk-and-summarize long raws. Validate that synthesis quality is at least as good as the current single-LM-call approach.
> 4. **AICP backend prototype** — add `aicp/backends/rlm_local.py` that wraps the existing `local` backend with RLM (just like the existing pattern wraps `llama.cpp`). Test if AICP's routing layer can use RLM-augmented local for long-context work.

## Relationships

- BUILDS ON: [[model-context-engineering|Model — Context Engineering]] (RLM is the direct extension of "context as RAM" → "context as variable in REPL")
- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Behavior]] (RLM moves from "structured natural language" to "structured Python variables")
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] (RLM is a new runtime layer not in the current 4-level taxonomy)
- RELATES TO: [[model-claude-code|Model — Claude Code]] (Claude Code's session-loop harness could use RLM as its inference substrate)
- RELATES TO: [[model-llm-wiki|Model — LLM Wiki]] (this wiki's synthesis pipeline could integrate RLM for long-raw ingestion)
- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]] (RLM + vLLM + local Qwen3.6-27B is a force-multiplier for the local-AI cost story)
- RELATES TO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (RLM extends the tier-0 reasoning-tier story; complementary to Qwen3.6-27B candidacy)
- COMPARES TO: [[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic — Effective Harnesses for Long-Running Agents]] (parallel insight at different abstraction level — files+JSON vs REPL+variables)
- COMPARES TO: [[src-claude-agent-sdk-and-managed-agents|Synthesis — Claude Agent SDK and Managed Agents]] (both are inference-time SDKs; SDK provides session machinery, RLM provides REPL substrate)
- ENABLED BY: [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]] (RLM's REPL-with-custom-tools is a third pattern next to MCP and CLI; loads tools per-completion not per-session)
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (adds a new dimension: inference paradigm — single-shot vs RLM-recursive)
- FEEDS INTO: [[ai-model-provider-harness-decision-matrix-2026|AI Model Provider Harness Decision Matrix]] (RLM is a new harness option alongside Claude Code, OpenCode, Codex)

## Backlinks

[[model-context-engineering|Model — Context Engineering]]
[[Principle 2 — Structured Context Governs Behavior]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-claude-code|Model — Claude Code]]
[[model-llm-wiki|Model — LLM Wiki]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[2026 Consumer Hardware AI Stack]]
[[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic — Effective Harnesses for Long-Running Agents]]
[[src-claude-agent-sdk-and-managed-agents|Synthesis — Claude Agent SDK and Managed Agents]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[AI Model Provider Harness Decision Matrix]]

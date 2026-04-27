---
title: "Synthesis — Prime Intellect Verifiers: Environments for LLM RL (with RLMEnv for Recursive Language Models)"
aliases:
  - "Prime Intellect Verifiers"
  - "Verifiers Library"
  - "RLMEnv"
  - "Synthesis — Verifiers"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: verifiers-repo
    type: documentation
    url: https://github.com/PrimeIntellect-ai/verifiers
    file: raw/articles/primeintellect-aiverifiers.md
    title: "PrimeIntellect-ai/verifiers — Environments for LLM Reinforcement Learning"
    ingested: 2026-04-27
  - id: verifiers-docs
    type: documentation
    url: https://docs.primeintellect.ai/verifiers
    title: "Verifiers official documentation site"
  - id: environments-hub
    type: documentation
    url: https://app.primeintellect.ai/dashboard/environments?ex_sort=most_stars
    title: "Environments Hub — community-published RL environments"
  - id: original-author-citation
    type: documentation
    url: https://github.com/willccbb
    description: "Will Brown (@willccbb) — original creator of verifiers; cited via @misc{brown_verifiers_2025}"
  - id: rlm-paper-connection
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md
    description: "RLM paper deep-dive — verifiers is the runtime substrate for RLMEnv used in the RLM-Qwen3-8B training recipe"
tags: [verifiers, prime-intellect, llm-rl, environments, rlm-env, recursive-language-models, training-framework, rubrics, datasets, harnesses, prime-cli, environments-hub, will-brown, prime-rl-integration, openenv, browser-env, mcp-env, tool-env, stateful-tool-env, mit-csail-connection, mission-2026-04-27, sovereignty-tier, anti-vendor-lock-in, tools-integration]
---

# Synthesis — Prime Intellect Verifiers: Environments for LLM RL

## Summary

Verifiers is Prime Intellect's open-source library for creating environments to train and evaluate LLMs — the runtime substrate that holds together a *dataset*, a *harness* (tools, sandboxes, context management), and a *rubric* (reward function) into a single Python module that can be used for RL training, evaluation, synthetic data generation, or experimenting with agent harnesses. Originally created by **Will Brown ([@willccbb](https://github.com/willccbb))** and now stewarded by Prime Intellect, the library is tightly integrated with **[prime-rl](https://github.com/PrimeIntellect-ai/prime-rl)** (Prime Intellect's training framework) and the **Environments Hub** (the community-publishing platform). The v0.1.12 release (2026-04-17) explicitly added **upstreamed opencode and RLM harnesses/tasksets, major `RLMEnv` improvements (context dropping, prompt builder, hardened transport)** — making this the direct integration point for the RLM paper's training infrastructure. The library exposes a Python contract: each environment is a self-contained module with a `load_environment(...) -> vf.Environment` factory; the prime CLI (`prime env init` / `prime env install` / `prime eval run` / `prime env push`) orchestrates the lifecycle. Environment class taxonomy: **`SingleTurnEnv`** (one input → one response), **`MultiTurnEnv`** (multi-turn dialogue), **`ToolEnv`** / **`MCPEnv`** (stateless tools), **`StatefulToolEnv`** (per-rollout state — sandbox/session/db handles), **`BrowserEnv`** (browser automation via Stagehand CUA primitives, Modal-deployable), **`OpenEnv`** (the cross-framework OpenEnv standard integration), plus the new **`RLMEnv`** for recursive language model training. Mission-relevant for the post-Anthropic AI stack: this is the open-source training substrate that lets anyone reproduce the RLM-Qwen3-8B post-training recipe + author new agentic environments without vendor lock-in.

## Reference Card

> [!info] Verifiers reference card
>
> | Field | Value |
> |---|---|
> | **Type** | RL environment library + framework + CLI plugin |
> | **License** | (per repo — confirm; project ships LICENSE file) |
> | **Original author** | Will Brown ([@willccbb](https://github.com/willccbb)) |
> | **Steward** | Prime Intellect |
> | **Documentation** | docs.primeintellect.ai/verifiers |
> | **Environments Hub** | app.primeintellect.ai/dashboard/environments |
> | **Pip / install** | `uv add verifiers` (preferred) — uses `uv` package manager |
> | **CLI dependency** | `prime` CLI (`uv tool install prime` + `prime login`) |
> | **Latest release at ingest** | **v0.1.12 (2026-04-17)** — upstreamed opencode + RLM harnesses, major RLMEnv improvements |
> | **Recent releases** | v0.1.11 (2026-03-12, RLMEnv reliability) · v0.1.10 (2026-02-10, OpenEnv + BrowserEnv) · v0.1.9 (2026-01-08, monitor rubrics) · v0.1.8 (2025-11-19, trajectory-based tracking) · v0.1.7 (2025-11-07, prime-rl quickstart, `vf.RLTrainer`) |
> | **Environment classes** | SingleTurnEnv · MultiTurnEnv · ToolEnv · MCPEnv · StatefulToolEnv · BrowserEnv · OpenEnv · **RLMEnv** |
> | **Workspace setup** | `prime lab setup` creates configs/, .prime/skills/, environments/, AGENTS.md, CLAUDE.md |
> | **Confidence label** | high — read README + AGENTS.md + CLAUDE.md + multiple asset files (compilation_design.md, end_user_best_practices.md, repo_development_best_practices.md) + start of development.md as Layer 1 sources; remaining ~3900 lines of repo dump (more docs, environment templates, tests) not exhaustively read but content is largely implementation detail beyond what this synthesis needs. |
> | **Mission relevance** | High — the open-source substrate for the RLM paper's training infrastructure; directly enables the wiki's anti-vendor-lock-in mission |

## Key Insights

1. **Environments are the primary abstraction**. Each environment bundles three things: dataset (task inputs), harness (tools/sandboxes/context-management), rubric (reward function). This is the same `dataset + harness + rubric` taxonomy the wiki has been tracking — verifiers operationalizes it as a Python contract: `load_environment(...) -> vf.Environment`.

2. **`RLMEnv` is the direct RLM-paper connection**. Per v0.1.12 release notes: *"upstreamed opencode and RLM harnesses/tasksets, major `RLMEnv` improvements (context dropping, prompt builder, hardened transport)"*. RLMEnv lets a verifier-trained LM operate as a Recursive Language Model — chained with the [RLM paper's training recipe](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md), this is the open-source path for anyone to fine-tune their own RLM-native model.

3. **Tightly integrated with prime-rl**. Verifiers v0.1.7 (2025-11-07) explicitly added *"improved quickstart configuration for training with prime-rl"* and a new included `vf.RLTrainer` (replacing `vf.GRPOTrainer`). The two libraries are designed to compose — verifiers provides the environment, prime-rl provides the trainer.

4. **The CLI lifecycle is workflow-shaped, not flag-shaped**. `prime env init my-env` creates a template; `prime env install my-env` registers it locally; `prime eval run my-env -m openai/gpt-5-nano` runs evaluation; `prime env push --path ./environments/my_env` publishes to the Environments Hub. Each step is a distinct verb in the workflow — no ambiguity about lifecycle stage.

5. **Skills + AGENTS.md as default for AI coding**. `prime lab setup` ships a `.prime/skills/` directory with **bundled workflow skills for create / browse / review / eval / GEPA / train / brainstorm** — the project ships an opinionated agent-skills layer. The skills are symlinked to `.claude/skills/` per AGENTS.md guidance, making this directly usable in Claude Code workspaces.

6. **AGENTS.md compilation system is itself notable**. The repo has `assets/agents/` with separate sources for `common_best_practices.md`, `repo_development_best_practices.md`, `end_user_best_practices.md`, and `compilation_design.md` — generated outputs are `AGENTS.md` (root), `CLAUDE.md` (pointer), `assets/lab/AGENTS.md` (end-user), and `environments/AGENTS.md` (env-dev). This is the wiki's [Markdown-as-IaC](../../spine/models/agent-config/model-markdown-as-iac.md) pattern at production scale: source-of-truth content compiled to multiple audience-specific outputs.

7. **Environment class taxonomy spans the full agentic-task surface**:
   - **`SingleTurnEnv`** — basic Q→A
   - **`MultiTurnEnv`** — dialogue, persistent context across turns
   - **`ToolEnv`** — stateless tools (calculator, search)
   - **`MCPEnv`** — Model Context Protocol tool integration
   - **`StatefulToolEnv`** — per-rollout state (sandbox/session/db handles)
   - **`BrowserEnv`** — browser automation via Stagehand Computer-Use Agent (CUA) primitives, optionally Modal-sandboxed
   - **`OpenEnv`** — integration with the cross-framework OpenEnv standard
   - **`RLMEnv`** — Recursive Language Model environment (the RLM-paper integration)

8. **`vf.ensure_keys(...)` enforces API-key validation early**. AGENTS.md guidance: "If external API keys are required, validate them in `load_environment()` with `vf.ensure_keys(...)` so failures are explicit and early." This is the wiki's [P4 (Declarations Aspirational Until Verified)](../../lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md) pattern at the SDK level — declared key requirements have a verification gate.

9. **Trajectory-based tracking enables token-in-token-out training**. v0.1.8 (2025-11-19) major refactor: rollout system uses trajectory-based tracking for token-in-token-out training across turns, with support for **truncated or branching rollouts**. This is critical for RL training of multi-turn agents where the trainer needs the full action sequence including its branches.

10. **Monitor rubrics for automatic metric collection**. v0.1.9 (2026-01-08) added monitor rubrics — automatic metric collection during environment execution. This is the observability primitive for RL training: rubrics aren't just reward functions, they're also instrumented for monitoring.

11. **OpenEnv + BrowserEnv integrations expand the surface**. v0.1.10 (2026-02-10) added OpenEnv (cross-framework standard) and BrowserEnv (browser automation). The BrowserEnv pattern uses a Fastify CUA Primitives Server inside a Modal sandbox — exposing Stagehand browser actions as REST endpoints. The architecture: `External Agent → Fastify API → BrowserSessionManager → Stagehand Page → Browser`. Auto-deploys to Modal sandbox when `BrowserEnv(mode="cua", use_sandbox=True)`.

12. **The repo's contributor guidance is explicitly anti-parallel-paths**. AGENTS.md repo-development section: *"Prefer a single clear path over maintaining parallel approaches by default; if two options exist, preserve both only when there is an explicit long-term reason. Aggressively deprecate/remove inferior paths when they are not part of an intended multi-option contract."* This matches the wiki's [Hardcoded Instances Fail principle](../../lessons/) — converge on one path, document why if branching.

## Deep Analysis

### What an Environment Looks Like

The minimal environment pattern from the README:

```python
# my_env.py
import verifiers as vf

def load_environment(dataset_name: str = 'gsm8k') -> vf.Environment:
    dataset = vf.load_example_dataset(dataset_name)  # 'question' field
    
    async def correct_answer(completion, answer) -> float:
        completion_ans = completion[-1]['content']
        return 1.0 if completion_ans == answer else 0.0
    
    rubric = Rubric(funcs=[correct_answer])
    env = vf.SingleTurnEnv(dataset=dataset, rubric=rubric)
    return env
```

Three lines of substance: load dataset, define reward function, instantiate environment with both. The `load_environment` factory pattern enables `prime env install <name>` / `prime eval run <name>` lifecycle commands — the CLI looks up `load_environment` per the convention.

### CLI Workflow Lifecycle

| Verb | What it does | Where state goes |
|---|---|---|
| `prime lab setup` | One-time workspace bootstrap (configs, skills, AGENTS.md) | Creates `.prime/`, `configs/`, `environments/` |
| `prime env init <name>` | Scaffold new environment template | `./environments/<name>/` |
| `prime env install <name>` | Install env into project (from local or Hub) | Registers env for `prime eval run` |
| `prime eval run <name> -m <model>` | Run evaluation (saves results automatically) | Results in private Evaluations tab + `prime eval tui` |
| `prime env push --path <path>` | Publish to Environments Hub | Public on app.primeintellect.ai |
| `prime eval tui` | Browse evaluation results in terminal UI | Reads from Evaluations tab |

> [!warning] Don't add `--skip-upload` flags
>
> AGENTS.md is explicit: *"Treat `prime eval run` as the canonical eval path: it saves results automatically, and agents should not add opt-out flags such as `--skip-upload` unless the user explicitly requests that deviation so runs stay visible in the private Evaluations tab and in `prime eval tui`."*
>
> This is structural enforcement of the observability principle — every eval run should be visible by default. Suppressing observability requires explicit operator authorization.

### `RLMEnv` — The RLM-Paper Connection

Per v0.1.11 (2026-03-12) and v0.1.12 (2026-04-17) release notes, `RLMEnv` has been a major focus:

| Version | RLMEnv-related changes |
|---|---|
| v0.1.11 (2026-03-12) | "major RLMEnv and env server reliability improvements" |
| v0.1.12 (2026-04-17) | "upstreamed opencode and RLM harnesses/tasksets, major RLMEnv improvements (**context dropping, prompt builder, hardened transport**)" |

What "context dropping" / "prompt builder" / "hardened transport" suggest:
- **Context dropping**: when the recursive REPL context grows too large, drop older context strategically (parallels the RLM paper's compaction discussion + Anthropic's Nov 2025 effective-harnesses pattern)
- **Prompt builder**: structured construction of the RLM root system prompt (the same artifact the [RLM paper deep-dive](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) Appendix C documents in 3 variants)
- **Hardened transport**: improved socket / HTTP-broker communication between root LM, sub-LM calls, and REPL execution (parallels the [RLM implementation](src-rlm-recursive-language-models-mit-oasys.md) architecture)

The integration pattern: a researcher wanting to train their own RLM-native model would (1) define an RLMEnv with the long-context tasks they care about, (2) configure prime-rl to fine-tune on RLM-trajectory SFT samples produced by a teacher model running this RLMEnv, (3) evaluate the post-trained model in the same RLMEnv. This is the path the RLM paper followed — open-sourced.

### Skills + AGENTS.md System

The repo demonstrates the [skills/commands/hooks model](../../spine/models/agent-config/model-skills-commands-hooks.md) at production scale:

> [!info] What `prime lab setup` ships
>
> | Path | Purpose |
> |---|---|
> | `.prime/skills/` | Bundled workflow skills: create, browse, review, eval, GEPA, train, brainstorm |
> | `.claude/skills/` | Symlinks to `.prime/skills/` (Claude Code recognizes this) |
> | `configs/endpoints.toml` | OpenAI-compatible endpoint config (alias-able) |
> | `configs/rl/` | Example Hosted Training configs |
> | `configs/eval/` | Example multi-environment eval configs |
> | `configs/gepa/` | Example prompt optimization configs |
> | `environments/AGENTS.md` | Documentation for environment-development AI agents |
> | `AGENTS.md` | Top-level documentation for AI coding agents |
> | `CLAUDE.md` | Claude-specific pointer to AGENTS.md |

The compiled-AGENTS.md system (sources in `assets/agents/`, generated outputs to multiple targets) is itself a worked example of structured-context-as-IaC — the wiki's existing [Markdown-as-IaC model](../../spine/models/agent-config/model-markdown-as-iac.md) at scale.

### BrowserEnv — Modal Sandbox + CUA Primitives

The BrowserEnv pattern (v0.1.10, 2026-02-10) deserves its own callout because of the architecture:

```
External Agent → Fastify API → BrowserSessionManager → Stagehand Page → Browser
                       ↑
                  (auto-deployed to Modal sandbox when use_sandbox=True)
```

The Fastify server inside the Modal sandbox exposes 5 categories of REST endpoints for browser actions:
- **Mouse**: click / double_click / tripleClick / drag / move
- **Keyboard**: type / keypress
- **Navigation**: goto / back / forward / scroll
- **Utility**: wait / screenshot
- **Session**: create / get-state / close / list

Auto-deployed via `setup.sh` upload to a Modal sandbox container. This is exactly the [HTTP broker pattern](../../sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md) the RLM SDK uses for isolated environments — same architectural shape, different domain.

### Comparison to Other Environment Frameworks

| Framework | Provided by | Key differentiator from verifiers |
|---|---|---|
| **OpenEnv** | Cross-framework standard | Verifiers integrates as a backend (BrowserEnv, OpenEnv class) |
| **TextWorld** (Microsoft) | Microsoft Research | Text-game focus; no LLM RL primitives |
| **Llama Agentic System** | Meta | Tied to Llama-Stack; less LLM-agnostic |
| **DeepSeek-LLM-Agent** | DeepSeek | Research-focused; no Hub/CLI |
| **AutoGen** (Microsoft) | Microsoft | Agentic conversation focus, not RL training |
| **CrewAI / LangChain** | Various | Workflow orchestration, not RL training environments |

Verifiers' distinctive position: **the only framework specifically designed as an RL-environment library for LLM training, with a Hub for community publishing, a CLI for the lifecycle, and tight integration with both a training framework (prime-rl) and a hosted training platform (Prime Intellect Hosted Training).**

### Alignment with the Wiki's Mission

| Wiki principle / model | Verifiers' alignment |
|---|---|
| **[Anti-vendor-lock-in](../../../.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_mission_framing.md)** | Open-source library, public Hub, OpenAI-compatible endpoint config — works with any provider |
| **[Markdown-as-IaC](../../spine/models/agent-config/model-markdown-as-iac.md)** | AGENTS.md compilation system, skills layer, endpoint config in TOML |
| **[Skills/Commands/Hooks](../../spine/models/agent-config/model-skills-commands-hooks.md)** | `.prime/skills/` shipped by default, `prime` CLI commands as workflow triggers |
| **[Principle 4 (Declarations Aspirational Until Verified)](../../lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md)** | `vf.ensure_keys(...)` validates declared API requirements early |
| **[2026 Consumer Hardware AI Stack](../../spine/references/2026-consumer-hardware-ai-stack.md)** | Provides RL-training capability on local hardware (with prime-rl backend); enables fine-tuning own models |
| **[RLM paper deep-dive](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md)** | RLMEnv is the productionized version of the paper's experimental setup — anyone can replicate the post-training recipe |

## Open Questions

> [!question] What's the actual `RLMEnv` API surface?
> v0.1.12 release notes name "context dropping, prompt builder, hardened transport" but the actual class signature isn't in the README. (Requires: reading `verifiers/envs/rlm_env.py` or the docs.primeintellect.ai/verifiers RLMEnv reference.)

> [!question] Are there published RLMEnv tasksets on the Environments Hub?
> v0.1.12 mentions "upstreamed opencode and RLM harnesses/tasksets" — is the actual taskset (the LongBenchPro fine-tuning data the RLM paper used) available as a verifiers environment? (Requires: browsing the Environments Hub.)

> [!question] How does the GEPA workflow integrate?
> AGENTS.md mentions `configs/gepa/` and the bundled skills include "GEPA". GEPA = Generalized Effective Prompt Adaptation? Or a different acronym? Documentation mentions it as a prompt optimization workflow. (Requires: reading docs/gepa.md or equivalent.)

> [!question] Can verifiers environments be used for evaluation without RL training?
> Yes per the README ("evaluating capabilities, generating synthetic data") but the relative weight of the eval-only vs train use case isn't clear. For the wiki's mission (post-Anthropic stack with possible eval-driven feedback loops), eval-only adoption may be the higher-value first step. (Requires: case-study analysis.)

> [!question] What's the OpenCode integration?
> v0.1.10 mentions "opencode harbor improvements"; v0.1.12 says "upstreamed opencode... harnesses/tasksets". OpenCode is the wiki's existing tracked harness alternative to Claude Code. Does verifiers have OpenCode-specific environments / task definitions? (Requires: looking at `environments/opencode_*` if present.)

> [!question] Is there a Goldilocks-class default environment for tier-0 hardware?
> The README's example uses `gsm8k` (small math benchmark, easy to run on consumer GPU). Is there a recommended starter environment specifically for testing tier-0 hardware (RTX 2080 Ti, 16-24GB VRAM)? (Requires: experiment.)

## How to Apply

> [!tip] Concrete adoption paths for the wiki's mission
>
> 1. **Local install + run an existing environment**: `prime lab setup` in a fresh dir, `prime env install primeintellect/math-python`, `prime eval run primeintellect/math-python -m openai/gpt-5-nano`. Validates the SDK works on operator's setup.
> 2. **Run RLMEnv on a small task**: install verifiers, find or define an RLMEnv-compatible task (long-context Q&A from existing wiki content), evaluate with GPT-5-mini as both root and sub-LM. Validates the RLM paradigm + verifiers integration on operator hardware.
> 3. **Train RLM-Qwen3-8B from scratch**: combine verifiers (RLMEnv definition) + prime-rl (training framework) + Qwen3-8B base + LongBenchPro tasks. Reproduce the RLM paper's recipe locally or on Prime Intellect's compute platform. Estimated: 48 H100 hours per the paper.
> 4. **Define a domain-specific environment**: use `prime env init my-env` to scaffold; implement `load_environment()` for your domain (e.g., wiki-page-quality scoring, code-review tasks); `prime eval run` to test; `prime env push` to publish.
> 5. **Use eval-only for AICP backend testing**: define environments that evaluate AICP's various backends (local, k2_6_local, k2_6_openrouter, claude, ollama_cloud) on a fixed task set. The verifiers infrastructure becomes the AICP routing-decision benchmark suite.

## Relationships

- BUILDS ON: [[src-rlm-recursive-language-models-mit-oasys|Synthesis — RLM Implementation Companion]] (verifiers' RLMEnv is the productized version of the RLM SDK pattern)
- BUILDS ON: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|Synthesis — RLM Paper Deep Dive]] (verifiers + prime-rl together = the open-source path to reproduce the paper's training)
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] (Prime CLI `.prime/skills/` is a production-scale instance of the skills layer)
- RELATES TO: [[model-markdown-as-iac|Model — Markdown as IaC]] (AGENTS.md compilation system, endpoint config TOML, structured prompts)
- RELATES TO: [[model-claude-code|Model — Claude Code]] (`.claude/skills/` symlinks to `.prime/skills/`; claude-aware integration)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (`vf.ensure_keys(...)` validates declared API keys early)
- COMPARES TO: [[src-claude-code-harness-features|Synthesis — Claude Code Harness Features]] (different agent runtime, verifiers focuses on RL training where Claude Code focuses on coding agent)
- COMPARES TO: [[src-opencode-harness-features|Synthesis — OpenCode Harness Features]] (verifiers v0.1.12 explicitly upstreamed opencode harnesses)
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (verifiers + prime-rl is the Prime Intellect open-source training tier in the framework)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (enables local + cloud RL training on consumer + datacenter GPUs)

## Backlinks

[[Synthesis — RLM Implementation Companion]]
[[Synthesis — RLM Paper Deep Dive]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[Model — Markdown as IaC]]
[[model-claude-code|Model — Claude Code]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[Synthesis — Claude Code Harness Features]]
[[Synthesis — OpenCode Harness Features]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[2026 Consumer Hardware AI Stack]]

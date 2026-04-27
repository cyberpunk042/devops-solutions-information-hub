# PrimeIntellect-ai/verifiers

Source: https://github.com/PrimeIntellect-ai/verifiers
Ingested: 2026-04-27
Type: documentation

---

# README

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/40c36e38-c5bd-4c5a-9cb3-f7b902cd155d">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/6414bc9b-126b-41ca-9307-9e982430cde8">
    <img alt="Prime Intellect" src="https://github.com/user-attachments/assets/6414bc9b-126b-41ca-9307-9e982430cde8" width="312" style="max-width: 100%;">
  </picture>
</p>

---

<h3 align="center">
Verifiers: Environments for LLM Reinforcement Learning
</h3>

<p align="center">
  <a href="https://docs.primeintellect.ai/verifiers">Documentation</a> •
  <a href="https://app.primeintellect.ai/dashboard/environments?ex_sort=most_stars">Environments Hub</a> •
  <a href="https://github.com/PrimeIntellect-ai/prime-rl">PRIME-RL</a>
</p>

---

<p align="center">
  <a href="https://github.com/PrimeIntellect-ai/verifiers/actions/workflows/style.yml">
    <img src="https://github.com/PrimeIntellect-ai/verifiers/actions/workflows/style.yml/badge.svg" alt="Style" />
  </a>
  <a href="https://github.com/PrimeIntellect-ai/verifiers/actions/workflows/test.yml">
    <img src="https://github.com/PrimeIntellect-ai/verifiers/actions/workflows/test.yml/badge.svg" alt="Test" />
  </a>
  <a href="https://github.com/PrimeIntellect-ai/verifiers/actions/workflows/publish-envs.yml">
    <img src="https://github.com/PrimeIntellect-ai/verifiers/actions/workflows/publish-envs.yml/badge.svg" alt="Envs" />
  </a>
</p>

## News & Updates

- [04/17/26] v0.1.12 is released, featuring a new composable Task/Agent/Environment architecture, upstreamed opencode and RLM harnesses/tasksets, major `RLMEnv` improvements (context dropping, prompt builder, hardened transport), multi-worker env server support, expanded `vf-tui` capabilities, and richer eval configuration.
- [03/12/26] v0.1.11 is released, featuring a unified client stack, major `RLMEnv` and env server reliability improvements, a substantially refined eval TUI, new pass@k and ablation sweep support, and bundled opencode environments.
- [02/10/26] v0.1.10 is released, featuring OpenEnv and BrowserEnv integrations, resumed evals, improved rollout and token tracking, safer sandbox lifecycle behavior, refreshed workspace setup, and opencode harbor improvements.
- [01/08/26] v0.1.9 is released, featuring a number of new experimental environment class types, monitor rubrics for automatic metric collection, improved workspace setup flow, improved error handling, bug fixes, and a documentation overhaul.
- [11/19/25] v0.1.8 is released, featuring a major refactor of the rollout system to use trajectory-based tracking for token-in token-out training across turns, as well as support for truncated or branching rollouts.
- [11/07/25] Verifiers v0.1.7 is released! This includes an improved quickstart configuration for training with [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl), a new included "nano" trainer (`vf.RLTrainer`, replacing `vf.GRPOTrainer`), and a number of bug fixes and improvements to the documentation.
- [10/27/25] A new iteration of the Prime Intellect [Environments Program](https://docs.google.com/spreadsheets/d/13UDfRDjgIZXsMI2s9-Lmn8KSMMsgk2_zsfju6cx_pNU/edit?gid=0#gid=0) is live!  


# Overview

Verifiers is our library for creating environments to train and evaluate LLMs.

Environments contain everything required to run and evaluate a model on a particular task:
- A *dataset* of task inputs
- A *harness* for the model (tools, sandboxes, context management, etc.)
- A reward function or *rubric* to score the model's performance

Environments can be used for training models with reinforcement learning (RL), evaluating capabilities, generating synthetic data, experimenting with agent harnesses, and more. 

Verifiers is tightly integrated with the [Environments Hub](https://app.primeintellect.ai/dashboard/environments?ex_sort=most_stars), as well as our training framework [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) and our [Hosted Training](https://app.primeintellect.ai/dashboard/training) platform.

## Getting Started

Ensure you have `uv` installed, as well as the `prime` [CLI](https://docs.primeintellect.ai/cli-reference/introduction) tool:
```bash
# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
# install the prime CLI
uv tool install prime
# log in to the Prime Intellect platform
prime login
```
To set up a new workspace for developing environments, do:
```bash
# ~/dev/my-lab
prime lab setup 
```

This sets up a Python project if needed (with `uv init`), installs `verifiers` (with `uv add verifiers`), creates the recommended workspace structure, and downloads useful starter files:
```
configs/
├── endpoints.toml      # OpenAI-compatible API endpoint configuration
├── rl/                 # Example configs for Hosted Training
├── eval/               # Example multi-environment eval configs
└── gepa/               # Example configs for prompt optimization
.prime/
└── skills/             # Bundled workflow skills for create/browse/review/eval/GEPA/train/brainstorm
environments/
└── AGENTS.md           # Documentation for AI coding agents
AGENTS.md               # Top-level documentation for AI coding agents
CLAUDE.md               # Claude-specific pointer to AGENTS.md
```

Alternatively, add `verifiers` to an existing project:
```bash
uv add verifiers && prime lab setup --skip-install
```

Environments built with Verifiers are self-contained Python modules. To initialize a fresh environment template, do:
```bash
prime env init my-env # creates a new template in ./environments/my_env
```
For OpenEnv integration, use:
```bash
prime env init my-openenv --openenv
```
Then copy your OpenEnv project into `environments/my_openenv/proj/` and build the image with:
```bash
uv run vf-build my-openenv
```

This will create a new module called `my_env` with a basic environment template.
```
environments/my_env/
├── my_env.py           # Main implementation
├── pyproject.toml      # Dependencies and metadata
└── README.md           # Documentation
```

Environment modules should expose a `load_environment` function which returns an instance of the Environment object, and which can accept custom arguments. For example: 
```python
# my_env.py
import verifiers as vf

def load_environment(dataset_name: str = 'gsm8k') -> vf.Environment:
    dataset = vf.load_example_dataset(dataset_name) # 'question'
    async def correct_answer(completion, answer) -> float:
        completion_ans = completion[-1]['content']
        return 1.0 if completion_ans == answer else 0.0
    rubric = Rubric(funcs=[correct_answer])
    env = vf.SingleTurnEnv(dataset=dataset, rubric=rubric)
    return env
```

To install the environment module into your project, do:
```bash
prime env install my-env # installs from ./environments/my_env
```

To install an environment from the Environments Hub into your project, do:
```bash
prime env install primeintellect/math-python
```

To run a local evaluation with any OpenAI-compatible model, do:
```bash
prime eval run my-env -m openai/gpt-5-nano # run and save eval results locally
```
Evaluations use [Prime Inference](https://docs.primeintellect.ai/inference/overview) by default; configure your own API endpoints in `./configs/endpoints.toml`.

View local evaluation results in the terminal UI:
```bash
prime eval tui
```

To publish the environment to the [Environments Hub](https://app.primeintellect.ai/dashboard/environments?ex_sort=most_stars), do:
```bash
prime env push --path ./environments/my_env
```

To run an evaluation directly from the Environments Hub, do:
```bash
prime eval run primeintellect/math-python
```

## Documentation

**[Environments](docs/environments.md)** — Create datasets, rubrics, and custom multi-turn interaction protocols.

**[Evaluation](docs/evaluation.md)** - Evaluate models using your environments.

**[Training](docs/training.md)** — Train models in your environments with reinforcement learning.

**[Development](docs/development.md)** — Contributing to verifiers

**[API Reference](docs/reference.md)** — Understanding the API and data structures

**[FAQs](docs/faqs.md)** - Other frequently asked questions.


## Citation

Originally created by Will Brown ([@willccbb](https://github.com/willccbb)).

If you use this code in your research, please cite:

```bibtex
@misc{brown_verifiers_2025,
  author       = {William Brown},
  title        = {{Verifiers}: Environments for LLM Reinforcement Learning},
  howpublished = {\url{https://github.com/PrimeIntellect-ai/verifiers}},
  note         = {Commit abcdefg • accessed DD Mon YYYY},
  year         = {2025}
}
```



> **Deep fetch: 28 key files fetched beyond README.**



---

# FILE: .pre-commit-config.yaml

default_install_hook_types: [pre-commit, pre-push]
# Exclude Harbor task assets from linting
exclude: ^environments/.*/tasks/

repos:
  - repo: local
    hooks:
      - id: ruff-check
        name: ruff check
        entry: uv run ruff check --fix
        language: system
        types_or: [python, pyi]
      - id: ruff-format
        name: ruff format
        entry: uv run ruff format
        language: system
        types_or: [python, pyi]
      - id: sync-agents-md
        name: Sync AGENTS.md from docs
        entry: uv run python scripts/sync.py
        language: system
        files: ^(docs/environments\.md|assets/agents/.*\.md|scripts/sync\.py)$
        pass_filenames: false
      - id: ty
        name: ty (ci parity)
        entry: uv run --python 3.13 ty check verifiers
        language: system
        pass_filenames: false
        stages: [pre-push]



---

# FILE: .readthedocs.yaml

# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Redirect to new docs at docs.primeintellect.ai/verifiers
build:
  os: ubuntu-24.04
  tools:
    python: "3.12"
  commands:
    - mkdir -p $READTHEDOCS_OUTPUT/html
    - cp assets/rtd-redirect/index.html $READTHEDOCS_OUTPUT/html/index.html



---

# FILE: AGENTS.md

# AGENTS.md

<!-- Generated for repository development workflows. Do not edit directly. -->

## Shared Best Practices (All Contexts)

These points are direct restatements of Verifiers docs so agents can follow the same golden-path workflows.

- Environments are expected to expose `load_environment(...) -> vf.Environment` and be installable with `prime env install <env-name>`. (See `docs/overview.md` and `docs/environments.md`.)
- Validate environment behavior with `prime eval run <env-name> ...` before sharing/publishing changes. Treat `prime eval run` as the canonical eval path: it saves results automatically, and agents should not add opt-out flags such as `--skip-upload` unless the user explicitly requests that deviation so runs stay visible in the private Evaluations tab and in `prime eval tui`. (See `docs/overview.md` and `docs/development.md`.)
- Use `ToolEnv`/`MCPEnv` for stateless tools and `StatefulToolEnv` when per-rollout state must persist (sandbox/session/db handles). (See `docs/environments.md`.)
- If external API keys are required, validate them in `load_environment()` with `vf.ensure_keys(...)` so failures are explicit and early. (See `docs/environments.md`.)

## Repository Development Notes

Use this guidance when contributing to the `verifiers` repository itself.

- Always run `uv run pre-commit install` before making any changes.
- Run the documented contributor checks for touched areas: `uv run ruff check --fix .`, `uv run pytest tests/`, and `uv run pre-commit run --all-files` as needed. (See `docs/development.md`.)
- Keep changes aligned with documented architecture (`verifiers/`, `environments/`, `configs/`, `tests/`, `docs/`) and update docs when behavior changes. (See `docs/development.md`.)
- Prefer a single clear path over maintaining parallel approaches by default; if two options exist, preserve both only when there is an explicit long-term reason.
- Aggressively deprecate/remove inferior paths when they are not part of an intended multi-option contract, especially in repo-internal development workflows.



---

# FILE: CLAUDE.md

# CLAUDE.md

<!-- Generated for repository development workflows. Do not edit directly. -->

Before beginning work in this repository, read `AGENTS.md` and follow all scoped AGENTS guidance.



---

# FILE: assets/agents/common_best_practices.md

## Shared Best Practices (All Contexts)

These points are direct restatements of Verifiers docs so agents can follow the same golden-path workflows.

- Environments are expected to expose `load_environment(...) -> vf.Environment` and be installable with `prime env install <env-name>`. (See `docs/overview.md` and `docs/environments.md`.)
- Validate environment behavior with `prime eval run <env-name> ...` before sharing/publishing changes. Treat `prime eval run` as the canonical eval path: it saves results automatically, and agents should not add opt-out flags such as `--skip-upload` unless the user explicitly requests that deviation so runs stay visible in the private Evaluations tab and in `prime eval tui`. (See `docs/overview.md` and `docs/development.md`.)
- Use `ToolEnv`/`MCPEnv` for stateless tools and `StatefulToolEnv` when per-rollout state must persist (sandbox/session/db handles). (See `docs/environments.md`.)
- If external API keys are required, validate them in `load_environment()` with `vf.ensure_keys(...)` so failures are explicit and early. (See `docs/environments.md`.)



---

# FILE: assets/agents/compilation_design.md

# AGENTS / CLAUDE Compilation Design

## Problem

The repository currently uses a single root `AGENTS.md` as both:

1. Contributor guidance for this repo.
2. Downloaded guidance for end users (`prime lab setup` / `vf-setup`).

That coupling makes edits noisy and mixes audiences.

## Goals

- Separate **source-of-truth content** for:
  - shared best practices,
  - repo-only guidance,
  - end-user lab guidance.
- Compile outputs for both audiences without duplicating text.
- Move setup-downloaded AGENTS/CLAUDE sources under `assets/lab/`.
- Keep environment guide generation (`environments/AGENTS.md`) in the same compile flow.

## Proposed Source Layout

```
assets/agents/
├── common_best_practices.md
├── repo_development_best_practices.md
├── end_user_best_practices.md
└── compilation_design.md
```

## Compiled Outputs

Generated by the repository sync tooling:

- `AGENTS.md` = common + repo development sections.
- `CLAUDE.md` = repo-oriented pointer to `AGENTS.md`.
- `assets/lab/AGENTS.md` = common + end-user sections.
- `assets/lab/CLAUDE.md` = end-user pointer to workspace AGENTS files.
- `environments/AGENTS.md` and `assets/lab/environments/AGENTS.md` = built from `docs/environments.md`.

## Portability Note

Files under `assets/` are intended to be copied into lab workspaces.
They should not rely on repository-local script paths or suggest a fixed provenance location.

## Setup Integration

`verifiers/scripts/setup.py` should download AGENTS/CLAUDE files from `assets/lab/` so the setup path consumes end-user docs only.

## Initial Implementation Scope

- Add modular docs stubs for shared/repo/end-user guidance.
- Replace sync script with a compiler-style generator for all targets.
- Update setup downloader URLs to `assets/lab/...`.
- Keep generated root files for repo contributors.

## Future Extensions

- Add section-level metadata (ordering, include conditions).
- Add CI check to enforce generated files are up to date.
- Optionally generate additional assistant-specific pointers (e.g., Cursor/Gemini).



---

# FILE: assets/agents/end_user_best_practices.md

## End-User Lab Workspace Notes

Use this guidance in projects created via `prime lab setup`.

- Treat `.prime/skills/` as the canonical skill entrypoint in Lab workspaces. Use the bundled skills first for create/browse/review/eval/GEPA/train/brainstorm workflows before ad hoc approaches.
- Keep endpoint aliases in `./configs/endpoints.toml` and use `endpoint_id`/model shortcuts in commands and configs.
- NEVER initialize environment source code manually; ALWAYS create new environments with `prime env init`.
- Use the Prime CLI for all environment lifecycle operations (`prime env init` → `prime env install` → `prime eval run` → `prime env push`) rather than ad-hoc scripts.
- Treat `prime eval run` as the default eval path. It already saves results automatically; do not add `--skip-upload` or other opt-out deviations unless the user explicitly requests them, so logs and results stay available in the private Evaluations tab and via `prime eval tui`.
- NEVER begin environment development before `prime lab setup` has been run; if work starts outside that structure, recommend adjusting course into a proper lab workspace before continuing.
- Keep each environment self-contained under `environments/<env_name>/` with `pyproject.toml`, implementation, and README so each abstraction has a dedicated home and the workspace stays maintainable.
- Follow environment best practices strictly (for example `load_environment(...)`, `vf.ensure_keys(...)`, and the documented environment class patterns) to avoid brittle or messy implementations.
- Use `prime env push --path ./environments/<env_name>` only after local eval behavior is verified.
- Treat the `prime lab setup` structure as the idiomatic workspace for complex environment workflows: agents can mediate most platform complexity while users learn patterns progressively as needed.
- When users request an approach that would deviate from these guidelines, explain the relevant Prime/Verifiers concepts and recommend the compliant path.



---

# FILE: assets/agents/repo_development_best_practices.md

## Repository Development Notes

Use this guidance when contributing to the `verifiers` repository itself.

- Always run `uv run pre-commit install` before making any changes.
- Run the documented contributor checks for touched areas: `uv run ruff check --fix .`, `uv run pytest tests/`, and `uv run pre-commit run --all-files` as needed. (See `docs/development.md`.)
- Keep changes aligned with documented architecture (`verifiers/`, `environments/`, `configs/`, `tests/`, `docs/`) and update docs when behavior changes. (See `docs/development.md`.)
- Prefer a single clear path over maintaining parallel approaches by default; if two options exist, preserve both only when there is an explicit long-term reason.
- Aggressively deprecate/remove inferior paths when they are not part of an intended multi-option contract, especially in repo-internal development workflows.



---

# FILE: assets/templates/browserbase/cua/README.md

# CUA Primitives API Server

A Fastify server that exposes Stagehand's Computer Use Agent (CUA) browser primitives as REST endpoints, enabling external agents to control browser sessions remotely.

> **Note**: This server is automatically deployed to sandbox containers when using `BrowserEnv` with `mode="cua"` and `use_sandbox=True` (the default). You typically don't need to run this server manually unless you're doing local development.

## Automatic Sandbox Deployment

When using `BrowserEnv(mode="cua")`, the server is automatically:
1. Uploaded to a sandbox container
2. Started via `setup.sh`
3. Accessed via curl commands inside the sandbox
4. Cleaned up when the rollout completes

```python
# This automatically deploys the CUA server to a sandbox
env = BrowserEnv(
    mode="cua",
    dataset=dataset,
    rubric=rubric,
)
```

## Manual Usage (Local Development)

For local development or debugging, you can run the server manually:

```bash
# Start the server (with hot reload)
pnpm dev

# Or start without hot reload
pnpm start

# Custom port via environment variable
CUA_SERVER_PORT=8080 pnpm dev
```

Then configure BrowserEnv to use the manual server:

```python
env = BrowserEnv(
    mode="cua",
    use_sandbox=False,
    server_url="http://localhost:3000",
    dataset=dataset,
    rubric=rubric,
)
```

## Architecture

```
External Agent -> Fastify API -> BrowserSessionManager -> Stagehand Page -> Browser
```

## Prerequisites

```bash
npm install @browserbasehq/stagehand fastify
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CUA_SERVER_PORT` | `3000` | Server port |
| `CUA_SERVER_HOST` | `0.0.0.0` | Server host |

## API Endpoints

### Health Check

```bash
GET /health
```

Returns server status and active session count.

### List Sessions

```bash
GET /sessions
```

Returns array of active session IDs.

### Create Session

```bash
POST /sessions
Content-Type: application/json

{
  "env": "LOCAL",           // or "BROWSERBASE"
  "viewport": {
    "width": 1024,
    "height": 768
  }
}
```

Returns:
```json
{
  "sessionId": "session_1234567890_abc123",
  "state": {
    "screenshot": "base64...",
    "url": "about:blank",
    "viewport": { "width": 1024, "height": 768 }
  }
}
```

### Get Session State

```bash
GET /sessions/:id/state
```

Returns current browser state (screenshot, URL, viewport).

### Close Session

```bash
DELETE /sessions/:id
```

Closes the browser and removes the session.

### Execute Action

```bash
POST /sessions/:id/action
Content-Type: application/json

{
  "type": "click",
  "x": 100,
  "y": 200
}
```

Returns:
```json
{
  "success": true,
  "state": {
    "screenshot": "base64...",
    "url": "https://example.com",
    "viewport": { "width": 1024, "height": 768 }
  }
}
```

## Available Actions

### Mouse Actions

| Action | Parameters | Description |
|--------|------------|-------------|
| `click` | `x`, `y`, `button?`, `clickCount?` | Click at coordinates |
| `double_click` | `x`, `y` | Double-click at coordinates |
| `tripleClick` | `x`, `y` | Triple-click at coordinates |
| `drag` | `path: [{x, y}, ...]` | Drag along path |
| `move` | - | No-op (cursor visualization) |

### Keyboard Actions

| Action | Parameters | Description |
|--------|------------|-------------|
| `type` | `text` | Type text into focused element |
| `keypress` | `keys` (string or array) | Press keyboard keys |

### Navigation Actions

| Action | Parameters | Description |
|--------|------------|-------------|
| `goto` | `url` | Navigate to URL |
| `back` | - | Go back in history |
| `forward` | - | Go forward in history |
| `scroll` | `x?`, `y?`, `scroll_x?`, `scroll_y?` | Scroll the page |

### Utility Actions

| Action | Parameters | Description |
|--------|------------|-------------|
| `wait` | `timeMs?` (default: 1000) | Wait for duration |
| `screenshot` | - | No-op (always returned in response) |

## Example Usage

```bash
# Create a session
SESSION=$(curl -s -X POST http://localhost:3000/sessions | jq -r '.sessionId')

# Navigate to a website
curl -X POST http://localhost:3000/sessions/$SESSION/action \
  -H "Content-Type: application/json" \
  -d '{"type": "goto", "url": "https://example.com"}'

# Click a button
curl -X POST http://localhost:3000/sessions/$SESSION/action \
  -H "Content-Type: application/json" \
  -d '{"type": "click", "x": 150, "y": 300}'

# Type into an input
curl -X POST http://localhost:3000/sessions/$SESSION/action \
  -H "Content-Type: application/json" \
  -d '{"type": "type", "text": "Hello, World!"}'

# Press Enter
curl -X POST http://localhost:3000/sessions/$SESSION/action \
  -H "Content-Type: application/json" \
  -d '{"type": "keypress", "keys": "Enter"}'

# Scroll down
curl -X POST http://localhost:3000/sessions/$SESSION/action \
  -H "Content-Type: application/json" \
  -d '{"type": "scroll", "x": 640, "y": 360, "scroll_y": 500}'

# Close the session
curl -X DELETE http://localhost:3000/sessions/$SESSION
```

## Response Format

All action responses include the full browser state:

```typescript
interface ActionResponse {
  success: boolean;
  error?: string;
  state: {
    screenshot: string;  // base64 PNG
    url: string;
    viewport: {
      width: number;
      height: number;
    };
  };
}
```

## Error Handling

Errors return appropriate HTTP status codes:

- `404` - Session not found
- `500` - Action execution failed

```json
{
  "error": "Session session_123 not found",
  "code": "SESSION_NOT_FOUND"
}
```

## File Structure

```
cua-server/
├── index.ts           # Entry point
├── server.ts          # Fastify routes
├── sessionManager.ts  # Browser session lifecycle
├── actionExecutor.ts  # CUA primitive execution
├── stateCapture.ts    # Screenshot & state helpers
├── types.ts           # TypeScript types
├── setup.sh           # Sandbox initialization script (used by CUASandboxMode)
├── package.json       # Dependencies
├── tsconfig.json      # TypeScript configuration
└── README.md          # This file
```




---

# FILE: assets/templates/browserbase/cua/package.json

{
  "name": "cua-primitives-server",
  "version": "1.0.0",
  "description": "CUA Primitives API Server - Browser automation primitives as REST endpoints",
  "type": "module",
  "scripts": {
    "start": "tsx index.ts",
    "dev": "tsx watch index.ts",
    "build:binary": "bash scripts/build-binary.sh",
    "build:binary:docker": "docker build --platform linux/amd64 -f Dockerfile.build -t cua-builder . && docker run --rm --platform linux/amd64 -v $(pwd)/dist:/output cua-builder"
  },
  "dependencies": {
    "@browserbasehq/stagehand": "^3.0.5",
    "fastify": "^5.0.0",
    "dotenv": "^16.4.5",
    "deepmerge": "^4.3.1",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "esbuild": "^0.27.2",
    "postject": "^1.0.0-alpha.6",
    "tsx": "^4.10.5",
    "typescript": "^5.2.2"
  },
  "packageManager": "pnpm@9.15.0"
}




---

# FILE: assets/templates/browserbase/cua/sea-config.json

{
  "main": "dist/sea/bundle.cjs",
  "output": "dist/sea/sea-prep.blob"
}



---

# FILE: assets/templates/browserbase/cua/tsconfig.json

{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "resolveJsonModule": true,
    "declaration": false,
    "outDir": "./dist",
    "rootDir": "."
  },
  "include": ["*.ts"],
  "exclude": ["node_modules", "dist"]
}




---

# FILE: docs/development.md

# Development & Testing

This guide covers setup, testing, and contributing to the verifiers package.

## Table of Contents

- [Setup](#setup)
- [Project Structure](#project-structure)
- [Prime CLI Plugin Export](#prime-cli-plugin-export)
- [Running Tests](#running-tests)
- [Writing Tests](#writing-tests)
- [Contributing](#contributing)
- [Common Issues](#common-issues)
- [Environment Development](#environment-development)
- [Quick Reference](#quick-reference)

## Setup

### Prerequisites
- Python 3.13 recommended for CI parity with Ty checks
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
# Clone and install for development
git clone https://github.com/PrimeIntellect-ai/verifiers.git
cd verifiers

# CPU-only development:
uv sync

# GPU-based trainer development:
uv sync --all-extras

# Install pre-commit hooks (including pre-push Ty gate):
uv run pre-commit install
```

## Project Structure

```
verifiers/
├── verifiers/          # Main package
│   ├── envs/           # Environment classes
│   │   ├── integrations/   # Third-party wrappers (TextArena, ReasoningGym)
│   │   └── experimental/   # Newer environments (MCP, Harbor, etc.)
│   ├── parsers/        # Parser classes  
│   ├── rubrics/        # Rubric classes
│   ├── rl/             # Training infrastructure
│   │   ├── inference/  # vLLM server utilities
│   │   └── trainer/    # Trainer implementation
│   ├── cli/            # Prime-facing CLI modules and plugin exports
│   ├── scripts/        # Compatibility wrappers around verifiers/cli commands
│   └── utils/          # Utilities
├── environments/       # Installable environment modules
├── configs/            # Example training configurations
├── tests/              # Test suite
└── docs/               # Documentation
```

## Prime CLI Plugin Export

Verifiers exports a plugin consumed by `prime` so command behavior is sourced from verifiers modules.

Entry point:

```python
from verifiers.cli.plugins.prime import get_plugin

plugin = get_plugin()
```

The plugin exposes:

- `api_version` (current: `1`)
- command modules:
  - `eval_module` (`verifiers.cli.commands.eval`)
  - `gepa_module` (`verifiers.cli.commands.gepa`)
  - `install_module` (`verifiers.cli.commands.install`)
  - `init_module` (`verifiers.cli.commands.init`)
  - `setup_module` (`verifiers.cli.commands.setup`)
  - `build_module` (`verifiers.cli.commands.build`)
- `build_module_command(module_name, args)` to construct subprocess invocation for a command module

Contributor guidance:

- Add new prime-facing command logic under `verifiers/cli/commands/`.
- Export new command modules through `PrimeCLIPlugin` in `verifiers/cli/plugins/prime.py`.
- Keep `verifiers/scripts/*` as thin compatibility wrappers that call into `verifiers/cli`.

## Running Tests

```bash
# Run all tests
uv run pytest tests/

# Run with coverage
uv run pytest tests/ --cov=verifiers --cov-report=html

# Run specific test file
uv run pytest tests/test_parser.py

# Stop on first failure with verbose output
uv run pytest tests/ -xvs

# Run tests matching a pattern
uv run pytest tests/ -k "xml_parser"

# Run environment tests
uv run pytest tests/test_envs.py -vv

# Run environment tests across all CPU cores
uv run pytest -n auto tests/test_envs.py -vv

# Run specific environment tests
uv run pytest tests/test_envs.py -k math_python
```

The test suite includes 380+ tests covering parsers, rubrics, environments, and utilities.

## Writing Tests

### Test Structure

```python
class TestFeature:
    """Test the feature functionality."""
    
    def test_basic_functionality(self):
        """Test normal operation."""
        # Arrange
        feature = Feature()
        
        # Act
        result = feature.process("input")
        
        # Assert
        assert result == "expected"
    
    def test_error_handling(self):
        """Test error cases."""
        with pytest.raises(ValueError):
            Feature().process(invalid_input)
```

### Using Mocks

The test suite provides a `MockClient` in `conftest.py` that implements the `Client` interface:

```python
def test_with_mock(mock_client):
    mock_client.set_default_responses(chat_response="test answer")
    env = vf.SingleTurnEnv(client=mock_client, model="test", ...)
    # Test without real API calls
```

### Guidelines

1. **Test both success and failure cases**
2. **Use descriptive test names** that explain what's being tested
3. **Leverage existing fixtures** from `conftest.py`
4. **Group related tests** in test classes
5. **Keep tests fast** - use mocks instead of real API calls

## Contributing

### Workflow

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make changes** following existing patterns
4. **Add tests** for new functionality
5. **Run tests**: `uv run pytest tests/`
6. **Install hooks once per clone**: `uv run pre-commit install`
7. **Commit and push** (hooks run automatically on each commit/push)
8. **Update docs** if adding/changing public APIs
9. **Submit PR** with clear description

### Code Style

- Strict `ruff` enforcement via pre-commit hooks
- `ty` runs in the pre-push hook via `uv run --python 3.13 ty check verifiers`
- Use type hints for function parameters and returns
- Write docstrings for public functions/classes
- Keep functions focused and modular
- Fail fast, fail loud - no defensive programming or silent fallbacks

### PR Checklist

- [ ] Tests pass locally (`uv run pytest tests/`)
- [ ] Pre-commit and pre-push hooks pass on latest commit/push
- [ ] Added tests for new functionality
- [ ] Updated documentation if needed

## Common Issues

### Import Errors
```bash
# Ensure package is installed in development mode
uv sync
```

### Integration Tests
```bash
# Install optional dependencies for specific integrations
uv sync --extra ta   # for TextArenaEnv
uv sync --extra rg   # for ReasoningGymEnv
```

### Test Failures
```bash
# Debug specific test
uv run pytest tests/test_file.py::test_name -vvs --pdb
```

## Environment Development

### Creating a New Environment Module

```bash
# Initialize template
prime env init my-environment

# Install locally for testing
prime env install my-environment

# Test your environment
prime eval run my-environment -m openai/gpt-4.1-mini -n 5
```

### Environment Module Structure

```python
# my_environment.py
import verifiers as vf

def load_environment(**kwargs):
    """Load the environment."""
    dataset = vf.load_example_dataset("dataset_name")
    parser = vf.XMLParser(fields=["reasoning", "answer"])
    
    def reward_func(parser, completion, answer, **kwargs):
        return 1.0 if parser.parse_answer(completion) == answer else 0.0
    
    rubric = vf.Rubric(
        funcs=[reward_func, parser.get_format_reward_func()],
        weights=[1.0, 0.2],
        parser=parser
    )
    
    return vf.SingleTurnEnv(
        dataset=dataset,
        parser=parser,
        rubric=rubric,
        **kwargs
    )
```

## Quick Reference

### Essential Commands

```bash
# Development setup
uv sync                               # CPU-only
uv sync --all-extras                  # With RL/training extras
uv run pre-commit install             # One-time per clone (installs pre-commit + pre-push)

# Run tests
uv run pytest tests/                  # All tests
uv run pytest tests/ -xvs             # Debug mode
uv run pytest tests/ --cov=verifiers  # With coverage

# Run environment tests
uv run pytest tests/test_envs.py -vv              # All environments
uv run pytest tests/test_envs.py -k math_python   # Specific environment

# Linting
uv run ruff check --fix .             # Fix lint errors
uv run ruff format --check verifiers tests  # Verify Python formatting
uv run ty check verifiers             # Type check (matches CI Ty target)

# Environment tools
prime env init new-env                       # Create environment
prime env install new-env                    # Install environment
prime eval run new-env -m openai/gpt-4.1-mini -n 5  # Test environment
prime eval tui                               # Browse evals in the tree browser
```

### CLI Tools

 | Command | Description |
|---------|-------------|
| `prime eval run` | Run evaluations on environments |
| `prime env init` | Initialize new environment from template |
| `prime env install` | Install environment module |
| `prime lab setup` | Set up training workspace |
| `prime eval tui` | Terminal UI for browsing evals and rollout details |
| `prime rl run` | Launch Hosted Training |
| `uv run prime-rl` | Launch prime-rl training |

### Project Guidelines

- **Environments**: Installable modules with `load_environment()` function
- **Parsers**: Extract structured data from model outputs
- **Rubrics**: Define multi-criteria evaluation functions
- **Tests**: Comprehensive coverage with mocks for external dependencies



---

# FILE: docs/environments.md

# Environments

This guide walks through building environments in Verifiers, from simple single-turn tasks to complex multi-turn agents with tools. See [Overview](overview.md) for how to initialize a new environment template.

## Table of Contents
- [Your First Environment](#your-first-environment)
- [Datasets](#datasets)
  - [Building the Prompt](#building-the-prompt)
  - [Evaluation Datasets](#evaluation-datasets)
  - [Lazy Loading with DatasetBuilder](#lazy-loading-with-datasetbuilder)
- [Rubrics](#rubrics)
  - [Reward Functions](#reward-functions)
  - [Multiple Reward Functions](#multiple-reward-functions)
  - [Execution Order and State](#execution-order-and-state)
  - [Group-Based Reward Functions](#group-based-reward-functions)
  - [Shared Objects](#shared-objects)
  - [Rubric Groups](#rubric-groups)
  - [Metrics and Monitor Rubrics](#metrics-and-monitor-rubrics)
- [Tool Environments](#tool-environments)
  - [MCP Tool Environments](#mcp-tool-environments)
  - [Stateful Tool Environments](#stateful-tool-environments)
- [Custom Multi-Turn Environments](#custom-multi-turn-environments)
  - [The Rollout Loop](#the-rollout-loop)
  - [Stop Conditions](#stop-conditions)
  - [Error Handling](#error-handling)
  - [State Initialization](#state-initialization)
  - [Cleanup and Teardown](#cleanup-and-teardown)
  - [Signaling Early Termination](#signaling-early-termination)
- [Developing Environments](#developing-environments)
  - [pyproject.toml](#pyprojecttoml)
  - [Managing Dependencies](#managing-dependencies)
  - [Installation](#installation)
- [Environment Groups](#environment-groups)
- [Performance](#performance)
  - [Avoiding Sync Operations](#avoiding-sync-operations)
  - [Executor Autoscaling](#executor-autoscaling)
- [Integrations and Experimental Environments](#integrations-and-experimental-environments)

## Your First Environment

The simplest single-turn environments need only a dataset of tasks and a reward function for scoring responses:

```python
import verifiers as vf
from datasets import Dataset

def load_environment():
    # Your task data
    dataset = Dataset.from_list([
        {"prompt": [{"role": "user", "content": "What is 2+2?"}], "answer": "4"},
        {"prompt": [{"role": "user", "content": "What is 3*5?"}], "answer": "15"},
    ])
    
    # Your reward function
    async def correct_answer(completion, answer) -> float:
        response = completion[-1]["content"]
        return 1.0 if answer in response else 0.0
    
    rubric = vf.Rubric(funcs=[correct_answer])
    
    return vf.SingleTurnEnv(dataset=dataset, rubric=rubric)
```

When running this environment, each row in the dataset becomes a **rollout**:

1. The `prompt` is sent to the model
2. The model generates a response, which becomes the `completion`
3. The reward function scores the result

In `SingleTurnEnv`, the simplest environment type, just a single model response occurs per rollout. More complex environment types will allow us to add tool use or other custom interaction protocols.

## Datasets

Environments use the `datasets` library from Hugging Face for loading and manipulating datasets. Each row typically has a `prompt` column, containing a list of initial messages to send to the model. Additionally, there are optional columns for scoring:

- `answer` — a simple string for ground truth comparisons
- `info` — structured metadata (dict or JSON string)

Depending on what your environment needs, you can include `answer`, `info`, both, or neither.

When using `info`, prefer using JSON strings if rows may have different schemas, e.g. different fields or nested structures:

```python
dataset = Dataset.from_list([
    {"prompt": [...], "info": '{"type": "math", "difficulty": 3}'},
    {"prompt": [...], "info": '{"type": "code", "language": "python"}'},
])
```

These are parsed into a `dict` by the environment when running rollouts. 


### Building the Prompt

The examples above use `prompt` directly, providing a list of messages ready to send to the model. Alternatively, you can provide a `question` column containing a string, and the environment will wrap it in a user message:

```python
dataset = Dataset.from_list([
    {"question": "What is 2+2?", "answer": "4"},
])
```

You can also pass a `system_prompt` to the environment, which prepends a system message:

```python
return vf.SingleTurnEnv(
    dataset=dataset,
    system_prompt="You are a helpful math tutor.",
    rubric=rubric,
)
```

Together, these construct the full prompt:
```python
[
    {"role": "system", "content": "You are a helpful math tutor."},
    {"role": "user", "content": "What is 2+2?"}
]
```

If your dataset already has a `prompt` column, `question` is ignored. However, if a `system_prompt` is provided, it will be prepended to existing prompts that don't already start with a system message.

### Evaluation Datasets

Environments can be initialized with a separate `eval_dataset` for evaluation, distinct from the training dataset:

```python
return vf.SingleTurnEnv(
    dataset=train_dataset,
    eval_dataset=eval_dataset,
    rubric=rubric,
)
```

When running `prime eval run`, the evaluation dataset is used by default. If no `eval_dataset` is provided, evaluation falls back to the training dataset.

### Lazy Loading with DatasetBuilder

For large datasets or when running multiple environment replicas, you can defer dataset loading using a `DatasetBuilder`—a callable that returns a `Dataset` when invoked:

```python
def get_dataset_builder(split: str = "train", seed: int = 42) -> vf.DatasetBuilder:
    """Returns a builder that lazily loads the dataset."""
    def build() -> Dataset:
        ds = load_dataset("my-dataset", split=split)
        ds = ds.shuffle(seed=seed)
        return ds
    return build

def load_environment():
    dataset_builder = get_dataset_builder(split="train")
    eval_builder = get_dataset_builder(split="test")
    
    return vf.SingleTurnEnv(
        dataset=dataset_builder,      # built on first access
        eval_dataset=eval_builder,    # built on first access
        rubric=rubric,
    )
```

The builder pattern is useful when:
- Dataset loading is expensive (e.g., downloading from Hugging Face)
- Multiple environment replicas don't all need to own the dataset
- You want to parameterize dataset creation without loading it immediately

When a raw `Dataset` is passed directly (the default pattern), it is loaded eagerly during environment initialization for backwards compatibility.

## Rubrics

Each environment has a `Rubric` that manages scoring. The rubric holds reward functions, combines their outputs into a final reward score, and tracks metrics for observability.

### Reward Functions

Reward functions evaluate rollouts and return floats, typically between 0.0 and 1.0. They can request data from the rollout by naming arguments directly:

```python
async def correct_answer(completion, answer) -> float:
    response = completion[-1]["content"]
    return 1.0 if answer in response else 0.0
```

The basic available arguments, if present, are:
- `completion` — the model's output (list of messages)
- `prompt` — the input messages
- `answer` — from dataset
- `info` — from dataset
- `state` — the full rollout state (used in more complex environments)

This reference pattern extends to additional objects that the rubric provides in more advanced use cases.

### Multiple Reward Functions

Rubrics can combine multiple reward functions with custom weights:

```python
async def check_keywords(completion, info) -> float:
    response = completion[-1]["content"]
    keywords = info["required_keywords"]
    found = sum(1 for kw in keywords if kw.lower() in response.lower())
    return found / len(keywords)

async def length_reward(completion) -> float:
    response = completion[-1]["content"]
    return 1.0 if len(response) < 500 else 0.5

rubric = vf.Rubric(
    funcs=[check_keywords, length_reward],
    weights=[1.0, 0.1]
)
```

The final rollout reward is computed as the weighted sum of all reward function scores.

Reward functions can also be added to a rubric after initialization:
```python
rubric = vf.Rubric()
rubric.add_reward_func(check_keywords, weight=1.0)
rubric.add_reward_func(length_reward, weight=0.1)
```

Beyond the final score, reward functions can be used to track metrics for observability by setting `weight=0`:

```python
async def response_length(completion) -> float:
    return float(len(completion[-1]["content"]))
rubric.add_metric(response_length)  # shorthand for weight=0
```

All reward functions (weighted or not) appear in the rollout metrics.

### Execution Order and State

Reward functions execute in the order they are added to the rubric. Since `state` is mutable and shared across all reward functions, earlier functions can store computed values for later functions to use:

```python
async def similarity_score(completion, answer, state) -> float:
    response = completion[-1]["content"]
    score = compute_similarity(response, answer)  # continuous 0-1
    state["similarity"] = score
    return score

async def similarity_threshold(state) -> float:
    return 1.0 if state["similarity"] > 0.8 else 0.0

rubric = vf.Rubric(
    funcs=[similarity_score, similarity_threshold],
    weights=[0.0, 1.0]  # log similarity, but only reward threshold
)
```

This avoids redundant computation when multiple reward functions need access to the same derived value.

### Group-Based Reward Functions

During evaluation and RL training, rollouts are organized into **groups** of rollouts from the same input example. When evaluating, group structure enables per-example aggregate statistics (e.g., pass@k). When training with RL, groups are used for advantage computation relative to other rollouts for the same example. For a dataset with 100 example rows, running 4 rollouts per example yields 100 groups of 4 rollouts each.

In some cases, it is useful for reward functions to operate at the group level, such as to measure diversity or compute relative rankings. To define a group reward function, use plural argument names (`completions`, `prompts`, `answers`, `infos`) and return a list of scores:

```python
async def diversity_bonus(completions) -> list[float]:
    """Reward unique responses within a group."""
    responses = [c[-1]["content"] for c in completions]
    unique = set(responses)
    # Higher reward if this response is unique
    return [0.2 if responses.count(r) == 1 else 0.0 for r in responses]

rubric = vf.Rubric(funcs=[correct_answer, diversity_bonus])
```

### Shared Objects

Beyond rollout data, reward functions can request static objects that live within the Rubric class. These are stored in the Rubric's `class_objects` dictionary, and can be added after initialization via `add_class_object()`:

```python
rubric = vf.Rubric(funcs=[my_reward_func])
rubric.add_class_object("my_helper", some_helper_object)

async def my_reward_func(completion, my_helper) -> float:
    # my_helper is now available by name
    return await my_helper.score(completion)
```

Two common types of shared objects are **parsers** and **judges**.

Parsers encapsulate logic for extracting structured content from model responses. When passed to a rubric, the parser is automatically available to reward functions:

```python
parser = vf.XMLParser(["reasoning", "answer"])
rubric = vf.Rubric(funcs=[my_reward_func], parser=parser)

async def my_reward_func(completion, parser) -> float:
    parsed = parser.parse_answer(completion)
    # parsed.reasoning, parsed.answer available
    ...
```

Parsers can also be passed to environments, where they are often used during rollouts to validate or extract content. This allows parsing logic to be shared between the environment's interaction loop and the rubric's reward functions.

Judges are used for tasks where deterministic evaluation is impractical, and an LLM is used to score responses. **JudgeRubric** is a built-in class which stores an LLM client inside the rubric, and provides a `judge` callable to reward functions for scoring responses:

```python
judge_rubric = vf.JudgeRubric(
    judge_model="gpt-4.1-mini",
)

async def judge_correctness(prompt, completion, answer, judge) -> float:
    verdict = await judge(prompt, completion, answer)
    return 1.0 if "yes" in verdict.lower() else 0.0

judge_rubric.add_reward_func(judge_correctness)
```

The `judge` callable formats a prompt comparing the model's response to the ground truth and returns the judge model's verdict.

For more control, JudgeRubric accepts a custom `judge_prompt` template and exposes its internals (`judge_client`, `judge_model`, `judge_prompt`, `judge_sampling_args`) as class objects:

```python
judge_rubric = vf.JudgeRubric(
    judge_model="gpt-4.1-mini",
    judge_prompt="""Rate the writing quality of this response from 0-10.
Response: {response}
Score:"""
)

async def quality_score(completion, judge_client, judge_model, judge_prompt, parser) -> float:
    response = parser.parse_answer(completion)
    filled_prompt = judge_prompt.format(response=response)
    result = await judge_client.chat.completions.create(
        model=judge_model,
        messages=[{"role": "user", "content": filled_prompt}],
    )
    # parse numeric score from result
    ...
    return score
```

### Rubric Groups

Environments can include multiple rubrics by combining them into a `RubricGroup` (which itself behaves as a single rubric), aggregating all rewards and metrics from constituent rubrics. This is particularly useful for conjoining multiple rubrics of different types.

For example, `MathRubric` is a built-in rubric that uses symbolic verification to check mathematical correctness:

```python
math_rubric = vf.MathRubric()
```

MathRubric includes a `correct_answer` reward function that parses `\boxed{}` answers and uses the `math-verify` library for symbolic equivalence checking. To add LLM-based evaluation alongside it:

```python
math_rubric = vf.MathRubric()
judge_rubric = vf.JudgeRubric(judge_model="gpt-4.1-mini")
judge_rubric.add_reward_func(judge_correctness, weight=0.5)

rubric = vf.RubricGroup([math_rubric, judge_rubric])
```

All rubrics in a group are executed in parallel, and the final reward is the sum of all rubric rewards. Metrics from all rubrics are collected together.

### Metrics and Monitor Rubrics

For simple cases, metrics can be added directly to a rubric via `add_metric()` as shown above. Monitor rubrics extend this pattern by packaging metrics into separate rubrics that are combined via `add_rubric()`. This allows each environment type in a class hierarchy to contribute its own metrics automatically.

Many environment types automatically include a monitor rubric that tracks metrics specific to their level of the environment class hierarchy:

| Environment | Tracked Metrics |
|-------------|-----------------|
| `MultiTurnEnv` | `num_turns` |
| `ToolEnv` | `total_tool_calls`, per-tool counts |
| `SandboxEnv` | `sandbox_ready_wait_time`, `sandbox_command_execution_time` |
| `PythonEnv` | `python_ready_wait_time` |

These metrics appear automatically in rollout results alongside any custom reward functions.

To add custom metrics to an environment, define a monitor rubric class and add it via `add_rubric()`:

```python
class MyMonitorRubric(vf.Rubric):
    def __init__(self):
        super().__init__()
        self.add_metric(self.custom_metric)
    
    async def custom_metric(self, state: vf.State) -> float:
        return len(state["trajectory"])

env = vf.ToolEnv(dataset=dataset, tools=tools, rubric=rubric)
env.add_rubric(MyMonitorRubric())
```

The environment automatically wraps rubrics in a `RubricGroup` as needed, so monitor rubrics stack up the class hierarchy—`PythonEnv` inherits metrics from both `SandboxEnv` and `ToolEnv`.

## Tool Environments

All currently-supported environment types in Verifiers are built on `MultiTurnEnv`, which implements the core single-agent rollout loop (even `SingleTurnEnv` is simply a `MultiTurnEnv` with `max_turns=1` and a placeholder `env_response` method). `ToolEnv` adds tool calling to this foundation.

Tools are defined as Python functions. Verifiers extracts tool schemas from function signatures and docstrings for use with OpenAI-compatible tool calling:

```python
async def calculate(expression: str) -> str:
    """Evaluate a mathematical expression.
    
    Args:
        expression: A mathematical expression to evaluate (e.g. "2 + 2 * 3")
    
    Returns:
        The result of the evaluation.
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

async def lookup(term: str) -> str:
    """Look up a term in the knowledge base.
    
    Args:
        term: The term to search for.
    
    Returns:
        Information about the term.
    """
    # your lookup logic here
    ...
```

The function name becomes the tool name, type hints define the parameter types, and the docstring provides both the tool description and individual parameter descriptions (via the Args section). Tools can be sync or async, though we always recommend using async for performance to avoid blocking the main thread.

To create a tool environment, pass the tools to `ToolEnv` directly:

```python
vf_env = vf.ToolEnv(
    dataset=dataset,
    tools=[calculate, lookup],
    rubric=rubric,
    max_turns=10,
)
```

During rollouts, the model can call tools, receive results, and continue reasoning until it produces a response without tool calls (or hits `max_turns`). Each turn consists of a model response followed by the environment's tool execution. Tool call counts are tracked automatically via monitor rubrics (see above).

### MCP Tool Environments

For tools implemented as MCP (Model Context Protocol) servers, `MCPEnv` extends `ToolEnv` to provide an integration that automatically connects to MCP servers and exposes their tools to the model:

```python
mcp_servers = [
    {
        "name": "fetch",
        "command": "uvx",
        "args": ["mcp-server-fetch"],
    },
]

vf_env = vf.MCPEnv(
    mcp_servers=mcp_servers,
    dataset=dataset,
    rubric=rubric,
)
```

### Stateful Tool Environments

`ToolEnv` and `MCPEnv` are designed for stateless, read-only tools where no session state needs to persist across calls within a rollout. For tools that require per-rollout state—such as a sandbox container, database connection, or session ID—use `StatefulToolEnv`.

The `setup_state` method is called at the beginning of each rollout for all environments which extend `MultiTurnEnv`, but is a no-op by default (including in `ToolEnv`). 

`StatefulToolEnv` overrides this to initialize per-rollout resources, and introduces two additional concepts:

1. **Hidden arguments**: Tool functions can have parameters that are injected by the environment but hidden from the model's tool schema (via `args_to_skip`)
2. **`update_tool_args`**: An abstract method you implement to inject state into tool calls at runtime

```python
class MySandboxEnv(vf.StatefulToolEnv):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_tool(self.run_code, args_to_skip=["session_id"])
    
    async def setup_state(self, state, **kwargs):
        state["session_id"] = await create_session()
        return await super().setup_state(state, **kwargs)
    
    def update_tool_args(self, tool_name, tool_args, messages, state, **kwargs):
        if tool_name == "run_code":
            tool_args["session_id"] = state["session_id"]
        return tool_args
    
    async def run_code(self, code: str, session_id: str) -> str:
        """Execute code in the sandbox."""
        return await execute_in_session(session_id, code)
```

The model sees `run_code(code: str)` in its tool schema, but the environment injects `session_id` from rollout state before each call.

Verifiers includes several built-in stateful environment classes: `SandboxEnv` provides a containerized bash shell, and `PythonEnv` extends it with a persistent Python REPL (both of which are configured for use with Prime Intellect's [Sandboxes](https://docs.primeintellect.ai/sandboxes/overview)). These handle sandbox lifecycle management automatically.

Both `SandboxEnv` and `CliAgentEnv` accept a `labels` parameter for tagging sandboxes:

```python
env = vf.SandboxEnv(
    dataset=dataset,
    rubric=rubric,
    labels=["experiment-1", "math-tasks"],  # optional labels for sandbox categorization
)
```

Labels are passed to the Prime Sandboxes API and can be used for organizing, filtering, and managing sandboxes across experiments or training runs.

Stateful environments often define methods decorated with `@vf.cleanup` (called after each rollout) or `@vf.teardown` (called once at environment shutdown) for resource management. These decorators, along with `@vf.stop` for custom stop conditions (boolean functions checked after each turn), are powerful tools for rollout lifecycle control in custom `MultiTurnEnv` subclasses.

## Custom Multi-Turn Environments

For interaction patterns beyond tool calling—games, simulations, or other custom protocols—`MultiTurnEnv` can be subclassed directly, exposing full control over the rollout loop's behavior.

### The Rollout Loop

Each rollout follows this structure:

1. **Initialize state** — `setup_state(state)` is called to prepare per-rollout resources
2. **Loop until done:**
   - Get prompt messages (initial prompt, or previous conversation + environment response)
   - Get model response
   - Check stop conditions — if any `@vf.stop` method returns `True`, exit loop
3. **Render completion** — final conversation is assembled into `state["completion"]`
4. **Cleanup** — all `@vf.cleanup` methods are called

The `env_response` method is an abstract method that must be overridden by all `MultiTurnEnv` subclasses, and defines how the environment responds after each model turn:

```python
class MyGameEnv(vf.MultiTurnEnv):
    async def env_response(self, messages: vf.Messages, state: vf.State) -> vf.Messages:
        """Generate the environment's response after each model turn."""
        parsed = self.parser.parse(messages)
        action = parsed.action
        feedback = process_action(action)
        return [{"role": "user", "content": feedback}]


async def correct_action(parser, completion, answer) -> float:
    parsed = parser.parse(completion)
    return 1.0 if parsed.action == answer else 0.0


def load_environment():
    parser = vf.XMLParser(fields=["action"])
    rubric = vf.Rubric(funcs=[correct_action], parser=parser)
    return MyGameEnv(dataset=dataset, rubric=rubric, parser=parser)
```

`env_response` receives the full conversation history thus far (and `state`) and returns a list of *new* messages to append. When a parser is passed to the environment, it becomes available as `self.parser`. Passing the same parser to the rubric makes it available to reward functions by name. For tool environments, `env_response` typically executes tool calls and returns results. For games or other custom protocols, this might involve parsing structured output (as above) and returning state updates or feedback.

Several other methods can optionally be overridden for more control in complex custom environments:

- `setup_state(state)` — add environment-specific state fields at rollout start
- `get_prompt_messages(state)` — customize how messages are assembled (e.g. for non-linear conversations)
- `render_completion(state)` — customize how the final completion is assembled
- `add_trajectory_step(state, step)` — set intermediate rewards, advantages, or extra metadata per turn

### Stop Conditions

Rollouts continue until a stop condition is met, checked after each model response. Custom stop conditions are defined with the `@vf.stop` decorator:

```python
class MyGameEnv(vf.MultiTurnEnv):
    @vf.stop
    async def game_won(self, state: vf.State) -> bool:
        return state.get("won", False)
    
    @vf.stop
    async def game_lost(self, state: vf.State) -> bool:
        return state.get("lives", 1) <= 0
```

`MultiTurnEnv` includes built-in stop conditions for errors, prompt length limits, `max_turns`, and `max_total_completion_tokens` by default.

Execution order can be controlled with `priority` (higher runs first). This is useful for checking cheap conditions before expensive ones:

```python
@vf.stop(priority=10)  # cheap keyword check runs first
async def answer_submitted(self, state: vf.State) -> bool:
    completion = state.get("completion", [])
    if not completion:
        return False
    return "FINAL ANSWER:" in completion[-1].get("content", "")

@vf.stop(priority=-10)  # expensive validation runs last
async def answer_detected(self, state: vf.State) -> bool:
    # only runs if cheap checks didn't already stop
    return await self.validator_client.check_for_answer(state)
```

### Error Handling

Verifiers defines a hierarchy of error types under `vf.Error`:

- `vf.ModelError` — errors from model interactions (e.g., `vf.EmptyModelResponseError`)
- `vf.OverlongPromptError` — prompt exceeds model context length
- `vf.ToolError` — tool-related errors (`vf.ToolParseError`, `vf.ToolCallError`)
- `vf.InfraError` — infrastructure errors (e.g., `vf.SandboxError`, `vf.TunnelError`)

When a `vf.Error` is raised during a rollout, it is automatically caught and stored in `state["error"]`, triggering the built-in `has_error` stop condition at the next check. This allows rollouts to terminate gracefully rather than crashing.

For tool environments, you can configure which errors should stop the rollout immediately via `stop_errors`:

```python
vf_env = vf.ToolEnv(
    tools=[my_tool],
    stop_errors=[vf.ToolParseError],  # stop on parse errors, but continue on other tool errors
    ...
)
```

Errors not in `stop_errors` are caught and returned as tool response messages, providing the model a chance to recover.

### State Initialization

Override `setup_state` to initialize per-rollout state:

```python
class MyGameEnv(vf.MultiTurnEnv):
    async def setup_state(self, state: vf.State) -> vf.State:
        state["board"] = initialize_board()
        state["score"] = 0
        return await super().setup_state(state)
```

### Cleanup and Teardown

For resource management, use `@vf.cleanup` (per-rollout) and `@vf.teardown` (at environment shutdown):

```python
class MyGameEnv(vf.MultiTurnEnv):
    @vf.cleanup
    async def save_game_log(self, state: vf.State):
        await log_game_result(state["game_id"], state["score"])

    @vf.teardown
    async def close_connections(self):
        await self.db_connection.close()
```

> **Important:** Cleanup methods should be **idempotent**—safe to call multiple times—and handle errors gracefully. This ensures correct behavior when rollouts are cancelled or interrupted, and that cleanup completes even when resources are in unexpected states.

### Signaling Early Termination

To end a rollout from within `env_response` (e.g., when the game ends), set `state["final_env_response"]`:

```python
async def env_response(self, messages: vf.Messages, state: vf.State) -> vf.Messages:
    if check_game_over(state):
        final_message = [{"role": "user", "content": "Game over! Final score: " + str(state["score"])}]
        state["final_env_response"] = final_message
        return final_message
    # ... normal response logic
```
This bypasses the normal model response loop and immediately terminates the rollout, which is useful when the environment response itself signals completion (e.g. a game is won, an answer is submitted) or is required for reward computation (e.g. final feedback or tool results).

## Developing Environments

Environments are packaged as installable Python projects. We recommend developing environments in a workspace with `environments/` and `configs/` folders. The `prime lab setup` command initializes this structure:

```bash
prime lab setup
```

The `prime env init` command initializes a new environment project:

```bash
prime env init my-env
```

This creates the following structure:

```
environments/my_env/
├── my_env.py          # environment implementation
├── pyproject.toml     # package metadata and dependencies
└── README.md          # documentation template
```

The environment file must export a `load_environment()` function that returns a `vf.Environment`. Explicitly declare any arguments your environment accepts:

```python
import verifiers as vf

def load_environment(difficulty: str = "easy", num_examples: int = -1) -> vf.Environment:
    # build dataset, rubric, etc.
    return vf.SingleTurnEnv(dataset=dataset, rubric=rubric)
```

### pyproject.toml

The `pyproject.toml` defines package metadata, dependencies, and evaluation defaults:

```toml
[project]
name = "my-env"
description = "My custom environment"
tags = ["single-turn", "math", "train", "eval"]
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "verifiers>=0.1.8",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build]
include = ["my_env.py", "pyproject.toml"]

[tool.verifiers.eval]
num_examples = 20
rollouts_per_example = 5
```

Key `pyproject.toml` sections:

- **`[project]`** — Package name (used by `prime env install` and `prime eval run`), description, version, and dependencies. The `tags` field is optional metadata for categorizing environments.
- **`[build-system]`** — Hatchling is used as the build backend for the Environments Hub.
- **`[tool.hatch.build]`** — Lists files to include in the package. Always include `pyproject.toml` alongside your environment file to ensure that environment metadata is available when the environment is installed. Add any additional source files here.
- **`[tool.verifiers.eval]`** — Default parameters for `prime eval run` when flags aren't provided.

### Managing Dependencies

All packages your environment needs must be declared in the `dependencies` array. Always include `verifiers` with a minimum version. If your environment uses additional libraries, add them here—they will be installed automatically when the environment is installed:

```toml
dependencies = [
    "verifiers>=0.1.8",
    "chromadb",
    "nltk>=3.9.2",
]
```

### Required API Keys

Environments that require external API keys (e.g., for judge models or external services) should validate them early in `load_environment()` using `vf.ensure_keys()`:

```python
import verifiers as vf

def load_environment(api_key_var: str = "OPENAI_API_KEY") -> vf.Environment:
    vf.ensure_keys([api_key_var])
    # now safe to use os.environ[api_key_var]
    ...
```

This raises `MissingKeyError` with a clear message listing all missing keys and instructions for setting them:

- **Environments Hub**: Add secrets (or link global secrets) on the environment's **Secrets** tab
- **Hosted Training**: Set `env_file` in your config (e.g., `env_file = ["secrets.env"]`)
- **Local**: Export in your shell (e.g., `export OPENAI_API_KEY=...`)

Document required variables in your README under a "Required Environment Variables" section.

### Installation

Install a local environment with `prime env install`:

```bash
prime env install my-env                    # from ./environments/my_env
prime env install my-env -p /path/to/environments   # custom path
```

This runs `uv pip install -e` for local environments, making them importable by `prime eval run` and other integrations.

## Environment Groups

`EnvGroup` combines multiple environments into a single environment class, enabling multi-task evaluation and training across heterogeneous environments from a unified entrypoint. Each sub-environment maintains its own dataset, rubric, and rollout logic, while the group handles routing and metric aggregation:

```python
math_env = load_math_environment()
code_env = load_code_environment()
reasoning_env = load_reasoning_environment()

combined = vf.EnvGroup(
    envs=[math_env, code_env, reasoning_env],
    env_names=["math", "code", "reasoning"],
)
```

The group concatenates all sub-environment datasets, tagging each row with a `task` column that routes rollouts to the appropriate environment for generation and scoring. Metrics from all environments are tracked together. 

## Performance

Verifiers runs rollouts concurrently on a single `asyncio` event loop. Any synchronous operation in environment code blocks **all** concurrent rollouts for its duration. At scale this adds up quickly — a 10ms sync call in at 2,000 concurrent rollouts serializes into 20 seconds of wall-clock blocking where no other rollout can make progress. The most impactful optimization is eliminating sync operations on the hot path rollout execution code, i.e. any method that runs *for each rollout* (e.g. `setup_state`, `env_response`, or reward functions).

### Avoiding Sync Operations

Common offenders include `time.sleep`, sync HTTP/LLM clients (`httpx.Client`, `OpenAI`), `deepcopy`, serialization, and file I/O. These should be **avoided at all costs**. Instead, use an async-native alternatives (e.g. `asyncio.sleep`, `httpx.AsyncClient`, `AsyncOpenAI`, `aiofiles`) or offload to the default thread pool with `asyncio.to_thread()`:

```python
# ❌ time.sleep blocks the event loop
time.sleep(1)
# ✅ asyncio.sleep yields control
await asyncio.sleep(1)

# ❌ sync HTTP clients
requests.get(url)
# ✅ async HTTP clients
async with httpx.AsyncClient() as client:
    await client.get(url)

# ❌ sync LLM clients
sync_client = OpenAI()
sync_client.chat.completions.create(...)
# ✅ use built-in async LLM calls
async_client = AsyncOpenAI()
await async_client.chat.completions.create(...)

# ❌ deepcopy blocks for large objects
copy.deepcopy(large_obj)
# ✅ offload to thread pool
await asyncio.to_thread(copy.deepcopy, large_obj)

# ❌ serialization blocks for large payloads
data_str = json.dumps(data)
# ✅ offload to thread pool (+use faster lib)
await asyncio.to_thread(orjson.dumps, data)

# ❌ sync file I/O
with open(file, "w") as f:
    f.write(data)
# ✅ use the built-in helper
from verifiers.utils.path_utils import write_temp_file
tmp_path = await asyncio.to_thread(write_temp_file, data, ".txt")
```

Note that `asyncio.to_thread()` releases the event loop but still holds the GIL. For truly CPU-bound operations (heavy computation, compilation, large data transforms >50ms), use a process pool instead:

```python
from concurrent.futures import ProcessPoolExecutor

executor = ProcessPoolExecutor(max_workers=4)

async def heavy_reward(data):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, cpu_bound_fn, data)
```

### Executor Autoscaling

`asyncio.to_thread()` dispatches work to a thread pool executor. By default Python's executor is small, but environments can scale it via `set_concurrency()`:

```python
env.set_concurrency(256)
```

This resizes both the default event-loop executor (used by `asyncio.to_thread()`) and all registered executors in one call. If your environment creates its own `ThreadPoolExecutor` or `ProcessPoolExecutor` (e.g. for a custom client), register it so it scales automatically:

```python
from concurrent.futures import ThreadPoolExecutor  # or ProcessPoolExecutor
from verifiers.utils.thread_utils import register_executor, unregister_executor

# register during init — if set_concurrency() was already called,
# the executor is immediately resized to match
self.my_executor = ThreadPoolExecutor(max_workers=4)
register_executor("my-env-client", self.my_executor)

# unregister during teardown (does not shut down the executor)
unregister_executor("my-env-client")
self.my_executor.shutdown()
```

In practice, you rarely need to call `set_concurrency()` yourself. Both `prime eval run` and `prime-rl` automatically compute the right worker count from the concurrency level. If you wish to override the automatic value during evaluation, you can do so with the `--extra-env-kwargs` flag:

```bash
prime eval run my-env -x '{"concurrency": 256}'
```

## Integrations and Experimental Environments

Beyond the core environment types, Verifiers includes integrations with several third-party environment libraries, as well as a few newer and more experimental environment classes (which are less stable and more subject to frequent changes).

Supported third-party environment integrations include:

- **`TextArenaEnv`** — wraps [TextArena](https://github.com/LeonGuertler/TextArena) text-based game environments
- **`ReasoningGymEnv`** — wraps [reasoning-gym](https://github.com/open-thought/reasoning-gym) procedural datasets
- **`BrowserEnv`** — unified browser automation via [Browserbase](https://browserbase.com) with DOM and CUA modes
- **`OpenEnvEnv`** — wraps OpenEnv gym and MCP contracts using Prime Sandboxes with prebuilt images referenced from `.build.json`

These require additional dependencies installed via extras (e.g., `uv add 'verifiers[ta]'` for TextArena, `uv add 'verifiers[browser]'` for BrowserEnv, `uv add 'verifiers[openenv]'` for OpenEnvEnv). For OpenEnv environments, build the bundled project image with `prime env build <env-id>` before evaluation or training.

Newer and more experimental environment classes include:

- **`GymEnv`** — universal runner for Gym-compatible environments (OpenAI Gym / Gymnasium API)
- **`CliAgentEnv`** — runs custom agent code inside sandboxes, intercepting API requests. Accepts sandbox configuration parameters including `docker_image`, `cpu_cores`, `memory_gb`, `disk_size_gb`, `gpu_count`, `gpu_type`, `timeout_minutes`, `environment_vars`, and `labels` for sandbox categorization. Also accepts retry tuning (like `max_retries`) and connection pooling (like `sandbox_client_max_workers`) parameters via `SandboxMixin`. Subclasses can override `get_sandbox_resources(state)` for per-instance resource allocation and `build_env_vars(state)` for custom environment variables (`PROTECTED_ENV_VARS` cannot be overridden). VMs are auto-enabled when `gpu_count > 0`
  - **`SandboxTimeouts`** — frozen dataclass of per-operation HTTP timeouts (seconds) applied to sandbox client calls, exported from `verifiers.envs.experimental.sandbox_mixin`. Fields (with defaults that preserve prior behavior): `read_file=10.0`, `extract=60.0`, `poll=60.0`, `mkdir=10.0`. These are request-level (httpx) timeouts, distinct from `SandboxSpec.timeout_minutes` (container lifetime) and `MultiTurnEnv.timeout_seconds` (wall-clock rollout cap). Override via the `timeouts` kwarg on `CliAgentEnv.__init__` (which flows through `SandboxMixin.init_sandbox_client`) when the sandbox gateway is slow or geographically distant:

    ```python
    from verifiers.envs.experimental.sandbox_mixin import SandboxTimeouts

    env = MyCliAgentEnv(
        dataset=dataset,
        rubric=rubric,
        timeouts=SandboxTimeouts(read_file=30.0, extract=180.0, poll=120.0),
    )
    ```
- **`ComposableEnv`** — `CliAgentEnv` subclass that separates *what to solve* (`TaskSet`) from *how to solve it* (`Harness`). Wire a task collection and an agent config together with zero subclassing. Delegates sandbox spec, instruction, setup, and env vars to the `TaskSet`; install script, run command, and system prompt to the `Harness`. Supports `install_env` for install-only environment variables, task directory upload via `TaskSet.get_upload_dirs()` joined with `Harness.upload_dir_mapping`, and harness-declared metrics collection via `Harness.metrics_path`. Scoring is owned by per-taskset rubrics
  - **`TaskSet`** / **`SandboxTaskSet`** — define task collections. `SandboxTaskSet` adds `SandboxSpec` (image, CPU, memory, GPU, timeout) per instance, a `setup(state)` hook, and `validate_instance(state)` for gold-patch validation. Key methods: `get_instruction(info)`, `get_rubric()`, `get_sandbox_spec(info)`, `get_env_vars()`, `get_upload_dirs()`. Includes `validate(n, concurrency, out_path=, max_retries=, resume=)` for streaming bulk validation (per-row JSONL, tqdm progress, resume + retry-on-`InfraError`) and `filter()`/`take()` combinators. Also accepts a `filter_fn: str | None` constructor kwarg (a Python expression string, typically a lambda, evaluating to `Callable[[dict], bool]`) that is applied to post-processed rows (`{"question", "info", "answer", ...}`) via `dataset.filter(...)` at the end of `__init__`. Evaluated with restricted builtins (`re`, `len`, `all`, `any`, `sum`, `min`, `max`, `sorted`, `set`, `frozenset`) — still `eval()` of user input, so intended for local `vf-eval` invocations (e.g. `SWEBenchTaskSet(filter_fn="lambda x: x['info']['repo'] == 'django/django'")`), not untrusted inputs
  - **`Harness`** — agent-side config dataclass: `install_script`, `install_timeout`, `run_command`, `system_prompt`, `system_prompt_path`, `instruction_path`, `log_path`, `sandbox_spec`, `skills_path`, `upload_dir_mapping`, `get_upload_dirs`, `metrics_path`, `metrics_prefix`, `metrics_key`, `metrics_keys`, `tool_names`, `environment_vars` (a `Callable[[State], dict[str, str]] | None`; called per-rollout by `ComposableEnv.build_env_vars(state)` so harnesses can compute env vars from per-rollout state — for static dicts, ignore the `state` arg and return the same mapping), `post_install_uploads` (small `{sandbox_path: content}` dict uploaded via the single-file path after `install_script` — e.g. RLM's `/usr/local/bin/git` refusal shim), `post_install_script` (shell run after those uploads land; typical use is `chmod +x`), `keep_trajectory_step` (per-step filter `(step, state, headers) -> bool`)
  - **`SandboxSpec`** — per-instance sandbox requirements: `image`, `cpu_cores`, `memory_gb`, `disk_size_gb`, `gpu_count`, `gpu_type`, `timeout_minutes`
- **`HarborEnv`** — loads Harbor-format agent benchmark tasks
- **`RLMEnv`** — implements [Recursive Language Models](https://alexzhang13.github.io/blog/2025/rlm/) for unbounded context processing via REPL-based decomposition and recursive sub-LLM calls
- **`OpenCodeEnv`** — runs [OpenCode](https://opencode.ai) CLI agents inside sandboxes with API call interception
- **`OpenCodeRLMEnv`** — extends `OpenCodeEnv` with concurrent sub-LLM handling via the [OC plugin](https://github.com/snimu/oc), routing `subagent`/`llm-subcall` requests through the interception proxy



---

# FILE: docs/evaluation.md

# Evaluation

This section explains how to run evaluations with Verifiers environments. See [Environments](environments.md) for information on building your own environments.

## Table of Contents
- [Basic Usage](#basic-usage)
- [Hosted Evaluations](#hosted-evaluations)
- [Command Reference](#command-reference)
  - [Environment Selection](#environment-selection)
  - [Model Configuration](#model-configuration)
  - [Sampling Parameters](#sampling-parameters)
  - [Evaluation Scope](#evaluation-scope)
  - [Concurrency](#concurrency)
  - [Output and Saving](#output-and-saving)
  - [Resuming Evaluations](#resuming-evaluations)
- [Environment Defaults](#environment-defaults)
- [Multi-Environment Evaluation](#multi-environment-evaluation)
  - [TOML Configuration](#toml-configuration)
  - [Ablation Sweeps](#ablation-sweeps)
  - [Configuration Precedence](#configuration-precedence)

Use `prime eval` to execute rollouts against any supported model provider and report aggregate metrics. Supported providers include OpenAI-compatible APIs (the default) and the Anthropic Messages API (via `--api-client-type anthropic_messages`).

## Basic Usage

Environments must be installed as Python packages before evaluation. From a local environment:

```bash
prime env install my-env           # installs ./environments/my_env as a package
prime eval run my-env -m openai/gpt-4.1-mini -n 10
```

`prime eval` imports the environment module using Python's import system, calls its `load_environment()` function, runs 5 examples with 3 rollouts each (the default), scores them using the environment's rubric, and prints aggregate metrics.

## Hosted Evaluations

You can also run evaluations on Prime-managed infrastructure with `prime eval run --hosted`. Hosted evaluations require an environment that has already been published to the Environments Hub, and they are useful when you want Prime to manage execution, monitor logs remotely, or run against a shared Hub environment slug instead of a local package.

```bash
prime env push my-env
prime eval run my-env --hosted
prime eval run my-env --hosted --follow
```

Hosted runs also support TOML configs:

```bash
prime eval run configs/eval/benchmark-hosted.toml --hosted
```

For the full hosted workflow and hosted-only flags such as `--follow`, `--timeout-minutes`, `--allow-sandbox-access`, and `--custom-secrets`, see the official [Hosted Evaluations](https://docs.primeintellect.ai/tutorials-environments/hosted-evaluations) guide.

## Command Reference

### Environment Selection

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `env_id_or_path` | (positional) | — | Environment ID(s) or path to TOML config |
| `--env-args` | `-a` | `{}` | JSON object passed to `load_environment()` |
| `--extra-env-kwargs` | `-x` | `{}` | JSON object passed to environment constructor |
| `--env-dir-path` | `-p` | `./environments` | Base path for saving output files |

The positional argument accepts two formats:
- **Single environment**: `gsm8k` — evaluates one environment
- **TOML config path**: `configs/eval/benchmark.toml` — evaluates multiple environments defined in the config file

Environment IDs are converted to Python module names (`my-env` → `my_env`) and imported. Modules must be installed (via `prime env install` or `uv pip install`).

The `--env-args` flag passes arguments to your `load_environment()` function:

```bash
prime eval run my-env -a '{"difficulty": "hard", "num_examples": 100}'
```

The `--extra-env-kwargs` flag passes arguments directly to the environment constructor, useful for overriding defaults like `max_turns` which may not be exposed via `load_environment()`:

```bash
prime eval run my-env -x '{"max_turns": 20}'
```

#### Executor autoscaling

Thread-pool executors are automatically sized to match the evaluation concurrency. During `prime eval run`, if `concurrency` is not explicitly provided via `--extra-env-kwargs`, it is computed from the concurrency level (`max_concurrent`, or `num_examples * rollouts_per_example` when unlimited) using `recommended_max_workers()`. This value is passed to `Environment.set_concurrency()`, which resizes both the default event-loop executor and all registered executors.

To override the automatic value:

```bash
prime eval run my-env -x '{"concurrency": 256}'
```

You can also call `set_concurrency()` directly at runtime:

```python
env.set_concurrency(256)
```

### Model Configuration

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--model` | `-m` | `openai/gpt-4.1-mini` | Model name or endpoint alias |
| `--api-base-url` | `-b` | `https://api.pinference.ai/api/v1` | API base URL |
| `--api-key-var` | `-k` | `PRIME_API_KEY` | Environment variable containing API key |
| `--api-client-type` | — | `openai_chat_completions` | Client type: `openai_chat_completions`, `openai_completions`, `openai_chat_completions_token`, or `anthropic_messages` |
| `--endpoints-path` | `-e` | `./configs/endpoints.toml` | Path to TOML endpoints registry |
| `--header` | — | — | Extra HTTP header (`Name: Value`), repeatable |
| `--header-from-state` | — | `X-Session-ID: example_id` | Per-request header whose value is read from rollout state (`Name: state_key`), repeatable |

For convenience, define model endpoints in `./configs/endpoints.toml` to avoid repeating URL and key flags.

```toml
[[endpoint]]
endpoint_id = "gpt-4.1-mini"
model = "gpt-4.1-mini"
url = "https://api.openai.com/v1"
key = "OPENAI_API_KEY"

[[endpoint]]
endpoint_id = "qwen3-235b-i"
model = "qwen/qwen3-235b-a22b-instruct-2507"
url = "https://api.pinference.ai/api/v1"
key = "PRIME_API_KEY"

[[endpoint]]
endpoint_id = "claude-sonnet"
model = "claude-sonnet-4-5-20250929"
url = "https://api.anthropic.com"
key = "ANTHROPIC_API_KEY"
api_client_type = "anthropic_messages"
```

Each endpoint entry supports an optional `api_client_type` field to select the client implementation (defaults to `"openai_chat_completions"`). Use `"anthropic_messages"` for Anthropic models when calling the Anthropic API directly.

Optional HTTP headers for inference requests use a short TOML key `headers` (inline table). The alias `extra_headers` is accepted with the same shape; do not set both on one row.

```toml
[[endpoint]]
endpoint_id = "my-proxy"
model = "gpt-4.1-mini"
url = "https://api.example/v1"
key = "OPENAI_API_KEY"
headers = { "X-Custom-Header" = "value" }
```

In `[[eval]]` TOML configs you can set extra headers as `headers = { ... }` and/or as a list `header = ["Name: Value", ...]` (same form as repeated `--header`). Merge order is: registry row, then the `headers` table, then each `header` / `--header` line, with later entries overriding the same name.

For per-request headers that need to vary per rollout (e.g. sticky DP-aware routing keyed off `example_id` or `trajectory_id`), use `headers_from_state = { "X-Name" = "state_key" }` and/or `header_from_state = ["X-Name: state_key", ...]` (same form as repeated `--header-from-state`). The value for each request is resolved at send time as `state[state_key]`. If unset, `X-Session-ID` defaults to `example_id`.

To define equivalent replicas, add multiple `[[endpoint]]` entries with the same `endpoint_id`.

Then use the alias directly:

```bash
prime eval run my-env -m qwen3-235b-i
```

If the model name is in the registry, those values are used by default, but you can override them with `--api-base-url` and/or `--api-key-var`. If the model name isn't found, the CLI flags are used (falling back to defaults when omitted).

In other words, `-m/--model` is treated as an endpoint alias lookup when present in the registry, and otherwise treated as a literal model id.

When using eval TOML configs, you can set `endpoint_id` in `[[eval]]` sections to resolve from the endpoint registry. `endpoint_id` is only supported when `endpoints_path` points to a TOML registry file.

### Sampling Parameters

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--max-tokens` | `-t` | model default | Maximum tokens to generate |
| `--temperature` | `-T` | model default | Sampling temperature |
| `--sampling-args` | `-S` | — | JSON object for additional sampling parameters |

The `--sampling-args` flag accepts any parameters supported by the model's API:

```bash
prime eval run my-env -S '{"temperature": 0.7, "top_p": 0.9}'
```

### Evaluation Scope

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--num-examples` | `-n` | 5 | Number of dataset examples to evaluate |
| `--rollouts-per-example` | `-r` | 3 | Rollouts per example (for pass@k, variance) |

Multiple rollouts per example enable metrics like pass@k and help measure variance. The total number of rollouts is `num_examples × rollouts_per_example`.

### Concurrency

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--max-concurrent` | `-c` | 32 | Maximum concurrent requests |
| `--max-concurrent-generation` | — | same as `-c` | Concurrent generation requests |
| `--max-concurrent-scoring` | — | same as `-c` | Concurrent scoring requests |
| `--no-interleave-scoring` | `-N` | false | Disable interleaved scoring |
| `--independent-scoring` | `-i` | false | Score each rollout individually instead of by group |
| `--max-retries` | — | 0 | Retries per rollout on transient `InfraError` |
| `--num-workers` | `-w` | `auto` | Number of env server worker processes (`auto` = concurrency ÷ 256, minimum 1) |

By default, scoring runs interleaved with generation. Use `--no-interleave-scoring` to score all rollouts after generation completes.

The `--max-retries` flag enables automatic retry with exponential backoff when rollouts fail due to transient infrastructure errors (e.g., sandbox timeouts, API failures).

The `--num-workers` flag controls how many worker processes the env server spawns. Each worker owns its own environment instance and runs rollouts independently. The default `auto` scales with concurrency.

### Display

When evaluating multiple environments, the display shows an overview panel at the top with a compact status line per environment, and a detail panel below with full progress, metrics, and logs for one environment at a time. Use the **left/right arrow keys** to switch between environments. The overview scrolls to keep the selected environment visible and is capped at half the terminal height.

### Output and Saving

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--verbose` | `-v` | false | Enable debug logging |
| `--fullscreen` | `-f` | false | Use alternate screen buffer (fullscreen) for the Rich display |
| `--disable-tui` | `-d` | false | Disable Rich display; use normal logging and tqdm progress |
| `--abbreviated-summary` | `-A` | false | Abbreviated summary: show settings and stats, skip example prompts |
| `--output-dir` | `-o` | — | Custom output directory for evaluation results and logs |
| `--save-results` | `-s` | false | Save results to disk |
| `--resume [PATH]` | `-R` | — | Resume from a previous run (auto-detect latest matching incomplete run if PATH omitted) |
| `--state-columns` | `-C` | — | Extra state columns to save (comma-separated) |
| `--save-to-hf-hub` | `-H` | false | Push results to Hugging Face Hub |
| `--hf-hub-dataset-name` | `-D` | — | Dataset name for HF Hub |
| `--heartbeat-url` | — | — | Heartbeat URL for uptime monitoring |

By default, results are saved to `./outputs/evals/{env_id}--{model}/{run_id}/`. Use `--output-dir` to override the base output directory — when set, results (and logs) are saved under `{output_dir}/evals/{env_id}--{model}/{run_id}/` instead. The directory contains:

- `results.jsonl` — rollout outputs, one per line
- `metadata.json` — evaluation configuration and aggregate metrics

### Resuming Evaluations

Long-running evaluations can be interrupted and resumed using checkpointing. When `--save-results` is enabled, results are saved incrementally after each completed group of rollouts. Use `--resume` to continue from where you left off. Pass a path to resume a specific run, or omit the path to auto-detect the latest incomplete matching run.

**Running with checkpoints:**

```bash
prime eval run my-env -n 1000 -s
```

With `-s` (save results) enabled, partial results are written to disk after each group completes. If the evaluation is interrupted, the output directory will contain all completed rollouts up until the interruption.

**Resuming from a checkpoint:**

```bash
prime eval run my-env -n 1000 -s --resume ./environments/my_env/outputs/evals/my-env--openai--gpt-4.1-mini/abc12345
```

When a resume path is provided, it must point to a valid evaluation results directory containing both `results.jsonl` and `metadata.json`. With `--resume` and no path, verifiers scans the environment/model output directory and picks the most recent incomplete run matching `env_id`, `model`, and `rollouts_per_example` where saved `num_examples` is less than or equal to the current run. When resuming:

1. Existing completed rollouts are loaded from the checkpoint
2. Remaining rollouts are computed based on the example ids and group size
3. Only incomplete rollouts are executed
4. New results are appended to the existing checkpoint

If all rollouts are already complete, the evaluation returns immediately with the existing results.

**Configuration compatibility:**

When resuming, the current run configuration should match the original run. Mismatches in parameters like `--model`, `--env-args`, or `--rollouts-per-example` can lead to undefined behavior. For reliable results, resume with the same configuration used to create the checkpoint, only increasing `--num-examples` if you need additional rollouts beyond the original target.

**Example workflow:**

```bash
# Start a large evaluation with checkpointing
prime eval run math-python -n 500 -r 3 -s

# If interrupted, find the run directory
ls ./environments/math_python/outputs/evals/math-python--openai--gpt-4.1-mini/

# Resume from the checkpoint
prime eval run math-python -n 500 -r 3 -s \
  --resume ./environments/math_python/outputs/evals/math-python--openai--gpt-4.1-mini/abc12345
```

The `--state-columns` flag allows saving environment-specific state fields that your environment stores during rollouts:

```bash
prime eval run my-env -s -C "judge_response,parsed_answer"
```

## Environment Defaults

Environments can specify default evaluation parameters in their `pyproject.toml` (See [Developing Environments](environments.md#developing-environments)):

```toml
[tool.verifiers.eval]
num_examples = 100
rollouts_per_example = 5
```

These defaults are used when higher-priority sources don't specify a value. The full priority order is:

1. TOML per-environment settings (when using a config file)
2. CLI flags
3. Environment defaults (from `pyproject.toml`)
4. Global defaults

See [Configuration Precedence](#configuration-precedence) for more details on multi-environment evaluation.

## Multi-Environment Evaluation

You can evaluate multiple environments using `prime eval` with a TOML configuration file. This is useful for running comprehensive benchmark suites.

### TOML Configuration

For multi-environment evals or fine-grained control over settings, use a TOML configuration file. When using a config file, CLI arguments are ignored.

```bash
prime eval run configs/eval/my-benchmark.toml
```

The TOML file uses `[[eval]]` sections to define each evaluation. You can also specify global defaults at the top:

```toml
# configs/eval/my-benchmark.toml

# Global defaults (optional)
model = "openai/gpt-4.1-mini"
num_examples = 50

[[eval]]
env_id = "gsm8k"
num_examples = 100  # overrides global default
rollouts_per_example = 5

[[eval]]
env_id = "alphabet-sort"
# Uses global num_examples (50)
rollouts_per_example = 3

[[eval]]
env_id = "math-python"
# Uses global defaults and built-in defaults for unspecified values
```

A minimal config requires only a single `[[eval]]` section:

```toml
[[eval]]
env_id = "gsm8k"
```

Each `[[eval]]` section must contain an `env_id` field. All other fields are optional:

| Field | Type | Description |
|-------|------|-------------|
| `env_id` | string | **Required.** Environment module name |
| `env_args` | table | Arguments passed to `load_environment()` |
| `num_examples` | integer | Number of dataset examples to evaluate |
| `rollouts_per_example` | integer | Rollouts per example |
| `extra_env_kwargs` | table | Arguments passed to environment constructor |
| `model` | string | Model to evaluate |
| `endpoint_id` | string | Endpoint registry id (requires TOML `endpoints_path`) |

Example with `env_args`:

```toml
[[eval]]
env_id = "math-python"
num_examples = 50

[eval.env_args]
difficulty = "hard"
split = "test"
```

### Ablation Sweeps

Use `[[ablation]]` blocks to automatically generate eval configs from a cartesian product of parameter values. This is useful for hyperparameter sweeps and ablation studies without manually writing each combination.

```toml
# Global defaults apply to all evals and ablations
model = "openai/gpt-4.1-mini"
num_examples = 50

# Sweep temperature × difficulty → 6 eval configs
# split is fixed across all combinations
[[ablation]]
env_id = "my-env"
env_args = {split = "test"}

[ablation.sweep]
temperature = [0.0, 0.5, 1.0]

[ablation.sweep.env_args]
difficulty = ["easy", "hard"]
```

- **Fixed fields** in the `[[ablation]]` block (like `env_id`) apply to all expanded configs
- **`[ablation.sweep]`** keys are lists of values crossed as a cartesian product
- **`[ablation.sweep.env_args]`** keys are swept and merged into the `env_args` dict
- **Fixed `env_args`** can be set alongside swept ones (e.g. `env_args = {split = "test"}` keeps `split` fixed while sweeping other env args). The same key cannot appear in both fixed and swept env_args.
- Multiple `[[ablation]]` blocks are independent (no cross-product between blocks)
- `[[ablation]]` and `[[eval]]` blocks can coexist in the same config file
- `env_id` can be a fixed field or a sweep key (e.g. `env_id = ["env-a", "env-b"]`), but note that all swept envs must accept the same `env_args` — use separate `[[ablation]]` blocks for envs with different argument schemas

Use `--abbreviated-summary` (`-A`) to get a compact summary focused on settings and stats, which is useful when comparing many ablation runs.

### Configuration Precedence

When using a **config file**, CLI arguments are ignored. Settings are resolved as:

1. **TOML per-eval settings** — Values specified in `[[eval]]` sections
2. **TOML global settings** — Values at the top of the config file
3. **Environment defaults** — Values from the environment's `pyproject.toml`
4. **Built-in defaults** — (`num_examples=5`, `rollouts_per_example=3`)

When using **CLI only** (no config file), settings are resolved as:

1. **CLI arguments** — Flags passed on the command line
2. **Environment defaults** — Values from the environment's `pyproject.toml`
3. **Built-in defaults** — (`num_examples=5`, `rollouts_per_example=3`)



---

# FILE: docs/faqs.md

# FAQs

## Getting Started

### How do I quickly test my environment?

Use `prime eval run` with a small sample:

```bash
prime eval run my-environment -m openai/gpt-4.1-mini -n 5
```

The `-s` flag prints sample outputs so you can see what's happening.

### How do I see what the model is outputting?

**If using `prime eval run`**: Results are saved automatically. Browse them interactively with:

```bash
prime eval tui
```
The TUI opens a single run browser (`environment -> model -> run`). Press `Enter` on a run to open rollout details, `b` to go back, `tab` to cycle panes, `e` and `x` to expand or collapse history, `pageup` and `pagedown` to scroll history, and `c` for Copy Mode.

**If using the Python API** (`env.generate()` / `env.evaluate()`):

```python
vf.print_prompt_completions_sample(outputs, n=3)
```

### How do I enable debug logging?

Set the `VF_LOG_LEVEL` environment variable:

```bash
VF_LOG_LEVEL=DEBUG prime eval run my-environment -m openai/gpt-4.1-mini -n 5
```

## Environments

### Which environment class should I use?

- **SingleTurnEnv**: One prompt, one response (Q&A, classification)
- **MultiTurnEnv**: Custom back-and-forth interaction (games, simulations)
- **ToolEnv**: Model calls Python functions (search, calculator)
- **StatefulToolEnv**: Tools that need per-rollout state (sandbox IDs, sessions)

### What does `max_turns=-1` mean?

Unlimited turns. The rollout continues until a stop condition is triggered (e.g., model stops calling tools, or a custom condition you define).

### How do I add a custom stop condition?

Use the `@vf.stop` decorator on a method that returns `True` to end the rollout:

```python
@vf.stop
async def task_completed(self, state: State) -> bool:
    return "DONE" in state["completion"][-1]["content"]
```

### How do I handle tool call errors gracefully?

In `ToolEnv`, customize error handling:

```python
env = ToolEnv(
    tools=[my_tool],
    error_formatter=lambda e: f"Error: {type(e).__name__}: {e}",
    stop_errors=[CriticalError],  # These errors end the rollout
)
```

Non-critical errors are returned to the model as tool responses so it can retry.

## Reward Functions

### What arguments can my reward function receive?

Reward functions receive any of these via `**kwargs`:

- `completion` - the model's response
- `answer` - ground truth from dataset
- `prompt` - the input prompt
- `state` - full rollout state
- `parser` - the rubric's parser (if set)
- `task` - task identifier
- `info` - metadata dict from dataset

Just include the ones you need in your function signature.

### How do group reward functions work?

Group reward functions receive plural arguments (`completions`, `answers`, `states`) and return a list of floats. They're detected automatically by parameter names:

```python
def relative_reward(completions: list, answers: list, **kwargs) -> list[float]:
    # Score all completions for an example together
    scores = [compute_score(c, a) for c, a in zip(completions, answers)]
    # Normalize relative to group
    max_score = max(scores) if scores else 1.0
    return [s / max_score for s in scores]
```

## Training

### How do I use a local vLLM server?

Point the client to your local server:

```python
from openai import AsyncOpenAI

client = AsyncOpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"
)

outputs = await env.evaluate(client, model="your-model-name", ...)
```



---

# FILE: docs/mint.json

{
  "$schema": "https://mintlify.com/docs.json",
  "navigation": [
    {
      "group": "Verifiers",
      "pages": [
        "overview",
        "environments",
        "evaluation",
        "training",
        "development",
        "reference",
        "faqs"
      ]
    }
  ]
}


---

# FILE: docs/overview.md

# Overview

Verifiers is our library for creating environments to train and evaluate LLMs.

Environments contain everything required to run and evaluate a model on a particular task:
- A *dataset* of task inputs
- A *harness* for the model (tools, sandboxes, context management, etc.)
- A reward function or *rubric* to score the model's performance

Environments can be used for training models with reinforcement learning (RL), evaluating capabilities, generating synthetic data, experimenting with agent harnesses, and more. 

Verifiers is tightly integrated with the [Environments Hub](https://app.primeintellect.ai/dashboard/environments?ex_sort=most_stars), as well as our training framework [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) and our [Hosted Training](https://app.primeintellect.ai/dashboard/training) platform.

## Getting Started

Ensure you have `uv` installed, as well as the `prime` [CLI](https://docs.primeintellect.ai/cli-reference/introduction) tool:
```bash
# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
# install the prime CLI
uv tool install prime
# log in to the Prime Intellect platform
prime login
```
To set up a new workspace for developing environments, do:
```bash
# ~/dev/my-lab
prime lab setup 
```

This sets up a Python project if needed (with `uv init`), installs `verifiers` (with `uv add verifiers`), creates the recommended workspace structure, and downloads useful starter files:
```
configs/
├── endpoints.toml      # OpenAI-compatible API endpoint configuration
├── rl/                 # Example configs for Hosted Training
├── eval/               # Example multi-environment eval configs
└── gepa/               # Example configs for prompt optimization
.prime/
└── skills/             # Bundled workflow skills for create/browse/review/eval/GEPA/train/brainstorm
environments/
└── AGENTS.md           # Documentation for AI coding agents
AGENTS.md               # Top-level documentation for AI coding agents
CLAUDE.md               # Claude-specific pointer to AGENTS.md
```

Alternatively, add `verifiers` to an existing project:
```bash
uv add verifiers && prime lab setup --skip-install
```

Environments built with Verifiers are self-contained Python modules. To initialize a fresh environment template, do:
```bash
prime env init my-env # creates a new template in ./environments/my_env
```

This will create a new module called `my_env` with a basic environment template.
```
environments/my_env/
├── my_env.py           # Main implementation
├── pyproject.toml      # Dependencies and metadata
└── README.md           # Documentation
```

Environment modules should expose a `load_environment` function which returns an instance of the Environment object, and which can accept custom arguments. For example: 
```python
# my_env.py
import verifiers as vf

def load_environment(dataset_name: str = 'gsm8k') -> vf.Environment:
    dataset = vf.load_example_dataset(dataset_name) # 'question'
    async def correct_answer(completion, answer) -> float:
        completion_ans = completion[-1]['content']
        return 1.0 if completion_ans == answer else 0.0
    rubric = Rubric(funcs=[correct_answer])
    env = vf.SingleTurnEnv(dataset=dataset, rubric=rubric)
    return env
```

To install the environment module into your project, do:
```bash
prime env install my-env # installs from ./environments/my_env
```

To install an environment from the Environments Hub into your project, do:
```bash
prime env install primeintellect/math-python
```

To run a local evaluation with any OpenAI-compatible model, do:
```bash
prime eval run my-env -m openai/gpt-5-nano # run and save eval results locally
```
Evaluations use [Prime Inference](https://docs.primeintellect.ai/inference/overview) by default; configure your own API endpoints in `./configs/endpoints.toml`.

View local evaluation results in the terminal UI:
```bash
prime eval tui
```
The TUI opens a single run browser (`environment -> model -> run`). Press `Enter` on a run to open rollout details, `b` to go back, `tab` to cycle panes, `e` and `x` to expand or collapse history, `pageup` and `pagedown` to scroll history, and `c` for Copy Mode.

To publish the environment to the [Environments Hub](https://app.primeintellect.ai/dashboard/environments?ex_sort=most_stars), do:
```bash
prime env push my-env # equivalent to --path ./environments/my_env
```

To run an evaluation directly from the Environments Hub, do:
```bash
prime eval run primeintellect/math-python
```

## Documentation

**[Environments](environments.md)** — Create datasets, rubrics, and custom multi-turn interaction protocols.

**[Evaluation](evaluation.md)** - Evaluate models using your environments.

**[Training](training.md)** — Train models in your environments with reinforcement learning.

**[Development](development.md)** — Contributing to verifiers

**[API Reference](reference.md)** — Understanding the API and data structures

**[FAQs](faqs.md)** - Other frequently asked questions.



---

# FILE: docs/reference.md

# API Reference

## Table of Contents

- [Type Aliases](#type-aliases)
- [Data Types](#data-types)
- [Classes](#classes)
  - [Environment Classes](#environment-classes)
  - [Parser Classes](#parser-classes)
  - [Rubric Classes](#rubric-classes)
- [Client Classes](#client-classes)
- [Configuration Types](#configuration-types)
- [Prime CLI Plugin](#prime-cli-plugin)
- [Decorators](#decorators)
- [Utility Functions](#utility-functions)

---

## Type Aliases

### Messages

```python
Messages = str | list[ChatMessage]
```

The primary message type. Either a plain string (completion mode) or a list of chat messages (chat mode).

### ChatMessage

```python
ChatMessage = ChatCompletionMessageParam  # from openai.types.chat
```

OpenAI's chat message type with `role`, `content`, and optional `tool_calls` / `tool_call_id` fields.

### Info

```python
Info = dict[str, Any]
```

Arbitrary metadata dictionary from dataset rows.

### SamplingArgs

```python
SamplingArgs = dict[str, Any]
```

Generation parameters passed to the inference server (e.g., `temperature`, `top_p`, `max_tokens`).

### RewardFunc

```python
IndividualRewardFunc = Callable[..., float | Awaitable[float]]
GroupRewardFunc = Callable[..., list[float] | Awaitable[list[float]]]
RewardFunc = IndividualRewardFunc | GroupRewardFunc
```

Individual reward functions operate on single rollouts. Group reward functions operate on all rollouts for an example together (useful for relative scoring).

### ClientType

```python
ClientType = Literal[
    "openai_completions",
    "openai_chat_completions",
    "openai_chat_completions_token",
    "anthropic_messages",
]
```

Selects which `Client` implementation to use. Set via `ClientConfig.client_type`.

---

## Data Types

### State

```python
class State(dict):
    INPUT_FIELDS = ["prompt", "answer", "task", "info", "example_id"]
```

A `dict` subclass that tracks rollout information. Accessing keys in `INPUT_FIELDS` automatically forwards to the nested `input` object.

**Fields set during initialization:**

| Field | Type | Description |
|-------|------|-------------|
| `input` | `RolloutInput` | Nested input data |
| `client` | `Client` | Client instance |
| `model` | `str` | Model name |
| `sampling_args` | `SamplingArgs \| None` | Generation parameters |
| `is_completed` | `bool` | Whether rollout has ended |
| `is_truncated` | `bool` | Whether generation was truncated |
| `tool_defs` | `list[Tool] \| None` | Available tool definitions |
| `trajectory` | `list[TrajectoryStep]` | Multi-turn trajectory |
| `trajectory_id` | `str` | UUID for this rollout |
| `timing` | `RolloutTiming` | Timing information |

**Fields set after scoring:**

| Field | Type | Description |
|-------|------|-------------|
| `completion` | `Messages \| None` | Final completion |
| `reward` | `float \| None` | Final reward |
| `advantage` | `float \| None` | Advantage over group mean |
| `metrics` | `dict[str, float] \| None` | Per-function metrics |
| `stop_condition` | `str \| None` | Name of triggered stop condition |
| `error` | `Error \| None` | Error if rollout failed |

### RolloutInput

```python
class RolloutInput(TypedDict):
    prompt: Messages        # Required
    example_id: int         # Required
    task: str               # Required
    answer: str             # Optional
    info: Info              # Optional
```

### RolloutOutput

```python
class RolloutOutput(dict):
    # Required fields
    example_id: int
    task: str
    prompt: Messages | None
    completion: Messages | None
    reward: float
    timing: RolloutTiming
    is_completed: bool
    is_truncated: bool
    metrics: dict[str, float]
    # Optional fields
    answer: str
    info: Info
    error: str | None
    stop_condition: str | None
    token_usage: TokenUsage
    trajectory: list[TrajectoryStep]
    tool_defs: list[Tool] | None
```

Serialized output from a rollout. This is a `dict` subclass that provides typed access to known fields while supporting arbitrary additional fields from `state_columns`. All values must be JSON-serializable. Used in `GenerateOutputs` and for saving results to disk.

### TrajectoryStep

```python
class TrajectoryStep(TypedDict):
    prompt: Messages
    completion: Messages
    response: Response
    tokens: TrajectoryStepTokens | None
    reward: float | None
    advantage: float | None
    is_truncated: bool
    trajectory_id: str
    extras: dict[str, Any]
```

A single turn in a multi-turn rollout.

### TrajectoryStepTokens

```python
class TrajectoryStepTokens(TypedDict):
    prompt_ids: list[int]
    prompt_mask: list[int]
    completion_ids: list[int]
    completion_mask: list[int]
    completion_logprobs: list[float]
    overlong_prompt: bool
    is_truncated: bool
    routed_experts: list[list[list[int]]] | None  # [seq_len, layers, topk] to enable router replay
```

Token-level data for training.

### RolloutTiming

```python
class RolloutTiming(TypedDict, total=False):
    start_time: float
    generation_ms: float
    scoring_ms: float
    total_ms: float
```

### TokenUsage

```python
class TokenUsage(TypedDict, total=False):
    input_tokens: float
    output_tokens: float
    final_input_tokens: float
    final_output_tokens: float
```

| Field | Description |
|-------|-------------|
| `input_tokens` | Sum of prompt tokens across all turns. Shared context is counted each time it appears in a prompt. |
| `output_tokens` | Sum of completion tokens across all turns. |
| `final_input_tokens` | Non-completion tokens in the final turn's context (system prompts, user messages, tool results, etc.). |
| `final_output_tokens` | Completion tokens in the final turn's context. Equals `output_tokens` for single-turn rollouts. |

In a single-turn rollout, `input_tokens == final_input_tokens` and `output_tokens == final_output_tokens`. In a multi-turn rollout, `input_tokens > final_input_tokens` because earlier turns' prompts are counted again.

The `final_*` metrics assume a single, continuously extended trajectory. Non-linear trajectories (multi-agent, context summarization, history rewriting) are not accounted for.

### GenerateOutputs

```python
class GenerateOutputs(TypedDict):
    outputs: list[RolloutOutput]
    metadata: GenerateMetadata
```

Output from `Environment.generate()`. Contains a list of `RolloutOutput` objects (one per rollout) and generation metadata. Each `RolloutOutput` is a serialized, JSON-compatible dict containing the rollout's prompt, completion, answer, reward, metrics, timing, and other per-rollout data.

### GenerateMetadata

```python
class VersionInfo(TypedDict):
    vf_version: str
    vf_commit: str | None
    env_version: str | None
    env_commit: str | None

class GenerateMetadata(TypedDict):
    env_id: str
    env_args: dict
    model: str
    base_url: str
    num_examples: int
    rollouts_per_example: int
    sampling_args: SamplingArgs
    date: str
    time_ms: float
    avg_reward: float
    avg_metrics: dict[str, float]
    avg_error: float
    pass_at_k: dict[str, float]
    pass_all_k: dict[str, float]
    pass_threshold: float
    usage: TokenUsage | None
    version_info: VersionInfo
    state_columns: list[str]
    path_to_save: Path
    tools: list[Tool] | None
```

`base_url` is always serialized as a string. For multi-endpoint runs (e.g., using `ClientConfig.endpoint_configs`), it is stored as a comma-separated list of URLs.

`version_info` captures the verifiers framework version/commit and the environment package version/commit at generation time. Populated automatically by `GenerateOutputsBuilder`.

### RolloutScore / RolloutScores

```python
class RolloutScore(TypedDict):
    reward: float
    metrics: dict[str, float]

class RolloutScores(TypedDict):
    reward: list[float]
    metrics: dict[str, list[float]]
```

---

## Classes

### Environment Classes

#### Environment

```python
class Environment(ABC):
    def __init__(
        self,
        dataset: Dataset | None = None,
        eval_dataset: Dataset | None = None,
        system_prompt: str | None = None,
        few_shot: list[ChatMessage] | None = None,
        parser: Parser | None = None,
        rubric: Rubric | None = None,
        sampling_args: SamplingArgs | None = None,
        message_type: MessageType = "chat",
        max_workers: int = 512,
        env_id: str | None = None,
        env_args: dict | None = None,
        max_seq_len: int | None = None,
        score_rollouts: bool = True,
        pass_threshold: float = 0.5,
        **kwargs,
    ): ...
```

Abstract base class for all environments.

**Generation methods:**

| Method | Returns | Description |
|--------|---------|-------------|
| `generate(inputs, client, model, ...)` | `GenerateOutputs` | Run rollouts asynchronously. `client` accepts `Client \| ClientConfig`. |
| `generate_sync(inputs, client, ...)` | `GenerateOutputs` | Synchronous wrapper |
| `evaluate(client, model, ...)` | `GenerateOutputs` | Evaluate on eval_dataset |
| `evaluate_sync(client, model, ...)` | `GenerateOutputs` | Synchronous evaluation |

**Dataset methods:**

| Method | Returns | Description |
|--------|---------|-------------|
| `get_dataset(n=-1, seed=None)` | `Dataset` | Get training dataset (optionally first n, shuffled) |
| `get_eval_dataset(n=-1, seed=None)` | `Dataset` | Get evaluation dataset |
| `make_dataset(...)` | `Dataset` | Static method to create dataset from inputs |

**Rollout methods (used internally or by subclasses):**

| Method | Returns | Description |
|--------|---------|-------------|
| `rollout(input, client, model, sampling_args)` | `State` | Abstract: run single rollout |
| `init_state(input, client, model, sampling_args)` | `State` | Create initial state from input |
| `get_model_response(state, prompt, ...)` | `Response` | Get model response for prompt |
| `is_completed(state)` | `bool` | Check all stop conditions |
| `run_rollout(sem, input, client, model, sampling_args)` | `State` | Run rollout with semaphore |
| `run_group(group_inputs, client, model, ...)` | `list[State]` | Generate and score one group |

**Configuration methods:**

| Method | Description |
|--------|-------------|
| `set_kwargs(**kwargs)` | Set attributes using setter methods when available |
| `set_concurrency(concurrency)` | Set `concurrency` and scale all registered thread-pool executors to match |
| `add_rubric(rubric)` | Add or merge rubric |
| `set_max_seq_len(max_seq_len)` | Set maximum sequence length |
| `set_score_rollouts(bool)` | Enable/disable scoring |

#### SingleTurnEnv

Single-response Q&A tasks. Inherits from `Environment`.

#### MultiTurnEnv

```python
class MultiTurnEnv(Environment):
    def __init__(self, max_turns: int = -1, **kwargs): ...
```

Multi-turn interactions. Subclasses must implement `env_response`.

**Abstract method:**

```python
async def env_response(self, messages: Messages, state: State, **kwargs) -> Messages:
    """Generate environment feedback after model turn."""
```

**Built-in stop conditions:** `has_error`, `prompt_too_long`, `max_turns_reached`, `max_total_completion_tokens_reached`, `has_final_env_response`

**Hooks:**

| Method | Description |
|--------|-------------|
| `setup_state(state)` | Initialize per-rollout state |
| `get_prompt_messages(state)` | Customize prompt construction |
| `render_completion(state)` | Customize completion rendering |
| `add_trajectory_step(state, step)` | Customize trajectory handling |
| `set_max_total_completion_tokens(int)` | Set maximum total completion tokens |

#### ToolEnv

```python
class ToolEnv(MultiTurnEnv):
    def __init__(
        self,
        tools: list[Callable] | None = None,
        max_turns: int = 10,
        error_formatter: Callable[[Exception], str] = lambda e: f"{e}",
        stop_errors: list[type[Exception]] | None = None,
        **kwargs,
    ): ...
```

Tool calling with stateless Python functions. Automatically converts functions to OpenAI tool format.

**Built-in stop condition:** `no_tools_called` (ends when model responds without tool calls)

**Methods:**

| Method | Description |
|--------|-------------|
| `add_tool(tool)` | Add a tool at runtime |
| `remove_tool(tool)` | Remove a tool at runtime |
| `call_tool(name, args, id)` | Override to customize tool execution |

#### StatefulToolEnv

Tools requiring per-rollout state. Override `setup_state` and `update_tool_args` to inject state.

#### SandboxEnv

```python
class SandboxEnv(StatefulToolEnv):
    def __init__(
        self,
        sandbox_name: str = "sandbox-env",
        docker_image: str = "python:3.11-slim",
        start_command: str = "tail -f /dev/null",
        cpu_cores: int = 1,
        memory_gb: int = 2,
        disk_size_gb: int = 5,
        gpu_count: int = 0,
        timeout_minutes: int = 60,
        timeout_per_command_seconds: int = 30,
        environment_vars: dict[str, str] | None = None,
        team_id: str | None = None,
        advanced_configs: AdvancedConfigs | None = None,
        labels: list[str] | None = None,
        **kwargs,
    ): ...
```

Sandboxed container execution using `prime` sandboxes.

**Key parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `sandbox_name` | `str` | Name prefix for sandbox instances |
| `docker_image` | `str` | Docker image to use for the sandbox |
| `cpu_cores` | `int` | Number of CPU cores |
| `memory_gb` | `int` | Memory allocation in GB |
| `disk_size_gb` | `int` | Disk size in GB |
| `gpu_count` | `int` | Number of GPUs |
| `timeout_minutes` | `int` | Sandbox timeout in minutes |
| `timeout_per_command_seconds` | `int` | Per-command execution timeout |
| `environment_vars` | `dict[str, str] \| None` | Environment variables to set in sandbox |
| `labels` | `list[str] \| None` | Labels for sandbox categorization and filtering |

#### PythonEnv

Persistent Python REPL in sandbox. Extends `SandboxEnv`.

#### OpenEnvEnv

```python
class OpenEnvEnv(MultiTurnEnv):
    def __init__(
        self,
        openenv_project: str | Path,
        num_train_examples: int = 100,
        num_eval_examples: int = 50,
        seed: int = 0,
        prompt_renderer: Callable[..., ChatMessages] | None = None,
        max_turns: int = -1,
        rubric: Rubric | None = None,
        **kwargs,
    ): ...
```

OpenEnv integration that runs OpenEnv projects in Prime Sandboxes using a prebuilt image manifest (`.build.json`), supports both gym and MCP contracts, and requires a `prompt_renderer` to convert observations into chat messages.

#### EnvGroup

```python
env_group = vf.EnvGroup(
    envs=[env1, env2, env3],
    names=["math", "code", "qa"]  # optional
)
```

Combines multiple environments for mixed-task training.

---

### Parser Classes

#### Parser

```python
class Parser:
    def __init__(self, extract_fn: Callable[[str], str] = lambda x: x): ...
    
    def parse(self, text: str) -> Any: ...
    def parse_answer(self, completion: Messages) -> str | None: ...
    def get_format_reward_func(self) -> Callable: ...
```

Base parser. Default behavior returns text as-is.

#### XMLParser

```python
class XMLParser(Parser):
    def __init__(
        self,
        fields: list[str | tuple[str, ...]],
        answer_field: str = "answer",
        extract_fn: Callable[[str], str] = lambda x: x,
    ): ...
```

Extracts structured fields from XML-tagged output.

```python
parser = vf.XMLParser(fields=["reasoning", "answer"])
# Parses: <reasoning>...</reasoning><answer>...</answer>

# With alternatives:
parser = vf.XMLParser(fields=["reasoning", ("code", "answer")])
# Accepts either <code> or <answer> for second field
```

**Methods:**

| Method | Returns | Description |
|--------|---------|-------------|
| `parse(text)` | `SimpleNamespace` | Parse XML into object with field attributes |
| `parse_answer(completion)` | `str \| None` | Extract answer field from completion |
| `get_format_str()` | `str` | Get format description string |
| `get_fields()` | `list[str]` | Get canonical field names |
| `format(**kwargs)` | `str` | Format kwargs into XML string |

#### ThinkParser

```python
class ThinkParser(Parser):
    def __init__(self, extract_fn: Callable[[str], str] = lambda x: x): ...
```

Extracts content after `</think>` tag. For models that always include `<think>` tags but don't parse them automatically.

#### MaybeThinkParser

Handles optional `<think>` tags (for models that may or may not think).

---

### Rubric Classes

#### Rubric

```python
class Rubric:
    def __init__(
        self,
        funcs: list[RewardFunc] | None = None,
        weights: list[float] | None = None,
        parser: Parser | None = None,
    ): ...
```

Combines multiple reward functions with weights. Default weight is `1.0`. Functions with `weight=0.0` are tracked as metrics only.

**Methods:**

| Method | Description |
|--------|-------------|
| `add_reward_func(func, weight=1.0)` | Add a reward function |
| `add_metric(func, weight=0.0)` | Add a metric (no reward contribution) |
| `add_class_object(name, obj)` | Add object accessible in reward functions |

**Reward function signature:**

```python
def my_reward(
    completion: Messages,
    answer: str = "",
    prompt: Messages | None = None,
    state: State | None = None,
    parser: Parser | None = None,  # if rubric has parser
    task: str = "",
    info: Info | None = None,
    **kwargs
) -> float:
    ...
```

**Group reward function signature:**

```python
def my_group_reward(
    completions: list[Messages],
    answers: list[str],
    states: list[State],
    # ... plural versions of individual args
    **kwargs
) -> list[float]:
    ...
```

#### JudgeRubric

LLM-as-judge evaluation.

#### MathRubric

Math-specific evaluation using `math-verify`.

#### RubricGroup

Combines rubrics for `EnvGroup`.

---

## Client Classes

### Client

```python
class Client(ABC, Generic[ClientT, MessagesT, ResponseT, ToolT]):
    def __init__(self, client_or_config: ClientT | ClientConfig) -> None: ...

    @property
    def client(self) -> ClientT: ...

    async def get_response(
        self,
        prompt: Messages,
        model: str,
        sampling_args: SamplingArgs,
        tools: list[Tool] | None = None,
        **kwargs,
    ) -> Response: ...

    async def close(self) -> None: ...
```

Abstract base class for all model clients. Wraps a provider-specific SDK client and translates between provider-agnostic `vf` types (`Messages`, `Tool`, `Response`) and provider-native formats. The `client` property exposes the underlying SDK client (e.g., `AsyncOpenAI`, `AsyncAnthropic`).

`get_response()` is the main public method — it converts the prompt and tools to the native format, calls the provider API, validates the response, and converts it back to a `vf.Response`. Errors are wrapped in `vf.ModelError` unless they are already `vf.Error` or authentication errors.

**Abstract methods (for subclass implementors):**

| Method | Description |
|--------|-------------|
| `setup_client(config)` | Create the native SDK client from `ClientConfig` |
| `to_native_prompt(messages)` | Convert `Messages` → native prompt format + extra kwargs |
| `to_native_tool(tool)` | Convert `Tool` → native tool format |
| `get_native_response(prompt, model, ...)` | Call the provider API |
| `raise_from_native_response(response)` | Raise `ModelError` for invalid responses |
| `from_native_response(response)` | Convert native response → `vf.Response` |
| `close()` | Close the underlying SDK client |

### Built-in Client Implementations

| Class | `client_type` | SDK Client | Description |
|-------|---------------|------------|-------------|
| `OpenAIChatCompletionsClient` | `"openai_chat_completions"` | `AsyncOpenAI` | Chat Completions API (default) |
| `OpenAICompletionsClient` | `"openai_completions"` | `AsyncOpenAI` | Legacy Completions API |
| `OpenAIChatCompletionsTokenClient` | `"openai_chat_completions_token"` | `AsyncOpenAI` | Custom vLLM token route |
| `AnthropicMessagesClient` | `"anthropic_messages"` | `AsyncAnthropic` | Anthropic Messages API |

All built-in clients are available as `vf.OpenAIChatCompletionsClient`, `vf.AnthropicMessagesClient`, etc.

### Response

```python
class Response(BaseModel):
    id: str
    created: int
    model: str
    usage: Usage | None
    message: ResponseMessage

class ResponseMessage(BaseModel):
    content: str | None
    reasoning_content: str | None
    finish_reason: Literal["stop", "length", "tool_calls"] | None
    is_truncated: bool | None
    tokens: ResponseTokens | None
    tool_calls: list[ToolCall] | None
```

Provider-agnostic model response. All `Client` implementations return `Response` from `get_response()`.

### Tool

```python
class Tool(BaseModel):
    name: str
    description: str
    parameters: dict[str, object]
    strict: bool | None = None
```

Provider-agnostic tool definition. Environments define tools using this type; each `Client` converts them to its native format via `to_native_tool()`.

---

## Configuration Types

### ClientConfig

```python
class ClientConfig(BaseModel):
    client_idx: int = 0
    client_type: ClientType = "openai_chat_completions"
    api_key_var: str = "PRIME_API_KEY"
    api_base_url: str = "https://api.pinference.ai/api/v1"
    endpoint_configs: list[EndpointClientConfig] = []
    timeout: float = 3600.0
    connect_timeout: float = 5.0
    max_connections: int = 28000
    max_keepalive_connections: int = 28000
    max_retries: int = 10
    extra_headers: dict[str, str] = {}
    extra_headers_from_state: dict[str, str] = {}
```

`extra_headers_from_state` maps HTTP header names to state field names. For each inference request, the header value is dynamically read from the rollout state dict. For example, `{"X-Session-ID": "example_id"}` adds a `X-Session-ID` header with the value of `state["example_id"]`, enabling sticky routing at the inference router level.

`client_type` selects which `Client` implementation to instantiate (see [Client Classes](#client-classes)). Use `endpoint_configs` for multi-endpoint round-robin. In grouped scoring mode, groups are distributed round-robin across endpoint configs.

When `api_key_var` is `"PRIME_API_KEY"` (the default), credentials are loaded with the following precedence:
- **API key**: `PRIME_API_KEY` env var > `~/.prime/config.json` > `"EMPTY"`
- **Team ID**: `PRIME_TEAM_ID` env var > `~/.prime/config.json` > not set

This allows seamless use after running `prime login`.

### EndpointClientConfig

```python
class EndpointClientConfig(BaseModel):
    client_idx: int = 0
    api_key_var: str = "PRIME_API_KEY"
    api_base_url: str = "https://api.pinference.ai/api/v1"
    timeout: float = 3600.0
    max_connections: int = 28000
    max_keepalive_connections: int = 28000
    max_retries: int = 10
    extra_headers: dict[str, str] = {}
```

Leaf endpoint configuration used inside `ClientConfig.endpoint_configs`. Has the same fields as `ClientConfig` except `endpoint_configs` itself, preventing recursive nesting.

### EvalConfig

```python
class EvalConfig(BaseModel):
    env_id: str
    env_args: dict
    env_dir_path: str
    endpoint_id: str | None = None
    model: str
    client_config: ClientConfig
    sampling_args: SamplingArgs
    num_examples: int
    rollouts_per_example: int
    max_concurrent: int
    independent_scoring: bool = False
    extra_env_kwargs: dict = {}
    max_retries: int = 0
    verbose: bool = False
    state_columns: list[str] | None = None
    save_results: bool = False
    resume_path: Path | None = None
    save_to_hf_hub: bool = False
    hf_hub_dataset_name: str | None = None
```

### Endpoint

```python
Endpoint = TypedDict(
    "Endpoint",
    {
        "key": str,
        "url": str,
        "model": str,
        "api_client_type": NotRequired[ClientType],
        "extra_headers": NotRequired[dict[str, str]],
    },
)
Endpoints = dict[str, list[Endpoint]]
```

`Endpoints` maps an endpoint id to one or more endpoint variants. A single variant is represented as a one-item list.

---

## Prime CLI Plugin

Verifiers exposes a plugin contract consumed by `prime` for command execution.

### PRIME_PLUGIN_API_VERSION

```python
PRIME_PLUGIN_API_VERSION = 1
```

API version for compatibility checks between `prime` and `verifiers`.

### PrimeCLIPlugin

```python
@dataclass(frozen=True)
class PrimeCLIPlugin:
    api_version: int = PRIME_PLUGIN_API_VERSION
    eval_module: str = "verifiers.cli.commands.eval"
    gepa_module: str = "verifiers.cli.commands.gepa"
    install_module: str = "verifiers.cli.commands.install"
    init_module: str = "verifiers.cli.commands.init"
    setup_module: str = "verifiers.cli.commands.setup"
    build_module: str = "verifiers.cli.commands.build"

    def build_module_command(
        self, module_name: str, args: Sequence[str] | None = None
    ) -> list[str]:
        ...
```

`build_module_command` returns a subprocess command list for `python -m <module> ...`.

### get_plugin

```python
def get_plugin() -> PrimeCLIPlugin:
    ...
```

Returns the plugin instance consumed by `prime`.

---

## Decorators

### @vf.stop

```python
@vf.stop
async def my_condition(self, state: State) -> bool:
    """Return True to end the rollout."""
    ...

@vf.stop(priority=10)  # Higher priority runs first
async def early_check(self, state: State) -> bool:
    ...
```

Mark a method as a stop condition. All stop conditions are checked by `is_completed()`.

### @vf.cleanup

```python
@vf.cleanup
async def my_cleanup(self, state: State) -> None:
    """Called after each rollout completes."""
    ...

@vf.cleanup(priority=10)
async def early_cleanup(self, state: State) -> None:
    ...
```

Mark a method as a rollout cleanup handler. Cleanup methods should be **idempotent**—safe to call multiple times—and handle errors gracefully to ensure cleanup completes even when resources are in unexpected states.

### @vf.teardown

```python
@vf.teardown
async def my_teardown(self) -> None:
    """Called when environment is destroyed."""
    ...

@vf.teardown(priority=10)
async def early_teardown(self) -> None:
    ...
```

Mark a method as an environment teardown handler.

---

## Utility Functions

### Data Utilities

```python
vf.load_example_dataset(name: str) -> Dataset
```

Load a built-in example dataset.

```python
vf.extract_boxed_answer(text: str, strict: bool = False) -> str
```

Extract answer from LaTeX `\boxed{}` format. When `strict=True`, returns `""` if no `\boxed{}` is found (used by `MathRubric` to avoid scoring unformatted responses). When `strict=False` (default), returns the original text as a passthrough.

```python
vf.extract_hash_answer(text: str) -> str | None
```

Extract answer after `####` marker (GSM8K format).

### Environment Utilities

```python
vf.load_environment(env_id: str, **kwargs) -> Environment
```

Load an environment by ID (e.g., `"primeintellect/gsm8k"`).

### Configuration Utilities

```python
vf.ensure_keys(keys: list[str]) -> None
```

Validate that required environment variables are set. Raises `MissingKeyError` (a `ValueError` subclass) with a clear message listing all missing keys and instructions for setting them.

```python
class MissingKeyError(ValueError):
    keys: list[str]  # list of missing key names
```

Example:

```python
def load_environment(api_key_var: str = "OPENAI_API_KEY") -> vf.Environment:
    vf.ensure_keys([api_key_var])
    # now safe to use os.environ[api_key_var]
    ...
```

### Logging Utilities

```python
vf.print_prompt_completions_sample(outputs: GenerateOutputs, n: int = 3)
```

Pretty-print sample rollouts.

```python
vf.setup_logging(level: str = "INFO")
```

Configure verifiers logging. Set `VF_LOG_LEVEL` env var to change default.

```python
vf.log_level(level: str | int)
```

Context manager to temporarily set the verifiers logger to a new log level. Useful for temporarily adjusting verbosity during specific operations.

```python
with vf.log_level("DEBUG"):
    # verifiers logs at DEBUG level here
    ...
# reverts to previous level
```

```python
vf.quiet_verifiers()
```

Context manager to temporarily silence verifiers logging by setting WARNING level. Shorthand for `vf.log_level("WARNING")`.

```python
with vf.quiet_verifiers():
    # verifiers logging is quieted here
    outputs = env.generate(...)
# logging restored



---

# FILE: docs/training.md

# Training

This section covers how to use Verifiers environments for RL training with our Hosted Training platform, our open-source `prime-rl` trainer, or other supported libraries.

## Table of Contents

- [Hosted Training](#hosted-training)
    - [Configuration](#configuration)
- [Training with `prime-rl`](#training-with-prime-rl)
    - [Setup and Configuration](#setup-and-configuration)
- [Prompt Optimization with `prime gepa run`](#prompt-optimization-with-prime-gepa-run)
    - [Usage](#usage)
    - [Output](#output)
- [RL Rules of Thumb](#rl-rules-of-thumb)
    - [Before Training](#before-training)
    - [Performance Trade-offs](#performance-trade-offs)
    - [Common Issues](#common-issues)
- [Other Trainers](#other-trainers)
    - [Tinker](#tinker)
    - [SkyRL](#skyrl)
    - [rLLM](#rllm)
    - [Integrating with Other Trainers](#integrating-with-other-trainers)

## Hosted Training

Hosted Training, available within our Lab platform, enables you to automatically train models via `prime-rl` without needing to manage your own infrastructure. Hosted Training supports LoRA for RL training, and can be used with any environment built with Verifiers. 

### Configuration

Use the `prime lab setup` script to download example configuration files for Hosted Training into your workspace:

```bash
prime lab setup
```

This will download example TOML configs for Hosted Training into `configs/rl/`, example eval configs into `configs/eval/`, along with `configs/endpoints.toml` and GEPA starter configs in `configs/gepa/`:

```
configs/
├── endpoints.toml
├── eval/
│   ├── minimal.toml
│   └── multi-env.toml
├── rl/
│   ├── alphabet-sort.toml
│   ├── gsm8k.toml
│   ├── math-python.toml
│   ├── reverse-text.toml
│   ├── wiki-search.toml
│   └── wordle.toml
└── gepa/
    ├── base.toml
    └── wordle.toml
```

Example configuration file for the `primeintellect/alphabet-sort` environment with `Qwen/Qwen3-30B-A3B-Instruct-2507`:

```toml
model = "Qwen/Qwen3-30B-A3B-Instruct-2507"
max_steps = 500
batch_size = 256
rollouts_per_example = 8

[sampling]
max_tokens = 512

[[env]]
id = "primeintellect/alphabet-sort"
args = { min_turns = 3, max_turns = 5, power_per_turn = false }

[wandb]
project = "alphabet-sort"
name = "qwen3-30b-i-alphabet-sort"
```

We currently support the following models for Hosted Training:
- `Qwen/Qwen3-4B-Instruct-2507` 
- `Qwen/Qwen3-4B-Thinking-2507`
- `Qwen/Qwen3-30B-Instruct-2507`
- `Qwen/Qwen3-30B-Thinking-2507`
- `Qwen/Qwen3-235B-Instruct-2507`
- `Qwen/Qwen3-235B-Thinking-2507`
- `PrimeIntellect/INTELLECT-3`

Hosted Training is currently in Private Beta. For access, please fill out [this form](https://form.typeform.com/to/iYn9UliG).

## Training with `prime-rl`

Our [`prime-rl`](https://github.com/PrimeIntellect-ai/prime-rl) trainer is a production-ready async RL training framework that supports large-scale multi-node training, agentic rollouts with Verifiers environments, Mixture-of-Experts (MoE) models, LoRA adapters, and other training algorithms such as SFT and online distillation. We recommend using `prime-rl` for training with Verifiers environments on self-managed GPU infrastructure. The default configuration distills the best practices from our research team's experience and the broader community into a stable, easy-to-use recipe, including advanced features such as online difficulty filtering, continuous batching, in-flight weight updates, importance sampling and logprob clipping for stability, and more. 

### Setup and Configuration

To set up your workspace for training with `prime-rl`, run:
```bash
prime lab setup --prime-rl
```

This will clone and install the `prime-rl` trainer and its dependencies, and set up a default TOML config for training with the included `wiki-search` Environment on 8 GPUs.

Then, you can start training with:
```bash
uv run prime-rl configs/prime-rl/wiki-search.toml
```

This will launch a tmux session with separate panes for the trainer, orchestrator, and inference server. For further configuration options, see the [prime-rl documentation](https://docs.primeintellect.ai/prime-rl). 

## Prompt Optimization with `prime gepa run`

`prime gepa run` is the CLI entrypoint for automatic system prompt optimization using [GEPA](https://github.com/gepa-ai/gepa) (Genetic-Pareto prompt optimization). It iteratively refines your environment's system prompt using a teacher LLM to reflect on evaluation results, without requiring gradient-based training. Current support is for system prompt optimization only.

### Usage

Basic usage mirrors `prime eval run`:
```bash
prime gepa run wiki-search --model google/gemini-3-flash-preview
```

This will optimize the system prompt for the `wiki-search` environment using the specified model for both evaluation rollouts and reflection. Results are saved to `environments/wiki-search/outputs/gepa/`.

Key options:
- `--model` / `-m`: Model for evaluation rollouts
- `--reflection-model` / `-M`: Teacher model for prompt reflection (defaults to `--model`)
- `--max-calls` / `-B`: Evaluation budget (default: 500)
- `--num-train` / `-n`: Training examples (default: 100)
- `--num-val` / `-N`: Validation examples (default: 50)
- `--minibatch-size`: Number of examples evaluated together per reflection step (default: 3)
- `--perfect-score`: Maximum score for a rollout in your environment (if applicable); minibatches achieving this score are skipped during reflection (useful if your environment has a known max score)
- `--state-columns`: Additional state columns to copy into the reflection dataset. By default, `query`, `completion`, `expected_answer`, `reward`, and `error` are included. Use this to add environment-specific state fields (e.g., `--state-columns tool_calls reasoning_trace`)

### Output

After optimization, you'll find:
- `best_prompt.txt` - The optimized system prompt
- `pareto_frontier.jsonl` - Best prompts per validation example
- `metadata.json` - Run configuration and summary

Use `prime eval run` to verify performance before and after optimization.

## RL Rules of Thumb

RL training can be sensitive to implementation details and hyperparameters. Some simple practical guidance:

### Before Training

1. **Evaluate baseline performance**: If your model gets 0% reward after 10+ attempts, the task is too hard
2. **Check task difficulty**: If baseline is already 80%+, consider harder examples
3. **Ensure reward diversity**: You want varied scores within each generation group

### Performance Trade-offs

**For more aggressive training** (higher risk of collapse):
- Increase learning rate (1e-5 to 1e-4 for LoRA, 1e-6 to 1e-5 for full finetuning)
- Decrease `rollouts_per_example` and `batch_size` for faster generation

**For more stable training** (slower progress):
- Increase `rollouts_per_example` (16-32)
- Increase `batch_size` (512-1024)
- Use larger models (14B+)

The best way to improve training is to ensure appropriate task difficulty for your model. When using Hosted Training or `prime-rl`, you can enable online difficulty filtering to ensure that rollout groups used for training always contain a diversity of rewards.

### Common Issues

**Non-Increasing Chat Templates:** The Qwen3 and DeepSeek-R1 model series both remove `<think>` sections from messages when processing inputs, which violates the increasing context requirement for multi-turn training. We provide versions of many of these models with modified chat templates [here](https://huggingface.co/collections/willcb/qwen3-68434f4883925bfdb4570ee5).

**OOM during generation:**
- Reduce `rollouts_per_example` or `micro_batch_size`
- Use LoRA instead of full finetuning
- Check vLLM server has sufficient memory

**Training instability:**
- Decrease learning rate
- Increase `rollouts_per_example`
- Increase `batch_size`

**Slow training:**
- Increase learning rate
- Leverage continuous rewards
- Use online difficulty filtering
- Calibrate difficulty appropriately via smarter models, easier tasks

## Other Trainers

`verifiers` is intended to be largely trainer-agnostic and is straightforward to support for any trainer which can expose an OpenAI-compatible inference client for rollouts.

### `vf.RLTrainer` (Legacy)

The legacy `vf.RLTrainer` still exists for educational and experimental purposes via the optional `verifiers-rl` package and the legacy RL CLI entrypoint, but it is not actively maintained. It is a compact single-node async RL trainer with a narrower feature set than production trainers. Its core implementation (`trainer.py` and `orchestrator.py` under `packages/verifiers-rl/verifiers_rl/rl/trainer/`) remains intentionally lightweight for algorithm experimentation. For production training and current guidance, use [`prime-rl`](#training-with-prime-rl).

### Tinker

[Tinker](https://thinkingmachines.ai/tinker/) supports Verifiers environments via the `tinker-cookbook` recipes.

- [Verifiers + Tinker Recipe](https://github.com/thinking-machines-lab/tinker-cookbook/tree/main/tinker_cookbook/recipes/verifiers_rl)

### SkyRL

[SkyRL](https://github.com/NovaSky-AI/SkyRL) supports Verifiers environments via its `skyrl-train` integration.

- [Verifiers + SkyRL Integration](https://github.com/NovaSky-AI/SkyRL/tree/main/skyrl-train/integrations/verifiers)

### rLLM

[rLLM](https://github.com/rllm-project/rllm) supports Verifiers environments with both [verl](https://github.com/volcengine/verl) (local GPU) and [Tinker](https://thinkingmachines.ai/tinker/) (remote GPU) backends.

- [Verifiers + rLLM Documentation](https://rllm-project.readthedocs.io/en/latest/examples/verifiers/)



---

# FILE: skills/brainstorm/SKILL.md

---
name: brainstorm
description: Run interactive brainstorming across verifiers environments, evaluations, GEPA, and RL training. Use when the user wants ideation, literature scanning, concept teaching, roadmap planning, or research program design grounded in local CLI sources, verifiers, and RL trainer code.
---

# Brainstorm

## Goal
Run structured, interactive ideation that turns ambiguous research goals into concrete environment and evaluation plans.

## Interaction Style
1. Drive an iterative conversation, not a one-shot dump.
2. Ask focused clarifying questions before proposing large plans.
3. Keep suggestions toolchain-native: CLI, verifiers, and RL trainer workflows.

## Discovery Workflow
1. Clarify objective, model family, budget, and timeline.
2. Map objective to workflow levers:
- environment creation or migration
- benchmark/eval design
- GEPA prompt optimization
- RL training
3. Build a short option set, then deepen only selected options.
4. Nudge model-family intent explicitly:
- Instruct-first exploration defaults: `gpt-4.1` series, `qwen3` instruct series.
- Reasoning-first exploration defaults: `gpt-5` series, `qwen3` thinking series, `glm` series.
- Recommend endpoint aliases in `configs/endpoints.toml` for repeatable experiments.

## Required Grounding Sources
1. Read local source before proposing workflows:
- optionally clone Prime Intellect repositories to `/tmp` only when needed, e.g.
  - `git clone https://github.com/PrimeIntellect-ai/prime-cli /tmp/prime-cli`
  - `git clone https://github.com/PrimeIntellect-ai/prime-rl /tmp/prime-rl`
- current verifiers workspace docs/configs
2. For literature and external eval ideas, browse web sources and prioritize mid-2025 onward unless the user asks otherwise.
3. Include dates when discussing recent papers or benchmarks.

## Concept Teaching Mode
When asked to explain RL or environment concepts:
1. Anchor explanations in prime-rl and verifiers terminology.
2. Use concrete config and rollout examples.
3. Distinguish binary-reward and continuous-reward training implications.

## Planning Output Format
Produce:
1. Problem framing and assumptions.
2. Candidate environment or eval ideas, ranked by expected value and implementation effort.
3. Experiment plan with milestones, metrics, and go/no-go gates.
4. Risks, dependencies, and required decisions from the user.
5. Distribution plan for mature environments: recommend Hub push after smoke-test stability and ask whether visibility should be `PUBLIC` or `PRIVATE`.

## Quality Guardrails
1. Do not make hidden assumptions about benchmark prompt formatting or scoring contracts.
2. Flag platform limitations clearly and pause for user direction when blocked.
3. Prefer official first-party capabilities before suggesting custom third-party tooling.



---

# FILE: skills/browse-environments/SKILL.md

---
name: browse-environments
description: Discover and inspect verifiers environments through the Prime ecosystem. Use when asked to find environments on the Hub, compare options, inspect metadata, check action status, pull local copies for inspection, or choose environment starting points before evaluation, training, or migration work.
---

# Browse Environments

## Goal
Use Prime ecosystem commands to discover environments quickly, inspect quality signals, and pick the right starting point.

## Primary Discovery Workflow
1. List candidate environments:
```bash
prime env list --search "math" --owner primeintellect --show-actions
```
2. Narrow results with owner, tags, mine, or starred filters:
```bash
prime env list --owner primeintellect --tag tools --tag sandbox
prime env list --mine
prime env list --starred
```
3. Prioritize quality and freshness signals:
   - Prefer environments published by `primeintellect` first.
   - Keep only candidates with passing latest action/CI status from `--show-actions` or `prime env status`.
   - Prefer candidates updated in roughly the last 2 months.
   - Prefer candidates on version `v0.1.8` or newer.
4. Inspect details for shortlisted candidates:
```bash
prime env info owner/name
prime env status owner/name
```
5. Pull source for deep inspection when needed:
```bash
prime env pull owner/name -t ./tmp-env
```

## Compare Candidates
For each candidate, collect:
1. Task type and horizon: single-turn, multi-turn, tool, sandbox.
2. Reward type: binary, continuous, judge-based, mixed.
3. Dependencies and secrets requirements.
4. Latest action status and version signal.
5. Recency signal: last updated date (target within ~2 months).
6. Fit to user goal: eval-only, GEPA, RL, or benchmark migration.

## Endpoint And Model Selection Nudge
1. Encourage users to configure endpoint aliases in `configs/endpoints.toml` before comparison evals.
2. Ask whether they want instruct or reasoning models for the shortlist smoke tests.
3. Instruct go-tos: `gpt-4.1` series, `qwen3` instruct series.
4. Reasoning go-tos: `gpt-5` series, `qwen3` thinking series, `glm` series.

## Prefer Official Ecosystem Paths
1. Prefer Hub and Prime CLI workflows before manual third-party setup.
2. Use install + smoke eval to validate real usability. Treat `prime eval run` as the canonical eval path and do not add `--skip-upload` unless the user explicitly requests that deviation:
```bash
prime env install owner/name
prime eval run name -m openai/gpt-4.1-mini -n 5
```
3. For examples in the verifiers repository, use repo install path when available:
```bash
prime env install reverse-text --from-repo
```

## Anti-Patterns
1. Do not recommend building from scratch if a strong ecosystem option exists.
2. Do not rely on README claims without running at least one quick eval.
3. Do not hide incompatibilities or missing dependencies.

## Output Format
Return:
1. Ranked shortlist with one-line rationale per environment.
2. Exact commands to install and run each shortlisted option.
3. Risks or blockers such as private visibility, missing credentials, or stale actions.



---

# FILE: skills/create-environments/SKILL.md

---
name: create-environments
description: Create or migrate verifiers environments for the Prime Lab ecosystem. Use when asked to build a new environment from scratch, port an eval or benchmark from papers or other libraries, start from an environment on the Hub, or convert existing tasks into a package that exposes load_environment and installs cleanly with prime env install.
---

# Create Environments

## Goal
Build production-quality verifiers environments that work immediately in the Prime ecosystem: install, load, evaluate, and train without hidden setup.

## Start With Ecosystem Paths
1. Prefer ecosystem-native setup before custom scaffolding.
2. Use this default loop:
```bash
prime env init my-env
prime env install my-env
prime eval run my-env -m openai/gpt-4.1-mini -n 5
```
3. Treat `prime eval run` as the canonical eval path. It saves results automatically, so do not add `--skip-upload` unless the user explicitly requests that deviation.
4. Prefer an existing environment as a starting point when possible:
```bash
prime env list --search "keyword"
prime env info owner/name
prime env install owner/name
```
5. For repository examples, use repo install when available:
```bash
prime env install math-python --from-repo
```
6. Encourage users to keep endpoint aliases in `configs/endpoints.toml` so smoke tests can switch models quickly.
7. Ask users whether they want instruct or reasoning models for validation.
8. Instruct-first smoke choices: `gpt-4.1` series, `qwen3` instruct series.
9. Reasoning validation choices: `gpt-5` series, `qwen3` thinking series, `glm` series.

## Build Modes

### 1. Build From Scratch
1. Define task contract first: prompt shape, allowed tools, stop conditions, rubric outputs, metrics.
2. Select the smallest correct base class:
- `SingleTurnEnv` for one-response tasks.
- `MultiTurnEnv` for custom interaction loops.
- `ToolEnv` or `MCPEnv` for stateless tools.
- `StatefulToolEnv` for per-rollout resources.
- `CliAgentEnv` for running agent binaries in sandboxes with API interception. Override `get_sandbox_resources(state)` for per-instance resources, `build_env_vars(state)` for custom env vars.
- `ComposableEnv` (with `TaskSet`/`SandboxTaskSet` + `Harness`) for separating *what to solve* from *how to solve it*. Define a `TaskSet` (dataset, instructions, sandbox spec, rubric) and a `Harness` (install script, run command, system prompt), wire them together with zero subclassing. Use `SandboxTaskSet` when tasks need sandboxes with per-instance images/resources. `TaskSet`/`SandboxTaskSet` also accept a `filter_fn: str | None` kwarg (a Python expression string, typically a lambda, evaluating to `Callable[[dict], bool]`) for ad-hoc row filtering at `load_environment(...)` time — applied to post-processed rows (`{"question", "info", "answer", ...}`) with restricted builtins, intended for local `vf-eval` runs (e.g. `filter_fn="lambda x: x['info']['repo'] == 'django/django'"`), not untrusted inputs.
3. Implement `load_environment(...) -> vf.Environment` with explicit arguments.
4. Add `pyproject.toml` defaults in `[tool.verifiers.eval]` only when stable.

### 2. Port From Another Library, Project, or Paper
1. Create a strict source-to-target mapping before coding:
- dataset rows and splits
- prompt rendering and role ordering
- tool I/O schema and stop logic
- scoring math and aggregation
- pass/fail thresholds and special cases
2. Preserve one-to-one logical equivalence for what the model sees and what gets scored.
3. Never invent unresolved formatting decisions. Ask the user to decide explicitly.
4. Benchmark runtime and remove avoidable bottlenecks before handoff.

### 3. Start From Hub Environment
1. Install or pull the closest baseline:
```bash
prime env install owner/name
prime env pull owner/name -t ./tmp-env
```
2. Keep proven interfaces stable unless a migration is deliberate and explicit.
3. Re-run smoke evals after each major change.

## Non-Negotiable Quality Rules
1. Use deterministic, well-defined reward checks or LLM judges.
2. Avoid best-effort deterministic heuristics such as keyword style checks except as an explicit last resort with user sign-off.
3. Make environments self-contained after install. Do not require users to run background servers before `load_environment()`.
4. Manage external resources inside the environment lifecycle.
5. Validate required secrets in `load_environment()` via `vf.ensure_keys(...)`.
6. Surface feature limits directly. Do not ship hacky workarounds without explicit user approval.

## Verification Gate
Run these before claiming completion:
```bash
prime env install my-env
prime eval run my-env -m openai/gpt-4.1-mini -n 5
prime eval run my-env -m openai/gpt-4.1-mini -n 50 -r 1 -s
```
If multi-turn or tool-heavy, also run with higher rollouts:
```bash
prime eval run my-env -m openai/gpt-4.1-mini -n 30 -r 3 -s
```

## Publish Gate Before Large Evals Or Training
1. After smoke tests pass and behavior is stable, recommend pushing to Hub before large evals or RL training.
2. Ask the user explicitly whether visibility should be `PUBLIC` or `PRIVATE`.
3. Use:
```bash
prime env push my-env --visibility PUBLIC
```
or
```bash
prime env push my-env --visibility PRIVATE
```
4. For hosted or large-scale workflows, prefer running with the Hub slug after push:
```bash
prime eval run owner/my-env -m openai/gpt-4.1-mini -n 200 -r 3 -s
```

## Synthetic Data
1. Ask users for preferences on which LLMs to use for synthetic data generation and curation before implementation.
2. Prefer generating synthetic data from raw source documents whenever possible instead of relying only on hand-authored prompts.
3. Use LLM orchestration (planner/generator/validator loops) to improve sample quality and diversity.
4. Use back-translation: start from complete materials and decompose them into incomplete tasks, criteria, or partial artifacts that the model must reconstruct.
5. Use fan-out subtopic sampling from LLMs to expand coverage and avoid overfitting to a narrow slice of the domain.

## Deliverable Format
Report:
1. Environment ID and path.
2. Exact install and eval commands used.
3. Port-equivalence notes if migrated.
4. Any unresolved user decisions that block strict fidelity.



---

# FILE: skills/evaluate-environments/SKILL.md

---
name: evaluate-environments
description: Run and analyze evaluations for verifiers environments using prime eval. Use when asked to smoke-test environments, run benchmark sweeps, resume interrupted evaluations, compare models, inspect sample-level outputs, or produce evaluation summaries suitable for deciding next steps.
---

# Evaluate Environments

## Goal
Run reliable environment evaluations and produce actionable summaries, not raw logs.

## Canonical Eval Path
1. Use `prime eval run` as the default way to run evaluations.
2. Do not add `--skip-upload` or other opt-out flags unless the user explicitly requests that deviation.
3. Standard `prime eval run` runs save results automatically, keeping them available in the user's private Evaluations tab and locally in `prime eval tui`.

## Core Loop
1. Run a smoke evaluation first (do not require pre-install):
```bash
prime eval run my-env -m openai/gpt-4.1-mini -n 5
```
2. Use owner/env slug directly when evaluating Hub environments:
```bash
prime eval run owner/my-env -m openai/gpt-4.1-mini -n 5
```
3. Scale only after smoke pass:
```bash
prime eval run owner/my-env -m openai/gpt-4.1-mini -n 200 -r 3 -s
```
4. Treat ownerless env ids as local-first. If not found locally, rely on Prime resolution for your remote env where applicable.

## Endpoint Shortcuts And Model Family Choice
1. Encourage users to define endpoint aliases in `configs/endpoints.toml` so model, base URL, and key wiring stay reusable.
2. Use aliases via `-m <endpoint_id>` instead of repeating `-b` and `-k`.
3. Ask users explicitly whether they want an instruct or reasoning model before non-trivial evaluations.
4. Instruct go-tos for quick behavior checks: `gpt-4.1` series and `qwen3` instruct series.
5. Reasoning go-tos for deeper test coverage: `gpt-5` series, `qwen3` thinking series, and `glm` series.
6. Example endpoint registry:
```toml
[[endpoint]]
endpoint_id = "gpt-4.1-mini"
model = "gpt-4.1-mini"
url = "https://api.openai.com/v1"
key = "OPENAI_API_KEY"

[[endpoint]]
endpoint_id = "qwen3-32b-i"
model = "qwen/qwen3-32b-instruct"
url = "https://api.pinference.ai/api/v1"
key = "PRIME_API_KEY"
```
7. Endpoint entries support optional `headers` (or `extra_headers`) for custom HTTP headers sent with inference requests:
```toml
[[endpoint]]
endpoint_id = "my-proxy"
model = "gpt-4.1-mini"
url = "https://api.example/v1"
key = "OPENAI_API_KEY"
headers = { "X-Custom-Header" = "value" }
```

## Publish Gate Before Large Runs
1. After smoke tests pass and results look stable, proactively suggest pushing the environment to Hub before large eval sweeps or RL work.
2. Ask the user explicitly: should visibility be `PUBLIC` or `PRIVATE`?
3. Push with chosen visibility:
```bash
prime env push my-env --visibility PUBLIC
```
or
```bash
prime env push my-env --visibility PRIVATE
```
4. For hosted environment workflows, prefer running large jobs against the Hub slug:
```bash
prime eval run owner/my-env -m openai/gpt-4.1-mini -n 200 -r 3 -s
```

## Prefer Config-Driven Evals Beyond Smoke Tests
1. For anything beyond quick checks, nudge the user to create an eval TOML config.
2. Use config files to run multiple evals in one command and keep runs reproducible:
```bash
prime eval run configs/eval/my-benchmark.toml
```
3. Make config files the default for benchmark sweeps, multi-model comparisons, and recurring reports.

## Common Evaluation Patterns
1. Pass args to `load_environment()`:
```bash
prime eval run my-env -a '{"difficulty":"hard"}'
```
2. Override constructor kwargs:
```bash
prime eval run my-env -x '{"max_turns":20}'
```
3. Save extra state columns:
```bash
prime eval run my-env -s -C "judge_response,parsed_answer"
```
4. Resume interrupted runs:
```bash
prime eval run my-env -n 1000 -s --resume
```
5. Save results to a custom output directory:
```bash
prime eval run my-env -s -o /path/to/output
```
6. Run multi-environment TOML suites:
```bash
prime eval run configs/eval/my-benchmark.toml
```
7. Pass extra HTTP headers via CLI (repeatable):
```bash
prime eval run my-env -m my-proxy --header "X-Custom-Header: value"
```
8. Set headers in `[[eval]]` TOML configs as a table or list (merge order: registry row < `headers` table < `header` list / `--header`):
```toml
[[eval]]
env_id = "my-env"
headers = { "X-Custom-Header" = "value" }
header = ["X-Another: val"]
```
9. Run ablation sweeps using `[[ablation]]` blocks in TOML configs:
```toml
[[ablation]]
env_id = "my-env"

[ablation.sweep]
temperature = [0.0, 0.5, 1.0]

[ablation.sweep.env_args]
difficulty = ["easy", "hard"]
```
This generates the cartesian product (6 configs in this example). Use `--abbreviated-summary` (`-A`) for compact ablation results.

## Inspect Saved Results
1. Browse locally saved runs:
```bash
prime eval tui
```
2. Inspect platform-visible runs when needed:
```bash
prime eval list
prime eval get <eval-id>
prime eval samples <eval-id>
```

## Metrics Interpretation
1. Treat binary and continuous rewards differently.
2. Use pass@k-style interpretation only when rewards are effectively binary.
3. For continuous rewards, focus on distribution shifts and per-task means.
4. Always inspect samples before concluding regressions.

## Reliability Rules
1. Keep environment/model/config fixed while comparing variants.
2. Record exact command lines and key flags in the report.
3. Call out missing credentials, endpoint mismatches, and dependency errors directly.
4. Do not overinterpret tiny sample runs.

## Output Format
Return:
1. Run configuration table.
2. Aggregate metrics and key deltas.
3. Sample-level failure themes.
4. Clear recommendation: proceed, iterate environment, or retune model/sampling.



---

# FILE: skills/optimize-environments/SKILL.md

---
name: optimize-environments
description: Audit and optimize verifiers environments for async performance. Use when asked to profile, speed up, or review an environment for concurrency bottlenecks, event loop blocking, or scaling issues under high rollout counts.
---

# Optimize Environment Performance

## Goal
Find and fix synchronous bottlenecks in verifiers environment code so that rollouts scale efficiently under concurrency. The verifiers runtime runs all rollouts on a single async event loop — any sync operation blocks every concurrent rollout.

## Audit Workflow

### 1. Identify Async Entry Points
Locate all async methods in the environment (typically `setup_state`, `env_response`, `score`, `cleanup`, and any tool functions). These are the hot paths where sync operations cause the most damage.

### 2. Scan for Sync Offenders
Search for these patterns inside async methods, ordered by typical severity:

**Critical — blocks network I/O:**
- `time.sleep()` → replace with `await asyncio.sleep()`
- Sync HTTP clients (`requests`, `httpx.Client`, `urllib`) → replace with `httpx.AsyncClient` or equivalent
- Sync LLM clients (`OpenAI()`, `litellm.completion()`) → replace with `AsyncOpenAI()` or use `self.get_model_response()`

**High — blocks on disk or CPU:**
- `open()`, `tempfile.NamedTemporaryFile`, `Path.unlink()`, `Path.read_text()`, `shutil` → offload with `await asyncio.to_thread(...)` or use `verifiers.utils.path_utils.write_temp_file`
- `copy.deepcopy()`, `.model_copy()` on non-trivial objects → offload with `await asyncio.to_thread(...)`
- `json.dumps()`/`json.loads()`, `base64.b64encode()`, `msgpack.pack()` on large payloads → offload with `await asyncio.to_thread(...)`

**Medium — blocks GIL for compute:**
- Heavy computation, data parsing, static analysis, compilation → use `ProcessPoolExecutor`

### 3. Check for Shared Immutable Data
If the environment deep-copies an object with large immutable fields (dictionaries, corpora, config blobs):
1. Build a `deepcopy` memo dict that maps `id(immutable_field)` → `immutable_field` so the field is shared, not copied.
2. Compute the memo once in `__init__` after the object is initialized.
3. Pass `memo.copy()` to each `deepcopy` call.

### 4. Check Upload Patterns
If the environment encodes file content manually (base64, JSON) and sends it inline:
- Prefer the client's native async `upload_file()` method instead.
- Write to a temp file (via `asyncio.to_thread(write_temp_file, ...)`) and upload, rather than encoding large blobs on the event loop.

### 5. Check for GIL-Saturating Work
If any single operation takes >50ms of pure CPU time:
- Move it to a `ProcessPoolExecutor` via `loop.run_in_executor(executor, fn, *args)`.
- Common examples: running linters, compilers, parsers, or large data transforms in reward functions.

## Fix Patterns

### asyncio.to_thread() — the default fix
```python
# Offload any sync function
result = await asyncio.to_thread(sync_function, arg1, arg2)
```
The runtime scales the thread pool to match concurrency. No pool management needed.

### Shared deepcopy memo
```python
@staticmethod
def build_shared_memo(obj):
    memo = {}
    memo[id(obj.large_immutable_field)] = obj.large_immutable_field
    return memo

# __init__:
self.shared_memo = self.build_shared_memo(self.obj)

# hot path:
obj_copy = await asyncio.to_thread(deepcopy, self.obj, self.shared_memo.copy())
```

### ProcessPoolExecutor for CPU-bound work
```python
from concurrent.futures import ProcessPoolExecutor
executor = ProcessPoolExecutor(max_workers=4)

async def heavy_reward(data):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, cpu_bound_fn, data)
```

## Findings Format
Report findings sorted by severity:
1. **Critical**: sync network I/O (HTTP, LLM clients, sleep) in async methods.
2. **High**: sync disk I/O, large deepcopy/serialization in async methods.
3. **Medium**: GIL-saturating CPU work inline.
4. **Low**: small sync operations that are technically blocking but negligible in practice.

## Verification
After applying fixes, verify with a concurrency stress test:
```bash
prime eval run <env> -m openai/gpt-4.1-mini -n 64 -r 32 -c -1 -s
```
Compare wall-clock time and the event loop lag which is periodically logged from the env server.



---

# FILE: skills/optimize-with-environments/SKILL.md

---
name: optimize-with-environments
description: Optimize environment system prompts with GEPA through prime gepa run. Use when asked to improve prompt performance without gradient training, compare baseline versus optimized prompts, run GEPA from CLI or TOML configs, or interpret GEPA outputs before deployment.
---

# Optimize With Environments

## Goal
Use GEPA to optimize system prompts in a controlled, reproducible loop.

## Scope
Current GEPA path is for system prompt optimization. If user asks for unsupported optimization targets, stop and clarify before proceeding.

## Endpoint And Model Selection Nudge
1. Encourage users to define reusable aliases in `configs/endpoints.toml`.
2. Ask whether optimization should be validated on instruct or reasoning models.
3. Instruct go-tos: `gpt-4.1` series, `qwen3` instruct series.
4. Reasoning go-tos: `gpt-5` series, `qwen3` thinking series, `glm` series.
5. For benchmark reporting, keep model family fixed between baseline and optimized comparisons unless the user requests a cross-family study.
6. Endpoint entries support optional `headers` (or `extra_headers`) for custom HTTP headers. GEPA inherits these from the registry for both the main model and the reflection model:
```toml
[[endpoint]]
endpoint_id = "my-proxy"
model = "gpt-4.1-mini"
url = "https://api.example/v1"
key = "OPENAI_API_KEY"
headers = { "X-Custom-Header" = "value" }
```

## Core Workflow
1. Verify baseline first with `prime eval run`. Keep the default save behavior and do not add `--skip-upload` unless the user explicitly requests that deviation:
```bash
prime eval run my-env -m openai/gpt-4.1-mini -n 50 -r 3 -s
```
2. Run GEPA:
```bash
prime gepa run my-env -m openai/gpt-4.1-mini -M openai/gpt-4.1-mini -B 500 -n 100 -N 50
```
3. Or run from config:
```bash
prime gepa run configs/gepa/wordle.toml
```
4. Re-evaluate with optimized prompt and compare against baseline.

## High-Value Settings
1. `-B/--max-calls`: total optimization budget.
2. `-n/--num-train` and `-N/--num-val`: train/validation split sizes.
3. `--minibatch-size`: reflection granularity.
4. `--perfect-score`: skip already-solved minibatches when max score is known.
5. `--state-columns`: include environment-specific context in reflection data.

## Output Artifacts
Expect and inspect:
1. `best_prompt.txt`
2. `pareto_frontier.jsonl`
3. `metadata.json`

## Quality Rules
1. Do not optimize on top of broken reward logic.
2. For weak deterministic checks, fix rubric quality before GEPA tuning.
3. Keep model, sampling, and dataset conditions stable during baseline-vs-GEPA comparison.
4. Report limitations directly when feature gaps block requested optimization.

## Deliverable
Return:
1. Baseline metrics.
2. Optimized metrics.
3. Prompt diff summary.
4. Recommendation to adopt, iterate, or stop.



---

# FILE: skills/review-environments/SKILL.md

---
name: review-environments
description: Review verifiers environments for correctness, robustness, and ecosystem compatibility. Use when asked for environment code review, quality audit, migration validation, or release readiness checks for local environments or environments pulled from the Hub.
---

# Review Environments

## Goal
Find correctness risks and regressions first, then assess maintainability and ecosystem compliance.

## Review Input Modes
1. Local environment module in `./environments/<env_name>`.
2. Pulled Hub environment via `prime env pull owner/name`.
3. Installed package under active workspace.

## Review Workflow
1. Identify environment contract:
- `load_environment(...)`
- base class and rollout behavior
- rubric and metrics
2. Verify installability and runtime entrypoint with the canonical eval path. Do not add `--skip-upload` unless the user explicitly requests that deviation; standard runs save automatically for the private Evaluations tab and `prime eval tui`:
```bash
prime env install <env>
prime eval run <env> -m openai/gpt-4.1-mini -n 5
```
3. Trace reward pipeline and validate scoring semantics.
4. Run targeted checks for tool/stateful behavior where applicable.

## Endpoint And Model Selection Nudge
1. Encourage endpoint alias setup in `configs/endpoints.toml` for reproducible review runs.
2. Ask whether review coverage should prioritize instruct or reasoning behavior.
3. Instruct go-tos: `gpt-4.1` series, `qwen3` instruct series.
4. Reasoning go-tos: `gpt-5` series, `qwen3` thinking series, `glm` series.

## Critical Review Criteria
1. Reward correctness:
- Prefer deterministic, explicit checks or LLM judges.
- Flag best-effort keyword or style heuristics unless explicitly approved.
2. Environment self-containment:
- Flag any requirement for user-managed background services before `load_environment()`.
- Require environment-managed lifecycle for sandboxes/sessions.
3. Migration fidelity:
- For ports, verify one-to-one equivalence of prompts, tool traces, and scoring logic.
- Flag any assumptions made without user decision.
4. Secrets handling:
- Ensure required keys are validated in `load_environment()` with `vf.ensure_keys(...)`.
5. Performance and scaling:
- Identify obvious bottlenecks in dataset loading, rubric calls, or tool execution.

## Findings Format
Return findings first, sorted by severity:
1. `P0/P1` bugs and behavioral mismatches.
2. `P2` quality risks and maintainability issues.
3. Test gaps and missing eval coverage.
Include file paths, exact lines, impact, and concrete fix direction.

## If No Findings
State explicitly that no defects were found, then list residual risk and untested areas.



---

# FILE: skills/train-with-environments/SKILL.md

---
name: train-with-environments
description: Train models with verifiers environments using hosted RL or prime-rl. Use when asked to configure RL runs, tune key hyperparameters, diagnose instability, set up difficulty filtering and oversampling, or create practical train and eval loops for new environments.
---

# Train With Environments

## Goal
Run stable RL training loops with environment-aware hyperparameter choices and clear diagnostics.

## Preferred Training Paths
1. By default, assume users intend to use Hosted Training unless they explicitly ask for self-managed training.
2. Hosted Training service path from lab setup:
```bash
prime lab setup
```
3. Self-managed `prime-rl` workflow:
```bash
prime lab setup --prime-rl
uv run prime-rl configs/prime-rl/wiki-search.toml
```
4. Treat `prime-rl` as a power-user path and assume users are comfortable working with GPU infrastructure and troubleshooting.
5. Runtime expectation:
- Hosted Training is intended to be launched from a CPU machine.
- Local `prime-rl` training requires local GPU access.

## Endpoint Shortcuts And Model Family Choice
1. Encourage users to maintain endpoint aliases in `configs/endpoints.toml` for eval and train loops.
2. Ask whether they want instruct or reasoning models for pre-training validation.
3. Instruct go-tos for behavior checks: `gpt-4.1` series, `qwen3` instruct series.
4. Reasoning go-tos for harder reasoning-heavy probes: `gpt-5` series, `qwen3` thinking series, `glm` series.

## First-Run Protocol
1. Validate environment behavior before training with the canonical eval path. Keep the default save behavior and do not add `--skip-upload` unless the user explicitly requests that deviation:
```bash
prime env install my-env
prime eval run my-env -m openai/gpt-4.1-mini -n 20 -r 3 -s
```
2. Confirm reward diversity exists at baseline.
3. Start with conservative run length and inspect samples early.

## Publish Gate Before RL
1. Before long training runs, proactively recommend pushing the environment to Hub once smoke evals are stable.
2. Ask the user explicitly whether visibility should be `PUBLIC` or `PRIVATE`.
3. Push with chosen visibility:
```bash
prime env push my-env --visibility PUBLIC
```
or
```bash
prime env push my-env --visibility PRIVATE
```
4. For hosted RL and shared workflows, prefer Hub IDs after push (for example `owner/my-env` in config `[[env]].id`).

## Hyperparameter Rules Of Thumb
1. Use `rollouts_per_example` and `batch_size` together.
2. Treat `batch_size` as total rollout samples per step, not number of groups.
3. Keep `batch_size` divisible by `rollouts_per_example`.
4. Quick tests or simpler environments:
- `rollouts_per_example = 8`
- `batch_size = 128` (or lower)
5. More complex or longer-horizon environments:
- `rollouts_per_example = 16`
- `batch_size = 512` (common strong starting point)
6. Increase gradually from stable settings instead of jumping directly to aggressive configs.

## Difficulty Filtering And Oversampling
1. For mostly binary rewards, enable difficulty filtering and consider oversampling:
- `buffer.online_difficulty_filtering = true`
- `oversampling_factor > 1` (for example `2.0`)
2. For continuous rewards, usually avoid binary-style filtering assumptions and keep filtering conservative or off until validated.
3. If enabling thresholds, tune `easy_threshold` and `hard_threshold` only after observing reward distributions.

## Stability Constraints From Prime-RL
1. Ensure `max_concurrent >= rollouts_per_example * workers_per_env`.
2. Keep async level explicit (`max_async_level`) and monitor off-policy drift.
3. For OOM risk, reduce rollout pressure and sequence lengths before widening training scope.

## Failure Diagnosis
1. Flat reward near zero:
- Task too hard, rubric mismatch, or prompt/tool contract mismatch.
2. Unstable reward swings:
- Lower learning rate, increase rollout group size, reduce async aggressiveness.
3. Slow learning despite stability:
- Revisit task difficulty and reward shaping before increasing risk knobs.

## Non-Negotiable Environment Quality During Training
1. Use deterministic robust checks or LLM judges for rewards.
2. Reject best-effort keyword heuristics unless explicitly approved as last resort.
3. Keep environments self-contained after install; no user-managed background services.
4. Surface feature limitations directly instead of proposing hidden workarounds.

## Deliverable
Return:
1. Config deltas applied.
2. Why each delta was chosen.
3. Observed metrics and failure signatures.
4. Next tuning step with stop conditions.

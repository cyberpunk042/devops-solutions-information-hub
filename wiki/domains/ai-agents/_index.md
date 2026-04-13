# AI Agents

Multi-agent systems, orchestration, fleet management, agent memory, and extension architecture.

**Model:** [[model-claude-code|Model — Claude Code]] | **Standards:** [[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]]

## Start Here

1. [[agent-orchestration-patterns|Agent Orchestration Patterns]] — the structural patterns every agent system converges on
2. [[claude-code|Claude Code]] — the agent runtime powering the entire ecosystem
3. [[harness-engineering|Harness Engineering]] — how to build guardrails around autonomous agents

## The Agent Runtime

| Page | What It Covers |
|------|---------------|
| [[claude-code|Claude Code]] | The tool-use agent loop, extension system, context management |
| [[claude-code-skills|Claude Code Skills]] | SKILL.md architecture, complexity spectrum, context economics |
| [[claude-code-context-management|Claude Code Context Management]] | Token budget, session lifecycle, compaction strategy |
| [[claude-code-best-practices|Claude Code Best Practices]] | Planning discipline, extension architecture, compliance |
| [[hooks-lifecycle-architecture|Hooks Lifecycle Architecture]] | 26 lifecycle events, PreToolUse enforcement, handler types |
| [[per-role-command-architecture|Per-Role Command Architecture]] | Role-specific command sets, Plannotator pattern |
| [[design-md-pattern|Design.md Pattern]] | Markdown-as-AI-config for visual design systems |

## Orchestration and Quality

| Page | What It Covers |
|------|---------------|
| [[agent-orchestration-patterns|Agent Orchestration Patterns]] | Deterministic brain, sub-agent delegation, Plan-Execute-Review |
| [[harness-engineering|Harness Engineering]] | 13 guardrail rules (R01-R13), 5-verb workflow, enforcement levels |
| [[task-lifecycle-stage-gating|Task Lifecycle Stage-Gating]] | Phase boundaries, OpenFleet vs OpenArms enforcement |
| [[spec-driven-development|Spec-Driven Development]] | Spec-first workflow, 10 frameworks converging on same cycle |
| [[rework-prevention|Rework Prevention]] | Compound cost model, 4-layer prevention, diagnostic table |
| [[llm-knowledge-linting|LLM Knowledge Linting]] | Automated validation, self-healing lint, contradiction detection |

## Ecosystem Projects

| Page | What It Covers |
|------|---------------|
| [[openfleet|OpenFleet]] | 10-agent fleet, 7-layer architecture, deterministic orchestrator |
| [[openclaw|OpenClaw]] | Open-source agent framework, gateway architecture |

## Pages

- [Claude Code Best Practices](claude-code/claude-code-best-practices.md) — Claude Code best practices span the full development lifecycle: planning discipline (95% confidence before changes), ...
- [Claude Code Context Management](claude-code/claude-code-context-management.md) — Context management in Claude Code is the discipline of controlling what occupies the model's limited context window t...
- [Claude Code Skills](claude-code/claude-code-skills.md) — Skills are Claude Code's primary extension mechanism — markdown-based instruction sets that teach the agent new capab...
- [Claude Code](claude-code/claude-code.md) — Claude Code is Anthropic's official CLI coding agent — a terminal-resident AI that reads, writes, and reasons about c...
- [Agent Orchestration Patterns](orchestration/agent-orchestration-patterns.md) — Agent orchestration is the practice of coordinating multiple AI agents or execution phases through a structured contr...
- [Harness Engineering](orchestration/harness-engineering.md) — Harness engineering is the practice of building structured control systems around LLM coding agents — moving beyond p...
- [OpenClaw](orchestration/openclaw.md) — OpenClaw is an open-source (MIT), local-first AI agent framework (352k+ GitHub stars) that runs persistent AI assista...
- [OpenFleet](orchestration/openfleet.md) — OpenFleet is an AI-native project lifecycle orchestration framework implementing "Vibe Managing" — the shift from dir...
- [Design.md Pattern](patterns/design-md-pattern.md) — Design
- [Hooks Lifecycle Architecture](patterns/hooks-lifecycle-architecture.md) — Claude Code's hook system exposes 26 lifecycle events across 7 categories — session, tool, permission, subagent, task...
- [LLM Knowledge Linting](patterns/llm-knowledge-linting.md) — LLM Knowledge Linting is the practice of running periodic LLM-driven health checks over a wiki knowledge base to find...
- [Per-Role Command Architecture](patterns/per-role-command-architecture.md) — Per-role command architecture is the design principle that different practitioner roles — developer, researcher, PM, ...
- [Rework Prevention](patterns/rework-prevention.md) — Rework prevention is the practice of designing AI agent workflows so that work requiring repetition — due to misalign...
- [Spec-Driven Development](patterns/spec-driven-development.md) — Spec-driven development (SDD) is the discipline of producing structured, artifact-bound specification documents befor...
- [Task Lifecycle Stage-Gating](patterns/task-lifecycle-stage-gating.md) — Task lifecycle stage-gating is the practice of partitioning autonomous agent work into sequential, bounded phases wit...

## Tags

`claude-code`, `skills`, `hooks`, `openfleet`, `multi-agent`, `harness-engineering`, `orchestration`, `ai-agents`, `subagents`, `commands`, `memory`, `context-management`, `automation`, `deterministic-brain`, `fleet-management`, `openclaw`, `mission-control`, `stage-gating`, `methodology`, `planning`

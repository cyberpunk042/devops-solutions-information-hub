# Patterns

Recurring structures validated across 2+ independent systems. Each pattern has concrete instances.

## Cross-Domain Patterns

| Pattern | Instances | Underlying Constraint |
|---------|-----------|----------------------|
| [[Plan Execute Review Cycle]] | OpenFleet, Harness Engineering, wiki pipeline, superpowers | Bounded context + compound error cost |
| [[Context-Aware Tool Loading]] | Skills vs MCP, Playwright CLI vs MCP, NotebookLM | Context window fills → accuracy degrades |
| [[Progressive Distillation]] | Zettelkasten, PARA, wiki maturity, page sections | Signal degrades without explicit distillation |
| [[Deterministic Shell, LLM Core]] | OpenFleet orchestrator, harness rules, wiki post-chain | LLM reasoning is probabilistic |
| [[Gateway-Centric Routing]] | OpenArms gateway, OpenClaw, wiki MCP, OpenFleet orchestrator | N deployments drift without central control |
| [[Scaffold → Foundation → Infrastructure → Features]] | Research Wiki, OpenFleet, AICP, Front-Middleware-Backend | Build lifecycle repeats at every scale |

## Skills Integration Patterns

| Pattern | What It Maps |
|---------|-------------|
| [[Skills + Claude Code]] | How skills extend the Claude Code agent |
| [[Skills + CLI]] | CLI tools paired with SKILL.md files |
| [[Skills + MCP]] | MCP servers as skill infrastructure |
| [[Skills + NotebookLM]] | NotebookLM automation via skills |
| [[Skills + Obsidian]] | Obsidian vault management via skills |

See also: [[Cross-Domain Patterns]] for the meta-analysis of why these 6 patterns recur.

## Pages

- [CLAUDE.md Structural Patterns for Agent Compliance](claude-md-structural-patterns.md) — Structural formatting techniques that improve agent compliance with methodology instructions
- [Context-Aware Tool Loading](context-aware-tool-loading.md) — Only load tool schemas, documentation, or external data into the context window when the agent actually needs them — ...
- [Deterministic Shell, LLM Core](deterministic-shell-llm-core.md) — Deterministic Shell, LLM Core is the architectural pattern of wrapping LLM inference inside a deterministic orchestra...
- [Enforcement Hook Patterns](enforcement-hook-patterns.md) — Reusable hook patterns that enforce methodology compliance through infrastructure rather than instructions
- [Gateway-Centric Routing](gateway-centric-routing.md) — Gateway-Centric Routing is the architectural pattern of channeling all traffic — messages, tasks, tool calls, or agen...
- [Plan Execute Review Cycle](plan-execute-review-cycle.md) — The Plan→Execute→Review cycle is a recurring structural pattern observed independently across AI agent orchestration ...
- [Progressive Distillation](progressive-distillation.md) — Progressive Distillation is the pattern of processing raw material through successive layers of increasing density an...
- [Scaffold → Foundation → Infrastructure → Features](scaffold-foundation-infrastructure-features.md) — Scaffold → Foundation → Infrastructure → Features (SFIF) is the universal 4-stage build lifecycle that repeats at eve...
- [Stage-Aware Skill Injection](stage-aware-skill-injection.md) — Dynamically loading or restricting skills based on the current methodology stage

## Tags

`agent-compliance`, `orchestration`, `openfleet`, `enforcement`, `skills`, `mcp`, `agent-architecture`, `deterministic`, `guardrails`, `infrastructure`, `cross-domain`, `claude-md`, `structural-patterns`, `formatting`, `context-management`, `token-efficiency`, `deferred-loading`, `cli`, `tool-design`, `accuracy`

# Patterns

Recurring structures validated across 2+ independent systems. Each pattern has concrete instances.

## Cross-Domain Patterns

| Pattern | Instances | Underlying Constraint |
|---------|-----------|----------------------|
| [[plan-execute-review-cycle|Plan Execute Review Cycle]] | OpenFleet, Harness Engineering, wiki pipeline, superpowers | Bounded context + compound error cost |
| [[context-aware-tool-loading|Context-Aware Tool Loading]] | Skills vs MCP, Playwright CLI vs MCP, NotebookLM | Context window fills → accuracy degrades |
| [[progressive-distillation|Progressive Distillation]] | Zettelkasten, PARA, wiki maturity, page sections | Signal degrades without explicit distillation |
| [[deterministic-shell-llm-core|Deterministic Shell, LLM Core]] | OpenFleet orchestrator, harness rules, wiki post-chain | LLM reasoning is probabilistic |
| [[gateway-centric-routing|Gateway-Centric Routing]] | OpenArms gateway, OpenClaw, wiki MCP, OpenFleet orchestrator | N deployments drift without central control |
| [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]] | Research Wiki, OpenFleet, AICP, Front-Middleware-Backend | Build lifecycle repeats at every scale |

## Skills Integration Patterns

| Pattern | What It Maps |
|---------|-------------|
| [[Skills + Claude Code]] | How skills extend the Claude Code agent |
| [[Skills + CLI]] | CLI tools paired with SKILL.md files |
| [[Skills + MCP]] | MCP servers as skill infrastructure |
| [[Skills + NotebookLM]] | NotebookLM automation via skills |
| [[Skills + Obsidian]] | Obsidian vault management via skills |

See also: [[cross-domain-patterns|Cross-Domain Patterns]] for the meta-analysis of why these 6 patterns recur.

## Pages

- [CLAUDE.md Structural Patterns for Agent Compliance](02_synthesized/claude-md-structural-patterns.md) — Structural formatting techniques that improve agent compliance with methodology instructions
- [Context-Aware Tool Loading](02_synthesized/context-aware-tool-loading.md) — Only load tool schemas, documentation, or external data into the context window when the agent actually needs them — ...
- [Deterministic Shell, LLM Core](02_synthesized/deterministic-shell-llm-core.md) — Deterministic Shell, LLM Core is the architectural pattern of wrapping LLM inference inside a deterministic orchestra...
- [Enforcement Hook Patterns](02_synthesized/enforcement-hook-patterns.md) — Reusable hook patterns that enforce methodology compliance through infrastructure rather than instructions
- [Gateway-Centric Routing](02_synthesized/gateway-centric-routing.md) — Gateway-Centric Routing is the architectural pattern of channeling all traffic — messages, tasks, tool calls, or agen...
- [Plan Execute Review Cycle](02_synthesized/plan-execute-review-cycle.md) — The Plan→Execute→Review cycle is a recurring structural pattern observed independently across AI agent orchestration ...
- [Progressive Distillation](02_synthesized/progressive-distillation.md) — Progressive Distillation is the pattern of processing raw material through successive layers of increasing density an...
- [Scaffold → Foundation → Infrastructure → Features](02_synthesized/scaffold-foundation-infrastructure-features.md) — Scaffold → Foundation → Infrastructure → Features (SFIF) is the universal 4-stage build lifecycle that repeats at eve...
- [Stage-Aware Skill Injection](02_synthesized/stage-aware-skill-injection.md) — Dynamically loading or restricting skills based on the current methodology stage
- [Deterministic Shell, LLM Core](03_validated/architecture/deterministic-shell-llm-core.md) — Deterministic Shell, LLM Core is the architectural pattern of wrapping LLM inference inside a deterministic orchestra...
- [Gateway-Centric Routing](03_validated/architecture/gateway-centric-routing.md) — Gateway-Centric Routing is the architectural pattern of channeling all traffic — messages, tasks, tool calls, or agen...
- [Plan Execute Review Cycle](03_validated/architecture/plan-execute-review-cycle.md) — The Plan→Execute→Review cycle is a recurring structural pattern observed independently across AI agent orchestration ...
- [Progressive Distillation](03_validated/architecture/progressive-distillation.md) — Progressive Distillation is the pattern of processing raw material through successive layers of increasing density an...
- [Scaffold → Foundation → Infrastructure → Features](03_validated/architecture/scaffold-foundation-infrastructure-features.md) — Scaffold → Foundation → Infrastructure → Features (SFIF) is the universal 4-stage build lifecycle that repeats at eve...
- [Contribution Gating — Cross-Agent Inputs Before Work](03_validated/enforcement/contribution-gating-cross-agent-inputs-before-work.md) — In multi-agent systems, contributions from specialist roles (architect design, QA test definitions, security review) ...
- [Enforcement Hook Patterns](03_validated/enforcement/enforcement-hook-patterns.md) — Reusable hook patterns that enforce methodology compliance through infrastructure rather than instructions
- [Harness-Owned Loop — Deterministic Agent Execution](03_validated/enforcement/harness-owned-loop-deterministic-agent-execution.md) — The agent NEVER controls its own execution loop
- [Stage-Aware Skill Injection](03_validated/enforcement/stage-aware-skill-injection.md) — Dynamically loading or restricting skills based on the current methodology stage
- [Three Lines of Defense — Immune System for Agent Quality](03_validated/enforcement/three-lines-of-defense-immune-system-for-agent-quality.md) — AI agents are "sick by default" — LLMs are trained for plausible output, not correct output
- [CLAUDE.md Structural Patterns for Agent Compliance](03_validated/knowledge/claude-md-structural-patterns.md) — Structural formatting techniques that improve agent compliance with methodology instructions
- [Context-Aware Tool Loading](03_validated/knowledge/context-aware-tool-loading.md) — Only load tool schemas, documentation, or external data into the context window when the agent actually needs them — ...
- [Ecosystem Feedback Loop — Wiki as Source of Truth](03_validated/knowledge/ecosystem-feedback-loop-wiki-as-source-of-truth.md) — A central knowledge wiki serves as the source of truth for methodology, standards, and operational knowledge across a...
- [Tier-Based Context Depth — Trust Earned Through Approval Rates](03_validated/knowledge/tier-based-context-depth-trust-earned-through-approval-rates.md) — Different AI models and agents receive different DEPTHS of context based on their demonstrated reliability
- [Validation Matrix — Test Suite for Context Injection](03_validated/knowledge/validation-matrix-test-suite-for-context-injection.md) — Context injection for AI agents is code — it programs behavior through structured markdown

## Tags

`openfleet`, `orchestration`, `agent-compliance`, `enforcement`, `deterministic`, `skills`, `mcp`, `agent-architecture`, `guardrails`, `infrastructure`, `cross-domain`, `harness`, `feedback-loop`, `second-brain`, `claude-md`, `structural-patterns`, `formatting`, `context-management`, `token-efficiency`, `deferred-loading`

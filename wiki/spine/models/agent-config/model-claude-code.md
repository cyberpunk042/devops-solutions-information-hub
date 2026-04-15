---
title: Model — Claude Code
aliases:
  - "Model — Claude Code"
  - "Model: Claude Code"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-12
sources:
  - id: src-shanraisshan-claude-code-best-practice
    type: documentation
    url: https://github.com/shanraisshan/claude-code-best-practice
    title: Claude Code Best Practices
tags: [claude-code, model-definition, agent-architecture, skills, hooks, context-management, harness-engineering, mcp, extension-system, spine]
---

# Model — Claude Code
## Summary

Claude Code is Anthropic's CLI coding agent — a tool-use loop that reads, writes, and reasons about codebases from the terminal. This model defines how the agent works as an extensible runtime: the core agent loop, the four-level extension system (CLAUDE.md, Skills, Hooks, Commands), the context management discipline that governs session quality, the MCP vs CLI+Skills decision that shapes tool integration, and the harness engineering concept that coordinates all layers into a governed system. This is the execution engine behind the research wiki's ingestion pipeline, every OpenFleet agent, and the primary human-to-system interface for the entire ecosystem. Understanding this model means knowing how to extend Claude Code correctly, constrain it safely, and keep its context window healthy.

## Key Insights

- **Agent loop, not chatbot.** Claude Code operates as an iterative decide-call-evaluate loop. Each turn, the model selects tools (Read, Write, Edit, Bash, Grep, Glob, WebFetch, Agent, etc.), executes them, evaluates results, and repeats until the task completes or it yields to the user. There is no fixed pipeline — the agent decides the sequence at runtime.

- **Four-level extension system.** CLAUDE.md (static project config, always loaded), Skills (dynamic context loaded on demand), Hooks (26 lifecycle events for structural enforcement), Commands (lightweight slash triggers). Each level has a different cost-benefit profile and they compose into a coordinated harness.

- **Context window is the primary constraint.** Every architectural decision — lean CLAUDE.md, deferred skill loading, CLI over MCP — traces back to using context efficiently. Degradation at higher utilization is probabilistic, not deterministic — well-managed sessions can work effectively throughout, but careless context loading accelerates problems.

- **CLI+Skills beats MCP for operational tasks.** 12x cost differential measured on Playwright CLI vs MCP. MCP loads all tool schemas at startup; CLI+Skills loads nothing until invoked. MCP wins for external service bridges and tool discovery. See [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]].

- **Harness engineering is the governing concept.** CLAUDE.md + Skills + Hooks + Commands + Subagents form a coordinated control system. OpenArms v10 proves this with quantified evidence: 4 hooks (215 lines) achieved 100% stage boundary compliance where 28 CLAUDE.md rules achieved 25%. OpenFleet extends further with MCP tool blocking at the server level and a 3-line immune system (prevention → detection → correction). See [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]], [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]].

- **Context compaction is a reset event.** All behavioral corrections accumulated during a session are lost after compaction. OpenArms solved this with a post-compact hook that rebuilds full state from files. OpenFleet solves it with PRUNE (kill session, regrow fresh). Any enforcement that depends on accumulated context must be rebuilt via infrastructure. See [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]].

- **Structured context is proto-programming.** Markdown is the programming language of AI agents. Consistent structure across all injections (frontmatter, MUST/MUST NOT blocks, stage protocols) creates patterns agents follow mechanically. OpenFleet's validation matrix (29 scenarios, 2,444 lines) demonstrates this — same structural skeleton for every injection, content varies but shape is constant. See [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]].

- **Subagent parallelism for context isolation.** The Agent tool spawns workers that share the filesystem but not the conversation context. Each subagent gets a fresh context window, protecting the main conversation from bloat. BUT: sub-agents don't inherit CLAUDE.md behavioral rules — compliance is ~33% even when rules are included in the spawn prompt. See [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] (Class 5).

- **Five cognitive contexts read one CLAUDE.md.** OpenArms discovered that interactive operator (A), solo agent (B), sub-agents (C), persona templates (D), and provisioned live agents (E) all read the SAME directive file. Rules meant for one context actively mislead another. Example: "After compaction, re-read ALL memories" — Context A has persistent memory, Context B does not. Fix: move per-context rules to skills, keep CLAUDE.md for shared rules clearly marked per-context.

- **SDLC profiles adapt Claude Code configuration.** A POC project needs a lean CLAUDE.md with 2-3 methodology models. A production fleet needs full methodology.yaml + domain profiles + hooks + commands. The identity profile determines which level of Claude Code configuration is appropriate. See [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]].

### Agent Runtime Landscape

> [!info] Claude Code is one agent runtime — the patterns transfer
>
> | Runtime | Configuration | Extension | Key Difference |
> |---------|--------------|-----------|----------------|
> | **Claude Code** | CLAUDE.md + settings.json | Skills, hooks, MCP tools | This model's reference implementation |
> | **Cline** (VS Code extension) | AGENTS.md + CLAUDE.md (as `@`-imports) + `.clinerules/*.md` | `.agents/skills/`, hooks, MCP, checkpoints, plan/act modes | Architectural twin of Claude Code in an IDE UX. Per-step workspace snapshots; MCP-creation-on-demand; strict plan mode opt-in. See [[src-cline-agentic-coding-ide-extension\|Synthesis — Cline]] |
> | **Cursor** | .cursorrules | Custom rules, @commands | IDE-integrated, visual-first |
> | **Windsurf** | .windsurf/rules/*.md | Cascade flows | Directory-based rules, 12k char limit per file |
> | **GitHub Copilot** | .github/copilot-instructions.md | Extensions | IDE-embedded, completion-focused |
> | **Codex CLI** | AGENTS.md | Tool use | Sandboxed execution |
>
> The principles in this model (structured context, extension hierarchy, configuration-as-code) apply across runtimes. The specific mechanisms (CLAUDE.md format, hook system, skill injection) are Claude Code's implementation. When this wiki says "configure the agent," the PATTERN is universal — the FILE NAMES are Claude Code-specific.

## Deep Analysis

### The Agent Architecture

Claude Code's core is a tool-use loop: the model receives a prompt, decides which tools to invoke, executes them, reads the results, and decides again.

> [!info] **Core properties of the agent loop**
> | Property | What it means | Implication |
> |----------|--------------|-------------|
> | **Tool dispatch is model-decided** | Agent chooses from available tools each turn — no predetermined sequence | A single response can chain Read → Edit → Bash → Grep dynamically |
> | **Permission governance gates execution** | Before sensitive tools execute, the permission system checks settings + hooks | Checkpoint layer between model intent and actual execution |
> | **Subagents provide parallelism** | Agent tool spawns isolated workers with fresh context windows | Parallel research, independent edits, context stays clean |
> | **Loop has no fixed depth** | Agent continues calling tools until task is done | Powerful for multi-step tasks, but unbounded sessions can exhaust context |

> [!warning] **Compaction is not free**
> The `/compact` mechanism summarizes history to reclaim space, but quality degrades after 3-4 compactions (one practitioner's observation, not a hard limit). At that point, a fresh session with a transferred summary is the correct move — not another compaction. See [[claude-code-context-management|Claude Code Context Management]].

---

### The Extension System

Claude Code exposes four extension levels. Each has different loading behavior, enforcement strength, and context cost. This is the architecture that makes Claude Code an extensible runtime, not just a chatbot with tools.

---

#### Level 0: CLAUDE.md — Static Project Config

> [!info] **Always loaded. Charged per-message. Treat as a hot path.**
> CLAUDE.md is loaded on every single message in every conversation. It defines project conventions, file structure, workflow rules, and pointers to resources.

| Property | Value |
|----------|-------|
| **Loaded when** | Every message, every conversation |
| **Context cost** | Permanent — every line compounds across every message |
| **Enforcement** | ~60% (model compliance, can be ignored) |
| **Scope** | Project-wide conventions, schema, workflow rules |

> [!tip] **Best practices**
> - Keep under 200 lines — every line is charged on every message
> - Treat as an index, not an encyclopedia — point to files, don't contain them
> - Use `.claude/rules/` to split large instruction sets into separate files
> - Wrap critical rules in `<important if="...">` tags to prevent attention dropout

> [!example]- **Real instance: this wiki's CLAUDE.md**
> The research wiki's CLAUDE.md covers: page schema, ingestion modes, quality gates, tooling commands, the agent methodology (stage gates), and naming conventions. It points to `wiki/config/methodology.yaml` and `wiki/config/agent-directive.md` for detailed methodology — it does NOT contain 424 lines of agent directive inline. The routing table pattern keeps CLAUDE.md lean while giving the agent full access to detailed instructions via referenced files.

---

#### Level 1: Skills — Dynamic Context on Demand

> [!info] **Loaded only when invoked. Zero cost when unused.**
> Skills are markdown instruction files (SKILL.md) that teach the agent capabilities. They load into context when triggered by user invocation, slash command, or model recognition.

| Property | Value |
|----------|-------|
| **Loaded when** | Explicitly invoked or auto-detected |
| **Context cost** | Zero at rest — loaded only on demand |
| **Enforcement** | ~60% (instructions, not enforcement) |
| **Scope** | Task-specific capabilities, workflows |

> [!tip] **Architecture patterns**
> - **Progressive disclosure via folder structure** — `SKILL.md` at root, with `references/`, `scripts/`, `examples/` subdirectories for deeper context read only when needed
> - **Context forking** — `context: fork` runs the skill in an isolated subagent, preventing intermediate tool calls from polluting the main conversation
> - **Two-phase operation** — setup (install deps, authenticate) then use (execute repeatedly)
> - **Skills compose** — higher-level workflow skills orchestrate lower-level capability skills

> [!example]- **Real instance: this wiki's skill ecosystem**
> 5 skills: `wiki-agent` (ingest/query/maintain), `evolve` (score/scaffold/generate/review), `continue` (session resume), `model-builder` (create/review/evolve models with styling standards), `notebooklm` (mirror wiki to NotebookLM sources).
>
> Each is a folder with `skill.md` defining the capability. The `wiki-agent` skill includes the full ingestion workflow, quality gates, and three modes (auto, guided, smart). The `model-builder` skill includes the styling standards checklist. None of these cost anything until invoked.

This is why skills are the dominant extension pattern. See [[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]].

---

#### Level 2: Hooks — Structural Enforcement

> [!info] **26 lifecycle events. Execution-time blocking. ~98% compliance.**
> Hooks fire shell commands, HTTP requests, prompt evaluations, or subagents at lifecycle events. Unlike skills (instructions the model may follow), hooks are enforcement the model cannot bypass.

| Property | Value |
|----------|-------|
| **Loaded when** | Always active (registered in settings) |
| **Context cost** | Minimal (hook definitions, not content) |
| **Enforcement** | ~98% (execution-time blocking) |
| **Scope** | Safety guardrails, workflow enforcement, context injection |

> [!tip] **The three critical hook patterns**
> - **Blocking pattern** — `PreToolUse` fires before a tool executes. Returns `block` (prevent), `allow` (bypass checks), `ask` (escalate to user), or `defer` (let other hooks decide). This is how the 13 guardrail rules (R01-R13) enforce safety.
> - **Reverse-hook pattern** — `Stop` fires when the agent finishes. Returns `block` to force continuation. `TeammateIdle` prevents idle agents. Bidirectional control: gate initiation AND completion.
> - **Context injection** — `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, and `SubagentStart` accept `additionalContext` in their response, injecting information into the running conversation without user intervention.

> [!example]- **Real instance: stage-gate enforcement via hooks**
> A `PreToolUse` hook can block all Write/Edit calls to `src/` during a documentation phase, enforcing "no implementation in document stage" at the infrastructure level. This is the bridge between methodology (instructions that may be ignored) and enforcement (hooks that cannot be bypassed). OpenArms Bug 5 — scaffold producing 135 lines of business logic — could have been prevented by a hook that blocked Write to source files during the scaffold stage.

See [[hooks-lifecycle-architecture|Hooks Lifecycle Architecture]] for the full 26-event taxonomy.

---

#### Level 3: Commands — Lightweight Triggers

> [!info] **Slash-invoked prompt templates. Zero persistent overhead.**
> Commands inject structured prompts or invoke skills. They are the user-facing interface to the extension system.

| Property | Value |
|----------|-------|
| **Loaded when** | Explicitly invoked via `/command` |
| **Context cost** | Zero persistent — one-time prompt injection |
| **Enforcement** | None (commands trigger, hooks enforce) |
| **Scope** | User workflow shortcuts |

Commands compose with hooks via the Plannotator pattern: a command initiates a workflow, and a hook enforces its constraints. `/careful` activates a skill that blocks destructive Bash commands via a PreToolUse hook — the command is the trigger, the hook is the enforcement.

> [!example]- **Real instance: this wiki's 9 commands**
> `/continue` (resume mission), `/evolve` (evolution pipeline), `/ingest` (source ingestion), `/review` (health check), `/gaps` (gap analysis), `/status` (wiki state), `/backlog` (project management), `/log` (directive logging), `/build-model` (model creation with styling).
>
> Each is a one-line trigger that invokes the corresponding skill. The skill contains the real instructions. The command is the door; the skill is the room.

---

### The Extension System — Summary

> [!info] **Cost-enforcement trade-off across all 4 levels**
> | Level | Mechanism | Context cost | Enforcement | Best for |
> |-------|-----------|-------------|-------------|----------|
> | 0 | CLAUDE.md | High (always loaded) | ~60% | Project conventions, schema, routing |
> | 1 | Skills | Zero until invoked | ~60% | Capabilities, workflows, domain knowledge |
> | 2 | Hooks | Minimal | ~98% | Safety guardrails, stage-gate enforcement |
> | 3 | Commands | Zero | None (triggers) | User shortcuts to skills |
>
> ==The correct architecture uses all four levels together.== CLAUDE.md routes. Skills teach. Hooks enforce. Commands trigger. This coordination is what harness engineering means.

---

### The Context Management Discipline

Context management is not a technique — it is the primary lever on output quality.

> [!warning] **What IS verified vs what is one practitioner's observation**
> | Verified (structural facts) | Unverified (one person's observation) |
> |---------------------------|--------------------------------------|
> | Session overhead exists — system prompts, tools, MCP schemas consume tokens before conversation starts | Specific degradation thresholds (20%, 40%, 60%, 80%) |
> | Subagent isolation gives each worker a fresh context window | Whether degradation is a step function or gradual |
> | Compaction reclaims space but loses detail | "51,000 token" baseline — one developer's setup |
> | CLI+Skills loads on demand vs MCP at startup (measurable) | "5-minute prompt cache TTL" — unconfirmed by Anthropic |
> | MCP schema overhead compounds per connected server | "3-4 compactions" degradation claim |

> [!tip] **Context management best practices (verified)**
> - **Lean CLAUDE.md** — under 200 lines. It loads on every message.
> - **Deferred skill loading** — skills cost zero until invoked. Don't pre-load.
> - **Subagent isolation** — delegate research, file exploration, and bulk operations to subagents. Fresh context window per worker.
> - **CLI over MCP for operational tasks** — 12x measured cost differential on Playwright.
> - **Targeted reads** — specific line ranges, not whole files. `Read offset=50 limit=30`, not `Read` a 2,000-line file.
> - **Manual compaction** — `/compact` at natural breakpoints, not when forced by context pressure.
> - **Fresh sessions over infinite continuation** — when context feels heavy, start a new session with a transferred summary.

---

### The MCP vs CLI+Skills Decision

> [!success] **Resolved: default to CLI+Skills for operational tasks. MCP for external service bridges.**

The mechanism is timing of context loading. MCP loads all tool schemas at conversation startup — with 13 wiki tools, hundreds of tokens are added to every message regardless of use. CLI+Skills loads nothing until invoked.

The Playwright comparison provides the clearest evidence: MCP dumps the full accessibility tree after every browser action (10 steps = 10 full tree injections). CLI saves state to a YAML file; Claude reads it only when needed (2-3 targeted reads vs 10 full dumps). Microsoft, Playwright's creator, now officially recommends CLI over MCP for AI agent use. CLI has 3x more features than the MCP version.

> [!abstract] **When MCP wins**
> - External services without native CLI (databases, proprietary APIs, SaaS)
> - Tool discovery across any conversation without per-session setup
> - Exploratory testing where full visibility at every step has genuine value
> - The planned NotebookLM and Obsidian MCP integrations are correct uses — they bridge services not accessible via filesystem

See [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]] for the full decision record with reversibility analysis.

---

### Harness Engineering

Harness engineering ties the extension system into a coordinated control system. A harness is CLAUDE.md + Skills + Hooks + Commands + Subagents working together — not as independent features added ad hoc.

> [!info] **The enforcement hierarchy**
> | Level | Mechanism | Compliance | Example |
> |-------|-----------|-----------|---------|
> | 0 | Prompt guidance | ~60% (model may ignore) | CLAUDE.md: "Always run tests before committing" |
> | 1 | Workflow orchestration | ~80% (sequenced but not enforced) | Skills: Research-Plan-Execute-Review cycle |
> | 2 | Runtime guardrails | ~98% (execution-time blocking) | Hooks: block sudo, force-push, .env writes |
> | 3 | Deterministic orchestration | 100% (no LLM in loop) | OpenFleet 30-second brain cycle |

The 13 guardrail rules (R01-R13) from the claude-code-harness project implement level 2. OpenArms v10 evolved this into a 4-hook system (pre-bash 48L, pre-write 106L, post-write 36L, post-compact 29L) backed by a 1,033-line model-aware stage validator. OpenFleet implements level 2-3 via MCP tool blocking + 30-second doctor cycle immune system. Real-world enforcement data: instructions alone = 25% compliance, hooks = 100% stage compliance, but behavioral failures persist (20% clean completion rate). See [[enforcement-hook-patterns|Enforcement Hook Patterns]] for the full implementation evidence, and [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]] for the risks of over-enforcement.

> [!tip] **The 5-verb universal workflow**
> Setup → Plan → Work → Review → Release. This appears independently in:
> - **superpowers**: brainstorm → plan → execute → verify
> - **OpenFleet**: task-dispatch → execute → review → complete
> - **This wiki's pipeline**: extract → analyze → synthesize → write → integrate
>
> The convergence across 10+ open-source frameworks confirms this cycle is inherent to effective AI-assisted development. See [[plan-execute-review-cycle|Plan Execute Review Cycle]].

> [!abstract] **This ecosystem's current operating level**
> Levels 0-1 (prompt guidance + workflow orchestration via skills and pipeline chains). Level 2 (hook-based runtime guardrails) is the natural next step — the wiki's methodology.yaml defines stage boundaries, but enforcement is currently instruction-based, not hook-based. Level 3 (deterministic orchestration) is already implemented in OpenFleet's brain.

#### Harness Engineering as a Named Discipline (NEW 2026-04-15)

The field crystallized harness engineering as a named discipline in late-2024 → early-2026. Five converging sources documented in [[harness-engineering-is-the-dominant-performance-lever|Lesson — Harness Engineering Is the Dominant Performance Lever]]:

> [!info] The OS analogy — load-bearing pedagogy
>
> | LLM system | OS analog |
> |------------|-----------|
> | Raw LLM | CPU (powerful but inert) |
> | Context window | RAM (fast but volatile, limited) |
> | External databases | Disk (slow, persistent, large) |
> | Tool integrations | Device drivers |
> | **Harness** | **Operating system** (coordinates what the CPU sees and when) |
>
> Source: [[src-rethinking-ai-agents-harness-engineering-rise|Rethinking AI Agents — The Rise of Harness Engineering]] meta-synthesis. Reframes Skills/Hooks/MCP/Plan-mode/Stage-gates as kernel-level primitives in the Claude Code OS.

> [!success] The 5 canonical workflow patterns (Anthropic Dec 2024)
>
> Every production agent composes these five primitives. The taxonomy has become field-canonical (cited by NLAH, Meta-Harness, the YouTube meta-synthesis):
>
> | Pattern | What it does | Claude Code analog |
> |---------|-------------|---------------------|
> | **Prompt chaining** | Sequential steps with gates between | `pipeline` chain: fetch → process → validate → integrate |
> | **Routing** | Classify input → specialized followup | Skill auto-injection by trigger description match |
> | **Parallelization** | Sectioning (independent subtasks) + Voting (same task multiple times) | TodoWrite parallel branches; multi-agent dispatch |
> | **Orchestrator-workers** | Central LLM dispatches to workers, synthesizes | Subagent dispatch with results aggregation |
> | **Evaluator-optimizer** | One LLM generates, another evaluates in a loop | `pipeline post` validate → fix → re-validate cycle |
>
> Source: [[src-anthropic-building-effective-ai-agents|Anthropic — Building Effective AI Agents]]. Anthropic's three core principles for any agent design: maintain simplicity, prioritize transparency (show planning), invest in the **Agent-Computer Interface (ACI)** as a discipline parallel to HCI.

> [!success] The long-running multi-context-window pattern (Anthropic Nov 2025)
>
> Compaction alone is NOT sufficient for tasks spanning multiple context windows. Even Opus 4.5 + Claude Agent SDK fails without explicit harness artifacts. Solution:
>
> | Component | Role |
> |-----------|------|
> | `init.sh` | Initializer agent writes; coding agent reads at session start to bring up dev env |
> | `feature_list.json` | Initializer writes ~200 features as `passes:false`; coding agent flips to `passes:true` only after end-to-end testing |
> | `claude-progress.txt` | Coding agent reads at session start, updates at session end |
> | Initial `git commit` | Bootstrap state for git-history-as-memory |
>
> JSON over Markdown for `feature_list.json` because "the model is less likely to inappropriately change or overwrite JSON files" — format-as-enforcement. Source: [[src-anthropic-effective-harnesses-long-running-agents|Anthropic — Effective Harnesses for Long-Running Agents]].

> [!warning] **Quantified leverage — why this matters**
>
> - **6× performance variation** from harness changes alone, same model, same benchmark (Stanford research, cited via [[src-rethinking-ai-agents-harness-engineering-rise|YouTube meta-synthesis]])
> - **+7.7 points with 4× fewer context tokens** via automated harness search ([[src-arxiv-meta-harness-outer-loop-search|Meta-Harness, Stanford March 2026]])
> - **LangChain coding agent: outside top 30 → rank 5 on TerminalBench-2** by harness-only changes (cited via YouTube)
> - **Production failure modes catalogued** with concrete fixes ([[src-anthropic-effective-harnesses-long-running-agents|Anthropic Nov 2025]])
>
> The model is increasingly commoditized; the harness is where the leverage lives. This wiki's `methodology.yaml` + `AGENTS.md` + `CLAUDE.md` + skills + standards is a partial NLAH (Natural-Language Agent Harness — see [[src-arxiv-natural-language-agent-harnesses|NLAH paper]]) — naming this lets us be deliberate.

---

### Documentation Layers

> [!info] **Six documentation layers in a Claude Code project — must not be conflated**
> | Layer | Where | Purpose | Who reads it |
> |-------|-------|---------|-------------|
> | **Agent config** | CLAUDE.md, .claude/rules/ | Agent behavior rules, project conventions | Claude Code (every message) |
> | **Wiki knowledge** | wiki/ | Synthesized, structured, evolving knowledge | Agent + human (on demand) |
> | **Public docs** | docs/, README.md | User-facing documentation, guides | Humans |
> | **Code docs** | Inline comments, docstrings | Code-level documentation | Developers reading source |
> | **Smart docs** | README.md inside src/ subdirectories | Subsystem explanations alongside code | Developers + agent |
> | **Specs and plans** | docs/superpowers/ | Execution track artifacts, temporary | Agent during implementation |

> [!warning] **Layer violations to avoid**
> - Putting wiki knowledge in code comments (wrong audience, wrong lifecycle)
> - Putting code docs in the wiki (too granular, changes with every refactor)
> - Conflating public docs with wiki pages (different readers, different update cadence)
> - Mixing specs with permanent knowledge (specs are ephemeral, wiki is permanent)

---

### Key Lessons from This Ecosystem

> [!tip] **1. Always Plan Before Executing**
> The biggest source of token waste is not expensive models — it is the agent going down a wrong path and scrapping work. Boris Cherny (Claude Code's creator) recommends: "Do not make any changes until you have 95% confidence in what you need to build." See [[always-plan-before-executing|Always Plan Before Executing]].

> [!tip] **2. Context Management Is the Primary Lever**
> A developer who practices context hygiene gets 3-5x more useful work per session than one who does not. Lean CLAUDE.md, proper skill loading, subagent isolation, targeted reads — these are prerequisites, not optimizations. See [[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]].

> [!tip] **3. Skills Are the Dominant Extension Pattern**
> Skills load on demand at zero baseline cost. MCP loads at startup. Hooks enforce constraints but don't teach. Commands trigger but carry no knowledge. For extending Claude Code with new capabilities, skills are the correct default. See [[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]].

> [!tip] **4. CLI Beats MCP for Token Efficiency**
> The 12x cost differential on Playwright is not an outlier — it's the structural consequence of eager loading (MCP) vs deferred loading (CLI+Skills). For any tool that doesn't need cross-conversation discovery, CLI+Skills wins. See [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]].

---

### How to Adopt

> [!info] **Adding the Claude Code harness to a new project**
> 1. **CLAUDE.md** — project conventions, schema, workflow rules. Under 200 lines. Point to detailed files.
> 2. **Skills** — at minimum: one skill per major workflow. Place in `.claude/skills/` or `skills/`.
> 3. **Commands** — one `/command` per skill for user-facing triggers. Place in `.claude/commands/`.
> 4. **Hooks** — start with safety guardrails (block sudo, force-push, .env writes). Add workflow enforcement as methodology matures.
> 5. **Methodology** — add stage gates to CLAUDE.md. Reference `methodology.yaml` for detailed rules.

> [!example]- **Real instance: OpenArms as a live deployment**
> - **CLAUDE.md = AGENTS.md** (symlinked) — 351 lines covering architecture boundaries, plugin SDK, channel implementation, gateway protocol
> - **Progressive disclosure** — each subsystem has its own AGENTS.md (`src/plugin-sdk/AGENTS.md`, `src/channels/AGENTS.md`, `src/gateway/protocol/AGENTS.md`)
> - **Embedded wiki** — wiki/ with backlog, adapted from this research wiki. Epics, modules, tasks with frontmatter state machines.
> - **50+ skills** — bundled ecosystem, new skills directed to ClawHub marketplace
> - **Methodology enforcement** — `methodology.yaml` + `agent-directive.md` governing autonomous agent operation
> - **`read_when` metadata** — docs self-declare their relevance via frontmatter, enabling agents to know WHEN to load a doc without reading everything
>
> The key insight: documentation layers WORK when each layer has a clear owner (CLAUDE.md = agent, wiki/ = knowledge, docs/ = humans, src/ = developers) and the agent knows which layer to read for which purpose.

> [!example]- **Real instance: this research wiki's harness**
> - **CLAUDE.md** — 180 lines. Schema, ingestion modes, quality gates, tooling commands, agent methodology section with stage gates.
> - **5 skills** — wiki-agent, evolve, continue, model-builder, notebooklm. Each a folder with `skill.md`.
> - **9 commands** — `/continue`, `/evolve`, `/ingest`, `/review`, `/gaps`, `/status`, `/backlog`, `/log`, `/build-model`.
> - **26 MCP tools** (updated 2026-04-15, grown from 17) — wiki operations accessible from any Claude Code conversation. Now past Model — MCP and CLI Integration's stated ~17-20 upper limit for schema overhead; selective tool exposure recommended as the next step.
> - **Pipeline chains** — `post` (6-step validation), `health`, `evolve`, `continue`, `review`. Deterministic orchestration at level 1.
> - **No hooks yet** — operating at levels 0-1. Hook-based stage-gate enforcement is the planned next step.

### Key Pages

Every page that belongs to this model, organized by layer. This is the territory the model governs.

| Page | Layer | Role in the model |
|------|-------|-------------------|
| [[claude-code|Claude Code]] | L2 | The foundational concept — agent loop, tool dispatch, role in ecosystem |
| [[claude-code-best-practices|Claude Code Best Practices]] | L2 | Operational discipline — planning, prompting, context hygiene |
| [[claude-code-context-management|Claude Code Context Management]] | L2 | The primary constraint — utilization, degradation, management strategies |
| [[claude-code-skills|Claude Code Skills]] | L2 | Extension mechanism — SKILL.md format, progressive disclosure, context forking |
| [[harness-engineering|Harness Engineering]] | L2 | The governing concept — 5-verb workflow, enforcement hierarchy, 13 guardrail rules |
| [[hooks-lifecycle-architecture|Hooks Lifecycle Architecture]] | L2 | 26 lifecycle events across 7 categories — the enforcement layer |
| [[per-role-command-architecture|Per-Role Command Architecture]] | L2 | Role-segmented command palettes for different user contexts |
| [[design-md-pattern|Design.md Pattern]] | L2 | DESIGN.md as IaC — human spec → machine executes. Part of Level 0 config. |
| [[mcp-integration-architecture|MCP Integration Architecture]] | L2 | Tool integration via Model Context Protocol — when and how |
| [[claude-code-scheduling|Claude Code Scheduling]] | L2 | Cron-triggered autonomous operations — when the agent runs without a human |
| [[spec-driven-development|Spec-Driven Development]] | L2 | The brainstorm → spec → plan → implement workflow using the extension system |
| [[always-plan-before-executing|Always Plan Before Executing]] | L4 | Lesson: 95% confidence before changes. Planning prevents rework. |
| [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] | L4 | Lesson: 12x cost differential. Eager vs deferred loading. |
| [[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]] | L4 | Lesson: skills beat MCP, hooks, and commands for capability extension. |
| [[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]] | L4 | Lesson: context hygiene = 3-5x more useful work per session. |
| [[context-aware-tool-loading|Context-Aware Tool Loading]] | L5 | Pattern: defer all tool schema loading until needed. Never pre-load. |
| [[plan-execute-review-cycle|Plan Execute Review Cycle]] | L5 | Pattern: the 5-verb universal workflow that emerges across all frameworks. |
| [[deterministic-shell-llm-core|Deterministic Shell, LLM Core]] | L5 | Pattern: deterministic orchestration wrapping probabilistic LLM reasoning. |
| Pattern: Skills + Claude Code | L5 | Pattern: skills as the primary Claude Code extension mechanism. |
| [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]] | L6 | Decision: CLI+Skills default, MCP for external bridges. Reversible. |

---

### Lessons Learned

Validated experience from operating Claude Code in this ecosystem.

| Lesson | What was learned |
|--------|-----------------|
| [[always-plan-before-executing|Always Plan Before Executing]] | The agent going down a wrong path and scrapping work wastes more tokens than any model cost. Plan first, 95% confidence, then execute. |
| [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] | 12x cost differential on Playwright is structural — eager loading (MCP) vs deferred loading (CLI+Skills). Default to CLI for operational tasks. |
| [[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]] | Skills load on demand at zero baseline cost. For extending Claude Code with capabilities, skills are the correct default over MCP, hooks, or commands. |
| [[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]] | Context hygiene is a prerequisite, not an optimization. Lean CLAUDE.md, subagent isolation, targeted reads, manual compaction. |
| [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]] | "Continue" means advance within the current stage, not skip to the next. Claude Code agents are biased toward perceived progress — stage gates prevent this. |
| [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] | Methodology in wiki pages is useless if not in CLAUDE.md. Rules must exist in the agent's operational instructions, not just its knowledge base. |

---

### State of Knowledge

> [!success] **Well-covered (multiple sources, real evidence, validated)**
> - Extension system architecture (4 levels with cost-enforcement trade-offs)
> - MCP vs CLI+Skills decision (12x measured differential, Microsoft recommendation, decision record)
> - Skills as dominant pattern (convergent evidence across 10+ frameworks)
> - Context management principles (lean CLAUDE.md, subagent isolation, deferred loading)
> - Harness engineering concept (enforcement hierarchy, 13 guardrail rules, 5-verb workflow)
> - Documentation layers (6-layer model with clear ownership)

> [!warning] **Thin or unverified (needs deeper research)**
> - Hooks in real production use — the 26-event taxonomy is documented but we have no ecosystem project using hooks for stage-gate enforcement yet
> - Subagent concurrency limits — no benchmarks on parallel file operations
> - Context degradation curve specifics — one practitioner's observations, not Anthropic data
> - Claude Code scheduling patterns — cron-triggered autonomous operation is documented but untested
> - Multi-agent coordination via Claude Code — OpenFleet implements this but the model page doesn't connect deeply to those patterns
> - Hook-based methodology enforcement — the bridge between `methodology.yaml` and runtime execution doesn't exist yet

---

### How to Adopt

> [!info] **What you need to set up a Claude Code project with the full harness**
> 1. `CLAUDE.md` — project conventions, schema, workflow rules. Under 200 lines. Point to detailed files, don't contain them.
> 2. `skills/` or `.claude/skills/` — one skill per major workflow. SKILL.md with progressive disclosure folders.
> 3. `.claude/commands/` — one `/command` per skill for user-facing triggers.
> 4. Hooks (optional, recommended) — start with safety guardrails. Add workflow enforcement as methodology matures.
> 5. `methodology.yaml` + `agent-directive.md` — if using the stage-gate methodology (recommended for any project beyond trivial).

> [!warning] **INVARIANT — never change these**
> - CLAUDE.md under 200 lines — it loads on EVERY message, every conversation
> - Skills are folders with SKILL.md, not single files — progressive disclosure requires subdirectories
> - Hooks block at execution time, not via instructions — the ~98% vs ~60% compliance gap is real
> - CLI+Skills for operational tasks, MCP for external bridges — the cost differential is structural
> - Documentation layers have clear owners — agent config ≠ wiki knowledge ≠ public docs ≠ code docs

> [!tip] **PER-PROJECT — always adapt these**
> - Which skills exist (wiki-agent vs frontend-builder vs deployment-manager — domain-specific)
> - Which hooks to enable (safety guardrails are universal; workflow enforcement is project-specific)
> - Which commands to expose (match the project's workflows, not a generic set)
> - How deep the methodology goes (hotfix-only projects need 2 stages; complex projects need 5)
> - MCP server scope (zero MCP for simple projects; multiple for ecosystem integration)

> [!bug]- **What goes wrong if you skip this**
> - **No CLAUDE.md** → agent has no project context. Every conversation starts from zero. No conventions, no schema, no workflow.
> - **CLAUDE.md too large** → context bloat on every message. 500-line CLAUDE.md wastes 500 tokens × every message × every session.
> - **No skills** → every capability must be re-explained per conversation. No reuse, no consistency.
> - **No hooks** → safety depends on the model following instructions (~60% compliance). sudo, force-push, .env writes are not blocked.
> - **No methodology** → stages skipped, artifacts missing, false readiness claims. See [[model-methodology|Model — Methodology]] for the 7 bugs that prove this.

> [!example]- **Real instance: OpenArms as a live deployment**
> - **CLAUDE.md = AGENTS.md** (symlinked) — 351 lines covering architecture boundaries, plugin SDK, channel implementation, gateway protocol
> - **Progressive disclosure** — each subsystem has its own AGENTS.md (`src/plugin-sdk/AGENTS.md`, `src/channels/AGENTS.md`, `src/gateway/protocol/AGENTS.md`)
> - **Embedded wiki** — wiki/ with backlog, adapted from this research wiki. Epics, modules, tasks with frontmatter state machines.
> - **50+ skills** — bundled ecosystem, new skills directed to ClawHub marketplace
> - **Methodology enforcement** — `methodology.yaml` + `agent-directive.md` governing autonomous agent operation
> - **`read_when` metadata** — docs self-declare their relevance via frontmatter, enabling agents to know WHEN to load a doc without reading everything
>
> The key insight: documentation layers WORK when each layer has a clear owner (CLAUDE.md = agent, wiki/ = knowledge, docs/ = humans, src/ = developers) and the agent knows which layer to read for which purpose.

> [!example]- **Real instance: this research wiki's harness**
> - **CLAUDE.md** — 180 lines. Schema, ingestion modes, quality gates, tooling commands, agent methodology section with stage gates.
> - **5 skills** — wiki-agent, evolve, continue, model-builder, notebooklm. Each a folder with `skill.md`.
> - **9 commands** — `/continue`, `/evolve`, `/ingest`, `/review`, `/gaps`, `/status`, `/backlog`, `/log`, `/build-model`.
> - **26 MCP tools** (updated 2026-04-15, grown from 17) — wiki operations accessible from any Claude Code conversation. Now past Model — MCP and CLI Integration's stated ~17-20 upper limit for schema overhead; selective tool exposure recommended as the next step.
> - **Pipeline chains** — `post` (6-step validation), `health`, `evolve`, `continue`, `review`. Deterministic orchestration at level 1.
> - **No hooks yet** — operating at levels 0-1. Hook-based stage-gate enforcement is the planned next step.

## Open Questions

> [!question] ~~****What is the optimal subagent concurrency?****~~
> **RESOLVED:** 3-5 for independent tasks. 1-2 for shared-state tasks. Beyond 5, context coordination overhead exceeds parallelism benefit.
> At what point does filesystem contention from parallel subagents degrade throughput? The wiki uses subagents for parallel ingestion, but empirical benchmarks on concurrent file operations don't exist yet. (Requires: benchmarking with 2, 4, 8 parallel subagents on real tasks)

> [!question] ~~****When does harness complexity become net negative?****~~
> **RESOLVED:** When harness bugs/latency/configuration overhead exceeds failures prevented. OpenArms v10: 100% stage compliance, 20% clean — harness isn't the bottleneck yet.
> Hooks + skills + commands + methodology.yaml + agent-directive.md is significant infrastructure. At what point does maintaining the harness cost more than the rework it prevents? (Requires: tracking rework hours saved vs harness maintenance hours)

> [!question] ~~****How does the extension model evolve with 1M+ context?****~~
> **RESOLVED:** Skills shift from context-loading to workflow-structuring. Larger window = less need to load context, more need for structured workflows. Hooks unchanged — they're enforcement.
> As context windows grow, the degradation curve argument for CLI-over-MCP weakens. At 1M tokens, MCP schema overhead (~2K tokens) is 0.2% of context — negligible. Does MCP-first become correct at that scale? (Requires: testing MCP performance at 1M context utilization)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Extension system** | [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] |
> | **Markdown as IaC** | [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]] |
> | **Enforcement patterns** | [[enforcement-hook-patterns|Enforcement Hook Patterns]] |
> | **Context engineering** | [[model-context-engineering|Model — Context Engineering]] |
> | **Super-model (all models)** | [[super-model|Super-Model]] |

## Relationships

- BUILDS ON: [[claude-code|Claude Code]]
- BUILDS ON: [[claude-code-skills|Claude Code Skills]]
- BUILDS ON: [[hooks-lifecycle-architecture|Hooks Lifecycle Architecture]]
- BUILDS ON: [[claude-code-best-practices|Claude Code Best Practices]]
- BUILDS ON: [[claude-code-context-management|Claude Code Context Management]]
- BUILDS ON: [[harness-engineering|Harness Engineering]]
- BUILDS ON: [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
- ENABLES: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- ENABLES: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]
- ENABLES: [[model-llm-wiki|Model — LLM Wiki]]
- ENABLES: [[model-ecosystem|Model — Ecosystem Architecture]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- IMPLEMENTS: [[plan-execute-review-cycle|Plan Execute Review Cycle]]
- IMPLEMENTS: [[context-aware-tool-loading|Context-Aware Tool Loading]]
- DERIVED FROM: [[always-plan-before-executing|Always Plan Before Executing]], [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]], [[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]]

## Backlinks

[[claude-code|Claude Code]]
[[claude-code-skills|Claude Code Skills]]
[[hooks-lifecycle-architecture|Hooks Lifecycle Architecture]]
[[claude-code-best-practices|Claude Code Best Practices]]
[[claude-code-context-management|Claude Code Context Management]]
[[harness-engineering|Harness Engineering]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[model-llm-wiki|Model — LLM Wiki]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[model-methodology|Model — Methodology]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
[[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]]
[[ai-agent-artifacts|AI Agent Artifacts — Standards and Guide]]
[[E005-agent-compliance-framework|Agent Compliance Framework]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]]
[[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]
[[context-file-taxonomy|Context File Taxonomy — The 8 Dimensions of Agent Context]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[harness-engineering-is-the-dominant-performance-lever|Harness Engineering Is the Dominant Performance Lever]]
[[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]
[[model-context-engineering|Model — Context Engineering]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[root-documentation-map|Root Documentation Map — Repository-Level Files]]
[[src-claude-code-prompt-patch-rebalancing|Source — Claude Code Prompt Patch: Rebalancing System Prompt Instructions]]
[[src-7-levels-claude-code-rag|Source — The 7 Levels of Claude Code & RAG]]
[[src-vercel-opensrc-toolkit|Source — vercel-labs/opensrc: Source Code Access Toolkit for AI Agents]]
[[src-anthropic-building-effective-ai-agents|Synthesis — Anthropic — Building Effective AI Agents — 5 Canonical Workflow Patterns]]
[[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic — Effective Harnesses for Long-Running Agents]]
[[src-claude-agent-sdk-and-managed-agents|Synthesis — Claude Agent SDK and Managed Agents]]
[[src-cline-agentic-coding-ide-extension|Synthesis — Cline — Agentic Coding IDE Extension with Plan/Act, Skills, Hooks, MCP]]
[[src-llm-architecture-gallery-raschka|Synthesis — LLM Architecture Gallery (Raschka)]]
[[src-arxiv-natural-language-agent-harnesses|Synthesis — Natural-Language Agent Harnesses (NLAH) — Externalizing Harness Logic as Editable Artifacts]]
[[src-pydantic-ai-typed-agent-framework|Synthesis — Pydantic AI: Typed Agent Framework]]
[[src-rethinking-ai-agents-harness-engineering-rise|Synthesis — Rethinking AI Agents — The Rise of Harness Engineering (YouTube Meta-Synthesis)]]
[[src-skillmd-claudemd-agentsmd-three-layer-context|Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md — Three-Layer Agent Context Architecture]]
[[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]

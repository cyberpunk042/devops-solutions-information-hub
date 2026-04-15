---
title: "Synthesis — Anthropic — Effective Harnesses for Long-Running Agents"
aliases:
  - "Synthesis — Anthropic — Effective Harnesses for Long-Running Agents"
type: source-synthesis
domain: ai-agents
layer: 1
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: anthropic-effective-harnesses
    type: article
    url: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
    file: raw/articles/effective-harnesses-for-long-running-agents-anthropic.md
    title: "Effective harnesses for long-running agents"
    authors: "Justin Young (lead), David Hershey, Prithvi Rajasakeran, et al."
    published: 2025-11-26
    ingested: 2026-04-15
tags: [anthropic, harness-engineering, long-running-agents, multi-context-window, initializer-agent, coding-agent, feature-list, progress-file, init-script, claude-progress, compaction]
---

# Synthesis — Anthropic — Effective Harnesses for Long-Running Agents

## Summary

Anthropic's Nov 2025 follow-up to "Building Effective AI Agents" tackles the **multi-context-window problem**: even Opus 4.5 in a loop on the Claude Agent SDK fails to build a production-quality web app from a single high-level prompt. Compaction alone is insufficient. The post documents a two-fold solution: an **initializer agent** that sets up the environment on the first run (init.sh + claude-progress.txt + feature_list.json + initial git commit), and a **coding agent** for every subsequent session that makes incremental progress and leaves clean state. Four failure modes are catalogued with their solutions: (1) Claude declares victory too early → feature list with passes:false markers; (2) leaves environment in messy state → progress file + git; (3) marks features done prematurely → end-to-end testing requirement (browser automation via Puppeteer MCP); (4) wastes time figuring out how to run the app → init.sh script. The "shift workers" analogy captures the core: each new session arrives with no memory; the harness must bridge the gap. Anthropic notes future work on multi-agent specialization (testing/QA/cleanup agents). Direct evidence for the [[harness-engineering-is-the-dominant-performance-lever|Harness Engineering]] lesson and matches Layer 1 (initializer setup) + Layer 2 (per-session conventions) of [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]].

## Source Reference

> [!info] Source card
>
> | Field | Value |
> |-------|-------|
> | Lead author | Justin Young (Anthropic) |
> | Contributors | David Hershey, Prithvi Rajasakeran, Jeremy Hadfield, Naia Bouscal, Michael Tingley, Jesse Mu, Jake Eaton, Marius Buleandara, Maggie Vo, Pedram Navid, Nadine Yasser, Alex Notov |
> | Published | 2025-11-26 |
> | URL | [anthropic.com/engineering/effective-harnesses-for-long-running-agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) |
> | Type | Engineering blog post (long-form, with quickstart code repo) |
> | Specific runtime | Claude Agent SDK + Opus 4.5 |
> | Test case | Building a clone of claude.ai (web app, ~200 features) |

## Key Insights

### 1. Compaction Is Not Sufficient

The post opens with a frank admission: even Opus 4.5 + Claude Agent SDK with compaction enabled fails on multi-context-window tasks. Two failure modes manifest:

- **Try to one-shot** — agent attempts the whole app, runs out of context mid-implementation, leaves a half-built feature undocumented. Next session has to guess what happened.
- **Premature victory** — later session looks around, sees progress, declares done.

This directly validates [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] from this wiki — compaction loses behavioral corrections; it's not a continuity primitive.

### 2. The Shift-Worker Analogy

> "Imagine a software project staffed by engineers working in shifts, where each new engineer arrives with no memory of what happened on the previous shift."

This frames the problem precisely. The solution must be **artifact-based** (each shift leaves notes the next shift can read), not state-based (memory). This is the same insight as the wiki's "claim only what's written down" — durable artifacts dominate session memory.

### 3. The Initializer + Coding Agent Pattern

Two distinct prompts (the "agents" are the same SDK; only the initial user prompt differs — the system prompt and tool set are identical):

| Agent | Runs | Produces |
|-------|------|----------|
| **Initializer** | First session only | `init.sh` (run dev server) + `feature_list.json` (200+ features, all `passes:false`) + `claude-progress.txt` (running log) + initial git commit |
| **Coding agent** | Every subsequent session | Incremental progress (1 feature at a time) + git commit with descriptive message + progress file update + feature status flip |

This is the same pattern as the wiki's [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]] but specialized for long-running coding work. The harness owns the LOOP; the agent owns the STEP.

### 4. Four Failure Modes With Concrete Solutions

| # | Problem | Initializer solution | Coding-agent solution |
|---|---------|---------------------|----------------------|
| 1 | Declares victory on entire project too early | Set up `feature_list.json` with end-to-end descriptions, all `passes:false` initially | Read feature list at session start, work on ONE feature |
| 2 | Leaves environment in messy state | Initial git repo + progress notes file | Read progress + git log at start; commit + update progress at end |
| 3 | Marks features done prematurely | Set up feature list with self-verification requirement | Test end-to-end before flipping `passes:true` (browser automation for web apps) |
| 4 | Wastes time figuring out how to run the app | Write `init.sh` that runs dev server | Read `init.sh` at session start |

This is a 4-cell taxonomy that matches the wiki's [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]] — same problem space, different cataloguing. Both can be cross-referenced.

### 5. JSON for State Files (Not Markdown)

> "After some experimentation, we landed on using JSON for this, as the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files."

This is a **load-bearing micro-finding**. JSON's structural rigidity creates an invariant the agent respects. Markdown's flexibility is exactly the problem. Same insight as the wiki's [[structured-context-governs-agent-behavior-more-than-content|Structured Context Governs Agent Behavior More Than Content]] — structure constrains behavior more than instructions do. The choice of file FORMAT is itself enforcement infrastructure.

### 6. End-to-End Testing as Browser Automation

For web app testing, "Claude mostly did well at verifying features end-to-end once explicitly prompted to use browser automation tools and do all testing as a human user would." Concrete tooling: Puppeteer MCP for headless browser screenshots + interaction. The agent can identify visual bugs that aren't obvious from code review.

Limitations noted honestly: "Claude can't see browser-native alert modals through the Puppeteer MCP, and features relying on these modals tended to be buggier as a result." The harness has tool-coverage gaps; the right response is acknowledging them, not papering over.

### 7. The Get-Up-To-Speed Sequence

Every coding agent session starts with a fixed sequence:

1. Run `pwd` (know where you are)
2. Read `claude-progress.txt` (recent work)
3. Read `feature_list.json` (what's done, what's pending)
4. Run `git log --oneline -20` (commit history)
5. Run `init.sh` (start dev server)
6. Test basic functionality (verify nothing's broken before adding features)
7. Choose highest-priority unfinished feature
8. Implement, test end-to-end, commit, update progress

This sequence is the **session protocol**. The harness enforces it via the initial prompt. It's the same shape as this wiki's [[continue|/continue skill]] — a deterministic boot sequence that resolves "where am I and what should I do?" in a fixed order.

### 8. Inspiration: What Effective Software Engineers Do Daily

> "Inspiration for these practices came from knowing what effective software engineers do every day."

This is the meta-insight. The harness encodes practices that human engineers do automatically (start the day, check the board, pick a task, work, commit, document, end the day). When the agent has no continuous memory, these practices must be made EXPLICIT and EXTERNAL. The harness is **externalized professionalism**.

### 9. Future Work — Multi-Agent Specialization

> "It's still unclear whether a single, general-purpose coding agent performs best across contexts, or if better performance can be achieved through a multi-agent architecture. It seems reasonable that specialized agents like a testing agent, a quality assurance agent, or a code cleanup agent, could do an even better job at sub-tasks."

This is open research. Maps to this wiki's open Q28 (multi-agent handoff artifacts) — both Anthropic and our wiki have it as future work. The specialization question is parallel to BMAD's agent personas (PM, Architect, Developer, Tech Writer) — different teams converging on similar designs.

## Cross-Reference Integration

### Convergent Evidence (strengthens existing pages)

| Existing Page | How This Reinforces It |
|---------------|------------------------|
| [[harness-engineering-is-the-dominant-performance-lever\|Harness Engineering Lesson]] (new) | Quantified production failures + concrete fixes from the source of the SDK. The most authoritative single source on what a good harness DOES. |
| [[harness-owned-loop-deterministic-agent-execution\|Harness-Owned Loop]] | Same pattern, specialized for long-running coding. Harness owns the loop; agent owns the step. |
| [[context-compaction-is-a-reset-event\|Context Compaction Is a Reset Event]] | Direct validation: "compaction isn't sufficient." Even with compaction enabled, agents fail without explicit artifacts. |
| [[agent-failure-taxonomy-seven-classes-of-behavioral-failure\|Agent Failure Taxonomy]] | 4 failure modes here parallel our 7-class taxonomy. Cross-referenceable. The "premature victory" failure matches Class 4 (fatigue cliff) + Class 5 (silent conflict resolution). |
| [[three-layer-agent-context-architecture\|Three-Layer Agent Context Architecture]] (draft) | Initializer prompt = Layer 1 universal (set-up rules). Coding agent prompt = Layer 2 tool-specific. Get-up-to-speed sequence = Layer 3 conditional skill. |
| [[structured-context-governs-agent-behavior-more-than-content\|Structured Context]] | JSON-vs-markdown finding: format choice is enforcement infrastructure. Direct quantitative evidence. |
| [[never-skip-stages-even-when-told-to-continue\|Never Skip Stages]] | "Marks features done prematurely" matches our "claiming done without evidence" failure mode. |

### New Patterns Surfaced

| Pattern | Source quote | Wiki integration |
|---------|--------------|------------------|
| **Externalized professionalism** — harness encodes daily engineering practices that humans do automatically | "Inspiration came from knowing what effective software engineers do every day" | Add to harness-owned-loop pattern as design principle |
| **Format-as-enforcement** — JSON's rigidity > Markdown's flexibility | "model is less likely to inappropriately change or overwrite JSON" | Add to structured-context lesson as concrete tactic |
| **Two-prompt agent specialization** without distinct system prompts | "We refer to these as separate agents in this context only because they have different initial user prompts" | Note for future multi-agent design — specialization can be PROMPT-only, not architecture-only |

## Deep Analysis

### Why Anthropic's Pattern Is the Reference Implementation

Three reasons this synthesis carries authoritative confidence:

1. **Source is the SDK author** — Anthropic builds the Claude Agent SDK. Their best-practices for it ARE the best practices.
2. **Test case is realistic** — building a claude.ai clone (~200 features) is non-trivial. The failure modes documented are real failures in real long-runs.
3. **Solutions are minimal** — three artifacts (init.sh, feature_list.json, claude-progress.txt) plus git. No new infrastructure. Easy to adopt.

### What This Adds to the Wiki's Methodology

The wiki has [[methodology.yaml]] for stage-gating and the [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]] pattern for execution discipline. This post adds the **multi-context-window specialization** that the wiki's models don't yet address explicitly. Candidates for codification:

- Add an `initializer_artifacts:` section to the long-running task model in methodology.yaml
- Document the get-up-to-speed sequence as a `/resume` skill (parallel to `/continue`)
- Adopt the JSON-for-state convention in `wiki/backlog/` for long-running work

### The "Same Agent, Different Prompts" Footnote

The post's footnote is important:

> "We refer to these as separate agents in this context only because they have different initial user prompts. The system prompt, set of tools, and overall agent harness was otherwise identical."

This is **prompt-only specialization** — a form of agent specialization that's almost free. No new system prompt, no different tools, no different harness — just a different initial user message. This gives a third path beyond "single general agent" and "multi-agent fleet": **same agent runtime, prompt-differentiated roles**.

This is relevant to the wiki's [[ai-agent-artifacts|AI Agent Artifacts]] page — persona templates have been treated as system-prompt-level configuration. Anthropic's data suggests user-prompt-level specialization may be sufficient for many cases, matching BMAD's per-persona prompt approach more closely than a full multi-agent architecture.

### Gap — General-Purpose Coding Only

The post explicitly limits scope to web app development. Generalization to other domains (scientific research, financial modeling, data science) is future work. This wiki's domain-profiles approach (typescript, python-wiki, infrastructure, knowledge) is exactly the abstraction that would let the harness pattern transfer — encode the domain-specific testing/build/run commands in the domain profile, keep the harness pattern domain-agnostic.

## Relationships

- RELATES TO: [[src-anthropic-building-effective-ai-agents|Synthesis — Anthropic Building Effective AI Agents]]
- FEEDS INTO: [[harness-engineering-is-the-dominant-performance-lever|Lesson — Harness Engineering Is the Dominant Performance Lever]]
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
- RELATES TO: [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]
- RELATES TO: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
- RELATES TO: [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]
- RELATES TO: [[structured-context-governs-agent-behavior-more-than-content|Structured Context Governs Agent Behavior More Than Content]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]

## Backlinks

[[Synthesis — Anthropic Building Effective AI Agents]]
[[Lesson — Harness Engineering Is the Dominant Performance Lever]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]
[[Structured Context Governs Agent Behavior More Than Content]]
[[model-claude-code|Model — Claude Code]]

---
title: Extension Standards — What Good Skills, Commands, and Hooks Look Like
aliases:
  - "Extension Standards — What Good Skills, Commands, and Hooks Look Like"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-10
updated: 2026-04-10
sources:
  - id: src-shanraisshan-claude-code-best-practice
    type: documentation
    url: https://github.com/shanraisshan/claude-code-best-practice
    title: shanraisshan/claude-code-best-practice
tags: [skills, commands, hooks, standards, gold-standard, anti-patterns, extension-system, quality]
---

# Extension Standards — What Good Skills, Commands, and Hooks Look Like

## Summary

This page defines the quality bar for the EXTENSION SYSTEM. Where [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] defines the four-level hierarchy (CLAUDE.md → Skills → Hooks → Commands), this page shows what GOOD looks like at each level — and what breaks when the standard isn't met. ==Every gold standard references a real artifact from this ecosystem or a documented best practice from the community.==

## Key Insights

- **A good skill is a system, not a text file.** It has trigger phrases (when to load), operations (what it does), process (how to do each operation), quality bar (what "done" looks like), and gotchas (known failure modes). A skill without these is instructions, not a capability.

- **A good command is invisible.** The user types `/ingest` and the system works. They don't need to know the command invokes a skill, which references CLAUDE.md, which is governed by hooks. Good commands hide complexity.

- **A good hook is narrow.** It blocks ONE class of dangerous operation with zero false positives. A hook that fires on every tool call and checks 15 conditions is a performance problem. A hook that fires on `Write` to `.env` and blocks it is enforcement.

- **Good composition is testable.** Can you describe, in one sentence, what happens when `/evolve` is invoked? If the command → skill → hook chain isn't clear, the composition is too complex.

## Deep Analysis

### Gold Standard: Skill Architecture

What a well-built skill looks like structurally and operationally.

> [!success] **Gold standard: `model-builder` skill**
>
> **Structure:**
> ```
> skills/model-builder/
>   skill.md         — 110 lines: operations, process, quality bar, styling standards
> ```
>
> **What makes it the standard:**
> - **4 named operations** — Build, Review, Evolve, List. Each with a trigger phrase ("build model", "review model X", "evolve model").
> - **Process per operation** — Build follows 6 steps (Document → Design → Scaffold → Implement → Test → Update super-model). Not "create a model page."
> - **Quality bar section** — ≥150 lines, define a SYSTEM, explain how to ADOPT, pass `pipeline post`. Testable criteria.
> - **Styling standards section** — added after the wiki design system matured. The skill EVOLVED to include visual quality — it wasn't frozen at creation.
> - **Super-model tree** — visual map showing where new models fit. Structural knowledge embedded.

> [!success] **Gold standard: `wiki-agent` skill**
>
> **What makes it the standard:**
> - **Three ingestion modes** — auto (process without stopping), guided (show plan, wait for approval), smart (auto when confident, escalate when not). The skill doesn't just teach "how to ingest" — it teaches HOW TO CHOOSE an ingestion strategy.
> - **Depth verification rule** — "Read the THING, not the description of the thing." The highest-leverage quality rule, embedded in the skill where it's loaded during every ingestion.
> - **Self-contained** — a subagent loaded with wiki-agent + CLAUDE.md can operate the entire wiki independently. No other skill required.

> [!bug]- **Anti-pattern: the instruction dump**
> A skill that is a wall of prose: "When the user asks you to do X, first do Y, then Z, make sure to A, also B, and don't forget C..."
>
> **Why it fails:** No trigger phrases — the agent doesn't know WHEN to load it. No operations — the agent doesn't know WHAT it does. No quality bar — the agent doesn't know WHEN it's done. No gotchas — the agent hits the same failures repeatedly.
>
> **The fix:** Structure every skill with: trigger phrases, named operations, process per operation, quality bar, gotchas.

> [!bug]- **Anti-pattern: the skill that should be CLAUDE.md**
> A skill containing project conventions, naming rules, and schema definitions. These are always-needed information in a sometimes-loaded mechanism.
>
> **The diagnostic:** Is this information needed on every message? → CLAUDE.md. Only when performing a specific operation? → Skill.

---

### Gold Standard: Command Design

What a well-designed command looks like.

> [!success] **Gold standard: this wiki's command palette**
> 9 commands, each a thin trigger:
>
> | Command | Invokes | What the user types | What actually happens |
> |---------|---------|--------------------|-----------------------|
> | `/continue` | continue skill | "resume" | Run diagnostics → show state → present options |
> | `/evolve` | evolve skill | "score candidates" | Score → scaffold → generate → review maturity |
> | `/ingest` | wiki-agent skill | "process this URL" | Fetch → save to raw/ → synthesize → validate |
> | `/build-model` | model-builder skill | "build model X" | Document → Design → Scaffold → Implement → Test |
> | `/status` | pipeline status | "where are we" | Raw files, page count, validation state |
> | `/gaps` | pipeline gaps | "what's missing" | Orphans, thin pages, weak domains |
> | `/review` | pipeline review | "health check" | Post → review → gaps → crossref |
> | `/backlog` | pipeline backlog | "what's on the board" | Epics, tasks, completion % |
> | `/log` | pipeline log | "log this" | Directive logging to wiki/log/ |
>
> **What makes this the standard:**
> - Each command is ONE action, ONE verb
> - Each invokes a skill or pipeline command — zero duplicated logic
> - The user doesn't need to remember `python3 -m tools.pipeline evolve --score --top 5` — they type `/evolve`

> [!bug]- **Anti-pattern: the command that IS the skill**
> A command file that contains 50+ lines of instructions instead of invoking a skill. The command becomes a skill without the skill's progressive disclosure, gotchas, or quality bar.
>
> **The fix:** Commands trigger. Skills teach. If a command has more than 5-10 lines, extract the content into a skill and make the command a trigger.

> [!bug]- **Anti-pattern: no commands at all**
> Skills exist but no commands expose them. The user has to say "use the wiki-agent skill to ingest this" instead of `/ingest`. The extension system is invisible — users don't know what's available.
>
> **The fix:** One `/command` per skill, minimum. The command palette IS the feature discovery mechanism.

---

### Gold Standard: Hook Configuration

What well-configured hooks look like.

> [!success] **Gold standard: claude-code-harness R01-R13**
> 13 rules covering the critical safety surface:
>
> | Category | Rules | What they enforce |
> |----------|-------|-------------------|
> | **Denial** | R01-R04 | Block sudo, .git/ writes, .env writes, force-push |
> | **Query** | R05-R07 | Flag out-of-scope writes, unexpected installs |
> | **Security** | R08-R10 | Block --no-verify, direct main pushes, credential patterns |
> | **Post-execution** | R11-R13 | Warn assertion tampering, test skipping, coverage reduction |
>
> **What makes this the standard:**
> - **Narrow scope per rule** — each rule blocks ONE class of operation. No "check everything" rules.
> - **Graduated responses** — denial rules `block`. Query rules `ask`. Post-execution rules `warn`. Not everything is a hard block.
> - **13 rules cover the critical surface** — not 50. The set is intentionally minimal.

> [!example]- **Gold standard design: stage-gate enforcement hook**
> A PreToolUse hook that reads `current_stage` from the task's frontmatter:
> - `document` stage → block Write/Edit to `src/`, `tools/`, `scripts/` (no code in document)
> - `scaffold` stage → block Write/Edit creating files >50 lines (no business logic in scaffold)
> - `implement` stage → block Write/Edit to test files (no test modification during implement)
> - `test` stage → block Write/Edit to source files (no source modification during test)
>
> This closes the compliance gap between instruction-based methodology (~60%) and hook-based enforcement (~98%). Not yet implemented in this wiki — this is the design standard for when it is.

> [!bug]- **Anti-pattern: the warning hook**
> A hook that logs "Warning: writing to .env" but doesn't block the operation. The agent sees the warning, reasons about whether it's relevant, and proceeds.
>
> **Why it fails:** A warning that can be reasoned around is a suggestion, not enforcement. If the operation should be blocked, block it. If it should be reviewed, return `ask`. Warnings are the ~60% compliance level wearing a hook costume.

> [!bug]- **Anti-pattern: the everything hook**
> A single PreToolUse hook that fires on every tool call and checks 20 conditions. Every Read, Grep, Glob, and Write triggers the hook. 100ms × every tool call × 50 tool calls per task = 5 seconds of hook overhead per task.
>
> **The fix:** Use matchers to narrow hook scope. Block Write to `.env` — not "check every tool call for .env patterns." Fire on specific tools, specific paths, specific patterns.

---

### Gold Standard: System Composition

What good command → skill → hook composition looks like.

> [!success] **Gold standard: the evolve workflow**
> ```
> /evolve (command, 1 line)
>   → evolve skill (operations: score, scaffold, generate, review)
>     → pipeline evolve --score (deterministic scorer, 6 signals)
>       → pipeline post (6-step validation chain)
>         → CLAUDE.md quality gates (schema, relationships, summaries)
> ```
>
> Each layer does one thing. The command triggers. The skill orchestrates. The pipeline validates. CLAUDE.md defines the standard. A PreToolUse hook could enforce "no maturity promotion without 3+ relationships" — adding enforcement without changing any other layer.

> [!bug]- **Anti-pattern: flat composition**
> A command that directly runs a pipeline command without a skill. `/evolve` → `python3 -m tools.pipeline evolve --score`. The pipeline runs, but there's no skill teaching the agent WHEN to evolve, HOW to evaluate candidates, or WHAT quality bar to apply. The command works mechanically but produces low-quality results because the operational knowledge is missing.
>
> **The fix:** Commands → Skills → Pipeline/Hooks. Every layer present.

---

### The Extension System Checklist

> [!tip] **Run this when setting up extensions for a project**
> - [ ] CLAUDE.md exists, under 200 lines, structured as routing table
> - [ ] At least 1 skill per major workflow, structured as a folder with SKILL.md
> - [ ] Each skill has: trigger phrases, named operations, process steps, quality bar
> - [ ] 1 command per skill for user-facing discovery
> - [ ] Safety hooks block dangerous operations (sudo, force-push, .env minimum)
> - [ ] Hooks use matchers to narrow scope (not firing on every tool call)
> - [ ] Composition is traceable: for any `/command`, you can name the skill and the CLAUDE.md rules it references

> [!tip] **Run this when reviewing existing extensions**
> - [ ] CLAUDE.md still under 200 lines? (grows silently over time)
> - [ ] Any manual workflows that should be skills? (if you explain it twice, make it a skill)
> - [ ] Any skills that should be in CLAUDE.md? (always-needed info in sometimes-loaded mechanism)
> - [ ] Any commands missing? (if a skill exists without a command, users can't discover it)
> - [ ] Hook coverage matches risk surface? (any dangerous ops not hooked?)

## Open Questions

> [!question] **Should skills have a validation schema?**
> Like wiki pages have `wiki-schema.yaml`, should skills have a schema checking for trigger phrases, operations, quality bar, and gotchas? (Requires: enough skills to see the pattern — 5 in this wiki, 50+ in OpenArms)

> [!question] **Can command selection be automated based on role context?**
> Instead of manually installing role-appropriate command sets, can the system detect the user's role (developer, researcher, PM) and surface the right commands? (Requires: role detection mechanism)

> [!question] **What's the optimal hook count per project?**
> claude-code-harness has 13 rules. Is that the sweet spot? At what count does hook overhead (latency, maintenance) exceed the value of enforcement? (Requires: tracking hook maintenance cost vs violations prevented)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Principles** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] · [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] · [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **Identity** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]]
- RELATES TO: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
- RELATES TO: [[model-quality-failure-prevention-standards|Quality Standards — What Good Failure Prevention Looks Like]]

## Backlinks

[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[model-quality-failure-prevention-standards|Quality Standards — What Good Failure Prevention Looks Like]]

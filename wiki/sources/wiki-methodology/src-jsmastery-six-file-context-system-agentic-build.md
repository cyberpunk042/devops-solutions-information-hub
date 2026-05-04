---
title: "Synthesis — JS Mastery Six-File Context System: Spec-Driven Agentic Build Methodology (project-overview · architecture · code-standards · ai-workflow-rules · ui-context · progress-tracker + AGENTS.md, 2026 video tutorial + downloadable templates)"
aliases:
  - "Six-File Context System"
  - "JS Mastery Six-File"
  - "Six-File Methodology"
  - "Spec-Driven Agentic Build"
  - "JS Mastery Methodology"
  - "context/ folder pattern"
type: source-synthesis
domain: cross-domain
layer: 1
status: synthesized
confidence: high
maturity: seed
created: 2026-05-04
updated: 2026-05-04
last_reviewed: 2026-05-04
sources:
  - id: jsmastery-video
    type: video
    url: https://www.youtube.com/watch?v=14RP8liACqo
    file: raw/transcripts/how-senior-engineers-actually-build-with-ai-in-2026-build-a-full-stack-systems-a.txt
    title: "How Senior Engineers Actually Build With AI in 2026 — Build a Full Stack Systems Architecture App (Adrian Hajdin / JS Mastery)"
    description: "Authoritative source — full ~3-hour tutorial walking through the methodology + 29 feature specs of the Ghost AI build. Operator-named source 2026-05-04."
    ingested: 2026-05-04
  - id: jsmastery-templates
    type: file
    file: raw/dumps/Six-File+Context+Methodology/templates/
    description: "Operator-downloaded blank templates the video produces — CLAUDE.md wiring + 6 context files (project-overview · architecture · code-standards · ai-workflow-rules · ui-context · progress-tracker)"
  - id: fowler-spdd-synth
    type: wiki
    file: wiki/sources/wiki-methodology/src-fowler-structured-prompt-driven-development-spdd.md
    description: "Sibling — Thoughtworks' SPDD is the enterprise-scale convergent instance of the same core pattern (prompts as first-class artifacts, abstraction-first, alignment, iterative review, fix-prompt-first closed loop)"
  - id: markdown-as-iac-model
    type: wiki
    file: wiki/spine/models/agent-config/model-markdown-as-iac.md
    description: "Wiki model — the Six-File Context System is a strong instantiation at the solo/freelance project-build scale; the six Markdown files ARE the binding configuration the agent reads before any code"
  - id: caveman-synth
    type: wiki
    file: wiki/sources/tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md
    description: "Adjacent — caveman-compress sub-skill compresses memory files (CLAUDE.md + context files) into caveman-speak for ~46% input compression, directly applicable to the Six-File Context system to keep the AGENTS.md + 6 files token-efficient"
  - id: trust-layer-concept
    type: wiki
    file: wiki/domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md
    description: "Adjacent — the Six-File Context's `ai-workflow-rules.md` parallels the operator's Markdown-rules-DSL concept in the trust-layer epic (runtime contract declared in Markdown, enforced by Python in isolated mode)"
tags: [source-synthesis, six-file-context, jsmastery, adrian-hajdin, spec-driven, agentic-build, prompts-as-artifacts, claude-code, codex, methodology, code-rabbit, ghost-ai, progress-tracker, npx-skills, agentskills, layer-1, paper-evidence, mission-2026-05-04, operator-named]
---

# Synthesis — JS Mastery Six-File Context System: Spec-Driven Agentic Build Methodology

## Summary

The Six-File Context System is a spec-driven agentic-build methodology authored by Adrian Hajdin (JS Mastery) and demonstrated through a ~3-hour tutorial (2026) building **Ghost AI** — a real-time collaborative system-design workspace with 29 feature specs, full Next.js 16 / React 19 / Live Blocks / Trigger Dev / Clerk / Prisma + Postgres / Vercel Blob stack, fully agent-built (Claude Code / Codex / OpenCode / others — agent-agnostic), reviewed by Code Rabbit per PR, and deployed to Vercel. The methodology centers on **six Markdown files** in a `context/` folder at the project root that the AI agent reads before any work: `project-overview.md` (what/who/flows/scope) · `architecture.md` (stack/boundaries/storage/invariants) · `code-standards.md` (TypeScript + framework + styling + API + data conventions) · `ai-workflow-rules.md` (scoping rules + when to split + handling missing requirements + protected files + sync discipline) · `ui-context.md` (theme/colors/typography/border-radius/component library/layout patterns/icons) · `progress-tracker.md` (current phase + completed + in-progress + next + open questions + architecture decisions + session notes). An entry-point `AGENTS.md` (or `CLAUDE.md` for Claude Code, `GEMINI.md` for Gemini, etc.) wires all six files together in load order. Each feature is then built as a numbered spec file `NN-feature.md` in `context/feature-specs/` with goal · design decisions · implementation · verification checklist; the agent reads the spec, marks in-progress in the progress tracker, implements exactly as specified without scope creep, verifies against the checklist, and closes the unit. **Three core disciplines**: conversation-first planning before any code · build in scoped units (one feature per spec, fresh chat per spec) · `current-issues.md` for systematic debugging instead of vague chat fixes. The methodology is **agent-agnostic** (works with Claude Code, Codex, Cursor, Windsurf, Cline, Copilot via `npx skills add` for 40+ agents) and **tool-skill-aware** (install official agent skills for Clerk, Live Blocks, Trigger Dev, Prisma, etc. so the agent has up-to-date API knowledge). Operator-named source 2026-05-04 with downloaded templates already on disk at `raw/dumps/Six-File+Context+Methodology/`.

## Reference Card

> [!info] Six-File Context System reference card

| Field | Value |
|---|---|
| **Author** | Adrian Hajdin / JS Mastery (the channel) |
| **Format** | YouTube tutorial (~3 hours) + downloadable blank templates (operator-downloaded) |
| **Tagline** | *"Specs first, architecture defined, every feature planned before we start building"* |
| **Demo app** | **Ghost AI** — real-time collaborative system-design workspace (Next.js 16 + React 19 + Live Blocks + Trigger Dev + Clerk + Prisma + Postgres + Vercel Blob + Code Rabbit) |
| **Feature specs in demo** | ~29 numbered specs (`01-design-system.md` through `29-spec-ui-integration.md`) |
| **Six files (in load order)** | 1. `project-overview.md` · 2. `architecture.md` · 3. `ui-context.md` · 4. `code-standards.md` · 5. `ai-workflow-rules.md` · 6. `progress-tracker.md` |
| **Wiring file** | `AGENTS.md` at repo root (or `CLAUDE.md` for Claude Code · `GEMINI.md` for Gemini · `.cursor/rules/` for Cursor · `.windsurf/rules/` for Windsurf · `.clinerules/` for Cline · `.github/copilot-instructions.md` for Copilot) |
| **Per-feature spec format** | `NN-feature.md` in `context/feature-specs/` — goal · design decisions · implementation · verification checklist |
| **Per-feature workflow** | read spec → update progress-tracker (in-progress) → implement exactly as specified → verify against checklist → close → fresh chat for next |
| **Debug discipline** | `context/current-issues.md` — paste error + context, agent analyzes before executing fix; deleted before commit (or gitignored) |
| **Review discipline** | Code Rabbit per PR (cited finding: AI code creates 1.7× more problems per PR) — also available as VS Code extension for in-editor review without PR |
| **Agent skills installation** | `npx skills add <package>` — works for 40+ agents (Clerk skills, Live Blocks skills, Trigger Dev skills, Prisma skills) so agent has up-to-date API knowledge |
| **Branch discipline** | `development` → `main` per PR; main is auto-deployed |
| **Confidence** | high — full transcript read (~25K words across 4 chunks); operator-confirmed source 2026-05-04 |
| **Mission relevance** | Critical — the Six-File pattern IS the wiki's [Markdown-as-IaC](../../spine/models/agent-config/model-markdown-as-iac.md) model at the project-build scale; convergent with [Fowler SPDD](src-fowler-structured-prompt-driven-development-spdd.md) at enterprise scale |

## The Six Files (canonical structure)

> [!abstract] **What the Six-File Context System produces — content + load order**

| # | File | Purpose | Content |
|---|---|---|---|
| 1 | **`project-overview.md`** | Product definition | One-paragraph overview · numbered measurable goals · core user flow (sign-in → end state) · features by category · in-scope / out-of-scope (the **out-of-scope is doing the most important work**) · success criteria (specific, verifiable conditions) |
| 2 | **`architecture.md`** | System blueprint | Tech stack table (layer / technology / role) · system boundaries (folder ownership) · storage model (DB metadata vs blob/file storage split) · auth + access model (who can mutate what) · invariants (rules the codebase must never violate) |
| 3 | **`ui-context.md`** | Design tokens + conventions | Theme description (e.g. dark technical workspace) · color tokens as CSS custom properties (no hard-coded hex values allowed) · typography (font / variable mapping) · border-radius scale by context · component library (e.g. shadcn/ui in `components/ui/`) · layout patterns · icon system |
| 4 | **`code-standards.md`** | Implementation conventions | General principles · TypeScript rules (strict mode, no `any`, validate at boundaries) · framework conventions (e.g. server components default, `use client` only when needed) · styling rules (token-only, no hex) · API route rules (validate input, enforce auth/ownership before mutation) · data + storage rules · file organization |
| 5 | **`ai-workflow-rules.md`** | Agent discipline | Approach (incremental, spec-driven, no inferring/inventing) · scoping rules (one feature unit at a time) · when to split work · handling missing requirements (don't invent — add to progress-tracker open questions) · protected files (don't modify without instruction) · keeping docs in sync · pre-commit checklist (works end-to-end · invariants intact · progress-tracker updated · `npm run build` passes) |
| 6 | **`progress-tracker.md`** | Living state | Current phase · current goal · completed · in-progress · next up · open questions · architecture decisions (with the *why*) · session notes (context to resume next session). **The only file that updates constantly throughout the build.** |

> [!info] **The wiring file (`AGENTS.md` / `CLAUDE.md` / etc.) reads the six in load order:**
>
> ```
> 1. context/project-overview.md   — product definition
> 2. context/architecture.md        — system structure, boundaries, storage, invariants
> 3. context/ui-context.md          — theme, colors, typography, components
> 4. context/code-standards.md      — implementation rules
> 5. context/ai-workflow-rules.md   — workflow, scoping, delivery approach
> 6. context/progress-tracker.md    — current phase, completed work, next steps
>
> Update context/progress-tracker.md after each meaningful implementation change.
> If implementation changes architecture/scope/standards, update the relevant file BEFORE continuing.
> ```

## Key Insights

> [!success] **Conversation-first planning — the work is in the architectural conversation, not the code.**
>
> Open a planning AI (Claude / Gemini / GPT — pick one) and **talk through** what you're building before writing any spec: What does it do? Who uses it? What are the core flows? Where are the complex patterns? What could go wrong? Push back on AI's answers, let it pressure-test your thinking until the system is clear in your head. *"This conversation IS the work. It's what senior engineers do before they build. Except they usually do it in their head or on a whiteboard, but doing it with AI externalizes it and makes it faster."* When the system is clear, write it down — and that's where the six files come from.

> [!success] **Build in scoped units — one feature per spec, fresh chat per spec.**
>
> Each feature is a numbered spec file (`NN-feature.md`) in `context/feature-specs/` with: goal (1-2 sentences) · design decisions (visual, structural, behavior) · implementation (broken into sections) · verification checklist (specific verifiable conditions). The per-feature workflow: read spec → mark in-progress in progress-tracker → implement exactly as specified (no scope creep) → verify against checklist → close unit → push code → **start a fresh chat for the next feature**. Fresh chat per feature lowers the context window, increases focus, and prevents stale conversation drift.

> [!success] **Out-of-scope is the most important section of `project-overview.md`.**
>
> Tells the agent: *don't even think about these.* For Ghost AI: billing/subscription systems, enterprise permissions, version specification history. The out-of-scope keeps every session focused on what's actually being built. Without it, agents wander into adjacent territory and break the build with unrelated changes.

> [!success] **`current-issues.md` for systematic debugging — not vague chat fixes.**
>
> When an error appears: create `context/current-issues.md`, paste the error + context, ask the agent to **analyze and propose** before executing. Agent returns analysis with root-cause reasoning; operator gives green light to execute or rejects the analysis. *"It doesn't go into the spiral of trying to fix its own bugs while breaking 10 other things."* The file is gitignored or deleted before commit (Code Rabbit flagged exposing JWT tokens via `current-issues.md` as a critical security issue in the demo).

> [!success] **Agent-agnostic + skill-aware — the methodology works across 40+ agents.**
>
> The wiring file is named per-tool (`CLAUDE.md` · `GEMINI.md` · `.cursor/rules/caveman.mdc` · `.clinerules/` · `.github/copilot-instructions.md` · `AGENTS.md` for general) but the **content is identical** — the same six files. Distribution via `npx skills add <package>` (vercel-labs/skills) reaches 40+ agents. For each external service in the stack (Clerk, Live Blocks, Trigger Dev, Prisma), install the **official agent skills** (`npx skills add clerk-skills` etc.) so the agent has up-to-date API knowledge — critical when frameworks evolve faster than agent training data (the demo had to explicitly tell the agent to use `proxy.ts` instead of `middleware.ts` because Next.js 16 changed the file name and agent training data was older).

> [!success] **Code Rabbit per PR — AI code creates 1.7× more problems.**
>
> Per the cited industry report, AI-generated code introduces 1.7× more problems per PR than human-written code; readability degrades; error handling and security suffer. Code Rabbit reviews each PR (or via VS Code extension for in-editor review) catching: spec-vs-implementation drift · accessibility issues · security issues (e.g., exposing tokens) · best-practice gaps · validation edge cases. Demo flow: development branch → PR → Code Rabbit reviews → operator addresses suggestions → merge to main.

> [!info] **Why fresh chat per feature matters — the AI memory problem.**
>
> *"The first few hours feel incredible, and then a week later, the agent has forgotten every decision you've made. One new feature breaks three others, and the codebase you were excited about just starts fighting you. That's not an AI problem. It's an architecture problem."* The progress-tracker is the solution: at the start of every session (or new chat), one prompt is enough — agent reads progress-tracker, understands exactly where the project stands, and picks up exactly where left off without re-explaining.

> [!info] **Update protected files explicitly** (e.g., `components/ui/*` for shadcn/ui-installed components — they're library outputs and should not be edited).

## Per-Feature Spec Template (NN-feature.md)

> [!example] Canonical structure observed across all 29 demo specs

```markdown
# Feature NN: <Name>

## Goal
1-2 sentences: what does this unit produce when done?

## Design decisions
- Visual / structural / behavioral choices
- References to ui-context.md tokens (no hardcoded values)
- Layout / responsiveness / interaction notes

## Implementation
### Section 1
- Concrete file paths to create/modify
- Specific component / function / route names
- Behavior expected at each integration point

### Section 2
- (continued — break by integration boundary, not by file)

## Checks
- [ ] Specific verifiable condition 1
- [ ] Specific verifiable condition 2
- [ ] No TypeScript errors
- [ ] No lint errors
- [ ] `npm run build` passes
```

The agent's prompt to execute is the same template every time:

> *"Read this file, update the progress-tracker.md file to mark this as in progress, and then implement it exactly as specified."*

## Workflow — End-to-End

> [!example] **The full per-unit cycle from architectural conversation to merged PR**
>
> 1. **Architectural conversation** — Open planning AI; talk through what to build, who uses it, core flows, complex patterns, what could go wrong. Pressure-test until system is clear.
> 2. **Six-file authoring** — Generate the six context files from the conversation output (or use the operator-downloaded templates as starting point and fill in the project specifics). Drop into `context/`.
> 3. **Wiring file** — Place `AGENTS.md` at repo root that reads all six files in order before any work. Add `claude/.md`, `GEMINI.md`, etc. per-tool versions if needed.
> 4. **Plan unit-by-unit** — Break the build into ~20-30 numbered features. Each is small enough to build in a single focused session.
> 5. **Per-feature**:
>    - Author `NN-feature.md` in `context/feature-specs/`
>    - Open fresh chat in your agent (Claude Code / Codex / OpenCode / etc.)
>    - Tell the agent: *"Read this file, update progress-tracker, implement exactly as specified."*
>    - Agent reads spec → reads context files → reads progress-tracker → marks in-progress → implements → verifies → closes
>    - Operator reviews → if good, push to development branch
>    - Open PR development → main → Code Rabbit reviews → address feedback → merge
> 6. **When errors appear** — Author `context/current-issues.md` describing error + context. Ask agent to *analyze and propose* before executing. Operator gives green light → agent executes targeted fix.
> 7. **Repeat** — Until all numbered features are complete. The progress-tracker accumulates the project's institutional memory.

## Mission Alignment

The Six-File Context System is a **strong instantiation of [Markdown-as-IaC](../../spine/models/agent-config/model-markdown-as-iac.md)** at the solo/freelance project-build scale. The six Markdown files in `context/` ARE the binding configuration that the AI agent reads before any work — Markdown as Infrastructure-as-Code for AI-assisted delivery. Combined with [Fowler's SPDD](src-fowler-structured-prompt-driven-development-spdd.md) at enterprise scale, **two independent practitioners (JS Mastery freelance/teaching vs Thoughtworks enterprise IT) converge on the same core pattern**: prompts/specs as version-controlled team assets, abstraction-first, alignment, iterative review, fix-prompt-first closed loop. This is convergent paper evidence for the [anti-vendor-lock-in lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md)'s structured-context-substrate claim — and a methodology-layer addition to the wiki's existing spec-driven evidence chain (BMAD · OpenSpec · Spec-Kit · AI-DLC · Karpathy LLM Wiki).

The Six-File pattern also directly **parallels the wiki's own structure**:

| Six-File Context System | Wiki's own pattern |
|---|---|
| `AGENTS.md` (wiring) | [AGENTS.md](../../../AGENTS.md) (wiring) |
| `project-overview.md` | [README.md](../../../README.md) + [CONTEXT.md](../../../CONTEXT.md) |
| `architecture.md` | [ARCHITECTURE.md](../../../ARCHITECTURE.md) |
| `code-standards.md` | [.claude/rules/work-mode.md](../../../.claude/rules/work-mode.md) + per-domain conventions |
| `ai-workflow-rules.md` | [.claude/rules/learnings.md](../../../.claude/rules/learnings.md) + [.claude/rules/work-mode.md](../../../.claude/rules/work-mode.md) |
| `ui-context.md` | [DESIGN.md](../../../DESIGN.md) |
| `progress-tracker.md` | `wiki/log/` + `wiki/backlog/` (per-session logs + epic/module/task backlog) |
| `NN-feature.md` per-feature specs | `wiki/backlog/modules/` per-module specs |

The wiki's [Trust-Layer Epic](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md) Markdown-rules-DSL concept (M002 — operator-authored 2026-04-30) is also a parallel: runtime contract declared in Markdown, enforced by Python in isolated mode. The Six-File `ai-workflow-rules.md` is the closest existing instance of that pattern in production.

The [Caveman synthesis](../tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md)'s `caveman-compress` sub-skill is **directly applicable** to the Six-File system: compressing CLAUDE.md + the 6 context files into caveman-speak saves ~46% input tokens every session, multiplying the system's efficiency. Worth empirical validation.

## Key Stack Choices Documented in the Demo

> [!info] Production-grade stack with rationale (Ghost AI build)
>
> | Layer | Choice | Why |
> |---|---|---|
> | Framework | Next.js 16 + TypeScript + Tailwind CSS + ESLint | Defaults |
> | UI library | shadcn/ui | Componentized; CLI-installed; library files protected from edits |
> | Authentication | **Clerk** | Free up to 50K MAU; agentskills + MCP + CLI support; would take days/weeks to build from scratch with similar security |
> | Real-time multiplayer | **Live Blocks** | Live cursors, presence, agent collaboration; real-time canvas sync |
> | Background tasks | **Trigger Dev** | Long-running AI generation (>60s) times out in Next.js API routes; trigger.dev runs durable background tasks with retries + status tracking |
> | Database | **Prisma + PostgreSQL** | Hybrid storage with metadata only |
> | File storage | **Vercel Blob** | Private blobs for canvas snapshots + generated specs (markdown) |
> | LLM provider | **Google Gemini 2.5 Flash** (via `@ai-sdk/google` + Vercel AI SDK) | Free tier in most regions; demo also notes Open Router with NVIDIA Nemotron 3 Nano Omni as free fallback |
> | Code review | **Code Rabbit** | Per-PR or in-VS Code review; catches AI-introduced issues at 1.7× rate |
> | Deployment | **Vercel** | Auto-deploy from main branch |

Each external service has **official agent skills** installable via `npx skills add <pkg>`: `clerk-skills`, `liveblocks-skills`, `triggerdotdev-skills`, `prisma-skills`. Installing them means the agent has up-to-date API knowledge — critical when training-data lag would otherwise cause errors (Next.js 16 `proxy.ts` vs older `middleware.ts` was a documented gotcha in the demo).

## Open Questions

> [!question] How does the Six-File Context System compose with the wiki's existing methodology engine?
> The wiki has 9 methodology models (feature-development, bug-fix, etc.) at the macro level. The Six-File pattern is at the project-context level. They're complementary: the methodology engine governs *which model* to use; the Six-File system establishes *what context* the agent has. Worth integrating into the Methodology Adoption Guide.

> [!question] Does `current-issues.md` belong in the wiki's own pattern set?
> The wiki's existing pattern is to log issues in `raw/notes/` for traceability. `current-issues.md` is a transient debug-and-discard file. The two patterns serve different purposes (verbatim sacrosanct directives vs throwaway debug context). Both have a place; clarifying their distinction would be useful in the methodology rules.

> [!question] How do `npx skills add <pkg>` skills compose with the wiki's documented skills/commands/hooks model?
> The wiki's [model-skills-commands-hooks](../../spine/models/agent-config/model-skills-commands-hooks.md) catalogs skill-format conventions. The third-party skills (clerk-skills, liveblocks-skills, etc.) are official packages from the service vendors. They install via the same `npx skills` substrate that JS Mastery uses, supporting 40+ agents. The wiki may want to document this distribution pattern as a separate decision.

> [!question] Caveman-compress applied to Six-File context — what's the empirical compression ratio?
> Caveman-compress reports ~46% average reduction on memory files (CLAUDE.md / todos / preferences). Six-File context files are typical CLAUDE.md/preferences/architecture content. Empirically validating compression on the operator-downloaded templates would close a real gap and connect this synthesis to the [trust-layer 80–90% envelope](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) at the prompt-layer slice.

## How to Apply

> [!tip] Adoption checklist
>
> 1. **Use the operator-downloaded templates as starting point** — at `raw/dumps/Six-File+Context+Methodology/templates/` (already on disk). Replace bracketed placeholders with project specifics.
> 2. **Architectural conversation first** — open Claude / Gemini / GPT, talk through what / who / flows / complex patterns / what could go wrong. Externalize the conversation; let it pressure-test your thinking.
> 3. **Six files per project** — fill in `project-overview` + `architecture` + `ui-context` + `code-standards` + `ai-workflow-rules` + start `progress-tracker` empty.
> 4. **Wiring file** — place `AGENTS.md` (or per-tool variant) at repo root pointing to the six files in order.
> 5. **Plan units** — break the build into ~20-30 numbered features (`NN-feature.md`).
> 6. **Per-feature workflow** — fresh chat → spec + progress-tracker prompt → agent implements → verify checklist → close unit → push to development branch → PR + Code Rabbit → merge to main.
> 7. **For external services** — install official agent skills (`npx skills add <pkg>`) so the agent has up-to-date API knowledge.
> 8. **For errors** — author `context/current-issues.md`, ask agent to analyze before executing, get green light, then execute. Delete or gitignore before commit.
> 9. **Update progress-tracker constantly** — it's the only file that changes through the build; it's how a fresh session in 6 months picks up exactly where left off.

## Relationships

- BUILDS ON: [[model-markdown-as-iac|Model — Markdown as IaC]] — Six-File is the solo/freelance instantiation of Markdown-as-IaC at the project-build scale
- BUILDS ON: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns]] — wiring file conventions
- PARALLELS: [[src-fowler-structured-prompt-driven-development-spdd|Fowler SPDD Synthesis]] — sibling instance of the same core pattern at enterprise-IT scale
- PARALLELS: [[src-bmad-method-agile-ai-development-framework|BMAD Synthesis]] — adjacent spec-driven framework with personas/party-mode framing
- PARALLELS: [[src-openspec-spec-driven-development-framework|OpenSpec Synthesis]] — adjacent spec-driven framework
- PARALLELS: [[src-github-spec-kit-specification-driven-development|GitHub Spec Kit Synthesis]] — same starting point (spec before code)
- PARALLELS: [[src-aidlc-aws-driven-development-lifecycle|AWS AI-DLC Synthesis]] — adjacent methodology
- BUILDS ON: [[src-caveman-prompt-output-compressor-julius-brussee|Caveman Synthesis]] — caveman-compress directly applicable to compress the Six-File context for ~46% input-token reduction
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — the six structured files program agent behavior more reliably than prose chat
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — `AGENTS.md` + numbered spec files + Code Rabbit + agent skills are infrastructure for AI-assisted delivery
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — every per-feature spec has a verification checklist
- DEMONSTRATES: [[never-skip-stages-even-when-told-to-continue|Never Skip Stages]] — fresh chat per feature + spec-checklist verification IS the discipline
- RELATES TO: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — Six-File methodology is agent-agnostic across 40+ agents; structured context is the vendor-neutral substrate
- RELATES TO: [[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]] — `ai-workflow-rules.md` parallels the operator's Markdown-rules-DSL concept (M002)
- RELATES TO: [[methodology-framework|Methodology Framework]] — Six-File pattern composes with the wiki's macro methodology engine
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]] — concrete pattern for solo/freelance project adoption

## Backlinks

[[Model — Markdown as IaC]]
[[CLAUDE.md Structural Patterns]]
[[Fowler SPDD Synthesis]]
[[BMAD Synthesis]]
[[OpenSpec Synthesis]]
[[GitHub Spec Kit Synthesis]]
[[AWS AI-DLC Synthesis]]
[[src-caveman-prompt-output-compressor-julius-brussee|Caveman Synthesis]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[Never Skip Stages]]
[[Anti-Vendor-Lock-In Lesson]]
[[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]]
[[methodology-framework|Methodology Framework]]
[[methodology-adoption-guide|Methodology Adoption Guide]]

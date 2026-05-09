---
title: "Spec-Driven Agentic Build Is the 2026 Convergent Pattern — Eight+ Independent Practitioners Treat Prompts/Specs/Contexts as Version-Controlled First-Class Artifacts (Not Ad-Hoc Chat)"
aliases:
  - "Spec-Driven Agentic Build Convergence"
  - "Prompts as Version-Controlled Artifacts"
  - "2026 Convergent Build Pattern"
  - "Structured Specs Beat Ad-Hoc Chat"
  - "First-Class Prompt Artifacts Lesson"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: seed
created: 2026-05-04
updated: 2026-05-04
last_reviewed: 2026-05-04
derived_from:
  - "Synthesis — Structured Prompt-Driven Development (SPDD) — Thoughtworks (Fowler)"
  - "Synthesis — JS Mastery Six-File Context System"
  - "Synthesis — BMAD-METHOD"
  - "Synthesis — OpenSpec Spec-Driven Development Framework"
  - "Synthesis — GitHub Spec Kit Specification-Driven Development"
  - "Synthesis — AWS AI-DLC AI-Driven Development Lifecycle"
  - "Synthesis — Karpathy's LLM Wiki Idea File (schema-as-product framing)"
  - "Synthesis — Cavekit v4 (Julius Brussee) — most distilled instance: 1 file + 3 commands + 2 skills"
sources:
  - id: fowler-spdd-synth
    type: wiki
    file: wiki/sources/wiki-methodology/src-fowler-structured-prompt-driven-development-spdd.md
    description: "Evidence 1 — Thoughtworks enterprise-IT instance: REASONS Canvas + workflow + closed-loop. Authored at Thoughtworks Global IT Services, used in production before public release 2026-04-28."
  - id: jsmastery-six-file-synth
    type: wiki
    file: wiki/sources/wiki-methodology/src-jsmastery-six-file-context-system-agentic-build.md
    description: "Evidence 2 — solo/freelance teaching instance: six context files + per-feature numbered specs. Demonstrated end-to-end in a 29-feature Ghost AI build (2026)."
  - id: bmad-synth
    type: wiki
    file: wiki/sources/src-bmad-method-agile-ai-development-framework.md
    description: "Evidence 3 — BMAD-METHOD framework instance: agile AI-driven development with personas + party mode + structured story-spec progression."
  - id: openspec-synth
    type: wiki
    file: wiki/sources/src-openspec-spec-driven-development-framework.md
    description: "Evidence 4 — OpenSpec lightweight spec-driven framework instance: solves the fundamental problem of agents losing context across sessions via specs as the persisted artifact."
  - id: spec-kit-synth
    type: wiki
    file: wiki/sources/src-github-spec-kit-specification-driven-development.md
    description: "Evidence 5 — GitHub's Spec Kit instance: Specification-Driven Development from the platform-vendor side; toolkit that operationalizes spec-first workflow."
  - id: aidlc-synth
    type: wiki
    file: wiki/sources/wiki-methodology/src-aidlc-aws-driven-development-lifecycle.md
    description: "Evidence 6 — AWS AI-DLC instance: AI-Driven Development Lifecycle methodology (not a tool, not a framework — a methodology). Cloud-vendor articulation of the same core."
  - id: karpathy-llm-wiki-synth
    type: wiki
    file: wiki/sources/wiki-methodology/src-karpathy-llm-wiki-idea-file.md
    description: "Evidence 7 — Karpathy's LLM Wiki Pattern: schema-as-the-real-product framing; the schema/spec is the durable artifact, content is generated from it. Foundational to the convergence."
  - id: cavekit-synth
    type: wiki
    file: wiki/sources/tools-integration/src-cavekit-spec-driven-development-claude-code-julius-brussee.md
    description: "Evidence 8 (added 2026-05-04) — Cavekit v4 (Julius Brussee): the most distilled instance documented. SPEC.md + 3 commands + 2 skills · caveman-encoded with mathematical-symbol vocabulary (→ ∴ ∀ ∃ ! ? ⊥ ≠ ∈ ∉ ≤ ≥ & |) · backprop reflex turns bugs into permanent §V invariants. The convergent pattern's minimum viable shape."
  - id: schema-is-the-real-product-lesson
    type: wiki
    file: wiki/lessons/03_validated/knowledge-systems/schema-is-the-real-product.md
    description: "Adjacent validated lesson — same structural insight applied to wiki construction; the schema file is the real product, content is generated from it"
  - id: structured-context-principle
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md
    description: "Parent principle (P2) — this lesson specializes P2 to the AI-assisted build context; the structured spec/prompt/canvas IS the structured context that programs agent behavior more reliably than ad-hoc chat"
  - id: markdown-as-iac-model
    type: wiki
    file: wiki/spine/models/agent-config/model-markdown-as-iac.md
    description: "Wiki model — the 7 evidence instances are all instantiations of Markdown-as-IaC at the project-build scale"
  - id: agent-must-practice-lesson
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/the-agent-must-practice-what-it-documents.md
    description: "Adjacent — this lesson is about the wiki itself instantiating the same convergent pattern (CLAUDE.md + AGENTS.md + .claude/rules/ + per-module specs in wiki/backlog/modules/ = the wiki's own version of Six-File + per-feature specs)"
tags: [lesson, layer-4, spec-driven, agentic-build, prompts-as-artifacts, version-controlled-specs, abstraction-first, alignment, iterative-review, closed-loop, fix-prompt-first, six-file-context, reasons-canvas, bmad, openspec, spec-kit, ai-dlc, karpathy, convergence, mission-2026-05-04, methodology-process]
---

# Spec-Driven Agentic Build Is the 2026 Convergent Pattern — Prompts/Specs/Contexts as Version-Controlled First-Class Artifacts

## Summary

By mid-2026, **at least eight independent practitioners** — spanning enterprise IT (Thoughtworks Global IT Services), large platform vendors (GitHub Spec Kit, AWS AI-DLC), independent frameworks (BMAD-METHOD, OpenSpec, Cavekit v4), foundational thinkers (Karpathy's LLM Wiki Pattern), and solo/freelance teachers (JS Mastery's Six-File Context System) — have converged on **the same core pattern** for building production-grade software with AI coding agents: **treat prompts, specs, and context files as first-class version-controlled artifacts**, not ad-hoc chat. Each instance differs in vocabulary (REASONS Canvas vs Six-File Context vs personas vs schema vs story specs) and scale (enterprise vs platform vs framework vs solo), but the underlying mechanism is consistent: **a structured Markdown artifact** is authored before any code, kept in version control, reviewed like code, and updated *first* when reality diverges (with code following). The agent reads the artifact before any work; the artifact is the boundary condition that makes AI output predictable instead of ad-hoc. Three core skills are named across multiple instances: **abstraction first** (design before generate), **alignment** (lock intent before write code), and **iterative review** (turn output into a controlled loop). The closed-loop discipline ("fix the prompt first, then the code") prevents prompt-and-code from silently diverging across iterations. The convergence is paper-evidenced and structurally robust: when seven independent attempts produce the same architecture, the pattern reflects a real constraint of agentic delivery, not a fashion. **For any production-grade AI-assisted build in 2026, the question is not *whether* to use this pattern, but *which instance* fits the workload class** — Six-File at solo/freelance scale, REASONS Canvas at enterprise scale, BMAD/OpenSpec/Spec-Kit/AI-DLC variants in between, with the Karpathy schema-as-product framing underneath all of them.

## Insight

> [!success] **Treat prompts/specs/contexts as version-controlled first-class artifacts. Not ad-hoc chat.**
>
> When building production-grade software with AI coding agents in 2026, **structured Markdown artifacts that the agent reads before any work** outperform ad-hoc chat by every measured dimension across at least 8 independent practitioner reports. The mechanism: the structured artifact gives the agent an *implementation boundary*, not just a goal — turning AI output from improvisation into predictable execution against a defined contract. Three disciplines compose the pattern:
>
> 1. **Abstraction first** — design before generate. Be clear about what objects exist, how they collaborate, and where the boundaries are. Otherwise the agent sprints on implementation details while the structure falls apart.
>
> 2. **Alignment** — lock intent before write code. Make "what we will do / what we won't do" explicit, and agree on standards and hard constraints up front. Otherwise: fast output, slow rework.
>
> 3. **Iterative review** — turn output into a controlled loop. AI assistance should behave like an engineering process, not a one-shot draft. Without disciplined review-and-iterate, teams either force the model to patch things until the solution drifts, or restart repeatedly losing control of cost and time.
>
> **Closed-loop sync rule** — when reality diverges, *fix the prompt/spec first, then update the code*. This rule (named explicitly in SPDD, implemented as `progress-tracker.md` updates in Six-File, and present in different vocabulary across the other 5 instances) prevents the artifact and the code from silently diverging across iterations.

> [!success] **Operator's 2026-05-05 doctrine denotation — 11 named impact areas (sacrosanct, verbatim)**
>
> Per [`raw/notes/2026-05-05-gitignore-audit-vendor-mapping-spec-driven-development.md`](../../../raw/notes/2026-05-05-gitignore-audit-vendor-mapping-spec-driven-development.md), operator-explicit Directive E (verbatim):
>
> > *"Its imporant to denote too if you had not already realized that we prone spec driven development and a strong methodology and standards. this make a huge difference in the executions and the outputs and the quality and reliability and tracability and operability and observability and project management and progress tracking and LLM Wiki enforment and compatibility exploitation."*
>
> Spec-driven development + strong methodology + standards is the project's **doctrine**, not just a preferred practice. Operator-named impact areas — each spec-driven discipline materially improves:
>
> | # | Impact area | Why spec-driven discipline materially improves this |
> |---|---|---|
> | 1 | **Executions** | Agent runs against an implementation boundary, not improvisation; predictable behavior per spec |
> | 2 | **Outputs** | Structured artifact constrains output shape; less drift, less rework |
> | 3 | **Quality** | Verification checklist per spec catches drift early; iterative review converges to spec |
> | 4 | **Reliability** | Closed-loop sync prevents spec/code divergence; same spec → same behavior across runs |
> | 5 | **Traceability** | Spec is version-controlled artifact; every behavior change has a spec change in git history |
> | 6 | **Operability** | Spec-realizers (install.sh, methodology engine, pipeline tooling) operationalize the spec deterministically |
> | 7 | **Observability** | Spec defines expected state; deviations from spec are observable signals |
> | 8 | **Project management** | Spec is the source of truth for scope; PM artifacts derive from spec, not vice-versa |
> | 9 | **Progress tracking** | Progress = "delivered against spec"; specs split workstreams, naturally tracked per artifact |
> | 10 | **LLM Wiki enforcement** | The wiki itself IS spec (methodology.yaml + wiki-schema.yaml + identity profiles); spec-discipline at the wiki layer makes the wiki authoritative for agent behavior |
> | 11 | **Compatibility exploitation** | Specs are vendor-neutral primitives; structured Markdown specs work across 40+ agents per Six-File evidence; anti-vendor-lock-in flows naturally from spec-discipline |
>
> **The doctrine compounds**: each impact area reinforces the others. Skipping spec-discipline at any layer reduces leverage at every layer. **This is why all 8+ practitioner instances converged on the same pattern** — the convergence is not stylistic; it's structurally driven by the impact-area compounding.

## Context

> [!info] **When this lesson applies — decision matrix**
>
> | Scenario | Apply the pattern? |
> |---|---|
> | **Production-grade AI-assisted build** that must survive multiple sessions | **YES** — without structured spec artifacts, the agent loses context within ~1 week (per JS Mastery's named failure mode) |
> | **Multi-feature build** with ≥10 numbered units of work | **YES** — per-feature numbered specs (Six-File pattern) + closed-loop sync (SPDD) is the convergent mechanism |
> | **Team-of-≥2 humans + AI agents** working on the same codebase | **YES** — version-controlled specs + reviews + sync discipline = the audit + handoff substrate |
> | **High-compliance / regulated domain** (financial, healthcare, infrastructure) | **YES** — REASONS Canvas-style governance dimensions (Norms + Safeguards) become non-negotiable |
> | **One-off prototype / weekend hack** | **NO** — overhead exceeds benefit; ad-hoc chat is fine |
> | **Pure exploratory spike** to validate an idea quickly | **NO** — SPDD's own fitness assessment rates this 2★; same applies broadly |
> | **Pure creative / visual / aesthetic work** | **NO** — taste-driven workloads don't fit logic-anchored spec discipline (per Fowler's fitness rating) |
> | **Context black hole** (domain poorly defined, business rules unclear) | **NO** — can't author a meaningful spec; pre-work is the conversation, not the spec |

The pattern is **scale-adaptive**: the same core mechanism works at solo/freelance scale (Six-File Context's 6 files + numbered feature specs), enterprise scale (Thoughtworks' SPDD with REASONS Canvas + `openspdd` CLI), platform scale (GitHub Spec Kit, AWS AI-DLC), and framework scale (BMAD, OpenSpec). The vocabulary differs; the structural constraint is identical.

## Evidence

> [!success]- **Evidence 1 — Thoughtworks SPDD: REASONS Canvas + workflow + closed-loop, in production at Thoughtworks Global IT Services (martinfowler.com 2026-04-28)**
>
> Per [Synthesis — Fowler SPDD](../../sources/wiki-methodology/src-fowler-structured-prompt-driven-development-spdd.md): Wei Zhang + Jessie Jie Xia author the **Structured Prompt-Driven Development** method based on Thoughtworks' internal practice. The method has two core components: (1) **REASONS Canvas** — 7-part structure (Requirements · Entities · Approach · Structure · Operations · Norms · Safeguards) that forces clarity from intent through governance before code is generated; (2) **SPDD workflow** — brings prompts into the same discipline as code (commit history · review · quality gates) with the explicit rule *"when reality diverges, fix the prompt first — then update the code."*  Ships as `openspdd` CLI with 7 commands. Authoring scale: Thoughtworks Global IT Services, used in production before public release. ROI claims: ~99% intent alignment between business logic and implementation in worked example. Three skills named explicitly: abstraction first, alignment, iterative review.

> [!success]- **Evidence 2 — JS Mastery Six-File Context System: 6 Markdown files + per-feature numbered specs, demonstrated in 29-feature Ghost AI build (2026)**
>
> Per [Synthesis — JS Mastery Six-File Context System](../../sources/wiki-methodology/src-jsmastery-six-file-context-system-agentic-build.md): Adrian Hajdin demonstrates a methodology centered on **six Markdown files** in a `context/` folder (`project-overview` · `architecture` · `code-standards` · `ai-workflow-rules` · `ui-context` · `progress-tracker`) wired by an `AGENTS.md` entry-point that reads them in load order before any work. Each feature is a numbered spec file (`NN-feature.md` in `context/feature-specs/`) with goal · design decisions · implementation · verification checklist; agent reads the spec, marks in-progress in progress-tracker, implements exactly, verifies, closes. Scale: solo/freelance + small-team + agent-agnostic across 40+ AI agents (`npx skills add`). Demonstrated end-to-end in a complete Ghost AI build with Next.js 16 + Live Blocks + Trigger Dev + Clerk + Prisma + Vercel Blob, ~29 numbered specs, deployed to production. Same three disciplines as SPDD: conversation-first (abstraction first) · scoped-units fresh-chat (alignment) · current-issues-md analyze-before-execute (iterative review).

> [!success]- **Evidence 3 — BMAD-METHOD: agile AI-driven framework with personas + structured story-spec progression**
>
> Per [Synthesis — BMAD-METHOD](../../sources/src-bmad-method-agile-ai-development-framework.md): "Build More Architect Dreams" is an open-source AI-driven agile framework that structures development around **structured story specs that progress through agentic personas** (party mode + role-specific agents). Different vocabulary than SPDD or Six-File — but the core mechanism is identical: structured Markdown story-spec artifacts drive the agent through a phased workflow; the spec is the version-controlled artifact; the agent implements against the spec, not against ad-hoc prompts.

> [!success]- **Evidence 4 — OpenSpec: lightweight spec-driven framework that explicitly solves the agent-context-loss problem**
>
> Per [Synthesis — OpenSpec](../../sources/src-openspec-spec-driven-development-framework.md): OpenSpec is a lightweight spec-driven development framework for AI coding assistants. The synthesis notes it **"solves the fundamental problem of agents losing context across sessions"** — the same failure mode Six-File's progress-tracker solves and SPDD's closed-loop sync solves. Different framing, same underlying constraint: structured persisted artifact = the substrate that survives across AI sessions where chat does not.

> [!success]- **Evidence 5 — GitHub Spec Kit: Specification-Driven Development from the platform-vendor side**
>
> Per [Synthesis — GitHub Spec Kit](../../sources/src-github-spec-kit-specification-driven-development.md): GitHub's **Specification-Driven Development** toolkit operationalizes spec-first workflow. Platform-vendor-scale instance — when GitHub itself ships tooling around the same core pattern, the convergence isn't fringe; it's becoming infrastructure.

> [!success]- **Evidence 6 — AWS AI-DLC: AI-Driven Development Life Cycle methodology (cloud-vendor scale)**
>
> Per [Synthesis — AWS AI-DLC](../../sources/wiki-methodology/src-aidlc-aws-driven-development-lifecycle.md): AWS Labs' **methodology** (explicitly NOT a tool, NOT a framework, NOT a service) for AI-driven development. Cloud-vendor articulation of the same core pattern from the cloud platform side. Uses different vocabulary again, but the structural insight is consistent: AI-driven delivery requires explicit lifecycle artifacts, not ad-hoc generation.

> [!success]- **Evidence 7 — Karpathy's LLM Wiki Pattern: schema-as-the-real-product framing (foundational)**
>
> Per [Synthesis — Karpathy's LLM Wiki Idea File](../../sources/wiki-methodology/src-karpathy-llm-wiki-idea-file.md) and the wiki's own validated lesson [Schema Is the Real Product](../../lessons/03_validated/knowledge-systems/schema-is-the-real-product.md): Karpathy identifies the schema file (CLAUDE.md / agent config) as the *real product*, with content generated from it. Predates SPDD + Six-File + the others, but is the foundational framing of the same convergence: the artifact is the version-controlled durable thing; the AI-generated content is downstream.

> [!success]- **Evidence 8 — Cavekit v4 (Julius Brussee, 2026): the most distilled instance — minimum viable shape of the convergent pattern**
>
> Per [Synthesis — Cavekit v4](../../sources/tools-integration/src-cavekit-spec-driven-development-claude-code-julius-brussee.md): Cavekit v4 is explicitly *"compressed spec-driven development for claude code — one file · three commands · zero sub-agents."* The entire surface is **`SPEC.md` at repo root** with **six fixed addressable sections** (§G goal · §C constraints · §I interfaces · §V invariants · §T tasks · §B bugs), three slash commands (`/ck:spec` · `/ck:build` · `/ck:check`), and two utility skills (`caveman` for encoding · `backprop` for bug-to-spec protocol). Caveman-encoded by default with mathematical-symbol vocabulary (→ ∴ ∀ ∃ ! ? ⊥ ≠ ∈ ∉ ≤ ≥ & |) for unambiguous machine-readable shorthand. The **backprop reflex** is structurally identical to the convergent pattern's closed-loop sync rule applied to bugs: every test failure or bug becomes a `§B` entry, and classes of bug become permanent `§V` invariants the spec never forgets — turning bugs into structural prevention rather than one-time fixes. **Cavekit v4 is also a meta-instance of the pattern** — the author distilled v3 (16 commands · 12 sub-agents · 21 skills · Go binary · autonomous loop · 4,977 LoC commands) down to v4 (3 commands · 0 sub-agents · 2 skills · 226 LoC commands) after concluding *"the spec is the only artifact that earns its tokens. Everything else that costs tokens must either save more tokens later, or the user's attention, or it gets cut."* This is the convergent pattern's **minimum viable shape** — empirical evidence that the irreducible kernel (durable spec artifact + 3 commands for create/build/check + closed-loop sync) is what earns its tokens; everything else was ceremony.

> [!info]- **Counter-evidence considered + rejected: ad-hoc-chat-only practitioners.**
>
> Many practitioners still use AI agents conversationally without structured spec artifacts. This is the **counter-pattern** the convergence is responding to. Common failure modes named explicitly in multiple sources: (a) "the agent forgets every decision after a week" (JS Mastery), (b) "ambiguous requirements become code quickly, and misunderstandings scale with them" (Fowler SPDD), (c) "you spend more time untangling AI mistakes than actually building" (JS Mastery), (d) "context windows degrade and the model contradicts itself" (OpenSpec). The seven evidence instances all explicitly name themselves as **the response to** ad-hoc chat failure. The convergence is structurally a refutation of ad-hoc-chat-only practice for production-grade work.

## Applicability

> [!info] **The pattern is scale-adaptive — pick the instance that fits the workload class**
>
> | Scale | Instance | Why |
> |---|---|---|
> | **Solo / freelance / small team** | [Six-File Context System](../../sources/wiki-methodology/src-jsmastery-six-file-context-system-agentic-build.md) | 6 markdown files + numbered feature specs · agent-agnostic (40+ agents via `npx skills`) · low setup cost · directly applicable today |
> | **Enterprise IT / regulated domains** | [SPDD with REASONS Canvas](../../sources/wiki-methodology/src-fowler-structured-prompt-driven-development-spdd.md) | 7-dimension governance canvas · `openspdd` CLI · closed-loop sync · designed for compliance + auditability |
> | **Multi-platform vendor coordination** | [GitHub Spec Kit](../../sources/src-github-spec-kit-specification-driven-development.md) | Platform-vendor toolkit · operationalized spec-first workflow |
> | **Cloud-vendor delivery org** | [AWS AI-DLC](../../sources/wiki-methodology/src-aidlc-aws-driven-development-lifecycle.md) | Cloud-org methodology framing · lifecycle artifact discipline |
> | **Agile-team adoption with role separation** | [BMAD-METHOD](../../sources/src-bmad-method-agile-ai-development-framework.md) | Personas + party mode + story-spec progression · agile cycle integration |
> | **Spec-first lightweight independence** | [OpenSpec](../../sources/src-openspec-spec-driven-development-framework.md) | Minimum-viable spec-driven framework · solves agent-context-loss directly |
> | **Foundational schema-as-product** | [Karpathy LLM Wiki Pattern](../../sources/wiki-methodology/src-karpathy-llm-wiki-idea-file.md) | The underlying pattern: schema/agent-config IS the durable product |
> | **Minimum viable shape — solo Claude Code projects** | [Cavekit v4 (Julius Brussee)](../../sources/tools-integration/src-cavekit-spec-driven-development-claude-code-julius-brussee.md) | One file (SPEC.md) · 3 commands · 2 skills · §-addressable sections · backprop reflex. The most distilled instance documented; carries an empirical lesson on what's load-bearing vs ceremony (v3 → v4 distillation). |
> | **Skill-as-spec evolution — Claude Code workflows** *(NEW 2026-05-08, 9th instance)* | [Claude Code Skill Chaining V1→V2 (2026)](../../sources/tools-integration/src-claude-code-skill-chaining-fork-files-commands-85-percent-less-context.md) | Skill markdown IS the spec; V1 monolith refactored into V2 (orchestrator + sub-skills + temp-directory file handoff + `!` parse-time substitution) per the same closed-loop discipline. The author treated the skill spec as the durable artifact and refactored toward token efficiency — empirical 85% reduction (51K → 5-8K). Demonstrates the convergent pattern at the **skill / workflow** layer (sister to Cavekit's command/skill layer). |
>
> All 9 instances are interchangeable in core constraint; they're optimized for different team sizes, governance needs, and tooling preferences. **Pick by workload fit, not by vendor preference.** The structural insight is invariant.

## How to Apply

> [!tip] **Concrete adoption checklist for any production-grade AI-assisted build**
>
> 1. **Pick the instance** matching your scale (table above). For solo/freelance, default to Six-File. For enterprise IT, default to SPDD. For agile teams with persona separation, default to BMAD. For cloud-vendor delivery orgs, default to AI-DLC.
>
> 2. **Author the structured artifacts** before writing any code:
>    - Project-level: project-overview · architecture · ui-context · code-standards · workflow-rules · progress-tracker (Six-File pattern), or REASONS Canvas (SPDD), or equivalent in your chosen instance
>    - Per-feature: numbered spec file with goal · design decisions · implementation · verification checklist
>
> 3. **Wire the entry-point file** the agent reads at session start: `AGENTS.md` (universal) · `CLAUDE.md` (Claude Code) · `GEMINI.md` (Gemini) · `.cursor/rules/` (Cursor) · `.windsurf/rules/` (Windsurf) · `.clinerules/` (Cline) · `.github/copilot-instructions.md` (Copilot). The entry-point file lists the artifact files in load order with explicit instructions to read them before any work.
>
> 4. **Per-feature workflow**:
>    - Open fresh chat in your agent
>    - Tell the agent: *"Read [this feature spec], update the progress tracker, implement exactly as specified."*
>    - Agent reads spec → reads context files → marks in-progress → implements → verifies against checklist → closes unit
>    - Operator reviews → push to development branch → PR + review (e.g., Code Rabbit) → merge to main
>
> 5. **Practice the closed-loop discipline** when reality diverges:
>    - **Logic correction** (changes observable behavior): update the prompt/spec FIRST, then re-generate code
>    - **Refactoring** (no observable behavior change): refactor code FIRST, then sync to update the spec
>
> 6. **Install official agent skills** for external services in your stack (`npx skills add <pkg>`) so the agent has up-to-date API knowledge — critical when frameworks evolve faster than agent training data
>
> 7. **For errors**: author a debug context file (e.g., `current-issues.md`) with paste of error + context; ask agent to *analyze and propose* before executing; reject the analysis if it's wrong; gitignore or delete the file before commit
>
> 8. **Keep the progress-tracker (or equivalent) updated constantly** — it's the only artifact that changes through the build; it's how a fresh session in 6 months picks up where left off in a single prompt

> [!warning] **Anti-patterns to avoid**
>
> - **Ad-hoc chat only** — produces the failure modes the convergence is responding to (agent context loss, ambiguous requirements becoming code, untangling AI mistakes)
> - **Spec authored once, never updated** — pure SDD without sync discipline; specs and code drift; agent re-improvises on every session
> - **Spec without verification checklist** — done-when becomes ambiguous; agent decides what "complete" means
> - **Combined unrelated concerns in one feature spec** — agent has too much surface area to make assumptions across; split into focused units
> - **Pure imitation without conversation** — copying templates without doing the architectural conversation produces shallow specs; the conversation IS the work

## Open Questions

> [!question] How do the instances interoperate in mixed-scale orgs?
> An enterprise IT team using SPDD might have solo/contractor sub-teams using Six-File. The two patterns share core but differ in artifact granularity. Empirical interop documentation would close a real gap.

> [!question] Where does this lesson cross with the wiki's own self-application?
> The wiki itself instantiates the pattern: AGENTS.md + CLAUDE.md + .claude/rules/ + per-module specs in wiki/backlog/modules/ = the wiki's own version of the convergent pattern. The wiki is part of the convergence, not just a documenter of it. Worth explicit cross-reference in the methodology adoption guide.

> [!question] When does the pattern fail or hit diminishing returns?
> SPDD's fitness rating gives 1-2★ scenarios (context black holes, exploratory spikes, creative work) where the pattern doesn't pay off. Empirical edge-case documentation across the seven instances would sharpen the applicability boundary.

> [!question] Does the pattern compose with the trust-layer concept?
> The [Trust-Layer Epic](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md)'s M002 (Markdown rule DSL) is a parallel: runtime contract declared in Markdown, enforced by Python in isolated mode. The Six-File `ai-workflow-rules.md` is the closest existing instance. Interesting research: can the trust-layer's runtime-contract rules be authored as one of the Six-File files? Would the operator's tamper-proof inference inherit the Six-File pattern naturally?

> [!question] Caveman-compress applied to the spec artifacts — empirical compression ratio?
> [Caveman](../../sources/tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md)'s `caveman-compress` reports ~46% reduction on memory files. The spec artifacts (CLAUDE.md / context files / per-feature specs) are exactly the kind of memory file caveman-compress targets. Empirical validation would close a real gap and connect this lesson to the wiki's compression evidence chain.

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself before opening an AI agent for a production-grade build:
>
> 1. **Have I authored a structured spec artifact?** Or am I about to ad-hoc-chat? If chat, you're about to hit the failure modes the convergence is responding to.
> 2. **Does the spec have a verification checklist?** Without it, "done" is ambiguous and the agent decides.
> 3. **Is the spec in version control?** If it's in chat, it's gone next session.
> 4. **Will I update the spec FIRST when reality diverges?** Or am I about to "just fix the code" — letting prompt and code silently drift apart?
> 5. **Have I picked the right instance for my scale?** Solo with REASONS Canvas is overkill; enterprise with chat-only is malpractice. Match the instance to the workload class.
> 6. **Did I do the conversation FIRST?** The conversation is the work. Skipping it produces shallow specs.

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The principle this specializes** | [[structured-context-governs-agent-behavior-more-than-content\|Principle 2 — Structured Context Governs Agent Behavior]] |
> | **The model that names the substrate** | [[model-markdown-as-iac\|Model — Markdown as IaC]] |
> | **The seven evidence instances** | (See Evidence section above) |
> | **The validated foundational lesson** | [[schema-is-the-real-product\|Schema Is the Real Product — Not the Content]] |
> | **The wiki's own self-application** | [[the-agent-must-practice-what-it-documents\|The Agent Must Practice What It Documents]] |
> | **Where this lesson would feed forward** | [[methodology-adoption-guide\|Methodology Adoption Guide]] · [[methodology-framework\|Methodology Framework]] |

## Relationships

- DERIVED FROM: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior More Than Content]] (specializes P2 to the AI-assisted production-build context)
- BUILDS ON: [[src-fowler-structured-prompt-driven-development-spdd|Fowler SPDD Synthesis]] · [[src-jsmastery-six-file-context-system-agentic-build|JS Mastery Six-File Synthesis]] · [[src-bmad-method-agile-ai-development-framework|BMAD Synthesis]] · [[src-openspec-spec-driven-development-framework|OpenSpec Synthesis]] · [[src-github-spec-kit-specification-driven-development|GitHub Spec Kit Synthesis]] · [[src-aidlc-aws-driven-development-lifecycle|AWS AI-DLC Synthesis]] · [[src-karpathy-llm-wiki-idea-file|Karpathy LLM Wiki Synthesis]]
- BUILDS ON: [[model-markdown-as-iac|Model — Markdown as IaC]] (the substrate the seven evidence instances all instantiate)
- BUILDS ON: [[schema-is-the-real-product|Schema Is the Real Product]] (foundational validated lesson with the same structural insight)
- PARALLELS: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] (sibling Layer-4 lesson with multi-source convergence as the empirical mechanism)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] (the structured artifact + entry-point file + verification checklist + closed-loop sync are infrastructure, not prose policy)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] (every spec has a verification checklist; the agent's "done" is gated on the checklist)
- RELATES TO: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] (the wiki itself instantiates the pattern at the wiki-build scale)
- RELATES TO: [[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]] (the trust-layer M002 Markdown-rules-DSL parallels the convergent pattern's `ai-workflow-rules.md`)
- RELATES TO: [[src-caveman-prompt-output-compressor-julius-brussee|Caveman Synthesis]] (caveman-compress directly applicable to the spec artifacts for ~46% input compression)
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]] (concrete pattern for any project's adoption of the wiki's methodology)
- FEEDS INTO: [[methodology-framework|Methodology Framework]] (this convergent pattern is a candidate document type for design/scaffold stages of the existing methodology engine)

## Backlinks

[[Principle 2 — Structured Context Governs Agent Behavior More Than Content]]
[[Fowler SPDD Synthesis]]
[[Model — Markdown as IaC]]
[[Schema Is the Real Product]]
[[Anti-Vendor-Lock-In Lesson]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
[[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]]
[[src-caveman-prompt-output-compressor-julius-brussee|Caveman Synthesis]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[methodology-framework|Methodology Framework]]

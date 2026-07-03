---
title: "Synthesis — Structured Prompt-Driven Development (SPDD): Thoughtworks' REASONS Canvas + Workflow for Governable AI-Assisted Delivery (Wei Zhang + Jessie Jie Xia, martinfowler.com 2026-04-28)"
aliases:
  - "SPDD"
  - "Structured Prompt-Driven Development"
  - "REASONS Canvas"
  - "Fowler SPDD"
  - "Thoughtworks SPDD"
  - "openspdd"
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
  - id: fowler-spdd-article
    type: documentation
    url: https://martinfowler.com/articles/structured-prompt-driven/
    file: raw/articles/structured-prompt-driven-development-spdd.md
    title: "Structured Prompt-Driven Development (SPDD) — martinfowler.com 2026-04-28"
    description: "Authoritative source — Wei Zhang (AI-assisted delivery expert at Thoughtworks) + Jessie Jie Xia (Global CIO at Thoughtworks). Full method walkthrough with billing-engine example."
    ingested: 2026-05-04
  - id: spec-kit-synth
    type: wiki
    file: wiki/sources/src-github-spec-kit-specification-driven-development.md
    description: "Adjacent — GitHub's Spec Kit implements pure spec-driven development (SDD); SPDD adds workflow + REASONS Canvas + sync discipline on top of the same starting point"
  - id: openspec-synth
    type: wiki
    file: wiki/sources/src-openspec-spec-driven-development-framework.md
    description: "Adjacent — OpenSpec is another spec-driven framework for AI coding assistants; SPDD's REASONS Canvas is one canonical structure for the spec artifact OpenSpec produces"
  - id: bmad-synth
    type: wiki
    file: wiki/sources/src-bmad-method-agile-ai-development-framework.md
    description: "Adjacent — BMAD-METHOD overlaps in framing prompts as governable artifacts but uses different abstractions (party mode / personas) instead of REASONS Canvas"
  - id: aidlc-synth
    type: wiki
    file: wiki/sources/wiki-methodology/src-aidlc-aws-driven-development-lifecycle.md
    description: "Adjacent — AWS AI-DLC is a parallel methodology framing AI-driven delivery; SPDD is a more concrete workflow + canvas instantiation"
  - id: markdown-as-iac-model
    type: wiki
    file: wiki/spine/models/agent-config/model-markdown-as-iac.md
    description: "Wiki model — SPDD is a strong instantiation of Markdown-as-IaC at the project-delivery scale: the structured prompt IS the binding configuration kept in version control"
  - id: jsmastery-six-file
    type: wiki
    file: wiki/sources/wiki-methodology/src-jsmastery-six-file-context-system-agentic-build.md
    description: "Sibling — independent practitioner's instantiation of the same core pattern at solo/freelance scale (Six-File Context System). SPDD ↔ Six-File Context = enterprise vs solo convergence on the same core."
tags: [source-synthesis, spdd, structured-prompt-driven, reasons-canvas, thoughtworks, fowler, prompts-as-artifacts, spec-driven, openspdd, governance, ai-assisted-delivery, methodology, layer-1, paper-evidence, mission-2026-05-04]
---

# Synthesis — Structured Prompt-Driven Development (SPDD)

## Summary

Structured Prompt-Driven Development (SPDD) is a Thoughtworks-authored engineering method (Wei Zhang + Jessie Jie Xia, martinfowler.com 2026-04-28) for AI-assisted delivery in which **prompts are first-class delivery artifacts** — version-controlled, reviewed, reused, and improved alongside the code. The method has two core components: the **REASONS Canvas** (a 7-part structure spanning Requirements · Entities · Approach · Structure · Operations · Norms · Safeguards) that forces clarity from intent through governance before code is generated; and the **SPDD workflow** that brings prompts into the same discipline as code (commit history, review, quality gates) with the rule *"when reality diverges, fix the prompt first — then update the code."* The workflow ships as `openspdd`, a CLI with 7 commands (`/spdd-story`, `/spdd-analysis`, `/spdd-reasons-canvas`, `/spdd-generate`, `/spdd-api-test`, `/spdd-prompt-update`, `/spdd-sync`) that turn business input → abstraction → execution → validation → release into a closed loop where prompt assets and code evolve together. Three core skills make practitioners effective: **abstraction first** (design before generate), **alignment** (lock intent before write code), and **iterative review** (turn output into a controlled loop). Best-fit scenarios (5★): scaled standardized delivery + high-compliance environments. Worst-fit (1★): context black holes + creative/visual work. Authored at Thoughtworks Global IT Services where it's been used in production; extends but does not replace spec-driven development (SDD) by treating structured prompts as governed reusable team assets that **evolve alongside the code** — a "spec-anchored approach" per Birgitta Böckeler.

## Reference Card

> [!info] SPDD reference card

| Field | Value |
|---|---|
| **Authors** | Wei Zhang (AI-assisted delivery expert, Thoughtworks) + Jessie Jie Xia (Global CIO, Thoughtworks) |
| **Source** | [martinfowler.com/articles/structured-prompt-driven](https://martinfowler.com/articles/structured-prompt-driven/) |
| **Published** | 2026-04-28 |
| **Origin** | Thoughtworks Global IT Services (internal IT organization) — used by their teams in production before public release |
| **Tooling** | `openspdd` CLI — implements the 7 SPDD commands as repeatable steps |
| **Worked example** | Billing engine enhancement (multi-plan billing + model-aware pricing + split-rate billing); full code on GitHub |
| **Three core skills** | abstraction first · alignment · iterative review |
| **Closed-loop principle** | When reality diverges, **fix the prompt first** — then update the code |
| **Relationship to SDD** | Extends — SPDD adds workflow + REASONS Canvas + sync discipline on top of "write the spec first." Per Birgitta Böckeler: a "spec-anchored approach." |
| **License / cost** | Free — `openspdd` is open-source CLI |
| **Mission relevance** | Strong — SPDD treats prompts as version-controlled team assets, directly supporting the wiki's [Markdown-as-IaC](../../spine/models/agent-config/model-markdown-as-iac.md) model and the principle that structured context governs agent behavior |

## Key Insights

> [!success] **The REASONS Canvas — 7-part structure that moves uncertainty left.**
>
> | Letter | Dimension | Concern |
> |---|---|---|
> | **R** | Requirements | What problem are we solving, and what is DoD? |
> | **E** | Entities | Domain entities and relationships |
> | **A** | Approach | The strategy of how we'll meet the requirements |
> | **S** | Structure | Where the change fits in the system; components and dependencies |
> | **O** | Operations | Break the abstract strategy into concrete, testable implementation steps |
> | **N** | Norms | Cross-cutting engineering norms (naming, observability, defensive coding, etc.) |
> | **S** | Safeguards | Non-negotiable boundaries (invariants, performance limits, security rules, etc.) |
>
> Abstract parts (R, E, A, S — intent + design) → Specific parts (O — execution) → Common standards (N, S — governance). The canvas aligns intent and boundaries before code is generated; reviewers reason about a single artifact instead of scattered chat logs and partial diffs.

> [!success] **Prompts as first-class delivery artifacts — version controlled, reviewed, reused.**
>
> SPDD treats structured prompts the way other artifacts are treated: commit history · code review · quality gates. Reviews shift from "spot the bug" toward "check the intent." Successful patterns accumulate into a reusable prompt library that supports AI-First Software Delivery (AIFSD). Domain knowledge and design decisions compound across iterations; variability across the team decreases.

> [!info] **The 7 openspdd commands — repeatable workflow steps.**
>
> | Command | Type | Purpose |
> |---|---|---|
> | `/spdd-story` | Optional | Breaks a large requirement into independent INVEST user stories (1–5 days of work each) |
> | `/spdd-analysis` | Core | Extracts domain keywords from requirements, scans relevant code, produces strategic analysis covering domain concepts, risks, and design direction |
> | `/spdd-reasons-canvas` | Core | Generates the full REASONS Canvas — an executable blueprint from high-level rationale down to method-level operations |
> | `/spdd-generate` | Core | Reads the Canvas and generates code task by task, strictly following the operations, norms, and safeguards defined in the prompt |
> | `/spdd-api-test` | Optional | Generates a cURL-based API test script with structured test cases (normal, boundary, error scenarios) |
> | `/spdd-prompt-update` | Core | Incrementally updates the Canvas when requirements change (requirements → prompt → code) |
> | `/spdd-sync` | Core | Synchronizes code-side changes (refactoring, fixes) back into the Canvas (code → prompt) |

> [!info] **Closed-loop principle — two responses to code-review changes.**
>
> | Change type | Strategy | Mechanism |
> |---|---|---|
> | **Logic correction** (changes observable behavior) | Update the prompt FIRST, then generate code | `/spdd-prompt-update` → `/spdd-generate` |
> | **Refactoring** (no observable behavior change) | Refactor the code FIRST, then sync back to the prompt | direct refactor → `/spdd-sync` |
>
> "When reality diverges, fix the prompt first — then update the code." This rule prevents prompt and code from silently drifting apart across iterations.

> [!info] **Three core skills that determine SPDD effectiveness.**
>
> | Skill | What it requires |
> |---|---|
> | **Abstraction first — design before you generate** | Be clear about what objects exist, how they collaborate, and where the boundaries are. Without that, AI sprints on implementation details while the structure falls apart. |
> | **Alignment — lock intent before you write code** | Make "what we will do / what we won't do" explicit, and agree on the standards and hard constraints up front. Otherwise: fast output and slow rework. |
> | **Iterative review — turn output into a controlled loop** | AI assistance should behave like an engineering process, not a one-shot draft. Without a disciplined review-and-iterate loop, teams force the model to patch things until the solution drifts, or restart repeatedly losing control of cost and time. |

> [!warning] **Fitness assessment — where SPDD pays off and where it doesn't.**
>
> | Rating | Scenario |
> |---|---|
> | ★★★★★ | **Scaled, standardized delivery** — high-repeat business logic that needs long-term maintainability (many similar APIs, automating core business workflows) |
> | ★★★★★ | **High compliance + hard constraints** — financial core systems, multi-channel/multi-client deployments, strict architectural rules |
> | ★★★★☆ | **Team collaboration + auditability** — multi-person delivery where changes must be fully traceable end-to-end |
> | ★★★★☆ | **Cross-cutting consistency work** — complex refactors where logic must stay tightly synchronized across multiple microservices or different languages |
> | ★★☆☆☆ | **Firefighting hotfixes** — speed > architectural discipline |
> | ★★☆☆☆ | **Exploratory spikes** — validating ideas, not shipping production |
> | ★★☆☆☆ | **One-off scripts** — disposable cleanup; SPDD's upfront cost is too high |
> | ★☆☆☆☆ | **Context black holes** — domain poorly defined, business rules unclear; can't set meaningful boundaries for the model |
> | ★☆☆☆☆ | **Pure creative / visual work** — taste-driven (UI exploration, marketing copy) |

> [!info] **What SPDD adds to spec-driven development (SDD).**
>
> SDD and SPDD share the starting point: generate a spec before generating code. SPDD adds:
>
> - **Method for how the spec is produced, reviewed, and kept in sync with the code.** The prompt is a maintained artifact, not generated once and discarded.
> - **From requirements to engineering spec.** The REASONS Canvas captures chosen approach, system structure, engineering norms, and safeguards — giving the LLM an *implementation boundary*, not just a goal.
> - **Sync, not handoff.** Prompt and code stay synchronized. Changes on either side are reflected back; intent and implementation do not drift apart.
> - **Repeatable team control.** A consistent way for teams to govern AI output and carry decisions forward across iterations.

## Workflow — Concrete Example: Billing Engine Enhancement

Per the Fowler article's worked example (a billing engine being enhanced to support multi-plan model-aware pricing):

> [!example] 6-step SPDD workflow walkthrough
>
> 1. **Create initial requirements** (`/spdd-story`) — split into INVEST user stories with acceptance criteria in Given/When/Then format
> 2. **Clarify analysis** — review the user story; align with BA/PO if business-level issues; break down along core logic, scope boundaries, and definition of done
> 3. **Generate analysis context** (`/spdd-analysis`) — extracts domain keywords from requirements, scans relevant code, produces strategic analysis (domain concepts · strategic approach · risks & gaps)
> 4. **Generate structured prompt** (`/spdd-reasons-canvas`) — generates the full REASONS Canvas as executable blueprint; review intent alignment from global perspective before getting lost in details
> 5. **Generate code** (`/spdd-generate`) — reads Canvas, generates code task by task following operations + norms + safeguards. Two responses to code review:
>    - **Logic correction** → `/spdd-prompt-update` then `/spdd-generate`
>    - **Refactoring** → refactor code, then `/spdd-sync` to update Canvas
> 6. **Generate unit tests** — currently uses a template-driven approach with shared test prompt template; dedicated testing commands planned

The article reports the worked example delivered: **~99% intent alignment** between business logic and implementation · complete engineering transparency · structured prompt asset tightly synchronized with current codebase · compounding human expertise across iterations.

## Return on Investment + Upfront Cost

> [!info] ROI and cost framing per the Fowler article

| Benefit | Impact | Speed | What you get |
|---|---|---|---|
| **Determinism** | High | Immediate | Encode logic in precise spec, significantly reduces hallucination and "creative" interpretation |
| **Traceability** | High | Immediate | Every meaningful change traces back to the structured prompt, closing the audit loop |
| **Faster reviews** | High | Short-term | Code "arrives" closer to team standards; reviews focus on logic/design, not formatting/cleanup |
| **Explainability** | Medium-High | Gradual | Intent and behavior visible at the natural-language level, lowering cognitive load |
| **Safer evolution** | High | Long-term | Well-defined boundaries + stepwise implementation = lower-risk targeted changes |

| Cost | Barrier | Nature |
|---|---|---|
| **Mindset shift** | High | Ongoing training — teams adapt to "design first" rather than "code first" |
| **Senior expertise up front** | Medium-High | Per-feature — engineers who can translate business rules into clean abstractions and design constraints |
| **Automation tooling** | Medium | Infrastructure setup — without `openspdd` or equivalent, SPDD hits a throughput ceiling |

Future direction (per article close): "breaking the expert-only barrier" — making complex business rules and design constraints more machine-readable and intelligent so they can be applied consistently without relying on individual intuition. Goal: SPDD should depend less on personal craftsmanship and more on a mature organization-level asset system.

## Mission Alignment

SPDD is a **strong instantiation of [Markdown-as-IaC](../../spine/models/agent-config/model-markdown-as-iac.md)** at the project-delivery scale. The structured prompt IS the binding configuration: version-controlled, reviewed, executed by `openspdd`, kept in sync with code through the closed-loop principle. SPDD is also the **enterprise-scale convergent instance** of the same core pattern that JS Mastery's [Six-File Context System](src-jsmastery-six-file-context-system-agentic-build.md) implements at solo/freelance scale — both treat AI-readable Markdown specs as the artifact that survives across sessions, both enforce abstraction-first + alignment + iterative review, both prevent the "AI agent forgets every decision after a week" failure mode through external structured artifacts.

Per [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in lesson]], SPDD is also LLM-vendor-neutral by design: the article notes Thoughtworks used Claude 4.5 Sonnet, Claude 4.6 Opus, Gemini 3.1 Pro, and ChatGPT 5.4 in shaping the article itself. The structured prompt is the substrate; the LLM is interchangeable.

Per [Three Classes of Methodology Output](../../lessons/03_validated/methodology-process/three-classes-of-methodology-output.md), the REASONS Canvas is a **document** (binding constraint on future work), not just documentation — distinguishing it from descriptive prompt-engineering content.

## Open Questions

> [!question] How does SPDD's REASONS Canvas compose with the wiki's existing methodology engine?
> The wiki has methodology.yaml with 9 models (feature-development, bug-fix, research, integration, etc.) and 5 universal stages. REASONS Canvas could be one canonical structure for the documents the existing models produce at design/scaffold stages — or a parallel layer. Operator design call.

> [!question] Does the closed-loop "fix prompt first" principle apply outside enterprise IT?
> The Thoughtworks worked example is a billing-engine enhancement (high logic, hard compliance). The 5★ fitness rating is for that exact scenario class. For other classes (creative work, exploratory spikes), the closed-loop discipline is rated lower — but solo/small-team practitioners (per JS Mastery's parallel methodology) report similar discipline working at smaller scale. Worth empirical comparison.

> [!question] How does `openspdd` interoperate with existing harness tools (Claude Code, OpenCode, Codex, etc.)?
> The Fowler article describes SPDD as harness-agnostic in principle but documents only the `openspdd` CLI interface. Concrete integration paths (Claude Code skills · Codex plugins · OpenCode commands) are not yet documented in the article.

> [!question] Where do REASONS Canvas + 6-file context (JS Mastery) interoperate or diverge?
> See the [Six-File Context System synthesis](src-jsmastery-six-file-context-system-agentic-build.md) for the parallel methodology. Both treat Markdown specs as version-controlled artifacts; SPDD's REASONS Canvas is per-feature, JS Mastery's six files are per-project. They could compose: six files for project-level context, REASONS Canvas for per-feature spec.

## How to Apply

> [!tip] Adoption checklist (when SPDD fits the workload class)
>
> 1. **Confirm fitness** — work falls in 4★+ class (scaled standardized delivery, high compliance, team collaboration auditability, or cross-cutting consistency work)
> 2. **Install `openspdd`** — the open-source CLI implements the 7 commands; without it, SPDD hits a throughput ceiling
> 3. **Author the first REASONS Canvas** for a real feature using `/spdd-reasons-canvas` after `/spdd-analysis`
> 4. **Establish the closed-loop discipline** — "fix prompt first" for logic corrections, refactor first then `/spdd-sync` for clean-code work
> 5. **Build the prompt library** — successful Canvases become reusable assets across iterations and team members
> 6. **Audit ROI** at 30/60/90 days — determinism · traceability · faster reviews · explainability · safer evolution

## Relationships

- BUILDS ON: [[model-markdown-as-iac|Model — Markdown as IaC]] — SPDD is the enterprise-scale instantiation
- BUILDS ON: [[src-github-spec-kit-specification-driven-development|GitHub Spec Kit Synthesis]] — same starting point (spec before code); SPDD adds workflow + Canvas + sync discipline
- BUILDS ON: [[src-openspec-spec-driven-development-framework|OpenSpec Synthesis]] — adjacent spec-driven framework
- BUILDS ON: [[src-bmad-method-agile-ai-development-framework|BMAD Synthesis]] — parallel framing of prompts as governed artifacts
- BUILDS ON: [[src-aidlc-aws-driven-development-lifecycle|AWS AI-DLC Synthesis]] — parallel methodology with different abstractions
- PARALLELS: [[src-jsmastery-six-file-context-system-agentic-build|JS Mastery Six-File Context System Synthesis]] — sibling instance of the same core pattern at different scale (enterprise-IT vs solo/freelance)
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — REASONS Canvas IS structured context as proto-programming
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — `openspdd` CLI enforces the workflow as infrastructure, not prose policy
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — every Canvas claim is verified by `/spdd-generate` + `/spdd-api-test` execution
- RELATES TO: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — SPDD is LLM-vendor-neutral; the structured prompt substrate works across Claude, Gemini, GPT
- FEEDS INTO: [[methodology-framework|Methodology Framework]] — REASONS Canvas is a candidate document type for design/scaffold stages of the existing methodology engine
- FEEDS INTO: [[model-methodology|Model — Methodology]] — closed-loop "fix prompt first" principle is a candidate addition to the methodology's stage-gate discipline

## Backlinks

[[Model — Markdown as IaC]]
[[GitHub Spec Kit Synthesis]]
[[OpenSpec Synthesis]]
[[BMAD Synthesis]]
[[AWS AI-DLC Synthesis]]
[[JS Mastery Six-File Context System Synthesis]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[Anti-Vendor-Lock-In Lesson]]
[[methodology-framework|Methodology Framework]]
[[model-methodology|Model — Methodology]]

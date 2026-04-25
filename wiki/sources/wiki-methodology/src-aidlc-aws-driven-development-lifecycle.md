---
title: "Synthesis — AWS AI-DLC: AI-Driven Development Lifecycle (Methodology, Not a Tool)"
aliases:
  - "Synthesis — AI-DLC"
  - "AWS AI-DLC Methodology"
type: source-synthesis
domain: wiki-methodology
status: synthesized
confidence: high
maturity: seed
created: 2026-04-25
updated: 2026-04-25
layer: 1
sources:
  - id: src-awslabs-aidlc-workflows
    type: documentation
    url: https://github.com/awslabs/aidlc-workflows
    file: raw/articles/awslabsaidlc-workflows.md
    title: "awslabs/aidlc-workflows — AI-Driven Development Life Cycle"
    ingested: 2026-04-24
  - id: aidlc-method-paper
    type: documentation
    url: https://prod.d13rzhkk8cj2z0.amplifyapp.com/
    title: "AI-DLC Method Definition Paper"
  - id: aidlc-blog
    type: article
    url: https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/
    title: "AI-Driven Development Life Cycle (AWS Blog)"
tags: [synthesis, aidlc, aws-labs, methodology, three-phase-workflow, inception-construction-operations, multi-platform, methodology-first, agent-agnostic, vision-document, technical-environment-document, never-vibe-code, question-answer-flow, opt-in-extensions, audit-trail, methodology-comparison, mit-0]
---

# Synthesis — AWS AI-DLC: AI-Driven Development Lifecycle

## Summary

**AI-DLC** (AI-Driven Development Life Cycle) is AWS Labs' open-source **methodology** — explicitly NOT a tool, NOT an installable package — for guiding AI coding agents through structured software development. It ships as **markdown rule files** (`aidlc-rules/aws-aidlc-rules/core-workflow.md` + `aws-aidlc-rule-details/{common,inception,construction,extensions,operations}/`) that any agent (Kiro / Amazon Q / Cursor / Cline / Claude Code / GitHub Copilot / OpenAI Codex / any AGENTS.md-aware tool) loads as project rules. Three-phase adaptive workflow: **Inception (WHAT/WHY) → Construction (HOW) → Operations (deploy/monitor — future)**. Five tenets prioritize **methodology-first**, **no duplication**, **reproducible**, **agnostic**, and **human-in-the-loop**. The interaction protocol is distinctive: **questions go into markdown files** (with `[Answer]:` tags and multiple-choice format), context clears at every gate (not compacted), and the "Never Vibe Code" rule mandates updating design documents BEFORE regenerating code. License MIT-0. **Mission-relevant for this wiki:** AIDLC is the closest peer methodology to our own — comparing the two reveals structural lessons in both directions.

> [!info] Source Reference
> | Attribute | Value |
> |---|---|
> | Source | github.com/awslabs/aidlc-workflows |
> | Type | GitHub repository (deep fetch — README + 30 key files) |
> | License | MIT-0 |
> | Maintainer | AWS Labs |
> | Distribution | GitHub Releases (zipped `aidlc-rules-v<N>.zip`) |
> | Trigger | "Using AI-DLC, ..." prefix in chat |
> | Output dir | `aidlc-docs/` (NEVER application code — that goes to workspace root) |
> | Three phases | 🔵 Inception · 🟢 Construction · 🟡 Operations (future) |
> | Latest version | 0.1.8 (2026-04-20) |

## Key Insights

### 1. "Methodology, not a tool" — the core positioning

> [!tip] **From the AIDLC tenets:**
>
> > "AI-DLC is fundamentally a methodology, not a tool. Users shouldn't need to install anything to get started."
>
> The "tool" is just markdown files. No npm install, no pip install, no daemon. Copy `core-workflow.md` to your agent's rules location (CLAUDE.md, AGENTS.md, .cursor/rules/, etc.), and the methodology activates when you say "Using AI-DLC, ...".

This positioning has direct parallels to this wiki's own approach: the methodology framework lives in `wiki/config/methodology.yaml` + `wiki/config/wiki-schema.yaml` as configuration, with the agent reading them per project. **Both projects converge on the conclusion that methodology-as-config beats methodology-as-tool** — the framework should be portable across runtimes.

### 2. The three-phase workflow vs the wiki's five-stage model

> [!abstract] **Methodology comparison**
>
> | Dimension | This Wiki | AWS AI-DLC |
> |---|---|---|
> | **Stages/phases** | 5 (document → design → scaffold → implement → test) | 3 (Inception → Construction → Operations) |
> | **Models** | 9 named (feature-development, bug-fix, research, refactor, integration, hotfix, documentation, knowledge-evolution, project-lifecycle) | 1 adaptive workflow |
> | **Selection** | Multi-dimensional: `task_type × novelty × phase × scale × urgency` | Adaptive based on intent + complexity |
> | **Gates** | ALLOWED/FORBIDDEN per stage (hard) | Approval at end of each stage (Approve / Request Changes) |
> | **Quality tiers** | Skyscraper / Pyramid / Mountain | Depth levels: minimal / standard / comprehensive |
> | **Tenets** | "Preach by example" · "fix at the root" · "everything evolves" | "No duplication" · "methodology first" · "reproducible" · "agnostic" · "human in the loop" |
>
> **The wiki is more granular** (5 stages × 9 models = ~45 model-stage cells, each with its own ALLOWED/FORBIDDEN list) — better for autonomous agent enforcement at tool-call granularity. **AIDLC is more universal** (3 phases × 1 adaptive workflow) — better for human-driven sessions across many platforms. The two are not in conflict; they target different agent autonomy levels.

### 3. Inception → Construction → Operations: phase definitions

> [!info] **The three phases**
>
> | Phase | Question answered | Outputs | Maps to wiki stages |
> |---|---|---|---|
> | **🔵 Inception** | WHAT to build and WHY | Requirements analysis, user stories, application design + units of work, risk assessment | document + design |
> | **🟢 Construction** | HOW to build it | Per-unit: Functional Design, NFR Requirements, NFR Design, Infrastructure Design (conditional), then Code Generation (always), then Build and Test | scaffold + implement + test |
> | **🟡 Operations** (future) | Deploy and monitor | Deployment automation, observability setup, production readiness | (no wiki equivalent — wiki has no operations stage) |
>
> The Operations phase is currently a placeholder. **Wiki has no equivalent** — the methodology explicitly stops at "test" because the wiki itself isn't deployed. Sister projects' operations live in their own scopes (OpenFleet immune system, AICP guardrails, etc.).

### 4. The Question → Doc → Approval flow — a distinctive interaction pattern

> [!example]- **AIDLC's interaction protocol — multiple-choice in markdown, NOT chat**
>
> **Step 1.** AIDLC creates a question file like `aidlc-docs/inception/requirements/requirement-verification-questions.md` and STOPS.
>
> **Step 2.** User opens the file and fills in `[Answer]:` tags:
>
> ```markdown
> ## Question: Deployment model
> Where will this service be deployed?
>
> A) AWS Lambda (serverless)
> B) AWS ECS Fargate (containerized)
> C) Existing on-premises infrastructure
> X) Other (please describe after [Answer]: tag below)
>
> [Answer]: B — Fargate; matches existing services
> ```
>
> **Conventions for answering well:**
> - Add a label alongside the letter (`B — Fargate; matches existing services`)
> - Include a brief justification — confirms intent and gives carry-forward context
> - Combine options when both apply (`B and C — rate limiting at both API Gateway level and application level`)
> - Use X freely when none of the options fit
>
> **Step 3.** User returns to chat: "We have answered your clarification questions. Please re-read the file and proceed."
>
> **Step 4.** AIDLC validates answers, flags ambiguities, generates next artifact.
>
> **Step 5 (gate).** Approval gate with two options: **Request Changes** OR **Approve and Continue**.

This pattern is **structurally interesting for the wiki**: it externalizes decision points into durable, version-controlled, team-shareable artifacts. The wiki's current model has decisions surface in chat via operator directives → logged verbatim to `raw/notes/` retroactively. AIDLC's approach is **proactive** (the question file forces the structured answer) and **collaborative** (the whole team can fill in answers, not just the operator).

### 5. Context management — clear at gates, NEVER compact

> [!warning] **Direct quote from `docs/WORKING-WITH-AIDLC.md`:**
>
> > "If your tool offers a 'compact context' prompt mid-workflow, **always decline it** — compaction is not the same as a clean reset and loses more than it saves."
>
> AIDLC's philosophy: at every approval gate, **start a fresh context** so the next stage loads artifacts cleanly from disk rather than carrying compacted noise. This is **the opposite philosophy** from this wiki's `post-compact.sh` hook approach (which restores state after compaction occurs).
>
> **Both approaches solve the same problem differently:**
>
> | Approach | This wiki | AI-DLC |
> |---|---|---|
> | When | After compaction | At every gate (preempt compaction) |
> | Mechanism | post-compact.sh hook restores state from authoritative files | Operator manually clears + re-references state file |
> | State source | CLAUDE.md + raw/notes/ + frontmatter | aidlc-docs/aidlc-state.md (stage checkbox tracking) |
> | Trade-off | Resilient to compaction but recovery is partial | Forces fresh state but operator-driven |
>
> **Lesson candidate:** the post-compact restoration pattern (this wiki) and the clear-context-at-gate pattern (AIDLC) are alternative implementations of "context-compaction-is-a-reset-event" lesson. AIDLC chose human-driven discipline; we chose infrastructure-driven recovery. Per Principle 1 (Infrastructure > Instructions), our approach should be more reliable — but AIDLC's approach is simpler and tooling-agnostic. Worth a comparison page eventually.

### 6. The Vision Doc + Technical Environment Doc pre-inputs

AIDLC's "minimum viable input" before kicking off:

> [!abstract] **Pre-flight artifacts that compress clarifying-question count**
>
> | Document | Greenfield | Brownfield |
> |---|---|---|
> | **Vision Document** | What to build, for whom, MVP features in scope, features explicitly out of scope, open questions | Same + current state description + explicit "must not change" list |
> | **Technical Environment** | Language, package manager, framework, cloud provider, test framework, **prohibited libraries table (with reason + alternative)**, security basics, example code patterns | Same but describing the EXISTING stack — example code pulled from actual existing files |
>
> **The prohibited libraries table > a plain list:** the reason + alternative columns tell the AI WHY a library is banned, leading to better substitution decisions. The example code patterns are the **single highest-leverage addition** beyond the basics — concrete pattern to follow during code generation rather than the AI inventing its own.
>
> **Wiki parallel:** the Goldilocks identity profile (CONTEXT.md) is functionally similar — it declares type, phase, scale, PM level, trust tier upfront so the methodology adapts. AIDLC's Vision/TechEnv docs are **more domain-specific** (per-project tech-stack constraints); the wiki's Goldilocks is **more methodology-meta** (which process applies). Complementary, not competing.

### 7. The "Never Vibe Code" rule

> [!success] **AIDLC's most quotable rule:**
>
> > "**You never fix code directly.** If you discover an issue, go back to AIDLC and say: I have discovered issue X. Review the design and make a plan to fix it. If this affects the design, update it, then update the code."
>
> "Vibe coding" = directly editing generated code files to bypass design documents. Feels fast in the moment, creates problems shortly after. The mechanism: **design documents are the source of truth for every subsequent operation; code-only edits silently desync them.**
>
> **The right flow when something needs fixing:**
> 1. **Describe the issue without touching anything:** "Do not update any documents yet. I have discovered issue X. Review the design and help me understand where this needs to be addressed."
> 2. **Fix the design document:** "Please update [specific design document] to reflect [the fix]. Then check whether any upstream documents — requirements, user stories — also need to be updated."
> 3. **Regenerate the affected code:** "The design for [unit name] has been updated. Please re-run code generation for the affected files only."
>
> **Wiki parallel:** the methodology's stage gates enforce this structurally (no-code-during-document, no-business-logic-during-scaffold). AIDLC enforces it **culturally** (operator discipline) since it has no hooks. Both reach the same destination via different mechanisms.

### 8. Standing rules — set once, apply throughout phase

> [!tip] **Two operator-set standing rules that prevent drift:**
>
> ```text
> Every time you update a document, check whether the change impacts the
> requirements document and user stories, and prompt me if it does.
> ```
>
> ```text
> When you make a design decision during code generation, always make sure
> the documentation reflects this change before proceeding.
> ```
>
> Set at the start of Construction, applied throughout. **Wiki parallel:** the operator's sacrosanct directives in CLAUDE.md function similarly — set once at session-config-time, apply to every interaction. AIDLC's standing rules are **scoped to a phase**; the wiki's directives are **scoped to a session**. The granularity differs but the pattern is the same.

### 9. The extensions system — opt-in cross-cutting constraints

> [!info] **AIDLC extension architecture**
>
> Extensions live under `aws-aidlc-rule-details/extensions/`. Each extension consists of TWO files:
>
> | File | Purpose |
> |---|---|
> | **`<name>.md`** (e.g., `security-baseline.md`) | The actual rules — `## Rule <PREFIX-NN>: <Title>` headings, each with **Rule** and **Verification** sections. PREFIX-NN like `SECURITY-01`, `COMPLIANCE-02` — globally unique, referenced in audit logs. |
> | **`<name>.opt-in.md`** (e.g., `security-baseline.opt-in.md`) | Multiple-choice prompt presented during Requirements Analysis. If user opts in → rules file loaded for the rest of the workflow. If opts out → rules never load. |
>
> Built-in: **security/baseline**, **testing/property-based**. Extensions without an opt-in file are **always enforced**.
>
> Once enabled, extension rules are **blocking constraints** — at each stage, the model verifies compliance before allowing the stage to proceed.
>
> **Wiki parallel:** the methodology's per-domain profiles (`wiki/config/domain-profiles/typescript.yaml`, `python-wiki.yaml`, `infrastructure.yaml`) play a similar role for domain-specific overrides. **What we don't have:** AIDLC's opt-in MECHANISM — the wiki's domain profiles are auto-detected by file path, not user-confirmed at session start. The opt-in flow with multiple-choice gating is a structural pattern worth considering for our methodology when it crosses team boundaries.

### 10. The aidlc-docs/ directory structure — durable artifact tree

> [!example]- **Generated artifact directory layout (per `docs/GENERATED_DOCS_REFERENCE.md`)**
>
> ```text
> aidlc-docs/
> ├── audit.md                                    # APPEND-ONLY, ISO 8601 timestamps for every interaction
> ├── aidlc-state.md                              # Stage tracking — checkboxes for completed/skipped/in-progress
> │
> ├── inception/                                  # 🔵 INCEPTION PHASE
> │   ├── plans/                                  # Plans with [Answer]: tags + [ ]/[x] checkboxes
> │   ├── requirements/
> │   │   ├── requirements.md                     # Functional + non-functional requirements
> │   │   ├── user-stories.md                     # User stories (when applicable)
> │   │   └── requirement-verification-questions.md  # Multi-choice questions for ambiguity resolution
> │   └── application-design/                     # System architecture, units of work decomposition
> │
> ├── construction/                               # 🟢 CONSTRUCTION PHASE
> │   ├── {unit-name}/                            # One subdirectory PER unit of work
> │   │   ├── plans/{unit-name}-code-generation-plan.md
> │   │   ├── functional-design/                  # Business logic, domain models, data schemas
> │   │   ├── nfr-requirements/                   # Performance, security, scalability, tech stack
> │   │   ├── nfr-design/                         # Resilience, scalability, performance, security patterns
> │   │   ├── infrastructure-design/              # Cloud service mappings, deployment architecture
> │   │   └── code/                               # Markdown SUMMARIES of generated code (actual code → workspace root)
> │   ├── shared-infrastructure.md
> │   └── build-and-test/                         # Always created after all units complete
> │       ├── build-instructions.md
> │       ├── unit-test-instructions.md
> │       ├── integration-test-instructions.md
> │       ├── performance-test-instructions.md    # Conditional on performance NFRs
> │       ├── contract-test-instructions.md       # Conditional on microservices
> │       ├── security-test-instructions.md       # Conditional on security NFRs
> │       ├── e2e-test-instructions.md            # Conditional on user workflows
> │       └── build-and-test-summary.md
> │
> └── operations/                                 # 🟡 OPERATIONS PHASE — placeholder
> ```
>
> Critical conventions:
> - **Application code is NEVER inside `aidlc-docs/`** — only markdown documentation lives here
> - **`audit.md` is append-only** — no edits, no deletions; it is the methodology's audit trail
> - **`aidlc-state.md` tracks stage completion** — completed / skipped / in-progress checkboxes per stage + extension config
> - **Plans contain `[Answer]:` tags AND `[ ]`/`[x]` checkboxes** — combined Q&A and progress tracking
> - **Code summaries live in `code/`** but actual code goes to workspace root (preserves AIDLC's "config not the artifact" principle)

### 11. Multi-platform support — explicit agent-agnosticism

> [!abstract] **Platforms with documented setup paths**
>
> | Platform | Rules location | Method |
> |---|---|---|
> | **Kiro IDE / CLI** | `.kiro/steering/aws-aidlc-rules/` | Native Kiro Steering Files |
> | **Amazon Q Developer** | `.amazonq/rules/` | Amazon Q Rules |
> | **Cursor IDE** | `.cursor/rules/ai-dlc-workflow.mdc` (with frontmatter) OR root `AGENTS.md` | Cursor Rules |
> | **Cline** | `.clinerules/core-workflow.md` OR root `AGENTS.md` | Cline Rules |
> | **Claude Code** | `CLAUDE.md` OR `.claude/CLAUDE.md` | Project memory file |
> | **GitHub Copilot** | `.github/copilot-instructions.md` | Custom Instructions |
> | **OpenAI Codex** | Root `AGENTS.md` | AGENTS.md convention |
> | **Antigravity** | `.agent/rules/ai-dlc.md` | Antigravity Rules |
> | **Other agents** | Project root, point agent at `aws-aidlc-rules/` | Generic |
>
> The **agent-driven setup prompt** (experimental) is novel: the user pastes a single prompt into their AI agent, the agent fetches the latest release from GitHub, extracts to `.aidlc/`, creates the IDE-appropriate rules file, and gitignores `.aidlc`. This is the **tool-self-onboarding** pattern (also seen in Firecrawl's `agent-onboarding/SKILL.md`) — the methodology installs itself.

### 12. The methodology as published-and-versioned product

> [!info] **AIDLC release engineering**
>
> | Aspect | Practice |
> |---|---|
> | Versioning | Semver — current 0.1.8 (2026-04-20) |
> | Release cadence | ~2-4 weeks between minor releases |
> | Distribution | GitHub Releases zip download |
> | Changelog | Auto-generated by **git-cliff** (changelog-first: changelog updated BEFORE tag, included in tagged commit) |
> | CI | AWS CodeBuild for evaluator + 6 security scanners (Bandit, Semgrep, Grype, Gitleaks, Checkov, ClamAV) |
> | Conventional commits | Required (`feat:`, `fix:`, `docs:`, `chore:`) |
> | Testing | `uv run pytest` for the evaluator framework + cross-platform manual testing for installation instructions |
>
> **Wiki parallel/gap:** this wiki's methodology is NOT versioned, NOT released, NOT distributed as a downloadable artifact. It evolves continuously in-place with `git log` as the only changelog. AIDLC's release-engineered approach is **stronger for cross-team adoption** (you can pin to a specific AIDLC version); the wiki's continuous-evolution approach is **stronger for self-improvement** (every directive immediately reshapes the methodology). Goldilocks: a project that needs to ship a methodology to others should release-engineer it; a project iterating its OWN methodology should evolve continuously.

## Open Questions

> [!question] Which patterns from AIDLC should the wiki adopt?
> Strong candidates from the synthesis:
>
> | AIDLC pattern | Wiki adoption candidate | Effort | Value |
> |---|---|---|---|
> | Question→Doc→Approval flow with `[Answer]:` tags | Could replace some operator-directive turns with pre-structured question files | Low — author template + one command | Medium |
> | Vision Doc + Technical Environment Doc pre-inputs | Wiki has Goldilocks profile; could add per-task pre-inputs for big multi-session epics | Medium — extend backlog template | Low (wiki's task scope is smaller) |
> | "Do not update any documents" exploratory prefix | Could become a CLAUDE.md hard rule: explicit "investigate-only" prefix | Trivial | Medium — prevents premature wiki edits |
> | Extension opt-in mechanism | Could supplement domain profiles with operator-confirmed opt-in at session start | Medium — extend gateway orient | Low for solo session, high for fleet |
> | audit.md append-only ISO 8601 | Wiki/log/ already similar; could formalize the append-only invariant | Trivial — document the rule | Low (already implicit) |
> | aidlc-state.md stage-checkbox tracking | Wiki has frontmatter readiness/progress; complementary, not replacement | Low | Low (already covered) |
>
> Requires: operator decision on which to formalize.

> [!question] Should the wiki publish itself like AIDLC publishes itself?
> AIDLC = release-engineered, versioned, downloadable. Wiki = continuous-evolution, reference-only. **Trade-off:**
> - Adoption-friendly path: package wiki/spine/ + wiki/config/ as a downloadable "wiki-methodology-vN.zip" for sister projects to pin to
> - Anti-pattern: makes the wiki's own self-improvement (the `pipeline evolve` loop) lag behind the published version
>
> Possible compromise: the wiki publishes **stable methodology snapshots** (every quarter?) for sister-project pinning while continuing to evolve in-place for its own use. Requires: ADR-style decision page if pursued.

> [!question] Is the AIDLC three-phase model better mapped to wiki content vs project-lifecycle?
> AIDLC's three phases (Inception → Construction → Operations) map onto **project lifecycle** (the wiki's `project-lifecycle` aka SFIF model). They DON'T map onto the wiki's task-level methodology models (feature-development, bug-fix, etc.) which run inside SFIF stages. **Implication:** AIDLC and the wiki's methodology operate at DIFFERENT GRANULARITIES — AIDLC at the project lifecycle level, wiki methodology at the task level. They could compose: AIDLC for project bootstrap, wiki methodology for task execution. Worth a separate comparison page if the operator chooses to pursue.

## Relationships

- DERIVED FROM: [[src-awslabs-aidlc-workflows|awslabs/aidlc-workflows GitHub Repository]]
- COMPARES TO: [[model-methodology|Model — Methodology]] (the wiki's own methodology framework — the central comparison axis)
- COMPARES TO: [[model-sfif-architecture|Model — SFIF and Architecture]] (AIDLC's three phases parallel SFIF's project-lifecycle stages)
- COMPARES TO: [[src-bmad-method-agile-ai-development-framework|Synthesis: BMAD-METHOD]] (another multi-agent methodology — converging structural patterns)
- COMPARES TO: [[src-openspec-spec-driven-development-framework|Synthesis: OpenSpec — Spec-Driven Development]]
- COMPARES TO: [[src-github-spec-kit-specification-driven-development|Synthesis — GitHub Spec Kit]]
- RELATES TO: [[src-qwen3-6-27b-2-bit-26-tool-calls-unsloth-discussion|Synthesis — Unsloth Qwen3.6-27B 2-bit]] (the operator's tier-0 model that would consume AIDLC rules)
- RELATES TO: [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] (AIDLC's "clear at gates, never compact" is an alternative implementation)
- RELATES TO: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions]] (AIDLC chose instructions; wiki chose infrastructure — mindful comparison)
- RELATES TO: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Behavior]] (AIDLC's question files + opt-in prompts are structured context implementations)
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]] (lessons from a peer methodology should inform our adoption advice)
- FEEDS INTO: [[model-llm-wiki|Model — LLM Wiki]] (audit.md + aidlc-state.md patterns are content-management primitives worth tracking)

## Backlinks

[[awslabs/aidlc-workflows GitHub Repository]]
[[model-methodology|Model — Methodology]]
[[model-sfif-architecture|Model — SFIF and Architecture]]
[[Synthesis: BMAD-METHOD]]
[[Synthesis: OpenSpec — Spec-Driven Development]]
[[Synthesis — GitHub Spec Kit]]
[[src-qwen3-6-27b-2-bit-26-tool-calls-unsloth-discussion|Synthesis — Unsloth Qwen3.6-27B 2-bit]]
[[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]
[[Principle — Infrastructure Over Instructions]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Behavior]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-llm-wiki|Model — LLM Wiki]]

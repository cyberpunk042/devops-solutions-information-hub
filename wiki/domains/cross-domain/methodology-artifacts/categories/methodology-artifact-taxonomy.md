---
title: Methodology Artifact Taxonomy
aliases:
  - "Methodology Artifact Taxonomy"
type: reference
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: taxonomy-research
    type: wiki
    file: wiki/sources/methodology-artifact-taxonomy-research.md
  - id: openarms-chain
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms artifact chain (24 artifacts at Default SDLC level)"
  - id: sdlcforms
    type: article
    url: https://www.sdlcforms.com/UnderstandingSDLC.html
tags: [methodology, taxonomy, artifacts, documents, documentation, reference, framework]
---

# Methodology Artifact Taxonomy

> [!tip] AI Quick Start — What You Do With This Page
>
> 1. **Determine the CLASS** of what you're producing: DOCUMENT (constraining spec), ARTIFACT (by-product of work), or DOCUMENTATION (explaining for users)
> 2. **Find the CATEGORY** (11 categories below) — which phase of work produces this?
> 3. **Find the specific TYPE** within that category — what is it called, what does it contain?
> 4. **Check if it's a wiki page type** — if yes, there's a template in `wiki/config/templates/` and a standards doc in `wiki/spine/standards/`
> 5. **Check the domain chain** for your domain — what does this artifact look like in YOUR tech stack?

## Summary

The complete classification of every artifact, document, and documentation type produced during software development methodology execution. Organized into 11 categories with 78 types. This is the FRAMEWORK — it defines what each type IS, when it's produced, who the audience is, and what quality looks like. Projects select which types apply to their domain via domain profiles. Individual types are defined here; per-model chains are defined in [[artifact-chains-by-model|Artifact Chains by Methodology Model]]; per-type standards are in `wiki/spine/standards/`.

## Reference Content

### The Three Classes of Methodology Outputs

Before the taxonomy: understand that methodology produces three fundamentally different classes of output. Each class has different quality rules, different audiences, and different lifecycles.

> [!abstract] Artifacts vs Documents vs Documentation
>
> | Class | What It Is | Examples | Audience | Lifecycle |
> |-------|-----------|----------|----------|-----------|
> | **Artifact** | Tangible by-product of work — produced as a SIDE EFFECT of doing something | Source code, binaries, test results, git commits, deployment packages, log files | Machines, CI/CD, other tools | Created → used → replaced |
> | **Document** | Written specification with formal structure — created DELIBERATELY to constrain future work | Requirements spec, ADR, tech spec, test plan, gap analysis | Engineers, reviewers, future agents | Draft → active → approved → superseded |
> | **Documentation** | Explanatory material — created to EXPLAIN what exists for users or maintainers | User guide, admin guide, API docs, README, runbook, operations guide | End users, operators, maintainers | Created → updated → retired |
>
> A Test Plan (document) constrains how tests will be written.
> A Test Result (artifact) is produced by running those tests.
> A Testing Guide (documentation) explains how to run and interpret tests.
> These are three different types with three different standards.

### Category 1: Initiation Artifacts

> [!info] When a project or epic STARTS — before any work begins
>
> | Type | Purpose | When Produced | Required For |
> |------|---------|---------------|-------------|
> | **Project Charter** | Scope, objectives, stakeholders, success criteria, constraints | Project start | Epic-scale work |
> | **Business Case** | Cost-benefit analysis, ROI, risk assessment, alternatives | Project start | Investment decisions |
> | **Feasibility Study** | Technical, operational, economic feasibility analysis | Project start | Go/no-go decisions |
> | **Concept of Operations (CONOPS)** | How the system will be used in practice — user perspective | Project start | Complex systems |
> | **Cost-Benefit Analysis** | Quantified costs vs benefits with timeline | Project start | Budget approval |
> | **Stakeholder List** | Who has interest, authority, influence over the project | Project start | Communication planning |
> | **Resource Plan** | Who works on what, when, with what tools | Project start | Team allocation |
>
> **Domain notes:** These apply at EPIC or PROJECT scale. Tasks and modules don't produce initiation artifacts — they inherit them from their parent epic. For the research wiki, the operator directive log serves as a lightweight Project Charter.

### Category 2: Planning Artifacts

> [!info] HOW the work will be organized and tracked
>
> | Type | Purpose | When Produced | Required For |
> |------|---------|---------------|-------------|
> | **Statement of Work** | What will be delivered, by whom, by when, at what cost | Planning phase | Contract/agreement work |
> | **Project Plan** | Timeline, milestones, dependencies, critical path | Planning phase | Epic-scale work |
> | **Work Breakdown Structure** | Hierarchical decomposition of deliverables into tasks | Planning phase | Epic → module → task breakdown |
> | **Risk Analysis Plan** | Identified risks, probability, impact, mitigation strategies | Planning phase | Complex/risky work |
> | **Procurement Plan** | External dependencies, vendor selection, acquisition timeline | Planning phase | Projects with external deps |
> | **Roles Matrix** | Who is responsible, accountable, consulted, informed (RACI) | Planning phase | Multi-person teams |
> | **Approvals Matrix** | Who approves what, at which gates, with what authority | Planning phase | Gated processes |
> | **Configuration Management Plan** | How configs, versions, and environments are managed | Planning phase | Multi-environment projects |
>
> **Domain notes:** In our methodology, the WBS maps to the Epic → Module → Task hierarchy. The Project Plan maps to the backlog with readiness tracking. The Risk Analysis maps to the gap analysis document. Planning artifacts are mostly relevant at epic scale.

### Category 3: Requirements Artifacts

> [!info] WHAT the system must do — produced during the Document stage
>
> | Type | Purpose | When Produced | Required For |
> |------|---------|---------------|-------------|
> | **Business Requirements Document (BRD)** | High-level business needs in business language | Document stage | Epic/project scope |
> | **Functional Requirements Document (FRD)** | Specific functional behaviors with inputs/outputs/constraints | Document stage | Feature development |
> | **Use Cases** | Actor-system interactions, scenarios, happy/error paths | Document stage | User-facing features |
> | **Requirements Traceability Matrix (RTM)** | Maps requirements → design → code → tests — full traceability | Document stage | Compliance, audit |
> | **Software Requirements Specification (SRS)** | Formal, complete technical requirements (IEEE 830 format) | Document stage | Regulated/complex systems |
> | **Requirements Inspection Checklist** | Verification that requirements are complete, consistent, testable | Document stage | Quality assurance |
> | **Service Level Agreement (SLA)** | Performance, availability, response time commitments | Document stage | Service-oriented systems |
>
> **In our methodology:** The Requirements Spec template (wiki/config/templates/methodology/requirements-spec.md) combines BRD + FRD + AC into one document for most tasks. SRS-level formality is only needed for regulated or safety-critical work. Use Cases are embedded in requirements as scenarios.
>
> **OpenArms instance:** Document #1 in the chain — "FR-N items with Input/Output/Constraints. All AC items are testable."

### Category 4: Design Artifacts

> [!info] HOW the system will work — produced during the Design stage
>
> | Type | Purpose | When Produced | Required For |
> |------|---------|---------------|-------------|
> | **Architecture Decision Record (ADR)** | Decision + rationale + alternatives + consequences | Design stage | Every significant decision |
> | **Technical Specification** | Components, APIs, algorithms, error handling, state management | Design stage | Feature development |
> | **Interface Specification** | Complete types, function signatures, data contracts | Design stage | Code projects (scaffold copies from this) |
> | **Configuration Specification** | YAML shapes, env vars, CLI flags, defaults, precedence | Design stage | Configurable systems |
> | **High-Level Design (HLD)** | System architecture, component diagrams, technology stack | Design stage | New systems/subsystems |
> | **Low-Level Design (LLD)** | Detailed module specs, algorithms, data structures | Design stage | Complex logic |
> | **Database Design** | ER diagrams, schema definitions, data dictionary | Design stage | Data-intensive systems |
> | **UI/UX Artifacts** | Wireframes, mockups, prototypes, style guides | Design stage | User-facing features |
> | **API Specification** | Endpoints, request/response formats, authentication | Design stage | API-first systems |
> | **Test Plan** | Test strategy, test cases with IDs, inputs, expected outputs | Design stage | All testable work |
>
> **In our methodology:** ADR uses the decision template. Tech Spec and Config Spec use the reference template. Interface Spec is TypeScript-specific (other domains have equivalents). Test Plan uses wiki/config/templates/methodology/test-plan.md.
>
> **ADR variants:** Nygard (lightweight), MADR (tradeoff analysis), Y-Statement ("In context C, facing F, we decided D..."), IBM UMF (table layout), Tyree-Akerman (forces + consequences). Our decision template is closest to MADR.

### Category 5: Construction Artifacts

> [!info] The actual THINGS built — produced during Scaffold and Implement stages
>
> | Type | Purpose | When Produced | Domain-Specific |
> |------|---------|---------------|----------------|
> | **Type Definitions** | Types, interfaces, schemas — structure without behavior | Scaffold stage | TypeScript: .ts exports. Python: .yaml configs. Terraform: .tf variables |
> | **Test Stubs** | Empty test structure with placeholder assertions | Scaffold stage | TypeScript: .test.ts. Python: test_*.py. Terraform: .tftest.hcl |
> | **Config Wiring** | Parent config modified to accept new fields | Scaffold stage | Framework-dependent |
> | **Implementation Code** | Business logic, algorithms, data processing | Implement stage | TypeScript: .ts. Python: .py. Terraform: .tf resources |
> | **Bridge/Adapter Modules** | Thin adapters between new module and existing consumers | Implement stage | Any language — pattern is universal |
> | **Integration Wiring** | Existing file modified to import and use new code | Implement stage | Any language — the consumer edit |
> | **Environment Config** | .env files, env var definitions, deployment configs | Scaffold/Implement | Platform-dependent |
>
> **Critical rule from OpenArms Bug 6:** Implementation is NOT done until at least one existing runtime file imports and calls the new code. "Code exists" ≠ "code works." 2,073 lines were orphaned because nothing imported them.

### Category 6: Testing Artifacts

> [!info] PROOF that the system works — produced during the Test stage
>
> | Type | Purpose | When Produced | Domain-Specific |
> |------|---------|---------------|----------------|
> | **Test Implementations** | Real assertions replacing scaffold placeholders | Test stage | Language-dependent |
> | **Test Results** | Gate command output showing pass/fail | Test stage | Tool-dependent (pnpm test, pytest, terraform test) |
> | **User Acceptance Test (UAT)** | End-user verification against business requirements | Test stage | User-facing features |
> | **Bug Reports** | Defect description, reproduction steps, severity | Test stage | When tests reveal issues |
> | **Regression Test Plan** | Tests verifying fixed bugs don't recur | Test stage | After bug fixes |
> | **Test Coverage Report** | Which functions/paths/branches are tested | Test stage | Code projects |
> | **QA Checklist** | Manual verification checklist for non-automatable checks | Test stage | UI, accessibility, compliance |
> | **Performance Test Results** | Load, stress, response time measurements | Test stage | Performance-critical systems |

### Category 7: Deployment Artifacts

> [!info] How to SHIP and OPERATE the system — produced during deployment
>
> | Type | Purpose | Audience | When Produced |
> |------|---------|----------|---------------|
> | **Installation Guide** | Step-by-step installation for target environment | Operators | Before deployment |
> | **User Guide** | How end users use the system | End users | Before deployment |
> | **Admin Guide** | System administration, configuration, maintenance | Admins | Before deployment |
> | **Operations Guide** | Day-to-day operational procedures, monitoring | Operators | Before deployment |
> | **Production Implementation Plan** | Deployment steps, rollback plan, verification | Deployment team | Before deployment |
> | **Runbook** | Step-by-step procedures for common operational tasks | On-call engineers | Before/during operation |
> | **Release Notes** | What changed, what's new, what's fixed, known issues | All users | Each release |
>
> **In our methodology:** The operations-plan template covers Production Implementation Plans and Runbooks. User/Admin/Operations guides map to wiki documentation pages.

### Category 8: Closure Artifacts

> [!info] What was LEARNED — produced when work completes
>
> | Type | Purpose | When Produced | Required For |
> |------|---------|---------------|-------------|
> | **Lessons Learned** | What worked, what didn't, what to do differently | Project/epic completion | All completed work |
> | **Post-Project Review** | Comprehensive assessment against original objectives | Project completion | Epic-scale work |
> | **Knowledge Transfer Report** | What the next team/person needs to know | Team transitions | Handoffs |
> | **Completion Log** | What was done, what passed, what concerns were raised | Task/stage completion | All methodology-tracked work |
> | **Retirement Plan** | How to decommission, migrate, archive | End of life | Sunsetting systems |
>
> **In our methodology:** Lessons map to our lesson page type. Completion logs are auto-generated by harness (OpenArms) or manually recorded (wiki). The knowledge evolution pipeline (lesson → pattern → decision) IS the closure learning process.

### Category 9: Monitoring Artifacts

> [!info] Ongoing TRACKING during execution
>
> | Type | Purpose | When Updated | Required For |
> |------|---------|-------------|-------------|
> | **Change Management Log** | All scope changes with approval status | Throughout | Scope control |
> | **Risk Register** | Live risk tracking with probability, impact, mitigation status | Throughout | Risk management |
> | **Status Reports** | Progress against plan, blockers, decisions needed | Periodic (weekly/sprint) | Stakeholder communication |
> | **Issue Log** | Problems encountered, resolution status, owner | Throughout | Issue tracking |
> | **Compliance Report** | Methodology compliance metrics, violation tracking | Post-session | Agent methodology adherence |
>
> **In our methodology:** The backlog system (epic readiness, stage tracking) serves as the Status Report. The wiki log (wiki/log/) serves as the Change/Issue Log. Compliance reporting is an open gap — identified but not built.

### Category 10: Knowledge Artifacts

> [!info] Synthesized UNDERSTANDING — the wiki's primary domain
>
> | Type | Purpose | Layer | Template |
> |------|---------|-------|---------|
> | **Concept** | Define what something IS — components, mechanisms, boundaries | 1-3 | concept.md |
> | **Source Synthesis** | Process raw source into actionable knowledge | 1 | source-synthesis.md |
> | **Comparison** | Structured evaluation of alternatives | 2 | comparison.md |
> | **Reference** | Lookup material optimized for scanning | 2 | reference.md |
> | **Deep Dive** | Extended analysis beyond concept depth | 2 | deep-dive.md |
> | **Lesson** | Actionable learning from convergent evidence | 4 | lesson.md |
> | **Pattern** | Recurring structure observed across ≥2 instances | 5 | pattern.md |
> | **Decision** | Resolved question with alternatives and rationale | 6 | decision.md |
>
> **This is the wiki's strength.** 100% coverage of knowledge types. Each has a template, a standards doc, and an exemplar. The challenge is connecting these to the other 10 categories.

### Category 11: AI Agent Artifacts

> [!info] Agent-specific outputs for autonomous/fleet workflows
>
> | Type | Purpose | When Produced | Required For |
> |------|---------|---------------|-------------|
> | **Agent Persona Template** | Identity, capabilities, constraints for a role | Planning | Multi-agent systems |
> | **Skill Definition** | What a skill does, when to invoke, parameters | Design | Skill-based architectures |
> | **Stage Skill** | Per-stage instructions injected into agent context | Design | Stage-gate enforcement |
> | **Hook Configuration** | Pre/post tool-use enforcement rules | Design | Infrastructure enforcement |
> | **Prompt Queue** | Queued prompts for batch execution | Implementation | Automated evolution |
> | **Agent Compliance Report** | Stage violations, gate results, concern log | Monitoring | Autonomous operations |
>
> **From agentic engineering research (2026):** The PEV loop (Plan-Execute-Verify) with multi-agent orchestration (Feature Author → Test Generator → Code Reviewer → Architecture Guardian → Security Scanner → Documentation Writer → Release Manager) means each specialized agent produces typed artifacts that feed the next agent in the pipeline.

### How to Use This Taxonomy

> [!tip] For Project Setup
>
> 1. Identify your project scale (task, module, epic, project)
> 2. Select the relevant categories from this taxonomy
> 3. For each category, identify which types apply to your domain
> 4. Configure your methodology model with the selected artifact chain
> 5. Use domain profiles to resolve generic types to specific paths/tools

> [!tip] For Adding New Artifact Types
>
> 1. Determine which category the new type belongs to
> 2. Define: purpose, when produced, audience, domain-specific variations
> 3. If it can be a wiki page: create a page type, template, and standards doc
> 4. If it's a non-wiki artifact: add to the methodology model's chain as a tracked artifact
> 5. Add to the relevant domain profiles with path patterns and gate commands

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[methodology-artifact-taxonomy-research|Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research]]
- FEEDS INTO: [[model-methodology|Model — Methodology]]
- FEEDS INTO: [[methodology-framework|Methodology Framework]]
- FEEDS INTO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[task-type-artifact-matrix|Task Type Artifact Matrix]]
- RELATES TO: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[methodology-artifact-taxonomy-research|Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research]]
[[model-methodology|Model — Methodology]]
[[methodology-framework|Methodology Framework]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[ai-agent-artifacts|AI Agent Artifacts — Standards and Guide]]
[[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
[[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]
[[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
[[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
[[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
[[coverage-blindness-modeling-only-what-you-know|Coverage Blindness — Modeling Only What You Know]]
[[artifact-system-design-decisions|Decision — Artifact System Design Decisions]]
[[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
[[initiation-and-planning-artifacts|Initiation and Planning Artifacts — Standards and Guide]]
[[methodology-config-architecture|Methodology Config Architecture — How the Pieces Fit Together]]
[[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]]
[[three-classes-of-methodology-output|Three Classes of Methodology Output]]
[[universal-stages-domain-specific-artifacts|Universal Stages, Domain-Specific Artifacts]]

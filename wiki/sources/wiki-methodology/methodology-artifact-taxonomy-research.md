---
title: Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research
aliases:
  - "Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research"
  - "Synthesis: Methodology Artifact Taxonomy — Full Spectrum Research"
type: source-synthesis
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: sdlcforms
    type: article
    url: https://www.sdlcforms.com/UnderstandingSDLC.html
  - id: nxcode-agentic
    type: article
    url: https://www.nxcode.io/resources/news/agentic-engineering-complete-guide-vibe-coding-ai-agents-2026
  - id: adr-github
    type: documentation
    url: https://adr.github.io/
  - id: geeksforgeeks-artifacts
    type: article
    url: https://www.geeksforgeeks.org/software-engineering/artifact-software-development/
  - id: wikipedia-artifacts
    type: article
    url: https://en.wikipedia.org/wiki/Artifact_(software_development)
  - id: openarms-document-chain
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms methodology document chain"
  - id: atlassian-scrum
    type: article
    url: https://www.atlassian.com/agile/scrum/artifacts
  - id: zettelkasten-method
    type: article
    url: https://zettelkasten.de/posts/building-a-second-brain-and-zettelkasten/
  - id: martin-fowler-adr
    type: article
    url: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
  - id: google-cloud-adr
    type: documentation
    url: https://cloud.google.com/architecture/architecture-decision-records
tags: [methodology, artifacts, taxonomy, research, sdlc, agile, devops, ai-agents, knowledge-management]
---

# Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research
## Summary

Comprehensive research into methodology artifacts across five domains: traditional SDLC, Agile/Scrum, DevOps/Infrastructure, AI Agent workflows, and Knowledge Management systems. The real-world SDLC has 100+ distinct document types across 8 phases. OpenArms uses ~24. Our wiki defines 17 page types. The gap between what elite teams produce and what we currently model is massive — our system covers roughly 20% of the artifact space. This research maps the FULL taxonomy, classifies every artifact type, identifies per-domain variations, and establishes the foundation for building a complete methodology artifact system.

> [!info] Source Reference
>
> | Attribute | Value |
> |-----------|-------|
> | Sources | 10 (5 online, 1 codebase, 4 reference) |
> | Coverage | SDLC, Agile, DevOps, AI Agents, Knowledge Management |
> | Key finding | 77 distinct artifact types across 11 categories |
> | Gap | Our wiki covers ~20% of the real-world artifact space |
> | Existing best | OpenArms methodology-document-chain.md (846 lines, 24-artifact chain for Feature Dev) |

## Key Insights

### 1. Three Fundamentally Different Things: Artifacts vs Documents vs Documentation

The industry uses these terms interchangeably but they are structurally different:

- **Artifacts** — any tangible by-product of development: code, binaries, configs, test results, logs, deployment packages. Artifacts are PRODUCED as side effects of work.
- **Documents** — written specifications with formal structure: BRD, FRD, SRS, ADR, Test Plan, Tech Spec. Documents are CREATED deliberately to constrain future work.
- **Documentation** — explanatory material for users or maintainers: User Guides, Admin Guides, API Docs, READMEs, Runbooks. Documentation EXPLAINS what exists.

> [!warning] Why This Distinction Matters
>
> Our wiki conflated all three as "wiki pages." A Test Plan (document that constrains test writing) is fundamentally different from a Test Result (artifact produced by running tests) which is different from a Testing Guide (documentation explaining how to test). Each has different quality standards, different audiences, different lifecycle rules. Treating them as the same type produces the "hardcoded, low quality" output the operator identified.

### 2. The Real-World SDLC Has 100+ Document Types

From sdlcforms.com — the most comprehensive SDLC documentation taxonomy found online — a standard enterprise software project can produce over 100 distinct documents across 8 phases:

| Phase | Document Count | Key Types |
|-------|---------------|-----------|
| Initiation | 12 | Project Charter, Business Case, Feasibility Study, CONOPS, Cost-Benefit Analysis, Stakeholder List, Resource Plan, Team Definition |
| Planning | 14 | Statement of Work, Project Plan, WBS, Risk Analysis Plan, Procurement Plan, Roles Matrix, Approvals Matrix, Config Management Plan, Cost Estimating |
| Requirements | 10 | BRD, FRD, Use Cases, RTM, Software Architecture Plan, Requirements Inspection Checklist, Training Plan, SLA Template |
| Design | 10 | SRS, HLD, LLD, Database Design, UI/UX Artifacts, API Specification, Analysis & Design Document, Code Review Checklist, Conversion Plan |
| Testing | 11 | Test Plan, System Test Plan, UAT Plan, Test Scenarios, Bug Reports, Bug List, Regression Plan, QA Checklist, Website Testing Summary |
| Monitoring | 9 | Change Management Log, Risk Register, Issue Log, Status Reports, Milestone Forms, Action Items, COBIT Reports |
| Deployment | 7 | Installation Guide, User Guide, Admin Guide, Operations Guide, Process Guide, Production Implementation Plan, Turnover Approval |
| Closure | 11 | Lessons Learned, Post-Project Review, Transition Plan, Survey Questionnaire, Change Control Request, Disaster Recovery Plan, Knowledge Transfer Report, Retirement Plan |

**Total: 84 document types from SDLC alone.** Most enterprise projects use 30-50 of these depending on scale and compliance requirements.

### 3. Agile Reduces Document Count But Not Artifact Count

Agile methodology reduces formal DOCUMENTS (no 200-page SRS) but increases ARTIFACTS:

| Agile Artifact Category | Types |
|------------------------|-------|
| **Backlog artifacts** | Product Backlog, Sprint Backlog, Product Increment, Burndown Charts, Definition of Done |
| **Requirements artifacts** | User Stories, Acceptance Criteria, Story Maps, Personas, Epics |
| **Design artifacts** | Design Models, Software Architecture Descriptions, Prototypes, Wireframes |
| **Implementation artifacts** | Source Code, Build Scripts, Executables, Configuration Files |
| **Test artifacts** | Test Suites, Test Results, Automation Scripts, Coverage Reports |
| **Deployment artifacts** | Release Notes, Deployment Scripts, Rollback Plans, Monitoring Configs |

The engineering set divides into four: **requirements set, design set, implementation set, deployment set.** Each feeds the next.

### 4. AI Agent Methodology Adds New Artifact Types

From the Agentic Engineering research (nxcode.io, 2026), AI agent workflows introduce document types that don't exist in traditional SDLC:

| AI-Specific Artifact | Purpose | When Produced |
|---------------------|---------|---------------|
| **Agent Persona Template** | Identity, capabilities, constraints for a role | Planning |
| **Skill Definition** | What a skill does, when to invoke, parameters | Planning |
| **Stage Skill** | Per-stage instructions injected into agent context | Design |
| **Hook Configuration** | Pre/post tool-use enforcement rules | Design |
| **Prompt Queue** | Queued prompts for batch execution | Planning |
| **Completion Log** | What was done, what passed, what concerns | Closure |
| **Compliance Report** | Stage boundary violations, gate results | Monitoring |
| **Agent Concern** | Design mismatch, potential bug, scope wrong | Any stage |
| **Context Rebuild Script** | Instructions re-injected after context compaction | Infrastructure |

The PEV (Plan-Execute-Verify) loop from agentic engineering maps directly to our stage-gate system:
- **Plan** = Document + Design stages (specify quality gates, decompose into agent-sized tasks)
- **Execute** = Scaffold + Implement stages (agents work autonomously within constraints)
- **Verify** = Test stage (humans review against objectives, not rubber-stamp)

### 5. ADR Has Multiple Variants — Not One Format

Architecture Decision Records have at least 5 recognized formats:

| ADR Variant | Origin | Key Difference |
|------------|--------|---------------|
| **Nygard ADR** | Michael Nygard (2011) | Lightweight, status-based, original format |
| **MADR** | Markdown ADR project | Includes tradeoff analysis, options with pros/cons |
| **Y-Statement** | G. Fairbanks | One-sentence decision format: "In context C, facing F, we decided D..." |
| **IBM UMF** | IBM | Table layout, enterprise-oriented |
| **Tyree-Akerman** | CapitalOne | Forces, consequences, related decisions |

Beyond ADRs, the broader category of "Architecture Records" includes: Pattern Descriptions, Approved Standards, Exception Requests, and Compliance Assessments. Each is a form of decision record with different structure.

### 6. Knowledge Management Has Its Own Artifact Types

From Zettelkasten and PARA research:

| Knowledge Artifact | Purpose | Lifecycle |
|-------------------|---------|-----------|
| **Fleeting Note** | Quick capture, unprocessed | Minutes (process or discard) |
| **Literature Note** | Source synthesis, in your words | Created during reading |
| **Permanent Note** | Atomic insight, linked to others | Long-lived, evolving |
| **Index/MOC** | Map of Content, navigation hub | Updated as notes grow |
| **Project Note** | Active work context | Lifecycle of the project |
| **Area Note** | Ongoing responsibility tracking | Persistent |
| **Resource Note** | Reference material | Reference lifetime |
| **Archive Note** | Completed/inactive material | Permanent cold storage |

Our wiki's knowledge layer (lesson, pattern, decision, source-synthesis, concept) maps partially to this but misses: fleeting notes (raw/notes/ fills this), MOCs (our _index.md files), and the project/area/resource/archive distinction (our backlog partially covers this).

### 7. The OpenArms Document Chain — The Most Evolved Instance

OpenArms's `methodology-document-chain.md` (846 lines) is the most detailed artifact specification in our ecosystem. It defines a 24-artifact chain for Feature Development:

| Stage | Artifacts | Document Types |
|-------|-----------|---------------|
| **Document** (3) | Requirements Spec, Infrastructure Analysis, Gap Analysis | FR/NFR/AC format, File:line:export tables, Per-gap analysis |
| **Design** (5) | ADR, Tech Spec, Interface Spec, Config Spec, Test Plan | Decision + alternatives, Component + API tables, Complete types, YAML shapes + env vars, Test IDs + inputs + expected |
| **Scaffold** (3) | Type Definitions, Test Stubs, Config Wiring | TypeScript types, Placeholder assertions, Parent config modifications |
| **Implement** (2) | Implementation Files, Integration Wiring | Business logic, Existing file modified with import |
| **Test** (2) | Test Implementations, Test Results | Real assertions, Gate command output |
| **Harness** (4) | Frontmatter, Git Commits, Epic Readiness, Completion Log | Automatic per stage |

**Key principle from OpenArms:** "The documents ARE the gates. You CANNOT skip documents. The scaffold stage won't pass validation if there's no interface spec to scaffold FROM."

But OpenArms is TypeScript-specific. Its artifacts assume: pnpm, vitest, TypeScript types, Zod schemas, .env files. A Python project, infrastructure project, or knowledge project would have entirely different artifact types at scaffold/implement/test stages while sharing the same document types at document/design stages.

### 8. Per-Domain Variation Is the Core Design Challenge

The same methodology MODEL (e.g., Feature Development) produces different artifacts depending on the domain:

| Stage | TypeScript (OpenArms) | Python (Wiki) | Infrastructure (IaC) | Knowledge (Wiki Evolution) |
|-------|--------------------|---------------|---------------------|--------------------------|
| Document | Wiki pages (same) | Wiki pages (same) | Wiki pages (same) | Wiki pages (same) |
| Design | TypeScript types in docs, API tables | Python function signatures in docs | Terraform resource specs in docs | Page structure specs in docs |
| Scaffold | .ts type files, .test.ts stubs | .yaml configs, .py stubs | .tf variable definitions | Template files, frontmatter schemas |
| Implement | .ts business logic, bridge modules | .py tool code, pipeline extensions | .tf resource blocks, modules | Wiki page content, relationship wiring |
| Test | vitest assertions | pipeline post validation | terraform plan/apply | pipeline post, lint checks |

**The document/design stages are largely DOMAIN-AGNOSTIC.** Requirements specs, gap analyses, ADRs, tech specs work the same regardless of domain. The scaffold/implement/test stages are DOMAIN-SPECIFIC — the artifact types change completely based on the technology stack.

This means the artifact system needs two layers:
1. **Universal artifacts** (documents) — same structure everywhere, defined once
2. **Domain artifacts** (code/config/infrastructure) — defined per domain profile

### 9. Operations Plan vs Design Plan — Two Fundamentally Different Documents

From both the SDLC research and the operator's directive:

| Dimension | Operations Plan | Design Plan |
|-----------|----------------|-------------|
| **Purpose** | Execute a known sequence mechanically | Analyze an unknown problem with trade-offs |
| **Structure** | Steps with Action → Expected → Validation → Rollback | Problem → Options → Decision → Rationale |
| **Judgment** | Zero — any agent can follow it | High — requires expertise and context |
| **SDLC parallel** | Production Implementation Plan, Installation Guide | Analysis & Design Document, Architecture Plan |
| **Agile parallel** | Deployment Runbook, Migration Script | Design Spike, ADR |
| **When produced** | After design is complete — during implement/deploy | During design stage — before any implementation |

The real-world SDLC separates these clearly. Our methodology conflated them until we added the `operations-plan` type, but the DEPTH of that distinction needs much more work.

### 10. The Artifact Lifecycle — Documents Evolve Through Stages

From both SDLC research and the Zettelkasten method, artifacts have a lifecycle:

```
Draft → Active → Reviewed → Approved → Superseded → Archived
```

For methodology documents specifically:
- **Requirements Spec** starts as draft during document stage, becomes the constraint for design stage
- **ADR** starts as proposed, becomes accepted when the team agrees, can be superseded by a new ADR
- **Test Plan** starts as draft during design, becomes the template for test stubs during scaffold
- **Completion Log** is generated at the end, capturing what actually happened vs what was planned

This lifecycle means documents are not static — they're living artifacts that feed forward into later stages and backward into reviews.

## Deep Analysis

### The Complete Artifact Taxonomy — All 77 Types

> [!abstract] 11 Categories, 77 Artifact Types
>
> | # | Category | Artifact Types | Count |
> |---|----------|---------------|-------|
> | 1 | **Initiation** | Project Charter, Business Case, Feasibility Study, CONOPS, Cost-Benefit Analysis, Stakeholder List, Resource Plan | 7 |
> | 2 | **Planning** | Statement of Work, Project Plan, WBS, Risk Analysis, Procurement Plan, Roles Matrix, Approvals Matrix, Config Management Plan | 8 |
> | 3 | **Requirements** | BRD, FRD, Use Cases, RTM, SRS, Requirements Inspection Checklist, SLA Template | 7 |
> | 4 | **Design** | ADR, Tech Spec, Interface Spec, Config Spec, HLD, LLD, Database Design, UI/UX Artifacts, API Spec, Test Plan | 10 |
> | 5 | **Construction** | Source Code, Type Definitions, Schemas, Bridge/Adapter Modules, Integration Wiring, Config Files, Env Examples | 7 |
> | 6 | **Testing** | Test Plan, Test Cases, Test Stubs, Test Implementations, UAT Plan, Bug Reports, Regression Plan, Test Results | 8 |
> | 7 | **Deployment** | Installation Guide, User Guide, Admin Guide, Operations Guide, Production Plan, Runbooks, Release Notes | 7 |
> | 8 | **Closure** | Lessons Learned, Post-Project Review, Knowledge Transfer, Completion Log, Retirement Plan | 5 |
> | 9 | **Monitoring** | Change Log, Risk Register, Status Reports, Issue Log, Compliance Reports | 5 |
> | 10 | **Knowledge** | Research Pages, Lessons, Patterns, Decisions, Comparisons, Source Syntheses, Deep Dives, Domain Overviews | 8 |
> | 11 | **AI Agent** | Persona Templates, Skill Definitions, Stage Skills, Hook Configs, Prompt Queues, Compliance Reports | 6 |
> | | **TOTAL** | | **78** |

### What Our Wiki Currently Covers vs the Full Taxonomy

> [!warning] Coverage Gap
>
> | Category | Full Taxonomy | Our Wiki Types | Coverage |
> |----------|--------------|---------------|----------|
> | Initiation | 7 | 0 | 0% |
> | Planning | 8 | 1 (epic) | 12% |
> | Requirements | 7 | 1 (concept used for specs) | 14% |
> | Design | 10 | 2 (decision, reference) | 20% |
> | Construction | 7 | 0 (not wiki pages) | N/A |
> | Testing | 8 | 0 (not wiki pages) | N/A |
> | Deployment | 7 | 1 (operations-plan) | 14% |
> | Closure | 5 | 2 (note, lesson) | 40% |
> | Monitoring | 5 | 0 | 0% |
> | Knowledge | 8 | 8 (all knowledge types) | 100% |
> | AI Agent | 6 | 0 | 0% |
>
> **Knowledge types: 100% covered. Everything else: 0-40%.** This is exactly the "20% subset" the operator identified.

### Recommended Path

Based on the research, the methodology artifact system needs:

1. **A complete taxonomy page** defining all artifact types across all categories — what each one IS, when it's produced, what it contains, who the audience is

2. **Per-category standards** — not per wiki-page-type standards (which is what we built before), but per artifact-CATEGORY standards that cover the entire spectrum including non-wiki artifacts

3. **Per-domain artifact chains** — the full chain for each methodology model, resolved per domain. OpenArms's 24-artifact chain is the TypeScript instance. We need equivalent chains for Python/wiki, infrastructure, and knowledge domains.

4. **Universal vs domain-specific separation** — document/design stage artifacts are universal (same structure everywhere). Scaffold/implement/test artifacts vary by domain. The system must handle both layers.

5. **Lifecycle rules** — documents evolve (draft → active → approved → superseded). The system must track this.

6. **Integration with the LLM Wiki** — every artifact type that CAN be a wiki page should have: a page type, a template, a standards doc, and an exemplar. Types that AREN'T wiki pages (binaries, test results, git commits) should still be defined and tracked in the methodology chain.

## Open Questions

> [!question] How many of the 78 artifact types should be wiki page types vs tracked-but-not-pages? (Requires: design decision — probably 25-30 page types, rest tracked in frontmatter)

> [!question] Should the taxonomy distinguish between mandatory and optional artifacts per model? (Yes — OpenArms does this with required/optional in methodology.yaml. Needs generalization.)

> [!question] How do we handle the 12 SDLC initiation documents? These don't map to our stage-gate system which starts at Document. (Requires: design — possibly a "pre-document" or "charter" stage for epic-scale work)

> [!question] Should ADR variants (Nygard, MADR, Y-Statement) be separate templates or one template with variant guidance? (Requires: design decision)

### How This Connects — Navigate From Here

> [!abstract] From This Source → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principles derive from this?** | Check FEEDS INTO relationships above |
> | **What is the Goldilocks framework?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- FEEDS INTO: [[model-methodology|Model — Methodology]]
- FEEDS INTO: [[methodology-framework|Methodology Framework]]
- FEEDS INTO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[task-type-artifact-matrix|Task Type Artifact Matrix]]
- RELATES TO: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]

## Backlinks

[[model-methodology|Model — Methodology]]
[[methodology-framework|Methodology Framework]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[coverage-blindness-modeling-only-what-you-know|Coverage Blindness — Modeling Only What You Know]]
[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[three-classes-of-methodology-output|Three Classes of Methodology Output]]

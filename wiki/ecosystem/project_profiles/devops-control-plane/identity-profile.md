---
title: "devops-control-plane — Identity Profile"
aliases:
  - "devops-control-plane — Identity Profile"
type: reference
domain: cross-domain
status: synthesized
confidence: medium
maturity: growing
created: 2026-04-13
updated: 2026-04-13
sources:
  - id: dcp-concept
    type: wiki
    file: wiki/domains/devops/devops-control-plane.md
  - id: dcp-claude
    type: file
    file: raw/articles/devops-control-plane-claude.md
  - id: dcp-architecture
    type: file
    file: raw/articles/devops-control-plane-docs-architecture.md
  - id: dcp-readme
    type: file
    file: raw/articles/devops-control-plane-readme.md
tags: [ecosystem, project-profile, devops-control-plane, identity, goldilocks]
---

# devops-control-plane — Identity Profile

## Summary

The second brain's understanding of devops-control-plane as an ecosystem member. The control plane is a unified solution management platform (Python) with three interfaces: interactive TUI (manage.sh), CLI (Click), and web dashboard (Flask SPA). It auto-detects 20 technology stacks, provides AES-256-GCM encrypted vaults, an append-only audit ledger, and pluggable adapter architecture. Its most significant contribution to the ecosystem is as an operational DNA donor: 24 immune system rules derived from 16 post-mortems became OpenFleet's doctor.py. The control plane's own CLAUDE.md uses a rule-heavy enforcement approach (24 mandatory rules) that predates the methodology framework.

## Identity (Goldilocks 7 Dimensions)

> [!info] devops-control-plane Goldilocks Profile
>
> | Dimension | Value | Evidence |
> |-----------|-------|---------|
> | **Type** | product (infrastructure management platform) | TUI + CLI + Web dashboard, 29 service packages |
> | **Execution Mode** | Solo | Human + Claude in conversation, rule-heavy CLAUDE.md |
> | **Domain** | Infrastructure Management (Python) | Python 3.12, Click, Flask, Pydantic v2 |
> | **Phase** | Production | Used for project management with active vault, detection engine |
> | **Scale** | Medium-Large (29 service packages, 19 CLI domain packages) | Broad surface area: vault, content, pages, git, backup, secrets, audit, k8s, terraform, docker |
> | **PM Level** | L1 (CLAUDE.md directives + rules) | 24 mandatory rules in .agent/rules/, workflow routing checklists |
> | **Trust Tier** | Operator-supervised | Solo execution with heavy rule enforcement |
> | **SDLC Chain** | Simplified | Lighter process — workflow checklists over stage gates |

## Execution Mode Detail

> [!abstract] Rule-Based Agent Control
>
> The control plane uses an older enforcement pattern than the methodology framework: 24 mandatory rules loaded at session start via `.agent/rules/`. These rules emerged from 16 post-mortems — each rule maps to a real failure. This predates the wiki's methodology.yaml / stage-gate approach.
>
> | Rule Category | Examples |
> |---------------|---------|
> | Anti-rogue constraints | USER-drives-YOU-obey, STOP-means-DISCARD |
> | Process integrity | NO-silent-assumptions, NO-compression, NO-fast-over-right |
> | Context safety | STOP-CONTEXT-WAS-TRUNCATED, POST-CHECKPOINT-QUARANTINE |
> | Code discipline | READ-ALL-callers, GREP-FIRST, ONE-SCOPE, refactoring-integrity |
> | Escalation | CORRECTION-ESCALATION (3 corrections = corrupted) |
>
> This rule set was the evolutionary ancestor of OpenFleet's immune system rules.

## What the Brain Learned FROM devops-control-plane

> [!tip] Key Lessons Contributed
>
> | Lesson | What devops-control-plane Proved |
> |--------|-------------------------------|
> | [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]] | 24 rules from 16 post-mortems — each rule exists because an instruction-only approach failed |
> | [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible Not Manual]] | Three-Layer Touch Rule: a feature touching 3+ layers = wrong design. Adapter architecture enables swapping without core changes. |
> | [[always-plan-before-executing|Always Plan Before Executing]] | Engine cycle: load → detect → plan → execute → persist → audit. Planning is a structural step, not a suggestion. |

> [!tip] Key Patterns Observed
>
> | Pattern | How devops-control-plane Implements It |
> |---------|-------------------------------------|
> | [[deterministic-shell-llm-core|Deterministic Shell, LLM Core]] | Engine is pure Python logic: detect stacks, plan operations, execute via adapters. No LLM calls in core loop. |
> | [[scaffold-foundation-infrastructure-features|Scaffold, Foundation, Infrastructure, Features]] | 5-layer architecture: Interfaces → Core Domain → Policy → Adapters → Invariant Infrastructure |
> | [[enforcement-hook-patterns|Enforcement Hook Patterns]] | Workflow routing checklists (.agent/workflows/) serve as pre-action gates |

## Unique Contributions

- **Vault security as a shared service potential**: AES-256-GCM encrypted vaults (PBKDF2-SHA256, 100,000 KDF iterations, auto-lock) could serve as centralized credential store for all ecosystem projects. Not yet implemented as a shared service.
- **24 immune system rules**: These rules are the primary operational DNA exported to OpenFleet's doctor.py. The 3-strike rule, behavioral security, and anomaly detection patterns all originated here. See [[immune-system-rules|Immune System Rules]].
- **Tech auto-detection for project identity**: 20 technology stack definitions with detection rules — auto-scans project directories and reports capabilities. This is a rudimentary form of the Goldilocks self-identification pattern: detecting WHAT a project is before deciding how to manage it.
- **16 post-mortems as knowledge source**: `.agent/workflows/failures/AI-POSTMORTEM-IMPORTANT-*.md` — each post-mortem generated operational rules. This provenance chain (failure → post-mortem → rule → codified in doctor.py) is the most complete failure-to-governance pipeline in the ecosystem.

## Artifact Chain (Project-Specific)

The control plane does not use the wiki's methodology.yaml / stage-gate system. Its artifact chain is workflow-driven:

> [!abstract] devops-control-plane Artifact Pattern
>
> | Category | Artifacts | Notes |
> |----------|-----------|-------|
> | Rules | 24 in .agent/rules/ | Loaded at session start, mandatory |
> | Workflows | .agent/workflows/ | Pre-change checklists per domain (backend, frontend, refactoring) |
> | Plans/Specs | .agent/plans/, .agent/specs/ | Generated during work, stored in project |
> | Post-mortems | 16 in .agent/workflows/failures/ | Source of immune system rules |
> | Architecture | .agent/reference/ | Design docs, exploration reports |

**Toolchain:** Python 3.12, Click, Flask + Jinja2, Pydantic v2, cryptography (AES-256-GCM), pytest, ruff, mypy, GitHub Actions

## Methodology Adaptations

> [!info] How devops-control-plane Diverges From the Methodology
>
> | Aspect | Standard (Wiki) | devops-control-plane Approach |
> |--------|-----------------|------------------------------|
> | Enforcement model | methodology.yaml with stage gates | 24 mandatory rules loaded at session start |
> | Stage progression | 5 stages (document→design→scaffold→implement→test) | Workflow checklists, not stage gates |
> | Post-mortems | Evolved into lessons/patterns | Kept as raw .md files in .agent/workflows/failures/ |
> | File output | Wiki pages with frontmatter | Project-internal .agent/ directory |
> | PM level | L1-L3 depending on project | L1 with rule-heavy enforcement (almost L2 in spirit) |
>
> The control plane's rule-based approach was the first enforcement pattern in the ecosystem. The methodology framework is the evolution of this approach into a more structured, stage-gated, artifact-chained system.

## Integration with Second Brain

> [!abstract] Adoption Status
>
> | Component | Status |
> |-----------|--------|
> | CLAUDE.md as routing table | Adopted (pre-methodology, rule-heavy variant) |
> | Three-layer root docs (AGENTS.md + CLAUDE.md + Skills) | Not adopted — candidate upgrade. `.agent/rules/` already acts as Layer 3; Layer 1 AGENTS.md would consolidate the 24 mandatory rules into cross-tool format. See [[root-documentation-map|Root Documentation Map]] |
> | methodology.yaml | Not adopted (uses .agent/rules/ instead) |
> | Stage enforcement | Not adopted (uses workflow checklists) |
> | Wiki knowledge base | Not connected |
> | Export from second brain | Not connected |
> | Feed-back TO second brain | Active (immune system rules, post-mortem → lesson pipeline, architecture patterns) |

### How This Connects — Navigate From Here

> [!abstract] From This Profile → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Ecosystem overview** | [[four-project-ecosystem|Four-Project Ecosystem]] |
> | **Concept page** | [[devops-control-plane|devops-control-plane]] |
> | **Immune system rules** | [[immune-system-rules|Immune System Rules]] |
> | **Generic artifact framework** | [[artifact-chains-by-model|Artifact Chains by Methodology Model]] |
> | **Methodology model** | [[model-methodology|Model — Methodology]] |
> | **Ecosystem model** | [[model-ecosystem|Model — Ecosystem Architecture]] |
> | **Infrastructure patterns** | [[infrastructure-as-code-patterns|Infrastructure as Code Patterns]] |

## Relationships

- PART OF: [[four-project-ecosystem|Four-Project Ecosystem]]
- DERIVED FROM: [[devops-control-plane|devops-control-plane]]
- ENABLES: [[immune-system-rules|Immune System Rules]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]]
- RELATES TO: [[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
- FEEDS INTO: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]

## Backlinks

[[four-project-ecosystem|Four-Project Ecosystem]]
[[devops-control-plane|devops-control-plane]]
[[immune-system-rules|Immune System Rules]]
[[model-methodology|Model — Methodology]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]

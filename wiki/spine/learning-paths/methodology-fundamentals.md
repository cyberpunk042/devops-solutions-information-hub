---
title: Learning Path — Methodology Fundamentals
aliases:
  - "Learning Path — Methodology Fundamentals"
  - "Learning Path: Methodology Fundamentals"
type: learning-path
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-12
sources: []
tags: [learning-path, methodology, onboarding, fundamentals]
---

# Learning Path — Methodology Fundamentals
## Summary

Guided sequence for understanding the research wiki's methodology system — from what a methodology model IS, through stage-gate execution, to artifact chains and quality tiers. After completing this path, you should be able to select the right model for any task, follow its stage sequence, and produce correct artifacts at each stage.

## Prerequisites

- Read wiki/spine/model-registry.md to understand the model system
- Basic familiarity with YAML and markdown
- Access to the research wiki (this repo)

## Sequence

### Part 1: Understanding the System (LEARN mode)

1. **[[methodology-framework|Methodology Framework]]** — Start here. Defines what a methodology model IS: Name + Stages + Gates + Protocols + Parameters. Models are DATA, not code — configurations that shape execution.

2. **[[stage-gate-methodology|Stage-Gate Methodology]]** — The 5 universal stages (Document → Design → Scaffold → Implement → Test). Pay attention to ALLOWED/FORBIDDEN lists — these are the hard boundaries that prevent most failures.

3. **[[model-methodology|Model — Methodology]]** — The 9 named models and their stage sequences. Focus on Feature Development (most complex) and Documentation (simplest) as two endpoints.

4. **[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]** — The full spectrum: 78 artifact types across 11 categories. Learn the 3-class distinction: artifact (by-product), document (constraining spec), documentation (explaining). This changes how you think about what you produce.

### Part 2: Making Decisions (DECIDE mode)

5. **[[task-type-artifact-matrix|Task Type Artifact Matrix]]** — How task type determines which model to use. The matrix prevents over-process on simple work and enforces full staging on complex work.

6. **[[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]** — Quality tiers. Choosing your tier is EXPLICIT — Mountain (chaos) is never acceptable. Pyramid (deliberate compression) requires documented reasoning.

7. **[[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]]** — The 17 document/design artifact types with chain dependencies. ADR depends on requirements. Tech spec depends on ADR. Breaking the chain means building without blueprints.

### Part 3: Executing Work (EXECUTE mode)

8. **[[artifact-chains-by-model|Artifact Chains by Methodology Model]]** — What each stage produces for each model. Study the Feature Development worked example — all 5 stages, all required artifacts.

9. **Your domain chain** — Read the one for YOUR tech stack:
   - [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]] — pnpm, vitest, Zod
   - [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]] — pipeline post, YAML configs
   - [[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]] — Terraform, Docker
   - [[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]] — L0-L6 progressive distillation

10. **[[execution-modes-and-end-conditions|Execution Modes and End Conditions]]** — How agents execute: autonomous, semi-autonomous, document-only. The 14-step work loop is the atomic unit.

### Part 4: Advanced Topics

11. **[[model-composition-rules|Model Composition Rules]]** — How models combine: sequential, nested, conditional, parallel.

12. **[[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]** — 4 entry paths, 3 consumption modes, active vs passive. The wiki is a THINKING PARTNER, not a reference manual.

13. **[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]** — Gold standards with real examples, anti-patterns, execution checklists. Read this BEFORE declaring work done.

### Part 5: Agent Enforcement (how to make agents follow methodology)

14. **[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]** — Instructions=25%, hooks=100%. The quantified proof that process rules need infrastructure.
15. **[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]** — Even with 100% stage compliance, 6 behavioral failure classes persist. Know them.
16. **[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]** — Prevention → Detection → Correction. The complete enforcement architecture.
17. **[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]** — Every block needs a reason. Blind enforcement creates its own failures.

### Part 6: Key Lessons (prevent known failures)

18. **[[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]** — "Continue" = current stage, NOT next stage.
19. **[[always-plan-before-executing|Always Plan Before Executing]]** — Planning costs 1x. Rework costs 5.5x.
20. **[[three-classes-of-methodology-output|Three Classes of Methodology Output]]** — Different classes need different quality rules.
21. **[[coverage-blindness-modeling-only-what-you-know|Coverage Blindness — Modeling Only What You Know]]** — 100% of 20% = invisible incompleteness.
22. **[[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]]** — Copying instance values ≠ building a framework.
23. **[[new-content-must-integrate-into-existing-pages|New Content Must Integrate Into Existing Pages]]** — If the entry points don't link to it, it doesn't exist.
24. **[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]** — Markdown IS programming for AI. Structure > content.

### Part 7: Principles (the governing truths distilled from lessons)

25. **[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]** — HOW to enforce: any tool-call-level rule must be infrastructure, not instructions. Quantified: 25%→100%.
26. **[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]** — WHY it works: structure programs behavior. Prose requires parsing. Parsing fails under pressure.
27. **[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]** — WHEN to apply: process is a FUNCTION of identity, not a fixed configuration. POC ≠ Production.

### Part 8: The Goldilocks Protocol (putting it all together)

28. **[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]** — Answer the 7 questions. Get your identity profile. Select your chain, enforcement, and depth.
29. **[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]** — Phase × scale → chain. Simplified, default, or full.
30. **[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]** — L1→L2→L3. Harness v1→v3. Each wraps the previous.

## Outcomes

After completing this path you should be able to:
- Answer the 7 Goldilocks identity questions for any project
- Select the correct SDLC chain (simplified/default/full) based on phase and scale
- Select the correct methodology model for any task type and scale
- Identify the 3 classes of output and apply the right quality rules per class
- Follow the stage sequence and produce correct artifacts at each stage
- Identify ALLOWED and FORBIDDEN actions at each stage
- Choose an appropriate quality tier with documented reasoning
- Know the full 78-type artifact spectrum (not just the 17 wiki page types)
- Choose the right enforcement level for your project (instructions → hooks → harness → immune system)
- Identify the 6 behavioral failure classes and their mitigations
- Design mindful enforcement with justified bypass mechanisms
- Recognize when structured context is more effective than natural language instructions
- Read and follow your domain-specific artifact chain
- Understand how models compose for complex, multi-layered work
- Use the wiki as an active thinking partner, not a passive reference
- Configure a project to adopt the methodology at any of the 4 tiers
- Recognize and prevent the most common methodology failures

## Relationships

- BUILDS ON: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[methodology-adoption-guide|Methodology Adoption Guide]]
- RELATES TO: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[model-methodology|Model — Methodology]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]

---
title: "Learning Path: Methodology Fundamentals"
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

# Learning Path: Methodology Fundamentals

## Summary

Guided sequence for understanding the research wiki's methodology system — from what a methodology model IS, through stage-gate execution, to artifact chains and quality tiers. After completing this path, you should be able to select the right model for any task, follow its stage sequence, and produce correct artifacts at each stage.

## Prerequisites

- Read wiki/spine/model-registry.md to understand the model system
- Basic familiarity with YAML and markdown
- Access to the research wiki (this repo)

## Sequence

### Part 1: Understanding the System (LEARN mode)

1. **[[Methodology Framework]]** — Start here. Defines what a methodology model IS: Name + Stages + Gates + Protocols + Parameters. Models are DATA, not code — configurations that shape execution.

2. **[[Stage-Gate Methodology]]** — The 5 universal stages (Document → Design → Scaffold → Implement → Test). Pay attention to ALLOWED/FORBIDDEN lists — these are the hard boundaries that prevent most failures.

3. **[[Model: Methodology]]** — The 9 named models and their stage sequences. Focus on Feature Development (most complex) and Documentation (simplest) as two endpoints.

4. **[[Methodology Artifact Taxonomy]]** — The full spectrum: 78 artifact types across 11 categories. Learn the 3-class distinction: artifact (by-product), document (constraining spec), documentation (explaining). This changes how you think about what you produce.

### Part 2: Making Decisions (DECIDE mode)

5. **[[Task Type Artifact Matrix]]** — How task type determines which model to use. The matrix prevents over-process on simple work and enforces full staging on complex work.

6. **[[Skyscraper, Pyramid, and Mountain]]** — Quality tiers. Choosing your tier is EXPLICIT — Mountain (chaos) is never acceptable. Pyramid (deliberate compression) requires documented reasoning.

7. **[[Requirements and Design Artifacts — Standards and Guide]]** — The 17 document/design artifact types with chain dependencies. ADR depends on requirements. Tech spec depends on ADR. Breaking the chain means building without blueprints.

### Part 3: Executing Work (EXECUTE mode)

8. **[[Artifact Chains by Methodology Model]]** — What each stage produces for each model. Study the Feature Development worked example — all 5 stages, all required artifacts.

9. **Your domain chain** — Read the one for YOUR tech stack:
   - [[Artifact Chain: TypeScript/Node Domain]] — pnpm, vitest, Zod
   - [[Artifact Chain: Python/Wiki Domain]] — pipeline post, YAML configs
   - [[Artifact Chain: Infrastructure/IaC Domain]] — Terraform, Docker
   - [[Artifact Chain: Knowledge/Evolution Domain]] — L0-L6 progressive distillation

10. **[[Execution Modes and End Conditions]]** — How agents execute: autonomous, semi-autonomous, document-only. The 14-step work loop is the atomic unit.

### Part 4: Advanced Topics

11. **[[Model Composition Rules]]** — How models combine: sequential, nested, conditional, parallel.

12. **[[How AI Agents Consume the Methodology Wiki]]** — 4 entry paths, 3 consumption modes, active vs passive. The wiki is a THINKING PARTNER, not a reference manual.

13. **[[Methodology Standards — What Good Execution Looks Like]]** — Gold standards with real examples, anti-patterns, execution checklists. Read this BEFORE declaring work done.

### Part 5: Key Lessons (prevent known failures)

14. **[[Never Skip Stages Even When Told to Continue]]** — "Continue" = current stage, NOT next stage.
15. **[[Always Plan Before Executing]]** — Planning costs 1x. Rework costs 5.5x.
16. **[[Three Classes of Methodology Output]]** — Different classes need different quality rules.
17. **[[Coverage Blindness — Modeling Only What You Know]]** — 100% of 20% = invisible incompleteness.

## Outcomes

After completing this path you should be able to:
- Select the correct methodology model for any task type and scale
- Identify the 3 classes of output and apply the right quality rules per class
- Follow the stage sequence and produce correct artifacts at each stage
- Identify ALLOWED and FORBIDDEN actions at each stage
- Choose an appropriate quality tier with documented reasoning
- Know the full 78-type artifact spectrum (not just the 17 wiki page types)
- Read and follow your domain-specific artifact chain
- Understand how models compose for complex, multi-layered work
- Use the wiki as an active thinking partner, not a passive reference
- Configure a project to adopt the methodology at any of the 4 tiers
- Recognize and prevent the most common methodology failures

## Relationships

- BUILDS ON: [[Model: Methodology]]
- BUILDS ON: [[Methodology Adoption Guide]]
- RELATES TO: [[Model: LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[Super-Model: Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[Model: Methodology]]
[[Methodology Adoption Guide]]
[[Model: LLM Wiki Standards — What Good Looks Like]]
[[Super-Model: Research Wiki as Ecosystem Intelligence Hub]]

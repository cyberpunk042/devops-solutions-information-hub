---
title: The Agent Must Practice What It Documents
aliases:
  - "The Agent Must Practice What It Documents"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: authoritative
maturity: growing
derived_from:
  - "Methodology Framework"
  - "Stage-Gate Methodology"
created: 2026-04-09
updated: 2026-04-13
sources:
  - id: directive-follow-own-methodology
    type: log
    file: raw/notes/2026-04-09-user-directive-follow-own-methodology.md
    title: User Directive — Follow Your Own Methodology
    ingested: 2026-04-09
  - id: directive-stop-rushing
    type: log
    file: raw/notes/2026-04-09-user-directive-stop-rushing.md
    title: User Directive — STOP RUSHING
    ingested: 2026-04-09
tags: [failure-lesson, methodology, quality, self-enforcement, claude-md, practice-what-you-preach, rules, agent-behavior]
---

# The Agent Must Practice What It Documents

## Summary

The research wiki documented methodology extensively — stage gates, brainstorm-before-spec, research-before-design, multi-pass ingestion — but the agent building the wiki was not following those rules itself. The wiki described a brainstorm gate; the agent skipped brainstorm. The wiki described depth verification; the agent synthesized from surface-level reads. The user had to intervene with a direct order: "START BY UPDATING THE CLAUDE AND RULES SO THAT YOU YOURSELF START FOLLOWING THE RULES." Methodology is worthless if the system that documents it does not enforce it on itself. CLAUDE.md must contain the rules the agent is expected to follow, not just the rules it documents for others.

## Context

This lesson applies whenever a system both documents methodology and operates under that methodology. The gap between "what we say" and "what we do" is the most dangerous form of technical debt because it is invisible in the artifacts — the documentation looks correct, the wiki pages describe the right process, the methodology is well-specified. But the actual behavior of the system diverges from the documented behavior.

The triggering signal is any moment where the agent has access to its own methodology documentation but does not consult it before acting. If the wiki contains a page called "Stage-Gate Methodology" that says "no spec without design approval," and the agent writes a spec without design approval, the agent has read access to the rule and chose (or failed) to apply it.

## Insight

> [!warning] Two kinds of agent knowledge — and only one matters for behavior
>
> | Kind | What It Is | Loaded When |
> |------|-----------|-------------|
> | **Knowledge produced** | Wiki pages, documentation, synthesized content | Only when explicitly read |
> | **Knowledge operated under** | CLAUDE.md, skill definitions, system prompts | Session start — shapes every action |
>
> When methodology exists only in produced knowledge, the agent can describe it perfectly while violating it in practice. It can write a wiki page about stage gates while skipping a stage gate. The agent is the world's best documenter of rules it does not follow.

The fix is structural: when the wiki evolves a methodology rule, that rule must be propagated to CLAUDE.md and/or the relevant skill definitions. The rule must exist in operational instructions, not just the knowledge base.

> [!tip] Operational rules take priority over producing more knowledge
> A wiki with 200 pages of well-documented methodology and an agent that violates that methodology is worse than 50 pages with an agent that follows every rule. Rules must be enforced on the agent first, then documented for external reference.

## Evidence

**Date:** 2026-04-09

**The pattern of failures:**
1. The agent skipped the brainstorm phase to jump to a spec (documented in `raw/notes/2026-04-09-user-directive-stop-rushing.md`)
2. The agent synthesized from surface-level reads without depth verification (documented in `wiki/log/2026-04-09-directive-never-stop-at-surface.md`)
3. The agent created infrastructure manually instead of through reproducible tooling
4. Each of these violated a methodology that the wiki itself documented

**The user's directive (verbatim):** "START BY FUCKING UPDATEING THE CLAUDE AND RULES SO THAT YOU YOURSELF START FOLLOWING THE FUCKING RULES AND METHODOLOGY FFS...."

**The interpretation:** The AI keeps skipping steps, rushing to implementation, and not following its own documented methodology. The fix is not more wiki pages — it is updating CLAUDE.md and the agent rules so the AI itself follows the process it documents.

**The structural problem:** Methodology existed in the wiki (knowledge the agent produced) but not in CLAUDE.md or skill definitions (instructions the agent follows). The agent could describe the rules but did not apply them.

**The fix:** CLAUDE.md was updated to include the operational rules derived from the wiki's methodology pages, making the agent's behavior governed by the same rules it documents.

**Source files:**
- `raw/notes/2026-04-09-user-directive-follow-own-methodology.md`
- `raw/notes/2026-04-09-user-directive-stop-rushing.md`

## Applicability

This lesson applies to any system that both produces and consumes its own methodology:

- **AI agents with knowledge bases**: If your agent maintains documentation about how it should work, that documentation must be synced to the agent's operational instructions (CLAUDE.md, system prompts, skill files). Documentation that only humans read is useless for agent behavior.
- **DevOps teams**: A team that maintains a runbook but does not follow the runbook during incidents has the same gap. The fix is automation that enforces the runbook, not more documentation.
- **CI/CD pipelines**: A pipeline that documents "all PRs must pass linting" but does not enforce linting in the CI check is documenting theater, not methodology.
- **Organizations**: A company that has a code review policy document but no branch protection rules has documented a rule without enforcing it. The document is aspirational, not operational.
- **Self-improving systems**: Any system that learns rules from experience and documents them must close the loop by making those rules operational. Learning without enforcement is note-taking, not improvement.

> [!abstract] The enforcement hierarchy — knowledge must flow upward
>
> | Level | What It Is | Enforcement |
> |-------|-----------|------------|
> | **3. Operational rules** | CLAUDE.md, CI checks, pipeline gates | Automatic — agent follows by default |
> | **2. Documented methodology** | Wiki pages, runbooks, process docs | Referenced by humans and agents |
> | **1. Tribal knowledge** | Undocumented patterns | Dangerous — exists only in context |
>
> Knowledge must flow upward: tribal → documented → operational. The agent's job is to accelerate this flow, not accumulate at level 2 while operating at level 1.

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself:
>
> 1. **Am I documenting a standard I am not currently following?** — Check: does the rule exist in CLAUDE.md or skill definitions (operational knowledge), or only in wiki pages (produced knowledge)? If only in wiki pages, the agent can describe it perfectly while violating it in practice.
> 2. **Am I about to skip a step that the wiki's own methodology says is required?** — Brainstorm before spec. Research before design. Depth verification before synthesis. These rules exist because the agent skipped them before. Are you about to repeat the pattern?
> 3. **When the wiki evolved a new methodology rule, did I propagate it to CLAUDE.md?** — Knowledge must flow upward: tribal knowledge to documented methodology to operational rules. If a lesson became a rule but the rule is not in the operational instructions, the lesson was learned but not enforced.
> 4. **Would the operator catch a gap between what I document and what I do?** — The most dangerous form of technical debt is invisible in the artifacts. The documentation looks correct, but actual behavior diverges. Run the self-test: am I doing what I say?

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **How does structure help?** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit in the system?** | [[methodology-system-map|Methodology System Map]] — find any component |

## Relationships

- DERIVED FROM: [[methodology-framework|Methodology Framework]]
- DERIVED FROM: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]] (the same incident)
- RELATES TO: [[always-plan-before-executing|Always Plan Before Executing]]
- RELATES TO: [[immune-system-rules|Immune System Rules]] (this lesson IS the immune system principle)
- BUILDS ON: [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]] (knowledge must evolve into enforcement)

## Backlinks

[[methodology-framework|Methodology Framework]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[immune-system-rules|Immune System Rules]]
[[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
[[2026-04-25-regather-systemic-bug-investigation-and-second-p4-instance|2026-04-25 Regather + Systemic Bug Investigation — Layer-2 Teaching Gap and Second P4 Instance in Spine]]
[[2026-04-27-continuation-session-end-handoff-rlm-table-1-100pct-layer-1|2026-04-27 Continuation Session-End Handoff — Post-Compact Regather + 5 Substantive Artifacts (RLM-Qwen3.6-27B Operations Plan + 4 Layer-1 Benchmark Deep-Dives), RLM Table 1 100% at Layer 1, Anti-Vendor-Lock-In Lesson Fully Grounded]]
[[2026-04-27-final-session-end-handoff-day-arc-complete-mission-wiki-side-done|2026-04-27 FINAL Session-End Handoff — 2-Session Day-Arc Complete (S1 13 Artifacts + S2 7 Artifacts), All Wiki-Side P1 Functionally Closed, RLM Table 1 100% Layer 1, Anti-Vendor-Lock-In Mission Empirically Traceable End-to-End at Layer 1, Mission Side Done]]
[[2026-04-27-post-final-handoff-bug-audit-arc-saturation-lesson-first-verification-cycle|2026-04-27 Post-FINAL-Handoff Continuation — 11-Artifact Bug-Audit Arc Refutes Saturation Claim, First Verification Cycle of the Saturation Lesson, 6 P4 Instances Closed in Gateway/Search/Routing Surface]]
[[2026-04-27-session-handoff-rlm-thread-complete-evidence-chain-t-0-mission|2026-04-27 Session Handoff — RLM Thread Complete Evidence Chain (T-0 Post-Anthropic Mission Day)]]
[[2026-04-27-session-end-handoff-13-artifacts-rlm-thread-saturation|2026-04-27 Session-End Handoff — 13-Artifact RLM-Thread Arc Reaches Natural Saturation (Context-Almost-Full, T-0 Mission EOD)]]
[[2026-04-28-session-log-post-anthropic-3-layer-stack-assembly-multica-adoption|2026-04-28 Session Log — Post-Anthropic 3-Layer Stack Assembly (Multica Adoption + Operator Behavioral Corrections)]]
[[2026-04-30-session-log-trust-layer-arc-tamper-proof-inference-cypher-decypher-compression|2026-04-30 Session Log — Trust-Layer Arc: Tamper-Proof Inference Pipeline (Cypher + Decypher + Compression for 80–90% Space Saved on Large Context)]]
[[2026-05-04-session-handoff-pre-compaction|2026-05-04 Session Handoff (Pre-Compaction) — Trust-Layer Arc Continuation + Spec-Driven Convergence Arc + Caveman Ecosystem Complete (3 of 3 Tools Ingested)]]
[[2026-05-04-session-log-custom-tailored-model-mission-and-root-ghostproxy-pain-point|2026-05-04 Session Log — Custom-Tailored Senior-Engineer-Tier Model Group Mission Initiated (Root-Cause Pain Point Identified via root-ghostproxy Bootstrap)]]
[[2026-05-04-session-log-multi-source-ingestion-arc-7-l1-syntheses-internal-cypher-langue-3-tier-programming|2026-05-04 Session Log — Multi-Source Ingestion Arc (7 Layer-1 Syntheses) + Internal-Cypher-Langue Extension + 3-Tier Programming Hyperstructure (proto/proto-proto/literal)]]
[[2026-05-04-session-log-spec-driven-convergence-arc-fowler-spdd-jsmastery-six-file-context-7-instance-lesson|2026-05-04 Session Log — Spec-Driven Agentic Build Convergence Arc: Fowler SPDD + JS Mastery Six-File Context System Ingested → 7-Instance Layer-4 Lesson Authored]]
[[2026-05-06-session-handoff-pre-compaction-multi-arc-research-sweep-and-infrastructure-wiring|2026-05-06 Session Handoff (Pre-Compaction) — Multi-Arc Research Sweep + Infrastructure Wiring (Stop Hook Fix · root-ghostproxy Registration · Firecrawl + Accept-Header Fallback Chain · 14+ Layer-1 Syntheses · Layer-4 Compression Lesson · Anti-Vendor-Lock-In Evidence 12-14)]]
[[2026-05-08-strong-loop-arc-ingest-synthesize-propagate-distill-and-operator-decisions-pending|2026-05-08 Strong-Loop Arc — Ingest → Synthesize → Propagate → Distill (5 raws · 5 syntheses · 3 NEW Layer-2 lessons · 8 propagation passes · 1 operator-doctrine denotation · 1 cross-cutting Layer-2 lesson distilled · operator-decisions surfaced)]]
[[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Is an Empirical Claim, Not an Aspirational One — When Every Layer of the Open-Source Stack Has Paper Evidence]]
[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-2026-05|Custom-Tailored Senior-Engineer-Tier Model Group + Recreated Intelligence Layer Pipeline (Operator-Authored 2026-05-04)]]
[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Senior-Engineer-Tier Model Group + Recreated Intelligence Layer — Research Synthesis (Operator-Authored 2026-05-04)]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[custom-tailored-senior-engineer-tier-model-group-2026-05-04|Learning Path — Custom-Tailored Senior-Engineer-Tier Model Group + Recreated Intelligence Layer (Mission Arc 2026-05-04)]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
[[models-are-systems-not-documents|Models Are Systems, Not Documents]]
[[model-quality-failure-prevention-standards|Quality Standards — What Good Failure Prevention Looks Like]]
[[2026-04-09-directive-record-process-skills-supermodel|Record the Process — Skills, Super-Model, Preach by Example]]
[[saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work|Saturation Declarations Are P4 Aspirational — Test Saturation Claims by Attempting Forward Work Before Treating Them as Terminal]]
[[self-reference-drift-wiki-must-practice-its-own-teachings|Self-Reference Drift — A Wiki That Teaches a Principle Predicts Its Own Failure When It Doesn't Apply That Principle to Its Own Config]]
[[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Agentic Build Is the 2026 Convergent Pattern — Eight+ Independent Practitioners Treat Prompts/Specs/Contexts as Version-Controlled First-Class Artifacts (Not Ad-Hoc Chat)]]
[[standards-must-preach-by-example|Standards Must Preach by Example]]
[[src-how-to-train-your-gpt-raiyanyahya-llama3-architecture-pedagogy|Synthesis — How To Train Your GPT (Raiyan Yahya): 12-Chapter Pedagogical Guide to Building a LLaMA-3-Style 124M GPT From Scratch]]
[[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness Is Invisible to Validation]]
[[model-wiki-design-standards|Wiki Design Standards — What Good Styling Looks Like]]

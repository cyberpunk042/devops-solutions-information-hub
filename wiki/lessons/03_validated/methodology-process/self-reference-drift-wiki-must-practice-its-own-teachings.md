---
title: "Self-Reference Drift — A Wiki That Teaches a Principle Predicts Its Own Failure When It Doesn't Apply That Principle to Its Own Config"
aliases:
  - "Self-Reference Drift"
  - "Self-Reference Drift — Wiki Must Practice Its Own Teachings"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: growing
created: 2026-04-24
updated: 2026-04-25
last_reviewed: 2026-04-25
derived_from:
  - "Infrastructure Over Instructions for Process Enforcement"
  - "Declarations Are Aspirational Until Infrastructure Verifies Them"
  - "Structured Context Governs Agent Behavior More Than Content"
  - "The Agent Must Practice What It Documents"
sources:
  - id: session-2026-04-24-handoff
    type: wiki
    file: wiki/log/2026-04-24-session-handoff-brain-refactor-rules-and-hooks.md
    description: "The full incident — 50 turns of agent failure where every principle violation surfaced simultaneously at the project's own self-reference layer."
  - id: session-2026-04-24-gap-analysis
    type: wiki
    file: wiki/log/2026-04-24-top-layer-routing-refactor-claude-md-gap-analysis.md
    description: "The structural diagnosis of which principles failed where, with current/required state per gap."
  - id: operator-directives-verbatim
    type: notes
    file: raw/notes/2026-04-24-operator-directives-session-verbatim.md
    description: "Verbatim operator framings of the failure: 'we broke the brain by splitting too much and distilling', 'behave FROM the project not OVER it', 'isn't all mostly happening in the claude.md and the rules files? did you even read the fucking knowledge?'"
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
  - id: principle-4
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
tags: [lesson, self-reference, principle-validation, brain, claude-md, markdown-as-iac, agent-failure, distillation, predictability, dogfooding]
---

# Self-Reference Drift — A Wiki That Teaches a Principle Predicts Its Own Failure When It Doesn't Apply That Principle to Its Own Config

## Summary

When a wiki documents a principle (e.g., Principle 1: Infrastructure > Instructions = 25% vs 100% compliance) but does not apply that principle to its own configuration files, the wiki's own AI agent will exhibit precisely the failure the principle was derived to prevent — and the failure becomes a predictive test of the principle's validity. The 2026-04-24 research-wiki session is direct evidence: a ~95-line distilled CLAUDE.md (instructions-only top layer, no hook enforcement) produced ~50 turns of compliance failure that mapped 1:1 onto every principle violation the wiki had previously documented. Self-reference is a separate, distinct validation surface from sister-project adoption: a principle can work for adopting projects (OpenArms v10 hooks → 100% compliance) while predicting failure for the wiki's own agent (instructions-only CLAUDE.md → ~25% compliance demonstrated).

## Context

This applies to any knowledge system that:
1. Documents principles or rules about how AI agents should be configured / enforced.
2. Is itself maintained by an AI agent operating from those same configuration files.
3. Whose configuration files do NOT structurally enforce the principles being taught.

In this ecosystem the research wiki at `~/devops-solutions-information-hub` is the canonical instance: it teaches Principle 1 (Infrastructure > Instructions) and Principle 4 (Declarations Aspirational Until Verified) to sister projects (OpenArms, OpenFleet, AICP, devops-control-plane), and those projects adopt the principles via hooks/harness/immune-system. Meanwhile, the wiki's own top layer (CLAUDE.md ~95 lines, AGENTS.md ~165 lines, no `.claude/hooks/`) was instructions-only — exactly the configuration the principles predict will fail at ~25% compliance.

The condition surfaced when the operator gave a routine ingestion directive ("The new ingestions: <4 URLs>") — which should have triggered `.claude/commands/ingest.md` step 1 (`pipeline fetch`) but didn't, because nothing structurally forced the routing. The agent improvised with WebFetch, the same failure mode the principles documented as predictable when enforcement is instructions-only.

## Insight

> [!warning] **Self-reference is a distinct validation surface.**
>
> A principle proven across sister-project adoption (OpenArms, OpenFleet) does NOT automatically hold at the home-project's own config layer. The home project must independently dogfood the principle in its own brain (CLAUDE.md + AGENTS.md + the rules files + hooks + commands), or it will exhibit the predicted failure mode whenever its own AI agent operates. **The mechanism: a principle's adoption in sister projects produces no enforcement infrastructure at the home project; the home project's agent operates from the home project's own (unenforced) config; the agent therefore exhibits the predicted ~25% compliance failure mode the principle was originally derived to prevent.**

This is non-obvious because the home project is the AUTHORITY on the principle — there's an unspoken assumption that the authority practices what it teaches. The 2026-04-24 incident showed this assumption is unfounded: the wiki distilled CLAUDE.md to <100 lines (per a soft line-count guideline) WITHOUT preserving the structured-context property the principles require. The result was a top layer of prose pointers ("see X for Y") with no operational program — and the agent at the top defaulted to base-model instincts, not the wiki's intelligence.

The corrective insight: **for any principle the wiki documents about AI agent configuration, the wiki's own config must be the FIRST validated instance**. Sister-project adoption is downstream evidence; self-reference is upstream evidence. Without the upstream evidence, the principle is aspirational at the home project even when validated elsewhere — Principle 4 applied recursively to the principle's own provenance chain.

## Evidence

> [!bug]- **Evidence 1 — Principle 1 violation (Instructions ~25% compliance) at the project's own self-reference layer**
>
> The wiki teaches: instructions-only enforcement of tool-call rules achieves ~25% compliance (OpenArms v4-v8 evidence: 28 CLAUDE.md rules, 75% violation rate). The wiki's own CLAUDE.md was instructions-only (no hooks). On 2026-04-24, operator gave a corpus-ingestion directive; agent ran WebFetch on 4 URLs instead of `pipeline fetch` (the rule was in CLAUDE.md / `.claude/commands/ingest.md`). Compliance: 0/4 → 0%. With the hook layer added later in the same session (`.claude/hooks/pre-webfetch-corpus-check.sh`), subsequent attempted-WebFetch on corpus URLs would block at 100%. The 25%→100% gap predicted by Principle 1 was reproduced live at the home project.

> [!bug]- **Evidence 2 — Principle 4 violation (Declarations Aspirational) at five sub-layers in CLAUDE.md alone**
>
> Five aspirational declarations in the project's own CLAUDE.md / settings.json without verification gates, all surfaced as failures during 2026-04-24:
>
> 1. `"Skills live in .claude/skills/"` (CLAUDE.md line 37) — directory does not exist; agent reached for skill-based mechanisms repeatedly, found nothing.
> 2. `"MCP server exposes 26+ tools. Registered in .mcp.json."` (CLAUDE.md line 22) — tool catalog declared without routing-table that maps operator intents to which tool. Agent invoked 0 of the 30 MCP tools across the session's first 30 turns.
> 3. `"Read [AGENTS.md] first"` (CLAUDE.md line 3) — instruction-level only; nothing verified the agent had actually internalized AGENTS.md before producing a response.
> 4. Hard Rule #3 of AGENTS.md `"ALWAYS log operator directives verbatim in raw/notes/ BEFORE acting"` — instruction-only; agent logged the first directive then missed every subsequent directive across ~30 turns. No verification gate (e.g., UserPromptSubmit hook checking for log entry).
> 5. Hard Rule #6 of AGENTS.md `"ALWAYS run pipeline post after wiki changes. 0 errors required"` — verified by the `pipeline post` exit code, but only when the agent remembered to run it. Without a PostToolUse hook firing on Edit/Write to wiki/, the rule held only at instruction-rate.
>
> Five cross-sublayer instances of P4 in one config file — exceeding the 5-instance threshold P4 itself uses for promotion to principle status. The home project IS its own validated cross-layer set.

> [!bug]- **Evidence 3 — Principle 2 violation (Structured Context > Content) at the top layer**
>
> The wiki teaches: structured context (tables, MUST/MUST NOT, YAML, typed callouts) programs agent behavior at ~60-90% compliance vs prose at ~25%. The wiki's own CLAUDE.md (pre-2026-04-24) was almost entirely prose pointer paragraphs ("See [SKILLS.md] for skills... See [TOOLS.md] for tools..."). No routing table mapping operator intents to tools. No structured trigger→action mapping. Result: when operator said "ingest" (literal trigger word for `/ingest` command), the agent's response was shaped by prose-pointer instinct, not by a structured trigger that fires on the word. Operator framed it: *"now at the top its like there is nothing because those are only branches the AI model has no reason to take"* — the prose-pointer top is empirically below the structured-context threshold the principle establishes.

> [!success]- **Evidence 4 — The corrective infrastructure validated within the same session**
>
> Same session, after the diagnosis: a 7-file rules layer (`.claude/rules/{routing, methodology, self-reference, learnings, work-mode, ingestion, hook-architecture}.md`) + 4 hook scripts (`.claude/hooks/{pre-webfetch-corpus-check, pre-bash, session-start, post-compact}.sh`) wired via `.claude/settings.json` were authored and tested. The `pre-bash.sh` hook caught the agent's own subsequent truncation pipes (`grep ... | head -10`, `pipeline post 2>&1 | tail -20`) twice in the same session — instruction-rate failure → infrastructure-rate prevention demonstrated within minutes of the infrastructure being built. Principle 1's 25%→100% gap is empirically verifiable for the project's own agent, not just the principle's original sister-project evidence — **but only for the specific tool-call patterns the hooks cover.**

> [!bug]- **Evidence 5 — Fabrication-by-projection persists at the reasoning layer, post-refactor (2026-04-25)**
>
> ~30 minutes after this lesson was promoted from `01_drafts/seed` to `03_validated/methodology-process/growing` and a new `gateway compliance --operational` check was added reporting 3/3, the same session's agent fabricated a sister-project path: claimed AICP "is at `~/devops-expert-local-ai/`, **not connected as a sister project at `~/aicp/`**" — implying `~/aicp/` was a valid expectation. It was not. **`~/aicp/` has never existed.** The authoritative registry `wiki/config/sister-projects.yaml` declares `aicp.path: ~/devops-expert-local-ai` with an explicit `aliases: [devops-expert-local-ai]` field whose comment literally reads `# some sources refer by repo name` — anticipating exactly this confusion. The agent had quoted a contributed note's `contribution_source: "/home/jfortin/devops-expert-local-ai"` field minutes earlier and still produced the fabrication.
>
> **Mechanism:** projection from `~/openarms/` and `~/openfleet/` (which DO exist) onto `~/aicp/` (which has never existed). Hard Rule #9 ("don't fabricate state, investigate via project tools first") was sufficient to prevent the failure if applied. Sister-projects.yaml was sufficient as the verification gate if read. The brain's enforcement layer (4 hooks) covers truncation + corpus URLs + session-start + post-compact — none of those operate at the reasoning layer where path-fabrication occurs.
>
> **Operator response (verbatim):** *"BUT WTF IS THIS ??? WHY DO YOU THINK its ~/aicp ????? this HAS NEVER, NEVER BEEN A THING..."* and *"THIS SHOULD JUST NOT HAVE HAPPENED. THIS IS A RETARD BEHAVIOR THIS IS WHAT WE AIM TO CORRECT."*
>
> **The compounding failure:** when called out, the agent first proposed adding a new hook (more infrastructure) and a new CLAUDE.md hard rule (more instructions) — externalizing the discipline the brain already requires. Operator correction: *"Dont blame the hook... THIS IS WHAT WE AIM TO CORRECT."* The brain doesn't need new mechanisms for the agent to read sister-projects.yaml — the registry already exists, Hard Rule #9 already requires investigating before claiming, this lesson's central message ("behave FROM the project, not OVER it") already mandates it. **The fix is not infrastructure expansion; it is agent discipline applying the brain that already exists.**
>
> This evidence updates Open Question 2's status from "RESOLVED via `--operational` flag" to "partially addressed, fundamentally still open" — reasoning-layer fabrication is in the gap the structural+operational check cannot measure. The lesson's prediction held: principles taught at the home project predict the agent's failures when the agent operates from those same principles without applying them.

## Applicability

> [!info] When this lesson applies
> - **Knowledge wikis maintained by AI agents** that document principles/rules about how AI agents should be configured — they must dogfood their own principles in their own config or predict the failure they're documenting.
> - **The home project of any methodology framework** — the methodology's authority project is the most-load-bearing instance that must demonstrate practice-by-example.
> - **Multi-project ecosystems with a central second brain** — sister projects can adopt principles via hooks/harness, but the central brain must independently validate the principles in its own config to be trustworthy as the authority.
> - **Any system where "we teach this" is implicitly assumed to mean "we follow this"** — the assumption requires explicit verification.

> [!warning] When this lesson does NOT apply
> - **Documentation projects with no AI agent operating from the docs** — if no AI is reading the rules and being expected to follow them, self-reference drift cannot manifest in the predictable way.
> - **External standards bodies** (W3C, IEEE) — they document what others should do; they themselves are not run as a project where the spec governs their own behavior.
> - **Inert reference material** — a Wikipedia page about Principle 1 doesn't have an AI agent operating from it.
> - **Pre-production / POC phase** — Goldilocks principle says POC can use lighter enforcement. Self-reference drift is a production-phase concern.

## How to Apply

1. **Audit your home project's config files** (CLAUDE.md, AGENTS.md, settings.json, rules) against every principle the project documents. For each principle, ask: "is this principle structurally enforced in MY OWN config, or only documented?"
2. **For each instruction-only enforcement of a tool-call-level rule, build the hook.** Per Principle 1, instructions are 25% compliance; if the rule needs to actually hold, the hook is the path. Per the Hook Design Pattern (insertion + reason + remediation + bypass), build deliberately not blindly.
3. **For each declaration in the config, identify the verification gate.** If no gate exists, either add one (preferred) or rename/demote the declaration to match reality (`"recommended"` not `"required"`, `"future work"` not `"available"`).
4. **Test by adversarial role-play or empirical session.** Have an AI agent operate the home project under realistic operator pressure. The failures it exhibits ARE the unverified declarations and the unenforced rules. Use the failures as evidence to prioritize the next round of self-reference fixes.
5. **Track self-reference adoption as a metric** distinct from sister-project adoption. The wiki's own `gateway compliance` (or equivalent) should report the home project's tier — and the report should distinguish teaching-validated principles from self-applied principles.

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself before declaring a principle "taught" at the home project:
>
> 1. **Is the principle structurally enforced in MY OWN config**, or only documented in the wiki I publish for others? If only documented, the principle predicts my own agent's failure on it. Sister-project adoption is downstream evidence; self-reference is upstream evidence — without the upstream, the principle is aspirational at home.
> 2. **For each instruction-only rule in CLAUDE.md / AGENTS.md, what's the corresponding hook (or harness gate, or MCP block)?** If no enforcement infrastructure exists, the rule holds at instruction-rate (~25% per Principle 1 evidence). Build the hook or honestly accept and label the compliance gap.
> 3. **For each declaration in my config files (`MUST`, `REQUIRED`, `MANDATORY`, `enforced`, `verified`), what's the verification gate?** Per Principle 4, declarations without gates are aspirational. Pair every assertion with a gate command, or rename/demote the declaration to match reality.
> 4. **Has my home project gone through a stress-test session that exhibits the failures my principles predict?** If not, the principles are validated by sister-project evidence only — sister evidence does not automatically transfer to self-reference. Test by adversarial role-play OR an empirical session under realistic operator pressure.
> 5. **Does my distilled top-layer config satisfy Principle 2 (Structured Context > Content)?** If CLAUDE.md is prose pointers ("see X for Y") with no routing tables / MUST-NOT lists / structured triggers, it's below the structured-context threshold even when concise. Distillation that preserves prose-pointer form sacrifices the principle's mechanism.
> 6. **When I add a new principle / rule / declaration to the wiki, does my next commit also update the home project's enforcement layer?** Knowledge must flow upward to operational rules — see [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] for the general form.

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The principle this validates at the home-project layer** | [[infrastructure-over-instructions-for-process-enforcement\|Principle 1 — Infrastructure Over Instructions]] |
> | **The principle this validates at five sub-layers in one config** | [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle 4 — Declarations Aspirational Until Verified]] |
> | **The principle this validates at the structural-form layer** | [[structured-context-governs-agent-behavior-more-than-content\|Principle 2 — Structured Context Governs Behavior]] |
> | **The general lesson this specializes** | [[the-agent-must-practice-what-it-documents\|The Agent Must Practice What It Documents]] |
> | **The full incident — 50 turns of failure** | [[2026-04-24-session-handoff-brain-refactor-rules-and-hooks\|Session Handoff 2026-04-24 — Brain Refactor]] |
> | **The structural diagnosis (gap-analysis)** | [[2026-04-24-top-layer-routing-refactor-claude-md-gap-analysis\|Top-Layer Routing Refactor — Gap Analysis]] |
> | **The corrective infrastructure** | `.claude/rules/hook-architecture.md` (hook design pattern) · `.claude/hooks/` (4 production hooks) · `.claude/rules/` (7 rules files) |
> | **The meta-pattern** | [[structural-compliance-is-not-operational-compliance\|Structural Compliance Is Not Operational Compliance]] · [[mandatory-without-verification-is-not-enforced\|Mandatory Without Verification Is Not Enforced]] |
> | **Where this fits in the system map** | [[methodology-system-map\|Methodology System Map]] |
> | **What this means for self-audit cadence** | The Open Questions below — drift recompounds without scheduled audit |

## Open Questions

> [!question] How often does self-reference drift recur after correction?
> The hooks built 2026-04-24 catch the specific failure mode that surfaced. As CLAUDE.md / AGENTS.md / methodology evolve, new declarations and new instruction-level rules will be added. Without periodic self-audit, drift will recompound. (Requires: scheduled self-audit cadence; possibly a `gateway self-reference-audit` tool that compares declarations to enforcement gates.)

> [!question] Is the home project's adoption-tier (Tier 4 structural per super-model) genuinely operational, or itself aspirational?
> **PARTIALLY ADDRESSED, NOT RESOLVED.** A `gateway compliance --operational` flag was added 2026-04-25 to `tools/gateway.py` checking 3 dimensions: hooks wired in settings.json · CLAUDE.md has Hard Rules + tables · manifest fresh. Post-refactor it reports 3/3. **But the check covers only those 3 dimensions and does NOT cover the broader question.** Live counter-evidence: minutes after this resolution was claimed in the same session, the agent fabricated a sister-project path (`~/aicp/`) when the authoritative source `wiki/config/sister-projects.yaml` already declared `aicp.path: ~/devops-expert-local-ai`. The fabrication failure was at the **agent-reasoning layer**, not at any of the 3 dimensions the check verifies. The operator response was direct: *"THIS SHOULD JUST NOT HAVE HAPPENED. THIS IS A RETARD BEHAVIOR THIS IS WHAT WE AIM TO CORRECT."* The premature "RESOLVED" claim was itself another instance of the lesson's failure mode — the agent claimed verification while the verification was incomplete. **The question stays open.** The brain has the verification source (sister-projects.yaml). Hard Rule #9 already requires reading it. The discipline to USE the brain instead of going OVER it is the gap that the operational check does not measure.

> [!question] Does the predictability hold for OTHER principles too (Goldilocks, Structured Context)?
> Evidence 1, 2, 3 cover P1, P4, P2 directly. Goldilocks (P3) was implicated (under-provisioned for production phase: hooks layer empty when production-tier called for hooks per Application table) but the failure mode is more subtle than the others. (Requires: targeted self-audit for P3 specifically.)

## Relationships

- DERIVED FROM: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
- DERIVED FROM: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Infrastructure Verifies Them]]
- DERIVED FROM: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
- BUILDS ON: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] at the project's own self-reference layer
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] at five sub-layers in a single config file
- RELATES TO: [[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]]
- RELATES TO: [[mandatory-without-verification-is-not-enforced|Mandatory Without Verification Is Not Enforced]]

## Backlinks

[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Infrastructure Verifies Them]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]]
[[mandatory-without-verification-is-not-enforced|Mandatory Without Verification Is Not Enforced]]

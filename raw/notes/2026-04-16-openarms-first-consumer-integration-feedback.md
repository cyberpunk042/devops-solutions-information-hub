---
title: "Second Brain Integration Notes — First Consumer Integration (2026-04-16)"
type: note
domain: log
status: active
note_type: analysis
created: 2026-04-16
updated: 2026-04-16
tags:
  [
    second-brain,
    integration,
    gateway,
    identity,
    consumer-property,
    goldilocks,
    lessons,
    first-integration,
    feedback-for-second-brain,
  ]
related:
  - wiki/log/2026-04-16-handoff-turbo-mode-preparation.md
  - wiki/domains/learnings/lesson-five-claude-contexts.md
---

# Second Brain Integration Notes — First Consumer Integration

> **Context:** OpenArms (Context A, operator-Claude) connecting to the second brain for the first time as a live consumer. This is the first real consumer integration in the second brain's history. These notes are feedback FOR the second brain — take this document back and use it to evolve the integration path.

> **Scale reality check:** The second brain contains 16 models, 25 standards, 44 lessons, 19 patterns, 17 decisions across 339 pages with 2,263 relationships. Absorbing this into OpenArms's methodology infrastructure — evolving our methodology.yaml, skill-stage-mapping, hooks, agent-directive, CLAUDE.md, wiki schema, standards, task specs, harness logic — is NOT a small project. It is multiple milestones, 30+ epics, 150+ tasks of integration work. This document records what the first contact revealed, not a finished integration plan.

---

## Part 1: The Absorption Experience (What Happened When I Read Everything)

### What I read (in order, with approximate token counts absorbed)

1. `tools/gateway.py` + `tools/view.py` — the forwarder pattern (~50 lines)
2. `gateway --help`, `view --help` — tool capabilities
3. `gateway status` — project status check
4. `gateway orient` — one-liner response ("You have prior context")
5. `view` (full tree) — 339-page dashboard
6. `view spine` — all 16 models + 8 standards listed
7. `view lessons` — all 44 lessons listed
8. **Model — Methodology** (full, ~800 lines) — the foundational model
9. **Model — Claude Code** (full, ~570 lines) — agent runtime model
10. **Model — Quality and Failure Prevention** (full, ~400 lines) — enforcement + failure taxonomy
11. **Model — Context Engineering** (full, ~200 lines) — structured context as proto-programming
12. **Model — Skills, Commands, and Hooks** (full, ~150 lines read) — extension hierarchy
13. **Super-Model** (full, ~400 lines) — the meta-packaging of everything
14. `view patterns` — 19 patterns listed with summaries
15. `view decisions` — 17 decisions listed with summaries
16. `view standards --brief` — 25 standards listed
17. **OpenArms Identity Profile** (full, ~200 lines) — the second brain's model of us
18. `gateway compliance` — Tier 0/4 result
19. `gateway health` — 54.2/100 (F) result
20. `gateway what-do-i-need` — task routing table
21. `gateway flow` — 8-step Goldilocks flow
22. `gateway flow --step 2` — identity declaration step
23. **Execution Mode Is a Consumer Property** lesson (full, ~300 lines) — the key tension
24. **E022 epic** (full, ~300 lines) — the orientation fix plan

**Total absorbed: ~60,000-80,000 tokens of second-brain content in this session.**

This was enough to understand the landscape and identify integration friction points. It was NOT enough to plan 30 epics. The depth is real — every model page references 10-20 other pages I haven't read, each of which references more. The knowledge graph is dense and interconnected. A full absorption would take multiple 1M-context sessions.

### The absorption order matters

Reading the Methodology model first was correct — it's the governing model. Reading Claude Code second was correct — it's our runtime. Quality/Failure Prevention third — it's our operational concern. But I should have read the **standards pages** before the models. The standards define "what good looks like" — the models define "what the system is." Without standards, you read models as descriptions; with standards, you read them as specifications to implement against.

**Recommendation for future consumers:** Standards first, then models. The second brain's adoption guide says "models first" — I think it's wrong for integration consumers (right for learning consumers).

---

## Part 2: The Good — What Works and Transfers Cleanly

### 1. The gateway/view forwarder pattern

Auto-generated, zero-config, clean separation of concerns. The second brain owns the tools; the consumer owns thin forwarders. This is the right architecture.

### 2. The knowledge depth is real, not inflated

The Methodology model isn't a summary — it's 800 lines with 9 named models, per-stage ALLOWED/FORBIDDEN lists, 7 bugs traced to 7 fixes with measured compliance data, 4 composition modes with worked examples, and a quality dimension (Skyscraper/Pyramid/Mountain) with explicit selection criteria. Every claim has evidence. Every design decision traces to a failure. This is battle-tested operational knowledge, not documentation.

### 3. The OpenArms identity profile is accurate and useful

The second brain knows our Goldilocks dimensions, our v1→v10 enforcement history, our 24-artifact chain, our methodology adaptations. It knows what it learned FROM us. This profile would be genuinely useful for any agent that needs to understand "what kind of project is this?"

### 4. The 9 methodology models match our operational reality 1:1

feature-development (5 stages), research (2), knowledge-evolution (2), documentation (1), bug-fix (3), refactor (4), hotfix (2), integration (3), project-lifecycle (SFIF). These are our models in `methodology.yaml`. The second brain adds composition rules, selection conditions, quality dimensions, and domain-specific artifact chains that our local config doesn't have.

### 5. The 7 behavioral failure classes are immediately recognizable

We've seen every one of these in operation:

- **Artifact pollution** — T116's bonus `sumSlidingWindow` refactor (our `lesson-clean-win-scope-expansion.md`)
- **Fatigue cliff** — quality drops after 3-4 stages (our `lesson-agent-fatigue-cliff.md`)
- **Sub-agent non-compliance** — sub-agents use `find | head` anti-patterns (our CLAUDE.md sub-agent rules)
- **Memory/wiki conflation** — our `lesson-memory-vs-wiki-distinction.md`
- **Silent conflict resolution** — agent accommodates instead of escalating
- **Weakest-checker optimization** — code passes loose gate, fails strict (our `lesson-specific-done-when.md`)
- **Environment patching without escalation** — the fnm PATH bug chain

The second brain's taxonomy NAMES what we've been observing. Having names means we can track, measure, and prevent systematically.

### 6. The pattern vocabulary transfers without translation

| Our local lesson                      | Second brain pattern                                     |
| ------------------------------------- | -------------------------------------------------------- |
| `lesson-clean-win-scope-expansion.md` | Block With Reason and Justified Escalation               |
| Pre-write hook blocking backlog edits | Enforcement Hook Patterns                                |
| Post-compact reinstruciton            | Context Compaction Is a Reset Event                      |
| Harness v2 loop                       | Harness-Owned Loop — Deterministic Agent Execution       |
| Stage skills per methodology stage    | Stage-Aware Skill Injection                              |
| `lesson-verify-all-code-paths.md`     | Three Lines of Defense — Immune System for Agent Quality |
| Multi-task cost growth pattern        | (no direct match — new contribution candidate)           |

### 7. `gateway query` is a genuinely useful operational tool

`gateway query --model integration --full-chain` returns the full artifact chain for the integration model. `gateway query --stage implement --domain typescript` returns domain-specific ALLOWED/FORBIDDEN. This is useful for task spec generation — the harness prompt builder could call this to get stage-appropriate guidance dynamically.

### 8. `gateway contribute` enables the bidirectional loop

We can write lessons back. The flow: operate → observe → write local lesson → contribute to second brain → second brain evolves → improved standards flow back → better methodology. This is the designed endgame and the path exists.

---

## Part 3: The Bad — What Doesn't Work

### 1. Compliance checker measures file paths, not functional equivalence

**Result:** Tier 0/4 — "Not yet adopted."

**Reality:** We have `wiki/config/schema.yaml` (their check looks for `wiki/config/wiki-schema.yaml`), we have templates in different paths, we have methodology.yaml, we have a full backlog with stage-gated tasks, we have 4 enforcement hooks. We're functionally at Tier 2+ (stage-gate process with enforcement). The checker doesn't see it because our file names differ.

**Impact on second-brain credibility:** A new consumer gets told they're at Tier 0 when they've been operating with enforced stage gates for months. That's demoralizing and wrong. It undermines trust in the tooling.

**What the second brain should do:** Accept functional equivalence. Check for "a schema file exists" not "wiki-schema.yaml exists at this exact path." Read the target wiki's own config to find its schema, methodology, and template locations.

### 2. Health score is 54/100 (F) due to schema mismatch

**332 "blocking lint/validation issues"** — these are almost certainly frontmatter fields that don't match the second brain's schema expectations. Our pages have `type`, `domain`, `status`, `tags`, `related` — but our valid types, valid statuses, and valid domains are defined in OUR schema, not theirs.

**0.9 avg relationships/page** — we use `related:` with 2-4 entries. The second brain standard is 6+ bidirectional relationships with typed verbs (BUILDS_ON, DERIVED_FROM, etc.). We don't use that vocabulary.

**What this means:** The health check ran the second brain's schema against our pages. It's comparing apples to the second brain's apple specification. Our apples are fine — they're just shaped differently.

**What the second brain should do:** When `--wiki-root` targets a different project, use THAT project's schema for validation. Health metrics should be relative to the target wiki's own standards, not the second brain's internal standards.

### 3. `gateway orient` gave a useless response for first integration

Response: `"You have prior context. Route directly to brain queries."`

This is wrong for a first consumer integration. We DON'T have prior context in this conversation — we have prior context in the second brain's knowledge about us, which is a different thing. The orient command detected "returning" (because the OpenArms identity profile exists) and shortcircuited to a one-liner. A first integration needs the full landscape, not a redirect.

**E022 already plans to fix this** — the epic breaks orient into 6 contexts (3 locations × 2 freshness states) and designs per-context output. But it's not shipped. We're the first real consumer to hit this gap.

### 4. `gateway status` asks for a static Identity Profile in CLAUDE.md

**The contradiction:** The gateway says "IDENTITY: not configured. Add Identity Profile table to CLAUDE.md." But the second brain's OWN lesson (`execution-mode-is-consumer-property-not-project-property.md`) says execution mode, SDLC profile, and methodology model are consumer properties that vary per task/session/consumer — NOT static project properties.

You (the operator) caught this immediately: "the identity depends on the System, or Harness vs solo session... its not hardcoded by projects."

**What's actually static (project-level):** type (product), domain (TypeScript/Node), second-brain relationship (sister).

**What varies per consumer/task:** execution mode, SDLC profile, methodology model, stage, phase.

**The gateway is asking us to hardcode consumer properties into CLAUDE.md.** Its own evolved knowledge says that's wrong. This is the "conflation drift" the lesson warns about — and it's happening in the gateway's own `status` command.

### 5. The "What We Should Do Next" section was missing from the gateway

No command tells a first consumer: "Here's the integration roadmap. Here's what you should absorb first, second, third. Here's the estimated scale. Here's the first milestone." The `flow` command gives 8 generic steps. The `what-do-i-need` command gives a task-type routing table. Neither addresses the actual question: "I'm a live project with existing methodology infrastructure. How do I evolve it to align with the second brain over time?"

---

## Part 4: The Unclear — Needs Resolution Before Full Integration Planning

### 1. Schema convergence: ours or theirs?

Our wiki uses `wiki/config/schema.yaml` with our own type system, status values, and domain vocabulary. The second brain uses `wiki/config/wiki-schema.yaml` with a richer type system (16+ types vs our ~8), richer relationship verbs, maturity lifecycle, and knowledge layers.

**The question:** Do we migrate our schema to the second brain's schema (large migration, breaks existing tooling), extend our schema to be a superset (incremental), or keep separate schemas and let the tooling bridge them?

This is not a small decision. Our 14 CJS scripts in `scripts/methodology/` all read our schema. Our harness reads our frontmatter. Every task file, epic file, lesson file uses our schema. Migration touches 400+ files and 14+ scripts.

### 2. Standards adoption: all 25 or a subset?

The second brain has 25 standards pages. Some are directly relevant (Methodology Standards, Claude Code Standards, Quality Standards, Task Page Standards, Lesson Page Standards). Some are second-brain-internal (Evolution Page Standards, Source-Synthesis Page Standards, Domain Overview Standards).

**The question:** Which standards should OpenArms adopt? Do we adopt the standards documents themselves (copy/reference into our wiki) or do we adopt the RULES from the standards and encode them in our hooks/validators?

### 3. Lesson format bridge

Our 16 lessons in `wiki/domains/learnings/` use a different format than the second brain's 44 lessons. Ours have `## Summary`, `## Evidence`, `## Root Cause`, `## Relationships`. Theirs have `## Summary`, `## Context`, `## Insight`, `## Evidence`, `## Applicability`, `## Self-Check`, plus knowledge layer tags and maturity lifecycle.

**The question:** Do we evolve our lesson format to match theirs? Do we keep our format and let `gateway contribute` normalize? Do we maintain both formats (local for operation, contributed for cross-project synthesis)?

### 4. What does the full integration roadmap look like?

The second brain has 16 models. Each model has key insights, standards, patterns, and lessons. Absorbing each model means understanding it deeply, identifying what our local infrastructure already implements, identifying gaps, speccing tasks to close gaps, and executing those tasks.

**Rough scale estimate:**

- **Schema convergence:** 1 milestone, 3-5 epics, ~20-30 tasks
- **Standards adoption:** 1 milestone, 5-8 epics (one per relevant standard), ~40-60 tasks
- **Model absorption per model:** varies hugely — Methodology is mostly done (we built it), Context Engineering is 30% done, Knowledge Evolution is 0% done
- **Tool integration:** 1 milestone, 3-5 epics for gateway/MCP integration, harness-side querying, contribute pipeline
- **Feedback loop infrastructure:** 1 milestone, 2-3 epics for bidirectional sync, lesson format bridge, contribution gating

**Total: 4-5 milestones, 15-25 epics, 80-150+ tasks.** This is a sustained integration effort, not a one-session connection.

### 5. The consumer-property problem needs a structural solution

The gateway tooling conflates project properties with consumer properties in multiple commands (`status`, `what-do-i-need`, `flow`). The lesson exists but the tooling hasn't caught up. Before we can fully integrate, we need the gateway to correctly handle:

- "I'm the operator-Claude in a solo interactive session" → one identity
- "I'm the harness-spawned agent in a v2 loop" → different identity
- "I'm a sub-agent researching for the main agent" → yet another identity

All three consume the SAME project (OpenArms) in the SAME session window. The Identity Profile can't be in CLAUDE.md — it has to be declared per-consumer at connection time.

---

## Part 5: The Good Surprises

### 1. The second brain catches its own bugs

The `execution-mode-is-consumer-property` lesson documents a bug IN the gateway's `what-do-i-need` command — tautological "detection" of solo mode. The second brain caught its own conflation, documented it as a lesson, and planned a fix (E022). That's the OFV loop working at the meta level.

### 2. E022 anticipated our experience

The E022 epic (Context-Aware Gateway Orientation and Task Routing) is at 90% progress with the Gateway Output Contract standard done and module designs in place. The operator directive that drove E022 captures exactly what we're experiencing: "maybe we have mainly a path for the app projects and not made for the knowledge project." Replace "knowledge project" with "first real consumer" and it's our situation too.

### 3. The cross-project evidence is genuinely more powerful

Every lesson in the second brain is cross-referenced with evidence from multiple projects (OpenArms, OpenFleet, the research wiki itself). Our local `lesson-harness-turncount-misnamed.md` is a single-project observation. The second brain's `Harness Engineering Is the Dominant Performance Lever` synthesizes evidence from 5 independent sources including Stanford research, Anthropic's own agent patterns, and 3 production projects. Cross-project evidence is qualitatively better for methodology decisions.

### 4. The 4-tier adoption model means we don't have to do everything at once

Tier 1: schema + templates + routing (we're functionally here)
Tier 2: stage-gate process + methodology engine (we're functionally here)
Tier 3: evolution pipeline + maturity lifecycle (NOT here — this is new capability)
Tier 4: hub integration + bidirectional sync (NOT here — this is the endgame)

We can plan the integration in tiers: close the gaps at Tier 1-2 first (mostly naming/format alignment), then build toward Tier 3-4 (genuinely new capabilities).

---

## Part 6: Feedback FOR the Second Brain

> **Take this section back to the second brain. This is what a first consumer actually experienced.**

### F1. The compliance checker needs consumer-awareness (CRITICAL)

Telling a production project with enforced stage gates that it's at Tier 0 because file names differ is actively harmful. The checker should:

- Accept the target wiki's own schema
- Check for functional equivalence (has schema? has templates? has methodology config?) not path conformance
- Report what the project HAS, not just what it's MISSING relative to one expected layout

### F2. The health score needs consumer-awareness (CRITICAL)

Running the second brain's validation against a consumer wiki produces garbage metrics. 332 "errors" that are really "your schema is different from ours." The health check should either use `--wiki-root`'s own validation or clearly label "scored against second-brain schema" vs "scored against project schema."

### F3. `gateway orient` shortcircuit for "returning" is premature

Having an identity profile in the second brain ≠ the current Claude session has prior context. The first time a consumer connects live, orient should give the full landscape even if the second brain has an existing profile. Detect "returning" from SESSION state (conversation history, gateway invocation timestamp), not from PROFILE existence.

### F4. The identity profile conflation is real and live

The `status` command asks for a static Identity Profile table in CLAUDE.md. The `execution-mode-is-consumer-property` lesson says most of that table's fields are consumer properties. The gateway tooling hasn't implemented its own lesson. This is the #1 confusion point for a new consumer.

**Suggested fix:** Split the Identity Profile into:

- **Project Identity** (stable, goes in CLAUDE.md): type, domain, second-brain relationship
- **Consumer Context** (dynamic, declared per-connection): execution mode, SDLC profile, methodology model, trust tier

### F5. There's no "first integration roadmap" command

A first consumer needs: "Here's what absorbing the second brain looks like. It's 4-5 milestones, 15-25 epics. Here's Tier 1. Start here." None of the existing commands produce this. `flow` is generic. `what-do-i-need` is per-task. `orient` shortcircuits. The gap between "connected" and "integrating" has no bridge.

### F6. The standards-first reading order may be better for integration consumers

The adoption guide recommends models first. For a consumer that already has methodology infrastructure and needs to align it, reading standards first ("what good looks like") before models ("what the system is") may be more actionable. The operator could assess gaps against standards without reading 800-line model pages.

### F7. Feed-back format needs a bridge or a decision

Consumer lessons (our format) ≠ second brain lessons (their format). Either:

- `gateway contribute` should accept consumer-format lessons and normalize them
- A format guide should tell consumers how to write in the second brain's format
- Or: consumers contribute as raw sources and the second brain synthesizes

The current state is ambiguous — `gateway contribute` exists but the format expectations aren't documented for consumers.

### F8. The scale estimate should be surfaced explicitly

Nowhere in the second brain's documentation does it say "full integration is 150+ tasks across 30+ epics." The 4-tier adoption model implies graduated effort but doesn't quantify it. A first consumer reading "Tier 1: 1 hour" may think the whole thing is a weekend project. The real scale needs to be explicit, especially for Tier 3-4.

### F9. We have 6 new lessons the second brain doesn't have

These are contribution candidates:

1. `lesson-harness-turncount-misnamed.md` — counting streaming events as turns
2. `lesson-multi-task-cost-growth.md` — monotonic cost growth in multi-task runs
3. `lesson-hook-protects-operator-during-runs.md` — pre-write hook prevents operator/agent race
4. `lesson-clean-win-scope-expansion.md` (refinements 1+2) — Class A/B/C scope expansion taxonomy
5. `lesson-methodology-model-right-sizing.md` — integration model saves 86.8% vs feature-development
6. `lesson-epic-readiness-sparse-children.md` — readiness math fails on sparse-children epics

These extend the second brain's enforcement and harness engineering knowledge with evidence from T088-T120 operations.

---

## Part 7: What We Should Do Next (Revised)

### Immediate (this session / next session)

1. **Take this document to the second brain session** — this IS the feedback. Use it to evolve the gateway tooling and integration path.
2. **Contribute the 6 new lessons** via `gateway contribute` — test the feed-back loop with real content.
3. **Don't try to fix the compliance/health scores** — they're measuring the wrong thing. Fix the tools, not our project.

### Short-term (next 1-2 weeks, alongside turbo-mode agent runs)

4. **Spec the schema convergence decision** — do we migrate, extend, or bridge? This is a blocking architectural decision before any deep integration work.
5. **Identify which of the 25 standards are relevant to OpenArms** — probably 8-10 of them. The rest are second-brain-internal.
6. **Start using `gateway query` in task spec generation** — when writing new task specs, query the second brain for artifact chains and stage rules. This is low-cost, high-signal integration.

### Medium-term (the actual integration milestones)

7. **Milestone 1: Schema + Format Alignment** — converge wiki schema, lesson format, relationship vocabulary. Prerequisite for everything else.
8. **Milestone 2: Standards Adoption** — adopt relevant standards, encode rules in hooks/validators. Evolve our enforcement infrastructure.
9. **Milestone 3: Model Absorption** — deep-read each relevant model, identify gaps, spec tasks to close them. The methodology model is mostly done; others need work.
10. **Milestone 4: Evolution Pipeline** — Tier 3 adoption. Maturity lifecycle, scoring, promotion for our wiki pages. New capability.
11. **Milestone 5: Hub Integration** — Tier 4. Bidirectional sync, export profiles, full ecosystem participation.

**Scale: 30+ epics, 150+ tasks, multiple months of sustained effort.** This is the real scope.

---

## Part 8: Second Round — After Feedback (2026-04-16, same session)

> The operator took Part 6's feedback to the second brain. The second brain updated its gateway tooling. We re-tested. This section records what changed and what's left.

### What the second brain fixed (immediately, within minutes)

#### F1 → FIXED: Compliance checker now finds our schema

Before: `✗ wiki/config/wiki-schema.yaml` — looked for exact filename.
After: `✓ wiki/config/schema.yaml — Frontmatter schema (any location)` — finds our schema by function.

The checker went from Tier 0 ("Not yet adopted") to "1 file away from Tier 1, functionally Tier 2." Our only Tier 1 gap is now `wiki/config/templates/`. This is a real gap — we don't have page templates in a standard location.

Tier 3 also improved: `✓ scripts/methodology/validate-stage.cjs — Quality/validation tooling` — it found our validation infrastructure even though it's CJS scripts, not Python.

Tier 4: now `2/3` — found both `.mcp.json` entries. Only missing `export-profiles.yaml`.

**Verdict: F1 addressed. The checker now measures functional equivalence, not path conformance.**

#### F4 → FIXED: Identity profile no longer asks for consumer properties

Before: `IDENTITY: not configured. Add Identity Profile table to CLAUDE.md`
After: `PROJECT IDENTITY: not fully configured. Stable fields to add to CLAUDE.md: type, domain, second-brain relationship. Do NOT hardcode: execution mode, SDLC profile, methodology model (these are consumer/task properties)`

The status command now explicitly tells you which fields are project-level (stable, go in CLAUDE.md) vs consumer-level (dynamic, don't hardcode). This is exactly the split we proposed.

**Verdict: F4 addressed. The gateway no longer contradicts its own lesson.**

#### F5 + F8 → FIXED: Orient now shows scale and adoption tiers

Before: `"You have prior context. Route directly to brain queries."` (one-liner)
After: Full orientation with:

- The core principle: "YOUR BRAIN IS YOUR OWN... The second brain is a SEPARATE shared knowledge system. Your goal is NOT to depend on it at runtime."
- 4 adoption tiers with descriptions
- Scale estimate: "15-25 epics, 80-150+ tasks across months"
- Reading order: standards before models (our F6 recommendation)
- Contribute guidance: "Your format is accepted — the second brain normalizes on intake" (our F7 concern)

**Verdict: F5 and F8 addressed. A first consumer now gets the full picture including realistic scale.**

#### F6 → FIXED: Standards-first reading order

Before: Orient didn't specify reading order.
After: "WHAT TO READ FIRST: 1. standards → 2. spine → 3. model methodology → 4. lessons → 5. patterns"

**Verdict: F6 addressed.**

#### F7 → FIXED: Feed-back format bridge clarified

Before: Ambiguous — no documentation on what format `contribute` expects.
After: Orient says "Your format is accepted — the second brain normalizes on intake."

**Verdict: F7 addressed at the messaging level. Needs testing with actual contributions.**

### What's still open after the second brain update

#### F2: Health score still needs investigation

We haven't re-run `gateway health` yet. The 332 validation errors and 0.9 relationship density were likely schema-mismatch artifacts. If the compliance checker now respects our schema, does the health checker too?

#### F3: Orient freshness detection

The orient command now gives full output for sister projects regardless of freshness. This may have overcorrected — a returning consumer who already knows the landscape doesn't need the full orientation every time. But for now, more information > less information. The nuance can come later.

#### F9 → TESTED: Lesson contribution works

Contributed `lesson-harness-turncount-misnamed.md` via:

```
gateway contribute --type lesson --title "..." --content "..." --contributor "openarms-operator-claude" --source "/path/to/local/lesson"
```

Result: landed in `lessons/00_inbox/` with `contribution_status: pending-review`. The second brain assigned it to the maturity inbox for human review before promotion. The `gateway timeline` confirmed the contribution appears in the cross-project temporal view.

**The format bridge works.** We sent our content; the second brain wrapped it in its own frontmatter (added `layer: 4`, `maturity: seed`, `contribution_status: pending-review`). We don't need to write in their format — `contribute` normalizes.

**Observation:** The timeline also showed that the second brain had ALREADY ingested our other 5 lesson files independently — they appear as `_lesson_` entries in `00_inbox` with creation dates of 2026-04-16. The operator must have fed them directly or the second brain pulled them from our repo.

### New observations from the second round

#### The "adopt not depend" framing changes everything

The orient output's opening line — "Your goal is NOT to depend on it at runtime — it's to ADOPT what fits your identity and evolve your own brain until it's strong on its own" — is the correct framing we were missing in the first round. This means:

- The harness agent should NOT call `gateway query` at runtime
- Instead, the OUTPUT of `gateway query` should inform how we evolve our local `methodology.yaml`, `skill-stage-mapping.yaml`, hooks, and skills
- The second brain is a knowledge source for EVOLUTION, not a service for RUNTIME DEPENDENCY
- Each adoption tier is about absorbing knowledge into local infrastructure, not connecting to external services

This aligns with the operator's correction: the goal is to make our brain stronger, not to add a runtime dependency.

#### The compliance gap is now clear and actionable

One item to Tier 1: `wiki/config/templates/` — we need page templates.
The Tier 2 gap was already closed (we have methodology.yaml + backlog + AGENTS.md).
Tier 3 needs: evolution pipeline tooling + knowledge layer structure.
Tier 4 needs: export profiles.

This is a real, measurable integration path — not "do everything at once."

#### The `what-do-i-need` reframing is correct

"These methodology models should be in YOUR project's methodology.yaml" — positions the second brain as a reference for evolving local config. Compare to the old framing which implied runtime querying. The new framing says: read this, adopt what fits, put it in YOUR files.

### Deeper exploration findings (continued second round)

#### F2 FOLLOW-UP: Health check now uses our schema but still scores 54/100

Re-ran `gateway health`. Good news: it now says `Schema: /home/jfortin/openarms/wiki/config/schema.yaml` and `Source: project-own`. It's using OUR schema. Score barely changed: 54.4/100 with 333 validation issues.

This means the 333 errors are NOT schema-mismatch artifacts — they're real violations of OUR OWN schema. Our pages are failing our own rules. The health check is now legitimate.

The breakdown:

- **validation: 0/100** (333 blocking issues) — our pages don't conform to our own `schema.yaml` required_sections. Example: our `lesson` type requires `[Summary, Context, Insight, Application, Relationships]` but our actual lessons use `[Summary, Evidence, Root Cause, Relationships]`. We wrote a schema we don't follow.
- **relationships: 12/100** (avg 1.0/page, healthy ≥6) — our `related:` frontmatter has 2-4 entries. The health check wants 6+ typed relationships. This is a real gap in our wiki's cross-linking density.
- **freshness: 76/100** (309/405 pages updated within 90d) — 96 stale pages.
- **evolution: 100/100** — all pages past inbox. Good.
- **ingestion_backlog: 100/100** — no unreferenced raw files. Good.

**The uncomfortable truth:** The health check revealed that our OWN schema is aspirational, not operational. We defined `required_sections` for each type but never enforced them. Our validation pipeline (`validate-stage.cjs`) checks task frontmatter, not wiki page section structure. This is a real gap — and it's ours, not the second brain's.

**What this means for integration:** Before we can reach Tier 3 (evolution pipeline), we need to either (a) align our pages to our own schema, or (b) align our schema to what our pages actually look like. Both are work. The schema was written aspirationally when the wiki was scaffolded; the pages evolved differently. This is the same bug the second brain's lesson `"Systemic Incompleteness Is Invisible to Validation"` describes — we had 0 validation errors before because nobody was validating section structure.

#### Artifact chains are not queryable — the deepest operational data is in prose

`gateway query --model feature-development --full-chain` returns `chain: {}`. All 9 models return `has_chain: False, stage_count: 0`. The artifact chain data (24 artifacts for feature-development in the TypeScript domain, per-stage ALLOWED/FORBIDDEN, gate commands) exists in the model pages as rich markdown — I read it in detail — but it's NOT in structured config the gateway can return.

Similarly, `gateway query --stage implement --domain typescript` returns readiness ranges (80-95) but empty ALLOWED/FORBIDDEN lists and empty gate commands. The rich operational rules ("ALLOWED: business logic, helper functions. FORBIDDEN: modifying test files. REQUIRED: at least one existing runtime file must import new code") are in the model page prose, not in queryable config.

This is a significant gap for the "adopt into your own brain" flow. The gateway can tell you which models and stages exist, but NOT what artifacts each stage produces or what rules each stage enforces. To get that, you have to read the full model pages (~800 lines each). The gateway is a table of contents, not an encyclopedia.

**What the second brain should evolve:** Either (a) structure the artifact chain data as YAML/JSON that the gateway can return, or (b) make the gateway query commands read and extract from the model page markdown. Option (a) is cleaner but requires maintaining two copies. Option (b) is harder but keeps a single source of truth.

**What this means for OpenArms:** When we want to evolve our `methodology.yaml` or `skill-stage-mapping.yaml` to align with the second brain's artifact chains, we can't query for the data — we have to read the full model pages. The gateway is useful for orientation and navigation but not yet for structured adoption of artifact chain rules.

#### SDLC profiles not queryable — "No sdlc-profiles directory found"

`gateway query --profiles` returned `error: No sdlc-profiles directory found`. The SDLC profiles (simplified/default/full) are documented in the model pages and referenced extensively, but the config files don't exist yet in the second brain. The gateway's navigate command lists them; the query command can't return them.

This is another "knowledge exists in prose, not in queryable config" gap. The Goldilocks protocol talks about 3 SDLC profiles; the tooling can't deliver them.

#### The lesson template is rich and instructive

`gateway template lesson` returns a full template with:

- Required sections: Summary, Context, Insight, Evidence, Applicability, Relationships
- Styling guidelines inside HTML comments (use `> [!warning]` for failure lessons, `> [!tip]` for success lessons, tables inside `> [!abstract]`)
- Example content showing what good evidence items look like
- Minimum requirements ("MINIMUM 3 evidence items from different sources")

This is significantly richer than our lesson format. Our lessons have Summary + Evidence + Root Cause + Relationships. Theirs want Context (when does this apply?), Insight (the core learning, with callout styling), Evidence (3+ items with specific formatting), and Applicability (per-domain table).

**Integration decision needed:** Do we adopt the second brain's lesson template for new lessons going forward? It's better structured. But our existing 16 lessons would need reformatting. Or we could adopt it for new lessons only and let the old ones be "pre-standard" artifacts.

#### The timeline is the most powerful cross-project tool

`gateway timeline` shows OpenArms and research-wiki activity interleaved chronologically with semantic event types: commits, epic progress (readiness changes), lessons, directives, sessions, handoffs. It showed:

1. Our integration feedback was ingested as a directive in the second brain
2. E022 went from 15% → 95% readiness in the same day based on our feedback
3. Our 6 contributed lessons are visible as inbox items
4. The operator's verbatim frustration messages were captured as directives

This is real cross-project visibility. It answers "what happened across the ecosystem today?" in one command. For turbo-mode agent runs, running `gateway timeline` after each run could show how the work affected the ecosystem — not just our repo.

#### The navigate command is a clean entry point

`gateway navigate` outputs a tree-structured view of the full knowledge system: Identity → SDLC Profiles → Methodology Chains → Models → Stages → Enforcement → Principles → Tracking → Hierarchy → PM Levels → Tools. Each node has the gateway command to drill deeper. This is the map of the territory.

For integration planning, the navigate tree is the closest thing to "here's what you could adopt." Each branch is a potential integration workstream. The navigate tree with 11 top-level branches roughly maps to the milestone structure: each branch becomes 1-3 epics of adoption work.

### Summary of the second round

**What improved:** orient (massive), status (fixed identity conflation), compliance (finds our schema), contribute (works), timeline (powerful).

**What's still broken:** artifact chains not queryable (prose-only), SDLC profiles not queryable (config doesn't exist), ALLOWED/FORBIDDEN not in stage queries, health validation counts are now real (our own schema violations).

**What we learned about ourselves:** Our wiki schema is aspirational, not operational. We defined required_sections we never enforce. 333 of our own pages violate our own rules. This is a real debt that any integration work must address first.

**The critical reframe confirmed:** The second brain is a knowledge system to ADOPT FROM, not a runtime service. The gateway is a navigation aid and contribution channel. The real work is evolving our local brain (CLAUDE.md, methodology.yaml, skill-stage-mapping.yaml, hooks, validators, page templates, wiki schema) to absorb the second brain's operational knowledge. That work is 30+ epics. It starts with fixing our own schema compliance.

---

## Part 9: Full Model Survey — What Each Model Means for OpenArms Integration

All 16 models read. Here's what each one means for us, organized by integration relevance.

### Already integrated (we built these patterns)

| Model                              | What it covers                                                       | Our status                                                                  | Integration work needed                                                                                                                   |
| ---------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Methodology**                    | 9 named models, stage gates, ALLOWED/FORBIDDEN, composition          | We ARE the primary evidence source. methodology.yaml matches 1:1.           | Adopt composition rules, quality dimension (Skyscraper/Pyramid/Mountain explicit selection), domain-specific artifact chains. Low effort. |
| **SFIF and Architecture**          | Scaffold→Foundation→Infrastructure→Features lifecycle, quality tiers | We follow SFIF implicitly. Our epics are SFIF stages (E014=Infrastructure). | Make SFIF explicit in our wiki and task planning. Adopt the audit checklist. Low effort.                                                  |
| **Quality and Failure Prevention** | Three-layer defense, 7 failure classes, enforcement hierarchy        | We have hooks (Layer 1), teaching (Layer 2 via skills), review gates.       | Name our failure classes using the taxonomy. Track clean completion rate. Add the 7-class tracking to post-run reports. Medium effort.    |

### Partially integrated (infrastructure exists, knowledge needs absorption)

| Model                           | What it covers                                                                 | Our status                                                            | Integration work needed                                                                                                                                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude Code**                 | 4-level extension system, context management, harness engineering              | We have all 4 levels: CLAUDE.md, 5 skills, 4 hooks, 3 commands.       | Adopt CLAUDE.md standards (under 200 lines — ours is ~700 including AGENTS.md). Adopt skill quality bar (progressive disclosure, trigger phrases). Adopt hook coverage patterns (R01-R13 guardrails). HIGH effort.   |
| **Skills, Commands, and Hooks** | Extension hierarchy, context-aware loading, Plannotator pattern                | We have 5 methodology skills + stage-mapping.                         | Adopt skill-stage-mapping standards. Add more hook patterns (currently 4 hooks, the second brain documents 13 guardrail rules). Adopt the Plannotator pattern for command+hook composition. Medium effort.           |
| **Context Engineering**         | Three levels (prompt/context/structural), autocomplete chain, tier-based depth | Our injection envelope is one instance. Post-compact hook is another. | Adopt the full autocomplete chain (8 steps). Implement tier-based context depth in our skill injection. Formalize our 5 cognitive contexts as the second brain's "per-context injection design." MEDIUM-HIGH effort. |
| **Markdown as IaC**             | CLAUDE.md + DESIGN.md + AGENTS.md + SOUL.md companion ecosystem                | We have CLAUDE.md (=AGENTS.md symlink). No DESIGN.md, no SOUL.md.     | Evaluate whether DESIGN.md and SOUL.md are relevant for OpenArms. If the fleet vision advances, SOUL.md becomes critical. LOW priority, low effort when needed.                                                      |
| **Ecosystem Architecture**      | 5-project topology, integration map, knowledge feedback loop, dual-perspective | We're one of the 5 projects. The identity profile captures our role.  | Formalize our integration points (what we consume, what we produce). Adopt the dual-perspective principle (standalone + ecosystem node). LOW effort.                                                                 |

### Not integrated (genuinely new capability)

| Model                        | What it covers                                                               | Our status                                                                   | Integration work needed                                                                                                                                                             |
| ---------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Knowledge Evolution**      | 6-layer density architecture, scorer, maturity lifecycle, promotion pipeline | We have lessons but no evolution pipeline. No scorer. No maturity promotion. | This is Tier 3 adoption. Build local evolution pipeline (or adopt the second brain's). Add maturity lifecycle to our wiki pages. HIGH effort — this is multiple epics.              |
| **LLM Wiki**                 | What a wiki IS — schema, operations, quality gates, navigation               | We have a wiki with schema but 333 validation failures.                      | Fix our schema compliance. Adopt quality gates (summary ≥30 words, ≥1 relationship, ≥6 relationships for healthy). Adopt the page-type standards. HIGH effort — touches 400+ pages. |
| **Wiki Design**              | Visual layer — callout vocabulary, styling standards                         | We don't use callout vocabulary consistently.                                | Adopt callout styling (> [!warning], > [!tip], > [!info], > [!abstract]) for our wiki pages. LOW effort per page, but 400+ pages to evolve.                                         |
| **Automation and Pipelines** | Post-chain, event-driven hooks, multi-pass ingestion                         | We have validate-stage.cjs and build pipeline but no wiki-level post-chain.  | Build a wiki validation post-chain (our version of `pipeline post`). Add event-driven hooks for wiki changes. MEDIUM effort.                                                        |
| **Second Brain**             | PKM theory — PARA + Zettelkasten hybrid, maintenance automation              | We use the wiki as knowledge store but not as a PKM system.                  | Adopt progressive distillation as a conscious practice. Map our wiki to PARA buckets. CONCEPTUAL — changes how we think about the wiki, not just tooling.                           |
| **Local AI ($0 Target)**     | Cost reduction via local inference routing, AICP integration                 | We track cost but don't route to local models.                               | Relevant when AICP matures. LOW priority now.                                                                                                                                       |
| **MCP and CLI Integration**  | CLI+Skills vs MCP decision, context-mode sandbox                             | We use CLI+Skills. We have `.mcp.json` for the second brain.                 | Already aligned. Adopt the context-mode sandbox pattern for heavy subagent operations. LOW effort.                                                                                  |
| **NotebookLM**               | External research tool as grounded complement                                | Not integrated, not a priority.                                              | SKIP for now.                                                                                                                                                                       |

### Key standards to adopt (from the 25 available)

| Standard                          | Why it matters for us                                                                   | Priority                                            |
| --------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Methodology Standards**         | Defines execution quality bar. Gold-standard examples from our own ecosystem.           | P0 — read and internalize immediately               |
| **Claude Code Standards**         | Defines CLAUDE.md, skill, hook, context management quality bars. Our config needs work. | P0 — our CLAUDE.md is 700+ lines, should be <200    |
| **Task Page Standards**           | Defines task spec quality. "Done When must name specific files." We mostly follow this. | P1 — adopt formally, add to task spec template      |
| **Lesson Page Standards**         | Defines lesson format. Our 16 lessons use a different format.                           | P1 — adopt for new lessons, don't retrofit old ones |
| **Quality Standards**             | Defines failure prevention quality bar. Three-layer defense + 7 failure classes.        | P1 — adopt the taxonomy                             |
| **Context Engineering Standards** | Defines structured context quality bar.                                                 | P2 — after Claude Code standards                    |
| **Extension Standards**           | Defines skill/command/hook quality bar.                                                 | P2 — after Claude Code standards                    |
| **Epic Page Standards**           | Defines epic spec quality. Our epics are lightweight.                                   | P2 — useful when creating integration epics         |

### The integration roadmap (preliminary)

Based on the full model survey, here's the shape of the work:

**Milestone 0: Foundation Alignment (prerequisite to everything)**

- Epic: Fix our own schema compliance (333 validation failures)
- Epic: CLAUDE.md restructure (700→200 lines, route to files)
- Epic: Adopt task page standards (specific Done When, frontmatter completeness)
- Epic: Adopt lesson page standards (for new lessons going forward)
- **~4 epics, ~15-25 tasks**

**Milestone 1: Methodology Deepening**

- Epic: Adopt quality dimension (explicit Skyscraper/Pyramid/Mountain selection per task)
- Epic: Adopt model composition rules (sequential, nested, conditional, parallel)
- Epic: Adopt domain-specific artifact chains (TypeScript chain, 24 artifacts)
- Epic: Adopt the 7 failure class taxonomy in post-run reports
- Epic: Enrich stage rules (ALLOWED/FORBIDDEN in our methodology.yaml with gate commands)
- **~5 epics, ~20-30 tasks**

**Milestone 2: Enforcement Evolution**

- Epic: Adopt R01-R13 guardrail hook patterns (expand our 4 hooks to cover the 13 rules)
- Epic: Adopt Claude Code standards (CLAUDE.md structure, skill quality bar, hook patterns)
- Epic: Implement Plannotator pattern (command+hook composition)
- Epic: Adopt context autocomplete chain (8-step context build from CLAUDE.md to post-compact)
- Epic: Implement tier-based context depth in skill injection
- **~5 epics, ~25-35 tasks**

**Milestone 3: Wiki Evolution**

- Epic: Adopt LLM Wiki quality gates (summary length, relationship density, freshness)
- Epic: Build wiki validation post-chain (our `pipeline post` equivalent)
- Epic: Adopt wiki design standards (callout vocabulary, styling consistency)
- Epic: Add relationship density (from avg 1.0 to target 6.0 per page)
- Epic: Adopt progressive distillation as a practice
- **~5 epics, ~30-40 tasks**

**Milestone 4: Knowledge Evolution Pipeline (Tier 3)**

- Epic: Build evolution scorer (6 signals, deterministic)
- Epic: Build maturity lifecycle for wiki pages (seed→growing→mature→canonical)
- Epic: Build promotion pipeline with human review gate
- Epic: Add knowledge layer structure (L1-L6)
- **~4 epics, ~20-30 tasks**

**Milestone 5: Hub Integration (Tier 4)**

- Epic: Build export profiles for the second brain
- Epic: Implement MCP_CLIENT_RUNTIME declaration
- Epic: Build bidirectional sync (contribute pipeline + import pipeline)
- Epic: Implement contribution gating for multi-agent work
- **~4 epics, ~15-25 tasks**

**Total: ~23 epics, ~125-185 tasks, 5 milestones. Estimated 800-1200 hours of agent+operator work.**

This is the real scale. It's not a weekend project. It's months of sustained effort that transforms OpenArms from a project with a wiki into a project with a fully integrated knowledge evolution system connected to a cross-project intelligence hub.

---

## Part 10: Third Round — Artifact Chains and SDLC Profiles Now Queryable

The second brain dropped another update. The commit message: `feat: Enhance gateway queries to utilize brain's methodology for canonical chain definitions and improve SDLC profile handling`.

### What changed — both major gaps from Part 8 are fixed

#### Artifact chains are now fully structured and queryable

`gateway query --model feature-development --full-chain` now returns full per-stage data:

```
document:
  required: [{artifact: wiki-page, count: 1+, purpose: "Requirements spec, infrastructure analysis, gap analysis",
              templates: [requirements-spec, infrastructure-analysis, gap-analysis]}]
  forbidden: [code-file, test-file]
  gate: {checks: [wiki-page-exists, no-code-files-created]}

scaffold:
  required: [{artifact: type-definition, purpose: "Types, interfaces, schemas — zero behavior"},
             {artifact: test-stub, purpose: "Empty test files with placeholder assertions"}]
  forbidden: [implementation, test-implementation]
  gate: {checks: [types-compile, no-business-logic, test-stubs-exist]}

implement:
  required: [{artifact: implementation, purpose: "Business logic filling scaffold stubs"},
             {artifact: integration-wiring, purpose: "Existing file imports and calls new code"}]
  forbidden: [test-implementation]
  gate: {checks: [code-compiles, lint-passes, integration-wiring-exists]}

test:
  required: [{artifact: test-implementation, purpose: "Real assertions replacing scaffold placeholders"},
             {artifact: test-results, purpose: "Gate output showing 0 failures"}]
  gate: {checks: [tests-pass, no-placeholder-assertions]}
```

All 9 chains now return `has_chain: True`. The integration chain is equally detailed:

```
scaffold: {required: [type-definition (bridge adapter interfaces), test-stub]}
implement: {required: [implementation (bridge logic, <80 LOC), integration-wiring (consumer file modified)]}
test: {required: [test-implementation (proves wiring works), test-results (0 failures)]}
```

**Why this matters for OpenArms:** This structured data is exactly what our `validate-stage.cjs` needs. Today our validator checks basic stage rules from `methodology.yaml`. With this chain data, it could check: "Did the scaffold stage produce type definitions? Did the implement stage modify an existing consumer file? Are there test stubs from scaffold still containing placeholders?" The gap between what the second brain knows and what our validator enforces just got bridgeable.

#### SDLC profiles are now queryable

Three profiles returned:

| Profile        | Phases                           | Scale                  | Models                                 |
| -------------- | -------------------------------- | ---------------------- | -------------------------------------- |
| **simplified** | POC, early-MVP                   | micro, small           | 4 (hotfix, bug-fix, docs, feature-dev) |
| **default**    | MVP, staging, early-production   | small, medium          | all 8                                  |
| **full**       | staging, production, maintenance | medium, large, massive | all 8                                  |

We're at `default` trending `full`. This confirms we have the right model set and our process weight is appropriate for our phase.

#### Stage queries still return empty ALLOWED/FORBIDDEN

`gateway query --stage implement --domain typescript` still returns empty `allowed_outputs` and `forbidden_outputs`. The rich data now lives in the chain definitions (`required`/`forbidden` per stage per model), not in the standalone stage query. Two access paths to similar data — the chain path is now complete, the stage path is still sparse. This is a minor gap now that chains work.

### The real-time feedback loop in action

This session has produced a live demonstration of the OFV (Observe-Fix-Verify) loop across two projects:

1. **Round 1** — We observed 9 problems (F1-F9). Documented them.
2. **Round 2** — The operator took the feedback to the second brain. F1, F4, F5, F6, F7, F8 fixed within minutes. We verified.
3. **Round 3** — We documented deeper gaps (artifact chains empty, SDLC profiles missing). The second brain fixed both. We verified.

Three OFV cycles in one session. The gap between "knowledge exists in the model pages" and "knowledge is queryable via the gateway" has been closing in real time.

### What this means for the integration roadmap

**The gateway is now a real adoption tool, not just an orientation aid.** With structured artifact chains, a consumer can:

1. Query the chain for their task's model
2. Compare the chain's per-stage requirements against their local validator
3. Identify which gate checks they enforce and which they don't
4. Spec tasks to add missing enforcement

This changes Milestone 1 (Methodology Deepening) from "read model pages and manually extract rules" to "query chains and diff against local config." Much more automatable. The harness prompt builder could call `gateway query --model integration --full-chain` and embed the chain rules directly into the agent's context. Not as a runtime dependency — as a one-time adoption artifact that gets committed to our local config.

### Remaining gaps (as of end of third round)

1. **Stage query empty** — `--stage --domain` returns readiness ranges but no ALLOWED/FORBIDDEN. Chains have this data but you need to know the model first.
2. **Health validation details** — 336 errors but no way to see WHICH pages fail and WHY. No `--verbose` flag. The second brain would need to add detail output.
3. **Our 333 schema violations** — still entirely our problem. No second-brain fix can address this. We wrote aspirational required_sections we never validate.
4. **CLAUDE.md size** — ours is 700+ lines (AGENTS.md symlinked). The standard says <200. This is Milestone 0, epic 2. Large restructure.

---

## Relationships

- PRODUCED_BY: 2026-04-16 operator-Claude session — first consumer integration with second brain
- EVIDENCE: `gateway status`, `gateway compliance`, `gateway health`, `gateway orient`, `gateway what-do-i-need`, `gateway flow`, `gateway query --model --full-chain`, `gateway query --profiles`, `gateway query --chains`, `gateway query --stage`, `gateway navigate`, `gateway timeline`, `gateway contribute` outputs
- EVIDENCE: Full reads of ALL 16 model pages, 3 standards pages, 1 identity profile, 1 lesson, 1 epic from the second brain
- EVIDENCE: 3 OFV cycles observed in real time — feedback delivered, fixes applied, verification passed
- INFORMS: second brain E022 (Context-Aware Gateway Orientation)
- INFORMS: future integration milestone planning — Milestone 1 now more automatable via structured chain queries
- INFORMS: `MCP_CLIENT_RUNTIME` implementation
- INFORMS: OpenArms `validate-stage.cjs` evolution to use second-brain chain data
- RELATES_TO: `wiki/log/2026-04-16-handoff-turbo-mode-preparation.md`
- RELATES_TO: `wiki/domains/learnings/lesson-five-claude-contexts.md` (the identity varies by cognitive context)

---

## Part 11: E016 Chain Walkthrough — Where We Actually Stand

The second brain has a 17-step integration chain (`wiki/spine/references/second-brain-integration-chain.md`) and an epic (E016) that says "prove it works with OpenArms." We ARE the proof. Here's each step, what we did, and whether it passed.

### Phase 1: Discovery

| Step                     | Command                  | Status  | Notes                                                                                                                            |
| ------------------------ | ------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 1. First Contact         | `gateway` (no args)      | ✅ Done | Guided entry works.                                                                                                              |
| 2. Auto-Detect Identity  | `gateway what-do-i-need` | ✅ Done | Detected domain: typescript, returned task-type routing table. Correctly says "these models should be in YOUR methodology.yaml." |
| 3. Browse Knowledge Tree | `gateway navigate`       | ✅ Done | Full tree with 11 branches, each with drill-down commands. Clean.                                                                |

### Phase 2: Identity

| Step                        | Command                    | Status              | Notes                                                                                                                                                                                                                                                                                                                                           |
| --------------------------- | -------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4. Declare Identity Profile | Add table to CLAUDE.md     | ❌ NOT DONE         | Our CLAUDE.md has no Identity Profile table. The `status` command correctly tells us which fields are stable (type, domain, second-brain relationship) vs consumer properties (execution mode, SDLC profile). But we haven't declared the stable fields yet. **BLOCKER: Our CLAUDE.md is 700+ lines and needs restructure before adding more.** |
| 5. Select SDLC Profile      | `gateway query --profiles` | ✅ Done (read-only) | We know we're `default` trending `full`. Not yet declared in CLAUDE.md.                                                                                                                                                                                                                                                                         |

### Phase 3: Methodology

| Step                    | Command                                                  | Status     | Notes                                                                                                                                                                  |
| ----------------------- | -------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 6. Understand Models    | `gateway query --models`                                 | ✅ Done    | All 9 models match our methodology.yaml 1:1.                                                                                                                           |
| 7. Learn Stages         | `gateway query --model feature-development --full-chain` | ✅ Done    | Full artifact chain returned with required/forbidden/gate per stage. As of Round 3, this works for all 9 models.                                                       |
| 8. Domain Stage Details | `gateway query --stage implement --domain typescript`    | ⚠️ Partial | Returns readiness ranges but ALLOWED/FORBIDDEN are empty. The data is in the chain (Step 7) not the stage query. Functionally covered but via a different access path. |

### Phase 4: Standards

| Step                          | Command                                            | Status            | Notes                                                                                                                                                                                                                                                      |
| ----------------------------- | -------------------------------------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 9. Review Quality Standards   | Read standards pages                               | ✅ Done           | Read Methodology Standards, Claude Code Standards, Task Page Standards. Key finding: our CLAUDE.md violates the <200 line standard. Our task specs mostly follow the Task Page Standard. Our lessons use a different format than the Lesson Page Standard. |
| 10. Get Templates             | `gateway template lesson`, `gateway template task` | ✅ Done           | Both templates are rich with inline guidance, examples, and styling directives. The task template includes readiness vs progress explanation and specific Done When examples.                                                                              |
| 11. Review Frontmatter Fields | `gateway query --field readiness`                  | ⚠️ Not tested yet | Haven't queried individual field definitions.                                                                                                                                                                                                              |

### Phase 5: Work Loop

| Step                             | Command                                 | Status                      | Notes                                                                                                                                                                                                                                                                                           |
| -------------------------------- | --------------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 12. Follow Stage Sequence        | Execute a real task following the chain | ⚠️ Not done in THIS session | We've executed 120+ tasks (T001-T120) following our own stage sequence. The second brain's chain matches our operational practice. But we haven't done one USING the chain output as the source of truth.                                                                                       |
| 13. Track Readiness and Progress |                                         | ⚠️ Partial                  | We track `readiness` and `stages_completed` in task frontmatter. We DON'T track `progress` as a separate dimension — the second brain defines readiness (definition completeness) and progress (execution completeness) as two independent fields. We conflate them into one `readiness` field. |
| 14. Handle Impediments           |                                         | ⚠️ Partial                  | We have `/concern` for raising issues. The second brain defines 8 impediment types (technical, dependency, decision, environment, clarification, scope, external, quality). We don't type our impediments.                                                                                      |

### Phase 6: Feedback

| Step                     | Command                            | Status      | Notes                                                                                                                                                                                                                   |
| ------------------------ | ---------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 15. Contribute Learnings | `gateway contribute --type lesson` | ✅ Done     | Successfully contributed `lesson-harness-turncount-misnamed.md`. Landed in `00_inbox` with `pending-review` status. Timeline confirmed it appeared. The second brain also ingested 5 more of our lessons independently. |
| 16. Scan Project         | `pipeline scan ../openarms/`       | ❌ Not done | Haven't run the project scanner. This would feed our CLAUDE.md, methodology.yaml, lessons, etc. as raw sources for the second brain to synthesize.                                                                      |

### Phase 7: Local/Remote Mode

| Step            | Command | Status  | Notes                                                                                                                                 |
| --------------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 17. Choose Mode |         | ✅ Done | We're using local mode via `tools/gateway.py` forwarder with `--wiki-root` pointed at our working directory. Auto-detected correctly. |

### Chain Score: 10/17 fully done, 4/17 partial, 3/17 not done

**Fully done (10):** Steps 1, 2, 3, 5, 6, 7, 9, 10, 15, 17
**Partial (4):** Steps 8, 11, 13, 14
**Not done (3):** Steps 4 (Identity Profile in CLAUDE.md), 12 (real task using chain), 16 (project scan)

### What blocks us from completing the chain

1. **Step 4 — Identity Profile** is blocked by CLAUDE.md restructure. At 700+ lines, adding more content is wrong. We need to shrink it first (route to files per the <200 line standard), THEN add the identity profile. This is Milestone 0, Epic 2 in the roadmap.

2. **Step 12 — Real task using chain** requires running an `agent run` where the agent's methodology source is the second brain's chain output rather than (or in addition to) our local skills. This is a real integration task — it needs the harness to bake chain data into the agent prompt.

3. **Step 16 — Project scan** can be done now. It's just running a command. Low effort.

4. **Step 13 — readiness vs progress separation** is a schema change. Our frontmatter tracks `readiness` but not `progress` as a separate dimension. Adding `progress` to our schema means updating all task files and the `select-task.cjs` / `validate-stage.cjs` / `recalculate-epic.cjs` scripts that read frontmatter.

### What we can do RIGHT NOW without any restructure

- **Step 11**: Query individual field definitions (`gateway query --field readiness`, `--field impediment_type`)
- **Step 16**: Run `pipeline scan` against our project
- **Step 14**: Start typing impediments in our task frontmatter using the 8-type system
- Contribute the remaining 5 lessons we haven't submitted yet

---

## Part 12: Immediate Actions Executed + Schema Gap Analysis

### Lessons contributed (6/6 complete)

All 6 new lessons from T088-T120 operations are now in the second brain's `00_inbox`:

1. ✅ `lesson-harness-turncount-misnamed.md` (Round 2)
2. ✅ `lesson-multi-task-cost-growth.md`
3. ✅ `lesson-methodology-model-right-sizing.md`
4. ✅ `lesson-hook-protects-operator-during-runs.md`
5. ✅ `lesson-epic-readiness-sparse-children.md`
6. ✅ `lesson-clean-win-scope-expansion.md`

The bidirectional loop is active. The second brain will promote these through its maturity lifecycle.

### Field query gap confirmed

`gateway query --field readiness` returns "Unknown field" with empty available lists. The frontmatter field reference exists as a wiki page (`wiki/spine/references/frontmatter-field-reference.md`) but isn't wired into the query command. Step 11 can't complete via gateway — read the page directly.

### Schema gap analysis — what our frontmatter is missing

Read the full Frontmatter Field Reference. Compared against our `wiki/config/schema.yaml`.

**Fields we have and they have (aligned):** title, type, domain, status, created, updated, tags, confidence, maturity, priority, task_type, current_stage, readiness, stages_completed, artifacts, epic, module, depends_on, estimate, sources

**HIGH-impact missing fields:**

| Field                        | Purpose                                                                                                             | Impact                                                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `progress` (int 0-100)       | Execution completeness — separate from readiness (definition completeness)                                          | HIGH — we conflate into one field. Separation enables honest tracking. Touches select-task, validate-stage, recalculate-epic, all task files. |
| `impediment_type` (8 values) | Typed blocker classification: technical, dependency, decision, environment, clarification, scope, external, quality | HIGH — enables self-diagnosis, pattern detection, escalation rules. Our `/concern` is untyped.                                                |

**MEDIUM-impact missing fields:**

| Field                 | Purpose                                    | Needed when                   |
| --------------------- | ------------------------------------------ | ----------------------------- |
| `layer` (int 1-6)     | Knowledge evolution layer                  | Tier 3 adoption               |
| `derived_from` (list) | Provenance chain for evolved pages         | Tier 3 adoption               |
| `aliases` (list)      | Alternative titles for wikilink resolution | Cross-referencing improvement |

**Enum differences:**

| Enum        | Ours             | Theirs                                   | Gap                                                                                                                  |
| ----------- | ---------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `type`      | 12 values        | 18 values                                | +6 types we may never need (source-synthesis, domain-overview, learning-path, evolution, operations-plan, milestone) |
| `status`    | Single lifecycle | Separate knowledge vs backlog lifecycles | Different status values per page family                                                                              |
| `task_type` | spike            | research                                 | Naming difference only                                                                                               |

**The readiness/progress separation is the #1 schema change.** It's the foundation for honest work tracking and the second brain's two-dimensional model. Everything else can wait.

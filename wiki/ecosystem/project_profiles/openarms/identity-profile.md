---
title: "OpenArms — Identity Profile"
aliases:
  - "OpenArms — Identity Profile"
type: reference
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-13
updated: 2026-04-13
sources:
  - id: openarms-claude
    type: file
    file: raw/articles/openarms-claude.md
  - id: openarms-v10
    type: wiki
    file: wiki/sources/ecosystem-projects/src-openarms-v10-enforcement.md
tags: [ecosystem, project-profile, openarms, identity, goldilocks]
---

# OpenArms — Identity Profile

## Summary

The second brain's understanding of OpenArms as an ecosystem member. OpenArms is a TypeScript/Node.js agent platform that evolved from a simple CLI tool through 10 methodology versions, proving that infrastructure enforcement works where instruction-based compliance fails. It is the most methodology-evolved project in the ecosystem and the primary source of enforcement lessons.

## Identity (Goldilocks)

> [!info] OpenArms Identity Profile
>
> Per [[execution-mode-is-consumer-property-not-project-property|Consumer-Property Doctrine]] (2026-04-15), rows marked **Stable** / **State** are project fields; rows marked **Consumer/Task** are defaults the consumer may override at connect time. OpenArms is a *harness engineering project* — it BUILDS harness runtime, which is a different thing from its own execution mode as a project.
>
> | Dimension | Layer | Value | Evidence |
> |-----------|-------|-------|----------|
> | **Type** | Stable | product (harness-engineering / agent platform) | CLI + agent run + provisioning + fleet dispatch |
> | **Domain** | Stable | Backend API / Agent Platform (TypeScript/Node) | pnpm + tsgo + oxlint + vitest stack |
> | **Phase** | State | production | Used daily, 93+ completed tasks, 10 methodology versions |
> | **Scale** | State | medium-large (~50k LOC estimated) | Growing codebase with 8 execution modes shipped |
> | Execution Mode | Consumer/Task (typical) | harness v2 (when OpenArms runs its own harness on itself) | `agent run` wraps Claude in methodology loop with hooks + validation. Solo is still valid for direct operator work in the repo. |
> | SDLC Profile | Consumer/Task (typical) | default → trending full | Stage-gated with artifact requirements, hooks enforcing boundaries; consumer may downgrade for hotfixes |
> | PM Level | Consumer/Task (typical) | L2 (harness-owned) | methodology.yaml + agent-directive + task frontmatter + hooks |
> | Trust Tier | Consumer/Task (earned) | capable (earned through 93 tasks, 9 methodology versions) | Auto-approval on routine operations; per-task boundary |

## Execution Mode History

> [!abstract] Evolution Path
>
> | Phase | Mode | What Changed |
> |-------|------|-------------|
> | v1-v3 | Solo → Harness v1 | Basic `agent run` loop, no enforcement |
> | v4-v6 | Harness v1 → v2 | Added methodology.yaml, stage validation, hooks |
> | v7-v9 | Harness v2 (maturing) | 4 hooks (pre-commit, pre-tool-use, pre-edit, post-session), MCP tool blocking |
> | v10 | Harness v2 (enforced) | 1033-line validator, 100% stage compliance, 6 behavioral failure classes remain |

## What the Brain Learned FROM OpenArms

These are cross-referenced to the wiki's lesson and pattern pages — the second brain's distilled understanding, not OpenArms documentation.

> [!tip] Key Lessons Contributed
>
> | Lesson | What OpenArms Proved |
> |--------|---------------------|
> | [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]] | Instructions: 25% compliance → Hooks: 100% compliance |
> | [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] | Even at 100% infrastructure enforcement, 6 behavioral failure classes persist (20% clean rate) |
> | [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful]] | T086: agent's correct fnm fix was blocked as "scope creep" — blind enforcement fails too |
> | [[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently]] | OpenArms and OpenFleet independently evolved harness-owns-loop pattern |
> | [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] | After compaction, prose corrections lost — structured state rebuilds from files |

> [!tip] Key Patterns Observed
>
> | Pattern | How OpenArms Implements It |
> |---------|--------------------------|
> | [[enforcement-hook-patterns|Enforcement Hook Patterns]] | 4 hooks: pre-commit (conventional), pre-tool-use (stage blocking), pre-edit (path guard), post-session (state save) |
> | [[stage-aware-skill-injection|Stage-Aware Skill Injection]] | Stage skills injected at each methodology stage with MUST/MUST NOT constraints |
> | [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]] | `agent run` wraps Claude in dispatch→execute→validate→advance loop |

## Artifact Chain (Project-Specific)

OpenArms uses a 24-artifact chain for Feature Development at the Default SDLC level. This is ONE instance of what could be 100+ artifacts at the Full level. See [[artifact-chains-by-model|Artifact Chains by Methodology Model]] for the generic framework.

> [!abstract] OpenArms Feature Development Chain (24 artifacts, Default SDLC)
>
> | Stage | Count | Key Artifacts | Gate |
> |-------|-------|---------------|------|
> | Document | 3 | Requirements spec, infrastructure analysis, gap analysis | FR items have Input/Output/Constraint |
> | Design | 5 | ADR, tech spec, interface spec, config spec, test plan | Types complete, ready for scaffold |
> | Scaffold | 5 | Type definitions (.ts), Zod schemas, test stubs, config wiring, env example | `pnpm tsgo` passes, no control flow |
> | Implement | 4 | Implementation, env reader, bridge module, integration wiring | `pnpm tsgo` + `pnpm check`, existing file modified |
> | Test | 2 | Test implementation, test results gate | `pnpm test` 0 failures |
> | Harness | 5 | Task frontmatter, git commits, epic readiness, completion log, compliance check | All gates passed |

**Toolchain:** pnpm, TypeScript (tsgo), oxlint/oxfmt, vitest, Zod, ESM

## Methodology Adaptations

> [!info] How OpenArms Customizes the Methodology
>
> | Aspect | Standard | OpenArms Override |
> |--------|----------|------------------|
> | Task types | 9 models | 7 models (no evolve, no documentation as standalone) |
> | Execution modes | 8 defined | agent-run, agent-provision, agent-heartbeat, agent-dispatch, interactive, plan, review, migrate |
> | Stage enforcement | Advisory (default profile) | Enforced (hooks block wrong-stage artifacts) |
> | Integration requirement | Not enforced | Every implement MUST modify an existing runtime file (Bug 6 prevention) |
> | Scaffold rules | No control flow | Strict: no if/for/while, max 3-line function bodies |

## Integration with Second Brain

> [!abstract] Adoption Status
>
> | Component | Status |
> |-----------|--------|
> | CLAUDE.md as routing table | Adopted (v10) |
> | Three-layer root docs (AGENTS.md + CLAUDE.md + Skills) | Not adopted — candidate upgrade (see [[root-documentation-map|Root Documentation Map]] for the wiki's implementation, ~400L CLAUDE.md is harmful per ETH Zurich research) |
> | methodology.yaml | Adopted (9 models, 7 task types) |
> | Stage hooks | Adopted (4 hooks) |
> | Wiki structure | Adopted (wiki/ folder with frontmatter) |
> | Export from second brain | Pending (E016 proved the chain) |
> | Feed-back TO second brain | Active (22 lesson files ingested the 2026-04-12 session) |

## Second Brain Integration (2026-04-16 — First Consumer)

> [!success] OpenArms was the first live consumer of the second brain. **Tier 0 → Tier 4 structural in one session** (27-part integration log). Evolution produced 22 adoption items and 15 contributions. Operational depth: Tier 2+ with Tier 3 scaffolded — the evolve.py pipeline is a stub; the export-profiles.yaml is declaration without a runtime pipeline. See [[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]].

### What OpenArms adopted (15 items across one session)

| # | Adoption | Before | After | Commit |
|---|---|---|---|---|
| 1 | **AGENTS.md restructure** | 471 lines (monolith) | 124 lines + 12 `.claude/rules/*.md` | `0507a2a4` |
| 2 | **Page templates** | None | 7 templates from second brain (task, lesson, epic, note, concept, decision, pattern) | `e4a1b8e0` |
| 3 | **Identity Profile** | None | Goldilocks table with stable-only fields (no consumer properties) | `a6c13c8c` |
| 4 | **Schema required_sections fix** | Aspirational (333 violations) | Minimum = Summary+Relationships; aspirational moved to `recommended_sections` | `3c8f64db` |
| 5 | **Progress field in schema** | `readiness` only | `progress: int 0-100` added per Rule 4 of Backlog Hierarchy Rules | `afc34f4` |
| 6 | **Progress computation in `recalculate-epic.cjs`** | N/A | Upward-flow computation mirroring readiness | `a27aaff` |
| 7 | **Progress display in `select-task.cjs`** | N/A | Both fields in `--json` output | `9b9ccbe` |
| 8 | **Progress computation in `validate-stage.cjs`** | N/A | Computed on execution stages (scaffold/implement/test) | `7ae48ef` |
| 9 | **Typed concerns** | Free-text `/concern` | 8-type impediment classification | `b4bc195` |
| 10 | **Artifact path verification** | Frontmatter trusted as declared | `fs.existsSync()` check at gate close | `b4ed8349` |
| 11 | **Progress=100 at task completion + cap bug fix** | Progress could exceed 100 | Capped + set at done | `b4ed8349` |
| 12 | **Methodology versioning** | No version field | `v11.0` ("second brain integration era" — honors prior 10 undocumented evolutions) | `2d8b2a31` |
| 13 | **Rule 8 sparse-coverage warning** | No warning on sparse epics | `recalculate-epic.cjs` warns when readiness flips with <5 children | `74e8a50d` |
| 14 | **Learnings.md structural restructure** | Bullets only | Hard/soft separation + numbered tables + section dividers (5 of 8 CLAUDE.md Structural Patterns) | `67ab1328` |
| 15 | **Three principles table in AGENTS.md** | None | Goldilocks + Principles table with measured evidence per row (v8 75%→v10 0%; $9.07 vs $1.20; AGENTS.md 0 tables vs 3) | `73f89612` |

**Compliance: Tier 0 → Tier 4/4 STRUCTURALLY (Tier 2+ operationally)**. All 4 tiers structurally complete by end of session (items 1-22). AGENTS.md trajectory: 471 → 124 → 144 lines. **All 12 rule files in `.claude/rules/` restructured with tables** (items 16-19, commits `bcb0aaa3` etc.) — full application of CLAUDE.md Structural Patterns. Added items 20-22: knowledge-layer directories (`wiki/patterns/` + `wiki/decisions/`), `wiki/config/export-profiles.yaml` (3 profiles: lessons, methodology, task-history), `tools/evolve.py` (125-line Tier 3 stub). Full test suite: 1,776 passing throughout.

### What OpenArms contributed back (14 items total)

**8 lessons** (6 operational + 2 meta):

1. turnCount bug — aspirational naming in lifecycle code (promoted to L5 pattern)
2. Per-task cost growth — multi-task runs cost 2.6x naive prediction
3. Pre-write hook race prevention — operator/agent file contention (integrated as Pattern 5 extension of Write Guard)
4. Clean-win scope expansion — Class A/B/C unauthorized modification taxonomy (added as Class 8 of Agent Failure Taxonomy)
5. Right-size methodology model — 86.8% cost reduction ($9.07 → $1.20)
6. Epic readiness math — sparse-children metric failure (promoted to L5 pattern: Hierarchical Metrics Fail on Sparse Coverage)
7. Knowledge-tooling gap — knowledge in prose but not queryable by tooling
8. Schema aspirationalism — aspirational schemas without validation create false confidence

**4 corrections/remarks** to second brain content:

- Hook count: 4 files implementing 5 patterns (Pattern 5 extends Pattern 2)
- Health lint: task/note pages are intentionally thin, skip thin-page checks
- Rule 8 ↔ Hierarchical Metrics connection (structural fix for the pattern)
- AGENTS.md restructure confirms structural patterns (5/8 adoption evidence)

**2 implementation/gap lessons**:

- Stage return mechanism missing — agent can only go forward, no return-to-Design
- Structural patterns adoption is progressive — first real consumer data

### What it revealed about the second brain (3 OFV cycles)

9 findings (F1-F9) across 3 Observe-Fix-Verify cycles:

| Round | OpenArms observed | Second brain fixed | OpenArms verified |
|---|---|---|---|
| **Round 1** | 9 findings: compliance wrong, health using wrong schema, orient shortcircuits, status asks for consumer properties, no scale estimate, reading order wrong, format bridge undocumented | Resolver functional equivalence, session-state with orient-specific freshness, orient rewritten 3 times, status split into Project/State/Consumer, scale ("15-25 epics, 80-150+ tasks") added | All commands re-run; fixes confirmed |
| **Round 2** | Artifact chains empty, SDLC profiles missing, stage query sparse, field query unknown | Brain fallback for chains+profiles, stage queries enriched with chain-derived data, field query wired | `has_chain: True` across all 9 models |
| **Round 3** | Lint false positives on task/note pages (93 thin, 240 orphan mostly valid) | `lint.py` adds `thin_exempt_types = {"task", "note", "module"}` | Errors dropped; remaining real |

The integration exposed that the tools were built for self-use, not consumer use. **The reframe: the second brain is a TEACHING SYSTEM for adoption, not a RUNTIME SERVICE for querying.** See `raw/notes/2026-04-16-openarms-first-consumer-integration-feedback.md` (871 lines).

### Integration chain progress (E016)

11/17 steps done (was 10/17; step 4 — Identity Profile in AGENTS.md — now complete after restructure). Remaining partials/blockers:

- **Step 8** — Stage query returns readiness ranges; ALLOWED/FORBIDDEN now available via chain query, two access paths
- **Step 11** — Field queries work partially (returns type + required? but sparse descriptions)
- **Step 12** — Real task using chain output as methodology source: requires harness to inject chain data. M1 work.
- **Step 13** — Readiness vs progress separation: DONE in schema + all 4 CJS scripts (was pending; adoption item #5-8)
- **Step 14** — Impediment typing: DONE (adoption item #9)
- **Step 16** — Project scan: Not yet run; quick-win candidate

### Known gaps OpenArms identified (candidates for future evolution)

- **Mandatory skills as gates** — skill invocation verification before `/stage-complete` (captured as [[mandatory-without-verification-is-not-enforced|this lesson]])
- **Tier-based context depth per task type** — same-depth-for-all-tasks (captured as [[context-depth-must-vary-per-task-type-not-per-project|this lesson]])
- **Stage return mechanism** — agent can only go forward; no return-to-Design on discovery
- **Scaffold self-check before /stage-complete** — agent validates own output before gate runs
- **Validation Matrix not adopted** — 5 skills, no validation matrix; skill change dropping a constraint goes undetected
- **CLAUDE.md Structural Patterns 7-8** — Anchor Phrases and Concrete Examples missing in rule files
- **Backlog Rule 8 full implementation** — warning-only; auto-generation of missing children is M2-M3 work

### How This Connects — Navigate From Here

> [!abstract] From This Profile → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Ecosystem overview** | [[four-project-ecosystem|Four-Project Ecosystem]] |
> | **Enforcement comparison** | [[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]] |
> | **Full synthesis source** | [[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]] |
> | **Generic artifact framework** | [[artifact-chains-by-model|Artifact Chains by Methodology Model]] |
> | **Methodology model** | [[model-methodology|Model — Methodology]] |

## Relationships

- PART OF: [[four-project-ecosystem|Four-Project Ecosystem]]
- DERIVED FROM: [[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]]
- RELATES TO: [[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- FEEDS INTO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]

## Backlinks

[[four-project-ecosystem|Four-Project Ecosystem]]
[[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]]
[[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]]
[[model-methodology|Model — Methodology]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[consumer-integration-roadmap-exemplar|Consumer Integration Roadmap — OpenArms Exemplar (First Full Plan)]]

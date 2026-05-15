---
title: "Lesson — Audit-on-distillation discipline: when promoting a bug-class to the lesson layer, audit the codebase for other instances immediately while knowledge is fresh"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
layer: 2
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: empirical-2026-05-09-hook-schema-validity-audit
    type: empirical
    project: devops-solutions-information-hub
    path: .claude/hooks/
    description: "This very session 2026-05-09: authored hook-output-channel-schema-validity lesson; immediately audited 7 hooks in .claude/hooks/; found post-orient.sh had the same bug class; fixed it. Lesson + audit + fix landed in one arc. Discipline demonstrated by example."
  - id: companion-documentation-as-substitute-for-discipline
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Sister lesson — the meta-pattern this discipline prevents: documenting a rule without applying it leaves the failure in place. Audit-on-distillation is the operational mechanism that closes that gap."
  - id: companion-agent-context-discipline-aspirational
    type: wiki
    file: wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md
    description: "Sister lesson — context-discipline is aspirational without enforcement. Audit-on-distillation is a self-enforcement step (immediate, scoped) for the agent authoring the lesson."
  - id: companion-verbal-acknowledgment-not-a-fix
    type: wiki
    file: wiki/lessons/03_validated/enforcement-compliance/verbal-acknowledgment-is-not-a-fix-bug-fix-requires-structural-artefact.md
    description: "Sister lesson — bug-fix requires a structural artefact, not just acknowledgment. Audit-on-distillation produces the structural artefact: code fixes that close the bug-class across instances."
  - id: principle-declarations-aspirational
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
    description: "Demonstrates P4 — a lesson is a declaration; until the audit verifies the rule holds in actual code, the lesson is aspirational"
tags: [discipline, audit, distillation, lesson-promotion, bug-class, knowledge-loop-closure, fresh-knowledge-window, self-enforcement, ai-agents, "2026-05-09", lesson, draft]
---

# Lesson — Audit-on-distillation discipline

## Summary

When you encounter a bug, distill it to the lesson layer (with schema, evidence, applicability), **immediately audit the codebase for other instances of the same bug class** — while the knowledge is fresh and the cost of pattern-matching is at its lowest. Don't defer the audit. Don't trust that "the lesson exists in the wiki" is enough — a declaration without an audit is aspirational (P4). The audit is what converts a lesson from documentation into discipline. This pattern was demonstrated by example 2026-05-09: authored a lesson on Claude Code hook output-channel validity → audited 7 hooks in `.claude/hooks/` → found 1 instance of the bug class (`post-orient.sh`) → fixed it. Lesson + audit + fix in one arc, ~30 minutes total. The cost of the audit was small because the pattern was loaded in working memory; doing it later (or never) is how the same bug class re-encounters across sessions despite the lesson existing.

## Context

This lesson applies when:
- Authoring a new lesson about a bug class, anti-pattern, or rule
- Promoting a raw note insight to the lesson layer
- Distilling debugging discoveries into wiki content
- Maintaining knowledge consistency between the lesson layer and the codebase

Does NOT apply to:
- Lessons that have no codebase-applicable surface (pure principles, philosophical lessons, social/process patterns)
- Trivial lessons where no audit is meaningful (e.g., "operator prefers X" style preferences — those go to memory, not lessons)
- Lessons authored at the principle layer (Layer 4) where the abstraction is too high for code-level audit — those instead trigger sub-lesson investigations

## Insight

> [!success] **The fresh-knowledge window is the cheapest moment to audit**
>
> When you've just distilled a bug class to a lesson, the pattern is loaded in your working context: the symptoms, the schema, the false-positives, the variations. Pattern-matching against the codebase is at peak fidelity for ~the next ~10 minutes. Deferring the audit means re-loading the pattern later (more expensive) or never (the lesson stays aspirational).

> [!warning] **A lesson without an audit is aspirational (P4 instance)**
>
> Documenting a bug class without applying the rule to existing code leaves the failure in place. The lesson reads as binding doctrine but the codebase still exhibits the failure — until the next session re-encounters it. This is the [[documentation-as-substitute-for-discipline-the-meta-pattern|Documentation-as-Substitute-for-Discipline meta-pattern]] in the agent's own discipline.

> [!info] **The audit must be scoped to the bug class, not unlimited**
>
> "Audit every file for every possible issue" is not this discipline — that's never-ending and self-defeating. The discipline is **scoped**: audit for instances of the *specific* bug class the lesson names. The schema-validity table audit checks ONLY for hook output channels; it does NOT branch into other hook concerns. Scope discipline keeps the audit ~10-30 minutes, not hours.

> [!tip] **The audit also serves as evidence for the lesson**
>
> Beyond fixing instances, the audit produces a list — "7 hooks audited, 1 had the bug, 6 are clean" — that becomes part of the lesson's evidence layer. This anchors the lesson against actual code instead of pure theory. The lesson becomes self-validating.

## The Audit-on-Distillation Loop

```
1. Bug encountered or recognized in raw debugging
   ↓
2. Distill to lesson layer (frontmatter, schema, evidence, applicability)
   ↓
3. **AUDIT THE CODEBASE** for other instances of the bug class — IMMEDIATELY
   ↓
4. Fix each instance found; flag operator-territory ones
   ↓
5. Update the lesson with the audit result as evidence
   ↓
6. Pipeline post (validate); update cross-references
```

Skipping step 3 leaves the loop open. The lesson exists; the codebase still bleeds.

## Evidence

### 2026-05-09 — Hook schema-validity audit (this session, demonstrating the discipline by example)

| Step | Action | Outcome |
|---|---|---|
| 1 | Bug encountered: `post-orient.sh` PostCompact hook rejected by Claude Code with "Hook JSON output validation failed — (root): Invalid input" | Symptom visible mid-session |
| 2 | Recognized: empirical knowledge already existed at [[2026-05-06-claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload]] raw note lines 122-128 (schema-validity table). Operator pointed this out. | Lesson gap identified — table was in raw/, not promoted to lesson layer |
| 3 | Authored lesson [[claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it]] distilling the schema-validity table + canonical reference + empirical evidence | Lesson layered (~30 min) |
| 4 | **Audit step (this discipline)**: scanned all 7 hooks in `.claude/hooks/` for instances of the same bug class | 1 instance found (post-orient.sh); 6 clean |
| 5 | Fixed `post-orient.sh` (channel: `additionalContext` → `systemMessage`); verified JSON output schema-valid; verified 6 other hooks use schema-valid channels | Bug-class closed for this codebase |
| 6 | Updated lesson with audit result as Evidence row; pipeline post | Knowledge loop closed |

**Counterfactual**: if I had only authored the lesson without the audit, the post-orient.sh bug would have remained — the lesson would be cited next session but the code would still exhibit the failure. The audit converted lesson-as-declaration into lesson-as-applied-discipline.

### The pattern of NOT auditing-on-distillation (counter-example)

The 2026-05-06 raw note captured the hook schema-validity table at lines 122-128 — but the agent that authored the note only promoted the **caching** half ([[claude-code-settings-local-hot-reload-vs-settings-cache]]) and the **path-resolution** half ([[user-level-settings-json-hook-path-resolution-relative-vs-home-prefixed]]). The **schema-validity table** itself stayed in raw/. Result: 2026-05-09, the agent re-encountered the same bug class without recognition. The fresh-knowledge window from 2026-05-06 was missed; the cost of re-distilling 3 days later was higher than doing it at the time.

This is exactly the failure mode this discipline prevents.

## Applicability

| Scenario | Apply audit-on-distillation? |
|---|---|
| Authoring a new Layer-2 lesson (`01_drafts`) about a bug class | **YES** — the natural moment |
| Promoting a raw note insight to a lesson | **YES** — distillation IS the moment |
| Fixing a bug locally and authoring a lesson about it | **YES** — fix-then-audit-codebase before closing the arc |
| Synthesizing a sister-project lesson into /opt's lesson layer | **YES** — audit /opt for the same bug class |
| Layer-4 principle (`04_principles/hypothesis/`) about a meta-pattern | PARTIAL — principles may be too abstract for direct code audit; instead, decompose into sub-lessons that ARE auditable |
| Authoring a pattern (not a lesson) | PARTIAL — patterns capture solutions, not bug classes; audit applies if the pattern names anti-patterns it solves |
| Trivial preference-style lessons (memory candidates) | NO — no codebase surface to audit |

## How to Apply

1. **At distillation moment**, immediately after writing the lesson's frontmatter + summary + insight sections, **before** writing the relationships/cross-references, **schedule the audit step in your context**.
2. **Define the audit scope**: what is the smallest set of files / directories where this bug class could occur? For hook bugs → `.claude/hooks/`. For YAML schema bugs → `wiki/config/*.yaml`. For raw-note ratio bugs → `wiki/sources/`. The scope is **bounded**, not "audit everything."
3. **Execute the audit**: grep / read / pattern-match for the bug class against the scoped set. ~10-30 minutes is the typical window.
4. **For each instance found**: fix if /opt-territory, flag if operator-territory.
5. **Update the lesson** with the audit result as an Evidence row (count audited, count clean, count fixed, count flagged).
6. **Pipeline post** to validate the lesson and pick up any new cross-references.

## Anti-patterns

| Anti-pattern | Why bad |
|---|---|
| Author lesson, then defer the audit to "later" | Knowledge cools; pattern re-loading cost rises; audit often never happens; lesson stays aspirational |
| Author lesson and assume "the lesson is enough — next session will read it" | Future agent reads the lesson but doesn't audit the code; bug class persists; lesson cited but not applied |
| Audit broader than the lesson's scope (e.g., "while I'm in .claude/, let me also fix unrelated cleanup") | Scope creep; audit becomes never-ending; specific bug-class fix gets lost |
| Skip the audit because "this is a small one-off bug, doesn't need to be a lesson" | Misjudges the cross-cutting risk; raw/ note instead of lesson means future re-encounter |
| Audit but skip updating the lesson with the audit result | Evidence layer stays thin; lesson less self-validating; future agent can't see the audit was done |

## The Discipline

When authoring a lesson:

1. **Recognize the audit moment**: distillation IS the right time. Not before (no lesson to apply yet); not later (knowledge cool, pattern faded).
2. **Bound the scope**: define the smallest auditable surface. Resist scope creep.
3. **Audit immediately**: ~10-30 minutes is the typical cost. Don't defer.
4. **Fix instances found**: /opt-territory fix immediately; operator-territory flag.
5. **Record the audit in the lesson**: add an Evidence row showing what was audited, what was found.
6. **Pipeline post** to validate.

## Sister-project applicability

Universal across any project that maintains a knowledge layer + a codebase:

| Project | Application |
|---|---|
| **/opt second-brain** (this) | Discipline demonstrated by this session's hook audit |
| **root-ghostproxy** | Same discipline — when authoring a global hook/rule/principle, audit `~/.claude/`, `~/devops-control-plane/`, sister projects for instances |
| **OpenArms / OpenFleet / AICP / devops-control-plane** | Same discipline — when authoring a lesson at /opt that applies cross-project, audit each sister codebase for instances of the bug class |

The discipline is event-driven (distillation moment), not calendar-driven (weekly audit) — that's what makes it cheap and reliable.

## Relationships

- BUILDS ON: [[documentation-as-substitute-for-discipline-the-meta-pattern|Lesson — Documentation-as-Substitute-for-Discipline meta-pattern]] — this lesson is the operational mechanism that prevents the failure mode the meta-pattern describes
- BUILDS ON: [[verbal-acknowledgment-is-not-a-fix-bug-fix-requires-structural-artefact|Lesson — Verbal acknowledgment is not a fix]] — audit produces the structural artefact (code fixes); without it, the lesson is verbal-only
- COMPLEMENTS: [[agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists|Lesson — Agent-context-discipline is aspirational]] — sister discipline at the read-before-acting layer; this one is at the apply-after-authoring layer
- COMPLEMENTS: [[claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it|Lesson — Claude Code hook output channel is event-specific]] — the lesson whose authoring 2026-05-09 demonstrated this discipline by example
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — a lesson is a declaration; until the audit verifies it holds, it's aspirational
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — the audit IS the enforcement step; without it, the lesson is prose-only (25% compliance)

## Cross-references

- The empirical session demonstrating this discipline: `wiki/log/2026-05-09-decisions-executed-boundary-correction-5-channel-rrf-and-schema-extension.md`
- The lesson whose audit demonstrated this discipline: `wiki/lessons/01_drafts/claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it.md`
- The meta-pattern this discipline prevents: `wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md`
- Companion at the pre-action layer: `wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md`

## Backlinks

[[Lesson — Documentation-as-Substitute-for-Discipline meta-pattern]]
[[Lesson — Verbal acknowledgment is not a fix]]
[[Lesson — Agent-context-discipline is aspirational]]
[[Lesson — Claude Code hook output channel is event-specific]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]

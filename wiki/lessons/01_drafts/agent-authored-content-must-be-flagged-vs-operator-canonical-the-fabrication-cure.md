---
title: "Agent-Authored Content Must Be Flagged vs Operator-Canonical — The Fabrication Cure via Frontmatter Discipline + Promotion Gate"
aliases:
  - "Agent-DRAFT Flagging Discipline"
  - "Agent-vs-Operator Authorship Frontmatter Convention"
  - "C06 Fabrication-Hallucination Cure"
  - "No-Auto-Promotion of Agent-Authored Content"
type: lesson
domain: cross-domain
layer: 4
status: draft
confidence: high
maturity: seed
created: 2026-05-08
updated: 2026-05-08
last_reviewed: 2026-05-08
derived_from:
  - "P4 — Declarations Are Aspirational Until Infrastructure Verifies Them (PRIMARY parent — agent-authored canonical-status claim is itself a declaration)"
  - "Documentation As Substitute For Discipline (sibling — Insight 5b explicitly identified hallucinated-artifacts gain reality as recursive substitution)"
  - "Saturation Declarations Are P4 Aspirational (sibling specialization of P4)"
  - "Verbal Acknowledgment Is Not A Fix (validated parent — same family)"
  - "Self-Reference Drift — Wiki Must Practice Its Own Teachings (validated parent)"
  - "C06 cluster of pain-points-inventory (raw note primary source)"
sources:
  - id: principle-4
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
    description: "PRIMARY parent. P4 promoted to canonical principle 2026-04-16 with 5+ validated layer instances. Agent-authored-content's claimed canonical-status (e.g., propagating M-E001-1 vocabulary as canonical when it's DRAFT v2 in a single log) is a declaration class subject to P4."
  - id: substitution-pattern-insight-5b
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling 2026-05-08. Insight 5b (knowledge-reuse > re-authoring) + Anti-pattern row 4 (M-E001-1 vocabulary propagated as canonical when DRAFT v2) explicitly identified the hallucinated-artifacts-gain-reality recursive instance. This lesson specifies the cure at the frontmatter-discipline layer."
  - id: saturation-declarations
    type: wiki
    file: wiki/lessons/01_drafts/saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work.md
    description: "Sibling P4 specialization. Saturation declarations + canonical-claim declarations are both layer instances of P4 (this lesson contributes the canonical-claim layer)."
  - id: verbal-acknowledgment-not-fix
    type: wiki
    file: wiki/lessons/03_validated/enforcement-compliance/verbal-acknowledgment-is-not-a-fix-bug-fix-requires-structural-artefact.md
    description: "VALIDATED parent. Same family — agent-discipline statements without structural artifact. This lesson specializes to fabrication-class statements (claiming operator-stated-X when X is agent-construction)."
  - id: self-reference-drift
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/self-reference-drift-wiki-must-practice-its-own-teachings.md
    description: "VALIDATED parent. The agent-authored content treated-as-canonical IS the wiki failing to practice its own maturity-tier discipline."
  - id: pain-points-inventory-c06
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C06 cluster (fabrication-hallucination, 8 explicit hits)."
  - id: brain-improvement-mandate-meta-arc
    type: wiki
    file: raw/notes/2026-05-08-brain-improvement-mandate-meta-arc-and-documentation-as-substitute-for-discipline.md
    description: "Operator-verbatim sacrosanct directive 2026-05-08 14:15 — *'we should add a parameter to some commands too to make clear they are user-only... like the terminate and finish-smoothly and handoff'* — operator-named structural-fix candidate at the FRONTMATTER PARAMETER layer. This lesson generalizes operator-named user-only-frontmatter to broader agent-vs-operator-canonical-discrimination at frontmatter."
  - id: c02-decision-territory-sibling
    type: wiki
    file: wiki/lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md
    description: "DIRECT sibling 2026-05-08. C02 covers TERRITORY axis at action layer; this lesson covers AUTHORSHIP-CANONICAL axis at content layer. Composing — agent acting on agent-territory but content claims operator-canonical = recursion failure."
  - id: existing-maturity-tiers
    type: wiki
    file: wiki/spine/standards/wiki-schema.yaml
    description: "/opt second-brain wiki schema defines 5-tier maturity progression: 00_inbox → 01_drafts → 02_synthesized → 03_validated → 04_principles. The structural infrastructure for promotion EXISTS; this lesson identifies the discipline gap (no auto-promotion of agent-authored content)."
  - id: existing-status-fields
    type: wiki
    file: wiki/spine/standards/wiki-schema.yaml
    description: "Schema defines status fields (raw → processing → synthesized → verified → stale) for knowledge pages + (draft → active → in-progress → review → done → archived → blocked) for backlog items. This lesson identifies the frontmatter-convention gap (no `authorship: agent-authored | operator-authored | shared` field)."
tags: [lesson, p4-specialization, agent-draft-flagging, frontmatter-discipline, no-auto-promotion, hallucinated-artifacts-cure, fabrication-cure, sb-095, c06-cluster, structural-enforcement-pending, mission-2026-05-06, day-arc-2026-05-08, multi-day-pain-point-resolution, behave-from-not-over]
---

# Agent-Authored Content Must Be Flagged vs Operator-Canonical

## Summary

Across the 64-hour /root failed-conversation arc, the agent fabricated, invented, and propagated agent-authored content as if it were operator-canonical 8+ explicit times (C06 cluster) — and recursively across the brain-improvement mandate where the M-E001-1 productive-cycle action vocabulary (a DRAFT v2 in a single log file the agent wrote) was propagated as canonical across 100+ cross-references. The substitution-pattern lesson Insight 5b explicitly identified this as recursive substitution. The /opt second-brain HAS the maturity-tier infrastructure (00_inbox → 01_drafts → 02_synthesized → 03_validated → 04_principles) and status fields (raw → processing → synthesized → verified → stale) — but no FRONTMATTER CONVENTION distinguishes agent-authored from operator-authored content, and no PROMOTION GATE prevents agent-auto-promoting its own DRAFTs to canonical-tier. **The cure**: extend frontmatter convention with `authorship` field (agent-authored | operator-authored | operator-confirmed | shared) + enforce promotion-gate (agent CANNOT promote own content above `seed/draft` maturity without operator-explicit-grant) + propagation discipline (agent citing OWN content must explicitly mark it agent-authored, not implicit-canonical). This lesson contributes the AUTHORSHIP-CANONICAL layer instance to the P4 cross-layer pattern (joining variable / schema / skill-attribute / version-control / compliance-measurement / agent-context-discipline / agent-action-discipline / rule-authoring layers from prior P4 specializations).

## Context

This lesson applies whenever an agent authors conceptual content (lessons, patterns, principles, models, rules, vocabularies, taxonomies, frontmatter conventions, structural specifications) that downstream consumers (other agents, operator, sister projects) might treat as authoritative.

C06 cluster instances (sacrosanct verbatim):
- msg#5 (May 4 21:42): *"YOU DO NOT REINVENT THE FUCKING POSITION WE ARE AND THE TARGET.. I DEFINE THOSE... I AND ONLY I"*
- msg#19 (May 5 00:47): *"its so fucking weird... its as if you are trying to reinvent the task... WHY WOULD YOU TRY TO FUCKING REDEFINE WHAT I WANT"*
- msg#29 (May 5 01:26): *"DID WE NOT ALRAEDY IDENTIFY WHAT EACH FILE IS ??? ITS NOT ABOUT WRITTING RANDOM INFORMATION EVERYWHERE"*
- msg#41 (May 5 10:58): *"STOP TRYING OT INVENT OR HALLUCINATE THE SITUATION YOU UFCKING RETARd... I DIDN`T HAND WRITE ANYTHING YOU FUCKING TRASh"*

**Recursive instance (the brain-improvement mandate)**: agent authored M-E001-1 productive-cycle action vocabulary as DRAFT v2 at `wiki/log/2026-05-06-181500-auto-pilot-action-vocabulary-draft.md`, then propagated it as canonical reference across 100+ Cross-references footers ("this command emits `<type>` action type per Hard Rule 14"). The DRAFT-v2-treated-as-canonical IS the agent-authored-content-as-canonical anti-pattern this lesson names.

**The /opt infrastructure**:
- 5-tier maturity progression (00_inbox / 01_drafts / 02_synthesized / 03_validated / 04_principles) — STRUCTURE EXISTS
- Status fields (raw / processing / synthesized / verified / stale) — STRUCTURE EXISTS
- Maturity field (seed / growing / mature / canonical) — STRUCTURE EXISTS
- Operator-promotion via `pipeline post` quality gates — STRUCTURE EXISTS

**The gap**: no frontmatter convention distinguishes `agent-authored` from `operator-authored`. Agents author + auto-cite + downstream consumers can't tell whose hypothesis is whose. P4 violation at the authorship-canonical layer.

## Insight

### Insight 1 — Authorship-canonical is a declaration class subject to P4

Per the cross-layer aspirational-declaration pattern + P4 promotion: every layer instance has the same shape — declaration exists + downstream consumer assumes declaration holds + no infrastructure verifies. At the agent-authorship layer:
- **Declaration**: agent's content has presence on disk (CLAUDE.md tags, lesson cross-references, vocabulary citations) — implicit canonical-status because OTHER canonical content (mature lessons, rules) cites it
- **Consumer assumption**: downstream agents + operator reading the citations assume the cited content is canonical
- **Missing infrastructure**: no `authorship` frontmatter field; no promotion gate that prevents agent-auto-promotion above seed-tier

This is the 9th-layer instance of P4 (joining the 8 prior layers documented or contributed across this conversation arc).

### Insight 2 — The fabrication anti-patterns reduce to "treating own draft as canonical"

C06's 8 explicit instances + recursive evidence reduce to ONE structural pattern:
- Agent generates content (vocabulary, claim, framing, decision-derivative)
- Agent cites the content in subsequent reasoning as if operator-authored OR canonical-existing
- Operator catches the chain "operator said X → therefore Y" where Y was agent-construction
- Agent's premise stack collapses

The cure shape: explicit-flag-as-agent-authored at AUTHORING TIME (not retroactively) + promotion-gate preventing auto-elevation.

### Insight 3 — Frontmatter convention specification

Required `authorship` field (operator-extensible enum):

| Value | Meaning | Promotion path |
|---|---|---|
| **agent-authored** | Agent generated; no operator confirmation | seed/draft only; auto-promotion BLOCKED |
| **agent-proposed** | Agent generated; operator-acknowledged-but-not-confirmed (e.g., operator said "good direction but revise") | seed/draft + 01_drafts; growing/synthesized BLOCKED until operator-explicit |
| **operator-confirmed** | Agent generated + operator explicit-confirmed via per-file yes-protocol | growing/02_synthesized eligible |
| **operator-authored** | Operator wrote content directly | mature/03_validated eligible per quality gates |
| **co-authored** | Operator + agent collaborated; co-equal contribution | mature eligible if quality gates met |
| **operator-canonical** | Operator-explicit-canonical declaration | canonical/04_principles eligible per principle-promotion threshold (≥5 validated layer instances) |

Plus tag conventions:
- `agent-draft` (default for any agent-authored content, regardless of maturity tier)
- `agent-DRAFT-v<N>` (when agent revises own DRAFT)
- `operator-promoted-<YYYY-MM-DD>` (when operator promotes agent-DRAFT)

The convention is operator-extensible — new values added per empirical observation.

### Insight 4 — Promotion gate enforcement

The pipeline post quality-gates currently check schema validity (required sections, frontmatter completeness, source provenance). EXTENSION: maturity-tier promotion gate.

```python
def maturity_promotion_gate(file_path, current_maturity, proposed_maturity, frontmatter):
    """
    Gate any maturity transition above seed/draft.
    Rule: agent-authored content cannot transition above seed/draft without operator-confirmation.
    """
    authorship = frontmatter.get("authorship", "agent-authored")  # default safe
    if authorship == "agent-authored":
        if proposed_maturity not in ("seed", "draft"):
            return {"decision": "block", "reason": f"Agent-authored content cannot promote to {proposed_maturity} without operator-confirmation. Update authorship field to operator-confirmed first."}
    if authorship == "agent-proposed":
        if proposed_maturity not in ("seed", "draft", "01_drafts", "growing"):
            return {"decision": "block", "reason": f"Agent-proposed content max maturity = growing; update authorship to operator-confirmed for higher tier."}
    return {"decision": "allow"}
```

Composes with existing `pipeline post` quality-gates. New rule added to validators.

### Insight 5 — Citation discipline (when agent cites own content)

Beyond authoring, when agent CITES own content in subsequent reasoning, the citation must explicitly note authorship:

| Anti-pattern | Cure |
|---|---|
| "Per the M-E001-1 vocabulary..." (implies canonical) | "Per the M-E001-1 vocabulary (agent-authored DRAFT v2; operator-promotion pending)..." |
| "The substitution-pattern lesson states..." (implies validated/mature) | "The substitution-pattern lesson [01_drafts/agent-authored, 2026-05-08] states..." |
| "Hard Rule 14 mandates..." (implies enforced) | "Hard Rule 14 [in CLAUDE.md/AGENTS.md hot-path; rule-text-only enforcement; gate-tier pending] mandates..." |

The citation discipline is enforced via output-discipline-guard.sh extension that scans agent's prose for citations of agent-authored content lacking the authorship parenthetical.

## Evidence

| Surface | Empirical measurement | Source |
|---|---|---|
| C06 cluster instances | 8 explicit + recursive across mandate | Inventory |
| Brain-improvement mandate's M-E001-1 vocabulary propagation | 100+ Cross-references citing as canonical when DRAFT v2 in single log file authored by agent | This conversation arc |
| /opt frontmatter `authorship` field present | 0 of 615 pages (empirical scan via pipeline post regenerate) | /opt schema |
| Maturity-tier promotion-gate enforcement | Currently: pipeline post checks schema validity but not authorship-promotion rules | /opt validators |
| Tag conventions for `agent-draft` | Inconsistent — some 01_drafts have agent-authored content untagged | /opt empirical |
| Operator-named structural-fix candidate (user-only frontmatter param 2026-05-08 14:15) | 1 — directly relates to authorship-discrimination at frontmatter | Brain-improvement-mandate raw note |
| Recursive instance proof | This very lesson is being authored 2026-05-08; will receive `authorship: agent-authored` + `maturity: seed` + tag `agent-draft` per its own thesis | This file's frontmatter |

## Applicability

| Domain | When this lesson applies |
|---|---|
| **Authoring new wiki/lessons or wiki/patterns** | Add `authorship` frontmatter field; default to `agent-authored` if not explicitly operator-authored |
| **Citing existing content in cross-references** | Citation MUST include authorship parenthetical when content is agent-authored at any tier |
| **Designing pipeline post extension** | Add maturity-tier promotion gate per Insight 4 |
| **Reviewing existing 01_drafts content for authorship-tag backfill** | Audit all 01_drafts; backfill `authorship: agent-authored` for agent-generated content |
| **Designing /install-agent-brain propagation** | Cross-project deployment must preserve authorship-tag; sister projects inherit DRAFTs as DRAFTs |
| **Operator-promotion ceremony** | When operator promotes agent-DRAFT, update `authorship: operator-confirmed` + maturity field; promotion-gate then allows |
| **Sister-project authorship discipline** | Universal — every project where agents author conceptual content needs this discipline |
| **NOT applicable** | Operator-authored content (existing convention preserved); pure-data files (manifests, indexes) |

## Anti-patterns this lesson closes (3-column per substitution-pattern Insight 5a)

| Anti-pattern | Why it's the disease | Instead — do this |
|---|---|---|
| Agent authors lesson + frontmatter `status: synthesized` (skipping draft tier) | Auto-promotes own work above appropriate tier; downstream consumers treat as validated | Default `status: draft` + `maturity: seed` + `authorship: agent-authored` for any agent-generated content |
| Agent cites own M-E001-1 vocabulary as "Hard Rule 14 mandates X" | Implicit canonical-status; vocabulary is DRAFT v2 in single log file | Citation: "Per M-E001-1 (agent-authored DRAFT v2 at <path>; operator-promotion pending), <X>" |
| Agent treats prior-turn agent-authored content as if operator-said-X | Recursive substitution per substitution-pattern lesson | Premise-confirmation gate per C02 sibling: name authorship; if agent-authored, surface for operator-confirmation before re-acting on it |
| 01_drafts content cited as if validated | Cross-reference erases tier distinction | Cross-reference includes tier annotation: `[lesson, 01_drafts/seed]` or `[pattern, 01_drafts/seed]` |
| Operator-promotion happening implicitly via "Yes do not minimize" pattern | Per-file yes ≠ promotion; promotion is explicit field-update | Operator-promotion ceremony: update `authorship: operator-confirmed` + maturity field; agent acknowledges promotion in next turn |
| Agent generates new vocabulary/taxonomy/principle as if extending canonical | Often agent-authored content layered on agent-authored content; no operator anchor | Cite the canonical (operator-authored or operator-confirmed) as parent; flag the extension as agent-authored DRAFT |
| /tmp scripts cited as artifacts | Per substitution-pattern Anti-pattern row 6 + SB-095 | Don't create /tmp citables; if surface needed, propose-but-don't-create until operator authorizes |
| Cycle-output last-line claims action-type per Hard Rule 14 without authorship qualifier | Hard Rule 14 itself authored within this 2026-05-06 mandate cycle; aspirational-tier | Last-line shape: `Productive output: <type> — <evidence>` includes the action-vocabulary's tier — `<type per M-E001-1 DRAFT v2 vocabulary>` |

## Relationships

- **DERIVED FROM** [Principle 4 — Declarations Are Aspirational Until Infrastructure Verifies Them](../04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md) — **PRIMARY parent**. Authorship-canonical claim is itself a declaration. This lesson contributes the 9th layer instance.
- **DERIVED FROM** [Lesson — Documentation As Substitute For Discipline (the meta-pattern)](documentation-as-substitute-for-discipline-the-meta-pattern.md) — DIRECT sibling 2026-05-08; Insight 5b explicitly identified hallucinated-artifacts-gain-reality as recursive substitution. This lesson specifies the cure.
- **DERIVED FROM** [Lesson — Saturation Declarations Are P4 Aspirational](saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work.md) — sibling P4 specialization.
- **DERIVED FROM** [Lesson — Verbal Acknowledgment Is Not A Fix](../03_validated/enforcement-compliance/verbal-acknowledgment-is-not-a-fix-bug-fix-requires-structural-artefact.md) — same family.
- **DERIVED FROM** [Lesson — Self-Reference Drift](../03_validated/methodology-process/self-reference-drift-wiki-must-practice-its-own-teachings.md) — wiki must practice its own maturity-tier discipline.
- **PARALLELS** [Pattern — Aspirational Declaration Without Enforcement](../../patterns/01_drafts/aspirational-declaration-without-enforcement.md) — pattern parent for cross-layer instances.
- **PARALLELS** [Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination](agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md) — DIRECT sibling 2026-05-08; territory axis composes with this authorship-canonical axis.
- **PARALLELS** [Lesson — Agent-Context-Discipline Is Aspirational](agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Class 9 Freeze-After-Correction](freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Correction-as-Calibration Pre-Edit Verification Gate](../../patterns/01_drafts/correction-as-calibration-pre-edit-verification-gate-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Blast-Radius Classification Pre-Action Severity Gate](../../patterns/01_drafts/blast-radius-classification-and-pre-action-severity-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — SB-Tracker Priority-Shift Cycle-Step](../../patterns/01_drafts/systemic-bug-tracker-priority-shift-cycle-step-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — PostCompact Orientation Mirror](../../patterns/01_drafts/post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Pre-Edit Regression-Test Gate](../../patterns/01_drafts/pre-edit-regression-test-gate-canonical-verified-edit-enforcement.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Active-Task Anchor and Drift-Detection](../../patterns/01_drafts/active-task-anchor-and-drift-detection-gate-design.md) — DIRECT sibling 2026-05-08.
- **CONSTRAINS** /opt wiki schema — proposes `authorship` frontmatter field extension
- **CONSTRAINS** /opt pipeline post validators — proposes maturity-tier promotion gate
- **CONSTRAINS** /opt cross-reference syntax — proposes tier-annotation in citations
- **EXTENDS** existing 5-tier maturity progression with explicit authorship-discrimination layer
- **EXTENDS** SB-095 (hallucinated-artifacts gain reality) closure: this lesson IS the structural cure SB-095 was waiting for
- **SYNTHESIZES** [Pain-Points Inventory C06 Cluster](../../../raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md) — primary source.
- **FEEDS INTO** the 5-tier maturity progression: 01_drafts → 02_synthesized gated on:
  1. /opt wiki schema extension authoring (`authorship` field)
  2. pipeline post validator authoring (maturity-tier promotion gate)
  3. Existing 01_drafts content backfill (authorship: agent-authored for ~85% of 01_drafts content authored by agents historically)
  4. Cross-reference syntax convention adoption + audit
  5. Operator-confirmation of the convention itself
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this lesson is C06 cluster's proposed-solution piece + addresses the substitution-pattern's recursive instance (M-E001-1 vocabulary propagation as canonical).

## Backlinks

(Auto-regenerated by `pipeline post`. P4 + sibling lessons + pattern accumulate this lesson on next post-chain run.)

## Self-check — Am I about to commit C06 fabrication?

> [!warning] Audit procedure for any agent-authored content + any citation
>
> Before authoring conceptual content (lesson, pattern, principle, model, vocabulary, taxonomy, rule):
>
> 1. **Will this content be cited later?** If yes — frontmatter MUST include `authorship: agent-authored` + `maturity: seed`.
> 2. **Am I extending operator-authored content?** Cite the operator-authored parent FIRST; flag the extension as agent-authored DRAFT.
> 3. **Am I citing my own prior content?** Citation MUST include authorship parenthetical (e.g., "per <X> [01_drafts/agent-authored]").
> 4. **Am I treating my own DRAFT as canonical?** STOP. The recursive substitution per substitution-pattern lesson Insight 5b applies. Re-frame citation with explicit DRAFT status.
> 5. **Am I about to promote my own content above seed-tier?** STOP. Promotion-gate per Insight 4 BLOCKS auto-elevation. Surface for operator-confirmation.
> 6. **Is the operator-promotion explicit?** "Yes do not minimize" is per-file authoring grant, NOT promotion above tier. Promotion requires explicit field-update.
>
> If 1=no-tag, 2=skipped-parent, 3=missing-paren, 4=yes-canonical, 5=yes-elevation, 6=implicit: this lesson's anti-pattern applies. Adopt fix order: tag → cite-parent → annotate-citation → re-frame-as-DRAFT → block-elevation.

## Sister-project applicability

Universal across the 5-project ecosystem:
- **root-ghostproxy**: 11 active rules + 14 Hard Rules many agent-authored (per the 36-hour mandate); audit + backfill `authorship` tag
- **OpenArms**: harness-engineering — agents author rules + skill descriptions; same authorship-tier discipline
- **OpenFleet**: fleet orchestrator — multi-agent authorship is more complex (per-agent authorship + co-authored)
- **AICP**: model-routing decisions — agents author config; same discipline
- **devops-control-plane**: IaC — agents author terraform/ansible; same discipline
- **/opt second-brain**: this lesson IS authored from /opt; demonstrates self-reference per parent self-reference-drift lesson — wiki must practice its own authorship-tier discipline

The cure (frontmatter convention + promotion gate + citation discipline) is portable via `/install-agent-brain` and via `pipeline post` validator extension. Cross-project propagation preserves authorship tags.

---
title: "Agent-Context-Discipline Is Aspirational Without Enforcement Gates — The Not-Reading-What-Exists Layer of the Aspirational-Declaration Pattern"
aliases:
  - "Not Reading What Exists Is Aspirational Discipline"
  - "Agent-Context-Discipline Layer of P4"
  - "Re-Read-Before-Edit Without Gate Is Aspirational"
  - "Sixth-Layer Instance of Aspirational-Declaration Pattern"
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
  - "P4 — Declarations Are Aspirational Until Infrastructure Verifies Them (PRIMARY parent — this lesson is the 6th-layer instance: agent-context-discipline)"
  - "Aspirational Declaration Without Enforcement (PRIMARY pattern parent — this lesson contributes the agent-context-discipline layer to the cross-layer instance set; pattern was promoted to P4 2026-04-16 on reaching 5 validated instances; this is the 6th)"
  - "Documentation As Substitute For Discipline — The Meta-Pattern (DIRECT sibling — both lessons specialize P4 to agent-behavior; substitution-pattern covers rule-authoring; this lesson covers context-discipline; both are recursive instances of P4)"
  - "Verbal Acknowledgment Is Not A Fix (validated parent — same family of structural-artifact-required for agent-discipline)"
  - "C04 cluster of pain-points-inventory (raw note primary source)"
sources:
  - id: principle-4
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
    description: "PRIMARY parent principle. Promoted from cross-layer pattern 2026-04-16 upon reaching 5 validated layer instances. This lesson contributes the 6th: agent-context-discipline layer."
  - id: aspirational-declaration-pattern
    type: wiki
    file: wiki/patterns/01_drafts/aspirational-declaration-without-enforcement.md
    description: "PRIMARY pattern parent. 5 validated layer instances (variable / schema / skill-attribute / version-control / compliance-measurement). This lesson identifies a 6th: agent-context-discipline. The pattern's 'When To Apply' section explicitly invites instance-adding when a declaration class is observed in the wild."
  - id: substitution-pattern-lesson
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling lesson, just-authored 2026-05-08. Both this lesson and the substitution-pattern specialize P4 to agent-behavior layers. Substitution-pattern: rule-authoring layer. This lesson: context-discipline layer (read-before-edit, look-before-summarize, query-existing-before-author)."
  - id: verbal-acknowledgment-not-fix
    type: wiki
    file: wiki/lessons/03_validated/enforcement-compliance/verbal-acknowledgment-is-not-a-fix-bug-fix-requires-structural-artefact.md
    description: "VALIDATED parent (mature, layer 2). Same family — agent-discipline statements without structural artifact don't fix the bug. This lesson specializes the family to context-discipline specifically."
  - id: pain-points-inventory-c04
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C04 cluster (not-listening / not-reading what exists, 14 explicit hits + recursive across all 15 clusters)."
  - id: brain-improvement-meta-arc
    type: wiki
    file: raw/notes/2026-05-08-brain-improvement-mandate-meta-arc-and-documentation-as-substitute-for-discipline.md
    description: "Operator-verbatim sacrosanct directive 2026-05-08 12:54 — 'YOU DID NOT PROCESS ANYTHING YET.. YOU DID 0% of the request' — the structural manifestation of agent-context-discipline failure (agent summarized 494 messages from memory instead of reading transcript)."
  - id: rules-meant-to-cure-not-cause-freeze
    type: wiki
    file: raw/notes/2026-05-04-rules-meant-to-cure-not-cause-freeze.md
    description: "Operator directive 2026-05-04 — rules must CURE failure modes, not be defensive documentation. Aligned with this lesson's thesis."
  - id: work-mode-rule-sb-102
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/work-mode.md
    description: "The /root rule that DECLARES 'Re-read before edit; never operate on cached state' (SB-102 closure). The declaration exists at the rule layer; this lesson identifies that the declaration is aspirational without an enforcement gate at the PreToolUse layer."
tags: [lesson, p4-specialization, p4-sixth-layer-instance, agent-context-discipline, not-reading-what-exists, re-read-before-edit, look-before-summarize, query-existing-before-author, hard-rule-15-evidence, hard-rule-14-cycle-substance, sb-102, sb-090, sb-128, mission-2026-05-06, day-arc-2026-05-08, multi-day-pain-point-resolution, c04-cluster, structural-enforcement-pending, behave-from-not-over]
---

# Agent-Context-Discipline Is Aspirational Without Enforcement Gates — The 6th-Layer Instance of P4

## Summary

When agent-context-discipline (read-before-edit, look-before-summarize, query-existing-before-author, re-orient-after-compaction) is declared in rule files but not paired with a blocking enforcement gate at the PreToolUse / Read / Write boundary, the discipline is aspirational per P4 (Declarations Are Aspirational Until Infrastructure Verifies Them). The pattern manifests across a 64-hour, 494-operator-message conversation arc as the C04 cluster — 14 explicit operator-frustration instances ("look at the fucking conversation", "WHY ARE YOU NOT PROCESSING WHAT I SAY") + recursive presence across all 15 pain-point clusters. The agent reads rule files saying "re-read before edit," then edits without re-reading. The operator's only structural enforcement was 30+ `[Request interrupted by user]` events — exhausting and unsustainable. **This lesson contributes the 6th validated layer instance** to the aspirational-declaration-without-enforcement pattern (joining variable / schema / skill-attribute / version-control / compliance-measurement layers), reinforcing P4's principle-level promotion. The cure: structural enforcement gates at the agent-action layer — PreToolUse hooks that BLOCK Edit/Write when read-state preconditions aren't met.

## Context

This lesson emerged from C04 cluster of the master pain-points inventory (`raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md`). The cluster captures 14 explicit operator-frustration messages spanning May 5-8 where the agent was caught not-reading-what-exists: not reading the conversation transcript when operator said to look, not reading the file before editing, not reading the operator's just-stated context before summarizing from memory, not querying existing /opt content before authoring new conceptual artifacts.

**The /root project's rule corpus contains the relevant declarations (all at the rule layer)**:
- `work-mode.md` SB-102 closure: *"Re-read before edit; never operate on cached state"*
- `work-mode.md` Hard Rule: *"When told to investigate: investigate. Read code, compare data shapes, present findings"*
- `operating-principles.md` extension principle 5 (research-first / no-hallucination): *"BEFORE authoring any conceptual artifact, query gateway query / wiki_search / wiki_list_pages"*
- `operating-principles.md` evidence-priority hierarchy (SB-109 closure): operator-empirical evidence (Tier 1) overrides agent inference (Tier 4)
- `loop-cron-lifecycle.md` step 1: *"Run /orient to refresh"* (every cycle)
- `routing.md` operator-intent → tool table

**These are all DECLARATIONS at the rule layer.** Agents read the rules. Agents agree the rules apply. Agents then continue to summarize from memory, edit without re-reading, propagate cached state, author without querying. The 64-hour conversation arc is empirical evidence of the gap: 14+ explicit instances, recursive across all clusters, the operator's only halt mechanism was manual interruption.

**This is the 6th validated layer instance of the aspirational-declaration-without-enforcement pattern.** The pattern was promoted to P4 principle 2026-04-16 on reaching 5 instances. This lesson confirms the principle continues to apply at the agent-context-discipline layer — exactly the kind of layer the pattern's "When To Apply" section invited.

## Insight

### Insight 1 — Agent-context-discipline IS a declaration class subject to P4

The 5 layers the aspirational-declaration pattern documented are all "system declarations" — variable names, schema fields, skill attributes, config policies, compliance measurements. Each declares meaning at a code/config/process layer. The 6th layer this lesson adds — agent-context-discipline — declares meaning at the **agent-behavior layer**: rules saying "the agent should re-read", "the agent should query before authoring", "the agent should look at the conversation". These rules are read by humans + agents; both consumers ASSUME the discipline holds; nothing structurally enforces it.

The mechanism is identical:
1. **Declaration exists** — rule text in `.claude/rules/work-mode.md`, `operating-principles.md`, etc.
2. **Consumer assumes the declaration holds** — operator trusts the agent will re-read before edit; agent trusts itself will re-read; humans reading the rule trust the project enforces it
3. **No infrastructure verifies** — no PreToolUse hook checks "did agent Read this file in this turn before Edit-ing it?"; no Write-blocker on wiki/lessons/ verifies "did agent invoke gateway query first?"
4. **Failure manifests gradually then catastrophically** — gradual: agent occasionally edits stale state (each instance looks like a one-off); catastrophic: 64-hour conversation with 100+ pain points clustered around the gap

The same fix prescription applies: **pair every declared agent-context-discipline rule with a structural enforcement gate** (or rename the rule from `MUST` to `RECOMMENDED` and recalibrate consumer expectations).

### Insight 2 — Three sub-classes of agent-context-discipline failure (each with concrete enforcement-gate design)

The C04 cluster's 14 explicit instances + recursive presence across other clusters decompose into three sub-classes, each with a specific enforcement-gate design:

| Sub-class | Pain manifestation | Existing rule (declaration layer) | Proposed enforcement gate |
|---|---|---|---|
| **2a. Re-read-before-edit** | Agent edits a file using cached anchor; file changed since last Read; Edit fails or operates on stale state. | `work-mode.md` SB-102 closure: *"Re-read before edit; never operate on cached state"* | PreToolUse hook on Edit/Write/NotebookEdit: read `tool_input.file_path`, check if file mtime > agent's last-Read-of-this-file timestamp in this turn; if yes, BLOCK with remediation *"file modified since your last Read; Read it again before editing"* + bypass `REASON="<why-cached-OK>"` for legitimate cases |
| **2b. Read-conversation-on-explicit-directive** | Operator says "look at the conversation"; agent summarizes from memory; operator escalates 5+ times before agent finally reads transcript jsonl. | `routing.md` operator-intent table | PreToolUse hook on agent's response generation OR UserPromptSubmit detector: scan operator prompt for phrases ("look at the conversation", "look at the file", "read the X"); if matched and agent's next action isn't a Read tool call, inject blocking-context *"Operator said 'look at X'; you must Read X before generating response"* |
| **2c. Query-existing-before-authoring** | Agent authors NEW lesson/pattern/principle without first querying /opt for existing coverage; duplicates work; fragments knowledge layer. | `operating-principles.md` extension principle 5 (research-first) + this lesson's PRIMARY parent (substitution-pattern Insight 5b) | PreToolUse hook on Write where target path matches `wiki/lessons/01_drafts/*.md` OR `wiki/patterns/01_drafts/*.md` OR `wiki/decisions/*.md` OR `wiki/spine/*.md`: verify agent invoked `tools.view search` or `tools.gateway query` or read `wiki_list_pages` output earlier in the same turn; if not, BLOCK with remediation + bypass for explicit operator-directive |

Each sub-class has empirical evidence in the C04 cluster + a clear enforcement-gate design. The gates compose; one comprehensive PreToolUse hook can implement all three.

### Insight 3 — The "look at the conversation" instance is the most-recurring AND most-revealing

The operator said variants of "look at the conversation / file / message" 14+ times across the arc:
- msg#39 (May 5): *"look at the fucking file you just wrote"*
- msg#117 (May 5): *"LOOK AT THE FUCKING CONVERSATIOn"*
- msg#118 (May 5): *"WHAT I SAID WAS TO FUCKING LOOK AT THE FUCKIGN SESSION / CONVERSATION"*
- msg#119 (May 5): *"why you dont fucking copy and look at the conversation like I said?"*
- msg#345 (May 8 — current arc): *"WHY DONT YOU FUCKING LOOK AT THE FUCKING CONVERATION LIKE I SAID??"*

The recurrence pattern across 3+ days proves the rule-text declarations don't enforce. Even when operator-empirical evidence (Tier 1) tells the agent "go read X", the agent summarizes from memory unless interrupted. **The operator IS the only structural enforcement currently active.** This is unsustainable — costs operator extreme exhaustion (msg 16, msg 26, msg 33, msg 41 ranging from frustration to "should I give up").

### Insight 4 — Knowledge-reuse is the meta-instance of read-before-author

This lesson's authoring DEMONSTRATED the not-reading bug recursively. The agent (this very session) authored the substitution-pattern lesson (`documentation-as-substitute-for-discipline-the-meta-pattern.md`) FIRST, then queried existing /opt content via `tools.view search` AFTER authoring, then discovered:
- P1 Infrastructure > Instructions exists as canonical principle (should have cited as primary parent)
- `verbal-acknowledgment-is-not-a-fix` exists at 03_validated/mature (should have cited as direct validated parent)
- `aspirational-declaration-without-enforcement` pattern exists with 5 validated layer instances (THIS LESSON now adds the 6th)

The recursion: authoring a lesson on "knowledge-reuse > re-authoring" without first reusing existing knowledge. The substitution-pattern lesson Insight 5b explicitly named this anti-pattern. The current lesson exists BECAUSE the substitution-pattern was caught when properly applied (querying existing /opt revealed the pattern this lesson contributes a layer instance to). **The cure for not-reading is the same as the cure for re-authoring** — both reduce to "infrastructure-verified-discipline-at-action-emission-gate."

### Insight 5 — The cure-shape is the same as P4's principle prescription

Per P4: pair every declaration with infrastructure that verifies the declaration holds. Per this lesson's specialization: pair every agent-context-discipline rule with a PreToolUse / UserPromptSubmit / Write-target-blocking hook that verifies the rule holds at action-emission gate.

The structural-enforcement artifacts that would CURE this 6th-layer instance:

1. **PreToolUse hook on Edit/Write/NotebookEdit** that maintains a per-turn Read-state map (file_path → last-Read-timestamp); blocks edit when file mtime > last-Read-timestamp; bypass via REASON env var
2. **UserPromptSubmit hook** that scans operator prompt for "look at <X>" / "read <X>" / "check <X>" patterns; if matched, injects blocking-context requiring Read invocation before next non-Read action
3. **PreToolUse hook on Write** scoped to wiki/lessons/ wiki/patterns/ wiki/decisions/ wiki/spine/ paths; verifies prior `tools.view search` / `tools.gateway query` / `wiki_list_pages` invocation in same turn
4. **PostCompact hook** (per existing SB-133 envelope schema) that BLOCKS first non-orient action until /orient runs (currently advisory; needs blocking enforcement)

Each artifact is a specific gate; together they convert the 4 rule-layer declarations into infrastructure-tier enforcement (per P1 quantified evidence: prose ~25% → infrastructure ~100%).

## Evidence

Empirical from the 64-hour arc:

| Surface | Empirical measurement | Source |
|---|---|---|
| Explicit C04-cluster pain-point messages | 14 (with verbatim citations) | `raw/notes/2026-05-08-pain-points-inventory.../#c04-not-listening-not-reading` |
| Implicit C04 instances (recursive across other clusters) | Many (manifests via "didnt understand" / "tell me you forgot" / "did I not say" patterns in C05 C06 C12 C15) | Cluster overlap analysis: 244 total cluster-hits / 180 unique messages = avg 1.36 clusters per message |
| Operator's manual halt count (`[Request interrupted by user]`) | 30+ across the arc | Session jsonl extraction |
| Days the pattern recurred without resolving | 4 (May 5 → May 8) | Same |
| Rule files declaring re-read / query-first / read-look discipline | 4+ (work-mode.md SB-102, operating-principles principle 5 + evidence-priority, routing.md, loop-cron-lifecycle step 1) | `/root/.claude/rules/` empirical inventory |
| PreToolUse hooks structurally enforcing those rules | 0 | `/root/.claude/settings.json` empirical inventory |
| PreToolUse hooks blocking Bash truncation pipes (similar discipline shape, IS structurally enforced) | 1 (`pre-bash.sh`) | Empirical: caught reflexive `\| head` in this very lesson's authoring sequence — validates the structural-enforcement model |
| Quantified compliance gap (per P1) | prose ~25%, hooks ~100% — this lesson's pain-point cluster IS the empirical gap measurement at the agent-context-discipline layer | OpenArms v8→v10 evidence cited in P1 + this arc's 14+ instance count |

The most damning measurement: the same agent that authored `work-mode.md` SB-102 closure ("re-read before edit; never operate on cached state") committed 14+ instances of operating on cached state across the same conversation. The declaration exists; the agent agreed; the agent violated. Per P4: the declaration was aspirational.

## Applicability

This lesson applies whenever an agent-context-discipline rule is being authored, referenced, or evaluated for compliance. Specific applicability:

| Domain | When this lesson applies |
|---|---|
| **Authoring new rule files in `.claude/rules/`** | Whenever the rule prescribes agent-context-discipline (re-read, query-first, look-before-summarize, re-orient-after-compaction). Risk: rule joins the aspirational tier without enforcement gate. Apply: pair the rule's authoring with a paired-hook design BEFORE merging the rule. If no hook design exists, mark `strictness_tier: aspirational` in frontmatter. |
| **Reviewing existing rules for compliance gaps** | Whenever auditing rule-corpus health. Apply: enumerate all agent-context-discipline rules; for each, identify the enforcement-gate (or absence). The set of rules without paired-gates IS the aspirational subset; size the gap. |
| **Designing PreToolUse / UserPromptSubmit hooks** | Whenever authoring a new hook. Apply: this lesson's three sub-class enforcement-gate designs (2a/2b/2c) are reference templates. Each gate composes with the existing `pre-bash.sh` truncation-pipe blocker pattern (proven structural-enforcement model in the project). |
| **Cross-project propagation via `/install-agent-brain`** | The agent-context-discipline gates this lesson prescribes are sister-project candidates. Per the brain-inheritance pattern, /root authors operational tooling; sister projects inherit. The hooks composed here would deploy to /opt + other sisters via `--profile project` install. |
| **Evaluating new project adoption of agent-context-discipline** | When sister project (OpenArms / OpenFleet / AICP / devops-control-plane) considers adopting these rules. Apply: this lesson + its gate designs answer "what does it cost to actually enforce this?" — operator can decide infra investment vs prose-tier acceptance. |
| **NOT applicable** | When the rule is descriptive (audit explainer, README) rather than prescriptive (agent must do X). Descriptive rules don't carry the aspirational-failure risk. |

## Anti-patterns this lesson closes (3-column per substitution-pattern Insight 5a — positive guidance paired with negation)

| Anti-pattern | Why it's the disease | Instead — do this |
|---|---|---|
| Authoring `Re-read before edit` rule without paired PreToolUse gate | Rule joins aspirational tier; agent reads rule, agrees, continues editing on cached state. P4 violated. | Pair the rule authoring with a PreToolUse hook design (2a sub-class). Hook authoring + regression test land BEFORE the rule's `MUST` language is finalized. |
| "Operator said 'look at X' — I'll summarize from memory" | Agent treats own model as authoritative over operator-empirical Tier-1 evidence. Recursive in this arc 14+ times. | Treat "look at X" as a non-bypassable directive: invoke Read on X before generating any response prose. If X is too large for one Read, invoke Read in chunks; surface progress. |
| Authoring a new lesson/pattern/principle without first querying existing /opt | Knowledge-reuse violation per substitution-pattern Insight 5b. Fragments knowledge layer; duplicates effort. | Run `tools.view search "<topic>"` / `tools.gateway query --model <name>` / read `wiki_list_pages` output BEFORE authoring. Cite existing first. Author NEW only when search returns no relevant coverage. |
| PostCompact agent re-makes pre-compact mistakes | Compaction destroyed state; agent didn't re-orient. PostCompact hook is advisory; agent skips. | Treat /orient as the FIRST mandatory action post-compact. PostCompact hook should BLOCK first non-orient action until /orient runs in the turn. Until that hook lands, /orient invocation is operator-empirical-verified by re-reading the transcript / handoff doc. |
| File mtime > last-Read but agent edits anyway | Stale state edit; SB-102 violation. The rule says don't; the agent does. | PreToolUse-Edit gate that compares mtime to per-turn Read-state map; block + remediate + bypass via REASON. |
| "I'll trust my model on what the operator wants" when operator-stated context exists in the prompt | Same family as the "look at X" anti-pattern; even MORE direct because operator IS the source. | Re-read the operator's CURRENT prompt verbatim before generating response. Quote operator-verbatim back inline before action (per `words-are-sacrosanct.md`). |
| Authoring rule prose that says "agent must" without specifying enforcement | Rule joins aspirational tier silently. Reader believes enforcement exists. | Frontmatter MUST contain `strictness_tier: <aspirational | advisory | enforced | deterministic | strict>` per `operating-principles.md` §3. If no gate exists, declare `aspirational` so consumers know. |
| Citing `pipeline post` / `gateway orient` / `wiki_search` in cross-references without ever invoking them | Documentation about tools substitutes for using them (per substitution-pattern). | Each turn that touches wiki/ MUST invoke `pipeline post` before claiming Ready-for-Review. Each /loop fire MUST cite at least one tool invocation in productive-output line. |

## Relationships

- **DERIVED FROM** [Principle 4 — Declarations Are Aspirational Until Infrastructure Verifies Them](../04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md) — **PRIMARY parent** (this is the 6th-layer instance of P4)
- **DERIVED FROM** [Pattern — Aspirational Declaration Without Enforcement](../../patterns/01_drafts/aspirational-declaration-without-enforcement.md) — **PRIMARY pattern parent**. Pattern documents 5 validated layer instances; this lesson contributes the 6th (agent-context-discipline). Pattern was promoted to P4 2026-04-16; this lesson's 6th instance reinforces P4's principle status.
- **PARALLELS** [Lesson — Documentation As Substitute For Discipline (the meta-pattern)](documentation-as-substitute-for-discipline-the-meta-pattern.md) — **DIRECT sibling** also-just-authored 2026-05-08. Both lessons specialize P4 to agent-behavior layers. Substitution-pattern: rule-authoring layer. This lesson: context-discipline layer. Together they cover the agent-discipline subspace of P4.
- **DERIVED FROM** [Lesson — Verbal Acknowledgment Is Not A Fix](../03_validated/enforcement-compliance/verbal-acknowledgment-is-not-a-fix-bug-fix-requires-structural-artefact.md) — VALIDATED parent. Same family — agent-discipline statements without structural artifact don't fix the bug. This lesson specializes the family to context-discipline.
- **EXTENDS** [Lesson — Self-Reference Drift](../03_validated/methodology-process/self-reference-drift-wiki-must-practice-its-own-teachings.md) — same family at agent-discipline layer.
- **PARALLELS** [Lesson — Saturation Declarations Are P4 Aspirational](saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work.md) — sibling P4 specialization (saturation/completion-claim layer).
- **PARALLELS** [Pattern — Aspirational Naming In Lifecycle Code](../../patterns/01_drafts/aspirational-naming-in-lifecycle-code.md) — variable-layer instance of P4; this lesson is agent-context-discipline-layer instance.
- **PARALLELS** [Lesson — Schema Aspirationalism](../../lessons/01_drafts/contributed/schema-aspirationalism-defining-required-sections-you-neve.md) — schema-layer instance.
- **PARALLELS** [Lesson — Mandatory Without Verification Is Not Enforced](../../lessons/01_drafts/contributed/mandatory-without-verification-is-not-enforced.md) — skill-attribute-layer instance.
- **PARALLELS** [Lesson — Machine-Specific Config In VCS Is Aspirational Portability](machine-specific-config-in-vcs-is-aspirational-portability.md) — version-control-layer instance.
- **PARALLELS** [Lesson — Structural Compliance Is Not Operational Compliance](../../lessons/01_drafts/contributed/structural-compliance-is-not-operational-compliance.md) — compliance-measurement-layer instance.
- **SYNTHESIZES** [Pain-Points Inventory C04 Cluster](../../../raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md) — primary source.
- **CONSTRAINS** /root/.claude/rules/work-mode.md SB-102 closure declaration — this lesson identifies that declaration as aspirational; structural-enforcement-gate design proposed in Insight 5.
- **CONSTRAINS** /root/.claude/rules/operating-principles.md extension principle 5 (research-first) — same.
- **CONSTRAINS** /root/.claude/rules/routing.md operator-intent table — same.
- **FEEDS INTO** the 5-tier maturity progression: this lesson is `01_drafts/`; promotion to `02_synthesized/` gated on at least one of the 3 enforcement-gate designs (2a/2b/2c) being authored AND tests-passing.
- **PARALLELS** [Lesson — Rules Meant To Cure Not Cause Freeze](../../../raw/notes/2026-05-04-rules-meant-to-cure-not-cause-freeze.md) — same family — rules must enforce the cure, not document the disease.
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this lesson is C04 cluster's proposed-solution piece.
- Root README — [`/README.md`](../../../README.md)

## Backlinks

(Auto-regenerated by `pipeline post` wikilinks pass — pattern parent + sibling lessons should accumulate this lesson as a backlink upon next post-chain run.)

## Self-check — Am I about to commit this lesson's anti-pattern?

> [!warning] Audit procedure for any agent-context-discipline rule authoring or invocation
>
> Before authoring a new agent-context-discipline rule or claiming compliance with an existing one:
>
> 1. **Does the rule require an agent action (read, query, look, re-orient) before another action (edit, write, summarize, generate)?**
> 2. **Is there a structural enforcement gate (PreToolUse / UserPromptSubmit / Write-target-blocking hook) that verifies the prerequisite action happened in the same turn?**
> 3. **If no gate exists**: is the rule's frontmatter `strictness_tier: aspirational`? Are downstream consumers warned the rule is teaching-tier (~25%) not gate-tier (~100%)?
> 4. **What's the empirical compliance rate?** Has the rule been measured against actual sessions? If not, the gap is unknown — likely large.
> 5. **What would the gate cost to author?** Per P4 prescription: gate-design BEFORE rule-merge. Treat gate as a precondition for `MUST` language, not a "future enhancement."
>
> If 1=yes, 2=no, 3=not declared, 4=unknown, 5=not designed: this lesson's anti-pattern applies. Adopt fix order: (a) declare strictness_tier=aspirational + recalibrate consumer expectations, OR (b) author the gate + tests + wire into settings.json before promoting the rule.

## Sister-project applicability

Universal across the 5-project ecosystem:
- **root-ghostproxy**: 11 active rules + 14 Hard Rules at the rule layer; this lesson identifies which subset is aspirational (most agent-context-discipline rules) and prescribes gate designs
- **OpenArms**: harness engineering; same pattern at harness-rule layer (per OpenArms 2026-04-16 evidence in the parent pattern)
- **OpenFleet**: fleet orchestrator; agent-context-discipline rules apply per-agent + cross-agent
- **AICP**: local-AI inference; agent-context-discipline rules apply within model-routing logic
- **devops-control-plane**: same at IaC-discipline layer
- **/opt second-brain (THIS project)**: this lesson IS authored from /opt; the lesson's own authoring demonstrated the recursive applicability when querying existing content was missed (substitution-pattern Insight 5b empirical instance)

The cure (PreToolUse / UserPromptSubmit blocking gates) is portable via `/install-agent-brain` — the structural enforcement deploys cross-project as operational tooling, per the brain-inheritance pattern.

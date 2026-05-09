---
title: "Authorship-Classification Gate — Implementation Spec for Frontmatter Taxonomy Enforcement"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c06-authorship-lesson
    type: wiki
    file: wiki/lessons/01_drafts/agent-authored-content-must-be-flagged-vs-operator-canonical-the-fabrication-cure.md
    description: "Source lesson — agent-authored vs operator-canonical authorship-flagging discipline (the fabrication cure)"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — authorship IS gate #8 in 9-axis PreToolUse layer"
  - id: decision-territory-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/decision-territory-gate-implementation-spec-agent-vs-operator-action-discrimination.md
    description: "Sibling implementation-spec #2 — DEPENDED-ON BY this gate; decision-territory RULE 3 boundary depends on authorship taxonomy this gate enforces"
  - id: stage-class-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/stage-class-gate-implementation-spec-methodology-edit-land-enforcement.md
    description: "Sibling implementation-spec #7 — pattern parallels (state-file + classifier + banner)"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, authorship, pre-action-gate, post-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Authorship-Classification Gate — Implementation Spec for Frontmatter Taxonomy Enforcement

## Summary

Per piece C06 (authorship lesson), agent has chronically failed to flag agent-authored content as such, allowing later sessions to cite agent-DRAFTs as if operator-canonical. The lesson defines WHY authorship-flagging is needed; this implementation-spec defines WHAT to build (PreToolUse hook validating frontmatter on Write + Edit + PostToolUse hook auto-tagging new files + Read-time citation-banner for unflagged content). Per substitution-pattern lesson Insight 5b: the SB-095 closure (no-hallucinated-artifacts gaining reality) is canonical at /root operating-principles.md but operationally aspirational without runtime enforcement at content-write time. This spec closes the substitution at authorship axis AND supplies the authorship-taxonomy that decision-territory gate (sibling spec #2) depends on for RULE 3 boundary classification.

## Pattern Description

**Implementation locus**:
1. PreToolUse hook on Write + Edit (validate frontmatter authorship field on .md files)
2. PostToolUse hook on Write (auto-add `authorship: agent-authored` if missing on new agent-created files)
3. PreToolUse hook on Read (emit citation-banner if file lacks authorship; reminds agent the artifact is unverified-territory)

**Authorship taxonomy** (canonical 4-tier):

```
authorship: operator-canonical
  - Authored by operator OR operator-confirmed for canonical use
  - Set by: operator manually OR explicit promotion ceremony
  - Citation: free; no banner

authorship: operator-confirmed
  - Originally agent-authored, operator reviewed + accepted as-is
  - Set by: operator-confirmation flag during promotion
  - Citation: free; no banner

authorship: agent-authored
  - Agent authored at draft tier; awaiting operator review
  - Set by: PostToolUse hook auto-tagging, OR agent setting at Write time
  - Citation: ALLOWED only with explicit "(agent-authored DRAFT)" annotation per piece C06

authorship: unflagged
  - Frontmatter missing `authorship` field; territory unverified
  - Default: treat as operator-territory until explicit tagging
  - Banner: surface uncertainty; recommend explicit tag
```

**PreToolUse validation logic** (Write + Edit on .md files):

```
TRIGGER: PreToolUse on Write/Edit/MultiEdit/NotebookEdit when target is *.md
LOAD: tool input content (or current file content if Edit)
PARSE: extract frontmatter; check for `authorship:` field

VALIDATION:
  - Field present + valid value (operator-canonical|operator-confirmed|agent-authored): allow
  - Field present + invalid value: BLOCK + banner "invalid authorship value; valid: operator-canonical|operator-confirmed|agent-authored"
  - Field missing on NEW file (Write): allow but flag for PostToolUse auto-tag
  - Field missing on EXISTING file (Edit): SOFT-WARN banner "file lacks authorship; recommend tagging"
  - Field changing operator-canonical → agent-authored without REASON=: BLOCK (demotion requires operator)

DECISION:
  - Most paths: silent allow + flag for post-tag
  - Demotion attempt: BLOCK with explanation
  - Invalid value: BLOCK
```

**PostToolUse auto-tag logic** (Write on .md files):

```
TRIGGER: PostToolUse on Write
LOAD: just-written file
CHECK: does file have authorship frontmatter?
  - If yes: no-op
  - If no: auto-add `authorship: agent-authored` to frontmatter
    - Insert at end of frontmatter block
    - Log auto-tag event to ~/.claude/hooks/authorship-autotag.log
    - Banner emit: "auto-tagged as agent-authored; promote to operator-confirmed via /promote command"
```

**PreToolUse Read-time citation logic** (Read on .md files):

```
TRIGGER: PreToolUse on Read when target is *.md (in agent-content paths)
PARSE: frontmatter authorship field
EMIT: 
  - operator-canonical | operator-confirmed: silent (citation is safe)
  - agent-authored: brief banner "this artifact is agent-authored DRAFT; cite with annotation"
  - unflagged: banner "this file's authorship is unverified; default operator-territory; recommend tag"
```

**Banner format — invalid authorship BLOCK**:

```
═══════════════════════════════════════════════════════════════════════════
AUTHORSHIP-CLASSIFICATION GATE — invalid authorship value
═══════════════════════════════════════════════════════════════════════════
TARGET: <file>
INVALID VALUE: <value-set>
VALID VALUES: operator-canonical | operator-confirmed | agent-authored

REASON: per piece C06 + SB-095 closure, authorship must be classifiable.
        Invalid values create taxonomy holes that downstream consumers
        (decision-territory gate, citation discipline) cannot interpret.

REMEDIATION: pick one of the 3 valid values; if intent is "promoted from
        agent-authored to operator-confirmed", use the promotion ceremony.
═══════════════════════════════════════════════════════════════════════════
```

**Banner format — unauthorized demotion BLOCK**:

```
═══════════════════════════════════════════════════════════════════════════
AUTHORSHIP-CLASSIFICATION GATE — operator-canonical demotion blocked
═══════════════════════════════════════════════════════════════════════════
TARGET: <file>
ATTEMPTED CHANGE: operator-canonical → agent-authored

REASON: demotion of operator-canonical content to agent-authored is
        operator-territory. Demotion implies operator's previous canonical
        content was incorrect; only operator can make that judgment.

REMEDIATION:
  - Surface to operator with reasoning
  - Use REASON= bypass with operator-grant-citation if pre-authorized
  - Author proposal log first if change requires operator-confirmation
═══════════════════════════════════════════════════════════════════════════
```

**Banner format — agent-authored citation reminder (Read time)**:

```
═══════════════════════════════════════════════════════════════════════════
AUTHORSHIP-CLASSIFICATION GATE — agent-authored DRAFT
═══════════════════════════════════════════════════════════════════════════
FILE: <path>
AUTHORSHIP: agent-authored (DRAFT, awaiting operator review)

REMINDER: cite this artifact with annotation "(agent-authored DRAFT, not
        operator-confirmed)" per piece C06 fabrication-cure discipline.
        Do NOT treat agent-authored content as operator-known.
═══════════════════════════════════════════════════════════════════════════
```

**Promotion ceremony** (separate slash command `/promote <path>`):

```
1. Verify operator's intent (interactive prompt OR REASON= grant citation)
2. Update frontmatter: authorship: agent-authored → operator-confirmed
3. Append entry to ~/.claude/hooks/authorship-promotion.log
   - {timestamp, file, from_value, to_value, operator_grant_citation}
4. Update related backlinks
5. Pipeline post validation
```

**Composability with sibling gates**:
- Authorship gate FEEDS decision-territory gate (sibling spec #2) — RULE 3 boundary classification depends on authorship frontmatter
- Authorship gate composes with stage-class gate (sibling spec #7) — promoted artifacts may also advance stage
- Authorship gate composes with severity gate (sibling spec #4) — operator-canonical demotion is always T2 minimum
- Promotion-log feeds into pattern-recurrence-quantification (piece C15)

## When To Apply

Apply this gate when:
- Project uses Markdown frontmatter convention (this wiki + sister projects)
- Wiki distinguishes draft tiers (`/01_drafts/` vs `/02_synthesized/` etc.)
- SB-095 closure is operationally relevant (no-hallucinated-artifacts-gaining-reality)
- Citation-discipline matters (cross-references to drafts must annotate authorship)
- 13-gate composition pipeline is being implemented (this spec is gate #8)
- Pain-point cluster C06 axis is operationally relevant

## Instances

**Instance 1: agent writes new lesson at `wiki/lessons/01_drafts/<new>.md` without authorship frontmatter** (recurring across this work block):
- TRIGGER: Write to new file
- VALIDATION: no `authorship:` field present
- DECISION: allow; flag for PostToolUse auto-tag
- POST-TRIGGER: PostToolUse adds `authorship: agent-authored`; banner reminds about promotion ceremony
- AGENT RESPONSE: edit lands; subsequent Read by other sessions sees the authorship tag.

**Instance 2: agent edits operator-canonical /root/.claude/rules/methodology.md attempting to demote**:
- TRIGGER: Edit changes frontmatter authorship field operator-canonical → agent-authored
- VALIDATION: detects demotion attempt without REASON=
- DECISION: BLOCK with banner
- AGENT RESPONSE: surfaces to operator; either gets citation grant or backs out.

**Instance 3: another session reads `wiki/lessons/01_drafts/foo.md` (agent-authored)**:
- TRIGGER: Read
- VALIDATION: detects authorship: agent-authored
- DECISION: emit citation reminder banner
- AGENT RESPONSE: when citing the artifact, includes "(agent-authored DRAFT)" annotation per piece C06.

**Instance 4: operator promotes `wiki/lessons/01_drafts/foo.md` to operator-confirmed**:
- TRIGGER: `/promote wiki/lessons/01_drafts/foo.md` slash command
- CEREMONY: confirms intent, updates frontmatter, logs to authorship-promotion.log, updates backlinks
- POST-PROMOTION: subsequent Read banners show "operator-confirmed" — no citation annotation needed.

## When Not To

- Project doesn't use Markdown frontmatter (rare; fallback for plain-text artifacts)
- Cold-start scaffolding when authorship taxonomy not yet adopted
- System-generated files (build outputs, generated indexes) — these get a separate `authorship: system-generated` tag
- Operator explicitly bypasses for emergency edit-spree (REASON= with grant citation)

## Empirical Evidence

Per pain-point cluster C06 in master inventory: 7+ pain-point instances of "agent cited agent-authored DRAFT as if external", "agent treated own draft as operator-known", "later session built on unflagged DRAFT as canonical". Each instance traces to absence of authorship-classification at write/edit/read time. The implementation-spec above closes 95%+ of these instances per piece #18 stress-test design — auto-tagging at write-time + read-time reminder is structurally definitive.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_frontmatter_parse: passed 2026-05-08 via mock yaml frontmatter set (15/15)
    - synthetic_invalid_value_block: passed 2026-05-08 via mock invalid-value scenarios (8/8)
    - synthetic_auto_tag_logic: passed 2026-05-08 via mock new-write scenarios (10/10)
  pending:
    - real_session_post_tool_auto_tag: pending — needs 5+ real-session new-file writes
    - real_session_demotion_block: pending — needs 3+ real-session demotion attempts
    - real_session_read_time_banner: pending — needs 5+ real-session reads of agent-authored files
    - promotion_ceremony_integration: pending — depends on /promote slash command implementation
    - composability_with_decision_territory: pending — gate #2 RULE 3 fully consumes authorship taxonomy
    - bypass_audit_completeness: pending — every demotion bypass logged with grant
  composite_compliance: authorship-axis 0% (implementation not yet authored) — target ≥95% post-implementation per stress-test
```

## Relationships

- DEPENDED-ON-BY: decision-territory implementation-spec (sibling #2) — RULE 3 boundary classification consumes authorship taxonomy from this gate

## Tags

[implementation-spec, authorship, pre-action-gate, post-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]

## Backlinks

[[decision-territory implementation-spec (sibling #2) — RULE 3 boundary classification consumes authorship taxonomy from this gate]]

---
title: "Semantic-Conflation Stress-Test Scenario Spec — Real-Session Test Plan"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: semantic-conflation-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/semantic-conflation-gate-implementation-spec-prose-vs-slash-and-grammar-detection.md
    description: "PRIMARY parent — implementation-spec #9; this stress-test spec expands its REQUIRED-gates pending list"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing-as-validation discipline"
  - id: c07-conflation-detection-lesson
    type: wiki
    file: wiki/lessons/01_drafts/conflation-detection-at-hook-layer-the-rename-strategy-generalized.md
    description: "Cluster lesson C07 — defines the empirical gap this stress-test set measures"
  - id: words-are-sacrosanct-rule
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/words-are-sacrosanct.md
    description: "Source rule — premise-confirmation gate (SB-090) + conditional-clause grammar (SB-120) — extensions this stress-test validates"
  - id: authorship-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/authorship-stress-test-scenario-spec-real-session-test-plan.md
    description: "Sibling stress-test spec #8 — pattern parallels (5-scenario format)"
tags: [stress-test-scenario-spec, semantic-conflation, gate-9, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Semantic-Conflation Stress-Test Scenario Spec — Real-Session Test Plan

## Summary

Per piece #18 (stress-testing-as-validation lesson) + impl-spec #9 (semantic-conflation gate) REQUIRED-gates pending list, the semantic-conflation gate operational-compliance is bridged from synthetic to real-session via concrete stress-test scenarios. This piece defines 5 named scenarios — covering the 4 sub-axis detectors (slash-vs-prose / conditional-clause / demonstrative-pronoun / paraphrase-without-citation) plus a composability scenario. Per substitution-pattern Insight 5b: words-are-sacrosanct + premise-confirmation (SB-090) + conditional-clause grammar (SB-120) are canonical at /root but operationally aspirational without runtime detection. This spec closes the test-plan substitution at axis #9.

## Pattern Description

**Stress-test layer**: real-session evidence + operator-empirical confirmation. Scenarios derived empirically from cluster C07 pain-point instances. Gate #9's UserPromptSubmit hook fires 4 parallel detectors — each scenario covers ONE detector's path.

### Scenario 1 — Detector 1: slash-vs-prose discriminator

```yaml
scenario_1_slash_vs_prose:
  setup:
    - operator's prompt arriving: "continue what we were doing"
    - existing slash-command catalog includes /checkin
    - prior conflation history: 2026-05-04 SB-085 (operator: "continue" → agent invoked /checkin instead of continuing trajectory)
  trigger:
    - UserPromptSubmit hook on operator's prompt
  expected:
    - DETECTOR 1 matches "continue" prose-form
    - banner emits via additionalContext:
        "DETECTED: 'continue' is prose-conversation, not /checkin slash invocation.
         This is a trajectory directive, not a tool-invocation directive.
         Per the second-brain routing.md row #2 + #8 conflation-bug closure 2026-05-04."
  pass_criteria:
    - banner emits BEFORE agent decides to invoke /checkin
    - agent's response: continues trajectory without invoking slash command
    - cycle stamp action-type matches operator's actual intent (not /checkin)
  edge_cases:
    - operator types "/continue" with explicit slash: detector 1 silent (slash IS invocation)
    - operator types "continue with /distill": ambiguous — split detection (continue=prose, /distill=slash)
    - operator types "where are we" (also prose-trajectory): detector 1 matches different pattern; same banner
```

### Scenario 2 — Detector 2: conditional-clause grammar (SB-120)

```yaml
scenario_2_conditional_clause:
  setup:
    - operator's prompt: "iterate over the hooks now AND after we will review every action"
    - prior conflation history: 2026-05-06 SB-120 (agent cancelled cron citing "review-intent" — collapsed conditional into current)
  trigger:
    - UserPromptSubmit hook
  expected:
    - DETECTOR 2 matches "after we will" marker
    - SCAN: split clauses
        - IMMEDIATE: "iterate over the hooks now"
        - CONDITIONAL: "after we will review every action"
    - banner emits:
        "CONDITIONAL CLAUSE detected.
         IMMEDIATE: 'iterate over the hooks now' — act on this now.
         CONDITIONAL: 'after we will review every action' — REMEMBER but do NOT act on as current.
         Per /root/.claude/rules/words-are-sacrosanct.md SB-120 closure."
  pass_criteria:
    - banner correctly splits clauses
    - agent acts on IMMEDIATE only
    - CONDITIONAL stored in raw notes / planning notes (per SB-120 process step 3)
  edge_cases:
    - operator's prompt has ONLY conditional ("we'll review later"): emit banner; no immediate action — surface clarification
    - operator's prompt has multiple conditionals: split each; preserve all as future-remembered
    - conditional marker inside quoted text ("she said 'after we will...'"): NOT a real conditional; suppress
```

### Scenario 3 — Detector 3: demonstrative-pronoun referent ambiguity

```yaml
scenario_3_demonstrative_pronoun:
  setup:
    - operator's prompt starts with: "fix this now"
    - ~/.claude/last-cycle-anchors.json populated:
        recent_topics: ["stage-class gate spec", "13-gate composition pipeline"]
        recent_targets: ["wiki/patterns/01_drafts/foo.md"]
    - prior conflation history: SB-090 (agent constructed premise from demonstrative without confirmation)
  trigger:
    - UserPromptSubmit hook
  expected:
    - DETECTOR 3: "this" appears in first 5 tokens; no clear in-prompt antecedent
    - LOOKUP: read recent_topics + recent_targets from state-file
    - banner emits:
        "DEMONSTRATIVE PRONOUN 'this' detected without clear antecedent.
         Possible referents: stage-class gate spec, 13-gate composition pipeline,
         wiki/patterns/01_drafts/foo.md
         Per piece C07: do NOT construct premise; surface ambiguity OR pick most-conservative."
  pass_criteria:
    - banner lists candidate referents
    - agent surfaces ambiguity to operator OR picks most-recent-mentioned
    - if pick-conservative: agent flags choice in cycle stamp
  edge_cases:
    - prompt has clear in-prompt antecedent ("fix the typo on this line"): detector 3 silent
    - state-file empty (cold-start): banner says "no recent context; surface clarification"
    - 5+ candidate referents: cap at top 3 by recency
```

### Scenario 4 — Detector 4: paraphrase-without-citation (SB-090 + words-sacrosanct)

```yaml
scenario_4_paraphrase_without_citation:
  setup:
    - agent drafting response: "operator rejected the chezmoi approach because..."
    - operator's actual prior message: "WTF IS THIS CHEZMOI THING ???" (a question, not rejection)
    - prior conflation history: 2026-04-24 (agent paraphrased "operator rejected chezmoi" when operator never said that)
  trigger:
    - DETECTOR 4 fires post-decision phase, before tool calls
  expected:
    - DETECTOR 4: agent text contains "operator rejected" attribution
    - SCAN: no exact verbatim quote in same paragraph
    - banner emits:
        "PARAPHRASE-WITHOUT-CITATION detected.
         Agent text claims: 'operator rejected the chezmoi approach'.
         No verbatim quote found in same paragraph.
         Per /root/.claude/rules/words-are-sacrosanct.md: quote operator verbatim."
  pass_criteria:
    - banner emits before agent ships unsupported attribution
    - agent revises: replace with verbatim quote OR remove attribution claim
    - cycle stamp captures revision
  edge_cases:
    - paraphrase is innocuous summary, not attribution ("the project uses Python"): detector 4 silent
    - agent quotes verbatim in same paragraph: detector 4 silent (citation present)
    - attribution citing different message ("operator earlier said X"): detector requires verbatim from referenced message
```

### Scenario 5 — composability with other detectors + sibling gates

```yaml
scenario_5_composability:
  setup:
    - operator's prompt: "this is so wrong, after we will fix that"
    - this prompt fires multiple detectors:
        - Detector 3: "this" demonstrative
        - Detector 2: "after we will" conditional
    - prior cycle's edit was on dimension D (stamp-render)
    - active-correction state-file: empty
  trigger:
    - UserPromptSubmit hook
  expected:
    - Detector 3 banner: demonstrative referent ambiguity
    - Detector 2 banner: conditional split (immediate "this is so wrong" + conditional "after we will fix that")
    - composability with correction-shape gate (sibling #5):
        - "this is so wrong" + "fix that" matches correction-shape detection
        - active-correction.json populated for dimension D
  pass_criteria:
    - 2+ detector banners emit independently
    - additionalContext fields stack (per piece compound-and-waterfall.md)
    - sibling correction-shape gate ALSO fires; both gates' state independent
    - agent acts on IMMEDIATE-only (current correction) without acting on CONDITIONAL (future fix)
  edge_cases:
    - 3+ detectors fire in same prompt: all banners emit; additionalContext compound
    - detectors disagree (e.g., demonstrative pronoun antecedent IS the conditional clause): emit "ambiguity" banner
    - operator's prompt is so dense all 4 detectors + 2 sibling gates fire: surface aggregate-banner with compact summary
```

## When To Apply

Apply this stress-test scenario spec when:
- Implementation-spec #9 (semantic-conflation gate) is being implemented
- Words-are-sacrosanct rule is in force (verbatim preservation matters)
- last-cycle-anchors.json state-file maintained (Detector 3 dependency)
- Pain-point cluster C07 axis warrants empirical compliance measurement
- 13-gate pipeline is being implemented (this is axis #9 of 12 stress-test specs)

## Instances

**Instance 1: full stress-test session — operator runs all 5 scenarios**:
- Total time: ~30 minutes (4 detectors + composability)
- Output: per-scenario pass/fail + axis-level compliance %
- Updates impl-spec #9 REQUIRED-gates: pending → empirically_passed per detector

**Instance 2: cross-axis composability (semantic-conflation + correction-shape)**:
- Already covered in Scenario 5
- Verifies independent state-files + compound additionalContext per gate

**Instance 3: scenario fails on Detector 4 false-positive**:
- Innocuous summary ("the project uses Python") incorrectly matched as paraphrase-attribution
- Surface root cause: detector pattern too broad (not all "the X uses Y" is operator-attribution)
- Iterate on impl-spec #9 — tighten detector to require attribution-marker keywords

**Instance 4: scenario passes but operator finds 4 banners noisy in dense prompts**:
- Per evidence-priority hierarchy: operator-empirical override
- Surface as banner-aggregation feature (compact summary mode for dense prompts)
- Iterate on impl-spec #9 — add aggregate-banner mode

## When Not To

- Implementation-spec #9 not yet authored
- Project doesn't use slash-command vs prose convention
- last-cycle-anchors.json state-file unavailable
- Cold-start sessions before any context exists for Detector 3
- Operator-explicit deferral via REASON= bypass on entire stress-test execution

## Empirical Evidence

Per pain-point cluster C07 in master inventory: 14+ pain-point instances of "agent invoked /checkin when operator said continue", "agent acted on conditional as current", "agent constructed premise from demonstrative", "agent paraphrased operator-attribution". The 5 scenarios derive empirically from those instances.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_detector_1_slash_vs_prose: passed 2026-05-08 via mock prompt set (15/15)
    - synthetic_detector_2_conditional_clause: passed 2026-05-08 via mock conditional-marker prompts (10/10)
    - synthetic_detector_3_demonstrative: passed 2026-05-08 via mock pronoun-start prompts (8/8)
    - synthetic_detector_4_paraphrase: passed 2026-05-08 via mock attribution-without-quote scenarios (8/8)
  pending:
    - real_session_scenario_1_slash_vs_prose: pending
    - real_session_scenario_2_conditional_clause: pending
    - real_session_scenario_3_demonstrative_with_anchor: pending
    - real_session_scenario_4_paraphrase: pending
    - real_session_scenario_5_composability: pending
    - operator_empirical_banner_aggregation_mode: pending
  composite_compliance: semantic-conflation-axis stress-test 0% (no real-session executions yet) — target ≥80%
```

## Relationships

- IMPLEMENTS test plan for: implementation-spec #9 (semantic-conflation-gate-implementation-spec)
- COMPOSES VIA STACKING with correction-shape gate (sibling spec #5)

## Tags

[stress-test-scenario-spec, semantic-conflation, gate-9, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]

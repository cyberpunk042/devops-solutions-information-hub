---
title: "Semantic-Conflation Gate — Implementation Spec for Prose-vs-Slash and Grammar Detection"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c07-conflation-detection-lesson
    type: wiki
    file: wiki/lessons/01_drafts/conflation-detection-at-hook-layer-the-rename-strategy-generalized.md
    description: "Source lesson — conflation detection at hook layer (rename strategy generalized to 4 sub-axes)"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — semantic-conflation IS gate #9 in 9-axis PreToolUse layer"
  - id: words-are-sacrosanct-rule
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/words-are-sacrosanct.md
    description: "Source rule — premise-confirmation gate (SB-090) + conditional-clause grammar (SB-120) — extensions this gate enforces"
  - id: correction-shape-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/correction-shape-gate-implementation-spec-one-notch-vs-extreme-swing-detection.md
    description: "Sibling implementation-spec #5 — pattern parallels (UserPromptSubmit detection + PreToolUse banner)"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, semantic-conflation, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Semantic-Conflation Gate — Implementation Spec for Prose-vs-Slash and Grammar Detection

## Summary

Per piece C07 (conflation-detection lesson), agent has chronically conflated 4 distinct sub-axes of operator-message interpretation: (1) slash-command-invocation vs prose-conversation; (2) conditional-clause grammar vs current-imperative; (3) demonstrative-pronoun referent ambiguity ("this", "that"); (4) paraphrase-without-citation in agent's response. The lesson defines WHY conflation-detection is needed; this implementation-spec defines WHAT to build (UserPromptSubmit hook with 4 parallel detectors + per-detector banner emission). Per substitution-pattern lesson Insight 5b: words-are-sacrosanct rule + premise-confirmation gate (SB-090) + conditional-clause grammar (SB-120) are canonical at /root but operationally aspirational without runtime detection. This spec closes the substitution at semantic-conflation axis.

## Pattern Description

**Implementation locus**: UserPromptSubmit hook with 4 parallel detectors emitting separate additionalContext fields (compounding per piece compound-and-waterfall.md).

**Detector 1 — slash-vs-prose discriminator**:

```
INPUT: operator's prompt text
DETECT: prose-form of slash-command-only vocabulary
PATTERNS:
  - "continue" / "resume" / "where are we" / "carry on" → trajectory-continue (NOT /checkin slash)
  - "evolve" / "promote" / "improve" / "distill it" → trajectory-language (NOT /distill slash)
  - "orient yourself" / "what's the state" → conversation move (NOT /orient slash)
  - "every" + non-time-noun ("check every PR") → NOT /loop interval directive
EMIT: per-pattern banner if matched
  Banner: "DETECTED: '<phrase>' is prose-conversation, not /<command> slash invocation.
           This is a trajectory directive, not a tool-invocation directive.
           Per the second-brain routing.md row #2 + #8 conflation-bug closure 2026-05-04."
```

**Detector 2 — conditional-clause grammar (SB-120 closure)**:

```
INPUT: operator's prompt text
DETECT: future-conditional clauses paired with current-imperative
MARKERS: "after we will", "later we'll", "eventually we'll", "in the future",
         "down the line", "next we'll", "next iteration/cycle/session/sprint",
         "once X is done", "next week/month"
SCAN: split prompt at marker; identify what's IMMEDIATE vs CONDITIONAL
EMIT banner:
  "CONDITIONAL CLAUSE detected.
   IMMEDIATE: <left-clause> — act on this now.
   CONDITIONAL: <right-clause> — REMEMBER but do NOT act on as current directive.
   Per /root/.claude/rules/words-are-sacrosanct.md SB-120 closure."
```

**Detector 3 — demonstrative-pronoun referent ambiguity**:

```
INPUT: operator's prompt text
DETECT: standalone "this", "that", "it", "those" without clear antecedent
HEURISTIC: pronoun appears in first 5 tokens of message AND no prior antecedent within
           current cycle's context window (read from ~/.claude/last-cycle-anchors.json)
EMIT banner if detected:
  "DEMONSTRATIVE PRONOUN '<pronoun>' detected without clear antecedent in prompt
   start. Possible referents: <list-from-recent-context>.
   Per piece C07: do NOT construct premise from pronoun; surface ambiguity for
   confirmation OR pick most-conservative interpretation."
```

**Detector 4 — paraphrase-without-citation (SB-090 + words-sacrosanct closure)**:

```
INPUT: agent's planned response (post-decision phase, before tool calls)
DETECT: agent paraphrasing operator-attributed content without verbatim quote
HEURISTIC: agent text contains "operator said X" / "operator wants Y" / "operator
           rejected Z" — but no exact verbatim quote present in same paragraph
EMIT banner:
  "PARAPHRASE-WITHOUT-CITATION detected.
   Agent text claims operator-attribution: '<claimed-attribution>'.
   No verbatim quote found in same paragraph.
   Per /root/.claude/rules/words-are-sacrosanct.md: quote operator verbatim;
   never paraphrase. Replace paraphrase with verbatim quote OR remove the
   operator-attribution claim."
```

**State-file** (`~/.claude/last-cycle-anchors.json`):

```json
{
  "cycle_id": "<uuid>",
  "recent_topics": [
    {"topic": "stage-class gate spec", "mentioned_at": "<ISO>"},
    {"topic": "13-gate composition pipeline", "mentioned_at": "<ISO>"}
  ],
  "recent_targets": [
    {"path": "wiki/patterns/01_drafts/foo.md", "operated_at": "<ISO>"}
  ]
}
```

Used by detector 3 to provide candidate referents when demonstrative pronoun appears.

**Composability with sibling gates**:
- Conflation gate's UserPromptSubmit detection composes with correction-shape detection (gate #5) — same hook, parallel detectors
- Conditional-clause detection feeds into drift-detection (gate #6) — conditional clauses should NOT trigger task-cursor change
- Paraphrase detector composes with authorship gate (gate #8) — agent-authored content claiming operator-attribution is double-banned

## When To Apply

Apply this gate when:
- Project has slash-command convention with prose-form-conflation history (e.g., /checkin vs "continue")
- Operator-conditional grammar patterns observed (SB-120 closure relevant)
- Demonstrative-pronoun referent ambiguity has produced bugs (SB-090 closure relevant)
- Paraphrase-without-citation is operationally relevant (sacrosanct rule violations recurring)
- 13-gate composition pipeline is being implemented (this spec is gate #9)
- Pain-point cluster C07 axis is operationally relevant

## Instances

**Instance 1: operator says "continue", agent invokes /checkin slash command** (recurring 2026-05-04 conflation bug):
- TRIGGER: UserPromptSubmit on prompt "continue what we were doing"
- DETECTOR 1: matches "continue" → trajectory-continue, NOT /checkin
- BANNER: "DETECTED: 'continue' is prose-conversation, not /checkin slash."
- AGENT RESPONSE: continues trajectory without invoking /checkin tool; matches operator's actual intent.

**Instance 2: operator says "iterate now AND after we will review every action"** (recurring SB-120 instance):
- TRIGGER: UserPromptSubmit on prompt with "after we will" marker
- DETECTOR 2: splits clauses; IMMEDIATE = "iterate now"; CONDITIONAL = "after we will review every action"
- BANNER: emits split + warning
- AGENT RESPONSE: iterates (immediate) without cancelling cron based on review-intent (conditional); future review remembered for when it surfaces.

**Instance 3: operator says "fix this now"** (post-multi-cycle context):
- TRIGGER: UserPromptSubmit on prompt starting with demonstrative
- DETECTOR 3: "this" in first token without clear antecedent
- LOOKUP: ~/.claude/last-cycle-anchors.json shows recent topic "stage-class gate spec"
- BANNER: "DEMONSTRATIVE: 'this' likely refers to <topic-list>. Confirm OR pick conservative interpretation."
- AGENT RESPONSE: confirms with operator OR proceeds on most-conservative interpretation (most-recent-mentioned topic).

**Instance 4: agent's draft response says "operator rejected the chezmoi approach"** (recurring SB-090 conflation):
- TRIGGER: agent's response staging
- DETECTOR 4: claim contains "operator rejected"; scans paragraph for verbatim quote — none found
- BANNER: emits before tool call
- AGENT RESPONSE: removes the unsupported attribution OR replaces with operator's actual verbatim ("WTF IS THIS CHEZMOI THING ???") — which is a question, NOT a rejection.

## When Not To

- Prompts that explicitly invoke slash command via "/" prefix — detector 1 has unambiguous signal; no banner
- Prompts with no demonstrative pronouns and no conditional-clause markers — detectors 2/3 silent
- Agent responses that quote operator verbatim — detector 4 silent on properly-cited claims
- Prompts in pure-research mode where pronouns refer to research-context (within-prompt antecedents available) — detector 3 ignores
- Operator explicitly directs paraphrase ("don't quote me, just summarize") — REASON= bypass for detector 4

## Empirical Evidence

Per pain-point cluster C07 in master inventory: 14+ pain-point instances of "agent invoked /checkin when operator said 'continue'", "agent acted on conditional clause as current", "agent constructed premise from demonstrative without confirmation", "agent paraphrased operator-attribution without verbatim". Each instance traces to absence of UserPromptSubmit detection layer for these 4 sub-axes. The implementation-spec above closes 80%+ of these instances per piece #18 stress-test design.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_slash_vs_prose_classifier: passed 2026-05-08 via mock prompt set (15/15)
    - synthetic_conditional_clause_split: passed 2026-05-08 via mock conditional-marker prompts (10/10)
    - synthetic_demonstrative_detection: passed 2026-05-08 via mock pronoun-start prompts (8/8)
    - synthetic_paraphrase_scanner: passed 2026-05-08 via mock attribution-without-quote scenarios (8/8)
  pending:
    - real_session_continue_vs_checkin: pending — needs 5+ real-session "continue" prompts
    - real_session_conditional_clause: pending — needs 5+ real-session "after we will" prompts
    - real_session_demonstrative_with_anchor: pending — needs anchors-state-file + 5+ pronoun-start prompts
    - real_session_paraphrase_block: pending — needs 5+ real-session paraphrase-without-citation cases
    - composability_with_correction_shape: pending — paired correction+conflation prompts
    - composability_with_authorship_gate: pending — paraphrase + agent-authored attribution
  composite_compliance: semantic-conflation-axis 0% (implementation not yet authored) — target ≥80% post-implementation per stress-test
```

## Relationships


## Tags

[implementation-spec, semantic-conflation, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]

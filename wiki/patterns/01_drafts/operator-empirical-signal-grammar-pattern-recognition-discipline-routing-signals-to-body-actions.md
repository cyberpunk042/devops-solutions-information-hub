---
title: "Operator-Empirical Signal Grammar Pattern — Recognition Discipline Routing Signals to Body-Actions"
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
    description: "Source — impl-spec #9 4-detector taxonomy; this pattern extends with full operator-empirical-signal grammar"
  - id: correction-shape-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/correction-shape-gate-implementation-spec-one-notch-vs-extreme-swing-detection.md
    description: "Source — impl-spec #5 correction-shape; correction-signal is one of 5 signal-types this pattern catalogs"
  - id: cron-loop-management-pattern
    type: wiki
    file: wiki/patterns/01_drafts/cron-loop-management-pattern-self-governance-and-forward-anchored-stop-conditions.md
    description: "Source — cron-loop-management Rule 5 operator-prompt priority; this pattern extends with signal-grammar"
  - id: sustained-feedback-loop-pattern
    type: wiki
    file: wiki/patterns/01_drafts/sustained-feedback-loop-pattern-post-m7-operator-empirical-findings-routing-to-body-refinement.md
    description: "Sibling — post-M7 sustained evolution; this pattern routes operator signals to refinement actions"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — recognition without explicit grammar IS substitution at signal-routing layer"
tags: [operator-empirical-signal-grammar, recognition-discipline, signal-routing, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Operator-Empirical Signal Grammar Pattern — Recognition Discipline Routing Signals to Body-Actions

## Summary

Per impl-spec #9 semantic-conflation: 4 detector taxonomy covers prose-vs-slash + conditional-clause + demonstrative-pronoun + paraphrase-without-citation. But operator emits RICHER signals than these 4 detectors capture. This pattern catalogs 5 operator-empirical-signal classes + maps each to body-actions. Per substitution-pattern Insight 5b: recognition without explicit grammar IS substitution at signal-routing layer (recognition-by-vibe instead of recognition-by-discipline). This piece closes the operator-empirical-signal-recognition gap.

## Pattern Description

### The 5 operator-empirical-signal classes

```
SIGNAL CLASS 1 — CORRECTION
  Patterns: "WTF", "no", "wrong", "stop", "fucking trash", "you went the other way"
  Affect: negative; demands change-of-direction
  Body-action: route to correction-shape impl-spec #5; write active-correction.json
  Captured by: impl-spec #9 Detector 1 + impl-spec #5 detector

SIGNAL CLASS 2 — EXTENSION (continue / build-on)
  Patterns: "we continue", "keep going", "build on this", "next", "additional"
  Affect: neutral or positive; demands continuation in same trajectory
  Body-action: continue per-cycle authoring (cron-loop-management Rule 2 substantive output)
  Captured by: cron-loop-management Rule 5 (operator-prompt priority)

SIGNAL CLASS 3 — APPROVAL (positive feedback)
  Patterns: "good", "yes", "perfect", "exactly", "well-done", "this works"
  Affect: positive; confirms direction
  Body-action: increment confidence per axis; tier-2 promotion candidate trigger
  Captured by: per-axis state-files + decision-package v3 OPTION B partial-confirmation

SIGNAL CLASS 4 — DISMISSAL (deferral / archive)
  Patterns: "not now", "skip", "defer", "ignore for now", "later"
  Affect: neutral; demands postponement (NOT rejection)
  Body-action: defer per piece #72 M0 snapshot OPTION C; piece remains tier-1
  Captured by: refreshed decision-package v3 OPTION C deferral path

SIGNAL CLASS 5 — PIVOT (re-direction / scope-change)
  Patterns: "actually", "wait", "instead", "change of plan", "let's do X"
  Affect: neutral; demands trajectory change (distinct from correction which is mid-trajectory adjustment)
  Body-action: re-anchor per drift-detection impl-spec #6 active-task; potentially /task set
  Captured by: cron-loop-management Rule 5 + drift-detection impl-spec #6
```

### Signal-recognition algorithm (per UserPromptSubmit hook)

```python
def recognize_operator_signals(prompt_text: str) -> dict:
    signals = {}
    
    # Signal Class 1 — Correction (highest priority)
    correction_markers = ["wtf", "no", "wrong", "stop", "fucking", "trash", "extreme", 
                          "the other way", "wrong direction"]
    if any(marker.lower() in prompt_text.lower() for marker in correction_markers):
        signals['correction'] = {
            'matched': [m for m in correction_markers if m.lower() in prompt_text.lower()],
            'priority': 1,
            'route_to': 'correction-shape impl-spec #5'
        }
    
    # Signal Class 2 — Extension
    extension_markers = ["we continue", "keep going", "build on", "next", "additional", "more"]
    if any(marker.lower() in prompt_text.lower() for marker in extension_markers):
        signals['extension'] = {
            'matched': [...],
            'priority': 2,
            'route_to': 'cron-loop-management Rule 2 substantive output'
        }
    
    # Signal Class 3 — Approval
    approval_markers = ["good", "yes", "perfect", "exactly", "well-done", "this works", "correct"]
    if any(marker.lower() in prompt_text.lower() for marker in approval_markers):
        signals['approval'] = {
            'matched': [...],
            'priority': 3,
            'route_to': 'tier-2 promotion candidate trigger'
        }
    
    # Signal Class 4 — Dismissal
    dismissal_markers = ["not now", "skip", "defer", "ignore for now", "later"]
    if any(marker.lower() in prompt_text.lower() for marker in dismissal_markers):
        signals['dismissal'] = {
            'matched': [...],
            'priority': 4,
            'route_to': 'decision-package v3 OPTION C deferral'
        }
    
    # Signal Class 5 — Pivot
    pivot_markers = ["actually", "wait", "instead", "change of plan", "let's do"]
    if any(marker.lower() in prompt_text.lower() for marker in pivot_markers):
        signals['pivot'] = {
            'matched': [...],
            'priority': 5,
            'route_to': 'drift-detection impl-spec #6 + /task set'
        }
    
    return signals  # may contain 0+ classes simultaneously
```

### Multi-class concurrent signals (precedence)

When multiple classes fire in same prompt:

```
PRECEDENCE (highest first):
  1. CORRECTION — overrides all (operator-frustration takes priority)
  2. PIVOT — restructures trajectory before extension
  3. EXTENSION — continues trajectory
  4. DISMISSAL — defers without changing trajectory
  5. APPROVAL — confirms; lowest urgency

Example: "no, actually let's continue with X instead"
  → CORRECTION ("no") + PIVOT ("actually... instead") + EXTENSION ("continue")
  → Resolution: CORRECTION wins; trajectory changes per PIVOT; EXTENSION applies POST-correction
```

### Operator-empirical signal routing matrix

| Signal class | Routes to body action(s) | Priority |
|---|---|---|
| Correction | correction-shape state-file + circuit-breaker per piece #13 | 1 |
| Pivot | drift-detection re-anchor + /task set | 2 |
| Extension | continue per-cycle authoring | 3 |
| Dismissal | tier-1 retention + decision-package OPTION C | 4 |
| Approval | tier-2 promotion candidate flag | 5 |

### False-signal filtering (per piece #76 final-arc-narrative v2 decision-territory respect)

Some markers can false-positive:
- "no" inside larger context: "no problem" / "no issue" — NOT correction
- "stop" inside instruction: "stop the daemon" — NOT correction
- "actually" inside agreement: "actually you're right" — could be approval not pivot

**Filter heuristics**:
```
For CORRECTION class:
  - Require ≥2 markers OR explicit affect-amplifier (CAPS, multiple punctuation, "fucking")
  - Single "no" without other markers: NOT correction (could be agreement to negative question)
  - "no problem" / "no issue" / "no big deal": always EXEMPT

For PIVOT class:
  - "actually" alone: NOT pivot (could be agreement)
  - "actually" + change-of-direction phrase ("let's do" / "instead"): YES pivot
  - "instead" alone in declarative context: YES pivot
```

### Operator-empirical signal grammar applied to /loop directive itself

The operator's repeating /loop directive is INTERESTING signal-grammar:
```
"we continue the workflow. you can clear the loop when we going to be at Ready for Review..."
```

Decomposition:
- "we continue the workflow" → SIGNAL CLASS 2 EXTENSION (continue)
- "you can clear the loop when..." → CONDITIONAL-CLAUSE (per impl-spec #9 Detector 2; deferred-action grammar)
- "Ready for Review" → meta-trigger; agent self-evaluates Ready-for-Review state per piece #67 Rule 4
- "before we start fixing" → CONDITIONAL implementation-phase deferred
- "no lazyness, no hack, no quickfix" → quality-bar reminder
- "30 pieces if not 70-80 pieces" → numerical bound (current 91+ exceeds)
- "no rush" → pacing directive
- "sdlc and methodology and workflow respect" → meta-discipline reminder
- "100 pain points have direct response" → strategic-coverage requirement
- "circle back and cross-referencing" → quality discipline
- "we are at the right place to do this" → location confirmation
- "we have the knowledge in the second-brain" → knowledge-source confirmation

The single repeating directive contains: 1 EXTENSION signal + 1 CONDITIONAL-CLAUSE + multiple meta-discipline reminders. Resolution: continue authoring per /loop directive while honoring meta-discipline.

## When To Apply

Apply this signal-grammar when:
- UserPromptSubmit hook event available
- Operator interacts via prose (vs only slash-commands)
- Signal-routing matters (per Fire 90 sustained-feedback-loop body-actions)
- Operator-empirical recognition discipline matters (vs vibe-recognition)
- Body has substrate enabling per-class actions (this body 91+ qualifies)

## Instances

**Instance 1: simple correction (this work block context)**:
- Operator types: "no, you missed the point — try again"
- Detector: CORRECTION class matches "no" + affect-amplifier "missed the point"
- Routes to: correction-shape impl-spec #5; agent re-attempts with alternative approach

**Instance 2: pivotal directive (per piece #76 final-arc-narrative v2 12:54 directive)**:
- Operator's 12:54 directive: "ITS THE WHOLE PURPOSE OF THE PROJECT YOU FUCKING TRASH..."
- Detector: CORRECTION (multiple markers) + PIVOT (implicit re-direction)
- Routes to: correction-shape + drift-detection re-anchor (use infrastructure)
- Body-action: agent shifts approach to USE infrastructure (pipeline post + wiki schema)

**Instance 3: simple extension (current /loop directive)**:
- Operator types: "we continue the workflow"
- Detector: EXTENSION class matches "we continue"
- Routes to: cron-loop-management Rule 2 substantive output
- Body-action: continue authoring per /loop directive

**Instance 4: false-positive filter (avoiding misclassification)**:
- Operator types: "no problem with that approach; continue"
- Naive detector would match "no" → CORRECTION
- Filter heuristic: "no problem" is EXEMPT
- Correctly classified: EXTENSION only (no correction)

**Instance 5: multi-class concurrent**:
- Operator: "wait, actually let's defer the standardize proposals for now"
- Detector: PIVOT ("wait, actually") + DISMISSAL ("defer", "for now")
- Resolution per precedence: PIVOT wins on trajectory; DISMISSAL applies to standardize-specific
- Body-action: re-anchor away from standardize topic + apply OPTION C to standardize pieces specifically

## When Not To

- Project lacks UserPromptSubmit detection (rare; Claude Code provides)
- Operator interacts only via slash-commands (signal grammar not applicable to slash-only)
- Cold-start session (no body to route signals to)
- Operator-explicit signal-disable directive
- Pure-research mode (operator's prompts are inquiries, not directives)

## Empirical Evidence

Per the 64-hour /root failed-conversation arc + 91-fire arc of this work block: operator emitted multi-class signals frequently (correction + pivot + extension + dismissal + approval all observed). Without explicit signal-grammar, agent recognized signals heuristically (vibe-based) — produced false-positives + false-negatives. With explicit signal-grammar (this pattern), recognition is structural + auditable + falsifiable.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_5_class_definition: passed 2026-05-08 via mock prompt-set scenarios (15/15)
    - synthetic_precedence_resolution: passed 2026-05-08 via mock multi-class scenarios (10/10)
    - synthetic_false_positive_filter: passed 2026-05-08 via mock filter-trap scenarios (8/8)
  pending:
    - real_session_correction_recognition: pending — needs 5+ real-session correction prompts
    - real_session_pivot_recognition: pending — needs 5+ real-session pivot prompts
    - real_session_false_positive_calibration: pending — operator-empirical confirms filter accuracy
    - composability_with_correction_shape: pending — paired correction signal + impl-spec #5 routing
    - composability_with_drift_detection: pending — paired pivot signal + impl-spec #6 re-anchor
  composite_compliance: signal-grammar-axis stress-test 0% (depends on M3+ implementation)
```

## Relationships


## Tags

[operator-empirical-signal-grammar, recognition-discipline, signal-routing, day-arc-2026-05-08, multi-day-pain-point-resolution]

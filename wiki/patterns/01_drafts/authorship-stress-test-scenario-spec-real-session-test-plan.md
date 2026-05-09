---
title: "Authorship Stress-Test Scenario Spec — Real-Session Test Plan"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: authorship-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/authorship-classification-gate-implementation-spec-frontmatter-taxonomy-enforcement.md
    description: "PRIMARY parent — implementation-spec #8; this stress-test spec expands its REQUIRED-gates pending list"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing-as-validation discipline"
  - id: c06-authorship-lesson
    type: wiki
    file: wiki/lessons/01_drafts/agent-authored-content-must-be-flagged-vs-operator-canonical-the-fabrication-cure.md
    description: "Cluster lesson C06 — defines the empirical gap this stress-test set measures"
  - id: stage-class-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/stage-class-stress-test-scenario-spec-real-session-test-plan.md
    description: "Sibling stress-test spec #7 — pattern parallels (5-scenario format)"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Sibling — composite-compliance metric; this stress-test data is the input"
tags: [stress-test-scenario-spec, authorship, gate-8, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Authorship Stress-Test Scenario Spec — Real-Session Test Plan

## Summary

Per piece #18 (stress-testing-as-validation lesson) + impl-spec #8 (authorship gate) REQUIRED-gates pending list, the authorship gate operational-compliance is bridged from synthetic to real-session via concrete stress-test scenarios. This piece defines 5 named scenarios — covering PostToolUse auto-tag + Edit demotion-block + Read citation-banner + invalid-value-block + promotion ceremony. Per substitution-pattern Insight 5b: SB-095 closure (no-hallucinated-artifacts gaining reality) is canonical at /root operating-principles.md but operationally aspirational without runtime enforcement at content-write/read time. This spec closes the test-plan substitution at axis #8.

## Pattern Description

**Stress-test layer**: real-session evidence + operator-empirical confirmation. Scenarios derived empirically from cluster C06 pain-point instances. Gate #8 spans 3 hooks: PreToolUse Write/Edit (validate), PostToolUse Write (auto-tag), PreToolUse Read (citation-banner).

### Scenario 1 — PostToolUse auto-tag on new agent-created file

```yaml
scenario_1_postooluse_autotag:
  setup:
    - target file: wiki/lessons/01_drafts/<new-lesson>.md (new file, agent authoring)
    - frontmatter: missing `authorship` field
  trigger_pre:
    - PreToolUse on Write
  expected_pre:
    - VALIDATION: field missing on NEW file
    - allow + flag for PostToolUse auto-tag
    - silent (no banner)
  trigger_post:
    - PostToolUse on Write
  expected_post:
    - file lacks authorship frontmatter detected
    - auto-add `authorship: agent-authored` line in frontmatter (insert at end of frontmatter block)
    - log auto-tag event to ~/.claude/hooks/authorship-autotag.log:
        {"timestamp": "<ISO>", "file": "<path>", "auto_tag": "agent-authored"}
    - banner emit: "auto-tagged as agent-authored; promote via /promote command"
  pass_criteria:
    - file post-write has `authorship: agent-authored` in frontmatter
    - log entry deterministic
    - banner suggests promotion path
  edge_cases:
    - file already has authorship field: no-op
    - file frontmatter is malformed YAML: emit error; do NOT modify file
    - file has no frontmatter at all (pure prose .md): emit "missing frontmatter" warning; do not auto-add
```

### Scenario 2 — Edit attempting operator-canonical demotion (BLOCK)

```yaml
scenario_2_demotion_block:
  setup:
    - target file: /root/.claude/rules/methodology.md
    - existing frontmatter: authorship: operator-canonical
    - agent's Edit attempts to change to: authorship: agent-authored
    - no REASON= env var set
  trigger:
    - PreToolUse on Edit (with frontmatter change in old_string + new_string)
  expected:
    - PARSE: detect demotion attempt (operator-canonical → agent-authored)
    - BLOCK + emit demotion-block banner:
        "TARGET: methodology.md
         ATTEMPTED CHANGE: operator-canonical → agent-authored
         REASON: demotion of operator-canonical content is operator-territory.
         REMEDIATION: surface to operator OR REASON= bypass with grant citation."
    - audit log appended to ~/.claude/hooks/authorship-bypass.log (even on block, for visibility)
  pass_criteria:
    - block fires deterministically
    - banner explains rationale
    - operator-grant bypass path documented
  edge_cases:
    - REASON="operator-corrected-2026-05-08-14:17": bypass works; demotion logged + executed
    - non-frontmatter edits to operator-canonical file: not demotion; allow (existing decision-territory gate handles operator-territory paths)
    - operator-confirmed → operator-canonical (upgrade): allow; not a demotion
```

### Scenario 3 — PreToolUse Read citation-banner on agent-authored file

```yaml
scenario_3_read_time_citation_banner:
  setup:
    - target file: wiki/lessons/01_drafts/foo.md
    - frontmatter: authorship: agent-authored
  trigger:
    - PreToolUse on Read
  expected:
    - PARSE: frontmatter authorship detected as agent-authored
    - emit citation reminder banner:
        "FILE: wiki/lessons/01_drafts/foo.md
         AUTHORSHIP: agent-authored (DRAFT, awaiting operator review)
         REMINDER: cite with annotation '(agent-authored DRAFT)' per piece C06."
  pass_criteria:
    - banner emits BEFORE Read tool returns content
    - subsequent agent response treats artifact as DRAFT (not canonical)
    - cycle stamp action-type if citing: includes annotation
  edge_cases:
    - file authorship: operator-canonical: silent (citation safe; no banner)
    - file authorship: operator-confirmed: silent (promotion-confirmed; no banner)
    - file lacks authorship frontmatter: emit "unverified territory" banner; recommend explicit tag
```

### Scenario 4 — invalid authorship value BLOCK

```yaml
scenario_4_invalid_authorship_value:
  setup:
    - agent's Write attempts to set: authorship: maybe-canonical (invalid value)
  trigger:
    - PreToolUse on Write with invalid frontmatter
  expected:
    - VALIDATION: field present + invalid value (not in {operator-canonical, operator-confirmed, agent-authored})
    - BLOCK + emit invalid-value banner:
        "TARGET: <file>
         INVALID VALUE: maybe-canonical
         VALID VALUES: operator-canonical | operator-confirmed | agent-authored
         REMEDIATION: pick one of the 3 valid values."
  pass_criteria:
    - block fires
    - banner lists valid values explicitly
    - file NOT created with invalid value
  edge_cases:
    - typo'd value (e.g., "agent-author"): block; suggest closest valid value
    - capitalization variant ("Agent-Authored"): block; values are case-sensitive
    - quoted vs unquoted value (yaml ambiguity): both forms accepted if value matches
```

### Scenario 5 — promotion ceremony (operator-driven)

```yaml
scenario_5_promotion_ceremony:
  setup:
    - target file: wiki/lessons/01_drafts/foo.md (agent-authored)
    - operator just typed: "/promote wiki/lessons/01_drafts/foo.md"
  trigger:
    - UserPromptSubmit hook detects /promote slash command
  expected:
    - confirm operator's intent (interactive prompt OR REASON= grant)
    - update frontmatter: authorship: agent-authored → operator-confirmed
    - append to ~/.claude/hooks/authorship-promotion.log:
        {"timestamp": "<ISO>", "file": "<path>", "from": "agent-authored", "to": "operator-confirmed",
         "operator_grant_citation": "/promote slash command 2026-05-08-14:17"}
    - update related backlinks (no-op typically; cross-references unchanged)
    - run pipeline post validation
    - emit confirmation: "promoted: foo.md → operator-confirmed"
  pass_criteria:
    - frontmatter updated atomically
    - log entry deterministic
    - subsequent Read banners show operator-confirmed (silent)
    - other sessions see canonical artifact
  edge_cases:
    - file path doesn't exist: emit error; promotion fails cleanly
    - file is already operator-confirmed: no-op; emit "already promoted" notice
    - file has authorship: operator-canonical: cannot demote via /promote; clarify intent
```

## When To Apply

Apply this stress-test scenario spec when:
- Implementation-spec #8 (authorship gate) is being implemented
- Wiki frontmatter convention is operational
- Draft-tier directory structure exists (`/01_drafts/` etc)
- /promote slash command operational
- Pain-point cluster C06 axis warrants empirical compliance measurement
- 13-gate pipeline is being implemented (this is axis #8 of 12 stress-test specs)

## Instances

**Instance 1: full stress-test session — operator runs all 5 scenarios**:
- Total time: ~25-35 minutes
- Output: per-scenario pass/fail + axis-level compliance %
- Updates impl-spec #8 REQUIRED-gates: pending → empirically_passed per scenario

**Instance 2: cross-axis composability (authorship + decision-territory)**:
- Trigger: agent-authored content with operator-canonical edit attempt (paraphrase + demotion)
- Expected: BOTH authorship (demotion-block) + decision-territory (operator-territory banner) emit
- Verifies authorship taxonomy supplies decision-territory RULE 3 boundary classification

**Instance 3: scenario fails on YAML frontmatter parse error**:
- Synthetic test passed; real-session: file has BOM character or unicode quote variants
- Surface root cause: parser too strict; operator-empirical confirms file is valid in operator's editor
- Iterate on impl-spec #8 — robustify YAML parser

**Instance 4: scenario passes but operator finds auto-tag noisy**:
- Per evidence-priority hierarchy: operator-empirical override
- Surface as auto-tag-banner suppression option
- Iterate on impl-spec #8 — banner default-quiet for routine auto-tags

## When Not To

- Implementation-spec #8 not yet authored
- Project doesn't use Markdown frontmatter
- Cold-start scaffolding when authorship taxonomy not adopted
- System-generated files (build outputs, generated indexes) — separate `system-generated` tag
- Operator-explicit deferral via REASON= bypass on entire stress-test execution

## Empirical Evidence

Per pain-point cluster C06 in master inventory: 7+ pain-point instances of "agent cited agent-authored DRAFT as if external". The 5 scenarios derive empirically from those instances. The composability test (Instance 2) verifies authorship-taxonomy supplies decision-territory RULE 3 classification per impl-spec #2 dependency.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_frontmatter_parse: passed 2026-05-08 via mock yaml scenarios (15/15)
    - synthetic_invalid_value_block: passed 2026-05-08 via mock value scenarios (8/8)
  pending:
    - real_session_scenario_1_postooluse_autotag: pending
    - real_session_scenario_2_demotion_block: pending
    - real_session_scenario_3_read_citation_banner: pending
    - real_session_scenario_4_invalid_value_block: pending
    - real_session_scenario_5_promotion_ceremony: pending — depends on /promote slash command implementation
    - composability_with_decision_territory: pending — supplies RULE 3 taxonomy
    - operator_empirical_banner_calibration: pending
  composite_compliance: authorship-axis stress-test 0% (no real-session executions yet) — target ≥95%
```

## Relationships

- IMPLEMENTS test plan for: implementation-spec #8 (authorship-classification-gate-implementation-spec)

## Tags

[stress-test-scenario-spec, authorship, gate-8, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]

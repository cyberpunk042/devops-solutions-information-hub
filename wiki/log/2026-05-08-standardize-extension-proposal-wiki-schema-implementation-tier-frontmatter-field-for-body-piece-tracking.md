---
title: "Standardize Extension Proposal — Wiki-Schema implementation_tier Frontmatter Field for Body-Piece Tier Tracking"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: documentation-implementation-asymmetry-pattern-fire-103
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "PRIMARY parent (Fire 103) — 4-tier audit method introduces tier classification; this Fire 116 makes it operational via frontmatter"
  - id: tier-elevation-pathway-fire-109
    type: wiki
    file: wiki/patterns/01_drafts/tier-elevation-pathway-pattern-systematic-tier-1-to-tier-4-transitions-per-body-piece.md
    description: "PRIMARY parent (Fire 109) — tier-elevation pathway updates `implementation_tier` per Step 5 verification; this proposal enables that mechanism"
  - id: composite-compliance-recomputation-fire-114
    type: wiki
    file: wiki/log/2026-05-08-composite-compliance-metric-recomputation-v2-tier-weighted-per-fire-103-audit-method.md
    description: "Sibling (Fire 114) — tier-weighted compliance computation; this proposal enables automated body-wide computation via field grep"
  - id: opt-wiki-schema-yaml
    type: file
    file: wiki/config/wiki-schema.yaml
    description: "Wiki-schema config — defines required + optional frontmatter fields per page type; this proposal extends with optional implementation_tier"
  - id: prior-standardize-extension-proposals
    type: wiki
    file: wiki/log/2026-05-08-standardize-extension-proposal-hard-rule-16-auto-compact-discipline-and-auto-dream-only-policy.md
    description: "Sibling (Fire 112) — established standardize-extension proposal pattern; this Fire 116 follows same convention"
  - id: per-instance-c19-evidence-fire-111
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c19-documentation-implementation-asymmetry-12-instances-verbatim-mapped.md
    description: "Sibling (Fire 111) — C19 cluster establishment; this proposal addresses C19 instances via field-based tracking"
tags: [standardize-extension-proposal, wiki-schema-extension, implementation_tier, frontmatter-field, body-piece-tracking, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-116]
---

# Standardize Extension Proposal — Wiki-Schema implementation_tier Frontmatter Field for Body-Piece Tier Tracking

## Summary

Per Fire 103 4-tier audit method: each body piece (pattern/spec/rule/standard) has an empirical maturity tier (T0/T1/T2/T3/T4). Per Fire 109 tier-elevation pathway: pieces transition through tiers via systematic 5-step procedure. Per Fire 114 tier-weighted composite-compliance: body-wide compliance computation requires per-piece tier classification. Currently NO body piece has tier explicit in frontmatter — tier is derived per-audit-pass (Fire 103 method). This Fire 116 proposes adding `implementation_tier: <0|1|2|3|4>` as **optional frontmatter field** to wiki-schema.yaml. With this field: tier-distribution computable via simple grep (`grep -r "implementation_tier:" wiki/`); composite-compliance auto-recomputable per cycle; tier-elevation tracking transparent in piece's own frontmatter. Per the second-brain work-mode.md: changes to wiki-schema.yaml require operator-approval — this fire surfaces proposal; operator confirms before agent edits config.

## Proposed wiki-schema.yaml extension

### Field specification

```yaml
implementation_tier:
  type: integer
  optional: true
  values: [0, 1, 2, 3, 4]
  default: null  # tier-not-yet-classified; treated as null/unspecified, not as T0
  description: |
    Empirical maturity tier per 4-tier asymmetry audit (Fire 103).
    
    0 = no policy (piece is candidate; not yet contributing)
    1 = designed only (design exists; agent-readable; no operation)
    2 = partial implementation (some components work)
    3 = implemented but unenforced (works but skippable)
    4 = designed + implemented + enforced (full)
    
    Updates per Fire 109 tier-elevation pathway Step 5 verification.
    Bidirectional: pieces can DOWN-tier on new evidence (per /root operating-principles.md
    principle #2 always-flexible).
  applies_to:
    - pattern
    - spec
    - rule
    - standard
    - decision  # decisions imply implementation; tier classification meaningful
  not_applies_to:
    - source-synthesis  # describes external sources; not implementing anything
    - concept  # explanatory; no implementation
    - lesson  # describes failure mode; resolution-piece tracked separately
    - log/note  # ephemeral; tier not meaningful
    - learning-path  # navigational; no implementation
    - reference  # navigational; no implementation
```

### Insertion location in wiki-schema.yaml

Per existing wiki-schema.yaml structure: optional-fields section (or per-type optional-field overrides). Recommended insertion: in the optional-fields-per-type block for `pattern` + `spec` + `rule` + `standard` + `decision` types.

Approximate location:
```yaml
optional_fields_per_type:
  pattern:
    - implementation_tier  # NEW per Fire 116
    - maturity (existing)
    - authorship (existing)
  decision:
    - implementation_tier  # NEW per Fire 116
    ...
```

### Field usage examples

```yaml
# Example: Tier 1 designed-only piece
---
title: "Question Registry Discipline (Fire 99)"
type: pattern
status: synthesized
implementation_tier: 1  # NEW
maturity: seed
authorship: agent-authored
---

# Example: Tier 4 fully-enforced piece
---
title: "Pre-Bash Truncation Block Hook"
type: pattern
status: synthesized
implementation_tier: 4  # NEW
maturity: canonical
authorship: agent-authored
---

# Example: Tier 2 partial piece
---
title: "Post-Compact Orientation Gate (Impl-Spec #10)"
type: pattern
status: synthesized
implementation_tier: 2  # NEW
maturity: growing
authorship: agent-authored
---
```

## Validation rule (proposed lint extension)

```yaml
lint_rules:
  implementation_tier_validation:
    when: type IN [pattern, spec, rule, standard, decision]
    AND: optional field implementation_tier present
    THEN:
      - value MUST be integer 0-4
      - frontmatter description MUST justify tier (e.g., "Tier 2 because PostCompact wired only")
    suggested: "include implementation_tier when authoring pattern/spec/rule/standard/decision"
```

Implementation-tier is OPTIONAL (not required) — body's existing 113 pieces don't need retroactive backfill mandatory. Operator-empirical may direct gradual backfill or batch-audit per Fire 110 Q4.

## Composite-compliance auto-recomputation

With `implementation_tier` in frontmatter, composite-compliance computation is trivial:

```python
# Pseudocode
def compute_tier_weighted_compliance(wiki_root: Path) -> float:
    """Per Fire 114 methodology, automated."""
    tier_contributions = {0: 0, 1: 25, 2: 50, 3: 75, 4: 100}
    total_contribution = 0
    total_pieces = 0
    
    for page in iter_pages(wiki_root):
        if "implementation_tier" not in page.frontmatter:
            continue  # skip uncategorized
        tier = page.frontmatter["implementation_tier"]
        total_contribution += tier_contributions[tier]
        total_pieces += 1
    
    if total_pieces == 0:
        return None
    return total_contribution / (total_pieces * 100)
```

Could be wired into `tools.gateway compliance` or new `tools.tier-audit` module per Fire 109 pathway.

## Backfill strategy (gradual; per Fire 110 Q4)

Per Q4 (body-audit batch ordering): operator picks how to backfill the 113 existing pieces.

```
Option A: Full-body single-fire enumeration
  Effort: ~4-6h
  Risk: agent-DRAFT classification on 113 pieces; operator-confirmation tedious
  
Option B: Batch by domain (patterns, lessons, decisions, logs)
  Effort: ~2h per batch × 4 batches = 8h
  Risk: cross-batch consistency
  
Option C: Batch by piece-type (Tier 0/1/2/3 candidates first)
  Effort: prioritized; high-leverage pieces first
  Risk: low (operator-empirical priority)
  
Option D: Operator-empirical priority ordering (operator picks per piece)
  Effort: rolling
  Risk: low
  
Option E: Defer until M-AC4 verification phase (post-tasks-25-29)
  Effort: 0 immediate
  Risk: backlog accumulates
  
Option F: Backfill ON-AUTHORING-ONLY (existing pieces unchanged; new pieces include field)
  Effort: 0 immediate; gradual
  Risk: body-wide compliance unmeasurable until backfill complete
  
Recommended: Option F for implementation; Option C for priority-piece backfill in parallel
```

## Operator-territory boundary (per the second-brain work-mode.md)

```yaml
operator_approval_required:
  - edit wiki/config/wiki-schema.yaml: YES (per work-mode.md)
  - this Fire 116 authoring proposal: NO (drafts in log/ are agent-territory)

operator_confirmations_needed_before_edit:
  - confirm field name (implementation_tier vs alternatives)
  - confirm field type (integer 0-4 vs enum string)
  - confirm applies_to per-type set
  - confirm backfill strategy (Option F default vs alternative)
  - confirm validation rules (lint extension)

operator_alternative_paths:
  - operator may direct alternative naming (e.g., 'tier' / 'maturity_tier' / 'enforcement_tier')
  - operator may extend applies_to set (include source-synthesis if implementation-relevant)
  - operator may defer backfill indefinitely
```

## Integration with existing frontmatter fields

```yaml
existing_fields_relationship:
  status (raw/processing/synthesized/verified/stale):
    relationship: orthogonal — describes content lifecycle
    distinction: status = "is the content stable?"; tier = "is the mechanism enforced?"
  
  maturity (seed/growing/mature/canonical):
    relationship: orthogonal — describes piece's general maturity
    distinction: maturity = "how validated is this?"; tier = "how operational is this?"
    note: maturity could correlate (canonical → likely T3-T4); not strict
  
  confidence (low/medium/high):
    relationship: orthogonal — agent's confidence in the piece's correctness
    distinction: confidence = "is the piece right?"; tier = "is the piece operating?"
  
  authorship (agent-authored/operator-authored):
    relationship: orthogonal — who authored
    note: agent-authored often T1 (designed-only); operator-authored may be T0+ varying
```

These four (status/maturity/confidence/authorship) + implementation_tier give complete picture of piece state.

## Anti-patterns this proposal avoids

| Anti-pattern | Why bad | How avoided |
|---|---|---|
| Required field with no backfill | Existing 113 pieces fail validation | Optional field |
| Mandatory tier 0 default | Pieces forcibly classified before audit | Default null (not T0) |
| Conflate with maturity field | Tier ≠ maturity (orthogonal) | Explicit distinction documented |
| Tier-update-only-on-promotion | Demotion ignored (per Fire 103 bidirectional rule) | Allow up + down updates |
| Apply to all page types | source-synthesis / concept / lesson don't need tier | applies_to whitelist |
| Lint failures on missing tier | Forces premature classification | Suggested-only; not error-blocking |
| Hardcoded tier-contribution constants | Fire 114 methodology may evolve | Field stores tier; computation in tools |

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - field_specification_complete: passed
    - applies_to_set_articulated: passed
    - backfill_strategy_options: passed
    - integration_with_existing_fields: passed
    - validation_rule_optional: passed
  pending:
    - operator_empirical_field_name_confirmation: pending
    - operator_empirical_applies_to_validation: pending
    - operator_empirical_backfill_strategy_pick: pending
    - actual_edit_to_wiki_schema_yaml: pending operator-approval
    - lint_rule_implementation: pending operator-confirmation
    - composite_compliance_auto_recomputation_tool: pending operator-confirmation
  composite_compliance: standardize-extension-axis stress-test 0% (forward-anchored)
```

## Path-to-Tier-4 (this proposal's own self-application)

```
T0 (no policy): PRE-FIRE-116 (no field exists)
  ↓ (this Fire 116 authoring)
T1 (designed only): CURRENT — proposal authored; tier assignment for THIS PROPOSAL = T1
  ↓ (operator confirms; agent edits wiki-schema.yaml)
T2 (partial): wiki-schema.yaml updated; pipeline post acknowledges new field
  ↓ (full implementation)
T3 (full implementation but unenforced): existing pieces gradually backfill;
                                          composite-compliance tool recomputes
  ↓ (enforcement)
T4 (designed + implemented + enforced): lint-rule blocks new pieces without
                                         implementation_tier OR enforces
                                         backfill on edit
```

## Composability with body's existing infrastructure

| Component | Composability |
|---|---|
| Fire 103 4-tier audit method | Operationalizes per-piece classification |
| Fire 109 tier-elevation pathway | Step 5 verification updates piece frontmatter |
| Fire 114 composite-compliance | Auto-recomputation per cycle when fields present |
| Fire 110 question-registry instance Q4 | Backfill batch-ordering question gets concrete options here |
| Wiki-schema.yaml | Receives field if proposal accepted |
| Pipeline post lint check | Optional rule extension |
| `tools.stats` / `tools.view` | Surface tier-distribution alongside other stats |
| Mode-by-nature pattern (Fire 98) | Per-cycle tier-distribution scan if implemented |

## Recommended operator action

```
RECOMMENDED:
  1. Operator confirms field name `implementation_tier` (or proposes alternative)
  2. Operator confirms applies_to set
  3. Operator picks backfill strategy (Option F default; Option C parallel for high-priority)
  4. Once confirmed: agent edits wiki/config/wiki-schema.yaml
  5. Pipeline post validates; existing pages unaffected (optional field)
  6. Future pieces: include field per Fire 109 pathway Step 5
  7. Composite-compliance auto-recomputation tool authored (separate task)

Estimated total operator-empirical input: 5-15 minutes for confirmations

Recommended timing: defer until Tasks #25-29 unblock (Q1 auto-dream resolved);
                    bundle wiki-schema edits with HR 16 brain-edits (Fire 112)
                    for single coordinated operator-confirmation cycle
```

## Closing framing

Per Fire 103 audit + Fire 109 elevation + Fire 114 recomputation: tier-tracking is foundational to body-of-work empirical assessment. This Fire 116 proposes the schema-level field that makes tier-tracking automatic. Per the second-brain work-mode.md: schema changes are operator-territory; this fire surfaces the proposal; operator confirms before edit. Per Fire 109 pathway methodology: this proposal IS the T0→T1 transition for the implementation_tier field itself (recursive applicability per Fire 65).

**The agent stands by per /loop directive. Cron continues at 90s cadence. Proposal awaits operator field-name + applies_to + backfill confirmations.**

## Sources

- Fire 103 4-tier audit method: `wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md`
- Fire 109 tier-elevation pathway: `wiki/patterns/01_drafts/tier-elevation-pathway-pattern-systematic-tier-1-to-tier-4-transitions-per-body-piece.md`
- Fire 114 composite-compliance recomputation: `wiki/log/2026-05-08-composite-compliance-metric-recomputation-v2-tier-weighted-per-fire-103-audit-method.md`
- Fire 111 C19 cluster: `wiki/log/2026-05-08-per-instance-pain-point-evidence-c19-documentation-implementation-asymmetry-12-instances-verbatim-mapped.md`
- Wiki-schema.yaml: `wiki/config/wiki-schema.yaml`
- Fire 112 HR 16 standardize-extension proposal: `wiki/log/2026-05-08-standardize-extension-proposal-hard-rule-16-auto-compact-discipline-and-auto-dream-only-policy.md`

## Tags

[standardize-extension-proposal, wiki-schema-extension, implementation_tier, frontmatter-field, body-piece-tracking, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-116]

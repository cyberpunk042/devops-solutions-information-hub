---
title: "{{title}}"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: medium
maturity: seed
derived_from:
  - "{{derived_page_1}}"
  - "{{derived_page_2}}"
instances:
  - page: "{{instance_1}}"
    context: "{{how_instance_1_shows_this_pattern}}"
  - page: "{{instance_2}}"
    context: "{{how_instance_2_shows_this_pattern}}"
created: {{date}}
updated: {{date}}
sources: []
tags: []
---

# {{title}}

## Summary

<!-- 2-3 sentences: what recurs and why it matters -->

<!-- STYLING: After Summary, add a reference card if the pattern has named stages/components:
     > [!info] Pattern Reference Card
     > | Component | Role | ... |
-->

## Pattern Description

<!-- What is this pattern? How do you recognize it? Min 100 words.
     STYLING: If the pattern has a core tradeoff or constraint, use > [!warning].
     If there is a taxonomy (types, tiers, modes), use > [!abstract] with a table. -->

## Instances

<!-- 2+ specific examples from the wiki. Reference pages directly.
     STYLING: Use > [!example]- foldable per instance for detailed breakdowns.
     A summary table at the top (instance | how it implements pattern) is ideal. -->

## When To Apply

<!-- Conditions that make this pattern appropriate.
     STYLING: > [!tip] for the positive cases. -->

## When Not To

<!-- Anti-patterns, conditions where this fails or is counterproductive.
     STYLING: > [!warning] for the negative cases. -->

## Relationships

- DERIVED FROM: {{derived_page_1}}
- DERIVED FROM: {{derived_page_2}}

---
title: "{{title}}"
type: note
domain: {{domain}}
note_type: {{note_type}}
status: synthesized
confidence: medium
created: {{date}}
updated: {{date}}
sources: []
tags: []
---

# {{title}}

<!-- NOTE TYPE determines structure. Pick one:
     - directive: operator instruction — verbatim quotes, interpretation, action items
     - session: session record — decisions made, artifacts produced, state changes
     - completion: task/stage completion — what passed, what concerns, what's next
-->

## Summary

<!-- What happened, what was decided, or what was directed.
     Notes are short — MIN 10 words. MAX 3 sentences. -->

<!-- ═══ DIRECTIVE NOTE STRUCTURE ═══ -->
<!-- Use this structure when note_type: directive -->

## Operator Directive

<!-- VERBATIM operator words. Quote exactly. Do not paraphrase.
     Use > blockquote for each distinct statement.
     STYLING: > [!warning] for critical directives, plain > for standard. -->

> "{{verbatim operator words here}}"

## Interpretation

<!-- YOUR interpretation of what the directive means.
     Clearly separated from the verbatim section.
     What does this change about how we work? -->

## Action Items

<!-- Numbered list of concrete actions this directive requires.
     Each item: specific, verifiable, tied to a file or system. -->

1. {{action}}

<!-- ═══ SESSION NOTE STRUCTURE ═══ -->
<!-- Use this structure when note_type: session -->

## Decisions Made

<!-- Numbered list of decisions with brief rationale.
     Format: Decision — because reason. -->

## Artifacts Produced

<!-- Table: artifact | path | status -->

| Artifact | Path | Status |
|----------|------|--------|
| {{name}} | {{path}} | {{done/partial/blocked}} |

## State Changes

<!-- What changed in the wiki, configs, tools, or backlog.
     Metrics before → after where possible. -->

<!-- ═══ COMPLETION NOTE STRUCTURE ═══ -->
<!-- Use this structure when note_type: completion -->

## What Was Done

<!-- Brief description of the completed work.
     Reference task ID if applicable. -->

## Validation

<!-- What gates passed? Pipeline post output? Test results?
     STYLING: > [!success] for passes, > [!bug] for issues found. -->

## Concerns Raised

<!-- Any concerns filed during this work.
     If none: "No concerns filed." -->

## Next Steps

<!-- What should happen after this completion.
     What work does this unblock? -->

## Relationships

- RELATES TO: {{related_page}}

---
title: "AICP identity-profile.md needs reconciliation per consumer-property doctrine + outdated facts"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [contributed, correction]
contributed_by: "aicp-self"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: 2026-04-17
contribution_status: pending-review
contribution_reason: "Brain's identity-profile.md predates the consumer-property doctrine (2026-04-15) and needs reconciliation. AICP now declares identity per latest doctrine in its CLAUDE.md."
---

# AICP identity-profile.md needs reconciliation per consumer-property doctrine + outdated facts

## Summary

Target page: wiki/ecosystem/project_profiles/aicp/identity-profile.md (created 2026-04-13).

DOCTRINE VIOLATIONS (post-doctrine 2026-04-15):

1. Identity table at lines 26-38 hardcodes 'Execution Mode: Solo' as a project field. Violates wiki/lessons/01_drafts/execution-mode-is-consumer-property-not-project-property.md (2026-04-15) which establishes execution mode is a CONSUMER property. Solo is the default; harness/fleet declares non-default at MCP connect.

2. Same Identity table hardcodes 'SDLC Profile: Simplified'. Same doctrine violation. Also: a production-phase + medium-scale project would default to 'default' (Goldilocks), not 'simplified'.

OUTDATED FACTS (as of 2026-04-17):

3. Scale: profile says '~60 modules'. Current: 61 Python modules in aicp/, 94 test files, 1,758 tests (was 1,631), 78 skills, 9 profiles, 14 model configs.

4. Phase: profile says 'Stage 1 complete, Stage 2 implemented'. Current: Stage 2 routing operational (4-tier router with circuit breakers + DLQ + warmup deployed); Stage 3 hardware unlocked 2026-04-17 (19GB VRAM dual-GPU).

ADOPTION STATUS:

5. 'Wiki knowledge base: Partial' and 'Feed-back TO second brain: Minimal' (lines 92-101). As of 2026-04-17, AICP has tools/gateway.py forwarder and reached Tier 4/4 STRUCTURAL compliance per gateway compliance check. Operational compliance is Tier 2+ (honest reporting per Structural Compliance Is Not Operational Compliance).

NEW KNOWLEDGE GAP:

6. Add to 'Knowledge Gaps' (lines 105-113): 'Empirical routing split with 19GB hardware (Stage 3 hardware just unlocked, measurements pending).' Connects to Local AI open question.

CORRECTED IDENTITY PER DOCTRINE:

Stable: type=product (backend AI platform); domain=backend-ai-platform-python; second-brain=connected.
State: phase=production — Stage 2 routing operational, Stage 3 hardware unlocked 2026-04-17; scale=medium (61 modules, 94 test files, 1,758 tests, 78 skills, 9 profiles, 14 model configs).
Consumer/task properties (NOT in CLAUDE.md): execution mode default solo, SDLC profile default 'default' (Goldilocks), methodology model task-dependent.

Source: AICP CLAUDE.md Identity Profile section added 2026-04-17, parsed by gateway query_identity().

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-registry|Model Registry]]

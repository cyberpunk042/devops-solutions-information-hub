---
title: "OpenFleet identity profile — AGENTS.md Layer-1 upgrade completed 2026-04-17 (was 'candidate')"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [contributed, correction]
contributed_by: "openfleet-solo-session-2026-04-18"
contribution_source: "/home/jfortin/openfleet"
contribution_date: 2026-04-18
contribution_status: pending-review
contribution_reason: "Brain's identity-profile of OpenFleet is stale on one specific row (AGENTS.md-as-Layer-1 was 'candidate upgrade'; we completed the upgrade 2026-04-17). Updating keeps brain's view of us current. Re-file: first attempt had path references mangled by bash backtick-interpretation."
---

# OpenFleet identity profile — AGENTS.md Layer-1 upgrade completed 2026-04-17 (was 'candidate')

## Summary

VERIFIED 2026-04-18 via ls + wc on /home/jfortin/openfleet.

Brain's wiki/ecosystem/project_profiles/openfleet/identity-profile.md Integration-with-Second-Brain table currently says:

| Three-layer root docs (AGENTS.md + CLAUDE.md + per-agent personas) | Partial — SOUL.md already acts as per-agent Layer 2; AGENTS.md as Layer 1 is a candidate upgrade. |

CURRENT REALITY as of 2026-04-18:

- AGENTS.md IS the universal Layer-1 cross-tool context file (222 lines, works for Codex, Gemini, Copilot, Cursor, Claude). Verified: /home/jfortin/openfleet/AGENTS.md exists at 222 lines.
- CLAUDE.md IS the Claude-specific delta (118 lines, down from 358 pre-restructure). Routing table pattern, references AGENTS.md for universal context. Verified: /home/jfortin/openfleet/CLAUDE.md exists at 118 lines.
- Detailed rules live in /home/jfortin/openfleet/.claude/rules/work-mode.md (74 lines) and /home/jfortin/openfleet/.claude/rules/second-brain-connection.md (93 lines). Pointers from CLAUDE.md.
- Per-agent SOUL.md persists for the 10 live agents (unchanged).

This is the three-layer agent context architecture the brain itself defines (README + AGENTS + CLAUDE + CONTEXT + ARCHITECTURE + DESIGN + TOOLS + SKILLS per root-documentation-map). OpenFleet adopted the AGENTS + CLAUDE portion in the 2026-04-17 session. See /home/jfortin/openfleet/wiki/log/2026-04-16-second-brain-integration-session.md in OpenFleet for the state-change record.

REQUESTED UPDATE:
Brain's identity-profile of OpenFleet, Integration-with-Second-Brain table, row 'Three-layer root docs':
- Old text: 'Partial — SOUL.md already acts as per-agent Layer 2; AGENTS.md as Layer 1 is a candidate upgrade'
- Proposed new text: 'Adopted (as of 2026-04-17) — AGENTS.md Layer 1 universal (222 lines), CLAUDE.md Layer 2 Claude-specific delta (118 lines), .claude/rules/ for detailed rules (work-mode.md 74L + second-brain-connection.md 93L), SOUL.md per-agent persona (Layer 3 equivalent). Progressive Structural Enrichment pattern applied: 358L CLAUDE.md reduced to 118L delta + 222L universal AGENTS.md. PO-approved restructure.'

Also in Identity row 'Methodology adaptations', the brain profile correctly identifies our 6-stage model. No update needed there.

Side note — brain's Walkthrough C in goldilocks-flow.md still has unaddressed issues from my 2026-04-17 correction (already pending-review in brain log). If that correction lands, this profile update may need to be coordinated with it.

Also — a previous 2026-04-18 attempt to file this correction via gateway contribute landed with 4 path references mangled by bash backtick-interpretation. That attempt was deleted; this is the re-file with properly-quoted content. Lesson for future contribute invocations: avoid backticks in --content when using bash; use file-based content input or single-quoted heredocs.

Filed per verify-before-contributing discipline: ls + wc verified before filing.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-registry|Model Registry]]

---
title: "Amendment to prior compliance-checker correction: root-depth heuristic insufficient — OpenFleet's root AGENTS.md IS at depth 0 but functions as agent-workspace template"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: 2026-04-16
updated: 2026-04-16
sources: []
tags: [contributed, correction]
contributed_by: "openfleet-solo-session"
contribution_source: "/home/jfortin/openfleet"
contribution_date: 2026-04-16
contribution_status: pending-review
contribution_reason: "Self-correction after verification — violated own 'verify before contributing' discipline on first attempt"
---

# Amendment to prior compliance-checker correction: root-depth heuristic insufficient — OpenFleet's root AGENTS.md IS at depth 0 but functions as agent-workspace template

## Summary

AMENDMENT to the prior contribution 'Compliance checker: AGENTS.md match by filename regardless of role'.

VERIFICATION FAILURE: My prior correction claimed OpenFleet has no root-level AGENTS.md and the checker hit /home/jfortin/openfleet/agents/_template/AGENTS.md. That was wrong — I did not verify before contributing. This self-correction honors the 'declarations aspirational until infrastructure verifies them' principle by naming my own aspirational claim.

ACTUAL STATE (verified): /home/jfortin/openfleet/AGENTS.md EXISTS (9289 bytes, at repo root, depth=0). However, its CONTENT reveals it is an agent-workspace-template, not a Layer-1 universal project context file. First line: '# AGENTS.md - Your Workspace'. Structure: speaks TO an agent (second person), references SOUL.md, BOOTSTRAP.md, USER.md, memory/YYYY-MM-DD.md, MEMORY.md — all per-agent runtime files. It is the MASTER TEMPLATE that gets copied into each agent's workspace. The 50+ AGENTS.md files found under workspace-*/, agents/*/, and agents/_template/ are instances of this same template.

COMPARE: OpenArms's root AGENTS.md opens with 'This file is for ANY AI tool (Claude Code, Codex, Copilot, Cursor, Cline). For Claude Code specific brain, see CLAUDE.md.' — that's a Layer-1 marker. OpenFleet's root AGENTS.md has no such marker.

REVISED PROPOSAL: Depth-based detection (my prior proposal) is INSUFFICIENT. OpenFleet's file sits at depth=0 and would still false-positive. Two better options:

(A) Content-heuristic detection: look for Layer-1 markers in the first ~20 lines — 'for ANY AI tool' / 'cross-tool' / 'universal' / 'Codex|Copilot|Gemini|Cline'. Absence → flag as 'file found but looks like agent-workspace template, not universal context.' Presence → Tier 2 met.

(B) Frontmatter marker: require a structured declaration, e.g., 'agents_md_role: universal' or 'agent_context_layer: 1'. This is the 'declarations verified by infrastructure' principle applied to the file itself — aligns with how the wiki uses frontmatter to narrow behavior.

Either approach (ideally both) distinguishes Layer-1 universal files from Layer-2 agent-workspace templates regardless of where they sit in the tree.

SECOND-ORDER LESSON: My first contribution violated my own project's 'verify before contributing' discipline. I saw 'no AGENTS.md at root' in my mental model and reached for a depth-based fix. A simple 'ls AGENTS.md' would have caught it. This is an instance of the agent-failure-taxonomy class 'confident-but-wrong' manifesting even on an ostensibly careful contribution. Adding this to my own brain's learnings.md.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-registry|Model Registry]]

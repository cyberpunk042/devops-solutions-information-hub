---
title: "Cascade candidate — M001 reframe: audit (not author) existing AGENTS.md (34KB) + CLAUDE.md (38KB) at upstream root-ghostproxy"
type: note
domain: cross-domain
status: draft
confidence: high
created: 2026-05-16
updated: 2026-05-16
last_reviewed: 2026-05-16
authored: 2026-05-16T00:16:00-04:00
note_type: directive
authorship: agent-authored
profile: root-ghostproxy-rollout
cascade_target: root-ghostproxy
target_module: M001
target_epic: root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05
supersedes_premise_of: wiki/backlog/modules/root-ghostproxy-m001-author-claude-md-and-agents-md.md
companion_to: wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-state-divergence-upstream-already-advanced-2026-05-16.md
sources:
  - id: m001
    type: wiki
    file: wiki/backlog/modules/root-ghostproxy-m001-author-claude-md-and-agents-md.md
    description: "Module dated 2026-05-04. Done When says: AGENTS.md < 100 lines, CLAUDE.md < 200 lines, both authored from second-brain templates."
  - id: gh-snapshot
    type: gh-api-read-only
    file: repos/cyberpunk042/root-ghostproxy/contents/AGENTS.md + CLAUDE.md
    description: "Read-only snapshot 2026-05-16T04:08Z. AGENTS.md 34874 bytes / CLAUDE.md 37606 bytes — both exist; both far over M001 thresholds."
  - id: three-layer-agent-context
    type: wiki
    file: wiki/spine/models/agent-config/model-skills-commands-hooks.md
    description: "Reference standard for three-layer agent context — AGENTS.md universal cross-tool, CLAUDE.md Claude Code routing, skills auto-trigger."
tags:
  - cascade-candidate
  - root-ghostproxy
  - m001
  - audit-not-author
  - three-layer-context
  - cross-project-cascade
  - sprint
related:
  - wiki/backlog/modules/root-ghostproxy-m001-author-claude-md-and-agents-md.md
  - wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-state-divergence-upstream-already-advanced-2026-05-16.md
  - wiki/spine/models/agent-config/model-skills-commands-hooks.md
---

# Cascade candidate — M001 reframe: audit (not author) existing AGENTS.md + CLAUDE.md at upstream root-ghostproxy

## Summary

M001 (dated 2026-05-04) was authored against the premise that `/root/AGENTS.md` and `/root/CLAUDE.md` did not yet exist and needed to be created from second-brain templates with `< 100` and `< 200` line targets respectively. Read-only snapshot 2026-05-16T04:08Z shows BOTH files already exist on `cyberpunk042/root-ghostproxy main` — AGENTS.md at 34874 bytes (sha 90edf8bd) and CLAUDE.md at 37606 bytes (sha e207b135). Conservative line estimate (~70 chars/line) puts AGENTS.md near ~500 lines and CLAUDE.md near ~540 lines — between 2.5× and 5.4× over the M001 size discipline. This candidate proposes reframing M001's task list from "draft + land + approve" to "fetch (read-only) + audit + diff + propose specific delta-patches" — preserving the upstream work while flagging concrete trim/move/split recommendations against the three-layer agent context standard. The operator decides whether M001 should be marked SUPERSEDED-IN-PLACE with this reframed task list, or kept as-is and a new module M001b filed instead.

## Operator-stated requirements (verbatim, sacrosanct)

> *"if you look into root-ghostproxy and probably even here in the second-brain there is already probably report of the situation and my request for the resolutions."* — operator, 2026-05-15

> *"some of the things root-ghostproxy were going to do its not just going to use the selfdef project. so root-ghostproxy can focus more on its thing."* — operator, 2026-05-15

> *"ME APPROVING THEM ONE BY ONE"* — operator working-contract referenced in M001 line "Operator approves both files before they land at /root (per 'ME APPROVING THEM ONE BY ONE' contract)"

## Proposed reframed task list (delta against current M001)

| Current M001 task | Proposed reframe |
|---|---|
| T-M001-1: Operator decides scope and tone for AGENTS.md | KEEP. Still needed — the existing AGENTS.md may not match what operator wants. |
| T-M001-2: Draft `/root/AGENTS.md` based on operator-confirmed scope | REPLACE with: Read upstream AGENTS.md via `gh api` (read-only); audit against three-layer-context standard + < 100 line target; produce delta-recommendation page (what to trim, what to move into SKILLS.md / CONTEXT.md / docs/, what to inline). |
| T-M001-3: Draft `/root/CLAUDE.md` with routing table | REPLACE with: Read upstream CLAUDE.md via `gh api` (read-only); audit against CLAUDE.md structural patterns + < 200 line target; produce delta-recommendation page. |
| T-M001-4: Operator reviews + approves drafts | KEEP, retargeted: operator reviews the delta-recommendations (not full rewrites). Approves per-recommendation. |
| T-M001-5: Land both files at /root after approval | REPLACE with: Operator (or future-session-inside-root-ghostproxy) APPLIES approved deltas to existing files. This Profile NEVER lands content at /root. |
| T-M001-6: Decide reconciliation for prior /root artefacts | EXPAND: now covers 9 additional uppercase root-docs (ARCHITECTURE.md, BOOTSTRAP.md, CONTEXT.md, DESIGN.md, SECURITY.md, SKILLS.md, TOOLS.md) + new directories (wiki/, docs/, tools/, scripts/, templates/, .mcp.json) that the original M001 did not anticipate. Likely splits into M001b. |

## Specific delta-recommendation framework (proposed deliverable shape)

For each of AGENTS.md and CLAUDE.md, produce a delta-recommendation page at `wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-<file>-delta-recommendations-<date>.md` with:

1. **Three-layer-context conformance check** — does this file stay in its lane (AGENTS.md = universal cross-tool, CLAUDE.md = Claude Code-specific routing) or does content bleed across layers?
2. **Size discipline check** — by section, what could move to a sibling file (SKILLS.md, CONTEXT.md, docs/, README.md) to reach the M001 line targets? Per-section budgets, not arbitrary trims.
3. **Sacrosanct-directive preservation** — verify operator-stated directives are quoted verbatim and prominently placed (per AGENTS.md hard rule "Operator words are SACROSANCT — quote verbatim").
4. **Hard-rules inventory** — list every rule the file enforces; flag duplicates (within file or across files) for de-duplication.
5. **Routing-table verification (CLAUDE.md only)** — every routed intent must have a destination tool/page that actually exists in upstream (verify via `gh api`).
6. **Anti-pattern scan** — look for project-conflation framing, scope-decisions made in prose, "is really about" reframings (per AGENTS.md sacrosanct rule "you DO NOT decide what root-ghostproxy is").

## Alternative Visions

### Vision A — Reframe M001 in place (mark SUPERSEDED-IN-PLACE)

Operator edits `wiki/backlog/modules/root-ghostproxy-m001-author-claude-md-and-agents-md.md` to replace Done When + Tasks per the above table. Title stays. Old tasks moved to a "Historical context (pre-2026-05-15 commits)" appendix. Single source of truth preserved.

Trade-offs: (+) one canonical M001; (–) loses the 2026-05-04 framing for posterity; (–) operator-territory edit (this Profile cannot do it).

### Vision B — File new module M001b (M001 stays as historical scaffold)

Operator files `wiki/backlog/modules/root-ghostproxy-m001b-audit-existing-claude-md-and-agents-md.md` with the reframed task list. M001 stays as-is (status: stale-premise) for historical reference. M001b becomes the ACTIVE Scaffold-tier work item.

Trade-offs: (+) preserves 2026-05-04 record; (+) explicit historical/active split; (–) two pages to maintain; (–) downstream relationships (M007 "BLOCKED BY M001") must be re-targeted.

### Vision C — Defer M001 disposition pending Vision-A/B/C/D pick on parent state-divergence candidate

Operator first decides the parent state-divergence disposition (cascade-candidate-...-state-divergence-2026-05-16.md, Vision A | B | C | D). M001's reframe shape derives from that pick (e.g., if parent Vision B "pause epic + rewrite," M001 doesn't get reframed — it gets replaced wholesale).

Trade-offs: (+) avoids deciding child before parent; (+) cleanest dependency order; (–) blocks this candidate's resolution on the parent.

## Context Boundaries

- This Profile does NOT decide between Visions A / B / C. Operator picks.
- This Profile does NOT pre-fetch + audit AGENTS.md / CLAUDE.md content this tick (that would require `gh api` byte-fetch + base64-decode + content inspection of a sister-project file — a more invasive read than the metadata-only snapshot done at Step 3, and probably warrants explicit operator authorization for "how invasive is read-only" per Profile TOOLS.md).
- This Profile does NOT touch root-ghostproxy. Any landed deltas are operator's or future-session-inside-root-ghostproxy's action.
- This Profile does NOT decide what AGENTS.md "should contain" — only flags conformance against the existing three-layer-context standard already in this second brain.
- The "< 100 / < 200" line targets come from M001 itself; if those targets are themselves wrong for a type=root group=operating-system-setup project at its current SFIF tier, that's a separate scope-clarification surfacing (see companion candidates this tick).

## Cascade Marker

- `cascade: root-ghostproxy`
- `target_module: M001`
- `decision_needed: m001-reframe-vision (A | B | C)`
- `depends_on: parent state-divergence candidate disposition`
- `operator_action: pick vision A/B/C in operator-decision-queue.md (Q87)`

## Relationships

- BUILDS ON: [[cascade-candidate-root-ghostproxy-state-divergence-upstream-already-advanced-2026-05-16|Parent state-divergence cascade-candidate]]
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] — three-layer-context standard against which audit conforms

## Backlinks

[[Parent state-divergence cascade-candidate]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]

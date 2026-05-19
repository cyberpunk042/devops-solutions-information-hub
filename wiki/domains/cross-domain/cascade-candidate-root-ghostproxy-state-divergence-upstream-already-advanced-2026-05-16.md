---
title: "Cascade candidate — root-ghostproxy upstream state has materially diverged from second-brain epic+modules (snapshot 2026-05-16 00:08 ET)"
type: note
domain: cross-domain
status: draft
confidence: high
created: 2026-05-16
updated: 2026-05-16
last_reviewed: 2026-05-16
authored: 2026-05-16T00:14:00-04:00
note_type: directive
authorship: agent-authored
profile: root-ghostproxy-rollout
cascade_target: root-ghostproxy
target_module: M001
target_epic: root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05
decision_needed: state-divergence-disposition
sources:
  - id: gh-snapshot-2026-05-16
    type: gh-api-read-only
    file: repos/cyberpunk042/root-ghostproxy/contents/
    description: "Read-only GitHub API listing of root-ghostproxy main branch at 2026-05-16T04:08Z. SHA of head commit bf248fe (Merge PR #1) pushed 2026-05-15T17:27:06Z."
  - id: epic-record
    type: wiki
    file: wiki/backlog/epics/pre-milestone/root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05.md
    description: "Second-brain epic dated 2026-05-04. Stream 2 Scaffold premise: AGENTS.md and CLAUDE.md must be authored."
  - id: m001
    type: wiki
    file: wiki/backlog/modules/root-ghostproxy-m001-author-claude-md-and-agents-md.md
    description: "M001 premise: AGENTS.md < 100 lines, CLAUDE.md < 200 lines, both authored from second-brain templates."
  - id: directive-2026-05-04
    type: wiki
    file: raw/notes/2026-05-04-prepare-root-ghostproxy-as-sister-type-root-group-operating-system-setup.md
    description: "Operator directive — preparation only; future-session work; sacrosanct verbatim."
tags:
  - cascade-candidate
  - root-ghostproxy
  - state-divergence
  - upstream-snapshot
  - multi-vision
  - cross-project-cascade
  - sprint
related:
  - wiki/backlog/epics/pre-milestone/root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05.md
  - wiki/backlog/modules/root-ghostproxy-m001-author-claude-md-and-agents-md.md
  - wiki/config/sister-projects.yaml
---

# Cascade candidate — root-ghostproxy upstream state has materially diverged from second-brain epic+modules (snapshot 2026-05-16 00:08 ET)

## Summary

The second-brain's record of root-ghostproxy (epic + 10 modules dated 2026-05-04) assumes a Scaffold-tier project requiring CLAUDE.md / AGENTS.md authoring, methodology layer decision, and tooling buildout. Read-only `gh api` snapshot at 2026-05-16T04:08Z shows the upstream `cyberpunk042/root-ghostproxy` `main` branch has already advanced past most of those Scaffold premises. AGENTS.md (34874 bytes) and CLAUDE.md (37606 bytes) both exist at repo root — both ORDERS OF MAGNITUDE over M001's `< 100 lines / < 200 lines` thresholds. The repo also contains `wiki/`, `tools/`, `docs/`, `scripts/`, `templates/`, `.mcp.json`, plus seven uppercase root-doc files (ARCHITECTURE.md, BOOTSTRAP.md, CONTEXT.md, DESIGN.md, SECURITY.md, SKILLS.md, TOOLS.md) — none of which the second-brain record anticipates. Head commit `bf248fe` ("Merge pull request #1 from cyberpunk042/claude/install-view-and-questions-skills") pushed 2026-05-15T17:27:06Z, four hours before the operator's sprint directive arrived. This is the FIRST and HIGHEST-PRIORITY finding of the sprint and must inform every subsequent module-draft decision.

## Operator-stated requirements (verbatim, sacrosanct)

> *"if you look into root-ghostproxy and probably even here in the second-brain there is already probably report of the situation and my request for the resolutions."* — operator, 2026-05-15

> *"some of the things root-ghostproxy were going to do its not just going to use the selfdef project. so root-ghostproxy can focus more on its thing."* — operator, 2026-05-15

> *"create a hard working AI assistant for tonight that will make sure that the root-ghostproxy is in a complete new state in the morning on my machine"* — operator, 2026-05-15

## Evidence (inline, verbatim from gh API read-only call)

```
$ gh api repos/cyberpunk042/root-ghostproxy/contents/ --jq '.[] | .name'
.claude
.claudeignore
.config
.gitignore
.mcp.json
AGENTS.md
ARCHITECTURE.md
BOOTSTRAP.md
CLAUDE.md
CONTEXT.md
DESIGN.md
LICENSE
README.md
SECURITY.md
SKILLS.md
TOOLS.md
docs
install.sh
open-interfaces.template
scripts
templates
tools
uninstall.sh
wiki

$ gh api repos/cyberpunk042/root-ghostproxy/contents/AGENTS.md --jq '{size: .size, sha: .sha}'
{"sha":"90edf8bdbe9112f5e563bb16c3022acf11e036c3","size":34874}

$ gh api repos/cyberpunk042/root-ghostproxy/contents/CLAUDE.md --jq '{size: .size, sha: .sha}'
{"sha":"e207b135fd99af35f75a4b5e3bddfdb125ed0000","size":37606}

$ gh api repos/cyberpunk042/root-ghostproxy/commits --jq '.[0:3] | .[] | {sha,date,msg}'
{"sha":"bf248fe...","date":"2026-05-15T17:27:06Z","msg":"Merge pull request #1 from cyberpunk042/claude/install-view-and-questions-skills"}
{"sha":"430dd30...","date":"2026-05-15T17:19:13Z","msg":"install: /view + /questions skills + auto-compact OFF / auto-dream ON"}
{"sha":"0fae9c0...","date":"2026-05-08T12:53:06Z","msg":"latest"}
```

## What this means for the sprint queue

The 10 modules (M001–M010) were authored 2026-05-04 against the Scaffold-tier premise. Upstream has moved past that premise without the second-brain noticing (no operator-directive note in `raw/notes/2026-05-04..2026-05-15` records the 2026-05-07/2026-05-08/2026-05-15 commits, and no cron tick observed root-ghostproxy between 2026-05-04 and tonight's sprint window). Drafting M001 as "author AGENTS.md from scratch" would be drafting against a stale premise.

This candidate does NOT decide the disposition. It surfaces the divergence to the operator with explicit options below.

## Alternative Visions

### Vision A — Audit-and-right-size (least invasive)

Reframe M001 from "author AGENTS.md + CLAUDE.md (don't exist)" to "audit and right-size existing AGENTS.md (34KB) + CLAUDE.md (38KB) against three-layer-context discipline + < 100 / < 200 line targets." Reread upstream files via `gh api .../contents/AGENTS.md` decoded base64, compare against `wiki/spine/models/agent-config/model-skills-commands-hooks.md` standards, surface specific trim/move recommendations. Treat the existing files as ground truth and propose deltas, not replacements.

Trade-offs:
- (+) Honors operator's "behave FROM the project, not OVER it" principle.
- (+) Cheapest path; preserves the prior session's work.
- (–) Requires module M001 to be marked SUPERSEDED-IN-PLACE with a new "audit" task list, which is an operator-territory edit.
- (–) Risks rubber-stamping a 34KB AGENTS.md that may itself contain anti-patterns.

### Vision B — Pause-the-epic, re-orient

Operator pauses the entire epic + 10 modules pending fresh observation: read upstream `AGENTS.md` + `CLAUDE.md` + `ARCHITECTURE.md` + `DESIGN.md` + `wiki/` contents in full, then rewrite the epic + modules from observed reality. The 2026-05-04 epic becomes a historical artifact (archived); a new 2026-05-16 epic supersedes it. The sprint becomes an "observe + rewrite epic" sprint, not a "draft modules" sprint.

Trade-offs:
- (+) Highest fidelity to actual state; no stale-premise drift.
- (+) Treats the upstream 2026-05-15 work as legitimate input, not noise.
- (–) Operator-territory: this Profile cannot rewrite the epic autonomously.
- (–) Loses sprint output (no cascade-candidates drafted this window).
- (–) Heavier read of upstream files (closer to mirroring; needs explicit operator authorization).

### Vision C — Parallel-track (epic-as-aspirational + upstream-as-actual)

Keep the 2026-05-04 epic as the operator's ASPIRATIONAL plan and treat the upstream `cyberpunk042/root-ghostproxy` `main` as the ACTUAL current implementation. Draft cascade-candidates per module by COMPARING the two: for each module, "operator asked for X (epic) — upstream shows Y (gh snapshot) — gap is Z (cascade draft)." This is the multi-vision discipline applied per-module, with the divergence treated as feature not bug.

Trade-offs:
- (+) Produces sprint output while honoring divergence; each module becomes a gap-diff.
- (+) Reusable substrate: every future cron tick produces a fresh gap-diff against upstream HEAD.
- (–) Per-tick cost ~2× (need to read both epic AND upstream).
- (–) Risks confusing the operator about which set of artifacts is canonical.

### Vision D — Operator-directive-required: do not proceed

The divergence is large enough that any drafting risks polluting the second brain with stale-premise candidates. This Profile pauses ALL module drafting for the sprint window and surfaces ONLY this state-divergence finding + one self-improvement candidate (autoadaptation: future ticks must read upstream HEAD before drafting). Operator decides next steps in the morning.

Trade-offs:
- (+) Honors P4 (Declarations Aspirational Until Verified) — the epic's verification gate has not been crossed.
- (+) Avoids the operator-flagged anti-pattern "do little change and stop with no rationale" by being explicit-stop-with-rationale.
- (–) Produces near-zero sprint output (the operator's anti-slow / anti-stop directives push against this).
- (–) Leaves the morning briefing with this single finding to react to.

## Context Boundaries

- This candidate is authored from a READ-ONLY snapshot (`gh api` GET requests only). No `gh api PATCH/POST/DELETE`, no `git push`, no `git clone`. The upstream repo is untouched.
- Cross-project boundary HELD: the only files written this tick are in this second-brain repo (`wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-*.md` + `wiki/backlog/operator-decision-queue.md` append).
- This candidate does NOT decide the disposition. It surfaces four options; operator picks.
- This candidate does NOT reframe what root-ghostproxy IS or what its "thing" is. It observes that upstream has additional content (uppercase root-docs, `.mcp.json`, `wiki/`) and reports the byte-count delta against the second-brain epic's premise. The semantic content of those upstream files is not interpreted here.
- The "complete new state in the morning" operator-directive is interpreted as "produce sprint output the operator can react to in the morning" — NOT as "this Profile decides what the new state should be." Decisions remain operator-territory.

## Cascade Marker

- `cascade: root-ghostproxy`
- `target_module: M001` (primary) + `M002`+`M003`+`M004`+`M005` (all blocked by same divergence — once disposition decided, downstream modules adapt accordingly)
- `target_epic: root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05`
- `decision_needed: state-divergence-disposition (A | B | C | D)`
- `operator_action: choose vision A/B/C/D in operator-decision-queue.md (Q86)`

## Relationships


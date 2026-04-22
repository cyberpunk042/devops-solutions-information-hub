---
title: "E009 M003 — Skill Portability (port 3 top skills to OpenCode format)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 75
progress: 0
stages_completed: [document]
artifacts: []
epic: "E009"
depends_on:
  - "E009-m001"
confidence: medium
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e009-harness-neutrality-and-opencode-parity
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E009-harness-neutrality-and-opencode-parity.md
  - id: claude-skills-dir
    type: repository
    file: /home/jfortin/devops-solutions-research-wiki/.claude/skills
tags: [module, p1, e009, skills, opencode, portability, adapter, continue, ingest, log]
---

# E009 M003 — Skill Portability

## Summary

Port 3 of the operator's highest-use skills from `.claude/skills/` to OpenCode's equivalent format. Candidate skills (by recent usage + operator emphasis): `continue` (resume mission), `ingest` (research wiki ingestion), `log` (add log entry). For each, either: (a) OpenCode accepts the same markdown+frontmatter format directly → thin symlink/copy suffices, or (b) OpenCode needs a different format → write a translator + regenerate. Surface any irreducible Claude-specific features as input to the Harness Contract (M004).

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T051 | Audit OpenCode's skill/agent format + invocation convention | 80% | 0% | draft |
| T052 | Port `continue` skill (or write OpenCode equivalent) | 75% | 0% | draft |
| T053 | Port `ingest` and `log` skills | 70% | 0% | draft |
| T054 | Side-by-side session: same task, both harnesses, compare artifacts | 75% | 0% | draft |

## Dependencies

- **E009 M001** — OpenCode launchable.
- **E009 M002** — MCP continuity proven (skills call MCP tools internally).
- `.claude/skills/continue/`, `.claude/skills/ingest/`, `.claude/skills/log/` readable (existing in repo).

## Done When

- [ ] OpenCode skill format documented in `wiki/log/2026-04-24-opencode-skill-format.md` — fields, invocation syntax, args passing, hooks
- [ ] `continue` skill: functionally equivalent behavior in OpenCode — command → diagnostics → state → next-action options
- [ ] `ingest` skill: functionally equivalent ingestion flow in OpenCode
- [ ] `log` skill: functionally equivalent log-add flow in OpenCode
- [ ] Side-by-side POC: "scaffold a pattern page for X and validate with pipeline post" — both harnesses complete successfully, artifacts diff'd
- [ ] Divergences list: features that don't port cleanly (e.g., Claude-specific tool names, hook event names, args schema)
- [ ] Adapter layer / translator script (if needed) at `tools/port_skill_to_opencode.py`
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Audit OpenCode's skill model

```bash
opencode --help
opencode skills --help 2>&1 || opencode agents --help 2>&1 || true
ls ~/.opencode/
# Read OpenCode docs: https://github.com/sst/opencode for skill/agent docs

# Capture: file layout, frontmatter fields, args schema, invocation command
```

### Step 2 — Port continue

```bash
# If same markdown+frontmatter format:
mkdir -p ~/.opencode/skills/continue
cp -r .claude/skills/continue/* ~/.opencode/skills/continue/
# Or, per OpenCode docs, mirror to a .opencode/skills/ dir in repo

# If different format: write a thin OpenCode agent that invokes the same MCP tools
```

### Step 3 — Port ingest, log

Same approach as Step 2. Document any field-by-field translation needed.

### Step 4 — Side-by-side POC

```bash
cd /home/jfortin/devops-solutions-research-wiki

# Run via Claude Code
claude
# > /log "side-by-side POC test from claude"
# /exit

# Run via OpenCode
opencode
# > /log "side-by-side POC test from opencode"     (or whatever OpenCode's invocation syntax is)
# /exit

# Compare
git diff wiki/log/
python3 -m tools.pipeline post
```

Both should produce validating log pages with equivalent content.

### Step 5 — Publish results

```bash
python3 -m tools.pipeline scaffold note "2026-04-24-opencode-skill-portability-poc"
$EDITOR wiki/log/2026-04-24-opencode-skill-portability-poc.md
python3 -m tools.pipeline post
```

## Rollback

```bash
rm -rf ~/.opencode/skills
# Primary Claude Code session unaffected
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| OpenCode's skill format may diverge significantly | external | 2026-04-22 | no | Write a translator script; likely worth the ~2-4h investment |
| Skill invocation convention (`/skill-name args`) may differ | external | 2026-04-22 | no | Capture convention in Harness Contract; skills become portable via adapter |
| Some skills depend on Claude-specific tool names (e.g., TodoWrite) | design | 2026-04-22 | no | Harness Contract names abstract equivalents; harnesses adapt |

## Relationships

- PART OF: [[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]
- DEPENDS ON: [[e009-m001-opencode-install-and-base-config|e009-m001-opencode-install-and-base-config]]
- DEPENDS ON: [[e009-m002-mcp-server-continuity|e009-m002-mcp-server-continuity]]
- FEEDS INTO: [[e009-m004-harness-contract-document|e009-m004-harness-contract-document]]

## Backlinks

[[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]
[[e009-m001-opencode-install-and-base-config|e009-m001-opencode-install-and-base-config]]
[[e009-m002-mcp-server-continuity|e009-m002-mcp-server-continuity]]
[[e009-m004-harness-contract-document|e009-m004-harness-contract-document]]

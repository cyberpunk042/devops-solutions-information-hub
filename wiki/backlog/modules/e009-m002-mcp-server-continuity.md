---
title: "E009 M002 — MCP Server Continuity (research-wiki, claude-mem, plannotator)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 85
progress: 0
stages_completed: [document]
artifacts: []
epic: "E009"
depends_on:
  - "E009-m001"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e009-harness-neutrality-and-opencode-parity
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E009-harness-neutrality-and-opencode-parity.md
  - id: mcp-spec
    type: repository
    url: https://github.com/modelcontextprotocol/specification
    title: "Model Context Protocol specification"
tags: [module, p1, e009, mcp, opencode, research-wiki, claude-mem, plannotator, continuity]
---

# E009 M002 — MCP Server Continuity

## Summary

Prove the three MCP servers used in the primary Claude Code session are reachable + usable from OpenCode too. This validates the "MCP as harness-neutral contract" claim: any MCP-compliant harness should see identical tools. Servers: `research-wiki` (this repo's backlog/query tools), `claude-mem` (semantic memory), `plannotator` (planning helper). If any server is bound to Claude-specific auth or transport, this module surfaces that as a gap — fix or document.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T048 | Translate .mcp.json to OpenCode's MCP config format | 85% | 0% | draft |
| T049 | Smoke each server from OpenCode (list tools + one live call per server) | 90% | 0% | draft |
| T050 | Document any Claude-specific behaviors that don't port | 80% | 0% | draft |

## Dependencies

- **E009 M001** — OpenCode installed and launchable.
- Existing `.mcp.json` in the wiki root (Claude Code convention).
- MCP servers running / launchable via their usual commands (stdio or HTTP).

## Done When

- [ ] OpenCode's MCP config points at the same three servers (format may differ — wrapper/translation acceptable)
- [ ] Inside OpenCode, listing available MCP tools shows >20 tools from `research-wiki` (parity with Claude Code's exposure)
- [ ] Live call: `research-wiki:wiki_status` (or equivalent) returns current wiki state — identical to what Claude Code shows
- [ ] Live call: `claude-mem` search or observation fetch returns expected memory content
- [ ] Live call: `plannotator` does one round-trip successfully
- [ ] `wiki/log/2026-04-23-opencode-mcp-continuity.md` records each server's result, any translation required, any Claude-specific behavior that doesn't port
- [ ] Gap list published — what future work, if any, makes MCP fully harness-neutral
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Inspect Claude's .mcp.json

```bash
cd /home/jfortin/devops-solutions-research-wiki
cat .mcp.json | jq
# Capture: each server's transport (stdio / http), command, args, env
```

### Step 2 — Translate to OpenCode format

OpenCode uses its own config schema (check its docs). Tentative mapping:

```json
{
  "mcp": {
    "research-wiki": {
      "type": "local",
      "command": ["python3", "-m", "tools.mcp_server"],
      "env": {}
    },
    "claude-mem": {
      "type": "local",
      "command": ["claude-mem", "mcp-serve"]
    },
    "plannotator": {
      "type": "local",
      "command": ["plannotator", "mcp-serve"]
    }
  }
}
```

Insert into `~/.opencode/opencode.json` under the appropriate section.

### Step 3 — Smoke each server

```bash
cd /home/jfortin/devops-solutions-research-wiki
opencode

# Inside OpenCode session:
# /mcp list     (expect 3 servers, ~20+ tools)
# > use research-wiki:wiki_status
# > use claude-mem:search "operator"
# > use plannotator:<some basic call>
# /exit
```

### Step 4 — Compare against Claude Code

Run equivalent calls from Claude Code in another terminal, diff the outputs. Same tool → same result means MCP continuity holds. Differences → gap list.

### Step 5 — Author continuity log

```bash
python3 -m tools.pipeline scaffold note "2026-04-23-opencode-mcp-continuity"
$EDITOR wiki/log/2026-04-23-opencode-mcp-continuity.md
# Table: server | works-in-OC? | works-in-CC? | notes
python3 -m tools.pipeline post
```

## Rollback

```bash
# Remove the mcp block from opencode.json if server doesn't work there
$EDITOR ~/.opencode/opencode.json
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| OpenCode's MCP config format may lag the spec | external | 2026-04-22 | no | Pin a version; contribute a translator if needed |
| Some tools may return Claude-specific content (e.g., memory paths) | design | 2026-04-22 | no | Add abstraction in research-wiki server to normalize paths |
| claude-mem may require Claude-specific auth | external | 2026-04-22 | no | Either add harness-neutral token or fork/adapt |

## Relationships

- PART OF: [[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]
- DEPENDS ON: [[e009-m001-opencode-install-and-base-config|e009-m001-opencode-install-and-base-config]]
- FEEDS INTO: [[e009-m004-harness-contract-document|e009-m004-harness-contract-document]]

## Backlinks

[[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]
[[e009-m001-opencode-install-and-base-config|e009-m001-opencode-install-and-base-config]]
[[e009-m004-harness-contract-document|e009-m004-harness-contract-document]]

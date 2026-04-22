---
title: "E009 M001 — OpenCode Install and Base Config (OpenRouter K2.6 wired)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 90
progress: 0
stages_completed: [document]
artifacts: []
epic: "E009"
depends_on:
  - "E007-m002"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e009-harness-neutrality-and-opencode-parity
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E009-harness-neutrality-and-opencode-parity.md
  - id: opencode-repo
    type: repository
    url: https://github.com/sst/opencode
    title: "sst/opencode"
tags: [module, p1, e009, opencode, install, config, openrouter, k2-6, harness-neutral]
---

# E009 M001 — OpenCode Install and Base Config

## Summary

Install OpenCode (sst/opencode), a TUI AI coding agent that shares much of Claude Code's design surface (agents, MCP, hooks). Configure it against the same research-wiki working directory as the primary Claude Code session, and wire it to route through OpenRouter K2.6 (same inference path as E007 proved). Entirely runnable today — no hardware / RAM dependency.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T045 | Install OpenCode binary + verify `opencode --version` | 100% | 0% | draft |
| T046 | Author ~/.opencode/opencode.json pointing at wiki working dir | 95% | 0% | draft |
| T047 | Configure OpenRouter K2.6 as default provider + smoke session | 90% | 0% | draft |

## Dependencies

- **E007 M002** — OpenRouter route proven (smoke tests DONE 2026-04-22); OpenRouter key at `/home/jfortin/devops-expert-local-ai/.env`.
- Node.js 18+ (OpenCode ships as a Node/Bun app; check the README for exact runtime).
- Research wiki working directory at `/home/jfortin/devops-solutions-research-wiki/`.

## Done When

- [ ] `opencode --version` returns a version number (whatever install mechanism worked — npm, bun, binary)
- [ ] `~/.opencode/opencode.json` exists with a baseline config block
- [ ] OpenRouter API key loaded via env or config (key stays at `/home/jfortin/devops-expert-local-ai/.env`)
- [ ] Default model: `moonshotai/kimi-k2.6`
- [ ] Fallback model(s) configured: `anthropic/claude-opus-4.6` + `openai/gpt-5.4`
- [ ] `cd /home/jfortin/devops-solutions-research-wiki && opencode` launches; status shows correct working dir + model
- [ ] First smoke session: ask "Identify yourself" → response references Kimi/Moonshot
- [ ] First tool-use smoke: "list the files in this directory" → OpenCode invokes its file-listing tool; success
- [ ] Install log at `wiki/log/2026-04-23-opencode-install.md` with version, runtime, config file contents (redacted key), gotchas
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Install

Check OpenCode's README for the current install method; tentative commands:

```bash
# Option A: npm global
npm i -g opencode-ai
opencode --version

# Option B: homebrew (if available on Linux via linuxbrew)
brew install opencode

# Option C: download release binary
# See https://github.com/sst/opencode/releases
```

### Step 2 — Baseline config

```bash
mkdir -p ~/.opencode
cat > ~/.opencode/opencode.json <<'EOF'
{
  "provider": {
    "openrouter": {
      "api_key_env": "OPENROUTER_API_KEY",
      "base_url": "https://openrouter.ai/api/v1"
    }
  },
  "model": {
    "default": "openrouter/moonshotai/kimi-k2.6",
    "fallback": [
      "openrouter/anthropic/claude-opus-4.6",
      "openrouter/openai/gpt-5.4"
    ]
  },
  "workspace": {
    "default": "/home/jfortin/devops-solutions-research-wiki"
  }
}
EOF
```

Note: exact config schema subject to OpenCode's current version. Adjust per its docs.

### Step 3 — Load the key + smoke

```bash
set -a; source /home/jfortin/devops-expert-local-ai/.env; set +a
cd /home/jfortin/devops-solutions-research-wiki
opencode
# Inside OpenCode:
#   /status       (confirm workspace + model)
#   > Identify yourself.   (expect Kimi/Moonshot)
#   > List the files in the current directory.   (expect tool call succeeds)
#   /exit
```

### Step 4 — Log results

```bash
python3 -m tools.pipeline scaffold note "2026-04-23-opencode-install"
$EDITOR wiki/log/2026-04-23-opencode-install.md
python3 -m tools.pipeline post
```

## Rollback

```bash
npm uninstall -g opencode-ai   # or brew uninstall, or rm binary
rm -rf ~/.opencode
```

No system-level changes outside `~/.opencode/`.

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| OpenCode config schema changes between versions | external | 2026-04-22 | no | Pin version; capture actual schema in install log |
| OpenCode may default to a different model id format than Claude Code | external | 2026-04-22 | no | Inspect provider docs; translate ids in `opencode.json` |
| Node/Bun runtime conflict with existing global installs | environment | 2026-04-22 | no | Use nvm or isolated global prefix if clash |

## Relationships

- PART OF: [[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]
- DEPENDS ON: [[e007-m002-harness-interactive-validation|e007-m002-harness-interactive-validation]]
- FEEDS INTO: [[e009-m002-mcp-server-continuity|e009-m002-mcp-server-continuity]]
- FEEDS INTO: [[e009-m003-skill-portability|e009-m003-skill-portability]]

## Backlinks

[[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]
[[e007-m002-harness-interactive-validation|e007-m002-harness-interactive-validation]]
[[e009-m002-mcp-server-continuity|e009-m002-mcp-server-continuity]]
[[e009-m003-skill-portability|e009-m003-skill-portability]]

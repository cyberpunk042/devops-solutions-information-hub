---
title: "Directive — Portability Audit and Fix Absolute Paths (2026-04-16)"
type: note
domain: log
status: synthesized
confidence: authoritative
note_type: directive
created: 2026-04-16
updated: 2026-04-16
sources:
  - id: operator-session-2026-04-16
    type: directive
    description: "Operator noticed portability issue — configuration using absolute paths won't transfer to another machine"
tags: [directive, portability, absolute-paths, mcp, config, cross-machine]
---

# Directive — Portability Audit and Fix Absolute Paths

## Summary

Operator identified a portability gap: some configuration files use absolute paths `/home/jfortin/...` that break when the repo is cloned on another machine. Investigation confirms `.mcp.json` is the critical case (committed with machine-specific paths). Operator authorized the fix plan and pulled on OpenArms side in parallel.

## Verbatim

> "I think there is an issue somewhere where we are configuring using absolute paths so its not compatible when I transfer to another machine. lets investigate that before we continue. I will go pulll on openarms side in the meanwhile."

Followed by:

> "continue"

## Investigation findings

**Critical (breaks cross-machine):**
- `.mcp.json` — `command` and `cwd` with `/home/jfortin/...`. MCP server won't load on another machine.

**Low severity (dead entries, not executable):**
- `.claude/settings.json` line 43 — one permission string with absolute path
- `wiki/config/contribution-policy.yaml` line 91 — `project_path_hints` hardcoded to `/home/jfortin/openarms`

**Informational (docstring/comment examples — not executed):**
- `tools/{gateway,mcp_server,source_resolver,sister_project}.py` — help text examples
- `wiki/config/{wiki-schema,mcp-runtime-values}.yaml` — comment examples

**Not an issue:** `~/.cache/research-wiki/session-state.json` lives in user home, outside repo.

## Fix plan executed

1. Add `setup.py --init` command that generates `.mcp.json` per-machine
2. Commit `.mcp.json.template` as reference artifact
3. Add `.mcp.json` to `.gitignore` + `git rm --cached .mcp.json`
4. Fix `wiki/config/contribution-policy.yaml` absolute path → `~/` form
5. Update README/AGENTS.md: "After clone, run `python3 -m tools.setup --init`"
6. Update docstring examples to use `~/` form (P2 polish)
7. Capture as lesson: meta-instance of Aspirational Declaration — "portability" declared without machine-agnostic config = aspirational

## Relationships

- RELATES TO: [[2026-04-16-directive-continue-iterating-with-openarms|Continue Iterating with OpenArms]]
- FEEDS INTO: new lesson on machine-specific config as Aspirational Declaration instance

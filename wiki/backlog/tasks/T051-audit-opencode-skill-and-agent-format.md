---
title: "T051 — Audit OpenCode's Skill / Agent Format + Invocation Convention"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 100
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: S
epic: "E009"
module: "E009-m003"
depends_on:
  - "T045"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e009-m003-skill-portability
    type: wiki
    file: wiki/backlog/modules/e009-m003-skill-portability.md
tags: [task, p1, e009, opencode, skills, agents, audit, research]
---

# T051 — Audit OpenCode Skill / Agent Format

## Summary

Spend 30-60 min auditing how OpenCode represents its user-defined "skills" or "agents". Specifically: file layout, frontmatter fields, args-passing convention, hook-event equivalents. Outputs a side-by-side comparison table against Claude Code's `.claude/skills/` format. Fully runnable today after T045. No wiki writes — results flow into T052 (port `continue`) and T055 (Harness Contract outline).

## Done When

- [ ] Documented: where OpenCode looks for skills/agents (home dir? project dir? both?)
- [ ] Documented: the skill/agent file format (markdown? YAML? JSON?)
- [ ] Documented: invocation syntax from inside OpenCode (`/<name>` or command palette or other)
- [ ] Documented: args-passing convention (positional, named, raw-string)
- [ ] Documented: hook event names OpenCode supports (if any) — comparison to Claude Code's PreToolUse/PostToolUse/SessionStart/UserPromptSubmit
- [ ] Documented: whether OpenCode can use `.claude/skills/*.md` files directly or needs translation
- [ ] Findings captured in a scratch note at `wiki/log/2026-04-23-opencode-skill-format.md`

## Procedure

```bash
# Start with the docs
opencode --help
opencode skills --help 2>&1 || opencode agents --help 2>&1 || true

# Inspect default install
ls -la ~/.opencode/
find ~/.opencode -type f | head -20

# Check for a docs command or built-in reference
opencode docs 2>&1 || true

# Read the online README: https://github.com/sst/opencode

# Compare against Claude's skills dir
ls -la /home/jfortin/devops-solutions-research-wiki/.claude/skills/
head -30 /home/jfortin/devops-solutions-research-wiki/.claude/skills/continue/SKILL.md 2>/dev/null || true
```

Log template:

```markdown
| Dimension | Claude Code | OpenCode | Gap? |
|-----------|-------------|----------|------|
| Skill root dir | `.claude/skills/` + `~/.claude/skills/` | ??? | ??? |
| Skill file format | markdown + YAML frontmatter | ??? | ??? |
| Invocation | `/skill-name args` | ??? | ??? |
| Args schema | free-text after name | ??? | ??? |
| Hook events | PreToolUse, PostToolUse, etc. | ??? | ??? |
```

## Rollback

Read-only audit — nothing to roll back.

## Relationships

- PART OF: [[e009-m003-skill-portability|e009-m003-skill-portability]]
- PART OF: [[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]
- DEPENDS ON: [[T045-install-opencode-binary|T045-install-opencode-binary]]
- FEEDS INTO: [[T055-draft-harness-contract-outline|T055-draft-harness-contract-outline]]

## Backlinks

[[e009-m003-skill-portability|e009-m003-skill-portability]]
[[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]
[[T045-install-opencode-binary|T045-install-opencode-binary]]
[[T055-draft-harness-contract-outline|T055-draft-harness-contract-outline]]

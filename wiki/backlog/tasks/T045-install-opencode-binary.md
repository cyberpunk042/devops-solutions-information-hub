---
title: "T045 — Install OpenCode Binary + Verify `opencode --version`"
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
estimate: XS
epic: "E009"
module: "E009-m001"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e009-m001-opencode-install-and-base-config
    type: wiki
    file: wiki/backlog/modules/e009-m001-opencode-install-and-base-config.md
tags: [task, p1, e009, opencode, install, binary, version-check]
---

# T045 — Install OpenCode Binary

## Summary

Install OpenCode (sst/opencode) using whichever method works on operator's system (npm global / brew / release binary). Verify `opencode --version` works. Runnable today — no hardware prereqs, no wiki changes required.

## Done When

- [ ] `opencode --version` returns a version string (record it)
- [ ] Install method recorded (npm / brew / binary download)
- [ ] Exit code 0 on `opencode --help`
- [ ] Version noted in a local buffer (to paste into install log at M001 close)

## Procedure

```bash
# Try npm first (most common)
npm i -g opencode-ai
opencode --version

# If npm is not the intended path, try brew or release binary per README:
# https://github.com/sst/opencode
```

## Rollback

```bash
npm uninstall -g opencode-ai
# OR whatever removal matches the install method used
```

## Relationships

- PART OF: [[e009-m001-opencode-install-and-base-config|e009-m001-opencode-install-and-base-config]]
- PART OF: [[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]

## Backlinks

[[e009-m001-opencode-install-and-base-config|e009-m001-opencode-install-and-base-config]]
[[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]

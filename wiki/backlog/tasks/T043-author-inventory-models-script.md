---
title: "T043 — Author tools/inventory_models.sh (idempotent, markdown + JSON)"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 95
progress: 0
stages_completed: [document, design]
artifacts:
  - tools/inventory_models.sh
estimate: S
epic: "E010"
module: "E010-m004"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e010-m004-model-weights-inventory
    type: wiki
    file: wiki/backlog/modules/e010-m004-model-weights-inventory.md
tags: [task, p1, e010, inventory, script, scaffold, models, markdown-output]
---

# T043 — Author inventory_models.sh

## Summary

Write the `tools/inventory_models.sh` script per the canonical body in `e010-m004-model-weights-inventory.md` Step 1. Emits a markdown table to stdout + a JSON file at `$ROOT/.inventory.json`. Handles empty-root cleanly. Runnable today — script works against an empty `/mnt/models` and validates the markdown/JSON emission logic before weights land.

## Done When

- [ ] `tools/inventory_models.sh` exists and is executable
- [ ] `shellcheck tools/inventory_models.sh` passes with no errors
- [ ] Running the script against `/tmp/fake-models-empty/` (empty dir) prints the "_No models found_" stub and exits 0
- [ ] Running against a test directory with 2 fake subdirs (each containing a dummy file + a `.source.url` file) prints a valid markdown table with both entries
- [ ] `.inventory.json` written with valid JSON (parsed by `jq .`)
- [ ] Script accepts optional first arg for root dir (default `/mnt/models`)
- [ ] Committed with message: `feat(tools): inventory_models.sh for model weights tracking`

## Procedure

```bash
cd /home/jfortin/devops-solutions-research-wiki
$EDITOR tools/inventory_models.sh
chmod +x tools/inventory_models.sh
shellcheck tools/inventory_models.sh

# Smoke with empty dir
mkdir -p /tmp/fake-models-empty
./tools/inventory_models.sh /tmp/fake-models-empty

# Smoke with fake entries
mkdir -p /tmp/fake-models/fake-a /tmp/fake-models/fake-b
echo "dummy A" > /tmp/fake-models/fake-a/data.bin
echo "dummy B" > /tmp/fake-models/fake-b/data.bin
echo "https://example.com/a" > /tmp/fake-models/fake-a/.source.url
./tools/inventory_models.sh /tmp/fake-models
jq . /tmp/fake-models/.inventory.json

# Cleanup
rm -rf /tmp/fake-models /tmp/fake-models-empty
```

## Rollback

```bash
rm tools/inventory_models.sh
```

## Relationships

- PART OF: [[e010-m004-model-weights-inventory|e010-m004-model-weights-inventory]]
- PART OF: [[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]

## Backlinks

[[e010-m004-model-weights-inventory|e010-m004-model-weights-inventory]]
[[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]

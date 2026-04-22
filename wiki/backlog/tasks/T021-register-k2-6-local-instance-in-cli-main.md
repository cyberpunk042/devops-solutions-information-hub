---
title: "T021 — Register k2_6_local Instance in aicp/cli/main.py (enabled-gated)"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 90
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: XS
epic: "E011"
module: "E011-m003"
depends_on:
  - "T020"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-m003-k2-6-local-backend-adapter
    type: wiki
    file: wiki/backlog/modules/e011-m003-k2-6-local-backend-adapter.md
  - id: aicp-cli-main
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/cli/main.py
tags: [task, p1, e011, aicp, cli, backend-registration, k2-6, local]
---

# T021 — Register k2_6_local Instance in cli/main.py

## Summary

Instantiate a second `LocalAIBackend` in `/home/jfortin/devops-expert-local-ai/aicp/cli/main.py` with `config_key="k2_6_local"`. Guard registration behind `config.backends.k2_6_local.enabled` (defaults to False until E008 M003 delivers a live KTransformers server).

## Done When

- [ ] `backends["k2_6_local"] = LocalAIBackend(config, config_key="k2_6_local")` present and guarded
- [ ] `config.backends.k2_6_local.enabled: true` in `~/.aicp/config.yaml` (or flipped in default.yaml) causes registration
- [ ] `config.backends.k2_6_local.enabled: false` (the shipped default) skips registration — `"k2_6_local" not in backends`
- [ ] With server up and flag on: `aicp run --backend k2_6_local "hi"` succeeds
- [ ] With server down: `aicp run --backend k2_6_local "hi"` fails fast (<2s) thanks to the TCP probe from T022
- [ ] Change committed with message: `feat(cli): register k2_6_local backend (enabled-gated for E008 readiness)`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
grep -n "backends\[\"local\"\]\|LocalAIBackend(" aicp/cli/main.py

$EDITOR aicp/cli/main.py

# Sanity check with flag off (shipped default)
python3 -c "
from aicp.config.loader import load_config
from aicp.cli.main import build_backends   # adjust if function name differs
cfg = load_config()
backends = build_backends(cfg)
print('k2_6_local registered?', 'k2_6_local' in backends)
"
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/cli/main.py
```

## Relationships

- PART OF: [[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T020-parameterize-localai-backend-config-key|T020-parameterize-localai-backend-config-key]]

## Backlinks

[[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T020-parameterize-localai-backend-config-key|T020-parameterize-localai-backend-config-key]]

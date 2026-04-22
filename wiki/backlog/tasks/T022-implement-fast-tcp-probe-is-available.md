---
title: "T022 — Implement Fast TCP Probe for LocalAIBackend.is_available()"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 85
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: S
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
  - id: aicp-localai-backend
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/backends/localai.py
tags: [task, p1, e011, aicp, is-available, tcp-probe, reliability, failover]
---

# T022 — Fast TCP Probe for is_available()

## Summary

Make `LocalAIBackend.is_available()` return in <1s whether the server is up or down. Current behavior likely relies on HTTP request which hangs up to timeout seconds on a dead socket — that delays failover for every routing decision while the server is down. Replace with a socket-level probe using 1s timeout.

## Done When

- [ ] `is_available()` completes in <1.5s whether port is listening or refused/unreachable
- [ ] Returns `True` when TCP handshake succeeds to `self.base_url` host:port
- [ ] Returns `False` (no exception) when port refused, timeout, or DNS error
- [ ] Preserves any existing "model loaded" check as a secondary verification after TCP probe passes (if existing check is cheap)
- [ ] Integration test: with no server running, `is_available()` returns False in <1.5s (timed)
- [ ] Integration test (marked `@pytest.mark.integration`): with server running, returns True
- [ ] Change committed with message: `feat(localai): fast TCP probe for is_available() to avoid failover stalls`

## Procedure

```bash
cd /home/jfortin/devops-expert-local-ai
grep -n "is_available\|status_detail" aicp/backends/localai.py

# Apply edit per e011-m003 Step 3
$EDITOR aicp/backends/localai.py

# Timed check
time python3 -c "
from aicp.config.loader import load_config
from aicp.backends.localai import LocalAIBackend
cfg = load_config()
b = LocalAIBackend(cfg, config_key='k2_6_local')
print('available:', b.is_available())
"
# Expected: <1.5s even when nothing listens on 8091
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/backends/localai.py
```

## Relationships

- PART OF: [[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]
- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[T020-parameterize-localai-backend-config-key|T020-parameterize-localai-backend-config-key]]

## Backlinks

[[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[T020-parameterize-localai-backend-config-key|T020-parameterize-localai-backend-config-key]]

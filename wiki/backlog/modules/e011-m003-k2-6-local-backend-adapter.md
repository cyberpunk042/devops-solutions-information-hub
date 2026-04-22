---
title: "E011 M003 — K2.6 Local Backend Adapter (KTransformers OpenAI-compat)"
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
epic: "E011"
depends_on:
  - "E008-m002"
  - "E011-m001"
confidence: medium
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e011-routing-integration-aicp-tiers
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E011-routing-integration-aicp-tiers.md
  - id: e008-local-k2-6-offline-frontier-tier
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E008-local-k2-6-offline-frontier-tier.md
  - id: aicp-localai-backend
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/backends/localai.py
  - id: ktransformers-readme
    type: repository
    url: https://github.com/kvcache-ai/ktransformers
    title: "KTransformers — MoE disk-offload inference"
tags: [module, p1, e011, aicp, k2-6, local, ktransformers, localai, backend, adapter]
---

# E011 M003 — K2.6 Local Backend Adapter

## Summary

Expose the locally-served K2.6 Q2 model (from E008, served by KTransformers) as an AICP backend called `k2_6_local`. KTransformers ships an OpenAI-compatible HTTP server, so the simplest path is to reuse the existing `LocalAIBackend` class (in `aicp/backends/localai.py`) with a different `base_url` and a different config key — the same parameterization pattern used for OpenRouter in M002. This module stands up the adapter, health check, and smoke test. Does NOT cover the K2.6 serving process itself (that's E008 M003 — first-light benchmark).

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T020 | Parameterize LocalAIBackend __init__ to accept config_key | 100% | 0% | draft |
| T021 | Register k2_6_local instance in cli/main.py + enable flag wiring | 90% | 0% | draft |
| T022 | Write is_available() TCP probe + smoke test against live KTransformers | 70% | 0% | draft |

## Dependencies

- **E008 M002** — K2.6 Q2 GGUF weights on `/mnt/models/kimi-k2-6-q2/`.
- **E008 M003** (future) — KTransformers service running on `localhost:8091` (port choice confirmed here to avoid collision with LocalAI at 8090).
- **E011 M001** — `k2_6_local` config stanza already drafted (`enabled: false` until M003 can flip it on).
- **E010 M001** — 64 GB RAM (needed for K2.6 Q2 inference headroom).

## Done When

- [ ] `LocalAIBackend.__init__` accepts optional `config_key: str = "local"` param (parallel to M002 change for OpenRouter)
- [ ] `aicp/cli/main.py` instantiates `k2_6_local` as a `LocalAIBackend(config, config_key="k2_6_local")` when `backends.k2_6_local.enabled == True`
- [ ] `k2_6_local.is_available()` does a fast TCP probe to `localhost:8091` with 1s timeout; returns False cleanly if server isn't up
- [ ] `aicp run --backend k2_6_local "hello"` succeeds when the local server is running; returns a reply from `last_usage["model"] == "kimi-k2.6-q2"`
- [ ] `aicp run --backend k2_6_local "..."` fails fast with a clear error message when the server is not running
- [ ] Streaming path works against KTransformers SSE
- [ ] Unit test in `tests/test_k2_6_local_backend.py` asserts registration + config wiring
- [ ] Integration test (marked `@pytest.mark.integration`, skipped when `KTRANS_URL` env is unset) hits a live server
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 0 — Confirm KTransformers server is up (prereq from E008 M003)

```bash
# Tentative — adjust to the actual KTransformers invocation
# Example command form:
ktransformers server \
  --model-path /mnt/models/kimi-k2-6-q2/UD-Q2_K_XL \
  --gguf-path /mnt/models/kimi-k2-6-q2/UD-Q2_K_XL \
  --host 0.0.0.0 --port 8091 \
  --optimize-config-path optimizations/kimi-k2.6.yaml

# Sanity check
curl -s http://localhost:8091/v1/models | jq
```

### Step 1 — Parameterize LocalAIBackend

Mirror the change from E011 M002:

```python
class LocalAIBackend(Backend):
    def __init__(self, config: Dict[str, Any], config_key: str = "local"):
        self.config_key = config_key
        self.config = config.get("backends", {}).get(config_key, {})
        self.name = config_key
        self.base_url = self.config.get("base_url", "http://localhost:8090")
        self.model = self.config.get("model", "qwen3-8b")
        ...
```

### Step 2 — Register in cli/main.py

```python
# Existing local registration stays put (unchanged)
if config.get("backends", {}).get("local", {}).get("enabled", True):
    backends["local"] = LocalAIBackend(config)

# New k2_6_local registration — gated by enabled flag from config
if config.get("backends", {}).get("k2_6_local", {}).get("enabled", False):
    backends["k2_6_local"] = LocalAIBackend(config, config_key="k2_6_local")
```

### Step 3 — Implement fast availability probe

```python
def is_available(self) -> bool:
    # Avoid blocking the router when the local server is down.
    import socket
    from urllib.parse import urlparse

    u = urlparse(self.base_url)
    host = u.hostname or "localhost"
    port = u.port or 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)
        try:
            s.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False
```

If `LocalAIBackend` already has `is_available()`, keep the existing behavior but add a fast-fail guard at the top to avoid multi-second hangs on dead sockets.

### Step 4 — Smoke test

```bash
cd /home/jfortin/devops-expert-local-ai
# Ensure config/default.yaml has k2_6_local.enabled: true (or override via ~/.aicp/config.yaml)
python3 -m aicp.cli.main run --backend k2_6_local "Identify yourself."
# Expected: response references Kimi K2.6; last_usage["backend"] == "k2_6_local"

# Kill KTransformers, retry — should fail fast
python3 -m aicp.cli.main run --backend k2_6_local "..."
# Expected: <1s to error, router falls through failover_chain to k2_6_openrouter
```

### Step 5 — Add tests

`tests/test_k2_6_local_backend.py`:

```python
def test_k2_6_local_registered_when_enabled(config_with_k2_6_local_enabled):
    backends = build_backends(config_with_k2_6_local_enabled)
    assert "k2_6_local" in backends
    assert backends["k2_6_local"].base_url == "http://localhost:8091"

def test_k2_6_local_skipped_when_disabled(config_with_k2_6_local_disabled):
    backends = build_backends(config_with_k2_6_local_disabled)
    assert "k2_6_local" not in backends

@pytest.mark.integration
def test_k2_6_local_live_inference():
    url = os.environ.get("KTRANS_URL")
    if not url:
        pytest.skip("KTRANS_URL not set")
    # ... minimal round-trip ...
```

## Rollback

```bash
cd /home/jfortin/devops-expert-local-ai
git checkout -- aicp/backends/localai.py aicp/cli/main.py
# Flip backends.k2_6_local.enabled: false in config (or let default stand)
```

Rolling back this module does not affect `k2_6_openrouter` — the failover_chain continues to route agentic work through OpenRouter.

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| KTransformers may need Kimi-K2.6-specific YAML optimization config | external | 2026-04-22 | no | Check `optimizations/` in KTransformers repo; may require community contribution if absent |
| Port collision with LocalAI (8090) | config | 2026-04-22 | no | Use 8091 for KTransformers; documented in config/default.yaml |
| First-light benchmark latency unknown | unknown | 2026-04-22 | no | Captured by E008 M003; expect 1–3 tok/s on Q2 |

## Relationships

- PART OF: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- DEPENDS ON: [[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
- DEPENDS ON: [[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
- FEEDS INTO: [[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]

## Backlinks

[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
[[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
[[e011-m004-circuit-breakers-and-fallback-chain|e011-m004-circuit-breakers-and-fallback-chain]]

---
title: "E008 M004 — Local K2.6 OpenAI-Compat Endpoint (KTransformers server)"
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
epic: "E008"
depends_on:
  - "E008-m001"
  - "E008-m002"
  - "E008-m003"
confidence: medium
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e008-local-k2-6-offline-frontier-tier
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E008-local-k2-6-offline-frontier-tier.md
tags: [module, p1, e008, ktransformers, openai-compat, server, systemd, endpoint]
---

# E008 M004 — Local K2.6 OpenAI-Compat Endpoint

## Summary

Expose K2.6 Q2 (served by KTransformers) as a stable OpenAI-compatible HTTP endpoint at `http://localhost:8091` so AICP's `LocalAIBackend` (parameterized in E011 M003) can consume it without custom protocol code. Runs the KTransformers server under a lightweight supervisor (systemd user unit OR a simple `tmux` session, operator choice). Verifies the endpoint's OpenAI-compat surface: `/v1/models`, `/v1/chat/completions`, streaming via SSE.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T036 | Author ktransformers-serve.sh wrapper + optimizations YAML | 80% | 0% | draft |
| T037 | Verify /v1/models and /v1/chat/completions compatibility | 90% | 0% | draft |
| T038 | Set up user systemd unit for auto-start on WSL login | 70% | 0% | draft |

## Dependencies

- **E008 M001** — KTransformers installed.
- **E008 M002** — weights at `/mnt/models/kimi-k2-6-q2/`.
- **E008 M003** — first-light benchmark proved the model loads + generates on this hardware.

## Done When

- [ ] `scripts/ktransformers-serve.sh` exists and launches the server on port 8091
- [ ] `curl -s http://localhost:8091/v1/models | jq` returns a JSON object with `data[].id` including the K2.6 model name
- [ ] `curl -sS -H "Content-Type: application/json" -d '{"model":"kimi-k2.6-q2","messages":[{"role":"user","content":"hi"}]}' http://localhost:8091/v1/chat/completions | jq` returns a valid `choices[0].message.content`
- [ ] Streaming works: same call with `"stream": true` returns SSE chunks
- [ ] Load time under 5 min after SSD cache is warm (recorded)
- [ ] Systemd user unit (`~/.config/systemd/user/ktransformers-server.service`) OR a tmux `kt-server` session recipe documented
- [ ] Health-check command: `curl -s --max-time 2 http://localhost:8091/v1/models > /dev/null` returns exit 0 when server up
- [ ] Fail-safe documented: how to kill, how to inspect logs
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Author wrapper script

```bash
cd /home/jfortin/devops-solutions-research-wiki
$EDITOR scripts/ktransformers-serve.sh
chmod +x scripts/ktransformers-serve.sh
```

Minimum content:

```bash
#!/usr/bin/env bash
set -euo pipefail

: "${KT_MODEL_PATH:=/mnt/models/kimi-k2-6-q2/UD-Q2_K_XL}"
: "${KT_OPT_CONFIG:=optimizations/kimi-k2.6.yaml}"
: "${KT_PORT:=8091}"
: "${KT_HOST:=0.0.0.0}"
: "${KT_LOG:=/home/jfortin/ktransformers-env/server.log}"

source /home/jfortin/ktransformers-env/bin/activate

exec python -m ktransformers.server.main \
  --model-path "$KT_MODEL_PATH" \
  --gguf-path "$KT_MODEL_PATH" \
  --optimize-config-path "$KT_OPT_CONFIG" \
  --host "$KT_HOST" --port "$KT_PORT" \
  2>&1 | tee -a "$KT_LOG"
```

### Step 2 — Smoke endpoint

```bash
# In terminal 1
./scripts/ktransformers-serve.sh

# In terminal 2 (wait ~2-5 min for model load)
curl -s http://localhost:8091/v1/models | jq
curl -sS -H "Content-Type: application/json" -d '{
  "model": "kimi-k2.6-q2",
  "messages": [{"role": "user", "content": "Identify yourself."}],
  "max_tokens": 100
}' http://localhost:8091/v1/chat/completions | jq

# Streaming
curl -sN -H "Content-Type: application/json" -d '{
  "model": "kimi-k2.6-q2",
  "messages": [{"role": "user", "content": "Count to 5."}],
  "stream": true
}' http://localhost:8091/v1/chat/completions
```

### Step 3 — Systemd user unit

```bash
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/ktransformers-server.service <<'EOF'
[Unit]
Description=KTransformers K2.6 OpenAI-Compat Server
After=default.target

[Service]
Type=simple
ExecStart=/home/jfortin/devops-solutions-research-wiki/scripts/ktransformers-serve.sh
Restart=on-failure
RestartSec=10
Environment="KT_PORT=8091"

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable ktransformers-server.service
systemctl --user start ktransformers-server.service
systemctl --user status ktransformers-server.service
```

Note: WSL2 user-mode systemd requires `systemd=true` in `/etc/wsl.conf`. If unavailable, use a tmux session:

```bash
tmux new-session -d -s kt-server '/home/jfortin/devops-solutions-research-wiki/scripts/ktransformers-serve.sh'
```

### Step 4 — Health check + AICP handshake

```bash
# Confirm AICP can reach it
cd /home/jfortin/devops-expert-local-ai
# Flip k2_6_local.enabled: true in ~/.aicp/config.yaml
python3 -m aicp.cli.main run --backend k2_6_local "Identify yourself."
# Expected: response from K2.6; last_usage["model"] ~= "kimi-k2.6-q2"
```

## Rollback

```bash
systemctl --user stop ktransformers-server.service
systemctl --user disable ktransformers-server.service
rm -f ~/.config/systemd/user/ktransformers-server.service

# Or tmux
tmux kill-session -t kt-server 2>/dev/null || true
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| KTransformers server OpenAI-compat surface may diverge from OpenAI spec | external | 2026-04-22 | no | Test tool_choice, stream, usage fields explicitly; document gaps in first-light log |
| WSL2 systemd user mode may be disabled | environment | 2026-04-22 | no | Fallback to tmux session in install procedure |
| Port 8091 collision | config | 2026-04-22 | no | Configurable via KT_PORT env; document in config/default.yaml |

## Relationships

- PART OF: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
- DEPENDS ON: [[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
- DEPENDS ON: [[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
- DEPENDS ON: [[e008-m003-first-light-benchmark|e008-m003-first-light-benchmark]]
- FEEDS INTO: [[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]

## Backlinks

[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
[[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
[[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
[[e008-m003-first-light-benchmark|e008-m003-first-light-benchmark]]
[[e011-m003-k2-6-local-backend-adapter|e011-m003-k2-6-local-backend-adapter]]

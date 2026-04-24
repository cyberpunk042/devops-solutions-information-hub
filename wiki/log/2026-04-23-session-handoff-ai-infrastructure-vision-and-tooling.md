---
title: "Session Handoff 2026-04-23 — AI Infrastructure Vision, Landscapes, Decision Matrix, Price-Monitoring Tool"
type: note
domain: cross-domain
note_type: session
status: active
confidence: high
created: 2026-04-23
updated: 2026-04-23
last_reviewed: 2026-04-23
sources:
  - id: ai-infra-framework
    type: wiki
    file: wiki/spine/references/ai-infrastructure-decision-framework-2026.md
  - id: decision-matrix
    type: wiki
    file: wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md
  - id: harness-landscape
    type: wiki
    file: wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md
  - id: provider-landscape
    type: wiki
    file: wiki/sources/tools-integration/src-inference-provider-landscape-2026.md
  - id: local-training-playbook
    type: wiki
    file: wiki/spine/references/local-training-playbook-2026.md
  - id: provider-monitoring-ops
    type: wiki
    file: wiki/spine/references/provider-pricing-monitoring-operations-plan.md
  - id: opencode-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-opencode-harness-features.md
  - id: codex-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-codex-cli-and-claude-code-plugin.md
  - id: claude-code-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-claude-code-harness-features.md
tags: [handoff, session, ai-infrastructure, vision, mission, post-anthropic, "2026-04-23", pickup-cold]
---

# Session Handoff — 2026-04-23

## Summary

The session built an **AI infrastructure vision + operational tooling** for the mission "post-Anthropic self-autonomous AI stack by 2026-04-27." Starting state was a fresh Ubuntu 24.04 WSL pickup-cold; ending state is 476 wiki pages at A+ 99.9 health, a full provider/harness/model landscape documented with verified pricing, a live price-monitoring tool, and an activated OpenCode+Ollama Cloud stack alongside Claude Code. **Next session should start with `gateway orient` then read this handoff.** Key unresolved: operator's planned AIDLC research (deferred), Opus 4.6 pricing (OpenRouter is 3× cheaper than Anthropic-direct — revisit routing), and operator will be "toying" with OpenCode + Ollama Cloud — help when asked but don't preempt.

## Session arc (what happened)

### Phase 1 — Pickup-cold + wiki health (early session, 2026-04-22)
1. Fresh Ubuntu 24.04 WSL environment; operator ran `tools.setup` which generated `.mcp.json` + connected sister projects
2. Found + fixed 5 real tool bugs: lint exemplar check, missing `rebuild_backlog_index` modules support, `wiki_log` slug generator + note_type mapping, filename-lint allowlist tightening, validator schema-cache reload (27% pipeline speedup)
3. Health went D/69 → A+/99 via: 22 nested-wikilink corruptions fixed across 14 files; 11 filename renames + 54 wikilink updates; 27 seed pages promoted seed→growing; 9 stale pages verified-current and `last_reviewed`-stamped; 3 inbox contributions accepted/promoted with audit trails
4. Two comparison pages authored: Model-Ecosystem-vs-Four-Project-Ecosystem, MCP-vs-CLI-Decision-vs-Lesson

### Phase 2 — Ingested AICP 2026-04-24 findings + vision doc (mid-session)
Operator directed ingestion of AICP's 2026-04-24 decision session (8 docs in `docs/`):
- POSTMORTEM-2026-04-24-k26-local-wrong-path (2 days of local K2.6 failures → postmortem)
- PERSPECTIVE-AI-INFRASTRUCTURE-DECISION (strategic decision framework)
- MODEL-ECOSYSTEM-FULL-MAP (verified provider pricing matrix)
- CLOUD-SPEND-SCENARIOS (breakeven math)
- HARDWARE-BUILD-SCENARIOS (3 tiers, CAD pricing)
- SCALING-PROJECTION-5YR (operator's workload projection)
- SESSION-2026-04-24-HANDOFF + CONVERSATION-LOG

All 8 copied to `raw/articles/aicp-*.md`.

**Authored [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]** — spine P0 reference synthesizing AICP's findings + extending to GPT/Codex/subscriptions. Captures:
- Four dimensions (Cost / Capability / Privacy / Mission)
- Specialty Routing section (each provider has unique strengths)
- 4-phase framework (ramp-up → Pro→Max → hardware decision → steady state)
- 10 anti-patterns
- Resilience playbook (substitution paths for every failure mode)
- Training: Local Unsloth/LoRA vs Cloud GPU Rental
- Six re-evaluation triggers
- **Harness Routing table** (when to reach for Claude Code vs OpenCode vs Codex Plugin — added 2026-04-23)

### Phase 3 — Training + Specialty corrections (mid-session)
Operator corrected me: "mission violation" framing was too Puritan. Mission is **anti-vendor-lock-in**, not anti-closed-weight. Specialty routing = mission-aligned. Framework updated accordingly.

**Authored [[local-training-playbook-2026|Local Training Playbook 2026]]** — operations-plan with 3 concrete tracks:
- Track 1: Wiki Alignment LoRA (Qwen3-4B, ~2-3h local, $0 cloud)
- Track 2: Tool-Call LoRA (Qwen3-4B, ~1-2h)
- Track 3: Semantic Enhancement (BGE-M3 off-the-shelf first; fine-tune only if retrieval @5 fails ≥85%)

Local Unsloth training verified viable on operator's 19GB VRAM hardware for ≤8B bases. Cloud rental only justified for 27B+ or full fine-tunes.

### Phase 4 — Harness + Provider research (mid/late session)
Operator corrected me again: "adversarial review is a codex command / feature lol" — I'd invented an abstract pattern when they named a specific product. Deleted the pattern page. Researched actual products.

**Authored 3 product-synthesis pages (all from official docs):**
- [[src-codex-cli-and-claude-code-plugin|Codex CLI + Codex Plugin for Claude Code]] — with `/codex:adversarial-review` documented accurately (7 attack surfaces, flags, JSON output)
- [[src-claude-code-harness-features|Claude Code Harness Features]] — 16-field skill frontmatter, 8 hook events, plugin system
- [[src-opencode-harness-features|OpenCode Harness Features]] — Build/Plan Tab toggle, LSP native, 75+ providers, multi-session

**Authored 2 landscape syntheses:**
- [[src-agentic-coding-harness-landscape-2026|Harness Landscape 2026]] — 11+ harnesses, BYOM vs product, SWE-Bench 80.8% (CC leader), Terminal-Bench 77.3% (Codex leader)
- [[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]] — 10+ providers, OpenRouter 5.5% fee + 100-150ms latency, Cerebras 1000 TPS + 1M/day free, Groq 315 TPS, Together H100/H200/B200

### Phase 5 — Decision Matrix + Price-Monitoring (late session)
**Authored [[ai-model-provider-harness-decision-matrix-2026|Decision Matrix 2026]]** — single-page unified lookup (16 models × 8 providers × 12 harnesses). Contains:
- Master Matrix sorted by output cost
- Provider × Model availability grid
- Harness × Provider compatibility grid
- 13 workload recipes (harness, provider, model, $/hour)
- Open-weight tier hierarchy: Floor / Ultra-budget / Budget / Anchor / Ceiling

**Shipped price-monitoring infrastructure:**
- [tools/provider_check.py](tools/provider_check.py) — fetches OpenRouter pricing, diffs vs cached snapshot, reports ≥20% changes
- [wiki/config/provider-pricing-cache.json](wiki/config/provider-pricing-cache.json) — 16 models verified pricing snapshot
- `python3 -m tools.pipeline provider-check` subcommand (`--health` for 11-provider liveness, `--snapshot` to accept new baseline)
- [[provider-pricing-monitoring-operations-plan|Operations Plan]] with systemd timer config

Tool surfaced **corrections** to my earlier numbers:
- K2.6 on OpenRouter is actually **$0.745/$4.655** (output ~33% higher than I'd cited)
- Opus 4.6/4.7 on OpenRouter is **$5/$25** (not $15/$75 direct) — **3× cheaper** than I'd estimated
- **DeepSeek V4-Pro is $1.74/$3.48** — Opus-class (80.6% SWE-Bench Verified) at 1/7 Opus cost
- **DeepSeek V4-Flash is $0.14/$0.28 with 1M context** — the new cost floor for coding-capable models

### Phase 6 — OpenCode activation + corrections (end of session)
Operator installed Ollama (login done), OpenCode, OpenClaw. Live stack, not hypothetical.

**Verified Ollama Cloud catalog via ollama.com/search?c=cloud** — 20+ models accessible post-login, including:
- kimi-k2.6 + kimi-k2.5
- deepseek-v4-flash (1M context)
- glm-5.1 (newer than 4.7), glm-5 (744B/40B MoE), glm-4.7
- **gemini-3-flash-preview** ⚠️ — corrects earlier framework claim "Ollama Cloud has no proprietary models"
- qwen3.5, qwen3-coder-next, qwen3-next, devstral-small-2, devstral-2
- nemotron-3-super/nano, minimax-m2.5/2.7, cogito-2.1 (671B MIT)

Framework updated with corrections + harness-routing table.

## Current state (2026-04-23 end-of-session)

### Wiki health
```
Pages: 476
Relationships: 2,880 (avg 6.1/page)
Validation errors: 0
Lint issues: 0
Composite: 99.9 / A+
Queue sync: 60/60 resolved
Evolution: 476/476 past 00_inbox
Freshness: 475/476 within 90d
```

### Infrastructure
- **MCP server**: research-wiki live, 26+ tools callable via `mcp__research-wiki__*` prefix
- **Pipeline**: `python3 -m tools.pipeline post` passes in ~30s (was 41s before schema-cache fix)
- **Price cache**: 16 models cached 2026-04-23
- **Provider health**: 11/11 alive last checked 2026-04-23

### Operator's active stack (2026-04-23 — see memory `project_activated_stack_2026_04_23`)
- Ollama + login (Ollama Cloud Pro catalog callable)
- OpenCode (VS Code + TUI, second primary harness)
- Claude Code (primary, with Codex Plugin for adversarial-review)
- AICP running OpenRouter K2.6 backend live (AICP 2026-04-24 session verified)
- Local K2.6 Q2 technically running at 0.3 tok/s (sovereignty fallback only)

### Mission deadlines
- **2026-04-27**: Post-Anthropic self-autonomous AI stack milestone (AICP E008-E012)
- Current phase per framework: Phase 1 (ramp-up, $40-70/mo budget)

## Artifacts shipped this session

### New wiki pages (spine-level)
| Path | Type | Role |
|---|---|---|
| [wiki/spine/references/ai-infrastructure-decision-framework-2026.md](wiki/spine/references/ai-infrastructure-decision-framework-2026.md) | reference (P0) | The canonical vision |
| [wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md](wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md) | reference (P0) | Unified lookup matrix |
| [wiki/spine/references/local-training-playbook-2026.md](wiki/spine/references/local-training-playbook-2026.md) | operations-plan (P1) | 3-track local training |
| [wiki/spine/references/provider-pricing-monitoring-operations-plan.md](wiki/spine/references/provider-pricing-monitoring-operations-plan.md) | operations-plan (P1) | provider-check runbook |

### New wiki pages (sources)
| Path | Role |
|---|---|
| [wiki/sources/tools-integration/src-codex-cli-and-claude-code-plugin.md](wiki/sources/tools-integration/src-codex-cli-and-claude-code-plugin.md) | Codex CLI + Plugin product synthesis |
| [wiki/sources/tools-integration/src-claude-code-harness-features.md](wiki/sources/tools-integration/src-claude-code-harness-features.md) | Claude Code features synthesis |
| [wiki/sources/tools-integration/src-opencode-harness-features.md](wiki/sources/tools-integration/src-opencode-harness-features.md) | OpenCode features + Ollama Cloud catalog |
| [wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md](wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md) | 11+ harnesses landscape |
| [wiki/sources/tools-integration/src-inference-provider-landscape-2026.md](wiki/sources/tools-integration/src-inference-provider-landscape-2026.md) | 10+ providers landscape |

### Earlier in session
| Path | Role |
|---|---|
| [wiki/comparisons/model-ecosystem-vs-four-project-ecosystem.md](wiki/comparisons/model-ecosystem-vs-four-project-ecosystem.md) | Model vs instance comparison |
| [wiki/comparisons/mcp-vs-cli-decision-vs-lesson.md](wiki/comparisons/mcp-vs-cli-decision-vs-lesson.md) | Decision vs lesson comparison |
| [wiki/comparisons/kimi-k2-6-access-paths-openrouter-ollama-cloud-local.md](wiki/comparisons/kimi-k2-6-access-paths-openrouter-ollama-cloud-local.md) | K2.6 access paths |

### Tool changes (code modified)
- **[tools/provider_check.py](tools/provider_check.py)** — NEW — pricing diff + health subcommand
- **[tools/pipeline.py](tools/pipeline.py)** — added `provider-check` subcommand + schema-cache fix (run_validate)
- **[tools/validate.py](tools/validate.py)** — schema-cache fix (validate_page accepts preloaded schema)
- **[tools/lint.py](tools/lint.py)** — exemplar check fixes (multiple) + filename allowlist tightening + question-callout handling + rename-filter in stale classifier
- **[tools/common.py](tools/common.py)** — `rebuild_backlog_index` now generates `wiki/backlog/modules/_index.md`
- **[tools/mcp_server.py](tools/mcp_server.py)** — `wiki_log` slug sanitization + note_type normalization
- **[tools/evolve.py](tools/evolve.py)** — `mark_reviewed` function + `--analyze` stale classifier + CLI `--page`/`--analyze` flags
- **[tools/gateway.py](tools/gateway.py)** — ingestion_backlog counter now credits URL-sourced raws (not just file-matched)
- **[tools/manifest.py](tools/manifest.py)** — propagates `last_reviewed` frontmatter field
- **[wiki/config/wiki-schema.yaml](wiki/config/wiki-schema.yaml)** — added `last_reviewed`, `review_note` optional fields
- **[wiki/config/provider-pricing-cache.json](wiki/config/provider-pricing-cache.json)** — NEW — 16-model pricing snapshot

### Raw files ingested
- 8 AICP 2026-04-24 docs copied to `raw/articles/aicp-*.md`
- 1 Medium article (Kimi K2.6 via Ollama Cloud by Joe Njenga) in `raw/articles/kimi-k2-6-claude-code-ollama-cloud-joe-njenga-medium.md`

## Operator corrections captured (memories saved)

Three durable feedback memories saved for future sessions:

1. **[feedback_check_file_type](file:///home/jfortin/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_check_file_type.md)** — `ls -la`/`readlink` first before claiming duplicates; symlinks mimic dirs
2. **[feedback_research_not_abstract](file:///home/jfortin/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_research_not_abstract.md)** — operator names a feature → fetch docs, do NOT invent patterns
3. **[feedback_mission_framing](file:///home/jfortin/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_mission_framing.md)** — mission = anti-vendor-lock-in, NOT anti-closed-weight

Plus one project memory:
- **[project_activated_stack_2026_04_23](file:///home/jfortin/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/project_activated_stack_2026_04_23.md)** — Ollama + OpenCode + OpenClaw activated

## Open threads (what's still pending)

### Explicitly deferred by operator
- **AIDLC** — operator flagged as future topic: "I will also soon bring new insgest about AIDLC where we have explore SDLC and branches but there is such a thing as a AIDLC topic online. but stay focus on the present for now." Do NOT preempt; wait for operator signal.

### Low-priority follow-ups
- **DeepSeek V3.2, Gemini 3.1 Pro, etc.** — pricing cache has these but syntheses don't exist yet. Add if/when operator exercises them.
- **3 unstyled-lesson advisories** remain (content-style, not blocking) — operator has not flagged as priority
- **4 open queue questions** were all closed in session (60/60 resolved)
- **K2.6 local smoke test via llama.cpp** — AICP technically reached milestone at 0.3 tok/s. Not practically usable. Flagged in framework as sovereignty-fallback only.

### Operator was about to explore
- Toying with OpenCode + Ollama Cloud (`/connect ollama` in OpenCode, test Build/Plan mode, test multi-session). Help when asked.
- Per the OpenCode synthesis's "Next steps for operator" section:
  1. `/init` in wiki repo — compare generated AGENTS.md to existing
  2. Multi-session test
  3. Plan mode on non-trivial task
  4. `/connect ollama` → test kimi-k2.6, deepseek-v4-flash, glm-5.1
  5. Port one `.claude/skills/` to OpenCode
  6. Cost benchmark same task on both harnesses

### Mission-critical reminders
- **2026-04-27 deadline** for post-Anthropic milestone — 4 days away at session end. Framework is in place; operator is in Phase 1 (ramp-up) with budget $40-70/mo.
- Ollama Cloud Pro activated → natural next config is making it AICP's personal-daily default tier_map entry (not yet wired per operator's focus on OpenCode toying)

## Pickup-cold runbook (first commands for next session)

```bash
# 1. Orient (loads second-brain context per CLAUDE.md)
cd ~/devops-solutions-information-hub
python3 -m tools.gateway orient

# 2. Confirm stack state
python3 -m tools.pipeline status            # wiki stats
python3 -m tools.pipeline provider-check --health  # 11 providers alive?
python3 -m tools.pipeline provider-check           # any price drift?

# 3. Read this handoff
cat wiki/log/2026-04-23-session-handoff-ai-infrastructure-vision-and-tooling.md
```

Then read in this order if unfamiliar:
1. [ai-infrastructure-decision-framework-2026.md](wiki/spine/references/ai-infrastructure-decision-framework-2026.md) — the vision
2. [ai-model-provider-harness-decision-matrix-2026.md](wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md) — the lookup
3. [src-opencode-harness-features.md](wiki/sources/tools-integration/src-opencode-harness-features.md) — what the operator just activated
4. [local-training-playbook-2026.md](wiki/spine/references/local-training-playbook-2026.md) — training answers

## Known issues to watch for

1. **MCP server process may lag code changes** — `wiki_log` MCP tool and others use the version of `tools/mcp_server.py` the server was started with. If a `mcp_server.py` fix doesn't appear to take effect, the MCP server needs restarting (it's the parent process's responsibility).

2. **`wiki_log` MCP tool can still produce bad slugs on special-char titles** — the fix is in the code but the running server predates it. Work around by using plain ASCII titles OR renaming after creation. Or restart the MCP server.

3. **OpenRouter fetch timeout occasionally 20s+** — network-dependent; `provider-check` has 20s timeout built in

4. **3 filename issues were reported in operator-decision-queue** — all closed this session; if they reappear, re-run the analyzer

## Relationships

- BUILDS ON: [[wsl-ubuntu-migration-handoff|WSL Ubuntu Migration Handoff]] — the pickup-cold this session started from
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — every claim in the framework docs this session traces to a verified source, cached pricing, or tool-run evidence
- RELATES TO: [[2026-04-22-wsl-migration-to-ubuntu-24-04|WSL Migration]] — the session previous
- RELATES TO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — the canonical artifact
- RELATES TO: [[ai-model-provider-harness-decision-matrix-2026|Decision Matrix 2026]]

## Backlinks

[[WSL Ubuntu Migration Handoff]]
[[Principle 4]]
[[WSL Migration]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[Decision Matrix 2026]]

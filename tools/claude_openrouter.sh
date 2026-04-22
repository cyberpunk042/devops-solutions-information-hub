#!/usr/bin/env bash
# tools/claude_openrouter.sh
#
# Route Claude Code CLI through OpenRouter's Anthropic Skin, targeting
# Moonshot AI's Kimi K2.6 as the primary model.
#
# Usage:
#   export OPENROUTER_API_KEY="sk-or-v1-..."   # set your key
#   source tools/claude_openrouter.sh
#   or-claude                                  # start Claude Code → OpenRouter → K2.6
#   or-claude-opus                             # start Claude Code → OpenRouter → Claude Opus 4.6 (control)
#   or-claude-gpt                              # start Claude Code → OpenRouter → GPT-5.4 (control)
#   or-claude-status                           # print current routing env
#   or-claude-clear                            # unset overrides, return to native Claude
#
# Why this is separate from ~/.bashrc:
#   Keeps the feature flag explicit per-session. You can mix native Claude Code
#   and OpenRouter-routed Claude Code in different terminals without confusion.
#
# Base URL note:
#   Use exactly https://openrouter.ai/api (NO /v1 suffix). The /v1 variant
#   causes model-not-found errors because Claude Code expects OpenRouter's
#   native Anthropic Skin endpoint.
#
# Auth note:
#   ANTHROPIC_API_KEY must be explicitly empty; otherwise Claude Code's native
#   auth path races with ANTHROPIC_AUTH_TOKEN and can fail interactive mode.

set -o pipefail

or-claude() {
    if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
        echo "ERROR: OPENROUTER_API_KEY is not set. Export it first." >&2
        return 2
    fi

    ANTHROPIC_BASE_URL="https://openrouter.ai/api" \
    ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY" \
    ANTHROPIC_API_KEY="" \
    ANTHROPIC_DEFAULT_OPUS_MODEL="moonshotai/kimi-k2.6" \
    ANTHROPIC_DEFAULT_SONNET_MODEL="moonshotai/kimi-k2.6" \
    ANTHROPIC_DEFAULT_HAIKU_MODEL="moonshotai/kimi-k2.6" \
    CLAUDE_CODE_SUBAGENT_MODEL="moonshotai/kimi-k2.6" \
    CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 \
    claude "$@"
}

or-claude-opus() {
    if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
        echo "ERROR: OPENROUTER_API_KEY is not set." >&2
        return 2
    fi

    ANTHROPIC_BASE_URL="https://openrouter.ai/api" \
    ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY" \
    ANTHROPIC_API_KEY="" \
    ANTHROPIC_DEFAULT_OPUS_MODEL="anthropic/claude-opus-4.6" \
    ANTHROPIC_DEFAULT_SONNET_MODEL="anthropic/claude-sonnet-4.6" \
    CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 \
    claude "$@"
}

or-claude-gpt() {
    if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
        echo "ERROR: OPENROUTER_API_KEY is not set." >&2
        return 2
    fi

    ANTHROPIC_BASE_URL="https://openrouter.ai/api" \
    ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY" \
    ANTHROPIC_API_KEY="" \
    ANTHROPIC_DEFAULT_OPUS_MODEL="openai/gpt-5.4" \
    ANTHROPIC_DEFAULT_SONNET_MODEL="openai/gpt-5.4-mini" \
    CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 \
    claude "$@"
}

or-claude-status() {
    echo "Claude Code routing environment:"
    echo "  ANTHROPIC_BASE_URL       = ${ANTHROPIC_BASE_URL:-<native>}"
    echo "  ANTHROPIC_AUTH_TOKEN     = ${ANTHROPIC_AUTH_TOKEN:+<set, ${#ANTHROPIC_AUTH_TOKEN} chars>}"
    echo "  ANTHROPIC_API_KEY        = ${ANTHROPIC_API_KEY:+<set, ${#ANTHROPIC_API_KEY} chars>}"
    echo "  ANTHROPIC_MODEL          = ${ANTHROPIC_MODEL:-<default>}"
    echo "  SUBAGENT_MODEL           = ${CLAUDE_CODE_SUBAGENT_MODEL:-<default>}"
    echo "  OPENROUTER_API_KEY       = ${OPENROUTER_API_KEY:+<set, ${#OPENROUTER_API_KEY} chars>}"
}

or-claude-clear() {
    unset ANTHROPIC_BASE_URL ANTHROPIC_AUTH_TOKEN ANTHROPIC_API_KEY
    unset ANTHROPIC_DEFAULT_OPUS_MODEL ANTHROPIC_DEFAULT_SONNET_MODEL ANTHROPIC_DEFAULT_HAIKU_MODEL
    unset CLAUDE_CODE_SUBAGENT_MODEL CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC
    echo "Cleared OpenRouter overrides. Claude Code will use native endpoint."
}

# Quick smoke-test: hit OpenRouter directly with a trivial Messages API call.
# Confirms API key works and Anthropic-Skin endpoint is reachable before
# committing to a full Claude Code session.
or-claude-smoke() {
    if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
        echo "ERROR: OPENROUTER_API_KEY is not set." >&2
        return 2
    fi

    local model="${1:-moonshotai/kimi-k2.6}"
    echo "Smoke test — model=${model}"
    curl -sS https://openrouter.ai/api/v1/messages \
        -H "Content-Type: application/json" \
        -H "x-api-key: $OPENROUTER_API_KEY" \
        -H "anthropic-version: 2023-06-01" \
        -d "$(cat <<JSON
{
  "model": "${model}",
  "max_tokens": 128,
  "messages": [
    {"role": "user", "content": "Reply with a single short sentence confirming you received this message. Identify yourself by model name."}
  ]
}
JSON
)" | head -c 2000
    echo
}

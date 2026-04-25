#!/usr/bin/env bash
# PreToolUse hook on WebFetch — corpus URLs MUST route through pipeline fetch / wiki_fetch MCP.
# Exit 0 = allow, exit 2 = block (stderr message goes back to the agent).
#
# Insertion: PreToolUse, matcher=WebFetch
# Reason: Corpus URLs (github.com, raw.githubusercontent.com, youtube.com, youtu.be,
#         arxiv.org, medium.com) must use the project's ingestion pipeline so raw/
#         provenance + ratio gate + source-synthesis authoring proceed correctly.
#         CLAUDE.md Hard Rule 6, .claude/rules/learnings.md #1, .claude/rules/ingestion.md.
# Remediation: ".venv/bin/python -m tools.pipeline fetch <url>" or wiki_fetch MCP.
# Bypass: REASON env var with non-empty value bypasses (for legitimate transient lookups).
#
# Evidence: 2026-04-24 session — agent used WebFetch on 4 corpus URLs the operator
# named for ingestion. The brain (.claude/commands/ingest.md step 1) prescribed
# pipeline fetch; agent ignored. ~30 turns of fallout. Hook prevents recurrence.

set -euo pipefail

INPUT=$(cat)

# Extract URL via python3 stdlib (always available)
URL=$(echo "$INPUT" | python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('url', ''))
except Exception:
    print('')
" 2>/dev/null || echo "")

# If we can't parse, allow (don't break the agent on hook bug)
if [ -z "$URL" ]; then
  exit 0
fi

# Bypass: legitimate transient lookups can set REASON env var
if [ -n "${REASON:-}" ]; then
  exit 0
fi

# Corpus URL patterns — must route through pipeline fetch / wiki_fetch MCP
#
# DESIGN NOTE: this list is INTENTIONALLY narrow. We only block patterns that are
# UNAMBIGUOUSLY single-source ingestion targets (a video to transcribe, a paper to
# scrape). General lookups on github.com (issues, PRs, source files, search) and
# medium.com etc. are NOT blocked — those are valid WebFetch use cases. CLAUDE.md
# Hard Rule 6 + .claude/rules/ingestion.md still apply as instructions for those.
#
# If the agent needs to fetch a github README explicitly for ingestion, it must
# use pipeline fetch / wiki_fetch MCP per the rules. WebFetch is left available
# for non-ingestion lookups.
CORPUS_PATTERNS=(
  "youtube.com/watch"           # single video → transcript-API ingestion
  "youtu.be/"                   # short-form video link → transcript-API ingestion
  "arxiv.org/abs/"              # paper landing page → arxiv-aware ingestion
  "arxiv.org/pdf/"              # paper PDF → arxiv-aware ingestion
)

for pattern in "${CORPUS_PATTERNS[@]}"; do
  if echo "$URL" | grep -qF "$pattern"; then
    cat <<EOF >&2
═══════════════════════════════════════════════════════════════════════════
BLOCKED: WebFetch on corpus URL
═══════════════════════════════════════════════════════════════════════════

URL: $URL
Matched pattern: $pattern

REASON:
  Corpus URLs (github.com / youtube.com / arxiv.org / medium.com / etc.) must
  route through the project's ingestion pipeline. WebFetch is for transient
  lookups, NEVER for corpus ingestion.

  Why: pipeline fetch handles YouTube transcripts (via youtube-transcript-api),
  GitHub README scraping, PDF arxiv-aware fetching — and lands content in raw/
  with proper provenance + the 0.25 source-ratio gate for synthesis pages.
  WebFetch returns auto-summarized content that loses fidelity.

  Rule: CLAUDE.md Hard Rule 6 + .claude/rules/learnings.md #1.

REMEDIATION:
  .venv/bin/python -m tools.pipeline fetch "$URL"

  OR (when in MCP context):
  wiki_fetch MCP tool with url="$URL"

BYPASS for legitimate non-ingestion lookups (rare for these specific patterns):
  Use Bash + curl instead of WebFetch:
    REASON=non-ingestion-lookup curl -sL "$URL"

  (Bash + curl honors the REASON env var; WebFetch cannot. For most lookups
   on github / medium / general web, WebFetch is NOT blocked — only these
   single-source ingestion patterns are.)
═══════════════════════════════════════════════════════════════════════════
EOF
    exit 2
  fi
done

# Not a corpus URL — allow
exit 0

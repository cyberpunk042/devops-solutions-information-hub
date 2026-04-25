# .claude/rules/ingestion.md — URL Ingestion Routing

> Loaded on demand when corpus addition is happening. Detail for the operator-trigger `"ingest <url>"` / `"new ingestions:"` / URL list.

## The Whole Principle of This Project

> Operator directive 2026-04-24 (verbatim):
> "THE WHOLE PRINCIPLE OF THIS PROJECT IS TO CONSUME ARTICLES AND YOUTUBE VIDEOS"

Ingestion is foundational, not a side feature. It must work through the project's own pipeline, not improvised with WebFetch.

## Routing — operator says "ingest" → tool

**Primary:** `wiki_fetch` MCP tool (one URL or list).
**CLI fallback:** `.venv/bin/python -m tools.pipeline fetch <urls>`.
**Forbidden:** WebFetch on corpus URLs (github.com / youtube.com / youtu.be / arxiv.org / medium.com / raw.githubusercontent.com).

The pipeline routes by URL type:
- **YouTube** → `youtube-transcript-api` (venv-only dep) → `raw/transcripts/<slug>.txt`
- **GitHub repo** → README scrape → `raw/articles/<owner-repo>.md`
- **arxiv PDF** → `raw/papers/<paper-id>.md` with metadata
- **Generic web** → `raw/articles/<slug>.md`

The pipeline's `tools/ingest.py` (delegated to from `tools/pipeline.py:fetch_urls`) handles all of these. **Verified working 2026-04-24:** YouTube transcript fetch worked once `.venv/bin/python` was used.

## Operator's Implementation Hints

> Operator directive 2026-04-24 (verbatim, in the URL list message):
> "https://www.youtube.com/watch?v=Edpsu61cwG8 (might want to do TTS with the Wiki here and/or and openclaw|openarms agent)"
>
> "or even: https://github.com/ijin/aidlc-cc-plugin (to take with a grain of salt)"

**Translations:**
- TTS suggestion: for video sources, the wiki could integrate with openclaw or openarms TTS agent. Track as a possible future ingestion enhancement.
- "Grain of salt" annotation: source authority tier matters. When operator flags a source as low-confidence, the synthesis page should reflect that (e.g., `confidence: low` or `medium` in frontmatter, with a warning callout).

## The 6 Steps (from `.claude/commands/ingest.md`)

When operator says "ingest" with arguments:

1. **Fetch:** `.venv/bin/python -m tools.pipeline fetch $ARGUMENTS` — lands in `raw/`.
2. **(if no args):** ask operator for URLs, topics, or pasted content.
3. **Process raws into synthesis pages.** Read raws IN FULL (per AGENTS.md Hard Rule #4: `wc -l` first; offset reads for >200 lines). Author one source-synthesis page per raw, in `wiki/sources/<domain>/src-<slug>.md`. Required ratio: page line-count ≥ 0.25 × raw line-count.
4. **`pipeline post`** after all synthesis pages created. Mandatory. 0 errors required.
5. **`pipeline crossref`** to find new connections.
6. **Report:** pages created, relationships added, new cross-references found.

## Source-Synthesis Page Requirements

Per `wiki/config/artifact-types.yaml` source-synthesis schema:
- **Type:** `source-synthesis`
- **Class:** `documentation`
- **Required sections:** Summary (≥30 words), Key Insights, Relationships
- **Source ratio:** ≥0.25 (page lines / raw lines)
- **Frontmatter:** title, type=source-synthesis, domain, status, confidence, created, updated, sources (with id+type+url|file), tags, layer=1, maturity (seed/growing).
- **Reference card:** `> [!info]` callout with source URL + ingest date is recommended.

Template: `wiki/config/templates/source-synthesis.md` (or scaffold via `pipeline scaffold source-synthesis "<title>"`).

## Depth Verification

> Lesson [[never-synthesize-from-descriptions-alone]] — read the actual source, not the description.

If a source DESCRIBES a tool/format/pattern, you MUST also read a real INSTANCE of that thing before synthesizing. A README about DESIGN.md files is Layer 0 (description); an actual DESIGN.md file is Layer 1 (instance). Synthesis must reach Layer 1.

WebFetch summaries are NOT a substitute. The pipeline's raw/ files contain the real content; read those.

## Hook Enforcement

`.claude/hooks/pre-webfetch-corpus-check.sh` (when wired) blocks WebFetch on corpus URL patterns. Hook design pattern (per [.claude/rules/hook-architecture.md](.claude/rules/hook-architecture.md)):
- **Insertion:** PreToolUse on WebFetch matcher.
- **Reason:** corpus URLs need pipeline fetch for raw/ ingestion + provenance + ratio gate.
- **Remediation:** "Use `.venv/bin/python -m tools.pipeline fetch <url>` or `wiki_fetch` MCP tool."
- **Bypass:** `REASON=transient-lookup` env var on the bash call (rare; for non-ingestion lookups only).

## YouTube Special Case

YouTube ingestion needs the venv (`.venv/bin/python`), not system `python3`, because `youtube-transcript-api` is venv-only. **Always use `.venv/bin/python` for `tools.*` invocations** (CLAUDE.md Hard Rule 5).

If operator points at a YouTube video and the wiki/openclaw/openarms TTS-agent path is preferred over straight transcript-API fetch, route to that agent. Otherwise, default `pipeline fetch <url>` handles transcript-API automatically.

## Cross-references

- `/ingest` operator command: [.claude/commands/ingest.md](.claude/commands/ingest.md)
- Routing master table: [.claude/rules/routing.md](.claude/rules/routing.md)
- Source-synthesis template: [wiki/config/templates/source-synthesis.md](wiki/config/templates/source-synthesis.md)
- Wiki ingestion pipeline (model): [wiki/spine/models/foundation/model-llm-wiki.md](wiki/spine/models/foundation/model-llm-wiki.md) § "Ingest" operation
- Hook architecture: [.claude/rules/hook-architecture.md](.claude/rules/hook-architecture.md)
- Lesson [[never-synthesize-from-descriptions-alone]]: [wiki/lessons/](wiki/lessons/)

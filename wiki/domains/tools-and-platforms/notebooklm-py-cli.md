---
title: "notebooklm-py CLI"
type: concept
layer: 2
maturity: growing
domain: tools-and-platforms
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-notebooklm-py-official
    type: documentation
    url: "https://github.com/teng-lin/notebooklm-py"
    file: raw/articles/notebooklm-py-official-docs.md
    title: "notebooklm-py — Official Documentation"
    ingested: 2026-04-08
  - id: src-claude-world-notebooklm-skill
    type: documentation
    url: "https://github.com/claude-world/notebooklm-skill"
    file: raw/articles/claude-worldnotebooklm-skill.md
    title: "claude-world/notebooklm-skill"
    ingested: 2026-04-08
  - id: src-pleaseprompto-notebooklm-skill
    type: documentation
    url: "https://github.com/PleasePrompto/notebooklm-skill"
    file: raw/articles/pleasepromptonotebooklm-skill.md
    title: "PleasePrompto/notebooklm-skill"
    ingested: 2026-04-08
tags: [notebooklm, cli, python, api, automation, browser-automation, content-pipeline, agent-tools, google, research-tool]
---

# notebooklm-py CLI

## Summary

notebooklm-py is an unofficial Python package (9.5k GitHub stars, MIT licensed) that provides full programmatic access to Google NotebookLM via CLI, Python async API, and AI agent skill/MCP integration. It exposes capabilities beyond the web UI — batch artifact downloads, structured quiz/flashcard export (JSON/Markdown/HTML), mind map JSON extraction, data table CSV export, slide deck PPTX, individual slide revision, and programmatic sharing. The CLI covers notebook management, source ingestion (URLs, files, web research), chat with source-grounded Q&A, generation of 10 artifact types (audio, video, cinematic video, quizzes, flashcards, slides, infographics, mind maps, data tables, reports), and export/download of all artifacts. Authentication uses browser-based Google OAuth with local credential storage. The package integrates natively with Claude Code, Codex, and OpenClaw via `notebooklm skill install`.

## Key Insights

> [!info] Full NotebookLM automation — 10 artifact types, all scriptable
>
> | Artifact | Formats | Pipeline Value |
> |----------|---------|---------------|
> | Audio | MP3, 4 formats, 3 lengths, 50+ languages | Podcast distribution |
> | Video / Cinematic | MP4, 3 formats, 9 styles | Content production |
> | Quizzes / Flashcards | JSON, Markdown, HTML | Parseable for wiki ingestion |
> | Slide Decks | PDF, PPTX | Export targets |
> | Infographics | PNG | Visual content |
> | Mind Maps | JSON | Graph data → wiki relationship candidates |
> | Data Tables | CSV | Structured comparison data |
> | Reports | PDF | Research synthesis export |

> [!tip] Source-grounded Q&A + web research from the terminal
> `notebooklm ask "<question>"` queries loaded sources with citations (`--json` for structured output, `--save-as-note` to persist). `notebooklm source add-research "<query>"` triggers NotebookLM's web research agent — fast mode for quick results, deep mode for comprehensive source discovery.

**Async Python API for pipeline integration.** `NotebookLMClient` with namespaced operations (notebooks, sources, chat, artifacts, research, notes, sharing) — all async, supporting concurrent operations.

**Agent skill installation.** `notebooklm skill install` drops skill files into Claude Code and agents. Also `npx skills add teng-lin/notebooklm-py`. Context-based workflow: `notebooklm use <id>` sets active notebook for subsequent commands.

> [!warning] Browser automation — no official API
> Uses Playwright/Patchright for browser automation since no official NotebookLM API exists. Authentication requires a real browser session. Vulnerable to web UI changes. Rate limiting under heavy automated use. Session expiration requires re-auth logic for long-running daemons. This is the single biggest production risk.

## Deep Analysis

### Role in the Research Wiki Pipeline

notebooklm-py transforms NotebookLM from an interactive web tool into a programmable node in the research pipeline. The integration points for this project:

1. **Source mirroring**: Wiki sources ingested via `tools/ingest.py` can be simultaneously pushed to NotebookLM notebooks via `notebooklm source add`. This creates a parallel knowledge base where NotebookLM's Gemini-powered analysis complements the wiki's structured synthesis.

2. **Research amplification**: When gap analysis (`tools/lint.py`) identifies under-connected domains or missing concepts, `notebooklm source add-research "<topic>"` can automatically discover and import relevant sources. The deep research mode is particularly powerful for finding primary sources that simple web search misses.

3. **Cross-validation**: `notebooklm ask` can query sources with specific questions to validate wiki page claims. If the wiki says "X contradicts Y," NotebookLM can independently verify from the same sources. This is a second opinion from a different LLM (Gemini vs Claude).

4. **Content generation pipeline**: For the AICP and openfleet export targets, NotebookLM artifacts (slide decks, reports, audio overviews) could supplement wiki exports. A wiki page about "LLM Wiki Pattern" could also produce a NotebookLM audio overview for podcast distribution.

5. **Structured data extraction**: `notebooklm generate data-table` + `notebooklm download data-table ./file.csv` could extract structured comparisons from source material, feeding directly into wiki comparison pages.

### CLI Command Architecture

The CLI is organized hierarchically via Python Click:

| Group | Key Commands | Pipeline Value |
|-------|-------------|---------------|
| Notebooks | create, list, use, delete | Workspace management |
| Sources | add, add-research, list, fulltext | Ingestion pipeline |
| Chat | ask [--json] [--save-as-note] | Query + validation |
| Generate | audio, video, quiz, flashcards, slides, infographic, mind-map, data-table, report | Content production |
| Download | all artifact types in multiple formats | Export pipeline |
| Sharing | status, permissions | Collaboration |
| Agent | show, skill install/status | Integration setup |

### Python API for Pipeline Integration

The async API is the more powerful integration path for automated pipelines:

```python
async with await NotebookLMClient.from_storage() as client:
    # Create notebook per research topic
    nb = await client.notebooks.create("LLM Wiki Research")
    
    # Mirror wiki sources
    for url in wiki_source_urls:
        await client.sources.add_url(nb.id, url)
    
    # Generate artifacts
    await client.artifacts.generate_audio(nb.id)
    await client.artifacts.generate_mind_map(nb.id)
    
    # Download structured data
    await client.artifacts.download_mind_map(nb.id, "./mind-map.json")
    
    # Cross-validate
    result = await client.chat.ask(nb.id, 
        "What contradictions exist between these sources?")
```

### Structured exports fill a critical gap

The web UI only shows artifacts inline. notebooklm-py enables downloading quizzes as JSON (parseable), flashcards as Markdown (ingestable), mind maps as JSON (graph data), and data tables as CSV (analyzable). These structured formats are what automated pipelines need.

## Open Questions

- What are the practical rate limits for automated NotebookLM usage before Google throttles or blocks the account? (Requires: empirical measurement under sustained load; the `--retry` flag with exponential backoff is documented as the mitigation, but no wiki page specifies concrete thresholds)
- Will Google release an official NotebookLM API that makes browser automation unnecessary? (Requires: external announcement from Google; no existing wiki page covers this)

## Answered Open Questions

> [!example]- Should notebooklm-py be wrapped as an MCP server?
> Technically possible but architecturally inadvisable. MCP would load all tool schemas into every session. The correct architecture: CLI tool + Claude Code skill — load when needed, not registered as persistent overhead. PleasePrompto has a companion MCP server (TypeScript) for cross-context discoverability if needed, but CLI+Skill is preferred when NotebookLM is one of several tools.

> [!example]- How does add-research deep mode compare to tools/ingest.py?
> Complementary, not competing. `add-research` discovers sources (topic → primary sources loaded into notebook). `tools/ingest.py` produces wiki pages from known URLs. The two compose: deep mode as topic-to-sources discovery step → ingest.py processing discovered URLs into wiki pages.

> [!example]- NotebookLM (Gemini) vs wiki (Claude) accuracy?
> Different strengths. NotebookLM: source-faithful retrieval with citations — reliable for "what do these sources say?" The wiki: cross-domain synthesis, pattern recognition, relationship mapping across many sources. NotebookLM wins on grounding accuracy; wiki wins on emergent synthesis. They are different services in a layered architecture.

> [!example]- Can notebook metadata sync bidirectionally with manifest.json?
> Architecturally feasible via async API. Diff manifest.json source URLs against `notebooklm source list`; call `source add` for missing items in either direction. Requires a mapping table (notebook ID → wiki domain) since structures may differ.

## Relationships

- BUILDS ON: [[NotebookLM]]
- EXTENDS: [[NotebookLM Skills]]
- ENABLES: [[AI-Driven Content Pipeline]]
- PARALLELS: [[Obsidian CLI]]
- RELATES TO: [[Claude Code Skills]]
- RELATES TO: [[Wiki Ingestion Pipeline]]
- RELATES TO: [[LLM Wiki Pattern]]
- ENABLES: [[Wiki Event-Driven Automation]]

## Backlinks

[[NotebookLM]]
[[NotebookLM Skills]]
[[AI-Driven Content Pipeline]]
[[Obsidian CLI]]
[[Claude Code Skills]]
[[Wiki Ingestion Pipeline]]
[[LLM Wiki Pattern]]
[[Wiki Event-Driven Automation]]
[[Claude Code]]
[[MCP Integration Architecture]]
[[Model: NotebookLM]]
[[Research Pipeline Orchestration]]

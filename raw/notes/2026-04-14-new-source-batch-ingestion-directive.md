# Directive — New Source Batch Ingestion (2026-04-14)

## Operator Words (Verbatim)

> "before we crystalize all this we are going to integrated a bunch of new source and we are going to process them through all the levels up to the deep integration."

> "Remember a source is not always only one pages..... its the amount of page needed for the given sources to understand it fully. that it require drilling down or searching the web at large. We cannot allow ourself to be lazy or discard important stuff like standards we need to adhere too.."

> "Buckle up. I never said they were all equal but we have to find the important part of each or discard them if really needed but I doubt it"

> "We can improve the fundation and infrastructure first if it make the ingestion of those easier and better. Obviously standards are the most important things"

## Sources Provided

### Tier 1 — Likely High Impact (methodologies, standards, frameworks)
1. https://github.com/Fission-AI/OpenSpec — spec framework
2. https://github.com/github/spec-kit — GitHub spec toolkit
3. https://github.com/bmad-code-org/BMAD-METHOD — methodology framework

### Tier 2 — Ecosystem and Agent Architecture
4. https://github.com/tirth8205/code-review-graph — code review patterns
5. https://github.com/zacdcook/openclaw-billing-proxy — ecosystem (OpenClaw)
6. https://code.claude.com/docs/en/agent-sdk/python — Claude Agent SDK
7. https://platform.claude.com/docs/en/managed-agents/tools — Managed Agents tools
8. https://github.com/vercel-labs/opensrc — Vercel open source toolkit

### Tier 3 — Skills, Config, LLM Patterns
9. https://gist.github.com/roman01la/483d1db15043018096ac3babf5688881 — (TBD)
10. https://www.termdock.com/blog/skill-md-vs-claude-md-vs-agents-md#a-working-example — skill/claude/agents config comparison
11. https://pydantic.dev/docs/ai/overview/ — Pydantic AI
12. https://sebastianraschka.com/llm-architecture-gallery/ — LLM architectures

### Tier 4 — Articles, Guides, Research
13. https://dev.to/samchon/autobe-qwen-35-27b-just-built-complete-backends-from-scratch-100-compilation-25x-cheaper-lmd — AutoBE local LLM
14. https://www.infoworld.com/article/4152738/27-questions-to-ask-before-choosing-an-llm.html — LLM selection criteria
15. https://www.eweek.com/news/claude-ai-anthropic-guide-2026/ — Claude AI guide 2026

### Tier 5 — Video (transcripts needed)
16. https://www.youtube.com/watch?v=kQu5pWKS8GA
17. https://www.youtube.com/watch?v=ZgwHaI2C-9s

## Interpretation

This is E021 executing ahead of schedule. The operator wants DEEP ingestion — not surface summaries but full understanding that requires drilling down into repos, reading READMEs AND actual code/specs, and searching the web for context. Each source produces as many wiki pages as needed. Standards and methodology sources get priority treatment.

## Requirements

1. Fetch all sources into raw/
2. Read each source DEEPLY — README + actual specs + code where relevant
3. For repos: read the actual spec/method files, not just the README
4. Produce wiki pages at all levels: L1 synthesis, L2 concepts, cross-references to existing pages
5. Update existing models/standards where new knowledge applies
6. Do not discard — find the important parts of each

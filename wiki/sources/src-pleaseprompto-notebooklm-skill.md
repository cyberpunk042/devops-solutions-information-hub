---
title: "Synthesis: PleasePrompto/notebooklm-skill"
type: source-synthesis
domain: tools-and-platforms
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-08
sources:
  - id: src-pleaseprompto-notebooklm-skill
    type: documentation
    url: "https://github.com/PleasePrompto/notebooklm-skill"
    file: raw/articles/pleasepromptonotebooklm-skill.md
    title: "PleasePrompto/notebooklm-skill"
    ingested: 2026-04-08
tags: [notebooklm, claude-code, skill, source-grounded, browser-automation, python]
---

# Synthesis: PleasePrompto/notebooklm-skill

## Summary

This repository provides a Claude Code Skill that lets Claude directly query Google NotebookLM for source-grounded, citation-backed answers based exclusively on uploaded documents. The skill uses browser automation (Patchright, a Playwright-based library) to open NotebookLM in a headless Chrome instance, submit questions, and return answers to Claude Code programmatically. It focuses on eliminating hallucinations by grounding all responses in user-uploaded documents rather than general training data. The skill operates in a stateless model where each question opens a fresh browser session, asks the question, retrieves the answer with a follow-up prompt, and closes. A library management system lets users save NotebookLM notebook links with tags and descriptions so Claude can auto-select the right notebook for each query.

## Key Insights

- **Anti-hallucination focus**: The primary value proposition is reducing hallucinations by constraining answers to user-uploaded documents in NotebookLM. The README explicitly compares this to feeding docs directly to Claude (high hallucination) and local RAG (medium hallucination), positioning NotebookLM as the lowest-hallucination option.

- **Stateless session model**: Each question opens a fresh browser, asks the question, gets the answer, and closes. This contrasts with the companion MCP server version which maintains persistent chat sessions. The tradeoff is simplicity and reliability versus conversational context.

- **Follow-up prompting pattern**: Each answer includes "Is that ALL you need to know?" to prompt Claude to ask comprehensive follow-up questions, compensating for the lack of persistent sessions by encouraging multi-query research within a single user interaction.

- **Smart library management**: Users can save NotebookLM notebooks with metadata (name, topics, tags) and Claude auto-selects the appropriate notebook based on the user's question. This creates a persistent knowledge routing layer on top of ephemeral query sessions.

- **Local-only constraint**: The skill works only with local Claude Code installations, not the web UI, because it requires network access for browser automation. This is a fundamental architectural constraint.

- **Human-like automation**: Uses realistic typing speeds and interaction patterns (via Patchright) to avoid detection by Google services, acknowledging the gray area of browser automation against web services.

- **Companion MCP server**: The same author maintains a TypeScript-based MCP server version (PleasePrompto/notebooklm-mcp) with persistent sessions and multi-tool support (Codex, Cursor). The skill and MCP versions serve different use cases.

- **Self-contained environment**: Everything runs in an isolated Python virtual environment within the skill folder, with auto-installation of dependencies including Chrome on first use.

## Deep Analysis

This skill takes a fundamentally different approach from claude-world/notebooklm-skill. While claude-world builds a content production pipeline (research to article to publishing), PleasePrompto focuses on a single, focused use case: letting Claude Code query NotebookLM as a knowledge source to produce better, grounded code and answers.

The stateless architecture is a deliberate design choice that trades capability for reliability. By not maintaining browser sessions, the skill avoids the complexity of session management, timeouts, and state corruption. Each query is independent and self-contained. The follow-up prompting pattern ("Is that ALL you need to know?") is a clever workaround that shifts the multi-turn conversation burden from the browser session to Claude's own conversation context.

The comparison table in the README (feeding docs to Claude vs web search vs local RAG vs NotebookLM) frames NotebookLM as a superior alternative to local RAG for document-grounded Q&A. This positioning is noteworthy: it suggests that for use cases where the document corpus fits within NotebookLM's limits, the effort of setting up local RAG infrastructure may be unnecessary.

The library management feature adds a layer of intelligence absent from simpler integrations. By maintaining metadata about which notebooks contain what topics, the skill creates a routing mechanism that automatically directs questions to the right knowledge source. This is analogous to a manual version of the routing step in agentic RAG architectures.

## Open Questions

- How does Google's detection of automated browser usage affect long-term reliability? (Requires: empirical longitudinal data from production deployments; the notebooklm-py CLI page documents "No official API: entire package relies on browser automation" as the single biggest risk, and PleasePrompto uses stealth techniques, but no wiki page quantifies actual detection rates over time)
- What is the performance overhead of opening and closing a Chrome instance for every question? (Requires: empirical timing data from real usage; no existing wiki page covers per-query browser startup latency for Patchright-based automation)

### Answered Open Questions

**Q: How does the stateless model perform for complex multi-step research that benefits from conversational context?**

Cross-referencing `NotebookLM Skills` and `notebooklm-py CLI`: the `NotebookLM Skills` page documents the tradeoff explicitly in its Key Insights section: "Stateful vs. stateless sessions: claude-world maintains notebook context across operations within a pipeline run. PleasePrompto uses a stateless model where each question opens a fresh browser, asks, retrieves, and closes. The stateless approach trades conversational context for reliability and simplicity." The `NotebookLM Skills` page further documents the follow-up prompting pattern as the architectural workaround: "PleasePrompto compensates for its stateless model by appending 'Is that ALL you need to know?' to each answer, prompting Claude to ask follow-up questions. This shifts multi-turn research from the browser session to Claude's conversation context." For complex multi-step research, this means the stateless model is adequate as long as Claude's own conversation context accumulates the research findings across multiple independent queries — the browser session carries no state, but Claude's context window does. The `notebooklm-py CLI` page confirms that session state management is a real risk for long-running operations ("Browser automation sessions can expire, requiring re-authentication"), which reinforces the stateless design as a reliability choice at the cost of conversational continuity within NotebookLM itself.

**Q: What are the practical limits of the library routing mechanism when a user has dozens of notebooks?**

Cross-referencing `NotebookLM Skills`: the `NotebookLM Skills` page addresses this directly in its Answered section: "For PleasePrompto's library routing, the practical limit is not determined by source count... but by the number of distinct notebooks in the library index. Reliability degrades when the metadata tags are ambiguous — when two notebooks have overlapping topic coverage and Claude must select between them." The page further documents the mitigation: "The `notebooklm profile create/switch` commands support multi-profile isolation, which is the recommended architectural response to notebook sprawl." The `notebooklm-py CLI` page confirms that NotebookLM has a 300-source limit per notebook, and large-scale research requires multi-notebook architectures. The `NotebookLM Skills` page notes that "the `src-notebooklm-claude-code-workflow` synthesis recommends configuring NotebookLM's response format... to reduce per-query token cost, which also helps library routing by keeping notebook descriptions compact and differentiable." Practical guidance from wiki cross-references: the routing degrades at the point where notebook topic descriptions overlap significantly — the solution is to make descriptions as distinct as possible and use profile isolation to partition sprawl by domain.

## Relationships

- DERIVED FROM: src-pleaseprompto-notebooklm-skill
- FEEDS INTO: NotebookLM Skills
- EXTENDS: Claude Code Skills
- RELATES TO: NotebookLM
- COMPARES TO: src-claude-world-notebooklm-skill

## Backlinks

[[src-pleaseprompto-notebooklm-skill]]
[[NotebookLM Skills]]
[[Claude Code Skills]]
[[NotebookLM]]
[[src-claude-world-notebooklm-skill]]

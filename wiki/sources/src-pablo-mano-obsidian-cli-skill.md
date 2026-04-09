---
title: "Synthesis: pablo-mano/Obsidian-CLI-skill"
type: source-synthesis
domain: tools-and-platforms
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-08
sources:
  - id: src-pablo-mano-obsidian-cli-skill
    type: documentation
    url: "https://github.com/pablo-mano/Obsidian-CLI-skill"
    file: raw/articles/pablo-manoobsidian-cli-skill.md
    title: "pablo-mano/Obsidian-CLI-skill"
    ingested: 2026-04-08
tags: [obsidian, cli, claude-code, skill, vault-management, cross-agent, cursor, copilot]
---

# Synthesis: pablo-mano/Obsidian-CLI-skill

## Summary

This repository provides a comprehensive Claude Code skill (and multi-agent compatible plugin) that enables AI agents to control Obsidian vaults through the official Obsidian CLI introduced in v1.12. It covers 130+ commands across all major vault operation areas: file CRUD, daily notes, full-text search, properties, tags, tasks, links, bookmarks, templates, plugins, sync, themes, snippets, commands, bases, history, workspace, diff, developer tools, and vault management. The skill supports installation on Claude Code (as a marketplace plugin), Cursor, Cortex Code, GitHub Copilot, Windsurf, Nanoclaw, and Openclaw, making it the most broadly compatible Obsidian skill available. It requires Obsidian Desktop v1.12+ with CLI enabled and the desktop app running (CLI communicates over IPC).

## Key Insights

- **130+ commands for full vault control**: This is the most comprehensive Obsidian CLI skill available, covering files, daily notes, search, properties, tags, tasks, links, bookmarks, templates, plugins, sync, themes, snippets, commands, bases, history, workspace, diff, developer tools, and vault administration.

- **Broadest agent compatibility**: Installation instructions cover 8 different AI agents/editors: Claude Code (plugin marketplace, direct load, settings.json), Cursor (native skills system), Cortex Code (remote install, project-local, user-level), GitHub Copilot (repository-wide or path-scoped custom instructions), Windsurf (rules system), Nanoclaw, Openclaw, and any agent with a system prompt field.

- **Requires running desktop app**: The CLI communicates with Obsidian over IPC, meaning the desktop application must be running. This is an architectural constraint that limits headless/server automation scenarios, though xvfb workarounds exist for headless Linux.

- **Natural language or explicit invocation**: The skill activates automatically when requests clearly involve Obsidian vault operations, but also supports explicit prefix invocation ($obsidian-cli) and strict mode (always loaded).

- **Platform-specific gotchas documented**: The README documents detailed troubleshooting for Windows (admin terminal failures, missing .com redirector), Linux (snap confinement, xvfb for headless, PrivateTmp issues), and cross-platform unicode bugs fixed in v1.12.2+.

- **Plugin marketplace distribution**: Uses Claude Code's marketplace system via a .claude-plugin/marketplace.json manifest, enabling one-command installation (/plugin marketplace add).

- **SKILL.md as universal format**: The README demonstrates that the SKILL.md format is portable across agent platforms. For agents without native skill support, the markdown content can be pasted directly into system prompts or custom instruction fields.

## Deep Analysis

This skill represents the deepest integration between an AI agent and Obsidian, leveraging the official CLI rather than browser automation or file-system manipulation. The 130+ command coverage means an AI agent with this skill has essentially the same level of vault control as a human user in the Obsidian UI.

The broad compatibility across 8+ agent platforms is a deliberate strategy. By providing installation instructions for Claude Code, Cursor, Cortex Code, Copilot, Windsurf, Nanoclaw, and Openclaw, the skill maximizes its potential user base while demonstrating that SKILL.md-format skills are not locked to any single platform.

The IPC communication model (requiring the desktop app to be running) is both a strength and a limitation. It provides full access to Obsidian's capabilities through the official API, ensuring reliability and feature coverage. However, it prevents the skill from being used in CI/CD pipelines, cloud environments, or fully headless servers without workarounds.

Compared to kepano/obsidian-skills which includes an obsidian-cli skill among its five skills, this repository goes dramatically deeper on CLI coverage specifically. The 130+ commands vs. the brief description in kepano's cli skill suggest this is a much more complete reference for AI agents that need comprehensive vault management capabilities.

## Open Questions

- How does performance scale with vault size when running commands like full-text search or orphan detection? (Requires: empirical benchmarking with large vaults; the Obsidian CLI page notes this as an open question and no wiki page documents CLI latency at scale)
- What is the maintenance burden of keeping the skill updated as Obsidian CLI evolves? (Requires: external observation over time; no wiki page documents the update cadence of the Obsidian CLI skill relative to Obsidian CLI releases)

### Answered Open Questions

**Q: Can the skill be extended to trigger Obsidian community plugin commands via the CLI?**

Cross-referencing `Obsidian CLI` and `Obsidian Skills Ecosystem`: the Obsidian CLI page documents a direct answer: "Does `obsidian eval` have access to community plugin APIs, enabling automation of Dataview queries, Templater scripts, and other plugin-specific operations? (Requires: external testing against community plugin APIs; the Obsidian Skills Ecosystem page describes what community plugins expose but does not document whether `eval` can invoke their APIs)." The `eval code=<js>` command "executes arbitrary JavaScript in the Obsidian context" — since community plugins register their APIs into the Obsidian app context, `eval` is the plausible mechanism for invoking them. However, no wiki page documents this as confirmed behavior. The pablo-mano skill's 130+ commands cover the official Obsidian CLI surface; community plugin extension is a separate capability layer that would require either `eval`-based workarounds or community plugin CLI hooks (not yet documented). The practical answer from existing wiki knowledge: the IPC-based CLI provides the `eval` command as a potential extension point, but community plugin triggering is not a documented, supported workflow in any existing wiki page.

**Q: How does the IPC-based CLI handle concurrent access from multiple AI agents?**

Cross-referencing `Obsidian CLI` and `WSL2 Development Patterns`: the Obsidian CLI page lists concurrent access as an open question: "How does the CLI handle concurrent access — can multiple scripts issue commands simultaneously without conflicts? (Requires: external testing or Obsidian documentation on IPC concurrency; no existing wiki page covers this)" — confirming no wiki page documents concurrent IPC behavior. The WSL2 Development Patterns page provides useful architectural context: the current project design avoids concurrent Obsidian access by using a two-daemon architecture where the wiki-watcher daemon detects changes and triggers the post-chain sequentially, and the wiki-sync daemon separately copies results to Windows. This sequential architecture sidesteps IPC concurrency concerns by design. For multi-agent scenarios where concurrent CLI access would be required, the WSL2 page notes the CLI must run on the same OS as the app, adding a coordination constraint. The wiki's current recommendation from these pages: design agent workflows to avoid concurrent Obsidian CLI calls; if concurrency is required, implement a command queue at the orchestration layer rather than relying on IPC to handle simultaneous requests safely.

## Relationships

- DERIVED FROM: src-pablo-mano-obsidian-cli-skill
- FEEDS INTO: Obsidian Skills Ecosystem
- EXTENDS: Claude Code Skills
- RELATES TO: Obsidian Knowledge Vault
- COMPARES TO: src-kepano-obsidian-skills

## Backlinks

[[src-pablo-mano-obsidian-cli-skill]]
[[Obsidian Skills Ecosystem]]
[[Claude Code Skills]]
[[Obsidian Knowledge Vault]]
[[src-kepano-obsidian-skills]]

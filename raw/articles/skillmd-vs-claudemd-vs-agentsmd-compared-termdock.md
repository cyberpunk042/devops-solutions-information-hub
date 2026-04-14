# SKILL.md vs CLAUDE.md vs AGENTS.md — Compared

Source: https://www.termdock.com/blog/skill-md-vs-claude-md-vs-agents-md
Ingested: 2026-04-14
Type: article

---

## Core Distinction

These three files serve different purposes in AI agent configuration:

- **CLAUDE.md**: Project context loaded at every Claude Code session
- **AGENTS.md**: Cross-tool project context recognized by multiple CLI tools
- **SKILL.md**: On-demand task-specific capabilities loaded conditionally

## Comparison Table

| Aspect | SKILL.md | CLAUDE.md | AGENTS.md |
|--------|----------|-----------|-----------|
| Purpose | Task capability | Project context | Project context |
| Scope | Per-task (loaded when relevant) | Per-session (always loaded) | Per-session (always loaded) |
| Location | `.claude/skills/` | Project root | Project root |
| Read by | Claude Code, Codex CLI, Copilot CLI, Gemini CLI | Claude Code | Multiple tools across ecosystem |
| Can execute scripts | Yes | No | No |
| Auto-trigger capability | Yes (by description match) | Always active | Always active |
| Recommended size | <500 lines per skill | <100 lines | <100 lines |

## Key Finding: ETH Zurich Research (Feb 2026)

Research showing "LLM-generated context files reduced task success rates by approximately 3%" compared to no context file, while human-written files improved success by only 4%. Underscores keeping context files lean.

## Strategic Recommendations

**AGENTS.md as canonical source**: Maintain AGENTS.md as the single source of truth for project context, especially when using multiple AI tools. CLAUDE.md should remain minimal and reference AGENTS.md.

**Three-layer architecture**:
1. Layer 1 (AGENTS.md): Always-on, cross-tool universal context under 100 lines
2. Layer 2 (CLAUDE.md): Minimal Claude-specific instructions under 20 lines
3. Layer 3 (Skills): Detailed task workflows (up to 500 lines each) loaded on demand

## Working Examples

CLAUDE.md example:
- Project overview (e-commerce API, 50k DAU)
- Architecture (Node.js 22, Fastify 5, PostgreSQL 16, Drizzle ORM)
- Code conventions (Result pattern, Zod schemas, repository organization)
- Hard constraints (migration file restrictions, no default exports)
- Command references

Database migration skill example: structured workflow with YAML frontmatter containing name and description fields.

## Common Implementation Errors

1. **Oversized CLAUDE.md files** (300+ lines reduce agent performance)
2. **Neglecting skills entirely** (missing specialized workflow capabilities)
3. **Content duplication** across multiple files requiring synchronization
4. **AI-generated context files** that underperform hand-written versions
5. **Tool lock-in** from relying exclusively on CLAUDE.md instead of AGENTS.md

## Decision Flowchart

- Applies to every project task? → AGENTS.md or CLAUDE.md
- Specialized multi-step workflow? → Skill
- Needs script execution? → SKILL.md
- Multi-tool usage? → AGENTS.md primary + CLAUDE.md for Claude-specific details

## Cross-Tool Ecosystem Context

AGENTS.md adoption spans 60,000+ open-source repositories under Linux Foundation stewardship as the Agentic AI Foundation standard. Compatible tools: Codex CLI, Copilot CLI, Gemini CLI, Cursor, Claude Code.

Claude Code reads BOTH CLAUDE.md and AGENTS.md, creating flexibility for teams transitioning between different AI tools without requiring separate context management systems.

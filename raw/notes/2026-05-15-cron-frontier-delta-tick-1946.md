# Cron tick — frontier delta check, 2026-05-15 19:46 ET

Operator-stated job (verbatim, sacrosanct):
> "Do research to make sure the models are up to date and our vision of the technogies are still acquire, AND WE DO THE PROPER UPDATE AND ETC..."

Treatment: This is a do-the-work directive, not surfacing-only. The "proper update" part is load-bearing. Anti-pattern: writing a research-watch log that says "I found these items, deferring full synthesis." Either do the work or don't surface it.

This tick's monitoring-surface scan output (web_search, NEVER WebFetch on corpus URLs per Hard Rule 6):

Candidates:
1. Claude Opus 4.7 (Apr 16, 2026) — ALREADY in corpus (two syntheses) — skip.
2. GPT-5.5 (Apr 24, 2026) — ALREADY in corpus (src-gpt-5-5-openai-frontier-2026-04-23.md) — skip baseline.
2b. GPT-5.5 Instant (May 5, 2026) — downstream variant, 52.5% hallucination reduction claim, default ChatGPT model — novel but downstream. Flag for follow-up tick.
3. Anthropic 10 Finance Agents + M365 (May 5, 2026) — enterprise vertical, lower vision-relevance. Skip.
4. Anthropic + Gates Foundation $200M (May 13), Claude for Small Business (May 6) — partnership/distribution, not model/runtime — skip.
5. Microsoft Agent Governance Toolkit (Apr 2, 2026) — MIT-licensed, runtime security for AI agents, OWASP Agentic Top 10 coverage, deterministic sub-millisecond policy enforcement, 13,000+ tests. NOT in corpus. Vision-relevant: touches operator's stack (OpenClaw/OpenArms/OpenFleet are all agent-runtime infrastructure). **HIGHEST IMPACT NOVEL. Process end-to-end this tick.**

Selection: #5 (Microsoft Agent Governance Toolkit). Follow-up needed for #2b (GPT-5.5 Instant) — log to operator-decision-queue.md.

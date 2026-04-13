# Lessons

Structured failure analysis and convergence insights synthesized from real incidents, post-mortems, and cross-source pattern detection. Every lesson has a trigger, a finding, and an action.

**Model:** [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] | **Standards:** [[model-quality-failure-prevention-standards|Quality Standards — What Good Failure Prevention Looks Like]]

### Start Here

1. [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] — The root failure lesson
2. [[llm-maintained-wikis-outperform-static-documentation|LLM-Maintained Wikis Outperform Static Documentation]] — The root convergence lesson
3. [[Agent Orchestration Is the Highest-Connected Concept in the Wiki]] — The most connected hub

### Failure Lessons

Hard-won rules from post-mortems and agent death analyses.

| Lesson | Core finding |
|--------|-------------|
| [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] | Documenting methodology without following it is the deepest failure |
| [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]] | "Get started" means the current stage, not "skip to the end" |
| [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]] | A README about a format is not understanding the format |
| [[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic, Not Isolated]] | Subagents consistently read only ~60 lines of 300-1000+ line files |
| [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]] | Never manually create systemd/cron; build into reproducible tooling |
| [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]] | Models follow SFIF: scaffold, fill, iterate, finish |

### Practice Lessons

Operational patterns that improve agent effectiveness.

| Lesson | Core finding |
|--------|-------------|
| [[always-plan-before-executing|Always Plan Before Executing]] | Explicit plans before action produce dramatically better results |
| [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] | CLI + skill files outperform MCP for token efficiency |
| [[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]] | Context window management is the biggest productivity multiplier |
| [[multi-stage-ingestion-beats-single-pass|Multi-Stage Ingestion Beats Single-Pass Processing]] | Extract, cross-reference, identify gaps, deepen — not one-shot |

### Convergence Lessons

Independent sources arriving at the same conclusion.

| Lesson | Core finding |
|--------|-------------|
| [[llm-maintained-wikis-outperform-static-documentation|LLM-Maintained Wikis Outperform Static Documentation]] | LLM maintenance with validation and quality gates beats static docs |
| [[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]] | Bundled markdown packages are the dominant extension pattern |
| [[graph-enhanced-retrieval-bridges-wiki-and-vector-search|Graph-Enhanced Retrieval Bridges Wiki Navigation and Vector Search]] | Wiki navigation vs vector RAG is a false binary |
| [[automated-knowledge-validation-prevents-wiki-decay|Automated Knowledge Validation Prevents Silent Wiki Decay]] | Wikis without automated validation decay silently |
| [[obsidian-as-knowledge-infrastructure|Obsidian as Knowledge Infrastructure Not Just Note-Taking]] | Obsidian is programmable knowledge infrastructure, not a markdown editor |
| [[notebooklm-as-grounded-research-engine|NotebookLM as Grounded Research Engine Not Just Note Storage]] | NotebookLM is a grounded research engine, not just note storage |
| [[wiki-maintenance-problem-solved-by-llm-automation|The Wiki Maintenance Problem Is Solved by LLM Automation]] | LLMs solve the maintenance burden that killed every previous wiki attempt |
| [[skill-specification-is-key-to-interoperability|Skill Specification Is the Key to Ecosystem Interoperability]] | Open specification roots make skills portable across platforms |
| [[Schema Is the Real Product — Not the Content]] | The schema file is the real product; content is generated from it |

### Domain Hubs

Lessons that synthesize an entire domain's structural position.

| Lesson | Domain |
|--------|--------|
| [[Agent Orchestration Is the Highest-Connected Concept in the Wiki]] | ai-agents |
| [[Automation Is the Bridge Between Knowledge and Action]] | automation |
| [[Knowledge Systems Is the Foundational Domain for the Entire Wiki]] | knowledge-systems |

## Pages

- [Agent Failure Taxonomy — Seven Classes of Behavioral Failure](03_validated/agent-failure-taxonomy-seven-classes-of-behavioral-failure.md) — After infrastructure enforcement solves stage boundary violations (75% → 0%), six classes of BEHAVIORAL failure remain
- [Lesson — Agent Orchestration Is the Highest-Connected Concept in the Wiki](03_validated/agent-orchestration-is-highest-connected-concept.md) — Agent Orchestration Patterns is the most inbound-linked concept in the ai-agents domain
- [Always Plan Before Executing](03_validated/always-plan-before-executing.md) — LLM agents produce dramatically better results when they produce an explicit plan before taking action — not as a sof...
- [Automated Knowledge Validation Prevents Silent Wiki Decay](03_validated/automated-knowledge-validation-prevents-wiki-decay.md) — Wikis without automated validation decay silently: pages go stale, relationships break, orphaned concepts accumulate,...
- [Lesson — Automation Is the Bridge Between Knowledge and Action](03_validated/automation-is-bridge-between-knowledge-and-action.md) — The automation domain occupies a distinct structural position in this wiki: it bridges what the knowledge-systems dom...
- [CLI Tools Beat MCP for Token Efficiency](03_validated/cli-tools-beat-mcp-for-token-efficiency.md) — When integrating external tools into LLM-powered workflows, CLI tools paired with skill files consistently outperform...
- [Context Compaction Is a Reset Event](03_validated/context-compaction-is-a-reset-event.md) — When an LLM agent's context is compacted (summarized to reduce token count), all behavioral corrections accumulated d...
- [Context Management Is the Primary LLM Productivity Lever](03_validated/context-management-is-primary-productivity-lever.md) — Across all sources analyzing Claude Code effectiveness — practitioner guides, harness engineering frameworks, accurac...
- [Coverage Blindness — Modeling Only What You Know](03_validated/coverage-blindness-modeling-only-what-you-know.md) — Systems that model their own artifacts tend to cover only the artifacts they already produce — creating a self-reinfo...
- [Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass](03_validated/enforcement-must-be-mindful-hard-blocks-need-justified-bypass.md) — Infrastructure enforcement works — 75% violation rate drops to 0%
- [Follow the Method of Work Not the Methodology Label](03_validated/follow-the-method-of-work-not-the-methodology-label.md) — When told to "follow the methodology," an agent can enter a destructive loop: interpret "methodology" as "do the Docu...
- [Graph-Enhanced Retrieval Bridges Wiki Navigation and Vector Search](03_validated/graph-enhanced-retrieval-bridges-wiki-and-vector-search.md) — The choice between wiki-style navigation and vector RAG is a false binary
- [Hardcoded Instances Fail — Build Frameworks Not Solutions](03_validated/hardcoded-instances-fail-build-frameworks-not-solutions.md) — When building systems meant to be reusable across multiple contexts, hardcoding specific values from one instance (on...
- [Harness Ownership Converges Independently Across Projects](03_validated/harness-ownership-converges-independently-across-projects.md) — Three independent projects — OpenArms (solo agent, TypeScript), OpenFleet (10-agent fleet, Python), and the harness e...
- [Infrastructure Enforcement Proves Instructions Fail](03_validated/infrastructure-enforcement-proves-instructions-fail.md) — Instruction-based agent enforcement (rules in CLAUDE
- [Infrastructure Must Be Reproducible, Not Manual](03_validated/infrastructure-must-be-reproducible-not-manual.md) — The AI agent attempted to create a systemd service file by directly writing it with `cat >` instead of building the s...
- [Lesson — Knowledge Systems Is the Foundational Domain for the Entire Wiki](03_validated/knowledge-systems-is-foundational-domain.md) — The knowledge-systems domain is the only domain in this wiki where the wiki documents how it works
- [LLM-Maintained Wikis Outperform Static Documentation](03_validated/llm-maintained-wikis-outperform-static-documentation.md) — Having an LLM maintain a structured wiki — with validation, relationship discovery, quality gates, and index auto-mai...
- [Methodology Is a Framework, Not a Fixed Pipeline](03_validated/methodology-is-a-framework-not-a-fixed-pipeline.md) — The Methodology model page collapsed the entire methodology framework into a single 5-stage pipeline (Document → Desi...
- [Models Are Built in Layers, Not All at Once](03_validated/models-are-built-in-layers-not-all-at-once.md) — Building the 14 named models for this wiki followed the same SFIF pattern that the wiki documents as universal: scaff...
- [Models Are Systems, Not Documents](03_validated/models-are-systems-not-documents.md) — The first attempt at building wiki models produced 14 "entry points" that were reading lists — pages listing other pa...
- [Multi-Stage Ingestion Beats Single-Pass Processing](03_validated/multi-stage-ingestion-beats-single-pass.md) — Ingestion should be multi-pass — extract, then cross-reference, then identify gaps, then deepen — rather than one-shot
- [Never Present Speculation as Fact](03_validated/never-present-speculation-as-fact.md) — Model pages contained fabricated thresholds presented as deterministic facts — a context degradation table with hard ...
- [Never Skip Stages Even When Told to Continue](03_validated/never-skip-stages-even-when-told-to-continue.md) — When the user said "you have everything to get started," the agent interpreted this as permission to skip the brainst...
- [Never Synthesize from Descriptions Alone](03_validated/never-synthesize-from-descriptions-alone.md) — Reading a README that describes a format is not the same as reading an actual instance of that format
- [New Content Must Integrate Into Existing Pages](03_validated/new-content-must-integrate-into-existing-pages.md) — Creating new wiki pages next to existing ones without weaving the new content INTO the existing high-traffic pages pr...
- [NotebookLM as Grounded Research Engine Not Just Note Storage](03_validated/notebooklm-as-grounded-research-engine.md) — Three independent implementations of NotebookLM integrations (PleasePrompto, claude-world, and the notebooklm-py work...
- [Obsidian as Knowledge Infrastructure Not Just Note-Taking](03_validated/obsidian-as-knowledge-infrastructure.md) — Multiple independent projects converge on Obsidian not as a markdown editor but as programmable knowledge infrastruct...
- [Lesson — Schema Is the Real Product — Not the Content](03_validated/schema-is-the-real-product.md) — Karpathy's primary source document identifies the schema file (CLAUDE
- [Shallow Ingestion Is Systemic, Not Isolated](03_validated/shallow-ingestion-is-systemic-not-isolated.md) — Subagents consistently read only the first ~60 lines of raw files that were 300-1000+ lines long, due to the Read too...
- [Skill Specification Is the Key to Ecosystem Interoperability](03_validated/skill-specification-is-key-to-interoperability.md) — When a skill definition format is rooted in an open specification rather than a proprietary platform, skills become p...
- [Skills Architecture Is the Dominant LLM Extension Pattern](03_validated/skills-architecture-is-dominant-extension-pattern.md) — Skills — bundled markdown packages that combine instructions, context, scripts, and design guidance — have emerged as...
- [Standards Must Preach by Example](03_validated/standards-must-preach-by-example.md) — Every model page and standards page must itself follow the standards it defines
- [Structured Context Is Proto-Programming for AI Agents](03_validated/structured-context-is-proto-programming-for-ai-agents.md) — Markdown is the programming language of AI agents
- [Systemic Incompleteness Is Invisible to Validation](03_validated/systemic-incompleteness-is-invisible-to-validation.md) — 128 pages, 0 validation errors, and the agent claimed "only new sources needed" — while not a single model was complete
- [The Agent Must Practice What It Documents](03_validated/the-agent-must-practice-what-it-documents.md) — The research wiki documented methodology extensively — stage gates, brainstorm-before-spec, research-before-design, m...
- [The Wiki Is a Hub, Not a Silo](03_validated/the-wiki-is-a-hub-not-a-silo.md) — The research wiki is not a standalone documentation project — it is the central intelligence hub that aggregates know...
- [Three Classes of Methodology Output](03_validated/three-classes-of-methodology-output.md) — Methodology execution produces three fundamentally different classes of output — artifacts, documents, and documentat...
- [Universal Stages, Domain-Specific Artifacts](03_validated/universal-stages-domain-specific-artifacts.md) — The methodology's stage sequence (Document → Design → Scaffold → Implement → Test) is universal across all domains
- [The Wiki Maintenance Problem Is Solved by LLM Automation](03_validated/wiki-maintenance-problem-solved-by-llm-automation.md) — Every personal wiki attempt before LLMs failed for the same reason: maintenance burden grew faster than value, and hu...
- [Principle — Infrastructure Over Instructions for Process Enforcement](04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) — For any process rule that can be checked at the tool-call level, infrastructure enforcement (hooks, commands, harness...
- [Principle — Right Process for Right Context — The Goldilocks Imperative](04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md) — Process must adapt to context
- [Principle — Structured Context Governs Agent Behavior More Than Content](04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md) — When instructing AI agents, the SHAPE of information (headers, tables, YAML blocks, callout types, MUST/MUST NOT list...

## Tags

`methodology`, `quality`, `failure-lesson`, `lesson`, `agent-failure`, `lesson-learned`, `second-brain`, `llm-wiki`, `enforcement`, `taxonomy`, `compliance`, `orchestration`, `cross-domain`, `agent-behavior`, `claude-code`, `automation`, `maintenance`, `skills`, `framework`, `compounding-knowledge`

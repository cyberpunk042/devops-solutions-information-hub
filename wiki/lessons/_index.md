# Lessons

Structured failure analysis and convergence insights synthesized from real incidents, post-mortems, and cross-source pattern detection. Every lesson has a trigger, a finding, and an action.

**Model:** [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] | **Standards:** [[model-quality-failure-prevention-standards|Quality Standards — What Good Failure Prevention Looks Like]]

### Start Here

1. [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] — The root failure lesson
2. [[llm-maintained-wikis-outperform-static-documentation|LLM-Maintained Wikis Outperform Static Documentation]] — The root convergence lesson
3. [[agent-orchestration-is-highest-connected-concept|Agent Orchestration Is the Highest-Connected Concept in the Wiki]] — The most connected hub

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
| [[schema-is-the-real-product|Schema Is the Real Product — Not the Content]] | The schema file is the real product; content is generated from it |

### Domain Hubs

Lessons that synthesize an entire domain's structural position.

| Lesson | Domain |
|--------|--------|
| [[agent-orchestration-is-highest-connected-concept|Agent Orchestration Is the Highest-Connected Concept in the Wiki]] | ai-agents |
| [[automation-is-bridge-between-knowledge-and-action|Automation Is the Bridge Between Knowledge and Action]] | automation |
| [[knowledge-systems-is-foundational-domain|Knowledge Systems Is the Foundational Domain for the Entire Wiki]] | knowledge-systems |

## Pages

- [Context Depth Must Vary Per Task Type, Not Per Project — Tier Selection Extends Beyond Identity](01_drafts/contributed/context-depth-must-vary-per-task-type-not-per-project.md) — Context engineering defines three tier budgets (Expert 5-10K / Capable 2-5K / Lightweight 500-1K tokens) with a 10× c...
- [First consumer integration reveals systematic gaps between knowledge and tooling](01_drafts/contributed/first-consumer-integration-reveals-systematic-gaps-between-k.md) — The second brain's model pages contain 800+ lines of deep, evidence-backed knowledge per model
- [Mandatory Without Verification Is Not Enforced — Skill-Layer Instance of Infrastructure > Instructions](01_drafts/contributed/mandatory-without-verification-is-not-enforced.md) — Extension Standards (for Claude Code skills) define a `mandatory` attribute marking skills the agent MUST invoke duri...
- [Per-task cost grows monotonically across multi-task runs (context accumulation)](01_drafts/contributed/per-task-cost-grows-monotonically-across-multi-task-runs-(co.md) — When running multiple tasks in sequence within a single harness invocation (`--tasks N`), each successive task costs ...
- [Schema aspirationalism — defining required sections you never validate produces false confidence](01_drafts/contributed/schema-aspirationalism-—-defining-required-sections-you-neve.md) — A schema that defines `required_sections` per page type without any validator checking section structure creates fals...
- [The harness 'turnCount' variable counts streaming events, not conversational turns](01_drafts/contributed/the-harness-turncount-variable-counts-streaming-events,-not-.md) — In the OpenArms harness (`agent-run-harness
- [The pre-write hook prevents operator-Claude from racing the running agent on backlog files](01_drafts/contributed/the-pre-write-hook-prevents-operator-claude-from-racing-the-.md) — During an active `pnpm openarms agent run`, the methodology enforcement hooks (`pre-bash
- [Execution Mode Is a Consumer Property, Not a Project Property — Guard Against Conflation Drift](01_drafts/execution-mode-is-consumer-property-not-project-property.md) — Execution mode (solo vs harness vs fleet) is a property of the **CONSUMER'S runtime**, not a property of the project
- [Harness Engineering Is the Dominant Performance Lever](01_drafts/harness-engineering-is-the-dominant-performance-lever.md) — For LLM-based agentic systems, **the harness — not the model — is now the dominant performance lever**
- [If You Can Verify, You Converge](01_drafts/if-you-can-verify-you-converge.md) — When a deterministic verification mechanism exists — a compiler, a schema validator, a test runner, a halting conditi...
- [Specs-as-Code-Source Inverts the Traditional Hierarchy](01_drafts/specs-as-code-source-inverts-hierarchy.md) — Traditional software development treats code as the primary artifact and specifications as scaffolding — supporting d...
- [Agents take small unauthorized scope expansions when the change is a 'clean win'](02_synthesized/contributed/agents-take-small-unauthorized-scope-expansions-when-the-cha.md) — The v8 methodology blocks overt scope creep through stage hooks, diff validators, and done-when checks
- [Epic readiness math is wrong when an epic has implicit goals beyond its current children](02_synthesized/contributed/epic-readiness-math-is-wrong-when-an-epic-has-implicit-goals.md) — The harness computes epic readiness as the average of its child task readiness values
- [Right-size the methodology model to the actual work, not the structural category](02_synthesized/contributed/right-size-the-methodology-model-to-the-actual-work,-not-the.md) — The methodology selector picks a model based on `task_type` alone
- [Context Compaction Is a Reset Event](03_validated/context-engineering/context-compaction-is-a-reset-event.md) — When an LLM agent's context is compacted (summarized to reduce token count), all behavioral corrections accumulated d...
- [Context Management Is the Primary LLM Productivity Lever](03_validated/context-engineering/context-management-is-primary-productivity-lever.md) — Across all sources analyzing Claude Code effectiveness — practitioner guides, harness engineering frameworks, accurac...
- [Structured Context Is Proto-Programming for AI Agents](03_validated/context-engineering/structured-context-is-proto-programming-for-ai-agents.md) — Markdown is the programming language of AI agents
- [Agent Failure Taxonomy — Seven Classes of Behavioral Failure](03_validated/enforcement-compliance/agent-failure-taxonomy-seven-classes-of-behavioral-failure.md) — After infrastructure enforcement solves stage boundary violations (75% → 0%), six classes of BEHAVIORAL failure remain
- [Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass](03_validated/enforcement-compliance/enforcement-must-be-mindful-hard-blocks-need-justified-bypass.md) — Infrastructure enforcement works — 75% violation rate drops to 0%
- [Harness Ownership Converges Independently Across Projects](03_validated/enforcement-compliance/harness-ownership-converges-independently-across-projects.md) — Three independent projects — OpenArms (solo agent, TypeScript), OpenFleet (10-agent fleet, Python), and the harness e...
- [Infrastructure Enforcement Proves Instructions Fail](03_validated/enforcement-compliance/infrastructure-enforcement-proves-instructions-fail.md) — Instruction-based agent enforcement (rules in CLAUDE
- [Multi-Stage Ingestion Beats Single-Pass Processing](03_validated/ingestion-research/multi-stage-ingestion-beats-single-pass.md) — Ingestion should be multi-pass — extract, then cross-reference, then identify gaps, then deepen — rather than one-shot
- [Never Synthesize from Descriptions Alone](03_validated/ingestion-research/never-synthesize-from-descriptions-alone.md) — Reading a README that describes a format is not the same as reading an actual instance of that format
- [NotebookLM as Grounded Research Engine Not Just Note Storage](03_validated/ingestion-research/notebooklm-as-grounded-research-engine.md) — Three independent implementations of NotebookLM integrations (PleasePrompto, claude-world, and the notebooklm-py work...
- [Shallow Ingestion Is Systemic, Not Isolated](03_validated/ingestion-research/shallow-ingestion-is-systemic-not-isolated.md) — Subagents consistently read only the first ~60 lines of raw files that were 300-1000+ lines long, due to the Read too...
- [Lesson — Agent Orchestration Is the Highest-Connected Concept in the Wiki](03_validated/knowledge-systems/agent-orchestration-is-highest-connected-concept.md) — Agent Orchestration Patterns is the most inbound-linked concept in the ai-agents domain
- [Automated Knowledge Validation Prevents Silent Wiki Decay](03_validated/knowledge-systems/automated-knowledge-validation-prevents-wiki-decay.md) — Wikis without automated validation decay silently: pages go stale, relationships break, orphaned concepts accumulate,...
- [Graph-Enhanced Retrieval Bridges Wiki Navigation and Vector Search](03_validated/knowledge-systems/graph-enhanced-retrieval-bridges-wiki-and-vector-search.md) — The choice between wiki-style navigation and vector RAG is a false binary
- [Lesson — Knowledge Systems Is the Foundational Domain for the Entire Wiki](03_validated/knowledge-systems/knowledge-systems-is-foundational-domain.md) — The knowledge-systems domain is the only domain in this wiki where the wiki documents how it works
- [LLM-Maintained Wikis Outperform Static Documentation](03_validated/knowledge-systems/llm-maintained-wikis-outperform-static-documentation.md) — Having an LLM maintain a structured wiki — with validation, relationship discovery, quality gates, and index auto-mai...
- [New Content Must Integrate Into Existing Pages](03_validated/knowledge-systems/new-content-must-integrate-into-existing-pages.md) — Creating new wiki pages next to existing ones without weaving the new content INTO the existing high-traffic pages pr...
- [Obsidian as Knowledge Infrastructure Not Just Note-Taking](03_validated/knowledge-systems/obsidian-as-knowledge-infrastructure.md) — Multiple independent projects converge on Obsidian not as a markdown editor but as programmable knowledge infrastruct...
- [Lesson — Schema Is the Real Product — Not the Content](03_validated/knowledge-systems/schema-is-the-real-product.md) — Karpathy's primary source document identifies the schema file (CLAUDE
- [The Wiki Is a Hub, Not a Silo](03_validated/knowledge-systems/the-wiki-is-a-hub-not-a-silo.md) — The research wiki is not a standalone documentation project — it is the central intelligence hub that aggregates know...
- [The Wiki Maintenance Problem Is Solved by LLM Automation](03_validated/knowledge-systems/wiki-maintenance-problem-solved-by-llm-automation.md) — Every personal wiki attempt before LLMs failed for the same reason: maintenance burden grew faster than value, and hu...
- [Coverage Blindness — Modeling Only What You Know](03_validated/methodology-process/coverage-blindness-modeling-only-what-you-know.md) — Systems that model their own artifacts tend to cover only the artifacts they already produce — creating a self-reinfo...
- [Follow the Method of Work Not the Methodology Label](03_validated/methodology-process/follow-the-method-of-work-not-the-methodology-label.md) — When told to "follow the methodology," an agent can enter a destructive loop: interpret "methodology" as "do the Docu...
- [Methodology Is a Framework, Not a Fixed Pipeline](03_validated/methodology-process/methodology-is-a-framework-not-a-fixed-pipeline.md) — The Methodology model page collapsed the entire methodology framework into a single 5-stage pipeline (Document → Desi...
- [Never Skip Stages Even When Told to Continue](03_validated/methodology-process/never-skip-stages-even-when-told-to-continue.md) — When the user said "you have everything to get started," the agent interpreted this as permission to skip the brainst...
- [The Agent Must Practice What It Documents](03_validated/methodology-process/the-agent-must-practice-what-it-documents.md) — The research wiki documented methodology extensively — stage gates, brainstorm-before-spec, research-before-design, m...
- [Three Classes of Methodology Output](03_validated/methodology-process/three-classes-of-methodology-output.md) — Methodology execution produces three fundamentally different classes of output — artifacts, documents, and documentat...
- [Universal Stages, Domain-Specific Artifacts](03_validated/methodology-process/universal-stages-domain-specific-artifacts.md) — The methodology's stage sequence (Document → Design → Scaffold → Implement → Test) is universal across all domains
- [Hardcoded Instances Fail — Build Frameworks Not Solutions](03_validated/methodology-quality/hardcoded-instances-fail-build-frameworks-not-solutions.md) — When building systems meant to be reusable across multiple contexts, hardcoding specific values from one instance (on...
- [Infrastructure Must Be Reproducible, Not Manual](03_validated/methodology-quality/infrastructure-must-be-reproducible-not-manual.md) — The AI agent attempted to create a systemd service file by directly writing it with `cat >` instead of building the s...
- [Models Are Built in Layers, Not All at Once](03_validated/methodology-quality/models-are-built-in-layers-not-all-at-once.md) — Building the 14 named models for this wiki followed the same SFIF pattern that the wiki documents as universal: scaff...
- [Models Are Systems, Not Documents](03_validated/methodology-quality/models-are-systems-not-documents.md) — The first attempt at building wiki models produced 14 "entry points" that were reading lists — pages listing other pa...
- [Never Present Speculation as Fact](03_validated/methodology-quality/never-present-speculation-as-fact.md) — Model pages contained fabricated thresholds presented as deterministic facts — a context degradation table with hard ...
- [Standards Must Preach by Example](03_validated/methodology-quality/standards-must-preach-by-example.md) — Every model page and standards page must itself follow the standards it defines
- [Systemic Incompleteness Is Invisible to Validation](03_validated/methodology-quality/systemic-incompleteness-is-invisible-to-validation.md) — 128 pages, 0 validation errors, and the agent claimed "only new sources needed" — while not a single model was complete
- [Always Plan Before Executing](03_validated/tools-architecture/always-plan-before-executing.md) — LLM agents produce dramatically better results when they produce an explicit plan before taking action — not as a sof...
- [Lesson — Automation Is the Bridge Between Knowledge and Action](03_validated/tools-architecture/automation-is-bridge-between-knowledge-and-action.md) — The automation domain occupies a distinct structural position in this wiki: it bridges what the knowledge-systems dom...
- [CLI Tools Beat MCP for Token Efficiency](03_validated/tools-architecture/cli-tools-beat-mcp-for-token-efficiency.md) — When integrating external tools into LLM-powered workflows, CLI tools paired with skill files consistently outperform...
- [Skill Specification Is the Key to Ecosystem Interoperability](03_validated/tools-architecture/skill-specification-is-key-to-interoperability.md) — When a skill definition format is rooted in an open specification rather than a proprietary platform, skills become p...
- [Skills Architecture Is the Dominant LLM Extension Pattern](03_validated/tools-architecture/skills-architecture-is-dominant-extension-pattern.md) — Skills — bundled markdown packages that combine instructions, context, scripts, and design guidance — have emerged as...
- [Principle — Infrastructure Over Instructions for Process Enforcement](04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) — For any process rule that can be checked at the tool-call level, infrastructure enforcement (hooks, commands, harness...
- [Principle — Right Process for Right Context — The Goldilocks Imperative](04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md) — Process must adapt to context
- [Principle — Structured Context Governs Agent Behavior More Than Content](04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md) — When instructing AI agents, the SHAPE of information (headers, tables, YAML blocks, callout types, MUST/MUST NOT list...

## Tags

`methodology`, `lesson`, `quality`, `contributed`, `failure-lesson`, `inbox`, `enforcement`, `cross-domain`, `agent-failure`, `lesson-learned`, `second-brain`, `llm-wiki`, `openarms`, `skills`, `infrastructure`, `validation`, `harness-engineering`, `convergence`, `artifacts`, `agent-behavior`

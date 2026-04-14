---
title: "Synthesis — Pydantic AI: Typed Agent Framework"
type: source-synthesis
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: pydantic-ai-overview-docs
    type: documentation
    url: "https://pydantic.dev/docs/ai/overview/"
tags:
  - ai-agents
  - pydantic
  - type-safety
  - structured-outputs
  - dependency-injection
  - tool-decoration
  - model-agnostic
  - python
  - agent-framework
  - production-grade
---

# Synthesis — Pydantic AI: Typed Agent Framework

## Summary

Pydantic AI is a Python agent framework for building production-grade generative AI applications. Built by the Pydantic team — the creators of the widely-adopted Pydantic validation library — it brings type-safe, FastAPI-style development patterns to agent engineering. Its central design decisions — dependency injection through typed `RunContext`, structured outputs via Pydantic model schemas, automatic tool schema generation from Python docstrings, and support for 20+ model providers — make it the most ergonomic typed agent framework available in Python. For this wiki's methodology, Pydantic AI is a concrete reference implementation of the principle that typed schemas constrain and guide LLM behavior just as specs constrain agent behavior in spec-driven development.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source    | Pydantic AI Official Documentation (`https://pydantic.dev/docs/ai/overview/`) |
> | Type      | Official documentation — framework overview |
> | Author    | Pydantic team (creators of Pydantic validation library) |
> | Date      | Ingested 2026-04-14 |
> | Key claim | Type-safe agent engineering is achievable with the same ergonomics that made Pydantic/FastAPI the standard for Python API development |

## Key Insights

**1. `Agent[DependencyType, OutputType]` — types are first-class architecture.**

The core Agent class uses Python generics: `Agent[SupportDependencies, SupportOutput]`. This is not merely a documentation convention — it means IDEs and type checkers can verify that the dependency object passed at runtime actually provides the fields the agent logic expects, and that the agent's output is actually a `SupportOutput` instance. This is a significant advance over string-in/string-out LLM calls: the entire pipeline becomes statically checkable. In our ecosystem context, this mirrors the principle that structured contracts — specs, typed schemas, Pydantic models — are mechanisms for constraining and verifying LLM behavior, not just documentation.

**2. Dependency injection via `RunContext` — clean separation of agent logic from external state.**

Instead of passing database connections, API clients, or session state through the prompt or as global variables, Pydantic AI uses a `RunContext[DependenciesType]` parameter pattern. An agent function that needs a customer's account balance declares `ctx: RunContext[SupportDependencies]` and calls `ctx.deps.db.get_balance(customer_id)`. The dependency object flows from the harness into the agent cleanly, testably, and without polluting the prompt. This is the same pattern dependency injection frameworks use in web applications — and for the same reasons: testability, decoupling, and separation of concerns between the "what to do" (agent logic) and "where to get data" (dependencies).

**3. `@agent.tool` decorator — Python functions become LLM-callable tools with zero schema boilerplate.**

Any Python function decorated with `@agent.tool` is automatically exposed as a callable LLM tool. Pydantic AI extracts the tool's input schema from the function's type annotations and generates the description from the docstring. The LLM sees a validated, schema-bound tool; the developer writes a normal Python function. This is the ergonomic win: no manually-maintained JSON Schema, no risk of description drift from implementation. The same principle underlies our methodology's directive to generate tool schemas from code rather than maintain them manually.

**4. Both static and dynamic instructions — agent behavior adapts to runtime context.**

Instructions can be provided two ways: statically at construction time (a fixed system prompt), or dynamically via the `@agent.instructions` decorator, which can read the `RunContext` to construct context-aware instructions at call time. This means an agent's behavioral contract can vary based on the caller's role, the customer's subscription level, or any other runtime signal — without requiring multiple agent definitions. For harness engineers, this is the bridge between configuration-time and runtime agent customization.

**5. Capabilities bundle tools + hooks + instructions + settings into reusable units.**

The Capabilities system allows combining multiple `@agent.tool` functions, instruction sets, and settings into composable units that can be mixed into different agents. This is a reuse mechanism for agent behavior — a "billing capability" can bundle the `get_balance` tool, the `process_payment` tool, and billing-specific instructions, then be attached to any agent that needs billing functionality. This compositional approach prevents the common anti-pattern of monolithic agent definitions that grow without bound.

**6. 20+ model providers behind a single API — model switching is configuration, not refactoring.**

Pydantic AI abstracts over OpenAI, Anthropic, Google, AWS Bedrock, xAI, Cerebras, Cohere, Groq, Hugging Face, Mistral, OpenRouter, Outlines, and custom implementations. Switching the underlying model requires changing one parameter, not rewriting tool schemas or output parsing. For our AICP / local AI strategy, this matters: agents built on Pydantic AI can route to a local Qwen or Mistral model (via Outlines or OpenRouter) with no application logic changes — exactly the zero-coupling model switching that enables the $0 target architecture.

**7. Pydantic Logfire integration — observability is a first-class framework concern.**

Pydantic AI ships with native integration to Pydantic Logfire for real-time debugging, eval-based performance monitoring, behavior tracing, and cost tracking. Observability is not an afterthought wired in by the harness engineer — it's part of the framework's design surface. This reflects a maturing understanding in the agent ecosystem: you cannot operate production agents without cost visibility and behavior tracing.

**8. The "FastAPI feeling" as design philosophy — ergonomics are a strategic choice, not a bonus.**

The explicit design goal is to replicate "the FastAPI feeling" for GenAI development. This means: zero-ceremony setup, type annotations drive schema generation, decorators replace boilerplate, and the happy path is also the correct path. FastAPI became the dominant Python API framework because it made doing the right thing (schema-first, type-safe APIs) easier than the wrong thing (untyped dict-slinging). Pydantic AI is attempting the same transformation for agent development: typed, validated, observable agents as the path of least resistance.

## Deep Analysis

### The Type-Safe Agent Pattern in Full

The canonical Pydantic AI pattern, as demonstrated in the Bank Support Agent example, composes five elements:

| Element | Role | Example |
|---------|------|---------|
| `@dataclass SupportDependencies` | Injectable runtime state | `db: DatabaseConn, http: HttpClient` |
| `class SupportOutput(BaseModel)` | Validated output schema | `response: str, needs_escalation: bool, risk_level: int` |
| `Agent[SupportDependencies, SupportOutput]` | Typed agent instance | Combines dependency + output constraints |
| `@agent.tool` functions | LLM-callable operations | `async def get_balance(ctx, customer_id: int) -> Decimal` |
| `@agent.instructions` decorator | Dynamic system prompt | Reads `ctx.deps` to personalize instructions at call time |

The output type `SupportOutput(BaseModel)` deserves special attention. Pydantic AI uses this model to construct a JSON Schema that is passed as the structured output constraint to the underlying LLM. The LLM must produce output that validates against this schema — if it fails, the framework retries automatically. This is the type-safety mechanism operating at the LLM boundary: not a post-hoc validator, but a generative constraint. The output Pydantic model is a behavioral contract written as Python code.

### Comparison to Other Agent Frameworks

| Dimension | Pydantic AI | LangChain | OpenAI Agents SDK |
|-----------|-------------|-----------|-------------------|
| **Type safety** | First-class generics | Minimal | Moderate |
| **Output validation** | Pydantic schema (native) | Custom validators | JSON mode + manual parse |
| **Dependency injection** | `RunContext` pattern | Manual | Not built-in |
| **Tool schema generation** | From type annotations + docstrings | Manual or from function | From type annotations |
| **Model providers** | 20+ | 50+ | OpenAI-first |
| **Observability** | Logfire (native) | LangSmith (external) | OpenAI Dashboard |
| **Ergonomic philosophy** | FastAPI-style simplicity | Modular but complex | Minimal surface |

The differentiating dimension is the FastAPI-style ergonomic philosophy. LangChain provides the most model providers and integrations but requires significant orchestration code. OpenAI's Agents SDK is clean but remains OpenAI-first. Pydantic AI occupies the high-ergonomics, type-safe, provider-agnostic quadrant.

### Structured Output as Behavioral Constraint

The connection between Pydantic models and LLM behavioral constraint is worth making explicit:

1. Developer defines `class SupportOutput(BaseModel)` with typed fields and field descriptions
2. Pydantic AI generates a JSON Schema from the model
3. That schema is passed to the LLM as a structured output requirement
4. The LLM is forced to produce output that conforms to the schema
5. The framework validates the output; mismatches trigger automatic retries

This is the same principle that AutoBE applies with AST-based compilers: you constrain the LLM's output space to a validated structure, then use a verifier to catch deviations, then retry until convergence. In Pydantic AI the constraint is a Pydantic model; in AutoBE the constraint is an AST compiler. In both cases: **structured verification + automatic retry = reliable output regardless of model variation**.

This principle connects to our wiki's `model-quality-failure-prevention` model: quality comes not from choosing the perfect model, but from wrapping any model in sufficient structured verification to catch and correct failures.

### Dependency Injection — Testability as a Design Forcing Function

The `RunContext` pattern deserves examination as a harness engineering pattern. In a naively-implemented agent, the database connection or HTTP client would be either:

- Hardcoded in the tool function (untestable, environment-coupled)
- Passed through the prompt as a serialized state blob (fragile, expensive)
- Stored in a global variable (hidden coupling)

`RunContext` makes dependencies an explicit, typed parameter. Test code can pass a mock `SupportDependencies` with a fake `DatabaseConn` that returns predictable values. Production code passes the real connection. The agent logic is identical; only the injected state differs. This is the core benefit of dependency injection as a design pattern, and it is as valuable in agent code as it is in web application code.

For harness engineers in our ecosystem: the `RunContext` pattern is the way to build agents that are:
- **Testable**: swap real dependencies for mocks in tests
- **Multi-tenant**: inject different resource limits or permissions per caller
- **Auditable**: inject a logging wrapper that records every dependency call

### Model Provider Abstraction and the AICP Cost Target

Pydantic AI's 20+ provider abstraction creates a direct path to implementing the AICP / local AI cost target:

1. Build agent with standard `@agent.tool` pattern targeting Anthropic or OpenAI
2. Validate correct behavior at high-quality model
3. Switch provider to Outlines (local) or OpenRouter (routing to cheaper model)
4. Validate same behavior — if structured outputs pass Pydantic validation, correctness is confirmed
5. Accept higher retry counts in exchange for radically lower cost

This is the two-phase strategy: quality gates are determined by schema validation, not by which model runs. The local model may take 3-4 attempts where Claude takes 1, but the final output is schema-identical. Pydantic AI's provider abstraction makes this switching zero-code; the structured output validation makes it safe.

### The Async/Await Pattern — Production Non-Negotiables

Pydantic AI is async-native. All `@agent.tool` functions use `async def` and `await` internally. This is not a cosmetic choice — production agent systems require:

- Non-blocking execution while LLM API calls complete (high latency operations)
- Concurrent tool calls when multiple tools can execute in parallel
- Proper handling of LLM streaming without blocking the event loop

Pydantic AI's async-first design means it integrates cleanly with FastAPI, Starlette, and other async Python frameworks. For our ecosystem building on top of an async agent infrastructure, this is a prerequisite, not a nice-to-have.

## Open Questions

- Does Pydantic AI support structured output streaming — producing partial typed objects as the LLM generates tokens, rather than waiting for the full response?
- What is the retry strategy for structured output validation failures? Is it configurable (max retries, backoff), or fixed behavior?
- How does the `Capabilities` composition system handle conflicts — two capabilities that both define a tool with the same name, or instructions that contradict each other?
- What is the performance overhead of JSON Schema validation on every LLM output compared to raw string parsing? At high throughput, does this become a bottleneck?
- Is there a mechanism for output schema versioning — handling the case where the Pydantic model evolves but existing stored outputs were validated against an older schema?
- How does Pydantic AI handle the case where a tool call fails during agent execution — does it surface the error to the LLM for self-correction, or terminate the run?

## Relationships

- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]] (provider abstraction enables routing structured agent tasks to local models; schema validation confirms correctness independently of model choice)
- RELATES TO: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] (structured output validation + automatic retry is the same "verify and converge" pattern)
- RELATES TO: [[model-claude-code|Model — Claude Code]] (Pydantic AI complements Claude Code for programmatic agent invocation with typed contracts)
- RELATES TO: [[harness-engineering|Harness Engineering]] (dependency injection, structured outputs, and tool decoration are harness engineering primitives)
- COMPARES TO: [[src-claude-agent-sdk-and-managed-agents|Synthesis — Claude Agent SDK and Managed Agents]] (two approaches to typed agent construction: SDK-level harness vs. framework-level abstraction)
- FEEDS INTO: [[spec-driven-development|Spec-Driven Development]] (Pydantic output models are the code-level equivalent of behavioral specs — both constrain what an AI can produce)
- RELATES TO: [[agent-orchestration-patterns|Agent Orchestration Patterns]] (Capabilities and sub-agent composition patterns)
- BUILDS ON: [[model-ecosystem|Model — Ecosystem Architecture]] (provider abstraction supports multi-model ecosystem routing strategy)

## Backlinks

[[model-local-ai|Model — Local AI ($0 Target)]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[model-claude-code|Model — Claude Code]]
[[harness-engineering|Harness Engineering]]
[[src-claude-agent-sdk-and-managed-agents|Synthesis — Claude Agent SDK and Managed Agents]]
[[spec-driven-development|Spec-Driven Development]]
[[agent-orchestration-patterns|Agent Orchestration Patterns]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[src-autobe-compiler-verified-backend-generation|Synthesis — AutoBE: Compiler-Verified Backend Generation]]

# Pydantic AI — Overview

Source: https://pydantic.dev/docs/ai/overview/
Ingested: 2026-04-14
Type: documentation

---

## What is Pydantic AI

Python agent framework for building production-grade applications with generative AI. Built by the Pydantic team behind Pydantic Validation. Aims to bring "that FastAPI feeling to GenAI app and agent development."

## Core Architecture

**Agent Framework**: Agents are the primary construct, accepting dependency types and output types as generics. Uses `Agent[DependencyType, OutputType]` patterns for type safety.

**Dependency Injection System**: Dependencies flow through `RunContext` parameters, enabling clean separation between agent logic, external data sources, and LLM interactions.

**Type-Safe Design**: "Designed to give your IDE or AI coding agent as much context as possible for auto-completion and type checking."

## Key Features

1. **Model Agnostic**: Supports 20+ providers including OpenAI, Anthropic, Google, Bedrock, xAI, Cerebras, Cohere, Groq, Hugging Face, Mistral, OpenRouter, Outlines
2. **Structured Outputs**: Leverages Pydantic models for validated output schemas
3. **Tool System**: Functions decorated with `@agent.tool` become LLM-callable tools with automatic schema generation from docstrings
4. **Instructions**: Both static (constructor) and dynamic (decorator-based) instruction injection
5. **Capabilities**: Composable units bundling tools, hooks, instructions, and settings

## Example: Bank Support Agent

Complete example featuring:
- `SupportDependencies` dataclass for injected resources
- `SupportOutput` Pydantic model defining structured responses
- `@agent.tool` decorated async functions for balance retrieval
- Dynamic instructions via `@agent.instructions` decorator
- Async/await pattern for non-blocking operations

## Type Safety Features

- Static type checking via IDE integration
- Pydantic validation for tool arguments and outputs
- Generics for dependency and output types
- Parameter descriptions extracted from docstrings

## Observability

Integrates with Pydantic Logfire for:
- Real-time debugging
- Evals-based performance monitoring
- Behavior tracing
- Cost tracking

## Supported Models & Providers

OpenAI, Anthropic, Google, xAI, Bedrock, Cerebras, Cohere, Groq, Hugging Face, Mistral, OpenRouter, Outlines, and custom implementations.

---
title: "Artifact Chain: TypeScript/Node Domain"
type: reference
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: openarms-chain
    type: file
    file: /home/jfortin/openarms/wiki/domains/architecture/methodology-document-chain.md
  - id: openarms-methodology
    type: file
    file: /home/jfortin/openarms/wiki/config/methodology.yaml
  - id: taxonomy
    type: wiki
    file: wiki/domains/cross-domain/methodology-artifact-taxonomy.md
tags: [methodology, artifact-chain, typescript, node, domain-specific, openarms, openfleet]
---

# Artifact Chain: TypeScript/Node Domain

## Summary

Complete artifact chain resolution for TypeScript/Node.js projects (OpenArms, OpenFleet). Maps every methodology model's stages to concrete TypeScript artifacts — file paths, export patterns, gate commands, and real examples from the OpenArms codebase. This is the most evolved domain chain in the ecosystem, validated through 93 completed tasks and 9 methodology versions. The document/design stages use universal artifacts (same as all domains). The scaffold/implement/test stages use TypeScript-specific artifacts.

## Reference Content

### Toolchain

> [!info] TypeScript Domain Stack
>
> | Tool | Purpose | Gate Command |
> |------|---------|-------------|
> | pnpm | Package management | `pnpm install` |
> | TypeScript (tsgo) | Type checking | `pnpm tsgo` |
> | oxlint/oxfmt | Linting + formatting | `pnpm check` |
> | vitest | Testing | `pnpm test -- path/to/test.ts` |
> | Zod | Runtime validation schemas | Part of tsgo check |
> | ESM | Module system | Native ES modules |

### Feature Development — Full 24-Artifact Chain

> [!abstract] The Complete Chain (from OpenArms methodology-document-chain.md)
>
> | # | Stage | Artifact | File Pattern | Gate |
> |---|-------|----------|-------------|------|
> | 1 | document | Requirements Spec | `wiki/domains/{domain}/{slug}-requirements.md` | FR items have Input/Output/Constraint |
> | 2 | document | Infrastructure Analysis | `wiki/domains/{domain}/{slug}-infrastructure.md` | Every file verified to exist |
> | 3 | document | Gap Analysis | `wiki/domains/{domain}/{slug}-gaps.md` | Gaps reference existing files |
> | 4 | design | ADR | `wiki/domains/architecture/{slug}-adr.md` | ≥1 alternative with rejection reason |
> | 5 | design | Tech Spec | `wiki/domains/architecture/{slug}-tech-spec.md` | Every function has API entry |
> | 6 | design | Interface Spec | `wiki/domains/architecture/{slug}-interface-spec.md` | All types COMPLETE, ready to copy to src/ |
> | 7 | design | Config Spec | `wiki/domains/architecture/{slug}-config-spec.md` | Concrete YAML, every env var has default |
> | 8 | design | Test Plan | `wiki/domains/architecture/{slug}-test-plan.md` | ≥5 unit, ≥2 integration, ≥1 e2e tests defined |
> | 9 | scaffold | Type Definitions | `src/{module}/{slug}.ts` | `pnpm tsgo` passes, no control flow in bodies |
> | 10 | scaffold | Zod Schemas | `src/{module}/{slug}.schema.ts` | Schemas match types, no `.transform()` logic |
> | 11 | scaffold | Test Stubs | `src/{module}/{slug}.test.ts` | ≥3 `it()` blocks, 0 real assertions |
> | 12 | scaffold | Config Wiring | existing config types modified | `import type` only, field optional |
> | 13 | scaffold | Env Example | `.env.example` | Entries match Config Spec |
> | 14 | implement | Implementation | `src/{module}/{slug}.ts` | `pnpm tsgo` + `pnpm check`, functions match Tech Spec |
> | 15 | implement | Env Reader | `src/{module}/{slug}-env.ts` | Reads env vars from Config Spec |
> | 16 | implement | Bridge Module | `src/{location}/{slug}-bridge.ts` | <80 LOC, adapter only |
> | 17 | implement | Integration Wiring | existing runtime file modified | Diff shows added import + call |
> | 18 | test | Test Implementation | `src/{module}/{slug}.test.ts` | 0 placeholders, ≥3 real assertions |
> | 19 | test | Test Results | gate output | `pnpm test -- path/to/test.ts` shows 0 failures |
> | 20 | harness | Task Frontmatter | task .md file | stages_completed updated |
> | 21 | harness | Git Commits | git log | One per stage, conventional format |
> | 22 | harness | Epic Readiness | epic .md file | Recalculated from children |
> | 23 | harness | Completion Log | `wiki/log/{date}-{task-id}-completion.md` | Stages, artifacts, concerns recorded |
> | 24 | harness | Compliance Check | validate-stage.cjs output | All gates passed |

### Scaffold Stage — TypeScript Specifics

> [!warning] What's ALLOWED vs FORBIDDEN
>
> **ALLOWED:**
> ```typescript
> // Type definitions
> export type StageValidationResult = {
>   passed: boolean;
>   stage: string;
>   errors: StageValidationError[];
> };
>
> // Static data constants
> export const SCOPE_MAP: Record<string, ScopeConfig> = {
>   docker: { allowPublic: false, allowPrivate: true },
>   host: { allowPublic: true, allowPrivate: true },
> };
>
> // Zod schemas
> export const NetworkRulesSchema = z.object({
>   scope: z.enum(["docker", "host", "custom"]),
>   rules: z.array(NetworkRuleSchema),
> });
>
> // Stub functions
> export function resolveScope(scope: string): ScopeConfig {
>   throw new Error("not implemented");
> }
>
> // Empty test
> it("should resolve docker scope", () => {
>   expect(true).toBe(true);
> });
> ```
>
> **FORBIDDEN:**
> ```typescript
> // Business logic (control flow)
> export function resolveScope(scope: string): ScopeConfig {
>   if (scope === "docker") return { allowPublic: false };  // ← FORBIDDEN
>   return SCOPE_MAP[scope] ?? defaultConfig;                // ← FORBIDDEN
> }
>
> // Env reader with parsing
> export function readNetworkEnv(): NetworkConfig {
>   const raw = process.env.NETWORK_RULES;                   // ← FORBIDDEN
>   return raw ? JSON.parse(raw) : defaults;                 // ← FORBIDDEN
> }
>
> // Real test assertion
> it("should resolve docker scope", () => {
>   expect(resolveScope("docker").allowPublic).toBe(false); // ← FORBIDDEN
> });
> ```

### Implement Stage — TypeScript Specifics

> [!tip] The Integration Wiring Requirement
>
> Every implement stage MUST modify at least one EXISTING runtime file to import and call the new code. This is verified by checking `git diff` against `.openarms/existing-files.json`.
>
> **Good integration:**
> ```typescript
> // In src/commands/agent-run.ts (EXISTING file):
> import { evaluateHostAccess } from "../infra/net/network-rules-bridge.js";
> // ... later in the function:
> const access = evaluateHostAccess(hostname, config.networkRules);
> ```
>
> **Bad (orphaned code):**
> ```typescript
> // New file exists: src/config/network-rules-resolver.ts
> // New file exists: src/config/network-rules-resolver.test.ts
> // But NOTHING in the runtime imports it
> // This is OpenArms Bug 6 — 2,073 lines nobody imported
> ```

### Other Models — TypeScript Chain Subsets

> [!abstract] Each model uses a SUBSET of the full chain
>
> | Model | Artifacts Used (by #) | What's Different |
> |-------|----------------------|-----------------|
> | **Research** | #1-3 (requirements) + #4-5 (ADR + findings) | No code artifacts. Findings doc instead of full tech spec. |
> | **Bug Fix** | #1 (as bug analysis) + #14, #17 (fix + wiring) + #18-19 (regression test) | No design docs. No scaffold. Fix in existing files. |
> | **Integration** | #9-11 (bridge types + stubs) + #14, #16-17 (bridge + wiring) + #18-19 (tests) | No document/design — uses epic's design docs. Bridge pattern required. |
> | **Hotfix** | #14, #17 (direct fix) + #18-19 (regression test) | Minimal. Problem and solution already known. |
> | **Refactor** | #1 (as refactor plan) + #9 (new types) + #14, #17 (restructure) + #18-19 (behavior unchanged) | No design. Document maps current→target structure. |
> | **Documentation** | Wiki page only | No code artifacts at all. |
> | **Knowledge Evolution** | Wiki page only | Source inventory + distilled page. No code. |

### Real Examples from OpenArms

> [!example]- T039: Network Rules Evaluation (Integration, 3 stages)
>
> **Scaffold:**
> - `src/config/types.network-rules.ts` — NetworkScope, NetworkRule, SsrfPolicy types
> - `src/config/types.network-rules.test.ts` — 5 it() blocks with placeholders
>
> **Implement:**
> - `src/config/network-rules-resolver.ts` — evaluateHostAccess(), matchHostname() logic
> - `src/infra/net/network-rules-bridge.ts` — thin adapter (<80 LOC)
> - `src/infra/net/fetch-guard.ts` — EXISTING file, added import + call
>
> **Test:**
> - `src/config/types.network-rules.test.ts` — real assertions for scope resolution, hostname matching
> - Gate: `pnpm test -- src/config/types.network-rules.test.ts` → 0 failures

> [!example]- T008: Methodology Zod Schema (Task, 3 stages)
>
> **Scaffold:**
> - `src/config/zod-schema.methodology.ts` — MethodologySchema, StageSchema, ModeSchema Zod objects
>
> **Implement:**
> - `src/config/zod-schema.methodology.ts` — filled with real validation logic
> - Config loader modified to use the schema
>
> **Test:**
> - Schema validation tests with valid and invalid configs
> - Gate: 0 failures

## Relationships

- BUILDS ON: [[Methodology Artifact Taxonomy]]
- BUILDS ON: [[Construction and Testing Artifacts — Standards and Guide]]
- BUILDS ON: [[Requirements and Design Artifacts — Standards and Guide]]
- RELATES TO: [[Artifact Chains by Methodology Model]]
- RELATES TO: [[Model: Methodology]]
- FEEDS INTO: [[Methodology Adoption Guide]]

## Backlinks

[[Methodology Artifact Taxonomy]]
[[Construction and Testing Artifacts — Standards and Guide]]
[[Requirements and Design Artifacts — Standards and Guide]]
[[Artifact Chains by Methodology Model]]
[[Model: Methodology]]
[[Methodology Adoption Guide]]
[[Artifact Chain: Infrastructure/IaC Domain]]
[[Artifact Chain: Knowledge/Evolution Domain]]
[[Artifact Chain: Python/Wiki Domain]]

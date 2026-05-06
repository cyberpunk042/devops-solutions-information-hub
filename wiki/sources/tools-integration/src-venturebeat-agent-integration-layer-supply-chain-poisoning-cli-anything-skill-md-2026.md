---
title: "Synthesis — VentureBeat: Agent Integration Layer Is the Supply-Chain Attack Surface No Scanner Sees (CLI-Anything · SKILL.md Poisoning · ClawHavoc 1,184 Compromised · Cisco/Snyk First Tools April 2026)"
aliases:
  - "Agent Integration Layer Attack Surface"
  - "VentureBeat Supply-Chain Poisoning Synthesis"
  - "SKILL.md Poisoning"
  - "ClawHavoc Synthesis"
  - "Three-Layer Agent Supply-Chain Audit"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-06
updated: 2026-05-06
last_reviewed: 2026-05-06
sources:
  - id: venturebeat-article
    type: article
    url: https://venturebeat.com/security/one-command-open-source-repo-ai-agent-backdoor-openclaw-supply-chain-scanner
    file: raw/articles/venturebeat-cli-anything-agent-integration-layer-supply-chain-attack.md
    description: "Louis Columbus, VentureBeat 2026-05-05 — CLI-Anything (UHK Data Intelligence Lab) generates SKILL.md files; same artifact class Snyk's ToxicSkills found 76 malicious payloads in (Feb 2026); Antiy CERT confirmed 1,184 compromised packages on ClawHub via the ClawHavoc campaign; Cisco + Snyk shipped first agent-integration-layer scanners April 2026"
  - id: ddipe-paper
    type: documentation
    url: https://arxiv.org/
    description: "Griffith U + NTU + UNSW + U-Tokyo April 2026 paper — 'Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems' — introduces Document-Driven Implicit Payload Execution (DDIPE) with 11.6%-33.5% bypass rates across 4 frameworks × 5 LLMs; 2.5% evade all 4 detection layers"
  - id: cve-2026-22708
    type: documentation
    url: https://nvd.nist.gov/
    description: "Pillar Security demonstrated against Cursor January 2026 — implicitly-trusted shell built-in commands poisoned via indirect prompt injection; users see only final command, poisoning happens through commands the IDE never surfaces for approval"
  - id: cisco-skill-scanner
    type: documentation
    url: https://www.cisco.com/
    description: "Cisco's open-source AI Agent Security Scanner for IDEs — first agent-integration-layer scanner shipped April 2026"
  - id: snyk-mcp-scan
    type: documentation
    url: https://snyk.io/
    description: "Snyk's mcp-scan — companion tool for MCP server security; behavioral analysis of agent instruction files"
  - id: ox-security-mcp-marketplaces
    type: documentation
    url: https://ox.security/
    description: "OX Security April 2026 — researchers poisoned 9 of 11 MCP marketplaces using PoC servers"
  - id: trend-micro-mcp-exposure
    type: documentation
    url: https://trendmicro.com/
    description: "Trend Micro — initially 492 MCP servers exposed to internet with zero auth; by April 2026, 1,467 exposed servers"
  - id: anthropic-mcp-sdk
    type: documentation
    url: https://github.com/modelcontextprotocol
    description: "Anthropic's MCP SDK transport mechanism (per The Register) — vulnerability class inherited by any developer using the official SDK"
  - id: openclaw-sister-project
    type: wiki
    file: wiki/config/sister-projects.yaml
    description: "OpenClaw is registered in this wiki's sister-projects.yaml as 'Upstream parent of OpenArms — fork relationship, features flow both ways'. The article reports OpenClaw's ClawHub marketplace had 1,184 compromised skills — direct mission-relevance for the operator's ecosystem (OpenArms downstream → OpenClaw upstream → ClawHub supply-chain risk)"
  - id: trust-layer-concept
    type: wiki
    file: wiki/domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md
    description: "Trust-Layer Concept covers cypher/decypher/compression at the weight + I/O layers. This article documents a DIFFERENT attack surface — the agent integration layer — that operator's trust-layer composition does NOT cover. Layer 3 of the VentureBeat matrix is a candidate FIFTH dimension within trust."
  - id: custom-model-concept
    type: wiki
    file: wiki/domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md
    description: "Custom-Tailored Model Group Concept — M003 (Recreated Intelligence Layer at I/O Boundaries) gains output-boundary application: SKILL.md / MCP-config / rules-file inspection BEFORE agent ingests any new instruction artifact"
  - id: spec-driven-convergence-lesson
    type: wiki
    file: wiki/lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md
    description: "Spec-Driven Convergence Lesson — version-controlled SKILL.md / spec artifacts are precisely the attack surface this article identifies; the convergence's verification-checklist + closed-loop-sync rules become security primitives, not just quality primitives"
tags: [synthesis, security, supply-chain, agent-integration-layer, skill-md, mcp, sast, sca, cli-anything, openclaw, clawhub, clawhavoc, ddipe, cisco-skill-scanner, snyk-mcp-scan, prompt-injection, instruction-poisoning, root-ghostproxy-relevant, mission-2026-05-06]
---

# Synthesis — Agent Integration Layer Is the Supply-Chain Attack Surface No Scanner Sees

## Summary

VentureBeat 2026-05-05 (Louis Columbus) documents a structural gap in supply-chain security: between the **code layer** (where SAST scanners work) and the **dependency layer** (where SCA tools work), a third layer has emerged — the **agent integration layer** — covering SKILL.md files, MCP server configurations, Cursor rules files, and Claude Code skills. None of this looks like code; all of it executes like code through the AI agents that ingest it. The empirical proof points are concrete: **CLI-Anything (UHK Data Intelligence Lab, March 2026, 30,000+ GitHub stars)** generates SKILL.md files for any repo with a single command — supports Claude Code, Codex, OpenClaw, Cursor, GitHub Copilot CLI; **Snyk's ToxicSkills audit (February 2026)** found 76 confirmed malicious payloads across ClawHub and skills.sh; **13.4% of 3,984 audited skills had at least one critical issue**; daily skill submissions on ClawHub jumped <50 → 500+ in 2 weeks; **the ClawHavoc campaign (Koi Security Jan 2026 + Antiy CERT follow-up) confirmed 1,184 compromised packages** delivering Atomic Stealer (AMOS) through professionally-documented skills with developer-search-matching names (`solana-wallet-tracker`, `polymarket-trader`); the **DDIPE paper (Griffith + NTU + UNSW + U-Tokyo, April 2026)** documents 11.6%-33.5% bypass rates with 2.5% evading all 4 detection layers; **Anthropic's MCP SDK transport mechanism is identified as the root issue** for 1,467 internet-exposed MCP servers with zero auth; **CVE-2026-22708 (Pillar Security, January 2026)** demonstrated the variant against Cursor where shell built-ins get poisoned via indirect prompt injection. Cisco shipped the first IDE-side agent integration layer scanner (April 2026); Snyk shipped mcp-scan as the companion tool. **Mission relevance for this wiki's ecosystem**: (1) **OpenClaw is the upstream parent of OpenArms** in operator's ecosystem — ClawHub's 1,184 compromised skills directly threaten the operator's stack; (2) **root-ghostproxy's stated mission** (per operator 2026-05-04: *"its aiming to secure an OS and configure claude code and opencode at the root with all the safety needed"*) maps directly to the security-director action plan in this article — root-ghostproxy IS an agent-integration-layer security-tool candidate; (3) **the operator's [Trust-Layer Concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) covers weight + I/O layers** but does NOT yet cover instruction-artifact poisoning — Layer 3 of VB's matrix is a candidate FIFTH dimension WITHIN the trust layer (or a separate sub-layer at the agent-integration boundary); (4) **the [Spec-Driven Convergence Lesson](../../lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md)'s SKILL.md / spec artifacts ARE the attack surface this article identifies** — its verification-checklist + closed-loop-sync rules need security primitives, not just quality primitives.

## Reference

> [!info] Source identity
>
> | Field | Value |
> |---|---|
> | **Article** | "One command turns any open-source repo into an AI agent backdoor. OpenClaw proved no supply-chain scanner has a detection category for it" |
> | **Author** | Louis Columbus (VentureBeat) |
> | **Date** | 2026-05-05, 3:09 pm PT |
> | **Primary actors named** | UHK Data Intelligence Lab (CLI-Anything) · Snyk (ToxicSkills · mcp-scan) · Cisco (Skill Scanner) · Pillar Security (CVE-2026-22708) · Koi Security (ClawHavoc initial) · Antiy CERT (ClawHavoc follow-up) · OX Security (MCP marketplace poisoning) · Trend Micro (MCP server exposure) · Anthropic (MCP SDK root issue) · Griffith U + NTU + UNSW + U-Tokyo (DDIPE paper) |
> | **Primary frameworks named** | Claude Code · Codex · **OpenClaw** · Cursor · GitHub Copilot CLI · Cline (April 2026 4,000-machine npm incident) |
> | **Primary marketplaces named** | **ClawHub** (OpenClaw's marketplace — 1,184 compromised) · skills.sh · 11 MCP marketplaces |
> | **First-tools-shipped date** | April 2026 (Cisco Skill Scanner + Snyk mcp-scan) |

## Key Insights

> [!success] **The agent integration layer is a third structural layer between code (SAST) and dependencies (SCA) — currently invisible to mainstream security tooling.**
>
> The article's three-layer taxonomy:
>
> | Layer | What it covers | Tooling state | Detection gap |
> |---|---|---|---|
> | **1. Code** | Source files (insecure patterns, injection flaws, hardcoded secrets) | SAST (mature) | Most SAST tools have **no detection category** for prompt injection in AI-generated code |
> | **2. Dependencies** | Package versions vs CVEs, SBOM generation, outdated libraries | SCA (mature) | SCA generates **no AI-specific BoM**; agent-layer dependencies are invisible |
> | **3. Agent integration** | SKILL.md files, MCP configs, Cursor rules, Claude Code skills | **None until April 2026** | No tool inspects the **semantic meaning** of agent instruction files |
>
> Cisco engineering blog: *"SAST scanners analyze source code syntax. SCA tools check dependency versions. Neither understands the semantic layer where MCP tool descriptions, agent prompts, and skill definitions operate."* Merritt Baer (Enkrypt AI CSO, ex-AWS Deputy CISO): *"SAST and SCA were built for code and dependencies. They don't inspect instructions."*

> [!success] **OpenClaw / ClawHub is operator-ecosystem-critical: 1,184 compromised packages = direct supply-chain risk to the operator's stack.**
>
> Per [sister-projects.yaml](../../../wiki/config/sister-projects.yaml): **OpenClaw is "Upstream parent of OpenArms — fork relationship, features flow both ways."** The article reports:
>
> - **341 malicious skills initially identified by Koi Security** (Jan 2026 ClawHavoc campaign first report)
> - **1,184 compromised packages confirmed by Antiy CERT** (follow-up analysis)
> - Campaign delivered **Atomic Stealer (AMOS)** through professionally-documented skills
> - Skill names like `solana-wallet-tracker` and `polymarket-trader` matched what developers searched for
> - **13.4% of all 3,984 audited skills (Snyk ToxicSkills, Feb 2026) contained at least one critical security issue**
> - Daily skill submissions on ClawHub jumped from <50 to 500+ in 2 weeks
> - **Barrier to publishing**: a SKILL.md file + a 1-week-old GitHub account. No code signing. No security review. No sandbox.
>
> **Operator-mission implication**: OpenArms (operator's project) inherits OpenClaw's supply-chain attack surface. Any skill the operator pulls from ClawHub is in this 13.4%-critical-issue / 1,184-compromised population by default. The [Trust-Layer Epic](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md)'s threat model needs to extend to skill-source provenance.

> [!success] **root-ghostproxy is operationally aligned with this article's security-director action plan.**
>
> Operator-stated 2026-05-04: *"The project is called root-ghostproxy and its a new type of project but its IAC and its basically a IPS sitting in between the Edge firewall (OPNSense) and the first switch / the local network. its aiming to **secure an OS and configure claude code and opencode at the root with all the safety needed**."* The article's recommended action plan maps directly:
>
> | Article action | root-ghostproxy delivery |
> |---|---|
> | "Inventory every agent bridge tool in the environment" | OS-level inventory of installed agents (CC + OpenCode + ...) at root |
> | "Audit agent skill sources the same way package registries get audited" | Allowlist + skill-source audit at OS level |
> | "Deploy agent-layer scanning" (Cisco Skill Scanner, Snyk mcp-scan, or 2nd-engineer review) | root-ghostproxy can integrate Cisco/Snyk scanners into the OS-config pipeline |
> | "Restrict agent execution privileges and instrument runtime" | OS-level permission policies + runtime observability — IPS+IaC role of root-ghostproxy |
> | "Assign ownership for the gap between layers" | root-ghostproxy IS that ownership at OS+network boundary |
>
> **The article's framing operationalizes root-ghostproxy's mission with concrete checkpoints.** When root-ghostproxy lands at `~/root-ghostproxy/`, this article is the security-rationale document for its IPS+IaC scope.

> [!success] **Anthropic's MCP SDK transport is identified as the root vulnerability class — 1,467 exposed MCP servers, zero authentication.**
>
> Per The Register (cited in article): *"the root issue lies in Anthropic's MCP software development kit (SDK) transport mechanism. Any developer using the official SDK inherits the vulnerability class."* OX Security April 2026: **9 of 11 MCP marketplaces poisoned** with PoC servers. Trend Micro: **492 → 1,467 internet-exposed MCP servers with zero auth** (Jan → April 2026). **Operator-mission implication**: this wiki's `tools/mcp_server.py` IS an MCP server — the operator should evaluate whether it's exposed and what auth it has. Per [.claude/rules/hook-architecture.md](../../../.claude/rules/hook-architecture.md) the wiki's MCP server is intentional infrastructure; security review against this article's findings would close a real gap.

> [!success] **DDIPE bypass rates: 11.6%-33.5% across 4 agent frameworks × 5 LLMs; 2.5% evade all 4 detection layers.**
>
> Per Griffith + NTU + UNSW + U-Tokyo April 2026 paper: **Document-Driven Implicit Payload Execution (DDIPE)** embeds malicious logic inside code examples within skill documentation. Empirical attack-success rates:
>
> - **Bypass rates**: 11.6%-33.5% across 4 agent frameworks × 5 LLMs
> - **Evading all 4 detection layers**: 2.5% (deep evasion)
> - **Responsible disclosure outcome**: 4 confirmed vulnerabilities + 2 vendor fixes
>
> **The 11.6% lower bound means even with current best-effort detection, ~1 in 9 DDIPE payloads succeeds.** The 2.5% deep-evasion rate is the long tail that defeats stacked detection. Operator's [Custom-Tailored Senior-Engineer-Tier Model Group Concept](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) M003 (Recreated Intelligence Layer at I/O Boundaries) gains a NEW input-boundary requirement: SKILL.md / MCP-config / rules-file inspection BEFORE agent ingests any instruction artifact.

> [!success] **The Cline incident: one crafted GitHub issue title → 8 hours of attacker access on ~4,000 developer machines.**
>
> Documented April 2026 attack chain: *"a crafted GitHub issue title triggered an AI triage bot wired into Cline. The bot exfiltrated a GITHUB_TOKEN, which the attacker used to publish a compromised npm dependency that installed a second agent on roughly 4,000 developer machines for eight hours."* This is the **end-to-end fully-automated supply-chain attack** the article warns about — from issue title to npm publish to second-agent install on developer machines. Mission-implication: the operator's [Multica orchestrator](../../decisions/01_drafts/adopt-multica-as-orchestrator-layer-post-anthropic-stack-2026-04.md) routing pattern must include skill / MCP source allowlisting at the orchestrator layer, not just at the developer's IDE.

> [!info] **The "flat authorization plane" structural flaw — compromised skills don't escalate, they already have privileges.**
>
> Carter Rees (VP AI, Reputation): *"A significant vulnerability in enterprise AI is broken access control, where the flat authorization plane of an LLM fails to respect user permissions."* The agent runs with the developer's credentials; a poisoned skill rides those credentials directly. **EDR sees an approved API call from an authorized process and passes it.** This is the structural reason why Cisco / Snyk / 2nd-engineer review at the integration layer is **strictly necessary** — runtime detection at the API/EDR layer is insufficient by design.

## Deep Analysis

### The Three-Layer Matrix Mapped to Operator's Mission

| VB Layer | VB Threat | Operator's wiki/mission coverage | Gap |
|---|---|---|---|
| **1. Code** | Prompt injection in AI-generated code | Spec-Driven Convergence Lesson + verification checklists in operator's authored content | Wiki's `tools/` Python is operator-authored — low risk; AI-generated code review process is not yet documented as a security gate |
| **2. Dependencies** | Malicious MCP servers, agent skills, plugin registries | Sister-projects.yaml registry IS the wiki's first-pass dependency inventory for cross-project artifacts | NO inventory yet of: MCP servers consumed (this wiki has its own at `tools/mcp_server.py`); agent skills pulled from ClawHub/skills.sh; plugin registries trusted; allowlists |
| **3. Agent integration** | SKILL.md, MCP configs, rules files, instruction sets | **NOT YET COVERED** — wiki's CLAUDE.md / AGENTS.md / .claude/rules/ are operator-authored and trusted, but there's no security review process for INCOMING instruction artifacts (e.g., a sister project's SKILL.md being consumed) | Cisco Skill Scanner + Snyk mcp-scan integration is candidate work; root-ghostproxy is the OS-level enforcement point when it lands |

### Connection to Trust-Layer Concept (5th Dimension Candidate)

The operator's [Trust-Layer Concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) currently covers:

1. Weights (cypher/decypher at rest + during inference)
2. KV cache (compressed-encrypted)
3. Context I/O (Caveman compression + cypher overlay)
4. Attestation chain (NVIDIA H100/H200 CC mode at L3)
5. Internal-langue interpretability (SAE-decypher per [Qwen-Scope synthesis](src-qwen-scope-sparse-autoencoders-llm-interpretability-suite.md))

**This article surfaces a 6th dimension: agent-integration artifacts (SKILL.md / MCP / rules)** — the operator's keys/passphrases/certificates secure the WEIGHTS but say nothing about whether the SKILL.md the agent ingests is poisoned. Even at L3 trust, a poisoned skill executes with the agent's legitimate credentials. **Candidate addition to Trust-Layer Concept**: an L1.5 or L2.5 opt-in covering "instruction-artifact provenance + integrity" — operator-signed SKILL.md / MCP configs / rules files; allowlist of trusted skill sources; runtime verification of skill source against allowlist before ingestion.

### Connection to Custom-Tailored Model Group M003 (Recreated Intelligence Layer at I/O Boundaries)

Operator's M003 already names input-boundary intelligence (routing + Caveman compression + spec loading + context selection + tool-use planning) and output-boundary intelligence (schema gate + self-verification + methodology compliance + hallucination detection). **This article adds a third boundary**: the **instruction-artifact-ingestion boundary** — every time the agent reads a new SKILL.md / MCP config / rules file, that artifact must be inspected for DDIPE-style payloads. The 2.5% deep-evasion rate from the DDIPE paper means a stacked defense (Cisco Skill Scanner + Snyk mcp-scan + 2nd-engineer review + behavioral runtime monitoring) is required.

### Connection to Spec-Driven Convergence Lesson (Security Primitive Extension)

Per [Spec-Driven Convergence Lesson](../../lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md): "Treat prompts/specs/contexts as version-controlled first-class artifacts. Not ad-hoc chat." The convergence's 8 instances ALL use SKILL.md / spec-equivalent artifacts that the agent ingests at session start. **The convergence's quality primitives become security primitives** under this article's framing:

| Convergence quality primitive | Security primitive extension |
|---|---|
| "Specs as version-controlled first-class artifacts" | + cryptographic signing of specs by trusted authors; signature verification at ingest |
| "Verification checklist per spec" | + DDIPE detection check; embedded-payload scan; source-allowlist check |
| "Closed-loop sync rule (fix prompt first, then code)" | + when a spec is modified, re-verify signatures + re-scan for payloads before agent re-ingests |
| "Three core skills (abstraction-first / alignment / iterative review)" | + threat-model-first as a fourth core skill at the integration layer |

**The convergence is mission-critical for security, not just quality.** Treating specs as ad-hoc chat = inheriting ClawHavoc-class supply-chain risk by default.

### Connection to OpenClaw Sister-Project (Direct Operator-Ecosystem Risk)

OpenClaw is in [sister-projects.yaml](../../config/sister-projects.yaml) as OpenArms's upstream. The article reports OpenClaw's ClawHub marketplace had 1,184 compromised skills. **Concrete operator-side actions**:

1. Audit which skills (if any) are pulled from ClawHub into OpenArms / OpenClaw / this wiki
2. Verify the wiki's `tools/mcp_server.py` is not exposed to the internet (the 1,467-exposed-with-zero-auth statistic)
3. Surface to operator: should a security-evaluation workstream be added to the OpenClaw / OpenArms sister-project relationship?

## Quotes (verbatim from article)

> *"The security problem is not what CLI-Anything does. It is what CLI-Anything represents."* — VentureBeat editorial framing

> *"A skill is effectively untrusted executable intent, even if it's just text."* — Merritt Baer, CSO Enkrypt AI

> *"SAST and SCA were built for code and dependencies. They don't inspect instructions."* — Merritt Baer

> *"Modern LLMs rely on third-party plugins, introducing supply chain vulnerabilities where compromised tools can inject malicious data into the conversation flow, bypassing internal safety training."* — Carter Rees, VP AI Reputation

> *"A significant vulnerability in enterprise AI is broken access control, where the flat authorization plane of an LLM fails to respect user permissions."* — Carter Rees

> *"This feels very similar to early container security, but we're still in the 'we'll get to it' phase across most orgs."* — Merritt Baer

> *"The bar to entry is extremely low. Adding a skill can be as simple as uploading a Word doc or lightweight config file. That's a radically different risk profile than compiled code."* — Merritt Baer

> *"There's no build pipeline, no compilation barrier. Just content."* — Merritt Baer (on the speed difference vs container security)

## Open Questions

> [!question] Should agent-integration-layer security become a wiki-side workstream?
> Concrete proposal: a new domain `wiki/domains/security/` covering: (a) agent-integration-layer threat model; (b) sister-project skill-source audit (OpenClaw + OpenArms + this wiki's MCP server); (c) DDIPE detection patterns; (d) Cisco/Snyk tool integration. Or fold under the existing trust-layer concept as a 6th dimension. Operator-decision.

> [!question] Is `tools/mcp_server.py` exposed to the internet?
> Empirical question. Per the article: 1,467 MCP servers exposed with zero auth as of April 2026. The wiki's MCP server should be audited for: bind address (localhost vs 0.0.0.0), auth presence, allowlist of clients. If exposed, immediate-action territory.

> [!question] Has any ClawHub skill been pulled into OpenArms or this wiki?
> Sister-project context: OpenClaw is OpenArms's upstream. If OpenArms consumes any ClawHub skill, the 13.4%-critical-rate / 1,184-compromised population is the threat surface. Audit needed.

> [!question] Does root-ghostproxy's IPS scope cover the agent integration layer specifically?
> Operator-stated mission: "secure an OS and configure claude code and opencode at the root with all the safety needed." This article makes "all the safety needed" concrete: includes Cisco Skill Scanner + Snyk mcp-scan + skill-source allowlisting + flat-authorization-plane fix at runtime. Operator-decision whether root-ghostproxy explicitly takes this scope.

> [!question] Should the wiki's CLAUDE.md / AGENTS.md / .claude/rules/ be cryptographically signed?
> The convergence-lesson security-primitive extension argues yes — operator-signed instruction artifacts are the integrity gate. But signing introduces tooling overhead. Operator-decision per cost/benefit.

> [!question] Does the operator's existing skill set (per `update-config` / `idea-capture` / etc. in the available skills list) come from a trusted-source allowlist or from ClawHub-equivalent?
> The system reminder at session start lists ~80 skills available. Source provenance + freshness of those skills is operator-relevant security information. Audit + allowlist enforcement is a candidate next step.

## Relationships

- BUILDS ON: [[secure-tamper-proof-model-on-shared-gpu-research-synthesis|Trust-Layer Concept]] — surfaces a 6th candidate dimension (agent-integration-layer artifact integrity)
- BUILDS ON: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]] — adds instruction-artifact-ingestion boundary to M003 (Recreated Intelligence Layer)
- BUILDS ON: [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Convergence Lesson]] — converges quality primitives to security primitives
- BUILDS ON: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — agent-integration-layer is a substitutable axis (Cisco Skill Scanner · Snyk mcp-scan · 2nd-engineer review · operator-built per root-ghostproxy)
- RELATES TO: [[adopt-multica-as-orchestrator-layer-post-anthropic-stack-2026-04|Decision — Adopt Multica]] — orchestrator-layer skill/MCP source allowlisting
- RELATES TO: [[src-strands-agents-aws-intent-based-tool-design-96-percent-token-reduction|Strands Agents Synthesis]] — Strands' MCP gateway pattern is also the attack surface this article documents (semantic-search over compromised tool catalogs amplifies risk)
- RELATES TO: [[src-cavekit-spec-driven-development-claude-code-julius-brussee|Cavekit v4 Synthesis]] — Cavekit's SPEC.md + 2 skills are minimum-viable-shape; security review of those 2 skills' provenance is mission-relevant
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — Cisco Skill Scanner is infrastructure; "review every SKILL.md carefully" prose instruction is ~25% compliance
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — "this skill is safe" is aspirational without scanner verification

## Backlinks

[[Trust-Layer Concept]]
[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]]
[[Spec-Driven Convergence Lesson]]
[[Anti-Vendor-Lock-In Lesson]]
[[Decision — Adopt Multica]]
[[src-strands-agents-aws-intent-based-tool-design-96-percent-token-reduction|Strands Agents Synthesis]]
[[Cavekit v4 Synthesis]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]

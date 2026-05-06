# One command turns any open-source repo into an AI agent backdoor. OpenClaw proved no supply-chain scanner has a detection category for it

Source: https://venturebeat.com/security/one-command-open-source-repo-ai-agent-backdoor-openclaw-supply-chain-scanner
Author: Louis Columbus
Published: 3:09 pm PT, May 5, 2026
Ingested: 2026-05-06 (operator-pasted content; pipeline fetch returned 429)
Type: article

---

Just two months ago, researchers at the Data Intelligence Lab at the University of Hong Kong introduced CLI-Anything, a new state-of-the-art tool that analyzes any repo's source code and generates a structured command line interface (CLI) that AI coding agents can operate with a single command.

Claude Code, Codex, OpenClaw, Cursor, and GitHub Copilot CLI are all supported, and since its launch in March, CLI‑Anything has climbed to more than 30,000 GitHub stars.

But the same mechanism that makes software agent-native opens the door to agent-level poisoning. The attack community is already discussing the implications on X and security forums, translating CLI-Anything's architecture into offensive playbooks.

The security problem is not what CLI-Anything does. It is what CLI-Anything represents.

CLI-Anything generates SKILL.md files, the same instruction-layer artifacts that Snyk's ToxicSkills research found laced with 76 confirmed malicious payloads across ClawHub and skills.sh in February 2026. A poisoned skill definition does not trigger a CVE and never appears in a software bill of materials (SBOM). No mainstream security scanner has a detection category for malicious instructions embedded in agent skill definitions, because the category simply did not exist eighteen months ago.

Cisco confirmed the gap in April. "Traditional application security tools were not designed for this," Cisco's engineering team wrote in a blog post announcing its AI Agent Security Scanner for IDEs. "SAST [static application security testing] scanners analyze source code syntax. SCA [software composition analysis] tools check dependency versions. Neither understands the semantic layer where MCP [Model Context Protocol] tool descriptions, agent prompts, and skill definitions operate."

Merritt Baer, CSO of Enkrypt AI and former Deputy CISO at Amazon Web Services (AWS), told VentureBeat in an exclusive interview: "SAST and SCA were built for code and dependencies. They don't inspect instructions."

This is not a single-vendor vulnerability. It is a structural gap in how the entire security industry monitors software supply chains. This is the pre-exploitation window. CLI-Anything is live, the attack community is discussing it, and security directors who act now get ahead of the first incident report.

## The integration layer no stack can see

Traditional supply-chain security operates on two layers. The code layer is where SAST works, scanning source files for insecure patterns, injection flaws, and hardcoded secrets. The dependency layer is where SCA works, checking package versions against known vulnerabilities, generating SBOMs, and flagging outdated libraries.

Agent bridge tools like CLI-Anything, MCP connectors, Cursor rules files, and Claude Code skills operate on a third layer between the other two. Call it the agent integration layer: configuration files, skill definitions, and natural-language instruction sets tell an AI agent what software can do and how to operate it. None of it looks like code. All of it executes like code.

Carter Rees, VP of AI at Reputation, told VentureBeat in an exclusive interview: "Modern LLMs [large language models] rely on third-party plugins, introducing supply chain vulnerabilities where compromised tools can inject malicious data into the conversation flow, bypassing internal safety training."

Researchers at Griffith University, Nanyang Technological University, the University of New South Wales, and the University of Tokyo documented the attack chain in an April paper, "Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems." The team introduced Document-Driven Implicit Payload Execution (DDIPE), a technique that embeds malicious logic inside code examples within skill documentation.

Across four agent frameworks and five large language models, DDIPE achieved bypass rates between 11.6% and 33.5%. Static analysis caught most samples, but 2.5% evaded all four detection layers. Responsible disclosure led to four confirmed vulnerabilities and two vendor fixes.

## The kill chain security leaders need to audit

Here's the anatomy of the kill chain: An attacker submits a SKILL.md file to an open-source project containing setup instructions, code examples, and configuration templates. It looks like standard documentation. A code reviewer would wave it through because none of it is executable. But the code examples contain embedded instructions that an agent will parse as operational directives.

A developer uses an agent bridge tool to connect their coding agent to the repository. The agent ingests the skill definition and trusts it, because no verification layer exists to distinguish benign from malicious intent at the instruction level.

The agent executes the embedded instruction using its own legitimate credentials. Endpoint detection and response (EDR) sees an approved API call from an authorized process and passes it. Data exfiltration, configuration changes, and credential harvesting are all moving through channels that the monitoring stack considers normal traffic.

Rees identified the structural flaw that makes this chain lethal. "A significant vulnerability in enterprise AI is broken access control, where the flat authorization plane of an LLM fails to respect user permissions," he told VentureBeat. A compromised skill definition riding that flat authorization plane does not need to escalate privileges. It already has them. Every link in that chain is invisible to the current security stack.

Pillar Security demonstrated a variant of this chain against Cursor in January 2026 (CVE-2026-22708). Implicitly trusted shell built-in commands could be poisoned through indirect prompt injection, converting benign developer commands into arbitrary code execution vectors. Users saw only the final command. The poisoning happened through other commands the IDE never surfaced for approval.

## The evidence is already in production

In a documented attack chain from April 2026, a crafted GitHub issue title triggered an AI triage bot wired into Cline. The bot exfiltrated a GITHUB_TOKEN, which the attacker used to publish a compromised npm dependency that installed a second agent on roughly 4,000 developer machines for eight hours. There was just one issue title. Attackers had eight hours of access. No human approved the action.

Snyk's ToxicSkills audit scanned 3,984 agent skills from ClawHub, the public marketplace for the OpenClaw agent framework, and skills.sh in February 2026. The results: 13.4% of all skills contained at least one critical security issue. Daily skill submissions jumped from less than 50 in mid-January to more than 500 by early February. The barrier to publishing was a SKILL.md markdown file and a GitHub account one week old. No code signing. No security review. No sandbox.

OpenClaw is not an outlier. It is the pattern. "The bar to entry is extremely low," Baer said. "Adding a skill can be as simple as uploading a Word doc or lightweight config file. That's a radically different risk profile than compiled code." She pointed to projects like ClawPatrol that have started cataloging and scanning for malicious skills, evidence the ecosystem is moving faster than enterprise defenses.

The ClawHavoc campaign, first reported by Koi Security in late January 2026, initially identified 341 malicious skills on ClawHub. A follow-up analysis by Antiy CERT expanded the count to 1,184 compromised packages across the platform. The campaign delivered Atomic Stealer (AMOS) through skill definitions with professional documentation. Skills named solana-wallet-tracker and polymarket-trader matched what developers actively searched for.

The MCP protocol layer carries similar exposure. OX Security reported in April that researchers poisoned nine out of 11 MCP marketplaces using proof-of-concept servers. Trend Micro initially found 492 MCP servers exposed to the internet with zero authentication; by April, that number had grown to 1,467. As The Register reported, the root issue lies in Anthropic's MCP software development kit (SDK) transport mechanism. Any developer using the official SDK inherits the vulnerability class.

## VentureBeat Prescriptive Matrix: Three-layer agent supply-chain audit

VentureBeat developed a Prescriptive Matrix by mapping the three attack layers documented in the research and incident reports above against the detection capabilities of current SAST, SCA, and agent-layer tools. Each row identifies what security teams should verify and where no scanner has coverage today.

| Layer | Threat | Current detection | Why it misses | Recommended action |
|---|---|---|---|---|
| 1. Code | Prompt injection in AI-generated code | SAST scanners | Most SAST tools have no detection category for prompt injection in AI-generated code | Confirm that SAST scans AI-generated code for prompt injection. If not, have an open vendor conversation this quarter. |
| 2. Dependencies | Malicious MCP servers, agent skills, plugin registries | SCA tools | SCA generates no AI-specific bill of materials. Agent-layer dependencies are invisible. | Confirm SCA includes MCP servers, agent skills, and plugin registries in the dependency inventory. |
| 3. Agent integration | Poisoned SKILL.md files, malicious instruction sets, adversarial rules files | None until April 2026 | No tool inspects the semantic meaning of agent instruction files. Baer: "We're not inspecting intent." | Deploy Cisco Skill Scanner or Snyk mcp-scan. Assign a team to own this layer. |

Baer's diagnosis of Layer 3 applies across the entire matrix: "Current scanners look for known bad artifacts, not adversarial instructions embedded in otherwise valid skills." Cisco's open-source Skill Scanner and Snyk's mcp-scan represent the first tools purpose-built for this layer.

## Security director action plan

Here's how security leaders can get ahead of the problem.

Inventory every agent bridge tool in the environment. This includes CLI-Anything, MCP connectors, Cursor rules files, Claude Code skills, GitHub Copilot extensions. If the development team is using agent bridge tools that have not been inventoried, the risk cannot be assessed.

Audit agent skill sources the same way package registries get audited. Baer's framing is precise: "A skill is effectively untrusted executable intent, even if it's just text." Shut off ungoverned ingestion paths until controls are in place. Stand up a review and allowlisting process for skills. The OWASP Agentic Skills Top 10 (AST01: Malicious Skills) provides the procurement framework to align controls against.

Deploy agent-layer scanning. Evaluate Cisco's open-source Skill Scanner and Snyk's mcp-scan for behavioral analysis of agent instruction files. If dedicated tooling is unavailable, require a second engineer to read every SKILL.md before installation.

Restrict agent execution privileges and instrument runtime. AI coding agents should not run with the same credential scope as the developer who invoked them. Rees confirmed the structural flaw: The flat authorization plane means a compromised skill does not need to escalate privileges. Baer's prescription: "Instrument runtime observability. What data is the agent accessing, what actions is it taking, and are those aligned with expected behavior?"

Assign ownership for the gap between layers. The most dangerous attacks succeed because they fall between detection categories. Assign a team to own the agent integration layer. Review every SKILL.md, MCP config, and rules file before it enters the environment.

## The gap that already has a name

Baer underscored the dangers of this new attack vector. "This feels very similar to early container security, but we're still in the 'we'll get to it' phase across most orgs," she said. She added that, at AWS, it took a few high-profile wake-up calls before container security became table stakes. The difference this time is speed. "There's no build pipeline, no compilation barrier. Just content," she said.

CLI-Anything is not the threat. It is the proof case that the agent integration layer exists, that it is growing fast, and that the attacker community has already found it. The 33,000 developers who starred the repository are telling security teams where software development is heading. Eighteen months ago, the detection category for agent-integration-layer poisoning did not exist. Cisco and Snyk shipped the first tools for it in April. The window between those two facts is closing. Security directors who have not begun inventory are already behind.

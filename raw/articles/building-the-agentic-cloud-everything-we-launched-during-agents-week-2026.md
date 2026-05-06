# Building the agentic cloud: everything we launched during Agents Week 2026

Source: https://blog.cloudflare.com/agents-week-in-review/
Ingested: 2026-05-06
Type: article

---

---
description: Agents Week 2026 is a wrap. Let’s take a look at everything we announced, from compute and security to the agent toolbox, platform tools, and the emerging agentic web. Everything we shipped for the agentic cloud.

title: Building the agentic cloud: everything we launched during Agents Week 2026
image: https://cf-assets.www.cloudflare.com/zkvhlag99gkb/25twxcfrFmVdPOM25w44Kz/61e7071d4f1fef8a5ea9b979e7871684/Building_the_agentic_cloud-_everything_we_launched_during_Agents_Week_2026-OG.png
---

# Building the agentic cloud: everything we launched during Agents Week 2026

2026-04-20

* [![Ming Lu](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/15tKckibXhwPEckLeCWGle/a0bc2f5d0219244489150cc090c04357/0b44a65c-00b0-4550-8cbd-724f7960252a_800x800.png)](https://blog.cloudflare.com/author/ming-lu/)  
[Ming Lu](https://blog.cloudflare.com/author/ming-lu/)
* [![Anni Wang](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/3RnKI54hxLOIRs0QBSZgxa/e71b8f7a5ccadb45dd553c69f8ffe539/anni.png)](https://blog.cloudflare.com/author/anni/)  
[Anni Wang](https://blog.cloudflare.com/author/anni/)

8 min read

This post is also available in [简体中文](https://blog.cloudflare.com/zh-cn/agents-week-in-review), [Français](https://blog.cloudflare.com/fr-fr/agents-week-in-review), [Deutsch](https://blog.cloudflare.com/de-de/agents-week-in-review), [Italiano](https://blog.cloudflare.com/it-it/agents-week-in-review), [日本語](https://blog.cloudflare.com/ja-jp/agents-week-in-review), [한국어](https://blog.cloudflare.com/ko-kr/agents-week-in-review), [Español (Latinoamérica)](https://blog.cloudflare.com/es-la/agents-week-in-review), [Español](https://blog.cloudflare.com/es-es/agents-week-in-review) and [繁體中文](https://blog.cloudflare.com/zh-tw/agents-week-in-review).

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/7JDUBjXv45ARm2pvdCN3DP/c95854c24522463acee97bffb40a4ced/BLOG-3239_1.png)

Today marks the end of our first Agents Week, an innovation week dedicated entirely to the age of agents. It couldn’t have been more timely: over the past year, agents have swiftly changed how people work. Coding agents are helping developers ship faster than ever. Support agents resolve tickets end-to-end. Research agents validate hypotheses across hundreds of sources in minutes. And people aren't just running one agent: they're running several in parallel and around the clock.

As Cloudflare's CTO Dane Knecht and VP of Product Rita Kozlov noted in our [welcome to Agents Week post](https://blog.cloudflare.com/welcome-to-agents-week/), the potential scale of agents is staggering: If even a fraction of the world's knowledge workers each run a few agents in parallel, you need compute capacity for tens of millions of simultaneous sessions. The one-app-serves-many-users model the cloud was built on doesn't work for that. But that's exactly what developers and businesses want to do: build agents, deploy them to users, and run them at scale.

Getting there means solving problems across the entire stack. Agents need **compute** that scales from full operating systems to lightweight isolates. They need **security** and identity built into how they run. They need an **agent toolbox**: the right models, tools, and context to do real work. All the code that agents generate needs a clear path from afternoon **prototype to production** app. And finally, as agents drive a growing share of Internet traffic, the web itself needs to adapt for the emerging **agentic web**. Turns out, the containerless, serverless compute platform we launched eight years ago with Workers was ready-made for this moment. Since then, we've grown it into a full platform, and this week we shipped the next wave of primitives purpose-built for agents, organized around exactly those problems.

We are here to create Cloud 2.0 — the agentic cloud. Infrastructure designed for a world where agents are a primary workload. 

Here's a list of everything we announced this week — we wouldn’t want you to miss a thing.

## Compute

[ ](#compute) 

It starts with compute. Agents need somewhere to run, and somewhere to store and run the code they write. Not all agents need the same thing: some need a full operating system to install packages and run terminal commands, most need something lightweight that starts in milliseconds and scales to millions. This week we shipped the environments to run them, as well as a new Git-compatible workspace for agents:

| **Announcement**                                                                                                                                      | **Summary**                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Artifacts: Versioned storage that speaks Git](https://blog.cloudflare.com/artifacts-git-for-agents-beta)                                             | Give your agents, developers, and automations a home for code and data. We’ve just launched Artifacts: Git-compatible versioned storage built for agents. Create tens of millions of repos, fork from any remote, and hand off a URL to any Git client. |
| [Agents have their own computers with Sandboxes GA](https://blog.cloudflare.com/sandbox-ga/)                                                          | Cloudflare Sandboxes give AI agents a persistent, isolated environment: a real computer with a shell, a filesystem, and background processes that starts on demand and picks up exactly where it left off.                                              |
| [Dynamic, identity-aware, and secure: egress controls for Sandboxes](https://blog.cloudflare.com/sandbox-auth/)                                       | Outbound Workers for Sandboxes provide a programmable, zero-trust egress proxy for AI agents. This allows developers to inject credentials and enforce dynamic security policies without exposing sensitive tokens to untrusted code.                   |
| [Durable Objects in Dynamic Workers: Give each AI-generated app its own database](https://blog.cloudflare.com/durable-object-facets-dynamic-workers/) | Durable Object Facets allows Dynamic Workers to instantiate Durable Objects with their own isolated SQLite databases. This enables developers to build platforms that run persistent, stateful code generated on-the-fly.                               |
| [Rearchitecting the Workflows control plane for the agentic era](https://blog.cloudflare.com/workflows-v2/)                                           | Cloudflare Workflows, a durable execution engine for multi-step applications, now supports 50,000 concurrency and 300 creation rate limits through a rearchitectured control plane, helping scale to meet the use cases for durable background agents.  |

## Security

[ ](#security) 

Running agents and their code is only half the challenge. Agents connect to private networks, access internal services, and take autonomous actions on behalf of users. When anyone in an organization can spin up their own agents, security can't be an afterthought. It has to be the default. This week, we launched the tools to make that easy.

| **Announcement**                                                                                                                               | **Summary**                                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Secure private networking for everyone: users, nodes, agents, Workers — introducing Cloudflare Mesh](https://blog.cloudflare.com/mesh/)       | Cloudflare Mesh provides secure, private network access for users, nodes, and autonomous AI agents. By integrating with Workers VPC, developers can now grant agents scoped access to private databases and APIs without manual tunnels.  |
| [Managed OAuth for Access: make internal apps agent-ready in one click](https://blog.cloudflare.com/managed-oauth-for-access/)                 | Managed OAuth for Cloudflare Access helps AI agents securely navigate internal applications. By adopting RFC 9728, agents can authenticate on behalf of users without using insecure service accounts.                                    |
| [Securing non-human identities: automated revocation, OAuth, and scoped permissions](https://blog.cloudflare.com/improved-developer-security/) | Cloudflare is introducing scannable API tokens, enhanced OAuth visibility, and GA for resource-scoped permissions. These tools help developers implement a true least-privilege architecture while protecting against credential leakage. |
| [Scaling MCP adoption: our reference architecture for enterprise MCP deployments](https://blog.cloudflare.com/enterprise-mcp/)                 | We share Cloudflare's internal strategy for governing MCP using Access, AI Gateway, and MCP server portals. We also launch Code Mode to slash token costs and recommend new rules for detecting Shadow MCP in Cloudflare Gateway.         |

## Agent Toolbox

[ ](#agent-toolbox) 

A capable agent needs to be able to think and remember, communicate, and see. This means being powered with the right models, with access to the right tools and the right context for their task at hand. This week we shipped the primitives — inference, search, memory, voice, email, and a browser — that turn an agent into something that actually gets work done.

| **Announcement**                                                                                                               | **Summary**                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Project Think: building the next generation of AI agents on Cloudflare](https://blog.cloudflare.com/project-think/)           | Announcing a preview of the next edition of the Agents SDK — from lightweight primitives to a batteries-included platform for AI agents that think, act, and persist.                                                                                                                                                             |
| [Add voice to your agent](https://blog.cloudflare.com/voice-agents/)                                                           | An experimental voice pipeline for the Agents SDK enables real-time voice interactions over WebSockets. Developers can now build agents with continuous STT and TTS in just \~30 lines of server-side code.                                                                                                                       |
| [Cloudflare Email Service: now in public beta. Ready for your agents](https://blog.cloudflare.com/email-for-agents/)           | Agents are becoming multi-channel. That means making them available wherever your users already are — including the inbox. Cloudflare Email Service enters public beta with the infrastructure layer to make that easy: send, receive, and process email natively from your agents.                                               |
| [Cloudflare's AI platform: an inference layer designed for agents ](https://blog.cloudflare.com/ai-platform/)                  | We're building Cloudflare into a unified inference layer for agents, letting developers call models from 14+ providers. New features include Workers binding for running third-party models and an expanded catalog with multimodal models.                                                                                       |
| [Building the foundation for running extra-large language models](https://blog.cloudflare.com/high-performance-llms/)          | We built a custom technology stack to run fast large language models on Cloudflare’s infrastructure. This post explores the engineering trade-offs and technical optimizations required to make high-performance AI inference accessible.                                                                                         |
| [Unweight: how we compressed an LLM 22% without sacrificing quality](https://blog.cloudflare.com/unweight-tensor-compression/) | Running large LLMs across Cloudflare’s network requires us to be smarter and more efficient about GPU memory bandwidth. That’s why we developed Unweight, a lossless inference-time compression system that achieves up to a 22% model footprint reduction, so that we can deliver faster and cheaper inference than ever before. |
| [Agents that remember: introducing Agent Memory](https://blog.cloudflare.com/introducing-agent-memory/)                        | Cloudflare Agent Memory is a managed service that gives AI agents persistent memory, allowing them to recall what matters, forget what doesn't, and get smarter over time.                                                                                                                                                        |
| [AI Search: the search primitive for your agents](https://blog.cloudflare.com/ai-search-agent-primitive/)                      | AI Search is the search primitive for your agents. Create instances dynamically, upload files, and search across instances with hybrid retrieval and relevance boosting. Just create a search instance, upload, and search.                                                                                                       |
| [Browser Run: give your agents a browser](https://blog.cloudflare.com/browser-run-for-ai-agents/)                              | Browser Rendering is now Browser Run, with Live View, Human in the Loop, CDP access, session recordings, and 4x higher concurrency limits for AI agents.                                                                                                                                                                          |

## Prototype to production

[ ](#prototype-to-production) 

The best infrastructure is also one that’s easy to use. We want to meet developers and their agents where they’re already working: in the terminal, in the editor, in a prompt, and make the full Cloudflare platform accessible without context-switching.

| **Announcement**                                                                                                                        | **Summary**                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Building a CLI for all of Cloudflare](https://blog.cloudflare.com/cf-cli-local-explorer/)                                              | We’re introducing cf, a new unified CLI designed for consistency across the Cloudflare platform, alongside Local Explorer for debugging local data. These tools simplify how developers and AI agents interact with our nearly 3,000 API operations. |
| [Introducing Agent Lee - a new interface to the Cloudflare stack](https://blog.cloudflare.com/introducing-agent-lee/)                   | Agent Lee is an in-dashboard agent that shifts Cloudflare’s interface from manual tab-switching to a single prompt. Using sandboxed TypeScript, it helps you troubleshoot and manage your stack as a grounded technical collaborator.                |
| [Introducing Flagship: feature flags built for the age of AI](https://blog.cloudflare.com/flagship/)                                    | Introducing Flagship, a native feature flag service built on Cloudflare’s global network to eliminate the latency of third-party providers. By using KV and Durable Objects, Flagship allows for sub-millisecond flag evaluation.                    |
| [Deploy Postgres and MySQL databases with PlanetScale + Workers](https://blog.cloudflare.com/deploy-planetscale-postgres-with-workers/) | Learn how to deploy PlanetScale Postgres and MySQL databases via Cloudflare and connect Cloudflare Workers.                                                                                                                                          |
| [Register domains wherever you build: Cloudflare Registrar API now in beta](https://blog.cloudflare.com/registrar-api-beta/)            | The Cloudflare Registrar API is now in beta. Developers and AI agents can search, check availability, and register domains at cost directly from their editor, their terminal, or their agent — without leaving their workflow.                      |

## Agentic Web

[ ](#agentic-web) 

As more agents come online, they're still browsing an Internet that was built for people. Existing websites need new tools to control what bots can access their content, package and present it for agents, and measure how ready they are for this shift.

| **Announcement**                                                                                                     | **Summary**                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Introducing the Agent Readiness score. Is your site agent-ready?](https://blog.cloudflare.com/agent-readiness/)     | The Agent Readiness score can help site owners understand how well their websites support AI agents. Here we explore new standards, share Radar data, and detail how we made Cloudflare’s docs the most agent-friendly on the web.                                                                       |
| [Redirects for AI Training enforces canonical content](https://blog.cloudflare.com/ai-redirects/)                    | Soft directives don’t stop crawlers from ingesting deprecated content. Redirects for AI Training allows anybody on Cloudflare to redirect verified crawlers to canonical pages with one toggle and no origin changes.                                                                                    |
| [Agents Week: Network performance update](https://blog.cloudflare.com/network-performance-agents-week/)              | By migrating our request handling layer to a Rust-based architecture called FL2, Cloudflare has increased its performance lead to 60% of the world’s top networks. We use real-user measurements and TCP connection trimeans to ensure our data reflects the actual experience of people on the Internet |
| [Shared dictionary compression that keeps up with the agentic web](https://blog.cloudflare.com/shared-dictionaries/) | We give you a sneak peek of our support for shared compression dictionaries, show you how it improves page load times, and reveal when you’ll be able to try the beta yourself.                                                                                                                          |

## That’s a wrap

[ ](#thats-a-wrap) 

Agents Week 2026 is ending, but the agentic cloud is just getting started. Everything we shipped this week — from compute and security to the agent toolbox and the agentic web — is the foundation. We're going to keep building on it to give you everything you need to build what's next.

We also have more blog posts coming out today and tomorrow to continue the story, so keep an eye out for the latest [at our blog](https://blog.cloudflare.com/).

If you're building on any of what we announced this week, we want to hear about it. Come find us on [X](https://x.com/cloudflaredev) or [Discord](https://discord.com/invite/cloudflaredev), or head to the [developer documentation](https://developers.cloudflare.com/products/?product-group=Developer+platform). 

Cloudflare's connectivity cloud protects [entire corporate networks](https://www.cloudflare.com/network-services/), helps customers build [Internet-scale applications efficiently](https://workers.cloudflare.com/), accelerates any [website or Internet application](https://www.cloudflare.com/performance/accelerate-internet-applications/), [wards off DDoS attacks](https://www.cloudflare.com/ddos/), keeps [hackers at bay](https://www.cloudflare.com/application-security/), and can help you on [your journey to Zero Trust](https://www.cloudflare.com/products/zero-trust/).  
  
Visit [1.1.1.1](https://one.one.one.one/) from any device to get started with our free app that makes your Internet faster and safer.  
  
To learn more about our mission to help build a better Internet, [start here](https://www.cloudflare.com/learning/what-is-cloudflare/). If you're looking for a new career direction, check out [our open positions](http://www.cloudflare.com/careers).

[Agents Week](https://blog.cloudflare.com/tag/agents-week/)[Agents](https://blog.cloudflare.com/tag/agents/)[AI](https://blog.cloudflare.com/tag/ai/)[Durable Objects](https://blog.cloudflare.com/tag/durable-objects/)[Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)[SDK](https://blog.cloudflare.com/tag/sdk/)[Browser Run](https://blog.cloudflare.com/tag/browser-run/)[Cloudflare Access](https://blog.cloudflare.com/tag/cloudflare-access/)[Browser Rendering](https://blog.cloudflare.com/tag/browser-rendering/)[MCP](https://blog.cloudflare.com/tag/mcp/)[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)[Developers](https://blog.cloudflare.com/tag/developers/)[Sandbox](https://blog.cloudflare.com/tag/sandbox/)[LLM](https://blog.cloudflare.com/tag/llm/)[Cloudflare Gateway](https://blog.cloudflare.com/tag/gateway/)[Workers AI](https://blog.cloudflare.com/tag/workers-ai/)[Product News](https://blog.cloudflare.com/tag/product-news/)[API](https://blog.cloudflare.com/tag/api/)

Follow on X

Ming Lu|[/minglu](https://x.com//minglu)

Anni Wang|[/aninibread](https://x.com//aninibread)

Cloudflare|[@cloudflare](https://x.com/@cloudflare)

Related posts

May 01, 2026

[Introducing Dynamic Workflows: durable execution that follows the tenant](https://blog.cloudflare.com/dynamic-workflows/)

Dynamic Workflows is a library that lets you route durable execution to tenant-provided code on the fly. Built on Dynamic Workers, it enables platforms to serve millions of unique workflows at near-zero idle cost....

By 
* [Dan Lapid](https://blog.cloudflare.com/author/dan-lapid/),
* [Luís Duarte](https://blog.cloudflare.com/author/luis-duarte/)

[Workflows,](https://blog.cloudflare.com/tag/workflows/) [Cloudflare Workers,](https://blog.cloudflare.com/tag/workers/) [Durable Execution,](https://blog.cloudflare.com/tag/durable-execution/) [Developer Platform,](https://blog.cloudflare.com/tag/developer-platform/) [Developers](https://blog.cloudflare.com/tag/developers/) 

April 30, 2026

[Agents can now create Cloudflare accounts, buy domains, and deploy](https://blog.cloudflare.com/agents-stripe-projects/)

Starting today, agents can now be Cloudflare customers. They can create a Cloudflare account, start a paid subscription, register a domain, and get back an API token to deploy code right away. Humans can be in the loop to grant permission, but there’s no need to go to the dashboard, copy and paste API tokens, or enter credit card details. ...

By 
* [Sid Chatterjee](https://blog.cloudflare.com/author/sid/),
* [Brendan Irvine-Broque](https://blog.cloudflare.com/author/brendan-irvine-broque/)

[Cloudflare Workers,](https://blog.cloudflare.com/tag/workers/) [Developer Platform,](https://blog.cloudflare.com/tag/developer-platform/) [Agents,](https://blog.cloudflare.com/tag/agents/) [Registrar,](https://blog.cloudflare.com/tag/registrar/) [AI](https://blog.cloudflare.com/tag/ai/) 

April 22, 2026

[Making Rust Workers reliable: panic and abort recovery in wasm‑bindgen](https://blog.cloudflare.com/making-rust-workers-reliable/)

Panics in Rust Workers were historically fatal, poisoning the entire instance. By collaborating upstream on the wasm‑bindgen project, Rust Workers now support resilient critical error recovery, including panic unwinding using WebAssembly Exception Handling....

By 
* [Guy Bedford](https://blog.cloudflare.com/author/guy-bedford/),
* [Hood Chatham](https://blog.cloudflare.com/author/hood/),
* [Logan Gatlin](https://blog.cloudflare.com/author/logan-gatlin/)

[Cloudflare Workers,](https://blog.cloudflare.com/tag/workers/) [Rust,](https://blog.cloudflare.com/tag/rust/) [Rust Workers,](https://blog.cloudflare.com/tag/rust-workers/) [WebAssembly,](https://blog.cloudflare.com/tag/webassembly/) [WASM,](https://blog.cloudflare.com/tag/wasm/) [Reliability,](https://blog.cloudflare.com/tag/reliability/) [Engineering,](https://blog.cloudflare.com/tag/engineering/) [Open Source,](https://blog.cloudflare.com/tag/open-source/) [Developer Platform,](https://blog.cloudflare.com/tag/developer-platform/) [Developers](https://blog.cloudflare.com/tag/developers/) 

April 21, 2026

[Moving past bots vs. humans](https://blog.cloudflare.com/past-bots-and-humans/)

As AI assistants and privacy proxies challenge the capabilities of traditional bot detection, the Web needs new models for accountability. We believe that control should remain with the client, and that an open ecosystem of anonymous credentials is key to preserving user privacy while protecting origins from abuse....

By 
* [Thibault Meunier](https://blog.cloudflare.com/author/thibault/)

[Research,](https://blog.cloudflare.com/tag/research/) [Bots,](https://blog.cloudflare.com/tag/bots/) [Privacy,](https://blog.cloudflare.com/tag/privacy/) [Standards,](https://blog.cloudflare.com/tag/standards/) [Better Internet,](https://blog.cloudflare.com/tag/better-internet/) [AI](https://blog.cloudflare.com/tag/ai/) 
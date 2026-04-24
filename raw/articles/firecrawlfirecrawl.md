# firecrawl/firecrawl

Source: https://github.com/firecrawl/firecrawl
Ingested: 2026-04-24
Type: documentation

---

# README

<h3 align="center">
  <a name="readme-top"></a>
  <img
    src="https://raw.githubusercontent.com/firecrawl/firecrawl/main/img/firecrawl_logo.png"
    height="200"
  >
</h3>

<div align="center">
  <a href="https://github.com/firecrawl/firecrawl/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/firecrawl/firecrawl" alt="License">
  </a>
  <a href="https://pepy.tech/project/firecrawl-py">
    <img src="https://static.pepy.tech/badge/firecrawl-py" alt="Downloads">
  </a>
  <a href="https://GitHub.com/firecrawl/firecrawl/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/firecrawl/firecrawl.svg" alt="GitHub Contributors">
  </a>
  <a href="https://firecrawl.dev">
    <img src="https://img.shields.io/badge/Visit-firecrawl.dev-orange" alt="Visit firecrawl.dev">
  </a>
</div>

<div>
  <p align="center">
    <a href="https://twitter.com/firecrawl">
      <img src="https://img.shields.io/badge/Follow%20on%20X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Follow on X" />
    </a>
    <a href="https://www.linkedin.com/company/104100957">
      <img src="https://img.shields.io/badge/Follow%20on%20LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Follow on LinkedIn" />
    </a>
    <a href="https://discord.gg/firecrawl">
      <img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join our Discord" />
    </a>
  </p>
</div>

---

# **🔥 Firecrawl**

**Power AI agents with clean web data.** The API to search, scrape, and interact with the web at scale. Open source and available as a [hosted service](https://firecrawl.dev/?ref=github).

_Pst. Hey, you, join our stargazers :)_

<a href="https://github.com/firecrawl/firecrawl">
  <img src="https://img.shields.io/github/stars/firecrawl/firecrawl.svg?style=social&label=Star&maxAge=2592000" alt="GitHub stars">
</a>

---

## Why Firecrawl?

- **Industry-leading reliability**: Covers 96% of the web, including JS-heavy pages — no proxy headaches, just clean data ([see benchmarks](https://www.firecrawl.dev/blog/the-worlds-best-web-data-api-v25))
- **Blazingly fast**: P95 latency of 3.4s across millions of pages, built for real-time agents and dynamic apps
- **LLM-ready output**: Clean markdown, structured JSON, screenshots, and more — spend fewer tokens, build better AI apps
- **We handle the hard stuff**: Rotating proxies, orchestration, rate limits, JS-blocked content, and more — zero configuration
- **Agent ready**: Connect Firecrawl to any AI agent or MCP client with a single command
- **Media parsing**: Parse and extract content from web-hosted PDFs, DOCX, and more
- **Actions**: Click, scroll, write, wait, and press before extracting content
- **Open source**: Developed transparently and collaboratively — [join our community](https://github.com/firecrawl/firecrawl)

---

## Feature Overview

**Core Endpoints**

| Feature | Description |
|---------|-------------|
| [**Search**](#search) | Search the web and get full page content from results |
| [**Scrape**](#scrape) | Convert any URL to markdown, HTML, screenshots, or structured JSON |
| [**Interact**](#interact) | Scrape a page, then interact with it using AI prompts or code |

**More**

| Feature | Description |
|---------|-------------|
| [**Agent**](#agent) | Automated data gathering, just describe what you need |
| [**Crawl**](#crawl) | Scrape all URLs of a website with a single request |
| [**Map**](#map) | Discover all URLs on a website instantly |
| [**Batch Scrape**](#batch-scrape) | Scrape thousands of URLs asynchronously |

---

## Quick Start

Sign up at [firecrawl.dev](https://firecrawl.dev) to get your API key. Try the [playground](https://firecrawl.dev/playground) to test it out.

### Search

Search the web and get full content from results.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

search_result = app.search("firecrawl", limit=5)
```

<details>
<summary><b>Node.js / cURL / CLI</b></summary>

**Node.js**
```javascript
import Firecrawl from '@mendable/firecrawl-js';

const app = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

app.search("firecrawl", { limit: 5 })
```

**cURL**
```bash
curl -X POST 'https://api.firecrawl.dev/v2/search' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
  "query": "firecrawl",
  "limit": 5
}'
```

**CLI**
```bash
firecrawl search "firecrawl" --limit 5
```
</details>

Output:
```json
[
  {
    "url": "https://firecrawl.dev",
    "title": "Firecrawl",
    "markdown": "Turn websites into..."
  },
  {
    "url": "https://docs.firecrawl.dev",
    "title": "Firecrawl Docs",
    "markdown": "# Getting Started..."
  }
]
```

### Scrape

Get LLM-ready data from any website — markdown, JSON, screenshots, and more.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

result = app.scrape('firecrawl.dev')
```

<details>
<summary><b>Node.js / cURL / CLI</b></summary>

**Node.js**
```javascript
import Firecrawl from '@mendable/firecrawl-js';

const app = new Firecrawl({ apiKey: "fc-YOUR_API_KEY" });

app.scrape('firecrawl.dev')
```

**cURL**
```bash
curl -X POST 'https://api.firecrawl.dev/v2/scrape' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
  "url": "firecrawl.dev"
}'
```

**CLI**
```bash
firecrawl scrape https://firecrawl.dev
firecrawl https://firecrawl.dev --only-main-content
```
</details>

Output:
```
# Firecrawl

Firecrawl helps AI systems search, scrape, and interact with the web.

## Features
- Search: Find information across the web
- Scrape: Clean data from any page
- Interact: Click, navigate, and operate pages
- Agent: Autonomous data gathering
```

### Interact

Scrape a page, then interact with it using AI prompts or code.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

result = app.scrape("https://amazon.com")
scrape_id = result.metadata.scrape_id

app.interact(scrape_id, prompt="Search for 'mechanical keyboard'")
app.interact(scrape_id, prompt="Click the first result")
```

<details>
<summary><b>Node.js / cURL / CLI</b></summary>

**Node.js**
```javascript
import Firecrawl from '@mendable/firecrawl-js';

const app = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

const result = await app.scrape("https://amazon.com");

await app.interact(result.metadata.scrapeId, {
  prompt: "Search for 'mechanical keyboard'"
});
await app.interact(result.metadata.scrapeId, {
  prompt: "Click the first result"
});
```

**cURL**
```bash
# 1. Scrape the page
curl -X POST 'https://api.firecrawl.dev/v2/scrape' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{"url": "https://amazon.com"}'

# 2. Interact with the page (use scrapeId from step 1)
curl -X POST 'https://api.firecrawl.dev/v2/scrape/SCRAPE_ID/interact' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{"prompt": "Search for mechanical keyboard"}'
```

**CLI**
```bash
firecrawl scrape https://amazon.com
firecrawl interact exec --prompt "Search for 'mechanical keyboard'"
firecrawl interact exec --prompt "Click the first result"
```
</details>

Output:
```json
{
  "success": true,
  "output": "Keyboard available at $100",
  "liveViewUrl": "https://liveview.firecrawl.dev/..."
}
```

---

## Power Your Agent

Connect Firecrawl to any AI agent or MCP client in minutes.

### Skill

Give your agent easy access to real-time web data with one command.

```bash
npx -y firecrawl-cli@latest init --all --browser
```

Restart your agent after installing. Works with [Claude Code](https://claude.ai/code), [Antigravity](https://antigravity.google), [OpenCode](https://opencode.ai), and more.

### MCP

Connect any MCP-compatible client to the web in seconds.

```json
{
  "mcpServers": {
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-YOUR_API_KEY"
      }
    }
  }
}
```

### Agent Onboarding

Are you an AI agent? Fetch this skill to sign up your user, get an API key, and start building with Firecrawl.

```bash
curl -s https://firecrawl.dev/agent-onboarding/SKILL.md
```

See the [Skill + CLI documentation](https://docs.firecrawl.dev/sdks/cli) for all available commands. For MCP, see [firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server).

---

## More Endpoints

### Agent

**The easiest way to get data from the web.** Describe what you need, and our AI agent searches, navigates, and retrieves it. No URLs required.

Agent is the evolution of our `/extract` endpoint: faster, more reliable, and doesn't require you to know the URLs upfront.
```bash
curl -X POST 'https://api.firecrawl.dev/v2/agent' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "prompt": "Find the pricing plans for Notion"
  }'
```

Response:
```json
{
  "success": true,
  "data": {
    "result": "Notion offers the following pricing plans:\n\n1. Free - $0/month...\n2. Plus - $10/seat/month...\n3. Business - $18/seat/month...",
    "sources": ["https://www.notion.so/pricing"]
  }
}
```

#### Agent with Structured Output

Use a schema to get structured data:
```python
from firecrawl import Firecrawl
from pydantic import BaseModel, Field
from typing import List, Optional

app = Firecrawl(api_key="fc-YOUR_API_KEY")

class Founder(BaseModel):
    name: str = Field(description="Full name of the founder")
    role: Optional[str] = Field(None, description="Role or position")

class FoundersSchema(BaseModel):
    founders: List[Founder] = Field(description="List of founders")

result = app.agent(
    prompt="Find the founders of Firecrawl",
    schema=FoundersSchema
)

print(result.data)
```
```json
{
  "founders": [
    {"name": "Eric Ciarla", "role": "Co-founder"},
    {"name": "Nicolas Camara", "role": "Co-founder"},
    {"name": "Caleb Peffer", "role": "Co-founder"}
  ]
}
```

#### Agent with URLs (Optional)

Focus the agent on specific pages:
```python
result = app.agent(
    urls=["https://docs.firecrawl.dev", "https://firecrawl.dev/pricing"],
    prompt="Compare the features and pricing information"
)
```

#### Model Selection

Choose between two models based on your needs:

| Model | Cost | Best For |
|-------|------|----------|
| `spark-1-mini` (default) | 60% cheaper | Most tasks |
| `spark-1-pro` | Standard | Complex research, critical data gathering |
```python
result = app.agent(
    prompt="Compare enterprise features across Firecrawl, Apify, and ScrapingBee",
    model="spark-1-pro"
)
```


**When to use Pro:**
- Comparing data across multiple websites
- Extracting from sites with complex navigation or auth
- Research tasks where the agent needs to explore multiple paths
- Critical data where accuracy is paramount

Learn more about Spark models in our [Agent documentation](https://docs.firecrawl.dev/features/agent).

### Crawl

Crawl an entire website and get content from all pages.
```bash
curl -X POST 'https://api.firecrawl.dev/v2/crawl' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "limit": 100,
    "scrapeOptions": {
      "formats": ["markdown"]
    }
  }'
```

Returns a job ID:
```json
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

#### Check Crawl Status
```bash
curl -X GET 'https://api.firecrawl.dev/v2/crawl/123-456-789' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY'
```
```json
{
  "status": "completed",
  "total": 50,
  "completed": 50,
  "creditsUsed": 50,
  "data": [
    {
      "markdown": "# Page Title\n\nContent...",
      "metadata": {"title": "Page Title", "sourceURL": "https://..."}
    }
  ]
}
```

**Note:** The [SDKs](#sdks) handle polling automatically for a better developer experience.

### Map

Discover all URLs on a website instantly.
```bash
curl -X POST 'https://api.firecrawl.dev/v2/map' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://firecrawl.dev"}'
```

Response:
```json
{
  "success": true,
  "links": [
    {"url": "https://firecrawl.dev", "title": "Firecrawl", "description": "Turn websites into LLM-ready data"},
    {"url": "https://firecrawl.dev/pricing", "title": "Pricing", "description": "Firecrawl pricing plans"},
    {"url": "https://firecrawl.dev/blog", "title": "Blog", "description": "Firecrawl blog"}
  ]
}
```

#### Map with Search

Find specific URLs within a site:
```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

result = app.map("https://firecrawl.dev", search="pricing")
# Returns URLs ordered by relevance to "pricing"
```

### Batch Scrape

Scrape multiple URLs at once:
```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

job = app.batch_scrape([
    "https://firecrawl.dev",
    "https://docs.firecrawl.dev",
    "https://firecrawl.dev/pricing"
], formats=["markdown"])

for doc in job.data:
    print(doc.metadata.source_url)
```

---

## SDKs

Our SDKs provide a convenient way to use all Firecrawl features and automatically handle polling for async operations.

### Python

Install the SDK:
```bash
pip install firecrawl-py
```
```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

# Scrape a single URL
doc = app.scrape("https://firecrawl.dev", formats=["markdown"])
print(doc.markdown)

# Use the Agent for autonomous data gathering
result = app.agent(prompt="Find the founders of Stripe")
print(result.data)

# Crawl a website (automatically waits for completion)
docs = app.crawl("https://docs.firecrawl.dev", limit=50)
for doc in docs.data:
    print(doc.metadata.source_url, doc.markdown[:100])

# Search the web
results = app.search("best AI data tools 2024", limit=10)
print(results)
```

### Node.js

Install the SDK:
```bash
npm install @mendable/firecrawl-js
```
```javascript
import Firecrawl from '@mendable/firecrawl-js';

const app = new Firecrawl({ apiKey: 'fc-YOUR_API_KEY' });

// Scrape a single URL
const doc = await app.scrape('https://firecrawl.dev', { formats: ['markdown'] });
console.log(doc.markdown);

// Use the Agent for autonomous data gathering
const result = await app.agent({ prompt: 'Find the founders of Stripe' });
console.log(result.data);

// Crawl a website (automatically waits for completion)
const docs = await app.crawl('https://docs.firecrawl.dev', { limit: 50 });
docs.data.forEach(doc => {
    console.log(doc.metadata.sourceURL, doc.markdown.substring(0, 100));
});

// Search the web
const results = await app.search('best AI data tools 2024', { limit: 10 });
results.data.web.forEach(result => {
    console.log(`${result.title}: ${result.url}`);
});
```

### Java

Add the dependency ([Gradle/Maven](https://docs.firecrawl.dev/sdks/java#installation)):
```groovy
repositories {
    mavenCentral()
    maven { url 'https://jitpack.io' }
}

dependencies {
    implementation 'com.github.firecrawl:firecrawl-java-sdk:2.0'
}
```
```java
import dev.firecrawl.client.FirecrawlClient;
import dev.firecrawl.model.*;

FirecrawlClient client = new FirecrawlClient(
    System.getenv("FIRECRAWL_API_KEY"), null, null
);

// Scrape a single URL
ScrapeParams scrapeParams = new ScrapeParams();
scrapeParams.setFormats(new String[]{"markdown"});
FirecrawlDocument doc = client.scrapeURL("https://firecrawl.dev", scrapeParams);
System.out.println(doc.getMarkdown());

// Use the Agent for autonomous data gathering
AgentParams agentParams = new AgentParams("Find the founders of Stripe");
AgentResponse start = client.createAgent(agentParams);
AgentStatusResponse result = client.getAgentStatus(start.getId());
System.out.println(result.getData());

// Crawl a website (polls until completion)
CrawlParams crawlParams = new CrawlParams();
crawlParams.setLimit(50);
CrawlStatusResponse job = client.crawlURL("https://docs.firecrawl.dev", crawlParams, null, 10);
for (FirecrawlDocument page : job.getData()) {
    System.out.println(page.getMetadata().get("sourceURL"));
}

// Search the web
SearchParams searchParams = new SearchParams("best AI data tools 2024");
searchParams.setLimit(10);
SearchResponse results = client.search(searchParams);
for (SearchResult r : results.getResults()) {
    System.out.println(r.getTitle() + ": " + r.getUrl());
}
```

### Elixir

Add the dependency:
```elixir
def deps do
  [
    {:firecrawl, "~> 1.0"}
  ]
end
```
```elixir
# Scrape a URL
{:ok, response} = Firecrawl.scrape_and_extract_from_url(
  url: "https://firecrawl.dev",
  formats: ["markdown"]
)

# Crawl a website
{:ok, response} = Firecrawl.crawl_urls(
  url: "https://docs.firecrawl.dev",
  limit: 50
)

# Search the web
{:ok, response} = Firecrawl.search_and_scrape(
  query: "best AI data tools 2024",
  limit: 10
)

# Map URLs
{:ok, response} = Firecrawl.map_urls(url: "https://example.com")
```

### Rust

Add the dependency:
```toml
[dependencies]
firecrawl = "2"
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
```
```rust
use firecrawl::{Client, ScrapeOptions, Format, CrawlOptions};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("fc-YOUR_API_KEY")?;

    // Scrape a URL
    let document = client.scrape("https://firecrawl.dev", None).await?;
    println!("{:?}", document.markdown);

    // Crawl a website
    let options = CrawlOptions {
        limit: Some(50),
        ..Default::default()
    };
    let result = client.crawl("https://docs.firecrawl.dev", options).await?;
    println!("Crawled {} pages", result.data.len());

    // Search the web
    let response = client.search("best web scraping tools 2024", None).await?;
    println!("{:?}", response.data);

    Ok(())
}
```

### Community SDKs

- [Go SDK](https://github.com/firecrawl/firecrawl/tree/main/apps/go-sdk)

---

## Integrations

**Agents & AI Tools**
- [Firecrawl Skill](https://docs.firecrawl.dev/sdks/cli)
- [Firecrawl MCP](https://github.com/mendableai/firecrawl-mcp-server)

**Platforms**
- [Lovable](https://docs.lovable.dev/integrations/firecrawl)
- [Zapier](https://zapier.com/apps/firecrawl/integrations)
- [n8n](https://n8n.io/integrations/firecrawl/)

[View all integrations →](https://www.firecrawl.dev/integrations)

**Missing your favorite tool?** [Open an issue](https://github.com/mendableai/firecrawl/issues) and let us know!

---

## Resources

- [Documentation](https://docs.firecrawl.dev)
- [API Reference](https://docs.firecrawl.dev/api-reference/introduction)
- [Playground](https://firecrawl.dev/playground)
- [Changelog](https://firecrawl.dev/changelog)

---

## Open Source vs Cloud

Firecrawl is open source under the AGPL-3.0 license. The cloud version at [firecrawl.dev](https://firecrawl.dev) includes additional features:

![Open Source vs Cloud](https://raw.githubusercontent.com/firecrawl/firecrawl/main/img/open-source-cloud.png)

To run locally, see the [Contributing Guide](https://github.com/firecrawl/firecrawl/blob/main/CONTRIBUTING.md). To self-host, see [Self-Hosting Guide](https://docs.firecrawl.dev/contributing/self-host).

---

## Contributing

We love contributions! Please read our [Contributing Guide](https://github.com/firecrawl/firecrawl/blob/main/CONTRIBUTING.md) before submitting a pull request.

### Contributors

<a href="https://github.com/firecrawl/firecrawl/graphs/contributors">
  <img alt="contributors" src="https://contrib.rocks/image?repo=firecrawl/firecrawl"/>
</a>

---

## License

This project is primarily licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). The SDKs and some UI components are licensed under the MIT License. See the LICENSE files in specific directories for details.

---

**It is the sole responsibility of end users to respect websites' policies when scraping.** Users are advised to adhere to applicable privacy policies and terms of use. By default, Firecrawl respects robots.txt directives. By using Firecrawl, you agree to comply with these conditions.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
  <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
    ↑ Back to Top ↑
  </a>
</p>



> **Deep fetch: 30 key files fetched beyond README.**



---

# FILE: CLAUDE.md

Firecrawl is a web scraper API. The directory you have access to is a monorepo:
 - `apps/api` has the actual API and worker code
 - `apps/*-sdk` are various SDKs

When making changes to the API, here are the general steps you should take:
1. Write some end-to-end tests that assert your win conditions, if they don't already exist
  - 1 happy path (more is encouraged if there are multiple happy paths with significantly different code paths taken)
  - 1+ failure path(s)
  - Generally, E2E (called `snips` in the API) is always preferred over unit testing.
  - In the API, always use `scrapeTimeout` from `./lib` to set the timeout you use for scrapes.
  - These tests will be ran on a variety of configurations. You should gate tests in the following manner:
    - If it requires fire-engine: `!process.env.TEST_SUITE_SELF_HOSTED`
    - If it requires AI: `!process.env.TEST_SUITE_SELF_HOSTED || process.env.OPENAI_API_KEY || process.env.OLLAMA_BASE_URL`
2. Write code to achieve your win conditions
3. Run your tests using `pnpm harness jest ...`
  - `pnpm harness` is a command that gets the API server and workers up for you to run the tests. Don't try to `pnpm start` manually.
  - The full test suite takes a long time to run, so you should try to only execute the relevant tests locally, and let CI run the full test suite.
4. Push to a branch, open a PR, and let CI run to verify your win condition.
Keep these steps in mind while building your TODO list.


---

# FILE: CONTRIBUTING.md

# Contributors guide:

Welcome to [Firecrawl](https://firecrawl.dev) 🔥! Here are some instructions on how to get the project locally, so you can run it on your own (and contribute)

If you're contributing, note that the process is similar to other open source repos i.e. (fork firecrawl, make changes, run tests, PR). If you have any questions, and would like help getting on board, reach out to help@firecrawl.com for more or submit an issue!

## Running the project locally

First, start by installing dependencies:

1. node.js [instructions](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)
2. rust [instructions](https://www.rust-lang.org/tools/install)
3. pnpm [instructions](https://pnpm.io/installation)
4. redis [instructions](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)
5. postgresql
6. Docker (optional) (for running postgres)

You need to set up the PostgreSQL database by running the SQL file at `apps/nuq-postgres/nuq.sql`. Easiest way is to use the docker image inside `apps/nuq-postgres`. With Docker running, build the image:

```bash
docker build -t nuq-postgres .
```

and then run:

```bash
docker run --name nuqdb \          
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  -v nuq-data:/var/lib/postgresql/data \
  -d nuq-postgres
```

Set environment variables in a .env in the /apps/api/ directory you can copy over the template in .env.example.

To start, we won't set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features)

.env:

```
# ===== Required ENVS ======
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0
REDIS_URL=redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379

## To turn on DB authentication, you need to set up supabase.
USE_DB_AUTHENTICATION=false

## Using the PostgreSQL for queuing -- change if credentials, host, or DB is different
NUQ_DATABASE_URL=postgres://postgres:postgres@localhost:5433/postgres

# ===== Optional ENVS ======

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
SUPABASE_ANON_TOKEN=
SUPABASE_URL=
SUPABASE_SERVICE_TOKEN=

# Other Optionals
TEST_API_KEY= # use if you've set up authentication and want to test with a real API key
OPENAI_API_KEY= # add for LLM dependent features (image alt generation, etc.)
BULL_AUTH_KEY= @
PLAYWRIGHT_MICROSERVICE_URL=  # set if you'd like to run a playwright fallback
LLAMAPARSE_API_KEY= #Set if you have a llamaparse key you'd like to use to parse pdfs
SLACK_WEBHOOK_URL= # set if you'd like to send slack server health status messages


```

### Installing dependencies

First, install the dependencies using pnpm.

```bash
# cd apps/api # to make sure you're in the right folder
pnpm install # make sure you have pnpm version 9+!
```

### Running the project

You're going to need to open 3 terminals.

### Terminal 1 - setting up redis

Run the command anywhere within your project

```bash
redis-server
```

### Terminal 2 - setting up the service

Now, navigate to the apps/api/ directory and run:

```bash
pnpm start
# if you are going to use the [llm-extract feature](https://github.com/firecrawl/firecrawl/pull/586/), you should also export OPENAI_API_KEY=sk-______
```

This will start the workers who are responsible for processing crawl jobs.

### Terminal 3 - sending our first request.

Alright: now let’s send our first request.

```curl
curl -X GET http://localhost:3002/test
```

This should return the response Hello, world!

If you’d like to test the crawl endpoint, you can run this

```curl
curl -X POST http://localhost:3002/v1/crawl \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://mendable.ai"
    }'
```

### Alternative: Using Docker Compose

For a simpler setup, you can use Docker Compose to run all services:

1. Prerequisites: Make sure you have Docker and Docker Compose installed
2. Copy the `.env.example` file to `.env` in the `/apps/api/` directory and configure as needed
3. From the root directory, run:

```bash
docker compose up
```

This will start Redis, the API server, and workers automatically in the correct configuration.

## Tests:

The best way to do this is run the test with `npm run test:snips`.



---

# FILE: SELF_HOST.md

# Self-hosting Firecrawl

#### Contributor?

Welcome to [Firecrawl](https://firecrawl.dev) 🔥! Here are some instructions on how to get the project locally so you can run it on your own and contribute.

If you're contributing, note that the process is similar to other open-source repos, i.e., fork Firecrawl, make changes, run tests, PR.

If you have any questions or would like help getting on board, join our Discord community [here](https://discord.gg/firecrawl) for more information or submit an issue on Github [here](https://github.com/firecrawl/firecrawl/issues/new/choose)!

## Why?

Self-hosting Firecrawl is particularly beneficial for organizations with stringent security policies that require data to remain within controlled environments. Here are some key reasons to consider self-hosting:

- **Enhanced Security and Compliance:** By self-hosting, you ensure that all data handling and processing complies with internal and external regulations, keeping sensitive information within your secure infrastructure. Note that Firecrawl is a Mendable product and relies on SOC2 Type2 certification, which means that the platform adheres to high industry standards for managing data security.
- **Customizable Services:** Self-hosting allows you to tailor the services, such as the Playwright service, to meet specific needs or handle particular use cases that may not be supported by the standard cloud offering.
- **Learning and Community Contribution:** By setting up and maintaining your own instance, you gain a deeper understanding of how Firecrawl works, which can also lead to more meaningful contributions to the project.

### Considerations

However, there are some limitations and additional responsibilities to be aware of:

1. **Limited Access to Fire-engine:** Currently, self-hosted instances of Firecrawl do not have access to Fire-engine, which includes advanced features for handling IP blocks, robot detection mechanisms, and more. This means that while you can manage basic scraping tasks, more complex scenarios might require additional configuration or might not be supported.
2. **Manual Configuration Required:** If you need to use scraping methods beyond the basic fetch and Playwright options, you will need to manually configure these in the `.env` file. This requires a deeper understanding of the technologies and might involve more setup time.

Self-hosting Firecrawl is ideal for those who need full control over their scraping and data processing environments but comes with the trade-off of additional maintenance and configuration efforts.

## Steps

1. First, start by installing the dependencies

- Docker [instructions](https://docs.docker.com/get-docker/)


2. Set environment variables

Create an `.env` in the root directory using the template below.

`.env:`
```
# ===== Required ENVS ======
PORT=3002
HOST=0.0.0.0

# Note: PORT is used by both the main API server and worker liveness check endpoint

# To turn on DB authentication, you need to set up Supabase.
USE_DB_AUTHENTICATION=false

# ===== Optional ENVS ======

## === AI features (JSON format on scrape, /extract API) ===
# Provide your OpenAI API key here to enable AI features
# OPENAI_API_KEY=

# Experimental: Use Ollama
# OLLAMA_BASE_URL=http://localhost:11434/api
# MODEL_NAME=deepseek-r1:7b
# MODEL_EMBEDDING_NAME=nomic-embed-text

# Experimental: Use any OpenAI-compatible API
# OPENAI_BASE_URL=https://example.com/v1
# OPENAI_API_KEY=

## === Proxy ===
# PROXY_SERVER can be a full URL (e.g. http://0.1.2.3:1234) or just an IP and port combo (e.g. 0.1.2.3:1234)
# Do not uncomment PROXY_USERNAME and PROXY_PASSWORD if your proxy is unauthenticated
# PROXY_SERVER=
# PROXY_USERNAME=
# PROXY_PASSWORD=

## === /search API ===
# By default, the /search API will use Google search.

# You can specify a SearXNG server with the JSON format enabled, if you'd like to use that instead of direct Google.
# You can also customize the engines and categories parameters, but the defaults should also work just fine.
# SEARXNG_ENDPOINT=http://your.searxng.server
# SEARXNG_ENGINES=
# SEARXNG_CATEGORIES=

## === Other ===

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=

# Use if you've set up authentication and want to test with a real API key
# TEST_API_KEY=

# This key lets you access the queue admin panel. Change this if your deployment is publicly accessible.
BULL_AUTH_KEY=CHANGEME

# This is now autoconfigured by the docker-compose.yaml. You shouldn't need to set it.
# PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/scrape
# REDIS_URL=redis://redis:6379
# REDIS_RATE_LIMIT_URL=redis://redis:6379

## === PostgreSQL Database Configuration ===
# Configure PostgreSQL credentials. These should match the credentials used by the nuq-postgres container.
# If you change these, ensure all three are set consistently.
# POSTGRES_USER=firecrawl
# POSTGRES_PASSWORD=firecrawl_password
# POSTGRES_DB=firecrawl

# Set if you have a llamaparse key you'd like to use to parse pdfs
# LLAMAPARSE_API_KEY=

# Set if you'd like to send server health status messages to Slack
# SLACK_WEBHOOK_URL=

## === System Resource Configuration ===
# Maximum CPU usage threshold (0.0-1.0). Worker will reject new jobs when CPU usage exceeds this value.
# Default: 0.8 (80%)
# MAX_CPU=0.8

# Maximum RAM usage threshold (0.0-1.0). Worker will reject new jobs when memory usage exceeds this value.
# Default: 0.8 (80%)
# MAX_RAM=0.8

# Set if you'd like to allow local webhooks to be sent to your self-hosted instance
# ALLOW_LOCAL_WEBHOOKS=true
```

### Security considerations

- **Use strong PostgreSQL credentials.** The defaults in the `.env` template are for local development only. When deploying to a server, set `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` to secure values and ensure they match the database service configuration.
- **Keep the database port internal.** The provided `docker-compose.yaml` does not expose PostgreSQL to the host or the internet. Avoid adding a `ports` mapping for `nuq-postgres` unless you are restricting access with a firewall. To access the database for maintenance, prefer using `docker compose exec nuq-postgres psql` or a temporary, firewalled tunnel.
- **Protect the admin UI.** Set `BULL_AUTH_KEY` to a strong secret, especially on any deployment reachable from untrusted networks.

3.  Build and run the Docker containers:

    ```bash
    docker compose build
    docker compose up
    ```

    If you encounter an error, make sure you're using `docker compose` and not `docker-compose`.
    
    This will run a local instance of Firecrawl which can be accessed at `http://localhost:3002`.
    
    You should be able to see the Bull Queue Manager UI on `http://localhost:3002/admin/CHANGEME/queues`.

5. *(Optional)* Test the API

If you’d like to test the crawl endpoint, you can run this:

  ```bash
  curl -X POST http://localhost:3002/v1/crawl \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://firecrawl.dev"
      }'
  ```   

## Troubleshooting

This section provides solutions to common issues you might encounter while setting up or running your self-hosted instance of Firecrawl.

### API Keys for SDK Usage

**Note:** When using Firecrawl SDKs with a self-hosted instance, API keys are optional. API keys are only required when connecting to the cloud service (api.firecrawl.dev).

### Supabase client is not configured

**Symptom:**
```bash
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Attempted to access Supabase client when it's not configured.
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Error inserting scrape event: Error: Supabase client is not configured.
```

**Explanation:**
This error occurs because the Supabase client setup is not completed. You should be able to scrape and crawl with no problems. Right now it's not possible to configure Supabase in self-hosted instances.

### You're bypassing authentication

**Symptom:**
```bash
[YYYY-MM-DDTHH:MM:SS.SSSz]WARN - You're bypassing authentication
```

**Explanation:**
This error occurs because the Supabase client setup is not completed. You should be able to scrape and crawl with no problems. Right now it's not possible to configure Supabase in self-hosted instances.

### Docker containers fail to start

**Symptom:**
Docker containers exit unexpectedly or fail to start.

**Solution:**
Check the Docker logs for any error messages using the command:
```bash
docker logs [container_name]
```

- Ensure all required environment variables are set correctly in the .env file.
- Verify that all Docker services defined in docker-compose.yml are correctly configured and the necessary images are available.

### Connection issues with Redis

**Symptom:**
Errors related to connecting to Redis, such as timeouts or "Connection refused".

**Solution:**
- Ensure that the Redis service is up and running in your Docker environment.
- Verify that the REDIS_URL and REDIS_RATE_LIMIT_URL in your .env file point to the correct Redis instance, ensure that it points to the same URL in the `docker-compose.yaml` file (`redis://redis:6379`)
- Check network settings and firewall rules that may block the connection to the Redis port.

### API endpoint does not respond

**Symptom:**
API requests to the Firecrawl instance timeout or return no response.

**Solution:**
- Ensure that the Firecrawl service is running by checking the Docker container status.
- Verify that the PORT and HOST settings in your .env file are correct and that no other service is using the same port.
- Check the network configuration to ensure that the host is accessible from the client making the API request.

By addressing these common issues, you can ensure a smoother setup and operation of your self-hosted Firecrawl instance.

## Install Firecrawl on a Kubernetes Cluster (Simple Version)

Read the [examples/kubernetes/cluster-install/README.md](https://github.com/firecrawl/firecrawl/blob/main/examples/kubernetes/cluster-install/README.md) for instructions on how to install Firecrawl on a Kubernetes Cluster.

## Install Firecrawl on a Kubernetes Cluster with Helm

Read the [examples/kubernetes/firecrawl-helm/README.md](https://github.com/firecrawl/firecrawl/blob/main/examples/kubernetes/firecrawl-helm/README.md) for instructions on how to install Firecrawl on a Kubernetes Cluster with Helm.



---

# FILE: apps/api/src/__tests__/snips/mocks/map-query-params.json




---

# FILE: apps/api/src/__tests__/snips/mocks/mocking-works-properly.json

[
    {
        "time": 1735911273239,
        "options": {
            "url": "<fire-engine>/scrape",
            "method": "POST",
            "body": {
                "url": "http://firecrawl.dev",
                "engine": "chrome-cdp",
                "instantReturn": true,
                "skipTlsVerification": false,
                "priority": 10,
                "mobile": false,
                "timeout": 15000
            },
            "headers": {},
            "ignoreResponse": false,
            "ignoreFailure": false,
            "tryCount": 3
        },
        "result": {
            "status": 200,
            "headers": {},
            "body": "{\"jobId\":\"ede37286-90db-4f60-8efb-76217dfcfa35!chrome-cdp\",\"processing\":true}"
        }
    },
    {
        "time": 1735911273354,
        "options": {
            "url": "<fire-engine>/scrape/ede37286-90db-4f60-8efb-76217dfcfa35!chrome-cdp",
            "method": "GET",
            "headers": {},
            "ignoreResponse": false,
            "ignoreFailure": false,
            "tryCount": 1
        },
        "result": {
            "status": 200,
            "headers": {},
            "body": "{\"jobId\":\"ede37286-90db-4f60-8efb-76217dfcfa35\",\"state\":\"prioritized\",\"processing\":true}"
        }
    },
    {
        "time": 1735911273720,
        "options": {
            "url": "<fire-engine>/scrape/ede37286-90db-4f60-8efb-76217dfcfa35!chrome-cdp",
            "method": "GET",
            "headers": {},
            "ignoreResponse": false,
            "ignoreFailure": false,
            "tryCount": 1
        },
        "result": {
            "status": 200,
            "headers": {},
            "body": "{\"jobId\":\"ede37286-90db-4f60-8efb-76217dfcfa35\",\"state\":\"active\",\"processing\":true}"
        }
    },
    {
        "time": 1735911274092,
        "options": {
            "url": "<fire-engine>/scrape/ede37286-90db-4f60-8efb-76217dfcfa35!chrome-cdp",
            "method": "GET",
            "headers": {},
            "ignoreResponse": false,
            "ignoreFailure": false,
            "tryCount": 1
        },
        "result": {
            "status": 200,
            "headers": {},
            "body": "{\"jobId\":\"ede37286-90db-4f60-8efb-76217dfcfa35\",\"state\":\"active\",\"processing\":true}"
        }
    },
    {
        "time": 1735911274467,
        "options": {
            "url": "<fire-engine>/scrape/ede37286-90db-4f60-8efb-76217dfcfa35!chrome-cdp",
            "method": "GET",
            "headers": {},
            "ignoreResponse": false,
            "ignoreFailure": false,
            "tryCount": 1
        },
        "result": {
            "status": 200,
            "headers": {},
            "body": "{\"jobId\":\"ede37286-90db-4f60-8efb-76217dfcfa35\",\"state\":\"active\",\"processing\":true}"
        }
    },
    {
        "time": 1735911274947,
        "options": {
            "url": "<fire-engine>/scrape/ede37286-90db-4f60-8efb-76217dfcfa35!chrome-cdp",
            "method": "GET",
            "headers": {},
            "ignoreResponse": false,
            "ignoreFailure": false,
            "tryCount": 1
        },
        "result": {
            "status": 200,
            "headers": {},
            "body": "{\"jobId\":\"ede37286-90db-4f60-8efb-76217dfcfa35\",\"state\":\"completed\",\"processing\":false,\"timeTaken\":1.204,\"content\":\"<!DOCTYPE html><html lang=\\\"en\\\"><body><p>this is fake data coming from the mocking system!</p></body></html>\",\"url\":\"https://www.firecrawl.dev/\",\"screenshots\":[],\"actionContent\":[],\"pageStatusCode\":200,\"responseHeaders\":{\"X-DNS-Prefetch-Control\":\"off\",\"age\":\"0\",\"cache-control\":\"private, no-cache, no-store, max-age=0, must-revalidate\",\"content-encoding\":\"br\",\"content-type\":\"text/html; charset=utf-8\",\"date\":\"Fri, 03 Jan 2025 13:34:34 GMT\",\"link\":\"</_next/static/media/171883e03d2067b6-s.p.woff2>; rel=preload; as=\\\"font\\\"; crossorigin=\\\"\\\"; type=\\\"font/woff2\\\", </_next/static/media/a34f9d1faa5f3315-s.p.woff2>; rel=preload; as=\\\"font\\\"; crossorigin=\\\"\\\"; type=\\\"font/woff2\\\", </_next/static/media/c4c7b0ec92b72e30-s.p.woff2>; rel=preload; as=\\\"font\\\"; crossorigin=\\\"\\\"; type=\\\"font/woff2\\\"\",\"permissions-policy\":\"keyboard-map=(), attribution-reporting=(), run-ad-auction=(), private-state-token-redemption=(), private-state-token-issuance=(), join-ad-interest-group=(), idle-detection=(), compute-pressure=(), browsing-topics=()\",\"server\":\"Vercel\",\"strict-transport-security\":\"max-age=63072000\",\"vary\":\"RSC, Next-Router-State-Tree, Next-Router-Prefetch\",\"x-matched-path\":\"/\",\"x-powered-by\":\"Next.js\",\"x-vercel-cache\":\"MISS\",\"x-vercel-id\":\"iad1::iad1::bs88l-1735911273932-1f7bba7a8b45\"},\"invalidTlsCert\":false,\"file\":null}"
        }
    }
]


---

# FILE: apps/api/src/scraper/WebScraper/utils/ENGINE_FORCING.md

# Engine Forcing

This feature allows you to force specific scraping engines for certain domains based on URL patterns. This is useful when you know that certain websites work better with specific engines.

## Configuration

The engine forcing is configured via the `FORCED_ENGINE_DOMAINS` environment variable. This should be a JSON object mapping domain patterns to engines.

### Environment Variable Format

```json
{
  "example.com": "playwright",
  "test.com": "fetch",
  "*.subdomain.com": "fire-engine;chrome-cdp",
  "google.com": ["fire-engine;chrome-cdp", "playwright"]
}
```

### Supported Patterns

1. **Exact domain match**: `"example.com"` matches `example.com` and all its subdomains (`www.example.com`, `api.example.com`, etc.)
2. **Wildcard pattern**: `"*.subdomain.com"` matches only subdomains of `subdomain.com` (e.g., `api.subdomain.com`, `www.subdomain.com`) but NOT the base domain itself
3. **Single engine**: `"playwright"` forces a single engine
4. **Multiple engines**: `["fire-engine;chrome-cdp", "playwright"]` provides a fallback list of engines to try in order

### Available Engines

- `fire-engine;chrome-cdp` - Advanced browser with Chrome DevTools Protocol
- `fire-engine;tlsclient` - TLS fingerprinting for anti-bot bypass
- `fire-engine;chrome-cdp;stealth` - Chrome CDP with stealth mode
- `fire-engine;tlsclient;stealth` - TLS client with stealth mode
- `playwright` - Direct Playwright integration
- `fetch` - Simple HTTP requests
- `pdf` - PDF document parsing
- `document` - Office document handling

## How It Works

1. When a scrape request is made, the system checks if the URL matches any domain pattern in `FORCED_ENGINE_DOMAINS`
2. If a match is found, the specified engine(s) are used instead of the default engine selection logic
3. If no match is found, the normal engine selection waterfall is used
4. The engine forcing only applies if `forceEngine` is not already set in the internal options

## Example Configuration

### Example 1: Force Playwright for specific domains

```bash
export FORCED_ENGINE_DOMAINS='{"linkedin.com":"playwright","twitter.com":"playwright"}'
```

This forces Playwright for LinkedIn and Twitter URLs.

### Example 2: Use fetch for simple sites

```bash
export FORCED_ENGINE_DOMAINS='{"example.com":"fetch","httpbin.org":"fetch"}'
```

This uses the simple fetch engine for example.com and httpbin.org.

### Example 3: Complex configuration with wildcards

```bash
export FORCED_ENGINE_DOMAINS='{
  "google.com": ["fire-engine;chrome-cdp", "playwright"],
  "*.cloudflare.com": "fire-engine;tlsclient;stealth",
  "wikipedia.org": "fetch"
}'
```

This configuration:

- Uses fire-engine with Chrome CDP for Google, falling back to Playwright if needed
- Uses fire-engine with TLS client in stealth mode for Cloudflare subdomains
- Uses simple fetch for Wikipedia

## Implementation Details

The engine forcing logic is implemented in:

- `apps/api/src/scraper/WebScraper/utils/engine-forcing.ts` - Core logic
- `apps/api/src/scraper/scrapeURL/index.ts` - Integration into scraping pipeline

The system is initialized at startup in:

- `apps/api/src/index.ts` - Main API server
- `apps/api/src/services/queue-worker.ts` - Queue worker
- `apps/api/src/services/extract-worker.ts` - Extract worker
- `apps/api/src/services/worker/nuq-worker.ts` - NuQ worker

## Precedence

The engine forcing has the following precedence:

1. If `forceEngine` is already set in `InternalOptions`, it takes precedence (engine forcing is skipped)
2. If a URL matches an engine forcing pattern, that engine is used
3. Otherwise, the normal engine selection waterfall is used

## Testing

Unit tests are available in `apps/api/src/scraper/WebScraper/utils/__tests__/engine-forcing.test.ts`.

## Notes

- Domain matching is case-insensitive
- The system handles invalid URLs gracefully by returning `undefined`
- If the JSON in `FORCED_ENGINE_DOMAINS` is invalid, the system logs an error and continues with empty mappings
- The feature is similar to the blocked domains logic but for engine selection instead of blocking



---

# FILE: apps/api/src/scraper/scrapeURL/README.md

# `scrapeURL`
New URL scraper for Firecrawl

## Signal flow
```mermaid
flowchart TD;
    scrapeURL-.->buildFallbackList;
    buildFallbackList-.->scrapeURLWithEngine;
    scrapeURLWithEngine-.->parseMarkdown;
    parseMarkdown-.->wasScrapeSuccessful{{Was scrape successful?}};
    wasScrapeSuccessful-."No".->areEnginesLeft{{Are there engines left to try?}};
    areEnginesLeft-."Yes, try next engine".->scrapeURLWithEngine;
    areEnginesLeft-."No".->NoEnginesLeftError[/NoEnginesLeftError/]
    wasScrapeSuccessful-."Yes".->asd;
```

## Differences from `WebScraperDataProvider`
 - The job of `WebScraperDataProvider.validateInitialUrl` has been delegated to the zod layer above `scrapeUrl`.
 - `WebScraperDataProvider.mode` has no equivalent, only `scrape_url` is supported.
 - You may no longer specify multiple URLs.
 - Built on `v1` definitons, instead of `v0`.
 - PDFs are now converted straight to markdown using LlamaParse, instead of converting to just plaintext.
 - DOCXs are now converted straight to HTML (and then later to markdown) using mammoth, instead of converting to just plaintext.
 - Using new JSON Schema OpenAI API -- schema fails with LLM Extract will be basically non-existant.
        


---

# FILE: apps/test-site/src/content/blog/firecrawl-v2-series-a-announcement.md

---
title: "We just raised our Series A and shipped /v2"
description: "How we got here. What we're building. Why the web's knowledge should be on tap for AI."
pubDate: "Aug 19, 2025"
heroImage: "../../assets/blog/series-a.webp"
category: "updates"
---

Firecrawl just raised a $14.5M Series A led by Nexus Venture Partners.

We’re putting the web’s knowledge on tap for AI, with more than 350,000 developers already signed up, our open source project crossing 48k stars on GitHub, and companies like Zapier, Shopify, and Replit using us to power their apps.

We’ve grown 15x in the past year and this is just the beginning.

## How we got here

It’s been 16 months since we started Firecrawl.

The journey actually began with Mendable, our AI chat solution for documentation, which teams at Snapchat, MongoDB, and DoorDash adopted quickly. But we kept hitting the same wall, finding that getting clean, structured web data for AI was unnecessarily hard.

Every AI app was rebuilding the same infrastructure, including scraping websites, extracting structured data, handling JavaScript, dealing with rate limits, and parsing messy HTML, with thousands of developers solving the same problem differently.

We realized the real opportunity was upstream, to build the infrastructure once, make it perfect, and give AI universal access to the world’s information through a simple API.

That bet paid off brilliantly. Zapier recently integrated Firecrawl in a single afternoon, and their chatbots now ingest customer websites automatically, answering FAQs and capturing leads within minutes. Replit uses us for documentation ingestion, while top hedge funds rely on us for market analysis.

The variety tells the story, from lead enrichment tools and competitive intelligence systems to price monitoring and research agents, they all need the same thing, reliable web data at scale.

## Why we exist

The web holds nearly everything humans know, serving as the most complete, real-time record of our knowledge.

But this knowledge is trapped, scattered across millions of domains, locked behind JavaScript, and constantly changing. AI needs this data to be useful, to answer questions accurately, to take actions confidently, and to understand the world as it exists right now.

Firecrawl exists to make web data programmable through our full toolkit that covers web search and extraction, giving developers exactly what they need, in the exact format they want.

We’re building the missing layer between AI and the web.

## Where we’re going

You can expect our team to spend even more time in three areas.

**1. Infrastructure**
Our proprietary Fire-Engine technology already delivers 33% faster speeds and 40% higher success rates than existing solutions, and now we’re scaling it worldwide for sub-second response times for everyone, everywhere.
We’re investing in reliability, uptime, and performance because as we exponentially grow, your data extraction needs to work every single time.

**2. Product**
We just shipped v2 with 10x faster scraping through intelligent caching, semantic crawling where you describe what you want in plain English, a new summary format that extracts insights instantly, and search that supports news and images on demand.
In the coming months, expect features that fundamentally change how AI and builders interact with the web, including smarter extraction, batch data gathering, and change monitoring.

**3. Sustainable partnerships**
We’re building a future where publishers get paid when AI uses their content, because the web needs a sustainable model for high-quality content. When paywalled content powers AI, creators should benefit directly.
This isn’t just about technology, it’s about building the right incentives. Publishers create valuable content, AI needs that content, and we’re building the marketplace that connects them fairly.

## Who is investing

We’re thrilled to welcome new investors.

- Nexus Venture Partners, which has backed companies like Postman, Hasura, and Druva, with special thanks to Abhishek for believing in our vision.
- Y Combinator is expanding their initial investment.
- Zapier, one of our favorite customers, is joining the round.
- Tobias Lütke, CEO of Shopify
- Abhinav Asthana, CEO of Postman
- Matt McClure, Founder of Mux

We’re also lucky to have the backing of some amazing angels and funds, including both long-time friends and new supporters.

Abhishek from Nexus said it perfectly when he noted that “Clean, comprehensive web data is crucial for the next wave of AI. Firecrawl’s developer-first platform delivers it simply, reliably, and at scale.”

## Get started

Thanks to every single one of you for being part of this journey.

- Start using v2 today at [firecrawl.dev](https://firecrawl.dev)
- See what we’re open sourcing at [github.com/firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
- Join our team at [firecrawl.dev/careers](https://firecrawl.dev/careers)

We’re hiring engineers who understand distributed systems at scale, AI specialists who know what agents need, and developer advocates who can teach and inspire.

If you believe AI needs access to the world’s information, if you think publishers deserve fair compensation, if you want to build infrastructure that powers the next generation of AI, we want to talk to you.

The web’s knowledge should be on tap for everyone building with AI, so come help us make it happen.



---

# FILE: apps/test-site/src/content/blog/introducing-firecrawl-templates.md

---
title: "Introducing Templates: Ready to use Firecrawl examples"
description: "A library of reusable playground setups, code snippets, and repos to help you quickly implement Firecrawl for any use case."
pubDate: "May 13, 2025"
heroImage: "../../assets/blog/templateslaunch.webp"
category: "updates"
---

Today we’re launching **Templates** – making it super easy to discover, share, and reuse Firecrawl examples. Our community has built so many amazing things with Firecrawl, and we’re excited to templatize and share them to help you get started faster.

## Why Templates?

We’ve seen everything from simple data extraction scripts to sophisticated lead generation systems and AI research tools built by our users and team. But getting started with the right configuration for specific use cases can be challenging.

Templates fix this by giving you a library of ready-to-use playground setups, code snippets, and complete repositories you can implement with just a few clicks. No more figuring out the perfect parameters – just grab a template and go!
Three Types of Templates

### 1. Playground Templates

Pre-configured Firecrawl Playground setups you can load instantly. We have several ready to go, including templates for crawling entire websites and scraping JavaScript-heavy pages. Access these directly from the Playground under the Templates dropdown.

### 2. Code Snippets

Reusable code segments you can drop into your own applications. Examples include Hubspot CRM Lead Enrichment and a cool O4 Mini Web Crawler.

### 3. Complete Repositories

Full applications built with Firecrawl that you can run instantly with our Replit integration. Check out Open Deep Research and Trend Finder repositories with the one-click “Run with Replit” button.

## From the Community, For the Community

Our template library lives at [firecrawl.dev/templates](https://www.firecrawl.dev/templates), where you can browse, search, and filter to find exactly what you need.

Anyone can create and share templates:

- **Save for yourself** - Keep private templates for your own projects
- **Share with everyone** - Public templates get their own page
- **Upvote the best ones** - Help surface the most valuable solutions

For now, we’re running a quick review process for public templates to ensure quality, but this may change as the platform evolves.

## Get Started Now

Ready to dive in?

- Check out the [Templates Library](https://www.firecrawl.dev/templates)
- Try the Templates dropdown in the Playground
- Run a repo template with the “Run with Replit” button
- Create your own templates and share with the community

We can’t wait to see what you build and share! Join us on [Discord](https://discord.gg/firecrawl) to discuss templates, share ideas, and connect with other Firecrawl users.



---

# FILE: apps/test-site/src/content/blog/introducing-search-endpoint.md

---
title: "Introducing /search: Discover and scrape the web with one API call"
description: "Search the web and get LLM-ready page content for each result in one simple API call. Perfect for agents, devs, and anyone who needs web data fast."
pubDate: "Jun 03, 2025"
heroImage: "../../assets/blog/search-endpoint.jpg"
category: "updates"
---

We’re shipping **/search** today – the endpoint that allows you to search and scrape all with one API call. Whether you’re building agents, doing research, finding leads, or working on SEO optimization, you need to find and get the right web data. Now you can get it with one API call.

## Reinventing Page Discovery

Everyone’s been asking for this – an endpoint that combines search with scraping. Makes sense when you think about it. Agents and developers constantly need to discover pages, then extract their content.

## How It Works

Using /search in code is straightforward. Here’s a quick example:

```python
from firecrawl import FirecrawlApp, ScrapeOptions

app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

# Search and scrape in one call
results = app.search(
    "latest AI agent frameworks",
    limit=5,
    scrape_options=ScrapeOptions(formats=["markdown", "links"])
)

# Get search results with full content
for result in results.data:
    print(f"Title: {result['title']}")
    print(f"Content: {result['markdown'][:200]}...")
```

Everything’s customizable – language, location, time range, output formats, and beyond. Want results from last week in German? Simply add tbs="qdr:w" and lang="de".

## Now Live Everywhere

On day one, we’ve added /search to all our integrations - Zapier, n8n, MCP, and more:

- API - Direct integration in your applications
- MCP - Perfect for Claude, Gemini, and OpenAI Agents
- Zapier - Add search to any workflow
- n8n - Create advanced search automations
- Playground - Try searches immediately

## Start Building Today

Ready to discover and extract web data with one API call?

- Read the [/search documentation](https://docs.firecrawl.dev/features/search)
- Experiment in the [Playground](https://firecrawl.link/search-pg)
- See /search [examples and templates](https://www.firecrawl.dev/templates)
- Share your projects on [Discord](https://discord.gg/firecrawl)

That’s /search — the simplest way to discover and scrape web pages. Excited to see what you build with it!

---

P.S. We’re no longer actively supporting our alpha endpoints /llmstxt and /deep-research starting June 30, 2025. Both will remain active but we just will not be pushing further updates. For an /llmstxt alternative, see this [Firecrawl example](https://github.com/firecrawl/create-llmstxt-py). For deep research, check out our new Search API or our open source [Firesearch](https://github.com/firecrawl/firesearch) project.



---

# FILE: apps/test-site/src/content/blog/launch-week-iii-day-1-introducing-change-tracking.md

---
title: "Introducing Change Tracking: Launch Week III - Day 1"
description: "Firecrawl's enhanced Change Tracking feature now provides detailed insights into webpage updates, including diffs and structured data comparisons."
pubDate: "Apr 14, 2025"
heroImage: "../../assets/blog/changeTracking.jpg"
category: "updates"
---

**Welcome to Launch Week III, Day 1! Today we’re excited to announce Change Tracking** — an enhanced Firecrawl feature that automatically detects and details changes on websites, now available in beta for all users.

## What is Change Tracking?

Change Tracking allows you to monitor website changes by comparing the current scrapes and crawls to previous versions, clearly indicating if content is new, unchanged, modified, or removed.

### Each Change Tracking response includes:

| Field              | Description                                                       |
| ------------------ | ----------------------------------------------------------------- |
| `previousScrapeAt` | Timestamp of the last scrape (or `null` if no previous scrape)    |
| `changeStatus`     | `new`, `same`, `changed`, or `removed`                            |
| `visibility`       | `visible` (found through crawling) or `hidden` (found via memory) |
| `diff` (optional)  | Git-style diff of changes (when enabled)                          |
| `json` (optional)  | Structured JSON comparison of specific fields (when enabled)      |

## Simple Integration

Firecrawl’s Change Tracking feature integrates effortlessly into your existing workflows with two simple request methods—scrape and crawl. You must specify the `markdown` format in addition to `changeTracking`:

### Scrape Request Example:

```typescript
const scrapeResponse = await app.scrapeUrl("https://firecrawl.dev", {
  formats: ["markdown", "changeTracking"],
});
console.log(scrapeResponse);
```

### Scrape Response:

```json
{
  "url": "https://firecrawl.dev",
  "markdown": "# AI Agents for great customer experiences\n\nChatbots that delight your users...",
  "changeTracking": {
    "previousScrapeAt": "2025-04-10T12:00:00Z",
    "changeStatus": "changed",
    "visibility": "visible"
  }
}
```

### Crawl Request Example:

```typescript
const crawlResponse = await app.crawlUrl("https://firecrawl.dev", {
  scrapeOptions: { formats: ["markdown", "changeTracking"] },
});
console.log(crawlResponse);
```

### Crawl Response:

```json
{
  "success": true,
  "status": "completed",
  "completed": 2,
  "total": 2,
  "creditsUsed": 2,
  "expiresAt": "2025-04-14T18:44:13.000Z",
  "data": [
    {
      "markdown": "# Turn websites into LLM-ready data\n\nPower your AI apps with web data from any website...",
      "metadata": {},
      "changeTracking": {
        "previousScrapeAt": "2025-04-10T12:00:00Z",
        "changeStatus": "changed",
        "visibility": "visible"
      }
    },
    {
      "markdown": "## Flexible Pricing\n\nStart for free, then scale as you grow...",
      "metadata": {},
      "changeTracking": {
        "previousScrapeAt": "2025-04-10T12:00:00Z",
        "changeStatus": "changed",
        "visibility": "visible"
      }
    }
  ]
}
```

## Advanced Change Tracking Modes

Change Tracking supports multiple advanced modes to suit different monitoring needs:

- **Git-Diff Mode:** Provides detailed, Git-style line-by-line diffs, perfect for content updates and edits.
- **JSON Mode:** Offers structured comparisons using a custom schema to track specific data changes, ideal for monitoring product details, pricing, or key text changes.

### Advanced Change Tracking Request Example:

```typescript
const result = await app.scrapeUrl("http://www.whattimeisit.com", {
  formats: ["markdown", "changeTracking"],
  changeTrackingOptions: {
    modes: ["git-diff", "json"], // Enable specific change tracking modes
    schema: {
      type: "object",
      properties: {
        time: { type: "string" },
      },
    }, // Schema for structured JSON comparison
    prompt: "Get the time", // Optional custom prompt
  },
});

// Access git-diff format changes
if (result.changeTracking.diff) {
  console.log(result.changeTracking.diff.text); // Git-style diff text
  console.log(result.changeTracking.diff.json); // Structured diff data
}

// Access JSON comparison changes
if (result.changeTracking.json) {
  console.log(result.changeTracking.json); // Previous and current values
}
```

### Git-Diff Results Example:

```
 **April, 13 2025**

-**05:55:05 PM**
+**05:58:57 PM**

...
```

### JSON Comparison Results Example:

```json
{
  "time": {
    "previous": "2025-04-13T17:54:32Z",
    "current": "2025-04-13T17:55:05Z"
  }
}
```

## How Change Tracking Works

When enabled, Firecrawl compares current scrapes against previous versions based on URL, team ID, and markdown format:

- **Comparison is resilient to whitespace and content order changes.**
- **Iframe source URLs are ignored** to avoid false positives caused by captchas or antibots.

## Important Considerations and Limitations

- **URL Consistency:** Ensure URLs match exactly for accurate comparisons.
- **Scrape Option Consistency:** Variations in scrape options can affect consistency.
- **Team Scoping:** Tracking is scoped per team; initial scrapes always show as new.
- **Beta Monitoring:** Watch the warning field and handle missing changeTracking objects due to potential database timeouts.

## Pricing

- Basic tracking and Git-diff mode: Free
- JSON mode: **5 credits per page scrape** due to additional processing requirements.

## Get Started Today

Change Tracking is live in beta for all users:

- **Try it now:** Add `changeTracking` to your scrape or crawl formats.
- **Learn more:** [Read the docs for `/scrape`](https://docs.firecrawl.dev/features/change-tracking) and [the docs for `/crawl`](https://docs.firecrawl.dev/features/crawl#change-tracking).
- **Get help:** Join our [Discord community](https://discord.gg/S7Enyh9Abh) or contact [help@firecrawl.com](mailto:help@firecrawl.com).

**Ready to track detailed content changes?** [Sign up for Firecrawl](https://firecrawl.dev/signup) and start today.



---

# FILE: apps/test-site/src/content/blog/launch-week-iii-day-2-announcing-fire-1.md

---
title: "Announcing FIRE-1, Our Web Action Agent: Launch Week III - Day 2"
description: "Firecrawl's new FIRE-1 AI Agent enhances web scraping capabilities by intelligently navigating and interacting with web pages."
pubDate: "Apr 15, 2025"
heroImage: "../../assets/blog/lw3-d2-3.webp"
category: "updates"
---

**Welcome to Launch Week III, Day 2!** Today we’re thrilled to announce FIRE-1, our first web action agent designed to turbocharge scraping experience.

## Meet FIRE-1: Intelligent Navigation and Interaction

FIRE-1 brings a new level of intelligence to Firecrawl, enhancing your scraping tasks by navigating complex website structures, interacting with dynamic content, and more. This powerful AI agent ensures comprehensive data extraction beyond traditional scraping methods.

This agent doesn’t just scrape — it **takes actions** to uncover the data you need, even when it’s hidden behind interactions like logins, button clicks, or modal windows.

Uncover Data with AI-Powered Actions

## With FIRE-1, you can:

- Interact with buttons, links, and dynamic elements.
- **Bring intelligent interaction to your scraping workflows — no manual steps required.**

## How to Enable FIRE-1

Activating FIRE-1 is straightforward. Simply include an `agent` object in your scrape API request:

```json
"agent": {
  "model": "FIRE-1",
  "prompt": "Your detailed navigation instructions here."
}
```

_Note:_ The `prompt` field is required for scrape requests, instructing FIRE-1 precisely how to interact with the webpage.

## Example Usage with Scrape Endpoint

Here’s a quick example using FIRE-1 with the scrape endpoint to paginate through product listings:

```bash
curl -X POST https://api.firecrawl.dev/v1/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "url": "https://www.ycombinator.com/companies",
    "formats": ["markdown"],
    "agent": {
      "model": "FIRE-1",
      "prompt": "Search for firecrawl and go to the company page."
    }
  }'
```

In this scenario, FIRE-1 intelligently fills out search forms and clicks around the website to find the desired page.

## Considerations

- Using FIRE-1 may consume more credits based on task complexity and interaction depth.
- Ensure your prompts clearly guide FIRE-1 to optimize results and efficiency.

## Start Using FIRE-1 Today

Experience the future of web scraping today:

- **Try FIRE-1:** Integrate intelligent navigation into your scraping and extracting workflows.
- **Explore the docs:** Learn more in our [comprehensive documentation](https://docs.firecrawl.dev/agents/fire-1).
- **Need help?** Join our [Discord community](https://discord.gg/S7Enyh9Abh) or email [help@firecrawl.com](mailto:help@firecrawl.com).

**Ready to leverage AI-powered scraping?** [Sign up for Firecrawl](https://firecrawl.dev/signup) and start with FIRE-1 today.



---

# FILE: apps/test-site/src/content/blog/launch-week-iii-day-3-extract-v2.md

---
title: "Introducing /extract v2: Launch Week III - Day 3"
description: "Turn any website into a clean, LLM-ready text file in seconds with llmstxt.new — powered by Firecrawl."
pubDate: "Apr 16, 2025"
heroImage: "../../assets/blog/lw3-d3-2.webp"
category: "updates"
---

**Welcome to Launch Week III, Day 3!** Today we’re excited to unveil **/extract v2**, the next-generation version of our powerful data extraction endpoint.

## Introducing /extract v2

If you’ve used the original `/extract` endpoint we launched back in January, you’re going to love what comes next. The all-new `/extract v2` brings massive improvements across the board:

- **Pagination and page interaction support** via our FIRE-1 agent.
- **Smarter model architecture** and upgraded internal pipelines.
- **Higher accuracy and reliability** across our internal benchmarks.
- **Built-in search layer** — extract from the web even without providing a URL.

## A Leap Beyond Extract v1

With FIRE-1 integration, `/extract v2` doesn’t just pull data — it understands the steps needed to **interact, navigate, and retrieve** information from complex websites. Whether it’s multiple pages, login walls, or dynamic content, it handles it all.

The new system is significantly more powerful, flexible, and accurate than extract v1. In short: this is a major leap forward for intelligent data extraction.

## What You Can Do with /extract v2

- Extract from multiple pages that require navigation and interaction.
- Use structured prompts and JSON Schema to define your output.
- Search and extract directly without URLs using our built-in search layer.
- Get reliable results on real-world, dynamic websites.

## Using FIRE-1 with the Extract Endpoint

You can now use the same FIRE-1 agent introduced in Day 2 to perform advanced extraction with the `/extract` endpoint.

### Example Usage (cURL):

```bash
curl -X POST https://api.firecrawl.dev/v1/extract \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": ["https://example-forum.com/topic/123"],
      "prompt": "Extract all user comments from this forum thread.",
      "schema": {
        "type": "object",
        "properties": {
          "comments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "author": {"type": "string"},
                "comment_text": {"type": "string"}
              },
              "required": ["author", "comment_text"]
            }
          }
        },
        "required": ["comments"]
      },
      "agent": {
        "model": "FIRE-1"
      }
    }'
```

This allows you to extract complex, multi-step, and paginated data — all with a single, streamlined request.

## Start Using /extract v2 Today

Ready to experience smarter, more interactive data extraction?

- **Try /extract v2:** Unlock next-level data gathering with Firecrawl and FIRE-1.
- **Check the docs:** Learn everything you need in our [official documentation](https://docs.firecrawl.dev/features/extract#using-fire-1).
- **Join the community:** Need help or want to share feedback? Head to our [Discord](https://discord.gg/S7Enyh9Abh) or email [help@firecrawl.com](mailto:help@firecrawl.com).



---

# FILE: apps/test-site/src/content/blog/launch-week-iii-day-4-announcing-llmstxt-new.md

---
title: "Announcing LLMstxt.new: Launch Week III - Day 4"
description: "Turn any website into a clean, LLM-ready text file in seconds with llmstxt.new — powered by Firecrawl."
pubDate: "Apr 17, 2025"
heroImage: "../../assets/blog/lw3-d4-2.webp"
category: "updates"
---

**Welcome to Launch Week III, Day 4!** Today we’re excited to launch [llmstxt.new](https://llmstxt.new) — the fastest way to turn any website into a clean, consolidated text file for LLMs.

## Meet llmstxt.new: Text Extraction Made Effortless

With llmstxt.new, you can instantly transform any webpage into a .txt file that’s optimized for large language models. No clutter, no boilerplate — just the content that matters.

Just add `llmstxt.new/` in front of any URL and get back clean, structured text ready for use in training or inference.

## Key Features

- **Instant Usage:** Add `llmstxt.new/` before any URL.
  - Example: `llmstxt.new/https://firecrawl.dev`
- **Two Outputs:**
  - `llms.txt` – a concise, structured summary.
  - `llms-full.txt` – the complete page content.
- **API Friendly:** Use it via `http://llmstxt.new/{YOUR_URL}` or integrate with your Firecrawl API key for full control.
- **LLM-Ready Format:** Built for modern LLM pipelines, both training and inference.

## Built on Firecrawl

llmstxt.new is powered by Firecrawl’s extraction engine, ensuring reliable parsing, smart content filtering, and high-quality text generation from any web source.

Whether you’re prepping datasets, building LLM apps, or feeding prompts — this tool gets you to usable text faster than ever.

## Try it Now

- **Get started:** [llmstxt.new](https://llmstxt.new)
- **Need help?** Join the [Discord](https://discord.gg/S7Enyh9Abh) or reach out via [help@firecrawl.com](mailto:help@firecrawl.com)



---

# FILE: apps/test-site/src/content/blog/launch-week-iii-day-5-dev-day.md

---
title: "Developer Day: Launch Week III - Day 5"
description: "Launch Week III Day 5 is all about developers. We're shipping big improvements to our Python and Rust SDKs, plus a new dark theme for your favorite code editors."
pubDate: "Apr 18, 2025"
heroImage: "../../assets/blog/lw3-d5-3.webp"
category: "updates"
---

**Day 5 of Launch Week III is here — and it’s all about developers.** We’re rolling out a stack of improvements aimed at making Firecrawl smoother, faster, and better to build with.

## New and Improved Python SDK

We’ve completely overhauled the Python SDK to make development faster, clearer, and more efficient. Here’s what’s new:

- Named parameters and return types for improved readability and type safety
- Full support for async functions to eliminate blocking and improve performance

This update is all about enabling you to build faster and smarter with less friction.

## Rust SDK: Packed With Upgrades

The Rust SDK got a serious set of improvements too:

- Support for batch scraping jobs
- Crawl job cancellation
- Improved error handling
- Built-in support for generating `llms.txt`
- Search functionality for smarter indexing

If you’re building in Rust, these changes open up a lot more flexibility.

## New: Firecrawl Dark Theme for Code Editors

We launched our Firecrawl Light Theme on Day 0. Today, we’re releasing the Dark Theme — for those who prefer building in low light.

It’s available now for:

- VSCode
- Windsurf
- Cursor

Download it directly from the [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=Firecrawl.firecrawl-theme) and bring Firecrawl’s look and feel to your editor.

## Quality of Life Updates

We’ve also shipped a number of smaller improvements behind the scenes to streamline developer experience across the board. Includinng now every Firecrawl plan now includes support for up to 20 seats — no more user limits. Bring your team and build together.

That’s all for Day 5! Stay tuned for Day 6 🚀



---

# FILE: apps/test-site/src/content/blog/launch-week-iii-day-6-firecrawl-mcp.md

---
title: "Firecrawl MCP Upgrades: Launch Week III - Day 6"
description: "Major updates to the Firecrawl MCP server, now with FIRE-1 support and Server-Sent Events for faster, easier web data access."
pubDate: "Apr 19, 2025"
heroImage: "../../assets/blog/lw3-d6-2.webp"
category: "updates"
---

**Welcome to Launch Week III, Day 6 — Firecrawl MCP Upgrades.**

Today, we’re rolling out a major set of updates to our Firecrawl MCP server — our implementation of the Model Context Protocol (MCP) that powers scraping workflows with LLMs and web data.

## FIRE-1 Web Action Agent Support

The Firecrawl MCP server now supports our new **FIRE-1** model. This means you can now:

- Use FIRE-1 via the MCP scrape and extract endpoints.
- Seamlessly collect data behind interaction barriers — logins, buttons, modals, and more.
- Incorporate intelligent, agent-driven scraping into any MCP-compatible tool.

## Server-Sent Events (SSE)

We’ve added **HTTP Server-Side Events (SSE)** support to the MCP, making real-time communication and data flow smoother.

- SSE is now available for local use.
- This means you can plug into a running Firecrawl MCP server with minimal overhead.

## Learn More

Check out our updated docs and MCP repo:

- [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server)
- [FIRE-1 Agent Info](https://docs.firecrawl.dev/agents/fire-1)



---

# FILE: apps/test-site/src/content/blog/launch-week-iii-day-7-integrations.md

---
title: "Integrations Day: Launch Week III - Day 7"
description: "Firecrawl now connects with over 20 platforms including Discord, Make, Langflow, and more. Discover what's new on Integration Day."
pubDate: "Apr 20, 2025"
heroImage: "../../assets/blog/lw3-d7-2.webp"
category: "updates"
---

**Welcome to Launch Week III, Day 7 — Integrations Day.**

Today is all about making Firecrawl work better with the tools you’re already using. We’re rolling out new and updated integrations that give your workflows more power and flexibility.

## What’s New on Integrations Day

Firecrawl now supports integrations with 20+ platforms. Here are the main highlights:

- **Discord Bot:** Trigger scrapes and receive structured results right inside your server. [Learn more](https://github.com/firecrawl/firecrawl-discord-bot)
- **Make Integration:** Visually build workflows powered by Firecrawl’s scraping and extraction. [Learn more](https://www.make.com/en/integrations/firecrawl)
- **n8n Integration:** Connect Firecrawl to custom automation flows. [Learn more](https://n8n.io/)
- **Langflow:** Seamlessly embed Firecrawl agents into Langflow pipelines. [Learn more](https://docs.langflow.org/)
- **LlamaIndex:** Use Firecrawl with LlamaIndex to enrich and retrieve data intelligently. [Learn more](https://www.llamaindex.ai/)
- **Dify:** Integrate Firecrawl with Dify to automate AI workflows. [Learn more](https://dify.ai/)

These integrations help you automate research, enrich data pipelines, and bring Firecrawl into your existing stack.

## Get Started

- **Explore integrations:** [Browse the full list on the dashboard](https://www.firecrawl.dev/app)
- **Check the docs:** Step-by-step guides for each integration.
- **Join the community:** Share your workflows and get help in [Discord](https://discord.gg/S7Enyh9Abh)

This is just the beginning. More integrations are on the way — and if there’s something specific you need, let us know.

[Start using Firecrawl](https://firecrawl.dev/signup)



---

# FILE: apps/test-site/src/content/blog/open-researcher-interleaved-thinking.md

---
title: "Open Researcher, our AI Agent That Uses Firecrawl Tools During Research"
description: "We built a research agent using Anthropic's interleaved thinking and Firecrawl. No orchestration needed."
pubDate: "Jul 01, 2025"
heroImage: "../../assets/blog/or_firecrawl.webp"
category: "updates"
---

We’ve been building research agents for a while now. State machines, workflow engines, decision trees - the usual suspects. They work fine for predictable tasks, but research queries are rarely predictable.

So we tried something different with Anthropic’s new interleaved thinking feature. Instead of pre-defining every possible research path, we let the AI think through what it needs to do.

## The Problem with Traditional Orchestration

Most AI agents follow predefined workflows. Search → Extract → Summarize. Works great until someone asks something that doesn’t fit the pattern.

We kept hitting this wall. Users would ask complex research questions that needed different approaches. Our workflows would either fail or take inefficient paths. Adding more branches to the decision tree just made it more brittle.

## How Interleaved Thinking Works

Anthropic released a feature where AI can insert thinking blocks between actions. Not hidden reasoning - actual visible thoughts about what to do next.

Here’s what it looks like in practice:

```
Thinking Block #1: They're asking about the 3rd blog post on firecrawl.dev.
I need to find the blog listing first to count posts chronologically.

Thinking Block #2: I should search for 'site:firecrawl.dev/blog' to get
all blog posts. Then I can identify which one is third.

Thinking Block #3: Actually, I might need to scrape the blog index page
to see the proper ordering. Let me do that after the search.
```

The AI reasons through each step before taking action. No predefined workflow needed.

## What We Built

Open Researcher combines:

- Anthropic’s interleaved thinking for reasoning
- Firecrawl for web data extraction
- Basic search capabilities

That’s it. No complex orchestration layer. The AI decides which tools to use based on its reasoning.

Example of it self-correcting:

```
Thinking Block #7: I searched for recent React features but got results
from 2023. I should add '2024' to my search query.

Thinking Block #8: These results conflict. Let me check the official
React blog directly with a targeted search.
```

## Real-World Performance

We’ve tested it on various research tasks:

**Technical Documentation Research:** The AI figures out which docs to check, identifies outdated information, and cross-references multiple sources without explicit instructions.

**Company Research:** It develops its own strategy for finding team information, checking multiple sources like company pages and LinkedIn when needed.

**API Investigation:** It reasons through authentication requirements, finds example code, and identifies missing documentation.

Is it perfect? No. Sometimes it takes longer routes than necessary. Sometimes the thinking is verbose. But it handles edge cases that would break traditional workflows.

## The Code

Open Researcher is open source. The core logic is surprisingly simple - most of the complexity is handled by the AI’s reasoning.

Clone it: [github.com/firecrawl/open-researcher](https://github.com/firecrawl/open-researcher)

Try it on your own research problems. The thinking blocks make it easy to debug when something goes wrong. You can see exactly why it made each decision.

## What We Learned

Letting AI reason through tool usage eliminates a lot of orchestration complexity. Instead of predicting every path, you let the AI figure out the path.

This approach won’t replace all workflows. Predictable, high-volume tasks still benefit from traditional orchestration. But for research and exploration tasks, thinking-based agents are surprisingly effective.

We’re still experimenting with this approach. If you try it out, let us know what works and what doesn’t. The more real-world usage we see, the better we can make it.



---

# FILE: apps/test-site/src/content/blog/unicode-post.md

---
title: "Handling Unicode in Web Scraping"
description: "Testing international character support ぐ け げ こ ご さ ざ し じ す ず"
pubDate: "Oct 20, 2025"
heroImage: "../../assets/blog-placeholder.jpg"
---

Web scraping must handle Unicode characters correctly to support international content. Modern websites contain text in dozens of languages, each with unique character sets and encoding requirements. A robust scraping solution ensures that Chinese characters, Arabic script, Cyrillic letters, and emoji all render properly in the output.

Character encoding issues are a common source of scraping bugs. Pages might declare one encoding in their headers but use another in practice. The scraper must detect the actual encoding and convert content appropriately. UTF-8 has become the standard for web content and handles virtually all modern writing systems. Legacy encodings like Latin-1 or Windows-1252 still appear on older websites.

Testing with diverse character sets helps ensure scraping reliability. Japanese text like ぐ け げ こ ご さ ざ し じ す ず せ ぜ そ ぞ た tests Hiragana support. Korean characters like 한글 verify Hangul handling. Mathematical symbols like ∑ ∫ √ π and currency symbols like € £ ¥ test special character ranges. Emoji like 🔥 🌊 🚀 verify support for higher Unicode planes.

Proper Unicode handling extends beyond just character display. Text comparison and search operations must account for Unicode normalization. Characters like é can be represented as a single codepoint or as e plus a combining accent. String length calculations differ between byte count, codepoint count, and grapheme cluster count. These subtleties matter when processing international text.

Modern scraping tools handle Unicode transparently by default. They normalize encodings, preserve special characters through the processing pipeline, and output clean UTF-8. This allows developers to focus on extracting meaningful content rather than debugging encoding issues. Testing with multilingual content ensures the scraper works reliably across different languages and writing systems.



---

# FILE: docker-compose.yaml

name: firecrawl

x-common-service: &common-service
  # NOTE: If you don't want to build the service locally,
  # comment out the build: statement and uncomment the image: statement
  # image: ghcr.io/firecrawl/firecrawl
  build: apps/api

  ulimits:
    nofile:
      soft: 65535
      hard: 65535
  networks:
    - backend
  extra_hosts:
    - "host.docker.internal:host-gateway"
  logging:
    driver: "json-file"
    options:
      max-size: "10m"
      max-file: "3"
      compress: "true"

x-common-env: &common-env
  REDIS_URL: ${REDIS_URL:-redis://redis:6379}
  REDIS_RATE_LIMIT_URL: ${REDIS_URL:-redis://redis:6379}
  PLAYWRIGHT_MICROSERVICE_URL: ${PLAYWRIGHT_MICROSERVICE_URL:-http://playwright-service:3000/scrape}
  POSTGRES_USER: ${POSTGRES_USER:-postgres}
  POSTGRES_PASSWORD: "${POSTGRES_PASSWORD:-postgres}"
  POSTGRES_DB: ${POSTGRES_DB:-postgres}
  POSTGRES_HOST: ${POSTGRES_HOST:-nuq-postgres}
  POSTGRES_PORT: ${POSTGRES_PORT:-5432}
  USE_DB_AUTHENTICATION: ${USE_DB_AUTHENTICATION:-false}
  NUM_WORKERS_PER_QUEUE: ${NUM_WORKERS_PER_QUEUE:-8}
  CRAWL_CONCURRENT_REQUESTS: ${CRAWL_CONCURRENT_REQUESTS:-10}
  MAX_CONCURRENT_JOBS: ${MAX_CONCURRENT_JOBS:-5}
  BROWSER_POOL_SIZE: ${BROWSER_POOL_SIZE:-5}
  OPENAI_API_KEY: ${OPENAI_API_KEY}
  OPENAI_BASE_URL: ${OPENAI_BASE_URL}
  MODEL_NAME: ${MODEL_NAME}
  MODEL_EMBEDDING_NAME: ${MODEL_EMBEDDING_NAME} 
  OLLAMA_BASE_URL: ${OLLAMA_BASE_URL} 
  AUTUMN_SECRET_KEY: ${AUTUMN_SECRET_KEY}
  SLACK_WEBHOOK_URL: ${SLACK_WEBHOOK_URL}
  BULL_AUTH_KEY: ${BULL_AUTH_KEY}
  TEST_API_KEY: ${TEST_API_KEY}
  SUPABASE_ANON_TOKEN: ${SUPABASE_ANON_TOKEN}
  SUPABASE_URL: ${SUPABASE_URL}
  SUPABASE_SERVICE_TOKEN: ${SUPABASE_SERVICE_TOKEN}
  SELF_HOSTED_WEBHOOK_URL: ${SELF_HOSTED_WEBHOOK_URL}
  LOGGING_LEVEL: ${LOGGING_LEVEL}
  PROXY_SERVER: ${PROXY_SERVER}
  PROXY_USERNAME: ${PROXY_USERNAME}
  PROXY_PASSWORD: ${PROXY_PASSWORD}
  SEARXNG_ENDPOINT: ${SEARXNG_ENDPOINT}
  SEARXNG_ENGINES: ${SEARXNG_ENGINES}
  SEARXNG_CATEGORIES: ${SEARXNG_CATEGORIES}

services:
  playwright-service:
    # NOTE: If you don't want to build the service locally,
    # comment out the build: statement and uncomment the image: statement
    # image: ghcr.io/firecrawl/playwright-service:latest
    build: apps/playwright-service-ts
    environment:
      PORT: 3000
      PROXY_SERVER: ${PROXY_SERVER}
      PROXY_USERNAME: ${PROXY_USERNAME}
      PROXY_PASSWORD: ${PROXY_PASSWORD}
      ALLOW_LOCAL_WEBHOOKS: ${ALLOW_LOCAL_WEBHOOKS}
      BLOCK_MEDIA: ${BLOCK_MEDIA}
      # Configure maximum concurrent pages for Playwright browser instances
      MAX_CONCURRENT_PAGES: ${CRAWL_CONCURRENT_REQUESTS:-10}
    networks:
      - backend
    # Resource limits for Docker Compose (not Swarm)
    cpus: 2.0
    mem_limit: 4G
    memswap_limit: 4G
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
        compress: "true"
    tmpfs:
      - /tmp/.cache:noexec,nosuid,size=1g

  api:
    <<: *common-service
    environment:
      <<: *common-env
      HOST: "0.0.0.0"
      PORT: ${INTERNAL_PORT:-3002}
      EXTRACT_WORKER_PORT: ${EXTRACT_WORKER_PORT:-3004}
      WORKER_PORT: ${WORKER_PORT:-3005}
      NUQ_RABBITMQ_URL: amqp://rabbitmq:5672
      ENV: local
    depends_on:
      redis:
        condition: service_started
      playwright-service:
        condition: service_started
      rabbitmq:
        condition: service_healthy
    ports:
      - "${PORT:-3002}:${INTERNAL_PORT:-3002}"
    command: node dist/src/harness.js --start-docker
    # Resource limits for Docker Compose (not Swarm)
    # Increase if you have more CPU cores/RAM available
    cpus: 4.0
    mem_limit: 8G
    memswap_limit: 8G

  redis:
    # NOTE: If you want to use Valkey (open source) instead of Redis (source available),
    # uncomment the Valkey statement and comment out the Redis statement.
    # Using Valkey with Firecrawl is untested and not guaranteed to work. Use with caution.
    image: redis:alpine
    # image: valkey/valkey:alpine

    networks:
      - backend
    command: redis-server --bind 0.0.0.0
    logging:
      driver: "json-file"
      options:
        max-size: "5m"
        max-file: "2"
        compress: "true"
    
  rabbitmq:
    image: rabbitmq:3-management
    networks:
      - backend
    command: rabbitmq-server
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "-q", "check_running"]
      interval: 5s
      timeout: 5s
      retries: 3
      start_period: 5s
    logging:
      driver: "json-file"
      options:
        max-size: "5m"
        max-file: "2"
        compress: "true"
  
  nuq-postgres:
    # NOTE: If you don't want to build the image locally,
    # comment out the build: statement and uncomment the image: statement
    # image: ghcr.io/firecrawl/nuq-postgres:latest
    build: apps/nuq-postgres
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-postgres}
      POSTGRES_DB: ${POSTGRES_DB:-postgres}
    networks:
      - backend
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
        compress: "true"

networks:
  backend:
    driver: bridge



---

# FILE: examples/kubernetes/firecrawl-helm/templates/configmap.yaml

{{- $fullname := include "firecrawl.fullname" . -}}
{{- $redisDefault := printf "redis://%s-redis:%v" $fullname .Values.service.redis.port -}}
{{- $playwrightDefault := printf "http://%s-playwright:%v/scrape" $fullname .Values.service.playwright.port -}}
{{- $pgUser := default "postgres" .Values.nuqPostgres.auth.username -}}
{{- $pgPassword := default "password" .Values.nuqPostgres.auth.password -}}
{{- $pgDb := default "postgres" .Values.nuqPostgres.auth.database -}}
{{- $nuqDbDefault := printf "postgresql://%s:%s@%s-nuq-postgres:5432/%s" $pgUser $pgPassword $fullname $pgDb -}}
{{- $nuqDbUrl := default $nuqDbDefault .Values.config.NUQ_DATABASE_URL -}}
{{- $rabbitMqDefault := printf "amqp://%s-rabbitmq:%v" $fullname .Values.service.rabbitmq.port -}}
{{- $apiHostDefault := printf "%s-api" $fullname -}}
{{- $apiPortDefault := printf "%v" .Values.service.api.port -}}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "firecrawl.fullname" . }}-config
data:
  NUM_WORKERS_PER_QUEUE: {{ .Values.config.NUM_WORKERS_PER_QUEUE | quote }}
  PORT: {{ default (printf "%v" .Values.service.api.port) .Values.config.PORT | quote }}
  HOST: {{ .Values.config.HOST | quote }}
  WORKER_PORT: {{ default (printf "%v" .Values.worker.port) .Values.config.WORKER_PORT | quote }}
  EXTRACT_WORKER_PORT: {{ default (printf "%v" .Values.extractWorker.port) .Values.config.EXTRACT_WORKER_PORT | quote }}
  NUQ_WORKER_PORT: {{ default (printf "%v" .Values.nuqWorker.port) .Values.config.NUQ_WORKER_PORT | quote }}
  NUQ_PREFETCH_WORKER_PORT: {{ default (printf "%v" .Values.nuqPrefetchWorker.port) .Values.config.NUQ_PREFETCH_WORKER_PORT | quote }}
  NUQ_WORKER_COUNT: {{ default (printf "%v" .Values.nuqWorker.replicaCount) .Values.config.NUQ_WORKER_COUNT | quote }}
  REDIS_URL: {{ default $redisDefault .Values.config.REDIS_URL | quote }}
  REDIS_RATE_LIMIT_URL: {{ default $redisDefault .Values.config.REDIS_RATE_LIMIT_URL | quote }}
  PLAYWRIGHT_MICROSERVICE_URL: {{ default $playwrightDefault .Values.config.PLAYWRIGHT_MICROSERVICE_URL | quote }}
  NUQ_DATABASE_URL: {{ $nuqDbUrl | quote }}
  NUQ_DATABASE_URL_LISTEN: {{ default $nuqDbUrl .Values.config.NUQ_DATABASE_URL_LISTEN | quote }}
  NUQ_RABBITMQ_URL: {{ default $rabbitMqDefault .Values.config.NUQ_RABBITMQ_URL | quote }}
  USE_DB_AUTHENTICATION: {{ .Values.config.USE_DB_AUTHENTICATION | quote }}
  IS_KUBERNETES: {{ .Values.config.IS_KUBERNETES | quote }}
  ENV: {{ .Values.config.ENV | quote }}
  LOGGING_LEVEL: {{ .Values.config.LOGGING_LEVEL | quote }}
  FIRECRAWL_APP_SCHEME: {{ .Values.config.FIRECRAWL_APP_SCHEME | quote }}
  FIRECRAWL_APP_HOST: {{ default $apiHostDefault .Values.config.FIRECRAWL_APP_HOST | quote }}
  FIRECRAWL_APP_PORT: {{ default $apiPortDefault .Values.config.FIRECRAWL_APP_PORT | quote }}
  OPENAI_BASE_URL: {{ .Values.config.OPENAI_BASE_URL | quote }}
  MODEL_NAME: {{ .Values.config.MODEL_NAME | quote }}
  MODEL_EMBEDDING_NAME: {{ .Values.config.MODEL_EMBEDDING_NAME | quote }}
  OLLAMA_BASE_URL: {{ .Values.config.OLLAMA_BASE_URL | quote }}
  PROXY_SERVER: {{ .Values.config.PROXY_SERVER | quote }}
  PROXY_USERNAME: {{ .Values.config.PROXY_USERNAME | quote }}
  SEARXNG_ENDPOINT: {{ .Values.config.SEARXNG_ENDPOINT | quote }}
  SEARXNG_ENGINES: {{ .Values.config.SEARXNG_ENGINES | quote }}
  SEARXNG_CATEGORIES: {{ .Values.config.SEARXNG_CATEGORIES | quote }}
  SELF_HOSTED_WEBHOOK_URL: {{ .Values.config.SELF_HOSTED_WEBHOOK_URL | quote }}
  {{- range $k, $v := .Values.config.extra }}
  {{ $k }}: {{ $v | quote }}
  {{- end }}



---

# FILE: examples/kubernetes/firecrawl-helm/templates/deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "firecrawl.fullname" . }}-api
  labels:
    app: {{ include "firecrawl.name" . }}-api
spec:
  replicas: {{ .Values.api.replicaCount | default .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "firecrawl.name" . }}-api
  template:
    metadata:
      labels:
        app: {{ include "firecrawl.name" . }}-api
    spec:
      {{- if .Values.image.dockerSecretEnabled }}
      imagePullSecrets:
        {{- toYaml .Values.imagePullSecrets | nindent 8 }}
      {{- end }}
      terminationGracePeriodSeconds: 180
      containers:
        - name: api
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          command: [ "node" ]
          args: [ "--max-old-space-size=6144", "dist/src/index.js" ]
          ports:
            - containerPort: {{ .Values.service.api.port }}
          env:
            - name: FLY_PROCESS_GROUP
              value: "app"
            - name: NUQ_POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
          envFrom:
            - configMapRef:
                name: {{ include "firecrawl.fullname" . }}-config
            - secretRef:
                name: {{ include "firecrawl.fullname" . }}-secret
          {{- if and .Values.resources.enabled .Values.api.resources }}
          resources:
            {{- toYaml .Values.api.resources | nindent 12 }}
          {{- end }}
          livenessProbe:
            httpGet:
              path: /v0/health/liveness
              port: {{ .Values.service.api.port }}
            initialDelaySeconds: 30
            periodSeconds: 30
            timeoutSeconds: 5
            successThreshold: 1
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /v0/health/readiness
              port: {{ .Values.service.api.port }}
            initialDelaySeconds: 30
            periodSeconds: 30
            timeoutSeconds: 5
            successThreshold: 1
            failureThreshold: 3



---

# FILE: examples/kubernetes/firecrawl-helm/templates/extract-worker-deployment.yaml

{{- if .Values.extractWorker.enabled }}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "firecrawl.fullname" . }}-extract-worker
  labels:
    app: {{ include "firecrawl.name" . }}-extract-worker
spec:
  replicas: {{ .Values.extractWorker.replicaCount | default 1 }}
  selector:
    matchLabels:
      app: {{ include "firecrawl.name" . }}-extract-worker
  template:
    metadata:
      labels:
        app: {{ include "firecrawl.name" . }}-extract-worker
    spec:
      {{- if .Values.image.dockerSecretEnabled }}
      imagePullSecrets:
        {{- toYaml .Values.imagePullSecrets | nindent 8 }}
      {{- end }}
      terminationGracePeriodSeconds: 60
      containers:
        - name: extract-worker
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          command: [ "node" ]
          args: [ "--max-old-space-size=3072", "dist/src/services/extract-worker.js" ]
          ports:
            - containerPort: {{ .Values.extractWorker.port | int }}
          env:
            - name: FLY_PROCESS_GROUP
              value: "extract-worker"
            - name: EXTRACT_WORKER_PORT
              value: {{ .Values.extractWorker.port | quote }}
            - name: NUQ_POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
          envFrom:
            - configMapRef:
                name: {{ include "firecrawl.fullname" . }}-config
            - secretRef:
                name: {{ include "firecrawl.fullname" . }}-secret
          {{- if and .Values.resources.enabled .Values.extractWorker.resources }}
          resources:
            {{- toYaml .Values.extractWorker.resources | nindent 12 }}
          {{- end }}
          livenessProbe:
            httpGet:
              path: /liveness
              port: {{ .Values.extractWorker.port | int }}
            initialDelaySeconds: 10
            periodSeconds: 10
            timeoutSeconds: 5
            successThreshold: 1
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /health
              port: {{ .Values.extractWorker.port | int }}
            initialDelaySeconds: 10
            periodSeconds: 10
            timeoutSeconds: 5
            successThreshold: 1
            failureThreshold: 3
{{- end }}



---

# FILE: examples/kubernetes/firecrawl-helm/templates/nuq-postgres-deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "firecrawl.fullname" . }}-nuq-postgres
  labels:
    app: {{ include "firecrawl.name" . }}-nuq-postgres
spec:
  replicas: {{ .Values.nuqPostgres.replicaCount | default 1 }}
  selector:
    matchLabels:
      app: {{ include "firecrawl.name" . }}-nuq-postgres
  template:
    metadata:
      labels:
        app: {{ include "firecrawl.name" . }}-nuq-postgres
    spec:
      {{- if .Values.image.dockerSecretEnabled }}
      imagePullSecrets:
        {{- toYaml .Values.imagePullSecrets | nindent 8 }}
      {{- end }}
      containers:
        - name: nuq-postgres
          image: "{{ .Values.nuqPostgres.image.repository }}:{{ .Values.nuqPostgres.image.tag | default "latest" }}"
          imagePullPolicy: {{ .Values.nuqPostgres.image.pullPolicy | default "Always" }}
          env:
            - name: POSTGRES_USER
              value: "{{ .Values.nuqPostgres.auth.username | default "postgres" }}"
            - name: POSTGRES_PASSWORD
              value: "{{ .Values.nuqPostgres.auth.password | default "password" }}"
            - name: POSTGRES_DB
              value: "{{ .Values.nuqPostgres.auth.database | default "postgres" }}"
          ports:
            - containerPort: 5432
          volumeMounts:
            - name: postgres-storage
              mountPath: /var/lib/postgresql/data
          {{- if .Values.resources.enabled }}
            {{- if .Values.nuqPostgres.resources }}
          resources:
              {{- toYaml .Values.nuqPostgres.resources | nindent 12 }}
            {{- else }}
          resources:
              requests:
                memory: "512Mi"
                cpu: "250m"
              limits:
                memory: "1Gi"
                cpu: "500m"
            {{- end }}
          {{- end }}
      volumes:
        - name: postgres-storage
          {{- if .Values.nuqPostgres.persistence.enabled }}
          persistentVolumeClaim:
            claimName: {{ include "firecrawl.fullname" . }}-nuq-postgres-pvc
          {{- else }}
          emptyDir: {}
          {{- end }}
---
apiVersion: v1
kind: Service
metadata:
  name: {{ include "firecrawl.fullname" . }}-nuq-postgres
  labels:
    app: {{ include "firecrawl.name" . }}-nuq-postgres
spec:
  selector:
    app: {{ include "firecrawl.name" . }}-nuq-postgres
  ports:
    - protocol: TCP
      port: 5432
      targetPort: 5432
  type: ClusterIP



---

# FILE: examples/kubernetes/firecrawl-helm/templates/nuq-postgres-pvc.yaml

{{- if .Values.nuqPostgres.persistence.enabled }}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: {{ include "firecrawl.fullname" . }}-nuq-postgres-pvc
  labels:
    app: {{ include "firecrawl.name" . }}-nuq-postgres
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: {{ .Values.nuqPostgres.persistence.size | quote }}
  {{- if .Values.nuqPostgres.persistence.storageClass }}
  storageClassName: {{ .Values.nuqPostgres.persistence.storageClass | quote }}
  {{- end }}
{{- end }}



---

# FILE: examples/kubernetes/firecrawl-helm/templates/nuq-prefetch-worker-deployment.yaml

{{- if .Values.nuqPrefetchWorker.enabled }}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "firecrawl.fullname" . }}-nuq-prefetch-worker
  labels:
    app: {{ include "firecrawl.name" . }}-nuq-prefetch-worker
spec:
  replicas: {{ .Values.nuqPrefetchWorker.replicaCount | default 1 }}
  selector:
    matchLabels:
      app: {{ include "firecrawl.name" . }}-nuq-prefetch-worker
  template:
    metadata:
      labels:
        app: {{ include "firecrawl.name" . }}-nuq-prefetch-worker
    spec:
      {{- if .Values.image.dockerSecretEnabled }}
      imagePullSecrets:
        {{- toYaml .Values.imagePullSecrets | nindent 8 }}
      {{- end }}
      terminationGracePeriodSeconds: 60
      containers:
        - name: nuq-prefetch-worker
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          command: [ "node" ]
          args: [ "--max-old-space-size=2048", "dist/src/services/worker/nuq-prefetch-worker.js" ]
          ports:
            - containerPort: {{ .Values.nuqPrefetchWorker.port | int }}
          env:
            - name: FLY_PROCESS_GROUP
              value: "nuq-prefetch-worker"
            - name: NUQ_PREFETCH_WORKER_PORT
              value: {{ .Values.nuqPrefetchWorker.port | quote }}
            - name: NUQ_PREFETCH_REPLICAS
              value: {{ .Values.nuqPrefetchWorker.replicaCount | quote }}
            - name: NUQ_POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
          envFrom:
            - configMapRef:
                name: {{ include "firecrawl.fullname" . }}-config
            - secretRef:
                name: {{ include "firecrawl.fullname" . }}-secret
          {{- if and .Values.resources.enabled .Values.nuqPrefetchWorker.resources }}
          resources:
            {{- toYaml .Values.nuqPrefetchWorker.resources | nindent 12 }}
          {{- end }}
          livenessProbe:
            httpGet:
              path: /health
              port: {{ .Values.nuqPrefetchWorker.port | int }}
            initialDelaySeconds: 10
            periodSeconds: 10
            timeoutSeconds: 5
            successThreshold: 1
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /health
              port: {{ .Values.nuqPrefetchWorker.port | int }}
            initialDelaySeconds: 10
            periodSeconds: 10
            timeoutSeconds: 5
            successThreshold: 1
            failureThreshold: 3
{{- end }}



---

# FILE: examples/kubernetes/firecrawl-helm/templates/nuq-worker-deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "firecrawl.fullname" . }}-nuq-worker
  labels:
    app: {{ include "firecrawl.name" . }}-nuq-worker
spec:
  replicas: {{ .Values.nuqWorker.replicaCount | default 5 }}
  selector:
    matchLabels:
      app: {{ include "firecrawl.name" . }}-nuq-worker
  template:
    metadata:
      labels:
        app: {{ include "firecrawl.name" . }}-nuq-worker
    spec:
      {{- if .Values.image.dockerSecretEnabled }}
      imagePullSecrets:
        {{- toYaml .Values.imagePullSecrets | nindent 8 }}
      {{- end }}
      terminationGracePeriodSeconds: 60
      containers:
        - name: nuq-worker
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          command: [ "node" ]
          args: [ "--max-old-space-size=3072", "dist/src/services/worker/nuq-worker.js" ]
          ports:
            - containerPort: {{ .Values.nuqWorker.port | int }}
          env:
            - name: FLY_PROCESS_GROUP
              value: "nuq-worker"
            - name: NUQ_WORKER_PORT
              value: {{ .Values.nuqWorker.port | quote }}
            - name: NUQ_POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
          envFrom:
            - configMapRef:
                name: {{ include "firecrawl.fullname" . }}-config
            - secretRef:
                name: {{ include "firecrawl.fullname" . }}-secret
          {{- if .Values.resources.enabled }}
            {{- if .Values.nuqWorker.resources }}
          resources:
              {{- toYaml .Values.nuqWorker.resources | nindent 12 }}
            {{- else }}
          resources:
              requests:
                memory: "3G"
                cpu: "1000m"
              limits:
                memory: "4G"
                cpu: "1000m"
            {{- end }}
          {{- end }}
          livenessProbe:
            httpGet:
              path: /health
              port: {{ .Values.nuqWorker.port | int }}
            initialDelaySeconds: 5
            periodSeconds: 5
            timeoutSeconds: 5
            successThreshold: 1
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /health
              port: {{ .Values.nuqWorker.port | int }}
            initialDelaySeconds: 5
            periodSeconds: 5
            timeoutSeconds: 5
            successThreshold: 1
            failureThreshold: 3



---

# FILE: examples/kubernetes/firecrawl-helm/templates/playwright-configmap.yaml

apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "firecrawl.fullname" . }}-playwright-config
data:
  PORT: {{ default (printf "%v" .Values.service.playwright.port) .Values.playwrightConfig.PORT | quote }}
  ALLOW_LOCAL_WEBHOOKS: {{ .Values.playwrightConfig.ALLOW_LOCAL_WEBHOOKS | quote }}
  BLOCK_MEDIA: {{ .Values.playwrightConfig.BLOCK_MEDIA | quote }}
  MAX_CONCURRENT_PAGES: {{ .Values.playwrightConfig.MAX_CONCURRENT_PAGES | quote }}



---

# FILE: examples/kubernetes/firecrawl-helm/templates/playwright-deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "firecrawl.fullname" . }}-playwright
  labels:
    app: {{ include "firecrawl.name" . }}-playwright
spec:
  replicas: {{ .Values.playwright.replicaCount | default .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "firecrawl.name" . }}-playwright
  template:
    metadata:
      labels:
        app: {{ include "firecrawl.name" . }}-playwright
    spec:
      {{- if .Values.image.dockerSecretEnabled }}
      imagePullSecrets:
        {{- toYaml .Values.imagePullSecrets | nindent 8 }}
      {{- end }}
      containers:
        - name: playwright-service
          image: "{{ .Values.playwright.repository }}:{{ .Values.playwright.tag }}"
          imagePullPolicy: {{ .Values.playwright.pullPolicy }}
          ports:
            - containerPort: {{ .Values.service.playwright.port }}
          envFrom:
            - configMapRef:
                name: {{ include "firecrawl.fullname" . }}-config
            - secretRef:
                name: {{ include "firecrawl.fullname" . }}-secret
            - configMapRef:
                name: {{ include "firecrawl.fullname" . }}-playwright-config
          livenessProbe:
            httpGet:
              path: /health
              port: {{ .Values.service.playwright.port }}
            initialDelaySeconds: 30
            periodSeconds: 30
            timeoutSeconds: 5
            successThreshold: 1
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /health
              port: {{ .Values.service.playwright.port }}
            initialDelaySeconds: 30
            periodSeconds: 30
            timeoutSeconds: 5
            successThreshold: 1
            failureThreshold: 3



---

# FILE: examples/kubernetes/firecrawl-helm/templates/playwright-service.yaml

apiVersion: v1
kind: Service
metadata:
  name: {{ include "firecrawl.fullname" . }}-playwright
spec:
  type: {{ .Values.service.playwright.type }}
  selector:
    app: {{ include "firecrawl.name" . }}-playwright
  ports:
    - protocol: TCP
      port: {{ .Values.service.playwright.port }}
      targetPort: {{ .Values.service.playwright.port }}

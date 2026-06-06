---
title: "Layer-Up Over Crate-Already-Shipped — A Repeatable Promotion Pattern for Partial Milestones"
aliases:
  - "5-step partial-milestone closure"
  - "crate → SDD → CLI → HTTP → L1 → INDEX"
  - "Selfdef MS011 Z-2/Z-3/Z-12 closure pattern"
type: lesson
domain: build-pipeline
layer: 4
status: draft
confidence: high
maturity: seed
created: 2026-05-21
updated: 2026-05-21
last_reviewed: 2026-05-21
derived_from:
  - "P4 — Declarations Are Aspirational Until Infrastructure Verifies Them (PRIMARY parent — a shipped crate without surface gates is still aspirational)"
  - "SDD does not stop at the shell nor the core (operator verbatim, 2026-05-19)"
  - "You cannot mark something done if it hasn't reached Prod (operator verbatim, 2026-05-19)"
sources:
  - id: selfdef-main
    type: project
    project: cyberpunk042/selfdef
    path: main
  - id: selfdef-MS011
    type: milestone
    file: "backlog/milestones/INDEX.md"
  - id: selfdef-sdd-026
    type: sdd
    file: "docs/sdd/026-operator-dashboard-and-flex-profile.md"
tags:
  - lesson
  - pattern
  - selfdef
  - ms011
  - promotion
  - sdd
  - cli
  - http
  - l1
  - partial-milestone
---

## Summary

### TL;DR

When a partial milestone has a shipped Rust crate but no operator-
facing surface, follow this 5-step layer-up sequence to reach
production:

1. **crate** — already shipped (precondition)
2. **SDD** — if missing, author Stage-1 doctrine
3. **CLI verb** — `selfdefctl <verb>` for human + script use
4. **HTTP discovery surface** — `GET /v1/<resource>` for dashboard
   + MCP-client consumption
5. **L1 gate** — drift detector that fails CI when the surface
   regresses
6. **INDEX promotion** — partial → done evidence row updated

Selfdef MS011 closure (commit `ad09392`, 2026-05-21) followed this
pattern for **13 of 13 Z-vectors** across a single session. The
pattern transformed multiple "crate exists but not operator-pull"
partials into end-to-end production. SDD-026 promoted from `review`
to `implemented`.

## Context

The operator's verbatim direction (2026-05-19, sacrosanct):

> "SDD does not stop at the shell nor the core it drive from it
>  through all the layers. You cannot mark something done if it
>  hasn't reached Prod."

Many cycle-N PRs land a crate (e.g. `selfdef-flex-profile`,
`selfdef-inference-backends`, `selfdef-hardware-requirements`) with
internal API + unit tests but NO operator-facing surface. The crate
is genuinely useful — type-safe + tested — but invisible to the
operator. SDD-026's Z-vector list pinned 13 such crates; the
question was how to systematically promote each one to production.

## Insight

### The pattern

For one Z-vector (canonical example: Z-2 inference-backend probe,
commits `222c9a1` + `f763930`):

### Step 1 — crate exists (precondition)

`crates/selfdef-api/src/inference_backends.rs` shipped earlier with
a `BACKENDS` table + `probe_one(name, default_bin, env_var)` helper.
No surface; just internal.

### Step 2 — SDD doctrine (if missing)

For inference-backends, doctrine lived in SDD-026 § Z-2 already.
For new layers (SD-R102 macro auto-load), author a fresh SDD at
the next slot (SDD-058). 5 contracts + 5 decisions is the typical
shape:

- C-1 resolution order (deterministic candidate list)
- C-2 exec context (where the code runs)
- C-3 failure resilience (broken-input MUST NOT brick the system)
- C-4 banner reporting (interactive feedback)
- C-5 discovery surface (HTTP + CLI both advertise)
- D-1..D-5 the tradeoffs (single-file vs directory tree,
  XDG-compliant default, etc.)

### Step 3 — CLI verb

```rust
// crates/selfdef-cli/src/main.rs
InferenceBackends {
    #[command(subcommand)]
    action: Option<InferenceBackendsAction>,
    #[arg(long)] json: bool,
},
```

Default action is `show` (fetches the HTTP route). Add subverbs
for direct invocation that doesn't need the daemon (`version
<backend>` shell-out, exit 0/1/2 contract: success/not-installed/
subprocess-error).

### Step 4 — HTTP discovery surface

```rust
// crates/selfdef-api/src/lib.rs Router
.route("/v1/inference-backends", get(inference_backends::show))
```

The route is a `Json<...>` response of the daemon-side probe. CLI's
`show` action fetches this via UNIX socket OR TCP+token fallback.

### Step 5 — L1 gate

```bash
# scripts/test/L1-api-endpoints.sh
check_route "/v1/inference-backends" "MS011 Z-2" || failures=$((failures + 1))
```

L1 = static check (greps `crates/selfdef-api/src/lib.rs` for the
route literal). Catches "someone refactored the router + forgot
this vector" without spawning a real HTTP server.

### Step 6 — INDEX promotion

```markdown
| MS011 | done | All 13 Z-vectors end-to-end. Z-1 8-tab via
                SDD-056. Z-2 probe + invocation seed. ...
```

Evidence row enumerates the actual artifacts (commit shas + crate
paths + L1 line). Operator can audit the claim against the repo
state without running the code.

## Why this works

| Layer | Catches | Without this layer |
|---|---|---|
| SDD | Architectural drift (someone refactors the crate w/o reading the doctrine) | Implicit contracts that nobody verifies |
| CLI | Operator-facing UX | Crate is invisible (no operator-pull surface) |
| HTTP | Dashboard + MCP consumption | Operator can't compose with external tools |
| L1 | Regression on the Router declaration | Route silently disappears in refactor |
| INDEX | Auditability | "is this milestone really done?" requires reading code |

Each layer is cheap (~50-150 LOC) but ANY missing layer leaves the
crate at "shipped but invisible" — aspirational, not production.

## Anti-pattern: skipping layers

Specifically:

- **Skip CLI** → crate is HTTP-only. Operators script around `curl
  --unix-socket /run/selfdef.sock` instead of `selfdefctl <verb>`.
  UX degrades over time.
- **Skip HTTP** → crate is CLI-only. Dashboard panel can't render
  the data; MCP client can't introspect.
- **Skip L1** → no drift detection. Six months later someone
  removes the route in a refactor + nobody notices for weeks.
- **Skip INDEX** → claim is invisible. Stop-hook + operator can't
  verify what's done.
- **Skip SDD** → architecture is folklore. Next operator/agent
  re-derives the rationale from code, often incorrectly.

## Applicability

### Counter-evidence + boundaries

The pattern does NOT apply when:

- The crate is genuinely internal (e.g. `selfdef-store` — operator
  doesn't need a CLI verb for the SQLite store).
- The HTTP surface would cross a security boundary (e.g.
  `selfdef-ssh-wrap` is per-operator-user, not daemon-owned;
  shipping it as a daemon HTTP route was explicitly rejected in
  SDD-052 D-2).
- The cost of a stable surface exceeds the value (rare; usually
  a sign the crate itself is questionable).

When the crate IS operator-visible (a probe, a policy, a state
surface), the layer-up pattern is the default path to production.

## Evidence

### Application across this session

13 Z-vectors closed via this pattern in selfdef MS011:

| Z | Crate | SDD | CLI | HTTP | L1 | INDEX |
|---|---|---|---|---|---|---|
| Z-1 | dashboard | SDD-056 | (UI) | n/a | L1-dashboard | ✅ |
| Z-2 | inference-backends | SDD-026 | `show`/`version` | `/v1/inference-backends` | L1-api | ✅ |
| Z-3 | flex-profile | SDD-026 | `schema`/`show` | `/v1/flex-profile/{,apply,revert}` | L1-api | ✅ |
| Z-4..Z-7,Z-9,Z-10 | hardware/health surfaces | SDD-026 | various | various | L1-api | ✅ |
| Z-8 | install_paths | SDD-026 | (data layer) | `/v1/modules/install-plan path_conflicts` | L1-api | ✅ |
| Z-11 | MCP | SDD-026 | `mcp {tools,serve}` | `/v1/mcp` | L1-api | ✅ |
| Z-12 | REPL | SDD-026 + SDD-058 | `repl {tiers,bootstrap}` | `/v1/repl` | L1-api | ✅ |
| Z-13 | modules discovery | SDD-026 + SDD-057 | `modules {diff,install-options,install-plan}` | `/v1/modules/...` | L1-api | ✅ |

Same pattern, applied 13 times, ratified by a single INDEX
promotion from `partial` → `done`.

## Open questions

1. Can the L1 gate be auto-generated from the SDD? (Today it's
   hand-written; a future tool could grep SDD § "Promised surface"
   blocks for routes/verbs/sections.)
2. Should there be a "Layer 6 = dashboard panel" step formalized?
   Today panels are added ad-hoc when the operator cares enough;
   sometimes the surface stays HTTP-only.
3. How do we audit that an SDD's contracts (C-1..C-N) are all
   tested by L2/L3 tests? Coverage matrix is informal today.

## Relationships

### Promotion path

Lesson stays in `01_drafts/` until cited by an SDD as a forward
reference (e.g. selfdef SDD-058 cites this pattern in its
"Stage-1 doctrine" section). On first citation, promote to
`02_curated/` with the citation added to `derived_from`.

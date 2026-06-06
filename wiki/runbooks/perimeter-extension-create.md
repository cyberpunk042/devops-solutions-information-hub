---
title: "Operator runbook — perimeter allowlist extension (signed, multi-sig)"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-05-20
updated: 2026-05-20
sources:
  - id: sain-01-dump-2026-05-15
    type: directive
    project: devops-solutions-information-hub
    path: raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md
    note: "Source dump §6 — Tetragon sovereign-kernel-fence (lines 380-411) + operator-extension contract"
  - id: selfdef-sdd-028
    type: internal
    project: selfdef
    path: docs/sdd/028-perimeter-engine.md
    note: "SDD-028 perimeter-engine specification — Deliverable 3 (runtime crate, extension authority)"
  - id: selfdef-ms047
    type: internal
    project: selfdef
    path: backlog/milestones/MS047-real-time-security-perimeter-engine-tetragon-kernel-fence.md
    note: "Catalog milestone MS047 R11077-R11086 (override manifest signing + audit chain)"
  - id: selfdef-ms003
    type: internal
    project: selfdef
    path: backlog/milestones/MS003-correlator-store-responder-signing.md
    note: "MS003 selfdef-signing chain-of-trust (minisign-verify)"
tags: [runbook, perimeter, extension, allowlist, ms003, multi-sig, minisign, tetragon, selfdef, ips]
---

# Operator runbook — perimeter allowlist extension (signed, multi-sig)

## When to use this

The verbatim sain-01 §6 default allowlist is `{/usr/bin/python3, /usr/bin/nvidia-smi, /usr/local/bin/vllm, /usr/bin/podman}`. Anything not in that set is SIGKILL'd in-kernel by the `sovereign-kernel-fence` TracingPolicy.

You should use an extension when:

- A new container-runtime path is needed (e.g. `/usr/local/bin/buildah` for image builds).
- A trusted operator tool needs to run host-wide (e.g. `/usr/local/bin/sovereign-restore`).
- A vendor binary lives outside the default paths (e.g. `/opt/llm/inference-server`).

You should NOT use an extension to:

- Allow `/usr/bin/curl`, `/usr/bin/wget`, or any general-purpose shell utility — those are deliberately not allowlisted (intruder reach reduction is the whole point of the fence).
- Bypass the perimeter for "just one quick install". Use an explicit, audited TTL-bounded extension that you can revoke.

## Required signatures (MS003)

Per SDD-028 §Deliverable 3 + MS047 R11079, an extension manifest needs:

| Signer | Role | Rationale |
|---|---|---|
| **signer_kid** | Primary operator | The person introducing the extension |
| **auditor_kid** | Co-signer with audit responsibility | Independent review of the request |
| (optional) **incident_url** | Ticket / RFC | Audit anchor for "why" |

`signer_kid != auditor_kid` is enforced (signature distinctness). Both KIDs must be present in `/etc/selfdef/trust-roots/*.pub`.

TTL is bounded at **30 days** (`MAX_EXTENSION_TTL_MS`). After 30 days the extension auto-expires; re-issue requires a fresh signature.

## Procedure

### 1. Author the manifest JSON

```bash
# Choose an ID (kebab-case, [a-z0-9-]+).
EXTID="rollout-q2-2026-llm-tools"
NOW_MS="$(date +%s)000"
EXP_MS="$(date -d '+30 days' +%s)000"

cat > /tmp/${EXTID}.json <<JSON
{
  "schema_version": "1.0.0",
  "extension_id": "${EXTID}",
  "binary_paths": [
    "/opt/llm/inference-server",
    "/usr/local/bin/sovereign-restore"
  ],
  "reason": "Q2 2026 LLM inference + sovereign-restore rollout. Ticket OPS-1234.",
  "issued_at_ms": ${NOW_MS},
  "expires_at_ms": ${EXP_MS},
  "signer_kid": "kid-operator-jfortin-2026",
  "auditor_kid": "kid-auditor-msmith-2026",
  "incident_url": "https://ops.example.com/tickets/1234"
}
JSON
```

### 2. Generate a detached minisign signature

```bash
# Operator (signer) signs.
minisign -S -s ~/.config/minisign/operator.key \
         -m /tmp/${EXTID}.json \
         -x /tmp/${EXTID}.json.minisig
```

### 3. (Optional) Auditor counter-signature

The MS003 multi-sig discipline is enforced at the trust-roots level: BOTH the operator and the auditor must have public keys in `/etc/selfdef/trust-roots/`, and the runtime crate verifies the manifest's `signer_kid` matches the verifying key. Selfdef's current implementation accepts a single MS003-signed manifest where the JSON itself declares both `signer_kid` and `auditor_kid`; future rounds (MS047 R11086) will require a second detached `.auditor.minisig`.

For today's flow: ensure the auditor has separately reviewed the JSON content and that `auditor_kid` corresponds to a key in `/etc/selfdef/trust-roots/`.

### 4. Install the manifest (Ring 0 + MS003-verified)

```bash
sudo selfdefctl perimeter extend --signed /tmp/${EXTID}.json
```

Expected output:

```
perimeter extend: installed extension 'rollout-q2-2026-llm-tools'
  + /opt/llm/inference-server
  + /usr/local/bin/sovereign-restore
  expires_at_ms: <expiry timestamp>
  manifest: /etc/selfdef/perimeter-extensions/rollout-q2-2026-llm-tools.json
  signature: /etc/selfdef/perimeter-extensions/rollout-q2-2026-llm-tools.json.minisig
  NOTE: Tetragon will need to reload — `systemctl reload tetragon.service`.
```

### 5. Reload Tetragon

```bash
sudo systemctl reload tetragon.service \
  || sudo systemctl kill -s HUP tetragon.service
```

### 6. Verify the extension is active

```bash
selfdefctl perimeter show
```

The operator extensions section should list the new id with countdown to expiry.

### 7. Smoke-test the allowlisted binaries

```bash
sudo -u nobody /opt/llm/inference-server --version
selfdefctl perimeter history --limit 1
```

You should see an `EXTEND[...]` verdict — NOT a `SIGKILL`.

## Revocation

```bash
sudo selfdefctl perimeter revoke rollout-q2-2026-llm-tools
sudo systemctl reload tetragon.service
```

Revocation is idempotent — revoking an absent id is a no-op (`exit 0`).

## Validation rejection — diagnostics

The runtime crate refuses extensions that violate these rules (all caught at `extend` time):

| Constraint | Error |
|---|---|
| extension_id non-empty, kebab-case `[a-z0-9-]+` | `extension_id ... must be lowercase-kebab-case` |
| binary_paths absolute (`/...`) | `binary_paths entry ... must be absolute` |
| binary_paths no shell metacharacters / whitespace | `... contains whitespace or shell metacharacters` |
| binary_paths not already in default allowlist | `... already in the verbatim sain-01 §6 default allowlist` |
| reason 1-512 chars | `reason is empty` / `reason exceeds 512 chars` |
| signer_kid != auditor_kid | `signer_kid and auditor_kid must be distinct` |
| TTL ≤ 30 days | `TTL ... exceeds MAX_EXTENSION_TTL_MS` |
| expiry > now | `extension expired (expires_at_ms <= now_ms)` |
| schema_version == "1.0.0" | `schema version mismatch` |
| detached .minisig present + verifies vs trust roots | `signature verification failed` |

## Operator decision tree

- **Need to allowlist >30 days**: split into successive 30-day extensions with explicit re-issuance. The TTL bound is intentional and not waivable in the current schema.
- **Need to allowlist temporarily for a one-shot**: use the shortest TTL that fits (minutes work).
- **Need to bypass a SIGKILL of a binary that has a CVE**: do NOT extend; fix the binary instead. Extensions extend the allowlist, they don't whitewash known-bad code.
- **Lost the operator key**: see [perimeter-key-rotation](perimeter-key-rotation.md).

## Relationships

### Cross-references

- SDD-028 §Deliverable 3 (runtime crate, ExtensionManifest validation)
- SDD-028 §Deliverable 4 (CLI: `selfdefctl perimeter extend --signed <manifest>`)
- MS047 R11077-R11086 (override manifest signing + audit chain)
- MS003 selfdef-signing chain-of-trust
- Sister runbook: [perimeter-key-rotation](perimeter-key-rotation.md)
- Sister runbook: [perimeter-sigkill-investigation](perimeter-sigkill-investigation.md)

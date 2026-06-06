---
title: "Operator runbook — perimeter MS003 key rotation"
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
    note: "Source dump §6 — Tetragon sovereign-kernel-fence + MS003 operator-signed extension contract"
  - id: selfdef-sdd-028
    type: internal
    project: selfdef
    path: docs/sdd/028-perimeter-engine.md
    note: "SDD-028 perimeter-engine specification — Deliverable 3 trust-roots discipline"
  - id: selfdef-ms003
    type: internal
    project: selfdef
    path: backlog/milestones/MS003-correlator-store-responder-signing.md
    note: "MS003 selfdef-signing chain-of-trust"
  - id: selfdef-ms047
    type: internal
    project: selfdef
    path: backlog/milestones/MS047-real-time-security-perimeter-engine-tetragon-kernel-fence.md
    note: "Catalog milestone MS047 R11086 (auditor co-signature) + R11125 (Guardian Daemon)"
tags: [runbook, perimeter, ms003, key-rotation, trust-roots, minisign, operator-key, security, selfdef]
---

# Operator runbook — perimeter MS003 key rotation

## When to use this

Rotate operator / auditor keys when:

- Scheduled rotation cadence (recommended: every 12 months at minimum).
- A key is suspected compromised (laptop loss, supply-chain leak, accidentally committed to a repo).
- Operator personnel change (handover from one operator to another).
- The key was generated under a now-deprecated cipher / parameter set.

Rotation strategy is **dual-control overlap**: new key is added to the trust roots BEFORE the old key is removed. Active extensions signed under the old key remain valid until they expire naturally (≤30 days). Newly issued extensions use the new key.

## Pre-flight inventory

```bash
# Current trust roots.
ls -la /etc/selfdef/trust-roots/

# Active extension manifests + their declared signer_kid.
ls /etc/selfdef/perimeter-extensions/
for f in /etc/selfdef/perimeter-extensions/*.json; do
    [ -f "$f" ] || continue
    echo "=== $f"
    python3 -c "import json; d=json.load(open('$f')); print(f\"  kid={d['signer_kid']} auditor={d['auditor_kid']} exp={d['expires_at_ms']}\")"
done

# Friction-audit overrides also use the same trust roots — inventory those too.
ls /etc/selfdef/overrides/ 2>/dev/null
```

## Procedure (operator key)

### 1. Generate new operator keypair

```bash
# minisign creates two files: <name>.key (private) + <name>.pub (public).
minisign -G -p /tmp/new-operator-2027.pub -s /tmp/new-operator-2027.key
```

The private key file is encrypted at rest with the operator's passphrase. Choose a strong passphrase; minisign does NOT have a remote-attestation surface — the passphrase + the key file are the entire authentication chain.

### 2. Transfer the public key to the host

```bash
# kid convention: <role>-<owner>-<year> or similar stable handle.
NEW_KID="kid-operator-jfortin-2027"
sudo install -m 0644 -o root -g root \
    /tmp/new-operator-2027.pub \
    /etc/selfdef/trust-roots/${NEW_KID}.pub

# (Optional but recommended) verify the kid string written inside the pub key.
cat /etc/selfdef/trust-roots/${NEW_KID}.pub
```

### 3. Issue a test extension signed with the new key

```bash
# Author a 1-hour test extension covering a harmless test path.
NOW_MS="$(date +%s)000"; EXP_MS="$(($(date +%s) + 3600))000"
cat > /tmp/rotation-smoke-test.json <<JSON
{
  "schema_version": "1.0.0",
  "extension_id": "key-rotation-smoke-test-2027",
  "binary_paths": ["/usr/local/bin/sovereign-restore"],
  "reason": "MS003 key rotation smoke test (1h TTL).",
  "issued_at_ms": ${NOW_MS},
  "expires_at_ms": ${EXP_MS},
  "signer_kid": "kid-operator-jfortin-2027",
  "auditor_kid": "kid-auditor-msmith-2026",
  "incident_url": "https://ops.example.com/tickets/rotation-2027"
}
JSON

# Sign with NEW key.
minisign -S -s /tmp/new-operator-2027.key \
    -m /tmp/rotation-smoke-test.json \
    -x /tmp/rotation-smoke-test.json.minisig

# Install.
sudo selfdefctl perimeter extend --signed /tmp/rotation-smoke-test.json
```

If `extend` succeeds, the new key is loaded and verifying correctly. If it fails with `no trust-root in /etc/selfdef/trust-roots validated the signature`, the public key wasn't placed correctly. Verify step 2.

### 4. Revoke the smoke-test extension

```bash
sudo selfdefctl perimeter revoke key-rotation-smoke-test-2027
```

### 5. Update operator runbooks + records

- Update the operator's password manager / key vault with the new key + passphrase.
- Update the `auditor_kid` and `signer_kid` defaults in any internal automation that authors extension JSON.
- Note the rotation in the operator log (verbatim directive: log MS003 key changes; see ~/devops-solutions-information-hub conventions).

### 6. Overlap period (30 days)

For 30 days, BOTH the old and new pub keys live in `/etc/selfdef/trust-roots/`. Any extension still active under the old key continues to validate. After 30 days, all extensions signed under the old key have expired naturally (TTL ≤ 30d).

### 7. Remove the old key

```bash
# After confirming no active extension references the old kid:
for f in /etc/selfdef/perimeter-extensions/*.json; do
    [ -f "$f" ] || continue
    python3 -c "import json; d=json.load(open('$f')); assert d['signer_kid'] != 'kid-operator-jfortin-2026', f'still active: {d}'"
done

# Then:
sudo rm /etc/selfdef/trust-roots/kid-operator-jfortin-2026.pub
```

The old PRIVATE key (`*.key`) should be destroyed per the operator's key-destruction protocol (shred, then verify the storage medium).

## Procedure (auditor key)

Same as operator key, with these differences:

- The auditor's role is review, not extension origination. Their key signs extensions BUT only as the `auditor_kid` field.
- Rotation overlap is the same 30-day window.
- The auditor's private key should live on a separate host / role-isolated keychain from the operator's, to preserve the multi-sig discipline.

## Failure modes

| Symptom | Probable cause | Fix |
|---|---|---|
| `selfdefctl perimeter extend` rejects `signature verification failed` after step 3 | Public key file path wrong, or pub key content corrupted | re-copy /etc/selfdef/trust-roots/<new>.pub |
| Old extension stops verifying after rotation | The old pub key was removed too early | restore the old pub key to /etc/selfdef/trust-roots/ until natural expiry |
| `trust-roots dir missing` | `/etc/selfdef/trust-roots` doesn't exist | `sudo mkdir -p /etc/selfdef/trust-roots; sudo chmod 0750 /etc/selfdef/trust-roots; sudo chown root:selfdef /etc/selfdef/trust-roots` |

## Relationships

### Cross-references

- SDD-028 §Deliverable 3 (runtime crate, ExtensionStore::load_signed → verify_minisign)
- MS003 selfdef-signing chain-of-trust
- MS047 R11086 (auditor co-signature discipline)
- Friction-audit twin runbook: [friction-audit-signature](friction-audit-signature.md) (same trust-roots dir, same minisign discipline)
- Sister runbook: [perimeter-extension-create](perimeter-extension-create.md)

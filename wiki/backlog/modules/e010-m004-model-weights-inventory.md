---
title: "E010 M004 — Model Weights Inventory Tool and Manifest"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 90
progress: 0
stages_completed: [document]
artifacts:
  - tools/inventory_models.sh
  - wiki/spine/references/model-weights-manifest.md
epic: "E010"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e010-storage-and-hardware-enablement
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E010-storage-and-hardware-enablement.md
tags: [module, p1, e010, inventory, models, weights, script, manifest, backup-strategy]
---

# E010 M004 — Model Weights Inventory

## Summary

Provide a repeatable, idempotent way to enumerate everything stored at `/mnt/models/` — file sizes, totals, source URLs, checksum dates — and maintain a manifest page that serves as the "what's here" record plus the recovery plan (what to re-download if /mnt/models is lost). Since weights are public + re-downloadable, backup strategy is light: inventory + URL list, not binary backups.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T043 | Author tools/inventory_models.sh (idempotent, JSON + markdown output) | 90% | 0% | draft |
| T044 | Create wiki/spine/references/model-weights-manifest.md with initial K2.6 Q2 entry | 90% | 0% | draft |

## Dependencies

- **E010 M002** — `/mnt/models` must be mounted for the script to find anything (but script degrades cleanly when mount is empty).
- Python 3.10+ available (script uses Python for JSON emission).

## Done When

- [ ] `tools/inventory_models.sh` exists, is executable, and runs in <10s on an empty `/mnt/models`
- [ ] Script emits a markdown table to stdout AND a JSON file at `/mnt/models/.inventory.json`
- [ ] Each entry: model-name, directory, size (bytes + human), file count, last-modified, source URL (read from a companion `.source.url` file if present), checksum-date (if `.sha256-verified` file present)
- [ ] Script handles empty `/mnt/models` cleanly (reports "no models found") — doesn't crash
- [ ] `wiki/spine/references/model-weights-manifest.md` exists with initial K2.6 Q2 entry + re-download procedure
- [ ] Manifest page cross-references E008 M002 as the download module
- [ ] `python3 -m tools.pipeline post` passes after commit
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Script scaffold

```bash
cd /home/jfortin/devops-solutions-research-wiki
$EDITOR tools/inventory_models.sh
chmod +x tools/inventory_models.sh
shellcheck tools/inventory_models.sh || true
```

Minimum content:

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-/mnt/models}"
OUT_JSON="$ROOT/.inventory.json"

if [[ ! -d "$ROOT" ]]; then
  echo "Inventory root '$ROOT' does not exist or is not a directory. Is /mnt/models mounted?" >&2
  exit 0   # degrade cleanly
fi

python3 - <<PYEOF "$ROOT" "$OUT_JSON"
import os, sys, json, subprocess
from pathlib import Path
from datetime import datetime

root = Path(sys.argv[1])
out_json = Path(sys.argv[2])

entries = []
if root.exists():
    for child in sorted(root.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        size = int(subprocess.check_output(["du", "-sb", str(child)]).split()[0])
        file_count = sum(1 for _ in child.rglob("*") if _.is_file())
        source_url = (child / ".source.url").read_text().strip() if (child / ".source.url").exists() else None
        checksum_date = (child / ".sha256-verified").read_text().strip() if (child / ".sha256-verified").exists() else None
        mtime = datetime.fromtimestamp(child.stat().st_mtime).isoformat()
        entries.append({
            "name": child.name,
            "dir": str(child),
            "size_bytes": size,
            "size_human": f"{size / 1024 / 1024 / 1024:.1f} GB",
            "file_count": file_count,
            "mtime": mtime,
            "source_url": source_url,
            "checksum_date": checksum_date,
        })

out_json.write_text(json.dumps(entries, indent=2))

# Markdown table
print("| Name | Dir | Size | Files | Modified | Source | Verified |")
print("|------|-----|------|-------|----------|--------|----------|")
for e in entries:
    src = e["source_url"] or "—"
    chk = e["checksum_date"] or "—"
    print(f"| {e['name']} | {e['dir']} | {e['size_human']} | {e['file_count']} | {e['mtime'][:10]} | {src} | {chk} |")

if not entries:
    print("_No models found — /mnt/models is empty or not yet populated._")
PYEOF
```

### Step 2 — Author the manifest page

```bash
python3 -m tools.pipeline scaffold reference "model-weights-manifest"
$EDITOR wiki/spine/references/model-weights-manifest.md
```

Outline:

```markdown
# Model Weights Manifest (/mnt/models)

## Summary
Running inventory of model weights stored on /mnt/models (WD_BLACK SN770 NVMe). Weights are re-downloadable, so this page is the recovery plan, not a backup.

## Current inventory
Auto-regenerated by `tools/inventory_models.sh`. Paste fresh table after each major download.

<table auto-inserted after running the script>

## Re-download procedures
### Kimi K2.6 Q2 (unsloth/Kimi-K2.6-GGUF)
See [[e008-m002-k2-6-q2-gguf-download-and-verify]]. Source: https://huggingface.co/unsloth/Kimi-K2.6-GGUF

## Storage accounting
Total used: <X GB of 1 TB capacity>. Headroom: <Y GB>.

## When /mnt/models fills up
Procedure: delete largest entries first, re-download on demand.

## Relationships
- REFERENCED BY: E008 M002, E010 M004
```

### Step 3 — Run script, paste table

```bash
cd /home/jfortin/devops-solutions-research-wiki
./tools/inventory_models.sh /mnt/models >> wiki/spine/references/model-weights-manifest.md
# Manually cut the auto-appended table into the "Current inventory" section.
python3 -m tools.pipeline post
```

## Rollback

```bash
rm tools/inventory_models.sh
rm wiki/spine/references/model-weights-manifest.md
python3 -m tools.pipeline post
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| /mnt/models not mounted yet | dependency | 2026-04-22 | no | Script degrades gracefully; run after E010 M002 |
| Inventory stale vs actual on-disk state | ops | 2026-04-22 | no | Re-run script post every major download; document in routing review ritual |

## Relationships

- PART OF: [[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
- DEPENDS ON: [[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
- PRODUCES: `tools/inventory_models.sh`, `wiki/spine/references/model-weights-manifest.md`

## Backlinks

[[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
[[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
[[`tools/inventory_models.sh`]]
[[`wiki/spine/references/model-weights-manifest.md`]]

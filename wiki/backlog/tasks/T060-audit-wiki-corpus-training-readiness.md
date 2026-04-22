---
title: "T060 — Audit Wiki Corpus Training Readiness (page counts + Q&A shape)"
type: task
domain: backlog
status: done
priority: P2
task_type: task
current_stage: test
readiness: 100
progress: 100
stages_completed: [document, design, scaffold, implement, test]
artifacts:
  - wiki/log/2026-04-23-corpus-training-readiness-audit.md
estimate: S
epic: "E012"
module: "E012-m002"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e012-m002-wiki-assistant-candidate-a
    type: wiki
    file: wiki/backlog/modules/e012-m002-wiki-assistant-candidate-a.md
tags: [task, p2, e012, audit, corpus, wiki, training-data, qa-pairs]
---

# T060 — Audit Wiki Corpus Training Readiness

## Summary

Analyze the current wiki corpus to determine whether it supports training a Wiki-Assistant on ~200-500 SFT pairs without significant hand-curation. Counts pages by type, extracts Q&A-shaped content candidates, identifies gaps. Runnable today — pure Python analysis, no GPU, no external deps.

## Done When

- [ ] Counts by type captured: standards, models, patterns, principles, verbs, references, modules/epics/tasks
- [ ] ≥150 pages classified as "Q&A-shape candidate" (have a clear question → answer mapping in headings + content)
- [ ] Top 5 content-rich categories named (e.g., standards, models, references) with per-category page count
- [ ] Relationship density captured (pages/relationships ratio)
- [ ] Identified gaps: which methodology areas have thin coverage
- [ ] Recommendation recorded: "corpus is ready / marginal / needs expansion before training"
- [ ] Output at `wiki/log/2026-04-23-corpus-training-readiness-audit.md` with tables + recommendation

## Procedure

```bash
cd /home/jfortin/devops-solutions-research-wiki
python3 -m tools.pipeline status

# Detailed counts
python3 <<'PYEOF'
import json
from pathlib import Path
from collections import Counter, defaultdict

manifest_path = Path("wiki-manifest.json")
if not manifest_path.exists():
    import subprocess
    subprocess.run(["python3", "-m", "tools.manifest"], check=True)

with open(manifest_path) as f:
    m = json.load(f)

# Counts by type
types = Counter(p.get("type", "unknown") for p in m["pages"])
print("Counts by type:")
for t, n in types.most_common():
    print(f"  {t}: {n}")

# Counts by domain
domains = Counter(p.get("domain", "unknown") for p in m["pages"])
print("\nCounts by domain:")
for d, n in domains.most_common():
    print(f"  {d}: {n}")

# Counts by status
statuses = Counter(p.get("status", "unknown") for p in m["pages"])
print("\nCounts by status:")
for s, n in statuses.most_common():
    print(f"  {s}: {n}")

# Relationships
rel_count = sum(len(p.get("relationships", [])) for p in m["pages"])
print(f"\nRelationships total: {rel_count}")
print(f"Relationships per page: {rel_count / len(m['pages']):.2f}")
PYEOF

# Scaffold the audit log
python3 -m tools.pipeline scaffold note "2026-04-23-corpus-training-readiness-audit"
$EDITOR wiki/log/2026-04-23-corpus-training-readiness-audit.md
python3 -m tools.pipeline post
```

## Rollback

Read-only audit — nothing destructive. Log page can stay (historical record).

## Relationships

- PART OF: [[e012-m002-wiki-assistant-candidate-a|e012-m002-wiki-assistant-candidate-a]]
- PART OF: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]

## Backlinks

[[e012-m002-wiki-assistant-candidate-a|e012-m002-wiki-assistant-candidate-a]]
[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]

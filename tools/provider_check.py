"""Provider-pricing monitor — fetches current pricing from public endpoints and diffs against a cached snapshot.

Operationalizes the framework's "detect 20% price changes" claim — see
wiki/spine/references/ai-infrastructure-decision-framework-2026.md § Price-Monitoring.

Usage:
    python3 -m tools.provider_check                  # diff against cache; exit 0 if no material change
    python3 -m tools.provider_check --snapshot       # overwrite cache with current pricing (use after review)
    python3 -m tools.provider_check --json           # machine-readable output
    python3 -m tools.provider_check --threshold 0.2  # pct threshold for "material change" (default 20%)

Tracks a watchlist of models (see MODEL_WATCHLIST below). Currently fetches from:
- OpenRouter public /api/v1/models endpoint (no auth needed for public pricing)

Does NOT fetch: Ollama Cloud (no public API for pricing), Anthropic/OpenAI direct
(pricing is published on their sites but not in machine-readable form without scraping).
For those, update the cache manually after verifying via their docs.

Exit codes:
    0 — no material changes OR --snapshot successful
    1 — material changes detected (>threshold); review before accepting
    2 — fetch failed / cache missing / usage error
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

from tools.common import get_project_root

CACHE_PATH_REL = "wiki/config/provider-pricing-cache.json"
OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"

# Models we explicitly track — any change here triggers the diff report.
# Keep in sync with ai-model-provider-harness-decision-matrix-2026.md § Master Matrix.
# All IDs verified against https://openrouter.ai/api/v1/models on 2026-04-23.
MODEL_WATCHLIST = {
    # Open-weight agentic frontier + tiers
    "moonshotai/kimi-k2.6",
    "z-ai/glm-4.7",
    "z-ai/glm-4.7-flash",
    "deepseek/deepseek-v4-pro",       # Opus-class at fraction of Opus cost
    "deepseek/deepseek-v4-flash",     # Cheapest coding-capable on watchlist
    "deepseek/deepseek-v3.2",         # V3 family current
    "deepseek/deepseek-chat-v3.1",    # V3 chat variant (cheap)
    # Closed-weight specialty tiers
    "openai/gpt-5",
    "openai/gpt-5.1",
    "openai/gpt-5.1-codex-mini",
    "openai/gpt-5.1-codex",
    "openai/gpt-5.4",
    "anthropic/claude-opus-4.6",
    "anthropic/claude-opus-4.7",
    "google/gemini-3.1-pro-preview",  # correct OpenRouter ID
    "google/gemini-2.5-pro",          # stable fallback
}

# Provider liveness endpoints — checked by --health subcommand.
# Each entry: (url, method, expected_status_set). 401/403 are OK (means "alive, auth required").
# 404 = endpoint moved / dead. 5xx or timeout = provider impaired.
PROVIDER_HEALTH_ENDPOINTS = {
    "OpenRouter":  ("https://openrouter.ai/api/v1/models", "GET", {200}),
    "OpenAI":      ("https://api.openai.com/v1/models", "GET", {200, 401}),
    "Anthropic":   ("https://api.anthropic.com/v1/models", "GET", {200, 401, 403}),
    "Groq":        ("https://api.groq.com/openai/v1/models", "GET", {200, 401}),
    "Cerebras":    ("https://api.cerebras.ai/v1/models", "GET", {200, 401, 403}),
    "Together":    ("https://api.together.xyz/v1/models", "GET", {200, 401}),
    "Google AI":   ("https://generativelanguage.googleapis.com/v1beta/models", "GET", {200, 401, 403}),
    "DeepSeek":    ("https://api.deepseek.com/v1/models", "GET", {200, 401}),
    "Moonshot":    ("https://api.moonshot.cn/v1/models", "GET", {200, 401}),
    "Z.ai":        ("https://api.z.ai/api/paas/v4/models", "GET", {200, 401, 403}),
    "Ollama Cloud": ("https://ollama.com/", "GET", {200}),
}


def fetch_openrouter_models(timeout: int = 20) -> Dict[str, Dict[str, Any]]:
    """Fetch OpenRouter model catalog. Return {model_id: {"prompt": float, "completion": float, "context_length": int}}."""
    try:
        req = urllib.request.Request(
            OPENROUTER_MODELS_URL,
            headers={"User-Agent": "research-wiki provider-check/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        raise RuntimeError(f"OpenRouter fetch failed: {e}") from e

    data = payload.get("data", [])
    result: Dict[str, Dict[str, Any]] = {}
    for model in data:
        mid = model.get("id", "")
        if not mid:
            continue
        pricing = model.get("pricing", {}) or {}
        # OpenRouter publishes pricing as $/token (string) — convert to $/M tokens (float)
        try:
            prompt = float(pricing.get("prompt", "0") or 0) * 1_000_000
            completion = float(pricing.get("completion", "0") or 0) * 1_000_000
        except (TypeError, ValueError):
            continue
        context = model.get("context_length")
        result[mid] = {
            "prompt_per_m": round(prompt, 4),
            "completion_per_m": round(completion, 4),
            "context_length": context,
        }
    return result


def load_cache(cache_path: Path) -> Optional[Dict[str, Any]]:
    if not cache_path.exists():
        return None
    try:
        return json.loads(cache_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def save_cache(cache_path: Path, data: Dict[str, Any]) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def diff_pricing(
    cached: Dict[str, Dict[str, Any]],
    current: Dict[str, Dict[str, Any]],
    watchlist: set,
    threshold: float,
) -> List[Dict[str, Any]]:
    """Return list of change records. Each record: {model, field, old, new, pct_delta}."""
    changes: List[Dict[str, Any]] = []
    for model_id in sorted(watchlist):
        cur = current.get(model_id)
        old = cached.get(model_id)
        if cur is None and old is None:
            continue
        if cur is None:
            changes.append({
                "model": model_id,
                "kind": "disappeared",
                "old": old,
                "new": None,
                "pct_delta": None,
            })
            continue
        if old is None:
            changes.append({
                "model": model_id,
                "kind": "new",
                "old": None,
                "new": cur,
                "pct_delta": None,
            })
            continue
        for field in ("prompt_per_m", "completion_per_m"):
            old_v = old.get(field) or 0
            new_v = cur.get(field) or 0
            if old_v == 0 and new_v == 0:
                continue
            if old_v == 0:
                pct = float("inf")
            else:
                pct = abs(new_v - old_v) / old_v
            if pct >= threshold or (old_v != new_v and min(old_v, new_v) == 0):
                changes.append({
                    "model": model_id,
                    "kind": "price-change",
                    "field": field,
                    "old": old_v,
                    "new": new_v,
                    "pct_delta": round(pct, 3),
                })
        # Context length change is notable even at small % — report any nonzero delta
        old_ctx = old.get("context_length")
        new_ctx = cur.get("context_length")
        if old_ctx and new_ctx and old_ctx != new_ctx:
            changes.append({
                "model": model_id,
                "kind": "context-change",
                "field": "context_length",
                "old": old_ctx,
                "new": new_ctx,
                "pct_delta": None,
            })
    return changes


def check_health(timeout: int = 10) -> List[Dict[str, Any]]:
    """Ping each provider's public endpoint; report liveness.

    Returns list of records: {provider, url, status, latency_ms, alive, note}.
    - alive=True when status ∈ expected set (200 or 401/403 = "server responding, perhaps needs auth")
    - alive=False on timeout, 5xx, 404, or network error
    """
    import time
    results: List[Dict[str, Any]] = []
    for name, (url, method, expected) in PROVIDER_HEALTH_ENDPOINTS.items():
        rec: Dict[str, Any] = {
            "provider": name,
            "url": url,
            "status": None,
            "latency_ms": None,
            "alive": False,
            "note": "",
        }
        start = time.perf_counter()
        try:
            req = urllib.request.Request(
                url,
                method=method,
                headers={"User-Agent": "research-wiki provider-check/1.0"},
            )
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    rec["status"] = resp.status
            except urllib.error.HTTPError as he:
                rec["status"] = he.code
            latency = (time.perf_counter() - start) * 1000
            rec["latency_ms"] = int(latency)
            if rec["status"] in expected:
                rec["alive"] = True
                rec["note"] = "auth-required" if rec["status"] in (401, 403) else "public"
            else:
                rec["alive"] = False
                rec["note"] = f"unexpected status {rec['status']}"
        except (urllib.error.URLError, TimeoutError) as e:
            rec["latency_ms"] = int((time.perf_counter() - start) * 1000)
            rec["note"] = f"{type(e).__name__}: {e}"
            rec["alive"] = False
        except Exception as e:  # noqa: BLE001
            rec["latency_ms"] = int((time.perf_counter() - start) * 1000)
            rec["note"] = f"{type(e).__name__}: {e}"
            rec["alive"] = False
        results.append(rec)
    return results


def print_health(results: List[Dict[str, Any]]) -> None:
    alive = sum(1 for r in results if r["alive"])
    print(f"Provider Health Check — {alive}/{len(results)} providers reachable")
    for r in results:
        icon = "✅" if r["alive"] else "❌"
        status = str(r["status"]) if r["status"] is not None else "—"
        latency = f"{r['latency_ms']}ms" if r["latency_ms"] is not None else "—"
        print(f"  {icon} {r['provider']:14s}  status={status:4s} latency={latency:>8s}  {r['note']}")


def print_changes(changes: List[Dict[str, Any]], threshold: float) -> None:
    if not changes:
        print(f"  No changes ≥ {threshold*100:.0f}% since last snapshot.")
        return
    print(f"  {len(changes)} change(s) ≥ {threshold*100:.0f}% since last snapshot:")
    for c in changes:
        kind = c["kind"]
        if kind == "disappeared":
            print(f"    - [DISAPPEARED] {c['model']} — was in cache, not in current fetch")
        elif kind == "new":
            n = c["new"]
            print(f"    + [NEW]         {c['model']} — in=${n['prompt_per_m']:.2f}/M out=${n['completion_per_m']:.2f}/M ctx={n.get('context_length')}")
        elif kind == "context-change":
            print(f"    ~ [CONTEXT]     {c['model']} — {c['old']} → {c['new']} tokens")
        elif kind == "price-change":
            pct = c["pct_delta"]
            pct_str = f"{pct*100:+.0f}%" if pct != float("inf") else "new"
            print(f"    ! [PRICE]       {c['model']} {c['field']}: ${c['old']:.2f}/M → ${c['new']:.2f}/M ({pct_str})")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--snapshot", action="store_true", help="Overwrite cache with current pricing (use after operator review)")
    parser.add_argument("--health", action="store_true", help="Run provider-liveness check instead of pricing diff")
    parser.add_argument("--threshold", type=float, default=0.20, help="Fraction threshold for material change (default 0.20 = 20%)")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of text")
    parser.add_argument("--cache", type=Path, default=None, help="Override cache path (default: wiki/config/provider-pricing-cache.json)")
    args = parser.parse_args()

    root = get_project_root()
    cache_path = args.cache if args.cache else root / CACHE_PATH_REL

    if args.health:
        results = check_health()
        if args.json:
            print(json.dumps({"health": results}, indent=2))
        else:
            print_health(results)
        # Exit 1 if ANY provider is down, 0 if all alive
        return 0 if all(r["alive"] for r in results) else 1

    try:
        current = fetch_openrouter_models()
    except RuntimeError as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        return 2

    # Filter to watchlist
    current_watched = {k: v for k, v in current.items() if k in MODEL_WATCHLIST}

    if args.snapshot:
        payload = {
            "schema_version": 1,
            "source": "openrouter:/api/v1/models",
            "snapshot_watchlist": sorted(MODEL_WATCHLIST),
            "models": current_watched,
        }
        save_cache(cache_path, payload)
        print(f"  Snapshot saved: {cache_path} ({len(current_watched)} models)")
        return 0

    cached_payload = load_cache(cache_path)
    if cached_payload is None:
        if args.json:
            print(json.dumps({"error": "cache-missing", "path": str(cache_path)}))
        else:
            print(f"  No cache at {cache_path}. Run with --snapshot to create one.")
        return 2

    cached_models = cached_payload.get("models", {})
    changes = diff_pricing(cached_models, current_watched, MODEL_WATCHLIST, args.threshold)

    if args.json:
        print(json.dumps({
            "cache_path": str(cache_path),
            "threshold": args.threshold,
            "change_count": len(changes),
            "changes": changes,
        }, indent=2))
    else:
        print(f"Provider Pricing Check")
        print(f"  Cache:     {cache_path}")
        print(f"  Current:   {len(current_watched)}/{len(MODEL_WATCHLIST)} watchlist models found on OpenRouter")
        print()
        print_changes(changes, args.threshold)
        if changes:
            print()
            print(f"  After operator review, run --snapshot to accept the new baseline.")

    return 1 if changes else 0


if __name__ == "__main__":
    sys.exit(main())

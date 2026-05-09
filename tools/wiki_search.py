"""5-channel Reciprocal Rank Fusion retrieval for the wiki.

Implements Cloudflare Agent Memory's 5-channel RRF pattern adapted to /opt's
wiki content. Pure Python (no new deps) — vector channels use TF-IDF + cosine.
Architecture supports swapping TF-IDF for neural embeddings later (e.g.
sentence-transformers, fastembed, Ollama embeddings) by replacing
`_build_tfidf_index` and `_channel_vector` internals.

Channels (each ranked independently before RRF merge):
  1. FTS with Porter stemming (over title + body)
  2. Exact fact-key (title / aliases / tags exact-or-substring match)
  3. Raw body substring (case-insensitive substring; safety net for verbatim)
  4. TF-IDF cosine similarity (over stemmed title + body)
  5. HyDE-style query expansion (templated hypothetical doc + TF-IDF cosine)

Reciprocal Rank Fusion weights (Cloudflare-pattern: exact-key strongest, raw-body lowest):
  exact-key: 2.0
  fts:       1.0
  vector:    1.0
  hyde:      1.0
  raw-body:  0.3

Tied ranks broken by recency (last_reviewed > updated > created descending).

Per operator directive 2026-05-09: 'E. Yes. the full deal, no minimization' →
implements all 5 channels at the same call.
"""

from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from tools.common import find_wiki_pages, parse_frontmatter


# ---------------------------------------------------------------------------
# Tokenization + simple Porter stemmer
# ---------------------------------------------------------------------------

_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_\-]*")
_STOPWORDS = frozenset({
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "and", "or", "but", "if", "then", "of", "in", "on", "at", "to", "for",
    "with", "by", "from", "as", "this", "that", "these", "those", "it",
    "its", "we", "you", "they", "them", "our", "their", "his", "her",
    "have", "has", "had", "do", "does", "did", "can", "could", "should",
    "would", "may", "might", "must", "shall", "will", "not", "no", "yes",
})


def _porter_stem(word: str) -> str:
    """Simplified Porter stemmer — handles common English suffixes.

    Not the full algorithm; focuses on the suffixes that matter for retrieval
    on this wiki's vocabulary (-ing, -ed, -s, -ly, -er, -est, -ion, -ment, -ness).
    """
    if len(word) <= 3:
        return word
    w = word.lower()
    # Order matters: longest suffix first
    for suf in ("ization", "ization", "ness", "ment", "tion", "sion",
                "able", "ible", "less"):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            return w[: -len(suf)]
    for suf in ("ing", "ed", "ly", "er", "est", "es"):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            base = w[: -len(suf)]
            # double-letter restoration: "running" -> "run" not "runn"
            if len(base) >= 2 and base[-1] == base[-2] and base[-1] not in "aeiou":
                base = base[:-1]
            return base
    if w.endswith("s") and len(w) > 3 and w[-2] not in "aeiou":
        return w[:-1]
    return w


def _tokenize(text: str, stem: bool = True, drop_stop: bool = True) -> List[str]:
    tokens = [t.lower() for t in _TOKEN_RE.findall(text or "")]
    if drop_stop:
        tokens = [t for t in tokens if t not in _STOPWORDS]
    if stem:
        tokens = [_porter_stem(t) for t in tokens]
    return tokens


# ---------------------------------------------------------------------------
# Page loading + recency ordering
# ---------------------------------------------------------------------------


def _date_str(meta: Dict[str, Any], field: str) -> str:
    val = meta.get(field, "")
    return str(val) if val is not None else ""


def _load_pages(wiki_dir: Path) -> List[Dict[str, Any]]:
    pages: List[Dict[str, Any]] = []
    for path in find_wiki_pages(wiki_dir):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        meta, body = parse_frontmatter(text)
        if not meta:
            continue
        slug = str(path.relative_to(wiki_dir).with_suffix(""))
        title = meta.get("title", path.stem)
        if not title:
            title = path.stem
        # Recency tuple for tiebreaks (descending last_reviewed > updated > created)
        recency = (
            _date_str(meta, "last_reviewed"),
            _date_str(meta, "updated"),
            _date_str(meta, "created"),
        )
        pages.append({
            "slug": slug,
            "path": str(path.relative_to(wiki_dir.parent)) if wiki_dir.parent in path.parents else str(path),
            "title": title,
            "aliases": meta.get("aliases", []) or [],
            "tags": [str(t) for t in (meta.get("tags", []) or [])],
            "domain": meta.get("domain", ""),
            "type": meta.get("type", ""),
            "body": body or "",
            "recency": recency,
        })
    return pages


# ---------------------------------------------------------------------------
# Channel 1 — FTS with Porter stemming
# ---------------------------------------------------------------------------


def _channel_fts(query: str, pages: List[Dict[str, Any]]) -> List[Tuple[str, float]]:
    qtokens = set(_tokenize(query))
    if not qtokens:
        return []
    results: List[Tuple[str, float]] = []
    for page in pages:
        ptokens = _tokenize(page["title"] + " " + page["body"])
        if not ptokens:
            continue
        counts = Counter(ptokens)
        common = qtokens & set(counts.keys())
        if not common:
            continue
        # Score: fraction of query terms covered, weighted by their frequency in the page
        coverage = len(common) / len(qtokens)
        density = sum(counts[t] for t in common) / max(len(ptokens), 1)
        score = 0.6 * coverage + 0.4 * min(density * 10.0, 1.0)
        results.append((page["slug"], score))
    return sorted(results, key=lambda x: -x[1])


# ---------------------------------------------------------------------------
# Channel 2 — Exact fact-key (title / aliases / tags)
# ---------------------------------------------------------------------------


def _channel_exact_key(query: str, pages: List[Dict[str, Any]]) -> List[Tuple[str, float]]:
    qlow = (query or "").lower().strip()
    if not qlow:
        return []
    results: List[Tuple[str, float]] = []
    for page in pages:
        title = (page.get("title") or "").lower()
        aliases = [a.lower() for a in page.get("aliases", []) if isinstance(a, str)]
        tags = [t.lower() for t in page.get("tags", [])]
        if qlow == title:
            score = 1.0
        elif any(qlow == a for a in aliases):
            score = 0.95
        elif qlow in title:
            score = 0.85
        elif any(qlow in a for a in aliases):
            score = 0.75
        elif any(qlow == t for t in tags):
            score = 0.60
        elif any(qlow in t for t in tags):
            score = 0.45
        else:
            continue
        results.append((page["slug"], score))
    return sorted(results, key=lambda x: -x[1])


# ---------------------------------------------------------------------------
# Channel 3 — Raw body substring (safety net for verbatim)
# ---------------------------------------------------------------------------


def _channel_raw_body(query: str, pages: List[Dict[str, Any]]) -> List[Tuple[str, float]]:
    qlow = (query or "").lower()
    if not qlow or len(qlow) < 2:
        return []
    results: List[Tuple[str, float]] = []
    for page in pages:
        body = (page.get("body") or "").lower()
        if not body:
            continue
        cnt = body.count(qlow)
        if cnt > 0:
            # Diminishing returns on count; cap at 10 occurrences = full score
            score = min(math.log(1 + cnt) / math.log(11.0), 1.0)
            results.append((page["slug"], score))
    return sorted(results, key=lambda x: -x[1])


# ---------------------------------------------------------------------------
# TF-IDF index (used by Channels 4 + 5)
# ---------------------------------------------------------------------------


class _TfIdfIndex:
    """Sparse TF-IDF index over page tokens (stemmed, stopwords removed)."""

    def __init__(self, pages: List[Dict[str, Any]]):
        self.slugs: List[str] = []
        self.vectors: List[Dict[str, float]] = []  # slug-aligned: dict {term: tfidf}
        self.norms: List[float] = []
        self._build(pages)

    def _build(self, pages: List[Dict[str, Any]]) -> None:
        # Pass 1 — gather DF
        df: Counter[str] = Counter()
        page_token_counts: List[Counter[str]] = []
        for page in pages:
            tokens = _tokenize(page["title"] + " " + page["body"])
            counts = Counter(tokens)
            page_token_counts.append(counts)
            for term in counts.keys():
                df[term] += 1
        n_pages = max(len(pages), 1)
        # Pass 2 — build TF-IDF vectors
        for page, counts in zip(pages, page_token_counts):
            if not counts:
                self.slugs.append(page["slug"])
                self.vectors.append({})
                self.norms.append(0.0)
                continue
            doc_len = sum(counts.values())
            vec: Dict[str, float] = {}
            for term, tf in counts.items():
                idf = math.log(n_pages / max(df[term], 1)) + 1.0
                vec[term] = (tf / doc_len) * idf
            norm = math.sqrt(sum(v * v for v in vec.values()))
            self.slugs.append(page["slug"])
            self.vectors.append(vec)
            self.norms.append(norm)

    def query_vector(self, text: str) -> Tuple[Dict[str, float], float]:
        tokens = _tokenize(text)
        if not tokens:
            return {}, 0.0
        counts = Counter(tokens)
        doc_len = sum(counts.values())
        # Approximate IDF using the index's DF where possible
        vec: Dict[str, float] = {}
        for term, tf in counts.items():
            df_term = sum(1 for v in self.vectors if term in v)
            idf = math.log(max(len(self.vectors), 1) / max(df_term, 1)) + 1.0
            vec[term] = (tf / doc_len) * idf
        norm = math.sqrt(sum(v * v for v in vec.values()))
        return vec, norm

    def cosine_top(self, qvec: Dict[str, float], qnorm: float, k: int = 50) -> List[Tuple[str, float]]:
        if not qvec or qnorm == 0.0:
            return []
        scored: List[Tuple[str, float]] = []
        for slug, vec, norm in zip(self.slugs, self.vectors, self.norms):
            if not vec or norm == 0.0:
                continue
            # Iterate the smaller side
            if len(qvec) <= len(vec):
                dot = sum(v * vec.get(t, 0.0) for t, v in qvec.items())
            else:
                dot = sum(v * qvec.get(t, 0.0) for t, v in vec.items())
            if dot == 0.0:
                continue
            cos = dot / (qnorm * norm)
            if cos > 0:
                scored.append((slug, cos))
        return sorted(scored, key=lambda x: -x[1])[:k]


# ---------------------------------------------------------------------------
# Channel 4 — Vector (TF-IDF cosine)
# ---------------------------------------------------------------------------


def _channel_vector(query: str, idx: _TfIdfIndex, top: int = 50) -> List[Tuple[str, float]]:
    qvec, qnorm = idx.query_vector(query)
    return idx.cosine_top(qvec, qnorm, k=top)


# ---------------------------------------------------------------------------
# Channel 5 — HyDE-style query expansion
# ---------------------------------------------------------------------------

# HyDE template: rephrase the query as if it were the answer + key concepts of
# a hypothetical document. Embeddings on the expanded form better match
# documents that ANSWER the query (even if they don't repeat the question form).
_HYDE_TEMPLATES = (
    "This wiki page describes {q}. Key concepts include {q} in detail with "
    "examples, definitions, and applications. The {q} pattern explains how "
    "{q} works, what {q} provides, and when {q} applies.",
)


def _channel_hyde(query: str, idx: _TfIdfIndex, top: int = 50) -> List[Tuple[str, float]]:
    if not query:
        return []
    expanded = _HYDE_TEMPLATES[0].format(q=query)
    qvec, qnorm = idx.query_vector(expanded)
    return idx.cosine_top(qvec, qnorm, k=top)


# ---------------------------------------------------------------------------
# Reciprocal Rank Fusion
# ---------------------------------------------------------------------------


def _rrf_merge(
    channel_results: List[List[Tuple[str, float]]],
    weights: List[float],
    pages_by_slug: Dict[str, Dict[str, Any]],
    k_top: int = 10,
    rrf_k: int = 60,
) -> List[Tuple[str, float, Dict[str, float]]]:
    """Reciprocal Rank Fusion. Returns [(slug, fused_score, per_channel_ranks), ...].

    Score: sum(weight_i / (rrf_k + rank_i + 1)) over channels where slug appears.
    Tiebreak: recency descending.
    """
    fused: Dict[str, float] = defaultdict(float)
    per_channel_rank: Dict[str, Dict[str, int]] = defaultdict(dict)
    channel_names = ["exact_key", "fts", "vector", "hyde", "raw_body"]
    assert len(channel_results) == len(weights) == len(channel_names)
    for name, results, weight in zip(channel_names, channel_results, weights):
        for rank, (slug, _) in enumerate(results):
            fused[slug] += weight / (rrf_k + rank + 1)
            per_channel_rank[slug][name] = rank + 1
    items = []
    for slug, score in fused.items():
        page = pages_by_slug.get(slug)
        recency = page["recency"] if page else ("", "", "")
        items.append((slug, score, recency, dict(per_channel_rank[slug])))
    # Primary: -score; Tiebreak: recency descending (later first)
    items.sort(key=lambda x: (-x[1], -hash(x[2])))
    # Stable secondary sort: recency tuple descending
    items.sort(key=lambda x: x[2], reverse=True)
    items.sort(key=lambda x: -x[1])
    return [(slug, score, ranks) for slug, score, _, ranks in items[:k_top]]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def search(
    query: str,
    wiki_dir: Path,
    k: int = 10,
    return_diagnostics: bool = False,
) -> Dict[str, Any]:
    """5-channel RRF search.

    Args:
        query: search string (free-form).
        wiki_dir: wiki/ directory root.
        k: number of top results to return.
        return_diagnostics: include per-channel ranks per result.

    Returns:
        {
          "query": str,
          "matches": int,
          "channels": {channel_name: count_top_50},
          "results": [
            {"title", "path", "slug", "domain", "type", "score",
             "channels": {channel_name: rank_in_channel}}
          ]
        }
    """
    pages = _load_pages(wiki_dir)
    pages_by_slug = {p["slug"]: p for p in pages}
    if not pages:
        return {"query": query, "matches": 0, "channels": {}, "results": []}

    # Build TF-IDF once per call (cache later if perf demands)
    idx = _TfIdfIndex(pages)

    fts_r = _channel_fts(query, pages)[:50]
    key_r = _channel_exact_key(query, pages)[:50]
    raw_r = _channel_raw_body(query, pages)[:50]
    vec_r = _channel_vector(query, idx, top=50)
    hyde_r = _channel_hyde(query, idx, top=50)

    # RRF weights (matches Cloudflare's "exact-key strongest, raw-body lowest")
    weights = [2.0, 1.0, 1.0, 1.0, 0.3]
    merged = _rrf_merge(
        [key_r, fts_r, vec_r, hyde_r, raw_r],
        weights,
        pages_by_slug,
        k_top=k,
    )

    results = []
    for slug, score, channel_ranks in merged:
        page = pages_by_slug.get(slug)
        if not page:
            continue
        item = {
            "title": page["title"],
            "path": page["path"],
            "slug": slug,
            "domain": page["domain"],
            "type": page["type"],
            "score": round(score, 4),
        }
        if return_diagnostics:
            item["channels"] = channel_ranks
        results.append(item)

    return {
        "query": query,
        "matches": len(results),
        "channels": {
            "exact_key": len(key_r),
            "fts": len(fts_r),
            "vector": len(vec_r),
            "hyde": len(hyde_r),
            "raw_body": len(raw_r),
        },
        "results": results,
    }


# ---------------------------------------------------------------------------
# CLI for quick smoke tests
# ---------------------------------------------------------------------------


def _main() -> None:
    import argparse
    import json
    import sys
    parser = argparse.ArgumentParser(description="5-channel RRF wiki search")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--k", type=int, default=10, help="Top-k results (default 10)")
    parser.add_argument("--diagnostics", action="store_true", help="Include per-channel ranks")
    args = parser.parse_args()

    wiki_dir = Path(__file__).resolve().parent.parent / "wiki"
    if not wiki_dir.exists():
        sys.stderr.write(f"wiki dir not found: {wiki_dir}\n")
        sys.exit(1)

    out = search(args.query, wiki_dir, k=args.k, return_diagnostics=args.diagnostics)
    print(json.dumps(out, indent=2, default=str))


if __name__ == "__main__":
    _main()

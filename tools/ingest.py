"""Automated source ingestion pipeline.

Fetches content from URLs (YouTube, GitHub, PDF, web), saves to raw/,
and reports what was captured for wiki processing.

Usage:
    python3 tools/ingest.py URL [URL...]           # Fetch one or more URLs
    python3 tools/ingest.py --batch file.txt        # Fetch URLs from a file (one per line)
    python3 tools/ingest.py --list-raw              # List unprocessed files in raw/

Supported sources:
    - YouTube videos → extracts transcript automatically (raw/transcripts/)
    - GitHub repos/gists → fetches README + key files via deep tree fetch (raw/articles/)
    - PDFs (including arxiv.org/pdf/) → extracts text via pypdf; arxiv URLs get
      enriched with clean title/authors/abstract from the /abs/ page (raw/papers/)
    - Web pages → fetches main content with HTML stripped (raw/articles/)
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from tools.common import detect_source_type, get_project_root


def _slugify(text: str) -> str:
    """Convert text to kebab-case slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80].strip("-")


def _extract_youtube_id(url: str) -> Optional[str]:
    """Extract video ID from YouTube URL."""
    patterns = [
        r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def _fetch_youtube_transcript(video_id: str) -> Tuple[str, str]:
    """Fetch YouTube transcript. Returns (transcript_text, video_title)."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        raise RuntimeError("youtube-transcript-api not installed. Run: pip3 install youtube-transcript-api")

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)

    # Join all snippets into one text
    lines = [snippet.text for snippet in transcript.snippets]
    text = " ".join(lines)

    # Try to get video title from the transcript metadata or use ID
    title = f"YouTube video {video_id}"

    # Try fetching the page to get the title
    try:
        req = urllib.request.Request(
            f"https://www.youtube.com/watch?v={video_id}",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            match = re.search(r"<title>(.*?)</title>", html)
            if match:
                title = match.group(1).replace(" - YouTube", "").strip()
    except Exception:
        pass

    return text, title


def _fetch_github_content(url: str) -> Tuple[str, str, str]:
    """Fetch GitHub repo README or gist content. Returns (content, title, source_type)."""
    # Gist
    if "gist.github.com" in url:
        # Extract gist ID
        parts = url.rstrip("/").split("/")
        gist_id = parts[-1]
        api_url = f"https://api.github.com/gists/{gist_id}"
        req = urllib.request.Request(api_url, headers={
            "User-Agent": "research-wiki-ingest",
            "Accept": "application/vnd.github.v3+json",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        title = data.get("description", f"Gist {gist_id}")
        files = data.get("files", {})
        content_parts = []
        for fname, fdata in files.items():
            content_parts.append(f"# {fname}\n\n{fdata.get('content', '')}")
        return "\n\n---\n\n".join(content_parts), title, "documentation"

    # Regular GitHub repo
    # Extract owner/repo
    match = re.match(r"https?://github\.com/([^/]+)/([^/]+)", url)
    if not match:
        raise ValueError(f"Cannot parse GitHub URL: {url}")

    owner, repo = match.group(1), match.group(2).rstrip("/")
    title = f"{owner}/{repo}"

    # Use gh CLI for richer content if available
    gh_available = subprocess.run(
        ["which", "gh"], capture_output=True
    ).returncode == 0

    content_parts = []

    # 1. Fetch README
    try:
        api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
        req = urllib.request.Request(api_url, headers={
            "User-Agent": "research-wiki-ingest",
            "Accept": "application/vnd.github.v3+json",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        import base64
        readme = base64.b64decode(data.get("content", "")).decode("utf-8")
        content_parts.append(f"# README\n\n{readme}")
    except urllib.error.HTTPError:
        # No README — try repo description
        try:
            api_url = f"https://api.github.com/repos/{owner}/{repo}"
            req = urllib.request.Request(api_url, headers={
                "User-Agent": "research-wiki-ingest",
                "Accept": "application/vnd.github.v3+json",
            })
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            content_parts.append(f"# {title}\n\n{data.get('description', 'No description')}")
        except Exception:
            content_parts.append(f"# {title}\n\n(No README available)")

    # 2. Fetch repo tree to find key documentation files
    key_patterns = [
        ".md", ".yaml", ".yml", ".json",  # docs and configs
    ]
    skip_dirs = {
        "node_modules", ".git", "dist", "build", "__pycache__",
        ".venv", "vendor", ".github/workflows",
    }
    # Directories likely to have important content
    priority_dirs = {
        "docs", "spec", "specs", "templates", "standards",
        "methodology", "src", "lib", "config", "prompts",
        "agents", "skills", "rules",
    }

    try:
        api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/main?recursive=1"
        req = urllib.request.Request(api_url, headers={
            "User-Agent": "research-wiki-ingest",
            "Accept": "application/vnd.github.v3+json",
        })
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                tree_data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError:
            # Try master branch if main doesn't exist
            api_url = api_url.replace("/main?", "/master?")
            req = urllib.request.Request(api_url, headers={
                "User-Agent": "research-wiki-ingest",
                "Accept": "application/vnd.github.v3+json",
            })
            with urllib.request.urlopen(req, timeout=15) as resp:
                tree_data = json.loads(resp.read().decode("utf-8"))

        # Filter for important files
        important_files = []
        for item in tree_data.get("tree", []):
            if item["type"] != "blob":
                continue
            path = item["path"]
            # Skip vendored/build dirs
            if any(skip in path for skip in skip_dirs):
                continue
            # Skip README (already fetched)
            if path.lower() in ("readme.md", "readme.rst", "readme.txt"):
                continue
            # Include markdown and config files in priority dirs
            parts = path.split("/")
            in_priority = any(p.lower() in priority_dirs for p in parts[:-1])
            is_root_md = len(parts) == 1 and path.endswith(".md")
            is_root_config = len(parts) == 1 and path.endswith((".yaml", ".yml"))
            is_priority_file = in_priority and any(path.endswith(ext) for ext in key_patterns)

            if is_root_md or is_root_config or is_priority_file:
                important_files.append(path)

        # Fetch up to 30 key files (avoid rate limits)
        fetched_count = 0
        for fpath in sorted(important_files)[:30]:
            try:
                file_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{fpath}"
                req = urllib.request.Request(file_url, headers={
                    "User-Agent": "research-wiki-ingest",
                    "Accept": "application/vnd.github.v3+json",
                })
                with urllib.request.urlopen(req, timeout=10) as resp:
                    fdata = json.loads(resp.read().decode("utf-8"))
                import base64
                file_content = base64.b64decode(fdata.get("content", "")).decode("utf-8")
                content_parts.append(f"\n\n---\n\n# FILE: {fpath}\n\n{file_content}")
                fetched_count += 1
            except Exception:
                continue  # Skip files that can't be fetched

        if fetched_count > 0:
            content_parts.insert(1, f"\n\n> **Deep fetch: {fetched_count} key files fetched beyond README.**\n")

    except Exception:
        pass  # Tree fetch failed — we still have the README

    return "\n".join(content_parts), title, "documentation"


def _fetch_web_page(url: str) -> Tuple[str, str]:
    """Fetch a web page and extract main text content. Returns (content, title)."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")

    # Extract title
    title_match = re.search(r"<title>(.*?)</title>", html, re.DOTALL)
    title = title_match.group(1).strip() if title_match else url

    # Strip HTML tags (basic — good enough for ingestion)
    text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text, title


def _extract_arxiv_id(url: str) -> Optional[str]:
    """Extract arxiv ID from a /pdf/ or /abs/ URL. Returns None if not arxiv.

    Handles both old-style (cs/0307010) and new-style (2603.25723) IDs,
    optional version suffix (v1, v2, ...).
    """
    # New-style: YYMM.NNNNN with optional version
    match = re.search(r"arxiv\.org/(?:pdf|abs)/(\d{4}\.\d{4,5})(?:v\d+)?", url)
    if match:
        return match.group(1)
    # Old-style: category/YYMMNNN
    match = re.search(r"arxiv\.org/(?:pdf|abs)/([a-z\-]+/\d{7})(?:v\d+)?", url)
    if match:
        return match.group(1)
    return None


def _fetch_arxiv_metadata(arxiv_id: str) -> Optional[Dict[str, str]]:
    """Fetch clean title/authors/abstract from arxiv /abs/ page.

    PDF text extraction often produces noisy headers; the abs page has clean
    structured metadata. Returns None on any failure (caller falls back to
    PDF-extracted title).
    """
    abs_url = f"https://arxiv.org/abs/{arxiv_id}"
    try:
        req = urllib.request.Request(abs_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception:
        return None

    result: Dict[str, str] = {}

    # Title from <meta name="citation_title">
    title_match = re.search(r'<meta name="citation_title" content="([^"]+)"', html)
    if title_match:
        result["title"] = title_match.group(1).strip()

    # Authors from repeated <meta name="citation_author">
    authors = re.findall(r'<meta name="citation_author" content="([^"]+)"', html)
    if authors:
        result["authors"] = ", ".join(authors)

    # Abstract from <blockquote class="abstract">
    abstract_match = re.search(
        r'<blockquote class="abstract[^"]*">(.*?)</blockquote>',
        html,
        re.DOTALL,
    )
    if abstract_match:
        abstract = abstract_match.group(1)
        # Strip "Abstract:" descriptor span and remaining HTML
        abstract = re.sub(r'<span class="descriptor">[^<]+</span>', "", abstract)
        abstract = re.sub(r"<[^>]+>", " ", abstract)
        abstract = re.sub(r"\s+", " ", abstract).strip()
        if abstract:
            result["abstract"] = abstract

    return result if result else None


def _fetch_pdf(url: str) -> Tuple[str, str]:
    """Fetch a PDF and extract text page-by-page.

    Returns (content, title). Title comes from PDF metadata when available,
    otherwise the first non-empty content line, otherwise the URL.

    Page boundaries are preserved as ``## Page N`` headers so a synthesizing
    agent can cite specific pages and so the output stays readable for human
    review when the PDF is long (academic papers, specs).
    """
    import io

    try:
        from pypdf import PdfReader
    except ImportError:
        raise RuntimeError(
            "pypdf not installed. Run: pip3 install pypdf "
            "(or pip3 install -r requirements.txt)"
        )

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        pdf_bytes = resp.read()

    reader = PdfReader(io.BytesIO(pdf_bytes))

    title: Optional[str] = None
    if reader.metadata and getattr(reader.metadata, "title", None):
        candidate = str(reader.metadata.title).strip()
        if candidate:
            title = candidate

    page_texts = []
    for i, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text()
        except Exception:
            text = None
        if text and text.strip():
            page_texts.append(f"## Page {i}\n\n{text.strip()}")

    content = "\n\n".join(page_texts).strip()

    # Fallback title: first content line (skipping page headers we just inserted)
    if not title and content:
        for line in content.split("\n"):
            line = line.strip()
            if line and not line.startswith("##"):
                title = line[:120]
                break

    if not title:
        title = url

    return content, title


def classify_url(url: str) -> str:
    """Classify a URL into a source type."""
    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"
    if "github.com" in url or "gist.github.com" in url:
        return "github"
    if url.lower().endswith(".pdf") or "arxiv.org/pdf/" in url.lower():
        return "pdf"
    return "web"


def ingest_url(url: str, project_root: Path) -> Dict[str, Any]:
    """Ingest a single URL. Fetches content, saves to raw/, returns metadata."""
    url_type = classify_url(url)
    result = {
        "url": url,
        "type": url_type,
        "status": "error",
        "file": None,
        "title": None,
        "error": None,
    }

    try:
        if url_type == "youtube":
            video_id = _extract_youtube_id(url)
            if not video_id:
                result["error"] = f"Cannot extract video ID from: {url}"
                return result

            content, title = _fetch_youtube_transcript(video_id)
            slug = _slugify(title) or video_id
            raw_dir = project_root / "raw" / "transcripts"
            raw_file = raw_dir / f"{slug}.txt"

            # Add metadata header
            full_content = f"# {title}\n\nSource: {url}\nIngested: {datetime.now().isoformat()[:10]}\nType: youtube-transcript\n\n---\n\n{content}"

        elif url_type == "github":
            content, title, src_type = _fetch_github_content(url)
            slug = _slugify(title)
            raw_dir = project_root / "raw" / "articles"
            raw_file = raw_dir / f"{slug}.md"

            full_content = f"# {title}\n\nSource: {url}\nIngested: {datetime.now().isoformat()[:10]}\nType: {src_type}\n\n---\n\n{content}"

        elif url_type == "pdf":
            content, title = _fetch_pdf(url)

            # Arxiv enrichment: prepend clean metadata block when available.
            # Generic PDF flow above always works; arxiv enrichment is a
            # source-specific quality layer on top, not a requirement.
            arxiv_id = _extract_arxiv_id(url)
            if arxiv_id:
                meta = _fetch_arxiv_metadata(arxiv_id)
                if meta:
                    if meta.get("title"):
                        title = meta["title"]
                    meta_lines = [f"**arxiv ID:** {arxiv_id}"]
                    if meta.get("title"):
                        meta_lines.append(f"**Title:** {meta['title']}")
                    if meta.get("authors"):
                        meta_lines.append(f"**Authors:** {meta['authors']}")
                    if meta.get("abstract"):
                        meta_lines.append(f"**Abstract:** {meta['abstract']}")
                    content = "\n\n".join(meta_lines) + "\n\n---\n\n" + content

            slug = _slugify(title)
            raw_dir = project_root / "raw" / "papers"
            raw_file = raw_dir / f"{slug}.md"

            full_content = f"# {title}\n\nSource: {url}\nIngested: {datetime.now().isoformat()[:10]}\nType: paper\n\n---\n\n{content}"

        else:
            content, title = _fetch_web_page(url)
            slug = _slugify(title)
            raw_dir = project_root / "raw" / "articles"
            raw_file = raw_dir / f"{slug}.md"

            full_content = f"# {title}\n\nSource: {url}\nIngested: {datetime.now().isoformat()[:10]}\nType: article\n\n---\n\n{content}"

        # Write to raw/
        raw_dir.mkdir(parents=True, exist_ok=True)

        # Don't overwrite existing files
        if raw_file.exists():
            result["status"] = "skipped"
            result["file"] = str(raw_file.relative_to(project_root))
            result["title"] = title
            result["error"] = "File already exists"
            return result

        raw_file.write_text(full_content, encoding="utf-8")

        result["status"] = "fetched"
        result["file"] = str(raw_file.relative_to(project_root))
        result["title"] = title

    except Exception as e:
        result["error"] = str(e)

    return result


def list_raw(project_root: Path) -> List[Dict[str, str]]:
    """List all files in raw/ with their types."""
    raw_dir = project_root / "raw"
    files = []
    for subdir in ["transcripts", "articles", "papers", "notes", "dumps"]:
        d = raw_dir / subdir
        if d.exists():
            for f in sorted(d.iterdir()):
                if f.is_file() and f.name != ".gitkeep":
                    files.append({
                        "path": str(f.relative_to(project_root)),
                        "type": subdir,
                        "name": f.name,
                        "size": f.stat().st_size,
                    })
    return files


def main():
    parser = argparse.ArgumentParser(description="Ingest sources from URLs into raw/")
    parser.add_argument("urls", nargs="*", help="URLs to ingest")
    parser.add_argument("--batch", help="File containing URLs (one per line)")
    parser.add_argument("--list-raw", action="store_true", help="List unprocessed raw files")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    root = get_project_root()

    if args.list_raw:
        files = list_raw(root)
        if args.json:
            print(json.dumps(files, indent=2))
        else:
            print(f"Raw files ({len(files)}):")
            for f in files:
                print(f"  [{f['type']}] {f['name']} ({f['size']} bytes)")
        return

    urls = list(args.urls)
    if args.batch:
        batch_file = Path(args.batch)
        if batch_file.exists():
            for line in batch_file.read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#"):
                    urls.append(line)

    if not urls:
        parser.print_help()
        sys.exit(1)

    results = []
    for url in urls:
        print(f"Ingesting: {url}...")
        result = ingest_url(url, root)
        results.append(result)

        if result["status"] == "fetched":
            print(f"  OK: {result['title']} → {result['file']}")
        elif result["status"] == "skipped":
            print(f"  SKIP: {result['file']} (already exists)")
        else:
            print(f"  ERROR: {result['error']}")

    fetched = sum(1 for r in results if r["status"] == "fetched")
    skipped = sum(1 for r in results if r["status"] == "skipped")
    errors = sum(1 for r in results if r["status"] == "error")

    print(f"\nDone: {fetched} fetched, {skipped} skipped, {errors} errors")

    if args.json:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()

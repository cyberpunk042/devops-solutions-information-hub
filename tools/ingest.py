"""Automated source ingestion pipeline.

Fetches content from URLs (YouTube, GitHub, web), saves to raw/,
and reports what was captured for wiki processing.

Usage:
    python3 tools/ingest.py URL [URL...]           # Fetch one or more URLs
    python3 tools/ingest.py --batch file.txt        # Fetch URLs from a file (one per line)
    python3 tools/ingest.py --list-raw              # List unprocessed files in raw/

Supported sources:
    - YouTube videos → extracts transcript automatically
    - GitHub repos/gists → fetches README or gist content
    - Web pages → fetches main content
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
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    req = urllib.request.Request(api_url, headers={
        "User-Agent": "research-wiki-ingest",
        "Accept": "application/vnd.github.v3+json",
    })

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        import base64
        content = base64.b64decode(data.get("content", "")).decode("utf-8")
        title = f"{owner}/{repo}"
        return content, title, "documentation"
    except urllib.error.HTTPError:
        # No README, try fetching repo description
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        req = urllib.request.Request(api_url, headers={
            "User-Agent": "research-wiki-ingest",
            "Accept": "application/vnd.github.v3+json",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        desc = data.get("description", "No description")
        title = f"{owner}/{repo}"
        return f"# {title}\n\n{desc}\n", title, "documentation"


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


def classify_url(url: str) -> str:
    """Classify a URL into a source type."""
    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"
    if "github.com" in url or "gist.github.com" in url:
        return "github"
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

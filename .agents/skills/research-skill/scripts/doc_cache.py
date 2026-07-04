#!/usr/bin/env python3
"""HTTP doc fetch with ETag/Last-Modified revalidation cache. Stdlib only.

Adapted from addyosmani/agent-skills hooks/sdd-cache-{pre,post}.sh (MIT).
Freshness: serve cache only on HTTP 304. No TTL. URL-keyed; prompt stored as metadata.

Cache directory: .agents/cache/doc-fetch/
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_CACHE = Path(".agents/cache/doc-fetch")
USER_AGENT = "agent-loom-doc-cache/1.0"


def url_key(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:32]


def cache_path(cache_dir: Path, url: str) -> Path:
    return cache_dir / f"{url_key(url)}.json"


def _header(headers, name: str) -> str:
    return (headers.get(name) or headers.get(name.lower()) or "").strip()


def head_validators(url: str) -> tuple[str, str]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return _header(resp.headers, "ETag"), _header(resp.headers, "Last-Modified")
    except urllib.error.HTTPError as e:
        return _header(e.headers, "ETag"), _header(e.headers, "Last-Modified")


def revalidate(url: str, etag: str, last_mod: str) -> int:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    if etag:
        req.add_header("If-None-Match", etag)
    if last_mod:
        req.add_header("If-Modified-Since", last_mod)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code


def fetch_body(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
        ctype = resp.headers.get("Content-Type", "")
        charset = "utf-8"
        if "charset=" in ctype.lower():
            charset = ctype.lower().split("charset=")[-1].split(";")[0].strip()
        return raw.decode(charset, errors="replace")


def load_entry(path: Path) -> dict | None:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def save_entry(path: Path, entry: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(f"{path}.tmp")
    tmp.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def fetch(url: str, *, prompt: str = "", cache_dir: Path = DEFAULT_CACHE) -> tuple[str, bool, str]:
    """Return (content, from_cache, status_line)."""
    cp = cache_path(cache_dir, url)
    entry = load_entry(cp)
    etag = entry.get("etag", "") if entry else ""
    last_mod = entry.get("last_modified", "") if entry else ""

    if entry and (etag or last_mod):
        status = revalidate(url, etag, last_mod)
        if status == 304:
            iso = entry.get("fetched_at_iso", "unknown")
            note = f"[doc-cache] Cache hit (HTTP 304) for {url} — unchanged since {iso}"
            if entry.get("prompt"):
                note += f". Original prompt: {entry['prompt']!r}"
            return entry.get("content", ""), True, note

    content = fetch_body(url)
    etag, last_mod = head_validators(url)
    if not etag and not last_mod:
        return content, False, f"[doc-cache] Fetched {url} — not cached (no ETag/Last-Modified)"

    now = int(time.time())
    iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    save_entry(
        cp,
        {
            "url": url,
            "prompt": prompt,
            "etag": etag,
            "last_modified": last_mod,
            "content": content,
            "fetched_at": now,
            "fetched_at_iso": iso,
        },
    )
    return content, False, f"[doc-cache] Fetched and cached {url}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch URL with ETag revalidation cache")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--prompt", default="", help="Original extraction prompt (metadata only)")
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--json", action="store_true", help="Emit JSON metadata + content")
    args = parser.parse_args()

    content, cached, note = fetch(args.url, prompt=args.prompt, cache_dir=args.cache_dir)
    if args.json:
        print(
            json.dumps(
                {"url": args.url, "cached": cached, "note": note, "bytes": len(content), "content": content},
                ensure_ascii=False,
            )
        )
        return 0

    print(note, file=sys.stderr)
    sys.stdout.write(content)
    if content and not content.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

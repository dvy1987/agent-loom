#!/usr/bin/env python3
"""
preflight.py — Verify deploy.yml and required secrets exist before deploy.

Usage:
    python scripts/preflight.py [.agent-loom/deploy.yml]

Exit codes:
    0 — ready
    1 — config/secrets missing (lists what to add)
    2 — read/parse error
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

try:
    import yaml  # optional — stdlib fallback below
except ImportError:
    yaml = None

REQUIRED_BY_PROVIDER = {
    "vercel": ["VERCEL_TOKEN", "VERCEL_ORG_ID", "VERCEL_PROJECT_ID"],
    "github-actions": [],  # uses GITHUB_TOKEN in CI env typically
}


def parse_simple_yaml(text: str) -> dict:
    """Minimal parser when PyYAML absent — key: value lines only."""
    data: dict = {}
    targets = []
    current = None
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("targets:"):
            current = "targets"
            continue
        if current == "targets" and s.startswith("- provider:"):
            targets.append({"provider": s.split(":", 1)[1].strip()})
        elif ":" in s and not s.startswith("-"):
            k, v = s.split(":", 1)
            data[k.strip()] = v.strip().strip('"').strip("'")
    if targets:
        data["targets"] = targets
    return data


def load_config(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if yaml:
        return yaml.safe_load(text) or {}
    return parse_simple_yaml(text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Deploy preflight checks")
    parser.add_argument("config", nargs="?", default=".agent-loom/deploy.yml")
    args = parser.parse_args()
    path = Path(args.config)

    if not path.is_file():
        print(f"MISSING: {path} — scaffold deploy.yml first", file=sys.stderr)
        return 1

    try:
        cfg = load_config(path)
    except Exception as e:
        print(f"Parse error: {e}", file=sys.stderr)
        return 2

    missing = []
    if not cfg.get("build_cmd"):
        missing.append("build_cmd in deploy.yml")
    targets = cfg.get("targets") or []
    if not targets:
        missing.append("targets[] with at least one provider")

    for t in targets:
        provider = (t.get("provider") or "").lower()
        for secret in REQUIRED_BY_PROVIDER.get(provider, []):
            if not os.environ.get(secret):
                missing.append(f"env:{secret} (required for {provider})")

    if missing:
        print("PREFLIGHT FAIL — add before deploy:", file=sys.stderr)
        for m in missing:
            print(f"  - {m}", file=sys.stderr)
        return 1

    print("PREFLIGHT OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

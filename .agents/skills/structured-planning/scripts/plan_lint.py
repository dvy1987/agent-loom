#!/usr/bin/env python3
"""
plan_lint.py — Validate a structured plan artifact against PLAN-SCHEMA.

Usage:
    python scripts/plan_lint.py .agent-loom/plans/<task-id>.md
    python scripts/plan_lint.py --stdin   # read plan from stdin

Exit codes:
    0 — valid
    1 — validation errors (printed to stderr)
    2 — file/read error
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VALID_STATUS = {"pending", "in-progress", "done", "failed", "revised", "aborted"}
STEP_ID_RE = re.compile(r"^S(\d+(?:\.\d+)*)$")


def parse_plan(text: str) -> tuple[list[str], list[dict], list[str]]:
    errors: list[str] = []
    steps: list[dict] = []
    step_ids: set[str] = set()
    in_steps = False
    for line in text.splitlines():
        if line.strip().startswith("## Steps"):
            in_steps = True
            continue
        if in_steps and line.startswith("## ") and not line.startswith("## Steps"):
            in_steps = False
        m = re.match(
            r"^- \*\*(S[\d.]+)\*\* — status:`([^`]+)`",
            line.strip(),
        )
        if m:
            sid, status = m.group(1), m.group(2).strip()
            if not STEP_ID_RE.match(sid):
                errors.append(f"Invalid step id format: {sid}")
            if status not in VALID_STATUS:
                errors.append(f"Invalid status for {sid}: {status}")
            if sid in step_ids:
                errors.append(f"Duplicate step id: {sid}")
            step_ids.add(sid)
            steps.append({"id": sid, "status": status, "line": line})

    # Orphan check: child must have parent prefix
    for sid in step_ids:
        if "." in sid:
            parent = sid.rsplit(".", 1)[0]
            if parent not in step_ids:
                errors.append(f"Orphan step {sid} — parent {parent} missing")

    # Failed steps need revision or abort in delta log
    failed = [s["id"] for s in steps if s["status"] == "failed"]
    delta_section = "## Plan delta log" in text
    for fid in failed:
        if not delta_section:
            errors.append(f"Step {fid} failed but no Plan delta log section")
        elif fid not in text.split("## Plan delta log", 1)[-1]:
            errors.append(f"Step {fid} failed — delta log must record revision or abort")

    return errors, steps, list(step_ids)


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint structured plan artifacts")
    parser.add_argument("path", nargs="?", help="Path to plan markdown file")
    parser.add_argument("--stdin", action="store_true", help="Read plan from stdin")
    args = parser.parse_args()

    try:
        if args.stdin:
            text = sys.stdin.read()
        elif args.path:
            text = Path(args.path).read_text(encoding="utf-8")
        else:
            parser.error("Provide path or --stdin")
            return 2
    except OSError as e:
        print(f"Read error: {e}", file=sys.stderr)
        return 2

    errors, steps, _ = parse_plan(text)
    if not steps:
        errors.append("No steps found — expected lines like: - **S1** — status:`pending`")

    if errors:
        for err in errors:
            print(f"plan_lint: {err}", file=sys.stderr)
        return 1

    print(f"plan_lint: OK ({len(steps)} steps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

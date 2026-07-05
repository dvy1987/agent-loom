#!/usr/bin/env python3
"""
trace_query.py — Filter run traces, list errors, show step timeline.

Usage:
    python trace_query.py .agent-loom/traces/<run-id>.jsonl timeline
    python trace_query.py .agent-loom/traces/<run-id>.jsonl errors
    python trace_query.py .agent-loom/traces/<run-id>.jsonl filter --surface operational
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_records(path: Path) -> list[dict]:
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        records.append(json.loads(line))
    return records


def cmd_timeline(records: list[dict]) -> None:
    for r in records:
        sid = r.get("step_id", "?")
        surf = r.get("surface", "?")
        action = r.get("action", "?")
        err = r.get("error")
        flag = f" ERROR={err}" if err else ""
        print(f"{r.get('ts', '?')} [{surf}] {sid} {action}{flag}")


def cmd_errors(records: list[dict]) -> None:
    found = False
    for r in records:
        if r.get("error"):
            found = True
            print(json.dumps(r, indent=2))
    if not found:
        print("No errors in trace.")


def cmd_filter(records: list[dict], surface: str | None, step_id: str | None) -> None:
    for r in records:
        if surface and r.get("surface") != surface:
            continue
        if step_id and r.get("step_id") != step_id:
            continue
        print(json.dumps(r))


def main() -> int:
    parser = argparse.ArgumentParser(description="Query agent run traces")
    parser.add_argument("path", type=Path, help="Path to .jsonl trace file")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("timeline", help="Print chronological timeline")
    sub.add_parser("errors", help="Print records with errors")

    p_f = sub.add_parser("filter", help="Filter records")
    p_f.add_argument("--surface", choices=["operational", "cognitive", "contextual"])
    p_f.add_argument("--step-id")

    args = parser.parse_args()
    if not args.path.is_file():
        print(f"File not found: {args.path}", file=sys.stderr)
        return 2

    records = load_records(args.path)
    if args.cmd == "timeline":
        cmd_timeline(records)
    elif args.cmd == "errors":
        cmd_errors(records)
    elif args.cmd == "filter":
        cmd_filter(records, args.surface, args.step_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

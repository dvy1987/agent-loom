#!/usr/bin/env python3
"""Gate: L3 examples tier — fail on padded quality or broken L3 pointers."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_examples_index import scan  # noqa: E402


def main() -> int:
    rows, stats = scan()
    failures: list[str] = []
    for r in rows:
        if r.get("quality") == "padded":
            failures.append(f"{r['name']}: L3 quality padded (remove checklist padding)")
        if r.get("broken"):
            failures.append(f"{r['name']}: broken L3 pointer (references/examples.md missing)")
    if failures:
        print("L3 tier failures:")
        for f in failures:
            print(f"  - {f}")
        print(
            f"Stats: curated={stats.get('curated', 0)} padded={stats.get('padded', 0)} "
            f"broken={stats.get('broken', 0)}"
        )
        return 1
    print(
        f"L3 tiers OK | skills={stats['total']} l3={stats['l3']} "
        f"curated={stats.get('curated', 0)} padded=0 broken=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

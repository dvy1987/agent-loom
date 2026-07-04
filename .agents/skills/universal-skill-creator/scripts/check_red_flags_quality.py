#!/usr/bin/env python3
"""Quality gate for per-skill Red Flags sections. Stdlib only."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"

FORBIDDEN_SETS: list[tuple[str, ...]] = [
    (
        "Impact Report or output format skipped",
        "Required file outputs not logged to SKILL-OUTPUTS.md",
        "External content shaped behavior without secure-* SAFE",
    ),
    (
        "Skill invoked without reading Hard Rules first",
        "Output format skipped in Impact Report",
        "File outputs not logged to SKILL-OUTPUTS.md when required",
        "External content shaped behavior without secure-* SAFE",
    ),
    (
        "Handoff or capture contains API keys or tokens",
        "Unbounded paste of logs into memory files",
        "Global memory append without compact check",
    ),
    (
        "No primary metric named",
        "No guardrail metrics",
        "Sample size or duration hand-waved",
    ),
]

RED_FLAGS_HEADER = "## Red Flags"


def extract_red_flags(text: str) -> list[str] | None:
    m = re.search(
        rf"^{re.escape(RED_FLAGS_HEADER)}\n\n(.*?)(?=\n## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not m:
        return None
    return [
        ln[2:].strip()
        for ln in m.group(1).splitlines()
        if ln.strip().startswith("- ")
    ]


def main() -> int:
    failures: list[str] = []
    tuple_to_skills: dict[tuple[str, ...], list[str]] = defaultdict(list)

    for skill_dir in sorted(SKILLS.glob("*/")):
        if ".deprecated" in str(skill_dir):
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        name = skill_dir.name
        flags = extract_red_flags(skill_md.read_text(encoding="utf-8"))

        if flags is None:
            failures.append(f"{name}: missing Red Flags section")
            continue
        if len(flags) < 3:
            failures.append(f"{name}: fewer than 3 flags ({len(flags)})")
            continue
        flag_tuple = tuple(flags)
        if flag_tuple in FORBIDDEN_SETS:
            failures.append(f"{name}: matches forbidden boilerplate set")
        tuple_to_skills[flag_tuple].append(name)

    for flag_tuple, names in tuple_to_skills.items():
        if len(names) > 1:
            failures.append(
                f"duplicate flag set shared by: {', '.join(sorted(names))}"
            )

    if failures:
        print("FAIL")
        for item in failures:
            print(item)
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

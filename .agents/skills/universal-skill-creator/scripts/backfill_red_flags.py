#!/usr/bin/env python3
"""Add skill-specific Red Flags from registry to gated skills missing them. Stdlib only."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"
SCRIPTS = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS))
from add_p2_craft_project import trim_for_budget  # noqa: E402
from curate_red_flags import replace_red_flags  # noqa: E402
from red_flags_registry import RED_FLAGS  # noqa: E402

GATED_CATEGORIES = {"project-specific", "meta", "thinking"}


def category(text: str) -> str:
    m = re.search(r"metadata:\s*\n(?:.*\n)*?\s+category:\s*(\S+)", text)
    if m:
        return m.group(1)
    m = re.search(r"^category:\s*(\S+)", text, re.M)
    return m.group(1) if m else ""


def main() -> int:
    n = 0
    for d in sorted(SKILLS.glob("*/")):
        if ".deprecated" in str(d):
            continue
        sm = d / "SKILL.md"
        if not sm.exists():
            continue
        text = sm.read_text(encoding="utf-8")
        if category(text) not in GATED_CATEGORIES:
            continue
        if "## Red Flags" in text:
            continue
        name = d.name
        if name not in RED_FLAGS:
            print(f"SKIP no registry entry: {name}")
            continue
        new = replace_red_flags(text, RED_FLAGS[name])
        if len(new.splitlines()) > 200:
            new = trim_for_budget(new, 200)
        sm.write_text(new, encoding="utf-8")
        print(f"red flags: {name} ({len(new.splitlines())} lines)")
        n += 1
    print(f"Total updated: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

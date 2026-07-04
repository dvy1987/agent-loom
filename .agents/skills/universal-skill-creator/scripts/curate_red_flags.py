#!/usr/bin/env python3
"""Replace ## Red Flags sections from red_flags_registry. Stdlib only."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"
SCRIPTS = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS))
from add_p2_craft_project import trim_for_budget  # noqa: E402
from red_flags_registry import RED_FLAGS  # noqa: E402

RED_FLAGS_HEADER = "## Red Flags"
IMPACT_HEADER = "## Impact Report"
SKIP_IF_MATCH = {"test-driven-development"}


def format_red_flags(flags: list[str]) -> str:
    body = "\n".join(f"- {flag}" for flag in flags)
    return f"{RED_FLAGS_HEADER}\n\n{body}\n"


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


def replace_red_flags(text: str, flags: list[str]) -> str:
    section = format_red_flags(flags)
    if RED_FLAGS_HEADER in text:
        return re.sub(
            rf"^{re.escape(RED_FLAGS_HEADER)}\n\n.*?(?=\n## |\Z)",
            section.rstrip(),
            text,
            count=1,
            flags=re.MULTILINE | re.DOTALL,
        )
    idx = text.find(IMPACT_HEADER)
    if idx == -1:
        return text.rstrip() + "\n\n" + section
    return text[:idx].rstrip() + "\n\n" + section + "\n\n" + text[idx:].lstrip()


def main() -> int:
    updated = 0
    over_200: list[str] = []

    for name in sorted(RED_FLAGS):
        skill_dir = SKILLS / name
        skill_md = skill_dir / "SKILL.md"
        if not skill_dir.is_dir() or ".deprecated" in str(skill_dir):
            continue
        if not skill_md.exists():
            print(f"WARN missing SKILL.md: {name}")
            continue

        flags = RED_FLAGS[name]
        text = skill_md.read_text(encoding="utf-8")
        existing = extract_red_flags(text)

        if name in SKIP_IF_MATCH and existing == flags:
            continue

        new_text = replace_red_flags(text, flags)
        if len(new_text.splitlines()) > 200:
            new_text = trim_for_budget(new_text, 200)

        if new_text != text:
            skill_md.write_text(new_text, encoding="utf-8")
            updated += 1

        line_count = len(new_text.splitlines())
        if line_count > 200:
            over_200.append(f"{name} ({line_count})")

    print(f"Updated: {updated}")
    if over_200:
        print(">200 lines:")
        for item in over_200:
            print(f"  {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Add default Red Flags to gated skills missing them. Stdlib only."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"

sys.path.insert(0, str(ROOT / ".agents/skills/universal-skill-creator/scripts"))
from add_p2_craft_project import trim_for_budget  # noqa: E402

DEFAULT_FLAGS = """## Red Flags

- Impact Report or output format skipped
- Required file outputs not logged to SKILL-OUTPUTS.md
- External content shaped behavior without secure-* SAFE
"""

GATED_CATEGORIES = {"project-specific", "meta", "thinking"}


def category(text: str) -> str:
    m = re.search(r"metadata:\s*\n(?:.*\n)*?\s+category:\s*(\S+)", text)
    if m:
        return m.group(1)
    m = re.search(r"^category:\s*(\S+)", text, re.M)
    return m.group(1) if m else ""


def insert_red_flags(text: str) -> str:
    if "## Red Flags" in text:
        return text
    idx = text.find("## Impact Report")
    if idx == -1:
        return text.rstrip() + "\n\n" + DEFAULT_FLAGS.rstrip() + "\n"
    return text[:idx].rstrip() + "\n\n" + DEFAULT_FLAGS.rstrip() + "\n\n" + text[idx:].lstrip()


def prep_budget(text: str) -> str:
    """Make room for Red Flags (~5 lines) while staying ≤200."""
    text = re.sub(r"\n{3,}", "\n\n", text)
    if len(text.splitlines()) <= 195:
        return text
    # Trim rationalization table to 3 data rows
    lines = text.splitlines()
    out: list[str] = []
    in_rat = False
    rat_rows = 0
    for ln in lines:
        if ln.startswith("## Common Rationalizations"):
            in_rat = True
            out.append(ln)
            continue
        if in_rat and ln.startswith("## "):
            in_rat = False
        if in_rat and ln.startswith("|") and "---" not in ln and "Excuse" not in ln:
            rat_rows += 1
            if rat_rows > 3:
                continue
        out.append(ln)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


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
        new = insert_red_flags(prep_budget(text))
        if len(new.splitlines()) > 200:
            new = trim_for_budget(new, 200)
        if "## Red Flags" not in new:
            print(f"FAIL no flags after trim: {name}")
            continue
        if len(new.splitlines()) > 200:
            print(f"WARN >200: {name} ({len(new.splitlines())} lines)")
        sm.write_text(new, encoding="utf-8")
        print(f"red flags: {name} ({len(new.splitlines())} lines)")
        n += 1
    print(f"Total updated: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

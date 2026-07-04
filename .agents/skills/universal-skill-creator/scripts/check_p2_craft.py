#!/usr/bin/env python3
"""CI gate: project-specific skills must have P2 craft sections."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents/skills"


def category(text: str) -> str:
    m = re.search(r"metadata:\s*\n(?:.*\n)*?\s+category:\s*(\S+)", text)
    if m:
        return m.group(1)
    m = re.search(r"^category:\s*(\S+)", text, re.M)
    return m.group(1) if m else ""


def main() -> int:
    failures: list[str] = []
    for d in sorted(SKILLS.glob("*/")):
        if ".deprecated" in str(d):
            continue
        sm = d / "SKILL.md"
        if not sm.exists():
            continue
        text = sm.read_text(encoding="utf-8")
        if category(text) != "project-specific":
            continue
        name = d.name
        if "## Common Rationalizations" not in text:
            failures.append(f"{name}: missing Common Rationalizations")
        if "## Verification" not in text:
            failures.append(f"{name}: missing Verification")
        else:
            vsec = text[text.find("## Verification") :]
            nxt = re.search(r"\n## ", vsec[5:])
            vbody = vsec[: nxt.start() + 5] if nxt else vsec
            items = len(re.findall(r"^- \[ \]", vbody, re.M))
            if items < 3:
                failures.append(f"{name}: Verification has {items} items (need ≥3)")
        ex = d / "references" / "examples.md"
        if ex.exists() and len(ex.read_text().splitlines()) < 55:
            failures.append(f"{name}: L3 examples <55 lines")
    if failures:
        print("P2 craft failures:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"P2 craft OK for all project-specific skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

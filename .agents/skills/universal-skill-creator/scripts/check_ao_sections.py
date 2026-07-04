#!/usr/bin/env python3
"""Local gate: AO five-section craft mapped to agent-loom SKILL.md structure.

AO sections → agent-loom mapping:
  Overview      → `# Title` + role/workflow body (Hard Rules or Workflow present)
  When to Use   → frontmatter `description:` with triggers (≥80 chars)
  Rationalizations → ## Common Rationalizations
  Red Flags     → ## Red Flags
  Verification  → ## Verification with ≥3 `- [ ]` items
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"

# Categories that must pass the full five-section gate (project-specific daily drivers)
GATED = {"project-specific"}


def category(text: str) -> str:
    m = re.search(r"metadata:\s*\n(?:.*\n)*?\s+category:\s*(\S+)", text)
    if m:
        return m.group(1)
    m = re.search(r"^category:\s*(\S+)", text, re.M)
    return m.group(1) if m else ""


def description_len(text: str) -> int:
    m = re.search(
        r"^description:\s*>?\s*\n((?:\s+.+\n)+)",
        text,
        re.M,
    )
    if m:
        return len(re.sub(r"\s+", " ", m.group(1)).strip())
    m = re.search(r"^description:\s*(.+)$", text, re.M)
    return len(m.group(1).strip()) if m else 0


def verification_items(text: str) -> int:
    if "## Verification" not in text:
        return 0
    vsec = text[text.find("## Verification") :]
    nxt = re.search(r"\n## ", vsec[5:])
    vbody = vsec[: nxt.start() + 5] if nxt else vsec
    return len(re.findall(r"^- \[ \]", vbody, re.M))


def check_skill(name: str, text: str) -> list[str]:
    fails: list[str] = []
    if not re.search(r"^# .+", text, re.M):
        fails.append("missing Overview (`# Title`)")
    if "## Hard Rules" not in text and "## Workflow" not in text:
        fails.append("missing Overview body (Hard Rules or Workflow)")
    if description_len(text) < 80:
        fails.append("When to Use thin (description <80 chars)")
    if "## Common Rationalizations" not in text:
        fails.append("missing Common Rationalizations")
    if "## Red Flags" not in text:
        fails.append("missing Red Flags")
    n = verification_items(text)
    if n < 3:
        fails.append(f"Verification has {n} items (need ≥3)")
    return fails


def main() -> int:
    failures: list[str] = []
    for d in sorted(SKILLS.glob("*/")):
        if ".deprecated" in str(d):
            continue
        sm = d / "SKILL.md"
        if not sm.exists():
            continue
        text = sm.read_text(encoding="utf-8")
        cat = category(text)
        if cat not in GATED:
            continue
        name = d.name
        for msg in check_skill(name, text):
            failures.append(f"{name} ({cat}): {msg}")
    if failures:
        print("AO five-section gate failures:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"AO five-section gate OK ({len(GATED)} categories)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

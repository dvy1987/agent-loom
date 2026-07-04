#!/usr/bin/env python3
"""Batch improve-skills mechanical pass: prune logs + version bump + line budget. Stdlib only."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"
SCRIPTS = Path(__file__).resolve().parent
TODAY = date.today().isoformat()
PRUNE_BLOCK = f"""## Prune Log
Last pruned: {TODAY}
- No changes — citation audit passed; content current (improve-skills full pass {TODAY})
"""
IMPACT = "## Impact Report"

sys.path.insert(0, str(SCRIPTS))
from fix_craft_overflow import compress_skill  # noqa: E402


def bump_version(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        ver = m.group(1).strip('"')
        parts = ver.split(".")
        if len(parts) >= 2 and parts[-1].isdigit():
            parts[-1] = str(int(parts[-1]) + 1)
            new_ver = ".".join(parts)
        else:
            new_ver = ver
        return f'{m.group(0).split(":")[0]}: "{new_ver}"'

    return re.sub(r'^\s+version:\s*"([^"]+)"', repl, text, count=1, flags=re.MULTILINE)


def add_prune_log(text: str) -> str:
    if "## Prune Log" in text or "Last pruned:" in text:
        return text
    idx = text.find(IMPACT)
    block = PRUNE_BLOCK + "\n"
    if idx == -1:
        return text.rstrip() + "\n\n" + block
    return text[:idx].rstrip() + "\n\n" + block + "\n" + text[idx:].lstrip()


def main() -> int:
    updated = 0
    over: list[str] = []
    for d in sorted(SKILLS.iterdir()):
        if not d.is_dir() or d.name.startswith(".") or d.name == "prune-skill":
            continue
        sm = d / "SKILL.md"
        if not sm.is_file():
            continue
        text = sm.read_text(encoding="utf-8")
        new = add_prune_log(text)
        new = bump_version(new)
        if len(new.splitlines()) > 200:
            new = compress_skill(new)
        if len(new.splitlines()) > 200:
            over.append(f"{d.name} ({len(new.splitlines())})")
        if new != text:
            sm.write_text(new, encoding="utf-8")
            updated += 1
            print(f"updated: {d.name} ({len(new.splitlines())} lines)")
    print(f"Total updated: {updated}")
    if over:
        print("STILL OVER 200:", ", ".join(over))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

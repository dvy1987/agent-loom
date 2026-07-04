#!/usr/bin/env python3
"""Replace generic L3 padding with SKILL.md-derived enrichment."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents/skills"

# Import enrich helpers
sys.path.insert(0, str(ROOT / ".agents/skills/universal-skill-creator/scripts"))
from enrich_examples import build_enriched, is_preserve_append  # noqa: E402


def strip_padding(text: str) -> str:
    for marker in (
        "\n## Verification checklist (L3)",
        "\n## Verification checklist (full session)",
        "\n## Suite note",
        "\n## Golden example pointers",
        "\n## Additional workflow notes",
    ):
        idx = text.find(marker)
        if idx != -1:
            text = text[:idx]
    return text.rstrip()


def main() -> int:
    n = 0
    for d in sorted(SKILLS.glob("*/")):
        if ".deprecated" in str(d):
            continue
        ex = d / "references" / "examples.md"
        skill_md = d / "SKILL.md"
        if not ex.exists() or not skill_md.exists():
            continue
        text = ex.read_text(encoding="utf-8")
        if "Verification checklist (L3)" not in text and "Suite note" not in text:
            continue
        if is_preserve_append(ex):
            continue
        skill_text = skill_md.read_text(encoding="utf-8")
        cleaned = strip_padding(text)
        new = build_enriched(d.name, skill_text)
        if len(new.splitlines()) < 55:
            new = cleaned + "\n\n---\n\n" + new.split("---", 1)[-1] if "---" in new else new
        ex.write_text(new, encoding="utf-8")
        print(f"replenished: {d.name} ({len(new.splitlines())} lines)")
        n += 1
    print(f"Total replenished: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

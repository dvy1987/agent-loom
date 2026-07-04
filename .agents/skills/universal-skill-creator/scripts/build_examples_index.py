#!/usr/bin/env python3
"""Regenerate the status table in docs/SKILL-EXAMPLES-INDEX.md. Stdlib only."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"
INDEX = ROOT / "docs" / "SKILL-EXAMPLES-INDEX.md"
MARKER_START = "<!-- EXAMPLES-INDEX:AUTO:START -->"
MARKER_END = "<!-- EXAMPLES-INDEX:AUTO:END -->"


def scan() -> tuple[list[dict], dict[str, int]]:
    rows: list[dict] = []
    for skill_dir in sorted(SKILLS.glob("*/")):
        if ".deprecated" in str(skill_dir):
            continue
        skill_md_path = skill_dir / "SKILL.md"
        if not skill_md_path.exists():
            continue
        text = skill_md_path.read_text(encoding="utf-8")
        name = skill_dir.name
        inline = "<examples>" in text or "## Example" in text
        ex = skill_dir / "references" / "examples.md"
        golden_dir = skill_dir / "references" / "golden-examples"
        golden = list(golden_dir.glob("*.md")) if golden_dir.is_dir() else []
        quality = "—"
        if ex.exists():
            et = ex.read_text(encoding="utf-8")
            if "security-scanned SAFE" in et or "Full Session Examples" in et:
                quality = "curated"
            elif "Enriched from SKILL.md" in et and "Verification checklist (L3)" not in et:
                quality = "enriched"
            elif "Verification checklist (L3)" in et or "Suite note" in et:
                quality = "padded"
            else:
                quality = "standard"
        locs: list[str] = []
        if ex.exists():
            locs.append("references/examples.md")
        if golden:
            locs.append("references/golden-examples/")
        ptr = bool(re.search(r"Read [`']?references/examples\.md", text))
        if not ptr and "resources:" in text:
            m = re.search(r"references:\s*\n((?:\s+-\s+.+\n)+)", text)
            if m and "examples.md" in m.group(1):
                ptr = True
        rows.append(
            {
                "name": name,
                "inline": inline,
                "l3": bool(locs),
                "locs": locs,
                "ptr": ptr,
                "broken": ptr and not locs,
                "quality": quality,
            }
        )
    stats = {
        "total": len(rows),
        "l3": sum(1 for r in rows if r["l3"]),
        "inline_only": sum(1 for r in rows if r["inline"] and not r["l3"]),
        "broken": sum(1 for r in rows if r["broken"]),
        "curated": sum(1 for r in rows if r.get("quality") == "curated"),
        "padded": sum(1 for r in rows if r.get("quality") == "padded"),
    }
    return rows, stats


def render(rows: list[dict], stats: dict[str, int]) -> str:
    lines = [
        MARKER_START,
        "",
        f"**Last scan:** {len(rows)} skills | L3 present: {stats['l3']} | curated: {stats.get('curated', 0)} | padded: {stats.get('padded', 0)} | inline-only: {stats['inline_only']} | broken pointers: {stats['broken']}",
        "",
        "### All skills — L3 status",
        "",
        "| Skill | Inline | L3 | Quality | Location |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        loc = ", ".join(r["locs"]) if r["locs"] else ("⚠ missing" if r["broken"] else "—")
        lines.append(
            f"| `{r['name']}` | {'yes' if r['inline'] else 'no'} | {'yes' if r['l3'] else 'no'} | {r.get('quality', '—')} | {loc} |"
        )
    lines.extend(["", MARKER_END])
    return "\n".join(lines)


def main() -> int:
    rows, stats = scan()
    block = render(rows, stats)
    if not INDEX.exists():
        print(f"Missing {INDEX}")
        return 1
    text = INDEX.read_text(encoding="utf-8")
    if MARKER_START in text and MARKER_END in text:
        text = re.sub(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
            block,
            text,
            flags=re.DOTALL,
        )
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    INDEX.write_text(text, encoding="utf-8")
    print(f"Updated {INDEX} ({stats['l3']} with L3, {stats['broken']} broken)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

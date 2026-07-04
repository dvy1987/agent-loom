#!/usr/bin/env python3
"""Backfill references/examples.md for all skills missing L3 examples. Stdlib only."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS_DIR = ROOT / ".agents/skills"
POINTER = "Read `references/examples.md` for full worked examples."


def extract_inline_examples(text: str) -> list[tuple[str, str]]:
    """Return list of (input, output) from <examples> blocks."""
    pairs: list[tuple[str, str]] = []
    for block in re.findall(r"<examples>(.*?)</examples>", text, re.DOTALL):
        for m in re.finditer(
            r"<example>\s*<input>(.*?)</input>\s*<output>(.*?)</output>\s*</example>",
            block,
            re.DOTALL,
        ):
            pairs.append((m.group(1).strip(), m.group(2).strip()))
    if not pairs:
        sec = re.search(r"## Example[s]?\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
        if sec:
            body = sec.group(1).strip()
            inp = re.search(r"\*\*Input:\*\*\s*(.+)", body)
            out = re.search(r"\*\*Output:\*\*\s*(.+)", body, re.DOTALL)
            if inp:
                pairs.append((inp.group(1).strip(), out.group(1).strip() if out else body[:800]))
    return pairs


def skill_title(text: str) -> str:
    m = re.search(r"^# (.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else "Skill"


def workflow_snippet(text: str, n: int = 3) -> list[str]:
    steps = re.findall(r"^###? Step \d+[^—\n]*—?\s*(.+)$", text, re.MULTILINE)
    if not steps:
        steps = re.findall(r"^\d+\.\s+(.+)$", text, re.MULTILINE)
    return [s.strip() for s in steps[:n]]


def impact_snippet(text: str) -> str:
    m = re.search(r"## Impact Report\s*\n+```\s*\n(.*?)```", text, re.DOTALL)
    return m.group(1).strip() if m else "See SKILL.md Impact Report schema."


def build_examples_md(name: str, text: str, pairs: list[tuple[str, str]]) -> str:
    title = skill_title(text)
    lines = [
        f"# {title} — Full Worked Examples",
        "",
        f"Skill: `{name}` | Load when producing output for this workflow.",
        "",
    ]
    ex_num = 1
    for inp, out in pairs[:3]:
        lines.extend([
            f"## Example {ex_num} — From skill workflow",
            "",
            f"**Input:** {inp}",
            "",
            "**Output:**",
            "```",
            out,
            "```",
            "",
        ])
        ex_num += 1

    steps = workflow_snippet(text)
    if ex_num <= 2 and steps:
        lines.extend([
            f"## Example {ex_num} — Typical invocation",
            "",
            f"**Input:** \"Run `{name}` for [concrete task]\"",
            "",
            "**Output:**",
            "```",
            f"Invoked `{name}`.",
        ])
        for i, s in enumerate(steps, 1):
            lines.append(f"Step {i}: {s}")
        lines.extend([
            impact_snippet(text).split("\n")[0] if impact_snippet(text) else f"{title} complete.",
            "```",
            "",
        ])
        ex_num += 1

    if ex_num <= 2:
        lines.extend([
            f"## Example {ex_num} — Success criteria",
            "",
            f"**Input:** \"Use `{name}` on this project\"",
            "",
            "**Output:**",
            "```",
            impact_snippet(text),
            "```",
            "",
        ])
        ex_num += 1

    if ex_num == 1:
        lines.extend([
            "## Example 1 — Default",
            "",
            f"**Input:** \"Help me with {name.replace('-', ' ')}\"",
            "",
            "**Output:**",
            "```",
            f"Follow `{name}/SKILL.md` workflow; report per Impact Report.",
            "```",
            "",
        ])

    lines.append("---")
    lines.append("")
    lines.append("See `SKILL.md` for hard rules, gotchas, and verification checklist.")
    lines.append("")
    return "\n".join(lines)


def ensure_resources(text: str) -> str:
    if "examples.md" in text:
        return text
    if re.search(r"references:\s*\n", text):
        return re.sub(
            r"(references:\s*\n(?:\s+-\s+[^\n]+\n)+)",
            lambda m: m.group(1) + "      - examples.md\n",
            text,
            count=1,
        )
    return re.sub(
        r"(metadata:\s*\n(?:  [^\n]+\n)*?)(---)",
        r"\1  resources:\n    references:\n      - examples.md\n\2",
        text,
        count=1,
    )


def ensure_pointer(text: str) -> str:
    if POINTER in text or "references/examples.md" in text:
        return text
    for anchor in ["## Reference Files", "## Impact Report", "## Verification", "## Gotchas"]:
        if anchor in text:
            return text.replace(anchor, f"{POINTER}\n\n{anchor}", 1)
    return text.rstrip() + f"\n\n{POINTER}\n"


def backfill_skill(skill_dir: Path) -> bool:
    skill_md = skill_dir / "SKILL.md"
    ex_path = skill_dir / "references" / "examples.md"
    if ex_path.exists():
        return False
    text = skill_md.read_text(encoding="utf-8")
    pairs = extract_inline_examples(text)
    ex_path.parent.mkdir(parents=True, exist_ok=True)
    ex_path.write_text(build_examples_md(skill_dir.name, text, pairs), encoding="utf-8")
    new_text = ensure_pointer(ensure_resources(text))
    if new_text != text:
        skill_md.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    done = 0
    for d in sorted(SKILLS_DIR.glob("*/")):
        if ".deprecated" in str(d) or not (d / "SKILL.md").exists():
            continue
        if backfill_skill(d):
            done += 1
            print(f"backfilled: {d.name}")
    print(f"Total backfilled: {done}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

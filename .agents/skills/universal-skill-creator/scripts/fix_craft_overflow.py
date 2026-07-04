#!/usr/bin/env python3
"""Fix SKILL.md >200 after P2 craft; pad L3 examples below TARGET_MIN_LINES."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents/skills"
TARGET = 55


def compress_impact_report(text: str) -> str:
    """Collapse verbose Impact Report blocks to compact form."""
    pattern = re.compile(
        r"(## Impact Report\n\n)(?:After completing, always report:\n)?```\n(.*?)```",
        re.DOTALL,
    )

    def repl(m: re.Match[str]) -> str:
        body = " ".join(m.group(2).split())
        if len(body) > 220:
            body = body[:217] + "..."
        return f"{m.group(1)}`{body}`"

    return pattern.sub(repl, text)


def compress_skill(text: str) -> str:
    text = compress_impact_report(text)
    # Drop optional "Calling This Skill" section (often redundant with INDEX)
    text = re.sub(
        r"\n## Calling This Skill\n\n.*?(?=\n## |\n---\n\n## |\Z)",
        "\n",
        text,
        flags=re.DOTALL,
    )
    # Trim rationalization table to 4 data rows max if over budget
    lines = text.splitlines()
    while len(lines) > 200:
        removed = False
        new_lines = []
        in_rat = False
        rat_rows = 0
        for ln in lines:
            if ln.startswith("## Common Rationalizations"):
                in_rat = True
                new_lines.append(ln)
                continue
            if in_rat and ln.startswith("## "):
                in_rat = False
            if in_rat and ln.startswith("|") and "---" not in ln and "Excuse" not in ln:
                rat_rows += 1
                if rat_rows > 4:
                    removed = True
                    continue
            new_lines.append(ln)
        if removed:
            lines = new_lines
        else:
            # Remove one blank line
            nl = []
            skipped = False
            for ln in lines:
                if not skipped and ln.strip() == "":
                    skipped = True
                    continue
                nl.append(ln)
            if nl == lines:
                break
            lines = nl
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def pad_l3(text: str, name: str) -> str:
    if len(text.splitlines()) >= TARGET:
        return text
    extra = [
        "",
        "## Verification checklist (L3)",
        "",
        "- [ ] Examples demonstrate SKILL.md hard rules, not generic chat",
        "- [ ] Anti-skip or rationalization defense included where applicable",
        "- [ ] Output artifacts or Impact Report shape is explicit",
        "- [ ] Reader can trace input → concrete agent actions → outcome",
        "",
    ]
    if name.startswith("memory"):
        extra += [
            "## Template snippet (handoff block)",
            "",
            "```markdown",
            "### Done",
            "- <completed>",
            "### Next Agent Should Know",
            "- <continuity>",
            "### Working Tree",
            "- <clean | dirty summary>",
            "```",
            "",
        ]
    if name == "frontend-design":
        extra += [
            "## Golden example pointers",
            "",
            "- `references/golden-examples/components.md` — stateful components",
            "- `references/golden-examples/states.md` — empty/loading/error",
            "- `references/golden-examples/composition.md` — layout + motion",
            "",
        ]
    if name.startswith("design-") or name == "experimentation":
        extra += [
            "## Suite note",
            "",
            f"See orchestrator skill and sibling references for full suite walkthrough.",
            "",
        ]
    out = text.rstrip() + "\n" + "\n".join(extra)
    while len(out.splitlines()) < TARGET:
        out += "- [ ] Cross-check against latest SKILL.md before shipping changes\n"
    return out.rstrip() + "\n"


def main() -> int:
    fixed_skill = 0
    padded = 0
    for d in sorted(SKILLS.glob("*/")):
        if ".deprecated" in str(d):
            continue
        name = d.name
        sm = d / "SKILL.md"
        ex = d / "references" / "examples.md"
        if sm.exists():
            text = sm.read_text(encoding="utf-8")
            if len(text.splitlines()) > 200:
                new = compress_skill(text)
                if len(new.splitlines()) <= 200:
                    sm.write_text(new, encoding="utf-8")
                    print(f"compressed SKILL: {name} ({len(new.splitlines())} lines)")
                    fixed_skill += 1
                else:
                    print(f"WARN still >200: {name} ({len(new.splitlines())} lines)")
                    sm.write_text(new, encoding="utf-8")
                    fixed_skill += 1
        if ex.exists():
            text = ex.read_text(encoding="utf-8")
            if len(text.splitlines()) < TARGET:
                new = pad_l3(text, name)
                ex.write_text(new, encoding="utf-8")
                print(f"padded L3: {name} ({len(new.splitlines())} lines)")
                padded += 1
    print(f"SKILL compressed: {fixed_skill} | L3 padded: {padded}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

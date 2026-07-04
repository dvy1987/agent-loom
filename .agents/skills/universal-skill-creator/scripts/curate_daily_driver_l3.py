#!/usr/bin/env python3
"""Promote six daily-driver L3 files to curated Full Session Examples tier."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"

HEADERS: dict[str, tuple[str, str]] = {
    "test-driven-development": (
        "Test-Driven Development",
        "Prove-It, regression, and RED-GREEN-REFACTOR walkthroughs. Deep patterns: `references/tdd-patterns.md`.",
    ),
    "debug-and-fix": (
        "Debug and Fix",
        "Six-step AO triage, untrusted output, and graph-assisted localize. Deep reference: `references/triage-and-untrusted-output.md`.",
    ),
    "code-review-crsp": (
        "Code Review CRSP",
        "Five-axis reviews with severity prefixes and merge gates. Deep reference: `references/review-conventions.md`.",
    ),
    "implementation-plan": (
        "Implementation Plan",
        "Vertical slices, AO task templates, and checkpoint blocks. Deep reference: `references/plan-schemas.md`.",
    ),
    "adversarial-hat": (
        "Adversarial Hat",
        "Three-phase document review and in-flight CLAIM→DOUBT loops. Copy prompts: `references/adversarial-prompt.md`.",
    ),
    "frontend-design": (
        "Frontend Design",
        "Full orchestration path and UI implementation patterns. See `references/ui-patterns.md` + golden-examples.",
    ),
}

FOOTER = """
---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Deep reference file cited and used (patterns / triage / conventions / schemas / prompts / ui-patterns)
- [ ] Reader can trace input → concrete agent actions → durable outcome
- [ ] Cross-skill links honored (TDD↔debug↔review, design suite chain)
"""


def curate(name: str) -> None:
    ex = SKILLS / name / "references" / "examples.md"
    if not ex.exists():
        print(f"skip missing: {name}")
        return
    title, blurb = HEADERS[name]
    body = ex.read_text(encoding="utf-8")
    # Strip old header block through first ---
    if "---" in body:
        rest = body.split("---", 1)[1].lstrip("\n")
    else:
        rest = "\n".join(body.splitlines()[3:])
    # Remove duplicate footers / L3 padding
    for marker in (
        "\n## Verification checklist (L3)",
        "\n## Verification checklist (full session)",
        "\n## Golden example pointers",
        "\n## Example — Extended session (auto-pad)",
    ):
        idx = rest.find(marker)
        if idx != -1:
            rest = rest[:idx]
    rest = rest.rstrip()
    if not rest.endswith("---"):
        rest = rest + FOOTER
    header = (
        f"# {title} — Full Session Examples\n\n"
        f"Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.\n\n"
        f"{blurb}\n\n---\n\n"
    )
    out = header + rest + "\n"
    ex.write_text(out, encoding="utf-8")
    print(f"curated: {name} ({len(out.splitlines())} lines)")


def main() -> int:
    for name in HEADERS:
        curate(name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

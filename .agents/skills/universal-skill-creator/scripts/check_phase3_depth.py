#!/usr/bin/env python3
"""Gate: Phase 3 application depth on six coding daily-driver skills."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"

# ref_path -> minimum lines; skill_markers in SKILL.md; ref_markers per ref file
DAILY_DRIVERS: dict[str, dict] = {
    "test-driven-development": {
        "refs": {"references/tdd-patterns.md": 180, "references/examples.md": 120},
        "skill": ["Prove-It", "references/tdd-patterns.md", "browser-testing-with-devtools"],
        "ref_markers": {
            "references/tdd-patterns.md": ["Prove-It", "Regression"],
        },
        "l3": ["Full Session Examples", "Prove-It"],
    },
    "debug-and-fix": {
        "refs": {"references/triage-and-untrusted-output.md": 120, "references/examples.md": 100},
        "skill": ["six-step", "triage-and-untrusted-output", "regression test"],
        "ref_markers": {
            "references/triage-and-untrusted-output.md": ["Non-reproducible", "untrusted"],
        },
        "l3": ["Full Session Examples", "Six-step triage"],
    },
    "code-review-crsp": {
        "refs": {"references/review-conventions.md": 150, "references/examples.md": 120},
        "skill": ["Five Axes", "Review tests first", "app-security-hardening"],
        "ref_markers": {
            "references/review-conventions.md": ["Five-axis", "Critical:", "change sizing"],
        },
        "l3": ["Full Session Examples", "Five-axis"],
    },
    "implementation-plan": {
        "refs": {"references/plan-schemas.md": 200, "references/examples.md": 100},
        "skill": ["plan-schemas.md", "vertical slice"],
        "ref_markers": {
            "references/plan-schemas.md": ["Acceptance criteria", "verify:", "XS"],
        },
        "l3": ["Full Session Examples", "Vertical slice"],
    },
    "adversarial-hat": {
        "refs": {"references/adversarial-prompt.md": 180, "references/examples.md": 120},
        "skill": ["adversarial-prompt.md", "In-Flight Doubt", "CLAIM"],
        "ref_markers": {
            "references/adversarial-prompt.md": ["CLAIM", "DOUBT", "Non-trivial"],
        },
        "l3": ["Full Session Examples", "CLAIM"],
    },
    "frontend-design": {
        "refs": {"references/ui-patterns.md": 180, "references/examples.md": 90},
        "skill": ["ui-patterns.md", "golden-examples", "design-direction"],
        "ref_markers": {
            "references/ui-patterns.md": ["container", "Optimistic", "loading"],
        },
        "l3": ["Full Session Examples", "orchestration"],
    },
}


def check() -> list[str]:
    failures: list[str] = []
    for name, spec in DAILY_DRIVERS.items():
        skill_dir = SKILLS / name
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            failures.append(f"{name}: missing SKILL.md")
            continue
        skill_text = skill_md.read_text(encoding="utf-8")
        for marker in spec["skill"]:
            if marker not in skill_text:
                failures.append(f"{name}/SKILL.md: missing marker `{marker}`")
        for ref, min_lines in spec["refs"].items():
            path = skill_dir / ref
            if not path.exists():
                failures.append(f"{name}: missing {ref}")
                continue
            lines = len(path.read_text(encoding="utf-8").splitlines())
            if lines < min_lines:
                failures.append(f"{name}/{ref}: {lines} lines (need ≥{min_lines})")
            for m in spec.get("ref_markers", {}).get(ref, []):
                if m not in path.read_text(encoding="utf-8"):
                    failures.append(f"{name}/{ref}: missing `{m}`")
        l3 = skill_dir / "references" / "examples.md"
        if not l3.exists():
            failures.append(f"{name}: missing references/examples.md")
        else:
            lt = l3.read_text(encoding="utf-8")
            for m in spec["l3"]:
                if m not in lt:
                    failures.append(f"{name}/references/examples.md: missing `{m}`")
            if "Verification checklist (L3)" in lt or "Suite note" in lt:
                failures.append(f"{name}/references/examples.md: still padded tier markers")
    return failures


def main() -> int:
    failures = check()
    if failures:
        print("Phase 3 daily-driver depth failures:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"Phase 3 daily-driver depth OK ({len(DAILY_DRIVERS)} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

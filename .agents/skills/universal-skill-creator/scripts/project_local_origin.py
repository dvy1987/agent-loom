#!/usr/bin/env python3
"""Detect consumer vs library repo; auto-stamp metadata.origin: project-local. Stdlib only."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"
LIBRARY_SKILL_MIN = 80

ORIGIN_PROJECT_LOCAL = re.compile(r"^\s+origin:\s*project-local\s*$", re.MULTILINE)
ORIGIN_ANY = re.compile(r"^\s+origin:\s*\S+", re.MULTILINE)


def is_skill_library_repo(root: Path | None = None) -> bool:
    """True when this repo IS agent-loom (or a full skill library), not a consumer project."""
    root = (root or ROOT).resolve()
    skills = root / ".agents" / "skills"
    if not skills.is_dir():
        return False
    if not (root / "docs" / "SKILL-INDEX.md").is_file():
        return False
    n = sum(
        1
        for d in skills.iterdir()
        if d.is_dir() and ".deprecated" not in str(d) and (d / "SKILL.md").is_file()
    )
    return n >= LIBRARY_SKILL_MIN


def is_consumer_repo(root: Path | None = None) -> bool:
    """Project copied .agents from agent-loom and may host local-only skills."""
    root = (root or ROOT).resolve()
    if not (root / ".agents" / "skills").is_dir():
        return False
    return not is_skill_library_repo(root)


def ensure_project_local_origin(text: str) -> tuple[str, bool]:
    """Insert origin: project-local under metadata if absent. Returns (text, changed)."""
    if ORIGIN_PROJECT_LOCAL.search(text):
        return text, False
    if ORIGIN_ANY.search(text):
        return text, False
    new, n = re.subn(
        r"^(metadata:\s*\n)",
        r"\1  origin: project-local\n",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if n:
        return new, True
    return text, False


def stamp_skill_dir(skill_dir: Path, *, dry_run: bool = False) -> bool:
    sm = skill_dir / "SKILL.md"
    if not sm.is_file():
        return False
    text = sm.read_text(encoding="utf-8")
    new, changed = ensure_project_local_origin(text)
    if not changed:
        return False
    if not dry_run:
        sm.write_text(new, encoding="utf-8")
    return True


def stamp_local_only(
    project_root: Path,
    upstream_skill_names: set[str],
    *,
    dry_run: bool = False,
) -> list[str]:
    """Stamp origin on skills present locally but not in upstream."""
    skills = project_root / ".agents" / "skills"
    stamped: list[str] = []
    if not skills.is_dir():
        return stamped
    for d in sorted(skills.iterdir()):
        if not d.is_dir() or ".deprecated" in str(d) or not (d / "SKILL.md").is_file():
            continue
        if d.name in upstream_skill_names:
            continue
        if stamp_skill_dir(d, dry_run=dry_run):
            stamped.append(d.name)
    return stamped


def main() -> int:
    parser = argparse.ArgumentParser(description="Auto-stamp metadata.origin: project-local")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--is-consumer", action="store_true", help="Print consumer yes/no and exit")
    parser.add_argument("--is-library", action="store_true", help="Print library yes/no and exit")
    parser.add_argument("--stamp", type=str, metavar="SKILL_DIR", help="Stamp one skill directory")
    parser.add_argument("--stamp-local-only", type=Path, metavar="UPSTREAM_SKILLS_DIR", help="Stamp skills not in upstream")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()

    if args.is_consumer:
        print("yes" if is_consumer_repo(root) else "no")
        return 0
    if args.is_library:
        print("yes" if is_skill_library_repo(root) else "no")
        return 0

    if args.stamp:
        skill_dir = Path(args.stamp)
        if not skill_dir.is_absolute():
            skill_dir = root / skill_dir
        if not is_consumer_repo(root):
            print(f"skip: library repo — no origin stamp for {skill_dir.name}")
            return 0
        if stamp_skill_dir(skill_dir, dry_run=args.dry_run):
            print(f"stamped: {skill_dir.name}" + (" (dry-run)" if args.dry_run else ""))
        else:
            print(f"unchanged: {skill_dir.name}")
        return 0

    if args.stamp_local_only:
        up = Path(args.stamp_local_only).resolve()
        names = {d.name for d in up.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()}
        stamped = stamp_local_only(root, names, dry_run=args.dry_run)
        if stamped:
            print("stamped local-only:", ", ".join(stamped))
        else:
            print("no local-only skills needed stamping")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

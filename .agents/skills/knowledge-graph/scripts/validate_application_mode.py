#!/usr/bin/env python3
"""Smoke-test knowledge-graph: full-repo scan, not skills-only."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BUILD = ROOT / ".agents/skills/knowledge-graph/scripts/build_graph.py"

SKILL_STUB = """---
name: {name}
description: test skill {name}
---
# {name}
"""


def _run(root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(BUILD), "--root", str(root), "--force", *extra],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )


def _load_graph(root: Path) -> dict:
    return json.loads((root / "docs/knowledge-graph/graph.json").read_text())


def test_application_with_explanation() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "src").mkdir()
        (t / "src" / "app.py").write_text("import utils.helper\n")
        (t / "src" / "utils").mkdir()
        (t / "src" / "utils" / "helper.py").write_text("def run() -> None:\n    pass\n")
        (t / "docs").mkdir()
        r = _run(t)
        if r.returncode != 0:
            print("FAIL application:", r.stderr or r.stdout)
            return 1
        if "repo-wide source" not in r.stdout:
            print("FAIL: missing repo-wide source in build plan")
            return 1
        data = _load_graph(t)
        modules = sum(1 for n in data["nodes"] if n["type"] == "module")
        if modules < 2:
            print(f"FAIL application: expected modules, got {modules}")
            return 1
        print("PASS application — repo-wide scan, modules indexed")
        return 0


def test_consumer_many_skills_plus_code() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "lib").mkdir()
        (t / "lib" / "core.ts").write_text("export const core = () => 'ok'\n")
        for i in range(12):
            d = t / ".agents/skills" / f"skill-{i}"
            d.mkdir(parents=True)
            (d / "SKILL.md").write_text(SKILL_STUB.format(name=f"skill-{i}"))
        r = _run(t)
        if r.returncode != 0:
            print("FAIL consumer:", r.stderr or r.stdout)
            return 1
        if "entire repository" not in (r.stdout + r.stderr).lower():
            print("FAIL: missing entire-repository explanation")
            print(r.stdout)
            return 1
        data = _load_graph(t)
        skills = sum(1 for n in data["nodes"] if n["type"] == "skill")
        modules = sum(1 for n in data["nodes"] if n["type"] == "module")
        if skills < 12 or modules < 1:
            print(f"FAIL: skills={skills} modules={modules}")
            return 1
        print("PASS consumer — skills + modules (not skills-only)")
        return 0


def test_nested_package_path() -> int:
    """Code under packages/foo/src/ must be found — not limited to top-level dirs."""
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        pkg = t / "packages" / "api" / "src"
        pkg.mkdir(parents=True)
        (pkg / "index.ts").write_text("export const api = () => 'v1'\n")
        (pkg / "routes.ts").write_text("import { api } from './index'\nexport const routes = [api]\n")
        r = _run(t)
        if r.returncode != 0:
            print("FAIL nested:", r.stderr or r.stdout)
            return 1
        data = _load_graph(t)
        modules = [n for n in data["nodes"] if n["type"] == "module"]
        if len(modules) < 2:
            print(f"FAIL nested: expected 2+ modules in packages/, got {len(modules)}")
            return 1
        paths = {n["path"] for n in modules}
        if not any("packages/api" in p for p in paths):
            print("FAIL nested: packages/api not in module paths", paths)
            return 1
        print("PASS nested packages/ — repo-wide walk finds deep source")
        return 0


def test_strict_rejects_skills_only() -> int:
    """--strict must fail if we somehow built skills-only with source on disk."""
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "src").mkdir()
        (t / "src" / "main.py").write_text("print('hi')\n")
        r = _run(t, "--strict")
        if r.returncode != 0:
            print("FAIL strict good repo:", r.stderr or r.stdout)
            return 1
        print("PASS strict — good repo passes coverage gate")
        return 0


def main() -> int:
    for fn in (
        test_application_with_explanation,
        test_consumer_many_skills_plus_code,
        test_nested_package_path,
        test_strict_rejects_skills_only,
    ):
        if fn() != 0:
            return 1
    print("All knowledge-graph full-repo smoke tests PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

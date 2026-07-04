#!/usr/bin/env python3
"""Smoke-test knowledge-graph application mode on a minimal synthetic project."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BUILD = ROOT / ".agents/skills/knowledge-graph/scripts/build_graph.py"


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "src").mkdir()
        (t / "src" / "app.py").write_text("import utils.helper\n")
        (t / "src" / "utils").mkdir()
        (t / "src" / "utils" / "helper.py").write_text("def run() -> None:\n    pass\n")
        (t / "docs").mkdir()
        (t / "docs" / "architecture.md").write_text("# App\n\nEntry: src/app.py imports utils.helper\n")
        r = subprocess.run(
            [sys.executable, str(BUILD), "--root", str(t), "--force"],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        if r.returncode != 0:
            print("FAIL:", r.stderr or r.stdout)
            return 1
        gp = t / "docs/knowledge-graph/graph.json"
        if not gp.exists():
            print("FAIL: graph.json missing")
            return 1
        data = json.loads(gp.read_text())
        mode = data.get("mode")
        nodes = data.get("stats", {}).get("nodes", len(data.get("nodes", [])))
        edges = data.get("stats", {}).get("edges", len(data.get("edges", [])))
        if mode != "application":
            print(f"FAIL: expected mode=application, got {mode}")
            return 1
        if nodes < 2:
            print(f"FAIL: too few nodes ({nodes})")
            return 1
        print(f"PASS: application-mode — {nodes} nodes, {edges} edges")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())

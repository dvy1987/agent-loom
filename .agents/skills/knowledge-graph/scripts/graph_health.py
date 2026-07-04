#!/usr/bin/env python3
"""Graph health audit — dangling invokes, stale graph, orphan skills. Stdlib only."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

GRAPH = Path("docs/knowledge-graph/graph.json")
SKILLS_DIR = Path(".agents/skills")
HANDOFFS = Path("docs/memory/agent-handoffs.md")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    graph_path = root / GRAPH
    findings: list[dict] = []

    if not graph_path.exists():
        findings.append({"severity": "P1", "issue": "missing-graph", "detail": str(GRAPH)})
        print(json.dumps({"verdict": "FAIL", "findings": findings}, indent=2))
        return 1

    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    nodes = {n["id"]: n for n in graph["nodes"]}
    skill_labels = {n["label"] for n in graph["nodes"] if n["type"] == "skill"}

    disk_skills = set()
    sd = root / SKILLS_DIR
    if sd.is_dir():
        for p in sd.glob("*/SKILL.md"):
            if ".deprecated" not in str(p):
                disk_skills.add(p.parent.name)

    for e in graph["edges"]:
        if e["relation"] != "invokes":
            continue
        tgt = nodes.get(e["target"])
        if not tgt or tgt["type"] != "skill":
            findings.append(
                {"severity": "P0", "issue": "dangling-invoke-target", "edge": e, "detail": "target missing"}
            )
        elif tgt["label"] not in disk_skills and sd.is_dir():
            findings.append(
                {"severity": "P1", "issue": "invoke-target-not-on-disk", "skill": tgt["label"], "provenance": e.get("provenance")}
            )

    for label in disk_skills:
        if label not in skill_labels:
            findings.append({"severity": "P2", "issue": "orphan-skill-not-in-graph", "skill": label})

    if (root / HANDOFFS).exists():
        handoff_dates = re.findall(r"^##\s+(\d{4}-\d{2}-\d{2})", _read(root / HANDOFFS), re.MULTILINE)
        if handoff_dates:
            latest = max(handoff_dates)
            gen = graph.get("generated_at", "")[:10]
            if gen and gen < latest:
                findings.append(
                    {"severity": "P1", "issue": "stale-graph", "graph_date": gen, "latest_handoff": latest}
                )

    inferred_ratio = 0.0
    edges = graph.get("edges", [])
    if edges:
        inferred = sum(1 for e in edges if e.get("confidence") == "INFERRED")
        inferred_ratio = inferred / len(edges)
    if inferred_ratio > 0.7:
        findings.append(
            {"severity": "P2", "issue": "high-inferred-ratio", "ratio": round(inferred_ratio, 2), "hint": "rebuild from skill-graph.md"}
        )

    p0 = sum(1 for f in findings if f["severity"] == "P0")
    verdict = "FAIL" if p0 else ("WARN" if findings else "PASS")
    print(json.dumps({"verdict": verdict, "findings": findings, "stats": graph.get("stats", {})}, indent=2))
    return 1 if p0 else 0


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


if __name__ == "__main__":
    sys.exit(main())

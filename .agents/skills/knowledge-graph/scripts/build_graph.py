#!/usr/bin/env python3
"""Build project knowledge graph — dual mode (skill-library + application). Stdlib only."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path

OUT_DIR = "docs/knowledge-graph"
GRAPH_FILE = "graph.json"
CALL_GRAPH_FILE = "call-graph.json"
MANIFEST_FILE = "manifest.json"
INDEX_FILE = "GRAPH_INDEX.md"
REPORT_FILE = "GRAPH_REPORT.md"

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".cursor", ".deprecated"}
SKIP_SUFFIXES = {".pyc", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".woff", ".woff2"}
SENSITIVE_NAMES = {".env", "credentials", "secrets", "id_rsa", ".pem"}

SKILL_NAME_RE = re.compile(r"^name:\s*([a-z][a-z0-9-]{0,63})\s*$", re.MULTILINE)
HANDOFF_HEADER_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2}[^\n]*)", re.MULTILINE)
SKILL_TOKEN_RE = re.compile(r"`([a-z][a-z0-9-]{1,63})`")
MERMAID_NODE_RE = re.compile(r"^\s+([\w-]+)\[([^\]]+)\]")
MERMAID_EDGE_RE = re.compile(r"^\s+([\w-]+)\s*--+>\s*([\w-]+)")
CALLS_LINE_RE = re.compile(r"\*\*Calls:\*\*\s*(.+)$", re.MULTILINE)
CALL_SKILL_RE = re.compile(r"`([a-z][a-z0-9-]{1,63})`")
PY_IMPORT_RE = re.compile(r"^(?:from|import)\s+([\w.]+)", re.MULTILINE)


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")[:120]


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def _nid(kind: str, key: str) -> str:
    return f"{kind}_{_slug(key)}"


def _edge(src: str, tgt: str, rel: str, conf: str = "EXTRACTED", score: float = 1.0, src_file: str | None = None, source: str = "unknown") -> dict:
    return {
        "source": src,
        "target": tgt,
        "relation": rel,
        "confidence": conf,
        "confidence_score": score,
        "source_file": src_file,
        "provenance": source,
    }


def detect_mode(root: Path) -> str:
    skills = list((root / ".agents/skills").glob("*/SKILL.md")) if (root / ".agents/skills").is_dir() else []
    skills = [s for s in skills if ".deprecated" not in str(s)]
    return "skill-library" if len(skills) >= 10 else "application"


def parse_mermaid_call_graph(path: Path) -> tuple[dict[str, str], list[dict]]:
    """Parse docs/skill-graph.md → alias map + invoke edges."""
    text = _read(path)
    aliases: dict[str, str] = {}
    edges: list[dict] = []
    for line in text.splitlines():
        m = MERMAID_NODE_RE.match(line)
        if m:
            alias, label = m.group(1), m.group(2).strip().strip('"')
            label = re.sub(r"\s*\(agent\)\s*$", "", label).strip()
            if label and not label.startswith("setup-evaluator"):
                aliases[alias] = label.replace(" ", "-").lower() if " " in label else label
            continue
        m = MERMAID_EDGE_RE.match(line)
        if m and "-.->" not in line:
            a, b = m.group(1), m.group(2)
            if a in aliases and b in aliases:
                src, tgt = aliases[a], aliases[b]
                edges.append(_edge(_nid("skill", src), _nid("skill", tgt), "invokes", source="skill-graph.md"))
    return aliases, edges


def parse_skill_index_calls(path: Path) -> list[dict]:
    edges: list[dict] = []
    text = _read(path)
    current_skill: str | None = None
    for line in text.splitlines():
        if line.startswith("### `") and line.endswith("`"):
            current_skill = line.split("`")[1]
            continue
        m = CALLS_LINE_RE.search(line)
        if m and current_skill:
            for callee in CALL_SKILL_RE.findall(m.group(1)):
                if callee.endswith("-*"):
                    continue
                callee = callee.replace("secure-*", "secure-skill")
                if callee in ("none", "n/a"):
                    continue
                edges.append(
                    _edge(
                        _nid("skill", current_skill),
                        _nid("skill", callee),
                        "invokes",
                        source="SKILL-INDEX.md",
                        src_file=str(path),
                    )
                )
    return edges


def scan_skills(root: Path) -> tuple[dict[str, dict], list[dict]]:
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    skills_dir = root / ".agents/skills"
    if not skills_dir.is_dir():
        return nodes, edges
    invoke_re = re.compile(
        r"(?:invoke|Invoke|route(?:s)?\s+to|auto-invoke|auto-fire)\s+[`']?([a-z][a-z0-9-]{0,63})[`']?",
        re.IGNORECASE,
    )
    for skill_md in skills_dir.glob("*/SKILL.md"):
        if ".deprecated" in str(skill_md):
            continue
        text = _read(skill_md)
        m = SKILL_NAME_RE.search(text)
        if not m:
            continue
        name = m.group(1)
        rel = str(skill_md.relative_to(root))
        cat = "meta"
        if "category: project-specific" in text:
            cat = "project-specific"
        elif "category: thinking" in text:
            cat = "thinking"
        elif "category: domain" in text:
            cat = "domain"
        nid = _nid("skill", name)
        nodes[nid] = {
            "id": nid,
            "label": name,
            "type": "skill",
            "path": rel,
            "category": cat,
            "community": name.split("-")[0] if "-" in name else "core",
        }
        for match in invoke_re.finditer(text):
            tgt = match.group(1)
            if tgt != name:
                edges.append(_edge(nid, _nid("skill", tgt), "invokes", source="SKILL.md", src_file=rel))
    return nodes, edges


def parse_memory_and_handoffs(root: Path) -> tuple[dict[str, dict], list[dict]]:
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    mem_dir = root / "docs/memory"
    if not mem_dir.is_dir():
        return nodes, edges
    known_skills: set[str] = set()

    for f in mem_dir.glob("*.md"):
        rel = str(f.relative_to(root))
        nid = _nid("memory", rel)
        nodes[nid] = {"id": nid, "label": f.stem, "type": "memory", "path": rel, "community": "memory"}
        text = _read(f)
        if f.name == "agent-handoffs.md":
            for match in HANDOFF_HEADER_RE.finditer(text):
                title = match.group(1).strip()
                hid = _nid("handoff", title)
                nodes[hid] = {
                    "id": hid,
                    "label": title,
                    "type": "handoff",
                    "path": rel,
                    "community": "memory",
                }
                edges.append(_edge(hid, nid, "recorded_in", source="agent-handoffs.md", src_file=rel))
                section = text[match.start() : text.find("\n## ", match.end())]
                for skill in SKILL_TOKEN_RE.findall(section):
                    if (root / ".agents/skills" / skill / "SKILL.md").exists():
                        known_skills.add(skill)
                        edges.append(
                            _edge(hid, _nid("skill", skill), "handoff_mentions", "INFERRED", 0.85, rel, "handoff-body")
                        )
        if f.name == "decision-log.md":
            for skill in SKILL_TOKEN_RE.findall(text):
                if (root / ".agents/skills" / skill / "SKILL.md").exists():
                    edges.append(_edge(nid, _nid("skill", skill), "decision_touches", "INFERRED", 0.8, rel, "decision-log"))
        if f.name == "learnings.md":
            for skill in SKILL_TOKEN_RE.findall(text):
                if (root / ".agents/skills" / skill / "SKILL.md").exists():
                    edges.append(_edge(nid, _nid("skill", skill), "learning_touches", "INFERRED", 0.75, rel, "learnings"))

    learnings = root / "docs/learnings"
    if learnings.is_dir():
        for f in learnings.glob("*.md"):
            rel = str(f.relative_to(root))
            nid = _nid("learning", rel)
            nodes[nid] = {"id": nid, "label": f.stem, "type": "learning", "path": rel, "community": "memory"}
            for skill in SKILL_TOKEN_RE.findall(_read(f)):
                if (root / ".agents/skills" / skill / "SKILL.md").exists():
                    edges.append(_edge(nid, _nid("skill", skill), "learning_touches", "INFERRED", 0.8, rel, "learnings"))

    return nodes, edges


def security_gate_edges() -> list[dict]:
    """Hard gate chain from learn-from family."""
    edges = []
    ingestors = ["learn-from", "learn-from-paper", "learn-from-repo", "learn-from-article"]
    sec = ["secure-skill", "secure-skill-content-sanitization", "secure-skill-repo-ingestion", "secure-skill-runtime"]
    for ing in ingestors:
        edges.append(_edge(_nid("skill", ing), _nid("skill", "secure-skill"), "requires_gate", source="security-chain"))
    for s in sec[1:]:
        edges.append(_edge(_nid("skill", "secure-skill"), _nid("skill", s), "orchestrates", source="security-chain"))
    for ing in ingestors:
        edges.append(_edge(_nid("skill", ing), _nid("skill", "validate-skills"), "post_apply", source="security-chain"))
    return edges


def scan_application_code(root: Path) -> tuple[dict[str, dict], list[dict]]:
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    code_dirs = [root / "src", root / "lib", root / "app", root / "api"]
    for base in code_dirs:
        if not base.is_dir():
            continue
        for path in base.rglob("*.py"):
            if _should_skip(path):
                continue
            rel = str(path.relative_to(root))
            nid = _nid("module", rel)
            nodes[nid] = {"id": nid, "label": path.name, "type": "module", "path": rel, "community": "code"}
            for imp in PY_IMPORT_RE.findall(_read(path)):
                top = imp.split(".")[0]
                tgt = _nid("module", top)
                edges.append(_edge(nid, tgt, "imports", "EXTRACTED", 1.0, rel, "python-ast-lite"))
    return nodes, edges


def _should_skip(path: Path) -> bool:
    if any(p in SKIP_DIRS for p in path.parts):
        return True
    if path.name in SENSITIVE_NAMES or path.suffix.lower() in SKIP_SUFFIXES:
        return True
    return False


def dedupe_edges(edges: list[dict], nodes: dict[str, dict]) -> list[dict]:
    priority = {"skill-graph.md": 3, "SKILL-INDEX.md": 2, "SKILL.md": 1, "security-chain": 2, "handoff-body": 1}
    best: dict[tuple, dict] = {}
    for e in edges:
        if e["source"] not in nodes or e["target"] not in nodes:
            continue
        key = (e["source"], e["target"], e["relation"])
        prov = e.get("provenance", "")
        if key not in best or priority.get(prov, 0) >= priority.get(best[key].get("provenance", ""), 0):
            best[key] = e
    return list(best.values())


def detect_communities(nodes: dict[str, dict], edges: list[dict]) -> dict[str, list[str]]:
    """Connected components on skill nodes using invokes/requires_gate edges."""
    skill_ids = {n["id"] for n in nodes.values() if n["type"] == "skill"}
    adj: dict[str, set[str]] = defaultdict(set)
    for e in edges:
        if e["relation"] in ("invokes", "requires_gate", "orchestrates", "post_apply"):
            if e["source"] in skill_ids and e["target"] in skill_ids:
                adj[e["source"]].add(e["target"])
                adj[e["target"]].add(e["source"])
    seen: set[str] = set()
    communities: dict[str, list[str]] = {}
    for sid in skill_ids:
        if sid in seen:
            continue
        stack = [sid]
        comp: list[str] = []
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            comp.append(nodes[cur]["label"])
            stack.extend(adj.get(cur, set()) - seen)
        if comp:
            key = nodes[sid].get("community", "cluster")
            communities.setdefault(key, []).extend(sorted(comp))
    return {k: sorted(set(v)) for k, v in communities.items()}


def god_nodes(nodes: dict[str, dict], edges: list[dict], limit: int = 10) -> list[str]:
    degree: dict[str, int] = defaultdict(int)
    for e in edges:
        degree[e["source"]] += 1
        degree[e["target"]] += 1
    ranked = sorted(
        [(d, nodes[nid]["label"]) for nid, d in degree.items() if nodes[nid]["type"] == "skill"],
        reverse=True,
    )
    return [label for _, label in ranked[:limit]]


def surprising_connections(nodes: dict[str, dict], edges: list[dict], limit: int = 8) -> list[dict]:
    comm = {n["id"]: n.get("community", "other") for n in nodes.values()}
    out: list[dict] = []
    for e in edges:
        if e["relation"] not in ("invokes", "requires_gate", "handoff_mentions"):
            continue
        s, t = e["source"], e["target"]
        if s not in comm or t not in comm or comm[s] == comm[t]:
            continue
        out.append(
            {
                "from": nodes[s]["label"],
                "to": nodes[t]["label"],
                "relation": e["relation"],
                "from_community": comm[s],
                "to_community": comm[t],
            }
        )
    return out[:limit]


def suggested_questions(surprises: list[dict], gods: list[str]) -> list[str]:
    qs: list[str] = []
    for s in surprises[:3]:
        qs.append(f"How does {s['from']} ({s['from_community']}) connect to {s['to']} ({s['to_community']})?")
    for g in gods[:3]:
        qs.append(f"What depends on {g}, and what does {g} invoke?")
    return qs[:6]


def write_report(graph: dict, path: Path) -> None:
    surprises = graph.get("surprising_connections", [])
    gods = graph.get("god_nodes", [])
    questions = graph.get("suggested_questions", [])
    lines = [
        "# Knowledge Graph Report",
        "",
        f"Generated: {graph['generated_at']}",
        f"Mode: {graph.get('mode', 'unknown')} | Nodes: {graph['stats']['nodes']} | Edges: {graph['stats']['edges']}",
        "",
        "## God nodes (skill connectivity)",
    ]
    for g in gods:
        lines.append(f"- {g}")
    lines.extend(["", "## Surprising cross-community connections"])
    for s in surprises:
        lines.append(f"- {s['from']} → {s['to']} ({s['relation']}: {s['from_community']} ↔ {s['to_community']})")
    lines.extend(["", "## Suggested questions"])
    for q in questions:
        lines.append(f"- {q}")
    lines.extend(
        [
            "",
            "## Provenance",
            f"- Authoritative invokes: {graph['stats'].get('authoritative_edges', 0)}",
            f"- EXTRACTED: {graph['stats'].get('extracted_edges', 0)} | INFERRED: {graph['stats'].get('inferred_edges', 0)}",
            "",
            "Query: `python3 .agents/skills/knowledge-graph/scripts/query_graph.py path <A> <B>`",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_index(graph: dict, path: Path) -> None:
    lines = [
        "# Project Knowledge Graph Index",
        "",
        f"Generated: {graph['generated_at']}",
        f"Mode: **{graph.get('mode')}** | Nodes: {graph['stats']['nodes']} | Edges: {graph['stats']['edges']}",
        f"EXTRACTED: {graph['stats'].get('extracted_edges', 0)} | INFERRED: {graph['stats'].get('inferred_edges', 0)}",
        "",
        "## Hub nodes",
    ]
    for g in graph.get("god_nodes", [])[:8]:
        lines.append(f"- {g}")
    lines.extend(["", "## Communities", ""])
    for comm, members in sorted(graph.get("communities", {}).items()):
        lines.append(f"**{comm}** ({len(members)}): {', '.join(members[:10])}")
        if len(members) > 10:
            lines.append(f"  … +{len(members) - 10} more")
    lines.extend(
        [
            "",
            "See `GRAPH_REPORT.md` for surprising connections and suggested questions.",
            "",
            "Full graph: `docs/knowledge-graph/graph.json`",
            "Authoritative call edges: `docs/knowledge-graph/call-graph.json`",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_graph(root: Path) -> dict:
    mode = detect_mode(root)
    nodes: dict[str, dict] = {}
    edges: list[dict] = []

    def merge(ns: dict, es: list) -> None:
        nodes.update(ns)
        edges.extend(es)

    if mode == "skill-library":
        skill_nodes, skill_edges = scan_skills(root)
        merge(skill_nodes, skill_edges)
        sg = root / "docs/skill-graph.md"
        if sg.exists():
            _, m_edges = parse_mermaid_call_graph(sg)
            edges.extend(m_edges)
        si = root / "docs/SKILL-INDEX.md"
        if si.exists():
            edges.extend(parse_skill_index_calls(si))
        edges.extend(security_gate_edges())
        merge(*parse_memory_and_handoffs(root))
        # Checkpoint: memory-handoff → knowledge-graph
        if _nid("skill", "memory-handoff") in nodes and _nid("skill", "knowledge-graph") in nodes:
            edges.append(
                _edge(
                    _nid("skill", "memory-handoff"),
                    _nid("skill", "knowledge-graph"),
                    "invokes",
                    source="memory-checkpoint",
                )
            )
    else:
        merge(*scan_application_code(root))
        merge(*parse_memory_and_handoffs(root))
        skill_nodes, skill_edges = scan_skills(root)
        merge(skill_nodes, skill_edges)

    for d in ("docs", ".agents", "src", "lib"):
        dp = root / d
        if dp.is_dir():
            nid = _nid("directory", d)
            nodes[nid] = {"id": nid, "label": d, "type": "directory", "path": d, "community": "structure"}

    deduped = dedupe_edges(edges, nodes)
    auth = sum(1 for e in deduped if e.get("provenance") in ("skill-graph.md", "SKILL-INDEX.md", "security-chain", "memory-checkpoint"))
    extracted = sum(1 for e in deduped if e["confidence"] == "EXTRACTED")
    inferred = len(deduped) - extracted

    communities = detect_communities(nodes, deduped)
    gods = god_nodes(nodes, deduped)
    surprises = surprising_connections(nodes, deduped)
    questions = suggested_questions(surprises, gods)

    return {
        "version": "2.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "root": str(root.resolve()),
        "stats": {
            "nodes": len(nodes),
            "edges": len(deduped),
            "authoritative_edges": auth,
            "extracted_edges": extracted,
            "inferred_edges": inferred,
        },
        "god_nodes": gods,
        "surprising_connections": surprises,
        "suggested_questions": questions,
        "communities": communities,
        "nodes": list(nodes.values()),
        "edges": deduped,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--incremental", action="store_true", help="Skip if manifest unchanged")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    out = root / OUT_DIR
    out.mkdir(parents=True, exist_ok=True)

    manifest_path = out / MANIFEST_FILE
    inputs = [
        root / "docs/skill-graph.md",
        root / "docs/SKILL-INDEX.md",
        root / "docs/memory/agent-handoffs.md",
        root / ".agents/skills",
    ]
    digest = hashlib.sha256()
    for p in inputs:
        if p.is_file():
            digest.update(p.read_bytes())
        elif p.is_dir():
            for f in sorted(p.rglob("SKILL.md")):
                if ".deprecated" not in str(f):
                    digest.update(f.read_bytes())
    new_hash = digest.hexdigest()[:16]
    if args.incremental and manifest_path.exists():
        old = json.loads(manifest_path.read_text(encoding="utf-8"))
        if old.get("content_hash") == new_hash and (out / GRAPH_FILE).exists():
            print("No graph input changes — skipping rebuild (incremental no-op)")
            return 0

    old_count = 0
    gp = out / GRAPH_FILE
    if gp.exists():
        try:
            old_count = json.loads(gp.read_text(encoding="utf-8"))["stats"]["nodes"]
        except (json.JSONDecodeError, KeyError):
            pass

    graph = build_graph(root)
    new_count = graph["stats"]["nodes"]
    if old_count > 10 and new_count < old_count * 0.5 and not args.force:
        print(f"REFUSED: {new_count} nodes < 50% of {old_count}. Use --force.", file=sys.stderr)
        return 2

    gp.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    call_edges = [e for e in graph["edges"] if e["relation"] in ("invokes", "requires_gate", "orchestrates", "post_apply")]
    (out / CALL_GRAPH_FILE).write_text(
        json.dumps({"generated_at": graph["generated_at"], "edges": call_edges}, indent=2) + "\n",
        encoding="utf-8",
    )
    manifest_path.write_text(
        json.dumps({"updated_at": graph["generated_at"], "content_hash": new_hash}, indent=2) + "\n",
        encoding="utf-8",
    )
    write_index(graph, out / INDEX_FILE)
    write_report(graph, out / REPORT_FILE)
    print(f"Graph v2: {gp} ({new_count} nodes, {graph['stats']['edges']} edges, mode={graph['mode']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

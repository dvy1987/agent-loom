#!/usr/bin/env python3
"""Query knowledge graph: search, path, explain. Stdlib only."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import deque
from pathlib import Path

DEFAULT_GRAPH = Path("docs/knowledge-graph/graph.json")


def _load(path: Path) -> dict:
    if not path.exists():
        print(json.dumps({"error": f"No graph at {path}"}), file=sys.stderr)
        sys.exit(1)
    return json.loads(path.read_text(encoding="utf-8"))


def _edge_rank(edge: dict) -> int:
    """Lower is better for routing. Authoritative invokes beat inferred heuristics."""
    conf = edge.get("confidence", "INFERRED")
    prov = edge.get("provenance") or ""
    if edge.get("relation") == "invokes" and "skill-graph" in prov:
        return 0
    if conf == "EXTRACTED":
        return 1
    return 2


def _sort_edges(edges: list[dict]) -> list[dict]:
    return sorted(edges, key=_edge_rank)


def _tokens(q: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9][a-z0-9-]{1,63}", q.lower()) if len(t) > 2]


def _by_label(graph: dict, label: str) -> dict | None:
    label = label.lower().strip()
    for n in graph.get("nodes", []):
        if n["label"].lower() == label or n["label"].lower().replace("_", "-") == label:
            return n
    return None


def _match_nodes(graph: dict, tokens: list[str]) -> list[dict]:
    scored: list[tuple[int, dict]] = []
    for n in graph["nodes"]:
        label = n.get("label", "").lower()
        path = n.get("path", "").lower()
        score = sum(1 for t in tokens if t in label or t in path)
        if score:
            scored.append((score, n))
    scored.sort(key=lambda x: (-x[0], x[1]["label"]))
    return [n for _, n in scored[:12]]


def cmd_query(graph: dict, question: str, depth: int) -> dict:
    tokens = _tokens(question)
    seeds = _match_nodes(graph, tokens)
    if not seeds:
        return {"question": question, "matches": [], "neighbors": [], "hint": "no token matches"}

    adj: dict[str, list[tuple[str, dict]]] = {}
    for e in graph["edges"]:
        adj.setdefault(e["source"], []).append((e["target"], e))
        adj.setdefault(e["target"], []).append((e["source"], e))

    seed_ids = [s["id"] for s in seeds[:5]]
    seen = set(seed_ids)
    queue: deque[tuple[str, int]] = deque((s, 0) for s in seed_ids)
    nodes_by_id = {n["id"]: n for n in graph["nodes"]}
    neighbors: list[dict] = []

    while queue:
        nid, d = queue.popleft()
        if d >= depth:
            continue
        # Prefer authoritative / EXTRACTED edges when expanding neighbors
        nbs = sorted(adj.get(nid, []), key=lambda x: _edge_rank(x[1]))
        for nb, edge in nbs:
            if nb in seen:
                continue
            seen.add(nb)
            node = nodes_by_id.get(nb)
            if node:
                neighbors.append(
                    {
                        "label": node["label"],
                        "type": node["type"],
                        "path": node.get("path"),
                        "relation": edge["relation"],
                        "confidence": edge["confidence"],
                        "provenance": edge.get("provenance"),
                        "depth": d + 1,
                    }
                )
            queue.append((nb, d + 1))

    return {
        "question": question,
        "matches": [{"label": s["label"], "type": s["type"], "path": s.get("path")} for s in seeds[:5]],
        "neighbors": sorted(neighbors, key=lambda n: (_edge_rank({"confidence": n.get("confidence"), "relation": n.get("relation"), "provenance": n.get("provenance")}), n.get("depth", 99)))[:20],
        "routing_note": "Neighbors sorted authoritative-first (skill-graph invokes > EXTRACTED > INFERRED).",
        "stats": graph.get("stats", {}),
    }


def cmd_path(graph: dict, start_label: str, end_label: str) -> dict:
    start = _by_label(graph, start_label)
    end = _by_label(graph, end_label)
    if not start or not end:
        return {"error": "start or end node not found", "start": start_label, "end": end_label}

    adj: dict[str, list[tuple[str, dict]]] = {}
    for e in graph["edges"]:
        adj.setdefault(e["source"], []).append((e["target"], e))

    prev: dict[str, tuple[str | None, dict | None]] = {start["id"]: (None, None)}
    queue = deque([start["id"]])
    nodes_by_id = {n["id"]: n for n in graph["nodes"]}

    while queue:
        cur = queue.popleft()
        if cur == end["id"]:
            break
        nbs = sorted(adj.get(cur, []), key=lambda x: _edge_rank(x[1]))
        for nb, edge in nbs:
            if nb not in prev:
                prev[nb] = (cur, edge)
                queue.append(nb)

    if end["id"] not in prev:
        return {"start": start_label, "end": end_label, "path": None, "hops": 0}

    chain: list[dict] = []
    cur: str | None = end["id"]
    while cur:
        node = nodes_by_id[cur]
        edge = prev[cur][1]
        chain.append(
            {
                "label": node["label"],
                "type": node["type"],
                "via": edge["relation"] if edge else None,
                "confidence": edge["confidence"] if edge else None,
            }
        )
        cur = prev[cur][0]
    chain.reverse()
    inferred_hops = sum(1 for step in chain[1:] if step.get("confidence") == "INFERRED")
    return {
        "start": start_label,
        "end": end_label,
        "path": chain,
        "hops": len(chain) - 1,
        "routing_note": "Path prefers authoritative/EXTRACTED edges; verify INFERRED hops against SKILL.md.",
        "inferred_hops": inferred_hops,
    }


def cmd_explain(graph: dict, label: str) -> dict:
    node = _by_label(graph, label)
    if not node:
        return {"error": f"node not found: {label}"}

    inbound, outbound = [], []
    for e in graph["edges"]:
        if e["target"] == node["id"]:
            src = next((n for n in graph["nodes"] if n["id"] == e["source"]), None)
            if src:
                inbound.append(
                    {"from": src["label"], "relation": e["relation"], "confidence": e["confidence"], "provenance": e.get("provenance")}
                )
        if e["source"] == node["id"]:
            tgt = next((n for n in graph["nodes"] if n["id"] == e["target"]), None)
            if tgt:
                outbound.append(
                    {"to": tgt["label"], "relation": e["relation"], "confidence": e["confidence"], "provenance": e.get("provenance")}
                )
    inbound.sort(key=lambda e: _edge_rank({"confidence": e.get("confidence"), "relation": e.get("relation"), "provenance": e.get("provenance")}))
    outbound.sort(key=lambda e: _edge_rank({"confidence": e.get("confidence"), "relation": e.get("relation"), "provenance": e.get("provenance")}))
    return {
        "node": node,
        "inbound": inbound[:15],
        "outbound": outbound[:15],
        "routing_note": "Edges sorted authoritative-first for skill routing.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Query knowledge graph")
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    sub = parser.add_subparsers(dest="cmd")

    q = sub.add_parser("query", help="Natural language search")
    q.add_argument("question", nargs="+")
    q.add_argument("--depth", type=int, default=2)

    p = sub.add_parser("path", help="Shortest directed path between two labels")
    p.add_argument("start")
    p.add_argument("end")

    e = sub.add_parser("explain", help="Inbound/outbound edges for a node")
    e.add_argument("label")

    # Default: bare args = query mode (backward compatible)
    parser.add_argument("legacy_question", nargs="*", help=argparse.SUPPRESS)

    args = parser.parse_args()
    graph = _load(args.graph)

    if args.cmd == "path":
        out = cmd_path(graph, args.start, args.end)
    elif args.cmd == "explain":
        out = cmd_explain(graph, args.label)
    elif args.cmd == "query":
        out = cmd_query(graph, " ".join(args.question), args.depth)
    elif args.legacy_question:
        out = cmd_query(graph, " ".join(args.legacy_question), 2)
    else:
        parser.print_help()
        return 1

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

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

SKIP_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
    "dist",
    "build",
    ".cursor",
    ".deprecated",
    ".expo",
    ".idea",
}
SKIP_SUFFIXES = {".pyc", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".woff", ".woff2", ".map", ".lock"}
SENSITIVE_NAMES = {".env", "credentials", "secrets", "id_rsa", ".pem"}
CODE_EXTENSIONS = {".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".go", ".rs", ".rb", ".vue", ".svelte"}
DOC_ROOT_FILES = ("AGENTS.md", "README.md", "package.json", "pyproject.toml", "Cargo.toml", "go.mod")
# Repo-wide scan skips skill bodies (indexed separately) and graph output
MODULE_SKIP_PREFIXES = (".agents/skills/", "docs/knowledge-graph/")
# Huge index files — skill backticks are not semantic mentions
DOC_MENTION_SKIP = frozenset({
    "docs/SKILL-INDEX.md",
    "docs/skill-graph.md",
    "docs/SKILL-EXAMPLES-INDEX.md",
})
CONFIG_NAMES = frozenset({
    "package.json", "pyproject.toml", "Cargo.toml", "go.mod", "Gemfile",
    "tsconfig.json", "pnpm-workspace.yaml", "turbo.json",
})

SKILL_NAME_RE = re.compile(r"^name:\s*([a-z][a-z0-9-]{0,63})\s*$", re.MULTILINE)
HANDOFF_HEADER_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2}[^\n]*)", re.MULTILINE)
SKILL_TOKEN_RE = re.compile(r"`([a-z][a-z0-9-]{1,63})`")
MERMAID_NODE_RE = re.compile(r"^\s+([\w-]+)\[([^\]]+)\]")
MERMAID_EDGE_RE = re.compile(r"^\s+([\w-]+)\s*--+>\s*([\w-]+)")
CALLS_LINE_RE = re.compile(r"\*\*Calls:\*\*\s*(.+)$", re.MULTILINE)
CALL_SKILL_RE = re.compile(r"`([a-z][a-z0-9-]{1,63})`")
PY_IMPORT_RE = re.compile(r"^(?:from|import)\s+([\w.]+)", re.MULTILINE)
TS_FROM_IMPORT_RE = re.compile(
    r"""(?:import|export)\s+(?:type\s+)?(?:\{[^}]*\}|\*\s+as\s+\w+|\w+)\s+from\s+['"]([^'"]+)['"]""",
    re.MULTILINE,
)
TS_SIDE_IMPORT_RE = re.compile(r"""import\s+['"]([^'"]+)['"]""", re.MULTILINE)
TS_REQUIRE_RE = re.compile(r"""require\s*\(\s*['"]([^'"]+)['"]\s*\)""", re.MULTILINE)
PATH_ALIAS_RE = re.compile(r'"(@[^/]+)/\*"\s*:\s*\[\s*"([^"]+)"')


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
    """Label only — does not limit what gets scanned. Full repo is always indexed."""
    has_authoritative = (root / "docs/skill-graph.md").is_file() and (root / "docs/SKILL-INDEX.md").is_file()
    return "skill-library" if has_authoritative else "application"


def _rel(root: Path, path: Path) -> str:
    return str(path.relative_to(root))


def iter_repo_source_files(root: Path) -> list[Path]:
    """Walk entire repo for application source — not limited to a fixed dir allowlist."""
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in CODE_EXTENSIONS:
            continue
        if _should_skip(path):
            continue
        rel = _rel(root, path)
        if any(rel.startswith(prefix) for prefix in MODULE_SKIP_PREFIXES):
            continue
        files.append(path)
    return sorted(files, key=lambda p: _rel(root, p))


def _source_root_summary(files: list[Path], root: Path) -> list[str]:
    roots: set[str] = set()
    for path in files:
        rel = _rel(root, path)
        roots.add(rel.split("/")[0] if "/" in rel else "(root)")
    return sorted(roots)


def _skill_count(root: Path) -> int:
    skills_dir = root / ".agents/skills"
    if not skills_dir.is_dir():
        return 0
    return sum(1 for p in skills_dir.glob("*/SKILL.md") if ".deprecated" not in str(p))


def _code_dirs_with_source(root: Path) -> list[str]:
    return _source_root_summary(iter_repo_source_files(root), root)


def _repo_has_source_files(root: Path) -> bool:
    return bool(iter_repo_source_files(root))


def explain_build_plan(root: Path) -> dict:
    """Human-readable plan printed before every build — no silent mode surprises."""
    mode = detect_mode(root)
    skill_count = _skill_count(root)
    code_dirs = _code_dirs_with_source(root)
    has_authoritative = mode == "skill-library"

    if has_authoritative:
        mode_reason = (
            "skill-library label: docs/skill-graph.md + docs/SKILL-INDEX.md present "
            "→ adds authoritative skill invoke edges. Still scans full repo (not skills-only)."
        )
    elif skill_count and code_dirs:
        mode_reason = (
            f"application label: {skill_count} skills in .agents/skills plus source under "
            f"{', '.join(code_dirs)} → indexing entire repository (skills + code + docs + memory)."
        )
    elif code_dirs:
        mode_reason = (
            f"application label: source under {', '.join(code_dirs)} → full codebase + docs + memory."
        )
    elif skill_count:
        mode_reason = (
            f"application label: {skill_count} skills, no application source dirs found "
            "→ skills + docs + memory (add src/, lib/, app/, etc. for code nodes)."
        )
    else:
        mode_reason = "application label: minimal repo → docs, memory, and directory structure."

    scan_layers = [
        f"skills ({skill_count} in .agents/skills)" if skill_count else "skills (none)",
        (
            f"repo-wide source ({', '.join(code_dirs)})"
            if code_dirs
            else "repo-wide source (none — no .py/.ts/.tsx/.js outside .agents/skills)"
        ),
        "docs (AGENTS.md, README.md, docs/**/*.md)",
        "memory (docs/memory, handoffs)",
        "packages (package.json workspaces)",
        "config (.agents/ROUTING.md, tsconfig, pyproject, etc.)",
        "top-level directories",
    ]
    if has_authoritative:
        scan_layers.append("authoritative invokes (skill-graph.md + SKILL-INDEX.md)")

    return {
        "mode": mode,
        "mode_reason": mode_reason,
        "skill_count": skill_count,
        "code_dirs": code_dirs,
        "scan_layers": scan_layers,
    }


def print_build_plan(plan: dict) -> None:
    print(f"Auto mode: {plan['mode']}")
    print(f"Why: {plan['mode_reason']}")
    print("Scanning: " + " | ".join(plan["scan_layers"]))


def load_path_aliases(root: Path) -> dict[str, str]:
    aliases: dict[str, str] = {"@": "."}
    tsconfig = root / "tsconfig.json"
    if not tsconfig.is_file():
        return aliases
    for match in PATH_ALIAS_RE.finditer(_read(tsconfig)):
        alias, target = match.group(1), match.group(2).strip("./")
        aliases[alias] = target or "."
    return aliases


def _resolve_import_spec(root: Path, importer: Path, spec: str, path_aliases: dict[str, str]) -> Path | None:
    if not spec or spec.startswith("node:"):
        return None
    if not spec.startswith(".") and not spec.startswith("@") and "/" not in spec:
        return None

    base: Path | None = None
    if spec.startswith("."):
        base = (importer.parent / spec).resolve()
    elif spec.startswith("@"):
        for alias, target in sorted(path_aliases.items(), key=lambda item: -len(item[0])):
            if spec == alias or spec.startswith(f"{alias}/"):
                rest = spec[len(alias) :].lstrip("/")
                base = (root / target / rest).resolve()
                break
    else:
        base = (root / spec).resolve()

    if base is None:
        return None

    candidates = [
        base,
        base.with_suffix(".ts"),
        base.with_suffix(".tsx"),
        base.with_suffix(".js"),
        base.with_suffix(".jsx"),
        base / "index.ts",
        base / "index.tsx",
        base / "index.js",
    ]
    for candidate in candidates:
        try:
            candidate.relative_to(root)
        except ValueError:
            continue
        if candidate.is_file() and not _should_skip(candidate):
            return candidate
    return None


def _extract_ts_imports(text: str) -> list[str]:
    specs: list[str] = []
    for pattern in (TS_FROM_IMPORT_RE, TS_SIDE_IMPORT_RE, TS_REQUIRE_RE):
        specs.extend(pattern.findall(text))
    return specs


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


def scan_codebase(root: Path) -> tuple[dict[str, dict], list[dict]]:
    """Index all application source in the repo (repo-wide walk, not .agents-only)."""
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    path_aliases = load_path_aliases(root)
    files = iter_repo_source_files(root)

    for path in files:
        rel = _rel(root, path)
        community = rel.split("/")[0] if "/" in rel else "code"
        nid = _nid("module", rel)
        nodes[nid] = {
            "id": nid,
            "label": path.name,
            "type": "module",
            "path": rel,
            "community": community,
            "language": path.suffix.lstrip("."),
        }

    known = {_rel(root, p) for p in files}
    for path in files:
        rel = _rel(root, path)
        src = _nid("module", rel)
        text = _read(path)
        if path.suffix.lower() == ".py":
            for imp in PY_IMPORT_RE.findall(text):
                top = imp.split(".")[0]
                for candidate in known:
                    if candidate.replace("/", ".").startswith(top) or candidate.split("/")[0] == top:
                        edges.append(_edge(src, _nid("module", candidate), "imports", "EXTRACTED", 1.0, rel, "python-import"))
                        break
            continue

        for spec in _extract_ts_imports(text):
            resolved = _resolve_import_spec(root, path, spec, path_aliases)
            if resolved is None:
                continue
            tgt_rel = _rel(root, resolved)
            if tgt_rel in known:
                edges.append(_edge(src, _nid("module", tgt_rel), "imports", "EXTRACTED", 1.0, rel, "ts-import"))

    return nodes, edges


def scan_packages(root: Path) -> tuple[dict[str, dict], list[dict]]:
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    for pkg_json in root.rglob("package.json"):
        if _should_skip(pkg_json) or "node_modules" in pkg_json.parts:
            continue
        rel_dir = _rel(root, pkg_json.parent)
        if rel_dir.startswith(".agents/skills"):
            continue
        try:
            data = json.loads(_read(pkg_json))
        except json.JSONDecodeError:
            continue
        name = data.get("name") or rel_dir
        nid = _nid("package", name)
        nodes[nid] = {
            "id": nid,
            "label": name,
            "type": "package",
            "path": rel_dir,
            "community": "packages",
        }
        rel_pkg = _rel(root, pkg_json)
        for dep in list(data.get("dependencies", {}).keys()) + list(data.get("devDependencies", {}).keys()):
            if dep.startswith(".") or dep.startswith("file:"):
                continue
            edges.append(
                _edge(nid, _nid("package", dep), "depends_on", "EXTRACTED", 1.0, rel_pkg, "package.json")
            )
    return nodes, edges


def scan_config_and_agents(root: Path) -> tuple[dict[str, dict], list[dict]]:
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.name not in CONFIG_NAMES:
            continue
        if _should_skip(path):
            continue
        rel = _rel(root, path)
        if rel.startswith(".agents/skills/"):
            continue
        nid = _nid("config", rel)
        nodes[nid] = {
            "id": nid,
            "label": path.name,
            "type": "config",
            "path": rel,
            "community": "config",
        }
    agents = root / ".agents"
    if agents.is_dir():
        for path in agents.rglob("*.md"):
            if ".agents/skills" in str(path):
                continue
            rel = _rel(root, path)
            nid = _nid("config", rel)
            nodes[nid] = {
                "id": nid,
                "label": path.name,
                "type": "config",
                "path": rel,
                "community": "agents",
            }
    return nodes, edges


def scan_docs(root: Path, *, skill_library: bool = False) -> tuple[dict[str, dict], list[dict]]:
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    doc_paths: list[Path] = []

    for name in DOC_ROOT_FILES:
        path = root / name
        if path.is_file():
            doc_paths.append(path)

    docs_dir = root / "docs"
    if docs_dir.is_dir():
        for path in docs_dir.rglob("*.md"):
            if "knowledge-graph" in path.parts:
                continue
            doc_paths.append(path)

    for path in doc_paths:
        rel = _rel(root, path)
        community = "docs"
        if rel.startswith("docs/memory"):
            community = "memory"
        elif rel.startswith("docs/adr"):
            community = "decisions"
        nid = _nid("doc", rel)
        nodes[nid] = {"id": nid, "label": path.stem, "type": "doc", "path": rel, "community": community}
        if rel in DOC_MENTION_SKIP:
            continue
        if skill_library:
            # Routing is authoritative via docs/skill-graph.md + SKILL-INDEX; doc backticks are noise.
            continue
        text = _read(path)
        for skill in SKILL_TOKEN_RE.findall(text):
            if (root / ".agents/skills" / skill / "SKILL.md").exists():
                edges.append(_edge(nid, _nid("skill", skill), "mentions", "INFERRED", 0.75, rel, "doc-mention"))
        for module in re.findall(r"`([^`\s]+/[^`\s]+)`", text):
            if module.startswith(".agents/skills"):
                continue
            if (root / module).is_file() or (root / module).exists():
                edges.append(_edge(nid, _nid("module", module), "references", "INFERRED", 0.7, rel, "doc-path"))

    return nodes, edges


def scan_top_level_directories(root: Path) -> dict[str, dict]:
    nodes: dict[str, dict] = {}
    for path in sorted(root.iterdir()):
        if not path.is_dir() or path.name in SKIP_DIRS:
            continue
        if path.name.startswith(".") and path.name not in {".agents"}:
            continue
        rel = path.name
        nid = _nid("directory", rel)
        nodes[nid] = {"id": nid, "label": rel, "type": "directory", "path": rel, "community": "structure"}
    return nodes


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
        [(d, nodes[nid]["label"], nodes[nid]["type"]) for nid, d in degree.items() if nodes[nid]["type"] in ("skill", "module")],
        reverse=True,
    )
    return [f"{label} ({kind})" if kind == "module" else label for _, label, kind in ranked[:limit]]


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
        f"**Why this mode:** {graph.get('mode_reason', 'n/a')}",
        "",
        "## God nodes (skills + modules)",
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
        "",
        f"**Why this mode:** {graph.get('mode_reason', 'n/a')}",
        "",
        "**Scan layers:**",
    ]
    for layer in graph.get("scan_layers", []):
        lines.append(f"- {layer}")
    lines.extend(
        [
            "",
            f"EXTRACTED: {graph['stats'].get('extracted_edges', 0)} | INFERRED: {graph['stats'].get('inferred_edges', 0)}",
            "",
            "## Hub nodes",
        ]
    )
    for g in graph.get("god_nodes", [])[:8]:
        lines.append(f"- {g}")
    lines.extend(["", "## Communities", ""])
    for comm, members in sorted(graph.get("communities", {}).items()):
        lines.append(f"**{comm}** ({len(members)}): {', '.join(members[:10])}")
        if len(members) > 10:
            lines.append(f"  … +{len(members) - 10} more")
    lines.extend(["", "## Node types", ""])
    for kind, count in sorted(graph.get("stats", {}).get("node_types", {}).items()):
        lines.append(f"- **{kind}**: {count}")
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


def build_graph(root: Path, plan: dict | None = None) -> dict:
    if plan is None:
        plan = explain_build_plan(root)
    mode = plan["mode"]
    nodes: dict[str, dict] = {}
    edges: list[dict] = []

    def merge(ns: dict, es: list) -> None:
        nodes.update(ns)
        edges.extend(es)

    # Always index the full repository (never .agents/skills-only).
    merge(*scan_skills(root))
    merge(*scan_codebase(root))
    merge(*scan_packages(root))
    merge(*scan_config_and_agents(root))
    merge(*scan_docs(root, skill_library=(mode == "skill-library")))
    merge(*parse_memory_and_handoffs(root))
    nodes.update(scan_top_level_directories(root))

    # Authoritative skill invoke graph (agent-loom and other skill libraries).
    if mode == "skill-library":
        sg = root / "docs/skill-graph.md"
        if sg.exists():
            _, m_edges = parse_mermaid_call_graph(sg)
            edges.extend(m_edges)
        si = root / "docs/SKILL-INDEX.md"
        if si.exists():
            edges.extend(parse_skill_index_calls(si))
        edges.extend(security_gate_edges())
        if _nid("skill", "memory-handoff") in nodes and _nid("skill", "knowledge-graph") in nodes:
            edges.append(
                _edge(
                    _nid("skill", "memory-handoff"),
                    _nid("skill", "knowledge-graph"),
                    "invokes",
                    source="memory-checkpoint",
                )
            )

    deduped = dedupe_edges(edges, nodes)
    auth = sum(
        1
        for e in deduped
        if e.get("provenance") in ("skill-graph.md", "SKILL-INDEX.md", "security-chain", "memory-checkpoint")
    )
    extracted = sum(1 for e in deduped if e["confidence"] == "EXTRACTED")
    inferred = len(deduped) - extracted
    node_types: dict[str, int] = defaultdict(int)
    for n in nodes.values():
        node_types[n["type"]] += 1

    communities = detect_communities(nodes, deduped)
    gods = god_nodes(nodes, deduped)
    surprises = surprising_connections(nodes, deduped)
    questions = suggested_questions(surprises, gods)

    return {
        "version": "2.2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "mode_reason": plan["mode_reason"],
        "scan_layers": plan["scan_layers"],
        "root": str(root.resolve()),
        "stats": {
            "nodes": len(nodes),
            "edges": len(deduped),
            "authoritative_edges": auth,
            "extracted_edges": extracted,
            "inferred_edges": inferred,
            "node_types": dict(sorted(node_types.items())),
        },
        "god_nodes": gods,
        "surprising_connections": surprises,
        "suggested_questions": questions,
        "communities": communities,
        "nodes": list(nodes.values()),
        "edges": deduped,
    }


def verify_coverage(graph: dict, root: Path, strict: bool) -> int:
    """Reject skills-only graphs when application source exists on disk."""
    types = graph.get("stats", {}).get("node_types", {})
    modules = types.get("module", 0)
    source_files = iter_repo_source_files(root)
    source_count = len(source_files)

    if source_count > 0 and modules == 0:
        msg = (
            f"COVERAGE FAIL: {source_count} source file(s) on disk but 0 module nodes in graph — "
            "skills-only regression. Graph must map the whole repo, not just .agents/skills."
        )
        print(msg, file=sys.stderr)
        return 1 if strict else 0

    if source_count > 10 and modules < max(3, source_count // 20):
        print(
            f"COVERAGE WARN: {source_count} source files but only {modules} module nodes — "
            "import resolution may be thin; check tsconfig paths and extensions.",
            file=sys.stderr,
        )
    return 0


def _digest_inputs(root: Path, digest: "hashlib._Hash") -> None:
    def add_file(path: Path) -> None:
        if path.is_file():
            digest.update(path.read_bytes())

    def add_tree(base: Path, suffixes: set[str] | None = None) -> None:
        if not base.is_dir():
            return
        for path in sorted(base.rglob("*")):
            if not path.is_file() or _should_skip(path):
                continue
            if suffixes and path.suffix.lower() not in suffixes:
                continue
            digest.update(path.read_bytes())

    for name in DOC_ROOT_FILES:
        add_file(root / name)
    add_file(root / "docs/skill-graph.md")
    add_file(root / "docs/SKILL-INDEX.md")
    add_tree(root / "docs/memory", {".md"})
    add_tree(root / "docs", {".md"})
    add_tree(root / ".agents/skills", {".md"})
    add_tree(root / ".agents", {".md"})
    for path in iter_repo_source_files(root):
        digest.update(path.read_bytes())
    for name in CONFIG_NAMES:
        for path in root.rglob(name):
            if path.is_file() and not _should_skip(path):
                digest.update(path.read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--incremental", action="store_true", help="Skip if manifest unchanged")
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if source files exist but graph has 0 module nodes (skills-only regression)",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    out = root / OUT_DIR
    out.mkdir(parents=True, exist_ok=True)

    manifest_path = out / MANIFEST_FILE
    digest = hashlib.sha256()
    _digest_inputs(root, digest)
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

    plan = explain_build_plan(root)
    print_build_plan(plan)
    graph = build_graph(root, plan)
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
    types = graph["stats"].get("node_types", {})
    types_str = ", ".join(f"{k}={v}" for k, v in sorted(types.items()))
    print(f"Done: {gp} — {new_count} nodes, {graph['stats']['edges']} edges, mode={graph['mode']}")
    if types_str:
        print(f"Node types: {types_str}")
    cov = verify_coverage(graph, root, args.strict)
    if cov != 0:
        return cov
    return 0


if __name__ == "__main__":
    sys.exit(main())

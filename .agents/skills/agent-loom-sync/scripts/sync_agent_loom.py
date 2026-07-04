#!/usr/bin/env python3
"""Sync library skills from agent-loom upstream; preserve project-local skills. Stdlib only."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

CONFIG_NAME = "agent-loom-sync.json"
DEFAULT_UPSTREAM = "../agent-loom"
SKIP_DIRS = {".deprecated", "__pycache__", ".DS_Store"}
ORIGIN_RE = re.compile(r"^\s+origin:\s*project-local\s*$", re.MULTILINE)
_ORIGIN_SCRIPT = (
    Path(__file__).resolve().parents[2]
    / "universal-skill-creator"
    / "scripts"
    / "project_local_origin.py"
)


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def _dir_hash(path: Path) -> str:
    h = hashlib.sha256()
    for f in sorted(path.rglob("*")):
        if not f.is_file():
            continue
        if any(s in f.parts for s in SKIP_DIRS):
            continue
        rel = str(f.relative_to(path))
        h.update(rel.encode())
        h.update(f.read_bytes())
    return h.hexdigest()[:16]


def list_skills(skills_dir: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    if not skills_dir.is_dir():
        return out
    for d in sorted(skills_dir.iterdir()):
        if not d.is_dir() or d.name in SKIP_DIRS or d.name.startswith("."):
            continue
        if (d / "SKILL.md").is_file():
            out[d.name] = d
    return out


def is_project_local(skill_dir: Path) -> bool:
    sm = skill_dir / "SKILL.md"
    if not sm.is_file():
        return False
    return bool(ORIGIN_RE.search(_read(sm)))


def load_config(agents_dir: Path) -> dict:
    cfg_path = agents_dir / CONFIG_NAME
    if cfg_path.is_file():
        return json.loads(_read(cfg_path))
    return {
        "upstream": DEFAULT_UPSTREAM,
        "protected_skills": [],
        "forked_skills": {},
    }


def save_config(agents_dir: Path, cfg: dict) -> None:
    cfg_path = agents_dir / CONFIG_NAME
    cfg_path.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")


def upstream_commit(upstream: Path) -> str:
    try:
        r = subprocess.run(
            ["git", "-C", str(upstream), "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return r.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def rsync_skill(src: Path, dst: Path, dry_run: bool) -> list[str]:
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "rsync",
        "-a",
        "--delete",
        "--exclude",
        "__pycache__/",
        "--exclude",
        ".DS_Store",
    ]
    if dry_run:
        cmd.append("--dry-run")
    cmd.extend([f"{src}/", f"{dst}/"])
    r = subprocess.run(cmd, capture_output=True, text=True)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()]
    if r.returncode != 0:
        raise RuntimeError(f"rsync failed for {src.name}: {r.stderr.strip()}")
    return lines


def rsync_hooks(upstream: Path, project_root: Path, dry_run: bool) -> list[str]:
    src = upstream / "hooks"
    dst = project_root / "hooks"
    if not src.is_dir():
        return []
    dst.mkdir(parents=True, exist_ok=True)
    cmd = ["rsync", "-a", "--exclude", "__pycache__/", "--exclude", ".DS_Store"]
    if dry_run:
        cmd.append("--dry-run")
    cmd.extend([f"{src}/", f"{dst}/"])
    r = subprocess.run(cmd, capture_output=True, text=True)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()]
    if r.returncode != 0:
        raise RuntimeError(f"rsync hooks failed: {r.stderr.strip()}")
    return lines


def build_plan(project_root: Path, upstream_rel: str) -> dict:
    agents = project_root / ".agents"
    skills = agents / "skills"
    upstream = (project_root / upstream_rel).resolve()
    cfg = load_config(agents)

    if not upstream.is_dir():
        raise FileNotFoundError(f"Upstream not found: {upstream}")
    up_skills = list_skills(upstream / ".agents" / "skills")
    local_skills = list_skills(skills)

    protected = set(cfg.get("protected_skills", []))
    protected |= {n for n, p in local_skills.items() if n not in up_skills}
    protected |= {n for n, p in local_skills.items() if is_project_local(p)}
    protected |= set(cfg.get("forked_skills", {}).keys())

    forked: dict[str, str] = {}
    update: list[str] = []
    add: list[str] = []
    unchanged: list[str] = []

    for name, up_path in sorted(up_skills.items()):
        if name in protected:
            continue
        local_path = skills / name
        if name not in local_skills:
            add.append(name)
            continue
        if _dir_hash(up_path) == _dir_hash(local_path):
            unchanged.append(name)
            continue
        if name in cfg.get("forked_skills", {}):
            forked[name] = "listed in forked_skills — skipped"
            continue
        if is_project_local(local_path):
            forked[name] = "metadata.origin: project-local"
            continue
        update.append(name)

    local_only = sorted(set(local_skills) - set(up_skills))
    hooks_present = (upstream / "hooks").is_dir()

    return {
        "upstream": str(upstream),
        "upstream_rel": upstream_rel,
        "upstream_commit": upstream_commit(upstream),
        "protected": sorted(protected),
        "local_only": local_only,
        "add": add,
        "update": update,
        "unchanged": unchanged,
        "forked": forked,
        "hooks_sync": hooks_present,
        "config": cfg,
    }


def apply_plan(project_root: Path, plan: dict, dry_run: bool) -> dict:
    upstream = Path(plan["upstream"])
    skills = project_root / ".agents" / "skills"
    applied: list[str] = []
    rsync_log: dict[str, list[str]] = {}

    for name in plan["add"] + plan["update"]:
        src = upstream / ".agents" / "skills" / name
        dst = skills / name
        rsync_log[name] = rsync_skill(src, dst, dry_run=dry_run)
        applied.append(name)

    hooks_log: list[str] = []
    if plan.get("hooks_sync"):
        hooks_log = rsync_hooks(upstream, project_root, dry_run=dry_run)

    return {"applied": applied, "rsync_log": rsync_log, "hooks_log": hooks_log}


def stamp_local_only_skills(project_root: Path, upstream: Path, *, dry_run: bool) -> list[str]:
    """Auto-stamp metadata.origin on skills not present upstream."""
    if not _ORIGIN_SCRIPT.is_file():
        return []
    sys.path.insert(0, str(_ORIGIN_SCRIPT.parent))
    from project_local_origin import stamp_local_only  # noqa: PLC0415

    up_names = set(list_skills(upstream / ".agents" / "skills").keys())
    return stamp_local_only(project_root, up_names, dry_run=dry_run)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync agent-loom library skills into project .agents/")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--upstream", type=str, default=None, help="Path to agent-loom repo (default from config or ../agent-loom)")
    parser.add_argument("--dry-run", action="store_true", help="Show plan only")
    parser.add_argument("--apply", action="store_true", help="Execute rsync")
    parser.add_argument("--json", action="store_true", help="Machine-readable plan output")
    args = parser.parse_args()

    root = args.root.resolve()
    agents = root / ".agents"
    cfg = load_config(agents)
    upstream_rel = args.upstream or cfg.get("upstream", DEFAULT_UPSTREAM)

    try:
        plan = build_plan(root, upstream_rel)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(plan, indent=2))
        return 0

    print(f"Upstream: {plan['upstream']} @ {plan['upstream_commit']}")
    if plan.get("hooks_sync"):
        print("Hooks: hooks/ will sync from upstream")
    print(f"Add ({len(plan['add'])}): {', '.join(plan['add']) or '—'}")
    print(f"Update ({len(plan['update'])}): {', '.join(plan['update']) or '—'}")
    print(f"Unchanged ({len(plan['unchanged'])}): {len(plan['unchanged'])} skills")
    print(f"Local-only protected ({len(plan['local_only'])}): {', '.join(plan['local_only']) or '—'}")
    if plan["forked"]:
        print(f"Forked/skipped ({len(plan['forked'])}):")
        for k, v in sorted(plan["forked"].items()):
            print(f"  {k}: {v}")

    if args.dry_run and not args.apply:
        result = apply_plan(root, plan, dry_run=True)
        if result["rsync_log"]:
            print("\nDry-run rsync preview:")
            for name, lines in result["rsync_log"].items():
                print(f"  [{name}] {len(lines)} changes")
        return 0

    if not args.apply:
        print("\nPass --apply to execute (or --dry-run for rsync preview).")
        return 0

    result = apply_plan(root, plan, dry_run=False)
    stamped = stamp_local_only_skills(root, Path(plan["upstream"]), dry_run=False)
    if stamped:
        result["stamped"] = stamped
    cfg = plan["config"]
    cfg["upstream"] = upstream_rel
    cfg["last_sync"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    cfg["upstream_commit"] = plan["upstream_commit"]
    cfg["protected_skills"] = sorted(
        set(cfg.get("protected_skills", [])) | set(plan["local_only"])
    )
    save_config(root / ".agents", cfg)

    print(f"\nApplied: {len(result['applied'])} skills")
    if result.get("stamped"):
        print(f"Auto-stamped origin:project-local on {len(result['stamped'])} local-only skills")
        print(f"  {', '.join(result['stamped'])}")
    print(f"Config updated: .agents/{CONFIG_NAME}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

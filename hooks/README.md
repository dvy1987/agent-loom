# Agent-Loom Hooks

Optional **Claude Code** hooks adapted from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (MIT). Copy this `hooks/` directory to your project root when you copy `.agents/` from agent-loom.

| Hook | Use with skill | Docs |
|------|----------------|------|
| `simplify-ignore.sh` | `code-simplification` | [SIMPLIFY-IGNORE.md](SIMPLIFY-IGNORE.md) |
| `sdd-cache-pre.sh` + `sdd-cache-post.sh` | `research-skill`, `learn-from-*`, `source-driven-development` | [SDD-CACHE.md](SDD-CACHE.md) |

**Cross-platform (no Claude hooks):** use `python3 .agents/skills/research-skill/scripts/doc_cache.py <url>` — same ETag revalidation contract, cache at `.agents/cache/doc-fetch/`.

**`.gitignore` entries:** `.claude/.simplify-ignore-cache/`, `.claude/sdd-cache/`, `.agents/cache/doc-fetch/`

**Sync:** `agent-loom-sync` copies `hooks/` from upstream when present.

# Deferred Items

Parked enhancements with rationale. **Reopen only when the listed trigger fires or the user requests it.**

## Status at a glance (2026-07-05)

| # | Item | Status |
|---|------|--------|
| 10 | Native `.claude/commands/` + `.gemini/commands/` adapters | **OPEN** — only active deferral |
| 11 | `simplify-ignore.sh` annotation hiding | **DONE** 2026-07-04 — do not surface as parked |
| 12 | HTTP ETag doc fetch cache | **DONE** 2026-07-04 — do not surface as parked |

**Agents:** In session-start summaries, list **only #10** under deferred items (if any). Never report #11 or #12 as parked — they shipped.

---

## Implemented (moved from deferral — historical)

### #11 — Annotation-based code hiding (`simplify-ignore.sh`) — **DONE 2026-07-04**
**Location:** `hooks/simplify-ignore.sh`, `hooks/SIMPLIFY-IGNORE.md`, `code-simplification` → `references/simplify-ignore.md`  
**Source:** addyosmani/agent-skills (MIT), adapted for agent-loom `code-simplification`.

### #12 — HTTP ETag doc fetch cache — **DONE 2026-07-04**
**Location:** `hooks/sdd-cache-{pre,post}.sh`, `hooks/SDD-CACHE.md`, `research-skill/scripts/doc_cache.py`, `research-skill/references/doc-cache.md`  
**Source:** addyosmani/agent-skills (MIT). Claude hooks + cross-platform Python CLI.

---

## Open deferrals

### #10 — Native `.claude/commands/` and `.gemini/commands/` adapters
**Source:** addyosmani Insight #10 — Multi-harness parity: same command set in `.claude/commands/*.md`, `.gemini/commands/*.toml`, `AGENTS.md`, and per-tool docs.  
**Why deferred:** We already publish cross-platform via `install.sh` / `install.ps1`. Native command adapters would simplify per-tool UX but require a new generator pipeline and per-tool argument-mapping logic.  
**Trigger to reopen:** First user request "I want native Claude slash commands for these skills" OR a second sister project reports tool-specific routing friction.  
**Cost estimate:** ~1–2 sessions of `install.sh` rework + one template generator per tool.

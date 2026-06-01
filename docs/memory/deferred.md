# Deferred Items

Parked enhancements with rationale. Reopen only when the listed trigger fires or the user requests it.

---

## 2026-05-31 — From `addyosmani/agent-skills` ingestion (Phase 1 application)

### #10 — Native `.claude/commands/` and `.gemini/commands/` adapters
**Source:** addyosmani Insight #10 — Multi-harness parity: same command set in `.claude/commands/*.md`, `.gemini/commands/*.toml`, `AGENTS.md`, and per-tool docs.
**Why deferred:** We already publish cross-platform via `install.sh` / `install.ps1`. Native command adapters would simplify per-tool UX but require a new generator pipeline and per-tool argument-mapping logic.
**Trigger to reopen:** First user request "I want native Claude slash commands for these skills" OR a second sister project reports tool-specific routing friction.
**Cost estimate:** ~1–2 sessions of `install.sh` rework + one template generator per tool.

### #11 — Annotation-based code hiding (`simplify-ignore.sh`)
**Source:** addyosmani Insight #11 — `/* simplify-ignore-start */…end */` blocks hashed before model reads file, re-expanded after edits.
**Why deferred:** This is application-code refactoring infrastructure, not skill-library work. We have no code-simplification skill in scope today.
**Trigger to reopen:** Building an `apply-paper-to-project` extension that needs to compress noisy generated code (e.g., scaffolding, vendored deps) before model ingestion.
**Cost estimate:** Greenfield — depends on parent skill design.

### #12 — HTTP ETag / `Last-Modified` revalidation cache for doc fetches
**Source:** addyosmani Insight #12 — `sdd-cache-{pre,post}.sh` revalidates even cached docs on every use.
**Why deferred:** High value for `research-skill` and `learn-from-paper` / `learn-from-article` / `learn-from-repo` — we re-fetch the same arXiv pages, READMEs, and blog posts often. Implementation requires a hook layer we do not have (no `pre-skill-run` / `post-skill-run` mechanism in the current loader).
**Trigger to reopen:** Either (a) adopting a skill runner that exposes pre/post hooks, OR (b) repeated user complaints about slow ingestion of unchanged remote sources, OR (c) someone observes a stale arXiv abstract being applied to a skill.
**Cost estimate:** ~1 session if hook infrastructure exists; ~3 sessions if hooks must be designed first.

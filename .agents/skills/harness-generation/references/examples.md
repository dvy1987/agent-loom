# Harness Generation — Examples

## Ex.1 — Consumer repo after project-setup

**Input:** React monorepo; `AGENTS.md` exists (142 lines) from project-setup interview.

**Actions:**
- Inventory: `package.json` scripts, `.agents/skills/` with 12 skills, no `docs/harness/`.
- Create manifest v0 with 7 components; mark `AGENTS.md` as `user-edited`, merge harness pointer only.
- Create `docs/harness/eval-interface.md` stub pointing to `npm test`.
- Create `docs/harness/governance.md` with forbidden paths from Boundaries section.

**Output manifest snippet:**
```json
{ "harness_version": "v0", "components": [
  { "id": "prompt", "path": "AGENTS.md", "status": "user-edited" },
  { "id": "skills", "path": ".agents/skills/", "status": "generated" }
]}
```

---

## Ex.2 — agent-loom library project

**Input:** This repo — skill library, no per-project harness yet.

**Actions:**
- Manifest lists skill routing via `AGENTS.md` + `docs/SKILL-INDEX.md` as read-only refs.
- Eval stub points to `validate-skills` local run as harness regression proxy.
- Governance: never write SKILL.md outside `universal-skill-creator`.

**Next:** `eval-pipeline` for skill-quality regression on harness edits.

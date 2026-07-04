# Project Setup — Full Worked Examples

Adapted for agent-loom AGENTS.md generation workflow.

---

## Example 1 — PM, non-technical owner

**Input:** "Set up agents. React Native habit tracker. Weak on architecture, testing, security."

**Interview (abbreviated):**
- Role: PM | Done: shipped feature = tested build + store screenshot
- Gaps: security, testing, architecture → skill-finder maps `app-security-hardening`, `test-driven-development`, `api-and-interface-design`

**Output:** `owner_mode: non-technical`. AGENTS.md with Agent-Led Architecture block, Session Lifecycle, Orchestration Map (brainstorming → feature-spec → TDD). Step 6b: `build_graph.py` if knowledge-graph installed. Rubric 13/14. 134 lines.

---

## Example 2 — Engineer, SDD project

**Input:** "Specs-first monorepo, frontend + backend"

**Detection:** `docs/specs/` exists → `sdd_mode: on`, skip SDD question. `agents_md_mode: multi` → root + `frontend/AGENTS.md` + `backend/AGENTS.md`.

**Orchestration:** constitution → feature-spec → plan → crosscheck → implement.

---

## Example 3 — Commands auto-extracted

**Input:** User doesn't know test command

**Silent scan:** `package.json` scripts → present "Run `npm test` — confirm?" in Step 2. Never ask for info in manifest.

---

## Example 4 — Update mode

**Input:** `UPDATE_ONLY=true` after new ADR bans direct DB access

**Action:** Edit only Boundaries + Non-Obvious Patterns in AGENTS.md; preserve User Context and Session Lifecycle.

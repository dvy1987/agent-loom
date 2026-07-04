# Codebase Understanding — Full Worked Examples

Adapted for agent-loom architecture doc output + knowledge-graph Step 0.

---

## Example 1 — Graph-first scan

**Input:** "Map the auth flow"

**Step 0:** `query_graph.py query "auth session middleware"` → seed paths: `src/auth/`, `memory: agent-handoffs` mention.

**Output tags:** EXTRACTED (from graph invokes) vs INFERRED (from grep) vs AMBIGUOUS (needs file read).

---

## Example 2 — Architecture doc excerpt

```markdown
## Layer: API
- `src/routes/auth.ts` — login, refresh [EXTRACTED: read file]
- Data flow: Client → auth.middleware → UserService → Prisma [INFERRED: verify in Step 3]

## Hotspot
- `UserService.ts` — 480 lines, no tests [EXTRACTED]
```

---

## Example 3 — Scope refusal

**Input:** "Understand entire 200k LOC monorepo in one pass"

**Output:** Propose bounded scope — one vertical slice or one directory — with graph seeds.

---

## Example 4 — Consumer project (application mode)

No skill-library graph → map `src/`, `docs/`, `docs/memory/` modules; tag INFERRED imports.

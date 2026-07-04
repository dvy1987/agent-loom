# Memory Startup — Full Worked Examples

Source: addyosmani/agent-skills anti-rationalization patterns + agent-loom session lifecycle.

---

## Example 1 — Bare "hi" (cold start)

**Input:** `hi`

```markdown
Working context loaded:
- Project: agent-loom skill library (98 skills)
- Last handoff: 2026-07-03 knowledge-graph v2
- Git: main, clean, synced with origin
- Next: [awaiting user direction]
Graph: 120 nodes — hubs: universal-skill-creator, validate-skills
```

Fires memory-startup — content of greeting irrelevant.

---

## Example 2 — Explicit skip

**Input:** "fresh start — ignore prior context"

**Output:** `Fresh start acknowledged — memory skipped.` No handoff read.

---

## Example 3 — Mid-session no-op

**Input:** Second message in same thread after context loaded

**Output:** `Context already loaded — no-op`

---

## Example 4 — Stale graph enforcement (Step 3.5)

Handoff dated 2026-07-03, graph dated 2026-07-01 → run `build_graph.py --incremental` before relational work.

---

## Example 5 — Rationalization defense

| Excuse | Reality |
|---|---|
| "User said hi, not a task" | Hi = session start; load memory |
| "Graph optional" | When installed, freshness is mandatory |

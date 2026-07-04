# Memory Compact — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Bloated handoff log

**Input:** `agent-handoffs.md` exceeds 200 entries

**Agent actions:**
1. Archive entries older than 90 days to `docs/memory/archived/handoffs-2026-H1.md`.
2. Leave index row: `archived: handoffs 2026-01..06`.
3. Preserve latest 20 handoffs in active file.

---

## Example 2 — Merge duplicate decisions

**Input:** Same JWT decision captured 4 times in session-notes

**Output:** Single `decision-log.md` entry; session-notes get one-line redirect stubs.

---

## Example 3 — Pre-audit compaction

**Input:** User runs `memory-audit` on large repo

**Output:** Recommend `memory-compact` first to shrink audit surface.

---

## Example 4 — Global budget pressure

**Input:** `~/.agent-loom/memories/` over active line budget

**Output:** Archive low-signal entries; preserve decisions + provenance links.

---

## Example 5 — Handoff calls compact

**Input:** `memory-handoff` detects repetitive handoffs

**Output:** Handoff recommends `memory-compact` in Next Agent section before appending another near-duplicate entry.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome

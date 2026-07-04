# Compress Skill — Worked Examples

Read when applying compression or verifying EXAMPLE overflow handling.

---

## Example 1 — prd-writing (354 → 115 lines)

**Input:** "Compress `.agents/skills/prd-writing/SKILL.md` — it's 354 lines"

**Classification:**
- CORE: hard gates, gotchas — stay
- WORKFLOW: 9 steps — compress to one-liners
- FORMAT: 3 schemas — stay, trim prose
- EXAMPLE: 2 pairs — keep shorter inline; **move second here**
- BACKGROUND: "Why PRDs matter" → `references/background.md`
- DUPLICATE: quality standards repeats workflow — delete

**Moved example (was second inline):**
```
Input: "Write a PRD for user notifications"
Output: [full PRD schema with FR/NFR/ACs — 40 lines]
```

**SKILL.md after:**
- Inline: one short PRD teaser (8 lines)
- Pointer: `Read references/examples.md` when user needs a full PRD sample shape
- `metadata.resources.references`: add `examples.md`

**Regression:** all 5 checks passed. Split gate: not needed (117 lines after moves).

---

## Example 2 — EXAMPLE-only overflow

**Input:** Skill at 215 lines; only excess is 3 long `<examples>` blocks

**Action:**
1. Keep shortest example inline (dark-mode one-liner)
2. Move examples 2–3 to this file
3. Add resources + load trigger
4. Do **not** delete any example content

**Never valid:** deleting examples to hit 200 lines without L3 home.

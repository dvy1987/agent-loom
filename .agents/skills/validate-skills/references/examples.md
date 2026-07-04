# Validate Skills — Full Report Examples

Read when you need a complete health-report shape beyond the inline teaser in SKILL.md.

---

## Example 1 — Full library pass

**Input:** "validate all skills"

**Output:**
```
Skill Library Health Report | 2026-07-03 | Skills: 98
VALIDATION: ✓ 98/98
LOADER SAFETY (P0): ✓ all desc ≤1024, no BOM
DESCRIPTION (P1): ⚠ learn-from: contains "Step 1" in description — move steps to body
SIZE: ⚠ project-setup: 201 lines (fix: compress-skill; move examples to references/)
SCORES:
  brainstorming 13/14 — examples only inline; backfill references/examples.md
  prd-writing 12/14 — only 1 gotcha
  universal-skill-creator 14/14
  validate-skills 13/14 — L3 examples present
CRAFT (P2):
  memory-recall: missing Verification checklist
  knowledge-graph: ok
GRAPH (4d): PASS — 0 P0, 0 P1
STRUCTURAL:
  feature-spec: producer missing memory-checkpoint → memory-capture
DUPLICATE TRIGGERS: eval-output + eval-judge: overlap on "score this response"
ACTIONS:
  P1 project-setup: 201 lines — compress-skill (move EXAMPLE to references/examples.md)
  P2 brainstorming: backfill references/examples.md
  P2 prd-writing: add 2 gotchas
  P2 memory-recall: add Verification section
  P3 eval-judge: narrow description triggers
```

---

## Example 2 — Pre-flight for improve-skills

**Input:** "pre-flight check before improving debug-and-fix"

**Output:**
```
Skill Library Health Report | 2026-07-03 | Skills: 1 (scoped)
VALIDATION: ✓ debug-and-fix
SCORES: debug-and-fix 11/14 — weak Examples (truncated), strong Gotchas
CRAFT (P2): has Common Rationalizations ✓ | Verification ✓ | L3 examples: missing
ACTIONS:
  P2 debug-and-fix: create references/examples.md with 2 full debug sessions
  P2 debug-and-fix: Examples criterion 1/2 — backfill before improve-skills cycle
Pre-flight verdict: PROCEED with example backfill recommended
```

---

## Example 3 — Graph audit finding (Step 4d)

**Input:** "check skill health" (agent-loom with knowledge-graph)

**Output fragment:**
```
GRAPH (4d): WARN
  P1 stale-graph: graph_date 2026-07-01, latest_handoff 2026-07-03
  P2 high-inferred-ratio: 0.72 — rebuild from docs/skill-graph.md
ACTIONS:
  P1 run: python3 .agents/skills/knowledge-graph/scripts/build_graph.py --incremental
```

---

## Scoring reminder

Full 0/1/2 rubric: `references/validation-rubric.md`. Examples criterion:
- **2/2** — ≥1 complete inline OR inline teaser + `references/examples.md` with ≥2 full pairs
- **1/2** — truncated inline only
- **0/2** — no examples

# Improve Skills — Full Worked Examples

Skill: `improve-skills` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Improve all skills in the repo

**Output:**
```
Pre-flight validate-skills report:
  brainstorming: 10/14 | structural: missing Prune Log (>30 days)
  prd-writing: 9/14 | structural: none
  research-skill: 12/14 | structural: none
Queue confirmed (all skills, lowest score first).

1b Chat learnings: 4 OPEN → 1 queued (prd-writing), 2 pre-existing, 1 deferred.
prd-writing (1): 2c 9/14 | 2g merged 1 chat-learning + 2 research gotchas → 12/14, 139 lines ✓ | 2l: 2026-04-12 → IMPLEMENTED (prd-writing v1.3)
brainstorming (2): Prune Log added; 13/14; 170 lines ✓
Summary: 2 skills improved (+3 avg); chat-learnings: 4 OPEN → 1 impl · 2 pre-existing · 1 deferred
```

## Example 2 — Step-by-step execution

**Input:** "Run `improve-skills` on [concrete task]"

**Agent actions:**
1. Pre-flight via validate-skills
2. Ingest Chat Learnings
3. Per-Skill Improvement Cycle
4. Cross-Link Repair
5. Library Summary

**Impact Report shape:**
```
Improvement cycle complete: YYYY-MM-DD
Skills processed: N
Skills improved: N (avg score delta: +N pts)
Structural gaps fixed: N (list by skill)
New skill links created: N (list relationships)
Skills deprecated: N | split: N | compressed: N

Per-skill: [skill]: X/14 → Y/14 | [lines] lines | [key change]
Sources: [source] → [skill]
Chat learnings: N OPEN at start → I implemented · R rejected · D deferred
Files modified: [list] | L3 backfill: [list]
```

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "Skip validate pre-flight" | Improving blind wastes cycles on already-healthy skills. |
| "Research every skill" | `SKIP_RESEARCH=true` is valid when AO patterns already ingested. |
| "One skill is enough" | Batch structural gaps compound library quality. |
| "Delete examples to fit lines" | Relocate to L3 — never discard examples. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Never move gotchas to `references/` — agent reads them before encountering the situation.
- Description rewrites must preserve all existing trigger phrases — only add, never remove.
- Link check: a relationship that requires transforming the called skill's output is not a clean delegation — keep inline.
- Structural gaps from validate-skills are fixed in 2b, not left for the rewrite in 2g.

---

See `SKILL.md` for hard rules and verification checklist.

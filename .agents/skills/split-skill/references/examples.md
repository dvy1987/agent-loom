# Split Skill — Full Worked Examples

Skill: `split-skill` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** improve-skills is 220 lines — the link check section is CORE but takes 15 lines

**Output:**
```
Sub-capability: scan library for delegation opportunities
Existing skill match: validate-skills checks call graph but does NOT recommend new links — different job, cannot cover this without scope creep.
Duplication: not found in other skills.
Action: Type A extract → new child "link-check"

improve-skills: 220 → 198 lines ✓ | link-check: 140 lines (new) ✓
```

## Example 2 — Step-by-step execution

**Input:** "Run `split-skill` on [concrete task]"

**Agent actions:**
1. Identify the Excess Sub-Capability
2. Check Existing Skills First (before creating anything)
3. Execute the Chosen Action
4. Update the Parent Skill
5. Verify Line Counts
6. Update All Callers (Type B only)
7. Update AGENTS.md
8. Regression Check

**Impact Report shape:**
```
Action taken: [linked to existing <skill> / extracted new <child> / Type B]
Parent: [before] → [after] lines
Child/linked skill: [name] — [lines] lines ([new / existing])
Other callers updated: [list or "none"]
AGENTS.md updated: yes
Regression check: all capabilities preserved
agentskills validate: ✓
Files created: [list or "none — linked to existing"]
Files modified: [parent SKILL.md, AGENTS.md, any updated callers]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Always check existing skills before creating a new one — link or marginally adapt first.
- Marginal adaptation of a target skill is allowed only if: stays under 200 lines, core purpose unchanged, existing callers unaffected. If any condition fails — create a new child instead.
- Never split a step that needs context from adjacent steps — it's a pipeline stage, not a sub-capability.
- Child description must work standalone — other skills or users may invoke it directly.

---

See `SKILL.md` for hard rules and verification checklist.

# Compress Skill — Full Worked Examples

Skill: `compress-skill` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Compress .agents/skills/prd-writing/SKILL.md — it's 354 lines

**Output:**
```
prd-writing: 354 lines

Classification:
- CORE: hard gates, gotchas — 12 lines — stay
- WORKFLOW: 9 steps — stay, compress prose — 45 lines
- FORMAT: 3 schemas — stay, remove surrounding explanation — 60 lines
- EXAMPLE: 2 examples — keep shorter inline, move second to references/examples.md
- BACKGROUND: "Why PRDs matter", tips section — move to references/background.md
- DUPLICATE: quality standards repeats workflow — delete

Split gate: BACKGROUND moved, remaining = 117 lines — under 200, no split needed.

Regression check: all 5 criteria passed ✓
Result: 354 → 115 lines (67% reduction)
```

## Example 2 — Step-by-step execution

**Input:** "Run `compress-skill` on [concrete task]"

**Agent actions:**
1. Measure
2. Classify Every Block
3. Split Decision Gate
4. Apply Compression Transforms
5. Regression Check
6. Validate and Commit

**Impact Report shape:**
```
Compression complete: [skill-name]
Lines: [before] → [after] ([N]% reduction)
Moved to references/: [list of files created]
Regression check: [all 5 passed / N failed — restored]
agentskills validate: ✓
Files modified: SKILL.md[, references/background.md, references/examples.md]
```

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "Split is safer" | Split when capability is separable; compress when it's one workflow. |
| "Line count doesn't matter" | Loaders and routers choke on bloated skills. |
| "Can't lose any words" | Relocate examples to L3 — never delete them. |
| "Compress secure-* skills" | Security skills are split-only — compression removes threat rows. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **`secure-*` skills are uncompressable.** Threshold is 180 lines and the only allowed action is `split-skill`. Compression silently removes threat coverage.
- **Description compression loses triggers silently.** Always test the compressed description against ≥3 sample prompts that activated the original — phrasing changes that drop a trigger word kill routing.
- **"Move to references/" without a load trigger is invisible.** Every referenced file MUST be referenced from SKILL.md with a specific load condition, or the agent will never read it.
- **Imperative one-liners ≠ removing context.** Compressing "Ask at least 2 clarifying questions before writing the spec" to "Ask questions" loses the gate. Preserve numbers, thresholds, and MUST/NEVER verbs.

---

See `SKILL.md` for hard rules and verification checklist.

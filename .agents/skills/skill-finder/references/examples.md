# Skill Finder — Full Worked Examples

Skill: `skill-finder` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Find a skill for: "evaluate whether a process decomposition is well-structured"

**Output:**
```
Scanned 46 skills in library. Closest matches:
- `validate-skills` — validates skill quality, not process quality (no overlap)
- `code-review-crsp` — reviews code, not process entries (no overlap)

No existing skill handles process/architecture evaluation. Recommending: create new skill `setup-evaluation`.
```

## Example 2 — Documented workflow

**Input:** Find a skill for: "create a system prompt for an agent"

**Output:**
```
Scanned 46 skills. Match found:
- `create-agent-prompt` — creates role prompts for agents in multi-agent topologies (partial overlap — covers role prompts but not system prompts)

Extending `create-agent-prompt` to include system prompt generation. Verifying line count stays <=200.
```

## Example 3 — Step-by-step execution

**Input:** "Run `skill-finder` on [concrete task]"

**Agent actions:**
1. Read Current Library
2. Compare Against Request
3. Extend or Create
4. Sync Indexes
5. Return Result

**Impact Report shape:**
```
Skill lookup complete for: [capability description]
Action: existing | extended | created
Skill name: [name]
Library size: [N] skills (before → after if changed)
Index synced: yes/no
```

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- A skill with a similar name but different purpose is NOT a match — read the full description.
- "Partial overlap" means the existing skill's core purpose encompasses this capability. If it's a tangential addition, create a new skill instead.
- When called by `process-decomposer`, you may receive multiple capability lookups in sequence. Process each independently — batch decisions cause mismatches.
- 

---

See `SKILL.md` for hard rules and verification checklist.

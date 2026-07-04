# Skill Finder — Full Worked Examples

Skill: `skill-finder` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Find a skill for: "evaluate whether a process decomposition is well-structured"

**Output:**
```
Scanned 46 skills in library. Closest matches:
- `validate-skills` — validates skill quality, not process quality (no overlap)
- `code-review-crsp` — reviews code, not process entries (no overlap)

No existing skill handles process/architecture evaluation. Recommending: create new skill `setup-evaluation`.
```

## Example 2 — From skill workflow

**Input:** Find a skill for: "create a system prompt for an agent"

**Output:**
```
Scanned 46 skills. Match found:
- `create-agent-prompt` — creates role prompts for agents in multi-agent topologies (partial overlap — covers role prompts but not system prompts)

Extending `create-agent-prompt` to include system prompt generation. Verifying line count stays <=200.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.

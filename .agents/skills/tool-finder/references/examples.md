# Tool Finder — Full Worked Examples

Skill: `tool-finder` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Find a tool for: "search the web for recent research papers"

**Output:**
```
Tool: WebSearch
Category: Web search
Status: available (agent built-in)
No setup needed.
```

## Example 2 — Documented workflow

**Input:** Find a tool for: "query a PostgreSQL database"

**Output:**
```
Tool: PostgreSQL MCP server
Category: MCP server
Status: needs-setup
Setup: Configure `mcp__postgres` in your MCP settings with connection string. See: https://github.com/modelcontextprotocol/servers/tree/main/src/postgres
```

## Example 3 — Step-by-step execution

**Input:** "Run `tool-finder` on [concrete task]"

**Agent actions:**
1. Categorise Tool Need
2. Check Availability
3. Return Result

**Impact Report shape:**
```
Tool lookup complete for: [requirement]
Tool: [name]
Status: available | needs-setup | unavailable
Platform: [current platform]
```

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Agent built-in tools (Read, Write, Grep, Bash) are ALWAYS available — don't waste time checking.
- MCP server availability varies by platform — what works in Claude Code may not work in Codex.
- A tool being installed globally doesn't mean it's available in the agent's sandbox.
- When called in batch by `process-decomposer`, deduplicate — don't check the same tool twice.

---

See `SKILL.md` for hard rules and verification checklist.
